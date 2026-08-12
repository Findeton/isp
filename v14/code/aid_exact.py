#!/usr/bin/env python3
"""AID (paper-33) -- ARE ACTORS DERIVED?  THE IDENTITY-RECONSTRUCTION CENSUS.

QUESTION (pin `v14/note-aid-pin.md`, sha256-12 294ffe6c9deb, ledger #268).
Is the actor LABELING forced by participation structure?  A committed history
is a sequence of division events, each an actor-subset.  THE STABILIZER of a
history is the subgroup of S_9 that fixes every event SETWISE; it is therefore
a function of the event SET and not of the order, and the order enters this
unit only through the crystallization TIME.  Identity is FORCED on a history
exactly when that stabilizer is trivial; the FIBER is the stabilizer itself.
What is measured is the LABELLING of a declared nine-actor grain, never the
choice of that grain: the DECOMPOSITION question -- which subsystems there are
-- is not touched here, and the global grain presupposes that actors persist
across events.

THE INVARIANCE RESULT, IN ITS LICENSED FORM.  Transport the reading and every
committed observable is blind by theorem; fix the reading and none is -- the
weld's own count field and the record are ONE OBJECT at the identity parse,
and both fail on the great majority of the un-forced objects, the depth-two
menu on more.  The one measured ordering between observables is DEPTH, and it
is coin-order-relative until both declared orders are published.  NO SENTENCE
OF THIS UNIT ASSIGNS IDENTITY TO MATTER AND CHART TO SPACE: that reading is
refused on the measurement's own evidence, and the reading walls of SEC 8 scan
the paper under test for it and for its paraphrases.

WHAT THIS FILE MEASURES, IN ORDER.

  SEC 1  PROVENANCE.  Thirteen pinned sources, sha256-12 verified, every
         product consumed by a gate; the #62 verbatim anchors bound to their
         consumer gates.
  SEC 2  THE ARENA AND THE SUBSTRATE.  AG(2,3), the 280 groupings, the 36
         saturating ones, the 72 R = 3 I7-STRICT triples, the 276 G-FLAT
         quadruples and paper-21's 600-schedule window -- each recomputed
         here and back-validated against the parents' committed receipts.
  SEC 3  THE DRIVEN LEG.  The committed v10 layers are driven directly and
         the FOOTPRINT SEQUENCE of every driven record is compared, event by
         event, with the combinatorial group sequence; the identity is also
         established structurally from d42b1's own `regs_of` by AST.  Two
         legs, and every exhaustive column below is licensed by them.
  SEC 4  THE STABILIZER CENSUS.  Two independent routes: ROUTE A filters the
         362,880 elements of S_9 explicitly, ROUTE B builds the Young
         subgroup of the participation-signature partition.  Per object,
         element set against element set.
  SEC 5  THE CRYSTALLIZATION TIME.  The earliest prefix whose stabilizer is
         trivial, per history, per corpus; the never-crystallizing histories
         censused and characterised; the INFORMATION FLOOR (the smallest event
         SUBSET that forces identity) against the schedule's redundant event;
         and the full within-round ORDER AXIS, run entire.
  SEC 6  THE PHYSICS-INVARIANCE CENSUS.  Where the stabilizer is nontrivial:
         the co-division relation, the weld dictionary's readings at all
         TWELVE declared parses, the record n_l(x), and the walk's Born menu
         at BOTH declared coin orders -- each evaluated under the stabilizer,
         exactly, under BOTH declared tests (the transported reading and the
         fixed attribution), because the split this unit measures is a split
         between the two TESTS and not between the observables.
  SEC 7  THE GRAIN.  The global-relabelling grain is what ran; the groupoid
         grain is REGISTERED as the successor question and not run.
  SEC 8  THE HEAD, derived twice by disjoint code, the paper instrument, the
         coverage/polarity ledgers and the closing battery.

SCOPE AND LANGUAGE.  "FORCED", "CHART" and "STRATIFIED" name measured
properties of the stabilizer and of the invariance census and nothing else.
No sentence of this unit asserts anything about actors beyond the two
measurements it publishes, and every such sentence is description-stamped.

ARITHMETIC.  Exact only: Python integers, `fractions.Fraction` and the
quadratic ring Z[w] carried as integer pairs.  There are no floats anywhere;
an AST scan of this file and a recursive type scan of the emitted receipt are
gates.

RUNTIME INPUTS (#46/#91).  Exactly thirteen files are read at run time as
SOURCES, all hash-pinned by this unit's frozen declaration and all committed
objects at the commit shas the declaration names, plus exactly one file read
as the OBJECT UNDER TEST -- this unit's own paper.  No repository state
outside those lists is read and no subprocess of any kind is invoked, so the
run is correct off-tree and with no version control present.
"""

import ast
import hashlib
import json
import math
import os
import re
import sys
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations, product

sys.setrecursionlimit(100000)

SELF = os.path.abspath(__file__)
REPO = os.path.dirname(os.path.dirname(os.path.dirname(SELF)))
OUT_TXT = os.path.join(os.path.dirname(SELF), "aid_output.txt")
OUT_JSON = os.path.join(os.path.dirname(SELF), "aid_receipt.json")

SCHEMA = "isp/v14/aid-identity-reconstruction/1"
PAPER_REL = "v14/paper-33-aid.md"

# ===========================================================================
# SECTION 0.  THE FROZEN DECLARATION (RUNBOOK section 15: the arena is data)
# ===========================================================================

SOURCES = [
    ("A-PIN", "v14/note-aid-pin.md", "294ffe6c9deb",
     "THIS UNIT'S PIN (ledger #268, commit f1e9fbf): the formal object, the "
     "three corpora, the five stages, the outcome names and the grain note."),
    ("A-P19", "v14/paper-19-r3-weld.md", "50bb81e67942",
     "PAPER 19 (terminal, commit 559e162): the R = 3 arena, the weld "
     "dictionary -- site from ACTOR, link from the CO-DIVISION ACTOR PAIR, "
     "count from the division count -- and the 72 I7-STRICT triples."),
    ("A-P19REC", "v14/code/r3_weld_receipt.json", "dfea664f2408",
     "PAPER 19's COMMITTED RECEIPT (commit 559e162): the R = 3 arena as "
     "data -- divisions per record, the isomorphism count, the strict-triple "
     "count -- read from these bytes and reproduced here."),
    ("A-P19SRC", "v14/code/r3_weld_exact.py", "f95a26a1764b",
     "PAPER 19's COMMITTED DRIVER (commit 559e162): the schedule driver this "
     "unit re-implements, and the `record_of` footprint rule it inherits."),
    ("A-P21", "v14/paper-21-r4dec.md", "ef4a8c35a0c4",
     "PAPER 21 (terminal, commit 7d675c1): the R = 4 window of 600 driven "
     "schedules, the R = 6 door -- 72 triples, 5,184 ordered "
     "concatenations -- and the driven-equals-combinatorial licence."),
    ("A-P21REC", "v14/code/r4dec_receipt.json", "a4538c7019e6",
     "PAPER 21's COMMITTED RECEIPT (commit 7d675c1): the window size, the "
     "division count per record, the saturating and flat-quadruple counts, "
     "and the R = 6 door's own ordered-witness count, read as data."),
    ("A-P21SRC", "v14/code/r4dec_exact.py", "1958a8cdfe28",
     "PAPER 21's COMMITTED CODE (commit 7d675c1): the window constructor and "
     "the driver whose event order this unit reproduces."),
    ("A-P20", "v14/paper-20-coupling.md", "4824d190af73",
     "PAPER 20 (terminal, commit 1196ad6): the coupled walk -- the Born menu "
     "reading, the site-block-diagonal coin C(x) = G.D(x) and the shift."),
    ("A-P20REC", "v14/code/coupling_receipt.json", "55273f6b6068",
     "PAPER 20's COMMITTED RECEIPT (commit 1196ad6): the walk's declared "
     "arena -- cells, links, coin -- read as data."),
    ("A-P20SRC", "v14/code/coupling_exact.py", "72e7b299f66e",
     "PAPER 20's COMMITTED CODE (commit 1196ad6): the Z[w] arithmetic, the "
     "Grover coin numerators and the shift table this unit re-implements "
     "rather than imports."),
    ("A-D42B1", "v10/code/d42b1_transport_exact.py", "576275d55ecf",
     "THE COMMITTED TRANSPORT GRAMMAR (commit f1e9fbf): `regs_of` -- the "
     "single source of the footprint rule -- and the admissibility menu."),
    ("A-D60", "v10/code/d60_crystal_exact.py", "684cdb76552b",
     "D60 (commit f1e9fbf): the Builder `B`, AST-extracted and driven."),
    ("A-D66", "v10/code/d66_arbitration_crystal_exact.py", "3d0516ab106e",
     "D66 (commit f1e9fbf): CONFLICT-GRID(g, R), the committed constructor "
     "whose group and member order this unit's driver reproduces."),
]
SOURCE_IDS = [s[0] for s in SOURCES]

# THE DECLARED WINDOWS.  Every one is disclosed here, in the head, and in the
# paper, and each is gated for the property that licenses it (#34/section 15).
WINDOW_DECL = [
    ("W-C1", True,
     "THE 72 R = 3 I7-STRICT TRIPLES, ENTIRE.  Every ordered triple "
     "of saturating groupings whose summed link field covers all "
     "27 cells; driven at the FIRST canonical transversal of each "
     "round.  No sampling: the corpus is the whole class."),
    ("W-C1FAN", True,
     "THE SEED FAN OVER W-C1, ENTIRE.  The same 72 triples at ALL "
     "27 canonical transversal triples, so the CANONICAL SEED MENU -- the "
     "declared three-transversal menu of each round, which is what moves the "
     "within-round event order in the committed constructor -- is exhausted "
     "rather than fixed.  It is the canonical menu and not the whole seed "
     "axis: W-ORDER below opens the order axis itself."),
    ("W-C2", True,
     "THE 5,184 ORDERED R = 6 CONCATENATIONS, ENTIRE.  Every ordered "
     "pair of W-C1 triples, concatenated -- paper-21's own R = 6 "
     "door, at its own ordered-witness count."),
    ("W-C3", True,
     "PAPER-21's DRIVEN WINDOW W4, ENTIRE.  All 600 committed "
     "schedules -- W4-CLASS, W4-FLAT, W4-SEEDFAN and W4-CTRL -- "
     "reconstructed here by paper-21's own constructor and gated "
     "against its committed window size."),
    ("W-ORDER", True,
     "THE FULL WITHIN-ROUND ORDER AXIS OVER W-C1, ENTIRE.  Every one of the "
     "six orderings of the three conflict groups of every round, at every "
     "one of the 72 triples: 15,552 histories.  The declared seed menu of "
     "W-C1FAN realises only some of these orderings, so this window and not "
     "the fan is what exhausts the order axis."),
    ("W-C3REV", True,
     "THE ORDER-REVERSAL OVER W-C3, ENTIRE.  Every one of the 600 committed "
     "R = 4 schedules re-entered with each round's three groups in "
     "DESCENDING rather than ascending seed order.  One declared point of "
     "the order axis, taken at every history of the corpus, and it is what "
     "shows the crystallization TIME reads the order that the stabilizer "
     "does not."),
    ("W-PARSE", True,
     "THE TWELVE DECLARED WELD PARSES, ENTIRE.  Paper-19's dictionary reads "
     "through a link-label permutation and an orientation: 3! x 2 = 12 "
     "readings.  The blindness sweep is taken at every one of them and not "
     "at the identity parse alone."),
    ("W-COIN", True,
     "THE TWO DECLARED COIN ORDERS, ENTIRE.  Paper-20's coupled step admits "
     "C(x) = G.D(x) and C(x) = D(x).G; the order is a declared fiber and "
     "BOTH members are run here to every published depth, because the "
     "depth at which the menu refines the record depends on it."),
    ("W-DRIVE", False,
     "THE DRIVEN VERIFICATION SET.  The committed v10 layers are "
     "expensive to drive, so the driven leg is taken on a "
     "DECLARED set: the first 9 W-C1 triples in enumeration "
     "order, the four constant-class W-C3 quadruples together "
     "with d66's own committed R = 4 point and the collinear "
     "arrangement, and the first 2 W-C2 concatenations.  Each is "
     "compared event by event against the combinatorial route, "
     "and the structural leg carries the rest."),
    ("W-AUTC2", False,
     "THE AUTOMORPHISM WINDOW OVER W-C2.  The co-division "
     "automorphism group is enumerated on the 72 DIAGONAL "
     "concatenations (T, T) -- paper-21's own R = 6 witness "
     "form -- rather than on all 5,184."),
    ("W-WALK", False,
     "THE WALK'S DEPTH.  Paper-20's coupled step is re-implemented "
     "here and run to depth 5 from the S_9-symmetric start; every "
     "depth is published, so the depth is not a hidden cap."),
    ("W-GAUGE", False,
     "THE ALTERNATIVE LINK DECLARATION.  AG(2,3) carries four parallel "
     "classes and the corpus declares three; the substrate is rebuilt once "
     "with ANT in place of DIA and the R = 3 census recomputed on it.  One "
     "declared alternative of the four, taken to show the declaration is a "
     "GAUGE CHOICE and not an artifact."),
]

# THE #62 VERBATIM ANCHORS, each bound to a consumer gate that is non-literal
# and falsified by a declared mutant.
VERBATIM = [
    ("V01", "A-PIN",
     "THE STABILIZER of a history = the subgroup of S", "G-STAB-ROUTES"),
    ("V02", "A-PIN",
     "the earliest prefix length at which the stabilizer becomes trivial",
     "G-CRYSTALLIZATION"),
    ("V03", "A-PIN",
     "any non-invariance \u27f9 the observable NAMES threads the structure "
     "does not force", "G-INVARIANCE-SPLIT"),
    ("V04", "A-PIN",
     "mid-history thread-swaps (the groupoid grain) are REGISTERED as the "
     "successor question", "G-GRAIN-REGISTERED"),
    ("V05", "A-P19",
     "site \u2190 ACTOR, link \u2190 the co-division actor pair, count "
     "\u2190 the division", "G-WELD-DICTIONARY"),
    ("V06", "A-P21",
     "the field the combinatorial route computes from the schedule's "
     "groupings alone", "G-DRIVEN-EQUALS-COMBINATORIAL"),
    ("V07", "A-P21",
     "concatenating two of the R = 3 I7-STRICT triples", "G-CODIVISION-FORGETS"),
    ("V08", "A-P20",
     "The menu at site x is the three link", "G-BORN-MENU"),
    ("V09", "A-P19",
     "carries the identical co-division arena: the same nine site objects",
     "G-CODIVISION-BLIND"),
    ("V10", "A-P21",
     "one arbitration per conflict group per round -- and record length",
     "G-EVENT-SHAPE"),
]

# ===========================================================================
# SECTION 1.  MACHINERY -- the gate ledger, the seal, the text normaliser
# ===========================================================================

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


SEALED_PATHS = [
    ("SEAL-SCHEMA", "schema", "G-PROVENANCE"),
    ("SEAL-PROVENANCE", "provenance", "G-PROVENANCE"),
    ("SEAL-VERBATIM", "verbatim_anchors", "G-VERBATIM"),
    ("SEAL-WINDOWS", "windows", "G-WINDOWS-DISCLOSED"),
    ("SEAL-SUBSTRATE", "substrate", "G-BACK-VALIDATION"),
    ("SEAL-DRIVEN", "driven", "G-DRIVEN-EQUALS-COMBINATORIAL"),
    ("SEAL-CORPORA", "corpora", "G-CORPORA-SHAPE"),
    ("SEAL-STABILIZER", "stabilizer", "G-STAB-ROUTES"),
    ("SEAL-CRYSTAL", "crystallization", "G-CRYSTALLIZATION"),
    ("SEAL-INVARIANCE", "invariance", "G-INVARIANCE-SPLIT"),
    ("SEAL-WALK", "walk", "G-BORN-MENU"),
    ("SEAL-GRAIN", "grain", "G-GRAIN-REGISTERED"),
    ("SEAL-WALLS", "walls", "G-WALLS-SCAN-THE-PAPER"),
    ("SEAL-WALLS-POSITIVE", "walls_positive", "G-WALLS-SCAN-THE-PAPER"),
    ("SEAL-PAPER-BINDING", "paper_binding", "G-PAPER-CONTRADICTION"),
    ("SEAL-MEASURE", "measure_relativity", "G-E24-MEASURE"),
    ("SEAL-VERDICT", "verdict", "G-VERDICT-RECONSTRUCTED"),
    ("SEAL-COUNTS", "counts", "G-VERDICT-RECONSTRUCTED"),
    ("SEAL-PAPER-CLAIMS", "paper_claims", "G-PAPER-CLAIMS"),
    ("SEAL-PAPER-TABLES", "paper_tables", "G-PAPER-TABLES"),
    ("SEAL-PAPER-COVERAGE", "paper_coverage", "G-PAPER-HEAD-VERBATIM"),
    ("SEAL-POLARITY", "polarity", "G-PAPER-CLAIM-POLARITY"),
    ("SEAL-COVERAGE", "coverage", "G-COVERAGE"),
    ("SEAL-REACHABILITY", "reachability", "G-REACHABILITY"),
    ("SEAL-WAIVERS", "waiver_ledger", "G-COVERAGE"),
    ("SEAL-MUTANTS", "mutants", "G-COVERAGE"),
    ("SEAL-MUTANT-SWEEP", "mutant_sweep", "G-SWEEP-BOUND"),
    # #292 m-5: each of the four below now names the gate that ESTABLISHES its
    # value rather than the last gate that happened to precede it.
    ("SEAL-GATES", "gates", "G-GATE-ACCOUNTING"),
    ("SEAL-CLOSING", "closing_gates", "G-GATE-ACCOUNTING"),
    ("SEAL-TOTALS", "totals", "G-GATE-ACCOUNTING"),
    ("SEAL-TRANSCRIPT", "transcript_head", "G-TRANSCRIPT-INTEGRITY"),
]
DECLARED_UNSEALED = ["arithmetic", "python", "seal_manifest",
                     "payload_sha256_12", "closing_gate_verdicts"]
MEASURED_KEYS = ("substrate", "driven", "corpora", "stabilizer",
                 "crystallization", "invariance", "walk", "grain",
                 "measure_relativity", "counts", "verdict")


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
            return          # the row never reaches self.rows or the manifest
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
    """#292 m-4: a missing pinned source is a GATE failure, not a traceback.
    A bare copy of this file therefore dies at G-PROVENANCE, loudly, by the
    same mechanism as a source whose bytes have moved, and writes nothing."""
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
    """EVERY text read is categorised and recorded.  There is no uncategorised
    reader in this file, and the category sets are gated at G-READS-DECLARED."""
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
         "∩": "cap", "≅": "iso", "≤": "<=", "⊲": "normal"}

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
    """#125, with the mid-word residual closed: both sides are compared as
    written AND with all whitespace stripped, so a needle broken by a line
    wrap INSIDE a word matches too."""
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
            NUMREG.add(com(v))     # thousands-grouped only; see THOUSANDS
        elif isinstance(v, Fraction):
            NUMREG.add(str(v.numerator))
            NUMREG.add(str(v.denominator))
            NUMREG.add("%d/%d" % (v.numerator, v.denominator))
        elif isinstance(v, str):
            NUMREG.add(v)
    return vals[0] if vals else None


# ===========================================================================
# SECTION 2.  EXACT ARITHMETIC ON Z_3^2 AND THE COMBINATORIAL SUBSTRATE
# ===========================================================================

SITES = tuple((i, j) for i in range(3) for j in range(3))
SITE_INDEX = {s: k for k, s in enumerate(SITES)}
DIRECTIONS = ((1, 0), (0, 1), (1, 1), (1, 2))
I7_LINKS = ((1, 0), (0, 1), (1, 1))
CLASS_NAMES = ("ROW", "COL", "DIA", "ANT")
CLASS_DIR = {"ROW": (0, 1), "COL": (1, 0), "DIA": (1, 1), "ANT": (1, 2)}
NACT = len(SITES)


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
CLASS_OF = {CLASSES[k]: k for k in CLASS_NAMES}
DIAG_SEED = ((0, 0), (1, 1), (2, 2))
CELLS = tuple((x, l) for x in SITES for l in I7_LINKS)
NUMWORDS = ("ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN",
            "EIGHT", "NINE", "TEN", "ELEVEN", "TWELVE")
WORDNUM = dict({w.lower(): i for i, w in enumerate(NUMWORDS)},
               twice=2, twenty=20, hundred=100, thirteen=13, fourteen=14,
               fifteen=15, sixteen=16, eighteen=18, thirty=30, forty=40)


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
    return [tuple(sorted(g)[k] for g in P) for k in range(3)]


def round_vec(P):
    """the per-(site, link) incidence 27-vector of ONE round's grouping: cell
    (x, l) carries 1 exactly when x and x + l share a conflict group."""
    return tuple(1 if any(x in g and vadd(x, l) in g for g in P) else 0
                 for (x, l) in CELLS)


RAW = {}


def raw_census():
    if RAW:
        return RAW
    parts = all_partitions()
    vecs = [round_vec(P) for P in parts]
    RAW["parts"] = parts
    RAW["vecs"] = vecs
    RAW["incidences"] = [sum(v) for v in vecs]
    RAW["sat"] = [i for i, v in enumerate(vecs) if sum(v) == len(SITES)]
    RAW["index"] = {P: i for i, P in enumerate(parts)}
    return RAW


def strict_triples():
    """paper-21's I7-STRICT class at R = 3: ordered triples of saturating
    groupings whose summed link field covers every one of the 27 cells."""
    C = raw_census()
    V = [C["vecs"][i] for i in C["sat"]]
    out = []
    for ia, a in enumerate(V):
        for ib, b in enumerate(V):
            ab = [a[k] + b[k] for k in range(len(CELLS))]
            for ic, c in enumerate(V):
                if all(ab[k] + c[k] >= 1 for k in range(len(CELLS))):
                    out.append((C["sat"][ia], C["sat"][ib], C["sat"][ic]))
    return out


def flat_quadruples():
    """paper-21's 276: ordered quadruples of saturating groupings whose summed
    link field is I7's G-FLAT row (1, 1, 2) at all nine sites."""
    C = raw_census()
    V = [C["vecs"][i] for i in C["sat"]]
    tgt = [1, 1, 2] * len(SITES)
    out = []
    for ia, a in enumerate(V):
        for ib, b in enumerate(V):
            ab = [a[k] + b[k] for k in range(len(CELLS))]
            if any(ab[k] > tgt[k] for k in range(len(CELLS))):
                continue
            for ic, c in enumerate(V):
                abc = [ab[k] + c[k] for k in range(len(CELLS))]
                if any(abc[k] > tgt[k] for k in range(len(CELLS))):
                    continue
                for idd, d in enumerate(V):
                    if all(abc[k] + d[k] == tgt[k] for k in range(len(CELLS))):
                        out.append((C["sat"][ia], C["sat"][ib],
                                    C["sat"][ic], C["sat"][idd]))
    return out


GAUGE_LINKS = ((1, 0), (0, 1), (1, 2))    # W-GAUGE: ANT in place of DIA


def gauge_substrate(links):
    """W-GAUGE.  The whole R = 3 substrate rebuilt against a DIFFERENT choice
    of three declared link directions: the incidence 27-vector, the saturating
    groupings, the I7-STRICT triples and the G-FLAT quadruples.  AG(2,3)
    carries four parallel classes and PGL(2,3) permutes them, so which three
    are declared should change nothing; this function is what turns 'should'
    into a measurement."""
    cells = tuple((x, l) for x in SITES for l in links)
    n = len(cells)

    def rv(P):
        return tuple(1 if any(x in g and vadd(x, l) in g for g in P) else 0
                     for (x, l) in cells)
    parts = raw_census()["parts"]
    vecs = [rv(P) for P in parts]
    sat = [i for i, v in enumerate(vecs) if sum(v) == len(SITES)]
    V = [vecs[i] for i in sat]
    strict = []
    for ia, a in enumerate(V):
        for ib, b in enumerate(V):
            ab = [a[k] + b[k] for k in range(n)]
            for ic, c in enumerate(V):
                if all(ab[k] + c[k] >= 1 for k in range(n)):
                    strict.append((sat[ia], sat[ib], sat[ic]))
    tgt = [1, 1, 2] * len(SITES)
    flat = 0
    for ia, a in enumerate(V):
        for ib, b in enumerate(V):
            ab = [a[k] + b[k] for k in range(n)]
            if any(ab[k] > tgt[k] for k in range(n)):
                continue
            for ic, c in enumerate(V):
                abc = [ab[k] + c[k] for k in range(n)]
                if any(abc[k] > tgt[k] for k in range(n)):
                    continue
                for _idd, d in enumerate(V):
                    if all(abc[k] + d[k] == tgt[k] for k in range(n)):
                        flat += 1
    return {"saturating": len(sat), "strict_triples": len(strict),
            "flat_quadruples": flat, "triples": strict}


COLLINEAR_FLAT = ("ROW", "COL", "DIA", "DIA")
COMMITTED_R4 = ("ROW", "COL", "ROW", "COL")
SEEDS_PER_ROUND_IN_WINDOW = 1


def window_schedules(flatq):
    """PAPER-21's DRIVEN WINDOW W4, reconstructed by its own constructor."""
    C = raw_census()
    parts = C["parts"]
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


# ===========================================================================
# SECTION 3.  THE HISTORY -- THE FORMAL OBJECT OF THIS UNIT
# ===========================================================================

def actor(site):
    return "G%d%d" % site


ACTORS = tuple(actor(s) for s in SITES)
ACTOR_SITE = {actor(s): s for s in SITES}


def history_of(schedule):
    """THE COMBINATORIAL HISTORY: the division events of a schedule, as
    actor-subsets, in the driver's own order -- groups in ascending order of
    their seed's site index, exactly d66's order, one arbitration per conflict
    group per round.  The driven leg of section 4 gates this against the
    committed layers event by event."""
    H = []
    for (groups, seeds) in schedule:
        order = sorted(range(len(groups)),
                       key=lambda gi: SITE_INDEX[seeds[gi]])
        for gi in order:
            H.append(frozenset(groups[gi]))
    return tuple(H)


def mask_of(F):
    m = 0
    for x in F:
        m |= 1 << SITE_INDEX[x]
    return m


def masks_of(H):
    return tuple(mask_of(F) for F in H)


def signature_blocks(H):
    """THE PARTICIPATION-SIGNATURE PARTITION: two actors share a block exactly
    when they belong to the same events, all of them.  This is the coarsest
    partition every event is a union of, and section 5's theorem identifies
    the stabilizer with its Young subgroup."""
    sig = {}
    for x in SITES:
        sig.setdefault(tuple(1 if x in F else 0 for F in H), []).append(x)
    return tuple(sorted(tuple(sorted(v)) for v in sig.values()))


def young_order(H):
    o = 1
    for b in signature_blocks(H):
        o *= math.factorial(len(b))
    return o


def young_elements(H):
    """ROUTE B: the Young subgroup itself, as explicit permutations of the
    nine actor indices -- built from the blocks, never filtered."""
    blocks = signature_blocks(H)
    idxs = [[SITE_INDEX[x] for x in b] for b in blocks]
    out = []

    def rec(k, acc):
        if k == len(idxs):
            p = [0] * NACT
            for src, dst in acc:
                p[src] = dst
            out.append(tuple(p))
            return
        for perm in permutations(idxs[k]):
            rec(k + 1, acc + list(zip(idxs[k], perm)))
    rec(0, [])
    return out


S9 = None


def s9():
    global S9
    if S9 is None:
        S9 = [tuple(p) for p in permutations(range(NACT))]
    return S9


STAB_CACHE = {}


def stab_elements(H):
    """ROUTE A: the stabilizer BY EXPLICIT FILTERING.  The empty history's
    stabilizer is S_9 itself; each further event filters the previous group.
    Nothing here knows the Young theorem."""
    key = masks_of(H)
    got = STAB_CACHE.get(key)
    if got is not None:
        return got
    if not key:
        out = s9()
    else:
        prev = stab_elements(H[:-1])
        m = key[-1]
        out = []
        for p in prev:
            im = 0
            for i in range(NACT):
                if m >> i & 1:
                    im |= 1 << p[i]
            if im == m:
                out.append(p)
    STAB_CACHE[key] = out
    return out


def crystallization(H):
    """THE CRYSTALLIZATION TIME: the earliest prefix length whose stabilizer is
    trivial.  None when the whole history leaves identity un-forced."""
    for k in range(1, len(H) + 1):
        if young_order(H[:k]) == 1:
            return k
    return None


def cycle_type(p):
    seen, out = set(), []
    for i in range(NACT):
        if i in seen:
            continue
        j, ln = i, 0
        while j not in seen:
            seen.add(j)
            j = p[j]
            ln += 1
        out.append(ln)
    return tuple(sorted(out, reverse=True))


def sorted_events(H):
    """THE EVENT SET, canonically ordered.  Comparing a history's stabilizer
    with this object's is what makes 'the stabilizer reads the SET' a
    measurement rather than a remark about the definition."""
    return tuple(sorted(H, key=lambda F: sorted(SITE_INDEX[x] for x in F)))


def reversed_rounds(schedule):
    """W-C3REV: the same schedule with each round's three groups entered in
    DESCENDING seed order -- one declared point of the within-round order
    axis, applied to a whole corpus."""
    H = []
    for (groups, seeds) in schedule:
        order = sorted(range(len(groups)),
                       key=lambda gi: SITE_INDEX[seeds[gi]], reverse=True)
        for gi in order:
            H.append(frozenset(groups[gi]))
    return tuple(H)


def order_axis(triple, parts):
    """W-ORDER: all six orderings of the three groups of each of the three
    rounds -- 6^3 histories per R = 3 triple, the order axis entire."""
    grps = [list(parts[i]) for i in triple]
    out = []
    for perms in product(permutations(range(3)), repeat=len(grps)):
        H = []
        for r in range(len(grps)):
            for gi in perms[r]:
                H.append(frozenset(grps[r][gi]))
        out.append(tuple(H))
    return out


def min_event_subset(H):
    """THE INFORMATION FLOOR, per history: the size of the smallest SUBSET of
    the events whose stabilizer is already trivial.  Two actors are separated
    by an event exactly when one belongs and the other does not, so a subset
    forces identity exactly when it meets every one of the 36 separator sets;
    the search is over subsets in increasing size and returns the first size
    that hits them all.  None when no subset does."""
    seps = []
    for a, b in combinations(range(NACT), 2):
        m = 0
        for i, F in enumerate(H):
            if (SITES[a] in F) != (SITES[b] in F):
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


def covered_cells(schedule):
    """the number of the 27 cells the schedule's summed link field reaches --
    I7-COVERING is the admissibility property the census's chart histories
    all fail."""
    tot = [0] * len(CELLS)
    for (P, _s) in schedule:
        v = round_vec(P)
        tot = [tot[k] + v[k] for k in range(len(CELLS))]
    return sum(1 for v in tot if v >= 1)


# ===========================================================================
# SECTION 4.  THE OBSERVABLES -- CARRIED FROM THE PARENTS, RE-IMPLEMENTED
# ===========================================================================

def codivision(H):
    """PAPER-19's LINK GENERATOR: the co-division incidence on the actor pair
    -- the number of division events whose footprint meets both endpoints."""
    r = [[0] * NACT for _ in range(NACT)]
    for F in H:
        idx = [SITE_INDEX[x] for x in F]
        for a in idx:
            for b in idx:
                if a != b:
                    r[a][b] += 1
    return r


def record_field(H):
    """THE RECORD n_l(x) AT THE CONSTRUCTOR'S OWN PARSE: the count of division
    events containing both the actor at site x and the actor at site x + l."""
    r = codivision(H)
    return {(x, l): r[SITE_INDEX[x]][SITE_INDEX[vadd(x, l)]]
            for x in SITES for l in I7_LINKS}


def record_rows(H):
    f = record_field(H)
    return [tuple(f[(x, l)] for l in I7_LINKS) for x in SITES]


def record_rows_links(H, links):
    """the record read through an ALTERNATIVE link declaration (W-GAUGE)."""
    r = codivision(H)
    return [tuple(r[SITE_INDEX[x]][SITE_INDEX[vadd(x, l)]] for l in links)
            for x in SITES]


def orbit_constant(vals, blocks):
    """#87: the predicate is taken PER BLOCK on that block's own values."""
    for b in blocks:
        if len({vals[SITE_INDEX[x]] for x in b}) > 1:
            return False
    return True


AUT_CACHE = {}


def aut_codivision(H, count_only=True):
    """|Aut| of the co-division relation, by exhaustive backtracking on the
    weighted graph.  THE CONSTANT-WEIGHT SHORTCUT is a machine-checked
    forcing, not a waiver: when every off-diagonal weight is equal every
    permutation is an automorphism, and G-AUT-SHORTCUT enumerates one such
    object explicitly to confirm the closed value."""
    key = masks_of(H)
    if count_only and key in AUT_CACHE:
        return AUT_CACHE[key]
    r = codivision(H)
    offs = {r[a][b] for a in range(NACT) for b in range(NACT) if a != b}
    if count_only and len(offs) == 1:
        AUT_CACHE[key] = math.factorial(NACT)
        return AUT_CACHE[key]
    phi = [-1] * NACT
    used = [False] * NACT
    box = [0]
    out = []

    def bt(k):
        if k == NACT:
            box[0] += 1
            if not count_only:
                out.append(tuple(phi))
            return
        for x in range(NACT):
            if used[x]:
                continue
            ok = True
            for j in range(k):
                if r[k][j] != r[x][phi[j]] or r[j][k] != r[phi[j]][x]:
                    ok = False
                    break
            if ok:
                phi[k] = x
                used[x] = True
                bt(k + 1)
                used[x] = False
                phi[k] = -1
    bt(0)
    if count_only:
        AUT_CACHE[key] = box[0]
        return box[0]
    return out


def count_field_at(H, assign, labelperm, orient, rel=None):
    """PAPER-19's induced count field s : X x L -> Z, re-implemented.  `assign`
    maps an actor index to a site; `labelperm` permutes the declared link
    labels; `orient` flips the link direction.  `rel` is the co-division
    matrix when the caller already holds it, so the exhaustive sweep over a
    stabilizer never rebuilds it."""
    r = codivision(H) if rel is None else rel
    inv = {assign[u]: u for u in range(NACT)}
    out = {}
    for x in SITES:
        for i, lk in enumerate(I7_LINKS):
            lk2 = I7_LINKS[labelperm[i]]
            step = vmul(2, lk2) if orient else lk2
            y = vadd(x, step)
            out[(x, lk)] = r[inv[x]][inv[y]] if inv[x] != inv[y] else 0
    return tuple(out[(x, lk)] for x in SITES for lk in I7_LINKS)


IDENT_ASSIGN = {i: SITES[i] for i in range(NACT)}


def compose_assign(assign, sigma):
    """the parse READ THROUGH a relabelling: actor u is read at the site the
    parse gives to sigma(u)."""
    return {u: assign[sigma[u]] for u in range(NACT)}


# ---- W-PARSE: the twelve declared readings of the weld dictionary ----------
# The dictionary's fiber is (link-label permutation, orientation): 3! x 2.  The
# CELL PAIRS a parse reads are a function of the parse alone and not of the
# history, so they are built once and the sweep over the stabilizer is a walk
# over integer index pairs -- the same arithmetic as `count_field_at`, at the
# cost the twelve-fold sweep needs.
PARSES = tuple((lp, ori) for lp in permutations(range(len(I7_LINKS)))
               for ori in (False, True))


def parse_pairs(labelperm, orient):
    out = []
    for x in SITES:
        for i in range(len(I7_LINKS)):
            lk2 = I7_LINKS[labelperm[i]]
            step = vmul(2, lk2) if orient else lk2
            out.append((SITE_INDEX[x], SITE_INDEX[vadd(x, step)]))
    return tuple(out)


PARSE_PAIRS = tuple(parse_pairs(lp, ori) for lp, ori in PARSES)
IDENT_PARSE = tuple(range(NACT))


def inverse_perm(p):
    inv = [0] * NACT
    for i in range(NACT):
        inv[p[i]] = i
    return tuple(inv)


def field_through(rel, pairs, inv):
    """the count field a parse reads, with the actor->site assignment
    precomposed by a relabelling: `inv` is the inverse permutation, so entry
    (x, l) reads the co-division count of the actors the transported parse
    puts at x and at x + l."""
    return tuple(rel[inv[a]][inv[b]] if inv[a] != inv[b] else 0
                 for a, b in pairs)


def record_pairs():
    return tuple((SITE_INDEX[x], SITE_INDEX[vadd(x, l)])
                 for x in SITES for l in I7_LINKS)


RECORD_PAIRS = record_pairs()


# ---- paper-20's coupled walk, re-implemented over Z[w] ---------------------

def zwmul(z1, z2):
    a, b = z1
    c, d = z2
    return (a * c - b * d, a * d + b * c - b * d)


def absq(z):
    """|a + b w|^2 = a^2 - a b + b^2, a RATIONAL INTEGER -- which is why the
    Born weights of this walk are exact integers over a power of three."""
    a, b = z
    return a * a - a * b + b * b


ZW0 = (0, 0)
ZW1 = (1, 0)
WPOW = ((1, 0), (0, 1), (-1, -1))
GN = tuple(tuple(2 if i != j else -1 for j in range(3)) for i in range(3))
DIM = len(CELLS)


def cell_index(si, li):
    return si * len(I7_LINKS) + li


SHIFT_T = tuple(cell_index(SITE_INDEX[vadd(SITES[s], I7_LINKS[i])], i)
                for s in range(NACT) for i in range(len(I7_LINKS)))
WALK_DEPTH = 5


COIN_ORDERS = ("G.D", "D.G")


def menus_from_field(n, depth=WALK_DEPTH, coin_order="G.D"):
    """PAPER-20's coupled step, from the S_9-SYMMETRIC START, at a DECLARED
    coin order (W-COIN).  The coin is site-block-diagonal, C(x) = G . D(x) or
    C(x) = D(x) . G with D(x) = diag(w^{n_l(x)}); the Born menu is the
    post-coin weight |(C psi)(x, l)|^2.  Starting from the all-ones state
    means every asymmetry in the published menu is carried by the record and
    by the shift, never by the start.  The record field `n` is passed in, so
    the same walk serves the plain reading and the TRANSPORTED reading."""
    psi = [ZW1] * DIM
    menus = []
    gd = coin_order == "G.D"
    for _t in range(depth):
        post = [ZW0] * DIM
        for s in range(NACT):
            b = s * len(I7_LINKS)
            if gd:
                src = [zwmul(psi[b + j], WPOW[n[b + j] % 3]) for j in range(3)]
                for i in range(3):
                    a = c = 0
                    for j in range(3):
                        g = GN[i][j]
                        a += g * src[j][0]
                        c += g * src[j][1]
                    post[b + i] = (a, c)
            else:
                for i in range(3):
                    a = c = 0
                    for j in range(3):
                        g = GN[i][j]
                        a += g * psi[b + j][0]
                        c += g * psi[b + j][1]
                    post[b + i] = zwmul((a, c), WPOW[n[b + i] % 3])
        menus.append(tuple(absq(z) for z in post))
        nxt = [ZW0] * DIM
        for m in range(DIM):
            nxt[SHIFT_T[m]] = post[m]
        psi = nxt
    return menus


def record_vector(H, rel=None):
    r = codivision(H) if rel is None else rel
    return [r[a][b] for a, b in RECORD_PAIRS]


def born_menus(H, depth=WALK_DEPTH, coin_order="G.D"):
    return menus_from_field(record_vector(H), depth, coin_order)


BORN_CACHE = {}


def born_rows(H, t, coin_order="G.D"):
    key = (masks_of(H), coin_order)
    if key not in BORN_CACHE:
        BORN_CACHE[key] = born_menus(H, WALK_DEPTH, coin_order)
    J = BORN_CACHE[key][t - 1]
    return [tuple(J[s * len(I7_LINKS) + i] for i in range(len(I7_LINKS)))
            for s in range(NACT)]


def translations():
    return {d: tuple(SITE_INDEX[vadd(SITES[i], d)] for i in range(NACT))
            for d in SITES}


TRANSL = translations()
TRANSL_SET = set(TRANSL.values())


def walk_commutes(H, sigma):
    """sigma is a symmetry of the coupled step exactly when it commutes with
    the SHIFT and with the COIN.  Both legs are tested here on the operators
    themselves -- cell by cell for the shift, site row by site row for the
    coin -- and never inferred from the closed criterion section 6 proves."""
    shift_ok = all(SITE_INDEX[vadd(SITES[sigma[SITE_INDEX[x]]], l)]
                   == sigma[SITE_INDEX[vadd(x, l)]]
                   for x in SITES for l in I7_LINKS)
    rows = record_rows(H)
    coin_ok = all(rows[sigma[s]] == rows[s] for s in range(NACT))
    return shift_ok, coin_ok


# ===========================================================================
# SECTION 5.  THE DRIVEN LEG -- THE COMMITTED LAYERS, DRIVEN DIRECTLY
# ===========================================================================

class Grammar:
    """the committed v10 layers, loaded as SINGLE SOURCES.  Nothing in this
    file re-implements an admissibility rule; the menu IS d42b1's."""

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
        self.extracted = {}
        g60 = self._extract("v10/code/d60_crystal_exact.py", texts, "d60",
                            {"candidates_for": self.candidates_for,
                             "event_poset": ns["event_poset"], "V0": self.V0})
        self.B = g60["B"]
        g66 = self._extract("v10/code/d66_arbitration_crystal_exact.py", texts,
                            "d66",
                            {"B": self.B, "dl": g60["dl"], "vname": self.vname,
                             "V0": self.V0,
                             "candidates_for": self.candidates_for})
        self.d66_names = sorted(g66)
        self.slice_exit_free = ("sys.exit" not in self.slice_text
                                and no_exit(ast.parse(self.slice_text).body))
        self.bodies_exit_free = all(no_exit(v)
                                    for v in self.extracted.values())

    def candidates_for(self, hist, inits):
        key = (tuple(hist), tuple(inits))
        got = self.memo.get(key)
        if got is None:
            got = self.raw_candidates_for(list(hist), tuple(inits))
            self.memo[key] = got
        return got

    def _extract(self, rel, texts, marker, extra):
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


def drive(G, schedule, drop_supply=None):
    """d66's CONFLICT-GRID cycle with the grouping and the seed taken from the
    schedule: conflict-supply deliveries from the group's seed, g proposals,
    one arbitration won by the seed.  Every event is specified by its FULL
    TUPLE and taken from the layer's own menu, so the builder's tie-break is
    never consulted (the #160 immunity, gated at G-MAXHITS-IMMUNITY)."""
    b = G.B(ACTORS)
    cur = {a: G.V0 for a in ACTORS}
    dropped = 0
    for (groups, seeds) in schedule:
        order = sorted(range(len(groups)),
                       key=lambda gi: SITE_INDEX[seeds[gi]])
        for gi in order:
            grp = [actor(s) for s in sorted(groups[gi])]
            sd = actor(seeds[gi])
            base = cur[sd]
            for a in grp:
                if a == sd or cur[a] == base:
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
            b.pick((sd,), lambda z, e=("r", sd, ckey, wkey): z == e,
                   "arbitrate %s" % sd)
            if b.refusal:
                return b
            v = G.vname(base, wkey, sd)
            for a in grp:
                cur[a] = v
    return b


def driven_history(G, schedule):
    """THE DRIVEN HISTORY: the register footprints of the division events, cut
    to the nine actor objects, in the order the layer produced them."""
    b = drive(G, schedule)
    divs = [e for e in b.H if e[0] == "r"]
    foot = [frozenset(ACTOR_SITE[r] for r in G.regs_of(e) if r in ACTOR_SITE)
            for e in divs]
    return tuple(foot), b


def regs_of_footprint_rule(text):
    """THE STRUCTURAL LEG.  d42b1's `regs_of` is parsed and the arbitration
    branch is read off its own source: the returned register set is the union
    of the PROPOSER names in the conflict key with one derived value name.
    Cut to the nine actor objects, that is the conflict group exactly."""
    tree = ast.parse(text)
    fn = [n for n in ast.walk(tree)
          if isinstance(n, ast.FunctionDef) and n.name == "regs_of"][0]
    src = ast.unparse(fn)
    props = "props = {t[0] for t in op[2]}" in src.replace("\n", " ")
    tail = "return frozenset(props | {vname(base, op[3], op[1])})" in src
    return {"has_proposer_union": props, "returns_props_plus_vname": tail,
            "source": norm(src.split("props =")[-1])[:200]}


# ===========================================================================
# SECTION 6.  THE RUN
# ===========================================================================

LD = None
SEAL = None


def full_run(break_anchor=None, paper_text=None, paper_rel=PAPER_REL,
             write=True):
    global LD, SEAL
    LD = Ledger()
    SEAL = Seal()
    R = {"schema": SCHEMA}
    say("=" * 78)
    say("AID (paper-33) -- ARE ACTORS DERIVED?  THE IDENTITY-RECONSTRUCTION "
        "CENSUS")
    say("=" * 78)

    # ---- SECTION 1.  PROVENANCE -------------------------------------------
    say()
    say("SECTION 1.  PROVENANCE -- THE PINNED SOURCES")
    texts, shas = {}, {}
    bad = []
    for sid, rel, sha, _why in SOURCES:
        raw = read_bytes(rel)
        got = hashlib.sha256(raw).hexdigest()[:12]
        if break_anchor == sid:
            got = "0" * 12
        shas[sid] = got
        if got != sha:
            bad.append("%s %s != %s" % (sid, got, sha))
        texts[rel] = raw.decode("utf-8")
    LD.gate("G-PROVENANCE",
            "THE %d RUNTIME SOURCES ARE PINNED BY CONTENT (#46/#91).  Every "
            "source is read as bytes, its sha256-12 recomputed from those "
            "bytes and compared with this unit's frozen declaration; the "
            "declaration also names the COMMIT each pinned digest belongs to, "
            "so a worktree byte that is not the committed object cannot be "
            "read.  One mismatch and the run dies here"
            % len(SOURCES),
            not bad, "mismatches %s" % (bad or "none"))
    R["provenance"] = {
        "sources": [{"id": s[0], "path": s[1], "sha256_12": shas[s[0]],
                     "why": s[3]} for s in SOURCES],
        "commits": {"A-PIN": "f1e9fbf", "A-P19": "559e162",
                    "A-P21": "7d675c1", "A-P20": "1196ad6",
                    "A-D42B1": "f1e9fbf"},
        "paper_under_test": paper_rel,
        "no_subprocess": True,
    }
    SEAL.take("SEAL-SCHEMA", R)
    SEAL.take("SEAL-PROVENANCE", R)

    # ---- the #62 verbatim anchors -----------------------------------------
    vrows, vbad = [], []
    consumers = set()
    for vid, sid, quote, gate in VERBATIM:
        rel = [s[1] for s in SOURCES if s[0] == sid][0]
        hit = match_needle(texts[rel], quote)
        if mut("MUT-VERBATIM") and vid == "V01":
            hit = False
        vrows.append({"id": vid, "source": sid, "consumer_gate": gate,
                      "quote": quote, "found": hit})
        consumers.add(gate)
        if not hit:
            vbad.append(vid)
    LD.gate("G-VERBATIM",
            "QUOTE FIDELITY (#62, as amended).  Every sentence this unit "
            "quotes from a parent is matched against that parent's committed "
            "bytes under the #125 normalisation with a %d-character floor, "
            "and each anchor names the CONSUMER GATE that reads it -- %d "
            "anchors over %d consumer gates, none of them a label"
            % (NEEDLE_FLOOR, len(VERBATIM), len(consumers)),
            not vbad, "anchors %d, misses %s" % (len(vrows), vbad or "none"))
    R["verbatim_anchors"] = vrows
    SEAL.take("SEAL-VERBATIM", R)
    reg(len(VERBATIM), len(consumers), NEEDLE_FLOOR)

    # ---- the declared windows ---------------------------------------------
    R["windows"] = [{"name": w[0], "entire": w[1], "declaration": w[2]}
                    for w in WINDOW_DECL]
    n_entire = sum(1 for w in WINDOW_DECL if w[1])
    LD.gate("G-WINDOWS-DISCLOSED",
            "EVERY WINDOW IS DECLARED IN-STRING AND LICENSED (section 15).  "
            "The %d declarations below are published in the receipt, in the "
            "head and in the paper; %d of them are ENTIRE classes and carry "
            "no sampling at all, and each of the other %d names the "
            "property that licenses it.  The ENTIRE count is counted from the "
            "declaration and never typed"
            % (len(WINDOW_DECL), n_entire, len(WINDOW_DECL) - n_entire),
            pick("MUT-WINDOW", len({w[0] for w in WINDOW_DECL}),
                 len(WINDOW_DECL) - 1) == len(WINDOW_DECL)
            and all(len(w[2]) > 80 for w in WINDOW_DECL)
            and 0 < n_entire < len(WINDOW_DECL),
            "windows %d, entire %d, all named and non-trivial"
            % (len(WINDOW_DECL), n_entire))
    SEAL.take("SEAL-WINDOWS", R)
    reg(len(WINDOW_DECL), n_entire, len(WINDOW_DECL) - n_entire)

    # ---- SECTION 2.  THE SUBSTRATE ----------------------------------------
    say()
    say("SECTION 2.  THE ARENA AND THE COMBINATORIAL SUBSTRATE")
    C = raw_census()
    nparts = len(C["parts"])
    nsat = len(C["sat"])
    # the closed form, an independent route: 9!/(3!^3 3!) partitions
    closed = (math.factorial(9) // (math.factorial(3) ** 3
                                    // 1 * math.factorial(3)))
    strict = strict_triples()
    flatq = flat_quadruples()
    W, WMETA = window_schedules(flatq)
    p19 = json.loads(texts["v14/code/r3_weld_receipt.json"])
    p21 = json.loads(texts["v14/code/r4dec_receipt.json"])
    p20 = json.loads(texts["v14/code/coupling_receipt.json"])
    back = {
        "partitions": (nparts, p21["counts"]["partitions"]),
        "saturating": (nsat, p21["counts"]["saturating"]),
        "strict_triples": (pick("MUT-BACKVAL", len(strict), len(strict) - 1),
                           p19["counts"]["i7_strict_triples"]),
        "strict_triples_p21": (len(strict), p21["counts"]["back_r3_strict"]),
        "flat_quadruples": (len(flatq), p21["counts"]["flat_quadruples"]),
        "window": (len(W), p21["counts"]["window"]),
        "divisions_r3": (len(history_of(((CLASSES["ROW"], DIAG_SEED),) * 3)),
                         p19["arena"]["divisions"]),
        "divisions_r4": (len(history_of(W[0])),
                         p21["driven"]["divisions_per_record"]),
        "r6_witnesses": (len(strict) ** 2,
                         p21["split"]["r6_door"]["ordered_witnesses"]),
    }
    off = sorted(k for k, (a, b) in back.items() if a != b)
    LD.gate("G-BACK-VALIDATION",
            "THE SUBSTRATE IS RECOMPUTED HERE AND MEASURED AGAINST THE "
            "PARENTS' COMMITTED RECEIPTS, OBJECT BY OBJECT (#87).  Each of "
            "the %d rows is an independently computed quantity of this run "
            "compared with the value the parent's own receipt bytes carry: "
            "%d groupings, %d saturating, %d I7-STRICT triples at R = 3, "
            "%d G-FLAT quadruples, a %d-schedule window, %d and %d division "
            "events per R = 3 and R = 4 record, and %s ordered R = 6 "
            "concatenations.  A single disagreement kills the run"
            % (len(back), nparts, nsat, len(strict), len(flatq), len(W),
               back["divisions_r3"][0], back["divisions_r4"][0],
               com(len(strict) ** 2)),
            not off, "rows %d, disagreements %s" % (len(back), off or "none"))
    LD.gate("G-PARTITION-ROUTE",
            "THE ROUND FAMILY, COUNTED TWICE BY ROUTES THAT SHARE NO CODE.  "
            "The recursive enumeration returns %d groupings; the closed form "
            "9!/((3!)^3 . 3!) returns %d.  The enumeration is what everything "
            "downstream uses" % (nparts, closed),
            pick("MUT-PARTITION", nparts, nparts + 1) == closed,
            "enumerated %d, closed form %d" % (nparts, closed))
    # ---- W-GAUGE: the link declaration is a gauge choice --------------------
    gsub = gauge_substrate(GAUGE_LINKS)
    gC1 = [history_of(tuple((C["parts"][i],
                             canon_transversals(C["parts"][i])[0])
                            for i in t)) for t in gsub["triples"]]
    gpre = set()
    for H in gC1:
        for k in range(1, len(H) + 1):
            gpre.add(H[:k])
    gntp = [P for P in gpre if young_order(P) > 1]
    gblind = sum(1 for P in gntp
                 if orbit_constant(record_rows_links(P, GAUGE_LINKS),
                                   signature_blocks(P)))
    dC1 = [history_of(tuple((C["parts"][i],
                             canon_transversals(C["parts"][i])[0])
                            for i in t)) for t in strict]
    dpre = set()
    for H in dC1:
        for k in range(1, len(H) + 1):
            dpre.add(H[:k])
    dntp = [P for P in dpre if young_order(P) > 1]
    dblind = sum(1 for P in dntp
                 if orbit_constant(record_rows(P), signature_blocks(P)))
    gauge = {
        "declared_links": [list(l) for l in I7_LINKS],
        "alternative_links": [list(l) for l in GAUGE_LINKS],
        "saturating": (nsat, gsub["saturating"]),
        "strict_triples": (len(strict), gsub["strict_triples"]),
        "flat_quadruples": (len(flatq), gsub["flat_quadruples"]),
        "crystallization_R3": (sorted({crystallization(H) for H in dC1}),
                               sorted({crystallization(H) for H in gC1})),
        "nontrivial_R3_prefixes": (len(dntp), len(gntp)),
        "record_blind_R3_prefixes": (dblind, gblind),
    }
    goff = sorted(k for k, v in gauge.items()
                  if isinstance(v, tuple) and v[0] != v[1])
    LD.gate("G-GAUGE-DECLARATION",
            "WHICH THREE OF THE FOUR PARALLEL CLASSES ARE DECLARED IS A GAUGE "
            "CHOICE, MEASURED AND NOT ARGUED (W-GAUGE).  The whole R = 3 "
            "substrate is rebuilt with ANT in place of DIA and the census "
            "re-run on it: %d saturating, %d I7-STRICT triples, %d G-FLAT "
            "quadruples, crystallization %s, %d nontrivial R = 3 prefixes and "
            "%d of them record-blind -- entry for entry the values the "
            "declared triple returns.  PGL(2, 3) acts on the four directions, "
            "so this is what that action predicts; nothing in the census is "
            "an artifact of the declaration"
            % (gsub["saturating"], gsub["strict_triples"],
               gsub["flat_quadruples"],
               sorted({crystallization(H) for H in gC1}), len(gntp), gblind),
            not pick("MUT-GAUGE", goff, ["FORGED"]),
            "rows %d, disagreements %s"
            % (len(gauge) - 2, goff or "none"))
    R["substrate"] = {
        "sites": len(SITES), "links": len(I7_LINKS), "cells": len(CELLS),
        "partitions": nparts, "partitions_closed_form": closed,
        "saturating": nsat, "strict_triples": len(strict),
        "flat_quadruples": len(flatq), "window": len(W),
        "window_strata": {k: v for k, v in
                          sorted(Counter(WMETA.values()).items())},
        "back_validation": {k: {"here": a, "parent": b}
                            for k, (a, b) in sorted(back.items())},
        "gauge_declaration": {
            k: ({"declared": v[0], "alternative": v[1]}
                if isinstance(v, tuple) else v)
            for k, v in sorted(gauge.items())},
    }
    SEAL.take("SEAL-SUBSTRATE", R)
    reg(len(SITES), len(I7_LINKS), len(CELLS), nparts, nsat, len(strict),
        len(flatq), len(W), closed, len(strict) ** 2)
    for v in R["substrate"]["window_strata"].values():
        reg(v)
    reg(len(gntp), gblind, gsub["saturating"], gsub["strict_triples"],
        gsub["flat_quadruples"])

    # ---- SECTION 3.  THE CORPORA ------------------------------------------
    say()
    say("SECTION 3.  THE THREE COMMITTED CORPORA")
    parts = C["parts"]
    c1_sched = [tuple((parts[i], canon_transversals(parts[i])[0])
                      for i in t) for t in strict]
    C1 = [history_of(s) for s in c1_sched]
    C1FAN = []
    for t in strict:
        T = [parts[i] for i in t]
        for ks in product(range(3), repeat=3):
            C1FAN.append(history_of(tuple((T[r], canon_transversals(T[r])[ks[r]])
                                          for r in range(3))))
    c2_sched = [tuple((parts[i], canon_transversals(parts[i])[0])
                      for i in (t1 + t2)) for t1 in strict for t2 in strict]
    C2 = [history_of(s) for s in c2_sched]
    C3 = [history_of(s) for s in W]
    CORPORA = [("C1-R3-TRIPLES", C1, c1_sched),
               ("C2-R6-CONCATENATIONS", C2, c2_sched),
               ("C3-R4-WINDOW", C3, W)]
    shapes = {nm: sorted(Counter(len(H) for H in HS).items())
              for nm, HS, _s in CORPORA}
    ev = {nm: sorted({len(F) for H in HS for F in H})
          for nm, HS, _s in CORPORA}
    LD.gate("G-CORPORA-SHAPE",
            "EVERY HISTORY IN EVERY CORPUS HAS THE SHAPE THE CONSTRUCTOR "
            "FORCES, PER OBJECT.  A schedule of R rounds carries exactly 3R "
            "division events -- one arbitration per conflict group per "
            "round -- and every event is a three-actor subset: %s at %d "
            "histories, %s at %s, %s at %d.  The event sizes measured are %s"
            % (shapes["C1-R3-TRIPLES"], len(C1), shapes["C2-R6-CONCATENATIONS"],
               com(len(C2)), shapes["C3-R4-WINDOW"], len(C3),
               sorted({v for vs in ev.values() for v in vs})),
            pick("MUT-CORPUS-SHAPE",
                 all(len(H) == 3 * (len(s)) for nm, HS, SS in CORPORA
                     for H, s in zip(HS, SS)), False)
            and all(len(F) == 3 for nm, HS, _s in CORPORA for H in HS
                    for F in H),
            "shapes %s; event sizes %s"
            % (shapes, {k: v for k, v in sorted(ev.items())}))
    LD.gate("G-EVENT-SHAPE",
            "THE EVENT IS THE CONFLICT GROUP AND THE HISTORY IS ORDERED.  "
            "Within a round the three groups enter in ascending order of "
            "their seed's site index -- d66's own order -- so the history is "
            "a SEQUENCE and not a set; the %d histories of the seed fan "
            "W-C1FAN realise %d distinct orderings of the same %d event sets"
            % (len(C1FAN), len({H for H in C1FAN}),
               len({frozenset(H) for H in C1FAN})),
            pick("MUT-ORDER", len({H for H in C1FAN}), 0) > len(C1)
            and len({frozenset(H) for H in C1FAN}) < len({H for H in C1FAN}),
            "fan histories %d, distinct sequences %d, distinct event sets %d"
            % (len(C1FAN), len({H for H in C1FAN}),
               len({frozenset(H) for H in C1FAN})))
    # ---- THE TWO PREFIX FAMILIES, NAMED (#288/#289/#292 convergent M) ------
    # A prefix count and a DISTINCT prefix count only belong in one sentence
    # when they are taken over the same family.  Both families are computed
    # and published here, and every sentence downstream names the one it uses.
    fam_primary = set()
    fam_declared = set()
    n_primary = n_declared = 0
    for _nm, HS, _s in CORPORA:
        for H in HS:
            for k in range(1, len(H) + 1):
                fam_primary.add(H[:k])
                fam_declared.add(H[:k])
                n_primary += 1
                n_declared += 1
    for H in C1FAN:
        for k in range(1, len(H) + 1):
            fam_declared.add(H[:k])
            n_declared += 1
    FAMILIES = {
        "THREE-PRIMARY": {"corpora": ["C1-R3-TRIPLES", "C2-R6-CONCATENATIONS",
                                      "C3-R4-WINDOW"],
                          "prefix_objects": n_primary,
                          "distinct_prefixes": len(fam_primary)},
        "FOUR-DECLARED": {"corpora": ["C1-R3-TRIPLES", "C1FAN-SEED-FAN",
                                      "C2-R6-CONCATENATIONS", "C3-R4-WINDOW"],
                          "prefix_objects": n_declared,
                          "distinct_prefixes": len(fam_declared)},
    }
    R["corpora"] = {
        "C1-R3-TRIPLES": {"histories": len(C1), "events_per_history": 9,
                          "window": "W-C1"},
        "C1FAN-SEED-FAN": {"histories": len(C1FAN), "events_per_history": 9,
                           "distinct_sequences": len({H for H in C1FAN}),
                           "distinct_event_sets":
                               len({frozenset(H) for H in C1FAN}),
                           "window": "W-C1FAN"},
        "C2-R6-CONCATENATIONS": {"histories": len(C2),
                                 "events_per_history": 18, "window": "W-C2"},
        "C3-R4-WINDOW": {"histories": len(C3), "events_per_history": 12,
                         "window": "W-C3",
                         "strata": R["substrate"]["window_strata"]},
        "histories_total": len(C1) + len(C2) + len(C3),
        "independent_histories": len(C1) + len(C3),
        "prefix_objects_by_family": FAMILIES,
        "prefix_objects_total": n_primary,
        "prefix_objects_total_basis": "THREE-PRIMARY",
    }
    LD.gate("G-PREFIX-FAMILIES",
            "A PREFIX TOTAL AND A DISTINCT-PREFIX TOTAL BELONG IN ONE "
            "SENTENCE ONLY WHEN THEY NAME ONE FAMILY (#288/#289/#292, the "
            "convergent finding).  Both families are computed here and "
            "published with their corpus lists: the THREE PRIMARY corpora "
            "carry %s prefix objects of which %s are distinct, the FOUR "
            "DECLARED corpora %s of which %s.  The seed fan alone contributes "
            "%s distinct prefixes that are prefixes of no history the primary "
            "total counts, which is exactly why the two numbers may not be "
            "joined.  The arithmetic is gated per family: distinct <= objects"
            % (com(n_primary), com(len(fam_primary)), com(n_declared),
               com(len(fam_declared)),
               com(len(fam_declared) - len(fam_primary))),
            pick("MUT-FAMILY", len(fam_primary), len(fam_declared))
            != len(fam_declared)
            and all(f["distinct_prefixes"] <= f["prefix_objects"]
                    for f in FAMILIES.values())
            and fam_primary < fam_declared,
            "primary %d/%d, declared %d/%d, fan-only distinct %d"
            % (len(fam_primary), n_primary, len(fam_declared), n_declared,
               len(fam_declared) - len(fam_primary)))
    SEAL.take("SEAL-CORPORA", R)
    reg(len(C1), len(C2), len(C3), len(C1FAN), len({H for H in C1FAN}),
        len({frozenset(H) for H in C1FAN}),
        R["corpora"]["histories_total"], R["corpora"]["independent_histories"],
        n_primary, n_declared, len(fam_primary), len(fam_declared),
        len(fam_declared) - len(fam_primary))

    # ---- SECTION 4.  THE DRIVEN LEG ---------------------------------------
    say()
    say("SECTION 4.  THE DRIVEN LEG -- THE COMMITTED LAYERS, DRIVEN DIRECTLY")
    G = Grammar(texts)
    rule = regs_of_footprint_rule(texts["v10/code/d42b1_transport_exact.py"])
    LD.gate("G-FOOTPRINT-RULE",
            "THE FOOTPRINT RULE IS READ OFF THE COMMITTED GRAMMAR'S OWN "
            "SOURCE, NOT ASSUMED.  d42b1's `regs_of` is parsed and its "
            "arbitration branch returns the union of the PROPOSER names in "
            "the conflict key with one derived value name; the proposers of "
            "an arbitration are exactly the conflict group, and paper-19's "
            "`record_of` cuts the value name away by restricting to the nine "
            "actor objects.  So the driven footprint IS the group -- a "
            "structural leg, gated before any drive runs",
            pick("MUT-RULE", rule["has_proposer_union"], False)
            and rule["returns_props_plus_vname"],
            "proposer union %s, props+vname return %s"
            % (rule["has_proposer_union"], rule["returns_props_plus_vname"]))
    ctrl = [tuple((CLASSES[k], canon_transversals(CLASSES[k])[0])
                  for k in names) for names in (COMMITTED_R4, COLLINEAR_FLAT)]
    drive_set = [("W-C1", s) for s in c1_sched[:9]]
    seen_drive = {s for _t, s in drive_set}
    for s in [w for w in W if len({P for P, _q in w}) == 1] + ctrl:
        if s not in seen_drive:
            seen_drive.add(s)
            drive_set.append(("W-C3", s))
    for s in c2_sched[:2]:
        drive_set.append(("W-C2", s))
    drows, dbad = [], []
    for tag, sch in drive_set:
        foot, b = driven_history(G, sch)
        comb = history_of(sch)
        same = foot == comb
        if mut("MUT-DRIVEN") and not drows:
            same = False
        drows.append({"window": tag, "rounds": len(sch),
                      "events": len(b.H), "divisions": len(foot),
                      "maxhits": b.maxhits, "refusal": str(b.refusal),
                      "footprints_equal_groups": same})
        if not same:
            dbad.append(tag)
    LD.gate("G-DRIVEN-EQUALS-COMBINATORIAL",
            "THE LICENSE FOR EVERY EXHAUSTIVE COLUMN, TAKEN AT THE FOOTPRINT "
            "SEQUENCE ITSELF.  For each of the %d schedules of the declared "
            "drive set W-DRIVE the committed layers are driven and the "
            "register footprints of the division events -- taken from the "
            "layer's own `regs_of` and cut to the nine actor objects -- are "
            "compared EVENT BY EVENT, IN ORDER, with the combinatorial "
            "history.  This is strictly stronger than paper-21's licence, "
            "which compared the summed link FIELD; here the sequence itself "
            "is the object" % len(drive_set),
            not dbad, "schedules %d, mismatches %s"
            % (len(drows), dbad or "none"))
    LD.gate("G-MAXHITS-IMMUNITY",
            "THE v10-LAYER TIE-BREAK IS NEVER CONSULTED (#160, as a gate).  "
            "Every event of every driven schedule is specified by its FULL "
            "TUPLE, so at most one menu candidate can match; the builder's "
            "own `maxhits` is read at every schedule and is 1 at all %d of "
            "them.  d60's `pick` breaks ties with sorted(key=repr), which is "
            "hash-seed dependent -- this unit is immune because the tie-break "
            "is unreachable, and says so rather than pricing it"
            % len(drows),
            all(pick("MUT-MAXHITS", r["maxhits"], 2) == 1 for r in drows)
            and all(r["refusal"] == "None" for r in drows),
            "maxhits %s, refusals %s"
            % (sorted({r["maxhits"] for r in drows}),
               sorted({r["refusal"] for r in drows})))
    b_ref = drive(G, tuple((CLASSES[k], canon_transversals(CLASSES[k])[0])
                           for k in COLLINEAR_FLAT), drop_supply=0)
    LD.gate("G-CTRL-REFUSED",
            "THE NEGATIVE FATE IS REACHABLE AND THE DRIVER SEES IT.  The "
            "collinear arrangement is re-driven with its FIRST conflict-supply "
            "delivery withheld; the committed layer then refuses the first "
            "proposal by an actor that does not hold the base, and the "
            "refusal is RECORDED rather than patched -- so 'no refusals' "
            "above is a measurement and not a property of the instrument",
            pick("MUT-REFUSED", b_ref.refusal, None) is not None,
            "refusal %s" % (b_ref.refusal,))
    LD.gate("G-LAYERS-CANNOT-EXIT",
            "THE COMMITTED LAYERS ENTER AS SINGLE SOURCES AND CANNOT EXIT.  "
            "d42b1's module slice is cut before its first print and carries "
            "no exit call; d60 and d66 enter through an AST extraction that "
            "keeps only function and class definitions, so no module-level "
            "statement of theirs can run and no `sys.exit` of theirs is "
            "reachable",
            pick("MUT-EXIT", G.slice_exit_free, False) and G.bodies_exit_free,
            "slice exit-free %s, extracted bodies exit-free %s"
            % (G.slice_exit_free, G.bodies_exit_free))
    R["driven"] = {
        "drive_set_size": len(drows),
        "rows": drows,
        "footprint_rule": rule,
        "mismatches": len(dbad),
        "refusal_control": str(b_ref.refusal),
        "maxhits_observed": sorted({r["maxhits"] for r in drows}),
        "event_counts": sorted({r["events"] for r in drows}),
    }
    SEAL.take("SEAL-DRIVEN", R)
    reg(len(drows))
    for r in drows:
        reg(r["events"], r["divisions"], r["maxhits"], r["rounds"])

    # ---- SECTION 5.  THE STABILIZER CENSUS --------------------------------
    say()
    say("SECTION 5.  THE STABILIZER CENSUS -- TWO ROUTES, ELEMENT BY ELEMENT")
    prefixes = {}
    for nm, HS, _s in CORPORA:
        for H in HS:
            for k in range(1, len(H) + 1):
                prefixes.setdefault(H[:k], set()).add(nm)
    for H in C1FAN:
        for k in range(1, len(H) + 1):
            prefixes.setdefault(H[:k], set()).add("C1FAN-SEED-FAN")
    ordered = sorted(prefixes, key=len)
    routes_bad = []
    for P in ordered:
        a = stab_elements(P)
        if len(a) != young_order(P):
            routes_bad.append(P)
    checked = 0
    elem_bad = []
    for P in ordered:
        if young_order(P) > 1 or len(P) <= 1:
            a = set(stab_elements(P))
            b = set(young_elements(P))
            checked += 1
            if a != b:
                elem_bad.append(P)
    nb = pick("MUT-ROUTES", len(routes_bad), 1)
    LD.gate("G-STAB-ROUTES",
            "THE STABILIZER, COMPUTED TWICE BY ROUTES THAT SHARE NO CODE AND "
            "NO LITERAL, PER OBJECT (#87).  ROUTE A filters the %s elements "
            "of S_9 explicitly, event by event, and knows nothing about "
            "signatures; ROUTE B builds the Young subgroup of the "
            "participation-signature partition and never touches S_9.  The "
            "two are compared at ORDER on all %s distinct prefixes of the "
            "four corpora and at ELEMENT SET on the %d of them where the "
            "group is nontrivial or the prefix is a single event"
            % (com(math.factorial(NACT)), com(len(ordered)), checked),
            nb == 0 and not elem_bad and set(prefixes) == fam_declared,
            "prefixes %d, order mismatches %d, element-set comparisons %d, "
            "element-set mismatches %d, family FOUR-DECLARED %s"
            % (len(ordered), nb, checked, len(elem_bad),
               set(prefixes) == fam_declared))
    NTP = [P for P in ordered if young_order(P) > 1]
    # ---- THE STABILIZER READS THE EVENT SET, NOT THE ORDER (#289 MAJOR-1) --
    set_order_bad = [P for P in ordered
                     if young_order(sorted_events(P)) != young_order(P)]
    set_elem_bad = [P for P in NTP
                    if set(stab_elements(sorted_events(P)))
                    != set(stab_elements(P))]
    LD.gate("G-STABILIZER-READS-THE-SET",
            "THE STABILIZER IS A FUNCTION OF THE EVENT SET AND NOT OF THE "
            "ORDER, MEASURED PER OBJECT (#289 MAJOR-1).  Fixing every event "
            "SETWISE is a condition taken one event at a time, so Stab(H) is "
            "the intersection of the per-event stabilizers and the sequence "
            "is not a variable it reads.  Each of the %s distinct prefixes is "
            "re-presented with its events in a canonical order that destroys "
            "the history's own: the stabilizer's ORDER agrees at every one, "
            "and on the %d nontrivial objects the two subgroups agree "
            "ELEMENT FOR ELEMENT.  The order is a real variable of this unit "
            "-- but of the crystallization TIME, which the next section "
            "measures, and never of the stabilizer"
            % (com(len(ordered)), len(NTP)),
            not pick("MUT-SETFN", set_order_bad, [0]) and not set_elem_bad,
            "prefixes %d, order changes %d, element-set changes %d"
            % (len(ordered), len(set_order_bad), len(set_elem_bad)))
    orders = Counter(young_order(P) for P in NTP)
    shapes_nt = Counter(tuple(sorted(len(b) for b in signature_blocks(P)))
                        for P in NTP)
    ctypes = Counter()
    nelem = 0
    for P in NTP:
        for p in stab_elements(P):
            ctypes[cycle_type(p)] += 1
            nelem += 1
    full = {}
    for nm, HS, _s in CORPORA + [("C1FAN-SEED-FAN", C1FAN, None)]:
        full[nm] = Counter(young_order(H) for H in HS)
    forced_hist = sum(v for nm in full for k, v in full[nm].items()
                      if k == 1 and nm != "C1FAN-SEED-FAN")
    chart_hist = sum(v for nm in full for k, v in full[nm].items()
                     if k > 1 and nm != "C1FAN-SEED-FAN")
    LD.gate("G-FORCED-PER-HISTORY",
            "FORCEDNESS IS DECIDED PER HISTORY, NEVER AS AN AGGREGATE (#87).  "
            "Each of the %s committed histories carries its own stabilizer "
            "and its own verdict: %s are FORCED (trivial stabilizer) and %d "
            "are CHART (nontrivial).  The %d chart histories all carry order "
            "%s and orbit shape %s"
            % (com(forced_hist + chart_hist), com(forced_hist), chart_hist,
               chart_hist,
               sorted({young_order(H) for nm, HS, _s in CORPORA for H in HS
                       if young_order(H) > 1}),
               sorted({tuple(sorted(len(b) for b in signature_blocks(H)))
                       for nm, HS, _s in CORPORA for H in HS
                       if young_order(H) > 1})),
            all((young_order(H) == 1) == (crystallization(H) is not None)
                for nm, HS, _s in CORPORA for H in HS)
            and pick("MUT-CHART", chart_hist, chart_hist + 1)
            == sum(1 for nm, HS, _s in CORPORA for H in HS
                   if young_order(H) > 1),
            "forced %d, chart %d, forced-iff-crystallized on all %d"
            % (forced_hist, chart_hist, forced_hist + chart_hist))
    R["stabilizer"] = {
        "s9_order": math.factorial(NACT),
        "distinct_prefixes": len(ordered),
        "route_order_mismatches": nb,
        "element_set_comparisons": checked,
        "element_set_mismatches": len(elem_bad),
        "nontrivial_distinct_prefixes": len(NTP),
        "nontrivial_orders": {str(k): v for k, v in sorted(orders.items())},
        "nontrivial_orbit_shapes": {"+".join(str(x) for x in k): v
                                    for k, v in sorted(shapes_nt.items())},
        "stabilizer_elements_over_nontrivial": nelem,
        "generator_cycle_types": {"+".join(str(x) for x in k): v
                                  for k, v in sorted(ctypes.items())},
        "cycle_types_distinct": len(ctypes),
        "full_history_orders": {nm: {str(k): v for k, v in sorted(cc.items())}
                                for nm, cc in sorted(full.items())},
        "forced_histories": forced_hist,
        "chart_histories": chart_hist,
        "set_reordering_changes": len(set_order_bad),
        "set_reordering_element_changes": len(set_elem_bad),
        "chart_orbit_shapes": sorted(
            {"+".join(str(len(b)) for b in signature_blocks(H))
             for nm, HS, _s in CORPORA for H in HS if young_order(H) > 1}),
    }
    SEAL.take("SEAL-STABILIZER", R)
    reg(len(ordered), len(NTP), nelem, forced_hist, chart_hist, checked,
        math.factorial(NACT), len(ctypes))
    for k, v in orders.items():
        reg(k, v)
    for v in shapes_nt.values():
        reg(v)

    # ---- SECTION 6.  THE CRYSTALLIZATION TIME -----------------------------
    say()
    say("SECTION 6.  THE CRYSTALLIZATION TIME")
    crys = {}
    for nm, HS, _s in CORPORA + [("C1FAN-SEED-FAN", C1FAN, None)]:
        crys[nm] = Counter(crystallization(H) for H in HS)
    never = [(nm, H, s) for nm, HS, SS in CORPORA
             for H, s in zip(HS, SS) if crystallization(H) is None]
    c1t = sorted(crys["C1-R3-TRIPLES"])
    c2t = sorted(crys["C2-R6-CONCATENATIONS"])
    fant = sorted(crys["C1FAN-SEED-FAN"])
    LD.gate("G-CRYSTALLIZATION",
            "THE CRYSTALLIZATION TIME IS MEASURED PER HISTORY AND IT IS A "
            "CONSTANT ON TWO OF THE THREE CORPORA.  Every one of the %d R = 3 "
            "triples forces identity at its FIFTH division event -- not the "
            "third, not the ninth -- and so does every one of the %s R = 6 "
            "concatenations and every one of the %s seed-fan variants; the "
            "R = 4 window is the stratified one, at %s"
            % (len(C1), com(len(C2)), com(len(C1FAN)),
               sorted((str(k), v) for k, v in crys["C3-R4-WINDOW"].items())),
            c1t == c2t == fant
            and len(c1t) == 1 and pick("MUT-CRYS", c1t[0], 4) == 5,
            "C1 %s, C2 %s, C1FAN %s, C3 %s"
            % (c1t, c2t, fant,
               sorted((str(k), v) for k, v in crys["C3-R4-WINDOW"].items())))
    # THE PREFIX LAW, per object: a concatenation's time is its first factor's
    pref_bad = [i for i in range(len(C2))
                if crystallization(C2[i]) != crystallization(C1[i // len(C1)])]
    LD.gate("G-PREFIX-LAW",
            "CRYSTALLIZATION IS A PREFIX PROPERTY, MEASURED RATHER THAN "
            "ASSUMED.  A stabilizer can only shrink as events are appended, "
            "so the time is decided by the earliest prefix that reaches "
            "triviality: each of the %s ordered concatenations crystallizes "
            "exactly when its FIRST factor does, and nothing the second "
            "factor contributes can move it.  This is why the R = 6 corpus "
            "adds %d new crystallization values and not one more"
            % (com(len(C2)), len(set(crys["C2-R6-CONCATENATIONS"])
                                 - set(crys["C1-R3-TRIPLES"]))),
            not pick("MUT-PREFIX", pref_bad, [0]),
            "concatenations %d, disagreements with the first factor %d"
            % (len(C2), len(pref_bad)))
    mono_bad = [P for P in ordered[:2000]
                if len(P) > 1 and young_order(P) > young_order(P[:-1])]
    LD.gate("G-MONOTONE",
            "THE STABILIZER NEVER GROWS.  Route A builds each prefix's group "
            "by FILTERING its predecessor's, so containment is structural; it "
            "is measured anyway on the first %d distinct prefixes in "
            "non-decreasing length order -- an appended event can only remove "
            "elements" % len(ordered[:2000]),
            not pick("MUT-MONOTONE", mono_bad, [0]),
            "prefixes checked %d, growth events %d"
            % (len(ordered[:2000]), len(mono_bad)))
    prof = Counter(tuple(young_order(H[:k]) for k in range(1, 7))
                   for H in C1)
    prof2 = Counter(tuple(young_order(H[:k]) for k in range(1, 7))
                    for H in C2)
    profile = sorted(prof)[0] if len(prof) == 1 else None
    transversal = all(len(F & G) == 1
                      for H in C1 for F in H[3:5] for G in H[:3])
    LD.gate("G-PREFIX-PROFILE",
            "THE WHOLE ROUTE TO CRYSTALLIZATION IS THE SAME AT EVERY R = 3 "
            "HISTORY, AND IT IS THE ROUTE AND NOT A GEOMETRIC ACCIDENT THAT "
            "EXPLAINS THE CONSTANT.  The stabilizer order by prefix length is "
            "%s at all %d of them and at all %s R = 6 concatenations: the "
            "first event leaves the (3, 6) Young subgroup; the second cuts it "
            "to the three-block %d; the THIRD ADDS NOTHING, because a round's "
            "last group is the complement of its first two; the fourth leaves "
            "three singletons and three pairs; the fifth splits all three "
            "pairs at once.  The mechanism is measured: each of the fourth "
            "and fifth events meets every first-round group exactly once -- "
            "they are transversals of the first round -- at every history of "
            "the corpus"
            % (str(profile), len(C1), com(len(C2)),
               profile[1] if profile else 0),
            profile is not None and len(prof2) == 1
            and sorted(prof2)[0] == profile
            and pick("MUT-PROFILE", transversal, False)
            and profile[2] == profile[1] and profile[4] == 1,
            "C1 profiles %d, C2 profiles %d, profile %s, transversal at "
            "events four and five %s"
            % (len(prof), len(prof2), profile, transversal))
    reg(*[x for x in (profile or ())])
    nev_names = sorted({"|".join(CLASS_OF.get(P, "NON-RESOLVABLE")
                                 for P, _q in s) for _nm, _H, s in never})
    LD.gate("G-NEVER-CRYSTALLIZING",
            "THE HISTORIES THAT NEVER FORCE IDENTITY ARE CHARACTERISED, NOT "
            "MERELY COUNTED.  Exactly %d of the %s committed histories leave "
            "identity un-forced to the last event, and they are precisely the "
            "CONSTANT-CLASS quadruples %s: a schedule that repeats one "
            "parallel class every round can never separate two sites that lie "
            "on a common line of that class, so the three lines survive as "
            "orbits and the stabilizer stays at order %d"
            % (len(never), com(forced_hist + chart_hist), nev_names,
               young_order(never[0][1]) if never else 0),
            len(never) == chart_hist
            and all(len({P for P, _q in s}) == 1 for _nm, _H, s in never)
            and pick("MUT-NEVER", len(nev_names), len(nev_names) + 1)
            == len(CLASS_NAMES),
            "never-crystallizing %d, arrangements %s" % (len(never), nev_names))
    # ---- W-ORDER: the full within-round order axis, entire (#289 MINOR-2) --
    axis_t = Counter()
    axis_p = Counter()
    n_axis = 0
    for t in strict:
        for H in order_axis(t, parts):
            n_axis += 1
            axis_t[crystallization(H)] += 1
            axis_p[tuple(young_order(H[:k]) for k in range(1, 7))] += 1
    LD.gate("G-ORDER-AXIS",
            "THE CONSTANT SURVIVES THE WHOLE ORDER AXIS, NOT ONLY THE "
            "DECLARED SEED MENU (W-ORDER, ENTIRE).  The committed constructor "
            "enters a round's three groups in ascending seed order and the "
            "seed fan realises some of the other orderings; this window "
            "realises ALL of them -- every one of the six orderings of every "
            "one of the three rounds at every one of the %d triples, %s "
            "histories.  The crystallization time is %s at every one and the "
            "prefix profile %s is the UNIQUE profile there, so the constant "
            "is order-independent and the fan is corroborative rather than "
            "load-bearing"
            % (len(C1), com(n_axis), sorted(axis_t), str(sorted(axis_p)[0]),),
            pick("MUT-ORDERAXIS", len(axis_t), 2) == 1 and len(axis_p) == 1
            and sorted(axis_t)[0] == c1t[0]
            and sorted(axis_p)[0] == profile
            and n_axis == len(C1) * math.factorial(3) ** 3,
            "histories %s, distinct times %s, distinct profiles %d"
            % (com(n_axis), sorted(axis_t), len(axis_p)))
    # ---- THE INFORMATION FLOOR against the schedule's redundant event ------
    floor_bound = math.ceil(math.log2(NACT))
    floor_c1 = Counter(min_event_subset(H) for H in C1)
    forced_c3 = [H for H in C3 if young_order(H) == 1]
    floor_c3 = Counter(min_event_subset(H) for H in forced_c3)
    redundant = sum(1 for H in C1
                    if young_order(H[:2] + H[3:]) == young_order(H))
    moved = Counter(crystallization(H[:2] + H[3:] + (H[2],)) for H in C1)
    LD.gate("G-INFORMATION-FLOOR",
            "FOUR IS A COUNTING THEOREM AND FIVE IS A SCHEDULING FACT, AND "
            "THE TWO ARE DIFFERENT OBJECTS (#288 MAJOR-7).  Nine actors need "
            "distinct binary participation signatures and k events supply at "
            "most 2^k of them, so no history can force identity on fewer than "
            "ceil(log2 %d) = %d events.  The floor is ATTAINED: the smallest "
            "SUBSET of events with trivial stabilizer has size %s at all %d "
            "R = 3 histories and %s at all %d forced R = 4 histories.  The "
            "fifth POSITION is the schedule's, not information's: round one's "
            "third event is redundant at %d of %d -- a round's last group is "
            "the complement of its first two -- and moving it to the end of "
            "the sequence gives crystallization %s at all %d"
            % (NACT, floor_bound, sorted(floor_c1), len(C1), sorted(floor_c3),
               len(forced_c3), redundant, len(C1), sorted(moved), len(C1)),
            pick("MUT-FLOOR", sorted(floor_c1), [floor_bound - 1])
            == [floor_bound]
            and sorted(floor_c3) == [floor_bound]
            and redundant == len(C1) and sorted(moved) == [floor_bound]
            and floor_bound < c1t[0],
            "floor bound %d, C1 %s, forced C3 %s, redundant %d of %d, "
            "moved-to-the-end %s"
            % (floor_bound, sorted(floor_c1), sorted(floor_c3), redundant,
               len(C1), sorted(moved)))
    # ---- W-C3REV: the TIME reads the order the stabilizer does not ---------
    rev_moved = 0
    for _nm, HS, SS in CORPORA:
        if _nm != "C3-R4-WINDOW":
            continue
        for H, s in zip(HS, SS):
            if crystallization(reversed_rounds(s)) != crystallization(H):
                rev_moved += 1
    LD.gate("G-TIME-READS-THE-ORDER",
            "THE CRYSTALLIZATION TIME IS WHERE THE ORDER ENTERS (W-C3REV, "
            "ENTIRE).  Every one of the %d committed R = 4 schedules is "
            "re-entered with each round's three groups in DESCENDING rather "
            "than ascending seed order -- the same events, a different "
            "sequence -- and the crystallization time MOVES at %d of them.  "
            "So the ordered comparison this unit's driven leg takes is the "
            "stronger licence of the two quantities: the stabilizer cannot "
            "use it and the time can"
            % (len(C3), rev_moved),
            pick("MUT-REVERSAL", rev_moved, 0) > 0 and rev_moved < len(C3),
            "schedules %d, crystallization times that move %d"
            % (len(C3), rev_moved))
    R["crystallization"] = {
        "per_corpus": {nm: {("never" if k is None else str(k)): v
                            for k, v in sorted(cc.items(),
                                               key=lambda kv: (kv[0] is None,
                                                               kv[0]))}
                       for nm, cc in sorted(crys.items())},
        "constant_on_C1_C2_C1FAN": c1t[0] if len(c1t) == 1 else None,
        "prefix_law_disagreements": len(pref_bad),
        "stabilizer_order_by_prefix_length_C1": list(profile or ()),
        "stabilizer_order_by_prefix_length_C1_distinct": len(prof),
        "stabilizer_order_by_prefix_length_C2_distinct": len(prof2),
        "events_four_and_five_are_transversals_of_the_first_round":
            transversal,
        "monotonicity_growth_events": len(mono_bad),
        "monotonicity_prefixes_checked": len(ordered[:2000]),
        "never_crystallizing": len(never),
        "never_crystallizing_arrangements": nev_names,
        "never_crystallizing_stabilizer_orders":
            sorted({young_order(H) for _n, H, _s in never}),
        "never_crystallizing_records":
            sorted({str(sorted(set(record_rows(H)))) for _n, H, _s in never}),
        "order_axis": {
            "window": "W-ORDER", "histories": n_axis,
            "times": {str(k): v for k, v in sorted(axis_t.items())},
            "distinct_profiles": len(axis_p),
            "profile": list(sorted(axis_p)[0])},
        "information_floor": {
            "counting_bound_ceil_log2_actors": floor_bound,
            "minimal_event_subset_C1": {str(k): v
                                        for k, v in sorted(floor_c1.items())},
            "minimal_event_subset_forced_C3":
                {str(k): v for k, v in sorted(floor_c3.items())},
            "forced_C3_histories": len(forced_c3),
            "round_one_third_event_redundant": redundant,
            "crystallization_with_it_moved_to_the_end":
                {str(k): v for k, v in sorted(moved.items())}},
        "reversal": {"window": "W-C3REV", "schedules": len(C3),
                     "crystallization_times_that_move": rev_moved},
    }
    SEAL.take("SEAL-CRYSTAL", R)
    reg(len(never), len(pref_bad), len(mono_bad), len(ordered[:2000]),
        n_axis, floor_bound, len(forced_c3), redundant, rev_moved,
        len(axis_p), len(floor_c1), len(floor_c3))
    for cc in crys.values():
        for k, v in cc.items():
            reg(v)
            if k is not None:
                reg(k)
    for cc in (axis_t, floor_c1, floor_c3, moved):
        for k, v in cc.items():
            reg(v)
            if k is not None:
                reg(k)

    # ---- SECTION 7.  THE PHYSICS-INVARIANCE CENSUS ------------------------
    say()
    say("SECTION 7.  THE PHYSICS-INVARIANCE CENSUS")
    # (a) THE CO-DIVISION RELATION -- the weld's own link generator
    cod_bad = []
    for P in NTP:
        r = codivision(P)
        for p in stab_elements(P):
            if any(r[p[u]][p[v]] != r[u][v]
                   for u in range(NACT) for v in range(NACT) if u != v):
                cod_bad.append(P)
                break
    ncod = pick("MUT-CODIV", len(cod_bad), 1)
    LD.gate("G-CODIVISION-BLIND",
            "THE WELD'S LINK GENERATOR IS BLIND TO THE UN-FORCED PART OF "
            "IDENTITY -- A THEOREM, VERIFIED PER OBJECT.  A stabilizer "
            "element fixes every event SETWISE, so an actor belongs to an "
            "event exactly when its image does; the co-division count of a "
            "pair is therefore carried unchanged.  Measured on all %d "
            "nontrivial-stabilizer objects over all %s stabilizer elements: "
            "the relation is preserved everywhere"
            % (len(NTP), com(nelem)),
            ncod == 0, "objects %d, elements %s, violations %d"
            % (len(NTP), com(nelem), ncod))
    # (b) THE WELD DICTIONARY'S READINGS -- count fields under precomposition
    cf_checks = cf_bad = 0
    lp0 = tuple(range(len(I7_LINKS)))
    for P in NTP:
        rel = codivision(P)
        base = count_field_at(P, IDENT_ASSIGN, lp0, False, rel)
        for p in stab_elements(P):
            got = count_field_at(P, compose_assign(IDENT_ASSIGN, p), lp0,
                                 False, rel)
            cf_checks += 1
            if got != base:
                cf_bad += 1
    cf_bad = pick("MUT-WELDREAD", cf_bad, 1)
    LD.gate("G-WELD-DICTIONARY",
            "EVERY READING THE WELD DICTIONARY PUBLISHES IS BLIND TOO, AT THE "
            "IDENTITY PARSE.  Paper-19's induced count field reads the "
            "co-division relation through a parse; precomposing that parse "
            "with a stabilizer element leaves the field entry for entry, "
            "because the element is an automorphism of the relation the field "
            "reads.  Measured at %s parse comparisons over %d objects -- "
            "EVERY stabilizer element of every object, with no cap -- and %d "
            "differences.  This gate takes the IDENTITY parse; the twelve-"
            "parse sweep below is what licenses the word EVERY"
            % (com(cf_checks), len(NTP), cf_bad),
            cf_bad == 0, "comparisons %d, differences %d"
            % (cf_checks, cf_bad))
    # ---- W-PARSE: the same sweep at ALL TWELVE declared parses -------------
    p12_checks = p12_bad = 0
    for P in NTP:
        rel = codivision(P)
        for pairs in PARSE_PAIRS:
            base = field_through(rel, pairs, IDENT_PARSE)
            for p in stab_elements(P):
                p12_checks += 1
                if field_through(rel, pairs, inverse_perm(p)) != base:
                    p12_bad += 1
    p12_bad = pick("MUT-WELD12", p12_bad, 1)
    LD.gate("G-WELD-TWELVE-PARSES",
            "THE WORD 'EVERY' IS MEASURED AND NOT ONLY PROVED (W-PARSE, "
            "ENTIRE; #289 MINOR-3).  The dictionary's fiber carries %d "
            "readings -- %d link-label permutations times the two "
            "orientations -- and the delivered sweep took one of them.  Every "
            "reading is swept here against every stabilizer element of every "
            "nontrivial object: %s comparisons, %d differences.  The theorem "
            "is uniform in the label permutation and the orientation and the "
            "measurement now says so too"
            % (len(PARSES), math.factorial(len(I7_LINKS)), com(p12_checks),
               p12_bad),
            p12_bad == 0 and p12_checks == len(PARSES) * nelem,
            "parses %d, comparisons %d, differences %d"
            % (len(PARSES), p12_checks, p12_bad))
    reg(len(PARSES), p12_checks, p12_bad, math.factorial(len(I7_LINKS)))
    # (c) THE RECORD'S ATTRIBUTION -- the measurement, not a theorem
    def rec_inv(P):
        return orbit_constant(record_rows(P), signature_blocks(P))

    def born_inv(P, t):
        return orbit_constant(born_rows(P, t), signature_blocks(P))

    rec_ok = sum(1 for P in NTP if rec_inv(P))
    born_ok = {t: sum(1 for P in NTP if born_inv(P, t))
               for t in range(1, WALK_DEPTH + 1)}
    cross = Counter((rec_inv(P), born_inv(P, 1), born_inv(P, 2)) for P in NTP)
    rec_ok_m = pick("MUT-RECINV", rec_ok, len(NTP))
    LD.gate("G-RECORD-ATTRIBUTION",
            "THE RECORD IS ALWAYS WELL DEFINED AS A FIELD OVER THE ARENA, AND "
            "WELL DEFINED AS A PROPERTY OF A THREAD EXACTLY WHERE THE HISTORY "
            "FORCES THE THREAD (#288 MAJOR-4, the scoped form).  Two namings "
            "that differ by a stabilizer element produce the SAME labelled "
            "history, so the field n_l(x) is literally the same object; what "
            "differs is WHICH THREAD sits at which site.  Where identity is "
            "forced there is nothing to differ and the attribution is well "
            "defined trivially -- which on this census is almost every "
            "history.  The measurement is taken on the un-forced stratum, the "
            "%d objects whose stabilizer is nontrivial: the attribution "
            "survives at %d of them and fails at %d, so the failure is a "
            "statement about %d prefix objects and never about the census"
            % (len(NTP), rec_ok, len(NTP) - rec_ok, len(NTP)),
            rec_ok_m < len(NTP) and rec_ok > 0,
            "orbit-constant %d of %d; naming-dependent %d"
            % (rec_ok, len(NTP), len(NTP) - rec_ok))
    # (d) THE WALK'S BORN MENU
    nsym = ntr = nrecpres = 0
    sym_bad = []
    for P in NTP:
        rows = record_rows(P)
        for p in stab_elements(P):
            sh, cn = walk_commutes(P, p)
            istr = p in TRANSL_SET
            if sh:
                ntr += 1
            if cn:
                nrecpres += 1
            if sh and cn:
                nsym += 1
            if sh != istr:
                sym_bad.append((P, p))
    LD.gate("G-SHIFT-IS-TRANSLATION",
            "THE SHIFT'S SYMMETRIES ARE EXACTLY THE TRANSLATIONS -- A "
            "THEOREM, MEASURED BOTH WAYS.  A relabelling commutes with "
            "paper-20's shift exactly when it carries x + l to sigma(x) + l "
            "for all three declared links, which forces sigma to be a "
            "translation of AG(2,3).  Both sides are computed independently "
            "on all %s stabilizer elements -- the shift test cell by cell, "
            "the translation test against the nine translations -- and they "
            "agree at every one" % com(nelem),
            not pick("MUT-SHIFT", sym_bad, [(0, 0)]),
            "elements %d, shift-commuting %d, translations in the "
            "stabilizers %d, disagreements %d"
            % (nelem, ntr, sum(1 for P in NTP
                               for p in stab_elements(P) if p in TRANSL_SET),
               len(sym_bad)))
    LD.gate("G-BORN-MENU",
            "THE WALK SEES WHAT THE RECORD CANNOT.  Paper-20's coupled step "
            "-- the site-block-diagonal coin C(x) = G.D(x) with D(x) = "
            "diag(w^{n_l(x)}), then the shift -- is re-implemented here over "
            "Z[w] and run from the S_9-symmetric all-ones start, so every "
            "asymmetry in the published Born menu is carried by the record "
            "and the shift and never by the start.  AT THE DECLARED COIN "
            "ORDER G.D the menu is orbit-constant at %s objects by depth, "
            "against the record's %d: the one-step menu is blind at MORE "
            "objects than the record, and from depth two it is blind at "
            "FEWER.  That ordering is COIN-ORDER-RELATIVE and the other "
            "declared order is published at G-COIN-ORDER below.  A stabilizer "
            "element is a symmetry of the whole coupled step exactly when it "
            "is a translation AND preserves the record: %d of %s elements"
            % ([born_ok[t] for t in range(1, WALK_DEPTH + 1)], rec_ok,
               nsym, com(nelem)),
            born_ok[1] > rec_ok and born_ok[2] < rec_ok
            and pick("MUT-BORN", nsym, nelem) < nelem and nsym > 0,
            "born-invariant by depth %s; record-invariant %d; walk "
            "symmetries %d of %d; record-preserving elements %d"
            % ([born_ok[t] for t in range(1, WALK_DEPTH + 1)], rec_ok,
               nsym, nelem, nrecpres))
    # ---- W-COIN: the depth ordering is COIN-ORDER-RELATIVE -----------------
    born_dg = {t: sum(1 for P in NTP
                      if orbit_constant(born_rows(P, t, "D.G"),
                                        signature_blocks(P)))
               for t in range(1, WALK_DEPTH + 1)}
    ladder = {"G.D": [born_ok[t] for t in range(1, WALK_DEPTH + 1)],
              "D.G": [born_dg[t] for t in range(1, WALK_DEPTH + 1)]}
    cross_dg = Counter((rec_inv(P),
                        orbit_constant(born_rows(P, 2, "D.G"),
                                       signature_blocks(P))) for P in NTP)
    finer = {k: min([t for t in range(1, WALK_DEPTH + 1)
                     if ladder[k][t - 1] < rec_ok] or [0])
             for k in ladder}
    tail = {k: sorted({ladder[k][t - 1] for t in range(3, WALK_DEPTH + 1)})
            for k in ladder}
    LD.gate("G-COIN-ORDER",
            "THE DEPTH AT WHICH THE MENU REFINES THE RECORD IS COIN-ORDER-"
            "RELATIVE, AND BOTH DECLARED ORDERS ARE PUBLISHED (W-COIN, "
            "ENTIRE; #288 MAJOR-2).  Paper-20's step admits C(x) = G.D(x) and "
            "C(x) = D(x).G.  At G.D the blind ladder by depth is %s and the "
            "menu is strictly finer than the record's %d from depth %d; at "
            "D.G it is %s -- the record phase applied last is modulus-"
            "preserving, so the one-step menu is blind EVERYWHERE and the "
            "depth-two menu is blind at MORE objects than the record, which "
            "reverses the delivered ordering.  What is order-INDEPENDENT is "
            "the tail: %s under both orders from depth three on.  A unit that "
            "published one order would have published an artifact of the "
            "declaration"
            % (ladder["G.D"], rec_ok, finer["G.D"], ladder["D.G"],
               tail["G.D"]),
            pick("MUT-COINORDER", ladder["D.G"], ladder["G.D"])
            != ladder["G.D"]
            and tail["G.D"] == tail["D.G"] and len(tail["G.D"]) == 1
            and finer["G.D"] < finer["D.G"],
            "G.D %s, D.G %s, common tail %s, first finer depth G.D %d D.G %d"
            % (ladder["G.D"], ladder["D.G"], tail["G.D"], finer["G.D"],
               finer["D.G"]))
    reg(*ladder["D.G"])
    for v in cross_dg.values():
        reg(v)
    reg(finer["G.D"], finer["D.G"], tail["G.D"][0])
    # (e) THE DEGENERACY -- |Aut| of the co-division relation against |Stab|
    aut_full = {}
    for nm, HS, _s in CORPORA:
        if nm == "C2-R6-CONCATENATIONS":
            HS = [C2[i * len(C1) + i] for i in range(len(C1))]
        aut_full[nm] = Counter(aut_codivision(H) for H in HS)
    aut_pairs = Counter((young_order(P), aut_codivision(P)) for P in NTP)
    shortcut_obj = [H for _n, HS, _s in CORPORA for H in HS
                    if len({codivision(H)[a][b]
                            for a in range(NACT) for b in range(NACT)
                            if a != b}) == 1]
    shortcut_ok = None
    if shortcut_obj:
        shortcut_ok = len(aut_codivision(shortcut_obj[0], count_only=False))
    LD.gate("G-AUT-SHORTCUT",
            "THE CONSTANT-WEIGHT SHORTCUT IS A MACHINE-CHECKED FORCING, NOT A "
            "WAIVER (#34).  When every off-diagonal co-division weight is "
            "equal, every permutation preserves the relation and the "
            "automorphism group is all of S_9; the closed value is confirmed "
            "by ENUMERATING one such object's automorphisms explicitly, at "
            "%s of them" % com(shortcut_ok or 0),
            pick("MUT-SHORTCUT", shortcut_ok, 1) == math.factorial(NACT),
            "enumerated %s, closed %s" % (com(shortcut_ok or 0),
                                          com(math.factorial(NACT))))
    deg = sum(v for k, v in aut_full["C3-R4-WINDOW"].items()
              if k == math.factorial(NACT))
    LD.gate("G-CODIVISION-FORGETS",
            "THE RELATION FORGETS WHAT THE EVENTS REMEMBER (#289 MAJOR-1: "
            "the contrast is with the EVENTS, never with the ordering, which "
            "the stabilizer cannot read).  At %d of the %d R = 4 window "
            "histories -- exactly the schedules that use all four parallel "
            "classes once each, and %d = 4! is the number of their orderings, "
            "so the count is forced rather than found -- every pair of actors "
            "co-divides exactly once, so the co-division relation is the "
            "CONSTANT COMPLETE GRAPH and its automorphism group is the whole "
            "of S_9 at %s elements; yet the stabilizer of the EVENT SET is "
            "TRIVIAL at every one of them.  The weld reads through that "
            "relation, so at these histories the dictionary's site freedom is "
            "total while the identity the events force is complete.  The gap "
            "is CONTAINMENT WITH AN INDEX and never disjointness: Stab is a "
            "subgroup of Aut at every object, and the index is published in "
            "full"
            % (deg, len(C3), math.factorial(len(CLASS_NAMES)),
               com(math.factorial(NACT))),
            deg > 0
            and all(young_order(H) == 1 for H in C3
                    if aut_codivision(H) == math.factorial(NACT))
            and all((aut_codivision(history_of(sch))
                     == math.factorial(NACT))
                    == (len({CLASS_OF.get(P) for P, _q in sch})
                        == len(CLASS_NAMES))
                    for sch in W)
            and all(a % s == 0 and a >= s for s, a in aut_pairs)
            and pick("MUT-DEGENERACY", deg, 0)
            == math.factorial(len(CLASS_NAMES)),
            "complete-relation histories %d, all with trivial stabilizer %s, "
            "complete-relation iff all four classes used %s, index integral "
            "at all %d pair rows %s"
            % (deg, all(young_order(H) == 1 for H in C3
                        if aut_codivision(H) == math.factorial(NACT)),
               all((aut_codivision(history_of(sch)) == math.factorial(NACT))
                   == (len({CLASS_OF.get(P) for P, _q in sch})
                       == len(CLASS_NAMES)) for sch in W),
               len(aut_pairs),
               all(a % s == 0 for s, a in aut_pairs)))
    # ---- THE AXIS THE CENSUS STRATIFIES ALONG (#288 MAJOR-5) --------------
    # The four chart histories are not scattered: they are the constant-class
    # controls.  The axis is ADMISSIBILITY -- covering the link field, or
    # inducing I7's G-FLAT row -- and it is measured here rather than named.
    cov_flags = [covered_cells(s) == len(CELLS) for s in W]
    chart_flags = [young_order(H) > 1 for H in C3]
    five_flags = [crystallization(H) == c1t[0] for H in C3]
    flat_hist = [history_of(tuple((parts[i], canon_transversals(parts[i])[0])
                                  for i in q)) for q in flatq]
    n_cov = sum(cov_flags)
    n_five = sum(five_flags)
    both = sum(1 for i in range(len(C3)) if cov_flags[i] and five_flags[i])
    cov_only = n_cov - both
    five_only = n_five - both
    chart_cov = sum(1 for i in range(len(C3))
                    if cov_flags[i] and chart_flags[i])
    chart_flat = sum(1 for H in flat_hist if young_order(H) > 1)
    chart_cells = sorted(covered_cells(W[i]) for i in range(len(C3))
                         if chart_flags[i])
    LD.gate("G-ADMISSIBILITY-AXIS",
            "THE CENSUS STRATIFIES ALONG ADMISSIBILITY, AND THE FOUR CHART "
            "HISTORIES ARE CONSTANT-CLASS CONTROLS (#288 MAJOR-5).  Measured: "
            "%d of the %d R = 4 schedules are I7-COVERING and %d of them is "
            "chart; the %d G-FLAT quadruples induce %d histories and %d of "
            "them is chart; the summed link fields of the %d chart histories "
            "reach %s of the %d cells, so not one of them is admissible in "
            "either sense.  Identity is forced on EVERY admissible history of "
            "this census, and the exceptions are the controls the window was "
            "built to carry"
            % (n_cov, len(C3), chart_cov, len(flatq), len(flat_hist),
               chart_flat, len(chart_cells), chart_cells, len(CELLS)),
            pick("MUT-ADMISS", chart_cov, 1) == 0 and chart_flat == 0
            and 0 < n_cov < len(C3)
            and all(c < len(CELLS) for c in chart_cells),
            "covering %d of %d, chart among them %d; G-FLAT histories %d, "
            "chart among them %d; chart coverage %s"
            % (n_cov, len(C3), chart_cov, len(flat_hist), chart_flat,
               chart_cells))
    LD.gate("G-TWO-FOURS-ARE-NOT-ONE",
            "TWO EQUAL COUNTS IN ONE CORPUS ARE NOT A RESONANCE, AND THIS "
            "UNIT CARRIES ITS OWN CONTROL (#288 section 4.2).  %d of the %d "
            "R = 4 schedules are I7-COVERING and %d crystallize at %d -- the "
            "same numeral twice -- and they are NOT the same set: %d are "
            "both, %d cover without crystallizing at %d, %d crystallize at %d "
            "without covering.  A numeral co-incidence inside one corpus with "
            "no shared mechanism is exactly the shape of a co-incidence "
            "across two, which is why this unit registers no resonance "
            "between its crystallization constant and any inherited five and "
            "names the collision instead"
            % (n_cov, len(C3), n_five, c1t[0], both, cov_only, c1t[0],
               five_only, c1t[0]),
            pick("MUT-FIVES", n_cov, n_cov + 1) == n_five
            and cov_only > 0 and five_only > 0 and cov_only == five_only
            and both < n_cov,
            "covering %d, five %d, both %d, covering-not-five %d, "
            "five-not-covering %d"
            % (n_cov, n_five, both, cov_only, five_only))
    reg(n_cov, n_five, both, cov_only, five_only, chart_cov, chart_flat,
        len(flat_hist), *chart_cells)
    # ---- THE DECISIVE GATE: THE SPLIT IS BETWEEN TESTS (#288 MAJOR-1) -----
    # Two tests are declared.  THE TRANSPORTED READING asks whether the
    # observable survives when the reading is carried along by the relabelling;
    # THE FIXED ATTRIBUTION asks whether the observable, read at a fixed
    # parse, assigns the same value to actors the history cannot tell apart.
    # The delivered verdict paired one test on two observables against the
    # other test on two others.  Both tests are applied to both sides here.
    weld_is_record = 0
    for P in NTP:
        rel = codivision(P)
        if (field_through(rel, PARSE_PAIRS[0], IDENT_PARSE)
                == tuple(rel[a][b] for a, b in RECORD_PAIRS)):
            weld_is_record += 1
    weld_attr = []
    for pairs in PARSE_PAIRS:
        n = 0
        for P in NTP:
            f = field_through(codivision(P), pairs, IDENT_PARSE)
            rows = [tuple(f[s * len(I7_LINKS) + i]
                          for i in range(len(I7_LINKS)))
                    for s in range(NACT)]
            if orbit_constant(rows, signature_blocks(P)):
                n += 1
        weld_attr.append(n)
    hist_checks = hist_bad = 0
    menu_checks = menu_bad = 0
    for P in NTP:
        rel = codivision(P)
        base_menu = menus_from_field([rel[a][b] for a, b in RECORD_PAIRS], 2)
        for p in stab_elements(P):
            hist_checks += 1
            if tuple(frozenset(SITES[p[SITE_INDEX[x]]] for x in F)
                     for F in P) != P:
                hist_bad += 1
            inv = inverse_perm(p)
            menu_checks += 1
            if menus_from_field([rel[inv[a]][inv[b]]
                                 for a, b in RECORD_PAIRS], 2) != base_menu:
                menu_bad += 1
    split = {
        "tests": ["THE-TRANSPORTED-READING", "THE-FIXED-ATTRIBUTION"],
        "weld_field_equals_the_record_at_the_identity_parse": weld_is_record,
        "weld_field_attribution_by_parse": weld_attr,
        "record_attribution": rec_ok,
        "menu_attribution_depth_two_failures": len(NTP) - born_ok[2],
        "relabelled_history_comparisons": hist_checks,
        "relabelled_history_differences": hist_bad,
        "transported_menu_comparisons": menu_checks,
        "transported_menu_violations": menu_bad,
        "transported_record_comparisons": cf_checks,
        "transported_record_violations": cf_bad,
    }
    LD.gate("G-INVARIANCE-SPLIT",
            "THE SPLIT THIS UNIT MEASURES IS A SPLIT BETWEEN THE TWO TESTS "
            "AND NOT BETWEEN THE OBSERVABLES (#288 MAJOR-1, the decisive "
            "row).  The pin asks: any non-invariance implies the observable "
            "NAMES threads the structure does not force.  Both declared tests "
            "are applied to BOTH sides.  (1) At the identity parse the weld's "
            "own count field IS the record, object for object, at %d of %d.  "
            "(2) Under the FIXED ATTRIBUTION test the weld's own field is "
            "orbit-constant at %s of %d at every one of the twelve declared "
            "parses -- the record's own number -- and the depth-two menu "
            "fails at %d.  (3) Under the TRANSPORTED READING test a "
            "stabilizer element carries the labelled history to itself at %s "
            "of %s comparisons, so every field of the history is literally "
            "the same object; the record is re-read through the transported "
            "parse at %s comparisons with %d violations and the Born menu, "
            "recomputed from the transported record field to depth two, at %s "
            "with %d.  Swap the tests and the verdicts swap with them: "
            "NOTHING in this data distinguishes a 'space' observable from a "
            "'matter' observable, and no sentence of this unit may say "
            "otherwise"
            % (weld_is_record, len(NTP), sorted(set(weld_attr)), len(NTP),
               len(NTP) - born_ok[2], com(hist_checks - hist_bad),
               com(hist_checks), com(cf_checks), cf_bad, com(menu_checks),
               menu_bad),
            pick("MUT-SPLIT", weld_is_record, 0) == len(NTP)
            and len(set(weld_attr)) == 1 and weld_attr[0] == rec_ok
            and hist_bad == 0 and menu_bad == 0
            and len(NTP) - born_ok[2] > rec_ok,
            "weld==record %d of %d; attribution by parse %s; history "
            "differences %d of %d; transported menu violations %d of %d"
            % (weld_is_record, len(NTP), sorted(set(weld_attr)), hist_bad,
               hist_checks, menu_bad, menu_checks))
    reg(weld_is_record, hist_checks, hist_bad, menu_checks, menu_bad,
        len(NTP) - born_ok[2], *weld_attr)
    R["invariance"] = {
        "nontrivial_objects": len(NTP),
        "stabilizer_elements": nelem,
        "codivision_violations": ncod,
        "weld_twelve_parse_comparisons": p12_checks,
        "weld_twelve_parse_differences": p12_bad,
        "split_by_test": split,
        "born_orbit_constant_by_depth_DG": {str(t): born_dg[t]
                                            for t in range(1, WALK_DEPTH + 1)},
        "coin_orders": list(COIN_ORDERS),
        "coin_order_ladder": ladder,
        "coin_order_common_tail": tail["G.D"][0],
        "first_depth_strictly_finer_than_the_record":
            {k: finer[k] for k in sorted(finer)},
        "cross_tab_record_born2_DG": {"%s|%s" % k: v
                                      for k, v in sorted(cross_dg.items())},
        "weld_parse_comparisons": cf_checks,
        "weld_parse_differences": cf_bad,
        "record_orbit_constant": rec_ok,
        "record_naming_dependent": len(NTP) - rec_ok,
        "born_orbit_constant_by_depth": {str(t): born_ok[t]
                                         for t in range(1, WALK_DEPTH + 1)},
        "cross_tab_record_born1_born2": {
            "%s|%s|%s" % k: v for k, v in sorted(cross.items())},
        "walk_symmetries": nsym,
        "shift_commuting_elements": ntr,
        "record_preserving_elements": nrecpres,
        "shift_translation_disagreements": len(sym_bad),
        "aut_codivision_full_histories": {
            nm: {str(k): v for k, v in sorted(cc.items())}
            for nm, cc in sorted(aut_full.items())},
        "aut_window_C2": "W-AUTC2: the %d diagonal concatenations" % len(C1),
        "stab_aut_pairs": {"%d/%d" % k: v for k, v in sorted(aut_pairs.items())},
        "complete_relation_histories": deg,
        "complete_relation_histories_are_the_class_orderings":
            math.factorial(len(CLASS_NAMES)),
        "stab_is_a_subgroup_of_aut": "measured at G-CODIVISION-BLIND over "
                                     "every stabilizer element of every "
                                     "object; the index is published in full",
        "aut_shortcut_enumerated": shortcut_ok,
        "admissibility": {
            "covering_schedules": n_cov,
            "chart_among_covering": chart_cov,
            "flat_quadruple_histories": len(flat_hist),
            "chart_among_flat_quadruple_histories": chart_flat,
            "chart_history_cells_covered": chart_cells,
            "cells": len(CELLS)},
        "two_fours": {"covering": n_cov, "crystallize_at_the_constant": n_five,
                      "both": both, "covering_not_five": cov_only,
                      "five_not_covering": five_only},
    }
    SEAL.take("SEAL-INVARIANCE", R)
    reg(ncod, cf_checks, cf_bad, rec_ok, len(NTP) - rec_ok, nsym, ntr,
        nrecpres, deg, len(sym_bad), shortcut_ok)
    for t in born_ok:
        reg(born_ok[t])
    for v in cross.values():
        reg(v)
    for cc in aut_full.values():
        for k, v in cc.items():
            reg(k, v)
    for k, v in aut_pairs.items():
        reg(k[0], k[1], v)

    # ---- the walk's own arena, gated against paper-20's committed receipt --
    p20cells = len(p20["arena"]["cells"]) if isinstance(
        p20.get("arena", {}).get("cells"), list) else DIM
    LD.gate("G-WALK-ARENA",
            "THE WALK IS RE-IMPLEMENTED, NEVER IMPORTED, AND ITS ARENA IS "
            "GATED.  The %d cells, the three declared link directions, the "
            "Grover numerators over 3 and the shift table are rebuilt here "
            "from the arena's own definitions; the shift is a permutation of "
            "the cells (a bijection, checked), the coin is site-block-"
            "diagonal by construction, and the Born weights are RATIONAL "
            "INTEGERS because |a + bw|^2 = a^2 - ab + b^2"
            % DIM,
            sorted(SHIFT_T) == list(range(DIM))
            and all(isinstance(v, int) for J in born_menus(C1[0], 1) for v in J)
            and pick("MUT-WALK", DIM, DIM + 1) == len(CELLS),
            "cells %d, shift a bijection %s, integer Born weights %s"
            % (DIM, sorted(SHIFT_T) == list(range(DIM)), True))
    modmap = {}
    modbad = 0
    for P in NTP:
        rows = record_rows(P)
        jr = born_rows(P, 1)
        for si in range(NACT):
            key = tuple(v % 3 for v in rows[si])
            if key in modmap and modmap[key] != jr[si]:
                modbad += 1
            modmap[key] = jr[si]
    LD.gate("G-BORN-DEPTH-ONE-LAW",
            "THE DEPTH-ONE MENU IS A FUNCTION OF THE SITE'S OWN RECORD ROW "
            "MODULO THREE, MEASURED RATHER THAN ASSERTED.  The coin is "
            "site-block-diagonal and the start is the all-ones state, so the "
            "post-coin weight at a site depends on that site's three counts "
            "only through w to those powers.  Over every site of every one of "
            "the %d nontrivial objects the map from the residue triple to the "
            "menu row is single-valued: %d distinct residue triples, %d "
            "collisions" % (len(NTP), len(modmap), modbad),
            pick("MUT-BORNLAW", modbad, 1) == 0 and len(modmap) > 1,
            "residue triples %d, collisions %d" % (len(modmap), modbad))
    reg(len(modmap), modbad)
    R["walk"] = {
        "cells": DIM, "links": len(I7_LINKS), "depth": WALK_DEPTH,
        "start": "the S_9-symmetric all-ones state",
        "coin": "C(x) = G . D(x), D(x) = diag(w^{n_l(x)}); 3G has -1 on the "
                "diagonal and 2 off it",
        "born_weight_form": "|a + b w|^2 = a^2 - a b + b^2, a rational "
                            "integer",
        "shift_is_a_bijection": sorted(SHIFT_T) == list(range(DIM)),
        "depth_one_residue_classes": len(modmap),
        "depth_one_residue_collisions": modbad,
        "symmetry_criterion": "a stabilizer element is a symmetry of the "
                              "coupled step exactly when it is a translation "
                              "of AG(2,3) and preserves the record",
        "menu_at_the_never_crystallizing_histories": sorted(
            {str(sorted(set(born_rows(H, 1))))
             for _n, H, _s in never}) if never else [],
    }
    SEAL.take("SEAL-WALK", R)
    reg(DIM, WALK_DEPTH)

    # ---- SECTION 8.  E-24: THE COUNTS ARE MEASURE-RELATIVE -----------------
    say()
    say("SECTION 8.  THE MEASURE-RELATIVITY OF THE HEADLINE COUNTS (E-24)")
    mult_nt = mult_rec = mult_b2 = 0
    for nm, HS, _s in CORPORA:
        for H in HS:
            for k in range(1, len(H) + 1):
                P = H[:k]
                if young_order(P) > 1:
                    mult_nt += 1
                    if rec_inv(P):
                        mult_rec += 1
                    if born_inv(P, 2):
                        mult_b2 += 1
    # the SAME measure at the SAME family as the multiplicity leg, so that the
    # measure effect and the FAMILY effect are separated rather than summed
    # (#292 MAJOR-2): distinct prefixes over the three primary corpora.
    ntp_primary = [P for P in fam_primary if young_order(P) > 1]
    rec_primary = sum(1 for P in ntp_primary if rec_inv(P))
    f_dist = Fraction(rec_ok, len(NTP))
    f_mult = Fraction(mult_rec, mult_nt)
    f_dist_primary = Fraction(rec_primary, len(ntp_primary))
    g_dist = Fraction(born_ok[2], len(NTP))
    g_mult = Fraction(mult_b2, mult_nt)
    LD.gate("G-E24-MEASURE",
            "NO COUNT BECOMES A PROBABILITY WITHOUT A DECLARED MEASURE "
            "(E-24), AND THE MEASURE EFFECT IS SEPARATED FROM THE FAMILY "
            "EFFECT RATHER THAN SUMMED WITH IT (#292 MAJOR-2).  Three "
            "fractions, not two.  AT ONE FAMILY, the three primary corpora: "
            "the record's blindness is %s by distinct prefix and %s by corpus "
            "multiplicity -- that difference is the MEASURE effect, and it is "
            "small.  AT ONE MEASURE, distinct prefix: %s over the three "
            "primary corpora against %s over the four declared -- that "
            "difference is the FAMILY effect, and it is the larger half of "
            "the published contrast.  The walk's pair is %s and %s.  Every "
            "fraction is stamped COUNTING-ONLY and carries BOTH its measure "
            "and its family"
            % (f_dist_primary, f_mult, f_dist_primary, f_dist, g_dist, g_mult),
            pick("MUT-E24", f_dist, f_mult) != f_mult and g_dist != g_mult
            and f_dist_primary != f_mult and f_dist != f_dist_primary,
            "same family: distinct %s vs multiplicity %s; same measure: "
            "primary %s vs declared %s; walk %s vs %s"
            % (f_dist_primary, f_mult, f_dist_primary, f_dist, g_dist, g_mult))
    R["measure_relativity"] = {
        "stamp": "COUNTING-ONLY",
        "measures": ["DISTINCT-PREFIX-OVER-THE-FOUR-DECLARED-CORPORA",
                     "DISTINCT-PREFIX-OVER-THE-THREE-PRIMARY-CORPORA",
                     "MULTIPLICITY-OVER-THE-THREE-PRIMARY-CORPORA"],
        "nontrivial_distinct": len(NTP),
        "nontrivial_distinct_primary": len(ntp_primary),
        "nontrivial_with_multiplicity": mult_nt,
        "record_blind_distinct": rec_ok,
        "record_blind_distinct_primary": rec_primary,
        "record_blind_multiplicity": mult_rec,
        "walk_blind_distinct": born_ok[2],
        "walk_blind_multiplicity": mult_b2,
        "record_fraction_distinct": str(f_dist),
        "record_fraction_distinct_primary": str(f_dist_primary),
        "record_fraction_multiplicity": str(f_mult),
        "walk_fraction_distinct": str(g_dist),
        "walk_fraction_multiplicity": str(g_mult),
        "the_measure_effect": "at the THREE-PRIMARY family, distinct prefix "
                              "against corpus multiplicity",
        "the_family_effect": "at the DISTINCT-PREFIX measure, three primary "
                             "corpora against four declared",
    }
    SEAL.take("SEAL-MEASURE", R)
    reg(mult_nt, mult_rec, mult_b2, f_dist, f_mult, g_dist, g_mult,
        f_dist_primary, len(ntp_primary), rec_primary)

    # ---- SECTION 9.  THE GRAIN --------------------------------------------
    say()
    say("SECTION 9.  THE GRAIN -- WHAT RAN AND WHAT IS REGISTERED")
    groupoid_note = (
        "THE GROUPOID GRAIN, REGISTERED AND NOT RUN.  Everything above is "
        "taken at the GLOBAL-RELABELLING grain: one permutation of the nine "
        "actors, applied to every event of the history at once.  A strictly "
        "finer question is whether a thread may be re-identified BETWEEN "
        "events -- a groupoid of partial identifications rather than a group "
        "-- under which the object is not a stabilizer subgroup but a set of "
        "composable local isomorphisms.  Group-level triviality does NOT "
        "imply groupoid-level rigidity, so the word FORCED is not inherited "
        "by the finer grain and must be re-earned there.  This unit does not "
        "run it, does not estimate it, and does not let any sentence of its "
        "verdict depend on it; the successor question is stated here with its "
        "object named so that the scope of every result above is exactly the "
        "stabilizer grain.")
    decomposition_note = (
        "THE DECOMPOSITION GRAIN, OWED AND UNREGISTERED UNTIL NOW.  The two "
        "grains above both take the nine-actor decomposition as GIVEN and ask "
        "only what its parts are called.  Barandes' worry is about which "
        "factors there are: a decomposition of a system into subsystems is a "
        "factorization CHOICE unless the law picks it out.  The object of "
        "that question is the carrier and its arity -- the stabilizer census "
        "taken at the cell grain against the site grain -- and no unit of "
        "this corpus is pointed at it.  It is registered here as OWED so that "
        "no reader takes this unit's answer about NAMES for an answer about "
        "FACTORS; and the global grain this unit does run presupposes the "
        "thing the reality question asks about, since a global relabelling is "
        "definable only if actors persist across events.")
    LD.gate("G-GRAIN-REGISTERED",
            "THE SCOPE IS THE STABILIZER GRAIN, AND THE TWO FINER GRAINS ARE "
            "NAMED RATHER THAN ESTIMATED (#288 MAJOR-6).  The pin confines "
            "this unit to global relabelling.  THREE grains are distinguished "
            "and the receipt carries all three: NAMING (run -- S_9 on a "
            "granted nine-actor set), RE-IDENTIFICATION (registered, not run "
            "-- the groupoid), and DECOMPOSITION (owed and unregistered "
            "before this run -- which subsystems there are at all, the grain "
            "Barandes' worry actually names).  No verdict segment of this "
            "unit quantifies over the second or the third",
            pick("MUT-GRAIN", "groupoid" in groupoid_note, False)
            and "REGISTERED AND NOT RUN" in groupoid_note
            and len(groupoid_note) > 400
            and "OWED" in decomposition_note
            and len(decomposition_note) > 400,
            "grains 3, successor registered at %d characters, decomposition "
            "grain registered as owed at %d, no verdict segment depends on "
            "either" % (len(groupoid_note), len(decomposition_note)))
    R["grain"] = {
        "grain_run": "GLOBAL-RELABELLING (the stabilizer grain)",
        "grain_registered": "GROUPOID (mid-history thread swaps)",
        "grain_owed": "DECOMPOSITION (which subsystems there are: the "
                      "carrier and its arity)",
        "grains": [
            {"grain": "NAMING", "object": "S_9 acting on a granted "
                                          "nine-actor set", "status": "RUN"},
            {"grain": "RE-IDENTIFICATION",
             "object": "composable local isomorphisms between events",
             "status": "REGISTERED, NOT RUN"},
            {"grain": "DECOMPOSITION",
             "object": "which subsystems exist at all -- the carrier and its "
                       "arity", "status": "OWED, NOT REGISTERED BEFORE THIS "
                                          "RUN"}],
        "note": groupoid_note,
        "decomposition_note": decomposition_note,
    }
    SEAL.take("SEAL-GRAIN", R)
    reg(len(groupoid_note), len(decomposition_note), len(R["grain"]["grains"]))

    # ---- SECTION 10.  THE COUNTS AND THE VERDICT --------------------------
    say()
    say("SECTION 10.  THE VERDICT")
    R["counts"] = {
        "histories": R["corpora"]["histories_total"],
        "independent_histories": R["corpora"]["independent_histories"],
        "prefix_objects": R["corpora"]["prefix_objects_total"],
        "distinct_prefixes": len(ordered),
        "order_axis_histories": n_axis,
        "information_floor": floor_bound,
        "covering_schedules": n_cov,
        "weld_twelve_parse_comparisons": p12_checks,
        "forced_histories": forced_hist,
        "chart_histories": chart_hist,
        "nontrivial_prefixes": len(NTP),
        "stabilizer_elements": nelem,
        "crystallization_constant": R["crystallization"][
            "constant_on_C1_C2_C1FAN"],
        "never_crystallizing": len(never),
        "record_blind": rec_ok,
        "record_naming": len(NTP) - rec_ok,
        "walk_blind_depth1": born_ok[1],
        "walk_blind_depth2": born_ok[2],
        "walk_symmetries": nsym,
        "complete_relation_histories": deg,
        "sources": len(SOURCES),
        "windows": len(WINDOW_DECL),
        "verbatim_anchors": len(VERBATIM),
    }
    R["verdict"] = {"segments": verdict_segments(R, cross)}
    R["verdict"]["head"] = " ".join(R["verdict"]["segments"])
    indep = independent_head(R, C1, C2, C3, C1FAN, never)
    missing = sorted(k for k, v in indep.items()
                     if str(v) not in R["verdict"]["head"]
                     and com(v) not in R["verdict"]["head"]
                     if isinstance(v, int))
    disagree = sorted(k for k, v in indep.items()
                      if k in R["counts"] and R["counts"][k] != v)
    if mut("MUT-COMPARATOR"):
        disagree = ["FORGED"]
    LD.gate("G-VERDICT-RECONSTRUCTED",
            "THE HEAD IS DERIVED A SECOND TIME BY A COMPARATOR THAT SHARES "
            "NOTHING WITH THE BUILDER (#82, strengthened; #292 m-1 closed).  "
            "The comparator recomputes %d load-bearing quantities from the "
            "corpora themselves -- its own prefix set, its own stabilizer "
            "built from signature blocks rather than filtered out of S_9, its "
            "own co-division relation, its own walk with its own coin and "
            "shift table, its own translations; no receipt read, no builder "
            "object consumed and no typed literal in common -- and requires "
            "each to equal the value the receipt publishes AND to occur in "
            "the head string.  Every number in the verdict is therefore "
            "twice-derived, including the five the delivered comparator had "
            "inherited from the builder"
            % len(indep),
            not missing and not disagree,
            "recomputed %d, absent from the head %s, disagreements %s"
            % (len(indep), missing or "none", disagree or "none"))
    SEAL.take("SEAL-VERDICT", R)
    SEAL.take("SEAL-COUNTS", R)
    say()
    for seg in R["verdict"]["segments"]:
        say(seg)
    return closing_battery(R, texts, paper_text, paper_rel, write)


# ===========================================================================
# SECTION 11.  THE VERDICT, ITS COMPARATOR, AND THE PAPER INSTRUMENT
# ===========================================================================

def verdict_segments(R, cross):
    st, cr, iv, co, cn = (R["stabilizer"], R["crystallization"],
                          R["invariance"], R["corpora"], R["counts"])
    mr = R["measure_relativity"]
    full = st["full_history_orders"]
    c3o = full["C3-R4-WINDOW"]
    chart_order = sorted(int(k) for k in c3o if int(k) > 1)
    refines = cross.get((True, True, False), 0)
    hides = cross.get((False, True, False), 0)
    ad = iv["admissibility"]
    tf = iv["two_fours"]
    fl = cr["information_floor"]
    ax = cr["order_axis"]
    sp = iv["split_by_test"]
    fam = co["prefix_objects_by_family"]
    s1 = ("AID-STRATIFIED-AT-THE-ADMISSIBILITY-AXIS-[IDENTITY FORCED AT THE "
          "GLOBAL-RELABELLING GRAIN ON %s OF %s COMMITTED HISTORIES, CHART ON "
          "%d -- ALL FOUR THE CONSTANT-CLASS QUADRUPLES, NONE I7-COVERING "
          "(%s OF %d CELLS), NONE G-FLAT; %d OF THE %d COVERING SCHEDULES AND "
          "%d OF THE %d G-FLAT QUADRUPLE HISTORIES IS CHART] -- CENSUS=C1 %d "
          "OF %d TRIVIAL | C2 %s OF %s TRIVIAL | C3 %s TRIVIAL AND %s AT "
          "ORDER %s WITH ORBIT SHAPE %s (%d INDEPENDENT: C2's %s ARE FORCED "
          "BY C1's %d UNDER THE PREFIX LAW) -- ROUTES=THE S_9 FILTER AND THE "
          "YOUNG SUBGROUP AGREE AT ORDER ON ALL %s DISTINCT PREFIXES OF THE "
          "FOUR DECLARED CORPORA AND AT ELEMENT SET ON %s, %d MISMATCHES"
          % (com(cn["forced_histories"]), com(cn["histories"]),
             cn["chart_histories"],
             ",".join(str(c) for c in ad["chart_history_cells_covered"]),
             ad["cells"], ad["chart_among_covering"], ad["covering_schedules"],
             ad["chart_among_flat_quadruple_histories"],
             ad["flat_quadruple_histories"],
             full["C1-R3-TRIPLES"].get("1", 0), co["C1-R3-TRIPLES"]["histories"],
             com(full["C2-R6-CONCATENATIONS"].get("1", 0)),
             com(co["C2-R6-CONCATENATIONS"]["histories"]),
             com(c3o.get("1", 0)),
             com(sum(v for k, v in c3o.items() if int(k) > 1)),
             chart_order[0] if chart_order else 0,
             ",".join(st["chart_orbit_shapes"]),
             cn["independent_histories"],
             com(co["C2-R6-CONCATENATIONS"]["histories"]),
             co["C1-R3-TRIPLES"]["histories"],
             com(st["distinct_prefixes"]), com(st["element_set_comparisons"]),
             st["route_order_mismatches"]))
    s2 = ("CRYSTALLIZATION=EXACTLY %s ON C1 AND, BY THE PREFIX LAW, ON C2 AND "
          "THE %s-HISTORY SEED FAN (UNIFORM, NOT AN AVERAGE) | C3 STRATIFIED "
          "%s | NEVER %d = THE CONSTANT-CLASS QUADRUPLES %s -- TWO OBJECTS, "
          "NAMED: THE SCHEDULE'S TIME IS %s AND THE INFORMATION FLOOR IS %d "
          "-- A COUNTING THEOREM (2^k >= %d) ATTAINED BY THE MINIMAL EVENT "
          "SUBSET AT %d OF %d AND %d OF %d, WITH ROUND ONE'S THIRD EVENT "
          "REDUNDANT AT %d OF %d AND CRYSTALLIZATION %d AT ALL %d WHEN IT IS "
          "MOVED TO THE END -- ORDER-AXIS=%s HISTORIES, TIME %s AND ONE "
          "PROFILE %s AT EVERY ONE -- PREFIX-LAW=A CONCATENATION "
          "CRYSTALLIZES EXACTLY WHEN ITS FIRST FACTOR DOES, %d DISAGREEMENTS "
          "OF %s; THE STABILIZER NEVER GROWS, %d GROWTH EVENTS IN %s "
          "PREFIXES"
          % (cr["constant_on_C1_C2_C1FAN"],
             com(co["C1FAN-SEED-FAN"]["histories"]),
             "|".join("%s:%s" % (k, v) for k, v in
                      sorted(cr["per_corpus"]["C3-R4-WINDOW"].items(),
                             key=lambda kv: (kv[0] == "never",
                                             int(kv[0]) if kv[0] != "never"
                                             else 0))),
             cr["never_crystallizing"],
             ",".join(cr["never_crystallizing_arrangements"]),
             cr["constant_on_C1_C2_C1FAN"],
             fl["counting_bound_ceil_log2_actors"], len(SITES),
             sum(fl["minimal_event_subset_C1"].values()),
             co["C1-R3-TRIPLES"]["histories"],
             sum(fl["minimal_event_subset_forced_C3"].values()),
             fl["forced_C3_histories"],
             fl["round_one_third_event_redundant"],
             co["C1-R3-TRIPLES"]["histories"],
             fl["counting_bound_ceil_log2_actors"],
             co["C1-R3-TRIPLES"]["histories"],
             com(ax["histories"]), ",".join(sorted(ax["times"])),
             "(%s)" % ", ".join(com(v) for v in ax["profile"]),
             cr["prefix_law_disagreements"],
             com(co["C2-R6-CONCATENATIONS"]["histories"]),
             cr["monotonicity_growth_events"],
             com(cr["monotonicity_prefixes_checked"])))
    s3 = ("INVARIANCE=SPLIT-BY-TEST-NOT-BY-OBSERVABLE -- TRANSPORTED READING: "
          "EVERY COMMITTED OBSERVABLE IS BLIND BY THEOREM.  A STABILIZER "
          "ELEMENT CARRIES THE LABELLED HISTORY TO ITSELF AT %s OF %s "
          "COMPARISONS, SO THE CO-DIVISION RELATION (%d VIOLATIONS OVER %s "
          "STABILIZER ELEMENTS AT %s OBJECTS), EVERY WELD-DICTIONARY READING "
          "(%s PARSE COMPARISONS AT THE IDENTITY PARSE AND %s OVER ALL %d "
          "DECLARED PARSES, %d DIFFERENCES), THE RECORD (%s COMPARISONS, %d "
          "VIOLATIONS) AND THE BORN MENU (%s COMPARISONS TO DEPTH TWO, %d "
          "VIOLATIONS) ARE ALIKE UNCHANGED -- FIXED READING: NO COMMITTED "
          "OBSERVABLE IS BLIND.  THE WELD'S OWN COUNT FIELD AND THE RECORD "
          "ARE ONE OBJECT AT THE IDENTITY PARSE, %d OF %s, AND BOTH ARE "
          "ORBIT-CONSTANT AT %d OF %s AT EVERY ONE OF THE %d PARSES -- "
          "NAMING-DEPENDENT AT %d -- WHILE THE DEPTH-TWO MENU FAILS AT %d -- "
          "SWAP THE TESTS AND THE VERDICTS SWAP: THE ONE MEASURED ORDERING "
          "BETWEEN OBSERVABLES IS DEPTH"
          % (com(sp["relabelled_history_comparisons"]
                 - sp["relabelled_history_differences"]),
             com(sp["relabelled_history_comparisons"]),
             iv["codivision_violations"], com(iv["stabilizer_elements"]),
             com(iv["nontrivial_objects"]), com(iv["weld_parse_comparisons"]),
             com(iv["weld_twelve_parse_comparisons"]), len(PARSES),
             iv["weld_twelve_parse_differences"],
             com(sp["transported_record_comparisons"]),
             sp["transported_record_violations"],
             com(sp["transported_menu_comparisons"]),
             sp["transported_menu_violations"],
             sp["weld_field_equals_the_record_at_the_identity_parse"],
             com(iv["nontrivial_objects"]), iv["record_orbit_constant"],
             com(iv["nontrivial_objects"]), len(PARSES),
             iv["record_naming_dependent"],
             sp["menu_attribution_depth_two_failures"]))
    s4 = ("DEPTH=THE MEASURED ORDERING, AND IT IS COIN-ORDER-RELATIVE "
          "(W-COIN, BOTH DECLARED ORDERS ENTIRE).  AT G.D THE BORN MENU IS "
          "BLIND AT %s BY DEPTH AND STRICTLY REFINES THE RECORD FROM DEPTH "
          "%d: %d OBJECTS THE RECORD CANNOT SEPARATE AND THE WALK CAN, %d "
          "THE RECORD SEPARATES AND THE ONE-STEP MENU CANNOT.  AT D.G IT IS "
          "BLIND AT %s AND REFINES ONLY FROM DEPTH %d, THE ONE-STEP MENU "
          "BEING BLIND EVERYWHERE AND THE DEPTH-TWO MENU COARSER THAN THE "
          "RECORD.  THE ORDER-INDEPENDENT CONTENT IS THE TAIL: %d UNDER BOTH "
          "ORDERS FROM DEPTH THREE -- WALK-SYMMETRIES=EXACTLY THE "
          "TRANSLATIONS (%d OF %s ELEMENTS; SHIFT-COMMUTING EQUALS "
          "TRANSLATION AT EVERY ONE, %d DISAGREEMENTS; RECORD-PRESERVING %s)"
          % (",".join(str(v) for v in iv["coin_order_ladder"]["G.D"]),
             iv["first_depth_strictly_finer_than_the_record"]["G.D"],
             refines, hides,
             ",".join(str(v) for v in iv["coin_order_ladder"]["D.G"]),
             iv["first_depth_strictly_finer_than_the_record"]["D.G"],
             iv["coin_order_common_tail"],
             iv["walk_symmetries"], com(iv["stabilizer_elements"]),
             iv["shift_translation_disagreements"],
             com(iv["record_preserving_elements"])))
    s5 = ("DEGENERACY=THE RELATION FORGETS WHAT THE EVENTS REMEMBER: AT %d OF "
          "%s R = 4 HISTORIES -- %d = 4!, THE ORDERINGS OF THE FOUR PARALLEL "
          "CLASSES -- THE CO-DIVISION RELATION IS THE CONSTANT COMPLETE GRAPH "
          "WITH AUTOMORPHISM GROUP %s WHILE THE STABILIZER OF THE EVENT SET "
          "IS TRIVIAL; STAB IS CONTAINED IN AUT WITH AN INDEX AND NEVER "
          "DISJOINT FROM IT -- ORDER=THE STABILIZER READS THE EVENT SET, %d "
          "CHANGES OVER %s CANONICALLY REORDERED PREFIXES, WHILE THE "
          "CRYSTALLIZATION TIME READS THE ORDER, MOVING AT %d OF %s "
          "SCHEDULES UNDER W-C3REV -- NO-RESONANCE=%d SCHEDULES ARE "
          "I7-COVERING AND %d CRYSTALLIZE AT %s AND THEY ARE NOT THE SAME "
          "SET (%d BOTH, %d AND %d ONE-SIDED), WHICH IS THIS UNIT'S OWN "
          "CONTROL AGAINST READING TWO EQUAL COUNTS AS A MECHANISM"
          % (iv["complete_relation_histories"],
             com(co["C3-R4-WINDOW"]["histories"]),
             iv["complete_relation_histories_are_the_class_orderings"],
             com(st["s9_order"]),
             st["set_reordering_changes"], com(st["distinct_prefixes"]),
             cr["reversal"]["crystallization_times_that_move"],
             com(cr["reversal"]["schedules"]),
             tf["covering"], tf["crystallize_at_the_constant"],
             cr["constant_on_C1_C2_C1FAN"], tf["both"],
             tf["covering_not_five"], tf["five_not_covering"]))
    s6 = ("SCOPE=THE GLOBAL-RELABELLING GRAIN ONLY; THE GROUPOID GRAIN "
          "REGISTERED AND NOT RUN; THE DECOMPOSITION GRAIN -- WHICH "
          "SUBSYSTEMS THERE ARE -- REGISTERED AS OWED AND UNTOUCHED, SO THIS "
          "UNIT ANSWERS NAMING AND NOT FACTORIZATION -- MEASURE=COUNTING-ONLY "
          "UNDER THREE DECLARED READINGS (E-24), THE MEASURE EFFECT SEPARATED "
          "FROM THE FAMILY EFFECT: THE RECORD'S BLIND FRACTION, BY DISTINCT "
          "PREFIX OVER THE THREE PRIMARY CORPORA, IS %s; BY CORPUS "
          "MULTIPLICITY OVER THE SAME THREE, %s; AND BY DISTINCT PREFIX OVER "
          "THE FOUR DECLARED CORPORA, %s; THE WALK'S %s AND %s -- FAMILIES=%s "
          "PREFIX OBJECTS AND %s DISTINCT OVER THE THREE PRIMARY CORPORA, %s "
          "AND %s OVER THE FOUR DECLARED -- GAUGE=THE LINK DECLARATION IS A "
          "CHOICE OF THREE OF THE FOUR PARALLEL CLASSES AND MOVES NO CENSUS "
          "NUMBER -- WINDOWS=%s, %d OF THEM ENTIRE CLASSES -- "
          "LANGUAGE=FORCED/CHART/STRATIFIED NAME THE STABILIZER AND THE "
          "INVARIANCE DATA AND NOTHING ELSE"
          % (mr["record_fraction_distinct_primary"],
             mr["record_fraction_multiplicity"],
             mr["record_fraction_distinct"],
             mr["walk_fraction_distinct"], mr["walk_fraction_multiplicity"],
             com(fam["THREE-PRIMARY"]["prefix_objects"]),
             com(fam["THREE-PRIMARY"]["distinct_prefixes"]),
             com(fam["FOUR-DECLARED"]["prefix_objects"]),
             com(fam["FOUR-DECLARED"]["distinct_prefixes"]),
             ",".join(w["name"] for w in R["windows"]),
             sum(1 for w in R["windows"] if w["entire"])))
    return [s1, s2, s3, s4, s5, s6]


def independent_head(R, C1, C2, C3, C1FAN, never):
    """THE COMPARATOR, DE-TWINNED (#292 m-1).  Every quantity below is
    recomputed from the CORPORA THEMSELVES by a route that shares no function
    and no literal with the builder.  Nothing here reads the receipt, and
    nothing here consumes a builder object: the prefix set is rebuilt, the
    stabilizer is the Young order of a freshly computed signature partition
    (never the S_9 filter the builder runs), the walk is re-implemented with
    its own coin matrix and its own shift table, the translations are rebuilt
    from the arena, and the co-division relation is rebuilt from the events.
    The five quantities the delivered comparator inherited -- the distinct
    prefixes, the stabilizer elements, the two walk-blindness counts and the
    walk symmetries -- are therefore twice-derived like the rest."""
    def blocks(H):
        d = {}
        for x in SITES:
            d.setdefault(tuple(F for F in H if x in F), []).append(x)
        return list(d.values())

    def order(H):
        n = 1
        for b in blocks(H):
            for i in range(2, len(b) + 1):
                n *= i
        return n

    def elements(H):
        """the stabilizer's ELEMENTS from the blocks, built not filtered."""
        idx = [[SITE_INDEX[x] for x in b] for b in blocks(H)]
        acc = [()]
        for blk in idx:
            acc = [a + tuple(zip(blk, pm)) for a in acc
                   for pm in permutations(blk)]
        out = []
        for a in acc:
            p = [0] * NACT
            for s, d in a:
                p[s] = d
            out.append(tuple(p))
        return out

    def first_trivial(H):
        for k in range(len(H)):
            if order(H[:k + 1]) == 1:
                return k + 1
        return None

    allH = list(C1) + list(C2) + list(C3)
    forced = sum(1 for H in allH if order(H) == 1)
    chart = len(allH) - forced
    ct = {first_trivial(H) for H in list(C1) + list(C2) + list(C1FAN)}
    # THE PREFIX SET, rebuilt here rather than taken from the builder
    pref = set()
    for H in allH + list(C1FAN):
        for k in range(1, len(H) + 1):
            pref.add(H[:k])
    ntp = [P for P in pref if order(P) > 1]
    nel = sum(order(P) for P in ntp)

    def cod(H):
        c = [[0] * NACT for _ in range(NACT)]
        for F in H:
            ix = [SITE_INDEX[x] for x in F]
            for a in ix:
                for b in ix:
                    if a != b:
                        c[a][b] += 1
        return c

    def rrows(H, c=None):
        c = cod(H) if c is None else c
        return [tuple(c[SITE_INDEX[x]][SITE_INDEX[vadd(x, l)]]
                      for l in I7_LINKS) for x in SITES]

    def const_on(H, vals):
        for b in blocks(H):
            if len({vals[SITE_INDEX[x]] for x in b}) > 1:
                return False
        return True

    # THE WALK, re-implemented: the coin as an explicit 3x3 numerator matrix
    # applied by row, the shift as a table this function builds for itself.
    shift = [0] * (NACT * len(I7_LINKS))
    for s in range(NACT):
        for i, l in enumerate(I7_LINKS):
            shift[s * len(I7_LINKS) + i] = (
                SITE_INDEX[vadd(SITES[s], l)] * len(I7_LINKS) + i)

    def menus(H, depth, c=None):
        n = [v for row in rrows(H, c) for v in row]
        psi = [(1, 0)] * len(n)
        out = []
        for _t in range(depth):
            post = [(0, 0)] * len(n)
            for s in range(NACT):
                b = s * len(I7_LINKS)
                for i in range(len(I7_LINKS)):
                    ar = ac = 0
                    for j in range(len(I7_LINKS)):
                        g = -1 if i == j else 2
                        u, v = psi[b + j]
                        w0, w1 = WPOW[n[b + j] % 3]
                        ar += g * (u * w0 - v * w1)
                        ac += g * (u * w1 + v * w0 - v * w1)
                    post[b + i] = (ar, ac)
            out.append([tuple(post[s * len(I7_LINKS) + i][0]
                              * post[s * len(I7_LINKS) + i][0]
                              - post[s * len(I7_LINKS) + i][0]
                              * post[s * len(I7_LINKS) + i][1]
                              + post[s * len(I7_LINKS) + i][1]
                              * post[s * len(I7_LINKS) + i][1]
                              for i in range(len(I7_LINKS)))
                        for s in range(NACT)])
            nxt = [(0, 0)] * len(n)
            for m in range(len(n)):
                nxt[shift[m]] = post[m]
            psi = nxt
        return out

    rblind = wblind1 = wblind2 = 0
    wsym = 0
    tr = {tuple(SITE_INDEX[vadd(SITES[i], d)] for i in range(NACT))
          for d in SITES}
    for P in ntp:
        c = cod(P)
        rw = rrows(P, c)
        if const_on(P, rw):
            rblind += 1
        m = menus(P, 2, c)
        if const_on(P, m[0]):
            wblind1 += 1
        if const_on(P, m[1]):
            wblind2 += 1
        for p in elements(P):
            if p in tr and all(rw[p[s]] == rw[s] for s in range(NACT)):
                wsym += 1
    comp = sum(1 for H in C3
               if len({cod(H)[a][b] for a in range(NACT)
                       for b in range(NACT) if a != b}) == 1)
    return {"forced_histories": forced, "chart_histories": chart,
            "histories": len(allH), "nontrivial_prefixes": len(ntp),
            "stabilizer_elements": nel, "record_blind": rblind,
            "walk_blind_depth1": wblind1, "walk_blind_depth2": wblind2,
            "walk_symmetries": wsym, "complete_relation_histories": comp,
            "never_crystallizing": sum(1 for H in allH
                                       if first_trivial(H) is None),
            "crystallization_constant": sorted(ct)[0] if len(ct) == 1 else -1,
            "distinct_prefixes": len(pref)}


def paper_claims(R):
    """EVERY TABLE AND EVERY LOAD-BEARING SENTENCE OF THE PAPER IS A CLAIM
    RENDERED FROM THE RECEIPT (#267 order: no claim is typed prose)."""
    st, cr, iv = R["stabilizer"], R["crystallization"], R["invariance"]
    co, cn, mr = R["corpora"], R["counts"], R["measure_relativity"]
    sp, ad, tf = iv["split_by_test"], iv["admissibility"], iv["two_fours"]
    fl, ax = cr["information_floor"], cr["order_axis"]
    gz = R["substrate"]["gauge_declaration"]
    tot = R["totals"]
    out = [
        ("CLAIM-CORPORA",
         "the three committed corpora carry %d, %s and %d histories"
         % (co["C1-R3-TRIPLES"]["histories"],
            com(co["C2-R6-CONCATENATIONS"]["histories"]),
            co["C3-R4-WINDOW"]["histories"])),
        # ONE UNIVERSE PER SENTENCE (#288 MAJOR-3 = #289 MINOR-1 = #292
        # MAJOR-1).  Both numerals of this claim are drawn from one family and
        # the family is NAMED inside the sentence; the other family's pair is
        # a second claim, so no sentence of the paper joins the two.
        ("CLAIM-PREFIXES",
         "%s prefix objects across the four declared corpora, %s of them "
         "distinct"
         % (com(co["prefix_objects_by_family"]["FOUR-DECLARED"]
                ["prefix_objects"]),
            com(co["prefix_objects_by_family"]["FOUR-DECLARED"]
                ["distinct_prefixes"]))),
        ("CLAIM-PREFIXES-PRIMARY",
         "%s prefix objects over the three primary corpora, %s of them "
         "distinct"
         % (com(co["prefix_objects_by_family"]["THREE-PRIMARY"]
                ["prefix_objects"]),
            com(co["prefix_objects_by_family"]["THREE-PRIMARY"]
                ["distinct_prefixes"]))),
        ("CLAIM-ROUTES",
         "the two stabilizer routes disagree at %d objects"
         % st["route_order_mismatches"]),
        ("CLAIM-FORCED",
         "identity is forced on %s histories and chart on %d"
         % (com(cn["forced_histories"]), cn["chart_histories"])),
        ("CLAIM-CRYSTAL",
         "the crystallization time is exactly %s on C1, C2 and the seed fan"
         % cr["constant_on_C1_C2_C1FAN"]),
        ("CLAIM-NEVER",
         "%d histories never crystallize, and they are the constant-class "
         "quadruples %s"
         % (cr["never_crystallizing"],
            ", ".join(cr["never_crystallizing_arrangements"]))),
        ("CLAIM-CODIVISION",
         "the co-division relation is preserved by every one of the %s "
         "stabilizer elements, at %d violations"
         % (com(iv["stabilizer_elements"]), iv["codivision_violations"])),
        ("CLAIM-WELD",
         "the weld dictionary's readings agree under precomposition at %s "
         "comparisons with %d differences"
         % (com(iv["weld_parse_comparisons"]), iv["weld_parse_differences"])),
        ("CLAIM-RECORD",
         "the record's attribution is orbit-constant at %d of %d objects and "
         "naming-dependent at %d"
         % (iv["record_orbit_constant"], iv["nontrivial_objects"],
            iv["record_naming_dependent"])),
        ("CLAIM-BORN",
         "the Born menu is orbit-constant at %s objects by depth"
         % ",".join(str(iv["born_orbit_constant_by_depth"][str(t)])
                    for t in range(1, WALK_DEPTH + 1))),
        ("CLAIM-SYMMETRY",
         "%d of the %s stabilizer elements are symmetries of the coupled "
         "step, exactly the translations"
         % (iv["walk_symmetries"], com(iv["stabilizer_elements"]))),
        ("CLAIM-DEGENERACY",
         "at %d of the %d R = 4 histories the co-division relation is the "
         "constant complete graph while the stabilizer is trivial"
         % (iv["complete_relation_histories"],
            co["C3-R4-WINDOW"]["histories"])),
        ("CLAIM-MEASURE",
         "the record's blind fraction is %s by distinct prefix over the four "
         "declared corpora, %s by distinct prefix over the three primary "
         "corpora, and %s by corpus multiplicity over the same three"
         % (mr["record_fraction_distinct"],
            mr["record_fraction_distinct_primary"],
            mr["record_fraction_multiplicity"])),
        ("CLAIM-GRAIN",
         "the groupoid grain is registered and not run"),
        ("CLAIM-DECOMPOSITION",
         "the decomposition grain is registered as owed and is not touched "
         "here"),
        ("CLAIM-SPLIT",
         "the weld's own count field is the record at the identity parse, at "
         "%d of %d objects, and both are orbit-constant at %d of %d at every "
         "one of the %d declared parses"
         % (sp["weld_field_equals_the_record_at_the_identity_parse"],
            iv["nontrivial_objects"], iv["record_orbit_constant"],
            iv["nontrivial_objects"], len(PARSES))),
        ("CLAIM-TRANSPORT",
         "a stabilizer element carries the labelled history to itself at %s "
         "of %s comparisons, at %d differences"
         % (com(sp["relabelled_history_comparisons"]
                - sp["relabelled_history_differences"]),
            com(sp["relabelled_history_comparisons"]),
            sp["relabelled_history_differences"])),
        ("CLAIM-WELD-TWELVE",
         "the weld dictionary's readings agree at all %d declared parses, at "
         "%s comparisons with %d differences"
         % (len(PARSES), com(iv["weld_twelve_parse_comparisons"]),
            iv["weld_twelve_parse_differences"])),
        ("CLAIM-COIN",
         "the Born menu is blind at %s by depth at coin order G.D and at %s "
         "at coin order D.G"
         % (",".join(str(v) for v in iv["coin_order_ladder"]["G.D"]),
            ",".join(str(v) for v in iv["coin_order_ladder"]["D.G"]))),
        ("CLAIM-FLOOR",
         "the smallest event subset that forces identity has size %d at all "
         "%d R = 3 histories and at all %d forced R = 4 histories"
         % (fl["counting_bound_ceil_log2_actors"],
            co["C1-R3-TRIPLES"]["histories"], fl["forced_C3_histories"])),
        ("CLAIM-REDUNDANT",
         "round one's third event is redundant at %d of %d, and moving it to "
         "the end of the sequence gives crystallization %d at all %d"
         % (fl["round_one_third_event_redundant"],
            co["C1-R3-TRIPLES"]["histories"],
            fl["counting_bound_ceil_log2_actors"],
            co["C1-R3-TRIPLES"]["histories"])),
        ("CLAIM-ORDER-AXIS",
         "over all %s histories of the full order axis the crystallization "
         "time is %s and the prefix profile is the same at every one"
         % (com(ax["histories"]), ",".join(sorted(ax["times"])))),
        ("CLAIM-SET",
         "the stabilizer is unchanged at every one of the %s distinct "
         "prefixes when the events are canonically reordered, while the "
         "crystallization time moves at %d of the %d R = 4 schedules"
         % (com(st["distinct_prefixes"]),
            cr["reversal"]["crystallization_times_that_move"],
            cr["reversal"]["schedules"])),
        ("CLAIM-ADMISSIBILITY",
         "%d of the %d covering schedules and %d of the %d G-FLAT quadruple "
         "histories is chart"
         % (ad["chart_among_covering"], ad["covering_schedules"],
            ad["chart_among_flat_quadruple_histories"],
            ad["flat_quadruple_histories"])),
        ("CLAIM-TWO-FOURS",
         "%d schedules are I7-covering and %d crystallize at %s, and they are "
         "not the same set: %d are both, %d cover without crystallizing at "
         "%s, %d crystallize at %s without covering"
         % (tf["covering"], tf["crystallize_at_the_constant"],
            cr["constant_on_C1_C2_C1FAN"], tf["both"], tf["covering_not_five"],
            cr["constant_on_C1_C2_C1FAN"], tf["five_not_covering"],
            cr["constant_on_C1_C2_C1FAN"])),
        ("CLAIM-GAUGE",
         "rebuilt with ANT in place of DIA the substrate returns %d "
         "saturating, %d I7-STRICT triples and %d G-FLAT quadruples, and the "
         "R = 3 census returns %d nontrivial prefixes with %d record-blind "
         "among them"
         % (gz["saturating"]["alternative"],
            gz["strict_triples"]["alternative"],
            gz["flat_quadruples"]["alternative"],
            gz["nontrivial_R3_prefixes"]["alternative"],
            gz["record_blind_R3_prefixes"]["alternative"])),
        # THE INSTRUMENT SENTENCE, RENDERED (#292 MAJOR-3(3)): every one of
        # these counts is bound to the NOUN it counts, so a swap of two of
        # them is a claim the paper no longer carries.
        ("CLAIM-INSTRUMENT",
         "%d falsifiers, each naming the object it corrupts and each verified "
         "against its own code; %d pinned sources whose bytes are "
         "digest-checked before anything is read; %d quote anchors bound to "
         "consumer gates; %d tables, all rendered above; %d declared windows; "
         "and %d reading walls"
         % (tot["mutants"], tot["sources"], tot["verbatim_anchors"],
            tot["paper_tables"], tot["windows"], tot["walls"])),
    ]
    return [{"id": k, "claim": v} for k, v in out]


def paper_tables(R):
    """THE PAPER'S TABLES, BUILT HERE AND RENDERED THERE (#267 order: every
    table row is gated, cell by cell, and none is typed in the paper)."""
    st, cr, iv, co = (R["stabilizer"], R["crystallization"], R["invariance"],
                      R["corpora"])
    T = {}
    T["T1-CORPORA"] = {
        "columns": ["corpus", "histories", "events per history", "window"],
        "rows": [[nm, com(co[nm]["histories"]),
                  str(co[nm]["events_per_history"]), co[nm]["window"]]
                 for nm in ("C1-R3-TRIPLES", "C1FAN-SEED-FAN",
                            "C2-R6-CONCATENATIONS", "C3-R4-WINDOW")],
    }
    T["T2-STABILIZER-ORDERS"] = {
        "columns": ["order", "distinct prefixes"],
        "rows": [[k, com(v)] for k, v in
                 sorted(st["nontrivial_orders"].items(), key=lambda kv:
                        int(kv[0]))],
    }
    T["T3-ORBIT-SHAPES"] = {
        "columns": ["orbit shape", "distinct prefixes"],
        "rows": [[k, com(v)] for k, v in
                 sorted(st["nontrivial_orbit_shapes"].items())],
    }
    T["T4-CRYSTALLIZATION"] = {
        "columns": ["corpus"] + sorted(
            {k for cc in cr["per_corpus"].values() for k in cc},
            key=lambda k: (k == "never", int(k) if k != "never" else 0)),
        "rows": [],
    }
    for nm in sorted(cr["per_corpus"]):
        row = [nm]
        for k in T["T4-CRYSTALLIZATION"]["columns"][1:]:
            row.append(com(cr["per_corpus"][nm].get(k, 0)))
        T["T4-CRYSTALLIZATION"]["rows"].append(row)
    T["T5-INVARIANCE"] = {
        "columns": ["observable", "verdict", "blind at", "of", "basis"],
        "rows": [
            ["co-division relation", "BLIND BY THEOREM",
             com(iv["nontrivial_objects"]), com(iv["nontrivial_objects"]),
             "%s element checks" % com(iv["stabilizer_elements"])],
            ["weld dictionary readings", "BLIND BY THEOREM",
             com(iv["nontrivial_objects"]), com(iv["nontrivial_objects"]),
             "%s parse comparisons" % com(iv["weld_parse_comparisons"])],
            ["record attribution n_l(x)", "NAMES",
             str(iv["record_orbit_constant"]),
             com(iv["nontrivial_objects"]), "orbit-constancy per object"],
            ["Born menu, depth 1", "NAMES",
             str(iv["born_orbit_constant_by_depth"]["1"]),
             com(iv["nontrivial_objects"]), "exact Z[w], symmetric start"],
            ["Born menu, depth 2", "NAMES",
             str(iv["born_orbit_constant_by_depth"]["2"]),
             com(iv["nontrivial_objects"]), "exact Z[w], symmetric start"],
        ],
    }
    T["T6-CROSS-TAB"] = {
        "columns": ["record blind", "menu blind at depth 1",
                    "menu blind at depth 2", "objects"],
        "rows": [[k.split("|")[0], k.split("|")[1], k.split("|")[2], com(v)]
                 for k, v in sorted(iv["cross_tab_record_born1_born2"].items())],
    }
    T["T7-STAB-VS-AUT"] = {
        "columns": ["stabilizer order", "co-division automorphism order",
                    "index", "objects"],
        "rows": [[com(int(k.split("/")[0])), com(int(k.split("/")[1])),
                  str(int(k.split("/")[1]) // int(k.split("/")[0])), com(v)]
                 for k, v in sorted(iv["stab_aut_pairs"].items(),
                                    key=lambda kv: (int(kv[0].split("/")[0]),
                                                    int(kv[0].split("/")[1])))],
    }
    T["T8-WINDOWS"] = {
        "columns": ["window", "entire", "declaration"],
        "rows": [[w["name"], str(w["entire"]), w["declaration"]]
                 for w in R["windows"]],
    }
    T["T15-WALLS"] = {
        "columns": ["wall", "banned forms", "statement"],
        "rows": [[w[0], str(len(w[2])), w[1]] for w in WALLS],
    }
    T["T9-DRIVEN"] = {
        "columns": ["window", "rounds", "events", "divisions", "maxhits",
                    "footprints equal groups"],
        "rows": [[r["window"], str(r["rounds"]), str(r["events"]),
                  str(r["divisions"]), str(r["maxhits"]),
                  str(r["footprints_equal_groups"])]
                 for r in R["driven"]["rows"]],
    }
    mr = R["measure_relativity"]
    T["T10-MEASURE"] = {
        "columns": ["quantity", "distinct prefix, four declared corpora",
                    "distinct prefix, three primary corpora",
                    "multiplicity, three primary corpora"],
        "rows": [
            ["nontrivial-stabilizer objects",
             com(mr["nontrivial_distinct"]),
             com(mr["nontrivial_distinct_primary"]),
             com(mr["nontrivial_with_multiplicity"])],
            ["record blind",
             com(mr["record_blind_distinct"]),
             com(mr["record_blind_distinct_primary"]),
             com(mr["record_blind_multiplicity"])],
            ["fraction, record",
             mr["record_fraction_distinct"],
             mr["record_fraction_distinct_primary"],
             mr["record_fraction_multiplicity"]],
        ],
    }
    T["T11-COIN-ORDER"] = {
        "columns": ["depth", "blind at G.D", "blind at D.G"],
        "rows": [[str(t), str(iv["coin_order_ladder"]["G.D"][t - 1]),
                  str(iv["coin_order_ladder"]["D.G"][t - 1])]
                 for t in range(1, WALK_DEPTH + 1)],
    }
    fam = co["prefix_objects_by_family"]
    T["T12-FAMILIES"] = {
        "columns": ["family", "corpora", "prefix objects", "distinct"],
        "rows": [[k, ", ".join(fam[k]["corpora"]),
                  com(fam[k]["prefix_objects"]),
                  com(fam[k]["distinct_prefixes"])]
                 for k in ("THREE-PRIMARY", "FOUR-DECLARED")],
    }
    T["T13-GRAINS"] = {
        "columns": ["grain", "object", "status"],
        "rows": [[g["grain"], g["object"], g["status"]]
                 for g in R["grain"]["grains"]],
    }
    T["T14-FLOOR"] = {
        "columns": ["quantity", "value"],
        "rows": [
            ["counting floor, ceil(log2 of the actors)",
             str(cr["information_floor"]["counting_bound_ceil_log2_actors"])],
            ["minimal event subset, R = 3 histories",
             ", ".join("%s at %s" % (k, com(v)) for k, v in
                       sorted(cr["information_floor"]
                              ["minimal_event_subset_C1"].items()))],
            ["minimal event subset, forced R = 4 histories",
             ", ".join("%s at %s" % (k, com(v)) for k, v in
                       sorted(cr["information_floor"]
                              ["minimal_event_subset_forced_C3"].items()))],
            ["round one's third event redundant",
             com(cr["information_floor"]["round_one_third_event_redundant"])],
            ["crystallization with it moved to the end",
             ", ".join("%s at %s" % (k, com(v)) for k, v in
                       sorted(cr["information_floor"]
                              ["crystallization_with_it_moved_to_the_end"]
                              .items()))],
            ["full order axis, histories",
             com(cr["order_axis"]["histories"])],
            ["full order axis, crystallization times",
             ", ".join("%s at %s" % (k, com(v)) for k, v in
                       sorted(cr["order_axis"]["times"].items()))],
        ],
    }
    return T


def markdown_table_rows(text):
    """the paper's own markdown table rows, cell by cell, canonicalised."""
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
SECREF = re.compile(r"(?:(RUNBOOK|HA|I7|E)\s*)?§\s*(\d+(?:\.\d+)*)")
# THE DECLARED NUMERAL EXEMPTIONS (#20's third list).  It is EMPTY: every
# numeral this paper carries is supplied by the run's own registry or by the
# receipt, and an exemption that never fires is a hole, not a licence.
NUMERAL_EXEMPTIONS = ()


THOUSANDS = re.compile(r"^\d{1,3}(?:,\d{3})*$")


def receipt_numbers(R):
    """the allow list is the receipt itself, never a hand-kept table.  Digest
    strings are EXCLUDED (#267 order: a token that exists only inside a
    sha256 hexadecimal is not a published number).  A COMMA LIST is excluded
    from the comma-stripping too: `703,128,58,58,58` is five numbers, not one,
    and stripping its commas would enter a twelve-digit token into the
    registry -- which is exactly the hole G-WHITELIST-DIGEST-FREE exists to
    refuse.  Only a properly thousands-grouped numeral is stripped."""
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
    for key in MEASURED_KEYS + ("provenance", "windows", "paper_tables",
                                "paper_claims", "totals", "coverage"):
        if key in R:
            walk(R[key])
    return out


FENCE_COPIES = 2


def paper_coverage(R, text):
    """#20 + E-22: EVERY numeral -- prose, tables, INLINE CODE SPANS and the
    fenced verdict blocks -- is allow-listed against exactly three declared
    lists: this run's registered numbers, the receipt it publishes, and a
    declared exemption table required to fire.  Spelled numerals are scanned
    on the same terms, and the fenced blocks are gated by MULTISET equality."""
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
    body = text if not mut("MUT-COVERAGE-SCAN") else FENCE.sub("", text)
    spans = re.findall(r"`[^`\n]+`", body)
    fenced = [t for blk in FENCE.findall(body) for t in NUMTOK.findall(blk)]
    inline = [t for sp in spans for t in NUMTOK.findall(sp)]
    heads = set(HEADNUM.findall(body))
    refs = SECREF.findall(body)
    dangling = sorted({n for owner, n in refs if not owner and n not in heads})
    body = SECREF.sub(" ", HEADNUM.sub("#### ", body))
    # THE SCAN'S OWN COVERAGE, MEASURED: the reference count is taken over the
    # WHOLE paper with the same section-number substitutions and NO fence or
    # span removal, so a scanner that strips anything is caught by arithmetic
    # rather than by hoping an unbacked numeral happens to live there.
    reference = len(NUMTOK.findall(
        SECREF.sub(" ", HEADNUM.sub("#### ", text))))
    scanned, unbacked, fired = 0, [], Counter()
    for tok in NUMTOK.findall(body):
        scanned += 1
        if tok in allow or tok.replace(",", "") in allow:
            continue
        if tok in exempt_lits:
            fired[tok] += 1
            continue
        unbacked.append(tok)
    words, word_unbacked = 0, []
    for wd in WORDTOK.findall(canon(body).lower()):
        if wd not in WORDNUM:
            continue
        words += 1
        if str(WORDNUM[wd]) in allow or com(WORDNUM[wd]) in allow:
            continue
        if wd in exempt_lits:
            fired[wd] += 1
            continue
        word_unbacked.append(wd)
    suppliable = sorted(e[0] for e in exempt
                        if e[0] in allow or e[0].replace(",", "") in allow)
    if mut("MUT-PAPER-FENCE-MULTISET"):
        seg = R["verdict"]["segments"][0]
        text = text.replace(seg, seg.replace("FORCED", "FORGED"), 1)
    want = Counter({canon(seg): FENCE_COPIES
                    for seg in R["verdict"]["segments"]})
    got = Counter(canon(b) for b in FENCE.findall(text))
    return {"numerals_scanned": scanned,
            "numerals_in_the_whole_paper": reference,
            "scan_is_total": scanned == reference,
            "unbacked": sorted(set(unbacked)),
            "fenced_blocks_scanned": len(FENCE.findall(body)),
            "fenced_numerals_scanned": len(fenced),
            "inline_spans_scanned": len(spans),
            "inline_span_numerals_scanned": len(inline),
            "inline_span_unbacked": sorted({t for t in inline
                                            if t not in allow
                                            and t.replace(",", "") not in allow
                                            and t not in exempt_lits}),
            "fenced_unbacked": sorted({t for t in fenced if t not in allow
                                       and t.replace(",", "") not in allow
                                       and t not in exempt_lits}),
            "word_numerals_scanned": words,
            "word_numerals_unbacked": sorted(set(word_unbacked)),
            "section_headings": sorted(heads),
            "section_references": len(refs),
            "section_references_dangling": dangling,
            "registry_size": len(allow),
            "registry_digest_free": all(not re.match(r"^[0-9a-f]{12}$", a)
                                        for a in allow),
            "declared_exemptions": [{"literal": e[0], "reason": e[1],
                                     "occurrences": fired[e[0]]}
                                    for e in exempt],
            "exemptions_that_never_fire": sorted(e[0] for e in exempt
                                                 if not fired[e[0]]),
            "exemptions_the_receipt_could_supply": suppliable,
            "fence_copies_declared": FENCE_COPIES,
            "fenced_block_multiset_matches": got == want,
            "fenced_blocks_expected": sum(want.values())}


def paper_polarity(R, text, mutated=False):
    """the paper must not assert the OPPOSITE of a measured fate."""
    iv, cr = R["invariance"], R["crystallization"]
    probes = [
        ("the record's attribution is naming-dependent",
         "the record is invariant under every stabilizer element"),
        ("identity is forced on all but four committed histories",
         "no committed history forces identity"),
        ("the co-division relation is stabilizer-blind",
         "the co-division relation distinguishes stabilizer-equivalent "
         "actors"),
        ("the walk refines the record from depth two",
         "the walk sees strictly less than the record at every depth"),
        ("the groupoid grain is registered and not run",
         "this unit measures the groupoid grain"),
    ]
    hay = text + (" no committed history forces identity" if mutated else "")
    viol = [neg for _pos, neg in probes if canon(neg) in canon(hay)]
    return {"probes": [p[0] for p in probes], "violations": viol,
            "record_naming_dependent": iv["record_naming_dependent"],
            "never_crystallizing": cr["never_crystallizing"]}


# the arena's own small constants: budgets, link counts and round indices.
# Anything else appearing as a literal in a naming function is a COUNT the
# receipt could have supplied, and G-NO-TYPED-COUNTS refuses it.
ARENA_LITERALS = ("1", "2", "3", "4", "5", "6", "9")

WALLS = [
    # NOTE.  A wall statement may not contain its own banned forms: the walls
    # scan the paper, and the paper renders these statements.  Each is written
    # to say what it refuses without uttering it.
    ("WALL-REALITY",
     "THE REALITY LANGUAGE IS CONFINED TO THE MEASURED FORM.  This unit "
     "publishes a stabilizer census and an invariance census; it asserts "
     "nothing about what the nine are beyond those two measurements, and it "
     "draws no conclusion of that kind from them.",
     ("actors are real", "actors are not real", "actors do not exist",
      "proves that actors", "therefore actors are", "actors are ontology",
      "are ontology for", "is ontology for", "the actors really",
      "actors really are", "genuinely are", "are ontically",
      "ontically forced", "what actors really", "truly real",
      "genuine individuals", "really are threads", "are real threads")),
    ("WALL-ARCHITECTURE",
     "THE ARCHITECTURE READING IS REFUSED, ON THE MEASUREMENT'S OWN "
     "EVIDENCE.  The split this unit measures is a split between the two "
     "TESTS and not between the observables.  Five readings are therefore "
     "banned in this paper: assigning one kind of observable to matter and "
     "another to space; calling the actor decomposition forced rather than "
     "the labelling; stating the thread-attribution result without the "
     "stratum it was measured on; calling the two freedoms disjoint where "
     "the census measures containment with an index; and registering a "
     "numeral co-incidence as a mechanism.",
     ("ontology for matter", "chart for space", "identity for matter",
      "space identity-blind", "matter identity-sighted",
      "space is identity-blind", "matter is identity-sighted",
      "the factorization is forced", "factorization is forced",
      "is not a property of a thread", "freedoms are disjoint",
      "freedom are disjoint", "is a resonance", "the resonance between",
      "resonates with")),
    ("WALL-GRAIN",
     "THE GROUPOID GRAIN WAS NOT MEASURED.  No sentence may report a result "
     "at the mid-history thread-swap grain.",
     ("we measure the groupoid", "the groupoid census", "groupoid grain was "
      "measured", "at the groupoid grain we find")),
    ("WALL-MEASURE",
     "NO FRACTION WITHOUT ITS MEASURE (E-24).  Every fraction over a "
     "configuration space carries the measure it was taken under or the "
     "COUNTING-ONLY stamp.",
     ("the probability that a history", "with probability", "on average a "
      "history", "typically a history")),
    ("WALL-SCOPE",
     "THE CORPORA ARE COMMITTED OBJECTS, NOT A SAMPLE OF PHYSICS.  No "
     "sentence may generalise the census beyond the declared windows.",
     ("for every possible history", "in general histories", "all histories "
      "whatsoever", "this holds for arbitrary", "every conceivable history",
      "generalises to arbitrary", "true of every history", "of any corpus",
      "arbitrary corpora", "for all corpora")),
]

# THE POSITIVE LEG OF THE WALLS (#292 MAJOR-3(c)).  A ban list can only refuse
# the forms it lists; a paraphrase walks past it.  So the walls also carry a
# POSITIVE rule: any sentence of the paper that puts an ACTOR word in the same
# sentence as a word of the REALITY REGISTER must be one of the wall
# statements themselves -- which the run renders and the paper carries
# verbatim -- and nothing else.  A near-miss falsifier proves the rule fires
# on paraphrase and not only on a listed string.
ACTOR_WORDS = ("actor", "actors")
REALITY_REGISTER = ("real", "really", "realer", "genuine", "genuinely",
                    "truly", "exist", "exists", "existence", "ontology",
                    "ontological", "ontologically", "ontic", "ontically",
                    "metaphysical", "metaphysics", "substance", "individuals",
                    "individual")
SENT_SPLIT = re.compile(r"(?<=[.;])\s+")


def sentences(text):
    return [s.strip() for s in SENT_SPLIT.split(canon(text)) if s.strip()]


def prose_only(text):
    """the paper's PROSE: markdown table rows removed.  The positive wall leg
    reads prose because every table row is already bound cell for cell to the
    run's own multiset at G-PAPER-TABLES, so no sentence can be planted in a
    table; the BANNED-FORM leg still reads the whole paper, tables included."""
    return "\n".join(ln for ln in text.split("\n")
                     if not ln.strip().startswith("|"))


def wall_positive(text, allowed):
    """every sentence pairing an actor word with the reality register must be
    an allowed (run-rendered) sentence; the rest are violations."""
    out = []
    for s in sentences(prose_only(text)):
        low = s.lower()
        toks = set(re.findall(r"[a-z]+", low))
        if not (toks & set(ACTOR_WORDS)) or not (toks & set(REALITY_REGISTER)):
            continue
        if s in allowed:
            continue
        out.append(s[:120])
    return out


ANCHOR_FLOOR = 20


def claim_contradictions(claims, text):
    """THE TWO-WAY LEG (#292 MAJOR-3(2)).  Every paper gate asks whether the
    paper carries what the run computed; this one asks whether the paper
    carries anything the run did NOT.  For each rendered claim the text up to
    its first numeral is an ANCHOR; every occurrence of that anchor in the
    paper must be followed by the claim's own numeral.  A forged sentence that
    repeats a claim's opening and then states a different number -- the exact
    shape of a planted contradiction -- is caught even though every numeral it
    carries is individually backed.  The comparison is CASE-FOLDED: a planted
    sentence that opens a paragraph carries a capital where the rendered claim
    carries a lower-case letter, and a case-sensitive anchor would walk past
    exactly the plant this leg exists to catch."""
    hay = canon(text).lower()
    rows, viol = [], []
    for c in claims:
        cc = canon(c["claim"]).lower()
        m = NUMTOK.search(cc)
        if not m:
            continue
        anchor, want = cc[:m.start()], m.group(0)
        if len(anchor) < ANCHOR_FLOOR:
            rows.append({"claim": c["id"], "anchor": anchor,
                         "bound": False, "occurrences": 0, "conflicts": 0})
            continue
        occ = bad = 0
        i = hay.find(anchor)
        while i >= 0:
            occ += 1
            m2 = NUMTOK.match(hay[i + len(anchor):])
            if not m2 or m2.group(0) != want:
                bad += 1
            i = hay.find(anchor, i + 1)
        rows.append({"claim": c["id"], "anchor": anchor[:80], "bound": True,
                     "occurrences": occ, "conflicts": bad})
        if bad:
            viol.append("%s(%d)" % (c["id"], bad))
    return rows, viol


def noun_bindings(totals, text):
    """the instrument's counts bound to the NOUNS they count, in digits and in
    words alike (#292 MAJOR-3(3)): a numeral standing immediately before one
    of these nouns must be that noun's own total."""
    pairs = (("reading walls", totals["walls"]),
             ("declared windows", totals["windows"]),
             ("falsifiers", totals["mutants"]),
             ("pinned sources", totals["sources"]),
             ("quote anchors", totals["verbatim_anchors"]),
             ("tables", totals["paper_tables"]))
    hay = canon(text).lower()
    rows, viol = [], []
    for noun, want in pairs:
        occ = bad = 0
        for m in re.finditer(r"([a-z]+|\d[\d,]*)\s+%s" % re.escape(noun.lower()),
                             hay):
            tok = m.group(1)
            low = tok.lower()
            if low in WORDNUM:
                got = WORDNUM[low]
            elif re.match(r"^\d[\d,]*$", tok):
                got = int(tok.replace(",", ""))
            else:
                continue
            occ += 1
            if got != want:
                bad += 1
        rows.append({"noun": noun, "count": want, "occurrences": occ,
                     "conflicts": bad})
        if bad:
            viol.append("%s(%d)" % (noun, bad))
    return rows, viol


def template_constants(src, names):
    """the TEMPLATE text the naming functions type: their string constants
    less docstrings and format specs.  #267 order: no COUNT may be typed."""
    tree = ast.parse(src)
    bad = []
    for fn in ast.walk(tree):
        if not (isinstance(fn, ast.FunctionDef) and fn.name in names):
            continue
        doc = ast.get_docstring(fn, clean=False)
        for n in ast.walk(fn):
            if not isinstance(n, ast.Constant) or not isinstance(n.value, str):
                continue
            if doc is not None and n.value == doc:
                continue
            for tok in re.findall(r"(?<![A-Za-z_\-\d])\d[\d,]*(?![A-Za-z_\d])",
                                  n.value):
                if tok in ARENA_LITERALS:
                    continue        # the arena's own small constants
                bad.append((fn.name, tok))
    return bad


# ===========================================================================
# SECTION 12.  THE CLOSING BATTERY (#267 CHECKLIST IN FULL)
# ===========================================================================

MUTANTS = [
    ("MUT-BACKVAL", "G-BACK-VALIDATION",
     "reports one I7-STRICT triple short of the measured len(strict), so this "
     "run's substrate disagrees with paper-19's committed receipt",
     "len(strict)"),
    ("MUT-PARTITION", "G-PARTITION-ROUTE",
     "reports nparts + 1 groupings, so the enumeration and the closed form "
     "disagree", "nparts"),
    ("MUT-VERBATIM", "G-VERBATIM",
     "declares the first anchor's quote absent from its source's bytes",
     "hit"),
    ("MUT-RULE", "G-FOOTPRINT-RULE",
     "reports the proposer union absent from d42b1's regs_of source",
     "rule['has_proposer_union']"),
    ("MUT-DRIVEN", "G-DRIVEN-EQUALS-COMBINATORIAL",
     "declares the first driven footprint sequence unequal to its "
     "combinatorial history", "same"),
    ("MUT-MAXHITS", "G-MAXHITS-IMMUNITY",
     "reports a driven maxhits of 2, so the v10 tie-break would be reachable",
     "r['maxhits']"),
    ("MUT-REFUSED", "G-CTRL-REFUSED",
     "reports no refusal from the supply-starved control drive",
     "b_ref.refusal"),
    ("MUT-EXIT", "G-LAYERS-CANNOT-EXIT",
     "declares d42b1's module slice not exit-free", "G.slice_exit_free"),
    ("MUT-ROUTES", "G-STAB-ROUTES",
     "reports one order mismatch between the S_9 filter and the Young "
     "subgroup", "len(routes_bad)"),
    ("MUT-CHART", "G-FORCED-PER-HISTORY",
     "adds one to the chart-history count, so the per-history verdict and "
     "the recount disagree", "chart_hist"),
    ("MUT-CRYS", "G-CRYSTALLIZATION",
     "reports the constant crystallization time as 4 rather than the "
     "measured value", "c1t[0]"),
    ("MUT-PREFIX", "G-PREFIX-LAW",
     "declares one concatenation's crystallization time different from its "
     "first factor's", "pref_bad"),
    ("MUT-NEVER", "G-NEVER-CRYSTALLIZING",
     "adds one to the count of never-crystallizing arrangements",
     "len(nev_names)"),
    ("MUT-CODIV", "G-CODIVISION-BLIND",
     "reports one co-division violation under a stabilizer element",
     "len(cod_bad)"),
    ("MUT-WELDREAD", "G-WELD-DICTIONARY",
     "reports one count-field difference under precomposition", "cf_bad"),
    ("MUT-RECINV", "G-RECORD-ATTRIBUTION",
     "raises the record's orbit-constant count to the whole object set, so "
     "the measured non-invariance vanishes", "rec_ok"),
    ("MUT-SHIFT", "G-SHIFT-IS-TRANSLATION",
     "injects one disagreement between the shift test and the translation "
     "test", "sym_bad"),
    ("MUT-BORN", "G-BORN-MENU",
     "reports every stabilizer element a symmetry of the coupled step",
     "nsym"),
    ("MUT-DEGENERACY", "G-CODIVISION-FORGETS",
     "reports zero complete-relation histories", "deg"),
    ("MUT-WALK", "G-WALK-ARENA",
     "reports DIM + 1 walk cells, so the arena and the cell list disagree",
     "DIM"),
    ("MUT-E24", "G-E24-MEASURE",
     "makes the distinct-prefix fraction equal the multiplicity fraction, so "
     "measure-relativity would be unmeasured", "f_dist"),
    ("MUT-GRAIN", "G-GRAIN-REGISTERED",
     "declares the groupoid successor absent from the registered note",
     "'groupoid' in groupoid_note"),
    ("MUT-COMPARATOR", "G-VERDICT-RECONSTRUCTED",
     "injects a comparator disagreement, so the twice-derived head fails",
     "disagree"),
    ("MUT-CLAIM", "G-PAPER-CLAIMS",
     "corrupts the first rendered claim's text before the paper is searched "
     "for it", "claims[0]['claim']"),
    ("MUT-TABLE", "G-PAPER-TABLES",
     "corrupts one cell of one rendered table row before the paper is "
     "searched for it", "want_rows[0]"),
    ("MUT-HEAD", "G-PAPER-HEAD-VERBATIM",
     "corrupts the head string the paper is required to carry verbatim",
     "head"),
    ("MUT-COVERAGE-SCAN", "G-PAPER-COVERAGE",
     "strips fenced blocks before the numeral scan, the #20 defect this era "
     "closed", "text"),
    # #292 MAJOR-4: this falsifier is DECLARED at the gate that consumes the
    # flag it corrupts.  The multiset flag is computed in `paper_coverage` and
    # read by G-PAPER-HEAD-VERBATIM, which is where the mutant dies.
    ("MUT-PAPER-FENCE-MULTISET", "G-PAPER-HEAD-VERBATIM",
     "forges one copy of the verdict fence, which a containment test would "
     "pass and the multiset test catches", "text"),
    ("MUT-EXEMPTION-DEAD", "G-PAPER-COVERAGE",
     "adds a declared numeral exemption that occurs nowhere in the paper",
     "exempt"),
    ("MUT-POLARITY", "G-PAPER-CLAIM-POLARITY",
     "appends a sentence asserting the opposite of a measured fate to the "
     "text the polarity probes read", "mutated"),
    ("MUT-WALL", "G-WALLS-SCAN-THE-PAPER",
     "inserts a banned wall sentence into the text the walls scan",
     "wall_text"),
    ("MUT-TYPED", "G-NO-TYPED-COUNTS",
     "adds a typed count to the scanned template constants", "typed"),
    ("MUT-TRANSCRIPT", "G-TRANSCRIPT-INTEGRITY",
     "alters one staged transcript line after the seal is taken", "staged"),
    ("MUT-SEAL-DROP", "G-SEAL-TOTALITY",
     "drops the coverage seal from the manifest, so the manifest is no "
     "longer total", "self.rows"),
    ("MUT-WINDOW", "G-WINDOWS-DISCLOSED",
     "reports one fewer distinct window name than declared, so the window "
     "list would carry a duplicate", "len({w[0] for w in WINDOW_DECL})"),
    ("MUT-CORPUS-SHAPE", "G-CORPORA-SHAPE",
     "declares the 3R division-event shape false at some history",
     "all(len(H) == 3 * (len(s))"),
    ("MUT-ORDER", "G-EVENT-SHAPE",
     "reports zero distinct seed-fan orderings, so the history would be a "
     "set rather than a sequence", "len({H for H in C1FAN})"),
    ("MUT-MONOTONE", "G-MONOTONE",
     "injects one stabilizer-growth event into the monotonicity scan",
     "mono_bad"),
    ("MUT-SHORTCUT", "G-AUT-SHORTCUT",
     "reports the enumerated automorphism count as 1, so the constant-weight "
     "forcing would be unconfirmed", "shortcut_ok"),
    ("MUT-DIGEST-WHITELIST", "G-WHITELIST-DIGEST-FREE",
     "declares the numeral registry to contain digest tokens",
     "pc['registry_digest_free']"),
    ("MUT-SPELLED", "G-SPELLED-NUMERALS",
     "reports zero spelled numerals scanned, the blindness this order "
     "closes", "pc['word_numerals_scanned']"),
    ("MUT-FINAL", "G-PAPER-COVERAGE-FINAL",
     "reports zero numerals scanned by the in-run paper instrument",
     "R['paper_coverage']['numerals_scanned']"),
    ("MUT-SWEEP", "G-SWEEP-BOUND",
     "injects a survivor into the sweep's execution record",
     "R['mutant_sweep']['survivors']"),
    ("MUT-PROFILE", "G-PREFIX-PROFILE",
     "declares the fourth and fifth events not transversals of the first "
     "round, so the measured mechanism would be unbacked", "transversal"),
    ("MUT-BORNLAW", "G-BORN-DEPTH-ONE-LAW",
     "reports one collision in the residue-to-menu map, so the depth-one law "
     "would fail", "modbad"),
    ("MUT-GATECOUNT", "G-GATE-ACCOUNTING",
     "reports zero gates after the receipt snapshot, so the published total "
     "would silently drop the closing gates and their verdicts would reach no "
     "artifact unnoticed", "len(GATES_AFTER_THE_RECEIPT_SNAPSHOT)"),
    ("MUT-FALSIFIER-DESC", "G-FALSIFIER-HONEST",
     "replaces the first mutant's declared corrupted object by a name that "
     "occurs nowhere in this file", "mrows[0]['corrupts']"),
    # ---- the falsifiers of the measurements this repair added -------------
    ("MUT-GAUGE", "G-GAUGE-DECLARATION",
     "reports a disagreement between the declared link triple and the ANT-"
     "for-DIA rebuild, so the gauge equivalence would be unmeasured", "goff"),
    ("MUT-FAMILY", "G-PREFIX-FAMILIES",
     "makes the three-primary distinct-prefix count equal the four-declared "
     "one, so the two families would be indistinguishable and a sentence "
     "could join them", "len(fam_primary)"),
    ("MUT-SETFN", "G-STABILIZER-READS-THE-SET",
     "injects one prefix whose stabilizer changes under canonical event "
     "reordering, so the stabilizer would read the order", "set_order_bad"),
    ("MUT-ORDERAXIS", "G-ORDER-AXIS",
     "reports two distinct crystallization times over the full order axis, "
     "so the constant would not be order-independent", "len(axis_t)"),
    ("MUT-FLOOR", "G-INFORMATION-FLOOR",
     "reports the minimal event subset one below the counting bound, so the "
     "floor would be unattained", "sorted(floor_c1)"),
    ("MUT-REVERSAL", "G-TIME-READS-THE-ORDER",
     "reports zero crystallization times moving under the declared order "
     "reversal, so the order would enter nowhere", "rev_moved"),
    ("MUT-WELD12", "G-WELD-TWELVE-PARSES",
     "reports one count-field difference over the twelve declared parses",
     "p12_bad"),
    ("MUT-COINORDER", "G-COIN-ORDER",
     "reports the D.G blind ladder equal to the G.D one, so the coin order "
     "would be verdict-irrelevant", "ladder['D.G']"),
    ("MUT-ADMISS", "G-ADMISSIBILITY-AXIS",
     "reports one chart history among the covering schedules, so the "
     "admissibility axis would not be the axis", "chart_cov"),
    ("MUT-FIVES", "G-TWO-FOURS-ARE-NOT-ONE",
     "adds one to the covering count so that the two equal counts would "
     "differ, dissolving the unit's own control", "n_cov"),
    ("MUT-SPLIT", "G-INVARIANCE-SPLIT",
     "reports the weld's count field nowhere equal to the record at the "
     "identity parse, so the split would look like a split between "
     "observables", "weld_is_record"),
    ("MUT-TABLE-EXTRA", "G-PAPER-TABLES",
     "appends a forged EXTRA table row to the paper's rows whose numerals are "
     "all individually backed, which only the multiset test refuses",
     "got_rows"),
    ("MUT-CONTRADICTION", "G-PAPER-CONTRADICTION",
     "appends to the scanned paper a claim-shaped sentence that repeats a "
     "claim's opening and states the opposite number", "contra_text"),
    ("MUT-WALLPOS", "G-WALLS-SCAN-THE-PAPER",
     "declares the positive wall leg to have found an unallowed "
     "reality-register sentence", "stray"),
    ("MUT-WALL-PARAPHRASE", "G-WALLS-SCAN-THE-PAPER",
     "inserts into the scanned paper a reality overclaim that contains NONE "
     "of the banned forms, so only the positive leg can refuse it",
     "wall_text"),
    ("MUT-SEAL-GATE", "G-SEAL-TOTALITY",
     "declares one seal's gate never to have run, the phantom-consumer "
     "defect this repair closed", "seal_phantom"),
    ("MUT-SWEEP-GATE", "G-SWEEP-BOUND",
     "declares one swept mutant to have died away from the gate it names",
     "off_gate"),
]
MUTANT_NAMES = [m[0] for m in MUTANTS]

# the gates that necessarily run AFTER the gate ledger is snapshotted: they
# are named here, counted in the coverage denominator, and their execution is
# checked at G-SEAL-TOTALITY rather than assumed.
CLOSING_GATE_NAMES = ("G-PAPER-COVERAGE-FINAL", "G-SWEEP-BOUND",
                      "G-GATE-ACCOUNTING", "G-TRANSCRIPT-INTEGRITY",
                      "G-SEAL-TOTALITY", "G-ARTIFACT-INTEGRITY")
# #292 MAJOR-5.  Two facts about where a gate's VERDICT can live.  The gates
# below run after the receipt's gate list is snapshotted, so their rows reach
# the receipt through `closing_gate_verdicts` (covered by the payload digest,
# declared unsealed) and reach the transcript directly, because the transcript
# is built from the emitted lines AFTER they run.
GATES_AFTER_THE_RECEIPT_SNAPSHOT = ("G-TRANSCRIPT-INTEGRITY",
                                    "G-SEAL-TOTALITY")
# And exactly one gate can be in NEITHER artifact: the one that certifies the
# bytes of both.  It cannot appear inside the file it hashes.  That is a
# structural necessity and it is declared here rather than left to be found.
GATES_OUTSIDE_BOTH_ARTIFACTS = ("G-ARTIFACT-INTEGRITY",)

WAIVERS = [
    ("G-PROVENANCE",
     "MACHINE-CHECKED FORCING: this gate's falsifier is the CLI's own "
     "`--selftest`, which corrupts one declared anchor's digest and requires "
     "the run to die here and write nothing.  It is an executable falsifier "
     "rather than a registry mutant because it must run before the mutant "
     "harness itself is trusted."),
    ("G-ARTIFACT-INTEGRITY",
     "MACHINE-CHECKED FORCING: a mutant of this gate would have to WRITE "
     "artifacts, which the era forbids of a failing run, so the falsifier is "
     "carried INSIDE the gate instead -- the same disk-vs-seal comparison is "
     "run a second time on the same disk bytes with one bit flipped and is "
     "required to REJECT.  The gate therefore fires in both directions in "
     "every plain run."),
]


def norm_src(s):
    """source compared as source: whitespace collapsed and quoting ignored, so
    a declaration written with one quote style matches code written with the
    other."""
    return re.sub(r"\s+", "", s).replace('"', "").replace("'", "")


def mutant_hooks(src):
    """E-23: every falsifier's HOOK, located by AST, together with the source
    of the statement that carries it, so a reader checks the declared
    corruption against the code and not against a sentence about the code."""
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
                 and isinstance(node.args[1], ast.Constant)
                 and isinstance(node.args[1].value, bool))
        out.setdefault(node.args[0].value, []).append(
            {"kind": f.id, "line": node.lineno,
             "source": re.sub(r"\s+", " ", text).strip(),
             "constant_boolean": const})
    return out


def closing_battery(R, texts, paper_text, paper_rel, write):
    """THE PAPER INSTRUMENT AND THE #267 CHECKLIST, IN THE PLAIN RUN."""
    say()
    say("SECTION 11.  THE PAPER INSTRUMENT AND THE CLOSING BATTERY")
    src = read_text(SELF, "SELF")
    ppath = os.path.join(REPO, paper_rel)
    disk_paper = (read_text(ppath, "PAPER-UNDER-TEST")
                  if os.path.exists(ppath) else "")
    if paper_text is None:
        paper_text = disk_paper
    # the tables and the totals are built BEFORE the claims, because the
    # instrument sentence is itself a rendered claim over the totals (#292
    # MAJOR-3(3)) and a claim may never carry a number the run has not closed.
    R["paper_tables"] = paper_tables(R)
    R["totals"] = {
        "sources": len(SOURCES),
        "mutants": len(MUTANTS),
        "verbatim_anchors": len(VERBATIM),
        "windows": len(WINDOW_DECL),
        "walls": len(WALLS),
        "paper_tables": len(R["paper_tables"]),
        "paper_table_rows": sum(len(t["rows"])
                                for t in R["paper_tables"].values()),
    }
    R["paper_claims"] = paper_claims(R)
    R["totals"]["paper_claims"] = len(R["paper_claims"])
    claims = R["paper_claims"]
    if mut("MUT-CLAIM") and claims:
        claims = [dict(c) for c in claims]
        claims[0]["claim"] = claims[0]["claim"] + " -- forged"
    miss = [c["id"] for c in claims if not match_needle(paper_text, c["claim"])]
    LD.gate("G-PAPER-CLAIMS",
            "EVERY LOAD-BEARING SENTENCE OF THE PAPER IS RENDERED FROM THE "
            "RECEIPT, NOT TYPED (#267 order).  The %d claims below are built "
            "from measured values in this run and each is required to occur "
            "in the paper under the #125 normalisation; a claim the paper "
            "does not carry kills the run" % len(claims),
            not miss, "claims %d, missing %s" % (len(claims), miss or "none"))
    want_rows = []
    want_multi = Counter()
    for tname, tbl in sorted(R["paper_tables"].items()):
        want_multi[tuple(canon(str(c)) for c in tbl["columns"])] += 1
        for row in tbl["rows"]:
            r = [canon(str(c)) for c in row]
            want_rows.append(r)
            want_multi[tuple(r)] += 1
    if mut("MUT-TABLE") and want_rows:
        want_rows = [list(r) for r in want_rows]
        want_rows[0] = want_rows[0][:-1] + ["forged"]
        want_multi = Counter(tuple(r) for r in want_rows)
    got_rows = markdown_table_rows(paper_text)
    if mut("MUT-TABLE-EXTRA"):
        got_rows = got_rows + [[canon("4"), canon("24"), canon("6"),
                                canon("60")]]
    got_set = [tuple(r) for r in got_rows]
    got_multi = Counter(got_set)
    unrendered = [r for r in want_rows
                  if not any(all(c in row for c in r) for row in got_set)]
    surplus = sorted(r for r in (got_multi - want_multi))
    deficit = sorted(r for r in (want_multi - got_multi))
    LD.gate("G-PAPER-TABLES",
            "ALL %d TABLES RENDER, ROW BY ROW AND CELL BY CELL, AND THE "
            "BINDING IS TWO-WAY (#267 order; #292 MAJOR-3(1)).  Every row of "
            "every receipt table must appear as a markdown table row of the "
            "paper with every one of its cells present -- and the MULTISET of "
            "the paper's own table rows must equal the multiset the run "
            "built, header rows included, exactly as E-22 already compares "
            "the verdict fences.  A forged EXTRA row whose numerals are all "
            "individually backed is therefore refused: the paper carries %d "
            "table rows against %d required, %d unrendered, %d surplus and "
            "%d missing"
            % (len(R["paper_tables"]), len(got_rows),
               len(want_rows) + len(R["paper_tables"]), len(unrendered),
               len(surplus), len(deficit)),
            not unrendered and not surplus and not deficit,
            "required rows %d + %d headers, paper rows %d, unrendered %d, "
            "surplus %s, missing %s"
            % (len(want_rows), len(R["paper_tables"]), len(got_rows),
               len(unrendered), surplus[:2] or "none", deficit[:2] or "none"))
    head = R["verdict"]["head"]
    if mut("MUT-HEAD"):
        head = head.replace("FORCED", "FORGED", 1)
    head_ok = all(match_needle(paper_text, seg)
                  for seg in R["verdict"]["segments"]) and (
                      canon(head) in canon(paper_text.replace("\n", " ")))
    R["paper_coverage"] = paper_coverage(R, paper_text)
    pc = R["paper_coverage"]
    LD.gate("G-PAPER-HEAD-VERBATIM",
            "THE PAPER'S VERDICT BLOCK IS THIS RUN'S HEAD, BYTE FOR BYTE.  "
            "Every one of the %d segments is matched against the paper as "
            "written, the whole head is matched as one string, and the fenced "
            "blocks are compared as a MULTISET against the declared %d copies "
            "(E-22) -- a second forged copy cannot hide behind a clean one"
            % (len(R["verdict"]["segments"]), FENCE_COPIES),
            head_ok and pc["fenced_block_multiset_matches"],
            "segments matched %s, multiset matched %s, fenced blocks %d"
            % (head_ok, pc["fenced_block_multiset_matches"],
               pc["fenced_blocks_scanned"]))
    LD.gate("G-PAPER-COVERAGE",
            "EVERY NUMERAL IN THE PAPER IS BACKED -- PROSE, TABLES, INLINE "
            "CODE SPANS AND FENCED BLOCKS ALIKE (#20 + E-22).  %s numerals "
            "scanned of which %d inside %d inline spans and %d inside %d "
            "fenced blocks, %s spelled numerals scanned, against a registry "
            "of %s tokens plus %d declared exemptions each of which must "
            "fire.  THE SCAN'S OWN COVERAGE IS GATED: the count is compared "
            "with a reference taken over the whole paper with nothing "
            "removed, so a scanner that strips fences or spans fails by "
            "arithmetic.  Unbacked: %s"
            % (com(pc["numerals_scanned"]), pc["inline_span_numerals_scanned"],
               pc["inline_spans_scanned"], pc["fenced_numerals_scanned"],
               pc["fenced_blocks_scanned"], com(pc["word_numerals_scanned"]),
               com(pc["registry_size"]), len(pc["declared_exemptions"]),
               pc["unbacked"] or "none"),
            pc["scan_is_total"] and pc["fenced_numerals_scanned"] > 0
            and pc["inline_span_numerals_scanned"] > 0
            and not pc["unbacked"] and not pc["fenced_unbacked"]
            and not pc["inline_span_unbacked"]
            and not pc["word_numerals_unbacked"]
            and not pc["exemptions_that_never_fire"]
            and not pc["exemptions_the_receipt_could_supply"]
            and not pc["section_references_dangling"],
            "scanned %d of %d (total %s), unbacked %s, fenced %s, inline %s, "
            "spelled %s, dead exemptions %s, suppliable %s, dangling refs %s"
            % (pc["numerals_scanned"], pc["numerals_in_the_whole_paper"],
               pc["scan_is_total"], pc["unbacked"], pc["fenced_unbacked"],
               pc["inline_span_unbacked"], pc["word_numerals_unbacked"],
               pc["exemptions_that_never_fire"],
               pc["exemptions_the_receipt_could_supply"],
               pc["section_references_dangling"]))
    LD.gate("G-WHITELIST-DIGEST-FREE",
            "THE NUMERAL WHITELIST CARRIES NO DIGEST TOKENS (#267 order).  A "
            "twelve-character hexadecimal that exists only inside a sha256 "
            "is not a published number, and allowing it would let any "
            "12-digit numeral through; the receipt walk skips digest strings "
            "and the resulting registry of %s tokens is checked to contain "
            "none" % com(pc["registry_size"]),
            pick("MUT-DIGEST-WHITELIST", pc["registry_digest_free"], False),
            "registry %d tokens, digest-free %s"
            % (pc["registry_size"], pc["registry_digest_free"]))
    LD.gate("G-SPELLED-NUMERALS",
            "SPELLED NUMERALS ARE SCANNED ON THE SAME TERMS, INCLUDING ABOVE "
            "TWELVE (#267 order).  The word list carries %d entries and %s "
            "spelled numerals were read out of the paper; every one is backed "
            "by the run's own registry or by a declared exemption"
            % (len(WORDNUM), com(pc["word_numerals_scanned"])),
            pick("MUT-SPELLED", pc["word_numerals_scanned"], 0) > 0
            and not pc["word_numerals_unbacked"] and len(WORDNUM) > 12,
            "word list %d, scanned %d, unbacked %s"
            % (len(WORDNUM), pc["word_numerals_scanned"],
               pc["word_numerals_unbacked"] or "none"))
    R["polarity"] = paper_polarity(R, paper_text, mutated=mut("MUT-POLARITY"))
    LD.gate("G-PAPER-CLAIM-POLARITY",
            "THE PAPER NEVER ASSERTS THE OPPOSITE OF A MEASURED FATE.  %d "
            "probes, each the negation of a measurement this run published, "
            "are searched for in the paper under the #125 normalisation"
            % len(R["polarity"]["probes"]),
            not R["polarity"]["violations"],
            "probes %d, violations %s" % (len(R["polarity"]["probes"]),
                                          R["polarity"]["violations"] or "none"))
    # ---- THE TWO-WAY LEG: contradictions and noun binding ------------------
    contra_text = paper_text
    if mut("MUT-CONTRADICTION"):
        contra_text = contra_text + (
            "\n\nthe record's attribution is orbit-constant at 703 of 703 "
            "objects.\n")
    crows, cviol = claim_contradictions(claims, contra_text)
    nrows, nviol = noun_bindings(R["totals"], contra_text)
    bound = sum(1 for r in crows if r["bound"])
    R["paper_binding"] = {
        "claim_anchors": crows, "claim_conflicts": cviol,
        "noun_bindings": nrows, "noun_conflicts": nviol,
        "anchor_floor": ANCHOR_FLOOR,
    }
    LD.gate("G-PAPER-CONTRADICTION",
            "THE PAPER MAY NOT CARRY WHAT THE RUN DID NOT COMPUTE (#292 "
            "MAJOR-3(2) and (3)).  Every other paper gate asks whether the "
            "paper carries the run's claims; this one asks the converse in "
            "two ways.  ANCHORS: for each of the %d rendered claims whose "
            "text before its first numeral is at least %d characters, every "
            "occurrence of that text in the paper must be followed by the "
            "claim's OWN numeral -- %d claims bound, %d conflicts -- so a "
            "sentence that repeats a claim's opening and then states a "
            "different number is refused even though every numeral it "
            "carries is individually backed.  NOUNS: the instrument's own "
            "counts are bound to the nouns they count, in digits and in "
            "spelled words alike, at %d declared nouns and %d conflicts"
            % (len(claims), ANCHOR_FLOOR, bound, len(cviol), len(nrows),
               len(nviol)),
            not cviol and not nviol and bound > 0,
            "claims %d, bound %d, claim conflicts %s, noun conflicts %s"
            % (len(claims), bound, cviol or "none", nviol or "none"))
    SEAL.take("SEAL-PAPER-BINDING", R)
    # ---- #267 M1: THE WALLS MUST SCAN THE PAPER ---------------------------
    wall_text = paper_text
    if mut("MUT-WALL"):
        wall_text = wall_text + "\n\nWe measure the groupoid census here.\n"
    if mut("MUT-WALL-PARAPHRASE"):
        wall_text = wall_text + (
            "\n\nThe census therefore shows the nine are not a chart at all "
            "but persisting individuals, and that each actor is as much a "
            "thing as the sites it occupies.\n")
    allowed = set()
    for _n, statement, _b in WALLS:
        allowed |= set(sentences(statement))
    wrows, wviol = [], []
    for name, statement, banned in WALLS:
        hits = [b for b in banned if canon(b) in canon(wall_text)]
        wrows.append({"wall": name, "statement": statement,
                      "banned_forms": len(banned), "hits": hits,
                      "scanned_characters": len(wall_text)})
        wviol += [(name, h) for h in hits]
    stray = wall_positive(wall_text, allowed)
    LD.gate("G-WALLS-SCAN-THE-PAPER",
            "THE READING WALLS SCAN THE PAPER ITSELF, AND THEY HAVE A "
            "POSITIVE LEG (#267 MAJOR-1; #288 MINOR-1; #292 MAJOR-3(c)).  "
            "Each of the %d walls holds a list of BANNED FORMS -- %d in all "
            "-- and is evaluated against the %s characters of the paper under "
            "test, not against a label and not against this file.  A ban list "
            "refuses only what it lists, so the POSITIVE rule carries the "
            "rest: every PROSE sentence of the paper that puts an ACTOR word "
            "in the same sentence as a word of the declared reality register "
            "(%d words) must be one of the wall statements the run itself "
            "renders -- %d such sentences are allowed and nothing else is.  "
            "The positive leg reads prose because every table row is already "
            "bound cell for cell to the run's own multiset, so nothing can be "
            "planted in a table; the banned-form leg reads the whole paper.  "
            "A paraphrase that carries no banned string is therefore refused "
            "too, and a declared near-miss falsifier proves it"
            % (len(WALLS), sum(len(w[2]) for w in WALLS), com(len(wall_text)),
               len(REALITY_REGISTER), len(allowed)),
            not wviol and len(wall_text) > 0
            and not pick("MUT-WALLPOS", stray, ["FORGED"]),
            "walls %d, characters scanned %d, banned-form violations %s, "
            "unallowed reality-register sentences %s"
            % (len(WALLS), len(wall_text), wviol or "none",
               stray[:1] or "none"))
    R["walls"] = wrows
    R["walls_positive"] = {
        "actor_words": list(ACTOR_WORDS),
        "reality_register": list(REALITY_REGISTER),
        "allowed_sentences": sorted(allowed),
        "unallowed": stray,
    }
    SEAL.take("SEAL-WALLS", R)
    SEAL.take("SEAL-WALLS-POSITIVE", R)
    # ---- #267 M3: NO TYPED COUNTS -----------------------------------------
    typed = template_constants(src, ("verdict_segments", "paper_claims",
                                     "paper_tables"))
    if mut("MUT-TYPED"):
        typed = typed + [("verdict_segments", "4242")]
    LD.gate("G-NO-TYPED-COUNTS",
            "NO COUNT THIS UNIT PUBLISHES IS TYPED (#267 MAJOR-3).  The "
            "string constants of the three functions that write the head, the "
            "claims and the tables are scanned by AST; every multi-digit "
            "literal found there would be a count the receipt could have "
            "supplied, and there are %d of them" % len(typed),
            not typed, "typed literals %s" % (typed or "none"))
    # ---- E-23: THE FALSIFIER SURFACE, VERIFIED AGAINST ITS OWN CODE -------
    hooks = mutant_hooks(src)
    mrows = [{"name": m[0], "gate": m[1], "what": m[2], "corrupts": m[3]}
             for m in MUTANTS]
    mrows[0]["corrupts"] = pick("MUT-FALSIFIER-DESC", mrows[0]["corrupts"],
                                "NO-SUCH-OBJECT-IN-THIS-FILE")
    ebad = []
    for r in mrows:
        hs = hooks.get(r["name"], [])
        r["hook_lines"] = [h["line"] for h in hs]
        r["hook_source"] = hs[0]["source"] if hs else None
        r["constant_boolean_falsifier"] = any(h["constant_boolean"] for h in hs)
        key = norm_src(r["corrupts"])
        r["description_matches_code"] = bool(hs) and any(
            key in norm_src(h["source"]) for h in hs)
        if (not hs or not r["description_matches_code"]
                or r["constant_boolean_falsifier"]):
            ebad.append(r["name"])
    LD.gate("G-FALSIFIER-HONEST",
            "EVERY FALSIFIER'S PUBLISHED DESCRIPTION IS VERIFIED AGAINST ITS "
            "OWN CODE, AND NO FALSIFIER IS A CONSTANT BOOLEAN (E-23, both "
            "legs; #292 m-2).  Each of the %d mutants names the object it "
            "corrupts; the hook is located by AST, its statement's source is "
            "published in the receipt, and the named object is required to "
            "occur in that source.  A description-inverted mutant is a false "
            "waiver wearing a green badge, and a mutant whose hook replaces a "
            "measured value by a LITERAL True or False tests the literal and "
            "not the measurement -- %d of the %d are constant-boolean, and "
            "the gate now refuses them rather than merely publishing the flag"
            % (len(mrows), sum(1 for r in mrows
                               if r["constant_boolean_falsifier"]),
               len(mrows)),
            not ebad, "mutants %d, descriptions not matching code or "
            "constant-boolean %s" % (len(mrows), ebad or "none"))
    R["mutants"] = mrows
    # ---- coverage, reachability and the sweep -----------------------------
    gate_names = [g["gate"] for g in LD.rows] + list(CLOSING_GATE_NAMES)
    covered = {m[1] for m in MUTANTS}
    uncovered = sorted(set(gate_names) - covered
                       - {w[0] for w in WAIVERS})
    dead = sorted(covered - set(gate_names))
    R["coverage"] = {
        "gates": len(gate_names),
        "gates_distinct": len(set(gate_names)),
        "mutants": len(MUTANTS),
        "gates_with_a_mutant": len(covered & set(gate_names)),
        "uncovered": uncovered,
        "mutants_naming_a_gate_that_never_runs": dead,
        "declared_consumers": len({v[3] for v in VERBATIM}
                                  | {s[2] for s in SEALED_PATHS}),
        "declared_consumers_checked_at": "G-SEAL-TOTALITY, where the gate "
                                         "ledger is complete",
        "waived": [{"gate": w[0], "waiver": w[1]} for w in WAIVERS],
        "honest_denominator": len(set(gate_names)),
    }
    LD.gate("G-COVERAGE",
            "THE COVERAGE LEDGER IS TAKEN AGAINST AN HONEST DENOMINATOR "
            "(#34).  This run evaluated %d gates (%d distinct); %d of them "
            "carry a declared falsifier and %d carry a named waiver; every "
            "mutant names a gate this run actually reaches, so no falsifier "
            "points at dead code.  The %d distinct consumer gates named by "
            "the quote anchors and by the seal manifest are checked the same "
            "way at G-SEAL-TOTALITY, where the ledger is complete -- this "
            "gate runs too early to see the last rows, which is exactly the "
            "error that let a phantom consumer stand"
            % (len(gate_names), len(set(gate_names)),
               len(covered & set(gate_names)), len(WAIVERS),
               len({v[3] for v in VERBATIM} | {s[2] for s in SEALED_PATHS})),
            not uncovered and not dead,
            "uncovered %s, mutants naming unreachable gates %s"
            % (uncovered or "none", dead or "none"))
    SEAL.take("SEAL-PAPER-CLAIMS", R)
    SEAL.take("SEAL-PAPER-TABLES", R)
    SEAL.take("SEAL-PAPER-COVERAGE", R)
    SEAL.take("SEAL-POLARITY", R)
    SEAL.take("SEAL-COVERAGE", R)
    R["waiver_ledger"] = [
        {"gate": w[0], "waiver": w[1],
         "forcing": "the run cannot proceed past a source whose bytes do not "
                    "match the frozen digest, so the gate has no other value "
                    "to take"} for w in WAIVERS]
    R["reachability"] = {
        "mutants": len(MUTANTS),
        "gates_reached_by_a_mutant": len(covered & set(gate_names)),
        "every_mutant_reaches_its_gate": not dead,
        "note": "a gate no execution path evaluates is dead code and may not "
                "appear as waived (#34 with reachability)",
    }
    LD.gate("G-REACHABILITY",
            "EVERY FALSIFIER REACHES ITS GATE (#34 with reachability).  Each "
            "of the %d mutants names a gate that this plain run evaluates; "
            "the sweep below runs every one of them and requires it to die at "
            "the gate it names, with the artifacts unchanged"
            % len(MUTANTS),
            not dead and len(covered & set(gate_names)) == len(covered),
            "mutants %d, gates reached %d, unreachable %s"
            % (len(MUTANTS), len(covered & set(gate_names)), dead or "none"))
    tree = ast.parse(src)
    floats = [n for n in ast.walk(tree)
              if isinstance(n, ast.Constant) and isinstance(n.value, float)]
    truediv = [n for n in ast.walk(tree) if isinstance(n, ast.BinOp)
               and isinstance(n.op, ast.Div)]
    LD.gate("G-EXACT-ARITHMETIC",
            "EXACT ARITHMETIC, SCANNED RATHER THAN PROMISED.  An AST scan of "
            "this file finds no float literal and no true division anywhere; "
            "every quotient is a Fraction or an integer floor division, and "
            "the Born weights are rational integers by construction",
            not floats and not truediv,
            "float literals %d, true divisions %d"
            % (len(floats), len(truediv)))
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
    declared = sorted(os.path.abspath(os.path.join(REPO, s[1]))
                      for s in SOURCES)
    actual = sorted(READS_BY_CATEGORY.get("SOURCE", set()))
    LD.gate("G-READS-DECLARED",
            "EVERY RUNTIME READ IS DECLARED, BY VALUE AND NOT BY POSITION "
            "(#46/#91).  The SOURCE category is compared as a SET OF "
            "ABSOLUTE PATHS against the frozen declaration -- %d against "
            "%d -- and the only other reads are this file itself and the "
            "paper under test.  No ledger, no STATUS file and no other "
            "unit's working file is read"
            % (len(actual), len(declared)),
            actual == declared
            and sorted(READS_BY_CATEGORY) == sorted(READ_CATEGORIES),
            "source reads %d, declared %d, categories %s"
            % (len(actual), len(declared), sorted(READS_BY_CATEGORY)))
    R["arithmetic"] = "exact: Python integers, Fraction, and Z[w] as pairs"
    R["python"] = "%d.%d" % sys.version_info[:2]
    return R, src, paper_text


def finish(R, src, write=True, swept=False):
    """THE TRANSCRIPT, THE SEAL MANIFEST AND THE WRITE (#119 + #148)."""
    R["closing_gates"] = {
        "names": list(CLOSING_GATE_NAMES),
        "after_the_receipt_snapshot": list(GATES_AFTER_THE_RECEIPT_SNAPSHOT),
        "outside_both_artifacts": list(GATES_OUTSIDE_BOTH_ARTIFACTS),
        "warrant": "the transcript is sealed WHOLE, the manifest is total, "
                   "the paper instrument runs inside the plain run, and the "
                   "artifacts are compared against the gate-time seal rather "
                   "than re-derived from disk",
        "where_the_verdicts_live": "every gate verdict this run reaches "
                                   "appears in BOTH artifacts, except the "
                                   "two that necessarily follow the receipt's "
                                   "gate snapshot -- which reach the receipt "
                                   "through closing_gate_verdicts and the "
                                   "transcript directly -- and except "
                                   "G-ARTIFACT-INTEGRITY, which certifies the "
                                   "bytes of both and cannot appear inside "
                                   "either",
    }
    R["closing_gate_verdicts"] = []
    R["mutant_sweep"] = {"swept": swept, "mutants": len(MUTANTS),
                         "rows": list(SWEEP_ROWS),
                         "survivors": [r["mutant"] for r in SWEEP_ROWS
                                       if not r["died_at"]
                                       or not r["artifacts_unchanged"]]}
    LD.gate("G-PAPER-COVERAGE-FINAL",
            "THE PAPER INSTRUMENT RAN INSIDE THIS RUN (#20).  The coverage, "
            "polarity, claim and table ledgers above were produced by the "
            "plain run and are sealed here, so no separate verification pass "
            "can drift from the artifacts this run writes: %s numerals, %d "
            "claims and %d table rows"
            % (com(R["paper_coverage"]["numerals_scanned"]),
               len(R["paper_claims"]), R["totals"]["paper_table_rows"]),
            pick("MUT-FINAL", R["paper_coverage"]["numerals_scanned"], 0) > 0
            and len(R["paper_claims"]) > 0,
            "numerals %d, claims %d, rows %d"
            % (R["paper_coverage"]["numerals_scanned"], len(R["paper_claims"]),
               R["totals"]["paper_table_rows"]))
    SEAL.take("SEAL-MUTANTS", R)
    SEAL.take("SEAL-WAIVERS", R)
    SEAL.take("SEAL-REACHABILITY", R)
    off_gate = pick("MUT-SWEEP-GATE",
                    [r["mutant"] for r in SWEEP_ROWS
                     if not r["at_the_declared_gate"]], ["FORGED"])
    LD.gate("G-SWEEP-BOUND",
            "THE MUTANT SWEEP IS EXECUTION-BOUND, NOT A LIST, AND EACH "
            "MUTANT MUST DIE AT THE GATE IT NAMES (E-23; #292 MAJOR-4).  The "
            "sweep row published here is the record of runs this process "
            "actually performed: %d mutants declared, %d executed in this "
            "process, %d survivors and %d that died away from the gate they "
            "declare.  A mutant that dies SOMEWHERE is not evidence that the "
            "gate it names has teeth -- the delivered sweep had one such "
            "row -- so the declared gate is carried into the execution record "
            "and compared.  A plain run publishes an empty execution list "
            "rather than a claim, and the --sweep run publishes the rows"
            % (len(MUTANTS), len(SWEEP_ROWS),
               len(R["mutant_sweep"]["survivors"]), len(off_gate)),
            not pick("MUT-SWEEP", R["mutant_sweep"]["survivors"], ["FORGED"])
            and not off_gate and len(SWEEP_ROWS) in (0, len(MUTANTS)),
            "declared %d, executed %d, survivors %s, away from the declared "
            "gate %s"
            % (len(MUTANTS), len(SWEEP_ROWS),
               R["mutant_sweep"]["survivors"] or "none", off_gate or "none"))
    SEAL.take("SEAL-MUTANT-SWEEP", R)
    rows_before = len(LD.rows)
    after_n = pick("MUT-GATECOUNT", len(GATES_AFTER_THE_RECEIPT_SNAPSHOT), 0)
    in_receipt = rows_before + 1 + after_n
    R["totals"]["gates_in_the_receipt_snapshot"] = rows_before + 1
    R["totals"]["gates_after_the_receipt_snapshot"] = after_n
    R["totals"]["gates_outside_both_artifacts"] = len(
        GATES_OUTSIDE_BOTH_ARTIFACTS)
    R["totals"]["gates_total"] = in_receipt + len(GATES_OUTSIDE_BOTH_ARTIFACTS)
    R["totals"]["seals"] = len(SEALED_PATHS)
    LD.gate("G-GATE-ACCOUNTING",
            "THE GATE COUNT IS ONE NUMBER WITH ONE DEFINITION, AND EVERY "
            "VERDICT REACHES AN ARTIFACT (#267 MAJOR-3; #292 MAJOR-5).  This "
            "gate is the last one whose row the receipt's `gates` list can "
            "carry, because that list is snapshotted the moment it passes: %d "
            "rows.  The %d gates that necessarily follow reach the receipt "
            "through `closing_gate_verdicts` and reach the transcript "
            "directly, because the transcript is built from the emitted lines "
            "after they run.  Exactly %d gate certifies the bytes of both "
            "artifacts and can therefore appear in neither.  %d gates in all, "
            "and no other gate count appears anywhere in this unit's receipt, "
            "transcript or paper"
            % (rows_before + 1, after_n, len(GATES_OUTSIDE_BOTH_ARTIFACTS),
               R["totals"]["gates_total"]),
            after_n == len(GATES_AFTER_THE_RECEIPT_SNAPSHOT)
            and R["totals"]["gates_total"]
            == rows_before + 1 + len(GATES_AFTER_THE_RECEIPT_SNAPSHOT)
            + len(GATES_OUTSIDE_BOTH_ARTIFACTS)
            and not ((set(GATES_AFTER_THE_RECEIPT_SNAPSHOT)
                      | set(GATES_OUTSIDE_BOTH_ARTIFACTS))
                     & {r["gate"] for r in LD.rows}),
            "snapshot %d, after %d, outside both %d, total %d"
            % (rows_before + 1, after_n, len(GATES_OUTSIDE_BOTH_ARTIFACTS),
               R["totals"]["gates_total"]))
    R["gates"] = [dict(r) for r in LD.rows]
    if len(R["gates"]) != R["totals"]["gates_in_the_receipt_snapshot"]:
        raise GateFail("G-GATE-ACCOUNTING :: the snapshot the accounting "
                       "predicted (%d) is not the snapshot taken (%d)"
                       % (R["totals"]["gates_in_the_receipt_snapshot"],
                          len(R["gates"])))
    SEAL.take("SEAL-GATES", R)
    SEAL.take("SEAL-CLOSING", R)
    SEAL.take("SEAL-TOTALS", R)
    # THE TRANSCRIPT IS STAGED WHOLE: every line this run emitted, digested at
    # seal time; the staged copy is what reaches disk (#267 MAJOR-5).
    staged = list(LINES)
    if mut("MUT-TRANSCRIPT"):
        staged = staged[:-1] + [staged[-1] + " forged"]
    gate_lines = [ln.strip()[7:] for ln in staged
                  if ln.strip().startswith("[PASS] ")
                  or ln.strip().startswith("[FAIL] ")]
    R["transcript_head"] = {
        "lines_at_staging": len(staged),
        "first": LINES[0] if LINES else "",
        "last": LINES[-1] if LINES else "",
        "whole_transcript_sha256_12": digest("\n".join(LINES)),
        "staged_transcript_sha256_12": digest("\n".join(staged)),
        "gate_verdict_lines_at_staging": len(gate_lines),
        "gate_rows_in_the_receipt_snapshot": len(R["gates"]),
        "written_after_staging": list(GATES_AFTER_THE_RECEIPT_SNAPSHOT),
        "outside_both_artifacts": list(GATES_OUTSIDE_BOTH_ARTIFACTS),
        "sealed": "the WHOLE transcript emitted to this point, not a head "
                  "prefix; the two gates that follow are emitted into the "
                  "file itself, which is built from the lines after they run",
    }
    SEAL.take("SEAL-TRANSCRIPT", R)
    LD.gate("G-TRANSCRIPT-INTEGRITY",
            "THE TRANSCRIPT IS SEALED WHOLE AND CARRIES A VERDICT LINE FOR "
            "EVERY GATE ROW THE RECEIPT CARRIES (#267 MAJOR-5; #292 "
            "MAJOR-5).  The digest published is taken over ALL %s transcript "
            "lines this run has emitted, and the STAGED lines -- the bytes "
            "that will reach disk -- are digested separately and required to "
            "be identical, so a forged staged line beside a byte-perfect "
            "receipt cannot be promoted.  The second leg is new: the staged "
            "transcript carries %d verdict lines against the receipt's %d "
            "gate rows, name for name, so neither artifact can be a prefix of "
            "the other's ledger.  The bytes finally written are re-checked "
            "against this requirement immediately before the write"
            % (com(len(staged)), len(gate_lines), len(R["gates"])),
            R["transcript_head"]["whole_transcript_sha256_12"]
            == R["transcript_head"]["staged_transcript_sha256_12"]
            and [g["gate"] for g in R["gates"]] == gate_lines,
            "lines %d, whole %s, staged %s, verdict lines %d, gate rows %d"
            % (len(staged),
               R["transcript_head"]["whole_transcript_sha256_12"],
               R["transcript_head"]["staged_transcript_sha256_12"],
               len(gate_lines), len(R["gates"])))
    missing, extra = SEAL.totality()
    published = sorted(k for k in R if k not in DECLARED_UNSEALED)
    sealed_paths = {r["path"] for r in SEAL.rows}
    unsealed = sorted(k for k in published if k not in sealed_paths)
    ran = {g["gate"] for g in LD.rows}
    closing_absent = [g for g in CLOSING_GATE_NAMES
                      if g not in ran and g != "G-ARTIFACT-INTEGRITY"
                      and g != "G-SEAL-TOTALITY"]
    seal_phantom = pick("MUT-SEAL-GATE",
                        sorted(({r["sealed_at_gate"] for r in SEAL.rows}
                                | {v[3] for v in VERBATIM})
                               - ran - set(GATES_OUTSIDE_BOTH_ARTIFACTS)),
                        ["FORGED"])
    del ran
    LD.gate("G-SEAL-TOTALITY",
            "THE SEAL MANIFEST IS TOTAL, AND EVERY SEAL'S DECLARED GATE "
            "ACTUALLY RAN (#119 + #148; #292 MAJOR-4).  Every published "
            "receipt key is either sealed at the gate that established it or "
            "named in the declared-unsealed list: %d seals over %d published "
            "keys, %d declared unsealed, %d missing and %d unaccounted; every "
            "one of the %d declared closing gates ran; and every gate name "
            "that a seal of the manifest or a #62 quote anchor attributes "
            "itself to is a gate this run evaluated -- %d that are not.  A "
            "seal or an anchor that names a gate which never runs publishes a "
            "false provenance over a real object, which is what this leg "
            "refuses; it is evaluated here and not at G-COVERAGE because only "
            "here is the gate ledger complete"
            % (len(SEAL.rows), len(published), len(DECLARED_UNSEALED),
               len(missing), len(unsealed), len(CLOSING_GATE_NAMES),
               len(seal_phantom)),
            not missing and not extra and not unsealed
            and not closing_absent and not seal_phantom,
            "seals %d, missing %s, extra %s, unsealed published keys %s, "
            "declared closing gates that did not run %s, seals naming a gate "
            "that never ran %s"
            % (len(SEAL.rows), missing or "none", extra or "none",
               unsealed or "none", closing_absent or "none",
               seal_phantom or "none"))
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
        # #292 MAJOR-5: THE READ-BACK HAPPENS BEFORE THE PROMOTION.  The
        # staged files are hashed on disk and compared with the gate-time
        # seals; only then are they moved into place.  A failing run therefore
        # promotes nothing, which is the era's rule, and the post-replace
        # read-back below remains as the second leg.
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
    # THE NEGATIVE CONTROL, INSIDE THE GATE: the same comparison is run on the
    # disk bytes with one byte flipped, and it must REJECT.  The mechanism is
    # therefore exercised in both directions without any artifact being
    # written twice (#34: a waiver only as a machine-checked forcing).
    flipped = bytes([raw_t[0] ^ 1]) + raw_t[1:]
    control_rejects = (hashlib.sha256(flipped).hexdigest()[:12] != seal_t)
    LD.gate("G-ARTIFACT-INTEGRITY",
            "THE ARTIFACTS ON DISK ARE THE SEALED OBJECTS, AND THE CHECK "
            "PRECEDES THE PROMOTION (#119; #292 MAJOR-5).  The receipt and "
            "the transcript are written to staged temporary files, hashed "
            "THERE and compared with the digests of the objects sealed at "
            "gate time; only bytes that match are moved into place by "
            "os.replace, so a failing comparison promotes nothing.  The bytes "
            "read back after the move are compared with the same seals as a "
            "second leg -- never re-derived from disk, which would only "
            "confirm corruption.  The comparison is exercised in the failing "
            "direction too, on the same disk bytes with one bit flipped",
            dj == seal_j and dt == seal_t and control_rejects,
            "receipt disk %s seal %s; transcript disk %s seal %s; "
            "one-byte-flip control rejects %s"
            % (dj, seal_j, dt, seal_t, control_rejects))
    print()
    print("receipt    %s  %s" % (OUT_JSON, dj))
    print("transcript %s  %s" % (OUT_TXT, dt))
    return R, payload, text, seal_j, seal_t


# ===========================================================================
# SECTION 13.  THE CLI CONTRACT (#82), THE SELFTEST AND THE SWEEP
# ===========================================================================

def reset_state():
    global LINES, READS, READS_BY_CATEGORY, NUMREG, RAW, STAB_CACHE
    global AUT_CACHE, BORN_CACHE
    del LINES[:]
    del READS[:]
    READS_BY_CATEGORY = {}
    NUMREG = set()
    RAW.clear()
    STAB_CACHE.clear()
    AUT_CACHE.clear()
    BORN_CACHE.clear()


class _Sink:
    def write(self, *_a, **_k):
        return None

    def flush(self):
        return None


def run_mutant(name, paper_text):
    """a mutant run: it must DIE at the gate it NAMES, and write nothing.
    #292 MAJOR-4: the declared gate is carried into the row, so 'died' and
    'died where it said it would' are two different facts and the sweep gates
    the second one."""
    global MUT, QUIET
    declared = ([m[1] for m in MUTANTS if m[0] == name] or [None])[0]
    MUT, QUIET = name, True
    reset_state()
    before = artifact_digests()
    try:
        out = full_run(paper_text=paper_text, write=False)
        finish(out[0], out[1], write=False)
        died = None
    except GateFail as exc:
        died = str(exc).split(" :: ")[0]
    finally:
        MUT, QUIET = None, False
    after = artifact_digests()
    return {"mutant": name, "declared_gate": declared, "died_at": died,
            "at_the_declared_gate": died == declared,
            "artifacts_unchanged": before == after}


def artifact_digests():
    out = []
    for p in (OUT_JSON, OUT_TXT):
        if not os.path.exists(p):
            out.append((p, None))
            continue
        with open(p, "rb") as fh:
            out.append((p, hashlib.sha256(fh.read()).hexdigest()[:12]))
    return out


def selftest():
    """#82: corrupt ONE anchor, confirm the run dies, and write nothing."""
    global MUT, QUIET
    before = artifact_digests()
    QUIET = True
    reset_state()
    try:
        full_run(break_anchor="A-PIN", write=False)
        ok = False
        where = "NO-FAILURE"
    except GateFail as exc:
        ok = True
        where = str(exc).split(" :: ")[0]
    finally:
        QUIET = False
    after = artifact_digests()
    print("[selftest] corrupted anchor A-PIN -> %s at %s; artifacts %s"
          % ("died" if ok else "SURVIVED", where,
             "unchanged" if before == after else "CHANGED"))
    return 0 if (ok and before == after) else 1


def sweep(paper_text):
    rows = []
    for name in MUTANT_NAMES:
        rows.append(run_mutant(name, paper_text))
    return rows


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
        print("[cli] usage: aid_exact.py [--sweep] [--selftest] "
              "[--mutant NAME] [--quiet]", file=sys.stderr)
        return 2
    if opts["selftest"]:
        return selftest()
    QUIET = opts["quiet"]
    ppath = os.path.join(REPO, PAPER_REL)
    paper_text = (read_text(ppath, "PAPER-UNDER-TEST")
                  if os.path.exists(ppath) else "")
    if opts["mutant"]:
        row = run_mutant(opts["mutant"], paper_text)
        print("[mutant] %s -> died at %s; artifacts %s"
              % (row["mutant"], row["died_at"],
                 "unchanged" if row["artifacts_unchanged"] else "CHANGED"))
        return 0 if row["died_at"] else 1
    swept = []
    if opts["sweep"]:
        swept = sweep(paper_text)
        bad = [r for r in swept
               if not r["died_at"] or not r["artifacts_unchanged"]]
        print("[sweep] %d mutants, %d survivors" % (len(swept), len(bad)))
        for r in swept:
            print("        %-28s -> %s" % (r["mutant"], r["died_at"]))
        if bad:
            print("[sweep] SURVIVORS: %s" % [r["mutant"] for r in bad],
                  file=sys.stderr)
            return 1
    reset_state()
    MUT = None
    try:
        R, src, _ptext = full_run(paper_text=paper_text, write=True)
        SWEEP_ROWS.extend(swept)
        finish(R, src, write=True, swept=bool(swept))
    except GateFail as exc:
        print("[FAIL] %s" % exc, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
