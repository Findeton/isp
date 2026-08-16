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
Sec.11).  FIVE code regions, disjoint by machine check at G-S1-DISJOINT-CODE:
  b_*   THE BUILDER       -- the declared arena, the committed corpus, the
                             declared dynamics; the only region that may name a
                             declared-side constant;
  s_*   THE STRIPPER      -- the eraser that emits bare record bytes;
  r_*   THE RECONSTRUCTOR -- reads bare bytes and nothing else, ever;
  k_*   THE COMPARATOR    -- decides agreement and rebuilds the verdict; calls
                             no builder, no stripper and no reconstructor;
  the unprefixed PLUMBING -- digests, i/o, gates, rendering.  It is not policed
                             for reach, and the reach audit is transitive
                             THROUGH it, so a reconstructor that reaches a
                             builder by way of plumbing is still an offence.
Three legs answer the family, not one: the transitive reach audit; an
ALIAS leg that forbids globals()/getattr/sys.modules/importlib/eval/exec and
builder-name string constants inside any r_*/s_*/k_* subtree; and a
DECLARED-CONSTANT leg that forbids naming any member of DECLARED_CONSTANTS
there.  The reconstructor is shown to HAVE TEETH: it refuses four of the nine
declared generating mechanisms, and the comparator rebuilds the head from the
serialized receipt alone.

TEMPLATE.  The nine E-25...E-33 families are imported from
v14/code/era_template.py and USED, not copied: every family's entry point is
COUNTED AT THE CALL SITE in the mode being delivered, and G-TEMPLATE-EXERCISED
gates the execution census -- not a regex over this file's own source.

EXACTNESS.  Python integers and fractions.Fraction only.  No float appears
anywhere; an AST scan of this module and a recursive type walk of the receipt
are gates.

CLI (#82).  --run | --no-write | --selftest | --list-gates | --list-mutants
            | --mutant NAME | --render
--render is the paper-free diagnostic: it fires every gate whose object is the
payload, skips exactly the four whose object is the paper, writes nothing, and
exits 4 so that no exit-code-only harness can score it as a delivery.
The argv whitelist is STRICT AT EVERY POSITION: --mutant takes exactly one
operand and every other flag takes none, so `--run --mutant NAME` exits 2.
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
    "v15/PLAN.md": "754e075c4a0e",
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


def b_amplitudes():
    """the declared amplitudes the screening measurement is taken at.  The
    first is the uniform one the head is stamped to; the rest are the state
    space's own corners, so that the two legs of the screening theorem can be
    told apart (K2 MAJOR-3)."""
    single = [B_Z0] * DIM
    single[0] = B_Z1
    one_direction = [B_Z1 if k % len(DECLARED_LINKS) == 0 else B_Z0
                     for k in range(DIM)]
    alternating = [B_Z1 if k % 2 == 0 else B_WPOW[1] for k in range(DIM)]
    return (("THE-UNIFORM-AMPLITUDE", tuple([B_Z1] * DIM)),
            ("A-SINGLE-CELL-AMPLITUDE", tuple(single)),
            ("ONE-LINK-DIRECTION-ONLY", tuple(one_direction)),
            ("ALTERNATING-ROOTS", tuple(alternating)),
            ("THE-ZERO-AMPLITUDE", tuple([B_Z0] * DIM)))


def b_screening_at(psi, fields):
    """one screening measurement at one amplitude: the successors, the two
    residue legs, and both readings' menus."""
    succ = {}
    for n in fields:
        succ[n] = b_walk_step(list(psi), list(n))
    same = agree = diff = cross = 0
    for a, b in combinations(fields, 2):
        ra = tuple(v % B_Q for v in a)
        rb = tuple(v % B_Q for v in b)
        if ra == rb:
            same += 1
            if succ[a] == succ[b]:
                agree += 1
        else:
            diff += 1
            if succ[a] == succ[b]:
                cross += 1
    return {"successors": len({succ[n] for n in fields}),
            "equal_residue_pairs": same, "equal_residue_agreements": agree,
            "distinct_residue_pairs": diff, "distinct_residue_collisions": cross,
            "born_menus": len({b_born_menu(succ[n][1]) for n in fields}),
            "post_coin_vectors": len({succ[n][1] for n in fields})}


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
S_MULT_SECOND, S_ADD_SECOND = 7, 4        # a second, unrelated token naming


def s_coordinate(mult, add, tokens):
    """the emitted naming of the record's tokens.  `tokens` is handed in by
    the caller: the eraser is told how many tokens it is renaming and names no
    declared-side constant itself (S-1's declared-constant leg)."""
    return {k: (mult * k + add) % tokens for k in range(tokens)}


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


def r_direction_splittings(adj, pairs, arity):
    """the ways the reconstructed link structure splits into disjoint spans,
    each class a spanning union of cliques of the size the RECORD's own blocks
    have.  `arity` is that measured block size, handed in by the caller; this
    region names no declared-side constant.  The record offers these and
    prefers none."""
    toks = sorted(pairs)
    n = len(adj)
    tok_of = {frozenset(p): t for t, p in pairs.items()}
    # a candidate class is a partition of the actors into cliques of the size
    # the record's blocks have; its tokens are the edges those cliques carry.
    tri = [c for c in combinations(range(n), arity)
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
    spans = []
    for P in parts:
        toks_here = frozenset(tok_of[frozenset(e)]
                              for c in P for e in combinations(c, 2))
        spans.append(toks_here)
    spans = sorted(set(spans), key=sorted)
    splits = set()
    if spans:
        # how many spans a splitting takes is READ OFF the record: every
        # candidate class carries the same number of tokens, so the count is
        # the token total divided by that width.  (Writing the arity here
        # would be an a = 3 coincidence, K1 m7's species.)
        widths = {len(c) for c in spans}
        if len(widths) == 1 and len(toks) % len(spans[0]) == 0:
            per = len(toks) // len(spans[0])
            for tri in combinations(spans, per):
                if len(set().union(*tri)) == len(toks):
                    splits.add(frozenset(tri))
    return len(spans), splits


def r_block_components(blocks):
    """the number of connected components of the record's block hypergraph.
    The representation-class search offers each token after the first only one
    fresh label, which is exhaustive exactly when this count is one."""
    seen, comps = set(), 0
    bof = collections.defaultdict(list)
    for bi, b in enumerate(blocks):
        for t in b:
            bof[t].append(bi)
    for t0 in sorted({t for b in blocks for t in b}):
        if t0 in seen:
            continue
        comps += 1
        stack = [t0]
        while stack:
            t = stack.pop()
            if t in seen:
                continue
            seen.add(t)
            for bi in bof[t]:
                stack.extend(u for u in blocks[bi] if u not in seen)
    return comps


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


def k_parse_head(segment):
    """the verdict's own numerals, parsed back out of the emitted string by a
    reader that shares no code and no literal with the builder.  EVERY
    numeral position is returned, including the second half of a compound
    `A-OF-B` value, which the first reader stopped at the hyphen and never
    saw."""
    out = {}
    for m in re.finditer(
            r"([A-Z0-9\-]+)=([0-9][0-9,]*)(?:-OF-([0-9][0-9,]*))?", segment):
        vals = [int(m.group(2).replace(",", ""))]
        if m.group(3) is not None:
            vals.append(int(m.group(3).replace(",", "")))
        out[m.group(1)] = tuple(vals)
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

# Every declared-side constant this module carries.  Only the builder may name
# one; the stripper, the reconstructor and the comparator may not, and
# G-S1-DISJOINT-CODE's third leg enforces it CASE-INSENSITIVELY (K3 MAJOR-4:
# `region_of` is case-sensitive, so `B_ARITY` read as plumbing).
DECLARED_CONSTANTS = frozenset((
    "B_Q", "B_DIMENSION", "B_ARITY", "B_ROUNDS", "B_WPOW", "B_GROVER",
    "B_SHIFT", "B_Z0", "B_Z1", "B_COLLINEAR_FLAT", "B_COMMITTED_R4",
    "B_SEEDS_PER_ROUND", "SITES", "SITE_INDEX", "NACT", "DECLARED_LINKS",
    "CLASS_NAMES", "CLASS_DIR", "UNDECLARED_CLASS", "CLASSES", "CELLS",
    "CELL_INDEX", "DIM", "S_MULT", "S_ADD",
))

# The routes by which a region can reach another without leaving a call edge
# or a bare Name for the graph to see (K3 MAJOR-4, INJ-01).
ALIAS_ROUTES = ("globals", "getattr", "vars", "eval", "exec", "compile",
                "sys.modules", "importlib", "__import__", "locals")


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
    """LEG 1 -- no reconstructor and no comparator may REACH a builder or a
    stripper at any depth, transitively THROUGH the unpoliced plumbing."""
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


def _region_subtrees(src, regions):
    tree = ast.parse(src)
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and region_of(node.name) in regions:
            yield node


def audit_alias_routes(src):
    """LEG 2 -- inside any stripper, reconstructor or comparator, the routes
    that reach a function WITHOUT leaving a call edge are forbidden outright:
    name assembly through globals()/getattr()/sys.modules/importlib, eval and
    exec, and any string constant spelling a builder's or a stripper's name."""
    offences = []
    for node in _region_subtrees(src, ("stripper", "reconstructor",
                                       "comparator")):
        for sub in ast.walk(node):
            nm = None
            if isinstance(sub, ast.Call):
                nm = getattr(sub.func, "id", None)
                if nm is None and isinstance(sub.func, ast.Attribute):
                    root = sub.func
                    while isinstance(root, ast.Attribute):
                        root = root.value
                    if isinstance(root, ast.Name):
                        nm = "%s.%s" % (root.id, sub.func.attr)
            elif isinstance(sub, ast.Attribute):
                root = sub.value
                if isinstance(root, ast.Name):
                    nm = "%s.%s" % (root.id, sub.attr)
            elif isinstance(sub, ast.Name):
                nm = sub.id
            if nm and nm in ALIAS_ROUTES:
                offences.append("%s uses the alias route %s at line %d"
                                % (node.name, nm, getattr(sub, "lineno", 0)))
            if isinstance(sub, ast.Constant) and isinstance(sub.value, str):
                if re.fullmatch(r"(?:b_|s_)\w+", sub.value):
                    offences.append("%s spells the name %r at line %d"
                                    % (node.name, sub.value, sub.lineno))
    return offences


def audit_declared_constants(src):
    """LEG 3 -- only the builder may name a declared-side constant.  The test
    is case-insensitive, so a shouted constant cannot slip through the
    prefix map (K3 MAJOR-4)."""
    lowered = {c.casefold() for c in DECLARED_CONSTANTS}
    offences = []
    for node in _region_subtrees(src, ("stripper", "reconstructor",
                                       "comparator")):
        for sub in ast.walk(node):
            if isinstance(sub, ast.Name) and sub.id.casefold() in lowered:
                offences.append("%s names the declared constant %s at line %d"
                                % (node.name, sub.id, sub.lineno))
    return offences


def region_census(src):
    g = module_call_graph(src)
    return collections.Counter(region_of(n) for n in g)


def receipt_type_walk(obj, bad, path="$"):
    """returns the number of LEAVES visited, so that the count the gate
    publishes is the walk's own and not a typed zero (K3 MAJOR-8)."""
    if isinstance(obj, float):
        bad.append(path)
        return 1
    if isinstance(obj, bool) or isinstance(obj, int) or obj is None \
            or isinstance(obj, str):
        return 1
    if isinstance(obj, dict):
        return sum(receipt_type_walk(v, bad, path + "." + str(k))
                   for k, v in obj.items())
    if isinstance(obj, (list, tuple)):
        return sum(receipt_type_walk(v, bad, path + "[%d]" % i)
                   for i, v in enumerate(obj))
    bad.append(path + ":" + type(obj).__name__)
    return 1


# ===========================================================================
# SECTION E.  THE MEASUREMENT.  Every published value is produced here, once,
# and every gate below is a predicate over this payload and nothing else.
# ===========================================================================

CLASS_ALPHABET = ("PRIMITIVE", "DECLARED", "GENERATED", "RECONSTRUCTED",
                  "LAW-SELECTED")
# NONE is in the alphabet because a row whose declared backing the run cannot
# resolve MUST be able to read NONE -- that is what makes CENSUS-PARTIAL a
# reachable word at this corpus rather than an unfalsifiable one (K2 MAJOR-5c).
BACKING_ALPHABET = ("COMPUTED-HERE", "SEALED-CITATION", "NONE")

# the declared prefix lengths of the Q58 domain probe; each is gated to lie
# strictly below the measured covering prefix, so each fails to cover.
DOMAIN_PREFIXES = (4, 8, 12, 16, 20, 22)


def measure():
    R: dict = {}
    corp, parts, strict, flatq, scheds, smeta = b_build_corpus()
    pi = s_coordinate(S_MULT, S_ADD, DIM)
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
    # the carrier typing, MEASURED rather than asserted: the cell is the
    # unordered co-division pair, and the map is a bijection (K1's m2 check).
    R["arena_codivision_pairs"] = len({b_codivision_pair(c) for c in CELLS})
    R["arena_cell_pair_bijection"] = (R["arena_codivision_pairs"] == DIM)
    R["arena_groupings"] = len(parts)
    R["arena_saturating_groupings"] = len(b_raw_census()["sat"])
    # K1 m7: `sum(round_vec) == n` is an a = 3 coincidence of the idiom -- the
    # general identity is (n/a)*C(a,2) = n only at a = 3.  What the law says
    # structurally is that EVERY GROUP IS A TRIANGLE, and the two are measured
    # against each other here so that the coincidence is not reused as a
    # formula by a unit at another arity.
    _parts = b_raw_census()["parts"]
    _tri = [i for i, P_ in enumerate(_parts)
            if all(len(b_cell_footprint(frozenset(g))) == B_ARITY for g in P_)]
    R["arena_saturating_all_triangles"] = (
        sorted(_tri) == sorted(b_raw_census()["sat"]))
    R["arena_all_triangle_groupings"] = len(_tri)
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
    # The screening theorem is measured AT EVERY DECLARED AMPLITUDE, because
    # its two legs part company: sufficiency is structural and minimality is
    # amplitude-relative (K2 MAJOR-3).  The head is stamped to the first.
    amps = b_amplitudes()
    sweep = [(name, b_screening_at(list(psi), fields)) for name, psi in amps]
    R["state_amplitudes_probed"] = len(sweep)
    R["state_amplitude_rows"] = [
        [name, s["successors"], s["equal_residue_agreements"],
         s["equal_residue_pairs"], s["distinct_residue_collisions"],
         s["distinct_residue_pairs"], s["born_menus"], s["post_coin_vectors"]]
        for name, s in sweep]
    R["state_amplitudes_sufficient"] = sum(
        1 for _n, s in sweep
        if s["equal_residue_agreements"] == s["equal_residue_pairs"])
    R["state_amplitudes_minimal"] = sum(
        1 for _n, s in sweep if s["distinct_residue_collisions"] == 0)
    here = sweep[0][1]
    R["state_amplitude_stamped"] = sweep[0][0]
    R["state_successors_distinct"] = here["successors"]
    R["state_equal_residue_pairs"] = here["equal_residue_pairs"]
    R["state_equal_residue_agreements"] = here["equal_residue_agreements"]
    R["state_equal_residue_disagreements"] = (
        here["equal_residue_pairs"] - here["equal_residue_agreements"])
    R["state_distinct_residue_pairs"] = here["distinct_residue_pairs"]
    R["state_distinct_residue_collisions"] = here["distinct_residue_collisions"]
    single = [s for n, s in sweep if n == "A-SINGLE-CELL-AMPLITUDE"][0]
    R["state_single_cell_collisions"] = single["distinct_residue_collisions"]
    R["state_single_cell_pairs"] = single["distinct_residue_pairs"]
    # reading A's menu is the BORN menu -- the post-coin weights, not the
    # post-coin vectors (K1 M3).  Both are published; they are not the same
    # quantity and the row that names one may not print the other.
    R["state_reading_a_born_values"] = here["born_menus"]
    R["state_reading_a_post_coin_vectors"] = here["post_coin_vectors"]
    R["state_reading_a_menus"] = here["post_coin_vectors"]
    R["state_reading_b_menus"] = len({b_record_menu(n) for n in fields})
    R["state_reading_b_menus_on_residues"] = len(
        {b_record_menu(tuple(v % B_Q for v in n)) for n in fields})
    R["state_components"] = 2
    R["state_ensemble_components"] = 1
    R["state_background_components"] = 6

    # ---- the reconstruction and the gauge -------------------------------
    cert, cast, theta = r_reconstruct(blocks)
    R["recon_certificate"] = cert
    R["recon_threshold"] = theta
    R["recon_cast_size"] = len(cast)
    R["recon_actor_size"] = max(len(a) for a in cast)
    declared_moved = frozenset(frozenset(pi[c] for c in v) for v in DA.values())
    R["recon_set_equality"] = k_set_equal(cast, declared_moved)
    # the coordinate priced, not asserted: the record is re-emitted in a second,
    # unrelated naming of its tokens and the reconstruction is run again.
    pi2 = s_coordinate(S_MULT_SECOND, S_ADD_SECOND, DIM)
    blocks2 = s_bare_blocks(corp, pi2)
    cert2, cast2, _th2 = r_reconstruct(blocks2)
    R["recon_second_coordinate_certificate"] = cert2
    R["recon_coordinate_invariant"] = k_set_equal(
        cast2, frozenset(frozenset(pi2[c] for c in v) for v in DA.values()))
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
    # the arity the SPLITTING search uses is read off the record's own blocks,
    # never off the declaration.
    blk_arity = R["record_block_sizes"][0]
    R["recon_block_arity"] = blk_arity
    nclasses, splits = r_direction_splittings(adj, dpairs, blk_arity)
    R["inv_candidate_direction_classes"] = nclasses
    R["inv_direction_splittings"] = len(splits)
    declared_split = frozenset(
        frozenset(t for t in range(DIM) if _preimage(pi, t) % B_ARITY == d)
        for d in range(B_ARITY))
    R["inv_declared_splitting_offered"] = declared_split in splits
    # FOUND (K1 F1).  The two twelves are the same twelve by orbit-stabilizer:
    # Aut(link) acts on the splittings, the action is TRANSITIVE, and the
    # stabilizer of the declared splitting is the arena group ITSELF.
    # the action is taken in the DECLARED labelling, where the arena group and
    # the link group live, so that the stabilizer can be compared with the
    # arena group as a SET of permutations and not only by order.
    tok_pair = {pi[k]: frozenset(PAIRS[k]) for k in range(DIM)}
    idx_of = {}
    for t, p in tok_pair.items():
        idx_of.setdefault(p, t)

    def split_image(sp, perm):
        out = set()
        for cls in sp:
            moved = set()
            for t in cls:
                a, b = sorted(tok_pair[t])
                moved.add(idx_of[frozenset((perm[a], perm[b]))])
            out.add(frozenset(moved))
        return frozenset(out)
    # the same measurement restricted to ONE declared direction class: three
    # disjoint triangles, which offer exactly one splitting.  This is the
    # corpus-derived witness that the residue-one verdict word is reachable.
    one_class = sorted(sorted(declared_split, key=sorted)[0])
    sub_pairs = {t: dpairs[t] for t in one_class}
    sub_adj = {i: set() for i in range(len(members))}
    for _t, pr in sub_pairs.items():
        a, b = sorted(pr)
        sub_adj[a].add(b)
        sub_adj[b].add(a)
    n_one, s_one = r_direction_splittings(sub_adj, sub_pairs, blk_arity)
    R["inv_single_class_candidate_classes"] = n_one
    R["inv_single_class_splittings"] = len(s_one)
    orbit = {split_image(declared_split, p) for p in autos_site}
    stab_split = [p for p in autos_site
                  if split_image(declared_split, p) == declared_split]
    R["inv_splitting_orbit"] = len(orbit)
    R["inv_splitting_action_transitive"] = (orbit == splits)
    R["inv_splitting_stabilizer"] = len(stab_split)
    R["inv_splitting_stabilizer_is_the_arena_group"] = (
        {tuple(p) for p in stab_split}
        == {tuple(p) for p in b_arena_automorphisms()})
    R["inv_orbit_stabilizer_identity"] = (
        len(orbit) * len(stab_split) == len(autos_site))

    # the law's own stabilizer in the symmetric group
    admissible_groups = {frozenset(SITE_INDEX[x] for x in g)
                         for i in b_raw_census()["sat"] for g in parts[i]}
    stab = group_set_stabilizer(NACT, B_ARITY, admissible_groups)
    R["inv_admissible_groups"] = len(admissible_groups)
    R["inv_law_stabilizer"] = len(stab)
    R["inv_law_blind_to_direction"] = (len(stab) == len(autos))
    # FOUND (K1 F2 / K2 minor 3).  Not an order coincidence: the two groups
    # are EQUAL AS SETS of permutations of the nine actors, and the link graph
    # is complete multipartite, so the order is the closed form as well.
    R["inv_law_stabilizer_is_the_link_group"] = (
        {tuple(p) for p in stab} == {tuple(p) for p in autos_site})
    R["inv_arena_group_inside_the_link_group"] = (
        {tuple(p) for p in b_arena_automorphisms()}
        <= {tuple(p) for p in autos_site})
    parts_of_the_multipartition = collections.defaultdict(set)
    for a in range(NACT):
        parts_of_the_multipartition[
            frozenset(b for b in range(NACT) if b != a and b not in adj_site[a])
            | {a}].add(a)
    R["inv_link_graph_parts"] = len(parts_of_the_multipartition)
    R["inv_link_graph_part_sizes"] = sorted(
        len(v) for v in parts_of_the_multipartition.values())
    closed = 1
    for sz in R["inv_link_graph_part_sizes"]:
        closed *= _factorial(sz)
    closed *= _factorial(R["inv_link_graph_parts"])
    R["inv_link_graph_closed_form"] = closed

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

    # Each event is named by its index in the SORTED list of all actor groups
    # of the declared arity, a list the relabellings permute among themselves.
    # Index order is event order, so comparing index tuples is comparing event
    # tuples: the orbit counts below are the same numbers a direct image would
    # give, at a fraction of the work.
    all_events = [tuple(c) for c in combinations(range(NACT), B_ARITY)]
    ev_index = {e: i for i, e in enumerate(all_events)}
    hist_ids = [tuple(ev_index[tuple(sorted(SITE_INDEX[x] for x in F))]
                      for F in H) for H in hist]

    def perm_table(p):
        return tuple(ev_index[tuple(sorted(p[i] for i in e))]
                     for e in all_events)
    AUTA_T = [perm_table(p) for p in AUTA]
    AUTL_T = [perm_table(p) for p in AUTL]
    ident_T = perm_table(tuple(range(NACT)))

    def hkeep(Hid, t):
        """the ORDER-PRESERVING image: a history is a sequence, and this map
        keeps it one."""
        return tuple(t[i] for i in Hid)

    def himg(Hid, t):
        """the image AFTER the order is forgotten -- a different object, and
        the census row must say so (K1 M2)."""
        return tuple(sorted(t[i] for i in Hid))

    def fimg(n, p):
        d = {}
        for k in range(DIM):
            d[tuple(sorted(p[i] for i in PAIRS[k]))] = n[k]
        return tuple(v for _k, v in sorted(d.items()))
    R["quotient_histories"] = len(hist)
    # the three-step chain, with the step the group does NOT do published
    # first: sorting the events is not a group action.
    R["quotient_history_event_multisets"] = len(
        {himg(Hid, ident_T) for Hid in hist_ids})
    R["quotient_histories_arena"] = len(
        {min(himg(Hid, t) for t in AUTA_T) for Hid in hist_ids})
    R["quotient_histories_link"] = len(
        {min(himg(Hid, t) for t in AUTL_T) for Hid in hist_ids})
    R["quotient_histories_ordered_arena"] = len(
        {min(hkeep(Hid, t) for t in AUTA_T) for Hid in hist_ids})
    R["quotient_histories_ordered_link"] = len(
        {min(hkeep(Hid, t) for t in AUTL_T) for Hid in hist_ids})
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
    # the search's own precondition, gated rather than assumed (K1 m8): the
    # one-fresh-label menu is complete only if the record's block hypergraph
    # is connected, so the number of components is measured and gated.
    R["class_blocks_components"] = r_block_components(blocks)
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
    # THE GRAIN THE RECONSTRUCTOR ACTUALLY READS (K1 M1).  r_reconstruct is
    # handed a block set and nothing else, so the probe's width is the number
    # of DISTINCT block sets the nine arms supply, not the number of arms.
    record_id, seen_sets = {}, {}
    for name, _k, _a, bl in ARMS:
        key = frozenset(bl)
        if key not in seen_sets:
            seen_sets[key] = "RECORD-%d" % (len(seen_sets) + 1)
        record_id[name] = seen_sets[key]
    for name, kind, arity, bl in ARMS:
        c, ca, th = r_reconstruct(bl)
        arms.append({"arm": name, "mechanism": kind, "event_arity": arity,
                     "record": record_id[name],
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
    R["q58_distinct_inputs"] = len(seen_sets)
    R["q58_distinct_recovering_inputs"] = len(
        {a["record"] for a in arms if a["cast_recovered"]})
    R["q58_distinct_refusing_inputs"] = len(
        {a["record"] for a in arms if not a["cast_recovered"]})
    R["q58_records"] = sorted({a["record"] for a in arms})
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
    # the two refusals are not one refusal (K2 minor 7): at two arms the rule
    # RAN and its own membership certificate rejected the cast it built; at
    # two the rule DECLINED, because the record carries no co-writing at all.
    R["q58_arms_certificate_rejected"] = sum(
        1 for a in arms if a["certificate"] == "TOKEN-NOT-IN-EXACTLY-TWO")
    R["q58_arms_declined"] = sum(
        1 for a in arms if a["certificate"] == "THRESHOLD-UNDETERMINED")

    # ---- Q58, the DOMAIN probe: is the criterion sufficient off the arms? --
    # The arms decide the arms.  This family asks whether triangularity with
    # total cover is a property of MECHANISMS, and measures that it is not.
    tri_sorted = sorted(set(triangles))
    pair_sorted = sorted(set(pairs_only))
    cover, k_cover = set(), 0
    while len(cover) < DIM and k_cover < len(tri_sorted):
        cover |= set(tri_sorted[k_cover])
        k_cover += 1
    dom = [("all the triangles", tri_sorted),
           ("the smallest covering prefix", tri_sorted[:k_cover])]
    for label, d in (("the first", 0), ("a middle", len(tri_sorted) // 2),
                     ("the last", len(tri_sorted) - 1)):
        dom.append(("the triangles less %s block" % label,
                    tri_sorted[:d] + tri_sorted[d + 1:]))
    for k in DOMAIN_PREFIXES:
        dom.append(("a prefix of %s triangles" % com(k), tri_sorted[:k]))
    dom.append(("the triangles and one two-cell block",
                tri_sorted + [pair_sorted[0]]))
    probes = []
    for label, bl in dom:
        c, ca, _t = r_reconstruct(bl)
        probes.append({"probe": label, "blocks": len(bl),
                       "all_blocks_triangular": all(is_triangle(b) for b in bl),
                       "tokens_covered": len({t for b in bl for t in b}),
                       "certificate": c,
                       "cast_recovered": bool(ca == declared_moved)})
    R["q58_domain_probes"] = probes
    R["q58_domain_probe_count"] = len(probes)
    R["q58_domain_covering_prefix"] = k_cover
    R["q58_domain_prefixes_below_the_cover"] = sum(
        1 for k in DOMAIN_PREFIXES if k < k_cover)
    R["q58_domain_prefixes_declared"] = len(DOMAIN_PREFIXES)
    R["q58_domain_triangular_failures"] = sum(
        1 for p in probes if p["all_blocks_triangular"] and not p["cast_recovered"])
    R["q58_domain_failures_at_total_cover"] = sum(
        1 for p in probes if p["all_blocks_triangular"]
        and not p["cast_recovered"] and p["tokens_covered"] == DIM)
    R["q58_domain_nontriangular_recovering"] = sum(
        1 for p in probes if not p["all_blocks_triangular"] and p["cast_recovered"])
    # the two quantifiers the sealed sentence used to carry, MEASURED:
    R["q58_criterion_holds_on_every_triangle_writer"] = (
        R["q58_domain_triangular_failures"] == 0)
    R["q58_criterion_refuses_every_non_triangle_writer"] = (
        R["q58_domain_nontriangular_recovering"] == 0)

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
    # the three selection laws, MEASURED here rather than typed in the table
    R["coin_phase_group_order"] = len(B_WPOW)
    R["param_law_cell_count"] = (
        R["arena_cells"] == R["arena_sites"] * R["arena_declared_directions"])
    R["param_law_connection"] = (
        R["coin_phase_group_order"] == R["arena_field_order"])
    R["param_law_menu"] = (R["arena_menu"] == R["arena_translation_subgroups"])
    R["param_law_actor_count_conditional"] = (
        R["class_cast_matches_declared"] and R["q58_arms_refusing"] > 0)
    R["inv_direction_blind"] = (
        R["inv_direction_profiles_agreeing"] == R["inv_direction_choices"])
    rows = parameter_rows(R)
    R["param_rows"] = rows
    R["param_total"] = len(rows)
    R["param_free"] = sum(1 for p in rows if p[3] == "FREE")
    R["param_invariant"] = sum(
        1 for p in rows if p[3] == "INVARIANT-IN-THE-SUBSTRATE-CENSUS")
    R["param_derived"] = sum(1 for p in rows if p[3] == "DERIVED")
    R["param_reconstructed"] = sum(
        1 for p in rows if p[3] == "RECONSTRUCTED-CONDITIONALLY")
    R["param_initial"] = sum(1 for p in rows if p[3] == "INITIAL")
    R["param_selected_by_a_law"] = sum(1 for p in rows if p[4] == "YES")
    R["param_free_selected_by_a_law"] = sum(
        1 for p in rows if p[3] == "FREE" and p[4] == "YES")
    R["param_class_predicates"] = sum(
        len(v) for v in PARAM_CLASS_PREDICATE.values() if v)
    R["param_class_predicate_failures"] = sorted(
        "%s :: %s" % (nm, key)
        for cls, mapping in PARAM_CLASS_PREDICATE.items() if mapping
        for nm, key in mapping.items() if not R.get(key))
    R["param_laws_declared"] = sum(
        1 for p in PARAMETER_SPEC if p[4] is not None)
    R["param_laws_satisfied"] = sum(
        1 for p in PARAMETER_SPEC if p[4] is not None and bool(R.get(p[4])))

    return R


def census_payload(P, anchors):
    """the census, taken AFTER the anchors are located so that every cited
    cardinality is PARSED OUT OF THE LOCATED TEXT rather than typed here."""
    chart = anchor_numerals(anchors.read("SEC-CHART", "G-OBJECT-CENSUS"))
    carrier = anchor_numerals(anchors.read("REC-CARRIER", "G-OBJECT-CENSUS"))
    tick = anchor_spelled_numerals(anchors.read("HOR-TICK", "G-OBJECT-CENSUS"))
    P["cited_gluings"] = chart[0]
    P["cited_chart_types"] = chart[-1]
    P["cited_carrier_cells"] = carrier[0]
    P["cited_tick_sites"] = tick[0]
    P["cited_numeral_sources"] = len({"SEC-CHART", "REC-CARRIER", "HOR-TICK"})
    P["census_rows"] = census_rows(P)
    P["census_row_count"] = len(P["census_rows"])
    P["census_backed"] = sum(1 for r in P["census_rows"]
                             if r["backing"] != "NONE")
    P["census_computed_here"] = sum(1 for r in P["census_rows"]
                                    if r["backing"] == "COMPUTED-HERE")
    P["census_cited"] = sum(1 for r in P["census_rows"]
                            if r["backing"] == "SEALED-CITATION")
    P["census_unbacked"] = sum(1 for r in P["census_rows"]
                               if r["backing"] == "NONE")
    P["census_classes"] = sorted(collections.Counter(
        r["class"] for r in P["census_rows"]).items())
    P["census_primitive"] = sum(1 for r in P["census_rows"]
                                if r["class"] == "PRIMITIVE")
    P["census_class_words"] = len(CLASS_ALPHABET)
    P["census_backing_words"] = len(BACKING_ALPHABET)
    P["census_distinct_extents"] = len({r["extent"] for r in P["census_rows"]})
    P["census_identifications"] = (P["census_row_count"]
                                   - P["census_distinct_extents"])
    # the census and the parameter table reconciled: no object the census
    # classes DECLARED may go unpriced in section six (K2 MAJOR-5a).
    priced = {p[0] for p in PARAMETER_SPEC}
    P["census_declared_objects"] = sorted(
        r["object"] for r in P["census_rows"] if r["class"] == "DECLARED")
    P["param_declared_objects_unpriced"] = sum(
        1 for o in P["census_declared_objects"]
        if CENSUS_DECLARED_TO_PARAMETER.get(o) not in priced)
    return P


# every object the census classes DECLARED, and the row of section six that
# prices it
CENSUS_DECLARED_TO_PARAMETER = {
    "ACTOR": "n", "SITE": "n", "DIRECTION": "L", "QUANTUM-STATE": "the state",
    "COIN": "the coin", "SEAM": "the seam", "CHART": "the chart",
    "TICK": "the tick", "CARRIER-CANDIDATE": "the cell count",
}


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
    ("RECORD-BLOCK", "ACTOR", "the reconstruction reads a cast off the blocks"),
)

# Every declaration the corpus makes, INCLUDING the two the object census
# classes DECLARED and the first delivery did not price (K2 MAJOR-5a).  The
# fifth field is the PAYLOAD KEY of the measured predicate that selects the
# row -- None where the corpus has measured no such law -- so the class and
# the selection column are computed from a measurement and not typed (#295,
# K2 MAJOR-5b).  A row is DERIVED exactly when its predicate holds.
PARAMETER_SPEC = (
    ("d", "the spatial dimension", "UNSWEPT", "FREE", None, "NDEP"),
    ("q", "the field order", "SWEPT-AT-THREE-POINTS", "FREE", None, "NDEP"),
    ("a", "the division-event arity", "UNSWEPT", "FREE", None,
     "ARITY-CHARTERED"),
    ("R", "the depth in rounds", "SWEPT-ALONG-THE-LADDER", "FREE", None,
     "PERR"),
    ("the window", "the driven schedule set", "DECLARED-WINDOW", "FREE", None,
     "R4DEC"),
    ("the coin", "the S_3-covariant unitary", "COMPUTED-HERE", "FREE", None,
     "COUPLING"),
    ("the coin order", "coin before or after the residue", "DECLARED-PAIR",
     "FREE", None, "COUPLING"),
    ("the orientation", "the sign of the shift", "DECLARED-PAIR", "FREE",
     None, "COUPLING"),
    ("the horizon", "the number of coupled steps", "DECLARED", "FREE", None,
     "COUPLING"),
    ("the reading", "the Born menu or the record menu", "DECLARED-PAIR",
     "FREE", None, "COUPLING"),
    ("the seam", "the completion at a shared site", "COMPUTED-HERE", "FREE",
     None, "SEC-2"),
    ("the ceiling", "the occupancy ceiling", "DECLARED", "FREE", None, "OCC"),
    ("the measure", "the measure over configurations", "A-SIMPLEX", "FREE",
     None, "R5M"),
    ("the tick", "the scheduling convention", "DECLARED", "FREE", None, "HOR"),
    ("the chart", "the two-sector overlap type", "SEALED-CITATION", "FREE",
     None, "SEC"),
    ("L", "which classes are declared links", "COMPUTED-HERE",
     "INVARIANT-IN-THE-SUBSTRATE-CENSUS", None, "AID"),
    ("the coordinate", "the naming of the record tokens", "ANY-BIJECTION",
     "INVARIANT-IN-THE-SUBSTRATE-CENSUS", None, "REC"),
    ("n", "the actor count", "COMPUTED-HERE", "RECONSTRUCTED-CONDITIONALLY",
     None, "THIS-UNIT"),
    ("the cell count", "the carrier size", "COMPUTED-HERE", "DERIVED",
     "param_law_cell_count", "THIS-UNIT"),
    ("the connection", "the group the walk's phases live in", "DECLARED",
     "DERIVED", "param_law_connection", "COUPLING"),
    ("the menu", "the admissible actor grains", "COMPUTED-HERE", "DERIVED",
     "param_law_menu", "FAC"),
    ("the state", "the initial amplitude", "AN-INITIAL-CONDITION", "INITIAL",
     None, "COUPLING"),
    ("the record", "the initial count field", "AN-INITIAL-CONDITION",
     "INITIAL", None, "COUPLING"),
)

# The class words that are themselves carried by a measured predicate, and the
# payload key that carries each.  A row in one of these classes whose
# predicate is false is an offence at G-PARAMETERS.
PARAM_CLASS_PREDICATE = {
    "DERIVED": None,                     # handled by the row's own law key
    "INVARIANT-IN-THE-SUBSTRATE-CENSUS": {
        "L": "inv_direction_blind",
        "the coordinate": "recon_coordinate_invariant"},
    "RECONSTRUCTED-CONDITIONALLY": {"n": "param_law_actor_count_conditional"},
}


def parameter_rows(P):
    """the rendered parameter table: the selection column is READ OFF the
    measured predicate the row names, never typed."""
    out = []
    for (nm, what, fiber, cls, law, where) in PARAMETER_SPEC:
        selects = "YES" if (law is not None and bool(P.get(law))) else "NO"
        out.append((nm, what, fiber, cls, selects, where))
    return out


# One row per object.  Every row names the PAYLOAD KEY its cardinality is
# read from -- no cardinality is typed here (K3 MAJOR-7 / K2 minor 8) -- the
# backing word it claims, the EXTENT it is a name for (so that rows which are
# re-descriptions of one set are visible as such, K1 m2), and what the number
# counts (K1 m1: a state-space dimension and a kernel corank are not object
# counts).  A row whose key the run does not measure resolves NONE.
CENSUS_SPEC = (
    ("ACTOR", "DECLARED", "COMPUTED-HERE", "arena_sites", "THE-ACTORS",
     "actors",
     "declared as the points of the arena, and reconstructed from the record "
     "inside the triangular class of section five"),
    ("SITE", "DECLARED", "COMPUTED-HERE", "arena_sites", "THE-ACTORS",
     "sites", "the same objects as the actors under the weld's dictionary"),
    ("DIRECTION", "DECLARED", "COMPUTED-HERE", "arena_declared_directions",
     "THE-DIRECTIONS", "declared classes",
     "three of the parallel classes of the arena are declared links"),
    ("PARALLEL-CLASS", "GENERATED", "COMPUTED-HERE", "arena_parallel_classes",
     "THE-PARALLEL-CLASSES", "resolutions",
     "the resolutions of the arena, generated from the field"),
    ("CELL", "GENERATED", "COMPUTED-HERE", "arena_cells", "THE-CELLS",
     "cells", "one per site and declared direction"),
    ("CO-DIVISION-PAIR", "GENERATED", "COMPUTED-HERE",
     "arena_codivision_pairs", "THE-CELLS", "cells",
     "the cell is the unordered pair, by the carrier typing"),
    ("DIVISION-EVENT", "GENERATED", "COMPUTED-HERE", "arena_actor_groups",
     "THE-EVENTS", "actor groups",
     "every group of the declared arity; the corpus realises some of them"),
    ("REALISED-EVENT", "GENERATED", "COMPUTED-HERE", "corpus_distinct_events",
     "THE-REALISED-EVENTS", "events",
     "the events the committed corpus actually runs"),
    ("GROUPING", "GENERATED", "COMPUTED-HERE", "arena_groupings",
     "THE-GROUPINGS", "partitions",
     "the partitions of the actors into groups of the declared arity"),
    ("ADMISSIBLE-ROUND", "LAW-SELECTED", "COMPUTED-HERE",
     "arena_saturating_groupings", "THE-ADMISSIBLE-ROUNDS", "partitions",
     "the groupings the saturation law admits"),
    ("HISTORY", "GENERATED", "COMPUTED-HERE", "corpus_distinct_histories",
     "THE-HISTORIES", "sequences",
     "the distinct sequences of events the committed drivers produce"),
    ("RECORD-BLOCK", "GENERATED", "COMPUTED-HERE", "record_blocks",
     "THE-BLOCKS", "blocks", "the cells one event writes"),
    ("BARE-RECORD", "GENERATED", "COMPUTED-HERE",
     "record_distinct_bare_records", "THE-BARE-RECORDS", "sequences",
     "the sequence of blocks, actor labels erased"),
    ("COUNT-FIELD", "GENERATED", "COMPUTED-HERE", "record_count_fields",
     "THE-COUNT-FIELDS", "fields", "the division count on each cell"),
    ("QUANTUM-STATE", "DECLARED", "COMPUTED-HERE", "arena_cells",
     "THE-AMPLITUDE-COORDINATES", "ring coordinates",
     "one amplitude per cell, in the ring the field generates"),
    ("MENU", "LAW-SELECTED", "COMPUTED-HERE", "arena_menu", "THE-MENU",
     "coset partitions",
     "the coset partitions of the translation subgroups"),
    ("NAMING", "RECONSTRUCTED", "COMPUTED-HERE",
     "inv_link_graph_automorphisms", "THE-NAMINGS", "relabellings",
     "the relabellings the record admits of the reconstructed cast"),
    ("DIRECTION-SPLITTING", "RECONSTRUCTED", "COMPUTED-HERE",
     "inv_direction_splittings", "THE-SPLITTINGS", "splittings",
     "the ways the reconstructed link structure splits into classes"),
    ("COIN", "DECLARED", "COMPUTED-HERE", "coin_classes", "THE-COIN-CLASSES",
     "classes up to a phase",
     "the covariant unitary family, up to a global phase"),
    ("SEAM", "DECLARED", "COMPUTED-HERE", "seam_kernel", "THE-SEAM-KERNEL",
     "undetermined numbers",
     "the undetermined entries the chart leaves at a shared site"),
    ("CHART", "DECLARED", "SEALED-CITATION", "cited_chart_types",
     "THE-CHART-TYPES", "combinatorial types",
     "the combinatorial types of a two-sector overlap"),
    ("TICK", "DECLARED", "SEALED-CITATION", "cited_tick_sites", "THE-TICK",
     "sites a tick",
     "one scheduling convention; the emergent speed is one site a tick"),
    ("CARRIER-CANDIDATE", "DECLARED", "SEALED-CITATION",
     "cited_carrier_cells", "THE-CELLS", "cells",
     "the carrier the exclusion census selected; excitations are not "
     "declared until the excitation gate opens"),
)


def census_rows(R):
    """one row per object.  `class` is one of the pin's five words; `backing`
    is RESOLVED, not typed: a row whose declared cardinality key the run does
    not carry reads NONE and the census word falls to CENSUS-PARTIAL."""
    out = []
    for (o, c, bk, key, extent, counts, rd) in CENSUS_SPEC:
        if key in R:
            out.append({"object": o, "class": c, "backing": bk,
                        "cardinality": R[key], "extent": extent,
                        "counts": counts, "reading": rd})
        else:
            out.append({"object": o, "class": c, "backing": "NONE",
                        "cardinality": 0, "extent": extent,
                        "counts": counts, "reading": rd})
    return out


# ===========================================================================
# SECTION F.  THE ANCHORS, THE WALLS, THE UNIVERSES.
# ===========================================================================

# The fifth field is the BINDING: DIGIT and SPELLED anchors have a numeral
# parsed out of their located text and compared with a measurement; a WORD
# anchor carries no numeral at all, is declared as such, and may back no
# published cardinality (K3 MAJOR-7).
ANCHORS = (
    ("REC-CARRIER", "v14/paper-41-rec.md", "G-OBJECT-CENSUS",
     "27 cells against 27 pairs, two actors in each cell at all of them, "
     "six cells per actor at all nine", "DIGIT"),
    ("REC-NAMING", "v14/paper-41-rec.md", "G-INVARIANCE-GROUPS",
     "the record admits 1,296 namings of the derived cast and 108 of them "
     "carry the declared direction classes", "DIGIT"),
    ("REC-DEPTH", "v14/paper-41-rec.md", "G-RECORD-REBUILT",
     "no committed history sees more than 18 of the 27 record blocks", "DIGIT"),
    ("COUP-RESIDUE", "v14/paper-20-coupling.md", "G-STATE-READING-RELATIVE",
     "the walk consumes the count residue n mod 3, not the count.", "DIGIT"),
    ("COUP-COIN", "v14/paper-20-coupling.md", "G-COIN-FIBER",
     "falling into 6 classes up to a global phase, of which exactly 1 is "
     "+/- Grover", "DIGIT"),
    ("OCC-CARRIER", "v14/paper-31-occ.md", "G-OBJECT-CENSUS",
     "CELLS-WITH-EXACTLY-TWO-ACTORS=27-OF-27; ACTORS-IN-EXACTLY-SIX-CELLS=9-OF-9",
     "DIGIT"),
    ("SEC2-SEAM", "v14/paper-40-sec2.md", "G-SEAM-KERNEL",
     "The seam's own system is rank 6 on 10 by the chart alone, kernel 4; "
     "an unshared site's system is three equations on", "DIGIT"),
    ("AID-GAUGE", "v14/paper-33-aid.md", "G-DIRECTION-INVARIANCE",
     "rebuilt with ANT in place of DIA the substrate returns 36 saturating, "
     "72 I7-STRICT triples and 276 G-FLAT quadruples", "DIGIT"),
    ("NDEP-CARRIED", "v14/paper-39-ndep.md", "G-PARAMETERS",
     "NO TESTED NUMERAL IS REPRODUCED BY THE DECLARED n-ONLY READING", "WORD"),
    ("EPR-MULTIPARTITE", "v14/paper-38-epr.md", "G-ARENA-REBUILT",
     "The graph is therefore complete multipartite with those three lines as "
     "its parts, and every site has degree six", "SPELLED"),
    ("PLAN-WALLS", "v15/PLAN.md", "G-WALLS",
     "W1 : reconstruction is never promoted to derivation. W2 : invariance is "
     "never promoted to gauge or physical meaning before operational "
     "observables exist", "INDEX"),
    ("HOR-TICK", "v14/paper-42-hor.md", "G-OBJECT-CENSUS",
     "The Emergent Speed Is One Site a Tick and It Is Attained", "SPELLED"),
    ("SEC-CHART", "v14/paper-32-sec.md", "G-OBJECT-CENSUS",
     "the family is 45010 gluings in 16 combinatorial types", "DIGIT"),
)
ANCHOR_BINDING = {a[0]: a[4] for a in ANCHORS}

# which anchor's parsed numeral each cited census row's cardinality comes from
CENSUS_CITED_ANCHOR = {"CHART": "SEC-CHART", "TICK": "HOR-TICK",
                       "CARRIER-CANDIDATE": "REC-CARRIER"}


def anchor_numerals(text):
    """the integers an anchor's located text carries, in order."""
    return [int(m.group(0).replace(",", ""))
            for m in re.finditer(r"(?<![\w.])\d[\d,]*(?![\w])", text)]


def anchor_spelled_numerals(text):
    """the integers an anchor's located text spells IN WORDS, in order.  A
    parent whose sentence says `One Site a Tick` is carrying the numeral one,
    and a census row citing it is bound to that parse: were the parent to say
    two, the row would move (K3 MAJOR-7)."""
    words = {w: v for v, w in SPELLED.items()}
    out = []
    for m in re.finditer(r"[A-Za-z]+", text):
        w = m.group(0).casefold()
        if w in words:
            out.append(words[w])
    return out


# THE SEVEN WALLS, REBUILT (K2 MAJOR-2, K3 MAJOR-5).
#
# The negative leg is FRAME-GENERAL: a subject class, a bounded gap, a verb
# class, a bounded gap, an object class -- so the paraphrase, the passive and
# the re-voicing all match, and a sentence has to change what it SAYS to get
# past it, not merely how it says it.
#
# The LICENCE leg is switched ON for all seven (the previous delivery passed
# `(), ()` everywhere and the mechanism never ran).  Its vocabulary is the
# PROMOTION vocabulary: the words a paper reaches for when it upgrades a
# reconstruction to a derivation or an invariance to a gauge.  This paper
# carries none of them, so the leg reads as a ban with a licensed escape --
# any sentence carrying one must also carry a RENDERED CLAIM, which is a
# gated string.  Per POT MAJOR-1 the licence pool of each wall is the claim
# set MINUS any claim that itself carries that wall's policed vocabulary, so a
# policed word can never license itself; G-WALLS gates that every pool is
# non-empty.
#
# The controls are in WALL_PROBES below, written as prose BEFORE these
# patterns were written and sharing no long literal with them.
WALLS = (
    ("W-SCOPE",
     [r"\b(?:at|for|in|across)\s+(?:every|all|any)\s+"
      r"(?:arena|arenas|corpus|corpora|record|records)\b",
      r"\bin general\b", r"\bwithout restriction\b",
      r"\bfor every possible\b",
      r"\b(?:holds|true|the same)\b[^.|]{0,50}\b(?:at every|for all|in every)"
      r"\b[^.|]{0,20}\barena",
      r"\bthe (?:result|census|theorem) is universal\b",
      r"\b(?:extends|generalis\w+|generaliz\w+) to (?:every|all|any) "
      r"(?:arena|arenas|record|records|theory|theories)\b"],
     [r"one arena, the committed corpus", r"beyond the committed corpus"],
     ("at every arena", "for all arenas", "at any arena", "in general",
      "without restriction", "universally true")),
    ("W-EMERGENCE",
     [r"\b(?:the\s+)?(?:actors?|cast|points|actor count)\b[^.|]{0,60}"
      r"\bemerge\w*\b",
      r"\bemerge\w*\b[^.|]{0,50}\b(?:from|out of)\b[^.|]{0,30}\brecords?\b",
      r"\b(?:the\s+)?(?:actors?|cast)\b[^.|]{0,30}\b(?:is|are)\b[^.|]{0,20}"
      r"\bemergent\b",
      r"\bproves the emergence of\b",
      r"\b(?:actors?|cast)\b[^.|]{0,40}\baris\w+\b[^.|]{0,30}\brecords?\b",
      r"\b(?:reconstruction|result|cast|census|rule|criterion)\b[^.|]{0,50}"
      r"\b(?:is|are)\s+(?:therefore\s+|thus\s+)?generator[- ]independent\b",
      r"\bactors are not needed\b", r"\bactors need never be assumed\b",
      r"\bthe records?\s+alone\s+(?:creates?|makes?|produces?|generates?)\b",
      r"\bthe records?\b[^.|]{0,40}\bbrings?\b[^.|]{0,30}"
      r"\b(?:actors?|cast)\b[^.|]{0,20}\binto (?:being|existence)\b"],
     [r"identifiability within a generative class",
      r"the reconstruction is not generator[- ]independent"],
     ("emergence of the actors", "emerge from the record",
      "brought into being by", "creates the actors")),
    ("W-RECONSTRUCTION-IS-NOT-DERIVATION",
     [r"\brecords?\b[^.|]{0,60}\bderives?\b[^.|]{0,40}"
      r"\b(?:the\s+)?(?:actors?|cast|points)\b",
      r"\b(?:actors?|cast|actor count|points of the arena)\b[^.|]{0,60}"
      r"\b(?:is|are|was|were)\b[^.|]{0,40}\bderived\s+(?:back\s+)?from\b",
      r"\bderived\s+back\s+from\s+the\s+records?\b",
      r"\bthe\s+(?:cast|actors?|actor count)\s+(?:is|are)\s+"
      r"(?:therefore\s+|thus\s+)?(?:a\s+)?derived\b",
      r"\b(?:actors?|cast|actor count)\b[^.|]{0,60}\b(?:follows? from|"
      r"obtained from|obtained back|read out of|an output of|not an input)\b",
      r"\b(?:the record|the records|the reconstruction)\b[^.|]{0,40}"
      r"\b(?:selects?|chooses?|creates?|fixes?)\b[^.|]{0,30}"
      r"\b(?:the cast|the actors|among possible worlds)\b",
      r"\bidentifiability (?:is|means|amounts to|establishes) derivation\b",
      r"\breconstruction\b[^.|]{0,50}"
      r"\b(?:shows|proves|establishes|demonstrates)\b[^.|]{0,40}\bderivation\b",
      r"\b(?:reconstruction|records?)\b[^.|]{0,80}\bestablishes that\b"
      r"[^.|]{0,80}\b(?:an output|not an input)\b",
      r"\bthe (?:cast|actors?) (?:is|are) (?:an )?output of\b"],
     [r"is identifiability and not derivation"],
     ("derived from the record", "derives the cast", "derived back",
      "a derived quantity", "output of the writing", "output of the record",
      "obtained from the record", "not an input to it",
      "follow from the record", "follows from the record")),
    ("W-INVARIANCE-IS-NOT-GAUGE",
     [r"\b(?:stabilizer|invariance|relabellings?|orbit|quotient|"
      r"automorphisms?|group)\b[^.|]{0,60}\b(?:is|are)\s+"
      r"(?:therefore\s+|thus\s+|simply\s+|purely\s+)?(?:a\s+|pure\s+)?gauge\b",
      r"\b(?:is|are)\s+(?:therefore\s+|thus\s+)?(?:pure\s+|mere\s+)?gauge\b",
      r"\b(?:stabilizer|invariance|relabellings?|orbit|quotient|"
      r"automorphisms?|group)\b[^.|]{0,60}\b(?:is|are)\s+"
      r"(?:therefore\s+|thus\s+)?(?:a\s+|pure\s+)?redundanc\w*\b",
      r"\bunphysical\b",
      r"\bcarries the whole physical content\b",
      r"\b(?:is|are)\b[^.|]{0,20}\bphysically meaningless\b",
      r"\bthe gauge quotient is\b",
      r"\b(?:stabilizer|invariance|automorphisms?|relabellings?)\b"
      r"[^.|]{0,40}\bis the gauge group\b",
      r"\b(?:relabellings?|orbit|stabilizer|namings?)\b[^.|]{0,60}"
      r"\b(?:no physical content|not physical|carry no physics)\b"],
     [r"the gauge word is withheld here",
      r"every physical observable and every experiment"],
     ("unobservable in principle", "an experiment could ever see",
      "pure convention", "merely conventional", "redundant labelling",
      "without physical content", "the gauge group",
      "a mere relabelling")),
    ("W-STATE-SCOPE",
     [r"\bthe complete state of the theory\b",
      r"\bthe universal state is\b", r"\bthis is the state of isp\b",
      r"\bthe state (?:list )?is (?:universal|complete for every|"
      r"the theory's)\b",
      r"\bthe state is complete for every dynamics\b",
      r"\b(?:this|the) state list\b[^.|]{0,40}\b(?:every|any) "
      r"(?:dynamics|theory|arena)\b",
      r"\bstate\b[^.|]{0,30}\bsufficient\b[^.|]{0,30}\bfor (?:every|any) "
      r"dynamics\b"],
     [r"sufficient for the committed machine at fixed background",
      r"the universal state waits on the autonomous[- ]update unit"],
     ("the universal state is", "state of the theory",
      "complete for every dynamics", "the state list is universal",
      "sufficient for every dynamics")),
    ("W-MEASURE",
     [r"\bmore likely\b", r"\bprobability that a history\b",
      r"\bthe typical history\b", r"\bon average the\b",
      r"\bmost histories are\b", r"\bwith high probability\b",
      r"\bthe odds\b", r"\bexpected number of histories\b",
      r"\ba randomly chosen (?:history|record|field)\b"],
     [r"counts are counting[- ]only"],
     ("more likely", "probability that", "on average", "the typical history",
      "with high probability", "the odds")),
    ("W-NEW-PHYSICS",
     [r"\bthis unit predicts\b", r"\bwe therefore predict\b",
      r"\bin the continuum limit\b", r"\bthis is spacetime\b",
      r"\bthe theory is confirmed\b", r"\ba new law\b",
      r"\bwe derive a new\b", r"\bthe prediction is\b",
      r"\bexperimentally confirmed\b",
      r"\bthe\s+(?:carrier|cells?)\s+(?:is|are)\s+(?:the\s+|a\s+|an\s+)?"
      r"(?:particles?|excitations?|quanta)\b",
      r"\bthe (?:particle|excitation) content of (?:the theory|isp|"
      r"this corpus)\b",
      r"\bthese are the (?:particles|excitations)\b"],
     [r"no new physics claim"],
     ("we predict", "this unit predicts", "in the continuum limit",
      "this is spacetime", "the theory is confirmed", "a new law",
      "we derive a new", "the particle content", "the excitation content of")),
)

STANDING_WALLS = ("W-RECONSTRUCTION-IS-NOT-DERIVATION",
                  "W-INVARIANCE-IS-NOT-GAUGE")


def wall_licences(policed, texts):
    """POT MAJOR-1: a policed word may never license itself, so the pool is
    the rendered claim set minus every claim that carries one."""
    return tuple(c for c in texts
                 if not any(w in c.casefold() for w in policed))


def wall_objects(texts):
    return [ET.SemanticWall(n, neg, pos, pol, wall_licences(pol, texts))
            for (n, neg, pos, pol) in WALLS]


# THE CONTROLS.  Every one is a sentence a paper could write, drafted from the
# violation and not from the pattern list.  The first sixteen are the
# paraphrase families the effectus seat planted; the last two are the
# instrument seat's re-voicings of the two standing walls, verbatim.  Each
# declares the wall that must kill it, and G-WALLS runs each one through the
# delivered paper and requires that death.
WALL_PROBES = (
    ("W-RECONSTRUCTION-IS-NOT-DERIVATION",
     "The record therefore fixes the cast: the nine actors follow from the "
     "record blocks alone, and nothing else was needed to obtain them."),
    ("W-RECONSTRUCTION-IS-NOT-DERIVATION",
     "The actor count is therefore a derived quantity of the construction."),
    ("W-RECONSTRUCTION-IS-NOT-DERIVATION",
     "Because the blocks leave no choice, the cast is derived from the "
     "record and the arena's points are read off it."),
    ("W-RECONSTRUCTION-IS-NOT-DERIVATION",
     "The reconstruction establishes that the points of the arena are an "
     "output of the writing rather than an input to it."),
    ("W-RECONSTRUCTION-IS-NOT-DERIVATION",
     "The record selects the cast among the possible worlds the tokens "
     "allow."),
    ("W-EMERGENCE",
     "The nine actors emerge from the twenty-seven blocks and from nothing "
     "else."),
    ("W-EMERGENCE",
     "The cast is emergent: it was never assumed, only written."),
    ("W-EMERGENCE",
     "The reconstruction is generator-independent, so the actors arise from "
     "the records themselves."),
    ("W-INVARIANCE-IS-NOT-GAUGE",
     "The 1,296 relabellings the round law fixes are therefore without "
     "physical content: nothing an experiment could ever see distinguishes "
     "them."),
    ("W-INVARIANCE-IS-NOT-GAUGE",
     "The stabilizer of the round law is a redundancy of the description "
     "and nothing more."),
    ("W-INVARIANCE-IS-NOT-GAUGE",
     "Those 1,296 namings are unphysical, so the quotient is where the "
     "content lives."),
    ("W-INVARIANCE-IS-NOT-GAUGE",
     "The direction declaration is pure convention, a redundant labelling "
     "of one and the same structure."),
    ("W-STATE-SCOPE",
     "The components above are the complete state of the theory."),
    ("W-STATE-SCOPE",
     "The state list is universal: it is sufficient for every dynamics a "
     "successor unit could declare."),
    ("W-NEW-PHYSICS",
     "The carrier is the excitation, and the cells are the quanta the "
     "theory has been looking for."),
    ("W-NEW-PHYSICS",
     "In the continuum limit this is spacetime, and the theory is confirmed."),
    ("W-RECONSTRUCTION-IS-NOT-DERIVATION",
     "The records derive nine actors: the cast follows from the blocks "
     "alone, so the actor count is obtained from the record rather than "
     "assumed, and the reconstruction therefore establishes that the points "
     "of the arena are an output of the writing and not an input to it."),
    ("W-INVARIANCE-IS-NOT-GAUGE",
     "The round law's stabilizer is gauge: its 1,296 elements are "
     "unobservable in principle, the quotient by them carries the whole "
     "physical content, and the remaining 108 are the only relabellings an "
     "experiment could ever see."),
)


LITERAL_FLOOR = 12


def _pattern_literals(pat):
    """the literal PHRASES a regex insists on, so that a control can be
    checked for having been copied out of the pattern list (E-23).  Word
    boundaries are joined across and whitespace classes become spaces; every
    other regex construct breaks the phrase."""
    t = pat.replace(r"\b", "").replace(r"\s+", " ").replace(r"\s", " ")
    t = re.sub(r"\[[^\]]*\]", "\x00", t)
    t = re.sub(r"\\[a-zA-Z]", "\x00", t)
    t = re.sub(r"[(){}|?*+^$.\\]", "\x00", t)
    return [s.strip().casefold() for s in t.split("\x00")
            if len(s.strip()) >= LITERAL_FLOOR]


# The wall's own falsifier, written as a paper would write the violation and
# sharing no literal phrase with any pattern (K2 MAJOR-2's mechanism: the old
# MUT-WALL was the wall's own negative pattern spelled out as a sentence).
# It carries a POLICED phrase in an unlicensed sentence, so it dies at the
# licence leg -- the leg the first delivery never switched on.
MUT_WALL_SENTENCE = ("Two records that differ by a mere relabelling say the "
                     "same thing about the world.")


def wall_probe_report(walls, paper_text, claims):
    """every control planted into the delivered paper, one at a time, and run
    through the wall it names.  A control that does not die is an offence."""
    byname = {w.name: w for w in walls}
    rows, offences = [], []
    for wname, sentence in WALL_PROBES:
        w = byname[wname]
        planted = paper_text + "\n\n" + sentence + "\n"
        leg, detail = "SURVIVED", ""
        try:
            w.scan(planted, claims)
        except ET.CheckFail as exc:
            detail = exc.detail
            if "banned pattern" in detail:
                leg = "NEGATIVE"
            elif "policed sentence" in detail:
                leg = "LICENCE"
            elif "standing sentence" in detail:
                leg = "POSITIVE"
            else:
                leg = "OTHER"
        if leg in ("SURVIVED", "POSITIVE", "OTHER"):
            offences.append("%s :: %s" % (wname, sentence[:60]))
        copied = sorted({lit for pat in w.negative
                         for lit in _pattern_literals(pat)
                         if lit in sentence.casefold()})
        rows.append({"wall": wname, "died_at_leg": leg,
                     "copied_pattern_literals": len(copied)})
    return rows, offences


# ===========================================================================
# SECTION G.  THE RUN.
# ===========================================================================

GATE_ORDER = (
    "G-SOURCES-PINNED", "G-NO-FLOAT", "G-S1-DISJOINT-CODE",
    "G-ARENA-REBUILT", "G-CORPUS-REBUILT",
    "G-RECORD-REBUILT", "G-OBJECT-CENSUS", "G-STATE-COMPONENTS",
    "G-STATE-SCREENS-THE-HISTORY", "G-STATE-READING-RELATIVE",
    "G-INVARIANCE-GROUPS", "G-DIRECTION-INVARIANCE",
    "G-LOCAL-ARITY-GROUP", "G-QUOTIENT-CENSUS",
    "G-DEPENDENCY-CYCLE", "G-CAST-UNIQUE-IN-THE-CLASS", "G-CAST-RESIDUE",
    "G-Q58-ARMS", "G-Q58-VERDICT", "G-COIN-FIBER", "G-MENU-LAW-SELECTED",
    "G-SEAM-KERNEL", "G-PARAMETERS", "G-OUTCOMES-REACHABLE",
    "G-CLAIMS-EQUAL", "G-REFERENTS-BOUND", "G-WALLS", "G-ANCHORS-CONSUMED",
    "G-NO-TYPED-COUNTS", "G-RECEIPT-TYPES", "G-HEAD-REBUILT",
    "G-TRANSCRIPT-BOUND", "G-READS-DECLARED", "G-TEMPLATE-EXERCISED",
)

# The three gates whose object is the run itself, and which therefore fire
# AFTER the ordinary loop closes: the transcript's reconciliation, the read
# set, and the execution census.  Their measurements do not exist until the
# loop has run, so a mutant that names one of them is applied AT ITS OWN GATE
# and never at the payload's construction.
CLOSING_GATES = ("G-TRANSCRIPT-BOUND", "G-READS-DECLARED",
                 "G-TEMPLATE-EXERCISED")

# A key is sealed AT THE GATE WHOSE PREDICATE READS IT (E-25; K3 MINOR-1 found
# seven gates' worth of keys attributed to gates that never evaluated them).
# The longest matching prefix wins, so the specific routes below override the
# family prefixes at the bottom.
SEAL_AT = {
    "state_equal_residue": "G-STATE-SCREENS-THE-HISTORY",
    "state_distinct_residue": "G-STATE-SCREENS-THE-HISTORY",
    "state_single_cell": "G-STATE-SCREENS-THE-HISTORY",
    "state_successors": "G-STATE-SCREENS-THE-HISTORY",
    "state_amplitude": "G-STATE-SCREENS-THE-HISTORY",
    "state_reading": "G-STATE-READING-RELATIVE",
    "inv_local": "G-LOCAL-ARITY-GROUP",
    "inv_direction_profiles": "G-DIRECTION-INVARIANCE",
    "inv_direction_choices": "G-DIRECTION-INVARIANCE",
    "inv_direction_census": "G-DIRECTION-INVARIANCE",
    "inv_direction_blind": "G-DIRECTION-INVARIANCE",
    "inv_candidate_direction": "G-CAST-RESIDUE",
    "inv_declared_splitting": "G-CAST-RESIDUE",
    "inv_single_class": "G-CAST-RESIDUE",
    "class_cast_residue": "G-CAST-RESIDUE",
    "class_cast": "G-CAST-UNIQUE-IN-THE-CLASS",
    "class_blocks": "G-CAST-UNIQUE-IN-THE-CLASS",
    "recon_coordinate": "G-CAST-UNIQUE-IN-THE-CLASS",
    "recon_second": "G-CAST-UNIQUE-IN-THE-CLASS",
    "recon_set_equality": "G-CAST-UNIQUE-IN-THE-CLASS",
    "q58_split": "G-Q58-VERDICT",
    "q58_domain": "G-Q58-VERDICT",
    "q58_criterion": "G-Q58-VERDICT",
    "arena_menu": "G-MENU-LAW-SELECTED",
    "arena_translation": "G-MENU-LAW-SELECTED",
    "wall_": "G-WALLS",
    "referent_": "G-REFERENTS-BOUND",
    "delivery_falsifier": "G-TEMPLATE-EXERCISED",
    "template_": "G-TEMPLATE-EXERCISED",
    "region_": "G-S1-DISJOINT-CODE",
    "arena": "G-ARENA-REBUILT", "corpus": "G-CORPUS-REBUILT",
    "record": "G-RECORD-REBUILT", "census": "G-OBJECT-CENSUS",
    "cited": "G-OBJECT-CENSUS",
    "state": "G-STATE-COMPONENTS", "inv_": "G-INVARIANCE-GROUPS",
    "quotient": "G-QUOTIENT-CENSUS", "dep": "G-DEPENDENCY-CYCLE",
    "q58": "G-Q58-ARMS",
    "coin": "G-COIN-FIBER", "seam": "G-SEAM-KERNEL",
    "param": "G-PARAMETERS", "recon": "G-RECORD-REBUILT",
}


KEY_GATE_EXACT = {
    "source_count": "G-SOURCES-PINNED",
    "source_mismatches": "G-SOURCES-PINNED",
    "source_mismatch_count": "G-SOURCES-PINNED",
    "float_offences": "G-NO-FLOAT", "float_offence_count": "G-NO-FLOAT",
    "outcome_controls": "G-OUTCOMES-REACHABLE",
    "outcome_words": "G-OUTCOMES-REACHABLE",
    "outcome_reachable": "G-OUTCOMES-REACHABLE",
    "outcome_feasibility_distinct": "G-OUTCOMES-REACHABLE",
    "outcome_measured_witnesses": "G-OUTCOMES-REACHABLE",
    "param_declared_objects_unpriced": "G-PARAMETERS",
    "census_declared_objects": "G-OBJECT-CENSUS",
    "census_cited_rows": "G-ANCHORS-CONSUMED",
    "census_cited_rows_on_word_bound_anchors": "G-ANCHORS-CONSUMED",
    "anchor_count": "G-ANCHORS-CONSUMED",
    "anchor_consumers": "G-ANCHORS-CONSUMED",
    "anchor_bindings": "G-ANCHORS-CONSUMED",
    "anchor_numeral_bound": "G-ANCHORS-CONSUMED",
    "anchor_word_bound": "G-ANCHORS-CONSUMED",
    "anchor_unconsumed": "G-ANCHORS-CONSUMED",
    "anchor_phantom_consumers": "G-ANCHORS-CONSUMED",
    "claim_rows": "G-CLAIMS-EQUAL", "claim_prose": "G-CLAIMS-EQUAL",
    "claim_fences": "G-CLAIMS-EQUAL", "render_tables": "G-CLAIMS-EQUAL",
    "paper_digest": "G-CLAIMS-EQUAL",
    "claim_texts_fixed": "G-CLAIMS-EQUAL",
    "claim_texts_rendered": "G-CLAIMS-EQUAL",
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
    "head_positions_emitted": "G-HEAD-REBUILT",
    "head_mismatches": "G-HEAD-REBUILT",
    "transcript_rows": "G-TRANSCRIPT-BOUND",
    "transcript_preamble": "G-TRANSCRIPT-BOUND",
    "ledger_rows": "G-TRANSCRIPT-BOUND",
    "transcript_stray": "G-TRANSCRIPT-BOUND",
    "transcript_missing": "G-TRANSCRIPT-BOUND",
    "reads_declared": "G-READS-DECLARED", "reads_stray": "G-READS-DECLARED",
    "reads_never": "G-READS-DECLARED", "reads_distinct": "G-READS-DECLARED",
    "reads_unpinnable": "G-READS-DECLARED",
    "reads_after_the_gate": "G-READS-DECLARED",
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
    for pre in sorted(SEAL_AT, key=len, reverse=True):
        if k.startswith(pre):
            return SEAL_AT[pre]
    return None


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
    s1 = ("CONTRACT-%s<OBJECTS=%d; DISTINCT-EXTENTS=%d; COMPUTED-HERE=%d; "
          "CITED=%d; ACTORS=%d; CELLS=%d; EVENTS-REALISED=%d; HISTORIES=%d; "
          "BLOCKS=%d; COUNT-FIELDS=%d; MENU=%d; CHART-CLASSES=%d>") % (
        census, P["census_row_count"], P["census_distinct_extents"],
        P["census_computed_here"],
        P["census_cited"], P["arena_sites"], P["arena_cells"],
        P["corpus_distinct_events"], P["corpus_distinct_histories"],
        P["record_blocks"], P["record_count_fields"], P["arena_menu"],
        P["inv_link_graph_automorphisms"])
    s2 = ("CONTRACT-STATE-AT-FIXED-BACKGROUND-AND-INVARIANCE<"
          "STATE-COMPONENTS=%d; ENSEMBLE-SIDE-BOOKKEEPING=%d; BACKGROUND=%d; "
          "COUNT-FIELDS=%d; RESIDUE-FIELDS=%d; SUCCESSORS=%d; "
          "EQUAL-RESIDUE-PAIRS-AGREEING=%d-OF-%d; "
          "DISTINCT-RESIDUE-COLLISIONS-AT-THE-UNIFORM-AMPLITUDE=%d-OF-%d; "
          "DISTINCT-RESIDUE-COLLISIONS-AT-A-SINGLE-CELL-AMPLITUDE=%d-OF-%d; "
          "BORN-MENU-VALUES=%d; "
          "RELABELLINGS=%d; LAW-STABILIZER=%d; ARENA-STABILIZER=%d; "
          "DIRECTION-INDEX=%d; SPLITTINGS=%d; "
          "LOCAL-GROUP=%d; LOCAL-COLLAPSE-WIDTH=%d; "
          "HISTORY-EVENT-MULTISETS=%d; "
          "HISTORIES-SURVIVING=%d-OF-%d; "
          "HISTORIES-ORDER-KEPT-SURVIVING=%d-OF-%d; "
          "FIELDS-SURVIVING=%d-OF-%d; "
          "GAUGE-WORD=WITHHELD>") % (
        P["state_components"], P["state_ensemble_components"],
        P["state_background_components"],
        P["record_count_fields"], P["record_residue_fields"],
        P["state_successors_distinct"],
        P["state_equal_residue_agreements"], P["state_equal_residue_pairs"],
        P["state_distinct_residue_collisions"], P["state_distinct_residue_pairs"],
        P["state_single_cell_collisions"], P["state_single_cell_pairs"],
        P["state_reading_a_born_values"],
        P["inv_symmetric_group"], P["inv_law_stabilizer"],
        P["inv_arena_automorphisms"], P["inv_direction_index"],
        P["inv_direction_splittings"], P["inv_local_group_order"],
        P["inv_local_collapse_width"],
        P["quotient_history_event_multisets"],
        P["quotient_histories_link"], P["quotient_history_event_multisets"],
        P["quotient_histories_ordered_link"], P["quotient_histories"],
        P["quotient_fields_link"], P["quotient_fields"])
    s3 = ("CONTRACT-%s<CYCLE-LENGTH=%d; ACTOR-RECORD-CYCLE-LENGTH=%d; "
          "CAST-SOLUTIONS=%d; RESIDUE=%d; "
          "ARMS=%d; DISTINCT-INPUTS=%d; RECOVERING=%d; RECOVERING-INPUTS=%d; "
          "REFUSING=%d; REFUSING-INPUTS=%d>") % (
        circ, P["dep_cycle_length"], P["dep_actor_record_cycle_length"],
        P["class_cast_solutions"],
        P["class_cast_residue"], P["q58_arms_total"], P["q58_distinct_inputs"],
        P["q58_arms_recovering"], P["q58_distinct_recovering_inputs"],
        P["q58_arms_refusing"], P["q58_distinct_refusing_inputs"])
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


def outcome_controls(P):
    """#299-EXTENDED.  Every pre-registered word is (a) EMITTED by the real
    comparator, and (b) argued FEASIBLE AT THE COMMITTED CORPUS, per row, by a
    sentence that names the corpus fact which would flip it.  Where a real
    input of this run emits the word the witness is MEASURED-HERE; where the
    corpus supplies no such input the witness says which fact is missing.
    (K2 MAJOR-5c: eleven identical strings, and two words that no corpus this
    builder can produce could ever emit.)"""
    rows = []
    thin = {k: v for k, v in P.items() if k != "cited_tick_sites"}
    arms = P["q58_arms"]
    tri_recovering = sum(1 for a in arms
                         if a["all_blocks_triangular"] and a["cast_recovered"])
    tri_refusing = sum(1 for a in arms
                       if a["all_blocks_triangular"] and not a["cast_recovered"])
    non_recovering = sum(1 for a in arms
                         if not a["all_blocks_triangular"] and a["cast_recovered"])
    non_refusing = sum(1 for a in arms
                       if not a["all_blocks_triangular"] and not a["cast_recovered"])
    prefix = [p for p in P["q58_domain_probes"]
              if p["probe"] == "the smallest covering prefix"][0]

    def word_row(word, got, witness, feasibility):
        rows.append([word, got, witness, feasibility])
    word_row("CENSUS-TOTAL", k_census_word(P["census_rows"]), "MEASURED-HERE",
        "the delivered census: every row's cardinality key is carried by "
        "this run, so no row resolves NONE")
    word_row("CENSUS-PARTIAL", k_census_word(census_rows(thin)), "MEASURED-HERE",
        "the same builder over a payload from which one cited cardinality "
        "has been withheld: that row resolves NONE and the word falls")
    word_row("ACYCLIC", k_circularity_word(
        len(_all_cycles(tuple(e for e in DEPENDENCY_EDGES
                              if e not in FEEDBACK_EDGES))) > 0,
        P["class_cast_solutions"], P["class_cast_matches_declared"],
        P["class_cast_residue"]), "MEASURED-HERE",
        "the same dependency graph with its two feedback edges cut has no "
        "cycle at all, so a corpus that never wrote a record back would "
        "read here")
    word_row("CIRCULAR-CAST-UNIQUE-IN-THE-TRIANGULAR-CLASS",
        k_circularity_word(True, P["class_cast_solutions"],
                           P["class_cast_matches_declared"],
                           P["inv_single_class_splittings"]), "MEASURED-HERE",
        "one declared direction class of the same record offers exactly one "
        "splitting, so a record with no direction residue reads here")
    word_row("CIRCULAR-CAST-UNIQUE-IN-THE-TRIANGULAR-CLASS-"
        "UP-TO-THE-DIRECTION-DECLARATION",
        k_circularity_word(True, P["class_cast_solutions"],
                           P["class_cast_matches_declared"],
                           P["class_cast_residue"]), "MEASURED-HERE",
        "the delivered measurement: one cast family and a direction residue "
        "above one")
    word_row("CIRCULAR-BLOCKED-AT-THE-CAST",
        k_circularity_word(True, P["class_cast_solutions"],
                           prefix["cast_recovered"], P["class_cast_residue"]),
        "MEASURED-HERE",
        "the covering-prefix probe of section five does not return the "
        "declared cast, and a corpus whose whole record read like it would "
        "read here")
    word_row("Q58-EMERGENCE-GENERATOR-INDEPENDENT",
        k_q58_word(tri_recovering, tri_refusing), "MEASURED-HERE",
        "restricted to the arms that write triangles the corpus already "
        "shows no refusal, so a corpus whose every mechanism wrote "
        "triangles would read here")
    word_row("Q58-IDENTIFIABILITY-WITHIN-A-GENERATIVE-CLASS",
        k_q58_word(P["q58_arms_recovering"], P["q58_arms_refusing"]),
        "MEASURED-HERE",
        "the delivered measurement: more than one arm recovers and at least "
        "one refuses")
    word_row("Q58-UNDECIDED-NO-SECOND-MECHANISM",
        k_q58_word(non_recovering, non_refusing), "MEASURED-HERE",
        "restricted to the arms that do not write triangles no arm recovers, "
        "so a corpus supplying only those would leave the question open")
    word_row("ISP-IS-ONE-THEORY",
        k_parameter_word(P["param_free_selected_by_a_law"]), "MEASURED-HERE",
        "the word reads at a free count of zero; the free count is computed "
        "from the selection predicates, of which this corpus satisfies every "
        "one it declares and declares none for the rows that stay free")
    word_row("ISP-IS-A-FAMILY", k_parameter_word(P["param_free"]), "MEASURED-HERE",
        "the delivered measurement: the free count is positive")
    return rows


# the two edges that close the dependency graph's loops; cutting them is what
# the ACYCLIC control measures.
FEEDBACK_EDGES = (
    ("RECORD-BLOCK", "ACTOR", "the reconstruction reads a cast off the blocks"),
    ("EMISSION", "COUNT-FIELD", "an emission increments the count field"),
)


# ===========================================================================
# SECTION H.  THE GATES, AS PREDICATES OVER THE PAYLOAD.
# ===========================================================================

CTX: dict = {}

SPELLED = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six",
           7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven",
           12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen",
           16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen",
           20: "twenty", 21: "twenty-one", 22: "twenty-two",
           23: "twenty-three", 24: "twenty-four", 25: "twenty-five",
           26: "twenty-six", 27: "twenty-seven"}

# The four families whose object is the paper; --render skips their gates and
# therefore does not exercise them, and says so rather than counting them.
PAPERLESS_FAMILIES = ("T-WALL-SEMANTIC", "T-ANCHOR-CONSUMED",
                      "T-CLAIMS-EQUAL", "T-REFERENT-BOUND")


def _fam(cid):
    """THE EXECUTION CENSUS (K3 MAJOR-3).  Called at the family's own live
    call site, in the mode being delivered -- never a regex over this file's
    source, which a dead class or a token in a comment can satisfy."""
    CTX.setdefault("fam", collections.Counter())[cid] += 1
    return cid


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
    # every *_count is DERIVED from its own list at render time, so a failing
    # gate's published evidence cannot contradict its failure (K3 MINOR-5).
    P["source_mismatch_count"] = len(P["source_mismatches"])
    ok = not P["source_mismatches"]
    return ok, fmt(P, "sources {source_count} mismatches {source_mismatch_count}",
                   "source_count", "source_mismatch_count")


def g_no_float(P):
    P["float_offence_count"] = len(P["float_offences"])
    return not P["float_offences"], fmt(
        P, "float literals {float_offence_count} in the module",
        "float_offence_count")


def g_s1(P):
    P["region_offences"] = (P["region_reach_offences"]
                            + P["region_alias_offences"]
                            + P["region_constant_offences"])
    P["region_offence_count"] = len(P["region_offences"])
    return not P["region_offences"], fmt(
        P, "regions {region_count} legs {region_legs} reach "
           "{region_reach_offence_count} alias {region_alias_offence_count} "
           "declared-constant {region_constant_offence_count} offences "
           "{region_offence_count}",
        "region_count", "region_legs", "region_reach_offence_count",
        "region_alias_offence_count", "region_constant_offence_count",
        "region_offence_count")


def g_template(P):
    counts = dict(P["template_family_counts"])
    expected = [cid for (_l, _n, cid) in ET.FAMILIES
                if cid not in P["template_families_declared_out_of_mode"]]
    P["template_families_expected"] = len(expected)
    P["template_families_live"] = sum(1 for cid in expected
                                      if counts.get(cid, 0) > 0)
    P["template_families_unexercised"] = sorted(
        cid for cid in expected if counts.get(cid, 0) == 0)
    ok = (P["template_families_live"] == P["template_families_expected"]
          and not P["template_families_unexercised"]
          and P["template_families"] == len(ET.FAMILIES))
    return ok, fmt(
        P, "template families {template_families} expected in this mode "
           "{template_families_expected} exercised by a live call "
           "{template_families_live}",
        "template_families", "template_families_expected",
        "template_families_live")


def g_arena(P):
    a = CTX["anchors"].read("EPR-MULTIPARTITE", "G-ARENA-REBUILT")
    deg = "degree six" in a
    ok = (P["arena_sites"] == B_Q ** B_DIMENSION
          and P["arena_cells"] == P["arena_sites"] * P["arena_declared_directions"]
          and P["arena_parallel_classes"] == B_Q + 1
          and P["arena_groupings"] == len(b_raw_census()["parts"])
          and P["recon_degree"] * P["arena_sites"] == 2 * P["arena_cells"]
          and P["arena_saturating_all_triangles"]
          and P["arena_all_triangle_groupings"] == P["arena_saturating_groupings"]
          and P["arena_cell_pair_bijection"]
          and P["arena_codivision_pairs"] == P["arena_cells"]
          and deg)
    return ok, fmt(P, "sites {arena_sites} cells {arena_cells} classes "
                      "{arena_parallel_classes} groupings {arena_groupings} "
                      "saturating {arena_saturating_groupings} all-triangle "
                      "{arena_all_triangle_groupings} degree {recon_degree}",
                   "arena_sites", "arena_cells", "arena_parallel_classes",
                   "arena_groupings", "arena_saturating_groupings",
                   "arena_all_triangle_groupings", "recon_degree")


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
    tick = anchor_spelled_numerals(A.read("HOR-TICK", "G-OBJECT-CENSUS"))
    rows = P["census_rows"]
    byname = {r["object"]: r for r in rows}
    classes_ok = all(r["class"] in CLASS_ALPHABET for r in rows)
    backing_ok = all(r["backing"] in BACKING_ALPHABET for r in rows)
    names_ok = len({r["object"] for r in rows}) == len(rows)
    counts_ok = all(r["counts"] for r in rows)
    ok = (classes_ok and backing_ok and names_ok and counts_ok
          and carrier[0] == P["arena_cells"] and carrier[1] == P["arena_cells"]
          and SPELLED[P["arena_sites"]] in carrier_text
          and occ[0] == P["arena_cells"] and occ[-1] == P["arena_sites"]
          # every CITED cardinality is the numeral parsed out of its anchor,
          # spelled numerals included -- none is typed here (K3 MAJOR-7)
          and byname["CHART"]["cardinality"] == chart[-1]
          and byname["TICK"]["cardinality"] == tick[0]
          and byname["CARRIER-CANDIDATE"]["cardinality"] == carrier[0]
          and P["census_backed"] == P["census_row_count"]
          and P["census_unbacked"] == 0
          and P["census_distinct_extents"] < P["census_row_count"]
          and P["census_identifications"] > 0)
    return ok, fmt(P, "rows {census_row_count} computed {census_computed_here} "
                      "cited {census_cited} backed {census_backed} primitive "
                      "{census_primitive} distinct extents "
                      "{census_distinct_extents} identifications "
                      "{census_identifications}",
                   "census_row_count", "census_computed_here", "census_cited",
                   "census_backed", "census_primitive",
                   "census_distinct_extents", "census_identifications")


def g_state_components(P):
    """ONE CLASSIFICATION PER OBJECT (v15 #33).  The branch weight is
    ensemble-side bookkeeping and is gated OUT of the one-instant state list,
    so the two tables cannot both name it."""
    names = {a for (a, _b, _c) in STATE_COMPONENTS}
    ens = {a for (a, _b, _c) in STATE_ENSEMBLE}
    ok = (P["state_components"] == len(STATE_COMPONENTS)
          and P["state_ensemble_components"] == len(STATE_ENSEMBLE)
          and P["state_background_components"] == len(STATE_BACKGROUND)
          and not (names & ens)
          and not (names & {a for (a, _b) in STATE_BACKGROUND}))
    return ok, fmt(P, "state components {state_components} ensemble-side "
                      "{state_ensemble_components} background "
                      "{state_background_components}",
                   "state_components", "state_ensemble_components",
                   "state_background_components")


def g_state_screens(P):
    """the two legs, TOLD APART (K2 MAJOR-3, K1 m4).  Sufficiency is
    structural -- the coin indexes the count only through its residue -- and
    holds at every amplitude probed.  Minimality is amplitude-relative and
    fails at a single-cell amplitude, so the head's zero is stamped to the
    uniform one."""
    ok = (P["state_equal_residue_agreements"] == P["state_equal_residue_pairs"]
          and P["state_equal_residue_disagreements"] == 0
          and P["state_distinct_residue_collisions"] == 0
          and P["state_successors_distinct"] == P["record_residue_fields"]
          # sufficiency at EVERY amplitude probed; minimality at some but not
          # all, which is the disclosure this gate carries
          and P["state_amplitudes_sufficient"] == P["state_amplitudes_probed"]
          and 0 < P["state_amplitudes_minimal"] < P["state_amplitudes_probed"]
          and P["state_single_cell_collisions"] > 0
          and P["state_amplitude_stamped"] == "THE-UNIFORM-AMPLITUDE")
    return ok, fmt(P, "equal-residue pairs {state_equal_residue_pairs} agreeing "
                      "{state_equal_residue_agreements} distinct-residue pairs "
                      "{state_distinct_residue_pairs} colliding "
                      "{state_distinct_residue_collisions} successors "
                      "{state_successors_distinct} amplitudes "
                      "{state_amplitudes_probed} sufficient at "
                      "{state_amplitudes_sufficient} minimal at "
                      "{state_amplitudes_minimal} single-cell collisions "
                      "{state_single_cell_collisions}",
                   "state_equal_residue_pairs", "state_equal_residue_agreements",
                   "state_distinct_residue_pairs",
                   "state_distinct_residue_collisions",
                   "state_successors_distinct", "state_amplitudes_probed",
                   "state_amplitudes_sufficient", "state_amplitudes_minimal",
                   "state_single_cell_collisions")


def g_state_reading(P):
    """the Born menu is the post-coin WEIGHTS, and it is coarser than the
    post-coin vectors the first delivery printed under its name (K1 M3)."""
    a = CTX["anchors"].read("COUP-RESIDUE", "G-STATE-READING-RELATIVE")
    ok = (anchor_numerals(a) == [B_Q]
          and P["state_reading_a_post_coin_vectors"] == P["record_residue_fields"]
          and P["state_reading_b_menus"] == P["record_count_fields"]
          and P["state_reading_a_born_values"]
          < P["state_reading_a_post_coin_vectors"] < P["state_reading_b_menus"])
    return ok, fmt(P, "Born-menu values {state_reading_a_born_values} post-coin "
                      "vectors {state_reading_a_post_coin_vectors} record-menu "
                      "values {state_reading_b_menus} residue fields "
                      "{record_residue_fields} count fields {record_count_fields}",
                   "state_reading_a_born_values",
                   "state_reading_a_post_coin_vectors", "state_reading_b_menus",
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
          and P["inv_direction_index"] == P["inv_direction_splittings"]
          # THE TWO FOUNDS, GATED (K1 F1, F2 / K2 minor 3)
          and P["inv_law_stabilizer_is_the_link_group"]
          and P["inv_arena_group_inside_the_link_group"]
          and P["inv_link_graph_closed_form"]
          == P["inv_link_graph_automorphisms"]
          and P["inv_splitting_action_transitive"]
          and P["inv_splitting_orbit"] == P["inv_direction_splittings"]
          and P["inv_splitting_stabilizer"] == P["inv_arena_automorphisms"]
          and P["inv_splitting_stabilizer_is_the_arena_group"]
          and P["inv_orbit_stabilizer_identity"])
    return ok, fmt(P, "symmetric group {inv_symmetric_group} law stabilizer "
                      "{inv_law_stabilizer} link automorphisms "
                      "{inv_link_graph_automorphisms} arena automorphisms "
                      "{inv_arena_automorphisms} index {inv_direction_index} "
                      "splittings {inv_direction_splittings} orbit "
                      "{inv_splitting_orbit} splitting stabilizer "
                      "{inv_splitting_stabilizer} parts {inv_link_graph_parts} "
                      "closed form {inv_link_graph_closed_form}",
                   "inv_symmetric_group", "inv_law_stabilizer",
                   "inv_link_graph_automorphisms", "inv_arena_automorphisms",
                   "inv_direction_index", "inv_direction_splittings",
                   "inv_splitting_orbit", "inv_splitting_stabilizer",
                   "inv_link_graph_parts", "inv_link_graph_closed_form")


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
    """SAME OBJECT ON BOTH SIDES (K1 M2).  The multiset chain and the
    order-preserving chain are gated separately, and the step that forgets the
    order -- which no group performs -- is published as its own number."""
    ok = (# the multiset chain: the sort first, then the groups
          P["quotient_history_event_multisets"] <= P["quotient_histories"]
          and P["quotient_histories_link"] <= P["quotient_histories_arena"]
          <= P["quotient_history_event_multisets"]
          # the order-preserving chain, on the object the census row defines
          and P["quotient_histories_ordered_link"]
          <= P["quotient_histories_ordered_arena"] <= P["quotient_histories"]
          # the sort is not a group action, and here it does most of the work
          and P["quotient_history_event_multisets"] < P["quotient_histories"]
          and P["quotient_histories_ordered_link"]
          > P["quotient_histories_link"]
          and P["quotient_fields_link"] <= P["quotient_fields_arena"]
          <= P["quotient_fields"]
          and P["quotient_fields_arena"] == P["quotient_fields_link"])
    return ok, fmt(P, "histories {quotient_histories} event multisets "
                      "{quotient_history_event_multisets} arena "
                      "{quotient_histories_arena} link {quotient_histories_link} "
                      "order kept arena {quotient_histories_ordered_arena} "
                      "order kept link {quotient_histories_ordered_link} "
                      "fields {quotient_fields} arena {quotient_fields_arena} "
                      "link {quotient_fields_link}",
                   "quotient_histories", "quotient_history_event_multisets",
                   "quotient_histories_arena",
                   "quotient_histories_link",
                   "quotient_histories_ordered_arena",
                   "quotient_histories_ordered_link", "quotient_fields",
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
    """the search's exhaustiveness carries a HYPOTHESIS, and the hypothesis is
    gated rather than assumed (K1 m8): the one-fresh-label menu is complete
    only over a connected block hypergraph."""
    ok = (P["class_cast_solutions"] == 1 and P["class_cast_matches_declared"]
          and P["recon_set_equality"] and P["recon_certificate"] == "CERTIFIED"
          and P["recon_cast_size"] == P["arena_sites"]
          and P["class_blocks_components"] == 1
          and P["recon_coordinate_invariant"]
          and P["recon_second_coordinate_certificate"] == "CERTIFIED")
    return ok, fmt(P, "cast solutions {class_cast_solutions} certificate "
                      "{recon_certificate} reconstructed cast "
                      "{recon_cast_size} threshold {recon_threshold} block "
                      "components {class_blocks_components}",
                   "class_cast_solutions", "recon_certificate",
                   "recon_cast_size", "recon_threshold",
                   "class_blocks_components")


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
          and len({a["arm"] for a in arms}) == len(arms)
          # THE PROBE'S REAL WIDTH (K1 M1): distinct arm NAMES were gated and
          # distinct arm INPUTS were not, so five arms handing one record read
          # as five probes.  Both are now measured and the head carries both.
          and len({a["record"] for a in arms}) == P["q58_distinct_inputs"]
          and P["q58_distinct_inputs"] < P["q58_arms_total"]
          and P["q58_distinct_recovering_inputs"]
          + P["q58_distinct_refusing_inputs"] == P["q58_distinct_inputs"])
    return ok, fmt(P, "arms {q58_arms_total} distinct inputs "
                      "{q58_distinct_inputs} recovering {q58_arms_recovering} "
                      "from {q58_distinct_recovering_inputs} refusing "
                      "{q58_arms_refusing} from {q58_distinct_refusing_inputs} "
                      "triangular {q58_triangular_arms}",
                   "q58_arms_total", "q58_distinct_inputs",
                   "q58_arms_recovering", "q58_distinct_recovering_inputs",
                   "q58_arms_refusing", "q58_distinct_refusing_inputs",
                   "q58_triangular_arms")


def g_q58_verdict(P):
    """the criterion DECIDES THE ARMS and is measured NOT to be sufficient off
    them (K2 MAJOR-1): the domain probe exhibits triangle-writing block sets
    at total cover that do not return the cast, and one non-triangular set
    that does."""
    ok = (P["q58_arms_recovering"] > 1 and P["q58_arms_refusing"] > 0
          and P["q58_split_is_triangularity"]
          and not P["q58_split_is_the_block_size"]
          and len(P["q58_mechanism_kinds"]) > 1
          and P["q58_domain_triangular_failures"] > 0
          and P["q58_domain_failures_at_total_cover"] > 0
          and P["q58_domain_nontriangular_recovering"] > 0
          and not P["q58_criterion_holds_on_every_triangle_writer"]
          and not P["q58_criterion_refuses_every_non_triangle_writer"]
          and P["q58_domain_prefixes_below_the_cover"]
          == P["q58_domain_prefixes_declared"])
    return ok, fmt(P, "recovering {q58_arms_recovering} refusing "
                      "{q58_arms_refusing} triangularity decides the arms "
                      "{q58_split_is_triangularity} block size decides "
                      "{q58_split_is_the_block_size} domain probes "
                      "{q58_domain_probe_count} triangle-writing failures "
                      "{q58_domain_triangular_failures} of them at total cover "
                      "{q58_domain_failures_at_total_cover} non-triangular "
                      "recoveries {q58_domain_nontriangular_recovering}",
                   "q58_arms_recovering", "q58_arms_refusing",
                   "q58_split_is_triangularity", "q58_split_is_the_block_size",
                   "q58_domain_probe_count", "q58_domain_triangular_failures",
                   "q58_domain_failures_at_total_cover",
                   "q58_domain_nontriangular_recovering")


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
          and P["param_free"] > 0
          # #295: the class words are carried by measured predicates, and the
          # DERIVED count is exactly the number of satisfied selection laws
          and P["param_derived"] == P["param_laws_satisfied"]
          == P["param_laws_declared"]
          and P["param_selected_by_a_law"] == P["param_laws_satisfied"]
          and not P["param_class_predicate_failures"]
          and P["param_class_predicates"] > 0
          # every object the census classes DECLARED is priced here (K2
          # MAJOR-5a): the census and the parameter table are reconciled
          and P["param_declared_objects_unpriced"] == 0)
    return ok, fmt(P, "declarations {param_total} free {param_free} invariant "
                      "{param_invariant} derived {param_derived} "
                      "reconstructed-conditionally {param_reconstructed} "
                      "initial {param_initial} free rows a law selects "
                      "{param_free_selected_by_a_law} selection laws declared "
                      "{param_laws_declared} satisfied {param_laws_satisfied} "
                      "class predicates {param_class_predicates}",
                   "param_total", "param_free", "param_invariant",
                   "param_derived", "param_reconstructed", "param_initial",
                   "param_free_selected_by_a_law", "param_laws_declared",
                   "param_laws_satisfied", "param_class_predicates")


def g_outcomes(P):
    """#299-extended: reachable AND argued feasible against this corpus, per
    row, with no two rows sharing a feasibility sentence."""
    rows = P["outcome_controls"]
    ok = (all(want == got for want, got, _w, _f in rows)
          and len(rows) == P["outcome_words"]
          and P["outcome_feasibility_distinct"] == P["outcome_words"]
          and P["outcome_measured_witnesses"] > 0
          and all(w in ("MEASURED-HERE", "ARGUED") for _x, _g, w, _f in rows))
    return ok, fmt(P, "outcome words {outcome_words} reachable "
                      "{outcome_reachable} feasibility sentences "
                      "{outcome_feasibility_distinct} witnesses measured here "
                      "{outcome_measured_witnesses}",
                   "outcome_words", "outcome_reachable",
                   "outcome_feasibility_distinct",
                   "outcome_measured_witnesses")


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
        _fam("T-ANCHOR-CONSUMED")
        CTX["anchors"].verify_consumption(CTX["ledger"])
        bad = ""
    except ET.CheckFail as exc:
        bad = exc.detail
    # the measured split (K3 MAJOR-7): nine anchors have a DIGIT parsed out of
    # the located text, two a SPELLED numeral, one an engraved INDEX, and
    # exactly one carries no numeral at all -- that one is declared WORD-bound
    # and backs no published cardinality.
    P["anchor_bindings"] = sorted(collections.Counter(
        ANCHOR_BINDING[n] for n in A.by_name).items())
    P["anchor_numeral_bound"] = sum(
        1 for n in A.by_name if ANCHOR_BINDING[n] != "WORD")
    P["anchor_word_bound"] = sum(
        1 for n in A.by_name if ANCHOR_BINDING[n] == "WORD")
    cited_backings = {r["object"] for r in P["census_rows"]
                      if r["backing"] == "SEALED-CITATION"}
    P["census_cited_rows"] = sorted(cited_backings)
    P["census_cited_rows_on_word_bound_anchors"] = sum(
        1 for o in cited_backings
        if ANCHOR_BINDING.get(CENSUS_CITED_ANCHOR.get(o, ""), "WORD") == "WORD")
    ok = ((not bad) and P["anchor_unconsumed"] == 0
          and P["anchor_phantom_consumers"] == 0
          and P["anchor_numeral_bound"] + P["anchor_word_bound"]
          == P["anchor_count"]
          and P["census_cited_rows_on_word_bound_anchors"] == 0)
    return ok, fmt(P, "anchors {anchor_count} consumers {anchor_consumers} "
                      "unconsumed {anchor_unconsumed} phantom "
                      "{anchor_phantom_consumers} numeral-bound "
                      "{anchor_numeral_bound} word-bound {anchor_word_bound}",
                   "anchor_count", "anchor_consumers", "anchor_unconsumed",
                   "anchor_phantom_consumers", "anchor_numeral_bound",
                   "anchor_word_bound")


def g_claims(P):
    try:
        _fam("T-CLAIMS-EQUAL")
        got = CTX["claims"].gate(CTX["paper"])
        bad = ""
    except ET.CheckFail as exc:
        got, bad = {}, exc.detail
    ok = not bad
    CTX["claims_counts"] = got
    return ok, fmt(P, "rows {claim_rows} prose {claim_prose} fences {claim_fences}",
                   "claim_rows", "claim_prose", "claim_fences")


def spell_out(text):
    """the paper's SPELLED numerals, rewritten as digits, so that the same
    per-occurrence referent gate that binds `27` also binds `twenty-seven`
    (K3 MAJOR-6: NUM matches digits only, and 92 prose numerals sat outside
    every numeral gate)."""
    words = sorted(((w, v) for v, w in SPELLED.items()),
                   key=lambda kv: -len(kv[0]))
    out = text
    for w, v in words:
        out = re.sub(r"(?<![\w-])%s(?![\w-])" % w, str(v), out,
                     flags=re.IGNORECASE)
    return out


def count_spelled(text):
    words = {w for w in SPELLED.values()}
    return sum(1 for m in re.finditer(r"[A-Za-z][A-Za-z-]*", text)
               if m.group(0).casefold() in words)


# The DISCRIMINATING noun of each universe: a whole word that says what the
# sentence is about, as against the registry's own prefix list, which routes on
# common words like class, event and object.  The ambiguity leg below scores on
# these.
AMBIGUITY_NOUNS = {
    "THE-INVARIANCE": ("relabelling", "relabellings", "stabilizer",
                       "automorphism", "automorphisms", "orbit", "orbits",
                       "quotient", "splitting", "splittings", "naming",
                       "namings"),
    "THE-ARMS": ("arm", "arms", "mechanism", "mechanisms", "reconstructor"),
    "THE-PARAMETERS": ("declaration", "declarations", "parameter",
                       "parameters", "fiber", "fibers"),
    "THE-STATE": ("amplitude", "amplitudes", "residue", "residues",
                  "successor", "successors"),
    "THE-RECORD": ("history", "histories", "record", "records", "block",
                   "blocks"),
    "THE-ARENA": ("arena", "cell", "cells", "site", "sites", "actor",
                  "actors", "grouping", "groupings"),
}


def strict_referents(prose, ref):
    """THE AMBIGUITY LEG (K3 MINOR-4).  The registry routes a sentence to the
    FIRST universe whose noun it carries, so a sentence that names two
    universes can launder one's numerals into the other's subject.  Here every
    universe the sentence names BY ITS DISCRIMINATING NOUN is scored, and a
    numeral must belong to ALL of them."""
    unis = ref.universes
    offences, checked = [], 0
    for sentence in re.split(r"(?<=[.!?])\s+", prose):
        s = ET.canon(sentence)
        hit = [n for n in unis
               if any(re.search(r"\b%s\b" % re.escape(w), s)
                      for w in AMBIGUITY_NOUNS[n])]
        if len(hit) < 2:
            continue
        spans = [m.span() for m in ET.ReferentRegistry.NOF.finditer(sentence)]
        for m in ET.ReferentRegistry.NUM.finditer(sentence):
            if any(a <= m.start() < b for a, b in spans):
                continue
            v = int(m.group(1).replace(",", ""))
            checked += 1
            missing = [n for n in hit if v not in unis[n]["values"]]
            if missing:
                offences.append("%d is not a value of %s in a sentence that "
                                "also names %s" % (v, missing[0], hit))
    return checked, offences


def g_referents(P):
    prose = _paper_prose(CTX["paper"])
    checked, bad = 0, ""
    try:
        _fam("T-REFERENT-BOUND")
        got = CTX["ref"].gate(prose)
        checked += got["occurrences_checked"]
    except ET.CheckFail as exc:
        bad = exc.detail
    if not bad:
        try:
            got2 = CTX["ref"].gate(spell_out(prose))
            checked += got2["occurrences_checked"]
            P["referent_spelled_occurrences"] = (
                got2["occurrences_checked"] - got["occurrences_checked"])
        except ET.CheckFail as exc:
            bad = "spelled: " + exc.detail
    amb, amb_off = strict_referents(spell_out(prose), CTX["ref"])
    P["referent_ambiguous_occurrences"] = amb
    P["referent_ambiguity_offences"] = sorted(set(amb_off))
    P["referent_occurrences"] = checked
    P["referent_spelled_numerals"] = count_spelled(prose)
    CTX["referent_detail"] = bad
    ok = ((not bad) and checked > 0 and P["referent_spelled_numerals"] > 0
          and not P["referent_ambiguity_offences"])
    return ok, fmt(P, "universes {referent_universes} occurrences checked "
                      "{referent_occurrences} spelled numerals in the prose "
                      "{referent_spelled_numerals} of them newly bound "
                      "{referent_spelled_occurrences} cross-universe "
                      "occurrences {referent_ambiguous_occurrences}",
                   "referent_universes", "referent_occurrences",
                   "referent_spelled_numerals", "referent_spelled_occurrences",
                   "referent_ambiguous_occurrences")


def g_walls(P):
    order = CTX["anchors"].read("PLAN-WALLS", "G-WALLS")
    named = [w.name for w in CTX["walls"]]
    # the engraving's own INDEX is parsed out of the located text and compared
    # with the number of standing walls this run built (K3 MAJOR-7: the old
    # predicate was a substring test on the module's own literal).
    engraved = sorted({int(m.group(1))
                       for m in re.finditer(r"\bw(\d)\s*:", ET.canon(order))})
    P["wall_engraved_indices"] = engraved
    P["wall_engraved_count"] = len(engraved)
    standing_present = (all(s in named for s in STANDING_WALLS)
                        and len(engraved) == P["wall_standing"])
    bad = [] if standing_present else ["the two standing walls are not built"]
    for w in CTX["walls"]:
        if not w.licences:
            bad.append("%s: empty licence pool" % w.name)
        try:
            _fam("T-WALL-SEMANTIC")
            w.scan(CTX["paper"], CTX["claim_texts"])
        except ET.CheckFail as exc:
            bad.append(exc.detail)
    rows, off = wall_probe_report(CTX["walls"], CTX["paper"],
                                  CTX["claim_texts"])
    P["wall_probe_rows"] = rows
    P["wall_probes"] = len(rows)
    P["wall_probes_surviving"] = len(off)
    P["wall_probe_legs"] = sorted(collections.Counter(
        r["died_at_leg"] for r in rows).items())
    P["wall_probes_copying_a_pattern_literal"] = sum(
        1 for r in rows if r["copied_pattern_literals"])
    bad.extend(off)
    ok = not bad
    return ok, fmt(P, "walls {wall_count} patterns {wall_patterns} standing "
                      "sentences {wall_positives} policed {wall_policed} "
                      "controls {wall_probes} surviving "
                      "{wall_probes_surviving}",
                   "wall_count", "wall_patterns", "wall_positives",
                   "wall_policed", "wall_probes", "wall_probes_surviving")


def g_typed(P):
    P["typed_count_offence_count"] = len(P["typed_count_offences"])
    ok = (not P["typed_count_offences"]
          and P["exempt_tokens_unused"] == 0)
    return ok, fmt(
        P, "statement builders audited {typed_callers} offences "
           "{typed_count_offence_count} exemptions {exempt_tokens} unused "
           "{exempt_tokens_unused}",
        "typed_callers", "typed_count_offence_count", "exempt_tokens",
        "exempt_tokens_unused")


def g_receipt_types(P):
    """the walk runs BEFORE this gate (PRE_GATE) and writes what it found, so
    neither conjunct is constant and `receipt_leaves` is the walk's own count
    (K3 MAJOR-8: it was a typed zero, and false)."""
    P["receipt_type_offence_count"] = len(P["receipt_type_offences"])
    return not P["receipt_type_offences"], fmt(
        P, "receipt leaves {receipt_leaves} type offences "
           "{receipt_type_offence_count}",
        "receipt_leaves", "receipt_type_offence_count")


def g_head(P):
    """THE HEAD IS TOTAL BY CONSTRUCTION (K3 MAJOR-1).  Every `KEY=` position
    present in the emitted string is parsed back out by a reader that shares
    no code and no literal with the builder, and compared, as an integer,
    against the receipt leaf it names -- including BOTH halves of every
    compound `A-OF-B` field.  A position the string carries and the field
    table does not name is a STRAY and fails here."""
    bad, parsed = [], 0
    for seg, want in zip(P["head_segments"], HEAD_FIELDS):
        got = k_parse_head(seg)
        named = {f for f, _k in want}
        for field in sorted(got):
            if field not in named:
                bad.append("stray head position " + field)
        for field, key in want:
            if field not in got:
                bad.append("absent " + field)
                continue
            values = got[field]
            keys = key if isinstance(key, tuple) else (key,)
            if len(values) != len(keys):
                bad.append("arity " + field)
                continue
            for v, k in zip(values, keys):
                parsed += 1
                if v != P[k]:
                    bad.append("moved " + field)
    P["head_fields_parsed"] = parsed
    P["head_mismatches"] = len(bad)
    P["head_positions_emitted"] = sum(
        sum(len(v) for v in k_parse_head(s).values())
        for s in P["head_segments"])
    ok = (not bad and len(P["head_segments"]) == len(HEAD_FIELDS)
          and parsed == P["head_positions_emitted"])
    return ok, fmt(P, "segments {head_segment_count} numeral positions emitted "
                      "{head_positions_emitted} parsed back "
                      "{head_fields_parsed} mismatches {head_mismatches}",
                   "head_segment_count", "head_positions_emitted",
                   "head_fields_parsed", "head_mismatches")


def g_transcript(P):
    """the transcript reconciled with the ledger BY CONTENT.  The stray and
    missing counts are MEASURED before this gate from the multiset difference
    (K3 MAJOR-8: two of the three conjuncts were constant-True)."""
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

# THE ONE-INSTANT PHYSICAL STATE.  The branch weight is NOT here: it is
# ensemble-side bookkeeping, carried once in STATE_ENSEMBLE below (v15 #33,
# the ECC charter's state-vs-ensemble split).  The first delivery listed it as
# a state component AND described it as bookkeeping, which is two
# classifications of one object.
STATE_COMPONENTS = (
    ("THE-COUNT-FIELD", "one non-negative integer per cell",
     "the geometry: the division count the weld identifies with the metric"),
    ("THE-AMPLITUDE", "one ring element per cell",
     "the quantum state the coin and the shift act on"),
)

# ENSEMBLE-SIDE BOOKKEEPING.  It travels with a run and it is not a component
# of the state at one instant; the screening measurement above never reads it.
STATE_ENSEMBLE = (
    ("THE-BRANCH-WEIGHT", "one exact rational",
     "ensemble-side bookkeeping: the weight the emission law multiplies along "
     "a branch, carried to compare runs and never read by the one-instant "
     "update"),
)

STATE_BACKGROUND = (
    ("THE-ACTOR-SET", "the cast the arena declares"),
    ("THE-DIRECTION-DECLARATION", "which classes are links"),
    ("THE-COIN", "the covariant unitary chosen from its family"),
    ("THE-ORDER", "coin before or after the residue"),
    ("THE-ORIENTATION", "the sign of the shift"),
    ("THE-READING", "the Born menu or the record menu"),
)

# EVERY numeral position of the head, including BOTH halves of every compound
# `A-OF-B` field.  A tuple of keys is a compound position; g_head additionally
# fails on any `KEY=` position the string carries that this table does not
# name, so the check is TOTAL BY CONSTRUCTION (K3 MAJOR-1).
HEAD_FIELDS = (
    (("OBJECTS", "census_row_count"),
     ("DISTINCT-EXTENTS", "census_distinct_extents"),
     ("COMPUTED-HERE", "census_computed_here"),
     ("CITED", "census_cited"), ("ACTORS", "arena_sites"),
     ("CELLS", "arena_cells"), ("EVENTS-REALISED", "corpus_distinct_events"),
     ("HISTORIES", "corpus_distinct_histories"), ("BLOCKS", "record_blocks"),
     ("COUNT-FIELDS", "record_count_fields"), ("MENU", "arena_menu"),
     ("CHART-CLASSES", "inv_link_graph_automorphisms")),
    (("STATE-COMPONENTS", "state_components"),
     ("ENSEMBLE-SIDE-BOOKKEEPING", "state_ensemble_components"),
     ("BACKGROUND", "state_background_components"),
     ("COUNT-FIELDS", "record_count_fields"),
     ("RESIDUE-FIELDS", "record_residue_fields"),
     ("SUCCESSORS", "state_successors_distinct"),
     ("EQUAL-RESIDUE-PAIRS-AGREEING",
      ("state_equal_residue_agreements", "state_equal_residue_pairs")),
     ("DISTINCT-RESIDUE-COLLISIONS-AT-THE-UNIFORM-AMPLITUDE",
      ("state_distinct_residue_collisions", "state_distinct_residue_pairs")),
     ("DISTINCT-RESIDUE-COLLISIONS-AT-A-SINGLE-CELL-AMPLITUDE",
      ("state_single_cell_collisions", "state_single_cell_pairs")),
     ("BORN-MENU-VALUES", "state_reading_a_born_values"),
     ("RELABELLINGS", "inv_symmetric_group"),
     ("LAW-STABILIZER", "inv_law_stabilizer"),
     ("ARENA-STABILIZER", "inv_arena_automorphisms"),
     ("DIRECTION-INDEX", "inv_direction_index"),
     ("SPLITTINGS", "inv_direction_splittings"),
     ("LOCAL-GROUP", "inv_local_group_order"),
     ("LOCAL-COLLAPSE-WIDTH", "inv_local_collapse_width"),
     ("HISTORY-EVENT-MULTISETS", "quotient_history_event_multisets"),
     ("HISTORIES-SURVIVING",
      ("quotient_histories_link", "quotient_history_event_multisets")),
     ("HISTORIES-ORDER-KEPT-SURVIVING",
      ("quotient_histories_ordered_link", "quotient_histories")),
     ("FIELDS-SURVIVING", ("quotient_fields_link", "quotient_fields"))),
    (("CYCLE-LENGTH", "dep_cycle_length"),
     ("ACTOR-RECORD-CYCLE-LENGTH", "dep_actor_record_cycle_length"),
     ("CAST-SOLUTIONS", "class_cast_solutions"),
     ("RESIDUE", "class_cast_residue"), ("ARMS", "q58_arms_total"),
     ("DISTINCT-INPUTS", "q58_distinct_inputs"),
     ("RECOVERING", "q58_arms_recovering"),
     ("RECOVERING-INPUTS", "q58_distinct_recovering_inputs"),
     ("REFUSING", "q58_arms_refusing"),
     ("REFUSING-INPUTS", "q58_distinct_refusing_inputs")),
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
        "census", ("object", "class", "cardinality", "what the number counts",
                   "backing", "reading"),
        [(r["object"], r["class"], com(r["cardinality"]), r["counts"],
          r["backing"], r["reading"]) for r in P["census_rows"]])
    R["state"] = claims.table(
        "state", ("component", "shape", "what it carries"),
        [(a, b, c) for (a, b, c) in STATE_COMPONENTS])
    R["ensemble"] = claims.table(
        "ensemble", ("quantity", "shape", "what it carries"),
        [(a, b, c) for (a, b, c) in STATE_ENSEMBLE])
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
         ("post-coin state vectors", com(P["state_reading_a_post_coin_vectors"])),
         ("Born-menu values", com(P["state_reading_a_born_values"])),
         ("record-menu values", com(P["state_reading_b_menus"]))])
    R["amplitudes"] = claims.table(
        "amplitudes", ("amplitude", "one-step successors",
                       "equal-residue pairs agreeing",
                       "distinct-residue pairs colliding",
                       "Born-menu values"),
        [(nm, com(succ), "%s of %s" % (com(agree), com(pairs)),
          "%s of %s" % (com(coll), com(dpairs)), com(born))
         for (nm, succ, agree, pairs, coll, dpairs, born, _pc)
         in P["state_amplitude_rows"]])
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
        "quotient", ("object", "before", "modulo the arena",
                     "modulo the links"),
        [("histories, order kept", com(P["quotient_histories"]),
          com(P["quotient_histories_ordered_arena"]),
          com(P["quotient_histories_ordered_link"])),
         ("event multisets, order forgotten",
          com(P["quotient_history_event_multisets"]),
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
        "arms", ("mechanism", "kind", "the record it hands over",
                 "actors per event", "blocks", "block sizes", "certificate",
                 "cast recovered"),
        [(a["arm"], a["mechanism"], a["record"], com(a["event_arity"]),
          com(a["blocks"]),
          "+".join("%s x %s" % (com(n), com(s)) for s, n in a["block_sizes"]),
          a["certificate"], "yes" if a["cast_recovered"] else "no")
         for a in P["q58_arms"]])
    R["domain"] = claims.table(
        "domain", ("block set", "blocks", "all blocks triangular",
                   "tokens covered", "certificate", "cast recovered"),
        [(p["probe"], com(p["blocks"]),
          "yes" if p["all_blocks_triangular"] else "no",
          com(p["tokens_covered"]), p["certificate"],
          "yes" if p["cast_recovered"] else "no")
         for p in P["q58_domain_probes"]])
    R["parameters"] = claims.table(
        "parameters", ("declaration", "what it fixes", "fiber", "class",
                       "a measured law selects it", "where it is measured"),
        [(a, b, c, d, e, f) for (a, b, c, d, e, f) in P["param_rows"]])
    R["outcomes"] = claims.table(
        "outcomes", ("pre-registered word", "witness",
                     "what would make this corpus read it"),
        [(w, wit, feas) for w, _g, wit, feas in P["outcome_controls"]])
    R["sources"] = claims.table(
        "sources", ("path", "sha256-12"),
        [(k, v) for k, v in sorted(SOURCES.items())])
    return R


def spelled_name(P, name):
    """a count, spelled, entered in the registry under its own name so that a
    prose sentence carrying it in words is INTERPOLATED and never typed."""
    cr = CTX["cr"]
    key = name + "_spelled"
    cr.measured(key, SPELLED[P[name]], "spelled from a count this run made")
    return key


def spelled_claims(P):
    """The prose sentences whose load-bearing count is written IN WORDS.
    Every one is rendered from the payload and registered as a claim, so an
    inversion of the words dies at G-CLAIMS-EQUAL rather than sitting outside
    every numeral gate (K3 MAJOR-6, the Q58 headline inversion)."""
    cr = CTX["cr"]

    def made(template, *names):
        keys = [spelled_name(P, n) for n in names]
        return cr.stmt(template, **{k: None for k in keys})
    return (
        made("Run through {q58_arms_total_spelled} mechanisms, the cast comes "
             "back at {q58_arms_recovering_spelled} and does not at "
             "{q58_arms_refusing_spelled}: at "
             "{q58_arms_certificate_rejected_spelled} the rule ran and its "
             "own membership certificate rejected the cast it built, and at "
             "{q58_arms_declined_spelled} -- both grains of the coupled "
             "walk's own emission law -- the record carries no co-writing to "
             "threshold, so the rule declines and returns none.",
             "q58_arms_total", "q58_arms_recovering", "q58_arms_refusing",
             "q58_arms_certificate_rejected", "q58_arms_declined"),
        made("The {q58_arms_total_spelled} arms hand the reconstructor "
             "{q58_distinct_inputs_spelled} distinct block sets between them, "
             "of which {q58_distinct_recovering_inputs_spelled} recovers the "
             "cast and {q58_distinct_refusing_inputs_spelled} refuse.",
             "q58_arms_total", "q58_distinct_inputs",
             "q58_distinct_recovering_inputs", "q58_distinct_refusing_inputs"),
        made("{census_cited_spelled} rows are citations rather than "
             "computations, and their objects belong to units this one does "
             "not rebuild.",
             "census_cited"),
        made("{param_derived_spelled} rows are DERIVED and say so, each "
             "carrying the measured predicate that selects it; "
             "{param_invariant_spelled} are invariant in the substrate "
             "census; {param_reconstructed_spelled} is reconstructed "
             "conditionally; {param_initial_spelled} are initial conditions; "
             "and the rest are free.",
             "param_derived", "param_invariant", "param_reconstructed",
             "param_initial"),
        made("The census names {census_row_count_spelled} rows and "
             "{census_distinct_extents_spelled} distinct extents, because the "
             "weld's dictionary identifies the sites with the actors and the "
             "carrier typing identifies the co-division pairs and the carrier "
             "candidate with the cells.",
             "census_row_count", "census_distinct_extents"),
    )


def claim_texts(P):
    """the rendered claim set: the fixed sentences, and the ones whose count
    is computed."""
    return tuple(CLAIM_TEXTS) + tuple(spelled_claims(P))


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
    "The reconstruction is not generator-independent. Of the mechanisms the "
    "corpus supplies, those whose blocks are triangles covering every token "
    "recover the cast and the others do not, so triangularity with total "
    "cover decides every arm. It is not a sufficient condition beyond them: "
    "the domain probe exhibits triangle-writing block sets at total cover on "
    "which the rule does not return the declared cast, and one non-triangular "
    "block set on which it does, so the criterion is stated as what separates "
    "these arms and not as a property of mechanisms.",
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
    _fam("T-READ-SET")
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

    anchors = ET.AnchorSet([ET.Anchor(n, needle, s, c, floor=40)
                            for (n, s, c, needle, _b) in ANCHORS])
    sources_text = {s: read_text(s) for s in {a[1] for a in ANCHORS}}
    anchors.locate(sources_text, paper if paper else None)

    P = measure()
    census_payload(P, anchors)
    if mode == "--render":
        for _n, _s, _c, _needle, _b in ANCHORS:
            anchors.read(_n, _c)
    P["anchor_count"] = len(ANCHORS)
    P["anchor_consumers"] = len({a[2] for a in ANCHORS})
    P["source_count"] = len(SOURCES)
    P["source_mismatches"] = mismatch
    P["source_mismatch_count"] = len(mismatch)
    P["float_offences"] = audit_no_floats(src)
    P["float_offence_count"] = len(P["float_offences"])
    P["region_reach_offences"] = audit_regions(src)
    P["region_alias_offences"] = audit_alias_routes(src)
    P["region_constant_offences"] = audit_declared_constants(src)
    P["region_reach_offence_count"] = len(P["region_reach_offences"])
    P["region_alias_offence_count"] = len(P["region_alias_offences"])
    P["region_constant_offence_count"] = len(P["region_constant_offences"])
    P["region_offences"] = (P["region_reach_offences"]
                            + P["region_alias_offences"]
                            + P["region_constant_offences"])
    P["region_offence_count"] = len(P["region_offences"])
    P["region_legs"] = 3
    P["region_census"] = sorted(region_census(src).items())
    P["region_count"] = len(P["region_census"])
    P["region_declared_constants"] = len(DECLARED_CONSTANTS)
    P["template_families"] = len(ET.FAMILIES)
    P["template_families_live"] = 0
    P["template_families_expected"] = 0
    P["template_family_counts"] = []
    P["template_families_unexercised"] = []
    P["template_families_declared_out_of_mode"] = []
    P["outcome_controls"] = [list(r) for r in outcome_controls(P)]
    P["outcome_words"] = len(P["outcome_controls"])
    P["outcome_reachable"] = sum(
        1 for w, g, _wit, _f in P["outcome_controls"] if w == g)
    P["outcome_feasibility_distinct"] = len(
        {f for _w, _g, _wit, f in P["outcome_controls"]})
    P["outcome_measured_witnesses"] = sum(
        1 for _w, _g, wit, _f in P["outcome_controls"] if wit == "MEASURED-HERE")

    segs, words = head_segments(P)
    P["head_segments"] = segs
    P["head_words"] = list(words)
    P["head_segment_count"] = len(segs)
    P["head_fields_parsed"] = 0
    P["head_positions_emitted"] = 0
    P["head_mismatches"] = 0

    claims = ET.Claims()
    render = build_render(P, claims)
    texts = claim_texts(P)
    P["claim_texts_fixed"] = len(CLAIM_TEXTS)
    P["claim_texts_rendered"] = len(texts) - len(CLAIM_TEXTS)
    for t in texts:
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
    P["referent_spelled_numerals"] = 0
    P["referent_spelled_occurrences"] = 0
    P["referent_ambiguous_occurrences"] = 0
    P["referent_ambiguity_offences"] = []

    walls = wall_objects(texts)
    P["wall_count"] = len(walls)
    P["wall_patterns"] = sum(len(w.negative) for w in walls)
    P["wall_positives"] = sum(len(w.positive) for w in walls)
    P["wall_policed"] = sum(len(w.policed) for w in walls)
    P["wall_licence_pools"] = sum(1 for w in walls if w.licences)
    P["wall_standing"] = sum(1 for w in walls if w.name in STANDING_WALLS)
    P["wall_probes"] = len(WALL_PROBES)
    P["wall_probes_surviving"] = 0
    P["wall_probe_rows"] = []
    P["wall_probe_legs"] = []
    P["wall_probes_copying_a_pattern_literal"] = 0
    P["wall_engraved_indices"] = []
    P["wall_engraved_count"] = 0
    P["wall_control_copies_a_pattern_literal"] = sum(
        1 for w in walls for pat in w.negative
        for lit in _pattern_literals(pat)
        if lit in MUT_WALL_SENTENCE.casefold())

    P["typed_callers"] = len(TYPED_CALLERS)
    _fam("T-NO-TYPED-COUNTS")
    P["typed_count_offences"] = (cr.audit_module(src, TYPED_CALLERS)
                                 + audit_typed_deep(src, TYPED_CALLERS,
                                                    tuple(cr.exempt))
                                 + audit_typed_constants(src, TYPED_CALLERS))
    P["typed_count_offence_count"] = len(P["typed_count_offences"])
    P["exempt_tokens"] = len(EXEMPT_TOKENS)
    P["exempt_tokens_unused"] = sum(1 for t, _w in EXEMPT_TOKENS if t not in src)
    P["receipt_type_offences"] = []
    P["receipt_type_offence_count"] = 0
    P["receipt_leaves"] = 0
    P["transcript_preamble"] = 2
    P["transcript_rows"] = 0
    P["ledger_rows"] = 0
    P["transcript_stray"] = 0
    P["transcript_missing"] = 0
    P["transcript_digest"] = ""
    P["reads_declared"] = len(SOURCES) + 1
    P["reads_unpinnable"] = 1
    P["reads_stray"] = 0
    P["reads_never"] = 0
    P["reads_distinct"] = 0
    P["reads_after_the_gate"] = 0
    P["anchor_unconsumed"] = 0
    P["paper_digest"] = ET.bytes_digest(paper.encode("utf-8"))
    P["mode"] = mode
    P["mutant"] = mutant or "none"

    led = ET.Ledger()
    tr = ET.Transcript()
    seal = ET.Seal()
    CTX.update({"paper": paper, "claims": claims, "claim_texts": list(texts),
                "ref": ref, "anchors": anchors, "walls": walls, "ledger": led,
                "transcript": tr, "seal": seal,
                "src": src, "template": tpl_text, "render": render,
                "c1_first": [h for t, h in b_build_corpus()[0] if t == "C1"][0]})

    # T-FALSIFIER-POISONS, EXERCISED ON THE DELIVERY PATH (K3 MAJOR-3): the
    # harness is handed a copy of this run's own payload and a real recipe, and
    # it -- not this module -- checks that the recipe moved its declared target
    # and died at its declared gate.
    P["delivery_falsifier"] = delivery_falsifier_probe(P)
    P["delivery_falsifier_moved"] = bool(P["delivery_falsifier"]["target_moved"])
    P["delivery_falsifier_gate"] = P["delivery_falsifier"]["died_at"]

    # a mutant that names a CLOSING gate is applied at that gate and not here:
    # the key it moves is not measured until the ordinary loop has closed.
    if mutant and MUTANTS[mutant]["gate"] not in CLOSING_GATES:
        MUTANTS[mutant]["apply"](P)

    # an opaque leaf must die AT ITS OWN GATE'S NAME and as a CheckFail, not as
    # a raw TypeError out of the serializer the first seal happens to call
    # (K3 MAJOR-8's INJ-17).  The walk runs once here, once at the gate, and
    # once more at the door.
    _early = []
    receipt_type_walk(P, _early)
    if _early:
        raise ET.CheckFail("G-RECEIPT-TYPES", "opaque leaves: %s" % _early[:4])

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
    closing = CLOSING_GATES
    for gid in GATE_ORDER:
        if gid in closing:
            continue
        if mode == "--render" and gid in paperless:
            continue
        if gid in PRE_GATE:
            PRE_GATE[gid](P)
        ok, ev = GATE_FN[gid](P)
        for k in sorted(P):
            if gate_of_key(k) == gid and k not in seal.seals \
                    and k not in UNSEALED_KEYS:
                _fam("T-SEAL-PROMOTION")
                seal.seal(k, P[k], gid)
        led.gate(gid, GATE_STATEMENT[gid], ok, ev)
        tr.row(gid, ok, ev)
        fired.append(gid)

    # -- the closing gates -------------------------------------------------
    # the reconciliation is MEASURED here, before the gate that publishes it
    _fam("T-TRANSCRIPT-BOUND")
    _want = collections.Counter((r["gate"], r["passed"], r["evidence"])
                                for r in led.rows)
    _got = tr.parse()
    P["transcript_stray"] = sum((_got - _want).values())
    P["transcript_missing"] = sum((_want - _got).values())
    P["transcript_rows"] = sum(_got.values()) + P["transcript_preamble"]
    P["ledger_rows"] = len(led.rows) + P["transcript_preamble"]
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
    # the execution census is taken LAST, when every family that runs in this
    # mode has run (K3 MAJOR-3).
    _counts = dict(CTX.get("fam", {}))
    P["template_family_counts"] = sorted(
        [cid, _counts.get(cid, 0)] for (_l, _n, cid) in ET.FAMILIES)
    P["template_families_declared_out_of_mode"] = sorted(
        PAPERLESS_FAMILIES) if mode == "--render" else []
    if mutant and MUTANTS[mutant]["gate"] == "G-TEMPLATE-EXERCISED":
        MUTANTS[mutant]["apply"](P)
    ok, ev = GATE_FN["G-TEMPLATE-EXERCISED"](P)
    for k in sorted(P):
        if gate_of_key(k) == "G-TEMPLATE-EXERCISED" and k not in seal.seals:
            seal.seal(k, P[k], "G-TEMPLATE-EXERCISED")
    led.gate("G-TEMPLATE-EXERCISED", GATE_STATEMENT["G-TEMPLATE-EXERCISED"],
             ok, ev)
    tr.row("G-TEMPLATE-EXERCISED", ok, ev)

    P["gates"] = len(led.rows)
    P["ledger_head"] = led.recompute_chain()

    tr.say("")
    tr.say("VERDICT")
    for s in segs:
        tr.say("  " + s)
    text = tr.text()
    # THE SECOND ARTIFACT IS SEALED (K3 MAJOR-2).  The bind result is not
    # discarded: it becomes a payload leaf, it is sealed, and after promotion
    # the promoted bytes are re-read FROM DISK and compared against it, so a
    # transcript mutated between bind and promote cannot reach the tree.
    bound = tr.bind(led, text)
    P["transcript_digest"] = bound
    seal.seal("transcript_digest", bound, "G-TRANSCRIPT-BOUND")
    # the read set is re-evaluated at the DOOR, not only at its gate, so a read
    # taken after G-READS-DECLARED fired is still caught (K3 MINOR-3).
    _seen_late = collections.Counter(p for p in reads.log
                                     if not p.endswith(".tmp"))
    P["reads_after_the_gate"] = len(set(_seen_late) - set(declared))
    if P["reads_after_the_gate"] and mode != "--render":
        raise ET.CheckFail("T-READ-SET", "read after the read gate: %s"
                           % sorted(set(_seen_late) - set(declared)))
    bad = []
    receipt_type_walk(P, bad)          # the door's own re-walk; the gate-time
    if bad:                            # count is the sealed one and stands
        raise ET.CheckFail("G-RECEIPT-TYPES", "opaque leaves: %s" % bad[:4])

    for k, why in sorted(UNSEALED_KEYS.items()):
        if k not in seal.seals:
            seal.declare_unsealed(k, why)
    uncovered = sorted(k for k in P
                       if k not in seal.seals and k not in seal.unsealed)
    if uncovered and mode != "--render":
        raise ET.CheckFail("T-SEAL-PROMOTION",
                           "payload keys neither sealed at a gate nor "
                           "declared: %s" % uncovered)

    if write:
        _fam("T-SEAL-PROMOTION")
        digests = ET.promote(seal, led, P, text,
                             os.path.join(REPO, RECEIPT_REL),
                             os.path.join(REPO, OUTPUT_REL))
        with open(os.path.join(REPO, OUTPUT_REL), "rb") as fh:
            on_disk = fh.read()
        if ET.bytes_digest(on_disk) != bound or digests["side"] != bound:
            raise ET.CheckFail("T-SEAL-PROMOTION",
                               "the promoted transcript is not the bound "
                               "transcript")
    else:
        digests = {"receipt": bound, "side": bound}
    return P, led, tr, text, digests


EXEMPT_TOKENS = (("sha256-12", "the name of the digest format, not a count"),)

TYPED_CALLERS = ("stmt", "fmt", "claim", "fence", "table", "gate", "row", "say")


def _pre_receipt_types(P):
    """the type walk runs BEFORE its gate, so neither the offence list nor the
    leaf count is a constant the gate cannot move (K3 MAJOR-8).  A planted
    offence is APPENDED to, never erased by, this walk."""
    bad = list(P["receipt_type_offences"])
    P["receipt_leaves"] = receipt_type_walk(P, bad)
    P["receipt_type_offences"] = bad


PRE_GATE = {"G-RECEIPT-TYPES": _pre_receipt_types}


def delivery_falsifier_probe(P):
    """T-FALSIFIER-POISONS on the DELIVERY path.  The template's own harness
    is handed a copy of this run's payload and one real recipe; the harness
    refuses a recipe that leaves its declared target byte-identical, and
    refuses a death at any gate but the declared one."""
    _fam("T-FALSIFIER-POISONS")
    probe = ET.Falsifier(
        "MUT-DELIVERY-PROBE", "G-NO-FLOAT",
        "plants a float offence in a copy of this run's own payload",
        "float_offences", _hook("MUT-FLOAT"))
    H = ET.FalsifierHarness([probe])

    def build():
        return ({"float_offences": list(P["float_offences"]),
                 "float_offence_count": P["float_offence_count"]},
                ET.Ledger())
    return H.run_one(probe, build)


def audit_typed_constants(src, callers):
    """the taint leg (K3 MINOR-2): an int-valued MODULE constant, or a str()
    of one, reaching a statement builder is the same offence as a literal --
    the scan that only looks inside the call's own subtree is defeated at one
    remove."""
    tree = ast.parse(src)
    ints = set()
    for node in tree.body:
        if isinstance(node, ast.Assign) and isinstance(node.value, ast.Constant) \
                and isinstance(node.value.value, int) \
                and not isinstance(node.value.value, bool):
            for t in node.targets:
                if isinstance(t, ast.Name):
                    ints.add(t.id)
    out = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        fname = getattr(node.func, "attr", None) or getattr(node.func, "id", None)
        if fname not in callers:
            continue
        for sub in ast.walk(node):
            if isinstance(sub, ast.Name) and sub.id in ints:
                out.append("line %d: the module constant %s reaches a builder"
                           % (sub.lineno, sub.id))
    return out


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
                  (P["quotient_histories_link"],
                   P["quotient_history_event_multisets"]),
                  (P["quotient_histories_ordered_link"],
                   P["quotient_histories"]),
                  (P["quotient_fields_link"], P["quotient_fields"])})
    ref.universe("THE-ARMS", ["arm", "mechanism", "reconstructor",
                              "generating", "generator", "probe", "triangle"],
                 vals(["q58"]) | base,
                 {(P["q58_arms_recovering"], P["q58_arms_total"]),
                  (P["q58_arms_refusing"], P["q58_arms_total"]),
                  (P["q58_distinct_recovering_inputs"], P["q58_distinct_inputs"]),
                  (P["q58_distinct_refusing_inputs"], P["q58_distinct_inputs"]),
                  (P["q58_domain_failures_at_total_cover"],
                   P["q58_domain_triangular_failures"])})
    ref.universe("THE-PARAMETERS", ["parameter", "declaration", "fiber",
                                    "free item", "coin", "seam"],
                 vals(["param", "coin", "seam"]) | base,
                 {(P["param_free"], P["param_total"]),
                  (P["coin_grover_classes"], P["coin_classes"])})
    ref.universe("THE-STATE", ["state", "amplitude", "residue", "successor",
                               "menu", "walk"],
                 vals(["state", "record_residue", "record_count"]) | base,
                 {(P["state_equal_residue_agreements"],
                   P["state_equal_residue_pairs"]),
                  (P["state_distinct_residue_collisions"],
                   P["state_distinct_residue_pairs"]),
                  (P["state_single_cell_collisions"],
                   P["state_single_cell_pairs"])})
    # the counts the RECORD itself offers -- what it admits of the cast, and
    # what survives the quotient of its own histories -- are record facts as
    # well as invariance facts, and belong to both universes.
    ref.universe("THE-RECORD", ["record", "history", "histories", "corpus",
                                "block", "count field", "cast",
                                "cast solution", "cycle", "dependency"],
                 vals(["record", "corpus", "class_cast", "dep", "recon",
                       "quotient"]) | base
                 | {P["inv_link_graph_automorphisms"],
                    P["inv_arena_automorphisms"],
                    P["inv_direction_splittings"], P["inv_direction_index"]},
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
    "plants a comparator reaching a builder", "region_reach_offences",
    _plant("region_reach_offences", ["k_planted reaches b_planted"]))


def _unexercise_a_family(P):
    """the family (h) disease as a real instrument produces it: a template
    family that no live call in this mode exercises."""
    rows = [list(r) for r in P["template_family_counts"]]
    rows[0][1] = 0
    P["template_family_counts"] = rows
    return P


_mk("MUT-TEMPLATE", "G-TEMPLATE-EXERCISED",
    "zeroes one template family's live-call count", "template_family_counts",
    _unexercise_a_family)
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
    "plants an unlicensed policed sentence in the paper's own voice",
    "paper_digest",
    _corrupt_paper("## 1.", MUT_WALL_SENTENCE + "\n\n## 1."))
_mk("MUT-TYPED", "G-NO-TYPED-COUNTS", "plants a typed numeral offence",
    "typed_count_offences", _plant("typed_count_offences", ["line 1: '27'"]))
_mk("MUT-RECEIPT", "G-RECEIPT-TYPES", "plants an opaque receipt leaf",
    "receipt_type_offences", _plant("receipt_type_offences", ["$.planted"]))
_mk("MUT-HEAD", "G-HEAD-REBUILT",
    "moves one numeral of the head away from its receipt leaf", "head_segments",
    _corrupt_head)
_mk("MUT-TRANSCRIPT", "G-TRANSCRIPT-BOUND",
    "reports a transcript row the ledger does not carry", "transcript_stray",
    _bump("transcript_stray"))
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
                                  for (n, src, cons, needle, _b) in ANCHORS])
    fresh_anchors.locate(_BASE["sources_text"], _BASE["paper"] or None)
    for _n, _s, _c, _needle, _b in ANCHORS:
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
    # K3 MINOR-7: the honest denominator.  The nine template checks are
    # load-bearing kill paths outside this unit's ledger; they are falsified
    # by the era's own reference demos, and the split is stated rather than
    # folded into one number.
    cov["ledger_gates"] = len(GATE_ORDER)
    cov["template_checks_outside_the_ledger"] = len(ET.FAMILIES)
    cov["honest_denominator"] = (cov["gates"] + len(ET.FAMILIES))
    return rows, offenders, cov


# ===========================================================================
# SECTION K.  THE CLI (#82).
# ===========================================================================

USAGE = ("usage: contract_exact.py "
         "[--run|--no-write|--selftest|--list-gates|--list-mutants|"
         "--mutant NAME|--render]")

# #82, STRICT AT EVERY POSITION (K3 MAJOR-9): every flag's operand arity is
# declared, and an argv longer than its flag allows exits 2 -- so
# `--run --mutant NAME` can no longer write a clean delivery.
FLAG_ARITY = {"--run": 0, "--no-write": 0, "--selftest": 0, "--list-gates": 0,
              "--list-mutants": 0, "--render": 0, "--mutant": 1}

RENDER_EXIT = 4


def main(argv):
    if len(argv) == 1:
        argv = argv + ["--run"]
    flag = argv[1]
    if flag not in FLAG_ARITY or len(argv) != 2 + FLAG_ARITY[flag]:
        print(USAGE)
        return 2
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
        banner = ("DIAGNOSTIC-ONLY: the four paper gates are skipped, nothing "
                  "is written, and this mode exits non-zero by design")
        print(banner)
        sys.stderr.write(banner + "\n")
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
        for c in CTX["claim_texts"]:
            print("- " + c)
        return RENDER_EXIT
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
        if argv[2] not in MUTANTS:
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
