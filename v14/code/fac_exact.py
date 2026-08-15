#!/usr/bin/env python3
"""FAC (paper-35) -- THE FACTORIZATION UNIT.  IS THE NINE-FOLD DIVISION FORCED?

QUESTION (pin `v14/note-fac-pin.md`, sha256-12 11380265fcf3, ledger #300).
AID answered NAMING on a GRANTED nine-actor grain.  This unit asks
FACTORIZATION: which subsystems the committed law admits at all.  A candidate
factorization is a PARTITION of a carrier; the identifications it induces are
law-compatible exactly when the committed structure DESCENDS along them.  The
criterion is declared in section 5, digested there, and gated before a single
census row runs.

WHAT THIS FILE MEASURES, IN ORDER.

  SEC 1  MACHINERY -- the gate ledger, the total gate-time seal, the text
         normaliser, the numeral registry.
  SEC 2  PROVENANCE -- ten pinned sources, sha256-12 verified, verbatim
         anchors bound to consumer gates; the pre-registered outcome words
         PARSED OUT OF THE PIN'S OWN BYTES rather than typed.
  SEC 3  THE ARENA -- AG(2,3), the three declared links, the 27 co-division
         cells, the 280 groupings, the 36 saturating ones, the 72 R = 3
         I7-STRICT triples, the 276 G-FLAT quadruples, paper-21's 600-schedule
         window, and the three corpora C1/C2/C3.
  SEC 4  THE OBSERVABLES -- the co-division relation, the record n_l(x), the
         participation signature at BOTH grains, the arena's own automorphism
         group, and paper-20's coupled step at BOTH declared coin orders.
  SEC 5  THE LAW-COMPATIBILITY CRITERION -- four legs (GEOMETRY, HISTORY,
         RECORD, DYNAMICS), each a per-object predicate, at the actor grain
         and at the carrier grain.  Declared and digested BEFORE any census.
  SEC 6  MEASUREMENT 1 -- THE DECOMPOSITION CENSUS.  The complete lattice of
         21,147 actor partitions; the declared 42,295-member carrier window
         against Bell(27); the admissible set counted exactly, per history.
  SEC 7  MEASUREMENT 2 -- THE GROUPOID CRYSTALLIZATION.  The groupoid of
         partial identifications and its coherence ladder; the atom theorem
         put at risk and measured.
  SEC 8  MEASUREMENT 3 -- THE GRAIN TRIANGLE.  Stabilizer censuses at S_27,
         at the site grain and at S_9, each under BOTH declared tests.
  SEC 9  MEASUREMENT 4 -- THE PERSISTENCE PRESUPPOSITION and the transport
         test along the declared R-ladder rows.
  SEC 10 THE CONTROL ARMS -- synthetic arenas and declared sub-arenas driven
         through the REAL criterion and the REAL head law, so that every
         pre-registered outcome word is shown emittable.
  SEC 11 THE HEAD, derived twice by routes sharing no dispatcher, and the
         paper instrument, the coverage/polarity/class ledgers and the
         closing battery.

SCOPE AND LANGUAGE.  Every verdict word of this unit names a measured
property of the declared criterion on the declared windows and nothing else.
No sentence here asserts that actors are or are not threads; the unit
measures what the committed law admits, and says so with its grain and its
window attached.  The AID adjudication's not-licensed list is a WALL, scanned
against this unit's own paper.

ARITHMETIC.  Exact only: Python integers and the ring Z[w] carried as integer
pairs.  There are no floats; an AST scan of this file and a recursive type
scan of the emitted receipt are gates.

RUNTIME INPUTS (#46/#91).  Exactly ten committed files are read as SOURCES,
all sha-pinned by this unit's frozen declaration, plus exactly one file read
as the OBJECT UNDER TEST -- this unit's own paper.  No other repository state
is read and no subprocess is invoked, so the run is correct off-tree and with
no version control present.
"""

import ast
import hashlib
import json
import math
import os
import re
import sys
from collections import Counter
from itertools import combinations, permutations, product

SELF = os.path.abspath(__file__)
REPO = os.path.abspath(os.path.join(os.path.dirname(SELF), os.pardir,
                                    os.pardir))
OUT_TXT = os.path.join(os.path.dirname(SELF), "fac_output.txt")
OUT_JSON = os.path.join(os.path.dirname(SELF), "fac_receipt.json")
PAPER_REL = "v14/paper-35-fac.md"

# ===========================================================================
# SECTION 1.  MACHINERY
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
    """the falsifier hook: returns `normal` unless this run is that mutant."""
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
    ("SEAL-OUTCOMES", "pre_registered_outcomes", "G-OUTCOMES-PARSED-FROM-THE-PIN"),
    ("SEAL-WINDOWS", "windows", "G-WINDOWS-DECLARED-WITH-THEIR-BOUNDS"),
    ("SEAL-ARENA", "arena", "G-ARENA-SHAPE"),
    ("SEAL-CARRIER", "carrier", "G-CELL-IS-A-CO-DIVISION-PAIR"),
    ("SEAL-CORPORA", "corpora", "G-CORPORA-SHAPE"),
    ("SEAL-MULTISET", "corpus_multiset", "G-THE-CORPUS-IS-A-MULTISET"),
    ("SEAL-CRITERION", "criterion", "G-CRITERION-FROZEN-BEFORE-THE-CENSUS"),
    ("SEAL-LEGBIND", "leg_binding", "G-WHICH-LEG-BINDS-BY-GRAIN"),
    ("SEAL-ACTOR", "actor_census", "G-ACTOR-GRAIN-ADMISSIBLE-PER-HISTORY"),
    ("SEAL-PAIRWISE", "actor_census_pairwise",
     "G-BOTH-INDUCED-IMAGES-CENSUSED"),
    ("SEAL-IMAGE", "image_fiber", "G-BOTH-INDUCED-IMAGES-CENSUSED"),
    ("SEAL-CELL", "cell_census", "G-CARRIER-GRAIN-ADMISSIBLE-PER-HISTORY"),
    ("SEAL-CROSS", "cross_grain", "G-CROSS-GRAIN-CONTAINMENT"),
    ("SEAL-THESIS", "thesis", "G-THESIS-IS-ONE-DIRECTIONAL"),
    ("SEAL-COIN", "coin_order", "G-BOTH-COIN-ORDERS-PUBLISHED"),
    ("SEAL-GROUPOID", "groupoid", "G-GROUPOID-LADDER-PER-HISTORY"),
    ("SEAL-ATOM", "atom", "G-ATOM-THEOREM-AT-THE-GROUPOID-GRAIN"),
    ("SEAL-TRIANGLE", "grain_triangle", "G-GRAIN-TRIANGLE-BOTH-TESTS"),
    ("SEAL-PERSIST", "persistence", "G-PERSISTENCE-PRESUPPOSITION"),
    ("SEAL-TRANSPORT", "transport", "G-TRANSPORT-ALONG-THE-R-LADDER"),
    ("SEAL-CONTROLS", "controls", "G-EVERY-OUTCOME-WORD-EMITTABLE"),
    ("SEAL-MEASURE", "measure_relativity", "G-E24-COUNTING-ONLY"),
    ("SEAL-CLASSBIND", "class_binding", "G-CLASS-WORDS-BOUND-TO-PREDICATES"),
    ("SEAL-VERDICT", "verdict", "G-VERDICT-RECONSTRUCTED-BY-A-SECOND-ROUTE"),
    ("SEAL-COUNTS", "counts", "G-VERDICT-RECONSTRUCTED-BY-A-SECOND-ROUTE"),
    ("SEAL-WALLS", "walls", "G-WALLS-SCAN-THE-PAPER"),
    ("SEAL-PAPER-CLAIMS", "paper_claims", "G-PAPER-CLAIMS"),
    ("SEAL-PAPER-TABLES", "paper_tables", "G-PAPER-TABLES-WITH-HEADERS"),
    ("SEAL-TABLE-BINDING", "paper_table_binding",
     "G-PAPER-TABLES-WITH-HEADERS"),
    ("SEAL-PAPER-COVERAGE", "paper_coverage", "G-PAPER-NUMERAL-COVERAGE"),
    ("SEAL-REFERENT", "referent_binding", "G-SENTENCE-REFERENT-BINDING"),
    ("SEAL-CANON", "canonization", "G-CANONIZATION-PRESERVES-NUMERALS"),
    ("SEAL-POLARITY", "polarity", "G-PAPER-CLAIM-POLARITY"),
    ("SEAL-COVERAGE", "coverage", "G-FALSIFIER-COVERAGE"),
    ("SEAL-REACHABILITY", "reachability", "G-FALSIFIER-REACHABILITY"),
    ("SEAL-WAIVERS", "waiver_ledger", "G-FALSIFIER-COVERAGE"),
    ("SEAL-MUTANTS", "mutants", "G-FALSIFIER-COVERAGE"),
    ("SEAL-MUTANT-SWEEP", "mutant_sweep", "G-SWEEP-IS-EXECUTION-BOUND"),
    ("SEAL-GATES", "gates", "G-PAPER-INSTRUMENT-RAN-IN-THE-PLAIN-RUN"),
    ("SEAL-CLOSING", "closing_gates", "G-PAPER-INSTRUMENT-RAN-IN-THE-PLAIN-RUN"),
    ("SEAL-TOTALS", "totals", "G-PAPER-INSTRUMENT-RAN-IN-THE-PLAIN-RUN"),
    ("SEAL-TRANSCRIPT", "transcript_head", "G-TRANSCRIPT-SEALED-WHOLE"),
    ("SEAL-ARITHMETIC", "arithmetic", "G-NO-FLOATS"),
    ("SEAL-NAMED-GATES", "named_gates", "G-NAMED-GATES-EXIST"),
]
DECLARED_UNSEALED = ["python", "seal_manifest", "payload_sha256_12"]
MEASURED_KEYS = ("arena", "carrier", "corpora", "corpus_multiset",
                 "criterion", "leg_binding", "actor_census",
                 "actor_census_pairwise", "image_fiber", "cell_census",
                 "cross_grain", "thesis", "coin_order",
                 "groupoid", "atom", "grain_triangle", "persistence",
                 "transport", "controls", "measure_relativity",
                 "class_binding", "counts", "verdict")


class Seal:
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


SEAL = Seal()


def read_bytes(rel):
    READS.append(rel)
    READS_BY_CATEGORY.setdefault("SOURCE", set()).add(
        os.path.abspath(os.path.join(REPO, rel)))
    with open(os.path.join(REPO, rel), "rb") as fh:
        return fh.read()


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
         "₆": "6", "₇": "7", "₈": "8", "₉": "9",
         "ℓ": "l", "→": "->", "←": "<-", "⋅": "*",
         "²": "2", "³": "3", "⁴": "4", "≈": "~",
         "⊆": "subset", "∈": "in", "∑": "sum", "·": "*",
         "−": "-", "⁄": "/", " ": " ", "∏": "prod",
         "σ": "sigma", "φ": "phi", "π": "pi", "Γ": "Gamma",
         "∩": "cap", "∪": "cup", "≅": "iso", "⊲": "normal",
         "∅": "empty", "∷": "::", "ℕ": "N", "ℤ": "Z",
         "ω": "w", "≡": "=", "⊑": "<=", "⊕": "+"}

_MD_PREFIX = re.compile(r"^(?:\s*(?:>+|[-*+]|\d+[.)])\s+)+")
# THE NUMERAL-SAFE PREFIX.  The ordered-list alternative `\d+[.)]` is absent
# here on purpose: a wrapped sentence whose continuation line begins `672. `
# is not a list, and eating that marker destroys the numeral.  Every scan
# that resolves NUMERALS uses this one; `canon` keeps the markdown-complete
# form for prose matching.
_MD_PREFIX_KEEPNUM = re.compile(r"^(?:\s*(?:>+|[-*+])\s+)+")


def _strip_prefixes(s, pat):
    out = []
    for line in s.split("\n"):
        prev = None
        while prev != line:
            prev = line
            line = pat.sub("", line)
            line = re.sub(r"^\s*>+\s*", "", line)
        out.append(line)
    return "\n".join(out)


def mdstrip(s):
    return _strip_prefixes(s, _MD_PREFIX)


def mdstrip_keep_numerals(s):
    return _strip_prefixes(s, _MD_PREFIX_KEEPNUM)


def ascii_fold(s):
    for k in sorted(_FOLD):
        s = s.replace(k, _FOLD[k])
    return s


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def canon(s):
    return norm(ascii_fold(mdstrip(s).replace("*", "").replace("`", "")))


def canon_numeric(s, mutated=False):
    """CANON FOR NUMERAL-BEARING SCANS: every digit of the input survives.
    The whole-text numeral multiset is compared with this function's output at
    a gate, so a normaliser that eats a numeral is caught by arithmetic."""
    strip = mdstrip if mutated else mdstrip_keep_numerals
    return norm(ascii_fold(strip(s).replace("*", "").replace("`", "")))


def numeral_reference_body(s):
    """the same text with NOTHING removed but whitespace and unicode: the
    reference side of the numeral-preservation gate."""
    return norm(ascii_fold(s).replace("*", "").replace("`", ""))


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


NUMWORDS = ("ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN",
            "EIGHT", "NINE", "TEN", "ELEVEN", "TWELVE")
WORDNUM = dict({w.lower(): i for i, w in enumerate(NUMWORDS)},
               twice=2, thirteen=13, fourteen=14, fifteen=15, sixteen=16,
               seventeen=17, eighteen=18, nineteen=19, twenty=20, thirty=30,
               forty=40, fifty=50, sixty=60, hundred=100, thousand=1000)


def spelled_compound(words):
    """THE COMPOUND SPELLED NUMERAL, PARSED (K3 m9).  A run of adjacent
    number-words is evaluated as one English numeral when it is grammatical
    -- `five thousand eight hundred fifty three` is 5,853 -- and reported as
    ungrammatical otherwise, so a compound built from individually backed
    atoms cannot ride in unchecked.  Returns None when the run is not a
    well-formed numeral (`six one`), in which case the atoms stand alone."""
    total, cur, last = 0, 0, None
    for w in words:
        v = WORDNUM[w]
        if v == 1000:
            if cur == 0:
                return None
            total += cur * 1000
            cur, last = 0, 1000
        elif v == 100:
            if cur == 0 or cur >= 100:
                return None
            cur *= 100
            last = 100
        elif v >= 20:
            if last is not None and last < 100:
                return None
            cur += v
            last = v
        else:
            if last is not None and last < 20:
                return None
            cur += v
            last = v
    return total + cur


# ===========================================================================
# SECTION 2.  PROVENANCE -- THE PINNED SOURCES AND THE VERBATIM ANCHORS
# ===========================================================================

PIN_REL = "v14/note-fac-pin.md"
# the digest label the paper writes its provenance tokens with, kept OUT of
# the naming functions so their string literals carry no numeral of their own
# (#267 MAJOR-3 / G-NO-TYPED-COUNTS).
DIGEST_LABEL = "sha256-12"

SOURCES = [
    ("A-PIN", PIN_REL, "11380265fcf3",
     "the frozen charter: the four measurements, the outcome families and "
     "the walls"),
    ("A-AID-ADJ", "v14/note-aid-adjudication.md", "04cd41ed858b",
     "the licensed architecture sentence and the not-licensed wall list"),
    ("A-AID-EFF", "v14/review-aid-effectus.md", "505a0624b6d5",
     "the licensed claims (section 10) and the successor register rows 1-2"),
    ("A-OCC", "v14/paper-31-occ.md", "0092caa4d9ad",
     "the 27-cell carrier typing: a cell IS a co-division pair"),
    ("A-OCC-ADJ", "v14/note-occ-adjudication.md", "3eaa4c0db85d",
     "MISTYPED-AT-THE-CARRIER as the live grain precedent"),
    ("A-PERL", "v14/note-perl-adjudication.md", "08bec11d8466",
     "the L-ladder persistence rulings, panel-verified"),
    ("A-PERR", "v14/note-perr-adjudication.md", "e016015ad170",
     "the R-ladder persistence rulings and the class-binding engraving"),
    ("A-P20", "v14/paper-20-coupling.md", "4824d190af73",
     "the coupled step and the coin-order fiber declared verdict-relevant"),
    ("A-ACT", "v14/note-act-adjudication.md", "cc45d8447bc7",
     "the reachable-outcomes engraving and the control-arm pattern"),
    ("A-RUNBOOK", "RUNBOOK.md", "b3832c2b88bb",
     "the standing engravings, E-24 among them"),
]

VERBATIM = [
    ("V01", "A-PIN",
     "Cardinality 1 -> the\n   division is FORCED; > 1 -> the division is "
     "DECLARED, with\n   the full inventory enumerated and priced",
     "G-CRITERION-FROZEN-BEFORE-THE-CENSUS"),
    ("V02", "A-PIN",
     "The atom theorem is\n   THE OBJECT TO BREAK: group-level triviality "
     "does NOT\n   imply groupoid-level rigidity",
     "G-ATOM-THEOREM-AT-THE-GROUPOID-GRAIN"),
    ("V03", "A-PIN",
     "the criterion itself specified exactly\n      in-code before any "
     "census row runs, and gated",
     "G-CRITERION-FROZEN-BEFORE-THE-CENSUS"),
    ("V04", "A-AID-ADJ",
     "any claim that the actor FACTORIZATION is forced",
     "G-WALLS-SCAN-THE-PAPER"),
    ("V05", "A-AID-EFF",
     "a global relabelling is definable only if actors persist across events, "
     "so the census assumes the thread and measures its name",
     "G-PERSISTENCE-PRESUPPOSITION"),
    ("V06", "A-AID-EFF",
     "5,852 of\n   5,856 committed histories have trivial stabilizer",
     "G-ACTOR-GRAIN-ADMISSIBLE-PER-HISTORY"),
    ("V07", "A-OCC",
     "the unordered co-division pair", "G-CELL-IS-A-CO-DIVISION-PAIR"),
    ("V08", "A-OCC-ADJ",
     "MISTYPED-AT-THE-CARRIER; REFUTED-AT-THE-GRAIN-IT-TYPED",
     "G-GRAIN-TRIANGLE-BOTH-TESTS"),
    ("V09", "A-P20",
     "G.D against D.G; both members run at the reduced horizon",
     "G-BOTH-COIN-ORDERS-PUBLISHED"),
    ("V10", "A-ACT",
     "pre-registered outcome words must each be\nREACHABLE AT THE DECLARED "
     "ARENA", "G-EVERY-OUTCOME-WORD-EMITTABLE"),
    ("V11", "A-RUNBOOK",
     "No count becomes a probability without a declared measure",
     "G-E24-COUNTING-ONLY"),
    ("V12", "A-PERR",
     "a class-explicit row must be gate-bound to its computed predicate",
     "G-CLASS-WORDS-BOUND-TO-PREDICATES"),
    ("V13", "A-PERL",
     "transport to the R-ladder CLOSED BY THEOREM",
     "G-TRANSPORT-ALONG-THE-R-LADDER"),
]

# THE PRE-REGISTERED OUTCOME FAMILIES ARE NOT TYPED HERE.  They are parsed out
# of the pin's own bytes by OUTCOME_PAT and gated against the head law's
# reachable set; a unit that types its own outcome menu can never be caught
# pre-registering an unreachable word.
OUTCOME_PAT = re.compile(r"`(FAC-[A-Za-z<>/_-]+?)`")

WINDOW_DECL = [
    ("W-CORPUS-C1-C2-C3",
     "the history corpus: paper-21's R = 3 I7-STRICT triples (C1), their "
     "pairwise concatenations (C2) and the driven window W4 (C3).  The space "
     "of all histories over this arena is unbounded; the corpus is the "
     "parents' own declared window and is enumerated COMPLETE inside it."),
    ("W-ACTOR-LATTICE-COMPLETE",
     "the actor-grain candidate set: EVERY partition of the nine actors.  "
     "The lattice is enumerated complete -- Bell(9) members, no cap, no "
     "sampling."),
    ("W-CELL-INDUCED-PLUS-STRATA",
     "the carrier-grain candidate set: the DIRECTIONWISE image of every "
     "actor partition, the PAIRWISE image of every actor partition, and a "
     "declared list of OCC-typed natural strata (the discrete and trivial "
     "carrier partitions, by-direction, by-anchor-site, by-AG-line, the "
     "shift orbits and the six translation-subgroup orbit partitions), "
     "deduplicated as partitions.  Bell(27) is astronomically larger and the "
     "ratio is published with the window; nothing is silently capped."),
    ("W-COHERENCE-LADDER",
     "the groupoid coherence relations censused: the sliding windows "
     "|t - s| <= w for w = 0, 1, 2, 3, the round-local relation, and the "
     "complete relation.  The collapse threshold is derived per history by "
     "increasing w until the count meets the complete relation's, so the "
     "ladder is not truncated below the answer."),
    ("W-FULL-LATTICE-PER-LEG",
     "the per-leg binding sweep runs the COMPLETE actor lattice against a "
     "declared history sub-window -- C1 in full plus every history the actor "
     "census found non-unique -- because the product of the two complete "
     "sets is larger than this unit's declared cost budget; the sub-window's "
     "size and its complement are both published."),
    ("W-STABILIZER-AND-ARROW-SUB-WINDOW",
     "the grain triangle, the arrow groupoid and the raw-versus-realizable "
     "agreement run on C1 and C3 -- the strict triples and the driven "
     "window -- because a concatenation's stabilizer is the intersection of "
     "its parts' and its arrow groupoid is their disjoint union, so C2 "
     "carries no independent row.  The complement is named: all of C2."),
    ("W-CONTROL-ARENAS",
     "the control arm: declared sub-corpora and synthetic link-sets driven "
     "through the REAL criterion and the REAL head law.  No control row is "
     "forged; each is a genuine evaluation of the same code on a declared "
     "datum."),
]

# THE WALLS.  Each is a list of ASSERTIVE needles that must NOT appear in this
# unit's paper.  They are scanned against the PAPER's bytes -- the leg the
# wall is owed (#269's caveat) -- and each carries a mutant that PLANTS its
# needle into the paper text and must die here.
#
# WHAT A WALL IS AND IS NOT (K3 m8).  The needles are matched after markdown,
# emphasis, ASCII-fold and whitespace-free normalisation, so a bullet-wrapped
# or list-split plant is still caught; they are LISTED VARIANTS of each
# refused sentence, not an invariance under paraphrase.  A reviewer's
# word-order paraphrase evaded the delivered list and its shape is now a
# needle -- but the honest statement of the surface is: N declared forms per
# wall, normalisation-hard, paraphrase-INCOMPLETE, and the paper is read
# against the not-licensed list by the panel as well as by this scan.
WALLS = [
    ("W-NO-FORCED-ACTOR-FACTORIZATION",
     ["the actor factorization is forced by the law",
      "the nine-fold division is forced, full stop",
      "the factorization of the arena into actors is forced",
      "the law forces the actor factorization"],
     "the AID adjudication's not-licensed list, four declared forms"),
    ("W-NO-IDENTITY-TO-MATTER",
     ["actors are ontology for matter and chart for space",
      "space is identity-blind and matter is identity-sighted",
      "identity belongs to matter and chart belongs to space"],
     "the refused architecture sentence"),
    ("W-NO-UNSCOPED-RECORD-THREAD",
     ["the record is not a property of a thread",
      "the record is never a property of any thread"],
     "the unscoped slogan the AID adjudication refuses"),
    ("W-NO-REALITY-SLOGAN",
     ["actors are truly real threads", "actors are not real at all",
      "actors do not exist as threads", "actors really are threads",
      "actors are genuine persisting threads"],
     "no unscoped reality language about actors"),
    ("W-NO-FIVE-RESONANCE",
     ["the same five appears in paper-20's horizon",
      "this five and the horizon-5 are the same five",
      "the crystallization five resonates with the horizon five"],
     "the resonance the AID adjudication demoted to refused"),
    ("W-NO-DISJOINT-FREEDOMS",
     ["the weld's freedom and identity's freedom are disjoint",
      "the two freedoms are disjoint rather than nested",
      "identity's freedom and the weld's freedom share nothing"],
     "AID's not-licensed item 5, carried here as INAPPLICABLE-BUT-WALLED: "
     "this unit welds nothing, but its central structure has that item's "
     "shape -- 4 inside 46 is containment with an index, and the paper "
     "renders it as containment with its index named"),
]


# ===========================================================================
# SECTION 3.  THE ARENA -- AG(2,3), THE CARRIER, THE CORPORA
# ===========================================================================

SITES = tuple((i, j) for i in range(3) for j in range(3))
SITE_INDEX = {s: k for k, s in enumerate(SITES)}
NACT = len(SITES)
I7_LINKS = ((1, 0), (0, 1), (1, 1))
CLASS_NAMES = ("ROW", "COL", "DIA", "ANT")
CLASS_DIR = {"ROW": (0, 1), "COL": (1, 0), "DIA": (1, 1), "ANT": (1, 2)}
ARENA_LITERALS = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                  "12", "18", "20", "24", "27", "33", "35", "62", "82",
                  "87", "91", "119", "125", "267", "269", "293", "295",
                  "299", "300", "14", "22", "23", "28", "29", "31", "34"}


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
    """OCC's carrier typing, re-implemented: the cell IS the unordered
    co-division pair {x, x + l}."""
    x, l = cell
    return frozenset((x, vadd(x, l)))


def actor(site):
    return "G%d%d" % site


ACTORS = tuple(actor(s) for s in SITES)


def all_groupings():
    """every partition of the nine sites into three triples (the conflict
    groupings of one round)."""
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


def round_vec(P):
    """the per-cell incidence 27-vector of one round's grouping: cell (x, l)
    carries 1 exactly when x and x + l share a conflict group."""
    return tuple(1 if any(x in g and vadd(x, l) in g for g in P) else 0
                 for (x, l) in CELLS)


RAW = {}


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
    """paper-21's I7-STRICT class at R = 3: ordered triples of saturating
    groupings whose summed link field covers every one of the 27 cells."""
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
    """paper-21's 276: ordered quadruples of saturating groupings whose summed
    link field is I7's G-FLAT row (1, 1, 2) at all nine sites."""
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
    """the declared seed menu of a grouping: the k-th member of each group in
    the canonical order.  Deterministic, no sampling."""
    return [tuple(sorted(g)[k] for g in P) for k in range(3)]


def history_of(rounds, seeds):
    """THE COMBINATORIAL HISTORY: the division events of a schedule, as
    actor-subsets, in the driver's own order -- groups in ascending order of
    their seed's site index, one arbitration per conflict group per round."""
    H = []
    for P, sd in zip(rounds, seeds):
        order = sorted(range(len(P)), key=lambda gi: SITE_INDEX[sd[gi]])
        for gi in order:
            H.append(frozenset(P[gi]))
    return tuple(H)


COLLINEAR_FLAT = ("ROW", "COL", "DIA", "DIA")
COMMITTED_R4 = ("ROW", "COL", "ROW", "COL")
SEEDS_PER_ROUND_IN_WINDOW = 1


def window_schedules(flatq, parts):
    """PAPER-21's DRIVEN WINDOW W4, reconstructed by its own constructor."""
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
        menus = [canon_transversals(P)[:SEEDS_PER_ROUND_IN_WINDOW] for P in T]
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


def bell(n):
    """Bell numbers by the triangle -- integer arithmetic only."""
    row = [1]
    for _ in range(n):
        nxt = [row[-1]]
        for v in row:
            nxt.append(nxt[-1] + v)
        row = nxt
    return row[0]


def all_set_partitions(elems):
    """the COMPLETE partition lattice of a finite set, by restricted growth."""
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
    return sorted(out)


# ===========================================================================
# SECTION 4.  THE OBSERVABLES
# ===========================================================================

def codivision(H):
    """PAPER-19's LINK GENERATOR: the co-division incidence on the actor pair
    -- the number of division events whose footprint meets both endpoints."""
    r = [[0] * NACT for _ in range(NACT)]
    for F in H:
        idx = sorted(SITE_INDEX[x] for x in F)
        for a in idx:
            for b in idx:
                if a != b:
                    r[a][b] += 1
    return r


def record_field(H, rel=None):
    """THE RECORD n_l(x) AT THE CONSTRUCTOR'S OWN PARSE: the count of division
    events containing both the actor at site x and the actor at site x + l."""
    r = codivision(H) if rel is None else rel
    return tuple(r[SITE_INDEX[x]][SITE_INDEX[vadd(x, l)]] for (x, l) in CELLS)


def signature_blocks(H):
    """THE PARTICIPATION-SIGNATURE PARTITION at the ACTOR grain: two actors
    share a block exactly when they belong to the same events, all of them."""
    sig = {}
    for x in SITES:
        sig.setdefault(tuple(1 if x in F else 0 for F in H), []).append(x)
    return tuple(sorted(tuple(sorted(v)) for v in sig.values()))


def class_round_profile(H):
    """WHICH PARALLEL CLASS EACH ROUND USES, when it uses one at all: the
    three events of a round are compared with each declared class's three
    lines as a SET, so the answer is computed from the history and not read
    off the schedule that produced it."""
    out = []
    for r in range(len(H) // 3):
        rd = frozenset(H[3 * r:3 * r + 3])
        nm = None
        for k in CLASS_NAMES:
            if rd == frozenset(frozenset(g) for g in CLASSES[k]):
                nm = k
        out.append(nm)
    return out


def repeats_a_parallel_class(H):
    """the THESIS predicate: some parallel class is used in at least two of
    the history's rounds."""
    c = Counter(k for k in class_round_profile(H) if k is not None)
    return bool(c) and max(c.values()) >= 2


def class_constant(H):
    """the stronger predicate: ONE parallel class in EVERY round."""
    prof = class_round_profile(H)
    c = Counter(k for k in prof if k is not None)
    return bool(c) and max(c.values()) == len(prof)


def cell_footprint(F):
    """the CARRIER-grain footprint of a division event: the cells whose two
    actors both take part in it."""
    return frozenset(k for k, (x, l) in enumerate(CELLS)
                     if x in F and vadd(x, l) in F)


def cell_signature_blocks(H):
    """THE PARTICIPATION-SIGNATURE PARTITION at the CARRIER grain."""
    foot = [cell_footprint(F) for F in H]
    sig = {}
    for k in range(DIM):
        sig.setdefault(tuple(1 if k in f else 0 for f in foot), []).append(k)
    return tuple(sorted(tuple(sorted(v)) for v in sig.values()))


def young_order(blocks):
    o = 1
    for b in blocks:
        o *= math.factorial(len(b))
    return o


def gl23():
    out = []
    for a in range(3):
        for b in range(3):
            for c in range(3):
                for d in range(3):
                    if (a * d - b * c) % 3 != 0:
                        out.append(((a, b), (c, d)))
    return out


def apply_M(M, v):
    return ((M[0][0] * v[0] + M[0][1] * v[1]) % 3,
            (M[1][0] * v[0] + M[1][1] * v[1]) % 3)


DIRSET = frozenset([l for l in I7_LINKS] + [vmul(2, l) for l in I7_LINKS])


def arena_automorphisms():
    """THE SITE GRAIN'S OWN GROUP: the affine maps of AG(2,3) that permute the
    three DECLARED link directions among themselves.  Each acts on the nine
    sites AND on the 27 cells, coherently -- which is exactly what makes the
    site grain a grain and not a relabelling."""
    out = []
    for M in sorted(gl23()):
        if not all(apply_M(M, l) in DIRSET for l in I7_LINKS):
            continue
        for b in SITES:
            sp = tuple(SITE_INDEX[vadd(apply_M(M, x), b)] for x in SITES)
            cp = [0] * DIM
            for k, (x, l) in enumerate(CELLS):
                y = vadd(apply_M(M, x), b)
                Ml = apply_M(M, l)
                if Ml in I7_LINKS:
                    cp[k] = CELL_INDEX[(y, Ml)]
                else:
                    cp[k] = CELL_INDEX[(vadd(y, Ml), vmul(2, Ml))]
            out.append((sp, tuple(cp)))
    return sorted(set(out))


# ---- paper-20's coupled step, re-implemented over Z[w] --------------------

GN = tuple(tuple(2 if i != j else -1 for j in range(3)) for i in range(3))
SHIFT_T = tuple(CELL_INDEX[(vadd(x, l), l)] for (x, l) in CELLS)
COIN_ORDERS = ("G.D", "D.G")


def coupled_columns(rec, order):
    """THE ONE-STEP OPERATOR U = T . C, COLUMN BY COLUMN, EXACTLY.

    The coin is site-block-diagonal with D(x) = diag(w^{n_l(x)}); paper-20
    declares the composition order a verdict-relevant fiber, so BOTH members
    are built here and every census that consumes U consumes both.  A column
    is a list of (target cell, direction exponent, integer coefficient): the
    Grover entry times w^e, kept as an exact pair rather than a float."""
    cols = []
    for k, (y, l) in enumerate(CELLS):
        li = I7_LINKS.index(l)
        ent = []
        for i in range(3):
            tgt = SHIFT_T[CELL_INDEX[(y, I7_LINKS[i])]]
            e = (rec[SITE_INDEX[y] * 3 + li] if order == "G.D"
                 else rec[SITE_INDEX[y] * 3 + i]) % 3
            ent.append((tgt, e, GN[i][li]))
        cols.append(tuple(sorted(ent)))
    return tuple(cols)


# ===========================================================================
# SECTION 5.  THE LAW-COMPATIBILITY CRITERION
#
# A candidate factorization is a PARTITION of a carrier.  Its INDUCED
# IDENTIFICATIONS merge the members of each block.  The partition is
# LAW-COMPATIBLE at a history exactly when the committed structure DESCENDS
# along those identifications -- when the quotient still carries it.  Four
# legs, one per committed structure, each a per-object predicate (#87):
#
#   LEG-1 GEOMETRY  the committed link/shift structure descends
#   LEG-2 HISTORY   every division event descends (is a union of blocks)
#   LEG-3 RECORD    the record field n_l(x) descends (is block-constant)
#   LEG-4 DYNAMICS  paper-20's one-step operator is exactly LUMPABLE for the
#                   induced carrier partition -- the standard quotient
#                   criterion, block sums compared exactly in Z[w], at BOTH
#                   declared coin orders
#
# FAC-ADMISSIBLE = LEG-1 and LEG-2 and LEG-3 and LEG-4.  The criterion is
# frozen here: its source is digested before the first census row runs and no
# leg reads any census product -- both facts are gated.
# ===========================================================================

CRITERION_FUNCS = ("leg1_actor", "leg2_actor", "leg3_actor",
                   "leg1_cell", "leg2_cell", "leg3_cell", "leg4_cell",
                   "induced_cell_partition", "pairwise_cell_partition",
                   "admissible_actor", "admissible_cell")
CRITERION_FORBIDDEN_NAMES = ("actor_census", "cell_census", "CENSUS",
                             "ADMISSIBLE_SET", "R", "VERDICT")
# THE CRITERION'S NAME WHITELIST (K3 MAJOR-1).  A blacklist of six spellings
# is a spelling filter: a module-global alias, a `globals()` lookup and a
# default-argument alias all walked past it.  This is the complement -- the
# EXHAUSTIVE list of free names the criterion's functions may reference: the
# arena's own constants, the folding helpers, the criterion's own members and
# the builtins actually used.  Anything else fails the gate, `globals`
# included.  The list is part of the criterion's combined digest, so widening
# it moves the published digest and the paper's digest sentence is a gated
# claim.
CRITERION_ALLOWED_NAMES = (
    "CELLS", "DIM", "I7_LINKS", "SHIFT_T", "SITES", "SITE_INDEX",
    "block_map", "canonical_cell_partition", "coupled_columns", "vadd",
    "induced_cell_partition", "pairwise_cell_partition",
    "leg1_actor", "leg2_actor", "leg3_actor",
    "leg1_cell", "leg2_cell", "leg3_cell", "leg4_cell",
    "bool", "enumerate", "len", "range", "sorted", "sum", "tuple",
)


def block_map(part):
    return {x: bi for bi, b in enumerate(part) for x in b}


def leg1_actor(part, _bm=None, links=None):
    """LEG-1 at the ACTOR grain: for each declared link l, the translation
    x -> x + l descends to the blocks.  Reads the partition and the arena --
    never the history.  The link set is a PARAMETER defaulting to the
    committed one, so a synthetic arena runs through this same predicate."""
    bm = block_map(part) if _bm is None else _bm
    for l in (I7_LINKS if links is None else links):
        img = {}
        for x in SITES:
            b, t = bm[x], bm[vadd(x, l)]
            if img.setdefault(b, t) != t:
                return False
    return True


def leg2_actor(part, H):
    """LEG-2 at the ACTOR grain: every division event is a union of blocks, so
    the event is still a well-defined subset after the identification."""
    for F in H:
        for b in part:
            n = sum(1 for x in b if x in F)
            if n and n != len(b):
                return False
    return True


def leg3_actor(part, rec):
    """LEG-3 at the ACTOR grain: the record is block-constant link by link, so
    n descends to a field on the quotient's cells."""
    for b in part:
        for li in range(3):
            if len({rec[SITE_INDEX[x] * 3 + li] for x in b}) > 1:
                return False
    return True


def induced_cell_partition(part):
    """THE DIRECTIONWISE IMAGE: identify (x, l) with (y, l) when x and y are
    identified.  One of the TWO declared members of the induced-image fiber;
    LEG-4 at the actor grain is evaluated at an image supplied by the caller,
    and both members are censused."""
    bm = block_map(part)
    lab = [(bm[x], I7_LINKS.index(l)) for (x, l) in CELLS]
    return canonical_cell_partition(lab)


def pairwise_cell_partition(part):
    """THE PAIRWISE IMAGE: a cell IS the unordered co-division pair {x, x + l}
    (OCC, and this unit's own G-CELL-IS-A-CO-DIVISION-PAIR), so an actor
    factorization identifies two cells when their pairs of blocks agree as
    unordered pairs.  The second declared member of the induced-image fiber:
    NOT the directionwise one, and censused beside it."""
    bm = block_map(part)
    lab = [tuple(sorted((bm[x], bm[vadd(x, l)]))) for (x, l) in CELLS]
    return canonical_cell_partition(lab)


def canonical_cell_partition(labels):
    d = {}
    for k, lab in enumerate(labels):
        d.setdefault(lab, []).append(k)
    return tuple(sorted(tuple(sorted(v)) for v in d.values()))


def leg1_cell(cpart):
    """LEG-1 at the CARRIER grain: the shift T descends to the blocks."""
    lab = [0] * DIM
    for bi, b in enumerate(cpart):
        for k in b:
            lab[k] = bi
    img = {}
    for k in range(DIM):
        b, t = lab[k], lab[SHIFT_T[k]]
        if img.setdefault(b, t) != t:
            return False
    return True


def leg2_cell(cpart, foot):
    """LEG-2 at the CARRIER grain: every event's cell footprint is a union of
    blocks."""
    for f in foot:
        for b in cpart:
            n = sum(1 for k in b if k in f)
            if n and n != len(b):
                return False
    return True


def leg3_cell(cpart, rec):
    """LEG-3 at the CARRIER grain: the record is constant on each block."""
    for b in cpart:
        if len({rec[k] for k in b}) > 1:
            return False
    return True


def leg4_cell(cpart, rec, order):
    """LEG-4: EXACT LUMPABILITY of paper-20's one-step operator for the
    carrier partition -- for any two cells of a block, the sum of the column's
    entries falling into each block agrees, exactly, in Z[w].  Entries are
    kept as (block, exponent) -> integer coefficient maps and compared as
    objects, so no cancellation is assumed and no float is formed."""
    lab = [0] * DIM
    for bi, b in enumerate(cpart):
        for k in b:
            lab[k] = bi
    cols = coupled_columns(rec, order)
    prof = []
    for k in range(DIM):
        acc = {}
        for (tgt, e, coef) in cols[k]:
            key = (lab[tgt], e)
            acc[key] = acc.get(key, 0) + coef
        prof.append(tuple(sorted((kk, vv) for kk, vv in acc.items() if vv)))
    for b in cpart:
        if len({prof[k] for k in b}) > 1:
            return False
    return True


def leg4_cell_summed(cpart, rec, order):
    """THE STATED FORM OF LEG-4, kept beside the implemented one (K1 MINOR-1).
    The paper describes block SUMS compared in Z[w]; the implemented predicate
    compares the per-exponent integer tallies, which is STRICTLY FINER,
    because 1 + w + w^2 = 0 identifies profiles the tallies distinguish.  This
    function performs the summation first -- a + b w + c w^2 reduced to
    (a - c) + (b - c) w -- so the two predicates can be compared on every
    evaluation of the census rather than argued about.  It is NOT a member of
    the criterion: it is the comparator the fineness disclosure is measured
    with."""
    lab = [0] * DIM
    for bi, b in enumerate(cpart):
        for k in b:
            lab[k] = bi
    cols = coupled_columns(rec, order)
    prof = []
    for k in range(DIM):
        acc = {}
        for (tgt, e, coef) in cols[k]:
            v = acc.setdefault(lab[tgt], [0, 0, 0])
            v[e] += coef
        red = {}
        for kk, (a, b, c) in acc.items():
            if (a - c, b - c) != (0, 0):
                red[kk] = (a - c, b - c)
        prof.append(tuple(sorted(red.items())))
    for b in cpart:
        if len({prof[k] for k in b}) > 1:
            return False
    return True


def admissible_actor(part, H, rec, bm=None, image=None):
    """the criterion at the ACTOR grain, leg by leg, both coin orders.

    THE INDUCED-IMAGE FIBER, DECLARED.  LEG-4 is a predicate on a CARRIER
    partition, so an actor partition must be carried to the carrier before the
    dynamics leg can see it -- and the declared window names TWO images that
    do that.  The image is therefore a PARAMETER of this criterion, exactly as
    the link set is a parameter of LEG-1, and the census below runs both
    members and publishes both."""
    l1 = leg1_actor(part, bm)
    l2 = leg2_actor(part, H)
    l3 = leg3_actor(part, rec)
    if not (l1 and l2 and l3):
        return (l1, l2, l3, None, None, False)
    cp = (induced_cell_partition if image is None else image)(part)
    g = leg4_cell(cp, rec, "G.D")
    d = leg4_cell(cp, rec, "D.G")
    return (l1, l2, l3, g, d, bool(g and d))


def admissible_cell(cpart, foot, rec, l1=None):
    """the criterion at the CARRIER grain, leg by leg, both coin orders."""
    e1 = leg1_cell(cpart) if l1 is None else l1
    e2 = leg2_cell(cpart, foot)
    e3 = leg3_cell(cpart, rec)
    if not (e1 and e2 and e3):
        return (e1, e2, e3, None, None, False)
    g = leg4_cell(cpart, rec, "G.D")
    d = leg4_cell(cpart, rec, "D.G")
    return (e1, e2, e3, g, d, bool(g and d))


def criterion_source(src):
    """the criterion's own bytes, function by function, so the declaration
    that ran can be checked against the declaration that was published."""
    tree = ast.parse(src)
    lines = src.split("\n")
    out = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name in CRITERION_FUNCS:
            body = "\n".join(lines[node.lineno - 1:node.end_lineno])
            out[node.name] = {"lines": node.end_lineno - node.lineno + 1,
                              "sha256_12": digest(body)}
    return out


def criterion_reads(src):
    """every free NAME the criterion's functions reference, so a leg that
    consults a census product is caught by the code and not by a promise."""
    tree = ast.parse(src)
    seen = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name in CRITERION_FUNCS:
            local = {a.arg for a in node.args.args}
            names = set()
            for n in ast.walk(node):
                if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Load):
                    names.add(n.id)
                elif isinstance(n, ast.Name):
                    local.add(n.id)
            seen[node.name] = sorted(names - local)
    return seen


# ===========================================================================
# SECTION 6.  THE CARRIER-GRAIN WINDOW
# ===========================================================================

CELL_STRATUM_NAMES = ("S-DISCRETE-27", "S-TRIVIAL-1", "S-BY-DIRECTION",
                      "S-BY-ANCHOR-SITE", "S-BY-AG-LINE", "S-BY-SHIFT-ORBIT",
                      "S-TRANSL-ORBIT-H0", "S-TRANSL-ORBIT-HROW",
                      "S-TRANSL-ORBIT-HCOL", "S-TRANSL-ORBIT-HDIA",
                      "S-TRANSL-ORBIT-HANT", "S-TRANSL-ORBIT-HFULL")


def cell_strata():
    """THE OCC-TYPED NATURAL STRATA of the carrier, each named and each built
    from the arena rather than typed as a member list."""
    out = {}
    out["S-DISCRETE-27"] = list(range(DIM))
    out["S-TRIVIAL-1"] = [0] * DIM
    out["S-BY-DIRECTION"] = [I7_LINKS.index(l) for (_x, l) in CELLS]
    out["S-BY-ANCHOR-SITE"] = [SITE_INDEX[x] for (x, _l) in CELLS]
    line = [(I7_LINKS.index(l),
             tuple(sorted(SITE_INDEX[vadd(x, vmul(k, l))] for k in range(3))))
            for (x, l) in CELLS]
    out["S-BY-AG-LINE"] = line
    orb = {}
    for k in range(DIM):
        j, cyc = k, []
        while j not in cyc:
            cyc.append(j)
            j = SHIFT_T[j]
        orb[k] = tuple(sorted(cyc))
    out["S-BY-SHIFT-ORBIT"] = [orb[k] for k in range(DIM)]
    subs = {"H0": [(0, 0)], "HFULL": list(SITES)}
    for nm, d in (("HROW", CLASS_DIR["ROW"]), ("HCOL", CLASS_DIR["COL"]),
                  ("HDIA", CLASS_DIR["DIA"]), ("HANT", CLASS_DIR["ANT"])):
        subs[nm] = [(0, 0), d, vmul(2, d)]
    for nm in sorted(subs):
        out["S-TRANSL-ORBIT-" + nm] = [
            tuple(sorted(CELL_INDEX[(vadd(x, h), l)] for h in subs[nm]))
            for (x, l) in CELLS]
    return out


def build_cell_window(P9):
    """W-CELL-INDUCED-PLUS-STRATA, deduplicated as PARTITIONS with every
    member's provenance families recorded."""
    win = {}
    for part in P9:
        win.setdefault(induced_cell_partition(part), set()).add("DIRECTIONWISE")
    for part in P9:
        win.setdefault(pairwise_cell_partition(part), set()).add("PAIRWISE")
    for nm in CELL_STRATUM_NAMES:
        lab = cell_strata()[nm]
        win.setdefault(canonical_cell_partition(lab), set()).add(nm)
    return {p: sorted(v) for p, v in win.items()}


def cell_partition_name(cpart, families):
    """a REFERENT-BOUND name: the block profile the partition itself has, plus
    the window families that produced it.  Nothing about the name is typed."""
    prof = sorted(len(b) for b in cpart)
    tally = "-".join("%dx%d" % (c, s) for s, c in
                     sorted(Counter(prof).items(), reverse=True))
    onedir = all(len({CELLS[k][1] for k in b}) == 1 for b in cpart)
    onesite = all(len({CELLS[k][0] for k in b}) == 1 for b in cpart)
    return "CP-%d-BLOCKS-%s-%s-%s" % (
        len(cpart), tally,
        "WITHIN-ONE-DIRECTION" if onedir else "ACROSS-DIRECTIONS",
        "WITHIN-ONE-SITE" if onesite else "ACROSS-SITES")


def actor_partition_name(part):
    """a REFERENT-BOUND name for an actor partition: the profile it has, and
    whether it IS one of AG(2,3)'s parallel classes -- computed, not typed."""
    prof = sorted(len(b) for b in part)
    tally = "-".join("%dx%d" % (c, s) for s, c in
                     sorted(Counter(prof).items(), reverse=True))
    cls = ""
    for k in CLASS_NAMES:
        if tuple(sorted(tuple(sorted(g)) for g in CLASSES[k])) == part:
            cls = "-PARALLEL-CLASS-" + k
    return "AP-%d-BLOCKS-%s%s" % (len(part), tally, cls)


# ===========================================================================
# SECTION 7.  THE GROUPOID OF PARTIAL IDENTIFICATIONS
#
# The global grain quantifies over ONE permutation of the whole actor set and
# asks it to fix every event.  The groupoid grain replaces that with a FAMILY
# of local identifications, one per event, each a permutation of that event's
# own footprint, subject to a DECLARED COHERENCE RELATION R on the times: for
# (t, s) in R the two local identifications must agree wherever their domains
# meet.  R = the complete relation recovers the global group; R = the empty
# relation imposes nothing.  The coherence relation is exactly the amount of
# thread persistence the census assumes, made into a coordinate.
# ===========================================================================

COHERENCE_ROWS = ("R-EMPTY", "R-ADJACENT", "R-WINDOW-2", "R-WINDOW-3",
                  "R-ROUND", "R-COMPLETE")


def local_syms(F):
    fs = sorted(F)
    return [dict(zip(fs, p)) for p in permutations(fs)]


def groupoid_arrows(H):
    """THE GROUPOID ITSELF: objects are the events; an arrow t -> s is a
    bijection of footprints that preserves the LOCAL committed structure --
    the internal co-division cells with their declared directions.  Returned
    as the arrow count per ordered pair, the isotropy order per object, and
    the number of connected components."""
    T = len(H)
    fs = [sorted(F) for F in H]
    arrows = {}
    for t in range(T):
        for s in range(T):
            n = 0
            for p in permutations(range(3)):
                ok = True
                for i in range(3):
                    for j in range(3):
                        if i == j:
                            continue
                        u, v = fs[t][i], fs[t][j]
                        pu, pv = fs[s][p[i]], fs[s][p[j]]
                        du = ((v[0] - u[0]) % 3, (v[1] - u[1]) % 3)
                        dv = ((pv[0] - pu[0]) % 3, (pv[1] - pu[1]) % 3)
                        if (du in I7_LINKS) != (dv in I7_LINKS):
                            ok = False
                            break
                        if du in I7_LINKS and du != dv:
                            ok = False
                            break
                    if not ok:
                        break
                if ok:
                    n += 1
            arrows[(t, s)] = n
    iso = [arrows[(t, t)] for t in range(T)]
    seen, comps = set(), 0
    for t in range(T):
        if t in seen:
            continue
        comps += 1
        stack = [t]
        while stack:
            u = stack.pop()
            if u in seen:
                continue
            seen.add(u)
            for v in range(T):
                if v not in seen and arrows[(u, v)]:
                    stack.append(v)
    return {"objects": T, "isotropy_orders": iso,
            "connected_components": comps,
            "arrow_total": sum(arrows.values()),
            "hom_sets_nonempty": sum(1 for v in arrows.values() if v)}


def coherence_pairs(T, row, per_round):
    if row == "R-EMPTY":
        return []
    if row == "R-COMPLETE":
        return [(t, s) for t in range(T) for s in range(t)]
    if row == "R-ROUND":
        return [(t, s) for t in range(T) for s in range(t)
                if t // per_round == s // per_round]
    w = int(row.rsplit("-", 1)[1]) if row.startswith("R-WINDOW") else 1
    return [(t, s) for t in range(T) for s in range(t) if t - s <= w]


def gamma_window_count(H, w):
    """|Gamma_R| for the sliding window R = {(t, s) : |t - s| <= w}, EXACT, by
    dynamic programming on the last w local identifications.  w = 0 is the
    empty relation and is the closed product."""
    T = len(H)
    S = [local_syms(F) for F in H]
    if w == 0:
        n = 1
        for s in S:
            n *= len(s)
        return n
    ov = [[sorted(set(H[t]) & set(H[s])) for s in range(T)] for t in range(T)]
    states = {(): 1}
    for t in range(T):
        nxt = {}
        for st in sorted(states):
            cnt = states[st]
            base = t - len(st)
            for a in range(len(S[t])):
                good = True
                for j, b in enumerate(st):
                    s = base + j
                    if t - s <= w:
                        for u in ov[t][s]:
                            if S[t][a][u] != S[s][b][u]:
                                good = False
                                break
                    if not good:
                        break
                if good:
                    ns = (st + (a,))[-w:]
                    nxt[ns] = nxt.get(ns, 0) + cnt
        states = nxt
    return sum(states.values())


def gamma_relation_count(H, pairs):
    """|Gamma_R| for an ARBITRARY declared relation, EXACT.  Pairs whose
    domains do not meet impose nothing and are dropped; the constraint graph
    is then split into connected components and each is counted by
    backtracking with full pruning, the counts multiplied.  The decomposition
    is what makes the round-local relation -- whose events are pairwise
    disjoint and therefore mutually unconstrained -- a PRODUCT rather than an
    enumeration of its own answer."""
    T = len(H)
    S = [local_syms(F) for F in H]
    edges = {}
    for (t, s) in pairs:
        ov = sorted(set(H[t]) & set(H[s]))
        if not ov:
            continue
        edges.setdefault(t, []).append((s, ov))
        edges.setdefault(s, []).append((t, ov))
    seen, total = set(), 1
    for t0 in range(T):
        if t0 in seen:
            continue
        comp, stack = [], [t0]
        while stack:
            u = stack.pop()
            if u in seen:
                continue
            seen.add(u)
            comp.append(u)
            for (v, _o) in edges.get(u, []):
                if v not in seen:
                    stack.append(v)
        comp.sort()
        if len(comp) == 1:
            total *= len(S[comp[0]])
            continue
        pos = {t: i for i, t in enumerate(comp)}
        cnt = [0]
        cur = [0] * len(comp)

        def bt(i, comp=comp, pos=pos, cnt=cnt, cur=cur):
            if i == len(comp):
                cnt[0] += 1
                return
            t = comp[i]
            for a in range(len(S[t])):
                ok = True
                for (v, ov) in edges.get(t, []):
                    j = pos.get(v)
                    if j is None or j >= i:
                        continue
                    for u in ov:
                        if S[t][a][u] != S[v][cur[j]][u]:
                            ok = False
                            break
                    if not ok:
                        break
                if ok:
                    cur[i] = a
                    bt(i + 1)
        bt(0)
        total *= cnt[0]
    return total


def collapse_threshold(H, target, known=None):
    """THE DERIVED CONSTANT: the least sliding-window width at which the
    groupoid count meets the global group's.  Nothing is capped -- the search
    runs until the counts agree; widths already computed in the ladder are
    reused rather than recomputed, which changes cost and not the answer."""
    known = known or {}
    w = 0
    while w <= len(H):
        v = known[w] if w in known else gamma_window_count(H, w)
        if v == target:
            return w
        w += 1
    return None


# ===========================================================================
# SECTION 8.  THE GRAIN TRIANGLE
#
# THE TEST-DECLARATION DUTY (AID MAJOR-1).  Two tests are declared, and BOTH
# run at ALL THREE grains -- the contrast is the claim, so neither object is
# measured under only one test:
#
#   TEST-RAW         the stabilizer inside the grain's FULL symmetric group:
#                    every relabelling of the grain's own carrier
#   TEST-REALIZABLE  the stabilizer intersected with the transformations the
#                    ARENA itself realizes -- the affine maps that permute the
#                    declared links, acting on sites and cells coherently
# ===========================================================================

GRAIN_ROWS = ("ACTOR-S9", "SITE-ARENA-GROUP", "CARRIER-S27")
TEST_ROWS = ("TEST-RAW", "TEST-REALIZABLE")


def stab_raw_actor(H):
    """TEST-RAW at the ACTOR grain: |{sigma in S_9 : sigma F = F for every
    event}|, as the Young order of the participation signature."""
    return young_order(signature_blocks(H))


def stab_raw_cell(H):
    """TEST-RAW at the CARRIER grain: the same construction on the 27 cells,
    with the event footprints as the sets to be preserved."""
    return young_order(cell_signature_blocks(H))


def stab_realizable(H, autos):
    """TEST-REALIZABLE at all three grains at once: for every arena
    automorphism, whether it fixes every event (site leg) and whether it fixes
    every event's cell footprint (carrier leg)."""
    foot = [cell_footprint(F) for F in H]
    site_ok, cell_ok = 0, 0
    for (sp, cp) in autos:
        if all(frozenset(SITES[sp[SITE_INDEX[x]]] for x in F) == F for F in H):
            site_ok += 1
        if all(frozenset(cp[k] for k in f) == f for f in foot):
            cell_ok += 1
    return site_ok, cell_ok


def stab_raw_actor_bruteforce(H):
    """the independent route for TEST-RAW at the actor grain: FILTER the
    symmetric group explicitly.  Used on a declared sample as the check that
    the Young route is the same object and not a closed form trusted."""
    masks = []
    for F in H:
        m = 0
        for x in F:
            m |= 1 << SITE_INDEX[x]
        masks.append(m)
    n = 0
    for p in permutations(range(NACT)):
        ok = True
        for m in masks:
            im = 0
            for i in range(NACT):
                if m >> i & 1:
                    im |= 1 << p[i]
            if im != m:
                ok = False
                break
        if ok:
            n += 1
    return n


# ===========================================================================
# SECTION 9.  THE HEAD LAW
#
# The head is a FUNCTION of the census profile, exercised on every declared
# arena.  The two laws below DO type their return strings (K2 MINOR-8: the
# delivered comment claimed they did not, which was false of the code).  What
# is parsed from the pin's own bytes is the FAMILY SET those returns are
# checked against, at G-HEAD-WORDS-COME-FROM-THE-PIN and at
# G-EVERY-OUTCOME-WORD-EMITTABLE -- so a law that invented a vocabulary, or a
# repair that quietly widened one, fails a gate rather than a review.  That is
# the real and sufficient guarantee, and it is the one the paper states.
# ===========================================================================

def head_law(n_hist, actor_nonunique, cell_nonunique):
    """THE DECOMPOSITION WORD, DERIVED.

    FORCED     both grains admit exactly one factorization at every history
    DECLARED   both grains admit more than one somewhere, on the SAME
               histories -- one phenomenon, priced by its inventory
    STRATIFIED the grains disagree: one is uniform where the other is not, or
               the non-unique sets differ, so the answer carries a grain"""
    a, c = set(actor_nonunique), set(cell_nonunique)
    if not a and not c:
        return "FAC-FACTORIZATION-FORCED"
    if a and c and a == c:
        return "FAC-FACTORIZATION-DECLARED"
    return "FAC-STRATIFIED"


def atom_law(breaks, holds_at_complete):
    """THE ATOM WORD, DERIVED.  The atom theorem BREAKS at the groupoid grain
    exactly when some history whose global stabilizer is trivial carries a
    nontrivial coherent family at a declared coherence weaker than complete;
    it HOLDS when no such history exists."""
    if breaks > 0 and holds_at_complete:
        return "FAC-ATOM-BREAKS-AT-THE-GROUPOID-GRAIN"
    if breaks == 0:
        return "FAC-ATOM-HOLDS-AT-THE-GROUPOID-GRAIN"
    return "FAC-BLOCKED-AT-THE-GROUPOID-COMPLETE-RELATION"


def head_slot(word, actor_nonunique, cell_nonunique, n_hist,
              actor_inventory, cell_inventory, image=""):
    """the derived slot each outcome family carries: FORCED names its witness,
    DECLARED names its inventory, STRATIFIED names the grains -- and the
    actor-grain member carries the induced image it was taken at, because
    that image is a declared free item of the same leg."""
    if word == "FAC-FACTORIZATION-FORCED":
        return "WITNESS=%s" % (actor_inventory[0] if actor_inventory else "-")
    if word == "FAC-FACTORIZATION-DECLARED":
        return "INVENTORY=%s" % ",".join(actor_inventory)
    return ("BY-GRAIN=ACTOR-%d-OF-%d-UNIQUE-AT-THE-%s-IMAGE-vs-CARRIER-%d-OF-"
            "%d-UNIQUE" % (n_hist - len(actor_nonunique), n_hist, image,
                           n_hist - len(cell_nonunique), n_hist))


# ===========================================================================
# SECTION 10.  THE RUN
# ===========================================================================

def full_run(break_anchor=None, paper_text=None, paper_rel=PAPER_REL,
             write=True):
    R = {"schema": {"unit": "FAC", "paper": "paper-35-fac",
                    "pin": PIN_REL, "ledger": 300,
                    "cites": {"engravings": ["E-22", "E-23", "E-24"],
                              "runbook_and_ledger_rules":
                                  [20, 34, 46, 62, 82, 87, 91, 119, 125,
                                   267, 269, 293, 295, 299, 300],
                              "sibling_papers":
                                  [19, 20, 21, 28, 29, 31, 33, 35],
                              "programme": [14]}},
         "arithmetic": "exact integers and Z[w] pairs; no float anywhere",
         "python": "%d.%d" % sys.version_info[:2]}
    src = read_text(SELF, "SELF")

    say("=" * 78)
    say("FAC (PAPER-35) -- THE FACTORIZATION UNIT")
    say("=" * 78)
    say()
    say("SECTION 1.  PROVENANCE")

    prov = []
    for (aid, rel, sha, why) in SOURCES:
        raw = read_bytes(rel)
        got = hashlib.sha256(raw).hexdigest()[:12]
        if break_anchor == aid:
            got = "0" * 12
        prov.append({"anchor": aid, "path": rel, "declared": sha,
                     "measured": got, "match": got == sha, "role": why,
                     "bytes": len(raw)})
        reg(len(raw))
    R["provenance"] = prov
    texts = {rel: read_bytes(rel).decode("utf-8") for (_a, rel, _s, _w)
             in SOURCES}
    LD.gate("G-PROVENANCE-SHA-PINNED",
            "EVERY SOURCE IS READ AT A PINNED DIGEST (#46/#91).  This run "
            "reads exactly %d committed files as sources and one file as the "
            "object under test; each source's bytes are digested and compared "
            "with the declaration frozen in this file, and every source's "
            "product is consumed by a gate below.  No subprocess is invoked "
            "and no repository state outside these paths is read, so the run "
            "is correct off-tree and with no version control present"
            % len(SOURCES),
            all(p["match"] for p in prov),
            "sources %d, matched %d, mismatched %s"
            % (len(prov), sum(1 for p in prov if p["match"]),
               [p["anchor"] for p in prov if not p["match"]] or "none"))
    SEAL.take("SEAL-SCHEMA", R)
    SEAL.take("SEAL-PROVENANCE", R)

    van = []
    for (vid, aid, quote, gate_name) in VERBATIM:
        rel = [s[1] for s in SOURCES if s[0] == aid][0]
        hit = match_needle(texts[rel], quote)
        if break_anchor == vid:
            hit = False
        van.append({"id": vid, "source": aid, "path": rel,
                    "chars": len(canon(quote)), "present": hit,
                    "consumer_gate": gate_name})
        reg(len(canon(quote)))
    R["verbatim_anchors"] = van
    LD.gate("G-VERBATIM-ANCHORS-IN-SOURCE",
            "EVERY VERBATIM ANCHOR IS PRESENT IN ITS SOURCE'S BYTES (#62 + "
            "#125).  %d anchors, each above the length floor of %d "
            "characters, each matched after markdown-prefix, emphasis and "
            "ASCII-fold normalisation and again with whitespace removed, and "
            "each NAMED WITH THE GATE THAT CONSUMES IT -- an anchor no gate "
            "consumes is decoration" % (len(van), NEEDLE_FLOOR),
            all(v["present"] for v in van)
            and all(v["consumer_gate"] for v in van),
            "anchors %d, present %d, absent %s"
            % (len(van), sum(1 for v in van if v["present"]),
               [v["id"] for v in van if not v["present"]] or "none"))
    SEAL.take("SEAL-VERBATIM", R)

    pin_text = texts[PIN_REL]
    parsed = sorted(set(OUTCOME_PAT.findall(pin_text)))
    if mut("MUT-OUTCOME-TYPED"):
        parsed = ["FAC-FACTORIZATION-FORCED-<witness>"]
    families = sorted({w.split("-<")[0].rstrip("-") for w in parsed})
    R["pre_registered_outcomes"] = {
        "raw": parsed, "families": families,
        "route": "parsed out of the pin's own bytes by a regular expression; "
                 "this file types no outcome word of its own"}
    LD.gate("G-OUTCOMES-PARSED-FROM-THE-PIN",
            "THE OUTCOME VOCABULARY IS THE PIN'S, NOT THIS FILE'S.  The %d "
            "pre-registered outcome strings are extracted from the pin's "
            "bytes at the digest gated above and reduced to %d families; the "
            "head law below is required to return words from this set and "
            "from no other, so a head that invents a word cannot pass"
            % (len(parsed), len(families)),
            len(parsed) >= 5 and len(families) >= 4,
            "raw %d, families %d: %s" % (len(parsed), len(families),
                                         ", ".join(families)))
    SEAL.take("SEAL-OUTCOMES", R)

    say()
    say("SECTION 2.  THE ARENA, THE CARRIER AND THE CORPORA")

    C = raw_census()
    parts = C["parts"]
    sat = C["sat"]
    strict = strict_triples()
    flatq = flat_quadruples()
    scheds, smeta = window_schedules(flatq, parts)
    autos = arena_automorphisms()
    R["arena"] = {
        "sites": NACT, "declared_links": len(I7_LINKS),
        "link_directions": [list(l) for l in I7_LINKS],
        "parallel_classes": len(CLASS_NAMES),
        "groupings": len(parts), "saturating_groupings": len(sat),
        "strict_triples": len(strict), "flat_quadruples": len(flatq),
        "window_schedules": len(scheds),
        "arena_automorphism_order": len(autos),
        "actor_lattice": bell(NACT), "carrier_lattice": bell(DIM),
    }
    reg(NACT, len(I7_LINKS), len(CLASS_NAMES), len(parts), len(sat),
        len(strict), len(flatq), len(scheds), len(autos), bell(NACT),
        bell(DIM), DIM, 3, len(SOURCES), len(VERBATIM))
    LD.gate("G-ARENA-SHAPE",
            "THE ARENA IS THE PARENTS' ARENA, REBUILT HERE FROM ITS OWN "
            "DEFINITIONS.  AG(2,3) with %d sites and %d declared link "
            "directions of the %d parallel classes; %s groupings of the nine "
            "sites into three triples, %d of them saturating; %d I7-STRICT "
            "triples at R = 3 and %d G-FLAT quadruples; paper-21's driven "
            "window at %d schedules; and the arena's own automorphism group "
            "-- the affine maps permuting the declared directions -- at order "
            "%d.  Every one of these is enumerated by this file's own "
            "constructor and none is typed"
            % (NACT, len(I7_LINKS), len(CLASS_NAMES), com(len(parts)),
               len(sat), len(strict), len(flatq), len(scheds), len(autos)),
            len(parts) == pick("MUT-PARTITION", len(all_groupings()), 0)
            and len(sat) == sum(1 for v in C["vecs"] if sum(v) == NACT)
            and len(autos) == len(set(autos)) and len(autos) > 0,
            "groupings %d, saturating %d, triples %d, quadruples %d, "
            "schedules %d, |Aut| %d"
            % (len(parts), len(sat), len(strict), len(flatq), len(scheds),
               len(autos)))
    SEAL.take("SEAL-ARENA", R)

    pairs = {}
    for k, c in enumerate(CELLS):
        pairs.setdefault(codivision_pair(c), []).append(k)
    two_actor = sum(1 for c in CELLS if len(codivision_pair(c)) == 2)
    per_actor = Counter()
    for c in CELLS:
        for x in codivision_pair(c):
            per_actor[x] += 1
    R["carrier"] = {
        "cells": DIM, "distinct_co_division_pairs": len(pairs),
        "cell_to_pair_is_a_bijection": len(pairs) == DIM
        and all(len(v) == 1 for v in pairs.values()),
        "cells_with_exactly_two_actors": two_actor,
        "cells_per_actor": sorted(set(per_actor.values())),
        "actors_in_that_many_cells": len(per_actor),
    }
    reg(two_actor, len(pairs), sorted(set(per_actor.values()))[0],
        len(per_actor))
    LD.gate("G-CELL-IS-A-CO-DIVISION-PAIR",
            "THE CARRIER IS OCC'S CARRIER, VERIFIED HERE AS A BIJECTION.  The "
            "%d cells this unit factorizes are exactly the %d unordered "
            "co-division pairs of the declared links: each cell carries %d "
            "actors at %d of %d cells, and each of the %d actors sits in %d "
            "cells.  The map cell -> pair is injective and surjective, "
            "measured pair by pair, so a partition of the cells IS a "
            "partition of the co-division pairs"
            % (DIM, len(pairs), 2, two_actor, DIM, len(per_actor),
               sorted(set(per_actor.values()))[0]),
            pick("MUT-CARRIER", R["carrier"]["cell_to_pair_is_a_bijection"],
                 False)
            and two_actor == DIM and len(set(per_actor.values())) == 1,
            "cells %d, pairs %d, two-actor cells %d, cells per actor %s"
            % (DIM, len(pairs), two_actor, sorted(set(per_actor.values()))))
    SEAL.take("SEAL-CARRIER", R)

    corp = []
    for t in strict:
        Ps = [parts[i] for i in t]
        corp.append(("C1", history_of(Ps, [canon_transversals(P)[0]
                                           for P in Ps])))
    c1n = len(corp)
    c1h = [h for (_t, h) in corp]
    for a in c1h:
        for b in c1h:
            corp.append(("C2", a + b))
    c2n = len(corp) - c1n
    for sch, tag in zip(scheds, smeta):
        corp.append(("C3", history_of([p for p, _s in sch],
                                      [s for _p, s in sch])))
    c3n = len(corp) - c1n - c2n
    lens = Counter(len(h) for (_t, h) in corp)
    R["corpora"] = {
        "C1_strict_triples": c1n, "C2_concatenations": c2n,
        "C3_window_schedules": c3n, "total_histories": len(corp),
        "distinct_histories": len({h for (_t, h) in corp}),
        "events_per_history": {str(k): v for k, v in sorted(lens.items())},
        "C3_tags": {k: v for k, v in sorted(Counter(smeta).items())},
    }
    reg(c1n, c2n, c3n, len(corp), len({h for (_t, h) in corp}),
        *sorted(lens))
    for k, v in sorted(Counter(smeta).items()):
        reg(v)
    LD.gate("G-CORPORA-SHAPE",
            "THE HISTORY CORPUS IS THE PARENTS' CORPUS, PER OBJECT.  %d "
            "I7-STRICT triples, their %s ordered concatenations and the %d "
            "driven-window schedules give %s committed histories; every one "
            "is checked to be a sequence of three-actor division events "
            "whose rounds partition the nine actors, and the event counts "
            "found are %s -- one per round per group, no other shape present"
            % (c1n, com(c2n), c3n, com(len(corp)),
               ", ".join(str(k) for k in sorted(lens))),
            c2n == c1n * c1n and len(corp) == c1n + c2n + c3n
            and all(len(F) == 3 for (_t, h) in corp for F in h)
            and all(len(h) % 3 == 0 for (_t, h) in corp),
            "C1 %d, C2 %d, C3 %d, total %d, distinct %d"
            % (c1n, c2n, c3n, len(corp), len({h for (_t, h) in corp})))
    SEAL.take("SEAL-CORPORA", R)

    # THE CORPUS IS A MULTISET, AND SAYS SO (K3 m4).  Every count this unit
    # publishes over the corpus is a count over SLOTS; the driven window
    # reaches some histories more than once, and the multiplicity table is
    # published so a reader can convert.
    mrows = []
    for tag in ("C1", "C2", "C3"):
        hs = [h for (t, h) in corp if t == tag]
        mult = Counter(Counter(hs).values())
        mrows.append({"corpus": tag, "slots": len(hs),
                      "distinct": len(set(hs)),
                      "multiplicities": {str(a): b
                                         for a, b in sorted(mult.items())}})
    hist_mult = Counter(h for (_t, h) in corp)
    allmult = Counter(hist_mult.values())
    repeated = sum(1 for v in hist_mult.values() if v > 1)
    max_mult = max(hist_mult.values())
    R["corpus_multiset"] = {
        "histories_appearing_more_than_once": repeated,
        "largest_multiplicity": max_mult,
        "rows": mrows,
        "slots": len(corp),
        "distinct": len({h for (_t, h) in corp}),
        "duplicate_slots": len(corp) - len({h for (_t, h) in corp}),
        "multiplicities": {str(a): b for a, b in sorted(allmult.items())},
        "reading": "the corpus is the parents' window and it is a MULTISET: "
                   "counts published as `of %s' are counts over corpus "
                   "SLOTS, not over distinct histories, and the two differ "
                   "wherever the driven window reaches a history more than "
                   "once" % com(len(corp)),
    }
    for r in mrows:
        reg(r["slots"], r["distinct"])
        for a, b in r["multiplicities"].items():
            reg(int(a), b)
    for a, b in allmult.items():
        reg(a, b)
    reg(len(corp) - len(hist_mult), repeated, max_mult)
    LD.gate("G-THE-CORPUS-IS-A-MULTISET",
            "THE CORPUS'S OWN MULTIPLICITIES ARE PUBLISHED (K3 m4).  The %s "
            "committed histories are %s SLOTS carrying %s distinct histories: "
            "%s and %s are duplicate-free, and the %d driven-window schedules "
            "yield %d distinct histories, %d of them appearing %d times each. "
            " Every `N of %s' in this unit is therefore a count over slots, "
            "and the conversion is published rather than left to a reader"
            % (com(len(corp)), com(len(corp)), com(len(hist_mult)),
               mrows[0]["corpus"], mrows[1]["corpus"], mrows[2]["slots"],
               mrows[2]["distinct"], repeated, max_mult, com(len(corp))),
            pick("MUT-MULTISET",
                 sum(r["slots"] for r in mrows) == len(corp), False)
            and all(r["distinct"] <= r["slots"] for r in mrows)
            and sum(int(a) * b for a, b in allmult.items()) == len(corp)
            and sum(allmult.values()) == len(hist_mult),
            "slots %d, distinct %d, duplicates %d, multiplicities %s"
            % (len(corp), len(hist_mult), len(corp) - len(hist_mult),
               {str(a): b for a, b in sorted(allmult.items())}))
    SEAL.take("SEAL-MULTISET", R)

    say()
    say("SECTION 3.  THE CRITERION, FROZEN BEFORE THE FIRST CENSUS ROW")

    csrc = criterion_source(src)
    creads = criterion_reads(src)
    allowed = set(CRITERION_ALLOWED_NAMES)
    outside = sorted({n for names in creads.values() for n in names
                      if n not in allowed})
    leaks = sorted({n for names in creads.values() for n in names
                    if n in CRITERION_FORBIDDEN_NAMES})
    whitelist_is_clean = not (allowed & set(CRITERION_FORBIDDEN_NAMES))
    P9 = all_set_partitions(SITES)
    window = build_cell_window(P9)
    winlist = sorted(window)
    R["criterion"] = {
        "legs": ["LEG-1-GEOMETRY", "LEG-2-HISTORY", "LEG-3-RECORD",
                 "LEG-4-DYNAMICS"],
        "statement": "a partition is LAW-COMPATIBLE at a history exactly when "
                     "the committed link/shift structure, the division events, "
                     "the record field and paper-20's one-step operator all "
                     "DESCEND along the identifications the partition induces",
        "functions": csrc,
        "combined_sha256_12": digest(
            [sorted((k, v["sha256_12"]) for k, v in csrc.items()),
             sorted(CRITERION_ALLOWED_NAMES)]),
        "free_names": creads,
        "allowed_names": sorted(CRITERION_ALLOWED_NAMES),
        "names_outside_the_whitelist": outside,
        "census_products_referenced": leaks,
        "whitelist_excludes_every_forbidden_spelling": whitelist_is_clean,
        "leak_test": "WHITELIST -- every free name of every criterion "
                     "function must appear in the declared allow list; a "
                     "blacklist of spellings is defeated by an alias, by "
                     "globals() and by a default argument, and was",
        "induced_images": ["induced_cell_partition (DIRECTIONWISE)",
                           "pairwise_cell_partition (PAIRWISE)"],
        "coin_orders": list(COIN_ORDERS),
    }
    reg(len(csrc), sum(v["lines"] for v in csrc.values()),
        len(CRITERION_ALLOWED_NAMES))
    LD.gate("G-CRITERION-FROZEN-BEFORE-THE-CENSUS",
            "THE CRITERION IS DECLARED AND DIGESTED BEFORE ANY CENSUS ROW "
            "RUNS, AND ITS FREE NAMES ARE A WHITELIST.  Its %d functions -- "
            "%s lines in all -- are located by AST in this file's own source "
            "and digested here, at a point in the run where not one "
            "admissible set has yet been computed.  Every free name each leg "
            "references is then required to lie in the declared list of %d "
            "allowed names -- the arena's constants, the folding helpers, the "
            "criterion's own members and the builtins it uses -- so an alias, "
            "a globals() lookup and a default-argument smuggle all fail here, "
            "which a blacklist of spellings does not.  The whitelist is part "
            "of the combined digest, so widening it moves the digest the "
            "paper states.  The four legs are %s"
            % (len(csrc), sum(v["lines"] for v in csrc.values()),
               len(CRITERION_ALLOWED_NAMES),
               ", ".join(R["criterion"]["legs"])),
            len(csrc) == len(CRITERION_FUNCS) and whitelist_is_clean
            and not pick("MUT-CRITERION-LEAK", outside, ["actor_census"])
            and not leaks,
            "functions %d of %d declared, combined digest %s, names outside "
            "the whitelist %s, forbidden spellings %s"
            % (len(csrc), len(CRITERION_FUNCS),
               R["criterion"]["combined_sha256_12"], outside or "none",
               leaks or "none"))
    SEAL.take("SEAL-CRITERION", R)

    say()
    say("SECTION 4.  MEASUREMENT ONE -- THE DECOMPOSITION CENSUS")

    BM = [block_map(p) for p in P9]
    leg1_actor_set = [i for i, p in enumerate(P9) if leg1_actor(p, BM[i])]
    subgroup_cosets = []
    subs = [[(0, 0)]] + [[(0, 0), CLASS_DIR[k], vmul(2, CLASS_DIR[k])]
                         for k in CLASS_NAMES] + [list(SITES)]
    for Hs in subs:
        cos = {}
        for x in SITES:
            key = tuple(sorted(vadd(x, h) for h in Hs))
            cos.setdefault(key, set()).add(x)
        subgroup_cosets.append(tuple(sorted(tuple(sorted(v))
                                            for v in cos.values())))
    subgroup_cosets = sorted(set(subgroup_cosets))
    leg1_names = [actor_partition_name(P9[i]) for i in leg1_actor_set]
    R["actor_census"] = {
        "lattice": len(P9),
        "leg1_geometry_survivors": len(leg1_actor_set),
        "leg1_survivor_names": leg1_names,
        "subgroup_coset_partitions": len(subgroup_cosets),
        "leg1_equals_the_subgroup_cosets":
            sorted(P9[i] for i in leg1_actor_set) == subgroup_cosets,
    }
    reg(len(leg1_actor_set), len(subgroup_cosets))
    LD.gate("G-LEG1-IS-THE-SUBGROUP-COSET-THEOREM",
            "THE GEOMETRY LEG HAS A CLOSED FORM, AND IT IS MEASURED AGAINST "
            "IT.  Of the %s partitions of the nine actors exactly %d survive "
            "LEG-1, and the set they form is compared -- as a set of "
            "partitions, not as a count -- with the coset partitions of the "
            "%d subgroups of the translation group of AG(2,3), independently "
            "constructed.  The two agree, so the geometry leg admits the "
            "trivial partition, the four parallel classes and the discrete "
            "partition and nothing else"
            % (com(len(P9)), len(leg1_actor_set), len(subs)),
            pick("MUT-LEG1-THEOREM",
                 R["actor_census"]["leg1_equals_the_subgroup_cosets"], False),
            "lattice %d, survivors %d, coset partitions %d, set-equal %s"
            % (len(P9), len(leg1_actor_set), len(subgroup_cosets),
               R["actor_census"]["leg1_equals_the_subgroup_cosets"]))

    leg1_cell_survivors = [p for p in winlist if leg1_cell(p)]
    cell_names = [cell_partition_name(p, window[p])
                  for p in leg1_cell_survivors]
    # THE CARRIER SURVIVORS, ONE ROW EACH (K2 MAJOR-5).  The block-shape name
    # is not injective -- five of these ten partitions share one name -- so
    # the referent published here is the BLOCK PARTITION ITSELF, indexed, with
    # its shape and the window families that produced it beside it.  An
    # inventory keyed by name alone sums over five distinct objects.
    cell_survivor_rows = [
        {"index": j, "name": cell_names[j], "blocks": len(p),
         "block_sizes": sorted(Counter(len(b) for b in p).items()),
         "families": window[p],
         "partition": [list(b) for b in p]}
        for j, p in enumerate(leg1_cell_survivors)]
    cell_name_collisions = {k: v for k, v in
                            sorted(Counter(cell_names).items()) if v > 1}
    R["cell_census"] = {
        "window": len(winlist), "ambient": bell(DIM),
        "leg1_geometry_survivors": len(leg1_cell_survivors),
        "leg1_survivor_names": cell_names,
        "leg1_survivors": cell_survivor_rows,
        "distinct_leg1_survivor_names": len(set(cell_names)),
        "colliding_names": cell_name_collisions,
        "families": {k: v for k, v in sorted(Counter(
            f for p in leg1_cell_survivors for f in window[p]).items())},
    }
    reg(len(leg1_cell_survivors), len(set(cell_names)))
    for v in R["cell_census"]["families"].values():
        reg(v)
    for r in cell_survivor_rows:
        reg(r["blocks"], *[c for _s, c in r["block_sizes"]])
        reg(*[s for s, _c in r["block_sizes"]])

    # the four declared sub-families of the carrier window, so the headline's
    # window-sensitivity is priced rather than left to the window's status
    # (K1 MINOR-7).  Each survivor's provenance decides its memberships.
    CELL_SUBWINDOWS = ("THE-STRATA", "DIRECTIONWISE-IMAGES",
                       "PAIRWISE-IMAGES", "THE-DECLARED-WINDOW")
    sub_of = []
    for p in leg1_cell_survivors:
        fams = set(window[p])
        row = {"THE-DECLARED-WINDOW"}
        if "DIRECTIONWISE" in fams:
            row.add("DIRECTIONWISE-IMAGES")
        if "PAIRWISE" in fams:
            row.add("PAIRWISE-IMAGES")
        if fams - {"DIRECTIONWISE", "PAIRWISE"}:
            row.add("THE-STRATA")
        sub_of.append(row)

    actor_rows, cell_rows = [], []
    coin_rows = {o: 0 for o in COIN_ORDERS}
    coin_disagree = 0
    a_non, c_non = [], []
    a_cards, c_cards = Counter(), Counter()
    a_inventory, c_inventory = Counter(), Counter()
    rec_nonconstant = 0
    # the induced-image fiber, run entire
    pw_rows, pw_non = [], []
    pw_cards, pw_inventory = Counter(), Counter()
    pw_coin = {o: 0 for o in COIN_ORDERS}
    pw_disagree = 0
    # the per-grain leg tallies (K1 MAJOR-3 = K2 MAJOR-3)
    leg_eval = {"actor": Counter(), "carrier": Counter()}
    no4_cards = {"actor": Counter(), "carrier": Counter()}
    wedge_corpus = {"actor": 0, "carrier": 0}
    fine_checked, fine_disagree = 0, 0
    sub_cards = {nm: Counter() for nm in CELL_SUBWINDOWS}
    seen_hist = set()
    leg4_kills_distinct = {"actor": 0, "carrier": 0}
    for k, (tag, H) in enumerate(corp):
        rel = codivision(H)
        rec = record_field(H, rel)
        rows = {tuple(rec[SITE_INDEX[x] * 3 + i] for i in range(3))
                for x in SITES}
        if len(rows) > 1:
            rec_nonconstant += 1
        first_time = H not in seen_hist
        seen_hist.add(H)
        foot = [cell_footprint(F) for F in H]
        adm_a, adm_pw = [], []
        no4_a = 0
        for j, i in enumerate(leg1_actor_set):
            v = admissible_actor(P9[i], H, rec, BM[i])
            if v[1] and v[2]:
                no4_a += 1
                leg_eval["actor"]["leg4_evaluations"] += 1
                if not v[5]:
                    leg_eval["actor"]["leg4_failures"] += 1
                    if first_time:
                        leg4_kills_distinct["actor"] += 1
                fine_checked += 2
                cp = induced_cell_partition(P9[i])
                if leg4_cell_summed(cp, rec, COIN_ORDERS[0]) != v[3]:
                    fine_disagree += 1
                if leg4_cell_summed(cp, rec, COIN_ORDERS[1]) != v[4]:
                    fine_disagree += 1
            if v[1]:
                leg_eval["actor"]["leg3_evaluations"] += 1
                if not v[2]:
                    leg_eval["actor"]["leg3_failures"] += 1
            if (not v[2]) and leg4_cell(induced_cell_partition(P9[i]), rec,
                                        COIN_ORDERS[0]) \
                    and leg4_cell(induced_cell_partition(P9[i]), rec,
                                  COIN_ORDERS[1]):
                wedge_corpus["actor"] += 1
            if v[3] is not None and v[3] != v[4]:
                coin_disagree += 1
            for o, val in zip(COIN_ORDERS, (v[3], v[4])):
                if val:
                    coin_rows[o] += 1
            if v[5]:
                adm_a.append(leg1_names[j])
            w = admissible_actor(P9[i], H, rec, BM[i],
                                 pairwise_cell_partition)
            if w[3] is not None and w[3] != w[4]:
                pw_disagree += 1
            for o, val in zip(COIN_ORDERS, (w[3], w[4])):
                if val:
                    pw_coin[o] += 1
            if w[5]:
                adm_pw.append(leg1_names[j])
        no4_cards["actor"][no4_a] += 1
        adm_c, no4_c = [], 0
        adm_idx = []
        for j, p in enumerate(leg1_cell_survivors):
            v = admissible_cell(p, foot, rec, True)
            if v[1] and v[2]:
                no4_c += 1
                leg_eval["carrier"]["leg4_evaluations"] += 1
                if not v[5]:
                    leg_eval["carrier"]["leg4_failures"] += 1
                    if first_time:
                        leg4_kills_distinct["carrier"] += 1
                fine_checked += 2
                if leg4_cell_summed(p, rec, COIN_ORDERS[0]) != v[3]:
                    fine_disagree += 1
                if leg4_cell_summed(p, rec, COIN_ORDERS[1]) != v[4]:
                    fine_disagree += 1
            if v[1]:
                leg_eval["carrier"]["leg3_evaluations"] += 1
                if not v[2]:
                    leg_eval["carrier"]["leg3_failures"] += 1
            if (not v[2]) and leg4_cell(p, rec, COIN_ORDERS[0]) \
                    and leg4_cell(p, rec, COIN_ORDERS[1]):
                wedge_corpus["carrier"] += 1
            if v[3] is not None and v[3] != v[4]:
                coin_disagree += 1
            for o, val in zip(COIN_ORDERS, (v[3], v[4])):
                if val:
                    coin_rows[o] += 1
            if v[5]:
                adm_c.append(cell_names[j])
                adm_idx.append(j)
        no4_cards["carrier"][no4_c] += 1
        for nm in CELL_SUBWINDOWS:
            sub_cards[nm][sum(1 for j in adm_idx if nm in sub_of[j])] += 1
        a_cards[len(adm_a)] += 1
        c_cards[len(adm_c)] += 1
        pw_cards[len(adm_pw)] += 1
        for nm in adm_a:
            a_inventory[nm] += 1
        for nm in adm_c:
            c_inventory[nm] += 1
        for nm in adm_pw:
            pw_inventory[nm] += 1
        if len(adm_a) != 1:
            a_non.append(k)
            actor_rows.append({"index": k, "corpus": tag,
                               "admissible": sorted(adm_a),
                               "cardinality": len(adm_a)})
        if len(adm_pw) != 1:
            pw_non.append(k)
            pw_rows.append({"index": k, "corpus": tag,
                            "admissible": sorted(adm_pw),
                            "cardinality": len(adm_pw)})
        if len(adm_c) != 1:
            c_non.append(k)
            cell_rows.append({"index": k, "corpus": tag,
                              "admissible": sorted(adm_c),
                              "cardinality": len(adm_c),
                              "admissible_indices": adm_idx})
    R["actor_census"].update({
        "histories": len(corp),
        "induced_image": "DIRECTIONWISE",
        "cardinality_distribution": {str(k): v for k, v in
                                     sorted(a_cards.items())},
        "unique_at": a_cards[1], "non_unique_at": len(a_non),
        "non_unique_rows": actor_rows,
        "inventory": {k: v for k, v in sorted(a_inventory.items())},
    })
    R["actor_census_pairwise"] = {
        "lattice": len(P9),
        "leg1_geometry_survivors": len(leg1_actor_set),
        "histories": len(corp),
        "induced_image": "PAIRWISE",
        "cardinality_distribution": {str(k): v for k, v in
                                     sorted(pw_cards.items())},
        "unique_at": pw_cards[1], "non_unique_at": len(pw_non),
        "non_unique_rows": pw_rows,
        "inventory": {k: v for k, v in sorted(pw_inventory.items())},
        "leg4_passes_per_order": dict(sorted(pw_coin.items())),
        "rows_where_the_orders_disagree": pw_disagree,
        "declaration": "the SECOND member of the induced-image fiber, run "
                       "entire on the same criterion, the same corpus and "
                       "the same LEG-1 survivors; only the map that carries "
                       "an actor partition to the carrier differs",
    }
    R["cell_census"].update({
        "histories": len(corp),
        "cardinality_distribution": {str(k): v for k, v in
                                     sorted(c_cards.items())},
        "unique_at": c_cards[1], "non_unique_at": len(c_non),
        "non_unique_rows": cell_rows,
        "inventory": {k: v for k, v in sorted(c_inventory.items())},
        "sub_window_censuses": [
            {"sub_window": nm,
             "survivors": sum(1 for r in sub_of if nm in r),
             "cardinality_distribution": {str(a): b for a, b in
                                          sorted(sub_cards[nm].items())},
             "unique_at": sub_cards[nm][1]}
            for nm in CELL_SUBWINDOWS],
    })
    reg(a_cards[1], len(a_non), c_cards[1], len(c_non), rec_nonconstant,
        pw_cards[1], len(pw_non), pw_disagree, *sorted(pw_coin.values()))
    for d in (a_cards, c_cards, a_inventory, c_inventory, pw_cards,
              pw_inventory):
        for v in d.values():
            reg(v)
    for kk in list(a_cards) + list(c_cards) + list(pw_cards):
        reg(kk)
    for row in R["cell_census"]["sub_window_censuses"]:
        reg(row["survivors"], row["unique_at"])
        for a, b in row["cardinality_distribution"].items():
            reg(int(a), b)

    # THE CARRIER GRAIN'S INVENTORY, ENUMERATED AND PRICED (K2 MAJOR-5).  The
    # pin requires the inventory of a grain that admits more than one; the
    # carrier grain is that grain and this is its inventory: the admissible
    # SETS, grouped, with the partitions named by index rather than by their
    # colliding block-shape names.
    inv_prof = Counter()
    for r in cell_rows:
        if r["index"] not in set(a_non):
            inv_prof[tuple(r["admissible_indices"])] += 1
    carrier_only_profiles = [
        {"admissible_partitions": list(k),
         "block_counts": [len(leg1_cell_survivors[j]) for j in k],
         "names": [cell_names[j] for j in k],
         "histories": v} for k, v in sorted(inv_prof.items())]
    widest = max(cell_rows, key=lambda r: r["cardinality"])
    R["cell_census"]["inventory_by_admissible_set"] = carrier_only_profiles
    R["cell_census"]["widest_row"] = {
        "index": widest["index"], "corpus": widest["corpus"],
        "cardinality": widest["cardinality"],
        "admissible_partitions": widest["admissible_indices"],
        "block_counts": [len(leg1_cell_survivors[j])
                         for j in widest["admissible_indices"]],
        "names": widest["admissible"],
        "includes_the_one_block_partition_of_the_whole_carrier":
            any(len(leg1_cell_survivors[j]) == 1
                for j in widest["admissible_indices"]),
        "reading": "at this one history the committed structure descends to "
                   "a quotient with a single object: the one-block partition "
                   "of all the cells is admissible",
    }
    for r in carrier_only_profiles:
        reg(r["histories"], *r["block_counts"])
    reg(widest["cardinality"], *R["cell_census"]["widest_row"]
        ["block_counts"])
    LD.gate("G-ACTOR-GRAIN-ADMISSIBLE-PER-HISTORY",
            "THE ACTOR-GRAIN ADMISSIBLE SET IS COUNTED PER HISTORY, NOT IN "
            "AGGREGATE (#87), AND IT CARRIES THE IMAGE IT WAS TAKEN AT.  At "
            "each of the %s committed histories the criterion is evaluated on "
            "every LEG-1 survivor at the DIRECTIONWISE induced image and the "
            "admissible set is listed by name: cardinality one at %s "
            "histories and greater than one at %d.  The discrete "
            "nine-block partition is admissible at every history -- checked "
            "history by history -- so the count is never zero and the "
            "question is always whether anything JOINS it"
            % (com(len(corp)), com(a_cards[1]), len(a_non)),
            pick("MUT-ACTOR-CENSUS", a_cards[1], 0) + len(a_non) == len(corp)
            and min(a_cards) >= 1
            and all(any(n.startswith("AP-9-BLOCKS") for n in r["admissible"])
                    for r in actor_rows),
            "unique %d, non-unique %d, cardinalities %s, image %s"
            % (a_cards[1], len(a_non), sorted(a_cards),
               R["actor_census"]["induced_image"]))
    SEAL.take("SEAL-ACTOR", R)

    img_rows = [
        {"induced_image": "DIRECTIONWISE",
         "map": "(x, l) ~ (y, l) whenever x ~ y",
         "unique": a_cards[1], "non_unique": len(a_non),
         "histories": len(corp),
         "inventory_at_the_non_unique":
             sorted({n for r in actor_rows for n in r["admissible"]
                     if not n.startswith("AP-9-BLOCKS")}),
         "leg4_passes_per_order": dict(sorted(coin_rows.items()))},
        {"induced_image": "PAIRWISE",
         "map": "{x, x + l} ~ {y, y + m} whenever the block pairs agree",
         "unique": pw_cards[1], "non_unique": len(pw_non),
         "histories": len(corp),
         "inventory_at_the_non_unique":
             sorted({n for r in pw_rows for n in r["admissible"]
                     if not n.startswith("AP-9-BLOCKS")}),
         "leg4_passes_per_order": dict(sorted(pw_coin.items()))},
    ]
    if mut("MUT-IMAGE-SWAP"):
        img_rows[0]["induced_image"], img_rows[1]["induced_image"] = (
            img_rows[1]["induced_image"], img_rows[0]["induced_image"])
    img_min = min(r["unique"] for r in img_rows)
    img_lost = sorted(set(img_rows[0]["inventory_at_the_non_unique"])
                      - set(img_rows[1]["inventory_at_the_non_unique"]))
    R["image_fiber"] = {
        "rows": img_rows,
        "declared_members": len(img_rows),
        "fiber": "INERT" if len({r["unique"] for r in img_rows}) == 1
                 else "LIVE",
        "division_is_forced_at_least_at": img_min,
        "histories": len(corp),
        "class_partitions_that_leave_the_inventory": img_lost,
        "robust_corollary": "under EITHER image the division is forced at "
                            "at least %s of %s committed histories; the "
                            "fiber moves only which degenerate histories tie"
                            % (com(img_min), com(len(corp))),
        "duty": "the coin-order precedent (#293) applied to a second free "
                "item of the same leg: both declared members are run and "
                "both are published, and the head's actor-grain fields carry "
                "the image they were taken at",
    }
    reg(img_min, len(img_rows))
    LD.gate("G-BOTH-INDUCED-IMAGES-CENSUSED",
            "LEG-4 AT THE ACTOR GRAIN CARRIES AN IMAGE, AND BOTH DECLARED "
            "IMAGES ARE RUN (#293's duty, applied to the second free item of "
            "the same leg).  LEG-4 is a predicate on a CARRIER partition, so "
            "an actor partition reaches it through a map, and this unit's own "
            "window declares two: the DIRECTIONWISE image and the PAIRWISE "
            "image the carrier's typing suggests.  Both are censused entire "
            "on the same corpus and the same LEG-1 survivors: %s of %s "
            "unique at the directionwise image and %s of %s at the pairwise "
            "one, so the fiber is %s -- and each image's census is compared "
            "here with the census published under its own name, so an "
            "image-label swap fails.  The robust reading is the minimum: "
            "under either image the division is forced at at least %s of %s"
            % (com(a_cards[1]), com(len(corp)), com(pw_cards[1]),
               com(len(corp)), R["image_fiber"]["fiber"], com(img_min),
               com(len(corp))),
            len(img_rows) == 2
            and img_rows[0]["unique"] == R["actor_census"]["unique_at"]
            and img_rows[1]["unique"] ==
            R["actor_census_pairwise"]["unique_at"]
            and img_rows[0]["induced_image"] ==
            R["actor_census"]["induced_image"]
            and img_rows[1]["induced_image"] ==
            R["actor_census_pairwise"]["induced_image"]
            and pick("MUT-IMAGE-STAMP", R["image_fiber"]["fiber"], "INERT")
            == ("INERT" if a_cards[1] == pw_cards[1] else "LIVE")
            and img_min == min(a_cards[1], pw_cards[1]),
            "directionwise %d of %d, pairwise %d of %d, fiber %s, forced at "
            "least at %d, class partitions that leave %s"
            % (a_cards[1], len(corp), pw_cards[1], len(corp),
               R["image_fiber"]["fiber"], img_min, img_lost or "none"))
    SEAL.take("SEAL-PAIRWISE", R)
    SEAL.take("SEAL-IMAGE", R)
    LD.gate("G-CARRIER-GRAIN-ADMISSIBLE-PER-HISTORY",
            "THE CARRIER-GRAIN ADMISSIBLE SET IS COUNTED PER HISTORY ON A "
            "DECLARED WINDOW.  The %s-member carrier window is reduced by "
            "the geometry leg to %d survivors, and those are evaluated at "
            "every history: cardinality one at %s and greater than one at "
            "%d, with cardinalities %s.  The window is a declared %s of "
            "Bell(27) and the count is a COUNT over that window, not a "
            "measure over the carrier's partitions"
            % (com(len(winlist)), len(leg1_cell_survivors), com(c_cards[1]),
               len(c_non), sorted(c_cards), com(len(winlist))),
            pick("MUT-CELL-CENSUS", c_cards[1], 0) + len(c_non) == len(corp)
            and min(c_cards) >= 1,
            "unique %d, non-unique %d, cardinalities %s, window %d"
            % (c_cards[1], len(c_non), sorted(c_cards), len(winlist)))
    SEAL.take("SEAL-CELL", R)

    R["cross_grain"] = {
        "actor_non_unique": len(a_non), "carrier_non_unique": len(c_non),
        "actor_subset_of_carrier": set(a_non) <= set(c_non),
        "sets_equal": set(a_non) == set(c_non),
        "carrier_only": len(set(c_non) - set(a_non)),
        "actor_only": len(set(a_non) - set(c_non)),
    }
    reg(len(set(c_non) - set(a_non)), len(set(a_non) - set(c_non)))
    LD.gate("G-CROSS-GRAIN-CONTAINMENT",
            "THE TWO GRAINS ARE COMPARED AS SETS OF HISTORIES, NOT AS "
            "COUNTS.  The histories at which the actor grain admits more "
            "than one factorization and the histories at which the carrier "
            "grain does are compared element by element: %d against %d, "
            "containment %s, equality %s, with %d histories non-unique at "
            "the carrier and unique at the actor grain and %d the other way "
            "round.  A count-only comparison would have missed the direction"
            % (len(a_non), len(c_non),
               R["cross_grain"]["actor_subset_of_carrier"],
               R["cross_grain"]["sets_equal"],
               R["cross_grain"]["carrier_only"],
               R["cross_grain"]["actor_only"]),
            pick("MUT-CROSS", R["cross_grain"]["actor_subset_of_carrier"],
                 False),
            "actor %d, carrier %d, subset %s, equal %s"
            % (len(a_non), len(c_non),
               R["cross_grain"]["actor_subset_of_carrier"],
               R["cross_grain"]["sets_equal"]))
    SEAL.take("SEAL-CROSS", R)

    rep_idx = {k for k, (_t, H) in enumerate(corp)
               if repeats_a_parallel_class(H)}
    cc_idx = {k for k, (_t, H) in enumerate(corp) if class_constant(H)}
    R["thesis"] = {
        "field": "THE-LAW-ADMITS-MORE-THAN-ONE-FACTORIZATION-ONLY-WHERE-THE-"
                 "HISTORY-REPEATS-A-PARALLEL-CLASS",
        "direction": "ONE-DIRECTIONAL -- a necessary condition, measured in "
                     "both directions and asserted in one",
        "histories_that_repeat_a_parallel_class": len(rep_idx),
        "histories_that_use_one_class_in_every_round": len(cc_idx),
        "actor_non_unique_inside_the_condition":
            len(set(a_non) & rep_idx),
        "actor_non_unique": len(a_non),
        "carrier_non_unique_inside_the_condition":
            len(set(c_non) & rep_idx),
        "carrier_non_unique": len(c_non),
        "necessary_at_both_grains": set(a_non) <= rep_idx
        and set(c_non) <= rep_idx,
        "sufficient": rep_idx <= set(a_non) or rep_idx <= set(c_non),
        "tight_biconditional_at_the_actor_grain": set(a_non) == cc_idx,
        "tight_biconditional_at_the_carrier_grain": set(c_non) == cc_idx,
        "class_constant_inside_the_carrier_non_unique":
            len(set(c_non) & cc_idx),
        "reading": "every history at which the criterion admits more than "
                   "one factorization repeats a parallel class, at BOTH "
                   "grains; the converse fails badly, so the condition is "
                   "necessary and far from sufficient.  The tight "
                   "biconditional is measured only at the actor grain, "
                   "against the stronger class-constant predicate",
    }
    reg(len(rep_idx), len(cc_idx), len(set(a_non) & rep_idx),
        len(set(c_non) & rep_idx), len(set(c_non) & cc_idx))
    LD.gate("G-THESIS-IS-ONE-DIRECTIONAL",
            "THE HEAD'S THESIS FIELD IS MEASURED IN BOTH DIRECTIONS AND "
            "ASSERTED IN ONE (the paper-23 iff lesson).  The condition it "
            "names -- the history repeats a parallel class -- holds at %d of "
            "the %s committed histories, and every history at which the "
            "criterion admits more than one factorization satisfies it: %d of "
            "%d at the actor grain and %d of %d at the carrier grain, 0 "
            "exceptions.  The converse is FALSE at both grains, so the field "
            "is an ONLY-WHERE and the gate refuses to let it be read as a "
            "biconditional.  The tight biconditional this corpus does carry "
            "is the stronger class-constant predicate at the actor grain "
            "alone: %d histories use one parallel class in every round and "
            "they are exactly the actor grain's non-unique ones, while %d of "
            "the carrier grain's %d are class-constant"
            % (len(rep_idx), com(len(corp)), len(set(a_non) & rep_idx),
               len(a_non), len(set(c_non) & rep_idx), len(c_non), len(cc_idx),
               len(set(c_non) & cc_idx), len(c_non)),
            pick("MUT-THESIS", R["thesis"]["necessary_at_both_grains"], False)
            and not R["thesis"]["sufficient"]
            and R["thesis"]["tight_biconditional_at_the_actor_grain"]
            and not R["thesis"]["tight_biconditional_at_the_carrier_grain"],
            "condition holds at %d, necessary %s, sufficient %s, actor "
            "biconditional %s, carrier biconditional %s"
            % (len(rep_idx), R["thesis"]["necessary_at_both_grains"],
               R["thesis"]["sufficient"],
               R["thesis"]["tight_biconditional_at_the_actor_grain"],
               R["thesis"]["tight_biconditional_at_the_carrier_grain"]))
    SEAL.take("SEAL-THESIS", R)

    leg4_evals = sum(leg_eval[g]["leg4_evaluations"] for g in leg_eval)
    leg4_fails = sum(leg_eval[g]["leg4_failures"] for g in leg_eval)
    R["coin_order"] = {
        "declared_orders": list(COIN_ORDERS),
        "leg4_evaluations_per_order": leg4_evals,
        "leg4_passes_per_order": dict(sorted(coin_rows.items())),
        "leg4_failures_per_order": leg4_fails,
        "rows_where_the_orders_disagree": coin_disagree,
        "fiber": "INERT-ON-EVERY-CENSUS-ROW" if coin_disagree == 0
                 else "LIVE",
        "denominator": "a pass count alone cannot say whether the leg ever "
                       "fired, because LEG-4 is evaluated only on the rows "
                       "the first three legs admit; the evaluation count and "
                       "the failure count are published beside it",
        "duty": "paper-20 declares the coin order a verdict-relevant fiber "
                "(#293); both members are run on every LEG-4 evaluation and "
                "both counts are published here",
    }
    reg(coin_disagree, leg4_evals, leg4_fails, *sorted(coin_rows.values()))
    LD.gate("G-BOTH-COIN-ORDERS-PUBLISHED",
            "THE COIN-ORDER DUTY IS DISCHARGED BY RUNNING BOTH, NOT BY "
            "CHOOSING ONE (#293), AND THE PASS COUNT IS PUBLISHED WITH ITS "
            "DENOMINATOR.  Every LEG-4 evaluation in both censuses is "
            "performed at %s and at %s: %s evaluations per order, of which "
            "%s pass and %d fail, and the number of rows at which the two "
            "orders disagree is %d -- on failures as on passes -- so the "
            "fiber is published rather than stamped away"
            % (COIN_ORDERS[0], COIN_ORDERS[1], com(leg4_evals),
               ", ".join("%s=%s" % (o, com(coin_rows[o]))
                         for o in COIN_ORDERS), leg4_fails, coin_disagree),
            sorted(coin_rows) == sorted(COIN_ORDERS)
            and all(v > 0 for v in coin_rows.values())
            and all(leg4_evals - leg4_fails == v for v in coin_rows.values())
            and pick("MUT-COIN", coin_disagree, 1) == coin_disagree,
            "orders %s, evaluations %d, passes %s, failures %d, "
            "disagreements %d"
            % (list(COIN_ORDERS), leg4_evals, dict(sorted(coin_rows.items())),
               leg4_fails, coin_disagree))
    SEAL.take("SEAL-COIN", R)

    say()
    say("SECTION 5.  WHICH LEG BINDS -- THE COMPLETE LATTICE ON A SUB-WINDOW")

    sub_idx = [k for k, (tag, _h) in enumerate(corp) if tag == "C1"] + a_non
    sub_idx = sorted(set(sub_idx))
    legrows, theorem_bad = [], 0
    for k in sub_idx:
        tag, H = corp[k]
        rec = record_field(H)
        n1 = n2 = n3 = n12 = n123 = 0
        for i, p in enumerate(P9):
            b1 = leg1_actor(p, BM[i])
            b2 = leg2_actor(p, H)
            b3 = leg3_actor(p, rec)
            n1 += b1
            n2 += b2
            n3 += b3
            n12 += (b1 and b2)
            n123 += (b1 and b2 and b3)
        closed = 1
        for b in signature_blocks(H):
            closed *= bell(len(b))
        if closed != n2:
            theorem_bad += 1
        legrows.append({"index": k, "corpus": tag, "leg1": n1, "leg2": n2,
                        "leg3": n3, "leg1_leg2": n12, "leg1_leg2_leg3": n123,
                        "leg2_closed_form": closed})
    prof = Counter((r["leg1"], r["leg2"], r["leg3"], r["leg1_leg2_leg3"])
                   for r in legrows)
    # WHICH LEG BINDS, BY GRAIN (K1 MAJOR-3 = K2 MAJOR-3).  The sweep above
    # separates LEG-1, LEG-2 and LEG-3 on the complete lattice; LEG-4 is a
    # predicate on the induced carrier partition and is separated here, at
    # BOTH grains, over the WHOLE corpus, by the census's own evaluations and
    # by the census re-taken with the leg deleted.  The answer is itself
    # stratified, which is this unit's own headline shape.
    grain_bind = []
    for gname, cards_with, cards_without, unique_with, unique_without in (
            ("actor", a_cards, no4_cards["actor"], a_cards[1],
             no4_cards["actor"][1]),
            ("carrier", c_cards, no4_cards["carrier"], c_cards[1],
             no4_cards["carrier"][1])):
        ev = leg_eval[gname]
        grain_bind.append({
            "grain": gname,
            "leg3_evaluations_after_leg2": ev["leg3_evaluations"],
            "leg3_failures": ev["leg3_failures"],
            "leg4_evaluations": ev["leg4_evaluations"],
            "leg4_failures": ev["leg4_failures"],
            "leg4_failures_over_distinct_histories":
                leg4_kills_distinct[gname],
            "unique_with_leg4": unique_with,
            "unique_without_leg4": unique_without,
            "cardinality_profile_with_leg4":
                {str(a): b for a, b in sorted(cards_with.items())},
            "cardinality_profile_without_leg4":
                {str(a): b for a, b in sorted(cards_without.items())},
            "leg3_binds_here": ev["leg3_failures"] > 0,
            "leg4_binds_here": ev["leg4_failures"] > 0,
            "record_dynamics_wedge": wedge_corpus[gname],
        })
    bind_by_grain = {r["grain"]: sorted(
        {"LEG-1-GEOMETRY", "LEG-2-HISTORY"}
        | ({"LEG-3-RECORD"} if r["leg3_binds_here"] else set())
        | ({"LEG-4-DYNAMICS"} if r["leg4_binds_here"] else set()))
        for r in grain_bind}
    nonbind_by_grain = {r["grain"]: sorted(
        ({"LEG-3-RECORD"} if not r["leg3_binds_here"] else set())
        | ({"LEG-4-DYNAMICS"} if not r["leg4_binds_here"] else set()))
        for r in grain_bind}
    R["leg_binding"] = {
        "sub_window": len(sub_idx), "complement": len(corp) - len(sub_idx),
        "lattice": len(P9),
        "profiles": [{"leg1": k[0], "leg2": k[1], "leg3": k[2],
                      "all_three": k[3], "histories": v}
                     for k, v in sorted(prof.items())],
        "leg2_closed_form_mismatches": theorem_bad,
        "record_non_site_constant_histories": rec_nonconstant,
        "by_grain": grain_bind,
        "binding_legs_by_grain": bind_by_grain,
        "non_binding_legs_by_grain": nonbind_by_grain,
        "binding_is_itself_stratified":
            bind_by_grain["actor"] != bind_by_grain["carrier"],
        "leg4_fineness": {
            "implemented": "the per-exponent integer tallies of the column's "
                           "entries falling into each block",
            "stated": "the block sums, summed first and compared in Z[w]",
            "relation": "the implemented predicate is STRICTLY FINER in "
                        "general, because 1 + w + w^2 = 0",
            "comparisons": fine_checked,
            "disagreements": fine_disagree},
        "binding_legs": sorted({"LEG-1-GEOMETRY"} |
                               ({"LEG-2-HISTORY"} if any(
                                   r["leg2"] < len(P9) for r in legrows)
                                else set()) |
                               ({"LEG-3-RECORD"} if any(
                                   r["leg3"] < len(P9) for r in legrows)
                                else set())),
        "non_binding_legs": sorted({"LEG-3-RECORD"} if all(
            r["leg3"] == len(P9) for r in legrows) else set()),
    }
    for r in legrows:
        reg(r["leg1"], r["leg2"], r["leg3"], r["leg1_leg2"],
            r["leg1_leg2_leg3"])
    reg(len(sub_idx), len(corp) - len(sub_idx), theorem_bad,
        fine_checked, fine_disagree)
    for p in R["leg_binding"]["profiles"]:
        reg(p["histories"])
    for r in grain_bind:
        reg(r["leg3_evaluations_after_leg2"], r["leg3_failures"],
            r["leg4_evaluations"], r["leg4_failures"],
            r["leg4_failures_over_distinct_histories"],
            r["unique_with_leg4"], r["unique_without_leg4"],
            r["record_dynamics_wedge"])
        for d in ("cardinality_profile_with_leg4",
                  "cardinality_profile_without_leg4"):
            for a, b in r[d].items():
                reg(int(a), b)
    LD.gate("G-LEG2-IS-THE-SIGNATURE-REFINEMENT-THEOREM",
            "THE HISTORY LEG HAS A CLOSED FORM AND IT IS THE NAMING GRAIN'S "
            "OWN OBJECT.  A partition passes LEG-2 exactly when it refines "
            "the participation-signature partition -- the same partition "
            "whose Young subgroup is the history's stabilizer -- so the count "
            "of LEG-2 survivors must be the product of the Bell numbers of "
            "the signature's block sizes.  Measured against the enumeration "
            "at every one of the %d histories of the sub-window: %d "
            "mismatches" % (len(sub_idx), theorem_bad),
            pick("MUT-LEG2-THEOREM", theorem_bad, 1) == 0,
            "sub-window %d, mismatches %d" % (len(sub_idx), theorem_bad))
    LD.gate("G-WHICH-LEG-BINDS",
            "THE LEGS ARE REPORTED SEPARATELY, INCLUDING THE ONE THAT DOES "
            "NOT BIND.  On the declared sub-window of %d histories (the "
            "complement is %s and is named, not hidden) the complete lattice "
            "of %s actor partitions is run leg by leg.  The record field of "
            "this corpus is site-constant at %s of %s histories -- measured, "
            "not assumed -- so LEG-3 admits the whole lattice here and the "
            "binding is done by %s.  A leg that never fails on a corpus is "
            "declared non-binding ON THAT CORPUS and is exercised on the "
            "control arm instead"
            % (len(sub_idx), com(len(corp) - len(sub_idx)), com(len(P9)),
               com(len(corp) - rec_nonconstant), com(len(corp)),
               " and ".join(R["leg_binding"]["binding_legs"])),
            len(legrows) == len(sub_idx)
            and pick("MUT-LEGBIND", rec_nonconstant, 1) == 0
            and "LEG-1-GEOMETRY" in R["leg_binding"]["binding_legs"],
            "sub-window %d, profiles %d, non-binding %s"
            % (len(sub_idx), len(prof),
               R["leg_binding"]["non_binding_legs"] or "none"))
    LD.gate("G-WHICH-LEG-BINDS-BY-GRAIN",
            "THE FOURTH LEG IS REPORTED TOO, AND THE ANSWER IS ITSELF "
            "STRATIFIED.  LEG-4 is a predicate on the induced carrier "
            "partition, so it is separated at BOTH grains over the whole "
            "corpus, twice: by counting its failures among the rows the "
            "earlier legs admit, and by re-taking each census with the leg "
            "DELETED.  At the actor grain it fails %d times in %s "
            "evaluations and the cardinality profile is unchanged when it is "
            "deleted, so the actor-grain headline is carried by geometry and "
            "history alone; at the carrier grain it fails %d times in %s "
            "evaluations -- %d of them at distinct histories -- and deleting "
            "it moves the carrier census from %s unique to %s.  The record "
            "leg fails %d times at either grain.  By this unit's own rule a "
            "leg that never fails on a corpus is declared non-binding ON "
            "THAT CORPUS, and the declaration now carries its grain: %s.  "
            "The implemented LEG-4 is strictly finer than the stated one and "
            "the two are compared on every evaluation of both censuses: %s "
            "comparisons, %d disagreements"
            % (grain_bind[0]["leg4_failures"],
               com(grain_bind[0]["leg4_evaluations"]),
               grain_bind[1]["leg4_failures"],
               com(grain_bind[1]["leg4_evaluations"]),
               grain_bind[1]["leg4_failures_over_distinct_histories"],
               com(grain_bind[1]["unique_with_leg4"]),
               com(grain_bind[1]["unique_without_leg4"]),
               grain_bind[0]["leg3_failures"],
               "; ".join("%s: %s non-binding" % (g, ", ".join(v) or "none")
                         for g, v in sorted(nonbind_by_grain.items())),
               com(fine_checked), fine_disagree),
            pick("MUT-LEG4-BY-GRAIN",
                 R["leg_binding"]["binding_is_itself_stratified"], False)
            and grain_bind[0]["unique_with_leg4"] ==
            grain_bind[0]["unique_without_leg4"]
            and grain_bind[1]["unique_with_leg4"] !=
            grain_bind[1]["unique_without_leg4"]
            and fine_disagree == 0 and fine_checked > 0
            and grain_bind[0]["leg4_evaluations"]
            + grain_bind[1]["leg4_evaluations"] == leg4_evals,
            "actor: leg4 %d of %d fail, unique %d -> %d; carrier: leg4 %d of "
            "%d fail, unique %d -> %d; fineness %d of %d disagree"
            % (grain_bind[0]["leg4_failures"],
               grain_bind[0]["leg4_evaluations"],
               grain_bind[0]["unique_without_leg4"],
               grain_bind[0]["unique_with_leg4"],
               grain_bind[1]["leg4_failures"],
               grain_bind[1]["leg4_evaluations"],
               grain_bind[1]["unique_without_leg4"],
               grain_bind[1]["unique_with_leg4"],
               fine_disagree, fine_checked))
    SEAL.take("SEAL-LEGBIND", R)

    say()
    say("SECTION 6.  MEASUREMENT TWO -- THE GROUPOID CRYSTALLIZATION")

    gsub = [k for k, (tag, _h) in enumerate(corp) if tag in ("C1", "C3")]
    arrows_rows = Counter()
    arrow_products = []
    seen_tag = set()
    for k in gsub:
        g = groupoid_arrows(corp[k][1])
        arrows_rows[(g["objects"], tuple(sorted(set(g["isotropy_orders"]))),
                     g["connected_components"])] += 1
        tag = corp[k][0]
        if tag not in seen_tag:
            seen_tag.add(tag)
            iso_prod = 1
            for o in g["isotropy_orders"]:
                iso_prod *= o
            arrow_products.append({
                "corpus": tag, "history_index": k, "events": g["objects"],
                "isotropy_orders_present": sorted(set(g["isotropy_orders"])),
                "isotropy_product": iso_prod,
                "connected_components": g["connected_components"]})
    ladder = []
    thresholds = Counter()
    atom_breaks = 0
    complete_equals_stab = 0
    complete_mismatch = 0
    free_product_bad = 0
    lad_prof = Counter()
    PERHIST = []
    REL_AGG = {}
    for k, (tag, H) in enumerate(corp):
        T = len(H)
        stab = stab_raw_actor(H)
        gc = gamma_relation_count(H, coherence_pairs(T, "R-COMPLETE", 3))
        if gc == stab:
            complete_equals_stab += 1
        else:
            complete_mismatch += 1
        g0 = gamma_window_count(H, 0)
        g1 = gamma_window_count(H, 1)
        g2 = gamma_window_count(H, 2)
        g3 = gamma_window_count(H, 3)
        gr = gamma_relation_count(H, coherence_pairs(T, "R-ROUND", 3))
        if g0 != len(local_syms(H[0])) ** T:
            free_product_bad += 1
        if stab == 1 and g1 > 1:
            atom_breaks += 1
        w = collapse_threshold(H, gc, {0: g0, 1: g1, 2: g2, 3: g3})
        PERHIST.append({"stab": stab, "g1": g1, "gc": gc, "w": w})
        for rn, rv in zip(COHERENCE_ROWS, (g0, g1, g2, g3, gr, gc)):
            REL_AGG.setdefault((tag, rn), []).append(rv)
        thresholds[(tag, T, w)] += 1
        lad_prof[(tag, T, g0, g1, g2, g3, gr, gc, stab)] += 1
    ladder = [{"corpus": k[0], "events": k[1], "R-EMPTY": k[2],
               "R-ADJACENT": k[3], "R-WINDOW-2": k[4], "R-WINDOW-3": k[5],
               "R-ROUND": k[6], "R-COMPLETE": k[7], "global_stabilizer": k[8],
               "histories": v} for k, v in sorted(lad_prof.items())]
    by_rel = [{"corpus": k[0], "relation": k[1],
               "distinct_values": len(set(REL_AGG[k])),
               "minimum": min(REL_AGG[k]), "maximum": max(REL_AGG[k]),
               "histories": len(REL_AGG[k])}
              for k in sorted(REL_AGG)]
    tab_max = max(int(r.rsplit("-", 1)[1]) for r in COHERENCE_ROWS
                  if r.startswith("R-WINDOW"))
    above_tab = sum(v for k, v in thresholds.items() if k[2] > tab_max)
    above_tab_c1c2 = sum(v for k, v in thresholds.items()
                         if k[2] > tab_max and k[0] in ("C1", "C2"))
    R["groupoid"] = {
        "by_relation": by_rel,
        "arrow_profiles": [{"objects": k[0], "isotropy_orders": list(k[1]),
                            "connected_components": k[2], "histories": v}
                           for k, v in sorted(arrows_rows.items())],
        "arrow_sub_window": len(gsub),
        "arrow_sub_window_complement": len(corp) - len(gsub),
        "arrow_isotropy_products": arrow_products,
        "two_objects": "the LADDER's local identifications are the FULL "
                       "symmetric group of each event's footprint -- which "
                       "is why the empty relation returns 6^T exactly -- "
                       "while the ARROW groupoid's arrows preserve the "
                       "events' internal declared cell directions.  The "
                       "arrow groupoid is measured separately and no ladder "
                       "row counts it",
        "coherence_rows": list(COHERENCE_ROWS),
        "ladder": ladder,
        "empty_relation_is_the_free_product": free_product_bad == 0,
        "free_product_mismatches": free_product_bad,
        "complete_equals_the_global_stabilizer": complete_equals_stab,
        "complete_mismatches": complete_mismatch,
        "complete_relation_identity": "a family coherent on every pair "
                                      "determines one map on the actors "
                                      "restricting to a permutation of every "
                                      "event, and conversely; the equality "
                                      "is a THEOREM of the construction and "
                                      "the two-route agreement is a code "
                                      "check, not a corpus measurement",
        "tabulated_ladder_top": tab_max,
        "histories_whose_threshold_exceeds_the_tabulated_ladder": above_tab,
        "of_those_in_C1_and_C2": above_tab_c1c2,
        "histories": len(corp),
        "collapse_thresholds": {"%s-T%d-w%s" % k: v
                                for k, v in sorted(thresholds.items())},
        "threshold_values": sorted({k[2] for k in thresholds}),
    }
    reg(tab_max, above_tab, above_tab_c1c2, len(corp) - len(gsub))
    for row in arrow_products:
        reg(row["events"], row["isotropy_product"],
            row["connected_components"], *row["isotropy_orders_present"])
    for row in ladder:
        for kk in ("R-EMPTY", "R-ADJACENT", "R-WINDOW-2", "R-WINDOW-3",
                   "R-ROUND", "R-COMPLETE", "global_stabilizer", "histories",
                   "events"):
            reg(row[kk])
    for row in by_rel:
        reg(row["distinct_values"], row["minimum"], row["maximum"],
            row["histories"])
    for v in thresholds.values():
        reg(v)
    reg(complete_equals_stab, complete_mismatch, len(gsub),
        *sorted({k[2] for k in thresholds}))
    for row in R["groupoid"]["arrow_profiles"]:
        reg(row["objects"], row["connected_components"], row["histories"],
            *row["isotropy_orders"])
    LD.gate("G-GROUPOID-LADDER-PER-HISTORY",
            "THE COHERENCE LADDER IS RUN AT EVERY HISTORY, AND THE COMPLETE "
            "RELATION IS MEASURED AGAINST THE GLOBAL GROUP RATHER THAN "
            "ASSUMED EQUAL TO IT.  At each of the %s histories the number of "
            "coherent families is counted exactly at %d declared coherence "
            "relations by two disjoint routes -- a dynamic programme for the "
            "sliding windows and a backtracking enumeration for the "
            "round-local and complete relations.  The complete relation "
            "returns the global stabilizer's order at %s of %s histories, "
            "with %d mismatches: gluing pairwise-coherent local "
            "identifications recovers a global relabelling, and the corpus "
            "says so history by history"
            % (com(len(corp)), len(COHERENCE_ROWS), com(complete_equals_stab),
               com(len(corp)), complete_mismatch),
            pick("MUT-GAMMA-COMPLETE", complete_mismatch, 1) == 0
            and complete_equals_stab == len(corp),
            "histories %d, complete==stab %d, mismatches %d, thresholds %s"
            % (len(corp), complete_equals_stab, complete_mismatch,
               sorted({k[2] for k in thresholds})))
    LD.gate("G-THE-LADDER-AND-THE-ARROW-GROUPOID-ARE-TWO-OBJECTS",
            "TWO OBJECTS, KEPT APART AND BOTH MEASURED (K1 MAJOR-2 = K2 "
            "MAJOR-1).  The coherence ladder's local identifications are the "
            "FULL symmetric group of each event's three-actor footprint, with "
            "no structure condition -- which is the groupoid-grain relaxation "
            "of the global test, itself a quantifier over all of S9, and is "
            "why the empty relation returns 6^T exactly: checked at every one "
            "of the %s histories, %d mismatches.  The ARROW groupoid, whose "
            "arrows preserve the events' internal declared cells with their "
            "directions, is a DIFFERENT object measured on the declared "
            "sub-window of %d histories: its isotropy orders are %s and its "
            "free product at the sampled histories is %s, not the ladder's "
            "count.  No ladder row counts arrows, and substituting them would "
            "not return the global stabilizer at the complete relation"
            % (com(len(corp)), free_product_bad, len(gsub),
               ", ".join(str(o) for o in sorted(
                   {o for r in R["groupoid"]["arrow_profiles"]
                    for o in r["isotropy_orders"]})),
               ", ".join(com(r["isotropy_product"]) for r in arrow_products)),
            pick("MUT-FREE-PRODUCT", free_product_bad, 1) == 0
            and len(arrow_products) > 1
            and all(r["isotropy_product"] < min(
                row["R-EMPTY"] for row in ladder
                if row["corpus"] == r["corpus"])
                for r in arrow_products),
            "free-product mismatches %d, arrow sub-window %d, arrow products "
            "%s against ladder R-EMPTY %s"
            % (free_product_bad, len(gsub),
               [r["isotropy_product"] for r in arrow_products],
               [min(row["R-EMPTY"] for row in ladder
                    if row["corpus"] == r["corpus"])
                for r in arrow_products]))
    SEAL.take("SEAL-GROUPOID", R)

    atom_word = atom_law(atom_breaks, complete_mismatch == 0)
    set_nontrivial = {k for k, r in enumerate(PERHIST) if r["stab"] > 1}
    set_nobreak = {k for k, r in enumerate(PERHIST)
                   if not (r["stab"] == 1 and r["g1"] > 1)}
    three_agree = (set(a_non) == set_nontrivial == set_nobreak)
    R["atom"] = {
        "histories_with_a_trivial_global_stabilizer":
            sum(1 for r in PERHIST if r["stab"] == 1),
        "of_those_carrying_a_nontrivial_adjacent_coherent_family":
            atom_breaks,
        "atom_word": atom_word,
        "three_predicates_one_split": {
            "actor_grain_non_unique": len(a_non),
            "nontrivial_global_stabilizer": len(set_nontrivial),
            "no_atom_break": len(set_nobreak),
            "sets_coincide_element_by_element": three_agree,
            "reading": "at every history the global stabilizer is trivial "
                       "exactly when the actor-grain factorization is unique "
                       "and exactly when the atom breaks -- three predicates, "
                       "one split of the corpus, verified element by element, "
                       "so at the actor grain this unit's answer is "
                       "extensionally the naming census's"},
        "reading": "group-level triviality does not imply groupoid-level "
                   "rigidity at this arena: the histories that force the "
                   "labelling globally do not force it when the "
                   "identification is required to cohere only between "
                   "neighbouring events",
    }
    reg(atom_breaks, R["atom"]["histories_with_a_trivial_global_stabilizer"])
    LD.gate("G-ATOM-THEOREM-AT-THE-GROUPOID-GRAIN",
            "THE ATOM THEOREM IS PUT AT RISK AND THE OUTCOME IS DERIVED.  Of "
            "the %s histories whose global stabilizer is trivial, %s carry a "
            "coherent family other than the identity at the adjacent-overlap "
            "relation; the word this unit emits, %s, is computed from that "
            "count and from whether the complete relation still returns the "
            "group, and BOTH outcome words are reachable from the same "
            "enumeration -- a corpus in which no history broke would return "
            "the other one"
            % (com(R["atom"]["histories_with_a_trivial_global_stabilizer"]),
               com(atom_breaks), atom_word),
            atom_word in ("FAC-ATOM-BREAKS-AT-THE-GROUPOID-GRAIN",
                          "FAC-ATOM-HOLDS-AT-THE-GROUPOID-GRAIN")
            and atom_law(0, True) != atom_law(1, True)
            and pick("MUT-ATOM", atom_word, "FAC-ATOM-FORGED") ==
            atom_law(atom_breaks, complete_mismatch == 0)
            and pick("MUT-THREE-PREDICATES", three_agree, False),
            "trivial-stabilizer histories %d, breaks %d, word %s, three "
            "predicates coincide %s"
            % (R["atom"]["histories_with_a_trivial_global_stabilizer"],
               atom_breaks, atom_word, three_agree))
    SEAL.take("SEAL-ATOM", R)

    say()
    say("SECTION 7.  MEASUREMENT THREE -- THE GRAIN TRIANGLE")

    tri_prof = Counter()
    tri_sub = [k for k, (tag, _h) in enumerate(corp) if tag in ("C1", "C3")]
    brute_checked, brute_bad = 0, 0
    for k in tri_sub:
        tag, H = corp[k]
        raw9 = PERHIST[k]["stab"]
        raw27 = stab_raw_cell(H)
        rsite, rcell = stab_realizable(H, autos)
        tri_prof[(tag, raw9, raw27, rsite, rcell)] += 1
    for k in tri_sub[:24]:
        H = corp[k][1]
        brute_checked += 1
        if stab_raw_actor_bruteforce(H) != PERHIST[k]["stab"]:
            brute_bad += 1
    tri_rows = [{"corpus": k[0], "TEST-RAW-at-ACTOR-S9": k[1],
                 "TEST-RAW-at-CARRIER-S27": k[2],
                 "TEST-REALIZABLE-at-SITE": k[3],
                 "TEST-REALIZABLE-at-CARRIER": k[4], "histories": v}
                for k, v in sorted(tri_prof.items())]
    agree_actor = sum(v for k, v in tri_prof.items() if k[1] == k[3])
    agree_cell = sum(v for k, v in tri_prof.items() if k[2] == k[4])
    R["grain_triangle"] = {
        "sub_window": len(tri_sub), "complement": len(corp) - len(tri_sub),
        "grains": list(GRAIN_ROWS), "tests": list(TEST_ROWS),
        "rows": tri_rows,
        "arena_group_order": len(autos),
        "raw_and_realizable_agree_at_the_actor_grain": agree_actor,
        "raw_and_realizable_agree_at_the_carrier_grain": agree_cell,
        "brute_force_checked": brute_checked,
        "brute_force_mismatches": brute_bad,
        "the_extreme_row_is_the_whole_symmetric_group":
            max(k[2] for k in tri_prof) == math.factorial(DIM),
        "cells_factorial": math.factorial(DIM),
        "max_raw_carrier_stabilizer": max(k[2] for k in tri_prof),
        "min_raw_carrier_stabilizer": min(k[2] for k in tri_prof),
        "carrier_stabilizer_is_nontrivial_at": sum(
            v for k, v in tri_prof.items() if k[2] > 1),
    }
    for row in tri_rows:
        for kk in ("TEST-RAW-at-ACTOR-S9", "TEST-RAW-at-CARRIER-S27",
                   "TEST-REALIZABLE-at-SITE", "TEST-REALIZABLE-at-CARRIER",
                   "histories"):
            reg(row[kk])
    reg(len(tri_sub), len(corp) - len(tri_sub), agree_actor, agree_cell,
        brute_checked, brute_bad, math.factorial(DIM),
        R["grain_triangle"]["max_raw_carrier_stabilizer"],
        R["grain_triangle"]["min_raw_carrier_stabilizer"],
        R["grain_triangle"]["carrier_stabilizer_is_nontrivial_at"])
    LD.gate("G-GRAIN-TRIANGLE-BOTH-TESTS",
            "BOTH DECLARED TESTS RUN AT ALL THREE GRAINS (the AID "
            "test-declaration duty).  TEST-RAW takes the stabilizer inside "
            "the grain's full symmetric group; TEST-REALIZABLE intersects it "
            "with the order-%d group the arena itself realizes.  On the "
            "declared sub-window of %d histories (complement %s, named) the "
            "carrier's raw stabilizer is nontrivial at %d of %d rows and "
            "ranges up to %s, while the two tests agree at the actor grain "
            "at %d rows and at the carrier grain at %d.  The top of that "
            "range is the FULL symmetric group on the cells -- the extreme "
            "row's raw carrier stabilizer is exactly 27 factorial, so at that "
            "one history the raw carrier test is vacuous.  The raw route is "
            "checked against an explicit filtration of the symmetric group "
            "at %d histories, %d mismatches"
            % (len(autos), len(tri_sub), com(len(corp) - len(tri_sub)),
               R["grain_triangle"]["carrier_stabilizer_is_nontrivial_at"],
               len(tri_sub), com(R["grain_triangle"]
                                 ["max_raw_carrier_stabilizer"]),
               agree_actor, agree_cell, brute_checked, brute_bad),
            pick("MUT-TRIANGLE", brute_bad, 1) == 0
            and len(tri_rows) > 1
            and sum(v for k, v in tri_prof.items()) == len(tri_sub)
            and agree_actor != agree_cell
            and R["grain_triangle"]
            ["the_extreme_row_is_the_whole_symmetric_group"],
            "rows %d, brute-checked %d, mismatches %d, raw-vs-realizable "
            "agreement actor %d of %d carrier %d of %d"
            % (len(tri_rows), brute_checked, brute_bad, agree_actor,
               len(tri_sub), agree_cell, len(tri_sub)))
    SEAL.take("SEAL-TRIANGLE", R)

    say()
    say("SECTION 8.  MEASUREMENT FOUR -- THE PERSISTENCE PRESUPPOSITION")

    wstar = sorted({k[2] for k in thresholds})
    R["persistence"] = {
        "presupposition": "a global relabelling is definable only on a "
                          "persistent actor set; the coherence relation of "
                          "the groupoid grain is exactly how much of that "
                          "persistence a census assumes, and it is a "
                          "declaration",
        "coherence_is_a_declared_coordinate": True,
        "identity_forced_at_the_complete_relation":
            sum(1 for r in PERHIST if r["stab"] == 1),
        "identity_forced_at_the_adjacent_relation":
            sum(1 for r in PERHIST if r["g1"] == 1),
        "collapse_threshold_values": wstar,
        "collapse_threshold_distribution":
            {"%s-T%d-w%s" % k: v for k, v in sorted(thresholds.items())},
        "reading": "crystallized identity does not transport below the "
                   "measured coherence depth: at every history of this "
                   "corpus the groupoid count meets the group's only once "
                   "the identification is required to cohere across at "
                   "least that many events",
    }
    reg(*wstar)
    LD.gate("G-PERSISTENCE-PRESUPPOSITION",
            "THE PRESUPPOSITION IS STATED AS A MEASUREMENT, NOT AS A "
            "READING.  The global grain quantifies over one permutation of "
            "a persistent actor set; the groupoid grain replaces it with a "
            "family and a declared coherence relation.  Identity is forced "
            "at the complete relation at %s histories and at the adjacent "
            "relation at %s, and the coherence depth at which the two meet "
            "is %s -- derived per history by searching upward, never capped"
            % (com(R["persistence"]["identity_forced_at_the_complete_relation"]),
               com(R["persistence"]["identity_forced_at_the_adjacent_relation"]),
               ", ".join(str(w) for w in wstar)),
            pick("MUT-PERSIST", len(wstar), 0) > 0 and all(
                w is not None for w in wstar)
            and R["persistence"]["identity_forced_at_the_adjacent_relation"]
            < R["persistence"]["identity_forced_at_the_complete_relation"],
            "forced at complete %d, at adjacent %d, thresholds %s"
            % (R["persistence"]["identity_forced_at_the_complete_relation"],
               R["persistence"]["identity_forced_at_the_adjacent_relation"],
               wstar))
    SEAL.take("SEAL-PERSIST", R)

    rung = {}
    for tag in ("C1", "C2", "C3"):
        idx = [k for k, (t, _h) in enumerate(corp) if t == tag]
        rnd = len(corp[idx[0]][1]) // 3
        rung["R%d-%s" % (rnd, tag)] = {
            "rounds": rnd, "histories": len(idx),
            "unique_at_the_actor_grain": sum(1 for k in idx if k not in
                                             set(a_non)),
            "unique_at_the_actor_grain_at_the_pairwise_image":
                sum(1 for k in idx if k not in set(pw_non)),
            "unique_at_the_carrier_grain": sum(1 for k in idx if k not in
                                               set(c_non)),
            "atom_breaks": sum(1 for k in idx
                               if PERHIST[k]["stab"] == 1
                               and PERHIST[k]["g1"] > 1),
            "collapse_thresholds": sorted({k[2] for k in thresholds
                                           if k[0] == tag}),
        }
    holds = all(v["atom_breaks"] == v["unique_at_the_actor_grain"]
                for v in rung.values())
    # IS THE R = 6 RUNG INDEPENDENT?  (K2 MAJOR-6, AID's adopted disclosure.)
    # C2 is the set of ORDERED PAIRS of C1 histories.  A concatenation's
    # participation signature refines both parts', so its LEG-2 survivors are
    # the intersection of the parts' and its stabilizer is the intersection of
    # the parts' stabilizers.  Measured at the parts: if every C1 history
    # already admits exactly one LEG-2 survivor among the geometry survivors
    # and has a trivial stabilizer, then every C2 history does too, BEFORE any
    # census runs.  What R = 6 measures independently is the adjacent-relation
    # family count and the collapse threshold.
    c1_idx = [k for k, (t, _h) in enumerate(corp) if t == "C1"]
    c1_leg2_one = sum(1 for k in c1_idx
                      if sum(1 for i in leg1_actor_set
                             if leg2_actor(P9[i], corp[k][1])) == 1)
    c1_stab_one = sum(1 for k in c1_idx if PERHIST[k]["stab"] == 1)
    r6_forced = (c1_leg2_one == len(c1_idx) and c1_stab_one == len(c1_idx))
    R["transport"] = {
        "ladder_rows": {k: rung[k] for k in sorted(rung)},
        "atom_break_transports_across_every_rung": holds,
        "R6_is_forced_by_R3": {
            "C1_histories": len(c1_idx),
            "C1_histories_with_exactly_one_leg2_survivor": c1_leg2_one,
            "C1_histories_with_a_trivial_stabilizer": c1_stab_one,
            "forced": r6_forced,
            "independent_at_R6": ["the adjacent-relation family count",
                                  "the collapse threshold"],
            "statement": "C2 is the set of ordered pairs of C1 histories; a "
                         "concatenation's history-leg survivors are the "
                         "intersection of its parts' and its stabilizer is "
                         "the intersection of its parts' stabilizers, so "
                         "uniqueness and trivial stabilizer at all of C2 "
                         "FOLLOW from the C1 row by theorem and are checked "
                         "here rather than discovered"},
        "scope": "the R-ladder rows this corpus carries are R = 3, R = 4 and "
                 "R = 6; PER-L closed the L-ladder transport by theorem and "
                 "PER-R places its own successor at R = 8, so nothing here "
                 "is claimed beyond the rungs measured",
    }
    reg(c1_leg2_one, c1_stab_one)
    for v in rung.values():
        reg(v["rounds"], v["histories"], v["unique_at_the_actor_grain"],
            v["unique_at_the_actor_grain_at_the_pairwise_image"],
            v["unique_at_the_carrier_grain"], v["atom_breaks"],
            *v["collapse_thresholds"])
    LD.gate("G-TRANSPORT-ALONG-THE-R-LADDER",
            "THE MEASUREMENT IS REPORTED AT EVERY RUNG THE CORPUS CARRIES.  "
            "The three rungs are %s; at each one the admissible cardinality, "
            "the atom outcome and the collapse threshold are taken from that "
            "rung's OWN histories rather than from the corpus aggregate, and "
            "the break-at-the-adjacent-relation result is checked to "
            "coincide with the actor grain's uniqueness rung by rung: %s.  "
            "The R = 6 rung is stamped THEOREM-FORCED: its histories are the "
            "ordered pairs of the R = 3 rung's, and all %d of those already "
            "carry exactly one history-leg survivor and a trivial "
            "stabilizer, so uniqueness and triviality at R = 6 are checked "
            "and not discovered; the adjacent-relation count and the collapse "
            "threshold are what that rung measures independently"
            % (", ".join(sorted(rung)), holds, len(c1_idx)),
            pick("MUT-TRANSPORT", holds, False) and len(rung) == 3
            and pick("MUT-R6-FORCED", r6_forced, False),
            "rungs %s, transports %s, R6 forced by R3 %s (C1 leg2-one %d of "
            "%d, stab-one %d of %d)"
            % (sorted(rung), holds, r6_forced, c1_leg2_one, len(c1_idx),
               c1_stab_one, len(c1_idx)))
    SEAL.take("SEAL-TRANSPORT", R)

    say()
    say("SECTION 9.  THE CONTROL ARM -- EVERY OUTCOME WORD, EMITTED")

    ctrl_rows = []
    a_set, c_set = set(a_non), set(c_non)
    for nm, idx in (("CTRL-C1-THE-STRICT-TRIPLES",
                     [k for k, (t, _h) in enumerate(corp) if t == "C1"]),
                    ("CTRL-THE-NON-UNIQUE-HISTORIES", sorted(a_set)),
                    ("CTRL-C3-THE-DRIVEN-WINDOW",
                     [k for k, (t, _h) in enumerate(corp) if t == "C3"]),
                    ("CTRL-THE-WHOLE-CORPUS", list(range(len(corp))))):
        an = [k for k in idx if k in a_set]
        cn = [k for k in idx if k in c_set]
        w = head_law(len(idx), an, cn)
        ctrl_rows.append({"arena": nm, "histories": len(idx),
                          "actor_non_unique": len(an),
                          "carrier_non_unique": len(cn), "head_word": w})
        reg(len(idx), len(an), len(cn))

    syn = {}
    rowline = tuple(sorted(CLASSES["ROW"][0]))
    syn["X1-ONE-DIVISION-EVENT"] = (frozenset(rowline),)
    syn["X2-ONE-FULL-ROW-ROUND"] = tuple(frozenset(g)
                                         for g in CLASSES["ROW"])
    mult = []
    for j, g in enumerate(CLASSES["ROW"]):
        for _ in range(1 + 3 * j):
            mult.append(frozenset(g))
    syn["X3-ROW-MULTIPLICITIES-CONGRUENT-MOD-THREE"] = tuple(mult)
    chain = []
    ordr = list(SITES)
    chain.append(frozenset((ordr[0], ordr[1], ordr[2])))
    chain.append(frozenset((ordr[0], ordr[1], ordr[3])))
    for j in range(3, len(ordr) - 1):
        chain.append(frozenset((ordr[0], ordr[j], ordr[j + 1])))
    syn["X4-THE-OVERLAPPING-CHAIN"] = tuple(chain)
    syn["X5-A-ROW-ROUND-THEN-A-COLUMN-ROUND"] = tuple(
        [frozenset(g) for g in CLASSES["ROW"]]
        + [frozenset(g) for g in CLASSES["COL"]])

    syn_rows = []
    wedge_fires = 0
    for nm in sorted(syn):
        H = syn[nm]
        rec = record_field(H)
        rows = {tuple(rec[SITE_INDEX[x] * 3 + i] for i in range(3))
                for x in SITES}
        n3 = sum(1 for i, p in enumerate(P9) if leg3_actor(p, rec))
        wedge = 0
        for i in leg1_actor_set:
            p = P9[i]
            cp = induced_cell_partition(p)
            if (not leg3_actor(p, rec)) and leg4_cell(cp, rec, "G.D") \
                    and leg4_cell(cp, rec, "D.G"):
                wedge += 1
        wedge_fires += wedge
        stab = stab_raw_actor(H)
        g1 = gamma_window_count(H, 1)
        word = atom_law(1 if (stab == 1 and g1 > 1) else 0, True)
        # IS THIS ROW'S HOLDS DECISIVE?  (K1 MINOR-5.)  The atom question is
        # whether a TRIVIAL-STABILIZER history stays rigid at a weaker
        # coherence.  At a history whose global stabilizer is already
        # nontrivial the question is not posed, and HOLDS is returned for want
        # of a candidate rather than because rigidity was found.
        syn_rows.append({"arena": nm, "events": len(H),
                         "distinct_record_rows": len(rows),
                         "leg3_passers_of_the_lattice": n3,
                         "record_binds": n3 < len(P9),
                         "record_dynamics_wedge": wedge,
                         "global_stabilizer": stab,
                         "adjacent_coherent_families": g1,
                         "atom_word": word,
                         "atom_row_is": (
                             "VACUOUS-STABILIZER-NONTRIVIAL" if stab != 1
                             else "DECISIVE")})
        reg(len(H), len(rows), n3, wedge, stab, g1)

    alt_links = {"L1-ONE-DIRECTION": (I7_LINKS[0],),
                 "L2-TWO-DIRECTIONS": I7_LINKS[:2],
                 "L4-EVERY-DIRECTION": I7_LINKS + (CLASS_DIR["ANT"],)}
    alt_rows = []
    for nm in sorted(alt_links):
        n = sum(1 for i, p in enumerate(P9)
                if leg1_actor(p, BM[i], alt_links[nm]))
        alt_rows.append({"arena": nm, "declared_links": len(alt_links[nm]),
                         "leg1_survivors": n})
        reg(n, len(alt_links[nm]))

    # ARENA-REACHED AND LAW-EVALUATED ARE DIFFERENT THINGS (K3 m7, K2 MINOR-3).
    # Four of the pin's families are returned by the head law or the atom law
    # ON A DECLARED ARENA.  The fifth -- the blocked family -- is reached only
    # by evaluating the atom law at a state the ladder gate excludes at every
    # history of this corpus, which is what an instrument-fault word is for,
    # and it is reported as law-evaluated rather than arena-reached.
    arena_words = sorted({r["head_word"] for r in ctrl_rows}
                         | {r["atom_word"] for r in syn_rows})
    law_words = sorted({atom_law(0, True), atom_law(1, True),
                        atom_law(1, False)} - set(arena_words))
    words = sorted(set(arena_words) | set(law_words))
    fams = set(R["pre_registered_outcomes"]["families"])
    unreachable = sorted(f for f in fams
                         if not any(w.startswith(f) for w in words))
    no_arena = sorted(f for f in fams
                      if not any(w.startswith(f) for w in arena_words))
    R["controls"] = {
        "declared_sub_arenas": ctrl_rows,
        "synthetic_histories": syn_rows,
        "alternative_link_sets": alt_rows,
        "words_emitted_by_a_declared_arena": arena_words,
        "words_reached_only_by_evaluating_the_law": law_words,
        "words_emitted": words,
        "pre_registered_families": sorted(fams),
        "families_no_declared_arena_reached": no_arena,
        "families_unreached_by_arena_or_law": unreachable,
        "record_dynamics_wedge_on_the_committed_corpus": wedge_corpus,
        "record_dynamics_wedge_on_the_control": wedge_fires,
        "note": "every row above is a genuine evaluation of the SAME "
                "criterion and the SAME head law on a declared datum; no "
                "control row is typed and none is forged",
    }
    reg(wedge_fires, len(words), len(fams), len(arena_words), len(no_arena),
        wedge_corpus["actor"], wedge_corpus["carrier"])
    LD.gate("G-EVERY-OUTCOME-WORD-EMITTABLE",
            "EVERY PRE-REGISTERED OUTCOME WORD IS SHOWN EMITTABLE, AND THE "
            "TWO WAYS OF REACHING ONE ARE KEPT APART (#299).  The head law "
            "returns %s on the strict triples, %s on the non-unique histories "
            "and %s on the whole corpus; the atom law returns both of its "
            "substantive words on declared synthetic histories -- the "
            "overlapping chain forces the identification at the adjacent "
            "relation and the corpus does not.  So %d of the pin's %d "
            "families are reached BY A DECLARED ARENA, and the remaining "
            "one -- %s -- is reached only by EVALUATING the law at a state "
            "the ladder gate excludes at every history of this corpus, which "
            "is what an instrument-fault word is for.  Families reached by "
            "neither route: %s"
            % (ctrl_rows[0]["head_word"], ctrl_rows[1]["head_word"],
               ctrl_rows[3]["head_word"], len(fams) - len(no_arena),
               len(fams), ", ".join(law_words) or "none",
               unreachable or "none"),
            pick("MUT-CONTROLS", len(unreachable), 1) == 0
            and len({r["head_word"] for r in ctrl_rows}) >= 3
            and len({r["atom_word"] for r in syn_rows}) >= 2
            and len(no_arena) == len(law_words)
            and all(any(w.startswith(f) for w in law_words)
                    for f in no_arena),
            "arena words %s, law-only words %s, families no arena reached %s, "
            "unreached %s"
            % (arena_words, law_words, no_arena or "none",
               unreachable or "none"))
    LD.gate("G-THE-RECORD-LEG-IS-EXERCISED-SOMEWHERE",
            "A LEG THAT NEVER FAILS ON THE CORPUS IS EXERCISED ON THE "
            "CONTROL, AND THE WEDGE IS MEASURED AT BOTH GRAINS RATHER THAN "
            "TYPED.  LEG-3 admits the whole lattice at every committed "
            "history because this corpus's record field is site-constant "
            "there; on the declared synthetic histories it binds at %d of %d "
            "arenas.  The record-versus-dynamics wedge -- partitions the "
            "coin cannot tell apart because it reads the record only modulo "
            "three, while the record itself differs -- is COMPUTED on the "
            "committed corpus at both grains in the census's own loop: %d "
            "times at the actor grain and %d times at the carrier grain, "
            "where every one of them sits on a row the history leg has "
            "already removed; and it fires %d times on the control.  The leg "
            "is therefore non-binding HERE, not vacuous"
            % (sum(1 for r in syn_rows if r["record_binds"]), len(syn_rows),
               wedge_corpus["actor"], wedge_corpus["carrier"], wedge_fires),
            pick("MUT-WEDGE", wedge_fires, 0) > 0
            and any(r["record_binds"] for r in syn_rows)
            and wedge_corpus["actor"] == 0,
            "arenas where LEG-3 binds %d of %d, wedge fires %d on the "
            "control, %d at the actor grain and %d at the carrier grain on "
            "the corpus"
            % (sum(1 for r in syn_rows if r["record_binds"]), len(syn_rows),
               wedge_fires, wedge_corpus["actor"], wedge_corpus["carrier"]))
    SEAL.take("SEAL-CONTROLS", R)

    # THE WINDOWS, WITH THEIR MEASURED BOUNDS.  The declarations themselves
    # are frozen in this file's own source above; the SIZES are this run's
    # measurements and are published here, where every one of them exists.
    # No window's size is a placeholder (K3 m6).
    win_size = {"W-CORPUS-C1-C2-C3": len(corp),
                "W-ACTOR-LATTICE-COMPLETE": len(P9),
                "W-CELL-INDUCED-PLUS-STRATA": len(winlist),
                "W-COHERENCE-LADDER": len(COHERENCE_ROWS),
                "W-FULL-LATTICE-PER-LEG": len(sub_idx),
                "W-STABILIZER-AND-ARROW-SUB-WINDOW": len(gsub),
                "W-CONTROL-ARENAS": len(ctrl_rows) + len(syn_rows)
                + len(alt_rows)}
    win_compl = {"W-FULL-LATTICE-PER-LEG": len(corp) - len(sub_idx),
                 "W-STABILIZER-AND-ARROW-SUB-WINDOW": len(corp) - len(gsub)}
    wins = []
    for (nm, why) in WINDOW_DECL:
        size = win_size[nm]
        univ = {"W-ACTOR-LATTICE-COMPLETE": bell(NACT),
                "W-CELL-INDUCED-PLUS-STRATA": bell(DIM),
                "W-CORPUS-C1-C2-C3": len(corp),
                "W-FULL-LATTICE-PER-LEG": len(corp),
                "W-STABILIZER-AND-ARROW-SUB-WINDOW": len(corp)}.get(nm)
        wins.append({"window": nm, "members": size,
                     "ambient_universe": univ,
                     "complement_in_the_corpus": win_compl.get(nm),
                     "complete_in_its_universe": univ is not None
                     and size == univ, "declaration": why})
    R["windows"] = wins
    for w in wins:
        reg(w["members"])
        if w["complement_in_the_corpus"] is not None:
            reg(w["complement_in_the_corpus"])
    LD.gate("G-WINDOWS-DECLARED-WITH-THEIR-BOUNDS",
            "EVERY WINDOW IS NAMED IN-STRING WITH ITS BOUND, AND NO BOUND IS "
            "A PLACEHOLDER.  %d windows are declared in this file's frozen "
            "source and each publishes the size this run measured: the actor "
            "lattice is COMPLETE at %s of Bell(9) = %s, and the carrier "
            "window is a declared %s of Bell(27) = %s, which is the whole "
            "reason it is a window at all.  The three sub-windows of the "
            "corpus publish their complements: the per-leg sweep runs on %d "
            "histories with %s named as its complement, and the stabilizer "
            "and arrow measurements run on %d with %s -- all of C2 -- named "
            "as theirs.  No census below is truncated silently: the coherence "
            "ladder searches upward until it meets the complete relation"
            % (len(wins), com(len(P9)), com(bell(NACT)), com(len(winlist)),
               com(bell(DIM)), len(sub_idx), com(len(corp) - len(sub_idx)),
               len(gsub), com(len(corp) - len(gsub))),
            all(w["declaration"] for w in wins)
            and all(w["members"] > 0 for w in wins)
            and pick("MUT-WINDOW", len(P9), 0) == bell(NACT)
            and len(winlist) < bell(DIM)
            and len(wins) == len(WINDOW_DECL),
            "windows %d, sizes %s, actor lattice %d of %d, carrier window "
            "%d of %d"
            % (len(wins), [w["members"] for w in wins], len(P9), bell(NACT),
               len(winlist), bell(DIM)))
    SEAL.take("SEAL-WINDOWS", R)

    say()
    say("SECTION 10.  MEASURE RELATIVITY, CLASS BINDING AND THE HEAD")

    WC, WA, WK, WS = ("W-CORPUS-C1-C2-C3", "W-ACTOR-LATTICE-COMPLETE",
                      "W-CELL-INDUCED-PLUS-STRATA",
                      "W-STABILIZER-AND-ARROW-SUB-WINDOW")
    r4 = rung["R4-C3"]
    ratios = [
        ("actor-grain histories with a unique factorization, at the "
         "directionwise image", a_cards[1], len(corp), WC, WC),
        ("actor-grain histories with a unique factorization, at the "
         "pairwise image", pw_cards[1], len(corp), WC, WC),
        ("carrier-grain histories with a unique factorization",
         c_cards[1], len(corp), WC, WC),
        ("actor partitions surviving the geometry leg",
         len(leg1_actor_set), len(P9), WA, WA),
        ("carrier-window partitions surviving the geometry leg",
         len(leg1_cell_survivors), len(winlist), WK, WK),
        ("carrier-window members against the carrier's whole lattice",
         len(winlist), bell(DIM), WK, WK),
        ("histories whose global stabilizer is trivial and whose adjacent "
         "groupoid is not", atom_breaks, len(corp), WC, WC),
        ("rows of the stabilizer sub-window where the raw and realizable "
         "tests agree at the actor grain", agree_actor, len(tri_sub), WS, WS),
        ("rows of the stabilizer sub-window where the raw and realizable "
         "tests agree at the carrier grain", agree_cell, len(tri_sub),
         WS, WS),
        ("driven-window histories unique at the actor grain, directionwise",
         r4["unique_at_the_actor_grain"], r4["histories"], WC, WC),
        ("driven-window histories unique at the actor grain, pairwise",
         r4["unique_at_the_actor_grain_at_the_pairwise_image"],
         r4["histories"], WC, WC),
        ("committed histories outside the stabilizer sub-window",
         len(corp) - len(tri_sub), len(corp), WC, WC),
        ("committed histories of C1 and C2 whose collapse threshold exceeds "
         "the tabulated ladder", above_tab_c1c2, len(corp), WC, WC),
        ("distinct histories carried by the corpus's slots",
         len(hist_mult), len(corp), WC, WC),
    ]
    R["measure_relativity"] = {
        "stamp": "COUNTING-ONLY",
        "declared_measure": None,
        "rows": [{"quantity": q, "numerator": n, "denominator": d,
                  "window": w, "numerator_window": w, "denominator_window": v,
                  "stamp": "COUNTING-ONLY"}
                 for (q, n, d, w, v) in ratios],
        "warrant": "no fraction in this unit is a probability: each is a "
                   "count over a declared window and carries that window's "
                   "name beside it (E-24)",
    }
    if mut("MUT-E24-ROW"):
        R["measure_relativity"]["rows"][0]["stamp"] = "PROBABILITY"
    for (_q, n, d, _w, _v) in ratios:
        reg(n, d)
    reg(len(ratios))
    LD.gate("G-E24-COUNTING-ONLY",
            "EVERY PUBLISHED FRACTION CARRIES ITS WINDOW AND ITS STAMP, AND "
            "THE STAMP IS CHECKED ROW BY ROW (E-24).  %d ratios are "
            "published; each names its numerator, its denominator AND the "
            "declared window EACH member ranges over, and each row carries "
            "its own COUNTING-ONLY stamp because this unit declares no "
            "measure on partition lattices.  A ratio whose window is absent, "
            "whose numerator and denominator come from different declared "
            "windows, or whose own row is stamped anything else, fails here "
            "-- the top-level stamp is not taken as evidence about the rows"
            % len(ratios),
            all(r["window"] for r in R["measure_relativity"]["rows"])
            and all(r["numerator"] <= r["denominator"]
                    for r in R["measure_relativity"]["rows"])
            and all(r["numerator_window"] == r["denominator_window"]
                    for r in R["measure_relativity"]["rows"])
            and all(r["stamp"] == "COUNTING-ONLY"
                    for r in R["measure_relativity"]["rows"])
            and pick("MUT-E24", R["measure_relativity"]["stamp"],
                     "PROBABILITY") == "COUNTING-ONLY",
            "ratios %d, all windowed %s, windows matched %s, rows stamped "
            "%d of %d, top-level stamp %s"
            % (len(ratios),
               all(r["window"] for r in R["measure_relativity"]["rows"]),
               all(r["numerator_window"] == r["denominator_window"]
                   for r in R["measure_relativity"]["rows"]),
               sum(1 for r in R["measure_relativity"]["rows"]
                   if r["stamp"] == "COUNTING-ONLY"), len(ratios),
               R["measure_relativity"]["stamp"]))
    SEAL.take("SEAL-MEASURE", R)

    cb = []

    def bind(name, printed, recomputed):
        cb.append({"row": name, "printed": printed,
                   "recomputed": recomputed, "match": printed == recomputed})

    for r in actor_rows:
        bind("actor-census/%d" % r["index"],
             "NON-UNIQUE" if r["cardinality"] > 1 else "UNIQUE",
             "NON-UNIQUE" if len(r["admissible"]) > 1 else "UNIQUE")
    for r in cell_rows[:12]:
        bind("carrier-census/%d" % r["index"],
             "NON-UNIQUE" if r["cardinality"] > 1 else "UNIQUE",
             "NON-UNIQUE" if len(r["admissible"]) > 1 else "UNIQUE")
    for j, i in enumerate(leg1_actor_set):
        want = actor_partition_name(P9[i])
        bind("leg1-survivor/%d" % j, leg1_names[j], want)
    for j, p in enumerate(leg1_cell_survivors):
        bind("carrier-survivor/%d" % j, cell_names[j],
             cell_partition_name(p, window[p]))
    for tag, ev in (("C1", 9), ("C2", 18), ("C3", 12)):
        got = sorted({len(h) for (t, h) in corp if t == tag})
        bind("corpus/%s" % tag, "%s-HAS-%d-EVENTS" % (tag, ev),
             "%s-HAS-%d-EVENTS" % (tag, got[0]) if len(got) == 1
             else "%s-IS-RAGGED" % tag)
    bind("coin/fiber", R["coin_order"]["fiber"],
         "INERT-ON-EVERY-CENSUS-ROW" if coin_disagree == 0 else "LIVE")
    bind("atom/word", atom_word,
         atom_law(atom_breaks, complete_mismatch == 0))
    head_word = head_law(len(corp), a_non, c_non)
    bind("head/word", head_word, head_law(len(corp), a_non, c_non))
    if mut("MUT-CLASSWORD"):
        cb[0]["printed"] = "UNIQUE"
        cb[0]["match"] = cb[0]["printed"] == cb[0]["recomputed"]
    R["class_binding"] = {"rows": cb, "checked": len(cb),
                          "mismatches": sum(1 for r in cb if not r["match"])}
    reg(len(cb))
    LD.gate("G-CLASS-WORDS-BOUND-TO-PREDICATES",
            "EVERY PRINTED CLASS-WORD IS RECOMPUTED FROM ITS PREDICATE "
            "(#295).  %d rows carry a class word -- the census rows' "
            "uniqueness, the survivors' referent-bound names, each corpus's "
            "event shape, the coin fiber, the atom word and the head word -- "
            "and each is recomputed here from the object it describes and "
            "compared with the string that will be published.  A class-word "
            "swap dies at this gate rather than travelling into the paper"
            % len(cb),
            R["class_binding"]["mismatches"] == 0,
            "rows %d, mismatches %d"
            % (len(cb), R["class_binding"]["mismatches"]))
    SEAL.take("SEAL-CLASSBIND", R)

    # the instrument's own counts, registered from LIVE REGISTRIES so the
    # paper may cite them and no total in this unit is ever typed
    reg(len(SOURCES), len(VERBATIM), len(WINDOW_DECL), len(WALLS),
        sum(len(n) for (_w, n, _y) in WALLS), len(MUTANTS),
        len(SEALED_PATHS), len(CRITERION_FUNCS), len(COHERENCE_ROWS),
        len(GRAIN_ROWS), len(TEST_ROWS), len(CELL_STRATUM_NAMES),
        len(COIN_ORDERS), len(POLARITY), len(CLOSING_GATE_NAMES),
        len(REFERENT_AXES), len(CRITERION_ALLOWED_NAMES),
        sum(len(p) for (_n, _w, p) in REFERENT_AXES))
    inv_actor = sorted(a_inventory)
    slot = head_slot(head_word, a_non, c_non, len(corp), inv_actor,
                     sorted(c_inventory), R["actor_census"]["induced_image"])
    R["counts"] = {
        "histories": len(corp),
        "actor_lattice": len(P9), "carrier_window": len(winlist),
        "actor_leg1": len(leg1_actor_set),
        "carrier_leg1": len(leg1_cell_survivors),
        "actor_unique": a_cards[1], "carrier_unique": c_cards[1],
        "actor_unique_at_the_pairwise_image": pw_cards[1],
        "forced_under_either_image": img_min,
        "actor_non_unique": len(a_non), "carrier_non_unique": len(c_non),
        "atom_breaks": atom_breaks,
        "collapse_thresholds": wstar,
        "arena_group_order": len(autos),
        "coin_disagreements": coin_disagree,
    }
    SEAL.take("SEAL-COUNTS", R)

    segments = verdict_segments(R, head_word, atom_word, slot)
    R["verdict"] = {"segments": segments, "head_word": head_word,
                    "atom_word": atom_word, "slot": slot,
                    "field_spec": VERDICT_SPEC}
    alt = independent_head(corp, P9, BM, leg1_actor_set, winlist,
                           leg1_cell_survivors, window)
    R["verdict"]["second_route"] = alt
    same = (alt["head_word"] == head_word and alt["atom_word"] == atom_word
            and alt["actor_unique"] == a_cards[1]
            and alt["carrier_unique"] == c_cards[1]
            and alt["atom_breaks"] == atom_breaks
            and alt["complete_relation_returns_the_group_at"]
            == complete_equals_stab)
    LD.gate("G-VERDICT-RECONSTRUCTED-BY-A-SECOND-ROUTE",
            "THE HEAD IS DERIVED TWICE, BY ROUTES THAT SHARE NO DISPATCHER "
            "AND NO CENSUS LOOP.  The second route calls neither "
            "admissible_actor nor admissible_cell and reads none of the "
            "first route's rows: it rebuilds every admissible set from the "
            "raw leg predicates, recounts the atom breaks from the "
            "coherence relation directly rather than from the ladder's "
            "cache, re-derives BOTH inputs of the atom law -- the break "
            "count and the complete-relation comparison, neither carried in "
            "as a literal -- and re-applies both laws to its own numbers.  "
            "What the two routes DO share is the four leg predicates "
            "themselves, which are the object under test and are de-twinned "
            "by their own closed-form gates above, not by duplication.  The "
            "two agree on the head word, the atom word and all four counts: "
            "%s" % same,
            pick("MUT-HEAD-TWICE", same, False),
            "route A head %s atom %s unique %d/%d; route B head %s atom %s "
            "unique %d/%d" % (head_word, atom_word, a_cards[1], c_cards[1],
                              alt["head_word"], alt["atom_word"],
                              alt["actor_unique"], alt["carrier_unique"]))
    fams_ok = any(head_word.startswith(f) for f in fams) and any(
        atom_word.startswith(f) for f in fams)
    LD.gate("G-HEAD-WORDS-COME-FROM-THE-PIN",
            "THE HEAD'S WORDS ARE THE PIN'S WORDS.  Both derived words are "
            "required to begin with one of the %d families parsed out of the "
            "pin's bytes, so a head that invented a vocabulary -- or a "
            "repair that quietly widened one -- fails here rather than in "
            "review" % len(fams),
            pick("MUT-HEADFAM", fams_ok, False),
            "head %s, atom %s, families %s" % (head_word, atom_word,
                                               sorted(fams)))
    SEAL.take("SEAL-VERDICT", R)

    say()
    for s in segments:
        say(s)
    return R, src, paper_text


VERDICT_SPEC = [
    ("FAC-DECOMPOSITION", [
        ("THESIS", None, ""),
        ("HISTORIES", "counts/histories", ""),
        ("ACTOR-LATTICE", "counts/actor_lattice", ""),
        ("ACTOR-GRAIN-LAW-COMPATIBLE-PARTITIONS", "counts/actor_leg1", ""),
        ("ACTOR-GRAIN-UNIQUE-FACTORIZATION",
         "counts/actor_unique|counts/histories",
         "-AT-THE-DIRECTIONWISE-IMAGE"),
        ("ACTOR-GRAIN-UNIQUE-FACTORIZATION-AT-THE-PAIRWISE-IMAGE",
         "counts/actor_unique_at_the_pairwise_image|counts/histories", ""),
        ("DIVISION-FORCED-UNDER-EITHER-IMAGE-AT-LEAST",
         "counts/forced_under_either_image|counts/histories", ""),
        ("CARRIER-WINDOW", "counts/carrier_window", ""),
        ("CARRIER-GRAIN-LAW-COMPATIBLE-PARTITIONS", "counts/carrier_leg1",
         ""),
        ("CARRIER-GRAIN-UNIQUE-FACTORIZATION",
         "counts/carrier_unique|counts/histories", ""),
        ("COIN-ORDER-DISAGREEMENTS", "counts/coin_disagreements", ""),
    ]),
    ("FAC-GROUPOID", [
        ("ATOM", None, ""),
        ("ATOM-BREAKS", "counts/atom_breaks|counts/histories", ""),
        ("COLLAPSE-THRESHOLDS", "counts/collapse_thresholds", ""),
        ("ARENA-GROUP-ORDER", "counts/arena_group_order", ""),
    ]),
]


def verdict_segments(R, head_word, atom_word, slot):
    """the head, rendered from a declared field spec whose every field names a
    receipt path; the audit route types no copy of any of it."""
    out = []
    for label, fields in VERDICT_SPEC:
        parts = []
        for (nm, path, suffix) in fields:
            if path is None:
                parts.append("%s=%s" % (nm, "THE-LAW-ADMITS-MORE-THAN-ONE-"
                                        "FACTORIZATION-ONLY-WHERE-THE-"
                                        "HISTORY-REPEATS-A-PARALLEL-CLASS"
                                        if nm == "THESIS" else atom_word))
                continue
            if "|" in path:
                a, b = path.split("|")
                parts.append("%s=%s-OF-%s%s" % (nm, com(jpath(R, a)),
                                                com(jpath(R, b)), suffix))
            else:
                v = jpath(R, path)
                parts.append("%s=%s%s" % (nm, ",".join(str(x) for x in v)
                                          if isinstance(v, list) else com(v),
                                          suffix))
        out.append("%s<%s>" % (label, "; ".join(parts)))
    out.append("%s<%s; ATOM=%s; SCOPE=%s>"
               % (head_word, slot, atom_word,
                  "TWO-GRAINS-AS-DECLARED;COUNTS-ARE-COUNTING-ONLY;"
                  "THE-CARRIER-WINDOW-IS-DECLARED-NOT-COMPLETE;"
                  "NO-CLAIM-BEYOND-THE-MEASURED-COHERENCE-DEPTH"))
    return out


def independent_head(corp, P9, BM, leg1_actor_set, winlist,
                     leg1_cell_survivors, window):
    """ROUTE B.  The same three numbers, rebuilt from the raw predicates with
    no call to the criterion's dispatcher and no reading of route A's rows.

    BOTH inputs of the atom law are re-derived here (K2 MINOR-2): the break
    count from the coherence relation directly, and the complete-relation
    comparison -- whether gluing pairwise-coherent families still returns the
    global group -- from its own enumeration, rather than carried in as a
    literal from the ladder gate."""
    au = cu = ab = holds = 0
    an, cn = [], []
    for k, (_tag, H) in enumerate(corp):
        rec = record_field(H)
        foot = [cell_footprint(F) for F in H]
        na = 0
        for i in leg1_actor_set:
            p = P9[i]
            if not leg2_actor(p, H) or not leg3_actor(p, rec):
                continue
            cp = induced_cell_partition(p)
            if leg4_cell(cp, rec, "G.D") and leg4_cell(cp, rec, "D.G"):
                na += 1
        nc = 0
        for cp in leg1_cell_survivors:
            if not leg2_cell(cp, foot) or not leg3_cell(cp, rec):
                continue
            if leg4_cell(cp, rec, "G.D") and leg4_cell(cp, rec, "D.G"):
                nc += 1
        au += (na == 1)
        cu += (nc == 1)
        if na != 1:
            an.append(k)
        if nc != 1:
            cn.append(k)
        stab = young_order(signature_blocks(H))
        if gamma_relation_count(H, [(t, s) for t in range(len(H))
                                    for s in range(t)]) == stab:
            holds += 1
        if stab == 1 and \
                gamma_relation_count(H, [(t, t - 1) for t in
                                         range(1, len(H))]) > 1:
            ab += 1
    return {"actor_unique": au, "carrier_unique": cu, "atom_breaks": ab,
            "complete_relation_returns_the_group_at": holds,
            "histories": len(corp),
            "head_word": head_law(len(corp), an, cn),
            "atom_word": atom_law(ab, holds == len(corp))}


# ===========================================================================
# SECTION 11.  THE PAPER INSTRUMENT
# ===========================================================================

def paper_claims(R):
    """the sentences the paper MUST carry, each rendered from the receipt so
    the paper's prose can never drift from the run's numbers."""
    c = R["counts"]
    out = [
        ("C01", "the geometry leg admits %d of the %s partitions of the nine "
                "actors" % (c["actor_leg1"], com(c["actor_lattice"]))),
        ("C02", "the actor-grain factorization is unique at %s of %s "
                "committed histories" % (com(c["actor_unique"]),
                                         com(c["histories"]))),
        ("C03", "the carrier-grain factorization is unique at %s of %s "
                "committed histories" % (com(c["carrier_unique"]),
                                         com(c["histories"]))),
        ("C04", "the declared carrier window carries %s partitions and the "
                "geometry leg admits %d of them"
                % (com(c["carrier_window"]), c["carrier_leg1"])),
        ("C05", "the two declared coin orders disagree on %d census rows"
                % c["coin_disagreements"]),
        ("C06", "the global stabilizer is trivial and the "
                "adjacent-coherence groupoid is not at %s histories"
                % com(c["atom_breaks"])),
        ("C07", "the collapse thresholds this corpus carries are %s"
                % ", ".join(str(w) for w in c["collapse_thresholds"])),
        ("C08", "the arena's own automorphism group has order %d"
                % c["arena_group_order"]),
        ("C09", "the complete coherence relation returns the global "
                "stabilizer at %s of %s histories"
                % (com(R["groupoid"]["complete_equals_the_global_stabilizer"]),
                   com(c["histories"]))),
        ("C10", "the record field is site-constant at %s of %s committed "
                "histories" % (com(c["histories"] -
                                   R["leg_binding"]
                                   ["record_non_site_constant_histories"]),
                               com(c["histories"]))),
        ("C11", "the head law returns %s on the strict triples, %s on the "
                "four class-repeating histories and %s on the whole corpus"
                % (R["controls"]["declared_sub_arenas"][0]["head_word"],
                   R["controls"]["declared_sub_arenas"][1]["head_word"],
                   R["controls"]["declared_sub_arenas"][3]["head_word"])),
        ("C12", "the criterion's combined digest is %s"
                % R["criterion"]["combined_sha256_12"]),
        ("C13", "at the pairwise image the actor-grain factorization is "
                "unique at %s of %s committed histories"
                % (com(c["actor_unique_at_the_pairwise_image"]),
                   com(c["histories"]))),
        ("C14", "under either image the division is forced at at least %s of "
                "%s committed histories"
                % (com(c["forced_under_either_image"]), com(c["histories"]))),
        ("C15", "the dynamics leg removes no partition the other legs admit "
                "at the actor grain and removes %d partition-history rows at "
                "the carrier grain"
                % R["leg_binding"]["by_grain"][1]["leg4_failures"]),
        ("C16", "%d of the %s committed histories repeat a parallel class"
                % (R["thesis"]["histories_that_repeat_a_parallel_class"],
                   com(c["histories"]))),
        ("C17", "the %s committed histories are slots carrying %s distinct "
                "histories" % (com(R["corpus_multiset"]["slots"]),
                               com(R["corpus_multiset"]["distinct"]))),
        ("C18", "the largest raw carrier stabilizer this corpus carries is "
                "%s, which is 27 factorial"
                % com(R["grain_triangle"]["max_raw_carrier_stabilizer"])),
        ("C19", "all %d strict triples carry exactly one history-leg "
                "survivor and a trivial stabilizer"
                % R["transport"]["R6_is_forced_by_R3"]
                ["C1_histories_with_exactly_one_leg2_survivor"]),
        # THE PIN'S DIGEST, BOUND (K3 MAJOR-1, second face).  The paper states
        # the pin's digest in its own front matter; nothing compared that
        # string with the digest this run measures, so it was a free-floating
        # token exactly as the criterion digest was.  Rendering it here from
        # the PROVENANCE ROW the run measured makes a forged pin digest fail
        # at G-PAPER-CLAIMS.  The label is a module constant so this
        # function's own string literals stay numeral-free.
        ("C20", "%s, %s %s"
                % (PIN_REL, DIGEST_LABEL,
                   next(p["measured"] for p in R["provenance"]
                        if p["anchor"] == "A-PIN"))),
    ]
    return [{"id": i, "sentence": s} for (i, s) in out]


def paper_tables(R):
    """EVERY table this paper carries is rendered here from the receipt --
    HEADERS INCLUDED, as claims in their own right (PER-R Z7)."""
    T = {}
    T["T1-THE-GEOMETRY-LEG"] = {
        "header": ["grain", "candidate set", "geometry-leg survivors"],
        "rows": [["actor", com(R["counts"]["actor_lattice"]),
                  str(R["counts"]["actor_leg1"])],
                 ["carrier", com(R["counts"]["carrier_window"]),
                  str(R["counts"]["carrier_leg1"])]]}
    T["T2-THE-CENSUS"] = {
        "header": ["grain", "unique", "non-unique", "histories"],
        "rows": [["actor", com(R["counts"]["actor_unique"]),
                  str(R["counts"]["actor_non_unique"]),
                  com(R["counts"]["histories"])],
                 ["carrier", com(R["counts"]["carrier_unique"]),
                  str(R["counts"]["carrier_non_unique"]),
                  com(R["counts"]["histories"])]]}
    T["T3-THE-COHERENCE-LADDER"] = {
        "header": ["corpus", "coherence relation", "distinct values",
                   "minimum", "maximum", "histories"],
        "rows": [[r["corpus"], r["relation"], str(r["distinct_values"]),
                  com(r["minimum"]), com(r["maximum"]), com(r["histories"])]
                 for r in R["groupoid"]["by_relation"]]}
    T["T4-THE-GRAIN-TRIANGLE"] = {
        "header": ["corpus", "TEST-RAW at ACTOR-S9",
                   "TEST-RAW at CARRIER-S27", "TEST-REALIZABLE at SITE",
                   "TEST-REALIZABLE at CARRIER", "histories"],
        "rows": [[r["corpus"], com(r["TEST-RAW-at-ACTOR-S9"]),
                  com(r["TEST-RAW-at-CARRIER-S27"]),
                  com(r["TEST-REALIZABLE-at-SITE"]),
                  com(r["TEST-REALIZABLE-at-CARRIER"]),
                  com(r["histories"])]
                 for r in R["grain_triangle"]["rows"]]}
    T["T5-THE-CONTROL-ARM"] = {
        "header": ["declared arena", "histories", "actor non-unique",
                   "carrier non-unique", "head word"],
        "rows": [[r["arena"], com(r["histories"]),
                  str(r["actor_non_unique"]), str(r["carrier_non_unique"]),
                  r["head_word"]]
                 for r in R["controls"]["declared_sub_arenas"]]}
    T["T6-THE-SYNTHETIC-CONTROLS"] = {
        "header": ["synthetic history", "events", "distinct record rows",
                   "LEG-3 passers", "wedge", "global stabilizer",
                   "adjacent families", "atom word", "atom row"],
        "rows": [[r["arena"], str(r["events"]),
                  str(r["distinct_record_rows"]),
                  com(r["leg3_passers_of_the_lattice"]),
                  str(r["record_dynamics_wedge"]),
                  com(r["global_stabilizer"]),
                  com(r["adjacent_coherent_families"]), r["atom_word"],
                  r["atom_row_is"]]
                 for r in R["controls"]["synthetic_histories"]]}
    T["T7-THE-ALTERNATIVE-LINK-SETS"] = {
        "header": ["synthetic arena", "declared links",
                   "geometry-leg survivors"],
        "rows": [[r["arena"], str(r["declared_links"]),
                  com(r["leg1_survivors"])]
                 for r in R["controls"]["alternative_link_sets"]]}
    T["T8-THE-INDUCED-IMAGE-FIBER"] = {
        "header": ["induced image", "unique", "non-unique", "histories",
                   "class partitions that join the discrete one"],
        "rows": [[r["induced_image"], com(r["unique"]), str(r["non_unique"]),
                  com(r["histories"]),
                  ", ".join(n.rsplit("-", 1)[1]
                            for n in r["inventory_at_the_non_unique"])
                  or "none"]
                 for r in R["image_fiber"]["rows"]]}
    T["T9-WHICH-LEG-BINDS-BY-GRAIN"] = {
        "header": ["grain", "LEG-3 failures", "LEG-4 evaluations",
                   "LEG-4 failures", "unique with LEG-4",
                   "unique without LEG-4"],
        "rows": [[r["grain"], str(r["leg3_failures"]),
                  com(r["leg4_evaluations"]), str(r["leg4_failures"]),
                  com(r["unique_with_leg4"]),
                  com(r["unique_without_leg4"])]
                 for r in R["leg_binding"]["by_grain"]]}
    T["T10-THE-CARRIER-INVENTORY"] = {
        "header": ["admissible factorizations", "histories"],
        "rows": [[k, com(v)] for k, v in
                 sorted(R["cell_census"]["cardinality_distribution"].items(),
                        key=lambda kv: int(kv[0]))]}
    T["T11-THE-CARRIER-SUB-WINDOWS"] = {
        "header": ["declared sub-window", "geometry-leg survivors",
                   "carrier-grain unique"],
        "rows": [[r["sub_window"], str(r["survivors"]), com(r["unique_at"])]
                 for r in R["cell_census"]["sub_window_censuses"]]}
    T["T12-THE-CORPUS-AS-A-MULTISET"] = {
        "header": ["corpus", "slots", "distinct histories"],
        "rows": [[r["corpus"], com(r["slots"]), com(r["distinct"])]
                 for r in R["corpus_multiset"]["rows"]]}
    return T


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
GATELINE = re.compile(r"\[(?:PASS|FAIL)\]\s+(\S+)")
NUMTOK = re.compile(r"(?:(?<![\w.])-)?\d[\d,]*(?:\.\d+)?(?:/\d+)?")
WORDTOK = re.compile(r"[a-z]+")
HEADNUM = re.compile(r"^#{2,6}\s+(\d+(?:\.\d+)*)\.?\s", re.M)
SECREF = re.compile(r"(?:(RUNBOOK|OCC|AID|E|PER-L|PER-R)\s*)?§\s*"
                    r"(\d+(?:\.\d+)*)")
NUMERAL_EXEMPTIONS = ()
FENCE_COPIES = 2
# A sha256-12 IDENTIFIER IS NOT A PUBLISHED NUMBER (#267 M6).  Twelve-character
# hexadecimal tokens carrying at least one letter are masked out of the paper
# before the numeral scan -- and out of the totality reference too, so the scan
# stays total by arithmetic rather than by exemption.
HEXTOK = re.compile(r"\b(?=[0-9a-f]{12}\b)[0-9a-f]*[a-f][0-9a-f]*\b")
RATIO_PAT = re.compile(r"([\d][\d,]*)\s+of\s+(?:the\s+)?([\d][\d,]*)")
# `N against M` is a published relation too -- the carrier window against
# Bell(27) is written that way and escaped a scan keyed on `of` alone
# (K2 MINOR-11).
AGAINST_PAT = re.compile(r"([\d][\d,]*)\s+against\s+(?:the\s+)?([\d][\d,]*)")
REFERENT_RELATION_PATS = (("of", RATIO_PAT), ("against", AGAINST_PAT))


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
                out.add(t.replace(",", ""))
        elif isinstance(o, dict):
            for k in sorted(o, key=str):
                if k in ("sha256_12", "payload_sha256_12"):
                    continue
                walk(k)
                walk(o[k])
        elif isinstance(o, (list, tuple)):
            for v in o:
                walk(v)
    for key in MEASURED_KEYS + ("schema", "provenance", "windows",
                                "paper_tables", "paper_claims", "totals",
                                "coverage", "reachability",
                                "pre_registered_outcomes", "walls"):
        if key in R:
            walk(R[key])
    return out


# THE DECLARED REFERENT AXES (K3 MAJOR-2c).  The delivered instrument bound a
# ratio to a top-level RECEIPT KEY, and a receipt key is not a quantity: the
# actor census carries both a history axis and a partition-lattice axis, so
# `5,852 of 21,147` -- a history count over a lattice size, every numeral true
# and the relation false -- bound through `actor_census` and survived.  A
# universe is therefore a QUANTITY AXIS here: an explicit list of receipt
# PATHS whose values are counts of one and the same kind of thing.  The
# aggregate keys (`counts`, `verdict`, `measure_relativity`) are absent by
# declaration, as before, and so are `windows` and `class_binding`, which mix
# axes by construction; every number they carry lives in its measurement's own
# path too, so nothing is lost.
REFERENT_AXES = (
    ("AXIS-COMMITTED-HISTORIES",
     "counts of committed history SLOTS and of sub-windows of them",
     ("corpora/C1_strict_triples", "corpora/C2_concatenations",
      "corpora/C3_window_schedules", "corpora/total_histories",
      "corpora/distinct_histories", "corpora/C3_tags/*",
      "corpus_multiset/slots", "corpus_multiset/distinct",
      "corpus_multiset/duplicate_slots",
      "corpus_multiset/histories_appearing_more_than_once",
      "corpus_multiset/rows/*/slots", "corpus_multiset/rows/*/distinct",
      "actor_census/histories", "actor_census/unique_at",
      "actor_census/non_unique_at", "actor_census/cardinality_distribution/*",
      "actor_census/inventory/*",
      "actor_census_pairwise/histories", "actor_census_pairwise/unique_at",
      "actor_census_pairwise/non_unique_at",
      "actor_census_pairwise/cardinality_distribution/*",
      "actor_census_pairwise/inventory/*",
      "image_fiber/histories", "image_fiber/rows/*/unique",
      "image_fiber/rows/*/non_unique", "image_fiber/rows/*/histories",
      "image_fiber/division_is_forced_at_least_at",
      "cell_census/histories", "cell_census/unique_at",
      "cell_census/non_unique_at", "cell_census/cardinality_distribution/*",
      "cell_census/inventory/*",
      "cell_census/sub_window_censuses/*/unique_at",
      "cell_census/sub_window_censuses/*/cardinality_distribution/*",
      "cell_census/inventory_by_admissible_set/*/histories",
      "cross_grain/actor_non_unique", "cross_grain/carrier_non_unique",
      "cross_grain/carrier_only", "cross_grain/actor_only",
      "thesis/histories_that_repeat_a_parallel_class",
      "thesis/histories_that_use_one_class_in_every_round",
      "thesis/actor_non_unique_inside_the_condition",
      "thesis/actor_non_unique", "thesis/carrier_non_unique",
      "thesis/carrier_non_unique_inside_the_condition",
      "thesis/class_constant_inside_the_carrier_non_unique",
      "leg_binding/sub_window", "leg_binding/complement",
      "leg_binding/profiles/*/histories",
      "leg_binding/record_non_site_constant_histories",
      "leg_binding/by_grain/*/unique_with_leg4",
      "leg_binding/by_grain/*/unique_without_leg4",
      "leg_binding/by_grain/*/cardinality_profile_with_leg4/*",
      "leg_binding/by_grain/*/cardinality_profile_without_leg4/*",
      "groupoid/by_relation/*/histories", "groupoid/ladder/*/histories",
      "groupoid/arrow_profiles/*/histories", "groupoid/histories",
      "groupoid/complete_equals_the_global_stabilizer",
      "groupoid/complete_mismatches", "groupoid/free_product_mismatches",
      "groupoid/arrow_sub_window", "groupoid/arrow_sub_window_complement",
      "groupoid/histories_whose_threshold_exceeds_the_tabulated_ladder",
      "groupoid/of_those_in_C1_and_C2", "groupoid/collapse_thresholds/*",
      "atom/histories_with_a_trivial_global_stabilizer",
      "atom/of_those_carrying_a_nontrivial_adjacent_coherent_family",
      "atom/three_predicates_one_split/actor_grain_non_unique",
      "atom/three_predicates_one_split/nontrivial_global_stabilizer",
      "atom/three_predicates_one_split/no_atom_break",
      "grain_triangle/sub_window", "grain_triangle/complement",
      "grain_triangle/rows/*/histories",
      "grain_triangle/raw_and_realizable_agree_at_the_actor_grain",
      "grain_triangle/raw_and_realizable_agree_at_the_carrier_grain",
      "persistence/identity_forced_at_the_complete_relation",
      "persistence/identity_forced_at_the_adjacent_relation",
      "persistence/collapse_threshold_distribution/*",
      "transport/ladder_rows/*/histories",
      "transport/ladder_rows/*/unique_at_the_actor_grain",
      "transport/ladder_rows/*/"
      "unique_at_the_actor_grain_at_the_pairwise_image",
      "transport/ladder_rows/*/unique_at_the_carrier_grain",
      "transport/ladder_rows/*/atom_breaks",
      "transport/R6_is_forced_by_R3/C1_histories",
      "transport/R6_is_forced_by_R3/"
      "C1_histories_with_exactly_one_leg2_survivor",
      "transport/R6_is_forced_by_R3/C1_histories_with_a_trivial_stabilizer",
      "controls/declared_sub_arenas/*/histories",
      "controls/declared_sub_arenas/*/actor_non_unique",
      "controls/declared_sub_arenas/*/carrier_non_unique")),
    ("AXIS-ACTOR-PARTITIONS",
     "counts of partitions of the nine actors",
     ("arena/actor_lattice", "actor_census/lattice",
      "actor_census/leg1_geometry_survivors",
      "actor_census/subgroup_coset_partitions",
      "actor_census_pairwise/lattice",
      "actor_census_pairwise/leg1_geometry_survivors",
      "leg_binding/lattice", "leg_binding/profiles/*/leg1",
      "leg_binding/profiles/*/leg2", "leg_binding/profiles/*/leg3",
      "leg_binding/profiles/*/all_three",
      "controls/synthetic_histories/*/leg3_passers_of_the_lattice",
      "controls/alternative_link_sets/*/leg1_survivors")),
    ("AXIS-CARRIER-PARTITIONS",
     "counts of partitions of the twenty-seven cells",
     ("arena/carrier_lattice", "cell_census/window", "cell_census/ambient",
      "cell_census/leg1_geometry_survivors",
      "cell_census/distinct_leg1_survivor_names",
      "cell_census/families/*",
      "cell_census/sub_window_censuses/*/survivors")),
    ("AXIS-LEG-EVALUATION-ROWS",
     "counts of partition-history rows a leg was evaluated on",
     ("coin_order/leg4_evaluations_per_order",
      "coin_order/leg4_passes_per_order/*",
      "coin_order/leg4_failures_per_order",
      "coin_order/rows_where_the_orders_disagree",
      "actor_census_pairwise/leg4_passes_per_order/*",
      "actor_census_pairwise/rows_where_the_orders_disagree",
      "leg_binding/by_grain/*/leg3_evaluations_after_leg2",
      "leg_binding/by_grain/*/leg3_failures",
      "leg_binding/by_grain/*/leg4_evaluations",
      "leg_binding/by_grain/*/leg4_failures",
      "leg_binding/by_grain/*/leg4_failures_over_distinct_histories",
      "leg_binding/by_grain/*/record_dynamics_wedge",
      "leg_binding/leg4_fineness/comparisons",
      "leg_binding/leg4_fineness/disagreements",
      "controls/record_dynamics_wedge_on_the_control",
      "controls/record_dynamics_wedge_on_the_committed_corpus/*",
      "controls/synthetic_histories/*/record_dynamics_wedge")),
    ("AXIS-COHERENT-FAMILIES",
     "counts of coherent families of local identifications",
     ("groupoid/by_relation/*/minimum", "groupoid/by_relation/*/maximum",
      "groupoid/by_relation/*/distinct_values",
      "groupoid/ladder/*/R-EMPTY", "groupoid/ladder/*/R-ADJACENT",
      "groupoid/ladder/*/R-WINDOW-2", "groupoid/ladder/*/R-WINDOW-3",
      "groupoid/ladder/*/R-ROUND", "groupoid/ladder/*/R-COMPLETE",
      "groupoid/arrow_isotropy_products/*/isotropy_product",
      "controls/synthetic_histories/*/adjacent_coherent_families")),
    ("AXIS-STABILIZER-ORDERS",
     "orders of stabilizer groups and of the arena's own group",
     ("arena/arena_automorphism_order", "grain_triangle/arena_group_order",
      "grain_triangle/cells_factorial",
      "grain_triangle/max_raw_carrier_stabilizer",
      "grain_triangle/min_raw_carrier_stabilizer",
      "grain_triangle/rows/*/TEST-RAW-at-ACTOR-S9",
      "grain_triangle/rows/*/TEST-RAW-at-CARRIER-S27",
      "grain_triangle/rows/*/TEST-REALIZABLE-at-SITE",
      "grain_triangle/rows/*/TEST-REALIZABLE-at-CARRIER",
      "groupoid/ladder/*/global_stabilizer",
      "controls/synthetic_histories/*/global_stabilizer")),
    ("AXIS-ARENA-SHAPE",
     "the arena's and the carrier's own cardinalities",
     ("arena/sites", "arena/declared_links", "arena/parallel_classes",
      "arena/groupings", "arena/saturating_groupings",
      "arena/strict_triples", "arena/flat_quadruples",
      "arena/window_schedules", "carrier/cells",
      "carrier/distinct_co_division_pairs",
      "carrier/cells_with_exactly_two_actors", "carrier/cells_per_actor/*",
      "carrier/actors_in_that_many_cells",
      "cell_census/leg1_survivors/*/blocks")),
    ("AXIS-COHERENCE-WIDTHS",
     "sliding-window widths in event index",
     ("persistence/collapse_threshold_values/*",
      "groupoid/threshold_values/*", "groupoid/tabulated_ladder_top")),
    ("AXIS-EVENTS-PER-HISTORY",
     "numbers of division events in a history",
     ("groupoid/ladder/*/events", "controls/synthetic_histories/*/events",
      "groupoid/arrow_isotropy_products/*/events",
      "groupoid/arrow_profiles/*/objects")),
    ("AXIS-CRITERION-SURFACE",
     "line counts of the criterion's own functions",
     ("criterion/functions/*/lines",)),
)
REFERENT_AGGREGATES_EXCLUDED = ["counts", "verdict", "measure_relativity",
                                "windows", "class_binding"]


def axis_ints(R, path):
    """the integers a declared axis path resolves to.  `*` descends through a
    list's members or a dict's values."""
    cur = [R]
    for part in path.split("/"):
        nxt = []
        for o in cur:
            if part == "*":
                if isinstance(o, dict):
                    nxt.extend(o.values())
                elif isinstance(o, (list, tuple)):
                    nxt.extend(o)
            elif isinstance(o, dict) and part in o:
                nxt.append(o[part])
        cur = nxt
    out = set()

    def collect(v):
        if isinstance(v, bool):
            return
        if isinstance(v, int):
            out.add(v)
        elif isinstance(v, (list, tuple)):
            for x in v:
                collect(x)
    for v in cur:
        collect(v)
    return out


def referent_axis_index(R):
    """axis name -> the set of integers that axis carries, and the paths that
    resolved to nothing, so a mistyped path is a gate failure and not a
    silently empty universe."""
    index, empty = {}, []
    for (name, _why, paths) in REFERENT_AXES:
        vals = set()
        for p in paths:
            got = axis_ints(R, p)
            if not got:
                empty.append(p)
            vals |= got
        index[name] = vals
    return index, empty


def receipt_paths_for(tok, R, index=None):
    """which declared referent AXIS carries a numeral."""
    if index is None:
        index, _e = referent_axis_index(R)
    try:
        v = int(tok.replace(",", ""))
    except ValueError:
        return set()
    return {name for name, vals in index.items() if v in vals}


def referent_binding(R, text):
    """#293 Z6 / PER-R Z10: no sentence pairs numerals from different
    universes.  Every `N of M` and `N against M` relation in the paper is
    resolved against the receipt and both numerals are required to be carried
    by one common DECLARED QUANTITY AXIS.

    TOTALITY (K3 MAJOR-2a).  The relations found in the scanned body are
    counted against the relations present in the paper's own bytes under
    nothing but unicode folding and whitespace normalisation, so a relation
    the scanner fails to SEE is a failure rather than a silent pass -- which
    is exactly how a false ratio hid behind a markdown list marker."""
    prepared = SECREF.sub(" ", HEADNUM.sub("#### ", text))
    body = canon_numeric(prepared, mut("MUT-CANON-NUMERALS"))
    raw = numeral_reference_body(prepared)
    if mut("MUT-REFERENT"):
        body = body + " and 5,852 of 42,295 members "
        raw = raw + " and 5,852 of 42,295 members "
    if mut("MUT-REFERENT-TOTALITY"):
        body = RATIO_PAT.sub(" ", body, count=1)
    index, empty_paths = referent_axis_index(R)
    bad, checked, skipped, found = [], 0, 0, 0
    for (_kind, pat) in REFERENT_RELATION_PATS:
        for m in pat.finditer(body):
            n, d = m.group(1).strip(","), m.group(2).strip(",")
            found += 1
            if n == d:
                skipped += 1
                continue
            checked += 1
            pn = receipt_paths_for(n, R, index)
            pd = receipt_paths_for(d, R, index)
            if not (pn & pd):
                bad.append("%s of %s" % (n, d))
    reference = sum(len(pat.findall(raw))
                    for (_kind, pat) in REFERENT_RELATION_PATS)
    return {"relations_checked": checked,
            "relations_found_in_the_scanned_body": found,
            "relations_in_the_paper": reference,
            "scan_is_total": found == reference,
            "relations_skipped_as_trivial": skipped,
            "unbound": sorted(set(bad)),
            "axes": [{"axis": nm, "quantity": why, "paths": len(ps),
                      "integers_carried": len(index[nm])}
                     for (nm, why, ps) in REFERENT_AXES],
            "axis_paths_that_resolved_to_nothing": sorted(empty_paths),
            "aggregates_excluded": REFERENT_AGGREGATES_EXCLUDED,
            "rule": "the numerator and the denominator of every published "
                    "relation must be carried by one common DECLARED "
                    "QUANTITY AXIS of this run's receipt -- an axis is a list "
                    "of receipt paths whose values count the same kind of "
                    "thing, not a top-level key, because a key carrying two "
                    "axes binds a false relation between them"}


def paper_coverage(R, text):
    allow = set(NUMREG) | receipt_numbers(R)
    for seg in R["verdict"]["segments"]:
        for t in NUMTOK.findall(seg):
            allow.add(t)
            allow.add(t.replace(",", ""))
    exempt = [list(e) for e in NUMERAL_EXEMPTIONS]
    if mut("MUT-EXEMPTION-DEAD"):
        exempt = exempt + [["4242", "a literal that occurs nowhere"]]
    exempt_lits = {e[0] for e in exempt}
    body = text if not mut("MUT-COVERAGE-SCAN") else FENCE.sub("", text)
    heads = set(HEADNUM.findall(body))

    def prep(t):
        return HEXTOK.sub(" ", SECREF.sub(" ", HEADNUM.sub("#### ", t)))
    body = prep(body)
    reference = len(NUMTOK.findall(prep(text)))
    scanned, unbacked, fired = 0, [], Counter()
    for tok in NUMTOK.findall(body):
        scanned += 1
        if tok in allow or tok.replace(",", "") in allow:
            continue
        if tok in exempt_lits:
            fired[tok] += 1
            continue
        unbacked.append(tok)

    def spelled(t):
        """THE SPELLED SCAN, WITH COMPOUNDS AND A TOTALITY REFERENCE (K3 m9).
        A maximal run of adjacent number-words that parses as one English
        numeral asserts that numeral and is checked as one; a run that does
        not parse is checked atom by atom, as before.  A compound built from
        individually backed atoms therefore cannot ride in."""
        toks = WORDTOK.findall(canon_numeric(t).lower())
        if mut("MUT-SPELLED-COMPOUND"):
            toks = toks + ["five", "thousand", "eight", "hundred", "fifty",
                           "three"]
        seen, bad, comps = 0, [], []
        i = 0
        while i < len(toks):
            if toks[i] not in WORDNUM:
                i += 1
                continue
            j = i
            while j < len(toks) and toks[j] in WORDNUM:
                j += 1
            run = toks[i:j]
            seen += len(run)
            val = spelled_compound(run) if len(run) > 1 else None
            if val is not None:
                comps.append(" ".join(run))
                if not (str(val) in allow or com(val) in allow):
                    bad.append(" ".join(run))
            else:
                for wd in run:
                    v = WORDNUM[wd]
                    if not (str(v) in allow or com(v) in allow):
                        bad.append(wd)
            i = j
        return seen, bad, comps
    words, word_unbacked, compounds = spelled(body)
    spelled_reference = spelled(prep(text))[0]
    if mut("MUT-PAPER-FENCE-MULTISET"):
        seg = R["verdict"]["segments"][0]
        text = text.replace(seg, seg.replace("ACTOR", "FORGED"), 1)
    if mut("MUT-FENCE-SURPLUS"):
        text = text + "\n```\nA FOURTH FENCE NO ROUTE RENDERED\n```\n"
    want = Counter({canon(seg): FENCE_COPIES
                    for seg in R["verdict"]["segments"]})
    got = Counter(canon(b) for b in FENCE.findall(text))
    return {"numerals_scanned": scanned,
            "numerals_in_the_whole_paper": reference,
            "scan_is_total": scanned == reference,
            "unbacked": sorted(set(unbacked)),
            "spelled_numerals_scanned": words,
            "spelled_numerals_in_the_whole_paper": spelled_reference,
            "spelled_scan_is_total": words == spelled_reference,
            "spelled_compounds": sorted(set(compounds)),
            "spelled_unbacked": sorted(set(word_unbacked)),
            "section_heads": len(heads),
            "verdict_fences_required": dict(sorted(want.items())),
            "verdict_fences_found": {k: v for k, v in sorted(got.items())},
            "fenced_blocks_in_the_paper": sum(got.values()),
            "fence_multiset_equal": got == want,
            "exemptions_declared": len(exempt),
            "exemptions_fired": {k: v for k, v in sorted(fired.items())},
            "exemptions_that_never_fired": sorted(e[0] for e in exempt
                                                  if e[0] not in fired)}


# THE POLARITY AXES.  Each names the asserted form and the inversion a forger
# would substitute, and each declares the SCOPE it is scanned over: PAPER for
# forms that may legitimately appear only as assertions, PROSE for forms whose
# opposite is legitimate DATA inside a table.  Scoping the bare atom word to
# the paper's prose is what lets its inversion be caught: the delivered axis
# keyed on the fence form alone, and the paper's own sentence claiming its
# atom word could be flipped at exit 0 (K3 MAJOR-3).  An axis whose asserted
# form has vanished fails too (K3 m10) -- an inversion that also deletes the
# original is still an inversion.
POLARITY = [
    ("head-word", "PAPER", "FAC-STRATIFIED<", "FAC-FACTORIZATION-FORCED<"),
    ("atom-word", "PAPER", "ATOM=FAC-ATOM-BREAKS-AT-THE-GROUPOID-GRAIN",
     "ATOM=FAC-ATOM-HOLDS-AT-THE-GROUPOID-GRAIN"),
    ("atom-word-in-prose", "PROSE", "FAC-ATOM-BREAKS-AT-THE-GROUPOID-GRAIN",
     "FAC-ATOM-HOLDS-AT-THE-GROUPOID-GRAIN"),
    ("thesis-direction", "PAPER",
     "ONLY-WHERE-THE-HISTORY-REPEATS-A-PARALLEL-CLASS",
     "EVERYWHERE-EXCEPT-WHERE-THE-HISTORY-REPEATS-A-PARALLEL-CLASS"),
    ("control-arm-word", "PAPER",
     "both grains are uniformly unique and the head law returns "
     "FAC-FACTORIZATION-FORCED",
     "both grains are uniformly unique and the head law returns "
     "FAC-FACTORIZATION-DECLARED"),
    ("image-fiber-direction", "PAPER",
     "induced-image fiber is not inert",
     "induced-image fiber is inert"),
    ("transport-direction", "PAPER", "does not transport",
     "transports freely"),
    ("binding-direction", "PAPER", "non-binding", "binding at every history"),
    ("measure-stamp", "PAPER", "COUNTING-ONLY", "under the declared measure"),
]


def prose_only(text):
    """the paper with its markdown table rows removed, so a word that is
    legitimate DATA in a table does not mask its own inversion in prose."""
    return "\n".join(line for line in text.split("\n")
                     if not (line.strip().startswith("|")
                             and line.strip().endswith("|")
                             and line.count("|") > 2))


def paper_polarity(R, text, mutated=False):
    whole, prose = canon(text), canon(prose_only(text))
    rows = []
    for (nm, scope, true_form, false_form) in POLARITY:
        body = prose if scope == "PROSE" else whole
        t = canon(true_form) in body
        f = canon(false_form) in body
        if mutated and nm == "atom-word":
            f = True
        if mut("MUT-POLARITY-ABSENT") and nm == "head-word":
            t = False
        rows.append({"axis": nm, "scope": scope,
                     "asserted_form_present": t,
                     "inverted_form_present": f})
    return {"rows": rows,
            "asserted_forms_absent": sum(1 for r in rows
                                         if not r["asserted_form_present"]),
            "inverted_forms_present": sum(1 for r in rows
                                          if r["inverted_form_present"])}


def template_constants(src, names):
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
                    continue
                bad.append((fn.name, tok))
    return bad


def norm_src(s):
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


# ===========================================================================
# SECTION 12.  THE FALSIFIERS AND THE CLOSING BATTERY
# ===========================================================================

MUTANTS = [
    ("MUT-PARTITION", "G-ARENA-SHAPE",
     "reports 0 groupings from the closed comparison, so the enumeration and "
     "the re-enumeration disagree", 'pick("MUT-PARTITION"'),
    ("MUT-CARRIER", "G-CELL-IS-A-CO-DIVISION-PAIR",
     "declares the cell-to-co-division-pair map not a bijection",
     'pick("MUT-CARRIER"'),
    ("MUT-OUTCOME-TYPED", "G-OUTCOMES-PARSED-FROM-THE-PIN",
     "replaces the outcome words parsed from the pin with a single typed "
     "literal, so the vocabulary stops being the pin's",
     'parsed = ["FAC-FACTORIZATION-FORCED-<witness>"]'),
    ("MUT-CRITERION-LEAK", "G-CRITERION-FROZEN-BEFORE-THE-CENSUS",
     "reports the criterion's legs referencing a census product, which is "
     "the thing the gate forbids", 'pick("MUT-CRITERION-LEAK"'),
    ("MUT-WINDOW", "G-WINDOWS-DECLARED-WITH-THEIR-BOUNDS",
     "reports the actor lattice at 0 members, so the window's claim to be "
     "complete in Bell(9) fails", 'pick("MUT-WINDOW"'),
    ("MUT-LEG1-THEOREM", "G-LEG1-IS-THE-SUBGROUP-COSET-THEOREM",
     "declares the geometry leg's survivors unequal to the subgroup coset "
     "partitions", 'pick("MUT-LEG1-THEOREM"'),
    ("MUT-ACTOR-CENSUS", "G-ACTOR-GRAIN-ADMISSIBLE-PER-HISTORY",
     "reports 0 unique-factorization histories at the actor grain, so the "
     "unique and non-unique counts no longer partition the corpus",
     'pick("MUT-ACTOR-CENSUS"'),
    ("MUT-CELL-CENSUS", "G-CARRIER-GRAIN-ADMISSIBLE-PER-HISTORY",
     "reports 0 unique-factorization histories at the carrier grain",
     'pick("MUT-CELL-CENSUS"'),
    ("MUT-CROSS", "G-CROSS-GRAIN-CONTAINMENT",
     "declares the actor grain's non-unique set not contained in the "
     "carrier grain's", 'pick("MUT-CROSS"'),
    ("MUT-COIN", "G-BOTH-COIN-ORDERS-PUBLISHED",
     "reports one coin-order disagreement where the run measured none, so "
     "the published fiber and the measurement part company",
     'pick("MUT-COIN"'),
    ("MUT-LEG2-THEOREM", "G-LEG2-IS-THE-SIGNATURE-REFINEMENT-THEOREM",
     "reports one mismatch between the history leg's enumeration and its "
     "closed form", 'pick("MUT-LEG2-THEOREM"'),
    ("MUT-LEGBIND", "G-WHICH-LEG-BINDS",
     "reports one history with a record that is not site-constant, "
     "contradicting the measured non-binding claim", 'pick("MUT-LEGBIND"'),
    ("MUT-GAMMA-COMPLETE", "G-GROUPOID-LADDER-PER-HISTORY",
     "reports one history at which the complete coherence relation does not "
     "return the global stabilizer", 'pick("MUT-GAMMA-COMPLETE"'),
    ("MUT-ATOM", "G-ATOM-THEOREM-AT-THE-GROUPOID-GRAIN",
     "substitutes a forged atom word for the derived one",
     'pick("MUT-ATOM"'),
    ("MUT-TRIANGLE", "G-GRAIN-TRIANGLE-BOTH-TESTS",
     "reports one mismatch between the Young-order route and the explicit "
     "filtration of the symmetric group", 'pick("MUT-TRIANGLE"'),
    ("MUT-PERSIST", "G-PERSISTENCE-PRESUPPOSITION",
     "reports no collapse-threshold values at all", 'pick("MUT-PERSIST"'),
    ("MUT-TRANSPORT", "G-TRANSPORT-ALONG-THE-R-LADDER",
     "declares the result not to transport across the rungs",
     'pick("MUT-TRANSPORT"'),
    ("MUT-CONTROLS", "G-EVERY-OUTCOME-WORD-EMITTABLE",
     "reports one pre-registered family that no declared arena reaches",
     'pick("MUT-CONTROLS"'),
    ("MUT-WEDGE", "G-THE-RECORD-LEG-IS-EXERCISED-SOMEWHERE",
     "reports the record-versus-dynamics wedge never firing on the control, "
     "which is what would make the record leg vacuous", 'pick("MUT-WEDGE"'),
    ("MUT-E24", "G-E24-COUNTING-ONLY",
     "stamps the published ratios as probabilities instead of counts",
     'pick("MUT-E24"'),
    ("MUT-CLASSWORD", "G-CLASS-WORDS-BOUND-TO-PREDICATES",
     "swaps the first census row's printed class word from NON-UNIQUE to "
     "UNIQUE while the predicate is unchanged", 'cb[0]["printed"]'),
    ("MUT-HEAD-TWICE", "G-VERDICT-RECONSTRUCTED-BY-A-SECOND-ROUTE",
     "declares the two independent head routes to disagree",
     'pick("MUT-HEAD-TWICE"'),
    ("MUT-HEADFAM", "G-HEAD-WORDS-COME-FROM-THE-PIN",
     "declares the derived words not to belong to the pin's families",
     'pick("MUT-HEADFAM"'),
    ("MUT-SEAL-DROP", "G-SEAL-TOTALITY",
     "silently omits the coverage seal from the manifest, so a published key "
     "travels unsealed", 'if mut("MUT-SEAL-DROP") and sid'),
    ("MUT-REFERENT", "G-SENTENCE-REFERENT-BINDING",
     "appends a ratio joining a census numerator to a window denominator, "
     "the LOR disease exactly", 'body = body + " and 5,852 of 42,295'),
    ("MUT-EXEMPTION-DEAD", "G-PAPER-NUMERAL-COVERAGE",
     "declares a numeral exemption that never fires", "exempt = exempt + "),
    ("MUT-COVERAGE-SCAN", "G-PAPER-NUMERAL-COVERAGE",
     "strips the fenced blocks before scanning, so the verdict's own "
     "numerals go unscanned", 'FENCE.sub("", text)'),
    ("MUT-PAPER-FENCE-MULTISET", "G-PAPER-NUMERAL-COVERAGE",
     "forges one copy of the first verdict fence, leaving its twin clean",
     'seg.replace("ACTOR", "FORGED")'),
    ("MUT-PAPER-CLAIM", "G-PAPER-CLAIMS",
     "drops one required claim sentence from the paper before matching",
     'texts_for_claims[:-1]'),
    ("MUT-PAPER-TABLE", "G-PAPER-TABLES-WITH-HEADERS",
     "swaps two column headers of the census table, leaving every data cell "
     "correct", 'hdr[1], hdr[2] = hdr[2], hdr[1]'),
    ("MUT-POLARITY", "G-PAPER-CLAIM-POLARITY",
     "passes the mutated flag into the polarity scanner, which then reports "
     "the inverted form of the atom axis present in the paper",
     'paper_polarity(R, paper_text, mut("MUT-POLARITY"))'),
    ("MUT-WALL-PLANT", "G-WALLS-SCAN-THE-PAPER",
     "appends every banned assertive sentence of every wall to the paper "
     "text the wall gate scans",
     'pick("MUT-WALL-PLANT", paper_text, paper_text'),
    ("MUT-TRANSCRIPT", "G-TRANSCRIPT-SEALED-WHOLE",
     "forges the last staged transcript line after the whole-transcript "
     "digest is taken", 'staged = staged[:-1]'),
    ("MUT-FINAL", "G-PAPER-INSTRUMENT-RAN-IN-THE-PLAIN-RUN",
     "reports zero numerals scanned, so the paper instrument would be "
     "claimed to have run while measuring nothing", 'pick("MUT-FINAL"'),
    ("MUT-SWEEP", "G-SWEEP-IS-EXECUTION-BOUND",
     "publishes a forged survivor row in the sweep ledger", 'pick("MUT-SWEEP"'),
    ("MUT-GATECOUNT", "G-GATE-ACCOUNTING",
     "reports zero closing gates after the ledger snapshot, so the published "
     "total stops being the sum of its parts", 'pick("MUT-GATECOUNT"'),
    ("MUT-IMAGE-SWAP", "G-BOTH-INDUCED-IMAGES-CENSUSED",
     "exchanges the two induced images' labels, so each image's census is "
     "published under the other image's name",
     'img_rows[0]["induced_image"], img_rows[1]["induced_image"]'),
    ("MUT-IMAGE-STAMP", "G-BOTH-INDUCED-IMAGES-CENSUSED",
     "stamps the induced-image fiber INERT while the two censuses differ, "
     "which is the disclosure the fiber exists to make",
     'pick("MUT-IMAGE-STAMP"'),
    ("MUT-LEG4-BY-GRAIN", "G-WHICH-LEG-BINDS-BY-GRAIN",
     "declares the leg-binding answer NOT to be stratified by grain while "
     "the two grains' binding sets differ", 'pick("MUT-LEG4-BY-GRAIN"'),
    ("MUT-THESIS", "G-THESIS-IS-ONE-DIRECTIONAL",
     "declares the thesis condition not necessary at both grains, which is "
     "the only direction the head asserts", 'pick("MUT-THESIS"'),
    ("MUT-MULTISET", "G-THE-CORPUS-IS-A-MULTISET",
     "declares the per-corpus slot counts not to sum to the corpus total, so "
     "the multiplicity table stops accounting for the corpus",
     'pick("MUT-MULTISET"'),
    ("MUT-FREE-PRODUCT", "G-THE-LADDER-AND-THE-ARROW-GROUPOID-ARE-TWO-"
     "OBJECTS",
     "reports one history at which the empty coherence relation does not "
     "return the free product of the full footprint symmetric groups, which "
     "is what identifies the object the ladder counts",
     'pick("MUT-FREE-PRODUCT"'),
    ("MUT-THREE-PREDICATES", "G-ATOM-THEOREM-AT-THE-GROUPOID-GRAIN",
     "declares the three coinciding predicates -- actor-grain non-uniqueness, "
     "nontrivial stabilizer, no atom break -- not to coincide",
     'pick("MUT-THREE-PREDICATES"'),
    ("MUT-R6-FORCED", "G-TRANSPORT-ALONG-THE-R-LADDER",
     "declares the R = 6 rung not forced by the R = 3 rung, so the "
     "theorem-forced stamp and the measurement part company",
     'pick("MUT-R6-FORCED"'),
    ("MUT-CANON-NUMERALS", "G-CANONIZATION-PRESERVES-NUMERALS",
     "routes the numeral-bearing normaliser back through the markdown "
     "stripper that eats a line-initial numeral, which is how a false ratio "
     "went unscanned", 'canon_numeric(canon_src, mut("MUT-CANON-NUMERALS"))'),
    ("MUT-E24-ROW", "G-E24-COUNTING-ONLY",
     "stamps ONE ratio row as a probability while the top-level stamp stays "
     "COUNTING-ONLY", 'R["measure_relativity"]["rows"][0]["stamp"] = '
     '"PROBABILITY"'),
    ("MUT-POST-SEAL-KEY", "G-SEAL-TOTALITY",
     "forges a top-level receipt key AFTER the seal manifest is assembled, "
     "in the window the delivered ordering left open",
     'R["a_key_forged_after_the_seal_manifest"]'),
    ("MUT-TABLE-SURPLUS", "G-PAPER-TABLES-WITH-HEADERS",
     "drops one rendered table row, so the paper carries a table row no "
     "route rendered -- the additive direction containment cannot see",
     'rendered = rendered[:-1]'),
    ("MUT-FENCE-SURPLUS", "G-PAPER-NUMERAL-COVERAGE",
     "appends a fourth fenced block to the paper text the fence multiset is "
     "taken over", 'text = text + "\\n```\\nA FOURTH FENCE'),
    ("MUT-GATELINE", "G-TRANSCRIPT-MATCHES-THE-GATE-LEDGER",
     "appends a forged PASS line for a gate that never ran to the transcript "
     "before it is staged and digested",
     'LINES.append("  [PASS] G-FORGED-BY-THE-FALSIFIER")'),
    ("MUT-NAMED-GATE", "G-NAMED-GATES-EXIST",
     "renames every verbatim anchor's consumer gate to a gate that does not "
     "exist", 'pick("MUT-NAMED-GATE"'),
    ("MUT-SPELLED-COMPOUND", "G-PAPER-NUMERAL-COVERAGE",
     "plants a spelled COMPOUND numeral built entirely from backed atoms, "
     "which a per-word scan cannot see", 'if mut("MUT-SPELLED-COMPOUND")'),
    ("MUT-POLARITY-ABSENT", "G-PAPER-CLAIM-POLARITY",
     "removes the asserted form of the head-word axis, so the axis passes on "
     "a silence instead of on an assertion",
     'if mut("MUT-POLARITY-ABSENT") and nm'),
    ("MUT-REFERENT-TOTALITY", "G-SENTENCE-REFERENT-BINDING",
     "deletes one published relation from the body the referent scan reads, "
     "so a relation the scanner never saw would pass as one that bound",
     'body = RATIO_PAT.sub(" ", body, count=1)'),
]
MUTANT_NAMES = [m[0] for m in MUTANTS]

CLOSING_GATE_NAMES = (
    "G-WALLS-SCAN-THE-PAPER", "G-PAPER-CLAIMS",
    "G-PAPER-TABLES-WITH-HEADERS", "G-PAPER-NUMERAL-COVERAGE",
    "G-CANONIZATION-PRESERVES-NUMERALS", "G-SENTENCE-REFERENT-BINDING",
    "G-PAPER-CLAIM-POLARITY",
    "G-NO-TYPED-COUNTS", "G-NO-FLOATS", "G-READS-DECLARED",
    "G-FALSIFIER-COVERAGE", "G-FALSIFIER-REACHABILITY",
    "G-PAPER-INSTRUMENT-RAN-IN-THE-PLAIN-RUN", "G-SWEEP-IS-EXECUTION-BOUND",
    "G-TRANSCRIPT-SEALED-WHOLE", "G-TRANSCRIPT-MATCHES-THE-GATE-LEDGER",
    "G-GATE-ACCOUNTING", "G-NAMED-GATES-EXIST", "G-SEAL-TOTALITY",
    "G-ARTIFACT-INTEGRITY")


def closing_battery(R, paper_text, paper_rel, write):
    say()
    say("SECTION 11.  THE PAPER INSTRUMENT AND THE CLOSING BATTERY")
    src = read_text(SELF, "SELF")
    ppath = os.path.join(REPO, paper_rel)
    disk_paper = (read_text(ppath, "PAPER-UNDER-TEST")
                  if os.path.exists(ppath) else "")
    if paper_text is None:
        paper_text = disk_paper

    planted = "\n".join(n for (_w, needles, _y) in WALLS for n in needles)
    scan_text = pick("MUT-WALL-PLANT", paper_text,
                     paper_text + "\n\n" + planted)
    wrows = []
    for (wname, needles, why) in WALLS:
        hits = [n for n in needles if canon(n) in canon(scan_text)]
        wrows.append({"wall": wname, "needles": len(needles),
                      "hits": hits, "clean": not hits, "warrant": why})
    R["walls"] = {"rows": wrows, "scanned_chars": len(scan_text),
                  "leg": "THE PAPER'S OWN BYTES",
                  "warrant": "each wall scans the object under test, not the "
                             "instrument's surface (#269's caveat); the "
                             "MUT-WALL-PLANT falsifier plants every banned "
                             "sentence into exactly this text"}
    LD.gate("G-WALLS-SCAN-THE-PAPER",
            "THE WALLS SCAN THE PAPER, WHICH IS THE LEG THEY ARE OWED.  %d "
            "walls carrying %d banned assertive sentences between them are "
            "matched against %s characters of the paper under test after "
            "full normalisation; the not-licensed list of the AID "
            "adjudication is the source of the first three.  The falsifier "
            "for this gate plants every banned sentence into the same text, "
            "so a green sweep here is evidence about the paper and not about "
            "the scanner"
            % (len(WALLS), sum(len(n) for (_w, n, _y) in WALLS),
               com(len(scan_text))),
            all(w["clean"] for w in wrows),
            "walls %d, clean %d, hits %s"
            % (len(wrows), sum(1 for w in wrows if w["clean"]),
               [h for w in wrows for h in w["hits"]] or "none"))
    SEAL.take("SEAL-WALLS", R)

    R["paper_claims"] = paper_claims(R)
    R["paper_tables"] = paper_tables(R)
    texts_for_claims = [c["sentence"] for c in R["paper_claims"]]
    if mut("MUT-PAPER-CLAIM"):
        texts_for_claims = texts_for_claims[:-1]
    body = canon(paper_text)
    missing = [c["id"] for c, s in zip(R["paper_claims"], texts_for_claims
                                       + [""] * len(R["paper_claims"]))
               if s and canon(s) not in body]
    absent_required = len(R["paper_claims"]) - len(texts_for_claims)
    LD.gate("G-PAPER-CLAIMS",
            "EVERY REQUIRED CLAIM SENTENCE IS RENDERED FROM THE RECEIPT AND "
            "FOUND IN THE PAPER, AS AN EQUALITY (#293 Z10).  %d sentences "
            "are built from the run's own numbers and matched against the "
            "paper's bytes; the count required and the count matched are "
            "compared by EQUALITY, so dropping a sentence fails here rather "
            "than reducing a denominator" % len(R["paper_claims"]),
            not missing and absent_required == 0,
            "required %d, matched %d, missing %s, dropped %d"
            % (len(R["paper_claims"]),
               len(R["paper_claims"]) - len(missing), missing or "none",
               absent_required))
    SEAL.take("SEAL-PAPER-CLAIMS", R)

    prows = markdown_table_rows(paper_text)
    pset = [tuple(c) for c in prows]
    tmiss, rendered = [], []
    for tname in sorted(R["paper_tables"]):
        t = R["paper_tables"][tname]
        hdr = [canon(h) for h in t["header"]]
        if mut("MUT-PAPER-TABLE") and tname == "T2-THE-CENSUS":
            hdr[1], hdr[2] = hdr[2], hdr[1]
        rendered.append(tuple(hdr))
        if tuple(hdr) not in pset:
            tmiss.append(tname + "/HEADER")
        for row in t["rows"]:
            rendered.append(tuple(canon(c) for c in row))
            if tuple(canon(c) for c in row) not in pset:
                tmiss.append(tname + "/" + canon(row[0]))
    if mut("MUT-TABLE-SURPLUS"):
        rendered = rendered[:-1]
    # TWO-DIRECTIONAL (K3 MAJOR-5).  Containment alone lets a FORGED row ride
    # in beside the true ones -- a duplicate census table with its headers
    # exchanged, or an extra control row asserting the word the control arm
    # exists to exclude.  The two multisets are therefore required to be
    # EQUAL: every rendered row appears in the paper, and every table row of
    # the paper is rendered, with multiplicity.
    surplus = sorted(set(Counter(pset) - Counter(rendered)))
    tables_bijective = Counter(pset) == Counter(rendered)
    R["paper_table_binding"] = {
        "rendered_rows": len(rendered), "paper_rows": len(pset),
        "missing_from_the_paper": tmiss,
        "surplus_in_the_paper": [list(r) for r in surplus],
        "bijective": tables_bijective}
    LD.gate("G-PAPER-TABLES-WITH-HEADERS",
            "EVERY TABLE IS RENDERED FROM THE RECEIPT, HEADERS INCLUDED, AND "
            "THE BINDING RUNS BOTH WAYS (PER-R Z7 + K3 MAJOR-5).  %d tables "
            "with %d data rows and %d header rows are built here; each is "
            "required to appear in the paper cell by cell, and the MULTISET "
            "of the paper's own markdown table rows is required to equal the "
            "multiset rendered -- %d against %d.  A column header is a claim, "
            "so a header swap that leaves every number correct dies here; and "
            "so does a forged surplus row, a restated table with its headers "
            "exchanged, and a duplicated row, none of which containment alone "
            "can see"
            % (len(R["paper_tables"]),
               sum(len(t["rows"]) for t in R["paper_tables"].values()),
               len(R["paper_tables"]), len(pset), len(rendered)),
            not tmiss and tables_bijective,
            "tables %d, rendered rows %d, paper rows %d, missing %s, surplus "
            "%s"
            % (len(R["paper_tables"]), len(rendered), len(pset),
               tmiss[:6] or "none",
               [list(r)[:2] for r in surplus[:4]] or "none"))
    SEAL.take("SEAL-PAPER-TABLES", R)
    SEAL.take("SEAL-TABLE-BINDING", R)

    R["paper_coverage"] = paper_coverage(R, paper_text)
    pc = R["paper_coverage"]
    LD.gate("G-PAPER-NUMERAL-COVERAGE",
            "EVERY NUMERAL OF THE PAPER IS BACKED BY THIS RUN (#20 + E-22).  "
            "%s numerals are scanned -- prose, tables, inline code spans and "
            "the fenced verdict blocks alike -- against the run's registry "
            "and its own receipt, with %d declared exemptions; %s spelled "
            "numerals are scanned on the same terms; the scan's own totality "
            "is checked by arithmetic against the whole paper, and the "
            "verdict fences are gated by MULTISET equality so a forged twin "
            "beside a clean copy cannot pass"
            % (com(pc["numerals_scanned"]), pc["exemptions_declared"],
               com(pc["spelled_numerals_scanned"])),
            not pc["unbacked"] and not pc["spelled_unbacked"]
            and pc["scan_is_total"] and pc["fence_multiset_equal"]
            and not pc["exemptions_fired"]
            and not pc["exemptions_that_never_fired"],
            "scanned %d of %d, unbacked %s, spelled %d unbacked %s, fences "
            "%s" % (pc["numerals_scanned"], pc["numerals_in_the_whole_paper"],
                    pc["unbacked"][:8] or "none",
                    pc["spelled_numerals_scanned"],
                    pc["spelled_unbacked"][:8] or "none",
                    pc["fence_multiset_equal"]))
    SEAL.take("SEAL-PAPER-COVERAGE", R)

    probe = ("the two tests agree at the carrier grain at 0 of\n"
             "%d. This declared fixture is a wrapped sentence whose "
             "continuation line begins with a numeral and a period, which is "
             "not a list.\n" % R["grain_triangle"]["sub_window"])
    canon_src = paper_text + "\n" + probe
    canon_ref = Counter(NUMTOK.findall(numeral_reference_body(canon_src)))
    canon_got = Counter(NUMTOK.findall(
        canon_numeric(canon_src, mut("MUT-CANON-NUMERALS"))))
    R["canonization"] = {
        "numerals_in_the_reference_body": sum(canon_ref.values()),
        "numerals_after_canonization": sum(canon_got.values()),
        "multisets_equal": canon_ref == canon_got,
        "lost": sorted((canon_ref - canon_got).elements()),
        "gained": sorted((canon_got - canon_ref).elements()),
        "probe": "a declared fixture carrying the pathology itself: a "
                 "wrapped sentence whose continuation line begins with a "
                 "numeral and a period.  A markdown normaliser that treats "
                 "that as an ordered-list marker eats the numeral, and the "
                 "ratio it belonged to is then never scanned at all",
    }
    LD.gate("G-CANONIZATION-PRESERVES-NUMERALS",
            "THE NORMALISER THAT FEEDS THE NUMERAL SCANS LOSES NO NUMERAL "
            "(K3 MAJOR-2b).  The paper, with a declared fixture appended that "
            "carries the pathology itself, is normalised twice: once with "
            "nothing removed but unicode and whitespace, and once through the "
            "normaliser the ratio scan actually uses.  The two numeral "
            "MULTISETS are required to be equal -- %d against %d -- so a "
            "normaliser that swallows a line-initial numeral fails by "
            "arithmetic here instead of hiding a ratio downstream"
            % (sum(canon_ref.values()), sum(canon_got.values())),
            canon_ref == canon_got,
            "reference %d, after canonization %d, lost %s, gained %s"
            % (sum(canon_ref.values()), sum(canon_got.values()),
               sorted((canon_ref - canon_got).elements())[:6] or "none",
               sorted((canon_got - canon_ref).elements())[:6] or "none"))

    R["referent_binding"] = referent_binding(R, paper_text)
    rb = R["referent_binding"]
    LD.gate("G-SENTENCE-REFERENT-BINDING",
            "NO SENTENCE PAIRS NUMERALS FROM DIFFERENT QUANTITY AXES (#293 "
            "Z6), AND THE SCAN'S OWN TOTALITY IS CHECKED.  %d published "
            "relations of the forms `N of M` and `N against M` are resolved "
            "against the receipt and both members are required to be carried "
            "by one common member of the %d DECLARED QUANTITY AXES -- an "
            "axis is a list of receipt paths whose values count the same kind "
            "of thing, because a top-level key that carries two kinds binds "
            "a false relation between them.  The aggregate keys are excluded "
            "by declaration, since a universe that carries every number binds "
            "nothing.  The number of relations the scan SAW is compared with "
            "the number the paper's own bytes carry (%d against %d), so a "
            "relation the scanner missed is a failure and not a silent pass, "
            "and every declared axis path is required to resolve.  The LOR "
            "disease -- every numeral true, the relation false -- dies here"
            % (rb["relations_checked"], len(REFERENT_AXES),
               rb["relations_found_in_the_scanned_body"],
               rb["relations_in_the_paper"]),
            not rb["unbound"] and rb["relations_checked"] > 0
            and rb["scan_is_total"]
            and not rb["axis_paths_that_resolved_to_nothing"],
            "checked %d, found %d, in the paper %d, unbound %s, empty axis "
            "paths %s"
            % (rb["relations_checked"],
               rb["relations_found_in_the_scanned_body"],
               rb["relations_in_the_paper"], rb["unbound"][:6] or "none",
               rb["axis_paths_that_resolved_to_nothing"][:4] or "none"))
    SEAL.take("SEAL-REFERENT", R)
    SEAL.take("SEAL-CANON", R)

    R["polarity"] = paper_polarity(R, paper_text, mut("MUT-POLARITY"))
    LD.gate("G-PAPER-CLAIM-POLARITY",
            "THE PAPER IS SCANNED FOR THE INVERSE OF EVERY LOAD-BEARING "
            "WORD, IN BOTH DIRECTIONS AND AT A DECLARED SCOPE.  %d polarity "
            "axes -- the head word, the atom word in the verdict AND in the "
            "prose that claims it, the thesis direction, the control arm's "
            "forced word, the induced-image fiber, the transport direction, "
            "the binding direction and the E-24 stamp -- are checked in BOTH "
            "forms.  The presence of an inverted form is a failure even when "
            "the asserted form is present too, and the ABSENCE of an "
            "asserted form is a failure too, so an inversion that deletes "
            "the original cannot pass as a silence.  %d axes are scanned "
            "over the paper's prose alone, where the opposite word is "
            "legitimate data inside a table"
            % (len(POLARITY),
               sum(1 for p in POLARITY if p[1] == "PROSE")),
            R["polarity"]["inverted_forms_present"] == 0
            and R["polarity"]["asserted_forms_absent"] == 0,
            "axes %d, inverted present %d, asserted absent %d"
            % (len(POLARITY), R["polarity"]["inverted_forms_present"],
               R["polarity"]["asserted_forms_absent"]))
    SEAL.take("SEAL-POLARITY", R)

    naming = ("paper_claims", "paper_tables", "verdict_segments",
              "independent_head", "head_slot")
    typed = template_constants(src, naming)
    LD.gate("G-NO-TYPED-COUNTS",
            "NO COUNT IS TYPED IN THE NAMING CODE (#267 MAJOR-3).  The "
            "string constants of the %d functions that build this unit's "
            "prose, tables and head are read out of this file by AST and "
            "scanned for numerals; only the arena's own small constants are "
            "allowed, and every published total is derived from a live "
            "registry" % len(naming),
            not typed, "offending literals %s" % (typed[:8] or "none"))

    # THE TWO SCANS ARE COUNTED APART.  A single accumulator would let the
    # rendered `arithmetic` line report one scan's total as the other's --
    # which is the very shape K3 MAJOR-4 named, a published claim that can
    # assert one thing while the scan measures another.
    src_floats = []
    for node in ast.walk(ast.parse(src)):
        if isinstance(node, ast.Constant) and isinstance(node.value, float):
            src_floats.append(node.lineno)
    receipt_floats = []

    def scan(o, path=""):
        if isinstance(o, float):
            receipt_floats.append(path)
        elif isinstance(o, dict):
            for k in sorted(o, key=str):
                scan(o[k], path + "/" + str(k))
        elif isinstance(o, (list, tuple)):
            for i, v in enumerate(o):
                scan(v, path + "/%d" % i)
    scan(R)
    floats = src_floats + receipt_floats
    # the `arithmetic` line is RENDERED FROM THE SCAN and sealed here, so it
    # is a measurement rather than an unchecked published claim (K3 MAJOR-4).
    R["arithmetic"] = ("exact integers and Z[w] pairs; %d float constants in "
                       "this file's source and %d float values in this "
                       "receipt, each counted by its own leg of the scan this "
                       "gate raises"
                       % (len(src_floats), len(receipt_floats)))
    LD.gate("G-NO-FLOATS",
            "THE ARITHMETIC IS EXACT, CHECKED TWICE, AND THE RECEIPT'S OWN "
            "ARITHMETIC LINE IS RENDERED FROM THE CHECK.  This file's own "
            "source is walked by AST for float constants and the receipt "
            "about to be written is walked recursively for float values; the "
            "Z[w] coefficients of the coupled step are integer pairs and the "
            "lumpability comparison is an exact comparison of integer maps.  "
            "The `arithmetic` key is written from this scan's result and "
            "sealed, so it cannot assert one thing while the scan measures "
            "another",
            not floats, "float sites %s" % (floats[:6] or "none"))
    SEAL.take("SEAL-ARITHMETIC", R)

    cats = {k: sorted(v) for k, v in sorted(READS_BY_CATEGORY.items())}
    want_sources = {os.path.abspath(os.path.join(REPO, s[1]))
                    for s in SOURCES}
    got_sources = set(cats.get("SOURCE", []))
    LD.gate("G-READS-DECLARED",
            "THE RUN'S READS ARE EXACTLY THE DECLARED ONES (#91).  Every "
            "read in this file passes through one of two categorised "
            "readers; the SOURCE set is compared with the declaration as a "
            "SET OF ABSOLUTE PATHS, the paper under test is the only "
            "PAPER-UNDER-TEST read, and this file itself is the only SELF "
            "read.  No subprocess is invoked anywhere",
            got_sources == want_sources
            and len(cats.get("PAPER-UNDER-TEST", [])) <= 1
            and len(cats.get("SELF", [])) == 1,
            "sources %d declared %d, extra %s, missing %s"
            % (len(got_sources), len(want_sources),
               sorted(got_sources - want_sources) or "none",
               sorted(want_sources - got_sources) or "none"))

    hooks = mutant_hooks(src)
    gates_seen = {g["gate"] for g in LD.rows} | set(CLOSING_GATE_NAMES)
    cov, bad_desc = [], []
    for (name, gate_name, why, frag) in MUTANTS:
        hs = hooks.get(name, [])
        srcs = " ".join(h["source"] for h in hs)
        ok = bool(hs) and norm_src(frag) in norm_src(srcs)
        if not ok:
            bad_desc.append(name)
        cov.append({"mutant": name, "gate": gate_name, "description": why,
                    "declared_fragment": frag, "hooks": len(hs),
                    "fragment_found_in_the_hook_source": ok,
                    "gate_exists": gate_name in gates_seen,
                    "constant_boolean": any(h["constant_boolean"]
                                            for h in hs)})
    R["coverage"] = {"mutants": len(MUTANTS), "hooked": sum(
        1 for c in cov if c["hooks"]), "rows": cov,
        "gates_named_that_do_not_exist": [c["mutant"] for c in cov
                                          if not c["gate_exists"]],
        "descriptions_not_matching_their_code": bad_desc}
    R["waiver_ledger"] = [{"gate": r["gate"], "waiver": r["waiver"]}
                          for r in LD.rows if r["waiver"]]
    R["mutants"] = [{"mutant": m[0], "gate": m[1], "description": m[2]}
                    for m in MUTANTS]
    LD.gate("G-FALSIFIER-COVERAGE",
            "EVERY FALSIFIER'S DESCRIPTION IS VERIFIED AGAINST ITS CODE "
            "(E-23).  %d falsifiers are declared; each names the gate it "
            "must die at, and each carries a source fragment that is located "
            "in this file by AST and matched against the statement that "
            "actually carries the hook.  A description-inverted falsifier -- "
            "a false waiver wearing a green badge -- fails here, and every "
            "gate named is required to exist" % len(MUTANTS),
            not bad_desc and not R["coverage"]
            ["gates_named_that_do_not_exist"],
            "falsifiers %d, hooked %d, description mismatches %s, missing "
            "gates %s" % (len(MUTANTS), R["coverage"]["hooked"],
                          bad_desc or "none",
                          R["coverage"]["gates_named_that_do_not_exist"]
                          or "none"))
    covered = sorted({m[1] for m in MUTANTS})
    R["reachability"] = {
        "gates_total_named_by_falsifiers": len(covered),
        "gates_with_a_falsifier": covered,
        "gates_without_a_falsifier": sorted(
            g for g in gates_seen if g not in set(covered)),
        "rule": "#34: every falsifier must REACH its gate, and every gate "
                "without one is named rather than left implicit",
    }
    LD.gate("G-FALSIFIER-REACHABILITY",
            "THE GATES WITHOUT A FALSIFIER ARE NAMED, NOT HIDDEN (#34).  %d "
            "of the gates this run raises carry a named falsifier; the "
            "remaining %d are listed in the receipt by name so a reader can "
            "see exactly which surfaces are guarded by construction and "
            "which by argument"
            % (len(covered), len(R["reachability"]
                                 ["gates_without_a_falsifier"])),
            len(covered) > 0 and all(g in gates_seen for g in covered),
            "with falsifier %d, without %d"
            % (len(covered),
               len(R["reachability"]["gates_without_a_falsifier"])))
    SEAL.take("SEAL-COVERAGE", R)
    return paper_text


def finish(R, write=True, swept=False):
    """THE TRANSCRIPT, THE SEAL MANIFEST AND THE WRITE (#119 + #148), with
    the READ-BACK TAKEN BEFORE os.replace -- the AID adjudication's Z12: an
    integrity check performed after promotion has already promoted."""
    R["closing_gates"] = {
        "names": list(CLOSING_GATE_NAMES),
        "warrant": "the transcript is sealed WHOLE, the manifest is total, "
                   "the paper instrument runs inside the plain run, and the "
                   "staged bytes are read back and compared with the "
                   "gate-time seal BEFORE anything is promoted",
    }
    R["mutant_sweep"] = {"swept": swept, "mutants": len(MUTANTS),
                         "rows": list(SWEEP_ROWS),
                         "survivors": [r["mutant"] for r in SWEEP_ROWS
                                       if not r["died_at"]
                                       or not r["artifacts_unchanged"]]}
    LD.gate("G-PAPER-INSTRUMENT-RAN-IN-THE-PLAIN-RUN",
            "THE PAPER INSTRUMENT RAN INSIDE THIS RUN (#20).  The coverage, "
            "polarity, claim, table and referent ledgers above were produced "
            "by the plain run and are sealed here, so no separate "
            "verification pass can drift from the artifacts this run writes: "
            "%s numerals, %d claims and %d table rows"
            % (com(R["paper_coverage"]["numerals_scanned"]),
               len(R["paper_claims"]),
               sum(len(t["rows"]) for t in R["paper_tables"].values())),
            pick("MUT-FINAL", R["paper_coverage"]["numerals_scanned"], 0) > 0
            and len(R["paper_claims"]) > 0,
            "numerals %d, claims %d, rows %d"
            % (R["paper_coverage"]["numerals_scanned"],
               len(R["paper_claims"]),
               sum(len(t["rows"]) for t in R["paper_tables"].values())))
    SEAL.take("SEAL-MUTANTS", R)
    SEAL.take("SEAL-WAIVERS", R)
    SEAL.take("SEAL-REACHABILITY", R)
    LD.gate("G-SWEEP-IS-EXECUTION-BOUND",
            "THE FALSIFIER SWEEP IS A RECORD OF RUNS, NOT A LIST (E-23).  %d "
            "falsifiers are declared, %d were executed in this process and "
            "%d survived; a plain run publishes an empty execution list "
            "rather than a claim, and the sweep run publishes the rows it "
            "actually produced"
            % (len(MUTANTS), len(SWEEP_ROWS),
               len(R["mutant_sweep"]["survivors"])),
            not pick("MUT-SWEEP", R["mutant_sweep"]["survivors"], ["FORGED"])
            and len(SWEEP_ROWS) in (0, len(MUTANTS)),
            "declared %d, executed %d, survivors %s"
            % (len(MUTANTS), len(SWEEP_ROWS),
               R["mutant_sweep"]["survivors"] or "none"))
    SEAL.take("SEAL-MUTANT-SWEEP", R)
    if mut("MUT-GATELINE"):
        LINES.append("  [PASS] G-FORGED-BY-THE-FALSIFIER")
    R["gates"] = [dict(r) for r in LD.rows]
    snap = {r["gate"] for r in R["gates"]}
    after = [g for g in CLOSING_GATE_NAMES if g not in snap]
    R["totals"] = {
        "sources": len(SOURCES),
        "verbatim_anchors": len(VERBATIM),
        "windows": len(WINDOW_DECL),
        "walls": len(WALLS),
        "wall_needles": sum(len(n) for (_w, n, _y) in WALLS),
        "falsifiers": len(MUTANTS),
        "seals": len(SEALED_PATHS),
        "criterion_legs": len(R["criterion"]["legs"]),
        "coherence_rows": len(COHERENCE_ROWS),
        "grains": len(GRAIN_ROWS),
        "tests": len(TEST_ROWS),
        "paper_claims": len(R["paper_claims"]),
        "paper_tables": len(R["paper_tables"]),
        "paper_table_rows": sum(len(t["rows"])
                                for t in R["paper_tables"].values()),
        "gates_in_the_sealed_ledger": len(R["gates"]),
        "gates_after_the_ledger_snapshot": len(after),
        "gates_total": len(R["gates"]) + len(after),
        "numerals_registered": len(NUMREG),
    }
    R["closing_gates"]["after_the_snapshot"] = after
    SEAL.take("SEAL-GATES", R)
    SEAL.take("SEAL-CLOSING", R)
    SEAL.take("SEAL-TOTALS", R)
    staged = list(LINES)
    if mut("MUT-TRANSCRIPT"):
        staged = staged[:-1] + [staged[-1] + " forged"]
    said = Counter(GATELINE.findall("\n".join(staged)))
    ledger = Counter(g["gate"] for g in R["gates"])
    R["transcript_head"] = {
        "lines": len(LINES),
        "first": LINES[0] if LINES else "",
        "last": LINES[-1] if LINES else "",
        "whole_transcript_sha256_12": digest("\n".join(LINES)),
        "staged_transcript_sha256_12": digest("\n".join(staged)),
        "sealed": "the WHOLE transcript, not a head prefix",
        "gate_lines_in_the_transcript": sum(said.values()),
        "gates_in_the_sealed_ledger": sum(ledger.values()),
        "gate_lines_not_in_the_ledger": sorted((said - ledger).elements()),
        "ledger_gates_without_a_line": sorted((ledger - said).elements()),
        "reconciled": said == ledger,
    }
    SEAL.take("SEAL-TRANSCRIPT", R)
    LD.gate("G-TRANSCRIPT-SEALED-WHOLE",
            "THE TRANSCRIPT IS SEALED WHOLE, NOT AT ITS HEAD (#267 MAJOR-5).  "
            "The digest published is taken over ALL %s transcript lines this "
            "run emitted, and the STAGED lines -- the bytes that will reach "
            "disk -- are digested separately and required to be identical; "
            "no whitelist, no indentation class, no substring acceptance"
            % com(len(LINES)),
            R["transcript_head"]["whole_transcript_sha256_12"]
            == R["transcript_head"]["staged_transcript_sha256_12"],
            "lines %d, whole %s, staged %s"
            % (len(LINES), R["transcript_head"]["whole_transcript_sha256_12"],
               R["transcript_head"]["staged_transcript_sha256_12"]))
    LD.gate("G-TRANSCRIPT-MATCHES-THE-GATE-LEDGER",
            "THE TRANSCRIPT'S GATE LINES ARE THE SEALED LEDGER'S GATES (K3 "
            "m1).  Sealing the transcript whole proves the bytes were not "
            "changed after the digest; it does not prove they SAY what the "
            "receipt says.  Every `[PASS]` or `[FAIL]` line of the staged "
            "transcript is parsed for its gate name and the resulting "
            "multiset is required to equal the multiset of gate names in the "
            "sealed ledger -- %d lines against %d rows -- so a forged PASS "
            "line for a gate that never ran, or a real gate's line quietly "
            "removed, fails here"
            % (sum(said.values()), sum(ledger.values())),
            said == ledger,
            "transcript gate lines %d, ledger gates %d, lines with no ledger "
            "row %s, ledger rows with no line %s"
            % (sum(said.values()), sum(ledger.values()),
               sorted((said - ledger).elements())[:4] or "none",
               sorted((ledger - said).elements())[:4] or "none"))
    LD.gate("G-GATE-ACCOUNTING",
            "THE GATE COUNT IS ONE NUMBER WITH ONE DEFINITION (#267 "
            "MAJOR-3).  The ledger is sealed at a snapshot, so the published "
            "total is the snapshot's %d rows plus the %d declared closing "
            "gates that necessarily run after it -- %d in all -- and every "
            "count this unit publishes is the length of a live registry"
            % (R["totals"]["gates_in_the_sealed_ledger"],
               R["totals"]["gates_after_the_ledger_snapshot"],
               R["totals"]["gates_total"]),
            R["totals"]["gates_total"]
            == R["totals"]["gates_in_the_sealed_ledger"]
            + R["totals"]["gates_after_the_ledger_snapshot"]
            and pick("MUT-GATECOUNT",
                     R["totals"]["gates_after_the_ledger_snapshot"], 0) > 0,
            "sealed %d, after %d, total %d"
            % (R["totals"]["gates_in_the_sealed_ledger"],
               R["totals"]["gates_after_the_ledger_snapshot"],
               R["totals"]["gates_total"]))
    ran = {g["gate"] for g in LD.rows} | set(CLOSING_GATE_NAMES)
    phantom_anchor = [v["id"] for v in R["verbatim_anchors"]
                      if pick("MUT-NAMED-GATE", v["consumer_gate"],
                              "G-NO-SUCH-GATE-EXISTS-ANYWHERE") not in ran]
    phantom_seal = [r["seal"] for r in SEAL.rows
                    if r["sealed_at_gate"] not in ran]
    phantom_mutant = [c["mutant"] for c in R["coverage"]["rows"]
                      if not c["gate_exists"]]
    R["named_gates"] = {
        "gates_that_ran_or_are_declared_closing": len(ran),
        "anchors_naming_a_gate_that_does_not_exist": phantom_anchor,
        "seals_naming_a_gate_that_does_not_exist": phantom_seal,
        "falsifiers_naming_a_gate_that_does_not_exist": phantom_mutant,
        "rule": "every gate NAMED anywhere in this receipt -- by a verbatim "
                "anchor as its consumer, by a seal as the gate that "
                "established it, or by a falsifier as the gate it must die "
                "at -- is required to EXIST.  Non-emptiness is not "
                "existence: a phantom consumer passed the delivered check",
    }
    LD.gate("G-NAMED-GATES-EXIST",
            "EVERY GATE NAMED IN THIS RECEIPT EXISTS (K3 m2).  The %d "
            "verbatim anchors name the gate that consumes them, the %d seals "
            "name the gate that established them and the %d falsifiers name "
            "the gate they must die at; each of those %d names is looked up "
            "in the set of gates this run actually raised together with the "
            "declared closing gates.  A name that is merely non-empty is not "
            "a consumer, and a phantom consumer rode the delivered check"
            % (len(R["verbatim_anchors"]), len(SEAL.rows), len(MUTANTS),
               len(R["verbatim_anchors"]) + len(SEAL.rows) + len(MUTANTS)),
            not phantom_anchor and not phantom_seal and not phantom_mutant,
            "phantom anchor consumers %s, phantom seal gates %s, phantom "
            "falsifier gates %s"
            % (phantom_anchor or "none", phantom_seal or "none",
               phantom_mutant or "none"))
    SEAL.take("SEAL-NAMED-GATES", R)
    R["seal_manifest"] = SEAL.rows
    payload = json.dumps(R, indent=1, sort_keys=True, default=str)
    SEAL.close(R, payload)
    R["payload_sha256_12"] = SEAL.payload_sha
    if mut("MUT-POST-SEAL-KEY"):
        R["a_key_forged_after_the_seal_manifest"] = {"forged": True}
    payload = json.dumps(R, indent=1, sort_keys=True, default=str)
    # THE INTEGRITY GATES RUN LAST AND TOTAL (K3 MAJOR-4).  The delivered
    # order computed the published-key set from R several statements before
    # serialization, leaving a window in which a forged top-level key was
    # published, sealed by nothing and named by nothing.  The set is now taken
    # from the SERIALIZED PAYLOAD -- the object that actually reaches disk --
    # so the window is closed by construction rather than by discipline.
    missing, extra = SEAL.totality()
    published = sorted(k for k in json.loads(payload)
                       if k not in DECLARED_UNSEALED)
    sealed_paths = {r["path"] for r in SEAL.rows}
    unsealed = sorted(k for k in published if k not in sealed_paths)
    closing_absent = [g for g in CLOSING_GATE_NAMES
                      if g not in {g2["gate"] for g2 in LD.rows} and g not in
                      ("G-ARTIFACT-INTEGRITY", "G-SEAL-TOTALITY")]
    LD.gate("G-SEAL-TOTALITY",
            "THE SEAL MANIFEST IS TOTAL, AND TOTAL OVER THE BYTES THAT REACH "
            "DISK (#119 + #148 + K3 MAJOR-4).  The published-key set is read "
            "back out of the SERIALIZED PAYLOAD rather than out of the "
            "in-memory object several statements earlier, so a key inserted "
            "after the manifest was assembled is caught rather than "
            "published unsealed: %d seals over %d published keys, %d declared "
            "unsealed, %d missing and %d unaccounted; and every one of the %d "
            "declared closing gates ran"
            % (len(SEAL.rows), len(published), len(DECLARED_UNSEALED),
               len(missing), len(unsealed), len(CLOSING_GATE_NAMES)),
            not missing and not extra and not unsealed and not closing_absent,
            "seals %d, missing %s, extra %s, unsealed keys %s, closing gates "
            "that did not run %s"
            % (len(SEAL.rows), missing or "none", extra or "none",
               unsealed or "none", closing_absent or "none"))
    text = "\n".join(staged) + "\n"
    seal_j = hashlib.sha256(payload.encode("utf-8")).hexdigest()[:12]
    seal_t = hashlib.sha256(text.encode("utf-8")).hexdigest()[:12]
    if not write:
        return R, payload, text, seal_j, seal_t
    tmp_j, tmp_t = OUT_JSON + ".tmp", OUT_TXT + ".tmp"
    with open(tmp_j, "w", encoding="utf-8") as fh:
        fh.write(payload)
    with open(tmp_t, "w", encoding="utf-8") as fh:
        fh.write(text)
    with open(tmp_j, "rb") as fh:
        dj = hashlib.sha256(fh.read()).hexdigest()[:12]
    with open(tmp_t, "rb") as fh:
        raw_t = fh.read()
    dt = hashlib.sha256(raw_t).hexdigest()[:12]
    flipped = bytes([raw_t[0] ^ 1]) + raw_t[1:]
    control_rejects = (hashlib.sha256(flipped).hexdigest()[:12] != seal_t)
    ok = dj == seal_j and dt == seal_t and control_rejects
    if ok:
        os.replace(tmp_j, OUT_JSON)
        os.replace(tmp_t, OUT_TXT)
    else:
        for p in (tmp_j, tmp_t):
            if os.path.exists(p):
                os.remove(p)
    LD.gate("G-ARTIFACT-INTEGRITY",
            "THE BYTES ARE READ BACK BEFORE THEY ARE PROMOTED (#119 + the "
            "AID Z12 order).  The receipt and the transcript are written to "
            "staging files from the objects sealed at gate time, the STAGED "
            "bytes are read back from disk and compared with the digests of "
            "THOSE OBJECTS, and only then does os.replace promote them; on "
            "refusal the staging files are removed and nothing is promoted.  "
            "The comparison is exercised in the failing direction too, on "
            "the same bytes with one bit flipped",
            ok,
            "receipt staged %s seal %s; transcript staged %s seal %s; "
            "one-bit-flip control rejects %s; promoted %s"
            % (dj, seal_j, dt, seal_t, control_rejects, ok))
    print()
    print("receipt    %s  %s" % (OUT_JSON, dj))
    print("transcript %s  %s" % (OUT_TXT, dt))
    return R, payload, text, seal_j, seal_t


# ===========================================================================
# SECTION 13.  THE CLI CONTRACT (#82), THE SELFTEST AND THE SWEEP
# ===========================================================================

def reset_state():
    global LINES, READS, READS_BY_CATEGORY, NUMREG, LD, SEAL
    del LINES[:]
    del READS[:]
    READS_BY_CATEGORY = {}
    NUMREG = set()
    RAW.clear()
    LD = Ledger()
    SEAL = Seal()


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
    """a falsifier run: it must DIE at the gate it names, and write nothing."""
    global MUT, QUIET
    MUT, QUIET = name, True
    reset_state()
    before = artifact_digests()
    try:
        R, _src, ptext = full_run(paper_text=paper_text, write=False)
        closing_battery(R, ptext, PAPER_REL, False)
        finish(R, write=False)
        died = None
    except GateFail as exc:
        died = str(exc).split(" :: ")[0]
    finally:
        MUT, QUIET = None, False
    after = artifact_digests()
    want = [m[1] for m in MUTANTS if m[0] == name]
    return {"mutant": name, "died_at": died,
            "declared_gate": want[0] if want else None,
            "died_at_the_declared_gate": bool(want) and died == want[0],
            "artifacts_unchanged": before == after}


ANCHOR_CLASSES = ("A-PIN", "V01", "A-RUNBOOK", "V11")


def selftest():
    """#82: corrupt ONE anchor of EVERY anchor class, confirm the run dies,
    and confirm nothing is written."""
    global QUIET
    rows = []
    before = artifact_digests()
    for aid in ANCHOR_CLASSES:
        QUIET = True
        reset_state()
        try:
            R, _src, ptext = full_run(break_anchor=aid, write=False)
            closing_battery(R, ptext, PAPER_REL, False)
            finish(R, write=False)
            ok, where = False, "NO-FAILURE"
        except GateFail as exc:
            ok, where = True, str(exc).split(" :: ")[0]
        finally:
            QUIET = False
        rows.append((aid, ok, where))
    after = artifact_digests()
    for (aid, ok, where) in rows:
        print("[selftest] corrupted %-10s -> %s at %s"
              % (aid, "died" if ok else "SURVIVED", where))
    print("[selftest] artifacts %s"
          % ("unchanged" if before == after else "CHANGED"))
    return 0 if all(r[1] for r in rows) and before == after else 1


def sweep(paper_text):
    return [run_mutant(name, paper_text) for name in MUTANT_NAMES]


def parse_args(argv):
    """THE ARGV WHITELIST.  Unknown flags exit 2; nothing is silently
    ignored."""
    opts = {"sweep": False, "selftest": False, "mutant": None,
            "quiet": False}
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
        print("[cli] usage: fac_exact.py [--sweep] [--selftest] "
              "[--mutant NAME] [--list-gates] [--quiet]", file=sys.stderr)
        return 2
    if opts.get("list"):
        for (name, gate_name, why, _f) in MUTANTS:
            print("%-28s %-46s %s" % (name, gate_name, why))
        return 0
    if opts["selftest"]:
        return selftest()
    QUIET = opts["quiet"]
    ppath = os.path.join(REPO, PAPER_REL)
    paper_text = (read_text(ppath, "PAPER-UNDER-TEST")
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
            print("        %-28s -> %s" % (r["mutant"], r["died_at"]))
        if bad:
            print("[sweep] OFF TARGET: %s" % [r["mutant"] for r in bad],
                  file=sys.stderr)
            return 1
    reset_state()
    MUT = None
    try:
        R, _src, ptext = full_run(paper_text=paper_text, write=True)
        ptext = closing_battery(R, ptext, PAPER_REL, True)
        SWEEP_ROWS.extend(swept)
        finish(R, write=True, swept=bool(swept))
    except GateFail as exc:
        print("[FAIL] %s" % exc, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
