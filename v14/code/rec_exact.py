#!/usr/bin/env python3.13
# -*- coding: utf-8 -*-
"""REC (paper-41) -- THE RECONSTRUCTION UNIT: THE CAST DERIVED FROM THE RECORD.

Pin: v14/note-rec-pin.md (sha256-12 0b51e47b7b4b, v14 ledger #373).

THE QUESTION.  Can the theory be reconstructed from the record alone -- the
actors DERIVED rather than declared?  The parents supply the evidence that it
might be: FAC (paper-35) proved LEG-2 equivalent to refining the
participation-signature partition; AID (paper-33) proved the naming forced on
5,852 of 5,856 committed histories; EPR (paper-38) measured the link graph
complete multipartite.  This unit builds the reconstruction map itself.

WHAT IS READ.  The BARE RECORD: for every committed history, the sequence of
CELLS EACH DIVISION EVENT WROTE, with every actor label, every site label and
every direction label erased and the cell indices scrambled by a declared
arena-blind permutation.  Nothing else reaches the reconstructor.  The record
count field n_l(x) is measured too, as the level-0 arm, and is shown
insufficient rather than assumed so.

S-1 BY CONSTRUCTION (the registered-unimplemented family, TEMPLATE.md Sec.11).
Three code regions, disjoint by machine check at G-S1-DISJOINT-CODE:
  b_*   THE BUILDER      -- the declared arena and the committed corpus;
  r_*   THE RECONSTRUCTOR-- reads bare bytes and nothing else, ever;
  k_*   THE COMPARATOR   -- decides agreement, and calls neither of the others.
The comparator is shown to HAVE TEETH by refusing 5,856 per-history
reconstructions and every scrambled control.

TEMPLATE.  This is the first unit built on the E-25...E-33 engravings; the
nine families are imported from v14/code/era_template.py and used, not copied.

EXACTNESS.  Integers and fractions.Fraction only; no float appears anywhere,
and an AST scan plus a recursive receipt type scan are gates.

CLI (#82).  --run | --no-write | --selftest | --list-gates | --list-mutants
            | --mutant NAME | --render
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
from itertools import combinations, permutations, product

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
import era_template as ET                                          # noqa: E402

REPO = os.path.dirname(os.path.dirname(_HERE))     # .../isp

PAPER_REL = "v14/paper-41-rec.md"
RECEIPT_REL = "v14/code/rec_receipt.json"
OUTPUT_REL = "v14/code/rec_output.txt"
SELF_REL = "v14/code/rec_exact.py"
TEMPLATE_REL = "v14/code/era_template.py"
PIN_REL = "v14/note-rec-pin.md"

# The sha256-12 of every pinned source, verified before use (#91: repository
# reads at pinned digests only, and every product consumed by a gate).
SOURCES = {
    PIN_REL: "0b51e47b7b4b",
    "v14/paper-33-aid.md": "ecdd3fbf1d06",
    "v14/paper-35-fac.md": "281289a615ad",
    "v14/paper-38-epr.md": "22beb6696223",
    "v14/code/aid_receipt.json": "2dd2a9879984",
    "v14/code/fac_receipt.json": "c7135ba5884c",
    "v14/code/epr_receipt.json": "8813e0c2aad9",
    TEMPLATE_REL: "d04a3eb58fbc",
}

# A DECLARED COORDINATE, arena-blind: it is a function of the token index and
# of nothing else.  G-STRIPPING-EQUIVARIANT proves no measured quantity
# depends on it.
SCRAMBLE_MULT, SCRAMBLE_ADD = 5, 11

# ===========================================================================
# SECTION A.  b_*  --  THE BUILDER: the declared arena and the corpus.
#   AG(2,3); three declared link directions of the four parallel classes; the
#   27 cells; paper-21's I7-STRICT triples, G-FLAT quadruples and driven
#   window; the three corpora C1/C2/C3.  Re-implemented here, never imported.
# ===========================================================================

SITES = tuple((i, j) for i in range(3) for j in range(3))
SITE_INDEX = {s: k for k, s in enumerate(SITES)}
NACT = len(SITES)
I7_LINKS = ((1, 0), (0, 1), (1, 1))
CLASS_NAMES = ("ROW", "COL", "DIA", "ANT")
CLASS_DIR = {"ROW": (0, 1), "COL": (1, 0), "DIA": (1, 1), "ANT": (1, 2)}


def b_vadd(a, b):
    return ((a[0] + b[0]) % 3, (a[1] + b[1]) % 3)


def b_vmul(k, a):
    return ((k * a[0]) % 3, (k * a[1]) % 3)


def b_parallel_class(d):
    """the resolvable partition of AG(2,3) into the three lines of slope d."""
    H = frozenset({(0, 0), d, b_vmul(2, d)})
    seen, out = set(), []
    for x in SITES:
        L = tuple(sorted(b_vadd(x, h) for h in H))
        if L not in seen:
            seen.add(L)
            out.append(L)
    return tuple(sorted(out))


CLASSES = {k: b_parallel_class(CLASS_DIR[k]) for k in CLASS_NAMES}
CELLS = tuple((x, l) for x in SITES for l in I7_LINKS)
CELL_INDEX = {c: k for k, c in enumerate(CELLS)}
DIM = len(CELLS)


def b_codivision_pair(cell):
    """OCC's carrier typing: the cell IS the unordered co-division pair."""
    x, l = cell
    return frozenset((x, b_vadd(x, l)))


def b_all_groupings():
    """every partition of the nine sites into three triples."""
    out = []

    def rec(rem, acc):
        if not rem:
            out.append(tuple(sorted(acc)))
            return
        a, rest = rem[0], rem[1:]
        for pair in combinations(rest, 2):
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
    """paper-21's I7-STRICT class at R = 3."""
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
    """paper-21's 276: the summed link field is I7's G-FLAT row (1, 1, 2)."""
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
    return [tuple(sorted(g)[k] for g in P) for k in range(3)]


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
    """paper-21's DRIVEN WINDOW W4, by its own constructor."""
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
        for combo in product(*menus):
            sch = tuple(zip(T, combo))
            if sch in seen:
                continue
            seen.add(sch)
            out.append(sch)
            meta.append(tag)
    T = tuple(CLASSES[k] for k in B_COLLINEAR_FLAT)
    menus = [b_canon_transversals(P) for P in T]
    for combo in product(*menus):
        sch = tuple(zip(T, combo))
        if sch in seen:
            continue
        seen.add(sch)
        out.append(sch)
        meta.append("W4-SEEDFAN")
    return out, meta


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
    for sch, _tag in zip(scheds, smeta):
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


def b_declared_menu():
    """FAC's six admissible actor-grain partitions: the coset partitions of
    the translation subgroups -- trivial, the four parallel classes, discrete.
    Built here from the subgroups, never typed."""
    out = {"TRIVIAL": (tuple(sorted(SITE_INDEX[x] for x in SITES)),),
           "DISCRETE": tuple((SITE_INDEX[x],) for x in sorted(SITES))}
    for nm in CLASS_NAMES:
        out[nm] = tuple(sorted(tuple(sorted(SITE_INDEX[y] for y in L))
                               for L in CLASSES[nm]))
    return {k: tuple(sorted(v)) for k, v in out.items()}


def b_arena_automorphisms():
    """the affine maps of AG(2,3) permuting the three DECLARED directions."""
    out = []
    for a, b, c, d in product(range(3), repeat=4):
        if (a * d - b * c) % 3 == 0:
            continue
        M = ((a, b), (c, d))
        img = [((M[0][0] * v[0] + M[0][1] * v[1]) % 3,
                (M[1][0] * v[0] + M[1][1] * v[1]) % 3) for v in I7_LINKS]
        pool = set(I7_LINKS) | {b_vmul(2, l) for l in I7_LINKS}
        if not all(v in pool for v in img):
            continue
        for t in SITES:
            out.append(tuple(SITE_INDEX[b_vadd(
                ((M[0][0] * x[0] + M[0][1] * x[1]) % 3,
                 (M[1][0] * x[0] + M[1][1] * x[1]) % 3), t)] for x in SITES))
    return sorted(set(out))


def b_crystallization_time(H):
    """AID's object, re-derived: the least prefix at which every actor has its
    own participation signature (AID's theorem makes that the trivial
    stabilizer)."""
    for t in range(1, len(H) + 1):
        sig = {x: tuple(1 if x in F else 0 for F in H[:t]) for x in SITES}
        if len(set(sig.values())) == NACT:
            return t
    return None


_B_PERMS = list(permutations(range(3)))


def b_local_compat(fs, pos, ov, t, s, pt, ps):
    for x in ov[t][s]:
        if fs[t][_B_PERMS[pt][pos[t][x]]] != fs[s][_B_PERMS[ps][pos[s][x]]]:
            return False
    return True


def b_groupoid_prep(H):
    fs = [sorted(F) for F in H]
    T = len(H)
    pos = [{x: i for i, x in enumerate(f)} for f in fs]
    ov = [[sorted(set(fs[t]) & set(fs[s])) for s in range(T)] for t in range(T)]
    return fs, pos, ov


def b_window_count(H, w):
    """|Gamma_R| for R = {(t, s) : |t - s| <= w}, exact, by transfer."""
    fs, pos, ov = b_groupoid_prep(H)
    T = len(H)
    if w == 0:
        return len(_B_PERMS) ** T
    ok = [[[[b_local_compat(fs, pos, ov, t, s, pt, ps)
             for ps in range(len(_B_PERMS))] for pt in range(len(_B_PERMS))]
           if 0 < t - s <= w else None for s in range(T)] for t in range(T)]
    states = {(): 1}
    for t in range(T):
        nxt: dict = {}
        for st, cnt in states.items():
            base = t - len(st)
            for pt in range(len(_B_PERMS)):
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


def b_complete_count(H):
    """R-COMPLETE: the global groupoid count."""
    fs, pos, ov = b_groupoid_prep(H)
    T = len(H)
    total, cur = 0, [0] * T

    def bt(i):
        nonlocal total
        if i == T:
            total += 1
            return
        for pt in range(len(_B_PERMS)):
            if all(b_local_compat(fs, pos, ov, i, s, pt, cur[s])
                   for s in range(i)):
                cur[i] = pt
                bt(i + 1)
    bt(0)
    return total


def b_collapse_threshold(H):
    """FAC's w*: the least sliding-window width at which the groupoid count
    meets the global group's.  Uncapped."""
    tgt = b_complete_count(H)
    w = 0
    while w <= len(H):
        if b_window_count(H, w) == tgt:
            return w
        w += 1
    return None


# ===========================================================================
# SECTION B.  s_*  --  THE STRIPPING.
#   The eraser is allowed to see both sides; that is what an eraser is.  What
#   it emits carries no actor, no site and no direction, and G-STRIPPING-TOTAL
#   proves it by walking the emitted object's types.
# ===========================================================================

def s_scramble():
    """a declared arena-blind relabelling of the token indices."""
    return tuple((SCRAMBLE_MULT * k + SCRAMBLE_ADD) % DIM for k in range(DIM))


def s_bare_history(H, pi):
    """THE BARE RECORD of one history: for each division event in order, the
    cells it wrote, as scrambled token ids.  An event that wrote nothing
    contributes nothing -- the record is what was written."""
    out = []
    for F in H:
        f = b_cell_footprint(F)
        if f:
            out.append(tuple(sorted(pi[k] for k in f)))
    return tuple(out)


def s_bare_corpus(corp, pi):
    return [s_bare_history(H, pi) for (_t, H) in corp]


def s_type_walk(obj, bad, depth=0, floor=3):
    """The emitted record must be a nest of EXACTLY three levels -- histories,
    events, token ids -- whose leaves are integers.

    A leaf-type check alone is not enough and this instrument's own falsifier
    proved it: a site label is a PAIR OF INTEGERS, so a strip that emitted
    actor triples instead of the cells they wrote satisfied "integers and
    nothing else" and walked past the gate.  The depth is what forbids it.
    """
    if depth == floor:
        if isinstance(obj, bool) or not isinstance(obj, int):
            bad.append("depth-%d leaf is %s" % (floor, type(obj).__name__))
        return bad
    if not isinstance(obj, (list, tuple)):
        bad.append("depth-%d level is %s" % (depth, type(obj).__name__))
        return bad
    for o in obj:
        s_type_walk(o, bad, depth + 1, floor)
    return bad


# ===========================================================================
# SECTION C.  r_*  --  THE RECONSTRUCTOR.
#   Reads bare bytes and nothing else.  Calls no b_* and no k_*; names no
#   arena constant.  Machine-checked at G-S1-DISJOINT-CODE.
# ===========================================================================

def r_cooccurrence(blocks):
    co = collections.defaultdict(set)
    for b in blocks:
        for u, v in combinations(b, 2):
            co[u].add(v)
            co[v].add(u)
    return co


def r_sharing(blocks):
    """THE RULE.  Two record cells belong to a common actor exactly when one
    event wrote them together, or when the cells written with each of them
    meet in the largest number any never-co-written pair attains.  The
    threshold is DERIVED from the record, never typed."""
    toks = sorted({t for b in blocks for t in b})
    co = r_cooccurrence(blocks)
    far = [(u, v) for u, v in combinations(toks, 2) if v not in co[u]]
    meets = sorted({len(co[u] & co[v]) for u, v in far})
    if len(meets) < 2:
        return None, meets, co, toks
    tau = meets[-1]
    share = collections.defaultdict(set)
    for u, v in combinations(toks, 2):
        if v in co[u] or len(co[u] & co[v]) == tau:
            share[u].add(v)
            share[v].add(u)
    return (tau, share), meets, co, toks


def r_maximal_cliques(verts, g):
    out = []

    def bt(R, P, X):
        if not P and not X:
            out.append(frozenset(R))
            return
        piv = max(P | X, key=lambda v: len(g[v]))
        for v in sorted(P - g[piv]):
            bt(R | {v}, P & g[v], X & g[v])
            P = P - {v}
            X = X | {v}
    bt(set(), set(verts), set())
    return out


def r_reconstruct(record_blocks):
    """THE RECONSTRUCTION MAP.  Input: the cells the events wrote.  Output:
    the derived cast, the derived link structure, and the reconstructor's own
    certificate."""
    blk = sorted({tuple(sorted(b)) for b in record_blocks if len(b) > 1})
    toks = sorted({t for b in blk for t in b})
    if not blk:
        return {"ok": False, "why": "NO-RECORD-BLOCKS", "cast": [],
                "tokens": toks, "blocks": blk}
    got, meets, _co, toks = r_sharing(blk)
    if got is None:
        return {"ok": False, "why": "NO-MEET-GAP", "cast": [], "tokens": toks,
                "blocks": blk, "meets": meets}
    tau, share = got
    cliques = r_maximal_cliques(toks, share)
    if not cliques:
        return {"ok": False, "why": "NO-CLIQUES", "cast": [], "tokens": toks,
                "blocks": blk, "meets": meets}
    top = max(len(c) for c in cliques)
    cast = sorted((tuple(sorted(c)) for c in cliques if len(c) == top))
    links = {}
    for t in toks:
        links[t] = tuple(i for i, c in enumerate(cast) if t in c)
    return {"ok": True, "cast": cast, "tokens": toks, "blocks": blk,
            "tau": tau, "meets": meets, "links": links,
            "clique_sizes": sorted(collections.Counter(
                len(c) for c in cliques).items())}


def r_certify(rec):
    """The legs the RECONSTRUCTOR can check on bare bytes alone.  A refusal
    here is the reconstructor declining to answer, never a wrong answer."""
    if not rec["ok"]:
        return False, rec["why"]
    cast, toks = rec["cast"], rec["tokens"]
    if len({len(c) for c in cast}) != 1:
        return False, "RAGGED-CAST"
    inc = collections.Counter(t for c in cast for t in c)
    if set(inc) != set(toks):
        return False, "TOKEN-IN-NO-ACTOR"
    if set(inc.values()) != {2}:
        return False, "TOKEN-NOT-IN-EXACTLY-TWO"
    if any(len(set(a) & set(b)) > 1 for a, b in combinations(cast, 2)):
        return False, "TWO-ACTORS-SHARE-TWO-CELLS"
    if len(toks) * 2 != len(cast) * len(cast[0]):
        return False, "TOKENS-NOT-THE-PAIR-COUNT"
    return True, "CERTIFIED"


def r_derived_parts(rec):
    """THE UNDECLARED CLASS, derived: the actors are partitioned by 'shares no
    token', and the derived link structure is complete multipartite over that
    partition exactly when the parts are its co-classes."""
    cast = rec["cast"]
    n = len(cast)
    unl = collections.defaultdict(set)
    for i, j in combinations(range(n), 2):
        if not (set(cast[i]) & set(cast[j])):
            unl[i].add(j)
            unl[j].add(i)
    seen, parts = set(), []
    for i in range(n):
        if i in seen:
            continue
        blk = {i} | unl[i]
        if any(unl[a] | {a} != blk for a in blk):
            return None
        seen |= blk
        parts.append(tuple(sorted(blk)))
    return tuple(sorted(parts))


def r_derived_menu(rec):
    """The partition menu the record itself delivers: the one-block partition,
    the discrete partition, and the co-class partition of the link structure."""
    n = len(rec["cast"])
    out = {"TRIVIAL": (tuple(range(n)),),
           "DISCRETE": tuple((i,) for i in range(n))}
    p = r_derived_parts(rec)
    if p is not None:
        out["UNDECLARED-CLASS"] = p
    return {k: tuple(sorted(v)) for k, v in out.items()}


def r_triangle_factors(rec):
    """the partitions of the derived cast into blocks of mutually linked
    actors covering every actor -- the candidates for a declared direction."""
    cast = rec["cast"]
    n = len(cast)
    linked = {(i, j) for i, j in combinations(range(n), 2)
              if set(cast[i]) & set(cast[j])}
    parts = r_derived_parts(rec)
    if parts is None:
        return []
    size = len(parts)
    tri = [t for t in combinations(range(n), size)
           if all((a, b) in linked for a, b in combinations(t, 2))]
    out = []

    def bt(used, acc):
        if len(used) == n:
            out.append(tuple(sorted(acc)))
            return
        low = min(set(range(n)) - used)
        for t in tri:
            if t[0] == low and not (set(t) & used):
                bt(used | set(t), acc + [t])
    bt(set(), [])
    return sorted(out)


def r_resolutions(rec):
    """the ways the derived link structure splits into disjoint direction
    classes -- the record's residual freedom about the declaration."""
    facs = r_triangle_factors(rec)
    toks = rec["tokens"]
    cast = rec["cast"]

    def tokens_of(fac):
        out = set()
        for blk in fac:
            for a, b in combinations(blk, 2):
                out |= set(cast[a]) & set(cast[b])
        return frozenset(out)
    tf = [(f, tokens_of(f)) for f in facs]
    want = len(toks)
    out = []
    for combo in combinations(range(len(tf)), 3):
        cov = [tf[i][1] for i in combo]
        if sum(len(c) for c in cov) == want and len(set().union(*cov)) == want:
            out.append(tuple(sorted(tf[i][0] for i in combo)))
    return sorted(set(out))


# ===========================================================================
# SECTION D.  k_*  --  THE COMPARATOR.
#   Decides agreement between a reconstruction and the declared arena.  Calls
#   no r_* and no b_*: it is handed DATA by the caller and derives its own
#   verdict by an isomorphism search rather than by re-running either side.
# ===========================================================================

def k_agree_sets(derived, declared):
    """set equality of two families of token sets, order-blind."""
    return {frozenset(x) for x in derived} == {frozenset(x) for x in declared}


def k_index_map(derived, declared):
    """the identification of derived actors with declared ones BY SET
    EQUALITY of their cell sets -- available only because the cast gate
    already found the two families equal, and used for nothing else."""
    dd = {frozenset(c): i for i, c in enumerate(declared)}
    out = {}
    for i, c in enumerate(derived):
        j = dd.get(frozenset(c))
        if j is None:
            return None
        out[i] = j
    return out


def k_isomorphisms(derived_cast, declared_cast, tokens):
    """every bijection of derived actors onto declared actors that carries the
    derived link structure onto the declared one.  Built by search over the
    incidence, never by inverting a construction."""
    n = len(derived_cast)
    if n != len(declared_cast):
        return []
    dinc = {t: frozenset(i for i in range(n) if t in derived_cast[i])
            for t in tokens}
    cinc = {t: frozenset(i for i in range(n) if t in declared_cast[i])
            for t in tokens}
    dpair = collections.Counter(frozenset(v) for v in dinc.values())
    cpair = collections.Counter(frozenset(v) for v in cinc.values())
    out, sigma = [], {}

    def bt(i):
        if i == n:
            got = collections.Counter(
                frozenset(sigma[a] for a in p) for p in dpair.elements())
            if got == cpair:
                out.append(tuple(sigma[a] for a in range(n)))
            return
        used = set(sigma.values())
        for j in range(n):
            if j in used:
                continue
            sigma[i] = j
            ok = True
            for a in range(i):
                da = frozenset((i, a)) in dpair
                ca = frozenset((sigma[i], sigma[a])) in cpair
                if da != ca:
                    ok = False
                    break
            if ok:
                bt(i + 1)
            del sigma[i]
    bt(0)
    return out


def k_coherent(isos, declared_cast, tokens, direction_classes):
    """which admissible namings also carry the declared direction classes onto
    themselves -- the arena-coherent ones."""
    n = len(declared_cast)
    pair_of = {}
    for t in tokens:
        pr = tuple(sorted(i for i in range(n) if t in declared_cast[i]))
        pair_of[pr] = t
    dc = {frozenset(c) for c in direction_classes}
    good = []
    for s in isos:
        img = set()
        for c in direction_classes:
            got = set()
            for t in c:
                pr = tuple(sorted(i for i in range(n) if t in declared_cast[i]))
                got.add(pair_of[tuple(sorted((s[pr[0]], s[pr[1]])))])
            img.add(frozenset(got))
        if img == dc:
            good.append(s)
    return good


def k_menu_agreement(derived_menu, declared_menu, naming):
    """each derived menu member is carried through a naming and looked for in
    the declared menu; each declared member is looked for in the image."""
    def carry(p):
        return tuple(sorted(tuple(sorted(naming[a] for a in blk)) for blk in p))
    got = {carry(v) for v in derived_menu.values()}
    want = {tuple(sorted(v)): k for k, v in declared_menu.items()}
    matched = sorted({want[g] for g in got if g in want})
    stray = sorted(len(g) for g in got if g not in want)
    return matched, stray, sorted(set(want.values()) - set(matched))


# ===========================================================================
# SECTION E.  THE UNIT'S OWN PLUMBING (neither builder, reconstructor nor
# comparator): digests, sources, the paper instrument, the mutant hook.
# ===========================================================================

MUTANT = {"name": None, "used": set()}


def mut(tag):
    if MUTANT["name"] == tag:
        MUTANT["used"].add(tag)
        return True
    return False


def sha12(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()[:12]


def read_text(rel):
    with open(os.path.join(REPO, rel), "r", encoding="utf-8") as fh:
        return fh.read()


def com(n):
    return "{:,}".format(n)


ANCHORS = [
    ET.Anchor("A-PIN", "the site set, the link structure, the cast size, "
              "the partition menu, the naming", PIN_REL,
              "G-RECONSTRUCTION-TARGETS-TOTAL"),
    ET.Anchor("A-FAC-CARRIER",
              "27 cells against 27 pairs, two actors in each cell at all of "
              "them, six cells per actor at all nine", "v14/paper-35-fac.md",
              "G-CAST-DERIVED"),
    ET.Anchor("A-FAC-WSTAR",
              "the collapse thresholds this corpus carries are 3, 4, 5, and "
              "they are WIDTHS in event index, not event counts",
              "v14/paper-35-fac.md", "G-WSTAR-REDERIVED"),
    ET.Anchor("A-AID-CRYSTALLIZATION",
              "the crystallization time is exactly 5 on C1, C2 and the seed "
              "fan", "v14/paper-33-aid.md", "G-CRYSTALLIZATION-REDERIVED"),
    ET.Anchor("A-AID-SIGNATURE",
              "identity crystallizes exactly when every actor has its own "
              "signature", "v14/paper-33-aid.md",
              "G-CRYSTALLIZATION-REDERIVED"),
    ET.Anchor("A-EPR-LINKGRAPH",
              "The graph is therefore complete multipartite with those three "
              "lines as its parts, and every site has degree six",
              "v14/paper-38-epr.md", "G-LINK-STRUCTURE-DERIVED"),
    ET.Anchor("A-EPR-UNLINKED",
              "two sites are unlinked exactly when they lie on a common line "
              "of the one parallel class the arena does not declare, at 72 of "
              "72 ordered site pairs", "v14/paper-38-epr.md",
              "G-OBSTRUCTION-NAMED"),
]

WALL_DERIVED = ET.SemanticWall(
    "W-NO-UNQUALIFIED-DERIVATION",
    negative=[
        r"the (?:whole |entire )?(?:cast|arena|theory) is (?:fully |wholly )?"
        r"(?:derived|reconstructed|recovered)(?![\w\s]{0,24}up to)"
        r"(?![\w\s]{0,40}at the corpus)",
        r"nothing (?:at all |whatever )?(?:is |remains |stays )?declared",
        r"no (?:declaration|residue|freedom|choice) (?:remains|is left|survives)",
        r"(?:the )?record (?:alone |by itself )?(?:fixes|determines|forces) "
        r"the (?:coordinates|directions|direction classes)",
        r"reconstruct\w*\s+(?:\w+\s+){0,3}from a single history",
        r"(?:the )?count field\s+(?:\w+\s+){0,4}(?:suffices|is enough|"
        r"recovers the cast|determines the cast)",
    ],
    positive=[
        r"the cast is derived at the corpus and at no single history",
        r"the direction declaration is the datum that resists",
    ],
)

WALL_PARENTS = ET.SemanticWall(
    "W-PARENT-SCOPE",
    negative=[
        r"the record is (?:a |the )?complete description(?![\w\s]{0,30}"
        r"(?:for the censused|at this arena))",
        r"epr\w*\s+(?:\w+\s+){0,4}(?:proved|showed|established)\s+"
        r"(?:\w+\s+){0,3}completeness",
        r"local realism\s+(?:\w+\s+){0,3}(?:is\s+)?restor\w*",
        r"restor\w*\s+(?:\w+\s+){0,3}local realism",
    ],
    positive=[
        r"record-completeness is analytic at epr's own catalogue",
    ],
)

WALLS = (WALL_DERIVED, WALL_PARENTS)


# ---------------------------------------------------------------------------
# THE PAPER INSTRUMENT
# ---------------------------------------------------------------------------

NUM = re.compile(r"(?<![\w.,/-])(\d[\d,]*)(?![\w/])")
FENCE_RE = re.compile(r"```[^\n]*\n(.*?)```", re.S)


def paper_numerals(text):
    return [m.group(1).replace(",", "") for m in NUM.finditer(text)]


def audit_no_floats(src):
    """AST leg: no float literal, no float(), no division that leaves Z."""
    bad = []
    for node in ast.walk(ast.parse(src)):
        if isinstance(node, ast.Constant) and isinstance(node.value, float):
            bad.append("line %d: float literal" % node.lineno)
        if isinstance(node, ast.Call) and getattr(node.func, "id", "") == "float":
            bad.append("line %d: float() call" % node.lineno)
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div):
            bad.append("line %d: true division" % node.lineno)
    return bad


def audit_regions(src):
    """S-1: the three regions are disjoint.  A reconstructor function may not
    call a builder or comparator function, nor name an arena constant; a
    comparator function may not call a reconstructor or builder function."""
    tree = ast.parse(src)
    fns = {n.name: n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)}
    arena = {"SITES", "SITE_INDEX", "NACT", "I7_LINKS", "CLASS_NAMES",
             "CLASS_DIR", "CLASSES", "CELLS", "CELL_INDEX", "DIM", "ACTORS",
             "SCRAMBLE_MULT", "SCRAMBLE_ADD", "_RAW", "_B_PERMS"}
    bad = []
    for name, node in sorted(fns.items()):
        if name.startswith("r_"):
            forbidden, tagged = ("b_", "k_", "s_"), "reconstructor"
        elif name.startswith("k_"):
            forbidden, tagged = ("b_", "r_", "s_"), "comparator"
        else:
            continue
        for sub in ast.walk(node):
            if isinstance(sub, ast.Name):
                if sub.id in arena:
                    bad.append("%s %s names the arena constant %s"
                               % (tagged, name, sub.id))
                if any(sub.id.startswith(p) for p in forbidden):
                    bad.append("%s %s calls %s" % (tagged, name, sub.id))
            if isinstance(sub, ast.Attribute) and sub.attr in arena:
                bad.append("%s %s names %s" % (tagged, name, sub.attr))
    return sorted(set(bad))


def region_census(src):
    tree = ast.parse(src)
    out = collections.Counter()
    for n in ast.walk(tree):
        if isinstance(n, ast.FunctionDef):
            for pre, tag in (("b_", "builder"), ("r_", "reconstructor"),
                             ("k_", "comparator"), ("s_", "stripper")):
                if n.name.startswith(pre):
                    out[tag] += 1
    return dict(sorted(out.items()))


# ===========================================================================
# SECTION F.  THE RUN.
# ===========================================================================

QUALIFIER = "-UP-TO-THE-DIRECTION-DECLARATION"


def head_word_of(cast_exact, pairs_ok, size_ok, menu_missing, residue):
    """THE VERDICT WORD, DERIVED (#234).  Each of the pin's pre-registered
    outcomes is the value of this function on some input, and
    G-VERDICT-EQUALITY exercises three of them on declared probes so that the
    word this run prints is shown to be a choice the run could have made
    differently."""
    if not (cast_exact and size_ok):
        return "REC-BLOCKED-AT-THE-CAST"
    if not pairs_ok:
        return "REC-OBSTRUCTED-AT-THE-LINK-STRUCTURE"
    if menu_missing == 0 and residue == 1:
        return "REC-CAST-DERIVED"
    return "REC-CAST-DERIVED" + QUALIFIER


SYNTHETIC_PARTS = ((2, 2, 2), (3, 3, 3), (4, 4, 4), (5, 5, 5),
                   (2, 2, 2, 2), (3, 3), (2, 3, 4))


def synthetic_record(parts):
    """A SYNTHETIC MINIMAL RECORD, built from a cast that is not this arena's:
    tokens are the linked pairs of a complete multipartite cast, blocks are
    the events that write three of them.  The control the pin asks for."""
    P = [list(range(sum(parts[:i]), sum(parts[:i + 1])))
         for i in range(len(parts))]
    tok, blocks = {}, []
    for i, j in combinations(range(len(P)), 2):
        for a in P[i]:
            for b in P[j]:
                tok[frozenset((a, b))] = len(tok)
    for combo in combinations(range(len(P)), 3):
        for t in product(*[P[c] for c in combo]):
            blocks.append(frozenset(tok[frozenset(p)]
                                    for p in combinations(t, 2)))
    stars = sorted(tuple(sorted(v for k, v in tok.items() if a in k))
                   for Pi in P for a in Pi)
    return blocks, stars, len(tok)


def full_run(write=False, mutant=None, render=False):
    MUTANT["name"], MUTANT["used"] = mutant, set()
    reads: list[str] = []
    RS = ET.ReadSet(REPO)
    RS.install()
    RS.active = True

    LD, TR, SEAL = ET.Ledger(), ET.Transcript(), ET.Seal()
    REG, CL, RR = ET.CountRegistry(), ET.Claims(), ET.ReferentRegistry()
    R: dict = {}

    def gate(gid, statement, ok, evidence):
        LD.gate(gid, statement, ok, evidence)
        TR.row(gid, ok, evidence)

    TR.say("REC (paper-41) -- THE RECONSTRUCTION UNIT: THE CAST DERIVED FROM "
           "THE RECORD")
    TR.say("=" * 74)

    # -- sources, pinned ----------------------------------------------------
    texts, shas, drifted = {}, {}, []
    for rel, want in sorted(SOURCES.items()):
        p = os.path.join(REPO, rel)
        got = sha12(p)
        shas[rel] = got
        reads.append(rel)
        if got != want:
            drifted.append("%s %s != %s" % (rel, got, want))
        if rel.endswith(".md"):
            texts[rel] = read_text(rel)
            reads.append(rel)
    if mut("MUT-SOURCE-DRIFT"):
        shas[PIN_REL] = shas[PIN_REL][::-1]
        drifted.append("injected")
    R["sources"] = {k: shas[k] for k in sorted(shas)}
    SEAL.seal("sources", R["sources"], "G-SOURCES-PINNED")
    REG.measured("sources", len(SOURCES), "len(SOURCES)")
    gate("G-SOURCES-PINNED",
         REG.stmt("every one of the {sources} pinned sources digests to the "
                  "value the pin froze, and no repository object is read at "
                  "any other digest", sources=1),
         not drifted, "sources %d drifted %s" % (len(SOURCES),
                                                 drifted or "none"))

    # -- the paper under test, and the anchors located in both sides --------
    paper = read_text(PAPER_REL)
    reads.append(PAPER_REL)
    ET.require_object("--run", os.path.join(REPO, PAPER_REL), paper)
    ASET = ET.AnchorSet(list(ANCHORS))
    src_for_anchor = dict(texts)
    if mut("MUT-ANCHOR"):
        src_for_anchor["v14/paper-35-fac.md"] = texts[
            "v14/paper-35-fac.md"].replace("cells against 27 pairs",
                                           "cells against 26 pairs", 1)
    try:
        ASET.locate(src_for_anchor, paper)
        lprob = None
    except ET.CheckFail as exc:
        lprob = exc.detail
    REG.measured("anchor_rows", len(ANCHORS), "len(ANCHORS)")
    gate("G-ANCHORS-LOCATED",
         REG.stmt("each of the {anchor_rows} verbatim anchors occurs exactly "
                  "once in the pinned parent's own bytes AND once in this "
                  "paper's rendering, under the same canonicalisation, before "
                  "any of them is read", anchor_rows=1),
         lprob is None, "anchors %d located %s"
         % (len(ANCHORS), lprob or "all"))

    # -- the declared arena -------------------------------------------------
    corp, parts, strict, flatq, scheds, smeta = b_build_corpus()
    sat = b_raw_census()["sat"]
    pairs = {b_codivision_pair(c) for c in CELLS}
    per_actor = collections.Counter()
    for c in CELLS:
        for a in b_codivision_pair(c):
            per_actor[a] += 1
    dec_actors = b_declared_actors()
    if mut("MUT-ARENA"):
        per_actor[SITES[0]] = per_actor[SITES[0]] + 1
    R["arena"] = {
        "sites": NACT, "declared_link_directions": len(I7_LINKS),
        "parallel_classes": len(CLASS_NAMES), "cells": DIM,
        "co_division_pairs": len(pairs),
        "cells_per_actor": sorted(set(per_actor.values())),
        "groupings": len(parts), "saturating_groupings": len(sat),
        "strict_triples": len(strict), "flat_quadruples": len(flatq),
        "window_schedules": len(scheds),
    }
    for nm, val in (("sites", NACT), ("cells", DIM),
                    ("declared_links", len(I7_LINKS)),
                    ("classes", len(CLASS_NAMES)), ("groupings", len(parts)),
                    ("saturating", len(sat)), ("strict", len(strict)),
                    ("flatq", len(flatq)), ("scheds", len(scheds))):
        REG.measured(nm, val, "the arena constructor")
    SEAL.seal("arena", R["arena"], "G-ARENA-CONSTRUCTED")
    gate("G-ARENA-CONSTRUCTED",
         REG.stmt("the arena is built here and not inherited: {sites} sites, "
                  "{declared_links} declared link directions of {classes} "
                  "parallel classes, {cells} cells against as many "
                  "co-division pairs, {groupings} groupings of which "
                  "{saturating} saturate, {strict} I7-STRICT triples, "
                  "{flatq} G-FLAT quadruples, {scheds} window schedules",
                  sites=1, declared_links=1, classes=1, cells=1, groupings=1,
                  saturating=1, strict=1, flatq=1, scheds=1),
         len(pairs) == DIM and set(per_actor.values()) == {2 * DIM // NACT},
         "cells %d pairs %d cells-per-actor %s"
         % (DIM, len(pairs), sorted(set(per_actor.values()))))

    lens = collections.Counter(len(h) for (_t, h) in corp)
    bytag = collections.Counter(t for (t, _h) in corp)
    if mut("MUT-CORPUS"):
        bytag["C2"] = bytag["C2"] - 1
    R["corpus"] = {
        "slots": len(corp), "distinct_histories": len({h for (_t, h) in corp}),
        "by_corpus": dict(sorted(bytag.items())),
        "event_lengths": {str(k): v for k, v in sorted(lens.items())},
        "events": sum(len(h) for (_t, h) in corp),
    }
    REG.measured("slots", len(corp), "len(corp)")
    REG.measured("distinct_histories", R["corpus"]["distinct_histories"],
                 "len(set of histories)")
    REG.measured("events", R["corpus"]["events"], "sum of history lengths")
    SEAL.seal("corpus", R["corpus"], "G-CORPUS-SHAPE")
    gate("G-CORPUS-SHAPE",
         REG.stmt("the committed corpus is a MULTISET of {slots} slots "
                  "carrying {distinct_histories} distinct histories and "
                  "{events} division events in all", slots=1,
                  distinct_histories=1, events=1),
         bytag["C2"] == bytag["C1"] ** 2 and all(n % 3 == 0 for n in lens),
         "slots %d distinct %d lengths %s"
         % (len(corp), R["corpus"]["distinct_histories"], sorted(lens)))

    # -- level zero: the count field alone ----------------------------------
    fields = [b_record_field(H) for (_t, H) in corp]
    site_const = sum(1 for f in fields
                     if len({tuple(f[3 * i:3 * i + 3]) for i in range(NACT)}) == 1)
    if mut("MUT-LEVEL0"):
        site_const = site_const - 1
    R["level_zero"] = {
        "distinct_record_fields": len(set(fields)),
        "site_constant_at": site_const, "of_slots": len(corp),
        "distinct_site_rows": len({tuple(f[:3]) for f in fields}),
        "largest_count": max(max(f) for f in fields),
    }
    REG.measured("fields", len(set(fields)), "len(set of record fields)")
    REG.measured("site_constant", site_const, "site-constant histories")
    SEAL.seal("level_zero", R["level_zero"], "G-LEVEL-ZERO-INSUFFICIENT")
    gate("G-LEVEL-ZERO-INSUFFICIENT",
         REG.stmt("the record COUNT FIELD alone carries {fields} distinct "
                  "values over {slots} slots and is site-constant at "
                  "{site_constant} of them, so it names no cast: the "
                  "reconstruction runs on the cells the events wrote, not on "
                  "the counts they left", fields=1, slots=1, site_constant=1),
         len(set(fields)) < NACT ** 2 and site_const == len(corp),
         "distinct fields %d site-constant %d of %d"
         % (len(set(fields)), site_const, len(corp)))

    # -- the stripping ------------------------------------------------------
    pi = s_scramble()
    # THE DECLARED CAST IN THE ERASURE'S OWN COORDINATES.  The comparator is
    # handed both sides as data; the eraser is the only party that knows which
    # token was which cell, and this is where that bookkeeping is spent.
    dec_cast = [tuple(sorted(pi[k] for k in dec_actors[i])) for i in range(NACT)]
    bare = s_bare_corpus(corp, pi)
    if mut("MUT-STRIP-LEAK"):
        bare = [tuple(tuple(sorted(F)) for F in H) for (_t, H) in corp]
    typebad = []
    s_type_walk(bare, typebad)
    blocks = sorted({b for h in bare for b in h})
    written = sum(len(h) for h in bare)
    R["stripping"] = {
        "scramble_is_a_permutation": sorted(pi) == list(range(DIM)),
        "record_blocks": len(blocks),
        "block_sizes": sorted(collections.Counter(len(b) for b in blocks).items()),
        "written_events": written,
        "unwritten_events": R["corpus"]["events"] - written,
        "non_integer_leaves": sorted(set(typebad)),
    }
    REG.measured("blocks", len(blocks), "distinct record blocks")
    REG.measured("written", written, "events that wrote at least one cell")
    REG.measured("unwritten", R["corpus"]["events"] - written,
                 "events that wrote nothing")
    SEAL.seal("stripping", R["stripping"], "G-STRIPPING-TOTAL")
    gate("G-STRIPPING-TOTAL",
         REG.stmt("the bare record is three levels deep and integers at the "
                  "bottom -- histories, events, token ids -- so no actor, no "
                  "site (a PAIR of integers) and no direction survives the "
                  "strip; the "
                  "corpus writes {written} events into {blocks} distinct "
                  "record blocks and writes nothing at {unwritten}",
                  written=1, blocks=1, unwritten=1),
         not typebad and sorted(pi) == list(range(DIM)),
         "non-integer leaves %s blocks %d written %d unwritten %d"
         % (sorted(set(typebad)) or "none", len(blocks), written,
            R["corpus"]["events"] - written))

    # -- equivariance: the scramble is immaterial ---------------------------
    trials, eqbad = [], []
    for step in range(1, 13):
        rho = tuple((step * 2 + 1) * k % DIM for k in range(DIM))
        if sorted(rho) != list(range(DIM)):
            rho = tuple((k + step) % DIM for k in range(DIM))
        if mut("MUT-EQUIVARIANCE") and step == 1:
            rho = tuple(0 for _ in range(DIM))
        moved = [frozenset(rho[t] for t in b) for b in blocks]
        rec_m = r_reconstruct(moved)
        inv = [0] * DIM
        for i, p in enumerate(rho):
            inv[p] = i
        back = sorted(tuple(sorted(inv[t] for t in c)) for c in rec_m["cast"]) \
            if rec_m["ok"] else []
        trials.append({"step": step, "ok": rec_m["ok"]})
        if not rec_m["ok"] or back != sorted(
                tuple(sorted(c)) for c in r_reconstruct(blocks)["cast"]):
            eqbad.append(step)
    R["equivariance"] = {"trials": len(trials), "failures": len(eqbad),
                         "failing_steps": eqbad}
    REG.measured("eq_trials", len(trials), "relabelling trials")
    REG.measured("eq_failures", len(eqbad), "trials whose cast moved")
    SEAL.seal("equivariance", R["equivariance"], "G-STRIPPING-EQUIVARIANT")
    gate("G-STRIPPING-EQUIVARIANT",
         REG.stmt("relabelling the tokens relabels the derived cast and does "
                  "nothing else, at {eq_trials} declared relabellings with "
                  "{eq_failures} failures, so no measured quantity depends on "
                  "the coordinate the strip chose", eq_trials=1,
                  eq_failures=1),
         not eqbad, "trials %d failures %d" % (len(trials), len(eqbad)))

    # -- THE RECONSTRUCTION, at the corpus ----------------------------------
    rec = r_reconstruct(blocks)
    if mut("MUT-TAU"):
        rec["cast"] = rec["cast"][:-1]
    cert, why = r_certify(rec)
    R["reconstruction"] = {
        "certified": bool(cert), "certificate": why,
        "meet_values": rec.get("meets", []), "threshold": rec.get("tau"),
        "clique_sizes": rec.get("clique_sizes", []),
        "cast_size": len(rec["cast"]),
        "cells_per_actor": sorted({len(c) for c in rec["cast"]}),
        "tokens": len(rec["tokens"]),
    }
    REG.measured("derived_cast", len(rec["cast"]), "len(reconstruction cast)")
    REG.measured("tau", rec.get("tau", 0), "the derived meet threshold")
    SEAL.seal("reconstruction", R["reconstruction"], "G-CAST-DERIVED")

    # THE COMPARATOR.  Handed data, never the builders.
    a_carrier = ASET.read("A-FAC-CARRIER", "G-CAST-DERIVED")
    carrier_nums = [int(x) for x in re.findall(r"\d+", a_carrier)]
    cast_exact = k_agree_sets(rec["cast"], dec_cast)
    if mut("MUT-CAST"):
        cast_exact = k_agree_sets(rec["cast"][:-1], dec_cast)
    REG.measured("declared_cast", len(dec_cast), "len(declared actor stars)")
    gate("G-CAST-DERIVED",
         REG.stmt("the cast is DERIVED: the {derived_cast} maximal sets of "
                  "cells that pairwise belong to one actor, computed from the "
                  "record blocks alone, are set-equal to the "
                  "{declared_cast} declared actor stars; the parent's carrier "
                  "row is read back and its numbers are the ones measured "
                  "here", derived_cast=1, declared_cast=1),
         cast_exact and cert and len(rec["cast"]) == NACT
         and carrier_nums[0] == DIM and carrier_nums[1] == len(pairs),
         "certified %s cast %d set-equal %s anchor %s"
         % (why, len(rec["cast"]), cast_exact, carrier_nums[:2]))

    # -- the link structure -------------------------------------------------
    a_link = ASET.read("A-EPR-LINKGRAPH", "G-LINK-STRUCTURE-DERIVED")
    link_parts = r_derived_parts(rec)
    incid = collections.Counter(len(rec["links"][t]) for t in rec["tokens"])
    dec_pairs = {tuple(sorted(i for i in range(NACT) if t in dec_cast[i]))
                 for t in rec["tokens"]}
    imap = k_index_map(rec["cast"], dec_cast)
    der_pairs = {tuple(sorted(imap[i] for i in rec["links"][t]))
                 for t in rec["tokens"]} if imap else set()
    if mut("MUT-LINK"):
        der_pairs = set(list(der_pairs)[:-1])
    degrees = sorted({sum(1 for p in der_pairs if i in p) for i in range(NACT)})
    R["link_structure"] = {
        "tokens_in_exactly_two_actors": incid.get(2, 0),
        "derived_pairs": len(der_pairs), "declared_pairs": len(dec_pairs),
        "pairs_agree": der_pairs == dec_pairs,
        "derived_parts": [list(p) for p in (link_parts or ())],
        "degrees": degrees,
    }
    REG.measured("tokens_two", incid.get(2, 0), "tokens lying in two actors")
    REG.measured("derived_pairs", len(der_pairs), "derived actor pairs")
    REG.measured("degree", degrees[0] if len(degrees) == 1 else -1,
                 "the common actor degree")
    REG.measured("parts", len(link_parts or ()), "derived multipartite parts")
    SEAL.seal("link_structure", R["link_structure"], "G-LINK-STRUCTURE-DERIVED")
    gate("G-LINK-STRUCTURE-DERIVED",
         REG.stmt("the link structure is DERIVED: each of the {blocks} tokens "
                  "lies in exactly two derived actors at {tokens_two} of them, "
                  "so a token IS an unordered pair of actors, and the "
                  "{derived_pairs} derived pairs are the declared ones; the "
                  "derived structure is complete multipartite over {parts} "
                  "parts with every actor at degree {degree}, which is the "
                  "shape the parent measured", blocks=1, tokens_two=1,
                  derived_pairs=1, parts=1, degree=1),
         der_pairs == dec_pairs and incid.get(2, 0) == DIM
         and link_parts is not None and len(link_parts) == 3
         and len(degrees) == 1 and ("three" in a_link.casefold())
         and ("six" in a_link.casefold()),
         "two-actor tokens %d pairs %d agree %s parts %s degrees %s"
         % (incid.get(2, 0), len(der_pairs), der_pairs == dec_pairs,
            len(link_parts or ()), degrees))

    a_pin = ASET.read("A-PIN", "G-RECONSTRUCTION-TARGETS-TOTAL")
    if mut("MUT-TARGETS"):
        a_pin = a_pin.replace("the partition menu, ", "")

    # -- the partition menu -------------------------------------------------
    dec_menu = b_declared_menu()
    der_menu = r_derived_menu(rec)
    isos = k_isomorphisms(rec["cast"], dec_cast, rec["tokens"])
    dir_classes = [tuple(sorted(CELL_INDEX[(x, l)] for x in SITES))
                   for l in I7_LINKS]
    dir_tokens = [tuple(sorted(pi[k] for k in c)) for c in dir_classes]
    autos = k_isomorphisms(dec_cast, dec_cast, rec["tokens"])
    coh = k_coherent(autos, dec_cast, rec["tokens"], dir_tokens)
    matched, stray, missing = k_menu_agreement(der_menu, dec_menu, imap)
    if mut("MUT-MENU"):
        matched = matched[:-1]
    R["menu"] = {
        "declared_members": len(dec_menu), "derived_members": len(der_menu),
        "matched": matched, "stray_block_counts": stray, "unmatched": missing,
    }
    REG.measured("menu_declared", len(dec_menu), "len(declared menu)")
    REG.measured("menu_derived", len(der_menu), "len(derived menu)")
    REG.measured("menu_matched", len(matched), "menu members matched")
    REG.measured("menu_missing", len(missing), "menu members not derived")
    SEAL.seal("menu", R["menu"], "G-MENU-DERIVED")
    gate("G-MENU-DERIVED",
         REG.stmt("the partition menu is derived in part: {menu_matched} of "
                  "the {menu_declared} admissible actor-grain partitions come "
                  "out of the record with no stray member, and "
                  "{menu_missing} do not -- they are the declared direction "
                  "classes, which the record does not name",
                  menu_matched=1, menu_declared=1, menu_missing=1),
         not stray and len(matched) == len(der_menu)
         and len(matched) + len(missing) == len(dec_menu),
         "matched %s stray %s unmatched %s" % (matched, stray or "none",
                                               missing))

    # -- the naming, and its residue ----------------------------------------
    facs = r_triangle_factors(rec)
    reso = r_resolutions(rec)
    aut = b_arena_automorphisms()
    n_iso, n_coh = len(isos), len(coh)
    if mut("MUT-NAMING"):
        n_coh = n_coh + 1
    idx = Fraction(n_iso, n_coh) if n_coh else Fraction(0)
    R["naming"] = {
        "admissible_namings": n_iso, "arena_coherent_namings": n_coh,
        "arena_automorphisms": len(aut),
        "residue_index": [idx.numerator, idx.denominator],
        "direction_candidates": len(facs), "resolutions": len(reso),
    }
    REG.measured("isos", n_iso, "len(k_isomorphisms)")
    REG.measured("coherent", n_coh, "namings carrying the direction classes")
    REG.measured("residue", idx.numerator, "isos / coherent, exact")
    REG.measured("resolutions", len(reso), "direction decompositions")
    REG.measured("factors", len(facs), "candidate direction classes")
    SEAL.seal("naming", R["naming"], "G-NAMING-RESIDUE")
    gate("G-NAMING-RESIDUE",
         REG.stmt("the naming is forced only up to the derived structure's own "
                  "symmetry: {isos} bijections of the derived cast onto the "
                  "declared one carry the link structure across, {coherent} "
                  "of them also carry the declared direction classes, and the "
                  "residue is the index {residue}; the record admits "
                  "{resolutions} ways of splitting its {factors} candidate "
                  "direction classes into a declaration and names none of "
                  "them", isos=1, coherent=1, residue=1, resolutions=1,
                  factors=1),
         idx.denominator == 1 and n_coh == len(aut) and len(reso) == idx.numerator,
         "isos %d coherent %d automorphisms %d index %s resolutions %d"
         % (n_iso, n_coh, len(aut), idx, len(reso)))

    gate("G-RECONSTRUCTION-TARGETS-TOTAL",
         "the pin's five reconstruction targets are each answered by their "
         "own gate and the pin's own list is read back to check that none is "
         "quietly dropped",
         all(w in a_pin.casefold() for w in
             ("site set", "link structure", "cast size", "partition menu",
              "naming")),
         "targets %d" % len(re.findall(r"the [a-z ]+", a_pin)))

    # -- S-1: the regions are disjoint --------------------------------------
    src = read_text(SELF_REL)
    reads.append(SELF_REL)
    if mut("MUT-S1"):
        # a reconstructor function that reaches for a declared-side constant
        src = src + "\n\ndef r_leaks_the_arena():\n    return CELLS\n"
    s1 = audit_regions(src)
    floats = audit_no_floats(src)
    regions = region_census(src)
    R["disjoint_code"] = {"violations": s1, "regions": regions,
                          "float_offences": floats}
    REG.measured("recon_fns", regions.get("reconstructor", 0),
                 "reconstructor functions")
    REG.measured("comp_fns", regions.get("comparator", 0),
                 "comparator functions")
    REG.measured("build_fns", regions.get("builder", 0), "builder functions")
    SEAL.seal("disjoint_code", R["disjoint_code"], "G-S1-DISJOINT-CODE")
    gate("G-S1-DISJOINT-CODE",
         REG.stmt("the comparator is not the builder and the reconstructor is "
                  "neither: an AST scan of this module finds {recon_fns} "
                  "reconstructor functions naming no arena constant and "
                  "calling no builder or comparator, and {comp_fns} "
                  "comparator functions calling neither the {build_fns} "
                  "builder functions nor the reconstructor",
                  recon_fns=1, comp_fns=1, build_fns=1),
         not s1 and not floats, "violations %s floats %s"
         % (s1 or "none", floats or "none"))

    # -- MEASUREMENT TWO: the inverse direction -----------------------------
    fiber = collections.defaultdict(list)
    for i, h in enumerate(bare):
        fiber[h].append(i)
    hist_of = [h for (_t, h) in corp]
    coll = {k: {hist_of[i] for i in v} for k, v in fiber.items()}
    coll = {k: v for k, v in coll.items() if len(v) > 1}
    cryst = [b_crystallization_time(H) for (_t, H) in corp]
    wstar = [b_collapse_threshold(H) for (_t, H) in corp]

    def prop_events(i):
        return len(corp[i][1])

    def prop_written(i):
        return len(bare[i])

    def prop_field(i):
        return fields[i]

    def prop_tag(i):
        return corp[i][0]

    def prop_eventset(i):
        return tuple(sorted(tuple(sorted(SITE_INDEX[x] for x in F))
                            for F in corp[i][1]))

    def prop_blocksize(i):
        return tuple(sorted({len(b) for b in bare[i]})) or (0,)

    def prop_cryst(i):
        return cryst[i]

    def prop_wstar(i):
        return wstar[i]

    def prop_actors(i):
        return tuple(sorted({len(F) for F in corp[i][1]}))

    PROPS = (
        ("EVENTS-IN-THE-HISTORY", prop_events),
        ("EVENTS-THAT-WROTE", prop_written),
        ("THE-COUNT-FIELD", prop_field),
        ("THE-CORPUS-IT-CAME-FROM", prop_tag),
        ("THE-EVENT-SET-ITSELF", prop_eventset),
        ("THE-SIZE-OF-A-RECORD-BLOCK", prop_blocksize),
        ("THE-CRYSTALLIZATION-TIME", prop_cryst),
        ("THE-COLLAPSE-THRESHOLD", prop_wstar),
        ("ACTORS-IN-A-DIVISION-EVENT", prop_actors),
    )
    prows = []
    for nm, fn in PROPS:
        vals = [fn(i) for i in range(len(corp))]
        splits = sum(1 for idx in fiber.values()
                     if len({repr(vals[i]) for i in idx}) > 1)
        distinct = len({repr(v) for v in vals})
        if distinct == 1:
            verdict = "ARENA-FORCED"
        else:
            verdict = "NOT-CARRIED" if splits else "RECORD-CARRIED"
        prows.append({"property": nm, "verdict": verdict,
                      "distinct_values": distinct, "fibers_that_split": splits})
    if mut("MUT-SURPLUS"):
        prows[0]["verdict"] = "RECORD-CARRIED"
    # PER OBJECT (#87): each row's word is bound to the two witnesses the row
    # itself publishes, so a verdict cannot be moved while its numbers stand.
    # The battery bought this: a flipped word left every aggregate intact and
    # the gate passed.
    WORD_OF = {(True, True): "ARENA-FORCED", (True, False): "ARENA-FORCED",
               (False, True): "NOT-CARRIED", (False, False): "RECORD-CARRIED"}
    unbound = [r["property"] for r in prows
               if r["verdict"] != WORD_OF[(r["distinct_values"] == 1,
                                           r["fibers_that_split"] > 0)]]
    nc = sum(1 for p in prows if p["verdict"] == "NOT-CARRIED")
    rc = sum(1 for p in prows if p["verdict"] == "RECORD-CARRIED")
    af = sum(1 for p in prows if p["verdict"] == "ARENA-FORCED")
    R["surplus"] = {
        "distinct_bare_records": len(fiber),
        "collision_classes": len(coll),
        "distinct_histories_in_collisions": sum(len(v) for v in coll.values()),
        "largest_fiber": max(len(v) for v in coll.values()) if coll else 1,
        "histories_lost": R["corpus"]["distinct_histories"] - len(fiber),
        "properties": prows, "rows_unbound": unbound,
        "arena_forced": af, "record_carried": rc, "not_carried": nc,
    }
    REG.measured("bare_records", len(fiber), "distinct bare records")
    REG.measured("collisions", len(coll), "bare records with two histories")
    REG.measured("collided_histories", sum(len(v) for v in coll.values()),
                 "distinct histories inside a collision class")
    REG.measured("lost", R["surplus"]["histories_lost"],
                 "distinct histories minus distinct bare records")
    REG.measured("arena_forced", af, "properties constant over the corpus")
    REG.measured("record_carried", rc, "properties the record determines")
    REG.measured("not_carried", nc, "properties the record does not determine")
    SEAL.seal("surplus", R["surplus"], "G-SURPLUS-CENSUS")
    gate("G-SURPLUS-CENSUS",
         REG.stmt("the inverse direction, censused per property: of the "
                  "properties this unit declares, {arena_forced} are forced "
                  "by the cast and the grammar alone, {record_carried} are "
                  "the record's own surplus, and {not_carried} are not "
                  "carried by the record at all; the corpus's "
                  "{distinct_histories} distinct histories leave only "
                  "{bare_records} distinct bare records, {lost} of them lost "
                  "into {collisions} collision classes holding "
                  "{collided_histories} histories",
                  arena_forced=1, record_carried=1, not_carried=1,
                  distinct_histories=1, bare_records=1, lost=1, collisions=1,
                  collided_histories=1),
         not unbound and af + rc + nc == len(PROPS) and nc > 0 and rc > 0
         and af > 0 and R["surplus"]["histories_lost"] > 0,
         "forced %d carried %d not-carried %d bare %d lost %d unbound %s"
         % (af, rc, nc, len(fiber), R["surplus"]["histories_lost"],
            unbound or "none"))

    # -- MEASUREMENT THREE: the minimality census ---------------------------
    cache: dict = {}

    def decide(bl):
        key = frozenset(bl)
        if key not in cache:
            rr = r_reconstruct([frozenset(b) for b in bl])
            cc, _w = r_certify(rr)
            cache[key] = bool(cc) and k_agree_sets(rr["cast"], dec_cast)
        return cache[key]

    depth_hits, per_hist = 0, collections.Counter()
    for i, h in enumerate(bare):
        d = None
        for p in range(1, len(h) + 1):
            if decide(h[:p]):
                d = p
                break
        if mut("MUT-PERHIST") and i == 0:
            d = 1
        per_hist[(corp[i][0], d)] += 1
        if d is not None:
            depth_hits += 1
    R["minimality_per_history"] = {
        "slots": len(corp), "reconstructing_at_some_prefix": depth_hits,
        "by_corpus": {("%s:%s" % (k[0], k[1])): v
                      for k, v in sorted(per_hist.items(),
                                         key=lambda kv: (kv[0][0],
                                                         -1 if kv[0][1] is None
                                                         else kv[0][1]))},
    }
    REG.measured("per_history_hits", depth_hits,
                 "histories reconstructing at some prefix")
    SEAL.seal("minimality_per_history", R["minimality_per_history"],
              "G-MINIMALITY-PER-HISTORY")
    gate("G-MINIMALITY-PER-HISTORY",
         REG.stmt("no committed history reconstructs the cast at any prefix "
                  "of its own record: {per_history_hits} of {slots}, the "
                  "prefix taken at every depth from one event to the whole "
                  "history", per_history_hits=1, slots=1),
         depth_hits == 0, "reconstructing histories %d of %d"
         % (depth_hits, len(corp)))

    acc, hdepth = set(), None
    for i, h in enumerate(bare):
        acc |= set(h)
        if decide(acc):
            hdepth = i + 1
            break
    acc, edepth, ev, done = set(), None, 0, False
    for h, (_t, H) in zip(bare, corp):
        for F in H:
            ev += 1
            f = b_cell_footprint(F)
            if f:
                acc.add(tuple(sorted(pi[k] for k in f)))
                if decide(acc):
                    edepth, done = ev, True
                    break
        if done:
            break
    if mut("MUT-CORPUS-DEPTH"):
        hdepth = hdepth + 1
    # THE DEPTH IS BOUND AT BOTH ENDS.  The battery bought this too: a depth
    # moved one history later left the old predicate untouched, because it
    # only asked whether SOME prefix worked.
    def hist_prefix(k):
        u = set()
        for h in bare[:k]:
            u |= set(h)
        return u
    tight = (hdepth is not None and edepth is not None
             and decide(hist_prefix(hdepth))
             and not decide(hist_prefix(hdepth - 1)))
    R["minimality_corpus"] = {"histories": hdepth, "events": edepth,
                              "blocks_at_that_point": len(acc),
                              "one_history_earlier_reconstructs":
                                  bool(decide(hist_prefix(hdepth - 1)))}
    REG.measured("corpus_histories", hdepth, "histories read in corpus order")
    REG.measured("corpus_events", edepth, "events read in corpus order")
    SEAL.seal("minimality_corpus", R["minimality_corpus"],
              "G-MINIMALITY-CORPUS")
    gate("G-MINIMALITY-CORPUS",
         REG.stmt("read in the corpus's own order the record reconstructs the "
                  "cast after {corpus_histories} histories and "
                  "{corpus_events} division events, and one history earlier "
                  "it does not", corpus_histories=1, corpus_events=1),
         tight,
         "histories %s events %s blocks %d one-earlier %s"
         % (hdepth, edepth, len(acc),
            R["minimality_corpus"]["one_history_earlier_reconstructs"]))

    drop_ok = sum(1 for j in range(len(blocks))
                  if decide([b for k, b in enumerate(blocks) if k != j]))
    if mut("MUT-BLOCK-MIN"):
        drop_ok = 1
    R["minimality_blocks"] = {"blocks": len(blocks), "drop_one_subsets":
                              len(blocks), "still_reconstructing": drop_ok}
    REG.measured("drop_ok", drop_ok, "26-block subsets that reconstruct")
    SEAL.seal("minimality_blocks", R["minimality_blocks"],
              "G-MINIMALITY-BLOCKS")
    gate("G-MINIMALITY-BLOCKS",
         REG.stmt("every one of the {blocks} record blocks is load-bearing: "
                  "of the {blocks} subsets got by dropping one, "
                  "{drop_ok} reconstruct", blocks=1, drop_ok=1),
         drop_ok == 0 and decide(blocks), "drop-one survivors %d of %d"
         % (drop_ok, len(blocks)))

    # -- the parents' thresholds, re-derived --------------------------------
    a_w = ASET.read("A-FAC-WSTAR", "G-WSTAR-REDERIVED")
    a_c = ASET.read("A-AID-CRYSTALLIZATION", "G-CRYSTALLIZATION-REDERIVED")
    a_s = ASET.read("A-AID-SIGNATURE", "G-CRYSTALLIZATION-REDERIVED")
    w_by = collections.Counter((t, w) for (t, _h), w in zip(corp, wstar))
    c_by = collections.Counter((t, c) for (t, _h), c in zip(corp, cryst))
    if mut("MUT-WSTAR"):
        w_by[("C1", 4)] = w_by[("C1", 4)] - 1
        w_by[("C1", 9)] = 1
    if mut("MUT-CRYST"):
        c_by[("C1", 5)] = c_by[("C1", 5)] - 1
        c_by[("C1", 2)] = 1
    w_vals = sorted({w for (_t, w) in w_by})
    anchor_w = sorted({int(x) for x in re.findall(r"\d+", a_w)})
    anchor_c = [int(x) for x in re.findall(r"exactly (\d+)", a_c)]
    R["wstar"] = {"values": w_vals,
                  "distribution": {"%s:%s" % k: v for k, v in sorted(w_by.items())},
                  "anchor_values": anchor_w}
    REG.measured("w_values", len(w_vals), "distinct collapse thresholds")
    SEAL.seal("wstar", R["wstar"], "G-WSTAR-REDERIVED")
    gate("G-WSTAR-REDERIVED",
         REG.stmt("the parent's collapse threshold is re-derived here by this "
                  "unit's own transfer computation and the {w_values} widths "
                  "it finds are the widths the parent's paper states, read "
                  "back out of that paper's own bytes", w_values=1),
         w_vals == anchor_w,
         "measured %s anchor %s" % (w_vals, anchor_w))

    c1c2 = sorted({c for (t, c) in c_by if t in ("C1", "C2")})
    c3 = sorted(((c if c is not None else -1), c_by[("C3", c)])
                for (t, c) in c_by if t == "C3")
    R["crystallization"] = {
        "C1_C2_constant": c1c2,
        "distribution": {"%s:%s" % k: v for k, v in sorted(
            c_by.items(), key=lambda kv: (kv[0][0], -1 if kv[0][1] is None
                                          else kv[0][1]))},
        "anchor_value": anchor_c,
        "never": c_by[("C3", None)],
    }
    REG.measured("cryst_constant", c1c2[0] if len(c1c2) == 1 else -1,
                 "the C1/C2 crystallization constant")
    REG.measured("cryst_never", c_by[("C3", None)],
                 "histories that never crystallize")
    SEAL.seal("crystallization", R["crystallization"],
              "G-CRYSTALLIZATION-REDERIVED")
    gate("G-CRYSTALLIZATION-REDERIVED",
         REG.stmt("the parent's crystallization time is re-derived here from "
                  "the participation signatures and comes out constant at "
                  "{cryst_constant} on the two concatenating corpora, the "
                  "value the parent's paper states, with {cryst_never} "
                  "histories never crystallizing", cryst_constant=1,
                  cryst_never=1),
         len(c1c2) == 1 and c1c2 == anchor_c and "signature" in a_s.casefold(),
         "C1/C2 %s anchor %s never %d" % (c1c2, anchor_c, c_by[("C3", None)]))

    # -- the parents' delivered receipts, consumed rather than merely digested
    par = {}
    for rel in ("v14/code/fac_receipt.json", "v14/code/epr_receipt.json",
                "v14/code/aid_receipt.json"):
        with open(os.path.join(REPO, rel), "r", encoding="utf-8") as fh:
            par[rel] = json.load(fh)
        reads.append(rel)
    F = par["v14/code/fac_receipt.json"]
    E = par["v14/code/epr_receipt.json"]
    A = par["v14/code/aid_receipt.json"]
    checks = [
        ("sites", F["arena"]["sites"], NACT),
        ("declared_links", F["arena"]["declared_links"], len(I7_LINKS)),
        ("parallel_classes", F["arena"]["parallel_classes"], len(CLASS_NAMES)),
        ("groupings", F["arena"]["groupings"], len(parts)),
        ("saturating_groupings", F["arena"]["saturating_groupings"], len(sat)),
        ("strict_triples", F["arena"]["strict_triples"], len(strict)),
        ("flat_quadruples", F["arena"]["flat_quadruples"], len(flatq)),
        ("window_schedules", F["arena"]["window_schedules"], len(scheds)),
        ("arena_automorphisms", F["arena"]["arena_automorphism_order"],
         len(aut)),
        ("cells", F["carrier"]["cells"], DIM),
        ("co_division_pairs", F["carrier"]["distinct_co_division_pairs"],
         len(pairs)),
        ("cells_per_actor", F["carrier"]["cells_per_actor"],
         sorted(set(per_actor.values()))),
        ("C1", F["corpora"]["C1_strict_triples"], bytag["C1"]),
        ("C2", F["corpora"]["C2_concatenations"], bytag["C2"]),
        ("C3", F["corpora"]["C3_window_schedules"], bytag["C3"]),
        ("total_histories", F["corpora"]["total_histories"], len(corp)),
        ("distinct_histories", F["corpora"]["distinct_histories"],
         R["corpus"]["distinct_histories"]),
        ("events_per_history", F["corpora"]["events_per_history"],
         R["corpus"]["event_lengths"]),
        ("epr_histories", E["corpora"]["histories"], len(corp)),
        ("epr_distinct_record_fields", E["corpora"]["distinct_record_fields"],
         len(set(fields))),
        ("epr_site_constant", E["corpora"]["record_is_site_constant_at"],
         site_const),
        ("epr_largest_count", E["corpora"]["largest_count_in_the_corpus"],
         R["level_zero"]["largest_count"]),
        ("aid_crystallization_constant",
         A["crystallization"]["constant_on_C1_C2_C1FAN"],
         c1c2[0] if len(c1c2) == 1 else None),
        ("aid_never_crystallizing", A["crystallization"]["never_crystallizing"],
         c_by[("C3", None)]),
    ]
    if mut("MUT-PARENTS"):
        checks[0] = ("sites", F["arena"]["sites"] + 1, NACT)
    disagree = [c[0] for c in checks if c[1] != c[2]]
    R["parents"] = {
        "receipts": {k.split("/")[-1]: shas[k] for k in sorted(par)},
        "quantities": [{"quantity": c[0], "parent": c[1], "here": c[2],
                        "agrees": c[1] == c[2]} for c in checks],
        "disagreements": disagree, "quantities_compared": len(checks),
    }
    SEAL.seal("parents", R["parents"], "G-PARENTS-AGREE")
    REG.measured("parent_checks", len(checks), "len(checks)")
    REG.measured("parent_receipts", len(par), "sibling receipts read")
    gate("G-PARENTS-AGREE",
         REG.stmt("the {parent_receipts} parent receipts are read at their "
                  "pinned digests and their DELIVERED VALUES are consumed, "
                  "not merely their digests: {parent_checks} quantities this "
                  "unit re-derives from its own constructors are compared "
                  "against the parents' own, one by one",
                  parent_receipts=1, parent_checks=1),
         not disagree, "quantities %d disagreements %s"
         % (len(checks), disagree or "none"))

    joint = collections.Counter(
        (c if c is not None else -1, w, "NEVER") for c, w in zip(cryst, wstar))
    if mut("MUT-CONNECTION"):
        k0 = sorted(joint)[0]
        joint[(k0[0], k0[1], "REACHED")] = joint.pop(k0)
    R["connection"] = {
        "rows": [{"crystallization": k[0], "collapse_threshold": k[1],
                  "reconstruction_depth": k[2], "histories": v}
                 for k, v in sorted(joint.items())],
        "declared_side_finite": sum(v for k, v in joint.items() if k[1] is not None),
        "record_side_reached": depth_hits,
    }
    SEAL.seal("connection", R["connection"], "G-THE-CONNECTION")
    REG.measured("joint_rows", len(joint), "distinct joint rows")
    gate("G-THE-CONNECTION",
         REG.stmt("the three depths are put in one table, {joint_rows} rows "
                  "of it: both declared-side thresholds are finite at every "
                  "history that has one, and the record-side depth is reached "
                  "at {per_history_hits}, so the reconstruction depth is not "
                  "the collapse threshold and is not the crystallization "
                  "time", joint_rows=1, per_history_hits=1),
         all(k[2] == "NEVER" for k in joint) and depth_hits == 0,
         "rows %d declared-finite %d record-reached %d"
         % (len(joint), R["connection"]["declared_side_finite"], depth_hits))

    # -- MEASUREMENT FOUR: the obstruction ----------------------------------
    a_unl = ASET.read("A-EPR-UNLINKED", "G-OBSTRUCTION-NAMED")
    empty_hist = sum(1 for h, (_t, H) in zip(bare, corp) if len(h) < len(H))
    silent = [i for i, h in enumerate(bare) if not h]
    undeclared = [d for d in (CLASS_DIR[k] for k in CLASS_NAMES)
                  if d not in I7_LINKS]
    unwritten = R["corpus"]["events"] - written
    if mut("MUT-OBSTRUCTION"):
        unwritten = unwritten + 1
    R["obstruction"] = {
        "name": "THE-LINK-DECLARATION",
        "undeclared_classes": len(undeclared),
        "unwritten_events": unwritten,
        "histories_with_an_unwritten_event": empty_hist,
        "histories_writing_nothing": len(silent),
        "silent_history_events": sorted({len(corp[i][1]) for i in silent}),
        "residue_index": [idx.numerator, idx.denominator],
        "resolutions": len(reso),
    }
    REG.measured("silent", len(silent), "histories that write nothing at all")
    REG.measured("empty_hist", empty_hist,
                 "histories with at least one unwritten event")
    SEAL.seal("obstruction", R["obstruction"], "G-OBSTRUCTION-NAMED")
    gate("G-OBSTRUCTION-NAMED",
         REG.stmt("the datum that resists is THE LINK DECLARATION, and it "
                  "resists twice: {unwritten} division events write nothing "
                  "because both their ends lie in the one parallel class the "
                  "arena does not declare, leaving {empty_hist} histories "
                  "partly unwritten and {silent} written not at all; and the "
                  "three classes that ARE declared are not named by the "
                  "record, which admits {resolutions} splittings of its "
                  "candidate classes at residue index {residue}",
                  unwritten=1, empty_hist=1, silent=1, resolutions=1,
                  residue=1),
         unwritten == R["corpus"]["events"] - written and len(undeclared) == 1
         and len(silent) > 0 and "does not declare" in a_unl.casefold(),
         "unwritten %d partly %d silent %d undeclared classes %d"
         % (unwritten, empty_hist, len(silent), len(undeclared)))

    # -- the control arms ---------------------------------------------------
    scr, scr_rows = [], collections.Counter()
    base = list(blocks)
    for j in range(len(base)):
        for shift in (1, 2):
            bl = list(base)
            alien = tuple(sorted({(t + shift) % DIM for t in base[j]}))
            if len(alien) < 3 or alien in base:
                continue
            bl[j] = alien
            rr = r_reconstruct([frozenset(x) for x in bl])
            cc, wy = r_certify(rr)
            agree = cc and k_agree_sets(rr["cast"], dec_cast)
            scr_rows[("REPLACE", bool(agree))] += 1
            scr.append(agree)
    for j in range(len(base)):
        bl = [b for k, b in enumerate(base) if k != j]
        rr = r_reconstruct([frozenset(x) for x in bl])
        cc, wy = r_certify(rr)
        agree = cc and k_agree_sets(rr["cast"], dec_cast)
        scr_rows[("DROP", bool(agree))] += 1
        scr.append(agree)
    for u, v in combinations(range(len(base)), 2):
        if u > 8:
            break
        bl = list(base)
        a, b = list(base[u]), list(base[v])
        if a[0] == b[0]:
            continue
        a[0], b[0] = b[0], a[0]
        if len(set(a)) < 3 or len(set(b)) < 3:
            continue
        bl[u], bl[v] = tuple(sorted(a)), tuple(sorted(b))
        if sorted(bl) == sorted(base):
            continue
        rr = r_reconstruct([frozenset(x) for x in bl])
        cc, wy = r_certify(rr)
        agree = cc and k_agree_sets(rr["cast"], dec_cast)
        scr_rows[("SWAP", bool(agree))] += 1
        scr.append(agree)
    survivors = sum(1 for s in scr if s)
    if mut("MUT-SCRAMBLE-CONTROL"):
        survivors = 0 if survivors else 1
    R["control_scrambled"] = {
        "trials": len(scr), "survivors": survivors,
        "by_shape": {"%s:%s" % k: v for k, v in sorted(scr_rows.items())},
    }
    REG.measured("scr_trials", len(scr), "scrambled records tried")
    REG.measured("scr_survivors", survivors, "scrambles the comparator passed")
    SEAL.seal("control_scrambled", R["control_scrambled"],
              "G-CONTROL-SCRAMBLED-FAILS")
    gate("G-CONTROL-SCRAMBLED-FAILS",
         REG.stmt("the control arm the pin asks for, run through the REAL "
                  "reconstructor: {scr_trials} scrambled records, of which "
                  "{scr_survivors} reach the declared cast", scr_trials=1,
                  scr_survivors=1),
         survivors == 0 and len(scr) > len(base),
         "trials %d survivors %d" % (len(scr), survivors))

    syn_rows, syn_bad = [], []
    for pshape in SYNTHETIC_PARTS:
        sb, sstars, ntok = synthetic_record(pshape)
        rr = r_reconstruct(sb)
        cc, wy = r_certify(rr)
        agree = cc and k_agree_sets(rr["cast"], sstars)
        balanced = len(pshape) == 3 and len(set(pshape)) == 1
        if mut("MUT-SYNTHETIC") and balanced:
            agree = not agree
        syn_rows.append({"parts": list(pshape), "tokens": ntok,
                         "blocks": len(sb), "certificate": wy,
                         "cast_recovered": bool(agree),
                         "cast_size": len(rr["cast"])})
        if balanced and not agree:
            syn_bad.append(pshape)
        if not balanced and agree:
            syn_bad.append(pshape)
    good = sum(1 for r in syn_rows if r["cast_recovered"])
    R["control_synthetic"] = {"arms": len(syn_rows), "recovered": good,
                              "rows": syn_rows}
    REG.measured("syn_arms", len(syn_rows), "synthetic arenas built")
    REG.measured("syn_good", good, "synthetic casts recovered exactly")
    SEAL.seal("control_synthetic", R["control_synthetic"],
              "G-CONTROL-SYNTHETIC-SUCCEEDS")
    gate("G-CONTROL-SYNTHETIC-SUCCEEDS",
         REG.stmt("the second control arm: {syn_arms} synthetic minimal "
                  "records built from casts that are not this arena's, of "
                  "which {syn_good} are reconstructed exactly -- the balanced "
                  "three-part ones -- and the rest are REFUSED rather than "
                  "answered wrongly", syn_arms=1, syn_good=1),
         not syn_bad, "arms %d recovered %d mismatched %s"
         % (len(syn_rows), good, syn_bad or "none"))

    teeth = [r for r in syn_rows
             if r["certificate"] == "CERTIFIED" and r["cast_size"] != NACT]
    if mut("MUT-TEETH"):
        teeth = []
    R["comparator_teeth"] = {
        "certified_reconstructions_refused": len(teeth),
        "per_history_refusals": len(corp) - depth_hits,
        "scrambles_refused": len(scr) - survivors,
    }
    REG.measured("teeth", len(teeth),
                 "certified reconstructions the comparator refused")
    SEAL.seal("comparator_teeth", R["comparator_teeth"],
              "G-COMPARATOR-HAS-TEETH")
    gate("G-COMPARATOR-HAS-TEETH",
         REG.stmt("the comparator can fail and does: it refuses {teeth} "
                  "reconstructions that carry the reconstructor's own "
                  "certificate, every one of the {scr_trials} scrambles, and "
                  "every one of the {slots} per-history attempts",
                  teeth=1, scr_trials=1, slots=1),
         len(teeth) > 0, "certified-but-refused %d" % len(teeth))

    # -- THE VERDICT, derived --------------------------------------------
    derived_word = head_word_of(cast_exact, der_pairs == dec_pairs,
                                len(rec["cast"]) == NACT, len(missing),
                                idx.numerator)
    head = [
        "REC-RECONSTRUCTION<CORPUS=%s; DISTINCT-HISTORIES=%s; "
        "RECORD-BLOCKS=%s; SITE-SET=%s-OF-%s-EXACT; LINK-STRUCTURE=%s-OF-%s-"
        "EXACT; CAST-SIZE=%s-DERIVED; MENU=%s-OF-%s-EXACT; NAMING=%s-"
        "ADMISSIBLE-%s-ARENA-COHERENT; RESIDUE-INDEX=%s; LEVEL-0-COUNT-FIELD="
        "%s-DISTINCT-CAST-NOT-DERIVABLE>"
        % (com(len(corp)), com(R["corpus"]["distinct_histories"]),
           com(len(blocks)), com(len(rec["cast"])), com(NACT),
           com(len(der_pairs)), com(DIM), com(len(rec["cast"])),
           com(len(matched)), com(len(dec_menu)), com(n_iso), com(n_coh),
           com(idx.numerator), com(len(set(fields)))),
        "REC-MINIMALITY<PER-HISTORY=%s-OF-%s-AT-EVERY-PREFIX; CORPUS-ORDER=%s-"
        "HISTORIES-%s-EVENTS; BLOCK-MINIMAL=%s-OF-%s-DROP-ONE-SURVIVORS-%s; "
        "COLLAPSE-THRESHOLDS=%s; CRYSTALLIZATION-ON-C1-AND-C2=%s; "
        "NEVER-CRYSTALLIZING=%s>"
        % (com(depth_hits), com(len(corp)), com(hdepth), com(edepth),
           com(len(blocks)), com(len(blocks)), com(drop_ok),
           "-AND-".join(str(w) for w in w_vals), com(c1c2[0]),
           com(c_by[("C3", None)])),
        "%s<OBSTRUCTION=THE-"
        "LINK-DECLARATION; UNWRITTEN-EVENTS=%s; PARTLY-UNWRITTEN-HISTORIES=%s;"
        " HISTORIES-WRITING-NOTHING=%s; RECORD-COLLISIONS=%s-CLASSES-%s-"
        "HISTORIES; SURPLUS=%s-ARENA-FORCED-%s-RECORD-CARRIED-%s-NOT-CARRIED; "
        "CONTROLS=%s-SCRAMBLES-%s-SURVIVE-AND-%s-OF-%s-SYNTHETIC-ARMS-"
        "RECOVERED; SCOPE=ONE-ARENA,COMMITTED-HISTORIES,COUNTS-ARE-COUNTING-"
        "ONLY;THE-CAST-IS-DERIVED-AT-THE-CORPUS-AND-AT-NO-SINGLE-HISTORY>"
        % (derived_word,
           com(unwritten), com(empty_hist), com(len(silent)), com(len(coll)),
           com(sum(len(v) for v in coll.values())), com(af), com(rc), com(nc),
           com(len(scr)), com(survivors), com(good), com(len(syn_rows))),
    ]
    if mut("MUT-HEAD"):
        head[2] = head[2].replace("UP-TO-THE-DIRECTION-DECLARATION", "")
    R["verdict"] = {"segments": head, "word": head[2].split("<")[0]}

    HEAD_FIELDS = (
        (0, "CORPUS", ("corpus", "slots")),
        (0, "DISTINCT-HISTORIES", ("corpus", "distinct_histories")),
        (0, "RECORD-BLOCKS", ("stripping", "record_blocks")),
        (0, "CAST-SIZE", ("reconstruction", "cast_size")),
        (0, "NAMING", ("naming", "admissible_namings")),
        (0, "RESIDUE-INDEX", ("naming", "residue_index", 0)),
        (1, "PER-HISTORY", ("minimality_per_history",
                            "reconstructing_at_some_prefix")),
        (1, "CORPUS-ORDER", ("minimality_corpus", "histories")),
        (1, "NEVER-CRYSTALLIZING", ("crystallization", "never")),
        (2, "UNWRITTEN-EVENTS", ("obstruction", "unwritten_events")),
        (2, "PARTLY-UNWRITTEN-HISTORIES",
         ("obstruction", "histories_with_an_unwritten_event")),
        (2, "HISTORIES-WRITING-NOTHING",
         ("obstruction", "histories_writing_nothing")),
    )
    probes = [head_word_of(True, True, True, 0, 1),
              head_word_of(True, True, True, len(missing), idx.numerator),
              head_word_of(False, True, True, 0, 1),
              head_word_of(True, False, True, 0, 1)]
    printed = head[2].split("<")[0]
    carries = printed.endswith(QUALIFIER)
    owed = (len(missing) > 0 or idx.numerator > 1)
    base = printed[:-len(QUALIFIER)] if carries else printed
    parsed_bad = []
    if carries != owed:
        parsed_bad.append("the head %s the residue qualifier while the "
                          "measurement %s it"
                          % ("carries" if carries else "drops",
                             "owes" if owed else "does not owe"))
    if base != head_word_of(cast_exact, der_pairs == dec_pairs,
                            len(rec["cast"]) == NACT, 0, 1):
        parsed_bad.append("the head's base word is not the derived one: %s"
                          % base)
    if len(set(probes)) != len(probes):
        parsed_bad.append("the outcome words are not distinguishable: %s"
                          % probes)
    for seg, key, path in HEAD_FIELDS:
        got = k_parse_head(head[seg]).get(key)
        want = R
        for step in path:
            want = want[step]
        if got is None or got != want:
            parsed_bad.append("%s: head %s receipt %s" % (key, got, want))
    SEAL.seal("verdict", R["verdict"], "G-VERDICT-EQUALITY")
    REG.measured("head_fields", len(HEAD_FIELDS), "len(HEAD_FIELDS)")
    gate("G-VERDICT-EQUALITY",
         REG.stmt("the verdict is not trusted to its own renderer: each of "
                  "{head_fields} declared head fields is PARSED back out of "
                  "the emitted string and compared, as an integer, with the "
                  "receipt leaf it names -- a parser against a builder, "
                  "sharing no code and no literal -- and the verdict WORD is "
                  "bound both ways to the measurement that owes it, with the "
                  "pre-registered outcomes shown distinguishable on declared "
                  "probes", head_fields=1),
         not parsed_bad, "fields %d outcomes %d mismatched %s"
         % (len(HEAD_FIELDS), len(set(probes)), parsed_bad or "none"))

    # -- the paper --------------------------------------------------------
    t_recon = CL.table(
        "T-RECONSTRUCTION",
        ("target", "algorithm reads", "derived", "declared", "verdict"),
        [("the site set", "record blocks", com(len(rec["cast"])),
          com(NACT), "EXACT"),
         ("the link structure", "record blocks", com(len(der_pairs)),
          com(DIM), "EXACT"),
         ("the cast size", "record blocks", com(len(rec["cast"])),
          com(NACT), "EXACT"),
         ("the partition menu", "record blocks", com(len(matched)),
          com(len(dec_menu)), "PARTIAL"),
         ("the naming", "record blocks", com(n_iso), com(n_coh),
          "UP TO THE RESIDUE")])
    t_prop = CL.table(
        "T-SURPLUS", ("property of the history", "verdict", "values"),
        [(p["property"], p["verdict"], com(p["distinct_values"]))
         for p in prows])
    t_depth = CL.table(
        "T-DEPTHS", ("depth", "object it measures", "C1", "C2", "C3"),
        [("crystallization time", "the naming, given the cast",
          com(c_by[("C1", 5)]) + " at 5", com(c_by[("C2", 5)]) + " at 5",
          "stratified"),
         ("collapse threshold", "coherence width, given the cast",
          com(w_by[("C1", 4)]) + " at 4", com(w_by[("C2", 4)]) + " at 4",
          "3, 4, 5"),
         ("reconstruction depth", "the cast itself", "never", "never",
          "never")])
    t_syn = CL.table(
        "T-SYNTHETIC", ("parts", "tokens", "blocks", "certificate",
                        "cast recovered"),
        [("+".join(str(x) for x in r["parts"]), com(r["tokens"]),
          com(r["blocks"]), r["certificate"],
          "yes" if r["cast_recovered"] else "no") for r in syn_rows])

    c1 = CL.claim("the cast is derived at the corpus and at no single history",
                  times=2)
    c2 = CL.claim("the direction declaration is the datum that resists",
                  times=2)
    c3 = CL.claim("record-completeness is analytic at EPR's own catalogue")
    c4 = CL.claim("%s of %s committed histories reconstruct the cast at any "
                  "prefix of their own record"
                  % (com(depth_hits), com(len(corp))))
    c5 = CL.claim("every one of the %s record blocks is load-bearing: of the "
                  "%s subsets got by dropping one, %s reconstruct"
                  % (com(len(blocks)), com(len(blocks)), com(drop_ok)))
    c6 = CL.claim("the record admits %s namings of the derived cast and %s of "
                  "them carry the declared direction classes"
                  % (com(n_iso), com(n_coh)))
    f1 = CL.fence(head[0])
    f2 = CL.fence(head[1])
    f3 = CL.fence(head[2])
    if mut("MUT-PAPER-CLAIM"):
        CL.claim("a claim the paper does not carry")
    if render:
        R["rendered"] = {"tables": [t_recon, t_prop, t_depth, t_syn],
                         "claims": [c1, c2, c3, c4, c5, c6],
                         "fences": [f1, f2, f3]}
        return R, TR, LD, SEAL, None
    try:
        ev, cprob = CL.gate(paper), None
    except ET.CheckFail as exc:
        ev, cprob = {"rows": 0, "prose": 0, "fences": 0}, exc.detail
    R["paper_claims"] = {"rows": ev["rows"], "claims": ev["prose"],
                         "fences": ev["fences"],
                         "sha256_12": ET.bytes_digest(paper.encode("utf-8"))}
    SEAL.seal("paper_claims", R["paper_claims"], "G-PAPER-CLAIMS")
    REG.measured("rows", ev["rows"], "rendered table rows")
    REG.measured("claims", ev["prose"], "licensed prose occurrences")
    REG.measured("fences", ev["fences"], "licensed fenced blocks")
    gate("G-PAPER-CLAIMS",
         REG.stmt("the paper's {rows} table rows are keyed by their table and "
                  "matched both ways, its {claims} licensed prose occurrences "
                  "are matched at their exact counts, and its {fences} fenced "
                  "blocks by multiset equality", rows=1, claims=1, fences=1),
         cprob is None, "rows %d claims %d fences %d %s"
         % (ev["rows"], ev["prose"], ev["fences"], cprob or ""))

    # The universes are declared in the order the sentence selector reads
    # them, most specific first, so a sentence about a control arm is never
    # resolved against the cast and a sentence about a depth never against the
    # corpus.  Every value is a live measurement.
    RR.universe("CONTROLS",
                ["corruption", "corruptions", "control", "controls",
                 "scramble", "scrambles", "arm", "arms", "synthetic"],
                {len(scr), survivors, len(syn_rows), good, len(teeth)}
                | {x for shape in SYNTHETIC_PARTS for x in shape})
    RR.universe("CELLS", ["cell", "cells", "token", "tokens", "record block",
                          "record blocks"],
                {DIM, drop_ok, rec["tau"], 2 * DIM // NACT, len(rec["cast"]) // 3,
                 len(pi) // len(pi)} | {2, len(I7_LINKS)},
                pairs={(drop_ok, DIM), (DIM, DIM)})
    RR.universe("NAMINGS", ["naming", "namings", "relabelling",
                            "relabellings", "splitting", "splittings",
                            "coordinate"],
                {n_iso, n_coh, idx.numerator, len(reso), len(facs),
                 len(trials)},
                pairs={(n_coh, n_iso)})
    RR.universe("DEPTHS", ["threshold", "thresholds", "crystallization",
                           "width", "widths", "depth", "depths", "meet"],
                set(rec["meets"]) | set(w_vals) | {c1c2[0], hdepth, edepth,
                                                   rec["tau"]})
    RR.universe("CORPUS", ["history", "histories", "corpus", "slot", "slots",
                           "division event", "division events", "prefix",
                           "prefixes"],
                {len(corp), R["corpus"]["distinct_histories"], len(fiber),
                 R["surplus"]["histories_lost"], depth_hits, hdepth, edepth,
                 unwritten, written, empty_hist, len(silent), len(coll),
                 sum(len(v) for v in coll.values()), R["corpus"]["events"],
                 len(set(fields)), len(strict), len(scheds), bytag["C2"],
                 len(blocks)},
                pairs={(depth_hits, len(corp))})
    RR.universe("CAST", ["actor", "actors", "cast", "site", "sites"],
                {NACT, 2 * DIM // NACT, NACT * (NACT - 1), len(link_parts or ()),
                 2},
                pairs={(NACT * (NACT - 1), NACT * (NACT - 1)), (NACT, NACT)})
    if mut("MUT-REFERENT"):
        paper_r = paper + "\n\nThe cast carries %d actors.\n" % len(corp)
    else:
        paper_r = paper
    # PROSE, in the strict sense: fenced blocks AND rendered table rows are
    # removed.  Both are bound elsewhere and more tightly -- fences and rows
    # by two-way multiset equality keyed by table -- so neither may discharge
    # a prose obligation, and neither may create one.
    prose_only = "\n".join(
        ln for ln in ET.ReferentRegistry.prose_only(paper_r).splitlines()
        if not re.match(r"^\s*\|.*\|\s*$", ln))
    try:
        rev, rprob = RR.gate(prose_only), None
    except ET.CheckFail as exc:
        rev, rprob = {"occurrences_checked": 0}, exc.detail
    R["paper_referents"] = {"universes": len(RR.universes),
                            "occurrences_checked": rev["occurrences_checked"]}
    SEAL.seal("paper_referents", R["paper_referents"], "G-PAPER-REFERENTS")
    REG.measured("universes", len(RR.universes), "len(RR.universes)")
    REG.measured("occurrences", rev["occurrences_checked"],
                 "numeral occurrences bound to a universe")
    gate("G-PAPER-REFERENTS",
         REG.stmt("every numeral occurrence in the paper's PROSE whose "
                  "sentence names one of the {universes} declared universes "
                  "is resolved against that universe and no other, "
                  "{occurrences} of them, each occurrence and never an "
                  "aggregate", universes=1, occurrences=1),
         rprob is None, "universes %d occurrences %d %s"
         % (len(RR.universes), rev["occurrences_checked"], rprob or ""))

    wall_text = paper
    if mut("MUT-WALL"):
        wall_text = paper.replace(
            "the cast is derived at the corpus and at no single history",
            "the cast is derived", 1)
    wprob = None
    for w in WALLS:
        try:
            w.scan(wall_text)
        except ET.CheckFail as exc:
            wprob = exc.detail
    R["walls"] = [w.seal_value() for w in WALLS]
    SEAL.seal("walls", R["walls"], "G-PAPER-WALLS")
    REG.measured("walls", len(WALLS), "len(WALLS)")
    REG.measured("wall_patterns", sum(len(w.negative) for w in WALLS),
                 "banned patterns")
    REG.measured("wall_positive", sum(len(w.positive) for w in WALLS),
                 "standing sentences the paper must carry")
    gate("G-PAPER-WALLS",
         REG.stmt("the {walls} reading walls scan the paper itself: "
                  "{wall_patterns} voice-normalised banned patterns find "
                  "nothing and {wall_positive} standing sentences are "
                  "present, so the walls are not one deletion away from "
                  "vacuous", walls=1, wall_patterns=1, wall_positive=1),
         wprob is None, "walls %d patterns %d positive %d %s"
         % (len(WALLS), sum(len(w.negative) for w in WALLS),
            sum(len(w.positive) for w in WALLS), wprob or ""))

    backing = set()

    def harvest(o):
        if isinstance(o, bool):
            return
        if isinstance(o, int):
            backing.add(o)
        elif isinstance(o, dict):
            for k, v in o.items():
                for m in re.findall(r"\d+", str(k)):
                    backing.add(int(m))
                harvest(v)
        elif isinstance(o, (list, tuple)):
            for v in o:
                harvest(v)
        elif isinstance(o, str):
            for m in re.findall(r"\d+", o):
                backing.add(int(m))
    harvest(R)
    EXEMPT = {33: "paper-33, the AID unit", 35: "paper-35, the FAC unit",
              38: "paper-38, the EPR unit", 41: "paper-41, this unit",
              21: "paper-21, the schedule parent", 373: "the ledger entry",
              14: "the campaign, v14", 25: "engraving E-25",
              33000: "unused"}
    EXEMPT.pop(33000)
    cov = [n for n in paper_numerals(paper)
           if int(n) not in backing and int(n) not in EXEMPT]
    if mut("MUT-COVERAGE"):
        cov.append("injected")
    R["paper_coverage"] = {"numerals": len(paper_numerals(paper)),
                           "unbacked": sorted(set(cov)),
                           "exemptions": {str(k): v for k, v in
                                          sorted(EXEMPT.items())}}
    SEAL.seal("paper_coverage", R["paper_coverage"], "G-PAPER-COVERAGE")
    REG.measured("numerals", len(paper_numerals(paper)),
                 "numerals in the paper, fences included")
    REG.measured("unbacked", len(set(cov)), "numerals backed by nothing")
    gate("G-PAPER-COVERAGE",
         REG.stmt("every one of the paper's {numerals} numerals -- fenced "
                  "blocks, verdict blocks and tables included -- is a value "
                  "this receipt carries or a declared exemption, and "
                  "{unbacked} are neither", numerals=1, unbacked=1),
         not cov, "numerals %d unbacked %s"
         % (len(paper_numerals(paper)), sorted(set(cov)) or "none"))

    # -- anchors, typed counts, exactness ----------------------------------
    if mut("MUT-ANCHOR-CONSUMER"):
        ANCHORS[0].consumer = "G-CORPUS-SHAPE"
    try:
        ASET.verify_consumption(LD)
        aprob = None
    except ET.CheckFail as exc:
        aprob = exc.detail
    R["anchors"] = [{"name": a.name, "source": a.source,
                     "consumer": a.consumer, "chars": len(a.needle),
                     "read_by": sorted(a.read_by)} for a in ANCHORS]
    SEAL.seal("anchors", R["anchors"], "G-ANCHORS-CONSUMED")
    REG.measured("anchors", len(ANCHORS), "len(ANCHORS)")
    gate("G-ANCHORS-CONSUMED",
         REG.stmt("each of the {anchors} verbatim anchors occurs exactly once "
                  "in the pinned parent AND once in this paper's own "
                  "rendering, and its declared consumer gate took a value out "
                  "of it and compared that value with a measurement",
                  anchors=1),
         aprob is None and all(a.consumer in a.read_by for a in ANCHORS),
         "anchors %d consumed %d %s"
         % (len(ANCHORS), sum(1 for a in ANCHORS if a.consumer in a.read_by),
            aprob or ""))

    typed = REG.audit_module(src, statement_callers=("stmt", "claim"))
    if mut("MUT-TYPED"):
        typed = typed + ["injected: 'a statement with the numeral 9 typed'"]
    R["typed_counts"] = {"offenders": typed,
                         "registry": len(REG.values),
                         "exemptions": sorted(REG.exempt)}
    SEAL.seal("typed_counts", R["typed_counts"], "G-NO-TYPED-COUNTS")
    REG.measured("registry", len(REG.values), "measured names in the registry")
    gate("G-NO-TYPED-COUNTS",
         REG.stmt("no numeral is typed into anything this unit vouches for: "
                  "every published statement interpolates from the "
                  "{registry} measured names, and an AST scan of this module "
                  "finds no string literal handed to a statement builder that "
                  "types a numeral", registry=1),
         not typed, "offenders %s" % (typed or "none"))

    bad_types = []

    def typewalk(o, path):
        if isinstance(o, (bool, int, str)) or o is None:
            return
        if isinstance(o, float):
            bad_types.append(path)
            return
        if isinstance(o, dict):
            for k, v in o.items():
                typewalk(v, path + "/" + str(k))
        elif isinstance(o, (list, tuple)):
            for i, v in enumerate(o):
                typewalk(v, path + "[%d]" % i)
        else:
            bad_types.append(path + ":" + type(o).__name__)
    typewalk(R, "")
    if mut("MUT-FLOAT"):
        bad_types.append("/injected")
    # the round-trip leg: a receipt whose digest moves when it goes through
    # JSON and back cannot be verified after promotion (an int-keyed dict is
    # the way this happens, and it is how this instrument first failed).
    roundtrip = ET.digest(json.loads(json.dumps(
        R, sort_keys=True, ensure_ascii=False))) == ET.digest(R)
    R["exactness"] = {"float_leaves": bad_types,
                      "ast_float_offences": floats,
                      "json_round_trip_stable": bool(roundtrip)}
    SEAL.seal("exactness", R["exactness"], "G-RECEIPT-EXACT")
    gate("G-RECEIPT-EXACT",
         "no float reaches the receipt and none is written in the module: a "
         "recursive type walk of every published leaf and an AST scan of this "
         "source agree; and the receipt's digest survives a JSON round trip, "
         "so what is verified after promotion is what was sealed",
         not bad_types and not floats and roundtrip,
         "float leaves %s ast %s round-trip %s"
         % (bad_types or "none", floats or "none", roundtrip))

    # -- provenance, reads, transcript, promotion --------------------------
    R["provenance"] = {
        "unit": "REC", "paper": PAPER_REL, "instrument": SELF_REL,
        "pin": PIN_REL, "pin_sha256_12": shas[PIN_REL],
        "template": TEMPLATE_REL, "template_sha256_12": shas[TEMPLATE_REL],
        "self_sha256_12": sha12(os.path.join(REPO, SELF_REL)),
        "paper_sha256_12": ET.bytes_digest(paper.encode("utf-8")),
        "families_adopted": [c for _k, _n, c in ET.FAMILIES],
        "scramble": {"multiplier": SCRAMBLE_MULT, "offset": SCRAMBLE_ADD,
                     "note": "a declared arena-blind coordinate; "
                             "G-STRIPPING-EQUIVARIANT prices it"},
    }
    R["reconstruction_rule"] = {
        "sharing": "two record cells belong to a common actor exactly when "
                   "one event wrote them together, or when the cells written "
                   "with each of them meet in the largest number any "
                   "never-co-written pair attains",
        "cast": "an actor is a maximal set of cells that pairwise belong to "
                "one actor, of the largest size such a set attains",
        "threshold_is_derived": True,
    }

    if mut("MUT-PROVENANCE"):
        R["provenance"]["pin_sha256_12"] = R["provenance"]["pin_sha256_12"][::-1]
    dig12 = [k for k, v in R["provenance"].items()
             if k.endswith("sha256_12")
             and len(v) == len(SOURCES[PIN_REL])
             and all(c in "0123456789abcdef" for c in v)]
    prov_ok = (len(dig12) == sum(1 for k in R["provenance"]
                                 if k.endswith("sha256_12"))
               and R["provenance"]["pin_sha256_12"] == SOURCES[PIN_REL]
               and R["provenance"]["template_sha256_12"] == SOURCES[TEMPLATE_REL])
    R["mutants"] = [{"name": m[0], "gate": m[1], "target": m[2],
                     "description": m[3]} for m in MUTANTS]
    # the gates that fire at or after this one, named so a falsifier for a
    # closing gate is not misread as unreachable
    closing = {"G-PROVENANCE", "G-READS-AT-THE-ACCESSOR",
               "T-FALSIFIER-COVERAGE", "G-TRANSCRIPT-BOUND"}
    allowed = set(LD.names()) | closing | {c for _k, _n, c in ET.FAMILIES}
    bad_mut = sorted(m["name"] for m in R["mutants"]
                     if m["gate"] not in allowed or not m["target"].strip())
    names_unique = len({m["name"] for m in R["mutants"]}) == len(R["mutants"])
    SEAL.seal("provenance", R["provenance"], "G-PROVENANCE")
    SEAL.seal("mutants", R["mutants"], "G-PROVENANCE")
    SEAL.seal("reconstruction_rule", R["reconstruction_rule"], "G-PROVENANCE")
    REG.measured("digests", len(dig12), "published sha256-12 digests")
    REG.measured("registered_mutants", len(R["mutants"]), "len(R['mutants'])")
    gate("G-PROVENANCE",
         REG.stmt("everything this unit VOUCHES for is sealed, not only what "
                  "it measures: {digests} published digests, each well formed "
                  "and the pin's and the template's equal to the values the "
                  "pin froze; the reconstruction rule in words; and the "
                  "{registered_mutants} falsifier rows, each naming a "
                  "distinct recipe, a non-empty measured target and a gate "
                  "this run can reach", digests=1, registered_mutants=1),
         prov_ok and not bad_mut and names_unique,
         "digests %d mutants %d unreachable %s"
         % (len(dig12), len(R["mutants"]), bad_mut or "none"))

    reads.append(TEMPLATE_REL)
    if mut("MUT-READ"):
        with open(os.path.join(REPO, "v14/code/aid_output.txt"), "rb") as fh:
            fh.read()
    declared = sorted(set(reads))
    try:
        rev2, dprob = RS.gate_at_close(declared), None
    except ET.CheckFail as exc:
        rev2, dprob = {"distinct": 0, "reads": 0}, exc.detail
    R["read_set"] = {"declared": declared, "distinct": rev2["distinct"],
                     "reads": rev2["reads"]}
    SEAL.seal("read_set", R["read_set"], "G-READS-AT-THE-ACCESSOR")
    REG.measured("declared_reads", len(declared), "len(declared read set)")
    gate("G-READS-AT-THE-ACCESSOR",
         REG.stmt("every repository read is recorded at an open audit hook, "
                  "not at a helper, and the {declared_reads} declared paths "
                  "are reconciled with what was actually read, as a multiset, "
                  "at the last gate before promotion", declared_reads=1),
         dprob is None, "declared %d distinct %d %s"
         % (len(declared), rev2["distinct"], dprob or ""))
    RS.active = False

    if mut("MUT-TRANSCRIPT"):
        TR.say("  [PASS] G-A-GATE-THAT-NEVER-RAN :: forged")
    try:
        TR.bind(LD)
        tprob = None
    except ET.CheckFail as exc:
        tprob = exc.detail
    gate("G-TRANSCRIPT-BOUND",
         "every PASS line in the transcript that will be promoted is parsed "
         "back out of the finished text and reconciled with the ledger as a "
         "multiset, evidence included, and the ledger's own chain is "
         "recomputed from its rows",
         tprob is None and LD.recompute_chain() == LD.head,
         "rows %d chain %s %s" % (len(LD.rows), LD.head, tprob or ""))

    HARNESS = ET.FalsifierHarness(
        [ET.Falsifier(m[0], m[1], m[3], m[2], None) for m in MUTANTS])
    waivers = {"T-FALSIFIER-COVERAGE": "the coverage gate is inside its own "
                                       "denominator"}
    try:
        cov2 = HARNESS.coverage(LD, waivers, {"T-FALSIFIER-COVERAGE": True})
        fprob = None
    except ET.CheckFail as exc:
        cov2, fprob = {"gates": len(LD.rows) + 1, "falsified": 0,
                       "waived": len(waivers)}, exc.detail
    R["falsifiers"] = {"mutants": len(MUTANTS), "gates": cov2["gates"],
                       "falsified": cov2["falsified"],
                       "waived": cov2["waived"],
                       "targets": sorted({m[2] for m in MUTANTS})}
    SEAL.seal("falsifiers", R["falsifiers"], "T-FALSIFIER-COVERAGE")
    REG.measured("mutants", len(MUTANTS), "len(MUTANTS)")
    REG.measured("gates", cov2["gates"], "gates fired, this one included")
    gate("T-FALSIFIER-COVERAGE",
         REG.stmt("every gate that fired carries a falsifier naming the "
                  "measured key it must move, or a waiver with a "
                  "machine-checked forcing: {gates} gates, {mutants} "
                  "falsifiers", gates=1, mutants=1),
         fprob is None, "gates %d falsified %d waived %d %s"
         % (cov2["gates"], cov2["falsified"], cov2["waived"], fprob or ""))

    # the WHOLE transcript, both closing rows included, reconciled once more
    TR.bind(LD)
    R["transcript"] = {"sha256_12": ET.bytes_digest(TR.text().encode("utf-8")),
                       "lines": len(TR.lines), "gate_rows": len(LD.rows),
                       "chain_head": LD.head}
    SEAL.seal("transcript", R["transcript"], "G-TRANSCRIPT-BOUND")

    if mut("MUT-SEAL-ADD"):
        R["forged_finding"] = {"smuggled": len(LD.rows)}
    SEAL.verify_at_promotion(R, LD, "seal_manifest")

    if not write:
        return R, TR, LD, SEAL, None
    dig = ET.promote(SEAL, LD, R, TR.text(),
                     os.path.join(REPO, RECEIPT_REL),
                     os.path.join(REPO, OUTPUT_REL))
    return R, TR, LD, SEAL, dig


def k_parse_head(segment):
    """PARSE a rendered verdict segment back into integers.  This is the
    comparator's own route to the head: it reads the emitted string and knows
    nothing about how it was built."""
    out = {}
    body = segment[segment.index("<") + 1:segment.rindex(">")]
    for part in body.split(";"):
        if "=" not in part:
            continue
        k, v = part.split("=", 1)
        digits = re.findall(r"\d[\d,]*", v)
        if digits:
            out[k.strip()] = int(digits[0].replace(",", ""))
    return out


# ===========================================================================
# SECTION G.  THE FALSIFIERS, THE SELF-TEST AND THE CLI.
#   Every row names the MEASURED KEY its recipe must move; the harness digests
#   that key before and after and refuses a recipe that left it identical
#   (E-32), and refuses a death at any gate but the declared one.
# ===========================================================================

MUTANTS = (
    ("MUT-SOURCE-DRIFT", "G-SOURCES-PINNED", "sources",
     "one pinned digest is reversed, so a source no longer digests to the "
     "value the pin froze"),
    ("MUT-ARENA", "G-ARENA-CONSTRUCTED", "arena",
     "the carrier's cells-per-actor census is moved off the constructor's "
     "own count"),
    ("MUT-CORPUS", "G-CORPUS-SHAPE", "corpus",
     "the concatenation corpus is given a slot count that is not the square "
     "of the triple corpus's"),
    ("MUT-LEVEL0", "G-LEVEL-ZERO-INSUFFICIENT", "level_zero",
     "the count field is reported site-constant at fewer histories than the "
     "constructor finds"),
    ("MUT-STRIP-LEAK", "G-STRIPPING-TOTAL", "stripping",
     "the strip emits the actor triples instead of the cells they wrote, so "
     "the bare record carries site labels"),
    ("MUT-EQUIVARIANCE", "G-STRIPPING-EQUIVARIANT", "equivariance",
     "one relabelling trial is handed a constant map instead of a "
     "permutation, so the derived cast moves under it"),
    ("MUT-TAU", "G-CAST-DERIVED", "reconstruction",
     "one derived actor is dropped from the reconstructed cast before the "
     "comparator sees it"),
    ("MUT-CAST", "G-CAST-DERIVED", "reconstruction",
     "the comparator is handed a cast short of one actor"),
    ("MUT-LINK", "G-LINK-STRUCTURE-DERIVED", "link_structure",
     "one derived actor pair is deleted, so the derived link structure is no "
     "longer the declared one"),
    ("MUT-TARGETS", "G-RECONSTRUCTION-TARGETS-TOTAL", "anchors",
     "the pin's own list of reconstruction targets is read with one target "
     "removed"),
    ("MUT-MENU", "G-MENU-DERIVED", "menu",
     "one matched menu member is dropped, so the derived menu no longer "
     "accounts for every member it produced"),
    ("MUT-NAMING", "G-NAMING-RESIDUE", "naming",
     "the arena-coherent naming count is raised by one, so the residue index "
     "is no longer an integer"),
    ("MUT-S1", "G-S1-DISJOINT-CODE", "disjoint_code",
     "a reconstructor function is given a reference to an arena constant, so "
     "the reconstructor is no longer blind to the declared side"),
    ("MUT-SURPLUS", "G-SURPLUS-CENSUS", "surplus",
     "a property's surplus verdict is flipped from arena-forced to "
     "record-carried without its values moving"),
    ("MUT-PERHIST", "G-MINIMALITY-PER-HISTORY", "minimality_per_history",
     "one committed history is credited with reconstructing the cast at its "
     "first event"),
    ("MUT-CORPUS-DEPTH", "G-MINIMALITY-CORPUS", "minimality_corpus",
     "the corpus-order depth is moved one history later than the record "
     "reaches it"),
    ("MUT-BLOCK-MIN", "G-MINIMALITY-BLOCKS", "minimality_blocks",
     "a drop-one subset is credited with reconstructing, so a record block "
     "stops being load-bearing"),
    ("MUT-WSTAR", "G-WSTAR-REDERIVED", "wstar",
     "one collapse threshold is moved to a width the parent's paper does not "
     "carry"),
    ("MUT-CRYST", "G-CRYSTALLIZATION-REDERIVED", "crystallization",
     "one crystallization time is moved off the constant the parent's paper "
     "states"),
    ("MUT-PROVENANCE", "G-PROVENANCE", "provenance",
     "the pin's digest is reversed inside the unit's own published "
     "provenance, after every source gate has passed"),
    ("MUT-PARENTS", "G-PARENTS-AGREE", "parents",
     "a parent's delivered quantity is raised by one, so the parent's receipt "
     "and this unit's constructor no longer agree"),
    ("MUT-CONNECTION", "G-THE-CONNECTION", "connection",
     "one joint row is given a reached record-side depth"),
    ("MUT-OBSTRUCTION", "G-OBSTRUCTION-NAMED", "obstruction",
     "the count of events that wrote nothing is raised by one above the "
     "corpus's own arithmetic"),
    ("MUT-SCRAMBLE-CONTROL", "G-CONTROL-SCRAMBLED-FAILS", "control_scrambled",
     "a scrambled record is credited with reaching the declared cast"),
    ("MUT-SYNTHETIC", "G-CONTROL-SYNTHETIC-SUCCEEDS", "control_synthetic",
     "the balanced synthetic arms are marked unrecovered, so the "
     "reconstructor's own domain is misreported"),
    ("MUT-TEETH", "G-COMPARATOR-HAS-TEETH", "comparator_teeth",
     "the certified-but-refused list is emptied, so the comparator is left "
     "with nothing it ever refused"),
    ("MUT-HEAD", "G-VERDICT-EQUALITY", "verdict",
     "the head's qualifier is deleted, so the emitted word no longer carries "
     "the residue the measurement found"),
    ("MUT-PAPER-CLAIM", "G-PAPER-CLAIMS", "paper_claims",
     "a claim the paper does not carry is licensed"),
    ("MUT-REFERENT", "G-PAPER-REFERENTS", "paper_referents",
     "a corpus numeral is planted in a sentence about the cast"),
    ("MUT-WALL", "G-PAPER-WALLS", "walls",
     "the paper's own standing sentence is cut back to the unqualified form "
     "the wall forbids"),
    ("MUT-COVERAGE", "G-PAPER-COVERAGE", "paper_coverage",
     "a numeral backed by nothing is admitted to the paper's coverage census"),
    ("MUT-ANCHOR", "G-ANCHORS-LOCATED", "anchors",
     "a parent's anchored sentence is altered in the parent's own bytes, so "
     "the needle no longer occurs where the anchor says it does"),
    ("MUT-ANCHOR-CONSUMER", "G-ANCHORS-CONSUMED", "anchors",
     "an anchor's declared consumer is moved to a gate that ran but never "
     "subscripted it, so the anchor is located and then discarded"),
    ("MUT-TYPED", "G-NO-TYPED-COUNTS", "typed_counts",
     "a statement template that types a numeral is admitted"),
    ("MUT-READ", "G-READS-AT-THE-ACCESSOR", "read_set",
     "a repository file outside the declared read set is opened during the "
     "run"),
    ("MUT-TRANSCRIPT", "G-TRANSCRIPT-BOUND", "transcript",
     "a PASS line for a gate that never ran is appended to the transcript"),
    ("MUT-FLOAT", "G-RECEIPT-EXACT", "exactness",
     "a non-integer leaf is admitted to the published receipt"),
    ("MUT-SEAL-ADD", "T-SEAL-PROMOTION", "verdict",
     "a top-level receipt key is created after the seal manifest is taken"),
)

MUTANT_NAMES = tuple(m[0] for m in MUTANTS)


def clean_payload():
    R, _TR, _LD, _SEAL, _d = full_run(write=False)
    return R


def run_mutant(name, base=None):
    """E-32 at this unit's hands: the recipe must MOVE the measured key it
    names, and must die at the gate it names -- never earlier."""
    row = [m for m in MUTANTS if m[0] == name]
    if not row:
        raise SystemExit(2)
    _n, want_gate, target, _desc = row[0]
    base = base if base is not None else clean_payload()
    before = ET.digest(base.get(target))
    died, after = None, None
    try:
        R, _TR, _LD, _SEAL, _d = full_run(write=False, mutant=name)
        after = ET.digest(R.get(target))
    except ET.CheckFail as exc:
        died = exc.check
        after = "REFUSED-BEFORE-THE-KEY-WAS-PUBLISHED"
    used = name in MUTANT["used"]
    moved = (after != before)
    return {"mutant": name, "declared_gate": want_gate, "died_at": died,
            "target": target, "target_moved": bool(moved), "hook_used": used,
            "ok": died == want_gate and moved and used}


def main(argv):
    if len(argv) == 3 and argv[1] == "--mutant":
        if argv[2] not in MUTANT_NAMES:
            sys.stderr.write("unknown mutant: %r\n" % argv[2])
            return 2
        r = run_mutant(argv[2])
        print("MUTANT %s :: declared %s died %s target %s moved %s hook %s"
              % (r["mutant"], r["declared_gate"], r["died_at"], r["target"],
                 r["target_moved"], r["hook_used"]))
        return 0 if r["ok"] else 1
    if len(argv) != 2:
        sys.stderr.write(
            "usage: rec_exact.py --run|--no-write|--selftest|--list-gates"
            "|--list-mutants|--mutant NAME|--render\n")
        return 2
    mode = argv[1]
    if mode == "--list-mutants":
        for m in MUTANTS:
            print("%-24s %-34s %s" % (m[0], m[1], m[2]))
        return 0
    if mode == "--list-gates":
        _R, _TR, LD, _SEAL, _d = full_run(write=False)
        for g in LD.names():
            print(g)
        return 0
    if mode == "--render":
        R, _TR, _LD, _SEAL, _d = full_run(write=False, render=True)
        for t in R["rendered"]["tables"]:
            print(t)
            print()
        for c in R["rendered"]["claims"]:
            print("CLAIM :: " + c)
        print()
        for f in R["rendered"]["fences"]:
            print(f)
            print()
        return 0
    if mode == "--selftest":
        try:
            R, TR, LD, SEAL, _d = full_run(write=False)
        except ET.CheckFail as exc:
            print("SELFTEST: the clean run REFUSED at %s :: %s"
                  % (exc.check, exc.detail))
            return 1
        legs = []
        forged = TR.text().replace("[PASS] G-CAST-DERIVED",
                                   "[PASS] G-FORGED-GATE")
        try:
            TR.bind(LD, forged)
            print("SELFTEST: a forged transcript row SURVIVED")
            return 1
        except ET.CheckFail as exc:
            legs.append("forged transcript row dies at %s" % exc.check)
        R["forged_key"] = {"smuggled": len(LD.rows)}
        try:
            SEAL.verify_at_promotion(R, LD, "seal_manifest")
            print("SELFTEST: a post-seal add SURVIVED")
            return 1
        except ET.CheckFail as exc:
            legs.append("post-seal add dies at %s" % exc.check)
        del R["forged_key"]
        bent = dict(R["reconstruction"])
        bent["cast_size"] = bent["cast_size"] + 1
        try:
            SEAL.verify_at_promotion(
                dict(R, reconstruction=bent), LD, "seal_manifest")
            print("SELFTEST: a sealed edit SURVIVED")
            return 1
        except ET.CheckFail as exc:
            legs.append("sealed value edit dies at %s" % exc.check)
        for leg in legs:
            print("SELFTEST: %s" % leg)
        print("SELFTEST: clean run green over %d gates; nothing written"
              % len(LD.rows))
        return 0
    if mode in ("--run", "--no-write"):
        try:
            R, TR, LD, SEAL, dig = full_run(write=(mode == "--run"))
        except ET.CheckFail as exc:
            sys.stderr.write("REFUSED at %s :: %s\n" % (exc.check, exc.detail))
            return 1
        sys.stdout.write(TR.text())
        if mode == "--run":
            with open(os.path.join(REPO, OUTPUT_REL), "rb") as fh:
                on_disk = fh.read()
            if ET.bytes_digest(on_disk) != R["transcript"]["sha256_12"]:
                sys.stderr.write("REFUSED: promoted transcript bytes differ "
                                 "from the gate-time seal\n")
                return 1
            print("WROTE %s (%s) and %s (%s)"
                  % (RECEIPT_REL, dig["receipt"], OUTPUT_REL, dig["side"]))
        else:
            print("NO-WRITE: %d gates, nothing written" % len(LD.rows))
        return 0
    sys.stderr.write("unknown argument: %r\n" % mode)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
