#!/usr/bin/env python3.13
# -*- coding: utf-8 -*-
"""
v14 SIG -- SIGNATURE SELECTION: REACHABILITY BEFORE POLARITY.
Instrument for `v14/paper-24-sig.md`.

QUESTION (pin `v14/note-sig-pin.md`, sha256-12 ab73239daff5, ledger #233).
Does the coupled dynamics SELECT, AVOID or remain NEUTRAL toward the
INDEFINITE-signature region of record space -- or is that region unreachable
at every honest parameter choice?  The pin binds two constraints adopted
before it: (A) REACHABILITY BEFORE POLARITY -- no polarity sentence without a
Stage-0 licence, and SIG-BLOCKED-AT-REACHABILITY is a first-class outcome;
(B) NO SITE-MARGINAL OBSERVABLES -- the GDL block-diagonal blindness theorem
makes any site-marginal record-blind, so this unit's observables must read the
record.

  STAGE 0  THE REACHABILITY CENSUS, static and dynamic, at every declared
           arena x horizon.  The static half is the GRAMMAR's own reach: the
           deposit theorem, the region arithmetic, and the attainment ladder
           in four nested classes.  The dynamic half is the coupled walk's:
           the region masses at every horizon on three arenas at both
           emission readings.
  STAGE 1  THE CLEARING (arena, horizon) under a declared cost order.
  STAGE 2  THE POLARITY CENSUS on the clearing arena: exact region masses per
           step, per branch class, under THREE declared measures -- the Born
           branch measure, the uniform-on-support counting measure, and the
           stage-frozen (no-back-reaction) arm -- at both readings.
  STAGE 3  FORCEDNESS across the coin fiber and the mod-3 theorem that says
           what the polarity can and cannot be a property of.

WHAT THIS PROGRAM DOES
  SEC 1  MACHINERY: the gate ledger, the total seal, the text normaliser, the
         input memo with its own liveness gate.
  SEC 2  PROVENANCE: 10 pinned sources, sha256-12 verified, path-value
         anchors, #62 verbatim anchors bound to consumer gates.
  SEC 3  THE ARENA as data: sites, links READ from I7's own receipt, the
         readout, the region trichotomy by two routes.
  SEC 4  STAGE 0A, the static census.
  SEC 5  THE WALK, rebuilt from the parents' declared machinery and ANCHORED
         against paper-20's committed receipt at five independent rows.
  SEC 6  STAGE 0B, the dynamic census.   SEC 7  STAGE 1.
  SEC 8  STAGE 2.   SEC 9  STAGE 3.   SEC 10  THE WALLS.
  SEC 11 The verdict, derived a second time by a comparator that types every
         template itself and shares no literal with the builder; the paper
         gates; the TOTAL seal; the artifacts; the integrity check.

CLI CONTRACT (the #82 minimum: argv parsed against a whitelist)
---------------------------------------------------------------
    python3.13 v14/code/sig_exact.py
        THE DELIVERY RUN, and the ONLY writer.  Exits 0 iff every gate passes.
    --no-write      the same run, writing nothing.
    --numbers       the census only; nothing written.
    --selftest      corrupts one anchor's expected digest IN MEMORY, confirms
                    the run dies at the anchor gate, writes nothing, exits 1
                    (2 if the corrupted run does not die).
    --mutant NAME   runs the pipeline with the named mutant active; exits 1
                    when it is killed (the intended outcome), 0 if it
                    survives, 2 on an unknown NAME.  Writes nothing.
    --break-anchor NAME
                    corrupts the named source anchor's expected digest.
    --verify-paper [PATH]
                    the paper gates against PATH (this unit's paper by
                    default).  1 on drift, 0 clean, 2 if PATH is not a file.
    --list-gates / --list-mutants
                    print the registries and exit 0.
    Any other argument, any unknown flag argument, any missing flag argument
    and any SECOND MODE FLAG exits 2.  Modes do not compose.

ARITHMETIC.  Exact only: Python ints, `fractions.Fraction`, and the
cyclotomic ring Z[w] as integer pairs.  No float exists anywhere -- an AST
scan of this file and a recursive type scan of the receipt are gates.

RUNTIME INPUTS (#46/#91).  Exactly 10 files are read as SOURCES, all
hash-pinned by this unit's frozen declaration, plus exactly one file as the
OBJECT UNDER TEST (this unit's own paper) and this file itself as SELF.  No
other repository state is read and no subprocess of any kind is invoked, so
the run is correct off-tree and with no version control present.  The GDL
delivery is CITED FROM A FROZEN QUOTATION carrying its commit sha rather than
read, because its working-tree copy is held dirty by a concurrent sibling and
a committed-sha read would need a subprocess.
"""

import ast
import hashlib
import json
import os
import re
import sys
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, combinations_with_replacement, product

sys.setrecursionlimit(100000)

SELF = os.path.abspath(__file__)
REPO = os.path.dirname(os.path.dirname(os.path.dirname(SELF)))
OUT_TXT = os.path.join(os.path.dirname(SELF), "sig_output.txt")
OUT_JSON = os.path.join(os.path.dirname(SELF), "sig_receipt.json")

SCHEMA = "isp/v14/sig-signature-selection/1"
PAPER_REL = "v14/paper-24-sig.md"

LINES = []
QUIET = False
MUT = None
READ_CATEGORIES = ("SOURCE", "OBJECT-UNDER-TEST", "SELF", "ARTIFACT-STAGED")
READS_BY_CATEGORY = {}


class GateFail(Exception):
    pass


class CliError(Exception):
    pass


def say(s=""):
    LINES.append(s)
    if not QUIET:
        print(s, flush=True)


def mut(name):
    return MUT == name


def pick(name, normal, corrupted):
    """the mutant hook: returns `normal` unless this run is that mutant."""
    return corrupted if MUT == name else normal


# ===========================================================================
# SECTION 1.  MACHINERY
# ===========================================================================

class Ledger:
    """gates carry their verdict IN the statement; a failure raises."""

    def __init__(self):
        self.rows = []

    def gate(self, name, statement, ok, evidence, waiver=None):
        ok = bool(ok)
        self.rows.append({"gate": name, "statement": statement,
                          "passed": ok, "evidence": str(evidence),
                          "waiver": waiver})
        say("  [%s] %s" % ("PASS" if ok else "FAIL", name))
        say("         %s" % statement)
        say("         evidence: %s" % evidence)
        if not ok:
            raise GateFail("%s :: %s" % (name, evidence))
        return ok


def digest(value):
    if isinstance(value, str):
        return hashlib.sha256(value.encode("utf-8")).hexdigest()[:12]
    return hashlib.sha256(
        json.dumps(value, indent=1, sort_keys=True, default=str).encode("utf-8")
    ).hexdigest()[:12]


def jpath(obj, path):
    cur = obj
    for part in path.split("/"):
        cur = cur[int(part)] if isinstance(cur, list) else cur[part]
    return cur


# ---- THE INPUT MEMO -------------------------------------------------------
# Walks and censuses are memoised ON THEIR COMPLETE INPUT TUPLE, never on a
# label.  A mutant that corrupts an input therefore MISSES and recomputes,
# and a mutant that corrupts a downstream published value hits a cache whose
# contents its corruption does not touch.  RUNBOOK 14 addendum (v13 #185):
# the hit/miss ledger is itself gated and the self-test evaluates fresh.
MEMO = {}
MEMO_HITS = Counter()
MEMO_MISSES = Counter()
MEMO_ENABLED = True


def memo(kind, key, fn):
    if not MEMO_ENABLED:
        MEMO_MISSES[kind] += 1
        return fn()
    k = pick("MUT-MEMO", (kind, key), (kind, "LABEL"))
    if k in MEMO:
        MEMO_HITS[kind] += 1
        return MEMO[k]
    MEMO_MISSES[kind] += 1
    MEMO[k] = fn()
    return MEMO[k]


def read_bytes(rel):
    p = os.path.join(REPO, rel)
    READS_BY_CATEGORY.setdefault("SOURCE", set()).add(os.path.abspath(p))
    with open(p, "rb") as fh:
        return fh.read()


def read_text(path, category):
    if category not in READ_CATEGORIES:
        raise GateFail("G-READS-DECLARED :: undeclared read category %r"
                       % category)
    READS_BY_CATEGORY.setdefault(category, set()).add(os.path.abspath(path))
    with open(path, "r", encoding="utf-8") as fh:
        return fh.read()


_FOLD = {"—": "--", "–": "-", "’": "'", "“": '"',
         "”": '"', "≤": "<=", "≥": ">=", "≠": "!=",
         "≡": "=", "×": "x", "₁": "1", "₂": "2",
         "₀": "0", "₃": "3", "ℓ": "l", "→": "->",
         "⋅": "*", "²": "2", "≈": "~", "⊆": "subset",
         "∈": "in", "∑": "sum", "·": "*", "−": "-",
         "⁄": "/", " ": " ", "⁴": "4", "∏": "prod",
         "√": "sqrt", "ω": "w", "³": "3", "≥": ">="}

_MD_PREFIX = re.compile(r"^(?:\s*(?:>+|[-*+]|\d+[.)])\s+)+")


def mdstrip(s):
    out = []
    for line in s.split("\n"):
        prev = None
        while prev != line:
            prev = line
            line = _MD_PREFIX.sub("", line)
            line = re.sub(r"^\s*>+\s*", "", line)
        out.append(line)
    return "\n".join(out)


def ascii_fold(s):
    for k, v in _FOLD.items():
        s = s.replace(k, v)
    return s


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def canon(s):
    return norm(ascii_fold(mdstrip(s).replace("*", "").replace("`", "")))


NEEDLE_FLOOR = 30


def match_needle(hay, needle):
    n = canon(needle)
    if len(n) < NEEDLE_FLOOR:
        raise GateFail("G-VERBATIM :: needle below the #62 length floor: %r"
                       % needle)
    h = canon(hay)
    return n in h or n.replace(" ", "") in h.replace(" ", "")


def norm_src(s):
    return re.sub(r"\s+", " ", s).replace('"', "").replace("'", "").strip()


# ===========================================================================
# SECTION 2.  THE FROZEN DECLARATION (RUNBOOK section 15: the arena is data)
# ===========================================================================

SOURCES = [
    ("A-PIN", "v14/note-sig-pin.md", "ab73239daff5",
     "THIS UNIT'S PIN (ledger #233): the stages, the two binding constraints, "
     "the pre-registered outcome names."),
    ("A-P21", "v14/paper-21-r4dec.md", "ef4a8c35a0c4",
     "PAPER 21 (terminal): the R = 4 arena, the covering machinery, the "
     "incidence spectrum, block quantisation, the det spectrum, the naming "
     "wall this unit inherits."),
    ("A-P21REC", "v14/code/r4dec_receipt.json", "a4538c7019e6",
     "PAPER 21's COMMITTED RECEIPT: the incidence spectrum and the R = 4 "
     "determinant spectrum, READ as data and reproduced here."),
    ("A-P20", "v14/paper-20-coupling.md", "4824d190af73",
     "PAPER 20 (terminal): the coupled machine, the emission law, the coin "
     "fiber, the admissibility ladder and the exit census this unit rebuilds "
     "and anchors against."),
    ("A-P20REC", "v14/code/coupling_receipt.json", "55273f6b6068",
     "PAPER 20's COMMITTED RECEIPT: the branch ladder, the exit "
     "probabilities at both readings, the exit census and the visit "
     "schedule -- the five rows this unit's rebuilt walk must reproduce."),
    ("A-P20CODE", "v14/code/coupling_exact.py", "72e7b299f66e",
     "PAPER 20's INSTRUMENT: the declared machinery this unit re-implements "
     "independently -- coin, shift, emission readings, update semantics."),
    ("A-HA", "v13/paper-ha-successor.md", "f286ba10d2d9",
     "I7 / HA: the declared readout and the admissibility criterion."),
    ("A-I7", "v13/code/ha_successor_receipt.json", "542b8735daf0",
     "I7's ARENA AS DATA: the declared link set and the declared record "
     "family, including G-SINGULAR and G-INDEF, read and never re-typed."),
    ("A-L1", "v11/note-L1-lorentz-no-go-lemma.md", "93ea24591c3c",
     "L-1: the fourth-form clause argued before any test, and the sentence "
     "retracted in 2026 that no paper of this line may reproduce."),
    ("A-CAT", "v11/note-v11p0a-reproduction-catalog.md", "0cebe543e814",
     "the reproduction catalog: the BHS block and the Kleitman-Rothschild "
     "height-control warning."),
]
SOURCE_IDS = [s[0] for s in SOURCES]

BANNED_L1 = ("precisely the form U4 tests, and precisely the form the "
             "corpus's strongest relativity result took")

# THE GDL CITATION, frozen here rather than read: the working-tree copy of
# `v14/paper-25-gdl.md` is held dirty by a concurrent sibling and a
# committed-sha read would require a subprocess, which #91 forbids.  The
# quotation is this unit's own frozen declaration and carries the commit it
# was taken from.
GDL_COMMIT = "4c85ca4"
GDL_REL = "v14/paper-25-gdl.md"
GDL_BLINDNESS = ("a decoherence functional built from the state at a single "
                 "time, in a basis the coin acts on site-locally, is blind "
                 "to the record it is supposed to be a function of")

PATH_ROWS = [
    ("P-I7-LINKS", "A-I7", ("declarations", "links_d2"),
     [[1, 0], [0, 1], [1, 1]],
     "the declared link set: the two axis links and the one positive "
     "diagonal -- this unit's three cell directions"),
    ("P-I7-RECORDS", "A-I7", ("declarations", "records_d2"),
     {"G-ANISO": [1, 4, 5], "G-ANISO2": [4, 9, 13], "G-DIAG2": [2, 2, 4],
      "G-FLAT": [1, 1, 2], "G-INDEF": [1, 1, 6], "G-OFFDIAG": [2, 2, 6],
      "G-OFFDIAG2": [3, 5, 12], "G-OFFNEG": [3, 5, 4],
      "G-SINGULAR": [1, 1, 4]},
     "the declared homogeneous record family: G-FLAT is this unit's clearing "
     "arena, G-SINGULAR and G-INDEF are the two non-admissible declared "
     "records whose budgets this unit measures"),
    ("P-P21-SPECTRUM", "A-P21REC", ("family", "incidence_spectrum"),
     {"0": 1, "4": 27, "6": 54, "7": 162, "9": 36},
     "paper-21's committed incidence spectrum over the 280 partitions -- "
     "recomputed here from the deposit map"),
    ("P-P21-DET", "A-P21REC", ("price", "det_spectrum"),
     {"3/4": 437184, "1": 386640, "7/4": 76896},
     "paper-21's committed R = 4 determinant spectrum: three POSITIVE "
     "values, no zero and no negative one -- the static R = 4 row this unit "
     "extends"),
    ("P-P20-EXIT", "A-P20REC", ("ladder", "rows", 4, "coupled_exit"),
     "927415552/847288609443",
     "paper-20's committed Born-menu exit probability at horizon 5 on the "
     "welded record -- reproduced here by an independent rebuild"),
    ("P-P20-EXITB", "A-P20REC", ("ladder", "rows", 9, "coupled_exit"),
     "37440224/5811307335",
     "paper-20's committed RECORD-menu exit probability at horizon 5 -- the "
     "second independent anchor on the rebuilt walk"),
    ("P-P20-BRANCHES", "A-P20REC",
     ("ensemble", "arms", "A-COUPLED", "levels", 4, "branches"), 284078,
     "paper-20's committed Born-menu branch count at horizon 5"),
    ("P-P20-BRANCHESB", "A-P20REC",
     ("ensemble", "arms", "B-COUPLED", "levels", 4, "branches"), 314928,
     "paper-20's committed record-menu branch count at horizon 5"),
    ("P-P20-EXITCENSUS", "A-P20REC", ("exit_census", "count_vectors"),
     {"1,1,4": 466, "1,4,1": 471, "4,1,1": 379},
     "paper-20's committed exit census: every inadmissible leaf carries one "
     "site at a SINGULAR code, three-fold degenerate across the link "
     "classes -- and no indefinite one"),
    ("P-P20-THIRD", "A-P20REC",
     ("exit_census", "schedule", "earliest_third_visit"), 5,
     "paper-20's committed return-time row: the earliest third visit to a "
     "site is step 5 -- the datum that fixes both dynamic floors"),
]

VERBATIM = [
    ("V-P20-EXIT", "A-P20",
     "the coupled record leaves I7's admissible class with exact probability "
     "927415552/847288609443 at the Born menu", "G-WALK-ANCHORED"),
    ("V-P20-CENSUS", "A-P20",
     "all 1,316 inadmissible leaves carry the excess pattern (0, 0, 3) at "
     "exactly one site", "G-WALK-ANCHORED"),
    ("V-P20-OPEN", "A-P20",
     "Whether the probability grows, whether the indefinite region is "
     "reached at all, and whether a halt-on-inadmissibility semantics "
     "changes any verdict are three separate measurements, none taken here",
     "G-STAGE0-DYNAMIC"),
    ("V-P20-MOD3", "A-P20",
     "the walk consumes the count residue n mod 3, not the count",
     "G-MOD3-THEOREM"),
    ("V-P20-SYLVESTER", "A-P20",
     "a record is admissible when q is nonsingular and positive definite at "
     "every site, by the exact Sylvester criterion", "G-REGION-ARITHMETIC"),
    ("V-P21-BUDGET", "A-P21",
     "no round can deposit more than 9 link incidences", "G-DEPOSIT-THEOREM"),
    ("V-P21-BLOCK", "A-P21",
     "Across the whole covering class the maximum cell count is 2",
     "G-STATIC-LADDER"),
    ("V-P21-COLLINEAR", "A-P21",
     "the three link-direction parallel classes of AG(2,3) with the diagonal "
     "class taken twice", "G-COLLINEAR-LADDER"),
    ("V-P21-NAMED", "A-P21",
     "is a positive definite Euclidean form on a nine-site lattice, it is "
     "not a signature, it is not a metric on any continuum",
     "G-WALL-SIGNATURE-NAMED"),
    ("V-CAT-BHS", "A-CAT",
     "a Poisson sprinkling admits no Lorentz-invariant finite-valency graph",
     "G-WALL-BHS"),
]

# ===========================================================================
# SECTION 3.  THE ARENA, AS DATA
# ===========================================================================

SITES = tuple((i, j) for i in range(3) for j in range(3))
SITE_INDEX = {s: k for k, s in enumerate(SITES)}
NSITE = 9
NLINK = 3
NCELL = 27
DIM = 27
ANT = (1, 2)
CLASS_NAMES = ("ROW", "COL", "DIA", "ANT")


def vadd(a, b):
    return ((a[0] + b[0]) % 3, (a[1] + b[1]) % 3)


def vsub(a, b):
    return ((a[0] - b[0]) % 3, (a[1] - b[1]) % 3)


def cell(si, li):
    return si * 3 + li


def zmul(z1, z2):
    a, b = z1
    c, d = z2
    return (a * c - b * d, a * d + b * c - b * d)


def zadd(z1, z2):
    return (z1[0] + z2[0], z1[1] + z2[1])


def zconj(z):
    a, b = z
    return (a - b, -b)


def absq(z):
    """|a + b w|^2 = a^2 - a b + b^2, a RATIONAL INTEGER."""
    a, b = z
    return a * a - a * b + b * b


Z0 = (0, 0)
Z1 = (1, 0)
WPOW = [(1, 0), (0, 1), (-1, -1)]

REGION_NAMES = ("POSDEF", "SINGULAR", "INDEFINITE")


def det4_of(n1, n2, n3):
    """FOUR TIMES the determinant of I7's readout, as an INTEGER.  Route 2 of
    the region arithmetic: the symmetric (Heron) form."""
    return 2 * (n1 * n2 + n1 * n3 + n2 * n3) - (n1 * n1 + n2 * n2 + n3 * n3)


def q_of(nvec):
    """I7's own readout: the three link counts at a site give the 2x2 form.
    Route 1 -- the readout as written, in exact Fractions."""
    n1, n2, n3 = nvec
    q11 = Fraction(n1)
    q22 = Fraction(n2)
    q12 = Fraction(n3 - n1 - n2, 2)
    return q11, q22, q12, q11 * q22 - q12 * q12


def region_of(nvec):
    """THE TRICHOTOMY.  A site is POSDEF when I7's exact Sylvester criterion
    holds (q11 > 0 and det > 0), SINGULAR when det = 0, INDEFINITE when
    det < 0.  This function reads the RECORD and nothing else -- constraint B
    (no site-marginal observables) is discharged by construction, and the
    argument list is what G-CONSTRAINT-B checks."""
    d = det4_of(*nvec)
    if d < 0:
        return 2
    if d == 0:
        return 1
    return 0 if nvec[0] > 0 else 1


def record_region(n):
    """the record's region: the WORST of its nine sites."""
    r = 0
    for s in range(NSITE):
        v = region_of((n[s * 3], n[s * 3 + 1], n[s * 3 + 2]))
        if v > r:
            r = v
    return r


# ===========================================================================
# SECTION 4.  STAGE 0A -- THE STATIC CENSUS (the grammar's own reach)
# ===========================================================================

def all_partitions():
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
    rec(tuple(range(NSITE)), [])
    return sorted(out)


def class_of(d, links):
    """the parallel class of a difference: one of the three DECLARED link
    directions, or the undeclared fourth (ANT)."""
    for i, u in enumerate(links):
        if d == u or d == ((2 * u[0]) % 3, (2 * u[1]) % 3):
            return i
    return None


def group_deposit(group, links):
    """THE DEPOSIT MAP.  A conflict group's realised co-division pairs are its
    three site pairs.  A pair whose difference lies in a DECLARED direction l
    is the cell (tail, l), where head = tail + l -- the three +l moves along a
    line of direction l cover that line's three unordered pairs exactly once,
    so (site, link) and (realised pair) are in bijection.  A pair along the
    undeclared direction is FOREIGN and deposits nothing."""
    cells, foreign = [], 0
    for a, b in combinations(group, 2):
        x, y = SITES[a], SITES[b]
        i = class_of(vsub(y, x), links)
        if i is None:
            foreign += 1
            continue
        tail = a if vadd(x, links[i]) == y else b
        cells.append(cell(tail, i))
    return cells, foreign


def partition_deposit(p, links):
    cells, foreign = [], 0
    for g in p:
        c, f = group_deposit(g, links)
        cells += c
        foreign += f
    return cells, foreign


def parallel_class(d):
    """the resolvable partition of AG(2,3) into the three lines of slope d."""
    seen, out = set(), []
    for s in range(NSITE):
        x = SITES[s]
        L = tuple(sorted((s, SITE_INDEX[vadd(x, d)],
                          SITE_INDEX[vadd(vadd(x, d), d)])))
        if L not in seen:
            seen.add(L)
            out.append(L)
    return tuple(sorted(out))


def cell_orbit(links):
    """the arena's own symmetry group acting on the 27 cells: the linear maps
    of AG(2,3) that preserve the DECLARED link set as a set, together with the
    nine translations.  Transitivity is what licenses every single-cell census
    below as a statement about all 27."""
    gl = []
    for a, b, c, d in product(range(3), repeat=4):
        if (a * d - b * c) % 3:
            gl.append(((a, b), (c, d)))
    keep = []
    for M in gl:
        img = set()
        for u in links:
            v = ((M[0][0] * u[0] + M[0][1] * u[1]) % 3,
                 (M[1][0] * u[0] + M[1][1] * u[1]) % 3)
            img.add(class_of(v, links))
        if img == {0, 1, 2}:
            keep.append(M)
    seen, frontier = set(), {(0, 2)}
    while frontier:
        new = set()
        for (s, l) in frontier:
            if (s, l) in seen:
                continue
            seen.add((s, l))
            x, u = SITES[s], links[l]
            for M in keep:
                y = ((M[0][0] * x[0] + M[0][1] * x[1]) % 3,
                     (M[1][0] * x[0] + M[1][1] * x[1]) % 3)
                w = ((M[0][0] * u[0] + M[0][1] * u[1]) % 3,
                     (M[1][0] * u[0] + M[1][1] * u[1]) % 3)
                j = class_of(w, links)
                for t in SITES:
                    a = vadd(y, t)
                    b = vadd(a, w)
                    tail = a if vadd(a, links[j]) == b else b
                    new.add((SITE_INDEX[tail], j))
        frontier = new - seen
    return len(keep), len(seen)


def field_of(rounds, DEP):
    n = [0] * NCELL
    for i in rounds:
        for m in DEP[i]:
            n[m] += 1
    return n


def static_floors(box):
    """THE FLOOR THEOREM, machine-checked over a declared code box: at a site
    whose three cells are all >= 1, SINGULAR requires a cell at >= 4 and
    INDEFINITE a cell at >= 5.  With the deposit theorem (a cell takes at most
    one incidence per round) this converts directly into a budget floor."""
    fs = fi = None
    for a in range(1, box + 1):
        for b in range(1, box + 1):
            for c in range(1, box + 1):
                d = det4_of(a, b, c)
                k = max(a, b, c)
                if d == 0 and (fs is None or k < fs[0]):
                    fs = (k, a + b + c, (a, b, c))
                if d < 0 and (fi is None or k < fi[0]):
                    fi = (k, a + b + c, (a, b, c))
    return fs, fi


def min_uncovered_5(PCELLS, MASKS, target):
    """EXHAUSTIVE over every multiset of five rounds that all hit one cell:
    the least number of cells left uncovered.  At R = 5 the deposit theorem
    forces exactly this shape for an indefinite site, so a positive minimum
    is a proof that no COVERING R = 5 record carries one."""
    pc = [i for i in range(len(PCELLS)) if target in PCELLS[i]]
    full = (1 << NCELL) - 1
    best, seen = NCELL + 1, 0
    for combo in combinations_with_replacement(pc, 5):
        cov = 0
        for i in combo:
            cov |= MASKS[i]
        seen += 1
        u = bin(full & ~cov).count("1")
        if u < best:
            best = u
    return best, seen, len(pc)


def exists_covering_indefinite(R, pool, PCELLS, MASKS, target_site=0,
                               want=None):
    """does a multiset of R rounds from `pool` induce a COVERING record with
    an INDEFINITE site at `target_site`?  Depth-first with two sound prunes:
    the uncovered cells must fit in what the remaining rounds can deposit, and
    the site's own code must still be able to go indefinite (each cell grows
    by at most one per round)."""
    full = (1 << NCELL) - 1
    base = target_site * 3
    n = [0] * NCELL
    found = []

    def rec(k, start, cov):
        if found:
            return
        if k == R:
            if cov == full:
                c = (n[base], n[base + 1], n[base + 2])
                if min(c) >= 1 and det4_of(*c) < 0:
                    found.append((list(n), c))
            return
        rem = R - k
        if bin(full & ~cov).count("1") > 9 * rem:
            return
        srt = sorted((n[base], n[base + 1], n[base + 2]))
        if det4_of(max(srt[0], 1), max(srt[1], 1), srt[2] + rem) >= 0:
            return
        for idx in range(start, len(pool)):
            p = pool[idx]
            for m in PCELLS[p]:
                n[m] += 1
            rec(k + 1, idx, cov | MASKS[p])
            for m in PCELLS[p]:
                n[m] -= 1
            if found:
                return
    rec(0, 0, 0)
    return found[0] if found else None


def static_census(links):
    """STAGE 0A, computed once and memoised on its complete input."""
    P = all_partitions()
    DEP, FOR, MASKS = [], [], []
    spec = Counter()
    maxcell = maxsite = 0
    for p in P:
        c, f = partition_deposit(p, links)
        DEP.append(tuple(c))
        FOR.append(f)
        MASKS.append(sum(1 << x for x in set(c)))
        spec[len(c)] += 1
        cnt = Counter(c)
        maxcell = max(maxcell, max(cnt.values()) if cnt else 0)
        sc = Counter(m // 3 for m in c)
        maxsite = max(maxsite, max(sc.values()) if sc else 0)
    SAT = [i for i in range(len(P)) if len(DEP[i]) == 9]
    CLS = {}
    for k, nm in enumerate(CLASS_NAMES):
        d = links[k] if k < 3 else ANT
        CLS[nm] = P.index(parallel_class(d))
    # the R = 1 row: one ROW round, unrestricted.  Its budget is the length
    # of the probe's own round list, not a typed 1.
    r1_rounds = [CLS["ROW"]]
    n1 = field_of(r1_rounds, DEP)
    codes1 = sorted(set((n1[s * 3], n1[s * 3 + 1], n1[s * 3 + 2])
                        for s in range(NSITE)))
    r1 = [region_of(c) for c in codes1]
    # the collinear ladder: ROW^a COL^b DIA^c
    ladder = []
    for (a, b, c) in ((1, 1, 1), (1, 1, 2), (1, 1, 3), (1, 1, 4), (1, 1, 5),
                      (1, 1, 6), (2, 2, 2)):
        rounds = [CLS["ROW"]] * a + [CLS["COL"]] * b + [CLS["DIA"]] * c
        n = field_of(rounds, DEP)
        codes = set((n[s * 3], n[s * 3 + 1], n[s * 3 + 2])
                    for s in range(NSITE))
        ladder.append({"record": [a, b, c], "R": a + b + c,
                       "homogeneous": len(codes) == 1,
                       "covering": min(n) > 0, "incidences": sum(n),
                       "foreign": sum(FOR[i] for i in rounds),
                       "region": REGION_NAMES[region_of(sorted(codes)[0])],
                       "det4": det4_of(*sorted(codes)[0])})
    fs, fi = static_floors(12)
    target = cell(0, 2)
    mu, mu_seen, mu_pool = memo(
        "min_uncovered", (target, tuple(MASKS)),
        lambda: min_uncovered_5(DEP, MASKS, target))
    rows = []
    for R in (4, 5, 6, 7):
        for nm, pool in (("ALL", list(range(len(P)))), ("LIVE", SAT)):
            if R == 5 and nm == "ALL":
                # the deposit theorem makes the five-round case exactly the
                # shape min_uncovered_5 enumerates, and that enumeration is
                # exhaustive: no search is needed and none is run.
                w = None
            else:
                w = memo("cov", (R, nm, tuple(MASKS)),
                         lambda R=R, pool=pool: exists_covering_indefinite(
                             R, pool, DEP, MASKS))
            rows.append({"R": R, "pool": nm, "exists": bool(w),
                         "witness_code": list(w[1]) if w else None,
                         "witness_total": sum(w[0]) if w else None})
    # the FULL-SITE (site-local) attainment at R = 5, and its count
    pc = [i for i in range(len(P)) if target in DEP[i]]
    prof = Counter((DEP[i].count(cell(0, 0)), DEP[i].count(cell(0, 1)))
                   for i in pc)
    fullsite = None
    cnt5 = 0
    for combo in combinations_with_replacement(sorted(prof), 5):
        a = sum(k[0] for k in combo)
        b = sum(k[1] for k in combo)
        code = (a, b, 5)
        if min(code) >= 1 and det4_of(*code) < 0:
            ways = 1
            for k, m in Counter(combo).items():
                nk = prof[k]
                ways *= len(list(combinations_with_replacement(range(nk), m)))
            cnt5 += ways
            if fullsite is None:
                fullsite = code
    # an explicit witness of that class, and ITS OWN covered-cell count --
    # computed from the witness rather than typed
    fswitness, fscov = None, None
    for combo in combinations_with_replacement(pc, 5):
        n = field_of(combo, DEP)
        cd = (n[0], n[1], n[2])
        if min(cd) >= 1 and det4_of(*cd) < 0:
            fswitness = list(combo)
            fscov = sum(1 for x in n if x > 0)
            break
    ngroups, orbit = cell_orbit(links)
    return {"partitions": len(P), "incidence_spectrum": dict(spec),
            "max_per_cell_per_round": maxcell,
            "max_per_site_per_round": maxsite,
            "saturating": len(SAT),
            "saturating_foreign_free": sum(1 for i in SAT if FOR[i] == 0),
            "r1_rounds": len(r1_rounds),
            "r1_codes": [list(c) for c in codes1],
            "r1_regions": sorted(set(REGION_NAMES[x] for x in r1)),
            "r1_sites_indefinite": sum(1 for x in r1 if x == 2) * NSITE
            // max(1, len(codes1)),
            "collinear_ladder": ladder,
            "floor_singular": {"max_cell": fs[0], "sum": fs[1],
                               "code": list(fs[2])},
            "floor_indefinite": {"max_cell": fi[0], "sum": fi[1],
                                 "code": list(fi[2])},
            "r5_min_uncovered": mu, "r5_multisets": mu_seen,
            "r5_pool": mu_pool,
            "fullsite_r5_code": list(fullsite) if fullsite else None,
            "fullsite_r5_multisets": cnt5,
            "fullsite_r5_witness": fswitness,
            "fullsite_r5_cells_covered": fscov,
            "covering_rows": rows,
            "linear_maps": ngroups, "cell_orbit": orbit}


# ===========================================================================
# SECTION 5.  THE WALK -- rebuilt from the parents' declared machinery
# ===========================================================================
# The machinery is paper-20's, re-implemented independently and anchored
# against its committed receipt at five rows.  The coin is site-block-diagonal
# C(x) = G . D(x) with D(x) = diag(w^{n_l(x)}); the shift is |x,l> -> |x+l,l>;
# a step emits exactly one division event on a cell, whose weight is the
# law-native kernel's own -- the post-coin Born weight under READING A (the
# Born menu) and p(x) n_l(x)/N(x) under READING B (the record menu).  The
# emission is non-selective: the state is not collapsed onto the emitted cell.

GN = tuple(tuple(2 if i != j else -1 for j in range(3)) for i in range(3))
GROVER_Z = tuple(tuple((GN[i][j], 0) for j in range(3)) for i in range(3))

# THE S_3-COVARIANT COIN FAMILY (paper-20 section 3.2): 3C = 3a I + 3b J, one
# class per member of the fiber, the delivered member first.
COIN_FIBER = (
    ("GROVER", (-3, 0), (2, 0), "b/a = -2/3, the delivered member"),
    ("W", (3, 0), (0, 1), "b/a = w/3"),
    ("MW", (3, 0), (-1, 1), "b/a = (-1+w)/3"),
    ("MMW", (3, 0), (-1, -1), "b/a = (-1-w)/3"),
    ("M2W", (3, 0), (-2, -1), "b/a = (-2-w)/3"),
)


def coin_matrix(a3, b3):
    return tuple(tuple((a3[0] + b3[0], a3[1] + b3[1]) if i == j else b3
                       for j in range(3)) for i in range(3))


def coin_unitary(M):
    """M M* = 9 I exactly in Z[w] -- M is 3C, so unitarity of C reads this."""
    for i in range(3):
        for j in range(3):
            tot = Z0
            for k in range(3):
                tot = zadd(tot, zmul(M[i][k], zconj(M[j][k])))
            if tot != ((9, 0) if i == j else Z0):
                return False
    return True


def shift_table(links):
    return tuple(cell(SITE_INDEX[vadd(SITES[s], links[i])], i)
                 for s in range(NSITE) for i in range(NLINK))


def walk_step(psi, n, M, table):
    """one coupled step's quantum half: coin, then shift.  Returns the shifted
    state and the post-coin Born weights, which ARE the arena's menu."""
    post = [Z0] * DIM
    rational = all(M[i][j][1] == 0 for i in range(3) for j in range(3))
    for s in range(NSITE):
        b = s * 3
        src = [zmul(psi[b + j], WPOW[n[b + j] % 3]) for j in range(3)]
        if rational:
            for i in range(3):
                a = c = 0
                for j in range(3):
                    g = M[i][j][0]
                    z = src[j]
                    a += g * z[0]
                    c += g * z[1]
                post[b + i] = (a, c)
        else:
            for i in range(3):
                tot = Z0
                for j in range(3):
                    tot = zadd(tot, zmul(M[i][j], src[j]))
                post[b + i] = tot
    out = [Z0] * DIM
    for m in range(DIM):
        out[table[m]] = post[m]
    return out, [absq(post[m]) for m in range(DIM)]


def run_arm(T, n0, links, reading="A", coin=GROVER_Z, feedback=True,
            update=True, start=(0, 0), init_coin=0, paths=False):
    """ONE ARM, exhaustively to horizon T.  Every branch of the emission tree
    is carried: no sampling, no pruning, no truncation by weight.

      feedback=True  the coin reads the LIVE record (the coupled arm).
      feedback=False THE STAGE-FROZEN CONTROL: the identical walk, the
                     identical emission rule and the identical branching on
                     phases that never update, while the record still
                     accumulates -- the arm that isolates the back-reaction
                     from the accumulation.
      update=False   paper-20's frozen arm: the record never changes at all.

    The Born branch weight is an exact Fraction; the uniform-on-support
    counting measure is carried as an integer denominator product, so both
    measures stay exact and neither is a re-weighting of the other's numbers.

      READING A (the Born menu).  q(l|x) is the post-coin Born weight, so the
                 law-native kernel makes the emission distribution the
                 post-coin Born distribution itself.
      READING B (the record menu).  q(l|x) is the division count n_l(x), so
                 the weight is p(x) n_l(x)/N(x)."""
    table = shift_table(links)
    p0 = [Z0] * DIM
    p0[cell(SITE_INDEX[start], init_coin)] = Z1
    one = Fraction(1)
    frontier = [(tuple(p0), tuple(n0), tuple(n0), one, 1, ())]
    levels = []
    visits = defaultdict(set)
    checks = [0, 0]
    for t in range(T):
        den = 9 ** (t + 1)
        nxt = []
        for (psi, nph, nrec, w, dnull, path) in frontier:
            newpsi, J = walk_step(list(psi), nph, coin, table)
            for s in range(NSITE):
                if J[s * 3] + J[s * 3 + 1] + J[s * 3 + 2]:
                    visits[SITES[s]].add(t + 1)
            wts = [None] * DIM
            for s in range(NSITE):
                b = s * 3
                pn = J[b] + J[b + 1] + J[b + 2]
                N = nrec[b] + nrec[b + 1] + nrec[b + 2]
                for i in range(3):
                    if reading == "A":
                        wts[b + i] = Fraction(J[b + i], den)
                    elif pn and N:
                        wts[b + i] = Fraction(pn * nrec[b + i], den * N)
                    else:
                        wts[b + i] = Fraction(0)
            sup = [m for m in range(DIM) if wts[m]]
            checks[0] += 1
            if sum(wts) != 1:
                checks[1] += 1
            npsi = tuple(newpsi)
            k = len(sup)
            for m in sup:
                if update:
                    nn = list(nrec)
                    nn[m] += 1
                    nn = tuple(nn)
                else:
                    nn = nrec
                nxt.append((npsi, nn if feedback else nph, nn,
                            w * wts[m], dnull * k,
                            (path + (m,)) if paths else ()))
        frontier = nxt
        levels.append(frontier)
    return {"levels": levels, "checks": checks,
            "visits": {"%d%d" % k: sorted(v)
                       for k, v in sorted(visits.items())}}


def region_profile(levels, T, reading):
    """the region masses at every step under BOTH declared measures, plus the
    exit census at the final step.  Every quantity here is a functional of the
    RECORD -- constraint B."""
    out = []
    census = Counter()
    leaves_out = 0
    for t, frontier in enumerate(levels):
        born = defaultdict(Fraction)
        null = defaultdict(lambda: defaultdict(int))
        maxcell = 0
        for (_p, _nph, n, w, dn, _pa) in frontier:
            r = record_region(n)
            born[r] += w
            null[r][dn] += 1
            m = max(n)
            if m > maxcell:
                maxcell = m
            if t == T - 1 and r:
                leaves_out += 1
                for s in range(NSITE):
                    c = (n[s * 3], n[s * 3 + 1], n[s * 3 + 2])
                    if region_of(c):
                        census["%d,%d,%d|%s" % (c + (REGION_NAMES[
                            region_of(c)],))] += 1
        row = {"t": t + 1, "branches": len(frontier), "max_cell": maxcell,
               "born": {REGION_NAMES[r]: str(born[r]) for r in sorted(born)},
               "null": {REGION_NAMES[r]: str(sum(Fraction(c, d)
                                                 for d, c in null[r].items()))
                        for r in sorted(null)},
               "reading": reading}
        out.append(row)
    return out, dict(census), leaves_out


def massof(row, key, region):
    v = row[key].get(region)
    return Fraction(v) if v is not None else Fraction(0)


def first_positive(rows, key, region):
    for r in rows:
        if massof(r, key, region) > 0:
            return r["t"]
    return None


# ===========================================================================
# SECTION 6.  THE DECLARED ARENAS AND THE DECLARED HORIZON
# ===========================================================================
# Every arena is a HOMOGENEOUS record (1, 1, c) -- the collinear arrangement's
# own family, reachable by the committed grammar at R = 2 + c (section 4).
# A3 is paper-19/20's welded record, A4 is I7's own declared G-FLAT and
# paper-21's driven record, A5 is the cheapest arena one round above it.
# A6/A7/A8 are the residue partners the mod-3 theorem pairs them with.

ARENAS = (("A3", 1, 3, "the welded R = 3 record, paper-20's own arena"),
          ("A4", 2, 4, "I7's DECLARED G-FLAT, paper-21's driven record"),
          ("A5", 3, 5, "the cheapest live record one round above G-FLAT"),
          ("A6", 4, 6, "I7's declared G-SINGULAR"),
          ("A7", 5, 7, "the cheapest homogeneous indefinite record"),
          ("A8", 6, 8, "I7's declared G-INDEF"))
HORIZON = 5
LADDER_T = 6            # the extension horizon, declared and priced
PRIMARY = "A4"


def arena_field(c):
    return tuple((1, 1, c)[i % 3] for i in range(NCELL))


def arena_of(name):
    return [a for a in ARENAS if a[0] == name][0]


# ===========================================================================
# SECTION 7.  THE PRUNED ENGINE (the horizon extension) AND ITS SOUNDNESS
# ===========================================================================

def run_pruned(T, n0, links, coin=GROVER_Z):
    """the same arm, carrying only branches that can still leave the all-
    POSDEF region.  THE PRUNE IS A THEOREM: a branch whose largest per-cell
    emission count is e, with r steps left, can raise no cell above its start
    by more than e + r; if that cannot reach the region floor of section 4,
    the branch and its whole subtree stay POSDEF and their mass is carried in
    aggregate.  The gate below re-runs the unpruned engine at the horizon they
    share and requires identical masses."""
    table = shift_table(links)
    p0 = [Z0] * DIM
    p0[cell(SITE_INDEX[(0, 0)], 0)] = Z1
    base = tuple(n0)
    need = None
    for c in range(1, 40):
        probe = list(base)
        probe[2] += c
        if region_of((probe[0], probe[1], probe[2])):
            need = c
            break
    frontier = [(tuple(p0), base, 1, 0)]
    kept = []
    rows = []
    for t in range(T):
        den = 9 ** (t + 1)
        nxt = []
        pruned_mass = 0
        for (psi, n, w, e) in frontier:
            newpsi, J = walk_step(list(psi), n, coin, table)
            npsi = tuple(newpsi)
            for m in range(DIM):
                if not J[m]:
                    continue
                nn = list(n)
                nn[m] += 1
                nn = tuple(nn)
                ee = max(e, nn[m] - base[m])
                ww = w * J[m]
                if ee + (T - t - 1) < need:
                    pruned_mass += ww
                else:
                    nxt.append((npsi, nn, ww, ee))
        frontier = nxt
        tden = 9 ** ((t + 1) * (t + 2) // 2)
        born = defaultdict(int)
        for (_p, n, w, _e) in frontier:
            born[record_region(n)] += w
        rows.append({"t": t + 1, "retained": len(frontier),
                     "region_floor_events": need,
                     "SINGULAR": str(Fraction(born.get(1, 0), tden)),
                     "INDEFINITE": str(Fraction(born.get(2, 0), tden))})
    return rows


# ===========================================================================
# SECTION 8.  THE DERIVED HEAD
# ===========================================================================

def polarity_word(born, null):
    """the polarity, DERIVED from the two measured masses and never typed."""
    if born > null:
        return "SELECTED"
    if born < null:
        return "AVOIDED"
    return "NEUTRAL"


def outcome_word(reachable, words):
    """THE OUTCOME, derived: no polarity word without a Stage-0 licence, and
    no single polarity word when the declared readings disagree in sign."""
    if not reachable:
        return "SIG-BLOCKED-AT-REACHABILITY"
    ws = sorted(set(words))
    if len(ws) == 1:
        return "SIG-" + ws[0]
    return "SIG-BLOCKED-AT-THE-EMISSION-READING"


def build_verdict(R):
    seg = []
    st = R["static"]
    dy = R["dynamic"]
    seg.append(
        "SIG-STAGE-0-REACHABILITY-[STATIC: THE INDEFINITE REGION IS OCCUPIED "
        "AT R=%d UNRESTRICTED (%s AT %d OF %d SITES), AT R=%d AT A FULL SITE "
        "(%s), AT R=%d IN A COVERING RECORD AND AT R=%d IN A STRUCTURALLY "
        "LIVE ONE -- THE INHERITED #211 FLOOR R=5 IS NECESSARY AND NOT "
        "ATTAINED (%s MULTISETS SCANNED, MINIMUM UNCOVERED %d) | DEPOSIT "
        "THEOREM: %d PER CELL PER ROUND OVER ALL %d PARTITIONS, SPECTRUM %s "
        "| DYNAMIC: THE COUPLED WALK OCCUPIES IT AT %s]@%s"
        % (st["r1"]["R"], st["r1"]["region"], st["r1"]["sites"], NSITE,
           st["fullsite"]["R"], "%d,%d,%d" % tuple(st["fullsite"]["code"]),
           st["covering"]["R"], st["live"]["R"],
           "{:,}".format(st["r5"]["multisets"]), st["r5"]["min_uncovered"],
           st["max_per_cell_per_round"], st["partitions"],
           ",".join("%s:%s" % (k, v)
                    for k, v in sorted(st["incidence_spectrum"].items(),
                                       key=lambda kv: int(kv[0]))),
           " AND ".join("(%s=%s AT R=%d, T=%d)"
                        % (p["arena"], "%d,%d,%d" % tuple(p["record"]),
                           p["R"], p["horizon"])
                        for p in R["clearing"]["pairs"]),
           R["window"]["label"]))
    cl = R["clearing"]
    seg.append(
        "SIG-CLEARING-[%d PAIRS CLEAR AND THE CHEAPEST IS ORDER-RELATIVE "
        "(WINNERS %s); THE UNIQUE PAIR THAT COSTS NO NEW DECLARATION IS "
        "%s = %s = %s AT R=%d, HORIZON %d -- I7'S OWN DECLARED RECORD, "
        "PAPER-21'S DRIVEN ARENA, AT PAPER-20'S OWN DECLARED HORIZON; "
        "INDEFINITE MASS %s AT THE BORN MENU AND %s AT THE RECORD MENU; "
        "SINGULAR FIRST AT T=%d; THE GRAMMAR CANNOT REACH THE REGION BELOW "
        "R=%d AT ALL (LIVE R=%d) AND THE MECHANISM IS THE DEPOSIT THEOREM "
        "THE EMISSION CHANNEL IS FREE OF]"
        % (len(cl["pairs"]),
           ",".join("%s:%s" % (k, v)
                    for k, v in sorted(cl["winners"].items())),
           cl["arena"], "%d,%d,%d" % tuple(cl["record"]),
           cl["declared_name"], cl["R"], cl["horizon"], cl["indefinite_A"],
           cl["indefinite_B"], cl["first_singular"],
           R["static"]["covering"]["R"], R["static"]["live"]["R"]))
    po = R["polarity"]
    seg.append(
        "SIG-POLARITY-[BORN MENU %s: INDEFINITE MASS %s AGAINST %s UNDER THE "
        "UNIFORM-ON-SUPPORT COUNTING MEASURE ON THE SAME TREE, RATIO %s | "
        "RECORD MENU %s: %s AGAINST %s, RATIO %s | BOTH SIGNS ARENA-"
        "INVARIANT ACROSS THE ARENAS THAT CLEAR INSIDE THE HORIZON | THE "
        "STAGE-FROZEN ARM (NO BACK-REACTION, THE RECORD STILL ACCUMULATING) "
        "GIVES %s AND %s | PAPER-20'S FROZEN CONTROL GIVES %s BY THEOREM AT "
        "EVERY HORIZON] -- OBSERVABLES=RECORD-READING(CONSTRAINT B: THE SITE "
        "MARGINAL IS SIGNATURE-BLIND, MEASURED IDENTICAL AT %s AND %s WHILE "
        "THEIR INDEFINITE MASSES ARE %s AND %s)"
        % (po["A"]["word"], po["A"]["born"], po["A"]["null"], po["A"]["ratio"],
           po["B"]["word"], po["B"]["born"], po["B"]["null"], po["B"]["ratio"],
           po["A"]["stage_frozen"], po["B"]["stage_frozen"],
           po["A"]["frozen"], R["mod3"]["pairs"][1]["x"],
           R["mod3"]["pairs"][1]["y"], R["mod3"]["pairs"][1]["indefinite_x"],
           R["mod3"]["pairs"][1]["indefinite_y"]))
    fo = R["forcedness"]
    seg.append(
        "%s-<COIN-FIBER=%s: ALL %d S_3-COVARIANT CLASSES EXACTLY UNITARY, "
        "ALL %d %s AT THE BORN MENU AND ALL %d %s AT THE RECORD MENU -- THE "
        "SIGN IS A FUNCTION OF THE EMISSION READING ALONE AND OF NOTHING "
        "ELSE MEASURED HERE | MOD-3 THEOREM=MACHINE-CHECKED(%d ARENA PAIRS "
        "AT %d BRANCH-WEIGHT MAPS COMPARED PATH BY PATH, IDENTICAL AT %d OF "
        "%d UNDER THE BORN MENU AND AT NONE UNDER THE RECORD MENU: THE BORN "
        "BRANCH MEASURE IS A FUNCTION OF n0 mod 3 WHILE THE SIGNATURE IS A "
        "FUNCTION OF n0, SO THE ABSOLUTE MASSES ARE REPRESENTATIVE-RELATIVE "
        "AND ONLY THE RELATIVE POLARITY CAN BE FORCED) | SCOPE=THIS UNIT "
        "MEASURES A REGION OF RECORD SPACE, NOT A SPACETIME SIGNATURE>"
        % (R["outcome"], fo["verdict"], fo["members"], fo["members"],
           fo["word_A"], fo["members"], fo["word_B"],
           R["mod3"]["checked"], R["mod3"]["maps"], R["mod3"]["identical"],
           R["mod3"]["maps"]))
    return seg


def reconstruct(serialized):
    """the head, DERIVED A SECOND TIME from the serialized receipt by a
    routine that types every template itself and re-derives the outcome word
    from the receipt's own measured rows.  It shares no code path, no input
    object and no typed numeral with the builder."""
    D = json.loads(serialized)
    S, Y = D["static"], D["dynamic"]
    parts = []
    spec = ",".join("%s:%s" % (a, b)
                    for a, b in sorted(S["incidence_spectrum"].items(),
                                       key=lambda kv: int(kv[0])))
    C = D["clearing"]
    parts.append(
        "SIG-STAGE-0-REACHABILITY-[STATIC: THE INDEFINITE REGION IS OCCUPIED "
        "AT R={r1} UNRESTRICTED ({w1} AT {s1} OF {ns} SITES), AT R={r2} AT A "
        "FULL SITE ({c2}), AT R={r3} IN A COVERING RECORD AND AT R={r4} IN A "
        "STRUCTURALLY LIVE ONE -- THE INHERITED #211 FLOOR R=5 IS NECESSARY "
        "AND NOT ATTAINED ({ms} MULTISETS SCANNED, MINIMUM UNCOVERED {mu}) | "
        "DEPOSIT THEOREM: {pc} PER CELL PER ROUND OVER ALL {np} PARTITIONS, "
        "SPECTRUM {sp} | DYNAMIC: THE COUPLED WALK OCCUPIES IT AT "
        "{dy}]@{win}".format(
            r1=S["r1"]["R"], w1=S["r1"]["region"], s1=S["r1"]["sites"],
            ns=len(D["arena"]["sites"]), r2=S["fullsite"]["R"],
            c2=",".join(str(x) for x in S["fullsite"]["code"]),
            r3=S["covering"]["R"], r4=S["live"]["R"],
            ms="{:,}".format(S["r5"]["multisets"]),
            mu=S["r5"]["min_uncovered"], pc=S["max_per_cell_per_round"],
            np=S["partitions"], sp=spec,
            dy=" AND ".join("({a}={rec} AT R={r}, T={t})".format(
                a=p["arena"], rec=",".join(str(x) for x in p["record"]),
                r=p["R"], t=p["horizon"]) for p in C["pairs"]),
            win=D["window"]["label"]))
    parts.append(
        "SIG-CLEARING-[{np} PAIRS CLEAR AND THE CHEAPEST IS ORDER-RELATIVE "
        "(WINNERS {wn}); THE UNIQUE PAIR THAT COSTS NO NEW DECLARATION IS "
        "{a} = {rec} = {nm} AT R={r}, HORIZON {h} -- I7'S OWN DECLARED "
        "RECORD, PAPER-21'S DRIVEN ARENA, AT PAPER-20'S OWN DECLARED "
        "HORIZON; INDEFINITE MASS {ia} AT THE BORN MENU AND {ib} AT THE "
        "RECORD MENU; SINGULAR FIRST AT T={fs}; THE GRAMMAR CANNOT REACH THE "
        "REGION BELOW R={cf} AT ALL (LIVE R={lf}) AND THE MECHANISM IS THE "
        "DEPOSIT THEOREM THE EMISSION CHANNEL IS FREE OF]".format(
            np=len(C["pairs"]),
            wn=",".join("%s:%s" % (k, v)
                        for k, v in sorted(C["winners"].items())),
            a=C["arena"], rec=",".join(str(x) for x in C["record"]),
            nm=C["declared_name"], r=C["R"], h=C["horizon"],
            ia=C["indefinite_A"], ib=C["indefinite_B"],
            fs=C["first_singular"], cf=S["covering"]["R"], lf=S["live"]["R"]))
    P = D["polarity"]
    M = D["mod3"]["pairs"][1]
    parts.append(
        "SIG-POLARITY-[BORN MENU {wa}: INDEFINITE MASS {ba} AGAINST {na} "
        "UNDER THE UNIFORM-ON-SUPPORT COUNTING MEASURE ON THE SAME TREE, "
        "RATIO {ra} | RECORD MENU {wb}: {bb} AGAINST {nb}, RATIO {rb} | BOTH "
        "SIGNS ARENA-INVARIANT ACROSS THE ARENAS THAT CLEAR INSIDE THE "
        "HORIZON | THE STAGE-FROZEN ARM (NO BACK-REACTION, THE RECORD STILL "
        "ACCUMULATING) GIVES {sa} AND {sb} | PAPER-20'S FROZEN CONTROL GIVES "
        "{fr} BY THEOREM AT EVERY HORIZON] -- OBSERVABLES=RECORD-READING"
        "(CONSTRAINT B: THE SITE MARGINAL IS SIGNATURE-BLIND, MEASURED "
        "IDENTICAL AT {mx} AND {my} WHILE THEIR INDEFINITE MASSES ARE {ix} "
        "AND {iy})".format(
            wa=P["A"]["word"], ba=P["A"]["born"], na=P["A"]["null"],
            ra=P["A"]["ratio"], wb=P["B"]["word"], bb=P["B"]["born"],
            nb=P["B"]["null"], rb=P["B"]["ratio"],
            sa=P["A"]["stage_frozen"], sb=P["B"]["stage_frozen"],
            fr=P["A"]["frozen"], mx=M["x"], my=M["y"],
            ix=M["indefinite_x"], iy=M["indefinite_y"]))
    F = D["forcedness"]
    live = bool(C["pairs"])
    signs = {F["word_A"], F["word_B"]}
    if not live:
        word = "SIG-BLOCKED-AT-REACHABILITY"
    elif len(signs) == 1:
        word = "SIG-" + sorted(signs)[0]
    else:
        word = "SIG-BLOCKED-AT-THE-EMISSION-READING"
    parts.append(
        "{ow}-<COIN-FIBER={fv}: ALL {n} S_3-COVARIANT CLASSES EXACTLY "
        "UNITARY, ALL {n} {wa} AT THE BORN MENU AND ALL {n} {wb} AT THE "
        "RECORD MENU -- THE SIGN IS A FUNCTION OF THE EMISSION READING ALONE "
        "AND OF NOTHING ELSE MEASURED HERE | MOD-3 THEOREM=MACHINE-CHECKED"
        "({ck} ARENA PAIRS AT {mp} BRANCH-WEIGHT MAPS COMPARED PATH BY PATH, "
        "IDENTICAL AT {id} OF {mp} UNDER THE BORN MENU AND AT NONE UNDER THE "
        "RECORD MENU: THE BORN BRANCH MEASURE IS A FUNCTION OF n0 mod 3 "
        "WHILE THE SIGNATURE IS A FUNCTION OF n0, SO THE ABSOLUTE MASSES ARE "
        "REPRESENTATIVE-RELATIVE AND ONLY THE RELATIVE POLARITY CAN BE "
        "FORCED) | SCOPE=THIS UNIT MEASURES A REGION OF RECORD SPACE, NOT A "
        "SPACETIME SIGNATURE>".format(
            ow=word, fv=F["verdict"], n=F["members"], wa=F["word_A"],
            wb=F["word_B"], ck=D["mod3"]["checked"], mp=D["mod3"]["maps"],
            id=D["mod3"]["identical"]))
    return parts, word


# ===========================================================================
# SECTION 10.  THE WALLS
# ===========================================================================

def signature_named(code, det4):
    """THE NAMING SENTENCE, mandatory in the paper and DERIVED here from the
    measured code rather than typed: the region is a region of RECORD space."""
    return ("The indefinite region is NAMED AND NOT READ: a site whose "
            "counts are (%d, %d, %d) has 4 det q = %d < 0, which is a sign "
            "of a two-by-two form built from division counts on a nine-site "
            "lattice; it is not a spacetime signature, not a light cone, not "
            "a metric on any continuum, and no Lorentzian, causal, "
            "signature-change or cosmological reading of it is taken here or "
            "licensed by anything measured here."
            % (code[0], code[1], code[2], det4))


# ===========================================================================
# SECTION 11.  PAPER CLAIMS, TABLES, COVERAGE, POLARITY
# ===========================================================================

NUMTOK = re.compile(r"\d[\d,]*(?:/\d[\d,]*)?")
WORDTOK = re.compile(r"[a-z]+")
FENCE = re.compile(r"```(.*?)```", re.S)
HEADNUM = re.compile(r"^#+\s*[\d.]+", re.M)
SECREF = re.compile(r"(paper-\d+|R6a|R6b'|CR-[AB])?\s*§\s*([\d.]+)")
NUMWORDS = ("ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN",
            "EIGHT", "NINE", "TEN", "ELEVEN", "TWELVE")
WORDNUM = dict({w.lower(): i for i, w in enumerate(NUMWORDS)},
               twice=2, thrice=3, twenty=20, hundred=100)
NUMREG = set()


def reg(*vals):
    """every number this run publishes into prose is REGISTERED here, so the
    coverage allow-list is computed and never hand-kept."""
    for v in vals:
        NUMREG.add(str(v))
        if isinstance(v, int):
            NUMREG.add("{:,}".format(v))
    return vals[0] if len(vals) == 1 else vals


NUMERAL_EXEMPTIONS = [
    ("2,3", "the affine plane AG(2,3), named in the parents and in this "
            "paper's arena section; the scanner reads its comma as a "
            "thousands separator"),
    ("256", "the sha256-12 convention in the provenance sentences"),
    ("19", "paper-19, the weld this arena family descends from, named once "
           "in the arena section"),
    ("82", "the CLI-contract engraving, named once in the instrument "
           "section"),
]


def paper_claims(R):
    """every headline sentence, rendered FROM THE RECEIPT and required to
    occur in the paper (RUNBOOK 13: prose renders from the receipt)."""
    S, Y, C, P, F = (R["static"], R["dynamic"], R["clearing"], R["polarity"],
                     R["forcedness"])
    out = [
        ("C-DEPOSIT",
         "A round deposits at most %d incidence on any one cell, measured "
         "exhaustively over all %d partitions, so a cell's count after R "
         "rounds is at most R."
         % (reg(S["max_per_cell_per_round"]), reg(S["partitions"]))),
        ("C-FLOOR",
         "At a site whose three cells are all at least one, SINGULAR needs a "
         "cell at %d and INDEFINITE needs a cell at %d."
         % (reg(S["floor_singular"]["max_cell"]),
            reg(S["floor_indefinite"]["max_cell"]))),
        ("C-R1",
         "One round of the ROW parallel class induces the code (%d, %d, %d) "
         "at every one of the nine sites, with 4 det q = %d: the indefinite "
         "region is occupied at R = %d."
         % (tuple(S["r1"]["code"]) + (reg(S["r1"]["det4"]),
                                      reg(S["r1"]["R"])))),
        ("C-R5",
         "No covering record at R = 5 carries an indefinite site: over all "
         "%s multisets of five rounds that all hit one cell the least number "
         "of uncovered cells is %d."
         % (reg("{:,}".format(S["r5"]["multisets"])),
            reg(S["r5"]["min_uncovered"]))),
        ("C-FULLSITE",
         "The full-site class is attained at R = 5: %s multisets of five "
         "rounds induce the code (%d, %d, %d) at the target site, and the "
         "witness this unit exhibits leaves %d of its 27 cells at zero."
         % (reg("{:,}".format(S["fullsite"]["multisets"])),
            S["fullsite"]["code"][0], S["fullsite"]["code"][1],
            S["fullsite"]["code"][2],
            reg(NCELL - S["fullsite"]["cells_covered"]))),
        ("C-COVERING",
         "The covering floor is R = %d, and the structurally live covering "
         "floor is R = %d."
         % (reg(S["covering"]["R"]), reg(S["live"]["R"]))),
        ("C-CLEARING",
         "The clearing pair is (%s, horizon %d): I7's own declared %s at "
         "R = %d, driven by paper-21, walked at paper-20's own declared "
         "horizon."
         % (C["arena"], reg(C["horizon"]), C["declared_name"], reg(C["R"]))),
        ("C-INDEF-A",
         "At the clearing arena the coupled walk puts exact mass %s on "
         "records with an indefinite site at the Born menu, first positive "
         "at step %d."
         % (reg(C["indefinite_A"]), reg(C["first_indefinite"]))),
        ("C-POLARITY-A",
         "Under the Born menu the indefinite mass is %s against %s under the "
         "uniform-on-support counting measure on the same tree: %s."
         % (reg(P["A"]["born"]), reg(P["A"]["null"]), P["A"]["word"])),
        ("C-POLARITY-B",
         "Under the record menu the indefinite mass is %s against %s: %s."
         % (reg(P["B"]["born"]), reg(P["B"]["null"]), P["B"]["word"])),
        ("C-FIBER",
         "All %d members of the S_3-covariant coin fiber are exactly "
         "unitary, and all %d return %s at the Born menu and %s at the "
         "record menu."
         % (reg(F["members"]), reg(F["members"]), F["word_A"], F["word_B"])),
        ("C-MOD3",
         "The Born branch measure is a function of the record modulo three: "
         "%d arena pairs compared path by path agree at %d of %d "
         "branch-weight maps."
         % (reg(R["mod3"]["checked"]), reg(R["mod3"]["identical"]),
            reg(R["mod3"]["maps"]))),
        ("C-GRAMMAR-GAP",
         "The walk reaches at R = %d and horizon %d a region the grammar "
         "cannot reach below R = %d."
         % (reg(C["R"]), reg(C["horizon"]), reg(S["covering"]["R"]))),
    ]
    return [{"id": i, "claim": c} for i, c in out]


def paper_tables(R):
    """the two load-bearing tables, assembled from this run and required to
    occur in the paper exactly once each (E-22: tables render as claims)."""
    rows = []
    for r in R["static"]["covering_rows"]:
        rows.append("| %d | %s | %s |" % (r["R"], r["pool"],
                                          "YES" if r["exists"] else "NO"))
        reg(r["R"])
    pairs = {p["arena"]: p for p in R["clearing"]["pairs"]}
    for r in R["dynamic"]["floors"]:
        pr = pairs.get(r["arena"])
        last = ("%d at the extension" % pr["horizon"]
                if pr and pr["measured_at_extension"] else str(pr["horizon"]))
        rows.append("| %s | %s | %s | %s | %s | %s |"
                    % (r["arena"], "%d, %d, %d" % tuple(r["record"]), r["R"],
                       r["events_to_indefinite"], r["first_singular"], last))
        reg(r["R"], r["first_singular"], r["events_to_indefinite"],
            pr["horizon"])
    for m in R["forcedness"]["rows"]:
        rows.append("| `%s` | %s | %s | %s | %s |"
                    % (m["coin"], m["born_A"], m["null_A"], m["word_A"],
                       m["word_B"]))
        reg(m["born_A"], m["null_A"])
    return rows


def receipt_numbers(R):
    out = set()

    def walk(o):
        if isinstance(o, bool):
            return
        if isinstance(o, int):
            out.add(str(o))
            out.add("{:,}".format(o))
        elif isinstance(o, str):
            for t in NUMTOK.findall(o):
                out.add(t)
                out.add(t.replace(",", ""))
        elif isinstance(o, dict):
            for k, v in o.items():
                walk(k)
                walk(v)
        elif isinstance(o, (list, tuple)):
            for v in o:
                walk(v)
    for key in ("static", "dynamic", "clearing", "polarity", "forcedness",
                "mod3", "arena", "walk", "window", "provenance", "anchors",
                "counts", "walls", "constraint_b", "prune"):
        if key in R:
            walk(R[key])
    return out


FENCE_COPIES = 2


def paper_coverage(R, text):
    """#20 + E-22: EVERY numeral -- prose, tables, INLINE SPANS and the fenced
    verdict blocks -- allow-listed against exactly three declared lists: this
    run's registered numbers, the receipt it publishes, and a declared
    exemption table published with a reason per literal, each required to
    fire.  The fenced blocks are matched by MULTISET against the declared copy
    count, so forging either copy, deleting one, or appending a third dies."""
    allow = set(NUMREG) | receipt_numbers(R)
    for seg in R["verdict"]["segments"]:
        for t in NUMTOK.findall(seg):
            allow.add(t)
            allow.add(t.replace(",", ""))
    exempt = [list(e) for e in NUMERAL_EXEMPTIONS]
    if mut("MUT-EXEMPTION-DEAD"):
        exempt = exempt + [["4242", "a literal that occurs nowhere"]]
    exempt_lits = {e[0] for e in exempt}
    body = text if not mut("MUT-COVERAGE-SCAN") else FENCE.sub("", text)
    fenced = [t for blk in FENCE.findall(body) for t in NUMTOK.findall(blk)]
    heads = set(HEADNUM.findall(body))
    body = SECREF.sub(" ", HEADNUM.sub("#### ", body))
    scanned, unbacked, fired = 0, [], Counter()
    for tok in NUMTOK.findall(body):
        scanned += 1
        if tok in allow or tok.replace(",", "") in allow:
            continue
        if tok in exempt_lits:
            fired[tok] += 1
            continue
        unbacked.append(tok)
    words, word_unbacked = 0, []
    for wd in WORDTOK.findall(canon(body).lower()):
        if wd not in WORDNUM:
            continue
        words += 1
        if str(WORDNUM[wd]) in allow:
            continue
        if wd in exempt_lits:
            fired[wd] += 1
            continue
        word_unbacked.append(wd)
    if mut("MUT-PAPER-FENCE"):
        seg = R["verdict"]["segments"][0]
        text = text.replace(seg, seg.replace("STATIC", "STAIIC"), 1)
    want = Counter({canon(seg): FENCE_COPIES
                    for seg in R["verdict"]["segments"]})
    got = Counter(canon(b) for b in FENCE.findall(text))
    return {"numerals_scanned": scanned,
            "unbacked": sorted(set(unbacked)),
            "fenced_blocks_scanned": len(FENCE.findall(body)),
            "fenced_numerals_scanned": len(fenced),
            "fenced_unbacked": sorted({t for t in fenced if t not in allow
                                       and t.replace(",", "") not in allow
                                       and t not in exempt_lits}),
            "word_numerals_scanned": words,
            "word_numerals_unbacked": sorted(set(word_unbacked)),
            "section_headings": sorted(heads),
            "registry_size": len(allow),
            "declared_exemptions": [{"literal": e[0], "reason": e[1],
                                     "occurrences": fired[e[0]]}
                                    for e in exempt],
            "exemptions_that_never_fire": sorted(e[0] for e in exempt
                                                 if not fired[e[0]]),
            "fence_copies_declared": FENCE_COPIES,
            "fenced_block_multiset_matches": got == want,
            "fenced_blocks_expected": sum(want.values()),
            "fenced_blocks_found": sum(got.values())}


POLARITY_ROWS = [
    ("PL-REACH", True,
     "the indefinite region is REACHED by the coupled dynamics at the "
     "clearing arena"),
    ("PL-STATIC-R5", False,
     "a covering record with an indefinite site exists at R = 5"),
    ("PL-FORCED-READING", False,
     "the polarity sign is invariant across the declared emission readings"),
    ("PL-FORCED-COIN", True,
     "the polarity sign is invariant across the declared coin fiber"),
    ("PL-FROZEN", False,
     "paper-20's frozen control ever leaves the positive-definite region"),
]


def paper_polarity(R, text):
    """the pre-registered polarity of five load-bearing claims, each measured
    from the receipt and compared against the value declared BEFORE the run."""
    S, C, F = R["static"], R["clearing"], R["forcedness"]
    measured = {
        "PL-REACH": bool(C["first_indefinite"]),
        "PL-STATIC-R5": any(r["exists"] for r in S["covering_rows"]
                            if r["R"] == 5),
        "PL-FORCED-READING": F["word_A"] == F["word_B"],
        "PL-FORCED-COIN": F["verdict"] == "INVARIANT",
        "PL-FROZEN": R["polarity"]["frozen_leaves"],
    }
    if mut("MUT-POLARITY-FLIP"):
        measured["PL-REACH"] = not measured["PL-REACH"]
    rows = [{"id": i, "declared": d, "measured": bool(measured[i]),
             "statement": s, "agrees": bool(measured[i]) == d}
            for i, d, s in POLARITY_ROWS]
    return rows


# ===========================================================================
# SECTION 12.  THE SEAL
# ===========================================================================

SEALED_PATHS = [
    ("SEAL-SCHEMA", "schema", "G-PROVENANCE"),
    ("SEAL-PROVENANCE", "provenance", "G-PROVENANCE"),
    ("SEAL-ANCHORS", "anchors", "G-ANCHORS-READ"),
    ("SEAL-VERBATIM", "verbatim_anchors", "G-VERBATIM"),
    ("SEAL-ARENA", "arena", "G-REGION-ARITHMETIC"),
    ("SEAL-STATIC", "static", "G-STATIC-LADDER-LIVE"),
    ("SEAL-WALK", "walk", "G-WALK-ANCHORED"),
    ("SEAL-DYNAMIC", "dynamic", "G-STAGE0-DYNAMIC"),
    ("SEAL-PRUNE", "prune", "G-PRUNE-SOUND"),
    ("SEAL-CLEARING", "clearing", "G-CLEARING"),
    ("SEAL-POLARITY-CENSUS", "polarity", "G-POLARITY-B"),
    ("SEAL-CONSTRAINT-B", "constraint_b", "G-CONSTRAINT-B"),
    ("SEAL-MOD3", "mod3", "G-MOD3-THEOREM"),
    ("SEAL-FORCEDNESS", "forcedness", "G-FORCEDNESS"),
    ("SEAL-WINDOW", "window", "G-WINDOW-DISCLOSED"),
    ("SEAL-WALLS", "walls", "G-WALL-SIGNATURE-NAMED"),
    ("SEAL-VERDICT", "verdict", "G-VERDICT-RECONSTRUCTED"),
    ("SEAL-OUTCOME", "outcome", "G-VERDICT-RECONSTRUCTED"),
    ("SEAL-COUNTS", "counts", "G-VERDICT-RECONSTRUCTED"),
    ("SEAL-MEMO", "memo", "G-MEMO-LIVE"),
    ("SEAL-PAPER-CLAIMS", "paper_claims", "G-PAPER-CLAIMS"),
    ("SEAL-PAPER-TABLES", "paper_tables", "G-PAPER-TABLES"),
    ("SEAL-PAPER-COVERAGE", "paper_coverage", "G-PAPER-COVERAGE"),
    ("SEAL-POLARITY", "polarity_rows", "G-PAPER-POLARITY"),
    ("SEAL-COVERAGE", "coverage", "G-COVERAGE"),
    ("SEAL-WAIVERS", "waiver_ledger", "G-COVERAGE"),
    ("SEAL-MUTANTS", "mutants", "G-COVERAGE"),
    ("SEAL-MUTANT-SWEEP", "mutant_sweep", "G-SWEEP-BOUND"),
    ("SEAL-REACHABILITY", "reachability", "G-REACHABILITY"),
    ("SEAL-GATES", "gates", "G-PAYLOAD-CLOSES"),
    ("SEAL-CLOSING", "closing_gates", "G-PAYLOAD-CLOSES"),
    ("SEAL-TOTALS", "totals", "G-PAYLOAD-CLOSES"),
    ("SEAL-TRANSCRIPT", "transcript_head", "G-PAYLOAD-CLOSES"),
]
DECLARED_UNSEALED = ["arithmetic", "python", "seal_manifest",
                     "payload_sha256_12"]
DECLARED_UNSEALED_FROZEN = ("arithmetic", "python", "seal_manifest",
                            "payload_sha256_12")
MEASURED_KEYS = ("static", "dynamic", "clearing", "polarity", "forcedness",
                 "mod3", "walk", "prune", "constraint_b", "counts", "verdict")


class Seal:
    def __init__(self):
        self.rows = []
        self.index = {}
        self.payload = None
        self.payload_sha = None

    def take(self, sid, obj):
        path = [p for s, p, _g in SEALED_PATHS if s == sid][0]
        at = [g for s, _p, g in SEALED_PATHS if s == sid][0]
        d = digest(jpath(obj, path))
        if mut("MUT-SEAL-DROP") and sid == "SEAL-COVERAGE":
            return
        self.rows.append({"seal": sid, "path": path, "sealed_at_gate": at,
                          "sha256_12": d})
        self.index[sid] = d

    def verify(self, obj, only=None):
        broken = []
        for row in self.rows:
            if only is not None and row["seal"] not in only:
                continue
            try:
                now = digest(jpath(obj, row["path"]))
            except (KeyError, IndexError, TypeError):
                broken.append(row["seal"])
                continue
            if now != row["sha256_12"]:
                broken.append(row["seal"])
        return broken

    def totality(self):
        have = {r["seal"] for r in self.rows}
        want = {s for s, _p, _g in SEALED_PATHS}
        return sorted(want - have), sorted(have - want)

    def close(self, obj, payload):
        broken = self.verify(obj)
        if broken:
            raise GateFail("G-ARTIFACT-INTEGRITY :: the payload was sealed "
                           "over a broken seal :: %s" % broken)
        self.payload = payload
        self.payload_sha = digest(payload)


# ===========================================================================
# SECTION 13.  THE GATE REGISTRY, THE FALSIFIERS AND THE WAIVERS
# ===========================================================================

GATE_REGISTRY = [
    "G-PROVENANCE", "G-ANCHORS-READ", "G-VERBATIM", "G-ANCHOR-CONSUMERS",
    "G-NO-FLOAT", "G-NO-SUBPROCESS", "G-READS-DECLARED", "G-FALSIFIER-HONEST",
    "G-REGION-ARITHMETIC", "G-DEPOSIT-THEOREM", "G-CELL-TRANSITIVE",
    "G-COLLINEAR-LADDER", "G-STATIC-FLOOR", "G-STATIC-LADDER",
    "G-STATIC-LADDER-LIVE", "G-WALK-STOCHASTIC", "G-WALK-ANCHORED",
    "G-COIN-FAMILY", "G-STAGE0-DYNAMIC", "G-PRUNE-SOUND", "G-CLEARING",
    "G-NULL-MEASURE", "G-POLARITY-A", "G-POLARITY-B", "G-CONSTRAINT-B",
    "G-MOD3-THEOREM", "G-FORCEDNESS", "G-MEMO-LIVE", "G-WINDOW-DISCLOSED",
    "G-WALL-L1", "G-WALL-BHS", "G-WALL-KR", "G-WALL-SIGNATURE-NAMED",
    "G-VERDICT-RECONSTRUCTED", "G-PAPER-CLAIMS", "G-PAPER-TABLES",
    "G-PAPER-COVERAGE", "G-PAPER-POLARITY", "G-COVERAGE", "G-SWEEP-BOUND",
    "G-REACHABILITY", "G-MUTANTS-ON-TARGET", "G-PAYLOAD-CLOSES",
    "G-SEAL-COMPLETE", "G-ARTIFACT-INTEGRITY",
]
LATE_GATES = ("G-COVERAGE", "G-SWEEP-BOUND", "G-ANCHOR-CONSUMERS",
              "G-REACHABILITY", "G-PAYLOAD-CLOSES", "G-READS-DECLARED",
              "G-SEAL-COMPLETE", "G-ARTIFACT-INTEGRITY")
# the three gates that exist only where an object under test does; a run
# without one (--numbers, --selftest, --break-anchor) declares them here
# rather than dropping them from the coverage denominator
PAPER_GATES = ("G-PAPER-CLAIMS", "G-PAPER-TABLES", "G-PAPER-COVERAGE")
CLOSING_LEDGER_GATES = ("G-SEAL-COMPLETE",)
SWEEP_GATE = "G-MUTANTS-ON-TARGET"

# EVERY ROW CARRIES THE OBJECT IT CORRUPTS (E-23).  The fourth field names,
# as it appears in the code, the object the hook moves, and the gate below
# requires that name to occur in the hook's own source.
MUTANTS = [
    ("MUT-ANCHOR-VALUE", "G-ANCHORS-READ",
     "moves one path-value anchor's expected value away from the bytes it "
     "anchors", "want"),
    ("MUT-VERBATIM", "G-VERBATIM",
     "perturbs one verbatim needle at a content-bearing token", "needle"),
    ("MUT-CONSUMER-BINDING", "G-ANCHOR-CONSUMERS",
     "points one verbatim anchor's consumer at a gate that does not exist",
     "vcons"),
    ("MUT-FALSIFIER-DESC", "G-FALSIFIER-HONEST",
     "points one falsifier's declared corrupted object at an object its code "
     "does not touch", "mrows[0][corrupts]"),
    ("MUT-HERON", "G-REGION-ARITHMETIC",
     "corrupts the symmetric route's determinant so the two routes disagree",
     "d4"),
    ("MUT-SPECTRUM", "G-DEPOSIT-THEOREM",
     "moves one entry of the recomputed incidence spectrum", "spec"),
    ("MUT-DEPOSIT-MAX", "G-DEPOSIT-THEOREM",
     "lowers the measured maximum deposit per cell per round", "percell"),
    ("MUT-TRANSITIVE", "G-CELL-TRANSITIVE",
     "shrinks the measured cell orbit so the single-cell census loses its "
     "licence", "orbit"),
    ("MUT-COLLINEAR", "G-COLLINEAR-LADDER",
     "corrupts one rung of the collinear ladder's induced record", "ladder"),
    ("MUT-FLOOR", "G-STATIC-FLOOR",
     "moves the measured indefinite floor's maximum cell", "fi"),
    ("MUT-R5", "G-STATIC-LADDER",
     "reports the R = 5 covering scan as fully covered", "mu"),
    ("MUT-R6LIVE", "G-STATIC-LADDER-LIVE",
     "asserts a structurally live covering witness where the search found "
     "none", "rows"),
    ("MUT-WALK-ANCHOR", "G-WALK-ANCHORED",
     "moves the rebuilt walk's exit probability away from paper-20's "
     "committed row", "exitA"),
    ("MUT-WALK-BRANCH", "G-WALK-ANCHORED",
     "moves the rebuilt walk's branch count at the anchored horizon",
     "branches"),
    ("MUT-COIN", "G-COIN-FAMILY",
     "breaks one coin of the declared fiber so it is no longer unitary",
     "M"),
    ("MUT-FIRST-INDEF", "G-STAGE0-DYNAMIC",
     "moves the first horizon at which the indefinite region is occupied",
     "floors"),
    ("MUT-PRUNE", "G-PRUNE-SOUND",
     "zeroes the pruned engine's extension row so the horizon floor moves",
     "ext"),
    ("MUT-CLEARING", "G-CLEARING",
     "selects a clearing arena whose indefinite mass is zero", "chosen"),
    ("MUT-NULL", "G-NULL-MEASURE",
     "corrupts the uniform-on-support measure's total mass", "ntot"),
    ("MUT-POLARITY-A", "G-POLARITY-A",
     "swaps the Born-menu polarity word for its opposite", "word"),
    ("MUT-POLARITY-B", "G-POLARITY-B",
     "moves the record-menu indefinite mass so its ratio inverts", "born"),
    ("MUT-CONSTRAINT-B", "G-CONSTRAINT-B",
     "declares a site-marginal observable as the polarity's carrier",
     "carrier"),
    ("MUT-MOD3", "G-MOD3-THEOREM",
     "corrupts one residue partner's branch-weight map", "my"),
    ("MUT-FORCEDNESS", "G-FORCEDNESS",
     "reports the coin fiber as invariant while one member disagrees",
     "frows"),
    ("MUT-MEMO", "G-MEMO-LIVE",
     "keys the memo on a label instead of on its complete input", "k"),
    ("MUT-WINDOW", "G-WINDOW-DISCLOSED",
     "drops the declared window from the head's own arena string", "label"),
    ("MUT-WALL-L1", "G-WALL-L1",
     "moves the object under test to a copy carrying the retracted L-1 "
     "sentence", "ptext"),
    ("MUT-WALL-NAMED", "G-WALL-SIGNATURE-NAMED",
     "deletes the mandatory naming sentence from the object under test",
     "ptext"),
    ("MUT-WALL-BHS", "G-WALL-BHS",
     "writes a sprinkling-grade reading into the declared measurement "
     "surface", "surface"),
    ("MUT-WALL-KR", "G-WALL-KR",
     "writes a dimension reading into the declared measurement surface",
     "surface"),
    ("MUT-VERDICT", "G-VERDICT-RECONSTRUCTED",
     "forges the outcome word in the builder's own segment", "segs"),
    ("MUT-PAPER-CLAIM", "G-PAPER-CLAIMS",
     "corrupts one rendered claim so it no longer occurs in the paper",
     "claims"),
    ("MUT-PAPER-TABLE", "G-PAPER-TABLES",
     "forges one rendered table row", "trows"),
    ("MUT-COVERAGE-SCAN", "G-PAPER-COVERAGE",
     "strips the fenced blocks from the coverage scan", "body"),
    ("MUT-EXEMPTION-DEAD", "G-PAPER-COVERAGE",
     "adds a declared exemption that fires nowhere", "exempt"),
    ("MUT-PAPER-FENCE", "G-PAPER-COVERAGE",
     "forges one copy of a fenced verdict block", "text"),
    ("MUT-POLARITY-FLIP", "G-PAPER-POLARITY",
     "inverts one pre-registered claim's measured polarity", "measured"),
    ("MUT-SEAL-DROP", "G-SEAL-COMPLETE",
     "drops one seal row so the manifest is no longer total", "sid"),
]
MUTANT_NAMES = [m[0] for m in MUTANTS]


def waiver_ledger():
    """every gate with no declared falsifier carries a machine-readable
    forcing that says why it cannot fail."""
    return {
        "G-PROVENANCE": ("ANCHORED",
                         "--break-anchor NAME corrupts any source's expected "
                         "digest and the run dies here; the mode is part of "
                         "the CLI contract and the self-test exercises it"),
        "G-READS-DECLARED": ("STRUCTURAL",
                             "the read categories are a closed tuple and an "
                             "undeclared category raises inside the reader "
                             "itself, before any gate"),
        "G-NO-FLOAT": ("ANALYTIC",
                       "an AST scan of this file for float literals and true "
                       "division; a violation is a source-level fact, not a "
                       "value this run can move"),
        "G-NO-SUBPROCESS": ("ANALYTIC",
                            "an import and attribute scan; the same class"),
        "G-WALK-STOCHASTIC": ("ANALYTIC",
                              "the emission weights are the branch's own "
                              "post-coin Born weights over their own sum, so "
                              "the check raises inside the walk itself"),
        "G-COVERAGE": ("LEDGER",
                       "the coverage ledger's own denominator is this run's "
                       "gate set; MUT-SEAL-DROP and every other mutant pass "
                       "through it"),
        "G-SWEEP-BOUND": ("LEDGER",
                          "a mutant sub-run declares itself un-swept and is "
                          "held to that; the delivery run's conjunction is "
                          "re-taken at G-ARTIFACT-INTEGRITY"),
        "G-REACHABILITY": ("LEDGER",
                           "every declared falsifier's gate is required to "
                           "be in this run's own evaluated ledger"),
        "G-MUTANTS-ON-TARGET": ("SWEEP",
                                "this gate IS the sweep; a mutant cannot "
                                "target the instrument that runs it"),
        "G-PAYLOAD-CLOSES": ("LEDGER",
                             "a conjunction over the gate ledger and a "
                             "recursive type scan; any mutant that fails "
                             "earlier never reaches it"),
        "G-ARTIFACT-INTEGRITY": ("TERMINAL",
                                 "a mutant sub-run returns before the write; "
                                 "the gate corrupts a written byte on a "
                                 "read-back copy and shows the corruption "
                                 "detected before it passes"),
    }


def template_constants(tree, name):
    """the TEMPLATE TEXT a routine types: its string constants less its
    docstring, less the receipt keys it looks values up by, and less the
    separators and format specs it calls methods on.  What remains is exactly
    the text that reaches the head."""
    fn = [n for n in ast.walk(tree)
          if isinstance(n, ast.FunctionDef) and n.name == name][0]
    doc = ast.get_docstring(fn, clean=False)
    skip = set()
    for n in ast.walk(fn):
        if isinstance(n, ast.Subscript) and isinstance(n.slice, ast.Constant):
            skip.add(id(n.slice))
        if isinstance(n, ast.Attribute) and isinstance(n.value, ast.Constant):
            skip.add(id(n.value))
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute):
            for a in list(n.args) + [k.value for k in n.keywords]:
                if isinstance(a, ast.Constant):
                    skip.add(id(a))
    return {c.value for c in ast.walk(fn)
            if isinstance(c, ast.Constant) and isinstance(c.value, str)
            and c.value != doc and id(c) not in skip}


def mutant_hooks(src):
    """E-23: every falsifier's HOOK, located by AST, with the source of the
    statement that carries it published in the receipt."""
    tree = ast.parse(src)
    lines = src.split("\n")
    stmts = [n for n in ast.walk(tree) if isinstance(n, ast.stmt)]
    out = {}
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        f = node.func
        if not (isinstance(f, ast.Name) and f.id in ("pick", "mut")):
            continue
        if not node.args or not isinstance(node.args[0], ast.Constant):
            continue
        best = None
        for s in stmts:
            if s.lineno <= node.lineno <= (s.end_lineno or s.lineno):
                if best is None or (s.end_lineno - s.lineno
                                    < best.end_lineno - best.lineno):
                    best = s
        text = "\n".join(lines[best.lineno - 1:best.end_lineno])
        const = (f.id == "pick" and len(node.args) > 2
                 and isinstance(node.args[1], ast.Constant)
                 and isinstance(node.args[1].value, bool))
        out.setdefault(node.args[0].value, []).append(
            {"kind": f.id, "line": node.lineno, "source": norm_src(text),
             "constant_boolean": const})
    return out


# ===========================================================================
# SECTION 14.  THE RUN
# ===========================================================================

def source_text(texts, sid):
    return texts[sid]


def full_run(break_anchor=None, paper_text=None, paper_rel=PAPER_REL,
             do_paper=True):
    LD, SEAL, R = Ledger(), Seal(), {}
    R["schema"] = SCHEMA
    say("\n[SEC 1] PROVENANCE -- %d pinned sources" % len(SOURCES))
    texts, prov = {}, []
    for sid, rel, want, why in SOURCES:
        raw = read_bytes(rel)
        got = hashlib.sha256(raw).hexdigest()[:12]
        exp = "0" * 12 if sid == break_anchor else want
        prov.append({"id": sid, "path": rel, "expected": exp, "found": got,
                     "matches": got == exp, "why": why})
        texts[sid] = raw.decode("utf-8")
    bad = [p["id"] for p in prov if not p["matches"]]
    R["provenance"] = prov
    LD.gate("G-PROVENANCE",
            "EVERY SOURCE IS READ AT ITS PINNED sha256-12 (#46/#62/#91).  "
            "%d files enter this run as SOURCES, each hash-verified against "
            "this unit's own frozen declaration before a single byte of it "
            "is used; --break-anchor corrupts any one of them and the run "
            "dies here" % len(SOURCES),
            not bad, "sources %d, mismatched %s" % (len(SOURCES),
                                                    bad or "none"))
    SEAL.take("SEAL-SCHEMA", R)
    SEAL.take("SEAL-PROVENANCE", R)

    # ---- path-value anchors (#62: the PAIR, not the bytes) ---------------
    arows = []
    for aid, sid, path, want, why in PATH_ROWS:
        obj = json.loads(texts[sid])
        cur = obj
        for part in path:
            cur = cur[part]
        if mut("MUT-ANCHOR-VALUE") and aid == "P-P20-THIRD":
            want = want + 1
        arows.append({"id": aid, "source": sid,
                      "path": "/".join(str(p) for p in path),
                      "expected": want, "found": cur, "matches": cur == want,
                      "why": why})
    R["anchors"] = arows
    abad = [a["id"] for a in arows if not a["matches"]]
    LD.gate("G-ANCHORS-READ",
            "THE PATH-VALUE ANCHORS BIND THE PAIR, NOT THE BYTES (#62).  %d "
            "rows name a source, a path INTO that source and the value that "
            "must stand there; a path drift that leaves the file's hash "
            "intact but moves the arena or a parent's committed number dies "
            "here" % len(arows),
            not abad, "anchors %d, mismatched %s" % (len(arows),
                                                     abad or "none"))
    SEAL.take("SEAL-ANCHORS", R)

    # ---- verbatim anchors (#62 as amended: QUOTE FIDELITY) ---------------
    vrows = []
    for vid, sid, needle, gname in VERBATIM:
        nd = needle
        if mut("MUT-VERBATIM") and vid == "V-P21-BUDGET":
            nd = needle.replace("9", "8")
        ok = match_needle(source_text(texts, sid), nd)
        vrows.append({"id": vid, "source": sid, "needle": nd,
                      "canon_len": len(canon(nd)), "found": ok,
                      "consumer_gate": gname})
    R["verbatim_anchors"] = vrows
    vbad = [v["id"] for v in vrows if not v["found"]]
    LD.gate("G-VERBATIM",
            "QUOTE FIDELITY (#62 as amended at v14 #62).  %d quotations are "
            "matched against their source's COMMITTED BYTES under the #125 "
            "normalisation -- markdown prefixes stripped, ASCII folded, "
            "whitespace collapsed, and compared whitespace-stripped as well "
            "-- each clearing the %d-character floor and each naming the "
            "gate that consumes it" % (len(vrows), NEEDLE_FLOOR),
            not vbad, "anchors %d, not found %s" % (len(vrows),
                                                    vbad or "none"))
    SEAL.take("SEAL-VERBATIM", R)

    # ---- the file's own arithmetic and read discipline -------------------
    src = read_text(SELF, "SELF")
    tree = ast.parse(src)
    floats = [n.lineno for n in ast.walk(tree)
              if isinstance(n, ast.Constant) and isinstance(n.value, float)]
    divs = [n.lineno for n in ast.walk(tree)
            if isinstance(n, ast.BinOp) and isinstance(n.op, ast.Div)]
    LD.gate("G-NO-FLOAT",
            "EXACT ARITHMETIC, AS A SOURCE-LEVEL FACT.  An AST scan of this "
            "file finds no float literal and no true division: every number "
            "this run computes is a Python int, a Fraction, or an element of "
            "Z[w] carried as an integer pair",
            not floats and not divs,
            "float literals %s, true divisions %s" % (floats or "none",
                                                      divs or "none"))
    mods = set()
    for n in ast.walk(tree):
        if isinstance(n, ast.Import):
            mods |= {a.name.split(".")[0] for a in n.names}
        elif isinstance(n, ast.ImportFrom) and n.module:
            mods.add(n.module.split(".")[0])
        elif isinstance(n, ast.Attribute):
            mods.add(n.attr)
    LD.gate("G-NO-SUBPROCESS",
            "NO SUBPROCESS OF ANY KIND (#91 off-tree and git-less).  The "
            "import and attribute sets are scanned: no subprocess, no "
            "shutil, no socket, no urllib.  This is also why the GDL "
            "delivery is CITED from a frozen quotation carrying its commit "
            "%s rather than read: its working-tree copy is held dirty by a "
            "concurrent sibling and a committed-sha read would need one"
            % GDL_COMMIT,
            not (mods & {"subprocess", "shutil", "socket", "urllib",
                         "multiprocessing", "requests"}),
            "forbidden imports %s"
            % (sorted(mods & {"subprocess", "shutil", "socket", "urllib",
                              "multiprocessing", "requests"}) or "none"))

    # ---- E-23: the falsifier surface, verified against its own code ------
    hooks = mutant_hooks(src)
    mrows = [{"name": m[0], "gate": m[1], "what": m[2], "corrupts": m[3]}
             for m in MUTANTS]
    mrows[0]["corrupts"] = pick("MUT-FALSIFIER-DESC", mrows[0]["corrupts"],
                                "NO-SUCH-OBJECT-IN-THIS-FILE")
    for r in mrows:
        hs = hooks.get(r["name"], [])
        r["hook_lines"] = [h["line"] for h in hs]
        r["hook_source"] = hs[0]["source"] if hs else None
        r["constant_boolean_falsifier"] = any(h["constant_boolean"]
                                              for h in hs)
        want = norm_src(r["corrupts"]).replace("[", "").replace("]", "")
        r["description_matches_code"] = bool(hs) and any(
            want in h["source"].replace("[", "").replace("]", "")
            .replace('"', "").replace("'", "") for h in hs)
    R["mutants"] = mrows
    unhooked = [r["name"] for r in mrows if not r["hook_lines"]]
    const_bool = [r["name"] for r in mrows if r["constant_boolean_falsifier"]]
    desc_bad = [r["name"] for r in mrows if not r["description_matches_code"]]
    LD.gate("G-FALSIFIER-HONEST",
            "E-23: A FALSIFIER'S PUBLISHED DESCRIPTION IS PART OF THE SEALED "
            "SURFACE.  Each of the %d declared falsifiers names the OBJECT "
            "it corrupts; this gate locates every hook by AST, publishes the "
            "source of the statement carrying it, requires the named object "
            "to occur there, and REJECTS any falsifier whose corruption is a "
            "constant boolean" % len(mrows),
            not unhooked and not const_bool and not desc_bad,
            "falsifiers %d, unhooked %s, constant-boolean %s, description "
            "unmatched %s" % (len(mrows), unhooked or "none",
                              const_bool or "none", desc_bad or "none"))

    # ---- the arena, from I7's own receipt --------------------------------
    i7 = json.loads(texts["A-I7"])
    links = tuple(tuple(v) for v in i7["declarations"]["links_d2"])
    fam = i7["declarations"]["records_d2"]
    box = 12
    dis = []
    for a in range(box + 1):
        for b in range(box + 1):
            for c in range(box + 1):
                q11, q22, q12, det = q_of((a, b, c))
                d4 = det4_of(a, b, c)
                if mut("MUT-HERON") and (a, b, c) == (1, 1, 5):
                    d4 = -d4
                if Fraction(d4, 4) != det:
                    dis.append((a, b, c))
    R["arena"] = {"sites": [list(s) for s in SITES],
                  "links": [list(v) for v in links],
                  "cells": NCELL,
                  "declared_records": fam,
                  "readout": "q11 = n_1, q22 = n_2, q12 = (n_3 - n_1 - n_2)/2",
                  "region_names": list(REGION_NAMES),
                  "code_box": box,
                  "codes_checked": (box + 1) ** 3,
                  "route_disagreements": len(dis),
                  "declared_region": {k: REGION_NAMES[region_of(tuple(v))]
                                      for k, v in sorted(fam.items())}}
    LD.gate("G-REGION-ARITHMETIC",
            "THE REGION TRICHOTOMY, BY TWO ROUTES THAT SHARE NO EXPRESSION.  "
            "Route 1 is I7's readout as written, in exact Fractions; route 2 "
            "is the symmetric integer form 2(n1n2+n1n3+n2n3) - (n1^2+n2^2+"
            "n3^2), which is 4 det q.  All %d codes of the declared box are "
            "compared entry by entry, and I7's own criterion -- nonsingular "
            "and positive definite by the exact Sylvester test -- names the "
            "three regions" % ((box + 1) ** 3),
            not dis, "codes %d, disagreements %d, declared records by region "
            "%s" % ((box + 1) ** 3, len(dis),
                    R["arena"]["declared_region"]))
    SEAL.take("SEAL-ARENA", R)

    # ---- the memo's own liveness probe (RUNBOOK 14 addendum) -------------
    p1 = memo("probe", ("alpha",), lambda: 1)
    p2 = memo("probe", ("beta",), lambda: 2)
    p3 = memo("probe", ("alpha",), lambda: 3)
    R["memo"] = {"probe_distinct": p1 != p2, "probe_hit": p3 == p1,
                 "kinds": sorted(set(list(MEMO_HITS) + list(MEMO_MISSES)))}
    LD.gate("G-MEMO-LIVE",
            "THE INPUT MEMO IS KEYED ON ITS COMPLETE INPUT, NOT ON A LABEL "
            "(RUNBOOK 14 addendum, v13 #185).  Two probes with DIFFERENT "
            "keys must return different values and a third with a repeated "
            "key must return the first one's: a memo keyed on a label "
            "collapses them and dies here, before any measurement depends "
            "on it.  Every walk and every census below is keyed on its "
            "complete input tuple, so a falsifier that moves an input MISSES "
            "the cache and recomputes",
            p1 != p2 and p3 == p1,
            "probe values %s %s %s, distinct %s, repeat hit %s"
            % (p1, p2, p3, p1 != p2, p3 == p1))
    SEAL.take("SEAL-MEMO", R)

    # ---- STAGE 0A: THE STATIC CENSUS -------------------------------------
    say("\n[SEC 2] STAGE 0A -- THE STATIC CENSUS")
    ST = dict(memo("static", (links,), lambda: static_census(links)))
    spec = dict(ST["incidence_spectrum"])
    if mut("MUT-SPECTRUM"):
        spec[9] = spec[9] + 1
    percell = pick("MUT-DEPOSIT-MAX", ST["max_per_cell_per_round"], 0)
    want_spec = [a["expected"] for a in arows if a["id"] == "P-P21-SPECTRUM"][0]
    spec_ok = {str(k): v for k, v in spec.items()} == want_spec
    LD.gate("G-DEPOSIT-THEOREM",
            "THE DEPOSIT THEOREM, EXHAUSTIVE OVER ALL %d PARTITIONS: a round "
            "deposits AT MOST ONE incidence on any one cell and at most two "
            "on any one site, so after R rounds every cell count is at most "
            "R.  The recomputed incidence spectrum is compared cell for cell "
            "against paper-21's committed row, which is where this unit's "
            "arithmetic meets its parent's" % ST["partitions"],
            percell == 1 and ST["max_per_site_per_round"] == 2 and spec_ok,
            "max per cell %s, max per site %d, spectrum %s, matches "
            "paper-21's committed row %s"
            % (percell, ST["max_per_site_per_round"], sorted(spec.items()),
               spec_ok))
    orbit = pick("MUT-TRANSITIVE", ST["cell_orbit"], 9)
    LD.gate("G-CELL-TRANSITIVE",
            "THE SINGLE-CELL CENSUSES ARE LICENSED BY A MEASURED SYMMETRY.  "
            "The %d linear maps of AG(2,3) that preserve the declared link "
            "SET, together with the nine translations, act on the 27 cells "
            "with a single orbit; every census below that fixes one cell is "
            "therefore a statement about all of them, and a shrunken orbit "
            "removes the licence here rather than silently downstream"
            % ST["linear_maps"],
            orbit == NCELL, "linear maps %d, orbit %s of %d"
            % (ST["linear_maps"], orbit, NCELL))
    ladder = [dict(x) for x in ST["collinear_ladder"]]
    if mut("MUT-COLLINEAR"):
        ladder[1]["homogeneous"] = False
    lad_ok = all(x["homogeneous"] and x["covering"] and x["foreign"] == 0
                 and x["R"] == sum(x["record"]) for x in ladder)
    named = {tuple(v): k for k, v in fam.items()}
    LD.gate("G-COLLINEAR-LADDER",
            "THE ARENA LADDER IS CONSTRUCTED, NOT ASSUMED.  ROW^a COL^b "
            "DIA^c induces the homogeneous record (a, b, c) at R = a+b+c, "
            "covering and foreign-pair-free at every rung; the rungs carry "
            "I7's own G-FLAT at R = 4, G-SINGULAR at R = 6 and G-INDEF at "
            "R = 8, and each rung's region is read by the criterion of the "
            "gate above",
            lad_ok, "rungs %s"
            % [(x["record"], x["R"], x["region"],
                named.get(tuple(x["record"]), "-")) for x in ladder])
    fi = dict(ST["floor_indefinite"])
    if mut("MUT-FLOOR"):
        fi["max_cell"] = fi["max_cell"] - 1
    LD.gate("G-STATIC-FLOOR",
            "THE FLOOR THEOREM.  At a site whose three cells are all at "
            "least one, the cheapest SINGULAR code has a cell at %d and the "
            "cheapest INDEFINITE code has a cell at %d -- measured over the "
            "whole declared box.  With the deposit theorem this is a BUDGET "
            "floor: a covered indefinite site needs R >= 5.  That floor is "
            "NECESSARY; whether it is ATTAINED is the next gate's question "
            "and the answer is no"
            % (ST["floor_singular"]["max_cell"],
               ST["floor_indefinite"]["max_cell"]),
            fi["max_cell"] == 5 and ST["floor_singular"]["max_cell"] == 4,
            "singular floor %s at code %s, indefinite floor %s at code %s"
            % (ST["floor_singular"]["max_cell"], ST["floor_singular"]["code"],
               fi["max_cell"], fi["code"]))
    mu = pick("MUT-R5", ST["r5_min_uncovered"], 0)
    rows = [dict(x) for x in ST["covering_rows"]]
    r5 = [x for x in rows if x["R"] == 5 and x["pool"] == "ALL"][0]
    r5["exists"] = mu == 0
    cov_floor = min(x["R"] for x in rows if x["exists"] and x["pool"] == "ALL")
    LD.gate("G-STATIC-LADDER",
            "THE INHERITED FLOOR IS NECESSARY AND NOT ATTAINED.  At R = 5 an "
            "indefinite site needs a cell at 5, so ALL FIVE rounds must hit "
            "that one cell; over every one of the %s such multisets the "
            "least number of cells left uncovered is %s.  A covering record "
            "with an indefinite site therefore first exists at R = %d, not "
            "at 5 -- and paper-21's own block-quantisation row is the R = 4 "
            "end of the same fact" % ("{:,}".format(ST["r5_multisets"]),
                                      mu, cov_floor),
            mu > 0 and cov_floor == 6,
            "pool %d partitions, multisets %d, min uncovered %s, covering "
            "floor R = %d, rows %s"
            % (ST["r5_pool"], ST["r5_multisets"], mu, cov_floor,
               [(x["R"], x["pool"], x["exists"]) for x in rows]))
    if mut("MUT-R6LIVE"):
        rows = [dict(x, exists=True) if (x["R"] == 6 and x["pool"] == "LIVE")
                else x for x in rows]
    live_floor = min(x["R"] for x in rows if x["exists"]
                     and x["pool"] == "LIVE")
    ST["covering"] = {"R": cov_floor}
    ST["live"] = {"R": live_floor}
    ST["r5"] = {"min_uncovered": mu, "multisets": ST["r5_multisets"],
                "pool": ST["r5_pool"]}
    ST["r1"] = {"R": ST["r1_rounds"], "code": ST["r1_codes"][0],
                "det4": det4_of(*ST["r1_codes"][0]),
                "region": REGION_NAMES[region_of(tuple(ST["r1_codes"][0]))],
                "sites": NSITE}
    ST["fullsite"] = {"R": fi["max_cell"], "code": ST["fullsite_r5_code"],
                      "multisets": ST["fullsite_r5_multisets"],
                      "cells_covered": ST["fullsite_r5_cells_covered"]}
    ST["covering_rows"] = rows
    ST["collinear_ladder"] = ladder
    R["static"] = ST
    LD.gate("G-STATIC-LADDER-LIVE",
            "THE STRUCTURALLY LIVE FLOOR IS ONE ROUND DEARER STILL.  "
            "Restricted to the %d saturating (foreign-pair-free) partitions "
            "-- paper-21's own structurally live class -- no covering record "
            "carries an indefinite site at R = 6 either; the live floor is "
            "R = %d, where the collinear arrangement ROW COL DIA^5 induces "
            "the homogeneous (1, 1, 5).  I7's own declared G-INDEF costs "
            "R = 8" % (ST["saturating"], live_floor),
            live_floor == 7 and ST["saturating_foreign_free"]
            == ST["saturating"],
            "live floor R = %d, saturating partitions %d all foreign-free "
            "%s, live rows %s"
            % (live_floor, ST["saturating"],
               ST["saturating_foreign_free"] == ST["saturating"],
               [(x["R"], x["exists"]) for x in rows if x["pool"] == "LIVE"]))
    SEAL.take("SEAL-STATIC", R)
    cl, floors, crows, a3A = continue_run(LD, SEAL, R, texts, links, ST, fam,
                                          paper_text, paper_rel, do_paper)
    stages23(LD, SEAL, R, texts, links, ST, fam, cl, floors, crows, a3A,
             paper_text, paper_rel, do_paper)
    return LD, SEAL, R


def coin_by_name(nm):
    row = [c for c in COIN_FIBER if c[0] == nm][0]
    return coin_matrix(row[1], row[2])


def site_marginal(frontier, T):
    """the ENSEMBLE SITE DISTRIBUTION at the final step: sum over branches of
    the branch weight times the branch's own site mass.  This is the
    site-marginal object the GDL blindness theorem is about, computed here so
    that constraint B can be MEASURED rather than declared."""
    out = [Fraction(0)] * NSITE
    den = 9 ** T
    for (psi, _nph, _n, w, _dn, _pa) in frontier:
        for s in range(NSITE):
            b = s * 3
            m = absq(psi[b]) + absq(psi[b + 1]) + absq(psi[b + 2])
            if m:
                out[s] += w * Fraction(m, den)
    return [str(x) for x in out]


def arm_stats(T, c, links, reading, coin_name, feedback, update):
    """ONE ARM, digested.  Only the aggregates are returned, so the memo holds
    kilobytes rather than the branch tree."""
    res = run_arm(T, arena_field(c), links, reading, coin_by_name(coin_name),
                  feedback, update)
    rows, census, leaves_out = region_profile(res["levels"], T, reading)
    return {"rows": rows, "census": census, "leaves_out": leaves_out,
            "checks": res["checks"], "visits": res["visits"],
            "marginal": site_marginal(res["levels"][T - 1], T),
            "branches": [len(l) for l in res["levels"]]}


def arm(T, c, links, reading="A", coin_name="GROVER", feedback=True,
        update=True):
    key = (T, c, links, reading, coin_name, feedback, update)
    return memo("arm", key,
                lambda: arm_stats(T, c, links, reading, coin_name, feedback,
                                  update))


def path_map(T, c, links, reading):
    """the branch measure AS A MAP from emission path to exact weight -- the
    object the mod-3 theorem is about.  Two arenas whose records agree modulo
    three must produce the SAME map under the Born menu."""
    def build():
        res = run_arm(T, arena_field(c), links, reading, GROVER_Z, True, True,
                      paths=True)
        return [{p: str(w) for (_ps, _nph, _n, w, _dn, p) in lvl}
                for lvl in res["levels"]]
    return memo("paths", (T, c, links, reading), build)


def continue_run(LD, SEAL, R, texts, links, ST, fam, paper_text, paper_rel,
                 do_paper):
    """STAGE 0B onward: the walk, the dynamic census, the clearing, the
    polarity census, the forcedness census, the walls and the verdict."""
    say("\n[SEC 3] THE WALK, REBUILT AND ANCHORED")
    A3 = arena_of("A3")[1]
    a3A = arm(HORIZON, A3, links, "A")
    a3B = arm(HORIZON, A3, links, "B")
    exitA = str(Fraction(1) - massof(a3A["rows"][-1], "born", "POSDEF"))
    exitB = str(Fraction(1) - massof(a3B["rows"][-1], "born", "POSDEF"))
    branches = a3A["branches"][-1]
    if mut("MUT-WALK-ANCHOR"):
        exitA = str(Fraction(exitA) * Fraction(1, 2))
    if mut("MUT-WALK-BRANCH"):
        branches = branches + 1
    anch = {a["id"]: a["found"] for a in R["anchors"]}
    third = min(v[2] for v in a3A["visits"].values() if len(v) > 2)
    cen = {k.split("|")[0]: v for k, v in a3A["census"].items()}
    R["walk"] = {"arena": "A3", "record": [1, 1, A3], "horizon": HORIZON,
                 "exit_A": exitA, "exit_B": exitB,
                 "branches_A": a3A["branches"], "branches_B": a3B["branches"],
                 "visits": a3A["visits"], "earliest_third_visit": third,
                 "exit_census": cen, "leaves_out": a3A["leaves_out"],
                 "one_site_out_per_leaf":
                     sum(cen.values()) == a3A["leaves_out"],
                 "indefinite_at_horizon_5": str(massof(a3A["rows"][-1],
                                                       "born", "INDEFINITE"))}
    ok = (exitA == anch["P-P20-EXIT"] and exitB == anch["P-P20-EXITB"]
          and branches == anch["P-P20-BRANCHES"]
          and a3B["branches"][-1] == anch["P-P20-BRANCHESB"]
          and cen == anch["P-P20-EXITCENSUS"] and third == anch["P-P20-THIRD"]
          and R["walk"]["one_site_out_per_leaf"])
    LD.gate("G-WALK-ANCHORED",
            "THE REBUILT WALK IS PAPER-20'S WALK, AT FIVE INDEPENDENT ROWS.  "
            "This file re-implements the coupled machine from the parent's "
            "declared machinery and never imports it; the rebuild is bound "
            "by reproducing, from its own arithmetic, the committed exit "
            "probability at BOTH emission readings, the branch counts at "
            "both, the exit census code by code, and the return-time row -- "
            "and by measuring, as the parent did, that every inadmissible "
            "leaf has exactly one site out",
            ok,
            "exit A %s vs %s, exit B %s vs %s, branches %s/%s vs %s/%s, "
            "census %s vs %s, third visit %s vs %s, one site out per leaf %s"
            % (exitA, anch["P-P20-EXIT"], exitB, anch["P-P20-EXITB"],
               branches, a3B["branches"][-1], anch["P-P20-BRANCHES"],
               anch["P-P20-BRANCHESB"], cen, anch["P-P20-EXITCENSUS"],
               third, anch["P-P20-THIRD"],
               R["walk"]["one_site_out_per_leaf"]))
    stoch = [0, 0]
    for st in (a3A, a3B):
        stoch[0] += st["checks"][0]
        stoch[1] += st["checks"][1]
    R["walk"]["stochastic_checks"] = stoch[0]
    R["walk"]["stochastic_violations"] = stoch[1]
    LD.gate("G-WALK-STOCHASTIC",
            "THE EMISSION LAW IS A PROBABILITY DISTRIBUTION AT EVERY BRANCH "
            "OF EVERY STEP (#87: per object, never in aggregate).  The "
            "law-native kernel's weights are summed on each branch "
            "separately and required to be exactly one; %d such checks are "
            "taken on the two anchored arms alone" % stoch[0],
            stoch[1] == 0 and stoch[0] > 0,
            "checks %d, violations %d" % (stoch[0], stoch[1]))
    SEAL.take("SEAL-WALK", R)

    # ---- the coin family --------------------------------------------------
    crows = []
    for nm, a3v, b3v, why in COIN_FIBER:
        M = coin_matrix(a3v, b3v)
        if mut("MUT-COIN") and nm == "MW":
            M = coin_matrix(a3v, (b3v[0], b3v[1] + 1))
        crows.append({"coin": nm, "why": why, "unitary": coin_unitary(M)})
    LD.gate("G-COIN-FAMILY",
            "THE DECLARED COIN FIBER IS EXACTLY UNITARY, MEMBER BY MEMBER.  "
            "Paper-20's S_3-covariant family 3C = 3a I + 3b J is rebuilt "
            "here and each of its %d classes is verified by C C* = I in "
            "Z[w] -- per member, never by a count" % len(COIN_FIBER),
            all(c["unitary"] for c in crows),
            "members %s" % [(c["coin"], c["unitary"]) for c in crows])

    # ---- STAGE 0B: the dynamic census -------------------------------------
    say("\n[SEC 4] STAGE 0B -- THE DYNAMIC REACHABILITY CENSUS")
    floors, prof = [], {}
    for nm, c, Rb, why in ARENAS[:3]:
        need = {}
        for tgt in (1, 2):
            need[tgt] = next((k for k in range(1, 12)
                              if region_of((1, 1, c + k)) == tgt), None)
        row = {"arena": nm, "record": [1, 1, c], "R": Rb, "why": why,
               "events_to_singular": need[1], "events_to_indefinite": need[2],
               "declared_name": {tuple(v): k
                                 for k, v in fam.items()}.get((1, 1, c), "-")}
        for rd in ("A", "B"):
            st = arm(HORIZON, c, links, rd)
            prof["%s/%s" % (nm, rd)] = st["rows"]
            row["first_singular_" + rd] = first_positive(st["rows"], "born",
                                                         "SINGULAR")
            row["first_indefinite_" + rd] = first_positive(st["rows"], "born",
                                                           "INDEFINITE")
            row["indefinite_" + rd] = str(massof(st["rows"][-1], "born",
                                                 "INDEFINITE"))
        row["first_singular"] = row["first_singular_A"]
        row["first_indefinite"] = row["first_indefinite_A"]
        floors.append(row)
    if mut("MUT-FIRST-INDEF"):
        floors = [dict(f) for f in floors]
        floors[1]["first_indefinite"] = 1
    R["dynamic"] = {"horizon": HORIZON, "floors": floors, "profiles": prof,
                    "measure": "the Born branch measure of the coupled "
                               "emission tree, exhaustive at every level"}
    live = [f for f in floors if f["first_indefinite"]]
    # THE EVENT-BUDGET BOUND, per object: the walk emits exactly one division
    # event per step, so a region that needs k events on one cell cannot be
    # entered before step k.  Every arena's measured first step is checked
    # against its own bound, never against an aggregate (#87).
    consistent = all(
        (f["first_indefinite"] is None
         or f["first_indefinite"] >= f["events_to_indefinite"])
        and (f["first_singular"] is None
             or f["first_singular"] >= f["events_to_singular"])
        for f in floors)
    LD.gate("G-STAGE0-DYNAMIC",
            "STAGE 0's DYNAMIC HALF, AND THE LICENCE EVERY POLARITY SENTENCE "
            "BELOW DEPENDS ON.  The region masses are measured at every "
            "horizon of the declared ladder on %d arenas at both emission "
            "readings; the indefinite region is occupied with POSITIVE exact "
            "mass at %d of them, and paper-20's own open question -- whether "
            "the indefinite region is reached at all -- is answered here "
            "rather than assumed.  Had this gate found no arena, the head "
            "would read SIG-BLOCKED-AT-REACHABILITY and no polarity word "
            "would be emitted" % (len(floors), len(live)),
            bool(live) and consistent,
            "arenas %s"
            % [(f["arena"], f["R"], f["events_to_singular"],
                f["first_singular"], f["events_to_indefinite"],
                f["first_indefinite"]) for f in floors])
    SEAL.take("SEAL-DYNAMIC", R)

    # ---- the pruned engine, and its soundness ------------------------------
    pr = {}
    for nm, c, _Rb, _w in ARENAS[:2]:
        pr[nm] = memo("prune", (HORIZON, c, links),
                      lambda c=c: run_pruned(HORIZON, arena_field(c), links))
    ext = memo("prune", (LADDER_T, A3, links),
               lambda: run_pruned(LADDER_T, arena_field(A3), links))
    if mut("MUT-PRUNE"):
        ext = [dict(r) for r in ext]
        ext[-1]["INDEFINITE"] = "0"
    mism = []
    for nm, c, _Rb, _w in ARENAS[:2]:
        for a, b in zip(pr[nm], arm(HORIZON, c, links, "A")["rows"]):
            for reg_ in ("SINGULAR", "INDEFINITE"):
                if Fraction(a[reg_]) != massof(b, "born", reg_):
                    mism.append((nm, a["t"], reg_))
    R["prune"] = {"horizon": LADDER_T, "arena": "A3", "rows": ext,
                  "checked_against_full_engine": len(pr) * HORIZON * 2,
                  "mismatches": mism,
                  "indefinite_at_extension": ext[-1]["INDEFINITE"],
                  "first_indefinite": next((r["t"] for r in ext
                                            if Fraction(r["INDEFINITE"]) > 0),
                                           None)}
    LD.gate("G-PRUNE-SOUND",
            "THE HORIZON EXTENSION IS PRUNED BY A THEOREM AND THE THEOREM IS "
            "CHECKED.  A branch that cannot raise any cell to the region "
            "floor within its remaining steps stays positive definite with "
            "its whole subtree, so its mass is carried in aggregate; the "
            "pruned engine is required to reproduce the FULL engine's "
            "singular and indefinite masses at every step of the horizon "
            "they share, on two arenas, before its extension to horizon %d "
            "is read.  That extension answers the inherited #211 dynamic "
            "floor: on paper-20's own arena the indefinite region is first "
            "occupied at step %s" % (LADDER_T, R["prune"]["first_indefinite"]),
            not mism and R["prune"]["first_indefinite"] == LADDER_T,
            "cross-checks %d, mismatches %s, first indefinite step %s, mass "
            "%s" % (R["prune"]["checked_against_full_engine"],
                    mism or "none", R["prune"]["first_indefinite"],
                    R["prune"]["indefinite_at_extension"]))
    SEAL.take("SEAL-PRUNE", R)

    # ---- STAGE 1: the clearing --------------------------------------------
    say("\n[SEC 5] STAGE 1 -- THE CLEARING")
    pairs = []
    for f in floors:
        # the sealed dynamic object is never mutated here: the extension
        # arena's horizon is read from the prune row beside it
        t = f["first_indefinite"]
        at_ext = False
        if not t and f["arena"] == R["prune"]["arena"]:
            t, at_ext = R["prune"]["first_indefinite"], True
        if not t:
            continue
        pairs.append({
            "arena": f["arena"], "record": f["record"], "R": f["R"],
            "horizon": t, "measured_at_extension": at_ext,
            "declared_name": f["declared_name"],
            "record_is_declared": f["declared_name"] != "-",
            "horizon_is_declared": t <= HORIZON,
            "no_new_declaration": (f["declared_name"] != "-"
                                   and t <= HORIZON),
            "cost_static_first": [f["R"], t],
            "cost_steps": f["R"] + t,
            "cost_incidences": 9 * f["R"] + t})
    winners = {
        "STATIC-FIRST": min(pairs, key=lambda p: p["cost_static_first"])
        ["arena"],
        "STEPS": min(pairs, key=lambda p: p["cost_steps"])["arena"],
        "INCIDENCES": min(pairs, key=lambda p: p["cost_incidences"])["arena"]}
    free = [p for p in pairs if p["no_new_declaration"]]
    chosen = pick("MUT-CLEARING", free[0] if free else pairs[0], pairs[-1])
    alt = sorted([p for p in pairs if p["arena"] != chosen["arena"]],
                 key=lambda p: p["horizon"])[0]
    cl = dict(chosen)
    cl.update({
        "first_singular": [f for f in floors
                           if f["arena"] == chosen["arena"]][0]
        ["first_singular"],
        "first_indefinite": chosen["horizon"],
        "indefinite_A": [f for f in floors
                         if f["arena"] == chosen["arena"]][0]["indefinite_A"],
        "indefinite_B": [f for f in floors
                         if f["arena"] == chosen["arena"]][0]["indefinite_B"],
        "alt_arena": alt["arena"], "alt_horizon": alt["horizon"],
        "alt_R": alt["R"], "pairs": pairs, "winners": winners,
        "selection": "THE PAIR THAT COSTS NO NEW DECLARATION: a record I7 "
                     "itself declares, at a horizon paper-20 itself "
                     "declared.  The three cost orders below do NOT agree, "
                     "and that disagreement is published rather than "
                     "resolved by fiat",
        "cost_order": "declared: STATIC-FIRST (R, then horizon), STEPS "
                      "(R + T) and INCIDENCES (9R + T), all three reported"})
    R["clearing"] = cl
    LD.gate("G-CLEARING",
            "STAGE 1, AND THE CHEAPEST PAIR IS ORDER-RELATIVE (RUNBOOK 15).  "
            "%d pairs clear.  Under the three declared cost orders the "
            "winners are %s -- they do not agree, so no pair is 'the' "
            "cheapest and this unit says so.  What IS unique is the pair "
            "that costs NO NEW DECLARATION: %s is I7's own declared %s at "
            "paper-20's own declared horizon %d, and it is selected on that "
            "measured property.  The gate requires the selected pair to "
            "carry POSITIVE indefinite mass at BOTH declared emission "
            "readings"
            % (len(pairs), winners, cl["arena"], cl["declared_name"],
               HORIZON),
            Fraction(cl["indefinite_A"]) > 0
            and Fraction(cl["indefinite_B"]) > 0
            and cl["no_new_declaration"] and len(free) == 1,
            "pairs %s, winners %s, no-new-declaration pairs %s, chosen %s "
            "(R=%d, T=%s), indefinite A %s B %s"
            % ([(p["arena"], p["R"], p["horizon"]) for p in pairs], winners,
               [p["arena"] for p in free], cl["arena"], cl["R"],
               cl["horizon"], cl["indefinite_A"], cl["indefinite_B"]))
    SEAL.take("SEAL-CLEARING", R)
    return cl, floors, crows, a3A


def stages23(LD, SEAL, R, texts, links, ST, fam, cl, floors, crows, a3A,
             paper_text, paper_rel, do_paper):
    """STAGE 2 (the polarity census) and STAGE 3 (forcedness), then the
    walls, the verdict and the paper gates."""
    say("\n[SEC 6] STAGE 2 -- THE POLARITY CENSUS")
    c = cl["record"][2]
    pol = {}
    ntot_bad = []
    for rd in ("A", "B"):
        st = arm(HORIZON, c, links, rd)
        sf = arm(HORIZON, c, links, rd, feedback=False)
        fz = arm(HORIZON, c, links, rd, feedback=False, update=False)
        last = st["rows"][-1]
        born = massof(last, "born", "INDEFINITE")
        null = massof(last, "null", "INDEFINITE")
        if mut("MUT-POLARITY-B") and rd == "B":
            born = null * Fraction(1, 2)
        for row in st["rows"]:
            ntot = sum(Fraction(v) for v in row["null"].values())
            btot = sum(Fraction(v) for v in row["born"].values())
            if mut("MUT-NULL") and row["t"] == 1:
                ntot = ntot + 1
            if ntot != 1 or btot != 1:
                ntot_bad.append((rd, row["t"], str(ntot), str(btot)))
        word = polarity_word(born, null)
        if mut("MUT-POLARITY-A") and rd == "A":
            word = "SELECTED"
        pol[rd] = {"born": str(born), "null": str(null),
                   "ratio": str(Fraction(born, null) if null else 0),
                   "word": word,
                   "stage_frozen": str(massof(sf["rows"][-1], "born",
                                              "INDEFINITE")),
                   "frozen": str(massof(fz["rows"][-1], "born",
                                        "INDEFINITE")),
                   "steps": [{"t": r["t"], "born": r["born"], "null": r["null"],
                              "branches": r["branches"],
                              "max_cell": r["max_cell"]} for r in st["rows"]]}
    pol["frozen_leaves"] = (Fraction(pol["A"]["frozen"]) > 0
                            or Fraction(pol["B"]["frozen"]) > 0)
    # THE POLARITY'S ARENA ROBUSTNESS: the same census at every arena that
    # clears inside the declared horizon, and the extension arena's Born mass
    # beside them (its uniform-on-support comparator is not affordable at the
    # extension horizon and no polarity word is emitted for it).
    arena_rows = []
    for f in floors:
        cc = f["record"][2]
        row = {"arena": f["arena"], "record": f["record"], "R": f["R"]}
        if f["first_indefinite"]:
            for rd in ("A", "B"):
                st = arm(HORIZON, cc, links, rd)
                b = massof(st["rows"][-1], "born", "INDEFINITE")
                n = massof(st["rows"][-1], "null", "INDEFINITE")
                row["born_" + rd] = str(b)
                row["null_" + rd] = str(n)
                row["word_" + rd] = polarity_word(b, n)
            row["horizon"] = HORIZON
        else:
            row["born_A"] = R["prune"]["indefinite_at_extension"]
            row["null_A"] = None
            row["word_A"] = None
            row["word_B"] = None
            row["horizon"] = LADDER_T
            row["priced"] = ("the extension horizon carries the Born mass "
                             "only: the uniform-on-support comparator needs "
                             "the whole unpruned tree, which the pruning "
                             "theorem is precisely what avoids")
        arena_rows.append(row)
    pol["arena_rows"] = arena_rows
    pol["arena_invariant_A"] = len({r["word_A"] for r in arena_rows
                                    if r["word_A"]}) == 1
    pol["arena_invariant_B"] = len({r["word_B"] for r in arena_rows
                                    if r["word_B"]}) == 1
    pol["measures"] = {
        "BORN": "the coupled emission tree's own branch measure",
        "NULL": "the UNIFORM-ON-SUPPORT counting measure on the SAME tree: "
                "every branch of a node gets equal weight, so the two "
                "measures differ only in the weights and never in the "
                "branches (E-24: the comparison is measure-declared)",
        "STAGE-FROZEN": "the same walk on phases that never update, with the "
                        "record still accumulating -- the arm that isolates "
                        "the back-reaction from the accumulation",
        "FROZEN": "paper-20's own control: the record never changes"}
    R["polarity"] = pol
    LD.gate("G-NULL-MEASURE",
            "BOTH DECLARED MEASURES ARE PROBABILITY MEASURES AT EVERY STEP "
            "(E-24).  The Born branch measure and the uniform-on-support "
            "counting measure are each required to sum to one at every step "
            "of every reading, per object rather than in aggregate, so no "
            "ratio below is a fraction of an unnormalised total",
            not ntot_bad, "steps checked %d, failures %s"
            % (2 * HORIZON, ntot_bad or "none"))
    LD.gate("G-POLARITY-A",
            "THE BORN MENU'S POLARITY, AGAINST A DECLARED NULL ON THE SAME "
            "TREE.  The indefinite mass is %s against %s, so the coupled "
            "dynamics is measured %s toward the indefinite region at this "
            "arena under this reading; the word is DERIVED from the two "
            "masses and typed nowhere"
            % (pol["A"]["born"], pol["A"]["null"], pol["A"]["word"]),
            pol["A"]["word"] == polarity_word(Fraction(pol["A"]["born"]),
                                              Fraction(pol["A"]["null"]))
            and pol["A"]["word"] == "AVOIDED"
            and pol["arena_invariant_A"],
            "born %s, null %s, ratio %s, word %s, stage-frozen %s, per-arena "
            "words %s (invariant %s)"
            % (pol["A"]["born"], pol["A"]["null"], pol["A"]["ratio"],
               pol["A"]["word"], pol["A"]["stage_frozen"],
               [(r["arena"], r["word_A"]) for r in pol["arena_rows"]],
               pol["arena_invariant_A"]))
    LD.gate("G-POLARITY-B",
            "THE RECORD MENU'S POLARITY, AND IT HAS THE OPPOSITE SIGN.  "
            "Under paper-20's second declared emission reading the same "
            "arena, the same walk and the same null give %s against %s: %s.  "
            "Both readings are the parent's own declared fiber and neither "
            "is privileged by anything measured here, which is what the "
            "outcome word below records"
            % (pol["B"]["born"], pol["B"]["null"], pol["B"]["word"]),
            pol["B"]["word"] == polarity_word(Fraction(pol["B"]["born"]),
                                              Fraction(pol["B"]["null"]))
            and pol["B"]["word"] == "SELECTED"
            and pol["arena_invariant_B"],
            "born %s, null %s, ratio %s, word %s, frozen control %s, "
            "per-arena words %s (invariant %s)"
            % (pol["B"]["born"], pol["B"]["null"], pol["B"]["ratio"],
               pol["B"]["word"], pol["B"]["frozen"],
               [(r["arena"], r["word_B"]) for r in pol["arena_rows"]],
               pol["arena_invariant_B"]))
    SEAL.take("SEAL-POLARITY-CENSUS", R)

    # ---- the mod-3 theorem, machine-checked -------------------------------
    say("\n[SEC 7] THE MOD-3 THEOREM")
    pairs, maps, ident = [], 0, 0
    for (x, y) in (("A3", "A6"), ("A4", "A7"), ("A5", "A8")):
        cx, cy = arena_of(x)[1], arena_of(y)[1]
        mx = path_map(4, cx, links, "A")
        my = path_map(4, cy, links, "A")
        if mut("MUT-MOD3") and x == "A4":
            my = [dict(d) for d in my]
            k = sorted(my[-1])[0]
            my[-1][k] = str(Fraction(my[-1][k]) * Fraction(1, 2))
        same = [a == b for a, b in zip(mx, my)]
        maps += len(same)
        ident += sum(1 for s in same if s)
        bx = arm(HORIZON, cx, links, "A")
        by = arm(HORIZON, cy, links, "A")
        rx = path_map(3, cx, links, "B")
        ry = path_map(3, cy, links, "B")
        pairs.append({"x": x, "y": y, "record_x": [1, 1, cx],
                      "record_y": [1, 1, cy], "levels": len(same),
                      "identical_A": sum(1 for s in same if s),
                      "identical_B": sum(1 for a, b in zip(rx, ry) if a == b),
                      "indefinite_x": str(massof(bx["rows"][-1], "born",
                                                 "INDEFINITE")),
                      "indefinite_y": str(massof(by["rows"][-1], "born",
                                                 "INDEFINITE")),
                      "marginal_identical": bx["marginal"] == by["marginal"]})
    R["mod3"] = {"checked": len(pairs), "maps": maps, "identical": ident,
                 "pairs": pairs, "horizon": 4,
                 "statement": "the Born branch measure is a function of the "
                              "record MODULO THREE, because the coin's only "
                              "record input is w^{n mod 3}; the signature is "
                              "a function of the record itself"}
    bbroken = all(p["identical_B"] < p["levels"] for p in pairs)
    LD.gate("G-MOD3-THEOREM",
            "THE MOD-3 THEOREM, MACHINE-CHECKED AND TWO-WAY.  The coin reads "
            "the record only through w^{n mod 3}, so two arenas whose "
            "records differ by three at every cell generate the SAME Born "
            "branch measure: %d pairs are compared path by path at %d "
            "branch-weight maps and agree at %d.  The same comparison under "
            "the RECORD menu DISAGREES at every level, which is what makes "
            "this a measurement rather than a restatement -- and the "
            "consequence is the scope of every absolute mass in this unit: "
            "the same measure carries different signature censuses"
            % (len(pairs), maps, ident),
            ident == maps and bbroken,
            "pairs %s, identical A %d of %d, record-menu levels identical %s"
            % ([(p["x"], p["y"]) for p in pairs], ident, maps,
               [p["identical_B"] for p in pairs]))
    SEAL.take("SEAL-MOD3", R)

    # ---- constraint B ------------------------------------------------------
    p2 = R["mod3"]["pairs"][1]
    carrier = pick("MUT-CONSTRAINT-B", "THE RECORD (the count field n)",
                   "THE SITE MARGINAL p(x)")
    fn = ast.parse(read_text(SELF, "SELF"))
    argsets = {}
    for node in ast.walk(fn):
        if isinstance(node, ast.FunctionDef) and node.name in (
                "region_of", "record_region", "det4_of", "q_of"):
            argsets[node.name] = [a.arg for a in node.args.args]
    banned = sorted({a for v in argsets.values() for a in v}
                    & {"psi", "state", "p", "marginal", "born"})
    R["constraint_b"] = {
        "carrier": carrier, "observable_signatures": argsets,
        "forbidden_arguments_present": banned,
        "cited": {"source": GDL_REL, "commit": GDL_COMMIT,
                  "quotation": GDL_BLINDNESS,
                  "why_not_read": "the working-tree copy is held dirty by a "
                                  "concurrent sibling and a committed-sha "
                                  "read would require a subprocess, which "
                                  "#91 forbids"},
        "site_marginal_identical": p2["marginal_identical"],
        "site_marginal_x": p2["x"], "site_marginal_y": p2["y"],
        "indefinite_x": p2["indefinite_x"], "indefinite_y": p2["indefinite_y"]}
    LD.gate("G-CONSTRAINT-B",
            "NO SITE-MARGINAL OBSERVABLE (the pin's constraint B, from the "
            "GDL blindness theorem at commit %s).  Two checks, one "
            "structural and one measured.  Structural: every observable this "
            "unit reads the region with takes the RECORD and nothing else -- "
            "an AST scan of their argument lists finds no state and no "
            "marginal.  Measured: the ensemble site marginal is IDENTICAL at "
            "%s and %s, whose records agree modulo three, while their "
            "indefinite masses are %s and %s -- so a site-marginal "
            "observable provably cannot carry this unit's verdict, and the "
            "blindness the parent proved is exhibited here on the very "
            "quantity in question"
            % (GDL_COMMIT, p2["x"], p2["y"], p2["indefinite_x"],
               p2["indefinite_y"]),
            carrier.startswith("THE RECORD") and not banned
            and p2["marginal_identical"]
            and p2["indefinite_x"] != p2["indefinite_y"],
            "carrier %s, observable arguments %s, forbidden arguments %s, "
            "marginals identical %s, indefinite masses %s vs %s"
            % (carrier, argsets, banned or "none", p2["marginal_identical"],
               p2["indefinite_x"], p2["indefinite_y"]))
    SEAL.take("SEAL-CONSTRAINT-B", R)

    # ---- STAGE 3: forcedness ----------------------------------------------
    say("\n[SEC 8] STAGE 3 -- FORCEDNESS ACROSS THE COIN FIBER")
    frows = []
    for row in crows:
        nm = row["coin"]
        r = {"coin": nm, "why": row["why"], "unitary": row["unitary"]}
        for rd in ("A", "B"):
            st = arm(HORIZON, c, links, rd, coin_name=nm)
            last = st["rows"][-1]
            b = massof(last, "born", "INDEFINITE")
            n = massof(last, "null", "INDEFINITE")
            r["born_" + rd] = str(b)
            r["null_" + rd] = str(n)
            r["word_" + rd] = polarity_word(b, n)
            r["branches_" + rd] = st["branches"][-1]
        frows.append(r)
    words = {"A": sorted({r["word_A"] for r in frows}),
             "B": sorted({r["word_B"] for r in frows})}
    if mut("MUT-FORCEDNESS"):
        frows = [dict(x) for x in frows]
        frows[2]["word_A"] = "SELECTED"
    inv = (len({r["word_A"] for r in frows}) == 1
           and len({r["word_B"] for r in frows}) == 1)
    R["forcedness"] = {"members": len(frows), "rows": frows,
                       "verdict": "INVARIANT" if inv else "COIN-RELATIVE",
                       "word_A": words["A"][0], "word_B": words["B"][0],
                       "readings_agree": words["A"] == words["B"],
                       "frozen_static_half":
                           "paper-20's frozen control cannot leave the region "
                           "it starts in at any horizon: its record never "
                           "changes and the region is a function of the "
                           "record alone -- measured %s here"
                           % R["polarity"]["A"]["frozen"]}
    LD.gate("G-FORCEDNESS",
            "STAGE 3.  The polarity is censused across paper-20's whole "
            "declared coin fiber -- %d S_3-covariant classes, every member "
            "run to the full horizon at BOTH readings.  The sign is "
            "INVARIANT across the fiber and OPPOSITE across the readings, so "
            "what is forced at this arena is the coin-independence, and what "
            "is not forced is the polarity itself" % len(frows),
            inv and not R["forcedness"]["readings_agree"],
            "verdict %s, Born words %s, record words %s, readings agree %s"
            % (R["forcedness"]["verdict"], words["A"], words["B"],
               R["forcedness"]["readings_agree"]))
    SEAL.take("SEAL-FORCEDNESS", R)

    # ---- the declared window ----------------------------------------------
    label = pick("MUT-WINDOW",
                 "ARENAS-%d-OF-THE-COLLINEAR-FAMILY+HORIZON-%d(LADDER-1..%d;"
                 "EXTENSION-%d-ON-A3)+COIN-FIBER-%d"
                 % (len(ARENAS), HORIZON, HORIZON, LADDER_T, len(COIN_FIBER)),
                 "NO-WINDOW")
    R["window"] = {
        "label": label, "arenas": len(ARENAS), "horizon": HORIZON,
        "extension": LADDER_T, "coins": len(COIN_FIBER),
        "priced": "the dynamic census is exhaustive at every level of every "
                  "arm it runs -- no sampling, no pruning by weight -- and "
                  "capped only by the declared horizon; the static census is "
                  "exhaustive over the objects it quantifies over, by "
                  "enumeration or by the deposit theorem, and never by the "
                  "window"}
    LD.gate("G-WINDOW-DISCLOSED",
            "THE WINDOW IS DECLARED IN THE HEAD'S OWN STRING.  %d arenas of "
            "the collinear family, horizon %d with the whole ladder "
            "published, one extension to %d, %d coins; every exhaustive "
            "column below is exhaustive over an object the window does not "
            "cap" % (len(ARENAS), HORIZON, LADDER_T, len(COIN_FIBER)),
            label != "NO-WINDOW" and str(HORIZON) in label,
            "window %s" % label)
    SEAL.take("SEAL-WINDOW", R)

    # ---- the walls ---------------------------------------------------------
    say("\n[SEC 9] THE WALLS")
    ptext = paper_text if paper_text is not None else ""
    if mut("MUT-WALL-L1"):
        ptext = ptext + "\n" + BANNED_L1 + "\n"
    named = signature_named(ST["floor_indefinite"]["code"],
                            det4_of(*ST["floor_indefinite"]["code"]))
    if mut("MUT-WALL-NAMED"):
        ptext = ptext.replace("is NAMED AND NOT READ", "is unremarkable")
    surface = json.dumps({k: R[k] for k in sorted(R) if k in MEASURED_KEYS},
                         sort_keys=True, default=str)
    surface += " ".join(g["statement"] + g["evidence"] for g in LD.rows)
    if mut("MUT-WALL-BHS"):
        surface = surface + " this record is a Poisson sprinkling into " \
                            "Minkowski and is statistically Lorentz invariant"
    if mut("MUT-WALL-KR"):
        surface = surface + " the Myrheim-Meyer dimension estimate of this " \
                            "order is 4 and the height control is not owed"
    l1 = canon(BANNED_L1) in canon(ptext)
    bhs = [w for w in ("sprinkling", "lorentz invariant", "lorentz-invariant")
           if w in surface.lower()]
    kr = [w for w in ("myrheim", "dimension estimate", "max-shatter",
                      "chart width") if w in surface.lower()]
    R["walls"] = {"L1_banned_present": l1, "bhs_hits": bhs, "kr_hits": kr,
                  "naming_sentence": named,
                  "naming_present": (canon(named) in canon(ptext)
                                     if paper_text is not None else None),
                  "surface_chars": len(surface),
                  "scope": "every wall is a scan of THIS RUN's declared "
                           "measurement surface -- every measured receipt key "
                           "together with the statement and evidence of every "
                           "gate evaluated -- and not a declaration"}
    LD.gate("G-WALL-L1",
            "L-1, ARGUED AND DECLINED.  Order-level covariance is a fourth "
            "form outside paper 8's three; admissibility would need a group "
            "declared to act on the generated causal order and a reason to "
            "read it as a covariance group.  This arena supplies finite "
            "records and a translation action on a nine-site lattice, and "
            "this unit constructs no bridge to any boost.  THE FOURTH FORM "
            "IS NOT TESTED HERE, and the sentence retracted in 2026 is "
            "absent from the object under test under the #125 normalisation",
            not l1, "retracted sentence present %s" % l1)
    LD.gate("G-WALL-BHS",
            "BHS.  The catalog records that a Poisson sprinkling admits no "
            "Lorentz-invariant finite-valency graph, and this arena is "
            "finite-valency by construction, so a sprinkling-grade test "
            "would manufacture a false negative.  None is run, and the "
            "abstention is MEASURED: this run's whole declared measurement "
            "surface (%d characters) is scanned for a sprinkling-grade "
            "reading" % len(surface),
            not bhs, "sprinkling-grade hits %s" % (bhs or "none"))
    LD.gate("G-WALL-KR",
            "KLEITMAN-ROTHSCHILD.  Every dimension reading owes a height "
            "control; this unit takes NO dimension reading -- no chart "
            "width, no Myrheim-Meyer estimate, no max-shatter reading -- so "
            "none is owed and none is manufactured.  The same surface is "
            "scanned",
            not kr, "dimension-reading hits %s" % (kr or "none"))
    LD.gate("G-WALL-SIGNATURE-NAMED",
            "THE SIGNATURE RESONANCE, NAMED AND NOT READ -- the sharpest "
            "wall this line has faced, because a determinant has now gone "
            "NEGATIVE.  The mandatory sentence is DERIVED from the measured "
            "floor code rather than typed, and it is required to be present "
            "in the object under test; a falsifier deletes it from that "
            "object and dies here.  Paper-21's own naming sentence is "
            "carried as a verbatim anchor beside it",
            (paper_text is None) or R["walls"]["naming_present"],
            "naming sentence present %s :: %s"
            % (R["walls"]["naming_present"], named[:60]))
    SEAL.take("SEAL-WALLS", R)

    # ---- the verdict -------------------------------------------------------
    say("\n[SEC 10] THE VERDICT")
    R["outcome"] = outcome_word(
        bool([f for f in floors if f["first_indefinite"]]),
        [R["forcedness"]["word_A"], R["forcedness"]["word_B"]])
    R["counts"] = {
        "sources": len(SOURCES), "path_anchors": len(PATH_ROWS),
        "verbatim_anchors": len(VERBATIM), "partitions": ST["partitions"],
        "arenas": len(ARENAS), "horizon": HORIZON, "extension": LADDER_T,
        "coins": len(COIN_FIBER), "covering_floor": ST["covering"]["R"],
        "live_floor": ST["live"]["R"], "clearing_R": cl["R"],
        "clearing_horizon": cl["first_indefinite"],
        "r5_multisets": ST["r5_multisets"],
        "fullsite_multisets": ST["fullsite_r5_multisets"],
        "branches_at_horizon": a3A["branches"][-1],
        "memo_hits": sum(MEMO_HITS.values()),
        "memo_misses": sum(MEMO_MISSES.values())}
    segs = build_verdict(R)
    if mut("MUT-VERDICT"):
        segs = [s.replace("SIG-BLOCKED-AT-THE-EMISSION-READING",
                          "SIG-AVOIDED") for s in segs]
    R["verdict"] = {"segments": segs}
    rebuilt, rword = reconstruct(json.dumps(R, indent=1, sort_keys=True,
                                            default=str))
    drift = [i for i, (a, b) in enumerate(zip(segs, rebuilt)) if a != b]
    tree = ast.parse(read_text(SELF, "SELF"))
    lit = {n: template_constants(tree, n)
           for n in ("build_verdict", "reconstruct")}
    typed = sorted({s for s in lit["build_verdict"] & lit["reconstruct"]
                    if NUMTOK.search(s)})
    LD.gate("G-VERDICT-RECONSTRUCTED",
            "THE HEAD IS DERIVED TWICE, BY ROUTINES THAT SHARE NO TYPED "
            "NUMBER.  The comparator re-parses the SERIALIZED receipt, types "
            "all %d templates itself, and re-derives the OUTCOME WORD from "
            "the receipt's own reachability and polarity rows through its "
            "own conditional -- so a forged word moves the builder alone and "
            "dies here.  An AST scan requires the two routines to share no "
            "string constant containing a numeral" % len(segs),
            not drift and rword == R["outcome"] and not typed,
            "segments %d, drift %s, outcome %s vs comparator %s, shared "
            "numeric literals %s"
            % (len(segs), drift or "none", R["outcome"], rword,
               typed or "none"))
    SEAL.take("SEAL-VERDICT", R)
    SEAL.take("SEAL-OUTCOME", R)
    SEAL.take("SEAL-COUNTS", R)
    for s in segs:
        say("")
        say(s)

    # ---- the paper gates ---------------------------------------------------
    R["paper_claims"] = paper_claims(R)
    R["paper_tables"] = paper_tables(R)
    claims = [dict(x) for x in R["paper_claims"]]
    if mut("MUT-PAPER-CLAIM"):
        claims[0]["claim"] = claims[0]["claim"].replace("at most", "at least")
    trows = list(R["paper_tables"])
    if mut("MUT-PAPER-TABLE"):
        trows[0] = trows[0].replace("NO", "YES")
    if do_paper and paper_text is not None:
        miss = [x["id"] for x in claims if not match_needle(ptext, x["claim"])]
        LD.gate("G-PAPER-CLAIMS",
                "EVERY HEADLINE SENTENCE RENDERS FROM THE RECEIPT.  %d "
                "claims are assembled from this run's measured values and "
                "required to occur in the object under test under the #125 "
                "normalisation, so a paper numeral that drifts from the "
                "receipt cannot survive" % len(claims),
                not miss, "claims %d, not found %s" % (len(claims),
                                                       miss or "none"))
        cnt = Counter(canon(ptext).count(canon(t)) for t in trows)
        tbad = [t for t in trows if canon(ptext).count(canon(t)) != 1]
        LD.gate("G-PAPER-TABLES",
                "THE LOAD-BEARING TABLES RENDER AS CLAIMS (E-22).  %d rows "
                "of the reachability, floor and coin-fiber tables are "
                "assembled from this run and each required to occur in the "
                "paper EXACTLY ONCE, so a forged cell dies even when every "
                "numeral in it is receipt-backed" % len(trows),
                not tbad, "rows %d, occurrence spectrum %s, wrong %s"
                % (len(trows), dict(cnt), tbad[:3] or "none"))
        R["paper_coverage"] = paper_coverage(R, ptext)
        pc = R["paper_coverage"]
        LD.gate("G-PAPER-COVERAGE",
                "NUMERAL COVERAGE OVER THE WHOLE PAPER (#20 + E-22): prose, "
                "tables, INLINE CODE SPANS and the fenced verdict blocks, "
                "against exactly three declared lists -- this run's "
                "registered numbers, the receipt it publishes, and a "
                "declared exemption table with a reason per literal, every "
                "one of which must fire.  The fenced blocks are matched by "
                "MULTISET against the declared copy count, and the scan is "
                "required to be NON-VACUOUS on the fences: a scanner that "
                "strips them is blind exactly where the highest-stakes "
                "numerals live (#168)",
                not pc["unbacked"] and not pc["fenced_unbacked"]
                and not pc["word_numerals_unbacked"]
                and not pc["exemptions_that_never_fire"]
                and pc["fenced_block_multiset_matches"]
                and pc["fenced_blocks_scanned"] == pc["fenced_blocks_found"]
                and pc["fenced_numerals_scanned"] > 0,
                "scanned %d numerals (%d fenced in %d blocks, %d spelled), "
                "unbacked %s, fenced unbacked %s, spelled unbacked %s, dead "
                "exemptions %s, fence multiset matches %s (%d of %d)"
                % (pc["numerals_scanned"], pc["fenced_numerals_scanned"],
                   pc["fenced_blocks_scanned"],
                   pc["word_numerals_scanned"], pc["unbacked"] or "none",
                   pc["fenced_unbacked"] or "none",
                   pc["word_numerals_unbacked"] or "none",
                   pc["exemptions_that_never_fire"] or "none",
                   pc["fenced_block_multiset_matches"],
                   pc["fenced_blocks_found"], pc["fenced_blocks_expected"]))
    else:
        R["paper_coverage"] = {"skipped": True}
    R["paper_claims"] = claims
    R["paper_tables"] = trows
    SEAL.take("SEAL-PAPER-CLAIMS", R)
    SEAL.take("SEAL-PAPER-TABLES", R)
    SEAL.take("SEAL-PAPER-COVERAGE", R)
    prows = paper_polarity(R, ptext)
    R["polarity_rows"] = prows
    LD.gate("G-PAPER-POLARITY",
            "THE PRE-REGISTERED POLARITY OF %d LOAD-BEARING CLAIMS.  Each "
            "was declared TRUE or FALSE before the run and is measured from "
            "the receipt here; the reachability row is the one the pin's "
            "first constraint turns on, and the two forcedness rows are "
            "where this unit's negative lives" % len(prows),
            all(p["agrees"] for p in prows),
            "rows %s" % [(p["id"], p["declared"], p["measured"])
                         for p in prows])
    SEAL.take("SEAL-POLARITY", R)


# ===========================================================================
# SECTION 15.  THE CLOSE
# ===========================================================================

def finish(LD, SEAL, R, write=True, swept=False):
    gate_names = sorted({g["gate"] for g in LD.rows} | set(LATE_GATES)
                        | set(PAPER_GATES) | set(CLOSING_LEDGER_GATES)
                        | {SWEEP_GATE})
    targeted = Counter(m[1] for m in MUTANTS)
    waivers = waiver_ledger()
    uncovered = [g for g in gate_names
                 if not targeted.get(g) and g not in waivers]
    registry_drift = sorted(set(gate_names) ^ set(GATE_REGISTRY))
    R["coverage"] = {
        "gates_evaluated": len(gate_names),
        "gates_with_a_declared_mutant": sum(1 for g in gate_names
                                            if targeted.get(g)),
        "gates_waived": sum(1 for g in gate_names if g in waivers),
        "uncovered": uncovered, "registry_drift": registry_drift,
        "denominator": "the gate count of THIS run, not a hand-kept number"}
    R["waiver_ledger"] = {k: {"class": v[0], "forcing": v[1]}
                          for k, v in waivers.items()}
    LD.gate("G-COVERAGE",
            "THE COVERAGE LEDGER IS HONEST AND ITS DENOMINATOR IS THIS RUN'S "
            "OWN.  Every gate evaluated anywhere in this run is either "
            "falsified by a declared mutant or waived with a machine-readable "
            "forcing; the declared registry and the set actually evaluated "
            "must agree exactly, so a gate removed from the file or added "
            "without a registry row dies here",
            not uncovered and not registry_drift,
            "gates %d, with a mutant %d, waived %d, uncovered %s, registry "
            "drift %s" % (len(gate_names),
                          R["coverage"]["gates_with_a_declared_mutant"],
                          R["coverage"]["gates_waived"], uncovered or "none",
                          registry_drift or "none"))
    SEAL.take("SEAL-COVERAGE", R)
    SEAL.take("SEAL-WAIVERS", R)
    SEAL.take("SEAL-MUTANTS", R)
    R.setdefault("mutant_sweep", [])
    sweep_rows = R["mutant_sweep"]
    sweep_ok = ((not swept) or (len(sweep_rows) == len(MUTANTS)
                                and all(k.get("on_target")
                                        for k in sweep_rows)))
    LD.gate("G-SWEEP-BOUND",
            "THE MUTANT SWEEP'S EXECUTION IS BOUND, NOT MERELY DECLARED.  A "
            "%s run must carry one sweep row per declared falsifier (%d), "
            "every row ON TARGET, and the same conjunction is re-taken at "
            "the terminal integrity gate, so the only writer in this file is "
            "downstream of a sweep that actually ran"
            % ("delivery-level" if swept else "mutant sub-", len(MUTANTS)),
            sweep_ok, "delivery-level %s, sweep rows %d of %d, on target %d"
            % (swept, len(sweep_rows), len(MUTANTS),
               sum(1 for k in sweep_rows if k.get("on_target"))))
    SEAL.take("SEAL-MUTANT-SWEEP", R)
    ran_here = {g["gate"] for g in LD.rows}
    vcons = [(v["id"], v["consumer_gate"]) for v in R["verbatim_anchors"]]
    if mut("MUT-CONSUMER-BINDING"):
        vcons = vcons[:-1] + [(vcons[-1][0], "G-NO-SUCH-GATE")]
    cons_bad = [vid for vid, g in vcons
                if g not in GATE_REGISTRY or g not in ran_here]
    LD.gate("G-ANCHOR-CONSUMERS",
            "EVERY VERBATIM ANCHOR'S NAMED CONSUMER IS A REAL GATE THAT "
            "REALLY RAN.  All %d anchors name the gate that consumes them, "
            "and each named gate is required here to be in the declared "
            "registry AND in this run's own evaluated ledger" % len(vcons),
            not cons_bad, "anchors %d, consumers not registered-and-evaluated "
            "%s" % (len(vcons), cons_bad or "none"))
    R["reachability"] = [
        {"mutant": m[0], "gate": m[1],
         "gate_evaluated_in_this_run": m[1] in gate_names,
         "late": m[1] in LATE_GATES} for m in MUTANTS]
    unreached = [r["mutant"] for r in R["reachability"]
                 if not r["gate_evaluated_in_this_run"]]
    LD.gate("G-REACHABILITY",
            "EVERY DECLARED FALSIFIER DEMONSTRABLY REACHES ITS GATE (#34).  "
            "%d of them name gates evaluated after this point in this same "
            "function, and their presence is verified at "
            "G-ARTIFACT-INTEGRITY rather than assumed here"
            % sum(1 for r in R["reachability"] if r["late"]),
            not unreached, "falsifiers %d, gates unreached %s"
            % (len(MUTANTS), unreached or "none"))
    SEAL.take("SEAL-REACHABILITY", R)
    R["arithmetic"] = "exact: Python int, fractions.Fraction, Z[w] as pairs"
    R["python"] = sys.version.split()[0]
    R["transcript_head"] = "\n".join(LINES).split("\n")[:40]
    R["totals"] = {
        "sources": len(SOURCES), "path_anchors": len(PATH_ROWS),
        "verbatim_anchors": len(R["verbatim_anchors"]),
        "gates": len(LD.rows), "mutants": len(MUTANTS),
        "seals": len(SEALED_PATHS), "waivers": len(R["waiver_ledger"]),
        "declared_unsealed": len(DECLARED_UNSEALED),
        "memo_entries": len(MEMO),
        "gates_snapshot_instant": "the gate ledger AT THE MOMENT THE PAYLOAD "
                                  "CLOSED: the two closing gates are "
                                  "evaluated after this snapshot, which is "
                                  "why coverage counts more gates than this"}
    bad_types = []

    def scan(o, path=""):
        if isinstance(o, float):
            bad_types.append(path)
        elif isinstance(o, dict):
            for k, v in o.items():
                scan(v, path + "/" + str(k))
        elif isinstance(o, (list, tuple)):
            for m, v in enumerate(o):
                scan(v, path + "/" + str(m))
    scan(R)
    LD.gate("G-PAYLOAD-CLOSES",
            "THE PAYLOAD CLOSES: %d gates evaluated, all passed, and a "
            "RECURSIVE TYPE SCAN of the receipt finds no float anywhere -- "
            "every published number is an int or a string carrying an exact "
            "Fraction" % len(LD.rows),
            all(g["passed"] for g in LD.rows) and not bad_types,
            "gates %d, float-valued receipt paths %s"
            % (len(LD.rows), bad_types or "none"))
    R["gates"] = [dict(g) for g in LD.rows]
    R["closing_gates"] = {
        "names": ["G-SEAL-COMPLETE", "G-ARTIFACT-INTEGRITY"],
        "warrant": "these two are evaluated after the gate ledger is "
                   "snapshotted and sealed -- G-SEAL-COMPLETE cannot be "
                   "inside the object it seals, and G-ARTIFACT-INTEGRITY "
                   "runs after the bytes are on disk; a run that fails any "
                   "gate writes nothing, so the artifacts themselves record "
                   "that verdict"}
    SEAL.take("SEAL-GATES", R)
    SEAL.take("SEAL-CLOSING", R)
    SEAL.take("SEAL-TOTALS", R)
    SEAL.take("SEAL-TRANSCRIPT", R)
    missing, extra = SEAL.totality()
    declared = sorted(set(R.keys()))
    covered = sorted({r["path"] for r in SEAL.rows} | set(DECLARED_UNSEALED))
    uncovered_keys = sorted(set(declared) - set(covered))
    unsealed_frozen = (tuple(DECLARED_UNSEALED) == DECLARED_UNSEALED_FROZEN)
    unsealed_clean = not (set(DECLARED_UNSEALED)
                          & ({p for _s, p, _g in SEALED_PATHS}
                             | set(MEASURED_KEYS)))
    R["seal_manifest"] = {"rows": SEAL.rows,
                          "declared_unsealed": DECLARED_UNSEALED,
                          "declared_unsealed_frozen": unsealed_frozen,
                          "declared_unsealed_carries_no_measurement":
                              unsealed_clean,
                          "declared_seals": [s for s, _p, _g in SEALED_PATHS]}
    broken = SEAL.verify(R)
    LD.gate("G-SEAL-COMPLETE",
            "THE TOTAL GATE-TO-DISK SEAL (#119 + the #148 totality "
            "addendum).  EVERY published receipt key is either sealed at the "
            "moment its gate passed or listed as DECLARED-UNSEALED, and this "
            "gate compares the manifest against the DECLARED seal set rather "
            "than against the seals that happened to be taken.  The vouching "
            "layer is inside the seal: schema, provenance, paper claims, "
            "polarity, coverage, reachability, gates, totals and the "
            "transcript head.  The unsealed list is frozen by content and by "
            "length and names no key that carries a measurement",
            not missing and not extra and not uncovered_keys and not broken
            and unsealed_frozen and unsealed_clean,
            "declared seals %d, taken %d, missing %s, extra %s, receipt keys "
            "not covered %s, broken at close %s, unsealed frozen %s and "
            "measurement-free %s"
            % (len(SEALED_PATHS), len(SEAL.rows), missing or "none",
               extra or "none", uncovered_keys or "none", broken or "none",
               unsealed_frozen, unsealed_clean))
    payload = json.dumps(R, indent=1, sort_keys=True, default=str)
    SEAL.close(R, payload)
    R["payload_sha256_12"] = SEAL.payload_sha
    text = "\n".join(LINES) + "\n"
    if not write:
        return payload, text
    tmp_j, tmp_t = OUT_JSON + ".tmp", OUT_TXT + ".tmp"
    try:
        return _write(LD, SEAL, R, payload, text, tmp_j, tmp_t)
    except GateFail:
        for stage in (tmp_j, tmp_t):
            if os.path.exists(stage):
                os.unlink(stage)
        raise


def _write(LD, SEAL, R, payload, text, tmp_j, tmp_t):
    final = json.dumps(R, indent=1, sort_keys=True, default=str)
    with open(tmp_j, "w", encoding="utf-8") as fh:
        fh.write(final + "\n")
    with open(tmp_t, "w", encoding="utf-8") as fh:
        fh.write(text)
    back = json.loads(read_text(tmp_j, "ARTIFACT-STAGED"))
    probe = dict(back)
    probe["counts"] = dict(probe["counts"])
    probe["counts"]["covering_floor"] = probe["counts"]["covering_floor"] + 1
    probe_caught = bool(SEAL.verify(probe))
    disk_broken = SEAL.verify(back)
    head_ok = (read_text(tmp_t, "ARTIFACT-STAGED").split("\n")[:40]
               == R["transcript_head"])
    sweep_complete = (len(R.get("mutant_sweep") or []) == len(MUTANTS)
                      and all(k.get("on_target")
                              for k in R.get("mutant_sweep") or []))
    reads_ok = (set(READS_BY_CATEGORY) <= set(READ_CATEGORIES)
                and len(READS_BY_CATEGORY.get("SOURCE", ())) == len(SOURCES))
    LD.gate("G-READS-DECLARED",
            "THE RUNTIME INPUT SET IS EXACTLY THE DECLARED ONE (#46/#91).  "
            "Every reader in this file records its category -- SOURCE, "
            "OBJECT-UNDER-TEST, SELF or the run's own staged artifacts -- "
            "and the SOURCE set is required to be exactly the %d pinned "
            "files" % len(SOURCES),
            reads_ok, "categories %s, sources read %d"
            % (sorted(READS_BY_CATEGORY), len(READS_BY_CATEGORY.get(
                "SOURCE", ()))))
    ran = {g["gate"] for g in LD.rows}
    late_ok = all(g in ran for g in LATE_GATES[:6])
    LD.gate("G-ARTIFACT-INTEGRITY",
            "INTEGRITY IS DISK-VS-SEAL, never a re-derivation: the payload "
            "is written from the SEALED object to a staged file, read back "
            "FROM DISK, and every sealed object compared against the digest "
            "taken at the moment its gate passed -- with a deliberately "
            "corrupted probe shown to be detected first.  The staged bytes "
            "are moved into place by os.replace ONLY after this gate passes",
            probe_caught and not disk_broken and head_ok and late_ok
            and sweep_complete,
            "corrupted probe detected %s, sealed objects broken on disk %s, "
            "transcript head matches %s, declared-later gates evaluated %s, "
            "sweep complete %s"
            % (probe_caught, disk_broken or "none", head_ok, late_ok,
               sweep_complete))
    os.replace(tmp_j, OUT_JSON)
    os.replace(tmp_t, OUT_TXT)
    return payload, text


# ===========================================================================
# SECTION 16.  THE CLI (#82)
# ===========================================================================

def run_mutant(name, paper_text):
    global MUT, QUIET
    old, MUT, QUIET = MUT, name, True
    del LINES[:]
    try:
        LD, SEAL, R = full_run(paper_text=paper_text)
        finish(LD, SEAL, R, write=False, swept=False)
        out = (False, None)
    except GateFail as exc:
        out = (True, str(exc).split(" :: ")[0])
    except (KeyError, IndexError, TypeError, ValueError, AssertionError,
            ZeroDivisionError) as exc:
        out = (True, "CRASH:%s" % type(exc).__name__)
    finally:
        MUT, QUIET = old, False
    return out


def artifact_digests():
    out = []
    for p in (OUT_JSON, OUT_TXT):
        if not os.path.exists(p):
            out.append((p, None))
            continue
        with open(p, "rb") as fh:
            out.append((p, hashlib.sha256(fh.read()).hexdigest()[:12]))
    return out


def selftest():
    """the REAL self-test: corrupt one anchor's expected digest in memory,
    confirm the run dies at the anchor gate, and WRITE NOTHING -- proved by
    DIGEST rather than by mtime.  The memo is CLEARED first, so the self-test
    evaluates fresh (RUNBOOK 14 addendum)."""
    global QUIET
    before = artifact_digests()
    MEMO.clear()
    MEMO_HITS.clear()
    MEMO_MISSES.clear()
    QUIET = True
    del LINES[:]
    died, where = False, None
    try:
        LD, SEAL, R = full_run(break_anchor="A-P20REC", do_paper=False)
        finish(LD, SEAL, R, write=False)
    except GateFail as exc:
        died = True
        where = str(exc).split(" :: ")[0]
    QUIET = False
    after = artifact_digests()
    print("[SELFTEST] corrupted anchor A-P20REC :: died=%s at %s :: the "
          "memo was CLEARED first and the corrupted run reached it %d times "
          "(it dies at provenance, upstream of every memoised object) :: "
          "artifacts unchanged by sha256=%s %s"
          % (died, where, sum(MEMO_MISSES.values()) + sum(MEMO_HITS.values()),
             before == after, [d for _p, d in after]))
    if not died or before != after:
        return 2
    return 1


def parse_args(argv):
    """the #82 whitelist: unknown flags, unknown flag arguments, missing flag
    arguments and second mode flags all exit 2."""
    modes = {"--no-write", "--numbers", "--selftest", "--mutant",
             "--break-anchor", "--verify-paper", "--list-gates",
             "--list-mutants"}
    out = {"mode": None, "arg": None}
    i = 0
    while i < len(argv):
        a = argv[i]
        if a not in modes:
            raise CliError("unknown argument %r" % a)
        if out["mode"] is not None:
            raise CliError("modes do not compose: %r after %r"
                           % (a, out["mode"]))
        if a == "--mutant":
            if i + 1 >= len(argv):
                raise CliError("--mutant requires NAME")
            if argv[i + 1] not in MUTANT_NAMES:
                raise CliError("unknown mutant %r" % argv[i + 1])
            out["mode"], out["arg"] = a, argv[i + 1]
            i += 2
            continue
        if a == "--break-anchor":
            if i + 1 >= len(argv):
                raise CliError("--break-anchor requires NAME")
            if argv[i + 1] not in SOURCE_IDS:
                raise CliError("unknown anchor %r" % argv[i + 1])
            out["mode"], out["arg"] = a, argv[i + 1]
            i += 2
            continue
        if a == "--verify-paper":
            out["mode"] = a
            if i + 1 < len(argv) and not argv[i + 1].startswith("--"):
                out["arg"] = argv[i + 1]
                i += 2
                continue
            i += 1
            continue
        out["mode"] = a
        i += 1
    return out


def main(argv=None):
    global MUT, QUIET
    argv = list(sys.argv[1:] if argv is None else argv)
    try:
        opt = parse_args(argv)
    except CliError as exc:
        print("[CLI] %s" % exc)
        return 2
    mode, arg = opt["mode"], opt["arg"]
    if mode == "--list-gates":
        for g in GATE_REGISTRY:
            print(g)
        return 0
    if mode == "--list-mutants":
        for m in MUTANTS:
            print("%-22s %-26s corrupts %-24s %s" % (m[0], m[1], m[3], m[2]))
        return 0
    if mode == "--selftest":
        return selftest()
    if mode == "--break-anchor":
        try:
            LD, SEAL, R = full_run(break_anchor=arg, do_paper=False)
            finish(LD, SEAL, R, write=False)
        except GateFail as exc:
            print("[BREAK-ANCHOR %s] died at %s"
                  % (arg, str(exc).split(" :: ")[0]))
            return 1
        print("[BREAK-ANCHOR %s] SURVIVED -- not load-bearing" % arg)
        return 0
    if mode == "--verify-paper":
        path = arg or os.path.join(REPO, PAPER_REL)
        if not os.path.isfile(path):
            print("[CLI] --verify-paper: %r is not a file" % path)
            return 2
        try:
            LD, SEAL, R = full_run(
                paper_text=read_text(path, "OBJECT-UNDER-TEST"),
                paper_rel=os.path.relpath(path, REPO))
            finish(LD, SEAL, R, write=False)
        except GateFail as exc:
            print("[VERIFY-PAPER] DRIFT :: %s" % exc)
            return 1
        print("[VERIFY-PAPER] clean: %s" % path)
        return 0
    if mode == "--mutant":
        killed, where = run_mutant(
            arg, read_text(os.path.join(REPO, PAPER_REL),
                           "OBJECT-UNDER-TEST"))
        target = [m[1] for m in MUTANTS if m[0] == arg][0]
        print("[MUTANT %s] killed=%s at %s (target %s) -> %s"
              % (arg, killed, where, target,
                 "ON TARGET" if killed and where == target else "OFF TARGET"))
        return 1 if killed else 0
    if mode == "--numbers":
        LD, SEAL, R = full_run(do_paper=False)
        print(json.dumps(R["counts"], indent=1, sort_keys=True))
        for seg in R["verdict"]["segments"]:
            print()
            print(seg)
        return 0
    ptext = read_text(os.path.join(REPO, PAPER_REL), "OBJECT-UNDER-TEST")
    LD, SEAL, R = full_run(paper_text=ptext)
    say("\n[SEC 11] THE MUTANT SWEEP, IN-PROCESS")
    sweep = []
    keep = list(LINES)
    for name, gate, _what, _corrupts in MUTANTS:
        killed, where = run_mutant(name, ptext)
        sweep.append({"mutant": name, "target": gate, "killed": killed,
                      "died_at": where,
                      "on_target": bool(killed and where == gate)})
    del LINES[:]
    LINES.extend(keep)
    for row in sweep:
        say("    %-22s -> %-28s %s"
            % (row["mutant"], row["died_at"],
               "ON TARGET" if row["on_target"] else "OFF TARGET"))
    R["mutant_sweep"] = sweep
    off = [r["mutant"] for r in sweep if not r["on_target"]]
    LD.gate("G-MUTANTS-ON-TARGET",
            "EVERY DECLARED FALSIFIER IS RUN IN-PROCESS AND DIES AT THE GATE "
            "IT NAMES.  %d falsifiers, each a real corruption of a measured "
            "value or of the object under test, each required to be killed "
            "BY ITS OWN NAMED GATE rather than by whichever gate fires first"
            % len(MUTANTS),
            not off, "falsifiers %d, off target %s" % (len(MUTANTS),
                                                       off or "none"))
    payload, text = finish(LD, SEAL, R, write=(mode != "--no-write"),
                           swept=True)
    print("\n[PAYLOAD] sha256-12 %s   gates %d   falsifiers %d   %s"
          % (R["payload_sha256_12"], len(LD.rows), len(MUTANTS),
             "WROTE %s and %s" % (os.path.basename(OUT_JSON),
                                  os.path.basename(OUT_TXT))
             if mode != "--no-write" else "wrote nothing"))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except GateFail as _exc:
        print("\n[GATE FAILED] %s" % _exc)
        sys.exit(1)
    except FileNotFoundError as _exc:
        print("[CLI] missing source: %s" % _exc)
        sys.exit(1)
