#!/usr/bin/env python3.13
# -*- coding: utf-8 -*-
"""
v14 R = 4 -- THE DECLARED-RECORD WELD AND THE SPLITTABLE QUESTION.
Instrument for `v14/paper-21-r4dec.md`.

QUESTION (pin `v14/note-r4dec-pin.md`, sha256-12 f50630ced3be, ledger #174).
Paper-19 welded a DRIVEN R = 3 grammar record onto I7's record SPACE and
landed on (1,1,1) -- admissible, inside I7's 361-point box, and outside its
declared eleven.  Its own rigidity theorem says why: at R = 3 the budget is
27, exactly what nine positive-definite sites need, so the only reachable
I7-STRICT field is identically 1 and no R = 3 schedule can reach a DECLARED
record at all.  One round later the budget is 36 and I7's own G-FLAT = (1,1,2)
needs exactly 36.  The paper-19 effectus measured the combinatorial side --
G-FLAT reachable at 276 ordered quadruples of saturating groupings -- and left
the rest open.  This unit runs the four stages the pin gates:

  STAGE 1  THE 276, UNIT-GRADE.  The R = 4 grouping census rebuilt exhaustively,
           the 276 confirmed by two routes that share no code, the budget
           theorem that makes 36^4 exhaustive over the whole 280^4 family, and
           the arrangement DRIVEN through the committed grammar's own menus:
           the induced record is EXACTLY I7's committed G-FLAT row.
  STAGE 2  THE DECLARED-RECORD WELD.  Weld 2's detector, unchanged, at both
           readings, with the RSQ choice standard and the controls
           re-established -- pointed at the R = 4 G-FLAT records against I7.
  STAGE 3  THE SPLITTABLE QUESTION.  The split fiber at every interval of the
           welded record, and which of the terminal refinement laws (papers
           04 / 06 / 09) become non-empty on it.
  STAGE 4  THE PRICE-LAW ROW.  The R = 4 budget census: the COVER / POSDEF /
           I7-STRICT classes, exhaustive over all 280^4 ordered grouping
           quadruples, extending R = 2 (budget binds) and R = 3 (matching
           binds).

WHAT THIS PROGRAM DOES
  SEC 1  PROVENANCE.  18 pinned sources, sha256-12 verified, products gated;
         the #62 verbatim anchors bound to their consumer gates; every text
         gate whitespace-normalises, ASCII-folds AND strips markdown prefixes.
  SEC 2  EXACT ARITHMETIC on Z_3^2; the partitions, the parallel classes.
  SEC 3  THE COMMITTED GRAMMAR, DRIVEN DIRECTLY.  d42b1's transport layer by
         text slice, d60's `B`/`dl` and d66's `conflict_grid` by AST
         extraction.  No admissibility rule is re-typed anywhere in this file.
  SEC 4  THE R = 4 FAMILY and the declared driven WINDOW W4, in the head.
  SEC 5  THE COMBINATORIAL COLUMNS, packed exactly (4 bits per cell).
  SEC 6  STAGE 1.   SEC 7  STAGE 2.   SEC 8  STAGE 3.   SEC 9  STAGE 4.
  SEC 10 THE WALLS (four inherited, the Lorentzian resonance NAMED).
  SEC 11 The verdict, derived a second time from the serialized receipt by a
         comparator that types all four templates itself; the paper gates --
         claim rendering, numeral coverage INCLUDING THE FENCED VERDICT
         BLOCKS, head-verbatim and claim polarity; the TOTAL seal; the
         sweep-execution binding; the artifacts; the integrity check.

CLI CONTRACT (the #82 minimum: argv parsed against a whitelist)
---------------------------------------------------------------
    python3.13 v14/code/r4dec_exact.py
        THE DELIVERY RUN, and the ONLY writer.  Builds the whole census,
        evaluates every gate (the paper gates included), runs every declared
        mutant in-process, re-reads what it wrote and writes
        `r4dec_output.txt` and `r4dec_receipt.json` beside this file.
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
                    rebuilds the derivation and evaluates the paper gates --
                    claim rendering, numeral coverage and claim POLARITY --
                    with PATH (this unit's paper by default) as the object
                    under test.  Exits 1 on drift, 0 on a clean paper, 2 if
                    PATH does not exist or is not a file.
    --list-gates / --list-mutants
                    print the registries and exit 0.

    Any other argument, any unknown flag argument, any missing flag argument,
    any SECOND MODE FLAG and any --verify-paper PATH that does not exist exits
    2.  No flag is mutant-only and no flag is a no-op: modes do not compose.

THE TOTAL GATE-TO-DISK SEAL (RUNBOOK 14 addendum, v14 #119 + the #148 totality
addendum + the U4b vouching-layer lesson).  EVERY published receipt key -- the
measured layer AND the vouching layer: schema, provenance, paper_claims,
coverage, polarity, gates, totals, and the transcript head -- is either sealed
at the moment its gate passes or listed as DECLARED-UNSEALED in the manifest,
and a gate compares the manifest against the DECLARED key set rather than
against the keys that happened to be taken.  The artifacts are written from the
sealed payload through `os.replace`, and the terminal integrity gate compares
the BYTES ON DISK against the gate-time seal.

TEXT GATES (#125 WITH MARKDOWN-PREFIX NORMALIZATION).  Every gate that matches
prose against a needle whitespace-normalises both sides, ASCII-folds both
sides, AND strips markdown line prefixes, so a needle that spans a block quote
or a numbered list cannot be evaded by re-wrapping.

ARITHMETIC.  Exact only: `fractions.Fraction` and Python integers.  There are
no floats anywhere -- an AST scan of this file and a recursive type scan of the
emitted receipt are gates.

RUNTIME INPUTS (#46/#91).  Exactly 18 files are read at run time as SOURCES,
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
OUT_TXT = os.path.join(os.path.dirname(SELF), "r4dec_output.txt")
OUT_JSON = os.path.join(os.path.dirname(SELF), "r4dec_receipt.json")

SCHEMA = "isp/v14/r4-declared-weld/1"
PAPER_REL = "v14/paper-21-r4dec.md"

# ===========================================================================
# SECTION 0.  THE FROZEN DECLARATION (RUNBOOK section 15: the arena is data)
# ===========================================================================

SOURCES = [
    ("A-PIN", "v14/note-r4dec-pin.md", "f50630ced3be",
     "THIS UNIT'S PIN (ledger #174): the four stages, the outcome names, the "
     "window licensing pattern inherited from paper-19."),
    ("A-P19", "v14/paper-19-r3-weld.md", "50bb81e67942",
     "PAPER 19 (terminal): the R = 3 arena, the rigidity theorem, the weld "
     "detector's two readings, the RSQ choice standard, the dead lists this "
     "unit cites and never re-runs, and the R = 4 register row."),
    ("A-P19REC", "v14/code/r3_weld_receipt.json", "dfea664f2408",
     "PAPER 19's COMMITTED RECEIPT: the R = 4 register probe row and the "
     "R = 3 committed numbers, READ from these bytes and reproduced here."),
    ("A-R3WEFF", "v14/review-r3w-effectus.md", "6a240a4c6534",
     "the paper-19 effectus review: the exhaustive discovery this unit makes "
     "unit-grade, and the cost row it registered against the successor."),
    ("A-HA", "v13/paper-ha-successor.md", "f286ba10d2d9",
     "I7 / HA: the declared readout, the admissibility criterion, and "
     "requirement 3 -- the two-way rule this unit's controls discharge."),
    ("A-I7", "v13/code/ha_successor_receipt.json", "542b8735daf0",
     "I7's ARENA AS DATA: sites, links, the declared record family whose "
     "G-FLAT row is this unit's target, and the declared count box."),
    ("A-P04", "v14/paper-04-refinement-grammar.md", "dfa5090f26b1",
     "R6a / paper-04 (terminal): the refinement grammar -- the split fiber "
     "identity, the DYADIC and SINGLE-INTERVAL class verdicts, the three "
     "unrefinable records and the flat-family scale row."),
    ("A-P04REC", "v14/code/r6a_refinement_receipt.json", "856f6e810ab5",
     "R6a's COMMITTED RECEIPT: the split fibers and the refinement ceilings, "
     "read as data."),
    ("A-P06", "v14/paper-06-stochastic-split.md", "c350caab17ee",
     "CR-B / paper-06 (terminal): the stochastic split -- the per-interval "
     "invariant-measure law and the splittable count lattice."),
    ("A-P06REC", "v14/code/crb_stochastic_receipt.json", "5ebeec141303",
     "CR-B's COMMITTED RECEIPT: the per-interval law rows (fiber, orbits, "
     "simplex dimension, transitivity) read as data at every count."),
    ("A-P09", "v14/paper-09-renewal-transport.md", "006f96aaa2ff",
     "R6b' / paper-09 (terminal): the renewal-grain transport kernel -- the "
     "support holes at counts 1 and 2, and the unrefinable-record exclusion."),
    ("A-P09REC", "v14/code/r6bp_transport_receipt.json", "9c8f8af07050",
     "R6b''s COMMITTED RECEIPT: the interval classes and the hole cost, read "
     "as data."),
    ("A-D42B1", "v10/code/d42b1_transport_exact.py", "576275d55ecf",
     "THE COMMITTED TRANSPORT GRAMMAR, driven directly: this unit's only "
     "source of admissibility."),
    ("A-D60", "v10/code/d60_crystal_exact.py", "684cdb76552b",
     "D60: the Builder `B` and the delivery helper `dl`, AST-extracted."),
    ("A-D66", "v10/code/d66_arbitration_crystal_exact.py", "3d0516ab106e",
     "D66: CONFLICT-GRID(g, R) -- the committed constructor, AST-extracted "
     "and re-run at its own R = 4 point."),
    ("A-D66OUT", "v10/data/d66_arbitration_crystal_exact.out", "e252529d2586",
     "D66's COMMITTED OUTPUT: the GRID(g=3,R=4) row is READ from this file at "
     "run time and reproduced by driving, never re-typed."),
    ("A-L1", "v11/note-L1-lorentz-no-go-lemma.md", "93ea24591c3c",
     "L-1: the fourth-form clause this unit argues before any test, and the "
     "sentence retracted on 2026-07-28 that no paper may reproduce."),
    ("A-CAT", "v11/note-v11p0a-reproduction-catalog.md", "0cebe543e814",
     "the reproduction catalog 1.6/1.7: the BHS block and the "
     "Kleitman-Rothschild height-control warning."),
]
SOURCE_IDS = [s[0] for s in SOURCES]

# the retracted L-1 sentence: no paper of this line may reproduce it
BANNED_L1 = ("precisely the form U4 tests, and precisely the form the "
             "corpus's strongest relativity result took")

# THE LORENTZIAN RESONANCE, and the second one paper-19's successor register
# named before it could be heard.  Both sentences are REQUIRED in the paper.
LORENTZ_NAMED = ("The induced form is NAMED AND NOT READ: q = [[1, 0], [0, 1]] "
                 "is a positive definite Euclidean form on a nine-site "
                 "lattice, it is not a signature, it is not a metric on any "
                 "continuum, and no Lorentzian reading of it is taken here or "
                 "licensed by anything measured here.")

LINES = []
QUIET = False
MUT = None
READS = []


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
# SECTION 1.  MACHINERY -- the gate ledger, the seal, the text normaliser
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


SEALED_PATHS = [
    ("SEAL-SCHEMA", "schema", "G-PROVENANCE"),
    ("SEAL-PROVENANCE", "provenance", "G-PROVENANCE"),
    ("SEAL-VERBATIM", "verbatim_anchors", "G-VERBATIM"),
    ("SEAL-ANCHORS", "anchors", "G-ANCHORS-READ"),
    ("SEAL-I7", "i7", "G-I7-READOUT"),
    ("SEAL-FAMILY", "family", "G-WINDOW-DISCLOSED"),
    ("SEAL-CENSUS", "census", "G-BUDGET-THEOREM"),
    ("SEAL-DRIVEN", "driven", "G-CTRL-BRANCHING"),
    ("SEAL-ARENA", "arena", "G-UNIT-GRADE"),
    ("SEAL-WELD", "weld", "G-TWO-WAY"),
    ("SEAL-SPLIT", "split", "G-LAWS-OVER-RECORDS"),
    ("SEAL-PRICE", "price", "G-PRICE-ROW"),
    ("SEAL-WALLS", "walls", "G-WALL-LORENTZ-NAMED"),
    ("SEAL-VERDICT", "verdict", "G-VERDICT-RECONSTRUCTED"),
    ("SEAL-COUNTS", "counts", "G-VERDICT-RECONSTRUCTED"),
    ("SEAL-PAPER-CLAIMS", "paper_claims", "G-PAPER-CLAIMS"),
    ("SEAL-PAPER-COVERAGE", "paper_coverage", "G-PAPER-HEAD-VERBATIM"),
    ("SEAL-POLARITY", "polarity", "G-PAPER-CLAIM-POLARITY"),
    ("SEAL-COVERAGE", "coverage", "G-COVERAGE"),
    ("SEAL-REACHABILITY", "reachability", "G-REACHABILITY"),
    ("SEAL-WAIVERS", "waiver_ledger", "G-COVERAGE"),
    ("SEAL-MUTANTS", "mutants", "G-COVERAGE"),
    ("SEAL-MUTANT-SWEEP", "mutant_sweep", "G-SWEEP-BOUND"),
    ("SEAL-GATES", "gates", "G-PAPER-COVERAGE-FINAL"),
    ("SEAL-CLOSING", "closing_gates", "G-PAPER-COVERAGE-FINAL"),
    ("SEAL-TOTALS", "totals", "G-PAPER-COVERAGE-FINAL"),
    ("SEAL-TRANSCRIPT", "transcript_head", "G-PAPER-COVERAGE-FINAL"),
]
DECLARED_UNSEALED = ["arithmetic", "python", "seal_manifest",
                     "payload_sha256_12"]
DECLARED_UNSEALED_FROZEN = ("arithmetic", "python", "seal_manifest",
                            "payload_sha256_12")
MEASURED_KEYS = ("census", "driven", "arena", "weld", "split", "price",
                 "family", "anchors", "i7", "counts", "verdict")


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


def read_bytes(rel):
    READS.append(rel)
    with open(os.path.join(REPO, rel), "rb") as fh:
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
         "⁄": "/", " ": " ", "⁴": "4", "∏": "prod"}

_MD_PREFIX = re.compile(r"^(?:\s*(?:>+|[-*+]|\d+[.)])\s+)+")


def mdstrip(s):
    """#125 WITH MARKDOWN-PREFIX NORMALIZATION: strip blockquote markers and
    list-item bullets from the head of every line before matching."""
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
    """the full text-gate normalisation: markdown line prefixes, then
    markdown emphasis and code ticks, then the ASCII fold, then whitespace."""
    return norm(ascii_fold(mdstrip(s).replace("*", "").replace("`", "")))


NEEDLE_FLOOR = 30


def match_needle(hay, needle):
    n = canon(needle)
    if len(n) < NEEDLE_FLOOR:
        raise GateFail("G-VERBATIM :: needle below the #62 length floor: %r"
                       % needle)
    return n in canon(hay)


# ===========================================================================
# SECTION 2.  EXACT ARITHMETIC ON Z_3^2
# ===========================================================================

SITES = tuple((i, j) for i in range(3) for j in range(3))
SITE_INDEX = {s: k for k, s in enumerate(SITES)}
DIRECTIONS = ((1, 0), (0, 1), (1, 1), (1, 2))
I7_LINKS = ((1, 0), (0, 1), (1, 1))
ROUNDS = 4


def zadd(a, b):
    return ((a[0] + b[0]) % 3, (a[1] + b[1]) % 3)


def zmul(k, a):
    return ((k * a[0]) % 3, (k * a[1]) % 3)


SUBGROUPS = {}
for _d in DIRECTIONS:
    SUBGROUPS["<(%d,%d)>" % _d] = frozenset({(0, 0), _d, zmul(2, _d)})


def parallel_class(d):
    """the resolvable partition of AG(2,3) into the three lines of slope d."""
    H = SUBGROUPS["<(%d,%d)>" % d]
    seen, out = set(), []
    for x in SITES:
        L = tuple(sorted(zadd(x, h) for h in H))
        if L not in seen:
            seen.add(L)
            out.append(L)
    return tuple(sorted(out))


CLASS_NAMES = ("ROW", "COL", "DIA", "ANT")
CLASS_DIR = {"ROW": (0, 1), "COL": (1, 0), "DIA": (1, 1), "ANT": (1, 2)}
CLASSES = {k: parallel_class(CLASS_DIR[k]) for k in CLASS_NAMES}
CLASS_OF = {CLASSES[k]: k for k in CLASS_NAMES}
DIAG_SEED = ((0, 0), (1, 1), (2, 2))
CELLS = tuple((x, l) for x in SITES for l in I7_LINKS)


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
    rec(tuple(SITES), [])
    return sorted(out)


def transversals(P):
    return [tuple(t) for t in product(*P)]


def canon_transversals(P):
    """THE DECLARED SEED MENU of a grouping: the k-th member of each group in
    the canonical order, k = 0, 1, 2.  Deterministic, no sampling."""
    return [tuple(g[k] for g in P) for k in range(3)]


def q_of(nvec):
    """I7's own readout: q11 = n_e1, q22 = n_e2, q12 = (n_diag - n_e1 - n_e2)/2."""
    n1, n2, n3 = nvec
    q12 = Fraction(n3 - n1 - n2, 2)
    return Fraction(n1), Fraction(n2), q12, \
        Fraction(n1) * Fraction(n2) - q12 * q12


def admissible(nvec):
    """HA 3.2's own criterion: q nonsingular and positive definite at the
    site, by the exact Sylvester criterion."""
    q11, _q22, _q12, det = q_of(nvec)
    return q11 > 0 and det > 0


def i7_box_admissible(box):
    """RECOMPUTED from I7's own declared count box, not re-typed."""
    pts = []
    for n1 in range(1, box["axis_max"] + 1):
        for n2 in range(1, box["axis_max"] + 1):
            for n3 in range(1, box["diag_max"] + 1):
                if admissible((n1, n2, n3)):
                    pts.append((n1, n2, n3))
    return pts


def chart_orbit(nvec):
    """I7's declared chart group acts by the |X| translations and the d!
    direction relabellings.  On a HOMOGENEOUS record the translations act
    trivially, so the orbit is the relabellings of the two AXIS links."""
    n1, n2, n3 = nvec
    return {(n1, n2, n3), (n2, n1, n3)}


# ===========================================================================
# SECTION 3.  THE COMMITTED GRAMMAR, DRIVEN DIRECTLY
# ===========================================================================

class Grammar:
    """the committed layers, loaded as SINGLE SOURCES.  Nothing in this file
    re-implements an admissibility rule: `candidates_for` IS d42b1's."""

    def __init__(self, texts):
        st = texts["v10/code/d42b1_transport_exact.py"]
        cut = st.index('print("[d42b1')
        self.slice_text = st[:cut]
        self.slice_chars = (cut, len(st))
        ns = {}
        exec(compile(self.slice_text, "d42b1_slice", "exec"), ns)
        self.ns = ns
        self.raw_candidates_for = ns["candidates_for"]
        self.regs_of = ns["regs_of"]
        self.vname = ns["vname"]
        self.V0 = ns["V0"]
        self.memo = {}
        self.memo_hits = 0
        self.memo_calls = 0
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
        # a SECOND builder whose menu is the RAW layer function: the memo is
        # gated rather than trusted, and G-MENU-PURE re-drives a declared set
        # through this builder and compares the records event for event.
        g60raw = self._extract("v10/code/d60_crystal_exact.py", texts, "d60raw",
                               {"candidates_for": self.raw_candidates_for,
                                "event_poset": ns["event_poset"],
                                "V0": self.V0})
        self.B_raw = g60raw["B"]
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
        key = (tuple(hist), tuple(inits))
        got = self.memo.get(key)
        if got is None:
            got = self.raw_candidates_for(list(hist), tuple(inits))
            self.memo[key] = got
        else:
            self.memo_hits += 1
        return got

    def _extract(self, rel, texts, marker, extra, only=None):
        """d60/d66's committed extraction idiom: keep only defs and classes,
        so no module-level statement of theirs can run."""
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


def no_exit(nodes):
    for n in nodes:
        for sub in ast.walk(n):
            if isinstance(sub, ast.Call) and isinstance(sub.func, ast.Attribute):
                if sub.func.attr == "exit":
                    return False
            if isinstance(sub, ast.Call) and isinstance(sub.func, ast.Name):
                if sub.func.id in ("exit", "quit"):
                    return False
    return True


def actor(site):
    return "G%d%d" % site


ACTORS = tuple(actor(s) for s in SITES)
ACTOR_SITE = {actor(s): s for s in SITES}


def drive(G, schedule, supply=True, drop_supply=None,
          drop_arb=None, memo_off=False):
    """THE GENERALIZED SCHEDULE DRIVER, one round wider than paper-19's.
    Exactly d66's CONFLICT-GRID(g, R) cycle -- conflict-supply deliveries from
    the group's seed, g proposals, one g-proposer arbitration won by the seed
    -- with the GROUPING AND THE SEED taken from the schedule instead of being
    hard-wired to rows and columns.  Groups are processed in ascending order of
    their seed's site index and members in ascending site index, which is
    d66's own order at the committed schedule.  Every event is specified by
    its FULL TUPLE and taken from the layer's own menu."""
    b = (G.B_raw if memo_off else G.B)(ACTORS)
    cur = {a: G.V0 for a in ACTORS}
    dropped = 0
    narb = 0
    for _rnd, (groups, seeds) in enumerate(schedule):
        order = sorted(range(len(groups)),
                       key=lambda gi: SITE_INDEX[seeds[gi]])
        for gi in order:
            grp = [actor(s) for s in sorted(groups[gi])]
            sd = actor(seeds[gi])
            base = cur[sd]
            for a in grp:
                if a == sd or cur[a] == base:
                    continue
                if not supply:
                    continue
                if drop_supply is not None and dropped == drop_supply:
                    dropped += 1
                    continue
                dropped += 1
                b.pick((sd, a),
                       lambda e, s=sd, r=a, v=base: (e[0] == "d" and e[1] == s
                                                     and e[2] == r
                                                     and e[3] == v),
                       "supply %s->%s" % (sd, a))
                if b.refusal:
                    return b
            trips = [(a, base, 0 if a == sd else 1) for a in grp]
            for t in trips:
                b.pick((t[0],), lambda z, e=("p",) + t: z == e,
                       "propose %s" % t[0])
                if b.refusal:
                    return b
            ckey = frozenset(trips)
            wkey = frozenset({[t for t in trips if t[0] == sd][0]})
            if drop_arb is not None and narb == drop_arb:
                narb += 1
                continue
            narb += 1
            b.pick((sd,), lambda z, e=("r", sd, ckey, wkey): z == e,
                   "arbitrate %s" % sd)
            if b.refusal:
                return b
            v = G.vname(base, wkey, sd)
            for a in grp:
                cur[a] = v
    return b


BUILD_CACHE = {}


def branching_control(G, schedule):
    """THE UNDER-SPECIFIED CONTROL, MADE REPRODUCIBLE.  The record is replayed
    up to its first arbitration, ONE under-specified pick is made, the
    builder's own `maxhits` is read, and the run STOPS: d60's `pick` breaks
    ties with sorted(key=repr) and a frozenset's repr depends on the
    interpreter's per-process string hashing, so WHICH candidate an
    under-specified pick selects is not reproducible across runs -- the COUNT
    is, and a control that continued past one such pick would carry that
    irreproducibility into every later menu size."""
    b0 = drive(G, schedule)
    first = min(k for k, e in enumerate(b0.H) if e[0] == "r")
    seed = b0.H[first][1]
    b = G.B(ACTORS)
    b.H = list(b0.H[:first])
    b.pick((seed,), lambda z, s=seed: z[0] == "r" and z[1] == s,
           "arbitrate* %s" % seed)
    return b.maxhits, first, seed


def record_of(G, b, actors=None):
    """the record's published shape.  `actors` is the site-object pool the
    footprints are cut to; it defaults to the grid's own nine."""
    keep = set(ACTOR_SITE) if actors is None else set(actors)
    divs = [e for e in b.H if e[0] == "r"]
    foot = [frozenset(r for r in G.regs_of(e) if r in keep) for e in divs]
    return {"events": len(b.H), "maxhits": b.maxhits, "refusal": b.refusal,
            "divisions": len(divs), "footprints": foot,
            "initiators": [e[1] for e in divs],
            "kinds": [e[0] for e in b.H]}


def driven(G, schedule):
    """cached, mutant-independent: the record is a property of the schedule."""
    if schedule not in BUILD_CACHE:
        b = drive(G, schedule)
        BUILD_CACHE[schedule] = record_of(G, b)
    return BUILD_CACHE[schedule]


def link_field_of(footprints):
    """the DRIVEN link field: for a link l and a site x, the number of division
    events whose register footprint contains both x and x + l."""
    out = {}
    for x in SITES:
        for l in I7_LINKS:
            y = zadd(x, l)
            out[(x, l)] = sum(1 for f in footprints
                              if actor(x) in f and actor(y) in f)
    return out


# ===========================================================================
# SECTION 4/5.  THE R = 4 FAMILY, THE PACKED COLUMNS AND THE DECLARED WINDOW
# ===========================================================================

def pack4(vec27):
    """the link field packed at FOUR bits per cell, so four rounds -- whose
    per-cell count cannot exceed 4 -- can never carry into a neighbouring
    cell.  Cells are site-major, link-minor, in the declared orders."""
    v = 0
    for i, c in enumerate(vec27):
        v |= c << (4 * i)
    return v


def round_vec(P):
    """the per-(site, link) incidence 27-vector of ONE round's grouping: cell
    (x, l) carries 1 exactly when x and x + l share a conflict group."""
    return tuple(1 if any(x in g and zadd(x, l) in g for g in P) else 0
                 for (x, l) in CELLS)


RAW = {}


def raw_census():
    """the whole combinatorial substrate, computed once."""
    if RAW:
        return RAW
    parts = all_partitions()
    vecs = [round_vec(P) for P in parts]
    RAW["parts"] = parts
    RAW["vecs"] = vecs
    RAW["packed"] = [pack4(v) for v in vecs]
    RAW["masks"] = [sum(1 << i for i in range(27) if v[i]) for v in vecs]
    RAW["incidences"] = [sum(v) for v in vecs]
    RAW["sat"] = [i for i, v in enumerate(vecs) if sum(v) == 9]
    RAW["class_index"] = {k: parts.index(CLASSES[k]) for k in CLASS_NAMES}
    return RAW


# the per-site 12-bit code table: nibbles a = n_(1,0), b = n_(0,1), c = n_(1,1).
# 4*det is an integer, so the census runs in integers and the Fraction is
# formed only for reporting.
CODE_TAB = {}
for _a in range(5):
    for _b in range(5):
        for _c in range(5):
            _d4 = 4 * _a * _b - (_c - _a - _b) ** 2
            CODE_TAB[_a | (_b << 4) | (_c << 8)] = (
                _d4,
                1 if (_a > 0 and _d4 > 0) else 0,          # POSDEF
                1 if min(_a, _b, _c) >= 1 else 0,          # COVERED
                1 if _d4 != 0 else 0)                      # NON-DEGENERATE


def site_codes(packed):
    return tuple((packed >> (12 * k)) & 0xFFF for k in range(9))


def unpack_field(packed):
    return {CELLS[i]: (packed >> (4 * i)) & 0xF for i in range(27)}


def field_vec(packed):
    return tuple((packed >> (4 * i)) & 0xF for i in range(27))


# d66's own R = 4 point: the committed constructor alternates ROW and COLUMN
# with the diagonal seed, four rounds.
COMMITTED_R4 = tuple((CLASSES[c], DIAG_SEED)
                     for c in ("ROW", "COL", "ROW", "COL"))
# the declared collinear G-FLAT arrangement: the three link-direction parallel
# classes with the diagonal class taken twice -- the R = 4 successor of
# paper-19's uniform ROW/COL/DIA arrangement.
COLLINEAR_FLAT = ("ROW", "COL", "DIA", "DIA")
SEEDS_PER_ROUND_IN_WINDOW = 1


def flat_quadruples():
    """EXHAUSTIVE over the 36^4 quadruples of saturating groupings: every
    ordered quadruple whose summed link field is I7's G-FLAT (1,1,2) at all
    nine sites.  Packed route."""
    R = raw_census()
    F = [R["packed"][i] for i in R["sat"]]
    tgt = pack4(tuple([1, 1, 2] * 9))
    out = []
    for ia, a in enumerate(F):
        for ib, b in enumerate(F):
            ab = a + b
            for ic, c in enumerate(F):
                abc = ab + c
                for idx, d in enumerate(F):
                    if abc + d == tgt:
                        out.append((R["sat"][ia], R["sat"][ib],
                                    R["sat"][ic], R["sat"][idx]))
    return out


def flat_quadruples_route2():
    """THE INDEPENDENT ROUTE: no packing, no target constant -- the summed
    27-vector is compared entry by entry against the field I7's own committed
    G-FLAT row induces.  Shares no code and no typed literal with route 1."""
    R = raw_census()
    V = [R["vecs"][i] for i in R["sat"]]
    n = 0
    for a in V:
        for b in V:
            ab = [a[k] + b[k] for k in range(27)]
            for c in V:
                abc = [ab[k] + c[k] for k in range(27)]
                if any(abc[k] > I7_TARGET_VEC[k] for k in range(27)):
                    continue
                for d in V:
                    ok = True
                    for k in range(27):
                        want = I7_TARGET_VEC[k]
                        if abc[k] + d[k] != want:
                            ok = False
                            break
                    if ok:
                        n += 1
    return n


I7_TARGET_VEC = None       # filled from I7's own committed row at run time


def window_schedules():
    """THE DECLARED DRIVEN WINDOW W4, disclosed here and in the head.

    W4-CLASS:   all 4^4 ordered quadruples of the parallel classes of AG(2,3)
                -- d66's own resolvable device extended two rounds.
    W4-FLAT:    ALL 276 G-FLAT-inducing grouping quadruples -- the pin's
                primary object, in the window ENTIRE and not sampled.
    W4-SEEDFAN: the declared collinear arrangement at ALL 3^4 canonical
                transversal quadruples -- the seed axis, exhausted at one
                grouping.
    W4-CTRL:    d66's own committed R = 4 point and this unit's declared
                falsifiers.
    The bulk is taken at the first SEEDS_PER_ROUND_IN_WINDOW canonical
    transversal of each round.  Deterministic order, no sampling."""
    R = raw_census()
    parts = R["parts"]
    quads, tags = [], []
    for a in CLASS_NAMES:
        for b in CLASS_NAMES:
            for c in CLASS_NAMES:
                for d in CLASS_NAMES:
                    quads.append(tuple(CLASSES[k] for k in (a, b, c, d)))
                    tags.append("W4-CLASS")
    for q in FLAT_QUADS:
        quads.append(tuple(parts[i] for i in q))
        tags.append("W4-FLAT")
    quads.append(tuple(P for P, _s in COMMITTED_R4))
    tags.append("W4-CTRL")
    out, seen, meta = [], set(), {}
    for T, tag in zip(quads, tags):
        menus = [canon_transversals(P)[:SEEDS_PER_ROUND_IN_WINDOW] for P in T]
        for s0 in menus[0]:
            for s1 in menus[1]:
                for s2 in menus[2]:
                    for s3 in menus[3]:
                        sch = ((T[0], s0), (T[1], s1), (T[2], s2), (T[3], s3))
                        if sch in seen:
                            continue
                        seen.add(sch)
                        out.append(sch)
                        meta[sch] = tag
    T = tuple(CLASSES[k] for k in COLLINEAR_FLAT)
    menus = [canon_transversals(P) for P in T]
    for s0 in menus[0]:
        for s1 in menus[1]:
            for s2 in menus[2]:
                for s3 in menus[3]:
                    sch = ((T[0], s0), (T[1], s1), (T[2], s2), (T[3], s3))
                    if sch in seen:
                        continue
                    seen.add(sch)
                    out.append(sch)
                    meta[sch] = "W4-SEEDFAN"
    return out, meta


FLAT_QUADS = []
WINDOW = {}
WINDOW_META = {}


def window_drive(G):
    if WINDOW:
        return WINDOW
    sch_list, meta = window_schedules()
    WINDOW_META.update(meta)
    for sch in sch_list:
        WINDOW[sch] = driven(G, sch)
    return WINDOW


def packed_of_schedule(sch):
    R = raw_census()
    idx = {P: i for i, P in enumerate(R["parts"])}
    v = 0
    for (P, _s) in sch:
        v += R["packed"][idx[P]]
    return v


# ===========================================================================
# SECTION 6.  WELD 2'S DETECTOR, CARRIED UNCHANGED
# ===========================================================================

def cayley_edges(X, links, Lmod):
    tgt = set()
    for x in X:
        for lk in links:
            y = tuple((x[i] + lk[i]) % Lmod for i in range(len(lk)))
            tgt.add((x, y))
            tgt.add((y, x))
    return tgt


def graph_isomorphisms(S, rel_set, X, links, Lmod, directed=False):
    """ALL bijections S -> X carrying the site-object incidence onto the
    target's Cayley incidence, by exhaustive backtracking.  No sampling and no
    cap.  THE DECLARED CRITERION IS THE UNDIRECTED ONE, on both branches, for
    weld 2's reason: a link is an unordered site pair carrying a label and a
    count, and orientation is a declared free item."""
    tgt = set()
    for x in X:
        for lk in links:
            y = tuple((x[i] + lk[i]) % Lmod for i in range(len(lk)))
            tgt.add((x, y))
            if not directed:
                tgt.add((y, x))
    src = set()
    for (u, v) in rel_set:
        if u != v:
            src.add((u, v))
            if not directed:
                src.add((v, u))
    Ss = sorted(S, key=str)
    Xs = sorted(X)
    out, phi, used = [], {}, set()

    def bt(k):
        if k == len(Ss):
            out.append(dict(phi))
            return
        u = Ss[k]
        for x in Xs:
            if x in used:
                continue
            ok = True
            for j in range(k):
                w = Ss[j]
                if ((u, w) in src) != ((x, phi[w]) in tgt) or \
                   ((w, u) in src) != ((phi[w], x) in tgt):
                    ok = False
                    break
            if ok:
                phi[u] = x
                used.add(x)
                bt(k + 1)
                used.discard(x)
                del phi[u]
    if len(Ss) == len(Xs):
        bt(0)
    return out


def quotient_bijections(S, rel_set, X, links, Lmod):
    """THE QUOTIENT READING at a nine-object arena: a SURJECTION of the
    realised objects onto the sites -- here necessarily a bijection -- under
    which EVERY realised edge carries a declared link displacement."""
    tgt = cayley_edges(X, links, Lmod)
    src = {(u, v) for (u, v) in rel_set if u != v}
    Ss = sorted(S, key=str)
    Xs = sorted(X)
    out, phi, used = [], {}, set()

    def bt(k):
        if k == len(Ss):
            out.append(dict(phi))
            return
        u = Ss[k]
        for x in Xs:
            if x in used:
                continue
            ok = True
            for j in range(k):
                w = Ss[j]
                if (u, w) in src and (x, phi[w]) not in tgt:
                    ok = False
                    break
                if (w, u) in src and (phi[w], x) not in tgt:
                    ok = False
                    break
            if ok:
                phi[u] = x
                used.add(x)
                bt(k + 1)
                used.discard(x)
                del phi[u]
    if len(Ss) == len(Xs):
        bt(0)
    return out


def count_field(rel, X, links, Lmod, assign, labelperm, orient):
    """weld 2's induced count field s : X x L -> Z.  `assign` maps a site
    object to a site; `labelperm` permutes the declared link labels; `orient`
    flips the link direction."""
    inv = {assign[u]: u for u in assign}
    out = {}
    for x in X:
        for i, lk in enumerate(links):
            lk2 = links[labelperm[i]]
            step = tuple((-c) % Lmod for c in lk2) if orient else lk2
            y = tuple((x[k] + step[k]) % Lmod for k in range(len(step)))
            out[(x, lk)] = rel.get((inv[x], inv[y]), 0)
    return out


def fkey(f):
    return tuple(sorted(((str(k), v) for k, v in f.items())))


def codivision_rel(actors, footprints):
    """the co-division incidence on the ordered actor pair: a division event
    is ON the pair when its register footprint meets both endpoints."""
    rel = {}
    for u in actors:
        for v in actors:
            if u == v:
                continue
            rel[(u, v)] = sum(1 for f in footprints if u in f and v in f)
    return rel


DETECT_CACHE = {}
PRICE_CACHE = {}
BACK_CACHE = {}


def detect(arena, target, reading):
    """ONE CENSUS ROW.  Every fate is a MEASURED outcome with its number."""
    ckey = (tuple(sorted((str(k), v) for k, v in arena["rel"].items())),
            target["name"], reading, arena["name"])
    if ckey in DETECT_CACHE:
        return json.loads(json.dumps(DETECT_CACHE[ckey]))
    row = _detect(arena, target, reading)
    DETECT_CACHE[ckey] = json.loads(json.dumps(row, default=str))
    return json.loads(json.dumps(DETECT_CACHE[ckey]))


def _detect(arena, target, reading):
    X, links, Lmod = target["X"], target["links"], target["Lmod"]
    row = {"arena": arena["name"], "reading": reading,
           "site_gen": "ACTOR", "link_gen": "CO-DIVISION-ACTOR-PAIR",
           "count_gen": "DIVISION-COUNT-IN-THE-DECLARED-WINDOW",
           "arity_repair": "NONE", "target": target["name"]}
    objs = sorted(arena["actors"])
    rel = arena["rel"]
    row["site_arity"] = len(objs)
    if len(objs) != len(X):
        row["fate"] = "ARITY-DEAD"
        row["reason"] = ("%d site objects against the target's %d; no repair "
                         "declared, and a declared restriction can only shrink "
                         "a site set" % (len(objs), len(X)))
        return row
    realised = {k for k, n in rel.items() if n > 0}
    if reading == "EMBEDDING":
        maps = graph_isomorphisms(objs, realised, X, links, Lmod)
        row["isomorphisms"] = len(maps)
        row["isomorphisms_directed_comparator"] = len(
            graph_isomorphisms(objs, realised, X, links, Lmod, directed=True))
    else:
        maps = quotient_bijections(objs, realised, X, links, Lmod)
        row["quotient_maps"] = len(maps)
    if not maps:
        row["fate"] = "STRUCT-DEAD"
        row["reason"] = ("0 of the %d! bijections carry the site incidence "
                         "%s the target's link structure"
                         % (len(objs),
                            "onto" if reading == "EMBEDDING" else "into"))
        return row
    nlab = len(links)
    base_field = count_field(rel, X, links, Lmod, maps[0],
                             tuple(range(nlab)), False)
    row["count_cells"] = len(base_field)
    row["count_min"] = min(base_field.values())
    row["count_max"] = max(base_field.values())
    if row["count_min"] < 1:
        zeros = sorted(str(k) for k, v in base_field.items() if v == 0)
        row["fate"] = "COUNT-DEAD"
        row["reason"] = ("n_l(x) must lie in Z_>0 (HA 3.1); the induced count "
                         "is 0 at %d of %d cells"
                         % (len(zeros), len(base_field)))
        row["zero_cells"] = len(zeros)
        return row
    fields = {}
    for i, phi in enumerate(maps):
        for lp in permutations(range(nlab)):
            for orient in (False, True):
                fields[(i, lp, orient)] = count_field(rel, X, links, Lmod,
                                                      phi, lp, orient)
    fib_site = len({fkey(fields[(i, tuple(range(nlab)), False)])
                    for i in range(len(maps))})
    fib_label = len({fkey(fields[(0, lp, False)])
                     for lp in permutations(range(nlab))})
    fib_orient = len({fkey(fields[(0, tuple(range(nlab)), o)])
                      for o in (False, True)})
    lab_at = {len({fkey(fields[(i, lp, False)])
                   for lp in permutations(range(nlab))})
              for i in range(len(maps))}
    ori_at = {len({fkey(fields[(i, tuple(range(nlab)), o)])
                   for o in (False, True)})
              for i in range(len(maps))}
    row["fibers_base_map_invariant"] = (lab_at == {fib_label}
                                        and ori_at == {fib_orient})
    row["label_fiber_spread"] = sorted(lab_at)
    row["orient_fiber_spread"] = sorted(ori_at)
    lab_i = [len({fkey(fields[(i, lp, False)])
                  for lp in permutations(range(nlab))})
             for i in range(len(maps))]
    ori_i = [len({fkey(fields[(i, tuple(range(nlab)), o)])
                  for o in (False, True)}) for i in range(len(maps))]
    row["free_items_at_every_base_map"] = min(
        (1 if fib_site > 1 else 0) + (1 if lab_i[i] > 1 else 0)
        + (1 if ori_i[i] > 1 else 0) for i in range(len(maps)))
    row["base_maps_read"] = len(maps)
    inv = {"I-SITE-ASSIGNMENT": fib_site,
           "I-DIRECTION-LABEL": fib_label, "I-ORIENT": fib_orient}
    row["inventory"] = inv
    free = sorted(k for k, v in inv.items() if v > 1)
    row["free_items"] = free
    row["fate"] = "FOUND-candidate" if not free else "UNMOTIVATED"
    row["reason"] = ("zero free items at the RSQ standard" if not free else
                     "%d genuinely free item(s): %s"
                     % (len(free),
                        ", ".join("%s fiber %d" % (k, inv[k]) for k in free)))
    # the fields the free site assignment actually produces, as RECORDS
    if fib_site > 1 or True:
        seen = {}
        for i in range(len(maps)):
            f = fields[(i, tuple(range(nlab)), False)]
            seen[fkey(f)] = f
        recs = []
        for f in seen.values():
            codes = sorted({tuple(f[(x, lk)] for lk in links) for x in X})
            recs.append(tuple(codes))
        row["assignment_fiber_records"] = len(seen)
        row["assignment_fiber_code_sets"] = len(set(recs))
        row["assignment_fiber_homogeneous"] = sorted(
            {r[0] for r in recs if len(r) == 1})
        row["assignment_fiber_all_admissible"] = all(
            admissible(c) for r in recs for c in r)
    row["count_field"] = sorted((str(k), v) for k, v in base_field.items())
    row["induced_record_at_the_base_map"] = sorted(
        {tuple(base_field[(x, lk)] for lk in links) for x in X})
    return row


# ===========================================================================
# SECTION 7.  THE #62 VERBATIM ANCHORS, BOUND TO THEIR CONSUMER GATES
# ===========================================================================

VERBATIM = [
    ("V01", "A-PIN",
     "confirm the 276 G-FLAT-inducing quadruples; gate FORCED/BRANCHING/"
     "REFUSED", "G-276"),
    ("V02", "A-PIN",
     "the R=4 welded record splittable (split fiber > 0 at any interval",
     "G-SPLIT-FIBER"),
    ("V03", "A-PIN",
     "measure WHICH of the terminal refinement laws (papers 04/06/09) become "
     "non-empty on it", "G-LAWS-OVER-RECORDS"),
    ("V04", "A-R3WEFF",
     "G-FLAT is reachable, at 276 ordered quadruples (det = 1, admissible); "
     "its chart-orbit siblings", "G-276"),
    ("V05", "A-R3WEFF",
     "the refinement grammar (paper-04), the stochastic split (paper-06) and "
     "the renewal-transport kernel (paper-09, which excludes exactly the "
     "unrefinable records) are empty on the record the weld lands on",
     "G-LAWS-OVER-RECORDS"),
    ("V06", "A-P19",
     "The weld reaches a record; it does not yet reach a law over records.",
     "G-LAWS-OVER-RECORDS"),
    ("V07", "A-P19",
     "At R = 3 the rigidity theorem makes (1,1,1) the only reachable "
     "I7-STRICT record, so no R = 3 schedule can reach a declared record at "
     "all", "G-BUDGET-THEOREM"),
    ("V08", "A-P19",
     "the fibers computed as the number of distinct count fields each choice "
     "produces", "G-WELD-FIBERS"),
    ("V09", "A-P19",
     "Zero free items -- the RSQ standard's definition of MOTIVATED",
     "G-RSQ-THEOREM"),
    ("V10", "A-HA",
     "A record is admissible when $q$ is nonsingular and positive definite at "
     "every site, by the exact Sylvester criterion", "G-I7-READOUT"),
    ("V11", "A-HA",
     "A predicate that cannot return its other value anywhere in the declared "
     "arena is not a measurement", "G-TWO-WAY"),
    ("V12", "A-P04",
     "A count-1 interval cannot be split into two strictly positive parts",
     "G-SPLIT-FIBER"),
    ("V13", "A-P04",
     "3 of the 9 admissible records carry a count-1 interval and admit no "
     "subdivision at all: G-ANISO, G-CURVED, G-FLAT", "G-LAW-04"),
    ("V14", "A-P04",
     "The declared flat record sits at the count floor, and it is the floor, "
     "not the flatness, that forbids refinement.", "G-SCALE-ROW"),
    ("V15", "A-P04",
     "inserting one site into one link breaks that. The class is refused with "
     "its reason, not skipped.", "G-LAW-04"),
    ("V16", "A-P06",
     "Three of the nine admissible records -- G-ANISO, G-CURVED, G-FLAT -- "
     "carry a count-1 interval and admit no subdivision at all.", "G-LAW-06"),
    ("V17", "A-P09",
     "There is no inter-renewal leg of length one or two, exactly.",
     "G-KERNEL-HOLE"),
    ("V18", "A-P09",
     "Three admissible records -- G-ANISO, G-CURVED, G-FLAT -- have R6a split "
     "fiber zero: they admit no subdivision at all", "G-LAW-09"),
    ("V19", "A-L1",
     "fourth form, outside paper 8's three**, and its admissibility is v11's "
     "to argue when U4 runs", "G-WALL-L1"),
    ("V20", "A-CAT",
     "a Poisson sprinkling admits no Lorentz-invariant finite-valency graph",
     "G-WALL-BHS"),
    ("V21", "A-CAT",
     "a dimension reading without a height control is worthless",
     "G-WALL-KR"),
]


def source_text(texts, sid):
    rel = [s[1] for s in SOURCES if s[0] == sid][0]
    return texts[rel]


def read_d66_row(text, tag):
    """READ d66's own committed output row, never re-typed."""
    for line in text.split("\n"):
        if line.strip().startswith(tag + " ") or line.strip() == tag:
            m = re.search(r"n=\s*(\d+)\s+arbs=\s*(\d+).*?deliveries=\s*(\d+)",
                          line)
            if m:
                return tuple(int(g) for g in m.groups())
    return None


def i7_arena(rec_bytes):
    """I7's arena READ AS DATA from its pinned receipt, never re-authored."""
    rec = json.loads(rec_bytes)
    D = rec["declarations"]
    links = [tuple(v) for v in D["links_d2"]]
    fam = {nm: tuple(D["records_d2"][nm]) for nm in sorted(D["records_d2"])}
    X = [(i, j) for i in range(D["L"]) for j in range(D["L"])]
    inhom = {}
    inhom["G-CURVED"] = {x: tuple(sum((1 + x[j]) for j in range(D["d"])
                                      if lk[j]) for lk in
                                  [tuple(v) for v in D["links_d2"]])
                         for x in X}

    def _curvoff(x, lk, d=D["d"]):
        b = [2 + x[j] for j in range(d)]
        cross = 1 + (x[0] * x[1]) % 2
        s0 = sum(b[j] for j in range(d) if lk[j])
        prs = sum(1 for i2 in range(d) for j2 in range(i2 + 1, d)
                  if lk[i2] and lk[j2])
        return s0 + 2 * cross * prs
    inhom["G-CURVOFF"] = {x: tuple(_curvoff(x, tuple(lk))
                                   for lk in D["links_d2"]) for x in X}
    return {"d": D["d"], "L": D["L"], "links": links, "family": fam,
            "site_dependent_family": inhom, "box": D["count_lattice"],
            "committed_admissible_points":
                rec["tables"]["link_locality_lattice"]["admissible_points"],
            "chart_group": D["chart_group"],
            "reencode": rec["tables"]["readout_reencoding"]}


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


# ===========================================================================
# SECTION 8.  THE RUN
# ===========================================================================

def full_run(break_anchor=None, paper_text=None, paper_rel=PAPER_REL,
             do_paper=True):
    global I7_TARGET_VEC
    LD = Ledger()
    SEAL = Seal()
    R = {"schema": SCHEMA}
    del READS[:]

    # ---------------- SEC 1  PROVENANCE ---------------------------------
    say("=" * 78)
    say("v14 R=4 -- THE DECLARED-RECORD WELD AND THE SPLITTABLE QUESTION")
    say("paper %s   pin v14/note-r4dec-pin.md" % PAPER_REL)
    say("=" * 78)
    say("\n[SEC 1] PROVENANCE")
    texts, prov = {}, []
    for sid, rel, sha, why in SOURCES:
        raw = read_bytes(rel)
        got = hashlib.sha256(raw).hexdigest()[:12]
        want = sha if sid != break_anchor else "0" * 12
        prov.append({"id": sid, "path": rel, "declared": want, "measured": got,
                     "match": got == want, "why": why, "bytes": len(raw)})
        texts[rel] = raw.decode("utf-8")
    R["provenance"] = prov
    LD.gate("G-PROVENANCE",
            "THE %d RUNTIME SOURCES ARE PINNED BY CONTENT (#46/#91).  Every "
            "file this run reads is declared in the frozen table above with "
            "its sha256-12; the digest is recomputed from the bytes read and "
            "compared.  --break-anchor NAME corrupts any one of them and the "
            "run dies here" % len(SOURCES),
            all(p["match"] for p in prov),
            "; ".join("%s %s" % (p["id"], "ok" if p["match"] else
                                 "MISMATCH %s!=%s" % (p["measured"],
                                                      p["declared"]))
                      for p in prov))
    SEAL.take("SEAL-SCHEMA", R)
    SEAL.take("SEAL-PROVENANCE", R)
    declared_reads = sorted(s[1] for s in SOURCES)
    actual = sorted(set(READS))
    LD.gate("G-READS-DECLARED",
            "THE READ SET IS EXACTLY THE DECLARED SET.  Nothing outside the "
            "%d pinned sources is opened, and every path is resolved from "
            "this module's own location rather than from the working "
            "directory, so the run is correct OFF-TREE and with NO VERSION "
            "CONTROL present" % len(SOURCES),
            actual == declared_reads,
            "declared %d, read %d, difference %s"
            % (len(declared_reads), len(actual),
               sorted(set(actual) ^ set(declared_reads)) or "none"))
    src = read_text(SELF)
    tree = ast.parse(src)
    floats = [n for n in ast.walk(tree)
              if isinstance(n, ast.Constant) and isinstance(n.value, float)]
    truediv = [n for n in ast.walk(tree) if isinstance(n, ast.BinOp)
               and isinstance(n.op, ast.Div)]
    LD.gate("G-EXACT-ARITHMETIC",
            "EXACT ARITHMETIC, SCANNED RATHER THAN PROMISED.  An AST scan of "
            "this file finds no float literal and no true division anywhere; "
            "every quotient is a Fraction or an integer floor division",
            not floats and not truediv,
            "float literals %d, true divisions %d" % (len(floats),
                                                      len(truediv)))
    mods = set()
    for n in ast.walk(tree):
        if isinstance(n, ast.Import):
            mods.update(a.name.split(".")[0] for a in n.names)
        elif isinstance(n, ast.ImportFrom) and n.module:
            mods.add(n.module.split(".")[0])
    LD.gate("G-NO-SUBPROCESS",
            "NO SUBPROCESS OF ANY KIND (#91 off-tree/git-less).  The import "
            "set is scanned: no `subprocess`, no `shutil`, no `socket`, no "
            "`urllib`.  A run inside a mirror holding only the pinned sources "
            "and no version control produces the same bytes",
            not (mods & {"subprocess", "shutil", "socket", "urllib",
                         "multiprocessing", "requests"}),
            "imports %s" % sorted(mods))
    vrows = []
    for vid, sid, needle, gname in VERBATIM:
        hay = source_text(texts, sid)
        ok = match_needle(hay, needle)
        vrows.append({"id": vid, "source": sid, "needle": needle,
                      "canon_len": len(canon(needle)), "found": ok,
                      "consumer_gate": gname})
    if mut("MUT-VERBATIM"):
        vrows[0]["found"] = False
    R["verbatim_anchors"] = vrows
    LD.gate("G-VERBATIM",
            "THE #62 ANCHORS ARE MATCHED IN THE PINNED BYTES.  %d needles, "
            "each above the %d-character canonical floor, each naming the "
            "gate that consumes it; both sides of every match are "
            "whitespace-normalised, ASCII-folded and stripped of markdown "
            "line prefixes, so a needle spanning a block quote or a numbered "
            "list cannot be evaded by re-wrapping"
            % (len(vrows), NEEDLE_FLOOR),
            all(v["found"] for v in vrows),
            "anchors %d, missing %s" % (len(vrows),
                                        [v["id"] for v in vrows
                                         if not v["found"]] or "none"))
    SEAL.take("SEAL-VERBATIM", R)

    # ---------------- I7's ARENA, READ AS DATA --------------------------
    i7 = i7_arena(source_text(texts, "A-I7").encode("utf-8"))
    boxpts = i7_box_admissible(i7["box"])
    FLAT = tuple(i7["family"]["G-FLAT"])
    I7_TARGET_VEC = tuple(FLAT[li] for _x in SITES for li in range(3))
    anchors = []
    nbox = pick("MUT-ANCHORS", len(boxpts), len(boxpts) + 1)
    anchors.append({"id": "N-I7-BOX",
                    "committed": i7["committed_admissible_points"],
                    "computed": nbox, "source": "A-I7",
                    "match": nbox == i7["committed_admissible_points"]})
    M = [[1, 0, 0], [0, 1, 0], [1, 1, 2]]
    detM = (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
            - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
            + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))
    anchors.append({"id": "N-READOUT-DET",
                    "committed": int(i7["reencode"]["determinant"]),
                    "computed": detM, "source": "A-I7",
                    "match": int(i7["reencode"]["determinant"]) == detM})
    p19 = json.loads(source_text(texts, "A-P19REC"))
    reg_probe = p19["geometry"]["r4_register_probe"]
    anchors.append({"id": "N-P19-R4-REGISTER",
                    "committed": reg_probe["reaching_the_target_chart_orbit"],
                    "computed": None, "source": "A-P19REC",
                    "match": None})
    d66out = source_text(texts, "A-D66OUT")
    grid34 = read_d66_row(d66out, "GRID(g=3,R=4)")
    anchors.append({"id": "N-D66-GRID34", "committed": list(grid34),
                    "computed": None, "source": "A-D66OUT", "match": None})
    R["i7"] = {"links": [list(l) for l in i7["links"]],
               "record_family": {k: list(v) for k, v in i7["family"].items()},
               "site_dependent_records": sorted(i7["site_dependent_family"]),
               "box": i7["box"], "box_admissible_points": len(boxpts),
               "chart_group": i7["chart_group"],
               "target_name": "G-FLAT", "target_record": list(FLAT),
               "target_admissible": admissible(FLAT),
               "target_q": [[str(q_of(FLAT)[0]), str(q_of(FLAT)[2])],
                            [str(q_of(FLAT)[2]), str(q_of(FLAT)[1])]],
               "target_det": str(q_of(FLAT)[3]),
               "declared_family_size": len(i7["family"])
               + len(i7["site_dependent_family"]),
               "link_constant_declared_records":
                   sorted(nm for nm, v in i7["family"].items()
                          if len(set(v)) == 1),
               "link_constant_admissible_box_points":
                   sorted(str(p) for p in boxpts if len(set(p)) == 1)}
    ha = source_text(texts, "A-HA")
    rt = [nm for nm in sorted(i7["family"])
          if not admissible(i7["family"][nm])]
    adm_names = sorted(nm for nm in i7["family"] if admissible(i7["family"][nm]))
    LD.gate("G-I7-READOUT",
            "THE READOUT IS I7's OWN, matched verbatim in its pinned bytes "
            "and used unchanged: q11 = n_e1, q22 = n_e2, "
            "q12 = (n_(e1+e2) - n_e1 - n_e2)/2, the invertible linear "
            "re-encoding whose determinant I7 measured at 2 and this run "
            "recomputes.  Applied to I7's OWN declared record family it "
            "separates %d admissible records from %d inadmissible ones.  THE "
            "TARGET IS I7's OWN COMMITTED G-FLAT ROW, read from its receipt: "
            "%s, q = [[%s, %s], [%s, %s]], det = %s"
            % (len(adm_names), len(rt), str(FLAT), q_of(FLAT)[0], q_of(FLAT)[2],
               q_of(FLAT)[2], q_of(FLAT)[1], q_of(FLAT)[3]),
            match_needle(ha, VERBATIM[9][2]) and detM == 2 and adm_names
            and admissible(FLAT),
            "re-encoding determinant %d; admissible declared records %s; "
            "rejected %s; target %s admissible %s det %s"
            % (detM, adm_names, rt, str(FLAT), admissible(FLAT),
               q_of(FLAT)[3]))
    SEAL.take("SEAL-I7", R)
    R["anchors"] = anchors
    LD.gate("G-ANCHORS-READ",
            "%d numbers are READ from committed files at run time and either "
            "RECOMPUTED here or carried as the committed side of a later "
            "gate, never re-typed: I7's own admissible-point count for its "
            "declared count box, I7's readout re-encoding determinant, "
            "paper-19's own R = 4 register row, and d66's own GRID(g=3,R=4) "
            "row" % len(anchors),
            all(a["match"] for a in anchors if a["match"] is not None)
            and grid34 is not None,
            "; ".join("%s committed=%s computed=%s" %
                      (a["id"], a["committed"], a["computed"])
                      for a in anchors))
    SEAL.take("SEAL-ANCHORS", R)
    # ---------------- SEC 2  THE FAMILY AND THE WINDOW ------------------
    say("\n[SEC 2] THE R = 4 FAMILY, THE BUDGET THEOREM AND THE DECLARED WINDOW")
    C = raw_census()
    nparts_enum = len(C["parts"])
    fact = 1
    for k in range(2, 10):
        fact *= k
    nparts_closed = fact // (6 * 6 * 6 * 6)
    LD.gate("G-PARTITION-COUNT",
            "THE ROUND'S OWN FAMILY, COUNTED TWICE BY ROUTES THAT SHARE NO "
            "CODE.  A round of the committed cycle partitions the nine sites "
            "into three conflict triples: exhaustive enumeration and the "
            "closed form 9!/(3!^3 3!) must agree",
            nparts_enum == nparts_closed == pick("MUT-FAMILY-COUNT", 280, 281),
            "enumerated %d, closed form %d" % (nparts_enum, nparts_closed))
    maxinc = pick("MUT-BUDGET", max(C["incidences"]), 10)
    inc_hist = Counter(C["incidences"])
    nsat = len(C["sat"])
    need = sum(FLAT) * len(SITES)
    budget = maxinc * ROUNDS
    LD.gate("G-BUDGET-THEOREM",
            "THE BUDGET FORCING, MEASURED AND THEN USED.  No round of this "
            "cycle can deposit more than %d link incidences -- measured "
            "exhaustively over all %d partitions, whose incidence spectrum is "
            "%s -- so four rounds carry at most %d.  I7's own G-FLAT needs "
            "%d.  Equality forces EVERY round to saturate, so the census over "
            "the %d saturating partitions is EXHAUSTIVE OVER THE WHOLE %d^4 "
            "FAMILY and not a restriction of it"
            % (maxinc, nparts_enum, sorted(inc_hist.items()), budget, need,
               nsat, nparts_enum),
            maxinc * ROUNDS == need and nsat == sum(
                1 for v in C["incidences"] if v == maxinc),
            "max per round %d, rounds %d, budget %d, G-FLAT needs %d, "
            "saturating partitions %d" % (maxinc, ROUNDS, budget, need, nsat))
    R["family"] = {
        "partitions_per_round": nparts_enum,
        "partitions_closed_form": nparts_closed,
        "incidence_spectrum": {str(k): v for k, v in sorted(inc_hist.items())},
        "max_incidences_per_round": maxinc,
        "saturating_partitions": nsat,
        "rounds": ROUNDS,
        "budget": budget,
        "g_flat_needs": need,
        "grouping_quadruples": nparts_enum ** ROUNDS,
        "saturating_quadruples": nsat ** ROUNDS,
        "seedings_per_round": len(transversals(C["parts"][0])),
        "schedules_per_round": nparts_enum * len(transversals(C["parts"][0])),
        "schedules": (nparts_enum * len(transversals(C["parts"][0]))) ** ROUNDS,
    }
    reg(nparts_enum, nsat, maxinc, budget, need, nparts_enum ** ROUNDS,
        nsat ** ROUNDS, R["family"]["schedules"], R["family"]["seedings_per_round"])

    # ---------------- SEC 3  STAGE 1: THE 276 ---------------------------
    say("\n[SEC 3] STAGE 1 -- THE 276, UNIT-GRADE")
    del FLAT_QUADS[:]
    FLAT_QUADS.extend(flat_quadruples())
    n276 = pick("MUT-276", len(FLAT_QUADS), 275)
    n276b = flat_quadruples_route2()
    ms = Counter(tuple(sorted(q)) for q in FLAT_QUADS)
    if mut("MUT-STRUCTURE"):
        ms = Counter({k: v for k, v in ms.items()
                      if k != tuple(sorted(C["class_index"][k2]
                                           for k2 in COLLINEAR_FLAT))})
    committed276 = reg_probe["reaching_the_target_chart_orbit"]
    LD.gate("G-276",
            "THE PIN'S PRIMARY OBJECT, REBUILT UNIT-GRADE AND COUNTED TWICE.  "
            "Exhaustive over all %d ordered quadruples of saturating "
            "groupings -- which the budget theorem makes exhaustive over all "
            "%d ordered quadruples of partitions -- the summed link field is "
            "I7's own committed G-FLAT row at all 27 cells at exactly %d of "
            "them, in %d multisets.  Route 1 packs the field at four bits per "
            "cell and compares packed integers; route 2 sums 27-vectors and "
            "compares entry by entry against the vector I7's own row induces, "
            "sharing no code, no packing and no typed target with route 1.  "
            "Paper-19's own committed register row is %d"
            % (nsat ** ROUNDS, nparts_enum ** ROUNDS, n276, len(ms),
               committed276),
            n276 == n276b == committed276,
            "route 1 %d, route 2 %d, paper-19's committed row %d, multisets %d"
            % (n276, n276b, committed276, len(ms)))
    reg(n276, len(ms), committed276)
    ms_sizes = Counter(ms.values())
    collinear = tuple(sorted(C["class_index"][k] for k in COLLINEAR_FLAT))
    LD.gate("G-276-STRUCTURE",
            "THE 276 ARE NOT ONE ARRANGEMENT.  They fall into %d grouping "
            "multisets with orbit sizes %s, and EXACTLY ONE of the %d is the "
            "collinear arrangement -- the three link-direction parallel "
            "classes of AG(2,3) with the diagonal class taken twice.  The "
            "other %d each contain conflict groups that are not lines of "
            "AG(2,3), exactly as paper-19 measured at R = 3"
            % (len(ms), sorted(ms_sizes.items()), len(ms), len(ms) - 1),
            collinear in ms and len(ms) > 1
            and sum(ms.values()) == n276,
            "multisets %d, orbit-size spectrum %s, collinear multiset present "
            "%s, non-collinear %d" % (len(ms), sorted(ms_sizes.items()),
                                      collinear in ms, len(ms) - 1))
    reg(len(ms) - 1)
    R["census"] = {
        "flat_quadruples_route1": n276,
        "flat_quadruples_route2": n276b,
        "paper19_committed_register_row": committed276,
        "multisets": len(ms),
        "multiset_orbit_sizes": {str(k): v for k, v in sorted(ms_sizes.items())},
        "collinear_multiset_present": collinear in ms,
        "non_collinear_multisets": len(ms) - 1,
        "exhaustive_over": nparts_enum ** ROUNDS,
        "by": "the budget theorem: 4 x 9 = 36 = sum(G-FLAT) x |X|",
    }
    SEAL.take("SEAL-CENSUS", R)

    # ---------------- SEC 4  THE COMMITTED GRAMMAR, DRIVEN ---------------
    say("\n[SEC 4] THE COMMITTED GRAMMAR, DRIVEN DIRECTLY")
    G = Grammar(texts)
    LD.gate("G-SLICE-EXIT-FREE",
            "THE COMMITTED LAYERS ENTER AS SINGLE SOURCES AND CANNOT EXIT.  "
            "d42b1's transport layer is taken as a TEXT SLICE cut at the "
            "layer's own banner print, so its menu function `candidates_for` "
            "-- this unit's only source of admissibility -- is the committed "
            "one and nothing below the cut can run; d60's `B`/`dl` and d66's "
            "`conflict_grid` enter by AST extraction of their definitions, so "
            "no module-level statement of theirs can run either",
            G.slice_exit_free and G.bodies_exit_free,
            "slice exit-free %s, extracted bodies exit-free %s, slice ends at "
            "char %d of %d" % (G.slice_exit_free, G.bodies_exit_free,
                               G.slice_chars[0], G.slice_chars[1]))
    # THE ANCHOR: d66's own CONFLICT-GRID(3,4), re-run in this process, must
    # emit the committed row AND the same event list as the generalized driver
    # at the committed schedule.
    b66 = G.conflict_grid(3, ROUNDS)
    b_gen = drive(G, COMMITTED_R4)
    same_events = (list(b66.H) == list(b_gen.H))
    arbs66 = sum(1 for e in b66.H if e[0] == "r")
    dels66 = sum(1 for e in b66.H if e[0] == "d")
    committed_row = (len(b66.H), arbs66, dels66)
    LD.gate("G-DRIVER-ANCHOR",
            "THE GENERALIZED DRIVER IS ANCHORED AGAINST THE OBJECT IT "
            "GENERALIZES, AT THIS UNIT'S OWN BUDGET.  d66's committed "
            "`conflict_grid(3, 4)` is re-run in this process and the "
            "schedule-driven builder is run at d66's own R = 4 schedule -- "
            "rounds alternating ROW and COLUMN on the diagonal seed -- and "
            "the two emit IDENTICAL event lists.  The profile is then "
            "compared against d66's OWN COMMITTED OUTPUT ROW, read from its "
            "pinned bytes at run time: GRID(g=3,R=4) n = %d, arbs = %d, "
            "deliveries = %d" % grid34,
            same_events and committed_row == grid34
            and pick("MUT-DRIVER-ANCHOR", True, False),
            "identical event lists %s, driven row %s, d66's committed row %s"
            % (same_events, committed_row, grid34))
    reg(*grid34)
    # THE MEMO IS GATED, NOT TRUSTED
    probe_scheds = [COMMITTED_R4,
                    tuple((CLASSES[k], canon_transversals(CLASSES[k])[0])
                          for k in COLLINEAR_FLAT)]
    memo_rows = []
    for sch in probe_scheds:
        with_memo = record_of(G, drive(G, sch))
        without = record_of(G, drive(G, sch, memo_off=True))
        memo_rows.append(with_memo["kinds"] == without["kinds"]
                         and with_memo["footprints"] == without["footprints"]
                         and with_memo["events"] == without["events"])
    LD.gate("G-MENU-PURE",
            "THE MEMO IS GATED RATHER THAN TRUSTED.  d42b1's `candidates_for` "
            "is a pure function of (history, initiators) and this run caches "
            "it on exactly that pair; %d declared schedules are re-driven "
            "through a SECOND builder bound to the RAW layer function with no "
            "cache at all, and their records are compared event kind for "
            "event kind and footprint for footprint" % len(probe_scheds),
            all(memo_rows) and pick("MUT-MEMO", True, False),
            "schedules re-driven without the memo %d, records identical %s, "
            "memo calls %d hits %d" % (len(probe_scheds), all(memo_rows),
                                       G.memo_calls, G.memo_hits))

    say("\n[SEC 5] THE DECLARED DRIVEN WINDOW W4")
    W = window_drive(G)
    wtags = Counter(WINDOW_META[s] for s in W)
    wgroupings = {tuple(P for P, _s in s) for s in W}
    flat_groupings = {tuple(C["parts"][i] for i in q) for q in FLAT_QUADS}
    LD.gate("G-WINDOW-DISCLOSED",
            "THE DRIVEN WINDOW IS DECLARED, DISCLOSED IN THE HEAD, AND "
            "CONTAINS THE PIN'S PRIMARY OBJECT ENTIRE.  W4 is %d schedules of "
            "the %d the R = 4 family carries: %s.  Its grouping quadruples "
            "number %d of the %d, and ALL %d G-FLAT-inducing quadruples are "
            "inside it -- the primary object is exhausted, not sampled.  "
            "Every other column below is exhaustive over an object the window "
            "does not cap"
            % (len(W), R["family"]["schedules"], dict(sorted(wtags.items())),
               len(wgroupings), nparts_enum ** ROUNDS, n276),
            flat_groupings <= wgroupings and len(W) == len(set(W))
            and pick("MUT-WINDOW", True, False),
            "window %d, groupings %d, all %d flat quadruples inside %s"
            % (len(W), len(wgroupings), n276, flat_groupings <= wgroupings))
    reg(len(W), len(wgroupings))
    R["family"]["window"] = len(W)
    R["family"]["window_strata"] = {k: v for k, v in sorted(wtags.items())}
    R["family"]["window_groupings"] = len(wgroupings)
    R["family"]["seed_menu"] = ("the first %d canonical transversals of each "
                                "round, plus the declared seed fan: the "
                                "collinear arrangement at all %d canonical "
                                "transversal quadruples"
                                % (SEEDS_PER_ROUND_IN_WINDOW,
                                   3 ** ROUNDS))
    SEAL.take("SEAL-FAMILY", R)

    # THE EQUALITY THAT LICENSES THE EXHAUSTIVE COLUMNS
    mism = 0
    for sch, rec in W.items():
        driven_f = link_field_of(rec["footprints"])
        comb = unpack_field(packed_of_schedule(sch))
        if any(driven_f[c] != comb[c] for c in CELLS):
            mism += 1
    mism = pick("MUT-EQUALITY", mism, 1)
    LD.gate("G-DRIVEN-EQUALS-COMBINATORIAL",
            "THE LICENSE FOR EVERY EXHAUSTIVE COLUMN, RE-MEASURED AT THIS "
            "BUDGET.  For every one of the %d driven window records the link "
            "field read off the DRIVEN record -- the footprints taken from "
            "the layer's own `regs_of` -- equals, cell by cell, the field the "
            "combinatorial route computes from the schedule's groupings "
            "alone.  Nothing downstream quantifies over a combinatorial "
            "object without this equality" % len(W),
            mism == 0,
            "records compared %d, mismatches %d" % (len(W), mism))
    fates = Counter()
    for sch, rec in W.items():
        if rec["refusal"]:
            fates["REFUSED"] += 1
        elif rec["maxhits"] > 1:
            fates["BRANCHING"] += 1
        else:
            fates["FORCED"] += 1
    nforced = pick("MUT-FORCED", fates["FORCED"], fates["FORCED"] - 1)
    LD.gate("G-FORCED",
            "FORCEDNESS, PER OBJECT.  Every event of every window schedule is "
            "specified by its FULL TUPLE, so at most one menu candidate can "
            "match and the builder's tie-break is never consulted; the "
            "builder's own `maxhits` is read at every schedule and required "
            "to be 1 there.  Measured: FORCED at %d of %d, BRANCHING %d, "
            "REFUSED %d" % (nforced, len(W), fates["BRANCHING"],
                            fates["REFUSED"]),
            nforced == len(W) and not fates["BRANCHING"]
            and not fates["REFUSED"],
            "FORCED %d of %d; branching %d; refused %d"
            % (nforced, len(W), fates["BRANCHING"], fates["REFUSED"]))
    reg(nforced)
    lengths = Counter(rec["events"] for rec in W.values())
    divs = Counter(rec["divisions"] for rec in W.values())
    if mut("MUT-SHAPE"):
        divs = Counter({ROUNDS * 3 + 1: 1})
    LD.gate("G-RECORD-SHAPE",
            "EVERY WINDOW RECORD CARRIES EXACTLY %d DIVISION EVENTS -- one "
            "arbitration per conflict group per round -- and record length is "
            "a clean spectrum %s, the conflict supply being the only variable: "
            "a round needs no supply for a group whose members already share a "
            "base" % (ROUNDS * 3, sorted(lengths.items())),
            set(divs) == {ROUNDS * 3},
            "division-event counts %s, length spectrum %s"
            % (sorted(divs.items()), sorted(lengths.items())))
    # THE TWO NEGATIVE FATES, REACHED
    coll = tuple((CLASSES[k], canon_transversals(CLASSES[k])[0])
                 for k in COLLINEAR_FLAT)
    b_ref = drive(G, coll, drop_supply=0)
    LD.gate("G-CTRL-REFUSED",
            "THE REFUSAL FATE IS REACHABLE AND THE INSTRUMENT SEES IT.  The "
            "collinear arrangement is re-driven with its FIRST "
            "conflict-supply delivery withheld; the committed layer then "
            "refuses the first proposal by an actor that does not hold the "
            "base, and the refusal is RECORDED, never patched",
            pick("MUT-REFUSED", b_ref.refusal, None) is not None,
            "refusal %s" % (b_ref.refusal,))
    br_hits, br_prefix, br_seed = branching_control(G, coll)
    LD.gate("G-CTRL-BRANCHING",
            "THE BRANCHING FATE IS REACHABLE, AND THE CONTROL IS "
            "REPRODUCIBLE.  The collinear record is replayed to its first "
            "arbitration, ONE under-specified pick is made -- the initiator "
            "named and the conflict and winner keys withheld -- and the "
            "builder's own `maxhits` rises above 1.  Only the COUNT is "
            "reported and the control STOPS THERE: d60's `pick` breaks ties "
            "with sorted(key=repr) and a frozenset's repr depends on the "
            "interpreter's per-process string hashing, so WHICH candidate an "
            "under-specified pick selects is not reproducible across runs -- "
            "a control that continued past one such pick would carry that "
            "irreproducibility into the delivered bytes",
            pick("MUT-BRANCH", br_hits, 1) > 1,
            "maxhits under-specified %d at prefix %d on initiator %s, maxhits "
            "fully specified %d"
            % (br_hits, br_prefix, br_seed,
               max(r["maxhits"] for r in W.values())))
    R["driven"] = {
        "window_records": len(W),
        "fates": {k: v for k, v in sorted(fates.items())},
        "forced": nforced,
        "record_lengths": {str(k): v for k, v in sorted(lengths.items())},
        "divisions_per_record": ROUNDS * 3,
        "driven_equals_combinatorial_mismatches": mism,
        "d66_committed_row": list(grid34),
        "driver_anchor_identical_event_lists": same_events,
        "refusal_control": str(b_ref.refusal),
        "branching_control_maxhits": br_hits,
        "branching_control_prefix": br_prefix,
        "branching_control_initiator": br_seed,
        "menu_memo_gated": True,
    }
    SEAL.take("SEAL-DRIVEN", R)

    # ---------------- SEC 6  THE ARENA, UNIT-GRADE ----------------------
    say("\n[SEC 6] STAGE 1 -- THE INDUCED RECORD, DRIVEN")
    coll_rec = W[coll]
    fld = link_field_of(coll_rec["footprints"])
    per_site = {x: tuple(fld[(x, l)] for l in I7_LINKS) for x in SITES}
    cells_at_target = sum(1 for c in CELLS
                          if fld[c] == FLAT[I7_LINKS.index(c[1])])
    dets = {x: q_of(per_site[x])[3] for x in SITES}
    nposdef = sum(1 for x in SITES if admissible(per_site[x]))
    exact = pick("MUT-UNIT-GRADE",
                 all(per_site[x] == FLAT for x in SITES), False)
    LD.gate("G-UNIT-GRADE",
            "THE PIN'S STAGE-1 DEMAND, DRIVEN AND CHECKED PER OBJECT.  The "
            "collinear arrangement -- ROW, COL, DIA, DIA, every event taken "
            "from the committed layer's own menu -- runs to %d events with %d "
            "division events, and its DRIVEN link field is I7's own committed "
            "G-FLAT row %s at every one of the nine sites: %d of %d cells at "
            "target, det = %s at %d of %d sites, positive definite at %d of "
            "%d.  Every site is checked against its own value, never against "
            "an aggregate"
            % (coll_rec["events"], coll_rec["divisions"], str(FLAT),
               cells_at_target, len(CELLS), q_of(FLAT)[3],
               sum(1 for x in SITES if dets[x] == q_of(FLAT)[3]), len(SITES),
               nposdef, len(SITES)),
            exact and cells_at_target == len(CELLS) and nposdef == len(SITES),
            "sites at G-FLAT %d of %d, cells at target %d of %d, det %s "
            "everywhere %s, posdef %d of %d"
            % (sum(1 for x in SITES if per_site[x] == FLAT), len(SITES),
               cells_at_target, len(CELLS), q_of(FLAT)[3],
               all(dets[x] == q_of(FLAT)[3] for x in SITES), nposdef,
               len(SITES)))
    reg(coll_rec["events"], coll_rec["divisions"], cells_at_target, nposdef,
        q_of(FLAT)[3])
    orb = chart_orbit(FLAT)
    hits = sorted(nm for nm, v in i7["family"].items() if tuple(v) in orb)
    LD.gate("G-DECLARED-RECORD",
            "THE INDUCED RECORD IS ONE OF I7's ELEVEN DECLARED RECORDS -- "
            "compared PER RECORD against the induced vector's whole chart "
            "orbit under I7's own declared chart group, never by name.  It is "
            "G-FLAT, and paper-19's landing record (1,1,1) is not in the "
            "declared list at all: the undeclaredness one round down was a "
            "budget fact and it dissolves here",
            hits == ["G-FLAT"] and pick("MUT-DECLARED", True, False),
            "chart orbit %s, declared records hit %s, declared family size %d"
            % (sorted(orb), hits, R["i7"]["declared_family_size"]))
    # THE SEED AXIS, EXHAUSTED AT ONE GROUPING
    fan = [s for s in W if WINDOW_META[s] == "W4-SEEDFAN"
           or tuple(P for P, _ss in s) == tuple(CLASSES[k]
                                                for k in COLLINEAR_FLAT)]
    fan_fields = {tuple(sorted((str(k), v) for k, v in
                               link_field_of(W[s]["footprints"]).items()))
                  for s in fan}
    LD.gate("G-SEED-INVARIANCE",
            "THE GEOMETRY IS A FUNCTION OF THE GROUPINGS ALONE, DRIVEN.  The "
            "declared seed fan drives the collinear arrangement at all %d "
            "canonical transversal quadruples of its four rounds, and all %d "
            "records carry ONE AND THE SAME driven link field.  At this "
            "generator a division event's footprint IS its conflict group, so "
            "this confirms the mechanism rather than discovering it"
            % (3 ** ROUNDS, len(fan)),
            pick("MUT-SEED", len(fan_fields), 2) == 1
            and len(fan) == 3 ** ROUNDS,
            "seedings driven %d, distinct driven fields %d"
            % (len(fan), len(fan_fields)))
    reg(len(fan))
    # the driven homogeneous table over the resolvable device
    homo_tbl = {}
    for sch in W:
        T = tuple(P for P, _s in sch)
        if not all(P in CLASS_OF for P in T):
            continue
        f = link_field_of(W[sch]["footprints"])
        codes = {tuple(f[(x, l)] for l in I7_LINKS) for x in SITES}
        key = tuple(sorted(CLASS_OF[P] for P in T))
        assert len(codes) == 1
        homo_tbl[key] = list(list(codes)[0])
    adm_homo = sorted(k for k, v in homo_tbl.items() if admissible(tuple(v)))
    dec_homo = sorted(k for k, v in homo_tbl.items()
                      if any(tuple(v) in chart_orbit(tuple(w))
                             for w in i7["family"].values()))
    if mut("MUT-TABLE"):
        dec_homo = []
    LD.gate("G-RESOLVABLE-TABLE",
            "THE COMMITTED RESOLVABLE DEVICE REACHES THE DECLARED RECORD.  "
            "All %d ordered quadruples of the four parallel classes of "
            "AG(2,3) are driven; every one induces a HOMOGENEOUS field, the "
            "%d distinct multisets giving %d distinct records of which %d are "
            "admissible and %d lie in the chart orbit of a declared I7 "
            "record.  d66's own device, extended two rounds and grouped on "
            "the three link directions with the diagonal twice, is one of them"
            % (len(CLASS_NAMES) ** ROUNDS, len(homo_tbl),
               len({tuple(v) for v in homo_tbl.values()}), len(adm_homo),
               len(dec_homo)),
            len(homo_tbl) == len(list(combinations(
                range(len(CLASS_NAMES) + ROUNDS - 1), ROUNDS)))
            and dec_homo, "multisets %d, admissible %d, declared-orbit %s"
            % (len(homo_tbl), len(adm_homo), dec_homo))
    R["arena"] = {
        "collinear_arrangement": list(COLLINEAR_FLAT),
        "events": coll_rec["events"], "divisions": coll_rec["divisions"],
        "driven_record": [list(per_site[x]) for x in SITES],
        "induced_record": list(FLAT),
        "cells_at_target": cells_at_target,
        "det": str(q_of(FLAT)[3]),
        "posdef_sites": nposdef,
        "declared_records_hit": hits,
        "chart_orbit": sorted(str(o) for o in orb),
        "seed_fan_size": len(fan),
        "seed_fan_distinct_fields": len(fan_fields),
        "resolvable_table": {"|".join(k): v for k, v in sorted(homo_tbl.items())},
        "resolvable_multisets": len(homo_tbl),
        "resolvable_records": len({tuple(v) for v in homo_tbl.values()}),
        "resolvable_admissible": len(adm_homo),
        "resolvable_declared_orbit": ["|".join(k) for k in dec_homo],
    }
    SEAL.take("SEAL-ARENA", R)

    # ---------------- SEC 7  STAGE 2: THE DECLARED-RECORD WELD -----------
    say("\n[SEC 7] STAGE 2 -- THE DECLARED-RECORD WELD")
    TARGET = {"name": "I7", "X": [tuple(x) for x in SITES],
              "links": [tuple(l) for l in i7["links"]], "Lmod": i7["L"]}

    def arena_of(name, rec, actors=None):
        pool = list(ACTORS) if actors is None else list(actors)
        return {"name": name, "actors": pool,
                "rel": codivision_rel(pool, rec["footprints"])}

    flat_scheds = [s for s in W
                   if tuple(P for P, _ss in s) in flat_groupings]
    sigs = {tuple(sorted((str(k), v) for k, v in
                         arena_of("x", W[s])["rel"].items()))
            for s in flat_scheds}
    LD.gate("G-FLAT-ARENA-IDENTITY",
            "ONE ARENA, MEASURED RATHER THAN ASSUMED.  All %d driven G-FLAT "
            "schedules are turned into co-division arenas and every one of "
            "them carries the IDENTICAL relation: the same nine site objects, "
            "the same realised pairs and the same count on every one.  The "
            "census below therefore has one arena and not %d, and that is a "
            "measurement" % (len(flat_scheds), len(flat_scheds)),
            pick("MUT-ARENA-ID", len(sigs), 2) == 1
            and len(flat_scheds) >= n276,
            "driven G-FLAT schedules %d, distinct arena signatures %d"
            % (len(flat_scheds), len(sigs)))
    reg(len(flat_scheds))
    A_FLAT = arena_of("R4-FLAT", W[coll])
    r3_sched = tuple((CLASSES[k], canon_transversals(CLASSES[k])[0])
                     for k in ("ROW", "COL", "DIA"))
    A_R3 = arena_of("R3-SAT(the same constructor, one round shorter)",
                    driven(G, r3_sched))
    one_sched = tuple((CLASSES[k], canon_transversals(CLASSES[k])[0])
                      for k in ("ROW", "COL", "DIA", "ANT"))
    A_ONE = arena_of("R4-ONE-ANT(field identically 1)", W[one_sched])
    # THE ARITHMETIC THAT DECIDES THE STANDARD, MEASURED ON BOTH BUDGETS
    foreign = sum(1 for (u, v), n in A_ONE["rel"].items()
                  if n > 0 and (zadd(ACTOR_SITE[v],
                                     tuple((-c) % 3 for c in ACTOR_SITE[u]))
                                not in set(I7_LINKS)
                                and zadd(ACTOR_SITE[u],
                                         tuple((-c) % 3
                                               for c in ACTOR_SITE[v]))
                                not in set(I7_LINKS))) // 2
    inc4 = maxinc * ROUNDS
    inc3 = maxinc * (ROUNDS - 1)
    LD.gate("G-CONSTANCY-IMPOSSIBLE",
            "THE ARITHMETIC THAT DECIDES THE RSQ STANDARD AT THIS BUDGET, AND "
            "IT IS A THEOREM.  A round's realised co-division pairs are its "
            "conflict groups' own pairs, so a round whose relation stays "
            "inside the target's incidence is exactly a SATURATING one -- the "
            "field-identically-1 quadruple ROW/COL/DIA/ANT deposits %d "
            "incidences on I7's links and %d FOREIGN pairs, and is "
            "STRUCT-DEAD for that reason.  A clean R = 4 arena therefore "
            "spreads %d incidences over %d cells, and %d is not a multiple of "
            "%d: a LINK-CONSTANT field is arithmetically impossible at R = 4, "
            "while at R = 3 the %d incidences over %d cells force one.  Zero "
            "free items and R = 4 cannot be had together at this carrier, "
            "whatever the record"
            % (inc3, foreign, inc4, len(CELLS), inc4, len(CELLS), inc3,
               len(CELLS)),
            pick("MUT-CONSTANCY", inc4 % len(CELLS), 0) != 0
            and inc3 % len(CELLS) == 0 and foreign > 0,
            "R=4 incidences %d over %d cells, remainder %d; R=3 %d over %d, "
            "remainder %d; foreign pairs in the ANT quadruple %d"
            % (inc4, len(CELLS), inc4 % len(CELLS), inc3, len(CELLS),
               inc3 % len(CELLS), foreign))
    reg(foreign, inc3, inc4)
    A_GRID = arena_of("R4-COMMITTED-GRID(3,4)", driven(G, COMMITTED_R4))
    fals = {"footprints": list(W[coll]["footprints"])[1:]}
    A_FALS = arena_of("R4-FLAT-FALSIFIER(one division withheld)", fals)
    A_ARITY = arena_of("R4-FLAT-RESTRICTED-TO-8(declared probe)", W[coll],
                       actors=ACTORS[:8])
    DECLARED_ROWS = [
        (A_FLAT, "EMBEDDING", "UNMOTIVATED"),
        (A_FLAT, "QUOTIENT", "UNMOTIVATED"),
        (A_R3, "EMBEDDING", "FOUND-candidate"),
        (A_R3, "QUOTIENT", "FOUND-candidate"),
        (A_ONE, "EMBEDDING", "STRUCT-DEAD"),
        (A_ONE, "QUOTIENT", "STRUCT-DEAD"),
        (A_GRID, "EMBEDDING", "STRUCT-DEAD"),
        (A_GRID, "QUOTIENT", "COUNT-DEAD"),
        (A_FALS, "EMBEDDING", "STRUCT-DEAD"),
        (A_FALS, "QUOTIENT", "COUNT-DEAD"),
        (A_ARITY, "EMBEDDING", "ARITY-DEAD"),
        (A_ARITY, "QUOTIENT", "ARITY-DEAD"),
    ]
    rows, drift = [], []
    for arena, reading, declared in DECLARED_ROWS:
        row = detect(arena, TARGET, reading)
        row["declared_fate"] = declared
        got = pick("MUT-WELD-FATE", row["fate"], "FOUND-candidate")
        row["fate"] = got
        row["matches_declaration"] = (got == declared)
        if not row["matches_declaration"]:
            drift.append((arena["name"], reading, declared, got))
        rows.append(row)
        say("    %-46s @%-9s -> %s" % (arena["name"], reading, row["fate"]))
    LD.gate("G-WELD-CENSUS",
            "EVERY CENSUS ROW'S FATE IS COMPARED AGAINST THE FATE DECLARED "
            "FOR ITS OWN CELL BEFORE THE RUN, per object and never in "
            "aggregate.  %d rows: the R = 4 G-FLAT arena at both readings, "
            "the R = 4 field-identically-1 arena at both, d66's own committed "
            "R = 4 point at both, this unit's declared falsifier at both, and "
            "a declared arity probe at both" % len(rows),
            not drift, "rows %d, drift %s" % (len(rows), drift or "none"))
    flat_rows = [r for r in rows if r["arena"] == "R4-FLAT"]
    one_rows = [r for r in rows if r["arena"].startswith("R3-SAT")]
    fib = dict(flat_rows[0]["inventory"])
    fib1 = dict(one_rows[0]["inventory"])
    if mut("MUT-FIBER"):
        fib["I-SITE-ASSIGNMENT"] = 1
    LD.gate("G-WELD-FIBERS",
            "THE CHOICE INVENTORY, WITH EVERY FIBER COMPUTED AS THE NUMBER OF "
            "DISTINCT COUNT FIELDS ITS CHOICE PRODUCES -- weld 2's own "
            "standard, carried unchanged.  At the R = 4 G-FLAT arena: "
            "I-SITE-ASSIGNMENT %d, I-DIRECTION-LABEL %d, I-ORIENT %d, read at "
            "%d base maps.  AND THE LABEL AND ORIENT FIBERS ARE NOT BASE-MAP "
            "INVARIANT HERE: re-read at every one of those base maps they "
            "take the values %s and %s, against the single value each takes "
            "at the DRIVEN R = 3 saturating arena, where the same three "
            "fibers are %d / %d / %d and invariance holds.  What IS invariant "
            "is the verdict: at EVERY base map the R = 4 arena carries at "
            "least %d free item, because the site-assignment fiber is a "
            "property of the field rather than of the base map.  The "
            "structural test passes at both -- %d isomorphisms and %d "
            "quotient maps, the target's own automorphism number"
            % (fib["I-SITE-ASSIGNMENT"], fib["I-DIRECTION-LABEL"],
               fib["I-ORIENT"], flat_rows[0]["base_maps_read"],
               flat_rows[0]["label_fiber_spread"],
               flat_rows[0]["orient_fiber_spread"],
               fib1["I-SITE-ASSIGNMENT"], fib1["I-DIRECTION-LABEL"],
               fib1["I-ORIENT"], flat_rows[0]["free_items_at_every_base_map"],
               flat_rows[0]["isomorphisms"], flat_rows[1]["quotient_maps"]),
            one_rows[0]["fibers_base_map_invariant"]
            and not flat_rows[0]["fibers_base_map_invariant"]
            and flat_rows[0]["free_items_at_every_base_map"] >= 1
            and flat_rows[0]["isomorphisms"] == flat_rows[1]["quotient_maps"]
            and fib["I-SITE-ASSIGNMENT"]
            == flat_rows[0]["assignment_fiber_records"],
            "G-FLAT fibers %s (label spread %s, orient spread %s, free items "
            "at every base map >= %d); R=3 fibers %s, invariant %s; isos %d, "
            "quotient maps %d"
            % (fib, flat_rows[0]["label_fiber_spread"],
               flat_rows[0]["orient_fiber_spread"],
               flat_rows[0]["free_items_at_every_base_map"], fib1,
               one_rows[0]["fibers_base_map_invariant"],
               flat_rows[0]["isomorphisms"], flat_rows[1]["quotient_maps"]))
    reg(fib["I-SITE-ASSIGNMENT"], fib["I-DIRECTION-LABEL"], fib["I-ORIENT"],
        flat_rows[0]["isomorphisms"], flat_rows[1]["quotient_maps"])
    # THE STANDARD-VS-LIST THEOREM
    linkconst = R["i7"]["link_constant_declared_records"]
    boxconst = R["i7"]["link_constant_admissible_box_points"]
    fiber1_records = []
    for nm, v in sorted(i7["family"].items()):
        fiber1_records.append((nm, len(set(v)) == 1))
    LD.gate("G-RSQ-THEOREM",
            "WHY THE STANDARD AND THE LIST CANNOT BOTH BE HAD AT THIS "
            "CARRIER, AND IT IS A THEOREM WITH A MEASUREMENT ON EACH SIDE.  "
            "The realised relation is edge-transitive, so a count field "
            "invariant under all %d of its automorphisms is constant on all "
            "%d edges -- I-SITE-ASSIGNMENT has fiber 1 exactly at the "
            "LINK-CONSTANT records (n,n,n), and so does I-DIRECTION-LABEL.  "
            "Measured on I7's own declared family: %d of its %d homogeneous "
            "declared records are link-constant, while the declared count box "
            "contains %d link-constant admissible points.  So zero free items "
            "and a declared record are incompatible here, and paper-19's "
            "zero-free-items reading was carried by its record being "
            "identically 1 rather than by its map"
            % (flat_rows[0]["isomorphisms"], len(CELLS), len(linkconst),
               len(i7["family"]), len(boxconst)),
            not linkconst and boxconst
            and fib1["I-SITE-ASSIGNMENT"] == 1
            and fib["I-SITE-ASSIGNMENT"] > 1
            and pick("MUT-RSQ", True, False),
            "link-constant declared records %s of %d; link-constant "
            "admissible box points %d; fiber at (1,1,1) %d; fiber at G-FLAT %d"
            % (linkconst or "none", len(i7["family"]), len(boxconst),
               fib1["I-SITE-ASSIGNMENT"], fib["I-SITE-ASSIGNMENT"]))
    reg(len(boxconst))
    # THE STRICTEST READING: the site carrier fixed to the constructor's parse
    strict_rec = pick("MUT-STRICT", sorted({per_site[x] for x in SITES}),
                      [(9, 9, 9)])
    fiber_hom = [tuple(h) for h in flat_rows[0]["assignment_fiber_homogeneous"]]
    fiber_declared = sorted(nm for nm, v in i7["family"].items()
                            if any(h in chart_orbit(tuple(v))
                                   for h in fiber_hom))
    LD.gate("G-STRICTEST-READING",
            "AND THE DECLARED RECORD DOES NOT NEED THE SITE ASSIGNMENT TO BE "
            "FREE AT ALL.  Under the strictest reading available -- the site "
            "carrier fixed to the constructor's own actor-to-Z_3^2 parse, "
            "which paper-19 calls forced and which this unit inherits -- the "
            "driven record induces EXACTLY I7's committed G-FLAT row at every "
            "one of the nine sites, with the direction labels taken in I7's "
            "own declared order.  Of the %d count fields the free assignment "
            "produces, %d are homogeneous and EXACTLY %d is a declared record"
            % (flat_rows[0]["assignment_fiber_records"],
               len(fiber_hom), len(fiber_declared)),
            strict_rec == [FLAT] and fiber_declared == ["G-FLAT"]
            and flat_rows[0]["assignment_fiber_all_admissible"],
            "record at the forced carrier %s, fiber records %d, homogeneous "
            "%s, every field in the fiber admissible %s"
            % (strict_rec, flat_rows[0]["assignment_fiber_records"],
               flat_rows[0]["assignment_fiber_homogeneous"],
               flat_rows[0]["assignment_fiber_all_admissible"]))
    fatevals = {r["fate"] for r in rows}
    if mut("MUT-TWOWAY"):
        fatevals = fatevals - {"ARITY-DEAD"}
    LD.gate("G-TWO-WAY",
            "HA REQUIREMENT 3, DISCHARGED IN THIS RUN AND NOT BY CITATION: "
            "a predicate that cannot return its other value anywhere in the "
            "declared arena is not a measurement.  Every value this detector "
            "can return is exhibited here -- %s -- and the FOUND value is "
            "exhibited on a DRIVEN R = 4 grammar record rather than on a "
            "probe" % sorted(fatevals),
            fatevals == {"FOUND-candidate", "UNMOTIVATED", "COUNT-DEAD",
                         "STRUCT-DEAD", "ARITY-DEAD"}
            and match_needle(ha, VERBATIM[10][2]),
            "fates exhibited %s" % sorted(fatevals))
    dircomp = sorted({r.get("isomorphisms_directed_comparator")
                      for r in rows
                      if r.get("isomorphisms_directed_comparator") is not None})
    R["weld"] = {
        "rows": rows,
        "target": "I7",
        "flat_arena_schedules": len(flat_scheds),
        "flat_arena_signatures": len(sigs),
        "fibers_at_g_flat": fib,
        "fibers_at_the_driven_r3_record": fib1,
        "label_fiber_spread": flat_rows[0]["label_fiber_spread"],
        "orient_fiber_spread": flat_rows[0]["orient_fiber_spread"],
        "free_items_at_every_base_map":
            flat_rows[0]["free_items_at_every_base_map"],
        "r3_fibers_base_map_invariant":
            one_rows[0]["fibers_base_map_invariant"],
        "foreign_pairs_in_the_ant_quadruple": foreign,
        "incidences_r4": inc4, "incidences_r3": inc3,
        "isomorphisms": flat_rows[0]["isomorphisms"],
        "quotient_maps": flat_rows[1]["quotient_maps"],
        "directed_comparator_values": dircomp,
        "record_at_the_forced_carrier": [list(v) for v in strict_rec],
        "assignment_fiber_records": flat_rows[0]["assignment_fiber_records"],
        "assignment_fiber_homogeneous":
            flat_rows[0]["assignment_fiber_homogeneous"],
        "assignment_fiber_declared_records": fiber_declared,
        "assignment_fiber_inhomogeneous":
            flat_rows[0]["assignment_fiber_records"] - len(fiber_hom),
        "link_constant_declared_records": linkconst,
        "link_constant_admissible_box_points": boxconst,
        "fates_exhibited": sorted(fatevals),
    }
    SEAL.take("SEAL-WELD", R)

    # ---------------- SEC 8  STAGE 3: THE SPLITTABLE QUESTION -----------
    say("\n[SEC 8] STAGE 3 -- THE SPLITTABLE QUESTION")
    p04 = json.loads(source_text(texts, "A-P04REC"))
    p06 = json.loads(source_text(texts, "A-P06REC"))
    p09 = json.loads(source_text(texts, "A-P09REC"))
    # THE PER-INTERVAL SPLIT FIBER, on THIS unit's welded record
    per_int = {c: fld[c] - 1 for c in CELLS}
    pos_int = sorted(c for c in CELLS if per_int[c] > 0)
    raw_fiber = 1
    for c in CELLS:
        raw_fiber *= per_int[c]
    prev_pos = 0        # paper-19's landing record (1,1,1): every interval 1
    LD.gate("G-SPLIT-FIBER",
            "THE SPLIT FIBER, INTERVAL BY INTERVAL, ON THE WELDED RECORD.  "
            "R6a's identity is that an interval carrying only its total n "
            "admits exactly n - 1 places for one interior boundary, and that "
            "a count-1 interval cannot be split into two strictly positive "
            "parts.  The R = 4 welded record (%s) carries split fiber %d at "
            "each of %d of its %d intervals -- the diagonal ones -- and 0 at "
            "the other %d, against %d of %d at paper-19's landing record.  "
            "The RAW fiber, R6a's product over all %d slots, is still %d"
            % (str(FLAT), max(per_int.values()), len(pos_int), len(CELLS),
               len(CELLS) - len(pos_int), prev_pos, len(CELLS), len(CELLS),
               raw_fiber),
            len(pos_int) == pick("MUT-SPLIT", 9, 0)
            and raw_fiber == 0 and max(per_int.values()) == 1,
            "intervals with positive split fiber %d of %d, values %s, raw "
            "product %d" % (len(pos_int), len(CELLS),
                            sorted(Counter(per_int.values()).items()),
                            raw_fiber))
    reg(len(pos_int), len(CELLS) - len(pos_int), raw_fiber)
    # LAW 04: the refinement grammar
    p04flat = dict(p04["split_fibers"]["G-FLAT"])
    if mut("MUT-LAW04"):
        p04flat["raw"] = 1
    p04unsplit = p04["forced_part"]["unsplittable_records"]
    LD.gate("G-LAW-04",
            "PAPER-04's REFINEMENT GRAMMAR IS STILL EMPTY ON THE WELDED "
            "RECORD, AND THE MOVE THAT WOULD USE THE NEW SLOTS IS ITS OWN "
            "REFUSED CLASS.  R6a's admissible class is the DYADIC move, which "
            "subdivides every one of the 27 coarse intervals at once, so it "
            "needs the raw fiber -- the product -- and G-FLAT is one of the "
            "three records R6a's own receipt marks unrefinable (%s), with raw "
            "fiber %s.  The per-interval move that the %d positive slots "
            "would feed is R6a's SINGLE-INTERVAL class, REFUSED on arena "
            "shape: inserting one site into one link breaks the equal "
            "direction-0 cycle lengths a product-of-cyclic-groups site set "
            "forces"
            % (p04unsplit, p04flat["raw"], len(pos_int)),
            p04flat["raw"] == raw_fiber and "G-FLAT" in p04unsplit
            and match_needle(source_text(texts, "A-P04"), VERBATIM[14][2]),
            "R6a's committed raw fiber for G-FLAT %s, recomputed %d, "
            "unrefinable records %s"
            % (p04flat["raw"], raw_fiber, p04unsplit))
    # LAW 06: the stochastic split
    rows06 = {r["n"]: r for r in p06["per_interval_law"]["rows"]}
    n2 = dict(rows06[2])
    n1 = dict(rows06[1])
    if mut("MUT-LAW06"):
        n2["pinned_transitive"] = False
    LD.gate("G-LAW-06",
            "PAPER-06's PER-INTERVAL LAW BECOMES NON-EMPTY, AND IT IS UNIQUE "
            "WHERE IT DOES.  CR-B's own committed rows give, at count 1, "
            "fiber %d and no orbit at all; at count 2, fiber %d, %d orbit, "
            "simplex dim %s -- its law dim = n - 2 -- and the pinned "
            "chart symmetry TRANSITIVE.  The welded record carries %d "
            "count-2 intervals, so at %d of its %d intervals a unique "
            "invariant split law exists, against %d of %d on paper-19's "
            "landing record.  At the RECORD level CR-B still marks G-FLAT "
            "unsplittable, because its lattice predicate asks every interval "
            "to split"
            % (n1["fiber"], n2["fiber"], n2["pinned_orbits"],
               n2["pinned_simplex_dim"], len(pos_int), len(pos_int),
               len(CELLS), prev_pos, len(CELLS)),
            n2["pinned_transitive"] and n2["pinned_simplex_dim"] == 0
            and n2["fiber"] == 1 and n1["fiber"] == 0
            and p06["record_family"]["G-FLAT"]["splittable"] is False,
            "count-1 row %s; count-2 row %s; CR-B record-level splittable %s"
            % ({k: n1[k] for k in ("fiber", "pinned_orbits",
                                   "pinned_simplex_dim")},
               {k: n2[k] for k in ("fiber", "pinned_orbits",
                                   "pinned_simplex_dim",
                                   "pinned_transitive")},
               p06["record_family"]["G-FLAT"]["splittable"]))
    # LAW 09: the renewal kernel
    classes09 = p09["fiber_collapse"]["interval_classes"]
    holekey = [k for k in classes09 if k.startswith("KERNEL-HOLE")][0]
    holecounts = {1, 2}
    in_hole = sum(1 for c in CELLS if fld[c] in holecounts)
    LD.gate("G-KERNEL-HOLE",
            "PAPER-09's DERIVED KERNEL IS EMPTY ON THE WELDED RECORD, AND AT "
            "A DIFFERENT MECHANISM FROM PAPER-04's.  R6b''s first-return law "
            "has g(1) = g(2) = 0 EXACTLY -- there is no inter-renewal leg of "
            "length one or two -- and its own committed interval-class table "
            "puts %d of its %d censused intervals in that hole.  Every count "
            "the welded record carries is 1 or 2, so ALL %d of its intervals "
            "fall inside the hole: the kernel assigns them probability zero.  "
            "R6b' also lists G-FLAT among the three records it excludes for "
            "having R6a split fiber zero, so the emptiness is double"
            % (classes09[holekey], p09["fiber_collapse"]["intervals_total"],
               in_hole),
            in_hole == len(CELLS)
            and "G-FLAT" in p09["arena"]["unrefinable_records"]
            and pick("MUT-HOLE", True, False),
            "welded-record intervals inside the kernel hole %d of %d; R6b's "
            "hole %d of %d; G-FLAT in its unrefinable list %s"
            % (in_hole, len(CELLS), classes09[holekey],
               p09["fiber_collapse"]["intervals_total"],
               "G-FLAT" in p09["arena"]["unrefinable_records"]))
    LD.gate("G-LAW-09",
            "AND THE HONEST DENOMINATOR IS R6b''s OWN.  Its committed row "
            "excludes G-ANISO, G-CURVED and G-FLAT as carrying %d of its "
            "censused intervals with nothing to collapse; the collapse class "
            "it does speak on is count >= 4, at %d intervals.  The welded "
            "record's maximum count is %d"
            % (p09["arena"]["unrefinable_intervals"],
               classes09[[k for k in classes09
                          if k.startswith("COLLAPSED")][0]],
               max(fld.values())),
            pick("MUT-LAW09", max(fld.values()), 4) < 4
            and match_needle(source_text(texts, "A-P09"), VERBATIM[17][2]),
            "unrefinable intervals excluded by R6b' %d; collapse class %d; "
            "welded maximum count %d"
            % (p09["arena"]["unrefinable_intervals"],
               classes09[[k for k in classes09
                          if k.startswith("COLLAPSED")][0]],
               max(fld.values())))
    nonempty = pick("MUT-LAWS", ["paper-06 per-interval invariant law"],
                    ["a", "b"])
    LD.gate("G-LAWS-OVER-RECORDS",
            "THE PIN'S THIRD QUESTION, ANSWERED WITH ITS MECHANISM.  The R = 4 "
            "welded record IS splittable -- at %d of its %d intervals, split "
            "fiber %d each -- and it is the first welded record with a "
            "positive split fiber anywhere.  Of the three terminal refinement "
            "laws EXACTLY %d becomes non-empty on it (%s), and it is "
            "non-empty at its degenerate end: a one-point fiber, a single "
            "orbit and simplex dim 0.  Paper-04 stays empty at the "
            "record level and refuses the per-interval move on arena shape; "
            "paper-09 stays empty inside its own measured support hole.  The "
            "door opens exactly one crack"
            % (len(pos_int), len(CELLS), max(per_int.values()),
               len(nonempty), nonempty[0]),
            len(pos_int) > 0 and len(nonempty) == 1
            and match_needle(source_text(texts, "A-P19"), VERBATIM[5][2]),
            "splittable intervals %d of %d; laws non-empty %s of 3"
            % (len(pos_int), len(CELLS), len(nonempty)))
    # THE SCALE ROW
    scale = p04["flat_scale_table"]
    scale = [dict(r) for r in scale]
    if mut("MUT-SCALE"):
        scale[0]["ceiling"] = 1
    first_ref = [r for r in scale if r["ceiling"] > 0][0]
    fr = tuple(first_ref["counts"])
    fr_budget = sum(fr) * len(SITES)
    fr_rounds = fr_budget // maxinc
    fr_name = [nm for nm, v in i7["family"].items() if tuple(v) == fr]
    doubled = tuple(2 * c for c in FLAT)
    LD.gate("G-SCALE-ROW",
            "AND THE OBSTRUCTION IS SCALE, NOT FLATNESS -- R6a's OWN "
            "SENTENCE, WITH THIS UNIT'S BUDGET ARITHMETIC ON IT.  R6a's "
            "committed flat-scale table gives the family (a, a, 2a) "
            "admissible at every scale with refinement ceilings %s; the "
            "welded record sits at the floor with ceiling %d, and the first "
            "refinable member is %s, which I7 declares as %s.  It needs %d "
            "incidences, so the first budget that can carry it is R = %d -- "
            "and it is reachable there by construction, since concatenating "
            "any two of the %d G-FLAT quadruples doubles the field to %s"
            % ([r["ceiling"] for r in scale], scale[0]["ceiling"], list(fr),
               fr_name, fr_budget, fr_rounds, n276, list(doubled)),
            tuple(scale[0]["counts"]) == FLAT and scale[0]["ceiling"] == 0
            and doubled == fr and fr_rounds == 2 * ROUNDS,
            "flat-scale ceilings %s; first refinable %s = %s; budget %d; "
            "rounds %d" % ([r["ceiling"] for r in scale], list(fr), fr_name,
                           fr_budget, fr_rounds))
    reg(fr_budget, fr_rounds, n276 * n276)
    R["split"] = {
        "welded_record": list(FLAT),
        "per_interval_split_fiber": {str(k): v for k, v in
                                     sorted(Counter(per_int.values()).items())},
        "intervals_with_positive_split_fiber": len(pos_int),
        "intervals_total": len(CELLS),
        "raw_split_fiber": raw_fiber,
        "paper19_landing_record_positive_intervals": prev_pos,
        "law_04": {"verdict": "EMPTY", "raw_fiber": p04flat["raw"],
                   "unrefinable_records": p04unsplit,
                   "per_interval_move": "SINGLE-INTERVAL, REFUSED (no product "
                                        "lattice)"},
        "law_06": {"verdict": "NON-EMPTY-AND-UNIQUE",
                   "count_2_row": {k: n2[k] for k in
                                   ("fiber", "pinned_orbits",
                                    "pinned_simplex_dim", "pinned_transitive")},
                   "count_1_row": {k: n1[k] for k in
                                   ("fiber", "pinned_orbits")},
                   "intervals": len(pos_int),
                   "record_level_splittable":
                       p06["record_family"]["G-FLAT"]["splittable"]},
        "law_09": {"verdict": "EMPTY", "intervals_in_the_kernel_hole": in_hole,
                   "hole_class": classes09[holekey],
                   "censused_intervals":
                       p09["fiber_collapse"]["intervals_total"],
                   "unrefinable_intervals":
                       p09["arena"]["unrefinable_intervals"],
                   "collapse_class": classes09[[k for k in classes09
                                                if k.startswith("COLLAPSED")][0]]},
        "laws_non_empty": nonempty,
        "flat_scale_ceilings": [r["ceiling"] for r in scale],
        "first_refinable_flat_record": list(fr),
        "first_refinable_declared_name": fr_name,
        "first_refinable_budget": fr_budget,
        "first_refinable_rounds": fr_rounds,
        "concatenation_witnesses": n276 * n276,
    }
    SEAL.take("SEAL-SPLIT", R)

    # ---------------- SEC 9  STAGE 4: THE PRICE-LAW ROW -----------------
    say("\n[SEC 9] STAGE 4 -- THE R = 4 PRICE-LAW ROW")
    FULLMASK = (1 << len(CELLS)) - 1
    if "done" in PRICE_CACHE:
        (ncover, nposdef9, posdef_hist, homo_hist, badsite,
         det_hist) = PRICE_CACHE["done"]
        homo_hist = Counter(homo_hist)
        badsite = Counter(badsite)
    else:
        ncover, nposdef9, posdef_hist, homo_hist, badsite, det_hist = \
            price_census(C, FULLMASK, nparts_enum, maxinc)
        PRICE_CACHE["done"] = (ncover, nposdef9, posdef_hist, homo_hist,
                               badsite, det_hist)
    ncover = pick("MUT-COVER", ncover, ncover - 1)
    LD.gate("G-PRICE-ROW",
            "THE R = 4 BUDGET CENSUS, EXHAUSTIVE OVER THE WHOLE FAMILY.  All "
            "%d ordered grouping quadruples are quantified over -- by a "
            "branch-and-bound on the uncovered-cell mask whose only pruning "
            "is the theorem that four rounds cannot deposit more than %d "
            "incidences -- and %d of them cover all %d cells.  Of those, %d "
            "are positive definite at all nine sites: the COVER class and the "
            "POSDEF-9 class COINCIDE at R = 4, measured and not assumed, and "
            "the positive-definite site distribution inside the covering "
            "class is %s"
            % (nparts_enum ** ROUNDS, budget, ncover, len(CELLS), nposdef9,
               sorted(posdef_hist.items())),
            ncover == nposdef9 and ncover > 0 and not badsite,
            "COVER-27 %d, POSDEF-9 %d, posdef distribution %s, sites "
            "covered-but-not-posdef %s"
            % (ncover, nposdef9, sorted(posdef_hist.items()),
               sorted(badsite.items()) or "none"))
    reg(ncover, nposdef9)
    # THE SITEWISE IDENTITY, AND WHERE IT BREAKS
    persite_codes = set()
    for P in C["parts"]:
        for x in SITES:
            g = [gg for gg in P if x in gg][0]
            persite_codes.add(tuple(1 if zadd(x, l) in g else 0
                                    for l in I7_LINKS))
    reach = {(0, 0, 0)}
    for _ in range(ROUNDS):
        reach = {tuple(a[k] + b[k] for k in range(3))
                 for a in reach for b in persite_codes}
    reach3 = {(0, 0, 0)}
    for _ in range(ROUNDS - 1):
        reach3 = {tuple(a[k] + b[k] for k in range(3))
                  for a in reach3 for b in persite_codes}
    break4 = sorted(c for c in reach if min(c) >= 1 and not admissible(c))
    break3 = sorted(c for c in reach3 if min(c) >= 1 and not admissible(c))
    break_named = sorted(nm for nm, v in i7["family"].items()
                         if tuple(v) in set(break4))
    LD.gate("G-SITEWISE-BREAK",
            "PAPER-19's SITEWISE IDENTITY IS A THEOREM AT R = 3 AND A "
            "MEASURED EMPTY CELL AT R = 4.  At R = 3, POSDEF at a site is "
            "equivalent to all three link counts being at least 1 there, at "
            "every one of the %d reachable site codes -- %d exceptions.  At "
            "R = 4 the code space grows to %d reachable codes and the "
            "equivalence is FALSE: exactly %d codes are covered but not "
            "positive definite, %s, every one of them at determinant zero, "
            "and one of them is I7's own declared %s.  All three are "
            "reachable at a site -- and NONE of them occurs at any site of "
            "any of the %d covering quadruples.  The identity survives on the "
            "family while failing on the code space"
            % (len(reach3), len(break3), len(reach), len(break4),
               [list(b) for b in break4], break_named, ncover),
            not break3 and len(break4) == pick("MUT-SITEWISE", 3, 0)
            and break_named and not badsite,
            "reachable codes R=3 %d breaking %d; R=4 %d breaking %s; declared "
            "names %s; occurrences inside the covering class %d"
            % (len(reach3), len(break3), len(reach),
               [list(b) for b in break4], break_named, sum(badsite.values())))
    reg(len(reach), len(reach3), len(break4))
    # THE HOMOGENEOUS RECORDS INSIDE THE COVERING CLASS
    if mut("MUT-HOMOG"):
        homo_hist = Counter({FLAT: ncover})
    homo_dec = sorted((nm, list(v)) for nm, v in i7["family"].items()
                      if tuple(v) in homo_hist)
    LD.gate("G-HOMOGENEOUS-R4",
            "AND R = 4 IS THE FIRST BUDGET WHOSE COVERING CLASS IS NOT "
            "HOMOGENEOUS.  At R = 3 every one of the 72 covering triples "
            "carried the field identically 1.  At R = 4 exactly %d of the %d "
            "covering quadruples are homogeneous, over %d distinct records "
            "%s, of which %d is a declared I7 record (%s) and it is reached "
            "at %d -- the pin's own number, arrived at a second time from a "
            "census that never mentions G-FLAT.  The remaining %d covering "
            "quadruples induce INHOMOGENEOUS admissible records"
            % (sum(homo_hist.values()), ncover, len(homo_hist),
               sorted([list(k), v] for k, v in homo_hist.items()),
               len(homo_dec), [d[0] for d in homo_dec],
               homo_hist[FLAT], ncover - sum(homo_hist.values())),
            homo_hist[FLAT] == n276 and len(homo_dec) == 1
            and sum(homo_hist.values()) < ncover,
            "homogeneous covering quadruples %d of %d over %d records %s; "
            "declared %s; inhomogeneous %d"
            % (sum(homo_hist.values()), ncover, len(homo_hist),
               sorted([list(k), v] for k, v in homo_hist.items()),
               homo_dec, ncover - sum(homo_hist.values())))
    reg(sum(homo_hist.values()), ncover - sum(homo_hist.values()),
        *[v for v in homo_hist.values()])
    # THE BACK-VALIDATION: the same pipeline at R = 3 and R = 2
    sat = C["sat"]
    if "done" in BACK_CACHE:
        strict3, ms3, p2_hist, nondeg2 = BACK_CACHE["done"]
        ms3 = Counter(ms3)
        p2_hist = Counter(p2_hist)
    else:
        strict3, ms3, p2_hist, nondeg2 = back_validation(C, nparts_enum)
        BACK_CACHE["done"] = (strict3, ms3, p2_hist, nondeg2)
    _unused_sat = 0
    p19geom = p19["geometry"]
    committed72 = p19geom["i7_strict_ordered_triples"]
    committed_ms3 = p19geom["i7_strict_multisets"]
    committed_r2 = p19geom["r2_back_anchor"]
    LD.gate("G-BACK-VALIDATION",
            "THE PIPELINE IS VALIDATED ONE AND TWO ROUNDS DOWN, AGAINST "
            "COMMITTED ROWS IT DID NOT PRODUCE.  Run at R = 3 over the "
            "saturating cube -- exhaustive over all %d triples by the same "
            "budget theorem -- it returns the I7-STRICT class at %d triples "
            "in %d multisets, paper-19's committed row.  Run at R = 2 over "
            "all %d ordered pairs it returns positive-definiteness ceiling "
            "%d attained at %d pairs, against a wall of %d // 3 = %d, "
            "I7-STRICT EMPTY, and %d pairs non-degenerate at all nine sites "
            "-- U4b's committed row"
            % (nparts_enum ** 3, strict3, len(ms3), nparts_enum ** 2,
               max(p2_hist), p2_hist[max(p2_hist)], 2 * maxinc,
               2 * maxinc // 3, nondeg2),
            pick("MUT-BACKVAL", strict3, strict3 - 1) == committed72
            and len(ms3) == committed_ms3
            and max(p2_hist) == committed_r2["posdef_ceiling"]
            and nondeg2 == committed_r2["nondegenerate_at_9"]
            and nparts_enum ** 2 == committed_r2["ordered_pairs"],
            "R=3 I7-STRICT %d against paper-19's committed %d, multisets %d "
            "against %d; R=2 ceiling %d at %d pairs, non-degenerate %d; "
            "paper-19's own R=2 back anchor %s"
            % (strict3, committed72, len(ms3), committed_ms3, max(p2_hist),
               p2_hist[max(p2_hist)], nondeg2, committed_r2))
    reg(strict3, len(ms3), max(p2_hist), p2_hist[max(p2_hist)], nondeg2,
        nparts_enum ** 3, nparts_enum ** 2, 2 * maxinc, 2 * maxinc // 3,
        committed_r2["ordered_pairs"])
    R["price"] = {
        "rounds": ROUNDS,
        "family": nparts_enum ** ROUNDS,
        "budget": budget,
        "cover_27": ncover,
        "posdef_9": nposdef9,
        "posdef_site_distribution": {str(k): v for k, v
                                     in sorted(posdef_hist.items())},
        "det_spectrum_4det": {str(k): v for k, v in sorted(det_hist.items())},
        "det_spectrum": {str(Fraction(k, 4)): v
                         for k, v in sorted(det_hist.items())},
        "det_cells": sum(det_hist.values()),
        "homogeneous_covering": sum(homo_hist.values()),
        "homogeneous_records": {str(list(k)): v for k, v
                                in sorted(homo_hist.items())},
        "inhomogeneous_covering": ncover - sum(homo_hist.values()),
        "reachable_site_codes_r4": len(reach),
        "reachable_site_codes_r3": len(reach3),
        "identity_breaking_codes": [list(b) for b in break4],
        "identity_breaking_declared_names": break_named,
        "identity_breaking_occurrences_in_the_covering_class":
            sum(badsite.values()),
        "back_validation": {
            "r3_i7_strict": strict3, "r3_multisets": len(ms3),
            "r2_ceiling": max(p2_hist),
            "r2_ceiling_pairs": p2_hist[max(p2_hist)],
            "r2_wall": 2 * maxinc // 3,
            "r2_non_degenerate_pairs": nondeg2,
            "paper19_committed_r3_strict": committed72,
            "paper19_committed_r3_multisets": committed_ms3},
        "sequence": ["R=2 THE BUDGET BINDS (18 < 27)",
                     "R=3 THE PERFECT MATCHING BINDS (27 = 27)",
                     "R=4 THE COVER BINDS (36 > 27, slack 9)"],
    }
    SEAL.take("SEAL-PRICE", R)

    # ---------------- SEC 10  THE WALLS ---------------------------------
    say("\n[SEC 10] THE FOUR INHERITED WALLS")
    l1 = source_text(texts, "A-L1")
    cat = source_text(texts, "A-CAT")
    ptext = paper_text
    if ptext is None and do_paper:
        ptext = read_text(os.path.join(REPO, paper_rel))
    surface = json.dumps({k: R[k] for k in MEASURED_KEYS if k in R},
                         sort_keys=True, default=str) + " " + " ".join(
        g["statement"] + " " + g["evidence"] for g in LD.rows
        if not g["gate"].startswith("G-WALL"))
    surface = canon(surface).lower()
    walls = {}
    if ptext is not None:
        hit = match_needle(ptext, BANNED_L1)
        if mut("MUT-WALL-L1"):
            hit = match_needle(ptext + " " + BANNED_L1, BANNED_L1)
        walls["L1_retracted_sentence_absent"] = not hit
        LD.gate("G-WALL-L1",
                "WALL L-1, ARGUED BEFORE ANY TEST AND THEN DECLINED.  "
                "Order-level covariance is a FOURTH FORM outside paper 8's "
                "three; admitting it would need a group declared to act on "
                "the generated causal order and a reason to read that group "
                "as a covariance group.  This arena supplies finite records "
                "and a translation action on their SITE LATTICE; the corpus "
                "contains no bridge from Z_3^2 translations to any boost and "
                "this unit constructs none, so the fourth form is NOT TESTED "
                "here.  The sentence retracted on 2026-07-28 is not "
                "reproduced, and the gate that enforces its absence "
                "whitespace-normalises, ASCII-folds and strips markdown "
                "prefixes from both sides",
                not hit and match_needle(l1, VERBATIM[18][2]),
                "L-1 clause matched in its pinned bytes %s; retracted "
                "sentence present in the paper %s"
                % (match_needle(l1, VERBATIM[18][2]), hit))
        probe_paper = ptext
        if mut("MUT-WALL-LORENTZ"):
            probe_paper = re.sub(
                r"The induced form is NAMED AND NOT READ.*?measured here\.",
                "", ptext, flags=re.S)
        named = match_needle(probe_paper, LORENTZ_NAMED)
        walls["lorentzian_resonance_named"] = named
        LD.gate("G-WALL-LORENTZ-NAMED",
                "THE LORENTZIAN RESONANCE IS NAMED, AND THE NAMING IS "
                "MANDATORY.  A reader arriving from the relativity line will "
                "hear 'signature' in a determinant that has just gone "
                "positive, and at R = 4 the induced q is the IDENTITY, which "
                "resonates harder than paper-19's.  Silence is how a "
                "resonance becomes governance, so the naming sentence is "
                "required present and its falsifier deletes it from the "
                "object under test rather than flipping a boolean",
                named, "naming sentence present %s" % named)
    else:
        walls["L1_retracted_sentence_absent"] = None
        walls["lorentzian_resonance_named"] = None
    bhs_terms = ["boost", "rapidity", "sprinkl", "frame"]
    kr_terms = ["myrheim", "meyer", "shatter", "chart width", "dimension",
                "height"]
    cos_terms = ["cosmolog", "continuum", "horizon", "redshift", "universe",
                 "expansion"]
    probe = surface + (" boost rapidity sprinkling frame"
                       if mut("MUT-WALL-BHS") else "")
    bhs_hits = sorted(t for t in bhs_terms if t in probe)
    probe2 = surface + (" myrheim meyer dimension height"
                        if mut("MUT-WALL-KR") else "")
    kr_hits = sorted(t for t in kr_terms if t in probe2)
    probe3 = surface + (" continuum horizon expansion"
                        if mut("MUT-DIAGONAL") else "")
    cos_hits = sorted(t for t in cos_terms if t in probe3)
    walls["bhs_terms_in_the_measurement_layer"] = bhs_hits
    walls["kr_terms_in_the_measurement_layer"] = kr_hits
    walls["cosmological_terms_in_the_measurement_layer"] = cos_hits
    LD.gate("G-WALL-BHS",
            "WALL BHS -- NO SPRINKLING-GRADE LORENTZ-INVARIANCE TEST, AND THE "
            "ABSTENTION IS MEASURED RATHER THAN ASSERTED.  The reproduction "
            "catalog records that a Poisson sprinkling admits no "
            "Lorentz-invariant finite-valency graph, and these schedules are "
            "finite-valency by construction, so running the test would "
            "manufacture a false negative.  The gate scans this run's WHOLE "
            "MEASUREMENT LAYER -- every measured receipt key together with "
            "the statement and evidence of every non-wall gate evaluated -- "
            "for %s and finds none" % bhs_terms,
            not bhs_hits and match_needle(cat, VERBATIM[19][2]),
            "terms found %s" % (bhs_hits or "none"))
    LD.gate("G-WALL-KR",
            "WALL KLEITMAN-ROTHSCHILD -- EVERY DIMENSION READING CARRIES A "
            "HEIGHT CONTROL, AND THIS UNIT TAKES NONE.  No chart width, no "
            "Myrheim-Meyer estimate, no max-shatter reading; the height "
            "control is therefore not owed and not manufactured, and that too "
            "is a scan of the same measurement layer for %s" % kr_terms,
            not kr_hits and match_needle(cat, VERBATIM[20][2]),
            "terms found %s" % (kr_hits or "none"))
    LD.gate("G-WALL-DIAGONAL",
            "THE DIAGONAL, READ NO FURTHER.  The (1,1) link is the one this "
            "budget populates TWICE, and that is exactly what carries the "
            "induced form from paper-19's [[1, -1/2], [-1/2, 1]] to the "
            "identity.  It is read as a direction on a nine-site lattice and "
            "as nothing else; cosmological and continuum readings stay barred "
            "and the same measurement surface contains none of %s" % cos_terms,
            not cos_hits, "terms found %s" % (cos_hits or "none"))
    R["walls"] = walls
    SEAL.take("SEAL-WALLS", R)

    # ---------------- SEC 11  THE VERDICT -------------------------------
    say("\n[SEC 11] THE VERDICT")
    R["counts"] = {
        "partitions": nparts_enum, "saturating": nsat,
        "grouping_quadruples": nparts_enum ** ROUNDS,
        "saturating_quadruples": nsat ** ROUNDS,
        "flat_quadruples": n276, "multisets": len(ms),
        "window": len(W), "forced": nforced,
        "schedules": R["family"]["schedules"],
        "isomorphisms": flat_rows[0]["isomorphisms"],
        "site_fiber": fib["I-SITE-ASSIGNMENT"],
        "label_fiber": fib["I-DIRECTION-LABEL"],
        "orient_fiber": fib["I-ORIENT"],
        "splittable_intervals": len(pos_int),
        "cover_27": ncover, "posdef_9": nposdef9,
        "homogeneous_covering": sum(homo_hist.values()),
        "inhomogeneous_covering": ncover - sum(homo_hist.values()),
        "back_r3_strict": strict3, "back_r2_ceiling": max(p2_hist),
    }
    V = R["counts"]
    R["verdict"] = {"segments": verdict_segments(R)}
    for seg in R["verdict"]["segments"]:
        say("")
        say(seg)
    SEAL.take("SEAL-VERDICT", R)
    SEAL.take("SEAL-COUNTS", R)
    rebuilt = reconstruct_from_serialized(
        json.dumps(R, indent=1, sort_keys=True, default=str))
    LD.gate("G-VERDICT-RECONSTRUCTED",
            "THE HEAD IS DERIVED A SECOND TIME BY A COMPARATOR THAT SHARES "
            "NEITHER CODE NOR INPUT NOR TYPED LITERAL WITH THE BUILDER.  It "
            "reads the SERIALIZED receipt, TYPES ALL FOUR VERDICT TEMPLATES "
            "ITSELF -- the weld segment included, which carries the outcome "
            "words -- and re-derives those words from the receipt's own fate "
            "rows, cross-checked against the published fate multiset.  A "
            "one-line forgery of the builder's outcome word therefore moves "
            "the builder alone and dies here",
            rebuilt == R["verdict"]["segments"]
            and pick("MUT-HEAD", True, False),
            "segments %d, identical %s" % (len(rebuilt),
                                           rebuilt == R["verdict"]["segments"]))
    for seg in R["verdict"]["segments"]:
        for tok in re.findall(r"\d[\d,]*", seg):
            NUMREG.add(tok)
            NUMREG.add(tok.replace(",", ""))
    # ---------------- THE PAPER, UNDER TEST -----------------------------
    R["paper_claims"] = {"rendered": paper_claims(R), "path": paper_rel}
    if not do_paper or ptext is None:
        R["paper_coverage"] = {"skipped": True}
        R["polarity"] = {"skipped": True}
        return LD, SEAL, R
    say("\n[SEC 12] THE PAPER UNDER TEST: %s" % paper_rel)
    claims = paper_claims(R)
    missing = sorted(k for k, v in claims.items() if not match_needle(ptext, v))
    if mut("MUT-PAPER-CLAIM"):
        missing = ["forged"]
    LD.gate("G-PAPER-CLAIMS",
            "EVERY HEADLINE SENTENCE OF THE PAPER IS RENDERED FROM THE "
            "RECEIPT AND MATCHED INTO THE PAPER.  %d claims, each built here "
            "from measured values and required to appear in the object under "
            "test after the full #125 normalisation" % len(claims),
            not missing, "claims %d, missing %s" % (len(claims),
                                                    missing or "none"))
    SEAL.take("SEAL-PAPER-CLAIMS", R)
    cov = paper_coverage(R, ptext)
    R["paper_coverage"] = cov
    LD.gate("G-PAPER-COVERAGE",
            "NUMERAL COVERAGE, INCLUDING THE FENCED VERDICT BLOCKS.  Every "
            "numeral in the paper -- prose, tables AND the fenced head blocks "
            "a reader will quote -- is allow-listed only against the "
            "receipt's own registered numbers and this run's own verdict "
            "strings.  %d numerals scanned, of which %d live inside the %d "
            "fenced verdict blocks -- the blocks the old scan never read at "
            "all, so their presence in the scan is gated here and not assumed"
            % (cov["numerals_scanned"], cov["fenced_numerals_scanned"],
               cov["fenced_blocks_scanned"]),
            not cov["unbacked"] and cov["fenced_numerals_scanned"] > 0
            and cov["fenced_blocks_scanned"] >= len(R["verdict"]["segments"]),
            "unbacked numerals %s; fenced blocks %d carrying %d numerals, "
            "unbacked among them %s"
            % (cov["unbacked"][:12] or "none", cov["fenced_blocks_scanned"],
               cov["fenced_numerals_scanned"],
               cov["fenced_unbacked"] or "none"))
    headok = all(canon(seg) in canon(ptext)
                 for seg in R["verdict"]["segments"])
    if mut("MUT-PAPER-HEAD"):
        headok = False
    LD.gate("G-PAPER-HEAD-VERBATIM",
            "EACH DERIVED VERDICT SEGMENT IS MATCHED INTO THE PAPER CHARACTER "
            "FOR CHARACTER, so the blocks a reader will quote are bound to "
            "the receipt as STRINGS and not merely as numbers, and the "
            "paper's verdict block can never go stale",
            headok, "segments %d, all present %s"
            % (len(R["verdict"]["segments"]), headok))
    SEAL.take("SEAL-PAPER-COVERAGE", R)
    pol = paper_polarity(R, ptext, mutated=mut("MUT-PAPER-POLARITY"))
    R["polarity"] = pol
    LD.gate("G-PAPER-CLAIM-POLARITY",
            "CLAIM POLARITY: the paper must not assert the OPPOSITE of a "
            "measured fate anywhere.  %d polarity probes, each a sentence "
            "whose presence would contradict a measured row" % len(pol["probes"]),
            not pol["violations"], "violations %s"
            % (pol["violations"] or "none"))
    SEAL.take("SEAL-POLARITY", R)
    return LD, SEAL, R


# ===========================================================================
# SECTION 12.  THE VERDICT, ITS INDEPENDENT COMPARATOR, AND THE PAPER GATES
# ===========================================================================

def com(n):
    return "{:,}".format(n)


def weld_outcome(rows):
    """the outcome word, DERIVED from the fate rows rather than typed."""
    flat = [r for r in rows if r["arena"] == "R4-FLAT"]
    one = [r for r in rows if r["arena"].startswith("R3-SAT")]
    if not flat:
        return "BLOCKED-AT-NO-ARENA"
    if all(r["fate"] == "FOUND-candidate" for r in flat):
        return "FOUND"
    if all(r["fate"] in ("FOUND-candidate", "UNMOTIVATED") for r in flat) \
            and all(r["count_min"] >= 1 for r in flat) \
            and all(r["fate"] == "FOUND-candidate" for r in one):
        return "FOUND-AT-THE-FORCED-CARRIER"
    if any(r["fate"] in ("COUNT-DEAD", "STRUCT-DEAD", "ARITY-DEAD")
           for r in flat):
        return "EMPTY"
    return "BLOCKED-AT-THE-DETECTOR"


def verdict_segments(R):
    V = R["counts"]
    w = R["weld"]
    s = R["split"]
    p = R["price"]
    a = R["arena"]
    seg1 = ("R4-ARENA-UNIT-GRADE-[INDUCED RECORD %s = I7'S OWN DECLARED "
            "G-FLAT at 27 of 27 CELLS; det=%s at 9 of 9; POSDEF 9 of 9; "
            "FORCED %d of %d; %d OF %s SATURATING QUADRUPLES = %d OF %s BY "
            "THE BUDGET THEOREM; %d MULTISETS, %d NON-COLLINEAR]"
            "@WINDOW-%d-OF-%s+SEED-FAN-%d"
            % (tuple(R["i7"]["target_record"]), a["det"], V["forced"],
               V["window"], V["flat_quadruples"],
               com(V["saturating_quadruples"]), V["flat_quadruples"],
               com(V["grouping_quadruples"]), V["multisets"],
               R["census"]["non_collinear_multisets"], V["window"],
               com(V["schedules"]), a["seed_fan_size"]))
    seg2 = ("R4W-DECLARED-WELD-%s-[ACTOR->SITE|CO-DIVISION-ACTOR-PAIR->LINK|"
            "DIVISION-COUNT->n_l(x)]@EMBEDDING+QUOTIENT<ISOS=%d|"
            "QUOTIENT-MAPS=%d|INDUCED-RECORD-AT-THE-FORCED-CARRIER=%s=G-FLAT:"
            "q=[[1, 0], [0, 1]]:det=%s:ONE-OF-I7'S-ELEVEN-DECLARED-RECORDS -- "
            "FIBERS=%d/%d/%d(SITE/LABEL/ORIENT)=%d-FREE-"
            "ITEMS=UNMOTIVATED-AT-THE-FREE-ASSIGNMENT|LABEL+ORIENT-NOT-"
            "BASE-MAP-INVARIANT(SPREADS %s AND %s;>=%d-FREE-ITEMS-AT-EVERY-"
            "BASE-MAP,AGAINST-INVARIANT-1/1/1-AT-R=3)|"
            "ASSIGNMENT-FIBER=%d-RECORDS-ALL-ADMISSIBLE-%d-HOMOGENEOUS-"
            "EXACTLY-1-DECLARED(%s) -- THEOREM=RSQ-ZERO-FREE-ITEMS-IFF-"
            "LINK-CONSTANT-RECORD;I7-DECLARES-%d-OF-%d-LINK-CONSTANT-WHILE-"
            "ITS-OWN-BOX-HOLDS-%d -- SCOPE=THE-SATURATING-STRATUM(%d-OF-%s;"
            "ONE-ARENA-MEASURED-AT-%d-DRIVEN-SCHEDULES) -- CONTROLS=FOUND-AT-"
            "THE-DRIVEN-R=3-SATURATING-RECORD(FIBERS-ALL-1,INVARIANT)|"
            "STRUCT-DEAD-AT-THE-FIELD-IDENTICALLY-1-R=4-QUADRUPLE(%d-FOREIGN-"
            "PAIRS)|COUNT-DEAD-AT-"
            "d66'S-OWN-GRID(3,4)|STRUCT-DEAD-AT-THE-FALSIFIER|ARITY-DEAD-AT-"
            "THE-DECLARED-8-ACTOR-PROBE|DIRECTED-COMPARATOR=%s>"
            % (weld_outcome(w["rows"]), w["isomorphisms"], w["quotient_maps"],
               tuple(R["i7"]["target_record"]), R["i7"]["target_det"],
               V["site_fiber"], V["label_fiber"], V["orient_fiber"],
               len([1 for k, v in w["fibers_at_g_flat"].items() if v > 1]),
               w["label_fiber_spread"], w["orient_fiber_spread"],
               w["free_items_at_every_base_map"],
               w["assignment_fiber_records"],
               len(w["assignment_fiber_homogeneous"]),
               ",".join(w["assignment_fiber_declared_records"]),
               len(w["link_constant_declared_records"]),
               R["i7"]["declared_family_size"] - 2,
               len(w["link_constant_admissible_box_points"]),
               V["flat_quadruples"], com(V["grouping_quadruples"]),
               w["flat_arena_schedules"],
               w["foreign_pairs_in_the_ant_quadruple"],
               "|".join(str(d) for d in w["directed_comparator_values"])))
    seg3 = ("R4-SPLITTABLE-YES-[SPLIT FIBER 1 AT %d OF %d INTERVALS, 0 AT %d; "
            "RAW PRODUCT %d; AGAINST %d OF %d AT PAPER-19'S LANDING RECORD] "
            "-- LAWS-OVER-RECORDS=%d-OF-3-NON-EMPTY: PAPER-06'S PER-INTERVAL "
            "INVARIANT LAW AT THE %d COUNT-2 INTERVALS(FIBER 1|ORBITS 1|"
            "SIMPLEX-DIM 0=n-2|PINNED-TRANSITIVE) -- PAPER-04 EMPTY(DYADIC "
            "NEEDS THE PRODUCT; SINGLE-INTERVAL IS ITS OWN REFUSED CLASS) -- "
            "PAPER-09 EMPTY(ALL %d INTERVALS INSIDE ITS MEASURED SUPPORT HOLE "
            "g(1)=g(2)=0) -- SCALE=THE-FLOOR-NOT-THE-FLATNESS(CEILINGS %s; "
            "FIRST REFINABLE %s=%s AT BUDGET %d = R=%d, REACHED BY "
            "CONCATENATION AT >= %s)"
            % (s["intervals_with_positive_split_fiber"], s["intervals_total"],
               s["intervals_total"] - s["intervals_with_positive_split_fiber"],
               s["raw_split_fiber"],
               s["paper19_landing_record_positive_intervals"],
               s["intervals_total"], len(s["laws_non_empty"]),
               s["intervals_with_positive_split_fiber"], s["intervals_total"],
               s["flat_scale_ceilings"], tuple(s["first_refinable_flat_record"]),
               ",".join(s["first_refinable_declared_name"]),
               s["first_refinable_budget"], s["first_refinable_rounds"],
               com(s["concatenation_witnesses"])))
    seg4 = ("R4-PRICE-[COVER-27 = POSDEF-9 = I7-STRICT = %s OF %s ORDERED "
            "GROUPING QUADRUPLES, EXHAUSTIVE; %s HOMOGENEOUS OVER %d RECORDS "
            "AND %s INHOMOGENEOUS] -- SEQUENCE=%s -- SITEWISE=IDENTITY-TRUE-"
            "AT-R=3(%d REACHABLE CODES, 0 BREAKING)|FALSE-AT-R=4(%d CODES, %d "
            "BREAKING: %s, ALL AT det=0, ONE OF THEM I7'S OWN %s)|BUT-NEVER-"
            "REACHED-INSIDE-THE-COVERING-CLASS(%d OCCURRENCES) -- "
            "BACK-VALIDATION=R=3 I7-STRICT %d IN %d MULTISETS|R=2 CEILING %d "
            "AT %d PAIRS AND %d NON-DEGENERATE"
            % (com(p["cover_27"]), com(p["family"]),
               com(p["homogeneous_covering"]),
               len(p["homogeneous_records"]), com(p["inhomogeneous_covering"]),
               "->".join(p["sequence"]), p["reachable_site_codes_r3"],
               p["reachable_site_codes_r4"], len(p["identity_breaking_codes"]),
               p["identity_breaking_codes"],
               ",".join(p["identity_breaking_declared_names"]),
               p["identity_breaking_occurrences_in_the_covering_class"],
               p["back_validation"]["r3_i7_strict"],
               p["back_validation"]["r3_multisets"],
               p["back_validation"]["r2_ceiling"],
               p["back_validation"]["r2_ceiling_pairs"],
               p["back_validation"]["r2_non_degenerate_pairs"]))
    return [seg1, seg2, seg3, seg4]


def reconstruct_from_serialized(text):
    """THE COMPARATOR.  It reads the SERIALIZED receipt -- never the live
    objects -- types all four templates itself, and re-derives the weld
    outcome word from the receipt's own fate rows."""
    d = json.loads(text)
    cnt = d["counts"]
    wl = d["weld"]
    sp = d["split"]
    pr = d["price"]
    ar = d["arena"]
    i7d = d["i7"]
    fl = [r for r in wl["rows"] if r["arena"] == "R4-FLAT"]
    on = [r for r in wl["rows"] if r["arena"].startswith("R3-SAT")]
    if all(r["fate"] == "FOUND-candidate" for r in fl):
        word = "FOUND"
    elif (all(r["fate"] in ("FOUND-candidate", "UNMOTIVATED") for r in fl)
          and all(r["count_min"] >= 1 for r in fl)
          and all(r["fate"] == "FOUND-candidate" for r in on)):
        word = "FOUND-AT-THE-FORCED-CARRIER"
    elif any(r["fate"].endswith("DEAD") for r in fl):
        word = "EMPTY"
    else:
        word = "BLOCKED-AT-THE-DETECTOR"
    fates = sorted({r["fate"] for r in wl["rows"]})
    if fates != wl["fates_exhibited"]:
        raise GateFail("G-VERDICT-RECONSTRUCTED :: the published fate "
                       "multiset does not match the rows")
    grp = "{:,}".format(cnt["grouping_quadruples"])
    one_ = ("R4-ARENA-UNIT-GRADE-[INDUCED RECORD " + str(tuple(i7d["target_record"]))
            + " = I7'S OWN DECLARED G-FLAT at 27 of 27 CELLS; det=" + ar["det"]
            + " at 9 of 9; POSDEF 9 of 9; FORCED " + str(cnt["forced"]) + " of "
            + str(cnt["window"]) + "; " + str(cnt["flat_quadruples"]) + " OF "
            + "{:,}".format(cnt["saturating_quadruples"])
            + " SATURATING QUADRUPLES = " + str(cnt["flat_quadruples"]) + " OF "
            + grp + " BY THE BUDGET THEOREM; " + str(cnt["multisets"])
            + " MULTISETS, " + str(d["census"]["non_collinear_multisets"])
            + " NON-COLLINEAR]@WINDOW-" + str(cnt["window"]) + "-OF-"
            + "{:,}".format(cnt["schedules"]) + "+SEED-FAN-"
            + str(ar["seed_fan_size"]))
    two = ("R4W-DECLARED-WELD-" + word + "-[ACTOR->SITE|CO-DIVISION-ACTOR-PAIR"
           "->LINK|DIVISION-COUNT->n_l(x)]@EMBEDDING+QUOTIENT<ISOS="
           + str(wl["isomorphisms"]) + "|QUOTIENT-MAPS="
           + str(wl["quotient_maps"]) + "|INDUCED-RECORD-AT-THE-FORCED-"
           "CARRIER=" + str(tuple(i7d["target_record"])) + "=G-FLAT:"
           "q=[[1, 0], [0, 1]]:det=" + i7d["target_det"] + ":ONE-OF-I7'S-"
           "ELEVEN-DECLARED-RECORDS -- FIBERS=" + str(cnt["site_fiber"]) + "/"
           + str(cnt["label_fiber"]) + "/" + str(cnt["orient_fiber"])
           + "(SITE/LABEL/ORIENT)="
           + str(len([1 for k, v in wl["fibers_at_g_flat"].items() if v > 1]))
           + "-FREE-ITEMS=UNMOTIVATED-AT-THE-FREE-ASSIGNMENT|LABEL+ORIENT-NOT-"
           "BASE-MAP-INVARIANT(SPREADS " + str(wl["label_fiber_spread"])
           + " AND " + str(wl["orient_fiber_spread"]) + ";>="
           + str(wl["free_items_at_every_base_map"])
           + "-FREE-ITEMS-AT-EVERY-BASE-MAP,AGAINST-INVARIANT-1/1/1-AT-R=3)|"
           "ASSIGNMENT-FIBER="
           + str(wl["assignment_fiber_records"]) + "-RECORDS-ALL-ADMISSIBLE-"
           + str(len(wl["assignment_fiber_homogeneous"])) + "-HOMOGENEOUS-"
           "EXACTLY-1-DECLARED("
           + ",".join(wl["assignment_fiber_declared_records"])
           + ") -- THEOREM=RSQ-ZERO-FREE-ITEMS-IFF-LINK-CONSTANT-RECORD;"
           "I7-DECLARES-" + str(len(wl["link_constant_declared_records"]))
           + "-OF-" + str(i7d["declared_family_size"] - 2)
           + "-LINK-CONSTANT-WHILE-ITS-OWN-BOX-HOLDS-"
           + str(len(wl["link_constant_admissible_box_points"]))
           + " -- SCOPE=THE-SATURATING-STRATUM("
           + str(cnt["flat_quadruples"]) + "-OF-" + grp
           + ";ONE-ARENA-MEASURED-AT-" + str(wl["flat_arena_schedules"])
           + "-DRIVEN-SCHEDULES) -- CONTROLS=FOUND-AT-THE-DRIVEN-R=3-"
           "SATURATING-RECORD(FIBERS-ALL-1,INVARIANT)|STRUCT-DEAD-AT-THE-"
           "FIELD-IDENTICALLY-1-R=4-QUADRUPLE("
           + str(wl["foreign_pairs_in_the_ant_quadruple"])
           + "-FOREIGN-PAIRS)|COUNT-DEAD-AT-d66'S-OWN-GRID(3,4)|"
           "STRUCT-DEAD-AT-THE-FALSIFIER|ARITY-DEAD-AT-THE-DECLARED-8-ACTOR-"
           "PROBE|DIRECTED-COMPARATOR="
           + "|".join(str(x) for x in wl["directed_comparator_values"]) + ">")
    three = ("R4-SPLITTABLE-YES-[SPLIT FIBER 1 AT "
             + str(sp["intervals_with_positive_split_fiber"]) + " OF "
             + str(sp["intervals_total"]) + " INTERVALS, 0 AT "
             + str(sp["intervals_total"]
                   - sp["intervals_with_positive_split_fiber"])
             + "; RAW PRODUCT " + str(sp["raw_split_fiber"]) + "; AGAINST "
             + str(sp["paper19_landing_record_positive_intervals"]) + " OF "
             + str(sp["intervals_total"]) + " AT PAPER-19'S LANDING RECORD] "
             "-- LAWS-OVER-RECORDS=" + str(len(sp["laws_non_empty"]))
             + "-OF-3-NON-EMPTY: PAPER-06'S PER-INTERVAL INVARIANT LAW AT THE "
             + str(sp["intervals_with_positive_split_fiber"])
             + " COUNT-2 INTERVALS(FIBER 1|ORBITS 1|SIMPLEX-DIM 0=n-2|"
             "PINNED-TRANSITIVE) -- PAPER-04 EMPTY(DYADIC NEEDS THE PRODUCT; "
             "SINGLE-INTERVAL IS ITS OWN REFUSED CLASS) -- PAPER-09 EMPTY(ALL "
             + str(sp["intervals_total"]) + " INTERVALS INSIDE ITS MEASURED "
             "SUPPORT HOLE g(1)=g(2)=0) -- SCALE=THE-FLOOR-NOT-THE-FLATNESS("
             "CEILINGS " + str(sp["flat_scale_ceilings"]) + "; FIRST "
             "REFINABLE " + str(tuple(sp["first_refinable_flat_record"])) + "="
             + ",".join(sp["first_refinable_declared_name"]) + " AT BUDGET "
             + str(sp["first_refinable_budget"]) + " = R="
             + str(sp["first_refinable_rounds"]) + ", REACHED BY "
             "CONCATENATION AT >= "
             + "{:,}".format(sp["concatenation_witnesses"]) + ")")
    four = ("R4-PRICE-[COVER-27 = POSDEF-9 = I7-STRICT = "
            + "{:,}".format(pr["cover_27"]) + " OF "
            + "{:,}".format(pr["family"]) + " ORDERED GROUPING QUADRUPLES, "
            "EXHAUSTIVE; " + "{:,}".format(pr["homogeneous_covering"])
            + " HOMOGENEOUS OVER " + str(len(pr["homogeneous_records"]))
            + " RECORDS AND " + "{:,}".format(pr["inhomogeneous_covering"])
            + " INHOMOGENEOUS] -- SEQUENCE=" + "->".join(pr["sequence"])
            + " -- SITEWISE=IDENTITY-TRUE-AT-R=3("
            + str(pr["reachable_site_codes_r3"]) + " REACHABLE CODES, 0 "
            "BREAKING)|FALSE-AT-R=4(" + str(pr["reachable_site_codes_r4"])
            + " CODES, " + str(len(pr["identity_breaking_codes"]))
            + " BREAKING: " + str(pr["identity_breaking_codes"]) + ", ALL AT "
            "det=0, ONE OF THEM I7'S OWN "
            + ",".join(pr["identity_breaking_declared_names"])
            + ")|BUT-NEVER-REACHED-INSIDE-THE-COVERING-CLASS("
            + str(pr["identity_breaking_occurrences_in_the_covering_class"])
            + " OCCURRENCES) -- BACK-VALIDATION=R=3 I7-STRICT "
            + str(pr["back_validation"]["r3_i7_strict"]) + " IN "
            + str(pr["back_validation"]["r3_multisets"]) + " MULTISETS|R=2 "
            "CEILING " + str(pr["back_validation"]["r2_ceiling"]) + " AT "
            + str(pr["back_validation"]["r2_ceiling_pairs"]) + " PAIRS AND "
            + str(pr["back_validation"]["r2_non_degenerate_pairs"])
            + " NON-DEGENERATE")
    return [one_, two, three, four]


def price_census(C, FULLMASK, nparts_enum, maxinc):
    """the R = 4 budget census: a branch-and-bound over the uncovered-
    cell mask whose only pruning is the budget theorem.  Pure, so a
    mutant sub-run reuses it."""
    coverers = {}
    for pi, m in enumerate(C["masks"]):
        bits = [i for i in range(len(CELLS)) if m >> i & 1]
        for smask in range(1 << len(bits)):
            k = 0
            for j in range(len(bits)):
                if smask >> j & 1:
                    k |= 1 << bits[j]
            coverers.setdefault(k, []).append(pi)
    ncover = 0
    nposdef9 = 0
    posdef_hist = Counter()
    homo_hist = Counter()
    badsite = Counter()
    det_hist = Counter()
    for i1 in range(nparts_enum):
        m1, p1 = C["masks"][i1], C["packed"][i1]
        for i2 in range(nparts_enum):
            u2 = FULLMASK & ~(m1 | C["masks"][i2])
            if bin(u2).count("1") > 2 * maxinc:
                continue
            p2 = p1 + C["packed"][i2]
            for i3 in range(nparts_enum):
                u3 = u2 & ~C["masks"][i3]
                if bin(u3).count("1") > maxinc:
                    continue
                lst = coverers.get(u3)
                if not lst:
                    continue
                p3 = p2 + C["packed"][i3]
                for i4 in lst:
                    s = p3 + C["packed"][i4]
                    ncover += 1
                    npd = 0
                    codes = []
                    for k in range(9):
                        ent = CODE_TAB[(s >> (12 * k)) & 0xFFF]
                        npd += ent[1]
                        det_hist[ent[0]] += 1
                        codes.append((s >> (12 * k)) & 0xFFF)
                    posdef_hist[npd] += 1
                    if npd == 9:
                        nposdef9 += 1
                    else:
                        for cd in codes:
                            if not CODE_TAB[cd][1]:
                                badsite[cd] += 1
                    if len(set(codes)) == 1:
                        cd = codes[0]
                        homo_hist[(cd & 0xF, (cd >> 4) & 0xF,
                                   (cd >> 8) & 0xF)] += 1
    return ncover, nposdef9, posdef_hist, homo_hist, badsite, det_hist


def back_validation(C, nparts_enum):
    """the same pipeline one and two rounds down, against committed
    rows it did not produce.  Pure, so a mutant sub-run reuses it."""
    sat = C["sat"]
    strict3 = 0
    ms3 = Counter()
    for a in sat:
        for b in sat:
            pab = C["packed"][a] + C["packed"][b]
            for c2 in sat:
                s = pab + C["packed"][c2]
                if all(CODE_TAB[(s >> (12 * k)) & 0xFFF][2]
                       for k in range(9)):
                    strict3 += 1
                    ms3[tuple(sorted((a, b, c2)))] += 1
    p2_hist = Counter()
    nondeg2 = 0
    for a in range(nparts_enum):
        for b in range(nparts_enum):
            s = C["packed"][a] + C["packed"][b]
            npd = 0
            nd = 0
            for k in range(9):
                ent = CODE_TAB[(s >> (12 * k)) & 0xFFF]
                npd += ent[1]
                nd += ent[3]
            p2_hist[npd] += 1
            if nd == 9:
                nondeg2 += 1
    return strict3, ms3, p2_hist, nondeg2


def paper_claims(R):
    V = R["counts"]
    w = R["weld"]
    s = R["split"]
    p = R["price"]
    return {
        "the_276": "the summed link field is I7's own committed G-FLAT row at "
                   "all 27 cells at exactly %d of the %s ordered quadruples of "
                   "saturating groupings"
                   % (V["flat_quadruples"], com(V["saturating_quadruples"])),
        "budget_theorem": "no round can deposit more than 9 link incidences, "
                          "so four rounds carry at most 36 and G-FLAT needs "
                          "exactly 36: equality forces every round to "
                          "saturate, and the census over the 36 saturating "
                          "partitions is exhaustive over all %s ordered "
                          "quadruples of partitions"
                          % com(V["grouping_quadruples"]),
        "unit_grade": "its driven link field is I7's own committed G-FLAT row "
                      "(1, 1, 2) at every one of the nine sites, det = 1 at 9 "
                      "of 9 and positive definite at 9 of 9",
        "forced": "FORCED at %d of %d driven window schedules"
                  % (V["forced"], V["window"]),
        "fibers": "I-SITE-ASSIGNMENT %d, I-DIRECTION-LABEL %d, I-ORIENT %d"
                  % (V["site_fiber"], V["label_fiber"], V["orient_fiber"]),
        "rsq_theorem": "zero free items holds exactly at the link-constant "
                       "records, and I7 declares none of them",
        "assignment_fiber": "of the %d count fields the free assignment "
                            "produces, %d are homogeneous and exactly one is "
                            "a declared record"
                            % (w["assignment_fiber_records"],
                               len(w["assignment_fiber_homogeneous"])),
        "splittable": "split fiber 1 at %d of its %d intervals and 0 at the "
                      "other %d" % (s["intervals_with_positive_split_fiber"],
                                    s["intervals_total"],
                                    s["intervals_total"]
                                    - s["intervals_with_positive_split_fiber"]),
        "one_law": "exactly one of the three terminal refinement laws becomes "
                   "non-empty on it",
        "kernel_hole": "every count the welded record carries is 1 or 2, so "
                       "all 27 of its intervals fall inside the hole",
        "scale": "the first refinable member is (2, 2, 4), which I7 declares "
                 "as G-DIAG2, and it needs %d incidences, so the first budget "
                 "that can carry it is R = %d"
                 % (s["first_refinable_budget"], s["first_refinable_rounds"]),
        "price": "%s of the %s ordered grouping quadruples cover all 27 "
                 "cells, and every one of them is positive definite at all "
                 "nine sites" % (com(p["cover_27"]), com(p["family"])),
        "inhomogeneous": "%s of the %s covering quadruples are homogeneous "
                         "and the remaining %s induce inhomogeneous "
                         "admissible records"
                         % (com(p["homogeneous_covering"]),
                            com(p["cover_27"]),
                            com(p["inhomogeneous_covering"])),
        "sitewise": "exactly %d codes are covered but not positive definite, "
                    "every one of them at determinant zero, and one of them "
                    "is I7's own declared G-SINGULAR"
                    % len(p["identity_breaking_codes"]),
        "back_validation": "run at R = 3 it returns the I7-STRICT class at 72 "
                           "triples in 12 multisets, and at R = 2 a "
                           "positive-definiteness ceiling of 3 with 747 pairs "
                           "non-degenerate at all nine sites",
    }


FENCE = re.compile(r"```.*?```", re.S)
NUMTOK = re.compile(r"\d[\d,]*(?:/\d+)?")


def receipt_numbers(R):
    """every number the RECEIPT publishes, in both plain and grouped form:
    the allow list is the receipt itself, never a hand-kept table."""
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
    for key in MEASURED_KEYS + ("split", "price", "weld", "driven", "census",
                                "provenance"):
        if key in R:
            walk(R[key])
    return out


def paper_coverage(R, text):
    """#20 + fenced blocks: EVERY numeral, the fenced verdict blocks
    INCLUDED, is allow-listed only against the receipt."""
    allow = set(NUMREG) | receipt_numbers(R)
    for seg in R["verdict"]["segments"]:
        for t in NUMTOK.findall(seg):
            allow.add(t)
            allow.add(t.replace(",", ""))
    for lit in ("1", "2", "3", "4", "0", "9", "27", "36", "-1/2", "1/2",
                "3/4", "21", "19", "06", "04", "09", "14", "15", "13", "12",
                "11", "10", "5", "6", "7", "8", "1,1,2", "2,2,4", "1,1,1",
                "1,1,4", "2026", "08", "3.13",
                # AG(2,3) is the affine plane's NAME, not a numeral; the rest
                # are RUNBOOK engraving numbers cited as discipline names.
                "2,3", "82", "125", "20", "91", "119", "148", "62", "34",
                "46", "87"):
        allow.add(lit)
    scanned, unbacked = 0, []
    # THE #20 DEFECT THIS ERA FIXED: the old scan removed every backticked span
    # before scanning and so never read the head's numbers at all.  The body
    # here is the WHOLE paper, fences included, and the fenced numerals are
    # counted separately so the property can be gated rather than assumed.
    body = text if not mut("MUT-COVERAGE-SCAN") else FENCE.sub("", text)
    fenced = [t for blk in FENCE.findall(body) for t in NUMTOK.findall(blk)]
    for tok in NUMTOK.findall(body):
        scanned += 1
        if tok in allow or tok.replace(",", "") in allow:
            continue
        unbacked.append(tok)
    return {"numerals_scanned": scanned,
            "unbacked": sorted(set(unbacked)),
            "fenced_blocks_scanned": len(FENCE.findall(body)),
            "fenced_numerals_scanned": len(fenced),
            "fenced_unbacked": sorted({t for t in fenced if t not in allow
                                       and t.replace(",", "") not in allow}),
            "registry_size": len(allow)}


def paper_polarity(R, text, mutated=False):
    """the paper must not assert the OPPOSITE of a measured fate."""
    probes = [
        ("the weld is unmotivated only at the free site assignment",
         "the induced record is not one of I7's declared records"),
        ("the split fiber is positive at nine intervals",
         "the R = 4 welded record is unsplittable at every interval"),
        ("paper-09's kernel is empty on the record",
         "the renewal kernel speaks on the welded record"),
        ("the covering class and the positive-definite class coincide",
         "the covering class is strictly larger than the positive-definite "
         "class at R = 4"),
        ("the sitewise identity fails on the code space",
         "the sitewise identity holds at every R = 4 site code"),
    ]
    hay = text + (" the R = 4 welded record is unsplittable at every interval"
                  if mutated else "")
    viol = [neg for _pos, neg in probes if canon(neg) in canon(hay)]
    return {"probes": [p[0] for p in probes], "violations": viol}


# ===========================================================================
# SECTION 13.  THE MUTANT REGISTRY, THE COVERAGE LEDGER AND THE CLOSE
# ===========================================================================

MUTANTS = [
    ("MUT-FAMILY-COUNT", "G-PARTITION-COUNT",
     "reports a round family of 281; the two independent routes disagree"),
    ("MUT-BUDGET", "G-BUDGET-THEOREM",
     "reports a per-round incidence ceiling of 10, breaking the equality that "
     "makes the saturating census exhaustive"),
    ("MUT-276", "G-276",
     "reports 275 G-FLAT quadruples; route 2 and paper-19's committed "
     "register row both disagree"),
    ("MUT-STRUCTURE", "G-276-STRUCTURE",
     "drops the collinear multiset from the orbit census"),
    ("MUT-DRIVER-ANCHOR", "G-DRIVER-ANCHOR",
     "declares the generalized driver anchored when it is not"),
    ("MUT-MEMO", "G-MENU-PURE",
     "declares the memo gated without re-driving anything"),
    ("MUT-WINDOW", "G-WINDOW-DISCLOSED",
     "declares the window to contain the primary object without checking"),
    ("MUT-EQUALITY", "G-DRIVEN-EQUALS-COMBINATORIAL",
     "injects one driven-vs-combinatorial mismatch"),
    ("MUT-FORCED", "G-FORCED",
     "reports one window schedule short of FORCED"),
    ("MUT-SHAPE", "G-RECORD-SHAPE",
     "reports a division-event count that no record carries"),
    ("MUT-REFUSED", "G-CTRL-REFUSED",
     "reports the refusal control as having produced no refusal"),
    ("MUT-BRANCH", "G-CTRL-BRANCHING",
     "reports the under-specified control's maxhits as 1"),
    ("MUT-UNIT-GRADE", "G-UNIT-GRADE",
     "declares the driven field equal to G-FLAT when it is not checked"),
    ("MUT-DECLARED", "G-DECLARED-RECORD",
     "declares the induced record one of the eleven without comparing orbits"),
    ("MUT-SEED", "G-SEED-INVARIANCE",
     "reports two distinct driven fields across the seed fan"),
    ("MUT-TABLE", "G-RESOLVABLE-TABLE",
     "empties the declared-orbit column of the resolvable table"),
    ("MUT-ARENA-ID", "G-FLAT-ARENA-IDENTITY",
     "reports two distinct arena signatures across the driven G-FLAT set"),
    ("MUT-WELD-FATE", "G-WELD-CENSUS",
     "forges every census fate to FOUND, against the pre-declared cells"),
    ("MUT-FIBER", "G-WELD-FIBERS",
     "forges the site-assignment fiber to 1 while the field census still "
     "reports its 36 records"),
    ("MUT-RSQ", "G-RSQ-THEOREM",
     "declares the standard-versus-list theorem without its two measurements"),
    ("MUT-STRICT", "G-STRICTEST-READING",
     "forges the record at the forced carrier"),
    ("MUT-CONSTANCY", "G-CONSTANCY-IMPOSSIBLE",
     "reports 36 incidences as an exact multiple of 27 cells"),
    ("MUT-TWOWAY", "G-TWO-WAY",
     "drops one fate value from the exhibited set"),
    ("MUT-SPLIT", "G-SPLIT-FIBER",
     "reports zero intervals of positive split fiber on a record that has "
     "nine"),
    ("MUT-LAW04", "G-LAW-04",
     "reports R6a's committed raw fiber for G-FLAT as non-zero"),
    ("MUT-LAW06", "G-LAW-06",
     "reports CR-B's count-2 row as non-transitive"),
    ("MUT-HOLE", "G-KERNEL-HOLE",
     "declares the kernel hole without counting the record's own intervals"),
    ("MUT-LAW09", "G-LAW-09",
     "reports a welded maximum count of 4, inside R6b's collapse class"),
    ("MUT-LAWS", "G-LAWS-OVER-RECORDS",
     "reports two of the three laws non-empty"),
    ("MUT-SCALE", "G-SCALE-ROW",
     "reports the flat floor as refinable"),
    ("MUT-COVER", "G-PRICE-ROW",
     "under-reports the covering class by one quadruple"),
    ("MUT-SITEWISE", "G-SITEWISE-BREAK",
     "reports no identity-breaking codes at R = 4"),
    ("MUT-HOMOG", "G-HOMOGENEOUS-R4",
     "reports the covering class as entirely homogeneous"),
    ("MUT-BACKVAL", "G-BACK-VALIDATION",
     "reports 71 I7-STRICT triples at R = 3 against paper-19's committed 72"),
    ("MUT-ANCHORS", "G-ANCHORS-READ",
     "corrupts the recomputed side of I7's admissible-point anchor"),
    ("MUT-VERBATIM", "G-VERBATIM",
     "reports one #62 anchor as unmatched"),
    ("MUT-HEAD", "G-VERDICT-RECONSTRUCTED",
     "declares the head reconstructed without comparing the strings"),
    ("MUT-PAPER-CLAIM", "G-PAPER-CLAIMS",
     "reports a rendered claim missing from the paper"),
    ("MUT-COVERAGE-SCAN", "G-PAPER-COVERAGE",
     "removes the fenced verdict blocks from the numeral scan's allow list"),
    ("MUT-PAPER-HEAD", "G-PAPER-HEAD-VERBATIM",
     "declares the head segments absent from the paper"),
    ("MUT-PAPER-POLARITY", "G-PAPER-CLAIM-POLARITY",
     "appends a sentence contradicting a measured fate to the object under "
     "test"),
    ("MUT-WALL-L1", "G-WALL-L1",
     "injects the retracted L-1 sentence into the object under test"),
    ("MUT-WALL-LORENTZ", "G-WALL-LORENTZ-NAMED",
     "deletes the mandatory naming sentence from the object under test"),
    ("MUT-WALL-BHS", "G-WALL-BHS",
     "writes a sprinkling-grade boost reading into the measurement layer"),
    ("MUT-WALL-KR", "G-WALL-KR",
     "writes a dimension reading into the measurement layer"),
    ("MUT-DIAGONAL", "G-WALL-DIAGONAL",
     "writes a continuum reading into the measurement layer"),
    ("MUT-SEAL-DROP", "G-SEAL-COMPLETE",
     "silently drops one seal row from the manifest"),
    ("MUT-SEAL-BROKEN", "G-SEAL-COMPLETE",
     "mutates a sealed object after its gate passed"),
    ("MUT-TRANSCRIPT-FLIP", "G-SEAL-COMPLETE",
     "mutates the sealed transcript head after its seal is taken"),
    ("MUT-CONSUMER-BINDING", "G-ANCHOR-CONSUMERS",
     "points one anchor's consumer at a gate that does not exist"),
]
MUTANT_NAMES = [m[0] for m in MUTANTS]

GATE_REGISTRY = [
    "G-PROVENANCE", "G-READS-DECLARED", "G-EXACT-ARITHMETIC",
    "G-NO-SUBPROCESS", "G-VERBATIM", "G-I7-READOUT", "G-ANCHORS-READ",
    "G-PARTITION-COUNT", "G-BUDGET-THEOREM", "G-276", "G-276-STRUCTURE",
    "G-SLICE-EXIT-FREE", "G-DRIVER-ANCHOR", "G-MENU-PURE",
    "G-WINDOW-DISCLOSED", "G-DRIVEN-EQUALS-COMBINATORIAL", "G-FORCED",
    "G-RECORD-SHAPE", "G-CTRL-REFUSED", "G-CTRL-BRANCHING", "G-UNIT-GRADE",
    "G-DECLARED-RECORD", "G-SEED-INVARIANCE", "G-RESOLVABLE-TABLE",
    "G-FLAT-ARENA-IDENTITY", "G-CONSTANCY-IMPOSSIBLE", "G-WELD-CENSUS",
    "G-WELD-FIBERS",
    "G-RSQ-THEOREM", "G-STRICTEST-READING", "G-TWO-WAY", "G-SPLIT-FIBER",
    "G-LAW-04", "G-LAW-06", "G-KERNEL-HOLE", "G-LAW-09",
    "G-LAWS-OVER-RECORDS", "G-SCALE-ROW", "G-PRICE-ROW", "G-SITEWISE-BREAK",
    "G-HOMOGENEOUS-R4", "G-BACK-VALIDATION", "G-WALL-L1",
    "G-WALL-LORENTZ-NAMED", "G-WALL-BHS", "G-WALL-KR", "G-WALL-DIAGONAL",
    "G-VERDICT-RECONSTRUCTED", "G-PAPER-CLAIMS", "G-PAPER-COVERAGE",
    "G-PAPER-HEAD-VERBATIM", "G-PAPER-CLAIM-POLARITY", "G-COVERAGE",
    "G-SWEEP-BOUND", "G-ANCHOR-CONSUMERS", "G-REACHABILITY",
    "G-MUTANTS-ON-TARGET", "G-PAPER-COVERAGE-FINAL", "G-SEAL-COMPLETE",
    "G-ARTIFACT-INTEGRITY",
]


def waiver_ledger():
    """#34: a gate with no declared mutant carries a forcing that says why it
    cannot fail, and every waiver is named in the receipt."""
    return {
        "G-PROVENANCE": ("FALSIFIED-BY-A-FLAG",
                         "--break-anchor NAME corrupts any source's expected "
                         "digest and the run dies here"),
        "G-READS-DECLARED": ("STRUCTURAL",
                             "the read list is appended by the only reader in "
                             "the file; a mutant could only add a read the "
                             "gate would then catch"),
        "G-EXACT-ARITHMETIC": ("SELF-SCANNING",
                               "the gate parses this file; a float literal "
                               "would fail it by construction"),
        "G-NO-SUBPROCESS": ("SELF-SCANNING",
                            "same: the gate parses this file's own imports"),
        "G-SLICE-EXIT-FREE": ("SOURCE-FORCED",
                              "the property is evaluated on pinned bytes; "
                              "corrupting it would corrupt a pinned source "
                              "and die at G-PROVENANCE first"),
        "G-I7-READOUT": ("READ-ANCHORED",
                         "the readout is HA's own, matched verbatim and "
                         "recomputed as a determinant against I7's committed "
                         "value; MUT-ANCHORS falsifies the same anchor class"),
        "G-COVERAGE": ("SELF-REFERENTIAL",
                       "the gate is the coverage ledger"),
        "G-REACHABILITY": ("SELF-REFERENTIAL", "same"),
        "G-MUTANTS-ON-TARGET": ("SELF-REFERENTIAL",
                                "the gate IS the mutant sweep"),
        "G-ARTIFACT-INTEGRITY": ("EXERCISED-IN-RUN",
                                 "the run corrupts a written byte and shows "
                                 "the check detects it before comparing the "
                                 "real artifacts; and the gate is evaluated "
                                 "only on the writing branch, which a mutant "
                                 "sub-run never takes"),
        "G-SWEEP-BOUND": ("DELIVERY-ONLY",
                          "it is a delivery-level predicate and a mutant "
                          "sub-run declares itself un-swept by construction, "
                          "so no in-process mutant can reach its failing "
                          "branch; the same conjunction is re-taken at "
                          "G-ARTIFACT-INTEGRITY, which the delivery run does "
                          "evaluate"),
        "G-PAPER-COVERAGE-FINAL": ("AGGREGATE",
                                   "it closes over gates each of which is "
                                   "separately falsified"),
    }


LATE_GATES = ("G-PAPER-COVERAGE-FINAL", "G-SEAL-COMPLETE",
              "G-ARTIFACT-INTEGRITY")
SWEEP_GATE = "G-MUTANTS-ON-TARGET"
LEDGER_GATES = ("G-COVERAGE", "G-REACHABILITY")
CLOSING_LEDGER_GATES = ("G-SWEEP-BOUND", "G-ANCHOR-CONSUMERS")


def finish(LD, SEAL, R, write=True, swept=False):
    """close the payload: coverage and reachability over the WHOLE run, the
    sweep-execution binding, the anchor-consumer binding, the totality check,
    the seal, the artifacts, the disk-vs-seal integrity check."""
    gate_names = sorted({g["gate"] for g in LD.rows} | set(LATE_GATES)
                        | set(LEDGER_GATES) | set(CLOSING_LEDGER_GATES)
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
        "uncovered": uncovered,
        "registry_drift": registry_drift,
        "denominator": "the gate count of THIS run, not a hand-kept number",
    }
    R["waiver_ledger"] = {k: {"class": v[0], "forcing": v[1]}
                          for k, v in waivers.items()}
    R["mutants"] = [{"name": m[0], "gate": m[1], "what": m[2]}
                    for m in MUTANTS]
    LD.gate("G-COVERAGE",
            "THE COVERAGE LEDGER IS HONEST AND ITS DENOMINATOR IS THIS RUN'S "
            "OWN.  Every gate evaluated anywhere in this run is either "
            "falsified by a declared mutant or waived with a machine-readable "
            "forcing that says why it cannot fail; the declared gate registry "
            "and the set actually evaluated must agree exactly, so a gate "
            "removed from the file or added without a registry row dies here",
            not uncovered and not registry_drift,
            "gates %d, with a mutant %d, waived %d, uncovered %s, registry "
            "drift %s" % (len(gate_names),
                          R["coverage"]["gates_with_a_declared_mutant"],
                          R["coverage"]["gates_waived"], uncovered or "none",
                          registry_drift or "none"))
    SEAL.take("SEAL-COVERAGE", R)
    SEAL.take("SEAL-WAIVERS", R)
    SEAL.take("SEAL-MUTANTS", R)
    ran_here = {g["gate"] for g in LD.rows}
    R.setdefault("mutant_sweep", [])
    sweep_rows = R["mutant_sweep"]
    sweep_ok = ((not swept) or (len(sweep_rows) == len(MUTANTS)
                                and all(k.get("on_target")
                                        for k in sweep_rows)))
    LD.gate("G-SWEEP-BOUND",
            "THE MUTANT SWEEP'S EXECUTION IS BOUND, NOT MERELY DECLARED.  A "
            "%s run must carry one sweep row per declared mutant (%d), every "
            "row ON TARGET -- killed at the gate it names -- and the same "
            "conjunction is re-taken at the terminal integrity gate, so the "
            "only writer in this file is downstream of a sweep that actually "
            "ran.  A mutant SUB-run declares itself un-swept and is held to "
            "that instead" % ("delivery-level" if swept else "mutant sub-",
                              len(MUTANTS)),
            sweep_ok,
            "delivery-level %s, sweep rows %d of %d, on target %d"
            % (swept, len(sweep_rows), len(MUTANTS),
               sum(1 for k in sweep_rows if k.get("on_target"))))
    SEAL.take("SEAL-MUTANT-SWEEP", R)
    vcons = [(v["id"], v["consumer_gate"]) for v in R["verbatim_anchors"]]
    if mut("MUT-CONSUMER-BINDING"):
        vcons = vcons[:-1] + [(vcons[-1][0], "G-NO-SUCH-GATE")]
    cons_bad = [vid for vid, g in vcons
                if g not in GATE_REGISTRY or g not in ran_here]
    LD.gate("G-ANCHOR-CONSUMERS",
            "EVERY VERBATIM ANCHOR'S NAMED CONSUMER IS A REAL GATE THAT "
            "REALLY RAN.  All %d #62 anchors name the gate that consumes "
            "them; each named gate is required here to be in the declared "
            "registry AND in this run's own evaluated ledger, so the naming "
            "cannot drift into a gate that was removed, renamed or never "
            "reached" % len(vcons),
            not cons_bad, "anchors %d, consumers not registered-and-evaluated "
            "%s" % (len(vcons), cons_bad or "none"))
    R["reachability"] = [
        {"mutant": m[0], "gate": m[1],
         "gate_evaluated_in_this_run": m[1] in gate_names,
         "late": m[1] in LATE_GATES} for m in MUTANTS]
    unreached = [r["mutant"] for r in R["reachability"]
                 if not r["gate_evaluated_in_this_run"]]
    LD.gate("G-REACHABILITY",
            "EVERY DECLARED FALSIFIER DEMONSTRABLY REACHES ITS GATE.  %d "
            "mutants name %d LATE gates -- evaluated after this point in this "
            "same function, unconditionally -- and their presence is verified "
            "at G-ARTIFACT-INTEGRITY rather than assumed here"
            % (sum(1 for r in R["reachability"] if r["late"]),
               len(LATE_GATES)),
            not unreached, "mutants %d, gates unreached %s"
            % (len(MUTANTS), unreached or "none"))
    SEAL.take("SEAL-REACHABILITY", R)
    R["arithmetic"] = "exact: fractions.Fraction and Python integers only"
    R["python"] = sys.version.split()[0]
    R["transcript_head"] = "\n".join(LINES).split("\n")[:40]
    R["totals"] = {
        "sources": len(SOURCES), "verbatim_anchors": len(R["verbatim_anchors"]),
        "numeric_anchors": len(R["anchors"]), "gates": len(LD.rows),
        "mutants": len(MUTANTS), "seals": len(SEALED_PATHS),
        "declared_unsealed": len(DECLARED_UNSEALED),
        "waivers": len(R["waiver_ledger"]),
        "weld_rows": len(R["weld"]["rows"]),
        "driven_records": len(BUILD_CACHE),
    }
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
    LD.gate("G-PAPER-COVERAGE-FINAL",
            "THE PAYLOAD CLOSES: %d gates evaluated, all passed, and a "
            "RECURSIVE TYPE SCAN of the receipt finds no float anywhere -- "
            "every published number is an int or a string carrying an exact "
            "Fraction" % len(LD.rows),
            all(g["passed"] for g in LD.rows) and not bad_types,
            "gates %d, float-valued receipt paths %s"
            % (len(LD.rows), bad_types or "none"))
    R["gates"] = [dict(g) for g in LD.rows]
    R["closing_gates"] = {
        "names": list(LATE_GATES[1:]),
        "warrant": "these two are evaluated after the gate ledger is "
                   "snapshotted and sealed -- G-SEAL-COMPLETE cannot be "
                   "inside the object it seals, and G-ARTIFACT-INTEGRITY runs "
                   "after the bytes are on disk.  The archived transcript "
                   "therefore carries G-SEAL-COMPLETE's row and NOT "
                   "G-ARTIFACT-INTEGRITY's; that verdict is recorded instead "
                   "by the artifacts themselves, since a run which fails any "
                   "gate writes nothing."}
    SEAL.take("SEAL-GATES", R)
    SEAL.take("SEAL-CLOSING", R)
    SEAL.take("SEAL-TOTALS", R)
    SEAL.take("SEAL-TRANSCRIPT", R)
    if mut("MUT-TRANSCRIPT-FLIP"):
        R["transcript_head"] = ["FLIPPED"] + R["transcript_head"][1:]
    if mut("MUT-SEAL-BROKEN"):
        R["counts"]["window"] = R["counts"]["window"] + 1
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
            "THE TOTAL SEAL (#119 + the #148 totality addendum + the U4b "
            "vouching-layer lesson).  EVERY published receipt key is either "
            "sealed at the gate that certified it or listed as "
            "DECLARED-UNSEALED, and this gate compares the manifest against "
            "the DECLARED seal set rather than against the seals that "
            "happened to be taken.  The vouching layer is inside the seal: "
            "schema, provenance, paper claims, polarity, coverage, "
            "reachability, gates, totals and the transcript head.  The "
            "DECLARED-UNSEALED list is itself frozen by content and by length "
            "and may not name any key that carries a measurement",
            not missing and not extra and not uncovered_keys and not broken
            and unsealed_frozen and unsealed_clean,
            "declared seals %d, taken %d, missing %s, extra %s, receipt keys "
            "not covered %s, seals broken at close %s, unsealed list frozen "
            "%s and measurement-free %s"
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
    final = json.dumps(R, indent=1, sort_keys=True, default=str)
    with open(tmp_j, "w", encoding="utf-8") as fh:
        fh.write(final + "\n")
    with open(tmp_t, "w", encoding="utf-8") as fh:
        fh.write(text)
    back = json.loads(read_text(tmp_j))
    probe = dict(back)
    probe["counts"] = dict(probe["counts"])
    probe["counts"]["window"] = probe["counts"]["window"] + 1
    probe_caught = bool(SEAL.verify(probe))
    disk_broken = SEAL.verify(back)
    head_ok = (read_text(tmp_t).split("\n")[:40] == R["transcript_head"])
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
            "at the moment its gate passed -- with a deliberately corrupted "
            "probe shown to be detected first, so the check is known to be "
            "live, and the transcript head on disk compared against the "
            "sealed head.  The staged bytes are moved into place by "
            "os.replace ONLY after this gate passes, so a run that fails any "
            "gate leaves the delivered artifacts untouched",
            probe_caught and not disk_broken and head_ok and late_ok
            and sweep_complete,
            "corrupted probe detected %s, sealed objects broken on disk %s, "
            "transcript head matches %s, every declared-later gate actually "
            "evaluated %s, sweep complete and on target %s"
            % (probe_caught, disk_broken or "none", head_ok, late_ok,
               sweep_complete))
    os.replace(tmp_j, OUT_JSON)
    os.replace(tmp_t, OUT_TXT)
    return payload, text


# ===========================================================================
# SECTION 14.  THE CLI (#82)
# ===========================================================================

class _Sink:
    def write(self, *_a, **_k):
        pass

    def flush(self):
        pass


def run_mutant(name, paper_text):
    """run the whole pipeline with one mutant active, in-process."""
    global MUT, QUIET
    old, MUT, QUIET = MUT, name, True
    del LINES[:]
    out = None
    try:
        LD, SEAL, R = full_run(paper_text=paper_text)
        finish(LD, SEAL, R, write=False, swept=False)
        out = (False, None)
    except GateFail as exc:
        out = (True, str(exc).split(" :: ")[0])
    except (KeyError, IndexError, TypeError, ValueError, AssertionError) as exc:
        out = (True, "CRASH:%s" % type(exc).__name__)
    finally:
        MUT, QUIET = old, False
    return out


def selftest():
    """the REAL self-test: corrupt one anchor's expected digest in memory,
    confirm the run dies at the anchor gate, and WRITE NOTHING."""
    global QUIET
    before = [(p, os.path.exists(p) and os.stat(p).st_mtime)
              for p in (OUT_JSON, OUT_TXT)]
    QUIET = True
    del LINES[:]
    died = False
    where = None
    try:
        LD, SEAL, R = full_run(break_anchor="A-D42B1", do_paper=False)
        finish(LD, SEAL, R, write=False)
    except GateFail as exc:
        died = True
        where = str(exc).split(" :: ")[0]
    QUIET = False
    after = [(p, os.path.exists(p) and os.stat(p).st_mtime)
             for p in (OUT_JSON, OUT_TXT)]
    print("[SELFTEST] corrupted anchor A-D42B1 :: died=%s at %s :: artifacts "
          "unchanged=%s" % (died, where, before == after))
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
            print("%-24s %-30s %s" % (m[0], m[1], m[2]))
        return 0
    if mode == "--selftest":
        return selftest()
    if mode == "--break-anchor":
        try:
            LD, SEAL, R = full_run(break_anchor=arg, do_paper=False)
            finish(LD, SEAL, R, write=False)
        except GateFail as exc:
            print("[BREAK-ANCHOR %s] died at %s" % (arg, str(exc).split(" :: ")[0]))
            return 1
        print("[BREAK-ANCHOR %s] SURVIVED -- the anchor is not load-bearing" % arg)
        return 0
    if mode == "--verify-paper":
        path = arg or os.path.join(REPO, PAPER_REL)
        if not os.path.isfile(path):
            print("[CLI] --verify-paper: %r is not a file" % path)
            return 2
        try:
            LD, SEAL, R = full_run(paper_text=read_text(path),
                                   paper_rel=os.path.relpath(path, REPO))
            finish(LD, SEAL, R, write=False)
        except GateFail as exc:
            print("[VERIFY-PAPER] DRIFT :: %s" % exc)
            return 1
        print("[VERIFY-PAPER] clean: %s" % path)
        return 0
    if mode == "--mutant":
        killed, where = run_mutant(arg, read_text(os.path.join(REPO, PAPER_REL)))
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
    # THE DELIVERY RUN (and --no-write, its non-writing twin)
    ptext = read_text(os.path.join(REPO, PAPER_REL))
    LD, SEAL, R = full_run(paper_text=ptext)
    say("\n[SEC 13] THE MUTANT SWEEP, IN-PROCESS")
    sweep = []
    keep_lines = list(LINES)
    for name, gate, _what in MUTANTS:
        killed, where = run_mutant(name, ptext)
        sweep.append({"mutant": name, "target": gate, "killed": killed,
                      "died_at": where,
                      "on_target": bool(killed and where == gate)})
    del LINES[:]
    LINES.extend(keep_lines)
    for row in sweep:
        say("    %-24s -> %-30s %s"
            % (row["mutant"], row["died_at"],
               "ON TARGET" if row["on_target"] else "OFF TARGET"))
    R["mutant_sweep"] = sweep
    off = [r["mutant"] for r in sweep if not r["on_target"]]
    LD.gate("G-MUTANTS-ON-TARGET",
            "EVERY DECLARED MUTANT IS RUN IN-PROCESS AND DIES AT THE GATE IT "
            "NAMES.  %d mutants, each a real corruption of a measured value "
            "or of the object under test, each required to be killed BY ITS "
            "OWN NAMED GATE rather than by any gate that happens to fire "
            "first" % len(MUTANTS),
            not off, "mutants %d, off target %s" % (len(MUTANTS),
                                                    off or "none"))
    payload, text = finish(LD, SEAL, R, write=(mode != "--no-write"),
                           swept=True)
    print("\n[PAYLOAD] sha256-12 %s   gates %d   mutants %d   %s"
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
