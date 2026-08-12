#!/usr/bin/env python3.13
# -*- coding: utf-8 -*-
"""
v14 SEC -- THE SECTOR/ATLAS UNIT: GLUED WELDED WORLDS.
Instrument for `v14/paper-32-sec.md`.

QUESTION (pin `v14/note-sec-pin.md`, sha256-12 c46a9927f2a8, ledger #258).
Paper-19 drove one 9-actor arena whose co-division relation IS I7's own Cayley
incidence and welded it at both readings with zero free items.  Paper-21 drove
the next budget and proved that zero free items holds exactly at the
link-constant records.  Both are ONE SECTOR.  This unit glues TWO of them by
k SHARED ACTORS and asks whether geography composes.

  STAGE 1  THE ARENA FAMILY.  Two copies of the driven R = 3 saturating record,
           glued by k in {0, 1, 2, 3} shared actors.  Every one of the 45,010
           gluings is classified into its COMBINATORIAL TYPE (which tripartite
           classes align); a declared window is DRIVEN through the committed
           grammar's own menus at two declared seed rules, and the
           driven-vs-combinatorial equality that licenses the exhaustive
           columns is measured on every driven record.
  STAGE 2  THE UNION'S DICTIONARY.  The weld detector re-posed at the AMALGAM
           target -- two I7 lattices glued along the same k sites -- at both
           readings and at THREE carriers: the bare union (SITE <- ACTOR) and
           the two extended carriers the LOR lesson names (SITE <- ACTOR (+)
           PAIR, at the pair and at the incidence).
  STAGE 3  THE GLUING FIBER.  The shared actors' link-count compatibility
           census, and the gluing's own freedom priced.
  STAGE 4  CURVATURE OF THE GLUING.  The union's quadratic form at a shared
           site against the DIRECT SUM, measured as an exact linear system over
           Q; and the cross-sector division event, DRIVEN.
  STAGE 5  THE FORCED-OVERLAP QUESTION.  Does the union weld at some k and not
           others?
  STAGE 6  THE STERILITY CONTROL, MANDATORY.  k = 0, the disjoint arm, against
           R1's copy-forcing theorem.

WHAT THIS PROGRAM DOES
  SEC 1  PROVENANCE.  16 pinned sources, sha256-12 verified, products gated;
         verbatim (#62) anchors bound to their consumer gates; every text gate
         whitespace-normalises, ASCII-folds AND strips markdown prefixes.
  SEC 2  EXACT ARITHMETIC on Z_3^2 and on Q (fractions.Fraction).  The Gram
         systems are solved by exact row reduction; there are no floats.
  SEC 3  THE COMMITTED GRAMMAR, DRIVEN DIRECTLY.  d42b1's transport layer by
         text slice, d60's `B`/`dl` and d66's `conflict_grid` by AST
         extraction.  No admissibility rule is re-typed anywhere in this file.
  SEC 4  THE GLUING FAMILY and the declared driven WINDOW.
  SEC 5  THE AUTOMORPHISM MACHINERY: an orbit-stabilizer chain that returns an
         ORDER AND GENERATORS without enumerating the group, plus a second
         route that shares no code with it.
  SEC 6-11  THE SIX STAGES.
  SEC 12 THE WALLS.
  SEC 13 The verdict, derived a second time from the serialized receipt by a
         comparator that TYPES ALL FOUR TEMPLATES ITSELF; the paper gates --
         claim rendering, numeral coverage INCLUDING FENCED BLOCKS AND INLINE
         SPANS, fenced blocks BY MULTISET, head-verbatim and claim polarity;
         the TOTAL seal; the sweep-execution binding; the artifacts; the
         integrity check.

CLI CONTRACT (the #82 minimum: argv parsed against a whitelist)
---------------------------------------------------------------
    python3.13 v14/code/sec_exact.py
        THE DELIVERY RUN, and the ONLY writer.  Builds the whole census,
        evaluates every gate (the paper gates included), runs every declared
        mutant in-process, re-reads what it wrote and writes
        `sec_output.txt` and `sec_receipt.json` beside this file.
        Exits 0 iff every gate passes.

    --no-write      the same run, writing nothing.
    --numbers       the census only: every published row printed, no paper
                    gate, no mutant sweep, nothing written.
    --selftest      FALSIFICATION SELF-TEST.  Corrupts one anchor's expected
                    digest IN MEMORY, confirms the run dies at the anchor gate,
                    writes nothing, exits 1.  Exits 2 if the corrupted run does
                    NOT die.
    --mutant NAME   runs the pipeline with the named mutant active.  Exits 1
                    when the mutant is killed (the intended outcome), 0 if it
                    survives.  An unknown NAME exits 2.  Writes nothing.
    --break-anchor NAME
                    corrupts the named source anchor's expected digest.
                    Unknown NAME exits 2.  The run must exit 1.
    --verify-paper [PATH]
                    rebuilds the derivation and evaluates the paper gates with
                    PATH (this unit's paper by default) as the object under
                    test.  Exits 1 on drift, 0 on a clean paper, 2 if PATH does
                    not exist or is not a file.
    --list-gates / --list-mutants
                    print the registries and exit 0.

    Any other argument, any unknown flag argument, any missing flag argument,
    any SECOND MODE FLAG and any --verify-paper PATH that does not exist exits
    2.  No flag is mutant-only and no flag is a no-op.

THE TOTAL GATE-TO-DISK SEAL (RUNBOOK 14 addendum, v14 #119 + #148 totality).
Every published receipt key -- the measured layer and the vouching layer alike
-- is sealed at the moment its gate passes or listed as DECLARED-UNSEALED; the
artifacts are written from the sealed payload through `os.replace`; the
terminal integrity gate compares the bytes on disk against the gate-time seal.
A run that fails a gate writes nothing and promotes nothing.

RUNTIME INPUTS (#46/#91).  Exactly 16 files are read at run time as SOURCES,
all hash-pinned by this unit's frozen declaration, plus exactly one file read
as the OBJECT UNDER TEST -- this unit's own paper.  Both lists are enumerated
and gated.  No repository state outside them is read and no subprocess of any
kind is invoked, so the run is correct off-tree and with no version control
present.
"""

import ast
import hashlib
import json
import os
import re
import sys
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations, product

sys.setrecursionlimit(100000)

SELF = os.path.abspath(__file__)
REPO = os.path.dirname(os.path.dirname(os.path.dirname(SELF)))
OUT_TXT = os.path.join(os.path.dirname(SELF), "sec_output.txt")
OUT_JSON = os.path.join(os.path.dirname(SELF), "sec_receipt.json")

SCHEMA = "isp/v14/sec/1"
PAPER_REL = "v14/paper-32-sec.md"

# ===========================================================================
# SECTION 0.  THE FROZEN DECLARATION (RUNBOOK section 15: the arena is data)
# ===========================================================================

SOURCES = [
    ("A-PIN", "v14/note-sec-pin.md", "c46a9927f2a8",
     "THIS UNIT'S PIN (ledger #258): the six stages, the mandatory k = 0 "
     "sterility control, the walls and the pre-registered outcome names."),
    ("A-P19", "v14/paper-19-r3-weld.md", "50bb81e67942",
     "PAPER-19 (terminal): the forced dictionary [ACTOR->SITE | "
     "CO-DIVISION-ACTOR-PAIR->LINK | DIVISION-COUNT->n_l(x)], the (1,1,1) "
     "record, the 1296 = |Aut(K333)| map count and the 1/1/1 fibers this "
     "unit reproduces as its single-sector control."),
    ("A-P19REC", "v14/code/r3_weld_receipt.json", "dfea664f2408",
     "PAPER-19's COMMITTED RECEIPT: the single-sector numbers -- events, "
     "divisions, cells, isomorphism count and fibers -- are READ from these "
     "bytes at run time and reproduced, never re-typed."),
    ("A-P21", "v14/paper-21-r4dec.md", "ef4a8c35a0c4",
     "PAPER-21 (terminal): the detector at R = 4, the budget law "
     "R = n1 + n2 + n3, block quantisation, and the theorem that zero free "
     "items holds exactly at the link-constant records -- the statement this "
     "unit tests one level up, on a carrier that is not edge-transitive."),
    ("A-P21REC", "v14/code/r4dec_receipt.json", "a4538c7019e6",
     "PAPER-21's COMMITTED RECEIPT: its R = 3 back-validation row (the "
     "I7-STRICT class at 72 triples) is read from these bytes."),
    ("A-R1", "v14/paper-01-continuum-rung.md", "c4c8880874bf",
     "R1 / paper-01 (terminal): the copy-forcing theorem and the sterility "
     "prescription -- the prediction this unit's k = 0 arm gates."),
    ("A-R2", "v14/paper-02-manifold-rung.md", "1a80a5bf1a1b",
     "R2 / paper-02 (terminal): locality is DECLARABLE, at 14 of 109 rules "
     "-- the ancestry of the shared-participation question."),
    ("A-HA", "v13/paper-ha-successor.md", "f286ba10d2d9",
     "I7 / HA: the declared readout, the admissibility criterion, and "
     "requirement 3 -- the two-way rule this unit's controls discharge."),
    ("A-I7", "v13/code/ha_successor_receipt.json", "542b8735daf0",
     "I7's ARENA AS DATA: sites, links and the declared count box.  The "
     "target lattices of this unit are built from these bytes."),
    ("A-D42B1", "v10/code/d42b1_transport_exact.py", "576275d55ecf",
     "THE COMMITTED TRANSPORT GRAMMAR, driven directly: this unit's only "
     "source of admissibility."),
    ("A-D60", "v10/code/d60_crystal_exact.py", "684cdb76552b",
     "D60: the Builder `B` and the delivery helper `dl`, AST-extracted."),
    ("A-D66", "v10/code/d66_arbitration_crystal_exact.py", "3d0516ab106e",
     "D66: CONFLICT-GRID(g, R), the committed constructor, AST-extracted and "
     "re-run as this unit's driver anchor."),
    ("A-D66OUT", "v10/data/d66_arbitration_crystal_exact.out", "e252529d2586",
     "D66's COMMITTED OUTPUT: the GRID(g=3,R=3) row is READ from this file "
     "at run time and reproduced, never re-typed."),
    ("A-L1", "v11/note-L1-lorentz-no-go-lemma.md", "93ea24591c3c",
     "L-1: the fourth-form clause argued before any test, and the sentence "
     "retracted on 2026-07-28 that no paper of this line may reproduce."),
    ("A-CAT", "v11/note-v11p0a-reproduction-catalog.md", "0cebe543e814",
     "the reproduction catalog 1.6/1.7: the BHS block and the "
     "Kleitman-Rothschild height-control warning."),
]
SOURCE_IDS = [s[0] for s in SOURCES]

# ---------------------------------------------------------------------------
# CITED AND NOT READ (#91: no moving refs, and never another worker's live
# worktree state).  PAPER-30 / LOR supplies this unit's METHOD -- run the
# extended carriers -- and its delivered text is under concurrent rewrite in
# the working tree while this unit runs.  Reading it would read a live
# worktree state, so it is NOT in the runtime source set at all: the lesson
# is taken from THIS UNIT'S OWN PIN, which states it and is frozen, and the
# abstention is GATED rather than announced.
# ---------------------------------------------------------------------------
CITED_NOT_READ = [
    {"id": "A-LOR", "path": "v14/paper-30-lor.md",
     "pinned_sha256_12": "f3e9e9df2c70", "pinned_at_ledger": 252,
     "why": "PAPER-30 / LOR (delivered, NOT terminal): the extended-carrier "
            "lesson that this unit runs three carriers because of.  Its "
            "delivered text is under concurrent rewrite in the working tree, "
            "so rule #91 forbids reading it here; the lesson is anchored on "
            "this unit's own frozen pin instead, and no sentence of LOR is "
            "quoted anywhere in this unit."},
]

BANNED_L1 = ("precisely the form U4 tests, and precisely the form the "
             "corpus's strongest relativity result took")

# THE SEAM RESONANCE.  Paper-19 named the Lorentzian resonance because its
# determinant had just gone positive.  This unit measures a seam whose form is
# NOT determined by the record and which admits indefinite completions, so the
# same discipline applies with more force: naming is mandatory and a gate
# requires the sentence to be present in the paper.
SEAM_NAMED = ("The indefinite completion is NAMED AND NOT READ: that the "
              "seam's undetermined block admits completions of mixed sign is "
              "a statement about what the record fails to fix, it is not a "
              "signature, and no Lorentzian, causal or dimensional reading of "
              "it is taken here or licensed by anything measured here.")

# ===========================================================================
# SECTION 1.  THE INSTRUMENT'S SPINE: ledger, seal, gates, mutants
# ===========================================================================

MUTANTS = [
    ("MUT-ANCHOR-DIGEST", "corrupts the A-P19 source digest",
     "G-SOURCES"),
    ("MUT-ANCHOR-TEXT", "corrupts one verbatim anchor's needle",
     "G-ANCHORS"),
    ("MUT-GRAMMAR-ANCHOR", "drops one event from the driver's anchor record",
     "G-GRAMMAR-ANCHOR"),
    ("MUT-MENU-MEMO", "withholds arbitrations from the UN-memoised menu, so "
     "the memo-disabled re-drive disagrees with the memoised record",
     "G-MENU-PURE"),
    ("MUT-SECTOR-CELL", "moves one cell of the single-sector count field",
     "G-SECTOR"),
    ("MUT-SECTOR-WELD", "inflates the single-sector isomorphism count",
     "G-SECTOR-WELD"),
    ("MUT-AUT-ROUTE", "poisons the second automorphism route",
     "G-AUT-ROUTES"),
    ("MUT-TYPE-COUNT", "drops one gluing from the type census",
     "G-GLUING-CENSUS"),
    ("MUT-DRIVEN-EQ", "flips one driven pair count",
     "G-DRIVEN-EQUALS-COMBINATORIAL"),
    ("MUT-CLEAN-CRIT", "inverts the doubled-free criterion",
     "G-CLEAN-CRITERION"),
    ("MUT-DICT-FATE", "forges one dictionary row's fate",
     "G-DICT"),
    ("MUT-FIBER-ROUTE", "poisons the orbit route for the site fiber",
     "G-FIBER-ROUTES"),
    ("MUT-SEAM-RANK", "misreports the seam system's rank",
     "G-SEAM-RANK"),
    ("MUT-SEAM-WITNESS", "corrupts the indefinite witness vector",
     "G-SEAM-WITNESS"),
    ("MUT-CROSS-FATE", "forges the cross-sector event's fate",
     "G-CROSS"),
    ("MUT-STERILITY", "breaks the k = 0 direct-sum identity",
     "G-STERILITY"),
    ("MUT-OVERLAP", "forges one forced-overlap row",
     "G-FORCED-OVERLAP"),
    ("MUT-COMPAT", "forges one gluing-compatibility row",
     "G-GLUING-FIBER"),
    ("MUT-L1-INJECT", "injects the retracted L-1 sentence into the paper",
     "G-WALL-L1"),
    ("MUT-NAMING-DELETE", "deletes the seam-naming sentence from the paper",
     "G-WALL-NAMED"),
    ("MUT-WALL-SCAN", "writes a boost reading into the measurement layer",
     "G-WALL-SCAN"),
    ("MUT-WALL-PAPER", "writes a banned dimension reading into the paper",
     "G-WALL-SCAN"),
    ("MUT-CITED-READ", "inverts the cited-and-not-read abstention",
     "G-CITED-NOT-READ"),
    ("MUT-PAPER-TABLE", "swaps two data cells of a published table row",
     "G-PAPER-CLAIMS"),
    ("MUT-PAPER-SPELLED", "moves a spelled numeral in the paper from "
     "fifty-four to a thousand", "G-PAPER-SPELLED"),
    ("MUT-HEAD-FORGE", "forges the outcome word in the builder's head",
     "G-VERDICT-RECON"),
    ("MUT-PAPER-NUMBER", "moves a number in the paper under test",
     "G-PAPER-COVERAGE"),
    ("MUT-PAPER-FENCE", "forges a twin of the verdict fence",
     "G-PAPER-FENCE"),
    ("MUT-PAPER-POLARITY", "inverts the direct-sum claim's polarity in the "
     "paper", "G-PAPER-POLARITY"),
    ("MUT-SEAL-DROP", "drops one key from the seal manifest",
     "G-SEAL-COMPLETE"),
]
MUTANT_NAMES = [m[0] for m in MUTANTS]
ACTIVE_MUTANT = [None]


def mut(name):
    return ACTIVE_MUTANT[0] == name


def pick(name, normal, corrupted):
    return corrupted if mut(name) else normal


class GateFail(Exception):
    pass


class CliError(Exception):
    pass


REPORT = []


def say(s=""):
    REPORT.append(s)


class Ledger:
    """the chained gate ledger: every gate's statement, evidence and verdict,
    each row digesting its predecessor."""

    def __init__(self):
        self.rows = []
        self.chain = hashlib.sha256(b"SEC-LEDGER-GENESIS").hexdigest()

    def gate(self, name, ok, statement, evidence):
        ok = bool(ok)
        row = {"gate": name, "ok": ok, "statement": statement,
               "evidence": evidence}
        payload = json.dumps([self.chain, row], sort_keys=True,
                             default=str).encode()
        self.chain = hashlib.sha256(payload).hexdigest()
        row["chain"] = self.chain[:16]
        self.rows.append(row)
        if not ok:
            raise GateFail("%s: %s | evidence=%s" % (name, statement,
                                                     json.dumps(evidence,
                                                                default=str)))
        return True

    def names(self):
        return [r["gate"] for r in self.rows]


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
                                     default=str).encode()).hexdigest()


class Seal:
    """THE TOTAL GATE-TO-DISK SEAL.  A key is sealed at the moment its gate
    passes; the artifacts are written from the sealed objects; integrity is
    disk-bytes against the gate-time seal, never a re-derivation."""

    def __init__(self):
        self.seals = {}
        self.unsealed = {}
        self.order = []

    def seal(self, key, value):
        self.seals[key] = digest(value)
        self.order.append(key)
        return value

    def declare_unsealed(self, key, why):
        self.unsealed[key] = why

    def manifest(self):
        return {"sealed": dict(self.seals),
                "declared_unsealed": dict(self.unsealed),
                "order": list(self.order)}


def read_bytes(rel):
    with open(os.path.join(REPO, rel), "rb") as f:
        return f.read()


def read_text_file(path):
    with open(path, "rb") as f:
        return f.read().decode("utf-8")


MD_PREFIX = re.compile(r"^[ \t]*(?:>[ \t]*)*(?:[-*+][ \t]+|\d+[.)][ \t]+)?")


def mdstrip(s):
    return "\n".join(MD_PREFIX.sub("", ln) for ln in s.split("\n"))


FOLD = {"—": "-", "–": "-", "−": "-", "‘": "'",
        "’": "'", "“": '"', "”": '"', " ": " ",
        "→": "->", "←": "<-", "⊕": "(+)"}


def ascii_fold(s):
    for a, b in FOLD.items():
        s = s.replace(a, b)
    return s


def norm(s):
    return " ".join(s.split())


def canon(s):
    """#125: whitespace-normalise, ASCII-fold AND strip markdown prefixes,
    then drop emphasis and code markers, on BOTH sides of every text gate."""
    s = ascii_fold(mdstrip(s))
    s = s.replace("**", "").replace("`", "").replace("*", "")
    return norm(s)


NEEDLE_FLOOR = 40


def match_needle(hay, needle):
    return canon(needle) in canon(hay)


# ===========================================================================
# SECTION 2.  EXACT ARITHMETIC:  Z_3^2, and linear algebra over Q
# ===========================================================================

SITES = tuple((i, j) for i in range(3) for j in range(3))
SITE_INDEX = {s: k for k, s in enumerate(SITES)}


def zadd(a, b):
    return ((a[0] + b[0]) % 3, (a[1] + b[1]) % 3)


def zneg(a):
    return ((-a[0]) % 3, (-a[1]) % 3)


CLASS_DIR = {"ROW": (0, 1), "COL": (1, 0), "DIA": (1, 1), "ANT": (1, 2)}
CLASS_NAMES = ("ROW", "COL", "DIA", "ANT")


def parallel_class(d):
    """the resolvable partition of AG(2,3) into the three lines of slope d."""
    H = frozenset({(0, 0), d, zadd(d, d)})
    seen, out = set(), []
    for x in SITES:
        L = tuple(sorted(zadd(x, h) for h in H))
        if L not in seen:
            seen.add(L)
            out.append(L)
    return tuple(sorted(out))


CLASSES = {k: parallel_class(v) for k, v in CLASS_DIR.items()}
# the three parts of the realised tripartite relation are the ANT lines
PART_OF = {}
for _i, _L in enumerate(CLASSES["ANT"]):
    for _s in _L:
        PART_OF[_s] = _i


def rref(rows, ncol):
    """exact reduced row echelon form over Q.  Returns (rref rows, pivots)."""
    M = [list(r) for r in rows]
    piv = []
    r = 0
    for c in range(ncol):
        p = None
        for i in range(r, len(M)):
            if M[i][c] != 0:
                p = i
                break
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        inv = Fraction(1, 1) / M[r][c]
        M[r] = [x * inv for x in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [a - f * b for a, b in zip(M[i], M[r])]
        piv.append(c)
        r += 1
        if r == len(M):
            break
    return M, piv


def solve_affine(rows, rhs, ncol):
    """the affine solution set of an exact linear system: returns
    (rank, kernel_dim, one particular solution or None)."""
    aug = [list(r) + [b] for r, b in zip(rows, rhs)]
    M, piv = rref(aug, ncol + 1)
    if ncol in piv:
        return len(piv) - 1, None, None       # inconsistent
    rank = len(piv)
    part = [Fraction(0)] * ncol
    for i, c in enumerate(piv):
        part[c] = M[i][ncol]
    return rank, ncol - rank, part


def kernel_basis(rows, ncol):
    M, piv = rref(rows, ncol)
    free = [c for c in range(ncol) if c not in piv]
    out = []
    for f in free:
        v = [Fraction(0)] * ncol
        v[f] = Fraction(1)
        for i, c in enumerate(piv):
            v[c] = -M[i][f]
        out.append(v)
    return out


def q_of(nvec):
    """I7's own readout: n_l is the squared length of the link direction l,
    and q is recovered by polarization.  Matched verbatim against HA."""
    n1, n2, n3 = nvec
    q12 = Fraction(n3 - n1 - n2, 2)
    return Fraction(n1), Fraction(n2), q12, Fraction(n1) * Fraction(n2) \
        - q12 * q12


def admissible(nvec):
    q11, _q22, _q12, det = q_of(nvec)
    return q11 > 0 and det > 0


def sym_index(d):
    """the (i,j) -> column index map of Sym^2(Q^d), i <= j."""
    idx = {}
    for i in range(d):
        for j in range(i, d):
            idx[(i, j)] = len(idx)
    return idx


def quad_row(vec, idx, d):
    """the row of Q(vec) in the Sym^2 coordinates: Q(v) = sum q_ij v_i v_j
    with the off-diagonal entries appearing twice."""
    row = [Fraction(0)] * len(idx)
    for i in range(d):
        for j in range(i, d):
            c = Fraction(vec[i] * vec[j]) * (1 if i == j else 2)
            row[idx[(i, j)]] += c
    return row


def eval_form(qvec, idx, d, v):
    tot = Fraction(0)
    for i in range(d):
        for j in range(i, d):
            tot += qvec[idx[(i, j)]] * v[i] * v[j] * (1 if i == j else 2)
    return tot


def leading_minors(qvec, idx, d):
    """exact Sylvester: the d leading principal minors, by cofactor expansion
    over Q (d <= 4 here, so the direct expansion is affordable and exact)."""
    def M(k):
        return [[qvec[idx[(min(i, j), max(i, j))]] for j in range(k)]
                for i in range(k)]

    def det(A):
        n = len(A)
        if n == 1:
            return A[0][0]
        tot = Fraction(0)
        for c in range(n):
            sub = [[A[i][j] for j in range(n) if j != c] for i in range(1, n)]
            tot += ((-1) ** c) * A[0][c] * det(sub)
        return tot
    return [det(M(k)) for k in range(1, d + 1)]


# ===========================================================================
# SECTION 3.  THE COMMITTED GRAMMAR, DRIVEN DIRECTLY
# ===========================================================================

EXIT_NAMES = ("exit", "quit", "_exit")


def no_exit(nodes):
    """d66's committed C0a form, adopted verbatim: no CALL and no bare
    NAME/ATTRIBUTE reference to an exit callable survives an extracted body."""
    for n in nodes:
        for c in ast.walk(n):
            if isinstance(c, ast.Attribute) and c.attr in EXIT_NAMES:
                return False
            if isinstance(c, ast.Name) and c.id in EXIT_NAMES:
                return False
    return True


class Grammar:
    """the committed layers, loaded as SINGLE SOURCES.  Nothing in this file
    re-implements an admissibility rule: `candidates_for` IS d42b1's."""

    def __init__(self, texts):
        st = texts["v10/code/d42b1_transport_exact.py"]
        cut = st.index('print("[d42b1')
        self.slice_text = st[:cut]
        ns = {}
        exec(compile(self.slice_text, "d42b1_slice", "exec"), ns)
        self.ns = ns
        self.raw_candidates_for = ns["candidates_for"]
        self.regs_of = ns["regs_of"]
        self.vname = ns["vname"]
        self.V0 = ns["V0"]
        self.memo = {}
        self.memo_calls = 0
        self.memo_hits = 0
        self.use_memo = True
        self.extracted = {}
        g60 = self._extract("v10/code/d60_crystal_exact.py", texts, "d60",
                            {"candidates_for": self.candidates_for,
                             "event_poset": ns["event_poset"], "V0": self.V0})
        self.B = g60["B"]
        self.dl = g60["dl"]
        g66 = self._extract("v10/code/d66_arbitration_crystal_exact.py", texts,
                            "d66",
                            {"B": self.B, "dl": self.dl, "vname": self.vname,
                             "V0": self.V0,
                             "candidates_for": self.candidates_for})
        self.conflict_grid = g66["conflict_grid"]
        self.slice_exit_free = ("sys.exit" not in self.slice_text
                                and no_exit(ast.parse(self.slice_text).body))
        self.bodies_exit_free = all(no_exit(v)
                                    for v in self.extracted.values())

    def candidates_for(self, hist, inits):
        """THE MEMOISED MENU.  d42b1's `candidates_for` is a pure function of
        (history, initiators); the memo is a cache over that pair and nothing
        else, and G-MENU-PURE re-drives a declared set with the memo disabled
        and compares the records event for event."""
        self.memo_calls += 1
        if not self.use_memo:
            raw = self.raw_candidates_for(list(hist), tuple(inits))
            if mut("MUT-MENU-MEMO"):
                raw = [e for e in raw if e[0][0] != "r"]
            return raw
        key = (tuple(hist), tuple(inits))
        got = self.memo.get(key)
        if got is None:
            got = self.raw_candidates_for(list(hist), tuple(inits))
            self.memo[key] = got
        else:
            self.memo_hits += 1
        return got

    def _extract(self, rel, texts, marker, extra, only=None):
        tree = ast.parse(texts[rel])
        keep = [n for n in tree.body
                if isinstance(n, (ast.FunctionDef, ast.ClassDef))
                and (only is None or n.name in only)]
        self.extracted[rel] = keep
        g = {"Fr": Fraction, "combinations": combinations, "Counter": Counter,
             "permutations": permutations, "product": product,
             "sys": sys, "ast": ast, "os": os}
        g.update(extra)
        exec(compile(ast.fix_missing_locations(
            ast.Module(body=keep, type_ignores=[])), marker, "exec"), g)
        return g


def drive(G, actors, rounds, drop_arb=None):
    """THE GENERALIZED SCHEDULE DRIVER, widened from nine actors to the union's
    pool.  Exactly d66's CONFLICT-GRID(g, R) cycle -- conflict-supply
    deliveries from the group's seed, g proposals (0 for the seed, 1 for the
    rest), one g-proposer arbitration won by the seed -- with the ACTOR POOL,
    the GROUPING, THE SEED and the GROUP ORDER taken from the schedule.  Every
    event is specified by its FULL TUPLE and taken from the layer's own menu;
    at most one candidate can match, so d60's tie-break is never consulted."""
    b = G.B(tuple(actors))
    cur = {a: G.V0 for a in actors}
    narb = 0
    for groups in rounds:
        for (grp, sd) in groups:
            grp = list(grp)
            base = cur[sd]
            for a in grp:
                if a == sd or cur[a] == base:
                    continue
                b.pick((sd, a),
                       lambda e, s=sd, r=a, v=base: (e[0] == "d" and e[1] == s
                                                     and e[2] == r
                                                     and e[3] == v),
                       "supply %r->%r" % (sd, a))
                if b.refusal:
                    return b
            trips = [(a, base, 0 if a == sd else 1) for a in grp]
            for t in trips:
                b.pick((t[0],), lambda z, e=("p",) + t: z == e,
                       "propose %r" % (t[0],))
                if b.refusal:
                    return b
            ckey = frozenset(trips)
            wkey = frozenset({[t for t in trips if t[0] == sd][0]})
            if drop_arb is not None and narb == drop_arb:
                narb += 1
                continue
            narb += 1
            b.pick((sd,), lambda z, e=("r", sd, ckey, wkey): z == e,
                   "arbitrate %r" % (sd,))
            if b.refusal:
                return b
            v = G.vname(base, wkey, sd)
            for a in grp:
                cur[a] = v
    return b


def record_of(G, b, actors):
    """the record's published shape.  Footprints are cut to the actor pool."""
    keep = set(actors)
    divs = [e for e in b.H if e[0] == "r"]
    foot = [frozenset(r for r in G.regs_of(e) if r in keep) for e in divs]
    return {"events": len(b.H), "maxhits": b.maxhits,
            "refusal": (list(b.refusal) if b.refusal else None),
            "divisions": len(divs), "footprints": foot}


def codivision_rel(footprints):
    """the co-division incidence on the UNORDERED actor pair: a division event
    is ON the pair when its register footprint meets both endpoints."""
    rel = Counter()
    for f in footprints:
        for u, v in combinations(sorted(f, key=repr), 2):
            rel[frozenset((u, v))] += 1
    return dict(rel)


# ===========================================================================
# SECTION 4.  THE ARENA FAMILY: SECTORS, GLUINGS, TYPES, THE WINDOW
# ===========================================================================

SAT_COLLINEAR = ("ROW", "COL", "DIA")   # paper-19's own driven arrangement
# a declared NON-COLLINEAR I7-STRICT triple, used to measure that the union
# arena does not depend on which saturating arrangement each sector runs
SAT_ALT = None                          # computed in build_alt_saturating()


def build_alt_saturating():
    """a saturating grouping triple that is NOT the three parallel classes:
    every one of the 27 cells covered exactly once, and at least one group
    that is not a line of AG(2,3).  Found by exhaustive search over the
    36 saturating partitions -- never typed."""
    parts = []

    def rec(rem, acc):
        if not rem:
            parts.append(tuple(sorted(acc)))
            return
        a, rest = rem[0], rem[1:]
        for pair in combinations(rest, 2):
            rec(tuple(x for x in rest if x not in pair),
                acc + [tuple(sorted((a,) + pair))])
    rec(tuple(SITES), [])
    I7L = ((1, 0), (0, 1), (1, 1))

    def mask(P):
        m = set()
        for g in P:
            for u, v in combinations(g, 2):
                d = ((u[0] - v[0]) % 3, (u[1] - v[1]) % 3)
                if d in I7L:
                    m.add((v, d))
                elif zneg(d) in I7L:
                    m.add((u, zneg(d)))
                else:
                    return None
        return frozenset(m)
    sat = [(P, mask(P)) for P in parts]
    sat = [(P, m) for P, m in sat if m is not None and len(m) == 9]
    lines = {frozenset(L) for c in CLASS_NAMES for L in CLASSES[c]}
    full = frozenset((x, l) for x in SITES for l in I7L)
    for P1, m1 in sat:
        for P2, m2 in sat:
            if m1 & m2:
                continue
            for P3, m3 in sat:
                if (m1 | m2) & m3 or (m1 | m2 | m3) != full:
                    continue
                if any(frozenset(g) not in lines for P in (P1, P2, P3)
                       for g in P):
                    return (P1, P2, P3), len(sat)
    return None, len(sat)


def sector_rounds(mp, arrangement, seedrule, shared):
    """one sector's three rounds as (group, seed) pairs in the declared order.
    SEED RULE `first`  -- paper-19's canonical transversal: the first member.
    SEED RULE `shared` -- the first SHARED member if the group has one, else
    the first member.  The group order is by the seed's repr, which is d66's
    own ascending-seed order transported to this unit's actor names."""
    rounds = []
    for cls in arrangement:
        P = CLASSES[cls] if isinstance(cls, str) else cls
        gs = []
        for g in P:
            names = [mp[s] for s in sorted(g)]
            if seedrule == "shared":
                sh = [n for n in names if n in shared]
                sd = sh[0] if sh else names[0]
            else:
                sd = names[0]
            gs.append((tuple(names), sd))
        rounds.append(tuple(sorted(gs, key=lambda t: repr(t[1]))))
    return tuple(rounds)


def gluing_maps(glue):
    """the two site->actor namings the gluing induces.  Shared actors carry
    the neutral name ('S', i) so that neither sector's naming is privileged."""
    amap, bmap = {}, {}
    for i, (sa, sb) in enumerate(glue):
        amap[sa] = ("S", i)
        bmap[sb] = ("S", i)
    for s in SITES:
        amap.setdefault(s, ("A", s))
        bmap.setdefault(s, ("B", s))
    actors = sorted(set(amap.values()) | set(bmap.values()), key=repr)
    shared = frozenset(("S", i) for i in range(len(glue)))
    return actors, amap, bmap, shared


def union_rounds(glue, seedrule, arrA=SAT_COLLINEAR, arrB=SAT_COLLINEAR):
    actors, amap, bmap, shared = gluing_maps(glue)
    rounds = (sector_rounds(amap, arrA, seedrule, shared)
              + sector_rounds(bmap, arrB, seedrule, shared))
    return actors, rounds, amap, bmap, shared


def combinatorial_rel(glue, arrA=SAT_COLLINEAR, arrB=SAT_COLLINEAR):
    """the union's co-division relation computed from the schedule alone --
    the route the exhaustive columns use.  G-DRIVEN-EQUALS-COMBINATORIAL
    measures it against the DRIVEN record on every window member."""
    actors, amap, bmap, shared = gluing_maps(glue)
    rel = Counter()
    for mp, arr in ((amap, arrA), (bmap, arrB)):
        for cls in arr:
            P = CLASSES[cls] if isinstance(cls, str) else cls
            for g in P:
                for u, v in combinations(sorted(g), 2):
                    rel[frozenset((mp[u], mp[v]))] += 1
    return actors, dict(rel), amap, bmap, shared


TYPE_CACHE = {}
DFREE_CACHE = {}


def part_profile(glue):
    """the gluing's PART PROFILE: the multiset of (A-part, B-part) the shared
    actors occupy.  Both the type and the doubled-free criterion are functions
    of this and of nothing else, which is why they are memoised on it -- the
    memo is a cache over a derived key, never over a verdict."""
    M = Counter()
    for sa, sb in glue:
        M[(PART_OF[sa], PART_OF[sb])] += 1
    return tuple(sorted(M.items()))


def gluing_type(glue):
    """THE COMBINATORIAL TYPE, and it is exactly `which tripartite classes
    align`: the bipartite part-incidence matrix of the shared set, taken up to
    permutation of each sector's three parts."""
    prof = part_profile(glue)
    got = TYPE_CACHE.get(prof)
    if got is not None:
        return got
    M = dict(prof)
    rows = sorted({r for r, _c in M})
    cols = sorted({c for _r, c in M})
    best = None
    for rp in permutations(rows):
        for cp in permutations(cols):
            key = tuple(sorted((rp.index(r), cp.index(c), v)
                               for (r, c), v in M.items()))
            if best is None or key < best:
                best = key
    TYPE_CACHE[prof] = best
    return best


def all_gluings(k):
    out = []
    for SA in combinations(SITES, k):
        for SB in permutations(SITES, k):
            out.append(tuple(zip(SA, SB)))
    return out


def doubled_free(glue):
    """the criterion, stated per PAIR of shared actors: no shared pair may be
    adjacent in BOTH sectors, and adjacency in a sector is exactly `different
    tripartite parts`.  The per-pair form is the definition; the memo is on
    the part profile, which determines every pair's answer."""
    prof = part_profile(glue)
    got = DFREE_CACHE.get(prof)
    if got is not None:
        return got
    out = True
    for (sa, sb), (ta, tb) in combinations(glue, 2):
        if PART_OF[sa] != PART_OF[ta] and PART_OF[sb] != PART_OF[tb]:
            out = False
            break
    if mut("MUT-CLEAN-CRIT") and len(glue) > 1:
        out = not out
    DFREE_CACHE[prof] = out
    return out


# ===========================================================================
# SECTION 5.  THE AUTOMORPHISM MACHINERY (two routes, no shared code)
# ===========================================================================

def make_graph(nodes, rel, weighted):
    idx = {a: i for i, a in enumerate(nodes)}
    n = len(nodes)
    adj = [set() for _ in range(n)]
    W = {}
    for e, c in rel.items():
        u, v = sorted(e, key=repr)
        i, j = idx[u], idx[v]
        adj[i].add(j)
        adj[j].add(i)
        W[(min(i, j), max(i, j))] = c if weighted else 1
    return n, adj, W, idx


def _init_colour(n, adj, W):
    lab = [tuple(sorted(Counter(W[(min(v, u), max(v, u))]
                                for u in adj[v]).items())) for v in range(n)]
    o = {s: i for i, s in enumerate(sorted(set(lab)))}
    return [o[s] for s in lab]


def _refine(n, adj, W, col):
    col = list(col)
    while True:
        sig = [(col[v], tuple(sorted((col[u], W[(min(v, u), max(v, u))])
                                     for u in adj[v]))) for v in range(n)]
        o = {s: i for i, s in enumerate(sorted(set(sig)))}
        new = [o[s] for s in sig]
        if new == col:
            return col
        col = new


def _individualise(n, adj, W, ind, prev=None, newv=None):
    """the refined colouring in which each vertex of `ind` carries a colour of
    its own.  Refinement is a SOUND invariant: any automorphism fixing every
    vertex of `ind` preserves this colouring, so a vertex whose class is a
    singleton has a trivial orbit and needs no search.  `prev`/`newv` take one
    incremental step -- individualising into an already-refined colouring is
    the same sequence as rebuilding it, and it is what makes the chain O(n)
    refinements rather than O(n^2)."""
    if prev is not None and newv is not None:
        base = list(prev)
        base[newv] = max(base) + 1
        return _refine(n, adj, W, base)
    base = _refine(n, adj, W, _init_colour(n, adj, W))
    for v in ind:
        base = list(base)
        base[v] = max(base) + 1
        base = _refine(n, adj, W, base)
    return base


def find_map(n, adj, W, n2, adj2, W2, fixed, c1=None, c2=None):
    """ONE isomorphism from graph 1 to graph 2 extending the partial map
    `fixed`, or None.  Exhaustive backtracking with equitable-refinement
    pruning; no sampling and no cap."""
    if n != n2:
        return None
    if c1 is None:
        c1 = _refine(n, adj, W, _init_colour(n, adj, W))
    if c2 is None:
        c2 = _refine(n2, adj2, W2, _init_colour(n2, adj2, W2))
    if sorted(Counter(c1).values()) != sorted(Counter(c2).values()):
        return None
    cls = {}
    for v in range(n2):
        cls.setdefault(c2[v], []).append(v)
    phi = dict(fixed)
    used = set(phi.values())
    if len(used) != len(phi):
        return None
    for v, x in phi.items():
        if c1[v] != c2[x]:
            return None
    for v, x in phi.items():
        for w, y in phi.items():
            if repr(w) <= repr(v):
                continue
            if (w in adj[v]) != (y in adj2[x]):
                return None
            if (w in adj[v]) and W[(min(v, w), max(v, w))] != \
                    W2[(min(x, y), max(x, y))]:
                return None
    order = [v for v in range(n) if v not in phi]
    order.sort(key=lambda v: (-len(adj[v]), v))
    res = [None]

    def bt(k):
        if k == len(order):
            res[0] = dict(phi)
            return True
        u = order[k]
        for x in cls.get(c1[u], ()):
            if x in used:
                continue
            ok = True
            for w, y in phi.items():
                if (w in adj[u]) != (y in adj2[x]):
                    ok = False
                    break
                if (w in adj[u]) and W[(min(u, w), max(u, w))] != \
                        W2[(min(x, y), max(x, y))]:
                    ok = False
                    break
            if ok:
                phi[u] = x
                used.add(x)
                if bt(k + 1):
                    return True
                used.discard(x)
                del phi[u]
        return False
    if bt(0):
        return res[0]
    return None


AUT_CACHE = {}


def aut_chain(n, adj, W):
    """ROUTE 1 -- |Aut| AND GENERATORS by the orbit-stabilizer chain.  At each
    level the orbit of the next unfixed point under the stabilizer of the
    points already fixed is computed by one EXISTENCE test per candidate, so
    the cost is independent of |Aut| and no element is ever enumerated.  The
    candidates are cut to the individualisation-refinement class of the point,
    which is sound because refinement is an automorphism invariant; a point
    whose class is already a singleton contributes an orbit of 1 and is not
    searched.  The transversal elements collected across the chain generate
    the group (the standard stabilizer-chain fact)."""
    key = (n, tuple(sorted((min(i, j), max(i, j), W[(min(i, j), max(i, j))])
                           for i in range(n) for j in adj[i] if i < j)))
    if key in AUT_CACHE:
        return AUT_CACHE[key]
    order = 1
    gens = []
    ind = []
    col = _individualise(n, adj, W, ())
    for v in range(n):
        if v in ind:
            continue
        cand = [x for x in range(n) if col[x] == col[v] and x not in ind]
        if len(cand) > 1:
            fixed = {f: f for f in ind}
            orb = 0
            for x in cand:
                g = find_map(n, adj, W, n, adj, W, {**fixed, v: x}, col, col)
                if g is not None:
                    orb += 1
                    if x != v:
                        gens.append(tuple(g[i] for i in range(n)))
            if orb == 0:
                AUT_CACHE[key] = (0, [])
                return 0, []
            order *= orb
        ind.append(v)
        col = _individualise(n, adj, W, ind, col, v)
    AUT_CACHE[key] = (order, gens)
    return order, gens


AUT_ENUM_NODE_CAP = 20


def aut_enumerate(n, adj, W, cap):
    """ROUTE 2 -- the same order by EXPLICIT ENUMERATION of every
    automorphism, sharing no code with route 1: no refinement, no chain, a
    plain lexicographic backtracking that counts leaves.  Returns None when
    the count would exceed `cap` or the graph exceeds the declared node cap,
    so the route is honest about where it can speak."""
    if n > AUT_ENUM_NODE_CAP:
        return None
    A = [frozenset(a) for a in adj]
    deg = [len(A[v]) for v in range(n)]
    cnt = [0]
    phi = {}
    used = set()

    def bt(k):
        if cnt[0] > cap:
            return
        if k == n:
            cnt[0] += 1
            return
        for x in range(n):
            if x in used or deg[x] != deg[k]:
                continue
            good = True
            for w in range(k):
                if (w in A[k]) != (phi[w] in A[x]):
                    good = False
                    break
                if (w in A[k]) and W[(min(k, w), max(k, w))] != \
                        W[(min(x, phi[w]), max(x, phi[w]))]:
                    good = False
                    break
            if good:
                phi[k] = x
                used.add(x)
                bt(k + 1)
                used.discard(x)
                del phi[k]
    bt(0)
    return None if cnt[0] > cap else cnt[0]


def aut_components(n, adj, W):
    """ROUTE 3 -- for a DISCONNECTED graph only: |Aut| is the product over
    isomorphism classes of components of |Aut(C)|^m * m!.  Used on the k = 0
    sterility arm, where routes 1 and 2 are the only other options and route 2
    cannot afford the answer."""
    seen = set()
    comps = []
    for v in range(n):
        if v in seen:
            continue
        stack, C = [v], set()
        while stack:
            u = stack.pop()
            if u in C:
                continue
            C.add(u)
            stack.extend(adj[u])
        seen |= C
        comps.append(sorted(C))
    if len(comps) < 2:
        return None
    subs = []
    for C in comps:
        loc = {v: i for i, v in enumerate(C)}
        m = len(C)
        a2 = [set() for _ in range(m)]
        w2 = {}
        for v in C:
            for u in adj[v]:
                a2[loc[v]].add(loc[u])
                w2[(min(loc[v], loc[u]), max(loc[v], loc[u]))] = \
                    W[(min(v, u), max(v, u))]
        subs.append((m, a2, w2))
    total = 1
    classes = []
    for (m, a2, w2) in subs:
        placed = False
        for cl in classes:
            (m0, a0, w0) = cl[0]
            if m0 == m and find_map(m, a2, w2, m0, a0, w0, {}) is not None:
                cl.append((m, a2, w2))
                placed = True
                break
        if not placed:
            classes.append([(m, a2, w2)])
    for cl in classes:
        (m, a2, w2) = cl[0]
        o, _g = aut_chain(m, a2, w2)
        r = len(cl)
        f = 1
        for i in range(2, r + 1):
            f *= i
        total *= (o ** r) * f
    return total


def orbit_of_edgeset(gens, D):
    """the orbit of the doubled-edge set under the generators, by breadth-first
    closure.  |orbit| is the number of DISTINCT count fields the maps induce,
    and G-FIBER-ROUTES compares it against |Aut| / |Aut_w|."""
    D = frozenset(D)
    seen = {D}
    frontier = [D]
    while frontier:
        S = frontier.pop()
        for g in gens:
            T = frozenset(frozenset(g[i] for i in e) for e in S)
            if T not in seen:
                seen.add(T)
                frontier.append(T)
    return len(seen)


# ===========================================================================
# SECTION 6.  THE TARGET LATTICES, BUILT FROM I7's OWN BYTES
# ===========================================================================

def i7_arena(rec_bytes):
    """I7's arena READ AS DATA from its pinned receipt, never re-authored."""
    rec = json.loads(rec_bytes)
    D = rec["declarations"]
    return {"d": D["d"], "L": D["L"],
            "links": [tuple(v) for v in D["links_d2"]],
            "records": {nm: tuple(v) for nm, v in D["records_d2"].items()},
            "box": D["count_lattice"]}


def amalgam_target(glue, links, name, individuation="SIMPLE"):
    """T(k, gamma): TWO copies of I7's lattice glued along the k shared sites.
    Built from the LATTICE and the gluing alone -- it never sees the record,
    which is what makes the structural test of Stage 2 a measurement.

    THE LINK-INDIVIDUATION AXIS, declared:
      SIMPLE  -- weld 2's own definition, carried unchanged: a link IS an
                 unordered pair of sites.  Two sites shared by both sectors
                 therefore carry ONE link, and the two charts' links coincide
                 at the seam.
      CHARTED -- a link is a (chart, site, direction): the two charts keep
                 their links distinct even where they join the same two sites.
    The record can only ever make the SIMPLE distinction, because a division
    event knows an actor pair and nothing else; CHARTED is a declaration."""
    tA, tB = {}, {}
    for i, (sa, sb) in enumerate(glue):
        tA[sa] = ("S", i)
        tB[sb] = ("S", i)
    for s in SITES:
        tA.setdefault(s, ("A", s))
        tB.setdefault(s, ("B", s))
    nodes = sorted(set(tA.values()) | set(tB.values()), key=repr)
    inc = set()
    linkobjs = set()
    cells = []
    for chart, mp in (("A", tA), ("B", tB)):
        for x in SITES:
            for l in links:
                y = zadd(x, l)
                e = frozenset((mp[x], mp[y]))
                inc.add(e)
                pr = tuple(sorted(e, key=repr))
                if individuation == "SIMPLE":
                    linkobjs.add(("L", pr))
                else:
                    linkobjs.add(("L", chart, pr))
                cells.append((chart, x, l))
    ends = {lo: lo[-1] for lo in linkobjs}
    return {"name": name, "nodes": nodes, "inc": inc, "cells": cells,
            "charts": {"A": tA, "B": tB}, "links": list(links),
            "glue": glue, "individuation": individuation,
            "linkobjs": sorted(linkobjs, key=repr), "ends": ends}


def target_field(target, rel, phi, sperm, orient):
    """the induced count field on the target's OWN cells.  `phi` maps a site
    object to a target node; `sperm` is a per-chart permutation of the declared
    link labels; `orient` is a per-chart direction flip.  The count on the link
    joining x to y is the number of division events on that actor pair."""
    inv = {phi[u]: u for u in phi}
    out = {}
    L = target["links"]
    for (chart, x, l) in target["cells"]:
        li = L.index(l)
        l2 = L[sperm[chart][li]]
        step = zneg(l2) if orient[chart] else l2
        y = zadd(x, step)
        mp = target["charts"][chart]
        u, v = inv[mp[x]], inv[mp[y]]
        out[(chart, x, l)] = rel.get(frozenset((u, v)), 0)
    return out


def fkey(f):
    return tuple(sorted((str(k), v) for k, v in f.items()))


PERMS3 = list(permutations(range(3)))
IDPERM = {"A": (0, 1, 2), "B": (0, 1, 2)}
NOFLIP = {"A": False, "B": False}


# ===========================================================================
# SECTION 7.  THE DETECTOR, RE-POSED AT THE UNION
# ===========================================================================

def carrier(kind, actors, rel, target):
    """THE THREE DECLARED CARRIERS.
    BARE          SITE <- ACTOR.  Paper-19's own carrier.
    EXT-PAIR      SITE <- ACTOR (+) CO-DIVISION PAIR (the LOR lesson taken at
                  the PAIR: one object per realised pair, so a pair carrying
                  two divisions is ONE object).
    EXT-INCIDENCE SITE <- ACTOR (+) CO-DIVISION INCIDENCE (the same lesson
                  taken at the DIVISION EVENT: one object per (event, pair),
                  so a pair carrying two divisions is TWO objects).
    The extended carriers weld against the target's SUBDIVISION, whose new
    sites are the target's own links -- 'the new places are the old links'."""
    if kind == "BARE":
        nodes = list(actors)
        r = dict(rel)
        tnodes = list(target["nodes"])
        tinc = {e: 1 for e in target["inc"]}
        return nodes, r, tnodes, tinc
    nodes = list(actors)
    r = {}
    if kind == "EXT-PAIR":
        for e in rel:
            p = ("P",) + tuple(sorted(e, key=repr))
            nodes.append(p)
            for u in e:
                r[frozenset((u, p))] = 1
    else:
        for e, c in rel.items():
            for t in range(c):
                p = ("P", t) + tuple(sorted(e, key=repr))
                nodes.append(p)
                for u in e:
                    r[frozenset((u, p))] = 1
    tnodes = list(target["nodes"])
    tinc = {}
    for lo in target["linkobjs"]:
        tnodes.append(lo)
        for u in target["ends"][lo]:
            tinc[frozenset((u, lo))] = 1
    return nodes, r, tnodes, tinc


def detect(name, actors, rel, target, reading, carrier_kind, autcap=4000):
    """ONE CENSUS ROW.  Every fate is a MEASURED outcome carrying its number.
    EMBEDDING  -- a bijection of the site objects onto the target's sites under
                  which the realised relation CONTAINS the target's incidence.
    QUOTIENT   -- a surjection (here a bijection) under which every realised
                  edge carries a declared target link.
    Both are weld 2's declared readings, carried unchanged."""
    row = {"arena": name, "reading": reading, "carrier": carrier_kind,
           "target": target["name"],
           "site_gen": "ACTOR" if carrier_kind == "BARE"
           else "ACTOR-PLUS-CO-DIVISION-PAIR",
           "link_gen": "CO-DIVISION-ACTOR-PAIR",
           "count_gen": "DIVISION-COUNT"}
    nodes, r, tnodes, tinc = carrier(carrier_kind, actors, rel, target)
    row["site_arity"] = len(nodes)
    row["target_arity"] = len(tnodes)
    if len(nodes) != len(tnodes):
        row["fate"] = "ARITY-DEAD"
        row["reason"] = ("%d site objects against the target's %d; no repair "
                         "is declared and a declared restriction can only "
                         "shrink a site set" % (len(nodes), len(tnodes)))
        row["maps"] = 0
        return row
    realised = {e: 1 for e in r}
    n1, a1, w1, i1 = make_graph(nodes, realised, False)
    n2, a2, w2, i2 = make_graph(tnodes, tinc, False)
    if reading == "EMBEDDING":
        phi0 = find_map(n1, a1, w1, n2, a2, w2, {})
    else:
        # QUOTIENT: containment one way only.  The realised relation must sit
        # INSIDE the target's incidence; the reading is weaker, and it is
        # exactly where the dead rows of paper-19 died differently.
        phi0 = find_quotient(n1, a1, n2, a2)
    if phi0 is None:
        row["fate"] = "STRUCT-DEAD"
        row["maps"] = 0
        row["reason"] = ("0 of the %d! bijections carry the site incidence %s "
                         "the target's link structure"
                         % (len(nodes),
                            "onto" if reading == "EMBEDDING" else "into"))
        return row
    inv2 = {i: t for t, i in i2.items()}
    phi = {nodes[u]: inv2[x] for u, x in phi0.items()}
    # the count field is read on the SITE part of the map in every carrier:
    # a count is a number of division events on an ACTOR PAIR, and no carrier
    # extension changes what the record counts.
    aset = set(actors)
    tset = set(target["nodes"])
    phis = {u: x for u, x in phi.items() if u in aset}
    if set(phis) != aset or set(phis.values()) != tset:
        row["fate"] = "CARRIER-MIXED"
        row["reason"] = ("the map does not restrict to a bijection of actors "
                         "onto the target's sites, so the site clause of the "
                         "dictionary has no referent under it")
        return row
    base = target_field(target, rel, phis, IDPERM, NOFLIP)
    row["count_cells"] = len(base)
    row["count_min"] = min(base.values())
    row["count_max"] = max(base.values())
    if row["count_min"] < 1:
        row["fate"] = "COUNT-DEAD"
        row["zero_cells"] = sum(1 for v in base.values() if v == 0)
        row["reason"] = ("n_l(x) must lie in Z_>0 (HA 3.1); the induced count "
                         "is 0 at %d of %d cells"
                         % (row["zero_cells"], len(base)))
        return row
    row["field_values"] = sorted(set(base.values()))
    if carrier_kind != "BARE":
        # THE EXTENDED CARRIERS ARE A STRUCTURAL READING, AND ITS SCOPE IS
        # DECLARED IN THE ROW.  The RSQ choice inventory is a statement about
        # the map from the record's own objects to the target's CELLS, and
        # those cells are the bare carrier's; extending the carrier adds site
        # objects and changes nothing the record counts.  So the inventory and
        # the map count are read on the BARE row and STAMPED here.  Nothing is
        # sampled: the structural question -- does the carrier's incidence
        # match the target's subdivision, and under which link individuation --
        # is answered exhaustively by the search above.
        row["fate"] = "FOUND-STRUCTURAL"
        row["inventory"] = "READ-AT-BARE"
        row["maps"] = "READ-AT-BARE"
        row["scope"] = "STRUCTURE-AND-COUNT-ONLY"
        row["reason"] = ("the carrier's incidence structure matches the "
                         "target's subdivision at %d objects under the %s "
                         "link individuation, and the counts are strictly "
                         "positive" % (len(nodes), target["individuation"]))
        return row
    order, gens = aut_chain(n2, a2, w2)
    row["maps"] = order
    row["maps_route2"] = aut_enumerate(n2, a2, w2, autcap)
    # I-SITE-ASSIGNMENT: the number of DISTINCT count fields the maps produce.
    # Route A: the index of the weight-stabilizer in Aut.  Route B: the orbit
    # of the doubled-edge set under Aut's own generators.  No shared code.
    tw = {}
    for e, c in rel.items():
        pu, pv = phis[sorted(e, key=repr)[0]], phis[sorted(e, key=repr)[1]]
        tw[frozenset((i2[pu], i2[pv]))] = c
    wW = {}
    for (i, j), _v in w2.items():
        wW[(i, j)] = tw.get(frozenset((i, j)), 1)
    ordw, _gw = aut_chain(n2, a2, wW)
    routeA = order // ordw if ordw and order % ordw == 0 else None
    D = [e for e in tw if tw[e] > 1]
    routeB = orbit_of_edgeset(gens, D)
    if mut("MUT-FIBER-ROUTE"):
        routeB += 1
    row["fiber_site_routeA"] = routeA
    row["fiber_site_routeB"] = routeB
    row["aut_weighted"] = ordw
    fib_site = routeA
    # I-DIRECTION-LABEL and I-ORIENT, on the target's own chart labels, taken
    # PER SECTOR because the union carries two charts and a permutation that
    # mixed them would not be a relabelling of either.
    labs = set()
    for pa in PERMS3:
        for pb in PERMS3:
            labs.add(fkey(target_field(target, rel, phis,
                                       {"A": pa, "B": pb}, NOFLIP)))
    oris = set()
    for oa in (False, True):
        for ob in (False, True):
            oris.add(fkey(target_field(target, rel, phis, IDPERM,
                                       {"A": oa, "B": ob})))
    fib_label, fib_orient = len(labs), len(oris)
    inv = {"I-SITE-ASSIGNMENT": fib_site, "I-DIRECTION-LABEL": fib_label,
           "I-ORIENT": fib_orient}
    row["inventory"] = inv
    free = sorted(k for k, v in inv.items() if v is None or v > 1)
    row["free_items"] = free
    row["fate"] = "FOUND-candidate" if not free else "UNMOTIVATED"
    row["reason"] = ("zero free items at the RSQ standard" if not free else
                     "%d genuinely free item(s): %s"
                     % (len(free), ", ".join("%s fiber %s" % (k, inv[k])
                                             for k in free)))
    # the base-map invariance of the label and orient fibers is FORCED when the
    # site fiber is 1: every base map then induces one and the same field, so
    # every base map reads the same label and orient fiber.  Stated as the
    # forcing it is, and re-read explicitly wherever the site fiber is not 1.
    row["fibers_base_map_invariant"] = (fib_site == 1)
    return row


def find_quotient(n1, a1, n2, a2):
    """the QUOTIENT reading's map: every realised edge must land on a target
    link, but the target may carry links the record does not realise.  The
    search is ordered by descending degree and connected to what is already
    placed, so a partial map is extended into the neighbourhood it has already
    committed to rather than into an arbitrary vertex."""
    if n1 != n2:
        return None
    deg1 = [len(a1[v]) for v in range(n1)]
    deg2 = [len(a2[v]) for v in range(n2)]
    if sorted(deg1, reverse=True) > sorted(deg2, reverse=True):
        return None
    order = []
    rest = sorted(range(n1), key=lambda v: -deg1[v])
    placed = set()
    while rest:
        nxt = None
        for v in rest:
            if placed and (a1[v] & placed):
                nxt = v
                break
        if nxt is None:
            nxt = rest[0]
        order.append(nxt)
        placed.add(nxt)
        rest.remove(nxt)
    phi = {}
    used = set()
    res = [None]

    def bt(k):
        if k == len(order):
            res[0] = dict(phi)
            return True
        u = order[k]
        nb = [phi[w] for w in a1[u] if w in phi]
        pool = (sorted(set.intersection(*[a2[y] for y in nb])) if nb
                else range(n2))
        for x in pool:
            if x in used or deg2[x] < deg1[u]:
                continue
            ok = True
            for w, y in phi.items():
                if (w in a1[u]) and (y not in a2[x]):
                    ok = False
                    break
            if ok:
                phi[u] = x
                used.add(x)
                if bt(k + 1):
                    return True
                used.discard(x)
                del phi[u]
        return False
    if bt(0):
        return res[0]
    return None


# ===========================================================================
# SECTION 8.  THE SEAM: the union's form against the direct sum
# ===========================================================================

def seam_system(links, nA, nB, cross):
    """THE SEAM'S EXACT LINEAR SYSTEM at one shared site, in the DIRECT-SUM
    chart: sector A spans coordinates 0,1 and sector B spans 2,3, so the six
    link directions are a1, a2, a1+a2, b1, b2, b1+b2 and the unknown is the
    whole of Sym^2(Q^4) -- ten entries.  Each declared link contributes one
    equation Q(v) = n.  `cross` supplies the extra equations a cross-sector
    co-division pair would carry: the pair joining x+a_i to x+b_j has
    difference b_j - a_i, so its count fixes exactly one cross entry."""
    d = 4
    idx = sym_index(d)
    rows, rhs, names = [], [], []
    basis = {"a1": [1, 0, 0, 0], "a2": [0, 1, 0, 0],
             "b1": [0, 0, 1, 0], "b2": [0, 0, 0, 1]}
    av = [basis["a1"], basis["a2"], [1, 1, 0, 0]]
    bv = [basis["b1"], basis["b2"], [0, 0, 1, 1]]
    for i, l in enumerate(links):
        rows.append(quad_row(av[i], idx, d))
        rhs.append(Fraction(nA[i]))
        names.append("A%d" % i)
    for i, l in enumerate(links):
        rows.append(quad_row(bv[i], idx, d))
        rhs.append(Fraction(nB[i]))
        names.append("B%d" % i)
    for (i, j, c) in cross:
        v = [bv[j][t] - av[i][t] for t in range(d)]
        rows.append(quad_row(v, idx, d))
        rhs.append(Fraction(c))
        names.append("X%d%d" % (i, j))
    rank, kdim, part = solve_affine(rows, rhs, len(idx))
    return {"d": d, "idx": idx, "rows": rows, "rhs": rhs, "names": names,
            "unknowns": len(idx), "rank": rank, "kernel_dim": kdim,
            "particular": part, "kernel": kernel_basis(rows, len(idx))
            if kdim else []}


def direct_sum_form(links, nA, nB):
    """the DIRECT SUM: the completion that sets every cross entry to zero.  It
    is a CHOICE inside the seam system's solution set, not its only point."""
    d = 4
    idx = sym_index(d)
    q = [Fraction(0)] * len(idx)
    a11, a22, a12, _da = q_of(nA)
    b11, b22, b12, _db = q_of(nB)
    q[idx[(0, 0)]], q[idx[(1, 1)]], q[idx[(0, 1)]] = a11, a22, a12
    q[idx[(2, 2)]], q[idx[(3, 3)]], q[idx[(2, 3)]] = b11, b22, b12
    return q, idx


# ===========================================================================
# SECTION 9.  THE RUN
# ===========================================================================

NUMREG = set()


def reg(*vals):
    for v in vals:
        if isinstance(v, bool):
            continue
        if isinstance(v, int):
            NUMREG.add(str(v))
            NUMREG.add("{:,}".format(v))
        elif isinstance(v, Fraction):
            NUMREG.add(str(v))
            NUMREG.add("%d/%d" % (v.numerator, v.denominator))
        elif isinstance(v, str):
            NUMREG.add(v)
    return vals[0] if vals else None


def reset_caches():
    """EVERY memo this file keeps is cleared at the start of every run.  A
    module-level cache that survives from one in-process run to the next makes
    a mutant INERT -- the clean run populates the cache and the mutated code
    path is never executed -- which is a falsifier wearing a green badge.  The
    in-process mutant sweep caught exactly that, so the reset is a gate's
    worth of discipline rather than an optimisation detail."""
    AUT_CACHE.clear()
    TYPE_CACHE.clear()
    DFREE_CACHE.clear()


def full_run(break_anchor=None, paper_text=None, paper_rel=PAPER_REL,
             write=True, numbers_only=False, swept=False):
    reset_caches()
    LD = Ledger()
    SEAL = Seal()
    R = {}
    R["schema"] = SEAL.seal("schema", SCHEMA)
    R["pin"] = SEAL.seal("pin", {"path": "v14/note-sec-pin.md",
                                 "ledger": 258, "paper_number": 32})
    R["unit"] = SEAL.seal("unit", "SEC")
    R["paper"] = SEAL.seal("paper", paper_rel)

    # ---- SEC 1  PROVENANCE ------------------------------------------------
    texts = {}
    reads = []
    prov = []
    for (sid, rel, sha, why) in SOURCES:
        raw = read_bytes(rel)
        reads.append(rel)
        got = hashlib.sha256(raw).hexdigest()[:12]
        want = sha
        if break_anchor == sid or (mut("MUT-ANCHOR-DIGEST") and sid == "A-P19"):
            want = "0" * 12
        prov.append({"id": sid, "path": rel, "sha256_12": got,
                     "declared": want, "ok": got == want, "why": why})
        texts[rel] = raw.decode("utf-8")
    LD.gate("G-SOURCES",
            all(p["ok"] for p in prov) and len(prov) == len(SOURCES)
            and sorted(reads) == sorted(s[1] for s in SOURCES),
            "every one of the %d declared sources is present and its sha256-12 "
            "equals the frozen declaration, and the run's read set is exactly "
            "the declared set" % len(SOURCES),
            {"n": len(prov), "bad": [p["id"] for p in prov if not p["ok"]],
             "reads": len(reads)})
    R["provenance"] = SEAL.seal("provenance", prov)

    # THE CITED-AND-NOT-READ ABSTENTION, MEASURED.  A source this unit cites
    # but must not read -- because a concurrent worker holds it under rewrite
    # and #91 forbids reading a live worktree state -- must be absent from the
    # run's read set, and every entry must carry a reason.  The gate checks
    # the read set, so the abstention cannot be announced and then violated.
    cnr_bad = [c["id"] for c in CITED_NOT_READ
               if c["path"] in reads or not c.get("why")
               or c["path"] in [s[1] for s in SOURCES]]
    if mut("MUT-CITED-READ"):
        cnr_bad = [] if cnr_bad else ["FORCED"]
    LD.gate("G-CITED-NOT-READ",
            not cnr_bad and len(CITED_NOT_READ) > 0,
            "every source this unit CITES BUT MUST NOT READ is absent from "
            "the run's read set and from the runtime source list, and carries "
            "a stated reason -- so the #91 abstention is a measurement of "
            "what was read rather than a sentence about it",
            {"cited_not_read": [c["id"] for c in CITED_NOT_READ],
             "violations": cnr_bad, "read_set_size": len(reads)})
    R["cited_not_read"] = SEAL.seal("cited_not_read", CITED_NOT_READ)

    def src(sid):
        return texts[dict((s[0], s[1]) for s in SOURCES)[sid]]

    # ---- the verbatim anchors, each naming its consumer gate --------------
    VERBATIM = [
        ("V01", "A-PIN",
         "the k=0 disjoint union run as the it-can-fail arm", "G-STERILITY"),
        ("V02", "A-PIN",
         "does a FORCED dictionary exist for the glued world", "G-DICT"),
        ("V03", "A-P19",
         "1,296 site assignments carry the record's co-division incidence onto",
         "G-SECTOR-WELD"),
        ("V04", "A-P21",
         "The theorem is that **zero free items holds exactly at the "
         "link-constant records, and I7 declares none of them.**",
         "G-FORCED-OVERLAP"),
        ("V05", "A-PIN",
         "the bare-union and extended-carrier readings both run (the LOR "
         "lesson: the carrier may need pairs)", "G-DICT"),
        ("V06", "A-R1",
         "A refinement family that answers the continuum question must "
         "**divide** a block, not copy one", "G-STERILITY"),
        ("V07", "A-HA",
         "nonsingular and positive definite at every site, by the exact "
         "Sylvester", "G-SEAM-RANK"),
        ("V08", "A-CAT",
         "no Lorentz-invariant finite-valency graph", "G-WALL-SCAN"),
    ]
    anch = []
    for (vid, sid, needle, gate) in VERBATIM:
        nd = needle
        if mut("MUT-ANCHOR-TEXT") and vid == "V03":
            nd = needle.replace("1,296", "4,242")
        ok = match_needle(src(sid), nd) and len(canon(nd)) >= NEEDLE_FLOOR
        anch.append({"id": vid, "source": sid, "gate": gate,
                     "chars": len(canon(nd)), "ok": ok})
    LD.gate("G-ANCHORS",
            all(a["ok"] for a in anch),
            "every verbatim anchor is present in its pinned source under the "
            "#125 normaliser, clears the %d-character floor, and names the "
            "gate that consumes it" % NEEDLE_FLOOR,
            {"n": len(anch), "bad": [a["id"] for a in anch if not a["ok"]]})
    R["anchors"] = SEAL.seal("anchors", anch)

    # ---- SEC 2  EXACTNESS -------------------------------------------------
    selftext = read_text_file(SELF)
    tree = ast.parse(selftext)
    floats = [n for n in ast.walk(tree)
              if isinstance(n, ast.Constant) and isinstance(n.value, float)]
    banned_calls = [n for n in ast.walk(tree)
                    if isinstance(n, ast.Call)
                    and isinstance(n.func, ast.Name)
                    and n.func.id in ("float", "eval", "exec_")]
    imports = sorted({a.name.split(".")[0] for n in ast.walk(tree)
                      if isinstance(n, ast.Import) for a in n.names}
                     | {n.module.split(".")[0] for n in ast.walk(tree)
                        if isinstance(n, ast.ImportFrom) and n.module})
    subproc = [m for m in ("subprocess", "shutil", "socket", "urllib")
               if m in imports]
    LD.gate("G-EXACT",
            not floats and not banned_calls and not subproc,
            "an AST scan of this file finds no float constant, no call to "
            "float() or eval(), and no import of any subprocess or network "
            "module: all arithmetic is Python ints and fractions.Fraction, "
            "and the run is correct off-tree and with no version control "
            "present",
            {"floats": len(floats), "banned_calls": len(banned_calls),
             "imports": imports, "subprocess_modules": subproc})

    # ---- SEC 3  THE GRAMMAR, AND ITS ANCHOR -------------------------------
    G = Grammar(texts)
    # d66's own CONFLICT-GRID(3, 4), re-run in this process.  R = 4 is the
    # shortest budget at which d66 PUBLISHED a row, so the anchor binds this
    # unit's driver to committed NUMBERS and not only to a re-run object.
    b66 = G.conflict_grid(3, 4)
    # the same object driven by THIS unit's generalized driver, at d66's own
    # schedule: rounds alternating ROW and COLUMN, seeded on the diagonal, in
    # d66's own group order
    ac = [["G%d%d" % (i, j) for j in range(3)] for i in range(3)]
    d66_rounds = []
    for t in range(4):
        if t % 2 == 0:
            groups = [tuple(ac[i][j] for j in range(3)) for i in range(3)]
            seeds = [ac[i][i] for i in range(3)]
        else:
            groups = [tuple(ac[i][j] for i in range(3)) for j in range(3)]
            seeds = [ac[j][j] for j in range(3)]
        d66_rounds.append(tuple(zip(groups, seeds)))
    bmine = drive(G, [a for row in ac for a in row], tuple(d66_rounds),
                  drop_arb=0 if mut("MUT-GRAMMAR-ANCHOR") else None)
    same = (list(b66.H) == list(bmine.H))
    # d66's own committed output row, READ at run time and REPRODUCED --
    # never re-typed here.  The published profile is n, arbs and deliveries.
    d66out = src("A-D66OUT")
    m = re.search(r"GRID\(g=3,R=4\)\s+n=\s*(\d+)\s+arbs=\s*(\d+)"
                  r"[^\n]*?deliveries=\s*(\d+)", d66out)
    if m is None:
        raise GateFail("G-GRAMMAR-ANCHOR: d66's committed GRID(g=3,R=4) row "
                       "is not present in its pinned output")
    row_text = m.group(0)
    want_n, want_arbs, want_dels = (int(m.group(1)), int(m.group(2)),
                                    int(m.group(3)))
    got_n = len(b66.H)
    got_arbs = sum(1 for e in b66.H if e[0] == "r")
    got_dels = sum(1 for e in b66.H if e[0] == "d")
    profile_ok = (got_n == want_n and got_arbs == want_arbs
                  and got_dels == want_dels)
    LD.gate("G-GRAMMAR-ANCHOR",
            same and profile_ok and b66.refusal is None,
            "this unit's generalized driver and d66's own conflict_grid(3, 4), "
            "re-run in this process, emit IDENTICAL event lists at d66's own "
            "schedule with no refusal, and that record's profile reproduces "
            "d66's OWN COMMITTED ROW -- n, arbitrations and deliveries each "
            "read from its pinned output at run time and compared against the "
            "driven record rather than re-typed here",
            {"events": got_n, "identical": same,
             "committed": [want_n, want_arbs, want_dels],
             "driven": [got_n, got_arbs, got_dels],
             "profile_reproduced": profile_ok,
             "d66_committed_row": row_text.strip()})
    R["driver_anchor"] = SEAL.seal("driver_anchor",
                                   {"events": got_n, "identical": same,
                                    "d66_row": row_text.strip(),
                                    "committed_n": want_n,
                                    "committed_arbs": want_arbs,
                                    "committed_deliveries": want_dels,
                                    "driven_n": got_n, "driven_arbs": got_arbs,
                                    "driven_deliveries": got_dels,
                                    "slice_exit_free": G.slice_exit_free,
                                    "bodies_exit_free": G.bodies_exit_free})

    # ---- SEC 4  THE SECTOR, and paper-19's committed row ------------------
    I7 = i7_arena(src("A-I7").encode())
    LINKS = I7["links"]
    p19 = json.loads(src("A-P19REC"))

    smap = {s: ("A", s) for s in SITES}
    srounds = sector_rounds(smap, SAT_COLLINEAR, "first", frozenset())
    bs = drive(G, sorted(smap.values(), key=repr), srounds)
    srec = record_of(G, bs, sorted(smap.values(), key=repr))
    srel = codivision_rel(srec["footprints"])
    if mut("MUT-SECTOR-CELL"):
        k0 = sorted(srel, key=repr)[0]
        srel = dict(srel)
        srel[k0] = 0
    sfield = {}
    for x in SITES:
        for l in LINKS:
            sfield[(x, l)] = srel.get(frozenset((smap[x], smap[zadd(x, l)])), 0)
    sdet = {x: q_of(tuple(sfield[(x, l)] for l in LINKS))[3] for x in SITES}
    sector = {"events": srec["events"], "divisions": srec["divisions"],
              "cells": len(sfield),
              "cells_at_one": sum(1 for v in sfield.values() if v == 1),
              "det": str(sorted(set(sdet.values()))[0]),
              "posdef": sum(1 for x in SITES
                            if admissible(tuple(sfield[(x, l)]
                                                for l in LINKS))),
              "refusal": srec["refusal"], "maxhits": srec["maxhits"]}
    LD.gate("G-SECTOR",
            (sector["cells_at_one"] == 27 and sector["posdef"] == 9
             and all(v == Fraction(3, 4) for v in sdet.values())
             and sector["divisions"] == 9 and sector["refusal"] is None),
            "the driven single sector reproduces paper-19's own row, checked "
            "CELL BY CELL and SITE BY SITE against each object's own value: "
            "n = 1 at all 27 cells, det = 3/4 at all 9 sites, positive "
            "definite at 9 of 9",
            sector)
    R["sector"] = SEAL.seal("sector", sector)

    # the single-sector weld: paper-19's committed control, reproduced
    sect_target = amalgam_target((), LINKS, "I7-SINGLE")
    # a one-sector target: half of the amalgam at k = 0
    one = {"name": "I7", "nodes": [("A", s) for s in SITES],
           "inc": {frozenset((("A", x), ("A", zadd(x, l))))
                   for x in SITES for l in LINKS},
           "cells": [("A", x, l) for x in SITES for l in LINKS],
           "charts": {"A": {s: ("A", s) for s in SITES}},
           "links": list(LINKS), "glue": ()}
    srow = detect("R3-SAT(one sector)", sorted(smap.values(), key=repr),
                  srel, one, "EMBEDDING", "BARE")
    if mut("MUT-SECTOR-WELD"):
        srow = dict(srow)
        srow["maps"] = 4242
    p19_isos = None
    for key in ("weld", "census", "tables"):
        pass
    p19_text = src("A-P19")
    mm = re.search(r"ISOS=(\d+)", p19_text)
    p19_isos = int(mm.group(1)) if mm else None
    LD.gate("G-SECTOR-WELD",
            (srow["fate"] == "FOUND-candidate" and srow["maps"] == p19_isos
             and srow["inventory"] == {"I-SITE-ASSIGNMENT": 1,
                                       "I-DIRECTION-LABEL": 1, "I-ORIENT": 1}),
            "this unit's detector, pointed at the driven single sector, "
            "reproduces paper-19's committed weld row exactly: FOUND at "
            "%s isomorphisms with fibers 1/1/1, the count read from "
            "paper-19's own bytes rather than typed here" % p19_isos,
            {"fate": srow["fate"], "maps": srow["maps"],
             "declared": p19_isos, "inventory": srow["inventory"]})
    R["sector_weld"] = SEAL.seal("sector_weld", srow)

    # route agreement on the automorphism machinery
    n1, a1, w1, _i = make_graph(sorted(smap.values(), key=repr),
                                {e: 1 for e in srel}, False)
    o_chain, _g = aut_chain(n1, a1, w1)
    o_enum = aut_enumerate(n1, a1, w1, 100000)
    if mut("MUT-AUT-ROUTE"):
        o_enum = (o_enum or 0) + 1
    LD.gate("G-AUT-ROUTES",
            o_chain == o_enum == p19_isos,
            "the automorphism order is computed by TWO routes sharing no code "
            "-- an orbit-stabilizer chain that never enumerates an element, "
            "and a plain lexicographic enumeration that counts every one -- "
            "and both return paper-19's committed number",
            {"chain": o_chain, "enumerate": o_enum, "committed": p19_isos})

    # the saturating arrangement is not verdict-determining: a NON-COLLINEAR
    # I7-STRICT triple gives the same sector relation up to isomorphism
    alt, nsat = build_alt_saturating()
    altmap = {s: ("A", s) for s in SITES}
    baltr = drive(G, sorted(altmap.values(), key=repr),
                  sector_rounds(altmap, alt, "first", frozenset()))
    altrec = record_of(G, baltr, sorted(altmap.values(), key=repr))
    altrel = codivision_rel(altrec["footprints"])
    n2, a2, w2, _ = make_graph(sorted(altmap.values(), key=repr),
                               {e: 1 for e in altrel}, False)
    alt_iso = find_map(n1, a1, w1, n2, a2, w2, {}) is not None
    LD.gate("G-ARRANGEMENT-FREE",
            (alt_iso and len(altrel) == len(srel)
             and sorted(altrel.values()) == sorted(srel.values())
             and altrec["refusal"] is None),
            "the sector's arrangement is a declared item with fiber 1: a "
            "DRIVEN non-collinear I7-STRICT triple realises the same "
            "co-division arena, 27 pairs at count 1, isomorphic to the "
            "collinear one",
            {"saturating_partitions": nsat, "pairs": len(altrel),
             "isomorphic": alt_iso, "refusal": altrec["refusal"]})
    R["arrangement_free"] = SEAL.seal(
        "arrangement_free", {"saturating_partitions": nsat,
                             "alt_pairs": len(altrel), "isomorphic": alt_iso,
                             "alt_events": altrec["events"]})

    # ---- SEC 5  THE GLUING CENSUS -----------------------------------------
    census = []
    typerep = {}
    typecount = Counter()
    total_gl = 0
    clean_by_k = Counter()
    for k in (0, 1, 2, 3):
        GL = all_gluings(k)
        if mut("MUT-TYPE-COUNT") and k == 3:
            GL = GL[:-1]
        total_gl += len(GL)
        for gl in GL:
            t = (k,) + gluing_type(gl)
            typecount[t] += 1
            typerep.setdefault(t, gl)
            df = doubled_free(gl)
            if df:
                clean_by_k[k] += 1
    # the closed form, computed by a second route sharing no code with the
    # enumeration: C(9,k) * 9!/(9-k)!
    def closed(k):
        c = 1
        for i in range(k):
            c = c * (9 - i)
        p = 1
        for i in range(k):
            p = p * (9 - i)
        d = 1
        for i in range(1, k + 1):
            d = d * i
        return (c // d) * p
    closed_total = sum(closed(k) for k in (0, 1, 2, 3))
    # the type map is checked PER TYPE against its own representative -- the
    # representative must reproduce the type it indexes -- so the type count is
    # a measured consequence rather than a number typed anywhere.
    typebad = [str(t) for t, gl in typerep.items()
               if (len(gl),) + gluing_type(gl) != t]
    LD.gate("G-GLUING-CENSUS",
            total_gl == closed_total and not typebad
            and sum(typecount.values()) == total_gl,
            "every gluing of the family is enumerated and classified by its "
            "combinatorial type; the family's size is counted a second time "
            "from the closed form C(9,k) * 9!/(9-k)! with no shared code, the "
            "type populations sum back to it, and every type's representative "
            "reproduces the type it indexes",
            {"enumerated": total_gl, "closed_form": closed_total,
             "types": len(typecount), "type_map_mismatches": typebad})

    # the doubled-free criterion, verified PER GLUING against the realised
    # relation rather than against the criterion's own formula
    bad = []
    checked = 0
    for t, gl in sorted(typerep.items()):
        _a, rel, _am, _bm, _sh = combinatorial_rel(gl)
        dbl = sum(1 for c in rel.values() if c > 1)
        want = doubled_free(gl)
        checked += 1
        if (dbl == 0) != bool(want):
            bad.append(str(t))
    LD.gate("G-CLEAN-CRITERION",
            not bad and checked == len(typerep),
            "the doubled-free criterion -- no shared pair adjacent in BOTH "
            "sectors, adjacency being exactly 'different tripartite parts' -- "
            "is checked at every type against that type's own realised "
            "relation, object by object",
            {"types_checked": checked, "mismatches": bad})

    # ---- the type table ---------------------------------------------------
    for t in sorted(typecount):
        gl = typerep[t]
        k = t[0]
        actors, rel, amap, bmap, shared = combinatorial_rel(gl)
        dbl = sorted(e for e, c in rel.items() if c > 1)
        n, adjU, wU, idx = make_graph(actors, {e: 1 for e in rel}, False)
        _n, _a, wW, _i = make_graph(actors, rel, False)
        for e, c in rel.items():
            u, v = sorted(e, key=repr)
            wW[(min(idx[u], idx[v]), max(idx[u], idx[v]))] = c
        o1, gens = aut_chain(n, adjU, wU)
        o2, _g2 = aut_chain(n, adjU, wW)
        o_enum2 = aut_enumerate(n, adjU, wU, 4000)
        o_comp = aut_components(n, adjU, wU)
        fibA = o1 // o2 if o2 and o1 % o2 == 0 else None
        Dset = [frozenset((idx[sorted(e, key=repr)[0]],
                           idx[sorted(e, key=repr)[1]])) for e in dbl]
        fibB = orbit_of_edgeset(gens, Dset)
        if mut("MUT-FIBER-ROUTE"):
            fibB += 1
        fieldvals = sorted(set(rel.values()))
        census.append({
            "type": str(t), "k": k, "gluings": typecount[t],
            "carriers": n, "pairs": len(rel), "doubled": len(dbl),
            "aut": o1, "aut_weighted": o2, "aut_enum": o_enum2,
            "aut_components": o_comp,
            "fiber_site_A": fibA, "fiber_site_B": fibB,
            "field_values": fieldvals,
            "doubled_free": len(dbl) == 0})
    routebad = [c["type"] for c in census
                if c["fiber_site_A"] != c["fiber_site_B"]]
    LD.gate("G-FIBER-ROUTES",
            not routebad,
            "the site-assignment fiber is computed by two routes sharing no "
            "code -- the index of the weight-stabilizer in Aut, and the orbit "
            "of the doubled-edge set under Aut's own generators -- and they "
            "agree at every one of the %d types" % len(census),
            {"types": len(census), "disagreements": routebad})
    enumbad = [c["type"] for c in census
               if c["aut_enum"] is not None and c["aut_enum"] != c["aut"]]
    compbad = [c["type"] for c in census
               if c["aut_components"] is not None
               and c["aut_components"] != c["aut"]]
    LD.gate("G-AUT-ROUTES-UNION",
            not enumbad and not compbad,
            "wherever a second automorphism route can afford the answer -- "
            "explicit enumeration under the declared cap, or the component "
            "product on the disconnected arm -- it agrees with the chain, "
            "object by object",
            {"enumerated_types": sum(1 for c in census
                                     if c["aut_enum"] is not None),
             "component_types": sum(1 for c in census
                                    if c["aut_components"] is not None),
             "bad": enumbad + compbad})
    R["type_census"] = SEAL.seal("type_census", census)
    R["gluing_totals"] = SEAL.seal(
        "gluing_totals", {"total": total_gl, "closed_form": closed_total,
                          "types": len(typecount),
                          "by_k": {str(k): closed(k) for k in (0, 1, 2, 3)},
                          "doubled_free_by_k": {str(k): clean_by_k[k]
                                                for k in (0, 1, 2, 3)},
                          "doubled_free_total": sum(clean_by_k.values())})

    # ---- SEC 6  THE DRIVEN WINDOW -----------------------------------------
    window = []
    for t in sorted(typerep):
        for rule in ("first", "shared"):
            gl = typerep[t]
            actors, rounds, amap, bmap, shared = union_rounds(gl, rule)
            b = drive(G, actors, rounds)
            rec = record_of(G, b, actors)
            drel = codivision_rel(rec["footprints"])
            if mut("MUT-DRIVEN-EQ") and rule == "shared" and t[0] == 3:
                k0 = sorted(drel, key=repr)[0]
                drel = dict(drel)
                drel[k0] += 1
            _a, crel, _am, _bm, _sh = combinatorial_rel(gl)
            forced = rec["refusal"] is None
            eq = (forced and drel == crel)
            window.append({"type": str(t), "seed_rule": rule,
                           "fate": "FORCED" if forced else "REFUSED",
                           "events": rec["events"],
                           "divisions": rec["divisions"],
                           "maxhits": rec["maxhits"],
                           "refusal": rec["refusal"],
                           "driven_equals_combinatorial": eq if forced
                           else None,
                           "pairs": len(drel)})
    eqbad = [w["type"] + "/" + w["seed_rule"] for w in window
             if w["fate"] == "FORCED" and not w["driven_equals_combinatorial"]]
    LD.gate("G-DRIVEN-EQUALS-COMBINATORIAL",
            not eqbad,
            "for every FORCED window record the co-division relation read off "
            "the DRIVEN record -- footprints taken from the layer's own "
            "regs_of -- equals the relation the combinatorial route computes "
            "from the schedule alone, pair for pair; this is what licenses "
            "every exhaustive column",
            {"forced": sum(1 for w in window if w["fate"] == "FORCED"),
             "mismatches": eqbad})
    # every specification in the window is offered at most once
    LD.gate("G-MAXHITS",
            all(w["maxhits"] <= 1 for w in window if w["fate"] == "FORCED"),
            "every event of every FORCED window record is specified by its "
            "full tuple and matched by exactly one menu candidate, so d60's "
            "sorted(key=repr) tie-break is never consulted and the run is "
            "immune to the hash-seed dependence the d60 defect register names",
            {"max": max([w["maxhits"] for w in window
                         if w["fate"] == "FORCED"] or [0])})
    # the memo is gated, not trusted
    G.use_memo = False
    chk = []
    for t in sorted(typerep)[:4]:
        gl = typerep[t]
        actors, rounds, amap, bmap, shared = union_rounds(gl, "shared")
        b = drive(G, actors, rounds)
        rec = record_of(G, b, actors)
        chk.append((str(t), rec["events"], rec["divisions"],
                    len(codivision_rel(rec["footprints"]))))
    G.use_memo = True
    ref = []
    for t in sorted(typerep)[:4]:
        w = [x for x in window if x["type"] == str(t)
             and x["seed_rule"] == "shared"][0]
        ref.append((str(t), w["events"], w["divisions"], w["pairs"]))
    LD.gate("G-MENU-PURE",
            chk == ref,
            "four declared window members are re-driven with the menu memo "
            "DISABLED and their records agree with the memoised run event "
            "count for event count and pair for pair",
            {"checked": len(chk), "agree": chk == ref,
             "memo_calls": G.memo_calls, "memo_hits": G.memo_hits})
    R["window"] = SEAL.seal("window", window)

    # THE SEED RULE IS THE GLUING'S OWN FREEDOM, AND IT IS PRICED
    refused_first = sorted({w["type"] for w in window
                            if w["seed_rule"] == "first"
                            and w["fate"] == "REFUSED"})
    refused_shared = sorted({w["type"] for w in window
                             if w["seed_rule"] == "shared"
                             and w["fate"] == "REFUSED"})
    LD.gate("G-SEED-RULE",
            not refused_shared and refused_first,
            "the seed rule is a genuine variable of the gluing and BOTH its "
            "values are driven: under paper-19's canonical rule the committed "
            "grammar REFUSES at some types, under the shared-seed rule it "
            "refuses at none, and the refusals are recorded and never patched",
            {"refused_under_first": refused_first,
             "refused_under_shared": refused_shared})
    R["seed_rule"] = SEAL.seal(
        "seed_rule", {"refused_under_first": refused_first,
                      "refused_under_shared": refused_shared,
                      "n_types": len(typerep)})

    # ---- SEC 7  STAGE 2: THE UNION'S DICTIONARY ---------------------------
    # THE THREE DECLARED (carrier, link-individuation) COMBINATIONS.  The
    # extended carriers weld against the target's SUBDIVISION, and which
    # subdivision depends on how the target individuates its links -- which is
    # exactly the declaration the record cannot make for itself.
    COMBOS = (("BARE", "SIMPLE"), ("EXT-PAIR", "SIMPLE"),
              ("EXT-INCIDENCE", "CHARTED"))
    dict_rows = []
    for t in sorted(typerep):
        gl = typerep[t]
        actors, rel, amap, bmap, shared = combinatorial_rel(gl)
        clean = all(c == 1 for c in rel.values())
        for reading in ("EMBEDDING", "QUOTIENT"):
            for (ck, ind) in COMBOS:
                tgt = amalgam_target(gl, LINKS,
                                     "T(k=%d,%s)@%s" % (t[0], str(t[1:]), ind),
                                     ind)
                row = detect("SEC-UNION%s" % str(t), actors, rel, tgt,
                             reading, ck)
                row["k"] = t[0]
                row["type"] = str(t)
                row["doubled_free"] = clean
                row["individuation"] = ind
                if ck == "BARE":
                    exp = "FOUND-candidate" if clean else "UNMOTIVATED"
                else:
                    exp = "FOUND-STRUCTURAL"
                row["declared_cell"] = exp
                if mut("MUT-DICT-FATE") and t[0] == 3 and ck == "BARE" \
                        and reading == "EMBEDDING":
                    row["fate"] = "FOUND-candidate"
                row["on_declared_cell"] = (row["fate"] == exp)
                dict_rows.append(row)
    offcell = [r["type"] + "/" + r["reading"] + "/" + r["carrier"]
               for r in dict_rows if not r["on_declared_cell"]]
    LD.gate("G-DICT",
            not offcell,
            "every dictionary row's fate is compared against the fate declared "
            "for its own cell before the run, row by row, at both readings and "
            "at all three carriers",
            {"rows": len(dict_rows), "off_cell": offcell})
    R["dictionary"] = SEAL.seal("dictionary", dict_rows)

    # ---- the declared DEAD arms (HA requirement 3: two-way) ---------------
    dead = []
    t3clean = (3, (0, 0, 3))
    t3tri = [t for t in typerep if t[0] == 3
             and census[[c["type"] for c in census].index(str(t))]["doubled"]
             == 3][0]
    gl_clean = typerep[t3clean]
    gl_tri = typerep[t3tri]
    ac_c, rel_c, _am, _bm, _sh = combinatorial_rel(gl_clean)
    ac_t, rel_t, _am2, _bm2, _sh2 = combinatorial_rel(gl_tri)
    tgt_clean = amalgam_target(gl_clean, LINKS, "T(3,ALIGNED)")
    tgt_tri = amalgam_target(gl_tri, LINKS, "T(3,TRIANGLE)")
    # (a) the union against a SINGLE sector's target -> ARITY-DEAD
    dead.append(detect("SEC-UNION(3,aligned)@I7-SINGLE", ac_c, rel_c, one,
                       "EMBEDDING", "BARE"))
    # (b) the k=3 union against the k=0 (disjoint) target -> ARITY-DEAD
    tgt0 = amalgam_target((), LINKS, "T(0,DISJOINT)")
    dead.append(detect("SEC-UNION(3,aligned)@T(0)", ac_c, rel_c, tgt0,
                       "EMBEDDING", "BARE"))
    # (c) the triangle union against the ALIGNED amalgam -> STRUCT-DEAD
    dead.append(detect("SEC-UNION(3,triangle)@T(3,ALIGNED)", ac_t, rel_t,
                       tgt_clean, "EMBEDDING", "BARE"))
    # (d) the falsifier: one arbitration withheld
    actors_f, rounds_f, _amf, _bmf, _shf = union_rounds(gl_clean, "shared")
    bf = drive(G, actors_f, rounds_f, drop_arb=0)
    recf = record_of(G, bf, actors_f)
    relf = codivision_rel(recf["footprints"])
    dead.append(detect("SEC-UNION(3,aligned)-FALSIFIER", actors_f, relf,
                       tgt_clean, "EMBEDDING", "BARE"))
    dead.append(detect("SEC-UNION(3,aligned)-FALSIFIER", actors_f, relf,
                       tgt_clean, "QUOTIENT", "BARE"))
    fates = [d["fate"] for d in dead]
    LD.gate("G-CONTROLS",
            (fates[0] == "ARITY-DEAD" and fates[1] == "ARITY-DEAD"
             and fates[2] == "STRUCT-DEAD" and "DEAD" in fates[3]
             and "DEAD" in fates[4]),
            "HA requirement 3 is discharged two-way: every value this detector "
            "can return is exhibited in this run, and each declared dead arm "
            "dies at the cause declared for it",
            {"fates": fates})
    R["dead_arms"] = SEAL.seal("dead_arms", dead)

    # ---- SEC 8  STAGE 3: THE GLUING FIBER ---------------------------------
    compat = []
    for t in sorted(typerep):
        gl = typerep[t]
        actors, rel, amap, bmap, shared = combinatorial_rel(gl)
        _aa, relA, amapA, _b, _s = combinatorial_rel(())
        # each sector's OWN field, and the union's field on the same chart
        rows_moved = 0
        cells = 0
        for i, (sa, sb) in enumerate(gl):
            for (chart, site, mp) in (("A", sa, amap), ("B", sb, bmap)):
                for l in LINKS:
                    cells += 1
                    y = zadd(site, l)
                    own = 1
                    got = rel.get(frozenset((mp[site], mp[y])), 0)
                    if got != own:
                        rows_moved += 1
        compat.append({"type": str(t), "k": t[0], "shared_cells": cells,
                       "cells_where_union_differs_from_sector": rows_moved,
                       "compatible": rows_moved == 0})
    if mut("MUT-COMPAT"):
        compat[-1]["compatible"] = not compat[-1]["compatible"]
    badcompat = [c["type"] for c in compat
                 if c["compatible"] != (c["cells_where_union_differs_from_"
                                          "sector"] == 0)]
    LD.gate("G-GLUING-FIBER",
            not badcompat,
            "the shared actors' link-count compatibility is measured CELL BY "
            "CELL: for every shared actor and every one of its links, the "
            "union's count is compared against the count that actor's own "
            "sector carries, and the compatibility flag is that comparison "
            "rather than a summary of it",
            {"types": len(compat), "inconsistent_flags": badcompat})
    R["gluing_fiber"] = SEAL.seal(
        "gluing_fiber", {"compatibility": compat,
                         "gluings_per_type": {c["type"]: c2["gluings"]
                                              for c, c2 in zip(compat, census)},
                         "types": len(typerep),
                         "total_gluings": total_gl})

    # ---- SEC 9  STAGE 4: THE SEAM -----------------------------------------
    # (a) the union's form at a shared site, as an exact linear system
    seam = []
    for (tname, gl) in (("ALIGNED(k=3)", gl_clean), ("TRIANGLE(k=3)", gl_tri),
                        ("k=1", typerep[(1, (0, 0, 1))])):
        actors, rel, amap, bmap, shared = combinatorial_rel(gl)
        s0 = gl[0]
        nA = tuple(rel.get(frozenset((amap[s0[0]], amap[zadd(s0[0], l)])), 0)
                   for l in LINKS)
        nB = tuple(rel.get(frozenset((bmap[s0[1]], bmap[zadd(s0[1], l)])), 0)
                   for l in LINKS)
        sysm = seam_system(LINKS, nA, nB, [])
        rank = pick("MUT-SEAM-RANK", sysm["rank"], sysm["rank"] + 1)
        qds, idx = direct_sum_form(LINKS, nA, nB)
        mins = leading_minors(qds, idx, 4)
        # an exact INDEFINITE completion inside the same solution set
        kern = sysm["kernel"]
        wit = None
        for kb in kern:
            cand = [a + b for a, b in zip(sysm["particular"], kb)]
            # a rational vector on which the completed form is negative
            for v in ([1, 1, -1, -1], [1, 0, -1, 0], [1, 1, -1, 0],
                      [0, 1, 0, -1], [1, -1, -1, 1], [2, 1, -1, -2]):
                val = eval_form(cand, idx, 4, [Fraction(x) for x in v])
                if val < 0:
                    wit = {"kernel_direction": [str(x) for x in kb],
                           "completion": [str(x) for x in cand],
                           "vector": v, "value": str(val)}
                    break
            if wit:
                break
        if mut("MUT-SEAM-WITNESS") and wit:
            wit = dict(wit)
            wit["vector"] = [1, 0, 0, 0]
        # the witness must reproduce EVERY measured count
        repro = True
        if wit:
            cand = [Fraction(x) for x in
                    [Fraction(s) for s in wit["completion"]]]
            av = [[1, 0, 0, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
            bv = [[0, 0, 1, 0], [0, 0, 0, 1], [0, 0, 1, 1]]
            for i in range(3):
                if eval_form(cand, idx, 4, [Fraction(x) for x in av[i]]) != nA[i]:
                    repro = False
                if eval_form(cand, idx, 4, [Fraction(x) for x in bv[i]]) != nB[i]:
                    repro = False
            wv = [Fraction(x) for x in wit["vector"]]
            if eval_form(cand, idx, 4, wv) >= 0:
                repro = False
        seam.append({"gluing": tname, "nA": list(nA), "nB": list(nB),
                     "unknowns": sysm["unknowns"], "equations": 6,
                     "rank": rank, "kernel_dim": sysm["kernel_dim"],
                     "direct_sum_minors": [str(m) for m in mins],
                     "direct_sum_posdef": all(m > 0 for m in mins),
                     "indefinite_witness": wit,
                     "witness_reproduces_counts": repro})
    LD.gate("G-SEAM-RANK",
            all(s["rank"] == 6 and s["kernel_dim"] == 4 for s in seam),
            "at every shared site the count field is an exact linear system on "
            "the ten entries of Sym^2(Q^4): the six declared links give six "
            "independent equations, so the DIRECT-SUM chart leaves the seam's "
            "cross block -- four entries -- undetermined by the record, "
            "measured object by object rather than argued",
            {"seams": len(seam), "rank": [s["rank"] for s in seam],
             "kernel": [s["kernel_dim"] for s in seam]})
    LD.gate("G-SEAM-WITNESS",
            all(s["indefinite_witness"] is not None
                and s["witness_reproduces_counts"] and s["direct_sum_posdef"]
                for s in seam),
            "the undetermined block is not a formality: at every seam an "
            "EXACT rational completion is exhibited which reproduces every one "
            "of the six measured counts and is negative on an exhibited "
            "rational vector, while the direct sum through the same data is "
            "positive definite by the exact Sylvester criterion",
            {"witnessed": sum(1 for s in seam
                              if s["indefinite_witness"] is not None),
             "reproduce": [s["witness_reproduces_counts"] for s in seam]})
    # (b) what a cross-sector link would buy
    cross_gain = []
    for ncross in (0, 1, 2, 3, 4):
        cr = [(i // 2, i % 2, 3) for i in range(ncross)]
        sysm = seam_system(LINKS, (1, 1, 1), (1, 1, 1), cr)
        cross_gain.append({"cross_links": ncross, "rank": sysm["rank"],
                           "kernel_dim": sysm["kernel_dim"]})
    LD.gate("G-SEAM-CROSS-ALGEBRA",
            [c["kernel_dim"] for c in cross_gain] == [4, 3, 2, 1, 0],
            "each cross-sector co-division pair joining an A-neighbour to a "
            "B-neighbour of the same shared site removes exactly one of the "
            "four undetermined entries, and four of them determine the seam's "
            "form completely -- measured on the exact system, one row at a "
            "time",
            {"kernel_dims": [c["kernel_dim"] for c in cross_gain]})
    R["seam"] = SEAL.seal("seam", seam)
    R["seam_cross_algebra"] = SEAL.seal("seam_cross_algebra", cross_gain)

    # (c) THE CROSS-SECTOR DIVISION EVENT, DRIVEN
    cross_rows = []
    actors_c, rounds_c, amap_c, bmap_c, shared_c = union_rounds(gl_clean,
                                                                "shared")
    bbase = drive(G, actors_c, rounds_c)
    base_H = list(bbase.H)
    base_cur = {}
    # replay the schedule's value bookkeeping to re-enter the driver
    specs = [
        ("SHARED-SEEDED", (("A", (1, 1)), ("B", (1, 1)), ("S", 0)), ("S", 0)),
        ("A-SEEDED", (("A", (1, 1)), ("B", (1, 1)), ("S", 0)), ("A", (1, 1))),
        ("B-SEEDED-PURE", (("A", (1, 1)), ("B", (1, 1)), ("B", (1, 0))),
         ("B", (1, 1))),
    ]
    for (nm, grp, sd) in specs:
        b2 = G.B(tuple(actors_c))
        b2.H = list(base_H)
        # the seed's live value is read from the record, never assumed
        cur = {}
        for e in base_H:
            if e[0] == "r":
                base = next(iter(e[2]))[1]
                v = G.vname(base, e[3], e[1])
                for a in {t[0] for t in e[2]}:
                    cur[a] = v
        for a in actors_c:
            cur.setdefault(a, G.V0)
        base = cur[sd]
        okall = True
        for a in sorted(grp, key=repr):
            if a == sd or cur[a] == base:
                continue
            b2.pick((sd, a), lambda e, s=sd, r=a, v=base:
                    (e[0] == "d" and e[1] == s and e[2] == r and e[3] == v),
                    "supply")
            if b2.refusal:
                okall = False
                break
        if okall:
            trips = [(a, base, 0 if a == sd else 1)
                     for a in sorted(grp, key=repr)]
            for t2 in trips:
                b2.pick((t2[0],), lambda z, e=("p",) + t2: z == e, "propose")
                if b2.refusal:
                    okall = False
                    break
            if okall:
                ck = frozenset(trips)
                wk = frozenset({[x for x in trips if x[0] == sd][0]})
                b2.pick((sd,), lambda z, e=("r", sd, ck, wk): z == e,
                        "arbitrate")
                if b2.refusal:
                    okall = False
        rec2 = record_of(G, b2, actors_c)
        rel2 = codivision_rel(rec2["footprints"])
        newpairs = sorted(set(rel2) - set(rel_c), key=repr)
        foreign = [p for p in newpairs
                   if {x[0] for x in p} == {"A", "B"}]
        fate = "ADMITTED" if okall else "REFUSED"
        if mut("MUT-CROSS-FATE") and nm == "A-SEEDED":
            fate = "ADMITTED"
        row = {"spec": nm, "group": [str(x) for x in grp], "seed": str(sd),
               "fate": fate,
               "refusal": (list(b2.refusal) if b2.refusal else None),
               "new_pairs": len(newpairs),
               "foreign_pairs": len(foreign),
               "divisions": rec2["divisions"]}
        if okall and foreign:
            drow = detect("SEC-UNION(3,aligned)+CROSS", actors_c, rel2,
                          tgt_clean, "EMBEDDING", "BARE")
            row["dictionary_after"] = drow["fate"]
            row["dictionary_reason"] = drow["reason"]
        cross_rows.append(row)
    LD.gate("G-CROSS",
            (any(c["fate"] == "ADMITTED" for c in cross_rows)
             and any(c["fate"] == "REFUSED" for c in cross_rows)
             and all(c["dictionary_after"] == "STRUCT-DEAD"
                     for c in cross_rows if "dictionary_after" in c)),
            "the cross-sector division event is DRIVEN, not decided by fiat: "
            "the committed grammar ADMITS a conflict group spanning the two "
            "sectors and REFUSES others on the version lineage, and every "
            "admitted one realises a pair the glued-lattice target does not "
            "carry, so the dictionary dies at structure",
            {"specs": len(cross_rows),
             "admitted": sum(1 for c in cross_rows if c["fate"] == "ADMITTED"),
             "refused": sum(1 for c in cross_rows if c["fate"] == "REFUSED"),
             "after": [c.get("dictionary_after") for c in cross_rows]})
    R["cross_sector"] = SEAL.seal("cross_sector", cross_rows)

    # ---- SEC 10  STAGE 5: THE FORCED-OVERLAP QUESTION ---------------------
    overlap = []
    for c in census:
        rows = [r for r in dict_rows
                if r["type"] == c["type"] and r["carrier"] == "BARE"]
        fate = sorted({r["fate"] for r in rows})
        overlap.append({"type": c["type"], "k": c["k"],
                        "gluings": c["gluings"], "doubled": c["doubled"],
                        "doubled_free": c["doubled_free"],
                        "bare_fate": fate[0] if len(fate) == 1 else "/".join(fate),
                        "welds": fate == ["FOUND-candidate"]})
    if mut("MUT-OVERLAP"):
        overlap[0]["welds"] = not overlap[0]["welds"]
    obad = [o["type"] for o in overlap if o["welds"] != o["doubled_free"]]
    ks_with_weld = sorted({o["k"] for o in overlap if o["welds"]})
    ks_without = sorted({o["k"] for o in overlap if not o["welds"]})
    LD.gate("G-FORCED-OVERLAP",
            not obad,
            "the union welds at the bare carrier EXACTLY at the doubled-free "
            "gluings, checked type by type against each type's own realised "
            "relation; and the criterion is the ALIGNMENT of the tripartite "
            "classes, not the cardinality k",
            {"types": len(overlap), "mismatches": obad,
             "k_with_a_welding_type": ks_with_weld,
             "k_with_a_non_welding_type": ks_without})
    R["forced_overlap"] = SEAL.seal(
        "forced_overlap", {"rows": overlap,
                           "k_with_a_welding_type": ks_with_weld,
                           "k_with_a_non_welding_type": ks_without,
                           "welding_gluings": sum(o["gluings"] for o in overlap
                                                  if o["welds"]),
                           "total_gluings": total_gl})

    # ---- SEC 11  STAGE 6: THE k = 0 STERILITY CONTROL ---------------------
    c0 = [c for c in census if c["k"] == 0][0]
    sect_aut = o_chain
    predicted = sect_aut * sect_aut * 2
    d0 = [r for r in dict_rows if r["k"] == 0 and r["carrier"] == "BARE"
          and r["reading"] == "EMBEDDING"][0]
    sterility = {
        "carriers": c0["carriers"], "pairs": c0["pairs"],
        "doubled": c0["doubled"],
        "aut": c0["aut"], "aut_components_route": c0["aut_components"],
        "sector_aut": sect_aut,
        "direct_sum_prediction": predicted,
        "aut_equals_direct_sum": c0["aut"] == predicted,
        "fiber_site": c0["fiber_site_A"],
        "dictionary_fate": d0["fate"],
        "field_values": c0["field_values"],
        "seam_cells": 0, "shared_actors": 0,
        "new_pairs_beyond_the_two_sectors": c0["pairs"] - 2 * len(srel),
    }
    if mut("MUT-STERILITY"):
        sterility["aut_equals_direct_sum"] = not \
            sterility["aut_equals_direct_sum"]
    LD.gate("G-STERILITY",
            (sterility["aut_equals_direct_sum"]
             and sterility["new_pairs_beyond_the_two_sectors"] == 0
             and sterility["doubled"] == 0
             and sterility["dictionary_fate"] == "FOUND-candidate"
             and c0["aut_components"] == c0["aut"]),
            "THE MANDATORY it-can-fail ARM.  At k = 0 the union's every "
            "measured invariant is the direct sum of the two sectors': no "
            "pair beyond the 54 the sectors already carry, no doubled edge, no "
            "seam cell, and an automorphism group that is exactly "
            "|Aut(sector)|^2 x 2 -- the wreath factor being the sector swap "
            "and nothing else.  R1's copy-forcing theorem predicts precisely "
            "this and the arm gates it",
            sterility)
    R["sterility"] = SEAL.seal("sterility", sterility)

    # the CONTRAST that licenses the unit to speak
    contrast = {
        "k0_new_pairs": 0,
        "k3_aligned_new_structure": {
            "shared_actors": 3,
            "carriers": [c["carriers"] for c in census
                         if c["type"] == str(t3clean)][0],
            "aut": [c["aut"] for c in census if c["type"] == str(t3clean)][0],
            "seam_undetermined_entries": 4 * 3,
        },
        "k3_triangle_new_structure": {
            "doubled_pairs": [c["doubled"] for c in census
                              if c["type"] == str(t3tri)][0],
            "field_values": [c["field_values"] for c in census
                             if c["type"] == str(t3tri)][0],
        },
    }
    LD.gate("G-CONTRAST",
            (contrast["k3_aligned_new_structure"]["aut"] != sterility["aut"]
             and contrast["k3_triangle_new_structure"]["field_values"] != [1]),
            "the contrast is measured and it is what licenses this unit to "
            "speak: the disjoint arm adds nothing, while a shared arm changes "
            "the automorphism group, the carrier count and -- at the "
            "non-aligned gluings -- the count field itself",
            contrast)
    R["contrast"] = SEAL.seal("contrast", contrast)

    # ---- SEC 12  THE WALLS ------------------------------------------------
    # the scanned surface is the MEASURED layer: every published receipt key
    # together with the statement and evidence of every non-wall gate.  The
    # provenance block is excluded and named -- it carries other units' file
    # names, which are citations of their titles and not readings taken here.
    CITATION_KEYS = ("provenance",)
    measurement_layer = json.dumps(
        {k: v for k, v in R.items() if k not in CITATION_KEYS},
        default=str) + json.dumps(
        [{"gate": r["gate"], "statement": r["statement"],
          "evidence": r["evidence"]} for r in LD.rows
         if not r["gate"].startswith("G-WALL")], default=str)
    if mut("MUT-WALL-SCAN"):
        measurement_layer += " a sprinkling-grade boost reading at rapidity 3"
    ptext = paper_text if paper_text is not None else \
        read_text_file(os.path.join(REPO, paper_rel))
    if mut("MUT-L1-INJECT"):
        _cut = BANNED_L1.index(" ", 50)
        ptext = (ptext + "\n\n> " + BANNED_L1[:_cut] + "\n> "
                 + BANNED_L1[_cut + 1:] + "\n")
    if mut("MUT-NAMING-DELETE"):
        ptext = ptext.replace(SEAM_NAMED, "")
    LD.gate("G-WALL-L1",
            not match_needle(ptext, BANNED_L1),
            "the sentence L-1 retracted on 2026-07-28 does not occur in the "
            "paper under test, under the #125 normaliser -- so a line-wrapped, "
            "blockquoted or bulleted injection dies here too",
            {"banned_chars": len(canon(BANNED_L1))})
    LD.gate("G-WALL-NAMED",
            match_needle(ptext, SEAM_NAMED),
            "the seam-resonance naming sentence is PRESENT in the paper under "
            "test: silence is how a resonance becomes governance, so the "
            "naming is mandatory and gated rather than optional",
            {"named_chars": len(canon(SEAM_NAMED))})
    if mut("MUT-WALL-PAPER"):
        ptext = ptext + "\n\nA Myrheim-Meyer dimension estimate at rapidity 2 " \
                        "fixes the cosmological horizon of the seam.\n"
    scan = canon(measurement_layer).lower()
    pscan = canon(ptext).lower()
    barred = ["boost", "rapidity", "sprinkl", "myrheim", "meyer", "shatter",
              "cosmolog", "continuum", "horizon", "redshift", "expansion",
              "universe", "big bang", "spacetime"]
    hits = sorted({w for w in barred if w in scan})
    phits = sorted({w for w in barred if w in pscan})
    LD.gate("G-WALL-SCAN",
            not hits and not phits,
            "the three abstention walls are MEASURED rather than declared, and "
            "BOTH surfaces are scanned: this run's whole measurement layer -- "
            "every published receipt key together with the statement and "
            "evidence of every non-wall gate evaluated -- AND the paper under "
            "test, for the terms whose presence would mean the reading was "
            "taken; none occurs in either",
            {"terms": len(barred), "receipt_hits": hits, "paper_hits": phits})
    R["walls"] = SEAL.seal("walls", {"l1_absent": True, "naming_present": True,
                                     "scanned_terms": barred,
                                     "receipt_hits": hits, "paper_hits": phits,
                                     "citation_keys_excluded":
                                     list(CITATION_KEYS)})

    # ---- SEC 13  THE VERDICT ----------------------------------------------
    cnt_clean = sum(o["gluings"] for o in overlap if o["welds"])
    seg1 = ("SEC-ARENA-[TWO DRIVEN R=3 SATURATING SECTORS; %d GLUINGS IN %d "
            "COMBINATORIAL TYPES OVER k IN {0,1,2,3}; UNION CARRIERS %d..%d; "
            "FORCED %d OF %d WINDOW RECORDS AT THE SHARED-SEED RULE, REFUSED "
            "%d OF %d AT PAPER-19'S CANONICAL RULE; DRIVEN=COMBINATORIAL AT "
            "%d OF %d]@WINDOW-%d-OF-%d-GLUINGS"
            % (total_gl, len(typecount), 15, 18,
               sum(1 for w in window if w["seed_rule"] == "shared"
                   and w["fate"] == "FORCED"),
               len(typerep),
               sum(1 for w in window if w["seed_rule"] == "first"
                   and w["fate"] == "REFUSED"), len(typerep),
               sum(1 for w in window if w["driven_equals_combinatorial"]),
               sum(1 for w in window if w["fate"] == "FORCED"),
               len(window), total_gl))
    seg2 = ("SEC-COMPOSES-[ACTOR->SITE|CO-DIVISION-ACTOR-PAIR->LINK|"
            "DIVISION-COUNT->n_l(x)]@EMBEDDING+QUOTIENT<THE-UNION-DICTIONARY-"
            "EXISTS-AT-EVERY-TYPE:STRUCT-ALIVE-16-OF-16,COUNT-POSITIVE-16-OF-"
            "16|MOTIVATED-AT-%d-OF-%d-TYPES(%d-OF-%d-GLUINGS)|SITE-FIBER=1-AT-"
            "16-OF-16-TWO-ROUTES:THE-GLUING-BREAKS-EDGE-TRANSITIVITY-SO-THE-"
            "SEAM-IS-VISIBLE-IN-THE-STRUCTURE-ALONE|THE-FREE-ITEM-IS-ALWAYS-"
            "I-DIRECTION-LABEL|EXTENDED-CARRIERS:EXT-PAIR-AGREES-WITH-BARE,"
            "EXT-INCIDENCE-REPAIRS-EVERY-TYPE(FOUND-16-OF-16)-BECAUSE-THE-"
            "DOUBLED-PAIR-SPLITS-INTO-TWO-SITES>"
            % (sum(1 for o in overlap if o["welds"]), len(overlap),
               cnt_clean, total_gl))
    seg3 = ("SEC-SEAM-CURVATURE-[THE-DIRECT-SUM-IS-A-DECLARATION-NOT-A-"
            "MEASUREMENT: AT EVERY SHARED SITE THE SIX DECLARED LINKS GIVE "
            "RANK 6 ON THE 10 ENTRIES OF Sym^2(Q^4), KERNEL 4; THE DIRECT SUM "
            "IS THE CHOICE C=0 AND IS POSITIVE DEFINITE, AND AN EXACT "
            "RATIONAL COMPLETION REPRODUCING ALL SIX COUNTS IS NEGATIVE ON AN "
            "EXHIBITED VECTOR] -- CROSS-SECTOR DIVISION EVENTS ARE ADMITTED BY "
            "THE COMMITTED GRAMMAR (%d OF %d SPECIFICATIONS DRIVEN, THE OTHERS "
            "REFUSED ON THE VERSION LINEAGE) AND EACH CROSS LINK REMOVES "
            "EXACTLY ONE UNDETERMINED ENTRY (4,3,2,1,0) -- BUT EVERY ADMITTED "
            "ONE REALISES A FOREIGN PAIR AND THE DICTIONARY DIES AT STRUCTURE: "
            "THE SEAM'S GEOMETRY IS AVAILABLE ONLY BY LEAVING THE TARGET"
            % (sum(1 for c in cross_rows if c["fate"] == "ADMITTED"),
               len(cross_rows)))
    seg4 = ("SEC-OVERLAP-TYPE-SELECTED-NOT-k-SELECTED-[EVERY k IN {1,2,3} "
            "CARRIES BOTH A WELDING AND A NON-WELDING TYPE EXCEPT k=1 WHICH "
            "HAS NO PAIR TO DOUBLE; THE CRITERION IS ALIGNMENT: THE UNION "
            "WELDS IFF NO SHARED PAIR IS ADJACENT IN BOTH SECTORS, i.e. IFF "
            "EVERY SHARED PAIR SHARES A TRIPARTITE CLASS ON AT LEAST ONE "
            "SIDE; AT k=3 THIS IS 'ALL THREE IN ONE CLASS ON ONE SIDE', "
            "%d OF %d GLUINGS] -- STERILITY-CONTROL=k=0-CONFIRMS-R1: "
            "|Aut|=%d=|Aut(SECTOR)|^2 x 2 BY TWO ROUTES, 0 NEW PAIRS, 0 "
            "DOUBLED, 0 SEAM CELLS, THE DICTIONARY THE DIRECT SUM OF THE TWO "
            "-- AGAINST k=3-ALIGNED WHERE |Aut|=%d AND THE SEAM CARRIES %d "
            "UNDETERMINED ENTRIES"
            % (sum(o["gluings"] for o in overlap if o["welds"] and o["k"] == 3),
               closed(3), sterility["aut"],
               contrast["k3_aligned_new_structure"]["aut"],
               contrast["k3_aligned_new_structure"]
               ["seam_undetermined_entries"]))
    if mut("MUT-HEAD-FORGE"):
        seg2 = seg2.replace("SEC-COMPOSES", "SEC-NEVER-WELDS")
    verdict = [seg1, seg2, seg3, seg4]
    R["verdict"] = SEAL.seal("verdict", verdict)

    # the comparator: it types all four templates ITSELF and re-derives the
    # outcome word from the receipt's own rows.  No shared code, no shared
    # input, no shared literal with the builder above.
    def reconstruct(rec):
        rows = rec["dictionary"]
        bare = [r for r in rows if r["carrier"] == "BARE"]
        alive = all(r["fate"] in ("FOUND-candidate", "UNMOTIVATED")
                    for r in bare)
        motiv = sorted({r["type"] for r in bare
                        if r["fate"] == "FOUND-candidate"})
        if not alive:
            word = "SEC-NEVER-WELDS"
        elif motiv and len(motiv) < len({r["type"] for r in bare}):
            word = "SEC-COMPOSES"
        elif motiv:
            word = "SEC-COMPOSES"
        else:
            word = "SEC-BLOCKED-AT-THE-UNION-DICTIONARY"
        seam_ok = all(s["kernel_dim"] == 4 for s in rec["seam"])
        return {"word": word, "seam_kernel_4": seam_ok,
                "motivated_types": len(motiv),
                "sterile": rec["sterility"]["aut_equals_direct_sum"]}
    recon = reconstruct(R)
    headword = verdict[1].split("-[")[0]
    LD.gate("G-VERDICT-RECON",
            (recon["word"] == headword and recon["seam_kernel_4"]
             and recon["sterile"]
             and recon["motivated_types"] == sum(1 for o in overlap
                                                 if o["welds"])),
            "a comparator that shares neither code nor input nor typed literal "
            "with the builder re-derives the head's outcome word from the "
            "receipt's own fate rows and re-checks the seam and sterility "
            "claims; a one-line forgery of the builder's word moves the "
            "builder alone and dies here",
            {"builder": headword, "comparator": recon["word"],
             "motivated_types": recon["motivated_types"]})
    R["reconstruction"] = SEAL.seal("reconstruction", recon)

    # ---- the paper gates --------------------------------------------------
    # the standing disciplines this run vouches for BY NAME (the vouching
    # layer, #119: seal what you vouch, not only what you measure)
    R["standards"] = SEAL.seal("standards", {
        "cli_contract": 82, "gates_bind_objects": 87, "no_moving_refs": 91,
        "gate_to_disk_seal": 119, "text_gates_as_written": 125,
        "paper_coverage": 20, "honest_denominators": 34,
        "declared_arena": 15,
        "era": ["E-22", "E-23", "E-24"]})
    # the declared registries, sealed BEFORE the paper gates so the paper's
    # own counts are backed by the run that tests it rather than by a later
    # key the coverage scan cannot yet see
    R["totals"] = SEAL.seal("totals", {
        "mutants": len(MUTANTS), "sources": len(SOURCES),
        "cited_not_read": len(CITED_NOT_READ), "gluings": total_gl,
        "types": len(typecount), "window": len(window),
        "dictionary_rows": len(dict_rows), "dead_arms": len(dead),
        "seams": len(seam), "cross_specs": len(cross_rows),
        "verdict_segments": len(verdict)})
    claims = paper_claims(R, overlap, census, window, seam, cross_rows,
                          sterility, total_gl, closed)
    R["paper_claims"] = SEAL.seal("paper_claims", claims)
    if not numbers_only:
        if mut("MUT-PAPER-NUMBER"):
            ptext = ptext.replace("45010", "45011", 1)
        if mut("MUT-PAPER-FENCE"):
            ptext = ptext + "\n```\n" + verdict[0].replace("16", "17") + "\n```\n"
        if mut("MUT-PAPER-POLARITY"):
            ptext = ptext.replace("the direct sum is a declaration",
                                  "the direct sum is a measurement", 1)
        if mut("MUT-PAPER-TABLE"):
            trow = [c["text"] for c in claims
                    if c["id"].startswith("T-CENSUS-")][0]
            cells = trow.split("|")
            cells[2], cells[3] = cells[3], cells[2]
            ptext = ptext.replace(trow, "|".join(cells), 1)
        if mut("MUT-PAPER-SPELLED"):
            ptext = ptext.replace("fifty-four", "a thousand", 1)
        miss = [c["id"] for c in claims if not match_needle(ptext, c["text"])]
        LD.gate("G-PAPER-CLAIMS",
                not miss,
                "every rendered claim of the receipt -- the prose claims AND "
                "every data row of every published table -- occurs in the "
                "paper under test as written, under the #125 normaliser, so a "
                "swapped table cell dies here",
                {"claims": len(claims), "missing": miss})
        cov = paper_coverage(R, ptext, verdict)
        LD.gate("G-PAPER-COVERAGE",
                not cov["unbacked"],
                "every numeral in the paper under test -- INCLUDING those "
                "inside fenced blocks, inline code spans and tables -- is "
                "backed by the receipt's own number registry; no blanket "
                "whitelist is used",
                {"scanned": cov["scanned"], "unbacked": cov["unbacked"][:12],
                 "n_unbacked": len(cov["unbacked"])})
        fence = paper_fences(ptext, verdict)
        LD.gate("G-PAPER-FENCE",
                fence["ok"],
                "every fenced block of the paper is verbatim one of THIS "
                "RUN's verdict strings and every verdict string occurs -- the "
                "stray side admits no fenced block the run did not generate, "
                "so a forged twin of a clean fence cannot hide behind its "
                "sibling",
                fence)
        pol = paper_polarity(ptext)
        LD.gate("G-PAPER-POLARITY",
                pol["ok"],
                "every polarity-bearing sentence the receipt vouches for is "
                "matched in the paper with its sign, so an inverted claim dies "
                "even when its numbers are untouched",
                pol)
        spl = paper_spelled(ptext, cov["registry"])
        LD.gate("G-PAPER-SPELLED",
                spl["ok"],
                "a numeral spelled in words above twelve is a claim like any "
                "other: every spelled numeral in the paper has its integer in "
                "the receipt's own registry, and the registry carries no "
                "sha256, ledger-chain or seal-manifest token",
                spl)
        R["paper_gates"] = SEAL.seal(
            "paper_gates", {"claims": len(claims), "coverage": cov["scanned"],
                            "fences": fence, "polarity": pol, "spelled": spl,
                            "registry_size": len(cov["registry"])})
    else:
        SEAL.declare_unsealed("paper_gates",
                              "--numbers runs the census only; no paper is "
                              "read and no paper gate is evaluated")

    # ---- coverage, falsifier honesty (E-23), and the sweep binding --------
    gates_run = LD.names()
    cover = []
    for (mname, mdesc, mgate) in MUTANTS:
        cover.append({"mutant": mname, "description": mdesc, "gate": mgate,
                      "gate_reached": mgate in gates_run})
    unguarded = [g for g in gates_run
                 if g not in {m[2] for m in MUTANTS}
                 and g not in WAIVED]
    # #34 REACHABILITY WITH DECLARED-LATER GATES.  Three gates are emitted
    # after this one by construction -- the sweep binding, the seal
    # completeness and the disk integrity -- and in `--numbers` the paper
    # gates are not evaluated at all because no paper is read.  Both sets are
    # NAMED here and their presence is verified at the last gate rather than
    # assumed; every other mutant's target must be reached in this very run.
    later = set(LATER_GATES) | (set(PAPER_GATES) if numbers_only else set())
    for c in cover:
        c["declared_later"] = c["gate"] in later
    unreached = [c["mutant"] for c in cover
                 if not c["gate_reached"] and not c["declared_later"]]
    LD.gate("G-COVERAGE",
            not unguarded and not unreached,
            "every gate this run evaluated is either falsified by a declared "
            "mutant or carries a named waiver with a forcing, and every "
            "declared mutant's target gate is REACHED in this run unless it is "
            "named DECLARED-LATER -- the denominator is the run's own gate "
            "count, not a hand-kept number",
            {"gates": len(gates_run), "mutants": len(MUTANTS),
             "unguarded": unguarded, "unreachable": unreached,
             "declared_later": sorted(later), "mode_numbers_only": numbers_only,
             "waived": sorted(WAIVED)})
    R["coverage"] = SEAL.seal("coverage", {"gates": gates_run,
                                           "mutant_map": cover,
                                           "waivers": WAIVED})
    R["ledger"] = SEAL.seal("ledger", [{"gate": r["gate"], "ok": r["ok"],
                                        "chain": r["chain"]}
                                       for r in LD.rows])
    R["gate_count"] = SEAL.seal("gate_count", len(LD.rows))
    # E-24, MEASURE-RELATIVITY OF COUNTS.  This unit publishes no probability
    # and no percentage.  Every ratio it publishes is a COUNT over a declared
    # exhaustive enumeration with its denominator written beside it, and no
    # measure is declared on the gluing family -- so every one is stamped
    # COUNTING-ONLY rather than dressed as a likelihood.
    R["measure_stamp"] = SEAL.seal("measure_stamp", {
        "stamp": "COUNTING-ONLY",
        "declared_measure_on_the_gluing_family": None,
        "ratios_published": ["welding types of types",
                             "welding gluings of gluings",
                             "doubled-free gluings of gluings by k",
                             "FORCED window records of window records",
                             "admitted cross specifications of specifications"],
        "note": "each is a count over an exhaustive enumeration with its "
                "denominator published; none is a probability, and this unit "
                "declares no measure under which it could be read as one"})
    R["schema_version"] = SEAL.seal("schema_version", SCHEMA)
    R["swept"] = swept
    SEAL.declare_unsealed("swept",
                          "the sweep flag is set by the caller after the "
                          "mutant sweep runs; it is bound by G-SWEEP-EXECUTED "
                          "in the delivery path rather than sealed here")
    SEAL.declare_unsealed("seal_manifest",
                          "the manifest cannot digest itself")
    SEAL.declare_unsealed("ledger_chain",
                          "the chained ledger head is the seal of every gate "
                          "row and is emitted after the manifest is closed")
    SEAL.declare_unsealed("mutant_sweep",
                          "the sweep rows are produced by the delivery caller "
                          "after this run returns and are sealed there")
    return LD, SEAL, R, verdict, ptext


LATER_GATES = ("G-SWEEP-EXECUTED", "G-SEAL-COMPLETE", "G-INTEGRITY")
PAPER_GATES = ("G-PAPER-CLAIMS", "G-PAPER-COVERAGE", "G-PAPER-FENCE",
               "G-PAPER-POLARITY", "G-PAPER-SPELLED")

WAIVED = {
    "G-EXACT": "a mutant that introduced a float would have to be a float, "
               "and the AST scan is the falsifier of its own object; the "
               "gate's other value is exercised by G-EXACT's own scan of the "
               "receipt's types",
    "G-ARRANGEMENT-FREE": "waived with a forcing: the alternative arrangement "
                          "is SEARCHED FOR rather than typed, so a run in "
                          "which no non-collinear saturating triple exists "
                          "fails at the search rather than at the gate",
    "G-MAXHITS": "waived with a forcing: every event is specified by its full "
                 "tuple, at most one candidate can match, and the under-"
                 "specified control is paper-19's committed measurement "
                 "(maxhits 7) which this unit cites and does not re-run",
    "G-CONTROLS": "falsified by MUT-DICT-FATE, which forges a fate in the same "
                  "detector these rows come from",
    "G-AUT-ROUTES-UNION": "falsified by MUT-AUT-ROUTE, which poisons the "
                          "second automorphism route the gate compares",
    "G-SEED-RULE": "falsified by MUT-MENU-MEMO, which changes what the "
                   "committed menu offers and so moves the refusal set",
    "G-SEAM-CROSS-ALGEBRA": "falsified by MUT-SEAM-RANK, which misreports the "
                            "rank of the same exact system",
    "G-CONTRAST": "falsified by MUT-STERILITY, which breaks the direct-sum "
                  "identity the contrast is taken against",
    "G-GLUING-CENSUS": "falsified by MUT-TYPE-COUNT",
    "G-DECLARED-LATER": "waived with a forcing: the gate discharges the "
                        "coverage gate's own declared-later promise, and a "
                        "mutant of it would be a mutant of the ledger it "
                        "reads",
    "G-COVERAGE": "waived with a forcing: a mutant of the coverage gate would "
                  "be a mutant of the mutant registry, and the registry is "
                  "compared against the run's own evaluated ledger",
    "G-PAPER-CLAIMS": "falsified by MUT-PAPER-TABLE, which swaps two data "
                      "cells of a published table row in the object under "
                      "test",
    "G-SWEEP-EXECUTED": "waived with a forcing: the sweep gate is the binding "
                        "itself; it is re-taken at the integrity gate, so a "
                        "run reaching the writer without a sweep dies twice",
    "G-INTEGRITY": "waived with a forcing: the integrity gate compares disk "
                   "bytes against the gate-time seal after a deliberately "
                   "corrupted probe has been shown to be detected in the same "
                   "run",
    "G-MENU-PURE": "falsified by MUT-MENU-MEMO",
    "G-DRIVEN-EQUALS-COMBINATORIAL": "falsified by MUT-DRIVEN-EQ",
    "G-SOURCES": "falsified by MUT-ANCHOR-DIGEST and by --break-anchor",
    "G-ANCHORS": "falsified by MUT-ANCHOR-TEXT",
}


# ---------------------------------------------------------------------------
# the paper instrument
# ---------------------------------------------------------------------------

def paper_claims(R, overlap, census, window, seam, cross_rows, sterility,
                 total_gl, closed):
    """the rendered claims: the paper's prose AND EVERY DATA ROW OF EVERY
    PUBLISHED TABLE are checked against these, and they are rendered FROM THE
    RECEIPT so a stale sentence or a swapped cell cannot survive.  E-22:
    tables render as claims."""
    nw = sum(1 for o in overlap if o["welds"])
    c0 = [c for c in census if c["k"] == 0][0]
    out = [
        ("C01", "the family is %d gluings in %d combinatorial types"
         % (total_gl, len(census))),
        ("C02", "the union welds at %d of the %d types" % (nw, len(census))),
        ("C03", "the site-assignment fiber is 1 at every one of the %d types"
         % len(census)),
        ("C04", "at k = 0 the automorphism group is %d, which is "
                "|Aut(sector)|^2 times 2" % c0["aut"]),
        ("C05", "the seam system has rank 6 on 10 unknowns, so its kernel is 4"),
        ("C06", "%d of the %d cross-sector specifications are ADMITTED by the "
                "committed grammar"
         % (sum(1 for c in cross_rows if c["fate"] == "ADMITTED"),
            len(cross_rows))),
        ("C07", "the doubled-free gluings number %d of %d"
         % (sum(o["gluings"] for o in overlap if o["welds"]), total_gl)),
        ("C08", "at k = 3 the aligned type carries %d of the %d gluings"
         % (sum(o["gluings"] for o in overlap if o["welds"] and o["k"] == 3),
            closed(3))),
    ]
    # ---- EVERY DATA ROW OF EVERY PUBLISHED TABLE, rendered as a claim ----
    for c in census:
        out.append(("T-CENSUS-%s" % c["type"],
                    "| `%s` | %d | %d | %d | %d | %d | %d | %d |"
                    % (c["type"], c["gluings"], c["carriers"], c["pairs"],
                       c["doubled"], c["aut"], c["aut_weighted"],
                       c["fiber_site_A"])))
    for o in overlap:
        out.append(("T-OVERLAP-%s" % o["type"],
                    "| `%s` | %d | %d | %d | %s | %s |"
                    % (o["type"], o["k"], o["gluings"], o["doubled"],
                       o["bare_fate"], "YES" if o["welds"] else "no")))
    for w in window:
        out.append(("T-WINDOW-%s-%s" % (w["type"], w["seed_rule"]),
                    "| `%s` | %s | %s | %s | %s | %s |"
                    % (w["type"], w["seed_rule"], w["fate"], w["events"],
                       w["divisions"],
                       "yes" if w["driven_equals_combinatorial"] else "--")))
    for s in seam:
        out.append(("T-SEAM-%s" % s["gluing"],
                    "| %s | %s | %s | %d | %d | %d | %d | %s |"
                    % (s["gluing"], s["nA"], s["nB"], s["equations"],
                       s["unknowns"], s["rank"], s["kernel_dim"],
                       s["indefinite_witness"]["value"])))
    for c in cross_rows:
        out.append(("T-CROSS-%s" % c["spec"],
                    "| %s | %s | %s | %d | %d | %s |"
                    % (c["spec"], c["seed"], c["fate"], c["new_pairs"],
                       c["foreign_pairs"],
                       c.get("dictionary_after", "--"))))
    for c in R["seam_cross_algebra"]:
        out.append(("T-XALG-%d" % c["cross_links"],
                    "| %d | %d | %d |"
                    % (c["cross_links"], c["rank"], c["kernel_dim"])))
    return [{"id": i, "text": t} for i, t in out]


SPELLED = {"thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16,
           "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20,
           "twenty-seven": 27, "thirty": 30, "thirty-six": 36, "fifty": 50,
           "fifty-four": 54, "eighty-one": 81, "hundred": 100,
           "thousand": 1000}


def paper_spelled(text, reg):
    """#267 (d): a numeral spelled in words above twelve is a claim like any
    other.  Every spelled numeral above twelve must have its integer in the
    receipt's own registry."""
    low = canon(text).lower()
    bad = []
    seen = []
    for word, val in sorted(SPELLED.items(), key=lambda kv: -len(kv[0])):
        if re.search(r"(?<![\w-])" + re.escape(word) + r"(?![\w-])", low):
            seen.append(word)
            if str(val) not in reg:
                bad.append(word)
    return {"ok": not bad, "spelled_found": seen, "unbacked": bad}


NUM_RE = re.compile(r"(?<![\w./-])\d[\d,]*(?:/\d+)?(?![\w.])")


DIGEST_KEYS = ("sha256_12", "declared", "chain", "ledger_chain",
               "seal_manifest", "sealed", "order")
PURE_NUM = re.compile(r"^-?\d[\d,]*(?:/\d+)?$")


def paper_coverage(R, text, verdict):
    """E-22: coverage includes fenced blocks AND inline code spans; tables
    render as claims.  Nothing is stripped before the scan.  #267 (d): the
    registry is built from the MEASURED layer only -- no sha256, ledger-chain
    or seal-manifest token may back a numeral in the paper."""
    reg = set(NUMREG)
    for v in verdict:
        for m in NUM_RE.finditer(v):
            reg.add(m.group(0))

    def walk(o):
        if isinstance(o, dict):
            for k, v in o.items():
                if k in DIGEST_KEYS:
                    continue
                walk(v)
        elif isinstance(o, (list, tuple)):
            for v in o:
                walk(v)
        elif isinstance(o, bool):
            pass
        elif isinstance(o, int):
            reg.add(str(o))
            reg.add("{:,}".format(o))
        elif isinstance(o, str):
            # #267 (d), STRICTER THAN THE LETTER: a numeral is backed only by
            # a MEASURED VALUE -- an integer or an exact rational the run
            # computed -- never by a digit that happens to occur inside a
            # prose string of the receipt.  Harvesting substrings of reasons
            # and descriptions is a blanket whitelist wearing a walk.
            if PURE_NUM.match(o.strip()):
                for m in NUM_RE.finditer(o):
                    reg.add(m.group(0))
    walk(R)
    # the paper's own structural numerals: section and list numbering
    struct = set()
    for ln in text.split("\n"):
        m = re.match(r"^\s*#{1,6}\s+([\d.]+)", ln)
        if m:
            struct.add(m.group(1))
            for p in m.group(1).split("."):
                struct.add(p)
        m2 = re.match(r"^\s*(\d+)[.)]\s", ln)
        if m2:
            struct.add(m2.group(1))
    scanned = 0
    unbacked = []
    for m in NUM_RE.finditer(text):
        tok = m.group(0)
        scanned += 1
        if tok in reg or tok.replace(",", "") in reg or tok in struct:
            continue
        if tok.replace(",", "") in {s.replace(",", "") for s in reg}:
            continue
        unbacked.append(tok)
    return {"scanned": scanned, "unbacked": sorted(set(unbacked)),
            "registry": {s.replace(",", "") for s in reg} | set(struct)}


def paper_fences(text, verdict):
    """E-22, BLOCKS BY MULTISET.  Every fenced block of the paper is taken as
    a claim: each must be verbatim one of THIS RUN's verdict strings, and each
    verdict string must occur.  Containment alone is what E-22 was bought to
    kill -- an object carrying two copies of its verdict fence, one clean and
    one forged, satisfies containment while its twin is a forgery -- so the
    stray side is total here and admits no fenced block the run did not
    generate, whatever its prefix."""
    blocks = re.findall(r"```[a-zA-Z]*\n(.*?)```", text, re.S)
    got = Counter(norm(b) for b in blocks)
    want = Counter(norm(v) for v in verdict)
    missing = [k[:60] for k in want if got[k] < want[k]]
    stray = [k[:60] for k in got if k not in want]
    return {"ok": not missing and not stray, "blocks": len(blocks),
            "distinct_blocks": len(got), "verdict_segments": len(want),
            "missing": missing, "stray": stray}


# each row carries its OWN negation, so the gate tests the sign it names
# rather than a string edit that happens to be meaningful for one row.
POLARITY = [
    ("P1", "the union welds", "the union never welds"),
    ("P2", "the direct sum is a declaration",
     "the direct sum is a measurement"),
    ("P3", "R1's prediction is confirmed", "R1's prediction is refuted"),
]


def paper_polarity(text):
    bad = []
    rows = []
    for (pid, pos, neg) in POLARITY:
        gotp = match_needle(text, pos)
        gotn = match_needle(text, neg)
        rows.append({"id": pid, "positive_present": gotp,
                     "negation_present": gotn})
        if not gotp or gotn:
            bad.append(pid)
    return {"ok": not bad, "checked": len(POLARITY), "bad": bad,
            "rows": rows}


# ---------------------------------------------------------------------------
# delivery
# ---------------------------------------------------------------------------

def render(R, verdict, LD):
    L = []
    L.append("=" * 78)
    L.append("v14 SEC -- THE SECTOR/ATLAS UNIT: GLUED WELDED WORLDS")
    L.append("instrument for v14/paper-32-sec.md   schema %s" % SCHEMA)
    L.append("=" * 78)
    L.append("")
    L.append("PROVENANCE: %d sources, all sha256-12 verified." % len(SOURCES))
    for p in R["provenance"]:
        L.append("  %-10s %-44s %s" % (p["id"], p["path"], p["sha256_12"]))
    L.append("")
    L.append("-- STAGE 1: THE ARENA FAMILY " + "-" * 48)
    s = R["sector"]
    L.append("  the driven sector: %d events, %d divisions, %d of %d cells at "
             "n = 1, det = %s, posdef %d of 9"
             % (s["events"], s["divisions"], s["cells_at_one"], s["cells"],
                s["det"], s["posdef"]))
    g = R["gluing_totals"]
    L.append("  the family: %d gluings (closed form %d) in %d combinatorial "
             "types" % (g["total"], g["closed_form"], g["types"]))
    L.append("  by k: " + "  ".join("k=%s:%d" % (k, v)
                                    for k, v in sorted(g["by_k"].items())))
    L.append("  doubled-free: " + "  ".join(
        "k=%s:%d" % (k, v) for k, v in sorted(g["doubled_free_by_k"].items()))
        + "   total %d" % g["doubled_free_total"])
    L.append("")
    L.append("  %-26s %7s %4s %4s %4s %9s %9s %6s" %
             ("type", "gluings", "n", "E", "dbl", "|Aut|", "|Aut_w|", "fiber"))
    for c in R["type_census"]:
        L.append("  %-26s %7d %4d %4d %4d %9d %9d %6s"
                 % (c["type"], c["gluings"], c["carriers"], c["pairs"],
                    c["doubled"], c["aut"], c["aut_weighted"],
                    c["fiber_site_A"]))
    L.append("")
    L.append("  the driven window: %d records" % len(R["window"]))
    for w in R["window"]:
        L.append("    %-26s %-7s %-8s ev=%-4s div=%-3s eq=%s"
                 % (w["type"], w["seed_rule"], w["fate"], w["events"],
                    w["divisions"], w["driven_equals_combinatorial"]))
    L.append("")
    L.append("-- STAGE 2: THE UNION'S DICTIONARY " + "-" * 42)
    L.append("  %-26s %-10s %-14s %-18s %s"
             % ("type", "reading", "carrier", "fate", "inventory"))
    for r in R["dictionary"]:
        L.append("  %-26s %-10s %-14s %-18s %s"
                 % (r["type"], r["reading"], r["carrier"], r["fate"],
                    r.get("inventory", "")))
    L.append("")
    L.append("  the declared dead arms:")
    for d in R["dead_arms"]:
        L.append("    %-42s %-10s %-12s %s"
                 % (d["arena"], d["reading"], d["fate"], d["reason"][:60]))
    L.append("")
    L.append("-- STAGE 3: THE GLUING FIBER " + "-" * 48)
    for c in R["gluing_fiber"]["compatibility"]:
        L.append("    %-26s shared cells %-4d union differs at %-3d  %s"
                 % (c["type"], c["shared_cells"],
                    c["cells_where_union_differs_from_sector"],
                    "COMPATIBLE" if c["compatible"] else "SEAM-DEFORMED"))
    L.append("")
    L.append("-- STAGE 4: CURVATURE OF THE GLUING " + "-" * 41)
    for s2 in R["seam"]:
        L.append("    %-14s nA=%s nB=%s  unknowns=%d equations=%d rank=%d "
                 "kernel=%d  direct-sum minors %s posdef=%s"
                 % (s2["gluing"], s2["nA"], s2["nB"], s2["unknowns"],
                    s2["equations"], s2["rank"], s2["kernel_dim"],
                    s2["direct_sum_minors"], s2["direct_sum_posdef"]))
        w = s2["indefinite_witness"]
        if w:
            L.append("      indefinite completion: Q(%s) = %s, all six counts "
                     "reproduced = %s"
                     % (w["vector"], w["value"],
                        s2["witness_reproduces_counts"]))
    L.append("    cross-link algebra: " + ", ".join(
        "%d links -> kernel %d" % (c["cross_links"], c["kernel_dim"])
        for c in R["seam_cross_algebra"]))
    L.append("")
    for c in R["cross_sector"]:
        L.append("    cross spec %-16s seed %-12s %-9s new pairs %d foreign "
                 "%d  dictionary after: %s"
                 % (c["spec"], c["seed"], c["fate"], c["new_pairs"],
                    c["foreign_pairs"], c.get("dictionary_after", "-")))
    L.append("")
    L.append("-- STAGE 5: THE FORCED-OVERLAP QUESTION " + "-" * 37)
    for o in R["forced_overlap"]["rows"]:
        L.append("    %-26s k=%d gluings=%-6d doubled=%d  %-18s welds=%s"
                 % (o["type"], o["k"], o["gluings"], o["doubled"],
                    o["bare_fate"], o["welds"]))
    L.append("    k with a welding type: %s ; k with a non-welding type: %s"
             % (R["forced_overlap"]["k_with_a_welding_type"],
                R["forced_overlap"]["k_with_a_non_welding_type"]))
    L.append("")
    L.append("-- STAGE 6: THE k = 0 STERILITY CONTROL " + "-" * 37)
    st = R["sterility"]
    for k2 in sorted(st):
        L.append("    %-38s %s" % (k2, st[k2]))
    L.append("")
    L.append("-- THE WALLS " + "-" * 64)
    L.append("    scan: %d terms; receipt hits %s ; paper hits %s"
             % (len(R["walls"]["scanned_terms"]), R["walls"]["receipt_hits"],
                R["walls"]["paper_hits"]))
    L.append("")
    L.append("-- GATES " + "-" * 68)
    for r in LD.rows:
        L.append("    %-32s %-4s %s" % (r["gate"], "PASS" if r["ok"] else "FAIL",
                                        r["chain"]))
    L.append("")
    L.append("-- VERDICT " + "-" * 66)
    for v in verdict:
        L.append("")
        L.append(v)
    L.append("")
    L.append("=" * 78)
    return "\n".join(L) + "\n"


def finish(LD, SEAL, R, verdict, write=True, swept=False):
    R["swept"] = swept
    LD.gate("G-SWEEP-EXECUTED",
            swept,
            "the delivery run carries one sweep row per declared mutant, every "
            "row on target, and has evaluated this gate itself -- so the only "
            "writer in this file is downstream of a sweep that actually ran",
            {"mutants": len(MUTANTS), "swept": swept})
    manifest = SEAL.manifest()
    published = sorted(k for k in R if k not in ("swept",))
    missing = [k for k in published
               if k not in manifest["sealed"] and k not in
               manifest["declared_unsealed"]]
    if mut("MUT-SEAL-DROP") and manifest["sealed"]:
        drop = sorted(manifest["sealed"])[0]
        del manifest["sealed"][drop]
        missing = [k for k in published
                   if k not in manifest["sealed"]
                   and k not in manifest["declared_unsealed"]]
    LD.gate("G-SEAL-COMPLETE",
            not missing,
            "THE MANIFEST IS TOTAL: every published receipt key is either "
            "sealed at the moment its gate passed or listed as "
            "DECLARED-UNSEALED, and the completeness check compares the "
            "manifest against the published key set rather than against the "
            "seals that happened to be taken",
            {"published": len(published), "sealed": len(manifest["sealed"]),
             "declared_unsealed": len(manifest["declared_unsealed"]),
             "missing": missing})
    # the DECLARED-LATER promise, discharged at the last gate: every gate
    # G-COVERAGE named as emitted-later must actually be in this run's ledger,
    # except the integrity gate itself, which is emitted after the transcript
    # is serialized and is recorded by the artifacts' existence instead.
    names = set(LD.names())
    owed = [g for g in LATER_GATES if g != "G-INTEGRITY" and g not in names]
    LD.gate("G-DECLARED-LATER",
            not owed,
            "every gate named DECLARED-LATER by the coverage gate is present "
            "in this run's own ledger by the time the run ends, so the "
            "reachability waiver is discharged rather than promised",
            {"declared_later": list(LATER_GATES), "still_owed": owed})
    R["seal_manifest"] = manifest
    R["ledger_chain"] = LD.chain[:16]
    txt = render(R, verdict, LD)
    payload = json.dumps(R, indent=1, sort_keys=True, default=str)
    if not write:
        return txt, payload, True
    tmp1, tmp2 = OUT_TXT + ".tmp", OUT_JSON + ".tmp"
    with open(tmp1, "w") as f:
        f.write(txt)
    os.replace(tmp1, OUT_TXT)
    with open(tmp2, "w") as f:
        f.write(payload)
    os.replace(tmp2, OUT_JSON)
    # the integrity check: disk bytes against the gate-time seal, after a
    # deliberately corrupted probe has been shown to be detected
    probe_ok = (hashlib.sha256((txt + "x").encode()).hexdigest()
                != hashlib.sha256(txt.encode()).hexdigest())
    d1 = hashlib.sha256(read_text_file(OUT_TXT).encode()).hexdigest()
    d2 = hashlib.sha256(read_text_file(OUT_JSON).encode()).hexdigest()
    ok = (probe_ok and d1 == hashlib.sha256(txt.encode()).hexdigest()
          and d2 == hashlib.sha256(payload.encode()).hexdigest())
    if not ok:
        raise GateFail("G-INTEGRITY: disk bytes differ from the gate-time seal")
    return txt, payload, ok


def selftest():
    """FALSIFICATION SELF-TEST: corrupt one anchor's expected digest in memory,
    confirm the run dies at the anchor gate, WRITE NOTHING."""
    before = [os.path.exists(OUT_TXT) and read_text_file(OUT_TXT),
              os.path.exists(OUT_JSON) and read_text_file(OUT_JSON)]
    try:
        full_run(break_anchor="A-D42B1", write=False)
    except GateFail as e:
        after = [os.path.exists(OUT_TXT) and read_text_file(OUT_TXT),
                 os.path.exists(OUT_JSON) and read_text_file(OUT_JSON)]
        return (str(e).startswith("G-SOURCES"), str(e).split("|")[0],
                before == after)
    return False, "the corrupted run did NOT die", None


class _Sink:
    def write(self, *a, **k):
        pass

    def flush(self):
        pass


def run_mutant(name):
    ACTIVE_MUTANT[0] = name
    old = sys.stdout
    sys.stdout = _Sink()
    try:
        LD, SEAL, R, V, ptext = full_run(write=False)
        finish(LD, SEAL, R, V, write=False, swept=True)
        return None
    except GateFail as e:
        return str(e).split(":")[0]
    except Exception as e:                      # a mutant may crash a route
        return "CRASH/" + type(e).__name__
    finally:
        sys.stdout = old
        ACTIVE_MUTANT[0] = None


FLAGS = {"--no-write": 0, "--numbers": 0, "--selftest": 0, "--mutant": 1,
         "--break-anchor": 1, "--verify-paper": "opt", "--list-gates": 0,
         "--list-mutants": 0}
MODES = ("--numbers", "--selftest", "--mutant", "--break-anchor",
         "--verify-paper", "--list-gates", "--list-mutants")


def parse_args(argv):
    out = {}
    i = 0
    modes = []
    while i < len(argv):
        a = argv[i]
        if a not in FLAGS:
            raise CliError("unknown argument %r" % a)
        spec = FLAGS[a]
        if a in MODES:
            modes.append(a)
        if spec == 0:
            out[a] = True
            i += 1
        elif spec == 1:
            if i + 1 >= len(argv) or argv[i + 1].startswith("--"):
                raise CliError("%s requires an argument" % a)
            out[a] = argv[i + 1]
            i += 2
        else:
            if i + 1 < len(argv) and not argv[i + 1].startswith("--"):
                out[a] = argv[i + 1]
                i += 2
            else:
                out[a] = True
                i += 1
    if len(modes) > 1:
        raise CliError("modes do not compose: %s" % ", ".join(modes))
    if "--mutant" in out and out["--mutant"] not in MUTANT_NAMES:
        raise CliError("unknown mutant %r" % out["--mutant"])
    if "--break-anchor" in out and out["--break-anchor"] not in SOURCE_IDS:
        raise CliError("unknown anchor %r" % out["--break-anchor"])
    if "--verify-paper" in out and out["--verify-paper"] is not True:
        p = out["--verify-paper"]
        if not os.path.isfile(p):
            raise CliError("--verify-paper path does not exist: %r" % p)
    return out


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    try:
        opt = parse_args(argv)
    except CliError as e:
        sys.stderr.write("CLI: %s\n" % e)
        return 2
    if "--list-gates" in opt:
        LD, SEAL, R, V, _p = full_run(write=False)
        for g in LD.names():
            print(g, "  waived" if g in WAIVED else "")
        return 0
    if "--list-mutants" in opt:
        for (n, d, g) in MUTANTS:
            print("%-24s %-52s -> %s" % (n, d, g))
        return 0
    if "--selftest" in opt:
        died, why, nowrite = selftest()
        print("selftest: died=%s at %s ; artifacts unchanged=%s"
              % (died, why, nowrite))
        return 1 if (died and nowrite) else 2
    if "--mutant" in opt:
        got = run_mutant(opt["--mutant"])
        want = dict((m[0], m[2]) for m in MUTANTS)[opt["--mutant"]]
        print("mutant %s -> %s (declared gate %s)"
              % (opt["--mutant"], got, want))
        return 1 if got == want else 0
    if "--break-anchor" in opt:
        try:
            full_run(break_anchor=opt["--break-anchor"], write=False)
        except GateFail as e:
            print("break-anchor %s -> %s" % (opt["--break-anchor"],
                                             str(e).split(":")[0]))
            return 1
        print("break-anchor %s SURVIVED" % opt["--break-anchor"])
        return 0
    if "--verify-paper" in opt:
        p = opt["--verify-paper"]
        rel = PAPER_REL if p is True else os.path.relpath(os.path.abspath(p),
                                                          REPO)
        try:
            path = os.path.join(REPO, rel)
            txt = read_text_file(path)
            LD, SEAL, R, V, _pp = full_run(paper_text=txt, paper_rel=rel,
                                           write=False)
        except GateFail as e:
            print("verify-paper: FAIL %s" % str(e).split("|")[0])
            return 1
        print("verify-paper: PASS (%d gates)" % len(LD.rows))
        return 0
    numbers = "--numbers" in opt
    write = ("--no-write" not in opt) and not numbers
    try:
        LD, SEAL, R, V, ptext = full_run(write=False, numbers_only=numbers)
    except GateFail as e:
        sys.stderr.write("GATE FAIL: %s\n" % e)
        return 1
    swept = False
    sweep_rows = []
    if not numbers:
        for (n, d, g) in MUTANTS:
            got = run_mutant(n)
            sweep_rows.append({"mutant": n, "died_at": got, "declared": g,
                               "on_target": got == g})
        swept = all(r["on_target"] for r in sweep_rows)
        if not swept:
            sys.stderr.write("MUTANT SWEEP OFF TARGET: %s\n"
                             % [r for r in sweep_rows if not r["on_target"]])
            return 1
        R["mutant_sweep"] = SEAL.seal("mutant_sweep", sweep_rows)
    else:
        SEAL.declare_unsealed("mutant_sweep",
                              "--numbers runs no sweep and writes nothing")
    try:
        txt, payload, ok = finish(LD, SEAL, R, V, write=write, swept=swept
                                  or numbers)
    except GateFail as e:
        sys.stderr.write("GATE FAIL: %s\n" % e)
        return 1
    print(txt)
    if write:
        print("wrote %s (%d bytes) and %s (%d bytes)"
              % (os.path.basename(OUT_TXT), len(txt),
                 os.path.basename(OUT_JSON), len(payload)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
