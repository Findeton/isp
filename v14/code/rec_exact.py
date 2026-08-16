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
CELLS EACH DIVISION EVENT WROTE, with every actor label and every site label
erased and the cell indices moved by a declared coordinate.  The record count
field n_l(x) is measured too, as the level-0 arm, and is shown insufficient
rather than assumed so.

THE ERASER, DECLARED HONESTLY.  The declared coordinate is affine, k -> 5k+11
mod 27, and the cells are enumerated site-major and link-minor, so a cell's
index modulo three IS its declared direction and every affine map fixes that
residue: the three declared direction classes remain readable off the emitted
ids.  The eraser is therefore NOT ARENA-BLIND AS DECLARED.  The reconstruction
is ARENA-BLIND AS MEASURED, and that is a measurement rather than a promise:
the reconstructor does no arithmetic on token ids at all, and every quantity
this unit publishes is unchanged at 60 uniformly random coordinates, with the
derived cast relabelling and nothing else moving at 300 random (and
overwhelmingly non-affine) relabellings.  G-STRIPPING-COORDINATE-FREE prices
the channel the twelve affine trials cannot price.

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
from itertools import (combinations, combinations_with_replacement,
                       permutations, product)

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

# THE DECLARED COORDINATE.  It is a function of the token index and of nothing
# else, and it is AFFINE, which is exactly why it leaves one arena datum
# readable: the direction class survives as the token id's residue mod 3 (see
# the module docstring, R["residue_channel"] and G-STRIPPING-TOTAL's statement).
# It is kept for reproducibility and PRICED at G-STRIPPING-COORDINATE-FREE,
# where the whole reconstruction is re-run at uniformly random coordinates.
SCRAMBLE_MULT, SCRAMBLE_ADD = 5, 11

# The random coordinate census.  The generator is a declared integer LCG so
# that "uniformly random" is also byte-reproducible; no float is involved.
COORD_SEED = 20260816
COORD_TRIALS = 60
RELABEL_TRIALS = 300

# THE SWAP LEG'S DECLARED CAP.  It is a cap, it is named here, and every one
# of its witnesses is published at G-CONTROL-SCRAMBLED-FAILS: the pairs it
# visits, the moving corruptions it runs, and the moving corruptions it drops.
SWAP_CAP = 8

# The declared coordinates at which the control arm's own DENOMINATOR is
# recomputed, so that its coordinate-relativity is published rather than found.
SCRAMBLE_COORDINATES = ((1, 0), (2, 5), (4, 1), (5, 11), (7, 3), (8, 17),
                        (10, 2), (13, 25), (20, 7), (25, 26))

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
    """THE DECLARED COORDINATE: a relabelling of the token indices that is a
    function of the token index alone -- and affine, so it fixes the residue
    mod 3 that carries the declared direction.  Disclosed, not hidden."""
    return tuple((SCRAMBLE_MULT * k + SCRAMBLE_ADD) % DIM for k in range(DIM))


def s_lcg(seed):
    """A declared integer generator: exact, reproducible, no float."""
    s = seed
    while True:
        s = (6364136223846793005 * s + 1442695040888963407) % (2 ** 64)
        yield s >> 33


def s_random_permutation(gen, n):
    """A uniform draw from the FULL symmetric group on n letters -- the family
    the declared affine coordinate is a vanishing part of."""
    out = list(range(n))
    for i in range(n - 1, 0, -1):
        j = next(gen) % (i + 1)
        out[i], out[j] = out[j], out[i]
    return tuple(out)


def s_declared_relabelling(step):
    """the declared equivariance trials: multiplicative where the multiplier is
    a unit, a translation otherwise.  All twelve are AFFINE, which is exactly
    what G-STRIPPING-COORDINATE-FREE prices them for."""
    rho = tuple((step * 2 + 1) * k % DIM for k in range(DIM))
    if sorted(rho) != list(range(DIM)):
        rho = tuple((k + step) % DIM for k in range(DIM))
    return rho


def s_is_affine(rho):
    """is this coordinate of the form k -> a*k + b mod n?"""
    n = len(rho)
    for a in range(1, n):
        for b in range(n):
            if all(rho[k] == (a * k + b) % n for k in range(n)):
                return True
    return False


def s_direction_is_the_residue(coord):
    """THE LEAK, MEASURED.  Under this coordinate, is the declared direction a
    function of the emitted token id modulo three?  Under the declared affine
    map it is, exactly; under a random coordinate it is not."""
    seen = collections.defaultdict(set)
    for k, (_x, l) in enumerate(CELLS):
        seen[coord[k] % len(I7_LINKS)].add(I7_LINKS.index(l))
    return all(len(v) == 1 for v in seen.values())


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
    widths = {len(c) for _f, c in tf}
    if len(widths) != 1:
        return []
    width = widths.pop()
    if not width or want % width:
        return []
    need = want // width          # DERIVED: how many classes a splitting needs
    out = []
    for combo in combinations(range(len(tf)), need):
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


def k_factor_of(cast, tokens_of_one_class):
    """the partition of the cast induced by ONE class of tokens: two actors
    are together when the tokens they share all lie in the class."""
    want = set(tokens_of_one_class)
    n = len(cast)
    adj = collections.defaultdict(set)
    for i, j in combinations(range(n), 2):
        sh = set(cast[i]) & set(cast[j])
        if sh and sh <= want:
            adj[i].add(j)
            adj[j].add(i)
    seen, out = set(), []
    for i in range(n):
        if i in seen:
            continue
        blk = tuple(sorted({i} | adj[i]))
        seen |= set(blk)
        out.append(blk)
    return tuple(sorted(out))


def k_declared_splitting(derived_cast, declared_cast, direction_classes):
    """THE DECLARED SPLITTING, expressed in the derived cast's own indices --
    so that it can be looked for among the record's own resolutions."""
    if not k_agree_sets(derived_cast, declared_cast):
        return None
    return tuple(sorted(k_factor_of(derived_cast, c)
                        for c in direction_classes))


def k_orbit_of(derived_cast, declared_cast, isos, splitting):
    """the ORBIT of a splitting under the admissible namings.  Transitivity is
    what makes the residue index a COUNT of the splittings rather than a
    number that happens to equal one."""
    if splitting is None:
        return []
    imap = k_index_map(derived_cast, declared_cast)
    if imap is None:
        return []
    inv = {v: k for k, v in imap.items()}
    out = set()
    for s in isos:
        rel = {i: inv[s[i]] for i in range(len(derived_cast))}
        out.add(tuple(sorted(
            tuple(sorted(tuple(sorted(rel[a] for a in blk)) for blk in fac))
            for fac in splitting)))
    return sorted(out)


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
PARTIAL: dict = {"R": None}


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

# The walls are written from the FINDING and not from a phrase list.  Each
# pattern below carries its verb, tense and number families and admits either
# order of subject and object, because eleven natural re-voicings of a
# delivered finding walked through the delivered blacklist (K3 MAJOR-1).
_BE = r"(?:is|was|are|were|has been|have been|can be|could be|gets|get)"
_DERIVE = (r"(?:derived|reconstructed|recovered|read off|readable|"
           r"determined|fixed|forced)")
_SUBJ = (r"(?:cast|actors|actor set|arena|theory|coordinate|coordinates|"
         r"direction|directions|direction class|direction classes|naming|"
         r"namings|declaration|residue)")

WALL_DERIVED = ET.SemanticWall(
    "W-NO-UNQUALIFIED-DERIVATION",
    negative=[
        # the whole thing derived, without the qualifier or the corpus scope
        r"the (?:whole |entire |full )?%s %s (?:fully |wholly |completely |in "
        r"full )?%s(?![\w\s]{0,24}up to)(?![\w\s]{0,40}at the corpus)"
        % (_SUBJ, _BE, _DERIVE),
        r"the (?:whole |entire |full )?%s (?:was |is |were |are )?%s in full"
        % (_SUBJ, _DERIVE),
        # nothing left to declare, in any voicing
        r"nothing (?:at all |whatever |else |more )?(?:is |remains |stays |"
        r"needs to be |need be |has to be )?(?:declared|left to declare)",
        r"no (?:declaration|residue|freedom|choice|coordinate|direction)s? "
        r"(?:remains?|is left|are left|survives?|is needed|are needed|is "
        r"required)",
        r"(?:leaves|leaving|with) no (?:residue|declaration|freedom|choice)",
        r"no declaration is (?:needed|required|left)",
        # the record fixing what it does not fix
        r"(?:the )?(?:bare )?record (?:alone |by itself |itself )?"
        r"(?:fixes|determines|forces|names|recovers|supplies|gives|hands "
        r"back|carries) the (?:coordinate|coordinates|direction|directions|"
        r"direction class|direction classes|declaration|naming)",
        r"the (?:coordinate|direction classes|directions) (?:comes?|come) "
        r"back",
        # per-history reconstruction, either order
        r"reconstruct\w*\s+(?:\w+\s+){0,4}from (?:a|one|any) single history",
        r"(?:a|one|any) single history (?:\w+\s+){0,3}(?:suffices|is enough|"
        r"is sufficient|recovers|reconstructs|determines|fixes)",
        r"(?:every |each )?actors? (?:can be|is|are|could be) (?:read off|"
        r"derived from|recovered from) (?:one|a single|any) history",
        r"(?:the cast|the actors) (?:can be |is |are )?(?:derived|recovered|"
        r"read off)(?:\w|\s){0,20}from (?:one|a single) history",
        # the count field doing what it cannot
        r"(?:the )?counts?(?: field| alone| by themselves| themselves)?\s+"
        r"(?:\w+\s+){0,4}(?:suffices|suffice|is enough|are enough|recovers? "
        r"the cast|determines? the cast|names? the cast)",
        # the methodological inversion of the second section
        r"isomorphism, not set equality",
        r"(?:merely |only )?isomorphic(?:\s+\w+){0,3}, not (?:the same sets|"
        r"set equality|equal)",
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
        r"epr[\w']*(?:\s+\w+){0,4}\s+(?:proved|showed|established|makes|made|"
        r"shows|renders)(?:\s+\w+){0,4}\s+(?:completeness|a complete "
        r"description)",
        r"(?:makes?|made|renders?|leaves?|left) the (?:bare )?record "
        r"(?:a |the )?complete",
        r"(?:the record|the bare record) is complete(?:\b|[^\w-])",
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

# The lookbehind admits a leading HYPHEN, so the hyphenated verdict blocks are
# inside the census rather than outside it (K3 MINOR-6: 50 of 194 digit tokens
# were skipped, 18 of them inside the fences).
NUM = re.compile(r"(?<![\w.,/])(\d[\d,]*)(?![\w/])")
FENCE_RE = re.compile(r"```[^\n]*\n(.*?)```", re.S)

# The spelled census (K2 m5, K3 MINOR-5): load-bearing counts written as words
# were outside every gate.  The vocabulary is declared and its values are
# checked against the same backing set the digits are.
SPELLED = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
    "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11,
    "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15,
    "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19,
    "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60,
    "seventy": 70, "eighty": 80, "ninety": 90, "hundred": 100,
    "thousand": 1000,
}
SPELLED_RE = re.compile(r"(?<![\w-])(%s)(?![\w-])"
                        % "|".join(sorted(SPELLED, key=len, reverse=True)),
                        re.I)


def paper_numerals(text):
    return [m.group(1).replace(",", "") for m in NUM.finditer(text)]


def paper_spelled(text):
    """every number WORD in the paper, as the integer it denotes."""
    return [SPELLED[m.group(1).casefold()] for m in SPELLED_RE.finditer(text)]


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


REGION_PREFIX = (("b_", "builder"), ("r_", "reconstructor"),
                 ("k_", "comparator"), ("s_", "stripper"))
# The reconstructor's own typing rule speaks of pairs and triples; constants at
# or below this value are declared structural and are not read as smuggled
# arena cardinalities.  Every larger arena cardinality is banned outright.
STRUCTURAL_CONSTANT = 3


def region_of(name):
    """TOTAL by construction: every function is in exactly one region, and the
    orchestrator is named rather than left out of the census (K1 MAJ-6: 35 of
    78 functions were in no region at all, `full_run` among them)."""
    for pre, tag in REGION_PREFIX:
        if name.startswith(pre):
            return tag
    return "plumbing"


def module_arena_names(src):
    """THE ARENA SET, DERIVED.  Every module-level binding made before the
    first stripper function is declared-side; the hand-typed blacklist this
    replaces had drifted in both directions (two live builder constants
    missing, two dead names listed)."""
    tree = ast.parse(src)
    floor = min([n.lineno for n in tree.body
                 if isinstance(n, ast.FunctionDef) and n.name.startswith("s_")]
                or [10 ** 9])
    out = set()
    for n in tree.body:
        if n.lineno >= floor:
            continue
        for tgt in (n.targets if isinstance(n, ast.Assign)
                    else [n.target] if isinstance(n, ast.AnnAssign) else []):
            for sub in ast.walk(tgt):
                if isinstance(sub, ast.Name):
                    out.add(sub.id)
    return out


def module_call_graph(src):
    """function -> the module-level function names its body reaches directly,
    with module-level ALIASES resolved (`_A = b_declared_actors` then
    `r_x(): return _A()` is a call to the builder)."""
    tree = ast.parse(src)
    fns = {n.name: n for n in tree.body if isinstance(n, ast.FunctionDef)}
    alias = {}
    for n in tree.body:
        if isinstance(n, ast.Assign) and isinstance(n.value, ast.Name) \
                and n.value.id in fns:
            for tgt in n.targets:
                if isinstance(tgt, ast.Name):
                    alias[tgt.id] = n.value.id
    graph = {}
    for name, node in fns.items():
        seen = set()
        for sub in ast.walk(node):
            if isinstance(sub, ast.Name):
                nm = alias.get(sub.id, sub.id)
                if nm in fns and nm != name:
                    seen.add(nm)
        graph[name] = seen
    return fns, graph, alias


def audit_regions(src, cardinalities=()):
    """S-1, STRUCTURALLY.  A reconstructor or comparator function may not name
    an arena constant, may not type an arena cardinality, and may not REACH --
    at any depth, through aliases and through helpers -- a builder, a stripper
    or the orchestrator.  Names alone were four leaks wide (K3 MAJOR-6)."""
    fns, graph, alias = module_call_graph(src)
    arena = module_arena_names(src)
    cards = {int(c) for c in cardinalities if int(c) > STRUCTURAL_CONSTANT}
    bad = []
    for name in sorted(fns):
        tagged = region_of(name)
        if tagged not in ("reconstructor", "comparator"):
            continue
        forbidden = {"builder", "stripper", "plumbing",
                     "comparator" if tagged == "reconstructor"
                     else "reconstructor"}
        # (i) named arena constants and typed arena cardinalities
        for sub in ast.walk(fns[name]):
            if isinstance(sub, ast.Name) and sub.id in arena:
                bad.append("%s %s names the arena constant %s"
                           % (tagged, name, sub.id))
            if isinstance(sub, ast.Attribute) and sub.attr in arena:
                bad.append("%s %s names %s" % (tagged, name, sub.attr))
            if isinstance(sub, ast.Constant) and isinstance(sub.value, int) \
                    and not isinstance(sub.value, bool) and sub.value in cards:
                bad.append("%s %s types the arena cardinality %d"
                           % (tagged, name, sub.value))
        # (ii) the CALL CLOSURE, aliases resolved
        seen, stack = set(), sorted(graph[name])
        while stack:
            nxt = stack.pop()
            if nxt in seen:
                continue
            seen.add(nxt)
            stack.extend(sorted(graph.get(nxt, ())))
        for reached in sorted(seen):
            if region_of(reached) in forbidden:
                how = "calls" if reached in graph[name] else "reaches"
                bad.append("%s %s %s the %s function %s"
                           % (tagged, name, how, region_of(reached), reached))
    for a, tgt in sorted(alias.items()):
        if region_of(a) in ("reconstructor", "comparator") \
                and region_of(tgt) not in (region_of(a), "plumbing"):
            bad.append("%s is an alias of the %s function %s"
                       % (a, region_of(tgt), tgt))
    return sorted(set(bad))


def region_census(src):
    """TOTAL: every top-level function definition lands in exactly one region,
    the orchestrator included, and the census sums to the module's own count."""
    tree = ast.parse(src)
    out = collections.Counter()
    for n in tree.body:
        if isinstance(n, ast.FunctionDef):
            out[region_of(n.name)] += 1
    return dict(sorted(out.items()))


def audit_typed_calls(src, callers):
    """The concatenation dodge and the table cells, closed (K3 MAJOR-10): every
    string constant ANYWHERE in the subtree of a call to a statement, claim,
    table or fence builder is scanned, not only the direct arguments."""
    tree = ast.parse(src)
    out = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        fname = getattr(node.func, "attr", None) or getattr(node.func, "id", None)
        if fname not in callers:
            continue
        for sub in ast.walk(node):
            if isinstance(sub, ast.Constant) and isinstance(sub.value, str) \
                    and re.search(r"(?<![\w])\d+(?![\w])", sub.value):
                out.append("line %d: %r" % (node.lineno, sub.value[:56]))
    return sorted(set(out))


EVNUM = re.compile(r"(?<![\w.,/])(\d[\d,]*)(?![\w/])")


def _ints_of(o, into):
    if isinstance(o, bool):
        return
    if isinstance(o, int):
        into.add(o)
    elif isinstance(o, dict):
        for k, v in o.items():
            for m in EVNUM.finditer(str(k)):
                into.add(int(m.group(1).replace(",", "")))
            _ints_of(v, into)
    elif isinstance(o, (list, tuple)):
        for v in o:
            _ints_of(v, into)
    elif isinstance(o, str):
        for m in EVNUM.finditer(o):
            into.add(int(m.group(1).replace(",", "")))


def evidence_offences(rows, seals, payload):
    """THE TRANSCRIPT'S OWN NUMBERS, BOUND (K3 MAJOR-9).  The rendered evidence
    and the receipt are two renderings of one measurement and nothing compared
    them: a forged evidence numeral shipped in both artifacts, contradicting
    the receipt on the unit's own census, at exit 0.  Every integer in every
    finished evidence line must be a value the gate's own sealed keys carry, or
    one its own statement already published."""
    at_gate: dict = collections.defaultdict(set)
    for key, s in seals.items():
        if key in payload:
            _ints_of(payload[key], at_gate[s["gate"]])
    out = []
    for row in rows:
        allowed = set(at_gate.get(row["gate"], set()))
        for m in EVNUM.finditer(row["statement"]):
            allowed.add(int(m.group(1).replace(",", "")))
        for m in EVNUM.finditer(row["evidence"]):
            v = int(m.group(1).replace(",", ""))
            if v not in allowed:
                out.append("%s: %d" % (row["gate"], v))
    return sorted(set(out))


def audit_mut_hooks(src, declared):
    """A falsifier row with no implementation, and an implementation with no
    row, both die (K3 MAJOR-3): the set of string constants handed to mut() is
    compared with the declared recipe names, in BOTH directions."""
    tree = ast.parse(src)
    hooks = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and getattr(node.func, "id", "") == "mut":
            for arg in node.args:
                if isinstance(arg, ast.Constant) and isinstance(arg.value, str):
                    hooks.add(arg.value)
    return (sorted(set(declared) - hooks), sorted(hooks - set(declared)))


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

# The balance probe's declared domain: every complete multipartite shape with
# parts of size 2..6, between 2 and 6 parts, and at most this many actors.
BALANCE_CEILING = 16


def balance_shapes():
    out = []
    for nparts in range(2, 7):
        for shape in combinations_with_replacement(range(2, 7), nparts):
            if sum(shape) <= BALANCE_CEILING:
                out.append(tuple(shape))
    return sorted(out)


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


def full_run(write=False, mutant=None, render=False, mode="--run"):
    MUTANT["name"], MUTANT["used"] = mutant, set()
    reads: list[str] = []
    RS = ET.ReadSet(REPO)
    RS.install()
    RS.active = True

    LD, TR, SEAL = ET.Ledger(), ET.Transcript(), ET.Seal()
    REG, CL, RR = ET.CountRegistry(), ET.Claims(), ET.ReferentRegistry()
    R: dict = {}
    # THE PAYLOAD AS IT STOOD AT REFUSAL.  E-32's move-proof is worthless if
    # `after` is a constant string: every falsifier dies at a gate, so the
    # comparison must be made against what the run had actually published when
    # the gate refused (K3 MAJOR-2).
    PARTIAL["R"] = R

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
        # the digest itself is reversed and the finding is RECOMPUTED from it,
        # so the real predicate runs rather than a constant being appended to
        # the offender list (K3 MAJOR-5's shape, removed here)
        shas[PIN_REL] = shas[PIN_REL][::-1]
        drifted = [k for k in sorted(shas) if shas[k] != SOURCES[k]]
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
    # require_object BEFORE the read, so its absent-object leg is reachable
    # (K3 MINOR-8), and with the mode that actually ran (K3 MINOR-9).
    paper_path = os.path.join(REPO, PAPER_REL)
    if not os.path.isfile(paper_path):
        # the absent-object leg, reachable at last -- and a directory in the
        # paper's place is an absent object too, rather than a traceback
        ET.require_object(mode, paper_path if os.path.exists(paper_path)
                          else None, None)
    paper = read_text(PAPER_REL)
    reads.append(PAPER_REL)
    ET.require_object(mode, paper_path, paper)
    # the anchor rows are copied per run: a recipe that moves a consumer must
    # not poison the next run in the same process (K3 MINOR-13).
    ASET = ET.AnchorSet([ET.Anchor(a.name, a.needle, a.source, a.consumer)
                         for a in ANCHORS])
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
    R["anchors_located"] = {"rows": len(ANCHORS), "problem": lprob or "none",
                            "sources": sorted({a.source for a in ANCHORS})}
    SEAL.seal("anchors_located", R["anchors_located"], "G-ANCHORS-LOCATED")
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
    # token was which cell, and this is where that bookkeeping is spent -- here
    # and at the declared direction classes below, and nowhere else.
    dec_cast = [tuple(sorted(pi[k] for k in dec_actors[i])) for i in range(NACT)]
    bare = s_bare_corpus(corp, pi)
    if mut("MUT-STRIP-LEAK"):
        bare = [tuple(tuple(sorted(F)) for F in H) for (_t, H) in corp]
    typebad = []
    s_type_walk(bare, typebad)
    blocks = sorted({b for h in bare for b in h})
    written = sum(len(h) for h in bare)
    alphabet = sorted({t for b in blocks for t in b})
    moved_tokens = sum(1 for k in range(DIM) if pi[k] != k)
    R["stripping"] = {
        "scramble_is_a_permutation": sorted(pi) == list(range(DIM)),
        "scramble_moves_tokens": moved_tokens,
        "token_alphabet": len(alphabet),
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
    REG.measured("alphabet", len(alphabet), "distinct token ids emitted")
    REG.measured("moved_tokens", moved_tokens, "token ids the coordinate moves")
    SEAL.seal("stripping", R["stripping"], "G-STRIPPING-TOTAL")
    # THE GATE STATES WHAT IT CHECKS AND NOTHING WIDER (K3 MINOR-1/2, K2 M3):
    # types, depth, alphabet and non-triviality.  It does NOT say "no
    # direction" -- the residue channel below says why it may not.
    gate("G-STRIPPING-TOTAL",
         REG.stmt("the bare record is three levels deep and integers at the "
                  "bottom -- histories, events, token ids -- over an alphabet "
                  "of {alphabet} ids, so no actor and no site (a PAIR of "
                  "integers) survives the strip, and the coordinate is a "
                  "non-trivial permutation moving {moved_tokens} of them; the "
                  "corpus writes {written} events into {blocks} distinct "
                  "record blocks and writes nothing at {unwritten}",
                  written=1, blocks=1, unwritten=1, alphabet=1,
                  moved_tokens=1),
         not typebad and sorted(pi) == list(range(DIM))
         and len(alphabet) == DIM and moved_tokens > 0
         and {n for n, _c in R["stripping"]["block_sizes"]} == {len(I7_LINKS)},
         "non-integer leaves %s alphabet %d moved %d blocks %d written %d "
         "unwritten %d"
         % (sorted(set(typebad)) or "none", len(alphabet), moved_tokens,
            len(blocks), written, R["corpus"]["events"] - written))

    # -- equivariance: the scramble is immaterial ---------------------------
    trials, eqbad = [], []
    for step in range(1, 13):
        rho = s_declared_relabelling(step)
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
                  "{eq_failures} failures; these trials are AFFINE and price "
                  "the affine family only -- the coordinate itself is priced "
                  "at G-STRIPPING-COORDINATE-FREE", eq_trials=1,
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
    # MUT-CAST used to sit here, poisoning this local flag; it named the
    # reconstruction as its target and never moved it, and it was in any case
    # MUT-TAU with a different name (K3 MAJOR-2, MINOR-15).  MUT-TAU drops an
    # actor from the sealed cast itself and is the honest form.
    cast_exact = k_agree_sets(rec["cast"], dec_cast)
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
        "matched": matched, "matched_count": len(matched),
        "stray_block_counts": stray, "unmatched": missing,
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
    # WHY THE INDEX COUNTS WHAT IT COUNTS (K1's second free strengthening).
    # The admissible namings act on the splittings; the orbit of the DECLARED
    # splitting is measured, and it is all of them -- the action is transitive,
    # which is why index = count rather than a coincidence.
    declared_split = k_declared_splitting(rec["cast"], dec_cast, dir_tokens)
    orbit = k_orbit_of(rec["cast"], dec_cast, isos, declared_split)
    if mut("MUT-ORBIT"):
        orbit = orbit[:-1]
    R["naming"] = {
        "admissible_namings": n_iso, "arena_coherent_namings": n_coh,
        "arena_automorphisms": len(aut),
        "residue_index": [idx.numerator, idx.denominator],
        "direction_candidates": len(facs), "resolutions": len(reso),
        "declared_splitting_is_a_resolution":
            bool(declared_split is not None and declared_split in set(reso)),
        "orbit_of_the_declared_splitting": len(orbit),
        "orbit_is_every_resolution": bool(set(orbit) == set(reso)),
    }
    REG.measured("isos", n_iso, "len(k_isomorphisms)")
    REG.measured("coherent", n_coh, "namings carrying the direction classes")
    REG.measured("residue", idx.numerator, "isos / coherent, exact")
    REG.measured("resolutions", len(reso), "direction decompositions")
    REG.measured("factors", len(facs), "candidate direction classes")
    REG.measured("orbit", len(orbit),
                 "the orbit of the declared splitting under the namings")
    SEAL.seal("naming", R["naming"], "G-NAMING-RESIDUE")
    gate("G-NAMING-RESIDUE",
         REG.stmt("the naming is forced only up to the derived structure's own "
                  "symmetry: {isos} bijections of the derived cast onto the "
                  "declared one carry the link structure across, {coherent} "
                  "of them also carry the declared direction classes, and the "
                  "residue is the index {residue}; the record admits "
                  "{resolutions} ways of splitting its {factors} candidate "
                  "direction classes into a declaration and names none of "
                  "them -- and the index IS that count rather than merely "
                  "equalling it, because the {isos} namings carry the declared "
                  "splitting onto {orbit} splittings, which is every one of "
                  "them", isos=1, coherent=1, residue=1, resolutions=1,
                  factors=1, orbit=1),
         idx.denominator == 1 and n_coh == len(aut)
         and len(reso) == idx.numerator
         and R["naming"]["declared_splitting_is_a_resolution"]
         and R["naming"]["orbit_is_every_resolution"]
         and len(orbit) == idx.numerator,
         "isos %d coherent %d automorphisms %d index %s resolutions %d orbit %d"
         % (n_iso, n_coh, len(aut), idx, len(reso), len(orbit)))

    # -- THE ERASER, PRICED WHERE THE AFFINE TRIALS CANNOT PRICE IT ---------
    # The declared coordinate is affine and the cells are enumerated site-major
    # and link-minor, so a cell index modulo three IS its declared direction
    # and every affine map fixes that residue: the direction survives the strip
    # as the emitted id's residue class.  The eraser is NOT ARENA-BLIND AS
    # DECLARED.  What is measured here is the other half: the reconstruction is
    # ARENA-BLIND AS MEASURED -- the reconstructor does no arithmetic on token
    # ids, and every published quantity is unchanged at coordinates drawn from
    # the FULL symmetric group, where the channel is not there to read.
    res_classes = {frozenset(t for t in range(DIM) if t % len(I7_LINKS) == c)
                   for c in range(len(I7_LINKS))}
    leak_declared = s_direction_is_the_residue(pi)
    leak_is_exact = {frozenset(c) for c in dir_tokens} == res_classes
    affine_leaks = sum(1 for st in range(1, 13)
                       for rho in [s_declared_relabelling(st)]
                       if s_direction_is_the_residue(
                           tuple(rho[pi[k]] for k in range(DIM))))
    baseline = (why, rec.get("tau"), tuple(rec.get("meets", [])),
                len(rec["cast"]), True, tuple(rec["clique_sizes"]),
                len(rec["tokens"]), n_iso, n_coh, tuple(matched), len(reso),
                len({tuple(h) for h in bare}))
    gen = s_lcg(COORD_SEED)
    coord_dev, coord_leaks, coord_nonaffine = [], 0, 0
    for trial in range(COORD_TRIALS):
        rho = s_random_permutation(gen, DIM)
        coord = tuple(rho[pi[k]] for k in range(DIM))
        if s_direction_is_the_residue(coord):
            coord_leaks += 1
        if not s_is_affine(coord):
            coord_nonaffine += 1
        bl2 = sorted({tuple(sorted(rho[t] for t in b)) for b in blocks})
        dc2 = [tuple(sorted(rho[t] for t in c)) for c in dec_cast]
        dt2 = [tuple(sorted(rho[t] for t in c)) for c in dir_tokens]
        r2 = r_reconstruct([frozenset(b) for b in bl2])
        c2, w2 = r_certify(r2)
        im2 = k_index_map(r2["cast"], dc2)
        got = (w2, r2.get("tau"), tuple(r2.get("meets", [])), len(r2["cast"]),
               bool(c2 and k_agree_sets(r2["cast"], dc2)),
               tuple(r2["clique_sizes"]), len(r2["tokens"]),
               len(k_isomorphisms(r2["cast"], dc2, r2["tokens"])),
               len(k_coherent(k_isomorphisms(dc2, dc2, r2["tokens"]), dc2,
                              r2["tokens"], dt2)),
               tuple(k_menu_agreement(r_derived_menu(r2), dec_menu, im2)[0]),
               len(r_resolutions(r2)),
               len({tuple(tuple(sorted(rho[t] for t in b)) for b in h)
                    for h in bare}))
        if got != baseline:
            coord_dev.append(trial)
    rel_bad, rel_nonaffine = [], 0
    basecast = sorted(tuple(sorted(c)) for c in rec["cast"])
    for trial in range(RELABEL_TRIALS):
        rho = s_random_permutation(gen, DIM)
        if not s_is_affine(rho):
            rel_nonaffine += 1
        rm = r_reconstruct([frozenset(rho[t] for t in b) for b in blocks])
        inv = [0] * DIM
        for i, p in enumerate(rho):
            inv[p] = i
        back = sorted(tuple(sorted(inv[t] for t in c)) for c in rm["cast"]) \
            if rm["ok"] else []
        if back != basecast:
            rel_bad.append(trial)
    if mut("MUT-COORDINATE"):
        coord_dev = coord_dev + [-1]
    R["residue_channel"] = {
        "declared_multiplier": SCRAMBLE_MULT, "declared_offset": SCRAMBLE_ADD,
        "declared_map_is_affine": bool(s_is_affine(pi)),
        "direction_is_the_token_residue": bool(leak_declared),
        "declared_classes_are_the_residue_classes": bool(leak_is_exact),
        "affine_trials": len(trials), "affine_trials_leaking": affine_leaks,
        "random_coordinates": COORD_TRIALS,
        "random_coordinates_non_affine": coord_nonaffine,
        "random_coordinates_leaking": coord_leaks,
        "quantities_compared_per_coordinate": len(baseline),
        "coordinates_that_moved_a_quantity": len(coord_dev),
        "random_relabellings": RELABEL_TRIALS,
        "random_relabellings_non_affine": rel_nonaffine,
        "relabellings_whose_cast_moved": len(rel_bad),
    }
    REG.measured("coords", COORD_TRIALS, "uniformly random coordinates")
    REG.measured("coord_quantities", len(baseline),
                 "published quantities compared at each coordinate")
    REG.measured("coord_moved", len(coord_dev), "coordinates that moved one")
    REG.measured("relabels", RELABEL_TRIALS, "uniformly random relabellings")
    REG.measured("relabel_bad", len(rel_bad), "relabellings whose cast moved")
    REG.measured("affine_leaking", affine_leaks,
                 "affine trials at which the direction is the residue")
    REG.measured("coord_leaking", coord_leaks,
                 "random coordinates at which it is")
    SEAL.seal("residue_channel", R["residue_channel"],
              "G-STRIPPING-COORDINATE-FREE")
    gate("G-STRIPPING-COORDINATE-FREE",
         REG.stmt("the declared coordinate is affine and LEAKS the direction "
                  "as the token id's residue -- at {affine_leaking} of the "
                  "{eq_trials} affine trials, every one of which fixes it -- "
                  "so the blindness is not the declaration's: it is measured "
                  "instead, at {coords} coordinates drawn from the full "
                  "symmetric group, where the channel is present at "
                  "{coord_leaking} and each of {coord_quantities} published "
                  "quantities moves at {coord_moved}, and at {relabels} random "
                  "relabellings at which the derived cast relabels and nothing "
                  "else moves, {relabel_bad} failing",
                  affine_leaking=1, eq_trials=1, coords=1, coord_leaking=1,
                  coord_quantities=1, coord_moved=1, relabels=1,
                  relabel_bad=1),
         leak_declared and leak_is_exact and affine_leaks == len(trials)
         and not coord_dev and not rel_bad and coord_leaks == 0
         and coord_nonaffine == COORD_TRIALS,
         "affine-leaking %d of %d random-leaking %d of %d moved %d relabel "
         "failures %d" % (affine_leaks, len(trials), coord_leaks,
                          COORD_TRIALS, len(coord_dev), len(rel_bad)))

    R["reconstruction_targets"] = {
        "declared": ["site set", "link structure", "cast size",
                     "partition menu", "naming"],
        "found_in_the_pin": sorted(w for w in
                                   ("site set", "link structure", "cast size",
                                    "partition menu", "naming")
                                   if w in a_pin.casefold()),
    }
    SEAL.seal("reconstruction_targets", R["reconstruction_targets"],
              "G-RECONSTRUCTION-TARGETS-TOTAL")
    REG.measured("targets_declared",
                 len(R["reconstruction_targets"]["declared"]),
                 "the pin's reconstruction targets")
    REG.measured("targets_found",
                 len(R["reconstruction_targets"]["found_in_the_pin"]),
                 "targets located in the pin's own bytes")
    gate("G-RECONSTRUCTION-TARGETS-TOTAL",
         REG.stmt("the pin's {targets_declared} reconstruction targets are "
                  "each answered by their own gate and the pin's own list is "
                  "read back to check that none is quietly dropped: "
                  "{targets_found} are found in the pin's bytes",
                  targets_declared=1, targets_found=1),
         (R["reconstruction_targets"]["found_in_the_pin"]
          == sorted(R["reconstruction_targets"]["declared"])),
         "targets %d of %d"
         % (len(R["reconstruction_targets"]["found_in_the_pin"]),
            len(R["reconstruction_targets"]["declared"])))

    # -- S-1: the regions are disjoint --------------------------------------
    src = read_text(SELF_REL)
    reads.append(SELF_REL)
    if mut("MUT-S1"):
        # a reconstructor function that reaches for a declared-side constant
        src = src + "\n\ndef r_leaks_the_arena():\n    return CELLS\n"
    cards = {NACT, DIM, len(I7_LINKS), len(CLASS_NAMES), 2 * DIM // NACT,
             NACT * (NACT - 1), len(pairs)}
    s1 = audit_regions(src, cards)
    floats = audit_no_floats(src)
    regions = region_census(src)
    arena_names = module_arena_names(src)
    defs = sum(1 for n in ast.parse(src).body
               if isinstance(n, ast.FunctionDef))
    R["disjoint_code"] = {
        "violations": s1, "regions": regions, "float_offences": floats,
        "top_level_functions": defs,
        "arena_names_derived": len(arena_names),
        "banned_cardinalities": sorted(c for c in cards
                                       if c > STRUCTURAL_CONSTANT),
        "structural_constant_floor": STRUCTURAL_CONSTANT,
    }
    REG.measured("recon_fns", regions.get("reconstructor", 0),
                 "reconstructor functions")
    REG.measured("comp_fns", regions.get("comparator", 0),
                 "comparator functions")
    REG.measured("build_fns", regions.get("builder", 0), "builder functions")
    REG.measured("plumb_fns", regions.get("plumbing", 0),
                 "orchestrator and plumbing functions")
    REG.measured("strip_fns", regions.get("stripper", 0), "stripper functions")
    REG.measured("all_fns", defs, "top-level function definitions")
    REG.measured("arena_names", len(arena_names),
                 "declared-side names derived from the module")
    SEAL.seal("disjoint_code", R["disjoint_code"], "G-S1-DISJOINT-CODE")
    gate("G-S1-DISJOINT-CODE",
         REG.stmt("the region map is TOTAL -- {all_fns} top-level functions, "
                  "{build_fns} builder, {strip_fns} stripper, {recon_fns} "
                  "reconstructor, {comp_fns} comparator and {plumb_fns} "
                  "plumbing, the orchestrator among the last -- and no "
                  "reconstructor or comparator function names any of the "
                  "{arena_names} declared-side names derived from this module, "
                  "types an arena cardinality, or REACHES a builder, a "
                  "stripper or the orchestrator at any depth, through an alias "
                  "or through a helper",
                  all_fns=1, build_fns=1, strip_fns=1, recon_fns=1, comp_fns=1,
                  plumb_fns=1, arena_names=1),
         not s1 and not floats and sum(regions.values()) == defs,
         "violations %s floats %s regions %s of %d"
         % (s1 or "none", floats or "none", sum(regions.values()), defs))

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
        # THE MULTISET, and it is named as one: division events repeat (C2
        # concatenates, W4-CLASS quadruples repeat classes), so the sorted
        # tuple keeps duplicates.  The SET is measured beside it below.
        return tuple(sorted(tuple(sorted(SITE_INDEX[x] for x in F))
                            for F in corp[i][1]))

    def prop_eventset_as_a_set(i):
        return tuple(sorted({tuple(sorted(SITE_INDEX[x] for x in F))
                             for F in corp[i][1]}))

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
        ("THE-EVENT-MULTISET", prop_eventset),
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
    # THE SET, BESIDE THE MULTISET (K1 MAJ-3).  The published row measures the
    # sorted multiset of events; the set of them is a coarser reading, and it
    # is computed here so the row's name and its number denote the same object
    # and the reader can see both.  The verdict is invariant under the choice.
    set_vals = [prop_eventset_as_a_set(i) for i in range(len(corp))]
    set_distinct = len({repr(v) for v in set_vals})
    set_splits = sum(1 for idx in fiber.values()
                     if len({repr(set_vals[i]) for i in idx}) > 1)
    ms_row = [p for p in prows if p["property"] == "THE-EVENT-MULTISET"][0]
    R["surplus"] = {
        "the_event_set_beside_the_multiset": {
            "multiset_distinct_values": ms_row["distinct_values"],
            "multiset_fibers_that_split": ms_row["fibers_that_split"],
            "set_distinct_values": set_distinct,
            "set_fibers_that_split": set_splits,
            "verdict_is_the_same": ms_row["verdict"]
            == ("NOT-CARRIED" if set_splits else "RECORD-CARRIED"),
        },
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
    REG.measured("eventset_values", set_distinct,
                 "distinct event SETS over the corpus")
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
                  "{collided_histories} histories; the event row measures the "
                  "MULTISET of a history's events and is named as one, and the "
                  "SET of them, {eventset_values} over the corpus, is measured "
                  "beside it and carries the same verdict",
                  arena_forced=1, record_carried=1, not_carried=1,
                  distinct_histories=1, bare_records=1, lost=1, collisions=1,
                  collided_histories=1, eventset_values=1),
         not unbound and af + rc + nc == len(PROPS) and nc > 0 and rc > 0
         and af > 0 and R["surplus"]["histories_lost"] > 0
         and R["surplus"]["the_event_set_beside_the_multiset"]
                        ["verdict_is_the_same"],
         "forced %d carried %d not-carried %d bare %d lost %d event-sets %d "
         "unbound %s"
         % (af, rc, nc, len(fiber), R["surplus"]["histories_lost"],
            set_distinct, unbound or "none"))

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
    refusal = collections.Counter()
    seen_blocks = collections.Counter()
    disjoint_hist = 0
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
        # THE MECHANISM, MEASURED (K1 MAJ-1 = K2 M1).  Why each history
        # refuses, and how much of the record it ever sees.
        bl = sorted({tuple(sorted(b)) for b in h})
        seen_blocks[len(bl)] += 1
        if not any(set(a) & set(b) for a, b in combinations(bl, 2)):
            disjoint_hist += 1
        rr = r_reconstruct([frozenset(b) for b in h])
        _cc, wy = r_certify(rr)
        refusal[wy] += 1
    max_blocks = max(seen_blocks) if seen_blocks else 0
    if mut("MUT-MECHANISM"):
        max_blocks = len(blocks)
    R["minimality_per_history"] = {
        "slots": len(corp), "reconstructing_at_some_prefix": depth_hits,
        "by_corpus": {("%s:%s" % (k[0], k[1])): v
                      for k, v in sorted(per_hist.items(),
                                         key=lambda kv: (kv[0][0],
                                                         -1 if kv[0][1] is None
                                                         else kv[0][1]))},
        "refusal_words": dict(sorted(refusal.items())),
        "most_blocks_one_history_writes": max_blocks,
        "record_blocks_in_all": len(blocks),
        "histories_with_pairwise_disjoint_blocks": disjoint_hist,
    }
    REG.measured("per_history_hits", depth_hits,
                 "histories reconstructing at some prefix")
    REG.measured("max_blocks", max_blocks,
                 "the most distinct blocks any one history writes")
    REG.measured("disjoint_hist", disjoint_hist,
                 "histories whose record blocks are pairwise disjoint")
    REG.measured("no_meet", refusal.get("NO-MEET-GAP", 0),
                 "histories refusing for want of a meet")
    REG.measured("no_actor", refusal.get("TOKEN-IN-NO-ACTOR", 0),
                 "histories refusing for want of blocks")
    SEAL.seal("minimality_per_history", R["minimality_per_history"],
              "G-MINIMALITY-PER-HISTORY")
    gate("G-MINIMALITY-PER-HISTORY",
         REG.stmt("no committed history reconstructs the cast at any prefix "
                  "of its own record: {per_history_hits} of {slots}, the "
                  "prefix taken at every depth from one event to the whole "
                  "history; the most distinct record blocks any one of them "
                  "writes is {max_blocks} of the {blocks}, and the refusal is "
                  "modally a want of blocks ({no_actor} histories) rather than "
                  "a want of overlap ({no_meet}, the pairwise-disjoint "
                  "mechanism, at {disjoint_hist} histories whose blocks are "
                  "disjoint)", per_history_hits=1, slots=1, max_blocks=1,
                  blocks=1, no_actor=1, no_meet=1, disjoint_hist=1),
         depth_hits == 0 and max_blocks < len(blocks)
         and sum(refusal.values()) == len(corp),
         "reconstructing histories %d of %d most-blocks %d refusals %s"
         % (depth_hits, len(corp), max_blocks,
            dict(sorted(refusal.items()))))

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
    drop2 = [(u, v) for u, v in combinations(range(len(blocks)), 2)]
    drop2_ok = sum(1 for u, v in drop2
                   if decide([b for k, b in enumerate(blocks)
                              if k not in (u, v)]))
    if mut("MUT-BLOCK-MIN"):
        drop_ok = 1
    if mut("MUT-BLOCKS-25"):
        drop2_ok = 1
    R["minimality_blocks"] = {"blocks": len(blocks), "drop_one_subsets":
                              len(blocks), "still_reconstructing": drop_ok,
                              "drop_two_subsets": len(drop2),
                              "still_reconstructing_at_two_fewer": drop2_ok}
    REG.measured("drop_ok", drop_ok, "26-block subsets that reconstruct")
    REG.measured("drop2", len(drop2), "25-block subsets")
    REG.measured("drop2_ok", drop2_ok, "25-block subsets that reconstruct")
    SEAL.seal("minimality_blocks", R["minimality_blocks"],
              "G-MINIMALITY-BLOCKS")
    gate("G-MINIMALITY-BLOCKS",
         REG.stmt("every one of the {blocks} record blocks is load-bearing: "
                  "of the {blocks} subsets got by dropping one, "
                  "{drop_ok} reconstruct, and of the {drop2} got by dropping "
                  "two, {drop2_ok} do", blocks=1, drop_ok=1, drop2=1,
                  drop2_ok=1),
         drop_ok == 0 and drop2_ok == 0 and decide(blocks),
         "drop-one survivors %d of %d drop-two survivors %d of %d"
         % (drop_ok, len(blocks), drop2_ok, len(drop2)))

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
    # THE ONE EXACT RELATION THE CORPUS CARRIES BETWEEN THE TWO PARENT DEPTHS
    # (K1's first free strengthening): never-crystallizing IFF w* is the least
    # width the corpus carries, measured in both directions.
    least_w = min(w for w in wstar if w is not None)
    never_set = {i for i, c in enumerate(cryst) if c is None}
    least_set = {i for i, w in enumerate(wstar) if w == least_w}
    if mut("MUT-BICONDITIONAL"):
        never_set = never_set | {max(set(range(len(corp))) - never_set)}
    bicond = {
        "never_crystallizing": len(never_set),
        "least_collapse_threshold": least_w,
        "at_the_least_threshold": len(least_set),
        "in_both": len(never_set & least_set),
        "never_but_not_least": len(never_set - least_set),
        "least_but_not_never": len(least_set - never_set),
        "biconditional": never_set == least_set,
    }
    R["connection"] = {
        "rows": [{"crystallization": k[0], "collapse_threshold": k[1],
                  "reconstruction_depth": k[2], "histories": v}
                 for k, v in sorted(joint.items())],
        "declared_side_finite": sum(v for k, v in joint.items() if k[1] is not None),
        "record_side_reached": depth_hits,
        "the_biconditional": bicond,
    }
    SEAL.seal("connection", R["connection"], "G-THE-CONNECTION")
    REG.measured("joint_rows", len(joint), "distinct joint rows")
    REG.measured("both_depths", len(never_set & least_set),
                 "histories that never crystallize AND take the least width")
    REG.measured("least_w", least_w, "the least collapse threshold")
    gate("G-THE-CONNECTION",
         REG.stmt("the three depths are put in one table, {joint_rows} rows "
                  "of it: both declared-side thresholds are finite at every "
                  "history that has one, and the record-side depth is reached "
                  "at {per_history_hits}, so the reconstruction depth is not "
                  "the collapse threshold and is not the crystallization "
                  "time; and the two declared-side depths carry one exact "
                  "relation -- a history never crystallizes exactly when its "
                  "collapse threshold is {least_w}, at {both_depths} of "
                  "{both_depths} in each direction",
                  joint_rows=1, per_history_hits=1, least_w=1, both_depths=1),
         all(k[2] == "NEVER" for k in joint) and depth_hits == 0
         and bicond["biconditional"],
         "rows %d declared-finite %d record-reached %d biconditional %s at %d"
         % (len(joint), R["connection"]["declared_side_finite"], depth_hits,
            bicond["biconditional"], len(never_set & least_set)))

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
        "name": "THE-DIRECTION-DECLARATION",
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
         REG.stmt("the datum that resists is THE DIRECTION DECLARATION -- the "
                  "choice of three of the four parallel classes as the links, "
                  "which is the one name this unit gives it -- and it "
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
    certified_scr, reached_comparator = 0, 0
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
            # the comparator is consulted only on a CERTIFIED reconstruction,
            # so how often it was consulted at all is COUNTED, not inferred
            # from arithmetic on another leg (K2 M2).
            certified_scr += bool(cc)
            if cc:
                reached_comparator += 1
                agree = k_agree_sets(rr["cast"], dec_cast)
            else:
                agree = False
            scr_rows[("REPLACE", bool(agree))] += 1
            scr.append(agree)
    for j in range(len(base)):
        bl = [b for k, b in enumerate(base) if k != j]
        rr = r_reconstruct([frozenset(x) for x in bl])
        cc, wy = r_certify(rr)
        certified_scr += bool(cc)
        if cc:
            reached_comparator += 1
            agree = k_agree_sets(rr["cast"], dec_cast)
        else:
            agree = False
        scr_rows[("DROP", bool(agree))] += 1
        scr.append(agree)
    # THE SWAP ARM CARRIES A DECLARED CAP, and it is published with its
    # witnesses (K1 MAJ-4, K3 MAJOR-11): how many pairs the cap visits, how
    # many of those the moving-filter drops, and how many moving swaps the
    # uncapped arm would hold.
    swap_candidates = swap_visited = 0
    for u, v in combinations(range(len(base)), 2):
        capped = u > SWAP_CAP
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
        swap_candidates += 1                 # a MOVING swap, capped or not
        if capped:
            continue
        swap_visited += 1
        rr = r_reconstruct([frozenset(x) for x in bl])
        cc, wy = r_certify(rr)
        certified_scr += bool(cc)
        if cc:
            reached_comparator += 1
            agree = k_agree_sets(rr["cast"], dec_cast)
        else:
            agree = False
        scr_rows[("SWAP", bool(agree))] += 1
        scr.append(agree)
    pairs_visited = sum(1 for u, _v in combinations(range(len(base)), 2)
                        if u <= SWAP_CAP)
    survivors = sum(1 for s in scr if s)
    if mut("MUT-SCRAMBLE-CONTROL"):
        survivors = 0 if survivors else 1
    # THE DENOMINATOR IS COORDINATE-RELATIVE, and the range is published rather
    # than left to be discovered (K3 MAJOR-11, RUNBOOK Sec.15).
    coord_totals = {}
    for m, a in SCRAMBLE_COORDINATES:
        p = tuple((m * k + a) % DIM for k in range(DIM))
        if sorted(p) != list(range(DIM)):
            continue
        bb = sorted({b for h in s_bare_corpus(corp, p) for b in h})
        n_rep = sum(1 for j in range(len(bb)) for sh in (1, 2)
                    if len({(t + sh) % DIM for t in bb[j]}) >= 3
                    and tuple(sorted({(t + sh) % DIM for t in bb[j]})) not in bb)
        n_swap = 0
        for u, v in combinations(range(len(bb)), 2):
            if u > SWAP_CAP:
                continue
            x, y = list(bb[u]), list(bb[v])
            if x[0] == y[0]:
                continue
            x[0], y[0] = y[0], x[0]
            if len(set(x)) < 3 or len(set(y)) < 3:
                continue
            cand = list(bb)
            cand[u], cand[v] = tuple(sorted(x)), tuple(sorted(y))
            if sorted(cand) == sorted(bb):
                continue
            n_swap += 1
        coord_totals["%d,%d" % (m, a)] = n_rep + len(bb) + n_swap
    R["control_scrambled"] = {
        "trials": len(scr), "survivors": survivors,
        "certified_at_all": certified_scr,
        "reached_the_comparator": reached_comparator,
        "by_shape": {"%s:%s" % k: v for k, v in sorted(scr_rows.items())},
        "candidates": 2 * len(base) + len(base) + pairs_visited,
        "rejected_as_non_moving":
            2 * len(base) + len(base) + pairs_visited - len(scr),
        "swap_cap": SWAP_CAP,
        "swap_pairs_available": len(list(combinations(range(len(base)), 2))),
        "swap_pairs_visited_under_the_cap": pairs_visited,
        "swap_moving_corruptions_uncapped": swap_candidates,
        "swap_moving_corruptions_run": swap_visited,
        "swap_moving_corruptions_dropped_by_the_cap":
            swap_candidates - swap_visited,
        "alien_family": ["the two token-index translates of the block"],
        "trials_by_coordinate": dict(sorted(coord_totals.items())),
        "trials_range": [min(coord_totals.values()), max(coord_totals.values())],
    }
    REG.measured("scr_trials", len(scr), "scrambled records tried")
    REG.measured("scr_survivors", survivors, "scrambles the comparator passed")
    REG.measured("scr_certified", certified_scr,
                 "scrambled records the reconstructor certified at all")
    REG.measured("swap_run", swap_visited, "moving swaps run under the cap")
    REG.measured("swap_uncapped", swap_candidates,
                 "moving swaps the uncapped arm would hold")
    REG.measured("swap_dropped", swap_candidates - swap_visited,
                 "moving swaps the cap drops")
    REG.measured("scr_candidates", 2 * len(base) + len(base) + pairs_visited,
                 "corruptions built before the moving-filter")
    REG.measured("scr_rejected",
                 2 * len(base) + len(base) + pairs_visited - len(scr),
                 "corruptions the moving-filter rejected")
    REG.measured("coord_lo", min(coord_totals.values()), "the least total")
    REG.measured("coord_hi", max(coord_totals.values()), "the largest total")
    REG.measured("coord_count", len(coord_totals), "coordinates recomputed")
    SEAL.seal("control_scrambled", R["control_scrambled"],
              "G-CONTROL-SCRAMBLED-FAILS")
    gate("G-CONTROL-SCRAMBLED-FAILS",
         REG.stmt("the control arm the pin asks for, run through the REAL "
                  "reconstructor: {scr_trials} scrambled records, of which "
                  "{scr_survivors} reach the declared cast and {scr_certified} "
                  "are certified at all; {scr_candidates} corruptions were "
                  "built and {scr_rejected} rejected for leaving the record "
                  "unmoved; the swap leg carries a DECLARED cap "
                  "under which {swap_run} of the {swap_uncapped} moving swaps "
                  "are run and {swap_dropped} are dropped; and the total is "
                  "coordinate-relative, running from {coord_lo} to {coord_hi} "
                  "over {coord_count} declared coordinates",
                  scr_trials=1, scr_survivors=1, scr_certified=1, swap_run=1,
                  swap_uncapped=1, swap_dropped=1, coord_lo=1, coord_hi=1,
                  coord_count=1, scr_candidates=1, scr_rejected=1),
         survivors == 0 and certified_scr == 0 and len(scr) > len(base)
         and swap_visited + (swap_candidates - swap_visited) == swap_candidates
         and R["control_scrambled"]["candidates"] - len(scr)
         == R["control_scrambled"]["rejected_as_non_moving"],
         "trials %d survivors %d certified %d swaps %d of %d range %d-%d"
         % (len(scr), survivors, certified_scr, swap_visited, swap_candidates,
            min(coord_totals.values()), max(coord_totals.values())))

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
                         "cast_size": len(rr["cast"]),
                         # the SAME clause reads a DIFFERENT threshold on each
                         # arm: the cleanest evidence that tau is read off the
                         # record rather than typed into it (K2's mandate 2)
                         "threshold": rr.get("tau"),
                         "meet_values": rr.get("meets", [])})
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

    # THE BALANCE PROBE.  The delivered seven arms locate the boundary badly:
    # it is BALANCE and not three-ness (K1 MAJ-2).  Every complete multipartite
    # shape up to the declared ceiling is run through the same reconstructor.
    bal_rows, bal_bad = [], []
    for pshape in balance_shapes():
        sb, sstars, ntok = synthetic_record(pshape)
        rr = r_reconstruct(sb)
        cc, wy = r_certify(rr)
        own = bool(cc and k_agree_sets(rr["cast"], sstars))
        if cc and not own:
            bal_bad.append(pshape)
        bal_rows.append({"parts": list(pshape), "balanced":
                         len(set(pshape)) == 1, "tokens": ntok,
                         "blocks": len(sb), "certificate": wy,
                         "cast_size": len(rr["cast"]),
                         "cast_recovered": own})
    if mut("MUT-BALANCE"):
        # an UNBALANCED shape credited with its cast: the boundary the sweep
        # locates stops being balance, which is what the gate asserts
        for r in bal_rows:
            if not r["balanced"]:
                r["cast_recovered"] = not r["cast_recovered"]
                break
    bal_ok = [r for r in bal_rows if r["cast_recovered"]]
    bal_unbalanced_ok = [r for r in bal_ok if not r["balanced"]]
    bal_balanced_no = [r for r in bal_rows
                       if r["balanced"] and not r["cast_recovered"]]
    R["control_balance"] = {
        "shapes": len(bal_rows), "balanced_shapes":
            sum(1 for r in bal_rows if r["balanced"]),
        "recovered": len(bal_ok),
        "recovered_unbalanced": len(bal_unbalanced_ok),
        "balanced_but_refused": [r["parts"] for r in bal_balanced_no],
        "certified_but_wrong": [list(p) for p in bal_bad],
        "ceiling_actors": BALANCE_CEILING,
        "rows": bal_rows,
    }
    REG.measured("bal_shapes", len(bal_rows), "multipartite shapes swept")
    REG.measured("bal_ok", len(bal_ok), "shapes whose cast comes back")
    REG.measured("bal_unbal", len(bal_unbalanced_ok),
                 "UNBALANCED shapes whose cast comes back")
    REG.measured("bal_wrong", len(bal_bad),
                 "shapes certified for a cast that was not the record's own")
    REG.measured("bal_refused", len(bal_balanced_no),
                 "balanced shapes the reconstructor refuses")
    SEAL.seal("control_balance", R["control_balance"], "G-CONTROL-BALANCE")
    gate("G-CONTROL-BALANCE",
         REG.stmt("the boundary of the reconstructor's domain is BALANCE and "
                  "not the number of parts: of {bal_shapes} complete "
                  "multipartite shapes swept, {bal_ok} recover their cast "
                  "exactly and {bal_unbal} of those are unbalanced; "
                  "{bal_refused} balanced shapes are refused rather than "
                  "answered wrongly; and {bal_wrong} shapes anywhere in the "
                  "sweep were certified for a cast that was not that record's "
                  "own", bal_shapes=1, bal_ok=1, bal_unbal=1, bal_refused=1,
                  bal_wrong=1),
         not bal_bad and len(bal_unbalanced_ok) == 0 and len(bal_ok) > 0
         and all(r["balanced"] for r in bal_ok),
         "shapes %d recovered %d unbalanced-recovered %d certified-wrong %s"
         % (len(bal_rows), len(bal_ok), len(bal_unbalanced_ok),
            bal_bad or "none"))

    # THE COMPARATOR'S OWN TEETH, MEASURED BY RUNNING IT (K2 M2, K3 MAJOR-8).
    # The delivered leg inferred the count from a CARDINALITY (cast_size != 9)
    # and never asked the comparator, which silently dropped the one arm whose
    # refusal is not decidable by size: the 3+3+3 arena carries a cast of
    # exactly nine that is not this arena's nine.
    certified_syn = [r for r in syn_rows if r["certificate"] == "CERTIFIED"]
    teeth, teeth_rows = [], []
    for r, pshape in zip(syn_rows, SYNTHETIC_PARTS):
        if r["certificate"] != "CERTIFIED":
            continue
        sb, _ss, _nt = synthetic_record(pshape)
        rr = r_reconstruct(sb)
        agrees = k_agree_sets(rr["cast"], dec_cast)
        if mut("MUT-TEETH") and r["cast_size"] == NACT:
            # the one arm whose refusal is not decidable by size is flipped:
            # the guard survives (three teeth remain) and the MEASUREMENT is
            # what moves (K2 m7)
            agrees = not agrees
        teeth_rows.append({"parts": list(pshape), "cast_size": r["cast_size"],
                           "size_alone_decides": r["cast_size"] != NACT,
                           "the_comparator_agrees": bool(agrees)})
        if not agrees:
            teeth.append(r)
    size_blind = [t for t in teeth_rows if not t["size_alone_decides"]]
    R["comparator_teeth"] = {
        "certified_reconstructions_refused": len(teeth),
        "certified_reconstructions_tried": len(certified_syn),
        "refusals_not_decidable_by_size":
            sum(1 for t in size_blind if not t["the_comparator_agrees"]),
        "rows": teeth_rows,
        "reconstructor_refusals_per_history": len(corp) - depth_hits,
        "reconstructor_refusals_on_scrambles": len(scr) - survivors,
        "scrambles_that_reached_the_comparator": reached_comparator,
        "history_attempts_that_reached_the_comparator": 0,
    }
    REG.measured("teeth", len(teeth),
                 "certified reconstructions the comparator refused")
    REG.measured("teeth_tried", len(certified_syn),
                 "certified reconstructions the comparator was asked about")
    REG.measured("teeth_blind", len(size_blind),
                 "of those whose cast size alone cannot decide")
    REG.measured("scr_reached", reached_comparator,
                 "scrambled records that reached the comparator")
    SEAL.seal("comparator_teeth", R["comparator_teeth"],
              "G-COMPARATOR-HAS-TEETH")
    gate("G-COMPARATOR-HAS-TEETH",
         REG.stmt("the comparator can fail and does, and it is ASKED rather "
                  "than inferred from a cardinality: of the {teeth_tried} "
                  "synthetic reconstructions carrying the reconstructor's own "
                  "certificate it refuses {teeth}, and {teeth_blind} of those "
                  "carry a cast of the declared size, so that refusal is not a "
                  "matter of size; everywhere else the RECONSTRUCTOR refuses "
                  "first -- {scr_reached} of the {scr_trials} scrambles and "
                  "none of the {slots} per-history attempts ever reach the "
                  "comparator at all",
                  teeth=1, teeth_tried=1, teeth_blind=1, scr_reached=1,
                  scr_trials=1, slots=1),
         len(teeth) == len(certified_syn) and len(teeth) > 0
         and len(size_blind) > 0
         and all(not t["the_comparator_agrees"] for t in teeth_rows),
         "certified-but-refused %d of %d size-blind %d reached-on-scrambles %d"
         % (len(teeth), len(certified_syn), len(size_blind),
            reached_comparator))

    # -- THE OUTCOME WORDS, WRITTEN AT DECLARED FAULTS (#299) ---------------
    # A pre-registered outcome that only a refused run could print is not a
    # deliverable outcome (K2 M4).  Each word is therefore produced HERE by the
    # real machinery -- the real reconstructor, the real certificate, the real
    # comparator -- reading a faulted object, and the word it writes is
    # recorded.  Two faults are on the RECORD side (a synthetic arena's own
    # bytes); one is on the DECLARED side, and it has to be, because at this
    # arena the declared pairs are a function of the declared stars: a cast
    # that is set-equal cannot carry a link structure that is not, so the
    # OBSTRUCTED word is unreachable from any record whatever.  That is itself
    # a measured fact, and it is published as one.
    reach_rows = []

    def reach(tag, side, blocks_in, declared_cast_in, declared_pairs_in,
              menu_missing, residue):
        rr = r_reconstruct([frozenset(b) for b in blocks_in])
        cc, wy = r_certify(rr)
        exact = bool(cc and k_agree_sets(rr["cast"], declared_cast_in))
        im = k_index_map(rr["cast"], declared_cast_in)
        dp = {tuple(sorted(im[i] for i in
                           tuple(j for j, c in enumerate(rr["cast"]) if t in c)))
              for t in rr["tokens"]} if im else set()
        word = head_word_of(exact, dp == declared_pairs_in,
                            len(rr["cast"]) == len(declared_cast_in),
                            menu_missing, residue)
        reach_rows.append({"fault": tag, "faulted_side": side,
                           "certificate": wy, "cast_size": len(rr["cast"]),
                           "word": word})
        return word

    syn_b3, syn_s3, _n3 = synthetic_record((3, 3, 3))
    syn_b234, syn_s234, _n4 = synthetic_record((2, 3, 4))
    syn_p3 = {tuple(sorted(i for i, c in enumerate(syn_s3) if t in c))
              for t in range(_n3)}
    syn_p234 = {tuple(sorted(i for i, c in enumerate(syn_s234) if t in c))
                for t in range(_n4)}
    reach("none: this corpus's own record against its own declared arena",
          "NEITHER", blocks, dec_cast, dec_pairs, len(missing), idx.numerator)
    reach("a synthetic arena's own record, read against its own cast, which "
          "declares no direction and so owes no residue",
          "RECORD", syn_b3, syn_s3, syn_p3, 0, 1)
    reach("a synthetic arena whose record leaves a token in no actor",
          "RECORD", syn_b234, syn_s234, syn_p234, 0, 1)
    reach("this corpus's record, read against a cast short of one actor",
          "RECORD", blocks, dec_cast[:-1], dec_pairs, 0, 1)
    reach("this corpus's record, read against a declared link structure "
          "missing one pair", "DECLARED", blocks, dec_cast,
          set(sorted(dec_pairs)[:-1]), len(missing), idx.numerator)
    got_words = sorted({r["word"] for r in reach_rows})
    if mut("MUT-REACHABILITY"):
        reach_rows = reach_rows[:1]
        got_words = sorted({r["word"] for r in reach_rows})
    R["outcome_reachability"] = {
        "rows": reach_rows, "distinct_words": got_words,
        "pre_registered": sorted({head_word_of(True, True, True, 0, 1),
                                  head_word_of(True, True, True, 1, 12),
                                  head_word_of(False, True, True, 0, 1),
                                  head_word_of(True, False, True, 0, 1)}),
    }
    SEAL.seal("outcome_reachability", R["outcome_reachability"],
              "G-OUTCOMES-REACHABLE")
    REG.measured("reach_rows", len(reach_rows), "declared faults run")
    REG.measured("reach_words", len(got_words), "distinct words they wrote")
    gate("G-OUTCOMES-REACHABLE",
         REG.stmt("every pre-registered outcome is DELIVERABLE and not merely "
                  "a value of a function: {reach_rows} declared faults are put "
                  "through the real reconstructor, the real certificate and "
                  "the real comparator, and the words they write are "
                  "{reach_words}, which is every word the pin registered",
                  reach_rows=1, reach_words=1),
         got_words == R["outcome_reachability"]["pre_registered"],
         "faults %d words %s" % (len(reach_rows), got_words))

    # -- THE VERDICT, derived --------------------------------------------
    derived_word = head_word_of(cast_exact, der_pairs == dec_pairs,
                                len(rec["cast"]) == NACT, len(missing),
                                idx.numerator)
    head = [
        "REC-RECONSTRUCTION<CORPUS=%s; DISTINCT-HISTORIES=%s; "
        "RECORD-BLOCKS=%s; SITE-SET=%s-OF-%s-EXACT; LINK-STRUCTURE=%s-OF-%s-"
        "EXACT; CAST-SIZE=%s-DERIVED; MENU=%s-OF-%s-PARTIAL; NAMING=%s-"
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
        "DIRECTION-DECLARATION; UNWRITTEN-EVENTS=%s; PARTLY-UNWRITTEN-HISTORIES=%s;"
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

    # EVERY NUMERAL POSITION IN THE HEAD IS BOUND TO A RECEIPT LEAF, in order:
    # the head is the artifact quoted standing alone, and a numeral in it that
    # no leaf answers for is a free number (K3 MAJOR-7).
    HEAD_FIELDS = (
        (0, "CORPUS", (("corpus", "slots"),)),
        (0, "DISTINCT-HISTORIES", (("corpus", "distinct_histories"),)),
        (0, "RECORD-BLOCKS", (("stripping", "record_blocks"),)),
        (0, "SITE-SET", (("reconstruction", "cast_size"), ("arena", "sites"))),
        (0, "LINK-STRUCTURE", (("link_structure", "derived_pairs"),
                               ("arena", "cells"))),
        (0, "CAST-SIZE", (("reconstruction", "cast_size"),)),
        (0, "MENU", (("menu", "matched_count"), ("menu", "declared_members"))),
        (0, "NAMING", (("naming", "admissible_namings"),
                       ("naming", "arena_coherent_namings"))),
        (0, "RESIDUE-INDEX", (("naming", "residue_index", 0),)),
        (0, "LEVEL-0-COUNT-FIELD", (("level_zero", "distinct_record_fields"),)),
        (1, "PER-HISTORY", (("minimality_per_history",
                             "reconstructing_at_some_prefix"),
                            ("minimality_per_history", "slots"))),
        (1, "CORPUS-ORDER", (("minimality_corpus", "histories"),
                             ("minimality_corpus", "events"))),
        (1, "BLOCK-MINIMAL", (("minimality_blocks", "blocks"),
                              ("minimality_blocks", "drop_one_subsets"),
                              ("minimality_blocks", "still_reconstructing"))),
        (1, "COLLAPSE-THRESHOLDS", (("wstar", "values", 0),
                                    ("wstar", "values", 1),
                                    ("wstar", "values", 2))),
        (1, "CRYSTALLIZATION-ON-C1-AND-C2", (("crystallization",
                                              "C1_C2_constant", 0),)),
        (1, "NEVER-CRYSTALLIZING", (("crystallization", "never"),)),
        (2, "UNWRITTEN-EVENTS", (("obstruction", "unwritten_events"),)),
        (2, "PARTLY-UNWRITTEN-HISTORIES",
         (("obstruction", "histories_with_an_unwritten_event"),)),
        (2, "HISTORIES-WRITING-NOTHING",
         (("obstruction", "histories_writing_nothing"),)),
        (2, "RECORD-COLLISIONS", (("surplus", "collision_classes"),
                                  ("surplus",
                                   "distinct_histories_in_collisions"))),
        (2, "SURPLUS", (("surplus", "arena_forced"),
                        ("surplus", "record_carried"),
                        ("surplus", "not_carried"))),
        (2, "CONTROLS", (("control_scrambled", "trials"),
                         ("control_scrambled", "survivors"),
                         ("control_synthetic", "recovered"),
                         ("control_synthetic", "arms"))),
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
    head_numerals = 0
    for seg, key, paths in HEAD_FIELDS:
        got = k_parse_head(head[seg]).get(key)
        want = []
        for path in paths:
            leaf = R
            for step in path:
                leaf = leaf[step]
            want.append(leaf)
        head_numerals += len(want)
        if got is None or got != want:
            parsed_bad.append("%s: head %s receipt %s" % (key, got, want))
    seen_numerals = sum(len(v) for seg in range(len(head))
                        for v in k_parse_head(head[seg]).values())
    if seen_numerals != head_numerals:
        parsed_bad.append("the head carries %d numerals and %d are bound"
                          % (seen_numerals, head_numerals))
    SEAL.seal("verdict", R["verdict"], "G-VERDICT-EQUALITY")
    REG.measured("head_fields", len(HEAD_FIELDS), "len(HEAD_FIELDS)")
    REG.measured("head_numerals", head_numerals, "head numerals bound to a leaf")
    gate("G-VERDICT-EQUALITY",
         REG.stmt("the verdict is not trusted to its own renderer: each of "
                  "{head_fields} declared head fields is PARSED back out of "
                  "the emitted string and compared, as integers, with the "
                  "receipt leaves it names -- a parser against a builder, "
                  "sharing no code and no literal -- at {head_numerals} "
                  "numeral positions, which is EVERY numeral the three "
                  "segments carry; and the verdict WORD is "
                  "bound both ways to the measurement that owes it, with the "
                  "pre-registered outcomes shown distinguishable on declared "
                  "probes", head_fields=1, head_numerals=1),
         not parsed_bad, "fields %d numerals %d of %d outcomes %d mismatched %s"
         % (len(HEAD_FIELDS), head_numerals, seen_numerals, len(set(probes)),
            parsed_bad or "none"))

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
        "T-SURPLUS", ("property of the history", "verdict", "distinct values"),
        [(p["property"], p["verdict"], com(p["distinct_values"]))
         for p in prows])
    cconst = c1c2[0]
    wc1 = [w for w in w_vals if w_by[("C1", w)]][0]
    c3c = ", ".join("%s:%s" % ("never" if k < 0 else k, com(v))
                    for k, v in sorted(c3, key=lambda kv: (kv[0] < 0, kv[0])))
    t_depth = CL.table(
        "T-DEPTHS", ("depth", "object it measures", "C1", "C2", "C3"),
        [("crystallization time", "the naming, given the cast",
          com(c_by[("C1", cconst)]) + " at " + str(cconst),
          com(c_by[("C2", cconst)]) + " at " + str(cconst), c3c),
         ("collapse threshold", "coherence width, given the cast",
          com(w_by[("C1", wc1)]) + " at " + str(wc1),
          com(w_by[("C2", wc1)]) + " at " + str(wc1),
          ", ".join(str(w) for w in w_vals)),
         ("reconstruction depth", "the cast itself", "never", "never",
          "never")])
    t_syn = CL.table(
        "T-SYNTHETIC", ("parts", "tokens", "blocks", "threshold",
                        "certificate", "derived cast", "cast recovered"),
        [("+".join(str(x) for x in r["parts"]), com(r["tokens"]),
          com(r["blocks"]),
          "none" if r["threshold"] is None else com(r["threshold"]),
          r["certificate"], com(r["cast_size"]),
          "yes" if r["cast_recovered"] else "no") for r in syn_rows])
    t_bal = CL.table(
        "T-BALANCE", ("parts", "balanced", "blocks", "certificate",
                      "cast recovered"),
        [("+".join(str(x) for x in r["parts"]),
          "yes" if r["balanced"] else "no", com(r["blocks"]),
          r["certificate"], "yes" if r["cast_recovered"] else "no")
         for r in bal_rows if r["balanced"] and len(r["parts"]) != 3])
    t_reach = CL.table(
        "T-REACHABILITY", ("declared fault", "faulted side", "certificate",
                           "word the machinery writes"),
        [(r["fault"], r["faulted_side"], r["certificate"], r["word"])
         for r in reach_rows])

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
    # THE DIRECTION-BEARING SENTENCES, LICENSED PER OCCURRENCE.  Each of these
    # was invertible at exit 0 with the artifacts byte-identical, because the
    # walls police phrases and the referent registry policies numerals, and a
    # reversed direction is neither (K3 MAJOR-12).
    c7 = CL.claim("the first three rows are set equality, not isomorphism")
    c8 = CL.claim("it is that the record does not carry them")
    c9 = CL.claim("overlap is what carries identity, and overlap is waste")
    c10 = CL.claim("the eraser is not arena-blind as declared, and the "
                   "reconstruction is arena-blind as measured")
    c11 = CL.claim("no committed history sees more than %s of the %s record "
                   "blocks" % (com(max_blocks), com(len(blocks))))
    c12 = CL.claim("what the arms locate is balance and not the number of "
                   "parts")
    # the anchors' FRAME, licensed too: a byte-perfect quotation can be
    # inverted around by the sentence that introduces it (K3 MAJOR-12)
    c13 = CL.claim("the object EPR measured is the right frame for this one. "
                   "Two structures decide everything, and both are measured")
    # THE SENTENCES WHOSE NUMERALS COULD BE EXCHANGED INVISIBLY.  Two numbers
    # of one universe swapped inside a sentence pass every numeral gate ever
    # built here -- the referent registry checks membership, not place (K1
    # MAJ-5's demonstration was exactly this swap).  Licensing the sentence
    # binds them to their places.
    c14 = CL.claim("There are %s such events in the corpus; %s histories carry "
                   "at least one" % (com(unwritten), com(empty_hist)))
    c15 = CL.claim("%s such events run in the corpus, leaving %s histories "
                   "partly unwritten" % (com(unwritten), com(empty_hist)))
    c16 = CL.claim("The corpus holds %s slots carrying %s distinct histories "
                   "and leaves %s distinct bare records; the %s that vanish "
                   "are the collisions"
                   % (com(len(corp)), com(R["corpus"]["distinct_histories"]),
                      com(len(fiber)), com(R["surplus"]["histories_lost"])))
    f1 = CL.fence(head[0])
    f2 = CL.fence(head[1])
    f3 = CL.fence(head[2])
    if mut("MUT-PAPER-CLAIM"):
        CL.claim("a claim the paper does not carry")
    if render:
        R["rendered"] = {"tables": [t_recon, t_prop, t_depth, t_syn, t_bal,
                                    t_reach],
                         "claims": [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10,
                                    c11, c12, c13, c14, c15, c16],
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
                {len(scr), survivors, len(syn_rows), good, len(teeth),
                 len(size_blind), certified_scr, reached_comparator,
                 swap_visited, swap_candidates, swap_candidates - swap_visited,
                 R["control_scrambled"]["candidates"],
                 R["control_scrambled"]["rejected_as_non_moving"],
                 SWAP_CAP, len(coord_totals), min(coord_totals.values()),
                 max(coord_totals.values()), len(bal_rows), len(bal_ok),
                 len(bal_unbalanced_ok), len(bal_bad), BALANCE_CEILING}
                | {x for shape in SYNTHETIC_PARTS for x in shape}
                | {len(s) for s in balance_shapes()}
                | {x for s in balance_shapes() for x in s},
                pairs={(survivors, len(scr)), (reached_comparator, len(scr)),
                       (swap_visited, swap_candidates),
                       (len(bal_ok), len(bal_rows)),
                       (len(size_blind), len(teeth))})
    RR.universe("CELLS", ["cell", "cells", "token", "tokens", "record block",
                          "record blocks"],
                {DIM, drop_ok, rec["tau"], 2 * DIM // NACT, len(drop2),
                 max_blocks, SCRAMBLE_MULT, SCRAMBLE_ADD, min(incid),
                 len(I7_LINKS)},
                pairs={(drop_ok, DIM), (DIM, DIM), (drop2_ok, len(drop2)),
                       (max_blocks, DIM)})
    RR.universe("NAMINGS", ["naming", "namings", "relabelling",
                            "relabellings", "splitting", "splittings",
                            "coordinate"],
                {n_iso, n_coh, idx.numerator, len(reso), len(facs),
                 len(trials), len(orbit), COORD_TRIALS, RELABEL_TRIALS,
                 len(coord_dev), len(rel_bad), len(baseline), affine_leaks,
                 coord_leaks},
                pairs={(n_coh, n_iso), (affine_leaks, len(trials)),
                       (coord_leaks, COORD_TRIALS)})
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
                 len(blocks), set_distinct, disjoint_hist, max_blocks,
                 c_by[("C3", None)], least_w, len(never_set & least_set)}
                | set(refusal.values()),
                pairs={(depth_hits, len(corp)),
                       (c_by[("C3", None)], len(corp)),
                       (refusal.get("NO-MEET-GAP", 0), len(corp)),
                       (refusal.get("TOKEN-IN-NO-ACTOR", 0), len(corp))})
    RR.universe("CAST", ["actor", "actors", "cast", "site", "sites"],
                {NACT, 2 * DIM // NACT, NACT * (NACT - 1), len(link_parts or ()),
                 min(incid)},
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
    if mut("MUT-WALL-PARAPHRASE"):
        wall_text = paper + ("\n\nA single history suffices to reconstruct "
                             "the cast.\n")
    if mut("MUT-WALL-POSITIVE"):
        # BOTH copies, line breaks and all, so the positive leg is exercised
        # on its own rather than left satisfied by the other occurrence
        wall_text = re.sub(
            r"the cast is derived at the corpus and at no\s+single history",
            "the cast comes out of the record", paper)
    wprob = None
    for w in WALLS:
        try:
            w.scan(wall_text)
        except ET.CheckFail as exc:
            wprob = exc.detail
    # THE SCAN'S OWN RESULT IS PUBLISHED, not only the pattern list: the
    # delivered key was the wall's declaration, which no paper edit can move,
    # so the wall's falsifier could not move its own declared target (K3
    # MAJOR-2).
    R["walls"] = {"walls": [w.seal_value() for w in WALLS],
                  "scanned_sha256_12": ET.bytes_digest(
                      wall_text.encode("utf-8")),
                  "violation": wprob or "none"}
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

    # THE BACKING SET IS BUILT FROM MEASUREMENTS, not from digits scraped out
    # of digests (K3 MINOR-4: 18 of 96 admitted values came from digest
    # fragments alone, and two probes walked in through them).  Integer leaves
    # count; a dictionary KEY counts only where the key is a declared numeric
    # index, and the pattern is named here rather than left to a regex over
    # every string in the receipt.
    backing = set()
    KEYNUM = re.compile(r"^(?:[A-Za-z][A-Za-z0-9-]*:)?(-?\d+)$")

    def harvest(o):
        if isinstance(o, bool):
            return
        if isinstance(o, int):
            backing.add(o)
        elif isinstance(o, dict):
            for k, v in o.items():
                m = KEYNUM.match(str(k))
                if m:
                    backing.add(int(m.group(1)))
                harvest(v)
        elif isinstance(o, (list, tuple)):
            for v in o:
                harvest(v)
    harvest(R)
    # The exemptions live in the registry that exists for them, and every one
    # must be USED (K3 MINOR-3/16): a declared exemption whose token the paper
    # never carries is deleted rather than shipped.
    for tok, why in (("paper-33", "the AID unit"), ("paper-35", "the FAC unit"),
                     ("paper-38", "the EPR unit"), ("paper 41", "this unit"),
                     ("paper-21", "the schedule parent"),
                     ("E-25", "the engraving this template opens at"),
                     ("E-33", "the engraving it closes at"),
                     ("E-24", "the counting-only engraving"),
                     ("AG(2, 3)", "the arena's name"),
                     ("sha256-12", "the digest length")):
        REG.exempt_token(tok, why)
    exempt_used = {t: w for t, w in REG.exempt.items() if t in paper}
    exempt_unused = sorted(t for t in REG.exempt if t not in paper)
    exempt_nums = {int(d) for t in exempt_used
                   for d in re.findall(r"\d+", t)}
    if mut("MUT-EXEMPTION"):
        exempt_unused = exempt_unused + ["injected"]
    nums = paper_numerals(paper)
    if mut("MUT-COVERAGE"):
        nums = nums + paper_numerals("\n\nAn unbacked numeral: 987654.\n")
    cov = [n for n in nums
           if int(n) not in backing and int(n) not in exempt_nums]
    spelled = paper_spelled(paper)
    if mut("MUT-SPELLED"):
        spelled = spelled + [SPELLED["thousand"] * SPELLED["thousand"]]
    spell_bad = sorted({v for v in spelled
                        if v not in backing and v not in exempt_nums})
    R["paper_coverage"] = {"numerals": len(nums),
                           "unbacked": sorted(set(cov)),
                           "spelled_numerals": len(spelled),
                           "spelled_unbacked": spell_bad,
                           "backing_values": len(backing),
                           "exemptions": {t: w for t, w in
                                          sorted(exempt_used.items())},
                           "exemptions_unused": exempt_unused}
    SEAL.seal("paper_coverage", R["paper_coverage"], "G-PAPER-COVERAGE")
    REG.measured("numerals", len(nums),
                 "numerals in the paper, fences included")
    REG.measured("unbacked", len(set(cov)), "numerals backed by nothing")
    REG.measured("spelled", len(spelled), "quantities the paper spells out")
    REG.measured("spelled_bad", len(spell_bad), "spelled quantities unbacked")
    gate("G-PAPER-COVERAGE",
         REG.stmt("every one of the paper's {numerals} numerals -- fenced "
                  "blocks, verdict blocks and tables included -- and every one "
                  "of the {spelled} quantities it spells out in words is a "
                  "value this receipt carries as an integer measurement or a "
                  "declared exemption whose token the paper actually carries; "
                  "{unbacked} and {spelled_bad} are neither",
                  numerals=1, unbacked=1, spelled=1, spelled_bad=1),
         not cov and not spell_bad and not exempt_unused,
         "numerals %d unbacked %s spelled %d unbacked %s unused exemptions %s"
         % (len(nums), sorted(set(cov)) or "none", len(spelled),
            spell_bad or "none", exempt_unused or "none"))

    # -- anchors, typed counts, exactness ----------------------------------
    if mut("MUT-ANCHOR-CONSUMER"):
        ASET.by_name[ANCHORS[0].name].consumer = "G-CORPUS-SHAPE"
    try:
        ASET.verify_consumption(LD)
        aprob = None
    except ET.CheckFail as exc:
        aprob = exc.detail
    arows = [ASET.by_name[a.name] for a in ANCHORS]   # the per-run copies
    R["anchors"] = [{"name": a.name, "source": a.source,
                     "consumer": a.consumer, "chars": len(a.needle),
                     "read_by": sorted(a.read_by)} for a in arows]
    SEAL.seal("anchors", R["anchors"], "G-ANCHORS-CONSUMED")
    REG.measured("anchors", len(ANCHORS), "len(ANCHORS)")
    gate("G-ANCHORS-CONSUMED",
         REG.stmt("each of the {anchors} verbatim anchors occurs exactly once "
                  "in the pinned parent AND once in this paper's own "
                  "rendering, and its declared consumer gate took a value out "
                  "of it and compared that value with a measurement",
                  anchors=1),
         aprob is None and all(a.consumer in a.read_by for a in arows),
         "anchors %d consumed %d %s"
         % (len(ANCHORS), sum(1 for a in arows if a.consumer in a.read_by),
            aprob or ""))

    src_typed = src
    if mut("MUT-TYPED"):
        # a REAL typed statement, admitted to the source the auditor reads
        src_typed = src + ('\n\ndef _typed_probe(REG):\n'
                           '    return REG.stmt("a statement with 9 typed")\n')
    # `gate` is scanned too, so that a typed fragment CONCATENATED beside a
    # statement -- outside the stmt call and inside the gate call -- is caught
    # as well (K3 MAJOR-10's first door).
    CALLERS = ("stmt", "claim", "table", "fence", "gate")
    typed = sorted(set(REG.audit_module(src_typed, statement_callers=CALLERS))
                   | set(audit_typed_calls(src_typed, CALLERS)))
    R["typed_counts"] = {"offenders": typed,
                         "registry": len(REG.values),
                         "statement_builders_scanned": sorted(CALLERS),
                         "exemptions": {t: w for t, w in sorted(REG.exempt.items())}}
    SEAL.seal("typed_counts", R["typed_counts"], "G-NO-TYPED-COUNTS")
    REG.measured("registry", len(REG.values), "measured names in the registry")
    REG.measured("builders", len(CALLERS), "statement builders scanned")
    gate("G-NO-TYPED-COUNTS",
         REG.stmt("no numeral is typed into anything this unit vouches for: "
                  "every published statement interpolates from the "
                  "{registry} measured names, and an AST scan of this module "
                  "finds no string literal ANYWHERE in the subtree of a call "
                  "to one of the {builders} statement, claim, table and fence "
                  "builders that types a numeral -- so neither a concatenated "
                  "fragment nor a table cell escapes it", registry=1,
                  builders=1),
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
    if mut("MUT-FLOAT"):
        # a GENUINE non-integer leaf, so the recursive type walk is the thing
        # that catches it.  The value is taken from the interpreter rather than
        # typed, because a float literal in this module is itself an offence.
        R["reconstruction"]["threshold"] = sys.float_info.epsilon
    typewalk(R, "")
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

    # THE NINE FAMILIES ARE USED, AND THE USE IS GATED (K2 m8): each family's
    # check id is read off the template's own table and matched to a live call
    # site found by AST in this module, so "imported and used, not copied" is a
    # measurement rather than a list.
    fam_member = {"T-SEAL-PROMOTION": "seal", "T-TRANSCRIPT-BOUND": "bind",
                  "T-WALL-SEMANTIC": "scan", "T-ANCHOR-CONSUMED": "locate",
                  "T-CLAIMS-EQUAL": "claim", "T-REFERENT-BOUND": "universe",
                  "T-NO-TYPED-COUNTS": "stmt",
                  "T-FALSIFIER-POISONS": "audit_descriptions",
                  "T-READ-SET": "gate_at_close"}
    called = {getattr(n.func, "attr", None) or getattr(n.func, "id", None)
              for n in ast.walk(ast.parse(src)) if isinstance(n, ast.Call)}
    fam_rows = [{"check": c, "member": fam_member.get(c),
                 "called": bool(fam_member.get(c) in called)}
                for _k, _n, c in ET.FAMILIES]
    if mut("MUT-FAMILIES"):
        fam_rows[0]["called"] = not fam_rows[0]["called"]
    R["provenance"]["families_used"] = fam_rows
    if mut("MUT-PROVENANCE"):
        R["provenance"]["pin_sha256_12"] = R["provenance"]["pin_sha256_12"][::-1]
    dig12 = [k for k, v in R["provenance"].items()
             if k.endswith("sha256_12")
             and len(v) == len(SOURCES[PIN_REL])
             and all(c in "0123456789abcdef" for c in v)]
    prov_ok = (len(dig12) == sum(1 for k in R["provenance"]
                                 if k.endswith("sha256_12"))
               and R["provenance"]["pin_sha256_12"] == SOURCES[PIN_REL]
               and R["provenance"]["template_sha256_12"] == SOURCES[TEMPLATE_REL]
               and all(r["called"] for r in fam_rows)
               and len(fam_rows) == len(ET.FAMILIES))
    R["mutants"] = [{"name": m[0], "gate": m[1], "target": m[2],
                     "description": m[3]} for m in MUTANTS]
    # the gates that fire at or after this one, named so a falsifier for a
    # closing gate is not misread as unreachable
    closing = {"G-PROVENANCE", "G-READS-AT-THE-ACCESSOR",
               "T-FALSIFIER-COVERAGE", "G-TRANSCRIPT-BOUND",
               "G-EVIDENCE-BOUND"}
    allowed = set(LD.names()) | closing | {c for _k, _n, c in ET.FAMILIES}
    bad_mut = sorted(m["name"] for m in R["mutants"]
                     if m["gate"] not in allowed or not m["target"].strip())
    names_unique = len({m["name"] for m in R["mutants"]}) == len(R["mutants"])
    SEAL.seal("provenance", R["provenance"], "G-PROVENANCE")
    SEAL.seal("mutants", R["mutants"], "G-PROVENANCE")
    SEAL.seal("reconstruction_rule", R["reconstruction_rule"], "G-PROVENANCE")
    REG.measured("digests", len(dig12), "published sha256-12 digests")
    REG.measured("registered_mutants", len(R["mutants"]), "len(R['mutants'])")
    REG.measured("families", len(fam_rows), "template families used")
    gate("G-PROVENANCE",
         REG.stmt("everything this unit VOUCHES for is sealed, not only what "
                  "it measures: {digests} published digests, each well formed "
                  "and the pin's and the template's equal to the values the "
                  "pin froze; the reconstruction rule in words; the "
                  "{registered_mutants} falsifier rows, each naming a "
                  "distinct recipe, a non-empty measured target and a gate "
                  "this run can reach; and the {families} template families, "
                  "each matched from the template's own table to a live call "
                  "in this module", digests=1, registered_mutants=1,
                  families=1),
         prov_ok and not bad_mut and names_unique,
         "digests %d mutants %d families %d unreachable %s"
         % (len(dig12), len(R["mutants"]),
            sum(1 for r in fam_rows if r["called"]), bad_mut or "none"))

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
                  "at the last gate before promotion -- and again after the "
                  "last gate of all, so the window between them is closed",
                  declared_reads=1),
         dprob is None, "declared %d distinct %d %s"
         % (len(declared), rev2["distinct"], dprob or ""))

    if mut("MUT-TRANSCRIPT"):
        TR.say("  [PASS] G-A-GATE-THAT-NEVER-RAN :: forged")
    try:
        TR.bind(LD)
        tprob = None
    except ET.CheckFail as exc:
        tprob = exc.detail
    R["transcript_binding"] = {"rows_at_this_gate": len(LD.rows),
                               "chain_at_this_gate": LD.head,
                               "problem": tprob or "none",
                               "chain_recomputes":
                                   LD.recompute_chain() == LD.head}
    SEAL.seal("transcript_binding", R["transcript_binding"],
              "G-TRANSCRIPT-BOUND")
    REG.measured("rows_here", len(LD.rows), "ledger rows at this gate")
    gate("G-TRANSCRIPT-BOUND",
         REG.stmt("every PASS line in the transcript that will be promoted is "
                  "parsed back out of the finished text and reconciled with "
                  "the ledger as a multiset, evidence included, and the "
                  "ledger's own chain is recomputed from its {rows_here} rows "
                  "so far", rows_here=1),
         tprob is None and LD.recompute_chain() == LD.head,
         "rows so far %d chain %s %s" % (len(LD.rows), LD.head, tprob or ""))

    evbad = evidence_offences(LD.rows, SEAL.seals, R)
    if mut("MUT-EVIDENCE"):
        evbad = evidence_offences(
            LD.rows + [dict(LD.rows[-1], gate="G-CORPUS-SHAPE",
                            statement="a forged row", evidence="slots %d"
                            % (len(corp) - 1))],
            SEAL.seals, R)
    R["evidence_bound"] = {"rows": len(LD.rows), "offences": evbad}
    SEAL.seal("evidence_bound", R["evidence_bound"], "G-EVIDENCE-BOUND")
    REG.measured("ev_rows", len(LD.rows), "finished evidence lines")
    gate("G-EVIDENCE-BOUND",
         REG.stmt("the transcript's own numbers are bound to the receipt: "
                  "every integer in each of the {ev_rows} finished evidence "
                  "lines is a value the gate's own sealed keys carry, or one "
                  "its own statement published -- so the two artifacts cannot "
                  "be promoted contradicting each other", ev_rows=1),
         not evbad, "rows %d offences %s" % (len(LD.rows), evbad or "none"))

    # THE COVERAGE GATE CARRIES NO WAIVER.  The delivered one said the gate
    # could not be falsified from inside its own denominator; K3 built the
    # falsifier and it dies here, so the claim was untrue and the waiver is
    # gone -- MUT-COVERAGE-GAP is that recipe, adopted.
    # the withheld row is the ONLY falsifier of its gate, so withholding it
    # really does leave a fired gate uncovered
    rows_for_harness = [ET.Falsifier(m[0], m[1], m[3], m[2], None)
                        for m in MUTANTS if not (mut("MUT-COVERAGE-GAP")
                                                 and m[0] == "MUT-SURPLUS")]
    HARNESS = ET.FalsifierHarness(rows_for_harness)
    waivers: dict = {}
    try:
        cov2 = HARNESS.coverage(LD, waivers, {})
        fprob = None
    except ET.CheckFail as exc:
        cov2, fprob = {"gates": len(LD.rows) + 1, "falsified": 0,
                       "waived": len(waivers)}, exc.detail
    # THE TEMPLATE'S OWN HONESTY LEG, CALLED (K3 MAJOR-5): a hook whose body
    # only appends a constant to the finding list dies at the gate it names
    # without ever moving the measurement that gate reads.
    sentinels = HARNESS.audit_descriptions(src)
    fired = set(LD.names()) | {"T-FALSIFIER-COVERAGE"}
    targeted = {m[1] for m in MUTANTS}
    missing_hooks, orphan_hooks = audit_mut_hooks(src, [m[0] for m in MUTANTS])
    if mut("MUT-HOOK-MISSING"):
        missing_hooks, orphan_hooks = audit_mut_hooks(
            src, [m[0] for m in MUTANTS] + ["MUT-NOT-IMPLEMENTED"])
    if mut("MUT-SENTINEL-DESC"):
        sentinels = HARNESS.audit_descriptions(
            src + "\n\ndef _sentinel_probe(bad):\n"
                  "    if mut('MUT-SENTINEL-DESC'):\n"
                  "        bad.append('injected')\n")
    R["falsifiers"] = {"mutants": len(MUTANTS), "gates": cov2["gates"],
                       "falsified": cov2["falsified"],
                       "falsified_at_fired_gates": len(targeted & fired),
                       "waived": cov2["waived"],
                       "sentinel_shaped_hooks": sentinels,
                       "rows_without_a_hook": missing_hooks,
                       "hooks_without_a_row": orphan_hooks,
                       "targets": sorted({m[2] for m in MUTANTS})}
    SEAL.seal("falsifiers", R["falsifiers"], "T-FALSIFIER-COVERAGE")
    REG.measured("mutants", len(MUTANTS), "len(MUTANTS)")
    REG.measured("gates", cov2["gates"], "gates fired, this one included")
    REG.measured("falsified_fired", len(targeted & fired),
                 "fired gates carrying a falsifier")
    gate("T-FALSIFIER-COVERAGE",
         REG.stmt("every gate that fired carries a falsifier naming the "
                  "measured key it must move, and none carries a waiver: "
                  "{gates} gates, {falsified_fired} of them falsified by one "
                  "of {mutants} recipes; every recipe has an implementation "
                  "and every implementation has a recipe, by AST; and no hook "
                  "is sentinel-shaped -- none merely appends a constant to the "
                  "finding list its gate reads", gates=1, mutants=1,
                  falsified_fired=1),
         fprob is None and not sentinels and not missing_hooks
         and not orphan_hooks and len(targeted & fired) == len(fired),
         "gates %d falsified %d of %d waived %d sentinels %s orphans %s %s"
         % (cov2["gates"], len(targeted & fired), len(fired), cov2["waived"],
            sentinels or "none", (missing_hooks + orphan_hooks) or "none",
            fprob or ""))

    # the WHOLE transcript, both closing rows included, reconciled once more
    TR.bind(LD)
    R["transcript"] = {"sha256_12": ET.bytes_digest(TR.text().encode("utf-8")),
                       "lines": len(TR.lines), "gate_rows": len(LD.rows),
                       "chain_head": LD.head}
    SEAL.seal("transcript", R["transcript"], "G-TRANSCRIPT-BOUND")
    # THE READ SET, RE-RECONCILED AFTER THE LAST GATE (K3 MINOR-7): the two
    # windows the delivered instrument left open -- between the read gate and
    # the flag, and after the flag -- are closed by re-taking the multiset here
    # and refusing if it moved.
    late = collections.Counter(p for p in RS.log
                               if p not in RS.exemptions
                               and not p.endswith(".tmp"))
    # and the evidence binding re-taken over the WHOLE ledger, its own row and
    # the coverage row included, so no line escapes by firing last
    closing = evidence_offences(LD.rows, SEAL.seals, R)
    if closing:
        raise ET.CheckFail("G-EVIDENCE-BOUND",
                           "closing rows carry unbound evidence: %s" % closing)
    if sum(late.values()) != rev2["reads"] or len(late) != rev2["distinct"]:
        raise ET.CheckFail("T-READ-SET",
                           "a repository read happened after the read gate: "
                           "%d/%d became %d/%d"
                           % (rev2["reads"], rev2["distinct"],
                              sum(late.values()), len(late)))

    if mut("MUT-SEAL-ADD"):
        R["forged_finding"] = {"smuggled": len(LD.rows)}
    # the audit hook stays LIVE until the moment of promotion, so the window
    # after the flag is closed as well as the window before it; promotion's own
    # opens are the only reads outside it
    late2 = collections.Counter(p for p in RS.log
                                if p not in RS.exemptions
                                and not p.endswith(".tmp"))
    RS.active = False
    if late2 != late:
        raise ET.CheckFail("T-READ-SET",
                           "a repository read happened after the closing "
                           "reconciliation: %s"
                           % sorted((late2 - late).elements()))
    SEAL.verify_at_promotion(R, LD, "seal_manifest")

    if not write:
        return R, TR, LD, SEAL, None
    # the side artifact is checked against its gate-time seal BEFORE anything
    # is staged, so a corrupted transcript never reaches disk at all
    if ET.bytes_digest(TR.text().encode("utf-8")) != R["transcript"]["sha256_12"]:
        raise ET.CheckFail("G-TRANSCRIPT-BOUND",
                           "the transcript to be promoted differs from the "
                           "gate-time seal")
    dig = ET.promote(SEAL, LD, R, TR.text(),
                     os.path.join(REPO, RECEIPT_REL),
                     os.path.join(REPO, OUTPUT_REL))
    return R, TR, LD, SEAL, dig


def k_parse_head(segment):
    """PARSE a rendered verdict segment back into integers.  This is the
    comparator's own route to the head: it reads the emitted string and knows
    nothing about how it was built.

    EVERY digit group of every field is returned, not merely the first: the
    delivered parser bound 12 of the head's numerals and left the rest free,
    so `9-OF-9`, `3-OF-6` and `0-SURVIVE` could each be moved in the renderer
    and the paper together at exit 0 (K3 MAJOR-7)."""
    out = {}
    body = segment[segment.index("<") + 1:segment.rindex(">")]
    for part in body.split(";"):
        if "=" not in part:
            continue
        k, v = part.split("=", 1)
        digits = [int(d.replace(",", "")) for d in re.findall(r"\d[\d,]*", v)]
        if digits:
            out[k.strip()] = digits
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
    ("MUT-LINK", "G-LINK-STRUCTURE-DERIVED", "link_structure",
     "one derived actor pair is deleted, so the derived link structure is no "
     "longer the declared one"),
    ("MUT-TARGETS", "G-RECONSTRUCTION-TARGETS-TOTAL", "reconstruction_targets",
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
    ("MUT-ANCHOR", "G-ANCHORS-LOCATED", "anchors_located",
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
    ("MUT-TRANSCRIPT", "G-TRANSCRIPT-BOUND", "transcript_binding",
     "a PASS line for a gate that never ran is appended to the transcript"),
    ("MUT-FLOAT", "G-RECEIPT-EXACT", "exactness",
     "a non-integer leaf is admitted to the published receipt"),
    ("MUT-SEAL-ADD", "T-SEAL-PROMOTION", "forged_finding",
     "a top-level receipt key is created after the seal manifest is taken"),
    # -- the recipes the panels bought --------------------------------------
    ("MUT-COORDINATE", "G-STRIPPING-COORDINATE-FREE", "residue_channel",
     "one uniformly random coordinate is recorded as having moved a published "
     "quantity, so the coordinate-freedom census no longer holds"),
    ("MUT-MECHANISM", "G-MINIMALITY-PER-HISTORY", "minimality_per_history",
     "a single history is credited with writing every record block, so the "
     "counting fact that no history carries enough of them is destroyed"),
    ("MUT-BLOCKS-25", "G-MINIMALITY-BLOCKS", "minimality_blocks",
     "a 25-block subset is credited with reconstructing, so the block set "
     "stops being irredundant two blocks down"),
    ("MUT-BICONDITIONAL", "G-THE-CONNECTION", "connection",
     "one further history is called never-crystallizing, so the biconditional "
     "with the least collapse threshold fails in one direction"),
    ("MUT-ORBIT", "G-NAMING-RESIDUE", "naming",
     "one splitting is removed from the orbit of the declared one, so the "
     "action is no longer transitive and the index stops being a count"),
    ("MUT-BALANCE", "G-CONTROL-BALANCE", "control_balance",
     "one swept shape's recovery is flipped, so the boundary the sweep "
     "locates is no longer balance"),
    ("MUT-REACHABILITY", "G-OUTCOMES-REACHABLE", "outcome_reachability",
     "all but one declared fault is dropped, so a pre-registered outcome is "
     "left with no run that writes it"),
    ("MUT-EVIDENCE", "G-EVIDENCE-BOUND", "evidence_bound",
     "a finished evidence line reports a corpus size the receipt does not "
     "carry, so the two artifacts contradict each other"),
    ("MUT-FAMILIES", "G-PROVENANCE", "provenance",
     "one template family is recorded as carried rather than called"),
    ("MUT-HOOK-MISSING", "T-FALSIFIER-COVERAGE", "falsifiers",
     "a falsifier row is declared for which no implementation exists anywhere "
     "in this module"),
    ("MUT-SENTINEL-DESC", "T-FALSIFIER-COVERAGE", "falsifiers",
     "a hook that only appends a constant to the finding list its gate reads "
     "is admitted to the module the honesty audit scans"),
    ("MUT-COVERAGE-GAP", "T-FALSIFIER-COVERAGE", "falsifiers",
     "one row is withheld from the harness, leaving a gate that fired with "
     "neither a falsifier nor a waiver -- the recipe the deleted waiver said "
     "could not exist"),
    ("MUT-EXEMPTION", "G-PAPER-COVERAGE", "paper_coverage",
     "an exemption is declared whose token the paper never carries"),
    ("MUT-SPELLED", "G-PAPER-COVERAGE", "paper_coverage",
     "a quantity spelled out in words is admitted that no measurement backs"),
    ("MUT-WALL-PARAPHRASE", "G-PAPER-WALLS", "walls",
     "the paper is given a natural re-voicing of a forbidden reading -- 'a "
     "single history suffices to reconstruct the cast' -- rather than the "
     "literal form the delivered blacklist knew"),
    ("MUT-WALL-POSITIVE", "G-PAPER-WALLS", "walls",
     "both copies of a standing sentence are deleted outright, so the wall's "
     "positive leg is exercised on its own"),
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
        # THE PAYLOAD AS IT STOOD AT REFUSAL.  Reading a constant here made
        # `moved` unconditionally true and the move-proof unfalsifiable; six of
        # the delivered recipes named a target they never moved (K3 MAJOR-2).
        after = ET.digest((PARTIAL["R"] or {}).get(target))
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
            "|--list-mutants|--mutant NAME|--render\n"
            "  --render and --list-gates are PARTIAL modes: they return "
            "before the paper gates\n")
        return 2
    mode = argv[1]
    if mode == "--list-mutants":
        for m in MUTANTS:
            print("%-24s %-34s %s" % (m[0], m[1], m[2]))
        return 0
    if mode == "--list-gates":
        _R, _TR, LD, _SEAL, _d = full_run(write=False, mode=mode)
        for g in LD.names():
            print(g)
        return 0
    if mode == "--render":
        R, _TR, _LD, _SEAL, _d = full_run(write=False, render=True, mode=mode)
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
            R, TR, LD, SEAL, _d = full_run(write=False, mode=mode)
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
        # THE SIDE ARTIFACT IS VERIFIED BEFORE THE REPLACE, AND ROLLED BACK IF
        # IT LANDS WRONG (K3 MINOR-10): the delivered instrument verified it
        # only after os.replace, so a corrupted transcript reached disk and
        # stayed there while the run refused.
        rollback = None
        out_path = os.path.join(REPO, OUTPUT_REL)
        if mode == "--run" and os.path.exists(out_path):
            with open(out_path, "rb") as fh:
                rollback = fh.read()
        try:
            R, TR, LD, SEAL, dig = full_run(write=(mode == "--run"), mode=mode)
        except ET.CheckFail as exc:
            sys.stderr.write("REFUSED at %s :: %s\n" % (exc.check, exc.detail))
            return 1
        sys.stdout.write(TR.text())
        if mode == "--run":
            with open(out_path, "rb") as fh:
                on_disk = fh.read()
            if ET.bytes_digest(on_disk) != R["transcript"]["sha256_12"]:
                if rollback is not None:
                    with open(out_path, "wb") as fh:
                        fh.write(rollback)
                sys.stderr.write("REFUSED: promoted transcript bytes differ "
                                 "from the gate-time seal (rolled back)\n")
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
