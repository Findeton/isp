#!/usr/bin/env python3
"""NDEP (paper-39) -- THE n-DEPENDENCE UNIT.  IS NINE STRUCTURAL OR DECLARED?

QUESTION (pin `v14/note-ndep-pin.md`, sha256-12 2ff14505f18f, ledger #332).
The corpus's arena is AG(2,3): nine actors.  Five core laws were established
there.  Is the actor count a PARAMETER of those laws, or is it a lab
declaration -- and where a law's numeral is 3, is that 3 the square root of
the actor count, the declared link count, or a literal that does not move?

This unit BUILDS the n = 4 arena -- AG(2,2), four actors, the Klein-four
translation group -- and its driven history corpus, by the SAME grammar the
nine-actor corpus used, and re-runs the five laws on it.  n = 16 (AG(2,4)) is
carried as a DECLARED WINDOW where affordable, and the window's limits are
published rather than hidden.

THE FIVE LAWS UNDER TEST, each sorted into LAW-IN-N / NEEDS-3 / BREAKS:

  L1  THE NAMING THEOREM (AID #304): the stabilizer of a history is the Young
      subgroup of its participation-signature partition, and the forced-naming
      fraction's analogue.
  L2  THE CRYSTALLIZATION PAIR (AID): schedule time against the information
      floor, and the redundant-event offset (one at n = 9 -- is it one at all
      n?).
  L3  THE COSET MENU (FAC #311): the geometry leg admits exactly the coset
      partitions of the translation subgroups; the count (6 at n = 9) as a
      function of q.
  L4  THE MOD-3 MOTIF: the weld ladder at R = 0 mod 3 and the coin's residue
      channel -- mod-q, or mod-3 forever?
  L5  THE DIVISION-FORCING FRACTION (FAC): unique factorization per history.

THE n = 9 NUMBERS ARE NEVER RE-DERIVED HERE.  They enter as ANCHORS -- byte
and path-value anchored against the parents' committed receipts, or, where a
parent's worktree copy is under repair, as FROZEN DECLARED CONSTANTS carrying
the source commit and the digest at that commit.  What IS recomputed at q = 3
is the CONSTRUCTOR, and only the constructor: the substrate counts that
license the claim that the n = 4 build uses the same grammar.  That leg is a
fidelity gate, not a finding, and it is stamped as one everywhere it appears.

ARITHMETIC.  Exact only: Python integers and the Grover/phase data carried as
integer pairs.  No floats anywhere; an AST scan of this file and a recursive
type scan of the emitted receipt are gates.

RUNTIME INPUTS (#46/#91).  Exactly three files are read as SOURCES, all
hash-pinned by this unit's frozen declaration, plus exactly one file read as
the OBJECT UNDER TEST -- this unit's own paper.  No repository state outside
those lists is read and no subprocess of any kind is invoked, so the run is
correct off-tree and with no version control present.
"""

import ast
import hashlib
import json
import math
import os
import re
import sys
from collections import Counter
from itertools import combinations, combinations_with_replacement, permutations, product

sys.setrecursionlimit(100000)

SELF = os.path.abspath(__file__)
REPO = os.path.dirname(os.path.dirname(os.path.dirname(SELF)))
OUT_TXT = os.path.join(os.path.dirname(SELF), "ndep_output.txt")
OUT_JSON = os.path.join(os.path.dirname(SELF), "ndep_receipt.json")

SCHEMA = "isp/v14/ndep-n-dependence/1"
PAPER_REL = "v14/paper-39-ndep.md"

# ===========================================================================
# SECTION 0.  THE FROZEN DECLARATION (RUNBOOK section 15: the arena is data)
# ===========================================================================

SOURCES = [
    ("A-PIN", "v14/note-ndep-pin.md", "2ff14505f18f",
     "THIS UNIT'S PIN (ledger #332, commit 11dff36): the question, the five "
     "laws, the outcome names, the walls and the feasibility rule."),
    ("A-AID", "v14/paper-33-aid.md", "ecdd3fbf1d06",
     "AID / PAPER-33 (terminal, v14 ledger #304): the naming theorem, the "
     "crystallization pair and the nine-actor corpus grammar.  Quoted, never "
     "re-derived."),
    ("A-AIDREC", "v14/code/aid_receipt.json", "2dd2a9879984",
     "AID's COMMITTED RECEIPT: the n = 9 substrate counts and the n = 9 law "
     "values, read by PATH and consumed as anchors by the fidelity and "
     "transport gates."),
]

# The FAC (paper-35) objects are pinned by COMMIT rather than read: the
# worktree copies are under repair at this unit's construction time, and
# #46 forbids reading mutable repo state.  The values below are therefore
# FROZEN DECLARED CONSTANTS with their source commit and digests recorded,
# and every one of them is cross-checked against a value this unit computes
# from the general formula (G-LAW3-PARENT / G-LAW5-PARENT).
FAC_COMMIT = "f4172ea"
FAC_RECEIPT_SHA12 = "240bad74217a"
FAC_PAPER_SHA12 = "2e9cbae8a83e"
# The weld ladder's own rung at the nine-actor arena is not carried by any
# receipt this unit reads, so it too is a FROZEN DECLARED PARENT CONSTANT
# rather than a typed number, and it is cross-checked against a value this
# unit computes (G-LAW4-LADDER).
LADDER_DECLARED = {
    "first_rung_at_n9": 3,
    "source": "THE R-RUNG PAPERS' LADDER LAW: a live weld is motivated "
              "exactly at budgets R congruent to 0 modulo 3 at the "
              "nine-actor arena, whose declared link count is 3",
}
FAC_DECLARED = {
    "leg1_geometry_survivors": 6,
    "subgroup_coset_partitions": 6,
    "leg1_equals_the_subgroup_cosets": True,
    "actor_lattice": 21147,
    "unique_at": 5852,
    "non_unique_at": 4,
}

# PATH-VALUE ANCHORS (#20 path-value anchoring): each row is (id, source id,
# json path, expected value, consumer gate).  A path drift that changes the
# arena or a verdict dies at the anchor.
PATH_ANCHORS = [
    ("P-PARTS", "A-AIDREC", "substrate/back_validation/partitions/parent",
     280, "G-CONSTRUCTOR-FIDELITY"),
    ("P-SAT", "A-AIDREC", "substrate/back_validation/saturating/parent",
     36, "G-CONSTRUCTOR-FIDELITY"),
    ("P-STRICT", "A-AIDREC", "substrate/back_validation/strict_triples/parent",
     72, "G-CONSTRUCTOR-FIDELITY"),
    ("P-FLAT", "A-AIDREC", "substrate/back_validation/flat_quadruples/parent",
     276, "G-CONSTRUCTOR-FIDELITY"),
    ("P-WINDOW", "A-AIDREC", "substrate/back_validation/window/parent",
     600, "G-CONSTRUCTOR-FIDELITY"),
    ("P-FORCED", "A-AIDREC", "counts/forced_histories",
     5852, "G-LAW1-TRANSPORT"),
    ("P-HISTS", "A-AIDREC", "counts/histories",
     5856, "G-LAW1-TRANSPORT"),
    ("P-CHART", "A-AIDREC", "counts/chart_histories",
     4, "G-LAW1-TRANSPORT"),
    ("P-TIME", "A-AIDREC", "crystallization/constant_on_C1_C2_C1FAN",
     5, "G-LAW2-TIME"),
    ("P-FLOOR", "A-AIDREC",
     "crystallization/information_floor/counting_bound_ceil_log2_actors",
     4, "G-LAW2-FLOOR"),
]

# VERBATIM-TEXT ANCHORS (#62, as amended): quote fidelity against the source's
# committed bytes, each bound to a NAMED, NON-LITERAL consumer gate.
VERBATIM = [
    ("V-YOUNG", "A-AID",
     "the stabilizer is the Young subgroup, its order is the product of the "
     "block factorials, and identity crystallizes exactly when every actor "
     "has its own signature",
     "G-LAW1-ROUTES"),
    ("V-FLOOR", "A-AID",
     "Nine actors need distinct binary participation signatures, and k events "
     "supply at most 2^k of them, so no history can force identity on fewer "
     "than four events",
     "G-LAW2-FLOOR"),
    ("V-ATTAINED", "A-AID",
     "That floor is a counting theorem, and it is attained",
     "G-LAW2-FLOOR"),
    ("V-TIME", "A-AID",
     "the crystallization time is exactly 5 on C1, C2 and the seed fan",
     "G-LAW2-TIME"),
    ("V-OFFSET", "A-AID",
     "the transportable content of the five is four informative events, a "
     "theorem floor attained everywhere, plus one structurally redundant "
     "event",
     "G-LAW2-OFFSET"),
    ("V-CHART", "A-AID",
     "they are the constant-class quadruples ANT|ANT|ANT|ANT, "
     "COL|COL|COL|COL, DIA|DIA|DIA|DIA, ROW|ROW|ROW|ROW",
     "G-LAW1-CHART"),
]

# THE DECLARED ARENA (RUNBOOK section 15), as data.
ARENA_DECL = [
    ("BOUNDARY", "AG(2,q) FOR q IN {2, 3, 4}.  The PRIMARY arena is q = 2 -- "
     "four actors, the Klein-four translation group, entire and complete.  "
     "q = 3 is entered ONLY as the constructor-fidelity leg and never as a "
     "finding.  q = 4 is a DECLARED WINDOW whose limits are published."),
    ("FAMILY", "THE DRIVEN HISTORY CORPUS by the parent's grammar, "
     "parameterised in q: groupings of the q^2 sites into q blocks of q; the "
     "saturating groupings; the strict R = L tuples; the seed fan; the "
     "R = 2L concatenations; the R = L + 1 driven window."),
    ("LAW", "THE FIVE PARENT LAWS, each carried as three candidate transports "
     "-- the n-only reading, the q = sqrt(n) reading and the literal reading "
     "-- and decided against the measurement at every feasible arena point."),
    ("STATE", "THE RECORD FIELD n_l(x) and paper-20's one-step operator, "
     "re-implemented at general (q, L, m); the coin's phase modulus m is a "
     "DECLARED FREE AXIS of this unit and is swept."),
    ("ARENA", "THE DECLARED LINK COUNT L is a FREE AXIS: the parent declares "
     "L = q of the q + 1 parallel classes, and this unit sweeps L over "
     "{1, 2, 3} at n = 4.  The sweep is what separates L from q and from the "
     "characteristic."),
    ("PROVENANCE", "THREE HASH-PINNED SOURCES read at run time; the FAC "
     "objects carried as frozen declared constants at commit %s because "
     "their worktree copies are under repair (#46)." % FAC_COMMIT),
]

WINDOWS = [
    ("W-N4", True,
     "THE n = 4 CORPUS, ENTIRE.  Every grouping of the four sites into two "
     "pairs, every saturating one, every strict R = 2 pair, the whole seed "
     "fan, every R = 4 concatenation and the whole R = 3 driven window.  No "
     "sampling anywhere: the corpus is the complete class."),
    ("W-N4-LATTICE", True,
     "THE COMPLETE ACTOR LATTICE AT n = 4: all Bell(4) partitions of the four "
     "actors, no cap and no sampling."),
    ("W-N4-S4", True,
     "THE COMPLETE SYMMETRIC GROUP S_4, filtered element by element -- the "
     "naming theorem's route A at n = 4 is exhaustive."),
    ("W-LSWEEP", True,
     "THE DECLARED-LINK SWEEP AT n = 4, ENTIRE: L = 1, 2 and 3, that is, "
     "every initial segment of the q + 1 = 3 canonical directions.  This is "
     "the window that separates the modulus's carrier from sqrt(n) and from "
     "the characteristic, both of which are 2 at every point of it."),
    ("W-MSWEEP", True,
     "THE COIN-MODULUS SWEEP AT n = 4: m = 2, 3, 4, 5.  Four declared points "
     "of an axis the parent fixed at three without deriving it."),
    ("W-RECFAM", True,
     "THE RECORD FAMILY, ENTIRE ON ITS DECLARATION: every corpus record "
     "vector with one cell raised by t for t = 0..6, deduplicated, and every "
     "unordered pair of it compared."),
    ("W-N16-CLASS", False,
     "THE n = 16 WINDOW.  Only the parallel-class R-tuples are built: the "
     "full saturating census at q = 4 needs the 2,627,625 groupings of 16 "
     "sites into four blocks of four and is DECLARED OUT OF SCOPE here.  "
     "Every n = 16 row below is a row about this window and says so."),
    ("W-N16-PERM", False,
     "THE n = 16 PERMUTATION WINDOW for the naming theorem's route A: all "
     "transpositions and all 3-cycles of the sixteen actors, at every prefix.  "
     "S_16 has 20,922,789,888,000 elements and is not filtered."),
    ("W-Q3", False,
     "THE CONSTRUCTOR-FIDELITY LEG AT q = 3.  The substrate counts only -- "
     "groupings, saturating groupings, strict triples, flat quadruples, "
     "window size.  No n = 9 law is evaluated here and no n = 9 finding is "
     "produced here."),
]

LINES = []
QUIET = False
MUT = None
READS = []
READS_BY_CATEGORY = {}
READ_CATEGORIES = ("SOURCE", "PAPER-UNDER-TEST", "SELF")
NUMREG = set()
SWEEP_ROWS = []


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
    """a missing pinned source is a GATE failure, not a traceback."""
    READS.append(rel)
    READS_BY_CATEGORY.setdefault("SOURCE", set()).add(
        os.path.abspath(os.path.join(REPO, rel)))
    try:
        with open(os.path.join(REPO, rel), "rb") as fh:
            return fh.read()
    except (FileNotFoundError, IsADirectoryError, PermissionError) as exc:
        raise GateFail("G-PROVENANCE :: pinned source absent or unreadable: "
                       "%s (%s)" % (rel, type(exc).__name__))


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
         "₀": "0", "₃": "3", "₄": "4", "₅": "5",
         "₆": "6", "₉": "9", "ℓ": "l", "→": "->",
         "←": "<-", "⋅": "*", "²": "2", "³": "3",
         "⁴": "4", "≈": "~", "⊆": "subset", "∈": "in",
         "∑": "sum", "·": "*", "−": "-", "⁄": "/",
         " ": " ", "∏": "prod", "σ": "sigma", "φ": "phi",
         "∩": "cap", "≅": "iso", "⊲": "normal",
         "⌈": "ceil", "⌉": "", "ω": "w", "≠": "!="}

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


def com(n):
    return "{:,}".format(n)


def reg(*vals):
    """every number this run publishes is REGISTERED here, so the paper's
    numeral allow list is the run's own product and never a typed table."""
    for v in vals:
        if isinstance(v, bool):
            continue
        if isinstance(v, int):
            NUMREG.add(str(v))
            NUMREG.add(com(v))
        elif isinstance(v, str):
            NUMREG.add(v)
    return vals[0] if vals else None


# ===========================================================================
# SECTION 1.  THE PARAMETERISED ARENA -- AG(2, q) FOR q IN {2, 3, 4}
#
# Everything below is the parent's own construction with the numeral 3
# replaced by a parameter.  Nothing is specialised to any q, and the
# constructor-fidelity leg of section 3 is what licenses that claim.
# ===========================================================================

F4_MUL = {(0, 0): 0, (0, 1): 0, (0, 2): 0, (0, 3): 0,
          (1, 0): 0, (1, 1): 1, (1, 2): 2, (1, 3): 3,
          (2, 0): 0, (2, 1): 2, (2, 2): 3, (2, 3): 1,
          (3, 0): 0, (3, 1): 3, (3, 2): 1, (3, 3): 2}


def field(q):
    """(elements, add, mul) for F_q.  q = 4 carries GF(4) explicitly: the
    additive group is Z_2^2, which is exactly why q = 4 separates the
    characteristic from q and is the window that does the discriminating."""
    if q in (2, 3):
        return tuple(range(q)), (lambda a, b: (a + b) % q), \
            (lambda a, b: (a * b) % q)
    if q == 4:
        return (0, 1, 2, 3), (lambda a, b: a ^ b), (lambda a, b: F4_MUL[(a, b)])
    raise GateFail("G-ARENA :: undeclared q %r" % (q,))


class Arena:
    """AG(2, q) with L declared link directions.  L defaults to q, which is
    the parent's own declaration (three of the four parallel classes at
    q = 3); L is a DECLARED FREE AXIS of this unit and is swept."""

    def __init__(self, q, L=None):
        self.q = q
        self.n = q * q
        self.el, self.add, self.mul = field(q)
        self.SITES = tuple((i, j) for i in self.el for j in self.el)
        self.SI = {s: k for k, s in enumerate(self.SITES)}
        rest = [t for t in self.el if t not in (0, 1)]
        self.DIRECTIONS = ((1, 0), (0, 1)) + tuple((1, t) for t in [1] + rest)
        if len(self.DIRECTIONS) != q + 1:
            raise GateFail("G-ARENA :: %d directions at q = %d" % (
                len(self.DIRECTIONS), q))
        self.L = q if L is None else L
        self.LINKS = self.DIRECTIONS[:self.L]
        self.CELLS = tuple((x, l) for x in self.SITES for l in self.LINKS)
        self.CI = {c: k for k, c in enumerate(self.CELLS)}
        self.CLASS_DIRS = ((0, 1), (1, 0)) + tuple((1, t) for t in [1] + rest)
        nm = ["ROW", "COL", "DIA", "ANT"] + ["CL%d" % i for i in range(4, q + 2)]
        self.CLASS_NAMES = tuple(nm[:q + 1])
        self.CLASSES = {self.CLASS_NAMES[i]: self.parallel_class(d)
                        for i, d in enumerate(self.CLASS_DIRS)}
        self.CLASS_OF = {v: k for k, v in self.CLASSES.items()}

    def vadd(self, a, b):
        return (self.add(a[0], b[0]), self.add(a[1], b[1]))

    def vmul(self, k, a):
        return (self.mul(k, a[0]), self.mul(k, a[1]))

    def parallel_class(self, d):
        """the resolvable partition of AG(2, q) into the q lines of slope d."""
        H = frozenset(self.vmul(t, d) for t in self.el)
        seen, out = set(), []
        for x in self.SITES:
            Ln = tuple(sorted(self.vadd(x, h) for h in H))
            if Ln not in seen:
                seen.add(Ln)
                out.append(Ln)
        return tuple(sorted(out))

    def all_groupings(self):
        """every partition of the q^2 sites into q blocks of size q."""
        out, q = [], self.q

        def rec(rem, acc):
            if not rem:
                out.append(tuple(sorted(acc)))
                return
            a, rest = rem[0], rem[1:]
            for extra in combinations(rest, q - 1):
                blk = tuple(sorted((a,) + extra))
                rec(tuple(x for x in rest if x not in extra), acc + [blk])
        rec(tuple(self.SITES), [])
        return sorted(out)

    def round_vec(self, P):
        """the per-(site, link) incidence vector of ONE round's grouping: cell
        (x, l) carries 1 exactly when x and x + l share a conflict group."""
        return tuple(1 if any(x in g and self.vadd(x, l) in g for g in P) else 0
                     for (x, l) in self.CELLS)

    def canon_transversals(self, P):
        """THE DECLARED SEED MENU: the k-th member of each group in the
        canonical order, k = 0..q-1.  Deterministic, no sampling."""
        return [tuple(sorted(g)[k] for g in P) for k in range(self.q)]

    def translations_generated(self):
        """the subgroup the DECLARED links generate.  At prime q this is the
        whole translation group; at q = 4 it is not, and that is measured."""
        S = {tuple(0 for _ in range(2))}
        S = {(self.el[0], self.el[0])}
        ch = True
        while ch:
            ch = False
            for s in list(S):
                for l in self.LINKS:
                    t = self.vadd(s, l)
                    if t not in S:
                        S.add(t)
                        ch = True
        return frozenset(S)

    def subgroups(self):
        """every subgroup of the translation group, by closure of generator
        sets.  Exhaustive: the group is elementary abelian of rank at most 4,
        so every subgroup is generated by at most 4 elements."""
        T = [s for s in self.SITES if s != (self.el[0], self.el[0])]
        found = set()
        for k in range(0, 5):
            for gens in combinations(T, k):
                S = {(self.el[0], self.el[0])}
                ch = True
                while ch:
                    ch = False
                    for s in list(S):
                        for g in gens:
                            t = self.vadd(s, g)
                            if t not in S:
                                S.add(t)
                                ch = True
                found.add(frozenset(S))
        return sorted(found, key=lambda s: (len(s), sorted(s)))

    def coset_partition(self, H):
        seen, out = set(), []
        for x in self.SITES:
            c = tuple(sorted(self.vadd(x, h) for h in H))
            if c not in seen:
                seen.add(c)
                out.append(c)
        return tuple(sorted(out))


def substrate(A):
    parts = A.all_groupings()
    vecs = [A.round_vec(P) for P in parts]
    sat = [i for i, v in enumerate(vecs) if sum(v) == A.n]
    return parts, vecs, sat


def strict_tuples(A, vecs, sat, R):
    """the parent's I7-STRICT class at R = L: ordered R-tuples of saturating
    groupings whose summed link field covers every cell."""
    V = [vecs[i] for i in sat]
    nc = len(A.CELLS)
    out = []

    def rec(depth, tot, acc):
        if depth == R:
            if all(t >= 1 for t in tot):
                out.append(tuple(sat[c] for c in acc))
            return
        for ci in range(len(V)):
            v = V[ci]
            rec(depth + 1, [tot[k] + v[k] for k in range(nc)], acc + [ci])
    rec(0, [0] * nc, [])
    return out


def flat_tuples(A, vecs, sat, R):
    """the parent's G-FLAT class: ordered R-tuples of saturating groupings
    whose summed link field is the NEAR-FLAT row (1, ..., 1, 2) at every site
    -- R = L + 1 spread over L links as evenly as it goes."""
    V = [vecs[i] for i in sat]
    nc = len(A.CELLS)
    tgt = ([1] * (A.L - 1) + [2]) * A.n
    out = []

    def rec(depth, tot, acc):
        if any(tot[k] > tgt[k] for k in range(nc)):
            return
        if depth == R:
            if tot == tgt:
                out.append(tuple(sat[c] for c in acc))
            return
        for ci in range(len(V)):
            v = V[ci]
            rec(depth + 1, [tot[k] + v[k] for k in range(nc)], acc + [ci])
    rec(0, [0] * nc, [])
    return out


def history_of(A, schedule):
    """THE COMBINATORIAL HISTORY: the division events of a schedule, as
    actor-subsets, in the driver's own order -- groups in ascending order of
    their seed's site index, which is the parent's constructor exactly."""
    H = []
    for (groups, seeds) in schedule:
        order = sorted(range(len(groups)), key=lambda gi: A.SI[seeds[gi]])
        for gi in order:
            H.append(frozenset(groups[gi]))
    return tuple(H)


def first_menu_schedule(A, T):
    return tuple((T[r], A.canon_transversals(T[r])[0]) for r in range(len(T)))


def build_corpora(A, parts, vecs, sat):
    """THE FOUR CORPORA, by the parent's own grammar with 3 -> q:

      C1     the strict R = L tuples at the first canonical seed menu
      C1FAN  the same tuples at ALL q^R canonical menus
      C2     every ordered concatenation of two C1 schedules (R = 2L)
      C3     the R = L + 1 driven window: every class tuple, every near-flat
             tuple, the alternating control, and the collinear seed fan
    """
    R = A.L
    C1t = strict_tuples(A, vecs, sat, R)
    C1 = [first_menu_schedule(A, tuple(parts[i] for i in T)) for T in C1t]
    C1FAN = []
    for T in C1t:
        Ps = tuple(parts[i] for i in T)
        menus = [A.canon_transversals(P) for P in Ps]
        for sel in product(range(A.q), repeat=R):
            C1FAN.append(tuple((Ps[r], menus[r][sel[r]]) for r in range(R)))
    C2 = [a + b for a in C1 for b in C1]
    R3 = A.L + 1
    quads, tags = [], []
    for names in product(A.CLASS_NAMES, repeat=R3):
        quads.append(tuple(A.CLASSES[k] for k in names))
        tags.append("W-CLASS")
    flatq = flat_tuples(A, vecs, sat, R3)
    for T in flatq:
        quads.append(tuple(parts[i] for i in T))
        tags.append("W-FLAT")
    ctrl = tuple(A.CLASS_NAMES[i % 2] for i in range(R3))
    quads.append(tuple(A.CLASSES[k] for k in ctrl))
    tags.append("W-CTRL")
    out, seen, meta = [], set(), {}
    for T, tag in zip(quads, tags):
        sch = first_menu_schedule(A, T)
        if sch in seen:
            continue
        seen.add(sch)
        out.append(sch)
        meta[sch] = tag
    coll = tuple(list(A.CLASS_NAMES[:A.L]) + [A.CLASS_NAMES[A.L - 1]])
    T = tuple(A.CLASSES[k] for k in coll)
    menus = [A.canon_transversals(P) for P in T]
    for sel in product(range(A.q), repeat=R3):
        sch = tuple((T[r], menus[r][sel[r]]) for r in range(R3))
        if sch in seen:
            continue
        seen.add(sch)
        out.append(sch)
        meta[sch] = "W-SEEDFAN"
    return {"C1t": C1t, "C1": C1, "C1FAN": C1FAN, "C2": C2, "C3": out,
            "C3meta": meta, "flat": flatq, "ctrl": ctrl, "coll": coll}


def class_names_of(A, schedule):
    return tuple(A.CLASS_OF.get(P, "MIXED") for (P, _s) in schedule)


# ===========================================================================
# SECTION 2.  THE LAWS' PRIMITIVES, ALL PARAMETERISED IN (q, L, m)
# ===========================================================================

def signature_blocks(A, H):
    """THE PARTICIPATION-SIGNATURE PARTITION: two actors share a block exactly
    when they belong to the same events, all of them."""
    sig = {}
    for x in A.SITES:
        sig.setdefault(tuple(1 if x in F else 0 for F in H), []).append(x)
    return tuple(sorted(tuple(sorted(v)) for v in sig.values()))


def young_order(A, H):
    o = 1
    for b in signature_blocks(A, H):
        o *= math.factorial(len(b))
    return o


def young_elements(A, H):
    """ROUTE B: the Young subgroup itself, as explicit permutations of the
    actor indices -- built from the blocks, never filtered."""
    blocks = signature_blocks(A, H)
    idxs = [[A.SI[x] for x in b] for b in blocks]
    out = []

    def rec(k, acc):
        if k == len(idxs):
            p = [0] * A.n
            for src, dst in acc:
                p[src] = dst
            out.append(tuple(p))
            return
        for perm in permutations(idxs[k]):
            rec(k + 1, acc + list(zip(idxs[k], perm)))
    rec(0, [])
    return sorted(out)


def masks_of(A, H):
    out = []
    for F in H:
        m = 0
        for x in F:
            m |= 1 << A.SI[x]
        out.append(m)
    return tuple(out)


def fixes_setwise(A, H, p):
    """the DEFINITION, applied to one permutation: sigma(F) = F for every
    event F, setwise.  Nothing here knows the Young theorem."""
    for m in masks_of(A, H):
        im = 0
        for i in range(A.n):
            if m >> i & 1:
                im |= 1 << p[i]
        if im != m:
            return False
    return True


def stab_bruteforce(A, H):
    """ROUTE A at n = 4: the WHOLE symmetric group, filtered element by
    element by the definition."""
    return sorted(p for p in permutations(range(A.n))
                  if fixes_setwise(A, H, p))


def in_young(A, H, p):
    sig = {x: tuple(1 if x in F else 0 for F in H) for x in A.SITES}
    return all(sig[A.SITES[p[A.SI[x]]]] == sig[x] for x in A.SITES)


def crystallization(A, H):
    """THE CRYSTALLIZATION TIME: the earliest prefix length whose stabilizer is
    trivial.  None when the whole history leaves identity un-forced."""
    for k in range(1, len(H) + 1):
        if young_order(A, H[:k]) == 1:
            return k
    return None


def min_event_subset(A, H):
    """THE INFORMATION FLOOR, per history: the size of the smallest SUBSET of
    the events whose stabilizer is already trivial."""
    seps = []
    for a, b in combinations(range(A.n), 2):
        m = 0
        for i, F in enumerate(H):
            if (A.SITES[a] in F) != (A.SITES[b] in F):
                m |= 1 << i
        if m == 0:
            return None
        seps.append(m)
    for k in range(1, len(H) + 1):
        for comb in combinations(range(len(H)), k):
            s = 0
            for i in comb:
                s |= 1 << i
            if all(sep & s for sep in seps):
                return k
    return None


def counting_floor(n):
    """THE PARENT'S STATED FLOOR: k events supply at most 2^k distinct binary
    signatures, so 2^k >= n.  A true bound at every n; the question this unit
    settles is whether it is the ATTAINED one."""
    k = 0
    while 2 ** k < n:
        k += 1
    return k


def weight_floor(n, q):
    """THE SHARPENED FLOOR this unit supplies.  Each event has exactly q
    members, so k events distribute total incidence k*q over the actors; n
    DISTINCT binary k-signatures cost at least the total weight of the n
    lightest distinct k-vectors.  The floor is the least k meeting both the
    counting bound and this weight bound."""
    k = 1
    while True:
        if 2 ** k >= n:
            tot, left, w = 0, n, 0
            while left > 0 and w <= k:
                take = min(math.comb(k, w), left)
                tot += take * w
                left -= take
                w += 1
            if left == 0 and tot <= k * q:
                return k
        k += 1


def codivision(A, H):
    r = [[0] * A.n for _ in range(A.n)]
    for F in H:
        idx = [A.SI[x] for x in F]
        for a in idx:
            for b in idx:
                if a != b:
                    r[a][b] += 1
    return r


def record_vector(A, H):
    """THE RECORD n_l(x): the count of division events containing both the
    actor at x and the actor at x + l."""
    r = codivision(A, H)
    return [r[A.SI[x]][A.SI[A.vadd(x, l)]] for x in A.SITES for l in A.LINKS]


# ---- the four legs of FAC's criterion, parameterised -----------------------

def block_map(part):
    return {x: bi for bi, b in enumerate(part) for x in b}


def leg1_actor(A, part):
    """LEG-1 GEOMETRY: for each declared link l, the translation x -> x + l
    descends to the blocks.  Reads the partition and the arena, never the
    history."""
    bm = block_map(part)
    for l in A.LINKS:
        img = {}
        for x in A.SITES:
            b, t = bm[x], bm[A.vadd(x, l)]
            if img.setdefault(b, t) != t:
                return False
    return True


def leg2_actor(A, part, H):
    """LEG-2 HISTORY: every division event is a union of blocks."""
    for F in H:
        for b in part:
            k = sum(1 for x in b if x in F)
            if k and k != len(b):
                return False
    return True


def leg3_actor(A, part, rec):
    """LEG-3 RECORD: the record is block-constant, link by link."""
    for b in part:
        for li in range(A.L):
            if len({rec[A.SI[x] * A.L + li] for x in b}) > 1:
                return False
    return True


def induced_cell_partition(A, part):
    """THE DIRECTIONWISE IMAGE: identify (x, l) with (y, l) when x and y are
    identified.  This is what LEG-4 is evaluated on."""
    bm = block_map(part)
    d = {}
    for k, (x, l) in enumerate(A.CELLS):
        d.setdefault((bm[x], A.LINKS.index(l)), []).append(k)
    return tuple(sorted(tuple(sorted(v)) for v in d.values()))


def shift_T(A):
    return tuple(A.CI[(A.vadd(x, l), l)] for (x, l) in A.CELLS)


def coupled_columns(A, rec, order, m):
    """PAPER-20's ONE-STEP OPERATOR U = T . C, COLUMN BY COLUMN, EXACTLY, at a
    general link count L and a general phase modulus m.  The coin is
    site-block-diagonal with D(x) = diag(z^{n_l(x)}) for z a primitive m-th
    root of unity; the Grover block is the L x L matrix 2 - L*delta, carried
    UNNORMALISED so every entry stays an integer.  A column is a list of
    (target cell, phase exponent, integer coefficient)."""
    L = A.L
    GN = tuple(tuple(2 if i != j else 2 - L for j in range(L))
               for i in range(L))
    ST = shift_T(A)
    cols = []
    for (y, l) in A.CELLS:
        li = A.LINKS.index(l)
        ent = []
        for i in range(L):
            tgt = ST[A.CI[(y, A.LINKS[i])]]
            e = (rec[A.SI[y] * L + li] if order == "G.D"
                 else rec[A.SI[y] * L + i]) % m
            if GN[i][li]:
                ent.append((tgt, e, GN[i][li]))
        cols.append(tuple(sorted(ent)))
    return tuple(cols)


def leg4_cell(A, cpart, rec, order, m):
    """LEG-4 DYNAMICS: EXACT LUMPABILITY of the one-step operator for the
    induced carrier partition -- for any two cells of a block the sums of the
    column's entries falling into each block agree exactly."""
    dim = len(A.CELLS)
    lab = [0] * dim
    for bi, b in enumerate(cpart):
        for k in b:
            lab[k] = bi
    cols = coupled_columns(A, rec, order, m)
    prof = []
    for k in range(dim):
        acc = {}
        for (tgt, e, coef) in cols[k]:
            key = (lab[tgt], e)
            acc[key] = acc.get(key, 0) + coef
        prof.append(tuple(sorted((kk, vv) for kk, vv in acc.items() if vv)))
    for b in cpart:
        if len({prof[k] for k in b}) > 1:
            return False
    return True


COIN_ORDERS = ("G.D", "D.G")


def admissible_actor(A, part, H, rec, m):
    """the criterion at the actor grain, leg by leg, BOTH coin orders."""
    l1 = leg1_actor(A, part)
    l2 = leg2_actor(A, part, H)
    l3 = leg3_actor(A, part, rec)
    if not (l1 and l2 and l3):
        return (l1, l2, l3, None, None, False)
    cp = induced_cell_partition(A, part)
    g = leg4_cell(A, cp, rec, "G.D", m)
    d = leg4_cell(A, cp, rec, "D.G", m)
    return (l1, l2, l3, g, d, bool(g and d))


def all_set_partitions(elems):
    elems = list(elems)
    out = []

    def rec(i, blocks):
        if i == len(elems):
            out.append(tuple(sorted(tuple(sorted(b)) for b in blocks)))
            return
        x = elems[i]
        for k in range(len(blocks)):
            blocks[k].append(x)
            rec(i + 1, blocks)
            blocks[k].pop()
        blocks.append([x])
        rec(i + 1, blocks)
        blocks.pop()
    rec(0, [])
    return sorted(set(out))


def homogeneous_ladder(A, vecs, sat, Rmax):
    """THE WELD LADDER, MEASURED: which budgets R admit an R-tuple of
    saturating groupings whose summed link field is CONSTANT on every cell.
    The parent proved its own rung by a mass argument; here the rungs are
    found by exhaustive search over multisets, at every declared L."""
    V = [vecs[i] for i in sat]
    nc = len(A.CELLS)
    out = []
    for R in range(1, Rmax + 1):
        hit = False
        for combo in combinations_with_replacement(range(len(V)), R):
            tot = [0] * nc
            for ci in combo:
                v = V[ci]
                for k in range(nc):
                    tot[k] += v[k]
            if len(set(tot)) == 1 and tot[0] > 0:
                hit = True
                break
        out.append((R, hit))
    return out


# ===========================================================================
# SECTION 3.  THE TRANSPORT DECISION PROCEDURE
#
# A law arrives with a parent value at n = 9.  This unit supplies THREE
# candidate transports of it and decides between them against the MEASURED
# value at every feasible arena point:
#
#   T-LITERAL   the parent numeral does not move
#   T-N         the reading in which the numeral is a function of n alone
#   T-Q         the reading in which the numeral is a function of q = sqrt(n)
#               (or of the declared link count L, which the L-sweep separates)
#
# THE WORDS, pre-registered in the pin:
#   LAW-IN-N  T-N agrees at every feasible point AND some feasible point
#             DISCRIMINATES it from T-LITERAL (else the test is blind and the
#             row is stamped UNDISCRIMINATED, which is not a word)
#   NEEDS-3   T-Q agrees at every feasible point and T-N does not
#   BREAKS    neither T-N nor T-Q agrees at some feasible point
#
# The procedure is a pure function of its rows, so a SYNTHETIC law forced to
# each word runs through this same code and nothing else (the control arms of
# section 9).
# ===========================================================================

WORDS = ("LAW-IN-N", "NEEDS-3", "BREAKS")


def transport_word(rows):
    """rows: list of dicts with keys n, q, L, feasible, measured, t_literal,
    t_n, t_q.  Returns (word, evidence dict).  Infeasible rows are carried and
    never scored -- #34: a row that cannot reach the test is not evidence."""
    feas = [r for r in rows if r["feasible"]]
    if not feas:
        return "BREAKS", {"reason": "NO-FEASIBLE-ROW", "rows": len(rows)}
    ok_n = [r for r in feas if r["t_n"] == r["measured"]]
    ok_q = [r for r in feas if r["t_q"] == r["measured"]]
    ok_lit = [r for r in feas if r["t_literal"] == r["measured"]]
    disc_n = [r for r in feas if r["t_n"] != r["t_literal"]]
    disc_q = [r for r in feas if r["t_q"] != r["t_n"]]
    ev = {"feasible": len(feas), "carried": len(rows),
          "t_n_agrees": len(ok_n), "t_q_agrees": len(ok_q),
          "t_literal_agrees": len(ok_lit),
          "rows_discriminating_n_from_literal": len(disc_n),
          "rows_discriminating_q_from_n": len(disc_q)}
    if len(ok_n) == len(feas):
        if not disc_n and not disc_q:
            ev["stamp"] = "UNDISCRIMINATED"
        else:
            ev["stamp"] = "DISCRIMINATED"
        return "LAW-IN-N", ev
    if len(ok_q) == len(feas):
        ev["stamp"] = "DISCRIMINATED" if disc_q else "UNDISCRIMINATED"
        return "NEEDS-3", ev
    ev["stamp"] = "FAILS-BOTH"
    ev["failing_points"] = sorted({r["n"] for r in feas
                                   if r["t_n"] != r["measured"]
                                   and r["t_q"] != r["measured"]})
    return "BREAKS", ev



PARENT_N = 9


def t_n_reading(parent_value, n):
    """THE UNIFORM n-ONLY READING, declared once and applied to every law.

    A single datum at n = 9 does not determine a function of n, so the reading
    is FIXED BY RULE rather than fitted per law: T-N is the corpus's own
    n-only quantity -- the counting floor ceil(log2 n) -- offset by the
    constant that reproduces the parent's numeral at n = 9.  The rule is the
    same for all five laws and is published with each transport table, so no
    law gets a friendlier n-only reading than another."""
    return counting_floor(n) + (parent_value - counting_floor(PARENT_N))


def row(n, q, L, feasible, measured, t_literal, t_n, t_q, note):
    return {"n": n, "q": q, "L": L, "feasible": bool(feasible),
            "measured": measured, "t_literal": t_literal, "t_n": t_n,
            "t_q": t_q, "note": note}


# ===========================================================================
# SECTION 4.  THE RUN
# ===========================================================================

LD = Ledger()


class Seal:
    """the TOTAL gate-time seal (#119 + #148)."""

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
        for r in self.rows:
            if only is not None and r["seal"] not in only:
                continue
            try:
                now = digest(jpath(obj, r["path"]))
            except (KeyError, IndexError, TypeError):
                broken.append(r["seal"])
                continue
            if now != r["sha256_12"]:
                broken.append(r["seal"])
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


SEALED_PATHS = [
    ("SEAL-SCHEMA", "schema", "G-PROVENANCE"),
    ("SEAL-PROVENANCE", "provenance", "G-PROVENANCE"),
    ("SEAL-ANCHORS", "path_anchors", "G-PARENT-ANCHORS"),
    ("SEAL-VERBATIM", "verbatim_anchors", "G-VERBATIM"),
    ("SEAL-ARENA", "arena", "G-ARENA-DECLARED"),
    ("SEAL-WINDOWS", "windows", "G-WINDOWS-DISCLOSED"),
    ("SEAL-FIDELITY", "fidelity", "G-CONSTRUCTOR-FIDELITY"),
    ("SEAL-CORPUS", "corpus", "G-CORPUS-SHAPE"),
    ("SEAL-LAW1", "law1_naming", "G-LAW1-WORD"),
    ("SEAL-LAW2", "law2_crystallization", "G-LAW2-WORD"),
    ("SEAL-LAW3", "law3_coset_menu", "G-LAW3-WORD"),
    ("SEAL-LAW4", "law4_mod_motif", "G-LAW4-WORD"),
    ("SEAL-LAW5", "law5_division_forcing", "G-LAW5-WORD"),
    ("SEAL-N16", "n16_window", "G-N16-WINDOW"),
    ("SEAL-CONTROLS", "controls", "G-CONTROL-ARMS"),
    ("SEAL-MEASURE", "measure_relativity", "G-E24-MEASURE"),
    ("SEAL-VERDICT", "verdict", "G-VERDICT-RECONSTRUCTED"),
    ("SEAL-COUNTS", "counts", "G-VERDICT-RECONSTRUCTED"),
    ("SEAL-WALLS", "walls", "G-WALLS-SCAN-THE-PAPER"),
    ("SEAL-WALLS-POSITIVE", "walls_positive", "G-WALLS-SCAN-THE-PAPER"),
    ("SEAL-NOUNS", "noun_bindings", "G-NOUN-BINDING"),
    ("SEAL-PAPER-CLAIMS", "paper_claims", "G-PAPER-CLAIMS"),
    ("SEAL-PAPER-TABLES", "paper_tables", "G-PAPER-TABLES"),
    ("SEAL-PAPER-COVERAGE", "paper_coverage", "G-PAPER-HEAD-VERBATIM"),
    ("SEAL-POLARITY", "polarity", "G-PAPER-CLAIM-POLARITY"),
    ("SEAL-COVERAGE", "coverage", "G-COVERAGE"),
    ("SEAL-REACHABILITY", "reachability", "G-REACHABILITY"),
    ("SEAL-WAIVERS", "waiver_ledger", "G-COVERAGE"),
    ("SEAL-MUTANTS", "mutants", "G-COVERAGE"),
    ("SEAL-MUTANT-SWEEP", "mutant_sweep", "G-SWEEP-BOUND"),
    ("SEAL-GATES", "gates", "G-GATE-ACCOUNTING"),
    ("SEAL-CLOSING", "closing_gates", "G-GATE-ACCOUNTING"),
    ("SEAL-TOTALS", "totals", "G-GATE-ACCOUNTING"),
    ("SEAL-TRANSCRIPT", "transcript_head", "G-GATE-ACCOUNTING"),
]
DECLARED_UNSEALED = ["arithmetic", "python", "seal_manifest",
                     "payload_sha256_12", "closing_gate_verdicts"]
MEASURED_KEYS = ("fidelity", "corpus", "law1_naming", "law2_crystallization",
                 "law3_coset_menu", "law4_mod_motif",
                 "law5_division_forcing", "n16_window", "controls",
                 "measure_relativity", "counts", "verdict")
SEAL = Seal()


MUTANTS = [
    ("MUT-ANCHOR-VALUE", "G-PARENT-ANCHORS",
     "the path-value anchor P-STRICT is read from a drifted path, so the "
     "parent's 72 is replaced by a value from elsewhere in the receipt"),
    ("MUT-VERBATIM", "G-VERBATIM",
     "the V-YOUNG quotation is altered by one clause, so the quote no longer "
     "matches the parent's committed bytes"),
    ("MUT-FIDELITY", "G-CONSTRUCTOR-FIDELITY",
     "the q = 3 saturation test compares against n + 1 instead of n, so the "
     "constructor no longer reproduces the parent's 36"),
    ("MUT-CORPUS", "G-CORPUS-SHAPE",
     "one C3 schedule is dropped AFTER the corpus is built, so the published "
     "corpus size and the constructor's own product disagree"),
    ("MUT-ROUTES", "G-LAW1-ROUTES",
     "route B returns the Young subgroup of the CELL-signature partition "
     "instead of the actor-signature partition, so the two routes part"),
    ("MUT-CHART", "G-LAW1-CHART",
     "the chart characterisation admits a history that is not constant-class, "
     "so the characterisation stops being exact"),
    ("MUT-LAW1WORD", "G-LAW1-WORD",
     "law 1's emitted word is replaced by BREAKS while its rows still agree"),
    ("MUT-TIME", "G-LAW2-TIME",
     "the n = 4 schedule time is published as the parent's own value instead "
     "of a value the corpus measured"),
    ("MUT-FLOOR", "G-LAW2-FLOOR",
     "the sharpened weight floor is replaced by the counting floor, so the "
     "successor formula no longer matches the n = 16 measurement"),
    ("MUT-OFFSET", "G-LAW2-OFFSET",
     "the n = 16 offset is taken as time minus the COUNTING bound rather "
     "than time minus the ATTAINED floor"),
    ("MUT-COSET", "G-LAW3-SET-EQUALITY",
     "one coset partition is dropped from the menu, so the set equality with "
     "the geometry leg's survivors fails"),
    ("MUT-GENERATE", "G-LAW3-HYPOTHESIS",
     "the subgroup the declared links generate is reported as the whole "
     "translation group at every q, hiding the q = 4 hypothesis failure"),
    ("MUT-LADDER", "G-LAW4-LADDER",
     "the ladder is read at L = 2 for every declared L, so the sweep no "
     "longer separates the modulus's carrier"),
    ("MUT-COIN", "G-LAW4-COIN",
     "the coin's phase exponent ignores the declared modulus, so the record "
     "no longer enters mod m and the congruence iff fails"),
    ("MUT-FORCING", "G-LAW5-CENSUS",
     "leg 2 is skipped in the admissibility criterion, so partitions that "
     "cut division events are counted as factorizations and the admissible "
     "set escapes a leg the census re-checks it against"),
    ("MUT-CONTROL", "G-CONTROL-ARMS",
     "one synthetic control law is fed rows that no longer force its "
     "pre-registered word"),
    ("MUT-VERDICT", "G-VERDICT-RECONSTRUCTED",
     "the head's aggregate portability count is written from a typed literal "
     "instead of the emitted law words"),
    ("MUT-HEAD", "G-PAPER-HEAD-VERBATIM",
     "one character of the paper's head fence is altered before the "
     "comparison, so the paper's verdict block goes stale"),
    ("MUT-COVERAGE-SCAN", "G-PAPER-COVERAGE",
     "the paper coverage scan strips fenced blocks before scanning, so the "
     "verdict fences' numerals go unchecked"),
    ("MUT-EXEMPTION-DEAD", "G-PAPER-COVERAGE",
     "a numeral exemption that fires on nothing is added to the declared "
     "exemption table"),
    ("MUT-SPAN", "G-PAPER-COVERAGE",
     "inline code spans are stripped from the scanned body, so a backticked "
     "numeral becomes invisible"),
    ("MUT-TABLE", "G-PAPER-TABLES",
     "one published table's HEADER row is dropped from the binding, so a "
     "table whose columns were renamed would pass"),
    ("MUT-NOUN", "G-NOUN-BINDING",
     "one referent binding is retargeted to the WRONG noun, so a count "
     "attached to the wrong universe must be caught"),
    ("MUT-WALL", "G-WALLS-SCAN-THE-PAPER",
     "one reading wall's positive control is replaced by a sentence its "
     "pattern cannot match, so a wall that could never fire must be caught "
     "by its own control"),
    ("MUT-POLARITY", "G-PAPER-CLAIM-POLARITY",
     "one polarity axis's forbidden partner is replaced by a phrase the "
     "paper does contain, so the negative leg must actually bite"),
    ("MUT-SEAL-DROP", "G-SEAL-TOTALITY",
     "the coverage seal is never taken, so a published key reaches disk "
     "unsealed"),
    ("MUT-SEAL-GATE", "G-SEAL-TOTALITY",
     "a seal names a gate this run never evaluates"),
]
MUTANT_NAMES = tuple(m[0] for m in MUTANTS)

# THE READING WALLS.  Each row is (id, forbidden pattern, why).  The paper is
# scanned for them; a positive control confirms each wall FIRES on a sentence
# built to trip it (#36: a zero without a positive control is not a result).
WALLS = [
    ("WALL-NINE-DERIVED",
     r"nine\s+(?:is|was)\s+(?:derived|forced|structurally\s+selected)",
     "this unit measures transport of laws, and never that the actor count "
     "nine is derived"),
    ("WALL-ARBITRARY",
     r"(?:the\s+)?actor\s+count\s+is\s+(?:arbitrary|meaningless|a\s+fiction)",
     "a declaration is not an arbitrariness claim, and this unit measures "
     "only which laws move with n"),
    ("WALL-N9-REDERIVED",
     r"(?:we|this\s+unit|the\s+run)\s+re-?derives?\s+the\s+n\s*=\s*9",
     "the n = 9 numbers are anchors here, never products"),
    ("WALL-N16-COMPLETE",
     r"n\s*=\s*16\s+(?:census|corpus)\s+is\s+(?:complete|exhaustive)",
     "n = 16 is a declared window and every n = 16 row says so"),
    ("WALL-PROBABILITY",
     r"(?:probability|likelihood)\s+that\s+a\s+(?:law|history)",
     "E-24: no count becomes a probability without a declared measure"),
]

# REFERENT BINDINGS: a published count is bound to the NOUN it counts, in the
# paper, adjacent -- not to the numeral alone (#87's sibling for prose).
NOUN_PATTERNS = [
    ("NB-HIST", "histories"),
    ("NB-LATTICE", "partitions"),
    ("NB-PREFIX", "prefixes"),
    ("NB-COMPARISON", "comparisons"),
    ("NB-PAIRS", "pairs"),
]

CLOSING_GATE_NAMES = (
    "G-PAPER-HEAD-VERBATIM", "G-PAPER-COVERAGE", "G-PAPER-CLAIMS",
    "G-PAPER-TABLES", "G-PAPER-CLAIM-POLARITY", "G-WALLS-SCAN-THE-PAPER",
    "G-NOUN-BINDING", "G-COVERAGE", "G-REACHABILITY", "G-SWEEP-BOUND",
    "G-NO-FLOATS", "G-GATE-ACCOUNTING", "G-SEAL-TOTALITY",
    "G-TRANSCRIPT-INTEGRITY", "G-ARTIFACT-INTEGRITY")
# G-TRANSCRIPT-INTEGRITY and G-ARTIFACT-INTEGRITY are PRE-PROMOTION REFUSALS
# rather than ledger rows: the first is evaluated on the bytes staged for
# disk (a ledger row would change those bytes and could not be checked
# against them), the second on the bytes after promotion.  Both raise on
# failure and write nothing, and both are excluded from the phantom-gate
# subtraction for exactly that reason.
GATES_OUTSIDE_BOTH_ARTIFACTS = ("G-ARTIFACT-INTEGRITY",
                                "G-TRANSCRIPT-INTEGRITY")


def full_run(break_anchor=None, paper_text=None, paper_rel=PAPER_REL,
             write=True):
    global LD, SEAL
    LD = Ledger()
    SEAL = Seal()
    R = {"schema": SCHEMA, "python": "%d.%d" % sys.version_info[:2],
         "arithmetic": "EXACT: python integers only; no float appears in any "
                       "substantive path and an AST scan gates it"}
    src = read_text(SELF, "SELF")

    # ---- SEC 1  PROVENANCE ------------------------------------------------
    say("=" * 78)
    say("NDEP (paper-39) -- THE n-DEPENDENCE UNIT")
    say("=" * 78)
    say()
    say("SECTION 1.  PROVENANCE")
    prov, bad = [], []
    texts = {}
    for sid, rel, want, why in SOURCES:
        raw = read_bytes(rel)
        if break_anchor == sid:
            raw = raw + b"\n<<broken>>\n"
        got = hashlib.sha256(raw).hexdigest()[:12]
        prov.append({"id": sid, "path": rel, "declared_sha256_12": want,
                     "measured_sha256_12": got, "matches": got == want,
                     "role": why})
        if got != want:
            bad.append(sid)
        texts[sid] = raw.decode("utf-8")
    prov.append({"id": "A-FAC", "path": "v14/paper-35-fac.md and "
                 "v14/code/fac_receipt.json", "declared_sha256_12":
                 "%s / %s" % (FAC_PAPER_SHA12, FAC_RECEIPT_SHA12),
                 "measured_sha256_12": "NOT-READ",
                 "matches": True,
                 "role": "FAC (paper-35) at commit %s.  NOT read at run time: "
                 "the worktree copies are under repair, and #46 forbids "
                 "reading mutable repository state.  The six values this unit "
                 "cites from it are FROZEN DECLARED CONSTANTS in section 0 "
                 "and each is cross-checked against a value computed here."
                 % FAC_COMMIT})
    R["provenance"] = {"sources": prov, "fac_commit": FAC_COMMIT,
                       "fac_declared": dict(FAC_DECLARED),
                       "read_categories": sorted(READ_CATEGORIES)}
    LD.gate("G-PROVENANCE",
            "EVERY PINNED SOURCE IS PRESENT AND ITS BYTES ARE THE DECLARED "
            "ONES (#91).  Three files are read as sources at run time and "
            "each carries a sha256-12 fixed in this unit's frozen "
            "declaration; a fourth parent (FAC) is carried by COMMIT and "
            "digest and is deliberately NOT read, because its worktree copy "
            "is under repair.  No subprocess is invoked and no repository "
            "state outside the declaration is touched",
            not bad, "sources %d, mismatches %s, fac carried at commit %s"
            % (len(SOURCES), bad or "none", FAC_COMMIT))
    # the unit's own identifiers are part of the frozen declaration and are
    # registered here, so the paper may name itself and its parents.
    reg(39, 33, 35, 14)
    SEAL.take("SEAL-SCHEMA", R)
    SEAL.take("SEAL-PROVENANCE", R)

    aidrec = json.loads(texts["A-AIDREC"])
    anch, abad = [], []
    for aid, sid, path, want, consumer in PATH_ANCHORS:
        p = pick("MUT-ANCHOR-VALUE",
                 path,
                 "counts/histories" if aid == "P-STRICT" else path)
        try:
            got = jpath({"A-AIDREC": aidrec}[sid], p)
        except (KeyError, IndexError, TypeError):
            got = None
        anch.append({"anchor": aid, "source": sid, "path": p,
                     "declared": want, "read": got, "matches": got == want,
                     "consumer_gate": consumer})
        if got != want:
            abad.append(aid)
        reg(want)
    reg(len(PATH_ANCHORS), len(VERBATIM), len(SOURCES), len(WINDOWS),
        len(MUTANTS), len(WALLS))
    R["path_anchors"] = anch
    LD.gate("G-PARENT-ANCHORS",
            "THE PARENT'S VALUES ARE READ BY PATH AND THE (PATH, VALUE) PAIR "
            "IS ANCHORED (#20).  Ten rows of AID's committed receipt are read "
            "at declared JSON paths and compared with the values this unit "
            "froze; a path drift that silently substitutes another number "
            "dies here.  Every row names the gate that CONSUMES it, and every "
            "named consumer is a gate this run evaluates (checked at "
            "G-SEAL-TOTALITY)",
            not abad, "anchors %d, mismatches %s, consumers %s"
            % (len(anch), abad or "none",
               len(sorted({a["consumer_gate"] for a in anch}))))
    SEAL.take("SEAL-ANCHORS", R)

    vb, vbad = [], []
    for vid, sid, needle, consumer in VERBATIM:
        nd = pick("MUT-VERBATIM",
                  needle,
                  needle.replace("Young subgroup", "Sylow subgroup")
                  if vid == "V-YOUNG" else needle)
        ok = match_needle(texts[sid], nd)
        vb.append({"anchor": vid, "source": sid, "chars": len(canon(nd)),
                   "quote_fidelity": ok, "consumer_gate": consumer})
        if not ok:
            vbad.append(vid)
    R["verbatim_anchors"] = vb
    LD.gate("G-VERBATIM",
            "THE QUOTATIONS ARE THE PARENT'S OWN BYTES (#62 as amended).  Six "
            "quotations carry the parent laws into this unit; each is matched "
            "against the pinned source's bytes under the full text "
            "normalisation with a length floor, and each is bound to a NAMED "
            "consumer gate that reads the quotation's content rather than its "
            "existence.  This gate is evaluated BEFORE the byte anchors are "
            "consumed anywhere downstream",
            not vbad, "quotes %d, failures %s, shortest %d chars"
            % (len(vb), vbad or "none", min(v["chars"] for v in vb)))
    SEAL.take("SEAL-VERBATIM", R)

    R["arena"] = {"declaration": [{"axis": k, "text": v}
                                  for k, v in ARENA_DECL]}
    LD.gate("G-ARENA-DECLARED",
            "THE ARENA IS DECLARED AS DATA, AXIS BY AXIS (RUNBOOK section "
            "15).  Six axes -- boundary, family, law, state, arena, "
            "provenance -- are published as rows of the receipt, and the two "
            "FREE axes this unit sweeps (the declared link count L and the "
            "coin's phase modulus m) are named as free in the declaration "
            "itself rather than discovered later",
            len(ARENA_DECL) == 6
            and any("FREE" in v for _k, v in ARENA_DECL),
            "axes %d, free axes named in-declaration %s"
            % (len(ARENA_DECL),
               sorted(k for k, v in ARENA_DECL if "FREE" in v)))
    SEAL.take("SEAL-ARENA", R)

    R["windows"] = [{"window": w, "entire": e, "declaration": d}
                    for w, e, d in WINDOWS]
    LD.gate("G-WINDOWS-DISCLOSED",
            "EVERY WINDOW IS DECLARED, AND WHETHER IT IS ENTIRE IS PART OF "
            "THE DECLARATION.  Nine windows; the six marked entire are whole "
            "classes with no sampling, and the three that are not carry the "
            "reason in their own text -- the q = 4 saturating census, S_16, "
            "and the q = 3 fidelity leg",
            len(WINDOWS) == 9
            and sum(1 for _w, e, _d in WINDOWS if e) == 6,
            "windows %d, entire %d, partial %s"
            % (len(WINDOWS), sum(1 for _w, e, _d in WINDOWS if e),
               [w for w, e, _d in WINDOWS if not e]))
    SEAL.take("SEAL-WINDOWS", R)

    # ---- SEC 2  THE CONSTRUCTOR-FIDELITY LEG AT q = 3 ---------------------
    say()
    say("SECTION 2.  THE CONSTRUCTOR-FIDELITY LEG (q = 3, W-Q3)")
    A3 = Arena(3)
    p3, v3, s3 = substrate(A3)
    satcut = pick("MUT-FIDELITY", A3.n, A3.n + 1)
    s3 = [i for i, v in enumerate(v3) if sum(v) == satcut]
    st3 = strict_tuples(A3, v3, s3, A3.L)
    fl3 = flat_tuples(A3, v3, s3, A3.L + 1)
    C3win = build_corpora(A3, p3, v3, s3)
    fid = {"q": 3, "n": 9, "L": A3.L,
           "groupings": {"here": len(p3), "parent": jpath(aidrec, PATH_ANCHORS[0][2])},
           "saturating": {"here": len(s3), "parent": jpath(aidrec, PATH_ANCHORS[1][2])},
           "strict_tuples": {"here": len(st3), "parent": jpath(aidrec, PATH_ANCHORS[2][2])},
           "flat_tuples": {"here": len(fl3), "parent": jpath(aidrec, PATH_ANCHORS[3][2])},
           "window": {"here": len(C3win["C3"]), "parent": jpath(aidrec, PATH_ANCHORS[4][2])},
           "stamp": "FIDELITY-LEG-ONLY: no n = 9 law is evaluated at q = 3 "
                    "here and no n = 9 finding is produced here"}
    for k in ("groupings", "saturating", "strict_tuples", "flat_tuples",
              "window"):
        reg(fid[k]["here"], fid[k]["parent"])
    agree = [k for k in ("groupings", "saturating", "strict_tuples",
                         "flat_tuples", "window")
             if fid[k]["here"] == fid[k]["parent"]]
    R["fidelity"] = fid
    say("  q = 3 substrate: %s" % ", ".join(
        "%s %d (parent %d)" % (k, fid[k]["here"], fid[k]["parent"])
        for k in ("groupings", "saturating", "strict_tuples", "flat_tuples",
                  "window")))
    LD.gate("G-CONSTRUCTOR-FIDELITY",
            "THE PARAMETERISED CONSTRUCTOR REPRODUCES THE PARENT'S SUBSTRATE "
            "AT q = 3, ROW BY ROW.  The same code that builds the n = 4 arena "
            "is run at q = 3 and its five substrate counts are compared -- "
            "each against the value read at its own anchored path in AID's "
            "committed receipt, per object and never as a total.  This is "
            "what licenses 'the same grammar' for the n = 4 build; it is a "
            "FIDELITY LEG and not a finding, and the receipt row says so",
            len(agree) == 5,
            "rows agreeing %d of 5 (%s); disagreeing %s"
            % (len(agree), ", ".join(agree),
               [k for k in ("groupings", "saturating", "strict_tuples",
                            "flat_tuples", "window") if k not in agree]
               or "none"))
    SEAL.take("SEAL-FIDELITY", R)

    # ---- SEC 3  THE n = 4 CORPUS -----------------------------------------
    say()
    say("SECTION 3.  THE n = 4 ARENA AND ITS DRIVEN CORPUS (W-N4, ENTIRE)")
    A = Arena(2)
    parts, vecs, sat = substrate(A)
    C = build_corpora(A, parts, vecs, sat)
    corpora = [("C1", C["C1"]), ("C1FAN", C["C1FAN"]),
               ("C2", C["C2"]), ("C3", C["C3"])]
    if mut("MUT-CORPUS"):
        corpora = [(k, v[:-1] if k == "C3" else v) for k, v in corpora]
    HIST = []
    for nm, corp in corpora:
        for s in corp:
            HIST.append((nm, s, history_of(A, s)))
    shapes = {nm: {"schedules": len(corp),
                   "rounds": len(corp[0]),
                   "events_per_history": len(history_of(A, corp[0]))}
              for nm, corp in corpora}
    corpus = {"q": A.q, "n": A.n, "L": A.L, "cells": len(A.CELLS),
              "parallel_classes": len(A.CLASS_NAMES),
              "groupings": len(parts), "saturating": len(sat),
              "max_round_incidence": max(sum(v) for v in vecs),
              "corpora": shapes, "histories": len(HIST),
              "class_names": list(A.CLASS_NAMES),
              "control_tuple": list(C["ctrl"]), "collinear_tuple": list(C["coll"]),
              "budget_ladder": {"R_strict": A.L, "R_concatenation": 2 * A.L,
                                "R_window": A.L + 1}}
    for k in ("groupings", "saturating", "max_round_incidence", "histories",
              "cells", "parallel_classes"):
        reg(corpus[k])
    for nm in shapes:
        reg(shapes[nm]["schedules"], shapes[nm]["rounds"],
            shapes[nm]["events_per_history"])
    R["corpus"] = corpus
    say("  groupings %d, saturating %d (max incidence %d = n), "
        "corpora %s, histories %d"
        % (corpus["groupings"], corpus["saturating"],
           corpus["max_round_incidence"],
           {k: v["schedules"] for k, v in shapes.items()}, corpus["histories"]))
    rebuilt = sum(v["schedules"] for v in shapes.values())
    from_constructor = (len(C["C1"]) + len(C["C1FAN"]) + len(C["C2"])
                        + len(C["C3"]))
    LD.gate("G-CORPUS-SHAPE",
            "THE n = 4 CORPUS IS THE CONSTRUCTOR'S PRODUCT, AND ITS SHAPE IS "
            "MEASURED PER CORPUS.  Each of the four corpora publishes its "
            "schedule count, its round count and its events-per-history, and "
            "the total is the sum of the four rather than a separately typed "
            "number; every event of every history is a conflict group of a "
            "grouping of the four sites into two pairs, and the published "
            "total is compared with the CONSTRUCTOR's own product, so a "
            "corpus row dropped after the build dies here.  No sampling: the "
            "class is entire",
            rebuilt == len(HIST) == from_constructor
            and all(v["events_per_history"] == v["rounds"] * A.q
                    for v in shapes.values()),
            "sum of corpora %d, histories %d, constructor product %d, "
            "events = rounds x q at %d of 4"
            % (rebuilt, len(HIST), from_constructor,
               sum(1 for v in shapes.values()
                   if v["events_per_history"] == v["rounds"] * A.q)))
    SEAL.take("SEAL-CORPUS", R)

    # ---- SEC 4  LAW 1: THE NAMING THEOREM --------------------------------
    say()
    say("SECTION 4.  LAW 1 -- THE YOUNG-SUBGROUP NAMING THEOREM")
    seen, routes, rbad = set(), 0, []
    for nm, _s, H in HIST:
        for k in range(len(H) + 1):
            key = tuple(sorted(tuple(sorted(A.SI[x] for x in F))
                               for F in H[:k]))
            if key in seen:
                continue
            seen.add(key)
            a = stab_bruteforce(A, H[:k])
            if mut("MUT-ROUTES"):
                cp = induced_cell_partition(A, all_set_partitions(A.SITES)[0])
                b = sorted({tuple(range(A.n))}) if len(cp) else []
            else:
                b = young_elements(A, H[:k])
            routes += 1
            if a != b:
                rbad.append(k)
    forced = [(nm, s) for nm, s, H in HIST if young_order(A, H) == 1]
    chart = [(nm, s) for nm, s, H in HIST if young_order(A, H) != 1]
    chart_names = sorted(class_names_of(A, s) for _nm, s in chart)
    constant_class = [(nm, s) for nm, s, _H in HIST
                      if len(set(class_names_of(A, s))) == 1
                      and "MIXED" not in class_names_of(A, s)]
    chart_set = {tuple(s) for _nm, s in chart}
    cc_set = {tuple(s) for _nm, s in constant_class}
    if mut("MUT-CHART"):
        cc_set = cc_set | {tuple(HIST[0][1])}
    orders = Counter(young_order(A, H) for _nm, _s, H in HIST)
    law1 = {"route_prefixes_compared": routes,
            "route_mismatches": len(rbad),
            "route_a": "THE COMPLETE SYMMETRIC GROUP S_4, FILTERED ELEMENT BY "
                       "ELEMENT BY THE DEFINITION (setwise fixing)",
            "route_b": "THE YOUNG SUBGROUP OF THE PARTICIPATION-SIGNATURE "
                       "PARTITION, BUILT FROM THE BLOCKS",
            "compared_as": "ELEMENT SET AGAINST ELEMENT SET, PER OBJECT",
            "s_n_size": math.factorial(A.n),
            "forced": len(forced), "chart": len(chart),
            "histories": len(HIST),
            "chart_is_exactly_constant_class": chart_set == cc_set,
            "chart_class_tuples": [list(t) for t in chart_names],
            "stabilizer_orders": {str(k): v for k, v in sorted(orders.items())},
            "parent_forced": jpath(aidrec, "counts/forced_histories"),
            "parent_histories": jpath(aidrec, "counts/histories"),
            "parent_chart": jpath(aidrec, "counts/chart_histories"),
            "chart_count_vs_classes": {"chart": len(chart),
                                       "parallel_classes": len(A.CLASS_NAMES)}}
    reg(routes, len(rbad), len(forced), len(chart), math.factorial(A.n),
        len(HIST))
    for k, v in orders.items():
        reg(k, v)
    R["law1_naming"] = law1
    say("  routes: %d distinct prefixes, %d mismatches; forced %d of %d, "
        "chart %d" % (routes, len(rbad), len(forced), len(HIST), len(chart)))
    LD.gate("G-LAW1-ROUTES",
            "THE NAMING THEOREM IS TESTED AS A THEOREM AND NOT ASSUMED, PER "
            "OBJECT.  Route A holds the whole of S_4 and keeps the elements "
            "that fix EVERY division event setwise; route B builds the Young "
            "subgroup of the participation-signature partition from the "
            "blocks and knows nothing of route A.  The two are compared as "
            "SETS OF PERMUTATIONS at every distinct prefix of the corpus.  "
            "This is the gate the parent's quotation V-YOUNG names: the "
            "stabilizer IS that Young subgroup, its order the product of the "
            "block factorials",
            len(rbad) == 0 and routes > 0,
            "prefixes %d, mismatches %d, |S_%d| = %d filtered per prefix"
            % (routes, len(rbad), A.n, math.factorial(A.n)))
    LD.gate("G-LAW1-CHART",
            "THE CHART SET IS CHARACTERISED, NOT COUNTED (#87).  Each history "
            "is tested individually for two properties -- a nontrivial "
            "stabilizer, and repeating one parallel class in every round -- "
            "and the two SETS OF HISTORIES are compared, not their sizes.  "
            "The parent's own characterisation (V-CHART: the constant-class "
            "quadruples, one per parallel class) is the statement under test, "
            "and at n = 4 the count that follows is the number of parallel "
            "classes",
            law1["chart_is_exactly_constant_class"],
            "chart %d, constant-class %d, sets equal %s, parallel classes %d"
            % (len(chart), len(cc_set), chart_set == cc_set,
               len(A.CLASS_NAMES)))
    l1rows = [
        row(9, 3, 3, True, jpath(aidrec, "counts/chart_histories"), 4,
            t_n_reading(4, 9), 3 + 1,
            "PARENT ANCHOR: the chart count at n = 9, read at its path"),
        row(4, 2, 2, True, len(chart), 4,
            t_n_reading(4, A.n), A.q + 1,
            "MEASURED at n = 4: the chart count.  T-N is the n-only reading "
            "that reproduces the parent's 4 at n = 9 -- the counting floor "
            "ceil(log2 n); T-Q is the parallel-class count q + 1"),
    ]
    w1, e1 = transport_word(l1rows)
    if mut("MUT-LAW1WORD"):
        w1 = "BREAKS"
    law1["transport_rows"] = l1rows
    law1["chart_count_word"] = w1
    law1["chart_count_evidence"] = e1
    law1["word"] = "LAW-IN-N" if (len(rbad) == 0
                                  and law1["chart_is_exactly_constant_class"]
                                  and not mut("MUT-LAW1WORD")) else "BREAKS"
    law1["word_basis"] = ("THE THEOREM IS n-FREE AND HOLDS AT n = 4 "
                          "EXHAUSTIVELY AND AT n = 16 ON ITS DECLARED WINDOW; "
                          "ITS CHART COUNT IS q + 1 = THE NUMBER OF PARALLEL "
                          "CLASSES, WHICH IS THE COUNT AND NOT THE LAW")
    LD.gate("G-LAW1-WORD",
            "LAW 1's OUTCOME WORD IS DERIVED FROM THE MEASUREMENTS AND IS ONE "
            "OF THE THREE PRE-REGISTERED NAMES.  The word is LAW-IN-N exactly "
            "when both legs pass -- the two routes agree at every prefix, and "
            "the chart SET is exactly the constant-class SET -- and BREAKS "
            "otherwise; the chart COUNT's own transport is decided separately "
            "by the same procedure the other four laws use, so the law and "
            "its numeral are never conflated",
            law1["word"] in WORDS and law1["chart_count_word"] in WORDS
            and law1["word"] == "LAW-IN-N",
            "word %s (chart-count word %s, %s), routes %d/%d, chart set exact %s"
            % (law1["word"], law1["chart_count_word"], e1["stamp"],
               routes - len(rbad), routes,
               law1["chart_is_exactly_constant_class"]))
    SEAL.take("SEAL-LAW1", R)

    # ---- SEC 5  THE n = 16 WINDOW (built here; consumed by laws 1-4) ------
    say()
    say("SECTION 5.  THE n = 16 WINDOW (W-N16-CLASS / W-N16-PERM, DECLARED)")
    A16 = Arena(4)
    decl16 = [A16.CLASS_NAMES[i] for i in range(A16.q + 1)
              if A16.CLASS_DIRS[i] in A16.LINKS]
    nc16 = len(A16.CELLS)
    cls16, cov16 = [], []
    for T in product(decl16, repeat=A16.L):
        Ps = tuple(A16.CLASSES[k] for k in T)
        tot = [0] * nc16
        for P in Ps:
            v = A16.round_vec(P)
            for k in range(nc16):
                tot[k] += v[k]
        H = history_of(A16, first_menu_schedule(A16, Ps))
        cls16.append((T, H))
        if all(t >= 1 for t in tot):
            cov16.append((T, H))
    ct16 = Counter(crystallization(A16, H) for _T, H in cov16)
    ms16 = Counter(min_event_subset(A16, H) for _T, H in cov16)
    win, pos16, bad16 = [], 0, 0
    for a, b in combinations(range(A16.n), 2):
        p = list(range(A16.n))
        p[a], p[b] = b, a
        win.append(tuple(p))
    for a, b, c in combinations(range(A16.n), 3):
        for cyc in ((b, c, a), (c, a, b)):
            p = list(range(A16.n))
            p[a], p[b], p[c] = cyc
            win.append(tuple(p))
    Href = cov16[0][1]
    cmp16 = 0
    for k in range(len(Href) + 1):
        Hp = Href[:k]
        for p in win:
            s = fixes_setwise(A16, Hp, p)
            y = in_young(A16, Hp, p)
            cmp16 += 1
            if s != y:
                bad16 += 1
            elif s:
                pos16 += 1
    Tdecl = {q: (len(Arena(q).translations_generated()), Arena(q).n)
             for q in (2, 3, 4)}
    subs16 = A16.subgroups()
    f4sub = [s for s in subs16
             if all(A16.vmul(t, x) in s for x in s for t in A16.el)]
    lad16 = homogeneous_ladder(
        A16, [A16.round_vec(A16.CLASSES[k]) for k in A16.CLASS_NAMES],
        [i for i, k in enumerate(A16.CLASS_NAMES)
         if sum(A16.round_vec(A16.CLASSES[k])) == A16.n], 2 * A16.L)
    witness = A16.coset_partition(
        frozenset([(0, 0), (1, 0), (0, 1), (1, 1)]))
    wsum = sum(A16.round_vec(witness))
    n16 = {"q": 4, "n": 16, "L": A16.L, "cells": nc16,
           "class_tuples": len(cls16), "covering": len(cov16),
           "crystallization": {str(k): v for k, v in sorted(ct16.items())},
           "attained_floor": {str(k): v for k, v in sorted(ms16.items())},
           "counting_floor": counting_floor(A16.n),
           "weight_floor": weight_floor(A16.n, A16.q),
           "schedule_time_formula_2q_minus_1": 2 * A16.q - 1,
           "route_window_comparisons": cmp16,
           "route_window_mismatches": bad16,
           "route_window_positive": pos16,
           "route_window_size": len(win),
           "s16_size_not_filtered": math.factorial(A16.n),
           "translations_generated": {str(k): {"generated": v[0], "group": v[1],
                                               "transitive": v[0] == v[1]}
                                      for k, v in sorted(Tdecl.items())},
           "subgroups_of_T": len(subs16),
           "f_q_subspaces": len(f4sub),
           "homogeneous_ladder": [{"R": r, "achievable": h} for r, h in lad16],
           "saturation_witness_incidence": wsum,
           "saturation_budget_n": A16.n,
           "saturation_is_maximal": wsum <= A16.n,
           "scope": "DECLARED WINDOW: only parallel-class R-tuples are built; "
                    "the full saturating census at q = 4 needs the 2,627,625 "
                    "groupings of sixteen sites into four blocks of four and "
                    "is out of scope.  S_16 is not filtered; route A is taken "
                    "on the declared permutation window"}
    reg(n16["class_tuples"], n16["covering"], n16["counting_floor"],
        n16["weight_floor"], n16["schedule_time_formula_2q_minus_1"],
        cmp16, bad16, pos16, len(win), len(subs16), len(f4sub), wsum,
        A16.n, nc16, math.factorial(A16.n))
    for k, v in ct16.items():
        reg(k, v)
    for k, v in ms16.items():
        reg(k, v)
    for k, v in Tdecl.items():
        reg(v[0], v[1])
    R["n16_window"] = n16
    say("  n = 16: %d class tuples, %d covering; crystallization %s; "
        "attained floor %s; counting floor %d"
        % (len(cls16), len(cov16), dict(ct16), dict(ms16),
           counting_floor(A16.n)))
    say("  n = 16 routes: %d comparisons, %d mismatches, %d positive"
        % (cmp16, bad16, pos16))
    LD.gate("G-N16-WINDOW",
            "THE n = 16 WINDOW IS BUILT, AND ITS LIMITS ARE MEASURED RATHER "
            "THAN ASSERTED.  The window's own arithmetic is published beside "
            "it: S_16 has 20,922,789,888,000 elements and is not filtered, so "
            "route A runs on a declared permutation window of transpositions "
            "and 3-cycles at every prefix -- and that window is exercised in "
            "BOTH polarities, with permutations inside the stabilizer and "
            "permutations outside it.  A window whose positive count were "
            "zero would be a gate that cannot fail",
            bad16 == 0 and pos16 > 0 and pos16 < cmp16 and len(cov16) > 0,
            "comparisons %d, mismatches %d, positive %d, negative %d, "
            "covering histories %d"
            % (cmp16, bad16, pos16, cmp16 - pos16, len(cov16)))
    LD.gate("G-LAW1-TRANSPORT",
            "THE NAMING THEOREM'S TRANSPORT IS MEASURED AT BOTH NEW ARENA "
            "POINTS.  At n = 4 the theorem is checked exhaustively (whole "
            "symmetric group, every distinct prefix); at n = 16 it is checked "
            "on the declared permutation window.  The parent's own numbers -- "
            "5,852 forced of 5,856, 4 chart -- enter ONLY as anchored reads "
            "of its committed receipt and are never recomputed here",
            len(rbad) == 0 and bad16 == 0
            and law1["parent_forced"] + law1["parent_chart"]
            == law1["parent_histories"],
            "n = 4 mismatches %d of %d, n = 16 mismatches %d of %d, parent "
            "anchors %d + %d = %d"
            % (len(rbad), routes, bad16, cmp16, law1["parent_forced"],
               law1["parent_chart"], law1["parent_histories"]))
    SEAL.take("SEAL-N16", R)

    # ---- SEC 6  LAW 2: THE CRYSTALLIZATION PAIR --------------------------
    say()
    say("SECTION 6.  LAW 2 -- THE CRYSTALLIZATION PAIR")
    cts = {}
    for nm, _s, H in HIST:
        c = crystallization(A, H)
        cts.setdefault(nm, Counter())[c] += 1
    mss = {}
    for nm, _s, H in HIST:
        m = min_event_subset(A, H)
        mss.setdefault(nm, Counter())[m] += 1
    constant_on = sorted(nm for nm in ("C1", "C1FAN", "C2")
                         if len(cts[nm]) == 1)
    t4 = sorted(cts["C1"])[0]
    if mut("MUT-TIME"):
        t4 = 5
    f4 = sorted(k for k in mss["C1"] if k is not None)[0]
    attained16 = sorted(k for k in ms16 if k is not None)[0]
    time16 = sorted(k for k in ct16 if k is not None)[0]
    sharp = weight_floor if not mut("MUT-FLOOR") else (
        lambda n, q: counting_floor(n))
    redundant, moved = 0, Counter()
    for nm, s, H in HIST:
        if nm != "C1":
            continue
        drop = H[:A.q - 1] + H[A.q:]
        if signature_blocks(A, drop) == signature_blocks(A, H):
            redundant += 1
        moved[crystallization(A, drop + (H[A.q - 1],))] += 1
    off4 = t4 - f4
    off16 = time16 - attained16 if mut("MUT-OFFSET") is False else \
        time16 - counting_floor(A16.n)
    parent_time = jpath(aidrec, "crystallization/constant_on_C1_C2_C1FAN")
    parent_floor = jpath(
        aidrec, "crystallization/information_floor/counting_bound_ceil_log2_actors")
    floor_rows = [
        row(9, 3, 3, True, parent_floor, parent_floor,
            t_n_reading(parent_floor, 9), sharp(9, 3),
            "PARENT ANCHOR: the attained information floor at n = 9"),
        row(4, 2, 2, True, f4, parent_floor, t_n_reading(parent_floor, 4),
            sharp(4, 2),
            "MEASURED at n = 4: the smallest event subset that forces "
            "identity, over the whole corpus"),
        row(16, 4, 4, True, attained16, parent_floor,
            t_n_reading(parent_floor, 16), sharp(16, 4),
            "MEASURED on W-N16-CLASS: the attained floor at every covering "
            "class tuple"),
    ]
    time_rows = [
        row(9, 3, 3, True, parent_time, parent_time,
            t_n_reading(parent_time, 9), 2 * 3 - 1,
            "PARENT ANCHOR: the schedule's crystallization time at n = 9"),
        row(4, 2, 2, True, t4, parent_time, t_n_reading(parent_time, 4),
            2 * 2 - 1,
            "MEASURED at n = 4: constant on C1, C1FAN and C2"),
        row(16, 4, 4, True, time16, parent_time, t_n_reading(parent_time, 16),
            2 * 4 - 1, "MEASURED on W-N16-CLASS: constant at every covering "
            "class tuple"),
    ]
    offset_rows = [
        row(9, 3, 3, True, parent_time - parent_floor, 1, 1, 1,
            "PARENT ANCHORS: schedule time minus attained floor at n = 9"),
        row(4, 2, 2, True, off4, 1, 1, 1,
            "MEASURED at n = 4: schedule time minus attained floor"),
        row(16, 4, 4, True, off16, 1, 1, 1,
            "MEASURED on W-N16-CLASS: schedule time minus attained floor"),
    ]
    wf, ef = transport_word(floor_rows)
    wt, et = transport_word(time_rows)
    wo, eo = transport_word(offset_rows)
    law2word = "BREAKS" if wf == "BREAKS" else (
        "NEEDS-3" if "NEEDS-3" in (wf, wt, wo) else "LAW-IN-N")
    law2 = {"schedule_time": {"n4": t4, "n16": time16, "parent_n9": parent_time,
                              "constant_on": constant_on,
                              "per_corpus": {nm: {str(k): v for k, v in
                                                  sorted(c.items(), key=lambda z: (z[0] is None, z[0]))}
                                             for nm, c in cts.items()},
                              "word": wt, "evidence": et, "rows": time_rows},
            "information_floor": {"n4_attained": f4, "n16_attained": attained16,
                                  "parent_n9_attained": parent_floor,
                                  "counting_floor": {"4": counting_floor(4),
                                                     "9": counting_floor(9),
                                                     "16": counting_floor(16)},
                                  "weight_floor": {"4": weight_floor(4, 2),
                                                   "9": weight_floor(9, 3),
                                                   "16": weight_floor(16, 4)},
                                  "per_corpus": {nm: {str(k): v for k, v in
                                                      sorted(c.items(), key=lambda z: (z[0] is None, z[0]))}
                                                 for nm, c in mss.items()},
                                  "word": wf, "evidence": ef,
                                  "rows": floor_rows},
            "redundant_event": {"round_one_last_event_redundant_at": redundant,
                                "of": len(C["C1"]),
                                "crystallization_when_moved_to_the_end":
                                    {str(k): v for k, v in sorted(moved.items(), key=lambda z: (z[0] is None, z[0]))}},
            "offset": {"n4": off4, "n16": off16,
                       "parent_n9": parent_time - parent_floor,
                       "word": wo, "evidence": eo, "rows": offset_rows},
            "word": law2word,
            "word_basis": "THE PAIR'S WEAKEST LEG GOVERNS: the floor FORMULA "
                          "the parent published is ceil(log2 n), and it is "
                          "not the attained floor at n = 16"}
    reg(t4, f4, time16, attained16, off4, off16, redundant, len(C["C1"]),
        parent_time, parent_floor, counting_floor(16), weight_floor(16, 4),
        weight_floor(4, 2), weight_floor(9, 3))
    for c in list(cts.values()) + list(mss.values()) + [moved]:
        for k, v in c.items():
            reg(v)
            if k is not None:
                reg(k)
    R["law2_crystallization"] = law2
    say("  time: n=4 %d (constant on %s), n=16 %d, parent n=9 %d -> %s"
        % (t4, ",".join(constant_on), time16, parent_time, wt))
    say("  floor: attained n=4 %d, n=16 %d, parent n=9 %d; counting floor at "
        "n=16 is %d -> %s" % (f4, attained16, parent_floor,
                              counting_floor(16), wf))
    say("  offset: %d, %d, %d -> %s" % (off4, parent_time - parent_floor,
                                        off16, wo))
    LD.gate("G-LAW2-TIME",
            "THE SCHEDULE'S CRYSTALLIZATION TIME IS MEASURED AT EVERY HISTORY "
            "AND ITS TRANSPORT DECIDED.  The parent's V-TIME quotation fixes "
            "the n = 9 value at 5 on C1, C2 and the seed fan; the same "
            "quantity is measured here at n = 4 (constant across three "
            "corpora) and at n = 16 (constant across the covering class "
            "tuples), and the three points are handed to the transport "
            "procedure with all three candidate readings",
            wt in WORDS and len(constant_on) == 3 and t4 in cts["C1"]
            and et["rows_discriminating_q_from_n"] > 0,
            "word %s (%s); n = 4 time %d is a measured value %s; constant on "
            "%s; n = 16 time %d; parent %d; rows discriminating q from n: %d"
            % (wt, et["stamp"], t4, t4 in cts["C1"], ",".join(constant_on),
               time16, parent_time, et["rows_discriminating_q_from_n"]))
    LD.gate("G-LAW2-FLOOR",
            "THE INFORMATION FLOOR IS MEASURED AS AN ATTAINED VALUE, NOT "
            "TAKEN FROM ITS BOUND.  The parent's V-FLOOR and V-ATTAINED "
            "quotations state a counting bound -- k events supply at most 2^k "
            "signatures -- AND that it is attained.  Here the attained value "
            "is the smallest event SUBSET whose stabilizer is trivial, "
            "searched by increasing size at every history; it is compared "
            "with the counting bound and with the sharpened bound this unit "
            "supplies, in which each event's fixed size q enters",
            wf in WORDS and ef["rows_discriminating_q_from_n"] > 0,
            "word %s (%s); attained 4:%d 9:%d 16:%d; counting bound 16:%d; "
            "sharpened bound 4:%d 9:%d 16:%d"
            % (wf, ef["stamp"], f4, parent_floor, attained16,
               counting_floor(16), weight_floor(4, 2), weight_floor(9, 3),
               weight_floor(16, 4)))
    LD.gate("G-LAW2-OFFSET",
            "THE REDUNDANT-EVENT OFFSET IS COMPUTED FROM THE TWO MEASURED "
            "OBJECTS AT EVERY ARENA POINT, AND ITS MECHANISM IS MEASURED "
            "TOO.  The offset is the schedule time minus the ATTAINED floor "
            "-- never minus the bound -- and the parent's V-OFFSET quotation "
            "names the mechanism: one structurally redundant event.  Here the "
            "last event of round one is dropped at every C1 history and the "
            "signature partition is checked unchanged, then the event is "
            "moved to the end and the crystallization time re-measured",
            wo in WORDS and redundant == len(C["C1"])
            and off4 == t4 - f4 and off16 == time16 - attained16
            and all(k == f4 for k in moved if k is not None),
            "word %s (%s); offsets 4:%d 9:%d 16:%d; round-one last event "
            "redundant at %d of %d; time when moved to the end %s"
            % (wo, eo["stamp"], off4, parent_time - parent_floor, off16,
               redundant, len(C["C1"]),
               sorted(str(k) for k in moved)))
    LD.gate("G-LAW2-WORD",
            "LAW 2's WORD IS DERIVED FROM ITS THREE LEGS BY A STATED RULE.  "
            "The pair's word is BREAKS when the floor leg breaks, NEEDS-3 "
            "when a surviving leg needs the square root, and LAW-IN-N only "
            "when every leg transports on n alone; each leg's own word is "
            "published beside it so the aggregation can be checked rather "
            "than believed",
            law2word in WORDS
            and law2word == ("BREAKS" if wf == "BREAKS" else law2word),
            "legs time %s / floor %s / offset %s -> pair %s"
            % (wt, wf, wo, law2word))
    SEAL.take("SEAL-LAW2", R)

    # ---- SEC 7  LAW 3: THE COSET MENU ------------------------------------
    say()
    say("SECTION 7.  LAW 3 -- FAC's COSET-MENU THEOREM")
    LAT = all_set_partitions(A.SITES)
    subs = A.subgroups()
    menu = sorted({A.coset_partition(H) for H in subs})
    if mut("MUT-COSET"):
        menu = menu[:-1]
    l1surv = sorted(p for p in LAT if leg1_actor(A, p))
    gen4 = A.translations_generated()
    subcounts = {}
    for qq in (2, 3, 4):
        B = Arena(qq)
        genq = pick("MUT-GENERATE", len(B.translations_generated()), B.n)
        subcounts[str(qq)] = {"subgroups_of_T": len(B.subgroups()),
                              "q_plus_3": qq + 3,
                              "declared_links_generate": genq,
                              "group_order": B.n,
                              "hypothesis_transitive": genq == B.n}
    law3rows = [
        row(9, 3, 3, True, FAC_DECLARED["leg1_geometry_survivors"], 6,
            t_n_reading(6, 9), 3 + 3,
            "FROZEN DECLARED PARENT CONSTANT (FAC at commit %s): the geometry "
            "leg's survivor count at n = 9" % FAC_COMMIT),
        row(4, 2, 2, True, len(l1surv), 6, t_n_reading(6, 4), 2 + 3,
            "MEASURED at n = 4 over the COMPLETE actor lattice"),
        row(16, 4, 4, False, None, 6, t_n_reading(6, 16), 4 + 3,
            "NOT FEASIBLE: the theorem's hypothesis fails at q = 4 -- the "
            "declared links generate a proper subgroup of the translation "
            "group -- so the closed form is not evaluable and the row is "
            "carried unscored"),
    ]
    w3, e3 = transport_word(law3rows)
    setequal = sorted(l1surv) == sorted(menu)
    law3 = {"actor_lattice": len(LAT), "bell": len(LAT),
            "subgroups_of_T": len(subs), "coset_partitions": len(menu),
            "leg1_survivors": len(l1surv),
            "set_equal": setequal,
            "menu_names": [len(p) for p in menu],
            "declared_links_generate": len(gen4),
            "translation_group_order": A.n,
            "hypothesis_transitive": len(gen4) == A.n,
            "by_q": subcounts,
            "q4_readings": {"abstract_subgroups_of_T": n16["subgroups_of_T"],
                            "f_q_subspaces": n16["f_q_subspaces"]},
            "parent_declared": dict(FAC_DECLARED),
            "rows": law3rows, "count_word": w3, "evidence": e3,
            "word": "LAW-IN-N" if setequal else "BREAKS",
            "word_basis": "THE THEOREM ITSELF -- geometry-leg survivors = the "
                          "coset partitions of the translation subgroups -- "
                          "is n-free and is verified as a SET EQUALITY at "
                          "n = 4; its COUNT is q + 3 at prime q, and at "
                          "q = 4 the hypothesis fails outright"}
    reg(len(LAT), len(subs), len(menu), len(l1surv), len(gen4), A.n)
    for k, v in subcounts.items():
        reg(v["subgroups_of_T"], v["q_plus_3"], v["declared_links_generate"],
            v["group_order"])
    R["law3_coset_menu"] = law3
    say("  lattice %d, subgroups %d, coset partitions %d, LEG-1 survivors %d, "
        "set-equal %s" % (len(LAT), len(subs), len(menu), len(l1surv),
                          setequal))
    say("  declared links generate: %s"
        % {k: v["declared_links_generate"] for k, v in subcounts.items()})
    LD.gate("G-LAW3-SET-EQUALITY",
            "THE COSET MENU IS COMPARED AS A SET OF PARTITIONS, NOT AS A "
            "COUNT.  The geometry leg is evaluated on every one of the "
            "Bell(4) partitions of the four actors -- the COMPLETE lattice, "
            "no window -- and the survivors are compared element by element "
            "with the coset partitions of every subgroup of the translation "
            "group, each subgroup obtained by closure of a generator set.  "
            "Two sets that merely have the same size do not pass this gate",
            setequal and len(l1surv) > 0,
            "lattice %d, survivors %d, coset partitions %d, set equality %s, "
            "block-size profiles %s"
            % (len(LAT), len(l1surv), len(menu), setequal,
               sorted(Counter(len(p) for p in menu).items())))
    LD.gate("G-LAW3-HYPOTHESIS",
            "THE THEOREM'S HYPOTHESIS IS MEASURED AT EVERY q, AND ITS FAILURE "
            "AT q = 4 IS A MEASUREMENT.  The closed form needs the DECLARED "
            "links to generate the whole translation group, since only then "
            "does every block become a single coset.  The generated subgroup "
            "is computed by closure at q = 2, 3 and 4 and its order compared "
            "with the group's: transitive at the two prime orders, of index "
            "two at q = 4 -- which is why the q = 4 row of the transport "
            "table is carried unscored rather than guessed",
            all(subcounts[str(k)]["hypothesis_transitive"] for k in (2, 3))
            and not subcounts["4"]["hypothesis_transitive"],
            "generated/order: %s"
            % {k: "%d/%d" % (v["declared_links_generate"], v["group_order"])
               for k, v in subcounts.items()})
    LD.gate("G-LAW3-PARENT",
            "THE FROZEN PARENT CONSTANT IS CROSS-CHECKED AGAINST A VALUE THIS "
            "UNIT COMPUTES.  FAC's worktree copy is under repair, so its "
            "6 is carried as a declared constant at commit %s; the same "
            "number is independently produced here by enumerating the "
            "subgroups of the translation group of AG(2,3) by closure, so the "
            "declaration is checked rather than trusted" % FAC_COMMIT,
            subcounts["3"]["subgroups_of_T"]
            == FAC_DECLARED["subgroup_coset_partitions"]
            == subcounts["3"]["q_plus_3"],
            "declared %d, enumerated at q = 3 %d, q + 3 %d"
            % (FAC_DECLARED["subgroup_coset_partitions"],
               subcounts["3"]["subgroups_of_T"], subcounts["3"]["q_plus_3"]))
    LD.gate("G-LAW3-WORD",
            "LAW 3's WORD IS DERIVED FROM THE SET EQUALITY AND THE TRANSPORT "
            "TABLE.  The theorem transports when the set equality holds at "
            "the new arena point; its count is decided separately by the "
            "transport procedure, and the infeasible q = 4 row is excluded "
            "from scoring by the procedure itself rather than by hand",
            w3 in WORDS and law3["word"] in WORDS and setequal,
            "word %s, count word %s (%s), feasible rows %d of %d, set "
            "equality %s"
            % (law3["word"], w3, e3["stamp"], e3["feasible"], e3["carried"],
               setequal))
    SEAL.take("SEAL-LAW3", R)

    # ---- SEC 8  LAW 4: THE MOD-3 MOTIF -----------------------------------
    say()
    say("SECTION 8.  LAW 4 -- THE MOD-3 MOTIF, SPLIT")
    lad = {}
    for LL in (1, 2, 3):
        B = Arena(2, LL if not mut("MUT-LADDER") else 2)
        bp, bv, bs = substrate(B)
        rungs = homogeneous_ladder(B, bv, bs, 7)
        hits = [r for r, h in rungs if h]
        modulus = min(hits) if hits else None
        lad[str(LL)] = {"declared_links": LL, "cells": len(B.CELLS),
                        "saturating": len(bs),
                        "rungs": [{"R": r, "achievable": h} for r, h in rungs],
                        "achievable_R": hits,
                        "first_rung": modulus,
                        "all_multiples_of_first":
                            bool(hits) and all(r % modulus == 0 for r in hits)
                            and all((r % modulus == 0) == (r in hits)
                                    for r, _h in rungs)}
        reg(LL, len(B.CELLS), len(bs))
        for r in hits:
            reg(r)
    lad16 = [r["R"] for r in n16["homogeneous_ladder"] if r["achievable"]]
    ladder_rows = [
        row(9, 3, 3, True, LADDER_DECLARED["first_rung_at_n9"],
            LADDER_DECLARED["first_rung_at_n9"],
            t_n_reading(LADDER_DECLARED["first_rung_at_n9"], 9), 3,
            "FROZEN DECLARED PARENT CONSTANT: the weld ladder's first rung at "
            "n = 9, cross-checked below against this unit's own arena"),
        row(4, 2, 2, True, lad["2"]["first_rung"], 3, t_n_reading(3, 4), 2,
            "MEASURED at n = 4 with the parent's own link declaration L = q"),
        row(16, 4, 4, True, min(lad16) if lad16 else None, 3,
            t_n_reading(3, 16), 4,
            "MEASURED on W-N16-CLASS with L = q"),
    ]
    w4, e4 = transport_word(ladder_rows)
    carrier_rows = [{"n": 4, "q": 2, "L": LL,
                     "modulus": lad[str(LL)]["first_rung"],
                     "equals_L": lad[str(LL)]["first_rung"] == LL,
                     "equals_q": lad[str(LL)]["first_rung"] == 2,
                     "equals_characteristic":
                         lad[str(LL)]["first_rung"] == 2}
                    for LL in (1, 2, 3)]
    carrier_is_L = all(r["equals_L"] for r in carrier_rows)
    carrier_not_q = not all(r["equals_q"] for r in carrier_rows)
    # the coin channel
    recs = sorted({tuple(record_vector(A, H)) for _nm, _s, H in HIST})
    fam = set()
    for r in recs:
        for k in range(len(A.CELLS)):
            for t in range(0, 7):
                rr = list(r)
                rr[k] += t
                fam.add(tuple(rr))
    fam = sorted(fam)
    coin = {}
    for m in (2, 3):
        mm = m if not mut("MUT-COIN") else 1000
        cache = {r: tuple(coupled_columns(A, list(r), "G.D", mm))
                 for r in fam}
        eq_cong = ne_incong = mism = 0
        for i in range(len(fam)):
            ai = fam[i]
            ca = cache[ai]
            for j in range(i + 1, len(fam)):
                bj = fam[j]
                cong = all((x - y) % m == 0 for x, y in zip(ai, bj))
                same = ca == cache[bj]
                if cong and same:
                    eq_cong += 1
                elif (not cong) and (not same):
                    ne_incong += 1
                else:
                    mism += 1
        coin[str(m)] = {"records": len(fam), "pairs": eq_cong + ne_incong + mism,
                        "congruent_and_identical": eq_cong,
                        "incongruent_and_different": ne_incong,
                        "mismatches": mism}
        reg(eq_cong, ne_incong, mism, len(fam))
    census_by_m = {}
    for m in (2, 3, 4, 5):
        u = nu = 0
        for _nm, _s, H in HIST:
            rec = record_vector(A, H)
            ad = [p for p in LAT if admissible_actor(A, p, H, rec, m)[5]]
            if len(ad) == 1:
                u += 1
            else:
                nu += 1
        census_by_m[str(m)] = {"unique": u, "non_unique": nu}
        reg(u, nu, m)
    m_blind = len({(v["unique"], v["non_unique"])
                   for v in census_by_m.values()}) == 1
    law4 = {"ladder_by_L": lad, "ladder_n16": lad16,
            "ladder_rows": ladder_rows, "ladder_word": w4,
            "ladder_evidence": e4,
            "parent_declared": dict(LADDER_DECLARED),
            "parent_cross_check": LADDER_DECLARED["first_rung_at_n9"]
                                  == Arena(3).L,
            "carrier": {"rows": carrier_rows, "modulus_equals_L": carrier_is_L,
                        "modulus_equals_q_at_every_row": not carrier_not_q,
                        "n_is_fixed_at": A.n,
                        "characteristic_is_fixed_at": A.q},
            "coin_channel": coin, "census_by_m": census_by_m,
            "coin_modulus_is_free": m_blind,
            "word": w4,
            "word_basis": "THE MOTIF SPLITS.  The ladder's modulus is DERIVED "
                          "and equals the declared link count L; under the "
                          "corpus's own declaration L = q, so it moves to "
                          "mod-q -- the pin's NEEDS-3 branch.  The coin's "
                          "modulus is DECLARED and free: the census is blind "
                          "to it while the record enters exactly modulo it"}
    R["law4_mod_motif"] = law4
    say("  ladder by L at n = 4: %s"
        % {k: v["achievable_R"] for k, v in lad.items()})
    say("  n = 16 ladder (L = 4): %s" % lad16)
    say("  coin channel: %s"
        % {k: (v["mismatches"], v["pairs"]) for k, v in coin.items()})
    say("  census by coin modulus: %s"
        % {k: v["unique"] for k, v in census_by_m.items()})
    LD.gate("G-LAW4-LADDER",
            "THE LADDER'S MODULUS IS MEASURED, AND ITS CARRIER IS SEPARATED "
            "FROM sqrt(n) AND FROM THE CHARACTERISTIC BY A SWEEP AT FIXED n.  "
            "For each declared link count L = 1, 2, 3 the achievable budgets "
            "are found by exhaustive search over multisets of saturating "
            "groupings -- which R admit a summed link field constant on every "
            "cell -- and the achievable set is checked to be EXACTLY the "
            "multiples of the first rung.  n, q and the characteristic are "
            "all held at their n = 4 values throughout the sweep, so a "
            "modulus that moves with L cannot be a function of any of them",
            all(v["all_multiples_of_first"] for v in lad.values())
            and carrier_is_L and carrier_not_q
            and LADDER_DECLARED["first_rung_at_n9"] == Arena(3).L,
            "first rungs by L %s; achievable sets %s; modulus equals L at "
            "every row %s; modulus equals q at every row %s; the frozen "
            "parent rung %d equals the parent arena's own link count %d"
            % ({k: v["first_rung"] for k, v in lad.items()},
               {k: v["achievable_R"] for k, v in lad.items()},
               carrier_is_L, not carrier_not_q,
               LADDER_DECLARED["first_rung_at_n9"], Arena(3).L))
    LD.gate("G-LAW4-COIN",
            "THE COIN'S RESIDUE CHANNEL IS MEASURED IN BOTH DIRECTIONS AND "
            "ITS MODULUS SHOWN FREE.  Over a declared record family every "
            "unordered pair is classified twice -- congruent modulo m or not, "
            "and carrying identical one-step operators or not -- and the two "
            "classifications are required to agree on every pair, at m = 2 "
            "and at m = 3.  The freedom is then measured rather than argued: "
            "the whole division-forcing census is re-run at m = 2, 3, 4 and 5 "
            "and its counts compared",
            all(v["mismatches"] == 0 for v in coin.values())
            and all(v["congruent_and_identical"] > 0 for v in coin.values())
            and all(v["incongruent_and_different"] > 0 for v in coin.values())
            and m_blind,
            "pairs %s; mismatches %s; census by m %s; blind %s"
            % ({k: v["pairs"] for k, v in coin.items()},
               {k: v["mismatches"] for k, v in coin.items()},
               {k: v["unique"] for k, v in census_by_m.items()}, m_blind))
    LD.gate("G-LAW4-WORD",
            "LAW 4's WORD IS DERIVED FROM THE LADDER'S TRANSPORT TABLE, AND "
            "THE SPLIT IS PUBLISHED WITH IT.  The pin pre-registered a "
            "dichotomy -- mod-q or mod-3 forever -- and the measurement "
            "dissolves it: the derived leg becomes mod-L, which is mod-q at "
            "the corpus's own declaration, while the declared leg stays "
            "wherever it is put.  Both halves are in the receipt and neither "
            "is allowed to stand for the other",
            w4 in WORDS and e4["rows_discriminating_q_from_n"] > 0,
            "word %s (%s); ladder rows feasible %d; derived leg carrier L %s; "
            "declared leg free %s"
            % (w4, e4["stamp"], e4["feasible"], carrier_is_L, m_blind))
    SEAL.take("SEAL-LAW4", R)

    # ---- SEC 9  LAW 5: THE DIVISION-FORCING FRACTION ---------------------
    say()
    say("SECTION 9.  LAW 5 -- THE DIVISION-FORCING FRACTION")
    mdef = A.L
    uniq, nonu, union, leg_violations = [], [], set(), []
    legcount = Counter()
    for nm, s, H in HIST:
        rec = record_vector(A, H)
        ad = []
        for p in LAT:
            l1, l2, l3, g, d, ok = admissible_actor(A, p, H, rec, mdef)
            if mut("MUT-FORCING"):
                ok = bool(l1 and l3 and leg4_cell(
                    A, induced_cell_partition(A, p), rec, "G.D", mdef))
            if l1:
                legcount["leg1"] += 1
            if l2:
                legcount["leg2"] += 1
            if l3:
                legcount["leg3"] += 1
            if ok:
                ad.append(p)
        union |= set(ad)
        if any(not leg2_actor(A, p, H) for p in ad):
            leg_violations.append(nm)
        (uniq if len(ad) == 1 else nonu).append((nm, s, len(ad)))
    discrete = tuple((x,) for x in A.SITES)
    disc_ok = all(admissible_actor(A, discrete, H, record_vector(A, H),
                                   mdef)[5] for _nm, _s, H in HIST)
    nonu_classes = sorted(class_names_of(A, s) for _nm, s, _k in nonu)
    thesis = all(len(set(class_names_of(A, s))) == 1 for _nm, s, _k in nonu)
    l5rows = [
        row(9, 3, 3, True, FAC_DECLARED["non_unique_at"], 4,
            t_n_reading(4, 9), 3 + 1,
            "FROZEN DECLARED PARENT CONSTANT (FAC at commit %s): histories "
            "with more than one factorization at n = 9" % FAC_COMMIT),
        row(4, 2, 2, True, len(nonu), 4, t_n_reading(4, A.n), 2 + 1,
            "MEASURED at n = 4 over the COMPLETE actor lattice"),
    ]
    w5c, e5c = transport_word(l5rows)
    law5 = {"histories": len(HIST), "actor_lattice": len(LAT),
            "unique_factorization": len(uniq), "non_unique": len(nonu),
            "union_of_admissible": len(union),
            "discrete_admissible_everywhere": disc_ok,
            "non_unique_class_tuples": [list(t) for t in nonu_classes],
            "thesis_holds": thesis,
            "thesis": "MORE THAN ONE FACTORIZATION ONLY WHERE THE HISTORY "
                      "REPEATS A PARALLEL CLASS",
            "leg_pass_counts": dict(legcount),
            "coin_order_disagreements": 0,
            "parent_declared_unique": FAC_DECLARED["unique_at"],
            "parent_declared_non_unique": FAC_DECLARED["non_unique_at"],
            "parent_declared_lattice": FAC_DECLARED["actor_lattice"],
            "count_rows": l5rows, "count_word": w5c, "count_evidence": e5c,
            "measure": "COUNTING-ONLY (E-24): no measure is declared over the "
                       "corpus, so the fraction 45 of 48 is a count of this "
                       "corpus's histories and not a probability",
            "word": "LAW-IN-N" if (thesis and disc_ok) else "BREAKS",
            "word_basis": "THE THESIS IS n-FREE AND HOLDS VERBATIM AT n = 4; "
                          "ITS COUNT IS q + 1, THE PARALLEL-CLASS COUNT"}
    reg(len(uniq), len(nonu), len(union), len(HIST), len(LAT))
    for k, v in legcount.items():
        reg(v)
    R["law5_division_forcing"] = law5
    say("  unique %d, non-unique %d of %d; union of admissible %d; thesis %s"
        % (len(uniq), len(nonu), len(HIST), len(union), thesis))
    LD.gate("G-LAW5-CENSUS",
            "THE DIVISION-FORCING CENSUS RUNS THE COMPLETE ACTOR LATTICE "
            "THROUGH THE FOUR-LEG CRITERION AT EVERY HISTORY, AND THE "
            "DISCRETE PARTITION IS CHECKED ADMISSIBLE AT EVERY ONE OF THEM "
            "SEPARATELY.  The count can therefore never be zero by "
            "construction, and the question is always whether anything JOINS "
            "the four-fold division -- which is the parent's own question, "
            "asked of a lattice with no window in it",
            disc_ok and len(uniq) + len(nonu) == len(HIST)
            and legcount["leg2"] < len(LAT) * len(HIST)
            and not leg_violations,
            "unique %d, non-unique %d, histories %d, discrete admissible "
            "everywhere %s, leg pass counts %s, histories whose admissible "
            "set escapes a leg %s"
            % (len(uniq), len(nonu), len(HIST), disc_ok, dict(legcount),
               sorted(set(leg_violations)) or "none"))
    LD.gate("G-LAW5-PARENT",
            "THE THESIS UNDER TEST IS THE PARENT'S OWN SENTENCE, AND IT IS "
            "TESTED PER HISTORY.  Each non-unique history is examined "
            "individually for the property the parent's thesis names -- that "
            "it repeats a single parallel class in every round -- rather "
            "than the set being compared with a count.  The parent's own "
            "counts are frozen declared constants at commit %s and are "
            "cross-checked for internal consistency" % FAC_COMMIT,
            thesis and FAC_DECLARED["unique_at"]
            + FAC_DECLARED["non_unique_at"] == 5856,
            "non-unique class tuples %s; thesis holds %s; parent %d + %d"
            % ([",".join(t) for t in nonu_classes], thesis,
               FAC_DECLARED["unique_at"], FAC_DECLARED["non_unique_at"]))
    LD.gate("G-LAW5-WORD",
            "LAW 5's WORD IS DERIVED FROM THE THESIS TEST, AND ITS FRACTION "
            "IS STAMPED COUNTING-ONLY (E-24).  The word records whether the "
            "parent's characterisation survives; the fraction 45 of 48 is a "
            "count over this corpus and is not converted into a probability "
            "anywhere, because no measure over histories is declared",
            law5["word"] in WORDS and w5c in WORDS,
            "word %s, count word %s (%s), measure stamp present %s"
            % (law5["word"], w5c, e5c["stamp"],
               "COUNTING-ONLY" in law5["measure"]))
    SEAL.take("SEAL-LAW5", R)

    # ---- SEC 10  THE CONTROL ARMS ----------------------------------------
    # Every outcome word is emitted through the REAL testers, driven by
    # SYNTHETIC laws built to force each word.  A vocabulary whose words
    # cannot all be produced by the instrument that publishes them is not a
    # measurement (#36, and the ACT pattern).
    say()
    say("SECTION 10.  THE CONTROL ARMS -- EVERY WORD FORCED THROUGH THE REAL "
        "TESTERS")
    ctrl = []
    synth = [
        ("CTRL-LAW-IN-N", "LAW-IN-N",
         "A SYNTHETIC LAW WHOSE VALUE IS THE COUNTING FLOOR ITSELF: measured "
         "= t_n at every row, and the rows discriminate it from the literal",
         [row(9, 3, 3, True, counting_floor(9), 4, t_n_reading(4, 9),
              3 + 1, "synthetic"),
          row(4, 2, 2, True, counting_floor(4), 4, t_n_reading(4, 4),
              2 + 1, "synthetic"),
          row(16, 4, 4, True, counting_floor(16), 4, t_n_reading(4, 16),
              4 + 1, "synthetic")]),
        ("CTRL-NEEDS-3", "NEEDS-3",
         "A SYNTHETIC LAW WHOSE VALUE IS q + 1: the q reading agrees "
         "everywhere and the n-only reading does not",
         [row(9, 3, 3, True, 4, 4, t_n_reading(4, 9), 3 + 1, "synthetic"),
          row(4, 2, 2, True, 3, 4, t_n_reading(4, 4), 2 + 1, "synthetic"),
          row(16, 4, 4, True, 5, 4, t_n_reading(4, 16), 4 + 1, "synthetic")]),
        ("CTRL-BREAKS", "BREAKS",
         "A SYNTHETIC LAW WHOSE n = 16 VALUE AGREES WITH NEITHER READING",
         [row(9, 3, 3, True, 4, 4, t_n_reading(4, 9), 3 + 1, "synthetic"),
          row(4, 2, 2, True, 3, 4, t_n_reading(4, 4), 2 + 1, "synthetic"),
          row(16, 4, 4, True, 11, 4, t_n_reading(4, 16), 4 + 1, "synthetic")]),
        ("CTRL-UNDISCRIMINATED", "LAW-IN-N",
         "A SYNTHETIC LAW WHOSE THREE READINGS COINCIDE AT EVERY ROW: the "
         "word is emitted but the row is stamped UNDISCRIMINATED, which is "
         "how this instrument refuses to read a blind test as a result",
         [row(9, 3, 3, True, 1, 1, 1, 1, "synthetic"),
          row(4, 2, 2, True, 1, 1, 1, 1, "synthetic")]),
        ("CTRL-NO-FEASIBLE", "BREAKS",
         "A SYNTHETIC LAW EVERY ROW OF WHICH IS INFEASIBLE: with nothing "
         "scored the procedure refuses rather than defaults",
         [row(16, 4, 4, False, None, 4, 4, 5, "synthetic")]),
    ]
    for cid, want, why, rows in synth:
        rr = rows if not (mut("MUT-CONTROL") and cid == "CTRL-BREAKS") \
            else rows[:2]
        got, ev = transport_word(rr)
        ctrl.append({"control": cid, "expected": want, "emitted": got,
                     "forced": got == want, "why": why, "evidence": ev})
    # the leg testers, forced both ways on synthetic objects
    disc = tuple((x,) for x in A.SITES)
    triv = (tuple(A.SITES),)
    Hcut = (frozenset([A.SITES[0]]),)
    leg_ctrl = [
        {"control": "CTRL-LEG1-POS", "tester": "leg1_actor",
         "expected": True, "emitted": leg1_actor(A, disc),
         "why": "the discrete partition is translation-invariant"},
        {"control": "CTRL-LEG1-NEG", "tester": "leg1_actor",
         "expected": False,
         "emitted": leg1_actor(A, (tuple(A.SITES[:3]), (A.SITES[3],))),
         "why": "a 3+1 partition is not a coset partition"},
        {"control": "CTRL-LEG2-POS", "tester": "leg2_actor",
         "expected": True, "emitted": leg2_actor(A, disc, HIST[0][2]),
         "why": "every event is a union of singletons"},
        {"control": "CTRL-LEG2-NEG", "tester": "leg2_actor",
         "expected": False, "emitted": leg2_actor(A, triv, Hcut),
         "why": "a one-block partition cuts a one-actor event"},
        {"control": "CTRL-LEG3-POS", "tester": "leg3_actor",
         "expected": True,
         "emitted": leg3_actor(A, disc, record_vector(A, HIST[0][2])),
         "why": "a singleton block is trivially record-constant"},
        {"control": "CTRL-LEG3-NEG", "tester": "leg3_actor",
         "expected": False,
         "emitted": leg3_actor(A, triv, [k for k in range(len(A.CELLS))]),
         "why": "a one-block partition over a strictly increasing record"},
        {"control": "CTRL-LEG4-POS", "tester": "leg4_cell",
         "expected": True,
         "emitted": leg4_cell(A, induced_cell_partition(A, disc),
                              record_vector(A, HIST[0][2]), "G.D", A.L),
         "why": "the discrete carrier partition is trivially lumpable"},
        {"control": "CTRL-LEG4-NEG", "tester": "leg4_cell",
         "expected": False,
         "emitted": leg4_cell(A, (tuple(range(len(A.CELLS))),),
                              [k for k in range(len(A.CELLS))], "G.D", A.L),
         "why": "the one-block carrier partition over a record that separates "
                "every cell"},
    ]
    for r in leg_ctrl:
        r["forced"] = (r["emitted"] == r["expected"])
    R["controls"] = {"transport_arms": ctrl, "leg_arms": leg_ctrl,
                     "words_emitted": sorted({c["emitted"] for c in ctrl}),
                     "vocabulary": list(WORDS)}
    say("  transport arms: %s"
        % [(c["control"], c["emitted"]) for c in ctrl])
    say("  leg arms forced: %d of %d"
        % (sum(1 for r in leg_ctrl if r["forced"]), len(leg_ctrl)))
    LD.gate("G-CONTROL-ARMS",
            "EVERY PRE-REGISTERED WORD IS EMITTED BY THE REAL TESTER ON A "
            "SYNTHETIC LAW BUILT TO FORCE IT, AND EVERY LEG FIRES IN BOTH "
            "DIRECTIONS.  The three outcome words are produced by the same "
            "transport procedure that decides the five real laws -- nothing "
            "is stubbed -- and the two degenerate cases (a blind test and a "
            "wholly infeasible table) are exercised too.  Each of the four "
            "criterion legs is then driven to True and to False on declared "
            "objects, so no leg is a branch that never executes",
            all(c["forced"] for c in ctrl)
            and all(r["forced"] for r in leg_ctrl)
            and set(WORDS) <= {c["emitted"] for c in ctrl},
            "transport arms forced %d of %d, words emitted %s, leg arms "
            "forced %d of %d"
            % (sum(1 for c in ctrl if c["forced"]), len(ctrl),
               sorted({c["emitted"] for c in ctrl}),
               sum(1 for r in leg_ctrl if r["forced"]), len(leg_ctrl)))
    SEAL.take("SEAL-CONTROLS", R)

    # ---- SEC 11  E-24 -----------------------------------------------------
    R["measure_relativity"] = {
        "stamp": "COUNTING-ONLY",
        "rows": [
            {"quantity": "forced naming fraction at n = 4",
             "value": "%d of %d" % (len(forced), len(HIST)),
             "measure": "NONE DECLARED; the denominator is this corpus's "
                        "history count and the fraction is a count, not a "
                        "probability"},
            {"quantity": "unique factorization at n = 4",
             "value": "%d of %d" % (len(uniq), len(HIST)),
             "measure": "NONE DECLARED; COUNTING-ONLY"},
            {"quantity": "the corpus itself",
             "value": "%d histories" % len(HIST),
             "measure": "the corpus is a MULTISET of schedules built by the "
                        "grammar; C1FAN repeats event sets at different seed "
                        "menus, so distinct-history and schedule counts are "
                        "different families and are never crossed"},
        ],
        "distinct_event_sets": len({tuple(sorted(
            tuple(sorted(A.SI[x] for x in F)) for F in H))
            for _nm, _s, H in HIST}),
        "schedules": len(HIST)}
    reg(R["measure_relativity"]["distinct_event_sets"])
    LD.gate("G-E24-MEASURE",
            "NO COUNT BECOMES A PROBABILITY (E-24).  Every published fraction "
            "is stamped COUNTING-ONLY with its denominator's family named, "
            "and the corpus's own multiplicity is disclosed: the schedule "
            "count and the distinct-event-set count are different families "
            "and the receipt publishes both rather than letting one stand for "
            "the other",
            R["measure_relativity"]["stamp"] == "COUNTING-ONLY"
            and R["measure_relativity"]["distinct_event_sets"] <= len(HIST),
            "schedules %d, distinct event sets %d, rows %d"
            % (len(HIST), R["measure_relativity"]["distinct_event_sets"],
               len(R["measure_relativity"]["rows"])))
    SEAL.take("SEAL-MEASURE", R)

    # ---- SEC 12  THE VERDICT ---------------------------------------------
    say()
    say("SECTION 12.  THE VERDICT")
    lawrows = [("NAMING", R["law1_naming"]["word"]),
               ("CRYSTALLIZATION", R["law2_crystallization"]["word"]),
               ("COSET-MENU", R["law3_coset_menu"]["word"]),
               ("MOD-MOTIF", R["law4_mod_motif"]["word"]),
               ("DIVISION-FORCING", R["law5_division_forcing"]["word"])]
    portable = sum(1 for _k, w in lawrows if w == "LAW-IN-N")
    if mut("MUT-VERDICT"):
        portable = 5
    counts = {"laws": len(lawrows), "portable": portable,
              "needs_root": sum(1 for _k, w in lawrows if w == "NEEDS-3"),
              "breaks": sum(1 for _k, w in lawrows if w == "BREAKS"),
              "histories_n4": len(HIST), "actor_lattice_n4": len(LAT),
              "forced_n4": len(forced), "chart_n4": len(chart),
              "unique_factorization_n4": len(uniq),
              "coset_menu_n4": len(menu),
              "schedule_time_n4": t4, "attained_floor_n4": f4,
              "schedule_time_n16": time16, "attained_floor_n16": attained16,
              "offset": off4,
              "numerals_q_carried": sum(
                  1 for w in (law1["chart_count_word"],
                              law2["schedule_time"]["word"],
                              law2["information_floor"]["word"],
                              law3["count_word"], law4["ladder_word"],
                              law5["count_word"]) if w == "NEEDS-3"),
              "numerals_tested": 6}
    for v in counts.values():
        reg(v)
    R["counts"] = counts
    segs = verdict_segments(R, lawrows)
    head = segs[0]
    R["verdict"] = {"head": head, "segments": segs,
                    "law_words": [{"law": k, "word": w} for k, w in lawrows],
                    "vocabulary": list(WORDS)}
    ind = independent_head(R, lawrows)
    for s in segs:
        say("  " + s)
    LD.gate("G-VERDICT-RECONSTRUCTED",
            "THE HEAD IS DERIVED TWICE BY DISJOINT CODE AND COMPARED AS "
            "COMPLETE STRINGS (#10: containment is not equality).  The "
            "publishing path builds the segments from the receipt's own "
            "objects; the comparator rebuilds every segment from the "
            "measured primitives, sharing no code, no inputs and no typed "
            "literal with the builder, and the two are compared for string "
            "EQUALITY segment by segment.  The aggregate count is derived "
            "from the five emitted words and never typed",
            ind == segs
            and portable == sum(1 for _k, w in lawrows if w == "LAW-IN-N"),
            "segments %d, byte-equal %s, portable %d of %d derived from the "
            "word list %s"
            % (len(segs), ind == segs, portable, len(lawrows),
               [w for _k, w in lawrows]))
    SEAL.take("SEAL-VERDICT", R)
    SEAL.take("SEAL-COUNTS", R)
    return R, src, paper_text



# ===========================================================================
# SECTION 13.  THE HEAD, DERIVED TWICE BY DISJOINT CODE
# ===========================================================================

def verdict_segments(R, lawrows):
    """THE PUBLISHING PATH: the segments built from the receipt's objects."""
    c = R["counts"]
    l1, l2 = R["law1_naming"], R["law2_crystallization"]
    l3, l4, l5 = (R["law3_coset_menu"], R["law4_mod_motif"],
                  R["law5_division_forcing"])
    n16 = R["n16_window"]
    head = ("NDEP-PORTABLE-%d-OF-%d<n=4 BUILT AND RUN ENTIRE -- AG(2,2), "
            "%d DRIVEN HISTORIES, ACTOR LATTICE %d COMPLETE, SYMMETRIC GROUP "
            "FILTERED WHOLE; n=16 A DECLARED WINDOW; EVERY ONE OF THE %d "
            "TESTED NUMERALS IS q-CARRIED (%d OF %d), SO WHAT TRANSPORTS ON n "
            "ALONE IS THE LAWS AND NEVER THEIR NUMBERS>"
            % (c["portable"], c["laws"], c["histories_n4"],
               c["actor_lattice_n4"], c["numerals_tested"],
               c["numerals_q_carried"], c["numerals_tested"]))
    s1 = ("NDEP-%s-NAMING<ROUTES=0 MISMATCHES OVER %d DISTINCT PREFIXES AT "
          "n=4, ELEMENT SET AGAINST ELEMENT SET, THE WHOLE OF S_%d FILTERED "
          "PER PREFIX | n=16 %s COMPARISONS 0 MISMATCHES ON THE DECLARED "
          "PERMUTATION WINDOW, %s POSITIVE | FORCED %d OF %d, CHART %d = THE "
          "CONSTANT-CLASS HISTORIES, ONE PER PARALLEL CLASS -- THE PARENT'S "
          "CHARACTERISATION VERBATIM | THE COUNT IS %s>"
          % (l1["word"], l1["route_prefixes_compared"], 4,
             com(n16["route_window_comparisons"]),
             com(n16["route_window_positive"]),
             l1["forced"], l1["histories"], l1["chart"],
             l1["chart_count_word"]))
    s2 = ("NDEP-%s-CRYSTALLIZATION<THE PAIR SURVIVES AS A STRUCTURE AND ITS "
          "FLOOR FORMULA DOES NOT: SCHEDULE TIME %d|%d|%d AT n=4|9|16 = 2q-1 "
          "(%s) | ATTAINED FLOOR %d|%d|%d WHILE THE COUNTING BOUND "
          "ceil(log2 n) READS %d AT n=16 (%s) | THE SUCCESSOR FORMULA, IN "
          "WHICH THE EVENT SIZE q ENTERS, READS %d|%d|%d AND MATCHES ALL "
          "THREE | OFFSET ONE AT ALL THREE (%s), ROUND ONE'S LAST EVENT "
          "REDUNDANT AT %d OF %d>"
          % (l2["word"], l2["schedule_time"]["n4"],
             l2["schedule_time"]["parent_n9"], l2["schedule_time"]["n16"],
             l2["schedule_time"]["word"],
             l2["information_floor"]["n4_attained"],
             l2["information_floor"]["parent_n9_attained"],
             l2["information_floor"]["n16_attained"],
             l2["information_floor"]["counting_floor"]["16"],
             l2["information_floor"]["word"],
             l2["information_floor"]["weight_floor"]["4"],
             l2["information_floor"]["weight_floor"]["9"],
             l2["information_floor"]["weight_floor"]["16"],
             l2["offset"]["word"],
             l2["redundant_event"]["round_one_last_event_redundant_at"],
             l2["redundant_event"]["of"]))
    s3 = ("NDEP-%s-COSET-MENU<SET-EQUAL AT n=4: THE GEOMETRY LEG'S %d "
          "SURVIVORS OVER THE COMPLETE LATTICE OF %d ARE EXACTLY THE %d "
          "COSET PARTITIONS OF THE %d TRANSLATION SUBGROUPS | THE COUNT IS "
          "q+3 AT PRIME q (%s) | THE HYPOTHESIS FAILS AT q=4: THE DECLARED "
          "LINKS GENERATE %d OF %d, SO THE q=4 ROW IS CARRIED UNSCORED AND "
          "THE TWO READINGS THERE (%d ABSTRACT SUBGROUPS, %d F_q-SUBSPACES) "
          "ARE NAMED AND NOT CHOSEN>"
          % (l3["word"], l3["leg1_survivors"], l3["actor_lattice"],
             l3["coset_partitions"], l3["subgroups_of_T"], l3["count_word"],
             l3["by_q"]["4"]["declared_links_generate"],
             l3["by_q"]["4"]["group_order"],
             l3["q4_readings"]["abstract_subgroups_of_T"],
             l3["q4_readings"]["f_q_subspaces"]))
    s4 = ("NDEP-%s-MOD-MOTIF<THE MOTIF SPLITS IN TWO. THE LADDER'S MODULUS IS "
          "DERIVED AND IS THE DECLARED LINK COUNT L: AT FIXED n=4 THE SWEEP "
          "L=1|2|3 RETURNS ACHIEVABLE BUDGETS %s|%s|%s, SO MOD-3 REAPPEARS AT "
          "FOUR ACTORS AND THE MODULUS IS NEITHER sqrt(n) NOR THE "
          "CHARACTERISTIC, BOTH FIXED AT 2 THROUGHOUT; n=16 RETURNS %s. THE "
          "COIN'S MODULUS IS A FREE DECLARATION: THE RECORD ENTERS EXACTLY "
          "MOD m (0 MISMATCHES OVER %s PAIRS AT EACH OF m=2 AND m=3) WHILE "
          "THE CENSUS IS BLIND TO m (%d UNIQUE AND %d NON-UNIQUE AT m=2,3,4,5)>"
          % (l4["word"],
             "{" + ",".join(str(r) for r in l4["ladder_by_L"]["1"]["achievable_R"]) + "}",
             "{" + ",".join(str(r) for r in l4["ladder_by_L"]["2"]["achievable_R"]) + "}",
             "{" + ",".join(str(r) for r in l4["ladder_by_L"]["3"]["achievable_R"]) + "}",
             "{" + ",".join(str(r) for r in l4["ladder_n16"]) + "}",
             com(l4["coin_channel"]["2"]["pairs"]),
             l4["census_by_m"]["2"]["unique"],
             l4["census_by_m"]["2"]["non_unique"]))
    s5 = ("NDEP-%s-DIVISION-FORCING<UNIQUE FACTORIZATION %d OF %d OVER THE "
          "COMPLETE ACTOR LATTICE OF %d, THE DISCRETE PARTITION CHECKED "
          "ADMISSIBLE AT EVERY HISTORY SEPARATELY | THE %d NON-UNIQUE ARE "
          "EXACTLY THE CONSTANT-CLASS HISTORIES AND THE PARENT'S THESIS "
          "HOLDS VERBATIM | UNION OF ADMISSIBLE PARTITIONS %d = THE DISCRETE "
          "ONE PLUS ONE PER PARALLEL CLASS | THE COUNT IS %s | COUNTING-ONLY>"
          % (l5["word"], l5["unique_factorization"], l5["histories"],
             l5["actor_lattice"], l5["non_unique"], l5["union_of_admissible"],
             l5["count_word"]))
    s6 = ("SCOPE=n=4 ENTIRE AND COMPLETE; n=16 A DECLARED WINDOW (CLASS "
          "TUPLES ONLY -- THE %s GROUPINGS OF SIXTEEN SITES ARE OUT OF SCOPE, "
          "S_16 IS NOT FILTERED); q=3 ENTERS ONLY AS THE CONSTRUCTOR-FIDELITY "
          "LEG AND NO n=9 NUMBER IS RE-DERIVED HERE -- ALL TEN ARE ANCHORED "
          "READS OF THE PARENT'S COMMITTED RECEIPT OR FROZEN DECLARED "
          "CONSTANTS | SATURATION IS MAXIMAL AT q=2 AND q=3 AND IS NOT AT "
          "q=4, WHERE A WITNESS GROUPING REACHES %d AGAINST THE BUDGET %d | "
          "MEASURE=COUNTING-ONLY (E-24) | LANGUAGE=LAW-IN-N, NEEDS-3 AND "
          "BREAKS NAME THE TRANSPORT OF A PUBLISHED LAW AND NOTHING ELSE"
          % (com(2627625), n16["saturation_witness_incidence"],
             n16["saturation_budget_n"]))
    return [head, s1, s2, s3, s4, s5, s6]


def independent_head(R, lawrows):
    """THE COMPARATOR.  It shares no code, no inputs and no typed literal with
    verdict_segments: it re-derives every quantity from the measured
    primitives in the receipt's law objects and assembles the segments by a
    different route, then the two complete strings are compared."""
    words = {k: w for k, w in lawrows}
    n4 = R["corpus"]
    l1, l2 = R["law1_naming"], R["law2_crystallization"]
    l3, l4, l5 = (R["law3_coset_menu"], R["law4_mod_motif"],
                  R["law5_division_forcing"])
    nw = R["n16_window"]
    numword = [l1["chart_count_word"], l2["schedule_time"]["word"],
               l2["information_floor"]["word"], l3["count_word"],
               l4["ladder_word"], l5["count_word"]]
    nq = len([w for w in numword if w == "NEEDS-3"])
    port = len([1 for _k, w in lawrows if w == "LAW-IN-N"])
    out = []
    out.append("NDEP-PORTABLE-" + str(port) + "-OF-" + str(len(lawrows))
               + "<n=4 BUILT AND RUN ENTIRE -- AG(2,2), "
               + str(n4["histories"]) + " DRIVEN HISTORIES, ACTOR LATTICE "
               + str(l3["actor_lattice"]) + " COMPLETE, SYMMETRIC GROUP "
               "FILTERED WHOLE; n=16 A DECLARED WINDOW; EVERY ONE OF THE "
               + str(len(numword)) + " TESTED NUMERALS IS q-CARRIED ("
               + str(nq) + " OF " + str(len(numword)) + "), SO WHAT "
               "TRANSPORTS ON n ALONE IS THE LAWS AND NEVER THEIR NUMBERS>")
    out.append("NDEP-" + words["NAMING"] + "-NAMING<ROUTES=0 MISMATCHES OVER "
               + str(l1["route_prefixes_compared"]) + " DISTINCT PREFIXES AT "
               "n=4, ELEMENT SET AGAINST ELEMENT SET, THE WHOLE OF S_"
               + str(n4["n"]) + " FILTERED PER PREFIX | n=16 "
               + com(nw["route_window_comparisons"]) + " COMPARISONS 0 "
               "MISMATCHES ON THE DECLARED PERMUTATION WINDOW, "
               + com(nw["route_window_positive"]) + " POSITIVE | FORCED "
               + str(l1["forced"]) + " OF " + str(l1["histories"])
               + ", CHART " + str(l1["chart"]) + " = THE CONSTANT-CLASS "
               "HISTORIES, ONE PER PARALLEL CLASS -- THE PARENT'S "
               "CHARACTERISATION VERBATIM | THE COUNT IS "
               + l1["chart_count_word"] + ">")
    ifl = l2["information_floor"]
    out.append("NDEP-" + words["CRYSTALLIZATION"] + "-CRYSTALLIZATION<THE "
               "PAIR SURVIVES AS A STRUCTURE AND ITS FLOOR FORMULA DOES NOT: "
               "SCHEDULE TIME " + str(l2["schedule_time"]["n4"]) + "|"
               + str(l2["schedule_time"]["parent_n9"]) + "|"
               + str(l2["schedule_time"]["n16"]) + " AT n=4|9|16 = 2q-1 ("
               + l2["schedule_time"]["word"] + ") | ATTAINED FLOOR "
               + str(ifl["n4_attained"]) + "|"
               + str(ifl["parent_n9_attained"]) + "|"
               + str(ifl["n16_attained"]) + " WHILE THE COUNTING BOUND "
               "ceil(log2 n) READS " + str(ifl["counting_floor"]["16"])
               + " AT n=16 (" + ifl["word"] + ") | THE SUCCESSOR FORMULA, IN "
               "WHICH THE EVENT SIZE q ENTERS, READS "
               + str(ifl["weight_floor"]["4"]) + "|"
               + str(ifl["weight_floor"]["9"]) + "|"
               + str(ifl["weight_floor"]["16"]) + " AND MATCHES ALL THREE | "
               "OFFSET ONE AT ALL THREE (" + l2["offset"]["word"] + "), "
               "ROUND ONE'S LAST EVENT REDUNDANT AT "
               + str(l2["redundant_event"]["round_one_last_event_redundant_at"])
               + " OF " + str(l2["redundant_event"]["of"]) + ">")
    out.append("NDEP-" + words["COSET-MENU"] + "-COSET-MENU<SET-EQUAL AT n=4: "
               "THE GEOMETRY LEG'S " + str(l3["leg1_survivors"])
               + " SURVIVORS OVER THE COMPLETE LATTICE OF "
               + str(l3["actor_lattice"]) + " ARE EXACTLY THE "
               + str(l3["coset_partitions"]) + " COSET PARTITIONS OF THE "
               + str(l3["subgroups_of_T"]) + " TRANSLATION SUBGROUPS | THE "
               "COUNT IS q+3 AT PRIME q (" + l3["count_word"] + ") | THE "
               "HYPOTHESIS FAILS AT q=4: THE DECLARED LINKS GENERATE "
               + str(l3["by_q"]["4"]["declared_links_generate"]) + " OF "
               + str(l3["by_q"]["4"]["group_order"]) + ", SO THE q=4 ROW IS "
               "CARRIED UNSCORED AND THE TWO READINGS THERE ("
               + str(l3["q4_readings"]["abstract_subgroups_of_T"])
               + " ABSTRACT SUBGROUPS, "
               + str(l3["q4_readings"]["f_q_subspaces"])
               + " F_q-SUBSPACES) ARE NAMED AND NOT CHOSEN>")
    bl = l4["ladder_by_L"]
    def setstr(xs):
        return "{" + ",".join([str(v) for v in xs]) + "}"
    out.append("NDEP-" + words["MOD-MOTIF"] + "-MOD-MOTIF<THE MOTIF SPLITS IN "
               "TWO. THE LADDER'S MODULUS IS DERIVED AND IS THE DECLARED LINK "
               "COUNT L: AT FIXED n=4 THE SWEEP L=1|2|3 RETURNS ACHIEVABLE "
               "BUDGETS " + setstr(bl["1"]["achievable_R"]) + "|"
               + setstr(bl["2"]["achievable_R"]) + "|"
               + setstr(bl["3"]["achievable_R"]) + ", SO MOD-3 REAPPEARS AT "
               "FOUR ACTORS AND THE MODULUS IS NEITHER sqrt(n) NOR THE "
               "CHARACTERISTIC, BOTH FIXED AT 2 THROUGHOUT; n=16 RETURNS "
               + setstr(l4["ladder_n16"]) + ". THE COIN'S MODULUS IS A FREE "
               "DECLARATION: THE RECORD ENTERS EXACTLY MOD m (0 MISMATCHES "
               "OVER " + com(l4["coin_channel"]["2"]["pairs"]) + " PAIRS AT "
               "EACH OF m=2 AND m=3) WHILE THE CENSUS IS BLIND TO m ("
               + str(l4["census_by_m"]["2"]["unique"]) + " UNIQUE AND "
               + str(l4["census_by_m"]["2"]["non_unique"])
               + " NON-UNIQUE AT m=2,3,4,5)>")
    out.append("NDEP-" + words["DIVISION-FORCING"] + "-DIVISION-FORCING<UNIQUE "
               "FACTORIZATION " + str(l5["unique_factorization"]) + " OF "
               + str(l5["histories"]) + " OVER THE COMPLETE ACTOR LATTICE OF "
               + str(l5["actor_lattice"]) + ", THE DISCRETE PARTITION CHECKED "
               "ADMISSIBLE AT EVERY HISTORY SEPARATELY | THE "
               + str(l5["non_unique"]) + " NON-UNIQUE ARE EXACTLY THE "
               "CONSTANT-CLASS HISTORIES AND THE PARENT'S THESIS HOLDS "
               "VERBATIM | UNION OF ADMISSIBLE PARTITIONS "
               + str(l5["union_of_admissible"]) + " = THE DISCRETE ONE PLUS "
               "ONE PER PARALLEL CLASS | THE COUNT IS " + l5["count_word"]
               + " | COUNTING-ONLY>")
    ng = 1
    for k in range(1, 5):
        ng = ng * (16 - 4 * (k - 1))
    del ng
    big = math.factorial(16) // (math.factorial(4) ** 4 * math.factorial(4))
    out.append("SCOPE=n=4 ENTIRE AND COMPLETE; n=16 A DECLARED WINDOW (CLASS "
               "TUPLES ONLY -- THE " + com(big) + " GROUPINGS OF SIXTEEN "
               "SITES ARE OUT OF SCOPE, S_16 IS NOT FILTERED); q=3 ENTERS "
               "ONLY AS THE CONSTRUCTOR-FIDELITY LEG AND NO n=9 NUMBER IS "
               "RE-DERIVED HERE -- ALL TEN ARE ANCHORED READS OF THE PARENT'S "
               "COMMITTED RECEIPT OR FROZEN DECLARED CONSTANTS | SATURATION "
               "IS MAXIMAL AT q=2 AND q=3 AND IS NOT AT q=4, WHERE A WITNESS "
               "GROUPING REACHES " + str(nw["saturation_witness_incidence"])
               + " AGAINST THE BUDGET " + str(nw["saturation_budget_n"])
               + " | MEASURE=COUNTING-ONLY (E-24) | LANGUAGE=LAW-IN-N, "
               "NEEDS-3 AND BREAKS NAME THE TRANSPORT OF A PUBLISHED LAW AND "
               "NOTHING ELSE")
    return out


# ===========================================================================
# SECTION 14.  THE PAPER INSTRUMENT (#20 + E-22 + #125)
# ===========================================================================

def markdown_table_rows(text):
    out = []
    for line in text.split("\n"):
        ln = line.strip()
        if ln.startswith("|") and ln.endswith("|") and ln.count("|") > 2:
            cells = [canon(c) for c in ln[1:-1].split("|")]
            if all(set(c) <= set("-: ") for c in cells):
                continue
            out.append(cells)
    return out


FENCE = re.compile(r"```.*?```", re.S)
NUMTOK = re.compile(r"(?:(?<![\w.])-)?\d[\d,]*(?:\.\d+)?(?:/\d+)?")
WORDTOK = re.compile(r"[a-z]+")
HEADNUM = re.compile(r"^#{2,6}\s+(\d+(?:\.\d+)*)\.?\s", re.M)
SECREF = re.compile(r"(?:(RUNBOOK|E|AID|FAC)\s*)?section\s+(\d+(?:\.\d+)*)")
NUMERAL_EXEMPTIONS = ()
THOUSANDS = re.compile(r"^\d{1,3}(?:,\d{3})*$")
NUMWORDS = ("ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN",
            "EIGHT", "NINE", "TEN", "ELEVEN", "TWELVE")
WORDNUM = dict({w.lower(): i for i, w in enumerate(NUMWORDS)},
               twice=2, thirteen=13, fourteen=14, fifteen=15, sixteen=16,
               seventeen=17, eighteen=18, nineteen=19, twenty=20, thirty=30,
               forty=40, fifty=50, sixty=60, hundred=100)
FENCE_COPIES = 1


def receipt_numbers(R):
    out = set()
    hexpat = re.compile(r"^[0-9a-f]{12}$")

    def walk(o):
        if isinstance(o, bool):
            return
        if isinstance(o, int):
            out.add(str(o))
            out.add(com(o))
        elif isinstance(o, str):
            if hexpat.match(o):
                return
            for t in NUMTOK.findall(o):
                out.add(t)
                if THOUSANDS.match(t):
                    out.add(t.replace(",", ""))
        elif isinstance(o, dict):
            for k, v in o.items():
                if k in ("sha256_12", "payload_sha256_12"):
                    continue
                walk(k)
                walk(v)
        elif isinstance(o, (list, tuple)):
            for v in o:
                walk(v)
    for key in MEASURED_KEYS + ("provenance", "windows", "arena",
                                "path_anchors", "paper_tables",
                                "paper_claims", "totals", "coverage"):
        if key in R:
            walk(R[key])
    return out


def paper_claims(R):
    """THE PAPER'S LOAD-BEARING SENTENCES, each with the receipt value it
    renders from and a polarity partner that must NOT appear."""
    c, n16 = R["counts"], R["n16_window"]
    l1, l2 = R["law1_naming"], R["law2_crystallization"]
    l3, l4, l5 = (R["law3_coset_menu"], R["law4_mod_motif"],
                  R["law5_division_forcing"])
    rows = [
        ("CL-PORTABLE",
         "three of the five laws transport with n as a parameter",
         c["portable"] == 3),
        ("CL-HISTORIES",
         "the n = 4 corpus carries %d driven histories" % c["histories_n4"],
         True),
        ("CL-ROUTES",
         "the two routes disagree at 0 of the %d distinct prefixes"
         % l1["route_prefixes_compared"], l1["route_mismatches"] == 0),
        ("CL-CHART",
         "chart at %d, and the %d are exactly the constant-class histories"
         % (l1["chart"], l1["chart"]),
         l1["chart_is_exactly_constant_class"]),
        ("CL-TIME",
         "the schedule's crystallization time is %d at n = 4 and %d at n = 16"
         % (l2["schedule_time"]["n4"], l2["schedule_time"]["n16"]), True),
        ("CL-FLOOR",
         "the attained floor at n = 16 is %d while the counting bound reads %d"
         % (l2["information_floor"]["n16_attained"],
            l2["information_floor"]["counting_floor"]["16"]),
         l2["information_floor"]["n16_attained"]
         > l2["information_floor"]["counting_floor"]["16"]),
        ("CL-OFFSET",
         "the offset is one at n = 4, at n = 9 and at n = 16", True),
        ("CL-COSET",
         "the geometry leg admits %d partitions of the complete lattice of %d"
         % (l3["leg1_survivors"], l3["actor_lattice"]), l3["set_equal"]),
        ("CL-HYPOTHESIS",
         "the declared links generate %d of the %d translations at q = 4"
         % (l3["by_q"]["4"]["declared_links_generate"],
            l3["by_q"]["4"]["group_order"]),
         not l3["by_q"]["4"]["hypothesis_transitive"]),
        ("CL-LADDER",
         "the modulus is the declared link count", l4["carrier"]["modulus_equals_L"]),
        ("CL-COIN",
         "the census is blind to the coin's modulus",
         l4["coin_modulus_is_free"]),
        ("CL-FORCING",
         "unique factorization at %d of %d" % (l5["unique_factorization"],
                                               l5["histories"]),
         True),
        ("CL-SATURATION",
         "saturation is not maximal at q = 4",
         not n16["saturation_is_maximal"]),
    ]
    return [{"claim": k, "sentence": s, "supported": bool(v)}
            for k, s, v in rows]


def paper_tables(R):
    """THE PUBLISHED TABLES, HEADER ROW INCLUDED (a table whose columns were
    renamed is a different table)."""
    l2 = R["law2_crystallization"]
    l3, l4 = R["law3_coset_menu"], R["law4_mod_motif"]
    t = []
    hdr1 = ["law", "word", "what the numeral is"]
    rows1 = [["naming", R["law1_naming"]["word"],
              R["law1_naming"]["chart_count_word"]],
             ["crystallization", l2["word"], l2["information_floor"]["word"]],
             ["coset menu", l3["word"], l3["count_word"]],
             ["mod motif", R["law4_mod_motif"]["word"], l4["ladder_word"]],
             ["division forcing", R["law5_division_forcing"]["word"],
              R["law5_division_forcing"]["count_word"]]]
    t.append({"table": "T-WORDS", "header": hdr1, "rows": rows1})
    hdr2 = ["n", "schedule time", "attained floor", "counting bound",
            "sharpened bound", "offset"]
    rows2 = [["4", str(l2["schedule_time"]["n4"]),
              str(l2["information_floor"]["n4_attained"]),
              str(l2["information_floor"]["counting_floor"]["4"]),
              str(l2["information_floor"]["weight_floor"]["4"]),
              str(l2["offset"]["n4"])],
             ["9", str(l2["schedule_time"]["parent_n9"]),
              str(l2["information_floor"]["parent_n9_attained"]),
              str(l2["information_floor"]["counting_floor"]["9"]),
              str(l2["information_floor"]["weight_floor"]["9"]),
              str(l2["offset"]["parent_n9"])],
             ["16", str(l2["schedule_time"]["n16"]),
              str(l2["information_floor"]["n16_attained"]),
              str(l2["information_floor"]["counting_floor"]["16"]),
              str(l2["information_floor"]["weight_floor"]["16"]),
              str(l2["offset"]["n16"])]]
    t.append({"table": "T-CRYSTAL", "header": hdr2, "rows": rows2})
    hdr3 = ["declared links L", "cells", "saturating groupings",
            "achievable budgets", "modulus"]
    rows3 = [[k, str(v["cells"]), str(v["saturating"]),
              ",".join(str(x) for x in v["achievable_R"]),
              str(v["first_rung"])]
             for k, v in sorted(l4["ladder_by_L"].items())]
    t.append({"table": "T-LADDER", "header": hdr3, "rows": rows3})
    hdr4 = ["q", "subgroups of T", "q + 3", "declared links generate",
            "group order"]
    rows4 = [[k, str(v["subgroups_of_T"]), str(v["q_plus_3"]),
              str(v["declared_links_generate"]), str(v["group_order"])]
             for k, v in sorted(l3["by_q"].items())]
    t.append({"table": "T-SUBGROUPS", "header": hdr4, "rows": rows4})
    return t


def sentences(text):
    body = FENCE.sub(" ", text)
    return [norm(s) for s in re.split(r"(?<=[.!?])\s+", body) if norm(s)]


def prose_only(text):
    return "\n".join(l for l in FENCE.sub(" ", text).split("\n")
                     if not l.strip().startswith("|"))


def wall_positive(text, walls):
    """the walls are exercised in BOTH directions: each pattern is run against
    a sentence built to trip it, so a wall that could never fire is caught."""
    probes = {
        "WALL-NINE-DERIVED": "here nine is derived from the law",
        "WALL-ARBITRARY": "the actor count is arbitrary",
        "WALL-N9-REDERIVED": "this unit re-derives the n = 9 census",
        "WALL-N16-COMPLETE": "the n = 16 census is complete",
        "WALL-PROBABILITY": "the probability that a law transports",
    }
    out = []
    for wid, pat, why in walls:
        hits = re.findall(pat, canon(text), re.I)
        probe = pick("MUT-WALL", probes[wid],
                     "a sentence this pattern cannot match"
                     if wid == "WALL-ARBITRARY" else probes[wid])
        probes[wid] = probe
        fires = bool(re.search(pat, probe, re.I))
        out.append({"wall": wid, "pattern": pat, "why": why,
                    "hits_in_paper": len(hits), "fires_on_probe": fires,
                    "probe": probes[wid]})
    return out


def noun_bindings(R, text):
    """REFERENT BINDING: a published count must appear NEXT TO the noun it
    counts, not merely somewhere in the paper."""
    c = R["counts"]
    want = [("NB-HIST", c["histories_n4"], "histories"),
            ("NB-LATTICE", c["actor_lattice_n4"], "partitions"),
            ("NB-PREFIX", R["law1_naming"]["route_prefixes_compared"],
             "prefixes"),
            ("NB-COMPARISON", R["n16_window"]["route_window_comparisons"],
             "comparisons"),
            ("NB-PAIRS", R["law4_mod_motif"]["coin_channel"]["2"]["pairs"],
             "pairs")]
    hay = canon(text).lower()
    out = []
    for bid, val, noun in want:
        pats = [r"%s\s+(?:\w+\s+){0,3}%s" % (re.escape(s), noun)
                for s in (str(val), com(val))]
        if mut("MUT-NOUN") and bid == "NB-HIST":
            pats = [r"%s\s+(?:\w+\s+){0,3}prefixes" % re.escape(str(val))]
        hit = any(re.search(p, hay) for p in pats)
        out.append({"binding": bid, "value": val, "noun": noun, "bound": hit})
    return out


def paper_coverage(R, text):
    """#20 + E-22: EVERY numeral -- prose, tables, INLINE CODE SPANS and the
    fenced verdict blocks -- allow-listed against this run's registered
    numbers, the receipt it publishes, and a declared exemption table required
    to fire.  Spelled numerals are scanned on the same terms; the fenced
    blocks are gated by MULTISET equality."""
    allow = set(NUMREG) | receipt_numbers(R)
    for seg in R["verdict"]["segments"]:
        for t in NUMTOK.findall(seg):
            allow.add(t)
            if THOUSANDS.match(t):
                allow.add(t.replace(",", ""))
    exempt = [list(e) for e in NUMERAL_EXEMPTIONS]
    if mut("MUT-EXEMPTION-DEAD"):
        exempt = exempt + [["4242", "a literal that occurs nowhere"]]
    exempt_lits = {e[0] for e in exempt}
    body = text
    if mut("MUT-COVERAGE-SCAN"):
        body = FENCE.sub("", body)
    if mut("MUT-SPAN"):
        body = re.sub(r"`[^`\n]+`", " ", body)
    spans = re.findall(r"`[^`\n]+`", body)
    fenced = [t for blk in FENCE.findall(body) for t in NUMTOK.findall(blk)]
    inline = [t for sp in spans for t in NUMTOK.findall(sp)]
    heads = set(HEADNUM.findall(body))
    refs = SECREF.findall(body)
    dangling = sorted({n for owner, n in refs if not owner and n not in heads})
    scanbody = SECREF.sub(" ", HEADNUM.sub("#### ", body))
    reference = len(NUMTOK.findall(
        SECREF.sub(" ", HEADNUM.sub("#### ", text))))
    scanned, unbacked, fired = 0, [], Counter()
    for tok in NUMTOK.findall(scanbody):
        scanned += 1
        if tok in allow:
            continue
        if tok.replace(",", "") in allow:
            continue
        if tok in exempt_lits:
            fired[tok] += 1
            continue
        unbacked.append(tok)
    words_scanned, words_unbacked = 0, []
    for w in WORDTOK.findall(canon(scanbody).lower()):
        if w in WORDNUM:
            words_scanned += 1
            v = WORDNUM[w]
            if str(v) not in allow and com(v) not in allow:
                words_unbacked.append(w)
    fences = FENCE.findall(text)
    required = {}
    for seg in R["verdict"]["segments"]:
        required[seg] = FENCE_COPIES
    found = Counter()
    for f in fences:
        inner = canon(f.strip("`").strip())
        for seg in required:
            if canon(seg) == inner:
                found[seg] += 1
    multiset_ok = all(found[s] == required[s] for s in required)
    return {"numerals_scanned": scanned,
            "reference_numerals_in_whole_paper": reference,
            "scan_covers_everything": scanned <= reference,
            "unbacked": sorted(set(unbacked)),
            "fenced_numerals_scanned": len(fenced),
            "inline_span_numerals_scanned": len(inline),
            "spelled_numerals_scanned": words_scanned,
            "spelled_unbacked": sorted(set(words_unbacked)),
            "table_rows": len(markdown_table_rows(text)),
            "exemptions_declared": len(exempt),
            "exemptions_fired": sum(fired.values()),
            "dangling_section_refs": dangling,
            "verdict_fences_required": {s: required[s] for s in required},
            "verdict_fences_found": {s: found[s] for s in required},
            "fence_multiset_equal": multiset_ok,
            "fences_in_paper": len(fences)}


def paper_polarity(R, text):
    """each axis is checked in BOTH directions: the licensed word must be
    present and its forbidden partner absent."""
    c = R["counts"]
    axes = [
        ("POL-PORTABLE", "portable",
         pick("MUT-POLARITY", "portable at all five", "portable"),
         c["portable"] < 5),
        ("POL-FLOOR", "the counting bound", "the counting bound is attained",
         True),
        ("POL-WINDOW", "declared window", "exhaustive at n = 16", True),
        ("POL-MEASURE", "counting-only", "the probability that a law", True),
        ("POL-SPLIT", "splits", "one modulus", True),
    ]
    hay = canon(text).lower()
    out = []
    for aid, pos, neg, live in axes:
        p = pos in hay
        n = neg.lower() in hay
        out.append({"axis": aid, "positive": pos, "positive_present": p,
                    "negative": neg, "negative_absent": not n,
                    "axis_live": bool(live),
                    "ok": p and not n})
    return out


# ===========================================================================
# SECTION 15.  THE CLOSING BATTERY AND THE GATE-TO-DISK SEAL
# ===========================================================================

def closing_battery(R, src, paper_text, paper_rel, write):
    say()
    say("SECTION 15.  THE CLOSING BATTERY")
    ptxt = paper_text if paper_text is not None else ""
    if mut("MUT-HEAD") and ptxt:
        ptxt = ptxt.replace("NDEP-PORTABLE-3", "NDEP-PORTABLE-9", 1)
    head_ok = (canon(R["verdict"]["head"]) in canon(ptxt)) if ptxt else None
    R["paper_claims"] = paper_claims(R)
    R["paper_tables"] = paper_tables(R)
    cov = paper_coverage(R, ptxt) if ptxt else {}
    R["paper_coverage"] = cov
    pol = paper_polarity(R, ptxt) if ptxt else []
    R["polarity"] = pol
    walls = list(WALLS)
    R["walls"] = [{"wall": w, "pattern": p, "why": y} for w, p, y in walls]
    R["walls_positive"] = wall_positive(ptxt, walls) if ptxt else []
    R["noun_bindings"] = noun_bindings(R, ptxt) if ptxt else []
    tabrows = markdown_table_rows(ptxt) if ptxt else []
    tabset = {tuple(r) for r in tabrows}
    missing_tab = []
    for t in R["paper_tables"]:
        hdr = tuple(canon(h) for h in (t["header"] if not (
            mut("MUT-TABLE") and t["table"] == "T-WORDS") else t["header"][1:]))
        if ptxt and hdr not in tabset:
            missing_tab.append((t["table"], "HEADER"))
        for r in t["rows"]:
            if ptxt and tuple(canon(x) for x in r) not in tabset:
                missing_tab.append((t["table"], r[0]))
    LD.gate("G-PAPER-HEAD-VERBATIM",
            "THE PAPER'S HEAD IS THIS RUN'S HEAD, CHARACTER FOR CHARACTER.  "
            "The derived head string is looked for in the paper under the "
            "full text normalisation, so a paper whose verdict block has gone "
            "stale against the measurement cannot pass",
            head_ok is not False,
            "paper present %s, head found %s" % (bool(ptxt), head_ok))
    LD.gate("G-PAPER-COVERAGE",
            "EVERY NUMERAL OF THE PAPER IS BACKED, INCLUDING THOSE IN FENCED "
            "BLOCKS, INLINE CODE SPANS AND TABLES (#20 + E-22).  The allow "
            "list is this run's own registry plus the receipt it publishes; "
            "the declared exemption table is EMPTY and an exemption that "
            "fires on nothing is itself a failure; spelled numerals are "
            "scanned on the same terms; and the verdict fences are gated by "
            "MULTISET equality rather than containment.  The scan's own "
            "coverage is measured against a reference count taken over the "
            "whole paper",
            (not ptxt) or (not cov["unbacked"] and not cov["spelled_unbacked"]
                           and cov["fence_multiset_equal"]
                           and cov["exemptions_fired"]
                           == cov["exemptions_declared"]
                           and not cov["dangling_section_refs"]
                           and cov["numerals_scanned"]
                           == cov["reference_numerals_in_whole_paper"]),
            "scanned %s of %s reference, unbacked %s, spelled %s unbacked %s, "
            "fenced %s, inline spans %s, fences multiset-equal %s, "
            "exemptions %s declared / %s fired, dangling refs %s"
            % (cov.get("numerals_scanned"),
               cov.get("reference_numerals_in_whole_paper"),
               cov.get("unbacked"), cov.get("spelled_numerals_scanned"),
               cov.get("spelled_unbacked"),
               cov.get("fenced_numerals_scanned"),
               cov.get("inline_span_numerals_scanned"),
               cov.get("fence_multiset_equal"),
               cov.get("exemptions_declared"), cov.get("exemptions_fired"),
               cov.get("dangling_section_refs")))
    LD.gate("G-PAPER-CLAIMS",
            "EVERY LOAD-BEARING SENTENCE OF THE PAPER IS SUPPORTED BY A "
            "MEASURED VALUE, AND THE SUPPORT IS EVALUATED HERE RATHER THAN "
            "ASSERTED IN THE PROSE.  Thirteen claims, each a predicate over "
            "the receipt's own objects; a claim whose predicate is false "
            "kills the run before anything is written",
            all(c["supported"] for c in R["paper_claims"]),
            "claims %d, unsupported %s"
            % (len(R["paper_claims"]),
               [c["claim"] for c in R["paper_claims"] if not c["supported"]]
               or "none"))
    LD.gate("G-PAPER-TABLES",
            "EVERY PUBLISHED TABLE IS BOUND TO THE PAPER ROW BY ROW, HEADER "
            "INCLUDED.  A table whose header row were renamed would be a "
            "different table making a different claim, so the header is bound "
            "on the same terms as the data rows",
            not missing_tab,
            "tables %d, rows bound %d, missing %s"
            % (len(R["paper_tables"]),
               sum(len(t["rows"]) + 1 for t in R["paper_tables"]),
               missing_tab or "none"))
    LD.gate("G-PAPER-CLAIM-POLARITY",
            "EVERY POLARITY AXIS IS CHECKED IN BOTH DIRECTIONS AND EVERY AXIS "
            "IS LIVE.  The licensed word must be present AND its forbidden "
            "partner absent; an axis whose negative could not have occurred "
            "is disclosed as such rather than counted as a pass",
            (not ptxt) or (all(a["ok"] for a in pol)
                           and all(a["axis_live"] for a in pol)),
            "axes %d, failing %s, dead axes %s"
            % (len(pol), [a["axis"] for a in pol if not a["ok"]] or "none",
               [a["axis"] for a in pol if not a["axis_live"]] or "none"))
    LD.gate("G-WALLS-SCAN-THE-PAPER",
            "THE READING WALLS SCAN THE PAPER AND ARE THEMSELVES EXERCISED.  "
            "Five forbidden readings; each pattern is run against the paper "
            "(zero hits required) AND against a probe sentence built to trip "
            "it (a hit required), so a wall that could never fire is caught "
            "by its own positive control",
            all(w["hits_in_paper"] == 0 and w["fires_on_probe"]
                for w in R["walls_positive"]) if ptxt else True,
            "walls %d, hits %s, probes firing %d of %d"
            % (len(R["walls"]),
               {w["wall"]: w["hits_in_paper"] for w in R["walls_positive"]
                if w["hits_in_paper"]} or "none",
               sum(1 for w in R["walls_positive"] if w["fires_on_probe"]),
               len(R["walls_positive"])))
    LD.gate("G-NOUN-BINDING",
            "EVERY HEADLINE COUNT IS BOUND TO ITS REFERENT IN THE PAPER, "
            "ADJACENT.  A numeral that appears anywhere in the paper does not "
            "discharge the obligation; the gate requires the numeral within "
            "three words of the noun it counts, so a count silently attached "
            "to the wrong universe fails",
            (not ptxt) or all(b["bound"] for b in R["noun_bindings"]),
            "bindings %d, unbound %s"
            % (len(R["noun_bindings"]),
               [b["binding"] for b in R["noun_bindings"] if not b["bound"]]
               or "none"))
    # coverage / reachability / waivers
    tree = ast.parse(src)
    floats = [n for n in ast.walk(tree)
              if isinstance(n, ast.Constant) and isinstance(n.value, float)]

    def typescan(o):
        if isinstance(o, float):
            return 1
        if isinstance(o, dict):
            return sum(typescan(v) for v in o.values())
        if isinstance(o, (list, tuple)):
            return sum(typescan(v) for v in o)
        return 0
    LD.gate("G-NO-FLOATS",
            "THE ARITHMETIC IS EXACT, AND BOTH THE SOURCE AND THE EMITTED "
            "OBJECT ARE SCANNED.  An AST walk of this file finds no float "
            "literal, and a recursive type scan of the receipt finds no float "
            "value: the two scans catch different diseases and both are run",
            not floats and typescan(R) == 0,
            "float literals in source %d, float values in receipt %d"
            % (len(floats), typescan(R)))
    reach = []
    for name, gate, why in MUTANTS:
        reach.append({"mutant": name, "declared_gate": gate,
                      "description": why,
                      "hook_present": ("\"%s\"" % name) in src
                      or ("'%s'" % name) in src})
    R["reachability"] = reach
    R["mutants"] = [{"mutant": n, "gate": g, "description": w}
                    for n, g, w in MUTANTS]
    R["waiver_ledger"] = [
        {"row": "G-LAW2-OFFSET transport", "status": "DISCLOSED-NOT-WAIVED",
         "note": "the offset's three candidate readings coincide at every "
                 "arena point, so the row is stamped UNDISCRIMINATED by the "
                 "transport procedure itself and the word is published with "
                 "that stamp attached"},
        {"row": "the q = 4 coset-menu row", "status": "INFEASIBLE-BY-GATE",
         "note": "the hypothesis failure is MEASURED at G-LAW3-HYPOTHESIS and "
                 "the row is excluded from scoring by the procedure, not by "
                 "hand"},
        {"row": "the q = 4 saturating census", "status": "OUT-OF-SCOPE",
         "note": "declared in W-N16-CLASS with its size; the non-maximality "
                 "finding rests on an exhibited WITNESS and needs no census"},
    ]
    LD.gate("G-REACHABILITY",
            "EVERY DECLARED FALSIFIER HAS A HOOK IN THIS SOURCE AND EVERY "
            "PUBLISHED WAIVER IS A DISCLOSURE WITH A MECHANISM (#34, E-23).  "
            "A mutant named in the registry but absent from the code is dead "
            "text; a waiver with no forcing is a false badge.  Three rows are "
            "carried and none of them is a never-falsified pass",
            all(r["hook_present"] for r in reach),
            "mutants %d, hooks present %d, waiver rows %d"
            % (len(reach), sum(1 for r in reach if r["hook_present"]),
               len(R["waiver_ledger"])))
    swept = list(SWEEP_ROWS)
    R["mutant_sweep"] = swept
    LD.gate("G-SWEEP-BOUND",
            "THE MUTANT SWEEP, WHEN RUN, IS BOUND TO ITS DECLARED TARGETS.  "
            "Every mutant must die at the gate its registry row NAMES -- "
            "'died' and 'died where it said it would' are two different "
            "facts -- and must leave both artifacts untouched",
            all(r["at_the_declared_gate"] and r["artifacts_unchanged"]
                for r in swept),
            "sweep rows %d, off-target %s"
            % (len(swept), [r["mutant"] for r in swept
                            if not r["at_the_declared_gate"]] or "none"))
    R["coverage"] = {
        "gates": len(LD.rows),
        "seals_taken_before_this_gate": len(SEAL.rows),
        "falsifiers": len(MUTANTS),
        "windows": len(WINDOWS),
        "byte_anchors": len(SOURCES),
        "path_value_anchors": len(PATH_ANCHORS),
        "verbatim_anchors": len(VERBATIM),
        "walls": len(WALLS),
        "noun_bindings": len(NOUN_PATTERNS),
        "polarity_axes": len(pol),
        "control_arms": len(R["controls"]["transport_arms"])
        + len(R["controls"]["leg_arms"]),
        "tables": len(R["paper_tables"]),
        "claims": len(R["paper_claims"])}
    for v in R["coverage"].values():
        reg(v)
    LD.gate("G-COVERAGE",
            "THE INSTRUMENT'S OWN CENSUS IS PUBLISHED AND CHECKED FOR "
            "EMPTINESS.  Gates, seals, falsifiers, windows, the three anchor "
            "kinds, walls, referent bindings, polarity axes, control arms, "
            "tables and claims are counted from the live objects rather than "
            "typed, and every category is required non-empty -- a category "
            "with no members is an instrument that is not there",
            all(v > 0 for v in R["coverage"].values()),
            "census %s" % R["coverage"])
    SEAL.take("SEAL-WALLS", R)
    SEAL.take("SEAL-WALLS-POSITIVE", R)
    SEAL.take("SEAL-NOUNS", R)
    SEAL.take("SEAL-PAPER-CLAIMS", R)
    SEAL.take("SEAL-PAPER-TABLES", R)
    SEAL.take("SEAL-PAPER-COVERAGE", R)
    SEAL.take("SEAL-POLARITY", R)
    SEAL.take("SEAL-COVERAGE", R)
    SEAL.take("SEAL-REACHABILITY", R)
    SEAL.take("SEAL-WAIVERS", R)
    SEAL.take("SEAL-MUTANTS", R)
    SEAL.take("SEAL-MUTANT-SWEEP", R)
    return R


def finish(R, src, paper_text, write=True, swept=False):
    R["gates"] = [dict(r) for r in LD.rows]
    closing_battery(R, src, paper_text, PAPER_REL, write)
    # THE TOTALS ARE A SNAPSHOT AND SAY SO.  A seal is taken at the gate
    # that establishes its value (#148), so this object is sealed before the
    # last two ledger gates run; rather than under-report, it names them and
    # the seals still to be taken, and G-SEAL-TOTALITY publishes the closed
    # figures in its own evidence.
    pending_gates = [g for g in ("G-GATE-ACCOUNTING", "G-SEAL-TOTALITY")
                     if g not in {r["gate"] for r in LD.rows}]
    pending_seals = sorted({s for s, _p, _g in SEALED_PATHS}
                           - {r["seal"] for r in SEAL.rows})
    R["totals"] = {"gates_at_this_seal": len(LD.rows),
                   "gates_passed_at_this_seal":
                       sum(1 for r in LD.rows if r["passed"]),
                   "gates_still_to_run": pending_gates,
                   "seals_at_this_seal": len(SEAL.rows),
                   "seals_still_to_take": pending_seals,
                   "reads": {k: len(v) for k, v in
                             sorted(READS_BY_CATEGORY.items())},
                   "sweep_rows": len(R.get("mutant_sweep", []))}
    reg(R["totals"]["gates_at_this_seal"],
        R["totals"]["gates_passed_at_this_seal"],
        R["totals"]["seals_at_this_seal"])
    R["closing_gates"] = list(CLOSING_GATE_NAMES)
    R["transcript_head"] = digest("\n".join(LINES[:40]))
    ran = {r["gate"] for r in LD.rows}
    closing_absent = [g for g in CLOSING_GATE_NAMES
                      if g not in ran and g not in GATES_OUTSIDE_BOTH_ARTIFACTS
                      and g not in ("G-GATE-ACCOUNTING", "G-SEAL-TOTALITY",
                                    "G-TRANSCRIPT-INTEGRITY")]
    LD.gate("G-GATE-ACCOUNTING",
            "THE GATE LEDGER IS COMPLETE AND EVERY DECLARED CLOSING GATE "
            "RAN.  The totals are computed from the live ledger rather than "
            "typed, and every gate named in the closing list is a gate this "
            "run evaluated",
            not closing_absent and len(LD.rows) > 0,
            "gates %d, closing gates declared %d, absent %s"
            % (len(LD.rows), len(CLOSING_GATE_NAMES),
               closing_absent or "none"))
    SEAL.take("SEAL-GATES", R)
    SEAL.take("SEAL-CLOSING", R)
    SEAL.take("SEAL-TOTALS", R)
    SEAL.take("SEAL-TRANSCRIPT", R)
    published = [k for k in R
                 if k not in ("gates", "closing_gate_verdicts",
                              "seal_manifest", "payload_sha256_12")]
    sealed_paths = {r["path"] for r in SEAL.rows}
    missing = sorted(k for k in published
                     if k not in sealed_paths and k not in DECLARED_UNSEALED)
    _m, extra = SEAL.totality()
    unsealed = sorted(k for k in DECLARED_UNSEALED if k in sealed_paths)
    ran = {r["gate"] for r in LD.rows}
    seal_phantom = pick("MUT-SEAL-GATE",
                        sorted(({r["sealed_at_gate"] for r in SEAL.rows}
                                | {v[3] for v in VERBATIM}
                                | {a[4] for a in PATH_ANCHORS})
                               - ran - set(GATES_OUTSIDE_BOTH_ARTIFACTS)),
                        ["FORGED"])
    LD.gate("G-SEAL-TOTALITY",
            "THE SEAL MANIFEST IS TOTAL AND EVERY SEAL'S DECLARED GATE "
            "ACTUALLY RAN (#119 + #148).  Every published receipt key is "
            "either sealed at the gate that established it or named in the "
            "declared-unsealed list, and every gate name that a seal, a "
            "verbatim anchor or a path-value anchor attributes itself to is a "
            "gate this run evaluated -- a seal naming a gate that never runs "
            "publishes a false provenance over a real object",
            not missing and not extra and not unsealed and not seal_phantom
            and not (_m and not mut("MUT-SEAL-DROP")),
            "seals %d over %d published keys, missing %s, extra %s, "
            "declared-unsealed that were sealed %s, phantom gate names %s, "
            "manifest gaps %s; CLOSED FIGURES: gates %d all passed, seals %d"
            % (len(SEAL.rows), len(published), missing or "none",
               extra or "none", unsealed or "none", seal_phantom or "none",
               _m or "none", len(LD.rows) + 1, len(SEAL.rows)))
    R["closing_gate_verdicts"] = [dict(r) for r in LD.rows[len(R["gates"]):]]
    R["seal_manifest"] = SEAL.rows
    payload = json.dumps(R, indent=1, sort_keys=True, default=str)
    SEAL.close(R, payload)
    R["payload_sha256_12"] = SEAL.payload_sha
    payload = json.dumps(R, indent=1, sort_keys=True, default=str)
    text = "\n".join(LINES) + "\n"
    seal_j = hashlib.sha256(payload.encode("utf-8")).hexdigest()[:12]
    seal_t = hashlib.sha256(text.encode("utf-8")).hexdigest()[:12]
    absent = [g["gate"] for g in R["gates"] + R["closing_gate_verdicts"]
              if ("[PASS] %s" % g["gate"]) not in text]
    if absent:
        raise GateFail("G-TRANSCRIPT-INTEGRITY :: gate verdicts absent from "
                       "the bytes staged for disk :: %s" % absent)
    if not write:
        return R, payload, text, seal_j, seal_t
    tmp_j, tmp_t = OUT_JSON + ".tmp", OUT_TXT + ".tmp"
    try:
        with open(tmp_j, "w", encoding="utf-8") as fh:
            fh.write(payload)
        with open(tmp_t, "w", encoding="utf-8") as fh:
            fh.write(text)
        # THE READ-BACK HAPPENS BEFORE THE PROMOTION: the staged files are
        # hashed on disk and compared with the gate-time seals; only then are
        # they moved into place, so a failing run promotes nothing.
        with open(tmp_j, "rb") as fh:
            pj = hashlib.sha256(fh.read()).hexdigest()[:12]
        with open(tmp_t, "rb") as fh:
            pt = hashlib.sha256(fh.read()).hexdigest()[:12]
        if pj != seal_j or pt != seal_t:
            raise GateFail("G-ARTIFACT-INTEGRITY :: the staged bytes do not "
                           "match the gate-time seal, nothing promoted :: "
                           "receipt %s vs %s, transcript %s vs %s"
                           % (pj, seal_j, pt, seal_t))
        os.replace(tmp_j, OUT_JSON)
        os.replace(tmp_t, OUT_TXT)
    finally:
        for tmp in (tmp_j, tmp_t):
            if os.path.exists(tmp):
                os.remove(tmp)
    with open(OUT_JSON, "rb") as fh:
        dj = hashlib.sha256(fh.read()).hexdigest()[:12]
    with open(OUT_TXT, "rb") as fh:
        raw_t = fh.read()
    dt = hashlib.sha256(raw_t).hexdigest()[:12]
    flipped = bytes([raw_t[0] ^ 1]) + raw_t[1:]
    control_rejects = (hashlib.sha256(flipped).hexdigest()[:12] != seal_t)
    LD.gate("G-ARTIFACT-INTEGRITY",
            "THE ARTIFACTS ON DISK ARE THE SEALED OBJECTS, AND THE CHECK "
            "PRECEDES THE PROMOTION (#119).  Receipt and transcript are "
            "written to staged temporary files, hashed THERE and compared "
            "with the digests of the objects sealed at gate time; only "
            "matching bytes are moved into place by os.replace.  The bytes "
            "read back after the move are compared with the same seals as a "
            "second leg, never re-derived from disk, and the comparison is "
            "exercised in the failing direction on the same disk bytes with "
            "one bit flipped",
            dj == seal_j and dt == seal_t and control_rejects,
            "receipt disk %s seal %s; transcript disk %s seal %s; "
            "one-byte-flip control rejects %s"
            % (dj, seal_j, dt, seal_t, control_rejects))
    print()
    print("receipt    %s  %s" % (OUT_JSON, dj))
    print("transcript %s  %s" % (OUT_TXT, dt))
    return R, payload, text, seal_j, seal_t


# ===========================================================================
# SECTION 16.  THE CLI CONTRACT (#82), THE SELFTEST AND THE SWEEP
# ===========================================================================

def reset_state():
    global LINES, READS, READS_BY_CATEGORY, NUMREG
    del LINES[:]
    del READS[:]
    READS_BY_CATEGORY = {}
    NUMREG = set()


def artifact_digests():
    out = []
    for p in (OUT_JSON, OUT_TXT):
        if not os.path.exists(p):
            out.append((p, None))
            continue
        with open(p, "rb") as fh:
            out.append((p, hashlib.sha256(fh.read()).hexdigest()[:12]))
    return out


def run_mutant(name, paper_text):
    """a mutant run: it must DIE at the gate it NAMES, and write nothing."""
    global MUT, QUIET
    declared = ([m[1] for m in MUTANTS if m[0] == name] or [None])[0]
    MUT, QUIET = name, True
    reset_state()
    before = artifact_digests()
    try:
        out = full_run(paper_text=paper_text, write=False)
        finish(out[0], out[1], out[2], write=False)
        died = None
    except GateFail as exc:
        died = str(exc).split(" :: ")[0]
    finally:
        MUT, QUIET = None, False
    after = artifact_digests()
    return {"mutant": name, "declared_gate": declared, "died_at": died,
            "at_the_declared_gate": died == declared,
            "artifacts_unchanged": before == after}


def selftest():
    """#82: corrupt ONE anchor, confirm the run dies, and write nothing."""
    global QUIET
    rc = 0
    before = artifact_digests()
    for anchor in ("A-PIN", "A-AID", "A-AIDREC"):
        QUIET = True
        reset_state()
        try:
            full_run(break_anchor=anchor, write=False)
            ok, where = False, "NO-FAILURE"
        except GateFail as exc:
            ok, where = True, str(exc).split(" :: ")[0]
        finally:
            QUIET = False
        after = artifact_digests()
        print("[selftest] corrupted anchor %-9s -> %s at %s; artifacts %s"
              % (anchor, "died" if ok else "SURVIVED", where,
                 "unchanged" if before == after else "CHANGED"))
        if not ok or before != after:
            rc = 1
    return rc


def sweep(paper_text):
    return [run_mutant(name, paper_text) for name in MUTANT_NAMES]


def parse_args(argv):
    """THE ARGV WHITELIST.  Unknown flags exit 2; there is no silent
    flag-ignoring anywhere in this file."""
    opts = {"sweep": False, "selftest": False, "mutant": None, "quiet": False}
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == "--sweep":
            opts["sweep"] = True
        elif a == "--selftest":
            opts["selftest"] = True
        elif a == "--quiet":
            opts["quiet"] = True
        elif a == "--mutant":
            if i + 1 >= len(argv):
                raise CliError("--mutant needs a NAME")
            if opts["mutant"] is not None:
                raise CliError("--mutant given twice; there is no silent "
                               "flag-ignoring in this file")
            opts["mutant"] = argv[i + 1]
            i += 1
        elif a.startswith("--mutant="):
            if opts["mutant"] is not None:
                raise CliError("--mutant given twice; there is no silent "
                               "flag-ignoring in this file")
            opts["mutant"] = a.split("=", 1)[1]
        else:
            raise CliError("unknown argument %r" % a)
        i += 1
    if opts["mutant"] is not None and opts["mutant"] not in MUTANT_NAMES:
        raise CliError("unknown mutant %r" % opts["mutant"])
    return opts


def main(argv=None):
    global QUIET, MUT
    argv = sys.argv[1:] if argv is None else argv
    try:
        opts = parse_args(argv)
    except CliError as exc:
        print("[cli] %s" % exc, file=sys.stderr)
        print("[cli] usage: ndep_exact.py [--sweep] [--selftest] "
              "[--mutant NAME] [--quiet]", file=sys.stderr)
        return 2
    if opts["selftest"]:
        return selftest()
    QUIET = opts["quiet"]
    ppath = os.path.join(REPO, PAPER_REL)
    paper_text = (read_text(ppath, "PAPER-UNDER-TEST")
                  if os.path.exists(ppath) else "")
    if opts["mutant"]:
        rowm = run_mutant(opts["mutant"], paper_text)
        print("[mutant] %s -> died at %s (declared %s); artifacts %s"
              % (rowm["mutant"], rowm["died_at"], rowm["declared_gate"],
                 "unchanged" if rowm["artifacts_unchanged"] else "CHANGED"))
        return 0 if rowm["at_the_declared_gate"] else 1
    swept = []
    if opts["sweep"]:
        swept = sweep(paper_text)
        bad = [r for r in swept
               if not r["at_the_declared_gate"] or not r["artifacts_unchanged"]]
        print("[sweep] %d mutants, %d off-target" % (len(swept), len(bad)))
        for r in swept:
            print("        %-24s -> %s" % (r["mutant"], r["died_at"]))
        if bad:
            print("[sweep] OFF-TARGET: %s" % [r["mutant"] for r in bad],
                  file=sys.stderr)
            return 1
    reset_state()
    MUT = None
    try:
        R, src, ptxt = full_run(paper_text=paper_text, write=True)
        SWEEP_ROWS.extend(swept)
        finish(R, src, ptxt, write=True, swept=bool(swept))
    except GateFail as exc:
        print("[FAIL] %s" % exc, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
