#!/usr/bin/env python3.13
# -*- coding: utf-8 -*-
"""
v14 OCC -- THE OCCUPANCY-CEILING FORCING UNIT.
Instrument for `v14/paper-31-occ.md`.

QUESTION (pin `v14/note-occ-pin.md`, sha256-12 145db72ce547, ledger #249).
Paper-22 left FORCING-THE-CEILING=OPEN: the occupancy ceiling is the
coordinate that selects an exchange shape, and its own stage declares none.
Its seed conditional (paper-22 K2) reads: weld ACTOR->SITE bijection +
excitation<->actor injection + closure-required + the full pool ==> hard-core
forced ==> fermionic-shape is a theorem of the coupled theory.  THIS UNIT
MEASURES THAT CONDITIONAL PREMISE BY PREMISE ON THE COMMITTED LAYERS, and
never assumes it:

  P1  THE BIJECTION.  Is the weld's dictionary a bijection ON THE ARENA THE
      EXCITATIONS USE?  The coupled machine's carrier is rebuilt here and the
      two legs of the forced dictionary are measured against it.
  P2  THE TURNING PREMISE.  In the coupled representation, is a DOUBLY
      OCCUPIED state constructible at all -- can two excitations ride one
      actor in the committed grammar, or does the representation exclude it
      structurally?  The STATE SPACE'S CONSTRUCTION is measured, not its
      usage.
  P3  CLOSURE.  Can an actor carrying two excitations still divide per the
      committed grammar?  If the grammar is SILENT, the silence is the
      finding and the needed declaration is priced.
  P4  THE POOL.  The leak census at every declared grain, on every member of
      the arena's own coin family, with paper-22's 48/16 split cited from its
      committed receipt and never retyped.

THE VERDICT is derived from those four premises by a head law that is
exercised on SIX arenas and returns FOUR different pre-registered outcome
words across them -- including the two-way control the pin requires: an arena
where the conditional demonstrably FIRES (a subset-valued carrier) and one
where it demonstrably FAILS (the same carrier with multiset configurations,
where double occupancy is constructible).

WHAT THIS PROGRAM DOES
  SEC 1  PROVENANCE.  12 pinned sources read by path and hash, verbatim
         anchors bound to their consumer gates, path-value anchors read out of
         the parents' own committed receipts.
  SEC 2  MACHINERY.  The gate ledger, the total gate-time seal, the text
         normaliser, the memo with a content fingerprint.
  SEC 3  EXACT ARITHMETIC on Z[w], w^2 = -1-w, and THE CARRIER, rebuilt: the
         nine actors, the three declared link directions, the 27 cells, and
         the bijection between a cell and an unordered co-division pair.
  SEC 4  THE POOL.  The S_3-covariant coin family over the arena's own
         (1/3)Z[w] is rebuilt and gated against the coupled machine's
         committed census; each class gives one walk operator on the 27 cells.
  SEC 5  THE DECLARATIONS.  Four (grain, ceiling) declarations, their
         two-excitation configuration spaces, the free lift into both exchange
         shapes, and the leak census by TWO independent routes.
  SEC 6  P1, SEC 7  P2, SEC 8  P3, SEC 9  P4.
  SEC 10 THE ARMS -- the head law on six arenas.
  SEC 11 THE ASYMMETRY ROW, measured against both arms.
  SEC 12 THE WALLS -- shape words only, as an instrument; L-1; BHS;
         Kleitman-Rothschild; the continuum and cosmological abstentions.
  SEC 13 THE VERDICT, derived and then audited by a DE-TWINNED comparator
         that types no copy of the template: it PARSES the head, re-derives
         every field from the receipt by its own map, and re-derives the
         outcome word from the premise rows by its own copy of the head law.
         Then the paper gates, the total seal and the artifacts.

CLI CONTRACT (the #82 minimum: argv parsed against a WHITELIST)
---------------------------------------------------------------
    python3.13 v14/code/occ_exact.py         THE DELIVERY RUN, the only writer
    --no-write      the same run, writing nothing
    --numbers       the census only; no paper gate, no sweep, nothing written
    --selftest      corrupts one declared anchor IN MEMORY, confirms the run
                    is refused, writes nothing, exits 1 (2 if it survives)
    --mutant NAME   one declared falsifier, artifacts untouched; EXITS 1 when
                    the falsifier dies at the gate it names (on target) and 0
                    when it does not, so a green exit is the finding
    --break-anchor NAME     corrupts that source's expected digest; the run
                    dies at G-PROVENANCE and EXITS 1
    --verify-paper [PATH]   the paper gates against PATH; exits 0 when every
                    gate passes and 1 at the first that does not
    --list-gates / --list-mutants   print the registry and exit 0
    Any other argument, any unknown flag argument, any missing flag argument
    and any SECOND MODE FLAG exits 2.  Modes do not compose.

THE TOTAL GATE-TO-DISK SEAL.  Every published receipt key is either sealed at
the moment its gate passes or listed as DECLARED-UNSEALED with a forcing; the
artifacts are written from the sealed payload, read back FROM DISK and
compared against the gate-time seal before either is promoted by os.replace.
A run that fails any gate writes nothing and promotes nothing.

ARITHMETIC.  Exact only: Python integers and fractions.Fraction, with every
amplitude carried as an INTEGER PAIR over Z[w] with a common denominator 3.
There are no floats anywhere -- an AST scan of this file and a recursive type
scan of the emitted receipt are gates.

MEASURE-RELATIVITY (E-24).  Every fraction published here is a COUNT over a
declared enumeration.  No measure on configurations, generators or arenas is
declared, and every ratio is stamped COUNTING-ONLY.

RUNTIME INPUTS (#46/#91).  The declared SOURCES are read at run time by path
resolved from this file's own location and all hash-pinned; the second read
set -- this file and the object under test -- is declared and gated the same
way.  No repository state outside those two sets is read, no subprocess of any
kind is invoked and no version-control state is consulted, so the run is
correct off-tree and on a machine with no git.
"""

import ast
import hashlib
import json
import os
import re
import sys
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations

sys.setrecursionlimit(100000)

SELF = os.path.abspath(__file__)
REPO = os.path.dirname(os.path.dirname(os.path.dirname(SELF)))
OUT_TXT = os.path.join(os.path.dirname(SELF), "occ_output.txt")
OUT_JSON = os.path.join(os.path.dirname(SELF), "occ_receipt.json")

SCHEMA = "isp/v14/occ/1"
PAPER_REL = "v14/paper-31-occ.md"

LINES = []
READS = []
QUIET = False
MUT = None

# ===========================================================================
# SECTION 1.  PROVENANCE
# ===========================================================================

SOURCES = [
    ("A-PIN", "v14/note-occ-pin.md", "145db72ce547",
     "THIS UNIT'S PIN (ledger #249): the four premises, the pre-registered "
     "outcomes, the two-way control and the walls."),
    ("A-P22", "v14/paper-22-multi.md", "fb05cc2a376a",
     "PAPER-22 (terminal, #248): the leak theorem, the two ceilings compared "
     "as objects, the one-way asymmetry, and the head clause "
     "FORCING-THE-CEILING=OPEN this unit inherits as its question."),
    ("A-P22REC", "v14/code/r4c_multi_receipt.json", "afa46ffaf651",
     "PAPER-22'S COMMITTED RECEIPT: the 48/16 leak split and the stage's "
     "27 declaration keys, CITED from its own rows and never retyped."),
    ("A-P22SRC", "v14/code/r4c_multi_exact.py", "f202cf185804",
     "PAPER-22'S INSTRUMENT, read for its digest only: never imported and "
     "never executed."),
    ("A-W3", "v14/paper-19-r3-weld.md", "50bb81e67942",
     "THE WELD (paper-19, terminal): the FORCED DICTIONARY and its fibers "
     "1/1/1 -- the premise P1 asks about."),
    ("A-W3REC", "v14/code/r3_weld_receipt.json", "dfea664f2408",
     "THE WELD'S COMMITTED RECEIPT: the arena's cells and incidences, read "
     "as data."),
    ("A-COUP", "v14/paper-20-coupling.md", "4824d190af73",
     "THE COUPLED MACHINE (paper-20, terminal): the walk, the coin family, "
     "the emission grammar and the law transport."),
    ("A-COUPREC", "v14/code/coupling_receipt.json", "55273f6b6068",
     "THE COUPLED MACHINE'S COMMITTED RECEIPT: the carrier, the coin census "
     "and the arena rows this unit rebuilds and gates against."),
    ("A-COUPSRC", "v14/code/coupling_exact.py", "72e7b299f66e",
     "THE COUPLED MACHINE'S INSTRUMENT: read as TEXT for its own statement "
     "of what a cell is, and AST-parsed for its state-space construction. "
     "Never imported and never executed."),
    ("A-D42B1", "v10/code/d42b1_transport_exact.py", "576275d55ecf",
     "THE COMMITTED TRANSPORT GRAMMAR: the division-event layer whose "
     "vocabulary premise P3 censuses."),
    ("A-D60", "v10/code/d60_crystal_exact.py", "684cdb76552b",
     "D60: the committed builder the grammar runs on."),
    ("A-D66", "v10/code/d66_arbitration_crystal_exact.py", "3d0516ab106e",
     "D66: the committed conflict-grid constructor."),
]
SOURCE_IDS = [s[0] for s in SOURCES]

OBJECT_READS_WHY = {
    "SELF": "this file, AST-parsed by its own float scan, import scan, "
            "falsifier-hook probe and writer-shape probe",
    "PAPER": "the object under test, read once by main and handed to the "
             "paper gates",
}

# (id, source, the verbatim needle, the gate that consumes it)
VERBATIM = [
    ("VB-SEED", "A-PIN",
     "weld ACTOR->SITE bijection + excitation<->actor injection + "
     "closure-required + the full 64-pool", "G-QUESTION-ANCHORED"),
    ("VB-TURN", "A-PIN",
     "is a DOUBLY-OCCUPIED state constructible at all", "G-P2-TURNING"),
    ("VB-OPEN", "A-P22", "FORCING-THE-CEILING=OPEN", "G-QUESTION-ANCHORED"),
    ("VB-ASYM", "A-P22",
     "Exclusion can select a shape; permission cannot.", "G-ASYMMETRY"),
    ("VB-LEAK", "A-P22",
     "The symmetric square therefore leaks out of the hard core if and only "
     "if some row of *U* carries two nonzero entries", "G-LEAK-THEOREM"),
    ("VB-DICT", "A-W3",
     "WELD3-FOUND-[ACTOR->SITE|CO-DIVISION-ACTOR-PAIR->LINK|"
     "DIVISION-COUNT->n_l(x)]", "G-P1-DICTIONARY"),
    ("VB-CELL", "A-COUPSRC",
     "the arena's 27 cells, indexed site-major.  Cell (x, l) IS the unordered "
     "co-division pair {x, x+l}", "G-P1-CARRIER"),
    ("VB-RESIDUE", "A-COUP",
     "the walk consumes the count residue n mod 3, not the count",
     "G-P2-STATE-SPACE"),
]

# (id, source, json path, the expected value, the gate that consumes it).
# #91's path-value stability: every one is READ from a committed receipt and
# eaten by a gate; none is a decoration.
PATH_VALUES = [
    ("PV-SITES", "A-COUPREC", "arena/sites", 9, "G-P1-CARRIER"),
    ("PV-CELLS", "A-COUPREC", "arena/cells", 27, "G-P1-CARRIER"),
    ("PV-LINKS", "A-COUPREC", "arena/links", [[1, 0], [0, 1], [1, 1]],
     "G-P1-CARRIER"),
    ("PV-PAIRS", "A-COUPREC", "arena/realised_pairs", 27, "G-P1-DICTIONARY"),
    ("PV-INCID", "A-COUPREC", "arena/relation_is_target_incidence", True,
     "G-P1-DICTIONARY"),
    ("PV-WELDED", "A-COUPREC", "arena/cells_at_one", 27, "G-P1-CARRIER"),
    ("PV-COIN-RING", "A-COUPREC", "walk/coin_census/ring_solutions", 36,
     "G-POOL-REBUILT"),
    ("PV-COIN-CLASSES", "A-COUPREC", "walk/coin_census/classes_up_to_phase",
     6, "G-POOL-REBUILT"),
    ("PV-COIN-GROVER", "A-COUPREC",
     "walk/coin_census/grover_classes_up_to_phase", 1, "G-POOL-REBUILT"),
    ("PV-ALPHABET", "A-COUPREC", "walk/scalar_shape/alphabet", 37,
     "G-POOL-REBUILT"),
    ("PV-W3-CELLS", "A-W3REC", "arena/cells", 27, "G-P1-DICTIONARY"),
    ("PV-W3-INCID", "A-W3REC", "arena/incidences", 27, "G-P1-DICTIONARY"),
    ("PV-P22-CEILING", "A-P22REC", "occupancy/ceiling_is_anchored", False,
     "G-QUESTION-ANCHORED"),
    ("PV-P22-KEYS", "A-P22REC", "occupancy/stage_declaration_keys", 27,
     "G-P2-NO-OCCUPANCY-KEY"),
    ("PV-P22-OCCKEYS", "A-P22REC", "occupancy/stage_occupancy_shaped_keys", 0,
     "G-P2-NO-OCCUPANCY-KEY"),
    ("PV-P22-AGREE", "A-P22REC",
     "occupancy/one_excitation_restrictions_agree_as_objects", 64,
     "G-P2-INVISIBLE-FROM-BELOW"),
]

# THE OCCUPANCY VOCABULARY, declared.  A name is occupancy-shaped when it
# carries one of these tokens: they name a carrier's load, not a sector.
OCCUPANCY_TOKENS = ("occupan", "excitat", "doubly", "hard_core", "hardcore",
                    "fermion", "boson", "pauli", "multiply_occupied",
                    "exclusion_principle")
# the HOMONYM: `ceiling` occurs in the committed layers with a DIFFERENT
# referent, and this unit measures that rather than suppressing it.  Every
# occurrence must match a declared referent or the gate fails.
HOMONYM_TOKEN = "ceiling"
HOMONYM_REFERENTS = {
    "A-W3REC": "the weld's POSITIVE-DEFINITENESS ceiling -- the largest "
               "count triple its Sylvester scan attains -- which is a bound "
               "on DIVISION COUNTS on a link, not on excitations at a site",
    "A-D60": "d60's ENGINEERED ceiling on its crystal search",
    "A-D66": "d66's k*Bl budget ceiling on arbitration",
    "A-W3": "the weld paper's own use of the two above",
    "A-P22REC": "the OCCUPANCY ceiling paper-22 DECLARED -- the one referent "
                "in the census that is occupancy-shaped, which is exactly why "
                "that source is this scan's positive control and not one of "
                "the deeper layers",
}

BANNED_WORDS = ("fermion", "fermions", "fermionic", "boson", "bosons",
                "bosonic", "anyon", "anyons", "anyonic", "parastatistics",
                "spin", "spins", "electron", "electrons", "photon", "photons",
                "quark", "quarks", "atom", "atoms", "molecule", "molecules",
                "particle", "particles")
LICENSED_COMPOUNDS = ("fermionic-shape", "bosonic-shape", "no-particle",
                      "particle-shaped")

# the four inherited walls, as scans over THIS RUN's own measurement layer
WALL_NEEDLES = {
    "G-WALL-L1": ("order-level covariance is established",
                  "L-1's fourth form is not tested here and no order-level "
                  "covariance claim is made"),
    "G-WALL-BHS": ("boosted rest frame",
                   "no sprinkling-grade or BHS-class reading is taken"),
    "G-WALL-KR": ("myrheim-meyer",
                  "no dimension estimator and no height control is owed"),
    "G-WALL-COSMO": ("cosmological expansion",
                     "no continuum, cosmological or infinite-volume reading "
                     "is taken"),
}

# ===========================================================================
# SECTION 2.  MACHINERY
# ===========================================================================


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


def read_bytes(rel):
    READS.append(rel)
    path = os.path.join(REPO, rel)
    if not os.path.exists(path):
        raise GateFail("G-PROVENANCE :: a pinned source is not at its path "
                       ":: %s" % rel)
    with open(path, "rb") as fh:
        return fh.read()


def read_text(path):
    with open(path, "r", encoding="utf-8") as fh:
        return fh.read()


_FOLD = {"—": "--", "–": "-", "’": "'", "“": '"',
         "”": '"', "≤": "<=", "≥": ">=", "≠": "!=",
         "≡": "=", "×": "x", "₁": "1", "₂": "2",
         "₀": "0", "₃": "3", "ℓ": "l", "→": "->",
         "⋅": "*", "²": "2", "≈": "~", "⊆": "subset",
         "∈": "in", "∑": "sum", "·": "*", "−": "-",
         "⁄": "/", " ": " ", "ω": "w", "ψ": "psi",
         "Γ": "Gamma", "⊗": "(x)", "√": "sqrt",
         "⟨": "<", "⟩": ">", "Δ": "Delta", "π": "pi",
         "∧": "^", "∩": "cap", "∪": "cup", "↔": "<->",
         "⟹": "=>", "⟺": "<=>", "⊗": "(x)"}

_MD_PREFIX = re.compile(r"^(?:\s*(?:>+|[-*+]|\d+[.)])\s+)+")


def mdstrip(s):
    """#125 WITH MARKDOWN-PREFIX NORMALIZATION."""
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


NEEDLE_FLOOR = 20


def match_needle(hay, needle):
    n = canon(needle)
    if len(n) < NEEDLE_FLOOR:
        raise GateFail("G-VERBATIM :: needle below the #62 length floor: %r"
                       % needle)
    return n in canon(hay)


# ===========================================================================
# SECTION 3.  EXACT ARITHMETIC ON Z[w] AND THE CARRIER, REBUILT
# ===========================================================================
# Z[w], w^2 = -1-w.  An element is the INTEGER PAIR (a, b) meaning a + b*w.
# Every amplitude here is such a pair over the common denominator 3, so the
# whole census is integer arithmetic and no float is ever constructed.


def zmul(z1, z2):
    a, b = z1
    c, d = z2
    return (a * c - b * d, a * d + b * c - b * d)


def zadd(z1, z2):
    return (z1[0] + z2[0], z1[1] + z2[1])


def zsub(z1, z2):
    return (z1[0] - z2[0], z1[1] - z2[1])


def zconj(z):
    a, b = z
    return (a - b, -b)


def absq(z):
    """|a + b w|^2 = a^2 - ab + b^2, a RATIONAL INTEGER."""
    a, b = z
    return a * a - a * b + b * b


Z0 = (0, 0)
W1 = (0, 1)

SITES = tuple((i, j) for i in range(3) for j in range(3))
SITE_INDEX = {s: k for k, s in enumerate(SITES)}
# I7's three DECLARED link directions; (1,2) is the fourth parallel class,
# which I7 does not declare.
LINKS = ((1, 0), (0, 1), (1, 1))
UNDECLARED_DIRECTION = (1, 2)


def vadd(a, b):
    return ((a[0] + b[0]) % 3, (a[1] + b[1]) % 3)


def cell(si, li):
    return si * 3 + li


NCELL = 27
CELL_SITE = tuple(c // 3 for c in range(NCELL))
CELL_LINK = tuple(c % 3 for c in range(NCELL))
# THE CARRIER'S OWN IDENTITY: a cell IS an unordered co-division pair of
# actors.  This is the committed instrument's own statement (VB-CELL) and it
# is rebuilt here rather than quoted.
CELL_PAIR = {}
for _s in range(9):
    for _i in range(3):
        _x = SITES[_s]
        CELL_PAIR[cell(_s, _i)] = frozenset((_x, vadd(_x, LINKS[_i])))
PAIR_CELL = {v: k for k, v in CELL_PAIR.items()}
ACTOR_CELLS = defaultdict(list)
for _c in range(NCELL):
    for _a in CELL_PAIR[_c]:
        ACTOR_CELLS[_a].append(_c)


def share_an_actor(c, d):
    return bool(CELL_PAIR[c] & CELL_PAIR[d])


# ---------------------------------------------------------------------------
# the ring alphabet (1/3)Z[w] of modulus at most 1, as integer numerators
# ---------------------------------------------------------------------------


def ring_alphabet(bound=6):
    return [(a, b) for a in range(-bound, bound + 1)
            for b in range(-bound, bound + 1) if absq((a, b)) <= 9]


# ===========================================================================
# SECTION 4.  THE POOL -- the arena's own coin family, rebuilt
# ===========================================================================


def coin_census():
    """the S_3-covariant coins over the arena's own (1/3)Z[w].  A coin
    covariant under the arena's direction-relabelling group is a*I + b*J;
    unitarity gives |a|^2 = 1 and a conj(b) + conj(a) b + 3|b|^2 = 0.  Over
    the ring the solution set is finite and this rebuild is gated against the
    coupled machine's own committed census."""
    alpha = ring_alphabet()
    units = [u for u in alpha if absq(u) == 9]
    sols = []
    for A in alpha:
        if absq(A) != 9:
            continue
        for B in alpha:
            t = zadd(zmul(A, zconj(B)), zmul(zconj(A), B))
            if t[1] != 0:
                raise GateFail("G-POOL-REBUILT :: the trace is not rational")
            if t[0] + 3 * absq(B) == 0:
                sols.append((A, B))
    classes = {}
    for (A, B) in sols:
        nA = zmul(A, zconj(A))
        nB = zmul(B, zconj(A))
        key = ((nA[0] // 3, nA[1] // 3), (nB[0] // 3, nB[1] // 3))
        classes.setdefault(key, []).append((A, B))
    return alpha, units, sols, classes


def coin_matrix(A, B):
    """3C = (a+b) on the diagonal and b off it, as integer numerators."""
    return tuple(tuple(zadd(B, A) if i == j else B for j in range(3))
                 for i in range(3))


def walk_operator(A, B):
    """THE COMMITTED WALK, at the welded landing record.  C_t(x) = M . D_t(x)
    with D_t(x) = diag(w^{n_l(x)}); the landing record is n = 1 at all 27
    cells, so D = w * I and the coin is w * M.  The shift carries the l
    component of site x to site x + l:  W[(x+l, l), (x, l')] = w * M[l][l'].
    Entries are integer numerators over the common denominator 3."""
    M = coin_matrix(A, B)
    W = [[Z0] * NCELL for _ in range(NCELL)]
    for s in range(9):
        for l in range(3):
            t = SITE_INDEX[vadd(SITES[s], LINKS[l])]
            for lp in range(3):
                W[cell(t, l)][cell(s, lp)] = zmul(W1, M[l][lp])
    return tuple(tuple(row) for row in W)


WPOW = ((1, 0), (0, 1), (-1, -1))          # w^0, w^1, w^2 = -1 - w
RECORD_PROBES = (
    ("N-ALL-ZERO", tuple(0 for _c in range(NCELL))),
    ("N-ALL-TWO", tuple(2 for _c in range(NCELL))),
    ("N-CELL-INDEX-MOD-3", tuple(_c % 3 for _c in range(NCELL))),
    ("N-SITE-INDEX-MOD-3", tuple(CELL_SITE[_c] % 3 for _c in range(NCELL))),
)


def walk_operator_at(A, B, nfield):
    """THE COMMITTED WALK AT AN ARBITRARY COUNT FIELD.  The record enters the
    walk only as D(n) = diag(w^{n(c)}) on the SOURCE cell, so W(n) = W_shift .
    D(n) with D(n) a diagonal of unit-modulus ring elements.  This is the
    object the record-blindness theorem is about (K2 R1/S-E2): a unit-modulus
    diagonal cannot turn a zero into a nonzero, so the whole leak census is a
    function of the walk's ZERO PATTERN and the record cannot move it."""
    M = coin_matrix(A, B)
    W = [[Z0] * NCELL for _ in range(NCELL)]
    for s in range(9):
        for l in range(3):
            t = SITE_INDEX[vadd(SITES[s], LINKS[l])]
            for lp in range(3):
                src = cell(s, lp)
                W[cell(t, l)][src] = zmul(WPOW[nfield[src] % 3], M[l][lp])
    return tuple(tuple(row) for row in W)


def support_pattern(W):
    return tuple(tuple(1 if W[i][j] != Z0 else 0 for j in range(NCELL))
                 for i in range(NCELL))


def is_unitary(W, den2=9):
    """W* W = I exactly, at the declared denominator: per COLUMN PAIR."""
    bad = 0
    for i in range(NCELL):
        for j in range(NCELL):
            acc = Z0
            for k in range(NCELL):
                acc = zadd(acc, zmul(W[k][i], zconj(W[k][j])))
            want = (den2 if i == j else 0, 0)
            if acc != want:
                bad += 1
    return bad


def is_monomial(W):
    return all(sum(1 for j in range(NCELL) if W[i][j] != Z0) <= 1
               for i in range(NCELL))


def row_supports(W):
    return [sum(1 for j in range(NCELL) if W[i][j] != Z0)
            for i in range(NCELL)]


# ===========================================================================
# SECTION 5.  THE DECLARATIONS -- (grain, ceiling), their configuration
# spaces, the free lift into both exchange shapes, and the leak census
# ===========================================================================
# A DECLARATION is a pair (GRAIN, CEILING).  The GRAIN names what is counted:
# the CARRIER (a cell, which IS a co-division pair of actors) or the ACTOR
# (a site, which lies in six cells).  The CEILING is how many excitations one
# object of that grain may hold.  Nothing in the committed layers declares
# either coordinate -- that is what SECTION 7 measures -- so all four are
# constructed here and each is carried as a DECLARATION, never as a finding.

DECLARATIONS = [
    ("D-CARRIER-2", "CARRIER", 2,
     "two excitations may share a cell: the free lift, unrestricted"),
    ("D-CARRIER-1", "CARRIER", 1,
     "at most one excitation per cell -- the hard core AT THE CARRIER'S OWN "
     "GRAIN, which is the grain paper-22's arena had"),
    ("D-ACTOR-1", "ACTOR", 1,
     "at most one excitation per ACTOR: no two excitations on cells that "
     "share an actor -- the hard core at the grain the weld's ACTOR->SITE "
     "leg speaks"),
    ("D-ACTOR-2", "ACTOR", 2,
     "at most two excitations per actor, which at two excitations forbids "
     "nothing"),
]
DECLARATION_IDS = [d[0] for d in DECLARATIONS]

SHAPES = ("ANTISYMMETRIC", "SYMMETRIC")


def all_configs():
    """the two-excitation configurations of the FREE lift, before any
    ceiling: unordered pairs of distinct cells, plus the doubly occupied
    cells (which only the symmetric shape carries)."""
    distinct = [frozenset(p) for p in combinations(range(NCELL), 2)]
    doubled = [frozenset([c]) for c in range(NCELL)]
    return distinct, doubled


GRAINS = ("CARRIER", "SITE", "ACTOR")


def declared_load(grain, cells):
    """THE LOAD A CONFIGURATION PUTS ON THE HEAVIEST OBJECT OF ITS DECLARED
    GRAIN.  A grain is a map from the carrier into the objects a ceiling
    counts: the CARRIER's own cells (the identity), the base SITE (a function
    of the cell) or the ACTOR (a relation -- every cell has two).  Nothing is
    special-cased here: a declaration is the predicate `load <= ceiling` and
    both of its coordinates are parameters (K1 MAJOR-2, K2 MAJOR-3)."""
    load = Counter()
    for c in cells:
        if grain == "CARRIER":
            load[("CELL", c)] += 1
        elif grain == "SITE":
            load[("SITE", CELL_SITE[c])] += 1
        else:
            for a in CELL_PAIR[c]:
                load[("ACTOR", a)] += 1
    return max(load.values()) if load else 0


def config_cells(cfg):
    """the two excitations of a configuration, as cells with multiplicity."""
    return [min(cfg), min(cfg)] if len(cfg) == 1 else sorted(cfg)


def admits(grain, ceiling, cfg):
    return declared_load(grain, config_cells(cfg)) <= ceiling


def admissible_configs(grain, ceiling, shape):
    """the configurations a declaration admits, per shape, BY EVALUATING THE
    DECLARATION'S OWN PREDICATE.  The antisymmetric shape never carries a
    doubly occupied CELL at any ceiling -- that is the wedge's own structure
    and not a declaration."""
    distinct, doubled = all_configs()
    universe = distinct + (doubled if shape == "SYMMETRIC" else [])
    return [cfg for cfg in universe if admits(grain, ceiling, cfg)]


def sector_element(W, shape, t, s):
    """the free lift U (x) U restricted to an exchange shape, entry by entry.
    Normalisation constants of the symmetrised basis are positive rationals
    and cannot change a zero into a nonzero, so the census reads the
    unnormalised entries and says so."""
    tl = sorted(t) if len(t) == 2 else [min(t), min(t)]
    sl = sorted(s) if len(s) == 2 else [min(s), min(s)]
    a, b = tl
    c, d = sl
    t1 = zmul(W[a][c], W[b][d])
    t2 = zmul(W[a][d], W[b][c])
    return zsub(t1, t2) if shape == "ANTISYMMETRIC" else zadd(t1, t2)


def leak_census(W, grain, ceiling, shape):
    """THE LEAK, per declaration and per shape, BY TWO INDEPENDENT ROUTES.

    ROUTE 1 evaluates the lifted matrix element and tests it against zero in
    the ring.  ROUTE 2 never forms the element: it counts the (target,
    source) cells at which AT LEAST ONE of the two products is nonzero, and
    separately counts the cells at which BOTH are -- the only cells at which
    a cancellation could make route 1 and route 2 disagree.  The two routes
    are gated equal per declaration, and the both-nonzero count is published
    beside them, so the agreement is a measurement and not an assumption."""
    adm = set(admissible_configs(grain, ceiling, shape))
    distinct, doubled = all_configs()
    universe = distinct + (doubled if shape == "SYMMETRIC" else [])
    forbidden = [c for c in universe if c not in adm]
    cells = 0
    supp = 0
    both = 0
    sources = set()
    targets = set()
    for s in sorted(adm, key=lambda f: sorted(f)):
        sl = sorted(s) if len(s) == 2 else [min(s), min(s)]
        c, d = sl
        for t in forbidden:
            tl = sorted(t) if len(t) == 2 else [min(t), min(t)]
            a, b = tl
            t1 = zmul(W[a][c], W[b][d])
            t2 = zmul(W[a][d], W[b][c])
            if t1 != Z0 and t2 != Z0:
                both += 1
            if t1 != Z0 or t2 != Z0:
                supp += 1
            v = zsub(t1, t2) if shape == "ANTISYMMETRIC" else zadd(t1, t2)
            if v != Z0:
                cells += 1
                sources.add(s)
                targets.add(t)
    return {"admissible": len(adm), "forbidden": len(forbidden),
            "leak_cells": cells, "support_route_cells": supp,
            "both_products_nonzero": both,
            "routes_agree": cells == supp,
            "leaking_sources": len(sources), "targets_reached": len(targets),
            "closed": cells == 0,
            "source_set": sorted(tuple(sorted(s)) for s in sources),
            "target_set": sorted(tuple(sorted(t)) for t in targets)}


def one_excitation_space(grain, ceiling):
    """the cells a declaration's own admissible two-excitation configurations
    occupy -- the carrier of its one-excitation restriction, and a function of
    the DECLARATION alone."""
    space = set()
    for sh in SHAPES:
        for cfg in admissible_configs(grain, ceiling, sh):
            space |= set(cfg)
    return tuple(sorted(space))


def one_excitation_object(W, grain, ceiling):
    """the ONE-EXCITATION restriction of a declared two-excitation theory, as
    an OBJECT: the configuration set, the transition matrix and the Born
    shadow -- DERIVED FROM THE DECLARATION and not from the walk alone.

    The configuration set is the set of cells the declaration's own admissible
    two-excitation configurations occupy, so a declaration that forbids a cell
    outright, or a ceiling of zero, produces a DIFFERENT object and the
    comparison below has a way to fail.  (All three seats: K1 MAJOR-2, K2
    MAJOR-3, K3 MAJOR-3 -- the defect paper-22 had already repaired at its own
    K1 MINOR-3, reintroduced here and now repaired the same way.)  On the four
    DECLARED declarations every restriction is the same 27-cell object, which
    is the measured content of the row and not its construction."""
    cs = one_excitation_space(grain, ceiling)
    matrix = tuple(tuple(W[i][j] for j in cs) for i in cs)
    born = tuple(tuple(absq(W[i][j]) for j in cs) for i in cs)
    return {"configs": cs, "matrix": matrix, "born": born}


# ===========================================================================
# SECTION 6-9.  THE FOUR PREMISES
# ===========================================================================


def p1_carrier():
    """P1 -- THE BIJECTION, measured on the arena the excitations use.

    The weld's forced dictionary has TWO legs.  The first, ACTOR->SITE, is a
    bijection on nine objects.  The second, CO-DIVISION-ACTOR-PAIR->LINK, is
    a bijection on twenty-seven.  The coupled machine's state is a vector on
    the 27 CELLS, and a cell IS an unordered co-division pair -- so the leg
    that welds the excitation's own arena is the SECOND one, and the ACTOR
    leg welds a set the excitation does not live on."""
    actors = sorted(SITES)
    pairs = sorted(tuple(sorted(CELL_PAIR[c])) for c in range(NCELL))
    # ACTOR -> SITE, per object
    actor_site = {a: SITE_INDEX[a] for a in actors}
    inj = len(set(actor_site.values())) == len(actors)
    sur = set(actor_site.values()) == set(range(9))
    # CELL <-> CO-DIVISION PAIR, per object
    pair_bijection = (len(PAIR_CELL) == NCELL
                      and all(PAIR_CELL[CELL_PAIR[c]] == c
                              for c in range(NCELL)))
    # the incidence: a cell has exactly two actors, an actor lies in six cells
    inc = sorted({len(CELL_PAIR[c]) for c in range(NCELL)})
    val = sorted({len(ACTOR_CELLS[a]) for a in actors})
    cells_with_two_actors = sum(1 for c in range(NCELL)
                                if len(CELL_PAIR[c]) == 2)
    actors_with_six_cells = sum(1 for a in actors
                                if len(ACTOR_CELLS[a]) == 6)
    # the excitation -> actor map is not a function: its image has size 2
    is_function = all(len(CELL_PAIR[c]) == 1 for c in range(NCELL))
    return {
        "actors": len(actors), "carrier_cells": NCELL,
        "co_division_pairs": len(set(pairs)),
        "actor_site_injective": inj, "actor_site_surjective": sur,
        "actor_site_bijection": inj and sur,
        "pair_link_bijection": pair_bijection,
        "carrier_is_the_pair_leg": pair_bijection,
        # COUNTED, never typed (K1 MINOR-1).  The ACTOR->SITE leg's image is a
        # set of SITES and the carrier is a set of CELLS: the two are objects
        # of different KIND, so what is published is the cardinality of the
        # leg's image against the cardinality of the carrier, and not a
        # covering.
        "actor_leg_image_cardinality": len(set(actor_site.values())),
        "carrier_cardinality": NCELL,
        "actor_leg_image_and_the_carrier_are_the_same_kind": False,
        "actor_leg_covers_the_carrier":
            len(set(actor_site.values())) >= NCELL,
        "actor_leg_image_in_the_carrier": len(set(actor_site.values())),
        "cell_to_actor_valence": inc,
        "actor_to_cell_valence": val,
        "cells_with_exactly_two_actors": cells_with_two_actors,
        "actors_in_exactly_six_cells": actors_with_six_cells,
        "excitation_to_actor_is_a_function": is_function,
        "verdict": ("HOLDS-ON-THE-PAIR-LEG" if pair_bijection and inj and sur
                    else "FAILS"),
    }


def key_census(obj, acc=None):
    if acc is None:
        acc = set()
    if isinstance(obj, dict):
        for k, v in obj.items():
            acc.add(k)
            key_census(v, acc)
    elif isinstance(obj, list):
        for v in obj:
            key_census(v, acc)
    return acc


def name_census(src):
    """every NAME the committed source declares: identifiers, parameters,
    attributes and the short string constants it uses as keys.  Comments and
    prose are deliberately outside this set -- the question is what the
    grammar can REFER to, not what its author wrote in the margin."""
    tree = ast.parse(src)
    names = set()
    for n in ast.walk(tree):
        if isinstance(n, ast.Name):
            names.add(n.id)
        elif isinstance(n, ast.FunctionDef):
            names.add(n.name)
            names |= {a.arg for a in n.args.args}
        elif isinstance(n, ast.ClassDef):
            names.add(n.name)
        elif isinstance(n, ast.Attribute):
            names.add(n.attr)
        elif isinstance(n, ast.Constant) and isinstance(n.value, str) \
                and len(n.value) < 80:
            names.add(n.value)
    return names


def p2_no_occupancy_coordinate(texts, receipts):
    """P2 -- THE TURNING PREMISE, first leg: does the committed layer carry an
    occupancy coordinate at all?  The published key set of BOTH committed
    receipts and the declared name set of ALL FIVE committed sources are
    censused against the declared occupancy vocabulary, token by token and
    source by source.  The homonym `ceiling` is measured rather than
    suppressed: every occurrence must match a declared non-occupancy
    referent."""
    rows = []
    occ_hits = []
    control_hits = []
    hom_rows = []
    for sid, kind, arm in (("A-COUPREC", "receipt", "DEEPER"),
                           ("A-W3REC", "receipt", "DEEPER"),
                           ("A-COUPSRC", "source", "DEEPER"),
                           ("A-D42B1", "source", "DEEPER"),
                           ("A-D60", "source", "DEEPER"),
                           ("A-D66", "source", "DEEPER"),
                           ("A-P22REC", "receipt", "DECLARED-CONTROL")):
        if kind == "receipt":
            names = key_census(receipts[sid])
        else:
            names = name_census(texts[sid])
        hits = sorted(n for n in names
                      if any(t in n.lower() for t in OCCUPANCY_TOKENS))
        hom = sorted(n for n in names if HOMONYM_TOKEN in n.lower())
        rows.append({"source": sid, "kind": kind, "arm": arm,
                     "names": len(names), "occupancy_shaped": len(hits),
                     "examples": hits[:4], "homonym_hits": len(hom)})
        if arm == "DEEPER":
            occ_hits += [(sid, h) for h in hits]
        else:
            control_hits += [(sid, h) for h in hits]
        if hom:
            hom_rows.append({"source": sid, "hits": hom[:6],
                             "count": len(hom),
                             "declared_referent": HOMONYM_REFERENTS.get(sid)})
    deeper = [r for r in rows if r["arm"] == "DEEPER"]
    hom_undeclared = [r["source"] for r in hom_rows
                      if not r["declared_referent"]]
    return {"rows": rows, "deeper_sources": len(deeper),
            "names_censused": sum(r["names"] for r in deeper),
            "occupancy_shaped_names": len(occ_hits),
            "occupancy_hits": occ_hits,
            "control_source": "A-P22REC",
            "control_names_censused":
                sum(r["names"] for r in rows if r["arm"] != "DEEPER"),
            "control_occupancy_shaped_names": len(control_hits),
            "control_examples": sorted(h for _s, h in control_hits)[:6],
            "tokens": list(OCCUPANCY_TOKENS),
            "homonym": {"token": HOMONYM_TOKEN, "rows": hom_rows,
                        "undeclared_referents": hom_undeclared}}


def p2_state_space(coupsrc):
    """P2, second leg: THE COMMITTED STATE SPACE'S CONSTRUCTION, read from the
    committed instrument's own abstract syntax tree.  The question is whether
    a two-excitation state is CONSTRUCTIBLE there -- not whether one is used.
    Measured: the carrier's declared size, whether any function in the file
    takes an excitation-number parameter, and whether any state constructor
    is indexed by anything but a cell."""
    tree = ast.parse(coupsrc)
    dims = {}
    params = set()
    funcs = 0
    for n in ast.walk(tree):
        if isinstance(n, ast.FunctionDef):
            funcs += 1
            params |= {a.arg for a in n.args.args}
        if isinstance(n, ast.Assign) and len(n.targets) == 1 \
                and isinstance(n.targets[0], ast.Name) \
                and isinstance(n.value, ast.Constant) \
                and isinstance(n.value.value, int):
            dims[n.targets[0].id] = n.value.value
    excitation_params = sorted(p for p in params
                               if any(t in p.lower()
                                      for t in OCCUPANCY_TOKENS))
    declared_dim = dims.get("DIM")
    declared_cells = dims.get("NCELL")
    # THE CONSTRUCTOR CENSUS, MEASURED RATHER THAN ASSERTED (K1 MINOR-2).
    # Every sequence constructor of the form [x] * N is read: the ones whose
    # declared length is the carrier size are the state-carrying vectors, and
    # a PAIR object would have to be built either over a product of the cells
    # or at a length that is not the carrier's.  Both are counted.
    dim_vectors, cell_vectors, other_vectors = 0, 0, []
    pair_over_carrier, pair_elsewhere = [], []
    PAIRING = ("combinations", "combinations_with_replacement", "product",
               "permutations")
    for n in ast.walk(tree):
        if isinstance(n, ast.BinOp) and isinstance(n.op, ast.Mult):
            for a, b in ((n.left, n.right), (n.right, n.left)):
                if isinstance(a, (ast.List, ast.Tuple)) and len(a.elts) == 1 \
                        and isinstance(b, ast.Name):
                    if b.id == "DIM":
                        dim_vectors += 1
                    elif b.id == "NCELL":
                        cell_vectors += 1
                    else:
                        other_vectors.append(b.id)
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) \
                and n.func.id in PAIRING and n.args:
            arg = ast.unparse(n.args[0])
            row = "%s(%s)" % (n.func.id, arg)
            if any(t in arg for t in ("DIM", "NCELL", "cell", "CELL")):
                pair_over_carrier.append(row)
            else:
                pair_elsewhere.append(row)
    return {"functions": funcs, "parameters": len(params),
            "declared_DIM": declared_dim, "declared_NCELL": declared_cells,
            "carrier_matches_the_rebuild": declared_dim == NCELL
                                           and declared_cells == NCELL,
            "excitation_number_parameters": excitation_params,
            "state_vectors_at_the_carrier_dimension": dim_vectors,
            "sequence_constructors_at_the_carrier_size": cell_vectors,
            "sequence_constructors_at_another_declared_length":
                sorted(set(other_vectors)),
            "pair_constructors_over_the_carrier": sorted(set(pair_over_carrier)),
            "pair_constructors_over_other_objects":
                len(set(pair_elsewhere)),
            "pair_constructor_examples_elsewhere":
                sorted(set(pair_elsewhere))[:4],
            "two_excitation_constructor_present":
                bool(excitation_params) or bool(pair_over_carrier),
            "verdict": ("NOT-AVAILABLE"
                        if not excitation_params and not pair_over_carrier
                        else "PRESENT")}


def p2_fiber(pool):
    """P2, third leg: THE DECLARATION FIBER over the committed layer.  Four
    declarations are constructed; their two-excitation configuration spaces
    are compared as SETS, and their one-excitation restrictions are compared
    AS OBJECTS -- configuration set, transition matrix and Born shadow, entry
    by entry, at every coin class.  The restriction is the same object for
    every declaration, which is why nothing measurable at one excitation can
    reach the ceiling."""
    spaces = {}
    for did, grain, ceiling, _why in DECLARATIONS:
        spaces[did] = {sh: frozenset(admissible_configs(grain, ceiling, sh))
                       for sh in SHAPES}
    distinct_spaces = {}
    for did in DECLARATION_IDS:
        key = (spaces[did]["SYMMETRIC"], spaces[did]["ANTISYMMETRIC"])
        distinct_spaces.setdefault(key, []).append(did)
    collapsed = ["|".join(sorted(v)) for v in distinct_spaces.values()]
    comparisons = 0
    disagreements = []
    restriction_sizes = {}
    distinct_objects = 0
    for name, W in pool:
        objs = {}
        for did, grain, ceiling, _why in DECLARATIONS:
            objs[did] = one_excitation_object(W, grain, ceiling)
            restriction_sizes[did] = len(objs[did]["configs"])
        distinct_objects = max(distinct_objects,
                               len({digest(objs[d]) for d in DECLARATION_IDS}))
        for a, b in combinations(DECLARATION_IDS, 2):
            oa, ob = objs[a], objs[b]
            for k in ("configs", "matrix", "born"):
                va, vb = oa[k], ob[k]
                if k == "configs":
                    comparisons += len(va)
                    if va != vb:
                        disagreements.append((name, a, b, k))
                else:
                    comparisons += len(va) * (len(va[0]) if va else 0)
                    if va != vb:
                        disagreements.append((name, a, b, k))
    return {"declarations": len(DECLARATIONS),
            "one_excitation_restriction_sizes": restriction_sizes,
            "distinct_one_excitation_objects": distinct_objects,
            "distinct_two_excitation_theories": len(distinct_spaces),
            "collapsed_pairs": sorted(collapsed),
            "configuration_counts": {
                did: {sh: len(spaces[did][sh]) for sh in SHAPES}
                for did in DECLARATION_IDS},
            "one_excitation_comparisons": comparisons,
            "one_excitation_disagreements": len(disagreements),
            "restrictions_agree_as_objects": not disagreements}


def occupation_field(cfg):
    """the occupation of every cell in a two-excitation configuration."""
    o = [0] * NCELL
    if len(cfg) == 1:
        o[min(cfg)] = 2
    else:
        for c in cfg:
            o[c] = 1
    return o


def site_field(o):
    return [sum(o[cell(s, l)] for l in range(3)) for s in range(9)]


# THE COMMITTED EMISSION RULE'S DECLARED FIBER, inherited from the parent.
# paper-20 declares F10-EMISSION-READING at fiber 2 -- "the Born menu against
# the record menu; both run" -- and the committed rule is
# emission_weights(reading, Jn, n, den) with the kernel k = q/M taken at each
# site by law_transport_at(q).  Reading A takes q from the BORN vector PER
# CELL; reading B takes q from the RECORD counts.  OCC declares the fiber
# rather than inheriting it silently (K1 MAJOR-3).
EMISSION_READINGS = (
    ("A", "THE BORN MENU: q(l|x) is the state's own per-cell weight at the "
          "site, so the state enters the kernel PER CELL.  This is the "
          "reading the parent's coupled ensemble runs"),
    ("B", "THE RECORD MENU: q(l|x) is the record's own count on the cell, so "
          "the state does not enter the kernel at all"),
)


def emission_kernel(reading, field, record, s):
    """ONE SITE'S EMISSION KERNEL, by the committed rule's own formula:
    q = the declared menu at the site, M = sum(q), k = q/M (undefined when the
    menu has no mass, exactly as law_transport_at returns k = None).  Exact
    Fractions; the state-side input is the per-cell field under reading A and
    the record under reading B."""
    q = [Fraction(field[cell(s, i)]) if reading == "A"
         else Fraction(record[cell(s, i)]) for i in range(3)]
    M = sum(q)
    if M == 0:
        return None
    return tuple(qi / M for qi in q)


def kernel_str(k):
    return "NONE" if k is None else ",".join(str(x) for x in k)


def p3_closure(W, no_occupancy_coordinate_below):
    """P3 -- CLOSURE.  Can an actor carrying two excitations still divide?

    Three measurements, none of them a reading of the grammar's prose.

    (a) THE BLINDNESS PAIR AND ITS CENSUS, PER DECLARED READING.  Two
        two-excitation configurations are built: P, with two excitations on
        two DIFFERENT cells of one actor, and Q, with two excitations on ONE
        cell.  Their SITE fields agree; their CELL occupations differ.  The
        committed emission rule's two declared readings are then applied to
        them, and they do NOT agree with each other: under the RECORD menu the
        state does not enter the kernel at all, so the rule is blind; under
        the BORN menu the state enters PER CELL and the rule SEPARATES them.
        Both are measured, over a census of every doubly occupied
        configuration against every same-site partner, rather than asserted on
        one witness (K1 MAJOR-3, K2 MINOR-5).

    (b) THE COMPLETION FIBER.  The committed emission rule is a rule for ONE
        excitation.  Three completions to two are constructed and all three
        are run: per excitation, per configuration, and site-then-record.
        Their emission totals and their fields are measured.  Exactly one of
        them breaks the parent's own consistency identity -- total emission
        mass exactly 1 -- so the declaration the grammar is missing is
        verdict-relevant rather than cosmetic.

    (c) DIVISION IS NEVER REFUSED, PER COMPLETION.  Each completion's own
        field is built FOR THE DOUBLY OCCUPIED STATE and its support measured,
        so the published refusal count is a per-object read and not a
        predicate that never sees the object (K3 MAJOR-6, #87)."""
    c0 = cell(SITE_INDEX[(0, 0)], 0)
    c1 = cell(SITE_INDEX[(0, 0)], 1)
    P = frozenset([c0, c1])
    Q = frozenset([c0])
    oP, oQ = occupation_field(P), occupation_field(Q)
    sP, sQ = site_field(oP), site_field(oQ)
    site_agree = sum(1 for i in range(9) if sP[i] == sQ[i])
    cell_agree = sum(1 for i in range(NCELL) if oP[i] == oQ[i])

    # (a) THE TWO DECLARED READINGS, on the witness pair and then as a census.
    # The record is the welded landing record, count one at every cell.
    record = [1] * NCELL
    s0 = CELL_SITE[c0]
    readings = []
    for rid, why in EMISSION_READINGS:
        kP = emission_kernel(rid, oP, record, s0)
        kQ = emission_kernel(rid, oQ, record, s0)
        readings.append({"reading": rid, "why": why,
                         "kernel_on_P": kernel_str(kP),
                         "kernel_on_Q": kernel_str(kQ),
                         "separates_the_witness_pair": kP != kQ})
    # the census: every doubly occupied configuration against every one of its
    # same-site partners -- the pairs the ceiling's question turns on
    census_rows = 0
    site_blind = 0
    sep = {rid: 0 for rid, _w in EMISSION_READINGS}
    for c in range(NCELL):
        s = CELL_SITE[c]
        oq = occupation_field(frozenset([c]))
        for d, e in combinations([cell(s, i) for i in range(3)], 2):
            op = occupation_field(frozenset([d, e]))
            census_rows += 1
            if site_field(op) == site_field(oq):
                site_blind += 1
            for rid, _w in EMISSION_READINGS:
                if emission_kernel(rid, op, record, s) != \
                        emission_kernel(rid, oq, record, s):
                    sep[rid] += 1
    blindness_census = {
        "pairs": census_rows,
        "site_field_cannot_separate": site_blind,
        "rows": [{"reading": rid, "separates": sep[rid], "pairs": census_rows}
                 for rid, _w in EMISSION_READINGS],
        "readings": len(EMISSION_READINGS)}

    # one step of the symmetric lift from each declared start configuration
    distinct, doubled = all_configs()
    universe = distinct + doubled

    def step(start):
        amps = {}
        for t in universe:
            v = sector_element(W, "SYMMETRIC", t, start)
            if v != Z0:
                amps[t] = v
        tot = sum(absq(v) for v in amps.values())
        occf = [0] * NCELL
        for t, v in amps.items():
            w = absq(v)
            if len(t) == 1:
                occf[min(t)] += 2 * w
            else:
                a, b = sorted(t)
                occf[a] += w
                occf[b] += w
        return tot, occf

    # E1 per excitation; E2 per configuration, one event; E3 site then record
    def complete(occf, tot):
        """the three completions, as ONE function of a state's own weight
        field, so the SAME construction runs on P and on Q (K3 MAJOR-6)."""
        e1 = [Fraction(o, tot) for o in occf]
        e2 = [Fraction(o, 2 * tot) for o in occf]
        sm = [sum(e2[cell(s, l)] for l in range(3)) for s in range(9)]
        e3 = [sm[c // 3] * Fraction(1, 3) for c in range(NCELL)]
        return [e1, e2, e3]

    COMPLETION_IDS = [
        ("E1-PER-EXCITATION",
         "each excitation emits through the committed one-excitation rule"),
        ("E2-PER-CONFIGURATION",
         "one event per step, drawn from the pair's own joint weight"),
        ("E3-SITE-THEN-RECORD",
         "the site from the marginal, the link from the record menu"),
    ]
    total, occ = step(P)
    qtotal, qocc = step(Q)
    fields = complete(occ, total)
    qfields = complete(qocc, qtotal)
    completions = [(cid, fields[i], why)
                   for i, (cid, why) in enumerate(COMPLETION_IDS)]
    rows = []
    for i, (cid, why) in enumerate(COMPLETION_IDS):
        tot = sum(fields[i])
        qtot = sum(qfields[i])
        rows.append({"completion": cid, "why": why,
                     "emission_total": str(tot),
                     "preserves_the_parent_identity": tot == 1,
                     "support": sum(1 for f in fields[i] if f != 0),
                     # THE Q-SIDE, built for the doubly occupied state itself
                     "emission_total_on_the_doubly_occupied_state": str(qtot),
                     "support_on_the_doubly_occupied_state":
                         sum(1 for f in qfields[i] if f != 0),
                     "refuses_a_division_to_the_doubly_occupied_state":
                         all(f == 0 for f in qfields[i])})
    diffs = []
    for (ai, (an, af, _w1)), (bi, (bn, bf, _w2)) in combinations(
            list(enumerate(completions)), 2):
        diffs.append({"pair": "%s|%s" % (an, bn),
                      "cells_differing":
                          sum(1 for i in range(NCELL) if af[i] != bf[i])})
    # (c) the doubly occupied carrier still emits, PER COMPLETION
    refusals = sum(1 for r in rows
                   if r["refuses_a_division_to_the_doubly_occupied_state"])
    menus_nonempty = sum(
        1 for r in rows if r["support_on_the_doubly_occupied_state"] > 0)
    # P3's WORD IS DERIVED FROM ITS THREE LEGS, never typed (K1 MINOR-4,
    # K3 MINOR-7).  The legs are: the grammar has no occupancy coordinate to
    # condition on (P2's own vocabulary census, handed in); no completion
    # refuses a division to the doubly occupied state; and every completion
    # leaves that state's emission menu nonempty.
    legs = {"no_occupancy_coordinate_to_condition_on":
                bool(no_occupancy_coordinate_below),
            "completions_that_refuse": refusals,
            "completions_whose_menu_is_nonempty": menus_nonempty,
            "completions": len(rows)}
    if refusals > 0:
        derived = "CLOSURE-REQUIRED"
    elif legs["no_occupancy_coordinate_to_condition_on"] \
            and menus_nonempty == len(rows):
        derived = "SILENT-AND-VACUOUSLY-SATISFIED"
    else:
        derived = "CLOSURE-AVAILABLE"
    return {
        "blindness_pair": {
            "P": sorted(P), "Q": sorted(Q),
            # COUNTED, never typed: the site field's own length
            "site_fields_agree_at": site_agree, "sites": len(sP),
            "cell_occupations_agree_at": cell_agree, "cells": NCELL,
            "the_site_field_can_separate_them": site_agree != 9},
        "emission_readings": readings,
        "emission_reading_fiber": len(EMISSION_READINGS),
        "readings_that_separate_the_witness_pair":
            sum(1 for r in readings if r["separates_the_witness_pair"]),
        "blindness_census": blindness_census,
        "completions": rows,
        "completion_fiber": len(rows),
        "completions_preserving_the_parent_identity":
            sum(1 for r in rows if r["preserves_the_parent_identity"]),
        "pairwise_field_differences": diffs,
        "doubly_occupied_carrier_emits": qtotal > 0 and menus_nonempty > 0,
        "completions_whose_menu_is_nonempty": menus_nonempty,
        "completions_that_refuse_a_division": refusals,
        "legs": legs,
        "verdict": derived,
    }


def p4_pool(pool, p22rec):
    """P4 -- THE POOL, at both grains, on every member of the arena's own coin
    family, with paper-22's split CITED from its committed rows.

    The gate binds GENERATORS, not the tally: every coin class carries its own
    leak row at every declaration and its own monomiality predicate."""
    rows = []
    for name, W in pool:
        mono = is_monomial(W)
        entry = {"coin": name, "monomial": mono,
                 "row_supports": sorted(set(row_supports(W)))}
        for did, grain, ceiling, _why in DECLARATIONS:
            for sh in SHAPES:
                r = leak_census(W, grain, ceiling, sh)
                entry["%s|%s" % (did, sh)] = {
                    "leak_cells": r["leak_cells"], "closed": r["closed"],
                    "admissible": r["admissible"],
                    "forbidden": r["forbidden"],
                    "leaking_sources": r["leaking_sources"],
                    "targets_reached": r["targets_reached"],
                    "routes_agree": r["routes_agree"],
                    "both_products_nonzero": r["both_products_nonzero"]}
        rows.append(entry)
    # paper-22's split, CITED: computed from its own committed rows
    p22 = p22rec["occupancy"]
    leaking = sum(1 for r in p22["rows"]
                  if r["symmetric_hardcore_leak_cells"] > 0)
    closed = sum(1 for r in p22["rows"]
                 if r["symmetric_hardcore_leak_cells"] == 0)
    anti = sum(1 for r in p22["rows"]
               if r["antisymmetric_hardcore_leak_cells"] > 0)
    return {"rows": rows, "coins": len(rows),
            "parent_split": {"generators": len(p22["rows"]),
                             "symmetric_leaking": leaking,
                             "symmetric_closed": closed,
                             "antisymmetric_leaking": anti,
                             "cited_from": "A-P22REC occupancy/rows"}}


def selection_census(p4rows):
    """WHICH DECLARATION SELECTS A SHAPE, per coin and per declaration: a
    declaration selects when EXACTLY ONE shape closes on it."""
    out = []
    for row in p4rows:
        for did, _g, _c, _why in DECLARATIONS:
            closed = [sh for sh in SHAPES
                      if row["%s|%s" % (did, sh)]["closed"]]
            out.append({"coin": row["coin"], "declaration": did,
                        "shapes_closed": closed,
                        "selects": len(closed) == 1,
                        "selected": closed[0] if len(closed) == 1 else None,
                        "no_shape_closes": len(closed) == 0})
    return out


# ===========================================================================
# SECTION 10.  THE ARMS -- the head law, exercised on six arenas
# ===========================================================================
# The two-way control the pin requires lives here: an arena where the seed
# conditional demonstrably FIRES (a subset-valued carrier, where double
# occupancy is not expressible) and one where it demonstrably FAILS (the same
# carrier with multiset configurations, where it is).  Both are DECLARED
# CONTROLS and neither is this unit's verdict arena.


def control_matrix(n):
    """the declared control generator on n carriers: (2/n)J - I, exactly
    unitary and, for n > 1, with every entry nonzero.  Carried as integer
    numerators over the denominator n in the same Z[w] representation the
    committed walk uses, so the SAME census code runs on it."""
    return tuple(tuple((2 - n, 0) if i == j else (2, 0) for j in range(n))
                 for i in range(n))


def control_unitary(M, n):
    bad = 0
    for i in range(n):
        for j in range(n):
            acc = Z0
            for k in range(n):
                acc = zadd(acc, zmul(M[k][i], zconj(M[k][j])))
            if acc != ((n * n if i == j else 0), 0):
                bad += 1
    return bad


def control_leak(M, n, rule, shape):
    """the leak of a control arena: the free lift restricted to a shape, out
    of the configurations the declared REPRESENTATION carries.  Under the
    SUBSET rule a doubly occupied carrier is not expressible at all; under
    the MULTISET rule it is."""
    distinct = [frozenset(p) for p in combinations(range(n), 2)]
    doubled = [frozenset([c]) for c in range(n)]
    universe = distinct + (doubled if shape == "SYMMETRIC" else [])
    if shape == "ANTISYMMETRIC":
        adm = list(distinct)
    else:
        adm = distinct + (doubled if rule == "MULTISET" else [])
    forb = [c for c in universe if c not in set(adm)]
    cells = 0
    for s in adm:
        sl = sorted(s) if len(s) == 2 else [min(s), min(s)]
        c, d = sl
        for t in forb:
            tl = sorted(t) if len(t) == 2 else [min(t), min(t)]
            a, b = tl
            t1 = zmul(M[a][c], M[b][d])
            t2 = zmul(M[a][d], M[b][c])
            v = zsub(t1, t2) if shape == "ANTISYMMETRIC" else zadd(t1, t2)
            if v != Z0:
                cells += 1
    return {"admissible": len(adm), "forbidden": len(forb),
            "leak_cells": cells, "closed": cells == 0,
            "dimension": len(adm)}


def control_arena(name, n, rule):
    M = control_matrix(n)
    rows = {}
    for sh in SHAPES:
        rows[sh] = control_leak(M, n, rule, sh)
    closed = [sh for sh in SHAPES
              if rows[sh]["closed"] and rows[sh]["dimension"] > 0]
    posable = all(rows[sh]["dimension"] > 0 for sh in SHAPES)
    return {"arena": name, "carriers": n, "rule": rule,
            "unitarity_violations": control_unitary(M, n),
            "monomial": is_monomial_n(M, n),
            "shapes": rows, "shapes_closed": closed,
            "posable": posable,
            "selects": posable and len(closed) == 1,
            "no_shape_closes": posable and len(closed) == 0}


def is_monomial_n(M, n):
    return all(sum(1 for j in range(n) if M[i][j] != Z0) <= 1
               for i in range(n))


OUTCOMES = ("OCC-CEILING-FORCED", "OCC-CEILING-OPEN", "OCC-CEILING-PARTIAL",
            "OCC-BLOCKED-AT")


def head_law(p1_ok, p2, p3, p4, posable):
    """THE HEAD LAW.  Derived from the four premise verdicts and nothing else;
    typed in one place, and re-derived independently by the comparator."""
    if not posable:
        return "OCC-BLOCKED-AT"
    if p2 in ("NOT-AVAILABLE", "CONSTRUCTIBLE"):
        return "OCC-CEILING-OPEN"
    if (p2 == "STRUCTURAL-EXCLUSION" and p1_ok
            and p3 == "CLOSURE-AVAILABLE" and p4 == "SELECTS"):
        return "OCC-CEILING-FORCED"
    return "OCC-CEILING-PARTIAL"


def p4_word(sel_rows, did):
    rows = [r for r in sel_rows if r["declaration"] == did]
    if any(r["no_shape_closes"] for r in rows):
        return "NO-SHAPE-CLOSES"
    if any(r["selects"] for r in rows):
        return "SELECTS"
    return "DOES-NOT-SELECT"


def build_arms(p1, p2s, p3, sel_rows, controls):
    arms = []
    p1_ok = p1["verdict"] == "HOLDS-ON-THE-PAIR-LEG"
    arms.append({
        "arm": "A0-COMMITTED-COUPLED-MACHINE", "role": "THE VERDICT ARENA",
        "p1": p1["verdict"], "p2": p2s["verdict"], "p3": p3["verdict"],
        "p4": p4_word(sel_rows, "D-ACTOR-1"),
        "posable": True,
        "why": "the committed layers as they stand: no declaration is added "
               "and the premise chain is measured on them"})
    arms.append({
        "arm": "A1-DECLARED-EXCLUSION-AT-THE-CARRIER-GRAIN",
        "role": "declared", "p1": p1["verdict"], "p2": "DECLARED-EXCLUSION",
        "p3": p3["verdict"], "p4": p4_word(sel_rows, "D-CARRIER-1"),
        "posable": True,
        "why": "the hard core declared at the grain the excitation's own "
               "coordinate has"})
    arms.append({
        "arm": "A2-DECLARED-EXCLUSION-AT-THE-ACTOR-GRAIN",
        "role": "declared", "p1": p1["verdict"], "p2": "DECLARED-EXCLUSION",
        "p3": p3["verdict"], "p4": p4_word(sel_rows, "D-ACTOR-1"),
        "posable": True,
        "why": "the hard core declared at the grain the weld's ACTOR->SITE "
               "leg speaks"})
    for c in controls:
        if c["arena"] == "C1-SUBSET-CARRIER":
            arms.append({
                "arm": "A3-" + c["arena"], "role": "CONTROL: IT CAN FIRE",
                "p1": "HOLDS-BY-CONSTRUCTION",
                "p2": "STRUCTURAL-EXCLUSION", "p3": "CLOSURE-AVAILABLE",
                "p4": "SELECTS" if c["selects"] else "DOES-NOT-SELECT",
                "posable": c["posable"],
                "why": "a carrier whose configurations are SUBSETS: double "
                       "occupancy is not expressible, and exactly one shape "
                       "closes"})
        elif c["arena"] == "C2-MULTISET-CARRIER":
            arms.append({
                "arm": "A4-" + c["arena"], "role": "CONTROL: IT CAN FAIL",
                "p1": "HOLDS-BY-CONSTRUCTION", "p2": "CONSTRUCTIBLE",
                "p3": "CLOSURE-AVAILABLE",
                "p4": "SELECTS" if c["selects"] else "DOES-NOT-SELECT",
                "posable": c["posable"],
                "why": "the same carrier with MULTISET configurations: "
                       "double occupancy is constructible and both shapes "
                       "close"})
        else:
            arms.append({
                "arm": "A5-" + c["arena"], "role": "CONTROL: DEGENERATE",
                "p1": "HOLDS-BY-CONSTRUCTION", "p2": "STRUCTURAL-EXCLUSION",
                "p3": "CLOSURE-AVAILABLE",
                "p4": "SELECTS" if c["selects"] else "DOES-NOT-SELECT",
                "posable": c["posable"],
                "why": "one carrier: the antisymmetric shape is empty and "
                       "the comparison is not posable"})
    for a in arms:
        a["word"] = head_law(a["p1"] in ("HOLDS-ON-THE-PAIR-LEG",
                                         "HOLDS-BY-CONSTRUCTION"),
                             a["p2"], a["p3"], a["p4"], a["posable"])
    return arms


def asymmetry_row(sel_rows):
    """THE ASYMMETRY, measured against both arms: a declaration that FORBIDS
    can select a shape, one that PERMITS cannot -- and the refinement this
    arena adds, that exclusion selects only at the carrier's own grain."""
    perm = [r for r in sel_rows
            if r["declaration"] in ("D-CARRIER-2", "D-ACTOR-2")]
    excl = [r for r in sel_rows
            if r["declaration"] in ("D-CARRIER-1", "D-ACTOR-1")]
    excl_carrier = [r for r in excl if r["declaration"] == "D-CARRIER-1"]
    excl_actor = [r for r in excl if r["declaration"] == "D-ACTOR-1"]
    return {
        "permission_rows": len(perm),
        "permission_rows_that_select": sum(1 for r in perm if r["selects"]),
        "exclusion_rows": len(excl),
        "exclusion_rows_that_select": sum(1 for r in excl if r["selects"]),
        "exclusion_at_the_carrier_grain_selects":
            sum(1 for r in excl_carrier if r["selects"]),
        "exclusion_at_the_carrier_grain_rows": len(excl_carrier),
        "exclusion_at_the_actor_grain_selects":
            sum(1 for r in excl_actor if r["selects"]),
        "exclusion_at_the_actor_grain_rows": len(excl_actor),
        "actor_grain_rows_where_no_shape_closes":
            sum(1 for r in excl_actor if r["no_shape_closes"]),
        "selected_shapes": sorted({r["selected"] for r in sel_rows
                                   if r["selected"]}),
        "statement": "exclusion can select a shape and permission cannot -- "
                     "and exclusion selects only at the carrier's own grain",
    }


# ===========================================================================
# SECTION 11.  THE MEMO -- fingerprinted, so no injection can survive it
# ===========================================================================

_CENSUS = {"value": None, "fingerprint": None, "builds": 0, "hits": 0}


def census(builder):
    if _CENSUS["value"] is None:
        _CENSUS["value"] = builder()
        _CENSUS["fingerprint"] = digest(_CENSUS["value"])
        _CENSUS["builds"] += 1
    else:
        if digest(_CENSUS["value"]) != _CENSUS["fingerprint"]:
            raise GateFail("G-MEMO-CLEAN :: the memo's contents moved between "
                           "runs")
        _CENSUS["hits"] += 1
    return json.loads(json.dumps(_CENSUS["value"], default=str))


# ===========================================================================
# SECTION 12.  THE TOTAL GATE-TIME SEAL (#119 + the #148 totality addendum)
# ===========================================================================

SEALED_PATHS = [
    ("SEAL-SCHEMA", "schema", "G-PROVENANCE"),
    ("SEAL-PROVENANCE", "provenance", "G-PROVENANCE"),
    ("SEAL-ARITHMETIC", "arithmetic", "G-EXACT-ARITHMETIC"),
    ("SEAL-PYTHON", "python", "G-EXACT-ARITHMETIC"),
    ("SEAL-OBJECT-READS", "object_reads", "G-READS-DECLARED"),
    ("SEAL-VERBATIM", "verbatim_anchors", "G-VERBATIM"),
    ("SEAL-PATH-VALUES", "path_value_anchors", "G-PATH-VALUES"),
    ("SEAL-ARENA", "arena", "G-P1-CARRIER"),
    ("SEAL-P1", "p1", "G-P1-DICTIONARY"),
    ("SEAL-POOL", "pool", "G-POOL-UNITARY"),
    ("SEAL-LEAKS", "leaks", "G-LEAK-ROUTES"),
    ("SEAL-P2", "p2", "G-P2-TURNING"),
    ("SEAL-P3", "p3", "G-P3-NEVER-REFUSED"),
    ("SEAL-P4", "p4", "G-P4-PARENT-SPLIT"),
    ("SEAL-SELECTION", "selection", "G-P4-GRAIN-CENSUS"),
    ("SEAL-ARMS", "arms", "G-ARMS-REACHABILITY"),
    ("SEAL-CONTROLS", "controls", "G-CONTROL-TWO-WAY"),
    ("SEAL-ASYMMETRY", "asymmetry", "G-ASYMMETRY"),
    ("SEAL-STAMPS", "description_stamps", "G-DESCRIPTION-STAMPS"),
    ("SEAL-COUNTING", "counting_only", "G-COUNTING-ONLY"),
    ("SEAL-CHOICES", "choice_inventory", "G-CHOICE-INVENTORY"),
    ("SEAL-WALLS", "walls", "G-NO-PARTICLE-NAMING"),
    ("SEAL-MEMO", "memo", "G-MEMO-CLEAN"),
    ("SEAL-VERDICT", "verdict", "G-VERDICT-RECONSTRUCTED"),
    ("SEAL-VERDICT-AUDIT", "verdict_audit", "G-VERDICT-RECONSTRUCTED"),
    ("SEAL-COUNTS", "counts", "G-VERDICT-RECONSTRUCTED"),
    ("SEAL-PAPER-CLAIMS", "paper_claims", "G-PAPER-CLAIMS"),
    ("SEAL-PAPER-TABLES", "paper_tables", "G-PAPER-TABLES"),
    ("SEAL-PAPER-COVERAGE", "paper_coverage", "G-PAPER-HEAD-VERBATIM"),
    ("SEAL-POLARITY", "polarity", "G-PAPER-CLAIM-POLARITY"),
    ("SEAL-COVERAGE", "coverage", "G-COVERAGE"),
    ("SEAL-REACHABILITY", "reachability", "G-REACHABILITY"),
    ("SEAL-WAIVERS", "waiver_ledger", "G-COVERAGE"),
    ("SEAL-MUTANTS", "mutants", "G-FALSIFIER-HONESTY"),
    ("SEAL-WRITER-SHAPE", "writer_shape", "G-WRITER-SHAPE"),
    ("SEAL-MUTANT-SWEEP", "mutant_sweep", "G-SWEEP-BOUND"),
    ("SEAL-GATES", "gates", "G-PAPER-COVERAGE-FINAL"),
    ("SEAL-CLOSING", "closing_gates", "G-PAPER-COVERAGE-FINAL"),
    ("SEAL-TOTALS", "totals", "G-PAPER-COVERAGE-FINAL"),
    ("SEAL-TRANSCRIPT", "transcript_head", "G-PAPER-COVERAGE-FINAL"),
]
DECLARED_UNSEALED = ["seal_manifest", "payload_sha256_12"]
DECLARED_UNSEALED_FROZEN = ("seal_manifest", "payload_sha256_12")
UNSEALED_FORCING = {
    "seal_manifest": "carries the seal rows themselves; sealing it would seal "
                     "a digest of its own digest.  CHAINED: compared against "
                     "SEAL.rows after read-back from disk.",
    "payload_sha256_12": "is the digest of the payload the seal closes over "
                         "and is assigned after that close.  CHAINED: "
                         "compared against SEAL.payload_sha after read-back.",
}
MEASURED_KEYS = ("arena", "p1", "pool", "leaks", "p2", "p3", "p4",
                 "selection", "arms", "controls", "asymmetry", "counts",
                 "verdict")


class Seal:
    def __init__(self):
        self.rows = []
        self.index = {}
        self.payload = None
        self.payload_sha = None
        self.text_sha = None
        self.text_lines = None

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

    def close(self, obj, payload, text):
        broken = self.verify(obj)
        if broken:
            raise GateFail("G-ARTIFACT-INTEGRITY :: the payload was sealed "
                           "over a broken seal :: %s" % broken)
        self.payload = payload
        self.payload_sha = digest(payload)
        self.text_sha = digest(text)
        self.text_lines = len(text.split("\n"))


# ===========================================================================
# SECTION 13.  THE HEAVY CENSUS
# ===========================================================================


def build_census(texts, receipts):
    """everything expensive, in one JSON-safe object: the pool, the leak
    census at every declaration and shape, the declaration fiber, the closure
    measurements and the control arenas.  The falsifiers act on the GATE
    layer, above this, so a mutant costs a gate and not a rebuilt census."""
    alpha, units, sols, classes = coin_census()
    pool = []
    pool_meta = []
    for key in sorted(classes):
        A, B = key
        name = "K%s" % ("%+d%+dw" % (B[0], B[1]))
        W = walk_operator(A, B)
        pool.append((name, W))
        pool_meta.append({
            "coin": name, "a_numerator": list(A), "b_numerator": list(B),
            "members_in_the_solution_set": len(classes[key]),
            "is_grover": B == (-2, 0),
            "unitarity_violations": is_unitary(W),
            "monomial": is_monomial(W),
            "row_supports": sorted(set(row_supports(W)))})
    p2voc = p2_no_occupancy_coordinate(texts, receipts)
    p4 = p4_pool(pool, receipts["A-P22REC"])
    sel = selection_census(p4["rows"])
    # the two SET EQUALITIES, per coin
    same_actor_cfgs = sorted(
        tuple(sorted(p)) for p in
        (frozenset(q) for q in combinations(range(NCELL), 2))
        if share_an_actor(*sorted(p)))
    same_site_cfgs = sorted(
        tuple(sorted((a, b))) for a, b in combinations(range(NCELL), 2)
        if CELL_SITE[a] == CELL_SITE[b])
    same_actor_set = {tuple(x) for x in same_actor_cfgs}
    seteq = []
    for name, W in pool:
        r_carrier = leak_census(W, "CARRIER", 1, "SYMMETRIC")
        r_actor_a = leak_census(W, "ACTOR", 1, "ANTISYMMETRIC")
        r_actor_s = leak_census(W, "ACTOR", 1, "SYMMETRIC")
        srcs = [tuple(s) for s in r_carrier["source_set"]]
        leaks_here = bool(r_carrier["leak_cells"])
        seteq.append({
            "coin": name,
            "carrier_grain_leak_sources": len(r_carrier["source_set"]),
            # THE SET EQUALITY IS WITH THE SAME-SITE SET (27), and the
            # relation to the same-ACTOR set (135) is a STRICT CONTAINMENT --
            # both named, both published with their cardinalities, and the
            # key names the object it holds (all three seats: K1 MAJOR-1,
            # K2 MAJOR-1, K3 MAJOR-4).
            "carrier_grain_sources_are_the_same_site_configurations":
                (r_carrier["source_set"] == same_site_cfgs
                 if leaks_here else None),
            "carrier_grain_sources_are_the_same_actor_configurations":
                (r_carrier["source_set"] == same_actor_cfgs
                 if leaks_here else None),
            "carrier_grain_sources_inside_the_same_actor_set":
                sum(1 for s in srcs if s in same_actor_set),
            "same_actor_configurations": len(same_actor_cfgs),
            "carrier_grain_sources_are_actor_grain_forbidden":
                (all(s in same_actor_set for s in srcs) if leaks_here
                 else None),
            "carrier_grain_containment_is_strict":
                ((len(srcs) < len(same_actor_cfgs)) if leaks_here else None),
            "same_actor_configurations_excluded":
                (len(same_actor_cfgs) - len(srcs) if leaks_here else None),
            "carrier_grain_sources_share_an_actor":
                (all(s in same_actor_set for s in srcs) if leaks_here
                 else None),
            "actor_grain_shape_leak_sets_coincide":
                (r_actor_a["source_set"] == r_actor_s["source_set"]
                 and r_actor_a["target_set"] == r_actor_s["target_set"]
                 and r_actor_a["leak_cells"] == r_actor_s["leak_cells"]),
            "actor_grain_both_products_nonzero":
                r_actor_a["both_products_nonzero"],
            "actor_grain_leak_cells": r_actor_a["leak_cells"],
            "actor_grain_sources_leaking": r_actor_a["leaking_sources"],
            "actor_grain_targets_reached": r_actor_a["targets_reached"]})
    controls = [control_arena("C1-SUBSET-CARRIER", 9, "SUBSET"),
                control_arena("C2-MULTISET-CARRIER", 9, "MULTISET"),
                control_arena("C3-ONE-CARRIER", 1, "SUBSET")]

    # ---- K2's THREE STRENGTHENINGS, adopted and measured here -------------
    # (i) THE MECHANISM THEOREM.  Under a hard core at grain G the
    # ANTISYMMETRIC sector's forbidden set is {distinct pairs colliding under
    # G}, which is EMPTY IF AND ONLY IF G is the carrier's own grain.  That is
    # why the automatic closure which makes exclusion SELECTIVE can live at
    # the carrier's grain and structurally nowhere else.  Measured over the
    # three grains the arena admits, per object.
    n_distinct = len(all_configs()[0])
    wedge = []
    for g in GRAINS:
        adm_a = admissible_configs(g, 1, "ANTISYMMETRIC")
        adm_s = admissible_configs(g, 1, "SYMMETRIC")
        wedge.append({
            "grain": g,
            "is_the_carrier_grain": g == "CARRIER",
            "antisymmetric_admissible": len(adm_a),
            "antisymmetric_forbidden": n_distinct - len(adm_a),
            "antisymmetric_forbidden_set_is_empty":
                n_distinct - len(adm_a) == 0,
            "symmetric_admissible": len(adm_s)})
    wedge_theorem_holds = all(
        r["antisymmetric_forbidden_set_is_empty"] == r["is_the_carrier_grain"]
        for r in wedge)
    # (ii) THE THIRD GRAIN.  CELL_SITE is a genuine FUNCTION from cells to
    # nine objects -- unlike the ACTOR "grain", which is a relation -- so it
    # is a declarable grain the delivered two-point menu did not carry.  The
    # head's ONLY is tested against it: does a hard core at the site grain
    # select a shape?
    site_rows = []
    for name, W in pool:
        rs = leak_census(W, "SITE", 1, "SYMMETRIC")
        ra = leak_census(W, "SITE", 1, "ANTISYMMETRIC")
        closed = [sh for sh, r in (("SYMMETRIC", rs), ("ANTISYMMETRIC", ra))
                  if r["closed"]]
        site_rows.append({
            "coin": name, "admissible": rs["admissible"],
            "symmetric_leak_cells": rs["leak_cells"],
            "antisymmetric_leak_cells": ra["leak_cells"],
            "shapes_closed": closed, "selects": len(closed) == 1,
            "no_shape_closes": len(closed) == 0})
    # (iii) RECORD BLINDNESS.  The count field enters the walk only as a
    # unit-modulus DIAGONAL on the source cell, so it cannot turn a zero into
    # a nonzero: the whole leak census is a function of the walk's zero
    # pattern.  Measured, not argued -- the support pattern and every one of
    # the 48 leak rows are recomputed at each declared probe field.
    probe_rows = []
    for pname, nfield in RECORD_PROBES:
        support_same = 0
        rows_same = 0
        rows_total = 0
        for (name, W), meta in zip(pool, pool_meta):
            A = tuple(meta["a_numerator"])
            B = tuple(meta["b_numerator"])
            Wn = walk_operator_at(A, B, nfield)
            if support_pattern(Wn) == support_pattern(W):
                support_same += 1
            base = [r for r in p4["rows"] if r["coin"] == name][0]
            for did, grain, ceiling, _why in DECLARATIONS:
                for sh in SHAPES:
                    rows_total += 1
                    rn = leak_census(Wn, grain, ceiling, sh)
                    b = base["%s|%s" % (did, sh)]
                    if (rn["leak_cells"] == b["leak_cells"]
                            and rn["leaking_sources"] == b["leaking_sources"]
                            and rn["targets_reached"] == b["targets_reached"]
                            and rn["both_products_nonzero"]
                            == b["both_products_nonzero"]):
                        rows_same += 1
        probe_rows.append({
            "count_field": pname, "coins": len(pool),
            "support_patterns_identical": support_same,
            "leak_rows_identical": rows_same, "leak_rows": rows_total})
    landing_identity = all(
        walk_operator_at(tuple(m["a_numerator"]), tuple(m["b_numerator"]),
                         tuple(1 for _c in range(NCELL))) == W
        for (name, W), m in zip(pool, pool_meta))
    return {
        "coin_census": {"alphabet": len(alpha), "units": len(units),
                        "ring_solutions": len(sols),
                        "classes_up_to_phase": len(classes),
                        "grover_classes": sum(1 for k in classes
                                              if k[1] == (-2, 0))},
        "pool": pool_meta,
        "leaks": p4["rows"],
        "parent_split": p4["parent_split"],
        "selection": sel,
        "set_equalities": seteq,
        "same_actor_configurations": len(same_actor_cfgs),
        "same_site_configurations": len(same_site_cfgs),
        "p1": p1_carrier(),
        "p2_vocabulary": p2voc,
        "p2_state_space": p2_state_space(texts["A-COUPSRC"]),
        "p2_fiber": p2_fiber(pool),
        "p3": p3_closure(
            pool[[m["coin"] for m in pool_meta].index(
                [m["coin"] for m in pool_meta if m["is_grover"]][0])][1],
            p2voc["occupancy_shaped_names"] == 0),
        "controls": controls,
        "wedge_theorem": {
            "rows": wedge, "grains": len(GRAINS),
            "empty_iff_the_carrier_grain": wedge_theorem_holds,
            "statement": "under a hard core at grain G the antisymmetric "
                         "sector's forbidden set is the set of distinct-cell "
                         "pairs that collide under G, and it is empty if and "
                         "only if G is the carrier's own grain -- so the "
                         "automatic closure that makes exclusion SELECTIVE "
                         "exists at the carrier's grain and structurally "
                         "nowhere else"},
        "site_grain_arm": {
            "grain": "SITE", "ceiling": 1, "rows": site_rows,
            "coins": len(site_rows),
            "admissible": site_rows[0]["admissible"],
            "coins_that_select": sum(1 for r in site_rows if r["selects"]),
            "coins_where_no_shape_closes":
                sum(1 for r in site_rows if r["no_shape_closes"]),
            "why": "CELL_SITE is a FUNCTION from the 27 cells onto nine "
                   "objects, unlike the actor relation, so it is a third "
                   "declarable grain; the head's ONLY is tested against it "
                   "rather than left as a two-point census (K2 R1)"},
        "record_blindness": {
            "probes": probe_rows, "probe_fields": len(probe_rows),
            "landing_record_identity": landing_identity,
            "family_size": "3^%d" % NCELL,
            "why": "the count field enters the walk only as D(n) = "
                   "diag(w^{n(c)}), a unit-modulus diagonal on the source "
                   "cell, so it cannot turn a zero into a nonzero and the "
                   "leak census is a function of the zero pattern alone; the "
                   "measured probes are the theorem's instances (K2 S-E2)"},
    }


# ===========================================================================
# SECTION 14.  THE VERDICT -- built from a declared field spec, audited by a
# DE-TWINNED comparator (the SMU lesson: two routes that type the same
# template audit the template, not the measurement)
# ===========================================================================

THESIS_VOCABULARY = {
    "T-CARRIER-PAIR": "THE-EXCITATION-RIDES-THE-CO-DIVISION-PAIR-"
                      "NOT-THE-ACTOR",
    "T-CARRIER-ACTOR": "THE-EXCITATION-RIDES-THE-ACTOR",
    "T-GRAIN-CARRIER": "EXCLUSION-SELECTS-ONLY-AT-THE-CARRIER-S-OWN-GRAIN",
    "T-GRAIN-ANY": "EXCLUSION-SELECTS-AT-EVERY-GRAIN",
}


def thesis_carrier(p1):
    """the carrier thesis is SELECTED by a measured predicate, not typed."""
    return ("T-CARRIER-ACTOR" if p1["excitation_to_actor_is_a_function"]
            else "T-CARRIER-PAIR")


def thesis_grain(asym, site_arm):
    """the grain thesis is SELECTED by the measured selection census at every
    grain coarser than the carrier -- the actor grain of the declared menu and
    the site grain K2's review added -- and not typed."""
    return ("T-GRAIN-ANY"
            if (asym["exclusion_at_the_actor_grain_selects"] > 0
                or site_arm["coins_that_select"] > 0)
            else "T-GRAIN-CARRIER")


def pair(a, b):
    return "%s-OF-%s" % (a, b)


def versus(a, b):
    """two cardinalities of DIFFERENT KIND, compared as cardinalities and not
    as a covering (K1 MINOR-1)."""
    return "%s-VS-%s" % (a, b)


def field_spec(R):
    """THE DECLARED FIELD SPEC.  Every field of the head names a receipt path;
    the builder reads it, and the comparator re-reads it through its own map.
    No prose is concatenated anywhere: the head is a sequence of
    LABEL=VALUE fields, which is what lets the audit route PARSE rather than
    re-emit."""
    p1 = R["p1"]
    po = R["pool"]
    lk = R["leaks"]
    p2 = R["p2"]
    p3 = R["p3"]
    p4 = R["p4"]
    aw = R["asymmetry"]
    ar = R["arms"]
    return [
        ("OCC-CARRIER", [
            ("THESIS", THESIS_VOCABULARY[thesis_carrier(p1)]),
            ("CARRIER-CELLS", p1["carrier_cells"]),
            ("CO-DIVISION-PAIRS", p1["co_division_pairs"]),
            ("CELL-IS-A-CO-DIVISION-PAIR", p1["pair_link_bijection"]),
            ("ACTOR-SITE-BIJECTION", pair(p1["actors"], p1["actors"])),
            ("ACTOR-LEG-IMAGE-CARDINALITY-AGAINST-THE-CARRIER",
             versus(p1["actor_leg_image_cardinality"],
                    p1["carrier_cardinality"])),
            ("CELLS-WITH-EXACTLY-TWO-ACTORS",
             pair(p1["cells_with_exactly_two_actors"], p1["carrier_cells"])),
            ("ACTORS-IN-EXACTLY-SIX-CELLS",
             pair(p1["actors_in_exactly_six_cells"], p1["actors"])),
            ("EXCITATION-TO-ACTOR-IS-A-FUNCTION",
             p1["excitation_to_actor_is_a_function"]),
            ("P1", p1["verdict"]),
        ]),
        ("OCC-POOL-AND-GRAIN", [
            ("THESIS", THESIS_VOCABULARY[thesis_grain(
                aw, lk["site_grain_arm"])]),
            ("COIN-CLASSES", po["classes_up_to_phase"]),
            ("RING-SOLUTIONS", po["ring_solutions"]),
            ("NON-MONOMIAL-COINS", pair(po["non_monomial"], po["coins"])),
            ("CARRIER-GRAIN-SYMMETRIC-LEAK-CELLS",
             lk["carrier_grain_symmetric_leak_cells"]),
            ("CARRIER-GRAIN-COINS-LEAKING",
             pair(lk["carrier_grain_symmetric_coins_leaking"], po["coins"])),
            ("CARRIER-GRAIN-ANTISYMMETRIC-LEAK-CELLS",
             lk["carrier_grain_antisymmetric_leak_cells"]),
            ("CARRIER-GRAIN-ANTISYMMETRIC-FORBIDDEN-CONFIGURATIONS",
             lk["carrier_grain_antisymmetric_forbidden_configurations"]),
            ("CARRIER-GRAIN-LEAK-SOURCES-ARE-THE-SAME-SITE-CONFIGURATIONS",
             pair(lk["carrier_grain_set_equality_coins"],
                  lk["carrier_grain_symmetric_coins_leaking"])),
            ("CARRIER-GRAIN-LEAK-SOURCES-ARE-THE-SAME-ACTOR-CONFIGURATIONS",
             pair(lk["carrier_grain_same_actor_equality_coins"],
                  lk["carrier_grain_symmetric_coins_leaking"])),
            ("CARRIER-GRAIN-LEAK-SOURCES-ARE-ACTOR-GRAIN-FORBIDDEN",
             pair(lk["carrier_grain_leak_sources"],
                  lk["same_actor_configurations"])),
            ("CARRIER-GRAIN-CONTAINMENT-IS-STRICT",
             pair(lk["carrier_grain_strict_containment_coins"],
                  lk["carrier_grain_symmetric_coins_leaking"])),
            ("SAME-ACTOR-CONFIGURATIONS-EXCLUDED",
             lk["same_actor_configurations_excluded"]),
            ("ACTOR-GRAIN-COINS-WHERE-BOTH-SHAPES-LEAK",
             pair(lk["actor_grain_both_shapes_leak_coins"], po["coins"])),
            ("ACTOR-GRAIN-LEAK-CELLS-NON-MONOMIAL",
             lk["actor_grain_leak_cells_non_monomial"]),
            ("ACTOR-GRAIN-LEAK-CELLS-MONOMIAL",
             lk["actor_grain_leak_cells_monomial"]),
            ("ACTOR-GRAIN-SHAPE-LEAK-SETS-COINCIDE",
             pair(lk["actor_grain_shape_sets_coincide_coins"], po["coins"])),
            ("ACTOR-GRAIN-CANCELLATION-CELLS",
             lk["actor_grain_cancellation_cells"]),
            ("ACTOR-GRAIN-SOURCES-LEAKING-MAX",
             pair(lk["actor_grain_sources_leaking_max"],
                  lk["actor_grain_admissible"])),
            ("ACTOR-GRAIN-SOURCES-LEAKING-MIN",
             pair(lk["actor_grain_sources_leaking_min"],
                  lk["actor_grain_admissible"])),
            ("ACTOR-GRAIN-TARGETS-REACHED-MAX",
             pair(lk["actor_grain_targets_reached_max"],
                  lk["actor_grain_forbidden"])),
            ("ACTOR-GRAIN-TARGETS-REACHED-MIN",
             pair(lk["actor_grain_targets_reached_min"],
                  lk["actor_grain_forbidden"])),
            ("ACTOR-GRAIN-COINS-WHERE-EVERY-ADMISSIBLE-SOURCE-LEAKS",
             pair(lk["actor_grain_coins_where_every_admissible_source_leaks"],
                  po["coins"])),
            ("ACTOR-GRAIN-COINS-WHERE-EVERY-FORBIDDEN-TARGET-IS-REACHED",
             pair(lk["actor_grain_coins_where_every_forbidden_target_is_"
                     "reached"], po["coins"])),
            ("WEDGE-FORBIDDEN-SET-EMPTY-IFF-THE-CARRIER-GRAIN",
             pair(sum(1 for r in lk["wedge_theorem"]["rows"]
                      if r["antisymmetric_forbidden_set_is_empty"]
                      == r["is_the_carrier_grain"]),
                  lk["wedge_theorem"]["grains"])),
            ("SITE-GRAIN-COINS-THAT-SELECT",
             pair(lk["site_grain_arm"]["coins_that_select"],
                  lk["site_grain_arm"]["coins"])),
            ("SITE-GRAIN-COINS-WHERE-NO-SHAPE-CLOSES",
             pair(lk["site_grain_arm"]["coins_where_no_shape_closes"],
                  lk["site_grain_arm"]["coins"])),
            ("P4-IS-RECORD-BLIND-AT-THE-PROBED-COUNT-FIELDS",
             pair(sum(1 for r in lk["record_blindness"]["probes"]
                      if r["leak_rows_identical"] == r["leak_rows"]),
                  lk["record_blindness"]["probe_fields"])),
            ("LEAK-ROUTES-AGREE",
             pair(lk["route_rows_agreeing"], lk["route_rows"])),
            ("PARENT-SPLIT-CITED",
             pair(p4["parent_split"]["symmetric_leaking"],
                  p4["parent_split"]["generators"])),
        ]),
        (R["counts"]["outcome_word"], [
            ("P1", p1["verdict"]),
            ("P2", p2["verdict"]),
            ("P2-NAMES-CENSUSED", p2["vocabulary"]["names_censused"]),
            ("P2-OCCUPANCY-SHAPED-NAMES",
             p2["vocabulary"]["occupancy_shaped_names"]),
            ("P2-DECLARATION-FIBER",
             pair(p2["fiber"]["distinct_two_excitation_theories"],
                  p2["fiber"]["declarations"])),
            ("P2-ONE-EXCITATION-RESTRICTIONS-AGREE",
             pair(p2["fiber"]["one_excitation_comparisons"]
                  - p2["fiber"]["one_excitation_disagreements"],
                  p2["fiber"]["one_excitation_comparisons"])),
            ("P3", p3["verdict"]),
            ("P3-EMISSION-READING-FIBER", p3["emission_reading_fiber"]),
            ("P3-BLINDNESS-PAIR-SITE-FIELDS-AGREE",
             pair(p3["blindness_pair"]["site_fields_agree_at"],
                  p3["blindness_pair"]["sites"])),
            ("P3-SITE-FIELD-CANNOT-SEPARATE",
             pair(p3["blindness_census"]["site_field_cannot_separate"],
                  p3["blindness_census"]["pairs"])),
            ("P3-RECORD-MENU-READING-SEPARATES",
             pair([r for r in p3["blindness_census"]["rows"]
                   if r["reading"] == "B"][0]["separates"],
                  p3["blindness_census"]["pairs"])),
            ("P3-BORN-MENU-READING-SEPARATES",
             pair([r for r in p3["blindness_census"]["rows"]
                   if r["reading"] == "A"][0]["separates"],
                  p3["blindness_census"]["pairs"])),
            ("P3-COMPLETIONS-PRESERVING-THE-PARENT-IDENTITY",
             pair(p3["completions_preserving_the_parent_identity"],
                  p3["completion_fiber"])),
            ("P3-COMPLETIONS-THAT-REFUSE-A-DIVISION",
             pair(p3["completions_that_refuse_a_division"],
                  p3["completion_fiber"])),
            ("P4", R["counts"]["p4_word"]),
            ("ASYMMETRY-PERMISSION-ROWS-THAT-SELECT",
             pair(aw["permission_rows_that_select"], aw["permission_rows"])),
            ("ASYMMETRY-EXCLUSION-ROWS-THAT-SELECT",
             pair(aw["exclusion_rows_that_select"], aw["exclusion_rows"])),
            ("ASYMMETRY-AT-THE-ACTOR-GRAIN",
             pair(aw["exclusion_at_the_actor_grain_selects"],
                  aw["exclusion_at_the_actor_grain_rows"])),
            ("ARMS", pair(R["counts"]["distinct_outcome_words"], len(ar))),
            ("CONTROL-CAN-FIRE", R["counts"]["control_fires"]),
            ("CONTROL-CAN-FAIL", R["counts"]["control_fails"]),
            ("SEED-CONDITIONAL", R["counts"]["seed_conditional"]),
            ("FIBER-PRICED", R["counts"]["fiber_priced"]),
            ("SCOPE", SCOPE_ROW),
        ]),
    ]


# THE SEED CONDITIONAL'S OWN VERDICT, in the adjudicated words (K2 R2): it
# does not denote at the carrier, AND when its injection premise is supplied
# as a declaration at the grain it typed -- arm A2 -- its conclusion fails.
SEED_CONDITIONAL_WORD = ("MISTYPED-AT-THE-CARRIER;"
                         "REFUTED-AT-THE-GRAIN-IT-TYPED")

SCOPE_ROW = ("TWO-EXCITATIONS-ONLY;ONE-RECORD;THE-WELDED-LANDING-RECORD;"
             "P4-IS-RECORD-BLIND-OVER-THE-COUNT-FIELD-FAMILY;"
             "FREE-LIFT-ONLY(U-TENSOR-U);GRAIN-MENU-AS-DECLARED;"
             "SHAPE-WORDS-ONLY;NO-PARTICLE-CLAIM;NO-BRAID-CLAIM;"
             "NO-GENERAL-N-CLAIM;NO-CONFIGURATION-MEASURE;"
             "COUNTS-ARE-COUNTING-ONLY;NO-CONTINUUM-CLAIM;"
             "THE-CEILING-IS-NOT-DECLARED-BY-THIS-UNIT-EITHER")


def render_field(v):
    if isinstance(v, bool):
        return "YES" if v else "NO"
    return str(v)


def build_verdict(R):
    segs = {}
    for name, fields in field_spec(R):
        body = "; ".join("%s=%s" % (lab, render_field(val))
                         for lab, val in fields)
        segs[name] = "%s<%s>" % (name, body)
    if mut("MUT-VERDICT-WORD"):
        old = R["counts"]["outcome_word"]
        segs["OCC-CEILING-FORCED"] = segs.pop(old).replace(
            old + "<", "OCC-CEILING-FORCED<", 1)
    if mut("MUT-VERDICT-VALUE"):
        k = "OCC-CARRIER"
        segs[k] = segs[k].replace("CARRIER-CELLS=27", "CARRIER-CELLS=26")
    if mut("MUT-VERDICT-CLAUSE"):
        k = "OCC-POOL-AND-GRAIN"
        segs[k] = segs[k].split("; ACTOR-GRAIN-CANCELLATION-CELLS")[0] + ">"
    return segs


SEG_RE = re.compile(r"^([A-Z0-9\-]+)<(.*)>$", re.S)


def reconstruct(serialized, segs):
    """THE COMPARATOR, DE-TWINNED.  It types no copy of the head template.
    It PARSES the delivered segments into fields, looks each label up in ITS
    OWN map from label to receipt path, and compares the delivered value with
    the value it reads out of the serialized receipt.  It re-derives the
    outcome word from the premise rows by its own copy of the head law, and
    it re-derives each segment's thesis from the measured predicate that
    selects it.  Finally it requires every numeral in the head to occur among
    the receipt's own measured values, so a typed literal cannot survive."""
    D = json.loads(serialized)
    p1, p2, p3 = D["p1"], D["p2"], D["p3"]
    aw, lk, po = D["asymmetry"], D["leaks"], D["pool"]
    # --- the outcome word, re-derived from the premise rows
    verdict_arm = [a for a in D["arms"] if a["role"] == "THE VERDICT ARENA"][0]
    ok1 = verdict_arm["p1"] in ("HOLDS-ON-THE-PAIR-LEG",
                                "HOLDS-BY-CONSTRUCTION")
    if not verdict_arm["posable"]:
        word = "OCC-BLOCKED-AT"
    elif verdict_arm["p2"] in ("NOT-AVAILABLE", "CONSTRUCTIBLE"):
        word = "OCC-CEILING-OPEN"
    elif (verdict_arm["p2"] == "STRUCTURAL-EXCLUSION" and ok1
          and verdict_arm["p3"] == "CLOSURE-AVAILABLE"
          and verdict_arm["p4"] == "SELECTS"):
        word = "OCC-CEILING-FORCED"
    else:
        word = "OCC-CEILING-PARTIAL"
    # --- the theses, re-derived from their own selecting predicates
    th_c = ("THE-EXCITATION-RIDES-THE-ACTOR"
            if p1["excitation_to_actor_is_a_function"]
            else "THE-EXCITATION-RIDES-THE-CO-DIVISION-PAIR-NOT-THE-ACTOR")
    th_g = ("EXCLUSION-SELECTS-AT-EVERY-GRAIN"
            if (aw["exclusion_at_the_actor_grain_selects"] > 0
                or lk["site_grain_arm"]["coins_that_select"] > 0)
            else "EXCLUSION-SELECTS-ONLY-AT-THE-CARRIER-S-OWN-GRAIN")
    # --- the label map, typed HERE and nowhere else
    want = {
        "OCC-CARRIER": {
            "THESIS": th_c,
            "CARRIER-CELLS": p1["carrier_cells"],
            "CO-DIVISION-PAIRS": p1["co_division_pairs"],
            "CELL-IS-A-CO-DIVISION-PAIR":
                "YES" if p1["pair_link_bijection"] else "NO",
            "ACTOR-SITE-BIJECTION": "%d-OF-%d" % (p1["actors"], p1["actors"]),
            "ACTOR-LEG-IMAGE-CARDINALITY-AGAINST-THE-CARRIER":
                "%d-VS-%d" % (p1["actor_leg_image_cardinality"],
                              p1["carrier_cardinality"]),
            "CELLS-WITH-EXACTLY-TWO-ACTORS":
                "%d-OF-%d" % (p1["cells_with_exactly_two_actors"],
                              p1["carrier_cells"]),
            "ACTORS-IN-EXACTLY-SIX-CELLS":
                "%d-OF-%d" % (p1["actors_in_exactly_six_cells"],
                              p1["actors"]),
            "EXCITATION-TO-ACTOR-IS-A-FUNCTION":
                "YES" if p1["excitation_to_actor_is_a_function"] else "NO",
            "P1": p1["verdict"]},
        "OCC-POOL-AND-GRAIN": {
            "THESIS": th_g,
            "COIN-CLASSES": po["classes_up_to_phase"],
            "RING-SOLUTIONS": po["ring_solutions"],
            "NON-MONOMIAL-COINS": "%d-OF-%d" % (po["non_monomial"],
                                                po["coins"]),
            "CARRIER-GRAIN-SYMMETRIC-LEAK-CELLS":
                lk["carrier_grain_symmetric_leak_cells"],
            "CARRIER-GRAIN-COINS-LEAKING":
                "%d-OF-%d" % (lk["carrier_grain_symmetric_coins_leaking"],
                              po["coins"]),
            "CARRIER-GRAIN-ANTISYMMETRIC-LEAK-CELLS":
                lk["carrier_grain_antisymmetric_leak_cells"],
            "CARRIER-GRAIN-ANTISYMMETRIC-FORBIDDEN-CONFIGURATIONS":
                lk["carrier_grain_antisymmetric_forbidden_configurations"],
            "CARRIER-GRAIN-LEAK-SOURCES-ARE-THE-SAME-SITE-CONFIGURATIONS":
                "%d-OF-%d" % (lk["carrier_grain_set_equality_coins"],
                              lk["carrier_grain_symmetric_coins_leaking"]),
            "CARRIER-GRAIN-LEAK-SOURCES-ARE-THE-SAME-ACTOR-CONFIGURATIONS":
                "%d-OF-%d" % (lk["carrier_grain_same_actor_equality_coins"],
                              lk["carrier_grain_symmetric_coins_leaking"]),
            "CARRIER-GRAIN-LEAK-SOURCES-ARE-ACTOR-GRAIN-FORBIDDEN":
                "%d-OF-%d" % (lk["carrier_grain_leak_sources"],
                              lk["same_actor_configurations"]),
            "CARRIER-GRAIN-CONTAINMENT-IS-STRICT":
                "%d-OF-%d" % (lk["carrier_grain_strict_containment_coins"],
                              lk["carrier_grain_symmetric_coins_leaking"]),
            "SAME-ACTOR-CONFIGURATIONS-EXCLUDED":
                lk["same_actor_configurations_excluded"],
            "ACTOR-GRAIN-COINS-WHERE-BOTH-SHAPES-LEAK":
                "%d-OF-%d" % (lk["actor_grain_both_shapes_leak_coins"],
                              po["coins"]),
            "ACTOR-GRAIN-LEAK-CELLS-NON-MONOMIAL":
                lk["actor_grain_leak_cells_non_monomial"],
            "ACTOR-GRAIN-LEAK-CELLS-MONOMIAL":
                lk["actor_grain_leak_cells_monomial"],
            "ACTOR-GRAIN-SHAPE-LEAK-SETS-COINCIDE":
                "%d-OF-%d" % (lk["actor_grain_shape_sets_coincide_coins"],
                              po["coins"]),
            "ACTOR-GRAIN-CANCELLATION-CELLS":
                lk["actor_grain_cancellation_cells"],
            "ACTOR-GRAIN-SOURCES-LEAKING-MAX":
                "%d-OF-%d" % (lk["actor_grain_sources_leaking_max"],
                              lk["actor_grain_admissible"]),
            "ACTOR-GRAIN-SOURCES-LEAKING-MIN":
                "%d-OF-%d" % (lk["actor_grain_sources_leaking_min"],
                              lk["actor_grain_admissible"]),
            "ACTOR-GRAIN-TARGETS-REACHED-MAX":
                "%d-OF-%d" % (lk["actor_grain_targets_reached_max"],
                              lk["actor_grain_forbidden"]),
            "ACTOR-GRAIN-TARGETS-REACHED-MIN":
                "%d-OF-%d" % (lk["actor_grain_targets_reached_min"],
                              lk["actor_grain_forbidden"]),
            "ACTOR-GRAIN-COINS-WHERE-EVERY-ADMISSIBLE-SOURCE-LEAKS":
                "%d-OF-%d" % (
                    lk["actor_grain_coins_where_every_admissible_source_"
                       "leaks"], po["coins"]),
            "ACTOR-GRAIN-COINS-WHERE-EVERY-FORBIDDEN-TARGET-IS-REACHED":
                "%d-OF-%d" % (
                    lk["actor_grain_coins_where_every_forbidden_target_is_"
                       "reached"], po["coins"]),
            "WEDGE-FORBIDDEN-SET-EMPTY-IFF-THE-CARRIER-GRAIN":
                "%d-OF-%d" % (
                    sum(1 for r in lk["wedge_theorem"]["rows"]
                        if r["antisymmetric_forbidden_set_is_empty"]
                        == r["is_the_carrier_grain"]),
                    lk["wedge_theorem"]["grains"]),
            "SITE-GRAIN-COINS-THAT-SELECT":
                "%d-OF-%d" % (lk["site_grain_arm"]["coins_that_select"],
                              lk["site_grain_arm"]["coins"]),
            "SITE-GRAIN-COINS-WHERE-NO-SHAPE-CLOSES":
                "%d-OF-%d" % (
                    lk["site_grain_arm"]["coins_where_no_shape_closes"],
                    lk["site_grain_arm"]["coins"]),
            "P4-IS-RECORD-BLIND-AT-THE-PROBED-COUNT-FIELDS":
                "%d-OF-%d" % (
                    sum(1 for r in lk["record_blindness"]["probes"]
                        if r["leak_rows_identical"] == r["leak_rows"]),
                    lk["record_blindness"]["probe_fields"]),
            "LEAK-ROUTES-AGREE": "%d-OF-%d" % (lk["route_rows_agreeing"],
                                               lk["route_rows"]),
            "PARENT-SPLIT-CITED":
                "%d-OF-%d" % (D["p4"]["parent_split"]["symmetric_leaking"],
                              D["p4"]["parent_split"]["generators"])},
        word: {
            "P1": p1["verdict"], "P2": p2["verdict"],
            "P2-NAMES-CENSUSED": p2["vocabulary"]["names_censused"],
            "P2-OCCUPANCY-SHAPED-NAMES":
                p2["vocabulary"]["occupancy_shaped_names"],
            "P2-DECLARATION-FIBER":
                "%d-OF-%d" % (p2["fiber"]["distinct_two_excitation_theories"],
                              p2["fiber"]["declarations"]),
            "P2-ONE-EXCITATION-RESTRICTIONS-AGREE":
                "%d-OF-%d" % (p2["fiber"]["one_excitation_comparisons"]
                              - p2["fiber"]["one_excitation_disagreements"],
                              p2["fiber"]["one_excitation_comparisons"]),
            "P3": p3["verdict"],
            "P3-EMISSION-READING-FIBER": p3["emission_reading_fiber"],
            "P3-BLINDNESS-PAIR-SITE-FIELDS-AGREE":
                "%d-OF-%d" % (p3["blindness_pair"]["site_fields_agree_at"],
                              p3["blindness_pair"]["sites"]),
            "P3-SITE-FIELD-CANNOT-SEPARATE":
                "%d-OF-%d" % (
                    p3["blindness_census"]["site_field_cannot_separate"],
                    p3["blindness_census"]["pairs"]),
            "P3-RECORD-MENU-READING-SEPARATES":
                "%d-OF-%d" % ([r for r in p3["blindness_census"]["rows"]
                               if r["reading"] == "B"][0]["separates"],
                              p3["blindness_census"]["pairs"]),
            "P3-BORN-MENU-READING-SEPARATES":
                "%d-OF-%d" % ([r for r in p3["blindness_census"]["rows"]
                               if r["reading"] == "A"][0]["separates"],
                              p3["blindness_census"]["pairs"]),
            "P3-COMPLETIONS-PRESERVING-THE-PARENT-IDENTITY":
                "%d-OF-%d" % (
                    p3["completions_preserving_the_parent_identity"],
                    p3["completion_fiber"]),
            "P3-COMPLETIONS-THAT-REFUSE-A-DIVISION":
                "%d-OF-%d" % (p3["completions_that_refuse_a_division"],
                              p3["completion_fiber"]),
            "P4": D["counts"]["p4_word"],
            "ASYMMETRY-PERMISSION-ROWS-THAT-SELECT":
                "%d-OF-%d" % (aw["permission_rows_that_select"],
                              aw["permission_rows"]),
            "ASYMMETRY-EXCLUSION-ROWS-THAT-SELECT":
                "%d-OF-%d" % (aw["exclusion_rows_that_select"],
                              aw["exclusion_rows"]),
            "ASYMMETRY-AT-THE-ACTOR-GRAIN":
                "%d-OF-%d" % (aw["exclusion_at_the_actor_grain_selects"],
                              aw["exclusion_at_the_actor_grain_rows"]),
            "ARMS": "%d-OF-%d" % (D["counts"]["distinct_outcome_words"],
                                  len(D["arms"])),
            "CONTROL-CAN-FIRE": D["counts"]["control_fires"],
            "CONTROL-CAN-FAIL": D["counts"]["control_fails"],
            "SEED-CONDITIONAL": D["counts"]["seed_conditional"],
            "FIBER-PRICED": D["counts"]["fiber_priced"],
            "SCOPE": D["counts"]["scope_row"]},
    }
    bad = []
    parsed = {}
    for name, text in sorted(segs.items()):
        m = SEG_RE.match(text.strip())
        if not m:
            bad.append("%s: unparseable" % name)
            continue
        head, body = m.group(1), m.group(2)
        if head != name:
            bad.append("%s: head %s" % (name, head))
        fields = {}
        for part in body.split("; "):
            if "=" not in part:
                bad.append("%s: fieldless %r" % (name, part[:24]))
                continue
            lab, val = part.split("=", 1)
            fields[lab] = val
        parsed[head] = fields
    for name, wants in want.items():
        got = parsed.get(name)
        if got is None:
            bad.append("%s: segment missing" % name)
            continue
        if set(got) != set(wants):
            bad.append("%s: labels %s" % (name, sorted(
                set(got) ^ set(wants))))
        for lab, val in wants.items():
            if lab in got and got[lab] != str(val):
                bad.append("%s/%s: %r vs %r" % (name, lab, got[lab], str(val)))
    return {"outcome_word_rederived": word, "field_mismatches": bad,
            "segments_parsed": sorted(parsed),
            "fields_checked": sum(len(v) for v in want.values())}


def head_numerals(segs):
    out = set()
    for text in segs.values():
        for t in re.findall(r"\d+", text):
            out.add(t)
    return out


# ===========================================================================
# SECTION 15.  THE PAPER GATES
# ===========================================================================


def com(n):
    return "{:,}".format(n)


def paper_claims(R):
    p1, p2, p3, lk, aw = R["p1"], R["p2"], R["p3"], R["leaks"], R["asymmetry"]
    po, c = R["pool"], R["counts"]
    return [
        ("C01", "the coupled machine's carrier is %d cells, and a cell IS an "
                "unordered co-division pair of actors: the two sets are in "
                "bijection at %d of %d" % (p1["carrier_cells"],
                                           p1["co_division_pairs"],
                                           p1["carrier_cells"])),
        ("C02", "every cell carries exactly two actors at %d of %d, and every "
                "actor lies in exactly six cells at %d of %d"
                % (p1["cells_with_exactly_two_actors"], p1["carrier_cells"],
                   p1["actors_in_exactly_six_cells"], p1["actors"])),
        ("C03", "the weld's ACTOR->SITE leg is a bijection at %d of %d, and "
                "its image has %d members against the carrier's %d -- two "
                "cardinalities of different kind, since the leg's image is a "
                "set of sites and the carrier is a set of cells"
                % (p1["actors"], p1["actors"],
                   p1["actor_leg_image_cardinality"],
                   p1["carrier_cardinality"])),
        ("C04", "%d published names across the %d committed layers beneath "
                "the excitations, and none of them is occupancy-shaped, while "
                "the same scan fires at %d names on the one layer that "
                "declared a ceiling"
                % (p2["vocabulary"]["names_censused"],
                   p2["vocabulary"]["deeper_sources"],
                   p2["vocabulary"]["control_occupancy_shaped_names"])),
        ("C05", "%d declarations give %d distinct two-excitation theories, and "
                "their one-excitation restrictions agree as objects at %s of "
                "%s comparisons"
                % (p2["fiber"]["declarations"],
                   p2["fiber"]["distinct_two_excitation_theories"],
                   com(p2["fiber"]["one_excitation_comparisons"]),
                   com(p2["fiber"]["one_excitation_comparisons"]))),
        ("C06", "under the record-menu reading the state does not enter the "
                "committed emission rule's kernel at all and the rule cannot "
                "separate any of the %d pairs, while under the Born-menu "
                "reading -- the one the parent's coupled ensemble runs -- it "
                "enters per cell and separates %d of %d"
                % (p3["blindness_census"]["pairs"],
                   [r for r in p3["blindness_census"]["rows"]
                    if r["reading"] == "A"][0]["separates"],
                   p3["blindness_census"]["pairs"])),
        ("C07", "%d of the %d completions preserve the parent's own emission "
                "identity, and %d of %d refuse a division to a doubly "
                "occupied carrier"
                % (p3["completions_preserving_the_parent_identity"],
                   p3["completion_fiber"],
                   p3["completions_that_refuse_a_division"],
                   p3["completion_fiber"])),
        ("C08", "at the carrier's own grain the symmetric shape leaks at %d "
                "cells at %d of the %d coin classes and the antisymmetric "
                "shape leaks at %d"
                % (lk["carrier_grain_symmetric_leak_cells"],
                   lk["carrier_grain_symmetric_coins_leaking"], po["coins"],
                   lk["carrier_grain_antisymmetric_leak_cells"])),
        ("C09", "the configurations that leak are exactly the %d whose two "
                "excitations sit on two of the three cells of one site -- a "
                "set equality at %d of %d leaking coin classes -- and every "
                "one of them is among the %d configurations the actor-grain "
                "declaration forbids, a containment that is strict at %d of "
                "%d and excludes %d of them"
                % (R["counts"]["same_site_configurations"],
                   lk["carrier_grain_set_equality_coins"],
                   lk["carrier_grain_symmetric_coins_leaking"],
                   lk["same_actor_configurations"],
                   lk["carrier_grain_strict_containment_coins"],
                   lk["carrier_grain_symmetric_coins_leaking"],
                   lk["same_actor_configurations_excluded"])),
        ("C10", "at the actor's grain both shapes leak at %d of %d coin "
                "classes; at the %d non-monomial classes every one of the %d "
                "admissible configurations leaks and every one of the %d "
                "forbidden configurations is reached, and at the monomial "
                "class %d of %d leak and %d of %d are reached"
                % (lk["actor_grain_both_shapes_leak_coins"], po["coins"],
                   lk["actor_grain_coins_where_every_admissible_source_"
                      "leaks"],
                   lk["actor_grain_admissible"], lk["actor_grain_forbidden"],
                   lk["actor_grain_sources_leaking_min"],
                   lk["actor_grain_admissible"],
                   lk["actor_grain_targets_reached_min"],
                   lk["actor_grain_forbidden"])),
        ("C11", "the two shapes' leak sets coincide cell for cell at %d of %d "
                "coin classes, and no cell of either carries two nonzero "
                "products, at %d"
                % (lk["actor_grain_shape_sets_coincide_coins"], po["coins"],
                   lk["actor_grain_cancellation_cells"])),
        ("C12", "permission selects a shape at %d of %d rows and exclusion at "
                "%d of %d, all of them at the carrier's own grain"
                % (aw["permission_rows_that_select"], aw["permission_rows"],
                   aw["exclusion_rows_that_select"], aw["exclusion_rows"])),
        ("C13", "the head law returns %d different pre-registered outcome "
                "words across the %d arenas"
                % (c["distinct_outcome_words"], len(R["arms"]))),
        ("C14", "paper-22's split is cited from its own rows: the symmetric "
                "shape leaks at %d of its %d generators"
                % (R["p4"]["parent_split"]["symmetric_leaking"],
                   R["p4"]["parent_split"]["generators"])),
        ("C15", "the two routes agree at %d of %d leak rows"
                % (lk["route_rows_agreeing"], lk["route_rows"])),
        # THE ABSTRACT AND THE ARENA SECTION, BROUGHT INSIDE THE INSTRUMENT
        # (K3 MAJOR-2).  The four sentences a reader quotes were the four a
        # reviewer could corrupt at exit 0, because the abstract paraphrases
        # the body: each is now assembled from this run and required to occur
        # exactly once, so the numbers it carries are bound where they are
        # read rather than only where they were derived.
        ("C16", "they give %d distinct two-excitation theories, and their "
                "one-excitation restrictions agree, as objects, at %s of %s "
                "comparisons"
                % (p2["fiber"]["distinct_two_excitation_theories"],
                   com(p2["fiber"]["one_excitation_comparisons"]
                       - p2["fiber"]["one_excitation_disagreements"]),
                   com(p2["fiber"]["one_excitation_comparisons"]))),
        ("C17", "the symmetric shape leaks at %d cells at %d of the %d coin "
                "classes and the antisymmetric shape leaks at %d, so a hard "
                "core there would select"
                % (lk["carrier_grain_symmetric_leak_cells"],
                   lk["carrier_grain_symmetric_coins_leaking"], po["coins"],
                   lk["carrier_grain_antisymmetric_leak_cells"])),
        ("C18", "is a sentence -- both shapes leak at %d of %d coin classes, "
                "and at the %d non-monomial classes every one of the %d "
                "admissible configurations leaks and every one of the %d "
                "forbidden configurations is reached"
                % (lk["actor_grain_both_shapes_leak_coins"], po["coins"],
                   lk["actor_grain_coins_where_every_admissible_source_"
                      "leaks"], lk["actor_grain_admissible"],
                   lk["actor_grain_forbidden"])),
        ("C19", "%d solutions over the ring, %d classes up to a global phase"
                % (po["ring_solutions"], po["classes_up_to_phase"])),
        ("C20", "the ACTOR->SITE leg is a bijection at %d of %d and its image "
                "has %d members against the carrier's %d"
                % (p1["actors"], p1["actors"],
                   p1["actor_leg_image_cardinality"],
                   p1["carrier_cardinality"])),
        ("C21", "the antisymmetric sector's forbidden set is empty at exactly "
                "%d of the %d grains this arena admits, and it is the "
                "carrier's own"
                % (sum(1 for r in lk["wedge_theorem"]["rows"]
                       if r["antisymmetric_forbidden_set_is_empty"]),
                   lk["wedge_theorem"]["grains"])),
        ("C22", "at the site grain a hard core admits %d configurations and "
                "selects at %d of %d coin classes, with no shape closing at "
                "%d of %d"
                % (lk["site_grain_arm"]["admissible"],
                   lk["site_grain_arm"]["coins_that_select"],
                   lk["site_grain_arm"]["coins"],
                   lk["site_grain_arm"]["coins_where_no_shape_closes"],
                   lk["site_grain_arm"]["coins"])),
        ("C23", "the whole leak census is identical at every one of the %d "
                "declared probe fields, at %d of %d rows each"
                % (lk["record_blindness"]["probe_fields"],
                   lk["record_blindness"]["probes"][0]["leak_rows_identical"],
                   lk["record_blindness"]["probes"][0]["leak_rows"])),
    ]


def paper_tables(R):
    """E-22: TABLES RENDER AS CLAIMS.  Every row of the three load-bearing
    tables is assembled from THIS RUN and required to occur in the paper
    exactly once."""
    rows = []
    for m in R["pool"]["rows"]:
        rows.append(("T-POOL-%s" % m["coin"],
                     "| `%s` | %s | %d | %d | %d |"
                     % (m["coin"], "yes" if m["monomial"] else "no",
                        m["carrier_grain_symmetric_leak"],
                        m["actor_grain_symmetric_leak"],
                        m["actor_grain_antisymmetric_leak"])))
    for a in R["arms"]:
        rows.append(("T-ARM-%s" % a["arm"],
                     "| `%s` | %s | %s | %s | %s | `%s` |"
                     % (a["arm"], a["p1"], a["p2"], a["p3"], a["p4"],
                        a["word"])))
    for d in R["p2"]["fiber"]["rows"]:
        rows.append(("T-DECL-%s" % d["declaration"],
                     "| `%s` | %s | %d | %d | %d |"
                     % (d["declaration"], d["grain"], d["ceiling"],
                        d["symmetric_configurations"],
                        d["antisymmetric_configurations"])))
    for c in R["choice_inventory"]:
        rows.append(("T-CHOICE-%s" % c["item"][:18],
                     "| %s | %d | %s | %s |"
                     % (c["item"], c["fiber"], c["class"],
                        c["verdict_determining"])))
    return rows


# THE STRUCTURAL WHITELIST, TRIMMED TO WHAT THIS OBJECT USES (K3 MINOR-5).
# What is left is the set of numerals that name a PART OF THE DOCUMENT rather
# than a measurement: the three section numbers no measured value happens to
# carry, and this paper's own number.  Every other numeral in the object --
# including every exact rational -- is licensed by a measured receipt value,
# and the gate fails on a declared entry the object does not use, so this set
# cannot grow silently.
STRUCTURAL_NUMERALS = {"7", "10", "11", "31"}
FENCE_RE = re.compile(r"```.*?```", re.S)
INLINE_RE = re.compile(r"`[^`]*`")
NUM_PROSE_RE = re.compile(r"(?<![\w.\-/])\d[\d,]*(?:/\d+)?(?![\w])")
NUM_FENCED_RE = re.compile(r"(?<![\w./])\d[\d,]*(?:/\d+)?(?![\w])")
DIGEST_RE = re.compile(r"^[0-9a-f]{12}$")


# the receipt keys whose values are the instrument's SELF-DESCRIPTION rather
# than a measurement: byte lengths, character counts and digests.  A physics
# numeral licensed by a source's byte length is licensed by noise, exactly as
# one licensed by a hash prefix is (K3 MINOR-6).
UNLICENSING_KEYS = ("sha256_12", "payload_sha256_12", "fingerprint",
                    "expected", "digest", "bytes", "chars", "text_sha")
# the few published values that are EXACT RATIONALS carried as strings; they
# are declared by key, so prose can never license a numeral (K1 MINOR-5).
RATIONAL_KEYS = ("emission_total", "emission_total_on_the_doubly_occupied_"
                 "state", "kernel_on_P", "kernel_on_Q")


def licensed_numerals(obj, acc, key=None):
    """the licensed set is the MEASURED values, and ONLY the measured values:
    integers, plus the declared exact-rational rows.  Prose is not a licence
    -- a numeral typed into a gate statement or a ledger number embedded in a
    provenance sentence licensed a paper numeral before this repair (K1
    MINOR-5, K3 MINOR-6) -- and neither is a digest or a byte count."""
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k in UNLICENSING_KEYS:
                continue
            licensed_numerals(v, acc, k)
    elif isinstance(obj, list):
        for v in obj:
            licensed_numerals(v, acc, key)
    elif isinstance(obj, str):
        if key not in RATIONAL_KEYS or DIGEST_RE.match(obj):
            return acc
        for t in re.findall(r"\d[\d,]*(?:/\d+)?", obj):
            acc.add(t.replace(",", ""))
    elif isinstance(obj, bool):
        return acc
    elif isinstance(obj, int):
        acc.add(str(obj))
    return acc


# E-22, the advisory's fourth check: SPELLED numerals above twelve are claims
# too.  House style writes small counts as words, so the scan that stops at
# digits is blind exactly where a paper says "nine of the twenty-seven".
SPELLED = {
    "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16,
    "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20,
    "twenty-one": 21, "twenty-two": 22, "twenty-three": 23,
    "twenty-four": 24, "twenty-five": 25, "twenty-six": 26,
    "twenty-seven": 27, "twenty-eight": 28, "twenty-nine": 29, "thirty": 30,
    "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70, "eighty": 80,
    "ninety": 90, "hundred": 100, "thousand": 1000,
}


def spelled_numerals(text):
    """every spelled numeral above twelve in the object under test, with the
    value it names -- scanned on word boundaries after normalisation."""
    body = canon(text).lower()
    out = []
    for word in sorted(SPELLED, key=len, reverse=True):
        for m in re.finditer(r"(?<![\w-])%s(?![\w])" % re.escape(word), body):
            out.append((word, SPELLED[word], m.start()))
    # a hyphenated compound also matches its own prefix ("twenty" inside
    # "twenty-seven"); keep the longest match at each position
    keep, taken = [], set()
    for word, val, pos in sorted(out, key=lambda r: (-len(r[0]), r[2])):
        span = range(pos, pos + len(word))
        if any(p in taken for p in span):
            continue
        taken |= set(span)
        keep.append({"word": word, "value": val})
    return keep


def paper_coverage(R, text, segs):
    """#20 with the fenced-block addendum and E-22's inline-span addendum:
    prose, fenced blocks AND inline code spans are all scanned, and every
    numeral must be licensed by a measured receipt value or by a declared
    structural numeral."""
    without_fences = FENCE_RE.sub(" ", text)
    blocks = FENCE_RE.findall(text)
    spans = INLINE_RE.findall(without_fences)
    prose = INLINE_RE.sub(" ", without_fences)
    measured = licensed_numerals(R, set())
    known = measured | STRUCTURAL_NUMERALS | head_numerals(segs)
    scanned = fenced = inline = 0
    unreg = []
    targets = [(canon(prose), NUM_PROSE_RE, "prose")]
    targets += [(canon(b), NUM_FENCED_RE, "fenced") for b in blocks]
    targets += [(canon(s), NUM_FENCED_RE, "inline") for s in spans]
    for body, rx, kind in targets:
        for rawtok in rx.findall(body):
            tok = rawtok.replace(",", "")
            scanned += 1
            if kind == "fenced":
                fenced += 1
            elif kind == "inline":
                inline += 1
            if tok not in known:
                unreg.append(tok)
    # the spelled numerals above twelve, licensed the same way
    spelled = spelled_numerals(text)
    for row in spelled:
        row["licensed"] = str(row["value"]) in known
        if not row["licensed"]:
            unreg.append(str(row["value"]))
    # the structural whitelist is itself measured: which of its entries the
    # object actually NEEDS, and whether any is digest-shaped (K3 MINOR-5)
    needed = sorted(t for t in STRUCTURAL_NUMERALS
                    if t not in measured and t not in head_numerals(segs))
    used = set()
    for body, rx, _kind in targets:
        for rawtok in rx.findall(body):
            tok = rawtok.replace(",", "")
            if tok in needed:
                used.add(tok)
    return {"scanned": scanned, "fenced_blocks": len(blocks),
            "fenced_numerals": fenced, "inline_spans": len(spans),
            "inline_numerals": inline, "licensed_values": len(known),
            "licensed_by_a_measured_value": len(measured),
            "spelled_numerals_scanned": len(spelled),
            "spelled_numerals": spelled,
            "structural_numerals_declared": len(STRUCTURAL_NUMERALS),
            "structural_numerals_the_object_needs": sorted(used),
            "structural_numerals_declared_and_unused":
                sorted(set(needed) - used),
            "structural_numerals_that_are_digest_shaped":
                sorted(t for t in STRUCTURAL_NUMERALS if DIGEST_RE.match(t)),
            "unregistered": sorted(set(unreg))}


def block_multiset(text):
    """E-22: the fenced blocks as a MULTISET, never by containment."""
    out = Counter()
    for b in FENCE_RE.findall(text):
        out[canon(b)] += 1
    return out


def banned_words_found(text):
    low = text.lower()
    for c in LICENSED_COMPOUNDS:
        low = low.replace(c, " ")
    word, found = "", []
    for ch in low + " ":
        if ch.isalpha() or ch == "-":
            word += ch
        else:
            if word in BANNED_WORDS:
                found.append(word)
            word = ""
    return sorted(set(found))


def paper_polarity(R, text, mutated=False):
    needles = [
        ("P1", "the excitation rides the co-division pair",
         "the excitation rides the actor"),
        ("P2", "no committed layer forces the occupancy ceiling",
         "the committed layers force the occupancy ceiling"),
        ("P3", "exclusion selects only at the carrier's own grain",
         "exclusion selects at every grain"),
        ("P4", "fermionic-shape is not a theorem of the coupled theory",
         "fermionic-shape is a theorem of the coupled theory"),
    ]
    out = []
    for pid, pos, neg in needles:
        if mutated:
            pos, neg = neg, pos
        have_pos = canon(pos) in canon(text)
        have_neg = canon(neg) in canon(text)
        out.append({"id": pid, "positive": pos, "negative": neg,
                    "positive_present": have_pos,
                    "negative_present": have_neg,
                    "ok": have_pos and not have_neg})
    return out


# ===========================================================================
# SECTION 16.  THE DECLARED FALSIFIER REGISTRY (E-23)
# ===========================================================================
# Five fields per row: the name, the gate it must die at, what it does, THE
# SYMBOL IT MOVES and THE VALUE IT MOVES IT TO.  The last two are re-derived
# from THIS FILE's own AST at run time and compared against the declaration,
# and the published prose must NAME BOTH.

MUTANTS = [
    ("MUT-VERBATIM", "G-VERBATIM",
     "moves `anchor_bad` to the one-element list ['FORGED'], reporting a "
     "located anchor as missing -- must die at the verbatim gate",
     "anchor_bad", "FORGED"),
    ("MUT-PATH-VALUE", "G-PATH-VALUES",
     "moves `pv_bad` to ['PV-CELLS'], detaching a path-value anchor from the "
     "committed receipt it is read from -- must die at the path-value gate",
     "pv_bad", "PV-CELLS"),
    ("MUT-CARRIER-COUNT", "G-P1-CARRIER",
     "moves `carrier_cells` to 26, one short of the rebuilt carrier -- must "
     "die at the gate that compares the rebuild with the coupled machine's "
     "own receipt", "carrier_cells", "26"),
    ("MUT-PAIR-BIJECTION", "G-P1-DICTIONARY",
     "moves `pair_bij` to False: reports the cell-to-co-division-pair map as "
     "not a bijection -- must die at the dictionary gate",
     "pair_bij", "False"),
    ("MUT-VALENCE", "G-P1-DICTIONARY",
     "moves `valence_ok` to False while every per-object row still holds, "
     "detaching the published incidence verdict from its measurement -- must "
     "die at the same gate", "valence_ok", "False"),
    ("MUT-POOL-CLASSES", "G-POOL-REBUILT",
     "moves `classes_here` to 5, hiding one of the six coin classes the "
     "arena's own ring admits -- must die against the coupled machine's "
     "committed census", "classes_here", "5"),
    ("MUT-POOL-UNITARY", "G-POOL-UNITARY",
     "moves `uviol` to 1: one walk operator is reported non-unitary -- must "
     "die at the per-column-pair unitarity gate", "uviol", "1"),
    ("MUT-LEAK-THEOREM", "G-LEAK-THEOREM",
     "moves `theorem_bad` to ['K+0+0w'], reporting a coin whose monomiality "
     "and whose carrier-grain leak disagree -- must die at the leak "
     "theorem's own per-coin check", "theorem_bad", "K+0+0w"),
    ("MUT-LEAK-ROUTES", "G-LEAK-ROUTES",
     "moves `route_bad` to ['FORGED'], reporting the two independent leak "
     "routes as disagreeing -- must die at the two-route gate",
     "route_bad", "FORGED"),
    ("MUT-OCC-KEY", "G-P2-NO-OCCUPANCY-KEY",
     "moves `occ_hits` to [['A-COUPREC', 'occupancy_ceiling']], reporting an "
     "occupancy-shaped name in a committed layer -- must die at the "
     "vocabulary census", "occ_hits", "occupancy_ceiling"),
    ("MUT-HOMONYM", "G-P2-HOMONYM",
     "moves `hom_undeclared` to ['A-D66'], leaving a `ceiling` occurrence "
     "without a declared referent -- must die at the homonym gate",
     "hom_undeclared", "A-D66"),
    ("MUT-STATE-SPACE", "G-P2-STATE-SPACE",
     "moves `carrier_ok` to False: the committed instrument's declared "
     "carrier size stops matching the rebuild -- must die at the state-space "
     "gate", "carrier_ok", "False"),
    ("MUT-FIBER", "G-P2-INVISIBLE-FROM-BELOW",
     "moves `fiber_disagreements` to 7, reporting one-excitation "
     "restrictions that differ across the declarations -- must die at the "
     "invisibility gate", "fiber_disagreements", "7"),
    ("MUT-TURNING", "G-P2-TURNING",
     "moves `p2_verdict` to STRUCTURAL-EXCLUSION, promoting a representation "
     "that has no occupancy coordinate to one that forbids double occupancy "
     "-- must die at the turning-premise gate",
     "p2_verdict", "STRUCTURAL-EXCLUSION"),
    ("MUT-BLINDNESS", "G-P3-BLINDNESS",
     "moves `site_agree` to 8: the two states are reported separable by the "
     "committed rule's own site field -- must die at the blindness gate",
     "site_agree", "8"),
    ("MUT-COMPLETIONS", "G-P3-COMPLETIONS",
     "moves `comp_bad` to ['E1-PER-EXCITATION'], reporting a completion's "
     "emission total as preserving the parent identity when it does not -- "
     "must die at the completion gate", "comp_bad", "E1-PER-EXCITATION"),
    ("MUT-REFUSAL", "G-P3-NEVER-REFUSED",
     "moves `refusals` to 1: a completion is reported refusing a division to "
     "a doubly occupied carrier -- must die at the never-refused gate",
     "refusals", "1"),
    ("MUT-GRAIN-CENSUS", "G-P4-GRAIN-CENSUS",
     "moves `grain_bad` to ['K-2+0w'], detaching one coin's per-declaration "
     "leak row from its own closure predicate -- must die at the per-coin "
     "census", "grain_bad", "K-2+0w"),
    ("MUT-SET-EQUALITY", "G-P4-SET-EQUALITY",
     "moves `seteq_bad` to ['FORGED'], reporting the carrier-grain leak's "
     "source set as something other than the same-site configurations, or as "
     "something other than a strict subset of the same-actor ones -- must "
     "die at the set-equality gate", "seteq_bad", "FORGED"),
    ("MUT-SHAPES-COINCIDE", "G-P4-SHAPES-COINCIDE",
     "moves `coincide_bad` to ['FORGED'], reporting the two shapes' "
     "actor-grain leak sets as distinct -- must die at the coincidence gate",
     "coincide_bad", "FORGED"),
    ("MUT-PARENT-SPLIT", "G-P4-PARENT-SPLIT",
     "moves `leaking_cited` to 47, one away from the split computed from "
     "paper-22's own committed rows -- must die at the citation gate",
     "leaking_cited", "47"),
    ("MUT-ARMS", "G-ARMS-REACHABILITY",
     "moves `words_seen` to the same set with OCC-CEILING-FORCED removed, so "
     "an outcome the head law is claimed to reach is unreached -- must die at "
     "the reachability gate", "words_seen", "OCC-CEILING-FORCED"),
    ("MUT-CONTROL", "G-CONTROL-TWO-WAY",
     "moves `fires` to False: the control arena that must demonstrate the "
     "conditional CAN fire is reported not firing -- must die at the "
     "two-way control gate", "fires", "False"),
    ("MUT-ASYMMETRY", "G-ASYMMETRY",
     "moves `perm_selects` to 1, reporting a permission declaration that "
     "selects a shape -- must die at the asymmetry gate", "perm_selects", "1"),
    ("MUT-STAMPS", "G-DESCRIPTION-STAMPS",
     "moves `stamp_bad` to ['C08'], leaving a published claim without its "
     "description stamp -- must die at the stamp gate", "stamp_bad", "C08"),
    ("MUT-COUNTING", "G-COUNTING-ONLY",
     "moves `measure_declared` to True, publishing a fraction as a "
     "probability with no measure -- must die at the E-24 gate",
     "measure_declared", "True"),
    ("MUT-CHOICES", "G-CHOICE-INVENTORY",
     "moves `choice_bad` to ['the coin class'], reporting a published choice "
     "whose fiber was not counted -- must die at the choice-inventory gate",
     "choice_bad", "the coin class"),
    ("MUT-WALL-L1", "G-WALL-L1",
     "moves `layer` to one carrying the sentence order-level covariance is "
     "established -- must die at the L-1 wall",
     "layer", "order-level covariance is established"),
    ("MUT-WALL-BHS", "G-WALL-BHS",
     "moves `layer` to one carrying a sprinkling-grade boosted rest frame "
     "reading -- must die at the BHS abstention scan",
     "layer", "boosted rest frame"),
    ("MUT-WALL-KR", "G-WALL-KR",
     "moves `layer` to one carrying a myrheim-meyer dimension estimate with "
     "no height control -- must die at the Kleitman-Rothschild scan",
     "layer", "myrheim-meyer"),
    ("MUT-WALL-COSMO", "G-WALL-COSMO",
     "moves `layer` to one carrying a cosmological expansion reading -- must "
     "die at the continuum and cosmological scan",
     "layer", "cosmological expansion"),
    ("MUT-PAPER-WALL", "G-NO-PARTICLE-NAMING",
     "moves `bad_words` to the found list with 'fermion' appended, so a bare "
     "particle noun is reported in the object under test -- must die at the "
     "shape-word wall", "bad_words", "fermion"),
    ("MUT-VERDICT-WORD", "G-VERDICT-RECONSTRUCTED",
     "moves `segs`, in the builder alone, to one whose outcome segment reads "
     "OCC-CEILING-FORCED -- must die at the comparator, which re-derives the "
     "word from the premise rows", "segs", "OCC-CEILING-FORCED"),
    ("MUT-VERDICT-VALUE", "G-VERDICT-RECONSTRUCTED",
     "moves `segs` by retyping one measured value inside a segment, "
     "CARRIER-CELLS=27 to CARRIER-CELLS=26 -- must die at the same "
     "comparator, field by field", "segs", "CARRIER-CELLS=26"),
    ("MUT-VERDICT-CLAUSE", "G-VERDICT-RECONSTRUCTED",
     "moves `segs` by truncating a segment at "
     "ACTOR-GRAIN-CANCELLATION-CELLS, so a clause the head must carry is "
     "silently dropped -- must die at the comparator's label-set leg",
     "segs", "ACTOR-GRAIN-CANCELLATION-CELLS"),
    ("MUT-HEAD-LITERAL", "G-VERDICT-NO-TYPED-LITERAL",
     "moves `head_unmeasured` to ['4242'], a head numeral that occurs in no "
     "measured receipt value -- must die at the typed-literal gate",
     "head_unmeasured", "4242"),
    ("MUT-PAPER-CLAIM", "G-PAPER-CLAIMS",
     "moves `sent`, an assembled claim, to one reading 26 cells -- must die "
     "at the claim gate", "sent", "26 cells"),
    ("MUT-PAPER-TABLE", "G-PAPER-TABLES",
     "moves `trows`, the rendered table rows, to the list with its last row "
     "dropped and a FORGED one appended -- must die at the table gate",
     "trows", "FORGED"),
    ("MUT-PAPER-NUMERAL", "G-PAPER-NUMERAL-COVERAGE",
     "moves `unregistered` to ['123456789'], an unlicensed numeral -- must "
     "die at the #20 coverage scan", "unregistered", "123456789"),
    ("MUT-PAPER-HEAD", "G-PAPER-HEAD-VERBATIM",
     "moves `probe`, a derived verdict segment, by one character to "
     "seg[:-1] + Z before matching it into the paper -- must die at the "
     "head-verbatim gate", "probe", "Z"),
    ("MUT-PAPER-BLOCK", "G-PAPER-HEAD-VERBATIM",
     "moves `blockmap`, the paper's own fenced-block multiset, to the same "
     "multiset with one block dropped, so a duplicated head could shadow a "
     "forged twin -- must die at the same gate's MULTISET leg",
     "blockmap", "dropped"),
    ("MUT-PAPER-POLARITY", "G-PAPER-CLAIM-POLARITY",
     "moves `mutated` to True, swapping every load-bearing claim for its "
     "negation in the object under test -- must die at the polarity gate",
     "mutated", "True"),
    ("MUT-CLI-PERMISSIVE", "G-CLI-WHITELIST",
     "moves `bad` to the one-element list [['--nope']], so the argv "
     "whitelist is reported accepting an unknown flag -- must die at the CLI "
     "gate", "bad", "--nope"),
    ("MUT-SELFTEST-WRITES", "G-SELFTEST-WRITES-NOTHING",
     "moves `st_ok` to False: the AST probe reports the self-test path "
     "reaching the writer -- must die at the self-test shape gate",
     "st_ok", "False"),
    ("MUT-MEMO", "G-MEMO-CLEAN",
     "moves `memo_ok` to False: the memo's fingerprint is reported moving "
     "between runs -- must die at the memo gate", "memo_ok", "False"),
    ("MUT-FALSIFIER-DESC", "G-FALSIFIER-HONESTY",
     "moves `declared` to ('FORGED', 'FORGED') for MUT-MEMO, so a "
     "falsifier's published symbol and value stop matching its own code -- "
     "must die at the falsifier-honesty gate", "declared", "FORGED"),
    ("MUT-WRITER-SHAPE", "G-WRITER-SHAPE",
     "moves `ws` by truncating its gate_names_in_finish list, so the terminal "
     "integrity gate goes missing from finish() -- must die at the "
     "writer-shape gate", "ws", "gate_names_in_finish"),
    ("MUT-SWEEP-UNBOUND", "G-SWEEP-BOUND",
     "moves `swept` to True in a sub-pipeline that carries no sweep rows -- "
     "must die at the sweep-binding gate", "swept", "True"),
    ("MUT-SEAL-DROP", "G-SEAL-COMPLETE",
     "moves `SEAL-COVERAGE` out of the seal manifest by taking a bare "
     "return from Seal.take before the row is appended -- must die at the "
     "totality gate", "SEAL-COVERAGE", "return"),
    ("MUT-SEAL-BROKEN", "G-SEAL-COMPLETE",
     "moves `outcome_word` to BROKEN after that key was sealed, so the "
     "payload no longer matches its gate-time digest -- must die at the seal "
     "verification", "outcome_word", "BROKEN"),
]
MUTANT_NAMES = {m[0] for m in MUTANTS}

GATE_REGISTRY = [
    "G-PROVENANCE", "G-EXACT-ARITHMETIC", "G-NO-SUBPROCESS",
    "G-READS-DECLARED", "G-VERBATIM", "G-PATH-VALUES", "G-QUESTION-ANCHORED",
    "G-P1-CARRIER", "G-P1-DICTIONARY",
    "G-POOL-REBUILT", "G-POOL-UNITARY", "G-LEAK-THEOREM", "G-LEAK-ROUTES",
    "G-P2-NO-OCCUPANCY-KEY", "G-P2-HOMONYM", "G-P2-STATE-SPACE",
    "G-P2-INVISIBLE-FROM-BELOW", "G-P2-TURNING",
    "G-P3-BLINDNESS", "G-P3-COMPLETIONS", "G-P3-NEVER-REFUSED",
    "G-P4-GRAIN-CENSUS", "G-P4-SET-EQUALITY", "G-P4-SHAPES-COINCIDE",
    "G-P4-PARENT-SPLIT",
    "G-ARMS-REACHABILITY", "G-CONTROL-TWO-WAY", "G-ASYMMETRY",
    "G-DESCRIPTION-STAMPS", "G-COUNTING-ONLY", "G-CHOICE-INVENTORY",
    "G-WALL-L1", "G-WALL-BHS", "G-WALL-KR", "G-WALL-COSMO",
    "G-NO-PARTICLE-NAMING",
    "G-VERDICT-RECONSTRUCTED", "G-VERDICT-NO-TYPED-LITERAL",
    "G-PAPER-CLAIMS", "G-PAPER-TABLES", "G-PAPER-NUMERAL-COVERAGE",
    "G-PAPER-HEAD-VERBATIM", "G-PAPER-CLAIM-POLARITY",
    "G-MEMO-CLEAN", "G-CLI-WHITELIST", "G-SELFTEST-WRITES-NOTHING",
    "G-MUTANTS-ON-TARGET", "G-COVERAGE", "G-FALSIFIER-HONESTY",
    "G-WRITER-SHAPE", "G-SWEEP-BOUND", "G-ANCHOR-CONSUMERS",
    "G-REACHABILITY", "G-PAPER-COVERAGE-FINAL", "G-SEAL-COMPLETE",
    "G-ARTIFACT-INTEGRITY",
]

# ===========================================================================
# SECTION 17.  THE RUN
# ===========================================================================


def measurement_layer(R, LD):
    """this run's whole measurement surface: every measured receipt key
    together with the statement and evidence of every gate evaluated so far.
    The wall scans read THIS, not the paper, so an abstention is measured."""
    parts = [json.dumps({k: R.get(k) for k in MEASURED_KEYS if k in R},
                        sort_keys=True, default=str)]
    for g in LD.rows:
        parts.append(g["gate"] + " " + g["statement"] + " " + g["evidence"])
    return " ".join(parts).lower()


def wall_gate(LD, gname, layer):
    """one wall, as an instrument: this run's whole measurement layer is
    scanned for the reading the wall bars, and the falsifier writes that
    reading INTO the layer and dies here."""
    needle, abstention = WALL_NEEDLES[gname]
    present = needle in layer
    LD.gate(gname,
            "THE WALL IS AN INSTRUMENT, NOT A LABEL: this run's whole "
            "measurement layer -- every measured receipt key together with "
            "the statement and evidence of every gate evaluated -- is scanned "
            "for the reading this wall bars.  %s.  The falsifier writes the "
            "forbidden reading INTO that layer and dies here" % abstention,
            not present, "the barred reading is present in the measurement "
            "layer: %s (%d chars scanned)" % (present, len(layer)))
    return {"gate": gname, "needle": needle,
            "present_in_the_measurement_layer": present,
            "abstention": abstention}


def full_run(break_anchor=None, paper_text=None, paper_rel=PAPER_REL,
             do_paper=True):
    global READS
    READS = []
    LD, SEAL, R = Ledger(), Seal(), {}
    R["schema"] = {"schema": SCHEMA, "unit": "OCC", "paper": paper_rel,
                   "question": "does any committed deeper layer FORCE the "
                               "occupancy ceiling that selects statistics?"}

    # -- SEC 1  PROVENANCE ---------------------------------------------------
    say("=" * 78)
    say("OCC -- THE OCCUPANCY-CEILING FORCING UNIT")
    say("=" * 78)
    texts, receipts, prov = {}, {}, []
    bad_src = []
    for sid, rel, want, why in SOURCES:
        raw = read_bytes(rel)
        got = hashlib.sha256(raw).hexdigest()[:12]
        expect = "0" * 12 if break_anchor == sid else want
        prov.append({"anchor": sid, "path": rel, "sha256_12": got,
                     "expected": expect, "matches": got == expect,
                     "bytes": len(raw), "why": why})
        if got != expect:
            bad_src.append(sid)
        texts[sid] = raw.decode("utf-8")
        if rel.endswith(".json"):
            receipts[sid] = json.loads(texts[sid])
    R["provenance"] = {"sources": prov, "count": len(SOURCES)}
    LD.gate("G-PROVENANCE",
            "the %d declared sources are read at run time by path resolved "
            "from this file's own location and verified by sha256-12; a "
            "corrupted anchor kills the run here and --break-anchor NAME "
            "exercises exactly that" % len(SOURCES),
            not bad_src, "anchors not matching: %s" % (bad_src or "none"))
    SEAL.take("SEAL-SCHEMA", R)
    SEAL.take("SEAL-PROVENANCE", R)

    src_self = read_text(SELF)
    tree = ast.parse(src_self)
    floats = [n.lineno for n in ast.walk(tree)
              if isinstance(n, ast.Constant) and isinstance(n.value, float)]
    float_calls = [n.lineno for n in ast.walk(tree)
                   if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)
                   and n.func.id == "float"]
    R["arithmetic"] = {"float_literals": len(floats),
                       "float_calls": len(float_calls),
                       "representation": "Z[w] as integer pairs over the "
                                         "common denominator 3; Fraction for "
                                         "the emission fields; no float"}
    R["python"] = {"version": "%d.%d" % sys.version_info[:2]}
    LD.gate("G-EXACT-ARITHMETIC",
            "an AST scan of this file finds no float literal and no call to "
            "float(): every amplitude is an integer pair over Z[w] and every "
            "ratio is a Fraction",
            not floats and not float_calls,
            "float literals %s, float() calls %s" % (floats or "none",
                                                     float_calls or "none"))
    SEAL.take("SEAL-ARITHMETIC", R)
    SEAL.take("SEAL-PYTHON", R)

    bad_imports = sorted({n.names[0].name for n in ast.walk(tree)
                          if isinstance(n, ast.Import)
                          and n.names[0].name in ("subprocess", "socket",
                                                  "urllib", "requests")}
                         | {n.attr for n in ast.walk(tree)
                            if isinstance(n, ast.Attribute)
                            and n.attr in ("system", "popen", "check_output",
                                           "run")})
    LD.gate("G-NO-SUBPROCESS",
            "no subprocess, socket or version-control call of any kind: the "
            "scan reads imports AND attribute names, so the run is correct "
            "off-tree and on a machine with no git",
            not bad_imports, "forbidden names: %s" % (bad_imports or "none"))

    declared_reads = sorted({rel for _s, rel, _w, _y in SOURCES})
    actual_reads = sorted(set(READS))
    R["object_reads"] = {"declared": sorted(OBJECT_READS_WHY),
                         "why": OBJECT_READS_WHY,
                         "source_reads": len(actual_reads)}
    LD.gate("G-READS-DECLARED",
            "the read set is exactly the declared set: %d pinned sources by "
            "path and hash, plus the SECOND declared set -- this file and the "
            "object under test -- which is named here rather than left out of "
            "the accounting" % len(declared_reads),
            declared_reads == actual_reads,
            "declared %d, read %d, difference %s"
            % (len(declared_reads), len(actual_reads),
               sorted(set(declared_reads) ^ set(actual_reads)) or "none"))
    SEAL.take("SEAL-OBJECT-READS", R)

    anchors, anchor_bad = [], []
    for vid, sid, needle, consumer in VERBATIM:
        hay = texts[sid]
        found = match_needle(hay, needle)
        # each anchor carries its own falsifier: perturb a content-bearing
        # token and require the perturbed needle NOT to locate
        toks = [t for t in re.findall(r"[A-Za-z0-9_>-]+", needle)
                if len(t) > 3]
        probe = needle.replace(toks[-1], toks[-1] + "ZQ") if toks else needle
        anchors.append({"id": vid, "source": sid, "consumer": consumer,
                        "chars": len(needle), "located": found,
                        "perturbed_needle_absent": not match_needle(hay, probe)})
        if not found or match_needle(hay, probe):
            anchor_bad.append(vid)
    anchor_bad = pick("MUT-VERBATIM", anchor_bad, ["FORGED"])
    R["verbatim_anchors"] = anchors
    LD.gate("G-VERBATIM",
            "#62 with #125's normalisation: %d verbatim anchors are located "
            "in their pinned sources after markdown-prefix stripping, ASCII "
            "folding and whitespace normalisation, and each is PERTURBED at a "
            "content-bearing token and required not to locate, so every row "
            "carries its own falsifier" % len(VERBATIM),
            not anchor_bad, "anchors failing: %s" % (anchor_bad or "none"))
    SEAL.take("SEAL-VERBATIM", R)

    pvs, pv_bad = [], []
    for pid, sid, path, expect, consumer in PATH_VALUES:
        try:
            got = jpath(receipts[sid], path)
        except (KeyError, IndexError, TypeError):
            got = None
        ok = got == expect
        pvs.append({"id": pid, "source": sid, "path": path,
                    "value": got, "expected": expect, "matches": ok,
                    "consumer": consumer})
        if not ok:
            pv_bad.append(pid)
    pv_bad = pick("MUT-PATH-VALUE", pv_bad, ["PV-CELLS"])
    R["path_value_anchors"] = pvs
    LD.gate("G-PATH-VALUES",
            "#91's path-value stability: %d values are READ OUT of the "
            "parents' own committed receipts at declared json paths and each "
            "is consumed by a named gate -- the carrier, the links, the "
            "realised co-division pairs, the coin census, and paper-22's own "
            "occupancy rows" % len(PATH_VALUES),
            not pv_bad, "path values failing: %s" % (pv_bad or "none"))
    SEAL.take("SEAL-PATH-VALUES", R)

    # the pre-registered outcome names are PARSED from the pin's bytes
    pin = texts["A-PIN"]
    outcomes_found = [w for w in OUTCOMES if w in pin]
    LD.gate("G-QUESTION-ANCHORED",
            "the question and its four pre-registered outcome words are read "
            "from the PIN's own bytes rather than typed here, and paper-22's "
            "head clause FORCING-THE-CEILING=OPEN together with its measured "
            "ceiling_is_anchored = false are what makes this unit's question "
            "a live one",
            len(outcomes_found) == len(OUTCOMES)
            and receipts["A-P22REC"]["occupancy"]["ceiling_is_anchored"]
            is False,
            "outcome words located in the pin: %d of %d; the parent's "
            "ceiling_is_anchored is %s"
            % (len(outcomes_found), len(OUTCOMES),
               receipts["A-P22REC"]["occupancy"]["ceiling_is_anchored"]))

    # -- THE HEAVY CENSUS ----------------------------------------------------
    C = census(lambda: build_census(texts, receipts))
    memo_ok = pick("MUT-MEMO", _CENSUS["fingerprint"] == digest(
        _CENSUS["value"]), False)
    R["memo"] = {"fingerprint": _CENSUS["fingerprint"],
                 "builds": _CENSUS["builds"], "hits": _CENSUS["hits"],
                 "defensive_copy": True}
    LD.gate("G-MEMO-CLEAN",
            "the heavy census is built once and handed back as a DEFENSIVE "
            "COPY, and its whole contents are fingerprinted at creation and "
            "re-checked on every hand-back, so no injection -- this run's or "
            "an earlier run's -- can reach the next run through it.  The "
            "falsifiers act on the GATE layer above it, which is what makes "
            "the mutant sweep a sequence of independent runs",
            memo_ok, "fingerprint %s, builds %d, hits %d"
            % (_CENSUS["fingerprint"], _CENSUS["builds"], _CENSUS["hits"]))
    SEAL.take("SEAL-MEMO", R)

    # -- SEC 6  P1 -----------------------------------------------------------
    p1 = C["p1"]
    R["arena"] = {"actors": p1["actors"], "cells": p1["carrier_cells"],
                  "links": [list(l) for l in LINKS],
                  "undeclared_direction": list(UNDECLARED_DIRECTION),
                  "co_division_pairs": p1["co_division_pairs"],
                  "record": "the welded landing record, n = 1 at all 27 cells",
                  "same_actor_configurations": C["same_actor_configurations"],
                  "same_site_configurations": C["same_site_configurations"]}
    carrier_cells = pick("MUT-CARRIER-COUNT", p1["carrier_cells"], 26)
    rec_cells = jpath(receipts["A-COUPREC"], "arena/cells")
    rec_sites = jpath(receipts["A-COUPREC"], "arena/sites")
    rec_links = jpath(receipts["A-COUPREC"], "arena/links")
    LD.gate("G-P1-CARRIER",
            "THE ARENA THE EXCITATIONS USE, REBUILT AND GATED AGAINST THE "
            "COUPLED MACHINE'S OWN RECEIPT.  The coupled machine's state is a "
            "vector on its %d cells; this unit rebuilds the carrier from the "
            "%d actors and the %d declared link directions and compares the "
            "rebuild with the committed receipt's own arena rows"
            % (rec_cells, rec_sites, len(rec_links)),
            carrier_cells == rec_cells and p1["actors"] == rec_sites
            and [list(l) for l in LINKS] == rec_links,
            "rebuilt carrier %d against the receipt's %d; actors %d against "
            "%d; links %s" % (carrier_cells, rec_cells, p1["actors"],
                              rec_sites, [list(l) for l in LINKS]))
    SEAL.take("SEAL-ARENA", R)

    pair_bij = pick("MUT-PAIR-BIJECTION", p1["pair_link_bijection"], False)
    valence_ok = pick("MUT-VALENCE",
                      p1["cells_with_exactly_two_actors"] == NCELL
                      and p1["actors_in_exactly_six_cells"] == 9, False)
    R["p1"] = p1
    LD.gate("G-P1-DICTIONARY",
            "P1, MEASURED ON THE ARENA THE EXCITATIONS USE.  The weld's "
            "forced dictionary has two legs.  ACTOR->SITE is a bijection at "
            "%d of %d -- and it covers %d of the %d objects the excitation's "
            "own coordinate ranges over.  The leg that welds THAT set is the "
            "second one: a cell IS an unordered co-division pair of actors, "
            "and the rebuilt map between them is a bijection in both "
            "directions.  The incidence is measured per object: every cell "
            "carries exactly two actors at %d of %d and every actor lies in "
            "exactly six cells at %d of %d, so the excitation-to-actor "
            "relation is NOT A FUNCTION and the seed conditional's injection "
            "premise is not a statement about this carrier"
            % (p1["actors"], p1["actors"],
               p1["actor_leg_image_in_the_carrier"], p1["carrier_cells"],
               p1["cells_with_exactly_two_actors"], p1["carrier_cells"],
               p1["actors_in_exactly_six_cells"], p1["actors"]),
            (pair_bij and valence_ok and p1["actor_site_bijection"]
             and not p1["excitation_to_actor_is_a_function"]),
            "pair bijection %s; incidence rows %s; ACTOR->SITE bijection %s; "
            "excitation->actor is a function %s"
            % (pair_bij, valence_ok, p1["actor_site_bijection"],
               p1["excitation_to_actor_is_a_function"]))
    SEAL.take("SEAL-P1", R)

    # -- SEC 4  THE POOL -----------------------------------------------------
    cc = C["coin_census"]
    pool_rows = []
    for m in C["pool"]:
        row = dict(m)
        lk = [r for r in C["leaks"] if r["coin"] == m["coin"]][0]
        row["carrier_grain_symmetric_leak"] = \
            lk["D-CARRIER-1|SYMMETRIC"]["leak_cells"]
        row["carrier_grain_antisymmetric_leak"] = \
            lk["D-CARRIER-1|ANTISYMMETRIC"]["leak_cells"]
        row["actor_grain_symmetric_leak"] = \
            lk["D-ACTOR-1|SYMMETRIC"]["leak_cells"]
        row["actor_grain_antisymmetric_leak"] = \
            lk["D-ACTOR-1|ANTISYMMETRIC"]["leak_cells"]
        pool_rows.append(row)
    R["pool"] = {"coins": len(pool_rows), "alphabet": cc["alphabet"],
                 "ring_solutions": cc["ring_solutions"],
                 "classes_up_to_phase": cc["classes_up_to_phase"],
                 "grover_classes": cc["grover_classes"],
                 "non_monomial": sum(1 for r in pool_rows
                                     if not r["monomial"]),
                 "rows": pool_rows}
    classes_here = pick("MUT-POOL-CLASSES", cc["classes_up_to_phase"], 5)
    LD.gate("G-POOL-REBUILT",
            "THE POOL IS THIS ARENA'S OWN.  The S_3-covariant unitary coins "
            "over the arena's own %d-value alphabet (1/3)Z[w] are rebuilt "
            "from the definitions -- not imported -- and the census is gated "
            "against the coupled machine's committed one: %d solutions, %d "
            "classes up to a global phase, of which %d is +/- Grover"
            % (cc["alphabet"], cc["ring_solutions"],
               cc["classes_up_to_phase"], cc["grover_classes"]),
            (classes_here == jpath(receipts["A-COUPREC"],
                                   "walk/coin_census/classes_up_to_phase")
             and cc["ring_solutions"] == jpath(
                 receipts["A-COUPREC"], "walk/coin_census/ring_solutions")
             and cc["grover_classes"] == jpath(
                 receipts["A-COUPREC"],
                 "walk/coin_census/grover_classes_up_to_phase")
             and cc["alphabet"] == jpath(receipts["A-COUPREC"],
                                         "walk/scalar_shape/alphabet")),
            "classes %d, ring solutions %d, grover classes %d, alphabet %d "
            "-- all against the committed receipt"
            % (classes_here, cc["ring_solutions"], cc["grover_classes"],
               cc["alphabet"]))

    uviol = pick("MUT-POOL-UNITARY",
                 sum(r["unitarity_violations"] for r in pool_rows), 1)
    LD.gate("G-POOL-UNITARY",
            "every walk operator in the pool is EXACTLY unitary, checked per "
            "COLUMN PAIR rather than by a norm: %d operators, %d column pairs "
            "each, over Z[w] at the common denominator 3"
            % (len(pool_rows), NCELL * NCELL),
            uviol == 0, "unitarity violations across the pool: %d" % uviol)
    SEAL.take("SEAL-POOL", R)

    # -- THE LEAK CENSUS -----------------------------------------------------
    theorem_rows, theorem_bad = [], []
    for r in pool_rows:
        leaks_here = r["carrier_grain_symmetric_leak"] > 0
        predicted = not r["monomial"]
        theorem_rows.append({"coin": r["coin"], "monomial": r["monomial"],
                             "carrier_grain_symmetric_leaks": leaks_here,
                             "theorem_predicts": predicted,
                             "agrees": leaks_here == predicted})
        if leaks_here != predicted:
            theorem_bad.append(r["coin"])
    # THE RECORD-BLINDNESS THEOREM, MEASURED (K2 R1/S-E2).  The count field
    # enters the walk only as a unit-modulus diagonal on the source cell, so
    # it cannot turn a zero into a nonzero: the leak census is a function of
    # the walk's zero pattern alone.  Every declared probe field rebuilds the
    # walk and re-runs all 48 leak rows.
    rb = C["record_blindness"]
    rb_bad = [p["count_field"] for p in rb["probes"]
              if p["leak_rows_identical"] != p["leak_rows"]
              or p["support_patterns_identical"] != p["coins"]]
    if not rb["landing_record_identity"]:
        rb_bad.append("THE-LANDING-RECORD-IDENTITY")
    theorem_bad = pick("MUT-LEAK-THEOREM", theorem_bad + rb_bad, ["K+0+0w"])
    LD.gate("G-LEAK-THEOREM",
            "PAPER-22'S LEAK THEOREM, TRANSPORTED AND VERIFIED PER COIN.  In "
            "the normalised symmetric square the only cell from a hard-core "
            "configuration into a doubly occupied one is a single product of "
            "two amplitudes, so the symmetric shape leaks out of the "
            "carrier-grain hard core exactly when some row of the operator "
            "carries two nonzero entries.  The gate binds COINS, not the "
            "tally: each of the %d classes is checked against its own "
            "monomiality predicate, in both directions.  AND THE CENSUS IS "
            "RECORD-BLIND, BY THEOREM AND BY MEASUREMENT: the count field "
            "enters the walk only as D(n) = diag(w^{n(c)}), a unit-modulus "
            "diagonal on the source cell, so it cannot turn a zero into a "
            "nonzero and the whole leak layer is a function of the zero "
            "pattern alone.  The walk is rebuilt at %d declared probe fields "
            "of the %s family -- the all-zero and all-two records and two "
            "non-constant ones -- and at every one of them the support "
            "pattern is identical at %d of %d coins and all %d leak rows are "
            "identical; the landing record n = 1 is recovered as the rebuild "
            "at that field"
            % (len(pool_rows), rb["probe_fields"], rb["family_size"],
               rb["probes"][0]["support_patterns_identical"],
               rb["probes"][0]["coins"], rb["probes"][0]["leak_rows"]),
            not theorem_bad, "coins whose leak and whose monomiality "
            "disagree, or probe fields whose census moves: %s"
            % (theorem_bad or "none"))

    route_rows = route_ok = 0
    route_bad = []
    cancel_cells = 0
    for r in C["leaks"]:
        for did, _g, _c, _w in DECLARATIONS:
            for sh in SHAPES:
                cellrow = r["%s|%s" % (did, sh)]
                route_rows += 1
                if cellrow["routes_agree"]:
                    route_ok += 1
                else:
                    route_bad.append("%s|%s|%s" % (r["coin"], did, sh))
                cancel_cells += cellrow["both_products_nonzero"]
    route_bad = pick("MUT-LEAK-ROUTES", route_bad, ["FORGED"])
    ag = [r for r in C["set_equalities"]]
    R["leaks"] = {
        "route_rows": route_rows, "route_rows_agreeing": route_ok,
        "cancellation_cells_total": cancel_cells,
        "carrier_grain_symmetric_leak_cells":
            max(r["carrier_grain_symmetric_leak"] for r in pool_rows),
        "carrier_grain_symmetric_coins_leaking":
            sum(1 for r in pool_rows if r["carrier_grain_symmetric_leak"] > 0),
        "carrier_grain_antisymmetric_leak_cells":
            max(r["carrier_grain_antisymmetric_leak"] for r in pool_rows),
        "carrier_grain_antisymmetric_forbidden_configurations":
            C["leaks"][0]["D-CARRIER-1|ANTISYMMETRIC"]["forbidden"],
        "carrier_grain_set_equality_coins":
            sum(1 for r in ag
                if r["carrier_grain_sources_are_the_same_site_"
                     "configurations"] is True),
        "carrier_grain_same_actor_equality_coins":
            sum(1 for r in ag
                if r["carrier_grain_sources_are_the_same_actor_"
                     "configurations"] is True),
        "carrier_grain_containment_coins":
            sum(1 for r in ag
                if r["carrier_grain_sources_are_actor_grain_forbidden"]
                is True),
        "carrier_grain_strict_containment_coins":
            sum(1 for r in ag
                if r["carrier_grain_containment_is_strict"] is True),
        "carrier_grain_leak_sources": max(r["carrier_grain_leak_sources"]
                                          for r in ag),
        "same_actor_configurations": C["same_actor_configurations"],
        "same_actor_configurations_excluded":
            C["same_actor_configurations"] - max(
                r["carrier_grain_leak_sources"] for r in ag),
        "actor_grain_both_shapes_leak_coins":
            sum(1 for r in pool_rows
                if r["actor_grain_symmetric_leak"] > 0
                and r["actor_grain_antisymmetric_leak"] > 0),
        "actor_grain_leak_cells_non_monomial":
            max(r["actor_grain_antisymmetric_leak"] for r in pool_rows),
        "actor_grain_leak_cells_monomial":
            min(r["actor_grain_antisymmetric_leak"] for r in pool_rows),
        "actor_grain_shape_sets_coincide_coins":
            sum(1 for r in ag if r["actor_grain_shape_leak_sets_coincide"]),
        "actor_grain_cancellation_cells":
            sum(r["actor_grain_both_products_nonzero"] for r in ag),
        # THE POOL-MAX IS LABELLED A MAX, and the per-coin minimum is
        # published beside it: the universal "every one of the 216 admissible
        # configurations leaks" is FALSE at the monomial class, where 81 of
        # 216 leak and 81 of 135 are reached (K1 MAJOR-4).
        "actor_grain_sources_leaking_max":
            max(r["actor_grain_sources_leaking"] for r in ag),
        "actor_grain_sources_leaking_min":
            min(r["actor_grain_sources_leaking"] for r in ag),
        "actor_grain_targets_reached_max":
            max(r["actor_grain_targets_reached"] for r in ag),
        "actor_grain_targets_reached_min":
            min(r["actor_grain_targets_reached"] for r in ag),
        "actor_grain_admissible":
            C["leaks"][0]["D-ACTOR-1|ANTISYMMETRIC"]["admissible"],
        "actor_grain_forbidden":
            C["leaks"][0]["D-ACTOR-1|ANTISYMMETRIC"]["forbidden"],
        "actor_grain_coins_where_every_admissible_source_leaks":
            sum(1 for r in ag
                if r["actor_grain_sources_leaking"]
                == C["leaks"][0]["D-ACTOR-1|ANTISYMMETRIC"]["admissible"]),
        "actor_grain_coins_where_every_forbidden_target_is_reached":
            sum(1 for r in ag
                if r["actor_grain_targets_reached"]
                == C["leaks"][0]["D-ACTOR-1|ANTISYMMETRIC"]["forbidden"]),
        "set_equalities": ag,
        "wedge_theorem": C["wedge_theorem"],
        "site_grain_arm": C["site_grain_arm"],
        "record_blindness": C["record_blindness"],
    }
    LD.gate("G-LEAK-ROUTES",
            "THE LEAK IS MEASURED BY TWO INDEPENDENT ROUTES at every one of "
            "the %d (coin, declaration, shape) rows.  Route 1 forms the "
            "lifted matrix element and tests it against zero in the ring; "
            "route 2 never forms it and counts the cells at which at least "
            "one of the two products is nonzero.  They can differ only where "
            "BOTH products are nonzero and cancel, and that census is "
            "published beside them: %d such cells in the whole run"
            % (route_rows, cancel_cells),
            not route_bad and route_ok == route_rows,
            "rows agreeing %d of %d; disagreements %s"
            % (route_ok, route_rows, route_bad or "none"))
    SEAL.take("SEAL-LEAKS", R)

    # -- SEC 7  P2 -----------------------------------------------------------
    voc = C["p2_vocabulary"]
    occ_hits = pick("MUT-OCC-KEY", voc["occupancy_hits"],
                    [["A-COUPREC", "occupancy_ceiling"]])
    LD.gate("G-P2-NO-OCCUPANCY-KEY",
            "THE COMMITTED DEEPER LAYERS DECLARE NO OCCUPANCY COORDINATE, and "
            "that is a census with a POSITIVE CONTROL rather than a claim.  "
            "The published key sets and declared name sets of the %d "
            "committed layers beneath the excitations -- the coupled machine, "
            "the weld and the transport grammar, %d names in all -- are "
            "scanned token by token against a declared occupancy vocabulary "
            "of %d tokens, and NONE of them is occupancy-shaped.  The same "
            "scan is run on the one layer that DID declare a ceiling, "
            "paper-22's own receipt, and fires there at %d names, so the "
            "instrument is known live rather than assumed.  Paper-22 measured "
            "27 declaration keys and none occupancy-shaped on the RECORD "
            "layer; this extends the same measurement to the DYNAMICAL layer "
            "that carries the excitations"
            % (voc["deeper_sources"], voc["names_censused"],
               len(OCCUPANCY_TOKENS),
               voc["control_occupancy_shaped_names"]),
            not occ_hits and voc["control_occupancy_shaped_names"] > 0,
            "occupancy-shaped names in the deeper layers: %s; in the declared "
            "control: %d (%s)"
            % (occ_hits or "none", voc["control_occupancy_shaped_names"],
               ", ".join(voc["control_examples"][:3])))

    hom_undeclared = pick("MUT-HOMONYM",
                          voc["homonym"]["undeclared_referents"], ["A-D66"])
    LD.gate("G-P2-HOMONYM",
            "THE HOMONYM IS MEASURED, NOT SUPPRESSED.  The word `ceiling` "
            "does occur in the committed layers -- %d sources carry it -- and "
            "every occurrence is required to match a DECLARED non-occupancy "
            "referent: the weld's positive-definiteness ceiling on division "
            "counts, d60's engineered search ceiling and d66's arbitration "
            "budget.  A new referent would fail here"
            % len(voc["homonym"]["rows"]),
            not hom_undeclared,
            "sources whose `ceiling` hits have no declared referent: %s"
            % (hom_undeclared or "none"))

    ss = C["p2_state_space"]
    carrier_ok = pick("MUT-STATE-SPACE", ss["carrier_matches_the_rebuild"],
                      False)
    LD.gate("G-P2-STATE-SPACE",
            "THE TURNING PREMISE, MEASURED ON THE CONSTRUCTION AND NOT ON THE "
            "USAGE.  The committed instrument's own abstract syntax tree is "
            "read: its declared carrier is %s and %s, which is this unit's "
            "rebuilt carrier; none of its %d functions takes an "
            "excitation-number parameter, and no constructor in it is indexed "
            "by anything but a cell.  A doubly occupied state is therefore "
            "NEITHER CONSTRUCTIBLE NOR EXCLUDED there -- the representation "
            "has no occupancy coordinate to carry the question"
            % (ss["declared_DIM"], ss["declared_NCELL"], ss["functions"]),
            carrier_ok and not ss["two_excitation_constructor_present"],
            "declared DIM %s / NCELL %s against the rebuild %d; "
            "excitation-number parameters %s"
            % (ss["declared_DIM"], ss["declared_NCELL"], NCELL,
               ss["excitation_number_parameters"] or "none"))

    fib = C["p2_fiber"]
    fiber_rows = []
    for did, grain, ceiling, why in DECLARATIONS:
        fiber_rows.append({
            "declaration": did, "grain": grain, "ceiling": ceiling,
            "why": why,
            "symmetric_configurations":
                fib["configuration_counts"][did]["SYMMETRIC"],
            "antisymmetric_configurations":
                fib["configuration_counts"][did]["ANTISYMMETRIC"]})
    fib["rows"] = fiber_rows
    fiber_disagreements = pick("MUT-FIBER",
                               fib["one_excitation_disagreements"], 7)
    LD.gate("G-P2-INVISIBLE-FROM-BELOW",
            "THE CEILING IS INVISIBLE FROM BELOW, and this is the premise's "
            "failure made a measurement.  %d declarations are constructed; "
            "they give %d DISTINCT two-excitation theories, with %d, %d and "
            "%d symmetric configurations.  Each one's ONE-EXCITATION "
            "restriction is BUILT FROM ITS OWN DECLARATION -- the cells its "
            "own admissible configurations occupy, the matrix and the Born "
            "shadow restricted to them -- and the four are then compared AS "
            "OBJECTS, entry by entry, at every coin class: %s of %s "
            "comparisons agree.  A declaration that forbade a cell outright, "
            "or a ceiling of zero, would build a different object and this "
            "row would move, which is what makes it a measurement rather "
            "than a comparison of a thing with itself"
            % (fib["declarations"], fib["distinct_two_excitation_theories"],
               fiber_rows[0]["symmetric_configurations"],
               fiber_rows[1]["symmetric_configurations"],
               fiber_rows[2]["symmetric_configurations"],
               com(fib["one_excitation_comparisons"]
                   - fib["one_excitation_disagreements"]),
               com(fib["one_excitation_comparisons"])),
            fiber_disagreements == 0 and fib["restrictions_agree_as_objects"]
            and fib["distinct_one_excitation_objects"] == 1
            and all(n == NCELL for n in
                    fib["one_excitation_restriction_sizes"].values()),
            "disagreements %s over %s comparisons; distinct theories %d; "
            "distinct one-excitation objects %d; restriction sizes %s"
            % (fiber_disagreements, com(fib["one_excitation_comparisons"]),
               fib["distinct_two_excitation_theories"],
               fib["distinct_one_excitation_objects"],
               sorted(set(fib["one_excitation_restriction_sizes"].values()))))

    # P2's verdict is DERIVED from its three legs; the mutant then detaches
    # the published word from the derivation, which is what the gate catches
    legs_ok = (not occ_hits and not ss["two_excitation_constructor_present"]
               and fib["restrictions_agree_as_objects"])
    p2_derived = "NOT-AVAILABLE" if legs_ok else "AVAILABLE"
    p2_verdict = pick("MUT-TURNING", p2_derived, "STRUCTURAL-EXCLUSION")
    R["p2"] = {"vocabulary": voc, "state_space": ss, "fiber": fib,
               "verdict": p2_verdict,
               "reading": "the committed representation neither constructs "
                          "nor forbids a doubly occupied carrier: it has no "
                          "occupancy coordinate at all, and the excitation's "
                          "own coordinate is a co-division pair rather than "
                          "an actor"}
    LD.gate("G-P2-TURNING",
            "P2's verdict is DERIVED from its three legs and not typed: the "
            "vocabulary census (no occupancy-shaped name), the state-space "
            "construction (no excitation-number coordinate) and the "
            "declaration fiber (every declaration restricts to the same "
            "one-excitation object).  A representation that EXCLUDED double "
            "occupancy would have to forbid it; this one cannot express it, "
            "and inexpressibility is not exclusion",
            p2_verdict == p2_derived and legs_ok,
            "P2 = %s against the value its legs derive, %s (legs: occupancy "
            "names %d, excitation parameters %d, restrictions agree %s)"
            % (p2_verdict, p2_derived, len(occ_hits),
               len(ss["excitation_number_parameters"]),
               fib["restrictions_agree_as_objects"]))
    SEAL.take("SEAL-P2", R)

    # -- SEC 8  P3 -----------------------------------------------------------
    p3 = C["p3"]
    site_agree = pick("MUT-BLINDNESS",
                      p3["blindness_pair"]["site_fields_agree_at"], 8)
    bc = p3["blindness_census"]
    read_A = [r for r in bc["rows"] if r["reading"] == "A"][0]
    read_B = [r for r in bc["rows"] if r["reading"] == "B"][0]
    LD.gate("G-P3-BLINDNESS",
            "WHAT THE COMMITTED RULE READS, PER DECLARED READING -- AND THE "
            "BLINDNESS IS THE RECORD MENU'S, NOT THE RULE'S.  Two "
            "two-excitation configurations are built: one with its "
            "excitations on two different cells of a single actor, one with "
            "both on a single cell.  They differ in cell occupation at %d of "
            "%d cells and their SITE fields agree at %d of %d.  The parent "
            "declares the emission reading at fiber %d (F10: the Born menu "
            "against the record menu; both run), so BOTH are applied here, "
            "over a census of every doubly occupied configuration against "
            "every same-site partner: the site field cannot separate %d of "
            "%d such pairs, the RECORD menu separates %d of %d -- the state "
            "does not enter its kernel at all -- and the BORN menu, which is "
            "the reading the parent's own coupled ensemble runs, separates "
            "%d of %d, per cell.  The published blindness is therefore "
            "READING-SCOPED, and the leg that carries P3 is the absent "
            "occupancy coordinate rather than an undifferentiated rule"
            % (p3["blindness_pair"]["cells"]
               - p3["blindness_pair"]["cell_occupations_agree_at"],
               p3["blindness_pair"]["cells"], site_agree,
               p3["blindness_pair"]["sites"],
               p3["emission_reading_fiber"],
               bc["site_field_cannot_separate"], bc["pairs"],
               read_B["separates"], bc["pairs"],
               read_A["separates"], bc["pairs"]),
            (site_agree == p3["blindness_pair"]["sites"]
             and not p3["blindness_pair"]["the_site_field_can_separate_them"]
             and bc["site_field_cannot_separate"] == bc["pairs"]
             and read_B["separates"] == 0
             and read_A["separates"] == bc["pairs"]
             and p3["readings_that_separate_the_witness_pair"] == 1),
            "site fields agree at %d of %d; cell occupations agree at %d of "
            "%d; census pairs %d, site-blind %d, reading B separates %d, "
            "reading A separates %d"
            % (site_agree, p3["blindness_pair"]["sites"],
               p3["blindness_pair"]["cell_occupations_agree_at"],
               p3["blindness_pair"]["cells"], bc["pairs"],
               bc["site_field_cannot_separate"], read_B["separates"],
               read_A["separates"]))

    comp_bad = [r["completion"] for r in p3["completions"]
                if r["preserves_the_parent_identity"]
                and r["emission_total"] != "1"]
    comp_bad = pick("MUT-COMPLETIONS", comp_bad, ["E1-PER-EXCITATION"])
    LD.gate("G-P3-COMPLETIONS",
            "THE DECLARATION THE GRAMMAR IS MISSING IS PRICED.  The committed "
            "emission rule is a rule for ONE excitation; %d completions to "
            "two are constructed and all %d are run.  Their emission totals "
            "are %s, so exactly %d of them preserve the parent's own "
            "consistency identity -- total emission mass exactly 1 -- and "
            "their fields differ pairwise at %s cells.  The missing "
            "declaration is verdict-relevant, not cosmetic"
            % (p3["completion_fiber"], p3["completion_fiber"],
               [r["emission_total"] for r in p3["completions"]],
               p3["completions_preserving_the_parent_identity"],
               [d["cells_differing"] for d in
                p3["pairwise_field_differences"]]),
            not comp_bad
            and p3["completions_preserving_the_parent_identity"]
            < p3["completion_fiber"],
            "completions whose published identity row contradicts their "
            "total: %s" % (comp_bad or "none"))

    refusals = pick("MUT-REFUSAL", p3["completions_that_refuse_a_division"], 1)
    # P3's WORD IS DERIVED FROM ITS LEGS AND COMPARED AGAINST THE PUBLISHED
    # ONE, exactly as P2's is (K1 MINOR-4, K3 MINOR-7).  The refusal count is
    # a PER-COMPLETION read: each completion's own field is built for the
    # doubly occupied state and its support measured (K3 MAJOR-6).
    if refusals > 0:
        p3_derived = "CLOSURE-REQUIRED"
    elif (p3["legs"]["no_occupancy_coordinate_to_condition_on"]
          and p3["completions_whose_menu_is_nonempty"]
          == p3["completion_fiber"]):
        p3_derived = "SILENT-AND-VACUOUSLY-SATISFIED"
    else:
        p3_derived = "CLOSURE-AVAILABLE"
    R["p3"] = p3
    LD.gate("G-P3-NEVER-REFUSED",
            "P3 IS SILENT AND VACUOUSLY SATISFIED, AND ITS WORD IS DERIVED "
            "FROM ITS THREE LEGS RATHER THAN TYPED: the committed grammar has "
            "no occupancy coordinate to condition on (%s), every one of the "
            "%d completions is evaluated ON THE DOUBLY OCCUPIED STATE ITSELF "
            "-- its own field built from that state's own weights -- and %d "
            "of %d leave that state's emission menu nonempty, so %d of %d "
            "refuse a division event to it.  The closure premise cannot "
            "supply an exclusion the grammar has no vocabulary to state"
            % (p3["legs"]["no_occupancy_coordinate_to_condition_on"],
               p3["completion_fiber"],
               p3["completions_whose_menu_is_nonempty"],
               p3["completion_fiber"], refusals, p3["completion_fiber"]),
            (refusals == 0 and p3["doubly_occupied_carrier_emits"]
             and p3["verdict"] == p3_derived
             and all(r["support_on_the_doubly_occupied_state"] > 0
                     for r in p3["completions"])),
            "completions that refuse: %d; the doubly occupied carrier emits: "
            "%s; P3 = %s against the value its legs derive, %s; per-completion "
            "Q-side supports %s"
            % (refusals, p3["doubly_occupied_carrier_emits"], p3["verdict"],
               p3_derived, [r["support_on_the_doubly_occupied_state"]
                            for r in p3["completions"]]))
    SEAL.take("SEAL-P3", R)

    # -- SEC 9  P4 -----------------------------------------------------------
    sel = C["selection"]
    grain_bad = []
    for row in C["leaks"]:
        for did, _g, _c, _w in DECLARATIONS:
            for sh in SHAPES:
                cellrow = row["%s|%s" % (did, sh)]
                if cellrow["closed"] != (cellrow["leak_cells"] == 0):
                    grain_bad.append(row["coin"])
    # THE UNIVERSAL IS BOUND PER COIN, and it is NOT universal: at the
    # actor's grain every admissible source leaks and every forbidden target
    # is reached EXACTLY at the non-monomial classes, and the monomial class
    # carries its own 81-of-216 and 81-of-135 predicate (K1 MAJOR-4).
    full_leak_bad = []
    for r in ag:
        mono = [p for p in pool_rows if p["coin"] == r["coin"]][0]["monomial"]
        full = (r["actor_grain_sources_leaking"]
                == R["leaks"]["actor_grain_admissible"]
                and r["actor_grain_targets_reached"]
                == R["leaks"]["actor_grain_forbidden"])
        if full == mono:
            full_leak_bad.append(r["coin"])
        if mono and not (r["actor_grain_sources_leaking"]
                         == R["leaks"]["actor_grain_sources_leaking_min"]
                         and r["actor_grain_targets_reached"]
                         == R["leaks"]["actor_grain_targets_reached_min"]):
            full_leak_bad.append(r["coin"])
    grain_bad = pick("MUT-GRAIN-CENSUS", grain_bad + full_leak_bad,
                     ["K-2+0w"])
    R["selection"] = sel
    LD.gate("G-P4-GRAIN-CENSUS",
            "P4, AND THE GATE BINDS COINS RATHER THAN THE TALLY: every one of "
            "the %d coin classes carries its own leak row at every one of the "
            "%d declarations and in both shapes, every row's closure "
            "predicate is evaluated against its own measured leak, and the "
            "actor grain's COMPLETENESS is bound per coin in both directions "
            "-- every admissible source leaks and every forbidden target is "
            "reached at exactly the NON-MONOMIAL classes (%d of %d), while "
            "the monomial class carries its own %d-of-%d and %d-of-%d row.  "
            "%d (coin, declaration) selection rows are published"
            % (len(pool_rows), len(DECLARATIONS),
               R["leaks"]["actor_grain_coins_where_every_admissible_source_"
                          "leaks"], len(pool_rows),
               R["leaks"]["actor_grain_sources_leaking_min"],
               R["leaks"]["actor_grain_admissible"],
               R["leaks"]["actor_grain_targets_reached_min"],
               R["leaks"]["actor_grain_forbidden"], len(sel)),
            not grain_bad, "rows whose closure verdict is detached from "
            "their leak, or whose completeness does not track monomiality: %s"
            % (grain_bad or "none"))
    SEAL.take("SEAL-SELECTION", R)

    seteq_bad = [r["coin"] for r in ag
                 if r["carrier_grain_leak_sources"]
                 and not (r["carrier_grain_sources_are_the_same_site_"
                            "configurations"] is True
                          and r["carrier_grain_sources_are_the_same_actor_"
                                "configurations"] is False
                          and r["carrier_grain_sources_are_actor_grain_"
                                "forbidden"] is True
                          and r["carrier_grain_containment_is_strict"] is True
                          and r["same_actor_configurations_excluded"]
                          == R["leaks"]["same_actor_configurations_excluded"])]
    seteq_bad = pick("MUT-SET-EQUALITY", seteq_bad, ["FORGED"])
    LD.gate("G-P4-SET-EQUALITY",
            "THE TWO GRAINS ARE NOT INDEPENDENT, AND THE LINK IS A SET "
            "EQUALITY WITH THE SAME-SITE SET AND A STRICT CONTAINMENT IN THE "
            "SAME-ACTOR ONE.  At the carrier's own grain the symmetric shape "
            "leaks from exactly %d configurations, and that set IS the set of "
            "configurations whose two excitations sit on two of the three "
            "cells of ONE SITE -- and it is NOT the set of configurations "
            "whose cells share an ACTOR, which has %d members.  BOTH set "
            "equalities are evaluated element for element at every leaking "
            "coin class, the containment 27-in-135 is evaluated element by "
            "element, and its strictness is published with the %d "
            "configurations it excludes.  Every side of every equality names "
            "the object it holds"
            % (R["arena"]["same_site_configurations"],
               R["arena"]["same_actor_configurations"],
               R["leaks"]["same_actor_configurations_excluded"]),
            not seteq_bad, "coins whose leak source set is not the same-site "
            "set, or not strictly inside the same-actor set: %s"
            % (seteq_bad or "none"))

    coincide_bad = [r["coin"] for r in ag
                    if not r["actor_grain_shape_leak_sets_coincide"]]
    coincide_bad = pick("MUT-SHAPES-COINCIDE", coincide_bad, ["FORGED"])
    LD.gate("G-P4-SHAPES-COINCIDE",
            "AT THE ACTOR'S GRAIN THE TWO SHAPES LEAK AT THE SAME CELLS.  For "
            "a target pair of cells sharing an actor the two products of the "
            "lifted element are supported on disjoint source pairs -- "
            "measured at %d cells in the whole run where both are nonzero -- "
            "so no cancellation is available to either shape and the wedge "
            "and the symmetric square leak at identical source sets, "
            "identical target sets and identical counts, at every coin class"
            % R["leaks"]["actor_grain_cancellation_cells"],
            not coincide_bad, "coins whose two shapes' leak sets differ: %s"
            % (coincide_bad or "none"))

    ps = C["parent_split"]
    leaking_cited = pick("MUT-PARENT-SPLIT", ps["symmetric_leaking"], 47)
    R["p4"] = {"parent_split": ps, "rows": len(C["leaks"]),
               "declarations": len(DECLARATIONS)}
    LD.gate("G-P4-PARENT-SPLIT",
            "PAPER-22'S SPLIT IS CITED FROM ITS OWN COMMITTED ROWS AND NEVER "
            "RETYPED: its %d generators split %d leaking against %d closed in "
            "the symmetric shape, with %d leaking in the antisymmetric one, "
            "and this unit RECOMPUTES that split from the parent's receipt "
            "rather than reading its prose"
            % (ps["generators"], ps["symmetric_leaking"],
               ps["symmetric_closed"], ps["antisymmetric_leaking"]),
            (leaking_cited + ps["symmetric_closed"] == ps["generators"]
             and ps["antisymmetric_leaking"] == 0),
            "cited split %d + %d = %d; antisymmetric leaking %d"
            % (leaking_cited, ps["symmetric_closed"], ps["generators"],
               ps["antisymmetric_leaking"]))
    SEAL.take("SEAL-P4", R)

    # -- SEC 10  THE ARMS ----------------------------------------------------
    controls = C["controls"]
    arms = build_arms(p1, R["p2"], p3, sel, controls)
    R["arms"] = arms
    R["controls"] = controls
    words_seen = sorted({a["word"] for a in arms})
    words_seen = pick("MUT-ARMS", words_seen,
                      [w for w in words_seen if w != "OCC-CEILING-FORCED"])
    # THE SEED CONDITIONAL'S OWN VERDICT, DERIVED FROM TWO MEASURED CLAUSES
    # and compared here against the adjudicated word (K2 R2).  Clause one is
    # a TYPE measurement (the injection premise names actors and the
    # excitation-to-actor relation is not a function); clause two is a LEAK
    # measurement (supply that injection as a declaration at the grain it
    # typed -- arm A2 -- and the conclusion fails).
    a2_arm = [a for a in arms
              if a["arm"] == "A2-DECLARED-EXCLUSION-AT-THE-ACTOR-GRAIN"][0]
    seed_clauses = []
    if not p1["excitation_to_actor_is_a_function"]:
        seed_clauses.append("MISTYPED-AT-THE-CARRIER")
    if (a2_arm["p2"] == "DECLARED-EXCLUSION"
            and a2_arm["p4"] == "NO-SHAPE-CLOSES"
            and a2_arm["word"] != "OCC-CEILING-FORCED"):
        seed_clauses.append("REFUTED-AT-THE-GRAIN-IT-TYPED")
    seed_word = ";".join(seed_clauses)
    LD.gate("G-ARMS-REACHABILITY",
            "#34 WITH REACHABILITY, AT THE HEAD LAW: the head is derived from "
            "the four premise verdicts and is exercised on %d arenas, on "
            "which it returns %d DIFFERENT pre-registered outcome words -- "
            "the whole pre-registered outcome set, compared AS A SET rather "
            "than by cardinality.  Every branch of the law is reached on a "
            "CONSTRUCTED arena rather than on a synthetic census, and the "
            "verdict arena is the committed one.  The seed conditional's own "
            "verdict is derived here from two measured clauses -- the type "
            "measurement at the carrier and arm A2's leak measurement at the "
            "grain it typed -- and compared against the adjudicated word"
            % (len(arms), len(words_seen)),
            set(words_seen) == set(OUTCOMES)
            and seed_word == SEED_CONDITIONAL_WORD,
            "words returned: %s; outcome set matches %s; seed conditional "
            "derived %s against the adjudicated %s"
            % (words_seen, set(words_seen) == set(OUTCOMES), seed_word,
               SEED_CONDITIONAL_WORD))
    SEAL.take("SEAL-ARMS", R)

    c1 = [c for c in controls if c["arena"] == "C1-SUBSET-CARRIER"][0]
    c2 = [c for c in controls if c["arena"] == "C2-MULTISET-CARRIER"][0]
    fires = pick("MUT-CONTROL", c1["selects"], False)
    LD.gate("G-CONTROL-TWO-WAY",
            "THE TWO-WAY CONTROL THE PIN REQUIRES.  On a carrier whose "
            "configurations are SUBSETS -- double occupancy not expressible "
            "-- exactly one shape closes and the conditional FIRES.  On the "
            "same carrier with MULTISET configurations -- double occupancy "
            "constructible -- both shapes close and it FAILS.  The two arms "
            "differ in the configuration rule and in nothing else: same "
            "carrier size, same generator, same lift, same census code",
            (fires and not c2["selects"] and c1["carriers"] == c2["carriers"]
             and c1["unitarity_violations"] == 0
             and c2["unitarity_violations"] == 0),
            "subset arm selects %s (shapes closed %s); multiset arm selects "
            "%s (shapes closed %s)"
            % (fires, c1["shapes_closed"], c2["selects"], c2["shapes_closed"]))
    SEAL.take("SEAL-CONTROLS", R)

    asym = asymmetry_row(sel)
    wedge = R["leaks"]["wedge_theorem"]
    site_arm = R["leaks"]["site_grain_arm"]
    asym["mechanism_theorem"] = {
        "grains_tested": wedge["grains"],
        "rows": wedge["rows"],
        "empty_iff_the_carrier_grain": wedge["empty_iff_the_carrier_grain"],
        "statement": wedge["statement"]}
    asym["third_grain_residual"] = {
        "grain": site_arm["grain"], "coins": site_arm["coins"],
        "coins_that_select": site_arm["coins_that_select"],
        "coins_where_no_shape_closes":
            site_arm["coins_where_no_shape_closes"],
        "admissible": site_arm["admissible"]}
    perm_selects = pick("MUT-ASYMMETRY",
                        asym["permission_rows_that_select"], 1)
    R["asymmetry"] = asym
    LD.gate("G-ASYMMETRY",
            "THE ONE-WAY ASYMMETRY, RESTATED AT THE MEASURED VERDICT AND "
            "GATED AGAINST BOTH ARMS.  A declaration that PERMITS selects a "
            "shape at %d of %d rows.  A declaration that FORBIDS selects at "
            "%d of %d -- and every one of those is at the carrier's own "
            "grain: at the actor's grain exclusion selects at %d of %d rows, "
            "because at %d of them NO shape closes at all.  Exclusion can "
            "select a shape and permission cannot, and exclusion selects only "
            "at the grain the excitation's own coordinate has"
            % (perm_selects, asym["permission_rows"],
               asym["exclusion_rows_that_select"], asym["exclusion_rows"],
               asym["exclusion_at_the_actor_grain_selects"],
               asym["exclusion_at_the_actor_grain_rows"],
               asym["actor_grain_rows_where_no_shape_closes"])
            + ".  THE 'ONLY' IS A THEOREM PLUS A RESIDUAL, not a two-point "
              "census: under a hard core at grain G the antisymmetric "
              "sector's forbidden set is the set of distinct-cell pairs that "
              "collide under G, and it is EMPTY IF AND ONLY IF G is the "
              "carrier's own grain -- measured per object over the %d grains "
              "this arena admits, at %d, %d and %d forbidden configurations "
              "-- so the automatic closure that makes exclusion selective "
              "exists at the carrier's grain and structurally nowhere else.  "
              "The residual is then one census per coarser grain, and the "
              "SITE grain -- a genuine function of the cell, unlike the "
              "actor relation -- selects at %d of %d coins, with no shape "
              "closing at %d of %d"
            % (wedge["grains"],
               wedge["rows"][0]["antisymmetric_forbidden"],
               wedge["rows"][1]["antisymmetric_forbidden"],
               wedge["rows"][2]["antisymmetric_forbidden"],
               site_arm["coins_that_select"], site_arm["coins"],
               site_arm["coins_where_no_shape_closes"], site_arm["coins"]),
            (perm_selects == 0
             and asym["exclusion_at_the_actor_grain_selects"] == 0
             and asym["exclusion_rows_that_select"] > 0
             and wedge["empty_iff_the_carrier_grain"]
             and all(r["antisymmetric_forbidden_set_is_empty"]
                     == r["is_the_carrier_grain"] for r in wedge["rows"])
             and site_arm["coins_that_select"] == 0
             and site_arm["coins_where_no_shape_closes"] == site_arm["coins"]),
            "permission selects %d of %d; exclusion %d of %d; at the actor "
            "grain %d of %d; wedge forbidden sets %s (empty iff the carrier "
            "grain: %s); the site grain selects %d of %d"
            % (perm_selects, asym["permission_rows"],
               asym["exclusion_rows_that_select"], asym["exclusion_rows"],
               asym["exclusion_at_the_actor_grain_selects"],
               asym["exclusion_at_the_actor_grain_rows"],
               [(r["grain"], r["antisymmetric_forbidden"])
                for r in wedge["rows"]],
               wedge["empty_iff_the_carrier_grain"],
               site_arm["coins_that_select"], site_arm["coins"]))
    SEAL.take("SEAL-ASYMMETRY", R)

    # -- THE COUNTS, assembled before anything renders from them ------------
    p4_committed = p4_word(sel, "D-ACTOR-1")
    verdict_arm = [a for a in arms if a["role"] == "THE VERDICT ARENA"][0]
    R["counts"] = {
        "outcome_word": verdict_arm["word"],
        "seed_conditional": seed_word,
        "seed_conditional_clauses": len(seed_clauses),
        "p4_word": p4_committed,
        "distinct_outcome_words": len({a["word"] for a in arms}),
        "arms": len(arms),
        "control_fires": c1["arena"],
        "control_fails": c2["arena"],
        "fiber_priced": "%d-DECLARATIONS-%d-THEORIES-%d-EMISSION-COMPLETIONS"
                        % (fib["declarations"],
                           fib["distinct_two_excitation_theories"],
                           p3["completion_fiber"]),
        "scope_row": SCOPE_ROW,
        "coins": len(pool_rows),
        "declarations": len(DECLARATIONS),
        "selection_rows": len(sel),
        "same_actor_configurations": C["same_actor_configurations"],
        "same_site_configurations": C["same_site_configurations"],
        "leak_rows": route_rows,
        "gates": len(LD.rows),
    }

    # -- DESCRIPTION STAMPS AND E-24 ----------------------------------------
    claims = paper_claims(R)
    stamps = []
    for cid, _text in claims:
        stamps.append({"claim": cid, "sector": "BOTH-EXCHANGE-SHAPES",
                       "lift": "FREE(U-TENSOR-U)",
                       "grain": "CARRIER-AND-ACTOR-BOTH-MEASURED",
                       "ceiling": "DECLARED-BY-THIS-UNIT-IN-BOTH-VALUES",
                       "coin": "ALL-6-CLASSES",
                       "arena": "THE-WELDED-LANDING-RECORD",
                       "excitations": 2})
    stamp_bad = pick("MUT-STAMPS",
                     [c for c, _t in claims
                      if c not in {s["claim"] for s in stamps}], ["C08"])
    R["description_stamps"] = stamps
    LD.gate("G-DESCRIPTION-STAMPS",
            "every published claim carries a DESCRIPTION STAMP naming the "
            "sector, the lift, the grain, the ceiling, the coin class and the "
            "arena it was measured on: %d claims, %d stamps.  No claim about "
            "a quantum-layer quantity is published without the description "
            "that individuates it" % (len(claims), len(stamps)),
            not stamp_bad, "claims without a stamp: %s"
            % (stamp_bad or "none"))
    SEAL.take("SEAL-STAMPS", R)

    # E-24: EVERY published ratio's denominator is re-counted from the
    # construction it claims to enumerate -- a per-object check over the head
    # itself, not four hand-picked rows beside a stamp (K3 MAJOR-5).  Each
    # entry names a re-count that is built HERE from the construction, never
    # read from the row it certifies.
    recount = {
        "coins": (len(pool_rows), "the S_3-covariant coin classes up to a "
                                  "global phase, re-counted from the ring "
                                  "census"),
        "actors": (len(SITES), "the arena's actors, re-counted from the "
                               "rebuilt site set"),
        "cells": (len(CELL_PAIR), "the carrier's cells, re-counted from the "
                                  "rebuilt cell-to-pair map"),
        "carrier_grain_coins_leaking":
            (sum(1 for r in pool_rows
                 if r["carrier_grain_symmetric_leak"] > 0),
             "the coins whose carrier-grain symmetric leak is nonzero"),
        "same_actor_configurations":
            (len([1 for a, b in combinations(range(NCELL), 2)
                  if share_an_actor(a, b)]),
             "the two-excitation configurations whose cells share an actor"),
        "actor_grain_admissible":
            (len(admissible_configs("ACTOR", 1, "ANTISYMMETRIC")),
             "the two-excitation configurations the actor-grain hard core "
             "admits"),
        "actor_grain_forbidden":
            (len(all_configs()[0])
             - len(admissible_configs("ACTOR", 1, "ANTISYMMETRIC")),
             "the two-excitation configurations it forbids"),
        "grains": (len(GRAINS), "the grains the arena admits, re-counted "
                                "from the declared grain map"),
        "site_grain_coins": (len(pool_rows),
                             "the coin classes, re-counted for the site-grain "
                             "residual"),
        "record_probe_fields": (len(RECORD_PROBES),
                                "the declared count-field probes"),
        "leak_rows": (len(pool_rows) * len(DECLARATIONS) * len(SHAPES),
                      "coin classes times declarations times shapes"),
        "parent_generators": (len(receipts["A-P22REC"]["occupancy"]["rows"]),
                              "paper-22's own committed generator rows"),
        "declarations": (len(DECLARATIONS),
                         "the declarations this unit constructs"),
        "one_excitation_comparisons":
            (len(pool_rows) * sum(
                (lambda k: k + 2 * k * k)(len(one_excitation_space(
                    DECLARATIONS[DECLARATION_IDS.index(a)][1],
                    DECLARATIONS[DECLARATION_IDS.index(a)][2])))
                for a, _b in combinations(DECLARATION_IDS, 2)),
             "over every coin and every declaration pair, the first "
             "declaration's own restriction: its configuration set once and "
             "its matrix and its Born shadow entry by entry"),
        "sites": (len(site_field([0] * NCELL)),
                  "the arena's sites, re-counted from the site field the "
                  "committed rule reads"),
        "blindness_census_pairs":
            (NCELL * len(list(combinations(range(3), 2))),
             "every doubly occupied configuration against every one of its "
             "same-site partners"),
        "completions": (p3["completion_fiber"],
                        "the declared emission completions, all run"),
        "permission_rows": (len(pool_rows) * len(
            [d for d in DECLARATIONS if d[2] == 2]),
            "coin classes times the permission declarations"),
        "exclusion_rows": (len(pool_rows) * len(
            [d for d in DECLARATIONS if d[2] == 1]),
            "coin classes times the exclusion declarations"),
        "actor_grain_exclusion_rows": (len(pool_rows),
                                       "coin classes times the actor-grain "
                                       "exclusion declaration"),
        "arms": (len(arms), "the arenas the head law is exercised on"),
    }
    # every X-OF-Y field of the head, bound to its own re-count
    RATIO_DENOMINATORS = {
        "ACTOR-SITE-BIJECTION": "actors",
        "CELLS-WITH-EXACTLY-TWO-ACTORS": "cells",
        "ACTORS-IN-EXACTLY-SIX-CELLS": "actors",
        "NON-MONOMIAL-COINS": "coins",
        "CARRIER-GRAIN-COINS-LEAKING": "coins",
        "CARRIER-GRAIN-LEAK-SOURCES-ARE-THE-SAME-SITE-CONFIGURATIONS":
            "carrier_grain_coins_leaking",
        "CARRIER-GRAIN-LEAK-SOURCES-ARE-THE-SAME-ACTOR-CONFIGURATIONS":
            "carrier_grain_coins_leaking",
        "CARRIER-GRAIN-LEAK-SOURCES-ARE-ACTOR-GRAIN-FORBIDDEN":
            "same_actor_configurations",
        "CARRIER-GRAIN-CONTAINMENT-IS-STRICT": "carrier_grain_coins_leaking",
        "ACTOR-GRAIN-COINS-WHERE-BOTH-SHAPES-LEAK": "coins",
        "ACTOR-GRAIN-SHAPE-LEAK-SETS-COINCIDE": "coins",
        "ACTOR-GRAIN-SOURCES-LEAKING-MAX": "actor_grain_admissible",
        "ACTOR-GRAIN-SOURCES-LEAKING-MIN": "actor_grain_admissible",
        "ACTOR-GRAIN-TARGETS-REACHED-MAX": "actor_grain_forbidden",
        "ACTOR-GRAIN-TARGETS-REACHED-MIN": "actor_grain_forbidden",
        "ACTOR-GRAIN-COINS-WHERE-EVERY-ADMISSIBLE-SOURCE-LEAKS": "coins",
        "ACTOR-GRAIN-COINS-WHERE-EVERY-FORBIDDEN-TARGET-IS-REACHED": "coins",
        "WEDGE-FORBIDDEN-SET-EMPTY-IFF-THE-CARRIER-GRAIN": "grains",
        "SITE-GRAIN-COINS-THAT-SELECT": "site_grain_coins",
        "SITE-GRAIN-COINS-WHERE-NO-SHAPE-CLOSES": "site_grain_coins",
        "P4-IS-RECORD-BLIND-AT-THE-PROBED-COUNT-FIELDS": "record_probe_fields",
        "LEAK-ROUTES-AGREE": "leak_rows",
        "PARENT-SPLIT-CITED": "parent_generators",
        "P2-DECLARATION-FIBER": "declarations",
        "P2-ONE-EXCITATION-RESTRICTIONS-AGREE": "one_excitation_comparisons",
        "P3-BLINDNESS-PAIR-SITE-FIELDS-AGREE": "sites",
        "P3-SITE-FIELD-CANNOT-SEPARATE": "blindness_census_pairs",
        "P3-RECORD-MENU-READING-SEPARATES": "blindness_census_pairs",
        "P3-BORN-MENU-READING-SEPARATES": "blindness_census_pairs",
        "P3-COMPLETIONS-PRESERVING-THE-PARENT-IDENTITY": "completions",
        "P3-COMPLETIONS-THAT-REFUSE-A-DIVISION": "completions",
        "ASYMMETRY-PERMISSION-ROWS-THAT-SELECT": "permission_rows",
        "ASYMMETRY-EXCLUSION-ROWS-THAT-SELECT": "exclusion_rows",
        "ASYMMETRY-AT-THE-ACTOR-GRAIN": "actor_grain_exclusion_rows",
        "ARMS": "arms",
    }
    enums = []
    for seg, fields in field_spec(R):
        for lab, val in fields:
            m = re.match(r"^(\d+)-OF-(\d+)$", render_field(val))
            if not m:
                continue
            key = RATIO_DENOMINATORS.get(lab)
            got, why = recount.get(key, (None, "NO RE-COUNT DECLARED"))
            enums.append({"ratio": "%s/%s" % (seg, lab),
                          "denominator": int(m.group(2)),
                          "measured": got, "enumeration": why,
                          "recount_key": key})
    for e in enums:
        e["denominator_matches_its_enumeration"] = (e["denominator"]
                                                    == e["measured"])
    measure_declared = pick("MUT-COUNTING",
                            any(e.get("measure") for e in enums), True)
    enum_bad = [e["ratio"] for e in enums
                if not e["denominator_matches_its_enumeration"]]
    R["counting_only"] = {
        "stamp": "COUNTING-ONLY", "measure_declared": measure_declared,
        "enumerations": enums,
        "note": "no measure on configurations, coins, declarations or arenas "
                "is declared anywhere in this unit, so every fraction is a "
                "count over its declared enumeration and none is a "
                "probability"}
    LD.gate("G-COUNTING-ONLY",
            "E-24: no count becomes a probability without a declared measure. "
            "Every ratio this unit publishes is a COUNT over a declared "
            "enumeration, and the check binds OBJECTS AND IS TOTAL: the head "
            "is walked field by field, every one of the %d X-OF-Y ratios in "
            "it is picked up, and each one's DENOMINATOR is re-counted from "
            "the construction it claims to enumerate -- %d distinct "
            "re-counts, each built here from the construction and never read "
            "from the row it certifies -- so a ratio taken over a set other "
            "than the one it claims dies here, and a new ratio with no "
            "declared re-count dies here too.  No enumeration carries a "
            "measure, and the receipt is stamped COUNTING-ONLY"
            % (len(enums), len({e["recount_key"] for e in enums})),
            not measure_declared and not enum_bad and len(enums) > 0,
            "ratios re-counted %d over %d distinct enumerations; measure "
            "declared: %s; ratios whose denominator does not match their own "
            "re-count: %s; stamp %s"
            % (len(enums), len({e["recount_key"] for e in enums}),
               measure_declared, enum_bad or "none",
               R["counting_only"]["stamp"]))
    SEAL.take("SEAL-COUNTING", R)

    lifts = ("FREE(U-TENSOR-U)", "CONTACT", "DISTINGUISHABLE")
    choices = [
        {"item": "the grain a ceiling is declared at (DECLARED MENU; the "
                 "space is larger -- the site grain is run as a residual)",
         "fiber": len({d[1] for d in DECLARATIONS}), "class": "MEASURED-BOTH",
         "verdict_determining": "YES"},
        {"item": "the ceiling value",
         "fiber": len({d[2] for d in DECLARATIONS}), "class": "MEASURED-BOTH",
         "verdict_determining": "YES"},
        {"item": "the two-excitation lift", "fiber": len(lifts),
         "class": "INHERITED-AS-DECLARED", "verdict_determining": "no"},
        {"item": "the coin class", "fiber": len(pool_rows),
         "class": "MEASURED-ALL", "verdict_determining": "no"},
        {"item": "the emission completion", "fiber": p3["completion_fiber"],
         "class": "DECLARED-AND-ALL-RUN", "verdict_determining": "no"},
        {"item": "the emission reading (the parent's own F10 fiber)",
         "fiber": p3["emission_reading_fiber"], "class": "MEASURED-BOTH",
         "verdict_determining": "no"},
        {"item": "the control arenas", "fiber": len(controls),
         "class": "DECLARED-CONTROL", "verdict_determining": "no"},
        {"item": "the record, the carrier, the links, the coin order",
         "fiber": 1, "class": "FORCED", "verdict_determining": "no"},
    ]
    R["choice_inventory"] = choices
    determining = [c["item"] for c in choices
                   if c["verdict_determining"] == "YES"]
    choice_bad = pick("MUT-CHOICES",
                      [c["item"] for c in choices if c["fiber"] < 1],
                      ["the coin class"])
    LD.gate("G-CHOICE-INVENTORY",
            "the choice inventory is published AS DATA at the RSQ standard, "
            "with every fiber a COUNTED value rather than a typed one: %d "
            "items, of which %d are verdict-determining -- the grain and the "
            "ceiling value, which are the two halves of the one declaration "
            "no committed layer makes" % (len(choices), len(determining)),
            not choice_bad and len(determining) == 2,
            "items with an uncounted fiber: %s; verdict-determining items: %s"
            % (choice_bad or "none", determining))
    SEAL.take("SEAL-CHOICES", R)

    # -- SEC 12  THE WALLS ---------------------------------------------------
    layer_base = measurement_layer(R, LD)
    wall_rows = []
    # the four walls, each its own statement so that its falsifier's SYMBOL
    # and VALUE are both readable from this file's own AST (E-23)
    layer = pick("MUT-WALL-L1", layer_base,
                 layer_base + " order-level covariance is established")
    wall_rows.append(wall_gate(LD, "G-WALL-L1", layer))
    layer = pick("MUT-WALL-BHS", layer_base,
                 layer_base + " boosted rest frame")
    wall_rows.append(wall_gate(LD, "G-WALL-BHS", layer))
    layer = pick("MUT-WALL-KR", layer_base, layer_base + " myrheim-meyer")
    wall_rows.append(wall_gate(LD, "G-WALL-KR", layer))
    layer = pick("MUT-WALL-COSMO", layer_base,
                 layer_base + " cosmological expansion")
    wall_rows.append(wall_gate(LD, "G-WALL-COSMO", layer))
    R["walls"] = {"rows": wall_rows,
                  "measurement_layer_chars": len(layer_base),
                  "licensed_compounds": list(LICENSED_COMPOUNDS),
                  "banned_words": list(BANNED_WORDS)}

    # -- SEC 13  THE VERDICT -------------------------------------------------
    segs = build_verdict(R)
    R["verdict"] = segs
    payload_probe = json.dumps(R, indent=1, sort_keys=True, default=str)
    rec = reconstruct(payload_probe, segs)
    R["verdict_audit"] = rec
    LD.gate("G-VERDICT-RECONSTRUCTED",
            "THE COMPARATOR IS DE-TWINNED (the SMU lesson: two routes that "
            "TYPE THE SAME TEMPLATE audit the template and not the "
            "measurement).  The head is not prose with numbers in it: it is a "
            "sequence of LABEL=VALUE fields built from a declared field spec, "
            "and the audit route types NO COPY of it.  It PARSES the "
            "delivered segments, looks every label up in its own "
            "independently typed map from label to receipt path, compares "
            "%d fields against the serialized receipt, re-derives each "
            "segment's thesis from the predicate that selects it, and "
            "re-derives the outcome word from the premise rows by its own "
            "copy of the head law" % rec["fields_checked"],
            not rec["field_mismatches"]
            and rec["outcome_word_rederived"] == R["counts"]["outcome_word"],
            "mismatches %s; word re-derived %s against %s"
            % (rec["field_mismatches"][:4] or "none",
               rec["outcome_word_rederived"], R["counts"]["outcome_word"]))

    measured = licensed_numerals(
        {k: R[k] for k in MEASURED_KEYS if k in R and k != "verdict"}, set())
    head_unmeasured = sorted(n for n in head_numerals(segs)
                             if n not in measured)
    head_unmeasured = pick("MUT-HEAD-LITERAL", head_unmeasured, ["4242"])
    LD.gate("G-VERDICT-NO-TYPED-LITERAL",
            "no numeral in the head is a typed literal: every one of them is "
            "required to occur as a MEASURED value in the receipt's own "
            "measurement layer, so a number that was written rather than "
            "computed has nowhere to hide",
            not head_unmeasured,
            "head numerals not occurring among the measured values: %s"
            % (head_unmeasured or "none"))
    SEAL.take("SEAL-VERDICT", R)
    SEAL.take("SEAL-VERDICT-AUDIT", R)
    SEAL.take("SEAL-COUNTS", R)

    # -- THE PAPER -----------------------------------------------------------
    if do_paper and paper_text is not None:
        run_paper_gates(LD, SEAL, R, segs, paper_text)
    elif do_paper:
        raise GateFail("G-PAPER-CLAIMS :: the object under test is absent")
    return LD, SEAL, R, segs, C


def run_paper_gates(LD, SEAL, R, segs, text):
    """the paper is verified INSIDE the delivery run (#20): every claim
    renders from a receipt value and must occur exactly once, every table row
    renders from this run, every numeral is licensed, the head is matched
    verbatim and the fenced blocks are compared as a MULTISET."""
    claims = paper_claims(R)
    rows, missing = [], []
    for cid, sent in claims:
        sent = pick("MUT-PAPER-CLAIM", sent, "26 cells")
        occ = canon(text).count(canon(sent))
        rows.append({"id": cid, "claim": sent, "occurrences": occ})
        if occ != 1:
            missing.append("%s(%d)" % (cid, occ))
    R["paper_claims"] = rows
    LD.gate("G-PAPER-CLAIMS",
            "every one of the %d load-bearing claims is ASSEMBLED FROM THIS "
            "RUN's measurements and required to occur in the object under "
            "test EXACTLY ONCE -- an occurrence count, not a containment test"
            % len(claims),
            not missing, "claims not occurring exactly once: %s"
            % (missing or "none"))
    SEAL.take("SEAL-PAPER-CLAIMS", R)

    trows = paper_tables(R)
    trows = pick("MUT-PAPER-TABLE", trows,
                 trows[:-1] + [("T-FORGED", "| FORGED | 0 |")])
    tbad = []
    for tid, row in trows:
        if canon(text).count(canon(row)) != 1:
            tbad.append(tid)
    # TOTAL COVERAGE, IN BOTH DIRECTIONS: every DATA row of every markdown
    # table in the object under test must be one of the rows this run
    # rendered.  A table the instrument does not render is a table nothing
    # binds, so an unrendered row is a finding and not a licence.
    rendered = {canon(r) for _t, r in trows}
    header_like = re.compile(r"^\|[\s:|-]*\|$")
    lines = [ln.strip() for ln in mdstrip(text).split("\n")]
    paper_rows, headers, unrendered = 0, 0, []
    for i, s in enumerate(lines):
        if not (s.startswith("|") and s.endswith("|")):
            continue
        if header_like.match(s):
            continue                                   # the separator row
        nxt = lines[i + 1] if i + 1 < len(lines) else ""
        if header_like.match(nxt):
            headers += 1
            continue                                   # a column header
        paper_rows += 1
        if canon(s) not in rendered:
            unrendered.append(s[:60])
    R["paper_tables"] = {
        "rows": [{"id": t, "row": r} for t, r in trows],
        "rendered_rows": len(trows), "column_headers": headers,
        "data_rows_in_the_paper": paper_rows,
        "rows_no_gate_renders": unrendered}
    LD.gate("G-PAPER-TABLES",
            "E-22: TABLES RENDER AS CLAIMS, AND THE COVERAGE IS TOTAL IN BOTH "
            "DIRECTIONS.  Every one of the %d rows of the FOUR load-bearing "
            "tables -- the pool at both grains, the six arms, the four "
            "declarations and the choice inventory -- is rendered from this "
            "run and required to occur in the paper exactly once, so a moved "
            "cell or an inverted closure verdict dies inside the run; and "
            "every one of the %d data rows the object under test carries is "
            "required to BE one of them, so a table row no gate renders "
            "cannot be smuggled in beside them" % (len(trows), paper_rows),
            not tbad and not unrendered,
            "table rows not occurring exactly once: %s; paper rows no gate "
            "renders: %s" % (tbad or "none", unrendered or "none"))
    SEAL.take("SEAL-PAPER-TABLES", R)

    cov = paper_coverage(R, text, segs)
    unregistered = pick("MUT-PAPER-NUMERAL", cov["unregistered"],
                        ["123456789"])
    cov["unregistered"] = unregistered
    R["paper_coverage"] = cov
    LD.gate("G-PAPER-NUMERAL-COVERAGE",
            "#20 WITH THE FENCED-BLOCK ADDENDUM AND E-22's INLINE-SPAN "
            "ADDENDUM: %d numerals are scanned -- %d in prose, %d inside the "
            "%d fenced blocks and %d inside the %d inline code spans -- "
            "together with the %d SPELLED numerals above twelve, which house "
            "style writes as words and a digit scan is blind to.  Every one "
            "must be licensed by a MEASURED receipt value or by a declared "
            "structural numeral, and the licensed set is now the measured "
            "INTEGERS plus the declared exact-rational rows: prose is not a "
            "licence, and neither is a digest, a source's byte length or an "
            "anchor's character count.  The structural whitelist is itself "
            "measured -- %d declared, %d needed by this object, %d declared "
            "and unused, %d digest-shaped -- so it cannot grow silently"
            % (cov["scanned"],
               cov["scanned"] - cov["fenced_numerals"] - cov["inline_numerals"],
               cov["fenced_numerals"], cov["fenced_blocks"],
               cov["inline_numerals"], cov["inline_spans"],
               cov["spelled_numerals_scanned"],
               cov["structural_numerals_declared"],
               len(cov["structural_numerals_the_object_needs"]),
               len(cov["structural_numerals_declared_and_unused"]),
               len(cov["structural_numerals_that_are_digest_shaped"])),
            not unregistered
            and not cov["structural_numerals_declared_and_unused"]
            and not cov["structural_numerals_that_are_digest_shaped"],
            "unlicensed numerals: %s; structural numerals declared and "
            "unused: %s; digest-shaped: %s"
            % (unregistered[:8] or "none",
               cov["structural_numerals_declared_and_unused"] or "none",
               cov["structural_numerals_that_are_digest_shaped"] or "none"))

    hbad = []
    for name, seg in sorted(segs.items()):
        probe = pick("MUT-PAPER-HEAD", seg, seg[:-1] + "Z")
        if canon(probe) not in canon(text):
            hbad.append(name)
    blockmap = block_multiset(text)
    dropped = Counter(dict(list(blockmap.items())[:-1]))
    blockmap = pick("MUT-PAPER-BLOCK", blockmap, dropped)
    want = Counter(canon(s) for s in segs.values())
    # E-22 AS WRITTEN: MULTISET EQUALITY, not containment-with-counts.  A
    # paper carrying a clean copy and a forged twin satisfies containment
    # with the clean one, and an EXTRA forged verdict block satisfies it
    # too; equality of the two multisets kills both (K3 MAJOR-1).
    multiset_ok = (blockmap == want)
    R["paper_coverage"]["fenced_multiset"] = {
        "blocks_in_the_paper": sum(blockmap.values()),
        "distinct_blocks": len(blockmap),
        "derived_segments": len(segs),
        "multiset_matches": multiset_ok}
    LD.gate("G-PAPER-HEAD-VERBATIM",
            "the paper's fenced verdict blocks are compared with the DERIVED "
            "head as a MULTISET and not by containment -- a paper carrying a "
            "clean copy and a forged twin satisfies containment with the "
            "clean one -- and each of the %d derived segments is additionally "
            "matched verbatim into the object under test after the full text "
            "normalisation" % len(segs),
            not hbad and multiset_ok,
            "segments not located verbatim: %s; multiset of %d fenced blocks "
            "matches the %d derived segments: %s"
            % (hbad or "none", sum(blockmap.values()), len(segs), multiset_ok))
    SEAL.take("SEAL-PAPER-COVERAGE", R)

    mutated = pick("MUT-PAPER-POLARITY", False, True)
    pol = paper_polarity(R, text, mutated=mutated)
    R["polarity"] = pol
    LD.gate("G-PAPER-CLAIM-POLARITY",
            "the %d load-bearing sentences carry POLARITY: each is required "
            "present in its positive form and ABSENT in its negation, so an "
            "inverted headline -- the excitation riding the actor, a forced "
            "ceiling, an exclusion that selects at every grain, or a "
            "fermionic-shape theorem -- dies here" % len(pol),
            all(p["ok"] for p in pol),
            "rows failing: %s" % ([p["id"] for p in pol if not p["ok"]]
                                  or "none"))
    SEAL.take("SEAL-POLARITY", R)

    bad = banned_words_found(text)
    bad_words = pick("MUT-PAPER-WALL", bad, bad + ["fermion"])
    R["walls"]["banned_words_found"] = bad_words
    LD.gate("G-NO-PARTICLE-NAMING",
            "THE NO-PARTICLE WALL AS AN INSTRUMENT (paper-22's pattern, "
            "inherited): the object under test is scanned WORD BY WORD "
            "against a declared list of %d banned words, and the shape words "
            "survive only as the compounds the pin licenses -- "
            "fermionic-shape and bosonic-shape.  No particle noun, no spin "
            "and no bare shape adjective occurs anywhere in it"
            % len(BANNED_WORDS),
            not bad_words, "banned words found: %s" % (bad_words or "none"))
    SEAL.take("SEAL-WALLS", R)


# ===========================================================================
# SECTION 18.  COVERAGE, THE SEAL, THE ARTIFACTS
# ===========================================================================

TERMINAL_GATE = "G-ARTIFACT-INTEGRITY"
LATE_GATES = ("G-PAPER-COVERAGE-FINAL", "G-SEAL-COMPLETE",
              "G-ARTIFACT-INTEGRITY")
SWEEP_GATE = "G-MUTANTS-ON-TARGET"
LEDGER_GATES = ("G-COVERAGE", "G-REACHABILITY")
CLOSING_LEDGER_GATES = ("G-SWEEP-BOUND", "G-ANCHOR-CONSUMERS",
                        "G-FALSIFIER-HONESTY", "G-WRITER-SHAPE")


def writer_shape():
    """THE SHAPE OF THE WRITER, measured from this file's own AST BEFORE the
    gate ledger is snapshotted: the terminal integrity gate is the one gate no
    mutant can reach, so its EXISTENCE is sealed here instead."""
    src = read_text(SELF)
    tree = ast.parse(src)
    fn = None
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name == "finish":
            fn = node
    if fn is None:
        return {"finish_found": False}
    names, gate_lines, replaces = [], {}, []
    for n in ast.walk(fn):
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute):
            if n.func.attr == "gate" and n.args and \
                    isinstance(n.args[0], ast.Constant):
                names.append(n.args[0].value)
                gate_lines[n.args[0].value] = n.lineno
            if n.func.attr == "replace":
                replaces.append(n.lineno)
    names.sort(key=lambda g: gate_lines[g])
    terminal_line = gate_lines.get(TERMINAL_GATE)
    return {"finish_found": True, "gate_names_in_finish": names,
            "terminal_gate": TERMINAL_GATE,
            "terminal_gate_present_exactly_once":
                names.count(TERMINAL_GATE) == 1,
            "os_replace_calls": len(replaces),
            "every_replace_after_the_terminal_gate":
                bool(terminal_line) and all(r > terminal_line
                                            for r in replaces)}


def falsifier_hooks():
    """E-23, THE MECHANICAL HALF: every declared falsifier's SYMBOL and VALUE
    are re-derived from this file's own AST -- the innermost statement
    enclosing its hook -- and compared against the declaration."""
    src = read_text(SELF)
    tree = ast.parse(src)
    found = defaultdict(list)
    for node in ast.walk(tree):
        if not isinstance(node, ast.stmt):
            continue
        names = set()
        for c in ast.walk(node):
            if isinstance(c, ast.Call) and isinstance(c.func, ast.Name) \
                    and c.func.id in ("pick", "mut") and c.args \
                    and isinstance(c.args[0], ast.Constant):
                names.add(c.args[0].value)
        if not names:
            continue
        seg = ast.get_source_segment(src, node) or ""
        lo, hi = node.lineno, (node.end_lineno or node.lineno)
        for nm in names:
            found[nm].append((lo, hi, seg))
    out = {}
    for nm, rows in found.items():
        keep = [r for r in rows
                if not any(o is not r and r[0] <= o[0] and o[1] <= r[1]
                           and (o[1] - o[0]) < (r[1] - r[0]) for o in rows)]
        out[nm] = [r[2] for r in sorted(keep)]
    return out


def falsifier_values():
    """E-23, THE VALUE HALF: the value a falsifier moves its symbol TO, read
    off the THIRD ARGUMENT of its own pick() call by unparsing that argument
    from this file's AST -- not by a substring test over the hook's source,
    which a description declaring `to 4` while the code moves to `47`
    survives (K3 MINOR-1)."""
    tree = ast.parse(read_text(SELF))
    out = defaultdict(list)
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) \
                and node.func.id == "pick" and len(node.args) == 3 \
                and isinstance(node.args[0], ast.Constant):
            out[node.args[0].value].append(ast.unparse(node.args[2]))
    return out


def waiver_ledger():
    return {
        "G-PROVENANCE": ("FALSIFIED-BY-A-FLAG",
                         "--break-anchor NAME corrupts any source's expected "
                         "digest and the run dies here; a mutant would be a "
                         "second, weaker copy of the same falsifier"),
        "G-EXACT-ARITHMETIC": ("SELF-SCANNING",
                               "the gate parses this file; a float literal "
                               "introduced anywhere in it fails the gate by "
                               "construction"),
        "G-NO-SUBPROCESS": ("SELF-SCANNING",
                            "the same, over this file's own imports and "
                            "attribute names"),
        "G-READS-DECLARED": ("STRUCTURAL",
                             "the read list is appended by read_bytes, the "
                             "only reader of a SOURCE in this file; the "
                             "second reader, read_text, reads only the two "
                             "files of the declared OBJECT set, which this "
                             "same gate names and binds"),
        "G-QUESTION-ANCHORED": ("SOURCE-FORCED",
                                "its two legs are the pin's own bytes and a "
                                "committed receipt value; corrupting either "
                                "corrupts a pinned source and dies at "
                                "G-PROVENANCE first"),
        "G-ANCHOR-CONSUMERS": ("STRUCTURAL",
                               "the gate compares two registries this file "
                               "owns; a mutant on it would move the "
                               "accounting rather than a measurement"),
        "G-COVERAGE": ("SELF-REFERENTIAL", "the gate IS the coverage ledger"),
        "G-REACHABILITY": ("SELF-REFERENTIAL", "the same"),
        "G-MUTANTS-ON-TARGET": ("SELF-REFERENTIAL",
                                "the gate IS the mutant sweep"),
        "G-PAPER-COVERAGE-FINAL": ("AGGREGATE",
                                   "it closes over gates each of which is "
                                   "separately falsified"),
        "G-ARTIFACT-INTEGRITY": (
            "EXERCISED-IN-RUN-AND-GUARDED-BY-THE-WRITER-SHAPE",
            "a mutant on this gate is UNREACHABLE by construction -- "
            "run_mutant calls finish(write=False), which returns before it -- "
            "so the waiver states the two things that do guard it.  (i) "
            "EXERCISED: the run corrupts a read-back copy of EVERY sealed row "
            "in turn and requires each corruption to be detected before the "
            "real artifacts are compared.  (ii) EXISTENCE: G-WRITER-SHAPE "
            "reads this file's AST BEFORE the gate ledger is snapshotted and "
            "publishes the gate names finish() calls together with the line "
            "of every os.replace, so dropping or renaming this gate, or "
            "lifting a write above it, moves a SEALED published value"),
    }


def finish(LD, SEAL, R, segs, write=True, swept=False):
    gate_names = sorted({g["gate"] for g in LD.rows} | set(LATE_GATES)
                        | set(LEDGER_GATES) | set(CLOSING_LEDGER_GATES)
                        | {SWEEP_GATE})
    targeted = Counter(m[1] for m in MUTANTS)
    waivers = waiver_ledger()
    uncovered = [g for g in gate_names
                 if not targeted.get(g) and g not in waivers]
    registry_drift = sorted(set(gate_names) ^ set(GATE_REGISTRY))
    R["coverage"] = {
        "gates": len(gate_names), "mutants": len(MUTANTS),
        "gates_with_a_mutant": sum(1 for g in gate_names if targeted.get(g)),
        "waived": sorted(waivers), "uncovered": uncovered,
        "late_gates": list(LATE_GATES),
        "declared_registry": len(GATE_REGISTRY),
        "registry_drift": registry_drift,
        "honest_denominator": len(gate_names)}
    R["waiver_ledger"] = [{"gate": g, "class": w[0], "reason": w[1]}
                          for g, w in sorted(waivers.items())]
    LD.gate("G-COVERAGE",
            "#34 WITH AN HONEST DENOMINATOR: of the %d gates this delivery "
            "run evaluates, %d are falsified by at least one declared mutant "
            "and %d are WAIVED with a forcing that says why they cannot fail. "
            "The denominator is THIS run's gate count, and the registry "
            "--list-gates prints is required to be exactly that set"
            % (len(gate_names),
               sum(1 for g in gate_names if targeted.get(g)), len(waivers)),
            not uncovered and not registry_drift,
            "uncovered gates: %s; declared registry %d vs evaluated %d, drift "
            "%s" % (uncovered or "none", len(GATE_REGISTRY), len(gate_names),
                    registry_drift or "none"))
    SEAL.take("SEAL-COVERAGE", R)
    SEAL.take("SEAL-WAIVERS", R)

    hooks = falsifier_hooks()
    values = falsifier_values()
    hook_rows, desc_bad, hook_bad, value_bad = [], [], [], []
    for name, gate, why, moves, to in MUTANTS:
        declared = (moves, to)
        if mut("MUT-FALSIFIER-DESC") and name == "MUT-MEMO":
            declared = ("FORGED", "FORGED")
        segs_here = hooks.get(name, [])
        code_ok = any(declared[0] in s and declared[1] in s
                      for s in segs_here)
        # THE VALUE LEG, ON THE UNPARSED THIRD ARGUMENT rather than on a
        # substring of the hook (K3 MINOR-1): the declared value must occur
        # as a WHOLE TOKEN of the expression the pick() actually moves to.
        argv_here = values.get(name, [])
        value_ok = (not argv_here) or any(
            re.search(r"(?<![\w.])%s(?![\w.])" % re.escape(str(declared[1])),
                      expr) for expr in argv_here)
        # THE PROSE LEG, ON WORD BOUNDARIES rather than as a substring
        prose_ok = bool(re.search(r"(?<![\w-])%s(?![\w])"
                                  % re.escape(str(moves)), why)) and \
            bool(re.search(r"(?<![\w-])%s(?![\w])" % re.escape(str(to)), why))
        hook_rows.append({"mutant": name, "gate": gate, "what_it_does": why,
                          "moves": declared[0], "to": declared[1],
                          "hook_sites": len(segs_here),
                          "pick_argument_expressions": argv_here,
                          "matches_its_code": code_ok,
                          "declared_value_is_the_picks_own_argument":
                              value_ok,
                          "named_in_its_description": prose_ok})
        if not code_ok:
            hook_bad.append(name)
        if not value_ok:
            value_bad.append(name)
        if not prose_ok:
            desc_bad.append(name)
    undeclared_hooks = sorted(set(hooks) - MUTANT_NAMES)
    R["mutants"] = hook_rows
    LD.gate("G-FALSIFIER-HONESTY",
            "E-23: A FALSIFIER'S PUBLISHED DESCRIPTION IS PART OF THE SEALED "
            "SURFACE.  Each of the %d declared falsifiers names THE SYMBOL IT "
            "MOVES and THE VALUE IT MOVES IT TO; both are re-derived from "
            "THIS FILE's own AST -- the innermost statement enclosing its "
            "hook -- and compared against the declaration.  THE VALUE LEG "
            "READS THE PICK'S OWN THIRD ARGUMENT, unparsed from the AST and "
            "matched as a whole token (%d such arguments located), so a "
            "falsifier declaring that it moves a symbol `to 4` while its code "
            "moves it to `47` dies here; and the published prose is required "
            "to name both, ON WORD BOUNDARIES.  %d hook sites are located, "
            "and every hook in the file names a declared falsifier"
            % (len(MUTANTS), sum(len(v) for v in values.values()),
               sum(len(v) for v in hooks.values())),
            not hook_bad and not desc_bad and not value_bad
            and not undeclared_hooks,
            "declarations not matching their code: %s; declared values that "
            "are not the pick's own argument: %s; descriptions not naming "
            "their symbol and value: %s; hooks naming an undeclared "
            "falsifier: %s" % (hook_bad or "none", value_bad or "none",
                               desc_bad or "none", undeclared_hooks or "none"))
    SEAL.take("SEAL-MUTANTS", R)

    ws = writer_shape()
    if mut("MUT-WRITER-SHAPE"):
        ws = dict(ws)
        ws["gate_names_in_finish"] = ws["gate_names_in_finish"][:-1]
    ws["terminal_gate_present_exactly_once"] = (
        ws["gate_names_in_finish"].count(TERMINAL_GATE) == 1)
    R["writer_shape"] = ws
    LD.gate("G-WRITER-SHAPE",
            "THE SHAPE OF THE WRITER IS SEALED, AND SEALED BEFORE THE GATE "
            "LEDGER IS SNAPSHOTTED, which is what makes it the one guard a "
            "post-snapshot gate's own removal cannot evade: finish() calls %d "
            "gates in source order, the terminal integrity gate appears "
            "exactly once among them, there are %d os.replace calls and every "
            "one sits BELOW that gate's own line"
            % (len(ws["gate_names_in_finish"]), ws["os_replace_calls"]),
            (ws["finish_found"] and ws["terminal_gate_present_exactly_once"]
             and ws["os_replace_calls"] == 2
             and ws["every_replace_after_the_terminal_gate"]),
            "gates called in finish %s; terminal gate exactly once %s; "
            "os.replace calls %d, all after it %s"
            % (ws["gate_names_in_finish"],
               ws["terminal_gate_present_exactly_once"],
               ws["os_replace_calls"],
               ws["every_replace_after_the_terminal_gate"]))
    SEAL.take("SEAL-WRITER-SHAPE", R)

    swept = pick("MUT-SWEEP-UNBOUND", swept, True)
    R.setdefault("mutant_sweep", [])
    sweep_rows = R.get("mutant_sweep") or []
    ran_here = {g["gate"] for g in LD.rows}
    sweep_ok = (not swept) or (
        len(sweep_rows) == len(MUTANTS)
        and all(k.get("on_target") for k in sweep_rows)
        and SWEEP_GATE in ran_here)
    LD.gate("G-SWEEP-BOUND",
            "THE SWEEP'S EXECUTION IS BOUND, NOT DECLARED: a delivery-level "
            "run must carry one sweep row per declared mutant (%d), every row "
            "ON TARGET, and must have evaluated the sweep gate itself.  This "
            "run is %s" % (len(MUTANTS),
                           "delivery-level" if swept else "a sub-pipeline"),
            sweep_ok, "sweep rows %d of %d; sweep gate evaluated %s"
            % (len(sweep_rows), len(MUTANTS), SWEEP_GATE in ran_here))
    SEAL.take("SEAL-MUTANT-SWEEP", R)

    consumers = {v[3] for v in VERBATIM} | {p[4] for p in PATH_VALUES}
    bad_consumers = sorted(c for c in consumers
                           if c not in GATE_REGISTRY or c not in ran_here)
    LD.gate("G-ANCHOR-CONSUMERS",
            "#62's consumer binding, with no phantom consumers: every "
            "verbatim anchor and every path-value anchor names a gate, and "
            "each named gate is required to be in the DECLARED registry AND "
            "in THIS RUN's own evaluated ledger -- %d distinct consumer gates"
            % len(consumers),
            not bad_consumers, "consumers not registered-and-evaluated: %s"
            % (bad_consumers or "none"))

    reach = []
    for name, gate, _why, _mv, _to in MUTANTS:
        reach.append({"mutant": name, "gate": gate,
                      "gate_registered": gate in GATE_REGISTRY,
                      "gate_evaluated_or_declared_later":
                          gate in ran_here or gate in LATE_GATES
                          or gate in LEDGER_GATES
                          or gate in CLOSING_LEDGER_GATES
                          or gate == SWEEP_GATE})
    dead = [r["mutant"] for r in reach
            if not (r["gate_registered"]
                    and r["gate_evaluated_or_declared_later"])]
    R["reachability"] = {"rows": reach, "dead_falsifiers": dead}
    LD.gate("G-REACHABILITY",
            "#34 WITH REACHABILITY: every declared falsifier is checked to "
            "REACH its gate -- the gate must be registered and must either "
            "have been evaluated in this run or be one of the gates this same "
            "function evaluates after the census, which are NAMED rather than "
            "assumed.  %d falsifiers, %d dead" % (len(reach), len(dead)),
            not dead, "dead falsifiers: %s" % (dead or "none"))
    SEAL.take("SEAL-REACHABILITY", R)

    R["totals"] = {
        "sources": len(SOURCES),
        "verbatim_anchors": len(R["verbatim_anchors"]),
        "path_value_anchors": len(R["path_value_anchors"]),
        "gates_in_the_registry": len(GATE_REGISTRY),
        "gates_evaluated_before_the_snapshot": len(LD.rows) + 1,
        "gates_after_the_snapshot": len(LATE_GATES) - 1,
        "mutants": len(MUTANTS), "seals": len(SEALED_PATHS),
        "coins": R["counts"]["coins"],
        "declarations": R["counts"]["declarations"],
        "arms": R["counts"]["arms"],
        "leak_rows": R["counts"]["leak_rows"],
        "declared_unsealed": len(DECLARED_UNSEALED),
        "waivers": len(R["waiver_ledger"])}
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
    names_now = ({g["gate"] for g in LD.rows} | {"G-PAPER-COVERAGE-FINAL"}
                 | set(LATE_GATES[1:]))
    names_ok = (not swept) or names_now == set(GATE_REGISTRY)
    LD.gate("G-PAPER-COVERAGE-FINAL",
            "the payload closes.  THE THREE GATE CARDINALITIES ARE NAMED "
            "RATHER THAN CONFLATED: %d gates in the DECLARED REGISTRY, %d "
            "evaluated and carried into the SEALED SNAPSHOT (this gate "
            "included), and %d evaluated AFTER it -- G-SEAL-COMPLETE, which "
            "cannot be inside the object it seals, and G-ARTIFACT-INTEGRITY, "
            "which runs after the bytes are on disk and whose existence is "
            "sealed by G-WRITER-SHAPE.  A RECURSIVE TYPE SCAN of the receipt "
            "finds no float anywhere"
            % (len(GATE_REGISTRY), len(LD.rows) + 1, len(LATE_GATES) - 1),
            all(g["passed"] for g in LD.rows) and not bad_types and names_ok,
            "registry %d, snapshot %d, post-snapshot %d, snapshot names equal "
            "the registry %s (%s), float-valued receipt paths %s"
            % (len(GATE_REGISTRY), len(LD.rows) + 1, len(LATE_GATES) - 1,
               names_ok, "delivery-level" if swept else "sub-pipeline",
               bad_types or "none"))
    R["gates"] = [dict(g) for g in LD.rows]
    R["closing_gates"] = {
        "names": list(LATE_GATES[1:]),
        "gates_in_the_registry": len(GATE_REGISTRY),
        "gates_in_the_sealed_snapshot": len(R["gates"]),
        "gates_after_the_snapshot": len(LATE_GATES) - 1,
        "warrant": "these two are evaluated after the gate ledger is "
                   "snapshotted and sealed -- G-SEAL-COMPLETE cannot be "
                   "inside the object it seals, and G-ARTIFACT-INTEGRITY runs "
                   "after the bytes are on disk.  That gate's existence is "
                   "witnessed by G-WRITER-SHAPE, which reads this file's AST "
                   "before the snapshot and seals the gate names finish() "
                   "calls together with the line of every write."}
    R["transcript_head"] = LINES[:40]
    SEAL.take("SEAL-GATES", R)
    SEAL.take("SEAL-CLOSING", R)
    SEAL.take("SEAL-TOTALS", R)
    SEAL.take("SEAL-TRANSCRIPT", R)
    if mut("MUT-SEAL-BROKEN"):
        R["counts"]["outcome_word"] = "BROKEN"
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
                          "declared_unsealed_forcings":
                              [{"key": k, "forcing": UNSEALED_FORCING[k]}
                               for k in DECLARED_UNSEALED],
                          "declared_unsealed_are_chained_on_read_back": True,
                          "declared_seals": [s for s, _p, _g in SEALED_PATHS]}
    broken = SEAL.verify(R)
    LD.gate("G-SEAL-COMPLETE",
            "THE TOTAL SEAL: every published receipt key is either sealed at "
            "the gate that certified it or listed as DECLARED-UNSEALED with a "
            "forcing, and this gate compares the manifest against the "
            "DECLARED seal set rather than against the seals that happened to "
            "be taken.  The vouching layer is inside the seal: schema, "
            "provenance, paper claims, tables, polarity, coverage, "
            "reachability, gates, totals and the transcript head",
            not missing and not extra and not uncovered_keys and not broken
            and unsealed_frozen and unsealed_clean,
            "declared seals %d, taken %d, missing %s, extra %s, receipt keys "
            "not covered %s, seals broken at close %s, unsealed list frozen "
            "%s and measurement-free %s"
            % (len(SEALED_PATHS), len(SEAL.rows), missing or "none",
               extra or "none", uncovered_keys or "none", broken or "none",
               unsealed_frozen, unsealed_clean))
    payload = json.dumps(R, indent=1, sort_keys=True, default=str)
    emit_report(R, LD)
    text = "\n".join(LINES) + "\n"
    SEAL.close(R, payload, text)
    R["payload_sha256_12"] = SEAL.payload_sha
    if not write:
        return payload, text
    tmp_j, tmp_t = OUT_JSON + ".tmp", OUT_TXT + ".tmp"
    final = json.dumps(R, indent=1, sort_keys=True, default=str)
    try:
        with open(tmp_j, "w", encoding="utf-8") as fh:
            fh.write(final + "\n")
        with open(tmp_t, "w", encoding="utf-8") as fh:
            fh.write(text)
        back = json.loads(read_text(tmp_j))
        probes_caught = 0
        for row in SEAL.rows:
            probe = json.loads(json.dumps(back))
            cur = probe
            parts = row["path"].split("/")
            for part in parts[:-1]:
                cur = cur[int(part)] if isinstance(cur, list) else cur[part]
            key = parts[-1]
            if isinstance(cur, list):
                cur[int(key)] = ["PROBE"]
            else:
                cur[key] = "PROBE"
            if row["seal"] in SEAL.verify(probe, only={row["seal"]}):
                probes_caught += 1
        probe_caught = probes_caught == len(SEAL.rows)
        disk_broken = SEAL.verify(back)
        back_text = read_text(tmp_t)
        head_ok = (back_text.split("\n")[:40] == R["transcript_head"])
        text_ok = digest(back_text) == SEAL.text_sha
        text_lines = len(back_text.split("\n"))
        chained_ok = (back.get("payload_sha256_12") == SEAL.payload_sha
                      and back.get("seal_manifest", {}).get("rows") == SEAL.rows)
        ran = {g["gate"] for g in LD.rows}
        late_ok = all(g in ran for g in tuple(LEDGER_GATES) + LATE_GATES[:2]
                      + CLOSING_LEDGER_GATES + (SWEEP_GATE,))
        sweep_complete = (len(R.get("mutant_sweep") or []) == len(MUTANTS)
                          and all(k.get("on_target")
                                  for k in R.get("mutant_sweep") or []))
        LD.gate("G-ARTIFACT-INTEGRITY",
                "INTEGRITY IS DISK-VS-SEAL, never a re-derivation: the payload is "
                "written from the SEALED object to a staged file, read back FROM "
                "DISK, and every sealed object compared against the digest taken "
                "at the moment its gate passed -- with every one of the %d sealed "
                "rows corrupted in turn on a read-back copy and shown to be "
                "detected first.  The transcript is compared IN FULL, %d of %d "
                "lines by digest, and the two DECLARED-UNSEALED keys are CHAINED "
                "here against the live seal object.  The staged bytes are moved "
                "into place by os.replace ONLY after this gate passes, so a run "
                "that fails any gate leaves the delivered artifacts untouched"
                % (len(SEAL.rows), text_lines, SEAL.text_lines),
                probe_caught and not disk_broken and head_ok and text_ok
                and chained_ok and late_ok and sweep_complete,
                "corrupted probes detected %d of %d, sealed objects broken on "
                "disk %s, transcript head matches %s, transcript matches in full "
                "%s (%d of %d lines), declared-unsealed keys chained %s, every "
                "declared-later gate evaluated %s, sweep complete and on target %s"
                % (probes_caught, len(SEAL.rows), disk_broken or "none", head_ok,
                   text_ok, text_lines, SEAL.text_lines, chained_ok, late_ok,
                   sweep_complete))
    except GateFail:
        # A FAILING RUN LEAVES NOTHING ON DISK -- STAGED OR PROMOTED (K3
        # MINOR-2).  The staged files are removed before the failure
        # propagates, so "writes nothing" is true of the file system and not
        # only of the two delivered artifacts.
        for _tmp in (tmp_j, tmp_t):
            if os.path.exists(_tmp):
                os.remove(_tmp)
        raise
    os.replace(tmp_j, OUT_JSON)
    os.replace(tmp_t, OUT_TXT)
    return payload, text


def emit_report(R, LD):
    say("")
    say("-" * 78)
    say("TOTALS: %d sources, %d verbatim anchors, %d path-value anchors, %d "
        "gates in the registry (%d in the sealed snapshot, %d after it), %d "
        "mutants, %d seals, %d coin classes, %d declarations, %d leak rows, "
        "%d arms"
        % (R["totals"]["sources"], R["totals"]["verbatim_anchors"],
           R["totals"]["path_value_anchors"],
           R["totals"]["gates_in_the_registry"],
           R["totals"]["gates_evaluated_before_the_snapshot"],
           R["totals"]["gates_after_the_snapshot"], R["totals"]["mutants"],
           R["totals"]["seals"], R["totals"]["coins"],
           R["totals"]["declarations"], R["totals"]["leak_rows"],
           R["totals"]["arms"]))
    say("VERDICT: %s" % R["counts"]["outcome_word"])
    # THE HEAD IS EMITTED INTO THE TRANSCRIPT TOO (K3 MINOR-3): the paper
    # says the head is quoted exactly as the instrument emits it, and the
    # transcript is the artifact a reader opens.
    for name in sorted(R["verdict"]):
        say(R["verdict"][name])
    say("-" * 78)


# ===========================================================================
# SECTION 19.  THE CLI (#82)
# ===========================================================================


def selftest():
    """the REAL self-test: corrupt one anchor's expected digest in memory,
    confirm the run dies at the anchor gate, and WRITE NOTHING."""
    global QUIET
    before = (os.path.exists(OUT_JSON) and os.stat(OUT_JSON).st_mtime,
              os.path.exists(OUT_TXT) and os.stat(OUT_TXT).st_mtime)
    QUIET = True
    died = None
    try:
        full_run(break_anchor="A-COUPREC", paper_text=None, do_paper=False)
    except GateFail as e:
        died = str(e).split(" ::")[0]
    except Exception as e:                             # pragma: no cover
        died = "UNEXPECTED:%s" % e
    QUIET = False
    after = (os.path.exists(OUT_JSON) and os.stat(OUT_JSON).st_mtime,
             os.path.exists(OUT_TXT) and os.stat(OUT_TXT).st_mtime)
    wrote = before != after
    print("[SELFTEST] corrupted anchor A-COUPREC -> died at %s" % died)
    print("[SELFTEST] G-SELFTEST-WRITES-NOTHING: artifacts untouched: %s"
          % (not wrote))
    return (died == "G-PROVENANCE") and not wrote


class _Sink:
    def write(self, *_a):
        return 0

    def flush(self):
        return None


def run_mutant(name, paper_text):
    global MUT, QUIET, LINES
    MUT, QUIET = name, True
    keep, keep_out = LINES, sys.stdout
    sys.stdout = _Sink()
    LINES = []
    killed_at = None
    try:
        LD, SEAL, R, segs, _C = full_run(paper_text=paper_text)
        cli_gates(LD)
        finish(LD, SEAL, R, segs, write=False)
    except GateFail as e:
        killed_at = str(e).split(" ::")[0]
    except Exception as e:                             # pragma: no cover
        killed_at = "UNEXPECTED:%s" % type(e).__name__
    MUT, QUIET, LINES = None, False, keep
    sys.stdout = keep_out
    return killed_at


FLAGS = ("--no-write", "--numbers", "--selftest", "--mutant",
         "--break-anchor", "--verify-paper", "--list-gates", "--list-mutants")


def parse_args(argv):
    out = {"mode": "deliver", "mutant": None, "anchor": None, "paper": None}
    i = 0
    while i < len(argv):
        a = argv[i]
        if a not in FLAGS:
            raise CliError("unknown argument %r" % a)
        if out["mode"] != "deliver":
            raise CliError("a second mode flag %r; modes do not compose" % a)
        if a == "--no-write":
            out["mode"] = "no-write"
        elif a == "--numbers":
            out["mode"] = "numbers"
        elif a == "--selftest":
            out["mode"] = "selftest"
        elif a == "--list-gates":
            out["mode"] = "list-gates"
        elif a == "--list-mutants":
            out["mode"] = "list-mutants"
        elif a == "--mutant":
            if i + 1 >= len(argv):
                raise CliError("--mutant needs a NAME")
            if argv[i + 1] not in MUTANT_NAMES:
                raise CliError("unknown mutant %r" % argv[i + 1])
            out["mode"], out["mutant"] = "mutant", argv[i + 1]
            i += 1
        elif a == "--break-anchor":
            if i + 1 >= len(argv):
                raise CliError("--break-anchor needs a NAME")
            if argv[i + 1] not in SOURCE_IDS:
                raise CliError("unknown anchor %r" % argv[i + 1])
            out["mode"], out["anchor"] = "break-anchor", argv[i + 1]
            i += 1
        elif a == "--verify-paper":
            out["mode"] = "verify-paper"
            if i + 1 < len(argv) and not argv[i + 1].startswith("--"):
                out["paper"] = argv[i + 1]
                i += 1
        i += 1
    return out


def parse_args_permissive(argv):
    """the REGISTERED PERMISSIVE SHAPE -- present only as the CLI gate's own
    falsifier.  It accepts anything, which is what #82 forbids."""
    out = {"mode": "deliver", "mutant": None, "anchor": None, "paper": None}
    for a in argv:
        if a.startswith("--"):
            out["mode"] = a[2:]
    return out


def cli_selftest():
    bad = []
    malformed = (["--nope"], ["--mutant"], ["--mutant", "NOPE"],
                 ["--break-anchor"], ["--break-anchor", "NOPE"], ["x"],
                 ["--numbers", "--zzz"],
                 ["--verify-paper", "--mutant", sorted(MUTANT_NAMES)[0]],
                 ["--numbers", "--no-write"], ["--selftest", "--list-gates"])
    for argv in malformed:
        try:
            parse_args(argv)
            bad.append(argv)
        except CliError:
            pass
    ok_shapes = 0
    for argv in ([], ["--no-write"], ["--numbers"], ["--selftest"],
                 ["--mutant", sorted(MUTANT_NAMES)[0]],
                 ["--break-anchor", SOURCE_IDS[0]], ["--verify-paper"],
                 ["--list-gates"], ["--list-mutants"]):
        parse_args(argv)
        ok_shapes += 1
    permissive = parse_args_permissive(["--nope"])["mode"] == "nope"
    return bad, ok_shapes, permissive, len(malformed)


def selftest_shape():
    tree = ast.parse(read_text(SELF))
    inside_finish = 0
    for fn in tree.body:
        if isinstance(fn, ast.FunctionDef) and fn.name == "finish":
            inside_finish = sum(1 for n in ast.walk(fn)
                                if isinstance(n, ast.Call)
                                and isinstance(n.func, ast.Name)
                                and n.func.id == "open"
                                and len(n.args) > 1)
    return inside_finish == 2


def cli_gates(LD):
    bad, ok_shapes, permissive, nmal = cli_selftest()
    bad = pick("MUT-CLI-PERMISSIVE", bad, [["--nope"]])
    LD.gate("G-CLI-WHITELIST",
            "the #82 CLI contract, exercised in this run: %d malformed "
            "argument vectors are all rejected with exit code 2 -- the last "
            "three of them SECOND-MODE vectors, since a mode flag silently "
            "overwriting an earlier one would make the earlier flag a no-op "
            "-- %d legal shapes parse, and the registered PERMISSIVE shape, "
            "present in this file only as this gate's own falsifier, accepts "
            "an unknown flag" % (nmal, ok_shapes),
            not bad and permissive,
            "malformed vectors accepted %s, legal shapes %d, permissive shape "
            "accepts unknown flags %s" % (bad or "none", ok_shapes, permissive))
    st_ok = pick("MUT-SELFTEST-WRITES", selftest_shape(), False)
    LD.gate("G-SELFTEST-WRITES-NOTHING",
            "the --selftest path corrupts an anchor in memory, dies at "
            "G-PROVENANCE and reaches no writer: the writer is called from "
            "exactly one place in this file and the self-test path does not "
            "reach it -- and the predicate is the AST probe's own value",
            st_ok, "the writer-shape probe reports the self-test path clean: "
            "%s" % st_ok)


def main(argv=None):
    global MUT
    argv = list(sys.argv[1:] if argv is None else argv)
    try:
        opt = parse_args(argv)
    except CliError as e:
        sys.stderr.write("usage error: %s\n" % e)
        return 2
    if opt["mode"] == "list-gates":
        for g in GATE_REGISTRY:
            print(g)
        return 0
    if opt["mode"] == "list-mutants":
        for m in MUTANTS:
            print("%-28s -> %s" % (m[0], m[1]))
        return 0
    if opt["mode"] == "selftest":
        return 1 if selftest() else 2
    paper_path = os.path.join(REPO, PAPER_REL)
    if opt["mode"] == "verify-paper":
        if opt["paper"]:
            paper_path = opt["paper"]
        if not os.path.isfile(paper_path):
            sys.stderr.write("usage error: no such paper %r\n" % paper_path)
            return 2
    paper_text = read_text(paper_path) if os.path.isfile(paper_path) else None
    if opt["mode"] == "mutant":
        name = opt["mutant"]
        gate = [m[1] for m in MUTANTS if m[0] == name][0]
        got = run_mutant(name, paper_text)
        print("[MUTANT] %s -> declared gate %s -> died at %s"
              % (name, gate, got))
        return 1 if got == gate else 0
    try:
        LD, SEAL, R, segs, _C = full_run(
            break_anchor=opt["anchor"], paper_text=paper_text,
            do_paper=opt["mode"] != "numbers")
        if opt["mode"] == "numbers":
            print("\n[NUMBERS] census complete; %d gates evaluated"
                  % len(LD.rows))
            return 0
        cli_gates(LD)
        if opt["mode"] == "verify-paper":
            print("\n[VERIFY-PAPER] %s -- %d gates, all passed"
                  % (paper_path, len(LD.rows)))
            return 0
        kills, misses = [], []
        for name, gate, _why, _mv, _to in MUTANTS:
            got = run_mutant(name, paper_text)
            kills.append({"mutant": name, "declared_gate": gate,
                          "died_at": got, "on_target": got == gate})
            if got != gate:
                misses.append("%s died at %s, declared %s"
                              % (name, got, gate))
        R["mutant_sweep"] = kills
        LD.gate("G-MUTANTS-ON-TARGET",
                "all %d declared mutants are run IN PROCESS and each dies at "
                "the gate it names, with the artifacts untouched" % len(kills),
                not misses, "on target %d of %d; misses %s"
                % (sum(1 for k in kills if k["on_target"]), len(kills),
                   misses or "none"))
        finish(LD, SEAL, R, segs, write=(opt["mode"] == "deliver"),
               swept=True)
        return 0
    except GateFail as e:
        sys.stderr.write("GATE FAILED: %s\n" % e)
        return 1


if __name__ == "__main__":
    sys.exit(main())






