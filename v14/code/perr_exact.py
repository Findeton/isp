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
    for m, c in D.items():
        ts = [site_trip(m, k) for k in range(9)]
        npd = sum(1 for t in ts if CODE_TAB[t[0] | (t[1] << 4) | (t[2] << 8)][1])
        pos[npd] += c
        if all(min(t) >= 1 for t in ts):
            ncov += c
            for t in ts:
                det[det4(t)] += c
                codes.add(t)
                if max(t) > maxcell:
                    maxcell = max(t)
            if len(set(ts)) == 1:
                homo[ts[0]] += c
    SC_CACHE[R] = {"total": sum(D.values()), "cover": ncov, "homo": homo,
                   "det": det, "pos": pos, "maxcell": maxcell,
                   "codes": sorted(codes), "distinct_fields": len(D)}
    return SC_CACHE[R]


def stratum_target_count(target, R):
    """the exact number of ordered saturating R-tuples inducing a given
    HOMOGENEOUS record, by a convolution of two half-length censuses that
    never enumerates the R-tuples themselves."""
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

    W5-LADDER:  the collinear arrangement of EVERY homogeneous record the
                R = 5 stratum reaches -- all six, none sampled.
    W5-SEEDFAN: the (1,1,3) arrangement at all 3 x 3 canonical transversal
                choices of its first two rounds -- the seed axis, declared.
    W5-CTRL:    d66's own R = 5 point.
    W6-DOOR:    the R = 6 rung -- the link-constant (2,2,2) concatenation and
                I7's own declared G-SINGULAR arrangement.
    W6-CTRL:    d66's own R = 6 point, whose committed output row this run
                reads from d66's pinned bytes."""
    out, meta = [], {}

    def add(sch, tag):
        if sch not in meta:
            out.append(sch)
            meta[sch] = tag
    for rec in records5:
        add(class_schedule(class_names_for(rec)), "W5-LADDER")
    base = class_names_for((1, 1, 3))
    for s0 in range(3):
        for s1 in range(3):
            T = tuple(CLASSES[n] for n in base)
            seeds = [canon_transversals(P)[0] for P in T]
            seeds[0] = canon_transversals(T[0])[s0]
            seeds[1] = canon_transversals(T[1])[s1]
            add(tuple((T[k], seeds[k]) for k in range(len(T))), "W5-SEEDFAN")
    add(committed_schedule(5), "W5-CTRL")
    add(class_schedule(class_names_for((2, 2, 2))), "W6-DOOR")
    add(class_schedule(class_names_for((1, 1, 4))), "W6-DOOR")
    add(committed_schedule(6), "W6-CTRL")
    add(committed_schedule(4), "W4-ANCHOR")
    return out, meta


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

    # ---- SEC 1  PROVENANCE ----------------------------------------------
    say("[SEC 1] PROVENANCE")
    texts, provrows = {}, []
    for sid, rel, sha, why in SOURCES:
        t = read_text(os.path.join(REPO, rel), "SOURCE")
        got = hashlib.sha256(t.encode("utf-8")).hexdigest()[:12]
        want = sha if break_anchor != sid else ("0" * 12)
        texts[rel] = t
        provrows.append({"id": sid, "path": rel, "declared": want,
                         "measured": got, "match": got == want, "why": why})
    bad = [p for p in provrows if not p["match"]]
    R["provenance"] = SEAL.take("provenance",
                                {"sources": provrows, "count": len(provrows)})
    LD.add("G-SOURCES",
           not bad and len(provrows) == len(SOURCES),
           "EVERY SOURCE IS READ AT ITS PINNED SHA.  The %d declared sources "
           "are read at run time and each file's measured sha256-12 equals "
           "the digest this unit froze; a single mismatch stops the run "
           "before any census is built" % len(SOURCES),
           "sources %d, mismatches %d" % (len(provrows), len(bad)))

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
    # THE CLASS-EXPLICIT REACHABILITY LADDER.  Every reachability row names
    # the CLASS it is about: a covered SITE code, a COVERING record, a
    # STRUCTURALLY LIVE record, or one of I7's DECLARED records.
    scan_to = ROUNDS + 3
    ladder_classes = []
    for pol in ("SINGULAR", "INDEFINITE"):
        row = {"polarity": pol, "scanned_to": scan_to}
        first = None
        for r in range(1, scan_to + 1):
            if class_split(r, alpha)[1][pol]:
                first = r
                break
        row["COVERED-SITE-CODE"] = first
        first = None
        for r in range(1, scan_to + 1):
            cands = sorted(c for c in class_split(r, alpha)[1][pol])
            if any(covering_with_code(c, r, alpha)[0] for c in cands):
                first = r
                break
        row["COVERING-RECORD"] = first
        first = None
        for r in range(1, scan_to + 1):
            cands = sorted(c for c in class_split(r, alpha)[1][pol])
            if any(covering_with_code(c, r, alpha, live_only=True)[0]
                   for c in cands):
                first = r
                break
        row["STRUCTURALLY-LIVE-RECORD"] = first
        dec = [sum(v) for nm, v in fam.items()
               if sig_class(tuple(v)) == pol]
        row["I7-DECLARED-RECORD"] = min(dec) if dec else None
        row["declared_names"] = sorted(nm for nm, v in fam.items()
                                       if sig_class(tuple(v)) == pol)
        ladder_classes.append(row)
    ladder_classes = pick("M-CLASS-LADDER", ladder_classes,
                          [dict(r0, **{"COVERING-RECORD":
                                       r0["COVERED-SITE-CODE"]})
                           for r0 in ladder_classes])
    R["reachability_ladder"] = SEAL.take("reachability_ladder", {
        "rows": ladder_classes,
        "classes": ["COVERED-SITE-CODE", "COVERING-RECORD",
                    "STRUCTURALLY-LIVE-RECORD", "I7-DECLARED-RECORD"],
        "note": "every reachability row names the class it is about; a floor "
                "for one class is not a floor for another"})
    LD.add("G-CLASS-LADDER",
           all(r0["COVERED-SITE-CODE"] is not None for r0 in ladder_classes)
           and all(r0["COVERED-SITE-CODE"] <= r0["COVERING-RECORD"]
                   <= r0["STRUCTURALLY-LIVE-RECORD"]
                   for r0 in ladder_classes)
           and all(r0["STRUCTURALLY-LIVE-RECORD"]
                   <= r0["I7-DECLARED-RECORD"] for r0 in ladder_classes)
           and [r0["COVERING-RECORD"] for r0 in ladder_classes
                if r0["polarity"] == "INDEFINITE"][0] > ROUNDS,
           "THE REACHABILITY LADDER IS CLASS-EXPLICIT, AND THE CLASSES DO NOT "
           "SHARE A FLOOR.  A determinant sign is reachable at four different "
           "budgets depending on WHICH class is asked about -- a covered site "
           "code, a record covering all 27 cells, a structurally live record "
           "with no foreign pair, or one of I7's own declared records -- and "
           "each floor is computed separately, in order, with the nesting "
           "checked rather than assumed",
           "; ".join("%s: site %s, covering %s, live %s, declared %s (%s)"
                     % (r0["polarity"], r0["COVERED-SITE-CODE"],
                        r0["COVERING-RECORD"],
                        r0["STRUCTURALLY-LIVE-RECORD"],
                        r0["I7-DECLARED-RECORD"], ", ".join(
                            r0["declared_names"]))
                     for r0 in ladder_classes))
    for r0 in ladder_classes:
        reg(r0["COVERED-SITE-CODE"], r0["COVERING-RECORD"],
            r0["STRUCTURALLY-LIVE-RECORD"], r0["I7-DECLARED-RECORD"])

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
           and all(need[c] == len(SITES) * sum(c) for c in homo5),
           "THE SATURATION SCHEMA, RE-PROVED AT THIS RUNG RATHER THAN "
           "INHERITED.  No round deposits more than 9 link incidences, so "
           "five rounds carry at most 45; a homogeneous record whose counts "
           "sum to 5 needs 9 x 5 = 45, and each target's requirement is "
           "recomputed from its own count vector: equality forces every "
           "round to saturate, so a census over the 36^5 saturating "
           "quintuples is exhaustive over all 280^5 for these targets",
           "budget %d = %d x %d, targets %s each needing %d incidences, "
           "forced %d of %d; saturating family %s of %s"
           % (budget, per_round, ROUNDS, [list(c) for c in homo5], budget,
              sum(1 for v in forced.values() if v), len(homo5),
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
    R["weld"] = SEAL.take("weld", {"rows": weld_rows,
                                   "fiber_law_holds": fiber_law})
    LD.add("G-WELD-ROWS",
           r4fib == p21_fibers
           and all(w["isomorphisms"] == p21["counts"]["isomorphisms"]
                   for w in weld_rows if w["reading"] == "EMBEDDING")
           and all(w["fate"] == "FOUND" for w in r6rows)
           and all(w["fate"] == "UNMOTIVATED" for w in r5rows),
           "THE WELD, RUN ON ONE INSTRUMENT AT EVERY RUNG, AND VALIDATED AT "
           "THE RUNG WHOSE ANSWER IS COMMITTED.  Weld 2's detector is "
           "carried unchanged at both readings; at R = 4 it returns "
           "paper-21's committed fibers and isomorphism count exactly, at "
           "R = 6 the link-constant record returns ZERO-FREE-ITEMS, and "
           "every R = 5 arena returns UNMOTIVATED",
           "R=4 fibers %s against paper-21's committed %s; R=5 fibers %s; "
           "R=6 (2,2,2) fibers %s; isomorphisms %d everywhere"
           % (list(r4fib), list(p21_fibers),
              [list(w["inventory"].values()) for w in r5rows
               if w["reading"] == "EMBEDDING"],
              [list(w["inventory"].values()) for w in r6rows
               if w["reading"] == "EMBEDDING"],
              p21["counts"]["isomorphisms"]))
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

    sch_list, meta = window_schedules(reached5)
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
    dia_rows = []
    r4targets = sorted(c for c in cs[4] if min(c) >= 1 and sum(c) == 4)
    r6targets = [(2, 2, 2), tuple(fam["G-SINGULAR"]), (1, 2, 3), (3, 2, 1)]
    for rec, r in ([(c, 4) for c in r4targets]
                   + [(c, ROUNDS) for c in reached5]
                   + [(c, 6) for c in r6targets]):
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
                                      if not d["naive_law_holds"]]})
    LD.add("G-DIA-LAW",
           all(d["compulsory"] == d["predicted_by_the_count_law"]
               for d in dia_rows)
           and not all(d["compulsory"] == d["predicted_by_the_naive_law"]
                       for d in dia_rows)
           and r4dia["frequency"]["DIA"] == p21_dia
           and r4dia["witnesses"] == p21_dia
           and all(d["frequency"]["ANT"] == 0 for d in dia_rows),
           "THE COMPULSORY CLASS IS A LAW, AND THE LAW HAS A BOUNDARY.  "
           "Every witness of every homogeneous record at R = 4, 5 and 6 is "
           "enumerated and each parallel class is counted against its own "
           "record: a class is compulsory exactly when the record counts its "
           "link more than once AND counts some link exactly once.  The "
           "count clause alone is FALSIFIED here -- at the link-constant "
           "record every link is counted twice and no class is compulsory at "
           "all -- so the compulsion is carried by the scarce link, and it "
           "vanishes at exactly the record where the weld turns motivated.  "
           "At R = 4 the census returns paper-21's own committed DIA row",
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
    wf = [w for w in weld_rows if w["budget"] == ROUNDS
          and w["reading"] == "EMBEDDING"][0]["inventory"]
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
        (8, "the site the local-type census is taken at", "forced", 1,
         "§2.1, by measured translation invariance"),
        (9, "the reading axis (EMBEDDING / QUOTIENT)", "declared",
         len({w["reading"] for w in weld_rows}), "weld 2's, carried unchanged"),
        (10, "I-SITE-ASSIGNMENT", "measured", wf["I-SITE-ASSIGNMENT"],
         "§6, at every arena above the floor"),
        (11, "I-DIRECTION-LABEL", "measured", wf["I-DIRECTION-LABEL"],
         "§6"),
        (12, "I-ORIENT", "measured", wf["I-ORIENT"], "§6"),
        (13, "the declared falsifier (one division withheld)", "free", "-",
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
    persist = [
        {"invariant": "the binding constraint of the price law",
         "at_the_rung_below": slack_rows[ROUNDS - 1]["binds"],
         "here": slack_rows[ROUNDS]["binds"],
         "witness": "slack %d against %d" % (slack_rows[ROUNDS - 1]["slack"],
                                             slack_rows[ROUNDS]["slack"])},
        {"invariant": "the saturation schema",
         "at_the_rung_below": "every round forced to saturate",
         "here": ("every round forced to saturate"
                  if R["saturation"]["every_round_forced_to_saturate"]
                  else "not forced"),
         "witness": "%d incidences needed against a ceiling of %d"
                    % (budget, budget)},
        {"invariant": "the weld fiber signature",
         "at_the_rung_below": [w["fiber_string"] for w in weld_rows
                               if w["budget"] == ROUNDS - 1
                               and w["reading"] == "EMBEDDING"][0],
         "here": [w["fiber_string"] for w in weld_rows
                  if w["budget"] == ROUNDS
                  and w["reading"] == "EMBEDDING"][0],
         "witness": "%d base maps read at both" % p21["counts"]["isomorphisms"]},
        {"invariant": "the fiber law (all ones iff link-constant)",
         "at_the_rung_below": "holds", "here": "holds" if fiber_law
         else "fails",
         "witness": "%d arenas" % len(weld_arenas)},
        {"invariant": "cover = positive definite",
         "at_the_rung_below": str(not [c for c in occ[ROUNDS - 1]
                                       if sig_class(c) != "POSDEF"]),
         "here": str(not occ5_bad),
         "witness": "the singular witness at %s" % (list(wit_code)
                                                    if wit_code else None)},
        {"invariant": "block quantisation (the covering class's cell ceiling)",
         "at_the_rung_below": str(occ4_max), "here": str(occ5_max),
         "witness": "cell counts %d against %d" % (occ4_max, occ5_max)},
        {"invariant": "the compulsory parallel class",
         "at_the_rung_below": "compulsory when the link is counted more than "
                              "once",
         "here": "and only when some link is counted exactly once",
         "witness": "the link-constant record at %s witnesses"
                    % com(dia_rows[[d["record"] for d in dia_rows].index(
                        list((2, 2, 2)))]["witnesses"])},
        {"invariant": "the declared-record yield",
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
    R["persistence"] = SEAL.take("persistence", {
        "rows": persist,
        "tally": {k: v for k, v in sorted(tally.items())}})
    LD.add("G-PERSISTENCE",
           all(r["verdict"] in ("PERSISTS", "TRANSFORMS",
                                "BREAKS-AT-R=%d" % ROUNDS) for r in persist)
           and all((r["at_the_rung_below"] == r["here"])
                   == (r["verdict"] == "PERSISTS") for r in persist)
           and all(persist[i]["here"] == here_measured[i]
                   for i in range(len(persist)))
           and sum(tally.values()) == len(persist),
           "THE PER-INVARIANT PERSISTENCE TABLE, EACH ROW DECIDED BY ITS OWN "
           "PAIR OF MEASUREMENTS.  Every invariant paper-21 delivered is "
           "re-measured here and its verdict is read off the comparison of "
           "the two values rather than assigned: a row PERSISTS exactly when "
           "the two agree, every row's value at this rung is re-checked "
           "against the census row that measured it, and every row carries "
           "the witness that decides it",
           "rows %d, tally %s"
           % (len(persist), {k: v for k, v in sorted(tally.items())}))
    reg(*[v for v in tally.values()])

    # ---- SEC 10  THE INTERFERENCE CENSUS, CLOSED BY THEOREM -------------
    say("")
    say("[SEC 10] THE CENSUS NOT RUN, AND THE WALLS")
    body = paper_body(paper_text or "")
    surface = json.dumps({k: R[k] for k in R}, sort_keys=True, default=str) \
        + " ".join(r0["statement"] + " " + str(r0["evidence"])
                   for r0 in LD.rows) \
        + " " + pick("M-PAPER-INTERFERENCE", body,
                     body + " the interference census at L = 5 carries here")
    surface = pick("M-INTERFERENCE", surface,
                   surface + " the interference census at L = 5 finds a "
                   "DDS-carrying ball on the R-ladder")
    banned_words = ("interference census at", "DDS-carrying", "Sidon at every")
    hits = [w for w in banned_words if w.lower() in surface.lower()]
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
           "-- every published receipt key, the statement and evidence of "
           "every gate evaluated, AND THE PAPER'S OWN BODY -- and finds no "
           "interference reading in it",
           "surface %d chars (paper body %d of them), interference readings "
           "found %d" % (len(surface), len(body), len(hits)))

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
           "manufacture a false negative; the gate scans this run's declared "
           "measurement surface AND THE PAPER'S OWN BODY -- every section but "
           "the wall section in which the abstention is stated -- rather than "
           "declaring the abstention",
           "surface %d chars, paper body %d chars, sprinkling-grade readings 0"
           % (len(surface), len(body)), wall=True)
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
           "surface is scanned for one, and so is the paper's own body",
           "surface %d chars, paper body %d chars, dimension readings 0"
           % (len(surface), len(body)), wall=True)
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
        "COVER=POSDEF BREAKS AT R=%d AFTER HOLDING AT R=%d AND R=%d -- "
        "RECORD FLOORS: G-SINGULAR R=%d, G-INDEF R=%d"
        "@EXHAUSTIVE-OVER-%s-ORDERED-GROUPING-QUINTUPLES") % (
        S["budget"], S["covered_codes"], S["posdef"], S["singular"],
        S["indefinite"], S["indefinite_det4"], S["covering_class_codes"],
        S["covering_class_max_cell"], S["covering_class_det4_support"],
        wit["code"], len([x for x in wit["site_codes"]
                          if x == wit["code"]]), len(wit["site_codes"]),
        wit["total_incidences"], wit["saturating_rounds"], S["budget"],
        S["budget"], S["budget"],
        lad[0], lad[1], S["g_singular_record_floor"],
        S["g_indef_record_floor"], "{:,}".format(ar["family"]))
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
        "RECORDS AND UNMOTIVATED EVERYWHERE ELSE; THE R=%d SIGNATURE IS THE "
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
          "AND R=%d -- RECORD FLOORS: ", "G-SINGULAR R=%d, ",
          "G-INDEF R=%d", "@EXHAUSTIVE-OVER-%s", "-ORDERED-GROUPING",
          "-QUINTUPLES"]
    seg1 = "".join(j1) % (
        s["budget"], s["covered_codes"], s["posdef"], s["singular"],
        s["indefinite"], s["indefinite_det4"], s["covering_class_codes"],
        s["covering_class_max_cell"], s["covering_class_det4_support"],
        wit["code"], len([x for x in wit["site_codes"]
                          if x == wit["code"]]), len(wit["site_codes"]),
        wit["total_incidences"], wit["saturating_rounds"], s["budget"],
        s["budget"], s["budget"], lad[0], lad[1],
        s["g_singular_record_floor"], s["g_indef_record_floor"],
        "{:,}".format(ar["family"]))
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
          "LINK-CONSTANT RECORDS AND UNMOTIVATED ", "EVERYWHERE ELSE; ",
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
          "the indefinite region is attained at R = %s as a covered site "
          "code, at R = %s as a covering record, at R = %s as a "
          "structurally live record and at R = %s as one of I7's declared "
          "records"
          % tuple(str([r0[k] for r0 in R["reachability_ladder"]["rows"]
                       if r0["polarity"] == "INDEFINITE"][0])
                  for k in ("COVERED-SITE-CODE", "COVERING-RECORD",
                            "STRUCTURALLY-LIVE-RECORD",
                            "I7-DECLARED-RECORD")),
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
    return cl


def paper_tables(R):
    """the paper's measurement TABLES, rendered row by row from the receipt
    (E-22: a table row is a claim)."""
    rows = []
    occ = R["covering_codes"]
    K = R["slack"]["buys"]
    for r in sorted(occ, key=int):
        rows.append("| %s | %s | %s | %s | %s |"
                    % (r, K["reachable_site_codes"][r], occ[r]["count"],
                       occ[r]["max_cell"],
                       "yes" if K["cover_equals_posdef"][r] else "**no**"))
    for row in R["weld"]["rows"]:
        if row["reading"] == "EMBEDDING":
            rows.append("| %s | %s | %s | %s | %s |"
                        % (row["arena"], row["budget"],
                           "/".join(str(row["inventory"][k]) for k in
                                    ("I-SITE-ASSIGNMENT", "I-DIRECTION-LABEL",
                                     "I-ORIENT")),
                           row["fate"],
                           "yes" if row["link_constant"] else "no"))
    for row in R["dia"]["rows"]:
        rows.append("| %s | %s | %s | %s | %s |"
                    % (row["record"], row["budget"], com(row["witnesses"]),
                       ", ".join(row["compulsory"]) or "none",
                       row["multisets"]))
    for row in R["choice_inventory"]:
        rows.append("| %s | %s | %s | %s | %s |"
                    % (row["item"], row["name"], row["class"], row["fiber"],
                       row["binds"]))
    for row in R["persistence"]["rows"]:
        rows.append("| %s | %s | %s | %s |"
                    % (row["invariant"], row["at_the_rung_below"],
                       row["here"], row["verdict"]))
    for row in R["reachability_ladder"]["rows"]:
        rows.append("| %s | %s | %s | %s | %s |"
                    % (row["polarity"], row["COVERED-SITE-CODE"],
                       row["COVERING-RECORD"],
                       row["STRUCTURALLY-LIVE-RECORD"],
                       row["I7-DECLARED-RECORD"]))
    for nm in sorted(R["sig_feed"]["record_floors"]):
        f = R["sig_feed"]["record_floors"][nm]
        rows.append("| %s | %s | %s | %s |"
                    % (nm, f["record"], f["budget"], f["class"]))
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
]


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
    fired = {}
    for lit, _why in EXEMPT:
        fired[lit] = len(re.findall(r"\b%s\b" % re.escape(lit), text))
    return {"numerals_scanned": len(seen), "unbacked": sorted(set(bad)),
            "number_words_scanned": len(words), "unbacked_words":
            sorted(set(w.lower() for w in badw)),
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


def waiver_ledger(LD, mutants_for_gate):
    """#34: every gate is either falsified by a declared mutant or waived
    with a machine-checked forcing that says why it cannot fail."""
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
        "G-WALL-BHS": "a scan of the declared surface; the interference "
                      "mutant demonstrates the same scanner firing",
        "G-WALL-KR": "a scan of the declared surface; the interference "
                     "mutant demonstrates the same scanner firing",
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
        "G-INTEGRITY-PRE": "the same seal and transcript comparison the "
                           "terminal integrity gate takes, which the seal and "
                           "transcript mutants falsify",
    }
    rows = []
    for name in LD.names():
        rows.append({"gate": name, "mutants": mutants_for_gate.get(name, []),
                     "waiver": waivers.get(name)})
    return rows


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
    "M-TRANSCRIPT": ("appends a forged gate line to the transcript after the "
                     "ledger is sealed", "G-INTEGRITY-PRE"),
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

        want = paper_tables(R)
        want = pick("M-PAPER-TABLE", want,
                    want[:-1] + [want[-1].replace("|", "!", 1)])
        have = markdown_table_rows(ptext)
        havec = [canon(h) for h in have]
        badrows = [w for w in want if havec.count(canon(w)) != 1]
        R["paper_tables"] = SEAL.take("paper_tables",
                                      {"rendered": len(want),
                                       "rows_in_the_paper": len(have),
                                       "not_exactly_once": badrows})
        LD.add("G-PAPER-TABLES",
               not badrows and len(want) > 0,
               "EVERY CELL OF EVERY MEASUREMENT TABLE IS RENDERED FROM THE "
               "RECEIPT AND REQUIRED TO OCCUR EXACTLY ONCE (E-22).  A table "
               "row is a claim: a forged cell dies even when every numeral "
               "in it is receipt-backed, and a duplicated row dies too",
               "rendered rows %d, table rows in the paper %d, rows not "
               "occurring exactly once %d"
               % (len(want), len(have), len(badrows)))

        cov = paper_coverage(R, pick("M-PAPER-COVERAGE", ptext,
                                     ptext + "\n\nan unbacked count: "
                                     "123456789\n"))
        R["coverage_scan"] = SEAL.take("coverage_scan", cov)
        LD.add("G-PAPER-COVERAGE",
               not cov["unbacked"] and not cov["unbacked_words"]
               and cov["exemptions_fired"] == cov["exemptions"],
               "NUMERAL COVERAGE SCANS THE WHOLE PAPER -- PROSE, TABLES, "
               "INLINE CODE SPANS AND THE FENCED VERDICT BLOCKS -- AGAINST "
               "EXACTLY THREE DECLARED LISTS: this run's registered numbers, "
               "the receipt it publishes, and a declared exemption table "
               "with a reason per literal, every one of which must fire.  "
               "The spelled-out numbers are scanned on the same terms",
               "numerals scanned %d, unbacked %s, number-words scanned %d, "
               "unbacked %s, exemptions fired %d of %d, chars %d"
               % (cov["numerals_scanned"], cov["unbacked"],
                  cov["number_words_scanned"], cov["unbacked_words"],
                  cov["exemptions_fired"], cov["exemptions"],
                  cov["chars_scanned"]))

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

    gate_of = {}
    for name, (_d, gate) in MUTANTS.items():
        gate_of.setdefault(gate, []).append(name)
    led = waiver_ledger(LD, gate_of)
    naked = [r["gate"] for r in led if not r["mutants"] and not r["waiver"]]
    R["coverage"] = SEAL.take("coverage", {
        "gates": len(led), "rows": led,
        "gates_with_a_declared_mutant": sum(1 for r in led if r["mutants"]),
        "gates_with_a_forcing_waiver": sum(1 for r in led if r["waiver"]
                                           and not r["mutants"]),
        "unguarded": naked})
    LD.add("G-COVERAGE-HONEST",
           not naked,
           "THE COVERAGE LEDGER IS HONEST: EVERY GATE IS EITHER FALSIFIED BY "
           "A DECLARED MUTANT OR WAIVED WITH A FORCING THAT SAYS WHY IT "
           "CANNOT FAIL.  The denominator is this run's own gate count "
           "rather than a hand-kept number, and a gate with neither is "
           "reported as unguarded",
           "gates %d, with a mutant %d, with a forcing waiver %d, unguarded "
           "%s" % (len(led), sum(1 for r in led if r["mutants"]),
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

    R["gates"] = SEAL.take("gates", {"rows": [dict(g) for g in LD.rows],
                                     "count": len(LD.rows),
                                     "chain": LD.chain[:12]})
    R["closing_gates"] = SEAL.take("closing_gates", {
        "names": ["G-SEAL-TOTAL", "G-INTEGRITY-PRE", "G-INTEGRITY"],
        "warrant": "these three are evaluated after the gate ledger is "
                   "snapshotted and sealed: a totality gate cannot be inside "
                   "the object it seals, and the integrity gates run against "
                   "the sealed payload and then against the bytes on disk.  "
                   "The archived transcript therefore carries their rows "
                   "while the sealed ledger does not, and a run that fails "
                   "any gate writes nothing at all"})
    snap = list(LINES)
    R["transcript_head"] = SEAL.take("transcript_head", snap[:3])
    R["transcript"] = SEAL.take("transcript", {
        "lines_sealed": len(snap),
        "digest": hashlib.sha256("\n".join(snap).encode()).hexdigest()[:12],
        "closing_lines": "the rows of the closing gates named in "
                         "closing_gates, and nothing else, may follow the "
                         "sealed prefix in the artifact"})
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
    text = "\n".join(LINES) + "\n"
    text = pick("M-TRANSCRIPT", text, text + "  [PASS] G-FORGED\n")
    tl = text.rstrip("\n").split("\n")
    pre_ok = (hashlib.sha256("\n".join(tl[:len(snap)]).encode())
              .hexdigest()[:12] == R["transcript"]["digest"])
    closing = R["closing_gates"]["names"]
    tail = [ln for ln in tl[len(snap):] if ln.strip()]
    tail_ok = all(any(g in ln for g in closing) or ln.startswith(" " * 9)
                  for ln in tail)
    LD.add("G-INTEGRITY-PRE",
           not bad and pre_ok and tail_ok,
           "THE PAYLOAD ABOUT TO BE WRITTEN IS THE PAYLOAD THAT WAS SEALED.  "
           "Every sealed key is re-digested from the serialized payload and "
           "compared against the digest taken at gate time, so a value that "
           "moved between its gate and the write is caught before any byte "
           "reaches the disk.  THE TRANSCRIPT IS COVERED LINE BY LINE ON THE "
           "SAME TERMS: the sealed prefix is re-digested from the text about "
           "to be written and every line after it must belong to a declared "
           "closing gate, so a forged late line dies here and not only at "
           "the artifact",
           "sealed keys %d, mismatches %s, transcript prefix %d lines "
           "re-digested %s, trailing lines %d all declared %s"
           % (len(SEAL.seals), bad, len(snap), pre_ok, len(tail), tail_ok))

    if write:
        tmp_j = OUT_JSON + ".tmp"
        tmp_t = OUT_TXT + ".tmp"
        with open(tmp_j, "w") as fh:
            json.dump(payload, fh, indent=1, sort_keys=True, default=str)
        with open(tmp_t, "w") as fh:
            fh.write(text)
        os.replace(tmp_j, OUT_JSON)
        os.replace(tmp_t, OUT_TXT)
        disk = json.loads(read_text(OUT_JSON, "ARTIFACT"))
        bad2 = SEAL.verify(disk)
        dl = read_text(OUT_TXT, "ARTIFACT").rstrip("\n").split("\n")
        pre_ok = (hashlib.sha256("\n".join(dl[:len(snap)]).encode())
                  .hexdigest()[:12] == R["transcript"]["digest"])
        tail = [ln for ln in dl[len(snap):] if ln.strip()]
        tail_ok = all(any(g in ln for g in closing) or ln.startswith(" " * 9)
                      for ln in tail)
        probe = json.loads(json.dumps(disk))
        probe["totals"]["gates"] = -1
        detected = bool(SEAL.verify(probe))
        LD.add("G-INTEGRITY",
               not bad2 and detected and swept and pre_ok and tail_ok,
               "THE BYTES ON DISK ARE THE BYTES THAT WERE SEALED, AND THE "
               "CHECK IS SHOWN TO BE ABLE TO FAIL.  The artifact is re-read "
               "from disk and every sealed key is compared against its "
               "gate-time digest; a deliberately corrupted probe of the same "
               "payload is then shown to be detected, and the writer is "
               "downstream of an executed mutant sweep.  THE TRANSCRIPT IS "
               "COVERED LINE BY LINE: the sealed prefix is re-digested from "
               "the bytes on disk and every line after it must belong to a "
               "declared closing gate, so a forged late line dies",
               "sealed keys %d, disk mismatches %s, corrupted probe detected "
               "%s, sweep executed %s, transcript prefix %d lines re-digested "
               "%s, trailing lines %d all declared %s"
               % (len(SEAL.seals), bad2, detected, swept, len(snap), pre_ok,
                  len(tail), tail_ok))
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
        for g in sorted({v[1] for v in MUTANTS.values()}):
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
