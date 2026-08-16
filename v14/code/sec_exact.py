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
  SEC 1  PROVENANCE.  15 pinned sources, sha256-12 verified, products gated;
         verbatim (#62) anchors bound to their consumer gates AND checked on
         the QUOTE side wherever the paper quotes them; every read at run time
         is recorded at the I/O accessor and the register is gated, so the
         cited-and-not-read abstention is an observation; every text gate
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
  SEC 13 The verdict, derived a second time from the serialized receipt by TWO
         comparators -- one for the dictionary word, one for the overlap word,
         the latter typing the k-hypothesis and the alignment-hypothesis itself
         and exercised on three declared control families through the REAL weld
         machinery; the paper gates -- EVERY table row AND EVERY table header
         rendered as a claim, numeral coverage INCLUDING FENCED BLOCKS AND
         INLINE SPANS, fenced blocks BY MULTISET EQUALITY WHATEVER THE INFO
         STRING, head-verbatim, quoted-source verbatim and claim polarity on
         every direction-bearing sentence; the TOTAL seal, VERIFIED against the
         payload before anything is written; the sweep-execution binding taken
         on the sweep's own rows; the staged artifacts; the integrity check.

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
    --mutant NAME   runs the pipeline with the named mutant active.  Exits 0
                    when the mutant dies at its declared gate (the intended
                    outcome) and 1 when it survives or dies elsewhere, so a
                    wrapper reading shell truth reads a clean sweep as clean.
                    An unknown NAME exits 2.  Writes nothing.
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
seals are then VERIFIED against the serialized payload before a byte is
written, the artifacts are STAGED beside their destinations, verified again
from the staged bytes with a corruption probe that is shown to fire, and only
then promoted through `os.replace`; the terminal integrity gate re-reads the
promoted bytes.  A run that fails a gate writes nothing, promotes nothing and
leaves no staging behind.

RUNTIME INPUTS (#46/#91).  Exactly 15 files are read at run time as SOURCES,
all hash-pinned by this unit's frozen declaration, plus exactly one file read
as the OBJECT UNDER TEST -- this unit's own paper -- plus this file itself and
this run's own staged artifacts.  EVERY read is recorded AT THE ACCESSOR with
its category, and the register is what the provenance and abstention gates
consume, so a read taken anywhere in this file is visible to them.  No
repository state outside the register is read and no subprocess of any kind is
invoked, so the run is correct off-tree and with no version control present.
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

# the terms whose presence in this run's measurement layer or in the paper
# would mean a reading this unit does not take had been taken.  Module-level
# because BOTH wall gates consume it -- the one inside the run and the TOTAL
# one at the writer, which scans the whole payload rather than the part of it
# that happened to exist when the first one ran.
BARRED_TERMS = ("boost", "rapidity", "sprinkl", "myrheim", "meyer", "shatter",
                "cosmolog", "continuum", "horizon", "redshift", "expansion",
                "universe", "big bang", "spacetime")

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
    ("MUT-WALL-SCAN", "writes one of the scanned barred terms into the "
     "measurement layer", "G-WALL-SCAN"),
    ("MUT-WALL-PAPER", "writes a banned dimension reading into the paper",
     "G-WALL-SCAN"),
    ("MUT-CITED-READ", "inverts the cited-and-not-read abstention",
     "G-CITED-NOT-READ"),
    ("MUT-PAPER-TABLE", "swaps two data cells of a published table row",
     "G-PAPER-CLAIMS"),
    ("MUT-PAPER-COMPAT", "flips the VERDICT WORD of a compatibility-census "
     "row in the paper, COMPATIBLE to SEAM-DEFORMED", "G-PAPER-CLAIMS"),
    ("MUT-ANCHOR-CONSUMER", "points one verbatim anchor at a gate this run "
     "never emits", "G-ANCHOR-CONSUMERS"),
    ("MUT-PAPER-ROWSET", "appends a STRAY data row nobody rendered to a real "
     "table in the paper", "G-PAPER-ROWSET"),
    ("MUT-PAPER-NAME", "publishes an object-under-test name the read register "
     "does not carry", "G-SOURCES"),
    ("MUT-STAMP-NAME", "stamps a fraction collection the paper never names",
     "G-DECLARED-STANDARDS"),
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
    ("MUT-STRAY-READ", "takes an undeclared repository read at the run's own "
     "I/O accessor", "G-SOURCES"),
    ("MUT-SEAM-CONFINED", "forges one seam-confinement row, reporting a moved "
     "cell that touches an unshared actor", "G-SEAM-CONFINED"),
    ("MUT-CARRIER-FIELD", "moves the induced count field on one extended-"
     "carrier row", "G-CARRIER-FIELD"),
    ("MUT-DEGREE", "forges one type's shared-actor degree", "G-DEGREE"),
    ("MUT-ARENA-COUNT", "forges the union-arena isomorphism classes",
     "G-ARENA-COUNT"),
    ("MUT-TYPE-INVARIANT", "poisons one sampled member's abstract union arena",
     "G-TYPE-INVARIANT"),
    ("MUT-SEED-PREDICATE", "flips one off-window validation record's predicted "
     "fate", "G-SEED-PREDICATE"),
    ("MUT-REP-SPREAD", "forges the representative-relative spread of the "
     "chart-borne fibers", "G-REPRESENTATIVE-ROWS"),
    ("MUT-SEAM-PROFILE-SPREAD", "forges the per-site seam profile's spread "
     "inside the type", "G-REPRESENTATIVE-ROWS"),
    ("MUT-SEAM-SITES", "misreports one shared site's seam kernel in the "
     "all-sites census", "G-SEAM-ALL-SITES"),
    ("MUT-ARRANGEMENT-ALL", "drops one admissible arrangement triple from the "
     "exhaustion", "G-ARRANGEMENT-FREE"),
    ("MUT-OVERLAP-WORD", "forges the overlap comparator's outcome word",
     "G-OVERLAP-RECON"),
    ("MUT-CONTROL-ARM", "forges one control family's emitted outcome word",
     "G-OVERLAP-CONTROLS"),
    ("MUT-STRUCT-INHERIT", "breaks the union-is-the-amalgam's-incidence "
     "identity on one type", "G-STRUCT-INHERITED"),
    ("MUT-SEED-FATE", "forges one shared-rule window fate", "G-SEED-RULE"),
    ("MUT-DEAD-FATE", "forges one declared dead arm's fate", "G-CONTROLS"),
    ("MUT-CROSS-ALGEBRA", "moves one kernel of the cross-link ladder",
     "G-SEAM-CROSS-ALGEBRA"),
    ("MUT-CONTRAST", "flattens the contrast against the sterile arm",
     "G-CONTRAST"),
    ("MUT-AUT-ROUTE-UNION", "poisons the union census's second automorphism "
     "route", "G-AUT-ROUTES-UNION"),
    ("MUT-PAPER-HEADER", "swaps two column labels of a published table header",
     "G-PAPER-TABLES"),
    ("MUT-PAPER-FENCE-INFO", "hides a forged head in a fenced block whose info "
     "string carries a non-letter", "G-PAPER-FENCE"),
    ("MUT-PAPER-PERIOD", "moves a paper numeral that is followed by a period",
     "G-PAPER-COVERAGE"),
    ("MUT-PAPER-DIRECTION", "inverts a direction-bearing headline sentence of "
     "the paper", "G-PAPER-POLARITY"),
    ("MUT-PAPER-QUOTE", "inverts a source sentence the paper quotes",
     "G-PAPER-QUOTES"),
    ("MUT-SEAL-FORGE", "moves a sealed value between its gate and the write",
     "G-SEAL-VERIFIED"),
    ("MUT-SWEEP-FORGE", "hands the writer a sweep row set that is not this "
     "run's own", "G-SWEEP-EXECUTED"),
    ("MUT-WALL-TOTAL", "writes a barred reading into a receipt key that did "
     "not exist when the in-run wall gate ran", "G-WALL-TOTAL"),
    ("MUT-SEED-CENSUS", "forges one type's shared-rule seed-carry count",
     "G-SEED-CENSUS"),
    ("MUT-PAPER-REFERENT", "plants a sentence whose numerals are each in the "
     "registry and each false of the noun it precedes", "G-PAPER-REFERENTS"),
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

    def verify(self, payload):
        """#119, the leg the seal was bought for: every sealed key is
        re-digested FROM THE PAYLOAD ABOUT TO BE WRITTEN and compared against
        the digest taken at gate time.  A value that moved between its gate
        and the write is caught before a byte reaches the disk."""
        bad = []
        for key, d in sorted(self.seals.items()):
            if key not in payload or digest(payload[key]) != d:
                bad.append(key)
        return bad


# THE READ REGISTER, RECORDED AT THE I/O ACCESSOR (#46/#91).  A register the
# producer fills from the same list the consumer compares it against proves
# nothing: it is true by construction and cannot observe a read taken
# elsewhere.  Every open in this file goes through `_open_recorded`, which
# appends the path and its category BEFORE the bytes are returned, so a read
# taken anywhere -- including one a mutant inserts -- is in the register the
# provenance and abstention gates consume.
READS = []

# the run's own anchor rows, kept for the transcript and for the paper leg's
# quote-side check; a one-slot list rather than a growing register
LAST_ANCHORS = [[]]


def _open_recorded(path, category):
    with open(path, "rb") as f:
        raw = f.read()
    READS.append({"path": os.path.relpath(os.path.abspath(path), REPO),
                  "category": category,
                  "sha256_12": hashlib.sha256(raw).hexdigest()[:12]})
    return raw


def _write_staged(path, text):
    """THE ONLY WRITER IN THIS FILE, and it never writes a destination.  It
    writes BESIDE the destination, under a staging suffix, and returns the
    staging path; promotion is a separate step that runs only after the staged
    bytes have been read back and compared.  The AST scan at G-EXACT knows both
    functions by name, so no other call site can open a file for any purpose."""
    stage = path + ".staging"
    with open(stage, "w") as f:
        f.write(text)
    return stage


def _unstage(paths):
    for p in paths:
        if os.path.exists(p):
            os.remove(p)


def read_bytes(rel, category="SOURCE"):
    return _open_recorded(os.path.join(REPO, rel), category)


def read_text_file(path, category="SOURCE"):
    return _open_recorded(path, category).decode("utf-8")


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


# THE COMMITTED MENU'S CACHE, and the ONE cache in this file that is not
# cleared between runs.  The object cached is d42b1's OWN `candidates_for`
# output, a pure function of (history, initiators): no mutant in this file
# alters that function, and none can be made inert by caching it, because the
# only mutant that touches the menu (MUT-MENU-MEMO) acts on the UN-cached path
# -- `use_memo = False` bypasses this dictionary entirely and calls the
# committed function directly, which is exactly the path G-MENU-PURE re-drives
# on.  Sharing it across the in-process mutant sweep is therefore sound and it
# is what makes the sweep affordable: 55 of the 56 mutant runs re-walk
# histories the first run already priced.
RAW_MENU_CACHE = {}


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
        self.memo = RAW_MENU_CACHE
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
        -- which bypasses the cache entirely and calls the committed function
        -- and compares the records event for event."""
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


SEEDCARRY_CACHE = {}


def seed_carry(glue, seedrule):
    """THE SEED-CARRY PREDICATE, and it is a property of the SCHEDULE and not
    a re-implementation of the layer's menu: in the SECOND sector's first
    round, is every group that holds a shared actor SEEDED by a shared actor?
    Nothing here decides admissibility -- the driven layer decides, and
    G-SEED-PREDICATE compares this predicate against the DRIVEN fate at every
    driven record, on and off the window, before any census it predicts is
    published.  Under the shared-seed rule it is true by construction; under
    paper-19's canonical rule it reads the actors' NAMES, which the
    combinatorial type does not fix.

    The memo is on a DERIVED KEY and never on a verdict: the second sector's
    schedule reads only which of the nine B-sites are shared, so the predicate
    is a function of that set and of the rule -- 130 distinct sets in this
    family -- and the cache is cleared at the start of every run."""
    key = (frozenset(sb for _sa, sb in glue), seedrule)
    got = SEEDCARRY_CACHE.get(key)
    if got is not None:
        return got
    _actors, _amap, bmap, shared = gluing_maps(glue)
    rounds = sector_rounds(bmap, SAT_COLLINEAR, seedrule, shared)
    out = True
    for (grp, sd) in rounds[0]:
        if any(a in shared for a in grp) and sd not in shared:
            out = False
            break
    SEEDCARRY_CACHE[key] = out
    return out


def type_sample(pool, n):
    """the declared sample of a type's own members: the representative first,
    then evenly spaced members of the enumeration, capped at n.  Deterministic,
    with no random source anywhere in this file."""
    if len(pool) <= n:
        return list(pool)
    step = len(pool) // n
    return [pool[i * step] for i in range(n)]


def union_degrees(actors, rel, shared):
    """the union's bare degree at the shared and at the unshared actors, and
    THE DEFICIT: a shared actor carries both sectors' six links, so it would
    have degree 2*6 were no pair doubled; each doubled pair is ONE link of the
    union and costs each of its two shared endpoints one degree.  The deficit
    summed over the shared actors is therefore exactly twice the doubled
    count, and that identity is the law the census gates."""
    deg = {a: 0 for a in actors}
    for e in rel:
        for u in e:
            deg[u] += 1
    sh = sorted({deg[a] for a in actors if a in shared})
    un = sorted({deg[a] for a in actors if a not in shared})
    base = 2 * (un[0] if un else 0)
    deficit = sum(base - deg[a] for a in actors if a in shared)
    return sh, un, deficit


def all_arrangement_triples():
    """EVERY admissible arrangement of a sector, by exhaustion rather than by
    one witness: all partitions of the nine sites into triples, those that are
    I7-STRICT saturating, and every triple of them that covers each of the 27
    (site, direction) cells exactly once.  Returns (triples, n_saturating,
    n_partitions)."""
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
    sat = [(P, m) for P, m in ((P, mask(P)) for P in parts)
           if m is not None and len(m) == 9]
    full = frozenset((x, l) for x in SITES for l in I7L)
    out = []
    for i, (P1, m1) in enumerate(sat):
        for j, (P2, m2) in enumerate(sat):
            if j <= i or (m1 & m2):
                continue
            for k, (P3, m3) in enumerate(sat):
                if k <= j or ((m1 | m2) & m3) or (m1 | m2 | m3) != full:
                    continue
                out.append((P1, P2, P3))
    return out, len(sat), len(parts)


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


def _wl_invariant(n, adj, W):
    """the 1-WL invariant of a WEIGHTED graph: the stable colour refinement's
    own multiset, taken as a canonical string.  It is computed by refinement
    alone and shares no code with the isomorphism SEARCH, so agreement between
    the two is agreement between two routes."""
    col = _refine(n, adj, W, _init_colour(n, adj, W))
    sig = sorted((col[v], tuple(sorted((col[u],
                                        W[(min(v, u), max(v, u))])
                                       for u in adj[v]))) for v in range(n))
    return json.dumps([n, sig], sort_keys=True, default=str)


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
    EMBEDDING  -- a bijection of the site objects onto the target's sites which
                  carries the realised relation ONTO the target's incidence:
                  an isomorphism, which is what the implementation tests and
                  what section 2.3 of the paper declares.
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


def chart_fibers(gl, links):
    """THE TWO CHART-BORNE FIBERS at one gluing -- `I-DIRECTION-LABEL` and
    `I-ORIENT` -- by the same route `detect` reads them, and without the
    automorphism machinery the SITE fiber needs.  These are the rows that are
    properties of the DRIVEN GLUING and not of its combinatorial type, and
    G-REPRESENTATIVE-ROWS measures the spread with this."""
    actors, rel, _am, _bm, _sh = combinatorial_rel(gl)
    tgt = amalgam_target(gl, links, "T", "SIMPLE")
    nodes = list(actors)
    n1, a1, w1, _i1 = make_graph(nodes, {e: 1 for e in rel}, False)
    tnodes = list(tgt["nodes"])
    n2, a2, w2, i2 = make_graph(tnodes, {e: 1 for e in tgt["inc"]}, False)
    phi0 = find_map(n1, a1, w1, n2, a2, w2, {})
    if phi0 is None:
        return None
    inv2 = {i: t for t, i in i2.items()}
    phis = {nodes[u]: inv2[x] for u, x in phi0.items()}
    labs = {fkey(target_field(tgt, rel, phis, {"A": pa, "B": pb}, NOFLIP))
            for pa in PERMS3 for pb in PERMS3}
    oris = {fkey(target_field(tgt, rel, phis, IDPERM, {"A": oa, "B": ob}))
            for oa in (False, True) for ob in (False, True)}
    return len(labs), len(oris)


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
    SEEDCARRY_CACHE.clear()


def full_run(break_anchor=None, paper_text=None, paper_rel=PAPER_REL,
             write=True, numbers_only=False, swept=False):
    reset_caches()
    READS.clear()
    LD = Ledger()
    SEAL = Seal()
    R = {}
    R["schema"] = SEAL.seal("schema", SCHEMA)
    R["pin"] = SEAL.seal("pin", {"path": "v14/note-sec-pin.md",
                                 "ledger": 258, "paper_number": 32})
    R["unit"] = SEAL.seal("unit", "SEC")
    R["paper"] = SEAL.seal("paper", paper_rel)

    # ---- SEC 1  PROVENANCE ------------------------------------------------
    # the OBJECT UNDER TEST is read FIRST and through the same accessor as
    # everything else, so the register the gates below consume is complete.
    if paper_text is not None:
        ptext = paper_text
    else:
        ptext = read_text_file(os.path.join(REPO, paper_rel),
                               "OBJECT-UNDER-TEST")
    if mut("MUT-STRAY-READ"):
        read_bytes("v14/PLAN.md")
    if mut("MUT-CITED-READ"):
        read_bytes(CITED_NOT_READ[0]["path"])
    texts = {}
    prov = []
    for (sid, rel, sha, why) in SOURCES:
        raw = read_bytes(rel)
        got = hashlib.sha256(raw).hexdigest()[:12]
        want = sha
        if break_anchor == sid or (mut("MUT-ANCHOR-DIGEST") and sid == "A-P19"):
            want = "0" * 12
        prov.append({"id": sid, "path": rel, "sha256_12": got,
                     "declared": want, "ok": got == want, "why": why})
        texts[rel] = raw.decode("utf-8")

    # THE CITED-AND-NOT-READ ABSTENTION, MEASURED AT THE ACCESSOR.  A source
    # this unit cites but must not read -- because a concurrent worker holds it
    # under rewrite and #91 forbids reading a live worktree state -- must be
    # absent from THE REGISTER OF READS ACTUALLY TAKEN, and every entry must
    # carry a reason.  The register is filled inside the I/O accessor, so a
    # read taken anywhere in this file is visible here: the abstention is an
    # observation and not a sentence about one.  It is taken BEFORE the
    # source gate so that a read of the cited file dies as the abstention it
    # violates rather than as a source-count mismatch.
    read_paths = [r["path"] for r in READS]
    cnr_bad = [c["id"] for c in CITED_NOT_READ
               if c["path"] in read_paths or not c.get("why")
               or c["path"] in [s[1] for s in SOURCES]]
    LD.gate("G-CITED-NOT-READ",
            not cnr_bad and len(CITED_NOT_READ) > 0,
            "every source this unit CITES BUT MUST NOT READ is absent from "
            "the register of reads this run actually took -- the register the "
            "I/O accessor fills, not a list the loop that reads the sources "
            "fills for itself -- and from the runtime source list, and carries "
            "a stated reason",
            {"cited_not_read": [c["id"] for c in CITED_NOT_READ],
             "violations": cnr_bad, "reads_taken": len(READS),
             "paths": sorted(set(read_paths))})
    R["cited_not_read"] = SEAL.seal("cited_not_read", CITED_NOT_READ)

    # THE READ REGISTER, category by category.  SOURCE must be exactly the 15
    # pinned paths, SELF exactly this file, OBJECT-UNDER-TEST exactly one file
    # (none in --numbers, which reads no paper), and no other category may
    # appear before the writer stages its artifacts.
    cats = {}
    for r0 in READS:
        cats.setdefault(r0["category"], []).append(r0["path"])
    declared_src = sorted(s[1] for s in SOURCES)
    src_ok = sorted(cats.get("SOURCE", [])) == declared_src
    obj_ok = len(cats.get("OBJECT-UNDER-TEST", [])) == (
        0 if paper_text is not None else 1)
    cat_ok = set(cats) <= {"SOURCE", "OBJECT-UNDER-TEST"}
    # R["paper"] names the object under test.  A published name nothing checks
    # is a name, so it is checked HERE against the register: the path the run
    # says it tested must be the path the accessor recorded it opening.  In
    # --numbers, where no paper is opened at all, the name must be absent from
    # the register rather than merely unread.
    paper_named_ok = (cats.get("OBJECT-UNDER-TEST", []) == [R["paper"]]
                      if paper_text is None
                      else R["paper"] not in cats.get("OBJECT-UNDER-TEST", []))
    if mut("MUT-PAPER-NAME"):
        paper_named_ok = not paper_named_ok
    LD.gate("G-SOURCES",
            all(p["ok"] for p in prov) and len(prov) == len(SOURCES)
            and src_ok and obj_ok and cat_ok and paper_named_ok,
            "every one of the %d declared sources is present and its sha256-12 "
            "equals the frozen declaration, and THE RUN'S OBSERVED READ SET -- "
            "recorded at the accessor every open in this file goes through -- "
            "is exactly the declared set, category by category: the SOURCE "
            "paths are the %d pinned ones, the object under test is a single "
            "file, and no other category occurs -- and the path this run "
            "PUBLISHES as the object under test is the path the accessor "
            "recorded it opening, so the name is checked and not merely "
            "written down" % (len(SOURCES), len(SOURCES)),
            {"n": len(prov), "bad": [p["id"] for p in prov if not p["ok"]],
             "reads": len(READS), "categories": sorted(cats),
             "sources_exactly_declared": src_ok,
             "published_paper_name_matches_the_register": paper_named_ok,
             "object_under_test": cats.get("OBJECT-UNDER-TEST", [])})
    R["provenance"] = SEAL.seal("provenance", prov)
    R["reads"] = SEAL.seal("reads", {"rows": list(READS),
                                     "by_category": {k: sorted(set(v))
                                                     for k, v in
                                                     sorted(cats.items())},
                                     "declared_categories":
                                     ["SOURCE", "OBJECT-UNDER-TEST", "SELF",
                                      "ARTIFACT"],
                                     "subprocesses_invoked": 0})

    def src(sid):
        return texts[dict((s[0], s[1]) for s in SOURCES)[sid]]

    # ---- the verbatim anchors, each naming its consumer gate --------------
    # THE QUOTE SIDE IS DECLARED PER ANCHOR.  An anchor that only checks the
    # SOURCE proves the sentence exists somewhere; it does not protect the
    # paper's rendering of it, and an inverted block quotation would survive.
    # Every anchor the paper quotes is marked `quoted` and G-PAPER-QUOTES
    # requires the SAME needle, under the same normaliser, in the object under
    # test.
    # The fifth field is the QUOTE-SIDE NEEDLE: the exact fragment the paper
    # renders inside its block quotation, or None where the paper does not
    # quote the anchor at all.  It must itself be a fragment of the SOURCE
    # needle -- so it is verbatim from the pinned parent and not a paraphrase
    # -- and G-PAPER-QUOTES requires it in the object under test.  V06's
    # fragment is shorter than its source needle because the paper's quotation
    # carries an editorial substitution for the parent's own subject; the
    # substitution sits OUTSIDE the fragment, and what remains is verbatim.
    VERBATIM = [
        ("V01", "A-PIN",
         "the k=0 disjoint union run as the it-can-fail arm", "G-STERILITY",
         None),
        ("V02", "A-PIN",
         "does a FORCED dictionary exist for the glued world", "G-DICT",
         None),
        ("V03", "A-P19",
         "1,296 site assignments carry the record's co-division incidence onto",
         "G-SECTOR-WELD",
         "1,296 site assignments carry the record's co-division incidence "
         "onto"),
        ("V04", "A-P21",
         "The theorem is that **zero free items holds exactly at the "
         "link-constant records, and I7 declares none of them.**",
         "G-FORCED-OVERLAP",
         "The theorem is that **zero free items holds exactly at the "
         "link-constant records, and I7 declares none of them.**"),
        ("V05", "A-PIN",
         "the bare-union and extended-carrier readings both run (the LOR "
         "lesson: the carrier may need pairs)", "G-DICT",
         "the bare-union and extended-carrier readings both run (the LOR "
         "lesson: the carrier may need pairs)"),
        ("V06", "A-R1",
         "A refinement family that answers the continuum question must "
         "**divide** a block, not copy one", "G-STERILITY",
         "must **divide** a block, not copy one"),
        ("V07", "A-HA",
         "nonsingular and positive definite at every site, by the exact "
         "Sylvester", "G-SEAM-RANK", None),
        ("V08", "A-CAT",
         "no Lorentz-invariant finite-valency graph", "G-WALL-SCAN",
         "no Lorentz-invariant finite-valency graph"),
    ]
    QUOTE_FLOOR = 30
    anch = []
    for (vid, sid, needle, gate, quote) in VERBATIM:
        nd = needle
        if mut("MUT-ANCHOR-TEXT") and vid == "V03":
            nd = needle.replace("1,296", "4,242")
        ok = match_needle(src(sid), nd) and len(canon(nd)) >= NEEDLE_FLOOR
        if quote is not None:
            ok = ok and canon(quote) in canon(nd) \
                and len(canon(quote)) >= QUOTE_FLOOR
        anch.append({"id": vid, "source": sid, "gate": gate,
                     "chars": len(canon(nd)), "ok": ok,
                     "quoted_in_the_paper": quote is not None,
                     "quote_chars": len(canon(quote)) if quote else 0,
                     "needle": nd, "quote": quote})
    LD.gate("G-ANCHORS",
            all(a["ok"] for a in anch),
            "every verbatim anchor is present in its pinned source under the "
            "#125 normaliser, clears the %d-character floor, and names the "
            "gate that consumes it -- a name CHECKED against this run's own "
            "ledger at G-ANCHOR-CONSUMERS, since the consumers run later than "
            "this gate does; and the %d anchors the paper quotes carry "
            "a QUOTE-SIDE fragment which is itself verbatim inside the source "
            "needle and clears a %d-character floor -- that fragment is "
            "required in the object under test at G-PAPER-QUOTES, so an "
            "inverted block quotation dies"
            % (NEEDLE_FLOOR, sum(1 for a in anch
                                 if a["quoted_in_the_paper"]), QUOTE_FLOOR),
            {"n": len(anch), "bad": [a["id"] for a in anch if not a["ok"]],
             "quoted": [a["id"] for a in anch if a["quoted_in_the_paper"]]})
    LAST_ANCHORS[0] = anch
    R["anchors"] = SEAL.seal("anchors",
                             [{k: v for k, v in a.items()
                               if k not in ("needle", "quote")}
                              for a in anch])

    # ---- SEC 2  EXACTNESS -------------------------------------------------
    selftext = read_text_file(SELF, "SELF")
    self_reads = [r["path"] for r in READS if r["category"] == "SELF"]
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
    # every `open` in this file must be the recorded accessor's own: an AST
    # scan finds the call sites, and the only one permitted is inside
    # `_open_recorded`.
    opens = []
    for n in ast.walk(tree):
        if isinstance(n, ast.FunctionDef):
            for c in ast.walk(n):
                if (isinstance(c, ast.Call) and isinstance(c.func, ast.Name)
                        and c.func.id == "open"):
                    opens.append(n.name)
    LD.gate("G-EXACT",
            not floats and not banned_calls and not subproc
            and sorted(set(opens)) == ["_open_recorded", "_write_staged"]
            and self_reads == [os.path.relpath(SELF, REPO)],
            "an AST scan of this file finds no float constant, no call to "
            "float() or eval(), and no import of any subprocess or network "
            "module: all arithmetic is Python ints and fractions.Fraction, "
            "and the run is correct off-tree and with no version control "
            "present.  The same scan finds every `open` call site, and there "
            "are exactly two: the recorded READ accessor, so the read register "
            "cannot be bypassed by a read this file takes somewhere else, and "
            "the staging WRITER, which writes beside a destination and never "
            "onto one",
            {"floats": len(floats), "banned_calls": len(banned_calls),
             "imports": imports, "subprocess_modules": subproc,
             "open_call_sites": sorted(set(opens)), "self_reads": self_reads})

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
    # THE FIBER BY EXHAUSTION, not by one witness.  Every admissible
    # arrangement of a sector is enumerated -- all partitions of the nine
    # sites into triples, the I7-STRICT saturating ones among them, and every
    # unordered triple of those covering each of the 27 cells exactly once --
    # and each is checked to realise the SAME arena.
    triples, nsat2, nparts = all_arrangement_triples()
    if mut("MUT-ARRANGEMENT-ALL"):
        triples = triples[:-1]
    arr_bad = []
    for T in triples:
        cT = Counter()
        for P in T:
            for g in P:
                for u, v in combinations(sorted(g), 2):
                    cT[frozenset((smap[u], smap[v]))] += 1
        relT = dict(cT)
        nT, aT, wT, _iT = make_graph(sorted(smap.values(), key=repr),
                                     {e: 1 for e in relT}, False)
        if (len(relT) != len(srel) or sorted(relT.values()) != [1] * len(relT)
                or find_map(n1, a1, w1, nT, aT, wT, {}) is None):
            arr_bad.append(str(T))
    LD.gate("G-ARRANGEMENT-FREE",
            (alt_iso and len(altrel) == len(srel)
             and sorted(altrel.values()) == sorted(srel.values())
             and altrec["refusal"] is None
             and not arr_bad and len(triples) * 6 == 72),
            "the sector's arrangement is a declared item with fiber 1, and the "
            "fiber is measured BY EXHAUSTION: a DRIVEN non-collinear I7-STRICT "
            "triple realises the same co-division arena at 27 pairs of count "
            "1, and every one of the %d unordered admissible arrangement "
            "triples -- %d ordered, found by search over the %d saturating "
            "partitions of the %d partitions into triples, never typed -- "
            "realises 27 pairs at count 1 on an arena isomorphic to the "
            "collinear one" % (len(triples), len(triples) * 6, nsat2, nparts),
            {"saturating_partitions": nsat, "pairs": len(altrel),
             "isomorphic": alt_iso, "refusal": altrec["refusal"],
             "unordered_triples": len(triples), "ordered_triples":
             len(triples) * 6, "partitions": nparts, "bad": arr_bad})
    R["arrangement_free"] = SEAL.seal(
        "arrangement_free", {"saturating_partitions": nsat,
                             "alt_pairs": len(altrel), "isomorphic": alt_iso,
                             "alt_events": altrec["events"],
                             "partitions_into_triples": nparts,
                             "unordered_arrangement_triples": len(triples),
                             "ordered_arrangement_triples": len(triples) * 6,
                             "all_realise_one_arena": not arr_bad})

    # ---- SEC 5  THE GLUING CENSUS -----------------------------------------
    census = []
    typerep = {}
    typemembers = {}
    typecount = Counter()
    total_gl = 0
    clean_by_k = Counter()
    carry_by_k = {"first": Counter(), "shared": Counter()}
    carry_by_type = {}
    for k in (0, 1, 2, 3):
        GL = all_gluings(k)
        if mut("MUT-TYPE-COUNT") and k == 3:
            GL = GL[:-1]
        total_gl += len(GL)
        for gl in GL:
            t = (k,) + gluing_type(gl)
            typecount[t] += 1
            typerep.setdefault(t, gl)
            typemembers.setdefault(t, []).append(gl)
            df = doubled_free(gl)
            if df:
                clean_by_k[k] += 1
            # THE SEED-CARRY PREDICATE, evaluated at every gluing of the
            # family and at both declared seed rules.  Nothing is published
            # from it until G-SEED-PREDICATE has compared it against the
            # DRIVEN fate at every driven record.
            row = carry_by_type.setdefault(t, {"first": 0, "shared": 0,
                                               "n": 0})
            row["n"] += 1
            for rule in ("first", "shared"):
                if seed_carry(gl, rule):
                    row[rule] += 1
                    carry_by_k[rule][k] += 1
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
            "from the closed form C(9,k) * 9!/(9-k)! -- a five-line route "
            "written beside its comparand and sharing no step with the "
            "enumeration, which is a weaker claim than 'no shared code' and "
            "the true one -- the type populations sum back to it, and every "
            "type's representative reproduces the type it indexes",
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
        if mut("MUT-AUT-ROUTE-UNION") and t[0] == 1:
            o_enum2 = (o_enum2 or 0) + 1
        fieldvals = sorted(set(rel.values()))
        degs, degu, degdef = union_degrees(actors, rel, shared)
        if mut("MUT-DEGREE") and t[0] == 2 and len(dbl) > 0:
            degs, degdef = [2 * degu[0]], 0
        census.append({
            "type": str(t), "k": k, "gluings": typecount[t],
            "carriers": n, "pairs": len(rel), "doubled": len(dbl),
            "aut": o1, "aut_weighted": o2, "aut_enum": o_enum2,
            "aut_components": o_comp,
            "fiber_site_A": fibA, "fiber_site_B": fibB,
            "field_values": fieldvals,
            "shared_degrees": degs, "unshared_degrees": degu,
            "shared_degree_deficit": degdef,
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
    # THE DEGREE LAW AT THE SEAM, measured type by type.  The site fiber's
    # mechanism is that the gluing destroys edge transitivity, and the reason
    # is a degree separation -- which is NOT `twice the degree`: a doubled pair
    # is one link of the union and costs its two shared endpoints one degree
    # apiece, so the shared degree is 12 only where no pair is doubled.
    degbad = [c["type"] for c in census
              if c["unshared_degrees"] != [6]
              or (c["k"] > 0 and (min(c["shared_degrees"]) <= 6
                                  or max(c["shared_degrees"]) > 12))
              or (c["k"] > 0 and c["doubled"] == 0
                  and c["shared_degrees"] != [12])
              # AND THE DOUBLED SIDE IS BOUND TOO, by an EXACT identity rather
              # than by a bound: the deficit of the shared actors' degrees
              # below 12, summed, is exactly twice the doubled count, because
              # a doubled pair is ONE link of the union and costs each of its
              # two shared endpoints one degree.  Without this leg the law's
              # own exception was unguarded and a forged 12 survived.
              or c["shared_degree_deficit"] != 2 * c["doubled"]]
    LD.gate("G-DEGREE",
            not degbad,
            "the seam is visible in the BARE structure at every type, and the "
            "separation is measured rather than stated as a law: every "
            "unshared actor has degree 6, every shared actor has degree "
            "strictly greater than 6 and at most 12, and the shared degree is "
            "12 exactly where no shared pair is doubled.  Where one is, the "
            "law is bound by an EXACT IDENTITY rather than by a bound: the "
            "shared actors' total deficit below 12 equals TWICE the doubled "
            "count at every type, because a pair realised in both sectors is "
            "still ONE link of the union and costs each of its two shared "
            "endpoints one degree.  So neither the doubled-free case nor its "
            "exception can be forged into the other",
            {"types": len(census), "bad": degbad,
             "shared_degrees": sorted({tuple(c["shared_degrees"])
                                       for c in census if c["k"] > 0}),
             "deficit_equals_twice_doubled":
             [[c["shared_degree_deficit"], 2 * c["doubled"]] for c in census],
             "unshared_degrees": sorted({tuple(c["unshared_degrees"])
                                         for c in census})})

    # THE UNION ARENA UP TO ISOMORPHISM.  The type is taken up to permutation
    # of each sector's parts but NOT up to the A<->B swap, so distinct types
    # can carry one arena.  Measured: the 16 representatives are compared
    # pairwise as WEIGHTED graphs.
    reps_graph = {}
    for t in sorted(typerep):
        ac_, rel_, _am, _bm, _sh = combinatorial_rel(typerep[t])
        reps_graph[t] = make_graph(ac_, rel_, True)
    arena_classes = []
    for t in sorted(typerep):
        n1_, a1_, w1_, _i_ = reps_graph[t]
        for cl in arena_classes:
            n2_, a2_, w2_, _j_ = reps_graph[cl[0]]
            if n1_ == n2_ and find_map(n1_, a1_, w1_, n2_, a2_, w2_,
                                       {}) is not None:
                cl.append(t)
                break
        else:
            arena_classes.append([t])
    if mut("MUT-ARENA-COUNT"):
        arena_classes = arena_classes + [arena_classes[0]]
    mirror = [[str(x) for x in cl] for cl in arena_classes if len(cl) > 1]
    mirror_rows = []
    for cl in arena_classes:
        if len(cl) == 2:
            mirror_rows.append({"type": str(cl[0]), "mirror": str(cl[1]),
                                "gluings": typecount[cl[0]],
                                "mirror_gluings": typecount[cl[1]],
                                "arena_fiber": typecount[cl[0]]
                                + typecount[cl[1]]})
    LD.gate("G-ARENA-COUNT",
            (len(arena_classes) < len(typerep) and all(len(cl) <= 2
                                                       for cl in arena_classes)
             and sum(len(cl) for cl in arena_classes) == len(typerep)),
            "the %d combinatorial types carry %d union arenas up to "
            "isomorphism of the WEIGHTED union: exactly %d pairs of types are "
            "exchanged by the A<->B swap, which the type does not quotient by, "
            "and each such pair carries one arena -- measured by an "
            "isomorphism search between the representatives, not read off the "
            "census's equal columns"
            % (len(typerep), len(arena_classes), len(mirror)),
            {"types": len(typerep), "arenas": len(arena_classes),
             "mirror_pairs": mirror})
    R["arena_classes"] = SEAL.seal(
        "arena_classes", {"types": len(typerep), "arenas": len(arena_classes),
                          "mirror_pairs": mirror_rows,
                          "classes": [[str(x) for x in cl]
                                      for cl in arena_classes]})

    # THE EXHAUSTIVENESS LICENCE, GATED.  Every 16-type column speaks about
    # 45,010 gluings only if the union arena is a function of the type.  That
    # is checked here against a DECLARED SAMPLE of each type's own members --
    # constructively, by exhibiting an isomorphism of the weighted union onto
    # the representative's, and by a Weisfeiler-Leman invariant computed
    # independently of the search -- rather than assumed by a cache-consistency
    # check on the representatives.
    SAMPLE_N = 12
    inv_rows = []
    inv_bad = []
    for t in sorted(typerep):
        sample = type_sample(typemembers[t], SAMPLE_N)
        wl = set()
        iso = 0
        for gl in sample:
            ac_, rel_, _am, _bm, _sh = combinatorial_rel(gl)
            n1_, a1_, w1_, _i_ = make_graph(ac_, rel_, True)
            if mut("MUT-TYPE-INVARIANT") and t[0] == 3 and gl is sample[-1]:
                w1_ = dict(w1_)
                w1_[sorted(w1_)[0]] = 7
            n2_, a2_, w2_, _j_ = reps_graph[t]
            if n1_ == n2_ and find_map(n1_, a1_, w1_, n2_, a2_, w2_,
                                       {}) is not None:
                iso += 1
            wl.add(_wl_invariant(n1_, a1_, w1_))
        row = {"type": str(t), "sampled": len(sample),
               "isomorphic_to_the_representative": iso,
               "wl_invariants": len(wl)}
        inv_rows.append(row)
        if iso != len(sample) or len(wl) != 1:
            inv_bad.append(str(t))
    LD.gate("G-TYPE-INVARIANT",
            not inv_bad,
            "the union arena IS a function of the combinatorial type, and it "
            "is measured on the type's own members rather than assumed: at "
            "every type a declared sample of up to %d of its gluings is "
            "compared against the type's representative, and every sampled "
            "member's WEIGHTED union is isomorphic to the representative's by "
            "an exhibited isomorphism, with a Weisfeiler-Leman invariant "
            "constant across the sample" % SAMPLE_N,
            {"types": len(inv_rows), "sample_cap": SAMPLE_N,
             "sampled": sum(r["sampled"] for r in inv_rows), "bad": inv_bad})
    R["type_invariance"] = SEAL.seal(
        "type_invariance", {"sample_cap": SAMPLE_N, "rows": inv_rows,
                            "sampled_total": sum(r["sampled"]
                                                 for r in inv_rows)})

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

    # THE SEED RULE IS THE DRIVER'S VARIABLE, AND IT IS PRICED.  The window
    # drives ONE representative per type, so what it measures at each rule is
    # the fate of THAT RECORD.  The refusals are recorded and never patched.
    if mut("MUT-SEED-FATE"):
        for w in window:
            if w["seed_rule"] == "shared":
                w["fate"] = "REFUSED"
                break
    refused_first = sorted({w["type"] for w in window
                            if w["seed_rule"] == "first"
                            and w["fate"] == "REFUSED"})
    refused_shared = sorted({w["type"] for w in window
                             if w["seed_rule"] == "shared"
                             and w["fate"] == "REFUSED"})
    LD.gate("G-SEED-RULE",
            not refused_shared and refused_first,
            "the seed rule is a genuine variable OF THE DRIVER and BOTH its "
            "values are driven: under paper-19's canonical rule the committed "
            "grammar REFUSES at %d of the 16 driven window records, under the "
            "shared-seed rule it refuses at none of them, and the refusals are "
            "recorded and never patched" % len(refused_first),
            {"records_refused_under_first": len(refused_first),
             "refused_under_first": refused_first,
             "refused_under_shared": refused_shared})

    # THE OFF-WINDOW VALIDATION SET, DRIVEN.  The window's representative is a
    # free choice of this unit's, so the fate it reports could be a property of
    # the CHOICE.  A declared second set of records is driven to measure that:
    # at every type whose LAST member the seed-carry predicate separates from
    # its representative, that last member is driven at BOTH rules.  The set is
    # named by a rule, not picked by hand, and both directions occur in it.
    offwin = []
    OFFWIN_CAP = 3
    off_types = [t for t in sorted(typerep)
                 if len(typemembers[t]) > 1
                 and seed_carry(typemembers[t][-1], "first")
                 != seed_carry(typerep[t], "first")][:OFFWIN_CAP]
    for t in off_types:
        gl = typemembers[t][-1]
        for rule in ("first", "shared"):
            actors, rounds, amap, bmap, shared = union_rounds(gl, rule)
            b = drive(G, actors, rounds)
            rec = record_of(G, b, actors)
            drel = codivision_rel(rec["footprints"])
            _a, crel, _am, _bm, _sh = combinatorial_rel(gl)
            forced = rec["refusal"] is None
            offwin.append({"type": str(t), "member": "LAST",
                           "seed_rule": rule,
                           "fate": "FORCED" if forced else "REFUSED",
                           "representative_fate":
                           [w["fate"] for w in window
                            if w["type"] == str(t)
                            and w["seed_rule"] == rule][0],
                           "events": rec["events"],
                           "divisions": rec["divisions"],
                           "predicted": ("FORCED" if seed_carry(gl, rule)
                                         else "REFUSED"),
                           "driven_equals_combinatorial":
                           (forced and drel == crel) if forced else None})
    if mut("MUT-SEED-PREDICATE") and offwin:
        offwin[0]["predicted"] = ("REFUSED"
                                  if offwin[0]["predicted"] == "FORCED"
                                  else "FORCED")
    # THE PREDICATE, VALIDATED AT EVERY DRIVEN RECORD.  Only after this may the
    # family-wide census it predicts be published, and it is published as a
    # PREDICTION and not as a drive.
    predbad = []
    for w in window:
        t = [t2 for t2 in typerep if str(t2) == w["type"]][0]
        want = "FORCED" if seed_carry(typerep[t], w["seed_rule"]) else "REFUSED"
        if want != w["fate"]:
            predbad.append("WINDOW/" + w["type"] + "/" + w["seed_rule"])
    for o in offwin:
        if o["predicted"] != o["fate"]:
            predbad.append("OFF/" + o["type"] + "/" + o["seed_rule"])
    off_eqbad = [o["type"] + "/" + o["seed_rule"] for o in offwin
                 if o["fate"] == "FORCED"
                 and not o["driven_equals_combinatorial"]]
    LD.gate("G-SEED-PREDICATE",
            not predbad and not off_eqbad and len(offwin) >= 2
            and len({o["fate"] for o in offwin}) == 2,
            "THE SEED-CARRY PREDICATE IS VALIDATED BEFORE IT IS USED.  It is a "
            "property of the SCHEDULE -- in the second sector's first round, "
            "is every group holding a shared actor seeded by a shared actor -- "
            "and not a re-implementation of the layer's menu; it is compared "
            "against the DRIVEN fate at every one of the %d window records and "
            "at every one of the %d off-window records driven here, both fates "
            "occurring among them, and the driven relation equals the "
            "combinatorial one at every FORCED off-window record"
            % (len(window), len(offwin)),
            {"window_records": len(window), "off_window_records": len(offwin),
             "off_window_types": [str(t) for t in off_types],
             "disagreements": predbad,
             "off_window_equality_failures": off_eqbad})
    R["off_window"] = SEAL.seal("off_window", offwin)

    # the family-wide census the validated predicate supports, stamped
    carry_rows = []
    for t in sorted(typerep):
        row = carry_by_type[t]
        carry_rows.append({"type": str(t), "gluings": row["n"],
                           "carrying_under_first": row["first"],
                           "carrying_under_shared": row["shared"],
                           "representative_carries_under_first":
                           seed_carry(typerep[t], "first"),
                           "first_rule_fate_splits_the_type":
                           0 < row["first"] < row["n"]})
    if mut("MUT-SEED-CENSUS"):
        carry_rows[3]["carrying_under_shared"] -= 1
    split = [r["type"] for r in carry_rows
             if r["first_rule_fate_splits_the_type"]]
    carry_first = sum(r["carrying_under_first"] for r in carry_rows)
    carry_shared = sum(r["carrying_under_shared"] for r in carry_rows)
    LD.gate("G-SEED-CENSUS",
            (carry_shared == total_gl and carry_first < total_gl
             and all(r["carrying_under_shared"] == r["gluings"]
                     for r in carry_rows)),
            "the validated predicate is evaluated at EVERY gluing of the "
            "family and at both rules: under the shared-seed rule every one of "
            "the %d gluings carries the base into the second sector, under "
            "paper-19's canonical rule %d of them do, and the canonical-rule "
            "prediction SPLITS %d of the %d types -- so the canonical-rule "
            "fate is a property of the driven gluing and not of its type, "
            "while the shared-rule fate is a property of the rule"
            % (total_gl, carry_first, len(split), len(typerep)),
            {"gluings": total_gl, "carrying_under_first": carry_first,
             "carrying_under_shared": carry_shared,
             "types_split_under_first": len(split)})
    R["seed_rule"] = SEAL.seal(
        "seed_rule", {"refused_under_first": refused_first,
                      "refused_under_shared": refused_shared,
                      "n_types": len(typerep),
                      "predicate": "the second sector's first round seeds "
                                   "every group holding a shared actor ON a "
                                   "shared actor",
                      "validated_at_driven_records": len(window) + len(offwin),
                      "rows": carry_rows,
                      "types_split_under_first": len(split),
                      "carrying_under_first": carry_first,
                      "carrying_under_shared": carry_shared,
                      "carrying_by_k": {rule: {str(k): carry_by_k[rule][k]
                                               for k in (0, 1, 2, 3)}
                                        for rule in ("first", "shared")}})

    # ---- SEC 7  STAGE 2: THE UNION'S DICTIONARY ---------------------------
    # THE THREE DECLARED (carrier, link-individuation) COMBINATIONS.  The
    # extended carriers weld against the target's SUBDIVISION, and which
    # subdivision depends on how the target individuates its links -- which is
    # exactly the declaration the record cannot make for itself.
    COMBOS = (("BARE", "SIMPLE"), ("EXT-PAIR", "SIMPLE"),
              ("EXT-INCIDENCE", "CHARTED"))
    SITE_OBJECTS = {"BARE": "ACTOR",
                    "EXT-PAIR": "ACTOR + CO-DIVISION PAIR",
                    "EXT-INCIDENCE": "ACTOR + CO-DIVISION INCIDENCE"}
    TARGET_OF = {"BARE": "the amalgam, SIMPLE",
                 "EXT-PAIR": "the amalgam's subdivision, SIMPLE",
                 "EXT-INCIDENCE": "the amalgam's subdivision, CHARTED"}
    R["carrier_axis"] = SEAL.seal(
        "carrier_axis", [{"carrier": ck, "individuation": ind,
                          "site_objects": SITE_OBJECTS[ck],
                          "target": TARGET_OF[ck]} for (ck, ind) in COMBOS])
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

    # THE FATE / FREE-ITEM / FIBER SUMMARY, grouped by the MEASURED inventory
    # rather than by a two-row story.  The delivered object published one
    # UNMOTIVATED row carrying one free item; the inventory has two at five of
    # the six doubled types, so the summary is grouped by the inventory triple
    # it actually measures and every group is a rendered claim.
    fgroups = {}
    for r0 in [x for x in dict_rows if x["carrier"] == "BARE"
               and x["reading"] == "EMBEDDING"]:
        iv = r0["inventory"]
        key = (r0["fate"], tuple(r0["free_items"]), iv["I-SITE-ASSIGNMENT"],
               iv["I-DIRECTION-LABEL"], iv["I-ORIENT"])
        fgroups.setdefault(key, []).append(r0["type"])
    fate_summary = []
    for i0, (key, ts) in enumerate(sorted(fgroups.items(),
                                          key=lambda kv: (-len(kv[1]),
                                                          str(kv[0])))):
        fate_summary.append({"id": "%02d" % (i0 + 1), "fate": key[0],
                             "types": len(ts), "of": len(typerep),
                             "free_items": ", ".join(key[1]) or "none",
                             "site": key[2], "label": key[3],
                             "orient": key[4], "members": ts})
    R["fate_summary"] = SEAL.seal("fate_summary", fate_summary)

    # THE INDUCED COUNT FIELD IS CARRIER-INDEPENDENT, MEASURED.  A count is a
    # number of division events on an ACTOR PAIR; no carrier extension changes
    # what the record counts.  So no extended carrier can repair a free item
    # that a non-constant count field carries -- and the row that would show
    # otherwise is measured here rather than argued.
    cf_bad = []
    for reading in ("EMBEDDING", "QUOTIENT"):
        for t in sorted(typerep):
            rows_t = [r for r in dict_rows if r["type"] == str(t)
                      and r["reading"] == reading]
            fv = {r["carrier"]: tuple(r.get("field_values", ()))
                  for r in rows_t}
            cc = {r["carrier"]: r.get("count_cells") for r in rows_t}
            if mut("MUT-CARRIER-FIELD") and t[0] == 3 \
                    and reading == "EMBEDDING":
                fv["EXT-INCIDENCE"] = (1,)
            if len(set(fv.values())) != 1 or len(set(cc.values())) != 1:
                cf_bad.append(str(t) + "/" + reading)
    ext_stamped = [r["type"] + "/" + r["carrier"] for r in dict_rows
                   if r["carrier"] != "BARE"
                   and (r.get("inventory") != "READ-AT-BARE"
                        or r.get("scope") != "STRUCTURE-AND-COUNT-ONLY")]
    LD.gate("G-CARRIER-FIELD",
            not cf_bad and not ext_stamped,
            "the dictionary's induced count field is read from the ACTOR PAIR "
            "and is therefore the SAME at all three carriers: at every type "
            "and both readings the three carriers' field values and cell "
            "counts are identical, and every extended-carrier row carries the "
            "READ-AT-BARE inventory stamp and the STRUCTURE-AND-COUNT-ONLY "
            "scope -- so no repair of a free item is measured at an extended "
            "carrier anywhere in this run",
            {"types": len(typerep), "mismatches": cf_bad,
             "unstamped_extended_rows": ext_stamped,
             "field_values_by_carrier":
             sorted({r["carrier"] + ":" + str(r.get("field_values"))
                     for r in dict_rows})})

    # STRUCT-ALIVE IS INHERITED, and the census says from where.  Under SIMPLE
    # individuation the amalgam's incidence set IS the union's realised pair
    # set at every type -- necessarily, since each sector's realised relation
    # is I7's own link incidence and the union and the amalgam are formed by
    # the same identification.  The structural test cannot fail on this family,
    # and the row is stamped with the identity rather than reported as news.
    sid_bad = []
    for t in sorted(typerep):
        gl = typerep[t]
        actors, rel, amap, bmap, shared = combinatorial_rel(gl)
        tgt = amalgam_target(gl, LINKS, "T", "SIMPLE")
        real = {frozenset(e) for e in rel}
        got = {frozenset(e) for e in tgt["inc"]}
        namemap = {}
        for x in SITES:
            namemap[amap[x]] = tgt["charts"]["A"][x]
            namemap[bmap[x]] = tgt["charts"]["B"][x]
        carried = {frozenset(namemap[u] for u in e) for e in real}
        if mut("MUT-STRUCT-INHERIT") and t[0] == 3:
            carried = set(list(carried)[1:])
        if carried != got:
            sid_bad.append(str(t))
    LD.gate("G-STRUCT-INHERITED",
            not sid_bad,
            "the union's realised pair set IS the amalgam's incidence set at "
            "every one of the %d types, under the naming the gluing declares "
            "and SIMPLE individuation -- so STRUCT-ALIVE at 16 of 16 is "
            "inherited from the single sector's own identity rather than new "
            "information at the union, and the detector's structural leg is "
            "not vacuous only because the declared dead arms exercise it"
            % len(typerep),
            {"types": len(typerep), "mismatches": sid_bad})

    # ---- WHICH PUBLISHED ROWS ARE ROWS OF THE TYPE, AND WHICH OF THE ------
    # ---- REPRESENTATIVE.  Two gluings of one type are related by an
    # element of Aut(K3,3,3) x Aut(K3,3,3), which is NOT the affine group: it
    # carries a collinear transversal to a non-collinear one.  So the ABSTRACT
    # weighted arena is a type invariant (G-TYPE-INVARIANT), while everything
    # read against the target's CHART is finer than the type.  Measured on the
    # same declared sample, so the paper can stamp every row.
    def seam_profile_of(gl):
        """the row section 6.1 publishes at a type's representative: the
        multiset of (n_A, n_B) count vectors over the gluing's own shared
        sites.  Read from the combinatorial union, exactly as the seam census
        reads it, so the spread measured here is a spread of the SAME row."""
        _a, rel_, amap_, bmap_, _s = combinatorial_rel(gl)
        prof = []
        for (sa, sb) in gl:
            nA = tuple(rel_.get(frozenset((amap_[sa], amap_[zadd(sa, l)])), 0)
                       for l in LINKS)
            nB = tuple(rel_.get(frozenset((bmap_[sb], bmap_[zadd(sb, l)])), 0)
                       for l in LINKS)
            prof.append((nA, nB))
        return tuple(sorted(prof))

    spread_rows = []
    for t in sorted(typerep):
        sample = type_sample(typemembers[t], SAMPLE_N)
        pairs = set()
        profiles = set()
        for gl in sample:
            cf = chart_fibers(gl, LINKS)
            if cf is not None:
                pairs.add(cf)
            profiles.add(seam_profile_of(gl))
        rep_pair = None
        rrow = [r for r in dict_rows if r["type"] == str(t)
                and r["carrier"] == "BARE" and r["reading"] == "EMBEDDING"][0]
        if isinstance(rrow.get("inventory"), dict):
            rep_pair = (rrow["inventory"]["I-DIRECTION-LABEL"],
                        rrow["inventory"]["I-ORIENT"])
        spread_rows.append({
            "type": str(t), "sampled": len(sample),
            "representative_label_orient": list(rep_pair) if rep_pair else None,
            "distinct_label_orient_pairs_in_the_sample": len(pairs),
            "label_orient_pairs": sorted([list(p) for p in pairs]),
            "constant_on_the_sample": len(pairs) == 1,
            "distinct_seam_profiles_in_the_sample": len(profiles),
            "seam_profile_constant_on_the_sample": len(profiles) == 1})
    if mut("MUT-REP-SPREAD"):
        for r in spread_rows:
            r["distinct_label_orient_pairs_in_the_sample"] = 1
            r["constant_on_the_sample"] = True
    if mut("MUT-SEAM-PROFILE-SPREAD"):
        for r in spread_rows:
            r["distinct_seam_profiles_in_the_sample"] = 1
            r["seam_profile_constant_on_the_sample"] = True
    moved = [r["type"] for r in spread_rows if not r["constant_on_the_sample"]]
    seam_moved = [r["type"] for r in spread_rows
                  if not r["seam_profile_constant_on_the_sample"]]
    consistent = all(
        (r["representative_label_orient"] in r["label_orient_pairs"])
        for r in spread_rows if r["representative_label_orient"])
    LD.gate("G-REPRESENTATIVE-ROWS",
            consistent and len(moved) > 0 and len(seam_moved) > 0,
            "the chart-borne rows are rows of the DRIVEN GLUING and not of its "
            "type, and the split is measured for BOTH of them: on a declared "
            "sample of up to %d members per type the (I-DIRECTION-LABEL, "
            "I-ORIENT) pair takes more than one value at %d of the %d types, "
            "and THE PER-SITE SEAM PROFILE -- the (n_A, n_B) row section 6.1 "
            "publishes -- takes more than one value at %d of the %d types, so "
            "neither is asserted to be representative on the strength of prose "
            "-- while the abstract arena, the doubled count and therefore the "
            "FOUND/UNMOTIVATED fate are constant on the type by "
            "G-TYPE-INVARIANT.  Every published row is stamped on the side "
            "this gate puts it"
            % (SAMPLE_N, len(moved), len(typerep), len(seam_moved),
               len(typerep)),
            {"types": len(spread_rows), "sample_cap": SAMPLE_N,
             "types_where_the_pair_moves": moved,
             "types_where_the_seam_profile_moves": seam_moved,
             "representative_in_the_sample_values": consistent})
    R["representative_rows"] = SEAL.seal(
        "representative_rows", {"sample_cap": SAMPLE_N, "rows": spread_rows,
                                "types_where_the_pair_moves": len(moved),
                                "types_where_the_seam_profile_moves":
                                len(seam_moved)})

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
    if mut("MUT-DEAD-FATE"):
        dead[4] = dict(dead[4])
        dead[4]["fate"] = "STRUCT-DEAD"
    fates = [d["fate"] for d in dead]
    # the falsifier's own shape, published rather than left to be imagined:
    # withholding the first arbitration stops the drive where it stops.
    stump = {"events": recf["events"], "divisions": recf["divisions"],
             "realised_pairs": len(relf),
             "refusal": recf["refusal"] is not None}
    LD.gate("G-CONTROLS",
            (fates == ["ARITY-DEAD", "ARITY-DEAD", "STRUCT-DEAD",
                       "STRUCT-DEAD", "COUNT-DEAD"]
             and stump["refusal"]),
            "HA requirement 3 is discharged two-way: every value this detector "
            "can return is exhibited in this run, and each declared dead arm "
            "dies at the cause declared for it -- bound to the EXACT fate "
            "string of every arm, so the two readings' published signature "
            "(STRUCT-DEAD under EMBEDDING, COUNT-DEAD under QUOTIENT) cannot "
            "be swapped; and the falsifier's own shape is published with it",
            {"fates": fates, "falsifier_stump": stump})
    R["dead_arms"] = SEAL.seal("dead_arms", dead)
    R["falsifier_stump"] = SEAL.seal("falsifier_stump", stump)

    # ---- SEC 8  STAGE 3: THE GLUING FIBER ---------------------------------
    # THE TEST IS DECLARED (AID section 6.2).  A cell is named by its ACTOR
    # PAIR, at the naming the gluing declares, and the union's count on it is
    # compared against the count the owning sector carries on the same pair.
    # That is the FIXED-ATTRIBUTION reading, and it is the only reading under
    # which the comparison is posed at all: under the TRANSPORTED reading
    # nothing carries the union's cells to a sector's, because the two objects
    # have different automorphism groups and no relabelling between them is
    # declared.  The sector's own count is READ FROM THE DRIVEN SECTOR, never
    # typed.
    compat = []
    for t in sorted(typerep):
        gl = typerep[t]
        actors, rel, amap, bmap, shared = combinatorial_rel(gl)
        rows_moved = 0
        cells = 0
        both_shared = 0
        for i, (sa, sb) in enumerate(gl):
            for (chart, site, mp) in (("A", sa, amap), ("B", sb, bmap)):
                for l in LINKS:
                    cells += 1
                    y = zadd(site, l)
                    own = sfield[(site, l)]
                    got = rel.get(frozenset((mp[site], mp[y])), 0)
                    if got != own:
                        rows_moved += 1
                        if mp[site] in shared and mp[y] in shared:
                            both_shared += 1
        # THE CONFINEMENT, measured over the WHOLE union arena and not only
        # over the census's shared cells: how many pairs carrying a count
        # other than 1 touch an UNSHARED actor.
        touching = sum(1 for e, c in rel.items()
                       if c != 1 and any(u not in shared for u in e))
        compat.append({"type": str(t), "k": t[0], "shared_cells": cells,
                       "cells_where_union_differs_from_sector": rows_moved,
                       "differing_cells_with_both_endpoints_shared":
                       both_shared,
                       "pairs_off_count_1_touching_an_unshared_actor":
                       touching,
                       "reading": "FIXED-ATTRIBUTION",
                       "compatible": rows_moved == 0})
    if mut("MUT-COMPAT"):
        compat[-1]["compatible"] = not compat[-1]["compatible"]
    if mut("MUT-SEAM-CONFINED"):
        compat[-1]["pairs_off_count_1_touching_an_unshared_actor"] = 1
    badcompat = [c["type"] for c in compat
                 if c["compatible"] != (c["cells_where_union_differs_from_"
                                          "sector"] == 0)]
    LD.gate("G-GLUING-FIBER",
            not badcompat,
            "the shared actors' link-count compatibility is measured CELL BY "
            "CELL at the FIXED ATTRIBUTION (AID 6.2), the reading that names a "
            "cell by its actor pair: for every shared actor and every one of "
            "its links, the union's count is compared against the count that "
            "actor's own sector carries -- read from THIS RUN's driven sector "
            "field, not typed -- and the compatibility flag is that comparison "
            "rather than a summary of it",
            {"types": len(compat), "inconsistent_flags": badcompat,
             "sector_field_read_from": "G-SECTOR's own 27 cells"})
    conf_bad = [c["type"] for c in compat
                if c["differing_cells_with_both_endpoints_shared"]
                != c["cells_where_union_differs_from_sector"]
                or c["pairs_off_count_1_touching_an_unshared_actor"] != 0]
    LD.gate("G-SEAM-CONFINED",
            not conf_bad,
            "THE DEFORMATION IS CONFINED TO THE SEAM, and the confinement is "
            "the measurement rather than a reading of it: at every one of the "
            "%d types EVERY cell at which the union's count differs from the "
            "owning sector's has BOTH its endpoints shared, and -- measured "
            "over the whole union arena and not only over the census's shared "
            "cells -- NO pair carrying a count other than 1 touches an "
            "unshared actor.  The union's geometry is the sectors' everywhere "
            "except on the links the two sectors hold in common, and there it "
            "is the sum of theirs; no sector-private link moves, at the fixed "
            "attribution or at any other reading" % len(compat),
            {"types": len(compat), "bad": conf_bad,
             "reading": "FIXED-ATTRIBUTION",
             "differing_cells": [c["cells_where_union_differs_from_sector"]
                                 for c in compat],
             "of_those_with_both_endpoints_shared":
             [c["differing_cells_with_both_endpoints_shared"]
              for c in compat],
             "pairs_off_count_1_touching_an_unshared_actor":
             sum(c["pairs_off_count_1_touching_an_unshared_actor"]
                 for c in compat)})
    R["gluing_fiber"] = SEAL.seal(
        "gluing_fiber", {"compatibility": compat,
                         "gluings_per_type": {c["type"]: c2["gluings"]
                                              for c, c2 in zip(compat, census)},
                         "types": len(typerep),
                         "reading": "FIXED-ATTRIBUTION",
                         "transported_reading":
                         "not posed: no relabelling carrying the union's cells "
                         "to a sector's is declared, and the two objects do "
                         "not share an automorphism group",
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
                     "chart_dim": sysm["d"], "declared_links": len(LINKS),
                     "unknowns": sysm["unknowns"], "equations": 6,
                     "rank": rank, "kernel_dim": sysm["kernel_dim"],
                     "direct_sum_minors": [str(m) for m in mins],
                     "direct_sum_posdef": all(m > 0 for m in mins),
                     "indefinite_witness": wit,
                     "witness_reproduces_counts": repro})
    LD.gate("G-SEAM-RANK",
            all(s["rank"] == 6 and s["kernel_dim"] == 4 for s in seam),
            "AT EACH OF THE THREE DECLARED SEAM OBJECTS the count field is an "
            "exact linear system on the ten entries of Sym^2(Q^4): the six "
            "declared links give six independent equations, so the DIRECT-SUM "
            "chart leaves the seam's cross block -- four entries -- "
            "undetermined by the record.  These are three objects and they buy "
            "no quantifier; the universal over every shared site of every type "
            "is earned separately, and twice, at G-SEAM-ALL-SITES",
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

    # THE UNIVERSAL, MEASURED AT EVERY SHARED SITE AND PROVED ON THE ROW SPACE.
    # The head says "AT EVERY SHARED SITE"; three witnesses do not buy that
    # quantifier.  Two legs do.  (i) THE ROW SPACE IS THE RIGHT-HAND SIDE'S
    # INDEPENDENT: the six rows are the quadratic rows of a1, a2, a1+a2, b1,
    # b2, b1+b2 and do not mention a count, so their rank is a property of the
    # six declared directions -- computed here on the coefficient matrix alone
    # and re-computed against a declared spread of right-hand sides.  (ii) THE
    # CENSUS: the system is solved at EVERY shared site of EVERY one of the 16
    # type representatives, and the undetermined-entry total the head publishes
    # is that census's own sum rather than a typed product.
    coeff_rows = seam_system(LINKS, (1, 1, 1), (1, 1, 1), [])["rows"]
    coeff_rank = len(rref(coeff_rows, 10)[1])
    rhs_spread = []
    for rhs in ((1, 1, 1), (1, 2, 1), (2, 1, 2), (1, 1, 2), (3, 1, 1)):
        s_ = seam_system(LINKS, rhs, rhs, [])
        rhs_spread.append([s_["rank"], s_["kernel_dim"]])
    all_sites = []
    for t in sorted(typerep):
        gl = typerep[t]
        _ac, rel_, amap_, bmap_, _sh = combinatorial_rel(gl)
        ks = []
        for (sa, sb) in gl:
            nA_ = tuple(rel_.get(frozenset((amap_[sa], amap_[zadd(sa, l)])), 0)
                        for l in LINKS)
            nB_ = tuple(rel_.get(frozenset((bmap_[sb], bmap_[zadd(sb, l)])), 0)
                        for l in LINKS)
            s_ = seam_system(LINKS, nA_, nB_, [])
            ks.append([s_["rank"], s_["kernel_dim"]])
        if mut("MUT-SEAM-SITES") and ks:
            ks[0] = [7, 3]
        all_sites.append({"type": str(t), "shared_sites": len(ks),
                          "rank_kernel": ks,
                          "undetermined_entries": sum(x[1] for x in ks)})
    n_sites = sum(a["shared_sites"] for a in all_sites)
    bad_sites = [a["type"] for a in all_sites
                 if any(rk != [6, 4] for rk in a["rank_kernel"])]
    aligned_entries = [a["undetermined_entries"] for a in all_sites
                       if a["type"] == str(t3clean)][0]
    LD.gate("G-SEAM-ALL-SITES",
            (not bad_sites and coeff_rank == 6
             and all(rk == [6, 4] for rk in rhs_spread) and n_sites > len(seam)
             and aligned_entries == 4 * len(gl_clean)),
            "the universal is earned twice.  THE ROW SPACE: the six rows are "
            "the quadratic rows of the six declared directions and mention no "
            "count, so the coefficient matrix alone has rank %d on the ten "
            "entries whatever the right-hand side -- computed here on the "
            "coefficients and re-computed at %d declared count vectors, all "
            "returning rank 6 and kernel 4.  THE CENSUS: the system is solved "
            "at EVERY ONE of the %d shared sites of the %d type "
            "representatives, and rank 6 / kernel 4 holds at every one of "
            "them; the aligned k = 3 seam's %d undetermined entries are that "
            "census's own per-site sum and not a typed product"
            % (coeff_rank, len(rhs_spread), n_sites, len(typerep),
               aligned_entries),
            {"shared_sites": n_sites, "types": len(all_sites),
             "coefficient_rank": coeff_rank, "rhs_spread": rhs_spread,
             "bad": bad_sites,
             "aligned_undetermined_entries": aligned_entries})
    R["seam_all_sites"] = SEAL.seal(
        "seam_all_sites", {"rows": all_sites, "shared_sites": n_sites,
                           "coefficient_rank": coeff_rank,
                           "right_hand_sides_checked": len(rhs_spread),
                           "aligned_undetermined_entries": aligned_entries,
                           "cross_site_consistency":
                           "one system per site; no cross-site consistency "
                           "condition is imposed or measured"})
    # (b) what a cross-sector link would buy
    cross_gain = []
    for ncross in (0, 1, 2, 3, 4):
        cr = [(i // 2, i % 2, 3) for i in range(ncross)]
        sysm = seam_system(LINKS, (1, 1, 1), (1, 1, 1), cr)
        cross_gain.append({"cross_links": ncross, "rank": sysm["rank"],
                           "kernel_dim": sysm["kernel_dim"]})
    if mut("MUT-CROSS-ALGEBRA"):
        cross_gain[2]["kernel_dim"] = 3
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
            not obad and bool(set(ks_with_weld) & set(ks_without)),
            "the union welds at the bare carrier EXACTLY at the doubled-free "
            "gluings, checked type by type against each type's own realised "
            "relation; and the k-claim is bound by this predicate and not "
            "left in its prose -- the set of k carrying a welding type and the "
            "set carrying a non-welding type MEET, so no value of k decides "
            "the fate and the criterion cannot be the cardinality",
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
            "and nothing else.  This is a fresh sterility measurement at THIS "
            "arena and it is CONSISTENT WITH R1's copying lesson; it is NOT an "
            "instance of R1's Theorem B, whose hypothesis this arena does not "
            "instantiate and whose conclusions concern quantities ADDITIVE "
            "over components, while |Aut| is multiplicative and "
            "|Aut(C + C)| = |Aut(C)|^2 x 2 is a wreath-product fact "
            "independent of R1",
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
            # MEASURED at G-SEAM-ALL-SITES: the per-site kernel dimensions of
            # the aligned representative's own shared sites, summed.  Never a
            # typed product of a kernel and a site count.
            "seam_undetermined_entries": aligned_entries,
        },
        "k3_triangle_new_structure": {
            "doubled_pairs": [c["doubled"] for c in census
                              if c["type"] == str(t3tri)][0],
            "field_values": [c["field_values"] for c in census
                             if c["type"] == str(t3tri)][0],
        },
    }
    if mut("MUT-CONTRAST"):
        contrast["k3_triangle_new_structure"]["field_values"] = [1]
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
    # THE PROVENANCE SURFACE IS EXCLUDED AND NAMED, both on the key side and
    # on the gate side.  It carries other units' FILE NAMES -- and a file name
    # such as paper-01's is a citation of another unit's title, not a reading
    # taken here.  The excluded surface is exactly: the provenance block, the
    # read register, and the three gates whose evidence IS that surface.
    # Nothing else is excluded anywhere, in this scan or in the total one.
    CITATION_KEYS = ("provenance", "reads")
    CITATION_GATES = ("G-SOURCES", "G-CITED-NOT-READ", "G-ANCHORS")
    measurement_layer = json.dumps(
        {k: v for k, v in R.items() if k not in CITATION_KEYS},
        default=str) + json.dumps(
        [{"gate": r["gate"], "statement": r["statement"],
          "evidence": r["evidence"]} for r in LD.rows
         if not r["gate"].startswith("G-WALL")
         and r["gate"] not in CITATION_GATES], default=str)
    if mut("MUT-WALL-SCAN"):
        # THE DISEASE, NOT THE FINDING.  The delivered mutant appended a
        # barred string to the SERIALISED layer after it was built, which
        # tests the scanner against a string the receipt never carried.  It
        # now writes the barred reading INTO a published receipt key, the way
        # a reading actually taken would have got there, and the layer picks
        # it up because the layer is built from that key.
        R["seam_all_sites"]["cross_site_consistency"] += (
            "; read as a sprinkling of boost-invariant horizon data")
        measurement_layer = json.dumps(
            {k: v for k, v in R.items() if k not in CITATION_KEYS},
            default=str) + json.dumps(
            [{"gate": r["gate"], "statement": r["statement"],
              "evidence": r["evidence"]} for r in LD.rows
             if not r["gate"].startswith("G-WALL")
             and r["gate"] not in CITATION_GATES], default=str)
    # the object under test was read ONCE, at the top of this run and through
    # the recorded accessor; it is not re-opened here, so the register stays
    # exactly one OBJECT-UNDER-TEST read long
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
    barred = list(BARRED_TERMS)
    hits = sorted({w for w in barred if w in scan})
    phits = sorted({w for w in barred if w in pscan})
    LD.gate("G-WALL-SCAN",
            not hits and not phits,
            "the three abstention walls are MEASURED rather than declared, and "
            "BOTH surfaces are scanned: this run's measurement layer AS IT "
            "STANDS AT THIS GATE'S OWN POSITION -- every receipt key already "
            "published together with the statement and evidence of every "
            "non-wall gate already evaluated, which is not yet the whole "
            "payload and does not claim to be, the remainder being scanned at "
            "G-WALL-TOTAL by the writer -- AND the paper under "
            "test, for the terms whose presence would mean the reading was "
            "taken; none occurs in either.  The PROVENANCE SURFACE is excluded "
            "by name on both sides -- the keys %s and the gates %s -- because "
            "it carries other units' file names, which are citations of their "
            "titles and not readings taken here"
            % (", ".join(CITATION_KEYS), ", ".join(CITATION_GATES)),
            {"terms": len(barred), "receipt_hits": hits, "paper_hits": phits,
             "excluded_keys": list(CITATION_KEYS),
             "excluded_gates": list(CITATION_GATES)})
    R["walls"] = SEAL.seal("walls", {"l1_absent": True, "naming_present": True,
                                     "scanned_terms": barred,
                                     "receipt_hits": hits, "paper_hits": phits,
                                     "citation_keys_excluded":
                                     list(CITATION_KEYS),
                                     "citation_gates_excluded":
                                     list(CITATION_GATES)})

    # ---- SEC 13  THE VERDICT ----------------------------------------------
    cnt_clean = sum(o["gluings"] for o in overlap if o["welds"])

    # THE OVERLAP COMPARATOR.  Segment 4's outcome word is NOT typed into a
    # format string.  It is TYPED BY A COMPARATOR that states the two rival
    # hypotheses itself -- k selects, or the alignment does -- and decides
    # between them from a family's own weld rows.  A world in which the two
    # k-classes did not meet would move the word, and the control arms below
    # exhibit exactly such a world through the SAME comparator.
    def overlap_word(rows):
        kw = sorted({r["k"] for r in rows if r["welds"]})
        kn = sorted({r["k"] for r in rows if not r["welds"]})
        aligned = all(bool(r["welds"]) == bool(r["doubled_free"])
                      for r in rows)
        if not kw:
            return "SEC-NEVER-WELDS"
        if not kn:
            return "SEC-OVERLAP-EVERY-TYPE-WELDS"
        if not (set(kw) & set(kn)):
            return "SEC-K-SELECTED"
        if aligned:
            return "SEC-OVERLAP-TYPE-SELECTED-NOT-k-SELECTED"
        return "SEC-OVERLAP-UNDECIDED"

    # the comparator's input is a FRESH weld measurement taken through the real
    # detector at the real amalgam target -- not the census rows the builder
    # used -- so the comparator and the builder do not share an input.
    fresh = []
    for c in census:
        t = [t2 for t2 in typerep if str(t2) == c["type"]][0]
        gl = typerep[t]
        ac_, rel_, _am, _bm, _sh = combinatorial_rel(gl)
        tgt_ = amalgam_target(gl, LINKS, "T(COMPARATOR)", "SIMPLE")
        r_ = detect("SEC-UNION-COMPARATOR", ac_, rel_, tgt_, "EMBEDDING",
                    "BARE")
        fresh.append({"type": c["type"], "k": c["k"],
                      "welds": r_["fate"] == "FOUND-candidate",
                      "doubled_free": c["doubled_free"],
                      "gluings": c["gluings"]})
    # THE CONTROL ARMS.  Three declared sub-families of the real one, each
    # measured through the real weld machinery above, on which the comparator
    # emits three OTHER words -- including the pin's pre-registered
    # SEC-K-SELECTED.  The declination of that word is therefore a
    # measurement: a family exists on which this instrument emits it.
    ARMS = (
        ("ARM-REAL-FAMILY", "every type of the family",
         lambda r: True),
        ("ARM-K-SELECTED", "the k <= 1 types together with the doubled types "
         "-- a family whose welding and non-welding k-classes do not meet",
         lambda r: r["k"] <= 1 or not r["doubled_free"]),
        ("ARM-NONE-WELDS", "the doubled types alone",
         lambda r: not r["doubled_free"]),
        ("ARM-EVERY-TYPE-WELDS", "the doubled-free types alone",
         lambda r: r["doubled_free"]),
    )
    arms = []
    for (anm, awhy, asel) in ARMS:
        arows = [r for r in fresh if asel(r)]
        aword = overlap_word(arows)
        if mut("MUT-CONTROL-ARM") and anm == "ARM-K-SELECTED":
            aword = "SEC-OVERLAP-TYPE-SELECTED-NOT-k-SELECTED"
        arms.append({"arm": anm, "family": awhy, "types": len(arows),
                     "k_values": sorted({r["k"] for r in arows}),
                     "welding_types": sum(1 for r in arows if r["welds"]),
                     "word": aword})
    overlap_head = [a for a in arms
                    if a["arm"] == "ARM-REAL-FAMILY"][0]["word"]
    if mut("MUT-OVERLAP-WORD"):
        overlap_head = "SEC-K-SELECTED"

    # ---- the head's own scalars, every one read off a measured row --------
    k_axis = sorted({c["k"] for c in census})
    k_both = sorted(set(ks_with_weld) & set(ks_without))
    k_only_weld = sorted(set(ks_with_weld) - set(ks_without))
    k_no_pair = [k for k in k_only_weld if k > 0]
    k_top = max(k_axis)
    seam_d = seam[0]["chart_dim"]
    nlink = seam[0]["declared_links"]
    carr_lo = min(c["carriers"] for c in census)
    carr_hi = max(c["carriers"] for c in census)
    bare_rows = [r for r in dict_rows if r["carrier"] == "BARE"]
    struct_alive = len({r["type"] for r in bare_rows
                        if r["fate"] in ("FOUND-candidate", "UNMOTIVATED")})
    count_pos = len({r["type"] for r in bare_rows
                     if r.get("count_min", 0) >= 1})
    site_fiber_1 = sum(1 for c in census if c["fiber_site_A"] == 1)
    dbl_rows = [r for r in bare_rows if r["reading"] == "EMBEDDING"
                and not r["doubled_free"]]
    n_dbl = len(dbl_rows)
    site_free_at_doubled = sum(1 for r in dbl_rows
                               if r["inventory"]["I-SITE-ASSIGNMENT"] > 1)
    label_fib = sorted({r["inventory"]["I-DIRECTION-LABEL"]
                        for r in dbl_rows})
    orient_hi = max(r["inventory"]["I-ORIENT"] for r in dbl_rows)
    orient_free = sum(1 for r in dbl_rows
                      if r["inventory"]["I-ORIENT"] > 1)
    orient_lo = min(r["inventory"]["I-ORIENT"] for r in dbl_rows)
    ext_rows = [r for r in dict_rows if r["carrier"] != "BARE"]
    ext_found = sum(1 for r in ext_rows if r["fate"] == "FOUND-STRUCTURAL")
    ext_types = len({r["type"] for r in ext_rows
                     if r["fate"] == "FOUND-STRUCTURAL"})
    seam_rank = sorted({s["rank"] for s in seam})[0]
    seam_unknowns = sorted({s["unknowns"] for s in seam})[0]
    seam_kern = sorted({s["kernel_dim"] for s in seam})[0]
    conf_moved = sum(c["cells_where_union_differs_from_sector"]
                     for c in compat)
    conf_shared = sum(c["differing_cells_with_both_endpoints_shared"]
                      for c in compat)
    conf_touch = sum(c["pairs_off_count_1_touching_an_unshared_actor"]
                     for c in compat)

    seg1 = ("SEC-ARENA-[TWO DRIVEN R=3 SATURATING SECTORS; %d GLUINGS IN %d "
            "COMBINATORIAL TYPES OVER k IN {%s}; UNION CARRIERS %d..%d; "
            "FORCED %d OF %d DRIVEN WINDOW RECORDS AT THE SHARED-SEED RULE, "
            "AND THAT FATE IS A PROPERTY OF THE RULE (ALL %d GLUINGS CARRY "
            "THE BASE INTO THE SECOND SECTOR UNDER IT); REFUSED %d OF %d AT "
            "PAPER-19'S CANONICAL RULE, WHERE THE FATE IS A PROPERTY OF THE "
            "DRIVEN GLUING AND NOT OF ITS TYPE -- THE CANONICAL RULE SPLITS "
            "%d OF THE %d TYPES AND ONLY %d OF THE %d GLUINGS CARRY; "
            "DRIVEN=COMBINATORIAL AT %d OF %d]"
            "@WINDOW-%d=%d-TYPE-TRANSVERSAL-x-%d-SEED-RULES-OF-%d-GLUINGS"
            % (total_gl, len(typecount), ",".join(str(k) for k in k_axis),
               carr_lo, carr_hi,
               sum(1 for w in window if w["seed_rule"] == "shared"
                   and w["fate"] == "FORCED"),
               sum(1 for w in window if w["seed_rule"] == "shared"),
               carry_shared,
               sum(1 for w in window if w["seed_rule"] == "first"
                   and w["fate"] == "REFUSED"),
               sum(1 for w in window if w["seed_rule"] == "first"),
               len(split), len(typerep), carry_first, total_gl,
               sum(1 for w in window if w["driven_equals_combinatorial"]),
               sum(1 for w in window if w["fate"] == "FORCED"),
               len(window), len(typerep), 2, total_gl))
    seg2 = ("SEC-COMPOSES-[ACTOR->SITE|CO-DIVISION-ACTOR-PAIR->LINK|"
            "DIVISION-COUNT->n_l(x)]@EMBEDDING+QUOTIENT<THE-UNION-DICTIONARY-"
            "EXISTS-AT-EVERY-TYPE:STRUCT-ALIVE-%d-OF-%d(INHERITED:THE-UNION'S-"
            "REALISED-PAIR-SET-IS-THE-AMALGAM'S-INCIDENCE-SET),COUNT-POSITIVE-"
            "%d-OF-%d|MOTIVATED-AT-%d-OF-%d-TYPES(%d-OF-%d-GLUINGS)|"
            "SITE-FIBER=1-AT-%d-OF-%d-TWO-ROUTES:THE-GLUING-BREAKS-EDGE-"
            "TRANSITIVITY-SO-THE-SEAM-IS-VISIBLE-IN-THE-STRUCTURE-ALONE|"
            "I-SITE-ASSIGNMENT-NEVER-FREE(%d-OF-%d-DOUBLED-TYPES,A-TYPE-ROW);"
            "AT-A-DOUBLED-TYPE'S-DECLARED-REPRESENTATIVE-THE-FREE-"
            "ITEMS-ARE-I-DIRECTION-LABEL(%d-AT-%d-OF-%d)-"
            "AND-I-ORIENT(%d-AT-%d-OF-%d,%d-AT-%d-OF-%d)-BOTH-REPRESENTATIVE-"
            "ROWS-NOT-TYPE-ROWS(THE-PAIR-MOVES-INSIDE-%d-OF-%d-TYPES-ON-THE-"
            "DECLARED-SAMPLE)|EXTENDED-CARRIERS:"
            "BOTH-RETURN-FOUND-STRUCTURAL-AT-%d-OF-%d-TYPES-AND-%d-OF-%d-ROWS,"
            "EXT-PAIR-UNDER-SIMPLE-AND-EXT-INCIDENCE-UNDER-CHARTED;THE-INDUCED"
            "-COUNT-FIELD-IS-CARRIER-INDEPENDENT-AND-UNCHANGED;THE-RSQ-"
            "INVENTORY-IS-READ-AT-BARE-ONLY-SO-NO-REPAIR-OF-THE-FREE-ITEM-IS-"
            "MEASURED>"
            % (struct_alive, len(typerep), count_pos, len(typerep),
               sum(1 for o in overlap if o["welds"]), len(overlap),
               cnt_clean, total_gl, site_fiber_1, len(census),
               site_free_at_doubled, n_dbl,
               label_fib[0], n_dbl, n_dbl,
               orient_hi, orient_free, n_dbl,
               orient_lo, n_dbl - orient_free, n_dbl,
               len(moved), len(typerep),
               ext_types, len(typerep), ext_found, len(ext_rows)))
    seg3 = ("SEC-SEAM-CURVATURE-[THE-DIRECT-SUM-IS-A-DECLARATION-NOT-A-"
            "MEASUREMENT: AT EVERY SHARED SITE THE %s DECLARED LINKS GIVE "
            "RANK %d ON THE %d ENTRIES OF Sym^2(Q^%d), KERNEL %d -- BY THEOREM "
            "ON THE ROW SPACE, WHICH MENTIONS NO COUNT, AND MEASURED AT %d OF "
            "%d SHARED SITES; THE DIRECT SUM IS THE CHOICE C=0 AND IS "
            "POSITIVE DEFINITE, AND AN EXACT RATIONAL COMPLETION REPRODUCING "
            "ALL %s COUNTS IS NEGATIVE ON AN EXHIBITED VECTOR] -- "
            "SEAM-CONFINED COMPOSITIONALITY: EVERY CELL AT WHICH THE UNION'S "
            "COUNT DIFFERS FROM THE OWNING SECTOR'S HAS BOTH ENDPOINTS "
            "SHARED, %d OF %d AT %d OF %d TYPES, AND %d PAIRS OFF COUNT 1 "
            "TOUCH AN UNSHARED ACTOR ANYWHERE IN THE UNION ARENA -- NO "
            "SECTOR-PRIVATE LINK EVER MOVES (FIXED-ATTRIBUTION READING) -- "
            "CROSS-SECTOR DIVISION EVENTS ARE "
            "ADMITTED BY THE COMMITTED GRAMMAR (%d OF %d SPECIFICATIONS "
            "DRIVEN, THE OTHERS REFUSED ON THE VERSION LINEAGE) AND EACH "
            "CROSS LINK REMOVES EXACTLY ONE UNDETERMINED ENTRY %s -- EVERY "
            "CROSS-SECTOR EVENT THAT WOULD FIX A SEAM ENTRY LEAVES THE TARGET "
            "BY THEOREM ON THE AMALGAM'S LINK SET (%d OF %d ADMITTED "
            "WITNESSES DIE AT STRUCTURE); WHETHER ANY OTHER COMMITTED "
            "STRUCTURE FIXES THEM IS OPEN AT S-3"
            % (num_word(2 * nlink).upper(), seam_rank, seam_unknowns,
               seam_d, seam_kern, n_sites, n_sites,
               num_word(2 * nlink).upper(),
               conf_shared, conf_moved, len(compat), len(compat), conf_touch,
               sum(1 for c in cross_rows if c["fate"] == "ADMITTED"),
               len(cross_rows),
               "(" + ",".join(str(c["kernel_dim"]) for c in cross_gain) + ")",
               sum(1 for c in cross_rows
                   if c.get("dictionary_after") == "STRUCT-DEAD"),
               sum(1 for c in cross_rows if "dictionary_after" in c)))
    seg4 = ("%s-[EVERY k IN {%s} CARRIES BOTH A WELDING AND A NON-WELDING "
            "TYPE, k IN {%s} ONLY WELDING TYPES AND k=%d HAS NO PAIR TO "
            "DOUBLE; THE CRITERION IS ALIGNMENT: THE UNION WELDS IFF NO "
            "SHARED PAIR IS ADJACENT IN BOTH SECTORS, i.e. IFF EVERY SHARED "
            "PAIR SHARES A TRIPARTITE CLASS ON AT LEAST ONE SIDE; AT k=%d "
            "THIS IS 'ALL %s IN ONE CLASS ON ONE SIDE', %d OF %d GLUINGS; THE "
            "WORD IS TYPED BY A COMPARATOR THAT STATES BOTH HYPOTHESES AND IS "
            "EXERCISED ON %d DECLARED CONTROL FAMILIES, ONE OF WHICH RETURNS "
            "SEC-K-SELECTED] -- STERILITY-CONTROL=k=0-CONSISTENT-WITH-R1'S-"
            "COPYING-LESSON-AT-A-DIFFERENT-OBJECT(NOT-AN-INSTANCE-OF-THEOREM-"
            "B): |Aut|=%d=|Aut(SECTOR)|^2 x 2 BY TWO ROUTES, 0 NEW PAIRS, 0 "
            "DOUBLED, 0 SEAM CELLS, THE DICTIONARY THE DIRECT SUM OF THE TWO "
            "-- AGAINST k=3-ALIGNED WHERE |Aut|=%d AND THE SEAM CARRIES %d "
            "UNDETERMINED ENTRIES"
            % (overlap_head, ",".join(str(k) for k in k_both),
               ",".join(str(k) for k in k_only_weld), k_no_pair[0], k_top,
               num_word(k_top).upper(),
               sum(o["gluings"] for o in overlap
                   if o["welds"] and o["k"] == k_top),
               closed(k_top), len(arms), sterility["aut"],
               contrast["k3_aligned_new_structure"]["aut"],
               contrast["k3_aligned_new_structure"]
               ["seam_undetermined_entries"]))
    if mut("MUT-HEAD-FORGE"):
        seg2 = seg2.replace("SEC-COMPOSES", "SEC-NEVER-WELDS")
    verdict = [seg1, seg2, seg3, seg4]
    R["verdict"] = SEAL.seal("verdict", verdict)

    # THE DICTIONARY COMPARATOR.  It re-derives SEGMENT 2's outcome word from
    # the receipt's own fate rows -- one word, one segment -- and re-checks the
    # seam kernel and the sterility identity.  It types its own branch
    # structure and shares no code, no input and no typed literal with the
    # builder.  Segment 4's word has its OWN comparator (`overlap_word` above,
    # gated at G-OVERLAP-RECON with control arms); segments 1 and 3 are
    # rendered from the receipt and gated verbatim against this run's own
    # verdict strings, and their words are not independently re-derived.
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

    # THE OVERLAP COMPARATOR'S OWN GATE.  Segment 4's word is the comparator's
    # output, and the comparator's input is a weld measurement taken again,
    # through the real detector, on the real target.
    fresh_bad = [f["type"] for f, o in zip(fresh, overlap)
                 if f["welds"] != o["welds"] or f["type"] != o["type"]]
    LD.gate("G-OVERLAP-RECON",
            (not fresh_bad and overlap_head == arms[0]["word"]
             and verdict[3].split("-[")[0] == overlap_head
             and bool(set(ks_with_weld) & set(ks_without))),
            "the head's fourth outcome word is TYPED BY A COMPARATOR and not "
            "by the builder: the weld column is measured a second time through "
            "the real detector at the real amalgam target and agrees with the "
            "published one at %d of %d types, and the comparator -- which "
            "states the k-hypothesis and the alignment hypothesis itself and "
            "decides between them from those rows alone -- emits the word the "
            "head carries.  A forged word moves the builder alone and dies "
            "here" % (len(fresh) - len(fresh_bad), len(fresh)),
            {"comparator_word": arms[0]["word"], "head_word":
             verdict[3].split("-[")[0], "fresh_disagreements": fresh_bad,
             "k_with_a_welding_type": ks_with_weld,
             "k_with_a_non_welding_type": ks_without})
    words = [a["word"] for a in arms]
    LD.gate("G-OVERLAP-CONTROLS",
            ("SEC-K-SELECTED" in words[1:]
             and len(set(words)) == len(words)
             and words[0] != "SEC-K-SELECTED"),
            "THE DECLINATION OF THE PRE-REGISTERED WORD IS MEASURED.  The same "
            "comparator is exercised on %d declared families, each measured "
            "through the real weld machinery: the real family, and three "
            "declared sub-families of it.  It emits %d DIFFERENT words, and "
            "one of them is the pin's own pre-registered SEC-K-SELECTED -- so "
            "the instrument can emit that word, this world is not one on which "
            "it does, and the declination is an outcome rather than an "
            "assertion" % (len(arms), len(set(words))),
            {"arms": [{"arm": a["arm"], "types": a["types"],
                       "word": a["word"]} for a in arms]})
    R["overlap_comparator"] = SEAL.seal(
        "overlap_comparator", {"head_word": overlap_head, "arms": arms,
                               "fresh_rows": fresh,
                               "hypotheses": [
                                   "k-SELECTED: the set of k carrying a "
                                   "welding type and the set carrying a "
                                   "non-welding type are disjoint",
                                   "ALIGNMENT: a type welds exactly when no "
                                   "shared pair is adjacent in both sectors"]})

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
    # THE CHOICE INVENTORY, PUBLISHED AS DATA (RUNBOOK section 15) so that
    # every row of the paper's own inventory table is a rendered claim.  The
    # measured fibers are read from the measurement; the classes are this
    # unit's declarations and are stated as such.
    lab_fibs = sorted({r0["inventory"]["I-DIRECTION-LABEL"] for r0 in dict_rows
                       if r0["carrier"] == "BARE"
                       and r0["reading"] == "EMBEDDING"})
    ori_fibs = sorted({r0["inventory"]["I-ORIENT"] for r0 in dict_rows
                       if r0["carrier"] == "BARE"
                       and r0["reading"] == "EMBEDDING"})
    R["choice_inventory"] = SEAL.seal("choice_inventory", [
        {"n": 1, "item": "the base object: two CONFLICT-GRID(3, 3)",
         "class": "forced", "fiber": "1", "binds": "paper-19's, driven"},
        {"n": 2, "item": "the saturating arrangement per sector",
         "class": "measured", "fiber": "1", "binds": "section 2.4"},
        {"n": 3, "item": "the site carrier: actors to the lattice",
         "class": "forced", "fiber": "1",
         "binds": "the constructor's own naming"},
        {"n": 4, "item": "admissibility: the layer's own menu",
         "class": "forced", "fiber": "1", "binds": "d42b1 driven directly"},
        {"n": 5, "item": "the I7 readout", "class": "forced", "fiber": "1",
         "binds": "HA, matched verbatim"},
        {"n": 6, "item": "k, and the gluing", "class": "declared, the axis",
         "fiber": "every member run", "binds": "section 2.1"},
        {"n": 7, "item": "the seed rule", "class": "declared", "fiber": "2",
         "binds": "both driven, section 3.2"},
        {"n": 8, "item": "the link individuation",
         "class": "declared, VERDICT-DETERMINING for EXT-INCIDENCE and for "
                  "the seam chart at a doubled site",
         "fiber": "2", "binds": "sections 4.3 and 6.1"},
        {"n": 9, "item": "the carrier", "class": "declared",
         "fiber": str(len(COMBOS)), "binds": "section 2.3"},
        {"n": 10, "item": "the reading", "class": "declared", "fiber": "2",
         "binds": "weld 2's, every row stamped"},
        {"n": 11, "item": "the seam chart: the direct-sum chart",
         "class": "declared", "fiber": "1", "binds": "section 6.1"},
        {"n": 12, "item": "I-SITE-ASSIGNMENT", "class": "measured",
         "fiber": "1", "binds": "section 3.1, two routes"},
        {"n": 13, "item": "I-DIRECTION-LABEL", "class": "measured",
         "fiber": " or ".join(str(x) for x in lab_fibs),
         "binds": "section 4.2"},
        {"n": 14, "item": "I-ORIENT", "class": "measured",
         "fiber": " or ".join(str(x) for x in ori_fibs),
         "binds": "section 4.2"},
        {"n": 15, "item": "the three cross-sector specifications",
         "class": "free", "fiber": "--", "binds": "this unit's; section 6.3"},
        {"n": 16, "item": "the window's type representative",
         "class": "free, VERDICT-DETERMINING for the canonical-rule fate "
                  "clause",
         "fiber": "--",
         "binds": "section 3.2; the abstract arena is a type invariant, "
                  "section 5.2"},
    ])
    claims = paper_claims(R, total_gl, closed)
    R["paper_claims"] = SEAL.seal("paper_claims", claims)
    # the surface the paper leg covers, published as NUMBERS so the paper's own
    # sentence about its coverage is backed by the run that tests it
    R["paper_surface"] = SEAL.seal(
        "paper_surface",
        {"table_rows_rendered": sum(1 for c in claims
                                    if c["id"].startswith("T-")),
         "tables": len(TABLE_HEADERS),
         "column_headers_rendered": len(TABLE_HEADERS),
         "prose_claims": sum(1 for c in claims if c["id"].startswith("C")),
         "polarity_rows": len(POLARITY),
         "quoted_anchors": sum(1 for a in anch if a["quote"] is not None),
         "fence_copies_each": FENCE_COPIES,
         "spelled_grammar_words": len(SPELLED)})
    if not numbers_only:
        if mut("MUT-PAPER-NUMBER"):
            ptext = ptext.replace("45010", "45011", 1)
        if mut("MUT-PAPER-PERIOD"):
            # a numeral immediately followed by a full stop: the digit-side
            # blind spot the delivered NUM_RE carried
            ptext = ptext.replace("62208.", "62209.", 1)
        if mut("MUT-PAPER-FENCE"):
            # a forged TWIN of a legitimate fence, carrying no new numeral and
            # no moved referent -- so it can only be caught by the fence gate
            ptext = (ptext + "\n```\n"
                     + verdict[0].replace("FORCED", "REFUSED") + "\n```\n")
        if mut("MUT-PAPER-FENCE-INFO"):
            # E-22's own disease: a fenced block whose info string carries a
            # NON-LETTER, which the delivered scanner's regex could not see
            ptext = (ptext + "\n```txt1\nSEC-NEVER-WELDS-[THE UNION CARRIES "
                     "NO DICTIONARY AT ANY TYPE]\n```\n")
        if mut("MUT-PAPER-POLARITY"):
            ptext = ptext.replace("the direct sum is a declaration",
                                  "the direct sum is a measurement", 1)
        if mut("MUT-PAPER-DIRECTION"):
            ptext = ptext.replace("every admitted one kills the dictionary",
                                  "no admitted one kills the dictionary", 1)
        if mut("MUT-PAPER-QUOTE"):
            ptext = ptext.replace("must **divide** a block, not copy one",
                                  "must **copy** a block, not divide one", 1)
        if mut("MUT-PAPER-TABLE"):
            trow = [c["text"] for c in claims
                    if c["id"].startswith("T-CENSUS-")][0]
            cells = trow.split("|")
            cells[2], cells[3] = cells[3], cells[2]
            ptext = ptext.replace(trow, "|".join(cells), 1)
        if mut("MUT-PAPER-COMPAT"):
            # THE VERDICT WORD OF THE SEAM-CONFINEMENT CENSUS.  The census's
            # own words are what the locality result is read off, so the paper
            # leg must be shown to hold them, not merely to hold the numbers
            # beside them.
            crow = [c["text"] for c in claims
                    if c["id"].startswith("T-COMPAT-")
                    and "COMPATIBLE" in c["text"]][0]
            ptext = ptext.replace(
                crow, crow.replace("COMPATIBLE", "SEAM-DEFORMED"), 1)
        if mut("MUT-PAPER-ROWSET"):
            # THE STRAY ROW: a data row nobody rendered, appended to a real
            # table, every numeral in it backed elsewhere in the receipt.  It
            # satisfies containment and dies at equality.
            crow = [c["text"] for c in claims
                    if c["id"].startswith("T-COMPAT-")][0]
            ptext = ptext.replace(crow, crow + "\n" + crow.replace(
                "COMPATIBLE", "SEAM-DEFORMED"), 1)
        if mut("MUT-PAPER-HEADER"):
            hdr = dict(TABLE_HEADERS)["H-OVERLAP"]
            cells = hdr.split("|")
            cells[2], cells[3] = cells[3], cells[2]
            ptext = ptext.replace(hdr, "|".join(cells), 1)
        if mut("MUT-PAPER-SPELLED"):
            ptext = ptext.replace("fifty-four", "a thousand", 1)
        if mut("MUT-PAPER-REFERENT"):
            # THE CROSS-COLLECTION SENTENCE.  Every numeral in it is in the
            # registry and every clause of it is false of the receipt.
            ptext = (ptext + "\n\nAt the aligned seam the union carries 16 "
                     "undetermined entries on 45010 shared cells, and 2970 of "
                     "its 42336 gluings are refused by the committed "
                     "grammar.\n")
        # the numeral registry and the SPELLED scan are taken FIRST, so a
        # spelled numeral that has been moved dies as the spelled-numeral
        # forgery it is rather than as a missing claim
        cov = paper_coverage(R, ptext, verdict)
        spl = paper_spelled(ptext, cov["registry"])
        LD.gate("G-PAPER-SPELLED",
                spl["ok"],
                "a numeral spelled in words is a claim like any other, at "
                "every magnitude and not only above twelve: the scanner "
                "carries a GENERATED number-word grammar of %d words rather "
                "than a hand-kept dictionary, every spelled numeral in the "
                "paper has its integer in the receipt's own registry, and the "
                "registry carries no sha256, ledger-chain or seal-manifest "
                "token.  The spelled numerals that carry a MEASUREMENT are "
                "bound tighter still, at G-PAPER-CLAIMS, by claims rendered "
                "from the measured value" % len(SPELLED),
                spl)
        miss = [c["id"] for c in claims if not match_needle(ptext, c["text"])]
        LD.gate("G-PAPER-CLAIMS",
                not miss,
                "every rendered claim of the receipt -- the prose claims AND "
                "EVERY DATA ROW OF EVERY published table, %d rows across %d "
                "tables -- occurs in the paper under test as written, under "
                "the #125 normaliser, so a swapped table cell dies here"
                % (sum(1 for c in claims if c["id"].startswith("T-")),
                   len(TABLE_HEADERS)),
                {"claims": len(claims), "missing": miss,
                 "table_rows": sum(1 for c in claims
                                   if c["id"].startswith("T-")),
                 "prose_claims": sum(1 for c in claims
                                     if c["id"].startswith("C"))})
        hmiss = [hid for (hid, htxt) in TABLE_HEADERS
                 if not match_needle(ptext, htxt)]
        LD.gate("G-PAPER-TABLES",
                not hmiss and len(TABLE_HEADERS) > 0,
                "every published table's COLUMN HEADER is a rendered claim "
                "too: a header names which column is which, so a swapped pair "
                "of labels moves every cell of the table without moving a "
                "numeral.  All %d headers are matched in the object under test"
                % len(TABLE_HEADERS),
                {"headers": len(TABLE_HEADERS), "missing": hmiss})
        rowset = paper_rowset(ptext, claims)
        LD.gate("G-PAPER-ROWSET",
                rowset["ok"],
                "the table side is an EQUALITY, not a containment: the "
                "multiset of the paper's %d table data rows is compared "
                "against the multiset of the %d rendered table rows and must "
                "be equal.  Containment alone admits a paper that carries "
                "every rendered row AND ONE MORE -- a forged row whose "
                "numerals are backed elsewhere, a duplicated row, a row of a "
                "table that does not exist -- and that stray was measured to "
                "survive the delivered object"
                % (rowset["paper_data_rows"], rowset["rendered_table_rows"]),
                rowset)
        qmiss = [a["id"] for a in anch if a["quote"] is not None
                 and not match_needle(ptext, a["quote"])]
        LD.gate("G-PAPER-QUOTES",
                not qmiss and sum(1 for a in anch
                                  if a["quote"] is not None) >= 5,
                "the verbatim anchors are checked ON THE QUOTE SIDE.  An "
                "anchor found only in its source proves the sentence exists "
                "somewhere; it does not protect the paper's rendering of it, "
                "and an inverted block quotation would survive.  Every one of "
                "the %d quoted anchors is required in the object under test, "
                "under the same normaliser, as the fragment G-ANCHORS has "
                "already shown to be verbatim inside its pinned parent"
                % sum(1 for a in anch if a["quote"] is not None),
                {"quoted": [a["id"] for a in anch if a["quote"] is not None],
                 "missing": qmiss})
        REFERENTS = [
            ("combinatorial types", {len(typecount)}),
            ("union arenas", {R["arena_classes"]["arenas"]}),
            ("undetermined entries",
             {contrast["k3_aligned_new_structure"]
              ["seam_undetermined_entries"]}),
            ("shared sites", {n_sites}),
            ("shared cells", {c["shared_cells"] for c in compat}),
            ("driven window records", {len(window) // 2, len(window)}),
            ("declared mutants", {len(MUTANTS)}),
            ("sources are read at run time", {len(SOURCES)}),
        ]
        ref = paper_referents(ptext, REFERENTS)
        LD.gate("G-PAPER-REFERENTS",
                ref["ok"],
                "every numeral standing in front of a DECLARED REFERENT "
                "PHRASE is a value this run measured FOR THAT PHRASE, and "
                "every one of the %d declared phrases is exercised by the "
                "paper.  A numeral can be individually backed by the registry "
                "and still be false of the noun it precedes: numerals drawn "
                "from four different collections compose into a sentence that "
                "contradicts the receipt on every clause while each of them "
                "is in the registry, and that is the disease this gate "
                "refuses" % len(REFERENTS),
                ref)
        LD.gate("G-PAPER-COVERAGE",
                not cov["unbacked"],
                "every numeral in the paper under test -- INCLUDING those "
                "inside fenced blocks, inline code spans and tables, and "
                "INCLUDING a numeral immediately followed by a full stop or "
                "carrying a leading minus -- is backed by the receipt's own "
                "number registry; no blanket whitelist is used",
                {"scanned": cov["scanned"], "unbacked": cov["unbacked"][:12],
                 "n_unbacked": len(cov["unbacked"])})
        fence = paper_fences(ptext, verdict)
        LD.gate("G-PAPER-FENCE",
                fence["ok"],
                "every fenced block of the paper is verbatim one of THIS "
                "RUN's verdict strings and the multiset of blocks is EQUAL to "
                "the declared one -- each segment exactly %d times, whatever "
                "the info string of the fence that carries it -- so neither a "
                "forged twin hiding behind a clean sibling nor a forged head "
                "behind a non-letter fence prefix survives"
                % FENCE_COPIES,
                fence)
        pol = paper_polarity(ptext)
        LD.gate("G-PAPER-POLARITY",
                pol["ok"],
                "every DIRECTION-BEARING sentence the head asserts is matched "
                "in the paper with its sign and its own inversion is required "
                "absent -- %d rows, not the three the delivered object "
                "carried -- so the alignment criterion, the selector, the "
                "cross-sector kill, the seam-confinement clause, the "
                "extended-carrier price, the E-24 stamp and the read-out "
                "cannot be inverted in prose while their numbers stay put"
                % len(POLARITY),
                pol)
        # THE TWO SELF-LISTS, BOUND.  The delivered object sealed a measure
        # stamp and a standards block that no gate read: keys that said the
        # right thing about a paper nothing compared them to.  Both are
        # compared against the object under test here.  E-24's duty is that
        # each fraction NAMES THE COLLECTION IT COUNTS, so each collection the
        # stamp names must occur in the paper; and the standards this run says
        # govern the paper's own instrument and arena sections must be cited
        # there.  (The word this duty is usually stated with is itself a
        # barred term at the cosmology wall, so it is not used here.)
        std = R["standards"]
        stamp_missing = [f for f in RATIO_FAMILIES
                         if not match_needle(ptext, f)]
        std_needles = ["#%d" % std["cli_contract"],
                       "RUNBOOK section %d" % std["declared_arena"]]
        if mut("MUT-STAMP-NAME"):
            stamp_missing = ["a collection the paper does not name"]
        std_missing = [s for s in std_needles if not match_needle(ptext, s)]
        LD.gate("G-DECLARED-STANDARDS",
                not stamp_missing and not std_missing
                and MEASURE_STAMP == "COUNTING-ONLY",
                "the measure stamp and the standards block are CONSUMED and "
                "not merely published: every one of the %d fraction "
                "collections "
                "this run stamps COUNTING-ONLY is named in the object under "
                "test, in the paper's own words, so E-24's naming duty is "
                "measured against the paper rather than asserted beside it; "
                "and the standards this run says govern the paper's CLI and "
                "arena declarations are cited in it"
                % len(RATIO_FAMILIES),
                {"ratio_families": len(RATIO_FAMILIES),
                 "collections_not_named_in_the_paper": stamp_missing,
                 "standards_not_cited_in_the_paper": std_missing,
                 "stamp": MEASURE_STAMP})
        R["paper_gates"] = SEAL.seal(
            "paper_gates", {"claims": len(claims), "coverage": cov["scanned"],
                            "fences": fence, "polarity": pol, "spelled": spl,
                            "headers": len(TABLE_HEADERS),
                            "rowset": rowset,
                            "quoted_anchors": sum(1 for a in anch
                                                  if a["quote"] is not None),
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
    # E-24, MEASURE-RELATIVITY OF COUNTS.  This unit publishes no probability
    # and no percentage.  Every ratio it publishes is a COUNT over a declared
    # exhaustive enumeration with its denominator written beside it, and no
    # measure is declared on the gluing family -- so every one is stamped
    # COUNTING-ONLY rather than dressed as a likelihood.
    R["measure_stamp"] = SEAL.seal("measure_stamp", {
        "stamp": MEASURE_STAMP,
        "declared_measure_on_the_gluing_family": None,
        "ratios_published": list(RATIO_FAMILIES),
        "note": "each is a count over an exhaustive enumeration with its "
                "denominator published; none is a probability, and this unit "
                "declares no measure under which it could be read as one"})
    R["schema_version"] = SEAL.seal("schema_version", SCHEMA)
    # THE THREE KEYS THAT CANNOT SEAL THEMSELVES, and the forcing is stated
    # rather than assumed: the ledger, its length and its chain head are the
    # per-row seal of every gate, including the gates emitted after them, so a
    # key cannot digest the row that publishes it.  What binds them instead is
    # RECOMPUTABILITY: the published chain head is the head of the published
    # rows under the genesis rule, and a receipt-only verifier can rebuild it.
    # The delivered object published a 37-row ledger beside a 40-row chain
    # head; here the rows and the head are taken together, at the writer.
    SEAL.declare_unsealed("ledger",
                          "the chained gate ledger is the seal of every gate "
                          "row and is closed at the writer, after the gates "
                          "that would otherwise have to appear inside it; it "
                          "is bound by recomputation from its own rows")
    SEAL.declare_unsealed("gate_count",
                          "the run's own gate count is the length of the "
                          "ledger and is closed with it")
    SEAL.declare_unsealed("seal_manifest",
                          "the manifest cannot digest itself")
    SEAL.declare_unsealed("ledger_chain",
                          "the chained ledger head is the seal of every gate "
                          "row and is emitted after the manifest is closed; "
                          "it is the head of the published rows under the "
                          "genesis rule and is recomputable from them")
    return LD, SEAL, R, verdict, ptext


LATER_GATES = ("G-SWEEP-EXECUTED", "G-SEAL-VERIFIED", "G-WALL-TOTAL",
               "G-ANCHOR-CONSUMERS", "G-SEAL-COMPLETE", "G-INTEGRITY")
PAPER_GATES = ("G-PAPER-CLAIMS", "G-PAPER-TABLES", "G-PAPER-ROWSET",
               "G-PAPER-QUOTES", "G-PAPER-REFERENTS", "G-PAPER-COVERAGE",
               "G-PAPER-FENCE", "G-PAPER-POLARITY", "G-PAPER-SPELLED",
               "G-DECLARED-STANDARDS")

# THE WAIVERS, AND EVERY FORCING IS TRUE.  The delivered object carried six
# waivers naming a mutant that provably died at an EARLIER gate and never
# reached the gate it was said to falsify; each of those six now has a mutant
# of its own (MUT-DEAD-FATE, MUT-AUT-ROUTE-UNION, MUT-SEED-FATE,
# MUT-CROSS-ALGEBRA, MUT-CONTRAST, MUT-SWEEP-FORGE) and has left this list.
# What remains is four gates that cannot be falsified by an object corruption
# because their subject IS the corruption machinery, and each states why.
WAIVED = {
    "G-EXACT": "waived with a forcing: a mutant that introduced a float would "
               "have to BE a float, and the AST scan is the falsifier of its "
               "own object; the same scan's open-call-site leg is exercised "
               "by MUT-STRAY-READ, which takes a read the register then sees",
    "G-MAXHITS": "waived with a forcing: every event is specified by its full "
                 "tuple, at most one candidate can match, and the under-"
                 "specified control is paper-19's committed measurement "
                 "(maxhits 7) which this unit cites and does not re-run",
    "G-DECLARED-LATER": "waived with a forcing: the gate discharges the "
                        "coverage gate's own declared-later promise, and a "
                        "mutant of it would be a mutant of the ledger it "
                        "reads",
    "G-COVERAGE": "waived with a forcing: a mutant of the coverage gate would "
                  "be a mutant of the mutant registry, and the registry is "
                  "compared against the run's own evaluated ledger",
    "G-INTEGRITY": "waived with a forcing: the integrity check is the write "
                   "path's own comparison, and the leg that says the "
                   "comparison can fail is a REAL corruption of a REAL staged "
                   "file, read back through the same accessor and required to "
                   "differ, in this very run -- not a constant-true expression",
}


# ---------------------------------------------------------------------------
# the paper instrument
# ---------------------------------------------------------------------------

def paper_claims(R, total_gl, closed):
    """the rendered claims: the paper's prose AND **EVERY DATA ROW OF EVERY
    PUBLISHED TABLE** are checked against these, and they are rendered FROM THE
    RECEIPT so a stale sentence or a swapped cell cannot survive.  E-22: tables
    render as claims -- all of them, not the six families the delivered object
    covered.  The header rows are rendered separately, at G-PAPER-TABLES."""
    census = R["type_census"]
    overlap = R["forced_overlap"]["rows"]
    window = R["window"]
    seam = R["seam"]
    cross_rows = R["cross_sector"]
    sterility = R["sterility"]
    compat = R["gluing_fiber"]["compatibility"]
    dead = R["dead_arms"]
    gt = R["gluing_totals"]
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
        ("C05", "the seam system has rank %d on %d unknowns, so its kernel "
                "is %d" % (seam[0]["rank"], seam[0]["unknowns"],
                           seam[0]["kernel_dim"])),
        ("C06", "%d of the %d cross-sector specifications are ADMITTED by the "
                "committed grammar"
         % (sum(1 for c in cross_rows if c["fate"] == "ADMITTED"),
            len(cross_rows))),
        ("C07", "the doubled-free gluings number %d of %d"
         % (sum(o["gluings"] for o in overlap if o["welds"]), total_gl)),
        ("C08", "at k = 3 the criterion is met by %d of the %d gluings"
         % (sum(o["gluings"] for o in overlap if o["welds"] and o["k"] == 3),
            closed(3))),
        # the registries the paper's own instrument section types in prose:
        # bound here so a moved count dies rather than travelling
        ("C09", "%d sources are read at run time" % len(R["provenance"])),
        ("C10", "%d declared mutants" % R["totals"]["mutants"]),
        ("C11", "the %d types carry %d union arenas up to isomorphism"
         % (R["arena_classes"]["types"], R["arena_classes"]["arenas"])),
        ("C12", "no pair carrying a count other than 1 touches an unshared "
                "actor at any of the %d types" % len(compat)),
        ("C13", "the seam system is solved at every one of the %d shared "
                "sites of the %d type representatives"
         % (R["seam_all_sites"]["shared_sites"],
            len(R["seam_all_sites"]["rows"]))),
        # THE SPELLED NUMERALS THAT CARRY A MEASUREMENT, rendered FROM the
        # measured value: a spelled numeral bound to its own claim's number
        # rather than to membership in a registry
        ("C14", "The record fixes %s of the %s entries of the seam's form"
         % (num_word(seam[0]["rank"]), num_word(seam[0]["unknowns"]))),
        ("C15", "realise %s pairs between them" % num_word(c0["pairs"])),
        ("C16", "the union carries %s links: %s of the A-chart and %s of the "
                "B-chart" % (num_word(2 * len(seam[0]["nA"])),
                             num_word(len(seam[0]["nA"])),
                             num_word(len(seam[0]["nB"])))),
        # the single-sector control, bound sentence by sentence so that a
        # numeral inside it cannot be moved to another measured value
        ("C23", "the (I-DIRECTION-LABEL, I-ORIENT) pair takes more than "
                "one value at %d of the %d types"
         % (R["representative_rows"]["types_where_the_pair_moves"],
            len(R["type_census"]))),
        ("C25", "the per-site seam profile takes more than one value at %d "
                "of the %d types"
         % (R["representative_rows"]["types_where_the_seam_profile_moves"],
            len(R["type_census"]))),
        ("C24", "a declared sample of up to %s of its gluings"
         % num_word(R["representative_rows"]["sample_cap"])),
        ("C18", "the union welds -- zero free items -- at %d of them, "
                "which are %d of the %d gluings"
         % (nw, sum(o["gluings"] for o in overlap if o["welds"]), total_gl)),
        ("C19", "canonical rule refuses at %d of the %d driven window "
                "records; the shared-seed rule drives all %d"
         % (sum(1 for w in window if w["seed_rule"] == "first"
                and w["fate"] == "REFUSED"),
            len(window) // 2, len(window) // 2)),
        ("C20", "the driven and combinatorial routes agree at %d of %d "
                "FORCED window records"
         % (sum(1 for w in window if w["driven_equals_combinatorial"]),
            sum(1 for w in window if w["fate"] == "FORCED"))),
        ("C21", "the drive itself is run at %d records"
         % (len(window) + len(R["off_window"]))),
        ("C22", "item %d chooses which gluing of a type is driven"
         % R["choice_inventory"][-1]["n"]),
        ("C17", "one sector runs to %d events with %d division events, its "
                "link field is 1 at all %d of %d cells, det = %s at all %s "
                "sites and the form is positive definite at %d of %d"
         % (R["sector"]["events"], R["sector"]["divisions"],
            R["sector"]["cells_at_one"], R["sector"]["cells"],
            R["sector"]["det"], num_word(len(SITES)),
            R["sector"]["posdef"], len(SITES))),
    ]
    # ---- EVERY DATA ROW OF EVERY PUBLISHED TABLE, rendered as a claim ----
    # section 2.3, the carriers and the readings
    for c in R["carrier_axis"]:
        out.append(("T-CARRIER-%s" % c["carrier"],
                    "| `%s` | %s | %s |"
                    % (c["carrier"], c["site_objects"], c["target"])))
    # section 3.1, the census of types
    for c in census:
        out.append(("T-CENSUS-%s" % c["type"],
                    "| `%s` | %d | %d | %d | %d | %d | %d | %d |"
                    % (c["type"], c["gluings"], c["carriers"], c["pairs"],
                       c["doubled"], c["aut"], c["aut_weighted"],
                       c["fiber_site_A"])))
    # section 3.2, the driven window
    for w in window:
        out.append(("T-WINDOW-%s-%s" % (w["type"], w["seed_rule"]),
                    "| `%s` | %s | %s | %s | %s | %s |"
                    % (w["type"], w["seed_rule"], w["fate"], w["events"],
                       w["divisions"],
                       "yes" if w["driven_equals_combinatorial"] else "--")))
    # section 4.1, the fate / free-item / fiber summary
    for f in R["fate_summary"]:
        out.append(("T-FATE-%s" % f["id"],
                    "| `%s` | %d of %d | %s | %d, %d, %d |"
                    % (f["fate"], f["types"], f["of"], f["free_items"],
                       f["site"], f["label"], f["orient"])))
    # section 4.4, the declared dead arms
    for d in dead:
        out.append(("T-DEAD-%s-%s" % (d["arena"], d["reading"]),
                    "| %s | %s | %s |"
                    % (d["arena"], d["reading"], d["fate"])))
    # section 5.1, the compatibility census
    for c in compat:
        out.append(("T-COMPAT-%s" % c["type"],
                    "| `%s` | %d | %d | %d | %d | %s |"
                    % (c["type"], c["shared_cells"],
                       c["cells_where_union_differs_from_sector"],
                       c["differing_cells_with_both_endpoints_shared"],
                       c["pairs_off_count_1_touching_an_unshared_actor"],
                       "COMPATIBLE" if c["compatible"] else "SEAM-DEFORMED")))
    # section 5.2, the mirror pairs that collapse the types onto arenas
    for m in R["arena_classes"]["mirror_pairs"]:
        out.append(("T-MIRROR-%s" % m["type"],
                    "| `%s` | `%s` | %d + %d | %d |"
                    % (m["type"], m["mirror"], m["gluings"],
                       m["mirror_gluings"], m["arena_fiber"])))
    # section 6.1, the seam systems
    for s in seam:
        out.append(("T-SEAM-%s" % s["gluing"],
                    "| %s | %s | %s | %d | %d | %d | %d | %s |"
                    % (s["gluing"], s["nA"], s["nB"], s["equations"],
                       s["unknowns"], s["rank"], s["kernel_dim"],
                       s["indefinite_witness"]["value"])))
    # section 6.2, the cross-link ladder
    for c in R["seam_cross_algebra"]:
        out.append(("T-XALG-%d" % c["cross_links"],
                    "| %d | %d | %d |"
                    % (c["cross_links"], c["rank"], c["kernel_dim"])))
    # section 6.3, the cross-sector specifications
    for c in cross_rows:
        out.append(("T-CROSS-%s" % c["spec"],
                    "| %s | %s | %s | %d | %d | %s |"
                    % (c["spec"], c["seed"], c["fate"], c["new_pairs"],
                       c["foreign_pairs"],
                       c.get("dictionary_after", "--"))))
    # section 7, the forced-overlap table
    for o in overlap:
        out.append(("T-OVERLAP-%s" % o["type"],
                    "| `%s` | %d | %d | %d | %s | %s |"
                    % (o["type"], o["k"], o["gluings"], o["doubled"],
                       o["bare_fate"], "YES" if o["welds"] else "no")))
    # section 7, the doubled-free count by k
    for k in ("0", "1", "2", "3"):
        out.append(("T-BYK-%s" % k,
                    "| %s | %d | %d |"
                    % (k, gt["by_k"][k], gt["doubled_free_by_k"][k])))
    # section 8, the k = 0 sterility control
    for (lab, key) in STERILITY_ROWS:
        out.append(("T-STERILE-%s" % key,
                    "| %s | %s |" % (lab, sterility[key])))
    # section 11, the choice inventory
    for c in R["choice_inventory"]:
        out.append(("T-CHOICE-%d" % c["n"],
                    "| %d | %s | %s | %s | %s |"
                    % (c["n"], c["item"], c["class"], c["fiber"],
                       c["binds"])))
    return [{"id": i, "text": t} for i, t in out]


# the published column headers, table by table.  A header is a claim about
# which column is which, and a swapped pair of labels moves every cell of the
# table without moving a numeral -- so the header rows are rendered too.
TABLE_HEADERS = [
    ("H-CARRIER", "| carrier | site objects | target |"),
    ("H-CENSUS", "| type | gluings | n | E | dbl | \\|Aut\\| | \\|Aut_w\\| | "
                 "site fiber |"),
    ("H-WINDOW", "| type | seed rule | fate | events | divisions | "
                 "driven = combinatorial |"),
    ("H-FATE", "| bare fate | types | free items | site, label, orient |"),
    ("H-DEAD", "| arena | reading | fate |"),
    ("H-COMPAT", "| type | shared cells | cells where the union differs | "
                 "of those, both endpoints shared | pairs off count 1 "
                 "touching an unshared actor | verdict |"),
    ("H-MIRROR", "| type | mirror type | gluings | arena fiber |"),
    ("H-SEAM", "| seam | n(A) | n(B) | equations | unknowns | rank | kernel | "
               "Q(v) at the witness |"),
    ("H-XALG", "| cross links | rank | kernel |"),
    ("H-CROSS", "| specification | seed | fate | new pairs | foreign pairs | "
                "dictionary after |"),
    ("H-OVERLAP", "| type | k | gluings | doubled | bare fate | welds |"),
    ("H-BYK", "| k | gluings | doubled-free |"),
    ("H-STERILE", "| quantity | k = 0 |"),
    ("H-CHOICE", "| # | item | class | fiber | where it binds |"),
]


STERILITY_ROWS = [
    ("carriers", "carriers"),
    ("realised pairs", "pairs"),
    ("pairs beyond the two sectors' own", "new_pairs_beyond_the_two_sectors"),
    ("doubled pairs", "doubled"),
    ("seam cells", "seam_cells"),
    ("shared actors", "shared_actors"),
    ("\\|Aut\\|, chain route", "aut"),
    ("\\|Aut\\|, component-product route", "aut_components_route"),
    ("the direct-sum prediction", "direct_sum_prediction"),
    ("dictionary", "dictionary_fate"),
]


# A COMPLETE NUMBER-WORD GRAMMAR, not a sixteen-word dictionary.  The
# delivered scanner missed `fifty-three` (not a key) and every word at or below
# twelve (not scanned by design), so "six of the ten entries" could be moved to
# "nine of the ten" in the sentence above the unit's own verdict fence.  The
# words are GENERATED, so no spelled numeral in this range is unscannable.
_UNITS = ("zero", "one", "two", "three", "four", "five", "six", "seven",
          "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen",
          "fifteen", "sixteen", "seventeen", "eighteen", "nineteen")
_TENS = {20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty",
         70: "seventy", 80: "eighty", 90: "ninety"}
SPELLED = {w: i for i, w in enumerate(_UNITS)}
for _v, _w in _TENS.items():
    SPELLED[_w] = _v
    for _i in range(1, 10):
        SPELLED["%s-%s" % (_w, _UNITS[_i])] = _v + _i
SPELLED["hundred"] = 100
SPELLED["thousand"] = 1000


def num_word(n):
    """the English spelling of a measured integer, so that a spelled numeral
    in the paper can be rendered FROM the value it claims rather than merely
    checked for membership in a registry."""
    if n < 20:
        return _UNITS[n]
    if n < 100:
        t, u = (n // 10) * 10, n % 10
        return _TENS[t] if u == 0 else "%s-%s" % (_TENS[t], _UNITS[u])
    return str(n)


def paper_spelled(text, reg):
    """#267 (d): a numeral spelled in words is a claim like any other.  Every
    spelled numeral in the paper must have its integer in the receipt's own
    registry -- and the spelled numerals that carry a MEASUREMENT are bound
    tighter still, at G-PAPER-CLAIMS, by claims rendered from the measured
    value through `num_word` rather than by registry membership."""
    low = canon(text).lower()
    bad = []
    seen = []
    for word, val in sorted(SPELLED.items(), key=lambda kv: -len(kv[0])):
        if re.search(r"(?<![\w-])" + re.escape(word) + r"(?![\w-])", low):
            seen.append(word)
            if str(val) not in reg:
                bad.append(word)
    return {"ok": not bad, "spelled_found": sorted(seen),
            "grammar_size": len(SPELLED), "unbacked": bad}


# #267 (d) / K3 MAJOR-1 (iv).  The delivered lookahead `(?![\w.])` made a
# numeral IMMEDIATELY FOLLOWED BY A FULL STOP unscannable -- a published
# measurement at the end of a sentence sat in a blind spot.  The lookahead now
# bars only a word character, so `62208.` is scanned; and a leading minus is
# admitted where it is not part of an identifier, so the seam's negative
# witness values are scanned rather than skipped.
NUM_RE = re.compile(r"(?<![\w./-])-?\d[\d,]*(?:/\d+)?(?![\w])")


DIGEST_KEYS = ("sha256_12", "declared", "chain", "ledger_chain",
               "seal_manifest", "sealed", "order")
PURE_NUM = re.compile(r"^-?\d[\d,]*(?:/\d+)?$")


def paper_coverage(R, text, verdict):
    """E-22: coverage includes fenced blocks AND inline code spans; tables
    render as claims.  Nothing is stripped before the scan.  #267 (d): the
    registry is built from the MEASURED layer only -- no sha256, ledger-chain
    or seal-manifest token may back a numeral in the paper."""
    reg = set()
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


def paper_referents(text, refs):
    """THE SENTENCE-LEVEL REFERENT BINDING (#267 / the LOR-AID disease).  A
    numeral can be individually backed by the registry and still be false of
    the noun it stands in front of: four numerals drawn from four different
    collections compose into a sentence that contradicts the receipt on every
    clause while every one of them is in the registry.  So a declared set of
    REFERENT PHRASES -- each naming a quantity this run measures -- is bound
    here: wherever the paper writes a numeral immediately before one of those
    phrases, the numeral must be one this run measured FOR THAT PHRASE."""
    low = canon(text)
    bad = []
    seen = Counter()
    for (phrase, allowed) in refs:
        for m in re.finditer(r"(?<![\w./-])(\d[\d,]*)\s+" + re.escape(phrase),
                             low, re.I):
            seen[phrase] += 1
            v = int(m.group(1).replace(",", ""))
            if v not in allowed:
                bad.append({"referent": phrase, "found": v,
                            "measured": sorted(allowed)})
    absent = [p for (p, _a) in refs if not seen[p]]
    return {"ok": not bad and not absent, "referents": len(refs),
            "occurrences": sum(seen.values()), "unexercised": absent,
            "violations": bad}


FENCE_COPIES = 2


def paper_fences(text, verdict):
    """E-22, BLOCKS BY MULTISET.  Every fenced block of the paper is taken as
    a claim: each must be verbatim one of THIS RUN's verdict strings, and each
    verdict string must occur.  Containment alone is what E-22 was bought to
    kill -- an object carrying two copies of its verdict fence, one clean and
    one forged, satisfies containment while its twin is a forgery -- so the
    stray side is total here and admits no fenced block the run did not
    generate, whatever its prefix.

    TWO REPAIRS, both measured diseases.  (i) THE INFO STRING: the delivered
    regex matched ```` ```[a-zA-Z]* ````, so a block opened ```` ```txt1 ````
    -- an info string carrying a non-letter -- was INVISIBLE to this scanner,
    and a forged head carrying no new numeral was invisible to coverage as
    well.  Any info string is tokenised now.  (ii) THE MULTISET IS AN
    EQUALITY against a DECLARED MULTIPLICITY, not a containment: the delivered
    `got[k] < want[k]` admitted EXTRA copies of a legitimate fence, so a paper
    could carry a clean fence and a forged twin of it and satisfy the test.
    The paper renders each verdict string exactly twice -- once in the head and
    once in the verdict section -- and that count is what the multiset is
    compared against."""
    blocks = re.findall(r"```[^\n]*\n(.*?)```", text, re.S)
    got = Counter(norm(b) for b in blocks)
    want = Counter({norm(v): FENCE_COPIES for v in verdict})
    missing = [k[:60] for k in want if got[k] != want[k]]
    stray = [k[:60] for k in got if k not in want]
    return {"ok": got == want, "blocks": len(blocks),
            "distinct_blocks": len(got), "verdict_segments": len(verdict),
            "declared_copies_each": FENCE_COPIES,
            "multiset_equal": got == want,
            "missing": missing, "stray": stray}


def paper_rowset(text, claims):
    """THE TABLE SIDE, GATED BY EQUALITY AND NOT BY CONTAINMENT.

    G-PAPER-CLAIMS asks that every rendered row OCCUR in the paper.  That is
    containment, and containment is one-sided: a paper carrying every
    rendered row AND ONE MORE -- a forged data row whose every numeral is
    backed elsewhere, a duplicated legitimate row, a row of a table that does
    not exist -- satisfies it.  E-22's equality ruling was applied to the
    fenced blocks and not to the tables, and the stray row was measured to
    survive.  It does not survive this.

    Every DATA row of every markdown table outside a fenced block is
    collected -- each contiguous block's first line is its header and its
    second is the |---| separator, both gated elsewhere -- and the multiset of
    those rows is required to EQUAL the multiset of rendered table rows.  A
    stray row is a stray, a missing row is missing, and a duplicated row is a
    multiplicity mismatch."""
    rows, block, fenced = [], [], False
    for ln in text.split("\n"):
        if ln.lstrip().startswith("```"):
            fenced = not fenced
            continue
        s = ln.strip()
        if not fenced and s.startswith("|") and s.endswith("|"):
            block.append(s)
            continue
        if block:
            rows.extend(block[2:])
            block = []
    if block:
        rows.extend(block[2:])
    got = Counter(canon(r) for r in rows)
    want = Counter(canon(c["text"]) for c in claims
                   if c["id"].startswith("T-"))
    stray = [k[:70] for k in got if got[k] != want.get(k, 0)]
    missing = [k[:70] for k in want if want[k] != got.get(k, 0)]
    return {"ok": got == want, "paper_data_rows": sum(got.values()),
            "rendered_table_rows": sum(want.values()),
            "multiset_equal": got == want,
            "stray": stray, "missing": missing}


# E-24's FRACTION UNIVERSES, in the words the paper uses for them.  The
# delivered object sealed this list and no gate read it, so the stamp was a
# self-list: a key that says the right thing about a paper nobody compared it
# to.  The list is the gate's subject now (G-DECLARED-STANDARDS), and it is
# written in the paper's own phrasing so the comparison is a real one.
MEASURE_STAMP = "COUNTING-ONLY"
RATIO_FAMILIES = (
    "welding types of types",
    "welding gluings of gluings",
    "doubled-free gluings of gluings by k",
    "FORCED records of window records",
    "admitted cross-sector specifications of specifications",
)


# each row carries its OWN negation, so the gate tests the sign it names
# rather than a string edit that happens to be meaningful for one row.
# EXTENDED TO EVERY DIRECTION-BEARING SENTENCE THE HEAD ASSERTS.  The delivered
# object carried three rows, and seven measured flips survived them -- the
# alignment criterion inverted inside its own theorem block, the selector
# inverted in prose, the cross-sector kill inverted, the read-out inverted.
# Each of those is a row now, and each row's negation is the inversion a reader
# would actually be misled by rather than a token substitution.
POLARITY = [
    ("P1", "the union welds", "the union never welds"),
    ("P2", "the direct sum is a declaration",
     "the direct sum is a measurement"),
    ("P3", "the disjoint arm adds nothing",
     "the disjoint arm adds new structure"),
    ("P4", "every admitted one kills the dictionary",
     "no admitted one kills the dictionary"),
    ("P5", "k is not what selects", "k is what selects"),
    ("P6", "what selects is the ALIGNMENT", "what selects is k"),
    ("P7", "if and only if no shared pair is adjacent in BOTH sectors",
     "if and only if some shared pair is adjacent in BOTH sectors"),
    ("P8", "every shared pair must share a tripartite class on at least one "
           "side",
     "no shared pair may share a tripartite class on any side"),
    ("P9", "Two welded worlds glued by shared actors compose",
     "Two welded worlds glued by shared actors never compose"),
    ("P10", "The extended carrier repairs the seam by declaring away the "
            "thing the seam measures",
     "The extended carrier repairs the seam by measuring the thing the seam "
     "declares"),
    ("P11", "This unit publishes no probability and no percentage",
     "This unit publishes a probability"),
    ("P12", "stamped COUNTING-ONLY", "stamped MEASURE-DECLARED"),
    ("P13", "no sector-private link ever moves",
     "a sector-private link moves"),
    ("P14", "no repair of the free item is measured",
     "the repair of the free item is measured"),
    ("P15", "the fate is a property of the driven gluing and not of its type",
     "the fate is a property of the type"),
    # the unit's own central existence claim, and the sentence a forger who
    # adds no numeral and no table row would write to invert it
    ("P16", "the union's dictionary EXISTS",
     "The union carries no dictionary at any type"),
    ("P17", "These two fibers are rows of the DRIVEN GLUING, not of its type",
     "These two fibers are rows of the type"),
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


def finish(LD, SEAL, R, verdict, write=True, sweep_rows=None):
    """THE WRITER, and the only one.  Nothing here re-derives a measurement;
    what it does is bind the four things a delivered artifact can lie about --
    that a sweep ran, that the sealed values are the values written, that the
    walls hold over the WHOLE payload and not the part of it that existed when
    the wall gate ran, and that the bytes on disk are the bytes that passed."""
    if mut("MUT-SEAL-FORGE") and R.get("type_census"):
        # a sealed value moved BETWEEN its gate and the write: the exact shape
        # #119 was bought for, and the shape the delivered object could not see
        R["type_census"][0]["aut"] = 424242

    # ---- the sweep binding, taken on the SWEEP'S OWN ROWS -----------------
    # A boolean handed in by the caller is not evidence: the delivered object
    # accepted `swept=True` from a run that had executed no sweep at all.  The
    # binding is on the rows.  Two modes are declared and they exhaust the
    # callers: the DELIVERY mode, which writes and must carry one on-target row
    # per declared mutant, named exactly as the registry names them; and the
    # NON-WRITING mode, which promotes nothing and must therefore claim no
    # sweep at all.  A run that claims a sweep it did not take dies here in
    # either mode.
    if sweep_rows is None:
        mode, sweep_ok = "NON-WRITING", (not write)
        rows_on_target = 0
    else:
        mode = "DELIVERY"
        rows_on_target = sum(1 for r in sweep_rows if r["on_target"])
        sweep_ok = (write and len(sweep_rows) == len(MUTANTS)
                    and rows_on_target == len(MUTANTS)
                    and sorted(r["mutant"] for r in sweep_rows)
                    == sorted(MUTANT_NAMES))
    LD.gate("G-SWEEP-EXECUTED",
            sweep_ok,
            "the writer is downstream of a sweep that actually ran, and the "
            "binding is on the SWEEP'S OWN ROWS rather than on a flag: a "
            "delivery run carries one row per declared mutant, named as the "
            "registry names it and on target, and a run that writes nothing "
            "claims no sweep at all.  There is no third mode, so a caller "
            "cannot hand the writer a sweep it did not take",
            {"mode": mode, "mutants": len(MUTANTS),
             "rows": 0 if sweep_rows is None else len(sweep_rows),
             "rows_on_target": rows_on_target, "writes": bool(write)})
    R["sweep_binding"] = SEAL.seal("sweep_binding",
                                   {"mode": mode, "declared_mutants":
                                    len(MUTANTS), "rows_on_target":
                                    rows_on_target, "writes": bool(write)})

    # ---- the seals VERIFIED against the payload about to be written -------
    moved = SEAL.verify(R)
    LD.gate("G-SEAL-VERIFIED",
            not moved and len(SEAL.seals) > 0,
            "every sealed key is RE-DIGESTED FROM THE PAYLOAD ABOUT TO BE "
            "WRITTEN and compared against the digest taken at the moment its "
            "gate passed.  The delivered object published %s digests and "
            "compared them to nothing, so a value moved after its gate shipped "
            "beside a seal that contradicted it; here it dies before a byte "
            "reaches the disk" % "its",
            {"sealed_keys": len(SEAL.seals), "moved_after_their_gate": moved})

    # ---- the walls, over the WHOLE receipt --------------------------------
    # The in-run wall gate scans the receipt as it stands when it runs, which
    # is before the verdict, the reconstruction, the paper gates, the coverage
    # map and the totals exist.  This one scans everything, naming its two
    # exclusions: the provenance block, which carries other units' file names,
    # and the walls key itself, which carries the scanned term list.
    EXCL = ("provenance", "reads", "walls")
    EXCL_G = ("G-SOURCES", "G-CITED-NOT-READ", "G-ANCHORS")
    total_layer = json.dumps({k: v for k, v in R.items() if k not in EXCL},
                             default=str) + json.dumps(
        [{"gate": r["gate"], "statement": r["statement"],
          "evidence": r["evidence"]} for r in LD.rows
         if not r["gate"].startswith("G-WALL")
         and r["gate"] not in EXCL_G], default=str)
    if mut("MUT-WALL-TOTAL"):
        total_layer += " read here as a spacetime with a horizon"
    tscan = canon(total_layer).lower()
    thits = sorted({w for w in BARRED_TERMS if w in tscan})
    LD.gate("G-WALL-TOTAL",
            not thits,
            "the abstention walls are re-scanned over the COMPLETE receipt at "
            "the writer -- every published key and the statement and evidence "
            "of every non-wall gate this run evaluated, including the %d keys "
            "and the gate rows that did not exist when the in-run wall gate "
            "ran -- with the same named exclusions and no others: the keys %s "
            "and the gates %s, which are the PROVENANCE SURFACE and carry "
            "other units' file names.  The delivered object's wall scan "
            "covered the keys that happened to exist at its own position"
            % (len(R), ", ".join(EXCL), ", ".join(EXCL_G)),
            {"terms": len(BARRED_TERMS), "keys_scanned":
             len([k for k in R if k not in EXCL]),
             "gate_rows_scanned": len([r for r in LD.rows
                                       if not r["gate"].startswith("G-WALL")
                                       and r["gate"] not in EXCL_G]),
             "excluded_by_name": list(EXCL) + list(EXCL_G), "hits": thits})

    # ---- the manifest, total ----------------------------------------------
    manifest = SEAL.manifest()
    published = sorted(k for k in R
                       if k not in ("ledger", "gate_count", "seal_manifest",
                                    "ledger_chain"))
    published = published + ["ledger", "gate_count", "seal_manifest",
                             "ledger_chain"]
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
            "DECLARED-UNSEALED with its forcing, the two lists are DISJOINT, "
            "and the completeness check compares the manifest against the "
            "published key set rather than against the seals that happened to "
            "be taken",
            {"published": len(published), "sealed": len(manifest["sealed"]),
             "declared_unsealed": len(manifest["declared_unsealed"]),
             "overlap": sorted(set(manifest["sealed"])
                               & set(manifest["declared_unsealed"])),
             "missing": missing})
    # THE ANCHOR CONSUMER, NO LONGER A PHANTOM.  Every verbatim anchor row
    # publishes the gate that consumes it, and G-ANCHORS' own statement says
    # so -- but nothing compared that name against anything, so renaming a
    # consumer to a gate this run never emits survived.  The consumers cannot
    # be checked where the anchors are declared, because they run later; they
    # are checked HERE, against the ledger the run actually built.
    names_now = set(LD.names())
    anchor_gates = sorted({a["gate"] for a in R["anchors"]})
    if mut("MUT-ANCHOR-CONSUMER"):
        anchor_gates = ["G-NO-SUCH-GATE-AT-ALL"] + anchor_gates[1:]
    phantom = [g for g in anchor_gates if g not in names_now]
    LD.gate("G-ANCHOR-CONSUMERS",
            not phantom and len(anchor_gates) > 0,
            "every gate named as an anchor's CONSUMER is a gate this run "
            "actually emitted: the %d distinct consumer names the %d anchor "
            "rows publish are compared against the ledger's own gate names, "
            "so an anchor pointing at a gate that does not exist dies here "
            "rather than being believed because it was written down"
            % (len(anchor_gates), len(R["anchors"])),
            {"anchors": len(R["anchors"]), "consumer_gates": anchor_gates,
             "not_in_the_ledger": phantom})

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

    # THE LEDGER IS CLOSED HERE, ROWS AND HEAD TOGETHER.  The delivered object
    # published a ledger of the rows that existed at its own position beside a
    # chain head taken after three later gates, so a receipt-only verifier was
    # handed a head that did not belong to the chain it was given.
    R["ledger"] = [{"gate": r["gate"], "ok": r["ok"], "chain": r["chain"]}
                   for r in LD.rows]
    R["gate_count"] = len(LD.rows)
    R["seal_manifest"] = manifest
    R["ledger_chain"] = LD.chain[:16]
    txt = render(R, verdict, LD)
    payload = json.dumps(R, indent=1, sort_keys=True, default=str)
    if not write:
        return txt, payload, True

    # ---- STAGE, VERIFY, PROMOTE.  Nothing is written onto a destination -----
    # until the staged bytes have been read back and compared, and the probe
    # that says the comparison can fail is a REAL corruption on a REAL file
    # rather than a constant-true expression.
    stages = []
    try:
        s1 = _write_staged(OUT_TXT, txt)
        stages.append(s1)
        s2 = _write_staged(OUT_JSON, payload)
        stages.append(s2)
        want1 = hashlib.sha256(txt.encode()).hexdigest()
        want2 = hashlib.sha256(payload.encode()).hexdigest()
        got1 = hashlib.sha256(_open_recorded(s1, "ARTIFACT")).hexdigest()
        got2 = hashlib.sha256(_open_recorded(s2, "ARTIFACT")).hexdigest()
        # THE PROBE, AND IT FIRES.  A third staging file is written with a
        # corrupted copy of the transcript and read back through the same
        # accessor; the comparison MUST report a difference.  If it does not,
        # the comparison itself is broken and nothing is promoted.
        probe_path = OUT_TXT + ".probe"
        p = _write_staged(probe_path, txt + "FORGED")
        stages.append(p)
        probe_fires = (hashlib.sha256(_open_recorded(p, "ARTIFACT")).hexdigest()
                       != want1)
        os.remove(p)
        stages.remove(p)
        ok = probe_fires and got1 == want1 and got2 == want2
        if not ok:
            raise GateFail("G-INTEGRITY: the staged bytes differ from the "
                           "payload that passed the gates, or the corruption "
                           "probe did not fire; nothing was promoted")
        os.replace(s1, OUT_TXT)
        stages.remove(s1)
        os.replace(s2, OUT_JSON)
        stages.remove(s2)
    finally:
        # a failed write leaves NO staging behind and never touches the
        # destinations, so the previous artifacts are intact
        _unstage(stages)
    # the promoted bytes, re-read from their destinations
    d1 = hashlib.sha256(read_text_file(OUT_TXT, "ARTIFACT").encode()).hexdigest()
    d2 = hashlib.sha256(read_text_file(OUT_JSON,
                                       "ARTIFACT").encode()).hexdigest()
    ok = (d1 == want1 and d2 == want2)
    if not ok:
        raise GateFail("G-INTEGRITY: promoted bytes differ from the gate-time "
                       "seal")
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
        # MUT-SWEEP-FORGE hands the writer a sweep row set that is not this
        # run's own: a non-writing run claiming a complete on-target sweep.
        forged = None
        if name == "MUT-SWEEP-FORGE":
            forged = [{"mutant": m[0], "died_at": m[2], "declared": m[2],
                       "on_target": True} for m in MUTANTS]
        finish(LD, SEAL, R, V, write=False, sweep_rows=forged)
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
        # SHELL TRUTH, the right way round (K3 minor 2): a mutant that dies at
        # its declared gate is the INTENDED outcome and exits 0; a mutant that
        # survives, or dies somewhere else, exits 1.  The delivered convention
        # was inverted, so a wrapper using shell truth read a clean sweep as a
        # wall of failures.
        return 0 if got == want else 1
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
    # the sweep runs only where it can be BOUND: the delivery path is the only
    # writer, so it is the only path that carries a sweep.  Every other mode
    # promotes nothing and claims nothing (G-SWEEP-EXECUTED's NON-WRITING
    # mode), which is why `--numbers` no longer passes a flag it did not earn.
    sweep_rows = None
    if write:
        sweep_rows = []
        for (n, d, g) in MUTANTS:
            got = run_mutant(n)
            sweep_rows.append({"mutant": n, "died_at": got, "declared": g,
                               "on_target": got == g})
        if not all(r["on_target"] for r in sweep_rows):
            sys.stderr.write("MUTANT SWEEP OFF TARGET: %s\n"
                             % [r for r in sweep_rows if not r["on_target"]])
            return 1
        R["mutant_sweep"] = SEAL.seal("mutant_sweep", sweep_rows)
    else:
        SEAL.declare_unsealed("mutant_sweep",
                              "this mode promotes nothing, so it carries no "
                              "sweep and claims none: G-SWEEP-EXECUTED's "
                              "NON-WRITING mode")
        R["mutant_sweep"] = {"mode": "NON-WRITING", "rows": []}
    try:
        txt, payload, ok = finish(LD, SEAL, R, V, write=write,
                                  sweep_rows=sweep_rows)
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
