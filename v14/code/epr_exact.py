#!/usr/bin/env python3
"""EPR (paper-38) -- THE COMPLETENESS AUDIT.  EPR 1935 RUN INSIDE THE THEORY.

QUESTION (pin `v14/note-epr-pin.md`, sha256-12 b1e4cf9a8b9f, ledger #328).
Einstein, Podolsky and Rosen state two criteria: an ELEMENT OF REALITY exists
for a quantity predictable with certainty without disturbing the system, and a
description is COMPLETE when every such element has a counterpart in it.  This
unit formalises both as TOTAL EXACT PREDICATES on the committed finite arena
and MEASURES which of the theory's two descriptions passes them.

WHAT THIS FILE MEASURES, IN ORDER.

  SEC 1  MACHINERY -- gate ledger, total gate-time seal, text normaliser,
         numeral registry, falsifier hooks.
  SEC 2  PROVENANCE -- six pinned sources, sha256-12 verified; fifteen
         verbatim anchors bound to the gates that consume them, and the
         binding is CHECKED: a gate that names an anchor is required to have
         consumed it, and every named consumer must be a gate that ran.  The
         pre-registered outcome vocabulary is PARSED OUT OF THE PIN'S BYTES.
  SEC 3  THE ARENA -- AG(2,3), the three declared link directions, the 27
         co-division cells, and the link graph MEASURED (not assumed) to be
         complete tripartite with the undeclared fourth parallel class as its
         parts.
  SEC 4  THE CORPUS -- paper-21's 72 I7-STRICT triples, their 5,184 ordered
         concatenations and the 600 driven-window schedules; the record field
         n_l(x); its site-constancy measured per history.
  SEC 5  THE BLOCKS -- FAC's forced per-history decomposition, rebuilt from
         the geometry and history legs and gated ROW BY ROW against FAC's
         delivered receipt.
  SEC 6  THE PREDICATES -- EPR-REALITY and EPR-COMPLETE, with the
         no-disturbance clause formalised as SEC's adjudicated SEAM-CONFINED
         separation.  Declared, AST-located, digested and gated BEFORE any
         census row runs.
  SEC 7  MEASUREMENT 1 -- DOES EPR'S SEPARATION PREMISE EXIST HERE?  The
         complete 512-subset census and the corpus-wide block-pair census, in
         both declared localizations.
  SEC 8  THE TWO DESCRIPTIONS -- D-RECORD and D-SHADOW; the shadow ceiling
         theorem (the coin consumes n mod 3), proved STATE-FREE from two
         exact ring identities and the measured residue partition, then
         witnessed over the declared 64-state family and cross-checked over
         the parent's own 37-value alphabet; the five declared readings.
  SEC 9  MEASUREMENT 2 -- THE CERTAINTY-ELEMENT CENSUS on the 2x2 grid of
         declared localization x declared separation, with the counterpart
         check in each description.
  SEC 10 MEASUREMENT 3 -- E4, THE TWO REDUCTIONS: how many distinct
         descriptions the same record reality is assigned.
  SEC 11 MEASUREMENT 4 -- E3, THE NON-COMMUTING PAIR: the commutator census
         and the reading pairs that are not jointly declarable.
  SEC 12 MEASUREMENT 5 -- THE E5 AUDIT: does B's record move with the reading
         declared on A?  Rendered with the test-declaration duty.
  SEC 13 MEASUREMENT 6 -- THE BELL WALL: the corpus's standing verdict as a
         wall over this unit's own bytes, and the desiderata table.
  SEC 14 THE CONTROL ARMS -- every pre-registered outcome word emitted by the
         REAL head law on declared data, synthetic descriptions included.
  SEC 15 THE HEAD, derived twice by routes sharing no dispatcher, the paper
         instrument, and the closing battery.

SCOPE AND LANGUAGE.  The phrase "element of reality" appears in this unit ONLY
inside the formalised predicate and inside verbatim quotation of the 1935
paper -- and that confinement is a GATE over the paper's own bytes, not a
promise.  Every count is COUNTING-ONLY over a declared window (E-24).  No
sentence of this unit claims local realism, Bell evasion, or a vindicated
hidden-variable completion: v5 paper-14's verdict is a WALL, scanned against
this unit's own paper as voice-normalised patterns, and carried POSITIVELY --
the paper is required to state the standing verdict, so deleting it fails.

ARITHMETIC.  Exact only: Python integers, fractions.Fraction, and the ring
Z[w] carried as integer pairs.  There are no floats; an AST scan of this file
and a recursive type scan of the emitted receipt are gates.

RUNTIME INPUTS (#46/#91).  Exactly six committed files are read as SOURCES,
all sha-pinned by this unit's frozen declaration, plus exactly one file read
as the OBJECT UNDER TEST -- this unit's own paper.  No other repository state
is read and no subprocess is invoked, so the run is correct off-tree and with
no version control present.
"""

import ast
import hashlib
import json
import os
import re
import sys
from collections import Counter
from fractions import Fraction
from itertools import combinations, product

SELF = os.path.abspath(__file__)
REPO = os.path.abspath(os.path.join(os.path.dirname(SELF), os.pardir,
                                    os.pardir))
OUT_TXT = os.path.join(os.path.dirname(SELF), "epr_output.txt")
OUT_JSON = os.path.join(os.path.dirname(SELF), "epr_receipt.json")
PAPER_REL = "v14/paper-38-epr.md"


# ===========================================================================
# SECTION 1.  MACHINERY
# ===========================================================================

LINES = []
QUIET = False
MUT = None
READS = []
READS_BY_CATEGORY = {}
READ_CATEGORIES = ("SOURCE", "PAPER-UNDER-TEST")
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
    """the falsifier hook: `normal` unless this run is that named mutant."""
    return corrupted if MUT == name else normal


class Ledger:
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


LD = Ledger()


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
    ("SEAL-SCHEMA", "schema", "G-PROVENANCE-SHA-PINNED"),
    ("SEAL-PROVENANCE", "provenance", "G-PROVENANCE-SHA-PINNED"),
    ("SEAL-VERBATIM", "verbatim_anchors", "G-VERBATIM-ANCHORS-IN-SOURCE"),
    ("SEAL-CAVEAT", "sufficiency_caveat", "G-EPR-SUFFICIENCY-CAVEAT"),
    ("SEAL-OUTCOMES", "pre_registered_outcomes",
     "G-OUTCOMES-PARSED-FROM-THE-PIN"),
    ("SEAL-WINDOWS", "windows", "G-WINDOWS-DECLARED-WITH-THEIR-BOUNDS"),
    ("SEAL-ARENA", "arena", "G-LINK-GRAPH-MEASURED"),
    ("SEAL-CARRIER", "carrier", "G-CELL-IS-A-CO-DIVISION-PAIR"),
    ("SEAL-CORPORA", "corpora", "G-CORPUS-AGREES-WITH-FAC"),
    ("SEAL-BLOCKS", "blocks", "G-BLOCKS-AGREE-WITH-FAC"),
    ("SEAL-PREDICATES", "predicates", "G-PREDICATES-FROZEN-BEFORE-THE-CENSUS"),
    ("SEAL-SEPARATION", "separation", "G-SEPARATION-PREMISE-CENSUS"),
    ("SEAL-DESCRIPTIONS", "descriptions", "G-SHADOW-CEILING"),
    ("SEAL-SHADOW-THEOREM", "shadow_theorem",
     "G-SHADOW-CARRIES-NOTHING-AT-EVERY-STATE"),
    ("SEAL-READINGS", "readings", "G-READINGS-PARTITION-MEASURED"),
    ("SEAL-ANALYTIC", "analytic_legs", "G-THE-ANALYTIC-LEGS-MEASURED"),
    ("SEAL-CERTAINTY", "certainty", "G-CERTAINTY-CENSUS-PER-ARM"),
    ("SEAL-REDUCTIONS", "reductions", "G-E4-TWO-REDUCTIONS"),
    ("SEAL-CONJUGACY", "conjugacy", "G-CONJUGATE-PAIR-MEASURED"),
    ("SEAL-E5", "e5_audit", "G-E5-RECORD-DOES-NOT-MOVE"),
    ("SEAL-BELL", "bell", "G-BELL-DESIDERATA-BOUND"),
    ("SEAL-BELL-POSITIVE", "bell_wall_positive_leg",
     "G-BELL-WALL-STATED-IN-THE-PAPER"),
    ("SEAL-CONTROLS", "controls", "G-EVERY-OUTCOME-WORD-EMITTABLE"),
    ("SEAL-MEASURE", "measure_relativity", "G-PROBABILITY-EXACTLY-ONE"),
    ("SEAL-CLASSBIND", "class_binding", "G-CLASS-WORDS-BOUND-TO-PREDICATES"),
    ("SEAL-COUNTS", "counts", "G-HEAD-DERIVED-TWICE"),
    ("SEAL-VERDICT", "verdict", "G-HEAD-DERIVED-TWICE"),
    ("SEAL-WALLS", "walls", "G-WALLS-SCAN-THE-PAPER"),
    ("SEAL-PAPER-CLAIMS", "paper_claims", "G-PAPER-CLAIMS"),
    ("SEAL-PAPER-FENCES", "paper_fences", "G-PAPER-FENCES-MATCH-THE-VERDICT"),
    ("SEAL-PAPER-TABLES", "paper_tables", "G-PAPER-TABLES-WITH-HEADERS"),
    ("SEAL-ELEMENT", "element_of_reality",
     "G-ELEMENT-OF-REALITY-CONFINED"),
    ("SEAL-PAPER-COVERAGE", "paper_coverage", "G-PAPER-NUMERAL-COVERAGE"),
    ("SEAL-REFERENT", "referent_binding", "G-SENTENCE-REFERENT-BINDING"),
    ("SEAL-POLARITY", "polarity", "G-PAPER-CLAIM-POLARITY"),
    ("SEAL-COVERAGE", "coverage", "G-FALSIFIER-COVERAGE"),
    ("SEAL-REACHABILITY", "reachability", "G-FALSIFIER-REACHABILITY"),
    ("SEAL-WAIVERS", "waiver_ledger", "G-FALSIFIER-COVERAGE"),
    ("SEAL-MUTANTS", "mutants", "G-FALSIFIER-COVERAGE"),
    ("SEAL-MUTANT-SWEEP", "mutant_sweep", "G-SWEEP-IS-EXECUTION-BOUND"),
    ("SEAL-READSET", "read_set", "G-READS-DECLARED"),
    ("SEAL-CONSUMERS", "anchor_consumers", "G-ANCHOR-CONSUMERS-RAN"),
    ("SEAL-ARITHMETIC", "arithmetic", "G-VOUCHING-KEYS-SEALED"),
    ("SEAL-PYTHON", "python", "G-VOUCHING-KEYS-SEALED"),
    ("SEAL-GATES", "gates", "G-CLOSING-BATTERY-RAN"),
    ("SEAL-CLOSING", "closing_gates", "G-CLOSING-BATTERY-RAN"),
    ("SEAL-TOTALS", "totals", "G-CLOSING-BATTERY-RAN"),
    ("SEAL-TRANSCRIPT", "transcript_head",
     "G-TRANSCRIPT-SEALED-AT-THE-SNAPSHOT"),
]
# THE ONLY UNSEALED PUBLISHED KEYS.  Both are structural: the manifest is the
# list of seals itself and the payload digest is taken over the manifest.
# #119 says SEAL WHAT YOU VOUCH, so `arithmetic` and `python` -- which are
# testimony about the run -- are sealed at G-VOUCHING-KEYS-SEALED above, and
# the promotion-time totality check compares this list against the literal
# two, so growing it publishes nothing.
DECLARED_UNSEALED = ["seal_manifest", "payload_sha256_12"]


class Seal:
    def __init__(self):
        self.rows = []
        self.index = {}
        self.payload = None
        self.payload_sha = None

    def take(self, sid, obj):
        path = [p for s, p, _g in SEALED_PATHS if s == sid][0]
        at = [g for s, _p, g in SEALED_PATHS if s == sid][0]
        # FALSIFIER MUT-SEAL-DROP: one seal is not taken
        if mut("MUT-SEAL-DROP") and sid == "SEAL-COVERAGE":
            return
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


SEAL = Seal()


def read_text(rel, category):
    if category not in READ_CATEGORIES:
        raise GateFail("G-READS-DECLARED :: undeclared read category %r"
                       % category)
    path = os.path.abspath(os.path.join(REPO, rel))
    READS.append(rel)
    READS_BY_CATEGORY.setdefault(category, set()).add(path)
    with open(path, "r", encoding="utf-8") as fh:
        return fh.read()


def read_bytes(rel, category="SOURCE"):
    path = os.path.abspath(os.path.join(REPO, rel))
    READS.append(rel)
    READS_BY_CATEGORY.setdefault(category, set()).add(path)
    with open(path, "rb") as fh:
        return fh.read()


_FOLD = {"—": "--", "–": "-", "’": "'", "“": '"',
         "”": '"', "≤": "<=", "≥": ">=", "≠": "!=",
         "≡": "=", "×": "x", "₁": "1", "₂": "2",
         "₀": "0", "₃": "3", "₄": "4", "₅": "5",
         "ℓ": "l", "→": "->", "←": "<-", "⋅": "*",
         "²": "2", "³": "3", "≈": "~", "·": "*",
         "⊆": "subset", "∈": "in", "∑": "sum",
         "−": "-", " ": " ", "ω": "w", "ψ": "psi",
         "φ": "phi", "Σ": "Sigma", "∩": "cap",
         "∪": "cup", "∅": "empty", "⟨": "|", "⟩": ">"}

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
    for k in sorted(_FOLD):
        s = s.replace(k, _FOLD[k])
    return s


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def canon(s):
    return norm(ascii_fold(mdstrip(s).replace("*", "").replace("`", "")))


NEEDLE_FLOOR = 30


def match_needle(hay, needle):
    n = canon(needle)
    if len(n) < NEEDLE_FLOOR:
        raise GateFail("G-VERBATIM-ANCHORS-IN-SOURCE :: needle below the #62 "
                       "length floor: %r" % needle)
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


NUMWORDS = ("zero", "one", "two", "three", "four", "five", "six", "seven",
            "eight", "nine", "ten", "eleven", "twelve")
WORDNUM = dict({w: i for i, w in enumerate(NUMWORDS)},
               twice=2, thirteen=13, fourteen=14, fifteen=15, sixteen=16,
               seventeen=17, eighteen=18, nineteen=19, twenty=20, thirty=30,
               forty=40, fifty=50, sixty=60, seventy=70, eighty=80, ninety=90,
               hundred=100, thousand=1000)
# EVERY English token that can carry a number.  A token in this shape that is
# not in WORDNUM is a spelled numeral the scan cannot resolve, and the gate
# fails rather than passing it over in silence (K3 MINOR-4).
NUMBER_WORD_SHAPES = frozenset(WORDNUM) | frozenset((
    "hundreds", "thousands", "million", "millions", "billion", "billions",
    "dozen", "dozens", "score", "scores", "twentyone", "fortytwo",
    "first", "second", "third", "fourth", "fifth", "sixth", "seventh",
    "eighth", "ninth", "tenth", "eleventh", "twelfth", "thirteenth",
    "fourteenth", "fifteenth", "sixteenth", "seventeenth", "eighteenth",
    "nineteenth", "twentieth", "thirtieth", "fortieth", "fiftieth",
    "sixtieth", "seventieth", "eightieth", "ninetieth", "hundredth",
    "thousandth"))
# the ordinals that name a POSITION and never a count: they carry no value to
# resolve, so they are declared here rather than mapped to a number.
ORDINAL_WORDS = frozenset((
    "first", "second", "third", "fourth", "fifth", "sixth", "seventh",
    "eighth", "ninth", "tenth", "eleventh", "twelfth", "thirteenth",
    "fourteenth", "fifteenth", "sixteenth", "seventeenth", "eighteenth",
    "nineteenth", "twentieth", "thirtieth", "fortieth", "fiftieth",
    "sixtieth", "seventieth", "eightieth", "ninetieth", "hundredth",
    "thousandth"))


# ===========================================================================
# SECTION 2.  PROVENANCE -- THE PINNED SOURCES AND THE VERBATIM ANCHORS
# ===========================================================================
# Six committed files are read as SOURCES at digests frozen in this
# declaration.  The 1935 paper itself is the SOURCE OF RECORD: it is read as
# bytes and its digest verified, and the six wall quotes E1-E6 are matched
# VERBATIM in the pin's own bytes, where the orchestrator transcribed them
# from the original.  Both legs are published: the quote's presence in the
# pin is machine-checked, the pin's fidelity to the 1935 print is testimony.
#
# E7 -- EPR'S OWN SUFFICIENT-NOT-NECESSARY CAVEAT -- is NOT in the pin.  The
# pin's six anchors omitted it; the omission was found at adjudication and is
# repaired here.  Its needle is therefore matched in THIS PAPER'S own bytes,
# where the repair worker transcribed it from the print (p.777 col.2 running
# to p.778 col.1, immediately after the criterion E2), so the caveat cannot
# be dropped from the paper without failing a gate.  The pin's own anchor
# list is frozen and is not edited; the erratum is carried in the paper.

PIN_REL = "v14/note-epr-pin.md"
SOURCES = (
    (PIN_REL, "b1e4cf9a8b9f", "the pin: the question, the six wall quotes, "
     "the pre-registered outcome vocabulary"),
    ("v14/sources/epr-1935-physrev-47-777.pdf", "66b5deb150c4",
     "THE SOURCE OF RECORD: Einstein, Podolsky and Rosen, Physical Review "
     "47, 777 (1935), four pages, read in the original"),
    ("v14/note-sec-adjudication.md", "7a82ffe7168a",
     "SEC's adjudicated SEAM-CONFINED ruling: the no-disturbance clause"),
    ("v14/paper-20-coupling.md", "4824d190af73",
     "paper-20's committed machinery: the two declared menu readings, the "
     "coin, the residue the walk consumes"),
    ("v14/paper-33-aid.md", "ecdd3fbf1d06",
     "AID: what an actor is in this corpus, and its reading walls"),
    ("v5/relativistic-isp-v5-paper14-non-markovianity-and-bell-nonlocality.md",
     "820aafdf42e6", "v5 paper-14: the corpus's standing Bell verdict, this "
     "unit's WALL"),
)

# THE CITED PARENT.  FAC's delivered receipt (v14/code/fac_receipt.json at
# sha256-12 240bad74217a) is the source of the block decomposition.  It is
# NOT read at run time: FAC is under repair and its working-tree copy has
# drifted from the delivered digest, so reading it would be a moving
# reference (#91).  Its delivered values are carried here as a CITATION and
# every one of them is re-derived by this instrument and compared, quantity
# by quantity, at G-CORPUS-AGREES-WITH-FAC and G-BLOCKS-AGREE-WITH-FAC.
FAC_CITED = {
    "digest": "240bad74217a",
    "status": "candidate-under-repair",
    "arena": {"sites": 9, "declared_links": 3, "parallel_classes": 4,
              "groupings": 280, "saturating_groupings": 36,
              "strict_triples": 72, "flat_quadruples": 276,
              "window_schedules": 600, "actor_lattice": 21147,
              "arena_automorphism_order": 108},
    "carrier": {"cells": 27, "distinct_co_division_pairs": 27,
                "cells_with_exactly_two_actors": 27,
                "actors_in_that_many_cells": 9,
                "cell_to_pair_is_a_bijection": True},
    "corpora": {"C1_strict_triples": 72, "C2_concatenations": 5184,
                "C3_window_schedules": 600, "total_histories": 5856,
                "distinct_histories": 5784,
                "events_per_history": {"9": 72, "12": 600, "18": 5184},
                "C3_tags": {"W4-CLASS": 256, "W4-FLAT": 264,
                            "W4-SEEDFAN": 80}},
    "actor_census": {
        "histories": 5856, "lattice": 21147, "leg1_geometry_survivors": 6,
        "unique_at": 5852, "non_unique_at": 4,
        "cardinality_distribution": {"1": 5852, "2": 4},
        "inventory": {"AP-9-BLOCKS-9x1": 5856,
                      "AP-3-BLOCKS-3x3-PARALLEL-CLASS-ROW": 1,
                      "AP-3-BLOCKS-3x3-PARALLEL-CLASS-COL": 1,
                      "AP-3-BLOCKS-3x3-PARALLEL-CLASS-DIA": 1,
                      "AP-3-BLOCKS-3x3-PARALLEL-CLASS-ANT": 1},
        "non_unique_rows": [
            {"index": 5256, "corpus": "C3", "cardinality": 2,
             "admissible": ["AP-3-BLOCKS-3x3-PARALLEL-CLASS-ROW",
                            "AP-9-BLOCKS-9x1"]},
            {"index": 5341, "corpus": "C3", "cardinality": 2,
             "admissible": ["AP-3-BLOCKS-3x3-PARALLEL-CLASS-COL",
                            "AP-9-BLOCKS-9x1"]},
            {"index": 5426, "corpus": "C3", "cardinality": 2,
             "admissible": ["AP-3-BLOCKS-3x3-PARALLEL-CLASS-DIA",
                            "AP-9-BLOCKS-9x1"]},
            {"index": 5511, "corpus": "C3", "cardinality": 2,
             "admissible": ["AP-3-BLOCKS-3x3-PARALLEL-CLASS-ANT",
                            "AP-9-BLOCKS-9x1"]}]},
}

ANCHORS = (
    ("A-E1", PIN_REL, "G-CERTAINTY-CENSUS-PER-ARM",
     "every element of the physical reality must have a counterpart in the "
     "physical theory."),
    ("A-E2", PIN_REL, "G-PREDICATES-FROZEN-BEFORE-THE-CENSUS",
     "If, without in any way disturbing a system, we can predict with "
     "certainty (i.e., with probability equal to unity) the value of a "
     "physical quantity, then there exists an element of physical reality "
     "corresponding to this physical quantity."),
    ("A-E3", PIN_REL, "G-CONJUGATE-PAIR-MEASURED",
     "either (1) the quantum-mechanical description of reality given by the "
     "wave function is not complete or (2) when the operators corresponding "
     "to two physical quantities do not commute the two quantities cannot "
     "have simultaneous reality."),
    ("A-E4", PIN_REL, "G-E4-TWO-REDUCTIONS",
     "it is possible to assign two different wave functions (in our example "
     "psi_k and phi_r) to the same reality."),
    ("A-E5", PIN_REL, "G-E5-RECORD-DOES-NOT-MOVE",
     "This makes the reality of P and Q depend upon the process of "
     "measurement carried out on the first system, which does not disturb "
     "the second system in any way."),
    ("A-E6", PIN_REL, "G-BELL-DESIDERATA-BOUND",
     "we left open the question of whether or not such a description "
     "exists. We believe, however, that such a theory is possible."),
    # E7, the caveat the pin omitted, transcribed from the print and matched
    # in the paper's own bytes (p.777 col.2 -> p.778 col.1).
    ("A-E7", PAPER_REL, "G-EPR-SUFFICIENCY-CAVEAT",
     "It seems to us that this criterion, while far from exhausting all "
     "possible ways of recognizing a physical reality, at least provides us "
     "with one such way, whenever the conditions set down in it occur. "
     "Regarded not as a necessary, but merely as a sufficient, condition of "
     "reality, this criterion is in agreement with classical as well as "
     "quantum-mechanical ideas of reality."),
    ("A-SEAM", "v14/note-sec-adjudication.md",
     "G-PREDICATES-FROZEN-BEFORE-THE-CENSUS",
     "the union changes geometry only on links both sectors jointly own; no "
     "sector-private link ever moves."),
    ("A-READING-A", "v14/paper-20-coupling.md", "G-SHADOW-CEILING",
     "The menu at site x is the three link traversals and the weight q(l|x) "
     "is the post-coin Born weight"),
    ("A-READING-B", "v14/paper-20-coupling.md",
     "G-READINGS-PARTITION-MEASURED",
     "The weight q(l|x) is the division count"),
    ("A-MOD3", "v14/paper-20-coupling.md", "G-SHADOW-CEILING",
     "the walk consumes the count residue n mod 3, not the count."),
    ("A-DGBLIND", "v14/paper-20-coupling.md",
     "G-READINGS-PARTITION-MEASURED",
     "phase applied after the coin cannot enter that step's Born weights at "
     "all."),
    # the two wall sentences.  Their consumer is the POSITIVE leg: they are
    # matched in v5 paper-14's bytes here AND required to stand in this
    # paper's own bytes at G-BELL-WALL-STATED-IN-THE-PAPER, so the wall
    # cannot be satisfied by deleting the section that carries it.
    ("A-BELL-E1", "v5/relativistic-isp-v5-paper14-non-markovianity-and-bell-"
     "nonlocality.md", "G-BELL-WALL-STATED-IN-THE-PAPER",
     "ISP cannot satisfy Bell local causality and still reproduce the "
     "Tsirelson violation. It is Bell-nonlocal."),
    ("A-BELL-E2", "v5/relativistic-isp-v5-paper14-non-markovianity-and-bell-"
     "nonlocality.md", "G-BELL-WALL-STATED-IN-THE-PAPER",
     "ISP is no-signalling and parameter-independent; there is no "
     "superluminal causal influence in its dynamics."),
    ("A-AID", "v14/paper-33-aid.md", "G-BLOCKS-AGREE-WITH-FAC",
     "The corpus defines an actor as an identity that recurs in the record."),
)


CONSUMED = {}


def consume(gate, R):
    """THE ANCHOR-CONSUMER BINDING (K3 MINOR-10).  An anchor's `consumed_by`
    field is not decoration: the gate that names it calls this, the call is
    recorded, and the closing battery requires every anchor to have been
    consumed at a gate that actually ran.  Returns True only when every
    anchor naming this gate was found in its source's bytes."""
    rows = [r for r in R["verbatim_anchors"]["rows"]
            if r["consumed_by"] == gate]
    CONSUMED.setdefault(gate, set()).update(r["anchor"] for r in rows)
    return bool(rows) and all(r["found"] for r in rows)


def provenance(R, paper_text=""):
    say("SECTION 2.  PROVENANCE")
    rows, texts = [], {}
    for rel, want, why in SOURCES:
        raw = read_bytes(rel)
        got = hashlib.sha256(raw).hexdigest()[:12]
        # FALSIFIER MUT-SOURCE-DIGEST: a source's digest is reported as
        # something else
        got = pick("MUT-SOURCE-DIGEST", got, "000000000000") \
            if rel == PIN_REL else got
        rows.append({"path": rel, "sha256_12": got, "declared": want,
                     "agrees": got == want, "role": why})
        if rel.endswith(".pdf"):
            texts[rel] = None
        else:
            texts[rel] = raw.decode("utf-8")
    bad = [r["path"] for r in rows if not r["agrees"]]
    R["schema"] = {
        "unit": "EPR", "paper": PAPER_REL, "instrument": "v14/code/"
        + os.path.basename(SELF), "pin": PIN_REL,
        "pin_sha256_12": "b1e4cf9a8b9f",
        "receipt_keys_are_sealed_or_declared_unsealed": True}
    R["provenance"] = {
        "sources": rows, "count": len(rows),
        "source_of_record": "v14/sources/epr-1935-physrev-47-777.pdf",
        "source_of_record_testimony":
            "the four pages were read in the original by the orchestrator at "
            "pin time and again by the construction worker before a line of "
            "this instrument was written; the six wall quotes were verified "
            "against that print, and are machine-matched here against the "
            "pin's bytes, which is the leg a program can take",
        "subprocesses_invoked": 0, "repository_reads_outside_the_list": 0,
        "cited_parent": {
            "path": "v14/code/fac_receipt.json",
            "delivered_sha256_12": FAC_CITED["digest"],
            "status": FAC_CITED["status"],
            "why_not_read": "FAC is under repair and its working-tree copy "
                            "has drifted from the delivered digest; reading "
                            "it would be a moving reference (#91), so its "
                            "delivered values are CITED here and every one "
                            "of them is re-derived by this instrument and "
                            "compared quantity by quantity",
            "abstention_is_provable": "the read set below is recorded at the "
                                      "I/O layer and does not contain it",
            "worker_testimony": "the construction worker inspected both the "
                                "delivered receipt and the drifted "
                                "working-tree copy: every quantity this unit "
                                "consumes is identical in the two"}}
    LD.gate("G-PROVENANCE-SHA-PINNED",
            "EVERY SOURCE IS READ AT A FROZEN DIGEST (#91).  The committed "
            "files are declared with their sha256-12 prefixes and each is "
            "verified against the bytes actually read, per file; the source "
            "of record is the 1935 print itself, and the one parent under "
            "repair is cited rather than read",
            not bad, "sources %d, disagreements %s"
            % (len(rows), bad or "none"))
    SEAL.take("SEAL-SCHEMA", R)
    SEAL.take("SEAL-PROVENANCE", R)

    # the object under test is an anchor source too: E7 is matched in the
    # paper's own bytes, which is what makes the caveat undeletable.
    texts[PAPER_REL] = paper_text
    arows = []
    for name, rel, gate, needle in ANCHORS:
        hay = texts.get(rel)
        # FALSIFIER MUT-ANCHOR-E2: the reality criterion's needle is altered by
        # one word
        needle_used = pick("MUT-ANCHOR-E2", needle,
                           needle.replace("certainty", "probability")) \
            if name == "A-E2" else needle
        # FALSIFIER MUT-CONSUMER-PHANTOM: an anchor's consumer is re-pointed
        # at a gate that never ran, leaving its real consumer's other anchor
        # in place so the consuming gate still passes
        gate_used = pick("MUT-CONSUMER-PHANTOM", gate,
                         "G-A-GATE-THAT-NEVER-RAN") if name == "A-SEAM" \
            else gate
        found = bool(hay is not None and match_needle(hay, needle_used))
        arows.append({"anchor": name, "source": rel, "consumed_by": gate_used,
                      "found": found, "chars": len(canon(needle_used))})
    miss = [r["anchor"] for r in arows if not r["found"]]
    R["verbatim_anchors"] = {
        "rows": arows, "count": reg(len(arows)), "missing": miss,
        "floor_chars": NEEDLE_FLOOR,
        "note": "each anchor names the gate that consumes it, and the naming "
                "is load-bearing: that gate calls consume() and cannot pass "
                "without it, and G-ANCHOR-CONSUMERS-RAN requires every named "
                "consumer to be a gate this run actually ran"}
    LD.gate("G-VERBATIM-ANCHORS-IN-SOURCE",
            "THE WALL QUOTES ARE MATCHED IN THEIR SOURCES' BYTES.  %d "
            "anchors, each above the #62 length floor, each naming the gate "
            "that consumes it; the six EPR quotes E1-E6 are matched in the "
            "pin, where they were transcribed from the 1935 print, and E7 -- "
            "the caveat the pin omitted -- is matched in this paper's own "
            "bytes" % len(ANCHORS),
            not miss, "anchors %d, missing %s" % (len(arows), miss or "none"))
    SEAL.take("SEAL-VERBATIM", R)

    e7 = [r for r in arows if r["anchor"] == "A-E7"][0]
    # the caveat must be USED, not merely quoted: the sentence that draws the
    # consequence is required in the paper too, so the quotation cannot be
    # decorative.
    use = ("the criterion is silent where its conditions do not occur, and "
           "so is this unit")
    ptext = paper_text
    # FALSIFIER MUT-CAVEAT-UNUSED: the sentence that puts EPR's caveat to
    # work is deleted from the paper, leaving the quotation decorative
    if mut("MUT-CAVEAT-UNUSED"):
        ptext = ptext.replace("and so is this unit", "and so is the corpus")
    used = bool(ptext) and canon(use) in canon(ptext)
    R["sufficiency_caveat"] = {
        "anchor": "A-E7",
        "the_consequence_drawn_in_the_paper": use,
        "consequence_stated": used,
        "where_in_the_print": "p.777 col.2 running to p.778 col.1, "
                              "immediately after the criterion anchored as "
                              "E2",
        "matched_in": e7["source"], "found": e7["found"],
        "chars": reg(e7["chars"]),
        "why_it_binds": "EPR's criterion is explicitly SUFFICIENT and not "
                        "necessary, and explicitly applies whenever its "
                        "conditions occur; so its non-instantiation at the "
                        "pair localization decides nothing about what is or "
                        "is not there, and this unit says so",
        "pin_erratum": "the pin's six anchors omit this passage; the omission "
                       "was found at adjudication.  The pin is frozen and is "
                       "not edited: the caveat is restored here, matched in "
                       "the paper's own bytes, and the erratum is carried in "
                       "the paper's provenance section"}
    LD.gate("G-EPR-SUFFICIENCY-CAVEAT",
            "EPR'S OWN SUFFICIENT-NOT-NECESSARY CAVEAT IS CARRIED, VERBATIM, "
            "IN THIS PAPER.  The passage the pin omitted is transcribed from "
            "the print and matched in the paper's bytes, so the unit cannot "
            "report a non-instantiation as a verdict against EPR while "
            "leaving out the sentence in which they disclaim exactly that.  "
            "The quotation is required to be USED: the sentence that draws "
            "the consequence must stand in the paper as well",
            consume("G-EPR-SUFFICIENCY-CAVEAT", R) and used,
            "anchor A-E7 found in %s: %s, %d chars; consequence stated %s"
            % (e7["source"], e7["found"], e7["chars"], used))
    SEAL.take("SEAL-CAVEAT", R)

    pin = texts[PIN_REL]
    parsed = []
    for line in pin.split("\n"):
        m = re.match(r"^- (EPR-[A-Z-]+(?:<object>)?)(?: |$)", line.strip())
        if m:
            parsed.append(m.group(1))
    # FALSIFIER MUT-OUTCOME-TYPED: the outcome vocabulary is typed instead of
    # parsed
    parsed = pick("MUT-OUTCOME-TYPED", sorted(set(parsed)),
                  ["EPR-SHADOW-INCOMPLETE-RECORD-COMPLETE"])
    fams = []
    for w in parsed:
        fams.append(w[:-len("<object>")] if w.endswith("<object>") else w)
    R["pre_registered_outcomes"] = {
        "parsed_from": PIN_REL, "words": parsed, "families": sorted(fams),
        "count": len(parsed),
        "note": "the vocabulary is PARSED OUT OF THE PIN'S OWN BYTES; a word "
                "the head law returns must match one family exactly or "
                "extend an <object> family"}
    LD.gate("G-OUTCOMES-PARSED-FROM-THE-PIN",
            "THE OUTCOME VOCABULARY IS THE PIN'S, NOT THE INSTRUMENT'S.  The "
            "pre-registered words are parsed out of the pin's bytes and "
            "reduced to families; five words are expected and every one of "
            "them must be shown emittable by the real head law",
            len(parsed) == 5 and len(set(fams)) == 5,
            "words %s" % (parsed,))
    SEAL.take("SEAL-OUTCOMES", R)
    return texts


# ===========================================================================
# SECTION 3.  THE ARENA -- AG(2,3) AND ITS LINK GRAPH, MEASURED
# ===========================================================================

SITES = tuple((i, j) for i in range(3) for j in range(3))
SITE_INDEX = {s: k for k, s in enumerate(SITES)}
NACT = len(SITES)
I7_LINKS = ((1, 0), (0, 1), (1, 1))
CLASS_NAMES = ("ROW", "COL", "DIA", "ANT")
CLASS_DIR = {"ROW": (0, 1), "COL": (1, 0), "DIA": (1, 1), "ANT": (1, 2)}


def vadd(a, b):
    return ((a[0] + b[0]) % 3, (a[1] + b[1]) % 3)


def vmul(k, a):
    return ((k * a[0]) % 3, (k * a[1]) % 3)


def parallel_class(d):
    """the resolvable partition of AG(2,3) into the three lines of slope d."""
    H = frozenset({(0, 0), d, vmul(2, d)})
    seen, out = set(), []
    for x in SITES:
        L = tuple(sorted(vadd(x, h) for h in H))
        if L not in seen:
            seen.add(L)
            out.append(L)
    return tuple(sorted(out))


CLASSES = {k: parallel_class(CLASS_DIR[k]) for k in CLASS_NAMES}
CELLS = tuple((x, l) for x in SITES for l in I7_LINKS)
CELL_INDEX = {c: k for k, c in enumerate(CELLS)}
DIM = len(CELLS)


def codivision_pair(cell):
    """OCC's carrier typing, re-implemented rather than inherited: the cell IS
    the unordered co-division pair {x, x + l}."""
    x, l = cell
    return frozenset((x, vadd(x, l)))


CELL_PAIR = {k: codivision_pair(c) for k, c in enumerate(CELLS)}


def link_set():
    """the declared link directions; a parameter, so a synthetic arena runs
    through the same predicates (the control arm of section 14)."""
    # FALSIFIER MUT-LINKGRAPH: the undeclared direction is declared, so the
    # link graph is complete
    return pick("MUT-LINKGRAPH", I7_LINKS, I7_LINKS + (CLASS_DIR["ANT"],))


def linked(x, y, links=None):
    """x and y are LINKED exactly when some declared cell is the pair {x,y}:
    the arena's own conflict topology, not a metric."""
    if x == y:
        return False
    ls = I7_LINKS if links is None else links
    for l in ls:
        if vadd(x, l) == y or vadd(y, l) == x:
            return True
    return False


def arena_measure(R):
    say("SECTION 3.  THE ARENA")
    ls = link_set()
    deg = {x: sum(1 for y in SITES if linked(x, y, ls)) for x in SITES}
    parts = CLASSES["ANT"]
    tri_ok, tri_rows = True, []
    for x in SITES:
        for y in SITES:
            if x == y:
                continue
            same_part = any(x in L and y in L for L in parts)
            ok = (linked(x, y, ls) == (not same_part))
            tri_rows.append(ok)
            tri_ok = tri_ok and ok
    pairs = {CELL_PAIR[k] for k in range(DIM)}
    two_actor = sum(1 for k in range(DIM) if len(CELL_PAIR[k]) == 2)
    per_actor = Counter()
    for k in range(DIM):
        for a in CELL_PAIR[k]:
            per_actor[a] += 1
    # FALSIFIER MUT-CARRIER: the cell-to-pair bijection is asserted false
    bij = pick("MUT-CARRIER", len(pairs) == DIM and two_actor == DIM,
               False)
    R["arena"] = {
        "sites": reg(NACT), "declared_link_directions": reg(len(I7_LINKS)),
        "link_directions": [list(l) for l in I7_LINKS],
        "parallel_classes": reg(len(CLASS_NAMES)),
        "the_undeclared_direction": list(CLASS_DIR["ANT"]),
        "the_undeclared_class": "ANT",
        "degree_of_every_site": reg(sorted(set(deg.values()))[0]),
        "degrees_distinct": len(set(deg.values())),
        "link_graph_is_complete_multipartite_with_the_undeclared_class_as_"
        "parts": tri_ok,
        "ordered_site_pairs_checked": reg(len(tri_rows)),
        "parts": [[list(x) for x in L] for L in parts],
        "part_size": reg(3),
        "note": "the link graph is MEASURED, pair by ordered pair, against "
                "the undeclared class's own lines; nothing here is inherited"}
    LD.gate("G-LINK-GRAPH-MEASURED",
            "THE ARENA'S SEPARATION STRUCTURE IS A MEASUREMENT (#87).  Every "
            "one of the 72 ordered site pairs is tested: two sites are "
            "UNLINKED exactly when they lie on a common line of the one "
            "parallel class the arena does not declare, so the link graph is "
            "complete multipartite with those three lines as its parts and "
            "every site has degree six",
            tri_ok and len(set(deg.values())) == 1,
            "ordered pairs %d, all agree %s, degrees %s"
            % (len(tri_rows), tri_ok, sorted(set(deg.values()))))
    SEAL.take("SEAL-ARENA", R)
    R["carrier"] = {
        "cells": reg(DIM), "distinct_co_division_pairs": reg(len(pairs)),
        "cells_with_exactly_two_actors": reg(two_actor),
        "cells_per_actor": reg(sorted(set(per_actor.values()))[0]),
        "cell_to_pair_is_a_bijection": bij,
        "the_quantity_referent": "a record entry n_l(x) is indexed by a CELL, "
                                 "and the cell IS the unordered co-division "
                                 "pair {x, x+l}: its referent is a PAIR of "
                                 "actors, not one of them"}
    LD.gate("G-CELL-IS-A-CO-DIVISION-PAIR",
            "THE QUANTITY'S REFERENT IS RE-VERIFIED, NOT INHERITED.  The 27 "
            "cells are in bijection with the 27 unordered co-division pairs, "
            "every cell carries exactly two actors and every actor sits in "
            "exactly six cells -- this is what makes a record entry a "
            "quantity OF A PAIR, which is the whole hinge of measurement one",
            bij, "cells %d, pairs %d, two-actor cells %d, cells per actor %s"
            % (DIM, len(pairs), two_actor, sorted(set(per_actor.values()))))
    SEAL.take("SEAL-CARRIER", R)


# ===========================================================================
# SECTION 4.  THE CORPUS -- THE COMMITTED HISTORIES AND THEIR RECORD
# ===========================================================================
# The corpus is the parents': paper-21's 72 I7-STRICT triples (C1), their
# 5,184 ordered concatenations (C2) and the 600 driven-window schedules (C3),
# each rebuilt by its own constructor here and then gated against FAC's
# delivered receipt row by row.

RAW = {}


def all_groupings():
    out = []

    def rec(rem, acc):
        if not rem:
            out.append(tuple(acc))
            return
        a = rem[0]
        rest = rem[1:]
        for i in range(len(rest)):
            for j in range(i + 1, len(rest)):
                nr = tuple(z for k, z in enumerate(rest) if k not in (i, j))
                rec(nr, acc + [(a, rest[i], rest[j])])
    rec(SITES, [])
    return out


def round_vec(P):
    v = [0] * DIM
    for g in P:
        S = set(g)
        for k, (x, l) in enumerate(CELLS):
            if x in S and vadd(x, l) in S:
                v[k] += 1
    return v


def raw_census():
    if RAW:
        return RAW
    parts = all_groupings()
    vecs = [round_vec(P) for P in parts]
    RAW["parts"] = parts
    RAW["vecs"] = vecs
    RAW["sat"] = [i for i, v in enumerate(vecs) if sum(v) == NACT]
    return RAW


def strict_triples():
    C = raw_census()
    V = [C["vecs"][i] for i in C["sat"]]
    out = []
    for ia, a in enumerate(V):
        for ib, b in enumerate(V):
            ab = [a[k] + b[k] for k in range(DIM)]
            for ic, c in enumerate(V):
                if all(ab[k] + c[k] >= 1 for k in range(DIM)):
                    out.append((C["sat"][ia], C["sat"][ib], C["sat"][ic]))
    return out


def flat_quadruples():
    C = raw_census()
    V = [C["vecs"][i] for i in C["sat"]]
    tgt = [1, 1, 2] * NACT
    out = []
    for ia, a in enumerate(V):
        for ib, b in enumerate(V):
            ab = [a[k] + b[k] for k in range(DIM)]
            if any(ab[k] > tgt[k] for k in range(DIM)):
                continue
            for ic, c in enumerate(V):
                abc = [ab[k] + c[k] for k in range(DIM)]
                if any(abc[k] > tgt[k] for k in range(DIM)):
                    continue
                for idd, d in enumerate(V):
                    if all(abc[k] + d[k] == tgt[k] for k in range(DIM)):
                        out.append((C["sat"][ia], C["sat"][ib],
                                    C["sat"][ic], C["sat"][idd]))
    return out


def canon_transversals(P):
    return [tuple(sorted(g)[k] for g in P) for k in range(3)]


def history_of(rounds, seeds):
    H = []
    for P, sd in zip(rounds, seeds):
        order = sorted(range(len(P)), key=lambda gi: SITE_INDEX[sd[gi]])
        for gi in order:
            H.append(frozenset(P[gi]))
    return tuple(H)


COLLINEAR_FLAT = ("ROW", "COL", "DIA", "DIA")
COMMITTED_R4 = ("ROW", "COL", "ROW", "COL")


def window_schedules(flatq, parts):
    quads, tags = [], []
    for a in CLASS_NAMES:
        for b in CLASS_NAMES:
            for c in CLASS_NAMES:
                for d in CLASS_NAMES:
                    quads.append(tuple(CLASSES[k] for k in (a, b, c, d)))
                    tags.append("W4-CLASS")
    for q in flatq:
        quads.append(tuple(parts[i] for i in q))
        tags.append("W4-FLAT")
    quads.append(tuple(CLASSES[k] for k in COMMITTED_R4))
    tags.append("W4-CTRL")
    out, seen, meta = [], set(), []
    for T, tag in zip(quads, tags):
        menus = [canon_transversals(P)[:1] for P in T]
        for combo in product(*menus):
            sch = tuple(zip(T, combo))
            if sch in seen:
                continue
            seen.add(sch)
            out.append(sch)
            meta.append(tag)
    T = tuple(CLASSES[k] for k in COLLINEAR_FLAT)
    menus = [canon_transversals(P) for P in T]
    for combo in product(*menus):
        sch = tuple(zip(T, combo))
        if sch in seen:
            continue
        seen.add(sch)
        out.append(sch)
        meta.append("W4-SEEDFAN")
    return out, meta


def codivision(H):
    r = [[0] * NACT for _ in range(NACT)]
    for F in H:
        idx = sorted(SITE_INDEX[x] for x in F)
        for a in idx:
            for b in idx:
                if a != b:
                    r[a][b] += 1
    return r


def record_field(H):
    """THE RECORD n_l(x): the count of division events containing both the
    actor at x and the actor at x + l."""
    r = codivision(H)
    return tuple(r[SITE_INDEX[x]][SITE_INDEX[vadd(x, l)]] for (x, l) in CELLS)


def site_rows(n):
    return [tuple(n[SITE_INDEX[x] * 3 + i] for i in range(3)) for x in SITES]


def build_corpus():
    C = raw_census()
    parts = C["parts"]
    strict = strict_triples()
    flatq = flat_quadruples()
    scheds, smeta = window_schedules(flatq, parts)
    corp = []
    for t in strict:
        Ps = [parts[i] for i in t]
        corp.append(("C1", history_of(Ps, [canon_transversals(P)[0]
                                           for P in Ps])))
    c1h = [h for (_t, h) in corp]
    for a in c1h:
        for b in c1h:
            corp.append(("C2", a + b))
    for sch in scheds:
        corp.append(("C3", history_of([p for p, _s in sch],
                                      [s for _p, s in sch])))
    # FALSIFIER MUT-CORPUS-CAP: the corpus is silently capped
    if mut("MUT-CORPUS-CAP"):
        corp = corp[:5000]
    return corp, strict, flatq, scheds, smeta


def corpus_measure(R, fac):
    say("SECTION 4.  THE CORPUS")
    corp, strict, flatq, scheds, smeta = build_corpus()
    lens = Counter(len(h) for (_t, h) in corp)
    tags = Counter(t for (t, _h) in corp)
    nf = [record_field(h) for (_t, h) in corp]
    sc = [len(set(site_rows(n))) == 1 for n in nf]
    sc_ok = sum(1 for b in sc if b)
    # FALSIFIER MUT-SITECONST: one history's record is reported as not
    # site-constant
    if mut("MUT-SITECONST"):
        sc_ok -= 1
    rows = [site_rows(n)[0] for n in nf]
    fa = fac["arena"]
    fc = fac["corpora"]
    checks = [
        ("sites", NACT, fa["sites"]),
        ("declared_links", len(I7_LINKS), fa["declared_links"]),
        ("cells", DIM, fac["carrier"]["cells"]),
        ("strict_triples", len(strict), fa["strict_triples"]),
        ("flat_quadruples", len(flatq), fa["flat_quadruples"]),
        ("window_schedules", len(scheds), fa["window_schedules"]),
        ("groupings", len(raw_census()["parts"]), fa["groupings"]),
        ("saturating_groupings", len(raw_census()["sat"]),
         fa["saturating_groupings"]),
        ("C1", tags["C1"], fc["C1_strict_triples"]),
        ("C2", tags["C2"], fc["C2_concatenations"]),
        ("C3", tags["C3"], fc["C3_window_schedules"]),
        ("total_histories", len(corp), fc["total_histories"]),
        ("distinct_histories", len({h for (_t, h) in corp}),
         fc["distinct_histories"]),
    ]
    for k, v in sorted(lens.items()):
        checks.append(("events_" + str(k), v, fc["events_per_history"][str(k)]))
    for k, v in sorted(Counter(smeta).items()):
        if k in fc["C3_tags"]:
            checks.append(("tag_" + k, v, fc["C3_tags"][k]))
    bad = [c[0] for c in checks if c[1] != c[2]]
    R["corpora"] = {
        "histories": reg(len(corp)), "C1_strict_triples": reg(tags["C1"]),
        "C2_concatenations": reg(tags["C2"]),
        "C3_window_schedules": reg(tags["C3"]),
        "distinct_histories": reg(len({h for (_t, h) in corp})),
        "events_per_history": {str(k): reg(v) for k, v in sorted(lens.items())},
        "distinct_record_fields": reg(len(set(nf))),
        "distinct_site_rows": reg(len(set(rows))),
        "largest_count_in_the_corpus": reg(max(max(n) for n in nf)),
        "record_is_site_constant_at": reg(sc_ok),
        "of_histories": reg(len(corp)),
        "agreements_with_FAC": [{"quantity": a, "here": b, "FAC": c,
                                 "agrees": b == c} for a, b, c in checks],
        "FAC_status": "candidate-under-repair (SEC/FAC repairs in flight at "
                      "delivery); the receipt is read at its pinned digest "
                      "240bad74217a and every shared quantity is re-derived "
                      "here rather than imported"}
    LD.gate("G-CORPUS-AGREES-WITH-FAC",
            "THE COMMITTED CORPUS IS REBUILT AND CROSS-CHECKED PER QUANTITY "
            "(#87).  Every structural count of the arena and of the three "
            "corpora is derived by this instrument's own constructors and "
            "compared, one by one, with FAC's delivered receipt; the record "
            "field is then measured SITE-CONSTANT at every committed history, "
            "which is the fact the certainty census will live on",
            not bad,
            "cross-checks %d, disagreements %s; site-constant %d of %d"
            % (len(checks), bad or "none", sc_ok, len(corp)))
    LD.gate("G-RECORD-SITE-CONSTANT",
            "THE RECORD FIELD IS SITE-CONSTANT AT EVERY COMMITTED HISTORY, "
            "PER HISTORY.  n_l(x) does not depend on x: the nine site rows "
            "of a history are equal at all 5,856 of them.  This is a "
            "property of the committed window, not a law, and it is what "
            "makes separated prediction possible at all here",
            sc_ok == len(corp), "site-constant %d of %d histories"
            % (sc_ok, len(corp)))
    SEAL.take("SEAL-CORPORA", R)
    return corp, nf, rows


# ===========================================================================
# SECTION 5.  THE BLOCKS -- FAC'S FORCED PER-HISTORY DECOMPOSITION
# ===========================================================================
# A block decomposition is a law-compatible partition of the nine actors.
# FAC measured the admissible set at every committed history.  Here the two
# BINDING legs are rebuilt -- geometry (the link descends to the blocks) and
# history (every division event is a union of blocks) -- and the resulting
# census is gated against FAC's delivered rows, cardinality distribution,
# inventory and named exceptions.

def coset_partitions():
    """LEG-1's closed form: the link descends exactly along the coset
    partitions of the subgroups of AG(2,3)'s translation group."""
    out = {"AP-9-BLOCKS-9x1": tuple(sorted((x,) for x in SITES)),
           "AP-1-BLOCKS-1x9": (tuple(sorted(SITES)),)}
    for k in CLASS_NAMES:
        out["AP-3-BLOCKS-3x3-PARALLEL-CLASS-" + k] = CLASSES[k]
    return out


COSETS = coset_partitions()


def signature_blocks(H):
    sig = {}
    for x in SITES:
        sig.setdefault(tuple(1 if x in F else 0 for F in H), []).append(x)
    return tuple(sorted(tuple(sorted(v)) for v in sig.values()))


def leg_geometry(part, links=None):
    """LEG-1: the link descends to the blocks -- for every block b and every
    declared direction l, b + l is again a block."""
    ls = I7_LINKS if links is None else links
    B = [frozenset(b) for b in part]
    S = set(B)
    for b in B:
        for l in ls:
            if frozenset(vadd(x, l) for x in b) not in S:
                return False
    return True


def leg_history(part, H):
    """LEG-2: every division event is a union of blocks."""
    # FALSIFIER MUT-BLOCKS-DROP: the history leg is dropped, so coarse
    # decompositions survive
    if mut("MUT-BLOCKS-DROP"):
        return True
    for F in H:
        for b in part:
            inside = sum(1 for x in b if x in F)
            if inside not in (0, len(b)):
                return False
    return True


def blocks_measure(R, corp, fac):
    say("SECTION 5.  THE BLOCKS")
    geo = {nm: leg_geometry(pt) for nm, pt in COSETS.items()}
    adm = []
    for (_tag, h) in corp:
        ok = sorted(nm for nm, pt in COSETS.items()
                    if geo[nm] and leg_history(pt, h))
        adm.append(ok)
    card = Counter(len(a) for a in adm)
    inv = Counter()
    for a in adm:
        for nm in a:
            inv[nm] += 1
    nonuniq = [{"index": i, "corpus": corp[i][0], "cardinality": len(adm[i]),
                "admissible": adm[i]}
               for i in range(len(adm)) if len(adm[i]) > 1]
    fa = fac["actor_census"]
    checks = [("leg1_geometry_survivors", sum(1 for v in geo.values() if v),
               fa["leg1_geometry_survivors"]),
              ("unique_at", card.get(1, 0), fa["unique_at"]),
              ("non_unique_at", len(nonuniq), fa["non_unique_at"]),
              ("histories", len(adm), fa["histories"])]
    for k, v in sorted(fa["cardinality_distribution"].items()):
        checks.append(("cardinality_" + k, card.get(int(k), 0), v))
    for k, v in sorted(fa["inventory"].items()):
        checks.append(("inventory_" + k, inv.get(k, 0), v))
    facrows = sorted(fa["non_unique_rows"], key=lambda r: r["index"])
    rowbad = []
    for a, b in zip(nonuniq, facrows):
        if a["index"] != b["index"] or a["admissible"] != sorted(
                b["admissible"]) or a["corpus"] != b["corpus"]:
            rowbad.append(a["index"])
    bad = [c[0] for c in checks if c[1] != c[2]]
    R["blocks"] = {
        "source": "FAC (paper-35), forced per-history decomposition",
        "legs_rebuilt_here": ["LEG-1 GEOMETRY", "LEG-2 HISTORY"],
        "legs_cited_from_FAC": ["LEG-3 RECORD (non-binding on this corpus)",
                                "LEG-4 DYNAMICS (no census row differs)"],
        "geometry_survivors": reg(sum(1 for v in geo.values() if v)),
        "forced_at": reg(card.get(1, 0)), "of_histories": reg(len(adm)),
        "non_unique_at": reg(len(nonuniq)),
        "inventory": {k: reg(v) for k, v in sorted(inv.items())},
        "non_unique_rows": nonuniq,
        "agreements_with_FAC": [{"quantity": a, "here": b, "FAC": c,
                                 "agrees": b == c} for a, b, c in checks],
        "row_disagreements": rowbad,
        "the_forced_decomposition": "AP-9-BLOCKS-9x1, the nine singleton "
                                    "blocks, admissible at every committed "
                                    "history and alone at 5,852 of them"}
    LD.gate("G-BLOCKS-AGREE-WITH-FAC",
            "THE BLOCKS ARE THE PARENT'S, REBUILT AND GATED ROW BY ROW "
            "(#87).  The two binding legs are re-implemented here; the "
            "resulting per-history admissible sets reproduce FAC's "
            "cardinality distribution, its whole inventory and its four "
            "named exceptions at their own corpus indices, each compared "
            "individually; what an actor IS here is AID's own sentence, "
            "matched verbatim as A-AID",
            not bad and not rowbad and consume("G-BLOCKS-AGREE-WITH-FAC", R),
            "cross-checks %d, disagreements %s; exception rows %d, "
            "disagreements %s"
            % (len(checks), bad or "none", len(nonuniq), rowbad or "none"))
    SEAL.take("SEAL-BLOCKS", R)
    return adm


# ===========================================================================
# SECTION 6.  THE PREDICATES -- EPR'S TWO CRITERIA, FORMALISED
# ===========================================================================
# EPR-REALITY(q | D, B, sep): the description D predicts the quantity q of
# block B with probability exactly one from data lying outside B and, per
# SEC's adjudicated SEAM-CONFINED ruling, sharing no link with B.  "With
# probability exactly one" is rendered MEASURE-FREE: q is constant on the
# conditioning fibre, which is probability one under EVERY measure of full
# support on the declared corpus -- and section 9 verifies exactly that, as
# exact rationals, under two declared measures.
#
# EPR-COMPLETE(D): every pair (history, quantity) for which EPR-REALITY holds
# has a COUNTERPART in D -- D's own content determines its value.
#
# Both are TOTAL on their declared domains: every argument combination
# returns True or False, and the totality is itself a gate.

WPOW = ((1, 0), (0, 1), (-1, -1))          # w^0, w^1, w^2 in Z[w]
GN = tuple(tuple(2 if i != j else -1 for j in range(3)) for i in range(3))
_MENU_CACHE = {}


def zmul(z1, z2):
    a, b = z1
    c, d = z2
    return (a * c - b * d, a * d + b * c - b * d)


def zadd(z1, z2):
    return (z1[0] + z2[0], z1[1] + z2[1])


def absq(z):
    a, b = z
    return a * a - a * b + b * b


def loc_pair(S):
    """THE RECORD'S OWN LOCALIZATION (OCC's carrier typing, gated in section
    3): a cell belongs to the block only when the block owns BOTH its
    actors."""
    fs = frozenset(S)
    return tuple(k for k in range(DIM) if CELL_PAIR[k] <= fs)


def loc_walk(S):
    """THE STATE'S OWN LOCALIZATION (paper-20's coin): the cell (x, l) is
    read at site x, because D(x) = diag(w^{n_l(x)}) consumes it there --
    even though the cell's referent is the pair {x, x+l}."""
    return tuple(k for k, (x, _l) in enumerate(CELLS) if x in S)


def far_region(B, links=None):
    """the region that can condition without disturbing B: outside B and
    sharing no link with it."""
    fb = frozenset(B)
    return tuple(y for y in SITES
                 if y not in fb and not any(linked(y, b, links) for b in fb))


def sep_link_disjoint(A, B, links=None):
    """EPR'S OWN NO-DISTURBANCE CLAUSE, per SEC's SEAM-CONFINED ruling: the
    conditioning region shares no link with B."""
    # FALSIFIER MUT-SEPARATION-LEAK: link-disjointness is granted to every pair
    if mut("MUT-SEPARATION-LEAK"):
        return True
    return all(not linked(a, b, links) for a in A for b in B)


def sep_actor_disjoint(A, B, links=None):
    """the declared WEAKER separation: no shared actor, links allowed."""
    return not (set(A) & set(B))


def coin_apply(row, psi_site, order):
    """paper-20's site block of the coin, C(x) = G . D(x), at both declared
    orders; the post-coin amplitudes are the arena's menu."""
    if order == "GD":
        src = [zmul(psi_site[j], WPOW[row[j] % 3]) for j in range(3)]
        out = []
        for i in range(3):
            t = (0, 0)
            for j in range(3):
                t = zadd(t, zmul((GN[i][j], 0), src[j]))
            out.append(t)
        return out
    out = []
    for i in range(3):
        t = (0, 0)
        for j in range(3):
            t = zadd(t, zmul((GN[i][j], 0), psi_site[j]))
        out.append(zmul(t, WPOW[row[i] % 3]))
    return out


def shadow_menu(row, psi_site, order="GD"):
    """D-SHADOW's content at one site: the Born menu k_1(l|x) = q/M as exact
    rationals, or the declared empty value where the site carries no mass.
    The record enters ONLY through w^{n mod 3}: that is the ceiling."""
    # FALSIFIER MUT-SHADOW-INJECTIVE: the shadow is allowed to read the count
    # rather than its residue
    if mut("MUT-SHADOW-INJECTIVE"):
        return ("RAW",) + tuple(row)
    key = (tuple(row), tuple(psi_site), order)
    if key in _MENU_CACHE:
        return _MENU_CACHE[key]
    J = [absq(z) for z in coin_apply(row, psi_site, order)]
    M = sum(J)
    out = (("EMPTY-MENU",) if M == 0
           else tuple(Fraction(J[i], M) for i in range(3)))
    _MENU_CACHE[key] = out
    return out


def record_menu(row):
    """paper-20's Reading B: the weight is the division count itself."""
    M = sum(row)
    if M == 0:
        return ("EMPTY-MENU",)
    return tuple(Fraction(row[i], M) for i in range(3))


def curvature_of(row):
    """paper-20's own plaquette, at a site-constant record:
    F = n_(1,0) + n_(0,1) - n_(1,1) mod 3."""
    return (row[0] + row[1] - row[2]) % 3


def data_record(row, cellids):
    """D-RECORD's content on a region: the region's own record entries."""
    return tuple((k % 3, row[k % 3]) for k in sorted(cellids))


def data_shadow(row, region, psi_site):
    """D-SHADOW's content on a region: the Born menu at the region's sites."""
    return tuple(shadow_menu(row, psi_site) for _x in region)


def fiber(rows, keyf, row):
    """the conditioning fibre: every committed record the conditioning data
    cannot tell apart from this one.  TOTAL: every row lands in exactly one
    fibre, and the row itself is always in its own."""
    k = keyf(row)
    out = tuple(r for r in rows if keyf(r) == k)
    # FALSIFIER MUT-FIBER-ROWS: the conditioning fibre is truncated to its own
    # row, so every description carries everything
    if mut("MUT-FIBER-ROWS"):
        out = out[:1]
    return out


def epr_reality_at(qdir, fib):
    """EPR-REALITY: the quantity's value is the same at every record the
    conditioning data admits -- prediction with certainty."""
    # FALSIFIER MUT-CERT-CONSTANT-TRUE: the certainty predicate is made
    # constantly true
    if mut("MUT-CERT-CONSTANT-TRUE"):
        return True
    return len({r[qdir] for r in fib}) == 1


def epr_counterpart_at(qdir, own):
    """THE COUNTERPART CLAUSE: the description's own content at the block
    determines the value."""
    # FALSIFIER MUT-COUNTERPART-BLIND: the counterpart predicate is made
    # constantly true
    if mut("MUT-COUNTERPART-BLIND"):
        return True
    return len({r[qdir] for r in own}) == 1


PREDICATE_NAMES = ("loc_pair", "loc_walk", "far_region", "sep_link_disjoint",
                   "sep_actor_disjoint", "shadow_menu", "record_menu",
                   "data_record", "data_shadow", "fiber", "epr_reality_at",
                   "epr_counterpart_at")
FORBIDDEN_FREE = ("SEPARATION", "CENSUS", "ARMS", "VERDICT", "HEAD",
                  "CERTAINTY", "REDUCTIONS")


def freeze_predicates(R):
    say("SECTION 6.  THE PREDICATES")
    src = open(SELF, "r", encoding="utf-8").read()
    tree = ast.parse(src)
    found, digests, frees = {}, {}, {}
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name in PREDICATE_NAMES:
            seg = ast.get_source_segment(src, node)
            found[node.name] = True
            digests[node.name] = digest(seg)
            names = set()
            for sub in ast.walk(node):
                if isinstance(sub, ast.Name):
                    names.add(sub.id)
            frees[node.name] = sorted(n for n in names
                                      if n.isupper() and n not in
                                      ("DIM", "SITES", "CELLS", "CELL_PAIR",
                                       "WPOW", "GN", "MUT"))
    missing = [n for n in PREDICATE_NAMES if n not in found]
    leaks = sorted({n for f in frees.values() for n in f
                    if any(bad in n for bad in FORBIDDEN_FREE)})
    combined = digest("|".join("%s:%s" % (n, digests.get(n, "-"))
                               for n in PREDICATE_NAMES))
    tot = predicate_totality()
    R["predicates"] = {
        "names": list(PREDICATE_NAMES), "located_by": "AST over this file",
        "per_predicate_sha256_12": digests, "combined_sha256_12": combined,
        "free_upper_case_names": frees, "leaks": leaks,
        "totality_probes": reg(tot["probes"]),
        "totality_failures": reg(tot["failures"]),
        "no_disturbance_clause": "link-disjointness -- the conditioning "
                                 "region shares no link with the block, per "
                                 "SEC's adjudicated SEAM-CONFINED ruling",
        "certainty_is_measure_free": "constancy on the conditioning fibre; "
                                     "probability one under every measure of "
                                     "full support, verified exactly under "
                                     "two declared measures in section 9"}
    LD.gate("G-PREDICATES-FROZEN-BEFORE-THE-CENSUS",
            "THE TWO CRITERIA ARE DECLARED, LOCATED IN SOURCE, DIGESTED AND "
            "TOTAL BEFORE A CENSUS ROW RUNS.  Twelve predicate functions are "
            "found by AST in this file, digested individually and jointly, "
            "and their upper-case free names are required to contain no "
            "census product, so no predicate can consult the answer it "
            "decides; ALL TWELVE are then exercised on every argument "
            "combination of a declared probe set and required to return a "
            "boolean or a declared value at each.  The criterion this gate "
            "freezes is EPR's own, matched verbatim in the pin as A-E2, and "
            "the no-disturbance clause is SEC's ruling, matched as A-SEAM",
            not missing and not leaks and tot["failures"] == 0
            and consume("G-PREDICATES-FROZEN-BEFORE-THE-CENSUS", R),
            "predicates %d, missing %s, leaks %s, totality probes %d "
            "failures %d, combined digest %s"
            % (len(PREDICATE_NAMES), missing or "none", leaks or "none",
               tot["probes"], tot["failures"], combined))
    SEAL.take("SEAL-PREDICATES", R)
    return combined


def predicate_totality():
    """every predicate is exercised on every combination of a declared probe
    set: the empty block, singletons, linked pairs, unlinked pairs, lines and
    the whole arena, against every declared record row shape."""
    probes = failures = 0
    subsets = [(), (SITES[0],), (SITES[0], SITES[1]),
               tuple(CLASSES["ANT"][0]), tuple(CLASSES["ROW"][0]),
               tuple(SITES)]
    testrows = [(0, 0, 0), (1, 1, 1), (0, 4, 0), (1, 1, 2), (4, 0, 0)]
    for S in subsets:
        for T in subsets:
            for f in (sep_link_disjoint, sep_actor_disjoint):
                probes += 1
                if not isinstance(f(S, T), bool):
                    failures += 1
        for f in (loc_pair, loc_walk, far_region):
            probes += 1
            if not isinstance(f(S), tuple):
                failures += 1
        for row in testrows:
            probes += 1
            if not isinstance(shadow_menu(row, ((1, 0),) * 3), tuple):
                failures += 1
            probes += 1
            if not isinstance(data_record(row, loc_walk(S)), tuple):
                failures += 1
            probes += 1
            if not isinstance(record_menu(row), tuple):
                failures += 1
            probes += 1
            if not isinstance(data_shadow(row, S, ((1, 0),) * 3), tuple):
                failures += 1
    for row in testrows:
        fb = fiber(testrows, lambda r: r[0] % 3, row)
        for d in range(3):
            probes += 2
            if not isinstance(epr_reality_at(d, fb), bool):
                failures += 1
            if not isinstance(epr_counterpart_at(d, fb), bool):
                failures += 1
    # FALSIFIER MUT-TOTALITY: a predicate is declared partial
    if mut("MUT-TOTALITY"):
        failures += 1
    return {"probes": probes, "failures": failures}


# ===========================================================================
# SECTION 7.  MEASUREMENT 1 -- DOES EPR'S SEPARATION PREMISE EXIST HERE?
# ===========================================================================
# EPR's criterion needs two things at once: a QUANTITY of the block, and a
# conditioning region that shares no link with it.  This section asks whether
# any object of the committed arena carries both.  The complete lattice of
# 512 subsets is censused, then every block pair of every admissible
# decomposition of every committed history, in both declared localizations.

ALL_TRIPLES = tuple(frozenset(t) for t in combinations(SITES, 3))


def disturbance_census():
    """THE DYNAMICAL READING of EPR's no-disturbance clause.  The kinematic
    reading -- SEC's ruling -- forbids a shared link.  The dynamical one asks
    the weaker and more literal question: can an event confined to A change
    any record entry B owns?  A record entry of B is a cell with both actors
    in B, and an event increments a cell only when it contains both of that
    cell's actors, so the answer is measurable over EVERY event shape the
    arena admits rather than only over the ones the corpus happens to run."""
    probes = viol = confined = sighted = 0
    for _nm, blocks in sorted(COSETS.items()):
        for A, B in product(blocks, repeat=2):
            if A == B or (set(A) & set(B)):
                continue
            ib = loc_pair(B)
            fa = frozenset(A)
            for T in ALL_TRIPLES:
                # FALSIFIER MUT-DISTURBANCE-CONFINEMENT: the confinement
                # premise is dropped, so unconfined events are counted as
                # confined ones
                inA = True if mut("MUT-DISTURBANCE-CONFINEMENT") else T <= fa
                touches = any(CELL_PAIR[k] <= T for k in ib)
                if inA:
                    confined += 1
                    probes += len(ib)
                    if touches:
                        viol += 1
                elif touches:
                    sighted += 1
    return {"event_shapes": len(ALL_TRIPLES), "confined_events": confined,
            "cell_probes": probes, "disturbances": viol,
            "events_that_do_reach_a_block_quantity": sighted}


def separation_measure(R, corp, adm):
    say("SECTION 7.  MEASUREMENT 1 -- THE SEPARATION PREMISE")
    rows512 = []
    for m in range(512):
        S = tuple(SITES[i] for i in range(NACT) if (m >> i) & 1)
        rows512.append({"size": len(S), "pair_cells": len(loc_pair(S)),
                        "walk_cells": len(loc_walk(S)),
                        "far": len(far_region(S))})
    both_pair = [r for r in rows512 if r["pair_cells"] > 0 and r["far"] > 0]
    both_walk = [r for r in rows512 if r["walk_cells"] > 0 and r["far"] > 0]
    qb = [r for r in rows512 if r["pair_cells"] > 0]
    fr = [r for r in rows512 if r["far"] > 0]
    farsizes = Counter(r["far"] for r in rows512)

    # the theorem, machine-checked in its own terms
    thm_probes = thm_bad = 0
    for m in range(512):
        S = frozenset(SITES[i] for i in range(NACT) if (m >> i) & 1)
        thm_probes += 1
        inside_one_part = any(S <= frozenset(L) for L in CLASSES["ANT"])
        if far_region(S) and not inside_one_part:
            thm_bad += 1
        if loc_pair(S) and inside_one_part:
            thm_bad += 1

    dyn = disturbance_census()
    stats = Counter()
    per_dec = {}
    for i, (_tag, _h) in enumerate(corp):
        for nm in adm[i]:
            blocks = COSETS[nm]
            for A, B in product(blocks, repeat=2):
                if A == B:
                    continue
                ld = sep_link_disjoint(A, B)
                qp = len(loc_pair(B)) > 0
                qw = len(loc_walk(B)) > 0
                stats["ordered_block_pairs"] += 1
                stats["link_disjoint"] += ld
                stats["quantity_bearing_LOC_PAIR"] += qp
                stats["quantity_bearing_LOC_WALK"] += qw
                stats["PREMISE_LOC_PAIR"] += (ld and qp)
                stats["PREMISE_LOC_WALK"] += (ld and qw)
                d = per_dec.setdefault(nm, Counter())
                d["pairs"] += 1
                d["link_disjoint"] += ld
                d["quantity_bearing_LOC_PAIR"] += qp
                d["PREMISE_LOC_PAIR"] += (ld and qp)
                d["PREMISE_LOC_WALK"] += (ld and qw)
    R["separation"] = {
        "subset_lattice": reg(len(rows512)),
        "subsets_owning_a_record_quantity": reg(len(qb)),
        "subsets_with_a_nonempty_far_region": reg(len(fr)),
        "subsets_with_both": reg(len(both_pair)),
        "subsets_with_a_walk_quantity_and_a_nonempty_far_region":
            reg(len(both_walk)),
        "far_region_sizes": {str(k): reg(v)
                             for k, v in sorted(farsizes.items())},
        "theorem": "a set with a nonempty far region lies inside one part of "
                   "the link graph, and a part is an unlinked triple, so it "
                   "owns no cell: quantity-bearing and separated are "
                   "mutually exclusive at this arena",
        "theorem_probes": reg(thm_probes), "theorem_failures": reg(thm_bad),
        "ordered_block_pairs": reg(stats["ordered_block_pairs"]),
        "link_disjoint_block_pairs": reg(stats["link_disjoint"]),
        "quantity_bearing_at_LOC_PAIR": reg(
            stats["quantity_bearing_LOC_PAIR"]),
        "quantity_bearing_at_LOC_WALK": reg(
            stats["quantity_bearing_LOC_WALK"]),
        "premise_instances_at_LOC_PAIR": reg(stats["PREMISE_LOC_PAIR"]),
        "premise_instances_at_LOC_WALK": reg(stats["PREMISE_LOC_WALK"]),
        "per_decomposition": {k: {kk: reg(vv) for kk, vv in sorted(v.items())}
                              for k, v in sorted(per_dec.items())},
        "dynamical_no_disturbance": {k: reg(v) for k, v
                                     in sorted(dyn.items())},
        "the_two_readings_of_the_clause":
            "KINEMATIC (SEC's ruling, the pin's instruction): the "
            "conditioning region shares no link with the block -- "
            "instantiable with a block quantity at no object of this arena.  "
            "DYNAMICAL: no event confined to the conditioning region can "
            "change a record entry the block owns -- which actor-"
            "disjointness alone already secures, measured over every event "
            "shape the arena admits.  Both are run; the head is taken at the "
            "kinematic reading, which is the stronger one and the one the "
            "pin declares",
        "window": "COUNTING-ONLY over the declared corpus and the complete "
                  "512-subset lattice (E-24)"}
    LD.gate("G-SEPARATION-PREMISE-CENSUS",
            "EPR'S PREMISE IS MEASURED BEFORE IT IS USED, AT EVERY OBJECT "
            "(#87).  The complete lattice of 512 subsets is censused for a "
            "record quantity and for a nonempty far region, and every "
            "ordered block pair of every admissible decomposition of every "
            "committed history is tested for link-disjointness against the "
            "block's own quantities in both declared localizations.  At the "
            "record's own localization the two requirements never hold "
            "together; at the state's localization they hold at 105,408 "
            "pairs, and the difference is the localization, not the arena",
            len(both_pair) == 0 and thm_bad == 0
            and stats["PREMISE_LOC_PAIR"] == 0
            and stats["PREMISE_LOC_WALK"] > 0,
            "512-subset census: quantity-bearing %d, far-nonempty %d, both "
            "%d; theorem probes %d failures %d; block pairs %d, "
            "link-disjoint %d, premise at LOC-PAIR %d, at LOC-WALK %d"
            % (len(qb), len(fr), len(both_pair), thm_probes, thm_bad,
               stats["ordered_block_pairs"], stats["link_disjoint"],
               stats["PREMISE_LOC_PAIR"], stats["PREMISE_LOC_WALK"]))
    LD.gate("G-NO-DISTURBANCE-DYNAMICAL",
            "THE OTHER READING OF EPR'S CLAUSE IS MEASURED TOO, AND THE "
            "PROBE IS SIGHTED.  Over every event shape this arena admits, no "
            "event confined to an actor-disjoint region changes any record "
            "entry the other block owns -- so actor-disjointness alone "
            "already secures the dynamical form of 'without in any way "
            "disturbing'.  The test-declaration duty is discharged by the "
            "positive control in the same census: events that are NOT so "
            "confined DO reach a block's quantities, and are counted",
            dyn["disturbances"] == 0
            and dyn["events_that_do_reach_a_block_quantity"] > 0
            and dyn["confined_events"] > 0,
            "event shapes %d, confined events %d, cell probes %d, "
            "disturbances %d, events that do reach a block quantity %d"
            % (dyn["event_shapes"], dyn["confined_events"],
               dyn["cell_probes"], dyn["disturbances"],
               dyn["events_that_do_reach_a_block_quantity"]))
    SEAL.take("SEAL-SEPARATION", R)
    return stats


# ===========================================================================
# SECTION 8.  THE TWO DESCRIPTIONS
# ===========================================================================
# D-RECORD is the theory's own state: the committed history and the record
# field it writes.  D-SHADOW is the declared Born-menu coarse reading --
# paper-20's Reading A, the wave-function analogue.
#
# THE SHADOW CARRIES NOTHING, AT EVERY STATE, BY THEOREM.  The audit does not
# rest on which state is declared, and the state sweep is a WITNESS of a
# proved statement rather than its ground.  The proof has three legs, all of
# them exact and all of them state-free:
#
#   L1  w^{(n + c) mod 3} = w^c * w^{n mod 3} in Z[w] -- checked at all nine
#       (n, c) residue pairs.  With the coin's linearity this says that
#       shifting every count at a site by one c multiplies all three
#       post-coin amplitudes by the single phase w^c, AT EVERY STATE.
#   L2  |w^c z| = |z| -- absq(w^c * z) = absq(z), checked exactly over a
#       declared probe grid of Z[w].  So the Born modulus cannot see that
#       phase, and the menu partition COARSENS the residue partition at every
#       state whatever.
#   L3  the residue partition itself carries nothing: no residue class of
#       this corpus is a single record, and no residue class is constant in
#       any direction -- measured over the committed records.
#
# L1 + L2 + L3: at EVERY state, the shadow's own fibre at a block contains a
# whole residue class, which fixes no direction; so no certified element is
# carried, at any state.  The declared 64-state family then witnesses it, and
# the sweep over paper-20's own 37-value alphabet -- 50,653 states, where the
# ceiling of 9 menus is attained at 34,992 of them -- is published as the
# disclosure it is: the declared family caps at 4 menus, the parent's own
# alphabet reaches the ceiling, and the shadow carries 0 at both.

PSI_ALPHABET = ((0, 0), (1, 0), (0, 1), (-1, -1))
PSI_DECLARED = (("PSI-FLAT", ((1, 0), (1, 0), (1, 0))),
                ("PSI-BASIS", ((1, 0), (0, 0), (0, 0))),
                ("PSI-W", ((1, 0), (0, 1), (-1, -1))))
PSI_PRIMARY = PSI_DECLARED[0][1]
# paper-20's own discriminating alphabet: the elements of (1/3)Z[w] of
# modulus at most one, carried here as Z[w] elements of norm at most nine
# (the menu is invariant under a global scaling of the state vector).
PSI_PARENT_ALPHABET = tuple(sorted(
    (a, b) for a in range(-4, 5) for b in range(-4, 5)
    if a * a - a * b + b * b <= 9))
ZW_PROBE_GRID = tuple((a, b) for a in range(-6, 7) for b in range(-6, 7))

READINGS = ("READ-RECORD", "READ-BORN-GD", "READ-BORN-DG",
            "READ-RECORD-MENU", "READ-CURVATURE")


def reading_value(name, row, psi=PSI_PRIMARY):
    if name == "READ-RECORD":
        return ("REC",) + tuple(row)
    if name == "READ-BORN-GD":
        return ("BGD",) + tuple(shadow_menu(row, psi, "GD"))
    if name == "READ-BORN-DG":
        return ("BDG",) + tuple(shadow_menu(row, psi, "DG"))
    if name == "READ-RECORD-MENU":
        return ("RM",) + tuple(record_menu(row))
    if name == "READ-CURVATURE":
        return ("CURV", curvature_of(row))
    raise GateFail("G-READINGS-PARTITION-MEASURED :: undeclared reading %r"
                   % name)


def residue_class(row):
    """the site's residue vector modulo the uniform shift the Born modulus
    cannot see (a global phase on the site's three amplitudes)."""
    return min(tuple((row[i] - c) % 3 for i in range(3)) for c in range(3))


def menu_key(triple, pw):
    """the Born menu as a PROPORTIONALITY CLASS of exact integer weights --
    the same partition shadow_menu's rationals induce, computed from the
    site's residue triple and the state's pre-multiplied phases."""
    J = []
    for i in range(3):
        a = b = 0
        for j in range(3):
            g = GN[i][j]
            z = pw[j][triple[j]]
            a += g * z[0]
            b += g * z[1]
        J.append(a * a - a * b + b * b)
    g = J[0]
    for v in J[1:]:
        while v:
            g, v = v, g % v
        g = abs(g)
    return ("EMPTY-MENU",) if g == 0 else tuple(v // g for v in J)


def shadow_theorem(R, uniq, classes):
    """THE STATE-FREE PROOF, MACHINE-CHECKED, plus its two witnesses."""
    # L1: the coin's dependence on a count is w^{n mod 3}, and a uniform
    # shift of the three counts factors out as one phase -- nine probes.
    l1_probes = l1_bad = 0
    for n in range(3):
        for c in range(3):
            l1_probes += 1
            if WPOW[(n + c) % 3] != zmul(WPOW[c], WPOW[n % 3]):
                l1_bad += 1
    # L2: the Born modulus cannot see that phase -- an exact identity in
    # Z[w], checked over a declared probe grid.
    l2_probes = l2_bad = 0
    for z in ZW_PROBE_GRID:
        for c in range(3):
            l2_probes += 1
            if absq(zmul(WPOW[c], z)) != absq(z):
                l2_bad += 1
    # L3: the residue partition carries nothing.  A class that were a single
    # record, or constant in some direction, would let the shadow fix a value
    # -- neither happens, and this is what makes L1+L2 bite.
    singleton = [k for k, v in sorted(classes.items()) if len(v) == 1]
    dconst = [(str(k), d) for k, v in sorted(classes.items())
              for d in range(3) if len({z[d] for z in v}) == 1]
    # the residue classes ARE the global-shift orbits: measured, both ways,
    # over every ordered pair of committed records.
    orb_probes = orb_bad = 0
    for a in uniq:
        for b in uniq:
            orb_probes += 1
            shifted = any(all((a[j] + c) % 3 == b[j] % 3 for j in range(3))
                          for c in range(3))
            if shifted != (residue_class(a) == residue_class(b)):
                orb_bad += 1
    # FALSIFIER MUT-RESIDUE-CARRIES: the residue partition is reported as
    # carrying something, so the theorem's third leg is asserted rather than
    # measured
    if mut("MUT-RESIDUE-CARRIES"):
        singleton = singleton + ["A-PLANTED-SINGLETON-CLASS"]
    l3_holds = not singleton and not dconst and orb_bad == 0
    # WITNESS 1: the declared 64-state family, where the proportionality key
    # is checked to induce exactly shadow_menu's own partition.
    key_probes = key_bad = 0
    for ps in product(PSI_ALPHABET, repeat=3):
        pw = [[zmul(ps[j], WPOW[k]) for k in range(3)] for j in range(3)]
        direct, viakey = {}, {}
        for r in uniq:
            direct.setdefault(shadow_menu(r, ps, "GD"), []).append(r)
            viakey.setdefault(menu_key(tuple(r[j] % 3 for j in range(3)), pw),
                              []).append(r)
        key_probes += 1
        if (sorted(sorted(v) for v in direct.values())
                != sorted(sorted(v) for v in viakey.values())):
            key_bad += 1
    # WITNESS 2: the parent's own 37-value alphabet, swept whole.  At every
    # state the menu partition is computed and asked whether ANY of its cells
    # fixes a direction -- which is what "the shadow carries an element"
    # would need.  The distribution of distinct menus is published as the
    # disclosure that the declared family is not the widest one available.
    triples = sorted({tuple(r[j] % 3 for j in range(3)) for r in uniq})
    tindex = {t: i for i, t in enumerate(triples)}
    rowtri = [tindex[tuple(r[j] % 3 for j in range(3))] for r in uniq]
    sweep, best, bestpsi, carry, carry_states = Counter(), 0, None, 0, 0
    for ps in product(PSI_PARENT_ALPHABET, repeat=3):
        pw = [[zmul(ps[j], WPOW[k]) for k in range(3)] for j in range(3)]
        keys = [menu_key(t, pw) for t in triples]
        cells = {}
        for ri, ti in enumerate(rowtri):
            cells.setdefault(keys[ti], []).append(uniq[ri])
        sweep[len(cells)] += 1
        if len(cells) > best:
            best, bestpsi = len(cells), ps
        hit = sum(1 for v in cells.values() for d in range(3)
                  if len({z[d] for z in v}) == 1)
        carry += hit
        carry_states += bool(hit)
    R["shadow_theorem"] = {
        "statement": "at EVERY state whatever, the Born-menu partition "
                     "coarsens the residue partition, and no residue class "
                     "of this corpus is a single record or is constant in "
                     "any direction; so the shadow carries NONE of the "
                     "certified elements at every state, by theorem",
        "L1_phase_factors_out_probes": reg(l1_probes),
        "L1_failures": reg(l1_bad),
        "L2_the_modulus_is_phase_blind_probes": reg(l2_probes),
        "L2_failures": reg(l2_bad),
        "L3_residue_classes": reg(len(classes)),
        "L3_singleton_classes": reg(len(singleton)),
        "L3_direction_constant_classes": reg(len(dconst)),
        "L3_shift_orbit_probes": reg(orb_probes),
        "L3_shift_orbit_disagreements": reg(orb_bad),
        "witness_declared_family_states": reg(len(PSI_ALPHABET) ** 3),
        "witness_key_agrees_with_shadow_menu_at": reg(key_probes - key_bad),
        "witness_key_disagreements": reg(key_bad),
        "parent_alphabet_size": reg(len(PSI_PARENT_ALPHABET)),
        "parent_alphabet_states": reg(len(PSI_PARENT_ALPHABET) ** 3),
        "parent_alphabet_distinct_menu_counts": {
            str(k): reg(v) for k, v in sorted(sweep.items())},
        "parent_alphabet_best_distinct_menus": reg(best),
        "parent_alphabet_states_attaining_the_ceiling": reg(sweep[best]),
        "parent_alphabet_states_carrying_a_direction": reg(carry_states),
        "parent_alphabet_menu_cells_fixing_a_direction": reg(carry),
        "an_example_state_attaining_the_ceiling":
            [list(z) for z in bestpsi],
        "the_declared_family_is_not_the_widest": "the declared family "
            "{0, 1, w, w^2}^3 separates at most 4 menus; the parent's own "
            "alphabet reaches the ceiling of 9.  The carried count is 0 at "
            "both, which is the theorem and not a property of the family",
        "window": "COUNTING-ONLY; both state families are declared with "
                  "their bounds (E-24)"}
    ok = (l1_bad == 0 and l2_bad == 0 and l3_holds and key_bad == 0
          and carry == 0 and best == len(classes))
    LD.gate("G-SHADOW-CARRIES-NOTHING-AT-EVERY-STATE",
            "THE SHADOW'S ZERO IS A THEOREM, NOT A SWEEP RESULT.  Two exact "
            "ring identities -- the count enters the coin as w^{n mod 3} and "
            "a uniform shift factors out as one phase, and the Born modulus "
            "cannot see that phase -- put every Born-menu partition, at every "
            "state whatever, below the residue partition; and the residue "
            "partition is measured to carry nothing, with no class a single "
            "record and none constant in any direction.  The declared "
            "64-state family witnesses it and the parent's whole 37-value "
            "alphabet is swept as a cross-check: at none of its 50,653 "
            "states does any menu cell fix a direction",
            ok,
            "L1 probes %d failures %d; L2 probes %d failures %d; residue "
            "classes %d, singletons %d, direction-constant %d, shift-orbit "
            "disagreements %d of %d; key witness disagreements %d of %d; "
            "parent alphabet %d states, best %d menus at %d states, menu "
            "cells fixing a direction %d"
            % (l1_probes, l1_bad, l2_probes, l2_bad, len(classes),
               len(singleton), len(dconst), orb_bad, orb_probes, key_bad,
               key_probes, len(PSI_PARENT_ALPHABET) ** 3, best, sweep[best],
               carry))
    SEAL.take("SEAL-SHADOW-THEOREM", R)
    return best, sweep


def descriptions_measure(R, rows):
    say("SECTION 8.  THE TWO DESCRIPTIONS")
    uniq = sorted(set(rows))
    classes = {}
    for r in uniq:
        classes.setdefault(residue_class(r), []).append(r)
    sweep, best, bestpsi, seps = Counter(), 0, None, 0
    for ps in product(PSI_ALPHABET, repeat=3):
        m = {}
        for r in uniq:
            m.setdefault(shadow_menu(r, ps, "GD"), []).append(r)
        sweep[len(m)] += 1
        if len(m) > best:
            best, bestpsi = len(m), ps
        for v in classes.values():
            for a, b in combinations(v, 2):
                if shadow_menu(a, ps, "GD") != shadow_menu(b, ps, "GD"):
                    seps += 1
    prim = {}
    for r in uniq:
        prim.setdefault(shadow_menu(r, PSI_PRIMARY, "GD"), []).append(r)
    dg = {}
    for r in uniq:
        dg.setdefault(shadow_menu(r, PSI_PRIMARY, "DG"), []).append(r)
    declared = []
    for nm, ps in PSI_DECLARED:
        m = {}
        for r in uniq:
            m.setdefault(shadow_menu(r, ps, "GD"), []).append(r)
        declared.append({"state": nm, "distinct_menus": reg(len(m)),
                         "largest_fibre": reg(max(len(v)
                                                  for v in m.values()))})
    R["descriptions"] = {
        "D_RECORD": "the committed history and its record field n_l(x) -- "
                    "the theory's own state",
        "D_SHADOW": "paper-20's Reading A, the Born menu k_1(l|x) read off "
                    "the coin at the record -- the wave-function analogue",
        "distinct_records_in_the_corpus": reg(len(uniq)),
        "residue_classes_up_to_the_site_phase": reg(len(classes)),
        "largest_residue_class": reg(max(len(v) for v in classes.values())),
        "state_sweep_size": reg(len(PSI_ALPHABET) ** 3),
        "state_sweep_distinct_menu_counts": {str(k): reg(v) for k, v
                                             in sorted(sweep.items())},
        "best_distinct_menus_over_the_sweep": reg(best),
        "primary_state": PSI_DECLARED[0][0],
        "primary_distinct_menus": reg(len(prim)),
        "primary_largest_fibre": reg(max(len(v) for v in prim.values())),
        "primary_attains_the_sweep_maximum": len(prim) == best,
        "coin_order_DG_distinct_menus": reg(len(dg)),
        "declared_states": declared,
        "states_separating_two_records_of_one_residue_class": reg(seps),
        "ceiling": "the coin reads w^{n mod 3}, so two committed records "
                   "with equal residues have the SAME menu at every state: "
                   "proved state-free at G-SHADOW-CARRIES-NOTHING-AT-EVERY-"
                   "STATE and witnessed here at 0 separations over the "
                   "declared family's whole sweep",
        "what_this_sweep_is": "a WITNESS of the theorem below, not its "
                              "ground: the audit does not depend on which "
                              "state is declared, and the declared family is "
                              "reported with its own ceiling (4 menus) "
                              "beside the parent alphabet's (9)",
        "window": "COUNTING-ONLY; the state family is declared and its "
                  "bounds published (E-24)"}
    LD.gate("G-SHADOW-CEILING",
            "THE DECLARED STATE FAMILY WITNESSES THE THEOREM, AT ITS OWN "
            "BEST CASE.  Sixty-four states are swept; not one separates two "
            "committed records that share a residue class.  The primary "
            "state is required to attain this family's maximum, so the audit "
            "gives the shadow the best case the declared family has -- and "
            "the next gate shows the result does not depend on that at all.  "
            "The reading audited is paper-20's own, matched verbatim as "
            "A-READING-A, and the residue the walk consumes as A-MOD3",
            seps == 0 and len(prim) == best and len(classes) < len(uniq)
            and consume("G-SHADOW-CEILING", R),
            "records %d, residue classes %d, sweep %d states, best %d, "
            "primary %d, separations %d"
            % (len(uniq), len(classes), len(PSI_ALPHABET) ** 3, best,
               len(prim), seps))
    SEAL.take("SEAL-DESCRIPTIONS", R)
    shadow_theorem(R, uniq, classes)

    rfib, rrows = {}, {}
    for rd in READINGS:
        g = {}
        for r in uniq:
            g.setdefault(reading_value(rd, r), []).append(r)
        rfib[rd] = {r: tuple(g[reading_value(rd, r)]) for r in uniq}
        rrows[rd] = {"reading": rd, "cells": reg(len(g)),
                     "largest_fibre": reg(max(len(v) for v in g.values()))}
    ref = {}
    for a in READINGS:
        for b in READINGS:
            ref[(a, b)] = all(set(rfib[a][r]) <= set(rfib[b][r])
                              for r in uniq)
    conj = [(a, b) for a in READINGS for b in READINGS
            if a < b and not ref[(a, b)] and not ref[(b, a)]]
    R["readings"] = {
        "declared": list(READINGS),
        "count": reg(len(READINGS)),
        "ordered_pairs_compared": reg(len(READINGS) ** 2),
        "rows": [rrows[rd] for rd in READINGS],
        "refinement_matrix": {"%s|%s" % (a, b): ref[(a, b)]
                              for a in READINGS for b in READINGS},
        "not_jointly_declarable_pairs": ["%s|%s" % p for p in conj],
        "not_jointly_declarable_count": reg(len(conj)),
        "note": "a reading is a declared coarse-graining of the record; "
                "READ-RECORD refines every one of them, which is what makes "
                "D-RECORD the certifier of section 9"}
    LD.gate("G-READINGS-PARTITION-MEASURED",
            "THE FIVE DECLARED READINGS ARE MEASURED AS PARTITIONS, NOT "
            "ASSERTED.  Each reading's fibres over the committed records are "
            "enumerated, the refinement relation is computed in both "
            "directions for all twenty-five ordered pairs, and the pairs "
            "where neither refines the other are the corpus's conjugate "
            "pairs.  paper-20's other coin order is measured record-blind: "
            "one cell, every record in it -- which is that parent's own "
            "sentence, matched verbatim as A-DGBLIND, beside its record "
            "menu A-READING-B",
            len(conj) > 0 and rrows["READ-BORN-DG"]["cells"] == 1
            and ref[("READ-RECORD", "READ-BORN-GD")]
            and consume("G-READINGS-PARTITION-MEASURED", R),
            "readings %d, conjugate pairs %d, DG cells %d"
            % (len(READINGS), len(conj), rrows["READ-BORN-DG"]["cells"]))
    SEAL.take("SEAL-READINGS", R)
    return uniq, classes, rfib, conj, ref


# ===========================================================================
# SECTION 9.  MEASUREMENT 2 -- THE CERTAINTY-ELEMENT CENSUS
# ===========================================================================
# Four arms: the two declared localizations against the two declared
# separations.  In each, every ordered block pair of every admissible
# decomposition of every committed history is run through the frozen
# predicates, quantity by quantity.

LOCALIZATIONS = (("LOC-PAIR", loc_pair), ("LOC-WALK", loc_walk))
SEPARATIONS = (("SEP-LINK-DISJOINT", sep_link_disjoint),
               ("SEP-ACTOR-DISJOINT", sep_actor_disjoint))
ARM_OBJECT = {"LOC-PAIR": "THE-PAIR-LOCALIZED-BLOCK-QUANTITY",
              "LOC-WALK": "THE-WALK-LOCALIZED-BLOCK-QUANTITY"}


def arm_word(a):
    """THE HEAD LAW, applied per arm.  It reads only measured counts."""
    if a["totality_failures"] > 0:
        return "EPR-BLOCKED-AT-THE-PREDICATE-TOTALITY"
    if a["premise_instances"] == 0:
        return "EPR-CRITERION-INAPPLICABLE-AT-" + a["object"]
    if a["certainty_elements"] == 0:
        return "EPR-CRITERION-INAPPLICABLE-AT-THE-CERTAINTY-ELEMENT"
    if a["without_counterpart_in_D_RECORD"] > 0:
        return "EPR-RECORD-ALSO-INCOMPLETE"
    if a["without_counterpart_in_D_SHADOW"] > 0:
        return "EPR-SHADOW-INCOMPLETE-RECORD-COMPLETE"
    return "EPR-BOTH-COMPLETE"


def pair_specs(locf, septest):
    """the (decomposition, ordered block pair) spec list: computed once, so
    the census loop is a lookup rather than a re-derivation."""
    out = {}
    for nm, blocks in COSETS.items():
        spec = []
        for A, B in product(blocks, repeat=2):
            if A == B or not septest(A, B):
                continue
            qs = locf(B)
            if not qs:
                continue
            spec.append((tuple(sorted({k % 3 for k in locf(A)})),
                         tuple(sorted({k % 3 for k in locf(B)})),
                         tuple(sorted(k % 3 for k in qs))))
        out[nm] = spec
    return out


ARENA_BUILDERS = ("build_corpus", "record_field", "codivision", "history_of",
                  "window_schedules", "leg_history", "leg_geometry",
                  "signature_blocks", "round_vec", "strict_triples")
READING_NAMES_IN_SOURCE = ("READINGS", "reading_value", "shadow_menu",
                           "record_menu", "curvature_of", "rd")


def analytic_legs(R, uniq, classes):
    """WHAT THE CENSUS CANNOT PUT AT RISK.  Three columns of the census are
    settled before it runs, and this measures exactly how far that goes: the
    record's counterpart zero is the counterpart predicate's own DOMAIN, the
    both-complete branch is closed by the residue ceiling at every declared
    state, and the E5 zero is forced because nothing that builds a history
    takes a reading.  All three are disclosed rather than left to be read off
    as findings."""
    specs = qs_in_db = qs_in_da = 0
    for _locname, locf in LOCALIZATIONS:
        for _sepname, septest in SEPARATIONS:
            for _nm, spec in sorted(pair_specs(locf, septest).items()):
                for (da, db, qs) in spec:
                    specs += 1
                    # FALSIFIER MUT-SPEC-DOMAIN: the containment that makes
                    # the record's counterpart zero analytic is left
                    # unmeasured
                    if mut("MUT-SPEC-DOMAIN"):
                        continue
                    qs_in_db += set(qs) <= set(db)
                    qs_in_da += set(qs) <= set(da)
    # the both-complete branch: at every declared state, count the (record,
    # direction) pairs the shadow's own fibre FAILS to fix.  A state at which
    # this reached zero would open EPR-BOTH-COMPLETE; the minimum is the
    # measurement, and by the theorem above it is 108 at every state.
    permin = None
    for ps in product(PSI_ALPHABET, repeat=3):
        cells = {}
        for r in uniq:
            cells.setdefault(shadow_menu(r, ps, "GD"), []).append(r)
        fails = sum(1 for v in cells.values() for _r in v for d in range(3)
                    if len({z[d] for z in v}) > 1)
        permin = fails if permin is None else min(permin, fails)
    src = open(SELF, "r", encoding="utf-8").read()
    tree = ast.parse(src)
    leak = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name in ARENA_BUILDERS:
            for sub in ast.walk(node):
                if isinstance(sub, ast.Name) and \
                        sub.id in READING_NAMES_IN_SOURCE:
                    leak.append("%s/%s" % (node.name, sub.id))
                if isinstance(sub, ast.arg) and \
                        sub.arg in READING_NAMES_IN_SOURCE:
                    leak.append("%s/arg:%s" % (node.name, sub.arg))
    R["analytic_legs"] = {
        "declared_specs": reg(specs),
        "specs_where_the_quantity_lies_in_the_block_s_own_directions":
            reg(qs_in_db),
        "specs_where_the_quantity_lies_in_the_conditioner_s_directions":
            reg(qs_in_da),
        "RECORD_COMPLETE_is_analytic":
            "a censused quantity of a block is BY CONSTRUCTION one of the "
            "directions the block's own localization carries, so D-RECORD's "
            "content at the block always fixes the value being predicted: "
            "without_counterpart_in_D_RECORD is identically zero on any "
            "arena whatever, and only the punctured control of section 14 -- "
            "which deletes a direction from the description by hand -- can "
            "move it",
        "CERTIFICATION_is_total_for_the_same_reason":
            "the same containment holds against the CONDITIONER's directions, "
            "so certified equals quantities on every arm; the two equal "
            "columns of the census table are this containment, not a finding",
        "BOTH_COMPLETE_is_closed_before_the_run":
            "the shadow's own fibre fails to fix a direction at every "
            "(record, direction) pair of every declared state; the minimum "
            "over the declared family is published below and is nonzero, so "
            "no declared state could have returned EPR-BOTH-COMPLETE here",
        "minimum_unfixed_pairs_over_the_declared_states": reg(permin),
        "records": reg(len(uniq)), "residue_classes": reg(len(classes)),
        "the_reading_has_no_path_into_the_history":
            "a reading in this unit is a FUNCTION ON RECORDS, not an "
            "operation on a history: no function that builds the arena, the "
            "corpus, the record field or the blocks takes a reading or names "
            "one, which is checked by AST below.  The E5 zero is therefore "
            "forced by the formalisation and would be returned on any arena; "
            "what the declared falsifier establishes is that no leak was "
            "introduced by accident, not that the arena forbids one",
        "arena_builders_scanned": list(ARENA_BUILDERS),
        "reading_names_found_in_them": sorted(set(leak)),
        "the_live_selector": "two-way at this corpus: the head law's "
                             "record-incomplete branch cannot fire on "
                             "unmutated data and its both-complete branch is "
                             "closed by the ceiling, so what the census "
                             "measures is one column -- the shadow's",
        "window": "COUNTING-ONLY over the declared spec list and the declared "
                  "state family (E-24)"}
    LD.gate("G-THE-ANALYTIC-LEGS-MEASURED",
            "WHAT THE CENSUS COULD NOT HAVE FOUND IS MEASURED AND PUBLISHED "
            "BEFORE IT RUNS (#299/#319).  Every declared spec is checked for "
            "the containment that makes the record's counterpart zero "
            "analytic and certification total; the both-complete branch is "
            "shown closed at every declared state by the residue ceiling; and "
            "the arena's own constructors are scanned by AST for any mention "
            "of a reading, because that absence is what forces the E5 zero.  "
            "The selector this unit really turns on is therefore two-way, and "
            "the paper says so",
            specs > 0 and qs_in_db == specs and qs_in_da == specs
            and permin > 0 and not leak,
            "specs %d, quantity in the block's own directions %d, in the "
            "conditioner's %d; minimum unfixed (record, direction) pairs over "
            "the declared states %d; arena builders %d, reading names found "
            "in them %s"
            % (specs, qs_in_db, qs_in_da, permin, len(ARENA_BUILDERS),
               sorted(set(leak)) or "none"))
    SEAL.take("SEAL-ANALYTIC", R)


def certainty_measure(R, corp, adm, uniq, classes, tot):
    say("SECTION 9.  MEASUREMENT 2 -- THE CERTAINTY-ELEMENT CENSUS")
    analytic_legs(R, uniq, classes)
    FR = {}
    for dd in ((), (0,), (1,), (2,), (0, 1), (0, 2), (1, 2), (0, 1, 2)):
        for r in uniq:
            FR[(dd, r)] = fiber(uniq, lambda z, dd=dd: tuple(z[d] for d in dd),
                                r)
    FS = {r: fiber(uniq, lambda z: shadow_menu(z, PSI_PRIMARY), r)
          for r in uniq}
    arms = []
    for locname, locf in LOCALIZATIONS:
        for sepname, septest in SEPARATIONS:
            specs = pair_specs(locf, septest)
            cache = {}
            for nm, spec in specs.items():
                for si, (da, db, qs) in enumerate(spec):
                    for r in uniq:
                        fr = FR[(da, r)]
                        fs = FS[r]
                        ownr = FR[(db, r)]
                        owns = FS[r]
                        cq = cr = cs = nr = ns = ss = 0
                        for d in qs:
                            cq += 1
                            if epr_reality_at(d, fr):
                                cr += 1
                                if not epr_counterpart_at(d, ownr):
                                    nr += 1
                                if not epr_counterpart_at(d, owns):
                                    ns += 1
                            if epr_reality_at(d, fs):
                                cs += 1
                                if epr_counterpart_at(d, owns):
                                    ss += 1
                        cache[(nm, si, r)] = (cq, cr, cs, nr, ns, ss)
            pairs = quant = cr = cs = nr = ns = ss = 0
            for i, (_tag, _h) in enumerate(corp):
                r = ROWCACHE[i]
                for nm in adm[i]:
                    spec = specs[nm]
                    for si in range(len(spec)):
                        c = cache[(nm, si, r)]
                        pairs += 1
                        quant += c[0]
                        cr += c[1]
                        cs += c[2]
                        nr += c[3]
                        ns += c[4]
                        ss += c[5]
            a = {"localization": locname, "separation": sepname,
                 "object": ARM_OBJECT[locname],
                 "premise_instances": reg(pairs),
                 "quantities": reg(quant),
                 "certainty_elements": reg(cr),
                 "certainty_elements_certified_by_D_SHADOW": reg(cs),
                 "without_counterpart_in_D_RECORD": reg(nr),
                 "without_counterpart_in_D_SHADOW": reg(ns),
                 "shadow_self_certified_and_carried": reg(ss),
                 "totality_failures": tot}
            a["word"] = arm_word(a)
            arms.append(a)
            say("    %-9s %-19s pairs %-8d quantities %-8d certified %-8d "
                "no counterpart in the shadow %-8d -> %s"
                % (locname, sepname, pairs, quant, cr, ns, a["word"]))
    R["certainty"] = {
        "arms": arms,
        "certifier": "D-RECORD, the theory's own state: an element of "
                     "reality is certified when the record's content on the "
                     "separated region fixes the quantity's value",
        "counterpart_reading": "the description's own content AT THE BLOCK "
                               "determines the value",
        "self_certified_arm": "the shadow's own certainty elements are "
                              "counted too, and are carried by the shadow "
                              "wherever they exist -- a coarse description "
                              "is complete about what it can itself predict, "
                              "which is why the cross-description reading is "
                              "the contentful one",
        "window": "COUNTING-ONLY over the declared corpus (E-24)"}
    prim = [a for a in arms if a["localization"] == "LOC-PAIR"
            and a["separation"] == "SEP-LINK-DISJOINT"][0]
    walk = [a for a in arms if a["localization"] == "LOC-WALK"
            and a["separation"] == "SEP-LINK-DISJOINT"][0]
    LD.gate("G-CERTAINTY-CENSUS-PER-ARM",
            "EVERY ARM IS CENSUSED QUANTITY BY QUANTITY THROUGH THE FROZEN "
            "PREDICATES (#87).  EPR's completeness condition -- every "
            "element of the physical reality must have a counterpart in the "
            "physical theory -- EPR's own sentence, matched verbatim as A-E1 "
            "-- is applied to both descriptions on all four arms; the record "
            "certifies and carries, the shadow certifies nothing and carries "
            "none of the record's.  What the record's zero is, and is not, "
            "is measured at G-THE-ANALYTIC-LEGS-MEASURED",
            consume("G-CERTAINTY-CENSUS-PER-ARM", R)
            and prim["premise_instances"] == 0
            and walk["certainty_elements"] > 0
            and walk["without_counterpart_in_D_RECORD"] == 0
            and walk["without_counterpart_in_D_SHADOW"]
            == walk["certainty_elements"],
            "arms %d; primary arm pairs %d; walk arm certified %d, without a "
            "record counterpart %d, without a shadow counterpart %d"
            % (len(arms), prim["premise_instances"],
               walk["certainty_elements"],
               walk["without_counterpart_in_D_RECORD"],
               walk["without_counterpart_in_D_SHADOW"]))
    LD.gate("G-CERTAINTY-POLARITY",
            "THE CENSUS IS CHECKED IN BOTH DIRECTIONS.  A predicate that "
            "returned certainty everywhere would make the shadow certify as "
            "much as the record; the measured counts differ by arm and the "
            "shadow's own certified count is zero at every one of them, so "
            "the two predicates are not the same predicate wearing two names",
            all(a["certainty_elements_certified_by_D_SHADOW"] == 0
                for a in arms) and any(a["certainty_elements"] > 0
                                       for a in arms),
            "shadow-certified totals %s; record-certified totals %s"
            % ([a["certainty_elements_certified_by_D_SHADOW"] for a in arms],
               [a["certainty_elements"] for a in arms]))
    SEAL.take("SEAL-CERTAINTY", R)
    return arms, FR, FS


# ===========================================================================
# SECTION 10.  MEASUREMENT 3 -- E4, THE TWO REDUCTIONS
# ===========================================================================
# EPR's example assigns two different wave functions to the same reality,
# depending on which quantity is measured on the first system.  Here the
# object is exact and countable: one committed record, five declared
# readings on the other block, and the DESCRIPTION ASSIGNED to this block --
# the set of values its quantities can still take, given what the reading at
# A reports.  The assignment is measure-free; the count is a count.

def assigned_description(rd, row, qs, rfib):
    # FALSIFIER MUT-E4-COLLAPSE: every reading is made to assign the same
    # description
    if mut("MUT-E4-COLLAPSE"):
        return ()
    return tuple(tuple(sorted({z[d] for z in rfib[rd][row]})) for d in qs)


def assigned_description_jointly(rd, row, qs, rfib):
    """THE DECLARED ALTERNATIVE.  `assigned_description` is the product of the
    per-quantity marginals: the set of values EACH quantity can still take,
    taken quantity by quantity.  This is the joint reading -- the set of
    value-TUPLES the fibre admits -- which keeps the correlations between the
    block's quantities.  It is measured beside the published one so that the
    definition-relativity of the E4 distribution is on the record."""
    return tuple(sorted({tuple(z[d] for d in qs) for z in rfib[rd][row]}))


def reductions_measure(R, corp, adm, uniq, rfib, arms):
    say("SECTION 10.  MEASUREMENT 3 -- E4, THE TWO REDUCTIONS")
    out = []
    for locname, locf in LOCALIZATIONS:
        for sepname, septest in SEPARATIONS:
            primary = (locname == "LOC-WALK"
                       and sepname == "SEP-LINK-DISJOINT")
            specs = pair_specs(locf, septest)
            cache, jcache = {}, {}
            for nm, spec in specs.items():
                for si, (_da, _db, qs) in enumerate(spec):
                    for r in uniq:
                        s = {assigned_description(rd, r, qs, rfib)
                             for rd in READINGS}
                        cache[(nm, si, r)] = len(s)
                        if primary:
                            j = {assigned_description_jointly(rd, r, qs, rfib)
                                 for rd in READINGS}
                            jcache[(nm, si, r)] = len(j)
            dist, probes, jdist = Counter(), 0, Counter()
            for i, (_tag, _h) in enumerate(corp):
                r = ROWCACHE[i]
                for nm in adm[i]:
                    for si in range(len(specs[nm])):
                        probes += 1
                        dist[cache[(nm, si, r)]] += 1
                        if primary:
                            jdist[jcache[(nm, si, r)]] += 1
            if probes:
                out.append({
                    "localization": locname, "separation": sepname,
                    "probes": reg(probes),
                    "distinct_assigned_descriptions": {
                        str(k): reg(v) for k, v in sorted(dist.items())},
                    "probes_with_more_than_one": reg(
                        sum(v for k, v in dist.items() if k > 1)),
                    "largest": reg(max(dist)), "smallest": reg(min(dist)),
                    "distinct_assigned_descriptions_under_the_joint_reading": {
                        str(k): reg(v) for k, v in sorted(jdist.items())}
                    if primary else "not measured on this arm"})
                say("    %-9s %-19s probes %-8d distinct assignments %s"
                    % (locname, sepname, probes,
                       {k: v for k, v in sorted(dist.items())}))
    R["reductions"] = {
        "arms": out,
        "readings_declared_on_the_other_block": list(READINGS),
        "assignment": "the set of values the block's quantities can still "
                      "take given what the declared reading at A reports, "
                      "TAKEN QUANTITY BY QUANTITY -- the product of the "
                      "per-quantity marginals; measure-free, so no measure is "
                      "smuggled in",
        "the_declared_alternative": "the JOINT reading -- the set of "
                                    "value-tuples the fibre admits, which "
                                    "keeps the correlations between a block's "
                                    "quantities -- is measured on the primary "
                                    "arm and published beside it.  The "
                                    "published distribution is therefore "
                                    "definition-relative, and the marginal "
                                    "reading is the conservative one: it "
                                    "assigns no more distinct descriptions "
                                    "than the joint one does at the head "
                                    "value",
        "A_independence_disclosed": "the reading's value at A does not "
                                    "depend on WHICH separated block A is, "
                                    "because the record field is measured "
                                    "site-constant at every committed "
                                    "history (section 4); the dependence "
                                    "that is measured here is on the READING, "
                                    "which is EPR's variable",
        "window": "COUNTING-ONLY over the declared corpus (E-24)"}
    walk = [a for a in out if a["localization"] == "LOC-WALK"
            and a["separation"] == "SEP-LINK-DISJOINT"][0]
    LD.gate("G-E4-TWO-REDUCTIONS",
            "THE TWO-REDUCTIONS PHENOMENON IS REBUILT AS A COUNT, PER PROBE "
            "(#87).  For one and the same committed record, the five "
            "declared readings on the separated block assign more than one "
            "description to this block at every probe of the primary arm, "
            "and the fibre's size is published as a distribution rather than "
            "as an average, beside the joint reading's distribution so the "
            "definition-relativity is on the record.  EPR's own sentence is "
            "matched verbatim as A-E4",
            consume("G-E4-TWO-REDUCTIONS", R)
            and walk["probes_with_more_than_one"] == walk["probes"]
            and walk["largest"] > 2,
            "primary arm probes %d, probes with more than one assignment %d, "
            "largest fibre %d" % (walk["probes"],
                                  walk["probes_with_more_than_one"],
                                  walk["largest"]))
    SEAL.take("SEAL-REDUCTIONS", R)
    return out


# ===========================================================================
# SECTION 11.  MEASUREMENT 4 -- E3, THE NON-COMMUTING PAIR
# ===========================================================================

def commutator_census(uniq):
    """[G, D(x)] over the committed records, exactly in Z[w]."""
    rows = []
    for r in uniq:
        gd = [[(0, 0)] * 3 for _ in range(3)]
        dg = [[(0, 0)] * 3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                gd[i][j] = zmul((GN[i][j], 0), WPOW[r[j] % 3])
                dg[i][j] = zmul(WPOW[r[i] % 3], (GN[i][j], 0))
        rows.append(gd != dg)
    return rows


def residue_degeneracy_census(uniq):
    """WHAT THE OPERATOR LEG ACTUALLY TRACKS.  The two declared coin orders
    are two candidate unitaries of paper-20's declaration fibre, not the
    operators of two physical quantities -- this unit exhibits no operator for
    the Born menu or for the record menu.  What the leg measures is the
    degeneracy of the PHASE ENCODING: the orders agree exactly when the three
    counts are equal modulo three, and at some of those records the record
    observable diag(w^n) is not degenerate at all."""
    comm = commutator_census(uniq)
    agree_rows = [r for r, differs in zip(uniq, comm) if not differs]
    criterion = sum(1 for r, differs in zip(uniq, comm)
                    if differs == (len({r[j] % 3 for j in range(3)}) != 1))
    nonscalar = [r for r in agree_rows if len(set(r)) != 1]
    # FALSIFIER MUT-RESIDUE-CRITERION: the operator leg is reported as
    # tracking the observables rather than the count residue
    if mut("MUT-RESIDUE-CRITERION"):
        criterion, nonscalar = len(uniq) - 1, []
    return {"agree_rows": agree_rows, "criterion_agreements": criterion,
            "nonscalar_agree_rows": nonscalar}


def conjugacy_measure(R, corp, uniq, rfib, conj, ref):
    say("SECTION 11.  MEASUREMENT 4 -- E3, THE NON-COMMUTING PAIR")
    comm = commutator_census(uniq)
    ncomm = sum(1 for b in comm if b)
    # FALSIFIER MUT-COMMUTATOR: the two coin orders are reported as commuting
    if mut("MUT-COMMUTATOR"):
        ncomm = 0
    P, Q = "READ-BORN-GD", "READ-RECORD-MENU"
    is_conj = (P, Q) in conj or (Q, P) in conj
    # FALSIFIER MUT-CONJ-REFINE: the conjugate pair is reported as jointly
    # declarable
    if mut("MUT-CONJ-REFINE"):
        is_conj = False
    carried = 0
    for r in uniq:
        fibP = rfib[P][r]
        if len({reading_value(Q, z) for z in fibP}) == 1:
            carried += 1
    carried_other = 0
    for r in uniq:
        fibQ = rfib[Q][r]
        if len({reading_value(P, z) for z in fibQ}) == 1:
            carried_other += 1
    hist_both = 0
    for i, (_t, _h) in enumerate(corp):
        r = ROWCACHE[i]
        if len(rfib["READ-RECORD"][r]) == 1:
            hist_both += 1
    deg = residue_degeneracy_census(uniq)
    R["conjugacy"] = {
        "operator_leg": "the two declared coin orders' OPERATORS are the two "
                        "orders of the same pair of matrices: G . D(x) "
                        "against D(x) . G, compared exactly in Z[w]",
        "what_the_operator_leg_is_not": "NOT an instance of EPR's antecedent. "
            "G . D(x) and D(x) . G are paper-20's two declared coin orders -- "
            "a declaration fibre, two candidate unitaries -- and this unit "
            "exhibits no operator for the Born menu or for the record menu at "
            "all.  The leg tracks the degeneracy of the phase encoding: the "
            "two orders agree exactly when the three counts are equal modulo "
            "three, which happens at records where the record observable is "
            "not degenerate.  EPR's antecedent is carried here by the READING "
            "leg alone, where three declared pairs admit no common refinement",
        "operator_leg_agrees_with_the_residue_criterion_at":
            reg(deg["criterion_agreements"]),
        "records_where_the_two_orders_commute":
            reg(len(deg["agree_rows"])),
        "of_those_where_the_record_observable_is_not_scalar":
            reg(len(deg["nonscalar_agree_rows"])),
        "the_commuting_records": [list(r) for r in deg["agree_rows"]],
        "records_where_the_two_orders_differ": reg(ncomm),
        "records": reg(len(uniq)),
        "reading_pair": "%s | %s" % (P, Q),
        "pair_is_not_jointly_declarable": is_conj,
        "all_not_jointly_declarable_pairs": ["%s|%s" % p for p in conj],
        "records_where_the_Born_menu_carries_the_record_menu": reg(carried),
        "records_where_the_record_menu_carries_the_Born_menu":
            reg(carried_other),
        "histories_where_D_RECORD_carries_both": reg(hist_both),
        "of_histories": reg(len(corp)),
        "the_antecedent_is_carried_by_the_reading_leg":
            "the five declared readings are measured as partitions and three "
            "unordered pairs admit no common refinement; that is this arena's "
            "rendering of two quantities that cannot be declared together, "
            "and it is what carries the dilemma below",
        "horn_1_for_D_SHADOW": "HOLDS -- the shadow is measured incomplete in "
                               "section 9",
        "horn_2_for_D_RECORD": "FAILS -- the record carries both members of a "
                               "pair that no single shadow carries, at every "
                               "committed history",
        "decision": "the dilemma is decided per description: the "
                    "wave-function analogue takes horn one, the record "
                    "refutes horn two",
        "bell_stamp": "this is not a local-realism claim: the joint values "
                      "live at the outcome-dependence level the corpus "
                      "already owns (v5 paper-14), and section 13 states "
                      "which desideratum is met by which description"}
    LD.gate("G-CONJUGATE-PAIR-MEASURED",
            "E3'S SECOND HORN IS PUT AT RISK AND MEASURED.  The corpus's own "
            "conjugate pair -- paper-20's Born menu against its record menu "
            "-- is verified NOT JOINTLY DECLARABLE by computing the "
            "refinement relation in both directions, which is the leg that "
            "carries EPR's antecedent here -- E3 itself matched verbatim as "
            "A-E3; the operator leg is taken exactly in Z[w], where the two "
            "declared coin orders' OPERATORS differ at %d of the %d committed "
            "records; and the record is measured to carry both members at "
            "every committed history while no single Born menu carries both"
            % (ncomm, len(uniq)),
            consume("G-CONJUGATE-PAIR-MEASURED", R)
            and is_conj and ncomm > 0 and hist_both == len(corp)
            and carried < len(uniq) and carried_other < len(uniq),
            "records where the orders differ %d of %d; pair not jointly "
            "declarable %s; histories where the record carries both %d of "
            "%d; Born menu carries the record menu at %d of %d records"
            % (ncomm, len(uniq), is_conj, hist_both, len(corp), carried,
               len(uniq)))
    LD.gate("G-OPERATOR-LEG-IS-RESIDUE-DEGENERACY",
            "THE OPERATOR LEG IS LABELLED FOR WHAT IT MEASURES.  The two "
            "coin orders commute exactly when the site's three counts are "
            "equal modulo three -- the criterion agrees with the exact Z[w] "
            "comparison at every committed record -- so the leg tracks n mod "
            "3 and not the observables; and at some of the commuting records "
            "the record observable diag(w^n) is not scalar, where the leg "
            "reports agreement while the two quantities' own operators do "
            "not commute.  This is a disclosure about the encoding, not an "
            "instance of EPR's antecedent, and the paper says so",
            deg["criterion_agreements"] == len(uniq)
            and len(deg["nonscalar_agree_rows"]) > 0,
            "criterion agreements %d of %d; commuting records %d, of those "
            "with a non-scalar record observable %d"
            % (deg["criterion_agreements"], len(uniq),
               len(deg["agree_rows"]), len(deg["nonscalar_agree_rows"])))
    SEAL.take("SEAL-CONJUGACY", R)
    return ncomm


# ===========================================================================
# SECTION 12.  MEASUREMENT 5 -- THE E5 AUDIT
# ===========================================================================
# EPR refuse a reality that depends on the measurement made elsewhere.  The
# audit is taken with the TEST-DECLARATION DUTY discharged: the probe is
# SIGHTED -- a falsifier that lets the reading at A reach B's record is
# declared, and it dies at this gate.

def record_at_B_under(rd, row, qs):
    """B's OWN RECORD, computed through a path that takes the reading
    declared on A as a parameter -- so that a leak would show."""
    j = READINGS.index(rd)
    vals = tuple(row[d] for d in qs)
    # FALSIFIER MUT-E5-LEAK: the reading declared at A is routed into B's own
    # record and shadow
    if mut("MUT-E5-LEAK"):
        vals = tuple(v + j for v in vals)
    return vals


def shadow_at_B_under(rd, row):
    """B's OWN SHADOW, likewise reading-parameterised."""
    j = READINGS.index(rd)
    if mut("MUT-E5-LEAK"):
        return ("LEAK", j) + tuple(shadow_menu(row, PSI_PRIMARY))
    return tuple(shadow_menu(row, PSI_PRIMARY))


def e5_measure(R, corp, adm, uniq, rfib, red):
    say("SECTION 12.  MEASUREMENT 5 -- THE E5 AUDIT")
    locf, septest = loc_walk, sep_link_disjoint
    specs = pair_specs(locf, septest)
    cache = {}
    for nm, spec in specs.items():
        for si, (_da, _db, qs) in enumerate(spec):
            for r in uniq:
                recs = {record_at_B_under(rd, r, qs) for rd in READINGS}
                shad = {shadow_at_B_under(rd, r) for rd in READINGS}
                asg = {assigned_description(rd, r, qs, rfib)
                       for rd in READINGS}
                cache[(nm, si, r)] = (len(recs) > 1, len(shad) > 1,
                                      len(asg) > 1)
    probes = rec_moved = sha_moved = asg_moved = 0
    for i, (_tag, _h) in enumerate(corp):
        r = ROWCACHE[i]
        for nm in adm[i]:
            for si in range(len(specs[nm])):
                probes += 1
                a, b, c = cache[(nm, si, r)]
                rec_moved += a
                sha_moved += b
                asg_moved += c
    R["e5_audit"] = {
        "arm": "LOC-WALK x SEP-LINK-DISJOINT, the arm where EPR's own "
               "criterion is instantiable here",
        "probes": reg(probes),
        "probes_where_B_s_record_moves_with_the_reading_at_A": reg(rec_moved),
        "probes_where_B_s_own_shadow_moves": reg(sha_moved),
        "probes_where_the_description_ASSIGNED_to_B_moves": reg(asg_moved),
        "test_declaration": "THE PROBE IS SIGHTED: the falsifier MUT-E5-LEAK "
                            "routes the index of the reading declared at A "
                            "into B's own record and into B's own shadow, "
                            "and it dies at this gate; so the zero below is "
                            "demonstrated UNINJECTED",
        "what_the_zero_is": "FORCED BY THE FORMALISATION, and reported as "
                            "that.  A reading in this unit is a function on "
                            "records, not an operation on a history: nothing "
                            "that builds the arena, the corpus, the record "
                            "field or the blocks takes a reading or names one "
                            "(AST-checked at G-THE-ANALYTIC-LEGS-MEASURED), "
                            "so no path from A's declaration to B's record "
                            "exists to be measured, and this zero would be "
                            "returned on any arena.  The falsifier "
                            "establishes that the instrument carries no such "
                            "path by accident; it does not establish that the "
                            "arena forbids one",
        "what_carries_the_row_instead": "the DYNAMICAL census of section 7, "
                                        "which is a measurement of the arena: "
                                        "over every event shape the arena "
                                        "admits, an event confined to an "
                                        "actor-disjoint region reaches a "
                                        "record entry the other block owns 0 "
                                        "times, while the unconfined ones do "
                                        "reach a block's quantities -- a "
                                        "sighted probe with its positive "
                                        "control in the same census",
        "the_successor_obligation": "testing SEC's ruling in EPR's own sense "
                                    "would require an OPERATION on A that the "
                                    "corpus's dynamics admits; this unit "
                                    "declares none, and that is the honest "
                                    "scope of the row",
        "reading": "nothing declared at A moves anything B has.  What moves "
                   "is the description an observer at A assigns to B, at "
                   "every probe -- which is E4, not a disturbance",
        "seam_confinement": "this is SEC's adjudicated ruling seen from the "
                            "other side, and it is a KINEMATIC statement: no "
                            "sector-private link ever moves"}
    LD.gate("G-E5-RECORD-DOES-NOT-MOVE",
            "B'S RECORD IS MEASURED NOT TO MOVE WITH THE READING DECLARED AT "
            "A, PROBE BY PROBE, WITH THE TEST DECLARED.  B's own record and "
            "B's own shadow are recomputed under every declared reading "
            "through a reading-parameterised path; neither moves at any of "
            "the 105,408 probes, while the description assigned to B moves "
            "at all of them.  EPR's own sentence is matched verbatim as "
            "A-E5.  The zero is forced by the formalisation and demonstrated "
            "uninjected -- what carries this row as a measurement of the "
            "ARENA is the dynamical census of section 7",
            consume("G-E5-RECORD-DOES-NOT-MOVE", R)
            and rec_moved == 0 and sha_moved == 0 and asg_moved == probes,
            "probes %d, record moves %d, own-shadow moves %d, assigned "
            "description moves %d" % (probes, rec_moved, sha_moved, asg_moved))
    SEAL.take("SEAL-E5", R)
    return probes, rec_moved, asg_moved


# ===========================================================================
# SECTION 13.  MEASUREMENT 6 -- THE BELL WALL AND THE DESIDERATA
# ===========================================================================

BANNED = (
    "local realism is restored",
    "this evades Bell",
    "Bell nonlocality is evaded",
    "locality is restored by the record",
    "hidden variables are vindicated",
    "the corpus satisfies Bell local causality",
    "a local hidden-variable completion exists",
)
# THE WALL'S SECOND LEG (K2 M5 = K3 M7).  Seven exact sentences are a
# blacklist, and a blacklist is defeated by re-voicing: "local realism is
# restored" is banned while "this restores local realism" is not.  These are
# VOICE-NORMALISED patterns over the paper's canonical bytes, published with
# the literals, and they are matched in both voices and at a distance.  The
# delivered paper is required to be clean under all of them.
BANNED_PATTERNS = (
    ("W1", r"restor\w*\s+(?:\w+\s+){0,3}?local realism"),
    ("W2", r"local realism\s+(?:\w+\s+){0,3}?(?:is|are|was|were)?\s*"
           r"restor\w*"),
    ("W3", r"(?:restor|recover|regain)\w*\s+(?:\w+\s+){0,3}?localit\w+"),
    ("W4", r"localit\w+\s+(?:\w+\s+){0,4}?(?:restor|recover|regain)\w*"),
    ("W5", r"(?:evad|escap|circumvent|sidestep)\w*\s+(?:\w+\s+){0,3}?bell"),
    ("W6", r"bell\w*\s+(?:\w+\s+){0,4}?(?:evad|escap|circumvent|sidestep)"
           r"\w*"),
    ("W7", r"bell\w*(?:'s)?\s+(?:theorem|inequalit\w+)\s+"
           r"(?:does not|do not|cannot|can not)\s+(?:apply|hold|bind)"),
    ("W8", r"local hidden.{0,2}variable"),
    ("W9", r"hidden.{0,2}variable\w*\s+(?:\w+\s+){0,4}?"
           r"(?:vindicat|establish|confirm|verifi)\w*"),
    ("W10", r"(?:vindicat|establish|confirm|verifi)\w*\s+(?:\w+\s+){0,4}?"
            r"hidden.{0,2}variable"),
    ("W11", r"spooky action\s+(?:\w+\s+){0,6}?"
            r"(?:refut|disprov|disproved|dispell|dismiss)\w*"),
    ("W12", r"(?:refut|disprov|dispell|dismiss)\w*\s+(?:\w+\s+){0,6}?"
            r"spooky action"),
    ("W13", r"einstein\s+(?:\w+\s+){0,4}?(?:was right|is right|were right|"
            r"vindicated|correct after all)"),
    ("W14", r"satisf\w+\s+(?:\w+\s+){0,3}?bell local causality"),
)
# TWO PASSAGES MAY CARRY THE WALL'S OWN WORDS, and only these two: the
# verbatim standing verdict this unit is required to state, and this unit's
# own denial.  Both are exact declared strings, both are separately gated --
# the first as a verbatim anchor that must be present, the second as a
# polarity-checked sentence -- and a pattern hit anywhere outside them fails.
WALL_LICENSED = (
    ("THE-STANDING-VERDICT-QUOTED",
     "ISP cannot satisfy Bell local causality and still reproduce the "
     "Tsirelson violation. It is Bell-nonlocal"),
    ("THE-UNIT-S-OWN-DENIAL",
     "No sentence of this unit claims a restored locality, an evaded Bell "
     "theorem, or a vindicated hidden-variable completion"),
)
# THE PHRASE THAT MAY ONLY APPEAR IN TWO PLACES (K2 M4).  "element of
# reality" is walled to the formalised predicate and to verbatim quotation of
# 1935.  The wall had no gate; this is the gate.  Every occurrence in the
# paper must sit inside one of the carriers declared here, and the accounting
# is by OCCURRENCE COUNT, so a planted sentence in the unit's own voice
# fails even though the carriers are all still present.
ELEMENT_RE = re.compile(r"elements? of (?:the )?(?:physical )?realit\w+")


def bell_measure(R, arms, walkarm):
    say("SECTION 13.  MEASUREMENT 6 -- THE BELL WALL")
    # each row carries the CELLS THE PAPER PRINTS, rendered here and matched
    # against the paper's own bytes at G-PAPER-TABLES-WITH-HEADERS: the §9
    # table is the one that carries this unit's Bell obligations, and it was
    # the one table the paper instrument did not render (K3 MAJOR-1).
    des = [
        {"desideratum": "E1 -- every element of reality has a counterpart",
         "D-RECORD": "MET on the measured arms",
         "D-SHADOW": "NOT MET: %d certified elements, none carried"
                     % walkarm["without_counterpart_in_D_SHADOW"],
         "bell_constrained": "no",
         "paper_cells": ["E1 counterpart for every element",
                         "met on the measured arms", "not met", "no"]},
        {"desideratum": "E2 -- prediction with certainty without disturbing",
         "D-RECORD": "INSTANTIABLE only in the state's localization",
         "D-SHADOW": "NEVER: the shadow certifies nothing here",
         "bell_constrained": "no",
         "paper_cells": ["E2 certainty without disturbance",
                         "instantiable only in the state's localization",
                         "never here", "no"]},
        {"desideratum": "E3 -- simultaneous reality for a conjugate pair",
         "D-RECORD": "HELD: both members carried at every history",
         "D-SHADOW": "REFUSED: no single menu carries both",
         "bell_constrained": "YES -- any joint assignment across blocks is "
                             "outcome-dependent in v5 paper-14's sense",
         "paper_cells": ["E3 simultaneous reality for a conjugate pair",
                         "held at every history", "refused", "yes"]},
        {"desideratum": "E4 -- one reality, several assigned descriptions",
         "D-RECORD": "one record throughout",
         "D-SHADOW": "up to five assignments at one record",
         "bell_constrained": "no",
         "paper_cells": ["E4 one reality, several assignments",
                         "one record throughout", "up to five assignments",
                         "no"]},
        {"desideratum": "E5 -- no dependence of B's reality on A's choice",
         "D-RECORD": "MET: zero moves measured",
         "D-SHADOW": "the ASSIGNED description moves; B's own does not",
         "bell_constrained": "no",
         "paper_cells": ["E5 no dependence on the distant choice",
                         "zero moves measured",
                         "the assigned description moves", "no"]},
        # E6 IS SCOPED (K2 M3).  EPR's "such a theory" is a theory furnishing
        # a COMPLETE DESCRIPTION OF PHYSICAL REALITY.  What is measured here
        # is completeness for the censused certainty-elements on the measured
        # arms -- and on those arms that completeness is analytic.  The cell
        # says so; it never says completeness simpliciter.
        {"desideratum": "E6 -- such a theory is possible",
         "D-RECORD": "COMPLETE FOR THE CENSUSED CERTAINTY-ELEMENTS on the "
                     "measured arms, AT THIS ARENA and under this corpus's "
                     "site-constancy -- never completeness simpliciter, which "
                     "is a claim about physical reality this unit neither "
                     "makes nor could make",
         "D-SHADOW": "not applicable",
         "bell_constrained": "YES -- it is not a local-realist theory; the "
                             "corpus is Bell-nonlocal by v5 paper-14 and "
                             "this unit claims nothing against that",
         "paper_cells": ["E6 such a theory is possible",
                         "complete for the censused certainty-elements on "
                         "the measured arms", "not applicable", "yes"]},
    ]
    # FALSIFIER MUT-BELL-TABLE: the desiderata table's two description
    # columns are swapped in the rendered row, with every flag left correct
    if mut("MUT-BELL-TABLE"):
        c = des[0]["paper_cells"]
        des[0]["paper_cells"] = [c[0], c[2], c[1], c[3]]
    R["bell"] = {
        "standing_verdict": "v5 paper-14: ISP is Bell-nonlocal (E1 false), "
                            "no-signalling and parameter-independent (E2 "
                            "true); outcome independence is what fails",
        "desiderata": des,
        "banned_sentences": list(BANNED),
        "banned_count": reg(len(BANNED)),
        "banned_patterns": [{"id": pid, "pattern": pat}
                            for pid, pat in BANNED_PATTERNS],
        "banned_pattern_count": reg(len(BANNED_PATTERNS)),
        "the_wall_has_a_positive_leg": "the standing verdict is not only "
                                       "forbidden to be contradicted, it is "
                                       "required to be STATED: v5 paper-14's "
                                       "two sentences are matched in this "
                                       "paper's own bytes, so a paper-38 that "
                                       "quietly dropped its Bell section "
                                       "would fail a gate",
        "the_locality_finding": "at this arena EPR's criterion is "
                                "instantiable only in the localization the "
                                "quantum state uses, where the quantity "
                                "attributed to a block has as its referent a "
                                "co-division pair straddling that block's own "
                                "boundary; so the element the criterion "
                                "certifies is not local to the block it is "
                                "certified for",
        "not_claimed": ["local realism", "Bell evasion",
                        "a vindicated hidden-variable completion",
                        "any statement about spacelike separation"]}
    LD.gate("G-BELL-DESIDERATA-BOUND",
            "EVERY EPR DESIDERATUM IS BOUND TO A MEASURED ROW AND TO ITS "
            "BELL STATUS.  Six rows, each naming what each description does "
            "with that desideratum and whether the corpus's standing Bell "
            "verdict constrains it; the two rows that are constrained say so "
            "in their own text, the E6 row is scoped to the censused "
            "certainty-elements and never to completeness simpliciter, and "
            "every cell the paper prints is RENDERED from these rows.  EPR's "
            "closing sentence is matched verbatim as A-E6",
            consume("G-BELL-DESIDERATA-BOUND", R)
            and len(des) == 6
            and all(len(d["paper_cells"]) == 4 for d in des)
            and all((d["paper_cells"][3] == "no")
                    == (d["bell_constrained"] == "no") for d in des)
            and sum(1 for d in des
                    if d["bell_constrained"] != "no") == 2,
            "desiderata %d, Bell-constrained %d"
            % (len(des), sum(1 for d in des
                             if d["bell_constrained"] != "no")))
    SEAL.take("SEAL-BELL", R)
    return des


# ===========================================================================
# SECTION 14.  THE CONTROL ARMS AND THE MEASURE LEG
# ===========================================================================
# Every pre-registered outcome word must be shown emittable by the REAL head
# law on declared data.  None of the rows below is forged: each is a genuine
# evaluation of the SAME predicates and the SAME head law.

def controls_measure(R, corp, adm, uniq, FR, FS, arms):
    say("SECTION 14.  THE CONTROL ARMS")
    rows = []
    for a in arms:
        if a["separation"] == "SEP-LINK-DISJOINT":
            rows.append({"arm": "CTRL-COMMITTED-" + a["localization"],
                         "declared_datum": "the committed corpus",
                         "premise_instances": a["premise_instances"],
                         "certainty_elements": a["certainty_elements"],
                         "without_counterpart_in_D_RECORD":
                             a["without_counterpart_in_D_RECORD"],
                         "without_counterpart_in_D_SHADOW":
                             a["without_counterpart_in_D_SHADOW"],
                         "totality_failures": 0, "object": a["object"],
                         "word": a["word"]})

    specs = pair_specs(loc_walk, sep_link_disjoint)
    mult = {}
    for i, (_t, _h) in enumerate(corp):
        for nm in adm[i]:
            mult[(nm, ROWCACHE[i])] = mult.get((nm, ROWCACHE[i]), 0) + 1

    def synth(name, ownR, ownS, tot=0):
        pairs = quant = cr = nr = ns = 0
        for (nm, r), m in mult.items():
            for (da, db, qs) in specs[nm]:
                pairs += m
                fr = FR[(da, r)]
                for d in qs:
                    quant += m
                    if epr_reality_at(d, fr):
                        cr += m
                        if not epr_counterpart_at(d, ownR(r, db)):
                            nr += m
                        if not epr_counterpart_at(d, ownS(r)):
                            ns += m
        a = {"arm": name, "declared_datum": "the committed corpus with a "
             "declared synthetic description", "premise_instances": reg(pairs),
             "certainty_elements": reg(cr),
             "without_counterpart_in_D_RECORD": reg(nr),
             "without_counterpart_in_D_SHADOW": reg(ns),
             "totality_failures": tot, "object": ARM_OBJECT["LOC-WALK"]}
        a["word"] = arm_word(a)
        return a

    rows.append(synth("CTRL-D-SHADOW-SYNTH-INJECTIVE",
                      lambda r, db: FR[(db, r)], lambda r: (r,)))
    rows.append(synth("CTRL-D-RECORD-SYNTH-PUNCTURED",
                      lambda r, db: FR[((0, 1), r)], lambda r: FS[r]))
    blocked = synth("CTRL-PREDICATE-PARTIAL", lambda r, db: FR[(db, r)],
                    lambda r: FS[r], tot=1)
    rows.append(blocked)

    # the synthetic ARENA: the same predicate forms with one declared link
    l1 = ((1, 0),)
    cells_l1 = tuple(k for k, (_x, l) in enumerate(CELLS) if l == l1[0])

    def loc_pair_l1(S):
        fs = frozenset(S)
        return tuple(k for k in cells_l1 if CELL_PAIR[k] <= fs)

    prem = qb = ld = cert = unc = quant = uncr = 0
    for i, (_t, _h) in enumerate(corp):
        r = ROWCACHE[i]
        for nm in ("AP-9-BLOCKS-9x1", "AP-3-BLOCKS-3x3-PARALLEL-CLASS-COL"):
            for A, B in product(COSETS[nm], repeat=2):
                if A == B:
                    continue
                d = sep_link_disjoint(A, B, l1)
                qs = loc_pair_l1(B)
                ld += d
                qb += (len(qs) > 0)
                if not (d and qs):
                    continue
                prem += 1
                da = tuple(sorted({k % 3 for k in loc_pair_l1(A)}))
                db = tuple(sorted({k % 3 for k in loc_pair_l1(B)}))
                fr = FR[(da, r)]
                for k in qs:
                    dd = k % 3
                    quant += 1
                    if epr_reality_at(dd, fr):
                        cert += 1
                        # COMPUTED, never typed (#4): the arm the paper calls
                        # scope-fixing runs the counterpart predicate against
                        # the record too, exactly as its siblings do.
                        if not epr_counterpart_at(dd, FR[(db, r)]):
                            uncr += 1
                        if not epr_counterpart_at(dd, FS[r]):
                            unc += 1
    a1 = {"arm": "CTRL-ARENA-ONE-DECLARED-DIRECTION",
          "declared_datum": "the same predicate forms with a single declared "
                            "link direction (FAC's L1 synthetic arena), at "
                            "the two named decompositions of every committed "
                            "history",
          "premise_instances": reg(prem),
          "link_disjoint_pairs": reg(ld),
          "quantity_bearing_at_LOC_PAIR": reg(qb),
          "quantities": reg(quant),
          "certainty_elements": reg(cert),
          "without_counterpart_in_D_RECORD": reg(uncr),
          "without_counterpart_in_D_SHADOW": reg(unc),
          "totality_failures": 0,
          "object": ARM_OBJECT["LOC-PAIR"]}
    a1["word"] = arm_word(a1)
    rows.append(a1)

    words = {r["word"] for r in rows}
    fams = R["pre_registered_outcomes"]["families"]
    unmatched = [w for w in words
                 if not any(w == f or (f.endswith("-AT-") and w.startswith(f))
                            for f in fams)]
    missing_fams = [f for f in fams
                    if not any(w == f or (f.endswith("-AT-")
                                          and w.startswith(f)) for w in words)]
    # FALSIFIER MUT-CONTROL-MISSING: control arms are dropped so a word becomes
    # undemonstrated
    if mut("MUT-CONTROL-MISSING"):
        rows = rows[:2]
        words = {r["word"] for r in rows}
        missing_fams = [f for f in fams
                        if not any(w == f or (f.endswith("-AT-")
                                              and w.startswith(f))
                                   for w in words)]
    R["controls"] = {
        "rows": rows, "count": reg(len(rows)),
        "distinct_words": sorted(words),
        "families_demonstrated": reg(len(fams) - len(missing_fams)),
        "families_declared": reg(len(fams)),
        "unmatched_words": unmatched, "families_not_demonstrated": missing_fams,
        "note": "the head law returns a different word on the declared arms, "
                "so no pigeonhole decided the verdict before the run"}
    LD.gate("G-EVERY-OUTCOME-WORD-EMITTABLE",
            "EVERY PRE-REGISTERED WORD IS EMITTED BY THE REAL HEAD LAW ON "
            "DECLARED DATA (#34 reachability).  Six arms run the same "
            "predicates: the two committed localizations, two synthetic "
            "descriptions with forced injectivity and a forced puncture, a "
            "declared partial predicate, and the same predicate forms on a "
            "synthetic arena with one declared link direction -- where the "
            "premise EXISTS, which is how the arena-relativity of the head "
            "is demonstrated rather than asserted",
            not unmatched and not missing_fams,
            "arms %d, distinct words %s, families not demonstrated %s"
            % (len(rows), sorted(words), missing_fams or "none"))
    SEAL.take("SEAL-CONTROLS", R)

    # THE MEASURE LEG (E-24): certainty is constancy on the fibre, which is
    # probability exactly one under every measure of full support.  Two
    # declared measures verify it as exact rationals, in both directions.
    wu = Counter()
    ws = Counter()
    for i, (_t, _h) in enumerate(corp):
        wu[ROWCACHE[i]] += 1
        ws[ROWCACHE[i]] += 1 + (i % 7)
    probes = agree = 0
    for dd in ((0,), (1,), (2,), (0, 1), (0, 1, 2)):
        for r in uniq:
            fib = FR[(dd, r)]
            for d in range(3):
                cert = epr_reality_at(d, fib)
                for W in (wu, ws):
                    tot = sum(W[z] for z in fib)
                    hit = sum(W[z] for z in fib if z[d] == r[d])
                    p = Fraction(hit, tot)
                    probes += 1
                    if (p == 1) == cert:
                        agree += 1
    # FALSIFIER MUT-MEASURE: one exact conditional probability is made to
    # disagree
    if mut("MUT-MEASURE"):
        agree -= 1
    R["measure_relativity"] = {
        "stamp": "COUNTING-ONLY: no count in this unit is a probability, and "
                 "no fraction is a frequency (E-24)",
        "certainty_is_measure_free": "constancy on the conditioning fibre",
        "declared_measures": ["MEASURE-UNIFORM (every committed history "
                              "weight one)",
                              "MEASURE-SKEWED (weight 1 + (index mod 7), "
                              "full support)"],
        "probes": reg(probes), "agreements": reg(agree),
        "note": "the equivalence is checked in BOTH directions: where the "
                "predicate says certain the exact conditional probability is "
                "1, and where it does not the probability is measured below 1"}
    LD.gate("G-PROBABILITY-EXACTLY-ONE",
            "EPR'S 'PROBABILITY EQUAL TO UNITY' IS TAKEN LITERALLY AND "
            "EXACTLY.  Under two declared measures of full support the "
            "conditional probability of the predicted value is computed as "
            "an exact rational at every probe and compared with the "
            "measure-free predicate, in both directions",
            agree == probes, "probes %d, agreements %d" % (probes, agree))
    SEAL.take("SEAL-MEASURE", R)
    return rows


# ===========================================================================
# SECTION 15.  THE HEAD, THE PAPER INSTRUMENT AND THE CLOSING BATTERY
# ===========================================================================

def head_route_two(corp, adm, uniq, tot):
    """THE SECOND ROUTE.  It shares no dispatcher and no cache with section
    9: it aggregates by DISTINCT RECORD with corpus multiplicities and
    re-applies the localization and separation predicates inline."""
    mult = {}
    for i, (_t, _h) in enumerate(corp):
        for nm in adm[i]:
            mult[(nm, ROWCACHE[i])] = mult.get((nm, ROWCACHE[i]), 0) + 1
    out = []
    for locname, locf in LOCALIZATIONS:
        for sepname, septest in SEPARATIONS:
            pairs = quant = cr = cs = nr = ns = 0
            for (nm, r), m in sorted(mult.items()):
                for A, B in product(COSETS[nm], repeat=2):
                    if A == B or not septest(A, B):
                        continue
                    qs = locf(B)
                    if not qs:
                        continue
                    pairs += m
                    da = tuple(sorted({k % 3 for k in locf(A)}))
                    db = tuple(sorted({k % 3 for k in locf(B)}))
                    fr = tuple(z for z in uniq
                               if all(z[d] == r[d] for d in da))
                    ownr = tuple(z for z in uniq
                                 if all(z[d] == r[d] for d in db))
                    fs = tuple(z for z in uniq
                               if shadow_menu(z, PSI_PRIMARY)
                               == shadow_menu(r, PSI_PRIMARY))
                    for k in qs:
                        d = k % 3
                        quant += m
                        if epr_reality_at(d, fr):
                            cr += m
                            if not epr_counterpart_at(d, ownr):
                                nr += m
                            if not epr_counterpart_at(d, fs):
                                ns += m
                        if epr_reality_at(d, fs):
                            cs += m
            a = {"localization": locname, "separation": sepname,
                 "object": ARM_OBJECT[locname], "premise_instances": pairs,
                 "quantities": quant, "certainty_elements": cr,
                 "certainty_elements_certified_by_D_SHADOW": cs,
                 "without_counterpart_in_D_RECORD": nr,
                 "without_counterpart_in_D_SHADOW": ns,
                 "totality_failures": tot}
            a["word"] = arm_word(a)
            out.append(a)
    return out


HEAD_FIELDS = (
    ("HISTORIES", "corpora/histories"),
    ("BLOCK-PAIRS", "separation/ordered_block_pairs"),
    ("LINK-DISJOINT", "separation/link_disjoint_block_pairs"),
    ("QUANTITY-BEARING-AT-THE-RECORD-LOCALIZATION",
     "separation/quantity_bearing_at_LOC_PAIR"),
    ("PREMISE-AT-THE-RECORD-LOCALIZATION",
     "separation/premise_instances_at_LOC_PAIR"),
    ("PREMISE-AT-THE-STATE-LOCALIZATION",
     "separation/premise_instances_at_LOC_WALK"),
    ("SUBSET-LATTICE", "separation/subset_lattice"),
    ("SUBSETS-WITH-BOTH", "separation/subsets_with_both"),
)


def verdict_measure(R, corp, adm, uniq, arms, tot, red, e5):
    say("SECTION 15.  THE HEAD")
    two = head_route_two(corp, adm, uniq, tot)
    diffs = []
    for a, b in zip(arms, two):
        for k in ("premise_instances", "quantities", "certainty_elements",
                  "certainty_elements_certified_by_D_SHADOW",
                  "without_counterpart_in_D_RECORD",
                  "without_counterpart_in_D_SHADOW", "word"):
            if a[k] != b[k]:
                diffs.append("%s/%s/%s" % (a["localization"],
                                           a["separation"], k))
    prim = [a for a in arms if a["localization"] == "LOC-PAIR"
            and a["separation"] == "SEP-LINK-DISJOINT"][0]
    walk = [a for a in arms if a["localization"] == "LOC-WALK"
            and a["separation"] == "SEP-LINK-DISJOINT"][0]
    # FALSIFIER MUT-HEAD-TYPED: the head word is typed rather than derived
    head = pick("MUT-HEAD-TYPED", prim["word"],
                "EPR-BOTH-COMPLETE")
    seg1 = ("EPR-SEPARATION<" + "; ".join(
        "%s=%s" % (nm, com(jpath(R, p))) for nm, p in HEAD_FIELDS)
        + "; THEOREM=THE-LINK-GRAPH-IS-COMPLETE-MULTIPARTITE-AND-A-PART-OWNS-"
          "NO-CELL>")
    seg2 = ("EPR-CENSUS<" + "; ".join(
        "%s-x-%s=%s-AT-%s-PAIRS-%s-CERTIFIED-%s-UNCARRIED"
        % (a["localization"], a["separation"], a["word"],
           com(a["premise_instances"]), com(a["certainty_elements"]),
           com(a["without_counterpart_in_D_SHADOW"])) for a in arms) + ">")
    seg3 = ("%s<PRIMARY-ARM=THE-RECORD-S-OWN-LOCALIZATION-AT-EPR-S-OWN-"
            "SEPARATION; SECOND-WORD=%s-AT-THE-STATE-LOCALIZATION-WITH-%s-"
            "CERTIFIED-AND-%s-UNCARRIED-AND-STATE-INVARIANT-BY-THEOREM; "
            "E4-ASSIGNMENTS-AT-ONE-RECORD=%s-AT-THE-DECLARED-PRIMARY-STATE-"
            "UNDER-THE-MARGINAL-READING; E5-RECORD-MOVES=%s-OF-%s; "
            "SCOPE=ONE-ARENA,COMMITTED-HISTORIES,"
            "KINEMATIC-SEPARATION-AS-MEASURED;COUNTS-ARE-COUNTING-ONLY;"
            "NO-LOCAL-REALISM-CLAIM>"
            % (head, walk["word"], com(walk["certainty_elements"]),
               com(walk["without_counterpart_in_D_SHADOW"]),
               com(red["largest"]), com(e5[1]), com(e5[0])))
    fams = R["pre_registered_outcomes"]["families"]
    okfam = any(head == f or (f.endswith("-AT-") and head.startswith(f))
                for f in fams)
    R["counts"] = {
        "arms_route_one": arms, "arms_route_two": two,
        "route_disagreements": diffs,
        "route_two_method": "aggregation by distinct record with corpus "
                            "multiplicities; no pair-spec list, no cache, no "
                            "shared loop with section 9"}
    R["verdict"] = {
        "head": head, "segment_1": seg1, "segment_2": seg2, "segment_3": seg3,
        "second_word": walk["word"],
        "head_is_in_the_pre_registered_vocabulary": okfam,
        "primary_arm": "LOC-PAIR x SEP-LINK-DISJOINT",
        "why_primary": "the record's own localization is the committed "
                       "carrier typing gated in section 3: a record entry's "
                       "referent is a co-division PAIR, so a block owns the "
                       "quantity only when it owns both its actors",
        "candidate": "between delivery and adjudication every headline here "
                     "is a candidate reading"}
    LD.gate("G-HEAD-DERIVED-TWICE",
            "THE HEAD IS DERIVED TWICE BY ROUTES SHARING NO DISPATCHER.  "
            "Section 9's census and a second aggregation by distinct record "
            "with corpus multiplicities agree on every count of every arm "
            "and on every arm word; the head word is then required to lie in "
            "the vocabulary parsed from the pin",
            not diffs and okfam and head == prim["word"]
            and head == two[0]["word"],
            "arms %d, disagreements %s, head %s in vocabulary %s, equals the "
            "primary arm's word on both routes %s"
            % (len(arms), diffs or "none", head, okfam,
               head == prim["word"] == two[0]["word"]))
    SEAL.take("SEAL-COUNTS", R)
    SEAL.take("SEAL-VERDICT", R)
    for seg in (seg1, seg2, seg3):
        say("")
        say(seg)
    return head, seg1, seg2, seg3


ROWCACHE = []

WINDOWS = (
    ("W-CORPUS", "the committed histories: paper-21's 72 I7-STRICT triples, "
     "their 5,184 ordered concatenations and the 600 driven-window "
     "schedules", "5856", False),
    ("W-SUBSETS", "the COMPLETE lattice of subsets of the nine actors -- no "
     "cap, no sampling", "512", True),
    ("W-EVENT-SHAPES", "the COMPLETE set of event shapes this arena admits: "
     "every three-actor subset, which is every division event's support -- "
     "the window the dynamical no-disturbance census runs over, and not a "
     "sample of the ones the corpus happens to run", "84", True),
    ("W-BLOCKS", "the COMPLETE set of law-compatible decompositions of the "
     "nine actors: FAC's geometry-leg survivors by closed form over the "
     "complete 21,147-partition actor lattice, restricted per history by the "
     "history leg", "6", True),
    ("W-STATES", "the declared state family for the shadow: every site "
     "vector over the alphabet {0, 1, w, w^2}.  It is a DECLARED bound and "
     "not a complete one -- the parent's own alphabet is wider, and the "
     "shadow theorem is proved without either", "64", False),
    ("W-READINGS", "the declared readings of a block: the record, the Born "
     "menu at both coin orders, the record menu, and paper-20's curvature",
     "5", False),
    ("W-MEASURES", "the declared measures for the probability leg: uniform "
     "and a skewed full-support measure", "2", False),
)


def windows_declare(R):
    complete = [a for a, _b, _c, comp in WINDOWS if comp]
    R["windows"] = {"rows": [{"window": a, "bound": c, "statement": b,
                              "complete": comp}
                             for a, b, c, comp in WINDOWS],
                    "count": reg(len(WINDOWS)),
                    "complete_windows": complete,
                    "complete_count": reg(len(complete)),
                    "note": "three of the seven windows are COMPLETE -- the "
                            "subset lattice, the event shapes and the block "
                            "lattice; the corpus, the states, the readings "
                            "and the measures are declared bounds"}
    LD.gate("G-WINDOWS-DECLARED-WITH-THEIR-BOUNDS",
            "EVERY WINDOW THIS UNIT COUNTS OVER IS DECLARED WITH ITS BOUND "
            "AND WITH WHETHER IT IS COMPLETE (§15).  Seven windows, three of "
            "them complete -- the subset lattice, the event shapes and the "
            "block lattice; every other is named with the parent that fixed "
            "it and is declared a bound rather than a completion",
            len(WINDOWS) == 7 and len(complete) == 3,
            "windows %d, complete %d %s"
            % (len(WINDOWS), len(complete), complete))
    SEAL.take("SEAL-WINDOWS", R)


CLASS_WORDS = (
    ("EPR-CRITERION-INAPPLICABLE-AT-", "the head law's first branch: the "
     "arm's premise instances are zero"),
    ("EPR-SHADOW-INCOMPLETE-RECORD-COMPLETE", "the head law's fourth branch: "
     "certified elements exist, none lacks a record counterpart, some lack a "
     "shadow counterpart"),
    ("EPR-BOTH-COMPLETE", "the head law's last branch: no certified element "
     "lacks a counterpart in either description"),
    ("EPR-RECORD-ALSO-INCOMPLETE", "the head law's third branch"),
    ("EPR-BLOCKED-AT-", "the head law's zeroth branch: a predicate is not "
     "total"),
    ("SEAM-CONFINED", "SEC's adjudicated ruling, the source of the "
     "no-disturbance clause"),
    ("COUNTING-ONLY", "E-24: no count here is a probability"),
    ("NOT-JOINTLY-DECLARABLE", "neither reading's fibres refine the other's"),
)


def class_binding_measure(R, arms, ctrl, conj):
    rows = []
    for word, why in CLASS_WORDS:
        emitted = [a["word"] for a in arms + ctrl if a.get("word", "")
                   .startswith(word)]
        rows.append({"class_word": word, "predicate": why,
                     "emitted_by_the_law_at": reg(len(emitted)),
                     "recomputed": True})
    # FALSIFIER MUT-CLASSWORD: a class word is typed rather than recomputed
    if mut("MUT-CLASSWORD"):
        rows.append({"class_word": "EPR-BOTH-COMPLETE", "predicate": "typed",
                     "emitted_by_the_law_at": 0, "recomputed": False})
    bad = [r["class_word"] for r in rows if not r["recomputed"]]
    R["class_binding"] = {"rows": rows, "count": reg(len(rows)),
                          "unbound": bad}
    LD.gate("G-CLASS-WORDS-BOUND-TO-PREDICATES",
            "EVERY CLASS WORD THIS UNIT PRINTS IS RECOMPUTED FROM THE "
            "PREDICATE THAT DEFINES IT (#295).  Eight class words, each "
            "carrying the branch or ruling that emits it and the count of "
            "arms at which the law actually emitted it",
            not bad, "class words %d, unbound %s" % (len(rows), bad or "none"))
    SEAL.take("SEAL-CLASSBIND", R)


# --------------------------------------------------------------------------
# THE PAPER INSTRUMENT
# --------------------------------------------------------------------------

# THE STRUCTURAL LITERALS ARE SCOPED TO THEIR CONTEXTS (K3 MINOR-9).  A bare
# allow-list of tokens like 19, 27 or 35 whitelists a forgery twice over,
# because those tokens are simultaneously runbook identifiers and measured
# values of this unit.  So there is no bare allow-list: a numeral that is not
# the run's own product must sit inside one of the declared IDENTIFIER SHAPES
# below, matched with its position, and nothing else passes.
LITERAL_CONTEXTS = (
    ("SECTION-HEADING", re.compile(r"^#+ \d+\.", re.M)),
    ("SECTION-REFERENCE", re.compile(r"sections? \d+")),
    ("PAPER-IDENTIFIER", re.compile(r"paper[ -]\d+")),
    ("LEDGER-REFERENCE", re.compile(r"#\d+")),
    ("ENGRAVING-REFERENCE", re.compile(r"E-\d+")),
    ("THE-1935-CITATION",
     re.compile(r"Phys\. Rev\. \d+, \d+ \(\d{4}\)")),
    ("THE-1935-PAPER", re.compile(r"\d{4} (?:paper|print)")),
    ("THE-SOURCE-FILENAME", re.compile(r"epr-\d{4}-physrev-\d+-\d+\.pdf")),
    ("THE-AFFINE-PLANE", re.compile(r"AG\(\d, \d\)")),
)

NUM_RE = re.compile(r"(?<![\w.])(\d[\d,]*\d|\d)(?![\w])")
FENCE_RE = re.compile(r"```[^\n]*\n(.*?)```", re.S)
NOF_RE = re.compile(r"([\d,]+)\s+of\s+([\d,]+)")
TABLE_ROW_RE = re.compile(r"^\|.*\|\s*$", re.M)


def paper_render(R):
    """the claims and tables the paper must carry, RENDERED FROM THE RECEIPT
    so that the paper can never drift from the run."""
    S = R["separation"]
    C = {(a["localization"], a["separation"]): a for a in R["counts"]
         ["arms_route_one"]}
    prim = C[("LOC-PAIR", "SEP-LINK-DISJOINT")]
    walk = C[("LOC-WALK", "SEP-LINK-DISJOINT")]
    rel = C[("LOC-PAIR", "SEP-ACTOR-DISJOINT")]
    D = R["descriptions"]
    E = R["e5_audit"]
    T = R["shadow_theorem"]
    A = R["analytic_legs"]
    Cj = R["conjugacy"]
    red = [x for x in R["reductions"]["arms"]
           if x["localization"] == "LOC-WALK"
           and x["separation"] == "SEP-LINK-DISJOINT"][0]
    claims = [
        ("C01", "two sites are unlinked exactly when they lie on a common "
         "line of the one parallel class the arena does not declare, at %s "
         "of %s ordered site pairs"
         % (com(R["arena"]["ordered_site_pairs_checked"]),
            com(R["arena"]["ordered_site_pairs_checked"]))),
        ("C02", "%s of %s subsets of the nine actors own a record quantity "
         "and a conditioning region sharing no link with them"
         % (com(S["subsets_with_both"]), com(S["subset_lattice"]))),
        ("C03", "%s subsets own a record quantity and %s have a nonempty far "
         "region" % (com(S["subsets_owning_a_record_quantity"]),
                     com(S["subsets_with_a_nonempty_far_region"]))),
        ("C04", "of %s ordered block pairs %s are link-disjoint and %s carry "
         "a record quantity at the block, and %s carry both"
         % (com(S["ordered_block_pairs"]),
            com(S["link_disjoint_block_pairs"]),
            com(S["quantity_bearing_at_LOC_PAIR"]),
            com(S["premise_instances_at_LOC_PAIR"]))),
        ("C05", "in the state's own localization the same predicates return "
         "%s instances of the premise"
         % com(S["premise_instances_at_LOC_WALK"])),
        ("C06", "the record field is site-constant at %s of %s committed "
         "histories" % (com(R["corpora"]["record_is_site_constant_at"]),
                        com(R["corpora"]["of_histories"]))),
        ("C07", "the corpus carries %s distinct records and the shadow can "
         "separate at most %s of them"
         % (com(D["distinct_records_in_the_corpus"]),
            com(D["residue_classes_up_to_the_site_phase"]))),
        ("C08", "not one of the %s declared states separates two committed "
         "records that share a residue class"
         % com(D["state_sweep_size"])),
        ("C09", "at the state's localization and EPR's own separation the "
         "record certifies %s elements and the shadow carries %s of them"
         % (com(walk["certainty_elements"]),
            com(walk["certainty_elements"]
                - walk["without_counterpart_in_D_SHADOW"]))),
        ("C10", "the shadow itself certifies %s elements at any of the four "
         "arms" % com(walk["certainty_elements_certified_by_D_SHADOW"])),
        ("C11", "at the record's own localization under the weaker "
         "separation the census runs at %s pairs and %s quantities"
         % (com(rel["premise_instances"]), com(rel["quantities"]))),
        ("C12", "the five declared readings assign more than one description "
         "to the same record at %s of %s probes, and as many as %s"
         % (com(red["probes_with_more_than_one"]), com(red["probes"]),
            com(red["largest"]))),
        ("C13", "B's own record moves at %s of %s probes and the description "
         "assigned to B moves at %s"
         % (com(E["probes_where_B_s_record_moves_with_the_reading_at_A"]),
            com(E["probes"]),
            com(E["probes_where_the_description_ASSIGNED_to_B_moves"]))),
        ("C14", "the two declared coin orders' operators differ at %s of the "
         "%s committed records"
         % (com(R["conjugacy"]["records_where_the_two_orders_differ"]),
            com(R["conjugacy"]["records"]))),
        ("C15", "the record carries both members of the conjugate pair at %s "
         "of %s committed histories"
         % (com(R["conjugacy"]["histories_where_D_RECORD_carries_both"]),
            com(R["conjugacy"]["of_histories"]))),
        ("C16", "over the %s event shapes this arena admits, an event "
         "confined to an actor-disjoint region changes a record entry the "
         "other block owns %s times, while %s unconfined ones do reach a "
         "block's quantities"
         % (com(S["dynamical_no_disturbance"]["event_shapes"]),
            com(S["dynamical_no_disturbance"]["disturbances"]),
            com(S["dynamical_no_disturbance"]
                ["events_that_do_reach_a_block_quantity"]))),
        # THE REPAIR'S OWN LOAD-BEARING SENTENCES, rendered like the rest.
        ("C17", "no residue class of this corpus is a single record, and "
         "none is constant in any direction: %s of %s and %s of %s"
         % (com(T["L3_singleton_classes"]), com(T["L3_residue_classes"]),
            com(T["L3_direction_constant_classes"]),
            com(T["L3_residue_classes"]))),
        ("C18", "over paper-20's own %s-value alphabet the sweep runs at %s "
         "states, the ceiling of %s menus is attained at %s of them, and the "
         "shadow carries a certified direction at %s"
         % (com(T["parent_alphabet_size"]),
            com(T["parent_alphabet_states"]),
            com(T["parent_alphabet_best_distinct_menus"]),
            com(T["parent_alphabet_states_attaining_the_ceiling"]),
            com(T["parent_alphabet_states_carrying_a_direction"]))),
        ("C19", "the quantity censused at a block is one of the block's own "
         "localization's directions at %s of %s declared specs"
         % (com(A["specs_where_the_quantity_lies_in_the_block_s_own_"
                  "directions"]),
            com(A["declared_specs"]))),
        ("C20", "the two coin orders commute at exactly the %s records whose "
         "three counts are equal modulo three, and at %s of those the record "
         "observable is not scalar"
         % (com(Cj["records_where_the_two_orders_commute"]),
            com(Cj["of_those_where_the_record_observable_is_not_scalar"]))),
    ]
    # HOW MANY TIMES EACH CLAIM MUST OCCUR (K3 MAJOR-3).  Containment is what
    # E-22 was bought to forbid: five of these sentences are said twice, in
    # the summary and again in their own section, and a containment gate lets
    # one copy be forged while the other satisfies it.  The multiplicity is
    # DECLARED here and the paper's occurrence count must equal it exactly,
    # so both forging a copy and planting a twin fail.
    multiplicity = {"C02": 2, "C04": 2, "C05": 2, "C07": 2, "C08": 2,
                    "C17": 2}
    claims = [(cid, txt, multiplicity.get(cid, 1)) for cid, txt in claims]
    tables = [
        {"name": "T-ARMS",
         "headers": ["localization", "separation", "pairs", "quantities",
                     "certified", "uncarried by the shadow", "word"],
         "rows": [[a["localization"], a["separation"],
                   com(a["premise_instances"]), com(a["quantities"]),
                   com(a["certainty_elements"]),
                   com(a["without_counterpart_in_D_SHADOW"]), a["word"]]
                  for a in R["counts"]["arms_route_one"]]},
        {"name": "T-CONTROLS",
         "headers": ["arm", "premise instances", "certified",
                     "uncarried by the record", "uncarried by the shadow",
                     "word"],
         "rows": [[c["arm"], com(c["premise_instances"]),
                   com(c["certainty_elements"]),
                   com(c["without_counterpart_in_D_RECORD"]),
                   com(c["without_counterpart_in_D_SHADOW"]), c["word"]]
                  for c in R["controls"]["rows"]]},
        {"name": "T-REDUCTIONS",
         "headers": ["arm", "assignments at one record", "probes"],
         "rows": [["%s x %s" % (a["localization"], a["separation"]), k,
                   com(v)] for a in R["reductions"]["arms"]
                  for k, v in sorted(a["distinct_assigned_descriptions"]
                                     .items())]},
        {"name": "T-READINGS",
         "headers": ["reading", "cells", "largest fibre"],
         "rows": [[r["reading"], com(r["cells"]), com(r["largest_fibre"])]
                  for r in R["readings"]["rows"]]},
        # THE FIFTH TABLE.  It carries this unit's Bell obligations and it
        # was the one table the instrument did not render (K3 MAJOR-1): a
        # header swap, an inverted row and a flipped constrained-flag all
        # passed.  It renders here like every other.
        {"name": "T-BELL",
         "headers": ["desideratum", "D-RECORD", "D-SHADOW",
                     "Bell-constrained"],
         "rows": [list(d["paper_cells"]) for d in R["bell"]["desiderata"]]},
    ]
    return claims, tables


POLARITY = (
    ("P1", "the criterion is inapplicable at the record's own localization",
     "the criterion is applicable at the record's own localization"),
    ("P2", "the shadow carries none of the certified elements",
     "the shadow carries every certified element"),
    ("P3", "B's record does not move with the reading declared at A",
     "B's record moves with the reading declared at A"),
    ("P4", "the record carries both members of the conjugate pair",
     "the record carries neither member of the conjugate pair"),
    ("P5", "the premise exists in the state's localization",
     "the premise exists in no localization"),
    # THE DILEMMA'S TWO HORNS ARE DIRECTIONS TOO (K3 PROBE 2).  Swapping them
    # in section 7's prose left every numeral in the paper correct and no
    # claim touched, so nothing fired; here each horn's assignment is an axis.
    ("P6", "horn (1) holds for D-SHADOW", "horn (2) holds for D-SHADOW"),
    ("P7", "horn (2) fails for D-RECORD", "horn (1) fails for D-RECORD"),
)

# EVERY UNIVERSE DECLARES ITS BOUND (K3 MINOR-7).  Membership alone lets an
# in-universe falsehood through -- "the shadow separates 36 of 36 records"
# has both members in RECORDS.  So a fraction must name a universe whose
# DECLARED BOUND is its denominator and one of whose declared VALUES is its
# numerator, and the numerator may not exceed the bound.
REFERENT_UNIVERSES = {
    "HISTORIES": {
        "bound": "corpora/histories",
        "values": ("corpora/record_is_site_constant_at",
                   "conjugacy/histories_where_D_RECORD_carries_both",
                   "blocks/forced_at")},
    "SUBSETS": {
        "bound": "separation/subset_lattice",
        "values": ("separation/subsets_owning_a_record_quantity",
                   "separation/subsets_with_a_nonempty_far_region",
                   "separation/subsets_with_both")},
    "BLOCK-PAIRS": {
        "bound": "separation/ordered_block_pairs",
        "values": ("separation/link_disjoint_block_pairs",
                   "separation/quantity_bearing_at_LOC_PAIR",
                   "separation/quantity_bearing_at_LOC_WALK",
                   "separation/premise_instances_at_LOC_PAIR",
                   "separation/premise_instances_at_LOC_WALK")},
    "RECORDS": {
        "bound": "descriptions/distinct_records_in_the_corpus",
        "values": ("descriptions/residue_classes_up_to_the_site_phase",
                   "conjugacy/records_where_the_two_orders_differ",
                   "conjugacy/records_where_the_two_orders_commute",
                   "conjugacy/records_where_the_Born_menu_carries_the_record_"
                   "menu")},
    "STATES": {
        "bound": "descriptions/state_sweep_size",
        "values": ("descriptions/states_separating_two_records_of_one_residue_"
                   "class",)},
    "PARENT-STATES": {
        "bound": "shadow_theorem/parent_alphabet_states",
        "values": ("shadow_theorem/parent_alphabet_states_attaining_the_"
                   "ceiling",
                   "shadow_theorem/parent_alphabet_states_carrying_a_"
                   "direction")},
    "RESIDUE-CLASSES": {
        "bound": "shadow_theorem/L3_residue_classes",
        "values": ("shadow_theorem/L3_singleton_classes",
                   "shadow_theorem/L3_direction_constant_classes")},
    "DECLARED-SPECS": {
        "bound": "analytic_legs/declared_specs",
        "values": ("analytic_legs/specs_where_the_quantity_lies_in_the_block_"
                   "s_own_directions",
                   "analytic_legs/specs_where_the_quantity_lies_in_the_"
                   "conditioner_s_directions")},
    "E4-PROBES": {
        "bound": "reductions/arms/1/probes",
        "values": ("reductions/arms/1/probes_with_more_than_one",)},
    "E5-PROBES": {
        "bound": "e5_audit/probes",
        "values": ("e5_audit/probes_where_B_s_record_moves_with_the_reading_"
                   "at_A",
                   "e5_audit/probes_where_B_s_own_shadow_moves",
                   "e5_audit/probes_where_the_description_ASSIGNED_to_B_"
                   "moves")},
    "SITE-PAIRS": {"bound": "arena/ordered_site_pairs_checked",
                   "values": ("arena/ordered_site_pairs_checked",)},
}
# THE ONLY PLACES "element of reality" MAY STAND (K2 M4).  Each carrier is
# matched in the paper's own bytes and its occurrences of the phrase are
# counted; the paper's total must equal the sum, so a sentence in the unit's
# own voice fails even with every carrier still present.
ELEMENT_CARRIERS = (
    ("THE-CRITERION-QUOTED", "then there exists an element of physical "
     "reality corresponding to this physical quantity."),
    ("THE-COMPLETENESS-CONDITION-QUOTED", "every element of the physical "
     "reality must have a counterpart in the physical theory."),
    ("THE-PREDICATE-DECLARED", "EPR-REALITY(q | D, B, sep) is the formalised "
     "criterion and the only predicate in this unit that carries the phrase "
     "element of reality"),
    ("THE-SELF-CERTIFICATION", "The phrase \"element of reality\" occurs in "
     "this unit only inside the formalised predicate's own declaration and "
     "inside verbatim quotation of the 1935 paper"),
)


def paper_battery(R, paper_text, claims, tables):
    say("SECTION 15b.  THE PAPER INSTRUMENT")
    # FALSIFIER MUT-BELL-PLANT: a banned local-realism sentence is planted
    # into the paper
    if mut("MUT-BELL-PLANT"):
        paper_text = paper_text + "\n\nlocal realism is restored.\n"
    # FALSIFIER MUT-BELL-VOICE: the banned claim is planted in the active
    # voice, which no literal blacklist catches
    if mut("MUT-BELL-VOICE"):
        paper_text = paper_text + \
            "\n\nOn the measured arms this restores local realism.\n"
    # FALSIFIER MUT-BELL-DELETE: the paper's own statement of the corpus's
    # standing Bell verdict is removed
    if mut("MUT-BELL-DELETE"):
        for _n, _s, _g, needle in ANCHORS:
            if _n == "A-BELL-E1":
                paper_text = paper_text.replace(
                    "**ISP cannot satisfy Bell local causality and still\n"
                    "reproduce the Tsirelson violation. It is "
                    "Bell-nonlocal.**",
                    "the corpus's Bell status is discussed in v5 paper-14.")
    # FALSIFIER MUT-ELEMENT-PLANT: the walled phrase is used in the unit's
    # own voice, outside the predicate and outside quotation
    if mut("MUT-ELEMENT-PLANT"):
        paper_text = paper_text + \
            "\n\nThere is an element of reality at every block.\n"
    # FALSIFIER MUT-PAPER-NUMERAL: an unregistered numeral is planted into
    # the paper
    if mut("MUT-PAPER-NUMERAL"):
        paper_text = paper_text + "\n\nthe census ran at 424,242 pairs.\n"
    # FALSIFIER MUT-PAPER-SPELLED: an unmapped spelled numeral is planted
    # into the paper
    if mut("MUT-PAPER-SPELLED"):
        paper_text = paper_text + \
            "\n\nThe census ran at forty-two pairs across ninety blocks.\n"
    # FALSIFIER MUT-PAPER-TABLE-HEADER: two table headers are swapped with
    # every number left correct
    if mut("MUT-PAPER-TABLE-HEADER"):
        paper_text = paper_text.replace("| localization | separation |",
                                        "| separation | localization |")
    # FALSIFIER MUT-PAPER-TABLE-ROW: a fabricated row built out of
    # registered numerals is appended to a rendered table
    if mut("MUT-PAPER-TABLE-ROW"):
        paper_text = paper_text.replace(
            "| LOC-WALK | SEP-ACTOR-DISJOINT | 421,656 | 1,265,112 | "
            "1,265,112 | 1,265,112 | EPR-SHADOW-INCOMPLETE-RECORD-COMPLETE |",
            "| LOC-WALK | SEP-ACTOR-DISJOINT | 421,656 | 1,265,112 | "
            "1,265,112 | 1,265,112 | EPR-SHADOW-INCOMPLETE-RECORD-COMPLETE |"
            "\n| LOC-WALK | SEP-LINK-DISJOINT | 105,408 | 316,224 | 316,224 "
            "| 0 | EPR-BOTH-COMPLETE |")
    # FALSIFIER MUT-CLAIM-TWIN: a duplicated claim's twin is forged, leaving
    # its clean copy in place to satisfy a containment gate
    if mut("MUT-CLAIM-TWIN"):
        paper_text = paper_text.replace(
            "`0 of 512 subsets of the nine actors own a record quantity and "
            "a\nconditioning region sharing no link with them`",
            "`512 of 512 subsets of the nine actors own a record quantity "
            "and a\nconditioning region sharing no link with them`", 1)
    # FALSIFIER MUT-FENCE: a verdict fence is altered in one of its two
    # printed copies
    if mut("MUT-FENCE"):
        paper_text = paper_text.replace(";NO-LOCAL-REALISM-CLAIM>", ">")
    # FALSIFIER MUT-POLARITY: an inverted claim is planted into the paper
    if mut("MUT-POLARITY"):
        paper_text = paper_text + "\n\n" + POLARITY[2][2] + ".\n"
    hay = canon(paper_text)
    for cid, txt, mult in claims:
        say("    %s x%d  %s" % (cid, mult, txt))
    for t in tables:
        say("    %s | %s |" % (t["name"], " | ".join(t["headers"])))
        for row in t["rows"]:
            say("            | %s |" % " | ".join(row))
    cmiss = ["%s(%d/%d)" % (cid, hay.count(canon(txt)), mult)
             for cid, txt, mult in claims
             if hay.count(canon(txt)) != mult]
    R["paper_claims"] = {
        "rows": [{"id": c, "claim": t, "declared_occurrences": reg(m),
                  "found_occurrences": reg(hay.count(canon(t)))}
                 for c, t, m in claims],
        "count": reg(len(claims)),
        "total_declared_occurrences": reg(sum(m for _c, _t, m in claims)),
        "wrong_occurrence_count": cmiss,
        "note": "the count is DECLARED per claim and compared exactly: five "
                "of these sentences are said twice, and a containment gate "
                "would let one copy be forged while its twin satisfied it"}
    LD.gate("G-PAPER-CLAIMS",
            "EVERY LOAD-BEARING SENTENCE OF THE PAPER IS RENDERED FROM THE "
            "RECEIPT AND MATCHED IN THE PAPER'S OWN BYTES BY OCCURRENCE "
            "COUNT (#20, E-22).  %d claims, each built out of receipt values "
            "rather than typed and each declaring how many times it is said, "
            "so a paper that drifts from its run cannot pass and neither can "
            "a forged twin of a sentence said twice" % len(claims),
            not cmiss, "claims %d, declared occurrences %d, wrong counts %s"
            % (len(claims), sum(m for _c, _t, m in claims), cmiss or "none"))
    SEAL.take("SEAL-PAPER-CLAIMS", R)

    # THE FENCED BLOCKS ARE MATCHED BY MULTISET (K3 MAJOR-2).  The three
    # verdict segments are printed twice each and were gated nowhere: a
    # forged head, a struck NO-LOCAL-REALISM-CLAIM stamp and a flipped count
    # all promoted clean.  E-22's rule is multiset equality, and this is it.
    segs = [R["verdict"]["segment_1"], R["verdict"]["segment_2"],
            R["verdict"]["segment_3"]]
    want = Counter({canon(s): 2 for s in segs})
    got = Counter(canon(b) for b in FENCE_RE.findall(paper_text))
    fdiff = sorted((got - want).elements()) + sorted((want - got).elements())
    R["paper_fences"] = {
        "declared_blocks": [{"segment": i + 1, "occurrences": reg(2)}
                            for i in range(len(segs))],
        "fenced_blocks_in_the_paper": reg(sum(got.values())),
        "distinct_blocks": reg(len(got)),
        "mismatches": [d[:80] for d in fdiff],
        "note": "the paper's fenced blocks must be exactly the run's three "
                "verdict segments, twice each -- MULTISET equality, not "
                "containment"}
    LD.gate("G-PAPER-FENCES-MATCH-THE-VERDICT",
            "THE VERDICT FENCES ARE THE RUN'S OWN, BY MULTISET (E-22).  The "
            "paper prints three fenced blocks twice each; they are compared "
            "as a multiset against the three segments this run emitted, so a "
            "word changed in one copy, a stamp struck from both, or an extra "
            "block anywhere fails here",
            not fdiff, "fenced blocks %d, distinct %d, mismatches %d"
            % (sum(got.values()), len(got), len(fdiff)))
    SEAL.take("SEAL-PAPER-FENCES", R)

    # THE TABLES ARE MATCHED BY MULTISET TOO (K3 MAJOR-1, MINOR-6): every
    # rendered table must appear whole, and the paper must carry no table
    # block the run did not render and no row inside one that it did not.
    blocks, cur = [], []
    for line in paper_text.split("\n"):
        if line.strip().startswith("|"):
            cur.append(canon(line))
        elif cur:
            blocks.append(cur)
            cur = []
    if cur:
        blocks.append(cur)
    tmiss = []
    for t in tables:
        head = canon("| " + " | ".join(t["headers"]) + " |")
        hits = [b for b in blocks if b and b[0] == head]
        if len(hits) != 1:
            tmiss.append("%s/headers(%d)" % (t["name"], len(hits)))
            continue
        body = Counter(r for r in hits[0][1:]
                       if set(r.replace("|", "").replace(" ", "")) - set("-:"))
        rendered = Counter(canon("| " + " | ".join(row) + " |")
                           for row in t["rows"])
        for d in sorted((body - rendered).elements()):
            tmiss.append("%s/extra:%s" % (t["name"], d[:60]))
        for d in sorted((rendered - body).elements()):
            tmiss.append("%s/absent:%s" % (t["name"], d[:60]))
    if len(blocks) != len(tables):
        tmiss.append("table blocks %d, rendered tables %d"
                     % (len(blocks), len(tables)))
    R["paper_tables"] = {"tables": tables, "count": reg(len(tables)),
                         "rows": reg(sum(len(t["rows"]) for t in tables)),
                         "table_blocks_in_the_paper": reg(len(blocks)),
                         "missing": tmiss}
    LD.gate("G-PAPER-TABLES-WITH-HEADERS",
            "EVERY TABLE IS RENDERED FROM THE RECEIPT WITH ITS HEADERS "
            "INCLUDED AND MATCHED BY MULTISET, so a header swap that leaves "
            "every number correct dies here, and so does a fabricated row "
            "built out of registered numerals, and so does a table the run "
            "never rendered (E-22: tables render as claims).  All five of "
            "the paper's tables are rendered -- including the section 9 "
            "desiderata table, which is the one that carries the Bell wall",
            not tmiss, "tables %d, rows %d, table blocks in the paper %d, "
            "mismatches %s"
            % (len(tables), sum(len(t["rows"]) for t in tables), len(blocks),
               tmiss or "none"))
    SEAL.take("SEAL-PAPER-TABLES", R)

    fenced = FENCE_RE.findall(paper_text)
    nums = NUM_RE.findall(paper_text)
    fnums = [n for blk in fenced for n in NUM_RE.findall(blk)]
    spans = []
    for cname, rx in LITERAL_CONTEXTS:
        for m in rx.finditer(paper_text):
            spans.append((m.start(), m.end(), cname))
    unknown, litrows = [], Counter()
    for m in NUM_RE.finditer(paper_text):
        tok = m.group(1)
        if tok in NUMREG or tok.replace(",", "") in NUMREG:
            continue
        home = [c for s, e, c in spans if s <= m.start() and m.end() <= e]
        if home:
            litrows[home[0]] += 1
        else:
            unknown.append(tok)
    unknown = sorted(set(unknown))
    tokens = [w for w in re.findall(r"[a-z]+", paper_text.lower())
              if w in NUMBER_WORD_SHAPES]
    words = [w for w in tokens if w in WORDNUM]
    unmapped = sorted({w for w in tokens
                       if w not in WORDNUM and w not in ORDINAL_WORDS})
    wordbad = sorted({w for w in words if str(WORDNUM[w]) not in NUMREG})
    R["paper_coverage"] = {
        "numerals": reg(len(nums)), "in_fenced_blocks": reg(len(fnums)),
        "spelled_numerals": reg(len(words)),
        "number_word_tokens": reg(len(tokens)),
        "registry_size": reg(len(NUMREG)),
        "structural_literals_by_context": {k: reg(v) for k, v
                                           in sorted(litrows.items())},
        "declared_literal_contexts": [c for c, _rx in LITERAL_CONTEXTS],
        "unknown_numerals": unknown, "unknown_spelled": wordbad,
        "unmapped_number_words": unmapped,
        "note": "coverage includes fenced blocks and inline code spans "
                "(E-22); the registry is the run's own product, and a "
                "numeral that is not in it passes only inside a DECLARED "
                "identifier shape at its own position -- there is no bare "
                "allow-list of tokens"}
    LD.gate("G-PAPER-NUMERAL-COVERAGE",
            "EVERY NUMERAL IN THE PAPER IS THE RUN'S OWN PRODUCT, OR AN "
            "IDENTIFIER IN A DECLARED SHAPE (#20, E-22).  The scan covers "
            "the whole file including fenced blocks and inline spans; a "
            "numeral outside the registry must sit inside one of the "
            "declared identifier contexts -- a section heading, a paper or "
            "ledger reference, an engraving, the 1935 citation -- matched at "
            "its own position, so a token like 19 or 27 is not whitelisted "
            "wherever it appears.  Spelled numerals are scanned through a "
            "vocabulary of every English number word, and one that the map "
            "cannot resolve fails rather than passing unseen",
            not unknown and not wordbad and not unmapped,
            "numerals %d (fenced %d), structural %s, spelled %d of %d "
            "number-word tokens, unknown %s / %s, unmapped %s"
            % (len(nums), len(fnums), dict(litrows), len(words), len(tokens),
               unknown or "none", wordbad or "none", unmapped or "none"))
    SEAL.take("SEAL-PAPER-COVERAGE", R)

    prows, pbad = [], []
    for pid, good, bad in POLARITY:
        g = canon(good) in hay
        b = canon(bad) in hay
        prows.append({"axis": pid, "asserted": g, "inverse_present": b})
        if b or not g:
            pbad.append(pid)
    R["polarity"] = {"rows": prows, "count": reg(len(prows)),
                     "failures": pbad}
    LD.gate("G-PAPER-CLAIM-POLARITY",
            "EVERY POLARITY AXIS IS CHECKED IN BOTH DIRECTIONS.  %d axes -- "
            "the head's applicability, the shadow's carrying, B's record, the "
            "record's conjugate pair, the premise's localization and the two "
            "horns of EPR's dilemma; the paper must assert the measured "
            "direction and must not contain its inverse anywhere in its bytes"
            % len(POLARITY),
            not pbad, "axes %d, failures %s" % (len(prows), pbad or "none"))
    SEAL.take("SEAL-POLARITY", R)

    uni = {}
    for name, spec in REFERENT_UNIVERSES.items():
        # the bound is NOT admitted as a numerator unless the run measured it
        # as one: "the shadow separates 36 of 36 records" is an in-universe
        # falsehood, and it fails here because 36 is this universe's total and
        # not a quantity measured in it (K3 MINOR-7).
        bound = int(jpath(R, spec["bound"]))
        vals = {int(jpath(R, p)) for p in spec["values"]}
        uni[name] = {"bound": bound, "values": sorted(vals)}
    frac, fbad = [], []
    for a, b in NOF_RE.findall(paper_text):
        na, nb = int(a.replace(",", "")), int(b.replace(",", ""))
        homes = [n for n, u in sorted(uni.items())
                 if nb == u["bound"] and na in u["values"] and na <= nb]
        frac.append({"fraction": "%s of %s" % (a, b), "universes": homes})
        if not homes:
            fbad.append("%s of %s" % (a, b))
    # FALSIFIER MUT-REFERENT: a fraction with no declared referent universe
    # is planted into the scan
    if mut("MUT-REFERENT"):
        for a, b in NOF_RE.findall(
                "\n\nthe shadow separates 36 of 512 records.\n"):
            na, nb = int(a.replace(",", "")), int(b.replace(",", ""))
            homes = [n for n, u in sorted(uni.items())
                     if nb == u["bound"] and na in u["values"] and na <= nb]
            frac.append({"fraction": "%s of %s" % (a, b), "universes": homes})
            if not homes:
                fbad.append("%s of %s" % (a, b))
    R["referent_binding"] = {
        "universes": {k: {"bound": reg(v["bound"]),
                          "values": [reg(x) for x in v["values"]]}
                      for k, v in sorted(uni.items())},
        "fractions": frac, "count": reg(len(frac)), "unbound": fbad,
        "note": "every 'N of M' in the paper must name a declared universe "
                "whose BOUND is M and one of whose declared VALUES is N, with "
                "N at most M: membership alone would pass an in-universe "
                "falsehood, so the denominator has to be the universe's own "
                "total and the numerator a quantity this run measured in it"}
    LD.gate("G-SENTENCE-REFERENT-BINDING",
            "EVERY FRACTION IN THE PAPER IS RESOLVED AGAINST A DECLARED "
            "UNIVERSE, BOUND AND VALUE.  %d universes are declared from "
            "receipt paths, each with the total it counts over; an 'N of M' "
            "passes only when M is that total, N is a value this run measured "
            "in it, and N does not exceed M" % len(uni),
            not fbad, "fractions %d, unbound %s" % (len(frac), fbad or "none"))
    SEAL.take("SEAL-REFERENT", R)

    # THE WALLED PHRASE, COUNTED (K2 M4).  §11 certifies that "element of
    # reality" occurs only inside the formalised predicate and inside
    # verbatim quotation.  That certificate had no gate and was false; this
    # is the gate, and the accounting is exact.
    occ = len(ELEMENT_RE.findall(hay))
    carrows, accounted = [], 0
    for cname, carrier in ELEMENT_CARRIERS:
        c = canon(carrier)
        n = hay.count(c)
        per = len(ELEMENT_RE.findall(c))
        accounted += n * per
        carrows.append({"carrier": cname, "occurrences_in_the_paper": reg(n),
                        "phrase_occurrences_each": reg(per)})
    R["element_of_reality"] = {
        "pattern": ELEMENT_RE.pattern,
        "occurrences_in_the_paper": reg(occ),
        "accounted_for_by_the_declared_carriers": reg(accounted),
        "carriers": carrows,
        "note": "the phrase may stand only inside the formalised predicate's "
                "own declaration and inside verbatim quotation of 1935; the "
                "paper's total is compared with the carriers' own count, so "
                "a sentence in this unit's voice fails even though every "
                "carrier is still present"}
    LD.gate("G-ELEMENT-OF-REALITY-CONFINED",
            "THE PHRASE 'ELEMENT OF REALITY' IS WALLED, AND THE WALL IS "
            "COUNTED.  Every occurrence in the paper must be accounted for "
            "by a declared carrier -- the formalised predicate's own "
            "declaration, or a verbatim quotation of the 1935 paper -- and "
            "the totals are compared exactly, so this unit cannot answer "
            "EPR's question in its own voice",
            occ == accounted and occ > 0,
            "occurrences %d, accounted for %d, carriers %d"
            % (occ, accounted, len(ELEMENT_CARRIERS)))
    SEAL.take("SEAL-ELEMENT", R)

    licensed, lrows = [], []
    for lname, passage in WALL_LICENSED:
        c = canon(passage)
        n, at = 0, hay.find(c)
        while at >= 0:
            licensed.append((at, at + len(c)))
            n += 1
            at = hay.find(c, at + 1)
        lrows.append({"passage": lname, "occurrences": reg(n)})
    hits = [s for s in BANNED if canon(s) in hay]
    phits, pexcused = [], 0
    for pid, pat in BANNED_PATTERNS:
        for m in re.finditer(pat, hay, re.I):
            if any(s <= m.start() and m.end() <= e for s, e in licensed):
                pexcused += 1
            else:
                phits.append(pid)
    R["walls"] = {"banned": list(BANNED), "count": reg(len(BANNED)),
                  "patterns": [p for p, _x in BANNED_PATTERNS],
                  "pattern_count": reg(len(BANNED_PATTERNS)),
                  "licensed_passages": lrows,
                  "pattern_hits_inside_the_licensed_passages": reg(pexcused),
                  "hits": hits, "pattern_hits": sorted(set(phits)),
                  "scanned": PAPER_REL,
                  "note": "the Bell wall is scanned against this unit's own "
                          "bytes -- the leg the wall is owed -- as seven "
                          "exact sentences AND as voice-normalised patterns, "
                          "because a blacklist is defeated by re-voicing"}
    LD.gate("G-WALLS-SCAN-THE-PAPER",
            "THE BELL WALL IS SCANNED AGAINST THIS UNIT'S OWN PAPER, IN BOTH "
            "VOICES.  Seven banned assertive sentences -- local realism "
            "restored, Bell evaded, hidden variables vindicated among them -- "
            "and %d voice-normalised patterns that catch the same claims "
            "said actively, at a distance, or in the passive: restoring "
            "local realism or locality, evading or circumventing Bell, a "
            "local hidden variable, a vindicated hidden-variable completion, "
            "a refuted spooky action, a vindicated Einstein.  All are matched "
            "against the paper's normalised bytes and must be absent OUTSIDE "
            "the two declared passages that are allowed to carry those words "
            "-- the verbatim standing verdict the paper is required to state, "
            "and the paper's own denial -- both of which are gated in their "
            "own right; two falsifiers plant one each, in either voice"
            % len(BANNED_PATTERNS),
            not hits and not phits,
            "banned %d, hits %s; patterns %d, hits outside the licensed "
            "passages %s, hits inside them %d; licensed passages found %d"
            % (len(BANNED), hits or "none", len(BANNED_PATTERNS),
               sorted(set(phits)) or "none", pexcused, len(licensed)))
    SEAL.take("SEAL-WALLS", R)

    # THE WALL'S POSITIVE LEG (K3 MAJOR-7).  A wall with only a blacklist is
    # satisfied by silence: a paper-38 that quietly deleted its Bell section
    # passed every gate.  The standing verdict must be STATED here.
    prows = []
    for nm, _src, gate, needle in ANCHORS:
        if gate == "G-BELL-WALL-STATED-IN-THE-PAPER":
            prows.append({"anchor": nm, "stated_in_the_paper":
                          bool(match_needle(paper_text, needle))})
    pmiss = [r["anchor"] for r in prows if not r["stated_in_the_paper"]]
    lmiss = [r["passage"] for r in lrows if r["occurrences"] != 1]
    R["bell_wall_positive_leg"] = {
        "rows": prows, "count": reg(len(prows)), "missing": pmiss,
        "licensed_passages": lrows, "licensed_passages_missing": lmiss,
        "note": "v5 paper-14's two verdict sentences are required VERBATIM "
                "in this paper's own bytes, so the wall cannot be satisfied "
                "by deleting the section that carries it; and the two "
                "passages the pattern scan licenses -- the standing verdict "
                "and this unit's own denial -- must each stand exactly once, "
                "so the licence cannot be widened by repeating them"}
    LD.gate("G-BELL-WALL-STATED-IN-THE-PAPER",
            "THE STANDING BELL VERDICT IS STATED, NOT MERELY NOT "
            "CONTRADICTED.  v5 paper-14's two sentences -- ISP is "
            "Bell-nonlocal, and ISP is no-signalling and "
            "parameter-independent -- are matched verbatim in this paper's "
            "own bytes as well as in their source's, so a paper-38 that "
            "silently dropped its Bell section would fail here.  The two "
            "passages the pattern scan licenses must each stand exactly once",
            not pmiss and not lmiss
            and consume("G-BELL-WALL-STATED-IN-THE-PAPER", R),
            "wall sentences required in the paper %d, missing %s; licensed "
            "passages %s, not standing exactly once %s"
            % (len(prows), pmiss or "none",
               [(r["passage"], r["occurrences"]) for r in lrows],
               lmiss or "none"))
    SEAL.take("SEAL-BELL-POSITIVE", R)
    return paper_text


# --------------------------------------------------------------------------
# THE FALSIFIER REGISTRY (#82, E-23)
# --------------------------------------------------------------------------

MUTANTS = (
    ("MUT-SOURCE-DIGEST", "G-PROVENANCE-SHA-PINNED",
     "a source's digest is reported as something else", "provenance"),
    ("MUT-ANCHOR-E2", "G-VERBATIM-ANCHORS-IN-SOURCE",
     "the reality criterion's needle is altered by one word", "provenance"),
    ("MUT-OUTCOME-TYPED", "G-OUTCOMES-PARSED-FROM-THE-PIN",
     "the outcome vocabulary is typed instead of parsed", "provenance"),
    ("MUT-LINKGRAPH", "G-LINK-GRAPH-MEASURED",
     "the undeclared direction is declared, so the link graph is complete",
     "link_set"),
    ("MUT-CARRIER", "G-CELL-IS-A-CO-DIVISION-PAIR",
     "the cell-to-pair bijection is asserted false", "arena_measure"),
    ("MUT-CORPUS-CAP", "G-CORPUS-AGREES-WITH-FAC",
     "the corpus is silently capped", "build_corpus"),
    ("MUT-SITECONST", "G-RECORD-SITE-CONSTANT",
     "one history's record is reported as not site-constant",
     "corpus_measure"),
    ("MUT-BLOCKS-DROP", "G-BLOCKS-AGREE-WITH-FAC",
     "the history leg is dropped, so coarse decompositions survive",
     "leg_history"),
    ("MUT-SEPARATION-LEAK", "G-SEPARATION-PREMISE-CENSUS",
     "link-disjointness is granted to every pair", "sep_link_disjoint"),
    ("MUT-DISTURBANCE-CONFINEMENT", "G-NO-DISTURBANCE-DYNAMICAL",
     "the confinement premise is dropped, so unconfined events are counted "
     "as confined ones", "disturbance_census"),
    ("MUT-SHADOW-INJECTIVE", "G-SHADOW-CEILING",
     "the shadow is allowed to read the count rather than its residue",
     "shadow_menu"),
    ("MUT-E4-COLLAPSE", "G-E4-TWO-REDUCTIONS",
     "every reading is made to assign the same description",
     "assigned_description"),
    ("MUT-CERT-CONSTANT-TRUE", "G-CERTAINTY-POLARITY",
     "the certainty predicate is made constantly true", "epr_reality_at"),
    ("MUT-COUNTERPART-BLIND", "G-CERTAINTY-CENSUS-PER-ARM",
     "the counterpart predicate is made constantly true",
     "epr_counterpart_at"),
    ("MUT-FIBER-ROWS", "G-CERTAINTY-CENSUS-PER-ARM",
     "the conditioning fibre is truncated to its own row, so every "
     "description carries everything", "fiber"),
    ("MUT-COMMUTATOR", "G-CONJUGATE-PAIR-MEASURED",
     "the two coin orders are reported as commuting", "conjugacy_measure"),
    ("MUT-CONJ-REFINE", "G-CONJUGATE-PAIR-MEASURED",
     "the conjugate pair is reported as jointly declarable",
     "conjugacy_measure"),
    ("MUT-E5-LEAK", "G-E5-RECORD-DOES-NOT-MOVE",
     "the reading declared at A is routed into B's own record and shadow",
     "record_at_B_under|shadow_at_B_under"),
    ("MUT-HEAD-TYPED", "G-HEAD-DERIVED-TWICE",
     "the head word is typed rather than derived", "verdict_measure"),
    ("MUT-CONTROL-MISSING", "G-EVERY-OUTCOME-WORD-EMITTABLE",
     "control arms are dropped so a word becomes undemonstrated",
     "controls_measure"),
    ("MUT-MEASURE", "G-PROBABILITY-EXACTLY-ONE",
     "one exact conditional probability is made to disagree",
     "controls_measure"),
    ("MUT-TOTALITY", "G-PREDICATES-FROZEN-BEFORE-THE-CENSUS",
     "a predicate is declared partial", "predicate_totality"),
    ("MUT-CLASSWORD", "G-CLASS-WORDS-BOUND-TO-PREDICATES",
     "a class word is typed rather than recomputed", "class_binding_measure"),
    ("MUT-BELL-PLANT", "G-WALLS-SCAN-THE-PAPER",
     "a banned local-realism sentence is planted into the paper",
     "paper_battery"),
    ("MUT-PAPER-NUMERAL", "G-PAPER-NUMERAL-COVERAGE",
     "an unregistered numeral is planted into the paper", "paper_battery"),
    ("MUT-PAPER-TABLE-HEADER", "G-PAPER-TABLES-WITH-HEADERS",
     "two table headers are swapped with every number left correct",
     "paper_battery"),
    ("MUT-POLARITY", "G-PAPER-CLAIM-POLARITY",
     "an inverted claim is planted into the paper", "paper_battery"),
    ("MUT-REFERENT", "G-SENTENCE-REFERENT-BINDING",
     "a fraction with no declared referent universe is planted into the scan",
     "paper_battery"),
    ("MUT-SEAL-DROP", "G-SEAL-TOTALITY",
     "one seal is not taken", "Seal"),
    ("MUT-INTEGRITY", "G-ARTIFACT-INTEGRITY",
     "the staged bytes are corrupted after sealing", "finish"),
    # THE REPAIR'S OWN FALSIFIERS.  Every gate this repair adds carries one,
    # and every hole the panel opened is closed by one that dies in it.
    ("MUT-RESIDUE-CARRIES", "G-SHADOW-CARRIES-NOTHING-AT-EVERY-STATE",
     "the residue partition is reported as carrying something, so the "
     "theorem's third leg is asserted rather than measured", "shadow_theorem"),
    ("MUT-SPEC-DOMAIN", "G-THE-ANALYTIC-LEGS-MEASURED",
     "the containment that makes the record's counterpart zero analytic is "
     "left unmeasured", "analytic_legs"),
    ("MUT-RESIDUE-CRITERION", "G-OPERATOR-LEG-IS-RESIDUE-DEGENERACY",
     "the operator leg is reported as tracking the observables rather than "
     "the count residue", "residue_degeneracy_census"),
    ("MUT-CONSUMER-PHANTOM", "G-ANCHOR-CONSUMERS-RAN",
     "an anchor's consumer is re-pointed at a gate that never ran, leaving "
     "its real consumer's other anchor in place so the consuming gate still "
     "passes", "provenance"),
    ("MUT-CAVEAT-UNUSED", "G-EPR-SUFFICIENCY-CAVEAT",
     "the sentence that puts EPR's caveat to work is deleted from the paper, "
     "leaving the quotation decorative", "provenance"),
    ("MUT-BELL-TABLE", "G-PAPER-TABLES-WITH-HEADERS",
     "the desiderata table's two description columns are swapped in the "
     "rendered row, with every flag left correct", "bell_measure"),
    ("MUT-BELL-VOICE", "G-WALLS-SCAN-THE-PAPER",
     "the banned claim is planted in the active voice, which no literal "
     "blacklist catches", "paper_battery"),
    ("MUT-BELL-DELETE", "G-BELL-WALL-STATED-IN-THE-PAPER",
     "the paper's own statement of the corpus's standing Bell verdict is "
     "removed", "paper_battery"),
    ("MUT-ELEMENT-PLANT", "G-ELEMENT-OF-REALITY-CONFINED",
     "the walled phrase is used in the unit's own voice, outside the "
     "predicate and outside quotation", "paper_battery"),
    ("MUT-PAPER-SPELLED", "G-PAPER-NUMERAL-COVERAGE",
     "an unmapped spelled numeral is planted into the paper", "paper_battery"),
    ("MUT-PAPER-TABLE-ROW", "G-PAPER-TABLES-WITH-HEADERS",
     "a fabricated row built out of registered numerals is appended to a "
     "rendered table", "paper_battery"),
    ("MUT-CLAIM-TWIN", "G-PAPER-CLAIMS",
     "a duplicated claim's twin is forged, leaving its clean copy in place "
     "to satisfy a containment gate", "paper_battery"),
    ("MUT-FENCE", "G-PAPER-FENCES-MATCH-THE-VERDICT",
     "a verdict fence is altered in one of its two printed copies",
     "paper_battery"),
    ("MUT-DESCRIPTION", "G-FALSIFIER-DESCRIBES-ITS-CODE",
     "a falsifier's published description is inverted while its code is left "
     "alone", "closing_battery"),
    ("MUT-VOUCHING", "G-VOUCHING-KEYS-SEALED",
     "the receipt's own testimony about its arithmetic is rewritten to "
     "something false", "closing_battery"),
    ("MUT-SEALED-AT-PHANTOM", "G-SEAL-TOTALITY",
     "a seal claims provenance from a gate that never ran", "finish"),
    ("MUT-POST-SNAPSHOT-KEY", "G-ARTIFACT-INTEGRITY",
     "a fabricated key is inserted into the receipt after the seal manifest "
     "was totalled", "finish"),
    ("MUT-POST-CLOSE-EDIT", "G-ARTIFACT-INTEGRITY",
     "a sealed value is edited after the manifest was closed and nothing "
     "re-derived it", "finish"),
    ("MUT-TRANSCRIPT-FORGE", "G-ARTIFACT-INTEGRITY",
     "a forged PASS line is appended to the transcript after its gate-time "
     "seal", "finish"),
)
MUTANT_NAMES = tuple(m[0] for m in MUTANTS)
POST_SNAPSHOT_GATES = ("G-TRANSCRIPT-SEALED-AT-THE-SNAPSHOT",
                       "G-RECEIPT-IS-EXACT", "G-SEAL-TOTALITY",
                       "G-ARTIFACT-INTEGRITY")
# The coverage census runs before the paper battery and before the closing
# four, so those gates are DECLARED here and folded into it; a gate that ran
# without appearing in this list or in the ledger would leave the census
# blind, and G-SEAL-TOTALITY checks the declaration against what actually ran.
DECLARED_LATE_GATES = ("G-PAPER-CLAIMS", "G-PAPER-FENCES-MATCH-THE-VERDICT",
                       "G-PAPER-TABLES-WITH-HEADERS",
                       "G-PAPER-NUMERAL-COVERAGE", "G-PAPER-CLAIM-POLARITY",
                       "G-SENTENCE-REFERENT-BINDING",
                       "G-ELEMENT-OF-REALITY-CONFINED",
                       "G-WALLS-SCAN-THE-PAPER",
                       "G-BELL-WALL-STATED-IN-THE-PAPER",
                       "G-ANCHOR-CONSUMERS-RAN",
                       # the five the census used to be blind to: they run at
                       # or after it, and their waivers went unpublished
                       "G-FALSIFIER-COVERAGE", "G-FALSIFIER-REACHABILITY",
                       "G-READS-DECLARED", "G-SWEEP-IS-EXECUTION-BOUND",
                       "G-CLOSING-BATTERY-RAN") + POST_SNAPSHOT_GATES


def hook_carriers():
    """E-23: every falsifier's published description is checked against the
    code that carries it -- the hook is located by AST and the enclosing
    function compared with the registry's declaration."""
    src = open(SELF, "r", encoding="utf-8").read()
    tree = ast.parse(src)
    out = {}
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
            for sub in ast.walk(node):
                if isinstance(sub, ast.Call) and isinstance(
                        sub.func, ast.Name) and sub.func.id in ("mut", "pick"):
                    if sub.args and isinstance(sub.args[0], ast.Constant):
                        out.setdefault(sub.args[0].value, set()).add(node.name)
    return out


def hook_annotations():
    """E-23, THE LEG THAT WAS MISSING (K3 MAJOR-4).  Matching the carrier's
    NAME cannot catch a description-inverted falsifier, because the statement
    string is never consulted.  Here every hook site carries the registry's
    own sentence as an in-source annotation, and the published description
    must be that annotation: invert the description and it no longer quotes
    the code, so the gate fires."""
    src = open(SELF, "r", encoding="utf-8").read()
    tree = ast.parse(src)
    out = {}
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
            seg = ast.get_source_segment(src, node) or ""
            out[node.name] = norm(seg.replace("#", " "))
    return out


VOUCHED_ARITHMETIC = ("exact integers, fractions.Fraction and Z[w] as "
                      "integer pairs; no float anywhere")


def closing_battery(R, paper_text, claims, tables):
    say("SECTION 15c.  THE CLOSING BATTERY")
    # FALSIFIER MUT-VOUCHING: the receipt's own testimony about its
    # arithmetic is rewritten to something false
    if mut("MUT-VOUCHING"):
        R["arithmetic"] = "float64 throughout; numpy used for the census"
    src = open(SELF, "r", encoding="utf-8").read()
    tree = ast.parse(src)
    floats = [n for n in ast.walk(tree)
              if isinstance(n, ast.Constant) and isinstance(n.value, float)]
    fcalls = [n for n in ast.walk(tree) if isinstance(n, ast.Call)
              and isinstance(n.func, ast.Name) and n.func.id == "float"]
    LD.gate("G-NO-FLOAT-IN-SOURCE",
            "THE ARITHMETIC IS EXACT BY CONSTRUCTION AND THE FILE IS SCANNED "
            "TO PROVE IT.  No float literal and no call to float() occurs "
            "anywhere in this instrument",
            not floats and not fcalls,
            "float literals %d, float() calls %d" % (len(floats), len(fcalls)))

    LD.gate("G-VOUCHING-KEYS-SEALED",
            "WHAT THE RECEIPT VOUCHES FOR IS SEALED (#119).  The receipt's "
            "own testimony about its arithmetic and its interpreter used to "
            "sit in the declared-unsealed list, where it could be rewritten "
            "after the fact to say the opposite of what the source scan just "
            "established.  Both are re-derived here against the run and then "
            "sealed like every other key",
            R["arithmetic"] == VOUCHED_ARITHMETIC
            and R["python"] == sys.version.split()[0]
            and not floats and not fcalls,
            "arithmetic vouched %r; python %s; float literals %d, float() "
            "calls %d" % (R["arithmetic"][:48], R["python"], len(floats),
                          len(fcalls)))
    SEAL.take("SEAL-ARITHMETIC", R)
    SEAL.take("SEAL-PYTHON", R)

    carriers = hook_carriers()
    annot = hook_annotations()
    mrows, mbad, dbad = [], [], []
    for name, gate, why, decl in MUTANTS:
        got = sorted(carriers.get(name, []))
        want = decl.split("|")
        ok = all(any(w == g for g in got) for w in want)
        # FALSIFIER MUT-DESCRIPTION: a falsifier's published description is
        # inverted while its code is left alone
        why_used = (why.replace("granted", "REFUSED")
                    if mut("MUT-DESCRIPTION") and name == "MUT-SEPARATION-LEAK"
                    else why)
        needle = norm("FALSIFIER %s: %s" % (name, why_used))
        quoted = any(needle in annot.get(w, "") for w in want)
        mrows.append({"mutant": name, "declared_gate": gate,
                      "statement": why_used,
                      "declared_carrier": decl, "located_in": got,
                      "carrier_matches_code": ok,
                      "description_quotes_the_code": quoted})
        if not ok:
            mbad.append(name)
        if not quoted:
            dbad.append(name)
    LD.gate("G-FALSIFIER-DESCRIBES-ITS-CODE",
            "EVERY FALSIFIER'S PUBLISHED DESCRIPTION IS THE CODE'S OWN "
            "ANNOTATION (E-23).  Locating the hook by carrier NAME never "
            "consults the statement, so a description-inverted falsifier "
            "passed.  Here each hook site carries the registry's sentence "
            "verbatim as an in-source annotation and the published "
            "description must quote it, so inverting what a falsifier claims "
            "to do -- without touching what it does -- fails",
            not dbad, "falsifiers %d, descriptions not quoting their code %s"
            % (len(MUTANTS), dbad or "none"))

    gates_with_falsifiers = {m[1] for m in MUTANTS}
    # THE CENSUS SEES EVERY GATE (K3 MINOR-1).  It used to be built from the
    # ledger plus the declared-late list only, which left the five gates that
    # run at or after it invisible -- and their waivers unpublished.
    ran = sorted({g["gate"] for g in LD.rows} | set(DECLARED_LATE_GATES)
                 | set(POST_SNAPSHOT_GATES))
    uncovered = [g for g in ran if g not in gates_with_falsifiers]
    waivers = {
        "G-WINDOWS-DECLARED-WITH-THEIR-BOUNDS":
            "a declaration gate: its content is the window list itself, "
            "which the seal manifest carries",
        "G-READINGS-PARTITION-MEASURED":
            "forced by MUT-SHADOW-INJECTIVE, which moves every reading's "
            "fibres and is checked to die upstream at G-SHADOW-CEILING",
        "G-NO-FLOAT-IN-SOURCE":
            "a source-scan gate: a float literal anywhere in this file fires "
            "it, which no mutant can simulate without editing the file",
        "G-READS-DECLARED":
            "forced: any read outside the declared set appends to READS and "
            "fires it",
        "G-FALSIFIER-COVERAGE": "this gate",
        "G-FALSIFIER-REACHABILITY": "this gate",
        "G-SWEEP-IS-EXECUTION-BOUND":
            "execution-bound by construction: the sweep rows are the run's "
            "own product and an empty sweep cannot claim to have run",
        "G-TRANSCRIPT-SEALED-AT-THE-SNAPSHOT":
            "forced: the transcript's gate-time digest is compared with the "
            "promoted bytes at G-ARTIFACT-INTEGRITY, which MUT-INTEGRITY and "
            "MUT-TRANSCRIPT-FORGE both exercise",
        "G-RECEIPT-IS-EXACT":
            "a type-scan gate over the published object: any inexact leaf "
            "anywhere fires it, and no mutant can plant one without editing "
            "the file, which the source scan and the digests would show",
        "G-CLOSING-BATTERY-RAN": "this gate",
        "G-BELL-DESIDERATA-BOUND":
            "forced from both sides: MUT-BELL-TABLE moves a rendered cell of "
            "the desiderata table and MUT-BELL-PLANT plants a banned sentence "
            "into the paper, which is where the wall is owed",
    }
    # THE WAIVER LEDGER CARRIES NO DEAD ROWS.  A waiver for a gate that has a
    # falsifier is a green badge over nothing (E-23), so the two lists are
    # required to be exactly complementary.
    dead = [g for g in sorted(waivers) if g not in uncovered]
    unwaived = [g for g in uncovered if g not in waivers]
    R["mutants"] = {"rows": mrows, "count": reg(len(mrows)),
                    "carrier_mismatches": mbad,
                    "description_mismatches": dbad}
    R["coverage"] = {"gates_run": reg(len(ran)),
                     "gates_declared_to_run_after_this_census":
                         reg(len(DECLARED_LATE_GATES)),
                     "gates_with_a_falsifier":
                         reg(len(ran) - len(uncovered)),
                     "distinct_gates_a_falsifier_targets":
                         reg(len(gates_with_falsifiers)),
                     "gates_with_a_waiver": reg(len(uncovered)),
                     "unwaived": unwaived, "dead_waivers": dead,
                     "gates": ran}
    R["waiver_ledger"] = {"rows": [{"gate": g, "forcing": waivers[g]}
                                   for g in uncovered if g in waivers],
                          "count": reg(len([g for g in uncovered
                                            if g in waivers]))}
    LD.gate("G-FALSIFIER-COVERAGE",
            "EVERY GATE CARRIES A FALSIFIER OR A NAMED WAIVER WITH A FORCING, "
            "AND THE CENSUS SEES EVERY GATE (E-23).  %d falsifiers are "
            "declared, each naming the gate it must die at and the function "
            "that carries its hook; every gate that has no falsifier carries "
            "a waiver whose forcing is stated; the gates that run at or after "
            "this census are folded in by declaration rather than left "
            "invisible to it; and a waiver for a gate that HAS a falsifier is "
            "refused, so no dead waiver sits in the ledger"
            % len(MUTANTS),
            not unwaived and not mbad and not dead,
            "gates %d, with falsifiers %d, waived %d, unwaived %s, dead "
            "waivers %s, carrier mismatches %s"
            % (len(ran), len(ran) - len(uncovered), len(uncovered),
               unwaived or "none", dead or "none", mbad or "none"))
    SEAL.take("SEAL-MUTANTS", R)
    SEAL.take("SEAL-COVERAGE", R)
    SEAL.take("SEAL-WAIVERS", R)

    reach = [{"mutant": m[0], "declared_gate": m[1],
              "hook_located": bool(carriers.get(m[0]))} for m in MUTANTS]
    R["reachability"] = {"rows": reach, "count": reg(len(reach)),
                         "not_located": [r["mutant"] for r in reach
                                         if not r["hook_located"]]}
    LD.gate("G-FALSIFIER-REACHABILITY",
            "EVERY DECLARED FALSIFIER REACHES ITS GATE (#34).  Each hook is "
            "located in this file by AST rather than trusted from its "
            "description, and the sweep executes every one of them and "
            "records where it actually died",
            not R["reachability"]["not_located"],
            "falsifiers %d, hooks not located %s"
            % (len(reach), R["reachability"]["not_located"] or "none"))
    SEAL.take("SEAL-REACHABILITY", R)

    declared = {os.path.abspath(os.path.join(REPO, s[0])) for s in SOURCES}
    declared_paper = os.path.abspath(os.path.join(REPO, PAPER_REL))
    got_src = READS_BY_CATEGORY.get("SOURCE", set())
    got_pap = READS_BY_CATEGORY.get("PAPER-UNDER-TEST", set())
    extra = sorted((got_src - declared) | (got_pap - {declared_paper}))
    R["read_set"] = {
        "sources": sorted(os.path.relpath(p, REPO) for p in got_src),
        "paper_under_test": sorted(os.path.relpath(p, REPO) for p in got_pap),
        "undeclared_reads": extra, "total_reads": reg(len(READS)),
        "subprocesses": 0,
        "note": "the read set is recorded at the actual I/O layer, so an "
                "abstention is provable rather than promised"}
    LD.gate("G-READS-DECLARED",
            "THE READ SET IS THE DECLARED ONE, RECORDED AT THE I/O LAYER "
            "(#91).  Six sources and one object under test, the paper's own "
            "read taken inside the run so that no leg is exempt; a read of any "
            "other repository file appears here and fires this gate; no "
            "subprocess is invoked, so the run is correct off-tree and with "
            "no version control present",
            not extra, "reads %d, undeclared %s"
            % (len(READS), extra or "none"))
    SEAL.take("SEAL-READSET", R)
    return paper_battery(R, paper_text, claims, tables)


def exactness_scan(obj, path="", bad=None):
    bad = [] if bad is None else bad
    if isinstance(obj, dict):
        for k, v in obj.items():
            exactness_scan(v, path + "/" + str(k), bad)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            exactness_scan(v, path + "/" + str(i), bad)
    elif not isinstance(obj, (str, int, bool, type(None))):
        bad.append(path + " :: " + type(obj).__name__)
    return bad


def full_run(paper_text="", write=False):
    global ROWCACHE
    R = {}
    ppath = os.path.join(REPO, PAPER_REL)
    if os.path.exists(ppath):
        # the object under test is read HERE, inside the run, so that the
        # read set the gate checks is the run's own I/O and the paper leg is
        # not exempt from it
        paper_text = read_text(PAPER_REL, "PAPER-UNDER-TEST")
    texts = provenance(R, paper_text)
    fac = FAC_CITED
    windows_declare(R)
    arena_measure(R)
    corp, nf, rows = corpus_measure(R, fac)
    ROWCACHE = rows
    adm = blocks_measure(R, corp, fac)
    freeze_predicates(R)
    tot = R["predicates"]["totality_failures"]
    separation_measure(R, corp, adm)
    uniq, classes, rfib, conj, ref = descriptions_measure(R, rows)
    arms, FR, FS = certainty_measure(R, corp, adm, uniq, classes, tot)
    red = reductions_measure(R, corp, adm, uniq, rfib, arms)
    conjugacy_measure(R, corp, uniq, rfib, conj, ref)
    walk = [a for a in arms if a["localization"] == "LOC-WALK"
            and a["separation"] == "SEP-LINK-DISJOINT"][0]
    e5 = e5_measure(R, corp, adm, uniq, rfib, red)
    bell_measure(R, arms, walk)
    ctrl = controls_measure(R, corp, adm, uniq, FR, FS, arms)
    redwalk = [x for x in red if x["localization"] == "LOC-WALK"
               and x["separation"] == "SEP-LINK-DISJOINT"][0]
    verdict_measure(R, corp, adm, uniq, arms, tot, redwalk, e5)
    class_binding_measure(R, arms, ctrl, conj)
    claims, tables = paper_render(R)
    R["arithmetic"] = VOUCHED_ARITHMETIC
    R["python"] = sys.version.split()[0]
    return R, claims, tables, paper_text


def finish(R, write=True, swept=False):
    # THE ANCHOR-CONSUMER CENSUS runs here, where every gate that names an
    # anchor has already run and recorded its consumption.
    ran_gates = {g["gate"] for g in LD.rows}
    crows, cbad = [], []
    for row in R["verbatim_anchors"]["rows"]:
        gate = row["consumed_by"]
        ran_it = gate in ran_gates
        took_it = row["anchor"] in CONSUMED.get(gate, set())
        crows.append({"anchor": row["anchor"], "consumed_by": gate,
                      "the_gate_ran": ran_it, "the_gate_consumed_it": took_it})
        if not (ran_it and took_it):
            cbad.append(row["anchor"])
    R["anchor_consumers"] = {
        "rows": crows, "count": reg(len(crows)), "unconsumed": cbad,
        "note": "an anchor's consumer is not decoration: the named gate must "
                "be a gate this run ran, and it must have called consume() on "
                "that anchor as part of its own condition, so a consumed_by "
                "field pointing anywhere at all fails here"}
    LD.gate("G-ANCHOR-CONSUMERS-RAN",
            "EVERY ANCHOR IS CONSUMED BY THE GATE IT NAMES (K3 MINOR-10).  "
            "The consumed_by field was written once and never read again; "
            "here each anchor's named gate must be one this run actually ran "
            "AND must have consumed that anchor inside its own condition, so "
            "re-pointing an anchor at an unrelated or non-existent gate fails",
            not cbad, "anchors %d, unconsumed or mis-pointed %s"
            % (len(crows), cbad or "none"))
    SEAL.take("SEAL-CONSUMERS", R)
    R["mutant_sweep"] = {
        "rows": SWEEP_ROWS, "executed": reg(len(SWEEP_ROWS)),
        "declared": reg(len(MUTANTS)), "swept": bool(swept),
        "off_target": [r["mutant"] for r in SWEEP_ROWS
                       if not r["died_at_the_declared_gate"]]}
    LD.gate("G-SWEEP-IS-EXECUTION-BOUND",
            "THE SWEEP FLAG IS BOUND TO EXECUTION.  A run may claim a sweep "
            "only when the sweep rows are its own product: the flag and the "
            "row count are compared here, so 'swept' with no sweep dies",
            bool(swept) == (len(SWEEP_ROWS) > 0)
            and not R["mutant_sweep"]["off_target"],
            "swept %s, rows %d, off target %s"
            % (swept, len(SWEEP_ROWS), R["mutant_sweep"]["off_target"]
               or "none"))
    SEAL.take("SEAL-MUTANT-SWEEP", R)
    LD.gate("G-CLOSING-BATTERY-RAN",
            "THE PAPER INSTRUMENT AND THE CLOSING BATTERY RAN IN THE PLAIN "
            "RUN (#20).  Every gate of this unit is in one ledger, and the "
            "ledger, the seal manifest and the transcript are sealed into "
            "the same receipt",
            len(LD.rows) > 20 and len(SEAL.rows) > 20,
            "gates %d, seals %d" % (len(LD.rows), len(SEAL.rows)))
    R["gates"] = list(LD.rows)
    R["closing_gates"] = {
        "in_the_sealed_ledger": [g["gate"] for g in R["gates"]],
        "declared_to_run_after_the_snapshot": list(POST_SNAPSHOT_GATES)}
    R["totals"] = {"gates_in_the_sealed_ledger": reg(len(R["gates"])),
                   "gates_after_the_snapshot": reg(len(POST_SNAPSHOT_GATES)),
                   "seals_at_the_snapshot": reg(len(SEAL.rows)),
                   "falsifiers": reg(len(MUTANTS)),
                   "sources": reg(len(SOURCES)),
                   "anchors": reg(len(ANCHORS)),
                   "windows": reg(len(WINDOWS))}
    SEAL.take("SEAL-GATES", R)
    SEAL.take("SEAL-CLOSING", R)
    SEAL.take("SEAL-TOTALS", R)
    text = "\n".join(LINES) + "\n"
    R["transcript_head"] = {"lines_at_the_seal": reg(len(LINES)),
                            "sha256_12": digest(text),
                            "note": "the ledger is snapshotted here; the "
                                    "gates that follow are declared in "
                                    "closing_gates and verified to be "
                                    "exactly those, and the whole "
                                    "transcript's own digest is compared "
                                    "with the staged bytes at "
                                    "G-ARTIFACT-INTEGRITY"}
    LD.gate("G-TRANSCRIPT-SEALED-AT-THE-SNAPSHOT",
            "THE TRANSCRIPT IS SEALED (#119).  Its digest is taken over "
            "every line the run has emitted at the snapshot and carried in "
            "the receipt; the gates that run after it are declared by name "
            "and checked to be exactly those, and the completed "
            "transcript's bytes are read back and compared at promotion",
            len(LINES) > 50, "transcript lines at the seal %d" % len(LINES))
    SEAL.take("SEAL-TRANSCRIPT", R)

    bad = exactness_scan(R)
    LD.gate("G-RECEIPT-IS-EXACT",
            "THE RECEIPT IS SCANNED RECURSIVELY FOR INEXACT TYPES.  Every "
            "leaf of the published object must be a string, an integer, a "
            "boolean or null",
            not bad, "inexact leaves %s" % (bad or "none"))
    missing, extra = SEAL.totality()
    published = sorted(k for k in R if k not in DECLARED_UNSEALED)
    sealed_paths = {r["path"] for r in SEAL.rows}
    unsealed = sorted(k for k in published if k not in sealed_paths)
    after = [g["gate"] for g in LD.rows[len(R["gates"]):]]
    late = [g for g in after if g not in POST_SNAPSHOT_GATES]
    # THE UNSEALED LIST IS PINNED, NOT CONSULTED (K3 MAJOR-5b).  Growing it
    # by a name used to publish a forged key under it; here the list itself
    # is compared with the literal two structural keys.
    unsealed_list_is_the_declared_two = (
        set(DECLARED_UNSEALED) == {"seal_manifest", "payload_sha256_12"})
    # EVERY SEAL'S PROVENANCE IS A GATE THAT RAN (K3 MAJOR-5c).  The shipped
    # manifest named G-TRANSCRIPT-SEALED-WHOLE, a gate that never existed.
    ledger_gates = {g["gate"] for g in LD.rows} | {"G-SEAL-TOTALITY"}
    # FALSIFIER MUT-SEALED-AT-PHANTOM: a seal claims provenance from a gate
    # that never ran
    if mut("MUT-SEALED-AT-PHANTOM"):
        SEAL.rows[0]["sealed_at_gate"] = "G-A-GATE-THAT-NEVER-RAN"
    phantom = sorted({r["seal"] for r in SEAL.rows
                      if r["sealed_at_gate"] not in ledger_gates})
    LD.gate("G-SEAL-TOTALITY",
            "THE SEAL MANIFEST IS TOTAL, AND ITS PROVENANCE IS REAL (#119).  "
            "Every published receipt key is either sealed at the gate that "
            "established it or is one of the two structural keys the "
            "declared-unsealed list is required to be, compared literally so "
            "that growing the list publishes nothing; every seal's named gate "
            "must be a gate this run actually ran, so a seal cannot claim "
            "provenance from a phantom; and every gate that ran after the "
            "ledger snapshot is one this unit declared would",
            not missing and not extra and not unsealed and not late
            and unsealed_list_is_the_declared_two and not phantom,
            "seals %d, published keys %d, missing %s, extra %s, unsealed %s, "
            "undeclared late gates %s, unsealed list pinned %s, seals naming "
            "a gate that never ran %s"
            % (len(SEAL.rows), len(published), missing or "none",
               extra or "none", unsealed or "none", late or "none",
               unsealed_list_is_the_declared_two, phantom or "none"))
    keys_at_totality = sorted(R)
    R["seal_manifest"] = SEAL.rows
    payload = json.dumps(R, indent=1, sort_keys=True, default=str)
    SEAL.close(R, payload)
    R["payload_sha256_12"] = SEAL.payload_sha
    # FALSIFIER MUT-POST-SNAPSHOT-KEY: a fabricated key is inserted into the
    # receipt after the seal manifest was totalled
    if mut("MUT-POST-SNAPSHOT-KEY"):
        R["headline_summary"] = {"verdict": "EPR-BOTH-COMPLETE",
                                 "certified": "316,224"}
    # FALSIFIER MUT-POST-CLOSE-EDIT: a sealed value is edited after the
    # manifest was closed and nothing re-derived it
    if mut("MUT-POST-CLOSE-EDIT"):
        R["verdict"]["head"] = "EPR-BOTH-COMPLETE"
    # THE SEALS ARE RE-DERIVED AT PROMOTION, NOT ONLY AT CLOSE.  SEAL.close
    # verifies every sealed path against its gate-time digest, but the payload
    # that is actually promoted is serialised AFTER it, so a sealed VALUE
    # edited in between was published against a seal nothing re-checked --
    # the third form of the ACT disease, beside the key ADD and the unsealed
    # list.  Here the whole manifest is re-derived over the object as it
    # stands at promotion.
    post_close_broken = SEAL.verify(R)
    payload = json.dumps(R, indent=1, sort_keys=True, default=str)
    # PROMOTION-TIME TOTALITY (#119 as amended).  G-SEAL-TOTALITY runs before
    # the payload is built, and nothing re-checked the object afterwards: a
    # key inserted in between was published unsealed, unlisted and
    # undetected.  The key set is recomputed HERE, at promotion, against the
    # set the manifest was totalled over plus exactly the two keys this
    # function is allowed to add.
    keys_now = sorted(R)
    keys_want = sorted(set(keys_at_totality)
                       | {"seal_manifest", "payload_sha256_12"})
    keys_added_after_the_snapshot = sorted(set(keys_now) - set(keys_want))
    keys_lost_after_the_snapshot = sorted(set(keys_want) - set(keys_now))
    # FALSIFIER MUT-TRANSCRIPT-FORGE: a forged PASS line is appended to the
    # transcript after its gate-time seal
    if mut("MUT-TRANSCRIPT-FORGE"):
        LINES.append("  [PASS] G-LOCAL-REALISM-RESTORED")
    text = "\n".join(LINES) + "\n"
    seal_j = hashlib.sha256(payload.encode("utf-8")).hexdigest()[:12]
    seal_t = hashlib.sha256(text.encode("utf-8")).hexdigest()[:12]
    # THE TRANSCRIPT IS CONTENT-SEALED, NOT ROUND-TRIPPED (K3 MAJOR-6).  Two
    # comparisons the old gate did not make: the promoted transcript's PREFIX
    # against the digest sealed at gate time, and every [PASS]/[FAIL] line it
    # carries against the ledger's own rows, as a multiset.  A hash of the
    # live lines taken at promotion can only prove the file write
    # round-tripped.
    head_lines = R["transcript_head"]["lines_at_the_seal"]
    prefix = "\n".join(LINES[:head_lines]) + "\n"
    prefix_sha = hashlib.sha256(prefix.encode("utf-8")).hexdigest()[:12]
    prefix_ok = prefix_sha == R["transcript_head"]["sha256_12"]
    printed = Counter()
    for line in LINES:
        m = re.match(r"\s*\[(PASS|FAIL)\] (G-[A-Z0-9-]+)$", line)
        if m:
            printed[(m.group(2), m.group(1) == "PASS")] += 1
    ledgered = Counter((g["gate"], g["passed"]) for g in LD.rows)
    line_diff = sorted("%s:%s" % (k[0], k[1]) for k in
                       list((printed - ledgered).elements())
                       + list((ledgered - printed).elements()))
    # FALSIFIER MUT-INTEGRITY: the staged bytes are corrupted after sealing
    staged_j = payload + (" " if mut("MUT-INTEGRITY") else "")
    tmp_j, tmp_t = OUT_JSON + ".tmp", OUT_TXT + ".tmp"
    if write:
        with open(tmp_j, "w", encoding="utf-8") as fh:
            fh.write(staged_j)
        with open(tmp_t, "w", encoding="utf-8") as fh:
            fh.write(text)
        with open(tmp_j, "rb") as fh:
            raw_j = fh.read()
        with open(tmp_t, "rb") as fh:
            raw_t = fh.read()
    else:
        raw_j = staged_j.encode("utf-8")
        raw_t = text.encode("utf-8")
    dj = hashlib.sha256(raw_j).hexdigest()[:12]
    dt = hashlib.sha256(raw_t).hexdigest()[:12]
    flipped = bytes([raw_t[0] ^ 1]) + raw_t[1:]
    control_rejects = (hashlib.sha256(flipped).hexdigest()[:12] != seal_t)
    ranset = {g["gate"] for g in LD.rows} | {"G-ARTIFACT-INTEGRITY"}
    late_missing = [g for g in DECLARED_LATE_GATES if g not in ranset]
    ok = (dj == seal_j and dt == seal_t and control_rejects
          and not keys_added_after_the_snapshot
          and not keys_lost_after_the_snapshot and not post_close_broken
          and prefix_ok and not line_diff and not late_missing)
    if write:
        if ok:
            os.replace(tmp_j, OUT_JSON)
            os.replace(tmp_t, OUT_TXT)
        else:
            for p in (tmp_j, tmp_t):
                if os.path.exists(p):
                    os.remove(p)
    # AFTER os.replace, NOT ONLY BEFORE (K3 MINOR-8).  The comparison used to
    # end at the staging read-back, leaving a window between it and the
    # promotion; the promoted paths are re-read here and compared again.
    promoted = {}
    if write and ok:
        for p, want in ((OUT_JSON, seal_j), (OUT_TXT, seal_t)):
            with open(p, "rb") as fh:
                promoted[p] = hashlib.sha256(fh.read()).hexdigest()[:12]
        ok = all(promoted[p] == w for p, w in ((OUT_JSON, seal_j),
                                               (OUT_TXT, seal_t)))
    LD.gate("G-ARTIFACT-INTEGRITY",
            "THE BYTES ARE READ BACK BEFORE THEY ARE PROMOTED, AND AGAIN "
            "AFTER (#119).  Both artifacts are written to staging, the "
            "STAGED bytes are read back from disk and compared with the "
            "digests of the objects sealed at gate time, and only then does "
            "os.replace promote them; the promoted paths are then re-read and "
            "compared once more, so the window between the read-back and the "
            "promotion is closed.  On refusal the staging files are removed "
            "and nothing is promoted; on a dry run the same comparison is "
            "taken over the same buffered bytes, so the gate is reachable "
            "there too, and it is exercised in the failing direction on the "
            "same bytes with one bit flipped.  FOUR further comparisons ride "
            "here because they can only be made at promotion: the receipt's "
            "key set against the set the seal manifest was totalled over, so "
            "a key inserted after the totality gate is caught; every sealed "
            "value re-derived against its gate-time digest over the object as "
            "it stands at promotion, so a sealed value edited after the "
            "manifest closed is caught too; the promoted "
            "transcript's PREFIX against the digest sealed at gate time; and "
            "every [PASS]/[FAIL] line the transcript carries against the "
            "ledger's own rows, as a multiset, so a forged PASS line is not a "
            "line the ledger never wrote",
            ok, "receipt staged %s seal %s; transcript staged %s seal %s; "
            "one-bit-flip control rejects %s; keys added after the snapshot "
            "%s, lost %s; seals broken after the close %s; transcript prefix "
            "%s vs sealed %s; transcript "
            "PASS/FAIL lines vs the ledger %s; declared-late gates that never "
            "ran %s; promoted %s, re-read %s"
            % (dj, seal_j, dt, seal_t, control_rejects,
               keys_added_after_the_snapshot or "none",
               keys_lost_after_the_snapshot or "none",
               post_close_broken or "none", prefix_sha,
               R["transcript_head"]["sha256_12"], line_diff or "agree",
               late_missing or "none", bool(write and ok),
               promoted or "not promoted"))
    if write:
        print()
        print("receipt    %s  %s" % (OUT_JSON, dj))
        print("transcript %s  %s" % (OUT_TXT, dt))
    return R, payload, text, seal_j, seal_t


# --------------------------------------------------------------------------
# THE CLI CONTRACT (#82), THE SELFTEST AND THE SWEEP
# --------------------------------------------------------------------------

def reset_state():
    global LD, SEAL
    del LINES[:]
    del READS[:]
    READS_BY_CATEGORY.clear()
    NUMREG.clear()
    _MENU_CACHE.clear()
    LD = Ledger()
    SEAL = Seal()


def artifact_state():
    out = {}
    for p in (OUT_JSON, OUT_TXT):
        out[p] = (hashlib.sha256(open(p, "rb").read()).hexdigest()[:12]
                  if os.path.exists(p) else None)
    return out


def run_mutant(name, paper_text):
    global MUT
    before = artifact_state()
    reset_state()
    MUT = name
    died = None
    try:
        R, claims, tables, ptxt = full_run(paper_text)
        closing_battery(R, ptxt, claims, tables)
        finish(R, write=False)
    except GateFail as exc:
        died = str(exc).split(" :: ")[0]
    except Exception as exc:                       # noqa: BLE001
        died = "UNCAUGHT:" + type(exc).__name__
    finally:
        MUT = None
    after = artifact_state()
    declared = [m[1] for m in MUTANTS if m[0] == name][0]
    return {"mutant": name, "declared_gate": declared, "died_at": died,
            "died_at_the_declared_gate": died == declared,
            "artifacts_unchanged": before == after}


def sweep(paper_text):
    rows = []
    for name, _g, _w, _c in MUTANTS:
        rows.append(run_mutant(name, paper_text))
    return rows


def selftest():
    """#82: a REAL selftest -- one anchor is corrupted, the run is confirmed
    to die at the gate that consumes it, and NOTHING is written."""
    global MUT
    before = artifact_state()
    ppath = os.path.join(REPO, PAPER_REL)
    ptext = (read_text(PAPER_REL, "PAPER-UNDER-TEST")
             if os.path.exists(ppath) else "")
    reset_state()
    MUT = "MUT-ANCHOR-E2"
    died = None
    try:
        R, claims, tables, ptxt = full_run(ptext)
        closing_battery(R, ptxt, claims, tables)
        finish(R, write=False)
    except GateFail as exc:
        died = str(exc).split(" :: ")[0]
    finally:
        MUT = None
    after = artifact_state()
    ok = (died == "G-VERBATIM-ANCHORS-IN-SOURCE" and before == after)
    print("[selftest] corrupted anchor A-E2 -> died at %s; artifacts %s"
          % (died, "unchanged" if before == after else "CHANGED"))
    return 0 if ok else 1


def parse_args(argv):
    """THE ARGV WHITELIST.  Unknown flags exit 2; nothing is silently
    ignored."""
    opts = {"sweep": False, "selftest": False, "mutant": None,
            "quiet": False, "list": False}
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == "--sweep":
            opts["sweep"] = True
        elif a == "--selftest":
            opts["selftest"] = True
        elif a == "--quiet":
            opts["quiet"] = True
        elif a == "--list-gates":
            opts["list"] = True
        elif a == "--mutant":
            if i + 1 >= len(argv):
                raise CliError("--mutant needs a NAME")
            opts["mutant"] = argv[i + 1]
            i += 1
        elif a.startswith("--mutant="):
            opts["mutant"] = a.split("=", 1)[1]
        else:
            raise CliError("unknown argument %r" % a)
        i += 1
    if opts["mutant"] is not None and opts["mutant"] not in MUTANT_NAMES:
        raise CliError("unknown falsifier %r" % opts["mutant"])
    return opts


def main(argv=None):
    global QUIET, MUT
    argv = sys.argv[1:] if argv is None else argv
    try:
        opts = parse_args(argv)
    except CliError as exc:
        print("[cli] %s" % exc, file=sys.stderr)
        print("[cli] usage: epr_exact.py [--sweep] [--selftest] "
              "[--mutant NAME] [--list-gates] [--quiet]", file=sys.stderr)
        return 2
    if opts["list"]:
        for name, gate, why, carrier in MUTANTS:
            print("%-26s %-42s %s" % (name, gate, why))
        return 0
    if opts["selftest"]:
        return selftest()
    QUIET = opts["quiet"]
    ppath = os.path.join(REPO, PAPER_REL)
    paper_text = (read_text(PAPER_REL, "PAPER-UNDER-TEST")
                  if os.path.exists(ppath) else "")
    if opts["mutant"]:
        row = run_mutant(opts["mutant"], paper_text)
        print("[falsifier] %s -> died at %s (declared %s, on target %s); "
              "artifacts %s"
              % (row["mutant"], row["died_at"], row["declared_gate"],
                 row["died_at_the_declared_gate"],
                 "unchanged" if row["artifacts_unchanged"] else "CHANGED"))
        return 0 if row["died_at_the_declared_gate"] else 1
    swept = []
    if opts["sweep"]:
        swept = sweep(paper_text)
        bad = [r for r in swept if not r["died_at_the_declared_gate"]
               or not r["artifacts_unchanged"]]
        print("[sweep] %d falsifiers, %d off target" % (len(swept), len(bad)))
        for r in swept:
            print("        %-26s -> %s" % (r["mutant"], r["died_at"]))
        if bad:
            print("[sweep] OFF TARGET: %s" % [r["mutant"] for r in bad],
                  file=sys.stderr)
            return 1
    reset_state()
    MUT = None
    try:
        R, claims, tables, ptxt = full_run(paper_text, write=True)
        closing_battery(R, ptxt, claims, tables)
        SWEEP_ROWS.extend(swept)
        finish(R, write=True, swept=bool(swept))
    except GateFail as exc:
        print("[FAIL] %s" % exc, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())








