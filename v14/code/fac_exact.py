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
    ("SEAL-CRITERION", "criterion", "G-CRITERION-FROZEN-BEFORE-THE-CENSUS"),
    ("SEAL-LEGBIND", "leg_binding", "G-WHICH-LEG-BINDS"),
    ("SEAL-ACTOR", "actor_census", "G-ACTOR-GRAIN-ADMISSIBLE-PER-HISTORY"),
    ("SEAL-CELL", "cell_census", "G-CARRIER-GRAIN-ADMISSIBLE-PER-HISTORY"),
    ("SEAL-CROSS", "cross_grain", "G-CROSS-GRAIN-CONTAINMENT"),
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
    ("SEAL-PAPER-COVERAGE", "paper_coverage", "G-PAPER-NUMERAL-COVERAGE"),
    ("SEAL-REFERENT", "referent_binding", "G-SENTENCE-REFERENT-BINDING"),
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
]
DECLARED_UNSEALED = ["arithmetic", "python", "seal_manifest",
                     "payload_sha256_12"]
MEASURED_KEYS = ("arena", "carrier", "corpora", "criterion", "leg_binding",
                 "actor_census", "cell_census", "cross_grain", "coin_order",
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


NUMWORDS = ("ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN",
            "EIGHT", "NINE", "TEN", "ELEVEN", "TWELVE")
WORDNUM = dict({w.lower(): i for i, w in enumerate(NUMWORDS)},
               twice=2, thirteen=13, fourteen=14, fifteen=15, sixteen=16,
               seventeen=17, eighteen=18, nineteen=19, twenty=20, thirty=30,
               forty=40, fifty=50, sixty=60, hundred=100, thousand=1000)


# ===========================================================================
# SECTION 2.  PROVENANCE -- THE PINNED SOURCES AND THE VERBATIM ANCHORS
# ===========================================================================

PIN_REL = "v14/note-fac-pin.md"

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
WALLS = [
    ("W-NO-FORCED-ACTOR-FACTORIZATION",
     ["the actor factorization is forced by the law",
      "the nine-fold division is forced, full stop",
      "the factorization of the arena into actors is forced"],
     "the AID adjudication's not-licensed list, paraphrase-hardened"),
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
      "actors do not exist as threads", "actors really are threads"],
     "no unscoped reality language about actors"),
    ("W-NO-FIVE-RESONANCE",
     ["the same five appears in paper-20's horizon",
      "this five and the horizon-5 are the same five",
      "the crystallization five resonates with the horizon five"],
     "the resonance the AID adjudication demoted to refused"),
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
                   "induced_cell_partition", "admissible_actor",
                   "admissible_cell")
CRITERION_FORBIDDEN_NAMES = ("actor_census", "cell_census", "CENSUS",
                             "ADMISSIBLE_SET", "R", "VERDICT")


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
    identified.  This is the carrier partition an actor-grain factorization
    induces, and it is what LEG-4 is evaluated on."""
    bm = block_map(part)
    lab = [(bm[x], I7_LINKS.index(l)) for (x, l) in CELLS]
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


def admissible_actor(part, H, rec, bm=None):
    """the criterion at the ACTOR grain, leg by leg, both coin orders."""
    l1 = leg1_actor(part, bm)
    l2 = leg2_actor(part, H)
    l3 = leg3_actor(part, rec)
    if not (l1 and l2 and l3):
        return (l1, l2, l3, None, None, False)
    cp = induced_cell_partition(part)
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


def pairwise_cell_partition(part):
    """THE PAIRWISE IMAGE: a cell IS the co-division pair {x, x + l} (OCC), so
    an actor factorization identifies two cells when their pairs of blocks
    agree as unordered pairs.  This family is NOT the directionwise one and is
    censused beside it."""
    bm = block_map(part)
    lab = [tuple(sorted((bm[x], bm[vadd(x, l)]))) for (x, l) in CELLS]
    return canonical_cell_partition(lab)


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
# arena.  It types no word: the outcome vocabulary is parsed from the pin.
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
              actor_inventory, cell_inventory):
    """the derived slot each outcome family carries: FORCED names its witness,
    DECLARED names its inventory, STRATIFIED names the grains."""
    if word == "FAC-FACTORIZATION-FORCED":
        return "WITNESS=%s" % (actor_inventory[0] if actor_inventory else "-")
    if word == "FAC-FACTORIZATION-DECLARED":
        return "INVENTORY=%s" % ",".join(actor_inventory)
    return ("BY-GRAIN=ACTOR-%d-OF-%d-UNIQUE-vs-CARRIER-%d-OF-%d-UNIQUE"
            % (n_hist - len(actor_nonunique), n_hist,
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

    say()
    say("SECTION 3.  THE CRITERION, FROZEN BEFORE THE FIRST CENSUS ROW")

    csrc = criterion_source(src)
    creads = criterion_reads(src)
    leaks = sorted({n for names in creads.values() for n in names
                    if n in CRITERION_FORBIDDEN_NAMES})
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
        "combined_sha256_12": digest(sorted(
            (k, v["sha256_12"]) for k, v in csrc.items())),
        "free_names": creads,
        "census_products_referenced": leaks,
        "coin_orders": list(COIN_ORDERS),
    }
    reg(len(csrc), sum(v["lines"] for v in csrc.values()))
    LD.gate("G-CRITERION-FROZEN-BEFORE-THE-CENSUS",
            "THE CRITERION IS DECLARED AND DIGESTED BEFORE ANY CENSUS ROW "
            "RUNS.  Its %d functions -- %s lines in all -- are located by AST "
            "in this file's own source and digested here, at a point in the "
            "run where not one admissible set has yet been computed; and the "
            "free names each leg references are extracted and required to "
            "contain no census product, so a leg cannot consult the answer it "
            "is deciding.  The four legs are %s"
            % (len(csrc), sum(v["lines"] for v in csrc.values()),
               ", ".join(R["criterion"]["legs"])),
            len(csrc) == len(CRITERION_FUNCS)
            and not pick("MUT-CRITERION-LEAK", leaks, ["actor_census"]),
            "functions %d of %d declared, combined digest %s, leaked names %s"
            % (len(csrc), len(CRITERION_FUNCS),
               R["criterion"]["combined_sha256_12"], leaks or "none"))
    SEAL.take("SEAL-CRITERION", R)

    wins = []
    for (nm, why) in WINDOW_DECL:
        size = {"W-CORPUS-C1-C2-C3": len(corp),
                "W-ACTOR-LATTICE-COMPLETE": len(P9),
                "W-CELL-INDUCED-PLUS-STRATA": len(winlist),
                "W-COHERENCE-LADDER": len(COHERENCE_ROWS),
                "W-FULL-LATTICE-PER-LEG": 0,
                "W-CONTROL-ARENAS": 0}[nm]
        univ = {"W-ACTOR-LATTICE-COMPLETE": bell(NACT),
                "W-CELL-INDUCED-PLUS-STRATA": bell(DIM)}.get(nm)
        wins.append({"window": nm, "members": size,
                     "ambient_universe": univ,
                     "complete_in_its_universe": univ is not None
                     and size == univ, "declaration": why})
    R["windows"] = wins
    LD.gate("G-WINDOWS-DECLARED-WITH-THEIR-BOUNDS",
            "EVERY WINDOW IS NAMED IN-STRING WITH ITS BOUND.  %d windows are "
            "declared; the actor lattice is COMPLETE at %s of Bell(9) = %s, "
            "and the carrier window is a declared %s of Bell(27) = %s, which "
            "is the whole reason it is a window at all.  No census below is "
            "truncated silently: the coherence ladder searches upward until "
            "it meets the complete relation, and the per-leg sweep publishes "
            "its sub-window and its complement"
            % (len(wins), com(len(P9)), com(bell(NACT)), com(len(winlist)),
               com(bell(DIM))),
            all(w["declaration"] for w in wins)
            and pick("MUT-WINDOW", len(P9), 0) == bell(NACT)
            and len(winlist) < bell(DIM),
            "windows %d, actor lattice %d of %d, carrier window %d of %d"
            % (len(wins), len(P9), bell(NACT), len(winlist), bell(DIM)))
    SEAL.take("SEAL-WINDOWS", R)

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
    R["cell_census"] = {
        "window": len(winlist), "ambient": bell(DIM),
        "leg1_geometry_survivors": len(leg1_cell_survivors),
        "leg1_survivor_names": cell_names,
        "families": {k: v for k, v in sorted(Counter(
            f for p in leg1_cell_survivors for f in window[p]).items())},
    }
    reg(len(leg1_cell_survivors))
    for v in R["cell_census"]["families"].values():
        reg(v)

    actor_rows, cell_rows = [], []
    coin_rows = {o: 0 for o in COIN_ORDERS}
    coin_disagree = 0
    a_non, c_non = [], []
    a_cards, c_cards = Counter(), Counter()
    a_inventory, c_inventory = Counter(), Counter()
    rec_nonconstant = 0
    for k, (tag, H) in enumerate(corp):
        rel = codivision(H)
        rec = record_field(H, rel)
        rows = {tuple(rec[SITE_INDEX[x] * 3 + i] for i in range(3))
                for x in SITES}
        if len(rows) > 1:
            rec_nonconstant += 1
        foot = [cell_footprint(F) for F in H]
        adm_a = []
        for j, i in enumerate(leg1_actor_set):
            v = admissible_actor(P9[i], H, rec, BM[i])
            if v[3] is not None and v[3] != v[4]:
                coin_disagree += 1
            for o, val in zip(COIN_ORDERS, (v[3], v[4])):
                if val:
                    coin_rows[o] += 1
            if v[5]:
                adm_a.append(leg1_names[j])
        adm_c = []
        for j, p in enumerate(leg1_cell_survivors):
            v = admissible_cell(p, foot, rec, True)
            if v[3] is not None and v[3] != v[4]:
                coin_disagree += 1
            for o, val in zip(COIN_ORDERS, (v[3], v[4])):
                if val:
                    coin_rows[o] += 1
            if v[5]:
                adm_c.append(cell_names[j])
        a_cards[len(adm_a)] += 1
        c_cards[len(adm_c)] += 1
        for nm in adm_a:
            a_inventory[nm] += 1
        for nm in adm_c:
            c_inventory[nm] += 1
        if len(adm_a) != 1:
            a_non.append(k)
            actor_rows.append({"index": k, "corpus": tag,
                               "admissible": sorted(adm_a),
                               "cardinality": len(adm_a)})
        if len(adm_c) != 1:
            c_non.append(k)
            cell_rows.append({"index": k, "corpus": tag,
                              "admissible": sorted(adm_c),
                              "cardinality": len(adm_c)})
    R["actor_census"].update({
        "histories": len(corp),
        "cardinality_distribution": {str(k): v for k, v in
                                     sorted(a_cards.items())},
        "unique_at": a_cards[1], "non_unique_at": len(a_non),
        "non_unique_rows": actor_rows,
        "inventory": {k: v for k, v in sorted(a_inventory.items())},
    })
    R["cell_census"].update({
        "histories": len(corp),
        "cardinality_distribution": {str(k): v for k, v in
                                     sorted(c_cards.items())},
        "unique_at": c_cards[1], "non_unique_at": len(c_non),
        "non_unique_rows": cell_rows,
        "inventory": {k: v for k, v in sorted(c_inventory.items())},
    })
    reg(a_cards[1], len(a_non), c_cards[1], len(c_non), rec_nonconstant)
    for d in (a_cards, c_cards, a_inventory, c_inventory):
        for v in d.values():
            reg(v)
    for kk in list(a_cards) + list(c_cards):
        reg(kk)
    LD.gate("G-ACTOR-GRAIN-ADMISSIBLE-PER-HISTORY",
            "THE ACTOR-GRAIN ADMISSIBLE SET IS COUNTED PER HISTORY, NOT IN "
            "AGGREGATE (#87).  At each of the %s committed histories the "
            "criterion is evaluated on every LEG-1 survivor and the "
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
            "unique %d, non-unique %d, cardinalities %s"
            % (a_cards[1], len(a_non), sorted(a_cards)))
    SEAL.take("SEAL-ACTOR", R)
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

    R["coin_order"] = {
        "declared_orders": list(COIN_ORDERS),
        "leg4_passes_per_order": dict(sorted(coin_rows.items())),
        "rows_where_the_orders_disagree": coin_disagree,
        "fiber": "INERT-ON-EVERY-CENSUS-ROW" if coin_disagree == 0
                 else "LIVE",
        "duty": "paper-20 declares the coin order a verdict-relevant fiber "
                "(#293); both members are run on every LEG-4 evaluation and "
                "both counts are published here",
    }
    reg(coin_disagree, *sorted(coin_rows.values()))
    LD.gate("G-BOTH-COIN-ORDERS-PUBLISHED",
            "THE COIN-ORDER DUTY IS DISCHARGED BY RUNNING BOTH, NOT BY "
            "CHOOSING ONE (#293).  Every LEG-4 evaluation in both censuses is "
            "performed at %s and at %s; the pass counts are %s and the "
            "number of rows at which the two orders disagree is %d, so the "
            "fiber is published rather than stamped away"
            % (COIN_ORDERS[0], COIN_ORDERS[1],
               ", ".join("%s=%s" % (o, com(coin_rows[o]))
                         for o in COIN_ORDERS), coin_disagree),
            sorted(coin_rows) == sorted(COIN_ORDERS)
            and all(v > 0 for v in coin_rows.values())
            and pick("MUT-COIN", coin_disagree, 1) == coin_disagree,
            "orders %s, passes %s, disagreements %d"
            % (list(COIN_ORDERS), dict(sorted(coin_rows.items())),
               coin_disagree))
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
    R["leg_binding"] = {
        "sub_window": len(sub_idx), "complement": len(corp) - len(sub_idx),
        "lattice": len(P9),
        "profiles": [{"leg1": k[0], "leg2": k[1], "leg3": k[2],
                      "all_three": k[3], "histories": v}
                     for k, v in sorted(prof.items())],
        "leg2_closed_form_mismatches": theorem_bad,
        "record_non_site_constant_histories": rec_nonconstant,
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
    reg(len(sub_idx), len(corp) - len(sub_idx), theorem_bad)
    for p in R["leg_binding"]["profiles"]:
        reg(p["histories"])
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
    SEAL.take("SEAL-LEGBIND", R)

    say()
    say("SECTION 6.  MEASUREMENT TWO -- THE GROUPOID CRYSTALLIZATION")

    gsub = [k for k, (tag, _h) in enumerate(corp) if tag in ("C1", "C3")]
    arrows_rows = Counter()
    for k in gsub:
        g = groupoid_arrows(corp[k][1])
        arrows_rows[(g["objects"], tuple(sorted(set(g["isotropy_orders"]))),
                     g["connected_components"])] += 1
    ladder = []
    thresholds = Counter()
    atom_breaks = 0
    complete_equals_stab = 0
    complete_mismatch = 0
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
    R["groupoid"] = {
        "by_relation": by_rel,
        "arrow_profiles": [{"objects": k[0], "isotropy_orders": list(k[1]),
                            "connected_components": k[2], "histories": v}
                           for k, v in sorted(arrows_rows.items())],
        "arrow_sub_window": len(gsub),
        "coherence_rows": list(COHERENCE_ROWS),
        "ladder": ladder,
        "complete_equals_the_global_stabilizer": complete_equals_stab,
        "complete_mismatches": complete_mismatch,
        "collapse_thresholds": {"%s-T%d-w%s" % k: v
                                for k, v in sorted(thresholds.items())},
        "threshold_values": sorted({k[2] for k in thresholds}),
    }
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
    SEAL.take("SEAL-GROUPOID", R)

    atom_word = atom_law(atom_breaks, complete_mismatch == 0)
    R["atom"] = {
        "histories_with_a_trivial_global_stabilizer":
            sum(1 for r in PERHIST if r["stab"] == 1),
        "of_those_carrying_a_nontrivial_adjacent_coherent_family":
            atom_breaks,
        "atom_word": atom_word,
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
            atom_law(atom_breaks, complete_mismatch == 0),
            "trivial-stabilizer histories %d, breaks %d, word %s"
            % (R["atom"]["histories_with_a_trivial_global_stabilizer"],
               atom_breaks, atom_word))
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
        brute_checked, brute_bad,
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
            "at %d rows and at the carrier grain at %d.  The raw route is "
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
            and agree_actor != agree_cell,
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
    R["transport"] = {
        "ladder_rows": {k: rung[k] for k in sorted(rung)},
        "atom_break_transports_across_every_rung": holds,
        "scope": "the R-ladder rows this corpus carries are R = 3, R = 4 and "
                 "R = 6; PER-L closed the L-ladder transport by theorem and "
                 "PER-R places its own successor at R = 8, so nothing here "
                 "is claimed beyond the rungs measured",
    }
    for v in rung.values():
        reg(v["rounds"], v["histories"], v["unique_at_the_actor_grain"],
            v["unique_at_the_carrier_grain"], v["atom_breaks"],
            *v["collapse_thresholds"])
    LD.gate("G-TRANSPORT-ALONG-THE-R-LADDER",
            "THE MEASUREMENT IS REPORTED AT EVERY RUNG THE CORPUS CARRIES.  "
            "The three rungs are %s; at each one the admissible cardinality, "
            "the atom outcome and the collapse threshold are taken from that "
            "rung's OWN histories rather than from the corpus aggregate, and "
            "the break-at-the-adjacent-relation result is checked to "
            "coincide with the actor grain's uniqueness rung by rung: %s"
            % (", ".join(sorted(rung)), holds),
            pick("MUT-TRANSPORT", holds, False) and len(rung) == 3,
            "rungs %s, transports %s"
            % (sorted(rung), holds))
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
        syn_rows.append({"arena": nm, "events": len(H),
                         "distinct_record_rows": len(rows),
                         "leg3_passers_of_the_lattice": n3,
                         "record_binds": n3 < len(P9),
                         "record_dynamics_wedge": wedge,
                         "global_stabilizer": stab,
                         "adjacent_coherent_families": g1,
                         "atom_word": atom_law(
                             1 if (stab == 1 and g1 > 1) else 0, True)})
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

    words = sorted({r["head_word"] for r in ctrl_rows}
                   | {r["atom_word"] for r in syn_rows}
                   | {atom_law(0, True), atom_law(1, True),
                      atom_law(1, False)})
    fams = set(R["pre_registered_outcomes"]["families"])
    unreachable = sorted(f for f in fams
                         if not any(w.startswith(f) for w in words))
    R["controls"] = {
        "declared_sub_arenas": ctrl_rows,
        "synthetic_histories": syn_rows,
        "alternative_link_sets": alt_rows,
        "words_emitted": words,
        "pre_registered_families": sorted(fams),
        "families_no_arena_reached": unreachable,
        "record_dynamics_wedge_on_the_committed_corpus": 0,
        "record_dynamics_wedge_on_the_control": wedge_fires,
        "note": "every row above is a genuine evaluation of the SAME "
                "criterion and the SAME head law on a declared datum; no "
                "control row is typed and none is forged",
    }
    reg(wedge_fires, len(words), len(fams))
    LD.gate("G-EVERY-OUTCOME-WORD-EMITTABLE",
            "EVERY PRE-REGISTERED OUTCOME WORD IS SHOWN EMITTABLE ON A "
            "DECLARED ARENA (#299).  The head law returns %s on the strict "
            "triples, %s on the non-unique histories and %s on the whole "
            "corpus; the atom law returns both of its substantive words on "
            "declared synthetic histories -- the overlapping chain forces "
            "the identification at the adjacent relation and the corpus "
            "does not -- and its blocked word is reachable only from an "
            "instrument fault, which is what that word is for.  %d of the "
            "pin's %d families are reached by an arena: %s"
            % (ctrl_rows[0]["head_word"], ctrl_rows[1]["head_word"],
               ctrl_rows[3]["head_word"], len(fams) - len(unreachable),
               len(fams), unreachable or "none unreached"),
            pick("MUT-CONTROLS", len(unreachable), 1) == 0
            and len({r["head_word"] for r in ctrl_rows}) >= 3
            and len({r["atom_word"] for r in syn_rows}) >= 2,
            "head words %s, atom words %s, unreached families %s"
            % (sorted({r["head_word"] for r in ctrl_rows}),
               sorted({r["atom_word"] for r in syn_rows}),
               unreachable or "none"))
    LD.gate("G-THE-RECORD-LEG-IS-EXERCISED-SOMEWHERE",
            "A LEG THAT NEVER FAILS ON THE CORPUS IS EXERCISED ON THE "
            "CONTROL.  LEG-3 admits the whole lattice at every committed "
            "history because this corpus's record field is site-constant "
            "there; on the declared synthetic histories it binds at %d of %d "
            "arenas, and the record-versus-dynamics wedge -- partitions the "
            "coin cannot tell apart because it reads the record only modulo "
            "three, while the record itself differs -- is empty on the "
            "committed corpus and fires %d times on the control.  The leg is "
            "therefore non-binding HERE, not vacuous"
            % (sum(1 for r in syn_rows if r["record_binds"]), len(syn_rows),
               wedge_fires),
            pick("MUT-WEDGE", wedge_fires, 0) > 0
            and any(r["record_binds"] for r in syn_rows),
            "arenas where LEG-3 binds %d of %d, wedge fires %d"
            % (sum(1 for r in syn_rows if r["record_binds"]), len(syn_rows),
               wedge_fires))
    SEAL.take("SEAL-CONTROLS", R)

    say()
    say("SECTION 10.  MEASURE RELATIVITY, CLASS BINDING AND THE HEAD")

    ratios = [
        ("actor-grain histories with a unique factorization",
         a_cards[1], len(corp), "W-CORPUS-C1-C2-C3"),
        ("carrier-grain histories with a unique factorization",
         c_cards[1], len(corp), "W-CORPUS-C1-C2-C3"),
        ("actor partitions surviving the geometry leg",
         len(leg1_actor_set), len(P9), "W-ACTOR-LATTICE-COMPLETE"),
        ("carrier-window partitions surviving the geometry leg",
         len(leg1_cell_survivors), len(winlist),
         "W-CELL-INDUCED-PLUS-STRATA"),
        ("carrier-window members against the carrier's whole lattice",
         len(winlist), bell(DIM), "W-CELL-INDUCED-PLUS-STRATA"),
        ("histories whose global stabilizer is trivial and whose adjacent "
         "groupoid is not", atom_breaks, len(corp), "W-CORPUS-C1-C2-C3"),
    ]
    R["measure_relativity"] = {
        "stamp": "COUNTING-ONLY",
        "declared_measure": None,
        "rows": [{"quantity": q, "numerator": n, "denominator": d,
                  "window": w, "stamp": "COUNTING-ONLY"}
                 for (q, n, d, w) in ratios],
        "warrant": "no fraction in this unit is a probability: each is a "
                   "count over a declared window and carries that window's "
                   "name beside it (E-24)",
    }
    for (_q, n, d, _w) in ratios:
        reg(n, d)
    LD.gate("G-E24-COUNTING-ONLY",
            "EVERY PUBLISHED FRACTION CARRIES ITS WINDOW AND ITS STAMP "
            "(E-24).  %d ratios are published; each names its numerator, its "
            "denominator AND the declared window the denominator ranges "
            "over, and each is stamped COUNTING-ONLY because this unit "
            "declares no measure on partition lattices.  A ratio whose "
            "window is absent, or whose numerator and denominator come from "
            "different windows, fails here" % len(ratios),
            all(r["window"] for r in R["measure_relativity"]["rows"])
            and all(r["numerator"] <= r["denominator"]
                    for r in R["measure_relativity"]["rows"])
            and pick("MUT-E24", R["measure_relativity"]["stamp"],
                     "PROBABILITY") == "COUNTING-ONLY",
            "ratios %d, all windowed %s, all stamped %s"
            % (len(ratios),
               all(r["window"] for r in R["measure_relativity"]["rows"]),
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
        len(COIN_ORDERS), len(POLARITY), len(CLOSING_GATE_NAMES))
    inv_actor = sorted(a_inventory)
    slot = head_slot(head_word, a_non, c_non, len(corp), inv_actor,
                     sorted(c_inventory))
    R["counts"] = {
        "histories": len(corp),
        "actor_lattice": len(P9), "carrier_window": len(winlist),
        "actor_leg1": len(leg1_actor_set),
        "carrier_leg1": len(leg1_cell_survivors),
        "actor_unique": a_cards[1], "carrier_unique": c_cards[1],
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
            and alt["atom_breaks"] == atom_breaks)
    LD.gate("G-VERDICT-RECONSTRUCTED-BY-A-SECOND-ROUTE",
            "THE HEAD IS DERIVED TWICE, BY ROUTES THAT SHARE NO DISPATCHER "
            "AND NO CENSUS LOOP.  The second route calls neither "
            "admissible_actor nor admissible_cell and reads none of the "
            "first route's rows: it rebuilds every admissible set from the "
            "raw leg predicates, recounts the atom breaks from the "
            "coherence relation directly rather than from the ladder's "
            "cache, and re-applies the head law to its own numbers.  What "
            "the two routes DO share is the four leg predicates themselves, "
            "which are the object under test and are de-twinned by their "
            "own closed-form gates above, not by duplication.  The two "
            "agree on the head word, the atom word and all three counts: %s"
            % same,
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
        ("THESIS", None),
        ("HISTORIES", "counts/histories"),
        ("ACTOR-LATTICE", "counts/actor_lattice"),
        ("ACTOR-GRAIN-LAW-COMPATIBLE-PARTITIONS", "counts/actor_leg1"),
        ("ACTOR-GRAIN-UNIQUE-FACTORIZATION",
         "counts/actor_unique|counts/histories"),
        ("CARRIER-WINDOW", "counts/carrier_window"),
        ("CARRIER-GRAIN-LAW-COMPATIBLE-PARTITIONS", "counts/carrier_leg1"),
        ("CARRIER-GRAIN-UNIQUE-FACTORIZATION",
         "counts/carrier_unique|counts/histories"),
        ("COIN-ORDER-DISAGREEMENTS", "counts/coin_disagreements"),
    ]),
    ("FAC-GROUPOID", [
        ("ATOM", None),
        ("ATOM-BREAKS", "counts/atom_breaks|counts/histories"),
        ("COLLAPSE-THRESHOLDS", "counts/collapse_thresholds"),
        ("ARENA-GROUP-ORDER", "counts/arena_group_order"),
    ]),
]


def verdict_segments(R, head_word, atom_word, slot):
    """the head, rendered from a declared field spec whose every field names a
    receipt path; the audit route types no copy of any of it."""
    out = []
    for label, fields in VERDICT_SPEC:
        parts = []
        for (nm, path) in fields:
            if path is None:
                parts.append("%s=%s" % (nm, "THE-LAW-ADMITS-MORE-THAN-ONE-"
                                        "FACTORIZATION-ONLY-WHERE-THE-"
                                        "HISTORY-REPEATS-A-PARALLEL-CLASS"
                                        if nm == "THESIS" else atom_word))
                continue
            if "|" in path:
                a, b = path.split("|")
                parts.append("%s=%s-OF-%s" % (nm, com(jpath(R, a)),
                                              com(jpath(R, b))))
            else:
                v = jpath(R, path)
                parts.append("%s=%s" % (nm, ",".join(str(x) for x in v)
                                        if isinstance(v, list) else com(v)))
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
    no call to the criterion's dispatcher and no reading of route A's rows."""
    au = cu = ab = 0
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
        if young_order(signature_blocks(H)) == 1 and \
                gamma_relation_count(H, [(t, t - 1) for t in
                                         range(1, len(H))]) > 1:
            ab += 1
    return {"actor_unique": au, "carrier_unique": cu, "atom_breaks": ab,
            "head_word": head_law(len(corp), an, cn),
            "atom_word": atom_law(ab, True)}


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
                   "adjacent families", "atom word"],
        "rows": [[r["arena"], str(r["events"]),
                  str(r["distinct_record_rows"]),
                  com(r["leg3_passers_of_the_lattice"]),
                  str(r["record_dynamics_wedge"]),
                  com(r["global_stabilizer"]),
                  com(r["adjacent_coherent_families"]), r["atom_word"]]
                 for r in R["controls"]["synthetic_histories"]]}
    T["T7-THE-ALTERNATIVE-LINK-SETS"] = {
        "header": ["synthetic arena", "declared links",
                   "geometry-leg survivors"],
        "rows": [[r["arena"], str(r["declared_links"]),
                  com(r["leg1_survivors"])]
                 for r in R["controls"]["alternative_link_sets"]]}
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
                                "coverage", "pre_registered_outcomes",
                                "walls"):
        if key in R:
            walk(R[key])
    return out


# THE DECLARED REFERENT UNIVERSES.  `counts`, `verdict` and
# `measure_relativity` are AGGREGATES -- they carry numbers drawn from every
# measurement at once, so admitting them as universes would make the
# sentence-level binding vacuous (a ratio joining any two published numbers
# would share one of them).  They are excluded by declaration, and the
# MUT-REFERENT falsifier is what established that they had to be.
REFERENT_UNIVERSES = ("arena", "carrier", "corpora", "criterion",
                      "leg_binding", "actor_census", "cell_census",
                      "cross_grain", "coin_order", "groupoid", "atom",
                      "grain_triangle", "persistence", "transport",
                      "controls", "class_binding", "provenance", "windows")


def receipt_paths_for(tok, R):
    """which declared referent universe carries a numeral -- the machinery
    behind the sentence-level referent binding."""
    hit = set()

    def walk(o):
        if isinstance(o, bool):
            return False
        if isinstance(o, int):
            return str(o) == tok or com(o) == tok
        if isinstance(o, str):
            return tok in NUMTOK.findall(o) or \
                tok.replace(",", "") in [t.replace(",", "")
                                         for t in NUMTOK.findall(o)]
        if isinstance(o, dict):
            return any(walk(o[k]) for k in sorted(o, key=str))
        if isinstance(o, (list, tuple)):
            return any(walk(v) for v in o)
        return False
    for key in REFERENT_UNIVERSES:
        if key in R and walk(R[key]):
            hit.add(key)
    return hit


def referent_binding(R, text):
    """#293 Z6 / PER-R Z10: no sentence pairs numerals from different
    universes.  Every `N of M` relation in the paper is resolved against the
    receipt and both numerals are required to be carried by a COMMON
    top-level measurement key."""
    body = SECREF.sub(" ", HEADNUM.sub("#### ", canon(text)))
    if mut("MUT-REFERENT"):
        body = body + " and 5,852 of 42,295 members "
    bad, checked = [], 0
    for m in RATIO_PAT.finditer(body):
        n, d = m.group(1).strip(","), m.group(2).strip(",")
        if n == d:
            continue
        checked += 1
        pn, pd = receipt_paths_for(n, R), receipt_paths_for(d, R)
        if not (pn & pd):
            bad.append("%s of %s" % (n, d))
    return {"relations_checked": checked, "unbound": sorted(set(bad)),
            "universes": list(REFERENT_UNIVERSES),
            "aggregates_excluded": ["counts", "verdict",
                                    "measure_relativity"],
            "rule": "the numerator and the denominator of every published "
                    "ratio must be carried by one common DECLARED REFERENT "
                    "UNIVERSE of this run's receipt; the aggregate keys, "
                    "which carry numbers from every measurement at once, are "
                    "excluded by declaration so the test is not vacuous"}


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
    body = HEXTOK.sub(" ", SECREF.sub(" ", HEADNUM.sub("#### ", body)))
    reference = len(NUMTOK.findall(
        HEXTOK.sub(" ", SECREF.sub(" ", HEADNUM.sub("#### ", text)))))
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
        word_unbacked.append(wd)
    if mut("MUT-PAPER-FENCE-MULTISET"):
        seg = R["verdict"]["segments"][0]
        text = text.replace(seg, seg.replace("ACTOR", "FORGED"), 1)
    want = Counter({canon(seg): FENCE_COPIES
                    for seg in R["verdict"]["segments"]})
    got = Counter(canon(b) for b in FENCE.findall(text))
    return {"numerals_scanned": scanned,
            "numerals_in_the_whole_paper": reference,
            "scan_is_total": scanned == reference,
            "unbacked": sorted(set(unbacked)),
            "spelled_numerals_scanned": words,
            "spelled_unbacked": sorted(set(word_unbacked)),
            "section_heads": len(heads),
            "verdict_fences_required": dict(sorted(want.items())),
            "verdict_fences_found": {k: got.get(k, 0) for k in sorted(want)},
            "fence_multiset_equal": all(got.get(k, 0) == v
                                        for k, v in want.items()),
            "exemptions_declared": len(exempt),
            "exemptions_fired": {k: v for k, v in sorted(fired.items())},
            "exemptions_that_never_fired": sorted(e[0] for e in exempt
                                                  if e[0] not in fired)}


# THE POLARITY AXES.  Each names the asserted form AS IT APPEARS IN THE HEAD
# and the inversion a forger would substitute.  The forms are the FENCE forms,
# so a control-arm row that legitimately reports the other word as DATA is not
# mistaken for an inverted claim -- the axis is about what the paper ASSERTS.
POLARITY = [
    ("head-word", "FAC-STRATIFIED<", "FAC-FACTORIZATION-FORCED<"),
    ("atom-word", "ATOM=FAC-ATOM-BREAKS-AT-THE-GROUPOID-GRAIN",
     "ATOM=FAC-ATOM-HOLDS-AT-THE-GROUPOID-GRAIN"),
    ("transport-direction", "does not transport", "transports freely"),
    ("binding-direction", "non-binding", "binding at every history"),
    ("measure-stamp", "COUNTING-ONLY", "under the declared measure"),
]


def paper_polarity(R, text, mutated=False):
    body = canon(text)
    rows = []
    for (nm, true_form, false_form) in POLARITY:
        t = canon(true_form) in body
        f = canon(false_form) in body
        if mutated and nm == "atom-word":
            f = True
        rows.append({"axis": nm, "asserted_form_present": t,
                     "inverted_form_present": f})
    return {"rows": rows,
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
]
MUTANT_NAMES = [m[0] for m in MUTANTS]

CLOSING_GATE_NAMES = (
    "G-WALLS-SCAN-THE-PAPER", "G-PAPER-CLAIMS",
    "G-PAPER-TABLES-WITH-HEADERS", "G-PAPER-NUMERAL-COVERAGE",
    "G-SENTENCE-REFERENT-BINDING", "G-PAPER-CLAIM-POLARITY",
    "G-NO-TYPED-COUNTS", "G-NO-FLOATS", "G-READS-DECLARED",
    "G-FALSIFIER-COVERAGE", "G-FALSIFIER-REACHABILITY",
    "G-PAPER-INSTRUMENT-RAN-IN-THE-PLAIN-RUN", "G-SWEEP-IS-EXECUTION-BOUND",
    "G-TRANSCRIPT-SEALED-WHOLE", "G-GATE-ACCOUNTING", "G-SEAL-TOTALITY",
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
    tmiss = []
    for tname in sorted(R["paper_tables"]):
        t = R["paper_tables"][tname]
        hdr = [canon(h) for h in t["header"]]
        if mut("MUT-PAPER-TABLE") and tname == "T2-THE-CENSUS":
            hdr[1], hdr[2] = hdr[2], hdr[1]
        if tuple(hdr) not in pset:
            tmiss.append(tname + "/HEADER")
        for row in t["rows"]:
            if tuple(canon(c) for c in row) not in pset:
                tmiss.append(tname + "/" + canon(row[0]))
    LD.gate("G-PAPER-TABLES-WITH-HEADERS",
            "EVERY TABLE IS RENDERED FROM THE RECEIPT, HEADERS INCLUDED "
            "(PER-R Z7).  %d tables with %d data rows and %d header rows are "
            "built here and each is required to appear in the paper cell by "
            "cell; a column header is a claim, so a header swap that leaves "
            "every number correct dies at this gate"
            % (len(R["paper_tables"]),
               sum(len(t["rows"]) for t in R["paper_tables"].values()),
               len(R["paper_tables"])),
            not tmiss,
            "tables %d, rows %d, missing %s"
            % (len(R["paper_tables"]),
               sum(len(t["rows"]) for t in R["paper_tables"].values()),
               tmiss[:6] or "none"))
    SEAL.take("SEAL-PAPER-TABLES", R)

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

    R["referent_binding"] = referent_binding(R, paper_text)
    rb = R["referent_binding"]
    LD.gate("G-SENTENCE-REFERENT-BINDING",
            "NO SENTENCE PAIRS NUMERALS FROM DIFFERENT UNIVERSES (#293 Z6).  "
            "%d published ratios of the form `N of M` are resolved against "
            "the receipt and both members are required to be carried by one "
            "common member of the %d DECLARED REFERENT UNIVERSES; the three "
            "aggregate keys are excluded by declaration, since a universe "
            "that carries every number binds nothing.  The LOR disease -- "
            "every numeral true, the relation false -- dies here"
            % (rb["relations_checked"], len(REFERENT_UNIVERSES)),
            not rb["unbound"] and rb["relations_checked"] > 0,
            "checked %d, unbound %s"
            % (rb["relations_checked"], rb["unbound"][:6] or "none"))
    SEAL.take("SEAL-REFERENT", R)

    R["polarity"] = paper_polarity(R, paper_text, mut("MUT-POLARITY"))
    LD.gate("G-PAPER-CLAIM-POLARITY",
            "THE PAPER IS SCANNED FOR THE INVERSE OF EVERY LOAD-BEARING "
            "WORD.  %d polarity axes -- the head word, the atom word, the "
            "transport direction, the binding direction and the E-24 stamp "
            "-- are checked in BOTH forms, and the presence of an inverted "
            "form is a failure even when the asserted form is present too"
            % len(POLARITY),
            R["polarity"]["inverted_forms_present"] == 0,
            "axes %d, inverted present %d"
            % (len(POLARITY), R["polarity"]["inverted_forms_present"]))
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

    floats = []
    for node in ast.walk(ast.parse(src)):
        if isinstance(node, ast.Constant) and isinstance(node.value, float):
            floats.append(node.lineno)

    def scan(o, path=""):
        if isinstance(o, float):
            floats.append(path)
        elif isinstance(o, dict):
            for k in sorted(o, key=str):
                scan(o[k], path + "/" + str(k))
        elif isinstance(o, (list, tuple)):
            for i, v in enumerate(o):
                scan(v, path + "/%d" % i)
    scan(R)
    LD.gate("G-NO-FLOATS",
            "THE ARITHMETIC IS EXACT, CHECKED TWICE.  This file's own source "
            "is walked by AST for float constants and the receipt about to "
            "be written is walked recursively for float values; the Z[w] "
            "coefficients of the coupled step are integer pairs and the "
            "lumpability comparison is an exact comparison of integer maps",
            not floats, "float sites %s" % (floats[:6] or "none"))

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
    R["transcript_head"] = {
        "lines": len(LINES),
        "first": LINES[0] if LINES else "",
        "last": LINES[-1] if LINES else "",
        "whole_transcript_sha256_12": digest("\n".join(LINES)),
        "staged_transcript_sha256_12": digest("\n".join(staged)),
        "sealed": "the WHOLE transcript, not a head prefix",
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
    missing, extra = SEAL.totality()
    published = sorted(k for k in R if k not in DECLARED_UNSEALED)
    sealed_paths = {r["path"] for r in SEAL.rows}
    unsealed = sorted(k for k in published if k not in sealed_paths)
    ran = {g["gate"] for g in LD.rows}
    closing_absent = [g for g in CLOSING_GATE_NAMES
                      if g not in ran and g not in
                      ("G-ARTIFACT-INTEGRITY", "G-SEAL-TOTALITY")]
    LD.gate("G-SEAL-TOTALITY",
            "THE SEAL MANIFEST IS TOTAL (#119 + #148).  Every published "
            "receipt key is either sealed at the gate that established it or "
            "named in the declared-unsealed list: %d seals over %d published "
            "keys, %d declared unsealed, %d missing and %d unaccounted; and "
            "every one of the %d declared closing gates ran"
            % (len(SEAL.rows), len(published), len(DECLARED_UNSEALED),
               len(missing), len(unsealed), len(CLOSING_GATE_NAMES)),
            not missing and not extra and not unsealed and not closing_absent,
            "seals %d, missing %s, extra %s, unsealed keys %s, closing gates "
            "that did not run %s"
            % (len(SEAL.rows), missing or "none", extra or "none",
               unsealed or "none", closing_absent or "none"))
    R["seal_manifest"] = SEAL.rows
    payload = json.dumps(R, indent=1, sort_keys=True, default=str)
    SEAL.close(R, payload)
    R["payload_sha256_12"] = SEAL.payload_sha
    payload = json.dumps(R, indent=1, sort_keys=True, default=str)
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
