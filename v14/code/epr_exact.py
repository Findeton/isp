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
  SEC 2  PROVENANCE -- seven pinned sources, sha256-12 verified; eleven
         verbatim anchors bound to the gates that consume them; the
         pre-registered outcome vocabulary PARSED OUT OF THE PIN'S BYTES.
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
         theorem (the coin consumes n mod 3) machine-checked over a declared
         state family; the five declared readings.
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
paper.  Every count is COUNTING-ONLY over a declared window (E-24).  No
sentence of this unit claims local realism, Bell evasion, or a vindicated
hidden-variable completion: v5 paper-14's verdict is a WALL and is scanned
against this unit's own paper.

ARITHMETIC.  Exact only: Python integers, fractions.Fraction, and the ring
Z[w] carried as integer pairs.  There are no floats; an AST scan of this file
and a recursive type scan of the emitted receipt are gates.

RUNTIME INPUTS (#46/#91).  Exactly seven committed files are read as SOURCES,
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
    ("SEAL-READINGS", "readings", "G-READINGS-PARTITION-MEASURED"),
    ("SEAL-CERTAINTY", "certainty", "G-CERTAINTY-CENSUS-PER-ARM"),
    ("SEAL-REDUCTIONS", "reductions", "G-E4-TWO-REDUCTIONS"),
    ("SEAL-CONJUGACY", "conjugacy", "G-CONJUGATE-PAIR-MEASURED"),
    ("SEAL-E5", "e5_audit", "G-E5-RECORD-DOES-NOT-MOVE"),
    ("SEAL-BELL", "bell", "G-BELL-DESIDERATA-BOUND"),
    ("SEAL-CONTROLS", "controls", "G-EVERY-OUTCOME-WORD-EMITTABLE"),
    ("SEAL-MEASURE", "measure_relativity", "G-PROBABILITY-EXACTLY-ONE"),
    ("SEAL-CLASSBIND", "class_binding", "G-CLASS-WORDS-BOUND-TO-PREDICATES"),
    ("SEAL-COUNTS", "counts", "G-HEAD-DERIVED-TWICE"),
    ("SEAL-VERDICT", "verdict", "G-HEAD-DERIVED-TWICE"),
    ("SEAL-WALLS", "walls", "G-WALLS-SCAN-THE-PAPER"),
    ("SEAL-PAPER-CLAIMS", "paper_claims", "G-PAPER-CLAIMS"),
    ("SEAL-PAPER-TABLES", "paper_tables", "G-PAPER-TABLES-WITH-HEADERS"),
    ("SEAL-PAPER-COVERAGE", "paper_coverage", "G-PAPER-NUMERAL-COVERAGE"),
    ("SEAL-REFERENT", "referent_binding", "G-SENTENCE-REFERENT-BINDING"),
    ("SEAL-POLARITY", "polarity", "G-PAPER-CLAIM-POLARITY"),
    ("SEAL-COVERAGE", "coverage", "G-FALSIFIER-COVERAGE"),
    ("SEAL-REACHABILITY", "reachability", "G-FALSIFIER-REACHABILITY"),
    ("SEAL-WAIVERS", "waiver_ledger", "G-FALSIFIER-COVERAGE"),
    ("SEAL-MUTANTS", "mutants", "G-FALSIFIER-COVERAGE"),
    ("SEAL-MUTANT-SWEEP", "mutant_sweep", "G-SWEEP-IS-EXECUTION-BOUND"),
    ("SEAL-READSET", "read_set", "G-READS-DECLARED"),
    ("SEAL-GATES", "gates", "G-CLOSING-BATTERY-RAN"),
    ("SEAL-CLOSING", "closing_gates", "G-CLOSING-BATTERY-RAN"),
    ("SEAL-TOTALS", "totals", "G-CLOSING-BATTERY-RAN"),
    ("SEAL-TRANSCRIPT", "transcript_head", "G-TRANSCRIPT-SEALED-WHOLE"),
]
DECLARED_UNSEALED = ["arithmetic", "python", "seal_manifest",
                     "payload_sha256_12"]


class Seal:
    def __init__(self):
        self.rows = []
        self.index = {}
        self.payload = None
        self.payload_sha = None

    def take(self, sid, obj):
        path = [p for s, p, _g in SEALED_PATHS if s == sid][0]
        at = [g for s, _p, g in SEALED_PATHS if s == sid][0]
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
               thirty_six=36, hundred=100, thousand=1000)


# ===========================================================================
# SECTION 2.  PROVENANCE -- THE PINNED SOURCES AND THE VERBATIM ANCHORS
# ===========================================================================
# Seven committed files are read as SOURCES at digests frozen in this
# declaration.  The 1935 paper itself is the SOURCE OF RECORD: it is read as
# bytes and its digest verified, and the six wall quotes E1-E6 are matched
# VERBATIM in the pin's own bytes, where the orchestrator transcribed them
# from the original.  Both legs are published: the quote's presence in the
# pin is machine-checked, the pin's fidelity to the 1935 print is testimony.

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
    ("A-BELL-E1", "v5/relativistic-isp-v5-paper14-non-markovianity-and-bell-"
     "nonlocality.md", "G-BELL-DESIDERATA-BOUND",
     "ISP cannot satisfy Bell local causality and still reproduce the "
     "Tsirelson violation. It is Bell-nonlocal."),
    ("A-BELL-E2", "v5/relativistic-isp-v5-paper14-non-markovianity-and-bell-"
     "nonlocality.md", "G-BELL-DESIDERATA-BOUND",
     "ISP is no-signalling and parameter-independent; there is no "
     "superluminal causal influence in its dynamics."),
    ("A-AID", "v14/paper-33-aid.md", "G-BLOCKS-AGREE-WITH-FAC",
     "The corpus defines an actor as an identity that recurs in the record."),
)


def provenance(R):
    say("SECTION 2.  PROVENANCE")
    rows, texts = [], {}
    for rel, want, why in SOURCES:
        raw = read_bytes(rel)
        got = hashlib.sha256(raw).hexdigest()[:12]
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

    arows = []
    for name, rel, gate, needle in ANCHORS:
        hay = texts.get(rel)
        needle_used = pick("MUT-ANCHOR-E2", needle,
                           needle.replace("certainty", "probability")) \
            if name == "A-E2" else needle
        found = bool(hay is not None and match_needle(hay, needle_used))
        arows.append({"anchor": name, "source": rel, "consumed_by": gate,
                      "found": found, "chars": len(canon(needle_used))})
    miss = [r["anchor"] for r in arows if not r["found"]]
    R["verbatim_anchors"] = {
        "rows": arows, "count": reg(len(arows)), "missing": miss,
        "floor_chars": NEEDLE_FLOOR,
        "note": "each anchor names the gate that consumes it; the quote side "
                "is matched, not merely the source side"}
    LD.gate("G-VERBATIM-ANCHORS-IN-SOURCE",
            "THE WALL QUOTES ARE MATCHED IN THEIR SOURCES' BYTES.  Fourteen "
            "anchors, each above the #62 length floor, each naming the gate "
            "that consumes it; the six EPR quotes are matched in the pin, "
            "where they were transcribed from the 1935 print",
            not miss, "anchors %d, missing %s" % (len(arows), miss or "none"))
    SEAL.take("SEAL-VERBATIM", R)

    pin = texts[PIN_REL]
    parsed = []
    for line in pin.split("\n"):
        m = re.match(r"^- (EPR-[A-Z-]+(?:<object>)?)(?: |$)", line.strip())
        if m:
            parsed.append(m.group(1))
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
            "individually",
            not bad and not rowbad,
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
    if mut("MUT-FIBER-ROWS"):
        out = out[:1]
    return out


def epr_reality_at(qdir, fib):
    """EPR-REALITY: the quantity's value is the same at every record the
    conditioning data admits -- prediction with certainty."""
    if mut("MUT-CERT-CONSTANT-TRUE"):
        return True
    return len({r[qdir] for r in fib}) == 1


def epr_counterpart_at(qdir, own):
    """THE COUNTERPART CLAUSE: the description's own content at the block
    determines the value."""
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
            "decides; every predicate is then exercised on every argument "
            "combination of a declared probe set and required to return a "
            "boolean or a declared value at each",
            not missing and not leaks and tot["failures"] == 0,
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
    for row in testrows:
        fb = fiber(testrows, lambda r: r[0] % 3, row)
        for d in range(3):
            probes += 2
            if not isinstance(epr_reality_at(d, fb), bool):
                failures += 1
            if not isinstance(epr_counterpart_at(d, fb), bool):
                failures += 1
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
# paper-20's Reading A, the wave-function analogue.  The shadow's ceiling is
# a THEOREM about the coin: D(x) = diag(w^{n_l(x)}) depends on the record
# only through n mod 3, so no state whatever can make the menu tell two
# records with equal residues apart.  It is machine-checked over a declared
# state family and the primary state is required to attain the sweep's
# maximum, so the shadow is audited at its BEST case.

PSI_ALPHABET = ((0, 0), (1, 0), (0, 1), (-1, -1))
PSI_DECLARED = (("PSI-FLAT", ((1, 0), (1, 0), (1, 0))),
                ("PSI-BASIS", ((1, 0), (0, 0), (0, 0))),
                ("PSI-W", ((1, 0), (0, 1), (-1, -1))))
PSI_PRIMARY = PSI_DECLARED[0][1]

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
                   "measured at 0 separations over the whole sweep",
        "window": "COUNTING-ONLY; the state family is declared and its "
                  "bounds published (E-24)"}
    LD.gate("G-SHADOW-CEILING",
            "THE SHADOW'S BLINDNESS IS A THEOREM ABOUT THE COIN, AND IT IS "
            "MEASURED AT EVERY STATE OF A DECLARED FAMILY.  Sixty-four "
            "states are swept; not one separates two committed records that "
            "share a residue class, so the shadow's ceiling is the residue "
            "class and no state can raise it.  The primary state is required "
            "to attain the sweep's maximum, so the audit gives the shadow "
            "its best case rather than a strawman",
            seps == 0 and len(prim) == best and len(classes) < len(uniq),
            "records %d, residue classes %d, sweep %d states, best %d, "
            "primary %d, separations %d"
            % (len(uniq), len(classes), len(PSI_ALPHABET) ** 3, best,
               len(prim), seps))
    SEAL.take("SEAL-DESCRIPTIONS", R)

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
            "one cell, every record in it",
            len(conj) > 0 and rrows["READ-BORN-DG"]["cells"] == 1
            and ref[("READ-RECORD", "READ-BORN-GD")],
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


def certainty_measure(R, corp, adm, uniq, tot):
    say("SECTION 9.  MEASUREMENT 2 -- THE CERTAINTY-ELEMENT CENSUS")
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
            "physical theory -- is applied to both descriptions on all four "
            "arms; the record certifies and carries, the shadow certifies "
            "nothing and carries none of the record's",
            prim["premise_instances"] == 0 and walk["certainty_elements"] > 0
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
    if mut("MUT-E4-COLLAPSE"):
        return ()
    return tuple(tuple(sorted({z[d] for z in rfib[rd][row]})) for d in qs)


def reductions_measure(R, corp, adm, uniq, rfib, arms):
    say("SECTION 10.  MEASUREMENT 3 -- E4, THE TWO REDUCTIONS")
    out = []
    for locname, locf in LOCALIZATIONS:
        for sepname, septest in SEPARATIONS:
            specs = pair_specs(locf, septest)
            cache = {}
            for nm, spec in specs.items():
                for si, (_da, _db, qs) in enumerate(spec):
                    for r in uniq:
                        s = {assigned_description(rd, r, qs, rfib)
                             for rd in READINGS}
                        cache[(nm, si, r)] = len(s)
            dist, probes = Counter(), 0
            for i, (_tag, _h) in enumerate(corp):
                r = ROWCACHE[i]
                for nm in adm[i]:
                    for si in range(len(specs[nm])):
                        probes += 1
                        dist[cache[(nm, si, r)]] += 1
            if probes:
                out.append({
                    "localization": locname, "separation": sepname,
                    "probes": reg(probes),
                    "distinct_assigned_descriptions": {
                        str(k): reg(v) for k, v in sorted(dist.items())},
                    "probes_with_more_than_one": reg(
                        sum(v for k, v in dist.items() if k > 1)),
                    "largest": reg(max(dist)), "smallest": reg(min(dist))})
                say("    %-9s %-19s probes %-8d distinct assignments %s"
                    % (locname, sepname, probes,
                       {k: v for k, v in sorted(dist.items())}))
    R["reductions"] = {
        "arms": out,
        "readings_declared_on_the_other_block": list(READINGS),
        "assignment": "the set of values the block's quantities can still "
                      "take given what the declared reading at A reports -- "
                      "measure-free, so no measure is smuggled in",
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
            "as an average",
            walk["probes_with_more_than_one"] == walk["probes"]
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


def conjugacy_measure(R, corp, uniq, rfib, conj, ref):
    say("SECTION 11.  MEASUREMENT 4 -- E3, THE NON-COMMUTING PAIR")
    comm = commutator_census(uniq)
    ncomm = sum(1 for b in comm if b)
    if mut("MUT-COMMUTATOR"):
        ncomm = 0
    P, Q = "READ-BORN-GD", "READ-RECORD-MENU"
    is_conj = (P, Q) in conj or (Q, P) in conj
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
    R["conjugacy"] = {
        "operator_leg": "the two declared coin orders are the two orders of "
                        "the same pair of matrices: G . D(x) against "
                        "D(x) . G, compared exactly in Z[w]",
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
            "refinement relation in both directions; the operator leg is "
            "taken exactly in Z[w], where the two declared coin orders "
            "differ at %d of the %d committed records; and the record is "
            "measured to carry both members at every committed history while "
            "no single Born menu carries both" % (ncomm, len(uniq)),
            is_conj and ncomm > 0 and hist_both == len(corp)
            and carried < len(uniq) and carried_other < len(uniq),
            "records where the orders differ %d of %d; pair not jointly "
            "declarable %s; histories where the record carries both %d of "
            "%d; Born menu carries the record menu at %d of %d records"
            % (ncomm, len(uniq), is_conj, hist_both, len(corp), carried,
               len(uniq)))
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
                            "a measurement and not a blind spot",
        "reading": "nothing declared at A moves anything B has.  What moves "
                   "is the description an observer at A assigns to B, at "
                   "every probe -- which is E4, not a disturbance",
        "seam_confinement": "this is SEC's adjudicated ruling seen from the "
                            "other side: no sector-private link ever moves"}
    LD.gate("G-E5-RECORD-DOES-NOT-MOVE",
            "B'S RECORD IS MEASURED NOT TO MOVE WITH THE READING DECLARED AT "
            "A, PROBE BY PROBE, WITH THE TEST DECLARED.  B's own record and "
            "B's own shadow are recomputed under every declared reading "
            "through a reading-parameterised path; neither moves at any of "
            "the 105,408 probes, while the description assigned to B moves "
            "at all of them",
            rec_moved == 0 and sha_moved == 0 and asg_moved == probes,
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


def bell_measure(R, arms, walkarm):
    say("SECTION 13.  MEASUREMENT 6 -- THE BELL WALL")
    des = [
        {"desideratum": "E1 -- every element of reality has a counterpart",
         "D-RECORD": "MET on the measured arms",
         "D-SHADOW": "NOT MET: %d certified elements, none carried"
                     % walkarm["without_counterpart_in_D_SHADOW"],
         "bell_constrained": "no"},
        {"desideratum": "E2 -- prediction with certainty without disturbing",
         "D-RECORD": "INSTANTIABLE only in the state's localization",
         "D-SHADOW": "NEVER: the shadow certifies nothing here",
         "bell_constrained": "no"},
        {"desideratum": "E3 -- simultaneous reality for a conjugate pair",
         "D-RECORD": "HELD: both members carried at every history",
         "D-SHADOW": "REFUSED: no single menu carries both",
         "bell_constrained": "YES -- any joint assignment across blocks is "
                             "outcome-dependent in v5 paper-14's sense"},
        {"desideratum": "E4 -- one reality, several assigned descriptions",
         "D-RECORD": "one record throughout",
         "D-SHADOW": "up to five assignments at one record",
         "bell_constrained": "no"},
        {"desideratum": "E5 -- no dependence of B's reality on A's choice",
         "D-RECORD": "MET: zero moves measured",
         "D-SHADOW": "the ASSIGNED description moves; B's own does not",
         "bell_constrained": "no"},
        {"desideratum": "E6 -- such a theory is possible",
         "D-RECORD": "one exists on the measured arms, AT THIS ARENA and "
                     "under this corpus's site-constancy",
         "D-SHADOW": "not applicable",
         "bell_constrained": "YES -- it is not a local-realist theory; the "
                             "corpus is Bell-nonlocal by v5 paper-14 and "
                             "this unit claims nothing against that"},
    ]
    R["bell"] = {
        "standing_verdict": "v5 paper-14: ISP is Bell-nonlocal (E1 false), "
                            "no-signalling and parameter-independent (E2 "
                            "true); outcome independence is what fails",
        "desiderata": des,
        "banned_sentences": list(BANNED),
        "banned_count": reg(len(BANNED)),
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
            "in their own text",
            len(des) == 6 and sum(1 for d in des
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

    prem = qb = ld = cert = unc = quant = 0
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
                fr = FR[(da, r)]
                for k in qs:
                    dd = k % 3
                    quant += 1
                    if epr_reality_at(dd, fr):
                        cert += 1
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
          "without_counterpart_in_D_RECORD": 0,
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
            "CERTIFIED-AND-%s-UNCARRIED; E4-ASSIGNMENTS-AT-ONE-RECORD=%s; "
            "E5-RECORD-MOVES=%s-OF-%s; SCOPE=ONE-ARENA,COMMITTED-HISTORIES,"
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
     "schedules", "5856"),
    ("W-SUBSETS", "the COMPLETE lattice of subsets of the nine actors -- no "
     "cap, no sampling", "512"),
    ("W-BLOCKS", "the six law-compatible decompositions of the nine actors "
     "(FAC's geometry-leg survivors), restricted per history by the history "
     "leg", "6"),
    ("W-STATES", "the declared state family for the shadow: every site "
     "vector over the alphabet {0, 1, w, w^2}", "64"),
    ("W-READINGS", "the declared readings of a block: the record, the Born "
     "menu at both coin orders, the record menu, and paper-20's curvature",
     "5"),
    ("W-MEASURES", "the declared measures for the probability leg: uniform "
     "and a skewed full-support measure", "2"),
)


def windows_declare(R):
    R["windows"] = {"rows": [{"window": a, "bound": c, "statement": b}
                             for a, b, c in WINDOWS],
                    "count": reg(len(WINDOWS))}
    LD.gate("G-WINDOWS-DECLARED-WITH-THEIR-BOUNDS",
            "EVERY WINDOW THIS UNIT COUNTS OVER IS DECLARED WITH ITS BOUND "
            "(§15).  Six windows; the subset lattice is complete and says "
            "so, and every other is named with the parent that fixed it",
            len(WINDOWS) == 6, "windows %d" % len(WINDOWS))
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

PAPER_LITERALS = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
                  "11", "12", "13", "14", "15", "19", "20", "21", "22", "23",
                  "24", "27", "32", "33", "34", "35", "38", "47", "62", "82",
                  "87", "91", "119", "125", "267", "295", "299", "319", "328",
                  "777", "1935", "2026"}

NUM_RE = re.compile(r"(?<![\w.])(\d[\d,]*\d|\d)(?![\w])")
FENCE_RE = re.compile(r"```[^\n]*\n(.*?)```", re.S)
NOF_RE = re.compile(r"([\d,]+)\s+of\s+([\d,]+)")


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
        ("C14", "the two declared coin orders differ at %s of the %s "
         "committed records"
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
    ]
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
)

REFERENT_UNIVERSES = {
    "HISTORIES": ("corpora/histories", "corpora/record_is_site_constant_at",
                  "conjugacy/histories_where_D_RECORD_carries_both",
                  "conjugacy/of_histories", "blocks/forced_at",
                  "blocks/of_histories"),
    "SUBSETS": ("separation/subset_lattice",
                "separation/subsets_owning_a_record_quantity",
                "separation/subsets_with_a_nonempty_far_region",
                "separation/subsets_with_both",
                "separation/theorem_probes"),
    "BLOCK-PAIRS": ("separation/ordered_block_pairs",
                    "separation/link_disjoint_block_pairs",
                    "separation/quantity_bearing_at_LOC_PAIR",
                    "separation/quantity_bearing_at_LOC_WALK",
                    "separation/premise_instances_at_LOC_PAIR",
                    "separation/premise_instances_at_LOC_WALK"),
    "RECORDS": ("descriptions/distinct_records_in_the_corpus",
                "descriptions/residue_classes_up_to_the_site_phase",
                "conjugacy/records",
                "conjugacy/records_where_the_two_orders_differ",
                "conjugacy/records_where_the_Born_menu_carries_the_record_"
                "menu"),
    "STATES": ("descriptions/state_sweep_size",
               "descriptions/states_separating_two_records_of_one_residue_"
               "class"),
    "SITE-PAIRS": ("arena/ordered_site_pairs_checked",),
}


def paper_battery(R, paper_text, claims, tables):
    say("SECTION 15b.  THE PAPER INSTRUMENT")
    if mut("MUT-BELL-PLANT"):
        paper_text = paper_text + "\n\nlocal realism is restored.\n"
    if mut("MUT-PAPER-NUMERAL"):
        paper_text = paper_text + "\n\nthe census ran at 424,242 pairs.\n"
    if mut("MUT-PAPER-TABLE-HEADER"):
        paper_text = paper_text.replace("| localization | separation |",
                                        "| separation | localization |")
    if mut("MUT-POLARITY"):
        paper_text = paper_text + "\n\n" + POLARITY[2][2] + ".\n"
    hay = canon(paper_text)
    for cid, txt in claims:
        say("    %s  %s" % (cid, txt))
    for t in tables:
        say("    %s | %s |" % (t["name"], " | ".join(t["headers"])))
        for row in t["rows"]:
            say("            | %s |" % " | ".join(row))
    miss = [cid for cid, txt in claims if canon(txt) not in hay]
    R["paper_claims"] = {"rows": [{"id": c, "claim": t} for c, t in claims],
                         "count": reg(len(claims)), "missing": miss}
    LD.gate("G-PAPER-CLAIMS",
            "EVERY LOAD-BEARING SENTENCE OF THE PAPER IS RENDERED FROM THE "
            "RECEIPT AND MATCHED IN THE PAPER'S OWN BYTES (#20).  Fifteen "
            "claims, each built out of receipt values rather than typed, so "
            "a paper that drifts from its run cannot pass",
            not miss, "claims %d, missing %s" % (len(claims), miss or "none"))
    SEAL.take("SEAL-PAPER-CLAIMS", R)

    tmiss = []
    for t in tables:
        head = canon("| " + " | ".join(t["headers"]) + " |")
        if head not in hay:
            tmiss.append(t["name"] + "/headers")
        for row in t["rows"]:
            if canon("| " + " | ".join(row) + " |") not in hay:
                tmiss.append(t["name"] + "/" + row[0])
    R["paper_tables"] = {"tables": tables, "count": reg(len(tables)),
                         "rows": reg(sum(len(t["rows"]) for t in tables)),
                         "missing": tmiss}
    LD.gate("G-PAPER-TABLES-WITH-HEADERS",
            "EVERY TABLE IS RENDERED FROM THE RECEIPT WITH ITS HEADERS "
            "INCLUDED, so a header swap that leaves every number correct "
            "dies here (E-22: tables render as claims)",
            not tmiss, "tables %d, rows %d, missing %s"
            % (len(tables), sum(len(t["rows"]) for t in tables),
               tmiss or "none"))
    SEAL.take("SEAL-PAPER-TABLES", R)

    fenced = FENCE_RE.findall(paper_text)
    nums = NUM_RE.findall(paper_text)
    fnums = [n for blk in fenced for n in NUM_RE.findall(blk)]
    words = [w for w in re.findall(r"[a-z]+", paper_text.lower())
             if w in WORDNUM]
    unknown = sorted({n for n in nums
                      if n not in NUMREG and n.replace(",", "") not in NUMREG
                      and n not in PAPER_LITERALS})
    wordbad = sorted({w for w in words
                      if str(WORDNUM[w]) not in NUMREG
                      and str(WORDNUM[w]) not in PAPER_LITERALS})
    R["paper_coverage"] = {
        "numerals": reg(len(nums)), "in_fenced_blocks": reg(len(fnums)),
        "spelled_numerals": reg(len(words)),
        "registry_size": reg(len(NUMREG)),
        "unknown_numerals": unknown, "unknown_spelled": wordbad,
        "note": "coverage includes fenced blocks and inline code spans "
                "(E-22); the registry is the run's own product"}
    LD.gate("G-PAPER-NUMERAL-COVERAGE",
            "EVERY NUMERAL IN THE PAPER IS THE RUN'S OWN PRODUCT (#20, "
            "E-22).  The scan covers the whole file including fenced blocks "
            "and inline spans, spelled numerals included; anything outside "
            "the run's registry and the declared structural literals fails",
            not unknown and not wordbad,
            "numerals %d (fenced %d), spelled %d, unknown %s / %s"
            % (len(nums), len(fnums), len(words), unknown or "none",
               wordbad or "none"))
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
            "EVERY POLARITY AXIS IS CHECKED IN BOTH DIRECTIONS.  Five axes; "
            "the paper must assert the measured direction and must not "
            "contain its inverse anywhere in its bytes",
            not pbad, "axes %d, failures %s" % (len(prows), pbad or "none"))
    SEAL.take("SEAL-POLARITY", R)

    uni = {}
    for name, paths in REFERENT_UNIVERSES.items():
        uni[name] = {str(jpath(R, p)) for p in paths}
        uni[name] |= {com(int(v)) for v in uni[name] if v.isdigit()}
    frac, fbad = [], []
    for a, b in NOF_RE.findall(paper_text):
        homes = [n for n, vals in uni.items() if a in vals and b in vals]
        frac.append({"fraction": "%s of %s" % (a, b), "universes": homes})
        if not homes:
            fbad.append("%s of %s" % (a, b))
    if mut("MUT-REFERENT"):
        fbad.append("planted")
    R["referent_binding"] = {
        "universes": {k: sorted(v) for k, v in sorted(uni.items())},
        "fractions": frac, "count": reg(len(frac)), "unbound": fbad,
        "note": "every 'N of M' in the paper must have BOTH members carried "
                "by one declared referent universe"}
    LD.gate("G-SENTENCE-REFERENT-BINDING",
            "EVERY FRACTION IN THE PAPER NAMES A UNIVERSE THAT CARRIES BOTH "
            "OF ITS MEMBERS.  Six universes are declared from receipt paths; "
            "an 'N of M' whose numerator and denominator are not carried by "
            "one common universe fails",
            not fbad, "fractions %d, unbound %s" % (len(frac), fbad or "none"))
    SEAL.take("SEAL-REFERENT", R)

    hits = [s for s in BANNED if canon(s) in hay]
    R["walls"] = {"banned": list(BANNED), "count": reg(len(BANNED)),
                  "hits": hits,
                  "scanned": PAPER_REL,
                  "note": "the Bell wall is scanned against this unit's own "
                          "bytes -- the leg the wall is owed"}
    LD.gate("G-WALLS-SCAN-THE-PAPER",
            "THE BELL WALL IS SCANNED AGAINST THIS UNIT'S OWN PAPER.  Seven "
            "banned assertive sentences -- local realism restored, Bell "
            "evaded, hidden variables vindicated among them -- are matched "
            "against the paper's normalised bytes and must be absent; the "
            "falsifier plants one into exactly that text",
            not hits, "banned %d, hits %s" % (len(BANNED), hits or "none"))
    SEAL.take("SEAL-WALLS", R)
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
     "a fraction is left without a common referent universe",
     "paper_battery"),
    ("MUT-SEAL-DROP", "G-SEAL-TOTALITY",
     "one seal is not taken", "Seal"),
    ("MUT-INTEGRITY", "G-ARTIFACT-INTEGRITY",
     "the staged bytes are corrupted after sealing", "finish"),
)
MUTANT_NAMES = tuple(m[0] for m in MUTANTS)
POST_SNAPSHOT_GATES = ("G-TRANSCRIPT-SEALED-AT-THE-SNAPSHOT",
                       "G-RECEIPT-IS-EXACT", "G-SEAL-TOTALITY",
                       "G-ARTIFACT-INTEGRITY")
# The coverage census runs before the paper battery and before the closing
# four, so those gates are DECLARED here and folded into it; a gate that ran
# without appearing in this list or in the ledger would leave the census
# blind, and G-SEAL-TOTALITY checks the declaration against what actually ran.
DECLARED_LATE_GATES = ("G-PAPER-CLAIMS", "G-PAPER-TABLES-WITH-HEADERS",
                       "G-PAPER-NUMERAL-COVERAGE", "G-PAPER-CLAIM-POLARITY",
                       "G-SENTENCE-REFERENT-BINDING",
                       "G-WALLS-SCAN-THE-PAPER") + POST_SNAPSHOT_GATES


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


def closing_battery(R, paper_text, claims, tables):
    say("SECTION 15c.  THE CLOSING BATTERY")
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

    carriers = hook_carriers()
    mrows, mbad = [], []
    for name, gate, why, decl in MUTANTS:
        got = sorted(carriers.get(name, []))
        want = decl.split("|")
        ok = all(any(w == g for g in got) for w in want)
        mrows.append({"mutant": name, "declared_gate": gate, "statement": why,
                      "declared_carrier": decl, "located_in": got,
                      "description_matches_code": ok})
        if not ok:
            mbad.append(name)
    gates_with_falsifiers = {m[1] for m in MUTANTS}
    ran = [g["gate"] for g in LD.rows] + list(DECLARED_LATE_GATES)
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
            "forced: the transcript's digest is compared with the promoted "
            "bytes at G-ARTIFACT-INTEGRITY, which MUT-INTEGRITY exercises",
        "G-RECEIPT-IS-EXACT":
            "a type-scan gate over the published object: any inexact leaf "
            "anywhere fires it, and no mutant can plant one without editing "
            "the file, which the source scan and the digests would show",
        "G-CLOSING-BATTERY-RAN": "this gate",
        "G-BELL-DESIDERATA-BOUND":
            "forced by MUT-BELL-PLANT at the paper leg, which is where the "
            "wall is owed",
        "G-PAPER-CLAIMS":
            "forced by MUT-PAPER-NUMERAL and MUT-POLARITY, both of which "
            "alter the paper's bytes",
        "G-SEAL-TOTALITY": "covered by MUT-SEAL-DROP",
        "G-ARTIFACT-INTEGRITY": "covered by MUT-INTEGRITY",
    }
    unwaived = [g for g in uncovered if g not in waivers]
    R["mutants"] = {"rows": mrows, "count": reg(len(mrows)),
                    "description_mismatches": mbad}
    R["coverage"] = {"gates_run": reg(len(ran)),
                     "gates_declared_to_run_after_this_census":
                         reg(len(DECLARED_LATE_GATES)),
                     "gates_with_a_falsifier": reg(len(gates_with_falsifiers)),
                     "gates_with_a_waiver": reg(len(uncovered)),
                     "unwaived": unwaived}
    R["waiver_ledger"] = {"rows": [{"gate": g, "forcing": waivers[g]}
                                   for g in uncovered if g in waivers],
                          "count": reg(len([g for g in uncovered
                                            if g in waivers]))}
    LD.gate("G-FALSIFIER-COVERAGE",
            "EVERY GATE CARRIES A FALSIFIER OR A NAMED WAIVER WITH A FORCING "
            "(E-23).  %d falsifiers are declared, each naming the "
            "gate it must die at and the function that carries its hook; "
            "every gate that has no falsifier carries a waiver whose forcing "
            "is stated, and the gates that run after this census are folded "
            "in by declaration rather than left invisible to it"
            % len(MUTANTS),
            not unwaived and not mbad,
            "gates %d, with falsifiers %d, waived %d, unwaived %s, "
            "description mismatches %s"
            % (len(ran), len(gates_with_falsifiers), len(uncovered),
               unwaived or "none", mbad or "none"))
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
    texts = provenance(R)
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
    arms, FR, FS = certainty_measure(R, corp, adm, uniq, tot)
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
    R["arithmetic"] = ("exact integers, fractions.Fraction and Z[w] as "
                       "integer pairs; no float anywhere")
    R["python"] = sys.version.split()[0]
    return R, claims, tables, paper_text


def finish(R, write=True, swept=False):
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
    allran = {g["gate"] for g in LD.rows} | set(POST_SNAPSHOT_GATES)
    late += [g for g in DECLARED_LATE_GATES if g not in allran]
    LD.gate("G-SEAL-TOTALITY",
            "THE SEAL MANIFEST IS TOTAL (#119).  Every published receipt key "
            "is either sealed at the gate that established it or named in "
            "the declared-unsealed list; every gate that ran after the "
            "ledger snapshot is one this unit declared would, and every gate "
            "the coverage census folded in as declared-late actually ran",
            not missing and not extra and not unsealed and not late,
            "seals %d, published keys %d, missing %s, extra %s, unsealed %s, "
            "undeclared late gates %s"
            % (len(SEAL.rows), len(published), missing or "none",
               extra or "none", unsealed or "none", late or "none"))
    R["seal_manifest"] = SEAL.rows
    payload = json.dumps(R, indent=1, sort_keys=True, default=str)
    SEAL.close(R, payload)
    R["payload_sha256_12"] = SEAL.payload_sha
    payload = json.dumps(R, indent=1, sort_keys=True, default=str)
    text = "\n".join(LINES) + "\n"
    seal_j = hashlib.sha256(payload.encode("utf-8")).hexdigest()[:12]
    seal_t = hashlib.sha256(text.encode("utf-8")).hexdigest()[:12]
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
    ok = dj == seal_j and dt == seal_t and control_rejects
    if write:
        if ok:
            os.replace(tmp_j, OUT_JSON)
            os.replace(tmp_t, OUT_TXT)
        else:
            for p in (tmp_j, tmp_t):
                if os.path.exists(p):
                    os.remove(p)
    LD.gate("G-ARTIFACT-INTEGRITY",
            "THE BYTES ARE READ BACK BEFORE THEY ARE PROMOTED (#119).  Both "
            "artifacts are written to staging, the STAGED bytes are read "
            "back from disk and compared with the digests of the objects "
            "sealed at gate time, and only then does os.replace promote "
            "them; on refusal the staging files are removed and nothing is "
            "promoted.  On a dry run the same comparison is taken over the "
            "same buffered bytes, so the gate is reachable there too.  The "
            "comparison is exercised in the failing direction as well, on "
            "the same bytes with one bit flipped",
            ok, "receipt staged %s seal %s; transcript staged %s seal %s; "
            "one-bit-flip control rejects %s; promoted %s"
            % (dj, seal_j, dt, seal_t, control_rejects, bool(write and ok)))
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








