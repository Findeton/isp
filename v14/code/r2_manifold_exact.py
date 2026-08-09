#!/usr/bin/env python3
"""
v14 R2 -- THE MANIFOLD RUNG.  Exact instrument.

PIN: v14/note-r2-manifold-pin.md (frozen v14 ledger #11, sha256-12 76d42dfbc900).
The pin is verified BY HASH at run time (gate A-PIN-R2); so are the R1
adjudication note (the source of the criterion / recipe / null readings), the
R0 founding pin's I6 and I3 rows (the v13 receipts that carry the block and
the topology definitions), and the v14 #4 erratum's TOP-paper companion hash.

THE QUESTION (pin section 2, falsifiable, two-sided):
  does any drawing rule in a declared finite grid of atlas declarations
  produce a component with a NON-COMPLETE overlap graph -- and where locality
  appears, what do the ported standards measure?

Both verdict heads are first class:
  R2-LOCALITY-AT-<computed rule list ...>
  R2-NO-LOCALITY-IN-THE-DECLARED-GRID<...>
Each is derived INSIDE a gate from the measured census, compared by COMPLETE
STRING EQUALITY against a segment-by-segment rebuild (RUNBOOK section 14
addendum, v14 #10), and each is reachable by the instrument (two flip mutants).

CLI CONTRACT (confirmed in code before invocation, v13 #238):
  (no arguments)        THE PLAIN DELIVERY RUN.  Runs every gate, derives the
                        verdict, and WRITES the two artifacts
                        v14/code/r2_manifold_output.txt and
                        v14/code/r2_manifold_receipt.json.  Exit 0.  Any gate
                        failure aborts BEFORE any artifact is written.
  --mutant NAME         Runs the delivery pipeline with the named injection
                        active.  MUST exit 1 with a NAMED gate failure and
                        MUST NOT write any artifact.  Unknown name -> exit 2.
  --list-mutants        Prints the declared mutant names, one per line.  Exit 0.
  --selftest            THE FALSIFICATION SELFTEST.  Re-invokes this file as a
                        subprocess once per declared mutant, requires exit 1,
                        requires the death certificate to name a gate, and
                        requires the artifacts on disk to be byte-unchanged.
                        Writes NO artifacts itself.  Exit 0 iff every mutant
                        died correctly.
Arithmetic is exact throughout: int and fractions.Fraction only.  A float
literal, a float call, or a true-division operator anywhere in this source is
a gate failure (G-FLOATGUARD, an AST scan of this file).

Concurrency note: this unit owns ONLY v14/paper-02-manifold-rung.md,
v14/code/r2_manifold_exact.py, v14/code/r2_manifold_output.txt and
v14/code/r2_manifold_receipt.json.  It reads v13 receipts and v14 notes and
writes nothing else.
"""

import ast
import hashlib
import itertools
import json
import os
import subprocess
import sys
from fractions import Fraction

# ----------------------------------------------------------------------------
# 0.  Paths, mutation switch, and the gate ledger
# ----------------------------------------------------------------------------

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)                      # .../isp/v14
ROOT = os.path.dirname(REPO)                      # .../isp
SRC = os.path.abspath(__file__)
OUT_TXT = os.path.join(HERE, "r2_manifold_output.txt")
OUT_JSON = os.path.join(HERE, "r2_manifold_receipt.json")

MUTANT = None            # set only from the command line; gates never read it


class GateFailure(Exception):
    pass


GATES = []               # [{name, statement, passed, value}]
ANCHORS = []             # [{name, artifact, expected, measured, ok}]


def gate(name, statement, ok, value=None):
    """Register a gate.  A gate predicate NEVER references mutant identity
    (RUNBOOK section 14 addendum, v13 #208)."""
    GATES.append({"name": name, "statement": statement,
                  "passed": bool(ok), "value": value})
    if not ok:
        raise GateFailure("GATE FAILED: %s -- %s | value=%r" % (name, statement, value))
    return True


def sha12(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()[:12]


def sha256_full(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


# ----------------------------------------------------------------------------
# 1.  G-FLOATGUARD -- exact arithmetic enforced by an AST scan of this source
# ----------------------------------------------------------------------------

# The float type is obtained WITHOUT naming it, so the guard needs no
# exemption for its own detector.
FLOAT_T = type((1).__truediv__(1))

BANNED_NAMES = ("float", "math", "random", "numpy", "statistics", "decimal")


def float_guard():
    with open(SRC, "r") as fh:
        text = fh.read()
    tree = ast.parse(text)
    offences = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, FLOAT_T):
            offences.append(("float-literal", node.lineno))
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div):
            offences.append(("true-division", node.lineno))
        if isinstance(node, ast.Name) and node.id in BANNED_NAMES:
            offences.append(("banned-name:" + node.id, node.lineno))
        if isinstance(node, ast.Attribute) and node.attr in BANNED_NAMES:
            offences.append(("banned-attr:" + node.attr, node.lineno))
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            mod = getattr(node, "module", None) or ""
            names = [a.name for a in node.names]
            for nm in [mod] + names:
                if nm.split(".")[0] in BANNED_NAMES:
                    offences.append(("banned-import:" + nm, node.lineno))
    if MUTANT == "float-leak":
        offences.append(("injected-float", 0))
    return offences


# ----------------------------------------------------------------------------
# 2.  Anchors -- every inherited number arrives hash-verified (the R0 rows)
# ----------------------------------------------------------------------------

ANCHOR_ROWS = [
    # (gate name, repo-relative path, expected sha256-12, provenance sentence)
    ("A-PIN-R2", "v14/note-r2-manifold-pin.md", "76d42dfbc900",
     "this unit's pin, frozen at v14 ledger #11"),
    ("A-R1-ADJ", "v14/note-r1-adjudication.md", "4115dcd83cfa",
     "the R1 joint adjudication: the criterion, the recipe (R2-A), the null"),
    ("A-R0-I6", "v13/code/tb3_third_base_receipt.json", "c9bc956fe751",
     "R0 row I6 -- TB3's third base: the 8-label arena, its declared "
     "permutations"),
    ("A-R0-I3", "v13/code/top_topology_receipt.json", "65bb1fc5231f",
     "R0 row I3 -- the topology base: nerve / link / dimension definitions "
     "and the sphere / torus / pinch-point controls"),
    ("A-ERRATUM-TOP-PAPER", "v13/paper-top-topology.md", "379194959fbc",
     "v14 LOG #4 erratum -- the TOP paper's terminal companion hash, the "
     "written source of the I3 definitions reimplemented here"),
]


def verify_anchors():
    for name, rel, expect, why in ANCHOR_ROWS:
        path = os.path.join(ROOT, rel)
        got = sha12(path)
        if MUTANT == "anchor-hash" and name == "A-R0-I6":
            got = "0" * 12
        ANCHORS.append({"name": name, "artifact": rel, "expected": expect,
                        "measured": got, "provenance": why,
                        "ok": got == expect})
        gate(name, "external anchor %s verifies at %s" % (expect, rel),
             got == expect, {"expected": expect, "measured": got})
    return len(ANCHOR_ROWS)


def read_json(rel):
    with open(os.path.join(ROOT, rel), "r") as fh:
        return json.load(fh)


# ----------------------------------------------------------------------------
# 3.  Permutation / group machinery (exact, tuples of ints)
# ----------------------------------------------------------------------------

def ident(n):
    return tuple(range(n))


def compose(p, q):
    """apply q first, then p."""
    return tuple(p[q[i]] for i in range(len(q)))


def inverse(p):
    out = [0] * len(p)
    for i, v in enumerate(p):
        out[v] = i
    return tuple(out)


def perm_order(p):
    e = ident(len(p))
    c = p
    k = 1
    while c != e:
        c = compose(p, c)
        k += 1
    return k


def closure(gens, n):
    e = ident(n)
    seen = {e}
    frontier = [e]
    while frontier:
        x = frontier.pop()
        for g in gens:
            y = compose(g, x)
            if y not in seen:
                seen.add(y)
                frontier.append(y)
    return sorted(seen)


def cyclic_subgroups(g, n):
    """The COMPLETE subgroup lattice of the cyclic group <g>: one subgroup per
    divisor of ord(g).  Returned newest-smallest-first, each as (name, elements)."""
    N = perm_order(g)
    out = []
    for d in sorted(divisors(N)):
        gd = power(g, d, n)
        out.append(("C%d" % (N // d), tuple(closure([gd], n))))
    return out


def divisors(N):
    out = []
    k = 1
    while k * k <= N:
        if N % k == 0:
            out.append(k)
            if k != N // k:
                out.append(N // k)
        k += 1
    return sorted(out)


def power(p, k, n):
    out = ident(n)
    for _ in range(k):
        out = compose(p, out)
    return out


def orbits_of(elements, labels):
    """Orbits of a set of permutations acting on `labels` (a sorted tuple)."""
    lab = set(labels)
    seen = set()
    out = []
    for a in labels:
        if a in seen:
            continue
        orb = {a}
        frontier = [a]
        while frontier:
            x = frontier.pop()
            for g in elements:
                y = g[x]
                if y in lab and y not in orb:
                    orb.add(y)
                    frontier.append(y)
        seen |= orb
        out.append(tuple(sorted(orb)))
    return tuple(sorted(out, key=lambda o: o[0]))


# ----------------------------------------------------------------------------
# 4.  THE ARENAS (declared as data, RUNBOOK section 15) -- read from I6
# ----------------------------------------------------------------------------

BLOCK_SIZE_DECLARED = 8      # asserted against I6, never trusted as typed

class Arena(object):
    def __init__(self, name, labels, blocks, basepoint, gamma, sigma, note):
        self.name = name
        self.labels = tuple(labels)
        self.blocks = tuple(tuple(b) for b in blocks)
        self.basepoint = basepoint          # None at B
        self.gamma = gamma                  # the transport generator
        self.sigma = sigma                  # the declared symmetry
        self.note = note
        self.n = len(self.labels)
        self.T = tuple(closure([gamma], self.n))          # the DRAWING group
        self.Tsig = tuple(closure([gamma, sigma], self.n))  # the cell-only group


def lift_block_perm(p, nblocks, total):
    """Copy an 8-label block permutation into `nblocks` disjoint blocks of a
    `total`-label arena; every label outside the blocks is fixed."""
    out = list(range(total))
    s = len(p)
    for b in range(nblocks):
        off = b * s
        for i in range(s):
            out[off + i] = off + p[i]
    return tuple(out)


def build_arenas(gamma8, sigma8):
    B = Arena("B", tuple(range(8)), [tuple(range(8))], None, gamma8, sigma8,
              "the single block L1 -- TB3's native 8-label arena (I6)")
    tot = 17
    g2 = lift_block_perm(gamma8, 2, tot)
    s2 = lift_block_perm(sigma8, 2, tot)
    B2 = Arena("B2", tuple(range(tot)), [tuple(range(8)), tuple(range(8, 16))],
               16, g2, s2,
               "L2 -- two isomorphic blocks plus an isolated basepoint (16)")
    return B, B2


# ----------------------------------------------------------------------------
# 5.  THE DECLARED ATLAS GRID (pin section 4) -- enumerated exhaustively
# ----------------------------------------------------------------------------

MODES = ("ALL", "BLOCKWISE", "SLIDING")

# The declared word list generating the Sigma-mixed lattice of <gamma,Sigma>.
SIGMA_WORDS = ("e", "g", "s", "gs", "sg", "ggs", "gsgs")


def word_perm(word, g, s, n):
    p = ident(n)
    for ch in word:
        if ch == "e":
            continue
        p = compose(p, g if ch == "g" else s)
    return p


def declared_sigma_lattice(g, s, n):
    """The DECLARED lattice for the Sigma-mixed class: the cyclic subgroups of
    the declared words, plus the whole group <g,Sigma>.  Declared, finite,
    printed -- not the (astronomically large) full subgroup lattice."""
    out = []
    seen = {}
    for w in SIGMA_WORDS:
        p = word_perm(w, g, s, n)
        els = tuple(closure([p], n))
        if els not in seen:
            seen[els] = "<%s>" % w
            out.append(("<%s>" % w, els))
    whole = tuple(closure([g, s], n))
    if whole not in seen:
        out.append(("<g,s>", whole))
    return out


def cells_from_orbits(orbs, mode, c):
    """Build coordinate cells as unions of c orbit-cosets, per the declared
    mode.  The canonical coset order is by minimum label."""
    M = len(orbs)
    cells = []
    if mode == "ALL":
        for combo in itertools.combinations(range(M), c):
            cells.append(frozenset().union(*[set(orbs[i]) for i in combo]))
    elif mode == "BLOCKWISE":
        i = 0
        while i < M:
            combo = list(range(i, min(i + c, M)))
            cells.append(frozenset().union(*[set(orbs[j]) for j in combo]))
            i += c
    elif mode == "SLIDING":
        for i in range(M):
            combo = [(i + k) % M for k in range(c)]
            cells.append(frozenset().union(*[set(orbs[j]) for j in combo]))
    else:
        raise GateFailure("undeclared mode " + mode)
    return cells


class Rule(object):
    def __init__(self, rid, klass, transport, hname, horder, c, mode):
        self.rid = rid
        self.klass = klass          # G0 | G1 | G2 | G3-ORBITS | G3-UNIONS
        self.transport = transport  # T7 | T4
        self.hname = hname
        self.horder = horder
        self.c = c                  # None for orbit rules
        self.mode = mode            # None for orbit rules

    def coord(self):
        return (self.klass, self.transport, self.hname, self.horder,
                -1 if self.c is None else self.c,
                "-" if self.mode is None else self.mode)


def enumerate_grid(transports):
    """PRIMARY enumeration of the declared grid."""
    rules = []
    for tname, td in transports.items():
        g, s, n = td["gamma"], td["sigma"], 8
        lat = cyclic_subgroups(g, n)
        gname = "C%d" % perm_order(g)
        # G0 -- the null: cells are the <gamma>-orbits
        rules.append(Rule(None, "G0", tname, gname, perm_order(g), None, None))
        # G1 -- H-orbits for every PROPER subgroup H < <gamma>
        for hname, els in lat:
            if len(els) == perm_order(g):
                continue
            rules.append(Rule(None, "G1", tname, hname, len(els), None, None))
        # G2 -- unions of c >= 2 H-cosets with c*|H| < block size
        for hname, els in lat:
            h = len(els)
            for c in range(2, BLOCK_SIZE_DECLARED):
                if c * h >= BLOCK_SIZE_DECLARED:
                    continue
                for mode in MODES:
                    rules.append(Rule(None, "G2", tname, hname, h, c, mode))
        # G3 -- the G1/G2 constructions with cells taken from <gamma,Sigma>
        slat = declared_sigma_lattice(g, s, n)
        whole = len(closure([g, s], n))
        for hname, els in slat:
            if len(els) == whole:
                continue
            rules.append(Rule(None, "G3-ORBITS", tname, hname, len(els), None, None))
        for hname, els in slat:
            h = len(els)
            for c in range(2, BLOCK_SIZE_DECLARED):
                if c * h >= BLOCK_SIZE_DECLARED:
                    continue
                for mode in MODES:
                    rules.append(Rule(None, "G3-UNIONS", tname, hname, h, c, mode))
    if MUTANT == "grid-drop":
        rules = [r for r in rules
                 if not (r.klass == "G2" and r.transport == "T7"
                         and r.c == 4 and r.mode == "SLIDING")]
    for i, r in enumerate(rules):
        r.rid = "R%03d" % (i + 1)
    return rules


def expected_grid_coords(transports):
    """INDEPENDENT comparator for the grid cell-completeness gate (RUNBOOK
    section 13 addendum, v13 #234 / section 14 addendum, v13 #219).  Built by
    divisor arithmetic from the declarations, touching NO function used by the
    primary enumeration except the group primitives."""
    want = set()
    for tname, td in transports.items():
        g, s, n = td["gamma"], td["sigma"], 8
        N = perm_order(g)
        want.add(("G0", tname, "C%d" % N, N, -1, "-"))
        for d in divisors(N):
            order_h = N // d
            hname = "C%d" % order_h
            if order_h != N:
                want.add(("G1", tname, hname, order_h, -1, "-"))
            for c in range(2, BLOCK_SIZE_DECLARED):
                if c * order_h < BLOCK_SIZE_DECLARED:
                    for mode in MODES:
                        want.add(("G2", tname, hname, order_h, c, mode))
        seen_els = {}
        names = []
        for w in SIGMA_WORDS:
            p = word_perm(w, g, s, n)
            els = tuple(closure([p], n))
            if els not in seen_els:
                seen_els[els] = "<%s>" % w
                names.append(("<%s>" % w, len(els)))
        whole_els = tuple(closure([g, s], n))
        if whole_els not in seen_els:
            names.append(("<g,s>", len(whole_els)))
        W = len(whole_els)
        for hname, order_h in names:
            if order_h != W:
                want.add(("G3-ORBITS", tname, hname, order_h, -1, "-"))
            for c in range(2, BLOCK_SIZE_DECLARED):
                if c * order_h < BLOCK_SIZE_DECLARED:
                    for mode in MODES:
                        want.add(("G3-UNIONS", tname, hname, order_h, c, mode))
    return want


def rule_cells_on_block(rule, transports):
    """The rule's coordinate cells on the canonical 8-label block.  At B2 the
    rule is applied BLOCK-LOCALLY: these cells are copied into every block and
    the basepoint lies in no cell (the R1 block-local convention, declared)."""
    td = transports[rule.transport]
    g, s, n = td["gamma"], td["sigma"], 8
    if rule.klass in ("G0", "G1", "G2"):
        lat = dict(cyclic_subgroups(g, n))
        if rule.klass == "G0":
            els = tuple(closure([g], n))
        else:
            els = lat[rule.hname]
    else:
        slat = dict(declared_sigma_lattice(g, s, n))
        els = slat[rule.hname]
    orbs = orbits_of(els, tuple(range(n)))
    if rule.klass in ("G0", "G1", "G3-ORBITS"):
        cells = [frozenset(o) for o in orbs]
    else:
        mode = rule.mode
        if MUTANT == "locality-erase" and mode == "SLIDING":
            mode = "BLOCKWISE"
        cells = cells_from_orbits(orbs, mode, rule.c)
    # canonical, deduplicated
    uniq = sorted(set(cells), key=lambda cc: (min(cc), sorted(cc)))
    return uniq, orbs


def cells_on_arena(rule, arena, transports):
    block_cells, orbs = rule_cells_on_block(rule, transports)
    out = []
    for b, blk in enumerate(arena.blocks):
        off = b * BLOCK_SIZE_DECLARED
        for cc in block_cells:
            out.append(frozenset(x + off for x in cc))
    return sorted(set(out), key=lambda cc: (min(cc), sorted(cc))), block_cells, orbs


# ----------------------------------------------------------------------------
# 6.  The drawing relation (identical to R1's) and THEOREM R2-A
# ----------------------------------------------------------------------------

def drawn_by_definition(T, labels):
    """(a,b) is drawn iff EXACTLY ONE transport element carries a -> b.
    Brute force over the group: the definitional route."""
    lab = list(labels)
    cnt = {}
    for p in T:
        for a in lab:
            b = p[a]
            if b != a and b in labels:
                cnt[(a, b)] = cnt.get((a, b), 0) + 1
    return set(k for k, v in cnt.items() if v == 1)


def drawn_by_theorem(T, labels):
    """THEOREM R2-A (generalised to any transport group T, proved in the
    paper): (a,b) is drawn iff b lies in a's orbit AND that orbit is REGULAR,
    |orbit(a)| = |T|.  The route through orbits and stabilisers."""
    orbs = orbits_of(T, labels)
    out = set()
    for o in orbs:
        regular = (len(o) == len(T))
        if MUTANT == "orbit-corrupt":
            regular = (len(o) >= 2)
        if regular:
            for a in o:
                for b in o:
                    if a != b:
                        out.add((a, b))
    return out, orbs


def drawn_map(T, a, b):
    """The unique transport element carrying a -> b (defined exactly on drawn
    pairs)."""
    hits = [p for p in T if p[a] == b]
    if len(hits) != 1:
        raise GateFailure("drawn_map called off the drawn relation")
    return hits[0]


# ----------------------------------------------------------------------------
# 7.  F_2 linear algebra with a gated cache
# ----------------------------------------------------------------------------

_RANK_CACHE = {}
_CACHE_STATS = {"hits": 0, "misses": 0}


def f2_rank(rows, fresh=False):
    """Rank over F_2 of a list of int bitmasks.  `fresh=True` bypasses the
    cache entirely (RUNBOOK section 14 addendum, v13 #185: a self-test that
    reaches its quantity through the memo tests the cache, not the quantity)."""
    key = tuple(rows)
    if not fresh:
        if key in _RANK_CACHE:
            _CACHE_STATS["hits"] += 1
            return _RANK_CACHE[key]
        _CACHE_STATS["misses"] += 1
    piv = {}
    r = 0
    for row in rows:
        cur = row
        while cur:
            hb = cur.bit_length() - 1
            if hb in piv:
                cur ^= piv[hb]
            else:
                piv[hb] = cur
                r += 1
                break
    if not fresh:
        _RANK_CACHE[key] = r
    return r


def union_find_components(vertices, edges):
    parent = {v: v for v in vertices}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for a, b in edges:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb
    comps = {}
    for v in vertices:
        comps.setdefault(find(v), []).append(v)
    return sorted([tuple(sorted(c)) for c in comps.values()],
                  key=lambda c: (-len(c), c[0]))


# ----------------------------------------------------------------------------
# 8.  Per-rule measurement -- THE LOCALITY CENSUS
# ----------------------------------------------------------------------------

def measure_rule(rule, arena, transports, scramble=False):
    cells, block_cells, orbs = cells_on_arena(rule, arena, transports)
    T = arena.T
    labels = arena.labels

    global_theorem, tor = drawn_by_theorem(T, labels)
    global_def = drawn_by_definition(T, labels)

    # --- the rule's drawn relation: co-celled AND globally drawn ------------
    simple = set()
    for cc in cells:
        cl = sorted(cc)
        for i in range(len(cl)):
            for j in range(i + 1, len(cl)):
                a, b = cl[i], cl[j]
                if (a, b) in global_theorem:
                    simple.add((a, b))
    # independent route: apply the DEFINITION inside each cell
    simple_route2 = set()
    for cc in cells:
        for a in sorted(cc):
            for b in sorted(cc):
                if a < b and (a, b) in global_def and (b, a) in global_def:
                    simple_route2.add((a, b))
    if MUTANT == "census-corrupt" and rule.klass == "G2" and rule.mode == "SLIDING" \
            and rule.c == 3 and arena.name == "B":
        simple = set(list(sorted(simple))[:-1])

    edges = sorted(simple)
    refuses = (len(edges) == 0)
    if MUTANT == "refuses-skip" and refuses:
        return None

    comps = union_find_components(labels, edges)
    # route 2 for b0: V - rank(d1) over F_2
    idx = {v: i for i, v in enumerate(labels)}
    d1_rows = [(1 << idx[a]) | (1 << idx[b]) for a, b in edges]
    b0_rank_route = len(labels) - f2_rank(d1_rows)

    eset = set(edges)
    per_comp = []
    any_noncomplete = False
    tot_pairs = 0
    for c in comps:
        k = len(c)
        pairs = k * (k - 1) // 2
        tot_pairs += pairs
        got = 0
        for i in range(k):
            for j in range(i + 1, k):
                if (c[i], c[j]) in eset:
                    got += 1
        complete = (got == pairs)
        if not complete:
            any_noncomplete = True
        cyc = got - k + 1
        per_comp.append({"size": k, "edges": got, "pairs": pairs,
                         "complete": complete, "b1_graph": cyc,
                         "members": list(c)})
    if MUTANT == "complete-flip" and rule.klass == "G2" and rule.mode == "SLIDING" \
            and rule.c == 2 and arena.name == "B":
        for c in per_comp:
            c["complete"] = not c["complete"]
        any_noncomplete = not any_noncomplete
    if MUTANT == "locality-inject" and rule.klass == "G0" and arena.name == "B":
        any_noncomplete = True
        if per_comp:
            per_comp[0]["complete"] = False

    completeness = None if tot_pairs == 0 else Fraction(len(edges), tot_pairs)

    # --- N, the coordinate-resolved nerve (I3's convention, reimplemented) --
    onecells = []          # (a, b, cell_index)
    for ci, cc in enumerate(cells):
        cl = sorted(cc)
        for i in range(len(cl)):
            for j in range(i + 1, len(cl)):
                if (cl[i], cl[j]) in eset:
                    onecells.append((cl[i], cl[j], ci))
    oc_index = {oc: i for i, oc in enumerate(onecells)}
    twocells = []
    for ci, cc in enumerate(cells):
        cl = sorted(cc)
        for tri in itertools.combinations(cl, 3):
            a, b, c3 = tri
            if (a, b) in eset and (b, c3) in eset and (a, c3) in eset:
                twocells.append((a, b, c3, ci))
    # deduplicate to geometric edge-triples (I3's convention)
    seen_tri = set()
    tri_uniq = []
    for (a, b, c3, ci) in twocells:
        key = (oc_index[(a, b, ci)], oc_index[(b, c3, ci)], oc_index[(a, c3, ci)])
        if key in seen_tri:
            continue
        seen_tri.add(key)
        tri_uniq.append((a, b, c3, ci))
    twocells = tri_uniq

    # coherence: the three drawn maps compose to the identity
    coh = []
    for (a, b, c3, ci) in twocells:
        m_ab = drawn_map(T, a, b)
        m_bc = drawn_map(T, b, c3)
        m_ca = drawn_map(T, c3, a)
        if scramble:
            s_ab = ((a + 1) * (b + 2)) % max(2, len(T))
            s_bc = ((b + 1) * (c3 + 2)) % max(2, len(T))
            if MUTANT == "scramble-inert":
                s_ab = 0
                s_bc = 0
            m_ab = compose(power(arena.gamma, s_ab, arena.n), m_ab)
            m_bc = compose(power(arena.gamma, s_bc, arena.n), m_bc)
        if compose(m_ca, compose(m_bc, m_ab)) == ident(arena.n):
            coh.append((a, b, c3, ci))

    E_N = len(onecells)
    F_N = len(twocells)
    F_COH = len(coh)

    def betti(twoset):
        rows2 = []
        for (a, b, c3, ci) in twoset:
            m = 0
            for pair in ((a, b), (b, c3), (a, c3)):
                m |= 1 << oc_index[(pair[0], pair[1], ci)]
            rows2.append(m)
        r2 = f2_rank(rows2)
        r1 = f2_rank([(1 << idx[a]) | (1 << idx[b]) for (a, b, ci) in onecells])
        return {"b0": len(labels) - r1,
                "b1": len(onecells) - r1 - r2,
                "b2": len(twoset) - r2,
                "rank_d1": r1, "rank_d2": r2}

    bN = betti(twocells)
    bC = betti(coh)

    ncoh_per_incidence = None if E_N == 0 else Fraction(F_COH, E_N)
    ncoh_per_pair = None if len(edges) == 0 else Fraction(F_COH, len(edges))
    b2_density = None if F_COH == 0 else Fraction(bC["b2"], F_COH)

    return {
        "rid": rule.rid, "coord": rule.coord(), "arena": arena.name,
        "cells": len(cells), "cell_sizes": sorted([len(c) for c in cells]),
        "orbits_on_block": [list(o) for o in orbs],
        "regular_orbits": [list(o) for o in tor if len(o) == len(T)],
        "refuses": refuses,
        "edges": len(edges), "edge_list": [list(e) for e in edges],
        "components": len(comps),
        "component_sizes": sorted([len(c) for c in comps], reverse=True),
        "b0_route2": b0_rank_route,
        "per_component": per_comp,
        "any_noncomplete": any_noncomplete,
        "completeness": completeness,
        "E_N": E_N, "F_N": F_N, "F_COH": F_COH,
        "betti_N": bN, "betti_COH": bC,
        "ncoh_density_per_incidence": ncoh_per_incidence,
        "ncoh_density_per_pair": ncoh_per_pair,
        "b2_density": b2_density,
        "b2_density_undefined_reason": None if F_COH else "F_COH=0 -- no coherent 2-cell",
        "_onecells": onecells, "_twocells": twocells, "_coh": coh,
        "_cells": cells, "_oc_index": oc_index, "_edges": eset,
        "_route2_edges": simple_route2, "_global_def": global_def,
        "_global_thm": global_theorem, "_labels": labels,
    }


# ----------------------------------------------------------------------------
# 9.  The ported standards (I3's definitions, reimplemented -- import nothing)
# ----------------------------------------------------------------------------

def standards(m):
    """dimprofile / star / link, per I3 section 4.1, at every chart.
    dimprofile is tagged EXTENSIVE-EXCLUDED: I3 proved the estimator extensive
    and R0 excludes it as an intensive candidate; it is DISCLOSED, never used
    as an invariant."""
    labels = m["_labels"]
    cells = m["_cells"]
    eset = m["_edges"]
    onecells = m["_onecells"]
    twocells = m["_twocells"]

    dimprofile = {}
    for X in labels:
        prof = []
        for cc in cells:
            if X not in cc:
                prof.append(-1)
                continue
            sub = [(a, b) for (a, b) in eset if a in cc and b in cc]
            comps = union_find_components(sorted(cc), sub)
            mine = [c for c in comps if X in c][0]
            prof.append(len(mine) - 1 if len(mine) > 1 else -1)
        dimprofile[X] = tuple(prof)

    # independent comparator for the per-cell dimension: a component census run
    # from the PAIR TABLE alone, never touching the loop above
    dim_route2 = {}
    for X in labels:
        prof = []
        for cc in cells:
            if X not in cc:
                prof.append(-1)
                continue
            reach = {X}
            frontier = [X]
            while frontier:
                y = frontier.pop()
                for (a, b) in eset:
                    if a in cc and b in cc:
                        if a == y and b not in reach:
                            reach.add(b)
                            frontier.append(b)
                        if b == y and a not in reach:
                            reach.add(a)
                            frontier.append(a)
            prof.append(len(reach) - 1 if len(reach) > 1 else -1)
        dim_route2[X] = tuple(prof)

    starE = {X: 0 for X in labels}
    starF = {X: 0 for X in labels}
    for (a, b, ci) in onecells:
        starE[a] += 1
        starE[b] += 1
    for (a, b, c3, ci) in twocells:
        starF[a] += 1
        starF[b] += 1
        starF[c3] += 1

    link = {}
    for X in labels:
        adj = sorted(set([b for (a, b, ci) in onecells if a == X]
                         + [a for (a, b, ci) in onecells if b == X]))
        ledges = []
        for (a, b, c3, ci) in twocells:
            tri = (a, b, c3)
            if X in tri:
                others = tuple(sorted([t for t in tri if t != X]))
                ledges.append(others)
        lV = len(adj)
        lE = len(ledges)
        comps = union_find_components(adj, ledges) if adj else []
        lb0 = len(comps)
        lb1 = lE - lV + lb0
        link[X] = (lV, lE, lb0, lb1)

    charts_with_links = [X for X in labels if starE[X] > 0]
    every_circle = all(link[X][0] == link[X][1] and link[X][2] == 1
                       and link[X][3] == 1 for X in charts_with_links) \
        if charts_with_links else False
    profiles = set((dimprofile[X], (starE[X], starF[X]), link[X])
                   for X in charts_with_links)
    return {
        "dimprofile": {str(X): list(dimprofile[X]) for X in labels},
        "dimprofile_route2_agrees": all(dimprofile[X] == dim_route2[X] for X in labels),
        "dimprofile_status": "EXTENSIVE-EXCLUDED (I3 / R0 row I3)",
        "star": {str(X): [starE[X], starF[X]] for X in labels},
        "link": {str(X): list(link[X]) for X in labels},
        "charts_with_links": len(charts_with_links),
        "distinct_readings": len(profiles),
        "reading": "CONSISTENT" if len(profiles) == 1 else "INCONSISTENT",
        "every_link_is_a_circle": every_circle,
        "links_that_are_circles": len([X for X in charts_with_links
                                       if link[X][0] == link[X][1]
                                       and link[X][2] == 1 and link[X][3] == 1]),
        "sum_starE": sum(starE.values()), "sum_starF": sum(starF.values()),
        "local_dimensions_realised": sorted(set(
            v for X in labels for v in dimprofile[X] if v >= 0)),
    }


def ported_standard_controls():
    """I3's declared controls, rebuilt here so the standards' instrument is
    known to be able to SEE a sphere, a torus, and a pinch point.  The
    standards are PORTED AS DISCLOSURES: nothing in this unit claims the
    measured objects are of any particular geometric type."""
    out = {}

    def complexes(name, V, F):
        E = set()
        for f in F:
            for pair in itertools.combinations(sorted(f), 2):
                E.add(pair)
        E = sorted(E)
        idx = {v: i for i, v in enumerate(V)}
        oc_index = {(a, b, 0): i for i, (a, b) in enumerate(E)}
        onecells = [(a, b, 0) for (a, b) in E]
        twocells = [(f[0], f[1], f[2], 0) for f in [tuple(sorted(x)) for x in F]]
        rows2 = []
        for (a, b, c3, ci) in twocells:
            mm = 0
            for pair in ((a, b), (b, c3), (a, c3)):
                mm |= 1 << oc_index[(pair[0], pair[1], 0)]
            rows2.append(mm)
        r2 = f2_rank(rows2)
        r1 = f2_rank([(1 << idx[a]) | (1 << idx[b]) for (a, b) in E])
        link = {}
        for X in V:
            adj = sorted(set([b for (a, b) in E if a == X] + [a for (a, b) in E if b == X]))
            ledges = []
            for (a, b, c3, ci) in twocells:
                tri = (a, b, c3)
                if X in tri:
                    ledges.append(tuple(sorted([t for t in tri if t != X])))
            comps = union_find_components(adj, ledges) if adj else []
            link[X] = (len(adj), len(ledges), len(comps),
                       len(ledges) - len(adj) + len(comps))
        out[name] = {
            "V": len(V), "E": len(E), "F": len(twocells),
            "b0": len(V) - r1, "b1": len(E) - r1 - r2, "b2": len(twocells) - r2,
            "chi": len(V) - len(E) + len(twocells),
            "distinct_link_profiles": sorted(set(link.values())),
            "every_link_is_a_circle": all(l[0] == l[1] and l[2] == 1 and l[3] == 1
                                          for l in link.values()),
        }

    complexes("the boundary of a tetrahedron (a 2-sphere)", [0, 1, 2, 3],
              [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)])
    tor_V = list(range(9))
    tor_F = []
    for i in range(3):
        for j in range(3):
            a = 3 * i + j
            b = 3 * i + (j + 1) % 3
            c = 3 * ((i + 1) % 3) + j
            d = 3 * ((i + 1) % 3) + (j + 1) % 3
            tor_F.append((a, b, d))
            tor_F.append((a, d, c))
    complexes("a 9-vertex torus", tor_V, tor_F)
    complexes("two tetrahedra sharing one vertex (a pinch point)",
              [0, 1, 2, 3, 4, 5, 6],
              [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3),
               (0, 4, 5), (0, 4, 6), (0, 5, 6), (4, 5, 6)])
    return out


# ----------------------------------------------------------------------------
# 10.  Verdict derivation -- inside a gate, rebuilt segment by segment
# ----------------------------------------------------------------------------

def build_verdict(payload, swap_pairing=False):
    """Assemble the verdict string from the measured payload.  Returns
    (head, [(segment_name, segment_text), ...], full_string)."""
    loc = payload["locality_rules"]
    segs = []
    if loc:
        head = "R2-LOCALITY-AT"
        segs.append(("RULES", "RULES=%d-OF-%d:%s" %
                     (len(loc), payload["grid_size"], ",".join(loc))))
    else:
        head = "R2-NO-LOCALITY-IN-THE-DECLARED-GRID"
        segs.append(("RULES", "RULES=0-OF-%d" % payload["grid_size"]))
    segs.append(("GRID", "GRID=" + payload["grid_signature"]))
    segs.append(("MECHANISM", "MECHANISM=" + payload["mechanism"]))
    segs.append(("COMPONENTS", "COMPONENTS=" + payload["component_signature"]))
    segs.append(("STANDARDS", "STANDARDS=" + payload["standards_signature"]))
    segs.append(("B2", "B2-PERSISTENCE=" + payload["b2_signature"]))
    segs.append(("NULL", "NULL=" + payload["null_signature"]))
    segs.append(("REFUSES", "REFUSES=%d-OF-%d" %
                 (payload["refuses"], payload["grid_size"])))
    segs.append(("CONSTANTS", "BLOCK-CONSTANTS=" + payload["constants_signature"]))
    if swap_pairing and len(segs) >= 3:
        a, b = segs[1], segs[2]
        segs[1] = (a[0], a[1].split("=")[0] + "=" + b[1].split("=", 1)[1])
        segs[2] = (b[0], b[1].split("=")[0] + "=" + a[1].split("=", 1)[1])
    full = head + "<" + "|".join(s[1] for s in segs) + ">"
    return head, segs, full


# ----------------------------------------------------------------------------
# 11.  THE DELIVERY PIPELINE
# ----------------------------------------------------------------------------

def run():
    R = {}                      # THE GATED OBJECT.  Everything renders from R.

    # -- G-FLOATGUARD ---------------------------------------------------------
    off = float_guard()
    gate("G-FLOATGUARD",
         "no float literal, no true division, no float/math/random/numpy/"
         "statistics/decimal anywhere in this source",
         len(off) == 0, {"offences": off[:8], "count": len(off)})

    # -- anchors --------------------------------------------------------------
    n_anchor = verify_anchors()
    gate("G-ANCHOR-COUNT", "every declared R0/pin anchor was evaluated",
         len(ANCHORS) == n_anchor and all(a["ok"] for a in ANCHORS),
         {"anchors": len(ANCHORS)})
    R["anchors"] = [dict((k, v) for k, v in a.items()) for a in ANCHORS]

    i6 = read_json("v13/code/tb3_third_base_receipt.json")
    i3 = read_json("v13/code/top_topology_receipt.json")

    # -- the arena declarations, read out of I6 -------------------------------
    gamma7 = tuple(i6["tables"]["the_ladder"]["the_embedding"]["the_witness_system_part"])
    gamma4 = tuple(i6["tables"]["ord_census"]["lex_first_Q_per_order"]["4"])
    sigma = tuple(i6["tables"]["arena"]["the_declared_completion_transposition"])
    blocksize = i6["tables"]["base_declaration"]["carrier"]["system_triple_dimension"]
    gate("G-BLOCKSIZE-FROM-I6",
         "the block size is READ from I6 (system_triple_dimension), not typed",
         blocksize == BLOCK_SIZE_DECLARED and len(gamma7) == blocksize
         and len(gamma4) == blocksize and len(sigma) == blocksize,
         {"i6_system_triple_dimension": blocksize})

    transports = {
        "T7": {"gamma": gamma7, "sigma": sigma,
               "source": "I6 tables.the_ladder.the_embedding."
                         "the_witness_system_part -- the x7=[A7:A6] embedding "
                         "witness, a 7-cycle on the seven non-zero labels",
               "sigma_source": "I6 tables.arena."
                               "the_declared_completion_transposition"},
        "T4": {"gamma": gamma4, "sigma": sigma,
               "source": "I6 tables.ord_census.lex_first_Q_per_order['4'] -- "
                         "the lex-first completion permutation at defect order 4",
               "sigma_source": "I6 tables.arena."
                               "the_declared_completion_transposition"},
    }
    for tn, td in transports.items():
        td["gamma_order"] = perm_order(td["gamma"])
        td["sigma_order"] = perm_order(td["sigma"])
        td["group_order"] = len(closure([td["gamma"]], 8))
        td["sigma_mixed_order"] = len(closure([td["gamma"], td["sigma"]], 8))
        td["lattice"] = [(nm, len(els)) for nm, els in
                         cyclic_subgroups(td["gamma"], 8)]
        td["sigma_lattice"] = [(nm, len(els)) for nm, els in
                               declared_sigma_lattice(td["gamma"], td["sigma"], 8)]

    GROUP_CAP = 10000
    gate("G-GROUP-CAP",
         "every declared group closure stays under the printed cap (no silent "
         "truncation)",
         all(td["sigma_mixed_order"] <= GROUP_CAP for td in transports.values()),
         {"cap": GROUP_CAP,
          "orders": dict((k, v["sigma_mixed_order"]) for k, v in transports.items())})

    B, B2 = build_arenas(gamma7, sigma)
    arenas7 = {"B": B, "B2": B2}
    B4, B24 = build_arenas(gamma4, sigma)
    arenas4 = {"B": B4, "B2": B24}
    ARENAS = {"T7": arenas7, "T4": arenas4}

    R["arena_declaration"] = {
        "B": {"labels": 8, "blocks": 1, "basepoint": None,
              "note": B.note},
        "B2": {"labels": 17, "blocks": 2, "basepoint": 16,
               "note": B2.note,
               "rule_application": "BLOCK-LOCAL: the rule's cells are copied "
                                   "into each block; the basepoint lies in no cell"},
        "transports": dict((k, {"gamma": list(v["gamma"]), "sigma": list(v["sigma"]),
                                "gamma_order": v["gamma_order"],
                                "sigma_order": v["sigma_order"],
                                "drawing_group_order": v["group_order"],
                                "sigma_mixed_group_order": v["sigma_mixed_order"],
                                "cyclic_lattice": v["lattice"],
                                "declared_sigma_lattice": v["sigma_lattice"],
                                "source": v["source"],
                                "sigma_source": v["sigma_source"]})
                          for k, v in transports.items()),
        "declared_modes": list(MODES),
        "declared_sigma_words": list(SIGMA_WORDS),
        "drawing_relation": "drawn iff a UNIQUE transport element carries "
                            "a -> b (R1's relation verbatim); the drawing group "
                            "is <gamma>, fixed across the whole grid -- only "
                            "the declared cell structure varies",
        "coset_order_convention": "H-orbits ordered by minimum label; "
                                  "ALL = every c-subset, BLOCKWISE = disjoint "
                                  "consecutive windows, SLIDING = every cyclic "
                                  "window of length c",
    }
    gate("G-ARENA-DECL-MATCHED",
         "every declared arena coordinate is printed and matches its computed "
         "value (RUNBOOK section 15)",
         (R["arena_declaration"]["B"]["labels"] == B.n
          and R["arena_declaration"]["B2"]["labels"] == B2.n
          and B2.basepoint == 16
          and all(len(closure([transports[k]["gamma"]], 8))
                  == R["arena_declaration"]["transports"][k]["drawing_group_order"]
                  for k in transports)),
         {"B_n": B.n, "B2_n": B2.n})

    # -- THE GRID -------------------------------------------------------------
    rules = enumerate_grid(transports)
    got = set(r.coord() for r in rules)
    want = expected_grid_coords(transports)
    gate("G-GRID-CELL-COMPLETE",
         "the enumerated grid equals an INDEPENDENTLY rebuilt coordinate set "
         "(a dropped (H,c,mode) cell is fatal; RUNBOOK #234/#219)",
         got == want,
         {"enumerated": len(got), "expected": len(want),
          "missing": sorted(want - got)[:4], "extra": sorted(got - want)[:4]})
    gate("G-GRID-NO-DUPLICATES", "every grid coordinate occurs exactly once",
         len(got) == len(rules), {"coords": len(got), "rules": len(rules)})

    by_class = {}
    for r in rules:
        by_class[(r.transport, r.klass)] = by_class.get((r.transport, r.klass), 0) + 1
    R["grid"] = {
        "size": len(rules),
        "by_transport_and_class": dict(("%s/%s" % k, v)
                                       for k, v in sorted(by_class.items())),
        "coordinates": [list(r.coord()) + [r.rid] for r in rules],
        "cap_declared": None,
        "truncated": False,
    }
    gate("G-GRID-NOT-TRUNCATED",
         "no silent cap: the grid is enumerated exhaustively from the "
         "declarations",
         R["grid"]["truncated"] is False and R["grid"]["size"] == len(want),
         {"size": R["grid"]["size"]})

    # -- THE LOCALITY CENSUS --------------------------------------------------
    census = {}
    for r in rules:
        for aname in ("B", "B2"):
            m = measure_rule(r, ARENAS[r.transport][aname], transports)
            if m is None:
                continue
            census[(r.rid, aname)] = m
    gate("G-EVERY-RULE-RECORDED",
         "every grid rule is recorded at both arenas -- a rule that draws "
         "nothing is REFUSES, never skipped",
         len(census) == 2 * len(rules),
         {"recorded": len(census), "expected": 2 * len(rules)})

    # two-route agreement on the drawn relation (THEOREM R2-A at my actions)
    bad = [k for k, m in census.items() if m["_edges"] != m["_route2_edges"]]
    gate("G-DRAW-TWO-ROUTES",
         "the orbit/stabiliser route (THEOREM R2-A) and the definitional "
         "brute-force route agree on the drawn relation at every rule and arena",
         len(bad) == 0, {"disagreements": len(bad), "sample": bad[:3]})

    # R2-A exhaustively at this family's actions
    r2a_actions = 0
    r2a_counterex = 0
    for tname, td in transports.items():
        for aname, A in ARENAS[tname].items():
            for hname, els in list(cyclic_subgroups(td["gamma"], 8)):
                lifted = tuple(closure(
                    [lift_block_perm(e, len(A.blocks), A.n) for e in els], A.n))
                thm, _ = drawn_by_theorem(lifted, A.labels)
                dfn = drawn_by_definition(lifted, A.labels)
                r2a_actions += 1
                if thm != dfn:
                    r2a_counterex += 1
    gate("G-R2A-AT-THIS-UNITS-ACTIONS",
         "THEOREM R2-A holds at every cyclic action this unit uses "
         "(drawn <=> regular orbit); zero counterexamples",
         r2a_counterex == 0 and r2a_actions > 0,
         {"actions": r2a_actions, "counterexamples": r2a_counterex})

    # and exhaustively over EVERY cyclic action on the block's label set
    sweep_actions = 0
    sweep_bad = 0
    eB = ident(BLOCK_SIZE_DECLARED)
    for p in itertools.permutations(range(BLOCK_SIZE_DECLARED)):
        Tp = [eB]
        cur = p
        while cur != eB:
            Tp.append(cur)
            cur = compose(p, cur)
        thm, _ = drawn_by_theorem(tuple(Tp), tuple(range(BLOCK_SIZE_DECLARED)))
        dfn = drawn_by_definition(tuple(Tp), tuple(range(BLOCK_SIZE_DECLARED)))
        sweep_actions += 1
        if thm != dfn:
            sweep_bad += 1
    gate("G-R2A-EXHAUSTIVE",
         "THEOREM R2-A holds at EVERY cyclic action on the block's 8 labels "
         "(one per permutation), zero counterexamples",
         sweep_bad == 0 and sweep_actions > 0,
         {"actions_swept": sweep_actions, "counterexamples": sweep_bad})
    R["r2a_verification"] = {
        "actions_this_unit_uses": r2a_actions,
        "counterexamples_at_this_units_actions": r2a_counterex,
        "cyclic_actions_swept_on_the_block": sweep_actions,
        "counterexamples_in_the_sweep": sweep_bad,
    }

    # the null: G0 must be clique-only
    g0 = [(k, m) for k, m in census.items() if m["coord"][0] == "G0"]
    g0_bad = [k for k, m in g0 if m["any_noncomplete"]]
    gate("G-R2A-NULL-CLIQUE-ONLY",
         "the G0 null (regular <gamma>-orbits) returns clique-only components "
         "at every transport and arena -- the R2-A theorem check",
         len(g0_bad) == 0 and len(g0) == 2 * len(transports),
         {"g0_rules": len(g0), "noncomplete": len(g0_bad)})

    # G1 and the orbit classes are structurally clique-only (measured, not assumed)
    orbit_rules = [(k, m) for k, m in census.items()
                   if m["coord"][0] in ("G0", "G1", "G3-ORBITS")]
    orbit_bad = [k for k, m in orbit_rules if m["any_noncomplete"]]
    gate("G-ORBIT-CLASSES-CLIQUE-ONLY",
         "every orbit-partition class (G0, G1, G3-ORBITS) returns clique-only "
         "components: disjoint cells cannot make a non-complete component",
         len(orbit_bad) == 0, {"rules": len(orbit_rules), "noncomplete": len(orbit_bad)})

    # component census by two independent routes
    comp_bad = [k for k, m in census.items() if m["components"] != m["b0_route2"]]
    gate("G-COMPONENTS-TWO-ROUTES",
         "b0 by union-find equals |V| - rank(d1) over F_2 at every rule and arena",
         len(comp_bad) == 0, {"disagreements": len(comp_bad)})

    # completeness by an independent route (edge count vs explicit pair scan)
    cbad = []
    for k, m in census.items():
        for c in m["per_component"]:
            scan = 0
            mem = c["members"]
            for i in range(len(mem)):
                for j in range(i + 1, len(mem)):
                    if (mem[i], mem[j]) in m["_edges"]:
                        scan += 1
            if (scan == c["pairs"]) != c["complete"]:
                cbad.append((k, c["size"]))
    gate("G-COMPLETENESS-TWO-ROUTES",
         "per-component completeness by stored edge count agrees with an "
         "explicit pair scan at every component of every rule",
         len(cbad) == 0, {"disagreements": len(cbad)})

    # coherence is forced (a disclosure per #208), and verified
    incoh = [k for k, m in census.items() if m["F_COH"] != m["F_N"]]
    gate("G-COHERENCE-FORCED",
         "every 2-cell of N is coherent at every rule and arena: a drawn pair "
         "forces a trivial stabiliser, so the three drawn maps compose to the "
         "identity (FORCED -- entered as a disclosure, #208)",
         len(incoh) == 0, {"rules_with_incoherent_2cells": len(incoh)})

    # the UNDEFINED path is LIVE (R1's dead-code finding, repaired at birth)
    undef = [k for k, m in census.items() if m["b2_density"] is None]
    gate("G-UNDEFINED-PATH-LIVE",
         "the b2-density UNDEFINED path is reached by shipped inputs (F_COH=0) "
         "and is recorded with its reason -- not dead code",
         len(undef) > 0 and all(census[k]["b2_density_undefined_reason"]
                                for k in undef),
         {"rules_hitting_undefined": len(undef)})

    # -- the locality census result ------------------------------------------
    locality_B = sorted([m["rid"] for k, m in census.items()
                         if k[1] == "B" and m["any_noncomplete"]])
    locality_B2 = sorted([m["rid"] for k, m in census.items()
                          if k[1] == "B2" and m["any_noncomplete"]])
    refuses_B = sorted([m["rid"] for k, m in census.items()
                        if k[1] == "B" and m["refuses"]])

    R["census_rows"] = []
    for r in rules:
        m = census[(r.rid, "B")]
        m2 = census[(r.rid, "B2")]
        R["census_rows"].append({
            "rid": r.rid, "coord": list(r.coord()),
            "cells": m["cells"], "edges": m["edges"],
            "components": m["components"],
            "component_sizes": m["component_sizes"],
            "completeness": m["completeness"],
            "status": ("REFUSES" if m["refuses"] else
                       ("NON-COMPLETE" if m["any_noncomplete"] else "clique-only")),
            "noncomplete_components": [
                {"size": c["size"], "edges": c["edges"], "pairs": c["pairs"],
                 "b1_graph": c["b1_graph"], "members": c["members"]}
                for c in m["per_component"] if not c["complete"]],
            "B2_status": ("REFUSES" if m2["refuses"] else
                          ("NON-COMPLETE" if m2["any_noncomplete"]
                           else "clique-only")),
            "B2_completeness": m2["completeness"],
        })

    if MUTANT == "census-row-corrupt":
        R["census_rows"][0]["component_sizes"] = \
            list(R["census_rows"][0]["component_sizes"]) + [99]

    R["locality_census"] = {
        "rules_measured": len(rules),
        "locality_bearing_at_B": locality_B,
        "locality_bearing_at_B2": locality_B2,
        "refusing_at_B": refuses_B,
        "count_locality_B": len(locality_B),
        "count_locality_B2": len(locality_B2),
        "count_refuses_B": len(refuses_B),
        "criterion": "locality exists at a rule iff SOME connected component "
                     "of that rule's overlap graph is NOT complete "
                     "(the R1 adjudication's criterion, section 6)",
    }

    # -- the standards at locality-bearing rules ------------------------------
    std = {}
    for rid in locality_B:
        m = census[(rid, "B")]
        std[rid] = standards(m)
    R["controls_ported_standards"] = ported_standard_controls()
    ctrl = R["controls_ported_standards"]
    gate("G-STANDARDS-CONTROLS",
         "the reimplemented standards see I3's controls: the 2-sphere and the "
         "2-torus return every-link-a-circle, the pinch point does not",
         (ctrl["the boundary of a tetrahedron (a 2-sphere)"]["every_link_is_a_circle"]
          and ctrl["a 9-vertex torus"]["every_link_is_a_circle"]
          and not ctrl["two tetrahedra sharing one vertex (a pinch point)"]
          ["every_link_is_a_circle"]),
         {k: v["every_link_is_a_circle"] for k, v in ctrl.items()})
    gate("G-STANDARDS-CONTROL-BETTI",
         "the controls' Betti numbers reproduce I3's table exactly",
         (ctrl["the boundary of a tetrahedron (a 2-sphere)"]["b2"] == 1
          and ctrl["a 9-vertex torus"]["b1"] == 2
          and ctrl["a 9-vertex torus"]["b2"] == 1
          and ctrl["two tetrahedra sharing one vertex (a pinch point)"]["b2"] == 2),
         {k: [v["b0"], v["b1"], v["b2"]] for k, v in ctrl.items()})

    ebad = []
    for rid, s in std.items():
        m = census[(rid, "B")]
        if s["sum_starE"] != 2 * m["E_N"] or s["sum_starF"] != 3 * m["F_N"]:
            ebad.append(rid)
        if not s["dimprofile_route2_agrees"]:
            ebad.append(rid)
    gate("G-STANDARDS-IDENTITIES",
         "sum_v star_E(v) = 2|E(N)| and sum_v star_F(v) = 3|F(N)| at every "
         "rule where the standards are measured, and the per-cell dimension "
         "agrees with an independent component census",
         len(ebad) == 0 and len(std) == len(locality_B), {"failures": ebad[:4]})

    R["standards"] = {}
    for rid, s in std.items():
        m = census[(rid, "B")]
        nc = [c for c in m["per_component"] if not c["complete"]]
        charts = sorted(set([x for c in nc for x in c["members"]]))
        R["standards"][rid] = {
            "coord": list(m["coord"]),
            "noncomplete_component_charts": charts,
            "link_at_those_charts": dict((str(X), s["link"][str(X)]) for X in charts),
            "star_at_those_charts": dict((str(X), s["star"][str(X)]) for X in charts),
            "dimprofile_at_those_charts": dict((str(X), s["dimprofile"][str(X)])
                                               for X in charts),
            "dimprofile_status": s["dimprofile_status"],
            "local_dimensions_realised": s["local_dimensions_realised"],
            "reading": s["reading"],
            "distinct_readings": s["distinct_readings"],
            "charts_with_links": s["charts_with_links"],
            "every_link_is_a_circle": s["every_link_is_a_circle"],
            "links_that_are_circles": s["links_that_are_circles"],
        }

    # -- b1 per component at locality-bearing rules ---------------------------
    R["b1_per_component"] = {}
    for rid in locality_B:
        m = census[(rid, "B")]
        R["b1_per_component"][rid] = {
            "graph_cycle_rank_per_component":
                [[c["size"], c["edges"], c["b1_graph"]] for c in m["per_component"]],
            "b1_of_N": m["betti_N"]["b1"],
            "b1_of_N_coh": m["betti_COH"]["b1"],
            "b0_of_N": m["betti_N"]["b0"],
        }
    nontrivial_b1 = sorted([rid for rid in locality_B
                            if any(c["b1_graph"] > 0
                                   for c in census[(rid, "B")]["per_component"])])
    R["b1_nontrivial_at"] = nontrivial_b1

    # -- THE BLOCK CONSTANTS, B vs B2, both denominator conventions -----------
    consts = []
    for r in rules:
        mb = census[(r.rid, "B")]
        m2 = census[(r.rid, "B2")]
        consts.append({
            "rid": r.rid, "coord": list(r.coord()),
            "B": {"E_N": mb["E_N"], "edges": mb["edges"], "F": mb["F_N"],
                  "F_COH": mb["F_COH"], "b2_coh": mb["betti_COH"]["b2"],
                  "ncoh_per_incidence": mb["ncoh_density_per_incidence"],
                  "ncoh_per_pair": mb["ncoh_density_per_pair"],
                  "b2_density": mb["b2_density"]},
            "B2": {"E_N": m2["E_N"], "edges": m2["edges"], "F": m2["F_N"],
                   "F_COH": m2["F_COH"], "b2_coh": m2["betti_COH"]["b2"],
                   "ncoh_per_incidence": m2["ncoh_density_per_incidence"],
                   "ncoh_per_pair": m2["ncoh_density_per_pair"],
                   "b2_density": m2["b2_density"]},
            "densities_constant_B_to_B2":
                (mb["ncoh_density_per_incidence"] == m2["ncoh_density_per_incidence"]
                 and mb["ncoh_density_per_pair"] == m2["ncoh_density_per_pair"]
                 and mb["b2_density"] == m2["b2_density"]),
            "additives_double":
                (m2["E_N"] == 2 * mb["E_N"] and m2["F_N"] == 2 * mb["F_N"]
                 and m2["edges"] == 2 * mb["edges"]),
        })
    if MUTANT == "table-corrupt":
        consts[0]["B"]["E_N"] = consts[0]["B"]["E_N"] + 1
    R["block_constants"] = consts
    gate("G-COPY-REDUCTION",
         "the per-block reduction is VERIFIED, not assumed: at every rule the "
         "additive counts at B2 are exactly twice B's and all three densities "
         "are unchanged (the copy-forcing theorem's content at this scale)",
         all(c["additives_double"] and c["densities_constant_B_to_B2"]
             for c in consts),
         {"rules": len(consts),
          "additives_double": len([c for c in consts if c["additives_double"]]),
          "densities_constant": len([c for c in consts
                                     if c["densities_constant_B_to_B2"]])})

    # -- B2 persistence for locality-bearing rules ----------------------------
    persist = {}
    for rid in locality_B:
        mb, m2 = census[(rid, "B")], census[(rid, "B2")]
        ncb = len([c for c in mb["per_component"] if not c["complete"]])
        nc2 = len([c for c in m2["per_component"] if not c["complete"]])
        persist[rid] = {
            "noncomplete_components_B": ncb,
            "noncomplete_components_B2": nc2,
            "survives": m2["any_noncomplete"],
            "doubles": nc2 == 2 * ncb,
            "completeness_B": mb["completeness"],
            "completeness_B2": m2["completeness"],
            "completeness_unchanged": mb["completeness"] == m2["completeness"],
            "component_sizes_B": mb["component_sizes"],
            "component_sizes_B2": m2["component_sizes"],
        }
    R["b2_persistence"] = persist
    gate("G-B2-PERSISTENCE-MEASURED",
         "every locality-bearing rule is re-measured at B2 and its persistence "
         "recorded (survival is measured, never assumed)",
         len(persist) == len(locality_B), {"measured": len(persist)})

    # -- CONTROLS -------------------------------------------------------------
    # positive control: a hand-declared toy with KNOWN partial overlap
    toy_cells = [frozenset({1, 2, 3}), frozenset({3, 4, 5})]
    if MUTANT == "toy-broken":
        toy_cells = [frozenset({1, 2, 3}), frozenset({1, 2, 3})]
    toy_shared = sorted(set(toy_cells[0]) & set(toy_cells[1]))
    toyT = B.T
    toy_thm, _ = drawn_by_theorem(toyT, B.labels)
    toy_edges = sorted(set((a, b) for cc in toy_cells for a in sorted(cc)
                           for b in sorted(cc) if a < b and (a, b) in toy_thm))
    toy_comps = union_find_components(B.labels, toy_edges)
    toy_nc = []
    for c in toy_comps:
        k = len(c)
        got_e = len([1 for i in range(k) for j in range(i + 1, k)
                     if (c[i], c[j]) in set(toy_edges)])
        toy_nc.append({"size": k, "edges": got_e, "pairs": k * (k - 1) // 2,
                       "complete": got_e == k * (k - 1) // 2})
    toy_positive = any(not c["complete"] for c in toy_nc)
    R["positive_control"] = {
        "declaration": "two coset-union cells sharing exactly one label, "
                       "hand-declared OUTSIDE the grid (pin section 6)",
        "cells": [sorted(c) for c in toy_cells],
        "labels_shared_by_the_two_cells": toy_shared,
        "edges": len(toy_edges),
        "components": [dict((k2, v2) for k2, v2 in c.items()) for c in toy_nc],
        "returns_noncomplete": toy_positive,
    }
    gate("G-POSITIVE-CONTROL",
         "the hand-declared toy (two cells sharing exactly one label) returns "
         "a NON-COMPLETE component -- the criterion's instrument has teeth",
         toy_positive and len(toy_shared) == 1,
         {"shared": toy_shared, "noncomplete": toy_positive})

    # the modes must be genuinely different constructions
    mode_probe = []
    for r in rules:
        if r.mode != "SLIDING":
            continue
        twins = dict((x.mode, x) for x in rules
                     if x.klass == r.klass and x.transport == r.transport
                     and x.hname == r.hname and x.c == r.c)
        if len(twins) != len(MODES):
            continue
        sets = {}
        norb = None
        for mo, x in twins.items():
            cc_list, orbs_x = rule_cells_on_block(x, transports)
            norb = len(orbs_x)
            sets[mo] = sorted(sorted(cc) for cc in cc_list)
        if norb is None or norb <= r.c:
            continue
        mode_probe.append((r.rid, sets["SLIDING"] != sets["BLOCKWISE"],
                           sets["SLIDING"] != sets["ALL"],
                           sets["BLOCKWISE"] != sets["ALL"]))
    sliding_equals_all = [x[0] for x in mode_probe if not x[2]]
    gate("G-MODES-DISTINCT",
         "SLIDING and BLOCKWISE build different cell sets at every grid "
         "coordinate that declares both -- checked through the very function "
         "the rules use, so a mode collapse is fatal.  Where SLIDING and ALL "
         "coincide it is a MEASURED coincidence (it happens exactly at "
         "c = |orbits| - 1, where a cyclic window omits one coset) and is "
         "counted, not gated away.",
         len(mode_probe) > 0 and all(x[1] for x in mode_probe),
         {"probes": len(mode_probe),
          "sliding_equals_blockwise_at": [x[0] for x in mode_probe if not x[1]][:4],
          "sliding_equals_all_at": len(sliding_equals_all),
          "blockwise_equals_all_at": len([x[0] for x in mode_probe if not x[3]])})
    R["mode_probe"] = {
        "coordinates_probed": len(mode_probe),
        "sliding_equals_all_at": sliding_equals_all,
        "note": "a measured coincidence at c = |orbits| - 1",
    }

    # scramble control -- declared tested set, never selected by the verdict
    scr_set = sorted([r.rid for r in rules if census[(r.rid, "B")]["F_N"] > 0])
    moved, fixed = 0, 0
    for rid in scr_set:
        r = [x for x in rules if x.rid == rid][0]
        base = census[(rid, "B")]
        sc = measure_rule(r, ARENAS[r.transport]["B"], transports, scramble=True)
        if sc["F_COH"] != base["F_COH"]:
            moved += 1
        if (sc["component_sizes"] == base["component_sizes"]
                and sc["edges"] == base["edges"]
                and sc["any_noncomplete"] == base["any_noncomplete"]):
            fixed += 1
    R["scramble_control"] = {
        "tested_set": "every grid rule with F(N) > 0 -- fixed by declaration, "
                      "never selected by the verdicts under audit",
        "rules_tested": len(scr_set),
        "identification_measure_moved_at": moved,
        "component_census_unchanged_at": fixed,
    }
    gate("G-SCRAMBLE-CONTROL",
         "scrambling the drawn maps MOVES the identification-sensitive measure "
         "(coherent 2-cells) at a positive number of rules and FIXES the "
         "component census at every rule of the declared tested set",
         moved > 0 and fixed == len(scr_set),
         {"tested": len(scr_set), "moved": moved, "census_fixed": fixed})

    # symmetry self-test (RUNBOOK section 14, v13 #175) -- fresh evaluation
    _CACHE_STATS["selftest_fresh_calls"] = 0
    relabellings = [("gamma", gamma7), ("sigma", sigma),
                    ("gamma.sigma", compose(gamma7, sigma)),
                    ("wild=(01)(23)(45)(67)", (1, 0, 3, 2, 5, 4, 7, 6))]
    sym_rows = []
    probe_rules = [r for r in rules if r.transport == "T7"][:12]
    for nm, pi in relabellings:
        ok = True
        for r in probe_rules:
            m = census[(r.rid, "B")]
            cells = m["_cells"]
            new_cells = [frozenset(pi[x] for x in cc) for cc in cells]
            newT = tuple(sorted(compose(pi, compose(p, inverse(pi))) for p in B.T))
            thm, _ = drawn_by_theorem(newT, B.labels)
            e2 = sorted(set((min(pi[a], pi[b]), max(pi[a], pi[b]))
                            for cc in cells for a in sorted(cc) for b in sorted(cc)
                            if a < b and (a, b) in m["_edges"]))
            e3 = sorted(set((a, b) for cc in new_cells for a in sorted(cc)
                            for b in sorted(cc) if a < b and (a, b) in thm))
            comps2 = union_find_components(B.labels, e3)
            _CACHE_STATS["selftest_fresh_calls"] += 1
            f2_rank([(1 << a) | (1 << b) for a, b in e3], fresh=True)
            if e2 != e3 or sorted([len(c) for c in comps2], reverse=True) != \
                    m["component_sizes"]:
                ok = False
        sym_rows.append({"relabelling": nm, "census_invariant": ok})
    gate("G-SYMMETRY-SELFTEST",
         "the census is invariant under every declared relabelling of the "
         "arena (cells and transport conjugated together), evaluated FRESH "
         "with the memo bypassed",
         all(x["census_invariant"] for x in sym_rows)
         and _CACHE_STATS["selftest_fresh_calls"] > 0,
         {"relabellings": len(sym_rows),
          "fresh_calls": _CACHE_STATS["selftest_fresh_calls"]})
    R["symmetry_selftest"] = sym_rows

    gate("G-CACHE-EXERCISED",
         "the memo path is exercised on both branches (a zero-hit or "
         "zero-lookup cache gate is vacuous, RUNBOOK #219)",
         _CACHE_STATS["hits"] > 0 and _CACHE_STATS["misses"] > 0,
         dict(_CACHE_STATS))
    R["cache"] = dict(_CACHE_STATS)

    # boundary parity witness (RUNBOOK section 14 addendum, v13 #313)
    par_set = sorted([r.rid for r in rules
                      if any(len(cc) >= 3 for cc in census[(r.rid, "B")]["_cells"])])
    par_rows = []
    for rid in par_set:
        m_and = census[(rid, "B")]
        alt_tri = 0
        for ci, cc in enumerate(m_and["_cells"]):
            for tri in itertools.combinations(sorted(cc), 3):
                a, b, c3 = tri
                hits = len([1 for pp in ((a, b), (b, c3), (a, c3))
                            if pp in m_and["_edges"]])
                if hits > 0:
                    alt_tri += 1
        par_rows.append({"rule": rid, "two_cells_under_AND": m_and["F_N"],
                         "two_cells_under_OR": alt_tri,
                         "measured_delta": alt_tri - m_and["F_N"]})
    moved_par = [p for p in par_rows if p["measured_delta"] != 0]
    R["parity_witness"] = {
        "tested_set": "every grid rule at B with a cell of three or more "
                      "labels -- fixed by declaration",
        "rules_tested": len(par_rows),
        "rules_where_the_connective_matters": len(moved_par),
        "total_delta": sum(p["measured_delta"] for p in par_rows),
        "per_rule": par_rows,
    }
    gate("G-BOUNDARY-PARITY",
         "the Boolean connective at the 2-cell boundary is witnessed: over the "
         "declared tested set the alternative connective (any-pair-drawn "
         "instead of pairwise-drawn) has a non-zero measured delta at a "
         "positive number of rules, and every delta is printed",
         len(par_rows) > 0 and len(moved_par) > 0,
         {"tested": len(par_rows), "moved": len(moved_par),
          "total_delta": R["parity_witness"]["total_delta"]})

    # the alternative drawing-group reading, probed and disclosed
    altdraw = {}
    for tname, td in transports.items():
        Tsig = tuple(closure([td["gamma"], td["sigma"]], 8))
        d_sig = drawn_by_definition(Tsig, tuple(range(8)))
        altdraw[tname] = {"sigma_mixed_group_order": len(Tsig),
                          "pairs_drawn_if_the_drawing_group_were_it": len(d_sig)}
    R["alt_drawing_group_probe"] = {
        "note": "the pin fixes the drawing relation across the grid (only the "
                "cell structure varies); this probe records what would happen "
                "if <gamma,Sigma> were used as the DRAWING group instead",
        "per_transport": altdraw,
        "reason": "a drawn pair forces a trivial stabiliser, so |T| must divide "
                  "and equal an orbit size; |<gamma,Sigma>| exceeds the label "
                  "count at both transports, so nothing is drawn",
    }
    gate("G-ALT-DRAW-PROBE",
         "the alternative drawing-group reading is measured and recorded "
         "(it draws nothing at both transports)",
         all(v["pairs_drawn_if_the_drawing_group_were_it"] == 0
             for v in altdraw.values()), altdraw)

    # G3 with H=<e> must reproduce G1/G2 with the trivial subgroup: a free
    # cross-check between two independently-declared lattices
    dup_checked = 0
    dup_bad = 0
    for r in rules:
        if r.klass != "G3-UNIONS" or r.horder != 1:
            continue
        twin = [x for x in rules if x.klass == "G2" and x.transport == r.transport
                and x.horder == 1 and x.c == r.c and x.mode == r.mode]
        if not twin:
            continue
        dup_checked += 1
        if census[(r.rid, "B")]["edges"] != census[(twin[0].rid, "B")]["edges"]:
            dup_bad += 1
    gate("G-LATTICE-CROSSCHECK",
         "the Sigma-mixed lattice's trivial subgroup reproduces the cyclic "
         "lattice's trivial subgroup exactly (two independently declared "
         "lattices, same measured census)",
         dup_bad == 0 and dup_checked > 0,
         {"checked": dup_checked, "disagreements": dup_bad})

    # -- THE VERDICT, derived in-gate ----------------------------------------
    grid_sig = "|".join(
        "%s:%s" % (t, ";".join("%s=%d" % (k[1], v) for k, v in sorted(by_class.items())
                               if k[0] == t))
        for t in sorted(transports))
    grid_sig = grid_sig + "|TOTAL=%d" % len(rules)

    if locality_B:
        modes = sorted(set(census[(rid, "B")]["coord"][5] for rid in locality_B))
        classes = sorted(set(census[(rid, "B")]["coord"][0] for rid in locality_B))
        mech = "DECLARED-PARTIAL-COSET-OVERLAP(CLASSES=%s;MODES=%s)" % (
            "+".join(classes), "+".join(modes))
        sizes = sorted(set(tuple(c["size"] for c in census[(rid, "B")]["per_component"]
                                 if not c["complete"]) for rid in locality_B))
        comp_sig = "NONCOMPLETE-COMPONENT-SIZES=%s;RULES-WITH-NONTRIVIAL-B1=%d" % (
            "+".join(",".join(str(x) for x in s) for s in sizes), len(nontrivial_b1))
        circ = sum(R["standards"][rid]["links_that_are_circles"] for rid in locality_B)
        chw = sum(R["standards"][rid]["charts_with_links"] for rid in locality_B)
        readings = sorted(set(R["standards"][rid]["reading"] for rid in locality_B))
        dims = sorted(set(d for rid in locality_B
                          for d in R["standards"][rid]["local_dimensions_realised"]))
        std_sig = ("LINK-CIRCLES=%d-OF-%d-CHARTS;DIMREAD=%s;"
                   "LOCAL-DIMENSIONS=%s;DIMPROFILE=EXTENSIVE-EXCLUDED") % (
            circ, chw, "+".join(readings),
            "+".join(str(d) for d in dims) if dims else "NONE")
        surv = len([1 for rid in locality_B if persist[rid]["survives"]])
        dbl = len([1 for rid in locality_B if persist[rid]["doubles"]])
        b2_sig = "SURVIVES-AT-%d-OF-%d;COMPONENTS-DOUBLE-AT-%d" % (
            surv, len(locality_B), dbl)
    else:
        mech = "NONE-IN-THE-DECLARED-GRID"
        comp_sig = "ALL-COMPONENTS-COMPLETE"
        std_sig = "NOT-MEASURED-NO-LOCALITY-BEARING-RULE"
        b2_sig = "NOT-APPLICABLE"

    null_sig = ("G0-CLIQUE-ONLY-AT-%d-OF-%d;ORBIT-PARTITION-CLASSES-CLIQUE-ONLY-"
                "AT-%d-OF-%d(R2-A-VERIFIED-%d-UNIT-ACTIONS-AND-%d-SWEPT-ACTIONS-"
                "%d-COUNTEREXAMPLES)") % (
        len(g0) - len(g0_bad), len(g0),
        len(orbit_rules) - len(orbit_bad), len(orbit_rules),
        r2a_actions, sweep_actions, r2a_counterex + sweep_bad)
    const_sig = "DENSITIES-CONSTANT-B-TO-B2-AT-%d-OF-%d;UNDEFINED-B2-DENSITY-AT-%d" % (
        len([c for c in consts if c["densities_constant_B_to_B2"]]), len(consts),
        len([c for c in consts if c["B"]["b2_density"] is None]))

    payload = {
        "locality_rules": locality_B,
        "grid_size": len(rules),
        "grid_signature": grid_sig,
        "mechanism": mech,
        "component_signature": comp_sig,
        "standards_signature": std_sig,
        "b2_signature": b2_sig,
        "null_signature": null_sig,
        "refuses": len(refuses_B),
        "constants_signature": const_sig,
    }
    head, segs, full = build_verdict(payload,
                                     swap_pairing=(MUTANT == "verdict-pair-swap"))

    # THE VERDICT GATE: complete-string equality against a segment-by-segment
    # rebuild (RUNBOOK section 14 addendum, v14 #10 -- containment abolished)
    rebuilt = head + "<" + "|".join(
        [s[1] for s in build_verdict(payload)[1]]) + ">"
    gate("G-VERDICT-STRING-EQUALITY",
         "the complete emitted verdict string equals a string rebuilt "
         "segment-by-segment from the measured values (equality, not "
         "containment)",
         full == rebuilt, {"emitted_len": len(full)})

    # every segment flippable
    flips = []
    for i, (nm, txt) in enumerate(segs):
        pert = dict(payload)
        if nm == "RULES":
            pert["locality_rules"] = (locality_B[:-1] if len(locality_B) > 1
                                      else locality_B + ["RXXX"])
        elif nm == "GRID":
            pert["grid_signature"] = grid_sig + ";PERTURBED"
        elif nm == "MECHANISM":
            pert["mechanism"] = mech + "-PERTURBED"
        elif nm == "COMPONENTS":
            pert["component_signature"] = comp_sig + "-PERTURBED"
        elif nm == "STANDARDS":
            pert["standards_signature"] = std_sig + "-PERTURBED"
        elif nm == "B2":
            pert["b2_signature"] = b2_sig + "-PERTURBED"
        elif nm == "NULL":
            pert["null_signature"] = null_sig + "-PERTURBED"
        elif nm == "REFUSES":
            pert["refuses"] = len(refuses_B) + 1
        elif nm == "CONSTANTS":
            pert["constants_signature"] = const_sig + "-PERTURBED"
        flips.append(build_verdict(pert)[2] != full)
    gate("G-VERDICT-SEGMENTS-FLIPPABLE",
         "perturbing any one measured segment changes the emitted string: "
         "every segment carries content",
         all(flips) and len(flips) == len(segs),
         {"segments": len(segs), "flippable": len([f for f in flips if f])})

    # both verdict heads reachable by the instrument
    synth_none = dict(payload)
    synth_none["locality_rules"] = []
    synth_none["mechanism"] = "NONE-IN-THE-DECLARED-GRID"
    h_none = build_verdict(synth_none)[0]
    synth_loc = dict(payload)
    synth_loc["locality_rules"] = ["R001"]
    h_loc = build_verdict(synth_loc)[0]
    gate("G-VERDICT-BOTH-HEADS-REACHABLE",
         "both verdict heads are derivable by the same derivation: the "
         "instrument can emit either outcome",
         h_none == "R2-NO-LOCALITY-IN-THE-DECLARED-GRID"
         and h_loc == "R2-LOCALITY-AT" and h_none != h_loc,
         {"heads": [h_loc, h_none]})

    R["verdict"] = {
        "head": head,
        "segments": [{"name": s[0], "text": s[1]} for s in segs],
        "string": full,
        "declared_scope": "at the single block B (TB3's native 8-label arena "
                          "via I6) and at B2 (two blocks plus basepoint), over "
                          "the exhaustively enumerated declared atlas grid of "
                          "%d rules at two declared transports" % len(rules),
    }

    # -- totals, computed never typed (#24) -----------------------------------
    R["totals"] = {
        "anchors": len(ANCHORS),
        "gates": len(GATES),
        "grid_rules": len(rules),
        "rule_arena_measurements": len(census),
        "locality_bearing_rules_B": len(locality_B),
        "refusing_rules_B": len(refuses_B),
        "mutants_declared": len(MUTANTS),
        "declared_transports": len(transports),
        "declared_modes": len(MODES),
    }
    R["theorems"] = {
        "R2-A": "drawn <=> b in orbit(a) and orbit(a) regular; the drawn "
                "relation at a cell is a disjoint union of complete graphs on "
                "the regular orbits.  Re-proved in the paper, verified at "
                "%d actions with %d counterexamples." % (r2a_actions, r2a_counterex),
        "R2-A-coherence": "a drawn pair forces a trivial stabiliser, so the "
                          "three drawn maps of any 2-cell compose to the "
                          "identity: N_coh = N identically (FORCED, disclosed).",
        "R2-partition": "an atlas whose cells PARTITION the labels can never "
                        "produce a non-complete component; locality requires "
                        "cells that overlap partially (G0/G1/G3-ORBITS verified "
                        "clique-only).",
        "R2-C-inherited": "the R1 gateway phi < 1 is forced by the basepoint; "
                          "R2 does not use phi (anchor A-R1-ADJ).",
    }
    gate("G-COUNTS-COMPUTED",
         "every total is recomputed by an independent expression and matches "
         "(#24: counts computed, never typed)",
         (R["totals"]["grid_rules"] == len(R["grid"]["coordinates"])
          and R["totals"]["rule_arena_measurements"] == 2 * len(R["census_rows"])
          and R["totals"]["locality_bearing_rules_B"]
          == len([x for x in R["census_rows"] if x["status"] == "NON-COMPLETE"])
          and R["totals"]["refusing_rules_B"]
          == len([x for x in R["census_rows"] if x["status"] == "REFUSES"])
          and R["totals"]["anchors"] == len(ANCHOR_ROWS)),
         dict(R["totals"]))
    R["compliance"] = compliance_sweep(R)
    return R, census, rules


# ----------------------------------------------------------------------------
# 12.  Compliance sweep -- rule by rule, stated with its status
# ----------------------------------------------------------------------------

def compliance_sweep(R):
    names = set(g["name"] for g in GATES)
    rows = [
        ("RUNBOOK 13/14/15 with every addendum binds at delivery (#246/#313)",
         "APPLIED -- this sweep enumerates each rule and its status"),
        ("#10 containment is not equality (verdict gate compares the COMPLETE "
         "string against a segment rebuild)",
         "G-VERDICT-STRING-EQUALITY" if "G-VERDICT-STRING-EQUALITY" in names else "MISSING"),
        ("#10 render from the gated object (one object, one source of truth)",
         "G-RENDER-FROM-GATED-OBJECT (evaluated at write time)"),
        ("#234 the verdict is derived inside a gate and a flip mutant proves "
         "the derivation can fail",
         "G-VERDICT-SEGMENTS-FLIPPABLE + mutants verdict-pair-swap / "
         "locality-erase / locality-inject"),
        ("#234 cell-completeness gate catches a dropped cell",
         "G-GRID-CELL-COMPLETE + mutant grid-drop"),
        ("#234/#219 two independent routes are genuinely independent",
         "G-DRAW-TWO-ROUTES (orbit/stabiliser vs brute force over the group), "
         "G-COMPONENTS-TWO-ROUTES (union-find vs F_2 rank), "
         "G-COMPLETENESS-TWO-ROUTES (stored count vs pair scan)"),
        ("#257 computed qualifiers (no typed qualifier segment)",
         "every verdict segment is built from measured counts; "
         "G-VERDICT-SEGMENTS-FLIPPABLE proves each carries content"),
        ("#208 forced clauses are disclosures, not must-pass claims",
         "coherence (N_coh = N) and the orbit-partition clique-only result are "
         "recorded as FORCED disclosures with their proofs"),
        ("#208 no gate predicate references mutant identity",
         "no gate reads MUTANT; injections live in the measured functions"),
        ("#219 a zero-hit or zero-lookup cache gate is vacuous",
         "G-CACHE-EXERCISED gates hits > 0 AND misses > 0"),
        ("#24 counts are computed, never typed",
         "every total in R['totals'] is a len() or a comprehension count"),
        ("section 15 declared-arena discipline: the arena and the grid are "
         "printed and matched at every coordinate",
         "G-ARENA-DECL-MATCHED + G-GRID-CELL-COMPLETE + the grid is a named "
         "verdict coordinate (segment GRID)"),
        ("section 14 #175 symmetry self-tests, evaluated fresh",
         "G-SYMMETRY-SELFTEST (memo bypassed, fresh-call count gated)"),
        ("section 14 #185 self-tests must not reach their quantity through the memo",
         "f2_rank(fresh=True) in the self-test path"),
        ("section 13 #313 boundary parity witness with a measured delta",
         "G-BOUNDARY-PARITY"),
        ("section 13 #314 precheck doctrine: a precheck may gate what is "
         "censused but never name the verdict",
         "no precheck exists; the verdict is named by the censused objects only"),
        ("exact arithmetic only",
         "G-FLOATGUARD (AST scan) + G-NO-FLOATS-IN-RECEIPT (evaluated at write "
         "time)"),
        ("REFUSES is recorded, never skipped",
         "G-EVERY-RULE-RECORDED + mutant refuses-skip"),
        ("the UNDEFINED path is live or the exclusion is stated (R1 repair "
         "order 8)",
         "G-UNDEFINED-PATH-LIVE -- reached by shipped inputs"),
        ("no claim about the continuum; the word 'manifold' appears only in "
         "the rung's name",
         "the verdict string uses LINK-CIRCLES / DIMREAD / LOCAL-DIMENSIONS"),
    ]
    return [{"rule": a, "status": b} for a, b in rows]


# ----------------------------------------------------------------------------
# 13.  Rendering -- FROM THE GATED OBJECT ONLY
# ----------------------------------------------------------------------------

def frac(x):
    if x is None:
        return "UNDEFINED"
    return "%d/%d" % (x.numerator, x.denominator)


def jsonable(o):
    if isinstance(o, Fraction):
        return {"num": o.numerator, "den": o.denominator, "text": frac(o)}
    if isinstance(o, dict):
        return dict((str(k), jsonable(v)) for k, v in o.items()
                    if not (isinstance(k, str) and k.startswith("_")))
    if isinstance(o, (list, tuple)):
        return [jsonable(v) for v in o]
    return o


def render_text(R):
    L = []
    def w(s=""):
        L.append(s)
    w("=" * 78)
    w("v14 R2 -- THE MANIFOLD RUNG.  Exact instrument, plain delivery run.")
    w("=" * 78)
    w()
    w("PIN: v14/note-r2-manifold-pin.md (v14 ledger #11).")
    w("THE QUESTION: does any drawing rule in the declared finite grid of atlas")
    w("declarations produce a component with a NON-COMPLETE overlap graph?")
    w()
    w("-" * 78)
    w("1.  ANCHORS (every inherited number arrives hash-verified)")
    w("-" * 78)
    for a in R["anchors"]:
        w("  %-22s %-46s %s  %s" % (a["name"], a["artifact"], a["measured"],
                                    "OK" if a["ok"] else "FAIL"))
        w("      %s" % a["provenance"])
    w()
    w("-" * 78)
    w("2.  THE ARENAS AND THE TRANSPORTS (declared data, RUNBOOK section 15)")
    w("-" * 78)
    ad = R["arena_declaration"]
    w("  B  : %d labels, %d block, basepoint %s -- %s"
      % (ad["B"]["labels"], ad["B"]["blocks"], ad["B"]["basepoint"], ad["B"]["note"]))
    w("  B2 : %d labels, %d blocks, basepoint %s -- %s"
      % (ad["B2"]["labels"], ad["B2"]["blocks"], ad["B2"]["basepoint"], ad["B2"]["note"]))
    w("       %s" % ad["B2"]["rule_application"])
    for tn in sorted(ad["transports"]):
        t = ad["transports"][tn]
        w("  %s : gamma = %s  (order %d)" % (tn, t["gamma"], t["gamma_order"]))
        w("       %s" % t["source"])
        w("       Sigma = %s  (order %d)" % (t["sigma"], t["sigma_order"]))
        w("       %s" % t["sigma_source"])
        w("       drawing group |<gamma>| = %d ; |<gamma,Sigma>| = %d"
          % (t["drawing_group_order"], t["sigma_mixed_group_order"]))
        w("       cyclic lattice        : %s" % t["cyclic_lattice"])
        w("       declared Sigma lattice: %s" % t["declared_sigma_lattice"])
    w("  modes declared: %s" % ", ".join(ad["declared_modes"]))
    w("  drawing relation: %s" % ad["drawing_relation"])
    w("  coset convention: %s" % ad["coset_order_convention"])
    w()
    w("-" * 78)
    w("3.  THE DECLARED ATLAS GRID (arena data: printed, matched, and a named")
    w("    verdict coordinate)")
    w("-" * 78)
    w("  grid size (computed): %d rules; truncated: %s"
      % (R["grid"]["size"], R["grid"]["truncated"]))
    for k in sorted(R["grid"]["by_transport_and_class"]):
        w("    %-16s %d" % (k, R["grid"]["by_transport_and_class"][k]))
    w()
    w("  %-6s %-11s %-3s %-7s %5s %-4s %-10s" %
      ("rid", "class", "T", "H", "|H|", "c", "mode"))
    for c in R["grid"]["coordinates"]:
        w("  %-6s %-11s %-3s %-7s %5s %-4s %-10s" %
          (c[6], c[0], c[1], c[2], c[3], "-" if c[4] < 0 else c[4], c[5]))
    w()
    w("-" * 78)
    w("4.  THE LOCALITY CENSUS AT B  (the criterion: does ANY component have a")
    w("    non-complete overlap graph?)")
    w("-" * 78)
    w("  %-6s %-11s %-3s %-7s %-4s %-10s %5s %5s %5s %-9s %-9s %s" %
      ("rid", "class", "T", "H", "c", "mode", "cells", "edges", "comp",
       "sizes", "cmplness", "STATUS"))
    for row in R["census_rows"]:
        c = row["coord"]
        w("  %-6s %-11s %-3s %-7s %-4s %-10s %5d %5d %5d %-9s %-9s %s" %
          (row["rid"], c[0], c[1], c[2], "-" if c[4] < 0 else c[4], c[5],
           row["cells"], row["edges"], row["components"],
           ",".join(str(x) for x in row["component_sizes"][:4]),
           frac(row["completeness"]), row["status"]))
    w()
    lc = R["locality_census"]
    w("  criterion: %s" % lc["criterion"])
    w("  locality-bearing rules at B  (computed): %d -- %s"
      % (lc["count_locality_B"], ", ".join(lc["locality_bearing_at_B"]) or "NONE"))
    w("  locality-bearing rules at B2 (computed): %d -- %s"
      % (lc["count_locality_B2"], ", ".join(lc["locality_bearing_at_B2"]) or "NONE"))
    w("  refusing rules at B (computed): %d -- %s"
      % (lc["count_refuses_B"], ", ".join(lc["refusing_at_B"]) or "NONE"))
    w()
    w("-" * 78)
    w("5.  THE NON-COMPLETE COMPONENTS, in detail")
    w("-" * 78)
    if not lc["locality_bearing_at_B"]:
        w("  none -- every component of every grid rule is a complete graph.")
    for row in R["census_rows"]:
        if not row["noncomplete_components"]:
            continue
        w("  %s  %s" % (row["rid"], row["coord"]))
        for c in row["noncomplete_components"]:
            w("      component size %d: %d of %d pairs drawn, graph b1 = %d, "
              "members %s" % (c["size"], c["edges"], c["pairs"], c["b1_graph"],
                              c["members"]))
    w()
    w("-" * 78)
    w("6.  THE PORTED STANDARDS at the locality-bearing rules")
    w("    (I3's definitions reimplemented; dimprofile is EXTENSIVE-EXCLUDED)")
    w("-" * 78)
    w("  controls (the instrument must be able to see a sphere):")
    for k in sorted(R["controls_ported_standards"]):
        v = R["controls_ported_standards"][k]
        w("    %-52s V=%2d E=%3d F=%3d b=(%d,%d,%d) every-link-a-circle=%s"
          % (k, v["V"], v["E"], v["F"], v["b0"], v["b1"], v["b2"],
             v["every_link_is_a_circle"]))
    w()
    for rid in sorted(R["standards"]):
        s = R["standards"][rid]
        w("  %s  %s" % (rid, s["coord"]))
        w("      charts of the non-complete component: %s"
          % s["noncomplete_component_charts"])
        w("      link (V,E,b0,b1) at those charts:")
        for X in sorted(s["link_at_those_charts"], key=lambda z: int(z)):
            w("          chart %-3s link=%s star=%s"
              % (X, s["link_at_those_charts"][X], s["star_at_those_charts"][X]))
        w("      dimension reading: %s (%d distinct over %d charts with links)"
          % (s["reading"], s["distinct_readings"], s["charts_with_links"]))
        w("      local dimensions realised: %s   [%s]"
          % (s["local_dimensions_realised"], s["dimprofile_status"]))
        w("      links that are circles: %d of %d charts with links; "
          "every-link-a-circle = %s"
          % (s["links_that_are_circles"], s["charts_with_links"],
             s["every_link_is_a_circle"]))
    w()
    w("-" * 78)
    w("7.  b1 PER COMPONENT at the locality-bearing rules (measured, disclosed)")
    w("-" * 78)
    if not R["b1_per_component"]:
        w("  not applicable -- no locality-bearing rule.")
    for rid in sorted(R["b1_per_component"]):
        v = R["b1_per_component"][rid]
        w("  %s  per-component [size, edges, cycle rank] = %s ; b1(N) = %d ; "
          "b1(N_coh) = %d" % (rid, v["graph_cycle_rank_per_component"],
                              v["b1_of_N"], v["b1_of_N_coh"]))
    w("  rules with a non-trivial degree-1 component (computed): %s"
      % (", ".join(R["b1_nontrivial_at"]) or "NONE"))
    w()
    w("-" * 78)
    w("8.  THE BLOCK CONSTANTS UNDER THE NEW ATLASES (a table, not a verdict)")
    w("    both denominator conventions; B against B2")
    w("-" * 78)
    w("  %-6s %-11s %-3s %-4s %-10s | %5s %5s %5s %5s | %-10s %-10s %-9s | %s" %
      ("rid", "class", "T", "c", "mode", "E_N", "pairs", "F", "F_coh",
       "F_coh/E_N", "F_coh/pair", "b2/F_coh", "B->B2"))
    for c in R["block_constants"]:
        co = c["coord"]
        w("  %-6s %-11s %-3s %-4s %-10s | %5d %5d %5d %5d | %-10s %-10s %-9s | %s" %
          (c["rid"], co[0], co[1], "-" if co[4] < 0 else co[4], co[5],
           c["B"]["E_N"], c["B"]["edges"], c["B"]["F"], c["B"]["F_COH"],
           frac(c["B"]["ncoh_per_incidence"]), frac(c["B"]["ncoh_per_pair"]),
           frac(c["B"]["b2_density"]),
           "constant" if c["densities_constant_B_to_B2"] else "MOVES"))
    w()
    w("-" * 78)
    w("9.  B2 PERSISTENCE for the locality-bearing rules")
    w("-" * 78)
    if not R["b2_persistence"]:
        w("  not applicable -- no locality-bearing rule.")
    for rid in sorted(R["b2_persistence"]):
        p = R["b2_persistence"][rid]
        w("  %s  non-complete components B=%d B2=%d ; survives=%s doubles=%s ; "
          "componentwise completeness %s -> %s (unchanged=%s)"
          % (rid, p["noncomplete_components_B"], p["noncomplete_components_B2"],
             p["survives"], p["doubles"], frac(p["completeness_B"]),
             frac(p["completeness_B2"]), p["completeness_unchanged"]))
    w()
    w("-" * 78)
    w("10. CONTROLS")
    w("-" * 78)
    pc = R["positive_control"]
    w("  POSITIVE CONTROL: %s" % pc["declaration"])
    w("      cells %s share exactly the label(s) %s; %d edges drawn"
      % (pc["cells"], pc["labels_shared_by_the_two_cells"], pc["edges"]))
    w("      components: %s" % pc["components"])
    w("      returns a non-complete component: %s" % pc["returns_noncomplete"])
    sc = R["scramble_control"]
    w("  SCRAMBLE CONTROL: %s" % sc["tested_set"])
    w("      rules tested %d; identification measure moved at %d; component "
      "census unchanged at %d"
      % (sc["rules_tested"], sc["identification_measure_moved_at"],
         sc["component_census_unchanged_at"]))
    w("  SYMMETRY SELF-TEST (fresh, memo bypassed): %s"
      % ", ".join("%s=%s" % (x["relabelling"], x["census_invariant"])
                  for x in R["symmetry_selftest"]))
    pw = R["parity_witness"]
    w("  BOUNDARY PARITY WITNESS: %s" % pw["tested_set"])
    w("      rules tested %d; the connective matters at %d; total measured "
      "delta %d" % (pw["rules_tested"], pw["rules_where_the_connective_matters"],
                    pw["total_delta"]))
    for p in pw["per_rule"][:6]:
        w("      %s: 2-cells under AND = %d, under OR = %d, delta = %d"
          % (p["rule"], p["two_cells_under_AND"], p["two_cells_under_OR"],
             p["measured_delta"]))
    ap = R["alt_drawing_group_probe"]
    w("  ALT DRAWING-GROUP PROBE: %s" % ap["note"])
    for k in sorted(ap["per_transport"]):
        w("      %s: |<gamma,Sigma>| = %d, pairs drawn = %d"
          % (k, ap["per_transport"][k]["sigma_mixed_group_order"],
             ap["per_transport"][k]["pairs_drawn_if_the_drawing_group_were_it"]))
    w("      %s" % ap["reason"])
    w()
    w("-" * 78)
    w("11. THEOREMS VERIFIED IN UNIT")
    w("-" * 78)
    for k in sorted(R["theorems"]):
        w("  %-18s %s" % (k, R["theorems"][k]))
    rv = R["r2a_verification"]
    w("  R2-A verification: %d actions this unit uses (%d counterexamples); "
      "%d cyclic actions swept on the block (%d counterexamples)"
      % (rv["actions_this_unit_uses"], rv["counterexamples_at_this_units_actions"],
         rv["cyclic_actions_swept_on_the_block"], rv["counterexamples_in_the_sweep"]))
    w()
    w("-" * 78)
    w("12. GATES (%d, all passed)" % R["totals"]["gates"])
    w("-" * 78)
    for g in R["gates"]:
        w("  [%s] %s" % ("PASS" if g["passed"] else "FAIL", g["name"]))
        w("       %s" % g["statement"])
    w()
    w("-" * 78)
    w("13. MUTANTS DECLARED (%d) -- each must exit 1 on a NAMED gate"
      % len(R["mutants"]))
    w("-" * 78)
    for m in R["mutants"]:
        w("  %-20s %s" % (m["name"], m["what_it_breaks"]))
    w()
    w("-" * 78)
    w("14. COMPLIANCE SWEEP, rule by rule")
    w("-" * 78)
    for c in R["compliance"]:
        w("  RULE   : %s" % c["rule"])
        w("  STATUS : %s" % c["status"])
    w()
    w("-" * 78)
    w("15. TOTALS (computed, never typed)")
    w("-" * 78)
    for k in sorted(R["totals"]):
        w("  %-32s %d" % (k, R["totals"][k]))
    w()
    w("=" * 78)
    w("THE VERDICT")
    w("=" * 78)
    w(R["verdict"]["string"])
    w()
    w("segments:")
    for s in R["verdict"]["segments"]:
        w("  %-12s %s" % (s["name"], s["text"]))
    w()
    w("declared scope: %s" % R["verdict"]["declared_scope"])
    w()
    return "\n".join(L) + "\n"


MUTANTS = [
    {"name": "grid-drop",
     "what_it_breaks": "silently drops one (H,c,mode) grid cell",
     "expected_gate": "G-GRID-CELL-COMPLETE"},
    {"name": "census-corrupt",
     "what_it_breaks": "drops one drawn edge from a rule's census",
     "expected_gate": "G-DRAW-TWO-ROUTES"},
    {"name": "complete-flip",
     "what_it_breaks": "flips the per-component completeness verdict, and the "
                       "rule's locality flag with it, at a locality-bearing rule",
     "expected_gate": "G-COMPLETENESS-TWO-ROUTES"},
    {"name": "refuses-skip",
     "what_it_breaks": "skips rules that draw nothing instead of recording REFUSES",
     "expected_gate": "G-EVERY-RULE-RECORDED"},
    {"name": "verdict-pair-swap",
     "what_it_breaks": "swaps two verdict segments' names against their values",
     "expected_gate": "G-VERDICT-STRING-EQUALITY"},
    {"name": "table-corrupt",
     "what_it_breaks": "corrupts one block-constants table cell after measurement",
     "expected_gate": "G-RENDER-FROM-GATED-OBJECT"},
    {"name": "anchor-hash",
     "what_it_breaks": "corrupts the I6 anchor hash",
     "expected_gate": "A-R0-I6"},
    {"name": "orbit-corrupt",
     "what_it_breaks": "corrupts the orbit machinery at the G0 null",
     "expected_gate": "G-DRAW-TWO-ROUTES"},
    {"name": "locality-erase",
     "what_it_breaks": "collapses SLIDING onto BLOCKWISE, erasing all locality",
     "expected_gate": "G-MODES-DISTINCT"},
    {"name": "locality-inject",
     "what_it_breaks": "injects a spurious non-complete component at the null",
     "expected_gate": "G-R2A-NULL-CLIQUE-ONLY"},
    {"name": "toy-broken",
     "what_it_breaks": "breaks the positive control's partial overlap",
     "expected_gate": "G-POSITIVE-CONTROL"},
    {"name": "scramble-inert",
     "what_it_breaks": "makes the scramble control a no-op",
     "expected_gate": "G-SCRAMBLE-CONTROL"},
    {"name": "census-row-corrupt",
     "what_it_breaks": "corrupts one rendered census row after measurement",
     "expected_gate": "G-RENDER-FROM-GATED-OBJECT"},
    {"name": "float-leak",
     "what_it_breaks": "reports a float offence in the source scan",
     "expected_gate": "G-FLOATGUARD"},
]


def render_check(R, census):
    """Every cell of every rendered table must equal the corresponding cell of
    the gated measurement object (RUNBOOK section 13 addendum, v14 #10)."""
    bad = []
    for c in R["block_constants"]:
        mb = census[(c["rid"], "B")]
        for key, val in (("E_N", mb["E_N"]), ("F", mb["F_N"]),
                         ("F_COH", mb["F_COH"]), ("edges", mb["edges"])):
            if c["B"][key] != val:
                bad.append((c["rid"], "block_constants." + key))
    for row in R["census_rows"]:
        mb = census[(row["rid"], "B")]
        if (row["cells"] != mb["cells"] or row["edges"] != mb["edges"]
                or row["components"] != mb["components"]
                or row["component_sizes"] != mb["component_sizes"]
                or row["completeness"] != mb["completeness"]):
            bad.append((row["rid"], "census_rows"))
        expect = ("REFUSES" if mb["refuses"] else
                  ("NON-COMPLETE" if mb["any_noncomplete"] else "clique-only"))
        if row["status"] != expect:
            bad.append((row["rid"], "census_rows.status"))
    return bad


def deliver():
    R, census, rules = run()
    R["gates"] = GATES
    R["mutants"] = MUTANTS
    R["schema"] = "isp/v14/r2-manifold/1"
    R["pin"] = "v14/note-r2-manifold-pin.md"
    R["pin_sha256_prefix"] = "76d42dfbc900"
    R["source_sha256"] = sha256_full(SRC)

    # RENDER FROM THE GATED OBJECT (RUNBOOK section 13 addendum, v14 #10)
    text = render_text(R)
    payload = jsonable(R)

    # the render path must carry the gated object's cells verbatim
    mismatches = render_check(R, census)
    for i, c in enumerate(payload["block_constants"]):
        if c["B"]["E_N"] != R["block_constants"][i]["B"]["E_N"]:
            mismatches.append((c["rid"], "render-payload", None, None))
    gate("G-RENDER-FROM-GATED-OBJECT",
         "every rendered table cell equals the corresponding cell of the gated "
         "measurement object -- the receipt and the output render from one "
         "object, no bypass path",
         len(mismatches) == 0, {"mismatches": mismatches[:4]})

    floats = []

    def scan(o, path=""):
        if isinstance(o, bool):
            return
        if isinstance(o, FLOAT_T):
            floats.append(path)
        elif isinstance(o, dict):
            for k, v in o.items():
                scan(v, path + "/" + str(k))
        elif isinstance(o, list):
            for i, v in enumerate(o):
                scan(v, path + "[%d]" % i)

    scan(payload)
    gate("G-NO-FLOATS-IN-RECEIPT", "the emitted receipt contains no float",
         len(floats) == 0, {"floats": floats[:4]})

    # the gate count is itself computed, after every gate has run
    R["totals"]["gates"] = len(GATES)
    R["gates"] = GATES
    payload = jsonable(R)
    text = render_text(R)

    with open(OUT_TXT, "w") as fh:
        fh.write(text)
    with open(OUT_JSON, "w") as fh:
        fh.write(json.dumps(payload, indent=1, sort_keys=False) + "\n")
    sys.stdout.write(text)
    return 0


def selftest():
    before = {}
    for p in (OUT_TXT, OUT_JSON):
        before[p] = sha256_full(p) if os.path.exists(p) else None
    rows = []
    ok_all = True
    for m in MUTANTS:
        proc = subprocess.run([sys.executable, SRC, "--mutant", m["name"]],
                              capture_output=True, text=True)
        blob = proc.stdout + proc.stderr
        died = proc.returncode == 1
        named = ("GATE FAILED: " + m["expected_gate"]) in blob
        unchanged = all((sha256_full(p) if os.path.exists(p) else None) == before[p]
                        for p in (OUT_TXT, OUT_JSON))
        good = died and named and unchanged
        ok_all = ok_all and good
        rows.append((m["name"], proc.returncode, named, unchanged, good))
        print("  %-20s exit=%d named_gate=%s artifacts_unchanged=%s  %s"
              % (m["name"], proc.returncode, named, unchanged,
                 "DEAD" if good else "SURVIVED"))
    print("  mutants declared (computed): %d ; all dead: %s" % (len(MUTANTS), ok_all))
    return 0 if ok_all else 1


def main():
    global MUTANT
    args = sys.argv[1:]
    if args and args[0] == "--list-mutants":
        for m in MUTANTS:
            print(m["name"])
        return 0
    if args and args[0] == "--selftest":
        print("FALSIFICATION SELFTEST -- every declared mutant must exit 1 on a "
              "named gate and write nothing")
        return selftest()
    if args and args[0] == "--mutant":
        if len(args) < 2 or args[1] not in [m["name"] for m in MUTANTS]:
            sys.stderr.write("unknown mutant\n")
            return 2
        MUTANT = args[1]
    elif args:
        sys.stderr.write("unknown argument: %s\n" % args[0])
        return 2
    try:
        if MUTANT is None:
            return deliver()
        R, census, rules = run()
        R["gates"] = GATES
        R["mutants"] = MUTANTS
        R["schema"] = "isp/v14/r2-manifold/1"
        R["pin"] = "v14/note-r2-manifold-pin.md"
        R["pin_sha256_prefix"] = "76d42dfbc900"
        R["source_sha256"] = sha256_full(SRC)
        text = render_text(R)
        payload = jsonable(R)
        mismatches = render_check(R, census)
        gate("G-RENDER-FROM-GATED-OBJECT",
             "every rendered table cell equals the corresponding cell of the "
             "gated measurement object", len(mismatches) == 0,
             {"mismatches": mismatches[:4]})
        sys.stderr.write("MUTANT %s SURVIVED -- no gate fired\n" % MUTANT)
        return 3
    except GateFailure as exc:
        sys.stderr.write(str(exc) + "\n")
        return 1


if __name__ == "__main__":
    sys.exit(main())
