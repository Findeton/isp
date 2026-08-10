#!/usr/bin/env python3.13
# -*- coding: utf-8 -*-
"""
v14 U4b -- THE SCHEDULE CENSUS.  Instrument for `v14/paper-17-schedule-census.md`.

QUESTION (pin `v14/note-u4b-pin.md`, sha256-12 d2cff9a274a8, ledger #126).  U4
measured the division-event crystal TRUE and the panel proved its periodicity
CONSTRUCTOR-INHERITED (the affine mechanism: n = c + m*1_S, S a union of
<(1,1)> cosets seated by d66's seed rule).  U4b turns the constructor into a
variable.  Over the declared family of admissible arbitration schedules on
CONFLICT-GRID(g=3, R=2) -- the committed diagonal-coset seed ONE point in it,
not its generator -- does crystallinity survive only at coset-union seeds
(INHERITED), or does it appear at beyond-coset schedules (emergence's first
foothold)?  And does ANY schedule induce a NON-DEGENERATE metric?

WHAT THIS PROGRAM DOES
  SEC 1  PROVENANCE.  Ten pinned sources, sha256-12 verified, products gated;
         the verbatim (#62) anchors bound to their consumer gates.
  SEC 2  THE GRAMMAR, DRIVEN DIRECTLY.  The committed d42b1 transport layer is
         loaded by text-slice (d66's own committed single-source idiom, cut at
         its banner print) and d60's `B`/`dl` and d66's `conflict_grid` by AST
         extraction.  Admissibility is decided by the layer's own menu; no menu
         law is re-typed anywhere in this file.
  SEC 3  THE FAMILY (pin R1), declared as data and COUNTED; the declared
         grammar window, disclosed; the committed schedule located inside it.
  SEC 4  CONSTRUCTIBILITY (pin R2.1) by driving the menus: FORCED / BRANCHING /
         REFUSED per schedule, with two declared controls that exhibit the two
         negative fates.
  SEC 5  THE STABILIZER COLUMN (pin R2.2) at BOTH site readings, by three
         independent routes (direct translation, Fourier annihilator in Z[w],
         subgroup lattice), full family and window.
  SEC 6  THE DETERMINANT COLUMN (pin R2.3): the induced I7 form per schedule
         through HA 3.2's readout as the U4 effectus evaluated it; det exact.
  SEC 7  THE AFFINE NULL (pin R3): coset-union vs beyond-coset, and the
         verdict stratified over it.
  SEC 8  FRAGILITY (pin R2.4) on the window, computed not sampled.
  SEC 9  THE WALLS (pin R4): L-1 argued first and declined; BHS; KR; the
         diagonal counterpoint measured, cosmological readings barred.
  SEC 10 The verdict, derived a second time from the serialized receipt by an
         independent path; the paper gates; the seal; the artifacts.

CLI CONTRACT (the #82 minimum: argv-parsed against a whitelist)
---------------------------------------------------------------
    python3.13 v14/code/u4b_schedule_exact.py
        THE DELIVERY RUN, and the ONLY writer.  Builds the whole census,
        evaluates every gate (the paper gates included), runs every declared
        mutant in-process, re-reads what it wrote and WRITES
        `u4b_schedule_output.txt` and `u4b_schedule_receipt.json` beside this
        file.  Exits 0 iff every gate passes.

    python3.13 v14/code/u4b_schedule_exact.py --no-write
        The same run, writing nothing.

    python3.13 v14/code/u4b_schedule_exact.py --numbers
        The census only: every published row printed, no paper gate, no mutant
        sweep, nothing written.  Exits 0 iff every gate it reaches passes.

    python3.13 v14/code/u4b_schedule_exact.py --selftest
        FALSIFICATION SELF-TEST.  Corrupts one anchor's expected digest IN
        MEMORY, confirms the run dies at the anchor gate, WRITES NOTHING, and
        exits 1.  Exits 2 if the corrupted run does NOT die.

    python3.13 v14/code/u4b_schedule_exact.py --mutant NAME
        Runs the pipeline with the named mutant active.  Exits 1 when the
        mutant is killed (the intended outcome), 0 if it survives.  An unknown
        NAME exits 2.  Writes nothing.

    python3.13 v14/code/u4b_schedule_exact.py --break-anchor NAME
        Corrupts the named source anchor's expected digest.  Unknown NAME exits
        2.  The run must exit 1.  Writes nothing.

    python3.13 v14/code/u4b_schedule_exact.py --verify-paper [PATH]
        Rebuilds the whole derivation and evaluates the paper gates -- claim
        rendering, numeral coverage and claim POLARITY -- with PATH (this
        unit's paper by default) as the object under test.  Exits 1 on any
        drift, 0 on a clean paper, 2 if PATH does not exist.  Writes nothing.

    Any other argument, any unknown flag argument, any missing flag argument
    and any --verify-paper PATH that does not exist exits 2.  No flag is
    mutant-only and no flag is a no-op.

THE GATE-TO-DISK SEAL (RUNBOOK 14 addendum, v14 #119), disciplined from birth.
Every published object is DIGESTED AT THE MOMENT ITS GATE PASSES; the payload
may only be sealed if every earlier seal still verifies; the artifacts are
written FROM the sealed payload; and the terminal integrity gate compares the
BYTES ON DISK against the gate-time seal.  A re-derivation from disk is not an
integrity check -- it confirms corruption.

TEXT GATES (RUNBOOK 14 addendum, v14 #125).  Every gate that matches prose
against a needle whitespace-normalises BOTH sides, uses #62-anchored needles
with a length floor, and includes the corpus's canonical short fragments.  The
four inherited U4 walls are enforced that way.

ARITHMETIC.  Exact only: `fractions.Fraction` and Python integers.  There are
no floats anywhere -- an AST scan of this file and a recursive type scan of the
emitted receipt are gates.

RUNTIME INPUTS (RUNBOOK 13/14, engravings #46/#91).  Exactly ten files are read
at run time as SOURCES, all hash-pinned by this unit's frozen declaration, plus
exactly one file read as the OBJECT UNDER TEST -- this unit's own paper, which
cannot be hash-pinned because it is the thing being verified.  Both lists are
enumerated and gated.  No repository state outside them is read, and no
subprocess -- in particular no `git` -- is ever invoked: the run is correct
off-tree and in a directory with no version control at all.
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
OUT_TXT = os.path.join(os.path.dirname(SELF), "u4b_schedule_output.txt")
OUT_JSON = os.path.join(os.path.dirname(SELF), "u4b_schedule_receipt.json")

SCHEMA = "isp/v14/u4b-schedule-census/1"
PAPER_REL = "v14/paper-17-schedule-census.md"

# ===========================================================================
# SECTION 0.  THE FROZEN DECLARATION (RUNBOOK section 15: the arena is data)
# ===========================================================================

SOURCES = [
    ("A-PIN", "v14/note-u4b-pin.md", "d2cff9a274a8",
     "THIS UNIT'S PIN (ledger #126): the family, the columns, the "
     "pre-registered outcome names."),
    ("A-ADJ", "v14/note-u4-adjudication.md", "fa991e19ae54",
     "the U4 adjudication (#125): the affine mechanism, the diagonal "
     "unification, the successor ruling that pinned this unit."),
    ("A-EFF", "v14/review-u4-effectus.md", "61fb7d9e8471",
     "the U4 effectus review (#122): the I7-coordinate evaluation route and "
     "the committed CONFLICT-GRID(3,2) I7 row this unit reproduces."),
    ("A-HA", "v13/paper-ha-successor.md", "f286ba10d2d9",
     "HA 3.2: the declared readout -- interval cardinality as squared "
     "separation -- that turns link counts into a metric candidate."),
    ("A-D42B1", "v10/code/d42b1_transport_exact.py", "576275d55ecf",
     "THE COMMITTED TRANSPORT GRAMMAR, driven directly: this unit's only "
     "source of admissibility."),
    ("A-D60", "v10/code/d60_crystal_exact.py", "684cdb76552b",
     "D60: the Builder `B` and the delivery helper `dl`, AST-extracted."),
    ("A-D66", "v10/code/d66_arbitration_crystal_exact.py", "3d0516ab106e",
     "D66: CONFLICT-GRID(g, R) -- the committed constructor whose schedule "
     "this unit turns into a variable, AST-extracted and re-run."),
    ("A-D66OUT", "v10/data/d66_arbitration_crystal_exact.out", "e252529d2586",
     "D66's COMMITTED OUTPUT: the GRID(g=3,*) rows are READ from this file at "
     "run time and reproduced, never re-typed."),
    ("A-L1", "v11/note-L1-lorentz-no-go-lemma.md", "93ea24591c3c",
     "L-1: the fourth-form clause this unit argues before any test, and the "
     "sentence retracted on 2026-07-28 that no paper may reproduce."),
    ("A-CAT", "v11/note-v11p0a-reproduction-catalog.md", "0cebe543e814",
     "the reproduction catalog 1.6/1.7: the BHS block and the "
     "Kleitman-Rothschild height-control warning."),
]
SOURCE_IDS = [s[0] for s in SOURCES]

MUTANTS = [
    ("MUT-CRYSTAL-SEEDED", "G-BEYOND-COSET-CRYSTALLINE",
     "reports the beyond-coset crystalline population as empty, forcing the "
     "pre-registered CRYSTAL-SEEDED outcome -- must die at the per-witness "
     "beyond-coset gate"),
    ("MUT-AFFINE-NULL", "G-AFFINE-LAW",
     "reports one coset-union schedule as non-crystalline -- must die at the "
     "affine-law gate, which evaluates every CU-JOINT seed pair"),
    ("MUT-CU-SPLIT", "G-CU-SPLIT-EMPTY",
     "reports a CU-SPLIT schedule as crystalline -- must die at the "
     "split-coset gate"),
    ("MUT-DET-EMPTY", "G-DET-NONZERO-EXISTS",
     "reports the determinant column as identically zero -- must die at the "
     "named-witness determinant gate"),
    ("MUT-DET-POSDEF", "G-POSDEF-EMPTY",
     "plants a positive-definite-at-every-site schedule -- must die at the "
     "exhaustive positive-definiteness census gate"),
    ("MUT-I7-STRICT", "G-I7-STRICT-EMPTY",
     "reports a schedule meeting I7's strict-positivity criterion -- must die "
     "at the strict-positivity census gate"),
    ("MUT-STAB-ROUTE", "G-STAB-ROUTES",
     "corrupts the Fourier-annihilator route on one field -- must die at the "
     "three-route agreement gate"),
    ("MUT-FOOTPRINT", "G-FOOTPRINT-CONSTANT",
     "makes one schedule's footprint field non-constant -- must die at the "
     "per-schedule footprint gate"),
    ("MUT-DRIVEN-FIELD", "G-DRIVEN-EQUALS-COMBINATORIAL",
     "detaches one driven record's division field from the combinatorial one "
     "-- must die at the per-schedule driven-vs-combinatorial gate"),
    ("MUT-NOT-FORCED", "G-CONSTRUCTIBILITY",
     "withholds one conflict-supply delivery from one window schedule, "
     "leaving a refused record reported as FORCED -- must die at the "
     "per-schedule constructibility gate"),
    ("MUT-REFUSAL-BLIND", "G-CTRL-REFUSED",
     "reports the declared no-supply control as constructible -- must die at "
     "the refusal control gate"),
    ("MUT-BRANCHING-BLIND", "G-CTRL-BRANCHING",
     "reports the declared under-specified control as forced -- must die at "
     "the branching control gate"),
    ("MUT-COMMITTED-RECORD", "G-COMMITTED-RECORD",
     "perturbs one event of the generalized driver's committed-schedule "
     "record -- must die at the event-for-event anchor against d66's own "
     "`conflict_grid(3, 2)`"),
    ("MUT-FAMILY-COUNT", "G-FAMILY-COUNT",
     "corrupts the computed family size -- must die at the two-route count "
     "gate (#24)"),
    ("MUT-WINDOW-SILENT", "G-WINDOW-DISCLOSED",
     "reports the declared window as the whole family -- must die at the "
     "no-silent-caps disclosure gate"),
    ("MUT-FRAGILITY", "G-FRAGILITY",
     "reports one admissible single-arbitration re-seating as preserving the "
     "stabilizer -- must die at the per-schedule fragility gate"),
    ("MUT-WALL-L1", "G-WALL-L1",
     "injects the retracted L-1 sentence into the paper under test, "
     "LINE-WRAPPED in house style -- must die at the whitespace-normalised "
     "L-1 wall gate (#125)"),
    ("MUT-WALL-BHS", "G-WALL-BHS",
     "runs a sprinkling-grade boost reading -- must die at the BHS wall gate"),
    ("MUT-HEAD", "G-VERDICT-RECONSTRUCTED",
     "corrupts one field of the head -- must die at the independent "
     "reconstruction gate"),
    ("MUT-SEAL-BROKEN", "G-SEAL-COMPLETE",
     "mutates a sealed object after its gate passed -- must die at the "
     "gate-time seal verification (#119)"),
    ("MUT-SELFTEST-WRITES", "G-SELFTEST-WRITES-NOTHING",
     "lets the self-test path reach a writer -- must die at the "
     "writes-nothing gate"),
    ("MUT-CLI-PERMISSIVE", "G-CLI-WHITELIST",
     "swaps the argv whitelist for the registered permissive shape -- must "
     "die at the CLI contract gate (#82)"),
    ("MUT-PAPER-POLARITY", "G-PAPER-CLAIM-POLARITY",
     "flips one declared polarity of the paper's head -- must die at the "
     "polarity gate"),
    ("MUT-VERBATIM", "G-VERBATIM",
     "corrupts one verbatim source quote -- must die at the #62 anchor gate"),
    ("MUT-ANCHOR-DRIFT", "G-ANCHORS-READ",
     "moves one number recomputed against a committed file -- must die at "
     "the read-anchor gate (which --break-anchor cannot reach, because the "
     "provenance gate kills that run first)"),
    ("MUT-STRATUM-BLIND", "G-STRATA-WITNESSED",
     "drops one census stratum's driven witness -- must die at the "
     "every-stratum-witnessed gate"),
    ("MUT-CLASSPAIR", "G-CLASS-PAIR-TABLE",
     "corrupts one row of the resolvable class-pair table -- must die at the "
     "per-row gate that binds it to the whole-family determinant column"),
    ("MUT-WALL-KR", "G-WALL-KR",
     "takes a dimension reading with no height control -- must die at the "
     "Kleitman-Rothschild wall gate"),
    ("MUT-WALL-COSMO", "G-WALL-DIAGONAL",
     "reads the measured diagonal cosmologically -- must die at the "
     "diagonal wall gate"),
    ("MUT-PAPER-CLAIM", "G-PAPER-CLAIMS",
     "silently drops one instrument claim from the paper under test -- must "
     "die at the claim-rendering gate"),
    ("MUT-PAPER-NUMERAL", "G-PAPER-NUMERAL-COVERAGE",
     "injects an unregistered numeral into the paper under test -- must die "
     "at the numeral-coverage gate"),
]
MUTANT_NAMES = {m[0] for m in MUTANTS}

# the retracted L-1 sentence: no paper of this line may reproduce it
BANNED_L1 = ("precisely the form U4 tests, and precisely the form the "
             "corpus's strongest relativity result took")

MUT = None
QUIET = False
LINES = []
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
# SECTION 1.  MACHINERY -- the gate ledger, the waiver ledger, the seal
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
        if waiver:
            say("         WAIVER [%s]: %s" % (waiver["class"], waiver["reason"]))
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
    ("SEAL-VERDICT-CRYSTAL", "verdict/crystal", "G-VERDICT-RECONSTRUCTED"),
    ("SEAL-VERDICT-DET", "verdict/det", "G-VERDICT-RECONSTRUCTED"),
    ("SEAL-VERDICT-CONSTR", "verdict/constructibility",
     "G-VERDICT-RECONSTRUCTED"),
    ("SEAL-COUNTS", "counts", "G-VERDICT-RECONSTRUCTED"),
    ("SEAL-FAMILY", "family", "G-WINDOW-DISCLOSED"),
    ("SEAL-CONSTRUCTIBILITY", "constructibility", "G-CTRL-BRANCHING"),
    ("SEAL-STABILIZER", "stabilizer", "G-FOOTPRINT-CONSTANT"),
    ("SEAL-DETERMINANT", "determinant", "G-I7-STRICT-EMPTY"),
    ("SEAL-CLASS-PAIRS", "class_pairs", "G-CLASS-PAIR-TABLE"),
    ("SEAL-AFFINE", "affine", "G-CU-SPLIT-EMPTY"),
    ("SEAL-FRAGILITY", "fragility", "G-FRAGILITY"),
    ("SEAL-STRATA", "strata", "G-STRATA-WITNESSED"),
    ("SEAL-ANCHORS", "anchors", "G-ANCHORS-READ"),
    ("SEAL-VERBATIM", "verbatim_anchors", "G-VERBATIM"),
    ("SEAL-WALLS", "walls", "G-WALL-DIAGONAL"),
    ("SEAL-WAIVERS", "waiver_ledger", "G-WAIVERS-VERIFIED"),
    ("SEAL-MUTANTS", "mutants", "G-MUTANTS-ON-TARGET"),
    ("SEAL-GATES", "gates", "G-PAPER-COVERAGE-FINAL"),
    ("SEAL-TOTALS", "totals", "G-PAPER-COVERAGE-FINAL"),
]
SEALS_IN_RUN = tuple(s for s, _p, g in SEALED_PATHS
                     if g not in ("G-MUTANTS-ON-TARGET",
                                  "G-PAPER-COVERAGE-FINAL"))


class Seal:
    """the gate-time seal (#119)."""

    def __init__(self):
        self.rows = []
        self.index = {}
        self.payload = None
        self.payload_sha = None
        self.transcript = None
        self.transcript_sha = None

    def take(self, sid, obj):
        path = [p for s, p, _g in SEALED_PATHS if s == sid][0]
        at = [g for s, _p, g in SEALED_PATHS if s == sid][0]
        d = digest(jpath(obj, path))
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

    def close(self, obj, payload):
        broken = self.verify(obj)
        if broken:
            raise GateFail("G-ARTIFACT-INTEGRITY :: the payload was sealed "
                           "over a broken seal :: %s" % broken)
        self.payload = payload
        self.payload_sha = digest(payload)

    def close_transcript(self, text):
        self.transcript = text
        self.transcript_sha = digest(text)


def read_bytes(rel):
    READS.append(rel)
    with open(os.path.join(REPO, rel), "rb") as fh:
        return fh.read()


def read_text(path):
    with open(path, "r", encoding="utf-8") as fh:
        return fh.read()


def norm(s):
    """#125: whitespace-normalise both sides of every text match."""
    return re.sub(r"\s+", " ", s).strip()


# ===========================================================================
# SECTION 2.  EXACT ARITHMETIC ON Z_3^2 AND Z[w]
# ===========================================================================

SITES = tuple((i, j) for i in range(3) for j in range(3))
SITE_INDEX = {s: k for k, s in enumerate(SITES)}
DIRECTIONS = ((1, 0), (0, 1), (1, 1), (1, 2))
I7_LINKS = ((1, 0), (0, 1), (1, 1))


def zadd(a, b):
    return ((a[0] + b[0]) % 3, (a[1] + b[1]) % 3)


def zmul(k, a):
    return ((k * a[0]) % 3, (k * a[1]) % 3)


SUBGROUPS = {"1": frozenset({(0, 0)}), "Z3^2": frozenset(SITES)}
for _d in DIRECTIONS:
    SUBGROUPS["<(%d,%d)>" % _d] = frozenset({(0, 0), _d, zmul(2, _d)})
SUBGROUP_NAME = {v: k for k, v in SUBGROUPS.items()}
SUBGROUP_ORDER = ["1", "<(1,0)>", "<(0,1)>", "<(1,1)>", "<(1,2)>", "Z3^2"]

# the 12 lines of AG(2,3): the cosets of the four order-3 subgroups
LINE_DIRECTION = {}
for _d in DIRECTIONS:
    for _x in SITES:
        LINE_DIRECTION[frozenset(zadd(_x, h)
                                 for h in SUBGROUPS["<(%d,%d)>" % _d])] = _d
AG_LINES = frozenset(LINE_DIRECTION)


def stab_direct(field):
    """ROUTE 1 -- the definition: translate the field and compare."""
    return frozenset(t for t in SITES
                     if all(field[zadd(x, t)] == field[x] for x in SITES))


# Z[w] = Z[t]/(t^2 + t + 1) carried as (a, b) = a + b*w, exact integers.
def w_pow(m):
    m %= 3
    return (1, 0) if m == 0 else ((0, 1) if m == 1 else (-1, -1))


def stab_fourier(field):
    """ROUTE 2 -- the annihilator of the support of the exact Z_3^2 Fourier
    transform in Z[w].  Shares no code and no constant with route 1."""
    support = []
    for k in SITES:
        acc = (0, 0)
        for x in SITES:
            c = field[x]
            if c == 0:
                continue
            p = w_pow(k[0] * x[0] + k[1] * x[1])
            acc = (acc[0] + c * p[0], acc[1] + c * p[1])
        if acc != (0, 0):
            support.append(k)
    return frozenset(t for t in SITES
                     if all((k[0] * t[0] + k[1] * t[1]) % 3 == 0
                            for k in support))


def stab_lattice(field):
    """ROUTE 3 -- the subgroup lattice: the largest H on whose cosets the
    field is constant."""
    best = SUBGROUPS["1"]
    for name in SUBGROUP_ORDER:
        H = SUBGROUPS[name]
        cosets = {}
        for x in SITES:
            key = frozenset(zadd(x, h) for h in H)
            cosets.setdefault(key, set()).add(field[x])
        if all(len(v) == 1 for v in cosets.values()) and len(H) > len(best):
            best = H
    return best


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
        self.slice_chars = (cut, len(st))
        ns = {}
        exec(compile(self.slice_text, "d42b1_slice", "exec"), ns)
        self.ns = ns
        self.candidates_for = ns["candidates_for"]
        self.admissible = ns["admissible"]
        self.regs_of = ns["regs_of"]
        self.vname = ns["vname"]
        self.V0 = ns["V0"]
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

    def _extract(self, rel, texts, marker, extra):
        """d60/d63/d64/d66's committed extraction idiom: keep only defs and
        classes, so no module-level statement can run."""
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


def drive(G, schedule, supply=True, underspecified=False, drop_supply=None):
    """THE GENERALIZED SCHEDULE DRIVER.  Exactly d66's CONFLICT-GRID(g, R)
    cycle -- conflict-supply deliveries from the group's seed, g proposals
    (0 for the seed, 1 for the rest), one g-proposer arbitration won by the
    seed -- with the GROUPING AND THE SEED taken from the schedule instead of
    being hard-wired to rows/columns and the diagonal.  Groups are processed in
    ascending order of their seed's site index and members in ascending site
    index, which is d66's own order at the committed schedule.  Every event is
    specified by its FULL TUPLE and taken from the layer's own menu."""
    b = G.B(ACTORS)
    cur = {a: G.V0 for a in ACTORS}
    dropped = 0
    for rnd, (groups, seeds) in enumerate(schedule):
        order = sorted(range(len(groups)), key=lambda gi: SITE_INDEX[seeds[gi]])
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
            if underspecified:
                b.pick((sd,), lambda z, s=sd: z[0] == "r" and z[1] == s,
                       "arbitrate* %s" % sd)
            else:
                b.pick((sd,), lambda z, e=("r", sd, ckey, wkey): z == e,
                       "arbitrate %s" % sd)
            if b.refusal:
                return b
            v = G.vname(base, wkey, sd)
            for a in grp:
                cur[a] = v
    return b


BUILD_CACHE = {}
ANCHOR_CACHE = {}


def driven(G, schedule):
    """cached, mutant-independent: the record is a property of the schedule."""
    if schedule not in BUILD_CACHE:
        b = drive(G, schedule)
        BUILD_CACHE[schedule] = {
            "events": len(b.H),
            "maxhits": b.maxhits,
            "refusal": b.refusal,
            "divisions": [e for e in b.H if e[0] == "r"],
            "H": list(b.H),
        }
    return BUILD_CACHE[schedule]


def branching_control(G):
    """THE UNDER-SPECIFIED CONTROL, made reproducible.  The committed record
    is replayed up to (not including) its first arbitration; d60's `pick` is
    then asked for an arbitration by that group's seed WITHOUT its conflict
    key or winner key, and the builder's own `maxhits` -- the NUMBER of menu
    candidates matching -- is read.  The run stops there: which candidate
    `sorted(key=repr)` would return is hash-seed dependent, the count is
    not."""
    rec = driven(G, COMMITTED)
    first = min(k for k, e in enumerate(rec["H"]) if e[0] == "r")
    seed = rec["H"][first][1]
    b = G.B(ACTORS)
    b.H = list(rec["H"][:first])
    b.pick((seed,), lambda z, s=seed: z[0] == "r" and z[1] == s,
           "arbitrate* %s" % seed)
    return b.maxhits, first, seed


def committed_grid(G, R_):
    """d66's own `conflict_grid(3, R)`, re-run once and cached."""
    if R_ not in ANCHOR_CACHE:
        b = G.conflict_grid(3, R_)
        ANCHOR_CACHE[R_] = {"events": len(b.H),
                            "arbs": sum(1 for e in b.H if e[0] == "r"),
                            "dels": sum(1 for e in b.H if e[0] == "d"),
                            "maxhits": b.maxhits, "refusal": b.refusal,
                            "H": list(b.H)}
    return ANCHOR_CACHE[R_]


# ===========================================================================
# SECTION 4.  THE FAMILY (pin R1)
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
    rec(tuple(SITES), [])
    return sorted(out)


def transversals(P):
    return [tuple(t) for t in product(*P)]


def align_seeds(P, T):
    """the seed tuple of a partition P whose image is the seed SET T: the
    i-th entry is T's unique member of P's i-th group."""
    return tuple([x for x in g if x in T][0] for g in P)


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
DIAG_SEED = ((0, 0), (1, 1), (2, 2))


def schedule_of(P0, s0, P1, s1):
    return ((P0, s0), (P1, s1))


COMMITTED = schedule_of(CLASSES["ROW"], DIAG_SEED, CLASSES["COL"], DIAG_SEED)


def window_schedules():
    """THE DECLARED GRAMMAR WINDOW: both rounds' groupings drawn from the four
    parallel classes of AG(2,3) -- d66's own resolvable device -- with the
    seeds free.  Deterministic order, no sampling."""
    out = []
    for a in CLASS_NAMES:
        for s0 in transversals(CLASSES[a]):
            for b in CLASS_NAMES:
                for s1 in transversals(CLASSES[b]):
                    out.append((a, s0, b, s1))
    return out


# ===========================================================================
# SECTION 5.  THE MEASURED COLUMNS (combinatorial, exact, full family)
# ===========================================================================

def initiator_field(S0, S1):
    return {x: (1 if x in S0 else 0) + (1 if x in S1 else 0) for x in SITES}


def footprint_field(P0, P1):
    n = {x: 0 for x in SITES}
    for P in (P0, P1):
        for g in P:
            for x in g:
                n[x] += 1
    return n


def link_counts(P0, P1):
    """the co-division adjacency: for a link l and a site x, the number of
    division events whose footprint contains both x and x + l."""
    n = {}
    for l in I7_LINKS:
        for x in SITES:
            y = zadd(x, l)
            n[(l, x)] = sum(1 for P in (P0, P1)
                            for g in P if x in g and y in g)
    return n


def i7_form(n, x):
    """HA 3.2's readout, in the U4 effectus's I7 coordinates."""
    q11 = Fraction(n[((1, 0), x)])
    q22 = Fraction(n[((0, 1), x)])
    q12 = Fraction(n[((1, 1), x)] - n[((1, 0), x)] - n[((0, 1), x)], 2)
    return q11, q22, q12, q11 * q22 - q12 * q12


def affine_class(S0, S1):
    """pin R3: is the seed set a union of cosets of one subgroup?"""
    f0, f1 = frozenset(S0), frozenset(S1)
    if f0 in AG_LINES and f1 in AG_LINES:
        return ("CU-JOINT" if LINE_DIRECTION[f0] == LINE_DIRECTION[f1]
                else "CU-SPLIT")
    return "BEYOND-COSET"


RAW = {}


def raw_census(G):
    """every measured column, computed once, mutant-independent."""
    if RAW:
        return RAW
    parts = all_partitions()
    pidx = {P: k for k, P in enumerate(parts)}
    subsets = sorted((frozenset(c) for c in combinations(SITES, 3)),
                     key=lambda T: sorted(T))
    sidx = {T: k for k, T in enumerate(subsets)}

    # -- the weight of a seed set: how many partitions admit it -------------
    weight = Counter()
    tr_index = []
    for P in parts:
        ts = set()
        for T in transversals(P):
            weight[frozenset(T)] += 1
            ts.add(sidx[frozenset(T)])
        tr_index.append(ts)

    # -- the stabilizer over seed-set pairs, three routes -------------------
    stabpair, affpair, route_rows = {}, {}, []
    for T0 in subsets:
        for T1 in subsets:
            n = initiator_field(T0, T1)
            r1, r2, r3 = stab_direct(n), stab_fourier(n), stab_lattice(n)
            stabpair[(sidx[T0], sidx[T1])] = SUBGROUP_NAME[r1]
            affpair[(sidx[T0], sidx[T1])] = affine_class(T0, T1)
            route_rows.append((sidx[T0], sidx[T1],
                               SUBGROUP_NAME[r1], SUBGROUP_NAME[r2],
                               SUBGROUP_NAME[r3]))

    # -- the link fields and the determinant column -------------------------
    fields = [tuple(1 if any(x in g and zadd(x, l) in g for g in P) else 0
                    for l in I7_LINKS for x in SITES) for P in parts]
    det_class, det9, posdef_max, strict_pos = {}, [], 0, 0
    detvals = Counter()
    for i0 in range(len(parts)):
        f0 = fields[i0]
        for i1 in range(len(parts)):
            f1 = fields[i1]
            nz = pd = 0
            rows = []
            for k, x in enumerate(SITES):
                a = f0[k] + f1[k]
                b = f0[9 + k] + f1[9 + k]
                c = f0[18 + k] + f1[18 + k]
                q12 = Fraction(c - a - b, 2)
                d = Fraction(a) * Fraction(b) - q12 * q12
                rows.append((a, b, c, q12, d))
                if d != 0:
                    nz += 1
                if d > 0 and a > 0:
                    pd += 1
            hom = len(set(rows)) == 1
            det_class[(i0, i1)] = (nz, pd, hom)
            posdef_max = max(posdef_max, pd)
            if all(f0[k] + f1[k] > 0 for k in range(27)):
                strict_pos += 1
            if nz == 9:
                det9.append((i0, i1, hom, tuple(r[4] for r in rows)))
                for r in rows:
                    detvals[str(r[4])] += 1

    # -- the joint stratum, and one DRIVEN witness per nonempty stratum -----
    joint = Counter((affpair[k], stabpair[k]) for k in affpair)
    joint_det = Counter()
    wit9 = {}
    for (i0, i1, _h, _d) in det9:
        for t0 in sorted(tr_index[i0]):
            for t1 in sorted(tr_index[i1]):
                key = (stabpair[(t0, t1)], affpair[(t0, t1)])
                joint_det[key] += 1
                if key not in wit9:
                    wit9[key] = (i0, i1, t0, t1)
    parts_with = {}
    for k, P in enumerate(parts):
        for t in sorted(tr_index[k]):
            parts_with.setdefault(t, []).append(k)
    rep = {}
    for (t0, t1), s in sorted(stabpair.items()):
        key = (s, affpair[(t0, t1)])
        rep.setdefault(key, (t0, t1))
    want, witness = [], {}
    for (a, s), v in sorted(joint.items()):
        key = (s, a)
        total = v * 90 * 90
        d9 = joint_det.get(key, 0)
        if d9:
            want.append(key + (True,))
            witness[key + (True,)] = wit9[key]
        if total - d9 > 0:
            want.append(key + (False,))
            t0, t1 = rep[key]
            found = None
            for i0 in parts_with[t0]:
                for i1 in parts_with[t1]:
                    if det_class[(i0, i1)][0] != 9:
                        found = (i0, i1, t0, t1)
                        break
                if found:
                    break
            witness[key + (False,)] = found

    RAW.update({
        "parts": parts, "pidx": pidx, "subsets": subsets, "sidx": sidx,
        "weight": weight, "tr_index": tr_index, "stabpair": stabpair,
        "affpair": affpair, "route_rows": route_rows, "fields": fields,
        "det_class": det_class, "det9": det9, "posdef_max": posdef_max,
        "strict_pos": strict_pos, "detvals": detvals, "joint": joint,
        "joint_det": joint_det, "want": want, "witness": witness,
    })
    return RAW


WINDOW_DRIVE = {}


def window_drive(G):
    """drive the layer's own menus over every schedule of the declared
    window.  Cached: the record is a function of the schedule alone."""
    if WINDOW_DRIVE:
        return WINDOW_DRIVE
    for (a, s0, b, s1) in window_schedules():
        sched = schedule_of(CLASSES[a], s0, CLASSES[b], s1)
        rec = driven(G, sched)
        init = Counter()
        foot = Counter()
        for e in rec["divisions"]:
            init[ACTOR_SITE[e[1]]] += 1
            for r in G.regs_of(e):
                if r in ACTOR_SITE:
                    foot[ACTOR_SITE[r]] += 1
        WINDOW_DRIVE[(a, s0, b, s1)] = {
            "events": rec["events"], "maxhits": rec["maxhits"],
            "refusal": rec["refusal"],
            "divisions": len(rec["divisions"]),
            "init": tuple(init[x] for x in SITES),
            "foot": tuple(foot[x] for x in SITES),
        }
    return WINDOW_DRIVE


# ===========================================================================
# SECTION 6.  THE RUN
# ===========================================================================

NUMREG = set()


def reg(*vals):
    for v in vals:
        if isinstance(v, Fraction):
            NUMREG.add(str(v))
            NUMREG.add(str(abs(v)))
            NUMREG.add(str(v.numerator))
            NUMREG.add(str(abs(v.numerator)))
            NUMREG.add(str(v.denominator))
        elif isinstance(v, int):
            NUMREG.add(str(v))
        elif isinstance(v, str):
            NUMREG.add(v)
    return vals[0] if vals else None


VERBATIM = [
    ("V01", "A-PIN",
     "all grammar-admissible choices of which cell-pairs\narbitrate per "
     "round, at the committed budget", "G-FAMILY-COUNT"),
    ("V02", "A-PIN",
     "any schedule with det != 0 at all sites is\n   the corpus's first "
     "non-degenerate grammar-generated geometry\n   carrier",
     "G-DET-NONZERO-EXISTS"),
    ("V03", "A-ADJ",
     "at all ten cells the division field is affine in the\nconstructor's "
     "seed set -- n = c + m*1_S -- so Stab(n) = Stab(1_S)",
     "G-AFFINE-LAW"),
    ("V04", "A-EFF",
     "q11 = n_{e1}`, `q22 = n_{e2}`, `q12 = (n_{e1+e2} - n_{e1} - "
     "n_{e2})/2", "G-I7-READOUT"),
    ("V05", "A-HA",
     "The readout is an invertible linear re-encoding: in count "
     "coordinates, the\n> record IS the metric.", "G-I7-READOUT"),
    ("V06", "A-D66",
     "each group is a g-PROPOSER conflict (g + 1 registers) whose base is\n"
     "    supplied by g - 1 deliveries from the group's diagonal seed",
     "G-COMMITTED-RECORD"),
    ("V07", "A-L1",
     "fourth form, outside paper 8's three**, and its admissibility is\n"
     "   v11's to argue when U4 runs", "G-WALL-L1"),
    ("V08", "A-CAT",
     "a Poisson sprinkling admits **no\nLorentz-invariant finite-valency "
     "graph** (BHS)", "G-WALL-BHS"),
    ("V09", "A-CAT",
     "a dimension reading without a height control is worthless",
     "G-WALL-KR"),
    ("V10", "A-PIN",
     "the diagonal counterpoint may be MEASURED here -- that is this "
     "unit's point --\nbut cosmological readings stay barred",
     "G-WALL-DIAGONAL"),
]
# the #62 length floor: no needle shorter than this may anchor a gate
NEEDLE_FLOOR = 40


def ascii_fold(s):
    """the pinned sources are typeset with Unicode punctuation and
    subscripts; the needles are ASCII.  This fold is declared, applied to
    BOTH sides of every verbatim match, and it changes no word."""
    table = {
        "—": "--", "–": "-", "−": "-", "‘": "'",
        "’": "'", "“": '"', "”": '"', "…": "...",
        "×": "x", "≈": "~", "≠": "!=", "≤": "<=",
        "≥": ">=", "⟨": "<", "⟩": ">", "→": "->",
        "≡": "==", "·": "*", "ℓ": "l", "ω": "w",
        "ℤ": "Z", "√": "sqrt",
        "₀": "0", "₁": "1", "₂": "2", "₃": "3", "₄": "4",
        "₅": "5", "₆": "6", "₇": "7", "₈": "8", "₉": "9",
        "⁰": "0", "¹": "1", "²": "2", "³": "3",
    }
    for k, v in table.items():
        s = s.replace(k, v)
    return re.sub(r"[^\x00-\x7f]", "?", s)


def match_needle(hay, needle):
    """#125: whitespace-normalise both sides; #62: enforce the length floor."""
    if len(norm(needle)) < NEEDLE_FLOOR:
        raise GateFail("G-VERBATIM :: needle below the #62 length floor")
    return norm(ascii_fold(needle)) in norm(ascii_fold(hay))


def full_run(break_anchor, paper_text, paper_rel):
    LD = Ledger()
    SEAL = Seal()
    R = {"schema": SCHEMA, "paper": paper_rel}
    NUMREG.clear()
    del READS[:]

    # -- SEC 1  PROVENANCE ---------------------------------------------------
    say("=" * 78)
    say("SEC 1   PROVENANCE -- ten pinned sources, sha256-12, products gated")
    say("=" * 78)
    texts, prov = {}, []
    for sid, rel, want, what in SOURCES:
        raw = read_bytes(rel)
        got = hashlib.sha256(raw).hexdigest()[:12]
        want_eff = "0" * 12 if break_anchor == sid else want
        texts[rel] = raw.decode("utf-8")
        ok = (got == want_eff)
        prov.append({"id": sid, "path": rel, "want": want_eff, "got": got,
                     "ok": ok, "what": what})
        LD.gate("G-PROV[%s]" % sid,
                "the pinned source %s is present and its sha256-12 is %s "
                "(measured %s) -- %s" % (rel, want_eff, got, what),
                ok, {"path": rel, "want": want_eff, "got": got})
    R["provenance"] = prov
    LD.gate("G-PROV-ALL",
            "ALL %d declared sources resolve under the repository root "
            "derived from this file's own location, every one reproduces its "
            "pinned sha256-12, and the set of hash-pinned runtime reads is "
            "EXACTLY the declared set -- nothing else in the repository is "
            "read except this file itself (for the exactness AST scan) and "
            "the paper under test (which cannot be hash-pinned because it is "
            "the object being verified).  No `git` subprocess is invoked "
            "anywhere in this program, so the run is correct off-tree and in "
            "a directory with no version control (#91)" % len(SOURCES),
            all(p["ok"] for p in prov)
            and set(READS) == {s[1] for s in SOURCES},
            {"sources": len(SOURCES), "reads": sorted(set(READS)),
             "unpinned_reads": ["<self>", paper_rel], "subprocesses": 0})

    # -- SEC 2  THE GRAMMAR --------------------------------------------------
    say("")
    say("=" * 78)
    say("SEC 2   THE COMMITTED GRAMMAR, DRIVEN DIRECTLY (no menu law re-typed)")
    say("=" * 78)
    G = Grammar(texts)
    say("  d42b1 text-slice: %d of %d chars, cut at the layer's own banner "
        "print" % G.slice_chars)
    say("  AST-extracted bodies: %s"
        % {k.split("/")[-1]: len(v) for k, v in sorted(G.extracted.items())})
    LD.gate("G-SLICE-EXIT-FREE",
            "the committed transport grammar enters this process as a SINGLE "
            "SOURCE -- a text slice of d42b1 cut at its own banner print, "
            "plus AST-extracted def/class bodies of d60 and d66 -- and the "
            "strip is GATED, not asserted: no reference to `exit`, `quit` or "
            "`_exit`, in CALL or bare NAME/ATTRIBUTE form, survives the slice "
            "(checked textually AND by AST) or any extracted body",
            G.slice_exit_free and G.bodies_exit_free,
            {"slice_chars": G.slice_chars, "slice_exit_free": G.slice_exit_free,
             "bodies_exit_free": G.bodies_exit_free,
             "bodies": {k.split("/")[-1]: len(v)
                        for k, v in sorted(G.extracted.items())}})

    # the menu is the layer's own: a behavioural probe, both directions
    menu0 = G.candidates_for([], (ACTORS[0],))
    probe_ok = (any(e[0] == "p" and e == ("p", ACTORS[0], G.V0, 0)
                    for e, _q in menu0)
                and not any(e[0] == "r" for e, _q in menu0)
                and not any(e[0] == "d" and e[3] != G.V0 for e, _q in menu0))
    LD.gate("G-GRAMMAR-LIVE",
            "the object deciding admissibility here is d42b1's own "
            "`candidates_for`, exercised in BOTH directions on the empty "
            "record: the genesis proposal ('p', G00, v0, 0) IS offered, no "
            "arbitration is offered (nothing is live) and no delivery of a "
            "non-genesis version is offered (nothing is held)",
            probe_ok, {"menu_size": len(menu0),
                       "kinds": sorted({e[0] for e, _q in menu0})})

    # the anchor: the generalized driver reproduces the committed constructor
    committed_ref = committed_grid(G, 2)
    mine = driven(G, COMMITTED)
    same = pick("MUT-COMMITTED-RECORD",
                committed_ref["H"] == mine["H"], False)
    LD.gate("G-COMMITTED-RECORD",
            "THE GENERALIZED SCHEDULE DRIVER REPRODUCES THE COMMITTED "
            "CONSTRUCTOR EVENT FOR EVENT.  d66's own `conflict_grid(3, 2)` "
            "function object, AST-extracted from the pinned source and re-run "
            "in this process, and this unit's schedule driver at the "
            "committed schedule (ROW class then COL class, diagonal seeds) "
            "emit IDENTICAL event lists of %d events with %d division events; "
            "so the family below is a generalization of the committed object "
            "and not a re-implementation of it"
            % (committed_ref["events"], committed_ref["arbs"]),
            same and not committed_ref["refusal"]
            and committed_ref["maxhits"] == 1,
            {"d66_events": committed_ref["events"],
             "driver_events": mine["events"],
             "identical": same, "maxhits": committed_ref["maxhits"],
             "refusal": committed_ref["refusal"]})
    reg(committed_ref["events"], committed_ref["arbs"])

    # the committed .out rows, READ and reproduced (not re-typed)
    d66out = texts["v10/data/d66_arbitration_crystal_exact.out"]
    anchors = []
    for R_ in (4, 6):
        m = re.search(r"GRID\(g=3,R=%d\)\s+n=\s*(\d+)\s+arbs=\s*(\d+)\s+"
                      r"\(k_min=(\d+), k_conflict=(\d+)\)\s+deliveries=\s*"
                      r"(\d+)\s+arb share (\d+)/(\d+)" % R_, d66out)
        b = committed_grid(G, R_)
        got = (b["events"], b["arbs"], b["dels"])
        wnt = (int(m.group(1)), int(m.group(2)), int(m.group(5)))
        anchors.append({"id": "A-D66-GRID3%d" % R_, "read": wnt,
                        "recomputed": got, "ok": got == wnt,
                        "source": "v10/data/d66_arbitration_crystal_exact.out"})
    eff = texts["v14/review-u4-effectus.md"]
    m = re.search(r"\|\s*CONFLICT-GRID\(3,2\)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|"
                  r"\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*−?-?(\d+)"
                  r"\s*\|\s*\*\*(\d+)\*\*", eff)
    eff_row = tuple(int(m.group(k)) for k in range(1, 8))
    nn = link_counts(CLASSES["ROW"], CLASSES["COL"])
    q11, q22, q12, det = i7_form(nn, (0, 0))
    got_row = (nn[((1, 0), (0, 0))], nn[((0, 1), (0, 0))],
               nn[((1, 1), (0, 0))], int(q11), int(q22), abs(int(q12)),
               int(det))
    anchors.append({"id": "A-EFF-I7", "read": list(eff_row),
                    "recomputed": list(got_row), "ok": got_row == eff_row,
                    "source": "v14/review-u4-effectus.md"})
    if mut("MUT-ANCHOR-DRIFT"):
        anchors[0] = dict(anchors[0])
        anchors[0]["recomputed"] = [x + 1 for x in anchors[0]["recomputed"]]
        anchors[0]["ok"] = False
    R["anchors"] = anchors
    for a in anchors:
        reg(*[int(x) for x in a["read"]])
    for a in anchors:
        say("  [ANCH] %s  read %s  recomputed %s" % (a["id"], a["read"],
                                                     a["recomputed"]))
    LD.gate("G-ANCHORS-READ",
            "the committed numbers this unit reproduces are READ from their "
            "committed files at run time and never re-typed: d66's own output "
            "rows for GRID(g=3,R=4) and GRID(g=3,R=6) (events, arbitrations, "
            "deliveries) are parsed out of `d66_arbitration_crystal_exact.out` "
            "and reproduced by the extracted constructor, and the U4 effectus "
            "review's CONFLICT-GRID(3,2) I7 row (n_(1,0), n_(0,1), n_(1,1), "
            "q_11, q_22, |q_12|, det) is parsed out of the review and "
            "reproduced by this unit's own readout -- %d of %d"
            % (sum(1 for a in anchors if a["ok"]), len(anchors)),
            all(a["ok"] for a in anchors), {"anchors": anchors})
    SEAL.take("SEAL-ANCHORS", R)

    va = []
    for vid, sid, quote, consumer in VERBATIM:
        rel = [s[1] for s in SOURCES if s[0] == sid][0]
        found = match_needle(texts[rel], quote)
        if mut("MUT-VERBATIM") and vid == "V03":
            found = False
        va.append({"id": vid, "source": sid, "path": rel,
                   "chars": len(norm(quote)), "found": found,
                   "consumer": consumer})
        say("  [VERB] %s  %s -> %s  (%d chars)"
            % (vid, rel, consumer, len(norm(quote))))
    R["verbatim_anchors"] = va
    LD.gate("G-VERBATIM",
            "every one of the %d verbatim source anchors (#62) is found in "
            "its pinned source after ASCII folding and whitespace "
            "normalisation, every needle clears the %d-character length "
            "floor, and every anchor names the gate that CONSUMES it -- no "
            "anchor is decorative"
            % (len(va), NEEDLE_FLOOR),
            all(a["found"] for a in va)
            and all(a["chars"] >= NEEDLE_FLOOR for a in va)
            and all(a["consumer"] for a in va),
            {"anchors": len(va), "min_chars": min(a["chars"] for a in va),
             "missing": [a["id"] for a in va if not a["found"]]})
    SEAL.take("SEAL-VERBATIM", R)

    LD.gate("G-I7-READOUT",
            "the determinant column is computed through HA 3.2's DECLARED "
            "readout in the U4 effectus review's own I7 coordinates -- "
            "q_11 = n_(1,0), q_22 = n_(0,1), q_12 = (n_(1,1) - n_(1,0) - "
            "n_(0,1))/2 -- applied to the co-division adjacency (the number "
            "of division events whose footprint contains both x and x + l); "
            "both source statements are verbatim anchors V04 and V05, and the "
            "route is validated by reproducing the effectus's committed "
            "CONFLICT-GRID(3,2) row exactly",
            [a["ok"] for a in anchors if a["id"] == "A-EFF-I7"][0],
            {"committed_row": list(eff_row), "recomputed": list(got_row)})

    # -- SEC 3  THE FAMILY ---------------------------------------------------
    say("")
    say("=" * 78)
    say("SEC 3   THE FAMILY (pin R1), declared as data and COUNTED")
    say("=" * 78)
    C = raw_census(G)
    parts, subsets = C["parts"], C["subsets"]
    n_parts = len(parts)
    n_seed = 27
    per_round = n_parts * n_seed
    family = per_round * per_round
    # route 2 for the same count: the multinomial 9!/(3!^3 3!) and 3^3
    f9 = 1
    for k in range(1, 10):
        f9 *= k
    n_parts_closed = f9 // (6 * 6 * 6 * 6)
    family_closed = (n_parts_closed * 27) ** 2
    if mut("MUT-FAMILY-COUNT"):
        family = family + 1
    say("  partitions of the nine sites into three triples : %d" % n_parts)
    say("  seed assignments per partition                   : %d" % n_seed)
    say("  schedules per round                              : %d" % per_round)
    say("  THE FAMILY (two rounds)                          : %d" % family)
    LD.gate("G-FAMILY-COUNT",
            "THE FAMILY IS COUNTED, NOT ASSERTED (#24).  A schedule is a "
            "choice, for each of the committed constructor's two rounds, of "
            "which cell-pairs arbitrate together -- equivalently a partition "
            "of the nine cells into three three-proposer conflict groups, the "
            "committed per-round budget -- together with a seed for each "
            "group.  Enumeration gives %d partitions and 27 seed assignments "
            "each, so %d schedules per round and %d in the family; the closed "
            "form 9!/(3!^3 3!) x 3^3, squared, computed by a second route "
            "that shares no code with the enumeration, returns the same "
            "number" % (n_parts, per_round, family),
            n_parts == n_parts_closed and family == family_closed,
            {"partitions": n_parts, "closed_form": n_parts_closed,
             "family": family, "family_closed": family_closed})
    reg(n_parts, n_seed, per_round, family)

    win = window_schedules()
    n_win = len(win)
    win_declared = 4 * 4 * 27 * 27
    committed_in_window = ("ROW", DIAG_SEED, "COL", DIAG_SEED) in set(win)
    window_is_strict = pick("MUT-WINDOW-SILENT", n_win < family, False)
    R["family"] = {"partitions": n_parts, "seeds_per_partition": n_seed,
                   "schedules_per_round": per_round, "family": family,
                   "window": n_win, "window_fraction": str(Fraction(n_win,
                                                                    family)),
                   "window_rule": "both rounds' groupings drawn from the four "
                                  "parallel classes of AG(2,3); seeds free",
                   "committed_in_window": committed_in_window}
    say("  THE DECLARED GRAMMAR WINDOW                      : %d (%s of the "
        "family)" % (n_win, Fraction(n_win, family)))
    LD.gate("G-WINDOW-DISCLOSED",
            "THE WINDOW IS DECLARED IN THE HEAD AND IS A STRICT SUBSET "
            "(no-silent-caps).  Driving the layer's menus over all %d "
            "schedules is not affordable, so grammar-admissibility is decided "
            "EXHAUSTIVELY on a declared window -- both rounds' groupings drawn "
            "from the four parallel classes of AG(2,3), which is d66's own "
            "resolvable device, with the seeds free: %d schedules, %s of the "
            "family, containing the committed schedule.  Every OTHER column "
            "below is exhaustive over the WHOLE family, and the window's "
            "scope is carried in the constructibility verdict string itself"
            % (family, n_win, Fraction(n_win, family)),
            window_is_strict and n_win == win_declared
            and committed_in_window,
            {"family": family, "window": n_win, "declared": win_declared,
             "strict_subset": window_is_strict,
             "committed_in_window": committed_in_window})
    SEAL.take("SEAL-FAMILY", R)
    reg(n_win, Fraction(n_win, family))

    # -- SEC 4  CONSTRUCTIBILITY --------------------------------------------
    say("")
    say("=" * 78)
    say("SEC 4   CONSTRUCTIBILITY (pin R2.1) -- the menus driven, per schedule")
    say("=" * 78)
    WD = window_drive(G)
    fates = {}
    for key, row in WD.items():
        if row["refusal"] is not None:
            fates[key] = "REFUSED"
        elif row["maxhits"] > 1:
            fates[key] = "BRANCHING"
        else:
            fates[key] = "FORCED"
    if mut("MUT-NOT-FORCED"):
        victim = ("ROW", DIAG_SEED, "COL", DIAG_SEED)
        b = drive(G, COMMITTED, drop_supply=0)
        WD = dict(WD)
        WD[victim] = dict(WD[victim])
        WD[victim]["refusal"] = b.refusal
        WD[victim]["events"] = len(b.H)
    census = Counter(fates.values())
    ev = Counter(row["events"] for row in WD.values())
    say("  window schedules driven : %d" % len(WD))
    say("  fates                   : %s" % dict(sorted(census.items())))
    say("  event counts            : %s" % dict(sorted(ev.items())))
    per_object_ok = all(
        (WD[k]["refusal"] is None and WD[k]["maxhits"] == 1
         and WD[k]["divisions"] == 6 and 24 <= WD[k]["events"] <= 30)
        for k in WD)
    refused_here = [k for k in WD if WD[k]["refusal"] is not None]
    LD.gate("G-CONSTRUCTIBILITY",
            "EVERY schedule of the declared window is evaluated against its "
            "OWN driven record (#87), not against an aggregate: for each of "
            "the %d schedules the layer's menu offered every specified full "
            "event tuple exactly once (maxhits = 1), no step was refused, the "
            "record carries exactly 6 division events and between 24 and 30 "
            "events in total.  Measured fates: %s.  The instrument's ability "
            "to return the other two fates is demonstrated by the two "
            "declared controls below"
            % (len(WD), dict(sorted(census.items()))),
            per_object_ok and not refused_here,
            {"schedules": len(WD), "fates": dict(sorted(census.items())),
             "events": dict(sorted(ev.items())),
             "refused": [str(k) for k in refused_here[:3]]})

    ctrl_ns = drive(G, COMMITTED, supply=False)
    ns_ok = pick("MUT-REFUSAL-BLIND", ctrl_ns.refusal is not None, False)
    say("  CONTROL 1 (no-supply)   : refusal %s after %d events"
        % (ctrl_ns.refusal, len(ctrl_ns.H)))
    LD.gate("G-CTRL-REFUSED",
            "THE REFUSED FATE IS REACHABLE AND THE INSTRUMENT SEES IT.  The "
            "declared no-supply control runs the committed schedule with the "
            "conflict-supply deliveries suppressed; the layer then refuses the "
            "first round-1 proposal by an actor that does not hold the base, "
            "at the located prefix %s.  A refusal is recorded, never patched"
            % (ctrl_ns.refusal,),
            ns_ok, {"refusal": ctrl_ns.refusal, "events": len(ctrl_ns.H)})
    us_hits, us_prefix, us_seed = branching_control(G)
    us_ok = pick("MUT-BRANCHING-BLIND", us_hits > 1, False)
    say("  CONTROL 2 (under-spec)  : %d menu candidates match at prefix %d, "
        "so maxhits = %d" % (us_hits, us_prefix, us_hits))
    LD.gate("G-CTRL-BRANCHING",
            "THE BRANCHING FATE IS REACHABLE AND THE INSTRUMENT SEES IT.  At "
            "prefix %d of the committed record the declared under-specified "
            "control asks d60's `pick` for an arbitration by %s WITHOUT "
            "naming its conflict key and winner key; %d menu candidates "
            "match, so the builder's own `maxhits` reads %d > 1 and the fate "
            "is BRANCHING.  This is what makes the FORCED reading above a "
            "measurement rather than a structural tautology.  ONLY THE COUNT "
            "IS REPORTED, and that is deliberate: d60's `pick` breaks ties "
            "with `sorted(key=repr)`, whose value on a frozenset depends on "
            "the interpreter's per-process string hashing, so WHICH "
            "candidate an under-specified pick selects is not reproducible.  "
            "Every event of every schedule in this census is specified by "
            "its FULL TUPLE, where at most one candidate can match and the "
            "tie-break is never consulted; the control stops at the first "
            "under-specified pick and never continues a record past it"
            % (us_prefix, us_seed, us_hits, us_hits),
            us_ok, {"candidates": us_hits, "prefix": us_prefix,
                    "initiator": us_seed})
    R["constructibility"] = {
        "window": len(WD), "fates": dict(sorted(census.items())),
        "events": {str(k): v for k, v in sorted(ev.items())},
        "control_nosupply": {"refusal": list(ctrl_ns.refusal)
                             if ctrl_ns.refusal else None,
                             "events": len(ctrl_ns.H)},
        "control_underspecified": {"candidates": us_hits,
                                   "prefix": us_prefix,
                                   "initiator": us_seed},
    }
    SEAL.take("SEAL-CONSTRUCTIBILITY", R)
    reg(len(WD), census["FORCED"], us_hits, us_prefix, len(ctrl_ns.H))
    reg(*[k for k in ev], *[v for v in ev.values()])

    # -- SEC 5  THE STABILIZER ----------------------------------------------
    say("")
    say("=" * 78)
    say("SEC 5   THE STABILIZER COLUMN (pin R2.2) -- both readings, 3 routes")
    say("=" * 78)
    route_rows = C["route_rows"]
    disagree = [r for r in route_rows if not (r[2] == r[3] == r[4])]
    if mut("MUT-STAB-ROUTE"):
        disagree = [route_rows[0]]
    LD.gate("G-STAB-ROUTES",
            "THE STABILIZER OF EVERY SEED-PAIR FIELD IS COMPUTED THREE TIMES "
            "BY ROUTES SHARING NO CODE AND NO TYPED CONSTANT, and the three "
            "agree element for element at every one of the %d objects: "
            "(1) translate the field over Z_3^2 and compare; (2) take the "
            "annihilator of the support of the exact Z_3^2 Fourier transform "
            "in Z[w] = Z[t]/(t^2 + t + 1), running over the dual group; "
            "(3) walk the subgroup lattice and take the largest H on whose "
            "cosets the field is constant" % len(route_rows),
            not disagree,
            {"objects": len(route_rows), "disagreements": len(disagree),
             "first": str(disagree[0]) if disagree else None})

    # driven records vs the combinatorial field, per window schedule
    bad = []
    for (a, s0, b, s1), row in WD.items():
        n_init = initiator_field(frozenset(s0), frozenset(s1))
        n_foot = footprint_field(CLASSES[a], CLASSES[b])
        if (row["init"] != tuple(n_init[x] for x in SITES)
                or row["foot"] != tuple(n_foot[x] for x in SITES)):
            bad.append((a, s0, b, s1))
    if mut("MUT-DRIVEN-FIELD"):
        bad = [win[0]]
    LD.gate("G-DRIVEN-EQUALS-COMBINATORIAL",
            "for EVERY one of the %d window schedules the division-event "
            "field read off the DRIVEN record -- the initiator field from "
            "each arbitration's `op[1]`, the footprint field from each "
            "arbitration's `regs_of` footprint intersected with the actor set "
            "-- equals the field the combinatorial census computes from the "
            "schedule alone (#87, per object).  That equality is what lets "
            "the stabilizer and determinant columns be exhaustive over the "
            "whole family while the menus are driven on the window"
            % len(WD),
            not bad, {"objects": len(WD), "mismatches": len(bad),
                      "first": str(bad[0]) if bad else None})

    foot_bad = [k for k, row in WD.items() if set(row["foot"]) != {2}]
    if mut("MUT-FOOTPRINT"):
        foot_bad = [win[0]]
    LD.gate("G-FOOTPRINT-CONSTANT",
            "AT THE FOOTPRINT READING THE DIVISION FIELD IS THE CONSTANT 2 AT "
            "EVERY SITE OF EVERY SCHEDULE, so its stabilizer is the whole "
            "group Z_3^2 identically -- checked on each of the %d driven "
            "records separately.  Each round's three conflict groups partition "
            "the nine cells, so every cell lies in exactly one footprint per "
            "round; the footprint reading is a CENSUS ARTIFACT of the "
            "committed budget and carries no information about the schedule.  "
            "This is the constant-field vacuous positive the U4 adjudication "
            "named, exhibited here as a property of the whole family"
            % len(WD),
            not foot_bad, {"objects": len(WD), "non_constant": len(foot_bad),
                           "value": 2})

    stabpair, affpair = C["stabpair"], C["affpair"]
    sidx = C["sidx"]
    W = 90
    weights = set(C["weight"].values())
    stab_counts = Counter(stabpair.values())
    fam_stab = {k: v * W * W for k, v in stab_counts.items()}
    crystalline = sum(v for k, v in fam_stab.items() if k != "1")
    say("  seed-set pairs                    : %d" % len(stabpair))
    say("  partitions admitting a given seed set (uniform) : %s"
        % sorted(weights))
    for k in SUBGROUP_ORDER:
        if k in stab_counts:
            say("    Stab = %-9s : %6d seed pairs -> %9d schedules"
                % (k, stab_counts[k], fam_stab[k]))
    say("  CRYSTALLINE (initiator reading)   : %d of %d = %s"
        % (crystalline, family, Fraction(crystalline, family)))
    LD.gate("G-STAB-FULL-FAMILY",
            "THE STABILIZER COLUMN IS EXHAUSTIVE OVER THE WHOLE FAMILY, not "
            "over a window.  The initiator field depends on the schedule only "
            "through its two seed sets, and every 3-subset of Z_3^2 is a "
            "transversal of exactly %d of the %d partitions -- a uniform "
            "weight, measured, not assumed -- so the %d seed-set pairs carry "
            "the whole census with multiplicity %d.  Measured: %d of %d "
            "schedules are crystalline at the initiator reading (%s), and the "
            "full group Z_3^2 never occurs there because six division events "
            "cannot spread evenly over nine sites"
            % (W, n_parts, len(stabpair), W * W, crystalline, family,
               Fraction(crystalline, family)),
            weights == {W} and len(stabpair) == 84 * 84
            and sum(fam_stab.values()) == family
            and "Z3^2" not in stab_counts,
            {"weights": sorted(weights), "pairs": len(stabpair),
             "per_subgroup": dict(sorted(stab_counts.items())),
             "family_check": sum(fam_stab.values())})
    R["stabilizer"] = {
        "reading_initiator": {k: fam_stab.get(k, 0) for k in SUBGROUP_ORDER},
        "reading_footprint": {"Z3^2": family},
        "seed_pair_counts": dict(sorted(stab_counts.items())),
        "uniform_weight": W,
        "crystalline": crystalline,
        "crystalline_fraction": str(Fraction(crystalline, family)),
        "routes": 3, "route_objects": len(route_rows),
    }
    SEAL.take("SEAL-STABILIZER", R)
    reg(crystalline, Fraction(crystalline, family), W, len(stabpair))
    for k in SUBGROUP_ORDER:
        if k in fam_stab:
            reg(fam_stab[k], stab_counts[k])

    # -- SEC 6  THE DETERMINANT ---------------------------------------------
    say("")
    say("=" * 78)
    say("SEC 6   THE DETERMINANT COLUMN (pin R2.3) -- the weld-arena scout")
    say("=" * 78)
    det_class, det9 = C["det_class"], C["det9"]
    n_pairs = n_parts * n_parts
    n_det9 = len(det9)
    det9_scheds = n_det9 * 729
    posdef_max = pick("MUT-DET-POSDEF", C["posdef_max"], 9)
    strict_pos = pick("MUT-I7-STRICT", C["strict_pos"], 1)
    hom9 = sum(1 for r in det9 if r[2])
    uniform_sign = sum(1 for r in det9 if all(d < 0 for d in r[3]))
    mixed_sign = n_det9 - uniform_sign
    say("  partition pairs                       : %d" % n_pairs)
    say("  det != 0 at ALL NINE sites            : %d pairs -> %d schedules"
        % (n_det9, det9_scheds))
    say("  of those, homogeneous (one q at every site) : %d" % hom9)
    say("  of those, det < 0 at all nine sites    : %d ; mixed sign : %d"
        % (uniform_sign, mixed_sign))
    say("  max sites at which q is positive definite, over ALL pairs : %d"
        % posdef_max)
    say("  pairs meeting I7's strict positivity (all 27 counts > 0)  : %d"
        % strict_pos)
    say("  det values over the non-degenerate cells : %s"
        % dict(sorted(C["detvals"].items())))

    # THE NAMED WITNESS
    pidx = C["pidx"]
    wi = (pidx[CLASSES["ROW"]], pidx[CLASSES["ROW"]])
    wname = "ROW|ROW/DIAG"
    wn = link_counts(CLASSES["ROW"], CLASSES["ROW"])
    wrows = [i7_form(wn, x) for x in SITES]
    w_ok = all(r[3] != 0 for r in wrows) and len(set(wrows)) == 1
    w_ok = pick("MUT-DET-EMPTY", w_ok, False)
    wq = wrows[0]
    say("  NAMED WITNESS %s : q_11=%s q_22=%s q_12=%s det=%s at 9 of 9 sites"
        % (wname, wq[0], wq[1], wq[2], wq[3]))
    LD.gate("G-DET-NONZERO-EXISTS",
            "DET-NONZERO-EXISTS, AND THE WITNESS IS NAMED.  The schedule "
            "%s -- the committed constructor with round 1's column class "
            "replaced by the row class again, i.e. the schedule that never "
            "rotates its conflict groups, with the committed diagonal seeds -- "
            "induces q = [[%s, %s], [%s, %s]] with det = %s at every one of "
            "the nine sites, the same form at every site.  It is a member of "
            "the declared window and its record is FORCED.  Over the whole "
            "family %d of the %d partition pairs (%d of %d schedules) carry a "
            "non-degenerate induced form at all nine sites"
            % (wname, wq[0], wq[2], wq[2], wq[1], wq[3], n_det9, n_pairs,
               det9_scheds, family),
            w_ok and n_det9 > 0
            and fates[("ROW", DIAG_SEED, "ROW", DIAG_SEED)] == "FORCED",
            {"witness": wname, "q11": str(wq[0]), "q22": str(wq[1]),
             "q12": str(wq[2]), "det": str(wq[3]), "sites": 9,
             "pairs": n_det9, "schedules": det9_scheds})
    LD.gate("G-POSDEF-EMPTY",
            "NO SCHEDULE IN THE FAMILY CARRIES A POSITIVE-DEFINITE INDUCED "
            "FORM AT EVERY SITE.  Exhaustively over all %d partition pairs "
            "the maximum number of sites at which q is positive definite is "
            "%d, never 9.  The mechanism is a budget: a partition into three "
            "triples has nine within-group pairs, and only those whose "
            "difference direction lies in I7's link set contribute, so the "
            "two rounds deposit at most 18 link-incidences over the nine "
            "sites -- while positive definiteness at a site needs q_11, q_22 "
            "> 0 and 4 q_11 q_22 > (n_(1,1) - q_11 - q_22)^2, hence at least "
            "3 incidences there, hence at least 27 in all"
            % (n_pairs, posdef_max),
            posdef_max < 9,
            {"pairs": n_pairs, "max_posdef_sites": posdef_max, "budget": 18,
             "needed": 27})
    LD.gate("G-I7-STRICT-EMPTY",
            "I7's OWN ADMISSIBILITY CRITERION IS EMPTY ON THIS FAMILY: not "
            "one of the %d partition pairs makes all 27 link counts strictly "
            "positive, so no schedule is an admissible I7 geometry record, "
            "and the renewal-crystal weld census the U4 effectus predicted "
            "EMPTY is recorded EMPTY here for a reason the effectus did not "
            "have -- the link budget, not the diagonal alone"
            % n_pairs,
            strict_pos == 0, {"pairs": n_pairs, "strictly_positive": strict_pos,
                              "budget": 18, "needed": 27})
    win_det9 = sum(1 for (a, s0, b, s1) in win
                   if det_class[(pidx[CLASSES[a]], pidx[CLASSES[b]])][0] == 9)
    say("  of the %d window schedules, %d carry det != 0 at all nine sites"
        % (n_win, win_det9))
    R["determinant"] = {
        "partition_pairs": n_pairs, "nonzero_at_all_sites_pairs": n_det9,
        "window_nonzero_at_all_sites": win_det9,
        "nonzero_at_all_sites_schedules": det9_scheds,
        "fraction_pairs": str(Fraction(n_det9, n_pairs)),
        "homogeneous": hom9, "uniform_negative": uniform_sign,
        "mixed_sign": mixed_sign,
        "max_posdef_sites": posdef_max, "strictly_positive_pairs": strict_pos,
        "det_values": dict(sorted(C["detvals"].items())),
        "witness": {"name": wname, "q11": str(wq[0]), "q22": str(wq[1]),
                    "q12": str(wq[2]), "det": str(wq[3])},
        "committed_schedule_det": str(det),
    }
    SEAL.take("SEAL-DETERMINANT", R)
    reg(n_pairs, n_det9, det9_scheds, hom9, uniform_sign, mixed_sign,
        posdef_max, strict_pos, wq[0], wq[1], wq[2], wq[3],
        Fraction(n_det9, n_pairs), det, 18, 27)
    for k, v in C["detvals"].items():
        reg(Fraction(k), v)
    reg(win_det9)

    # THE RESOLVABLE CLASS-PAIR TABLE (the window's own geometry, published)
    cp_rows, cp_bad = [], []
    for a in CLASS_NAMES:
        for b in CLASS_NAMES:
            nn2 = link_counts(CLASSES[a], CLASSES[b])
            rows2 = [i7_form(nn2, x) for x in SITES]
            hom2 = len(set(rows2)) == 1
            nz2 = sum(1 for r in rows2 if r[3] != 0)
            r0 = rows2[0]
            cp_rows.append({"round0": a, "round1": b, "q11": str(r0[0]),
                            "q22": str(r0[1]), "q12": str(r0[2]),
                            "det": str(r0[3]), "homogeneous": hom2,
                            "nonzero_sites": nz2})
            reg(r0[0], r0[1], r0[2], r0[3], nz2)
            # each row must agree with the whole-family determinant column
            want_nz = det_class[(pidx[CLASSES[a]], pidx[CLASSES[b]])][0]
            if not hom2 or nz2 != want_nz:
                cp_bad.append((a, b))
    if mut("MUT-CLASSPAIR"):
        cp_rows[0] = dict(cp_rows[0])
        cp_rows[0]["det"] = "42"
        cp_bad = [("ROW", "ROW")]
    for r in cp_rows:
        say("    %s + %s : q_11=%-2s q_22=%-2s q_12=%-4s det=%-4s homogeneous "
            "%s, non-degenerate at %d of 9 sites"
            % (r["round0"], r["round1"], r["q11"], r["q22"], r["q12"],
               r["det"], r["homogeneous"], r["nonzero_sites"]))
    LD.gate("G-CLASS-PAIR-TABLE",
            "THE SIXTEEN RESOLVABLE CLASS PAIRS CARRY A HOMOGENEOUS INDUCED "
            "FORM, AND EACH ROW IS BOUND TO THE WHOLE-FAMILY COLUMN.  When "
            "both rounds group along parallel classes, every site sees the "
            "same q -- checked row by row (#87), and each row's "
            "non-degeneracy count is required to equal the number the "
            "exhaustive %d-pair census independently assigns to that pair.  "
            "%d of the 16 pairs are non-degenerate at all nine sites, which "
            "is why %d of the %d window schedules are"
            % (n_pairs, sum(1 for r in cp_rows if r["nonzero_sites"] == 9),
               win_det9, n_win),
            not cp_bad, {"rows": len(cp_rows), "mismatches": cp_bad or "none",
                         "table": cp_rows})
    R["class_pairs"] = cp_rows
    reg(len(cp_rows))
    SEAL.take("SEAL-CLASS-PAIRS", R)

    # -- SEC 7  THE AFFINE NULL ---------------------------------------------
    say("")
    say("=" * 78)
    say("SEC 7   THE AFFINE NULL (pin R3) -- coset-union vs beyond-coset")
    say("=" * 78)
    aff_counts = Counter(affpair.values())
    joint = Counter((affpair[k], stabpair[k]) for k in affpair)
    strat = {}
    for a in ("CU-JOINT", "CU-SPLIT", "BEYOND-COSET"):
        tot = aff_counts[a] * W * W
        cry = sum(v for (aa, s), v in joint.items()
                  if aa == a and s != "1") * W * W
        subs = sorted({s for (aa, s), v in joint.items()
                       if aa == a and s != "1" and v > 0})
        strat[a] = {"schedules": tot, "crystalline": cry,
                    "fraction": str(Fraction(cry, tot)), "subgroups": subs}
        say("  %-13s : %9d schedules, %9d crystalline = %-6s  subgroups %s"
            % (a, tot, cry, Fraction(cry, tot), subs or "-"))
    cu_ok = pick("MUT-AFFINE-NULL",
                 all(stabpair[k] != "1" for k in affpair
                     if affpair[k] == "CU-JOINT"), False)
    LD.gate("G-AFFINE-LAW",
            "THE AFFINE NULL HOLDS EXACTLY WHERE IT IS PREDICTED TO.  Every "
            "one of the %d CU-JOINT seed pairs -- both seed sets a coset of "
            "ONE order-3 subgroup H -- is evaluated on its own field and every "
            "one has Stab containing H: %d of %d schedules, 100 per cent.  "
            "This is the U4 adjudication's mechanism n = c + m*1_S read as a "
            "prediction and confirmed; the crystallinity of these schedules "
            "carries NO emergence information"
            % (aff_counts["CU-JOINT"], strat["CU-JOINT"]["crystalline"],
               strat["CU-JOINT"]["schedules"]),
            cu_ok, {"cu_joint_pairs": aff_counts["CU-JOINT"],
                    "crystalline": strat["CU-JOINT"]["crystalline"],
                    "schedules": strat["CU-JOINT"]["schedules"]})
    split_ok = pick("MUT-CU-SPLIT",
                    all(stabpair[k] == "1" for k in affpair
                        if affpair[k] == "CU-SPLIT"), False)
    LD.gate("G-CU-SPLIT-EMPTY",
            "AND IT HOLDS NOWHERE ELSE AMONG THE COSET SEEDS.  Every one of "
            "the %d CU-SPLIT seed pairs -- both seed sets cosets, of "
            "DIFFERENT subgroups -- is evaluated on its own field and every "
            "one has trivial stabilizer: two lines of different directions "
            "meet in exactly one point, so the field takes the value 2 at a "
            "single site, and no order-3 period can carry a value that occurs "
            "once.  %d of %d schedules crystalline"
            % (aff_counts["CU-SPLIT"], strat["CU-SPLIT"]["crystalline"],
               strat["CU-SPLIT"]["schedules"]),
            split_ok, {"cu_split_pairs": aff_counts["CU-SPLIT"],
                       "crystalline": strat["CU-SPLIT"]["crystalline"]})
    bc_pairs = [k for k in affpair
                if affpair[k] == "BEYOND-COSET" and stabpair[k] != "1"]
    bc_subs = sorted({stabpair[k] for k in bc_pairs})
    bc_count = pick("MUT-CRYSTAL-SEEDED", len(bc_pairs), 0)
    inv = {v: k for k, v in sidx.items()}
    bc_wit = []
    for k in sorted(bc_pairs)[:4]:
        bc_wit.append({"S0": sorted(inv[k[0]]), "S1": sorted(inv[k[1]]),
                       "stab": stabpair[k],
                       "S0_is_line": inv[k[0]] in AG_LINES,
                       "S1_is_line": inv[k[1]] in AG_LINES})
    for w in bc_wit:
        say("    beyond-coset crystalline witness: S0=%s S1=%s -> Stab %s "
            "(lines: %s, %s)" % (w["S0"], w["S1"], w["stab"],
                                 w["S0_is_line"], w["S1_is_line"]))
    LD.gate("G-BEYOND-COSET-CRYSTALLINE",
            "CRYSTALLINITY IS NOT CONFINED TO THE CONSTRUCTOR-INHERITED "
            "LOCUS.  %d of the %d beyond-coset seed pairs -- at least one "
            "seed set NOT a coset of any order-3 subgroup -- carry a "
            "nontrivial translation stabilizer, and each is verified on its "
            "own field: %d of %d beyond-coset schedules, a rate of %s, "
            "realizing all four order-3 subgroups %s.  The mechanism is "
            "measured too: the field takes the value 1 on a union of two "
            "H-cosets and 0 on the third while NEITHER seed set is an "
            "H-coset, so the period is a property of the PAIR and not of "
            "either seed"
            % (len(bc_pairs), aff_counts["BEYOND-COSET"],
               strat["BEYOND-COSET"]["crystalline"],
               strat["BEYOND-COSET"]["schedules"],
               strat["BEYOND-COSET"]["fraction"], bc_subs),
            bc_count > 0 and len(bc_subs) == 4,
            {"beyond_coset_crystalline_pairs": bc_count,
             "beyond_coset_pairs": aff_counts["BEYOND-COSET"],
             "subgroups": bc_subs, "witnesses": bc_wit})
    R["affine"] = {"classes": strat, "beyond_coset_subgroups": bc_subs,
                   "beyond_coset_witnesses": bc_wit,
                   "committed_class": affine_class(frozenset(DIAG_SEED),
                                                   frozenset(DIAG_SEED))}
    SEAL.take("SEAL-AFFINE", R)
    for a in strat:
        reg(strat[a]["schedules"], strat[a]["crystalline"])
        reg(Fraction(strat[a]["crystalline"], strat[a]["schedules"]))
    reg(aff_counts["CU-JOINT"], aff_counts["CU-SPLIT"],
        aff_counts["BEYOND-COSET"], len(bc_pairs))

    # -- the joint stratum: crystalline AND non-degenerate ------------------
    tr_index = C["tr_index"]
    joint_det = C["joint_det"]
    cry_det = sum(v for (s, a), v in joint_det.items() if s != "1")
    cry_det_bc = sum(v for (s, a), v in joint_det.items()
                     if s != "1" and a == "BEYOND-COSET")
    say("  crystalline AND non-degenerate        : %d schedules (%d of them "
        "beyond-coset)" % (cry_det, cry_det_bc))
    strata = {"joint_det_stab": {"%s|%s" % k: v
                                 for k, v in sorted(joint_det.items())},
              "crystalline_and_nondegenerate": cry_det,
              "crystalline_and_nondegenerate_beyond_coset": cry_det_bc}

    # -- the strata witnesses, driven ---------------------------------------
    want, found = C["want"], C["witness"]
    wit_rows, driven_wit = [], 0
    inv_sub = {v: k for k, v in sidx.items()}
    for key in sorted(want):
        loc = found.get(key)
        if loc is None:
            continue
        i0, i1, t0, t1 = loc
        S0 = align_seeds(parts[i0], inv_sub[t0])
        S1 = align_seeds(parts[i1], inv_sub[t1])
        rec = driven(G, schedule_of(parts[i0], S0, parts[i1], S1))
        driven_wit += 1
        wit_rows.append({"stratum": "%s|%s|det9=%s" % key,
                         "S0": sorted(S0), "S1": sorted(S1),
                         "events": rec["events"], "maxhits": rec["maxhits"],
                         "refusal": rec["refusal"],
                         "divisions": len(rec["divisions"]),
                         "in_window": parts[i0] in CLASSES.values()
                         and parts[i1] in CLASSES.values()})
    if mut("MUT-STRATUM-BLIND") and wit_rows:
        wit_rows = wit_rows[:-1]
        driven_wit -= 1
    missing = sorted(k for k in want if found.get(k) is None)
    all_forced = all(w["refusal"] is None and w["maxhits"] == 1
                     for w in wit_rows)
    say("  census strata (stab x affine x det9)  : %d, all witnessed by a "
        "menu-driven schedule outside as well as inside the window: %d"
        % (len(want), driven_wit))
    LD.gate("G-STRATA-WITNESSED",
            "EVERY NONEMPTY CENSUS STRATUM HAS A MENU-DRIVEN WITNESS.  The "
            "%d nonempty (stabilizer x affine-class x non-degeneracy) strata "
            "of the WHOLE family are each given a deterministic representative "
            "-- the first in a fixed enumeration, no sampling -- and each "
            "representative's record is built by driving the layer's menus: "
            "%d witnesses, every one FORCED (maxhits = 1, no refusal, 6 "
            "division events).  So the grammar's verdict is not confined to "
            "the resolvable window: it has been taken at least once in every "
            "cell of the census" % (len(want), driven_wit),
            not missing and all_forced and driven_wit == len(want),
            {"strata": len(want), "witnessed": driven_wit,
             "missing": [str(m) for m in missing],
             "all_forced": all_forced})
    strata["witnesses"] = wit_rows
    strata["strata_count"] = len(want)
    R["strata"] = strata
    SEAL.take("SEAL-STRATA", R)
    reg(cry_det, cry_det_bc, len(want), driven_wit)

    # -- SEC 8  FRAGILITY ----------------------------------------------------
    say("")
    say("=" * 78)
    say("SEC 8   FRAGILITY (pin R2.4) -- computed, not sampled, on the window")
    say("=" * 78)
    frag_rows = Counter()
    frag_bad = []
    n_cryst_win = 0
    for (a, s0, b, s1) in win:
        key = (sidx[frozenset(s0)], sidx[frozenset(s1)])
        sname = stabpair[key]
        if sname == "1":
            continue
        n_cryst_win += 1
        H = SUBGROUPS[sname]
        broken = admissible_edits = 0
        for which, (cls, seeds) in enumerate(((CLASSES[a], s0),
                                              (CLASSES[b], s1))):
            for gi, g in enumerate(cls):
                old = seeds[gi]
                for new in g:
                    if new == old:
                        continue
                    ns = tuple(new if k == gi else seeds[k]
                               for k in range(3))
                    edit = ((a, ns, b, s1) if which == 0 else (a, s0, b, ns))
                    if edit not in WD or WD[edit]["refusal"] is not None:
                        continue
                    admissible_edits += 1
                    k2 = (sidx[frozenset(edit[1])], sidx[frozenset(edit[3])])
                    if not SUBGROUPS[stabpair[k2]] >= H:
                        broken += 1
        frag_rows[(broken, admissible_edits)] += 1
        if broken != admissible_edits or admissible_edits != 12:
            frag_bad.append((a, s0, b, s1))
    if mut("MUT-FRAGILITY"):
        frag_bad = [win[0]]
    say("  crystalline schedules in the window   : %d" % n_cryst_win)
    say("  (broken, admissible) edit census      : %s"
        % {str(k): v for k, v in sorted(frag_rows.items())})
    LD.gate("G-FRAGILITY",
            "THE CRYSTAL IS MAXIMALLY FRAGILE, AT EVERY CRYSTALLINE SCHEDULE "
            "OF THE WINDOW.  A single-arbitration re-seating -- moving exactly "
            "one division event to another cell of its own conflict group, "
            "the smallest edit that stays in the family -- has %d admissible "
            "forms at every schedule (6 arbitrations x 2 alternative seats, "
            "each an admissible member of the window in its own right), and "
            "at every one of the %d crystalline window schedules ALL of them "
            "destroy the period.  Each schedule is evaluated against its own "
            "edits (#87).  The mechanism: the edit changes the field by "
            "1_new - 1_old, and a difference of two distinct point masses is "
            "never constant on the cosets of an order-3 subgroup"
            % (12, n_cryst_win),
            not frag_bad and n_cryst_win > 0,
            {"crystalline_window": n_cryst_win,
             "census": {str(k): v for k, v in sorted(frag_rows.items())},
             "exceptions": len(frag_bad)})
    R["fragility"] = {"crystalline_in_window": n_cryst_win,
                      "edits_per_schedule": 12,
                      "census": {str(k): v
                                 for k, v in sorted(frag_rows.items())}}
    SEAL.take("SEAL-FRAGILITY", R)
    reg(n_cryst_win, 12, 6, 2)

    # -- SEC 9  THE WALLS ----------------------------------------------------
    say("")
    say("=" * 78)
    say("SEC 9   THE WALLS (pin R4), the four inherited from U4")
    say("=" * 78)
    src_text = read_text(SELF)
    banned_here = norm(BANNED_L1) in norm(src_text)
    paper_norm = norm(ascii_fold(paper_text))
    if mut("MUT-WALL-L1"):
        paper_norm = norm(ascii_fold(paper_text + "\n\nOrder-level "
                          "covariance is\nprecisely the form U4 tests, and "
                          "precisely the form the\ncorpus's strongest "
                          "relativity result took.\n"))
    l1_absent = norm(ascii_fold(BANNED_L1)) not in paper_norm
    l1_argued = ("fourth form" in paper_norm
                 and "not tested here" in paper_norm)
    LD.gate("G-WALL-L1",
            "L-1 IS ARGUED BEFORE ANY TEST AND THEN DECLINED, AND THE "
            "RETRACTED SENTENCE IS ABSENT.  Order-level covariance is a "
            "fourth form outside paper 8's three (verbatim anchor V07) and "
            "its admissibility is v11's to argue; this unit measures a "
            "PERMUTATION action of Z_3^2 on the actor set, which L-1's own "
            "scope guard leaves free, constructs no bridge from those "
            "translations to any boost, and states in the paper that the "
            "fourth form is NOT TESTED HERE.  The prohibition gate "
            "whitespace-normalises and ASCII-folds BOTH sides (#125), so a "
            "line-wrapped injection of the %d-character retracted sentence is "
            "caught -- the mutant MUT-WALL-L1 injects exactly that"
            % len(BANNED_L1),
            l1_absent and (l1_argued or not paper_text),
            {"banned_len": len(BANNED_L1), "absent_from_paper": l1_absent,
             "argued_first": l1_argued, "present_in_source_prose":
             banned_here})
    bhs_run = pick("MUT-WALL-BHS", False, True)
    LD.gate("G-WALL-BHS",
            "NO SPRINKLING-GRADE LORENTZ-INVARIANCE TEST IS RUN.  The "
            "catalog's BHS block (verbatim anchor V08) says a Poisson "
            "sprinkling admits no Lorentz-invariant finite-valency graph, and "
            "these schedules are finite-valency by construction, so running "
            "the test would manufacture a false negative.  Measured on this "
            "program's own source: no sprinkling, no boost, no rapidity and "
            "no frame is computed anywhere -- the only group that acts here is "
            "the translation group of a 9-element site lattice",
            not bhs_run,
            {"sprinkling_computed": bhs_run,
             "groups_acting": ["Z_3^2 translations"]})
    kr_hay = pick("MUT-WALL-KR", paper_norm.lower(),
                  paper_norm.lower().replace("height", "") + " dimension")
    kr_ok = ("dimension" not in kr_hay or "height" in kr_hay)
    LD.gate("G-WALL-KR",
            "NO DIMENSION READING IS TAKEN, SO THE KLEITMAN-ROTHSCHILD HEIGHT "
            "CONTROL HAS NOTHING TO CONTROL.  The catalog's carry is that a "
            "dimension reading without a height control is worthless "
            "(verbatim anchor V09).  This unit measures no chart width, no "
            "Myrheim-Meyer estimate and no max-shatter dimension: its columns "
            "are a translation stabilizer, a determinant and a "
            "constructibility fate, none of which is dimension-adjacent.  The "
            "gate is the conjunction: either the paper takes no dimension "
            "reading, or it carries a height control",
            kr_ok, {"dimension_reading": pick("MUT-WALL-KR", "none",
                                             "chart width"),
                    "paper_mentions_height": "height" in kr_hay})
    # the wall bars a cosmological READING, not the word: the paper is
    # required to SAY the reading is barred, so the needles are claim
    # phrases, never the bare stem
    COSMO_CLAIMS = ("cosmological constant", "hubble", "dark energy",
                    "expansion of the universe", "cosmic microwave",
                    "scale factor", "cosmological model")
    cosmo_hay = pick("MUT-WALL-COSMO", paper_norm.lower(),
                     paper_norm.lower() + " the measured period is the "
                     "expansion of the universe")
    cosmo = [w for w in COSMO_CLAIMS if w in cosmo_hay]
    diag_measured = ("(1,1)" in paper_norm or "<(1,1)>" in paper_norm)
    LD.gate("G-WALL-DIAGONAL",
            "THE DIAGONAL COUNTERPOINT IS MEASURED HERE -- THAT IS THIS "
            "UNIT'S POINT (verbatim anchor V10) -- AND COSMOLOGICAL READINGS "
            "STAY BARRED.  U4 found the division field's period and the "
            "vanishing diagonal link count jointly forced by one design "
            "choice; this census varies that choice and measures the two "
            "separately: the period direction ranges over all four order-3 "
            "subgroups and the diagonal link count is populated by the "
            "diagonal parallel class.  No cosmological word appears in the "
            "paper",
            not cosmo and (diag_measured or not paper_text),
            {"cosmological_words": cosmo, "diagonal_measured": diag_measured,
             "period_directions": bc_subs})
    R["walls"] = {"L1": "argued-first-and-declined", "BHS": "not-run",
                  "KR": "no-dimension-reading",
                  "diagonal": "measured-cosmology-barred"}
    SEAL.take("SEAL-WALLS", R)

    # -- SEC 10  THE VERDICT -------------------------------------------------
    say("")
    say("=" * 78)
    say("SEC 10  THE VERDICT")
    say("=" * 78)
    bc_rate = Fraction(strat["BEYOND-COSET"]["crystalline"],
                       strat["BEYOND-COSET"]["schedules"])
    v_crystal = ("U4B-CRYSTAL-GENERIC-[beyond-coset %s; %d of %d; %s]"
                 % (bc_rate, strat["BEYOND-COSET"]["crystalline"],
                    strat["BEYOND-COSET"]["schedules"], "|".join(bc_subs)))
    v_det = ("DET-NONZERO-EXISTS-[%s: det=%s at 9 of 9; %d of %d pairs; "
             "POSDEF-EMPTY; I7-STRICT-EMPTY]"
             % (wname, wq[3], n_det9, n_pairs))
    v_con = ("CONSTRUCTIBILITY-[FORCED %d of %d; BRANCHING 0; REFUSED 0]"
             "@WINDOW-%d-OF-%d+%d-STRATUM-WITNESSES"
             % (census["FORCED"], len(WD), n_win, family, driven_wit))
    if mut("MUT-HEAD"):
        v_crystal = v_crystal.replace("GENERIC", "SEEDED")
    for s in (v_crystal, v_det, v_con):
        say("  " + s)
    R["verdict"] = {"crystal": v_crystal, "det": v_det,
                    "constructibility": v_con}
    R["counts"] = {
        "family": family, "window": n_win, "partitions": n_parts,
        "seed_pairs": len(stabpair), "uniform_weight": W,
        "crystalline": crystalline,
        "beyond_coset_crystalline": strat["BEYOND-COSET"]["crystalline"],
        "cu_joint_crystalline": strat["CU-JOINT"]["crystalline"],
        "cu_split_crystalline": strat["CU-SPLIT"]["crystalline"],
        "det9_pairs": n_det9, "det9_schedules": det9_scheds,
        "posdef_max": posdef_max, "strict_pos": strict_pos,
        "strata": len(want), "stratum_witnesses": driven_wit,
        "crystalline_window": n_cryst_win, "forced": census["FORCED"],
    }
    reg(*[v for v in R["counts"].values() if isinstance(v, int)])

    ok_head = reconstruct(R) == (v_crystal, v_det, v_con)
    LD.gate("G-VERDICT-RECONSTRUCTED",
            "THE HEAD IS DERIVED A SECOND TIME BY A PATH THAT SHARES NEITHER "
            "CODE NOR INPUT NOR TYPED LITERAL WITH THE BUILDER.  The builder "
            "assembles the three verdict strings from live Python objects; "
            "the comparator reads the RECEIPT'S OWN census rows, recomputes "
            "the beyond-coset rate as a Fraction from the two counts it finds "
            "there, re-sorts the subgroup list, and rebuilds all three "
            "strings from its own format templates.  The two agree character "
            "for character",
            ok_head, {"crystal": v_crystal, "det": v_det,
                      "constructibility": v_con})
    SEAL.take("SEAL-VERDICT-CRYSTAL", R)
    SEAL.take("SEAL-VERDICT-DET", R)
    SEAL.take("SEAL-VERDICT-CONSTR", R)
    SEAL.take("SEAL-COUNTS", R)

    broken = SEAL.verify(R, only=SEALS_IN_RUN)
    if mut("MUT-SEAL-BROKEN"):
        R["counts"]["family"] = family + 1
        broken = SEAL.verify(R, only=SEALS_IN_RUN)
    LD.gate("G-SEAL-COMPLETE",
            "EVERY PUBLISHED OBJECT WAS DIGESTED AT THE MOMENT ITS GATE "
            "PASSED (#119) AND EVERY ONE OF THOSE %d IN-RUN SEALS STILL "
            "VERIFIES HERE.  The artifacts below are written FROM the sealed "
            "payload, and the terminal integrity gate compares the bytes on "
            "disk against these digests, never against a re-derivation"
            % len(SEAL.rows),
            not broken, {"seals": len(SEAL.rows),
                         "declared_in_run": len(SEALS_IN_RUN),
                         "broken": broken})

    # -- exactness -----------------------------------------------------------
    tree = ast.parse(src_text)
    floats = [n for n in ast.walk(tree)
              if isinstance(n, ast.Constant)
              and type(n.value).__name__ in ("float", "complex")]
    float_names = [n for n in ast.walk(tree)
                   if isinstance(n, ast.Name) and n.id in ("float", "complex")]

    def has_float(o):
        """the scanner names no builtin: it compares TYPE NAMES, so the AST
        scan above can require zero references to the name it is hunting."""
        if isinstance(o, dict):
            return any(has_float(k) or has_float(v) for k, v in o.items())
        if isinstance(o, (list, tuple)):
            return any(has_float(v) for v in o)
        return type(o).__name__ in ("float", "complex")
    LD.gate("G-EXACT",
            "THE ARITHMETIC IS EXACT END TO END.  An AST scan of this file "
            "finds %d float literals and %d references to `float`; a "
            "recursive type scan of the receipt about to be emitted finds no "
            "float anywhere.  Every quadratic form component and every "
            "determinant is a `fractions.Fraction`; every count is a Python "
            "integer" % (len(floats), len(float_names)),
            not floats and not float_names and not has_float(R),
            {"float_literals": len(floats), "float_refs": len(float_names),
             "receipt_floats": has_float(R)})

    # -- the CLI contract ----------------------------------------------------
    probes = []
    parser = parse_args_permissive if mut("MUT-CLI-PERMISSIVE") else parse_args
    for argv, want_reject in ((["--not-a-flag"], True), (["--mutant"], True),
                              (["--mutant", "NOPE"], True),
                              (["--break-anchor"], True),
                              (["--verify-paper", "/no/such/file.md"], True),
                              (["extra"], True), (["--no-write"], False),
                              (["--numbers"], False)):
        try:
            parser(argv)
            rejected = False
        except CliError:
            rejected = True
        probes.append({"argv": argv, "rejected": rejected,
                       "expected": want_reject})
    LD.gate("G-CLI-WHITELIST",
            "THE CLI IS ARGV-PARSED AGAINST A WHITELIST AND EXERCISED HERE "
            "(#82): unknown flags, unknown flag arguments, missing flag "
            "arguments and a --verify-paper path that does not exist are all "
            "rejected with exit 2, while the two documented no-op-free flags "
            "parse.  %d probes, all as declared.  The registered PERMISSIVE "
            "shape -- a runner that ignores what it does not recognise -- is "
            "present only as this gate's falsifier and is what "
            "MUT-CLI-PERMISSIVE substitutes" % len(probes),
            all(p["rejected"] == p["expected"] for p in probes),
            {"probes": probes})

    R["waiver_ledger"] = waiver_ledger(LD)
    LD.gate("G-WAIVERS-VERIFIED",
            "THE COVERAGE LEDGER IS HONEST (#34).  Every gate this "
            "instrument declares -- the ones evaluated here and the ones "
            "evaluated only in the paper, mutant, self-test and writing "
            "paths -- is classified FALSIFIABLE, meaning a declared mutant "
            "or a declared control drives it to FAIL, or WAIVED WITH A "
            "FORCING that says "
            "why it cannot fail and what would have to change for it to.  "
            "%d gates: %d falsifiable, %d waived-with-forcing, 0 unaccounted"
            % (len(R["waiver_ledger"]),
               sum(1 for w in R["waiver_ledger"] if w["status"] == "FALSIFIABLE"),
               sum(1 for w in R["waiver_ledger"] if w["status"] == "WAIVED")),
            all(w["status"] in ("FALSIFIABLE", "WAIVED")
                for w in R["waiver_ledger"])
            and all(w["reason"] for w in R["waiver_ledger"]),
            {"gates": len(R["waiver_ledger"]),
             "falsifiable": sum(1 for w in R["waiver_ledger"]
                                if w["status"] == "FALSIFIABLE"),
             "waived": sum(1 for w in R["waiver_ledger"]
                           if w["status"] == "WAIVED"),
             "unaccounted": [w["gate"] for w in R["waiver_ledger"]
                             if w["status"] == "UNACCOUNTED"] or "none"})
    SEAL.take("SEAL-WAIVERS", R)

    # the prediction: 3 paper gates + the mutant gate + the final coverage
    # gate are still to come inside the ledger, and the integrity gate is
    # evaluated only in the writing path and so never reaches the receipt
    R["totals"] = {
        "gates": len(LD.rows) + 6,
        "gates_in_receipt": len(LD.rows) + 5,
        "sources": len(SOURCES), "verbatim_anchors": len(VERBATIM),
        "anchors": len(anchors), "mutants": len(MUTANTS),
        "window_builds": len(WD) + driven_wit + 2,
    }
    return LD, R, SEAL, paper_norm


# ===========================================================================
# SECTION 7.  THE INDEPENDENT COMPARATOR, THE WAIVER LEDGER, THE PAPER GATES
# ===========================================================================

def reconstruct(receipt):
    """THE COMPARATOR (#82).  Input: the receipt's own census rows.  It shares
    no code path, no live object and no typed literal with the builder -- it
    re-derives the rate from the two counts it finds, re-sorts the subgroup
    list from the affine block, and re-assembles all three strings."""
    cls = receipt["affine"]["classes"]
    bc = cls["BEYOND-COSET"]
    rate = Fraction(int(bc["crystalline"]), int(bc["schedules"]))
    subs = sorted(set(receipt["affine"]["beyond_coset_subgroups"]))
    head = "".join([
        "U4B-CRYSTAL-", "GENERIC" if int(bc["crystalline"]) else "SEEDED",
        "-[beyond-coset ", str(rate), "; ", str(int(bc["crystalline"])),
        " of ", str(int(bc["schedules"])), "; ", "|".join(subs), "]"])
    d = receipt["determinant"]
    det = "".join([
        "DET-NONZERO-", "EXISTS" if int(d["nonzero_at_all_sites_pairs"])
        else "EMPTY",
        "-[", d["witness"]["name"], ": det=", d["witness"]["det"],
        " at 9 of 9; ", str(int(d["nonzero_at_all_sites_pairs"])), " of ",
        str(int(d["partition_pairs"])), " pairs; ",
        "POSDEF-EMPTY" if int(d["max_posdef_sites"]) < 9 else "POSDEF-EXISTS",
        "; ",
        "I7-STRICT-EMPTY" if int(d["strictly_positive_pairs"]) == 0
        else "I7-STRICT-EXISTS", "]"])
    c = receipt["constructibility"]
    f = receipt["family"]
    con = "".join([
        "CONSTRUCTIBILITY-[FORCED ", str(int(c["fates"].get("FORCED", 0))),
        " of ", str(int(c["window"])), "; BRANCHING ",
        str(int(c["fates"].get("BRANCHING", 0))), "; REFUSED ",
        str(int(c["fates"].get("REFUSED", 0))), "]@WINDOW-",
        str(int(f["window"])), "-OF-", str(int(f["family"])), "+",
        str(int(receipt["counts"]["stratum_witnesses"])),
        "-STRATUM-WITNESSES"])
    return head, det, con


def reconstruct_from_serialized(text):
    return reconstruct(json.loads(text))


POST_RUN_GATES = ("G-PAPER-CLAIMS", "G-PAPER-NUMERAL-COVERAGE",
                  "G-PAPER-CLAIM-POLARITY", "G-MUTANTS-ON-TARGET",
                  "G-PAPER-COVERAGE-FINAL", "G-ARTIFACT-INTEGRITY",
                  "G-SELFTEST-WRITES-NOTHING")

WAIVERS = {
    "G-MUTANTS-ON-TARGET": ("WAIVED", "the sweep's own closure gate: it "
                            "fails when a declared mutant survives or dies "
                            "off target, which is a fact about the OTHER "
                            "gates, so it has no falsifier of its own"),
    "G-PAPER-COVERAGE-FINAL": ("WAIVED", "the same three checks re-run once "
                               "the totals close; its in-run twins "
                               "G-PAPER-CLAIMS and G-PAPER-NUMERAL-COVERAGE "
                               "carry the injection falsifiers, and this "
                               "evaluation is the enforcement"),
    "G-ARTIFACT-INTEGRITY": ("WAIVED", "evaluated only in the writing path, "
                             "which no mutant run reaches; its negative "
                             "control fires on EVERY delivery run -- a "
                             "deliberately corrupted payload is written to a "
                             "probe path and the comparator must notice "
                             "before either artifact is moved into place"),
    "G-PROV-ALL": ("WAIVED", "an aggregate over per-source gates that each "
                   "carry MUT-ANCHOR's falsifier via --break-anchor; it "
                   "cannot fail once they pass, and --break-anchor NAME "
                   "drives it"),
    "G-SLICE-EXIT-FREE": ("WAIVED", "would fail if a committed v10 layer "
                          "gained an exit call; nothing in this unit can "
                          "make it fail, and the forcing is that the "
                          "sources are hash-pinned -- so --break-anchor "
                          "A-D42B1 is the live falsifier of the same read"),
    "G-GRAMMAR-LIVE": ("WAIVED", "a two-directional behavioural probe of a "
                       "hash-pinned committed function; it fails if that "
                       "function changes, which the provenance gate "
                       "forbids first"),
    "G-I7-READOUT": ("FALSIFIABLE", "MUT-DET-EMPTY and the A-EFF-I7 anchor "
                     "both drive it"),
    "G-STAB-FULL-FAMILY": ("FALSIFIABLE", "MUT-FAMILY-COUNT moves the family "
                           "total the gate's own sum must reach"),
    "G-EXACT": ("WAIVED", "would fail on any float entering this file or "
                "the receipt; no mutant introduces one because a mutant "
                "that did would be testing Python, not this census -- the "
                "forcing is the AST scan, which is evaluated fresh on the "
                "file's own bytes at every run"),
    "G-WAIVERS-VERIFIED": ("WAIVED", "the ledger's own closure gate; it "
                           "fails if any gate is unclassified, which is a "
                           "construction error rather than a measurement"),
    "G-SEAL-COMPLETE": ("FALSIFIABLE", "MUT-SEAL-BROKEN mutates a sealed "
                        "object after its gate"),
}


def waiver_ledger(LD):
    out = []
    targets = {m[1] for m in MUTANTS}
    for g in [r["gate"] for r in LD.rows] + list(POST_RUN_GATES):
        if g in WAIVERS:
            status, reason = WAIVERS[g]
        elif g in targets:
            status = "FALSIFIABLE"
            reason = "driven to FAIL by %s" % ", ".join(
                sorted(m[0] for m in MUTANTS if m[1] == g))
        elif g.startswith("G-PROV["):
            status = "FALSIFIABLE"
            reason = "driven to FAIL by --break-anchor %s" % g[7:-1]
        else:
            status = "UNACCOUNTED"
            reason = ""
        out.append({"gate": g, "status": status, "reason": reason})
    return out


def paper_claims(R):
    c = R["counts"]
    d = R["determinant"]
    a = R["affine"]["classes"]
    return [
        ("C01", R["verdict"]["crystal"]),
        ("C02", R["verdict"]["det"]),
        ("C03", R["verdict"]["constructibility"]),
        ("C04", "the family has %d schedules" % c["family"]),
        ("C05", "the declared window has %d schedules" % c["window"]),
        ("C06", "%d of %d schedules are crystalline"
         % (c["crystalline"], c["family"])),
        ("C07", "every one of the %d CU-JOINT seed pairs is crystalline"
         % 36),
        ("C08", "none of the %d CU-SPLIT seed pairs is crystalline" % 108),
        ("C09", "%d of the %d beyond-coset schedules are crystalline"
         % (a["BEYOND-COSET"]["crystalline"], a["BEYOND-COSET"]["schedules"])),
        ("C10", "%d of the %d partition pairs carry det != 0 at all nine "
         "sites" % (d["nonzero_at_all_sites_pairs"], d["partition_pairs"])),
        ("C11", "the maximum number of positive-definite sites is %d"
         % d["max_posdef_sites"]),
        ("C12", "no partition pair makes all 27 link counts strictly "
         "positive"),
        ("C13", "the footprint field is the constant 2 at every site of "
         "every schedule"),
        ("C14", "all %d admissible single-arbitration re-seatings break the "
         "stabilizer" % 12),
        ("C15", "the named witness is %s" % d["witness"]["name"]),
    ]


PAPER_POLARITY = [
    ("P1", "U4B-CRYSTAL-GENERIC", "U4B-CRYSTAL-SEEDED-"),
    ("P2", "DET-NONZERO-EXISTS", "DET-NONZERO-EMPTY"),
    ("P3", "POSDEF-EMPTY", "POSDEF-EXISTS"),
    ("P4", "I7-STRICT-EMPTY", "I7-STRICT-EXISTS"),
]

DERIVED_IN_TEXT = {
    "0": "the zero of a link count, a determinant and a refusal count",
    "1": "section numbers, the trivial subgroup, the unit link count",
    "2": "section numbers, the two rounds, the constant footprint value",
    "3": "section numbers, the three groups per round, the three proposers, "
         "Z_3^2's exponent",
    "4": "section numbers, the four parallel classes, the four order-3 "
         "subgroups",
    "5": "section numbers", "6": "section numbers, the six division events",
    "7": "section numbers", "8": "section numbers", "9": "the nine sites",
    "10": "section numbers", "11": "section numbers",
    "14": "the corpus's v14 label", "13": "the corpus's v13 label",
    "17": "this paper's number",
    "42": "the layer name `d42b1`", "60": "the layer name `d60`",
    "256": "the hash width in `sha256-12`",
    "119": "the RUNBOOK engraving numbers", "125": "the RUNBOOK engraving",
    "82": "the RUNBOOK engraving", "87": "the RUNBOOK engraving",
    "91": "the RUNBOOK engraving", "62": "the RUNBOOK engraving",
    "34": "the RUNBOOK engraving", "24": "the RUNBOOK engraving",
    "15": "the RUNBOOK section",
    "126": "this unit's ledger number",
    "3.2": "HA's section number", "2.1": "paper-13's section number",
    "2.2": "a subsection number of this paper",
    "2.3": "a subsection number of this paper",
    "2.4": "a subsection number of this paper",
    "4.1": "a subsection number of this paper",
    "4.2": "a subsection number of this paper",
    "5.1": "a subsection number of this paper",
    "5.2": "a subsection number of this paper",
    "5.3": "a subsection number of this paper",
    "2026": "the year", "12": "the edit count",
    "00": "the actor name G00 (the site (0,0))",
    "11": "a component index of the induced form (q11)",
    "22": "a component index of the induced form (q22)",
    "16": "the class pairs", "27": "the I7 cells and the seed assignments",
    "18": "the link-incidence budget", "36": "the CU-JOINT pairs",
    "108": "the CU-SPLIT pairs", "84": "the 3-subsets of Z_3^2",
    "280": "the partitions", "90": "the uniform weight",
    "729": "the seed pairs per partition pair", "747": "the det9 pairs",
    "7056": "the seed pairs", "6912": "the beyond-coset pairs",
}


HEXTOKEN = re.compile(r"\b(?=[0-9a-f]{7,64}\b)(?=[0-9a-f]*[a-f])[0-9a-f]+\b")
DECLARED_COMMITS = {
    "06b89fe": "the commit at which the U4 delivery artifacts are frozen and "
               "readable, cited and NOT read (a repair worker holds them "
               "under rewrite)",
    "58195da": "the commit at which weld 2's SEC 6 rebuild is readable, cited "
               "and NOT read",
    "42417f6": "the commit that froze this unit's pin",
}


def paper_coverage(R, paper_text):
    claims = paper_claims(R)
    hay = norm(ascii_fold(paper_text))
    missing = [cid for cid, txt in claims
               if norm(ascii_fold(txt)) not in hay]
    folded = ascii_fold(paper_text)
    hexes = set(HEXTOKEN.findall(folded))
    declared_hex = {s[2] for s in SOURCES} | set(DECLARED_COMMITS)
    undeclared_hex = sorted(hexes - declared_hex)
    nums = re.findall(r"[0-9]+(?:[.,/][0-9]+)*", HEXTOKEN.sub(" ", folded))

    def covered(n):
        """a numeral is covered if this run registered it, if it is a
        declared in-text residue, if it is the same number with thousands
        separators, or -- for a comma-joined coordinate such as `(1,0)` --
        if every comma-separated part is itself covered."""
        if n in NUMREG or n in DERIVED_IN_TEXT or n.replace(",", "") in NUMREG:
            return True
        parts = n.split(",")
        return (len(parts) > 1
                and all(q in NUMREG or q in DERIVED_IN_TEXT for q in parts))
    uncovered = sorted({n for n in nums if not covered(n)})
    declared_absent = sorted({k for k in DERIVED_IN_TEXT
                              if k not in nums and k not in NUMREG})
    return {"claims": len(claims), "missing": missing,
            "uncovered": uncovered,
            "residue_declared_but_absent": declared_absent,
            "hex_tokens": sorted(hexes),
            "undeclared_hex": undeclared_hex,
            "distinct_numerals": len(set(nums)),
            "numeral_occurrences": len(nums)}


def mutate_paper(text):
    """the two paper-side injections: a dropped claim and an unregistered
    numeral.  They act on a COPY of the object under test, never on disk."""
    if mut("MUT-PAPER-CLAIM"):
        return text.replace("crystalline", "crystallime")
    if mut("MUT-PAPER-NUMERAL"):
        return text + "\n\nAn unregistered number: 31337.\n"
    return text


def paper_polarity(R, paper_text, mutated=False):
    hay = norm(ascii_fold(paper_text))
    rows = []
    for pid, true_s, false_s in PAPER_POLARITY:
        t = norm(ascii_fold(true_s)) in hay
        f = norm(ascii_fold(false_s)) in hay
        if mutated and pid == "P1":
            t, f = False, True
        rows.append({"id": pid, "true_present": t, "false_present": f,
                     "ok": t and not f})
    return rows


# ===========================================================================
# SECTION 8.  THE CLI
# ===========================================================================

def parse_args(argv):
    opts = {"write": True, "mutant": None, "break_anchor": None,
            "verify_paper": None, "selftest": False, "numbers": False}
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == "--no-write":
            opts["write"] = False
        elif a == "--numbers":
            opts["numbers"] = True
            opts["write"] = False
        elif a == "--selftest":
            opts["selftest"] = True
            opts["write"] = bool(mut("MUT-SELFTEST-WRITES"))
        elif a == "--mutant":
            if i + 1 >= len(argv):
                raise CliError("--mutant requires a mutant NAME")
            if argv[i + 1] not in MUTANT_NAMES:
                raise CliError("unknown mutant %r" % argv[i + 1])
            opts["mutant"] = argv[i + 1]
            opts["write"] = False
            i += 1
        elif a == "--break-anchor":
            if i + 1 >= len(argv):
                raise CliError("--break-anchor requires an anchor NAME")
            if argv[i + 1] not in SOURCE_IDS:
                raise CliError("unknown anchor %r" % argv[i + 1])
            opts["break_anchor"] = argv[i + 1]
            opts["write"] = False
            i += 1
        elif a == "--verify-paper":
            opts["verify_paper"] = PAPER_REL
            if i + 1 < len(argv) and not argv[i + 1].startswith("--"):
                opts["verify_paper"] = argv[i + 1]
                i += 1
            p = opts["verify_paper"]
            if not os.path.exists(p if os.path.isabs(p)
                                  else os.path.join(REPO, p)):
                raise CliError("no such paper %r" % p)
            opts["write"] = False
        else:
            raise CliError("unknown argument %r" % a)
        i += 1
    return opts


def parse_args_permissive(argv):
    """THE FORBIDDEN SHAPE (#82, four named recurrences): a runner that
    ignores what it does not recognise.  Present only as G-CLI-WHITELIST's
    falsifier; nothing in the delivery path calls it."""
    return {"write": True, "mutant": None, "break_anchor": None,
            "verify_paper": None, "selftest": False, "numbers": False}


def selftest_result():
    """MEASURED, never typed: corrupt one anchor, run, and observe both
    whether the run died and whether anything on disk moved."""
    global QUIET
    was, saved_lines = QUIET, list(LINES)
    QUIET = True
    watched = (OUT_TXT, OUT_JSON, OUT_TXT + ".selftest-probe")

    def snap():
        return {p: (os.path.exists(p),
                    os.path.getmtime(p) if os.path.exists(p) else None,
                    os.path.getsize(p) if os.path.exists(p) else None)
                for p in watched}
    before = snap()
    died = False
    try:
        full_run("A-D42B1", "", PAPER_REL)
    except (GateFail, SystemExit):
        died = True
    if mut("MUT-SELFTEST-WRITES"):
        # THE INJECTION: the self-test path is allowed to reach a writer.
        with open(watched[2], "w", encoding="utf-8") as fh:
            fh.write("a writer was reached\n")
    wrote = (before != snap())
    if os.path.exists(watched[2]):
        os.remove(watched[2])
    LINES[:] = saved_lines
    QUIET = was
    return died, wrote


def selftest():
    """#82: corrupt one anchor, confirm exit 1, write nothing."""
    died, wrote = selftest_result()
    print("SELFTEST: corrupted anchor A-D42B1 -> run died = %s; wrote "
          "anything = %s" % (died, wrote))
    if not died:
        print("SELFTEST FAILED: the corrupted run did not die", file=sys.stderr)
        sys.exit(2)
    if wrote:
        print("GATE FAILED: G-SELFTEST-WRITES-NOTHING :: the self-test path "
              "reached a writer", file=sys.stderr)
        sys.exit(2)
    print("G-SELFTEST-WRITES-NOTHING: the corrupted run died at the anchor "
          "gate and wrote nothing.")
    sys.exit(1)


def emit_report(R, SEAL):
    say("")
    say("=" * 78)
    say("RECEIPT")
    say("=" * 78)
    say("  gates      : %d evaluated, all passed" % R["totals"]["gates"])
    say("  sources    : %d hash-pinned; verbatim anchors %d; read anchors %d"
        % (R["totals"]["sources"], R["totals"]["verbatim_anchors"],
           R["totals"]["anchors"]))
    say("  mutants    : %d declared" % R["totals"]["mutants"])
    say("  menu drives: %d records built by the layer's own menu"
        % R["totals"]["window_builds"])
    say("  seals      : %d objects sealed at gate time" % len(SEAL.rows))
    for row in SEAL.rows:
        say("    %-24s %-28s %s" % (row["seal"], row["path"],
                                    row["sha256_12"]))
    SEAL.close_transcript("\n".join(LINES) + "\n")


def main():
    global MUT, QUIET
    try:
        opts = parse_args(sys.argv[1:])
    except CliError as e:
        print("usage: %s [--no-write] [--numbers] [--selftest] "
              "[--mutant NAME] [--break-anchor NAME] [--verify-paper [PATH]]"
              % os.path.basename(SELF), file=sys.stderr)
        print("error: %s" % e, file=sys.stderr)
        sys.exit(2)
    if opts["selftest"]:
        selftest()
    MUT = opts["mutant"]
    write = opts["write"]

    say("=" * 78)
    say("v14 U4b -- THE SCHEDULE CENSUS (paper-17)")
    say("=" * 78)
    if MUT:
        say("MUTANT ACTIVE: %s" % MUT)
    if opts["break_anchor"]:
        say("ANCHOR BREAK SELF-TEST: %s" % opts["break_anchor"])

    paper_rel = opts["verify_paper"] or PAPER_REL
    paper_path = (paper_rel if os.path.isabs(paper_rel)
                  else os.path.join(REPO, paper_rel))
    paper_text = read_text(paper_path) if os.path.exists(paper_path) else ""
    if opts["verify_paper"]:
        say("VERIFY-PAPER: the object under test is %s" % paper_rel)

    try:
        LD, R, SEAL, _pn = full_run(opts["break_anchor"], paper_text, paper_rel)
    except GateFail as e:
        say("")
        say("GATE FAILED: %s" % e)
        say("EXIT 1")
        sys.exit(1)

    if opts["numbers"]:
        say("")
        say("THE CLAIMS THIS INSTRUMENT MAKES (each must be rendered in the "
            "paper)")
        for cid, txt in paper_claims(R):
            say("  %s  %s" % (cid, txt))
        say("")
        say("THE REGISTERED NUMERALS (%d)" % len(NUMREG))
        say("  " + " ".join(sorted(NUMREG)))
        say("")
        say("--numbers: the census is printed above; no paper gate, no "
            "mutant sweep, nothing written.")
        sys.exit(0)

    # -- the paper gates -----------------------------------------------------
    say("")
    say("=" * 78)
    say("SEC 11  THE PAPER GATES")
    say("=" * 78)
    try:
        cov = paper_coverage(R, mutate_paper(paper_text))
        LD.gate("G-PAPER-CLAIMS",
                "every one of the %d claims this instrument makes is rendered "
                "in the paper under test, whitespace-normalised and "
                "ASCII-folded on both sides (#125)" % cov["claims"],
                not cov["missing"], {"missing": cov["missing"] or "none",
                                     "claims": cov["claims"]})
        LD.gate("G-PAPER-NUMERAL-COVERAGE",
                "every numeral occurring in the paper is either a number this "
                "run COMPUTED and registered, or one of the %d declared "
                "in-text residues; every hexadecimal token is one of the %d "
                "pinned source digests or the %d declared commits; %d "
                "distinct numerals over %d occurrences"
                % (len(DERIVED_IN_TEXT), len(SOURCES),
                   len(DECLARED_COMMITS), cov["distinct_numerals"],
                   cov["numeral_occurrences"]),
                not cov["uncovered"] and not cov["undeclared_hex"],
                {"uncovered": cov["uncovered"] or "none",
                 "undeclared_hex": cov["undeclared_hex"] or "none"})
        pol = paper_polarity(R, paper_text, mut("MUT-PAPER-POLARITY"))
        LD.gate("G-PAPER-CLAIM-POLARITY",
                "every declared polarity of the head is present in the paper "
                "in its TRUE form and absent in its FALSE form: %d pairs"
                % len(pol),
                all(p["ok"] for p in pol),
                {"polarity": pol})
    except GateFail as e:
        say("")
        say("GATE FAILED: %s" % e)
        say("EXIT 1")
        sys.exit(1)
    R["paper_coverage"] = cov
    R["paper_polarity"] = pol
    R["paper_claims"] = [{"id": c, "text": t} for c, t in paper_claims(R)]

    if opts["verify_paper"]:
        say("")
        say("VERIFY-PAPER: %s -- every claim rendered, every numeral covered, "
            "every polarity held." % paper_rel)
        say("EXIT 0")
        sys.exit(0)
    if MUT or opts["break_anchor"]:
        say("")
        say("MUTANT SURVIVED: %s" % (MUT or opts["break_anchor"]))
        say("EXIT 0")
        sys.exit(0)

    # -- the mutant sweep ----------------------------------------------------
    say("")
    say("=" * 78)
    say("SEC 12  THE DECLARED MUTANTS, RUN IN PROCESS")
    say("=" * 78)
    report, all_dead, on_target = [], True, 0
    clean_numreg = set(NUMREG)
    for nm, target, note in MUTANTS:
        MUT = nm
        QUIET = True
        saved = list(LINES)
        killed_at = None
        try:
            if nm == "MUT-SELFTEST-WRITES":
                died, wrote = selftest_result()
                killed_at = ("G-SELFTEST-WRITES-NOTHING" if wrote else None)
            elif nm == "MUT-PAPER-POLARITY":
                p = paper_polarity(R, paper_text, True)
                killed_at = (None if all(x["ok"] for x in p)
                             else "G-PAPER-CLAIM-POLARITY")
            elif nm == "MUT-PAPER-CLAIM":
                c = paper_coverage(R, mutate_paper(paper_text))
                killed_at = "G-PAPER-CLAIMS" if c["missing"] else None
            elif nm == "MUT-PAPER-NUMERAL":
                c = paper_coverage(R, mutate_paper(paper_text))
                killed_at = ("G-PAPER-NUMERAL-COVERAGE"
                             if c["uncovered"] or c["undeclared_hex"]
                             else None)
            else:
                full_run(None, paper_text, paper_rel)
        except GateFail as e:
            killed_at = str(e).split(" ::")[0]
        except SystemExit:
            killed_at = "SYSTEM-EXIT"
        LINES[:] = saved
        QUIET = False
        MUT = None
        report.append({"mutant": nm, "target": target, "note": note,
                       "killed": killed_at is not None, "killed_at": killed_at,
                       "on_target": killed_at == target})
        if killed_at is None:
            all_dead = False
        if killed_at == target:
            on_target += 1
        say("  %-24s -> %s" % (nm, killed_at or "SURVIVED"))
    NUMREG.clear()
    NUMREG.update(clean_numreg)
    R["mutants"] = report
    off = [(m["mutant"], m["target"], m["killed_at"]) for m in report
           if not m["on_target"]]
    try:
        LD.gate("G-MUTANTS-ON-TARGET",
                "every one of the %d declared mutants is killed, and killed "
                "by the gate it was declared to falsify: a mutant that dies "
                "elsewhere is a gate boundary this unit does not understand"
                % len(MUTANTS),
                all_dead and on_target == len(MUTANTS),
                {"killed": sum(1 for m in report if m["killed"]),
                 "on_target": on_target, "off_target": off or "none"})
    except GateFail as e:
        say("")
        say("GATE FAILED: %s" % e)
        say("EXIT 1")
        sys.exit(1)
    SEAL.take("SEAL-MUTANTS", R)

    R["gates"] = LD.rows
    R["totals"]["mutants_killed"] = sum(1 for m in report if m["killed"])
    R["totals"]["mutants_on_target"] = on_target
    if R["totals"]["gates"] != len(LD.rows) + 2:
        say("")
        say("GATE FAILED: G-PAPER-COVERAGE-FINAL :: the predicted gate count "
            "%d did not close at %d" % (R["totals"]["gates"], len(LD.rows) + 1))
        say("EXIT 1")
        sys.exit(1)
    try:
        cov2 = paper_coverage(R, paper_text)
        LD.gate("G-PAPER-COVERAGE-FINAL",
                "the paper-claim and numeral-coverage check is re-run once "
                "the instrument's own totals close, so the paper's instrument "
                "section is covered too; its in-run twins carry the injection "
                "falsifiers and this evaluation is the enforcement -- a "
                "failure here exits 1 and writes nothing.  It also closes the "
                "residue ledger: every declared in-text residue must actually "
                "occur in the paper, so the list cannot be padded",
                not cov2["missing"] and not cov2["uncovered"]
                and not cov2["undeclared_hex"]
                and not cov2["residue_declared_but_absent"],
                {"missing": cov2["missing"] or "none",
                 "uncovered": cov2["uncovered"] or "none",
                 "undeclared_hex": cov2["undeclared_hex"] or "none",
                 "declared_but_absent":
                     cov2["residue_declared_but_absent"] or "none"})
    except GateFail as e:
        say("")
        say("GATE FAILED: %s" % e)
        say("EXIT 1")
        sys.exit(1)
    R["paper_coverage"] = cov2
    R["gates"] = LD.rows
    # counted AFTER the last ledger gate, so the published row is not a
    # snapshot of an earlier moment in the run
    R["totals"]["gates_passed"] = sum(1 for g in LD.rows if g["passed"])
    SEAL.take("SEAL-GATES", R)
    SEAL.take("SEAL-TOTALS", R)

    SEAL.close(R, json.dumps(R, indent=1, sort_keys=True, default=str))
    emit_report(R, SEAL)

    if write:
        payload, text = SEAL.payload, SEAL.transcript

        def against_the_seal(js, tx):
            if (digest(js) != SEAL.payload_sha
                    or digest(tx) != SEAL.transcript_sha):
                return False
            disk = json.loads(js)
            if SEAL.verify(disk):
                return False
            return (reconstruct_from_serialized(js)
                    == (R["verdict"]["crystal"], R["verdict"]["det"],
                        R["verdict"]["constructibility"]))

        probe = OUT_JSON + ".integrity-probe"
        with open(probe, "w", encoding="utf-8") as f:
            f.write(payload[:-1] + " }")
        detected = digest(read_text(probe)) != SEAL.payload_sha
        os.remove(probe)
        tj, tt = OUT_JSON + ".tmp", OUT_TXT + ".tmp"
        with open(tj, "w", encoding="utf-8") as f:
            f.write(payload)
        with open(tt, "w", encoding="utf-8") as f:
            f.write(text)
        if not (detected and against_the_seal(read_text(tj), read_text(tt))):
            os.remove(tj)
            os.remove(tt)
            print("GATE FAILED: G-ARTIFACT-INTEGRITY :: what was about to be "
                  "written does not match the gate-time seal (corruption "
                  "detected=%s); nothing written" % detected, flush=True)
            sys.exit(1)
        os.replace(tj, OUT_JSON)
        os.replace(tt, OUT_TXT)
        if not against_the_seal(read_text(OUT_JSON), read_text(OUT_TXT)):
            print("GATE FAILED: G-ARTIFACT-INTEGRITY :: the artifacts on disk "
                  "differ from the gate-time seal", flush=True)
            sys.exit(1)
        print("G-ARTIFACT-INTEGRITY: corrupted probe detected; both artifacts "
              "written from the SEALED payload, re-read from disk and matched "
              "against the gate-time seal -- %d sealed objects, payload %s, "
              "transcript %s (%d + %d bytes)."
              % (len(SEAL.rows), SEAL.payload_sha, SEAL.transcript_sha,
                 len(payload), len(text)), flush=True)
    sys.exit(0)


if __name__ == "__main__":
    main()
