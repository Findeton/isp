#!/usr/bin/env python3.13
# -*- coding: utf-8 -*-
"""
v14 PER-R -- THE R-LADDER PERSISTENCE CENSUS.
Instrument for `v14/paper-29-perr.md`.

QUESTION (pin `v14/note-perr-pin.md`, sha256-12 6339ba42f354, ledger #233).
Paper-21 closed the R = 4 arena with a price sequence that CLOSES -- for every
R >= 4 the cover binds, with slack 9(R - 3) -- and registered three falsifiable
predictions about the next budget, together with a saturation theorem to be
re-proved AS A SCHEMA rather than inherited.  This unit runs the R = 5 rung:

  STAGE 0  THE SIG FEED (computed first, stated separately).  The record-class
           structure at R = 5: the reachable site-code space, the covered
           codes split posdef / singular / indefinite, the COVERING-class code
           census exhaustive over all 280^5 ordered grouping quintuples, and
           the static reachability of I7's own G-SINGULAR and G-INDEF.
  STAGE 1  THE THREE PREDICTIONS, each PASS or FAIL with exact witnesses.
  STAGE 2  THE SLACK CENSUS: 9(R - 3) at R = 5, the binding constraint named,
           and what the slack buys measured against the two rungs below.
  STAGE 3  THE DICTIONARY ROW: the weld fibers along the ladder, R = 3, 4, 5
           and 6, on one instrument, with the R = 5 and R = 6 arenas DRIVEN
           through the committed grammar.
  STAGE 4  THE DIA ROW: which parallel classes are compulsory, at R = 4, 5, 6.

  NOT RUN: the interference census.  PER-L's #228 corollary closes it by
           theorem (LINK is Sidon at every L >= 3); it is cited, and a gate
           requires this run's own measurement surface to carry no
           interference reading.

WHAT THIS PROGRAM DOES
  SEC 1  PROVENANCE.  14 pinned sources, sha256-12 verified, products gated;
         the #62 verbatim anchors bound to their consumer gates; every text
         gate whitespace-normalises, ASCII-folds AND strips markdown prefixes.
  SEC 2  EXACT ARITHMETIC on Z_3^2; the 280 partitions; the parallel classes.
  SEC 3  THE COMMITTED GRAMMAR, DRIVEN DIRECTLY (d42b1 by text slice, d60/d66
         by AST extraction), anchored against d66's OWN COMMITTED OUTPUT ROWS
         at two budgets -- R = 4 (n = 66) and R = 6 (n = 102).
  SEC 4  THE PACKED COLUMNS and the declared driven window W5.
  SEC 5  STAGE 0.  SEC 6  STAGE 1.  SEC 7  STAGE 2.  SEC 8  STAGE 3.
  SEC 9  STAGE 4.  SEC 10  THE WALLS.
  SEC 11 The verdict, derived a second time from the serialized receipt by a
         comparator that types all four templates itself; the paper gates --
         claim rendering, table rendering, numeral coverage INCLUDING INLINE
         SPANS AND THE FENCED VERDICT BLOCKS (by multiset equality), and claim
         polarity; the TOTAL seal; the sweep-execution binding; the artifacts;
         the integrity check.

CLI CONTRACT (the #82 minimum: argv parsed against a whitelist)
---------------------------------------------------------------
    python3.13 v14/code/perr_exact.py
        THE DELIVERY RUN, and the ONLY writer.  Builds the whole census,
        evaluates every gate (the paper gates included), runs every declared
        mutant in-process, re-reads what it wrote and writes
        `perr_output.txt` and `perr_receipt.json` beside this file.
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
                    claim rendering, table rendering, numeral coverage and
                    claim POLARITY -- with PATH (this unit's paper by default)
                    as the object under test.  Exits 1 on drift, 0 on a clean
                    paper, 2 if PATH does not exist or is not a file.
    --list-gates / --list-mutants
                    print the registries and exit 0.

    Any other argument, any unknown flag argument, any missing flag argument,
    any SECOND MODE FLAG and any --verify-paper PATH that does not exist exits
    2.  No flag is mutant-only and no flag is a no-op: modes do not compose.

THE TOTAL GATE-TO-DISK SEAL (RUNBOOK 14 addendum, v14 #119 + the #148 totality
addendum).  EVERY published receipt key -- the measured layer AND the vouching
layer: schema, provenance, paper_claims, coverage, polarity, gates, totals and
the transcript head -- is either sealed at the moment its gate passes or listed
as DECLARED-UNSEALED in the manifest, and a gate compares the manifest against
the DECLARED key set rather than against the seals that happened to be taken.
The artifacts are written from the sealed payload through `os.replace`, and the
terminal integrity gate compares the BYTES ON DISK against the gate-time seal.

ARITHMETIC.  Exact only: `fractions.Fraction` and Python integers.  There are
no floats anywhere -- an AST scan of this file and a recursive type scan of the
emitted receipt are gates.

RUNTIME INPUTS (#46/#91).  Exactly 14 files are read at run time as SOURCES,
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
OUT_TXT = os.path.join(os.path.dirname(SELF), "perr_output.txt")
OUT_JSON = os.path.join(os.path.dirname(SELF), "perr_receipt.json")

SCHEMA = "isp/v14/r-ladder-persistence/1"
PAPER_REL = "v14/paper-29-perr.md"

# ===========================================================================
# SECTION 0.  THE FROZEN DECLARATION (RUNBOOK section 15: the arena is data)
# ===========================================================================

SOURCES = [
    ("A-PIN", "v14/note-perr-pin.md", "6339ba42f354",
     "THIS UNIT'S PIN (ledger #233): the three predictions, the slack census, "
     "the dictionary row, the SIG feed and the closed interference census."),
    ("A-P21", "v14/paper-21-r4dec.md", "ef4a8c35a0c4",
     "PAPER 21 (terminal, the nineteenth): the R = 4 arena -- the budget "
     "theorem, the ladder law, the RSQ zero-free-items theorem, the price "
     "sequence with its slack formula, block quantisation and the R = 6 "
     "door."),
    ("A-P21REC", "v14/code/r4dec_receipt.json", "a4538c7019e6",
     "PAPER 21's COMMITTED RECEIPT: the R = 4 numbers this unit compares "
     "against -- the reachable code counts, the covering class, its maximum "
     "cell count, the det spectrum, the weld fibers and the DIA row -- READ "
     "from these bytes, never re-typed."),
    ("A-P19", "v14/paper-19-r3-weld.md", "50bb81e67942",
     "PAPER 19 (terminal): the R = 3 arena, the rigidity theorem, the weld "
     "detector's two readings and the RSQ choice standard."),
    ("A-P19REC", "v14/code/r3_weld_receipt.json", "dfea664f2408",
     "PAPER 19's COMMITTED RECEIPT: the R = 3 row, read as data."),
    ("A-HA", "v13/paper-ha-successor.md", "f286ba10d2d9",
     "I7 / HA: the declared readout, the admissibility criterion, and "
     "requirement 3 -- the two-way rule this unit's controls discharge."),
    ("A-I7", "v13/code/ha_successor_receipt.json", "542b8735daf0",
     "I7's ARENA AS DATA: sites, links, THE ELEVEN DECLARED RECORDS whose "
     "committed box this unit walks, and the declared count lattice."),
    ("A-PERL", "v14/note-perl-adjudication.md", "08bec11d8466",
     "THE PER-L ADJUDICATION (#228): the corollary that closes the "
     "interference census on the R-ladder by theorem -- cited, not re-run."),
    ("A-D42B1", "v10/code/d42b1_transport_exact.py", "576275d55ecf",
     "THE COMMITTED TRANSPORT GRAMMAR, driven directly: this unit's only "
     "source of admissibility."),
    ("A-D60", "v10/code/d60_crystal_exact.py", "684cdb76552b",
     "D60: the Builder `B` and the delivery helper `dl`, AST-extracted."),
    ("A-D66", "v10/code/d66_arbitration_crystal_exact.py", "3d0516ab106e",
     "D66: CONFLICT-GRID(g, R) -- the committed constructor, AST-extracted "
     "and re-run at its own R = 4 and R = 6 points."),
    ("A-D66OUT", "v10/data/d66_arbitration_crystal_exact.out", "e252529d2586",
     "D66's COMMITTED OUTPUT: the GRID(g=3,R=4) and GRID(g=3,R=6) rows are "
     "READ from this file at run time and reproduced by driving."),
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


def lorentz_named(q11, q22, q12):
    """THE LORENTZIAN RESONANCE, required present in the paper.  The form is
    DERIVED from I7's own readout of the record this unit's own census
    returns, and typed NOWHERE."""
    return ("q = [[%s, %s], [%s, %s]]" % (q11, q12, q12, q22))


# ===========================================================================
# SECTION 1.  INFRASTRUCTURE
# ===========================================================================

class GateFail(Exception):
    pass


class CliError(Exception):
    pass


MUTANT = None
LINES = []


def say(s=""):
    LINES.append(s)
    print(s)


def mut(name):
    """a mutant switch: True exactly when the named mutant is active."""
    return MUTANT == name


def pick(name, normal, corrupted):
    """E-23: a falsifier corrupts an OBJECT.  Neither branch may be a bare
    boolean -- the corruption is a shadow object the gate then judges."""
    return corrupted if MUTANT == name else normal


class Ledger:
    def __init__(self):
        self.rows = []
        self.chain = hashlib.sha256(SCHEMA.encode()).hexdigest()

    def add(self, name, ok, statement, evidence, wall=False):
        self.chain = hashlib.sha256(
            (self.chain + name + str(bool(ok))).encode()).hexdigest()
        self.rows.append({"gate": name, "pass": bool(ok),
                          "statement": statement, "evidence": evidence,
                          "wall": bool(wall), "chain": self.chain[:12]})
        say("  [%s] %s" % ("PASS" if ok else "FAIL", name))
        say("         %s" % statement)
        say("         evidence: %s" % evidence)
        if not ok:
            raise GateFail(name)

    def names(self):
        return [r["gate"] for r in self.rows]


def digest(value):
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, default=str).encode()).hexdigest()


def jpath(obj, path):
    cur = obj
    for part in path.split("/"):
        if part == "":
            continue
        if isinstance(cur, list):
            cur = cur[int(part)]
        else:
            cur = cur[part]
    return cur


class Seal:
    """the gate-to-disk seal: a digest taken the moment a gate passes, the
    payload written from the sealed objects, integrity checked disk-vs-seal."""

    def __init__(self):
        self.seals = {}
        self.unsealed = []
        self.chain = hashlib.sha256(b"perr-seal").hexdigest()

    def take(self, key, value):
        d = digest(value)
        self.chain = hashlib.sha256((self.chain + key + d).encode()).hexdigest()
        self.seals[key] = d
        return value

    def declare_unsealed(self, key, reason):
        self.unsealed.append({"key": key, "reason": reason})

    def verify(self, payload):
        bad = []
        for key, d in self.seals.items():
            try:
                got = digest(jpath(payload, key))
            except Exception:
                bad.append(key)
                continue
            if got != d:
                bad.append(key)
        return bad


def read_bytes(rel):
    p = os.path.join(REPO, rel)
    with open(p, "rb") as fh:
        return fh.read()


READS = []
# the OBJECT-UNDER-TEST read happens in `main`, before the run's own register
# is cleared; it is carried across the clear so the provenance consumer gate
# sees the whole set of reads and not the sources alone.
OBJECT_READ = [None]


def read_text(path, category):
    """every read at run time records its CATEGORY, so the provenance gate
    holds all categories and not the pinned sources alone."""
    with open(path, "rb") as fh:
        b = fh.read()
    READS.append({"path": os.path.relpath(path, REPO), "category": category,
                  "sha256_12": hashlib.sha256(b).hexdigest()[:12]})
    return b.decode("utf-8")


FOLD = {"—": "-", "–": "-", "‘": "'", "’": "'",
        "“": '"', "”": '"', "≥": ">=", "≤": "<=",
        "≠": "!=", "≡": "=", "≢": "!=", "×": "x",
        "→": "->", "∈": "in", "⊆": "subset",
        "Σ": "sum", "∑": "sum", " ": " ", "…": "...",
        "′": "'", "·": ".", "−": "-"}


def ascii_fold(s):
    for k, v in FOLD.items():
        s = s.replace(k, v)
    return s


def mdstrip(s):
    """strip markdown LINE prefixes -- block quotes, list bullets, numbered
    list markers, heading hashes -- and inline emphasis/code marks."""
    out = []
    for line in s.split("\n"):
        t = line.lstrip()
        while t[:2] in ("> ", "- ", "* ", "+ ") or t[:1] == ">":
            t = t[2:] if t[:2] in ("> ", "- ", "* ", "+ ") else t[1:]
            t = t.lstrip()
        t = re.sub(r"^#{1,6}\s+", "", t)
        t = re.sub(r"^\d+\.\s+", "", t)
        out.append(t)
    s = "\n".join(out)
    return s.replace("**", "").replace("`", "").replace("*", "")


def norm(s):
    return re.sub(r"\s+", " ", ascii_fold(mdstrip(s))).strip()


def canon(s):
    return re.sub(r"\s+", "", ascii_fold(mdstrip(s)))


def match_needle(hay, needle):
    """#125: match text AS WRITTEN -- whitespace-normalised, ASCII-folded,
    markdown-prefix-stripped, and additionally compared whitespace-free so a
    needle broken by a line wrap inside a word matches too."""
    return norm(needle) in norm(hay) or canon(needle) in canon(hay)


# ===========================================================================
# SECTION 2.  EXACT ARITHMETIC ON Z_3^2
# ===========================================================================

L_MOD = 3
SITES = tuple((i, j) for i in range(L_MOD) for j in range(L_MOD))
SITE_INDEX = {s: i for i, s in enumerate(SITES)}
DIRECTIONS = ((1, 0), (0, 1), (1, 1), (1, 2))


def zadd(a, b):
    return ((a[0] + b[0]) % L_MOD, (a[1] + b[1]) % L_MOD)


def zmul(k, a):
    return ((k * a[0]) % L_MOD, (k * a[1]) % L_MOD)


def parallel_class(d):
    """the resolvable partition of AG(2,3) into the three lines of slope d."""
    H = frozenset({(0, 0), d, zmul(2, d)})
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

NUMWORDS = ("ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN",
            "EIGHT", "NINE", "TEN", "ELEVEN", "TWELVE", "THIRTEEN",
            "FOURTEEN", "FIFTEEN", "SIXTEEN", "SEVENTEEN", "EIGHTEEN",
            "NINETEEN", "TWENTY")
WORDNUM = dict({w.lower(): i for i, w in enumerate(NUMWORDS)},
               twice=2, thrice=3, thirty=30, forty=40, fifty=50, sixty=60,
               seventy=70, eighty=80, ninety=90, hundred=100, thousand=1000,
               million=1000000, billion=1000000000)


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


def canon_transversals(P):
    """THE DECLARED SEED MENU of a grouping: the k-th member of each group in
    the canonical order, k = 0, 1, 2.  Deterministic, no sampling."""
    return [tuple(g[k] for g in P) for k in range(3)]


def q_of(nvec):
    """I7's own readout: q11 = n_e1, q22 = n_e2, q12 = (n_diag - n_e1 - n_e2)/2."""
    n1, n2, n3 = nvec
    q12 = Fraction(n3 - n1 - n2, 2)
    return (Fraction(n1), Fraction(n2), q12,
            Fraction(n1) * Fraction(n2) - q12 * q12)


def admissible(nvec):
    """HA 3.2's own criterion: q nonsingular and positive definite at the
    site, by the exact Sylvester criterion."""
    q11, _q22, _q12, det = q_of(nvec)
    return q11 > 0 and det > 0


def det4(nvec):
    """4 * det, an integer, so every census runs in integers."""
    a, b, c = nvec
    return 4 * a * b - (c - a - b) ** 2


def sig_class(nvec):
    """the SIGNATURE CLASS of a covered site code, by its own Sylvester
    value: POSDEF, SINGULAR (the boundary) or INDEFINITE."""
    d = det4(nvec)
    if d > 0 and nvec[0] > 0:
        return "POSDEF"
    if d == 0:
        return "SINGULAR"
    return "INDEFINITE"


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


# I7's declared link order, DECLARED here and gated against I7's own receipt
# row cell by cell (G-I7-READOUT); nothing below runs if they differ.
I7_LINKS = ((1, 0), (0, 1), (1, 1))
CELLS = tuple((x, l) for x in SITES for l in I7_LINKS)
ROUNDS = 5
LADDER = (3, 4, 5, 6)


# ===========================================================================
# SECTION 3.  THE COMMITTED GRAMMAR, DRIVEN DIRECTLY
# ===========================================================================

def norm_src(s):
    return re.sub(r"\s+", " ", s).replace('"', "").replace("'", "").strip()


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

    def _extract(self, rel, texts, marker, extra):
        """d60/d66's committed extraction idiom: keep only defs and classes,
        so no module-level statement of theirs can run."""
        tree = ast.parse(texts[rel])
        keep = [n for n in tree.body
                if isinstance(n, (ast.FunctionDef, ast.ClassDef))]
        self.extracted[rel] = keep
        g = {"Fr": Fraction, "combinations": combinations, "Counter": Counter,
             "permutations": permutations, "product": product,
             "sys": sys, "ast": ast, "os": os}
        g.update(extra)
        exec(compile(ast.fix_missing_locations(
            ast.Module(body=keep, type_ignores=[])), marker, "exec"), g)
        return g


def actor(site):
    return "G%d%d" % site


ACTORS = tuple(actor(s) for s in SITES)
ACTOR_SITE = {actor(s): s for s in SITES}


def drive(G, schedule, supply=True, drop_supply=None, drop_arb=None,
          memo_off=False):
    """THE GENERALIZED SCHEDULE DRIVER, at any budget.  Exactly d66's
    CONFLICT-GRID(g, R) cycle -- conflict-supply deliveries from the group's
    seed, g proposals, one g-proposer arbitration won by the seed -- with the
    GROUPING AND THE SEED taken from the schedule.  Every event is specified
    by its FULL TUPLE and taken from the layer's own menu."""
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


def record_of(G, b):
    keep = set(ACTOR_SITE)
    divs = [e for e in b.H if e[0] == "r"]
    foot = [frozenset(r for r in G.regs_of(e) if r in keep) for e in divs]
    return {"events": len(b.H), "maxhits": b.maxhits, "refusal": b.refusal,
            "divisions": len(divs), "footprints": foot,
            "kinds": [e[0] for e in b.H]}


def driven(G, schedule):
    """cached: the record is a property of the schedule."""
    if schedule not in BUILD_CACHE:
        BUILD_CACHE[schedule] = record_of(G, drive(G, schedule))
    return BUILD_CACHE[schedule]


def link_field_of(footprints):
    """the DRIVEN link field: for a link l and a site x, the number of
    division events whose register footprint contains both x and x + l."""
    out = {}
    for x in SITES:
        for l in I7_LINKS:
            y = zadd(x, l)
            out[(x, l)] = sum(1 for f in footprints
                              if actor(x) in f and actor(y) in f)
    return out


# ===========================================================================
# SECTION 4.  THE PACKED COLUMNS
# ===========================================================================

def pack4(vec27):
    """the link field packed at FOUR bits per cell.  The largest count any
    budget in this unit can deposit at one cell is the budget itself, and
    every budget here is below sixteen, so no cell can carry."""
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
    RAW["sat"] = [i for i, v in enumerate(vecs) if sum(v) == len(CELLS) // 3]
    RAW["index"] = {P: i for i, P in enumerate(parts)}
    RAW["class_index"] = {k: RAW["index"][CLASSES[k]] for k in CLASS_NAMES}
    return RAW


CODE_TAB = {}
for _a in range(16):
    for _b in range(16):
        for _c in range(16):
            _d4 = 4 * _a * _b - (_c - _a - _b) ** 2
            CODE_TAB[_a | (_b << 4) | (_c << 8)] = (
                _d4,
                1 if (_a > 0 and _d4 > 0) else 0,
                1 if min(_a, _b, _c) >= 1 else 0)

FULLMASK = (1 << 27) - 1
POP12 = [bin(i).count("1") for i in range(1 << 12)]


def popc(m):
    n = 0
    while m:
        n += POP12[m & 0xFFF]
        m >>= 12
    return n


def site_trip(packed, k):
    return ((packed >> (12 * k)) & 0xF, (packed >> (12 * k + 4)) & 0xF,
            (packed >> (12 * k + 8)) & 0xF)


# ===========================================================================
# SECTION 5.  STAGE 0 -- THE SIG FEED
# ===========================================================================

def alphabet_census():
    """THE PER-ROUND SITE-CODE ALPHABET, measured at EVERY site (per-object,
    #87): which codes a single round can deposit at one site."""
    R = raw_census()
    per = {}
    for x in SITES:
        k = SITE_INDEX[x]
        per[x] = sorted({tuple(v[3 * k:3 * k + 3]) for v in R["vecs"]})
    alpha = sorted({c for x in SITES for c in per[x]})
    return alpha, per


CS_CACHE = {}
COV_CACHE = {}
WIT_CACHE = {}


def code_space(R, alpha):
    """the R-fold sumset of the alphabet: every site code the family can
    reach at budget R.  The rounds are independent at a fixed site, so the
    reachable set is exactly the sumset -- and the identity is BACK-VALIDATED
    against paper-21's committed counts at R = 3 and R = 4."""
    key = (R, tuple(sorted(alpha)))
    if key in CS_CACHE:
        return CS_CACHE[key]
    cur = {(0, 0, 0)}
    for _ in range(R):
        cur = {(c[0] + s[0], c[1] + s[1], c[2] + s[2])
               for c in cur for s in alpha}
    CS_CACHE[key] = cur
    return cur


def class_split(R, alpha):
    """the covered codes at budget R, split by their own Sylvester value."""
    cov = sorted(c for c in code_space(R, alpha) if min(c) >= 1)
    out = {"POSDEF": [], "SINGULAR": [], "INDEFINITE": []}
    for c in cov:
        out[sig_class(c)].append(c)
    return cov, out


LOCAL = {}


def local_buckets(site, link_index):
    """the partitions bucketed by their LOCAL TYPE at one site: which of the
    three declared partners share the site's conflict group.  The bucket key
    is the site's own per-round code."""
    key = (site, link_index)
    if key in LOCAL:
        return LOCAL[key]
    R = raw_census()
    k = SITE_INDEX[site]
    buckets = {}
    for i, v in enumerate(R["vecs"]):
        buckets.setdefault(tuple(v[3 * k:3 * k + 3]), []).append(i)
    bmask = {t: sorted({R["masks"][i] for i in v}) for t, v in buckets.items()}
    LOCAL[key] = (buckets, bmask)
    return LOCAL[key]


def type_multisets(target, R, alpha):
    """every multiset of R per-round site codes summing to the target."""
    out = []
    al = sorted(alpha)

    def rec(k, rem, acc, start):
        if k == R:
            if rem == (0, 0, 0):
                out.append(tuple(acc))
            return
        for j in range(start, len(al)):
            t = al[j]
            r2 = (rem[0] - t[0], rem[1] - t[1], rem[2] - t[2])
            if min(r2) < 0:
                continue
            rec(k + 1, r2, acc + [t], j)
    rec(0, target, [], 0)
    return out


def covering_with_code(target, R, alpha, site=(0, 0), want_witness=False,
                       live_only=False):
    """EXHAUSTIVE over all 280^R ordered grouping R-tuples: does any tuple
    COVER all 27 cells while carrying `target` as the site code at `site`?

    The quantifier is complete because a tuple's site code at `site` is the
    sum of its rounds' local types there, so every tuple with that code lies
    in exactly one type multiset; within a multiset the set of achievable
    unions is carried forward in full (deduplicated -- union is monotone, so
    dropping a duplicate drops no reachable union), and a partial union is
    dropped only when the cells it still has to cover outnumber what its
    remaining rounds can deposit."""
    key = (tuple(target), R, tuple(sorted(alpha)), site, want_witness,
           live_only)
    if key in COV_CACHE:
        return COV_CACHE[key]
    buck, bmask = local_buckets(site, 0)
    per_round = len(CELLS) // 3
    if live_only:
        RCl = raw_census()
        sat = set(RCl["sat"])
        bmask = {t: sorted({RCl["masks"][i] for i in v if i in sat})
                 for t, v in buck.items()}
    for types in type_multisets(target, R, alpha):
        cur = {0}
        for k, t in enumerate(types):
            left = R - k - 1
            nxt = set()
            for m in cur:
                for mm in bmask[t]:
                    n = m | mm
                    if popc(FULLMASK & ~n) <= per_round * left:
                        nxt.add(n)
            cur = nxt
            if not cur:
                break
        if FULLMASK in cur:
            out = ((True, witness_with_code(types, R, site)) if want_witness
                   else (True, None))
            COV_CACHE[key] = out
            return out
    COV_CACHE[key] = (False, None)
    return COV_CACHE[key]


def witness_with_code(types, R, site):
    """one explicit covering R-tuple with the given local types: the object
    the census's existence claim is about, exhibited round by round."""
    buckets, _bm = local_buckets(site, 0)
    RC = raw_census()
    per_round = len(CELLS) // 3
    found = []

    def dfs(k, chosen, m):
        if found:
            return
        if k == R:
            if m == FULLMASK:
                found.append(tuple(chosen))
            return
        if popc(FULLMASK & ~m) > per_round * (R - k):
            return
        for i in buckets[types[k]]:
            dfs(k + 1, chosen + [i], m | RC["masks"][i])
            if found:
                return
    dfs(0, [], 0)
    return found[0] if found else None


def maximal_masks(ms):
    """the ANTICHAIN of a set of unions: a union contained in another reaches
    no cell the larger one does not, and union is monotone, so dropping a
    dominated state drops no reachable completion.  Used only where the
    question is `is FULLMASK reachable` or `what is the largest union`, both
    of which are monotone in the state."""
    out = []
    for m in sorted(ms, key=lambda z: -popc(z)):
        if not any((m | o) == o for o in out):
            out.append(m)
    return out


CCC_CACHE = {}


def covering_class_codes(R, site=(0, 0)):
    """THE COVERING-CLASS CODE CENSUS BY ONE SHARED DP -- the route that
    reaches R = 6, where the per-code route does not.

    `covering_with_code` asks one code at a time and re-runs the union DP for
    every type multiset of that code.  This carries ALL codes forward at once:
    a state is a pair (partial site code, achievable union), the local type of
    each round advances both coordinates, and within one partial code the
    unions are reduced to their antichain.  The quantifier is the same one --
    every ordered R-tuple of groupings -- and the answer is BACK-VALIDATED
    against the per-code route at R = 3, 4 and 5."""
    key = (R, site)
    if key in CCC_CACHE:
        return CCC_CACHE[key]
    _buck, bmask = local_buckets(site, 0)
    per_round = len(CELLS) // 3
    cur = {(0, 0, 0): [0]}
    for k in range(R):
        left = R - k - 1
        nxt = {}
        for code, masks in cur.items():
            for t, tmasks in bmask.items():
                c2 = (code[0] + t[0], code[1] + t[1], code[2] + t[2])
                s = nxt.setdefault(c2, set())
                for m in masks:
                    for mm in tmasks:
                        n = m | mm
                        if popc(FULLMASK & ~n) <= per_round * left:
                            s.add(n)
        cur = {}
        for c2, s in nxt.items():
            keep = maximal_masks(s)
            if keep:
                cur[c2] = keep
    out = sorted(c for c, ms in cur.items() if FULLMASK in ms)
    CCC_CACHE[key] = out
    return out


BRIDGE_CACHE = {}


def posdef_with_a_zero_count(side):
    """every code of a box, walked for the one shape the `cover = posdef` row
    rests on being impossible: a POSITIVE-DEFINITE code carrying a zero
    count.  q11 = n1 forces n1 > 0, det > 0 forces n2 > 0, and with n3 = 0
    the integer 4.det is -(n1 - n2)^2, never positive -- so the list is
    expected empty, and it is walked rather than argued."""
    if side in BRIDGE_CACHE:
        return BRIDGE_CACHE[side]
    out = [(a, b, c) for a in range(side + 1) for b in range(side + 1)
           for c in range(side + 1)
           if min(a, b, c) == 0 and sig_class((a, b, c)) == "POSDEF"]
    BRIDGE_CACHE[side] = out
    return out


LIVE_CACHE = {}


def live_alphabet(site=(0, 0)):
    """THE PER-ROUND SITE-CODE ALPHABET OF A STRUCTURALLY LIVE ROUND: the
    codes a SATURATING partition can deposit at one site.  A live record's
    rounds all saturate, so this -- not the full alphabet -- is the letter
    set its site codes are summed from."""
    if site in LIVE_CACHE:
        return LIVE_CACHE[site]
    RC = raw_census()
    k = SITE_INDEX[site]
    sat = set(RC["sat"])
    out = sorted({tuple(RC["vecs"][i][3 * k:3 * k + 3]) for i in sat})
    LIVE_CACHE[site] = out
    return out


def live_code_space(R, live_alpha):
    """the R-fold sumset of the LIVE alphabet: every site code a bare-live
    record can carry, with no covering condition on it."""
    cur = {(0, 0, 0)}
    for _ in range(R):
        cur = {(c[0] + s[0], c[1] + s[1], c[2] + s[2])
               for c in cur for s in live_alpha}
    return cur


LW_CACHE = {}


def live_witness(target, R, site=(0, 0)):
    """one explicit STRUCTURALLY LIVE R-tuple -- every round saturating, so no
    foreign pair anywhere -- carrying `target` as its site code, exhibited
    round by round.  The object §3.7's licensed sentence is about."""
    RC = raw_census()
    k = SITE_INDEX[site]
    buckets = {}
    for i in RC["sat"]:
        buckets.setdefault(tuple(RC["vecs"][i][3 * k:3 * k + 3]), []).append(i)
    la = live_alphabet(site)
    found = []

    def rec(j, rem, acc):
        if found:
            return
        if j == R:
            if rem == (0, 0, 0):
                found.append(tuple(acc))
            return
        for t in la:
            r2 = (rem[0] - t[0], rem[1] - t[1], rem[2] - t[2])
            if min(r2) < 0:
                continue
            for i in buckets[t]:
                rec(j + 1, r2, acc + [i])
                if found:
                    return
    if (tuple(target), R, site) in LW_CACHE:
        return LW_CACHE[(tuple(target), R, site)]
    rec(0, tuple(target), [])
    LW_CACHE[(tuple(target), R, site)] = found[0] if found else None
    return LW_CACHE[(tuple(target), R, site)]


# ---------------------------------------------------------------------------
# THE REACHABILITY CLASSES, EACH AS ITS OWN PREDICATE PAIR (the #270 advisory
# given its binding gate).  A class here IS a pair of flags -- must the record
# COVER all 27 cells, must every one of its rounds SATURATE -- together with
# I7's declared list.  The WORDS the paper prints for a class are DERIVED from
# those flags by `class_label` and `class_predicate`, and every floor is
# computed by the single routine `floor_for` from the same flags, so the
# printed class and the computed class cannot come apart.  A class-word swap
# is then a claim about a predicate this file does not compute, and dies.
# ---------------------------------------------------------------------------

CLASS_FLAGS = (
    ("COVERED-SITE-CODE", False, False, False, "CHAIN"),
    ("COVERING-RECORD", True, False, False, "CHAIN"),
    ("BARE-LIVE-RECORD", False, True, False, "CONTROL"),
    ("STRUCTURALLY-LIVE-COVERING-RECORD", True, True, False, "CHAIN"),
    ("I7-DECLARED-RECORD", False, False, True, "CHAIN"),
)


def class_label(covering, live, declared):
    """the class's PRINTED WORDS, derived from the predicate its floor is
    computed with -- the table header, the §3.6 definition and the receipt
    row all read this one function."""
    if declared:
        return "I7-declared record"
    if covering and live:
        return "live and covering record"
    if covering:
        return "covering record"
    if live:
        return "bare-live record"
    return "covered site code"


def class_predicate(covering, live, declared):
    """the class's DEFINING CONDITION, in the same derived words."""
    if declared:
        return "is one of I7's own declared records"
    parts = []
    if covering:
        parts.append("covers all %d cells" % len(CELLS))
    if live:
        parts.append("carries no foreign pair, so every one of its rounds "
                     "saturates")
    if not parts:
        return ("has all %d declared links present, with no condition on the "
                "rest of the record" % len(I7_LINKS))
    return " and ".join(parts)


def floor_for(pol, covering, live, declared, alpha, live_alpha, fam, scan_to):
    """THE ONE FLOOR ROUTINE EVERY LADDER COLUMN IS COMPUTED BY.  The column
    is named by its flags and computed from them."""
    if declared:
        dec = [sum(v) for _nm, v in fam.items() if sig_class(tuple(v)) == pol]
        return min(dec) if dec else None
    for r in range(1, scan_to + 1):
        if live and not covering:
            if any(min(c) >= 1 and sig_class(c) == pol
                   for c in live_code_space(r, live_alpha)):
                return r
            continue
        cands = sorted(c for c in class_split(r, alpha)[1][pol])
        if not covering:
            if cands:
                return r
            continue
        if any(covering_with_code(c, r, alpha, live_only=live)[0]
               for c in cands):
            return r
    return None


LG_CACHE = {}


def locking_general(R):
    """THE LOCKING OBSTRUCTION'S GENERAL FORM, measured at every declared link
    and at every budget of the scan.  The counting mechanism is budget-free in
    its numerator -- a cell at count R locks two sites whose remaining cells
    demand seven distinct third members, and R rounds supply at most R -- so
    the obstruction is expected to dissolve at R = 7.  Here the union of R
    locked rounds is carried forward with NO completion prune, so the largest
    union it reaches is measured rather than only its success or failure."""
    if R in LG_CACHE:
        return LG_CACHE[R]
    RC = raw_census()
    rows = []
    for l in I7_LINKS:
        x = SITES[0]
        y = zadd(x, l)
        locked = [i for i, P in enumerate(RC["parts"])
                  if any(x in g and y in g for g in P)]
        masks = sorted({RC["masks"][i] for i in locked})
        cur = [0]
        for _k in range(R):
            nxt = set()
            for m in cur:
                for mm in masks:
                    nxt.add(m | mm)
            cur = maximal_masks(nxt)
        best = max(popc(m) for m in cur)
        rows.append({"link": str(l), "rounds_available": R,
                     "locked_partitions": len(locked),
                     "distinct_masks": len(masks),
                     "best_coverage": best,
                     "min_uncovered": len(CELLS) - best,
                     "covering_reachable": FULLMASK in cur})
    LG_CACHE[R] = rows
    return rows


def locking_census(R):
    """THE LOCKING THEOREM, measured.  A cell (x, l) carrying count R forces
    x and x + l into one conflict group in EVERY round.  This census asks --
    exhaustively, at every declared link -- whether the union of R such
    rounds can cover all 27 cells."""
    RC = raw_census()
    rows = []
    for li, l in enumerate(I7_LINKS):
        x = SITES[0]
        y = zadd(x, l)
        locked = [i for i, P in enumerate(RC["parts"])
                  if any(x in g and y in g for g in P)]
        masks = sorted({RC["masks"][i] for i in locked})
        cur = {0}
        for k in range(R):
            left = R - k - 1
            nxt = set()
            for m in cur:
                for mm in masks:
                    n = m | mm
                    if popc(FULLMASK & ~n) <= (len(CELLS) // 3) * left:
                        nxt.add(n)
            cur = nxt
        need = set()
        for (z, m) in CELLS:
            w = zadd(z, m)
            for (p1, p2) in ((z, w), (w, z)):
                if p1 == x and p2 != y:
                    need.add(p2)
                if p1 == y and p2 != x:
                    need.add(p2)
                if p2 == x and p1 != y:
                    need.add(p1)
                if p2 == y and p1 != x:
                    need.add(p1)
        rows.append({"link": str(l), "locked_partitions": len(locked),
                     "distinct_masks": len(masks),
                     "covering_reachable": FULLMASK in cur,
                     "third_members_required": len(need),
                     "rounds_available": R})
    return rows


def translation_invariance():
    """the nine chart translations act on the partitions and carry the cell
    masks with them: the site the local-type census is taken at is therefore
    any site.  Measured, not assumed."""
    RC = raw_census()
    idx = RC["index"]
    cellpos = {c: i for i, c in enumerate(CELLS)}
    ok = 0
    for t in SITES:
        for i, P in enumerate(RC["parts"]):
            Q = tuple(sorted(tuple(sorted(zadd(s, t) for s in g)) for g in P))
            j = idx[Q]
            want = 0
            for n, (x, l) in enumerate(CELLS):
                if RC["masks"][i] >> n & 1:
                    want |= 1 << cellpos[(zadd(x, t), l)]
            if RC["masks"][j] != want:
                return False, ok
            ok += 1
    return True, ok


# ===========================================================================
# SECTION 6/7.  THE SATURATING STRATUM AND THE SLACK
# ===========================================================================

STRATUM = {}


def stratum_sums(R):
    """the exact distribution of induced fields over the saturating stratum,
    36^R ordered grouping R-tuples, by convolution over distinct sums."""
    if R in STRATUM:
        return STRATUM[R]
    RC = raw_census()
    S = [RC["packed"][i] for i in RC["sat"]]
    D = Counter({0: 1})
    for _ in range(R):
        N = Counter()
        for m, c in D.items():
            for s in S:
                N[m + s] += c
        D = N
    STRATUM[R] = D
    return D


SC_CACHE = {}


def stratum_census(R):
    """the covering class inside the saturating stratum: its cardinality, its
    homogeneous records, its determinant spectrum, its positive-definite
    distribution, its maximum cell count and its site codes."""
    if R in SC_CACHE:
        return SC_CACHE[R]
    D = stratum_sums(R)
    ncov = 0
    homo = Counter()
    det = Counter()
    pos = Counter()
    maxcell = 0
    codes = set()
    cov_fields = 0
    for m, c in D.items():
        ts = [site_trip(m, k) for k in range(9)]
        npd = sum(1 for t in ts if CODE_TAB[t[0] | (t[1] << 4) | (t[2] << 8)][1])
        pos[npd] += c
        if all(min(t) >= 1 for t in ts):
            ncov += c
            cov_fields += 1
            for t in ts:
                det[det4(t)] += c
                codes.add(t)
                if max(t) > maxcell:
                    maxcell = max(t)
            if len(set(ts)) == 1:
                homo[ts[0]] += c
    SC_CACHE[R] = {"total": sum(D.values()), "cover": ncov, "homo": homo,
                   "det": det, "pos": pos, "maxcell": maxcell,
                   "codes": sorted(codes), "distinct_fields": len(D),
                   "cover_distinct_fields": cov_fields}
    return SC_CACHE[R]


STC_CACHE = {}


def stratum_target_count(target, R):
    """the exact number of ordered saturating R-tuples inducing a given
    HOMOGENEOUS record, by a convolution of two half-length censuses that
    never enumerates the R-tuples themselves."""
    if (tuple(target), R) in STC_CACHE:
        return STC_CACHE[(tuple(target), R)]
    half = R // 2
    A = stratum_sums(half)
    B = stratum_sums(R - half)
    T = pack4(tuple(target) * 9)
    n = 0
    for s, c in A.items():
        ok = True
        for k in range(27):
            if ((T >> (4 * k)) & 0xF) < ((s >> (4 * k)) & 0xF):
                ok = False
                break
        if not ok:
            continue
        n += c * B.get(T - s, 0)
    STC_CACHE[(tuple(target), R)] = n
    return n


def stratum_witnesses(target, R):
    """every ordered saturating R-tuple inducing a homogeneous target, listed
    -- the objects the DIA row quantifies over."""
    if (tuple(target), R) in WIT_CACHE:
        return WIT_CACHE[(tuple(target), R)]
    RC = raw_census()
    tgt = [target[i % 3] for i in range(27)]
    out = []

    def dfs(k, acc, cur):
        if k == R:
            if cur == tgt:
                out.append(tuple(acc))
            return
        for i in RC["sat"]:
            v = RC["vecs"][i]
            n = [cur[j] + v[j] for j in range(27)]
            if any(n[j] > tgt[j] for j in range(27)):
                continue
            dfs(k + 1, acc + [i], n)
    dfs(0, [], [0] * 27)
    WIT_CACHE[(tuple(target), R)] = out
    return out


# ===========================================================================
# SECTION 8.  WELD 2'S DETECTOR, CARRIED UNCHANGED
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
    target's Cayley incidence, by exhaustive backtracking.  No sampling and
    no cap.  THE DECLARED CRITERION IS THE UNDIRECTED ONE, on both branches,
    for weld 2's reason: a link is an unordered site pair carrying a label
    and a count, and orientation is a declared free item."""
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
    """THE QUOTIENT READING at a nine-object arena: a surjection of the
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
    """weld 2's induced count field s : X x L -> Z."""
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


def codivision_rel(footprints):
    """the co-division incidence on the ordered actor pair: a division event
    is ON the pair when its register footprint meets both endpoints."""
    rel = {}
    for u in ACTORS:
        for v in ACTORS:
            if u == v:
                continue
            rel[(u, v)] = sum(1 for f in footprints if u in f and v in f)
    return rel


def groupings_footprints(indices):
    """the co-division footprints of a grouping tuple: at this generator a
    division event's footprint IS its conflict group, which paper-21
    measured on its own seed fan rather than assumed."""
    RC = raw_census()
    return [frozenset(actor(s) for s in g)
            for i in indices for g in RC["parts"][i]]


DETECT_CACHE = {}


def detect(name, footprints, reading):
    """ONE CENSUS ROW of the weld detector.  Every fate is a MEASURED
    outcome with its number."""
    rel = codivision_rel(footprints)
    ckey = (tuple(sorted((str(k), v) for k, v in rel.items())), reading)
    if ckey in DETECT_CACHE:
        row = json.loads(json.dumps(DETECT_CACHE[ckey]))
        row["arena"] = name
        return row
    row = _detect(name, rel, reading)
    DETECT_CACHE[ckey] = json.loads(json.dumps(row, default=str))
    row = json.loads(json.dumps(DETECT_CACHE[ckey]))
    row["arena"] = name
    return row


def _detect(name, rel, reading):
    X, links, Lmod = list(SITES), list(I7_LINKS), L_MOD
    row = {"arena": name, "reading": reading, "site_gen": "ACTOR",
           "link_gen": "CO-DIVISION-ACTOR-PAIR",
           "count_gen": "DIVISION-COUNT-IN-THE-DECLARED-WINDOW"}
    objs = sorted(ACTORS)
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
    row["count_min"] = min(base_field.values())
    row["count_max"] = max(base_field.values())
    if row["count_min"] < 1:
        row["fate"] = "COUNT-DEAD"
        row["zero_cells"] = sum(1 for v in base_field.values() if v == 0)
        row["reason"] = ("n_l(x) must lie in Z_>0 (HA 3.1); the induced count "
                         "is 0 at %d of %d cells"
                         % (row["zero_cells"], len(base_field)))
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
    row["label_fiber_spread"] = sorted(lab_at)
    row["orient_fiber_spread"] = sorted(ori_at)
    row["fibers_base_map_invariant"] = (lab_at == {fib_label}
                                        and ori_at == {fib_orient})
    row["base_maps_read"] = len(maps)
    inv = {"I-SITE-ASSIGNMENT": fib_site, "I-DIRECTION-LABEL": fib_label,
           "I-ORIENT": fib_orient}
    row["inventory"] = inv
    free = sorted(k for k, v in inv.items() if v > 1)
    row["free_items"] = free
    row["fate"] = "FOUND" if not free else "UNMOTIVATED"
    row["reason"] = ("zero free items at the RSQ standard" if not free else
                     "%d genuinely free item(s): %s"
                     % (len(free), ", ".join("%s fiber %d" % (k, inv[k])
                                             for k in free)))
    seen = {}
    for i in range(len(maps)):
        f = fields[(i, tuple(range(nlab)), False)]
        seen[fkey(f)] = f
    recs = [tuple(sorted({tuple(f[(x, lk)] for lk in links) for x in X}))
            for f in seen.values()]
    row["assignment_fiber_records"] = len(seen)
    row["assignment_fiber_homogeneous"] = sorted(
        {r[0] for r in recs if len(r) == 1})
    row["assignment_fiber_all_admissible"] = all(
        admissible(c) for r in recs for c in r)
    row["induced_record_at_the_base_map"] = sorted(
        {tuple(base_field[(x, lk)] for lk in links) for x in X})
    return row


# ===========================================================================
# SECTION 9.  THE DECLARED DRIVEN WINDOW W5
# ===========================================================================

DIAG_SEED = ((0, 0), (1, 1), (2, 2))


def class_schedule(names):
    """a schedule built from parallel classes at the FIRST canonical
    transversal of each round."""
    return tuple((CLASSES[n], canon_transversals(CLASSES[n])[0])
                 for n in names)


def committed_schedule(R):
    """d66's OWN point at budget R: rounds alternating ROW and COLUMN on the
    diagonal seed, which is the committed constructor's own cycle."""
    return tuple((CLASSES["ROW" if k % 2 == 0 else "COL"], DIAG_SEED)
                 for k in range(R))


def class_names_for(record):
    """the collinear arrangement of a homogeneous record: the parallel class
    of each declared link taken as many times as the record counts it."""
    names = []
    for i, l in enumerate(I7_LINKS):
        nm = [k for k in CLASS_NAMES if CLASS_DIR[k] == l][0]
        names.extend([nm] * record[i])
    return tuple(names)


def window_schedules(records5):
    """THE DECLARED DRIVEN WINDOW W5, disclosed here and in the head.

    W4-ANCHOR:  d66's own R = 4 point -- the ONLY budget-4 member of the
                window, and the rung whose answer paper-21 committed.
    W5-LADDER:  the collinear arrangement of EVERY homogeneous record the
                R = 5 stratum reaches -- all six, none sampled.
    W5-SEEDFAN: the (1,1,3) arrangement at the 3 x 3 canonical transversal
                choices of its first two rounds -- the seed axis, declared.
                The fan enumerates NINE choices and contributes EIGHT
                schedules: the choice (0, 0) is the first canonical
                transversal at both rounds, which IS the W5-LADDER member of
                (1,1,3), so it is already counted there.  The collision is
                measured below rather than assumed.
    W5-CTRL:    d66's own R = 5 point.
    W6-DOOR:    the R = 6 rung -- the link-constant (2,2,2) concatenation and
                I7's own declared G-SINGULAR arrangement.
    W6-CTRL:    d66's own R = 6 point, whose committed output row this run
                reads from d66's pinned bytes.

    So the decomposition by parts is 1 + 6 + 8 + 1 + 2 + 1, over budgets
    4, 5 and 6 -- and the sum, the parts and the collision are all gated."""
    out, meta = [], {}

    def add(sch, tag):
        if sch not in meta:
            out.append(sch)
            meta[sch] = tag
            return True
        return False
    for rec in records5:
        add(class_schedule(class_names_for(rec)), "W5-LADDER")
    ladder_113 = class_schedule(class_names_for((1, 1, 3)))
    base = class_names_for((1, 1, 3))
    fan = {"choices": 0, "fresh": 0, "collided": [], "collides_with": None}
    for s0 in range(3):
        for s1 in range(3):
            T = tuple(CLASSES[n] for n in base)
            seeds = [canon_transversals(P)[0] for P in T]
            seeds[0] = canon_transversals(T[0])[s0]
            seeds[1] = canon_transversals(T[1])[s1]
            sch = tuple((T[k], seeds[k]) for k in range(len(T)))
            fan["choices"] += 1
            if add(sch, "W5-SEEDFAN"):
                fan["fresh"] += 1
            else:
                fan["collided"].append([s0, s1])
                if sch == ladder_113:
                    fan["collides_with"] = "W5-LADDER(1, 1, 3)"
    add(committed_schedule(5), "W5-CTRL")
    add(class_schedule(class_names_for((2, 2, 2))), "W6-DOOR")
    add(class_schedule(class_names_for((1, 1, 4))), "W6-DOOR")
    add(committed_schedule(6), "W6-CTRL")
    add(committed_schedule(4), "W4-ANCHOR")
    return out, meta, fan


DECLARED_DISPLACEMENTS = frozenset(
    [l for l in I7_LINKS] + [zmul(2, l) for l in I7_LINKS])


def foreign_pairs(indices):
    """the realised co-division pairs whose displacement I7 does not declare:
    exactly what STRUCT-DEAD means at this carrier."""
    RC = raw_census()
    n = 0
    for i in indices:
        for g in RC["parts"][i]:
            for (a, b) in combinations(sorted(g), 2):
                d = ((b[0] - a[0]) % L_MOD, (b[1] - a[1]) % L_MOD)
                if d not in DECLARED_DISPLACEMENTS:
                    n += 1
    return n


def field_of_schedule(sch):
    """the COMBINATORIAL link field of a schedule: the sum of its groupings'
    incidence vectors, computed without driving anything."""
    RC = raw_census()
    v = [0] * len(CELLS)
    for (P, _s) in sch:
        w = RC["vecs"][RC["index"][P]]
        for k in range(len(CELLS)):
            v[k] += w[k]
    return tuple(v)


# ===========================================================================
# SECTION 10.  THE #62 VERBATIM ANCHORS, BOUND TO THEIR CONSUMER GATES
# ===========================================================================

VERBATIM = [
    ("V01", "A-PIN", "THE THREE PREDICTIONS AT R=5 (falsifiable, from #211):",
     "G-PREDICTIONS"),
    ("V02", "A-PIN", "zero-free-items is IMPOSSIBLE at R=5 (5 != 0 mod 3",
     "G-PRED-B"),
    ("V23", "A-PIN", "NO declared I7 record has sum n = 5 (check the "
     "committed box)", "G-PRED-A"),
    ("V03", "A-PIN", "prove in-arena via the ladder law, not by citation",
     "G-PRED-B"),
    ("V04", "A-PIN", "the saturation SCHEMA's license re-proved at R=5, not "
     "assumed", "G-SATURATION-SCHEMA"),
    ("V05", "A-PIN", "G-SINGULAR and G-INDEF static reachability at R=5",
     "G-SIG-FEED"),
    ("V06", "A-PIN", "the interference census (PER-L's #228 corollary)",
     "G-INTERFERENCE-CLOSED"),
    ("V07", "A-P21", "is reachable by a structurally live schedule at exactly "
     "one budget, R = n_1 + n_2 + n_3", "G-LADDER"),
    ("V08", "A-P21", "zero free items holds exactly at the link-constant "
     "records, and I7 declares none of them", "G-PRED-B"),
    ("V09", "A-P21", "no round can deposit more than 9 link incidences",
     "G-SATURATION-SCHEMA"),
    ("V10", "A-P21", "so for every R >= 4 the cover binds, with slack "
     "9(R - 3)", "G-SLACK"),
    ("V11", "A-P21", "Across the whole covering class the maximum cell count "
     "is", "G-COVER-CODES"),
    ("V12", "A-P21", "whether the maximum cell count stays at 2 when the "
     "slack grows", "G-COVER-CODES"),
    ("V13", "A-P21", "the conflict-supply question re-asked two (resp. four) "
     "rounds wider", "G-DRIVEN-EQUALITY"),
    ("V14", "A-P21", "the full diagonal line-partition occurs in all 276 of "
     "the G-FLAT quadruples", "G-DIA-LAW"),
    ("V15", "A-P21", "the first budget above this one at which a live weld "
     "can be motivated at all is R = 6", "G-R6-DOOR"),
    ("V16", "A-P19", "the fibers computed as the number of distinct count "
     "fields each choice produces", "G-WELD-ROWS"),
    ("V17", "A-HA", "A predicate that cannot return its other value anywhere "
     "in the declared arena is not a measurement", "G-TWO-WAY"),
    ("V18", "A-HA", "A record is admissible when $q$ is nonsingular and "
     "positive definite at every site, by the exact Sylvester criterion",
     "G-I7-READOUT"),
    ("V19", "A-PERL", "LINK is Sidon at every L >= 3 - PER-R inherits this "
     "as a corollary, one census cancelled", "G-INTERFERENCE-CLOSED"),
    ("V20", "A-L1", "fourth form, outside paper 8's three, and its "
     "admissibility is v11's to argue when U4 runs", "G-WALL-L1"),
    ("V21", "A-CAT", "a Poisson sprinkling admits no Lorentz-invariant "
     "finite-valency graph", "G-WALL-BHS"),
    ("V22", "A-CAT", "a dimension reading without a height control is "
     "worthless", "G-WALL-KR"),
]

# the paper carries each verdict segment twice -- once in the head and once in
# the verdict section.  DECLARED here with its reason, and the multiset gate
# below binds the paper to exactly this count.
FENCE_COPIES = 2
FENCE_COPIES_REASON = ("each segment appears once in the head and once in the "
                       "verdict section; the multiset gate binds the count")

# THE COLUMNS BACK-VALIDATED AGAINST NUMBERS THIS UNIT DID NOT PRODUCE -- read
# from paper-21's committed receipt and from d66's committed output rather than
# re-typed.  §13's count is RENDERED from this list, never typed beside it.
BACK_VALIDATED = (
    "the reachable site-code counts at R = 3 and R = 4",
    "the covering-class row at R = 4 -- its code count, its maximum cell "
    "count and its determinant support",
    "the identity-breaking codes at R = 4",
    "the saturating stratum's covering class at R = 3 and its homogeneous "
    "records at R = 4",
    "the weld fibers and isomorphism count at R = 4",
    "the DIA row at R = 4",
    "the constructive lower bound at R = 6",
    "d66's own event profiles at R = 4 and R = 6",
)

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


def com(n):
    return "{:,}".format(n)


def mutant_hooks(src):
    """E-23: every falsifier's HOOK, located by AST, with the source of the
    statement carrying it, so a reader checks the declared corruption against
    the code rather than against a sentence about the code."""
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
                 and isinstance(node.args[2], ast.Constant)
                 and isinstance(node.args[2].value, bool))
        out.setdefault(node.args[0].value, []).append(
            {"kind": f.id, "line": node.lineno, "source": norm_src(text),
             "constant_boolean": const})
    return out


def template_constants(tree, name):
    """the TEMPLATE text a function types: its string constants less its
    docstring, less the receipt keys it looks values up by, and less the
    separators and format specs it calls methods on."""
    fns = [n for n in ast.walk(tree)
           if isinstance(n, ast.FunctionDef) and n.name == name]
    if not fns:
        return []
    fn = fns[0]
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
        if isinstance(n, ast.Compare):
            for a in [n.left] + list(n.comparators):
                if isinstance(a, ast.Constant):
                    skip.add(id(a))
    return [n.value for n in ast.walk(fn)
            if isinstance(n, ast.Constant) and isinstance(n.value, str)
            and id(n) not in skip and n.value != doc]


VERDICT_NAMES = (
    ("I7", "the parent unit's name (HA's I7), not a count"),
    ("PAPER-21", "the parent paper's number, a name"),
    ("PER-L", "the sibling unit's name"),
    ("G-SINGULAR", "one of I7's eleven declared records, a name"),
    ("G-INDEF", "one of I7's eleven declared records, a name"),
    ("G-FLAT", "one of I7's eleven declared records, a name"),
    ("AG(2,3)", "the committed affine plane's name"),
    ("Z_3^2", "the site lattice's name"),
    ("d66", "the committed constructor's name"),
    ("4det", "this instrument's own name for four times the determinant, "
             "the integer the census carries"),
    ("q12", "I7's own name for the off-diagonal entry of its readout"),
    ("ZERO-FREE-ITEMS", "the RSQ standard's own name for MOTIVATED, quoted "
                        "from paper-19 rather than recomputed"),
)


# ===========================================================================
# SECTION 11.  THE RUN
# ===========================================================================

def full_run(break_anchor=None, paper_text=None, paper_rel=PAPER_REL,
             do_paper=True, write=False, swept=False):
    LD = Ledger()
    SEAL = Seal()
    R = {"schema": SCHEMA, "unit": "perr", "python": "3.13",
         "pin": "v14/note-perr-pin.md@6339ba42f354"}
    NUMREG.clear()
    READS.clear()
    if OBJECT_READ[0] is not None:
        READS.append(dict(OBJECT_READ[0]))

    # ---- SEC 1  PROVENANCE ----------------------------------------------
    say("[SEC 1] PROVENANCE")
    texts, provrows = {}, []
    for sid, rel, sha, why in SOURCES:
        # a source that is not there is a PROVENANCE FAILURE with a name, not
        # a traceback: a bare copy of this file must abort at G-SOURCES.
        try:
            t = read_text(os.path.join(REPO, rel), "SOURCE")
        except OSError:
            provrows.append({"id": sid, "path": rel, "declared": sha,
                             "measured": "ABSENT", "match": False,
                             "why": why})
            continue
        got = hashlib.sha256(t.encode("utf-8")).hexdigest()[:12]
        want = sha if break_anchor != sid else ("0" * 12)
        texts[rel] = t
        provrows.append({"id": sid, "path": rel, "declared": want,
                         "measured": got, "match": got == want, "why": why})
    bad = [p for p in provrows if not p["match"]]
    absent = [p["path"] for p in provrows if p["measured"] == "ABSENT"]
    R["provenance"] = SEAL.take("provenance",
                                {"sources": provrows, "count": len(provrows)})
    LD.add("G-SOURCES",
           not bad and len(provrows) == len(SOURCES),
           "EVERY SOURCE IS READ AT ITS PINNED SHA.  The %d declared sources "
           "are read at run time and each file's measured sha256-12 equals "
           "the digest this unit froze; a single mismatch stops the run "
           "before any census is built, and a source that is ABSENT -- a bare "
           "copy of this file with no repository under it -- fails here by "
           "name rather than by traceback" % len(SOURCES),
           "sources %d, mismatches %d, absent %s"
           % (len(provrows), len(bad), absent))

    anchors = []
    for vid, sid, needle, gate in VERBATIM:
        rel = [s[1] for s in SOURCES if s[0] == sid][0]
        hay = texts[rel]
        hit = match_needle(hay, pick("M-ANCHOR", needle, needle + " XX"))
        anchors.append({"id": vid, "source": sid, "gate": gate,
                        "chars": len(needle), "found": hit})
    R["anchors"] = SEAL.take("anchors", anchors)
    floor = min(a["chars"] for a in anchors)
    LD.add("G-ANCHORS",
           all(a["found"] for a in anchors) and floor >= 40,
           "EVERY VERBATIM ANCHOR IS PRESENT IN ITS OWN SOURCE AND NAMES THE "
           "GATE THAT CONSUMES IT.  Each needle is matched "
           "whitespace-normalised, ASCII-folded and markdown-stripped, and "
           "each clears a length floor, so no anchor is a fragment that "
           "could match by accident",
           "anchors %d, found %d, shortest %d chars"
           % (len(anchors), sum(1 for a in anchors if a["found"]), floor))

    # ---- I7's ARENA, AS DATA --------------------------------------------
    i7 = json.loads(texts["v13/code/ha_successor_receipt.json"])
    D7 = i7["declarations"]
    links7 = pick("M-I7-LINKS", [tuple(v) for v in D7["links_d2"]],
                  [tuple(v) for v in reversed(D7["links_d2"])])
    fam = {nm: tuple(D7["records_d2"][nm]) for nm in sorted(D7["records_d2"])}
    inhom = list(D7["records_d2_inhomogeneous"])
    box = D7["count_lattice"]
    pts = i7_box_admissible(box)
    link_match = [tuple(l) == tuple(I7_LINKS[k]) for k, l in enumerate(links7)]
    declared_total = len(fam) + len(inhom)
    R["i7"] = SEAL.take("i7", {
        "links": [list(l) for l in links7], "record_family": fam,
        "site_dependent": inhom, "declared_records": declared_total,
        "box": box, "admissible_box_points": len(pts),
        "L": D7["L"], "d": D7["d"]})
    LD.add("G-I7-READOUT",
           all(link_match) and len(links7) == len(I7_LINKS)
           and declared_total == len(fam) + len(inhom)
           and all(admissible(v) or det4(v) <= 0 for v in fam.values()),
           "I7'S ARENA IS READ AS DATA, LINK BY LINK.  The three declared "
           "links are compared coordinate by coordinate against the order "
           "this unit uses, the declared record family and the two "
           "site-dependent records are read from I7's own receipt, and the "
           "admissible points of its declared count box are RECOMPUTED here "
           "by its own Sylvester criterion rather than re-typed",
           "links matched %d of %d, declared records %d (%d homogeneous + %d "
           "site-dependent), admissible box points %d"
           % (sum(1 for m in link_match if m), len(links7), declared_total,
              len(fam), len(inhom), len(pts)))
    reg(len(pts), declared_total, len(fam), len(inhom))

    # paper-21's committed receipt, read as data
    p21 = json.loads(texts["v14/code/r4dec_receipt.json"])
    P21 = p21["price"]
    p19 = json.loads(texts["v14/code/r3_weld_receipt.json"])

    # ---- SEC 2  THE ARENA ------------------------------------------------
    say("")
    say("[SEC 2] THE ARENA, DECLARED AS DATA")
    RC = raw_census()
    nparts = len(RC["parts"])
    closed = 1
    for k in range(1, 10):
        closed *= k
    closed = pick("M-ARENA", closed // ((6 ** 3) * 6),
                  closed // ((6 ** 3) * 6) + 1)
    spec = Counter(RC["incidences"])
    per_round = max(spec)
    nsat = len(RC["sat"])
    R["arena"] = SEAL.take("arena", {
        "sites": len(SITES), "cells": len(CELLS), "partitions": nparts,
        "partitions_closed_form": closed,
        "incidence_spectrum": {str(k): v for k, v in sorted(spec.items())},
        "max_incidences_per_round": per_round, "saturating": nsat,
        "budget": ROUNDS, "family": nparts ** ROUNDS,
        "saturating_family": nsat ** ROUNDS})
    LD.add("G-ARENA",
           nparts == closed and per_round == len(CELLS) // 3
           and nsat == spec[per_round]
           and all(sum(v) == RC["incidences"][i]
                   for i, v in enumerate(RC["vecs"])),
           "THE ROUND'S OBJECT SPACE, COUNTED TWICE AND PROFILED PER OBJECT.  "
           "Exhaustive enumeration of the partitions of the nine sites into "
           "three triples and the closed form 9!/(3!^3 . 3!) agree, every "
           "partition's incidence count is recomputed from its own 27-vector, "
           "and the saturating stratum is exactly the top of the spectrum",
           "partitions %d = %d (closed form), spectrum %s, saturating %d, "
           "family %s" % (nparts, closed,
                          dict(sorted(spec.items())), nsat,
                          com(nparts ** ROUNDS)))
    reg(nparts, nsat, per_round, len(CELLS), nparts ** ROUNDS)
    for k, v in spec.items():
        reg(k, v)

    ok_tr, tr_checks = translation_invariance()
    R["translation"] = SEAL.take("translation",
                                 {"invariant": ok_tr, "checks": tr_checks})
    LD.add("G-TRANSLATION",
           ok_tr and tr_checks == len(SITES) * nparts,
           "THE SITE THE LOCAL-TYPE CENSUS IS TAKEN AT IS ANY SITE.  Each of "
           "the nine chart translations is applied to each of the 280 "
           "partitions and the translate's own cell mask is compared against "
           "the image of the original's mask cell by cell, so the census "
           "below quantifies at one site and speaks about all nine",
           "translation-partition pairs checked %d, mismatches 0"
           % tr_checks)
    reg(tr_checks)

    # ---- SEC 3  STAGE 0 -- THE SIG FEED ---------------------------------
    say("")
    say("[SEC 3] STAGE 0 -- THE SIG FEED (the reachability census)")
    alpha, per_site_alpha = alphabet_census()
    alpha = pick("M-ALPHABET", alpha, alpha[:-1])
    same_at_every_site = all(sorted(per_site_alpha[x]) == sorted(alpha)
                             for x in SITES)
    R["alphabet"] = SEAL.take("alphabet", {
        "codes": [list(c) for c in alpha], "size": len(alpha),
        "same_at_every_site": same_at_every_site,
        "max_popcount": max(sum(c) for c in alpha)})
    LD.add("G-ALPHABET",
           same_at_every_site and len(alpha) == 2 ** len(I7_LINKS) - 1
           and max(sum(c) for c in alpha) == len(I7_LINKS) - 1,
           "THE PER-ROUND SITE-CODE ALPHABET, MEASURED AT EVERY SITE.  A "
           "conflict group holds three sites, so one round can co-group a "
           "site with at most two of its three declared partners: the "
           "alphabet is every 0/1 code of weight at most two, and the same "
           "alphabet is realised at each of the nine sites separately",
           "alphabet %d codes, maximum weight %d, realised identically at %d "
           "of %d sites" % (len(alpha), max(sum(c) for c in alpha),
                            sum(1 for x in SITES
                                if sorted(per_site_alpha[x]) == sorted(alpha)),
                            len(SITES)))
    reg(len(alpha))

    cs = {}
    for r in LADDER + (2,):
        cs[r] = code_space(r, alpha)
    cs[4] = pick("M-CODESPACE", cs[4], cs[4] | {(len(SITES),) * 3})
    back54 = P21["reachable_site_codes_r3"]
    back105 = P21["reachable_site_codes_r4"]
    R["code_space"] = SEAL.take("code_space", {
        str(r): len(cs[r]) for r in sorted(cs)})
    LD.add("G-CODESPACE",
           len(cs[3]) == back54 and len(cs[4]) == back105,
           "THE REACHABLE SITE-CODE SPACE IS THE SUMSET, AND THE IDENTITY IS "
           "BACK-VALIDATED AT TWO COMMITTED BUDGETS.  The rounds are "
           "independent at a fixed site, so the codes a budget reaches are "
           "the R-fold sumset of the alphabet; run at R = 3 and R = 4 it "
           "returns paper-21's own committed counts, read from that unit's "
           "receipt rather than re-typed here",
           "R=3 %d against paper-21's committed %d; R=4 %d against %d; "
           "R=5 %d; R=6 %d" % (len(cs[3]), back54, len(cs[4]), back105,
                               len(cs[5]), len(cs[6])))
    reg(*[len(cs[r]) for r in cs])

    split = {}
    for r in LADDER:
        cov, sp = class_split(r, alpha)
        sp = pick("M-CLASS", sp,
                  {"POSDEF": sp["POSDEF"] + sp["SINGULAR"], "SINGULAR": [],
                   "INDEFINITE": sp["INDEFINITE"]}) if r == ROUNDS else sp
        split[r] = {"covered": cov, "classes": sp}
    p21_break = [tuple(c) for c in P21["identity_breaking_codes"]]
    r4sing = split[4]["classes"]["SINGULAR"]
    r5 = split[ROUNDS]["classes"]
    consistent = all(sig_class(c) == k for k in r5 for c in r5[k])
    R["class_split"] = SEAL.take("class_split", {
        str(r): {"covered": len(split[r]["covered"]),
                 "posdef": len(split[r]["classes"]["POSDEF"]),
                 "singular": len(split[r]["classes"]["SINGULAR"]),
                 "indefinite": len(split[r]["classes"]["INDEFINITE"]),
                 "singular_codes": [list(c) for c in
                                    split[r]["classes"]["SINGULAR"]],
                 "indefinite_codes": [list(c) for c in
                                      split[r]["classes"]["INDEFINITE"]]}
        for r in LADDER})
    LD.add("G-CLASS-SPLIT",
           consistent and sorted(r4sing) == sorted(p21_break)
           and not split[4]["classes"]["INDEFINITE"]
           and len(r5["INDEFINITE"]) > 0,
           "THE COVERED CODES, SPLIT BY THEIR OWN SYLVESTER VALUE, AND THE "
           "BUDGET AT WHICH THE INDEFINITE REGION OPENS.  Every covered code "
           "is classified against its own 4.det rather than against an "
           "aggregate; at R = 4 the non-positive-definite covered codes are "
           "exactly paper-21's three identity-breaking codes and NONE is "
           "indefinite, and at R = 5 the indefinite region is non-empty for "
           "the first time",
           "R=4 covered %d = %d posdef + %d singular + %d indefinite "
           "(paper-21's committed breaking codes %s); R=5 covered %d = %d + "
           "%d + %d, indefinite %s at 4det %s"
           % (len(split[4]["covered"]), len(split[4]["classes"]["POSDEF"]),
              len(split[4]["classes"]["SINGULAR"]),
              len(split[4]["classes"]["INDEFINITE"]),
              [list(c) for c in p21_break], len(split[ROUNDS]["covered"]),
              len(r5["POSDEF"]), len(r5["SINGULAR"]), len(r5["INDEFINITE"]),
              [list(c) for c in r5["INDEFINITE"]],
              sorted({det4(c) for c in r5["INDEFINITE"]})))
    for r in LADDER:
        reg(len(split[r]["covered"]), len(split[r]["classes"]["POSDEF"]),
            len(split[r]["classes"]["SINGULAR"]),
            len(split[r]["classes"]["INDEFINITE"]))
    reg(*[det4(c) for c in r5["INDEFINITE"]])

    lock = locking_census(ROUNDS)
    lock = pick("M-LOCKING", lock,
                [dict(row, covering_reachable=True) for row in lock])
    R["locking"] = SEAL.take("locking", {"rows": lock, "budget": ROUNDS})
    LD.add("G-LOCKING",
           not any(row["covering_reachable"] for row in lock)
           and all(row["locked_partitions"] > 0 for row in lock)
           and all(row["third_members_required"] > row["rounds_available"]
                   for row in lock),
           "THE LOCKING THEOREM, MEASURED AT EVERY DECLARED LINK.  A cell "
           "carrying count R forces its two sites into one conflict group in "
           "every round, and the union of five such rounds is searched "
           "exhaustively: at each of the three declared links the union NEVER "
           "reaches all 27 cells, so no covering quintuple carries a cell "
           "count of 5 -- and the maximum a five-round lock can cover is "
           "measured rather than asserted",
           "; ".join("link %s: %d locked partitions, %d distinct masks, "
                     "covering reachable %s, distinct third members required "
                     "%d against %d rounds"
                     % (row["link"], row["locked_partitions"],
                        row["distinct_masks"], row["covering_reachable"],
                        row["third_members_required"], row["rounds_available"])
                     for row in lock))
    reg(*[row["third_members_required"] for row in lock])
    reg(*[row["locked_partitions"] for row in lock])

    occ = {}
    for r in (3, 4, ROUNDS):
        hits = []
        for c in split[r]["covered"] if r in split else \
                sorted(x for x in cs[r] if min(x) >= 1):
            ok, _w = covering_with_code(c, r, alpha)
            if ok:
                hits.append(c)
        occ[r] = hits
    occ[ROUNDS] = pick("M-COVER-CODES", occ[ROUNDS],
                       [c for c in occ[ROUNDS] if sig_class(c) == "POSDEF"])
    occ[4] = pick("M-COVER-R4", occ[4], occ[4] + [(1, 1, 4)])
    occ4_max = max(max(c) for c in occ[4])
    occ4_det = sorted({det4(c) for c in occ[4]})
    p21_det = sorted(int(k) for k in P21["det_spectrum_4det"])
    occ5 = occ[ROUNDS]
    occ5_max = max(max(c) for c in occ5)
    occ5_det = sorted({det4(c) for c in occ5})
    occ5_bad = [c for c in occ5 if sig_class(c) != "POSDEF"]
    R["covering_codes"] = SEAL.take("covering_codes", {
        str(r): {"codes": [list(c) for c in occ[r]], "count": len(occ[r]),
                 "max_cell": max(max(c) for c in occ[r]),
                 "det4_support": sorted({det4(c) for c in occ[r]}),
                 "non_posdef": [list(c) for c in occ[r]
                                if sig_class(c) != "POSDEF"]}
        for r in occ})
    LD.add("G-COVER-CODES",
           len(occ[4]) == P21["covering_class_site_codes"]
           and occ4_max == P21["covering_class_max_cell_count"]
           and occ4_det == p21_det and len(occ[3]) == 1
           and occ5_max > occ4_max,
           "THE COVERING-CLASS CODE CENSUS, EXHAUSTIVE OVER THE WHOLE FAMILY "
           "AND BACK-VALIDATED ONE ROUND DOWN.  For every covered code the "
           "census asks whether ANY ordered R-tuple of groupings both covers "
           "all 27 cells and carries that code at a site, quantifying over "
           "all 280^R tuples by local type; run at R = 4 it returns "
           "paper-21's committed covering-class row -- its code count, its "
           "maximum cell count and its determinant support -- and at R = 5 "
           "the maximum cell count has RISEN, so block quantisation does not "
           "survive the slack",
           "R=3 %d code; R=4 %d codes (paper-21's committed %d), max cell %d "
           "(committed %d), 4det support %s (committed %s); R=5 %d codes, "
           "max cell %d, 4det support %s, non-posdef %s"
           % (len(occ[3]), len(occ[4]), P21["covering_class_site_codes"],
              occ4_max, P21["covering_class_max_cell_count"], occ4_det,
              p21_det, len(occ5), occ5_max, occ5_det,
              [list(c) for c in occ5_bad]))
    reg(len(occ[3]), len(occ[4]), len(occ5), occ4_max, occ5_max)
    reg(*occ5_det)

    wit_code = sorted(occ5_bad)[0] if occ5_bad else None
    witness = None
    if wit_code is not None:
        _ok, widx = covering_with_code(wit_code, ROUNDS, alpha,
                                       want_witness=True)
        fld = [0] * len(CELLS)
        for i in widx:
            for k in range(len(CELLS)):
                fld[k] += RC["vecs"][i][k]
        fld = pick("M-WITNESS", fld, [c + 1 for c in fld])
        codes_at = [tuple(fld[3 * k:3 * k + 3]) for k in range(len(SITES))]
        witness = {
            "code": list(wit_code), "rounds": [list(map(list, RC["parts"][i]))
                                               for i in widx],
            "round_incidences": [RC["incidences"][i] for i in widx],
            "saturating_rounds": sum(1 for i in widx
                                     if RC["incidences"][i] == per_round),
            "site_codes": [list(c) for c in codes_at],
            "covering": all(c >= 1 for c in fld),
            "total_incidences": sum(fld), "max_cell": max(fld),
            "non_posdef_sites": [list(c) for c in codes_at
                                 if sig_class(c) != "POSDEF"],
            "det4_at_the_singular_site": det4(wit_code)}
    R["singular_witness"] = SEAL.take("singular_witness", witness)
    declared_by_code = [nm for nm, v in fam.items() if tuple(v) == wit_code]
    LD.add("G-SINGULAR-WITNESS",
           witness is not None and wit_code is not None
           and witness["covering"]
           and tuple(witness["site_codes"][0]) == wit_code
           and witness["det4_at_the_singular_site"] == 0
           and len(witness["non_posdef_sites"]) == 1
           and witness["saturating_rounds"] < ROUNDS,
           "THE COVERING QUINTUPLE THAT LEAVES THE POSITIVE-DEFINITE CLASS, "
           "EXHIBITED ROUND BY ROUND.  Its five groupings are listed, its "
           "field is summed cell by cell, every one of its nine sites is "
           "classified against its own Sylvester value, and exactly one site "
           "is singular -- carrying I7's own declared G-SINGULAR count "
           "vector.  It is not a saturating quintuple, which is why the "
           "stratum census below cannot see it",
           "code %s = %s, 4det %s, covering %s, total incidences %s, max "
           "cell %s, saturating rounds %s of %d, non-posdef sites %s of %d"
           % (list(wit_code) if wit_code else None,
              declared_by_code or "undeclared",
              (witness or {}).get("det4_at_the_singular_site"),
              (witness or {}).get("covering"),
              (witness or {}).get("total_incidences"),
              (witness or {}).get("max_cell"),
              (witness or {}).get("saturating_rounds"), ROUNDS,
              len((witness or {}).get("non_posdef_sites") or []), len(SITES)))
    reg((witness or {}).get("total_incidences"),
        (witness or {}).get("max_cell"),
        (witness or {}).get("saturating_rounds"))

    floors = {}
    for nm, v in sorted(fam.items()):
        floors[nm] = {"record": list(v), "budget": sum(v),
                      "class": sig_class(tuple(v)),
                      "reachable_as_a_site_code_from":
                          min(r for r in range(1, sum(v) + 1)
                              if tuple(v) in code_space(r, alpha))}
    # THE CLASS-EXPLICIT REACHABILITY LADDER.  Every column is a PREDICATE
    # PAIR (must it cover, must every round saturate) plus I7's declared list;
    # every floor is computed by `floor_for` FROM those flags, and every word
    # the paper prints for the column is derived from the same flags by
    # `class_label` / `class_predicate`.  The four CHAIN columns are
    # cumulative; BARE-LIVE is a CONTROL -- the live condition with the
    # covering condition dropped -- and it is what makes the substitution
    # visible: its floors are two rungs below the live-and-covering ones.
    scan_to = ROUNDS + 3
    live_alpha = live_alphabet()
    ladder_classes = []
    for pol in ("SINGULAR", "INDEFINITE"):
        row = {"polarity": pol, "scanned_to": scan_to}
        for key, cov, liv, dec, kind in CLASS_FLAGS:
            row[key] = floor_for(pol, cov, liv, dec, alpha, live_alpha, fam,
                                 scan_to)
        row["declared_names"] = sorted(nm for nm, v in fam.items()
                                       if sig_class(tuple(v)) == pol)
        ladder_classes.append(row)
    ladder_classes = pick("M-CLASS-LADDER", ladder_classes,
                          [dict(r0, **{"COVERING-RECORD":
                                       r0["COVERED-SITE-CODE"]})
                           for r0 in ladder_classes])
    # the printed words of each class, DERIVED from the flags its floor was
    # computed with -- swapping two of them in the paper is a claim about a
    # predicate this file does not compute
    class_rows = [{"class": key, "label": class_label(cov, liv, dec),
                   "predicate": class_predicate(cov, liv, dec),
                   "covering_required": cov, "every_round_saturating": liv,
                   "declared_list": dec, "kind": kind}
                  for key, cov, liv, dec, kind in CLASS_FLAGS]
    class_rows = pick("M-CLASS-WORDS", class_rows,
                      [dict(c, label=class_label(c["every_round_saturating"],
                                                 c["covering_required"],
                                                 c["declared_list"]))
                       for c in class_rows])
    chain = [k for k, _c, _l, _d, kind in CLASS_FLAGS if kind == "CHAIN"]
    R["reachability_ladder"] = SEAL.take("reachability_ladder", {
        "rows": ladder_classes, "classes": [k[0] for k in CLASS_FLAGS],
        "chain": chain, "class_rows": class_rows,
        "note": "every reachability row names the class it is about and every "
                "floor is computed from that class's own predicate flags; a "
                "floor for one class is not a floor for another"})
    nest_chain = all(
        r0[chain[i]] <= r0[chain[i + 1]]
        for r0 in ladder_classes for i in range(len(chain) - 1))
    nest_ctrl = all(r0["COVERED-SITE-CODE"] <= r0["BARE-LIVE-RECORD"]
                    <= r0["STRUCTURALLY-LIVE-COVERING-RECORD"]
                    for r0 in ladder_classes)
    LD.add("G-CLASS-LADDER",
           all(r0[k] is not None for r0 in ladder_classes
               for k, _c, _l, _d, _kd in CLASS_FLAGS)
           and nest_chain and nest_ctrl
           and [r0["COVERING-RECORD"] for r0 in ladder_classes
                if r0["polarity"] == "INDEFINITE"][0] > ROUNDS,
           "THE REACHABILITY LADDER IS CLASS-EXPLICIT, AND THE CLASSES DO NOT "
           "SHARE A FLOOR.  A determinant sign is reachable at a different "
           "budget in each of the four cumulative classes -- a covered site "
           "code, a record covering all 27 cells, a live AND covering record, "
           "or one of I7's own declared records -- and each floor is computed "
           "separately from its own predicate, with the nesting checked "
           "rather than assumed.  The BARE-LIVE control carries the live "
           "condition WITHOUT the covering condition, and it is checked to "
           "sit between the covered and the live-and-covering floors",
           "; ".join("%s: %s (control bare-live %s), declared %s"
                     % (r0["polarity"],
                        ", ".join("%s %s" % (class_label(c, l, d), r0[k])
                                  for k, c, l, d, kd in CLASS_FLAGS
                                  if kd == "CHAIN"),
                        r0["BARE-LIVE-RECORD"],
                        ", ".join(r0["declared_names"]))
                     for r0 in ladder_classes))
    for r0 in ladder_classes:
        reg(*[r0[k] for k, _c, _l, _d, _kd in CLASS_FLAGS])

    # THE CLASS-WORD BINDING (v14 #294's central ruling): the words printed
    # for a class must be the predicate its number was computed with.
    words_ok = all(
        c["label"] == class_label(c["covering_required"],
                                  c["every_round_saturating"],
                                  c["declared_list"])
        and c["predicate"] == class_predicate(c["covering_required"],
                                              c["every_round_saturating"],
                                              c["declared_list"])
        for c in class_rows)
    flags_ok = all(
        (c["covering_required"], c["every_round_saturating"],
         c["declared_list"]) == (cov, liv, dec)
        for c, (_k, cov, liv, dec, _kd) in zip(class_rows, CLASS_FLAGS))
    LD.add("G-CLASS-WORDS",
           words_ok and flags_ok
           and len({c["label"] for c in class_rows}) == len(class_rows),
           "EVERY LADDER CLASS'S PRINTED WORDS ARE ITS COMPUTED PREDICATE.  A "
           "class here is a pair of flags -- must the record cover all 27 "
           "cells, must every one of its rounds saturate -- plus I7's own "
           "declared list; the floor is computed FROM the flags by one "
           "routine and the words are DERIVED from the same flags, so the "
           "printed class and the computed class cannot come apart.  The "
           "labels are required to be pairwise distinct, and the paper's "
           "table headers and definition sentences are rendered from these "
           "rows, so a class-word swap dies at the table and claim gates",
           "classes %d, labels %s, predicates derived %s, flags matched %s"
           % (len(class_rows), [c["label"] for c in class_rows], words_ok,
              flags_ok))

    # THE BARE-LIVE CONTROL, EXHIBITED: a structurally live R = 5 record whose
    # site code is SINGULAR -- the object §3.7's licensed sentence is about.
    lw_target = sorted(c for c in live_code_space(ROUNDS, live_alpha)
                       if min(c) >= 1 and sig_class(c) == "SINGULAR")[0]
    lw_idx = live_witness(lw_target, ROUNDS)
    lfld = [0] * len(CELLS)
    for i in (lw_idx or ()):
        for kk in range(len(CELLS)):
            lfld[kk] += RC["vecs"][i][kk]
    lfld = pick("M-LIVE-CONTROL", lfld, [c + 1 for c in lfld])
    lw_codes = [tuple(lfld[3 * kk:3 * kk + 3]) for kk in range(len(SITES))]
    live_ctrl = {
        "budget": ROUNDS, "target": list(lw_target),
        "rounds": [list(map(list, RC["parts"][i])) for i in (lw_idx or ())],
        "round_incidences": [RC["incidences"][i] for i in (lw_idx or ())],
        "saturating_rounds": sum(1 for i in (lw_idx or ())
                                 if RC["incidences"][i] == per_round),
        "foreign_pairs": foreign_pairs(list(lw_idx or ())),
        "site_code_at_the_origin": list(lw_codes[0]),
        "det4_at_the_origin": det4(lw_codes[0]),
        "class_at_the_origin": sig_class(lw_codes[0]),
        "cells_covered": sum(1 for c in lfld if c > 0),
        "cells": len(CELLS), "covering": all(c >= 1 for c in lfld),
        "total_incidences": sum(lfld),
        "floors": {pol: [r0["BARE-LIVE-RECORD"] for r0 in ladder_classes
                         if r0["polarity"] == pol][0]
                   for pol in ("SINGULAR", "INDEFINITE")}}
    R["live_control"] = SEAL.take("live_control", live_ctrl)
    LD.add("G-LIVE-CONTROL",
           lw_idx is not None
           and live_ctrl["saturating_rounds"] == ROUNDS
           and live_ctrl["foreign_pairs"] == 0
           and live_ctrl["class_at_the_origin"] == "SINGULAR"
           and live_ctrl["covering"] is False
           and live_ctrl["floors"]["SINGULAR"] < ROUNDS
           and live_ctrl["floors"]["INDEFINITE"] <= ROUNDS,
           "THE BARE-LIVE CONTROL, EXHIBITED ROUND BY ROUND -- AND IT IS WHY "
           "THE COVERING CONDITION IS THE ONE DOING THE WORK.  Drop the "
           "covering condition and keep liveness alone and the floors fall "
           "two rungs; the run exhibits an explicit R = 5 record all of whose "
           "rounds saturate -- so it carries NO foreign pair -- whose site "
           "code at the origin is I7's own G-SINGULAR count vector at 4det 0. "
           "It does NOT cover, and its uncovered cells are counted, so a "
           "polarity census run over bare-live records at this budget sees a "
           "determinant that the live-AND-covering class cannot reach until "
           "two rungs later",
           "bare-live floors %s; the R=%d witness: target %s, rounds "
           "saturating %d of %d, foreign pairs %d, code at the origin %s at "
           "4det %d (%s), covering %s at %d of %d cells, %d incidences"
           % (live_ctrl["floors"], ROUNDS, list(lw_target),
              live_ctrl["saturating_rounds"], ROUNDS,
              live_ctrl["foreign_pairs"], live_ctrl["site_code_at_the_origin"],
              live_ctrl["det4_at_the_origin"],
              live_ctrl["class_at_the_origin"], live_ctrl["covering"],
              live_ctrl["cells_covered"], live_ctrl["cells"],
              live_ctrl["total_incidences"]))
    reg(live_ctrl["cells_covered"], live_ctrl["total_incidences"],
        live_ctrl["foreign_pairs"], live_ctrl["det4_at_the_origin"])

    # ---- THE CELL CEILING, CONTINUED TO THE RUNG ABOVE -------------------
    # The identity `cover = posdef` rode on the covering class's maximum cell
    # count, which is a BUDGET-DEPENDENT quantity.  The per-code route of
    # G-COVER-CODES does not reach R = 6; a second route that carries every
    # code forward at once does, and it is back-validated against the first
    # at all three budgets the first reaches.
    ceil_budgets = LADDER
    cc = {r: covering_class_codes(r) for r in ceil_budgets}
    ceiling = [{"budget": r, "covering_class_codes": len(cc[r]),
                "max_cell": max(max(c) for c in cc[r]),
                "det4_support": sorted({det4(c) for c in cc[r]}),
                "non_posdef": [list(c) for c in cc[r]
                               if sig_class(c) != "POSDEF"],
                "indefinite": [list(c) for c in cc[r]
                               if sig_class(c) == "INDEFINITE"],
                "codes": [list(c) for c in cc[r]]} for r in ceil_budgets]
    ceiling = pick("M-CEILING", ceiling,
                   [dict(c0, max_cell=c0["max_cell"] - 1)
                    if c0["budget"] == max(ceil_budgets) else c0
                    for c0 in ceiling])
    back_ok = {r: sorted(tuple(x) for x in cc[r]) == sorted(occ[r])
               for r in occ}
    seq = [c0["max_cell"] for c0 in ceiling]
    R["covering_ceiling"] = SEAL.take("covering_ceiling", {
        "rows": ceiling, "sequence": seq,
        "back_validated_against_the_per_code_route": back_ok,
        "route": "one shared dynamic program over (partial site code, "
                 "antichain of achievable unions); the quantifier is the "
                 "same 280^R ordered grouping R-tuples"})
    LD.add("G-CEILING",
           all(back_ok.values())
           and all(c0["max_cell"] == max(max(x) for x in c0["codes"])
                   for c0 in ceiling)
           and all(seq[i] <= seq[i + 1] for i in range(len(seq) - 1))
           and seq[-1] > seq[-2],
           "THE COVERING CLASS'S CELL CEILING, MEASURED ONE RUNG ABOVE THIS "
           "ONE BY A SECOND ROUTE, AND BACK-VALIDATED AGAINST THE FIRST.  The "
           "per-code census asks one code at a time; this carries every "
           "partial code forward at once, reducing the achievable unions of "
           "each partial code to their antichain -- sound because union is "
           "monotone, so a union contained in another reaches nothing the "
           "other does not.  At the three budgets the per-code route reaches, "
           "the two agree code for code; at the rung above, where the "
           "per-code route does not run, the ceiling is measured.  The "
           "ceiling RISES again, so the identity that rode on it was living "
           "on a budget-dependent quantity",
           "sequence %s over budgets %s; codes %s; back-validated against the "
           "per-code route at %s; 4det support at the top %s; non-posdef at "
           "the top %s"
           % (seq, list(ceil_budgets),
              [c0["covering_class_codes"] for c0 in ceiling],
              {k: v for k, v in sorted(back_ok.items())},
              ceiling[-1]["det4_support"], ceiling[-1]["non_posdef"]))
    for c0 in ceiling:
        reg(c0["budget"], c0["covering_class_codes"], c0["max_cell"])
        reg(*c0["det4_support"])

    # ---- THE LOCKING OBSTRUCTION'S GENERAL FORM --------------------------
    lock_gen = {str(r): locking_general(r) for r in range(3, ROUNDS + 4)}
    lock_gen = pick("M-LOCK-GENERAL", lock_gen,
                    {k: [dict(row, covering_reachable=True) for row in v]
                     for k, v in lock_gen.items()})
    third = sorted({row["third_members_required"] for row in lock})
    dissolves = min(int(k) for k, v in lock_gen.items()
                    if all(row["covering_reachable"] for row in v))
    min_unc = {k: sorted({row["min_uncovered"] for row in v})
               for k, v in sorted(lock_gen.items(), key=lambda z: int(z[0]))}
    # the counting mechanism is budget-free in its numerator; the measured
    # deficit follows 7 - R only from the budget at which it first can
    formula_from = min(int(k) for k in lock_gen
                       if all(int(k) >= 4 and
                              row["min_uncovered"] == third[0] - int(k)
                              for row in lock_gen[k]))
    # the ladder collapsed one row per budget: all three declared links agree
    # at every budget, and the gate below requires that agreement
    lg_ladder = [{"budget": int(k),
                  "third_members_required": third[0],
                  "best_coverage": sorted({r0["best_coverage"]
                                           for r0 in v})[0],
                  "min_uncovered": sorted({r0["min_uncovered"]
                                           for r0 in v})[0],
                  "covering_reachable": all(r0["covering_reachable"]
                                            for r0 in v),
                  "links_agreeing": len(v)}
                 for k, v in sorted(lock_gen.items(), key=lambda z: int(z[0]))]
    R["locking_general"] = SEAL.take("locking_general", {
        "rows": lock_gen, "ladder": lg_ladder,
        "third_members_required": third,
        "obstruction_dissolves_at": dissolves,
        "min_uncovered": {k: v[0] for k, v in min_unc.items()},
        "deficit_formula": "7 - R",
        "deficit_formula_holds_from": formula_from,
        "min_uncovered_at_this_budget":
            min_unc[str(ROUNDS)][0]})
    LD.add("G-LOCK-GENERAL",
           len(third) == 1 and dissolves == third[0]
           and all(len(v) == 1 for v in min_unc.values())
           and all(not row["covering_reachable"]
                   for k, v in lock_gen.items() if int(k) < third[0]
                   for row in v)
           and all(row["covering_reachable"]
                   for k, v in lock_gen.items() if int(k) >= third[0]
                   for row in v)
           and min_unc[str(ROUNDS)][0] == 2
           and all(len({r0["best_coverage"] for r0 in v}) == 1
                   and len(v) == len(I7_LINKS)
                   for v in lock_gen.values()),
           "THE LOCKING OBSTRUCTION'S GENERAL FORM, AND ITS BOUNDARY.  The "
           "numerator of the count is BUDGET-FREE: a cell at count R locks "
           "its two sites into one group in every round, the cells at those "
           "two sites demand the same seven distinct third members at every "
           "budget, and R rounds supply at most R.  The union of R locked "
           "rounds is therefore carried forward here with NO completion "
           "prune, so the LARGEST union it reaches is measured and not only "
           "its success: the obstruction holds at every budget below seven "
           "and dissolves at exactly seven, where seven rounds can supply "
           "seven thirds.  At this unit's own budget the deficit is two "
           "uncovered cells -- the same minimum the signature unit measures "
           "by branch-and-bound",
           "third members required %s at every link and every budget; "
           "obstruction dissolves at R=%d; minimum uncovered by budget %s; "
           "the deficit follows 7 - R from R=%d"
           % (third, dissolves, {k: v[0] for k, v in min_unc.items()},
              formula_from))
    reg(dissolves, formula_from)
    for k, v in min_unc.items():
        reg(v[0])
    for k, v in lock_gen.items():
        for row in v:
            reg(row["best_coverage"])

    # ---- THE BRIDGE THE `cover = posdef` ROW RESTS ON --------------------
    # A positive-definite code cannot carry a zero count: q11 = n1 > 0 and
    # det > 0 force n2 > 0, and with n3 = 0 the determinant 4.det =
    # -(n1 - n2)^2 <= 0.  So {posdef} is contained in {covered}, ALWAYS, and
    # the two RECORD classes can coincide at all.  Measured over a box that
    # contains every code this unit's ladder reaches.
    bridge_max = per_round * (ROUNDS + 3)
    bridge_bad = posdef_with_a_zero_count(bridge_max)
    bridge_bad = pick("M-BRIDGE", bridge_bad, bridge_bad + [(0, 0, 0)])
    posdef_covered = {str(r): len([c for c in split[r]["covered"]
                                   if sig_class(c) == "POSDEF"])
                      for r in LADDER}
    R["posdef_bridge"] = SEAL.take("posdef_bridge", {
        "box_side": bridge_max, "posdef_with_a_zero_count": len(bridge_bad),
        "positive_definite_covered_codes": posdef_covered,
        "statement": "a positive-definite site code has all three counts "
                     "positive, so a positive-definite RECORD necessarily "
                     "covers; the containment is one-way and the two record "
                     "classes coincide only while the covering class carries "
                     "no non-positive-definite code"})
    LD.add("G-POSDEF-COVERS",
           not bridge_bad and bridge_max > ROUNDS + 3,
           "THE ONE-WAY CONTAINMENT THE `cover = posdef` ROW RESTS ON, "
           "MEASURED.  A positive-definite code cannot carry a zero count: "
           "q11 = n1 forces n1 > 0, positivity of the determinant forces "
           "n2 > 0, and with n3 = 0 the integer 4.det is -(n1 - n2)^2, which "
           "is never positive.  Every code of a box wider than this ladder "
           "reaches is walked, and none is positive definite with a zero "
           "count -- so a positive-definite RECORD necessarily covers, the "
           "containment runs one way, and the equality of the two RECORD "
           "classes is a fact about which codes the covering class carries "
           "rather than a definition",
           "box side %d, positive-definite codes carrying a zero count %d; "
           "positive-definite covered codes by budget %s"
           % (bridge_max, len(bridge_bad), posdef_covered))

    # ---- THE PACKED COLUMN'S NO-CARRY INVARIANT, GATED -------------------
    pack_max = max([c0["max_cell"] for c0 in ceiling]
                   + [max(max(c) for c in split[r]["covered"])
                      for r in LADDER]
                   + [max(max(c) for c in cs[r]) for r in cs])
    pack_max = pick("M-PACK4", pack_max, 16)
    R["pack4"] = SEAL.take("pack4", {
        "bits_per_cell": 4, "capacity": 16, "largest_cell_count": pack_max,
        "statement": "the link field is packed at four bits a cell, so a cell "
                     "count of sixteen would carry into its neighbour; the "
                     "largest count any census of this unit deposits is "
                     "measured against that capacity rather than argued in a "
                     "docstring"})
    LD.add("G-PACK4",
           pack_max < 16 and pack_max > 0,
           "THE PACKED COLUMN CANNOT CARRY, AND THAT IS MEASURED.  Every "
           "census here sums link fields packed at four bits a cell; a cell "
           "reaching sixteen would carry into the next cell and silently "
           "corrupt every count above it.  The largest cell count this run "
           "deposits anywhere -- across the covering class at every budget of "
           "the ladder, the saturating stratum and the covered code space -- "
           "is compared against the packing's capacity",
           "largest cell count %d against a capacity of 16" % pack_max)

    floors = pick("M-SIG-FLOOR", floors,
                  dict(floors, **{"G-INDEF": dict(floors["G-INDEF"],
                                                  budget=ROUNDS)}))
    sig_feed = {
        "budget": ROUNDS,
        "covered_codes": len(split[ROUNDS]["covered"]),
        "posdef": len(r5["POSDEF"]), "singular": len(r5["SINGULAR"]),
        "indefinite": len(r5["INDEFINITE"]),
        "indefinite_codes": [list(c) for c in r5["INDEFINITE"]],
        "indefinite_det4": sorted({det4(c) for c in r5["INDEFINITE"]}),
        "singular_codes": [list(c) for c in r5["SINGULAR"]],
        "indefinite_opens_at": min(r for r in range(1, 9)
                                   if class_split(r, alpha)[1]["INDEFINITE"]),
        "singular_opens_at": min(r for r in range(1, 9)
                                 if class_split(r, alpha)[1]["SINGULAR"]),
        "covering_class_codes": len(occ5),
        "covering_class_max_cell": occ5_max,
        "covering_class_det4_support": occ5_det,
        "covering_class_singular_reachable": bool(occ5_bad),
        "covering_class_indefinite_reachable":
            any(sig_class(c) == "INDEFINITE" for c in occ5),
        "cover_implies_posdef_at_r4": not [c for c in occ[4]
                                           if sig_class(c) != "POSDEF"],
        "cover_implies_posdef_at_r5": not occ5_bad,
        "record_floors": floors,
        "g_singular_record_floor": floors["G-SINGULAR"]["budget"],
        "g_indef_record_floor": floors["G-INDEF"]["budget"]}
    R["sig_feed"] = SEAL.take("sig_feed", sig_feed)
    LD.add("G-SIG-FEED",
           sig_feed["indefinite_opens_at"] == ROUNDS
           and sig_feed["covering_class_indefinite_reachable"] is False
           and sig_feed["covering_class_singular_reachable"] is True
           and sig_feed["cover_implies_posdef_at_r4"] is True
           and sig_feed["cover_implies_posdef_at_r5"] is False
           and floors["G-INDEF"]["budget"] == 8,
           "THE SIG FEED.  At R = 5 the indefinite region opens in the code "
           "space for the first time and is UNREACHABLE inside the covering "
           "class by the locking theorem, while the singular boundary IS "
           "reachable there -- so the covering class stops coinciding with "
           "the positive-definite class exactly at this budget.  As RECORDS, "
           "I7's own G-SINGULAR and G-INDEF sit at the budgets their own "
           "count vectors sum to",
           "indefinite region opens at R=%d (%d codes, 4det %s); inside the "
           "covering class: singular %s, indefinite %s; cover=posdef R=4 %s "
           "-> R=5 %s; record floors G-SINGULAR R=%d, G-INDEF R=%d"
           % (sig_feed["indefinite_opens_at"], sig_feed["indefinite"],
              sig_feed["indefinite_det4"],
              sig_feed["covering_class_singular_reachable"],
              sig_feed["covering_class_indefinite_reachable"],
              sig_feed["cover_implies_posdef_at_r4"],
              sig_feed["cover_implies_posdef_at_r5"],
              floors["G-SINGULAR"]["budget"], floors["G-INDEF"]["budget"]))
    reg(sig_feed["g_singular_record_floor"], sig_feed["g_indef_record_floor"])

    # ---- SEC 4  THE SATURATION SCHEMA AND THE STRATUM --------------------
    say("")
    say("[SEC 4] THE SATURATION SCHEMA, RE-PROVED AT R = 5")
    budget = per_round * ROUNDS
    homo5 = [tuple(c) for c in sorted(cs[ROUNDS])
             if min(c) >= 1 and sum(c) == ROUNDS]
    need = {c: len(SITES) * sum(c) for c in homo5}
    need = pick("M-SATURATION", need, {c: need[c] + 1 for c in need})
    forced = {c: need[c] == budget for c in homo5}
    R["saturation"] = SEAL.take("saturation", {
        "max_incidences_per_round": per_round, "rounds": ROUNDS,
        "budget": budget, "cells": len(CELLS),
        "targets": [list(c) for c in homo5],
        "incidences_needed": {str(list(c)): need[c] for c in homo5},
        "every_round_forced_to_saturate": all(forced.values()),
        "saturating_family": nsat ** ROUNDS,
        "family": nparts ** ROUNDS})
    LD.add("G-SATURATION-SCHEMA",
           all(forced.values()) and budget == per_round * ROUNDS
           and all(need[c] == len(SITES) * sum(c) for c in homo5)
           and per_round == max(spec) and spec[per_round] == nsat,
           "THE SATURATION SCHEMA, RE-PROVED AT THIS RUNG RATHER THAN "
           "INHERITED.  No round deposits more than 9 link incidences, so "
           "five rounds carry at most 45; a homogeneous record whose counts "
           "sum to 5 needs 9 x 5 = 45, and each target's requirement is "
           "recomputed from its own count vector: equality forces every "
           "round to saturate, so a census over the 36^5 saturating "
           "quintuples is exhaustive over all 280^5 for these targets",
           "budget %d = %d x %d, targets %s each needing %d incidences, "
           "forced %d of %d; the empirical premise re-taken here: the "
           "spectrum's top is %d incidences and %d partitions attain it; "
           "saturating family %s of %s"
           % (budget, per_round, ROUNDS, [list(c) for c in homo5], budget,
              sum(1 for v in forced.values() if v), len(homo5),
              max(spec), spec[per_round],
              com(nsat ** ROUNDS), com(nparts ** ROUNDS)))
    reg(budget, len(homo5), nsat ** ROUNDS)

    strat = {}
    for r in (3, 4, ROUNDS):
        strat[r] = stratum_census(r)
    st5 = strat[ROUNDS]
    st5 = pick("M-STRATUM", st5, dict(st5, cover=st5["cover"] + 1))
    back72 = P21["back_validation"]["r3_i7_strict"]
    p21_homo = {tuple(json.loads(k)): v
                for k, v in P21["homogeneous_records"].items()}
    flat = tuple(fam["G-FLAT"])
    strat4_homo = strat[4]["homo"]
    R["stratum"] = SEAL.take("stratum", {
        str(r): {"total": strat[r]["total"], "cover": strat[r]["cover"],
                 "distinct_fields": strat[r]["distinct_fields"],
                 "homogeneous": {str(list(k)): v
                                 for k, v in sorted(strat[r]["homo"].items())},
                 "det4_spectrum": {str(k): v
                                   for k, v in sorted(strat[r]["det"].items())},
                 "posdef_distribution": {str(k): v for k, v in
                                         sorted(strat[r]["pos"].items())},
                 "max_cell": strat[r]["maxcell"],
                 "cover_distinct_fields": strat[r]["cover_distinct_fields"],
                 "site_codes": [list(c) for c in strat[r]["codes"]]}
        for r in (3, 4, ROUNDS)})
    LD.add("G-STRATUM",
           strat[3]["cover"] == back72
           and strat4_homo.get(flat) == p21_homo[flat]
           and all(strat4_homo.get(k) == v for k, v in p21_homo.items()
                   if sum(k) == 4)
           and st5["cover"] == strat[ROUNDS]["cover"],
           "THE SATURATING STRATUM, CENSUSED EXHAUSTIVELY AND VALIDATED "
           "AGAINST TWO COMMITTED ROWS.  Every field the stratum induces is "
           "summed exactly and every covering tuple is classified site by "
           "site; run at R = 3 the covering class is paper-21's committed "
           "I7-STRICT count and at R = 4 every homogeneous record it reaches "
           "matches that unit's committed row, G-FLAT included",
           "R=3 cover %d (committed %d); R=4 homogeneous %s (committed %s); "
           "R=5 total %s, cover %s, distinct fields %s, homogeneous %s, "
           "max cell %d"
           % (strat[3]["cover"], back72,
              {str(list(k)): v for k, v in sorted(strat4_homo.items())},
              {str(list(k)): v for k, v in sorted(p21_homo.items())
               if sum(k) == 4},
              com(strat[ROUNDS]["total"]), com(strat[ROUNDS]["cover"]),
              com(strat[ROUNDS]["distinct_fields"]),
              {str(list(k)): v for k, v in
               sorted(strat[ROUNDS]["homo"].items())},
              strat[ROUNDS]["maxcell"]))
    # THE TWO FIELD COUNTS ARE COUNTS OF DIFFERENT SETS, AND BOTH ARE
    # PUBLISHED.  `distinct_fields` counts the fields the WHOLE stratum
    # induces; `cover_distinct_fields` counts those induced by its COVERING
    # subset -- two orders of magnitude apart at this budget, and a sentence
    # that attaches the first to the second is false.
    cdf = {str(r): strat[r]["cover_distinct_fields"] for r in (3, 4, ROUNDS)}
    cdf = pick("M-FIELDS", cdf,
               {k: (strat[ROUNDS]["distinct_fields"] if int(k) == ROUNDS
                    else v) for k, v in cdf.items()})
    R["stratum_fields"] = SEAL.take("stratum_fields", {
        "whole_stratum": {str(r): strat[r]["distinct_fields"]
                          for r in (3, 4, ROUNDS)},
        "covering_subset": cdf,
        "statement": "the covering subset of the stratum induces far fewer "
                     "distinct fields than the stratum as a whole; the two "
                     "counts are counts of different sets"})
    LD.add("G-STRATUM-FIELDS",
           all(cdf[str(r)] == strat[r]["cover_distinct_fields"]
               for r in (3, 4, ROUNDS))
           and all(cdf[str(r)] < strat[r]["distinct_fields"]
                   for r in (4, ROUNDS))
           and cdf[str(ROUNDS)] > 0,
           "THE COVERING SUBSET'S FIELD COUNT IS ITS OWN MEASUREMENT.  The "
           "stratum induces one number of distinct link fields and its "
           "COVERING subset induces another; each is counted over the set it "
           "names, and the covering count is checked to be strictly the "
           "smaller at every budget where the stratum has a non-covering "
           "part, so a sentence attaching the stratum's count to the "
           "covering tuples cannot be built from these rows",
           "whole stratum %s; covering subset %s"
           % ({r: strat[r]["distinct_fields"] for r in (3, 4, ROUNDS)},
              {k: v for k, v in sorted(cdf.items(), key=lambda z: int(z[0]))}))
    for r in (3, 4, ROUNDS):
        reg(strat[r]["cover_distinct_fields"])

    for r in (3, 4, ROUNDS):
        reg(strat[r]["cover"], strat[r]["total"], strat[r]["maxcell"],
            strat[r]["distinct_fields"])
        for k, v in strat[r]["homo"].items():
            reg(v)
        for k, v in strat[r]["det"].items():
            reg(k, v)
        for k, v in strat[r]["pos"].items():
            reg(k, v)

    # ---- SEC 5  STAGE 1 -- THE THREE PREDICTIONS ------------------------
    say("")
    say("[SEC 5] STAGE 1 -- THE THREE PREDICTIONS")
    ladder_rows = []
    for nm, v in sorted(fam.items()):
        ladder_rows.append({"record": nm, "counts": list(v), "budget": sum(v),
                            "even": sum(v) % 2 == 0,
                            "q12_integer": (v[2] - v[0] - v[1]) % 2 == 0,
                            "link_constant": v[0] == v[1] == v[2]})
    ladder_rows = pick("M-LADDER", ladder_rows,
                       [dict(r0, budget=r0["budget"] + 1) if r0["record"]
                        == "G-FLAT" else r0 for r0 in ladder_rows])
    afford = {4: flat, 6: tuple(fam["G-SINGULAR"])}
    reach = {r: stratum_target_count(afford[r], r) for r in sorted(afford)}
    offrung = {str(list(flat)): stratum_target_count(flat, ROUNDS)}
    R["ladder"] = SEAL.take("ladder", {
        "rows": ladder_rows,
        "reachable_at_its_own_budget": {str(r): reach[r] for r in reach},
        "flat_at_r5": offrung})
    LD.add("G-LADDER",
           all(r0["budget"] == sum(r0["counts"]) for r0 in ladder_rows)
           and all(reach[r] > 0 for r in reach)
           and offrung[str(list(flat))] == 0,
           "THE LADDER LAW, RE-MEASURED ON I7'S OWN DECLARED FAMILY.  A "
           "structurally live schedule spends 9 incidences a round and a "
           "homogeneous record needs 9 per site per link, so its budget is "
           "the sum of its own counts; each declared record's budget is "
           "recomputed from its own count vector, and the two the stratum "
           "can afford are measured non-empty at exactly that budget -- "
           "G-FLAT, measured at R = 5, is empty",
           "budgets %s; reachable at their own budget %s; G-FLAT at R=5 %d"
           % ({r0["record"]: r0["budget"] for r0 in ladder_rows},
              {r: reach[r] for r in reach}, offrung[str(list(flat))]))
    reg(*[r0["budget"] for r0 in ladder_rows])
    reg(*[reach[r] for r in reach])

    # ---- THE DECLARED RECORDS, CENSUSED AT THEIR OWN BUDGETS -------------
    # The ladder law settles the LOWER half of a record floor -- nothing can
    # arrive earlier.  The upper half is a census, and it is run here at every
    # declared budget the saturating stratum reaches, G-INDEF's R = 8
    # included, so the floor column is a floor and not an inequality.
    census_ceiling = 2 * ROUNDS
    realiz = {}
    for nm, v in sorted(fam.items()):
        b = sum(v)
        realiz[nm] = {"record": list(v), "budget": b,
                      "class": sig_class(tuple(v)),
                      "witnesses": (stratum_target_count(tuple(v), b)
                                    if b <= census_ceiling else None),
                      "censused": b <= census_ceiling}
    realiz = pick("M-RECORD-FLOOR", realiz,
                  dict(realiz, **{"G-INDEF": dict(realiz["G-INDEF"],
                                                  witnesses=0)}))
    censused = [nm for nm in realiz if realiz[nm]["censused"]]
    R["record_realizability"] = SEAL.take("record_realizability", {
        "rows": realiz, "census_ceiling": census_ceiling,
        "censused": sorted(censused),
        "beyond_the_census": sorted(nm for nm in realiz
                                    if not realiz[nm]["censused"]),
        "statement": "the ladder law forbids a record before the sum of its "
                     "own counts; the census decides that it arrives there"})
    LD.add("G-RECORD-FLOORS",
           all(realiz[nm]["witnesses"] > 0 for nm in censused)
           and realiz["G-INDEF"]["censused"]
           and realiz["G-INDEF"]["witnesses"] > 0
           and all(realiz[nm]["budget"] == sum(realiz[nm]["record"])
                   for nm in realiz),
           "EVERY DECLARED RECORD THE STRATUM REACHES IS CENSUSED AT ITS OWN "
           "BUDGET, SO ITS FLOOR IS A FLOOR.  The ladder law gives only the "
           "lower half -- no record can arrive before its own counts sum -- "
           "and a column printing a budget without a witness there is an "
           "inequality wearing a floor's clothes.  Each record whose budget "
           "the saturating stratum reaches is counted at exactly that budget, "
           "I7's own G-INDEF at R = 8 included; the records beyond the "
           "census are named as such rather than asserted",
           "censused %s; beyond the census %s"
           % ({nm: realiz[nm]["witnesses"] for nm in sorted(censused)},
              sorted(nm for nm in realiz if not realiz[nm]["censused"])))
    for nm in censused:
        reg(realiz[nm]["witnesses"])

    even_pts = [p for p in pts if sum(p) % 2 == 0]
    parity = {"declared_even": sum(1 for r0 in ladder_rows if r0["even"]),
              "declared_total": len(ladder_rows),
              "box_even": len(even_pts), "box_odd": len(pts) - len(even_pts),
              "mechanism_holds": all(r0["even"] == r0["q12_integer"]
                                     for r0 in ladder_rows)}
    parity = pick("M-PARITY", parity, dict(parity, declared_even=0))
    R["parity"] = SEAL.take("parity", parity)
    LD.add("G-PARITY",
           parity["declared_even"] == len(ladder_rows)
           and parity["mechanism_holds"]
           and parity["box_even"] + parity["box_odd"] == len(pts),
           "THE PARITY LAW.  Every one of I7's nine declared homogeneous "
           "records has an EVEN count sum, and each record's parity is "
           "checked against its own off-diagonal entry: the sum is even "
           "exactly when q12 = (n_diag - n_e1 - n_e2)/2 is an integer, so "
           "the declared family lies inside the integer-off-diagonal "
           "sublattice.  Its own admissible box is not so restricted, and "
           "the split is measured",
           "declared with even sum %d of %d; the mechanism (even sum iff q12 "
           "integral) holds on %d of %d; admissible box %d even and %d odd "
           "of %d" % (parity["declared_even"], len(ladder_rows),
                      sum(1 for r0 in ladder_rows
                          if r0["even"] == r0["q12_integer"]),
                      len(ladder_rows), parity["box_even"], parity["box_odd"],
                      len(pts)))
    reg(parity["box_even"], parity["box_odd"])

    box5 = [p for p in pts if sum(p) == ROUNDS]
    reached5 = sorted(strat[ROUNDS]["homo"])
    declared5 = [nm for nm, v in fam.items() if sum(v) == ROUNDS]
    pred_a = {"declared_at_this_budget": declared5,
              "admissible_box_points_at_this_budget": [list(p) for p in box5],
              "reached": [list(c) for c in reached5],
              "reached_all_of_them": sorted(box5) == sorted(reached5),
              "any_reached_declared": [nm for nm, v in fam.items()
                                       if tuple(v) in set(reached5)],
              "verdict": "PASS"}
    pred_a = pick("M-PRED-A", pred_a,
                  dict(pred_a, declared_at_this_budget=["G-FLAT"]))
    pred_a["verdict"] = "PASS" if not pred_a["declared_at_this_budget"] \
        else "FAIL"
    R["prediction_a"] = SEAL.take("prediction_a", pred_a)
    LD.add("G-PRED-A",
           pred_a["verdict"] == "PASS" and pred_a["reached_all_of_them"]
           and not pred_a["any_reached_declared"],
           "PREDICTION (a) -- NO DECLARED RECORD AT THIS BUDGET -- PASSES, "
           "AND ON THE STRONGEST WITNESS AVAILABLE.  I7's committed box is "
           "walked point by point: it holds six admissible count vectors "
           "summing to 5, the R = 5 stratum reaches EVERY ONE of them, and "
           "not one is among I7's declared records -- so the prediction is "
           "confirmed by exhaustion rather than by absence of search",
           "declared records at this budget %s; admissible box points %s; "
           "reached %s; all reached %s"
           % (pred_a["declared_at_this_budget"],
              pred_a["admissible_box_points_at_this_budget"],
              pred_a["reached"], pred_a["reached_all_of_them"]))
    reg(len(box5), len(reached5))

    live_const = {}
    for r in LADDER:
        m9 = per_round * r
        live_const[r] = {"incidences": m9,
                         "divides": m9 % len(CELLS) == 0,
                         "record": [m9 // len(CELLS)] * 3
                         if m9 % len(CELLS) == 0 else None,
                         "mod3": r % 3}
    live_const = pick("M-PRED-B", live_const,
                      {r: dict(v, divides=True) for r, v in
                       live_const.items()})
    ant = class_schedule(("ROW", "COL", "DIA", "ANT", "ANT"))
    ant_field = field_of_schedule(ant)
    ant_idx = [RC["index"][P] for (P, _s) in ant]
    ant_row = detect("R5-TWO-ANT(field identically 1)",
                     groupings_footprints(ant_idx), "EMBEDDING")
    ant_foreign = foreign_pairs(ant_idx)
    pred_b = {"link_constant_needs": "27 | 9R",
              "rows": {str(r): live_const[r] for r in LADDER},
              "possible_at": [r for r in LADDER if live_const[r]["divides"]],
              "this_budget_possible": live_const[ROUNDS]["divides"],
              "control_field": sorted(set(ant_field)),
              "control_fate": ant_row["fate"],
              "control_foreign_pairs": ant_foreign,
              "modulus": len(CELLS) // per_round,
              "residue": (per_round * len(I7_LINKS)) % len(CELLS),
              "verdict": "PASS"}
    pred_b["verdict"] = "PASS" if not pred_b["this_budget_possible"] else "FAIL"
    R["prediction_b"] = SEAL.take("prediction_b", pred_b)
    LD.add("G-PRED-B",
           pred_b["verdict"] == "PASS"
           and pred_b["possible_at"] == [r for r in LADDER if r % 3 == 0]
           and ant_row["fate"] == "STRUCT-DEAD" and ant_foreign > 0
           and set(ant_field) == {1},
           "PREDICTION (b) -- ZERO FREE ITEMS IS IMPOSSIBLE AT THIS BUDGET -- "
           "PASSES, PROVED IN-ARENA.  Zero free items holds exactly at the "
           "link-constant records; a structurally live R-tuple deposits 9R "
           "incidences over 27 cells, so a link-constant field needs 27 | 9R, "
           "i.e. R = 0 mod 3, and the ladder's own rows are computed one by "
           "one.  The premise is not vacuous: this arena's own "
           "link-constant R = 5 control carries a field identically 1 and "
           "dies at STRUCTURE, on its foreign pairs, not at arithmetic",
           "link-constant possible at R %s (R = 0 mod 3), at this budget %s; "
           "the control's field %s, fate %s, foreign pairs %d"
           % (pred_b["possible_at"], pred_b["this_budget_possible"],
              pred_b["control_field"], ant_row["fate"], ant_foreign))
    reg(ant_foreign)

    yields = {}
    for r in LADDER:
        dec = [nm for nm, v in fam.items() if sum(v) == r]
        cnt = {}
        if r <= 6:
            for nm in dec:
                cnt[nm] = stratum_target_count(tuple(fam[nm]), r)
        yields[r] = {"declared_records_at_this_budget": sorted(dec),
                     "declared_yield": sum(cnt.values()),
                     "per_record": cnt,
                     "motivated_possible": r % 3 == 0,
                     "reachable_codes": len(cs[r]),
                     "covering_class_codes": len(occ[r]) if r in occ else None,
                     "covering_class_max_cell":
                         max(max(c) for c in occ[r]) if r in occ else None}
    yields = pick("M-PRED-C", yields,
                  {r: dict(v, declared_yield=v["declared_yield"] + 1)
                   for r, v in yields.items()})
    pred_c = {
        "currencies": ["A DECLARED RECORD", "A MOTIVATED WELD"],
        "rows": {str(r): yields[r] for r in LADDER},
        "this_budget_declared_yield": yields[ROUNDS]["declared_yield"],
        "parent_declared_yield": yields[4]["declared_yield"],
        "this_budget_motivated": yields[ROUNDS]["motivated_possible"],
        "parent_motivated": yields[4]["motivated_possible"],
        "strictly_weaker_in_the_currencies":
            yields[ROUNDS]["declared_yield"] < yields[4]["declared_yield"]
            and not yields[ROUNDS]["motivated_possible"]
            and not yields[4]["motivated_possible"],
        "parent_budget": ROUNDS - 1, "door_budget": ROUNDS + 1,
        "richer_in": {
            "reachable_codes": [len(cs[4]), len(cs[ROUNDS])],
            "covering_class_codes": [len(occ[4]), len(occ[ROUNDS])],
            "covering_class_max_cell": [occ4_max, occ5_max],
            "det4_support": [len(occ4_det), len(occ5_det)],
            "stratum_cover": [strat[4]["cover"], strat[ROUNDS]["cover"]]},
        "richer_in_denominators": {
            "reachable_codes": [len(cs[4]), len(cs[ROUNDS])],
            "covering_class_codes": [len(split[4]["covered"]),
                                     len(split[ROUNDS]["covered"])],
            "covering_class_max_cell": [len(CELLS) // len(SITES),
                                        len(CELLS) // len(SITES)],
            "det4_support": [len(occ4_det), len(occ5_det)],
            "stratum_cover": [strat[4]["total"], strat[ROUNDS]["total"]]},
        "richer_in_measure": "COUNTING-ONLY",
        "verdict": "PASS"}
    pred_c["verdict"] = ("PASS" if pred_c["strictly_weaker_in_the_currencies"]
                         else "FAIL")
    R["prediction_c"] = SEAL.take("prediction_c", pred_c)
    LD.add("G-PRED-C",
           pred_c["verdict"] == "PASS"
           and yields[4]["declared_yield"] == p21_homo[flat]
           and yields[6]["declared_yield"] > 0
           and all(v[1] > v[0] for v in pred_c["richer_in"].values()),
           "PREDICTION (c) -- R = 5 IS STRICTLY WEAKER THAN R = 4 -- PASSES "
           "IN THE LADDER'S TWO CURRENCIES, AND THE COUNTER-COLUMN IS "
           "PUBLISHED WITH IT.  The comparison is the declared-record yield "
           "and the motivated-weld yield, computed per budget from each "
           "record's own count vector: R = 4 buys a declared record at 276 "
           "witnesses and R = 5 buys neither currency, while R = 6 buys "
           "both.  In every SLACK column R = 5 is strictly RICHER, and those "
           "columns are reported here rather than suppressed",
           "declared yield: %s; motivated possible: %s; richer at R=5 in %s"
           % ({r: yields[r]["declared_yield"] for r in LADDER},
              {r: yields[r]["motivated_possible"] for r in LADDER},
              pred_c["richer_in"]))
    for r in LADDER:
        reg(yields[r]["declared_yield"])
    preds = {"a": pred_a["verdict"], "b": pred_b["verdict"],
             "c": pred_c["verdict"]}
    R["predictions"] = SEAL.take("predictions", {
        "verdicts": preds,
        "passed": sum(1 for v in preds.values() if v == "PASS"),
        "total": len(preds)})
    LD.add("G-PREDICTIONS",
           sum(1 for v in preds.values() if v == "PASS") == len(preds),
           "THE THREE PREDICTIONS THE PARENT REGISTERED, EACH DECIDED ON ITS "
           "OWN WITNESS.  Every one is evaluated against the object it is "
           "about -- I7's committed box, the arena's own arithmetic and the "
           "two ladder currencies -- and the verdict of each is carried "
           "separately rather than summed into a score",
           "verdicts %s, passed %d of %d"
           % (preds, sum(1 for v in preds.values() if v == "PASS"),
              len(preds)))

    # ---- SEC 6  STAGE 2 -- THE SLACK CENSUS ------------------------------
    say("")
    say("[SEC 6] STAGE 2 -- THE SLACK CENSUS")
    slack_rows = {}
    for r in (2,) + LADDER:
        dep = per_round * r
        slack_rows[r] = {"budget": dep, "cells": len(CELLS),
                         "slack": dep - len(CELLS),
                         "formula": per_round * (r - 3),
                         "binds": ("THE BUDGET" if dep < len(CELLS) else
                                   ("THE PERFECT MATCHING" if dep == len(CELLS)
                                    else "THE COVER"))}
    slack5 = slack_rows[ROUNDS]["slack"]
    slack5 = pick("M-SLACK", slack5, slack5 + 1)
    R["slack"] = SEAL.take("slack", {
        "rows": {str(r): slack_rows[r] for r in slack_rows},
        "slack_at_this_budget": slack5,
        "predicted": per_round * (ROUNDS - len(CELLS) // per_round),
        "formula_offset": len(CELLS) // per_round,
        "binding": slack_rows[ROUNDS]["binds"],
        "buys": {
            "reachable_site_codes": {str(r): len(cs[r]) for r in LADDER},
            "covering_class_codes": {str(r): len(occ[r]) for r in occ},
            "covering_class_max_cell": {str(r): max(max(c) for c in occ[r])
                                        for r in occ},
            "det4_support_size": {str(r): len({det4(c) for c in occ[r]})
                                  for r in occ},
            "cover_equals_posdef": {str(r): not [c for c in occ[r]
                                                 if sig_class(c) != "POSDEF"]
                                    for r in occ}}})
    LD.add("G-SLACK",
           slack5 == per_round * (ROUNDS - 3)
           and slack_rows[ROUNDS]["binds"] == slack_rows[4]["binds"]
           and slack_rows[3]["slack"] == 0 and slack_rows[2]["slack"] < 0,
           "THE SLACK, VERIFIED AGAINST THE PARENT'S FORMULA, AND WHAT IT "
           "BUYS.  Each row's slack is recomputed from its own budget as "
           "9R - 27 and compared with 9(R - 3); at R = 5 the cover is still "
           "what binds, so the sequence gains a fourth ROW and no fourth "
           "condition, and the slack's content is measured column by column",
           "slack %d = 9(%d - 3); binding %s; rows %s"
           % (slack5, ROUNDS, slack_rows[ROUNDS]["binds"],
              {r: (slack_rows[r]["budget"], slack_rows[r]["slack"],
                   slack_rows[r]["binds"]) for r in sorted(slack_rows)}))
    reg(slack5, *[slack_rows[r]["budget"] for r in slack_rows])

    # ---- SEC 7  STAGE 3 -- THE DICTIONARY ROW ----------------------------
    say("")
    say("[SEC 7] STAGE 3 -- THE DICTIONARY ROW (the weld along the ladder)")
    weld_arenas = [
        ("R3-SAT(1,1,1)", (1, 1, 1), 3),
        ("R4-FLAT(1,1,2)=G-FLAT", flat, 4),
        ("R5-COLLINEAR(1,1,3)", (1, 1, 3), ROUNDS),
        ("R5-(1,2,2)", (1, 2, 2), ROUNDS),
        ("R6-(2,2,2)", (2, 2, 2), 6),
        ("R6-(1,1,4)=G-SINGULAR", tuple(fam["G-SINGULAR"]), 6)]
    weld_rows = []
    for nm, rec, r in weld_arenas:
        idx = [RC["index"][CLASSES[c]] for c in class_names_for(rec)]
        fps = groupings_footprints(idx)
        for reading in ("EMBEDDING", "QUOTIENT"):
            row = detect(nm, fps, reading)
            row["record_declared"] = [k for k, v in fam.items()
                                      if tuple(v) == rec]
            row["fiber_string"] = "/".join(
                str(row["inventory"][k]) for k in
                ("I-SITE-ASSIGNMENT", "I-DIRECTION-LABEL", "I-ORIENT")
            ) if "inventory" in row else None
            row["budget"] = r
            row["link_constant"] = rec[0] == rec[1] == rec[2]
            weld_rows.append(row)
    weld_rows = pick("M-WELD", weld_rows,
                     [dict(w, inventory=dict(w["inventory"],
                                             **{"I-SITE-ASSIGNMENT": 1}),
                           fate="FOUND") if w["budget"] == ROUNDS else w
                      for w in weld_rows])
    weld_rows = pick("M-FIBER-LAW", weld_rows,
                     [dict(w, link_constant=not w["link_constant"])
                      for w in weld_rows])
    fiber_law = all((max(w["inventory"].values()) == 1) == w["link_constant"]
                    for w in weld_rows)
    p21_fibers = (p21["counts"]["site_fiber"], p21["counts"]["label_fiber"],
                  p21["counts"]["orient_fiber"])
    r4rows = [w for w in weld_rows if w["arena"].startswith("R4-FLAT")]
    r4fib = tuple(r4rows[0]["inventory"][k] for k in
                  ("I-SITE-ASSIGNMENT", "I-DIRECTION-LABEL", "I-ORIENT"))
    r5rows = [w for w in weld_rows if w["budget"] == ROUNDS]
    r6rows = [w for w in weld_rows if w["arena"] == "R6-(2,2,2)"]
    # THE SPREADS TRAVEL WITH THE HEADLINE FIBERS.  The site fiber is read at
    # every base map; the label and orient fibers are read at the
    # enumeration's FIRST base map and are not base-map invariant.  Both
    # spreads are bound here so the qualifier cannot be dropped silently.
    unmot = [w for w in weld_rows if w["fate"] == "UNMOTIVATED"]
    spread_rows = sorted({(w["budget"], tuple(w["label_fiber_spread"]),
                           tuple(w["orient_fiber_spread"]),
                           w["fibers_base_map_invariant"]) for w in unmot})
    spread_rows = pick("M-SPREAD", spread_rows,
                       [(b, (l[0],), o, inv)
                        for (b, l, o, inv) in spread_rows])
    spreads_persist = (len({(l, o) for (_b, l, o, _i) in spread_rows}) == 1
                       and len({b for (b, _l, _o, _i) in spread_rows}) > 1)
    R["weld"] = SEAL.take("weld", {
        "rows": weld_rows, "fiber_law_holds": fiber_law,
        "base_map_note": "the site fiber is read at every base map; the label "
                         "and orient fibers are read at the enumeration's "
                         "first and are not base-map invariant",
        "unmotivated_spreads": [{"budget": b, "label_fiber_spread": list(l),
                                 "orient_fiber_spread": list(o),
                                 "fibers_base_map_invariant": i}
                                for (b, l, o, i) in spread_rows],
        "spreads_persist": spreads_persist})
    LD.add("G-WELD-ROWS",
           r4fib == p21_fibers
           and all(w["isomorphisms"] == p21["counts"]["isomorphisms"]
                   for w in weld_rows if w["reading"] == "EMBEDDING")
           and all(w["fate"] == "FOUND" for w in r6rows)
           and all(w["fate"] == "UNMOTIVATED" for w in r5rows)
           and spreads_persist
           and all(i is False for (_b, _l, _o, i) in spread_rows)
           and all(len(l) > 1 and len(o) > 1
                   for (_b, l, o, _i) in spread_rows),
           "THE WELD, RUN ON ONE INSTRUMENT AT EVERY RUNG, AND VALIDATED AT "
           "THE RUNG WHOSE ANSWER IS COMMITTED -- WITH THE BASE-MAP "
           "QUALIFIER BOUND TO THE ROW.  Weld 2's detector is carried "
           "unchanged at both readings; at R = 4 it returns paper-21's "
           "committed fibers and isomorphism count exactly, at R = 6 the "
           "link-constant record returns ZERO-FREE-ITEMS, and every R = 5 "
           "arena returns UNMOTIVATED.  The headline triple is read AT ONE "
           "BASE MAP: the label and orient fibers are not base-map invariant, "
           "their spreads across the enumeration are measured here, and the "
           "spreads are required to be identical at every unmotivated arena "
           "-- so what persists across the rung is the whole spread and not "
           "only the headline",
           "R=4 fibers %s against paper-21's committed %s; R=5 fibers %s; "
           "R=6 (2,2,2) fibers %s; isomorphisms %d everywhere; unmotivated "
           "spreads %s, base-map invariant %s, spreads persist %s"
           % (list(r4fib), list(p21_fibers),
              [list(w["inventory"].values()) for w in r5rows
               if w["reading"] == "EMBEDDING"],
              [list(w["inventory"].values()) for w in r6rows
               if w["reading"] == "EMBEDDING"],
              p21["counts"]["isomorphisms"],
              [(b, list(l), list(o)) for (b, l, o, _i) in spread_rows],
              sorted({i for (_b, _l, _o, i) in spread_rows}),
              spreads_persist))
    for (_b, l, o, _i) in spread_rows:
        reg(*(list(l) + list(o)))
    reg(*p21_fibers)
    reg(p21["counts"]["isomorphisms"])
    LD.add("G-WELD-FIBER-LAW",
           fiber_law,
           "THE FIBER LAW, MEASURED PER ARENA.  Each arena's inventory is "
           "compared against its OWN record: the three fibers are all 1 "
           "exactly at the link-constant records, and the R = 5 rung -- "
           "which the ladder law says cannot carry one -- returns the same "
           "2-free-item signature the R = 4 rung returns, so the "
           "imperfection neither grows nor shrinks with the slack",
           "arenas %d, agreements %d of %d"
           % (len(weld_arenas), sum(1 for w in weld_rows
                                    if (max(w["inventory"].values()) == 1)
                                    == w["link_constant"]), len(weld_rows)))

    r6count = {"(2, 2, 2)": stratum_target_count((2, 2, 2), 6),
               "G-SINGULAR": stratum_target_count(tuple(fam["G-SINGULAR"]), 6)}
    r6count = pick("M-R6", r6count, dict(r6count, **{"(2, 2, 2)": 1}))
    m6 = re.search(r"concatenate to \(2, 2, 2\).*?at least \*\*([\d,]+)\*\* *\n? *ordered witnesses",
                   texts["v14/paper-21-r4dec.md"], re.S)
    p21_lower = int(m6.group(1).replace(",", "")) if m6 else None
    R["r6_door"] = SEAL.take("r6_door", {
        "counts": r6count, "budget": ROUNDS + 1,
        "link_constant_record": list((2, 2, 2)),
        "parent_constructive_lower_bound": p21_lower,
        "exceeds_the_parent_bound": r6count["(2, 2, 2)"] >= p21_lower,
        "declared_record_at_r6": [nm for nm, v in fam.items()
                                  if sum(v) == 6]})
    LD.add("G-R6-DOOR",
           p21_lower is not None
           and r6count["(2, 2, 2)"] >= p21_lower and r6count["G-SINGULAR"] > 0
           and r6count["(2, 2, 2)"] == stratum_target_count((2, 2, 2), 6),
           "THE R = 6 DOOR, CENSUSED EXACTLY WHERE THE PARENT COULD ONLY "
           "BOUND IT.  The saturation schema at R = 6 makes the 36^6 "
           "stratum exhaustive for records summing to 6, so the "
           "link-constant (2, 2, 2) is counted rather than bounded -- above "
           "the parent's constructive lower bound -- and the same census "
           "finds that I7's own DECLARED G-SINGULAR sits at this budget, one "
           "rung below the declared record the parent registered",
           "(2,2,2) at %s ordered saturating sextuples against the parent's "
           "constructive lower bound %s; G-SINGULAR at %s; declared records "
           "at R=6 %s" % (com(r6count["(2, 2, 2)"]), com(p21_lower),
                          com(r6count["G-SINGULAR"]),
                          [nm for nm, v in fam.items() if sum(v) == 6]))
    reg(r6count["(2, 2, 2)"], r6count["G-SINGULAR"], p21_lower)

    # ---- SEC 8  THE COMMITTED GRAMMAR, DRIVEN ---------------------------
    say("")
    say("[SEC 8] THE COMMITTED GRAMMAR, DRIVEN AT R = 5 AND R = 6")
    G = Grammar(texts)
    LD.add("G-SLICE-EXIT-FREE",
           G.slice_exit_free and G.bodies_exit_free,
           "THE COMMITTED LAYERS ENTER AS SINGLE SOURCES AND CANNOT EXIT.  "
           "d42b1's transport layer is taken as a TEXT SLICE cut at the "
           "layer's own banner print, so its menu function -- this unit's "
           "only source of admissibility -- is the committed one and nothing "
           "below the cut can run; d60's and d66's definitions enter by AST "
           "extraction, so no module-level statement of theirs can run",
           "slice exit-free %s, extracted bodies exit-free %s, slice ends at "
           "char %d of %d" % (G.slice_exit_free, G.bodies_exit_free,
                              G.slice_chars[0], G.slice_chars[1]))

    d66rows = {}
    for r in (4, 6):
        m = re.search(r"GRID\(g=3,R=%d\)\s+n=\s*(\d+)\s+arbs=\s*(\d+)"
                      r"[^\n]*?deliveries=\s*(\d+)" % r,
                      texts["v10/data/d66_arbitration_crystal_exact.out"])
        d66rows[r] = tuple(int(x) for x in m.groups()) if m else None
    anchor_rows = {}
    for r in (4, 6):
        b_committed = G.conflict_grid(3, r)
        b_driven = drive(G, committed_schedule(r))
        prof = (len(b_driven.H),
                sum(1 for e in b_driven.H if e[0] == "r"),
                sum(1 for e in b_driven.H if e[0] == "d"))
        prof = pick("M-DRIVE-ANCHOR", prof,
                    (prof[0] + 1, prof[1], prof[2])) if r == 6 else prof
        anchor_rows[str(r)] = {"identical_event_lists":
                          list(b_committed.H) == list(b_driven.H),
                               "driven_profile": list(prof),
                               "d66_committed_row": list(d66rows[r])}
    R["driver_anchor"] = SEAL.take("driver_anchor", anchor_rows)
    LD.add("G-DRIVER-ANCHOR",
           all(a["identical_event_lists"] for a in anchor_rows.values())
           and all(tuple(a["driven_profile"]) == tuple(a["d66_committed_row"])
                   for a in anchor_rows.values()),
           "THE GENERALIZED DRIVER IS ANCHORED AGAINST THE OBJECT IT "
           "GENERALIZES, AT TWO BUDGETS, ONE OF THEM WIDER THAN THIS UNIT'S "
           "OWN.  d66's committed constructor is re-run in this process at "
           "R = 4 and at R = 6 and the schedule-driven builder is run at "
           "d66's own schedule; the two emit IDENTICAL event lists, and each "
           "driven profile is compared against d66's OWN COMMITTED OUTPUT "
           "ROW read from its pinned bytes at run time",
           "; ".join("R=%s identical %s, driven (n, arbs, deliveries) %s, "
                     "d66's committed row %s"
                     % (r, anchor_rows[r]["identical_event_lists"],
                        tuple(anchor_rows[r]["driven_profile"]),
                        tuple(anchor_rows[r]["d66_committed_row"]))
                     for r in sorted(anchor_rows, key=int)))
    for r in anchor_rows:
        reg(*anchor_rows[r]["d66_committed_row"])

    sch_list, meta, fan = window_schedules(reached5)
    drows = []
    for sch in sch_list:
        rec = driven(G, sch)
        fld = link_field_of(rec["footprints"])
        drv = tuple(fld[c] for c in CELLS)
        comb = field_of_schedule(sch)
        drv = pick("M-DRIVEN-EQ", drv, tuple(c + 1 for c in drv)) \
            if meta[sch] == "W5-LADDER" and len(sch) == ROUNDS else drv
        codes = sorted({tuple(drv[3 * k:3 * k + 3]) for k in range(len(SITES))})
        drows.append({"tag": meta[sch], "rounds": len(sch),
                      "events": rec["events"], "divisions": rec["divisions"],
                      "maxhits": rec["maxhits"],
                      "refusal": rec["refusal"] is not None,
                      "equal": drv == comb,
                      "record": [list(c) for c in codes]})
    nequal = sum(1 for d in drows if d["equal"])
    R["driven"] = SEAL.take("driven", {
        "window": {t: sum(1 for d in drows if d["tag"] == t)
                   for t in sorted({d["tag"] for d in drows})},
        "schedules": len(drows), "rows": drows,
        "equalities": nequal,
        "budgets": sorted({d["rounds"] for d in drows}),
        "event_spectrum": {str(k): v for k, v in
                           sorted(Counter(d["events"] for d in drows).items())}})
    LD.add("G-DRIVEN-EQUALITY",
           nequal == len(drows) and len(drows) > 0
           and all(not d["refusal"] for d in drows)
           and max(d["rounds"] for d in drows) == 6,
           "THE COMMITTED GRAMMAR DRIVES THIS RUNG AND THE ONE ABOVE IT, AND "
           "EVERY DRIVEN FIELD IS ITS OWN GROUPINGS' FIELD.  Each schedule "
           "of the declared window W5 is driven event by event through the "
           "layer's own menus, and the link field read off the DRIVEN record "
           "-- footprints taken from the layer's own register reader -- is "
           "compared cell by cell against the field the combinatorial route "
           "computes from the groupings alone.  The parent left this open at "
           "R = 6: the concatenation IS driven",
           "schedules %d over budgets %s, cell-by-cell equalities %d, "
           "refusals %d, window %s"
           % (len(drows), sorted({d["rounds"] for d in drows}), nequal,
              sum(1 for d in drows if d["refusal"]),
              {t: sum(1 for d in drows if d["tag"] == t)
               for t in sorted({d["tag"] for d in drows})}))
    reg(len(drows), nequal)
    for d in drows:
        reg(d["events"], d["divisions"])

    # ---- THE DECLARED WINDOW, DECOMPOSED BY PARTS AND GATED --------------
    # The head advertises the window's SIZE; §6.2 states its PARTS.  A
    # decomposition whose parts are wrong in two places that cancel in the sum
    # is invisible to a gate on the sum alone, so the parts are rendered as
    # table rows and the sum is re-taken from them.
    wtags = sorted({d["tag"] for d in drows})
    window_rows = [{"tag": t,
                    "schedules": sum(1 for d in drows if d["tag"] == t),
                    "budgets": sorted({d["rounds"] for d in drows
                                       if d["tag"] == t})}
                   for t in wtags]
    window_rows = pick("M-WINDOW", window_rows,
                       [dict(w, schedules=w["schedules"] + 1)
                        if w["tag"] == "W5-SEEDFAN" else
                        (dict(w, schedules=w["schedules"] - 1)
                         if w["tag"] == "W4-ANCHOR" else w)
                        for w in window_rows])
    fan_ok = (fan["choices"] == len(canon_transversals(CLASSES["ROW"])) ** 2
              and fan["fresh"] == fan["choices"] - len(fan["collided"])
              and len(fan["collided"]) == 1
              and fan["collides_with"] is not None)
    anchor_budgets = sorted({d["rounds"] for d in drows
                             if d["tag"] == "W4-ANCHOR"})
    R["window"] = SEAL.take("window", {
        "rows": window_rows, "schedules": len(drows),
        "sum_by_parts": sum(w["schedules"] for w in window_rows),
        "seed_fan": fan, "budgets": sorted({d["rounds"] for d in drows}),
        "the_only_budget_4_member": [w["tag"] for w in window_rows
                                     if w["budgets"] == [ROUNDS - 1]]})
    LD.add("G-WINDOW-DECOMP",
           sum(w["schedules"] for w in window_rows) == len(drows)
           and fan_ok
           and anchor_budgets == [ROUNDS - 1]
           and [w["tag"] for w in window_rows
                if w["budgets"] == [ROUNDS - 1]] == ["W4-ANCHOR"]
           and all(w["schedules"] > 0 for w in window_rows),
           "THE DECLARED WINDOW IS BOUND BY ITS PARTS AND NOT ONLY BY ITS "
           "SUM.  Every tag's schedule count and budget set is rendered as a "
           "table row, the sum is re-taken from the parts, and the seed fan's "
           "own arithmetic is measured: the fan enumerates its choices, one "
           "of them coincides with a schedule already in the window, and the "
           "number it CONTRIBUTES is therefore one less than the number it "
           "enumerates.  The budget-4 member is identified by its budget "
           "rather than named, so a decomposition that omits it cannot sum",
           "parts %s summing to %d against %d schedules; the seed fan "
           "enumerates %d choices, contributes %d, and its one collision is "
           "with %s; the only budget-%d member is %s"
           % ({w["tag"]: w["schedules"] for w in window_rows},
              sum(w["schedules"] for w in window_rows), len(drows),
              fan["choices"], fan["fresh"], fan["collides_with"], ROUNDS - 1,
              [w["tag"] for w in window_rows
               if w["budgets"] == [ROUNDS - 1]]))
    reg(fan["choices"], fan["fresh"])
    for w in window_rows:
        reg(w["schedules"])

    forced = all(d["maxhits"] == 1 for d in
                 pick("M-FORCED", drows,
                      [dict(d, maxhits=d["maxhits"] + 1) for d in drows]))
    ctrl_sch = class_schedule(class_names_for((1, 1, 3)))
    b_ref = drive(G, ctrl_sch, drop_supply=0)
    refused = b_ref.refusal is not None
    rec_ctrl = driven(G, ctrl_sch)
    fal_fps = rec_ctrl["footprints"][1:]
    rec_arb = {"divisions": len(fal_fps)}
    fld_arb = link_field_of(fal_fps)
    fal_row = detect("R5-FALSIFIER(one division withheld)", fal_fps,
                     "QUOTIENT")
    R["controls"] = SEAL.take("controls", {
        "forced": forced,
        "maxhits_spectrum": sorted({d["maxhits"] for d in drows}),
        "refusal_control_refused": refused,
        "refusal_at": str(b_ref.refusal) if refused else None,
        "falsifier_divisions": rec_arb["divisions"],
        "falsifier_min_count": min(fld_arb.values()),
        "falsifier_fate": fal_row["fate"]})
    LD.add("G-FORCED",
           forced and refused
           and rec_arb["divisions"] == len(rec_ctrl["footprints"]) - 1
           and fal_row["fate"] in ("COUNT-DEAD", "STRUCT-DEAD"),
           "FORCEDNESS, AND BOTH NEGATIVE FATES REACHED.  Every schedule in "
           "the window is FORCED -- the builder's own maxhits is 1 at every "
           "one, so no pick in this census consults a tie-break -- and the "
           "instrument's two negative controls fire: withholding the first "
           "conflict-supply delivery makes the layer REFUSE a proposal, and "
           "withholding one division event makes the weld detector die at "
           "the count",
           "forced %s (maxhits spectrum %s of %d schedules); refusal control "
           "refused %s; the withheld-division falsifier keeps %d divisions, "
           "minimum count %d, fate %s"
           % (forced, sorted({d["maxhits"] for d in drows}), len(drows),
              refused, rec_arb["divisions"], min(fld_arb.values()),
              fal_row["fate"]))

    # ---- SEC 9  STAGE 4 -- THE DIA ROW -----------------------------------
    say("")
    say("[SEC 9] STAGE 4 -- THE DIA ROW")
    # EVERY homogeneous record the stratum reaches at every rung of the
    # ladder, derived from the code space rather than listed: the law is
    # quantified over its whole population at R = 3, 4, 5 and 6, so the two
    # LINK-CONSTANT records of the ladder -- (1,1,1) at R = 3 and (2,2,2) at
    # R = 6 -- are both in it, and "compulsion vanishes where the weld turns
    # motivated" has both of its instances rather than one.
    dia_rows = []
    dia_targets = []
    for r in LADDER:
        for c in sorted(x for x in cs[r] if min(x) >= 1 and sum(x) == r):
            dia_targets.append((c, r))
    r4targets = sorted(c for c in cs[4] if min(c) >= 1 and sum(c) == 4)
    for rec, r in dia_targets:
        W = stratum_witnesses(rec, r)
        freq = {k: sum(1 for w in W if RC["class_index"][k] in w)
                for k in CLASS_NAMES}
        comp = sorted(k for k in CLASS_NAMES if freq[k] == len(W) and W)
        naive = sorted(k for k in CLASS_NAMES if k != "ANT"
                       and rec[I7_LINKS.index(CLASS_DIR[k])] >= 2)
        predicted = naive if min(rec) == 1 else []
        dia_rows.append({"record": list(rec), "budget": r, "witnesses": len(W),
                         "multisets": len({tuple(sorted(w)) for w in W}),
                         "frequency": freq, "compulsory": comp,
                         "predicted_by_the_count_law": predicted,
                         "predicted_by_the_naive_law": naive,
                         "naive_law_holds": comp == naive,
                         "law_holds": comp == predicted})
    dia_rows = pick("M-DIA", dia_rows,
                    [dict(d, compulsory=sorted(CLASS_NAMES))
                     if d["budget"] == ROUNDS else d for d in dia_rows])
    dia_rows = pick("M-DIA-EXT", dia_rows,
                    [dict(d, compulsory=["DIA"])
                     if d["budget"] != ROUNDS and not d["compulsory"] else d
                     for d in dia_rows])
    # the undeclared direction's absence is FORCED, not found: the ANT
    # parallel class deposits no declared incidence at all, so it is not in
    # the saturating stratum and no live tuple can contain it.
    ant_inc = RC["incidences"][RC["class_index"]["ANT"]]
    p21_dia = p21["census"]["quadruples_containing_the_diagonal_class"]
    r4dia = [d for d in dia_rows if d["record"] == list(flat)][0]
    R["dia"] = SEAL.take("dia", {"rows": dia_rows,
                                 "law": "the parallel class of a link is "
                                        "compulsory exactly when the record "
                                        "counts that link more than once AND "
                                        "counts some link exactly once",
                                 "naive_law": "the parallel class of a link "
                                              "is compulsory exactly when "
                                              "the record counts that link "
                                              "more than once",
                                 "law_holds": all(d["law_holds"]
                                                  for d in dia_rows),
                                 "naive_law_holds": all(d["naive_law_holds"]
                                                        for d in dia_rows),
                                 "naive_law_counterexamples":
                                     [d["record"] for d in dia_rows
                                      if not d["naive_law_holds"]],
                                 "link_constant_rows":
                                     [d["record"] for d in dia_rows
                                      if len(set(d["record"])) == 1],
                                 "undeclared_direction": {
                                     "class": "ANT",
                                     "declared_incidences_per_round": ant_inc,
                                     "status": "FORCED, NOT MEASURED",
                                     "reason": "the ANT parallel class "
                                               "deposits no declared "
                                               "incidence at all, so it is "
                                               "not in the saturating "
                                               "stratum and no live tuple "
                                               "can contain it"},
                                 "vocabulary": {
                                     "witness": "an ordered saturating "
                                                "R-tuple whose induced record "
                                                "is the row's count vector",
                                     "compulsory": "a parallel class that "
                                                   "occurs as a round of "
                                                   "EVERY witness of the row",
                                     "multisets": "the number of distinct "
                                                  "round-multisets among the "
                                                  "row's witnesses"}})
    LD.add("G-DIA-LAW",
           all(d["compulsory"] == d["predicted_by_the_count_law"]
               for d in dia_rows)
           and not all(d["compulsory"] == d["predicted_by_the_naive_law"]
                       for d in dia_rows)
           and r4dia["frequency"]["DIA"] == p21_dia
           and r4dia["witnesses"] == p21_dia
           and all(d["frequency"]["ANT"] == 0 for d in dia_rows)
           and ant_inc == 0
           and len([d for d in dia_rows
                    if len(set(d["record"])) == 1 and not d["compulsory"]])
           == len([d for d in dia_rows if len(set(d["record"])) == 1]),
           "THE COMPULSORY CLASS IS A LAW, AND THE LAW HAS A BOUNDARY.  "
           "Every witness of every homogeneous record at R = 4, 5 and 6 is "
           "enumerated and each parallel class is counted against its own "
           "record: a class is compulsory exactly when the record counts its "
           "link more than once AND counts some link exactly once.  The "
           "count clause alone is FALSIFIED here -- at the link-constant "
           "record every link is counted twice and no class is compulsory at "
           "all -- so the compulsion is carried by the scarce link, and it "
           "vanishes at exactly the records where the weld turns motivated: "
           "BOTH link-constant records the ladder reaches, and no other row, "
           "carry no compulsory class.  The undeclared direction's absence is "
           "FORCED rather than found -- its parallel class deposits no "
           "declared incidence at all, so it is not in the stratum.  At "
           "R = 4 the census returns paper-21's own committed DIA row",
           "R=4 DIA in %d of %d witnesses (paper-21's committed %d); the "
           "law holds on %d of %d rows and the count clause alone on %d, "
           "falsified at %s; rows %s"
           % (r4dia["frequency"]["DIA"], r4dia["witnesses"], p21_dia,
              sum(1 for d in dia_rows
                  if d["compulsory"] == d["predicted_by_the_count_law"]),
              len(dia_rows),
              sum(1 for d in dia_rows
                  if d["compulsory"] == d["predicted_by_the_naive_law"]),
              [d["record"] for d in dia_rows if not d["naive_law_holds"]],
              [(str(d["record"]), d["budget"], d["witnesses"], d["compulsory"])
               for d in dia_rows]))
    for d in dia_rows:
        reg(d["witnesses"], d["multisets"])

    # ---- THE CHOICE INVENTORY, PUBLISHED AS DATA ------------------------
    wrow5 = [w for w in weld_rows if w["budget"] == ROUNDS
             and w["reading"] == "EMBEDDING"][0]
    wf = wrow5["inventory"]
    # THE TWO FIBERS THAT ARE READ AT ONE BASE MAP CARRY THEIR SPREAD WITH
    # THEM (paper-21's own disclosure, restored): the site fiber is read at
    # every base map, the label and orient fibers at the enumeration's first.
    lab_sp = wrow5["label_fiber_spread"]
    ori_sp = wrow5["orient_fiber_spread"]
    nbase = wrow5["base_maps_read"]
    base_note = ("§6, at the declared base map; spread %s across the %d - "
                 "not base-map invariant")
    inv_rows = [
        (1, "the base object: CONFLICT-GRID(3, R)", "forced", 1,
         "pin, from the committed constructor"),
        (2, "the per-round budget: %d groups of %d"
         % (len(I7_LINKS), len(I7_LINKS)), "forced", 1,
         "the committed cycle, anchored event for event at two budgets"),
        (3, "the site carrier: actors to Z_3^2", "forced", 1,
         "the constructor's own actor naming"),
        (4, "admissibility: the layer's own menu", "forced", 1,
         "d42b1 driven directly"),
        (5, "the I7 readout, links and record family", "forced", 1,
         "I7's own receipt, compared coordinate by coordinate"),
        (6, "R = %d rather than R = %d or R = %d"
         % (ROUNDS, ROUNDS - 1, ROUNDS + 1), "declared, VERDICT-DETERMINING",
         1, "the pin; both neighbours are measured in-unit"),
        (7, "the driven window W%d" % ROUNDS, "declared", 1,
         "§6.2, disclosed in the head"),
        (8, "the seed menu: the first canonical transversal, plus the "
            "declared fan", "declared", 1,
         "§6.2; the fan exercises %d x %d of it on (1, 1, 3)'s first two "
         "rounds; no exhaustive column uses it"
         % (len(canon_transversals(CLASSES["ROW"])),
            len(canon_transversals(CLASSES["ROW"])))),
        (9, "the site the local-type census is taken at", "forced", 1,
         "§2.1, by measured translation invariance"),
        (10, "the reading axis (EMBEDDING / QUOTIENT)", "declared",
         len({w["reading"] for w in weld_rows}), "weld 2's, carried unchanged"),
        (11, "I-SITE-ASSIGNMENT", "measured", wf["I-SITE-ASSIGNMENT"],
         "§6, at every arena above the floor; read at every base map"),
        (12, "I-DIRECTION-LABEL", "measured", wf["I-DIRECTION-LABEL"],
         base_note % (lab_sp, nbase)),
        (13, "I-ORIENT", "measured", wf["I-ORIENT"],
         base_note % (ori_sp, nbase)),
        (14, "the declared falsifier (one division withheld)", "free", "-",
         "a division-set edit on the driven record")]
    inv_rows = pick("M-INVENTORY", inv_rows,
                    [(a, b, c, 1 if c == "measured" else d, e)
                     for (a, b, c, d, e) in inv_rows])
    R["choice_inventory"] = SEAL.take("choice_inventory", [
        {"item": a, "name": b, "class": c, "fiber": d, "binds": e}
        for (a, b, c, d, e) in inv_rows])
    LD.add("G-INVENTORY",
           len(inv_rows) == len({r0[0] for r0 in inv_rows})
           and all(r0[3] == 1 for r0 in inv_rows if r0[2] == "forced")
           and all(r0[3] == wf[r0[1]] for r0 in inv_rows
                   if r0[2] == "measured")
           and all(r0[2] in ("forced", "declared", "measured", "free",
                             "declared, VERDICT-DETERMINING")
                   for r0 in inv_rows),
           "THE CHOICE INVENTORY IS PUBLISHED AS DATA AND ITS MEASURED ROWS "
           "ARE THE CENSUS'S OWN.  Every forced item carries fiber 1 by its "
           "own row, the declared reading axis carries the number of readings "
           "this run actually evaluates, and the three measured items are "
           "taken from this budget's own weld row rather than re-typed -- so "
           "a swapped or forged inventory row dies at the table gate",
           "items %d, forced %d, measured fibers %s"
           % (len(inv_rows),
              sum(1 for r0 in inv_rows if r0[2] == "forced"),
              [wf[k] for k in ("I-SITE-ASSIGNMENT", "I-DIRECTION-LABEL",
                               "I-ORIENT")]))

    # ---- THE PER-INVARIANT PERSISTENCE TABLE ----------------------------
    prev = str(ROUNDS - 1)
    here = str(ROUNDS)

    def weld_signature(b):
        """the rung's weld signature WITH its base map: the headline triple
        is read at one base map, so the row that claims persistence carries
        the spreads that persist with it."""
        w = [x for x in weld_rows if x["budget"] == b
             and x["reading"] == "EMBEDDING"][0]
        return ("%s at the declared base map, spreads %s and %s"
                % (w["fiber_string"], w["label_fiber_spread"],
                   w["orient_fiber_spread"]))

    persist = [
        {"invariant": "the binding constraint of the price law",
         "independence": "A THEOREM OF THE PRICE LAW",
         "at_the_rung_below": slack_rows[ROUNDS - 1]["binds"],
         "here": slack_rows[ROUNDS]["binds"],
         "witness": "slack %d against %d" % (slack_rows[ROUNDS - 1]["slack"],
                                             slack_rows[ROUNDS]["slack"])},
        {"invariant": "the saturation schema",
         "independence": "A THEOREM OF THE PRICE LAW",
         "at_the_rung_below": "every round forced to saturate",
         "here": ("every round forced to saturate"
                  if R["saturation"]["every_round_forced_to_saturate"]
                  else "not forced"),
         "witness": "%d incidences needed against a ceiling of %d"
                    % (budget, budget)},
        {"invariant": "the weld fiber signature",
         "independence": "MEASURED PER ARENA",
         "at_the_rung_below": weld_signature(ROUNDS - 1),
         "here": weld_signature(ROUNDS),
         "witness": "%d base maps read at both" % p21["counts"]["isomorphisms"]},
        {"invariant": "the fiber law (all ones iff link-constant)",
         "independence": "MEASURED PER ARENA",
         "at_the_rung_below": "holds", "here": "holds" if fiber_law
         else "fails",
         "witness": "%d arenas" % len(weld_arenas)},
        {"invariant": "cover = positive definite",
         "independence": "COROLLARY OF THE CELL-CEILING ROW",
         "at_the_rung_below": str(not [c for c in occ[ROUNDS - 1]
                                       if sig_class(c) != "POSDEF"]),
         "here": str(not occ5_bad),
         "witness": "the singular witness at %s" % (list(wit_code)
                                                    if wit_code else None)},
        {"invariant": "block quantisation (the covering class's cell ceiling)",
         "independence": "MECHANISM",
         "at_the_rung_below": str(occ4_max), "here": str(occ5_max),
         "witness": "cell counts %d against %d" % (occ4_max, occ5_max)},
        {"invariant": "the compulsory parallel class",
         "independence": "MEASURED PER RECORD",
         "at_the_rung_below": "compulsory when the link is counted more than "
                              "once",
         "here": "and only when some link is counted exactly once",
         "witness": "the link-constant record at %s witnesses"
                    % com(dia_rows[[d["record"] for d in dia_rows].index(
                        list((2, 2, 2)))]["witnesses"])},
        {"invariant": "the declared-record yield",
         "independence": "FORCED BY THE PARITY LAW",
         "at_the_rung_below": str(yields[ROUNDS - 1]["declared_yield"]),
         "here": str(yields[ROUNDS]["declared_yield"]),
         "witness": "the parity law: %d of %d declared records at an even "
                    "count sum" % (parity["declared_even"],
                                   parity["declared_total"])}]
    here_measured = [r0["here"] for r0 in persist]
    persist = pick("M-PERSIST", persist,
                   [dict(r0, here=r0["at_the_rung_below"]) for r0 in persist])
    for row in persist:
        row["verdict"] = ("PERSISTS" if row["at_the_rung_below"] == row["here"]
                          else ("TRANSFORMS"
                                if row["invariant"].startswith("the compulsory")
                                else "BREAKS-AT-R=%d" % ROUNDS))
    tally = Counter(r["verdict"] for r in persist)
    # THE TALLY COUNTS RE-MEASURED PROPOSITIONS, NOT INDEPENDENT CONTENT.
    # Each row also carries what it IS: a mechanism, a corollary of another
    # row, a theorem of the price law, a per-object measurement, or a
    # consequence of this unit's own parity law.  The break count is then
    # read out by independence rather than by arithmetic.
    breaks = [r for r in persist if r["verdict"].startswith("BREAKS")]
    bind = Counter(r["independence"] for r in breaks)
    R["persistence"] = SEAL.take("persistence", {
        "rows": persist,
        "tally": {k: v for k, v in sorted(tally.items())},
        "breaks_by_independence": {k: v for k, v in sorted(bind.items())},
        "independent_mechanisms_among_the_breaks": bind.get("MECHANISM", 0)})
    LD.add("G-PERSISTENCE",
           all(r["verdict"] in ("PERSISTS", "TRANSFORMS",
                                "BREAKS-AT-R=%d" % ROUNDS) for r in persist)
           and all((r["at_the_rung_below"] == r["here"])
                   == (r["verdict"] == "PERSISTS") for r in persist)
           and all(persist[i]["here"] == here_measured[i]
                   for i in range(len(persist)))
           and sum(tally.values()) == len(persist)
           and all(r.get("independence") for r in persist)
           and sum(bind.values()) == len(breaks)
           and bind.get("MECHANISM", 0) == 1,
           "THE PER-INVARIANT PERSISTENCE TABLE, EACH ROW DECIDED BY ITS OWN "
           "PAIR OF MEASUREMENTS.  Every invariant paper-21 delivered is "
           "re-measured here and its verdict is read off the comparison of "
           "the two values rather than assigned: a row PERSISTS exactly when "
           "the two agree, every row's value at this rung is re-checked "
           "against the census row that measured it, and every row carries "
           "the witness that decides it.  The tally counts RE-MEASURED "
           "PROPOSITIONS; each row also carries what it IS, so the breaks are "
           "read out by independence -- exactly one of them is a mechanism, "
           "and the others are that mechanism's corollary and this unit's own "
           "parity law seen from the other side",
           "rows %d, tally %s; breaks by independence %s"
           % (len(persist), {k: v for k, v in sorted(tally.items())},
              {k: v for k, v in sorted(bind.items())}))
    reg(*[v for v in tally.values()])

    # ---- SEC 10  THE INTERFERENCE CENSUS, CLOSED BY THEOREM -------------
    say("")
    say("[SEC 10] THE CENSUS NOT RUN, AND THE WALLS")
    body = paper_body(paper_text or "")
    # THE DECLARED MEASUREMENT SURFACE, ENUMERATED RATHER THAN DESCRIBED.
    # The scan is taken here, so the keys it covers are the CENSUS layer --
    # every key published up to this point, listed in the receipt so the
    # scope is data and not an adjective.  The vouching layer that follows is
    # sealed and gated separately, and the four DERIVED VERDICT SEGMENTS --
    # the highest-stakes text this unit publishes -- are derived early and
    # folded in here, so a banned reading in the head is seen by every wall.
    surface_keys = sorted(R)
    head_preview = verdict_segments(R)
    surface_keys = pick("M-SURFACE", surface_keys, surface_keys[1:])
    surface = json.dumps({k: R[k] for k in surface_keys}, sort_keys=True,
                         default=str) \
        + " " + " ".join(head_preview) \
        + " ".join(r0["statement"] + " " + str(r0["evidence"])
                   for r0 in LD.rows) \
        + " " + pick("M-PAPER-INTERFERENCE", body,
                     body + " the interference census at L = 5 carries here")
    surface = pick("M-INTERFERENCE", surface,
                   surface + " the interference census at L = 5 finds a "
                   "DDS-carrying ball on the R-ladder")
    banned_words = ("interference census at", "DDS-carrying", "Sidon at every")
    hits = [w for w in banned_words if w.lower() in surface.lower()]
    R["surface"] = SEAL.take("surface", {
        "scanned_receipt_keys": surface_keys,
        "scanned_receipt_key_count": len(surface_keys),
        "verdict_segments_included": len(head_preview),
        "gate_rows_included": len(LD.rows),
        "paper_body_included": True, "chars": len(surface),
        "scope": "the CENSUS layer of this run's receipt -- every key "
                 "published when the scan is taken, enumerated here -- "
                 "together with the four derived verdict segments, the "
                 "statement and evidence of every gate evaluated before the "
                 "scan, and the paper's own body.  The vouching layer "
                 "published after the scan is sealed and gated separately, "
                 "and the wall rows themselves necessarily quote the words "
                 "the scan bans"})
    R["interference"] = SEAL.take("interference", {
        "status": "NOT RUN -- CLOSED BY THEOREM",
        "authority": "the PER-L adjudication (v14 #228): the transport to "
                     "the R-ladder is closed by theorem, LINK being Sidon at "
                     "every L >= 3, so PER-R inherits it as a corollary and "
                     "one census is cancelled",
        "readings_in_this_run_s_surface": hits})
    LD.add("G-INTERFERENCE-CLOSED",
           not hits,
           "THE INTERFERENCE CENSUS IS NOT RUN, AND THE ABSTENTION IS "
           "MEASURED.  PER-L's adjudicated corollary closes it by theorem for "
           "the whole R-ladder, so running it here would re-derive a decided "
           "question; the gate scans this run's declared measurement surface "
           "-- the %d census keys of this run's receipt, ENUMERATED in the "
           "receipt rather than described, together with the four derived "
           "verdict segments, the statement and evidence of every gate "
           "evaluated before the scan, AND THE PAPER'S OWN BODY -- and finds "
           "no reading of it there" % len(surface_keys),
           "surface %d chars over %d enumerated receipt keys, %d verdict "
           "segments and %d gate rows (paper body %d chars of it), readings "
           "found %d" % (len(surface), len(surface_keys), len(head_preview),
                         len(LD.rows), len(body), len(hits)))

    # ---- THE WALLS -------------------------------------------------------
    ptext = paper_text if paper_text is not None else ""
    ptext = pick("M-WALL-L1", ptext, ptext + "\n\n" + BANNED_L1 + "\n")
    q11, q22, q12, _d = q_of(tuple(reached5[0]))
    named = lorentz_named(q11, q22, q12)
    reg(str(q11), str(q22), str(q12), named)
    ptext_nm = pick("M-WALL-LORENTZ", ptext,
                    ptext.replace("NAMED AND NOT READ", "read as a signature"))
    l1_present = match_needle(ptext, BANNED_L1) if ptext else False
    R["walls"] = SEAL.take("walls", {
        "L1": {"banned_sentence_present": l1_present,
               "fourth_form": "NOT TESTED HERE"},
        "BHS": {"sprinkling_grade_test": "NONE RUN",
                "reason": "these schedules are finite-valency by "
                          "construction and a Poisson sprinkling admits no "
                          "Lorentz-invariant finite-valency graph"},
        "KR": {"dimension_reading": "NONE TAKEN",
               "height_control": "NOT OWED"},
        "LORENTZ": {"form_at_this_rung": named,
                    "named_and_not_read": "NAMED AND NOT READ"
                    in (ptext_nm or "")},
        "DIAGONAL": {"reading": "a direction on a nine-site lattice"}})
    if ptext:
        LD.add("G-WALL-L1", not l1_present,
               "L-1: THE RETRACTED SENTENCE IS ABSENT FROM THE PAPER.  Order-"
               "level covariance is a fourth form outside paper 8's three "
               "and its admissibility is v11's to argue; this unit tests no "
               "such form and reproduces no retracted sentence.  The gate "
               "whitespace-normalises, ASCII-folds and strips markdown "
               "prefixes from both sides, so a line-wrapped or blockquoted "
               "injection dies too",
               "banned sentence present %s, needle %d chars"
               % (l1_present, len(BANNED_L1)), wall=True)
        LD.add("G-WALL-LORENTZ",
               "NAMED AND NOT READ" in (ptext_nm or "") and named in ptext_nm,
               "THE LORENTZIAN RESONANCE IS NAMED AND NOT READ, AND THE FORM "
               "IN THE NAMING SENTENCE IS DERIVED.  The induced form at this "
               "rung is computed from I7's own readout of the record this "
               "unit's census returns and is required to appear in the paper "
               "inside the naming sentence; the falsifier edits the paper "
               "under test rather than the gate's boolean",
               "naming sentence present %s, derived form %s present %s"
               % ("NAMED AND NOT READ" in (ptext_nm or ""), named,
                  named in ptext_nm), wall=True)
    bhs_scan = surface + " " + pick(
        "M-PAPER-BHS", body,
        body + " a sprinkling-grade Lorentz-invariance test is run here")
    LD.add("G-WALL-BHS",
           "sprinkling" not in bhs_scan.lower(),
           "BHS: NO SPRINKLING-GRADE LORENTZ-INVARIANCE TEST IS RUN, AND THE "
           "ABSTENTION IS MEASURED.  A Poisson sprinkling admits no "
           "Lorentz-invariant finite-valency graph and these schedules are "
           "finite-valency by construction, so running such a test would "
           "manufacture a false negative; the gate scans the same declared "
           "surface -- the %d enumerated census keys, the derived verdict "
           "segments, every gate row evaluated before the scan -- AND THE "
           "PAPER'S OWN BODY, every section but the wall section in which the "
           "abstention is stated, rather than declaring the abstention"
           % len(surface_keys),
           "surface %d chars over %d enumerated receipt keys, paper body %d "
           "chars, sprinkling-grade readings 0"
           % (len(surface), len(surface_keys), len(body)), wall=True)
    kr_scan = surface + " " + pick(
        "M-PAPER-KR", body,
        body + " the Myrheim-Meyer dimension estimate of this record is")
    LD.add("G-WALL-KR",
           not any(w in kr_scan.lower() for w in
                   ("myrheim", "midpoint scaling", "shatter", "dimension "
                    "estimate")),
           "KLEITMAN-ROTHSCHILD: NO DIMENSION READING IS TAKEN, SO NO HEIGHT "
           "CONTROL IS OWED.  This unit takes no chart width, no "
           "Myrheim-Meyer estimate and no shatter reading; the same declared "
           "surface -- the %d enumerated census keys, the derived verdict "
           "segments and every gate row evaluated before the scan -- is "
           "scanned for one, and so is the paper's own body"
           % len(surface_keys),
           "surface %d chars over %d enumerated receipt keys, paper body %d "
           "chars, dimension readings 0"
           % (len(surface), len(surface_keys), len(body)), wall=True)
    LD.add("G-TWO-WAY",
           len({w["fate"] for w in weld_rows}) > 1
           and {"FOUND", "UNMOTIVATED"} <= {w["fate"] for w in weld_rows}
           and fal_row["fate"] in ("COUNT-DEAD", "STRUCT-DEAD")
           and ant_row["fate"] == "STRUCT-DEAD",
           "HA REQUIREMENT 3, HONOURED: EVERY VALUE THIS DETECTOR RETURNS IS "
           "EXHIBITED IN THIS RUN.  A predicate that cannot return its other "
           "value anywhere in the declared arena is not a measurement, so "
           "FOUND, UNMOTIVATED, STRUCT-DEAD and COUNT-DEAD are each shown on "
           "a named object of this census",
           "fates exhibited %s"
           % sorted({w["fate"] for w in weld_rows}
                    | {fal_row["fate"], ant_row["fate"]}))

    # ---- EXACT ARITHMETIC ------------------------------------------------
    src = read_text(SELF, "SELF")
    tree = ast.parse(src)
    floats = [n for n in ast.walk(tree)
              if isinstance(n, ast.Constant) and isinstance(n.value, float)]
    truediv = [n for n in ast.walk(tree)
               if isinstance(n, ast.BinOp) and isinstance(n.op, ast.Div)]

    def scan(o):
        if isinstance(o, float):
            return 1
        if isinstance(o, dict):
            return sum(scan(v) for v in o.values()) + sum(scan(k) for k in o)
        if isinstance(o, (list, tuple)):
            return sum(scan(v) for v in o)
        return 0
    nfloat = scan(R)
    R["arithmetic"] = SEAL.take("arithmetic", {
        "float_literals": len(floats), "true_divisions": len(truediv),
        "floats_in_the_receipt": nfloat,
        "statement": "exact only: Python integers and fractions.Fraction"})
    LD.add("G-EXACT",
           not floats and not truediv and nfloat == 0,
           "THE ARITHMETIC IS EXACT END TO END.  An AST scan of this file "
           "finds no float literal and no true division, and a recursive "
           "type scan of the emitted receipt finds no float anywhere in it",
           "float literals %d, true divisions %d, floats in the receipt %d"
           % (len(floats), len(truediv), nfloat))

    # ---- THE READS REGISTER, WITH A CONSUMER ----------------------------
    # #46/#91: a register with a producer and no consumer vouches for
    # nothing.  Every read at run time records its category; here the whole
    # register is compared against the DECLARED set, category by category.
    reads = pick("M-READS", list(READS),
                 list(READS) + [{"path": "v14/PLAN.md", "category": "SOURCE",
                                 "sha256_12": "0" * 12}])
    cats = {}
    for r0 in reads:
        cats.setdefault(r0["category"], []).append(r0["path"])
    declared_src = sorted({s[1] for s in SOURCES})
    self_rel = os.path.relpath(SELF, REPO)
    artifacts = {os.path.relpath(OUT_JSON, REPO),
                 os.path.relpath(OUT_TXT, REPO),
                 os.path.relpath(OUT_JSON + ".tmp", REPO),
                 os.path.relpath(OUT_TXT + ".tmp", REPO)}
    cat_ok = set(cats) <= {"SOURCE", "OBJECT-UNDER-TEST", "SELF", "ARTIFACT"}
    src_ok = sorted(set(cats.get("SOURCE", []))) == declared_src
    self_ok = cats.get("SELF") == [self_rel]
    obj_ok = len(cats.get("OBJECT-UNDER-TEST", [])) == 1
    art_ok = set(cats.get("ARTIFACT", [])) <= artifacts
    R["reads"] = SEAL.take("reads", {
        "rows": reads, "by_category": {k: sorted(set(v))
                                       for k, v in sorted(cats.items())},
        "declared_categories": ["SOURCE", "OBJECT-UNDER-TEST", "SELF",
                                "ARTIFACT"],
        "declared_sources": declared_src, "self": self_rel,
        "declared_artifacts": sorted(artifacts),
        "subprocesses_invoked": 0})
    LD.add("G-READS",
           cat_ok and src_ok and self_ok and obj_ok and art_ok
           and len(cats.get("SOURCE", [])) == len(SOURCES),
           "THE SET OF RUN-TIME READS IS EXACTLY THE DECLARED SET, AND THE "
           "REGISTER THAT RECORDS IT HAS A CONSUMER.  Every read is stamped "
           "with its category as it happens -- SOURCE, OBJECT-UNDER-TEST, "
           "SELF or this run's own staged artifacts -- and the register is "
           "compared here against the declaration category by category: the "
           "SOURCE paths must be exactly the %d pinned sources, SELF must be "
           "this file, the object under test must be a single file, and no "
           "fifth category may appear.  No subprocess of any kind is invoked, "
           "so the run is correct off-tree and with no version control "
           "present" % len(SOURCES),
           "reads %d in categories %s; sources %d of %d declared %s; self %s; "
           "object under test %s; artifacts %s"
           % (len(reads), sorted(cats), len(cats.get("SOURCE", [])),
              len(SOURCES), src_ok, self_ok,
              cats.get("OBJECT-UNDER-TEST", []), sorted(cats.get("ARTIFACT",
                                                                 []))))
    return LD, SEAL, R, G, texts, src, tree, ptext, ptext_nm, weld_rows, drows


# ===========================================================================
# SECTION 12.  THE VERDICT, DERIVED AND RE-DERIVED
# ===========================================================================

def verdict_segments(R):
    """THE HEAD, BUILT FROM THE RECEIPT.  Every number is interpolated; no
    numeral, fraction or number-word is typed here."""
    S = R["sig_feed"]
    P = R["predictions"]
    A = R["prediction_a"]
    B = R["prediction_b"]
    C = R["prediction_c"]
    K = R["slack"]
    W = R["weld"]
    D = R["driven"]
    six = R["r6_door"]
    par = R["parity"]
    wit = R["singular_witness"]
    ar = R["arena"]
    lad = sorted(int(k) for k in K["buys"]["reachable_site_codes"])
    occ = K["buys"]["covering_class_codes"]
    mx = K["buys"]["covering_class_max_cell"]
    dets = K["buys"]["det4_support_size"]
    cep = K["buys"]["cover_equals_posdef"]
    keys = sorted(occ, key=int)
    seen = []
    for row in W["rows"]:
        if row["reading"] == "EMBEDDING":
            if not seen or seen[-1][0] != row["budget"]:
                seen.append((row["budget"], row["fiber_string"], row["fate"]))
    seg1 = (
        "PERR-SIG-FEED-AT-R=%d-[COVERED CODES %d = %d POSDEF + %d SINGULAR + "
        "%d INDEFINITE; THE INDEFINITE REGION OPENS HERE, AT 4det %s; "
        "COVERING-CLASS CODES %d, MAX CELL COUNT %d, 4det SUPPORT %s] -- "
        "INSIDE THE COVERING CLASS: THE SINGULAR BOUNDARY IS REACHABLE "
        "(WITNESS %s AT EXACTLY %d OF %d SITES, %d INCIDENCES, %d OF %d "
        "ROUNDS SATURATING) AND THE INDEFINITE REGION IS NOT (THE LOCKING "
        "THEOREM: "
        "NO COVERING QUINTUPLE CARRIES A CELL COUNT OF %d) -- SO "
        "COVER=POSDEF BREAKS AT R=%d AFTER HOLDING AT R=%d AND R=%d"
        "@EXHAUSTIVE-OVER-%s-ORDERED-GROUPING-QUINTUPLES -- "
        "RECORD FLOORS (BY THE LADDER LAW, THE ROWS CENSUSED OVER "
        "%d^%d AND %d^%d): G-SINGULAR R=%d, G-INDEF R=%d") % (
        S["budget"], S["covered_codes"], S["posdef"], S["singular"],
        S["indefinite"], S["indefinite_det4"], S["covering_class_codes"],
        S["covering_class_max_cell"], S["covering_class_det4_support"],
        wit["code"], len([x for x in wit["site_codes"]
                          if x == wit["code"]]), len(wit["site_codes"]),
        wit["total_incidences"], wit["saturating_rounds"], S["budget"],
        S["budget"], S["budget"],
        lad[0], lad[1], "{:,}".format(ar["family"]),
        ar["saturating"], S["g_singular_record_floor"],
        ar["saturating"], S["g_indef_record_floor"],
        S["g_singular_record_floor"], S["g_indef_record_floor"])
    seg2 = (
        "PERR-PREDICTIONS-%d-OF-%d-PASS-[(a) NO DECLARED RECORD AT COUNT-SUM "
        "%d: I7'S OWN BOX HOLDS %d ADMISSIBLE POINTS THERE, THE STRATUM "
        "REACHES ALL %d AND %d ARE DECLARED -- AND EVERY DECLARED "
        "HOMOGENEOUS RECORD OF I7'S %d HAS AN EVEN COUNT SUM, THE "
        "INTEGER-q12 SUBLATTICE, AGAINST ITS OWN BOX'S %d EVEN AND %d ODD | "
        "(b) ZERO-FREE-ITEMS IMPOSSIBLE: A LIVE R-TUPLE SPENDS %d PER ROUND "
        "OVER %d CELLS SO LINK-CONSTANCY NEEDS R=%d MOD %d, AND THE ARENA'S "
        "OWN LINK-CONSTANT CONTROL DIES STRUCT-DEAD ON %d FOREIGN PAIRS | "
        "(c) STRICTLY WEAKER IN BOTH CURRENCIES: DECLARED YIELD %d AT "
        "R=%d AND %d HERE, MOTIVATED AT NEITHER, WHILE R=%d BUYS BOTH -- AND "
        "STRICTLY RICHER IN EVERY SLACK COLUMN]") % (
        P["passed"], P["total"], sum(A["reached"][0]),
        len(A["admissible_box_points_at_this_budget"]), len(A["reached"]),
        len(A["declared_at_this_budget"]), par["declared_total"],
        par["box_even"], par["box_odd"],
        R["arena"]["max_incidences_per_round"], R["arena"]["cells"],
        B["residue"], B["modulus"], B["control_foreign_pairs"],
        C["parent_declared_yield"], C["parent_budget"],
        C["this_budget_declared_yield"], C["door_budget"])
    seg3 = (
        "PERR-SLACK-%d-AT-R=%d-[= %d(R-%d), THE PARENT'S FORMULA; BINDING=%s "
        "(%d > %d); THE SEQUENCE GAINS A ROW AND NO CONDITION] -- WHAT THE "
        "SLACK BUYS ALONG R=%s: SITE CODES %s | COVERING-CLASS CODES %s | "
        "MAX CELL COUNT %s (BLOCK QUANTISATION BREAKS) | 4det SUPPORT %s | "
        "COVER=POSDEF %s") % (
        K["slack_at_this_budget"], R["saturation"]["rounds"],
        R["arena"]["max_incidences_per_round"], K["formula_offset"],
        K["binding"],
        R["saturation"]["budget"], R["arena"]["cells"],
        "/".join(str(k) for k in keys),
        "/".join(str(K["buys"]["reachable_site_codes"][k]) for k in keys),
        "/".join(str(occ[k]) for k in keys),
        "/".join(str(mx[k]) for k in keys),
        "/".join(str(dets[k]) for k in keys),
        "/".join(str(cep[k]) for k in keys))
    seg4 = (
        "PERR-DICTIONARY-[WELD FIBERS %s, FOUND EXACTLY AT THE LINK-CONSTANT "
        "RECORDS AND UNMOTIVATED AT EVERY OTHER ARENA OF THE DECLARED "
        "DICTIONARY; THE R=%d SIGNATURE IS THE "
        "R=%d SIGNATURE] -- DRIVEN: THE COMMITTED GRAMMAR DRIVES %d "
        "SCHEDULES OVER BUDGETS %s WITH %d OF %d DRIVEN FIELDS EQUAL TO "
        "THEIR GROUPINGS' FIELD, ANCHORED AT d66's OWN COMMITTED R=%s ROWS "
        "-- THE R=%d DOOR CENSUSED EXACTLY: %s AT %s AND I7'S DECLARED "
        "G-SINGULAR AT %s ORDERED SATURATING SEXTUPLES -- DIA: A PARALLEL "
        "CLASS IS COMPULSORY EXACTLY WHEN THE RECORD COUNTS ITS LINK MORE "
        "THAN ONCE AND COUNTS SOME LINK EXACTLY ONCE, ON %d OF %d ROWS; THE "
        "COUNT CLAUSE ALONE IS FALSIFIED AT %s") % (
        " -> ".join("%s(R=%d)" % (f, b) for b, f, _fa in seen),
        seen[2][0], seen[1][0], D["schedules"],
        "/".join(str(b) for b in D["budgets"]), D["equalities"],
        D["schedules"],
        "/".join(sorted(R["driver_anchor"], key=int)),
        six["budget"], six["link_constant_record"],
        "{:,}".format(six["counts"]["(2, 2, 2)"]),
        "{:,}".format(six["counts"]["G-SINGULAR"]),
        sum(1 for d in R["dia"]["rows"] if d["law_holds"]),
        len(R["dia"]["rows"]), R["dia"]["naive_law_counterexamples"])
    return [seg1, seg2, seg3, seg4]


def reconstruct_from_serialized(text):
    """THE COMPARATOR.  It reads the SERIALIZED receipt, types all four
    verdict templates itself in its own fragments, and shares no code, no
    input object and no typed value with the builder above."""
    Z = json.loads(text)
    s, p, a, b, c = (Z["sig_feed"], Z["predictions"], Z["prediction_a"],
                     Z["prediction_b"], Z["prediction_c"])
    k, w, d = Z["slack"], Z["weld"], Z["driven"]
    six, par, wit, ar = Z["r6_door"], Z["parity"], Z["singular_witness"], \
        Z["arena"]
    ks = sorted(k["buys"]["covering_class_codes"], key=int)
    lad = sorted(int(x) for x in k["buys"]["reachable_site_codes"])
    rows = [r for r in w["rows"] if r["reading"] == "EMBEDDING"]
    seen = []
    for r in rows:
        if not seen or seen[-1][0] != r["budget"]:
            seen.append((r["budget"], r["fiber_string"]))
    j1 = ["PERR", "-SIG-FEED-AT-R=", "%d-[COVERED CODES ", "%d = ",
          "%d POSDEF + ", "%d SINGULAR + ", "%d INDEFINITE; ",
          "THE INDEFINITE REGION OPENS HERE, AT ", "4det %s; ",
          "COVERING-CLASS CODES %d, ", "MAX CELL COUNT %d, ",
          "4det SUPPORT %s] -- ", "INSIDE THE COVERING CLASS: ",
          "THE SINGULAR BOUNDARY IS REACHABLE ", "(WITNESS %s AT EXACTLY ",
          "%d OF %d SITES, %d INCIDENCES, ", "%d OF %d ROUNDS SATURATING) ",
          "AND THE INDEFINITE REGION IS NOT ", "(THE LOCKING THEOREM: ",
          "NO COVERING QUINTUPLE CARRIES A CELL COUNT OF %d) -- SO ",
          "COVER=POSDEF BREAKS AT R=%d AFTER HOLDING AT R=%d ",
          "AND R=%d", "@EXHAUSTIVE-OVER-%s", "-ORDERED-GROUPING",
          "-QUINTUPLES -- RECORD FLOORS (BY THE LADDER LAW, ",
          "THE ROWS CENSUSED OVER %d^%d AND %d^%d): ", "G-SINGULAR R=%d, ",
          "G-INDEF R=%d"]
    seg1 = "".join(j1) % (
        s["budget"], s["covered_codes"], s["posdef"], s["singular"],
        s["indefinite"], s["indefinite_det4"], s["covering_class_codes"],
        s["covering_class_max_cell"], s["covering_class_det4_support"],
        wit["code"], len([x for x in wit["site_codes"]
                          if x == wit["code"]]), len(wit["site_codes"]),
        wit["total_incidences"], wit["saturating_rounds"], s["budget"],
        s["budget"], s["budget"], lad[0], lad[1],
        "{:,}".format(ar["family"]), ar["saturating"],
        s["g_singular_record_floor"], ar["saturating"],
        s["g_indef_record_floor"], s["g_singular_record_floor"],
        s["g_indef_record_floor"])
    j2 = ["PERR", "-PREDICTIONS-%d", "-OF-%d-PASS-[", "(a) NO DECLARED ",
          "RECORD AT COUNT-SUM %d: ", "I7'S OWN BOX HOLDS %d ",
          "ADMISSIBLE POINTS THERE, ", "THE STRATUM REACHES ALL %d ",
          "AND %d ARE DECLARED -- AND ", "EVERY DECLARED HOMOGENEOUS ",
          "RECORD OF I7'S %d HAS AN ", "EVEN COUNT SUM, THE ",
          "INTEGER-q12 SUBLATTICE, ", "AGAINST ITS OWN BOX'S %d EVEN ",
          "AND %d ODD | (b) ZERO-FREE-ITEMS ", "IMPOSSIBLE: A LIVE R-TUPLE ",
          "SPENDS %d PER ROUND OVER %d CELLS ", "SO LINK-CONSTANCY NEEDS ",
          "R=%d MOD %d, AND THE ARENA'S OWN ", "LINK-CONSTANT CONTROL DIES ",
          "STRUCT-DEAD ON %d FOREIGN PAIRS | ", "(c) STRICTLY WEAKER IN ",
          "BOTH CURRENCIES: DECLARED YIELD %d ", "AT R=%d AND %d HERE, ",
          "MOTIVATED AT NEITHER, WHILE ", "R=%d BUYS BOTH -- AND STRICTLY ",
          "RICHER IN EVERY SLACK COLUMN]"]
    seg2 = "".join(j2) % (
        p["passed"], p["total"], sum(a["reached"][0]),
        len(a["admissible_box_points_at_this_budget"]), len(a["reached"]),
        len(a["declared_at_this_budget"]), par["declared_total"],
        par["box_even"], par["box_odd"], ar["max_incidences_per_round"],
        ar["cells"], b["residue"], b["modulus"], b["control_foreign_pairs"],
        c["parent_declared_yield"], c["parent_budget"],
        c["this_budget_declared_yield"], c["door_budget"])
    j3 = ["PERR", "-SLACK-%d-AT-R=%d-[= ", "%d(R-%d), THE PARENT'S FORMULA; ",
          "BINDING=%s (%d > %d); ", "THE SEQUENCE GAINS A ROW AND NO ",
          "CONDITION] -- WHAT THE SLACK BUYS ALONG R=%s: ", "SITE CODES %s | ",
          "COVERING-CLASS CODES %s | ", "MAX CELL COUNT %s ",
          "(BLOCK QUANTISATION BREAKS) | ", "4det SUPPORT %s | ",
          "COVER=POSDEF %s"]
    seg3 = "".join(j3) % (
        k["slack_at_this_budget"], Z["saturation"]["rounds"],
        ar["max_incidences_per_round"], k["formula_offset"], k["binding"],
        Z["saturation"]["budget"], ar["cells"],
        "/".join(str(x) for x in ks),
        "/".join(str(k["buys"]["reachable_site_codes"][x]) for x in ks),
        "/".join(str(k["buys"]["covering_class_codes"][x]) for x in ks),
        "/".join(str(k["buys"]["covering_class_max_cell"][x]) for x in ks),
        "/".join(str(k["buys"]["det4_support_size"][x]) for x in ks),
        "/".join(str(k["buys"]["cover_equals_posdef"][x]) for x in ks))
    j4 = ["PERR", "-DICTIONARY-[WELD FIBERS %s, ", "FOUND EXACTLY AT THE ",
          "LINK-CONSTANT RECORDS AND UNMOTIVATED ",
          "AT EVERY OTHER ARENA OF THE DECLARED DICTIONARY; ",
          "THE R=%d SIGNATURE IS THE R=%d SIGNATURE] ", "-- DRIVEN: THE ",
          "COMMITTED GRAMMAR DRIVES %d SCHEDULES ", "OVER BUDGETS %s WITH ",
          "%d OF %d DRIVEN FIELDS EQUAL TO ", "THEIR GROUPINGS' FIELD, ",
          "ANCHORED AT d66's OWN COMMITTED R=%s ROWS -- ",
          "THE R=%d DOOR CENSUSED EXACTLY: %s AT %s ",
          "AND I7'S DECLARED G-SINGULAR AT %s ", "ORDERED SATURATING ",
          "SEXTUPLES -- DIA: A PARALLEL CLASS IS ",
          "COMPULSORY EXACTLY WHEN THE RECORD COUNTS ",
          "ITS LINK MORE THAN ONCE AND COUNTS SOME LINK ",
          "EXACTLY ONCE, ON %d OF %d ROWS; THE COUNT ",
          "CLAUSE ALONE IS FALSIFIED AT %s"]
    seg4 = "".join(j4) % (
        " -> ".join(("%s" + "(R=" + "%d)") % (f, bb) for bb, f in seen),
        seen[2][0], seen[1][0], d["schedules"],
        "/".join(str(x) for x in d["budgets"]), d["equalities"],
        d["schedules"], "/".join(sorted(Z["driver_anchor"], key=int)),
        six["budget"], six["link_constant_record"],
        "{:,}".format(six["counts"]["(2, 2, 2)"]),
        "{:,}".format(six["counts"]["G-SINGULAR"]),
        len([r for r in Z["dia"]["rows"] if r["law_holds"]]),
        len(Z["dia"]["rows"]), Z["dia"]["naive_law_counterexamples"])
    return [seg1, seg2, seg3, seg4]


# ===========================================================================
# SECTION 13.  THE PAPER GATES
# ===========================================================================

def paper_claims(R):
    """every headline sentence of the paper, RENDERED FROM THE RECEIPT."""
    S, K, D = R["sig_feed"], R["slack"], R["driven"]
    A, B, C = R["prediction_a"], R["prediction_b"], R["prediction_c"]
    wit, six = R["singular_witness"], R["r6_door"]
    par, ar = R["parity"], R["arena"]
    occ = R["covering_codes"]
    cl = {"sig_split":
          "%d covered site codes at this budget: %d positive definite, %d "
          "singular and %d indefinite"
          % (S["covered_codes"], S["posdef"], S["singular"],
             S["indefinite"]),
          "sig_opens":
          "the indefinite region opens at R = %d" % S["indefinite_opens_at"],
          "sig_covering":
          "%d of the %d covered codes occur at a site of a covering "
          "quintuple" % (S["covering_class_codes"], S["covered_codes"]),
          "class_ladder":
          "the indefinite region is attained at "
          + ", ".join(
              "R = %s as %s %s"
              % ([r0[c0["class"]] for r0 in R["reachability_ladder"]["rows"]
                  if r0["polarity"] == "INDEFINITE"][0],
                 "an" if c0["label"][0].upper() in "AEIOU" else "a",
                 c0["label"])
              for c0 in R["reachability_ladder"]["class_rows"]
              if c0["kind"] == "CHAIN"),
          "sig_break":
          "the covering class and the positive-definite class coincide at "
          "R = 3 and at R = 4 and part company at R = 5",
          "locking":
          "no covering quintuple carries a cell count of %d"
          % R["locking"]["budget"],
          "witness":
          "one covering quintuple with %d incidences, %d of its five rounds "
          "saturating, and exactly one singular site"
          % (wit["total_incidences"], wit["saturating_rounds"]),
          "maxcell":
          "the covering class's maximum cell count is %d at R = 4 and %d "
          "here" % (occ["4"]["max_cell"], occ[str(R["saturation"]["rounds"])]
                    ["max_cell"]),
          "parity":
          "all %d of I7's homogeneous declared records carry an even count "
          "sum, while its own admissible box splits %d even and %d odd"
          % (par["declared_total"], par["box_even"], par["box_odd"]),
          "pred_a":
          "I7's box holds %d admissible count vectors summing to %d, the "
          "stratum reaches every one of them, and %d are declared"
          % (len(A["admissible_box_points_at_this_budget"]),
             sum(A["reached"][0]), len(A["declared_at_this_budget"])),
          "pred_b":
          "a link-constant field needs 27 to divide 9R, so R must be "
          "divisible by %d" % B["modulus"],
          "pred_b_control":
          "the link-constant control at this budget dies STRUCT-DEAD on %d "
          "foreign pairs" % B["control_foreign_pairs"],
          "pred_c":
          "the declared-record yield is %d at R = %d and %d here, and %d at "
          "R = %d" % (C["parent_declared_yield"], C["parent_budget"],
                      C["this_budget_declared_yield"],
                      C["rows"][str(C["door_budget"])]["declared_yield"],
                      C["door_budget"]),
          "slack":
          "the slack is %d = 9(R - 3) and what binds is %s"
          % (K["slack_at_this_budget"], K["binding"].lower()),
          "stratum":
          "%s of the %s ordered saturating quintuples cover all 27 cells"
          % (com(R["stratum"][str(R["saturation"]["rounds"])]["cover"]),
             com(R["stratum"][str(R["saturation"]["rounds"])]["total"])),
          "r6":
          "(2, 2, 2) at %s ordered saturating sextuples and G-SINGULAR at %s"
          % (com(six["counts"]["(2, 2, 2)"]),
             com(six["counts"]["G-SINGULAR"])),
          "driven":
          "%d schedules driven over budgets %s, with %d of %d driven fields "
          "equal to their groupings' field"
          % (D["schedules"], ", ".join(str(b) for b in D["budgets"]),
             D["equalities"], D["schedules"]),
          "dia":
          "a parallel class is compulsory exactly when the record counts its "
          "link more than once and counts some link exactly once, and the "
          "count clause alone is falsified at the link-constant record",
          "persistence":
          "%d invariants re-measured: %s"
          % (len(R["persistence"]["rows"]),
             ", ".join("%d %s" % (v, k) for k, v in
                       sorted(R["persistence"]["tally"].items()))),
          "arena":
          "%d partitions, %d of them saturating, and a family of %s"
          % (ar["partitions"], ar["saturating"], com(ar["family"]))}
    # the determinant support, rendered so the sentence that carries it is a
    # claim rather than a gap between two claims
    cl["det_support"] = ("the determinant support is {%s}"
                         % ", ".join(str(x) for x in
                                     S["covering_class_det4_support"]))
    cl["indefinite_codes"] = (
        "the indefinite region opens at R = %d, at %d codes, %s and %s, every "
        "one of them at 4det = %s"
        % (S["indefinite_opens_at"], S["indefinite"],
           ", ".join("(%s)" % ", ".join(str(y) for y in x)
                     for x in S["indefinite_codes"][:-1]),
           "(%s)" % ", ".join(str(y) for y in S["indefinite_codes"][-1]),
           ", ".join(str(x) for x in S["indefinite_det4"])))
    cl["locking_cells"] = (
        "it never reaches all %d cells: no covering quintuple carries a cell "
        "count of %d" % (ar["cells"], R["locking"]["budget"]))
    cl["pred_b_arith"] = (
        "a structurally live R-tuple spends %d incidences a round over %d "
        "cells, so a field constant on all three links needs %d to divide 9R"
        % (ar["max_incidences_per_round"], ar["cells"], ar["cells"]))
    cl["slack_binds"] = ("%d incidences over %d cells"
                         % (R["saturation"]["budget"], ar["cells"]))
    cl["stratum_fields"] = (
        "the stratum as a whole induces %s distinct fields, while its "
        "covering subset induces %s"
        % (com(R["stratum_fields"]["whole_stratum"][str(
            R["saturation"]["rounds"])]),
           com(R["stratum_fields"]["covering_subset"][str(
               R["saturation"]["rounds"])])))
    cl["r6_bound"] = ("a constructive lower bound of %s"
                      % com(six["parent_constructive_lower_bound"]))
    # the ceiling continuation, the locking general form and the bare-live
    # control -- the three promotions, each rendered from its own row
    ce = R["covering_ceiling"]
    cl["ceiling"] = (
        "the covering class's maximum cell count runs %s along R = %s, and at "
        "R = %d the covering class holds %d codes"
        % (", ".join(str(x) for x in ce["sequence"]),
           ", ".join(str(c0["budget"]) for c0 in ce["rows"]),
           ce["rows"][-1]["budget"], ce["rows"][-1]["covering_class_codes"]))
    lg = R["locking_general"]
    cl["lock_general"] = (
        "the cells at those two sites demand the same %s distinct third "
        "members at every budget, so the obstruction holds at every budget "
        "below %d and dissolves at exactly R = %d"
        % (", ".join(str(x) for x in lg["third_members_required"]),
           lg["obstruction_dissolves_at"], lg["obstruction_dissolves_at"]))
    cl["min_uncovered"] = (
        "a locked quintuple leaves %d of the %d cells uncovered"
        % (lg["min_uncovered_at_this_budget"], ar["cells"]))
    lc = R["live_control"]
    cl["live_control"] = (
        "an R = %d record all of whose %d rounds saturate, carrying no "
        "foreign pair, whose site code at the origin is (%s) at 4det %d, and "
        "which covers only %d of the %d cells"
        % (lc["budget"], lc["saturating_rounds"],
           ", ".join(str(x) for x in lc["site_code_at_the_origin"]),
           lc["det4_at_the_origin"], lc["cells_covered"], lc["cells"]))
    cl["live_floors"] = (
        "dropped to liveness alone, without the covering condition, the "
        "floors are %d and %d"
        % (lc["floors"]["SINGULAR"], lc["floors"]["INDEFINITE"]))
    # the window, by parts
    wd = R["window"]
    cl["window"] = (
        "the window is %d schedules: %s"
        % (wd["schedules"],
           ", ".join("%d %s" % (w["schedules"], w["tag"])
                     for w in wd["rows"])))
    cl["ladder_members"] = (
        "the collinear arrangement of every homogeneous record the R = %d "
        "stratum reaches, all %d of them, none sampled"
        % (R["saturation"]["rounds"],
           [w["schedules"] for w in wd["rows"] if w["tag"] == "W5-LADDER"][0]))
    cl["seed_fan"] = (
        "the fan enumerates %d canonical transversal choices and contributes "
        "%d schedules, because one of the %d is the W5-LADDER member of "
        "(1, 1, 3)" % (wd["seed_fan"]["choices"], wd["seed_fan"]["fresh"],
                       wd["seed_fan"]["choices"]))
    # the two §13 counts that were typed prose
    cl["sources"] = ("%d sources are read at run time"
                     % R["provenance"]["count"])
    cl["back_validation"] = ("%d columns are back-validated"
                             % len(BACK_VALIDATED))
    # G-INDEF's own budget, censused rather than asserted
    rr = R["record_realizability"]["rows"]
    cl["indef_record"] = (
        "I7's own G-INDEF arrives as a whole record at R = %d, at %s ordered "
        "saturating octuples" % (rr["G-INDEF"]["budget"],
                                 com(rr["G-INDEF"]["witnesses"])))
    # the class definitions, DERIVED from the predicate each floor is
    # computed with (the #294 ruling: a class-explicit row is only
    # class-explicit if its printed words are its computed predicate)
    for c0 in R["reachability_ladder"]["class_rows"]:
        art = "an" if c0["label"][0].upper() in "AEIOU" else "a"
        cl["class_%s" % c0["class"]] = ("%s %s %s" % (art, c0["label"].upper(),
                                                      c0["predicate"]))
    # the persistence read-out, by independence rather than by arithmetic
    pr = R["persistence"]
    cl["persistence"] = (
        "%d invariants re-measured: %s; of the breaks %s"
        % (len(pr["rows"]),
           ", ".join("%d %s" % (v, k) for k, v in sorted(pr["tally"].items())),
           ", ".join("%d %s" % (v, k.lower())
                     for k, v in sorted(pr["breaks_by_independence"].items()))))
    return cl


def paper_table_blocks(R):
    """THE PAPER'S MEASUREMENT TABLES, HEADERS AND ALL.  A table's header row
    is the row that says what its numbers ARE, so it is a claim exactly as
    its data rows are, and it is RENDERED from the receipt rather than left
    to the prose.  Every class-naming header is derived from the predicate
    its column's number was computed with, so swapping two of them is a
    claim about a predicate this file does not compute."""
    blocks = []
    occ = R["covering_codes"]
    K = R["slack"]["buys"]
    blocks.append((
        "the code space and the covering class",
        ("R", "site codes", "covering-class codes", "max cell count",
         "every covering-class code positive definite"),
        ["| %s | %s | %s | %s | %s |"
         % (r, K["reachable_site_codes"][r], occ[r]["count"],
            occ[r]["max_cell"],
            "yes" if K["cover_equals_posdef"][r] else "**no**")
         for r in sorted(occ, key=int)]))
    ce = R["covering_ceiling"]
    blocks.append((
        "the cell ceiling, continued",
        ("budget", "covering-class codes", "max cell count", "4det support"),
        ["| %s | %s | %s | %s |"
         % (c0["budget"], c0["covering_class_codes"], c0["max_cell"],
            "{%s}" % ", ".join(str(x) for x in c0["det4_support"]))
         for c0 in ce["rows"]]))
    lg = R["locking_general"]
    blocks.append((
        "the locking obstruction, budget by budget",
        ("budget", "third members required", "rounds available",
         "best coverage", "minimum uncovered", "covering reachable"),
        ["| %s | %s | %s | %s | %s | %s |"
         % (b["budget"], b["third_members_required"], b["budget"],
            b["best_coverage"], b["min_uncovered"], b["covering_reachable"])
         for b in lg["ladder"]]))
    rr = R["record_realizability"]["rows"]
    blocks.append((
        "the record floors",
        ("record", "counts", "budget", "class", "witnesses at that budget"),
        ["| %s | %s | %s | %s | %s |"
         % (nm, R["sig_feed"]["record_floors"][nm]["record"],
            R["sig_feed"]["record_floors"][nm]["budget"],
            R["sig_feed"]["record_floors"][nm]["class"],
            com(rr[nm]["witnesses"]) if rr[nm]["censused"]
            else "beyond this census")
         for nm in sorted(R["sig_feed"]["record_floors"])]))
    cls = R["reachability_ladder"]["class_rows"]
    blocks.append((
        "the reachability ladder",
        tuple(["polarity"] + [c["label"] for c in cls]),
        ["| %s | %s |" % (row["polarity"],
                          " | ".join(str(row[c["class"]]) for c in cls))
         for row in R["reachability_ladder"]["rows"]]))
    blocks.append((
        "the weld along the ladder",
        ("arena", "budget", "fibers (site/label/orient)", "fate",
         "link-constant"),
        ["| %s | %s | %s | %s | %s |"
         % (row["arena"], row["budget"],
            "/".join(str(row["inventory"][k]) for k in
                     ("I-SITE-ASSIGNMENT", "I-DIRECTION-LABEL", "I-ORIENT")),
            row["fate"], "yes" if row["link_constant"] else "no")
         for row in R["weld"]["rows"] if row["reading"] == "EMBEDDING"]))
    blocks.append((
        "the declared driven window",
        ("tag", "schedules", "budgets"),
        ["| %s | %s | %s |" % (w["tag"], w["schedules"],
                               ", ".join(str(b) for b in w["budgets"]))
         for w in R["window"]["rows"]]))
    blocks.append((
        "the compulsory parallel classes",
        ("record", "budget", "witnesses", "compulsory classes", "multisets"),
        ["| %s | %s | %s | %s | %s |"
         % (row["record"], row["budget"], com(row["witnesses"]),
            ", ".join(row["compulsory"]) or "none", row["multisets"])
         for row in R["dia"]["rows"]]))
    blocks.append((
        "the choice inventory",
        ("#", "item", "class", "fiber", "where it binds"),
        ["| %s | %s | %s | %s | %s |"
         % (row["item"], row["name"], row["class"], row["fiber"],
            row["binds"]) for row in R["choice_inventory"]]))
    blocks.append((
        "the persistence table",
        ("invariant", "at the rung below", "here", "verdict", "independence"),
        ["| %s | %s | %s | %s | %s |"
         % (row["invariant"], row["at_the_rung_below"], row["here"],
            row["verdict"], row["independence"])
         for row in R["persistence"]["rows"]]))
    return blocks


def paper_tables(R):
    """every rendered row of every measurement table -- HEADER ROWS INCLUDED
    (E-22: a table row is a claim, and the header row is the claim that says
    what the other rows are)."""
    rows = []
    for _name, header, data in paper_table_blocks(R):
        rows.append("| " + " | ".join(str(h) for h in header) + " |")
        rows.extend(data)
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
            for m in re.findall(
                    r"(?<![0-9A-Za-z])\d[\d,]*(?![0-9A-Za-z])", o):
                out.add(m)
        elif isinstance(o, dict):
            for k, v in o.items():
                walk(k)
                walk(v)
        elif isinstance(o, (list, tuple)):
            for v in o:
                walk(v)
    walk(R)
    return out


EXEMPT = [
    ("29", "this paper's own number"),
    ("14", "the corpus version v14 in paths and citations"),
    ("13", "the corpus version v13 in the I7 citation path"),
    ("11", "the corpus version v11 in the wall citations"),
    ("10", "the corpus version v10 in the committed-layer paths"),
    ("233", "this unit's pin ledger number"),
    ("228", "the PER-L adjudication's ledger number"),
    ("211", "the paper-21 adjudication's ledger number"),
    ("232", "the ledger number at which paper-21 went terminal"),
    ("19", "paper-19's number in citations"),
    ("21", "paper-21's number in citations"),
    ("28", "paper-28's number in the PER-L citation"),
    ("24", "paper-24's number in the SIG citation"),
    ("87", "the engraved discipline #87 cited in the instrument section"),
    ("82", "the engraved CLI contract #82"),
    ("91", "the engraved no-moving-refs discipline #91"),
    ("119", "the engraved gate-to-disk seal #119"),
    ("125", "the engraved text-gate discipline #125"),
    ("15", "RUNBOOK section 15, the declared-arena discipline"),
    ("22", "the E-22 engraving"),
    ("23", "the E-23 engraving"),
    ("34", "the engraved honest-denominator discipline #34"),
    ("62", "the #62 verbatim-anchor discipline"),
    ("148", "the seal-totality addendum's ledger number"),
    ("20", "the #20 paper-coverage discipline"),
    ("46", "the #46 provenance discipline"),
    ("2026", "the year the L-1 sentence was retracted, a date in the wall "
             "section rather than a measurement"),
]


def fold_numwords(text):
    """SPELLED NUMERALS COMPOSED, NOT DECOMPOSED.  `forty-two` is 42, not 40
    beside 2, and `two hundred` is 200: a compound whose PARTS are both
    receipt-backed but whose VALUE is not would otherwise pass the word
    scanner.  Only genuine compounds -- two or more number-words joined by a
    hyphen or a single space -- are returned, so the single-word scan and its
    count are untouched."""
    pat = "|".join(sorted(WORDNUM, key=len, reverse=True))
    out = []
    for m in re.finditer(r"\b(?:%s)(?:[- ](?:%s))+\b" % (pat, pat), text,
                         re.I):
        parts = [p.lower() for p in re.split(r"[- ]", m.group())]
        total, cur = 0, 0
        for p in parts:
            v = WORDNUM[p]
            if v >= 100:
                cur = (cur or 1) * v
                total += cur
                cur = 0
            else:
                cur += v
        out.append((m.group(), total + cur))
    return out


SENTENCE_NAMES = (
    ("S-1", "this unit's own successor-register row, a name"),
    ("S-2", "this unit's own successor-register row, a name"),
    ("S-3", "this unit's own successor-register row, a name"),
    ("S-4", "this unit's own successor-register row, a name"),
    ("L-1", "the retracted lemma's name"),
    ("AG(2,3)", "the committed affine plane's name"),
    ("Z_3^2", "the site lattice's name"),
    ("R6a", "a committed unit's name"),
    ("R6b", "a committed unit's name"),
    ("CR-B", "a committed unit's name"),
    ("d42b1", "the committed transport layer's name"),
    ("d60", "a committed layer's name"),
    ("d66", "the committed constructor's name"),
    ("I7", "the parent unit's name"),
    ("W4-ANCHOR", "a declared window tag"),
    ("W5-LADDER", "a declared window tag"),
    ("W5-SEEDFAN", "a declared window tag"),
    ("W5-CTRL", "a declared window tag"),
    ("W6-DOOR", "a declared window tag"),
    ("W6-CTRL", "a declared window tag"),
    ("W5", "the declared window's name"),
    ("E-22", "an engraving's name"),
    ("E-23", "an engraving's name"),
    ("E-24", "an engraving's name"),
    ("4det", "this instrument's name for four times the determinant"),
    ("q12", "I7's own name for the off-diagonal entry"),
    ("G3-", "I7's d = 3 record family prefix, a name"),
)


def prose_sentences(text):
    """the paper's PROSE, split into sentences: fenced blocks and table rows
    are gated elsewhere (by multiset and row equality respectively) and are
    cut out here so a sentence is a sentence."""
    keep, infence = [], False
    for ln in text.split("\n"):
        if ln.startswith("```"):
            infence = not infence
            continue
        if infence:
            continue
        t = ln.strip()
        if t.startswith("|") and t.endswith("|"):
            continue
        keep.append(ln)
    out = []
    for para in re.split(r"\n\s*\n", "\n".join(keep)):
        p = re.sub(r"\s+", " ", para).strip()
        if not p:
            continue
        for s in re.split(r"(?<=[.!?])\s+(?=[A-Z*`\(\[\"])", p):
            if s.strip():
                out.append(s.strip())
    return out


def sentence_referents(R, text, claims):
    """SENTENCE-LEVEL REFERENT BINDING (v14 #293's engraving, one universe
    per sentence).  A numeral in a sentence that carries a rendered claim
    belongs to that claim's census; a numeral sitting in the connective
    tissue BETWEEN two rendered claims belongs to nothing, and that is
    exactly where a true-looking false relation lives -- every numeral true,
    the relation forged.  Here every sentence that carries at least one
    rendered claim is required to carry NO numeral outside the claims it
    carries, so a numeral appended to a claim's sentence has no referent and
    dies."""
    exempt = {e[0] for e in EXEMPT}
    names = [norm(nm) for nm, _why in SENTENCE_NAMES]

    def denamed(t):
        t = norm(t)
        for nm in names:
            t = t.replace(nm, " ")
        return t
    nclaims = [(k, denamed(v)) for k, v in sorted(claims.items())
               if denamed(v).strip()]
    loose, checked = [], 0
    for s in prose_sentences(text):
        ns = denamed(s)
        spans, carried = [], []
        for k, nv in nclaims:
            i = ns.find(nv)
            if i >= 0:
                spans.append((i, i + len(nv)))
                carried.append(k)
        if not carried:
            continue
        checked += 1
        for m in re.finditer(r"(?<![0-9A-Za-z])\d[\d,]*(?:/\d+)?"
                             r"(?![0-9A-Za-z])", ns):
            tok = m.group().rstrip(",")
            end = m.start() + len(tok)
            if any(a <= m.start() and end <= b for a, b in spans):
                continue
            if tok in exempt or tok.replace(",", "") in exempt:
                continue
            loose.append({"numeral": tok, "claims": carried,
                          "sentence": ns[:160]})
    # THE RESIDUE.  The sentence rule above binds the sentences that carry a
    # referent.  A numeral standing in a sentence that carries NONE is backed
    # by the receipt-wide bag alone -- true of SOME census, of no stated one
    # -- and that is the whole breadth of the allow-list, published here as a
    # number instead of left implicit.  A paper whose residue is empty cannot
    # carry a borrowed numeral anywhere in its prose.
    reg = set(NUMREG)
    bag = receipt_numbers(R)
    nclaim_txt = [nv for _k, nv in nclaims]
    residue = []
    for s in prose_sentences(text):
        ns = denamed(s)
        spans = [(ns.find(nv), ns.find(nv) + len(nv))
                 for nv in nclaim_txt if nv in ns]
        for m in re.finditer(r"(?<![0-9A-Za-z])\d[\d,]*(?:/\d+)?"
                             r"(?![0-9A-Za-z])", ns):
            tok = m.group().rstrip(",")
            flat = tok.replace(",", "")
            if any(a <= m.start() and m.start() + len(tok) <= b
                   for a, b in spans):
                continue
            if tok in exempt or flat in exempt or tok in reg or flat in reg:
                continue
            if tok in bag or flat in bag:
                residue.append({"numeral": tok, "sentence": ns[:120]})
    wresidue = []
    for w in sorted({x.lower() for x in
                     re.findall(r"\b(%s)\b" % "|".join(WORDNUM), text, re.I)}):
        v = str(WORDNUM[w])
        if v in exempt or v in reg:
            continue
        if v in bag:
            wresidue.append({"word": w, "value": v})
    return {"sentences_scanned": len(prose_sentences(text)),
            "sentences_carrying_a_claim": checked,
            "loose_numerals": loose,
            "residue_numerals": residue,
            "residue_number_words": wresidue,
            "residue_ceiling": 0,
            "declared_names": len(SENTENCE_NAMES)}


def paper_body(text):
    """THE PAPER MINUS ITS WALL SECTION.  The reading walls are scanned
    against the body, because a wall section that NAMES an abstention must
    not be read as taking it -- and every other section must not take it
    either."""
    m = re.search(r"\n## \d+\. The walls\n", text)
    if not m:
        return text
    n = re.search(r"\n## ", text[m.end():])
    cut = m.end() + (n.start() if n else len(text))
    return text[:m.start()] + text[cut:]


def markdown_table_rows(text):
    out = []
    for line in text.split("\n"):
        t = line.strip()
        if t.startswith("|") and t.endswith("|") and set(t) - set("|-: "):
            out.append(re.sub(r"\s+", " ", t))
    return out


def fenced_blocks(text):
    """every fenced block of the paper, as a MULTISET (E-22): a containment
    test passes a forged twin, an equality of multisets does not."""
    return [re.sub(r"\s+", " ", b).strip()
            for b in re.findall(r"```[^\n]*\n(.*?)```", text, re.S)]


def paper_coverage(R, text):
    """#20 + E-22: EVERY numeral in the paper -- prose, tables, INLINE CODE
    SPANS and the fenced verdict blocks -- is scanned against exactly three
    declared lists."""
    allowed = set(NUMREG) | receipt_numbers(R) | {e[0] for e in EXEMPT}
    for v in list(allowed):
        if v.isdigit():
            allowed.add("{:,}".format(int(v)))
            allowed.add(v.replace(",", ""))
    seen = re.findall(r"(?<![0-9A-Za-z])\d[\d,]*(?:/\d+)?(?![0-9A-Za-z])",
                      text)
    bad = []
    for tok in seen:
        t = tok.replace(",", "")
        if tok in allowed or t in allowed:
            continue
        if "/" in tok:
            a, b = tok.split("/")
            if (str(Fraction(int(a.replace(",", "")), int(b))) in allowed
                    or (a.replace(",", "") in allowed and b in allowed)):
                continue
        bad.append(tok)
    words = re.findall(r"\b(%s)\b" % "|".join(WORDNUM), text, re.I)
    badw = [w for w in words if str(WORDNUM[w.lower()]) not in allowed]
    comp = fold_numwords(text)
    badc = sorted({t for t, v in comp if str(v) not in allowed})
    fired = {}
    for lit, _why in EXEMPT:
        fired[lit] = len(re.findall(r"\b%s\b" % re.escape(lit), text))
    return {"numerals_scanned": len(seen), "unbacked": sorted(set(bad)),
            "number_words_scanned": len(words), "unbacked_words":
            sorted(set(w.lower() for w in badw)),
            "compound_number_words": len(comp),
            "unbacked_compounds": badc,
            "exemptions": len(EXEMPT),
            "exemptions_fired": sum(1 for v in fired.values() if v),
            "chars_scanned": len(text)}


def paper_polarity(R, text):
    """the paper's POLARITY claims, each bound to the receipt row that
    decides it: a claim must be present exactly when its row says so."""
    S = R["sig_feed"]
    rows = [
        ("cover-posdef breaks", "part company at R = 5",
         not S["cover_implies_posdef_at_r5"]),
        ("indefinite unreachable inside the covering class",
         "the indefinite region is unreachable inside the covering class",
         not S["covering_class_indefinite_reachable"]),
        ("singular reachable inside the covering class",
         "the singular boundary is reachable inside the covering class",
         S["covering_class_singular_reachable"]),
        ("prediction a", "Prediction (a) PASSES",
         R["prediction_a"]["verdict"] == "PASS"),
        ("prediction b", "Prediction (b) PASSES",
         R["prediction_b"]["verdict"] == "PASS"),
        ("prediction c", "Prediction (c) PASSES",
         R["prediction_c"]["verdict"] == "PASS"),
        ("block quantisation breaks",
         "block quantisation does not survive the slack",
         R["covering_codes"][str(R["saturation"]["rounds"])]["max_cell"]
         > R["covering_codes"]["4"]["max_cell"]),
        ("the grammar drives the concatenation",
         "the committed grammar drives it",
         max(R["driven"]["budgets"]) > R["saturation"]["rounds"]),
    ]
    out = []
    for name, needle, should in rows:
        present = match_needle(text, needle)
        out.append({"claim": name, "needle_chars": len(needle),
                    "present": present, "should_be_present": bool(should),
                    "ok": present == bool(should)})
    return out


def waiver_ledger(names, mutants_for_gate):
    """#34: every gate is either falsified by a declared mutant or waived
    with a machine-checked forcing that says why it cannot fail.  `names` is
    the run's WHOLE gate set -- the ledger rows plus the closing gates that
    are evaluated after the ledger is snapshotted -- so the denominator is
    the run's own and not the subset standing when this is called."""
    waivers = {
        "G-SOURCES": "falsified by --break-anchor, which the selftest runs",
        "G-TRANSLATION": "a pure identity over the 2,520 translation-"
                         "partition pairs; its falsifier is the census "
                         "itself, which would report a mismatch count",
        "G-SLICE-EXIT-FREE": "a property of the committed source text at its "
                             "pinned sha, gated by G-SOURCES",
        "G-EXACT": "an AST and type scan of this file and this receipt; a "
                   "float literal anywhere in either fires it",
        "G-TWO-WAY": "discharged by the fates the census exhibits; a mutant "
                     "that removes one fate fires the gate that measures it",
        "G-PREDICTIONS": "an aggregate of three gates each separately "
                         "falsified",
        "G-COMPARATOR-INDEPENDENT": "an AST scan of this file's own two "
                                    "verdict routines; its falsifier is a "
                                    "source edit, and the scan publishes the "
                                    "shared constants and typed values it "
                                    "finds -- the head mutant demonstrates "
                                    "the paired gate firing",
        "G-FALSIFIER-CODE": "an AST scan of this file's own mutant hooks; a "
                            "mutant that removed its hook would break the "
                            "declared-versus-hooked equality this gate IS",
        "G-POSDEF-COVERS": "a walk of every code of a box wider than this "
                           "ladder reaches, by the same Sylvester value the "
                           "census classifies with; a positive-definite code "
                           "carrying a zero count anywhere in the box fires "
                           "it, and the bridge mutant plants one",
        "G-COVERAGE-HONEST": "this ledger itself -- a gate cannot be inside "
                             "the object it audits.  Its falsifier is the "
                             "unguarded list it publishes: a gate added "
                             "without a mutant or a forcing fills it and the "
                             "gate fails on its own row",
        "G-SWEEP-EXECUTED": "the sweep-to-writer binding; its conjunction is "
                            "RE-TAKEN as a conjunct of the terminal integrity "
                            "gate, so a run whose sweep did not execute "
                            "cannot write, and the mutants of that gate "
                            "exercise the same conjunction",
        "G-GATE-REGISTRY": "a comparison of this run's own evaluated gate "
                           "names against the frozen registry the CLI "
                           "prints; the registry mutant drops a name from it",
        "G-CLOSING-WARRANT": "a comparison of the sealed warrant against the "
                             "transcript it describes and an AST reading of "
                             "this file's own write path; the warrant mutant "
                             "corrupts the sealed row",
        "G-SEAL-TOTAL": "the totality gate; it compares the seal manifest "
                        "against the published key set, so a key published "
                        "without a seal or a declared-unsealed row fires it, "
                        "and no mutant can add a key without adding a gap",
        "G-INTEGRITY": "the terminal disk-versus-seal comparison, taken "
                       "against the STAGED bytes before they are promoted; "
                       "it re-takes the pre-write gate's whole conjunction on "
                       "the bytes actually written and additionally requires "
                       "the corrupted probe to be detected, which the run "
                       "demonstrates in line",
    }
    rows = []
    for name in names:
        rows.append({"gate": name, "mutants": mutants_for_gate.get(name, []),
                     "waiver": waivers.get(name),
                     "evaluated": name not in CLOSING_GATES})
    return rows


# the three gates evaluated AFTER the ledger is snapshotted and sealed: a
# totality gate cannot be inside the object it seals, and the integrity gates
# run against the sealed payload and then against the staged bytes.
CLOSING_GATES = ("G-SEAL-TOTAL", "G-INTEGRITY-PRE", "G-INTEGRITY")

# the sealed warrant's two clauses, frozen here so the gate that checks them
# compares strings rather than paraphrases
WARRANT_TRANSCRIPT = (
    "the closing gates are evaluated after the gate ledger is snapshotted and "
    "sealed: a totality gate cannot be inside the object it seals.  The "
    "archived transcript carries the rows of those evaluated before the write "
    "-- G-SEAL-TOTAL and G-INTEGRITY-PRE -- while the sealed ledger does not; "
    "the terminal integrity gate is evaluated against the STAGED bytes and "
    "cannot appear in the file it validates")
WARRANT_WRITE = (
    "a run that fails any gate writes nothing at all: the payload is staged "
    "beside its destination, the terminal integrity gate is taken against the "
    "staged bytes, and the promotion runs only after it passes -- a run that "
    "fails it removes its staging and leaves the committed artifacts "
    "untouched")

# the VOUCHING layer: the receipt keys published after the walls' scan is
# taken.  Declared here so the walls' scope is data and a census key that
# quietly moved outside the scan is caught.
LATE_KEYS = (
    "surface", "interference", "walls", "arithmetic", "reads", "verdict",
    "head_independence", "paper_claims", "paper_tables", "coverage_scan",
    "sentence_referents", "polarity", "paper_fences", "falsifiers",
    "anchor_consumers", "wall_surface", "e24", "coverage", "sweep", "gates",
    "closing_gates", "transcript_head", "transcript", "totals",
    "seal_manifest",
)

# E-24: every published quantity of this unit is a CARDINALITY over an
# exhaustively enumerated finite set.  Declared here with the set it counts,
# and stamped COUNTING-ONLY in the receipt rather than in a sentence.
E24_QUANTITIES = (
    ("the round's object space", "arena/partitions",
     "the partitions of the nine sites into three triples"),
    ("the saturating partitions", "arena/saturating",
     "the partitions attaining the top of the incidence spectrum"),
    ("the admissible points of I7's committed box",
     "i7/admissible_box_points", "I7's own declared count box"),
    ("the declared homogeneous records", "parity/declared_total",
     "I7's declared homogeneous record family"),
    ("the reachable site codes at this budget", "code_space/%d" % ROUNDS,
     "the R-fold sumset of the per-round alphabet"),
    ("the covered site codes at this budget", "sig_feed/covered_codes",
     "the reachable site codes with all three links present"),
    ("the covering-class codes at this budget",
     "sig_feed/covering_class_codes",
     "the site codes carried by a covering R-tuple"),
    ("the saturating stratum at this budget", "stratum/%d/total" % ROUNDS,
     "the ordered saturating R-tuples"),
    ("its covering tuples", "stratum/%d/cover" % ROUNDS,
     "the ordered saturating R-tuples covering all 27 cells"),
    ("the fields the stratum induces", "stratum/%d/distinct_fields" % ROUNDS,
     "the distinct link fields induced by the saturating stratum"),
    ("the fields its covering subset induces",
     "stratum_fields/covering_subset/%d" % ROUNDS,
     "the distinct link fields induced by the covering saturating R-tuples"),
    ("the link-constant record at the rung above", "r6_door/counts/(2, 2, 2)",
     "the ordered saturating sextuples inducing (2, 2, 2)"),
    ("I7's G-SINGULAR at its own budget", "r6_door/counts/G-SINGULAR",
     "the ordered saturating sextuples inducing (1, 1, 4)"),
    ("the driven schedules of the declared window", "driven/schedules",
     "the schedules of the declared window W5"),
)

# THE FROZEN GATE REGISTRY.  `--list-gates` prints this, and a gate compares
# it against the names this run actually evaluated, so the printed registry
# cannot drift from the run.
GATES_DECLARED = (
    "G-SOURCES", "G-ANCHORS", "G-I7-READOUT", "G-ARENA", "G-TRANSLATION",
    "G-ALPHABET", "G-CODESPACE", "G-CLASS-SPLIT", "G-LOCKING",
    "G-COVER-CODES", "G-SINGULAR-WITNESS", "G-CLASS-LADDER", "G-CLASS-WORDS",
    "G-LIVE-CONTROL", "G-CEILING", "G-LOCK-GENERAL", "G-POSDEF-COVERS",
    "G-PACK4", "G-SIG-FEED", "G-SATURATION-SCHEMA", "G-STRATUM",
    "G-STRATUM-FIELDS", "G-LADDER", "G-RECORD-FLOORS", "G-PARITY",
    "G-PRED-A", "G-PRED-B", "G-PRED-C", "G-PREDICTIONS", "G-SLACK",
    "G-WELD-ROWS", "G-WELD-FIBER-LAW", "G-R6-DOOR", "G-SLICE-EXIT-FREE",
    "G-DRIVER-ANCHOR", "G-DRIVEN-EQUALITY", "G-WINDOW-DECOMP", "G-FORCED",
    "G-DIA-LAW", "G-INVENTORY", "G-PERSISTENCE", "G-INTERFERENCE-CLOSED",
    "G-WALL-L1", "G-WALL-LORENTZ", "G-WALL-BHS", "G-WALL-KR", "G-TWO-WAY",
    "G-EXACT", "G-READS", "G-HEAD-DERIVED", "G-COMPARATOR-INDEPENDENT",
    "G-PAPER-CLAIMS", "G-PAPER-TABLES", "G-PAPER-COVERAGE",
    "G-PAPER-SENTENCE", "G-PAPER-POLARITY", "G-PAPER-FENCES",
    "G-FALSIFIER-CODE", "G-ANCHOR-CONSUMERS", "G-WALL-SURFACE",
    "G-E24-STAMPS", "G-COVERAGE-HONEST", "G-SWEEP-EXECUTED",
    "G-CLOSING-WARRANT", "G-GATE-REGISTRY", "G-SEAL-TOTAL",
    "G-INTEGRITY-PRE", "G-INTEGRITY",
)

# the gates a NON-DELIVERY mode does not reach, declared with the mode that
# skips them so the registry comparison is exact rather than a subset test
MODE_CONDITIONAL = {
    "G-WALL-L1": "evaluated only when an object under test is present",
    "G-WALL-LORENTZ": "evaluated only when an object under test is present",
    "G-PAPER-CLAIMS": "the paper gates, skipped by --numbers",
    "G-PAPER-TABLES": "the paper gates, skipped by --numbers",
    "G-PAPER-COVERAGE": "the paper gates, skipped by --numbers",
    "G-PAPER-SENTENCE": "the paper gates, skipped by --numbers",
    "G-PAPER-POLARITY": "the paper gates, skipped by --numbers",
    "G-PAPER-FENCES": "the paper gates, skipped by --numbers",
    "G-SWEEP-EXECUTED": "the sweep binding, taken only by a delivery run",
    "G-INTEGRITY": "the terminal disk check, taken only by a writing run",
}

MUTANTS = {
    "M-ANCHOR": ("corrupts every verbatim needle by appending two characters "
                 "before the search", "G-ANCHORS"),
    "M-ALPHABET": ("drops the last per-round site code from the measured "
                   "alphabet", "G-ALPHABET"),
    "M-CLASS": ("re-labels the singular covered codes as positive definite "
                "at this budget", "G-CLASS-SPLIT"),
    "M-LOCKING": ("reports the five-round lock as reaching a covering union "
                  "at every link", "G-LOCKING"),
    "M-COVER-CODES": ("deletes the non-positive-definite codes from the "
                      "covering-class census at this budget",
                      "G-SINGULAR-WITNESS"),
    "M-WITNESS": ("adds one incidence to every cell of the singular "
                  "witness's field", "G-SINGULAR-WITNESS"),
    "M-LADDER": ("moves G-FLAT's budget one rung up in the ladder table",
                 "G-LADDER"),
    "M-PARITY": ("reports none of the declared records as even-summed",
                 "G-PARITY"),
    "M-PRED-A": ("declares G-FLAT to be a record at this budget",
                 "G-PRED-A"),
    "M-STRATUM": ("adds one to the covering count of the saturating stratum",
                  "G-STRATUM"),
    "M-SLACK": ("adds one to the measured slack", "G-SLACK"),
    "M-WELD": ("sets the site-assignment fiber to 1 and the fate to FOUND at "
               "this budget's arenas", "G-WELD-ROWS"),
    "M-R6": ("replaces the R = 6 link-constant count with 1", "G-R6-DOOR"),
    "M-DIA": ("reports every parallel class as compulsory at this budget",
              "G-DIA-LAW"),
    "M-DRIVE-ANCHOR": ("adds one event to the driven R = 6 profile",
                       "G-DRIVER-ANCHOR"),
    "M-DRIVEN-EQ": ("adds one to every cell of the driven field at this "
                    "budget's ladder schedules", "G-DRIVEN-EQUALITY"),
    "M-INTERFERENCE": ("writes an interference reading into the declared "
                       "measurement surface", "G-INTERFERENCE-CLOSED"),
    "M-PAPER-INTERFERENCE": ("writes an interference reading into the paper's "
                             "body", "G-INTERFERENCE-CLOSED"),
    "M-PAPER-BHS": ("writes a sprinkling-grade reading into the paper's body",
                    "G-WALL-BHS"),
    "M-PAPER-KR": ("writes a dimension estimate into the paper's body",
                   "G-WALL-KR"),
    "M-WALL-L1": ("appends the retracted L-1 sentence to the paper under "
                  "test", "G-WALL-L1"),
    "M-WALL-LORENTZ": ("replaces the naming sentence's verb in the paper "
                       "under test", "G-WALL-LORENTZ"),
    "M-PAPER-CLAIM": ("corrupts the first rendered claim before it is "
                      "matched into the paper", "G-PAPER-CLAIMS"),
    "M-PAPER-TABLE": ("corrupts the last rendered table row before it is "
                      "matched into the paper", "G-PAPER-TABLES"),
    "M-PAPER-FENCE": ("appends a forged copy of the first verdict fence to "
                      "the paper under test", "G-PAPER-FENCES"),
    "M-PERSIST": ("copies each invariant's value at the rung below over its "
                  "value here, so every row reads PERSISTS",
                  "G-PERSISTENCE"),
    "M-PAPER-COVERAGE": ("appends an unbacked count to the paper under test",
                         "G-PAPER-COVERAGE"),
    "M-PAPER-POLARITY": ("negates a polarity claim in the paper under test",
                         "G-PAPER-POLARITY"),
    "M-HEAD": ("corrupts the builder's first verdict segment before the "
               "comparator sees it", "G-HEAD-DERIVED"),
    "M-SEAL": ("mutates a sealed receipt value between the gate and the "
               "write", "G-INTEGRITY-PRE"),
    "M-TRANSCRIPT": ("appends a forged NINE-SPACE-INDENTED line to the "
                     "transcript after the ledger is sealed -- the shape an "
                     "indentation whitelist admits", "G-INTEGRITY-PRE"),
    "M-I7-LINKS": ("reverses the declared link order read from I7's own "
                   "receipt", "G-I7-READOUT"),
    "M-ARENA": ("adds one to the closed-form partition count",
                "G-ARENA"),
    "M-CODESPACE": ("adds a spurious site code to the R = 4 code space",
                    "G-CODESPACE"),
    "M-COVER-R4": ("adds the singular code to the R = 4 covering-class "
                   "census", "G-COVER-CODES"),
    "M-INVENTORY": ("sets every measured choice-inventory fiber to 1",
                    "G-INVENTORY"),
    "M-CLASS-LADDER": ("copies the covered-site floor onto the covering-"
                       "record floor in every class row", "G-CLASS-LADDER"),
    "M-SIG-FLOOR": ("moves G-INDEF's record floor down to this budget",
                    "G-SIG-FEED"),
    "M-SATURATION": ("adds one incidence to every target's requirement",
                     "G-SATURATION-SCHEMA"),
    "M-PRED-B": ("reports link-constancy as arithmetically possible at every "
                 "budget", "G-PRED-B"),
    "M-PRED-C": ("adds one to every budget's declared-record yield",
                 "G-PRED-C"),
    "M-FIBER-LAW": ("flips the link-constancy flag of every weld row",
                    "G-WELD-FIBER-LAW"),
    "M-FORCED": ("adds one to the builder's maxhits at every driven "
                 "schedule", "G-FORCED"),
    "M-CLASS-WORDS": ("swaps the covering and saturating flags when the "
                      "ladder's class labels are derived, so a class is "
                      "printed under another class's words", "G-CLASS-WORDS"),
    "M-LIVE-CONTROL": ("adds one incidence to every cell of the bare-live "
                       "control's field", "G-LIVE-CONTROL"),
    "M-CEILING": ("lowers the covering class's maximum cell count at the "
                  "rung above this one", "G-CEILING"),
    "M-LOCK-GENERAL": ("reports the locked union as covering at every budget",
                       "G-LOCK-GENERAL"),
    "M-BRIDGE": ("plants a positive-definite code carrying a zero count in "
                 "the bridge census", "G-POSDEF-COVERS"),
    "M-PACK4": ("raises the largest measured cell count to the packing's "
                "capacity", "G-PACK4"),
    "M-FIELDS": ("copies the whole stratum's field count onto its covering "
                 "subset's", "G-STRATUM-FIELDS"),
    "M-RECORD-FLOOR": ("empties G-INDEF's census at its own budget",
                       "G-RECORD-FLOORS"),
    "M-DIA-EXT": ("reports a compulsory class at the link-constant records "
                  "outside this budget", "G-DIA-LAW"),
    "M-WINDOW": ("moves one schedule from the budget-4 anchor to the seed "
                 "fan in the window decomposition", "G-WINDOW-DECOMP"),
    "M-SPREAD": ("collapses the label fiber's spread to its headline value "
                 "at every unmotivated arena", "G-WELD-ROWS"),
    "M-READS": ("adds an undeclared source to the run's own reads register",
                "G-READS"),
    "M-HEADERS": ("swaps two column labels of the first rendered table "
                  "header", "G-PAPER-TABLES"),
    "M-SENTENCE": ("appends a numeral from another census to a rendered "
                   "claim's sentence in the paper under test",
                   "G-PAPER-SENTENCE"),
    "M-ANCHOR-GATE": ("re-points every verbatim anchor at a gate that does "
                      "not exist", "G-ANCHOR-CONSUMERS"),
    "M-SURFACE": ("drops a census key from the walls' declared scanned "
                  "surface", "G-WALL-SURFACE"),
    "M-STAMPS": ("re-stamps a counting-only quantity as a density",
                 "G-E24-STAMPS"),
    "M-REGISTRY": ("drops a name from the frozen gate registry the CLI "
                   "prints", "G-GATE-REGISTRY"),
    "M-WARRANT": ("corrupts the sealed closing-gate warrant's transcript "
                  "clause", "G-CLOSING-WARRANT"),
    "M-TAIL": ("appends a forged transcript line carrying a closing gate's "
               "name -- the second shape a containment whitelist admits",
               "G-INTEGRITY-PRE"),
    "M-RESIDUE": ("plants the DIA census's own class frequency, SPELLED, in "
                  "a referent-free sentence of the paper under test -- a "
                  "value true of a census in this receipt and of no claim",
                  "G-PAPER-SENTENCE"),
    "M-RESIDUE-N": ("plants the same DIA class frequency IN DIGITS in a "
                    "referent-free sentence of the paper under test -- the "
                    "residue's other list", "G-PAPER-SENTENCE"),
}


def finish(LD, SEAL, R, src, tree, ptext, ptext_nm, do_paper, write, swept,
           sweep_rows):
    say("")
    say("[SEC 11] THE VERDICT, THE PAPER AND THE SEAL")
    head = verdict_segments(R)
    head = pick("M-HEAD", head, [head[0] + " XX"] + head[1:])
    R["verdict"] = SEAL.take("verdict", head)
    serialized = json.dumps(R, sort_keys=True, default=str)
    comp = reconstruct_from_serialized(serialized)
    LD.add("G-HEAD-DERIVED",
           len(comp) == len(head) and all(comp[i] == head[i]
                                          for i in range(len(head))),
           "THE HEAD IS DERIVED TWICE AND THE TWO STRINGS ARE COMPARED "
           "CHARACTER FOR CHARACTER.  The builder renders the four verdict "
           "segments from its own objects; a comparator reads only the "
           "SERIALIZED receipt, types all four templates in its own "
           "fragments and rebuilds them, and the two routes must agree "
           "exactly -- so no segment of the head can go stale",
           "segments %d, exact string agreements %d, head %d chars"
           % (len(head), sum(1 for i in range(len(head))
                             if comp[i] == head[i]),
              sum(len(h) for h in head)))
    b_const = set(template_constants(tree, "verdict_segments"))
    c_const = set(template_constants(tree, "reconstruct_from_serialized"))
    names = [n for n, _w in VERDICT_NAMES]
    def strip_names(s):
        for n in names:
            s = s.replace(n, " ")
        return s
    digits = sorted({t for s in list(b_const) + list(c_const)
                     for t in re.findall(r"\d[\d,]*", strip_names(s))})
    nwords = sorted({w.lower() for s in list(b_const) + list(c_const)
                     for w in re.findall(r"\b(%s)\b" % "|".join(WORDNUM),
                                         strip_names(s), re.I)})
    R["head_independence"] = SEAL.take("head_independence", {
        "builder_constants": len(b_const), "comparator_constants":
            len(c_const), "shared": sorted(b_const & c_const),
        "declared_names": [list(v) for v in VERDICT_NAMES],
        "typed_numerals": digits, "typed_number_words": nwords})
    LD.add("G-COMPARATOR-INDEPENDENT",
           not (b_const & c_const) and not digits and not nwords
           and b_const and c_const,
           "THE TWO ROUTES SHARE NO TYPED TEXT AND NEITHER TYPES A VALUE.  "
           "An AST scan reads the string constants of the builder and of the "
           "comparator, requires the two sets to be DISJOINT, and requires "
           "that once the declared object names are removed no numeral and "
           "no number-word survives in either -- every number in the head "
           "is interpolated from the receipt on both sides",
           "builder constants %d, comparator constants %d, shared %d, typed "
           "numerals %s, typed number-words %s"
           % (len(b_const), len(c_const), len(b_const & c_const), digits,
              nwords))

    if do_paper and ptext:
        claims = paper_claims(R)
        claims = pick("M-PAPER-CLAIM", claims,
                      dict(claims, **{sorted(claims)[0]:
                                      claims[sorted(claims)[0]] + " XX"}))
        missing = [k for k, v in sorted(claims.items())
                   if not match_needle(ptext, v)]
        R["paper_claims"] = SEAL.take("paper_claims",
                                      {"rendered": claims,
                                       "missing": missing})
        LD.add("G-PAPER-CLAIMS",
               not missing,
               "EVERY HEADLINE SENTENCE OF THE PAPER IS RENDERED FROM THE "
               "RECEIPT AND MATCHED INTO THE PAPER.  Each claim is built "
               "from the receipt's own values and then searched for in the "
               "object under test, whitespace-normalised and "
               "markdown-stripped, so a sentence whose number drifts from "
               "the census cannot survive",
               "claims %d, matched %d, missing %s"
               % (len(claims), len(claims) - len(missing), missing))

        blocks = paper_table_blocks(R)
        headers = ["| " + " | ".join(str(h) for h in hd) + " |"
                   for _n, hd, _d in blocks]
        want = paper_tables(R)
        want = pick("M-PAPER-TABLE", want,
                    want[:-1] + [want[-1].replace("|", "!", 1)])

        def _swap_cells(row):
            cells = row.split(" | ")
            if len(cells) > 3:
                cells[1], cells[2] = cells[2], cells[1]
            return " | ".join(cells)
        want = pick("M-HEADERS", want,
                    [_swap_cells(w) if w == headers[0] else w for w in want])
        have = markdown_table_rows(ptext)
        havec = [canon(h) for h in have]
        badrows = [w for w in want if havec.count(canon(w)) != 1]
        R["paper_tables"] = SEAL.take("paper_tables",
                                      {"rendered": len(want),
                                       "tables": len(blocks),
                                       "headers": headers,
                                       "data_rows": len(want) - len(blocks),
                                       "rows_in_the_paper": len(have),
                                       "not_exactly_once": badrows})
        LD.add("G-PAPER-TABLES",
               not badrows and len(want) > 0
               and len(headers) == len(blocks)
               and len(set(headers)) == len(headers),
               "EVERY CELL OF EVERY MEASUREMENT TABLE IS RENDERED FROM THE "
               "RECEIPT AND REQUIRED TO OCCUR EXACTLY ONCE (E-22) -- THE "
               "HEADER ROWS INCLUDED.  A table row is a claim: a forged cell "
               "dies even when every numeral in it is receipt-backed, and a "
               "duplicated row dies too.  The HEADER row is the claim that "
               "says what the other rows ARE, so it is rendered from the "
               "receipt on the same terms, and every class-naming header is "
               "derived from the predicate its column's number was computed "
               "with -- a swapped column label is then a claim about a "
               "predicate this file does not compute, and dies here",
               "tables %d, header rows %d, data rows %d, rendered rows %d, "
               "table rows in the paper %d, rows not occurring exactly once %d"
               % (len(blocks), len(headers), len(want) - len(blocks),
                  len(want), len(have), len(badrows)))

        cov = paper_coverage(R, pick("M-PAPER-COVERAGE", ptext,
                                     ptext + "\n\nan unbacked count: "
                                     "123456789\n"))
        R["coverage_scan"] = SEAL.take("coverage_scan", cov)
        LD.add("G-PAPER-COVERAGE",
               not cov["unbacked"] and not cov["unbacked_words"]
               and not cov["unbacked_compounds"]
               and cov["exemptions_fired"] == cov["exemptions"],
               "NUMERAL COVERAGE SCANS THE WHOLE PAPER -- PROSE, TABLES, "
               "INLINE CODE SPANS AND THE FENCED VERDICT BLOCKS -- AGAINST "
               "EXACTLY THREE DECLARED LISTS: this run's registered numbers, "
               "the receipt it publishes, and a declared exemption table "
               "with a reason per literal, every one of which must fire.  "
               "The spelled-out numbers are scanned on the same terms",
               "numerals scanned %d, unbacked %s, number-words scanned %d, "
               "unbacked %s, compound number-words %d, unbacked %s, "
               "exemptions fired %d of %d, chars %d"
               % (cov["numerals_scanned"], cov["unbacked"],
                  cov["number_words_scanned"], cov["unbacked_words"],
                  cov["compound_number_words"], cov["unbacked_compounds"],
                  cov["exemptions_fired"], cov["exemptions"],
                  cov["chars_scanned"]))

        sent_txt = pick("M-SENTENCE", ptext,
                        ptext.replace("the determinant support is {",
                                      "over 72 classes the determinant "
                                      "support is {", 1))
        # THE TWO RESIDUE LEGS, FALSIFIED SEPARATELY.  The planted value is
        # the DIA census's own parallel-class frequency -- true of a census
        # in this very receipt, false of the sentence it is planted in, and
        # registered by no claim.  Spelled (M-RESIDUE) and in digits
        # (M-RESIDUE-N), because the gate tests the two on separate lists.
        sent_txt = pick("M-RESIDUE", sent_txt,
                        sent_txt.replace("Read out.",
                                         "Read out.  There are sixty "
                                         "rungs here.", 1))
        sent_txt = pick("M-RESIDUE-N", sent_txt,
                        sent_txt.replace("Read out.",
                                         "Read out.  There are 60 "
                                         "rungs here.", 1))
        sent = sentence_referents(R, sent_txt, claims)
        R["sentence_referents"] = SEAL.take("sentence_referents", sent)
        LD.add("G-PAPER-SENTENCE",
               not sent["loose_numerals"]
               and len(sent["residue_numerals"]) <= sent["residue_ceiling"]
               and len(sent["residue_number_words"]) <= sent["residue_ceiling"]
               and sent["sentences_carrying_a_claim"] > 0,
               "ONE UNIVERSE PER SENTENCE: EVERY NUMERAL OF A SENTENCE THAT "
               "CARRIES A RENDERED CLAIM BELONGS TO THAT CLAIM.  A numeral "
               "that is true of SOME census in this receipt can be false of "
               "the sentence it is standing in -- every numeral backed, the "
               "RELATION forged -- and a receipt-wide allow-list cannot see "
               "it.  So each prose sentence carrying at least one rendered "
               "claim is required to carry no numeral outside the spans of "
               "the claims it carries, with the declared object NAMES "
               "removed first; a numeral appended to a claim's sentence has "
               "no referent and dies here.  AND THE RESIDUE IS PUBLISHED: a "
               "numeral -- spelled or not -- standing in a sentence that "
               "carries no referent at all and backed by nothing but the "
               "receipt read as a bag is counted against a declared ceiling, "
               "so the breadth of the allow-list is a measured number and "
               "not an implicit licence",
               "sentences scanned %d, carrying a claim %d, declared names %d, "
               "numerals with no referent %s; residue against a ceiling of "
               "%d: %s numerals, %s number-words"
               % (sent["sentences_scanned"],
                  sent["sentences_carrying_a_claim"], sent["declared_names"],
                  [x["numeral"] for x in sent["loose_numerals"]],
                  sent["residue_ceiling"],
                  [x["numeral"] for x in sent["residue_numerals"]],
                  [x["word"] for x in sent["residue_number_words"]]))

        pol = paper_polarity(R, pick(
            "M-PAPER-POLARITY", ptext_nm,
            ptext_nm.replace("drives it", "was not asked")))
        R["polarity"] = SEAL.take("polarity", pol)
        LD.add("G-PAPER-POLARITY",
               all(p["ok"] for p in pol),
               "EVERY POLARITY CLAIM IS BOUND TO THE RECEIPT ROW THAT "
               "DECIDES IT.  A sentence saying a thing BREAKS must be "
               "present exactly when the census says it breaks, and absent "
               "when it does not; each row is checked against its own "
               "measured value rather than against an aggregate",
               "polarity claims %d, in agreement %d"
               % (len(pol), sum(1 for p in pol if p["ok"])))

        blocks = fenced_blocks(pick("M-PAPER-FENCE", ptext,
                                    ptext + "\n```\n" + head[0]
                                    + " FORGED\n```\n"))
        want_ms = Counter(re.sub(r"\s+", " ", h).strip() for h in head)
        for k in want_ms:
            want_ms[k] *= FENCE_COPIES
        got_ms = Counter(b for b in blocks if b.startswith("PERR"))
        R["paper_fences"] = SEAL.take("paper_fences", {
            "fenced_blocks": len(blocks), "verdict_fences": sum(got_ms.values()),
            "expected": sum(want_ms.values()),
            "multiset_equal": got_ms == want_ms})
        LD.add("G-PAPER-FENCES",
               got_ms == want_ms,
               "THE FENCED VERDICT BLOCKS ARE GATED BY MULTISET EQUALITY, "
               "NOT BY CONTAINMENT (E-22).  Each of the four segments must "
               "appear exactly twice -- once in the head and once in the "
               "verdict section -- so forging either copy, deleting one, or "
               "appending a forged third all die",
               "fenced blocks %d, verdict fences %d, expected %d, multiset "
               "equal %s" % (len(blocks), sum(got_ms.values()),
                             sum(want_ms.values()), got_ms == want_ms))

    hooks = mutant_hooks(src)
    declared = sorted(MUTANTS)
    hooked = sorted(hooks)
    const_bool = sorted(k for k, v in hooks.items()
                        if any(h["constant_boolean"] for h in v))
    desc_ok = []
    for name, (desc, gate) in sorted(MUTANTS.items()):
        srcs = " ".join(h["source"] for h in hooks.get(name, []))
        desc_ok.append({"mutant": name, "gate": gate,
                        "hooks": len(hooks.get(name, [])),
                        "source_published": bool(srcs)})
    R["falsifiers"] = SEAL.take("falsifiers", {
        "declared": declared, "hooked": hooked,
        "rows": desc_ok, "constant_boolean": const_bool,
        "hook_sources": {k: [h["source"] for h in v]
                         for k, v in sorted(hooks.items())}})
    LD.add("G-FALSIFIER-CODE",
           set(declared) == set(hooked) and not const_bool
           and all(d["hooks"] > 0 for d in desc_ok),
           "EVERY FALSIFIER IS CHECKED AGAINST ITS OWN CODE (E-23).  Each "
           "declared mutant's hook is located by AST, the source of the "
           "statement carrying it is published in the receipt, the declared "
           "set and the hooked set must agree exactly, and any corruption "
           "that is a constant boolean -- the class that cannot fail and "
           "whose description therefore inverts its code -- is rejected "
           "outright",
           "declared %d, hooked %d, constant-boolean corruptions %d, hooks "
           "published %d" % (len(declared), len(hooked), len(const_bool),
                             sum(d["hooks"] for d in desc_ok)))

    # ---- THE ANCHORS' CONSUMERS, ENFORCED --------------------------------
    anchor_rows2 = pick("M-ANCHOR-GATE", R["anchors"],
                        [dict(a, gate="G-DOES-NOT-EXIST") for a in R["anchors"]])
    evaluated = set(LD.names())
    named = sorted({a["gate"] for a in anchor_rows2})
    phantom = sorted(g for g in named if g not in evaluated)
    R["anchor_consumers"] = SEAL.take("anchor_consumers", {
        "anchors": len(anchor_rows2), "gates_named": named,
        "phantom_gates": phantom,
        "gates_evaluated_when_checked": len(evaluated)})
    LD.add("G-ANCHOR-CONSUMERS",
           not phantom and len(named) > 0
           and all(a["gate"] for a in anchor_rows2),
           "EVERY VERBATIM ANCHOR'S NAMED CONSUMER IS A GATE THIS RUN "
           "ACTUALLY EVALUATED.  The anchor register records, for each "
           "needle, the gate that consumes it; recording it is not enforcing "
           "it, and a register whose consumers are never checked admits a "
           "phantom.  Here every gate named by an anchor is required to be in "
           "this run's own evaluated gate list at the close, so an anchor "
           "pointed at a gate that does not exist -- or at one that never "
           "ran -- dies",
           "anchors %d naming %d distinct gates, phantom consumers %s, gates "
           "evaluated when checked %d"
           % (len(anchor_rows2), len(named), phantom, len(evaluated)))

    # ---- THE WALL SURFACE'S SCOPE, MADE DATA -----------------------------
    late = sorted(k for k in R if k not in set(R["surface"]
                                               ["scanned_receipt_keys"]))
    undeclared_late = [k for k in late if k not in LATE_KEYS]
    inside = [k for k in R["surface"]["scanned_receipt_keys"]
              if k in LATE_KEYS]
    R["wall_surface"] = SEAL.take("wall_surface", {
        "keys_published": len(R) + 1,
        "keys_scanned": R["surface"]["scanned_receipt_key_count"],
        "keys_outside_the_scan": late,
        "declared_outside": list(LATE_KEYS),
        "undeclared_outside": undeclared_late,
        "reason": "the keys outside the scan are the VOUCHING layer, "
                  "published after the census closes and sealed and gated in "
                  "its own right; the wall and interference rows among them "
                  "necessarily quote the very words the scan bans, which is "
                  "why the scan is taken before they exist"})
    LD.add("G-WALL-SURFACE",
           not undeclared_late and not inside
           and R["surface"]["paper_body_included"] is True
           and R["surface"]["verdict_segments_included"] > 0,
           "THE WALLS' DECLARED SURFACE IS ENUMERATED, AND WHAT IS OUTSIDE IT "
           "IS DECLARED.  A scan that claims to cover `every published receipt "
           "key` and covers two thirds of them is a false vouching row.  This "
           "run enumerates the keys its wall scans actually cover, lists the "
           "keys published after the scan, and requires that list to be "
           "exactly the DECLARED vouching layer -- so a census key that "
           "quietly moved outside the scan is caught.  The four derived "
           "verdict segments are inside the surface, so a banned reading in "
           "the head is seen",
           "keys published %d, scanned %d, outside %d (all declared %s), "
           "declared-late keys found inside %s, verdict segments in the "
           "surface %d, paper body in the surface %s"
           % (len(R) + 1, R["surface"]["scanned_receipt_key_count"],
              len(late), not undeclared_late, inside,
              R["surface"]["verdict_segments_included"],
              R["surface"]["paper_body_included"]))

    # ---- E-24: THE COUNTING-ONLY STAMPS, ACTUALLY EMITTED ----------------
    stamps = []
    for q, path, universe in E24_QUANTITIES:
        try:
            val = jpath(R, path)
        except Exception:
            val = None
        stamps.append({"quantity": q, "path": path, "value": val,
                       "measure": "COUNTING-ONLY", "universe": universe})
    stamps = pick("M-STAMPS", stamps,
                  [dict(s0, measure="A DENSITY") if i == 0 else s0
                   for i, s0 in enumerate(stamps)])
    dens = R["prediction_c"].get("richer_in_denominators", {})
    R["e24"] = SEAL.take("e24", {
        "stamps": stamps, "stamped": len(stamps),
        "counter_column_denominators": dens,
        "statement": "every quantity this unit publishes is a CARDINALITY "
                     "over an exhaustively enumerated finite set, stamped "
                     "COUNTING-ONLY beside its own universe; no typicality "
                     "claim rests on any of them, and the one counter-column "
                     "of ratios carries its denominators beside its "
                     "numerators"})
    LD.add("G-E24-STAMPS",
           all(s0["measure"] == "COUNTING-ONLY" for s0 in stamps)
           and all(isinstance(s0["value"], int) and not isinstance(
               s0["value"], bool) for s0 in stamps)
           and len(stamps) == len(E24_QUANTITIES)
           and set(dens) == set(R["prediction_c"]["richer_in"]),
           "E-24: EVERY PUBLISHED QUANTITY CARRIES ITS MEASURE AND ITS "
           "UNIVERSE, AND THE STAMP IS IN THE RECEIPT RATHER THAN IN A "
           "SENTENCE ABOUT THE RECEIPT.  A paper that says its counts are "
           "counting-only and stamps nothing has written an adjective; here "
           "each published cardinality is stamped COUNTING-ONLY beside the "
           "finite set it counts, each stamped value is checked to be an "
           "integer, and the counter-column's every pair carries its own "
           "denominators -- so a ratio cannot be read off a numerator alone",
           "quantities stamped %d, all COUNTING-ONLY %s, counter-column pairs "
           "with denominators %d of %d"
           % (len(stamps),
              all(s0["measure"] == "COUNTING-ONLY" for s0 in stamps),
              len(dens), len(R["prediction_c"]["richer_in"])))

    gate_of = {}
    for name, (_d, gate) in MUTANTS.items():
        gate_of.setdefault(gate, []).append(name)
    # THE HONEST DENOMINATOR IS THE RUN'S WHOLE GATE SET -- the rows sealed in
    # the ledger PLUS the declared closing gates, which are evaluated after
    # the ledger is snapshotted and would otherwise be counted by nobody.
    projected = list(LD.names()) + ["G-COVERAGE-HONEST"] \
        + (["G-SWEEP-EXECUTED"] if swept else []) \
        + ["G-CLOSING-WARRANT", "G-GATE-REGISTRY"] + list(CLOSING_GATES)
    led = waiver_ledger(projected, gate_of)
    naked = [r["gate"] for r in led if not r["mutants"] and not r["waiver"]]
    R["coverage"] = SEAL.take("coverage", {
        "gates": len(led), "rows": led,
        "gates_evaluated_when_the_ledger_is_built": len(LD.rows),
        "closing_gates_projected": list(CLOSING_GATES),
        "gates_with_a_declared_mutant": sum(1 for r in led if r["mutants"]),
        "gates_with_a_forcing_waiver": sum(1 for r in led if r["waiver"]
                                           and not r["mutants"]),
        "unguarded": naked})
    LD.add("G-COVERAGE-HONEST",
           not naked and len(led) == len(set(led_r["gate"] for led_r in led))
           and len(led) > len(LD.rows),
           "THE COVERAGE LEDGER IS HONEST: EVERY GATE IS EITHER FALSIFIED BY "
           "A DECLARED MUTANT OR WAIVED WITH A FORCING THAT SAYS WHY IT "
           "CANNOT FAIL.  The denominator is the run's WHOLE gate set -- the "
           "rows already in the ledger plus this gate, the sweep binding and "
           "the three declared closing gates, every one of which is evaluated "
           "after the ledger is snapshotted and would otherwise be audited by "
           "nobody -- so the denominator is strictly larger than the number "
           "of gates standing when it is built, and a gate with neither a "
           "mutant nor a forcing is reported as unguarded",
           "gates %d (%d evaluated when the ledger is built, %d projected "
           "closing rows), with a mutant %d, with a forcing waiver %d, "
           "unguarded %s"
           % (len(led), len(LD.rows), len(led) - len(LD.rows) - 1,
              sum(1 for r in led if r["mutants"]),
              sum(1 for r in led if r["waiver"] and not r["mutants"]),
              naked))

    if swept:
        on_target = [r for r in sweep_rows if r["killed_at"] == r["gate"]]
        R["sweep"] = SEAL.take("sweep", {
            "rows": sweep_rows, "mutants": len(sweep_rows),
            "on_target": len(on_target)})
        LD.add("G-SWEEP-EXECUTED",
               len(sweep_rows) == len(MUTANTS) and len(on_target)
               == len(sweep_rows),
               "THE MUTANT SWEEP ACTUALLY RAN, AND EVERY MUTANT DIED AT THE "
               "GATE ITS DECLARATION NAMES.  A delivery-level run carries "
               "one sweep row per declared mutant and every row is on "
               "target; the same conjunction is re-taken at the terminal "
               "integrity gate, so the only writer in this file is "
               "downstream of a sweep that actually ran",
               "declared %d, rows %d, on target %d"
               % (len(MUTANTS), len(sweep_rows), len(on_target)))

    # ---- THE CLOSING WARRANT, TRUE IN BOTH ITS CLAUSES ------------------
    # A sealed vouching row that says what the code does must be checked
    # against the code.  Clause one is checked against the transcript the run
    # is about to write; clause two is checked by READING THIS FILE'S OWN
    # WRITE PATH: the terminal integrity gate must be evaluated BEFORE the
    # promotion, so a run that fails it promotes nothing.
    fin_fn = [n for n in ast.walk(tree)
              if isinstance(n, ast.FunctionDef) and n.name == "finish"][0]

    def _call_lines(fn, owner, attr, first_arg=None):
        """the source lines of `owner.attr(...)` inside `fn` -- the OWNER is
        matched too, so a string's own `.replace` is not read as a
        promotion."""
        out = []
        for n in ast.walk(fn):
            if not (isinstance(n, ast.Call)
                    and isinstance(n.func, ast.Attribute)
                    and n.func.attr == attr
                    and isinstance(n.func.value, ast.Name)
                    and n.func.value.id == owner):
                continue
            if first_arg is not None:
                if not (n.args and isinstance(n.args[0], ast.Constant)
                        and n.args[0].value == first_arg):
                    continue
            out.append(n.lineno)
        return sorted(out)
    integ_at = _call_lines(fin_fn, "LD", "add", "G-INTEGRITY")
    promote_at = _call_lines(fin_fn, "os", "replace")
    readback_first = bool(integ_at) and bool(promote_at) \
        and min(promote_at) > max(integ_at)
    in_artifact = [g for g in CLOSING_GATES if g != "G-INTEGRITY"]
    closing_decl = {
        "names": list(CLOSING_GATES),
        "in_the_artifact": in_artifact,
        "not_in_the_artifact": ["G-INTEGRITY"],
        "warrant_transcript": WARRANT_TRANSCRIPT,
        "warrant_write": WARRANT_WRITE,
        "integrity_evaluated_at_source_line": integ_at,
        "promotion_at_source_line": promote_at,
        "read_back_before_promotion": readback_first}
    closing_decl = pick("M-WARRANT", closing_decl,
                        dict(closing_decl,
                             warrant_transcript="the archived transcript "
                                                "carries all three rows"))
    LD.add("G-CLOSING-WARRANT",
           closing_decl["warrant_transcript"] == WARRANT_TRANSCRIPT
           and closing_decl["warrant_write"] == WARRANT_WRITE
           and closing_decl["names"] == list(CLOSING_GATES)
           and closing_decl["in_the_artifact"] == in_artifact
           and readback_first,
           "THE SEALED CLOSING WARRANT IS TRUE IN BOTH ITS CLAUSES, AND BOTH "
           "ARE CHECKED RATHER THAN ASSERTED.  Clause one names which closing "
           "rows the archived transcript carries -- the two evaluated before "
           "the write -- and the terminal integrity row, which cannot appear "
           "in the file it validates; the transcript gate below compares the "
           "artifact's tail against exactly those rows.  Clause two says a "
           "failing run writes nothing, and it is checked by READING THIS "
           "FILE: the payload is staged beside its destination, the integrity "
           "gate is evaluated against the staged bytes, and the promotion "
           "call appears strictly after it in this function's own syntax "
           "tree, so a failing run cannot promote",
           "closing gates %s, carried in the artifact %s; integrity gate "
           "evaluated at source line %s, promotion at %s, read-back before "
           "promotion %s"
           % (closing_decl["names"], closing_decl["in_the_artifact"],
              integ_at, promote_at, readback_first))

    # ---- THE FROZEN GATE REGISTRY, COMPARED AGAINST THE RUN -------------
    declared_gates = pick("M-REGISTRY", list(GATES_DECLARED),
                          list(GATES_DECLARED)[1:])
    evaluated_names = list(LD.names())
    future = set(CLOSING_GATES) | {"G-GATE-REGISTRY"}
    unknown = [g for g in evaluated_names if g not in set(declared_gates)]
    missing = [g for g in declared_gates
               if g not in set(evaluated_names) | future]
    undeclared_skips = [g for g in missing if g not in MODE_CONDITIONAL]
    order_ok = [g for g in declared_gates if g in set(evaluated_names)] \
        == evaluated_names
    R["gate_registry"] = SEAL.take("gate_registry", {
        "declared": declared_gates, "declared_count": len(declared_gates),
        "evaluated": evaluated_names, "evaluated_count": len(evaluated_names),
        "closing_still_to_come": sorted(future),
        "skipped_in_this_mode": missing,
        "mode_conditional": MODE_CONDITIONAL,
        "unknown_gates": unknown, "undeclared_skips": undeclared_skips,
        "in_declared_order": order_ok})
    LD.add("G-GATE-REGISTRY",
           not unknown and not undeclared_skips and order_ok
           and len(set(declared_gates)) == len(declared_gates)
           and len(declared_gates) == len(GATES_DECLARED),
           "THE GATE REGISTRY THE CLI PRINTS IS THIS RUN'S OWN GATE SET.  A "
           "`--list-gates` that enumerates the falsifiable gates and calls "
           "them the gates is an undisclosed convention; here the registry is "
           "frozen in the source, printed by the CLI, and compared against "
           "the names this run actually evaluated -- every evaluated gate "
           "must be in it, in its declared ORDER, and every declared gate not "
           "evaluated must either be a closing gate still to come or carry a "
           "declared reason why this mode skips it",
           "declared %d, evaluated %d, still to come %d, skipped in this mode "
           "%s, unknown %s, in declared order %s"
           % (len(declared_gates), len(evaluated_names), len(future),
              missing, unknown, order_ok))

    R["closing_gates"] = SEAL.take("closing_gates", closing_decl)
    R["gates"] = SEAL.take("gates", {"rows": [dict(g) for g in LD.rows],
                                     "count": len(LD.rows),
                                     "chain": LD.chain[:12]})
    snap = list(LINES)
    snap_rows = len(LD.rows)
    R["transcript_head"] = SEAL.take("transcript_head", snap[:3])
    R["transcript"] = SEAL.take("transcript", {
        "lines_sealed": len(snap),
        "digest": hashlib.sha256("\n".join(snap).encode()).hexdigest()[:12],
        "closing_lines": "the artifact's tail must EQUAL, line for line, the "
                         "rows of the closing gates carried in it, rendered "
                         "from the ledger; there is no whitelist, so neither "
                         "an indented line nor a line merely containing a "
                         "closing gate's name is admitted"})
    R["totals"] = SEAL.take("totals", {
        "gates": len(LD.rows), "sources": len(SOURCES),
        "anchors": len(VERBATIM), "mutants": len(MUTANTS),
        "registered_numbers": len(NUMREG)})
    SEAL.declare_unsealed("seal_manifest", "the manifest of seals itself; "
                          "it carries no measurement and is frozen by the "
                          "seal chain")
    SEAL.declare_unsealed("python", "the interpreter's major version, a "
                          "declaration rather than a measurement")
    SEAL.declare_unsealed("schema", "this unit's schema string, frozen in "
                          "the source")
    SEAL.declare_unsealed("unit", "this unit's name, frozen in the source")
    SEAL.declare_unsealed("pin", "this unit's pin path and sha, frozen in "
                          "the source")
    manifest = {"seals": SEAL.seals, "unsealed": SEAL.unsealed,
                "chain": SEAL.chain[:12]}
    R["seal_manifest"] = manifest
    published = sorted(R)
    covered = sorted(set(SEAL.seals) | {u["key"] for u in SEAL.unsealed})
    gap = [k for k in published if k not in covered]
    LD.add("G-SEAL-TOTAL",
           not gap,
           "THE SEAL IS TOTAL.  Every published receipt key -- the measured "
           "layer and the vouching layer alike -- is either sealed at the "
           "moment its gate passed or listed as DECLARED-UNSEALED with a "
           "reason, and this gate compares the manifest against the "
           "published key set rather than against the seals that happened to "
           "be taken",
           "published keys %d, sealed %d, declared unsealed %d, uncovered %s"
           % (len(published), len(SEAL.seals), len(SEAL.unsealed), gap))

    payload = json.loads(json.dumps(R, sort_keys=True, default=str))
    if mut("M-SEAL"):
        payload["totals"]["gates"] += 1
    bad = SEAL.verify(payload)

    def rendered_tail():
        """THE ARTIFACT'S EXPECTED TAIL, RENDERED FROM THE LEDGER ITSELF.
        Every gate row the ledger has taken since the transcript prefix was
        sealed is re-rendered here in the writer's own format; the tail of
        the text is then required to EQUAL it, line for line.  There is no
        whitelist to defeat: neither a nine-space-indented line nor a line
        merely containing a closing gate's name is admitted."""
        out = []
        for r0 in LD.rows[snap_rows:]:
            out.append("  [%s] %s" % ("PASS" if r0["pass"] else "FAIL",
                                      r0["gate"]))
            out.append("         %s" % r0["statement"])
            out.append("         evidence: %s" % r0["evidence"])
        return out

    def transcript_ok(txt):
        tl = txt.rstrip("\n").split("\n")
        pre = (hashlib.sha256("\n".join(tl[:len(snap)]).encode())
               .hexdigest()[:12] == R["transcript"]["digest"])
        return pre, tl[len(snap):] == rendered_tail(), len(tl) - len(snap)

    text = "\n".join(LINES) + "\n"
    text = pick("M-TRANSCRIPT", text,
                text + " " * 9 + "FORGED: the covering class and the "
                "positive-definite class\n")
    text = pick("M-TAIL", text,
                text + "  [PASS] G-SEAL-TOTAL  forged twin row\n")
    pre_ok, tail_ok, ntail = transcript_ok(text)
    LD.add("G-INTEGRITY-PRE",
           not bad and pre_ok and tail_ok,
           "THE PAYLOAD ABOUT TO BE WRITTEN IS THE PAYLOAD THAT WAS SEALED.  "
           "Every sealed key is re-digested from the serialized payload and "
           "compared against the digest taken at gate time, so a value that "
           "moved between its gate and the write is caught before any byte "
           "reaches the disk.  THE TRANSCRIPT IS COVERED LINE BY LINE ON THE "
           "SAME TERMS, AND BY EQUALITY RATHER THAN BY WHITELIST: the sealed "
           "prefix is re-digested from the text about to be written, and the "
           "lines after it must EQUAL the closing rows rendered from the "
           "ledger itself -- so a forged line dies whatever it is indented "
           "by and whatever gate name it happens to contain",
           "sealed keys %d, mismatches %s, transcript prefix %d lines "
           "re-digested %s, trailing lines %d equal to the rendered closing "
           "rows %s" % (len(SEAL.seals), bad, len(snap), pre_ok, ntail,
                        tail_ok))

    if write:
        # THE PROMOTION IS DOWNSTREAM OF THE READ-BACK.  The payload is
        # staged beside its destination, the terminal gate is taken against
        # the STAGED bytes, and only a run that passes it promotes; a run
        # that fails removes its staging, so it leaves nothing behind.
        text = "\n".join(LINES) + "\n"
        tmp_j = OUT_JSON + ".tmp"
        tmp_t = OUT_TXT + ".tmp"
        with open(tmp_j, "w") as fh:
            json.dump(payload, fh, indent=1, sort_keys=True, default=str)
        with open(tmp_t, "w") as fh:
            fh.write(text)
        disk = json.loads(read_text(tmp_j, "ARTIFACT"))
        bad2 = SEAL.verify(disk)
        pre_ok, tail_ok, ntail = transcript_ok(read_text(tmp_t, "ARTIFACT"))
        probe = json.loads(json.dumps(disk))
        probe["totals"]["gates"] = -1
        detected = bool(SEAL.verify(probe))
        art_reads = sorted({r0["path"] for r0 in READS
                            if r0["category"] == "ARTIFACT"})
        art_ok = art_reads == sorted({os.path.relpath(tmp_j, REPO),
                                      os.path.relpath(tmp_t, REPO)})
        try:
            LD.add("G-INTEGRITY",
                   not bad2 and detected and swept and pre_ok and tail_ok
                   and art_ok,
                   "THE BYTES THAT WILL BE PROMOTED ARE THE BYTES THAT WERE "
                   "SEALED, AND THE CHECK IS SHOWN TO BE ABLE TO FAIL.  The "
                   "staged artifact is re-read FROM DISK before any promotion "
                   "and every sealed key is compared against its gate-time "
                   "digest; a deliberately corrupted probe of the same "
                   "payload is then shown to be detected, the writer is "
                   "downstream of an executed mutant sweep, and the run's own "
                   "reads register is checked to hold exactly the two staged "
                   "files it just read.  THE TRANSCRIPT IS COVERED BY "
                   "EQUALITY: the sealed prefix is re-digested from the bytes "
                   "on disk and the lines after it must equal the closing "
                   "rows rendered from the ledger.  Only then are the staged "
                   "files promoted, so a run that fails here leaves the "
                   "committed artifacts untouched",
                   "sealed keys %d, staged mismatches %s, corrupted probe "
                   "detected %s, sweep executed %s, transcript prefix %d "
                   "lines re-digested %s, trailing lines %d equal to the "
                   "rendered closing rows %s, staged reads %s"
                   % (len(SEAL.seals), bad2, detected, swept, len(snap),
                      pre_ok, ntail, tail_ok, art_ok))
        except GateFail:
            for tmp in (tmp_j, tmp_t):
                if os.path.exists(tmp):
                    os.remove(tmp)
            raise
        os.replace(tmp_j, OUT_JSON)
        os.replace(tmp_t, OUT_TXT)
    return payload, text


# ===========================================================================
# SECTION 14.  THE CLI
# ===========================================================================

def pipeline(break_anchor=None, paper_text=None, paper_rel=PAPER_REL,
             do_paper=True, write=False, swept=False, sweep_rows=None):
    (LD, SEAL, R, _G, _texts, src, tree, ptext, ptext_nm,
     _weld, _drows) = full_run(break_anchor=break_anchor,
                               paper_text=paper_text, paper_rel=paper_rel)
    payload, text = finish(LD, SEAL, R, src, tree, ptext, ptext_nm,
                           do_paper, write, swept, sweep_rows or [])
    return payload, text, LD


class _Sink:
    def write(self, _s):
        pass

    def flush(self):
        pass


def run_mutant(name, paper_text):
    global MUTANT
    MUTANT = name
    keep = sys.stdout
    n0 = len(LINES)
    try:
        sys.stdout = _Sink()
        pipeline(paper_text=paper_text, do_paper=True, write=False)
        return None
    except GateFail as e:
        return str(e)
    finally:
        sys.stdout = keep
        MUTANT = None
        del LINES[n0:]


def selftest(paper_text):
    keep = sys.stdout
    n0 = len(LINES)
    try:
        sys.stdout = _Sink()
        pipeline(break_anchor="A-PIN", paper_text=paper_text, write=False)
        return None
    except GateFail as e:
        return str(e)
    finally:
        sys.stdout = keep
        del LINES[n0:]


def parse_args(argv):
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
        out["mode"] = a
        if a in ("--mutant", "--break-anchor"):
            if i + 1 >= len(argv):
                raise CliError("%s needs a NAME" % a)
            out["arg"] = argv[i + 1]
            i += 1
        elif a == "--verify-paper":
            if i + 1 < len(argv) and not argv[i + 1].startswith("--"):
                out["arg"] = argv[i + 1]
                i += 1
        i += 1
    return out


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    try:
        opt = parse_args(argv)
    except CliError as e:
        sys.stderr.write("argv: %s\n" % e)
        return 2
    mode, arg = opt["mode"], opt["arg"]
    if mode == "--list-gates":
        for g in GATES_DECLARED:
            print(g)
        return 0
    if mode == "--list-mutants":
        for k in sorted(MUTANTS):
            print("%-18s -> %-24s %s" % (k, MUTANTS[k][1], MUTANTS[k][0]))
        return 0
    if mode in ("--mutant", "--break-anchor") and arg is None:
        return 2
    if mode == "--mutant" and arg not in MUTANTS:
        sys.stderr.write("unknown mutant %r\n" % arg)
        return 2
    if mode == "--break-anchor" and arg not in SOURCE_IDS:
        sys.stderr.write("unknown anchor %r\n" % arg)
        return 2
    paper_path = os.path.join(REPO, PAPER_REL)
    if mode == "--verify-paper" and arg:
        paper_path = arg if os.path.isabs(arg) else os.path.join(REPO, arg)
        if not os.path.isfile(paper_path):
            sys.stderr.write("not a file: %s\n" % paper_path)
            return 2
    paper_text = None
    if os.path.isfile(paper_path):
        paper_text = read_text(paper_path, "OBJECT-UNDER-TEST")
        OBJECT_READ[0] = dict(READS[-1])
    if mode == "--selftest":
        got = selftest(paper_text)
        print("selftest: corrupted anchor died at %s" % got)
        return 1 if got else 2
    if mode == "--mutant":
        got = run_mutant(arg, paper_text)
        want = MUTANTS[arg][1]
        print("mutant %s: killed at %s (declared %s)" % (arg, got, want))
        return 1 if got == want else 0
    if mode == "--break-anchor":
        try:
            pipeline(break_anchor=arg, paper_text=paper_text, write=False)
        except GateFail as e:
            print("break-anchor %s: died at %s" % (arg, e))
            return 1
        return 0
    if mode == "--verify-paper":
        try:
            pipeline(paper_text=paper_text, do_paper=True, write=False)
        except GateFail as e:
            print("verify-paper: FAILED at %s" % e)
            return 1
        print("verify-paper: clean")
        return 0
    if mode == "--numbers":
        try:
            pipeline(paper_text=paper_text, do_paper=False, write=False)
        except GateFail as e:
            print("numbers: FAILED at %s" % e)
            return 1
        return 0
    sweep_rows = []
    if mode is None:
        for name in sorted(MUTANTS):
            got = run_mutant(name, paper_text)
            sweep_rows.append({"mutant": name, "gate": MUTANTS[name][1],
                               "killed_at": got})
        bad = [r for r in sweep_rows if r["killed_at"] != r["gate"]]
        if bad:
            for r in bad:
                sys.stderr.write("mutant %s survived or died off target: %s\n"
                                 % (r["mutant"], r["killed_at"]))
            return 1
    try:
        pipeline(paper_text=paper_text, do_paper=True,
                 write=(mode is None), swept=(mode is None),
                 sweep_rows=sweep_rows)
    except GateFail as e:
        print("FAILED at %s" % e)
        return 1
    print("")
    print("OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
