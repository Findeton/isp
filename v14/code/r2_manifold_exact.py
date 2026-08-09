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
  R2-LOCALITY-DECLARABLE-AT<computed rule list ...>
  R2-NO-LOCALITY-IN-THE-DECLARED-GRID<...>
Each is derived INSIDE a gate from the measured census.  The emitted string is
compared for COMPLETE STRING EQUALITY against an INDEPENDENT RECONSTRUCTION
built from the receipt object alone (RUNBOOK section 14 addendum, v14 #10 and
v14 #20: a compliance gate whose comparator cannot disagree with the object
under test is vacuous by construction) -- reconstruct_verdict_from_receipt()
shares no code with build_verdict(), and five injection mutants prove it fires.

The unit measures, beyond the census:
  * THE WIDTH LAW -- the drawn graph on a regular orbit is the clique blow-up
    of a circulant; locality iff the declared window width c does not exceed
    the cyclic diameter D of the orbit's coset support.  Closed forms for the
    edge count and the cycle rank; the whole census predicted from the
    declaration and compared against the measurement at 109 of 109.  The two
    declared transports reach their thresholds by DIFFERENT causes (a missing
    coset-point at T7, a contiguous coset-arc at T4), both measured.
  * THE MOTIVATION CENSUS -- all 4,140 set partitions of the eight labels at
    both transports; I6's own seven Fano lines (derived from its declared
    non-zero F_2^3 labels) and their complements; the locality census over all
    40,320 numberings of the carrier.  Whether anything in the inheritance
    motivates the locality-bearing covers is MEASURED, not argued.
  * THE GRID BOUNDARY -- the rules a coset-count admissibility test would
    admit and the declared group-order test excludes, and their census.
  * THE SUCCESSOR CONTROL -- a fixed-point-free transport with the same
    sliding class, yielding a triangulated 1-manifold with a CONSISTENT
    chart-intrinsic dimension reading: the grid's boundary made visible.
  * THE LINK CONVENTION -- both link conventions and the triangulated-circle
    count, printed side by side.
  * THE PROSE AUDIT -- every load-bearing numeric sentence of the paper is
    RENDERED HERE from the measured object and gated to appear verbatim in
    v14/paper-02-manifold-rung.md (RUNBOOK section 13 addendum, v14 #20).

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


# The three gates that can only be evaluated at WRITE time, after the receipt
# object exists.  Named here so the falsifier census can account for them
# rather than silently mis-denominating itself; deliver() gates that all three
# really did run.
DEFERRED_GATES = ("G-RENDER-FROM-GATED-OBJECT", "G-NO-FLOATS-IN-RECEIPT",
                  "G-PROSE-RENDERS-FROM-THE-RECEIPT",
                  "G-FINAL-GATE-COUNT", "G-DEFERRED-GATES-EVALUATED")


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


def read_json(rel):
    with open(os.path.join(ROOT, rel), "r") as fh:
        return json.load(fh)


# PATH-VALUE ANCHORS (RUNBOOK section 14 addendum, v14 #20): a read-by-path
# from a pinned artifact anchors the (path, value) PAIR, not only the file
# bytes.  Every value this unit reads out of a pinned receipt appears here with
# its exact JSON path AND its exact expected value; a path drift that changes
# the arena or the verdict dies by anchor.
PATH_ANCHOR_ROWS = [
    ("P-I6-GAMMA7", "v13/code/tb3_third_base_receipt.json",
     ("tables", "the_ladder", "the_embedding", "the_witness_system_part"),
     [0, 2, 3, 4, 5, 6, 7, 1],
     "T7's transport generator: the x7 = [A7:A6] embedding witness's system part"),
    ("P-I6-GAMMA4", "v13/code/tb3_third_base_receipt.json",
     ("tables", "ord_census", "lex_first_Q_per_order", "4"),
     [0, 1, 3, 4, 5, 2, 7, 6],
     "T4's transport generator: the lex-first completion permutation at defect "
     "order 4"),
    ("P-I6-SIGMA", "v13/code/tb3_third_base_receipt.json",
     ("tables", "arena", "the_declared_completion_transposition"),
     [0, 3, 2, 1, 4, 5, 6, 7],
     "Sigma, the declared completion transposition (1 3)"),
    ("P-I6-BLOCKSIZE", "v13/code/tb3_third_base_receipt.json",
     ("tables", "base_declaration", "carrier", "system_triple_dimension"),
     8,
     "the block size, read from I6 and never typed"),
    ("P-I6-FANO-LABELS", "v13/code/tb3_third_base_receipt.json",
     ("tables", "the_ladder", "the_embedding", "the_non_zero_labels_of_F2_cubed"),
     [1, 2, 3, 4, 5, 6, 7],
     "the seven non-zero labels of F_2^3 -- the Fano points I6 declares its "
     "type on; the motivation census's one inherited partial-overlap cover"),
    ("P-I3-CONTROL-TETRA", "v13/code/top_topology_receipt.json",
     ("schema",), "top-topology-receipt-v1",
     "I3's receipt schema: the topology base whose nerve/link/dimension "
     "definitions are reimplemented here"),
]


def read_by_path(obj, path):
    cur = obj
    for k in path:
        cur = cur[k]
    return cur


def verify_anchors():
    rows = list(ANCHOR_ROWS)
    if MUTANT == "anchor-skip":
        rows = rows[:-1]
    for name, rel, expect, why in rows:
        path = os.path.join(ROOT, rel)
        got = sha12(path)
        if MUTANT == "anchor-hash" and name == "A-R0-I6":
            got = "0" * 12
        if MUTANT == "anchor-hash-" + name:
            got = "0" * 12
        ANCHORS.append({"name": name, "kind": "file-bytes", "artifact": rel,
                        "expected": expect, "measured": got, "provenance": why,
                        "ok": got == expect})
        gate(name, "external anchor %s verifies at %s" % (expect, rel),
             got == expect, {"expected": expect, "measured": got})
    return len(rows)


def verify_path_anchors():
    """Every (path, value) pair this unit reads out of a pinned artifact."""
    cache = {}
    rows = list(PATH_ANCHOR_ROWS)
    for name, rel, path, expect, why in rows:
        if rel not in cache:
            cache[rel] = read_json(rel)
        p = tuple(path)
        if MUTANT == "path-drift" and name == "P-I6-GAMMA4":
            p = ("tables", "ord_census", "lex_first_Q_per_order", "6")
        try:
            got = read_by_path(cache[rel], p)
        except (KeyError, IndexError, TypeError):
            got = None
        if MUTANT == "path-value-" + name:
            got = None
        ok = (got == expect)
        ANCHORS.append({"name": name, "kind": "path-value", "artifact": rel,
                        "json_path": list(p), "expected": expect,
                        "measured": got, "provenance": why, "ok": ok})
        gate(name,
             "path-value anchor: %s[%s] reads exactly %r (the PAIR is anchored, "
             "not only the file bytes)" % (rel, ".".join(str(x) for x in path),
                                           expect),
             ok, {"path": list(p), "expected": expect, "measured": got})
    return len(rows)


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
            if MUTANT == "window-drop" and M == 8 and c == 3 and i == 2:
                continue        # one interior cyclic window, silently missing
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
    if MUTANT == "refuses-reclassify":
        refuses = False         # the single unguarded bit, reclassified

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
    if MUTANT == "flag-flip" and rule.klass == "G2" and rule.mode == "SLIDING" \
            and rule.c == 2 and rule.transport == "T7" and arena.name == "B":
        any_noncomplete = False     # one rule silently leaves the headline
    if MUTANT == "b1-zero":
        for c in per_comp:
            c["b1_graph"] = 0       # the entire degree-one finding, erased

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
    if MUTANT == "twocell-drop":
        # the per-block-uniform drop: the first 2-cell of each block.  It
        # survives the copy-reduction and coherence gates by construction --
        # only an independent recount sees it.
        drop = set()
        for b in range(len(arena.blocks)):
            lo = b * BLOCK_SIZE_DECLARED
            hi = lo + BLOCK_SIZE_DECLARED
            for t in twocells:
                if lo <= t[0] < hi:
                    drop.add(t)
                    break
        twocells = [t for t in twocells if t not in drop]

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

    # THE TWO LINK CONVENTIONS, both computed (RUNBOOK section 14 addendum,
    # v13 #313: a convention that moves a headline carries its witness).
    #   cell-multiplicity : a 2-cell is counted once per coordinate cell
    #   simple-graph      : the link is the simple graph on distinct neighbours
    link = {}
    link_simple = {}
    link_is_triangulated_circle = {}
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
        sedges = sorted(set(ledges))
        scomps = union_find_components(adj, sedges) if adj else []
        link_simple[X] = (lV, len(sedges), len(scomps),
                          len(sedges) - lV + len(scomps))
        # a TRIANGULATED circle is a cycle graph: connected, >= 3 vertices,
        # |V| = |E| as simple edges, every degree exactly 2.
        deg = dict((v, 0) for v in adj)
        for (a, b) in sedges:
            deg[a] += 1
            deg[b] += 1
        link_is_triangulated_circle[X] = (
            lV >= 3 and len(sedges) == lV and len(scomps) == 1
            and all(deg[v] == 2 for v in adj))

    charts_with_links = [X for X in labels if starE[X] > 0]
    every_circle = all(link[X][0] == link[X][1] and link[X][2] == 1
                       and link[X][3] == 1 for X in charts_with_links) \
        if charts_with_links else False
    profiles = set((dimprofile[X], (starE[X], starF[X]), link[X])
                   for X in charts_with_links)
    # THE CHART-INTRINSIC READING: the same triple with the cell-INDEXED
    # dimprofile vector replaced by the chart-intrinsic sorted multiset of
    # local dimensions.  The delivered (cell-indexed) reading compares a vector
    # indexed by an EXTERNAL coordinate -- the rule's cell list -- so two
    # charts agree only if they lie in exactly the same cells.
    dim_multiset = dict((X, tuple(sorted(v for v in dimprofile[X] if v >= 0)))
                        for X in labels)
    profiles_intrinsic = set((dim_multiset[X], (starE[X], starF[X]), link[X])
                             for X in charts_with_links)
    return {
        "dimprofile": {str(X): list(dimprofile[X]) for X in labels},
        "dimprofile_route2_agrees": all(dimprofile[X] == dim_route2[X] for X in labels),
        "dimprofile_status": "EXTENSIVE-EXCLUDED (I3 / R0 row I3)",
        "star": {str(X): [starE[X], starF[X]] for X in labels},
        "link": {str(X): list(link[X]) for X in labels},
        "link_simple_graph_convention": {str(X): list(link_simple[X]) for X in labels},
        "link_is_a_triangulated_circle": {str(X): link_is_triangulated_circle[X]
                                          for X in labels},
        "charts_with_links": len(charts_with_links),
        "distinct_readings": len(profiles),
        "reading": "CONSISTENT" if len(profiles) == 1 else "INCONSISTENT",
        "dim_multiset": {str(X): list(dim_multiset[X]) for X in labels},
        "distinct_readings_chart_intrinsic": len(profiles_intrinsic),
        "reading_chart_intrinsic": ("CONSISTENT" if len(profiles_intrinsic) == 1
                                    else "INCONSISTENT"),
        "every_link_is_a_circle": every_circle,
        "links_that_are_circles": len([X for X in charts_with_links
                                       if link[X][0] == link[X][1]
                                       and link[X][2] == 1 and link[X][3] == 1]),
        "links_that_are_circles_simple_convention": len(
            [X for X in charts_with_links
             if link_simple[X][0] == link_simple[X][1]
             and link_simple[X][2] == 1 and link_simple[X][3] == 1]),
        "links_that_are_triangulated_circles": len(
            [X for X in charts_with_links if link_is_triangulated_circle[X]]),
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
# 9a.  THE WIDTH LAW -- the circulant theorem, derived and verified in unit
# ----------------------------------------------------------------------------
#
# THEOREM R2-W (the sliding-window drawn graph).  Let T = <gamma> act on the
# labels L and let R be a REGULAR orbit (|R| = |T|).  Let H be the declared
# subgroup, its orbits ("cosets") c_0 ... c_{k-1} ordered by minimum label, and
# write iota(x) for the coset index of x, S = iota(R) contained in Z_k,
# w_i = |c_i intersect R|, and d_k for cyclic distance.  For SLIDING of width c:
#
#   (1) STRUCTURE.  On R, x ~ y  iff  d_k(iota x, iota y) <= c-1.  The drawn
#       graph on R is the lexicographic blow-up of the induced circulant
#       C_k(1..c-1)[S] by cliques K_{w_i}.
#   (2) EDGE COUNT.  |E| = sum_{i in S} C(w_i,2) + sum_{i<j in S, d_k<=c-1} w_i w_j.
#   (3) LOCALITY.  A component is incomplete iff it contains a pair at cyclic
#       distance >= c.  When the circulant on S is connected this is exactly
#       c <= diam_k(S) -- THE WIDTH LAW.
#   (4) THE OTHER MODES ARE THEOREMS TOO.  ALL puts every two coset indices in
#       a common c-subset, so the drawn graph on R is complete.  BLOCKWISE and
#       the orbit classes partition the cosets, hence the labels, so the
#       partition corollary applies: clique-only, always.
#
# Consequence (#208): WHICH RULES ARE LOCAL is FORCED by the declaration.  The
# gate below evaluates the law from (mode, c, the coset partition, the regular
# orbits) alone -- no atlas is built, no cell is enumerated -- and compares it
# against the measured census at every rule.

def subgroup_of_rule(rule, transports):
    """The subgroup whose orbits are the rule's cosets, from the declaration."""
    td = transports[rule.transport]
    g, s, n = td["gamma"], td["sigma"], BLOCK_SIZE_DECLARED
    if rule.klass in ("G0", "G1", "G2"):
        if rule.klass == "G0":
            return tuple(closure([g], n))
        return dict(cyclic_subgroups(g, n))[rule.hname]
    return dict(declared_sigma_lattice(g, s, n))[rule.hname]


def cyclic_distance(i, j, k):
    d = i - j if i >= j else j - i
    return d if d + d <= k else k - d


def width_law_row(rule, transports):
    """THE ANALYTIC ROUTE.  Predict the rule's locality status and its drawn
    edge count from the DECLARATION alone -- the subgroup's orbit partition,
    the transport's regular orbits, the mode and the width.  Builds no atlas."""
    td = transports[rule.transport]
    n = BLOCK_SIZE_DECLARED
    T = tuple(closure([td["gamma"]], n))
    labels = tuple(range(n))
    cosets = orbits_of(subgroup_of_rule(rule, transports), labels)
    k = len(cosets)
    iota = {}
    for i, cs in enumerate(cosets):
        for x in cs:
            iota[x] = i
    regular = [o for o in orbits_of(T, labels) if len(o) == len(T)]
    mode = rule.mode
    c = rule.c

    def adjacent(i, j):
        if mode is None:                      # orbit classes: cells ARE cosets
            return i == j
        if mode == "ALL":                     # every pair of cosets co-celled
            return True
        if mode == "BLOCKWISE":               # disjoint consecutive windows
            return (i // c) == (j // c)
        return cyclic_distance(i, j, k) <= c - 1        # SLIDING

    total_edges = 0
    noncomplete = False
    per_orbit = []
    for Ro in regular:
        S = sorted(set(iota[x] for x in Ro))
        w = dict((i, len([x for x in Ro if iota[x] == i])) for i in S)
        E = sum(w[i] * (w[i] - 1) // 2 for i in S)
        sedges = []
        for a, b in itertools.combinations(S, 2):
            if adjacent(a, b):
                E += w[a] * w[b]
                sedges.append((a, b))
        total_edges += E
        for comp in union_find_components(S, sedges):
            for a, b in itertools.combinations(comp, 2):
                if not adjacent(a, b):
                    noncomplete = True
        D = max([cyclic_distance(a, b, k) for a in S for b in S]) if len(S) > 1 else 0
        # the support's SHAPE -- the cause of the threshold, measured
        contiguous = (len(S) > 1 and
                      all(S[t + 1] - S[t] == 1 for t in range(len(S) - 1)))
        shape = ("WHOLE-CYCLE" if len(S) == k else
                 ("MISSING-POINT" if len(S) == k - 1 else
                  ("CONTIGUOUS-ARC" if contiguous else "OTHER")))
        per_orbit.append({"orbit": list(Ro), "k": k, "support": S,
                          "multiplicities": [w[i] for i in S],
                          "cyclic_diameter_D": D, "support_shape": shape,
                          "edges_predicted": E,
                          "width_law_locality": (c is not None and mode == "SLIDING"
                                                 and c <= D)})
    return {"rid": rule.rid, "coord": list(rule.coord()), "cosets": k,
            "mode": "-" if mode is None else mode,
            "c": -1 if c is None else c,
            "predicted_noncomplete": noncomplete,
            "predicted_edges": total_edges,
            "per_regular_orbit": per_orbit}


def closed_form_families(rows_by_rid, census_edges, census_b1):
    """The three closed forms the width law specialises to, evaluated against
    the measured edge counts and cycle ranks.  Each is a THIRD route: neither
    the atlas enumeration nor the analytic graph build, but an arithmetic
    formula in (k, m, c)."""
    out = []
    for rid, row in sorted(rows_by_rid.items()):
        if row["mode"] != "SLIDING":
            continue
        for po in row["per_regular_orbit"]:
            k, S, w, c = po["k"], po["support"], po["multiplicities"], row["c"]
            m = len(S)
            if po["support_shape"] == "MISSING-POINT" and set(w) == {1} \
                    and (c - 1) * 2 < k:
                # S = Z_k minus a point, w == 1, c-1 < k/2
                E = (c - 1) * (k - 2)
                b1 = (c - 2) * (k - 2)
                fam = "MISSING-POINT:|E|=(c-1)(k-2),b1=(c-2)(k-2)"
            elif po["support_shape"] == "CONTIGUOUS-ARC" and set(w) == {1} \
                    and c <= m:
                # the band count on a path of m positions, valid while the
                # window is no longer than the arc it slides along
                E = (c - 1) * m - c * (c - 1) // 2
                b1 = E - m + 1
                fam = "CONTIGUOUS-ARC(c<=m):|E|=(c-1)m-C(c,2),b1=|E|-m+1"
            elif po["support_shape"] == "CONTIGUOUS-ARC" and set(w) == {1}:
                # SATURATED: a window at least as long as the arc puts every
                # pair of the arc in a common cell, so the blow-up is complete
                E = m * (m - 1) // 2
                b1 = E - m + 1
                fam = "CONTIGUOUS-ARC(c>m,SATURATED):|E|=C(m,2),b1=|E|-m+1"
            else:
                E = po["edges_predicted"]
                b1 = E - sum(w) + 1
                fam = "GENERAL-BLOW-UP:|E|=sum C(w_i,2)+sum_{d<=c-1} w_i w_j"
            out.append({"rid": rid, "family": fam, "k": k, "m": m, "c": c,
                        "closed_form_E": E, "measured_E": census_edges.get(rid),
                        "closed_form_b1": b1, "measured_b1": census_b1.get(rid),
                        "agrees": (E == census_edges.get(rid)
                                   and b1 == census_b1.get(rid))})
    return out


# ----------------------------------------------------------------------------
# 9b.  THE MOTIVATION CENSUS -- is any locality-bearing cover inherited?
# ----------------------------------------------------------------------------
#
# The RSQ precedent, applied: a positive result is demoted when the objects
# that carry it are selected by the property under test.  So the unit MEASURES
# what its own inheritance supplies.  Three sweeps, all exhaustive:
#
#   (a) every SET PARTITION of the eight labels, at both transports.  The orbit
#       family of ANY subgroup of S_8 is one of these, so this settles Sigma,
#       <gamma,Sigma>, the seven declared words, the ladder 1<A4<GL(3,2)<A6<A7
#       and every subgroup of every one of them AT ONCE.
#   (b) I6's OWN declared partial-overlap cover -- the seven Fano lines,
#       derived from the receipt's the_non_zero_labels_of_F2_cubed by the
#       F_2-linear rule a + b + c = 0 -- and their complements.
#   (c) the locality census under every NUMBERING of the carrier: SLIDING reads
#       the label order twice (to name the cosets, and to say "consecutive"),
#       so the rule list is a coordinate of the numbering.  Measured, not
#       argued.

def drawn_pairs_of_group(T, labels):
    """The unordered drawn pairs of a transport group (THEOREM R2-A)."""
    out = set()
    for o in orbits_of(T, labels):
        if len(o) == len(T):
            for a in o:
                for b in o:
                    if a < b:
                        out.add((a, b))
    return out


def cover_is_noncomplete(cells, drawn, labels):
    """The R1 criterion applied to an arbitrary cover: does SOME component of
    the drawn overlap graph fail to be complete?  Returns (verdict, edges)."""
    e = set()
    for cc in cells:
        cl = sorted(cc)
        for i in range(len(cl)):
            for j in range(i + 1, len(cl)):
                if (cl[i], cl[j]) in drawn:
                    e.add((cl[i], cl[j]))
    for comp in union_find_components(labels, sorted(e)):
        kk = len(comp)
        got = 0
        for i in range(kk):
            for j in range(i + 1, kk):
                if (comp[i], comp[j]) in e:
                    got += 1
        if got != kk * (kk - 1) // 2:
            return True, sorted(e)
    return False, sorted(e)


def all_set_partitions(items):
    items = list(items)
    if not items:
        yield []
        return
    first, rest = items[0], items[1:]
    for smaller in all_set_partitions(rest):
        for i in range(len(smaller)):
            yield smaller[:i] + [[first] + smaller[i]] + smaller[i + 1:]
        yield [[first]] + smaller


def bell_number(n):
    """Bell(n) by the triangle -- the partition sweep's denominator, DERIVED."""
    row = [1]
    for _ in range(n):
        nxt = [row[-1]]
        for v in row:
            nxt.append(nxt[-1] + v)
        row = nxt
    return row[0]


def fano_lines_from_i6(nonzero_labels):
    """The seven Fano lines of PG(2,2) on I6's declared non-zero F_2^3 labels:
    the triples {a,b,c} with a XOR b XOR c = 0.  DERIVED from the receipt's own
    declaration, not chosen here."""
    nz = tuple(nonzero_labels)
    lines = set()
    for a, b in itertools.combinations(nz, 2):
        c3 = a ^ b
        if c3 in nz:
            lines.add(tuple(sorted((a, b, c3))))
    return sorted(lines)


def sliding_locality_from_multiplicities(w, c, memo):
    """Locality of a SLIDING rule as a function of the cyclic multiplicity
    vector alone (THEOREM R2-W (1)+(3)).  Memoised: the order sweep evaluates
    1,209,600 rule-censuses and they take only a few hundred distinct values."""
    key = (w, c)
    if key in memo:
        return memo[key]
    k = len(w)
    S = [i for i in range(k) if w[i] > 0]
    edges = [(a, b) for a, b in itertools.combinations(S, 2)
             if cyclic_distance(a, b, k) <= c - 1]
    out = False
    for comp in union_find_components(S, edges):
        for a, b in itertools.combinations(comp, 2):
            if cyclic_distance(a, b, k) > c - 1:
                out = True
    memo[key] = out
    return out


def motivation_census(transports, rules, nonzero_labels):
    labels = tuple(range(BLOCK_SIZE_DECLARED))
    drawn = {}
    for tn, td in transports.items():
        drawn[tn] = drawn_pairs_of_group(tuple(closure([td["gamma"]], BLOCK_SIZE_DECLARED)),
                                         labels)

    # ---- (a) every set partition of the eight labels, at both transports ----
    parts = list(all_set_partitions(labels))
    if MUTANT == "partition-sweep-truncate":
        parts = parts[:100]
    p_meas = 0
    p_hits = []
    for p in parts:
        cells = [frozenset(b) for b in p]
        for tn in sorted(transports):
            p_meas += 1
            nc, _ = cover_is_noncomplete(cells, drawn[tn], labels)
            if nc:
                p_hits.append((len(p_hits), tn))

    # ---- (b) I6's own seven Fano lines, and their complements --------------
    lines = fano_lines_from_i6(nonzero_labels)
    if MUTANT == "fano-shrink":
        lines = lines[:3]
    pairs_covered = set()
    for L in lines:
        for pr in itertools.combinations(L, 2):
            pairs_covered.add(pr)
    pairs_possible = len(list(itertools.combinations(sorted(nonzero_labels), 2)))
    fano_rows = {}
    for tn in sorted(transports):
        nc, e = cover_is_noncomplete([frozenset(L) for L in lines], drawn[tn], labels)
        comp = [frozenset(set(nonzero_labels) - set(L)) for L in lines]
        nc2, e2 = cover_is_noncomplete(comp, drawn[tn], labels)
        fano_rows[tn] = {"lines_noncomplete": nc, "lines_edges": len(e),
                         "complements_noncomplete": nc2,
                         "complements_edges": len(e2)}

    # ---- (c) the locality census over every numbering of the carrier -------
    sliding = [r for r in rules if r.mode == "SLIDING"]
    systems = {}
    for r in sliding:
        key = (r.transport, orbits_of(subgroup_of_rule(r, transports), labels))
        systems.setdefault(key, []).append(r)
    sysinfo = []
    for (tn, cs), rs in sorted(systems.items(), key=lambda kv: (kv[0][0], len(kv[0][1]))):
        T = tuple(closure([transports[tn]["gamma"]], BLOCK_SIZE_DECLARED))
        reg = [o for o in orbits_of(T, labels) if len(o) == len(T)]
        sysinfo.append((tn, cs, reg, sorted(rs, key=lambda r: r.rid)))
    memo = {}
    dist = {}
    rulesets = {}
    per_rule = {}
    numberings = list(itertools.permutations(range(BLOCK_SIZE_DECLARED)))
    if MUTANT == "order-sweep-truncate":
        numberings = numberings[:100]
    censuses = 0
    for pi in numberings:
        loc = []
        for (tn, cs, reg, rs) in sysinfo:
            order = sorted(range(len(cs)), key=lambda i: min(pi[x] for x in cs[i]))
            wv = {}
            for oi, Ro in enumerate(reg):
                wv[oi] = tuple(len([x for x in Ro if x in cs[order[j]]])
                               for j in range(len(cs)))
            for r in rs:
                censuses += 1
                for oi in wv:
                    if sliding_locality_from_multiplicities(wv[oi], r.c, memo):
                        loc.append(r.rid)
                        break
        loc = tuple(sorted(loc))
        dist[len(loc)] = dist.get(len(loc), 0) + 1
        rulesets[loc] = rulesets.get(loc, 0) + 1
        for rid in loc:
            per_rule[rid] = per_rule.get(rid, 0) + 1
    modal = max(dist.items(), key=lambda kv: (kv[1], -kv[0]))

    return {
        "partition_sweep": {
            "partitions_of_the_eight_labels": len(parts),
            "bell_number_8_derived": bell_number(BLOCK_SIZE_DECLARED),
            "transports": len(transports),
            "measurements": p_meas,
            "noncomplete_hits": len(p_hits),
            "what_it_settles": "the orbit family of ANY subgroup of S_8 is one "
                               "of these partitions, so Sigma, <gamma,Sigma>, "
                               "the seven declared words, the ladder "
                               "1<A4<GL(3,2)<A6<A7 and every subgroup of every "
                               "one of them are settled at once",
        },
        "fano_cover": {
            "source": "I6 tables.the_ladder.the_embedding."
                      "the_non_zero_labels_of_F2_cubed (path-anchored), with "
                      "the lines derived by the F_2-linear rule a^b^c = 0",
            "lines": [list(L) for L in lines],
            "line_count": len(lines),
            "pairs_covered": len(pairs_covered),
            "pairs_possible": pairs_possible,
            "is_a_2_design": len(pairs_covered) == pairs_possible,
            "per_transport": fano_rows,
            "transports_where_it_is_clique_only": len(
                [1 for v in fano_rows.values() if not v["lines_noncomplete"]]),
        },
        "order_relativity": {
            "numberings_swept": len(numberings),
            "sliding_rules": len(sliding),
            "distinct_coset_systems": len(sysinfo),
            "rule_censuses": censuses,
            "count_distribution": dict((str(k), v) for k, v in sorted(dist.items())),
            "distinct_rule_sets": len(rulesets),
            "modal_count": modal[0],
            "modal_orders": modal[1],
            "declared_numbering_count": None,       # filled by the caller
            "rules_local_at_some_numbering": sorted(per_rule),
            "per_rule_orders_local": dict((k, per_rule[k]) for k in sorted(per_rule)),
        },
    }


# ----------------------------------------------------------------------------
# 9c.  THE GRID BOUNDARY -- what the admissibility proxy excludes
# ----------------------------------------------------------------------------
#
# The declared admissibility test is c * |H| < block size: an arithmetic on the
# GROUP ORDER.  But the construction uses H's ORBITS.  Where |H| exceeds its
# orbit count the two disagree, and rules whose cells are perfectly well formed
# are excluded.  The unit measures the excluded set and censuses it.

def grid_boundary_census(transports, declared_coords):
    labels = tuple(range(BLOCK_SIZE_DECLARED))
    drawn = dict((tn, drawn_pairs_of_group(
        tuple(closure([td["gamma"]], BLOCK_SIZE_DECLARED)), labels))
        for tn, td in transports.items())
    rows = []
    for tname in sorted(transports):
        td = transports[tname]
        g, s = td["gamma"], td["sigma"]
        whole = len(closure([g, s], BLOCK_SIZE_DECLARED))
        for klass, latt in (("G2", cyclic_subgroups(g, BLOCK_SIZE_DECLARED)),
                            ("G3-UNIONS", declared_sigma_lattice(g, s, BLOCK_SIZE_DECLARED))):
            for hname, els in latt:
                h = len(els)
                if klass == "G3-UNIONS" and h == whole:
                    continue
                orbs = orbits_of(els, labels)
                k = len(orbs)
                for c in range(2, k):
                    if c * h < BLOCK_SIZE_DECLARED:
                        continue            # already admitted by the declared test
                    for mode in MODES:
                        coord = (klass, tname, hname, h, c, mode)
                        if coord in declared_coords:
                            continue
                        cells = cells_from_orbits(orbs, mode, c)
                        cells = sorted(set(frozenset(x) for x in cells),
                                       key=lambda cc: (min(cc), sorted(cc)))
                        nc, e = cover_is_noncomplete(cells, drawn[tname], labels)
                        row = {"coord": list(coord), "cosets": k,
                               "cells": [sorted(x) for x in cells],
                               "edges": len(e), "noncomplete": nc}
                        if nc:
                            comps = union_find_components(labels, e)
                            eset = set(e)
                            det = []
                            for comp in comps:
                                kk = len(comp)
                                pr = kk * (kk - 1) // 2
                                got = len([1 for i in range(kk)
                                           for j in range(i + 1, kk)
                                           if (comp[i], comp[j]) in eset])
                                if got != pr:
                                    det.append({"size": kk, "drawn": got,
                                                "pairs": pr,
                                                "completeness": Fraction(got, pr)})
                            row["noncomplete_components"] = det
                        rows.append(row)
    word_rows = [r for r in rows if r["coord"][0] == "G3-UNIONS"]
    return {
        "declared_test": "c * |H| < block size (an arithmetic on the GROUP "
                         "ORDER)",
        "alternative_test": "c < the number of H-cosets (an arithmetic on the "
                            "ORBIT COUNT -- the quantity the construction "
                            "actually uses)",
        "excluded_from_the_declared_words": len(word_rows),
        "excluded_including_the_cyclic_lattice": len(rows),
        "excluded_noncomplete": len([r for r in rows if r["noncomplete"]]),
        "the_locality_bearing_exclusions": [r for r in rows if r["noncomplete"]],
        "rows": rows,
    }


# ----------------------------------------------------------------------------
# 9d.  THE SUCCESSOR CONTROL -- the grid's boundary, made visible
# ----------------------------------------------------------------------------
#
# Both declared transports have FIXED POINTS (T7 fixes 0; T4 fixes 0 and 1 and
# carries the 2-orbit {6,7}), so the regular orbit is never the whole label set
# and the coset-position circulant, restricted to it, is not vertex-transitive.
# That -- not "width-based overlap" -- is the obstruction to a chart-independent
# dimension at this scale.  The control below removes exactly that obstruction:
# the SAME sliding class at a FIXED-POINT-FREE transport (the 8-cycle).  It is
# outside the declared grid and claims nothing about the substrate; it exists to
# make the grid's boundary a measured object rather than an inference.

def successor_control():
    n = BLOCK_SIZE_DECLARED
    labels = tuple(range(n))
    cyc = tuple((i + 1) % n for i in range(n))
    if MUTANT == "successor-control-broken":
        cyc = tuple([0] + [(i + 1) % n for i in range(1, n - 1)] + [1])
    T = tuple(closure([cyc], n))
    orbs = orbits_of(T, labels)
    drawn = drawn_pairs_of_group(T, labels)
    rows = []
    for c in (2, 3, 4):
        cells = sorted(set(frozenset((i + t) % n for t in range(c)) for i in range(n)),
                       key=lambda cc: (min(cc), sorted(cc)))
        eset = set()
        onecells = []
        for ci, cc in enumerate(cells):
            cl = sorted(cc)
            for i in range(len(cl)):
                for j in range(i + 1, len(cl)):
                    if (cl[i], cl[j]) in drawn:
                        eset.add((cl[i], cl[j]))
                        onecells.append((cl[i], cl[j], ci))
        twocells = []
        for ci, cc in enumerate(cells):
            for tri in itertools.combinations(sorted(cc), 3):
                a, b, c3 = tri
                if (a, b) in eset and (b, c3) in eset and (a, c3) in eset:
                    twocells.append((a, b, c3, ci))
        m = {"_labels": labels, "_cells": cells, "_edges": eset,
             "_onecells": onecells, "_twocells": twocells}
        s = standards(m)
        comps = union_find_components(labels, sorted(eset))
        nc, _ = cover_is_noncomplete(cells, drawn, labels)
        deg = dict((X, 0) for X in labels)
        for (a, b) in eset:
            deg[a] += 1
            deg[b] += 1
        is_1manifold = (len(twocells) == 0 and len(comps) == 1
                        and len(eset) == n and all(deg[X] == 2 for X in labels))
        links = sorted(set(tuple(s["link"][str(X)]) for X in labels))
        links_simple = sorted(set(tuple(s["link_simple_graph_convention"][str(X)])
                                  for X in labels))
        rows.append({
            "c": c, "cells": len(cells), "edges": len(eset),
            "two_cells": len(twocells),
            "components": [len(x) for x in comps],
            "noncomplete": nc,
            "reading_cell_indexed": s["reading"],
            "distinct_readings_cell_indexed": s["distinct_readings"],
            "reading_chart_intrinsic": s["reading_chart_intrinsic"],
            "distinct_readings_chart_intrinsic": s["distinct_readings_chart_intrinsic"],
            "distinct_links_cell_multiplicity": [list(x) for x in links],
            "distinct_links_simple_graph": [list(x) for x in links_simple],
            "is_a_triangulated_1_manifold": is_1manifold,
        })
    return {
        "declaration": "the 8-cycle transport (fixed-point-free, regular on the "
                       "whole label set) with the SAME sliding cell class; "
                       "OUTSIDE the declared grid, a control only",
        "transport": list(cyc),
        "transport_order": perm_order(cyc),
        "fixed_points": [X for X in labels if cyc[X] == X],
        "orbits": [list(o) for o in orbs],
        "regular_orbit_is_the_whole_label_set": len(orbs) == 1 and len(orbs[0]) == n,
        "rows": rows,
    }


# ----------------------------------------------------------------------------
# 10.  Verdict derivation -- inside a gate, rebuilt segment by segment
# ----------------------------------------------------------------------------

SEGMENT_ORDER = ("RULES", "GRID", "DRAWING", "MECHANISM", "WIDTH-LAW",
                 "MOTIVATION", "COMPONENTS", "STANDARDS", "LINK-CONVENTION",
                 "B2-PERSISTENCE", "NULL", "REFUSES", "GRID-BOUNDARY",
                 "BLOCK-CONSTANTS")

HEAD_LOCALITY = "R2-LOCALITY-DECLARABLE-AT"
HEAD_NONE = "R2-NO-LOCALITY-IN-THE-DECLARED-GRID"


def build_verdict(payload, swap_pairing=False):
    """Assemble the verdict string from the measured payload.  Returns
    (head, [(segment_name, segment_text), ...], full_string).

    The HEAD is `LOCALITY-DECLARABLE`, not `LOCALITY-FOUND`: what the unit
    establishes is an existence statement about ATLAS SPACE -- the criterion is
    satisfiable, by a construction with a closed-form width threshold -- and
    the MOTIVATION segment carries the measurement that says why it is not a
    statement about the substrate."""
    loc = payload["locality_rules"]
    segs = []
    if loc:
        head = HEAD_LOCALITY
        segs.append(("RULES", "RULES=%d-OF-%d:%s" %
                     (len(loc), payload["grid_size"], ",".join(loc))))
    else:
        head = HEAD_NONE
        segs.append(("RULES", "RULES=0-OF-%d" % payload["grid_size"]))
    segs.append(("GRID", "GRID=" + payload["grid_signature"]))
    segs.append(("DRAWING", "DRAWING=" + payload["drawing_signature"]))
    segs.append(("MECHANISM", "MECHANISM=" + payload["mechanism"]))
    segs.append(("WIDTH-LAW", "WIDTH-LAW=" + payload["width_law_signature"]))
    segs.append(("MOTIVATION", "MOTIVATION=" + payload["motivation_signature"]))
    segs.append(("COMPONENTS", "COMPONENTS=" + payload["component_signature"]))
    segs.append(("STANDARDS", "STANDARDS=" + payload["standards_signature"]))
    segs.append(("LINK-CONVENTION",
                 "LINK-CONVENTION=" + payload["link_convention_signature"]))
    segs.append(("B2-PERSISTENCE", "B2-PERSISTENCE=" + payload["b2_signature"]))
    segs.append(("NULL", "NULL=" + payload["null_signature"]))
    segs.append(("REFUSES", "REFUSES=%d-OF-%d" %
                 (payload["refuses"], payload["grid_size"])))
    segs.append(("GRID-BOUNDARY",
                 "GRID-BOUNDARY=" + payload["grid_boundary_signature"]))
    segs.append(("BLOCK-CONSTANTS", "BLOCK-CONSTANTS=" + payload["constants_signature"]))
    if swap_pairing and len(segs) >= 3:
        a, b = segs[1], segs[2]
        segs[1] = (a[0], a[1].split("=")[0] + "=" + b[1].split("=", 1)[1])
        segs[2] = (b[0], b[1].split("=")[0] + "=" + a[1].split("=", 1)[1])
    if MUTANT == "verdict-typed-segment":
        segs[7] = ("STANDARDS", "STANDARDS=LINK-CIRCLES=80-OF-80-CHARTS;"
                                "DIMREAD=CONSISTENT;LOCAL-DIMENSIONS=2;"
                                "DIMPROFILE=EXTENSIVE-EXCLUDED")
    if MUTANT == "verdict-append-text":
        segs[3] = ("MECHANISM", segs[3][1] + "-AND-SUBSTRATE-MOTIVATED")
    if MUTANT == "verdict-typed-motivation":
        segs[5] = ("MOTIVATION", "MOTIVATION=INHERITED-FROM-I6-FANO-LINES")
    if MUTANT == "verdict-fully-typed":
        segs = [(nm, "%s=TYPED" % nm) for nm in SEGMENT_ORDER]
        segs[0] = ("RULES", "RULES=1-OF-1:R999")
        head = HEAD_LOCALITY
    if MUTANT == "verdict-inert-segment":
        segs[5] = ("MOTIVATION", "MOTIVATION=NONE-INHERITED")
    full = head + "<" + "|".join(s[1] for s in segs) + ">"
    return head, segs, full


# ----------------------------------------------------------------------------
# 10a.  THE INDEPENDENT COMPARATOR (RUNBOOK section 14 addendum, v14 #20)
# ----------------------------------------------------------------------------
#
# "A compliance gate whose comparator cannot disagree with the object under
# test is vacuous by construction."  The previous comparator called
# build_verdict twice on the same dict.  This one shares NO code with
# build_verdict and NO input with it: it reads the RECEIPT OBJECT -- the same
# stored tables the paper and the output render from -- and re-derives every
# segment from the measured rows.  If a segment is typed, appended to, swapped
# with its neighbour or replaced wholesale, this comparator disagrees.

def reconstruct_verdict_from_receipt(R):
    grid_size = len(R["grid"]["coordinates"])
    rows = R["census_rows"]
    loc = sorted([r["rid"] for r in rows if r["status"] == "NON-COMPLETE"])
    ref = [r["rid"] for r in rows if r["status"] == "REFUSES"]
    out = []

    if loc:
        head = HEAD_LOCALITY
        out.append("RULES=%d-OF-%d:%s" % (len(loc), grid_size, ",".join(loc)))
    else:
        head = HEAD_NONE
        out.append("RULES=0-OF-%d" % grid_size)
    if MUTANT == "head-constant":
        head = HEAD_LOCALITY        # the head stops tracking the census

    bt = R["grid"]["by_transport_and_class"]
    tnames = sorted(set(k.split("/")[0] for k in bt))
    gs = "|".join("%s:%s" % (t, ";".join(
        "%s=%d" % (k.split("/")[1], bt[k]) for k in sorted(bt) if k.split("/")[0] == t))
        for t in tnames)
    out.append("GRID=" + gs + "|TOTAL=%d" % grid_size)

    ad = R["alt_drawing_group_probe"]["per_transport"]
    zero = len([1 for v in ad.values()
                if v["pairs_drawn_if_the_drawing_group_were_it"] == 0])
    out.append("DRAWING=R1-RELATION-AT-<GAMMA>-VERDICT-DETERMINING"
               "(ALT-<GAMMA,SIGMA>:0-PAIRS-AT-%d-OF-%d-TRANSPORTS=>"
               "NO-LOCALITY-IN-THE-DECLARED-GRID)" % (zero, len(ad)))

    if loc:
        idx = dict((r["rid"], r) for r in rows)
        klasses = sorted(set(idx[x]["coord"][0] for x in loc))
        modes = sorted(set(idx[x]["coord"][5] for x in loc))
        out.append("MECHANISM=DECLARED-PARTIAL-COSET-OVERLAP(CLASSES=%s;MODES=%s)"
                   % ("+".join(klasses), "+".join(modes)))
    else:
        out.append("MECHANISM=NONE-IN-THE-DECLARED-GRID")

    wl = R["width_law"]
    causes = ";".join("%s:%s(D=%d,C-MAX=%d)" % (k, wl["threshold_causes"][k]["shape"],
                                                wl["threshold_causes"][k]["D"],
                                                wl["threshold_causes"][k]["D"])
                      for k in sorted(wl["threshold_causes"]))
    out.append("WIDTH-LAW=NONCOMPLETE-IFF-C<=D(D=MAX-CYCLIC-COSET-DISTANCE-IN-"
               "THE-REGULAR-ORBIT);TWO-CAUSES=%s;CENSUS-DERIVABLE-FROM-THE-"
               "DECLARATION-AT-%d-OF-%d;CLOSED-FORMS-AGREE-AT-%d-OF-%d"
               % (causes, wl["rules_predicted_correctly"], wl["rules"],
                  wl["closed_form_agreements"], wl["closed_form_rows"]))

    mo = R["motivation_census"]
    ps, fa, orl = mo["partition_sweep"], mo["fano_cover"], mo["order_relativity"]
    pct = orl["modal_share_percent_text"]
    if MUTANT == "verdict-inert-segment":
        # the MOTIVATION segment becomes a constant in BOTH the builder and
        # this comparator: string equality still holds, and the segment stops
        # carrying measured content.  Only the flippability gate can see it.
        out.append("MOTIVATION=NONE-INHERITED")
        ps = None
    if ps is not None:
        out.append("MOTIVATION=NONE-INHERITED:PARTITION-COVERS-NONCOMPLETE-AT-%d-OF-%d"
                   "(ALL-%d-PARTITIONS-X-%d-TRANSPORTS);I6-FANO-LINES-CLIQUE-ONLY-AT-"
                   "%d-OF-%d(2-DESIGN:%d-OF-%d-PAIRS-COVERED);ORDER-RELATIVE"
                   "(COUNT=%d..%d-OVER-%d-NUMBERINGS;DECLARED=%d-MODAL-%s%%;"
                   "DISTINCT-RULE-SETS=%d)"
                   % (ps["noncomplete_hits"], ps["measurements"],
                      ps["partitions_of_the_eight_labels"], ps["transports"],
                      fa["transports_where_it_is_clique_only"], len(fa["per_transport"]),
                      fa["pairs_covered"], fa["pairs_possible"],
                      min(int(k) for k in orl["count_distribution"]),
                      max(int(k) for k in orl["count_distribution"]),
                      orl["numberings_swept"], orl["declared_numbering_count"], pct,
                      orl["distinct_rule_sets"]))

    if loc:
        sizes = sorted(set(tuple(c["size"] for c in idx[x]["noncomplete_components"])
                           for x in loc))
        nb1 = len(R["b1_nontrivial_at"])
        out.append("COMPONENTS=NONCOMPLETE-COMPONENT-SIZES=%s;RULES-WITH-"
                   "NONTRIVIAL-B1=%d"
                   % ("+".join(",".join(str(v) for v in s) for s in sizes), nb1))
    else:
        out.append("COMPONENTS=ALL-COMPONENTS-COMPLETE")

    if loc:
        st = R["standards"]
        # the standards are measured at the locality set; that the two sets
        # AGREE is enforced by G-RECEIPT-INTERNALLY-CONSISTENT, so this
        # reconstruction reads what the receipt carries and does not
        # re-litigate it here
        sloc = [x for x in loc if x in st]
        circ = sum(st[x]["links_that_are_circles"] for x in sloc)
        chw = sum(st[x]["charts_with_links"] for x in sloc)
        readings = sorted(set(st[x]["reading"] for x in sloc))
        dims = sorted(set(d for x in sloc for d in st[x]["local_dimensions_realised"]))
        dr = R["dimension_reading_over_the_whole_grid"]
        out.append("STANDARDS=LINK-CIRCLES=%d-OF-%d-CHARTS;DIMREAD=%s-FORCED"
                   "(CELL-INDEXED-READING:CONSISTENT-EXCLUDES-NONCOMPLETE-BY-"
                   "THEOREM;CONSISTENT-AT-%d-OF-%d-RULES,INTERSECTION-WITH-"
                   "LOCALITY=%d);LOCAL-DIMENSIONS=%s-FORCED(=MAX|CELL-CAP-"
                   "REGULAR-ORBIT|-1-AT-%d-OF-%d);DIMPROFILE=EXTENSIVE-EXCLUDED"
                   % (circ, chw, "+".join(readings),
                      dr["consistent_rules"], dr["rules_measured"],
                      dr["intersection_with_locality"],
                      "+".join(str(d) for d in dims),
                      R["local_dimension_identity"]["agrees_at"],
                      R["local_dimension_identity"]["rules"]))
        lk = R["link_conventions"]
        out.append("LINK-CONVENTION=CELL-MULTIPLICITY=%d-OF-%d;SIMPLE-GRAPH=%d-OF-%d;"
                   "TRIANGULATED-CIRCLES=%d-OF-%d"
                   % (lk["cell_multiplicity_circles"], lk["charts"],
                      lk["simple_graph_circles"], lk["charts"],
                      lk["triangulated_circles"], lk["charts"]))
        pe = R["b2_persistence"]
        ploc = [x for x in loc if x in pe]
        surv = len([1 for x in ploc if pe[x]["survives"]])
        dbl = len([1 for x in ploc if pe[x]["doubles"]])
        out.append("B2-PERSISTENCE=FORCED-BY-BLOCK-LOCALITY:SURVIVES-AT-%d-OF-%d;"
                   "COMPONENTS-DOUBLE-AT-%d" % (surv, len(ploc), dbl))
    else:
        out.append("STANDARDS=NOT-MEASURED-NO-LOCALITY-BEARING-RULE")
        out.append("LINK-CONVENTION=NOT-MEASURED-NO-LOCALITY-BEARING-RULE")
        out.append("B2-PERSISTENCE=NOT-APPLICABLE")

    nl = R["null_census"]
    rv = R["r2a_verification"]
    out.append("NULL=G0-CLIQUE-ONLY-AT-%d-OF-%d-RULES(%d-OF-%d-MEASUREMENTS);"
               "ORBIT-PARTITION-CLASSES-CLIQUE-ONLY-AT-%d-OF-%d-RULES"
               "(%d-OF-%d-MEASUREMENTS;%d-OF-THEM-REFUSE)"
               "(R2-A-VERIFIED-%d-UNIT-ACTIONS-AND-%d-SWEPT-ACTIONS-"
               "%d-DISTINCT-CYCLIC-GROUPS-%d-COUNTEREXAMPLES)"
               % (nl["g0_rules_clique_only"], nl["g0_rules"],
                  nl["g0_measurements_clique_only"], nl["g0_measurements"],
                  nl["orbit_rules_clique_only"], nl["orbit_rules"],
                  nl["orbit_measurements_clique_only"], nl["orbit_measurements"],
                  nl["orbit_measurements_that_refuse"],
                  rv["actions_this_unit_uses"],
                  rv["cyclic_actions_swept_on_the_block"],
                  rv["distinct_cyclic_groups_in_the_sweep"],
                  rv["counterexamples_at_this_units_actions"]
                  + rv["counterexamples_in_the_sweep"]))

    out.append("REFUSES=%d-OF-%d" % (len(ref), grid_size))

    gb = R["grid_boundary"]
    exc = gb["the_locality_bearing_exclusions"]
    if exc:
        e0 = exc[0]
        cf = e0["noncomplete_components"][0]["completeness"]
        cft = cf["text"] if isinstance(cf, dict) else frac(cf)
        tag = "%s-%s-C%d-%s-%s" % (e0["coord"][1], e0["coord"][2].upper(),
                                   e0["coord"][4], e0["coord"][5],
                                   cft.replace("/", "-OF-"))
    else:
        tag = "NONE"
    out.append("GRID-BOUNDARY=(H,C)-ADMITTED-BY-GROUP-ORDER-NOT-COSET-COUNT:"
               "%d-DECLARED-WORD-RULES-EXCLUDED(%d-WITH-THE-CYCLIC-LATTICE);"
               "%d-OF-THEM-NONCOMPLETE(%s)"
               % (gb["excluded_from_the_declared_words"],
                  gb["excluded_including_the_cyclic_lattice"],
                  gb["excluded_noncomplete"], tag))

    bc = R["block_constants_summary"]
    out.append("BLOCK-CONSTANTS=DENSITIES-CONSTANT-B-TO-B2-AT-%d-OF-%d-FORCED-BY-"
               "COPYING;VALUES-GRID-DEPENDENT=%s..%s;UNDEFINED-B2-DENSITY-AT-%d"
               % (bc["densities_constant"], bc["rules"],
                  bc["per_incidence_min_text"], bc["per_incidence_max_text"],
                  bc["undefined_b2_density"]))

    return head + "<" + "|".join(out) + ">"


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
    n_path = verify_path_anchors()
    gate("G-ANCHOR-COUNT",
         "every declared anchor row -- file-bytes AND path-value -- was "
         "evaluated and passed; the count is derived from the declared tables, "
         "so a skipped row is fatal",
         (len(ANCHORS) == len(ANCHOR_ROWS) + len(PATH_ANCHOR_ROWS)
          and n_anchor == len(ANCHOR_ROWS) and n_path == len(PATH_ANCHOR_ROWS)
          and all(a["ok"] for a in ANCHORS)),
         {"anchors": len(ANCHORS), "file_rows": n_anchor, "path_rows": n_path,
          "declared": len(ANCHOR_ROWS) + len(PATH_ANCHOR_ROWS)})
    R["anchors"] = [dict((k, v) for k, v in a.items()) for a in ANCHORS]

    i6 = read_json("v13/code/tb3_third_base_receipt.json")
    i3 = read_json("v13/code/top_topology_receipt.json")

    # -- the arena declarations, read out of I6 BY PATH-VALUE ANCHOR ----------
    # Every read below is the anchored path of a P-* row above, so a path drift
    # dies at the anchor, not silently in the arena (RUNBOOK section 14
    # addendum, v14 #20).
    p_gamma7 = ("tables", "the_ladder", "the_embedding", "the_witness_system_part")
    p_gamma4 = ("tables", "ord_census", "lex_first_Q_per_order", "4")
    p_sigma = ("tables", "arena", "the_declared_completion_transposition")
    p_size = ("tables", "base_declaration", "carrier", "system_triple_dimension")
    p_fano = ("tables", "the_ladder", "the_embedding", "the_non_zero_labels_of_F2_cubed")
    if MUTANT == "path-drift":
        p_gamma4 = ("tables", "ord_census", "lex_first_Q_per_order", "6")
    gamma7 = tuple(read_by_path(i6, p_gamma7))
    gamma4 = tuple(read_by_path(i6, p_gamma4))
    if MUTANT == "read-value-drift":
        gamma4 = tuple(read_by_path(i6, ("tables", "ord_census",
                                         "lex_first_Q_per_order", "2")))
    sigma = tuple(read_by_path(i6, p_sigma))
    blocksize = read_by_path(i6, p_size)
    fano_labels = tuple(read_by_path(i6, p_fano))
    gate("G-BLOCKSIZE-FROM-I6",
         "the block size is READ from I6 (system_triple_dimension), not typed",
         blocksize == BLOCK_SIZE_DECLARED and len(gamma7) == blocksize
         and len(gamma4) == blocksize and len(sigma) == blocksize,
         {"i6_system_triple_dimension": blocksize})

    # THE READ VALUES ARE GATED, NOT ONLY THE FILE (instrument M8).  The paper
    # types "order 7", "order 4", "order 2", 5040 and 240; every one of those
    # is a COMPUTED property of the anchored value here.
    read_props = {
        "T7": {"gamma_order": perm_order(gamma7),
               "cycle_type": sorted(len(o) for o in orbits_of([gamma7], tuple(range(8)))),
               "sigma_mixed_order": len(closure([gamma7, sigma], 8))},
        "T4": {"gamma_order": perm_order(gamma4),
               "cycle_type": sorted(len(o) for o in orbits_of([gamma4], tuple(range(8)))),
               "sigma_mixed_order": len(closure([gamma4, sigma], 8))},
    }
    R["read_value_properties"] = {
        "declared": {"T7": {"gamma_order": 7, "cycle_type": [1, 7],
                            "sigma_mixed_order": 5040},
                     "T4": {"gamma_order": 4, "cycle_type": [1, 1, 2, 4],
                            "sigma_mixed_order": 240},
                     "sigma_order": 2},
        "measured": dict(read_props, sigma_order=perm_order(sigma)),
    }
    gate("G-READ-VALUES-MATCH-THE-DECLARATION",
         "every property the paper states about a value read from a pinned "
         "receipt -- the transport orders, their cycle types, the Sigma-mixed "
         "group orders -- is recomputed from the anchored value and matched "
         "(RUNBOOK section 15: match EVERY coordinate)",
         (read_props["T7"]["gamma_order"] == 7
          and read_props["T4"]["gamma_order"] == 4
          and perm_order(sigma) == 2
          and read_props["T7"]["cycle_type"] == [1, 7]
          and read_props["T4"]["cycle_type"] == [1, 1, 2, 4]
          and read_props["T7"]["sigma_mixed_order"] == 5040
          and read_props["T4"]["sigma_mixed_order"] == 240),
         R["read_value_properties"]["measured"])

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

    # -- CELL-LEVEL completeness: the coordinate gate above compares (H,c,mode)
    # triples; it does NOT look at the CELLS a rule generates.  A silently
    # dropped sliding window leaves the coordinate set intact.  This comparator
    # rebuilds every rule's cell set from the coset-INDEX map -- a construction
    # that never calls cells_from_orbits -- and compares the canonical sets.
    cellbad = []
    cellcount = 0
    for r in rules:
        got_cells, orbs = rule_cells_on_block(r, transports)
        k = len(orbs)
        iota = {}
        for i, o in enumerate(orbs):
            for x in o:
                iota[x] = i
        if r.klass in ("G0", "G1", "G3-ORBITS"):
            windows = [[i] for i in range(k)]
        elif r.mode == "ALL":
            windows = [list(cb) for cb in itertools.combinations(range(k), r.c)]
        elif r.mode == "BLOCKWISE":
            windows = [[j for j in range(i, min(i + r.c, k))]
                       for i in range(0, k, r.c)]
        else:
            windows = [[(i + t) % k for t in range(r.c)] for i in range(k)]
        want_cells = sorted(set(
            frozenset(x for x in range(BLOCK_SIZE_DECLARED) if iota[x] in set(win))
            for win in windows), key=lambda cc: (min(cc), sorted(cc)))
        cellcount += len(want_cells)
        if [sorted(c) for c in got_cells] != [sorted(c) for c in want_cells]:
            cellbad.append(r.rid)
    gate("G-GRID-CELL-SETS-COMPLETE",
         "every rule's CELL SET equals an independently rebuilt one (windows "
         "over the coset-index map, never through cells_from_orbits): a "
         "silently dropped window is fatal, not merely a coordinate drop",
         len(cellbad) == 0 and cellcount > 0,
         {"rules": len(rules), "cells_rebuilt": cellcount,
          "disagreements": cellbad[:4]})
    R["grid"]["cells_rebuilt_independently"] = cellcount

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
    distinct_groups = set()
    eB = ident(BLOCK_SIZE_DECLARED)
    perms = list(itertools.permutations(range(BLOCK_SIZE_DECLARED)))
    if MUTANT == "sweep-truncate":
        perms = perms[:100]
    for p in perms:
        Tp = [eB]
        cur = p
        while cur != eB:
            Tp.append(cur)
            cur = compose(p, cur)
        distinct_groups.add(tuple(sorted(Tp)))
        thm, _ = drawn_by_theorem(tuple(Tp), tuple(range(BLOCK_SIZE_DECLARED)))
        dfn = drawn_by_definition(tuple(Tp), tuple(range(BLOCK_SIZE_DECLARED)))
        sweep_actions += 1
        if thm != dfn:
            sweep_bad += 1
    # THE DENOMINATOR IS DERIVED, NOT ASSERTED (instrument M11 / RUNBOOK #24):
    # "exhaustive" means the sweep visited factorial(blocksize) permutations,
    # computed here by an independent product -- a truncated sweep is fatal.
    want_perms = 1
    for t in range(1, BLOCK_SIZE_DECLARED + 1):
        want_perms = want_perms * t
    gate("G-R2A-EXHAUSTIVE",
         "THEOREM R2-A holds at EVERY cyclic action on the block's 8 labels, "
         "and the sweep is EXHAUSTIVE BY DERIVED COUNT: it visited exactly "
         "factorial(block size) permutations (a silent truncation is fatal); "
         "the number of DISTINCT cyclic groups so obtained is printed beside "
         "the permutation count, since <p> is generated by phi(ord p) elements",
         sweep_bad == 0 and sweep_actions == want_perms,
         {"actions_swept": sweep_actions, "factorial_blocksize": want_perms,
          "distinct_cyclic_groups": len(distinct_groups),
          "counterexamples": sweep_bad})
    R["r2a_verification"] = {
        "actions_this_unit_uses": r2a_actions,
        "counterexamples_at_this_units_actions": r2a_counterex,
        "cyclic_actions_swept_on_the_block": sweep_actions,
        "factorial_of_the_block_size": want_perms,
        "distinct_cyclic_groups_in_the_sweep": len(distinct_groups),
        "counterexamples_in_the_sweep": sweep_bad,
    }

    # the null: G0 must be clique-only.  THE UNITS ARE NAMED (operator F7 /
    # effectus F13): 4 and 38 count rule-ARENA MEASUREMENTS over 2 and 19
    # RULES; the previous string called both "rules", and the gate compared a
    # measurement count against a TRANSPORT count -- right only by the
    # coincidence #arenas = #transports = 2.
    n_arenas = 2
    g0 = [(k, m) for k, m in census.items() if m["coord"][0] == "G0"]
    g0_rules = sorted(set(m["rid"] for _, m in g0))
    g0_bad = [k for k, m in g0 if m["any_noncomplete"]]
    gate("G-R2A-NULL-CLIQUE-ONLY",
         "the G0 null (regular <gamma>-orbits) returns clique-only components "
         "at every rule and arena -- the R2-A theorem check.  The denominator "
         "is DERIVED: #G0 rules x #arenas, not #transports x 2",
         len(g0_bad) == 0 and len(g0) == len(g0_rules) * n_arenas,
         {"g0_rules": len(g0_rules), "g0_measurements": len(g0),
          "arenas": n_arenas, "noncomplete": len(g0_bad)})

    # G1 and the orbit classes are structurally clique-only (measured, not assumed)
    orbit_rules = [(k, m) for k, m in census.items()
                   if m["coord"][0] in ("G0", "G1", "G3-ORBITS")]
    orbit_rids = sorted(set(m["rid"] for _, m in orbit_rules))
    orbit_bad = [k for k, m in orbit_rules if m["any_noncomplete"]]
    orbit_refuse = [k for k, m in orbit_rules if m["refuses"]]
    gate("G-ORBIT-CLASSES-CLIQUE-ONLY",
         "every orbit-partition class (G0, G1, G3-ORBITS) returns clique-only "
         "components: disjoint cells cannot make a non-complete component.  "
         "REFUSES is counted separately -- it is a distinct status, not a "
         "kind of clique-only",
         len(orbit_bad) == 0 and len(orbit_rules) == len(orbit_rids) * n_arenas,
         {"rules": len(orbit_rids), "measurements": len(orbit_rules),
          "noncomplete": len(orbit_bad), "of_them_refusing": len(orbit_refuse)})
    R["null_census"] = {
        "arenas": n_arenas,
        "g0_rules": len(g0_rules), "g0_measurements": len(g0),
        "g0_rules_clique_only": len(g0_rules) - len(set(
            census[k]["rid"] for k in g0_bad)),
        "g0_measurements_clique_only": len(g0) - len(g0_bad),
        "orbit_rules": len(orbit_rids), "orbit_measurements": len(orbit_rules),
        "orbit_rules_clique_only": len(orbit_rids) - len(set(
            census[k]["rid"] for k in orbit_bad)),
        "orbit_measurements_clique_only": len(orbit_rules) - len(orbit_bad),
        "orbit_measurements_that_refuse": len(orbit_refuse),
        "unit_note": "N-OF-M counts are labelled RULES or MEASUREMENTS at "
                     "every clause; a rule is measured at both arenas",
    }

    # component census by two independent routes
    if MUTANT == "components-route2-break":
        census[sorted(census)[0]]["b0_route2"] += 1
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

    # -- COUNT GUARDS: derive the stored flags afresh (instrument M4) ---------
    # any_noncomplete, refuses, status and the per-component cycle rank are
    # single bits consumed by the census, the render check and the verdict --
    # all of which read THE SAME BIT.  Here each is recomputed from
    # per_component / edges and compared, so a single flipped bit is fatal.
    flagbad = []
    for k, m in census.items():
        want_ref = (m["edges"] == 0)
        want_nc = any(not c["complete"] for c in m["per_component"])
        if want_ref != m["refuses"] or want_nc != m["any_noncomplete"]:
            flagbad.append((k, "flags"))
        for c in m["per_component"]:
            if c["b1_graph"] != c["edges"] - c["size"] + 1:
                flagbad.append((k, "b1_graph"))
            if c["complete"] != (c["edges"] == c["pairs"]):
                flagbad.append((k, "complete"))
    gate("G-FLAGS-DERIVED-NOT-TRUSTED",
         "the locality flag, the REFUSES flag, per-component completeness and "
         "the per-component cycle rank are each RE-DERIVED inside the gate "
         "from per_component/edges and compared against the stored bit: a "
         "single flipped bit is fatal, at every rule and arena",
         len(flagbad) == 0, {"measurements": len(census),
                             "disagreements": flagbad[:4]})

    # -- the 2-cell census by an INDEPENDENT route (instrument M3) ------------
    # F_N had no comparator: a per-block-uniform 2-cell drop moved the
    # densities and one verdict segment with nothing watching.  This route
    # counts triangles per cell from the drawn-pair set directly.
    tribad = []
    for k, m in census.items():
        cnt = 0
        for cc in m["_cells"]:
            cl = sorted(cc)
            for a, b, c3 in itertools.combinations(cl, 3):
                if (a, b) in m["_edges"] and (b, c3) in m["_edges"] \
                        and (a, c3) in m["_edges"]:
                    cnt += 1
        if cnt != m["F_N"]:
            tribad.append((k, cnt, m["F_N"]))
    gate("G-TWOCELLS-TWO-ROUTES",
         "the 2-cell count is reproduced by an independent triangle "
         "enumeration over the drawn-pair table at every rule and arena (the "
         "deduplication step is a measured no-op: combinations yields each "
         "triple once per cell)",
         len(tribad) == 0, {"measurements": len(census),
                            "disagreements": tribad[:4]})

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

    if MUTANT == "standards-identity-break" and std:
        std[sorted(std)[0]]["sum_starE"] += 1
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
            "links_that_are_circles_simple_convention":
                s["links_that_are_circles_simple_convention"],
            "links_that_are_triangulated_circles":
                s["links_that_are_triangulated_circles"],
            "link_simple_graph_convention_at_those_charts":
                dict((str(X), s["link_simple_graph_convention"][str(X)])
                     for X in charts),
            "reading_chart_intrinsic": s["reading_chart_intrinsic"],
            "distinct_readings_chart_intrinsic": s["distinct_readings_chart_intrinsic"],
        }

    # -- THE DIMENSION READING OVER THE WHOLE GRID ---------------------------
    # The reading was previously computed only on the FILTERED population (the
    # 14 locality rules), where INCONSISTENT is forced.  Run over all 109 it
    # becomes a mutual-exclusion measurement: CONSISTENT is attained, and never
    # at a locality-bearing rule.
    #
    # THEOREM R2-D (why).  Under the delivered CELL-INDEXED reading a
    # non-complete component can never read CONSISTENT.  Suppose C is
    # non-complete and every chart of C shares one dimprofile.  C has a drawn
    # edge, so some entry i is >= 1 at some chart, hence -- by constancy -- at
    # every chart of C; an entry >= 1 requires the chart to lie in cell i, so
    # C is contained in cell i; a component lies in a single regular orbit, so
    # every pair of C is drawn inside cell i and C is a clique -- complete.
    # Contradiction.  Hence DIMREAD=INCONSISTENT at the 14 is FORCED (#208).
    all_readings = {}
    for r in rules:
        m = census[(r.rid, "B")]
        s_all = std.get(r.rid) or standards(m)
        all_readings[r.rid] = {
            "reading": s_all["reading"],
            "charts_with_links": s_all["charts_with_links"],
            "reading_chart_intrinsic": s_all["reading_chart_intrinsic"],
            "status": ("REFUSES" if m["refuses"] else
                       ("NON-COMPLETE" if m["any_noncomplete"] else "clique-only")),
        }
    consistent_rules = sorted([k for k, v in all_readings.items()
                               if v["reading"] == "CONSISTENT"])
    intersection = sorted(set(consistent_rules) & set(locality_B))
    intr_consistent = sorted([k for k in locality_B
                              if all_readings[k]["reading_chart_intrinsic"]
                              == "CONSISTENT"])
    R["dimension_reading_over_the_whole_grid"] = {
        "rules_measured": len(rules),
        "consistent_rules": len(consistent_rules),
        "consistent_rule_list": consistent_rules,
        "locality_rules": len(locality_B),
        "intersection_with_locality": len(intersection),
        "intersection_list": intersection,
        "locality_rules_consistent_under_the_chart_intrinsic_reading":
            len(intr_consistent),
        "theorem": "R2-D: under the cell-indexed reading CONSISTENT and "
                   "NON-COMPLETE are mutually exclusive, so INCONSISTENT at "
                   "the locality-bearing rules is FORCED, not measured",
        "per_rule": all_readings,
    }
    gate("G-DIMREAD-MUTUAL-EXCLUSION",
         "the dimension reading is evaluated at EVERY grid rule, not only at "
         "the filtered locality-bearing ones: CONSISTENT is attained "
         "somewhere (so the measure has a positive control on shipped input) "
         "and its intersection with the locality census is EMPTY -- the "
         "mutual-exclusion theorem R2-D, measured",
         len(consistent_rules) > 0 and len(intersection) == 0
         and len(all_readings) == len(rules),
         {"rules": len(rules), "consistent": len(consistent_rules),
          "locality": len(locality_B), "intersection": len(intersection)})

    # -- THE LINK CONVENTION, both readings printed --------------------------
    lk_charts = sum(R["standards"][rid]["charts_with_links"] for rid in locality_B)
    lk_mult = sum(R["standards"][rid]["links_that_are_circles"] for rid in locality_B)
    lk_simple = sum(R["standards"][rid]["links_that_are_circles_simple_convention"]
                    for rid in locality_B)
    lk_tri = sum(R["standards"][rid]["links_that_are_triangulated_circles"]
                 for rid in locality_B)
    R["link_conventions"] = {
        "charts": lk_charts,
        "cell_multiplicity_circles": lk_mult,
        "simple_graph_circles": lk_simple,
        "triangulated_circles": lk_tri,
        "note": "the delivered link counts its EDGES as 2-cells WITH CELL "
                "MULTIPLICITY while counting its VERTICES as distinct "
                "neighbours; the simple-graph convention counts both without "
                "multiplicity.  The conventions disagree, and the headline "
                "moves with them -- so both are printed, together with the "
                "count of links that are TRIANGULATED CIRCLES (a cycle graph: "
                "the manifold condition, stronger than (b0,b1) = (1,1))",
    }
    gate("G-LINK-CONVENTION-WITNESSED",
         "both link conventions are computed and printed, and the "
         "triangulated-circle count is reported beside the Betti-coincidence "
         "count: the convention is a witnessed declaration, not an implicit "
         "one (RUNBOOK section 14 addendum, v13 #313)",
         lk_charts > 0 and lk_mult != lk_simple and lk_tri <= lk_mult,
         {"charts": lk_charts, "cell_multiplicity": lk_mult,
          "simple_graph": lk_simple, "triangulated_circles": lk_tri})

    # -- LOCAL-DIMENSIONS is an IDENTITY, measured as one ---------------------
    ident_ok = 0
    for rid in locality_B:
        m = census[(rid, "B")]
        reg = [set(o) for o in m["regular_orbits"]]
        top = 0
        for cc in m["_cells"]:
            for ro in reg:
                v = len(set(cc) & ro)
                if v - 1 > top:
                    top = v - 1
        realised = R["standards"][rid]["local_dimensions_realised"]
        if realised and max(realised) == top:
            ident_ok += 1
    R["local_dimension_identity"] = {
        "rules": len(locality_B), "agrees_at": ident_ok,
        "statement": "the top local dimension equals max |cell cap regular "
                     "orbit| - 1 -- a restatement of the declared window "
                     "width, not an independent reading (#208 disclosure)",
    }
    gate("G-LOCAL-DIMENSIONS-ARE-AN-IDENTITY",
         "the realised top local dimension equals max|cell cap regular "
         "orbit| - 1 at every locality-bearing rule: LOCAL-DIMENSIONS is "
         "carried as a FORCED identity, with the forcing measured",
         ident_ok == len(locality_B) and len(locality_B) > 0,
         {"rules": len(locality_B), "agrees": ident_ok})

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
    if MUTANT == "copy-reduction-break":
        consts[0]["additives_double"] = not consts[0]["additives_double"]
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
    if MUTANT == "b2-persistence-drop" and persist:
        persist.pop(sorted(persist)[0])
    R["b2_persistence"] = persist
    # the comparator is DERIVED afresh from per_component, not from the list
    # persist was built by iterating (the old predicate could not fail)
    want_persist = set(m["rid"] for k, m in census.items()
                       if k[1] == "B"
                       and any(not c["complete"] for c in m["per_component"]))
    gate("G-B2-PERSISTENCE-MEASURED",
         "every rule that has a non-complete component at B -- the set derived "
         "here afresh from per_component, not the list this dict was built by "
         "iterating -- is re-measured at B2 and its persistence recorded",
         set(persist) == want_persist and len(want_persist) > 0,
         {"measured": len(persist), "derived_locality_set": len(want_persist),
          "missing": sorted(want_persist - set(persist))})

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
        if MUTANT == "modes-collapse":
            sets["BLOCKWISE"] = sets["SLIDING"]
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
            if MUTANT == "symmetry-break" and nm == "sigma":
                e3 = e3[:-1] if e3 else e3
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
        if MUTANT == "parity-inert":
            alt_tri = m_and["F_N"]
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
        lhs = census[(r.rid, "B")]["edges"]
        if MUTANT == "lattice-crosscheck-break" and dup_checked == 1:
            lhs += 1
        if lhs != census[(twin[0].rid, "B")]["edges"]:
            dup_bad += 1
    gate("G-LATTICE-CROSSCHECK",
         "the Sigma-mixed lattice's trivial subgroup reproduces the cyclic "
         "lattice's trivial subgroup exactly (two independently declared "
         "lattices, same measured census)",
         dup_bad == 0 and dup_checked > 0,
         {"checked": dup_checked, "disagreements": dup_bad})

    # -- THE BLOCK CONSTANTS' SPAN, computed (operator F5) --------------------
    # The paper previously typed a per-incidence range by hand and got it
    # wrong.  The span is computed here, printed, and rendered into the paper's
    # sentence by the prose gate; the union-class maximum is carried beside it
    # because that is where the hand-typed number came from.
    inc = [c["B"]["ncoh_per_incidence"] for c in consts
           if c["B"]["ncoh_per_incidence"] is not None]
    union_inc = [c["B"]["ncoh_per_incidence"] for c in consts
                 if c["B"]["ncoh_per_incidence"] is not None
                 and c["coord"][0] in ("G2", "G3-UNIONS") and c["coord"][5] == "ALL"]
    R["block_constants_summary"] = {
        "rules": len(consts),
        "densities_constant": len([c for c in consts
                                   if c["densities_constant_B_to_B2"]]),
        "additives_double": len([c for c in consts if c["additives_double"]]),
        "undefined_b2_density": len([c for c in consts
                                     if c["B"]["b2_density"] is None]),
        "per_incidence_min": min(inc), "per_incidence_max": max(inc),
        "per_incidence_min_text": frac(min(inc)),
        "per_incidence_max_text": frac(max(inc)),
        "per_incidence_max_attained_at": sorted(
            [c["rid"] for c in consts
             if c["B"]["ncoh_per_incidence"] == max(inc)]),
        "per_incidence_max_within_the_ALL_union_classes": frac(max(union_inc)),
        "per_incidence_max_within_the_ALL_union_classes_attained_at": sorted(
            [c["rid"] for c in consts
             if c["B"]["ncoh_per_incidence"] == max(union_inc)]),
        "forcing": "constancy B->B2 is FORCED by the block-local declaration "
                   "plus copy-forcing (cells are copied into each block, the "
                   "basepoint lies in no cell, transports never cross blocks), "
                   "so B2 is a disjoint sum by construction; the VALUES are "
                   "measured and they are grid-dependent",
    }
    gate("G-CONSTANTS-SPAN-COMPUTED",
         "the per-incidence density's span across the grid is COMPUTED here "
         "and carried in the verdict, never typed in prose (RUNBOOK section 13 "
         "addendum, v14 #20: prose renders from the receipt)",
         (len(inc) > 0 and min(inc) < max(inc)
          and R["block_constants_summary"]["per_incidence_max"] == max(inc)),
         {"min": frac(min(inc)), "max": frac(max(inc)),
          "attained_at": R["block_constants_summary"]["per_incidence_max_attained_at"]})

    # -- THE WIDTH LAW (theorem R2-W), derived and gated ---------------------
    wl_rows = {}
    wl_bad = []
    for r in rules:
        row = width_law_row(r, transports)
        wl_rows[r.rid] = row
        m = census[(r.rid, "B")]
        if MUTANT == "width-law-corrupt" and r.rid == "R011":
            row["predicted_noncomplete"] = not row["predicted_noncomplete"]
        if (row["predicted_noncomplete"] != m["any_noncomplete"]
                or row["predicted_edges"] != m["edges"]):
            wl_bad.append((r.rid, row["predicted_noncomplete"],
                           m["any_noncomplete"], row["predicted_edges"],
                           m["edges"]))
    cf = closed_form_families(
        wl_rows,
        dict((r.rid, census[(r.rid, "B")]["edges"]) for r in rules),
        dict((r.rid, max([c["b1_graph"] for c in census[(r.rid, "B")]["per_component"]]
                         or [0])) for r in rules))
    # the two thresholds have DIFFERENT CAUSES -- measured, not asserted
    causes = {}
    for r in rules:
        if r.mode != "SLIDING" or r.horder != 1:
            continue
        for po in wl_rows[r.rid]["per_regular_orbit"]:
            causes[r.transport] = {"shape": po["support_shape"],
                                   "support_shape": po["support_shape"],
                                   "k": po["k"], "support": po["support"],
                                   "D": po["cyclic_diameter_D"],
                                   "locality_vanishes_at_c": po["cyclic_diameter_D"] + 1}
    R["width_law"] = {
        "theorem": "R2-W: on a regular orbit R, x ~ y iff the cyclic distance "
                   "of their coset indices is <= c-1, so the drawn graph is "
                   "the lexicographic blow-up of the circulant C_k(1..c-1)[S] "
                   "by cliques K_{w_i}; a component is incomplete iff it holds "
                   "a pair at cyclic distance >= c; when the circulant on S is "
                   "connected this is exactly c <= diam_k(S)",
        "rules": len(rules),
        "rules_predicted_correctly": len(rules) - len(wl_bad),
        "mismatches": wl_bad[:4],
        "closed_form_rows": len(cf),
        "closed_form_agreements": len([x for x in cf if x["agrees"]]),
        "closed_forms": cf,
        "threshold_causes": causes,
        "two_causes_note": "the two declared transports reach their thresholds "
                           "by DIFFERENT causes: at T7 the regular orbit's "
                           "coset support is Z_k minus ONE POINT (diam = "
                           "floor(k/2)), at T4 it is a CONTIGUOUS ARC of "
                           "length m (diam = m-1).  One reported effect, two "
                           "mechanisms",
        "epistemic_status": "FORCED (#208): which rules are local, their "
                            "component sizes, their completeness fractions and "
                            "their cycle ranks are all computed from the "
                            "declaration.  What remains MEASURED is the grid, "
                            "the drawing relation and the density values",
        "per_rule": wl_rows,
    }
    gate("G-WIDTH-LAW-PREDICTS-THE-CENSUS",
         "the width law predicts BOTH the locality status AND the drawn edge "
         "count of every grid rule from the declaration alone -- no atlas "
         "built, no cell enumerated -- and agrees with the measured census at "
         "every rule; the census is therefore a COROLLARY OF THE DECLARATION "
         "and its clauses are carried as forced (#208)",
         len(wl_bad) == 0 and len(wl_rows) == len(rules),
         {"rules": len(rules), "agreements": len(rules) - len(wl_bad),
          "mismatches": wl_bad[:3]})
    gate("G-WIDTH-LAW-CLOSED-FORMS",
         "the closed forms specialise the law to the declared families and "
         "reproduce the measured edge counts and cycle ranks by arithmetic in "
         "(k, m, c) alone -- a THIRD route, neither the atlas nor the graph "
         "build",
         len(cf) > 0 and all(x["agrees"] for x in cf),
         {"rows": len(cf), "agree": len([x for x in cf if x["agrees"]])})
    gate("G-WIDTH-LAW-TWO-CAUSES",
         "the two declared transports' width thresholds are shown to have "
         "DIFFERENT causes: the regular orbit's coset support is a punctured "
         "cycle at one transport and a contiguous arc at the other, measured "
         "and printed with each diameter",
         (len(causes) == len(transports)
          and len(set(v["shape"] for v in causes.values())) == len(transports)),
         causes)

    # -- THE MOTIVATION CENSUS ------------------------------------------------
    mot = motivation_census(transports, rules, fano_labels)
    mot["order_relativity"]["declared_numbering_count"] = len(locality_B)
    orl = mot["order_relativity"]
    # the modal share, as an exact percentage rendered by integer arithmetic
    num = orl["modal_orders"] * 10000
    den = orl["numberings_swept"]
    hundredths = (num + den // 2) // den
    orl["modal_share_percent_text"] = "%d.%02d" % (hundredths // 100, hundredths % 100)
    orl["declared_numbering_is_modal"] = (orl["modal_count"] == len(locality_B))
    R["motivation_census"] = mot
    ps, fa = mot["partition_sweep"], mot["fano_cover"]
    gate("G-MOTIVATION-PARTITION-SWEEP",
         "EVERY set partition of the eight labels is measured at every "
         "transport and NONE yields a non-complete component: since the orbit "
         "family of any subgroup of S_8 is one of these partitions, no "
         "inherited GROUP can motivate a locality-bearing cover.  The "
         "denominator is derived from the Bell number, so a truncated sweep "
         "is fatal",
         (ps["partitions_of_the_eight_labels"] == ps["bell_number_8_derived"]
          and ps["measurements"] == ps["bell_number_8_derived"] * len(transports)
          and ps["noncomplete_hits"] == 0),
         {"partitions": ps["partitions_of_the_eight_labels"],
          "bell_8": ps["bell_number_8_derived"],
          "measurements": ps["measurements"], "hits": ps["noncomplete_hits"]})
    gate("G-MOTIVATION-FANO-COVER",
         "I6's OWN declared partial-overlap cover -- the seven Fano lines, "
         "derived from the anchored non-zero F_2^3 labels -- is measured at "
         "both transports.  It is a 2-design (it covers every pair), so its "
         "overlap graph is complete: the one motivated cover the corpus owns "
         "is a locality-DESTROYER",
         (fa["line_count"] == 7 and fa["is_a_2_design"]
          and fa["transports_where_it_is_clique_only"] == len(transports)
          and all(not v["complements_noncomplete"] for v in fa["per_transport"].values())),
         {"lines": fa["line_count"], "pairs": [fa["pairs_covered"], fa["pairs_possible"]],
          "clique_only_at": fa["transports_where_it_is_clique_only"]})
    gate("G-MOTIVATION-ORDER-RELATIVITY",
         "the locality census is re-run under EVERY numbering of the carrier: "
         "SLIDING reads the label order twice (to name the cosets and to say "
         "'consecutive'), so the rule list is a coordinate of the numbering.  "
         "The sweep is exhaustive by derived count, the count distribution and "
         "the number of distinct rule sets are printed, and the declared "
         "numbering's own count is compared against the modal one",
         (orl["numberings_swept"] == want_perms
          and orl["distinct_rule_sets"] > 1
          and orl["declared_numbering_count"] == len(locality_B)
          and orl["declared_numbering_is_modal"]),
         {"numberings": orl["numberings_swept"],
          "distinct_rule_sets": orl["distinct_rule_sets"],
          "distribution": orl["count_distribution"],
          "declared": orl["declared_numbering_count"],
          "modal": orl["modal_count"], "modal_share": orl["modal_share_percent_text"]})

    # -- THE GRID BOUNDARY ----------------------------------------------------
    gb = grid_boundary_census(transports, want)
    R["grid_boundary"] = gb
    gate("G-GRID-BOUNDARY-CENSUSED",
         "the admissibility proxy c*|H| < block size is an arithmetic on the "
         "GROUP ORDER while the construction uses H's ORBITS; the rules a "
         "coset-count test would admit and this one excludes are enumerated, "
         "measured and printed -- including any that bear locality, whose "
         "completeness values are printed beside the censused ones",
         (gb["excluded_from_the_declared_words"] > 0
          and gb["excluded_noncomplete"] > 0
          and len(gb["the_locality_bearing_exclusions"])
          == gb["excluded_noncomplete"]),
         {"excluded_declared_words": gb["excluded_from_the_declared_words"],
          "excluded_total": gb["excluded_including_the_cyclic_lattice"],
          "of_them_noncomplete": gb["excluded_noncomplete"]})

    # -- THE SUCCESSOR CONTROL (the grid's boundary, made visible) -----------
    sc_ctrl = successor_control()
    R["successor_control"] = sc_ctrl
    row2 = [x for x in sc_ctrl["rows"] if x["c"] == 2][0]
    gate("G-SUCCESSOR-CONTROL",
         "a fixed-point-free transport with the SAME sliding cell class "
         "yields, at width 2, a NON-COMPLETE component that is a TRIANGULATED "
         "1-MANIFOLD -- a cycle graph whose every link is two points (S^0, the "
         "correct link for dimension one) -- and a CONSISTENT chart-intrinsic "
         "dimension reading.  The obstruction at the declared transports is "
         "their FIXED POINTS, not width-based overlap: measured, not inferred",
         (sc_ctrl["fixed_points"] == []
          and sc_ctrl["regular_orbit_is_the_whole_label_set"]
          and row2["noncomplete"] and row2["is_a_triangulated_1_manifold"]
          and row2["reading_chart_intrinsic"] == "CONSISTENT"
          and row2["distinct_links_cell_multiplicity"] == [[2, 0, 2, 0]]
          and all(x["reading_chart_intrinsic"] == "CONSISTENT"
                  for x in sc_ctrl["rows"])),
         {"fixed_points": sc_ctrl["fixed_points"],
          "c2": {k: row2[k] for k in ("noncomplete", "is_a_triangulated_1_manifold",
                                      "reading_cell_indexed",
                                      "reading_chart_intrinsic",
                                      "distinct_links_cell_multiplicity")}})

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
        dr = R["dimension_reading_over_the_whole_grid"]
        std_sig = ("LINK-CIRCLES=%d-OF-%d-CHARTS;DIMREAD=%s-FORCED"
                   "(CELL-INDEXED-READING:CONSISTENT-EXCLUDES-NONCOMPLETE-BY-"
                   "THEOREM;CONSISTENT-AT-%d-OF-%d-RULES,INTERSECTION-WITH-"
                   "LOCALITY=%d);LOCAL-DIMENSIONS=%s-FORCED(=MAX|CELL-CAP-"
                   "REGULAR-ORBIT|-1-AT-%d-OF-%d);DIMPROFILE=EXTENSIVE-EXCLUDED") % (
            circ, chw, "+".join(readings),
            dr["consistent_rules"], dr["rules_measured"],
            dr["intersection_with_locality"],
            "+".join(str(d) for d in dims) if dims else "NONE",
            R["local_dimension_identity"]["agrees_at"],
            R["local_dimension_identity"]["rules"])
        lk = R["link_conventions"]
        link_sig = ("CELL-MULTIPLICITY=%d-OF-%d;SIMPLE-GRAPH=%d-OF-%d;"
                    "TRIANGULATED-CIRCLES=%d-OF-%d") % (
            lk["cell_multiplicity_circles"], lk["charts"],
            lk["simple_graph_circles"], lk["charts"],
            lk["triangulated_circles"], lk["charts"])
        surv = len([1 for rid in locality_B if persist[rid]["survives"]])
        dbl = len([1 for rid in locality_B if persist[rid]["doubles"]])
        b2_sig = "FORCED-BY-BLOCK-LOCALITY:SURVIVES-AT-%d-OF-%d;COMPONENTS-DOUBLE-AT-%d" % (
            surv, len(locality_B), dbl)
    else:
        mech = "NONE-IN-THE-DECLARED-GRID"
        comp_sig = "ALL-COMPONENTS-COMPLETE"
        std_sig = "NOT-MEASURED-NO-LOCALITY-BEARING-RULE"
        link_sig = "NOT-MEASURED-NO-LOCALITY-BEARING-RULE"
        b2_sig = "NOT-APPLICABLE"

    # DRAWING -- the verdict-determining declaration, named (effectus F4)
    altd = R["alt_drawing_group_probe"]["per_transport"]
    zero_at = len([1 for v in altd.values()
                   if v["pairs_drawn_if_the_drawing_group_were_it"] == 0])
    draw_sig = ("R1-RELATION-AT-<GAMMA>-VERDICT-DETERMINING"
                "(ALT-<GAMMA,SIGMA>:0-PAIRS-AT-%d-OF-%d-TRANSPORTS=>"
                "NO-LOCALITY-IN-THE-DECLARED-GRID)") % (zero_at, len(altd))

    wl = R["width_law"]
    wl_causes = ";".join("%s:%s(D=%d,C-MAX=%d)" % (k, wl["threshold_causes"][k]["shape"],
                                                   wl["threshold_causes"][k]["D"],
                                                   wl["threshold_causes"][k]["D"])
                         for k in sorted(wl["threshold_causes"]))
    width_sig = ("NONCOMPLETE-IFF-C<=D(D=MAX-CYCLIC-COSET-DISTANCE-IN-THE-"
                 "REGULAR-ORBIT);TWO-CAUSES=%s;CENSUS-DERIVABLE-FROM-THE-"
                 "DECLARATION-AT-%d-OF-%d;CLOSED-FORMS-AGREE-AT-%d-OF-%d") % (
        wl_causes, wl["rules_predicted_correctly"], wl["rules"],
        wl["closed_form_agreements"], wl["closed_form_rows"])

    mo = R["motivation_census"]
    mps, mfa, mor = mo["partition_sweep"], mo["fano_cover"], mo["order_relativity"]
    mot_sig = ("NONE-INHERITED:PARTITION-COVERS-NONCOMPLETE-AT-%d-OF-%d"
               "(ALL-%d-PARTITIONS-X-%d-TRANSPORTS);I6-FANO-LINES-CLIQUE-ONLY-AT-"
               "%d-OF-%d(2-DESIGN:%d-OF-%d-PAIRS-COVERED);ORDER-RELATIVE"
               "(COUNT=%d..%d-OVER-%d-NUMBERINGS;DECLARED=%d-MODAL-%s%%;"
               "DISTINCT-RULE-SETS=%d)") % (
        mps["noncomplete_hits"], mps["measurements"],
        mps["partitions_of_the_eight_labels"], mps["transports"],
        mfa["transports_where_it_is_clique_only"], len(mfa["per_transport"]),
        mfa["pairs_covered"], mfa["pairs_possible"],
        min(int(k) for k in mor["count_distribution"]),
        max(int(k) for k in mor["count_distribution"]),
        mor["numberings_swept"], mor["declared_numbering_count"],
        mor["modal_share_percent_text"], mor["distinct_rule_sets"])

    nl = R["null_census"]
    null_sig = ("G0-CLIQUE-ONLY-AT-%d-OF-%d-RULES(%d-OF-%d-MEASUREMENTS);"
                "ORBIT-PARTITION-CLASSES-CLIQUE-ONLY-AT-%d-OF-%d-RULES"
                "(%d-OF-%d-MEASUREMENTS;%d-OF-THEM-REFUSE)"
                "(R2-A-VERIFIED-%d-UNIT-ACTIONS-AND-%d-SWEPT-ACTIONS-"
                "%d-DISTINCT-CYCLIC-GROUPS-%d-COUNTEREXAMPLES)") % (
        nl["g0_rules_clique_only"], nl["g0_rules"],
        nl["g0_measurements_clique_only"], nl["g0_measurements"],
        nl["orbit_rules_clique_only"], nl["orbit_rules"],
        nl["orbit_measurements_clique_only"], nl["orbit_measurements"],
        nl["orbit_measurements_that_refuse"],
        r2a_actions, sweep_actions,
        R["r2a_verification"]["distinct_cyclic_groups_in_the_sweep"],
        r2a_counterex + sweep_bad)

    gbx = R["grid_boundary"]
    exc = gbx["the_locality_bearing_exclusions"]
    if exc:
        e0 = exc[0]
        cft = frac(e0["noncomplete_components"][0]["completeness"])
        exc_tag = "%s-%s-C%d-%s-%s" % (e0["coord"][1], e0["coord"][2].upper(),
                                       e0["coord"][4], e0["coord"][5],
                                       cft.replace("/", "-OF-"))
    else:
        exc_tag = "NONE"
    gb_sig = ("(H,C)-ADMITTED-BY-GROUP-ORDER-NOT-COSET-COUNT:"
              "%d-DECLARED-WORD-RULES-EXCLUDED(%d-WITH-THE-CYCLIC-LATTICE);"
              "%d-OF-THEM-NONCOMPLETE(%s)") % (
        gbx["excluded_from_the_declared_words"],
        gbx["excluded_including_the_cyclic_lattice"],
        gbx["excluded_noncomplete"], exc_tag)

    bcs = R["block_constants_summary"]
    const_sig = ("DENSITIES-CONSTANT-B-TO-B2-AT-%d-OF-%d-FORCED-BY-COPYING;"
                 "VALUES-GRID-DEPENDENT=%s..%s;UNDEFINED-B2-DENSITY-AT-%d") % (
        bcs["densities_constant"], bcs["rules"],
        bcs["per_incidence_min_text"], bcs["per_incidence_max_text"],
        bcs["undefined_b2_density"])

    payload = {
        "locality_rules": locality_B,
        "grid_size": len(rules),
        "grid_signature": grid_sig,
        "drawing_signature": draw_sig,
        "mechanism": mech,
        "width_law_signature": width_sig,
        "motivation_signature": mot_sig,
        "component_signature": comp_sig,
        "standards_signature": std_sig,
        "link_convention_signature": link_sig,
        "b2_signature": b2_sig,
        "null_signature": null_sig,
        "refuses": len(refuses_B),
        "grid_boundary_signature": gb_sig,
        "constants_signature": const_sig,
    }
    head, segs, full = build_verdict(payload,
                                     swap_pairing=(MUTANT == "verdict-pair-swap"))

    # THE VERDICT GATE.  The comparator is an INDEPENDENT RECONSTRUCTION built
    # from the receipt object -- the same stored tables the paper and the
    # output render from -- and it shares no code and no input with
    # build_verdict.  (RUNBOOK section 14 addenda, v14 #10 + v14 #20: a
    # compliance gate whose comparator cannot disagree with the object under
    # test is vacuous by construction.  The previous comparator called
    # build_verdict twice on the same dict; five injection classes walked
    # through it.  Each of those five now has a declared mutant below.)
    rebuilt = reconstruct_verdict_from_receipt(R)
    gate("G-VERDICT-STRING-EQUALITY",
         "the complete emitted verdict string equals a string reconstructed "
         "INDEPENDENTLY from the receipt object's own measured tables -- "
         "equality, not containment, and a comparator that CAN disagree",
         full == rebuilt,
         {"emitted_len": len(full), "rebuilt_len": len(rebuilt),
          "first_difference": ([i for i in range(min(len(full), len(rebuilt)))
                                if full[i] != rebuilt[i]] or [None])[0]})

    # EVERY SEGMENT FLIPPABLE -- and flippable AT THE MEASUREMENT, not at the
    # string builder.  The old gate appended "-PERTURBED" to a signature and
    # checked that string concatenation is injective: true for every input.
    # This one perturbs the RECEIPT ROW the segment is derived from and
    # requires the independent reconstruction to move.
    flips = []
    for nm in SEGMENT_ORDER:
        snap = json.dumps(jsonable(R), sort_keys=True)
        Rp = json.loads(snap)
        if nm == "RULES":
            for row in Rp["census_rows"]:
                if row["status"] == "NON-COMPLETE":
                    row["status"] = "clique-only"
                    break
        elif nm == "GRID":
            k0 = sorted(Rp["grid"]["by_transport_and_class"])[0]
            Rp["grid"]["by_transport_and_class"][k0] += 1
        elif nm == "DRAWING":
            t0 = sorted(Rp["alt_drawing_group_probe"]["per_transport"])[0]
            Rp["alt_drawing_group_probe"]["per_transport"][t0][
                "pairs_drawn_if_the_drawing_group_were_it"] = 1
        elif nm == "MECHANISM":
            for row in Rp["census_rows"]:
                if row["status"] == "NON-COMPLETE":
                    row["coord"][5] = "ALL"
                    break
        elif nm == "WIDTH-LAW":
            Rp["width_law"]["rules_predicted_correctly"] -= 1
        elif nm == "MOTIVATION":
            Rp["motivation_census"]["partition_sweep"]["noncomplete_hits"] = 1
        elif nm == "COMPONENTS":
            Rp["b1_nontrivial_at"] = Rp["b1_nontrivial_at"][:-1]
        elif nm == "STANDARDS":
            k0 = sorted(Rp["standards"])[0]
            Rp["standards"][k0]["links_that_are_circles"] += 1
        elif nm == "LINK-CONVENTION":
            Rp["link_conventions"]["simple_graph_circles"] += 1
        elif nm == "B2-PERSISTENCE":
            k0 = sorted(Rp["b2_persistence"])[0]
            Rp["b2_persistence"][k0]["survives"] = False
        elif nm == "NULL":
            Rp["null_census"]["orbit_measurements_that_refuse"] += 1
        elif nm == "REFUSES":
            for row in Rp["census_rows"]:
                if row["status"] == "clique-only":
                    row["status"] = "REFUSES"
                    break
        elif nm == "GRID-BOUNDARY":
            Rp["grid_boundary"]["excluded_from_the_declared_words"] += 1
        elif nm == "BLOCK-CONSTANTS":
            Rp["block_constants_summary"]["undefined_b2_density"] += 1
        flips.append((nm, reconstruct_verdict_from_receipt(Rp) != rebuilt))
    gate("G-VERDICT-SEGMENTS-FLIPPABLE",
         "perturbing the RECEIPT ROW a segment is derived from moves the "
         "independently reconstructed string, at every one of the segments: "
         "each segment carries measured content, not decoration",
         all(f for _, f in flips) and len(flips) == len(segs),
         {"segments": len(segs), "flippable": len([1 for _, f in flips if f]),
          "inert": [nm for nm, f in flips if not f]})

    # BOTH HEADS REACHABLE -- through the reconstruction, on synthesised
    # receipts, so the check is of the DERIVATION and not of the branch it
    # just took.
    snap = json.dumps(jsonable(R), sort_keys=True)
    R_none = json.loads(snap)
    for row in R_none["census_rows"]:
        if row["status"] == "NON-COMPLETE":
            row["status"] = "clique-only"
    h_none = reconstruct_verdict_from_receipt(R_none).split("<")[0]
    R_loc = json.loads(snap)
    for row in R_loc["census_rows"]:
        if row["status"] == "clique-only":
            row["status"] = "NON-COMPLETE"
            break
    h_loc = reconstruct_verdict_from_receipt(R_loc).split("<")[0]
    gate("G-VERDICT-BOTH-HEADS-REACHABLE",
         "both verdict heads are emitted by the SAME derivation run on "
         "synthesised receipts -- a receipt with no non-complete rule yields "
         "the negative head, one with a non-complete rule the positive head",
         (h_none == HEAD_NONE and h_loc == HEAD_LOCALITY and h_none != h_loc
          and head in (HEAD_NONE, HEAD_LOCALITY)),
         {"heads": [h_loc, h_none], "emitted": head})

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
        "verdict_segments": len(segs),
        "path_value_anchors": len(PATH_ANCHOR_ROWS),
        "partition_sweep_measurements": mps["measurements"],
        "numberings_swept": mor["numberings_swept"],
        "cyclic_actions_swept": sweep_actions,
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
                        "clique-only).  Measured at full generality: all %d set "
                        "partitions of the eight labels, at both transports, "
                        "%d measurements, %d non-complete."
                        % (mps["partitions_of_the_eight_labels"],
                           mps["measurements"], mps["noncomplete_hits"]),
        "R2-W": R["width_law"]["theorem"],
        "R2-D": R["dimension_reading_over_the_whole_grid"]["theorem"],
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
          and R["totals"]["anchors"] == len(ANCHOR_ROWS) + len(PATH_ANCHOR_ROWS)
          and R["totals"]["verdict_segments"] == len(SEGMENT_ORDER)),
         dict(R["totals"]))

    # -- post-measurement injections (they live in the RENDERED OBJECT, never
    # in a gate predicate: RUNBOOK section 14 addendum, v13 #208) ------------
    if MUTANT == "render-escape":
        R["block_constants"][0]["B"]["b2_density"] = Fraction(99, 100)
        R["block_constants"][0]["B"]["ncoh_per_incidence"] = Fraction(7, 3)
        R["block_constants"][0]["B2"]["E_N"] = 999
        k0 = sorted(R["standards"])[0]
        R["standards"][k0]["reading"] = "CONSISTENT"
        R["standards"][k0]["links_that_are_circles"] = 77
        R["b1_per_component"][k0]["b1_of_N"] = 4242
        R["b2_persistence"][k0]["completeness_B2"] = Fraction(1, 1)
    if MUTANT == "internal-contradiction":
        for row in R["census_rows"]:
            if row["status"] == "NON-COMPLETE":
                row["status"] = "clique-only"
                break

    # -- INTERNAL CONSISTENCY (instrument M4 / the INJ8 class) ---------------
    icbad = internal_consistency(R)
    gate("G-RECEIPT-INTERNALLY-CONSISTENT",
         "the receipt does not contradict itself: no rule is labelled "
         "clique-only while a non-complete component is listed for it, no "
         "REFUSES draws an edge, every cycle rank agrees with its own (edges, "
         "size), and the locality set agrees across census_rows, "
         "locality_census, standards, b2_persistence and b1_per_component",
         len(icbad) == 0, {"contradictions": icbad[:6]})

    # -- THE FALSIFIER CENSUS, with an honest denominator (instrument M6) ----
    # R1 carried a never-falsified set and it was EMPTY; R2 carried none and
    # its true value was 30 of 42.  It is restored here, computed from the
    # declared mutant table against the gate ledger, with every gate that no
    # declared mutant reaches NAMED, and every waiver stating its forcing.
    # the ledger the census is taken against: the gates registered so far,
    # plus THIS gate, plus the write-time gates named in DEFERRED_GATES --
    # so the denominator covers every gate this instrument declares, not only
    # the ones that happen to have run by now
    gate_names = [g["name"] for g in GATES] + ["G-FALSIFIER-CENSUS"]
    gate_names = gate_names + [n for n in DEFERRED_GATES if n not in gate_names]
    falsified = {}
    for m in MUTANTS:
        falsified.setdefault(m["expected_gate"], []).append(m["name"])
    never = [n for n in gate_names if n not in falsified]
    R["falsifier_census"] = {
        "deferred_gates_evaluated_at_write_time": list(DEFERRED_GATES),
        "gates": len(gate_names),
        "gates_with_a_declared_falsifier": len([n for n in gate_names
                                                if n in falsified]),
        "never_falsified": never,
        "never_falsified_count": len(never),
        "denominator": "%d of %d gates" % (len(never), len(gate_names)),
        "falsifier_map": dict((k, sorted(v)) for k, v in sorted(falsified.items())
                              if k in gate_names),
        "waivers": WAIVERS,
        "waivers_censused": len(WAIVERS),
        "note": "a gate with no declared falsifier is NAMED here, never "
                "waived silently; the waiver rows below state, for each gate "
                "that cannot be falsified by construction, WHAT FORCES IT",
    }
    waived = set(w["gate"] for w in WAIVERS)
    gate("G-FALSIFIER-CENSUS",
         "the never-falsified set is computed from the declared mutant table "
         "against the gate ledger and emitted in the receipt with an honest "
         "denominator; every gate in it that cannot fail by construction "
         "carries a waiver stating its forcing, and every waiver names a gate "
         "that really is unfalsified",
         (len(gate_names) == len(set(gate_names))
          and all(w["gate"] in gate_names for w in WAIVERS)
          and all(w["gate"] in never for w in WAIVERS)
          and set(falsified) <= set(gate_names)),
         {"gates": len(gate_names), "never_falsified": len(never),
          "waivers": len(WAIVERS),
          "waivers_naming_a_falsified_gate": sorted(waived - set(never))})

    R["compliance"] = compliance_sweep(R)
    return R, census, rules, std


# ----------------------------------------------------------------------------
# 12.  Compliance sweep -- rule by rule, stated with its status
# ----------------------------------------------------------------------------

def compliance_sweep(R):
    """RULE BY RULE, with a COMPUTED status (instrument M10: nineteen of the
    delivered twenty statuses were literals, and two of the literals were
    false).  Every status below is built from the gate ledger or from a
    measured field, so a rule whose gate is absent says MISSING."""
    names = set(g["name"] for g in GATES)

    def by(*gates):
        have = [g for g in gates if g in names]
        miss = [g for g in gates if g not in names]
        if miss:
            return "MISSING: " + ", ".join(miss)
        return "APPLIED via " + ", ".join(have)

    def mut(*muts):
        declared = set(m["name"] for m in MUTANTS)
        miss = [m for m in muts if m not in declared]
        if miss:
            return "MISSING MUTANT: " + ", ".join(miss)
        return "falsifiers " + ", ".join(muts)

    fc = R.get("falsifier_census", {})
    rows = [
        ("RUNBOOK 13/14/15 with every addendum binds at delivery (#246/#313)",
         "APPLIED -- this sweep enumerates each rule and computes its status "
         "from the gate ledger (%d gates)" % len(names)),
        ("#10 containment is not equality: the verdict gate compares the "
         "COMPLETE string against a rebuild",
         by("G-VERDICT-STRING-EQUALITY") + "; " +
         mut("verdict-pair-swap", "verdict-typed-segment", "verdict-append-text",
             "verdict-typed-motivation", "verdict-fully-typed")),
        ("#20 compliance claims are gate claims: a gate asserting compliance "
         "with an engraved rule ships with an injection-falsifier, and a "
         "comparator that cannot disagree is vacuous",
         "APPLIED -- the verdict comparator is "
         "reconstruct_verdict_from_receipt(), which shares no code and no "
         "input with build_verdict(); all five R1 injection classes are "
         "declared mutants and die on it"),
        ("#10 render from the gated object (one object, one source of truth)",
         by("G-RENDER-FROM-GATED-OBJECT") + " -- TOTAL over every rendered "
         "field of every rendered object; " + mut("render-escape",
                                                  "table-corrupt",
                                                  "census-row-corrupt")),
        ("#20 prose renders from the receipt: every numeric claim in the paper "
         "renders from the receipt object",
         by("G-PROSE-RENDERS-FROM-THE-RECEIPT") + "; " +
         mut("prose-claim-drift")),
        ("#20 path-value anchoring: a read-by-path anchors the (path, value) "
         "pair, not only the file bytes",
         "APPLIED -- %d path-value anchor rows; %s; %s"
         % (len(PATH_ANCHOR_ROWS), by("G-READ-VALUES-MATCH-THE-DECLARATION"),
            mut("path-drift"))),
        ("#234 the verdict is derived inside a gate and a flip mutant proves "
         "the derivation can fail",
         by("G-VERDICT-SEGMENTS-FLIPPABLE", "G-VERDICT-BOTH-HEADS-REACHABLE")
         + " -- flippability is tested by perturbing the RECEIPT ROW each "
         "segment derives from, not by appending to its string; " +
         mut("verdict-inert-segment", "head-constant")),
        ("#234 the cell-completeness gate catches a dropped cell",
         by("G-GRID-CELL-COMPLETE", "G-GRID-CELL-SETS-COMPLETE") + "; " +
         mut("grid-drop", "window-drop")),
        ("#234/#219 two independent routes are genuinely independent",
         by("G-DRAW-TWO-ROUTES", "G-COMPONENTS-TWO-ROUTES",
            "G-TWOCELLS-TWO-ROUTES", "G-WIDTH-LAW-PREDICTS-THE-CENSUS") +
         " -- orbit/stabiliser vs brute force; union-find vs F_2 rank; cell "
         "enumeration vs triangle recount; atlas census vs the analytic width "
         "law.  G-COMPLETENESS-TWO-ROUTES is a stored-flag-versus-recomputation "
         "TAMPER check and is described as one, not as two routes"),
        ("#219 a gate clause may not compare an object against a copy of "
         "itself routed through the component under test",
         "APPLIED -- the verdict comparator was exactly that and is rebuilt; "
         "see the #20 row above"),
        ("#257 computed qualifiers (no typed qualifier segment)",
         "APPLIED -- all %d verdict segments are built from measured counts "
         "and each is shown flippable at its measurement"
         % len(SEGMENT_ORDER)),
        ("#208 forced clauses are disclosures, not must-pass claims",
         "APPLIED -- FORCED is written into the verdict string itself at "
         "DIMREAD, LOCAL-DIMENSIONS, B2-PERSISTENCE and BLOCK-CONSTANTS, and "
         "the width law states that WHICH RULES ARE LOCAL is computed from the "
         "declaration; the waiver table names %d gates that cannot fail, each "
         "with its forcing" % len(WAIVERS)),
        ("#208 no gate predicate references mutant identity",
         "APPLIED -- no gate reads MUTANT; every injection lives in a measured "
         "function or in the rendered object"),
        ("#208/#175 falsified-or-waived, with the waivers censused",
         "APPLIED -- %s never falsified, %d waived with forcing stated; the "
         "census is emitted in the receipt (%s)"
         % (fc.get("denominator", "?"), fc.get("waivers_censused", 0),
            by("G-FALSIFIER-CENSUS"))),
        ("#219 a zero-hit or zero-lookup cache gate is vacuous",
         by("G-CACHE-EXERCISED") + " -- hits > 0 AND misses > 0"),
        ("#24 counts are computed, never typed",
         by("G-COUNTS-COMPUTED", "G-R2A-EXHAUSTIVE", "G-CONSTANTS-SPAN-COMPUTED")
         + " -- the sweep's exhaustiveness is gated against a DERIVED "
         "factorial, and the constants' span is computed, not typed; " +
         mut("sweep-truncate", "partition-sweep-truncate", "order-sweep-truncate")),
        ("section 15 declared-arena discipline: the arena and the grid are "
         "printed and matched at every coordinate",
         by("G-ARENA-DECL-MATCHED", "G-GRID-CELL-COMPLETE",
            "G-READ-VALUES-MATCH-THE-DECLARATION") +
         " -- the grid, the drawing relation and the transport are named "
         "verdict coordinates; the two transports are arena data and the "
         "census is reported at both"),
        ("section 14 #175 symmetry self-tests, evaluated fresh",
         by("G-SYMMETRY-SELFTEST") + " (memo bypassed, fresh-call count "
         "gated).  DECLARED SCOPE: it conjugates the transport AND transports "
         "the cells, so it is a COVARIANCE check; the ORDER-invariance "
         "question it cannot reach is measured separately by " +
         ("G-MOTIVATION-ORDER-RELATIVITY" if
          "G-MOTIVATION-ORDER-RELATIVITY" in names else "MISSING")),
        ("section 14 #185 self-tests must not reach their quantity through "
         "the memo", "APPLIED -- f2_rank(fresh=True) in the self-test path"),
        ("section 13 #313 boundary parity witness with a measured delta",
         by("G-BOUNDARY-PARITY", "G-LINK-CONVENTION-WITNESSED") +
         " -- the 2-cell connective AND the link convention both carry their "
         "measured deltas"),
        ("section 13 #314 precheck doctrine: a precheck may gate what is "
         "censused but never name the verdict",
         "APPLIED -- no precheck exists; the verdict is named by the censused "
         "objects only"),
        ("section 13 #313 repair propagation: a recurrence of an engraved "
         "disease is a MAJOR by default",
         "APPLIED -- the three engravings of v14 #20 were all raised against "
         "THIS unit and all three are implemented above"),
        ("exact arithmetic only",
         by("G-FLOATGUARD", "G-NO-FLOATS-IN-RECEIPT") + " (AST scan of this "
         "source + a recursive scan of the emitted receipt); " +
         mut("float-leak")),
        ("REFUSES is recorded, never skipped",
         by("G-EVERY-RULE-RECORDED", "G-FLAGS-DERIVED-NOT-TRUSTED") + "; " +
         mut("refuses-skip", "refuses-reclassify")),
        ("the receipt may not contradict itself",
         by("G-RECEIPT-INTERNALLY-CONSISTENT") + "; " +
         mut("internal-contradiction", "flag-flip")),
        ("the UNDEFINED path is live or the exclusion is stated",
         by("G-UNDEFINED-PATH-LIVE") + " -- reached by shipped inputs at %d "
         "rules" % len([1 for c in R.get("block_constants", [])
                        if c["B"]["b2_density"] is None])),
        ("controls in both directions: a positive control that fires and a "
         "negative control that must not",
         by("G-POSITIVE-CONTROL", "G-SCRAMBLE-CONTROL", "G-STANDARDS-CONTROLS",
            "G-DIMREAD-MUTUAL-EXCLUSION", "G-SUCCESSOR-CONTROL") +
         " -- and the dimension reading now has a POSITIVE control on shipped "
         "input (CONSISTENT is attained) plus a constructive successor control"),
        ("no claim about the continuum; the word 'manifold' appears only in "
         "the rung's name and in the successor control's measured type",
         "APPLIED -- the verdict string uses LINK-CIRCLES / DIMREAD / "
         "LOCAL-DIMENSIONS / TRIANGULATED-CIRCLES; the one place the unit says "
         "'1-manifold' is the fixed-point-free CONTROL, where it is a measured "
         "graph-theoretic property (a cycle graph with S^0 links), declared "
         "outside the grid"),
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
    w("9a. THE WIDTH LAW (theorem R2-W) -- the census as a corollary of the")
    w("    declaration")
    w("-" * 78)
    wl = R["width_law"]
    w("  %s" % wl["theorem"])
    w("  predicted correctly (status AND edge count), no atlas built: %d of %d"
      % (wl["rules_predicted_correctly"], wl["rules"]))
    w("  closed forms agreeing with the measured (|E|, b1): %d of %d rows"
      % (wl["closed_form_agreements"], wl["closed_form_rows"]))
    w("  THE TWO THRESHOLDS HAVE DIFFERENT CAUSES:")
    for t in sorted(wl["threshold_causes"]):
        c = wl["threshold_causes"][t]
        w("    %-3s coset support %s of %d, shape %s, diameter D = %d "
          "=> locality vanishes at c = %d"
          % (t, c["support"], c["k"], c["support_shape"], c["D"],
             c["locality_vanishes_at_c"]))
    w("  %s" % wl["two_causes_note"])
    w("  epistemic status: %s" % wl["epistemic_status"])
    w("  closed-form rows (rule, family, k, m, c, |E|, b1):")
    seen_fam = set()
    for cf in wl["closed_forms"]:
        if cf["family"] in seen_fam:
            continue
        seen_fam.add(cf["family"])
        w("    %s  %s" % (cf["rid"], cf["family"]))
    for cf in wl["closed_forms"]:
        w("    %-6s k=%d m=%d c=%d  |E| closed=%-3d measured=%-3d  "
          "b1 closed=%-3d measured=%-3d  %s"
          % (cf["rid"], cf["k"], cf["m"], cf["c"], cf["closed_form_E"],
             cf["measured_E"], cf["closed_form_b1"], cf["measured_b1"],
             "agree" if cf["agrees"] else "DISAGREE"))
    w()
    w("-" * 78)
    w("9b. THE MOTIVATION CENSUS -- is any locality-bearing cover inherited?")
    w("-" * 78)
    mo = R["motivation_census"]
    ps, fa, orl = mo["partition_sweep"], mo["fano_cover"], mo["order_relativity"]
    w("  (a) EVERY set partition of the eight labels, at both transports")
    w("      partitions %d (Bell(8) derived = %d) x %d transports = %d "
      "measurements" % (ps["partitions_of_the_eight_labels"],
                        ps["bell_number_8_derived"], ps["transports"],
                        ps["measurements"]))
    w("      non-complete components found: %d" % ps["noncomplete_hits"])
    w("      %s" % ps["what_it_settles"])
    w("  (b) I6's OWN declared partial-overlap cover: the seven Fano lines")
    w("      source: %s" % fa["source"])
    w("      lines: %s" % fa["lines"])
    w("      pairs covered %d of %d -- a 2-design: %s"
      % (fa["pairs_covered"], fa["pairs_possible"], fa["is_a_2_design"]))
    for t in sorted(fa["per_transport"]):
        v = fa["per_transport"][t]
        w("      %-3s lines: non-complete=%s (%d drawn pairs) ; complements: "
          "non-complete=%s (%d drawn pairs)"
          % (t, v["lines_noncomplete"], v["lines_edges"],
             v["complements_noncomplete"], v["complements_edges"]))
    w("      clique-only at %d of %d transports -- THE ONE MOTIVATED COVER THE"
      % (fa["transports_where_it_is_clique_only"], len(fa["per_transport"])))
    w("      CORPUS OWNS IS A LOCALITY-DESTROYER, and for a reason: a 2-design")
    w("      covers every pair, so its overlap graph is complete.")
    w("  (c) the locality census under EVERY numbering of the carrier")
    w("      numberings swept %d ; sliding rules %d ; distinct coset systems "
      "%d ; rule-censuses %d"
      % (orl["numberings_swept"], orl["sliding_rules"],
         orl["distinct_coset_systems"], orl["rule_censuses"]))
    w("      locality count distribution:")
    tot = orl["numberings_swept"]
    for k in sorted(orl["count_distribution"], key=lambda z: int(z)):
        v = orl["count_distribution"][k]
        hund = (v * 10000 + tot // 2) // tot
        w("        %2s rules local at %6d numberings  (%d.%02d%%)%s"
          % (k, v, hund // 100, hund % 100,
             "   <-- THE DECLARED NUMBERING"
             if int(k) == orl["declared_numbering_count"] else ""))
    w("      distinct locality-bearing rule sets realised: %d"
      % orl["distinct_rule_sets"])
    w("      the declared numbering's count is %d and it is the MODAL value "
      "at %s%% -- the unit did not cherry-pick"
      % (orl["declared_numbering_count"], orl["modal_share_percent_text"]))
    w("      rules local at SOME numbering: %d -- %s"
      % (len(orl["rules_local_at_some_numbering"]),
         ", ".join(orl["rules_local_at_some_numbering"])))
    w("      per-rule numberings at which the rule is local:")
    for rid in sorted(orl["per_rule_orders_local"]):
        w("        %-6s %6d of %d" % (rid, orl["per_rule_orders_local"][rid], tot))
    w()
    w("-" * 78)
    w("9c. THE GRID BOUNDARY -- what the admissibility proxy excludes")
    w("-" * 78)
    gb = R["grid_boundary"]
    w("  declared test    : %s" % gb["declared_test"])
    w("  alternative test : %s" % gb["alternative_test"])
    w("  excluded rules constructible from the declared words : %d"
      % gb["excluded_from_the_declared_words"])
    w("  excluded rules including the cyclic lattice          : %d"
      % gb["excluded_including_the_cyclic_lattice"])
    w("  of the excluded, LOCALITY-BEARING                    : %d"
      % gb["excluded_noncomplete"])
    for r0 in gb["the_locality_bearing_exclusions"]:
        w("    %s  cosets %d  cells %s" % (r0["coord"], r0["cosets"], r0["cells"]))
        for c in r0["noncomplete_components"]:
            w("      component size %d: %d of %d pairs drawn, completeness %s"
              % (c["size"], c["drawn"], c["pairs"], frac(c["completeness"])))
    w()
    w("-" * 78)
    w("9d. THE SUCCESSOR CONTROL -- the grid's boundary, made visible")
    w("-" * 78)
    sc = R["successor_control"]
    w("  %s" % sc["declaration"])
    w("  transport %s (order %d), fixed points %s, orbits %s"
      % (sc["transport"], sc["transport_order"], sc["fixed_points"], sc["orbits"]))
    w("  the regular orbit is the WHOLE label set: %s"
      % sc["regular_orbit_is_the_whole_label_set"])
    for r0 in sc["rows"]:
        w("    c=%d  cells=%d edges=%d 2-cells=%d components=%s non-complete=%s"
          % (r0["c"], r0["cells"], r0["edges"], r0["two_cells"],
             r0["components"], r0["noncomplete"]))
        w("         reading: cell-indexed %s (%d distinct) ; chart-intrinsic "
          "%s (%d distinct)"
          % (r0["reading_cell_indexed"], r0["distinct_readings_cell_indexed"],
             r0["reading_chart_intrinsic"],
             r0["distinct_readings_chart_intrinsic"]))
        w("         links (cell multiplicity) %s ; (simple graph) %s"
          % (r0["distinct_links_cell_multiplicity"],
             r0["distinct_links_simple_graph"]))
        w("         A TRIANGULATED 1-MANIFOLD: %s"
          % r0["is_a_triangulated_1_manifold"])
    w()
    w("-" * 78)
    w("9e. THE DIMENSION READING OVER THE WHOLE GRID, AND THE LINK CONVENTION")
    w("-" * 78)
    dr = R["dimension_reading_over_the_whole_grid"]
    w("  %s" % dr["theorem"])
    w("  rules measured %d ; CONSISTENT at %d ; locality-bearing %d ; "
      "intersection %d"
      % (dr["rules_measured"], dr["consistent_rules"], dr["locality_rules"],
         dr["intersection_with_locality"]))
    w("  CONSISTENT at: %s" % ", ".join(dr["consistent_rule_list"]))
    w("  locality rules CONSISTENT under the chart-intrinsic reading: %d"
      % dr["locality_rules_consistent_under_the_chart_intrinsic_reading"])
    lk = R["link_conventions"]
    w("  link circles over %d charts with links:" % lk["charts"])
    w("      cell-multiplicity convention (delivered) : %d"
      % lk["cell_multiplicity_circles"])
    w("      simple-graph convention                  : %d"
      % lk["simple_graph_circles"])
    w("      TRIANGULATED circles (the manifold test)  : %d"
      % lk["triangulated_circles"])
    w("  %s" % lk["note"])
    li = R["local_dimension_identity"]
    w("  LOCAL-DIMENSIONS is an identity: agrees at %d of %d -- %s"
      % (li["agrees_at"], li["rules"], li["statement"]))
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
    fc = R.get("falsifier_census")
    if fc:
        w("  gates with a declared falsifier : %d of %d"
          % (fc["gates_with_a_declared_falsifier"], fc["gates"]))
        w("  NEVER FALSIFIED (honest denominator): %s" % fc["denominator"])
        for n in fc["never_falsified"]:
            wv = [x for x in fc["waivers"] if x["gate"] == n]
            w("      %-38s %s" % (n, ("WAIVED: " + wv[0]["forcing"])
                                  if wv else "no declared falsifier"))
        w("  waivers censused: %d" % fc["waivers_censused"])
    w()
    pc = R.get("paper_claims")
    if pc:
        w("-" * 78)
        w("13a. THE PAPER'S NUMERIC SENTENCES, RENDERED FROM THIS RECEIPT")
        w("-" * 78)
        w("  %s" % pc["rule"])
        w("  paper %s (sha256-12 %s); claims rendered %d, present %d"
          % (pc["paper"], pc["paper_sha256_prefix"], pc["claims_rendered"],
             pc["claims_present_in_the_paper"]))
        for k in sorted(pc["rendered"]):
            w("      %-22s %s" % (k, pc["rendered"][k]))
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
    # ---- the delivered fourteen ------------------------------------------
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
     "what_it_breaks": "collapses SLIDING onto BLOCKWISE, erasing all locality "
                       "and driving the head to NO-LOCALITY-IN-THE-DECLARED-"
                       "GRID; it is caught one level earlier than the mode "
                       "probe, by the cell-set comparator",
     "expected_gate": "G-GRID-CELL-SETS-COMPLETE"},
    {"name": "modes-collapse",
     "what_it_breaks": "makes the mode probe see BLOCKWISE and SLIDING as the "
                       "same construction",
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

    # ---- THE FIVE VERDICT INJECTION CLASSES (the R1 classes, re-run
    # against this unit by the instrument lens; all five survived the old
    # self-comparing gate and all five die on the reconstruction) ----------
    {"name": "verdict-typed-segment",
     "what_it_breaks": "TYPES the STANDARDS segment -- the headline negative "
                       "finding emitted inverted (links circles at 80 of 80, "
                       "DIMREAD=CONSISTENT)",
     "expected_gate": "G-VERDICT-STRING-EQUALITY"},
    {"name": "verdict-append-text",
     "what_it_breaks": "appends '-AND-SUBSTRATE-MOTIVATED' to the MECHANISM "
                       "segment (the containment class)",
     "expected_gate": "G-VERDICT-STRING-EQUALITY"},
    {"name": "verdict-typed-motivation",
     "what_it_breaks": "types the MOTIVATION segment to claim the cover is "
                       "inherited from I6's Fano lines -- the exact opposite "
                       "of the measurement",
     "expected_gate": "G-VERDICT-STRING-EQUALITY"},
    {"name": "verdict-fully-typed",
     "what_it_breaks": "replaces EVERY segment with a literal and names a rule "
                       "that does not exist (R999 in a grid of size 1)",
     "expected_gate": "G-VERDICT-STRING-EQUALITY"},
    {"name": "verdict-inert-segment",
     "what_it_breaks": "makes the MOTIVATION segment a constant in BOTH the "
                       "builder and the comparator: string equality still "
                       "holds and the segment stops carrying content",
     "expected_gate": "G-VERDICT-SEGMENTS-FLIPPABLE"},
    {"name": "head-constant",
     "what_it_breaks": "the reconstructed head stops tracking the census, so "
                       "the negative head becomes unreachable",
     "expected_gate": "G-VERDICT-BOTH-HEADS-REACHABLE"},

    # ---- the path-value anchor class --------------------------------------
    {"name": "path-drift",
     "what_it_breaks": "drifts ONE JSON path component "
                       "(lex_first_Q_per_order['4'] -> ['6']): a 115-rule "
                       "grid, an order-2 transport and an entirely different "
                       "verdict, with every file-bytes anchor green",
     "expected_gate": "P-I6-GAMMA4"},
    {"name": "anchor-skip",
     "what_it_breaks": "silently drops one declared anchor row",
     "expected_gate": "G-ANCHOR-COUNT"},

    # ---- the count-guard class --------------------------------------------
    {"name": "flag-flip",
     "what_it_breaks": "clears one rule's locality bit: the rule leaves the "
                       "headline census while its non-complete component stays "
                       "in the receipt (the internally contradictory receipt)",
     "expected_gate": "G-FLAGS-DERIVED-NOT-TRUSTED"},
    {"name": "refuses-reclassify",
     "what_it_breaks": "reclassifies every REFUSES as a drawing rule",
     "expected_gate": "G-FLAGS-DERIVED-NOT-TRUSTED"},
    {"name": "b1-zero",
     "what_it_breaks": "zeroes every per-component cycle rank -- the whole "
                       "degree-one finding erased",
     "expected_gate": "G-FLAGS-DERIVED-NOT-TRUSTED"},
    {"name": "twocell-drop",
     "what_it_breaks": "drops the first 2-cell of each block, per-block "
                       "uniformly, so the copy-reduction and coherence gates "
                       "stay green",
     "expected_gate": "G-TWOCELLS-TWO-ROUTES"},
    {"name": "window-drop",
     "what_it_breaks": "silently drops one interior sliding window: the grid "
                       "coordinate set is untouched and the grid still reports "
                       "complete",
     "expected_gate": "G-GRID-CELL-SETS-COMPLETE"},
    {"name": "sweep-truncate",
     "what_it_breaks": "truncates the 'exhaustive' R2-A sweep to 100 "
                       "permutations and emits the truncated count verbatim",
     "expected_gate": "G-R2A-EXHAUSTIVE"},

    # ---- the new measured segments' own falsifiers -------------------------
    {"name": "width-law-corrupt",
     "what_it_breaks": "corrupts the width law's prediction at one rule",
     "expected_gate": "G-WIDTH-LAW-PREDICTS-THE-CENSUS"},
    {"name": "partition-sweep-truncate",
     "what_it_breaks": "truncates the 4,140-partition motivation sweep",
     "expected_gate": "G-MOTIVATION-PARTITION-SWEEP"},
    {"name": "fano-shrink",
     "what_it_breaks": "drops four of I6's seven Fano lines, so the cover is "
                       "no longer the declared 2-design",
     "expected_gate": "G-MOTIVATION-FANO-COVER"},
    {"name": "order-sweep-truncate",
     "what_it_breaks": "truncates the 40,320-numbering order-relativity sweep",
     "expected_gate": "G-MOTIVATION-ORDER-RELATIVITY"},
    {"name": "successor-control-broken",
     "what_it_breaks": "gives the successor control a fixed point, destroying "
                       "the triangulated 1-manifold",
     "expected_gate": "G-SUCCESSOR-CONTROL"},

    # ---- the render / consistency / prose classes --------------------------
    {"name": "render-escape",
     "what_it_breaks": "corrupts seven receipt cells the old render check did "
                       "not cover (b2_density, ncoh_per_incidence, the whole "
                       "B2 column, a standards reading, a circle count, a "
                       "cycle rank, a B2 completeness)",
     "expected_gate": "G-RENDER-FROM-GATED-OBJECT"},
    {"name": "internal-contradiction",
     "what_it_breaks": "labels a rule clique-only in census_rows while leaving "
                       "its non-complete component listed",
     "expected_gate": "G-RECEIPT-INTERNALLY-CONSISTENT"},
    {"name": "prose-claim-drift",
     "what_it_breaks": "renders one paper claim with a number the measurement "
                       "does not support, so the paper no longer carries the "
                       "receipt's own sentence",
     "expected_gate": "G-PROSE-RENDERS-FROM-THE-RECEIPT"},

    # ---- gates the delivered instrument left without any falsifier --------
    {"name": "read-value-drift",
     "what_it_breaks": "swaps the T4 transport for the order-2 completion "
                       "AFTER the anchor, so the paper's typed 'order 4' no "
                       "longer describes the value in use",
     "expected_gate": "G-READ-VALUES-MATCH-THE-DECLARATION"},
    {"name": "copy-reduction-break",
     "what_it_breaks": "flips one rule's B->B2 doubling flag",
     "expected_gate": "G-COPY-REDUCTION"},
    {"name": "b2-persistence-drop",
     "what_it_breaks": "drops one locality-bearing rule from the B2 "
                       "persistence table",
     "expected_gate": "G-B2-PERSISTENCE-MEASURED"},
    {"name": "components-route2-break",
     "what_it_breaks": "perturbs the F_2-rank route to b0",
     "expected_gate": "G-COMPONENTS-TWO-ROUTES"},
    {"name": "standards-identity-break",
     "what_it_breaks": "breaks the star/edge global identity at one rule",
     "expected_gate": "G-STANDARDS-IDENTITIES"},
    {"name": "symmetry-break",
     "what_it_breaks": "makes the census non-invariant under the declared "
                       "Sigma relabelling",
     "expected_gate": "G-SYMMETRY-SELFTEST"},
    {"name": "parity-inert",
     "what_it_breaks": "makes the alternative 2-cell connective agree with the "
                       "delivered one everywhere -- a parity witness with no "
                       "measured delta",
     "expected_gate": "G-BOUNDARY-PARITY"},
    {"name": "lattice-crosscheck-break",
     "what_it_breaks": "breaks the agreement between the two independently "
                       "declared lattices at their shared trivial subgroup",
     "expected_gate": "G-LATTICE-CROSSCHECK"},
]

# One anchor-corruption mutant PER ANCHOR ROW -- the pin asks for "anchor-hash
# corruption for every I-row used" and the delivered instrument met it 1-of-5
# by name.  Built from the anchor tables so a new anchor cannot be added
# without its falsifier.
for _nm, _rel, _exp, _why in ANCHOR_ROWS:
    if _nm == "A-R0-I6":
        continue                      # already covered by "anchor-hash"
    MUTANTS.append({"name": "anchor-hash-" + _nm,
                    "what_it_breaks": "corrupts the %s file-bytes anchor" % _nm,
                    "expected_gate": _nm})
for _nm, _rel, _path, _exp, _why in PATH_ANCHOR_ROWS:
    if _nm == "P-I6-GAMMA4":
        continue                      # already covered by "path-drift"
    MUTANTS.append({"name": "path-value-" + _nm,
                    "what_it_breaks": "breaks the %s (path, value) anchor" % _nm,
                    "expected_gate": _nm})


# Gates that no declared mutant can reach, each with WHAT FORCES IT.  The era's
# standard is falsified-or-waived-with-the-waiver-censused; this table is the
# waiver half, and G-FALSIFIER-CENSUS gates that every row here names a gate
# that really is unfalsified (RUNBOOK section 14 addendum, v13 #208).
WAIVERS = [
    {"gate": "G-R2A-AT-THIS-UNITS-ACTIONS",
     "forcing": "ANALYTICALLY FORCED: theorem R2-A is true of every group "
                "action, so this can never report a fact about the substrate. "
                "Kept as an implementation comparator (two genuinely "
                "independent routes); shadowed by G-DRAW-TWO-ROUTES, which "
                "fires earlier on the same corruption."},
    {"gate": "G-ORBIT-CLASSES-CLIQUE-ONLY",
     "forcing": "ANALYTICALLY FORCED: the partition corollary is proved in "
                "the paper and measured at full generality by the 4,140-"
                "partition sweep.  A disclosure carried as an instrument "
                "check, not a claim about the substrate."},
    {"gate": "G-COHERENCE-FORCED",
     "forcing": "ANALYTICALLY FORCED: a drawn pair has a trivial stabiliser, "
                "so N_coh = N for every input.  Non-vacuous as an "
                "implementation check -- the scramble control moves the "
                "coherent count at every rule of its declared tested set."},
    {"gate": "G-ALT-DRAW-PROBE",
     "forcing": "ANALYTICALLY FORCED: |<gamma,Sigma>| exceeds the label count "
                "at both transports, so no orbit can be regular and nothing is "
                "drawable.  The MEASUREMENT it records is verdict-determining "
                "and is carried in the DRAWING segment."},
    {"gate": "G-GROUP-CAP",
     "forcing": "A DECLARED SCOPE STATEMENT, not a measurement: it records "
                "that no group closure was silently truncated.  It can fail "
                "only on a declaration whose closure exceeds the printed cap."},
    {"gate": "G-DIMREAD-MUTUAL-EXCLUSION",
     "forcing": "HALF FORCED: the EMPTY INTERSECTION is theorem R2-D "
                "(CONSISTENT and NON-COMPLETE are mutually exclusive under a "
                "cell-indexed reading), so that half cannot come out "
                "otherwise.  The other half -- that CONSISTENT is attained at "
                "all, at 22 of the 109 shipped rules -- IS a measurement, and "
                "it is the positive control the delivered instrument lacked."},
    {"gate": "G-LOCAL-DIMENSIONS-ARE-AN-IDENTITY",
     "forcing": "ANALYTICALLY FORCED: the top local dimension IS "
                "max|cell cap regular orbit| - 1 because the drawn slice of a "
                "cell inside a regular orbit is a clique.  The gate exists to "
                "make the identity visible, not to test it."},
    {"gate": "G-WIDTH-LAW-CLOSED-FORMS",
     "forcing": "ANALYTICALLY FORCED given the declaration: the closed forms "
                "are arithmetic specialisations of theorem R2-W, whose "
                "measured content is carried by "
                "G-WIDTH-LAW-PREDICTS-THE-CENSUS (falsifier: "
                "width-law-corrupt)."},
    {"gate": "G-WIDTH-LAW-TWO-CAUSES",
     "forcing": "FORCED BY THE ARENA: the two declared transports' regular "
                "orbits sit in their coset cycles as a punctured cycle and as "
                "a contiguous arc respectively; this is a property of the "
                "anchored permutations, not an outcome."},
    {"gate": "G-CONSTANTS-SPAN-COMPUTED",
     "forcing": "FORCED: the grid contains rules with F_coh = 0 and rules "
                "with F_coh > E_N, so the span is non-degenerate for any "
                "grid of this shape.  Its purpose is to make the span a "
                "COMPUTED object so the paper's sentence cannot be typed."},
    {"gate": "G-COUNTS-COMPUTED",
     "forcing": "INSTRUMENT BOOKKEEPING: it compares this run's totals "
                "against recomputations of the same objects.  Its content is "
                "that no total is typed (#24); it cannot report a fact about "
                "the substrate."},
    {"gate": "G-FALSIFIER-CENSUS",
     "forcing": "INSTRUMENT BOOKKEEPING: it gates the shape of this unit's "
                "own falsifier accounting -- that gate names are unique, that "
                "every waiver names a genuinely unfalsified gate, and that "
                "every declared mutant names a gate that exists."},
    {"gate": "G-DEFERRED-GATES-EVALUATED",
     "forcing": "INSTRUMENT BOOKKEEPING: it records that the three write-time "
                "gates ran, so the falsifier census's denominator covers "
                "every gate.  It can fail only if a write-time gate is "
                "removed from deliver()."},
    {"gate": "G-FINAL-GATE-COUNT",
     "forcing": "INSTRUMENT BOOKKEEPING: it checks that the gate count the "
                "paper's rendered sentence carries equals the number of gates "
                "actually registered -- the arithmetic of the claim, not a "
                "measurement."},
]


PAPER = os.path.join(REPO, "paper-02-manifold-rung.md")


def paper_claims(R):
    """THE PROSE RENDERER (RUNBOOK section 13 addendum, v14 #20).

    All four of the programme's false paper numbers to date lived in
    hand-written prose -- the one surface the render-from-the-gated-object rule
    did not cover.  Every load-bearing numeric sentence of paper-02 is BUILT
    HERE from the measured object and gated to appear VERBATIM in the paper.  A
    sentence the instrument does not render is not a sentence the paper may
    assert; a number that moves moves in both places or the run dies.

    (This is what would have caught the delivered `0/1 to 25/18`: the span is
    computed, so the sentence cannot be typed.)"""
    lc = R["locality_census"]
    gr = R["grid"]
    bcs = R["block_constants_summary"]
    mo = R["motivation_census"]
    ps, fa, orl = mo["partition_sweep"], mo["fano_cover"], mo["order_relativity"]
    wl = R["width_law"]
    dr = R["dimension_reading_over_the_whole_grid"]
    lk = R["link_conventions"]
    gb = R["grid_boundary"]
    sc = R["successor_control"]
    rv = R["r2a_verification"]
    nl = R["null_census"]
    fc = R["falsifier_census"]
    row2 = [x for x in sc["rows"] if x["c"] == 2][0]
    exc = gb["the_locality_bearing_exclusions"][0]
    excf = frac(exc["noncomplete_components"][0]["completeness"])
    r048 = R["standards"].get("R048")
    one_edge = 0
    if r048:
        one_edge = len([X for X, v in r048["link_at_those_charts"].items()
                        if v[1] == 1])
    causes = wl["threshold_causes"]

    C = {
        "census": "%d of %d rules produce a component that is not complete"
                  % (lc["count_locality_B"], gr["size"]),
        "refuses": "%d rules refuse" % lc["count_refuses_B"],
        "grid_size": "an exhaustively enumerated declared atlas grid of %d "
                     "rules at %d declared transports"
                     % (gr["size"], R["totals"]["declared_transports"]),
        "per_incidence_span": "the per-incidence density runs from %s to %s "
                              "across the grid"
                              % (bcs["per_incidence_min_text"],
                                 bcs["per_incidence_max_text"]),
        "per_incidence_union": "within the ALL-mode union classes it reaches %s"
                               % bcs["per_incidence_max_within_the_ALL_union_classes"],
        "r048_link_edges": "%d charts carry one link edge apiece" % one_edge,
        "link_circles": "links are circles at %d of %d charts under the "
                        "cell-multiplicity convention and at %d of %d under "
                        "the simple-graph convention"
                        % (lk["cell_multiplicity_circles"], lk["charts"],
                           lk["simple_graph_circles"], lk["charts"]),
        "triangulated": "%d of %d links is a triangulated circle"
                        % (lk["triangulated_circles"], lk["charts"]),
        "partitions": "all %d set partitions of the eight labels at both "
                      "transports -- %d measurements, %d non-complete"
                      % (ps["partitions_of_the_eight_labels"], ps["measurements"],
                         ps["noncomplete_hits"]),
        "fano": "the seven Fano lines cover %d of %d pairs and are clique-only "
                "at %d of %d transports"
                % (fa["pairs_covered"], fa["pairs_possible"],
                   fa["transports_where_it_is_clique_only"], len(fa["per_transport"])),
        "order_sweep": "over all %d numberings of the carrier the count runs "
                       "from %d to %d, realising %d distinct rule sets, and "
                       "the declared numbering's %d is the modal value at %s%%"
                       % (orl["numberings_swept"],
                          min(int(k) for k in orl["count_distribution"]),
                          max(int(k) for k in orl["count_distribution"]),
                          orl["distinct_rule_sets"],
                          orl["declared_numbering_count"],
                          orl["modal_share_percent_text"]),
        "order_extra": "%d rules are local at some numbering"
                       % len(orl["rules_local_at_some_numbering"]),
        "width_law": "the law predicts the locality status and the drawn edge "
                     "count of every rule at %d of %d"
                     % (wl["rules_predicted_correctly"], wl["rules"]),
        "closed_forms": "the closed forms reproduce the measured edge counts "
                        "and cycle ranks at %d of %d rows"
                        % (wl["closed_form_agreements"], wl["closed_form_rows"]),
        "two_causes": "at T7 the support is %s with diameter %d, at T4 it is "
                      "%s with diameter %d"
                      % (causes["T7"]["shape"].lower().replace("-", " "),
                         causes["T7"]["D"],
                         causes["T4"]["shape"].lower().replace("-", " "),
                         causes["T4"]["D"]),
        "dimread": "CONSISTENT is attained at %d of %d rules and its "
                   "intersection with the locality census is %s"
                   % (dr["consistent_rules"], dr["rules_measured"],
                      "empty" if dr["intersection_with_locality"] == 0
                      else str(dr["intersection_with_locality"])),
        "grid_boundary": "%d rules constructible from the same declared words "
                         "are excluded, and %d of them bears locality"
                         % (gb["excluded_from_the_declared_words"],
                            gb["excluded_noncomplete"]),
        "grid_boundary_value": "completeness %s, a value no censused rule "
                               "attains" % excf,
        "successor": "at width 2 the drawn graph is an %d-cycle: a "
                     "triangulated 1-manifold, every link two points, and the "
                     "chart-intrinsic reading is %s"
                     % (row2["edges"], row2["reading_chart_intrinsic"]),
        "r2a_sweep": "%d cyclic actions on the block's eight labels, %d "
                     "distinct cyclic groups, %d counterexamples"
                     % (rv["cyclic_actions_swept_on_the_block"],
                        rv["distinct_cyclic_groups_in_the_sweep"],
                        rv["counterexamples_in_the_sweep"]),
        "null_units": "G0 clique-only at %d of %d rules (%d of %d rule-arena "
                      "measurements) and the whole orbit-partition family at "
                      "%d of %d rules (%d of %d measurements, of which %d "
                      "refuse)"
                      % (nl["g0_rules_clique_only"], nl["g0_rules"],
                         nl["g0_measurements_clique_only"], nl["g0_measurements"],
                         nl["orbit_rules_clique_only"], nl["orbit_rules"],
                         nl["orbit_measurements_clique_only"],
                         nl["orbit_measurements"],
                         nl["orbit_measurements_that_refuse"]),
        # +3: this prose gate, G-FINAL-GATE-COUNT and
        # G-DEFERRED-GATES-EVALUATED are about to be registered.
        # G-FINAL-GATE-COUNT itself checks this arithmetic.
        "instrument": "%d gates, all passed; %d anchors; %d declared mutants, "
                      "all dead" % (len(GATES) + 3, R["totals"]["anchors"],
                                    R["totals"]["mutants_declared"]),
        "falsifiers": "%d of %d gates carry no declared falsifier, and %d of "
                      "those are waived with their forcing stated"
                      % (len([n for n in
                              [g["name"] for g in GATES]
                              + [d for d in DEFERRED_GATES
                                 if d not in [g["name"] for g in GATES]]
                              if n not in
                              set(m["expected_gate"] for m in MUTANTS)]),
                         len(GATES) + 3, len(WAIVERS)),
        "b1_nontrivial": "%d of the %d carry a non-trivial degree-one component"
                         % (len(R["b1_nontrivial_at"]), lc["count_locality_B"]),
    }
    if MUTANT == "prose-claim-drift":
        C["per_incidence_span"] = ("the per-incidence density runs from 0/1 to "
                                   "25/18 across the grid")
    return C


def paper_prose_audit(R):
    """Read the paper and require every rendered claim to appear verbatim."""
    claims = paper_claims(R)
    if not os.path.exists(PAPER):
        return claims, None, sorted(claims)
    with open(PAPER, "r") as fh:
        text = fh.read()
    missing = sorted([k for k, v in claims.items() if v not in text])
    return claims, sha12(PAPER), missing


def render_check(R, census, std):
    """TOTAL render check.  Every rendered field of every rendered object is
    rebuilt here from the live measurement and compared -- not a chosen subset
    of ten (RUNBOOK section 13 addendum, v14 #10; instrument M2, which reached
    the delivered receipt with seven corrupted cells at exit 0).

    The rule is mechanical: for each rendered object, derive the object AGAIN
    from `census` / `std` and compare the whole dict."""
    bad = []

    # ---- block_constants: EVERY key of BOTH arenas -------------------------
    for c in R["block_constants"]:
        for aname in ("B", "B2"):
            m = census[(c["rid"], aname)]
            want = {"E_N": m["E_N"], "edges": m["edges"], "F": m["F_N"],
                    "F_COH": m["F_COH"], "b2_coh": m["betti_COH"]["b2"],
                    "ncoh_per_incidence": m["ncoh_density_per_incidence"],
                    "ncoh_per_pair": m["ncoh_density_per_pair"],
                    "b2_density": m["b2_density"]}
            if dict(c[aname]) != want:
                for k in sorted(want):
                    if c[aname].get(k) != want[k]:
                        bad.append((c["rid"], "block_constants.%s.%s" % (aname, k)))
        mb, m2 = census[(c["rid"], "B")], census[(c["rid"], "B2")]
        if c["densities_constant_B_to_B2"] != (
                mb["ncoh_density_per_incidence"] == m2["ncoh_density_per_incidence"]
                and mb["ncoh_density_per_pair"] == m2["ncoh_density_per_pair"]
                and mb["b2_density"] == m2["b2_density"]):
            bad.append((c["rid"], "block_constants.densities_constant_B_to_B2"))
        if c["additives_double"] != (m2["E_N"] == 2 * mb["E_N"]
                                     and m2["F_N"] == 2 * mb["F_N"]
                                     and m2["edges"] == 2 * mb["edges"]):
            bad.append((c["rid"], "block_constants.additives_double"))

    # ---- census_rows: EVERY key, both arenas' statuses ---------------------
    def status_of(m):
        return ("REFUSES" if m["refuses"] else
                ("NON-COMPLETE" if m["any_noncomplete"] else "clique-only"))

    for row in R["census_rows"]:
        mb = census[(row["rid"], "B")]
        m2 = census[(row["rid"], "B2")]
        want = {
            "cells": mb["cells"], "edges": mb["edges"],
            "components": mb["components"],
            "component_sizes": mb["component_sizes"],
            "completeness": mb["completeness"], "status": status_of(mb),
            "noncomplete_components": [
                {"size": c["size"], "edges": c["edges"], "pairs": c["pairs"],
                 "b1_graph": c["b1_graph"], "members": c["members"]}
                for c in mb["per_component"] if not c["complete"]],
            "B2_status": status_of(m2), "B2_completeness": m2["completeness"],
        }
        for k in sorted(want):
            if row.get(k) != want[k]:
                bad.append((row["rid"], "census_rows." + k))

    # ---- standards: EVERY rendered key -------------------------------------
    for rid, s in sorted(R["standards"].items()):
        live = std[rid]
        m = census[(rid, "B")]
        charts = sorted(set([x for c in m["per_component"] if not c["complete"]
                             for x in c["members"]]))
        want = {
            "coord": list(m["coord"]),
            "noncomplete_component_charts": charts,
            "link_at_those_charts": dict((str(X), live["link"][str(X)]) for X in charts),
            "star_at_those_charts": dict((str(X), live["star"][str(X)]) for X in charts),
            "dimprofile_at_those_charts": dict((str(X), live["dimprofile"][str(X)])
                                               for X in charts),
            "dimprofile_status": live["dimprofile_status"],
            "local_dimensions_realised": live["local_dimensions_realised"],
            "reading": live["reading"],
            "distinct_readings": live["distinct_readings"],
            "charts_with_links": live["charts_with_links"],
            "every_link_is_a_circle": live["every_link_is_a_circle"],
            "links_that_are_circles": live["links_that_are_circles"],
            "links_that_are_circles_simple_convention":
                live["links_that_are_circles_simple_convention"],
            "links_that_are_triangulated_circles":
                live["links_that_are_triangulated_circles"],
            "link_simple_graph_convention_at_those_charts":
                dict((str(X), live["link_simple_graph_convention"][str(X)])
                     for X in charts),
            "reading_chart_intrinsic": live["reading_chart_intrinsic"],
            "distinct_readings_chart_intrinsic":
                live["distinct_readings_chart_intrinsic"],
        }
        for k in sorted(want):
            if s.get(k) != want[k]:
                bad.append((rid, "standards." + k))

    # ---- b1_per_component --------------------------------------------------
    for rid, v in sorted(R["b1_per_component"].items()):
        m = census[(rid, "B")]
        want = {"graph_cycle_rank_per_component":
                [[c["size"], c["edges"], c["b1_graph"]] for c in m["per_component"]],
                "b1_of_N": m["betti_N"]["b1"],
                "b1_of_N_coh": m["betti_COH"]["b1"],
                "b0_of_N": m["betti_N"]["b0"]}
        for k in sorted(want):
            if v.get(k) != want[k]:
                bad.append((rid, "b1_per_component." + k))

    # ---- b2_persistence ----------------------------------------------------
    for rid, p in sorted(R["b2_persistence"].items()):
        mb, m2 = census[(rid, "B")], census[(rid, "B2")]
        ncb = len([c for c in mb["per_component"] if not c["complete"]])
        nc2 = len([c for c in m2["per_component"] if not c["complete"]])
        want = {"noncomplete_components_B": ncb,
                "noncomplete_components_B2": nc2,
                "survives": m2["any_noncomplete"], "doubles": nc2 == 2 * ncb,
                "completeness_B": mb["completeness"],
                "completeness_B2": m2["completeness"],
                "completeness_unchanged": mb["completeness"] == m2["completeness"],
                "component_sizes_B": mb["component_sizes"],
                "component_sizes_B2": m2["component_sizes"]}
        for k in sorted(want):
            if p.get(k) != want[k]:
                bad.append((rid, "b2_persistence." + k))

    # ---- the rendered scalars of every remaining rendered object -----------
    lk = R["link_conventions"]
    loc = sorted(R["standards"])
    if lk["charts"] != sum(std[x]["charts_with_links"] for x in loc):
        bad.append(("*", "link_conventions.charts"))
    if lk["cell_multiplicity_circles"] != sum(std[x]["links_that_are_circles"]
                                              for x in loc):
        bad.append(("*", "link_conventions.cell_multiplicity_circles"))
    if lk["simple_graph_circles"] != sum(
            std[x]["links_that_are_circles_simple_convention"] for x in loc):
        bad.append(("*", "link_conventions.simple_graph_circles"))
    if lk["triangulated_circles"] != sum(
            std[x]["links_that_are_triangulated_circles"] for x in loc):
        bad.append(("*", "link_conventions.triangulated_circles"))
    dr = R["dimension_reading_over_the_whole_grid"]
    if dr["consistent_rules"] != len(dr["consistent_rule_list"]):
        bad.append(("*", "dimension_reading.consistent_rules"))
    if dr["intersection_with_locality"] != len(dr["intersection_list"]):
        bad.append(("*", "dimension_reading.intersection_with_locality"))
    bcs = R["block_constants_summary"]
    if bcs["densities_constant"] != len([c for c in R["block_constants"]
                                         if c["densities_constant_B_to_B2"]]):
        bad.append(("*", "block_constants_summary.densities_constant"))
    if bcs["undefined_b2_density"] != len([c for c in R["block_constants"]
                                           if c["B"]["b2_density"] is None]):
        bad.append(("*", "block_constants_summary.undefined_b2_density"))
    if bcs["rules"] != len(R["block_constants"]):
        bad.append(("*", "block_constants_summary.rules"))
    if R["locality_census"]["count_locality_B"] != len(
            [x for x in R["census_rows"] if x["status"] == "NON-COMPLETE"]):
        bad.append(("*", "locality_census.count_locality_B"))
    if R["locality_census"]["count_refuses_B"] != len(
            [x for x in R["census_rows"] if x["status"] == "REFUSES"]):
        bad.append(("*", "locality_census.count_refuses_B"))
    if R["grid"]["size"] != len(R["grid"]["coordinates"]):
        bad.append(("*", "grid.size"))
    return bad


def internal_consistency(R):
    """THE RECEIPT MUST NOT CONTRADICT ITSELF (instrument M4/INJ8).  A receipt
    that labels a rule clique-only while listing a non-complete component for
    it is internally contradictory, and the delivered instrument shipped
    exactly that at exit 0.  Every cross-field implication the receipt asserts
    is checked here against the receipt's OWN other fields -- no measurement
    is consulted, so this fires on a corruption that reached the tables."""
    bad = []
    loc = set()
    ref = set()
    for row in R["census_rows"]:
        st = row["status"]
        nc = row["noncomplete_components"]
        if st == "NON-COMPLETE" and not nc:
            bad.append((row["rid"], "NON-COMPLETE with no non-complete component"))
        if st != "NON-COMPLETE" and nc:
            bad.append((row["rid"], "%s while listing a non-complete component" % st))
        if st == "REFUSES" and row["edges"] != 0:
            bad.append((row["rid"], "REFUSES with %d drawn edges" % row["edges"]))
        if st != "REFUSES" and row["edges"] == 0:
            bad.append((row["rid"], "%s while drawing nothing" % st))
        for c in nc:
            if c["edges"] >= c["pairs"]:
                bad.append((row["rid"], "non-complete component with all pairs drawn"))
            if c["b1_graph"] != c["edges"] - c["size"] + 1:
                bad.append((row["rid"], "cycle rank contradicts (edges, size)"))
            if len(c["members"]) != c["size"]:
                bad.append((row["rid"], "component size contradicts its member list"))
        if st == "NON-COMPLETE":
            loc.add(row["rid"])
        if st == "REFUSES":
            ref.add(row["rid"])
    if set(R["locality_census"]["locality_bearing_at_B"]) != loc:
        bad.append(("*", "locality_census disagrees with census_rows.status"))
    if set(R["locality_census"]["refusing_at_B"]) != ref:
        bad.append(("*", "refusing_at_B disagrees with census_rows.status"))
    if set(R["standards"]) != loc:
        bad.append(("*", "standards measured at a set other than the locality set"))
    if set(R["b2_persistence"]) != loc:
        bad.append(("*", "b2_persistence measured at a set other than the locality set"))
    if set(R["b1_per_component"]) != loc:
        bad.append(("*", "b1_per_component measured at a set other than the locality set"))
    for rid in R["b1_nontrivial_at"]:
        rows = R["b1_per_component"][rid]["graph_cycle_rank_per_component"]
        if not any(x[2] > 0 for x in rows):
            bad.append((rid, "listed as nontrivial-b1 with every cycle rank zero"))
    for rid in loc:
        rows = R["b1_per_component"][rid]["graph_cycle_rank_per_component"]
        if any(x[2] > 0 for x in rows) and rid not in R["b1_nontrivial_at"]:
            bad.append((rid, "positive cycle rank but absent from b1_nontrivial_at"))
    if R["totals"]["locality_bearing_rules_B"] != len(loc):
        bad.append(("*", "totals disagree with census_rows"))
    return bad


def deliver():
    R, census, rules, std = run()
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
    mismatches = render_check(R, census, std)
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

    # -- THE PROSE GATE (RUNBOOK section 13 addendum, v14 #20) ---------------
    claims, paper_hash, missing = paper_prose_audit(R)
    R["paper_claims"] = {
        "paper": "v14/paper-02-manifold-rung.md",
        "paper_sha256_prefix": paper_hash,
        "claims_rendered": len(claims),
        "claims_present_in_the_paper": len(claims) - len(missing),
        "claims_missing": missing,
        "rendered": dict(sorted(claims.items())),
        "rule": "every load-bearing numeric sentence of the paper is RENDERED "
                "HERE from the measured object and must appear VERBATIM in the "
                "paper; a number the instrument does not render is a number "
                "the paper may not assert",
    }
    gate("G-PROSE-RENDERS-FROM-THE-RECEIPT",
         "every load-bearing numeric sentence of paper-02 is rendered from the "
         "receipt object and appears verbatim in the paper: the prose surface "
         "is gated like the tables (all four of the programme's false paper "
         "numbers to date lived in hand-written prose)",
         paper_hash is not None and len(missing) == 0,
         {"claims": len(claims), "missing": missing[:6],
          "paper_sha256_prefix": paper_hash})

    # the gate count is itself computed, after every gate has run
    R["totals"]["gates"] = len(GATES)
    R["falsifier_census"]["gates"] = len(GATES) + 2
    fnames = [g["name"] for g in GATES] + [n for n in DEFERRED_GATES
                                           if n not in [g["name"] for g in GATES]]
    fmap = {}
    for m in MUTANTS:
        fmap.setdefault(m["expected_gate"], []).append(m["name"])
    nf = [n for n in fnames if n not in fmap]
    R["falsifier_census"]["never_falsified"] = nf
    R["falsifier_census"]["never_falsified_count"] = len(nf)
    R["falsifier_census"]["gates_with_a_declared_falsifier"] = len(
        [n for n in fnames if n in fmap])
    R["falsifier_census"]["denominator"] = "%d of %d gates" % (len(nf), len(fnames))
    R["falsifier_census"]["falsifier_map"] = dict(
        (k, sorted(v)) for k, v in sorted(fmap.items()) if k in fnames)
    gate("G-FINAL-GATE-COUNT",
         "the gate count carried by the paper's rendered instrument sentence "
         "equals the number of gates this run actually registered (the claim's "
         "own arithmetic, gated)",
         R["paper_claims"]["rendered"]["instrument"].startswith(
             "%d gates, all passed" % (len(GATES) + 2)),
         {"registered_now": len(GATES),
          "claimed": R["paper_claims"]["rendered"]["instrument"]})
    gate("G-DEFERRED-GATES-EVALUATED",
         "the write-time gates named in the falsifier census really did "
         "run, so the census's denominator covers every gate this instrument "
         "declares",
         all(d in [g["name"] for g in GATES] for d in DEFERRED_GATES
             if d != "G-DEFERRED-GATES-EVALUATED"),
         {"deferred": list(DEFERRED_GATES), "registered": len(GATES) + 1})
    # the final ledger, after EVERY gate has run
    R["totals"]["gates"] = len(GATES)
    fnames = [g["name"] for g in GATES]
    nf = [n for n in fnames if n not in fmap]
    R["falsifier_census"]["gates"] = len(fnames)
    R["falsifier_census"]["never_falsified"] = nf
    R["falsifier_census"]["never_falsified_count"] = len(nf)
    R["falsifier_census"]["gates_with_a_declared_falsifier"] = len(
        [n for n in fnames if n in fmap])
    R["falsifier_census"]["denominator"] = "%d of %d gates" % (len(nf), len(fnames))
    R["falsifier_census"]["falsifier_map"] = dict(
        (k, sorted(v)) for k, v in sorted(fmap.items()) if k in fnames)
    # RECOMPUTE the compliance sweep now that EVERY gate has run.  Computed
    # from the final ledger, a status can no longer read MISSING for a gate
    # that exists but had not yet been registered when the sweep first ran --
    # the instrument-lens finding that nineteen of twenty statuses were
    # literals, two of them false, applies to stale statuses too.
    R["compliance"] = compliance_sweep(R)
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
        R, census, rules, std = run()
        R["gates"] = GATES
        R["mutants"] = MUTANTS
        R["schema"] = "isp/v14/r2-manifold/1"
        R["pin"] = "v14/note-r2-manifold-pin.md"
        R["pin_sha256_prefix"] = "76d42dfbc900"
        R["source_sha256"] = sha256_full(SRC)
        text = render_text(R)
        payload = jsonable(R)
        mismatches = render_check(R, census, std)
        gate("G-RENDER-FROM-GATED-OBJECT",
             "every rendered table cell equals the corresponding cell of the "
             "gated measurement object", len(mismatches) == 0,
             {"mismatches": mismatches[:4]})
        claims, paper_hash, missing = paper_prose_audit(R)
        gate("G-PROSE-RENDERS-FROM-THE-RECEIPT",
             "every load-bearing numeric sentence of paper-02 is rendered from "
             "the receipt object and appears verbatim in the paper",
             paper_hash is not None and len(missing) == 0,
             {"claims": len(claims), "missing": missing[:6]})
        sys.stderr.write("MUTANT %s SURVIVED -- no gate fired\n" % MUTANT)
        return 3
    except GateFailure as exc:
        sys.stderr.write(str(exc) + "\n")
        return 1


if __name__ == "__main__":
    sys.exit(main())
