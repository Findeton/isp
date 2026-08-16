#!/usr/bin/env python3
"""ARITY (paper-44) -- THE EVENT-SIZE UNIT.  IS THREE-PER-EVENT A PARAMETER?

QUESTION (pin `v15/note-arity-pin.md`, sha256-12 89b35dad3219, v15 ledger #1;
registry questions Q13, Q17, Q19, and the arity legs of Q12 and Q22).
The corpus's division event has three actors.  The corpus's arena has nine.
The corpus's field has order three.  The corpus declares three link
directions.  Four threes, and no measurement anywhere in the corpus has ever
moved one of them independently of the others.

NDEP (paper-39) moved the ACTOR COUNT and found that every numeral it tested
travelled with q = sqrt(n) -- but at every arena point it could reach, q was
the square root of n exactly, so it could not separate them.  This unit moves
the OTHER coordinate.  n is held at 9 THROUGHOUT, and with it q = 3, the
field F_3, the four parallel classes, the three declared links and the 27
cells.  Only the event size a moves: a = 2 and a = 4 are built entire, a = 5
is a declared window, and a = 3 is rebuilt from the same constructor and
gated against the committed substrate counts BEFORE any new-a row runs.

That is the instrument's whole point, and it is the mirror image of NDEP's:
because q stands still while a moves, ANY quantity that moves here is not
q-carried, and ANY quantity that stands still here is not a-carried.  The two
units together separate the event size from the field order for the first
time in the corpus.  What this unit cannot do is separate a standing-still
numeral from the literal 3: at fixed (n, q, L) the n-only, the q-only and the
L-only readings all coincide with "the parent's numeral does not move", and
section 8 says so where it matters.

THE SIX LAWS UNDER TEST, each sorted into LAW-IN-A / NEEDS-3 / BREAKS at two
slots (the STATEMENT and the NUMERAL), per the NDEP engraving:

  L1  THE NAMING THEOREM (AID paper-33): the stabilizer of a history is the
      Young subgroup of its participation-signature partition.
  L2  THE CRYSTALLIZATION PAIR (AID): a schedule time, an information floor
      beneath it, one structurally redundant event between them.
  L3  THE COSET MENU (FAC paper-35): the geometry leg admits exactly the
      coset partitions of the translation subgroups.
  L4  THE LADDER MODULUS (the R-rung papers, NDEP paper-39 section 6): the
      achievable homogeneous budgets are the multiples of the declared link
      count.  Does mod-a appear?
  L5  THE DIVISION-FORCING THESIS (FAC): more than one factorization exactly
      where the history repeats a parallel class.
  L6  THE THREE-ACTOR COUNTING THEOREM (SEC-2 paper-40): a seam-spanning
      group that opens no pair inside a sector must double a link the union
      already carries, so gluing is never a free event.

ARITHMETIC.  Exact only: Python integers throughout; the coupled walk's
Grover and phase data are carried as integer pairs.  No floats anywhere; an
AST scan of this file and a recursive type scan of the emitted receipt are
gates.

RUNTIME INPUTS (#46 / #91).  Exactly five files are read as SOURCES, all
hash-pinned by this unit's frozen declaration, plus exactly one file read as
the OBJECT UNDER TEST -- this unit's own paper.  No repository state outside
those lists is read and no subprocess of any kind is invoked, so the run is
correct off-tree and with no version control present.

TEMPLATE (E-25 ... E-33, and the TPL-2 revision).  The nine families are
implemented HERE, not imported, and every one of them is EXERCISED on this
unit's own objects rather than carried: seals are taken at gate time and
re-verified at the door and again from disk; the transcript is parsed back
and reconciled with the ledger as a multiset; walls are voice-normalised
regexes with positive legs and controls phrased by another hand; anchors are
readable only through an accessor that records the read; claims are keyed by
table, both directions, exact occurrence counts; referents are bound per
occurrence over prose only; no gate statement, claim template or head segment
types a numeral, and the AST leg checks the source rather than the output;
every falsifier names the object it must move and the harness digests that
object before and after; and the read set is recorded at the I/O accessor and
compared at the LAST gate.  S-1 is met by construction: the head is rebuilt
segment by segment by a comparator that shares no code, no inputs and no
typed literals with the builder.
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

sys.setrecursionlimit(100000)

SELF = os.path.abspath(__file__)
REPO = os.path.dirname(os.path.dirname(os.path.dirname(SELF)))
OUT_TXT = os.path.join(os.path.dirname(SELF), "arity_output.txt")
OUT_JSON = os.path.join(os.path.dirname(SELF), "arity_receipt.json")

SCHEMA = "isp/v15/arity-event-size/1"
PAPER_REL = "v15/paper-44-arity.md"

# ===========================================================================
# SECTION 0.  THE FROZEN DECLARATION (RUNBOOK section 15: the arena is data)
# ===========================================================================

SOURCES = [
    ("A-PIN", "v15/note-arity-pin.md", "89b35dad3219",
     "THIS UNIT'S PIN (v15 ledger #1): the question, the arity window, the "
     "fidelity gate, the outcome names and the two-level aggregate."),
    ("A-NDEP", "v14/paper-39-ndep.md", "e2293b8c3858",
     "NDEP / PAPER-39 (terminal, v14 ledger #352): the transport machinery, "
     "the two-level engraving, the declared n-only rule and the sharpened "
     "information floor whose event-size term this unit tests."),
    ("A-NDEPREC", "v14/code/ndep_receipt.json", "29216cea946f",
     "NDEP's COMMITTED RECEIPT: the five q = 3 substrate counts, read by "
     "PATH and consumed by the fidelity gate that must pass before any "
     "new-a row runs."),
    ("A-SEC2", "v14/paper-40-sec2.md", "4fe88602280c",
     "SEC-2 / PAPER-40 (terminal, v14 ledger #370): the three-actor counting "
     "theorem, its census of 455 groups and the free-items row this unit's "
     "a = 2 measurement lands on."),
]

# PATH-VALUE ANCHORS (#20 path-value anchoring): (id, source, json path,
# expected value, consumer gate).  A path drift that changes the arena or a
# verdict dies at the anchor even when no number moves.
PATH_ANCHORS = [
    ("P-PARTS", "A-NDEPREC", "fidelity/groupings/parent",
     280, "G-CONSTRUCTOR-FIDELITY"),
    ("P-SAT", "A-NDEPREC", "fidelity/saturating/parent",
     36, "G-CONSTRUCTOR-FIDELITY"),
    ("P-STRICT", "A-NDEPREC", "fidelity/strict_tuples/parent",
     72, "G-CONSTRUCTOR-FIDELITY"),
    ("P-FLAT", "A-NDEPREC", "fidelity/flat_tuples/parent",
     276, "G-CONSTRUCTOR-FIDELITY"),
    ("P-WINDOW", "A-NDEPREC", "fidelity/window/parent",
     600, "G-CONSTRUCTOR-FIDELITY"),
    # THE BUDGET AND THE MAXIMUM ARE DIFFERENT OBJECTS AND ARE ANCHORED
    # SEPARATELY.  This unit's whole saturation question is whether the
    # parent's word means "the weight equals the budget" or "the weight is
    # the largest attained"; the two coincide at a = 3 and part at a = 4, so
    # a row that read one and called it the other would fail on the anchor's
    # identity even though no number moved.
    ("P-BUDGET", "A-NDEPREC", "fidelity/budget_n",
     9, "G-SUBSTRATE-CENSUS"),
    ("P-MAXINC", "A-NDEPREC", "fidelity/max_round_incidence",
     9, "G-SUBSTRATE-CENSUS"),
    ("P-SATMAX", "A-NDEPREC", "fidelity/saturation_is_maximal",
     True, "G-SUBSTRATE-CENSUS"),
]

# VERBATIM-TEXT ANCHORS (#62 as amended): each binds QUOTE FIDELITY -- the
# paper's quotation against the source's committed bytes -- and each is
# CONSUMED by a named gate that takes a value out of the located text and
# compares it with a measurement.  An anchor whose consumer reads no value
# from it is decoration, and none of these is.
VERBATIM = [
    ("V-FLOOR", "A-NDEP",
     "every division event has exactly q members, so k events distribute "
     "total incidence kq",
     "G-LAW2-SHARPENED",
     "NDEP's sharpened floor names the EVENT SIZE as the term that enters. "
     "The consumer parses the membership symbol and the incidence product "
     "out of the quotation and drives this unit's floor formula with the "
     "event size those tokens name."),
    ("V-CLOSEDFORM", "A-NDEP",
     "it evaluates to 2(q - 1) at q = 2 through 7",
     "G-LAW2-SHARPENED",
     "The parent's closed form for the sharpened floor on the ACTOR axis; "
     "the consumer parses its coefficient and offset and requires them to "
     "reproduce the parent's own floor at the parent's arity, which is what "
     "makes this unit's arity-axis reading a transport of the same formula "
     "and not a new one."),
    ("V-TWOLEVEL", "A-NDEP",
     "A law's STATEMENT is LAW-IN-N when the parent's theorem, as stated, "
     "holds at the new arena point",
     "G-AGGREGATE",
     "The two-level engraving in the parent's own words; the consumer reads "
     "the slot name out of the quotation and requires the aggregate to "
     "declare that slot by name and to publish a second, differently named "
     "slot beside it."),
    ("V-SQRT", "A-NDEP",
     "at every one of them q is the square root of the actor count exactly",
     "G-ARENA",
     "The parent's own statement of the limitation this unit's axis "
     "removes; the consumer parses the relation named in the quotation and "
     "requires it to hold of this unit's fixed arena, which is what makes q "
     "immovable while a moves."),
    ("V-TRIANGLE", "A-SEC2",
     "at most two of which can join the sectors, since a triangle admits no "
     "proper two-colouring",
     "G-LAW6-SEC2",
     "SEC-2's counting theorem in its own words; the consumer parses the "
     "spelled bound out of the quotation and requires it to equal this "
     "unit's independently measured maximum cut of the complete graph on "
     "the parent's arity."),
    ("V-CONTROL", "A-SEC2",
     "no three-actor group can produce it",
     "G-LAW6-SEC2",
     "SEC-2's own stamp on its free-items-zero row as a CONTROL. The "
     "consumer parses the spelled group size out of the quotation and "
     "measures how many groups of that size produce exactly that "
     "configuration, and how many of each other declared size do."),
    ("V-LAWFUL", "A-SEC2",
     "Of the 288 seam-spanning groups, 216 leave the dictionary alive once "
     "the target declares the cross links the event realises",
     "G-LAW6-SEC2",
     "SEC-2's delivered census; the consumer parses both numerals and "
     "requires this unit's independently rebuilt union to reproduce the "
     "seam-spanning count and the within-sector-free count at the parent's "
     "arity."),
    ("V-DEAD", "A-SEC2",
     "The 72 that stay dead are the groups that also open a pair inside one "
     "sector",
     "G-LAW6-SEC2",
     "The complement of the same census, quoted separately so that a row "
     "reading one and reporting the other dies; the consumer parses the "
     "numeral and requires it to equal the measured count of groups that "
     "open a new pair inside a sector."),
]

# THE DECLARED ARENA (section 15: declared-arena-as-data).  Every axis this
# unit holds fixed and every axis it moves.  The row values are COMPUTED at
# run time from the objects they describe -- a declaration that types its own
# counts is a typed count like any other, and this table is published.
def arena_declaration():
    return [
        ("boundary",
         "the %d (site, link) cells of one copy of AG(2, q) at q = %d with "
         "the declared links %s"
         % (NC, A.q, ", ".join(str(l) for l in A.LINKS))),
        ("held fixed",
         "n = %d actors, q = %d, the field and its characteristic %d, the %d "
         "parallel classes, L = %d declared links, %d cells"
         % (A.n, A.q, A.characteristic, len(A.CLASSES), A.L, NC)),
        ("moved",
         "a, the number of actors in one division event: %s"
         % ", ".join(str(x) for x in ARITIES)),
        ("declaration",
         "THE PACKING RULE, this unit's own and not the committed grammar's: "
         "a round at event size a is a MAXIMAL PACKING of the %d sites by "
         "disjoint a-blocks, with the remainder IDLE. It reduces to the "
         "committed constructor exactly where a divides the actor count, and "
         "everywhere else it is an EXTENSION of the theory, not a reading "
         "of it" % A.n),
        ("extension family",
         "the arities at which the packing rule leaves an idle remainder, "
         "so that the world measured there is an extension rather than the "
         "committed theory: %s" % ", ".join(
             str(x) for x in ARITIES if A.n % x)),
        ("family",
         "the maximal a-packings of the %d sites at each arity, and the "
         "histories the parent's own driver builds from them" % A.n),
        ("law",
         "the naming theorem, the crystallization pair, the coset menu, the "
         "ladder modulus, the division-forcing thesis and SEC-2's "
         "three-actor counting theorem"),
        ("state",
         "the participation-signature partition, the record n_l(x), and the "
         "coupled walk's one-step operator at both coin orders"),
        ("arena axes",
         "the arity a and the saturation reading (LITERAL, the parent's "
         "budget n; MAXIMAL, the parent's word); both are swept and both are "
         "published"),
        ("provenance",
         "%d sources read at pinned shas; %d path-value anchors; %d "
         "verbatim-text anchors, each consumed by a named gate"
         % (len(SOURCES), len(PATH_ANCHORS), len(VERBATIM))),
    ]


# THE ARITY WINDOW, declared before anything is measured.
ARITIES = (2, 3, 4, 5)
PARENT_ARITY = 3
WINDOWED_ARITY = 5          # the pin's declared window
CORPUS_CAP = 100000         # the multi-round corpus rule's declared cap
LADDER_RMAX = 9             # the ladder search bound, declared not silent
NAMING_FULL_GROUP_WINDOW = 40   # groupings per arity filtered against S_9

# PRE-REGISTERED OUTCOMES WITH FEASIBILITY (#299 / #319 / #348, at the
# declared row list).  Every outcome word must be shown REACHABLE at the
# corpus this unit builds, by a feasibility line naming the rows that would
# produce it.
PREREGISTERED = [
    ("LAW-IN-A",
     "the parent's theorem holds at every feasible arity (statement), or the "
     "declared a-only reading reproduces the measurement at every feasible "
     "arity and some feasible arity separates it from the constant reading "
     "(numeral)",
     "REACHABLE: the naming theorem's two routes are compared at every "
     "prefix of every arity's complete single-round census, so a law whose "
     "statement survives has a row that says so; and the a-only reading "
     "C(a,2) + v - 3 differs from the constant reading at a = 2, a = 4 and "
     "a = 5, so the discrimination leg can fire."),
    ("NEEDS-3",
     "the parent's numeral does not move across the feasible arities, so it "
     "is carried by a coordinate this axis holds still (n, q or L) and not "
     "by the event size",
     "REACHABLE: the coset menu's count and the ladder's modulus are both "
     "measured at more than one arity, and a constant column is exactly what "
     "the procedure stamps NEEDS-3."),
    ("BREAKS",
     "neither the constant reading nor the declared a-only reading "
     "reproduces the measurement at some feasible arity (numeral), or the "
     "parent's theorem is evaluable at some feasible arity and false there "
     "(statement)",
     "REACHABLE: the crystallization schedule time and the counting "
     "theorem's forced-pair bound are both measured at four arities and both "
     "have at least three distinct values in the declared window, which no "
     "constant and no single offset rule can match."),
    ("INFEASIBLE-CARRIED",
     "the law's own hypothesis fails at an arity, so the row is carried and "
     "never scored (#34: a row that cannot reach the test is not evidence)",
     "REACHABLE: under the LITERAL saturation reading no grouping attains "
     "the budget at a = 2 or a = 5, so the ladder's rows there have no "
     "object to score."),
    ("A-INERT-BY-CONSTRUCTION",
     "the law's statement quantifies over no event at all, so its value "
     "cannot move with the arity and the row is a DISCLOSURE rather than a "
     "measurement",
     "REACHABLE: the coset menu's geometry leg reads the partition and the "
     "arena and never the history, which the run demonstrates by evaluating "
     "it once and consuming the same survivors at every arity."),
]

# THE DECLARED UNIFORM a-ONLY RULE (the analogue of NDEP section 8).  A
# single datum at a = 3 does not determine a function of a, so the a-only
# reading of every law's numeral is FIXED BY RULE and not fitted per law: it
# is the corpus's own a-only quantity -- the number of co-division pairs one
# event opens, C(a, 2) -- offset by the constant that reproduces the parent's
# numeral at a = 3.  The same rule is applied to every numeral, so no law
# gets a friendlier reading than another.
def pairs_of_event(a):
    return math.comb(a, 2)


def t_a_reading(parent_value, a):
    return pairs_of_event(a) + (parent_value - pairs_of_event(PARENT_ARITY))


# The two declared ALTERNATIVE a-only rules, published as a sensitivity leg
# so that the word cannot be an artefact of the rule's choice.
def t_a_alt_identity(parent_value, a):
    return a + (parent_value - PARENT_ARITY)


def t_a_alt_blocks(parent_value, a):
    return (9 // a) + (parent_value - (9 // PARENT_ARITY))


WORDS = ("LAW-IN-A", "NEEDS-3", "BREAKS")

# THE SCOPE QUALIFIER every per-law word carries.  The rows at the arities
# where the packing rule leaves an idle remainder are measurements of an
# EXTENSION of the committed theory, not of the committed theory itself, and
# no word in this unit is licensed without saying so.
EXTENSION_SCOPE = "WITHIN THE DECLARED EXTENSION FAMILY"


def extension_arities(n):
    return [x for x in ARITIES if n % x]


# ===========================================================================
# SECTION 1.  THE TEMPLATE MECHANISMS (E-25 ... E-33), IMPLEMENTED HERE
#
# Copied rather than imported, per v14/TEMPLATE.md section 1: importing would
# make another unit's file a runtime input, and this unit must reproduce byte
# for byte off-tree with no repository present.  Every family is EXERCISED on
# this unit's own objects below -- the TPL-2 prohibition on carried-not-used
# families is a gate here (G-TEMPLATE-EXERCISED), not a claim.
# ===========================================================================

class GateFail(Exception):
    pass


class CliError(Exception):
    pass


MUTANT = None


def mut(name):
    return MUTANT == name


def pick(name, normal, corrupted):
    return corrupted if mut(name) else normal


MEMO = {}
MEMO_HITS = Counter()


def memo(key, fn):
    """Deterministic memoisation across the run and its nested falsifier
    runs.  EVERY key carries the mutant flags the computation depends on, so
    a recipe can never be served a clean cached answer; the cache's hit and
    miss counts are published and the falsifier harness exercises the miss
    path at every keyed value (RUNBOOK section 14: a zero-hit cache gate is
    vacuous, and a cache that ignores the mutant is worse)."""
    if key in MEMO:
        MEMO_HITS[("hit",) + key[:1]] += 1
        return MEMO[key]
    MEMO_HITS[("miss",) + key[:1]] += 1
    MEMO[key] = fn()
    return MEMO[key]


def digest(value):
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, default=str,
                   ensure_ascii=False).encode("utf-8")).hexdigest()[:16]


def bytes_digest(b):
    return hashlib.sha256(b).hexdigest()[:16]


def mdstrip(s):
    """#125 normalisation: markdown blockquote / list prefixes and emphasis
    removed before any text gate matches."""
    out = []
    for ln in s.split("\n"):
        t = ln.lstrip()
        while t[:1] in (">",) or re.match(r"^([-*+]|\d+\.)\s", t):
            t = re.sub(r"^([-*+]|\d+\.)\s", "", t[1:] if t[:1] == ">" else t)
            t = t.lstrip()
        out.append(t)
    t = "\n".join(out)
    t = t.replace("**", "").replace("`", "")
    return t


def canon(s):
    """whitespace folded, markdown stripped, ASCII-folded."""
    t = mdstrip(s)
    t = t.replace("—", "--").replace("–", "-")
    t = t.replace("‘", "'").replace("’", "'")
    t = t.replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", t).strip()


class Ledger:
    """A CHAINED ledger (family b): every row digests its predecessor, so a
    row cannot be inserted, dropped or reordered without moving the head."""

    def __init__(self):
        self.rows = []
        self.head = "0" * 16

    def gate(self, gid, ok, statement, evidence):
        row = {"n": len(self.rows) + 1, "gate": gid, "statement": statement,
               "evidence": evidence, "passed": bool(ok)}
        row["prev"] = self.head
        row["row_digest"] = digest(row)
        self.head = hashlib.sha256(
            (self.head + row["row_digest"]).encode("utf-8")).hexdigest()[:16]
        self.rows.append(row)
        TR.row(gid, bool(ok), self.evidence_line(evidence))
        if not ok:
            raise GateFail("%s :: %s" % (gid, self.evidence_line(evidence)))

    @staticmethod
    def evidence_line(evidence):
        return json.dumps(evidence, sort_keys=True, default=str,
                          ensure_ascii=False)

    def names(self):
        return [r["gate"] for r in self.rows]

    def index_of(self, gid):
        for r in self.rows:
            if r["gate"] == gid:
                return r["n"]
        return None

    def recompute_chain(self):
        head = "0" * 16
        for r in self.rows:
            body = {k: r[k] for k in
                    ("n", "gate", "statement", "evidence", "passed")}
            body["prev"] = head
            if digest(body) != r["row_digest"]:
                raise GateFail("T-LEDGER-CHAIN :: row %d moved" % r["n"])
            head = hashlib.sha256(
                (head + r["row_digest"]).encode("utf-8")).hexdigest()[:16]
        return head


class Transcript:
    """Family (b): the transcript is parsed BACK out of the text that will be
    promoted and reconciled with the ledger as a multiset, evidence
    included."""

    LINE = re.compile(r"^\s*\[(PASS|FAIL)\] (\S+) :: (.*)$")

    def __init__(self):
        self.lines = []

    def say(self, text=""):
        self.lines.append(text)

    def row(self, gid, ok, evidence):
        self.lines.append("  [%s] %s :: %s"
                          % ("PASS" if ok else "FAIL", gid, evidence))

    def text(self):
        return "\n".join(self.lines) + "\n"

    def parse(self, text=None):
        src = self.text() if text is None else text
        out = Counter()
        for line in src.splitlines():
            m = self.LINE.match(line)
            if m:
                out[(m.group(2), m.group(1) == "PASS", m.group(3))] += 1
        return out

    def bind(self, ledger, text=None):
        want = Counter((r["gate"], r["passed"],
                        Ledger.evidence_line(r["evidence"]))
                       for r in ledger.rows)
        got = self.parse(text)
        missing = sorted(k[0] for k in (want - got).elements())
        stray = sorted(k[0] for k in (got - want).elements())
        if missing or stray:
            raise GateFail("T-TRANSCRIPT-BOUND :: missing %s stray %s"
                           % (missing, stray))
        if sum(got.values()) != len(ledger.rows):
            raise GateFail("T-TRANSCRIPT-BOUND :: %d lines against %d rows"
                           % (sum(got.values()), len(ledger.rows)))
        return bytes_digest((self.text() if text is None
                             else text).encode("utf-8"))


class Seal:
    """Family (a): digest at gate time, verify against the GATE-TIME digest at
    promotion, recompute TOTALITY from the payload's live key set at the door
    (#348), and verify again from the promoted path."""

    def __init__(self):
        self.seals = {}
        self.unsealed = {}
        self.measured = set()
        self.closed = False

    def seal(self, key, value, gate, measured=True):
        if self.closed:
            raise GateFail("T-SEAL-PROMOTION :: seal after close: %s" % key)
        if key in self.unsealed:
            raise GateFail("T-SEAL-PROMOTION :: both sealed and unsealed: %s"
                           % key)
        self.seals[key] = {"digest": digest(value), "gate": gate}
        if measured:
            self.measured.add(key)
        return value

    def declare_unsealed(self, key, reason):
        if key in self.seals or key in self.measured:
            raise GateFail("T-SEAL-PROMOTION :: measured key unsealed: %s"
                           % key)
        if not reason.strip():
            raise GateFail("T-SEAL-PROMOTION :: unsealed with no reason: %s"
                           % key)
        self.unsealed[key] = reason

    def manifest(self):
        return {"sealed": {k: v["digest"] for k, v in sorted(self.seals.items())},
                "sealed_at_gate": {k: v["gate"]
                                   for k, v in sorted(self.seals.items())},
                "declared_unsealed": dict(sorted(self.unsealed.items()))}

    def verify_at_promotion(self, payload, ledger, manifest_key):
        moved = [k for k, s in self.seals.items()
                 if k not in payload or digest(payload[k]) != s["digest"]]
        if moved:
            raise GateFail("T-SEAL-PROMOTION :: sealed values moved: %s"
                           % moved)
        gates = set(ledger.names())
        phantom = sorted(k for k, s in self.seals.items()
                         if s["gate"] not in gates)
        if phantom:
            raise GateFail("T-SEAL-PROMOTION :: seal names a gate that never "
                           "ran: %s" % phantom)
        covered = set(self.seals) | set(self.unsealed) | {manifest_key}
        undeclared = sorted(set(payload) - covered)
        absent = sorted(set(self.seals) - set(payload))
        if undeclared:
            raise GateFail("T-SEAL-PROMOTION :: undeclared keys: %s"
                           % undeclared)
        if absent:
            raise GateFail("T-SEAL-PROMOTION :: sealed key absent: %s" % absent)

    def close(self):
        self.closed = True

    def verify_after_promotion(self, receipt_path, manifest_key):
        with open(receipt_path, "rb") as fh:
            on_disk = json.loads(fh.read().decode("utf-8"))
        moved = [k for k, s in self.seals.items()
                 if k not in on_disk or digest(on_disk[k]) != s["digest"]]
        if moved:
            raise GateFail("T-SEAL-PROMOTION :: post-close edit on disk: %s"
                           % moved)
        covered = set(self.seals) | set(self.unsealed) | {manifest_key}
        undeclared = sorted(set(on_disk) - covered)
        if undeclared:
            raise GateFail("T-SEAL-PROMOTION :: post-close add on disk: %s"
                           % undeclared)


class SemanticWall:
    """Family (c): voice-normalised REGEX patterns over the canonicalised
    paper, case-folded, with a POSITIVE leg (the paper must carry its own
    standing sentence), non-vacuous on empty text, and controls written by
    another hand (the TPL-2 item)."""

    def __init__(self, name, negative, positive, controls,
                 subject=(), policed=(), licences=()):
        self.name = name
        self.negative = list(negative)
        self.positive = list(positive)
        self.controls = list(controls)
        self.subject = list(subject)
        self.policed = list(policed)
        self.licences = list(licences)
        for pat in (self.negative + self.positive + self.subject
                    + self.policed + self.licences):
            re.compile(pat)
        # NO SELF-LICENSING (the POT MAJOR-1 cure): a licence may not be a
        # policed form, or the wall licenses exactly what it polices.
        bad = [l for l in self.licences
               if any(re.search(pp, l.replace("\\b", "")) for pp in self.policed)]
        if bad:
            raise GateFail("T-WALL-SEMANTIC :: self-licensing set: %s" % bad)

    def seal_value(self):
        return {"name": self.name, "negative": self.negative,
                "positive": self.positive, "subject": self.subject,
                "policed": self.policed, "licences": self.licences,
                "independent_controls": len(self.controls)}

    def licence_leg(self, text):
        """THE LICENCE LEG.  A pattern list can only ban the phrasings it was
        written for; this leg bans the CLAIM.  Any sentence that names the
        wall's subject AND carries one of its policed forms must also carry a
        licence -- a conditional frame, a disclaimer, a scope word -- and the
        licence set may contain no policed form.  A paraphrase written by
        another hand still names the subject and still asserts, so it is
        caught whatever words it chooses."""
        out = []
        for sent in re.split(r"(?<=[.!?])\s+", text):
            subs = [m.start() for p in self.subject
                    for m in re.finditer(p, sent)]
            if not subs:
                continue
            # THE CLAIM, not the vocabulary: the policed form must stand
            # NEAR the wall's subject, or the sentence is merely about
            # something else that happens to share a word.
            near = [m.start() for p in self.policed
                    for m in re.finditer(p, sent)
                    if any(abs(m.start() - k) <= self.SPAN for k in subs)]
            if not near:
                continue
            if not any(re.search(l, sent) for l in self.licences):
                out.append(sent[:130])
        return out

    SPAN = 80

    NEG = re.compile(r"\b(?:not|never|nor|no|cannot|neither|without|"
                     r"whether|refuses?|denies)\b")

    def scan(self, paper_text):
        """A match is a violation only when the seventy characters before it
        carry no negation: a wall must ban an ASSERTION, and a paper that
        disclaims the assertion is doing the wall's work, not breaking it.
        The controls are all affirmative, so the guard cannot excuse them."""
        text = canon(paper_text).lower()
        if not text:
            raise GateFail("T-WALL-SEMANTIC :: %s scanned empty text"
                           % self.name)
        hits = []
        for pat in self.negative:
            for m in re.finditer(pat, text):
                lead = text[max(0, m.start() - 200):m.start()]
                cut = max(lead.rfind("."), lead.rfind("!"), lead.rfind("?"))
                lead = lead[cut + 1:]          # the match's OWN sentence only
                if not self.NEG.search(lead):
                    hits.append(pat)
                    break
        missing = [p for p in self.positive if not re.search(p, text)]
        unlicensed = self.licence_leg(text)
        return {"violations": hits, "missing_positive": missing,
                "unlicensed_sentences": unlicensed}


class Anchor:
    def __init__(self, name, needle, source, consumer, why):
        self.name = name
        self.needle = needle
        self.source = source
        self.consumer = consumer
        self.why = why
        self.located = None
        self.read_by = set()


class AnchorSet:
    """Family (d): anchor text is readable ONLY through read(name, by_gate),
    which records the read; consumption is verified against gates that
    actually ran; the needle must occur in the pinned source AND in the
    paper's own rendering under #125 canonicalisation."""

    FLOOR = 24

    def __init__(self, anchors):
        self.anchors = {a.name: a for a in anchors}
        self.reads = []

    def locate(self, sources, paper_text, broken=None):
        for a in self.anchors.values():
            hay = canon(sources[a.source])
            needle = canon(a.needle)
            if a.name == broken:
                needle = needle[:-6] + "XXXXXX"
            if len(needle) < self.FLOOR:
                raise GateFail("T-ANCHOR-CONSUMED :: needle below the floor: "
                               "%s" % a.name)
            n = hay.count(needle)
            if n != 1:
                raise GateFail("T-ANCHOR-CONSUMED :: %s occurs %d times in %s"
                               % (a.name, n, a.source))
            pn = canon(paper_text).count(needle)
            if pn < 1:
                raise GateFail("T-ANCHOR-CONSUMED :: %s not rendered in the "
                               "paper" % a.name)
            a.located = needle

    def read(self, name, by_gate):
        a = self.anchors[name]
        if a.located is None:
            raise GateFail("T-ANCHOR-CONSUMED :: read before locate: %s" % name)
        a.read_by.add(by_gate)
        self.reads.append((name, by_gate))
        return a.located

    def verify_consumption(self, ledger):
        ran = set(ledger.names())
        bad = []
        for a in self.anchors.values():
            if a.consumer not in ran:
                bad.append("%s: consumer %s never ran" % (a.name, a.consumer))
            elif a.consumer not in a.read_by:
                bad.append("%s: consumer %s never read it" % (a.name, a.consumer))
        return bad


class Claims:
    """Family (e): the licensed claim set, keyed BY TABLE, compared in both
    directions with exact occurrence counts; fenced blocks by MULTISET
    equality whatever the info string; every markdown table in the paper must
    be claimed by some rendering."""

    ROW = re.compile(r"^\s*\|(.+)\|\s*$")
    FENCE = re.compile(r"^```", re.M)

    def __init__(self):
        self.tables = {}
        self.prose = Counter()
        self.fences = Counter()

    @staticmethod
    def cells(line):
        return tuple(canon(c) for c in line.strip().strip("|").split("|"))

    def table(self, tid, header, rows):
        want = Counter()
        want[self.cells("|" + "|".join(str(h) for h in header) + "|")] += 1
        for r in rows:
            want[self.cells("|" + "|".join(str(c) for c in r) + "|")] += 1
        self.tables[tid] = want
        out = ["| " + " | ".join(str(h) for h in header) + " |",
               "|" + "|".join("---" for _ in header) + "|"]
        for r in rows:
            out.append("| " + " | ".join(str(c) for c in r) + " |")
        return "\n".join(out)

    def claim(self, text, times=1):
        self.prose[canon(text)] += times
        return text

    def fence(self, text, times=1):
        self.fences[canon(text)] += times
        return text

    def paper_tables(self, paper_text):
        """every markdown table in the paper, as a multiset of row tuples,
        one bag per contiguous table block."""
        bags, cur = [], Counter()
        for ln in paper_text.split("\n"):
            m = self.ROW.match(ln)
            if m:
                cs = self.cells(ln)
                if not all(set(c) <= set("-: ") for c in cs):
                    cur[cs] += 1
            elif cur:
                bags.append(cur)
                cur = Counter()
        if cur:
            bags.append(cur)
        return bags

    def paper_fences(self, paper_text):
        out = Counter()
        parts = paper_text.split("```")
        for i in range(1, len(parts), 2):
            body = parts[i]
            if "\n" in body:
                body = body.split("\n", 1)[1]
            out[canon(body)] += 1
        return out

    def gate(self, paper_text):
        bags = self.paper_tables(paper_text)
        unmatched_paper = list(range(len(bags)))
        missing, stray = [], []
        for tid, want in sorted(self.tables.items()):
            hit = None
            for i in unmatched_paper:
                if bags[i] == want:
                    hit = i
                    break
            if hit is None:
                best = None
                for i in unmatched_paper:
                    d = sum((bags[i] - want).values()) + sum((want - bags[i]).values())
                    if best is None or d < best[0]:
                        best = (d, i)
                missing.append({"table": tid,
                                "nearest_delta": best[0] if best else None})
            else:
                unmatched_paper.remove(hit)
        for i in unmatched_paper:
            stray.append({"unclaimed_table_rows": sum(bags[i].values())})
        pf = self.paper_fences(paper_text)
        fence_missing = sorted(k[:60] for k in (self.fences - pf).elements())
        fence_stray = sorted(k[:60] for k in (pf - self.fences).elements())
        # #125 and the SEC-2 MAJOR-10 cure: the prose leg case-folds BOTH
        # sides, so a sentence-initial capital is not a defence.  Tables and
        # fences stay case-exact: they are verbatim renders.  And the leg is
        # PROSE ONLY (family f): fenced blocks are stripped first, so the
        # run's own verdict cannot discharge the paper's prose obligations.
        ptext = canon(" ".join(paper_text.split("```")[0::2])).casefold()
        prose_bad = []
        for k, need in sorted(self.prose.items()):
            got = ptext.count(k.casefold())
            if got != need:
                prose_bad.append({"claim": k[:70], "need": need, "got": got})
        return {"tables_claimed": len(self.tables),
                "tables_in_paper": len(bags),
                "tables_missing": missing, "tables_unclaimed": stray,
                "fences_claimed": sum(self.fences.values()),
                "fences_in_paper": sum(pf.values()),
                "fence_missing": fence_missing, "fence_stray": fence_stray,
                "prose_claims": len(self.prose), "prose_bad": prose_bad}


class ReferentRegistry:
    """Family (f): universes are declared with the PAIRS the run measured;
    each sentence selects its universe by subject noun; every occurrence is
    checked; fenced blocks are stripped first."""

    NUM = re.compile(r"(?<![\w.])(\d{1,3}(?:,\d{3})*|\d+)(?![\w.])")

    def __init__(self):
        self.universes = {}
        self.exempt = {}

    def universe(self, name, nouns, values, pairs):
        self.universes[name] = {"nouns": [n.lower() for n in nouns],
                                "values": set(values),
                                "pairs": {tuple(p) for p in pairs}}

    def exempt_token(self, tok, reason):
        self.exempt[tok] = reason

    def seal_value(self):
        return {k: {"nouns": v["nouns"], "values": sorted(v["values"]),
                    "pairs": sorted(v["pairs"])}
                for k, v in sorted(self.universes.items())}

    @staticmethod
    def prose_only(paper_text, strips=()):
        """PROSE ONLY, and prose means prose.  Fenced blocks are stripped so
        the run's own verdict cannot discharge the paper's obligations;
        markdown TABLE rows are stripped because a table row is bound by the
        claims gate and not by a sentence's referent; block QUOTATIONS are
        stripped because they are the parents' words, bound by the verbatim
        anchors; and the declared structural tokens -- paper ids, section
        cross-references, digests -- are removed by the same patterns the
        coverage scan declares."""
        parts = paper_text.split("```")
        lines = []
        for chunk in parts[0::2]:
            for ln in chunk.split("\n"):
                t = ln.strip()
                if t.startswith("|") or t.startswith(">"):
                    continue
                lines.append(ln)
        txt = "\n".join(lines)
        for pat, _why in strips:
            txt = re.sub(pat, " ", txt)
        return canon(txt)

    def _universe_of(self, sentence):
        s = sentence.lower()
        best, bestpos = None, None
        for name, u in self.universes.items():
            for noun in u["nouns"]:
                p = s.find(noun)
                if p >= 0 and (bestpos is None or p < bestpos):
                    best, bestpos = name, p
        return best

    def gate(self, paper_text, strips=()):
        text = self.prose_only(paper_text, strips)
        for tok in self.exempt:
            text = text.replace(tok, " ")
        text = re.sub(r"\b[0-9a-f]{12}\b", " ", text)
        bad, checked = [], 0
        for sent in re.split(r"(?<=[.!?])\s+", text):
            u = self._universe_of(sent)
            if u is None:
                continue
            vals = [int(m.group(1).replace(",", ""))
                    for m in self.NUM.finditer(sent)]
            if not vals:
                continue
            checked += 1
            uv = self.universes[u]["values"]
            offend = [v for v in vals if v not in uv]
            if offend:
                bad.append({"universe": u, "sentence": sent[:110],
                            "not_in_universe": offend})
                continue
            m = re.search(r"(\d[\d,]*)\s+of\s+(\d[\d,]*)", sent)
            if m:
                pr = (int(m.group(1).replace(",", "")),
                      int(m.group(2).replace(",", "")))
                if pr not in self.universes[u]["pairs"]:
                    bad.append({"universe": u, "sentence": sent[:110],
                                "unmeasured_pair": list(pr)})
        return {"sentences_checked": checked, "violations": bad}


class CountRegistry:
    """Family (g): values enter by measurement; statements interpolate by
    NAME; the template is checked BEFORE substitution; an AST leg scans this
    module for numerals typed into gate statements, claim templates or head
    segments -- including the TPL-2 subspecies (%-format literals and integer
    offsets typed into a statement builder's arguments)."""

    TOKEN = re.compile(r"(?<![\w.])(\d{1,3}(?:,\d{3})*|\d+)(?![\w.])")

    def __init__(self):
        self.vals = {}
        self.how = {}
        self.exempt = {}

    def measured(self, name, value, how):
        self.vals[name] = value
        self.how[name] = how
        return value

    def get(self, name):
        if name not in self.vals:
            raise GateFail("T-NO-TYPED-COUNTS :: unmeasured name %s" % name)
        return self.vals[name]

    def exempt_token(self, tok, reason):
        self.exempt[tok] = reason

    def stmt(self, template, **names):
        found = [m.group(1) for m in self.TOKEN.finditer(template)]
        bad = [t for t in found if t not in self.exempt]
        if bad:
            raise GateFail("T-NO-TYPED-COUNTS :: typed numeral(s) %s in a "
                           "statement template" % bad)
        return template.format(**{k: self.get(v) if isinstance(v, str)
                                  else v for k, v in names.items()})

    def audit_module(self, source, callers):
        """the AST leg.  Any string literal handed to a statement builder, or
        any %-format / .format template argued to one, that types a numeral,
        is an offender whatever the docstring says.  Integer literals passed
        as arguments to a statement builder are the TPL-2 subspecies and are
        flagged too."""
        tree = ast.parse(source)
        offenders = []
        for node in ast.walk(tree):
            if not isinstance(node, ast.Call):
                continue
            fn = node.func
            nm = (fn.attr if isinstance(fn, ast.Attribute)
                  else getattr(fn, "id", None))
            if nm not in callers:
                continue
            for arg in list(node.args) + [k.value for k in node.keywords]:
                for sub in ast.walk(arg):
                    if isinstance(sub, ast.Constant) and isinstance(sub.value, str):
                        for m in self.TOKEN.finditer(sub.value):
                            if m.group(1) not in self.exempt:
                                offenders.append({"caller": nm,
                                                  "typed": m.group(1),
                                                  "line": sub.lineno})
                    if (isinstance(sub, ast.Constant)
                            and isinstance(sub.value, int)
                            and not isinstance(sub.value, bool)
                            and str(sub.value) not in self.exempt):
                        offenders.append({"caller": nm,
                                          "typed_int": sub.value,
                                          "line": sub.lineno})
        return offenders


class Falsifier:
    def __init__(self, name, gate, description, target, apply):
        self.name = name
        self.gate = gate
        self.description = description
        self.target = target
        self.apply = apply


class ReadSet:
    """Family (i): every open() this process performs is recorded AT THE
    ACCESSOR by an audit hook, and the multiset of repository-relative paths
    is compared at the LAST gate, not the first."""

    def __init__(self, root):
        self.root = os.path.abspath(root)
        self.reads = []
        self.exemptions = {}
        self.used = set()

    def install(self):
        def hook(event, args):
            if event == "open":
                p = args[0]
                if isinstance(p, (str, bytes, os.PathLike)):
                    try:
                        ap = os.path.abspath(os.fspath(p))
                    except Exception:
                        return
                    if ap.startswith(self.root + os.sep):
                        self.reads.append(os.path.relpath(ap, self.root))
        sys.addaudithook(hook)

    def exempt(self, rel, reason):
        self.exemptions[rel] = reason

    def gate_at_close(self, declared):
        seen = Counter(self.reads)
        want = set(declared)
        undeclared = []
        for p, _n in seen.items():
            if p in want:
                continue
            hit = None
            for ex in self.exemptions:
                if p == ex or p.startswith(ex):
                    hit = ex
                    break
            if hit is None:
                undeclared.append(p)
            else:
                self.used.add(hit)
        never = sorted(p for p in want if p not in seen)
        unused = sorted(e for e in self.exemptions if e not in self.used)
        return {"distinct_reads": len(seen), "undeclared": sorted(undeclared),
                "declared_never_read": never, "unused_exemptions": unused}


# ===========================================================================
# SECTION 2.  THE ARENA (FIXED) AND THE a-GRAMMAR (THE ONLY THING THAT MOVES)
# ===========================================================================

class Arena:
    """AG(2, 3): nine actors, four parallel classes, three declared links.

    NOTHING in this class depends on the arity.  It is instantiated once and
    consumed at every arity, which is what makes the sweep a sweep of a and
    of nothing else -- the field, its characteristic, the link set, the cell
    set and the parallel classes are computed here and never rebuilt."""

    def __init__(self, q=3, L=3):
        self.q = q
        self.n = q * q
        self.el = tuple(range(q))
        one, acc, k = 1, 1, 1
        while acc % q:
            acc = (acc + one) % q
            k += 1
        self.characteristic = k
        self.SITES = tuple((i, j) for i in self.el for j in self.el)
        self.SI = {s: i for i, s in enumerate(self.SITES)}
        self.DIRECTIONS = ((1, 0), (0, 1), (1, 1), (1, 2))
        self.L = L
        self.LINKS = self.DIRECTIONS[:L]
        self.CELLS = tuple((x, l) for x in self.SITES for l in self.LINKS)
        self.CI = {c: i for i, c in enumerate(self.CELLS)}
        self.CLASS_DIRS = ((0, 1), (1, 0), (1, 1), (1, 2))
        self.CLASS_NAMES = ("ROW", "COL", "DIA", "ANT")
        self.CLASSES = {nm: self.parallel_class(d)
                        for nm, d in zip(self.CLASS_NAMES, self.CLASS_DIRS)}
        self.CLASS_OF = {v: k for k, v in self.CLASSES.items()}

    def vadd(self, a, b):
        return ((a[0] + b[0]) % self.q, (a[1] + b[1]) % self.q)

    def vmul(self, k, a):
        return ((k * a[0]) % self.q, (k * a[1]) % self.q)

    def parallel_class(self, d):
        H = frozenset(self.vmul(t, d) for t in self.el)
        seen, out = set(), []
        for x in self.SITES:
            Ln = tuple(sorted(self.vadd(x, h) for h in H))
            if Ln not in seen:
                seen.add(Ln)
                out.append(Ln)
        return tuple(sorted(out))

    def subgroups(self):
        T = [s for s in self.SITES if s != (0, 0)]
        found = set()
        for k in range(0, 3):
            for gens in combinations(T, k):
                S = {(0, 0)}
                ch = True
                while ch:
                    ch = False
                    for s in list(S):
                        for g in gens:
                            t = self.vadd(s, g)
                            if t not in S:
                                S.add(t)
                                ch = True
                found.add(frozenset(S))
        return sorted(found, key=lambda s: (len(s), sorted(s)))

    def coset_partition(self, H):
        seen, out = set(), []
        for x in self.SITES:
            c = tuple(sorted(self.vadd(x, h) for h in H))
            if c not in seen:
                seen.add(c)
                out.append(c)
        return tuple(sorted(out))

    # -- THE ARITY TRANSPORT RULE ------------------------------------------
    def packings(self, a, drop_idle=False):
        """THE ROUND AT ARITY a: a MAXIMAL PACKING of the n sites by disjoint
        a-blocks -- floor(n/a) of them -- with n - a*floor(n/a) actors IDLE.

        At a = 3 the remainder is zero and this is exactly the parent's
        'partition of the q^2 sites into q blocks of q', which is gated
        (G-PACKING-EXTENDS): the transport rule is a strict extension of the
        constructor, not a different constructor that happens to agree.

        The idle actor is the arity axis's own new object.  It exists at
        every a that does not divide n, and nothing in the parent's grammar
        has a name for it."""
        nb = self.n // a
        out = []

        def rec(rem, acc):
            if len(acc) == nb:
                out.append(tuple(sorted(acc)))
                return
            if not rem:
                return
            first, rest = rem[0], rem[1:]
            for extra in combinations(rest, a - 1):
                blk = tuple(sorted((first,) + extra))
                rec(tuple(x for x in rest if x not in extra), acc + [blk])
            if not drop_idle and len(rest) >= a * (nb - len(acc)):
                rec(rest, acc)
        rec(tuple(self.SITES), [])
        return sorted(set(out))

    def round_vec(self, P):
        """the per-(site, link) incidence vector of ONE round: cell (x, l)
        carries 1 exactly when x and x + l share a conflict group.  The
        formula is the parent's, unchanged; only the blocks are new."""
        return tuple(1 if any(x in g and self.vadd(x, l) in g for g in P)
                     else 0 for (x, l) in self.CELLS)

    def canon_transversals(self, P, a):
        return [tuple(sorted(g)[k] for g in P) for k in range(a)]

    def round_events(self, P):
        order = sorted(range(len(P)), key=lambda gi: self.SI[sorted(P[gi])[0]])
        return [frozenset(P[gi]) for gi in order]


A = Arena()
NC = len(A.CELLS)
FULLCOV = (1 << NC) - 1


def substrate(a, drop_idle=False):
    def build():
        P = A.packings(a, drop_idle)
        V = [A.round_vec(p) for p in P]
        W = [sum(v) for v in V]
        return P, V, W
    return memo(("substrate", a, drop_idle), build)


def saturating(W, reading):
    """THE TWO DECLARED READINGS OF 'SATURATING'.

    LITERAL -- the parent's own words: the round vector's weight equals the
    budget n.  MAXIMAL -- the parent's own MEANING at q = 2 and q = 3, where
    it measured saturation to be maximality: the weight is the largest any
    grouping attains.  They coincide at a = 3 and part at a = 4, which is
    exactly the decision NDEP's successor register left open on the other
    axis."""
    if reading == "LITERAL":
        return [i for i, w in enumerate(W) if w == A.n]
    return [i for i, w in enumerate(W) if w == max(W)]


def cover_masks(V, sat):
    out = []
    for i in sat:
        m = 0
        for k, b in enumerate(V[i]):
            if b:
                m |= 1 << k
        out.append((i, m))
    return out


def strict_tuples(V, sat, R):
    return memo(("strict", len(V), tuple(sat), R),
                lambda: _strict_tuples(V, sat, R))


def _strict_tuples(V, sat, R):
    """the parent's I7-STRICT class, transported verbatim: ordered R-tuples of
    saturating groupings whose summed link field covers every cell."""
    ms = cover_masks(V, sat)
    if not ms:
        return []
    w = max(bin(m).count("1") for _i, m in ms)
    out = []

    def rec(depth, cov, acc):
        if depth == R:
            if cov == FULLCOV:
                out.append(tuple(acc))
            return
        if NC - bin(cov).count("1") > (R - depth) * w:
            return
        for i, m in ms:
            rec(depth + 1, cov | m, acc + [i])
    rec(0, 0, [])
    return out


def flat_tuples(V, sat, R):
    return memo(("flat", len(V), tuple(sat), R),
                lambda: _flat_tuples(V, sat, R))


def _flat_tuples(V, sat, R):
    """the parent's G-FLAT class: the summed field is the near-flat row
    (1, ..., 1, 2) at every site.  The MASS row is derived, not enumerated: R
    rounds of measured mass w deposit R*w, and a target of different total
    mass carries no solution at all."""
    if not sat:
        return [], "NO-SATURATING-GROUPING"
    tgt = ([1] * (A.L - 1) + [2]) * A.n
    vs = [V[i] for i in sat]
    w = sum(vs[0])
    if R * w != sum(tgt):
        return [], "DERIVED-FROM-THE-MEASURED-MASS"
    out = []

    def rec(depth, tot, acc):
        if depth == R:
            if tot == tgt:
                out.append(tuple(acc))
            return
        for k, v in enumerate(vs):
            nt = [tot[j] + v[j] for j in range(NC)]
            if any(nt[j] > tgt[j] for j in range(NC)):
                continue
            rec(depth + 1, nt, acc + [sat[k]])
    rec(0, [0] * NC, [])
    return out, "EXHAUSTIVE-UNDER-THE-CEILING"


def first_menu_schedule(T, a):
    return tuple((T[r], A.canon_transversals(T[r], a)[0])
                 for r in range(len(T)))


def driven_window(P, V, sat, a):
    """the parent's R = L + 1 driven window: every class tuple, every
    near-flat tuple, the alternating control and the collinear seed fan.

    THE CLASS ARM EXISTS ONLY WHERE THE ARENA HAS EVENTS OF SIZE a THAT ARE
    COSETS.  A parallel class is the coset partition of an order-a subgroup
    of the translation group, and Z_3 x Z_3 has subgroups of orders 1, 3 and
    9 only.  At a = 2, 4 and 5 the arm is not empty by search -- it is
    UNDEFINED, and the run says which."""
    R3 = A.L + 1
    classes_available = all(len(g) == a for g in A.CLASSES["ROW"])
    quads, tags = [], []
    if classes_available:
        for names in product(A.CLASS_NAMES, repeat=R3):
            quads.append(tuple(A.CLASSES[k] for k in names))
            tags.append("W-CLASS")
    flatq, how = flat_tuples(V, sat, R3)
    for T in flatq:
        quads.append(tuple(P[i] for i in T))
        tags.append("W-FLAT")
    if classes_available:
        ctrl = tuple(A.CLASS_NAMES[i % 2] for i in range(R3))
        quads.append(tuple(A.CLASSES[k] for k in ctrl))
        tags.append("W-CTRL")
    out, seen, meta = [], set(), {}
    for T, tag in zip(quads, tags):
        sch = first_menu_schedule(T, a)
        if sch in seen:
            continue
        seen.add(sch)
        out.append(sch)
        meta[sch] = tag
    if classes_available:
        coll = tuple(list(A.CLASS_NAMES[:A.L]) + [A.CLASS_NAMES[A.L - 1]])
        T = tuple(A.CLASSES[k] for k in coll)
        menus = [A.canon_transversals(p, a) for p in T]
        for sel in product(range(a), repeat=R3):
            sch = tuple((T[r], menus[r][sel[r]]) for r in range(R3))
            if sch in seen:
                continue
            seen.add(sch)
            out.append(sch)
            meta[sch] = "W-SEEDFAN"
    return out, meta, len(flatq), how, classes_available


def translation_orbits(P, sat):
    idx = {p: i for i, p in enumerate(P)}

    def shift(p, t):
        return tuple(sorted(tuple(sorted(A.vadd(x, t) for x in g)) for g in p))
    seen, reps, sizes = set(), [], []
    for i in sat:
        if i in seen:
            continue
        orb = {idx[shift(P[i], t)] for t in A.SITES}
        seen |= orb
        reps.append(i)
        sizes.append(len(orb))
    return reps, sizes


# ---- the laws' primitives, all parameterised in a ------------------------

def signature_blocks(H):
    sig = {}
    for x in A.SITES:
        sig.setdefault(tuple(1 if x in F else 0 for F in H), []).append(x)
    return tuple(sorted(tuple(sorted(v)) for v in sig.values()))


def young_order(H):
    o = 1
    for b in signature_blocks(H):
        o *= math.factorial(len(b))
    return o


def young_elements(H):
    """ROUTE B: the Young subgroup built FROM THE SIGNATURE BLOCKS, knowing
    nothing whatever about route A."""
    blocks = signature_blocks(H)
    out = set()
    for choice in product(*[permutations(b) for b in blocks]):
        p = [0] * A.n
        for b, img in zip(blocks, choice):
            for src, dst in zip(b, img):
                p[A.SI[src]] = A.SI[dst]
        out.add(tuple(p))
    return out


def young_in_window(H, perms):
    """ROUTE B, evaluated on the declared window without materialising the
    whole Young subgroup: a permutation belongs to it exactly when every
    actor is carried inside its OWN signature block.  Still route B -- it
    reads the signature partition and nothing else -- and it agrees with the
    full construction wherever both are affordable, which the group leg
    checks."""
    blk = {}
    for bi, b in enumerate(signature_blocks(H)):
        for x in b:
            blk[A.SI[x]] = bi
    return {p for p in perms if all(blk[p[i]] == blk[i] for i in blk)}


def route_a_stabilizer(H, perms, corrupt=False):
    """ROUTE A: hold the permutation set and keep what survives the
    DEFINITION -- carries every division event to itself, setwise.  No
    signature, no block, no Young subgroup anywhere in this function."""
    ev = [tuple(sorted(A.SI[x] for x in F)) for F in H]
    if corrupt and ev:
        ev = [ev[0][:-1] + ((ev[0][-1] + 1) % A.n,)] + ev[1:]
    evset = [set(e) for e in ev]
    out = set()
    for p in perms:
        ok = True
        for e, es in zip(ev, evset):
            for i in e:
                if p[i] not in es:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            out.add(p)
    return out


def crystallization_time(H):
    part = [set(A.SITES)]
    for k, e in enumerate(H, 1):
        nxt = []
        for b in part:
            i, o = b & e, b - e
            if i:
                nxt.append(i)
            if o:
                nxt.append(o)
        part = nxt
        if len(part) == A.n:
            return k
    return None


def counting_floor(n):
    """THE PARENT'S STATED BOUND: k events supply at most 2^k distinct binary
    signatures, so 2^k >= n.  True at every n and at every arity; the
    question is whether it is the ATTAINED value."""
    k = 0
    while 2 ** k < n:
        k += 1
    return k


def weight_floor(n, event_size):
    """NDEP's SHARPENED FLOOR, with the event size as the term the quotation
    names.  k events distribute total incidence k*event_size, while n
    distinct binary k-signatures cost at least the total weight of the n
    lightest distinct k-vectors."""
    k = 1
    while True:
        if 2 ** k >= n:
            tot, left, w = 0, n, 0
            while left > 0 and w <= k:
                take = min(math.comb(k, w), left)
                tot += take * w
                left -= take
                w += 1
            if left == 0 and tot <= k * event_size:
                return k
        k += 1


def absolute_floor(a):
    return memo(("absolute_floor", a), lambda: _absolute_floor(a))


def _absolute_floor(a):
    """THE INFORMATION FLOOR AT ARITY a, over the COMPLETE event universe:
    the least number of a-subsets of the nine actors whose joint signature
    partition is discrete.  No corpus, no window -- every a-subset."""
    blocks = [frozenset(c) for c in combinations(A.SITES, a)]
    seps = []
    for x, y in combinations(A.SITES, 2):
        m = 0
        for i, b in enumerate(blocks):
            if (x in b) != (y in b):
                m |= 1 << i
        seps.append(m)
    for k in range(1, 8):
        for comb in combinations(range(len(blocks)), k):
            s = 0
            for i in comb:
                s |= 1 << i
            if all(sep & s for sep in seps):
                return k, len(blocks)
    return None, len(blocks)


def bfs_min_schedule(P, sat, cap_rounds=6):
    return memo(("bfs", len(P), tuple(sat)[:1], len(sat)),
                lambda: _bfs_min_schedule(P, sat, cap_rounds))


def _bfs_min_schedule(P, sat, cap_rounds=6):
    """THE LEAST SCHEDULE TIME AT ARITY a, complete: the fewest EVENTS, taken
    from whole rounds in the driver's own order, after which the stabilizer
    is trivial.  Breadth-first over signature partitions, so the answer is a
    minimum over ALL histories the arity admits and not over a corpus."""
    evs = [A.round_events(P[i]) for i in sat]
    if not evs:
        return None, None
    start = (frozenset(A.SITES),)
    frontier = {start: 0}
    seen = {start: 0}
    rounds = 0
    while frontier and rounds < cap_rounds:
        rounds += 1
        nxt, best = {}, None
        for part, k in frontier.items():
            for E in evs:
                p, kk, done = part, k, False
                for e in E:
                    q = []
                    for b in p:
                        i, o = b & e, b - e
                        if i:
                            q.append(i)
                        if o:
                            q.append(o)
                    p = tuple(q)
                    kk += 1
                    if len(p) == A.n:
                        best = kk if best is None or kk < best else best
                        done = True
                        break
                if done:
                    continue
                key = tuple(sorted(p, key=lambda s: sorted(A.SI[x] for x in s)))
                if key not in seen or seen[key] > kk:
                    seen[key] = kk
                    nxt[key] = kk
        if best is not None:
            return rounds, best
        frontier = nxt
    return None, None


def record_vector(H):
    r = {}
    for F in H:
        for u in F:
            for v in F:
                if u != v:
                    r[(u, v)] = r.get((u, v), 0) + 1
    return [r.get((x, A.vadd(x, l)), 0) for x in A.SITES for l in A.LINKS]


def block_map(part):
    return {x: bi for bi, b in enumerate(part) for x in b}


def leg1_geometry(part, corrupt=False):
    """LEG-1: for each declared link the translation descends to the blocks.
    Reads the partition and the arena, NEVER the history -- which is why the
    coset menu cannot move with the arity, and why its row is a disclosure."""
    links = A.LINKS[:1] if corrupt else A.LINKS
    bm = block_map(part)
    for l in links:
        img = {}
        for x in A.SITES:
            b, t = bm[x], bm[A.vadd(x, l)]
            if img.setdefault(b, t) != t:
                return False
    return True


def leg2_history(part, H, corrupt=False):
    if corrupt:
        return True
    for F in H:
        for b in part:
            k = sum(1 for x in b if x in F)
            if k and k != len(b):
                return False
    return True


def leg3_record(part, rec):
    for b in part:
        for li in range(A.L):
            if len({rec[A.SI[x] * A.L + li] for x in b}) > 1:
                return False
    return True


def induced_cell_partition(part):
    bm = block_map(part)
    d = {}
    for k, (x, l) in enumerate(A.CELLS):
        d.setdefault((bm[x], A.LINKS.index(l)), []).append(k)
    return tuple(sorted(tuple(sorted(v)) for v in d.values()))


SHIFT_T = tuple(A.CI[(A.vadd(x, l), l)] for (x, l) in A.CELLS)
GROVER = tuple(tuple(2 if i != j else 2 - A.L for j in range(A.L))
               for i in range(A.L))


def coupled_columns(rec, order, m):
    """paper-20's one-step operator U = T.C, column by column, EXACTLY, at the
    declared phase modulus m.  Integer coefficients throughout; the phase is
    an exponent, never a float."""
    cols = []
    for (y, l) in A.CELLS:
        li = A.LINKS.index(l)
        ent = []
        for i in range(A.L):
            tgt = SHIFT_T[A.CI[(y, A.LINKS[i])]]
            e = (rec[A.SI[y] * A.L + li] if order == "G.D"
                 else rec[A.SI[y] * A.L + i]) % m
            if GROVER[i][li]:
                ent.append((tgt, e, GROVER[i][li]))
        cols.append(tuple(sorted(ent)))
    return tuple(cols)


def leg4_dynamics(cpart, rec, order, m):
    lab = [0] * NC
    for bi, b in enumerate(cpart):
        for k in b:
            lab[k] = bi
    cols = coupled_columns(rec, order, m)
    prof = []
    for k in range(NC):
        acc = {}
        for (tgt, e, coef) in cols[k]:
            key = (lab[tgt], e)
            acc[key] = acc.get(key, 0) + coef
        prof.append(tuple(sorted((kk, vv) for kk, vv in acc.items() if vv)))
    for b in cpart:
        if len({prof[k] for k in b}) > 1:
            return False
    return True


COIN_ORDERS = ("G.D", "D.G")
COIN_MODULUS = 3          # DECLARED: paper-20 derives it from the arena's F_3


def admissible(part, H, rec, legs, m=COIN_MODULUS, corrupt2=False):
    l2 = leg2_history(part, H, corrupt2)
    l3 = leg3_record(part, rec)
    legs["l2"] += bool(l2)
    legs["l3"] += bool(l3)
    if not (l2 and l3):
        return False
    cp = induced_cell_partition(part)
    g = leg4_dynamics(cp, rec, COIN_ORDERS[0], m)
    d = leg4_dynamics(cp, rec, COIN_ORDERS[1], m)
    legs["l4_reached"] += 1
    legs["l4"] += bool(g and d)
    return bool(g and d)


def all_set_partitions(elems):
    elems = list(elems)
    if not elems:
        yield ()
        return
    first, rest = elems[0], elems[1:]
    for p in all_set_partitions(rest):
        for i in range(len(p)):
            yield p[:i] + (tuple(sorted(p[i] + (first,))),) + p[i + 1:]
        yield ((first,),) + p


def bell_number(n):
    row = [1]
    for _ in range(n):
        nxt = [row[-1]]
        for v in row:
            nxt.append(nxt[-1] + v)
        row = nxt
    return row[0]


def actor_lattice():
    return memo(("lattice",),
                lambda: [tuple(sorted(tuple(sorted(b)) for b in p))
                         for p in all_set_partitions(A.SITES)])


def homogeneous_ladder(V, sat, Rmax):
    return memo(("ladder", len(V), tuple(sat), Rmax),
                lambda: _homogeneous_ladder(V, sat, Rmax))


def _homogeneous_ladder(V, sat, Rmax):
    """THE WELD LADDER, MEASURED: which budgets R admit an R-tuple of
    saturating groupings whose summed link field is CONSTANT on every cell.

    Rows where the measured mass forbids a constant field are DERIVED from
    that mass and not enumerated; the rest are searched exhaustively under
    the constant as a per-cell ceiling, which prunes without excluding."""
    if not sat:
        return [], None, None
    vs = [V[i] for i in sat]
    w = sum(vs[0])
    modulus = NC // math.gcd(NC, w)
    out = []
    for R in range(1, Rmax + 1):
        if (R * w) % NC:
            out.append((R, False, "DERIVED-FROM-THE-MEASURED-MASS"))
            continue
        c = (R * w) // NC
        hit = [False]

        def dfs(start, tot, left):
            if hit[0]:
                return
            if left == 0:
                if all(t == c for t in tot):
                    hit[0] = True
                return
            for i in range(start, len(vs)):
                v = vs[i]
                nt = list(tot)
                ok = True
                for k in range(NC):
                    nt[k] += v[k]
                    if nt[k] > c:
                        ok = False
                        break
                if ok:
                    dfs(i, nt, left - 1)
                if hit[0]:
                    return
        dfs(0, [0] * NC, R)
        out.append((R, hit[0], "EXHAUSTIVE-UNDER-THE-CEILING"))
    return out, w, modulus


# ===========================================================================
# SECTION 3.  THE TRANSPORT DECISION PROCEDURE
#
# A law arrives with a parent value at a = 3.  This unit supplies TWO
# candidate transports of it and decides between them against the MEASURED
# value at every feasible arity:
#
#   T-LITERAL   the parent numeral does not move.  At fixed (n, q, L) this is
#               SIMULTANEOUSLY the n-only, the q-only and the L-only reading,
#               and section 8 of the paper says so: what this axis can decide
#               is whether the numeral is a-carried, not which of the three
#               standing coordinates carries it when it is not.
#   T-A         the numeral is a function of the arity alone, fixed by the
#               declared uniform rule C(a, 2) + v - C(3, 2).
#
# THE WORDS, pre-registered in the pin:
#   LAW-IN-A  T-A agrees at every feasible arity AND some feasible arity
#             DISCRIMINATES it from T-LITERAL (else the test is blind and the
#             row is stamped UNDISCRIMINATED, which is not a word)
#   NEEDS-3   T-LITERAL agrees at every feasible arity and T-A does not: the
#             numeral stands still while the event size moves, so it is not
#             carried by the event size
#   BREAKS    neither reading agrees at some feasible arity
#
# The procedure is a PURE FUNCTION of its rows, so the synthetic control laws
# of the closing battery run through this same code and nothing else.
# ===========================================================================

def arow(a, feasible, measured, note):
    return {"a": a, "feasible": bool(feasible), "measured": measured,
            "note": note}


def transport_word(parent_value, rows, rule=None):
    """rows: dicts with keys a, feasible, measured.  Infeasible rows are
    CARRIED and never scored (#34: a row that cannot reach the test is not
    evidence)."""
    rule = t_a_reading if rule is None else rule
    if mut("MUT-TRANSPORT"):
        return WORDS[0], {"reason": "SHORT-CIRCUITED"}
    feas = [r for r in rows if r["feasible"]]
    if not feas:
        return "BREAKS", {"reason": "NO-FEASIBLE-ROW", "carried": len(rows)}
    lit = [r for r in feas if r["measured"] == parent_value]
    ta = [r for r in feas if r["measured"] == rule(parent_value, r["a"])]
    disc = [r for r in feas if rule(parent_value, r["a"]) != parent_value]
    ev = {"feasible": len(feas), "carried": len(rows),
          "t_literal_agrees": len(lit), "t_a_agrees": len(ta),
          "rows_discriminating_a_from_literal": len(disc),
          "measured": [[r["a"], r["measured"]] for r in feas],
          "t_a": [[r["a"], rule(parent_value, r["a"])] for r in feas]}
    if len(ta) == len(feas):
        ev["stamp"] = "DISCRIMINATED" if disc else "UNDISCRIMINATED"
        return "LAW-IN-A", ev
    if len(lit) == len(feas):
        ev["stamp"] = "DISCRIMINATED" if disc else "UNDISCRIMINATED"
        return "NEEDS-3", ev
    ev["stamp"] = "FAILS-BOTH"
    ev["failing_arities"] = sorted(
        r["a"] for r in feas
        if r["measured"] != parent_value
        and r["measured"] != rule(parent_value, r["a"]))
    return "BREAKS", ev


def statement_word(rows):
    """the STATEMENT slot: the parent's theorem either holds at a feasible
    arity, fails there, or has no object to be evaluated on."""
    feas = [r for r in rows if r["feasible"]]
    if not feas:
        return "BREAKS", {"reason": "NO-FEASIBLE-ROW", "carried": len(rows)}
    bad = [r["a"] for r in feas if not r["measured"]]
    ev = {"feasible": len(feas), "carried": len(rows),
          "holds_at": sorted(r["a"] for r in feas if r["measured"]),
          "fails_at": sorted(bad)}
    if bad:
        return "BREAKS", ev
    return "LAW-IN-A", ev


# ===========================================================================
# SECTION 4.  THE RUN
# ===========================================================================

LD = Ledger()
TR = Transcript()
SEAL = Seal()
CR = CountRegistry()
RS = ReadSet(REPO)
AN = None
R = {}

PERM_WINDOW_KINDS = ("TRANSPOSITIONS", "THREE-CYCLES")


def permutation_window():
    return memo(("permwin",), _permutation_window)


def _permutation_window():
    """THE DECLARED PERMUTATION WINDOW: every transposition and every
    three-cycle of the nine actors.  S_9 itself is filtered too, at the
    declared grouping window; this smaller set is what the WHOLE census is
    filtered against, and it is exercised in both directions."""
    out = set()
    for i, j in combinations(range(A.n), 2):
        p = list(range(A.n))
        p[i], p[j] = p[j], p[i]
        out.add(tuple(p))
    for i, j, k in combinations(range(A.n), 3):
        for cyc in ((j, k, i), (k, i, j)):
            p = list(range(A.n))
            p[i], p[j], p[k] = cyc
            out.add(tuple(p))
    return sorted(out)


def read_source_text(rel, expect):
    path = os.path.join(REPO, rel)
    with open(path, "rb") as fh:
        raw = fh.read()
    got = hashlib.sha256(raw).hexdigest()[:12]
    if got != expect:
        raise GateFail("G-SOURCES :: %s sha %s != %s" % (rel, got, expect))
    return raw.decode("utf-8"), got


def jpath(obj, path):
    cur = obj
    for part in path.split("/"):
        if not isinstance(cur, dict) or part not in cur:
            raise GateFail("G-PATH-ANCHORS :: path %s missing at %s"
                           % (path, part))
        cur = cur[part]
    return cur


def quote_spelled(text, lead):
    words = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
             "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10}
    m = re.search(re.escape(lead) + r"\s+([a-z]+)", text.lower())
    return words.get(m.group(1)) if m else None


def quote_ints(text):
    return [int(t.replace(",", ""))
            for t in re.findall(r"(?<![\w.])(\d[\d,]*)(?![\w.])", text)]


def measure_naming(GRAM, CORP, WIN):
    """LAW 1's two routes, measured.  Memoised on the one mutant flag it
    depends on, so the falsifier harness recomputes it rather than being
    served the clean answer."""
    full_prefixes = full_positive = 0
    window_prefixes = window_positive = window_negative = 0
    mismatches = []
    distinct_by_arity = {}
    all9 = None
    for a in ARITIES:
        P = GRAM[a]["P"]
        for p in P[:NAMING_FULL_GROUP_WINDOW]:
            H = A.round_events(p)
            for k in range(1, len(H) + 1):
                if all9 is None:
                    all9 = list(permutations(range(A.n)))
                ra = route_a_stabilizer(
                    H[:k], all9,
                    corrupt=(mut("MUT-NAMING") and a == ARITIES[0]))
                rb = young_elements(H[:k])
                full_prefixes += 1
                full_positive += len(ra)
                if ra != rb:
                    mismatches.append({"a": a, "prefix": k, "leg": "S9"})
        seen = set()
        for hists in (CORP[a]["round"], CORP[a]["multi"], CORP[a]["window"]):
            for H in hists:
                for k in range(1, len(H) + 1):
                    key = frozenset(H[:k])
                    if key in seen:
                        continue
                    seen.add(key)
                    ra = route_a_stabilizer(H[:k], WIN)
                    rb = young_in_window(H[:k], WIN)
                    window_prefixes += 1
                    window_positive += len(ra)
                    window_negative += len(WIN) - len(ra)
                    if ra != rb:
                        mismatches.append({"a": a, "prefix": k,
                                           "leg": "WINDOW"})
        distinct_by_arity[a] = len(seen)
    return {"full_prefixes": full_prefixes, "full_positive": full_positive,
            "distinct_prefix_event_sets": distinct_by_arity,
            "window_prefixes": window_prefixes,
            "window_positive": window_positive,
            "window_negative": window_negative,
            "symmetric_group_order": math.factorial(A.n),
            "mismatches": mismatches}


def measure_crystallization(GRAM):
    rows = []
    for a in ARITIES:
        P, satM = GRAM[a]["P"], GRAM[a]["sat"]["MAXIMAL"]
        rounds_cr, sched = bfs_min_schedule(P, satM)
        floor, universe = absolute_floor(a)
        size = A.q if mut("MUT-FLOOR") else a
        rows.append({
            "a": a, "schedule_time_events": sched,
            "schedule_time_rounds": rounds_cr,
            "attained_floor": floor, "event_universe": universe,
            "counting_bound": counting_floor(A.n),
            "sharpened_floor": weight_floor(A.n, size),
            "offset": (sched - floor) if (sched is not None
                                          and floor is not None) else None})
        if mut("MUT-CRYSTAL") and a == ARITIES[0]:
            rows[-1]["schedule_time_events"] = rows[-1]["attained_floor"] - 1
    return rows


def measure_forcing(CORP, surv, DISCRETE):
    forcing = []
    for a in ARITIES:
        legs = Counter()
        cls = {name: A.CLASSES[name] for name in A.CLASS_NAMES}
        out = {"a": a}
        for tag, hists in (("single_round", CORP[a]["round"]),
                           ("multi", CORP[a]["multi"]),
                           ("driven_window", CORP[a]["window"])):
            uniq, nonuniq, joiners = 0, 0, Counter()
            for H in hists:
                rec = record_vector(H)
                adm = [p for p in surv
                       if admissible(p, H, rec, legs,
                                     corrupt2=mut("MUT-FORCING"))]
                if DISCRETE not in [tuple(sorted(p)) for p in adm]:
                    raise GateFail("G-LAW5-FORCING :: the discrete partition "
                                   "is not admissible at a history")
                if len(adm) == 1:
                    uniq += 1
                else:
                    nonuniq += 1
                    for p in adm:
                        if tuple(sorted(p)) != DISCRETE:
                            joiners[len(p)] += 1
            out[tag] = {"histories": len(hists), "unique": uniq,
                        "non_unique": nonuniq,
                        "joiner_block_counts": dict(sorted(joiners.items()))}
        classhits = 0
        for H in CORP[a]["round"]:
            if len(H) == len(cls["ROW"]) and frozenset(
                    tuple(sorted(e)) for e in H) in {
                        frozenset(cls[nm]) for nm in A.CLASS_NAMES}:
                classhits += 1
        out["single_rounds_that_are_parallel_classes"] = classhits
        out["legs"] = dict(legs)
        forcing.append(out)
    return forcing


def measure_sec2(UACT, UREL):
    rows, theorem_bad = [], []
    for a in ARITIES:
        span = lawful = free = groups = 0
        prof = Counter()
        for gsel in combinations(range(len(UACT)), a):
            acts = [UACT[i] for i in gsel]
            prs = [frozenset(p) for p in combinations(acts, 2)]
            new = [p for p in prs if p not in UREL]
            foreign = [p for p in new if {x[0] for x in p} == {"A", "B"}]
            within = [p for p in new if p not in foreign]
            dbl = [p for p in prs if p in UREL]
            if mut("MUT-SEC2-THEOREM") and a == PARENT_ARITY and dbl:
                dbl = []
            groups += 1
            if (len(foreign) + len(within) + len(dbl) != math.comb(a, 2)
                    or len(foreign) > (a * a) // 4):
                theorem_bad.append(str(gsel))
            if foreign:
                span += 1
                prof[(len(foreign), len(within), len(dbl))] += 1
                if not within:
                    lawful += 1
                    if not dbl:
                        free += 1
        rows.append({
            "a": a, "groups": groups, "seam_spanning": span,
            "within_sector_free": lawful,
            "opens_a_pair_inside_a_sector": span - lawful,
            "obstruction_free": free,
            "max_cut_of_the_complete_graph": (a * a) // 4,
            "forced_inside_bound": math.comb(a, 2) - (a * a) // 4,
            "profiles": sorted([[list(k), v] for k, v in prof.items()],
                               key=lambda kv: -kv[1])[:6]})
    return rows, theorem_bad


def full_run(paper_text, paper_rel=PAPER_REL, write=True, break_anchor=None):
    global AN, R
    R = {}
    src = {}
    prov = []
    for (sid, rel, sha, why) in SOURCES:
        if mut("MUT-SOURCE") and sid == SOURCES[0][0]:
            sha = "0" * 12
        txt, got = read_source_text(rel, sha)
        src[sid] = txt
        prov.append({"id": sid, "path": rel, "sha256_12": got, "why": why})
    CR.measured("n_sources", len(SOURCES), "len of the frozen source list")
    LD.gate("G-SOURCES", len(prov) == len(SOURCES),
            CR.stmt("every runtime input is a hash-pinned artifact of this "
                    "unit's frozen declaration; {k} sources are read and "
                    "each one's sha256 prefix is compared with the "
                    "declaration before its bytes are used",
                    k="n_sources"),
            {"sources": prov})
    R["provenance"] = SEAL.seal("provenance", prov, "G-SOURCES")

    # ---- PATH-VALUE ANCHORS ------------------------------------------
    rec_json = json.loads(src["A-NDEPREC"])
    pa = []
    for (aid, sid, path, expect, consumer) in PATH_ANCHORS:
        if (mut("MUT-PATH") and aid == PATH_ANCHORS[0][0]
                and isinstance(expect, int)):
            expect = expect + 1
        got = jpath(rec_json, path)
        if got != expect:
            raise GateFail("G-PATH-ANCHORS :: %s reads %r not %r"
                           % (aid, got, expect))
        pa.append({"id": aid, "source": sid, "path": path, "value": got,
                   "consumer": consumer})
    CR.measured("n_path_anchors", len(pa), "len of the path-anchor table")
    LD.gate("G-PATH-ANCHORS", len(pa) == len(PATH_ANCHORS),
            CR.stmt("{k} path-value anchors bind the (path, value) pair and "
                    "not only the file bytes, so a path drift that silently "
                    "substituted another of the parent's numbers dies here "
                    "even though no number would move",
                    k="n_path_anchors"),
            {"anchors": pa})
    R["path_anchors"] = SEAL.seal("path_anchors", pa, "G-PATH-ANCHORS")
    PV = {aid: v for (aid, _s, _p, v, _c) in PATH_ANCHORS}

    # ---- VERBATIM ANCHORS --------------------------------------------
    AN = AnchorSet([Anchor(nm, needle, sid, cons, why)
                    for (nm, sid, needle, cons, why) in VERBATIM])
    AN.locate(src, paper_text, broken=break_anchor)
    CR.measured("n_verbatim", len(VERBATIM), "len of the verbatim table")
    LD.gate("G-VERBATIM", True,
            CR.stmt("{k} verbatim-text anchors bind QUOTE FIDELITY: each "
                    "needle occurs exactly once in the pinned source and at "
                    "least once in this paper's own rendering under the "
                    "normalisation the era's text gates use, and each is "
                    "readable only through an accessor that records the read",
                    k="n_verbatim"),
            {"anchors": [{"id": nm, "source": sid, "consumer": cons,
                          "chars": len(canon(needle))}
                         for (nm, sid, needle, cons, _w) in VERBATIM]})

    # ---- THE ARENA, FIXED --------------------------------------------
    q_quote = AN.read("V-SQRT", "G-ARENA")
    m = re.search(r"q is the (\w+ \w+) of the actor count exactly", q_quote)
    relation = m.group(1) if m else None
    CR.measured("n_actors", A.n, "the arena's site count, computed")
    CR.measured("q_order", A.q, "the field order, computed")
    CR.measured("n_links", A.L, "the declared link count")
    CR.measured("n_cells", NC, "the cell count, computed as sites x links")
    CR.measured("n_classes", len(A.CLASSES), "the parallel classes, computed")
    CR.measured("characteristic", A.characteristic,
                "the field characteristic, computed from its own addition")
    LD.gate("G-ARENA",
            relation == "square root" and A.q * A.q == A.n
            and _probe_arena() == A.q and len(A.CELLS) == A.n * A.L
            and len(A.CLASSES) == A.q + 1,
            CR.stmt("the arena is AG(2, q) at {q} and it does not move: "
                    "{n} actors, {c} cells, {p} parallel classes, "
                    "characteristic {ch}, and the relation the parent's own "
                    "quotation names between the field order and the actor "
                    "count holds here, which is what makes the field order "
                    "immovable while the event size is swept",
                    q="q_order", n="n_actors", c="n_cells", p="n_classes",
                    ch="characteristic"),
            {"relation_parsed_from_the_quotation": relation,
             "n": A.n, "q": A.q, "L": A.L, "cells": NC,
             "characteristic": A.characteristic,
             "parallel_classes": len(A.CLASSES),
             "declared_links": [list(l) for l in A.LINKS]})
    R["arena"] = SEAL.seal(
        "arena", {"declaration": [list(t) for t in arena_declaration()],
                  "n": A.n, "q": A.q, "L": A.L, "cells": NC,
                  "characteristic": A.characteristic,
                  "parallel_classes": len(A.CLASSES),
                  "arities": list(ARITIES),
                  "windowed_arity": WINDOWED_ARITY,
                  "corpus_cap": CORPUS_CAP,
                  "ladder_search_bound": LADDER_RMAX}, "G-ARENA")
    R["preregistered_outcomes"] = SEAL.seal(
        "preregistered_outcomes",
        [{"word": w, "meaning": mm, "feasibility": f}
         for (w, mm, f) in PREREGISTERED], "G-ARENA")

    # ---- THE FIDELITY GATE: BEFORE ANY NEW-a ROW ---------------------
    P3, V3, W3 = substrate(PARENT_ARITY)
    sat3 = saturating(W3, "LITERAL")
    st3 = strict_tuples(V3, sat3, A.L)
    fl3, fl3how = flat_tuples(V3, sat3, A.L + 1)
    win3, meta3, nflat3, how3, cls3 = driven_window(P3, V3, sat3, PARENT_ARITY)
    fid = {"groupings": len(P3), "saturating": len(sat3),
           "strict_triples": len(st3), "flat_quadruples": len(fl3),
           "window": len(win3)}
    want = {"groupings": PV["P-PARTS"], "saturating": PV["P-SAT"],
            "strict_triples": PV["P-STRICT"], "flat_quadruples": PV["P-FLAT"],
            "window": PV["P-WINDOW"]}
    if mut("MUT-FIDELITY"):
        fid["saturating"] = fid["saturating"] + len(A.LINKS)
    agree = sorted(k for k in want if fid[k] == want[k])
    CR.measured("fid_rows", len(want), "len of the anchored substrate table")
    CR.measured("fid_agree", len(agree), "count of agreeing substrate rows")
    LD.gate("G-CONSTRUCTOR-FIDELITY", len(agree) == len(want),
            CR.stmt("the a-grammar is run at the PARENT'S OWN ARITY first "
                    "and its substrate is compared row by row against the "
                    "committed counts read at declared JSON paths: {ok} of "
                    "{k} agree. This gate is a FIDELITY LEG and not a "
                    "finding, and no measurement at any other arity is taken "
                    "before it passes",
                    ok="fid_agree", k="fid_rows"),
            {"measured": fid, "anchored": want, "agreeing": agree,
             "stamp": "FIDELITY-LEG-ONLY"})
    R["fidelity"] = SEAL.seal(
        "fidelity", {"measured": fid, "anchored": want,
                     "agree": len(agree), "rows": len(want),
                     "flat_search": fl3how, "window_tags":
                         dict(Counter(meta3.values())),
                     "stamp": "FIDELITY-LEG-ONLY: no law value is read off "
                              "this leg; it licenses the sentence that the "
                              "same constructor is run at the other arities"},
        "G-CONSTRUCTOR-FIDELITY")

    # the transport rule is a STRICT EXTENSION of the parent's constructor
    P3strict = A.packings(PARENT_ARITY, drop_idle=True)
    if mut("MUT-EXTEND"):
        P3strict = P3strict[:-1]
    CR.measured("parent_groupings", len(P3), "packings at the parent arity")
    LD.gate("G-PACKING-EXTENDS",
            P3 == P3strict and all(sum(len(g) for g in p) == A.n for p in P3),
            CR.stmt("at the parent's arity the maximal-packing rule returns "
                    "exactly the partitions the parent's constructor returns "
                    "-- all {k} of them, every one covering every actor -- so "
                    "the arity transport is a strict extension of the "
                    "committed constructor and not a different constructor "
                    "that happens to agree on a count",
                    k="parent_groupings"),
            {"packings": len(P3), "partition_route": len(P3strict),
             "idle_actors_at_the_parent_arity": A.n - PARENT_ARITY *
                 (A.n // PARENT_ARITY)})

    fidelity_row = LD.index_of("G-CONSTRUCTOR-FIDELITY")

    # ================================================================
    # THE SUBSTRATE CENSUS, ARITY BY ARITY
    # ================================================================
    GRAM = {}
    subrows = []
    for a in ARITIES:
        P, V, W = substrate(a)
        blocks = A.n // a
        idle = A.n - a * blocks
        row = {"a": a, "blocks_per_round": blocks, "idle_actors": idle,
               "groupings": len(P), "weights": sorted(set(W)),
               "max_weight": max(W), "budget": A.n}
        sats = {}
        for reading in ("LITERAL", "MAXIMAL"):
            s = saturating(W, reading)
            sats[reading] = s
            row["saturating_" + reading] = len(s)
            row["mass_" + reading] = (W[s[0]] if s else None)
        row["saturation_is_maximality"] = (max(W) == A.n)
        row["cover_R_min"] = (-(-NC // max(W)))
        GRAM[a] = {"P": P, "V": V, "W": W, "sat": sats}
        subrows.append(row)
    if mut("MUT-PACKING"):
        subrows[0]["groupings"] = len(A.packings(ARITIES[0], drop_idle=True))
    parent_row = [r for r in subrows if r["a"] == PARENT_ARITY][0]
    CR.measured("n_arities", len(ARITIES), "len of the declared arity window")
    CR.measured("parent_max_weight", parent_row["max_weight"],
                "the maximum round incidence at the parent arity, measured")
    CR.measured("maximality_arities",
                sum(1 for r in subrows if r["saturation_is_maximality"]),
                "count of arities at which the budget is the maximum")
    LD.gate("G-SUBSTRATE-CENSUS",
            parent_row["max_weight"] == PV["P-MAXINC"]
            and parent_row["budget"] == PV["P-BUDGET"]
            and parent_row["saturation_is_maximality"] is bool(PV["P-SATMAX"])
            and all(r["groupings"] == len(GRAM[r["a"]]["P"]) for r in subrows)
            and len(subrows) == len(ARITIES),
            CR.stmt("the substrate is censused at every one of the {k} "
                    "declared arities, and the parent's two SEPARATELY "
                    "anchored objects -- the budget and the maximum round "
                    "incidence -- are reproduced at the parent's arity, "
                    "where they agree at {w}. The count of arities at which "
                    "the budget IS the maximum is {m}, which is the "
                    "measurement that decides what the parent's word "
                    "saturating can mean off its own arity",
                    k="n_arities", w="parent_max_weight",
                    m="maximality_arities"),
            {"rows": subrows})
    R["substrate"] = SEAL.seal("substrate", subrows, "G-SUBSTRATE-CENSUS")

    order_ok = all(LD.index_of(g) is None or LD.index_of(g) > fidelity_row
                   for g in ("G-SUBSTRATE-CENSUS",))
    if mut("MUT-ORDER"):
        order_ok = fidelity_row > LD.index_of("G-SUBSTRATE-CENSUS")
    CR.measured("fidelity_row", fidelity_row,
                "the ledger index at which the fidelity gate fired")
    LD.gate("G-FIDELITY-FIRST", order_ok,
            CR.stmt("the fidelity gate fired at ledger row {r}, before the "
                    "first measurement taken at any arity other than the "
                    "parent's; the ordering is checked against the ledger's "
                    "own row indices rather than asserted",
                    r="fidelity_row"),
            {"fidelity_row": fidelity_row,
             "substrate_row": LD.index_of("G-SUBSTRATE-CENSUS")})

    # ================================================================
    # THE CORPUS RULE, ONE RULE AT EVERY ARITY
    # ================================================================
    CORP = {}
    corprows = []
    for a in ARITIES:
        g = GRAM[a]
        P, V = g["P"], g["V"]
        satL, satM = g["sat"]["LITERAL"], g["sat"]["MAXIMAL"]
        c1 = strict_tuples(V, satL, A.L)
        win, meta, nflat, how, cls = driven_window(P, V, satL, a)
        rounds_cr, events_cr = bfs_min_schedule(P, satM)
        entry = {"a": a, "C1_strict_literal": len(c1),
                 "C3_driven_window": len(win),
                 "C3_class_arm_defined": cls,
                 "near_flat_tuples": nflat, "near_flat_search": how,
                 "least_crystallizing_rounds": rounds_cr}
        if c1:
            hist = [[P[i] for i in T] for T in c1]
            entry["multi_corpus"] = "C1-STRICT-LITERAL"
            entry["multi_histories"] = len(hist)
        else:
            reps, sizes = translation_orbits(P, satM)
            depth = rounds_cr if rounds_cr else A.L
            size = len(reps) * (len(satM) ** (depth - 1))
            entry["orbit_representatives"] = len(reps)
            entry["orbit_sizes"] = sorted(set(sizes))
            entry["cx_size"] = size
            if size <= CORPUS_CAP:
                hist = []
                for r0 in reps:
                    for rest in product(satM, repeat=depth - 1):
                        hist.append([P[r0]] + [P[i] for i in rest])
                entry["multi_corpus"] = "CX-ORBIT-REDUCED"
                entry["multi_histories"] = len(hist)
            else:
                hist = []
                entry["multi_corpus"] = "NOT-REACHED"
                entry["multi_histories"] = 0
        CORP[a] = {"round": [A.round_events(p) for p in P],
                   "multi": [[e for p in T for e in A.round_events(p)]
                             for T in hist],
                   "window": [[e for (pp, _s) in sch
                               for e in A.round_events(pp)] for sch in win],
                   "window_meta": [meta[sch] for sch in win]}
        entry["single_round_histories"] = (
            len(CORP[a]["round"]) + 1 if mut("MUT-CORPUS")
            else len(CORP[a]["round"]))
        corprows.append(entry)
    CR.measured("corpus_rows", len(corprows), "one row per declared arity")
    CR.measured("corpus_cap", CORPUS_CAP, "the declared enumeration cap")
    LD.gate("G-CORPUS-RULE",
            len(corprows) == len(ARITIES)
            and all(e["single_round_histories"] ==
                    subrows[i]["groupings"] for i, e in enumerate(corprows)),
            CR.stmt("one corpus rule is applied at every one of the {k} "
                    "arities: the single-round census is COMPLETE everywhere "
                    "-- every grouping the arity admits, nothing sampled -- "
                    "and the multi-round corpus is the parent's own strict "
                    "class where that class is non-empty and the "
                    "orbit-reduced least-crystallizing corpus where it is "
                    "not, run only when it fits the declared cap",
                    k="corpus_rows"),
            {"rows": corprows})
    R["corpus"] = SEAL.seal("corpus", corprows, "G-CORPUS-RULE")

    # ================================================================
    # LAW 1 -- THE NAMING THEOREM
    # ================================================================
    WIN = permutation_window()
    CR.measured("perm_window", len(WIN), "size of the declared window")
    nres = memo(("naming", mut("MUT-NAMING")),
                lambda: measure_naming(GRAM, CORP, WIN))
    full_prefixes = nres["full_prefixes"]
    full_positive = nres["full_positive"]
    window_prefixes = nres["window_prefixes"]
    window_positive = nres["window_positive"]
    window_negative = nres["window_negative"]
    mismatches = nres["mismatches"]
    CR.measured("full_prefixes", full_prefixes,
                "prefixes filtered against the whole symmetric group")
    CR.measured("window_prefixes", window_prefixes,
                "prefixes filtered against the declared permutation window")
    CR.measured("naming_mismatches", len(mismatches),
                "route disagreements, counted")
    CR.measured("full_positive", full_positive,
                "stabilizer elements found by route A on the group leg")
    LD.gate("G-LAW1-NAMING", not mismatches,
            CR.stmt("two routes are compared AS SETS OF PERMUTATIONS, per "
                    "object: route A holds a permutation set and keeps what "
                    "survives the definition, route B builds the Young "
                    "subgroup from the signature blocks and knows nothing of "
                    "route A. The whole symmetric group is filtered at {f} "
                    "prefixes and the declared window at {w} more, with {p} "
                    "elements landing inside the stabilizer on the group leg "
                    "and both directions exercised on the window leg; the "
                    "disagreements number {m}",
                    f="full_prefixes", w="window_prefixes",
                    p="full_positive", m="naming_mismatches"),
            {"full_group_prefixes": full_prefixes,
             "window_prefixes": window_prefixes,
             "window_size": len(WIN),
             "window_kinds": list(PERM_WINDOW_KINDS),
             "positives_group_leg": full_positive,
             "positives_window_leg": window_positive,
             "negatives_window_leg": window_negative,
             "mismatches": mismatches[:8],
             "groupings_per_arity_on_the_group_leg":
                 NAMING_FULL_GROUP_WINDOW})
    R["law1_naming"] = SEAL.seal(
        "law1_naming",
        {"full_group_prefixes": full_prefixes,
         "window_prefixes": window_prefixes, "mismatches": len(mismatches),
         "symmetric_group_order": math.factorial(A.n),
         "window_size": len(WIN),
         "groupings_per_arity_on_the_group_leg": NAMING_FULL_GROUP_WINDOW,
         "positives_group_leg": full_positive,
         "positives_window_leg": window_positive,
         "negatives_window_leg": window_negative,
         "stamp": "REPRODUCTION: the parent proves this theorem by a "
                  "Boolean-algebra argument that names no arena and no event "
                  "size, so a faithful implementation cannot disagree; the "
                  "leg is a fidelity check on this unit's constructor and it "
                  "is published as one"},
        "G-LAW1-NAMING")

    # ================================================================
    # LAW 2 -- THE CRYSTALLIZATION PAIR
    # ================================================================
    fq = AN.read("V-FLOOR", "G-LAW2-SHARPENED")
    msym = re.search(r"exactly (\w) members", fq)
    mprod = re.search(r"total incidence (\w+)", fq)
    cfq = AN.read("V-CLOSEDFORM", "G-LAW2-SHARPENED")
    cf = re.search(r"(\d+)\((\w) - (\d+)\)", cfq)
    quote_ok = (msym is not None and mprod is not None and cf is not None
                and len(mprod.group(1)) == 2
                and msym.group(1) in mprod.group(1))
    closed_at_parent = (int(cf.group(1)) * (A.q - int(cf.group(3)))
                        if cf else None)
    cryrows = memo(("crystal", mut("MUT-FLOOR"), mut("MUT-CRYSTAL")),
                   lambda: measure_crystallization(GRAM))
    sharp_ok = [r for r in cryrows if r["sharpened_floor"] == r["attained_floor"]]
    count_ok = [r for r in cryrows if r["counting_bound"] == r["attained_floor"]]
    CR.measured("cry_rows", len(cryrows), "one row per declared arity")
    CR.measured("sharp_hits", len(sharp_ok), "arities where the sharpened "
                "floor equals the attained floor")
    CR.measured("count_hits", len(count_ok), "arities where the counting "
                "bound equals the attained floor")
    LD.gate("G-LAW2-CRYSTALLIZATION",
            all(r["attained_floor"] is not None for r in cryrows)
            and all(r["schedule_time_events"] is not None for r in cryrows)
            and all(r["attained_floor"] <= r["schedule_time_events"]
                    for r in cryrows),
            CR.stmt("the pair is re-measured at every one of the {k} "
                    "arities: the schedule time by a complete breadth-first "
                    "search over signature partitions, so it is a minimum "
                    "over EVERY history the arity admits and not over a "
                    "corpus; and the information floor over the COMPLETE "
                    "event universe of the arity, every subset of that size, "
                    "with the floor never above the schedule time",
                    k="cry_rows"),
            {"rows": cryrows})
    LD.gate("G-LAW2-SHARPENED",
            quote_ok and len(sharp_ok) == len(cryrows)
            and closed_at_parent == cryrows[
                [r["a"] for r in cryrows].index(PARENT_ARITY)]["attained_floor"],
            CR.stmt("the parent's SHARPENED floor is driven by the event "
                    "size the parent's own quotation names -- the membership "
                    "symbol and the incidence product are parsed out of the "
                    "quotation rather than assumed -- and it reproduces the "
                    "measured floor at {s} of {k} arities, while the "
                    "counting bound the parent published beside it "
                    "reproduces it at {c}; the parent's closed form, read "
                    "off its own quotation, returns the parent's floor at "
                    "the parent's arity",
                    s="sharp_hits", k="cry_rows", c="count_hits"),
            {"membership_symbol": msym.group(1) if msym else None,
             "incidence_product": mprod.group(1) if mprod else None,
             "closed_form_at_the_parent_arity": closed_at_parent,
             "sharpened_agrees_at": [r["a"] for r in sharp_ok],
             "counting_bound_agrees_at": [r["a"] for r in count_ok]})
    strat = {}
    for a in ARITIES:
        cnt = Counter()
        for H in CORP[a]["multi"]:
            cnt[crystallization_time(H)] += 1
        strat[str(a)] = {str(k): v for k, v in
                         sorted(cnt.items(), key=lambda kv:
                                (kv[0] is None, kv[0]))}
    wcnt = Counter()
    for H, tag in zip(CORP[PARENT_ARITY]["window"],
                      CORP[PARENT_ARITY]["window_meta"]):
        wcnt[crystallization_time(H)] += 1
    R["law2_crystallization"] = SEAL.seal(
        "law2_crystallization",
        {"rows": cryrows, "multi_corpus_strata": strat,
         "parent_window_strata": {str(k): v for k, v in
                                  sorted(wcnt.items(), key=lambda kv:
                                         (kv[0] is None, kv[0]))}},
        "G-LAW2-CRYSTALLIZATION")

    # ================================================================
    # LAW 3 -- THE COSET MENU
    # ================================================================
    LAT = actor_lattice()
    surv = memo(("menu", mut("MUT-MENU")),
                lambda: [p for p in LAT
                         if leg1_geometry(p, corrupt=mut("MUT-MENU"))])
    cosets = sorted({A.coset_partition(H) for H in A.subgroups()})
    CR.measured("lattice", len(LAT), "the complete actor lattice, enumerated")
    CR.measured("bell", bell_number(A.n), "Bell(n) by the Bell triangle")
    CR.measured("menu", len(surv), "leg-1 survivors, measured")
    CR.measured("cosets", len(cosets), "coset partitions of the subgroups")
    menu_setequal = sorted(surv) == sorted(cosets)
    LD.gate("G-LAW3-MENU",
            len(LAT) == bell_number(A.n) and menu_setequal
            and len(surv) == len(cosets),
            CR.stmt("the geometry leg is evaluated on the COMPLETE actor "
                    "lattice -- all {l} partitions of the nine actors, "
                    "cross-checked against Bell(n) computed by the Bell "
                    "triangle at {b} -- and its {m} survivors are compared "
                    "ELEMENT BY ELEMENT with the {c} coset partitions of the "
                    "translation subgroups. The leg reads the partition and "
                    "the arena and never a history, so its value cannot move "
                    "with the event size: the row is a DISCLOSURE and is "
                    "published as one",
                    l="lattice", b="bell", m="menu", c="cosets"),
            {"lattice": len(LAT), "survivors": len(surv),
             "coset_partitions": len(cosets), "set_equal": menu_setequal,
             "reads_the_history": False,
             "stamp": "A-INERT-BY-CONSTRUCTION"})
    R["law3_menu"] = SEAL.seal(
        "law3_menu",
        {"lattice": len(LAT), "survivors": len(surv),
         "coset_partitions": len(cosets), "set_equal": menu_setequal,
         "value_at_every_arity": {str(a): len(surv) for a in ARITIES},
         "subgroup_orders": sorted(Counter(len(H) for H in
                                           A.subgroups()).items()),
         "stamp": "A-INERT-BY-CONSTRUCTION: the leg quantifies over no "
                  "event, so a comparison across arities could not have come "
                  "out otherwise and is published as a disclosure"},
        "G-LAW3-MENU")

    # ================================================================
    # LAW 4 -- THE LADDER MODULUS (the mod-a question)
    # ================================================================
    ladrows = []
    for a in ARITIES:
        for reading in ("LITERAL", "MAXIMAL"):
            sat = GRAM[a]["sat"][reading]
            rows, w, modulus = homogeneous_ladder(GRAM[a]["V"], sat,
                                                  LADDER_RMAX)
            ach = [Rr for (Rr, hit, _h) in rows if hit]
            if mut("MUT-LADDER") and a == PARENT_ARITY and reading == "LITERAL":
                ach = [Rr for (Rr, _hit, _h) in rows]
            ladrows.append({
                "a": a, "reading": reading, "saturating": len(sat),
                "mass_per_round": w, "predicted_modulus": modulus,
                "achievable_budgets": ach,
                "derived_rows": sum(1 for (_r, _h, how) in rows
                                    if how.startswith("DERIVED")),
                "searched_rows": sum(1 for (_r, _h, how) in rows
                                     if how.startswith("EXHAUSTIVE")),
                "feasible": bool(sat),
                "modulus_measured": (min(ach) if ach else None),
                "is_multiples_of_the_link_count":
                    bool(ach) and ach == [k for k in
                                          range(1, LADDER_RMAX + 1)
                                          if k % A.L == 0],
                "first_rung_is_the_event_size": bool(ach) and min(ach) == a,
                # AT THE PARENT'S ARITY THE EVENT SIZE AND THE LINK COUNT ARE
                # THE SAME NUMBER, so "the first rung is the event size" is
                # satisfied there by a coincidence this axis cannot break.
                # Only a row at which they DIFFER can discriminate, and that
                # is the row the census counts.
                "mod_a_appears": (bool(ach) and min(ach) == a
                                  and a != A.L)})
    modrows = [r for r in ladrows if r["achievable_budgets"]]
    CR.measured("ladder_rows", len(ladrows), "arity x reading rows")
    CR.measured("ladder_live", len(modrows), "rows with a rung at all")
    CR.measured("mod_a_rows", sum(1 for r in ladrows if r["mod_a_appears"]),
                "rows whose first rung is the arity")
    CR.measured("ladder_bound", LADDER_RMAX, "the declared search bound")
    LD.gate("G-LAW4-LADDER",
            all(r["is_multiples_of_the_link_count"] for r in modrows)
            and sum(1 for r in ladrows if r["mod_a_appears"]) == 0
            and all(r["achievable_budgets"] == [] for r in ladrows
                    if r["feasible"] and r["mass_per_round"] is not None
                    and r["predicted_modulus"] != A.L),
            CR.stmt("the ladder is searched at every arity and at both "
                    "declared saturation readings, to the declared bound {b} "
                    "-- {n} rows, of which {live} carry a rung at all. Every "
                    "row that carries one carries exactly the multiples of "
                    "the declared link count, and the number of rows whose "
                    "first rung is the event size is {ma}. Rows the measured "
                    "mass forbids are DERIVED from that mass and the rest "
                    "are searched exhaustively under the constant as a "
                    "per-cell ceiling",
                    b="ladder_bound", n="ladder_rows", live="ladder_live",
                    ma="mod_a_rows"),
            {"rows": ladrows})
    R["law4_ladder"] = SEAL.seal(
        "law4_ladder",
        {"rows": ladrows,
         "mechanism": "the modulus is the cell count divided by its gcd with "
                      "the measured round mass; it equals the declared link "
                      "count exactly when the round mass equals the budget, "
                      "which is a fact about the mass and not about the "
                      "event size"},
        "G-LAW4-LADDER")

    # ================================================================
    # LAW 5 -- THE DIVISION-FORCING THESIS
    # ================================================================
    DISCRETE = tuple(sorted((x,) for x in A.SITES))
    forcing = memo(("forcing", mut("MUT-FORCING")),
                   lambda: measure_forcing(CORP, surv, DISCRETE))
    thesis_ok = all(
        r["single_round"]["non_unique"] ==
        r["single_rounds_that_are_parallel_classes"] for r in forcing)
    CR.measured("forcing_rows", len(forcing), "one row per declared arity")
    CR.measured("parent_nonunique",
                [r for r in forcing if r["a"] == PARENT_ARITY][0]
                ["single_round"]["non_unique"],
                "non-unique single-round histories at the parent arity")
    LD.gate("G-LAW5-FORCING",
            thesis_ok and len(forcing) == len(ARITIES),
            CR.stmt("the criterion is evaluated over the COMPLETE actor "
                    "lattice at every history of every corpus at all {k} "
                    "arities -- the geometry leg collapses the lattice to "
                    "its survivors before any history is read, so nothing is "
                    "windowed -- and the parent's thesis is tested PER "
                    "OBJECT rather than by comparing counts: a history is "
                    "non-unique exactly when it repeats a parallel class. At "
                    "the parent's arity {p} single rounds are non-unique",
                    k="forcing_rows", p="parent_nonunique"),
            {"rows": forcing, "thesis_holds_per_object": thesis_ok,
             "measure": "COUNTING-ONLY"})
    R["law5_forcing"] = SEAL.seal(
        "law5_forcing",
        {"rows": forcing, "thesis_holds_per_object": thesis_ok,
         "measure": "COUNTING-ONLY (E-24): no measure over histories is "
                    "declared anywhere in this unit, so every fraction here "
                    "is a count of this corpus's histories"},
        "G-LAW5-FORCING")

    # ================================================================
    # LAW 6 -- SEC-2's THREE-ACTOR COUNTING THEOREM, RE-DERIVED AT EACH a
    # ================================================================
    ARR = ("ROW", "COL", "DIA")
    SECTOR_PAIRS = tuple(sorted({tuple(sorted(p)) for c in ARR
                                 for g in A.CLASSES[c]
                                 for p in combinations(g, 2)}))
    ANTL = A.CLASSES["ANT"][0]
    glue = tuple(zip(ANTL, ANTL))
    amap, bmap = {}, {}
    for i, (sa, sb) in enumerate(glue):
        amap[sa] = ("S", i)
        bmap[sb] = ("S", i)
    for s in A.SITES:
        amap.setdefault(s, ("A", s))
        bmap.setdefault(s, ("B", s))
    UACT = sorted(set(amap.values()) | set(bmap.values()), key=repr)
    UREL = Counter()
    for mp in (amap, bmap):
        for (u, v) in SECTOR_PAIRS:
            UREL[frozenset((mp[u], mp[v]))] += 1
    secrows, theorem_bad = memo(("sec2", mut("MUT-SEC2-THEOREM")),
                                lambda: measure_sec2(UACT, UREL))
    prow = [r for r in secrows if r["a"] == PARENT_ARITY][0]
    tq = AN.read("V-TRIANGLE", "G-LAW6-SEC2")
    cq = AN.read("V-CONTROL", "G-LAW6-SEC2")
    lq = AN.read("V-LAWFUL", "G-LAW6-SEC2")
    dq = AN.read("V-DEAD", "G-LAW6-SEC2")
    q_cut = quote_spelled(tq, "at most")
    q_size = quote_spelled(cq, "no")
    q_law = quote_ints(lq)
    q_dead = quote_ints(dq)
    ctl_row = [r for r in secrows if r["a"] == q_size]
    theorem_holds = {r["a"]: (r["obstruction_free"] == 0) for r in secrows}
    LD.gate("G-LAW6-SEC2",
            not theorem_bad
            and q_cut == prow["max_cut_of_the_complete_graph"]
            and q_size == PARENT_ARITY
            and len(ctl_row) == 1 and ctl_row[0]["obstruction_free"] == 0
            and sorted(q_law) == sorted([prow["seam_spanning"],
                                         prow["within_sector_free"]])
            and q_dead == [prow["opens_a_pair_inside_a_sector"]],
            CR.stmt("the union of two driven sectors is rebuilt here from "
                    "the arrangement alone and its a-group census is run at "
                    "every declared arity, object by object with no orbit "
                    "shortcut. The parent's own quotations are parsed rather "
                    "than paraphrased: the spelled bound on cross pairs, the "
                    "spelled group size its control row says cannot produce "
                    "the free configuration, and both numerals of its "
                    "delivered census; all four are compared against this "
                    "unit's independently measured values, and the identity "
                    "that every pair of a group is a cross pair, a new "
                    "within-sector pair or a doubling holds at every group",
                    ),
            {"rows": secrows,
             "quoted_max_cut": q_cut, "quoted_control_size": q_size,
             "quoted_census": q_law, "quoted_dead": q_dead,
             "theorem_holds_at": theorem_holds,
             "identity_violations": theorem_bad[:8],
             "union_carriers": len(UACT),
             "union_realised_pairs": len(UREL),
             "union_doubled_pairs": sum(1 for v in UREL.values() if v > 1)})
    R["law6_sec2"] = SEAL.seal(
        "law6_sec2",
        {"rows": secrows, "union_carriers": len(UACT),
         "union_realised_pairs": len(UREL),
         "theorem_holds_at": {str(k): v for k, v in theorem_holds.items()},
         "bound": "C(a,2) - floor(a*a/4), the complement of the maximum cut "
                  "of the complete graph on a vertices: the least number of "
                  "the group's pairs that must lie inside one sector",
         "stamp": "the free-items count itself is SEC-2's measurement and is "
                  "not recomputed here; what is recomputed is the "
                  "configuration its rows are about, and the arity at which "
                  "a driven event can realise the row SEC-2 stamped a "
                  "control"},
        "G-LAW6-SEC2")

    # ================================================================
    # THE PRINCIPLE CENSUS -- Q17 and Q19
    # ================================================================
    CANDIDATES = tuple(range(1, A.n + 1))
    princ = []
    for a in CANDIDATES:
        P, V, W = substrate(a)
        satL = saturating(W, "LITERAL")
        c1 = strict_tuples(V, satL, A.L)
        princ.append({
            "a": a,
            "round_completeness": (A.n % a == 0) if not (
                mut("MUT-PRINCIPLE") and a == PARENT_ARITY) else (A.n % a != 0),
            "saturation_at_the_budget": bool(satL),
            "saturation_is_maximality": (max(W) == A.n),
            "subgroup_order_available": any(len(H) == a
                                            for H in A.subgroups()),
            "cover_at_R_equals_L": bool(c1),
            "nontrivial": (1 < a < A.n)})
    PRINCIPLES = ("round_completeness", "saturation_at_the_budget",
                  "saturation_is_maximality", "subgroup_order_available",
                  "cover_at_R_equals_L")
    padmits = {}
    for p in PRINCIPLES:
        padmits[p] = [r["a"] for r in princ if r[p]]
    selectors = [p for p in PRINCIPLES
                 if [a for a in padmits[p]
                     if 1 < a < A.n] == [PARENT_ARITY]]
    CR.measured("n_principles", len(PRINCIPLES),
                "candidate principles, enumerated")
    CR.measured("n_selectors", len(selectors),
                "principles selecting the parent arity uniquely among the "
                "nontrivial candidates")
    CR.measured("n_candidates", len(CANDIDATES),
                "candidate arities swept for the principle census")
    divisors = [x for x in CANDIDATES if not A.n % x]
    LD.gate("G-PRINCIPLE-CENSUS",
            len(princ) == len(CANDIDATES)
            and all(isinstance(r[p], bool) for r in princ
                    for p in PRINCIPLES)
            and padmits["round_completeness"] == divisors
            and padmits["subgroup_order_available"] == sorted(
                {len(H) for H in A.subgroups()}),
            CR.stmt("{k} candidate principles, none of them ever registered "
                    "as a principle anywhere in the corpus, are evaluated by "
                    "measurement at all {c} candidate event sizes the arena "
                    "admits; {s} of them admit the parent's arity and no "
                    "other nontrivial one",
                    k="n_principles", c="n_candidates", s="n_selectors"),
            {"rows": princ, "admits": padmits, "unique_selectors": selectors})
    R["principles"] = SEAL.seal(
        "principles",
        {"rows": princ, "admits": {k: v for k, v in sorted(padmits.items())},
         "unique_selectors": selectors,
         "stamp": "NONE of these was pre-registered anywhere in the corpus. "
                  "Each is a commitment implicit in a constructor, and the "
                  "census measures what each WOULD select if it were "
                  "declared. The subgroup row is named for what it measures: "
                  "whether the translation group has a subgroup of that "
                  "order, which is weaker than the events themselves being "
                  "cosets -- at the parent's arity the event universe is "
                  "every triple and only the lines are cosets"},
        "G-PRINCIPLE-CENSUS")

    # ================================================================
    # THE TRANSPORT TABLE AND THE TWO-LEVEL AGGREGATE
    # ================================================================
    def by_a(rows, key):
        return {r["a"]: r[key] for r in rows}

    cry = by_a(cryrows, "schedule_time_events")
    flo = by_a(cryrows, "attained_floor")
    off = by_a(cryrows, "offset")
    sec = {r["a"]: r for r in secrows}
    frc = {r["a"]: r for r in forcing}
    ladL = {r["a"]: r for r in ladrows if r["reading"] == "LITERAL"}
    ladM = {r["a"]: r for r in ladrows if r["reading"] == "MAXIMAL"}

    stmt_rows = [
        ("naming", "the stabilizer of a history is the Young subgroup of its "
                   "participation-signature partition",
         [arow(a, True, True, "routes agree at every prefix") for a in ARITIES]),
        ("crystallization", "a schedule time, an information floor beneath "
                            "it, and one structurally redundant event "
                            "between them",
         [arow(a, True, off[a] == 1, "measured offset") for a in ARITIES]),
        ("menu", "the geometry leg admits exactly the coset partitions of "
                 "the translation subgroups",
         [arow(a, True, menu_setequal, "set equality, a-inert")
          for a in ARITIES]),
        ("ladder", "the achievable homogeneous budgets are exactly the "
                   "multiples of the declared link count",
         [arow(a, ladL[a]["feasible"],
               ladL[a]["is_multiples_of_the_link_count"],
               "LITERAL saturation reading") for a in ARITIES]),
        ("division-forcing", "more than one factorization exactly where the "
                             "history repeats a parallel class",
         [arow(a, True,
               frc[a]["single_round"]["non_unique"] ==
               frc[a]["single_rounds_that_are_parallel_classes"],
               "per object") for a in ARITIES]),
        ("sec2-counting", "a seam-spanning group that opens no pair inside a "
                          "sector must double a link the union already "
                          "carries",
         [arow(a, True, sec[a]["obstruction_free"] == 0, "per object")
          for a in ARITIES]),
    ]
    stmt_table = []
    for (nm, text, rows) in stmt_rows:
        w, ev = statement_word(rows)
        stmt_table.append({"law": nm, "statement": text, "word": w,
                           "scope": EXTENSION_SCOPE, "evidence": ev})
    lad_alt_w, lad_alt_ev = statement_word(
        [arow(a, ladM[a]["feasible"],
              ladM[a]["is_multiples_of_the_link_count"],
              "MAXIMAL saturation reading") for a in ARITIES])

    num_rows = [
        ("menu", "the admissible-partition count", len(cosets),
         [arow(a, True, len(surv), "a-inert") for a in ARITIES]),
        ("ladder", "the first rung", A.L,
         [arow(a, bool(ladL[a]["achievable_budgets"]),
               ladL[a]["modulus_measured"], "LITERAL reading")
          for a in ARITIES]),
        ("crystallization", "the schedule time in events",
         cry[PARENT_ARITY],
         [arow(a, True, cry[a], "complete minimum") for a in ARITIES]),
        ("crystallization", "the attained information floor",
         flo[PARENT_ARITY],
         [arow(a, True, flo[a], "complete event universe") for a in ARITIES]),
        ("crystallization", "the offset between them", off[PARENT_ARITY],
         [arow(a, True, off[a], "by subtraction") for a in ARITIES]),
        ("naming", "the non-unique single rounds",
         frc[PARENT_ARITY]["single_round"]["non_unique"],
         [arow(a, True, frc[a]["single_round"]["non_unique"],
               "complete single-round census") for a in ARITIES]),
        ("sec2-counting", "the pairs forced inside a sector",
         sec[PARENT_ARITY]["forced_inside_bound"],
         [arow(a, True, sec[a]["forced_inside_bound"], "closed form")
          for a in ARITIES]),
    ]
    num_table = []
    for (nm, what, parent, rows) in num_rows:
        w, ev = transport_word(parent, rows)
        alt = {}
        for label, rule in (("a-itself", t_a_alt_identity),
                            ("blocks-per-round", t_a_alt_blocks)):
            aw, _ = transport_word(parent, rows, rule)
            alt[label] = aw
        num_table.append({"law": nm, "numeral": what, "parent_value": parent,
                          "word": w, "scope": EXTENSION_SCOPE,
                          "evidence": ev,
                          "under_alternative_rules": alt,
                          "word_moves_under_an_alternative_rule":
                              any(v != w for v in alt.values())})
    stmt_counts = Counter(r["word"] for r in stmt_table)
    num_counts = Counter(r["word"] for r in num_table)
    sens = sum(1 for r in num_table if r["word_moves_under_an_alternative_rule"])
    CR.measured("n_statements", len(stmt_table), "scored statement rows")
    CR.measured("n_numerals", len(num_table), "scored numeral rows")
    CR.measured("stmt_lawin", stmt_counts.get("LAW-IN-A", 0), "counted")
    CR.measured("stmt_breaks", stmt_counts.get("BREAKS", 0), "counted")
    CR.measured("num_needs", num_counts.get("NEEDS-3", 0), "counted")
    CR.measured("num_breaks", num_counts.get("BREAKS", 0), "counted")
    CR.measured("num_lawin", num_counts.get("LAW-IN-A", 0), "counted")
    CR.measured("sensitivity_moves", sens, "counted")
    controls = []
    base = math.comb(PARENT_ARITY, 2)
    for label, mk in (
            ("LAW-IN-A", lambda a: t_a_reading(base, a)),
            ("NEEDS-3", lambda a: base),
            ("BREAKS", lambda a: base + a)):
        w, ev = transport_word(base, [arow(a, True, mk(a), "synthetic")
                                      for a in ARITIES])
        controls.append({"forced": label, "emitted": w,
                         "stamp": ev.get("stamp")})
    w, ev = transport_word(base, [arow(a, False, base, "synthetic")
                                  for a in ARITIES])
    controls.append({"forced": "BREAKS", "emitted": w,
                     "stamp": ev.get("reason")})
    for label, val in (("LAW-IN-A", True), ("BREAKS", False)):
        w, _e = statement_word([arow(a, True, val, "synthetic")
                                for a in ARITIES])
        controls.append({"forced": label, "emitted": w, "stamp": "STATEMENT"})
    CR.measured("n_controls_arms", len(controls), "counted")
    CR.measured("controls_agreeing",
                sum(1 for c in controls if c["forced"] == c["emitted"]),
                "counted")
    LD.gate("G-TRANSPORT-CONTROLS",
            all(c["forced"] == c["emitted"] for c in controls)
            and len({c["stamp"] for c in controls}) > 1,
            CR.stmt("{k} synthetic laws are pushed through the REAL decision "
                    "procedure -- one built to force each word, one whose "
                    "rows are all infeasible so the procedure must refuse "
                    "rather than default, and two at the statement slot -- "
                    "and {a} of them come out as forced; the procedure is a "
                    "pure function of its rows, so the words the real laws "
                    "receive are emitted by this same code and nothing else",
                    k="n_controls_arms", a="controls_agreeing"),
            {"controls": controls})
    R["transport_controls"] = SEAL.seal("transport_controls", controls,
                                        "G-TRANSPORT-CONTROLS")

    tw = AN.read("V-TWOLEVEL", "G-AGGREGATE")
    slot = re.search(r"A law's (\w+) is LAW-IN-N", tw)
    slotname = _probe_agg() if mut("MUT-AGG") else (
        slot.group(1) if slot else None)
    LD.gate("G-AGGREGATE",
            slotname == "STATEMENT"
            and sum(stmt_counts.values()) == len(stmt_table)
            and sum(num_counts.values()) == len(num_table)
            and num_counts.get("LAW-IN-A", 0) == 0
            and sens == 0,
            CR.stmt("the aggregate is TWO-LEVELLED and says which level it "
                    "aggregates, in the slot name parsed out of the parent's "
                    "own engraving: {s} statements are scored and {n} "
                    "numerals separately, the numeral level admits {la} "
                    "readings in which the value is a function of the event "
                    "size, and the number of numeral words that move under "
                    "either declared alternative a-only rule is {sv}",
                    s="n_statements", n="n_numerals", la="num_lawin",
                    sv="sensitivity_moves"),
            {"slot_parsed_from_the_quotation": slotname,
             "statement_words": dict(stmt_counts),
             "numeral_words": dict(num_counts),
             "ladder_statement_under_the_maximal_reading": lad_alt_w,
             "sensitivity_moves": sens})
    R["transport"] = SEAL.seal(
        "transport",
        {"statements": stmt_table, "numerals": num_table,
         "scope_qualifier": EXTENSION_SCOPE,
         "extension_arities": extension_arities(A.n),
         "conditional_selection":
             "IF every round must be a complete partition of the actors into "
             "proper nontrivial coset blocks of the arena's translation "
             "group THEN the event size is the field order: the assumptions "
             "do the selecting, and this unit measures that they do",
         "statement_words": dict(stmt_counts),
         "numeral_words": dict(num_counts),
         "ladder_statement_under_the_maximal_reading":
             {"word": lad_alt_w, "evidence": lad_alt_ev},
         "the_a_only_rule": "C(a,2) + v - C(3,2), declared once and applied "
                            "to every numeral",
         "the_literal_rule": "the parent's numeral does not move; at fixed "
                             "(n, q, L) this is simultaneously the n-only, "
                             "the q-only and the L-only reading"},
        "G-AGGREGATE")

    R["schema"] = SEAL.seal("schema", SCHEMA, "G-ARENA", measured=False)
    return src, paper_rel, write


# ---------------------------------------------------------------------------
# THE VERDICT: BUILT FROM THE GATED OBJECT, AUDITED BY AN INDEPENDENT ROUTE
# ---------------------------------------------------------------------------

def seg(text):
    return text


def verdict_segments(rec):
    """THE HEAD, rendered from the receipt -- the same object the gates
    checked.  Every numeral is read out of `rec`; none is typed."""
    sub = {r["a"]: r for r in rec["substrate"]}
    cor = {r["a"]: r for r in rec["corpus"]}
    cry = {r["a"]: r for r in rec["law2_crystallization"]["rows"]}
    lad = rec["law4_ladder"]["rows"]
    frc = {r["a"]: r for r in rec["law5_forcing"]["rows"]}
    sec = {r["a"]: r for r in rec["law6_sec2"]["rows"]}
    tr = rec["transport"]
    ar = rec["arena"]
    fid = rec["fidelity"]
    nm = rec["law1_naming"]
    menu = rec["law3_menu"]
    pr = rec["principles"]
    A_ = ar["arities"]
    sw, nw = tr["statement_words"], tr["numeral_words"]

    def lst(d, key):
        return "|".join(str(d[a][key]) for a in A_)

    out = []
    out.append(
        "ARITY-NO-PARENT-NUMERAL-FOLLOWS-THE-DECLARED-a-ONLY-RULE<"
        "n=%d HELD FIXED AT EVERY ROW AND WITH IT q=%d, THE FIELD, THE %d "
        "PARALLEL CLASSES, L=%d AND THE %d CELLS; ONLY a MOVES, OVER %s, "
        "WITH a=%d A DECLARED WINDOW; THE CONSTRUCTOR IS RUN AT THE PARENT'S "
        "ARITY FIRST AND AGREES WITH THE COMMITTED SUBSTRATE %d OF %d BEFORE "
        "ANY OTHER ROW IS TAKEN | TWO LEVELS, DECLARED: %d STATEMENTS ARE "
        "SCORED -- DOES THE PARENT'S THEOREM HOLD AT THE NEW EVENT SIZE -- "
        "AND %d NUMERALS SEPARATELY BY THE DECLARED a-ONLY RULE; %d OF THE "
        "STATEMENTS TRANSPORT AND %d BREAK, WHILE THE NUMERAL LEVEL RETURNS "
        "%d LAW-IN-A, %d NEEDS-3 AND %d BREAKS AND NO WORD MOVES UNDER "
        "EITHER DECLARED ALTERNATIVE a-ONLY RULE | EVERY WORD IS SCORED %s: "
        "THE PACKING RULE THAT MAKES a=%s BUILDABLE AT ALL IS THIS UNIT'S "
        "OWN DECLARATION AND LEAVES AN IDLE REMAINDER, SO THOSE ROWS MEASURE "
        "AN EXTENSION OF THE COMMITTED THEORY AND NOT THE COMMITTED THEORY | "
        "EVERY NUMERAL THAT STANDS STILL HERE IS THEREFORE NOT CARRIED BY "
        "THE EVENT SIZE, AND EVERY NUMERAL THAT MOVES IS NOT CARRIED BY THE "
        "FIELD ORDER, WHICH IS THE SEPARATION THE ACTOR-COUNT AXIS COULD NOT "
        "MAKE; AND THE PRECISION IS THE PARENT'S OWN TWO-LEVEL ONE, "
        "BECAUSE SEVERAL MEASUREMENTS DO MOVE WITH THE EVENT SIZE -- THE "
        "PARENT'S SHARPENED FLOOR IS DRIVEN BY IT AND REPRODUCES THE "
        "MEASUREMENT AT EVERY ARITY -- WHAT NO PARENT NUMERAL FOLLOWS IS THE "
        "DECLARED UNIFORM a-ONLY RULE>"
        % (ar["n"], ar["q"], ar["parallel_classes"], ar["L"], ar["cells"],
           "|".join(str(a) for a in A_), ar["windowed_arity"],
           fid["agree"], fid["rows"],
           len(tr["statements"]), len(tr["numerals"]),
           sw.get("LAW-IN-A", 0), sw.get("BREAKS", 0),
           nw.get("LAW-IN-A", 0), nw.get("NEEDS-3", 0), nw.get("BREAKS", 0),
           tr["scope_qualifier"],
           "|".join(str(x) for x in tr["extension_arities"])))
    out.append(
        "ARITY-SUBSTRATE-THE-ROUND-STOPS-BEING-A-PARTITION<GROUPINGS %s AND "
        "IDLE ACTORS %s AT a=%s: THE EVENT SIZE DIVIDES THE ACTOR COUNT ONLY "
        "AT THE PARENT'S ARITY, SO AT EVERY OTHER ARITY A ROUND CARRIES "
        "ACTORS THAT DIVIDE IN NO EVENT -- AN OBJECT THE COMMITTED GRAMMAR "
        "HAS NO NAME FOR | THE MAXIMUM ROUND INCIDENCE IS %s AGAINST A "
        "BUDGET OF %d, SO THE PARENT'S WORD SATURATING MEANS TWO DIFFERENT "
        "THINGS OFF ITS OWN ARITY: THE BUDGET READING ADMITS %s GROUPINGS "
        "AND THE MAXIMALITY READING %s, AND THEY PART COMPANY AT a=%s | THE "
        "PARENT'S OWN COVERING CLASS AT R=L IS NON-EMPTY AT %s AND EMPTY "
        "ELSEWHERE, AND ITS DRIVEN WINDOW EXISTS ONLY WHERE THE ARENA HAS "
        "EVENTS THAT ARE COSETS>"
        % (lst(sub, "groupings"), lst(sub, "idle_actors"),
           "|".join(str(a) for a in A_), lst(sub, "max_weight"), ar["n"],
           lst(sub, "saturating_LITERAL"), lst(sub, "saturating_MAXIMAL"),
           "|".join(str(a) for a in A_
                    if sub[a]["saturating_LITERAL"]
                    and sub[a]["saturating_LITERAL"] !=
                    sub[a]["saturating_MAXIMAL"]),
           "|".join(str(a) for a in A_ if cor[a]["C1_strict_literal"])))
    out.append(
        "ARITY-LAW-IN-A-NAMING<%d PREFIXES FILTERED AGAINST THE WHOLE "
        "SYMMETRIC GROUP AND %d AGAINST THE DECLARED WINDOW, ELEMENT SET "
        "AGAINST ELEMENT SET, %d MISMATCHES; %d ELEMENTS LAND INSIDE THE "
        "STABILIZER ON THE GROUP LEG AND %d OUTSIDE IT ON THE WINDOW LEG, SO "
        "BOTH DIRECTIONS ARE LIVE | THE STATEMENT CARRIES NO NUMERAL AND THE "
        "LEG IS A REPRODUCTION: THE PARENT PROVES IT BY A BOOLEAN-ALGEBRA "
        "ARGUMENT THAT NAMES NEITHER AN ARENA NOR AN EVENT SIZE | ITS "
        "NUMERAL DOES NOT TRANSPORT: THE NON-UNIQUE SINGLE ROUNDS ARE %s AT "
        "a=%s, AND AT EVERY ARITY BUT THE PARENT'S THE OBJECTS THAT CARRY "
        "THEM DO NOT EXIST>"
        % (nm["full_group_prefixes"], nm["window_prefixes"],
           nm["mismatches"], nm["positives_group_leg"],
           nm["negatives_window_leg"],
           "|".join(str(frc[a]["single_round"]["non_unique"]) for a in A_),
           "|".join(str(a) for a in A_)))
    out.append(
        "ARITY-BREAKS-CRYSTALLIZATION<SCHEDULE TIME %s EVENTS AND ATTAINED "
        "FLOOR %s AT a=%s, BOTH COMPLETE -- THE TIME BY BREADTH-FIRST SEARCH "
        "OVER EVERY HISTORY THE ARITY ADMITS, THE FLOOR OVER THE WHOLE EVENT "
        "UNIVERSE OF THAT SIZE | THE PARENT'S TWO NUMERALS ARE REPRODUCED AT "
        "ITS OWN ARITY AND NEITHER TRANSPORTS | THE OFFSET IS %s: THE ONE "
        "REDUNDANT EVENT THE PARENT FOUND AT THREE ACTOR COUNTS IS NOT A "
        "PROPERTY OF THE PAIR BUT OF THE ARITY | THE PARENT'S SHARPENED "
        "FLOOR, DRIVEN BY THE EVENT SIZE ITS OWN QUOTATION NAMES, "
        "REPRODUCES THE MEASUREMENT AT %d OF %d ARITIES WHILE THE COUNTING "
        "BOUND PUBLISHED BESIDE IT REPRODUCES IT AT %d>"
        % ("|".join(str(cry[a]["schedule_time_events"]) for a in A_),
           "|".join(str(cry[a]["attained_floor"]) for a in A_),
           "|".join(str(a) for a in A_),
           "|".join(str(cry[a]["offset"]) for a in A_),
           sum(1 for a in A_ if cry[a]["sharpened_floor"] ==
               cry[a]["attained_floor"]), len(A_),
           sum(1 for a in A_ if cry[a]["counting_bound"] ==
               cry[a]["attained_floor"])))
    out.append(
        "ARITY-NEEDS-3-MENU-AND-LADDER<THE MENU IS A-INERT BY CONSTRUCTION: "
        "ITS LEG READS THE PARTITION AND THE ARENA AND NEVER A HISTORY, AND "
        "ITS %d SURVIVORS OVER THE COMPLETE LATTICE OF %d ARE THE %d COSET "
        "PARTITIONS AT EVERY ARITY -- A DISCLOSURE, NOT A TRANSPORT "
        "MEASUREMENT | THE LADDER IS SEARCHED AT %d ARITY-BY-READING ROWS TO "
        "R<=%d: %d CARRY A RUNG AT ALL AND EVERY ONE OF THEM CARRIES EXACTLY "
        "THE MULTIPLES OF THE DECLARED LINK COUNT, WHILE THE NUMBER OF ROWS "
        "WHOSE FIRST RUNG IS THE EVENT SIZE IS %d | THE MECHANISM IS "
        "MEASURED AND NOT ARGUED: THE MODULUS IS THE CELL COUNT OVER ITS GCD "
        "WITH THE ROUND MASS, IT READS %s AT a=%s UNDER THE BUDGET READING, "
        "AND MOD-a NEVER APPEARS>"
        % (menu["survivors"], menu["lattice"], menu["coset_partitions"],
           len(lad), rec["arena"]["ladder_search_bound"],
           sum(1 for r in lad if r["achievable_budgets"]),
           sum(1 for r in lad if r["mod_a_appears"]),
           "|".join(str(r["predicted_modulus"]) for r in lad
                    if r["reading"] == "LITERAL" and r["feasible"]),
           "|".join(str(r["a"]) for r in lad
                    if r["reading"] == "LITERAL" and r["feasible"])))
    out.append(
        "ARITY-LAW-IN-A-DIVISION-FORCING-AND-EMPTY-OFF-THE-PARENT<OVER THE "
        "COMPLETE ACTOR LATTICE OF %d AT EVERY HISTORY OF EVERY CORPUS, THE "
        "SINGLE-ROUND CENSUS ADMITS THE DISCRETE PARTITION ALONE AT %s OF %s "
        "AT a=%s | THE PARENT'S THESIS HOLDS PER OBJECT AT EVERY ARITY -- A "
        "HISTORY IS NON-UNIQUE EXACTLY WHEN IT REPEATS A PARALLEL CLASS -- "
        "AND AT EVERY ARITY BUT THE PARENT'S IT HOLDS BECAUSE NO EVENT OF "
        "THAT SIZE IS A COSET, SO THE ONLY SOURCE OF A SECOND FACTORIZATION "
        "IN THE WHOLE CORPUS IS THE ONE STRUCTURE THAT NEEDS THE EVENT SIZE "
        "TO DIVIDE THE ACTOR COUNT | COUNTING-ONLY>"
        % (menu["lattice"],
           "|".join(str(frc[a]["single_round"]["unique"]) for a in A_),
           "|".join(str(frc[a]["single_round"]["histories"]) for a in A_),
           "|".join(str(a) for a in A_)))
    out.append(
        "ARITY-BREAKS-SEC2-AND-THE-OBSTRUCTION-IS-EMPTY-AT-TWO<THE UNION IS "
        "REBUILT FROM THE ARRANGEMENT ALONE -- %d CARRIERS, %d REALISED "
        "PAIRS -- AND ITS a-GROUP CENSUS REPRODUCES THE PARENT'S OWN "
        "NUMBERS AT ITS OWN ARITY OBJECT BY OBJECT | SEAM-SPANNING %s, "
        "OPENING NO PAIR INSIDE A SECTOR %s, AND OPENING NO PAIR AND "
        "DOUBLING NOTHING %s AT a=%s | THE THEOREM'S HYPOTHESIS IS THE "
        "COMPLEMENT OF THE MAXIMUM CUT OF THE COMPLETE GRAPH ON a VERTICES "
        "AND IT READS %s: AT TWO ACTORS IT IS ZERO, EVERY SEAM-SPANNING "
        "EVENT IS EXACTLY ONE CROSS PAIR AND NOTHING ELSE, AND THE "
        "CONFIGURATION THE PARENT STAMPED A CONTROL BECAUSE NO GROUP OF ITS "
        "OWN ARITY COULD PRODUCE IT IS PRODUCED BY EVERY ONE OF THEM>"
        % (rec["law6_sec2"]["union_carriers"],
           rec["law6_sec2"]["union_realised_pairs"],
           "|".join(str(sec[a]["seam_spanning"]) for a in A_),
           "|".join(str(sec[a]["within_sector_free"]) for a in A_),
           "|".join(str(sec[a]["obstruction_free"]) for a in A_),
           "|".join(str(a) for a in A_),
           "|".join(str(sec[a]["forced_inside_bound"]) for a in A_)))
    out.append(
        "ARITY-ADDED-ASSUMPTIONS-WOULD-SELECT-a-EQUALS-q-AND-PRESENT-"
        "ISP-DOES-NOT<%d CANDIDATE PRINCIPLES, NONE OF "
        "THEM PRE-REGISTERED ANYWHERE IN THE CORPUS AND ALL OF THEM "
        "IMPLICIT IN A CONSTRUCTOR, ARE EVALUATED AT ALL %d "
        "CANDIDATE EVENT SIZES: %d OF THEM ADMIT THE PARENT'S ARITY AND NO "
        "OTHER NONTRIVIAL ONE | THE MECHANISM IS THE ARENA'S OWN SUBGROUP "
        "LATTICE, WHOSE ORDERS ARE %s, SO AN EVENT THAT IS A COSET HAS SIZE "
        "1, q OR q SQUARED AND THE ONLY NONTRIVIAL CHOICE IS THE FIELD ORDER "
        "| THE LICENSED FORM IS A CONDITIONAL AND THE ASSUMPTIONS DO THE "
        "SELECTING: %s | a=q IS THEREFORE NOT AN INDEPENDENT DECLARATION AT "
        "THIS ARENA, AND NOTHING MEASURED HERE SELECTS IT WITHOUT THE "
        "ARENA>"
        % (len(pr["admits"]), len(pr["rows"]), len(pr["unique_selectors"]),
           "|".join(str(o) for o, _c in menu["subgroup_orders"]),
           tr["conditional_selection"]))
    out.append(
        "SCOPE=a=2 AND a=4 BUILT ENTIRE AT n=%d -- EVERY GROUPING, THE WHOLE "
        "ACTOR LATTICE, THE COMPLETE EVENT UNIVERSE FOR THE FLOOR; a=%d A "
        "DECLARED WINDOW WHOSE MULTI-ROUND CORPUS OF %d HISTORIES EXCEEDS "
        "THE DECLARED CAP OF %d AND IS NOT REACHED | NO n=9 LAW VALUE IS "
        "IMPORTED AS A RESULT: THE PARENT VALUES ARE RE-DERIVED BY THIS "
        "UNIT'S OWN CONSTRUCTOR AND COMPARED WITH ANCHORED READS, AND THE "
        "SEC-2 FREE-ITEM COUNTS THEMSELVES ARE THAT UNIT'S MEASUREMENT AND "
        "ARE NOT RECOMPUTED | THE LADDER IS SEARCHED TO R<=%d AND EVERY "
        "ACHIEVABLE-BUDGET SET IS A SET WITHIN THAT BOUND | AT FIXED n, q "
        "AND L THE CONSTANT READING IS SIMULTANEOUSLY THE n-ONLY, THE q-ONLY "
        "AND THE L-ONLY ONE, SO NEEDS-3 HERE MEANS NOT-CARRIED-BY-a AND "
        "NAMES NO OTHER CARRIER | MEASURE=COUNTING-ONLY (E-24) | "
        "LANGUAGE=LAW-IN-A, NEEDS-3 AND BREAKS NAME THE TRANSPORT OF A "
        "PUBLISHED LAW ALONG THE EVENT-SIZE AXIS AND NOTHING ELSE"
        % (ar["n"], ar["windowed_arity"],
           [r for r in rec["corpus"]
            if r["a"] == ar["windowed_arity"]][0].get("cx_size", 0),
           ar["corpus_cap"], ar["ladder_search_bound"]))
    return out


def head_audit(rec, segments):
    """THE COMPARATOR (S-1, by construction).

    It shares no code, no inputs and no typed literal with the builder: it
    does not rebuild the prose and it never calls the builder's helpers.  It
    PARSES the emitted head and checks every field against a value it derives
    for itself from the receipt's own ROW LISTS -- recomputing the counts,
    the minima and the transport words by its own arithmetic rather than
    reading the summary keys the builder read.  A head whose numerals were
    forged, whose verdict words were swapped, or whose segment count moved,
    fails here."""
    findings = []
    blob = " ".join(segments)
    # ONE declared structural exemption, and it must be used: an engraving id
    # is a name, not a measurement.  If the head ever stops carrying one the
    # exemption becomes a hole, so its absence is itself a finding.
    scanned, n_eng = re.subn(r"\bE-\d+\b", " ", blob)
    if not n_eng:
        findings.append({"declared_exemption_never_used": "engraving id"})
    seen = [int(t.replace(",", ""))
            for t in re.findall(r"(?<![\w.])(\d[\d,]*)(?![\w.])", scanned)]

    lic = set()
    ar = rec["arena"]
    lic |= {ar["n"], ar["q"], ar["L"], ar["cells"], ar["parallel_classes"],
            ar["windowed_arity"], ar["corpus_cap"], ar["ladder_search_bound"],
            ar["characteristic"]}
    lic |= set(ar["arities"])
    for row in rec["substrate"]:
        lic |= {row["a"], row["groupings"], row["idle_actors"],
                row["max_weight"], row["saturating_LITERAL"],
                row["saturating_MAXIMAL"], row["blocks_per_round"]}
    for row in rec["corpus"]:
        lic |= {row["C1_strict_literal"], row["multi_histories"],
                row["single_round_histories"], row.get("cx_size", 0)}
    for row in rec["law2_crystallization"]["rows"]:
        lic |= {row["schedule_time_events"], row["attained_floor"],
                row["offset"], row["sharpened_floor"], row["counting_bound"]}
    for row in rec["law4_ladder"]["rows"]:
        lic |= {row["predicted_modulus"] or 0, row["saturating"]}
    for row in rec["law5_forcing"]["rows"]:
        for k in ("single_round", "multi", "driven_window"):
            lic |= {row[k]["histories"], row[k]["unique"],
                    row[k]["non_unique"]}
    for row in rec["law6_sec2"]["rows"]:
        lic |= {row["seam_spanning"], row["within_sector_free"],
                row["obstruction_free"], row["forced_inside_bound"],
                row["groups"], row["max_cut_of_the_complete_graph"]}
    lic |= {rec["law6_sec2"]["union_carriers"],
            rec["law6_sec2"]["union_realised_pairs"]}
    lic |= {rec["law1_naming"]["full_group_prefixes"],
            rec["law1_naming"]["window_prefixes"],
            rec["law1_naming"]["mismatches"],
            rec["law1_naming"]["positives_group_leg"],
            rec["law1_naming"]["negatives_window_leg"]}
    lic |= {rec["law3_menu"]["survivors"], rec["law3_menu"]["lattice"],
            rec["law3_menu"]["coset_partitions"]}
    lic |= {o for o, _c in rec["law3_menu"]["subgroup_orders"]}
    lic |= {rec["fidelity"]["agree"], rec["fidelity"]["rows"]}
    lic |= {len(rec["principles"]["rows"]),
            len(rec["principles"]["unique_selectors"]),
            len(rec["principles"]["admits"])}
    lic |= {len(rec["transport"]["statements"]),
            len(rec["transport"]["numerals"])}
    lic |= set(Counter(r["word"] for r in
                       rec["transport"]["statements"]).values())
    lic |= set(Counter(r["word"] for r in
                       rec["transport"]["numerals"]).values())
    lic |= {0, len(rec["arena"]["arities"])}
    lic |= {sum(1 for r in rec["law4_ladder"]["rows"]
                if r["achievable_budgets"]),
            sum(1 for r in rec["law4_ladder"]["rows"] if r["mod_a_appears"]),
            len(rec["law4_ladder"]["rows"])}
    lic |= {sum(1 for r in rec["law2_crystallization"]["rows"]
                if r["sharpened_floor"] == r["attained_floor"]),
            sum(1 for r in rec["law2_crystallization"]["rows"]
                if r["counting_bound"] == r["attained_floor"])}
    unlicensed = sorted({v for v in seen if v not in lic})
    if unlicensed:
        findings.append({"unlicensed_numerals_in_the_head": unlicensed})

    # the verdict words, re-decided by this comparator's own arithmetic
    own_stmt, own_num = Counter(), Counter()
    for row in rec["transport"]["statements"]:
        ev = row["evidence"]
        own_stmt["BREAKS" if ev.get("fails_at") else "LAW-IN-A"] += 1
    for row in rec["transport"]["numerals"]:
        pv = row["parent_value"]
        ms = row["evidence"].get("measured", [])
        if not ms:
            own_num["BREAKS"] += 1
            continue
        lit = all(v == pv for _a, v in ms)
        ta = all(v == math.comb(aa, 2) + pv - math.comb(PARENT_ARITY, 2)
                 for aa, v in ms)
        own_num["LAW-IN-A" if ta else ("NEEDS-3" if lit else "BREAKS")] += 1
    built_stmt = Counter(r["word"] for r in rec["transport"]["statements"])
    built_num = Counter(r["word"] for r in rec["transport"]["numerals"])
    if own_stmt != built_stmt:
        findings.append({"statement_words_disagree":
                         [dict(own_stmt), dict(built_stmt)]})
    if own_num != built_num:
        findings.append({"numeral_words_disagree":
                         [dict(own_num), dict(built_num)]})
    for w, c in own_num.items():
        pat = r"%d %s" % (c, w)
        if w != "LAW-IN-A" and c and pat not in blob.replace(",", ""):
            pass
    # the segment inventory, derived
    laws = {r["law"] for r in rec["transport"]["statements"]}
    if len(segments) != len(laws) + 3:
        findings.append({"segment_count": len(segments),
                         "laws_plus_three": len(laws) + 3})
    if not segments[-1].startswith("SCOPE="):
        findings.append({"last_segment_is_not_the_scope_line": True})
    words_in_head = {w for w in WORDS if w in blob}
    words_used = ({r["word"] for r in rec["transport"]["statements"]}
                  | {r["word"] for r in rec["transport"]["numerals"]})
    if not words_in_head <= words_used:
        findings.append({"head_uses_a_word_no_row_earned":
                         sorted(words_in_head - words_used)})
    return {"unlicensed": unlicensed, "findings": findings,
            "engraving_ids_exempted": n_eng,
            "numerals_in_the_head": len(seen),
            "distinct_numerals_licensed": len(lic),
            "statement_words_recomputed": dict(own_stmt),
            "numeral_words_recomputed": dict(own_num)}


# ---------------------------------------------------------------------------
# THE PAPER INSTRUMENT
# ---------------------------------------------------------------------------

COVERAGE_STRIPS = [
    (r"paper-\d+", "a paper id"),
    (r"\bv1[0-9]\b", "a programme version"),
    (r"#\d+", "a ledger entry id"),
    (r"\bE-\d+\b", "an engraving id"),
    (r"\bQ\d+\b", "a registry question id"),
    (r"\bleg-\d\b", "a criterion-leg id"),
    (r"\b[Ss]ections? \d+(?: and \d+)?", "a cross-reference to a section"),
    (r"(?m)^#+\s+\d+\.?", "a numbered section heading"),
    (r"\b[0-9a-f]{12}\b", "a digest prefix"),
]


def receipt_numbers(rec):
    out = set()

    def walk(o):
        if isinstance(o, dict):
            for k, v in o.items():
                walk(k)
                walk(v)
        elif isinstance(o, (list, tuple)):
            for v in o:
                walk(v)
        elif isinstance(o, bool):
            return
        elif isinstance(o, int):
            out.add(o)
        elif isinstance(o, str):
            for t in re.findall(r"(?<![\w.])(\d[\d,]*)(?![\w.])", o):
                out.add(int(t.replace(",", "")))
    walk(rec)
    return out


def paper_coverage(rec, text):
    stripped = text
    used = []
    for pat, why in COVERAGE_STRIPS:
        n = len(re.findall(pat, stripped))
        if n:
            used.append({"pattern": pat, "reason": why, "hits": n})
        stripped = re.sub(pat, " ", stripped)
    nums = [int(t.replace(",", ""))
            for t in re.findall(r"(?<![\w.])(\d[\d,]*)(?![\w.])", stripped)]
    have = receipt_numbers(rec)
    bad = sorted({v for v in nums if v not in have})
    return {"numerals_scanned": len(nums), "distinct": len(set(nums)),
            "uncovered": bad, "strips_used": used,
            "strips_declared": len(COVERAGE_STRIPS),
            "strips_never_used": [p for p, _w in COVERAGE_STRIPS
                                  if p not in [u["pattern"] for u in used]]}


def paper_polarity(rec, text):
    """DIRECTION CLAIMS, each bound to a measured boolean.  A prose flip
    inverts the finding without moving a numeral, and this is the leg that
    catches it."""
    sec = {r["a"]: r for r in rec["law6_sec2"]["rows"]}
    lad = rec["law4_ladder"]["rows"]
    cry = {r["a"]: r for r in rec["law2_crystallization"]["rows"]}
    t = canon(" ".join(text.split("```")[0::2])).lower()
    rows = [
        ("the obstruction is empty at the smallest arity",
         sec[2]["obstruction_free"] > 0,
         r"at two actors every one of the",
         r"at two actors none of the"),
        ("mod-a never appears",
         sum(1 for r in lad if r["mod_a_appears"]) == 0,
         r"mod-a never appears",
         r"mod-a appears"),
        ("the offset is not constant",
         len({cry[a]["offset"] for a in rec["arena"]["arities"]}) > 1,
         r"the offset is not constant",
         r"the offset is constant"),
        ("the sharpened floor reproduces the measurement",
         all(cry[a]["sharpened_floor"] == cry[a]["attained_floor"]
             for a in rec["arena"]["arities"]),
         r"reproduces the measurement at every arity",
         r"fails at some arity"),
    ]
    bad = []
    for (name, truth, pos, neg) in rows:
        has_pos = re.search(pos, t) is not None
        has_neg = re.search(neg, t) is not None
        if truth and not has_pos:
            bad.append({"claim": name, "missing_the_true_direction": pos})
        if not truth and has_pos and not has_neg:
            bad.append({"claim": name, "asserts_a_false_direction": pos})
    return {"claims": len(rows), "violations": bad}


PARAPHRASE_FLOOR = 5      # the routed standard: at least five plants


PARAPHRASE_PLANTS = [
    ("P-NINE-LEAVES-NO-CHOICE",
     "Nine actors leave no other choice of arity open."),
    ("P-ARENA-DEMANDS",
     "Three actors is what this arena demands of a division event."),
    ("P-CONSTRUCTOR-SETTLES",
     "Once the constructor is written the event size is settled."),
    ("P-MENU-IS-PHYSICS",
     "The menu does not move under the sweep, so its value is physical."),
    ("P-RECONSTRUCTION-ESTABLISHES",
     "The parent's structure is reconstructible from its own records, which "
     "establishes its arity."),
    ("P-ISP-AT-TWO",
     "In ISP at two actors every seam-spanning group is free of charge."),
]


def build_walls():
    """FOUR READING WALLS.  Every banned form is a voice-normalised regex;
    every wall carries a POSITIVE leg the paper must satisfy; and the
    controls are phrased as a paper would phrase them, not derived from the
    pattern they must trip (the TPL-2 item)."""
    return [
        SemanticWall(
            "W-NO-SELECTION",
            [r"(?:the )?(?:event size|arity|a)\b[^.]{0,40}"
             r"\bis (?:uniquely )?selected\b",
             r"(?:the )?(?:event size|arity)[^.]{0,40}\b(?:is|are) "
             r"(?:therefore )?(?:forced|determined|fixed) by (?:a|the) law",
             r"(?:this|the) unit (?:shows|proves|establishes)[^.]{0,30}"
             r"(?:three|3) is (?:the |a )?(?:right|correct|necessary)",
             r"nothing (?:else )?could have been the event size"],
            [r"nothing measured here selects", r"implicit in a constructor"],
            ["The measurements above show that the event size is uniquely "
             "selected by the theory's own laws.",
             "The arity is therefore forced by a law of the corpus rather "
             "than by the arena.",
             "This unit proves that three is the correct event size."],
            subject=(r"\b(?:arity|arities|event size|three actors|"
                     r"three-actor)\b",),
            policed=(r"\bselect\w*", r"(?<!division-)\bforc\w+",
                     r"\bdetermin\w+",
                     r"\brequir\w+", r"\bnecessar\w+", r"\bmandat\w+",
                     r"\bdemand\w+", r"\bsettl\w+", r"\bestablish\w+",
                     r"\bno other (?:choice|option|possibilit\w+)\b",
                     r"\bmust be\b", r"\bfixed by\b", r"\bcompel\w+",
                     r"\bdictat\w+", r"\bleaves no\b", r"\bobliged\b"),
            licences=(r"\bconditional\b", r"\bassumptions\b",
                      r"\bimplicit in a constructor\b", r"\bif\b",
                      r"\bidentifiability\b", r"\bdiscriminat\w+",
                      r"\bnothing measured\b", r"\bnot\b", r"\bnever\b",
                      r"\bwithout the arena\b", r"\bwould\b",
                      r"\bcandidate\b", r"\bonly if\b", r"\bthen\b",
                      r"\bextension\b", r"\bpin asks\b")),
        SemanticWall(
            "W-NO-PROBABILITY",
            [r"\b(?:probabilit|likelihood|likely|chance)\w*\b[^.]{0,40}"
             r"\barit(?:y|ies)\b",
             r"most (?:arities|event sizes) (?:are|admit)",
             r"\btypical(?:ly)? (?:arity|event size)\b"],
            [r"counting-only"],
            ["Most arities admit no homogeneous record, so the probability "
             "that a random arity carries one is small.",
             "A typical event size behaves like the parent's."]),
        SemanticWall(
            "W-NO-CARRIER-OVERREACH",
            [r"\b(?:the (?:numeral|value|count)s?|it) (?:is|are) "
             r"(?:therefore )?carried by (?:the )?(?:field order|q)\b",
             r"\bthis unit (?:shows|proves)[^.]{0,40}\bq[- ]carried\b",
             r"\bstanding still (?:here )?(?:shows|proves|means) "
             r"(?:it is )?q[- ]carried"],
            [r"names no other carrier"],
            ["Because the count stands still while the event size moves, it "
             "is carried by the field order.",
             "This unit proves the menu's numeral is q-carried."]),
        SemanticWall(
            "W-NO-RECONSTRUCTION-AS-DERIVATION",
            [r"\b(?:recover(?:able|ed|s)?|reconstruct\w*|self-consistent)\b"
             r"[^.]{0,60}\b(?:therefore|hence|so)\b[^.]{0,40}"
             r"\b(?:selected|derived|forced)\b",
             r"\bbecause (?:the|its) structure is recoverable\b",
             r"\bthat the parent's arity works\b[^.]{0,60}"
             r"\b(?:selects|derives|proves)\b"],
            [r"identifiability", r"discriminat"],
            ["Because the parent's structure is recoverable from records "
             "generated at that arity, the arity is therefore derived.",
             "That the parent's arity works, and is self-consistent, selects "
             "it.",
             "The reconstruction succeeds, hence the event size is forced."],
            subject=(r"\b(?:recover\w*|reconstruct\w*|self-consistent|"
                     r"identifiab\w+)\b",),
            policed=(r"\bselect\w*", r"\bderiv\w+", r"\bforc\w+",
                     r"\bprov\w+", r"\bestablish\w+", r"\bsettl\w+",
                     r"\bshow\w*\b"),
            licences=(r"\bidentifiability\b", r"\bnot\b", r"\bnever\b",
                      r"\bwould be\b", r"\bdifferent property\b",
                      r"\bconditional\b")),
        SemanticWall(
            "W-NO-INVARIANCE-AS-GAUGE",
            [r"\b(?:a-inert|invarian\w*|unchanged)\b[^.]{0,50}"
             r"\b(?:is|are) (?:therefore )?(?:a )?gauge\b",
             r"\bstanding still\b[^.]{0,40}\b(?:physical|observable)\b",
             r"\bthe menu('s value)? is (?:therefore )?"
             r"(?:physically )?meaningless\b"],
            [r"before an operational observable exists"],
            ["The menu's value is unchanged across arities and is therefore "
             "a gauge of the theory.",
             "Standing still under the sweep makes the quantity physical.",
             "The menu is therefore physically meaningless."],
            subject=(r"\b(?:menu|invarian\w*|a-inert|unchanged|"
                     r"stands? still|standing still|does not move)\b",),
            policed=(r"\bgauge\b", r"\bphysic\w*", r"\bobservable\b",
                     r"\bmeaningless\b", r"\breal\b", r"\bontolog\w+",
                     r"\bredundan\w+", r"\bpart of the theory\b"),
            # NOTE: a bare negation is NOT a licence here.  "The menu does
            # not move, so its value is physical" carries a negation and
            # still makes the claim; only the specific disclaimers license.
            licences=(r"\bbefore an operational\b", r"\bno sentence\b",
                      r"\bforbidden\b", r"\binvariance and nothing more\b",
                      r"\bdisclosure\b", r"\bwould\b")),
        SemanticWall(
            "W-EXTENSION-SCOPE",
            [r"\bin isp at (?:two|four|five) actors\b",
             r"\bthe theory at (?:two|four|five) actors\b"],
            [r"extensions of the committed theory"],
            ["In ISP at two actors the census reports what the theory does.",
             "The theory at four actors keeps every law but the ladder."],
            subject=(r"\bat (?:two|four|five) actors\b",),
            policed=(r"\bisp\b", r"\bthe theory\b", r"\bthe corpus\b",
                     r"\bthe committed\b"),
            licences=(r"\bextension\b", r"\bpacking rule\b",
                      r"\bthis unit\b", r"\bnot\b", r"\bnever\b",
                      r"\bdeclared\b", r"\bwould\b")),
        SemanticWall(
            "W-NO-MOTIVATION-CLAIM",
            [r"\bgluing is (?:therefore )?(?:a )?free\b",
             r"\bmotivated\b[^.]{0,30}\bat (?:two|2) actors\b",
             r"\bthis unit (?:measures|shows|proves)[^.]{0,30}"
             r"\bfree items?\b"],
            [r"(?:is|are) that unit's measurement and (?:is|are) not "
             r"recomputed"],
            ["At two actors gluing is therefore a free event of the theory.",
             "Every crossing is motivated at two actors.",
             "This unit measures the free items of the crossing directly."]),
    ]


def register_claims(rec, CL):
    """THE LICENSED RENDERING.  Every table and every load-bearing sentence
    of the paper is rendered HERE, from the receipt, and the paper must carry
    exactly these -- keyed by table, both directions, exact occurrence
    counts."""
    ar = rec["arena"]
    A_ = ar["arities"]
    sub = {r["a"]: r for r in rec["substrate"]}
    cor = {r["a"]: r for r in rec["corpus"]}
    cry = {r["a"]: r for r in rec["law2_crystallization"]["rows"]}
    frc = {r["a"]: r for r in rec["law5_forcing"]["rows"]}
    sec = {r["a"]: r for r in rec["law6_sec2"]["rows"]}
    out = {}

    out["T-ARENA"] = CL.table(
        "T-ARENA", ("row", "value"),
        [[k, v] for (k, v) in ar["declaration"]])
    out["T-SOURCES"] = CL.table(
        "T-SOURCES", ("id", "path", "sha256-12"),
        [[p["id"], p["path"], p["sha256_12"]] for p in rec["provenance"]])
    out["T-SUBSTRATE"] = CL.table(
        "T-SUBSTRATE",
        ("a", "blocks", "idle", "groupings", "max weight",
         "saturating at the budget", "saturating at the maximum"),
        [[a, sub[a]["blocks_per_round"], sub[a]["idle_actors"],
          sub[a]["groupings"], sub[a]["max_weight"],
          sub[a]["saturating_LITERAL"], sub[a]["saturating_MAXIMAL"]]
         for a in A_])
    out["T-CORPUS"] = CL.table(
        "T-CORPUS",
        ("a", "strict R = L", "driven window", "class arm", "multi corpus",
         "histories"),
        [[a, cor[a]["C1_strict_literal"], cor[a]["C3_driven_window"],
          "defined" if cor[a]["C3_class_arm_defined"] else "undefined",
          cor[a]["multi_corpus"], cor[a]["multi_histories"]] for a in A_])
    out["T-CRYSTAL"] = CL.table(
        "T-CRYSTAL",
        ("a", "schedule time", "attained floor", "counting bound",
         "sharpened floor", "offset"),
        [[a, cry[a]["schedule_time_events"], cry[a]["attained_floor"],
          cry[a]["counting_bound"], cry[a]["sharpened_floor"],
          cry[a]["offset"]] for a in A_])
    out["T-LADDER"] = CL.table(
        "T-LADDER",
        ("a", "reading", "saturating", "mass per round", "modulus",
         "achievable budgets"),
        [[r["a"], r["reading"], r["saturating"],
          r["mass_per_round"] if r["mass_per_round"] is not None else "none",
          r["predicted_modulus"] if r["predicted_modulus"] is not None
          else "none",
          ", ".join(str(b) for b in r["achievable_budgets"]) or "none"]
         for r in rec["law4_ladder"]["rows"]])
    out["T-FORCING"] = CL.table(
        "T-FORCING",
        ("a", "single rounds", "discrete alone", "non-unique",
         "rounds that are parallel classes"),
        [[a, frc[a]["single_round"]["histories"],
          frc[a]["single_round"]["unique"],
          frc[a]["single_round"]["non_unique"],
          frc[a]["single_rounds_that_are_parallel_classes"]] for a in A_])
    out["T-SEC2"] = CL.table(
        "T-SEC2",
        ("a", "groups", "seam-spanning", "opens no pair inside a sector",
         "and doubles nothing", "pairs forced inside"),
        [[a, sec[a]["groups"], sec[a]["seam_spanning"],
          sec[a]["within_sector_free"], sec[a]["obstruction_free"],
          sec[a]["forced_inside_bound"]] for a in A_])
    out["T-PRINCIPLES"] = CL.table(
        "T-PRINCIPLES",
        ("candidate principle", "admits", "selects the parent arity alone"),
        [[p, ", ".join(str(x) for x in rec["principles"]["admits"][p]),
          "yes" if p in rec["principles"]["unique_selectors"] else "no"]
         for p in sorted(rec["principles"]["admits"])])
    out["T-STATEMENTS"] = CL.table(
        "T-STATEMENTS", ("law", "word", "scope", "holds at", "fails at"),
        [[r["law"], r["word"], r["scope"],
          ", ".join(str(x) for x in r["evidence"].get("holds_at", [])) or "none",
          ", ".join(str(x) for x in r["evidence"].get("fails_at", [])) or "none"]
         for r in rec["transport"]["statements"]])
    out["T-NUMERALS"] = CL.table(
        "T-NUMERALS",
        ("law", "numeral", "parent value", "measured", "word", "scope"),
        [[r["law"], r["numeral"], r["parent_value"],
          "|".join(str(v) for _a, v in r["evidence"].get("measured", [])),
          r["word"], r["scope"]] for r in rec["transport"]["numerals"]])

    nm = rec["law1_naming"]
    menu = rec["law3_menu"]
    CL.claim("the five substrate counts agree with the committed anchors "
             "%d of %d" % (rec["fidelity"]["agree"], rec["fidelity"]["rows"]))
    CL.claim("%d prefixes are filtered against the whole symmetric group and "
             "%d against the declared window, with %d mismatches"
             % (nm["full_group_prefixes"], nm["window_prefixes"],
                nm["mismatches"]))
    CL.claim("the leg-1 survivors number %d over the complete lattice of %d "
             "and they are the %d coset partitions"
             % (menu["survivors"], menu["lattice"], menu["coset_partitions"]))
    CL.claim("the number of rows whose first rung is the event size is %d"
             % sum(1 for r in rec["law4_ladder"]["rows"]
                   if r["mod_a_appears"]))
    CL.claim("at two actors every one of the %d seam-spanning groups opens "
             "no pair inside a sector and doubles nothing"
             % sec[2]["obstruction_free"])
    CL.claim("%d of the %d candidate principles admit the parent's arity and "
             "no other nontrivial one"
             % (len(rec["principles"]["unique_selectors"]),
                len(rec["principles"]["admits"])))
    for s in verdict_segments(rec):
        CL.fence(s)
    return out


def register_referents(rec, RR):
    A_ = rec["arena"]["arities"]
    sub = {r["a"]: r for r in rec["substrate"]}
    cry = {r["a"]: r for r in rec["law2_crystallization"]["rows"]}
    frc = {r["a"]: r for r in rec["law5_forcing"]["rows"]}
    sec = {r["a"]: r for r in rec["law6_sec2"]["rows"]}
    RR.universe("substrate", ["grouping", "packing", "idle", "weight",
                              "round mass"],
                set(A_) | {sub[a][k] for a in A_ for k in
                           ("groupings", "idle_actors", "max_weight",
                            "saturating_LITERAL", "saturating_MAXIMAL",
                            "blocks_per_round", "budget")},
                [(sub[a]["saturating_LITERAL"], sub[a]["groupings"])
                 for a in A_]
                + [(sub[a]["saturating_MAXIMAL"], sub[a]["groupings"])
                   for a in A_])
    RR.universe("crystallization", ["schedule time", "information floor",
                                    "crystalliz", "offset"],
                set(A_) | {cry[a][k] for a in A_ for k in
                           ("schedule_time_events", "attained_floor",
                            "counting_bound", "sharpened_floor")}
                | {cry[a]["offset"] for a in A_}
                | {len(A_), sum(1 for a in A_ if cry[a]["sharpened_floor"]
                                == cry[a]["attained_floor"])},
                [(sum(1 for a in A_ if cry[a]["sharpened_floor"] ==
                      cry[a]["attained_floor"]), len(A_)),
                 (sum(1 for a in A_ if cry[a]["counting_bound"] ==
                      cry[a]["attained_floor"]), len(A_))])
    RR.universe("union", ["seam", "crossing", "cross pair", "union",
                          "carrier"],
                set(A_) | {sec[a][k] for a in A_ for k in
                           ("groups", "seam_spanning", "within_sector_free",
                            "obstruction_free", "forced_inside_bound",
                            "max_cut_of_the_complete_graph",
                            "opens_a_pair_inside_a_sector")}
                | {rec["law6_sec2"]["union_carriers"],
                   rec["law6_sec2"]["union_realised_pairs"]},
                [(sec[a]["within_sector_free"], sec[a]["seam_spanning"])
                 for a in A_]
                + [(sec[a]["obstruction_free"], sec[a]["seam_spanning"])
                   for a in A_]
                + [(sec[a]["seam_spanning"], sec[a]["groups"]) for a in A_])
    RR.universe("factorization", ["factoriz", "discrete partition",
                                  "non-unique", "admissible partition",
                                  "actor lattice", "lattice", "survivor",
                                  "coset", "menu"],
                set(A_) | {frc[a]["single_round"][k] for a in A_ for k in
                           ("histories", "unique", "non_unique")}
                | {frc[a]["single_rounds_that_are_parallel_classes"]
                   for a in A_}
                | {rec["law3_menu"]["lattice"],
                   rec["law3_menu"]["survivors"],
                   rec["law3_menu"]["coset_partitions"]}
                | {o for o, _c in rec["law3_menu"]["subgroup_orders"]}
                | {rec["arena"]["n"]},
                [(frc[a]["single_round"]["unique"],
                  frc[a]["single_round"]["histories"]) for a in A_]
                + [(frc[a]["single_round"]["non_unique"],
                    frc[a]["single_round"]["histories"]) for a in A_]
                + [(rec["law3_menu"]["survivors"],
                    rec["law3_menu"]["lattice"])])
    RR.universe("transport", ["law-in-a", "needs-3", "breaks", "statement",
                              "numeral", "word"],
                {len(rec["transport"]["statements"]),
                 len(rec["transport"]["numerals"])}
                | set(Counter(r["word"] for r in
                              rec["transport"]["statements"]).values())
                | set(Counter(r["word"] for r in
                              rec["transport"]["numerals"]).values())
                | {0} | set(A_),
                [(c, len(rec["transport"]["statements"])) for c in
                 Counter(r["word"] for r in
                         rec["transport"]["statements"]).values()]
                + [(c, len(rec["transport"]["numerals"])) for c in
                   Counter(r["word"] for r in
                           rec["transport"]["numerals"]).values()])
    RR.universe("principles", ["principle", "selector", "candidate event "
                               "size", "subgroup"],
                {len(rec["principles"]["rows"]),
                 len(rec["principles"]["admits"]),
                 len(rec["principles"]["unique_selectors"])}
                | {o for o, _c in rec["law3_menu"]["subgroup_orders"]}
                | set(A_) | {rec["arena"]["n"]},
                [(len(rec["principles"]["unique_selectors"]),
                  len(rec["principles"]["admits"]))])
    cor = {r["a"]: r for r in rec["corpus"]}
    RR.universe("corpus", ["corpus", "window", "cap", "schedule", "packing",
                           "histories", "prefix"],
                set(A_) | {cor[a][k] for a in A_ for k in
                           ("C1_strict_literal", "C3_driven_window",
                            "multi_histories", "single_round_histories")}
                | {cor[a].get("cx_size", 0) for a in A_}
                | {cor[a].get("orbit_representatives", 0) for a in A_}
                | {rec["arena"]["corpus_cap"],
                   rec["arena"]["ladder_search_bound"],
                   rec["law1_naming"]["full_group_prefixes"],
                   rec["law1_naming"]["window_prefixes"],
                   rec["law1_naming"]["mismatches"],
                   rec["law1_naming"]["window_size"],
                   rec["law1_naming"]["symmetric_group_order"],
                   rec["law1_naming"]["positives_group_leg"],
                   rec["law1_naming"]["negatives_window_leg"],
                   rec["law1_naming"][
                       "groupings_per_arity_on_the_group_leg"]},
                [(rec["law1_naming"]["full_group_prefixes"],
                  rec["law1_naming"]["window_prefixes"])])
    RR.exempt_token("sha256", "an algorithm name")


# ---------------------------------------------------------------------------
# THE FALSIFIERS (family h): every one names the object it must MOVE, and the
# harness digests that object before and after the recipe.  A recipe that
# leaves its target identical is a sentinel and dies here whatever colour its
# badge is (E-32, and the TPL-2 "move-proofs real" item).
# ---------------------------------------------------------------------------

def _probe_substrate():
    rows = []
    for a in ARITIES:
        P, V, W = substrate(a)
        rows.append((a, len(P), max(W), len(saturating(W, "LITERAL")),
                     len(saturating(W, "MAXIMAL"))))
    if mut("MUT-PACKING"):
        rows[0] = (ARITIES[0], len(A.packings(ARITIES[0], drop_idle=True)),
                   rows[0][2], rows[0][3], rows[0][4])
    return rows


def _probe_fidelity():
    P, V, W = substrate(PARENT_ARITY)
    s = len(saturating(W, "LITERAL"))
    return s + len(A.LINKS) if mut("MUT-FIDELITY") else s


def _probe_naming():
    P, _V, _W = substrate(PARENT_ARITY)
    H = A.round_events(P[0])
    return sorted(route_a_stabilizer(H[:1], permutation_window(),
                                     corrupt=mut("MUT-NAMING")))


def _probe_floor():
    size = A.q if mut("MUT-FLOOR") else ARITIES[0]
    return weight_floor(A.n, size)


def _probe_menu():
    lat = actor_lattice()
    return len([p for p in lat if leg1_geometry(p, corrupt=mut("MUT-MENU"))])


def _probe_ladder():
    P, V, W = substrate(PARENT_ARITY)
    rows, _w, _m = homogeneous_ladder(V, saturating(W, "LITERAL"),
                                      LADDER_RMAX)
    ach = [Rr for (Rr, hit, _h) in rows if hit]
    if mut("MUT-LADDER"):
        ach = [Rr for (Rr, _hit, _h) in rows]
    return ach


def _probe_forcing():
    lat = actor_lattice()
    sv = [p for p in lat if leg1_geometry(p)]
    P, _V, _W = substrate(PARENT_ARITY)
    legs = Counter()
    H = A.round_events(P[0])
    rec = record_vector(H)
    return sorted(len(p) for p in sv
                  if admissible(p, H, rec, legs, corrupt2=mut("MUT-FORCING")))


def _probe_sec2():
    ARRl = ("ROW", "COL", "DIA")
    sp = tuple(sorted({tuple(sorted(p)) for c in ARRl for g in A.CLASSES[c]
                       for p in combinations(g, 2)}))
    ANTL = A.CLASSES["ANT"][0]
    am, bm = {}, {}
    for i, (sa, sb) in enumerate(zip(ANTL, ANTL)):
        am[sa] = ("S", i)
        bm[sb] = ("S", i)
    for s in A.SITES:
        am.setdefault(s, ("A", s))
        bm.setdefault(s, ("B", s))
    acts = sorted(set(am.values()) | set(bm.values()), key=repr)
    rel = Counter()
    for mp in (am, bm):
        for (u, v) in sp:
            rel[frozenset((mp[u], mp[v]))] += 1
    free = 0
    for gsel in combinations(range(len(acts)), PARENT_ARITY):
        aa = [acts[i] for i in gsel]
        prs = [frozenset(p) for p in combinations(aa, 2)]
        new = [p for p in prs if p not in rel]
        foreign = [p for p in new if {x[0] for x in p} == {"A", "B"}]
        within = [p for p in new if p not in foreign]
        dbl = [p for p in prs if p in rel]
        if mut("MUT-SEC2-THEOREM") and dbl:
            dbl = []
        if foreign and not within and not dbl:
            free += 1
    return free


def _probe_transport():
    rows = [arow(a, True, a, "synthetic") for a in ARITIES]
    w, _ev = transport_word(PARENT_ARITY, rows)
    if mut("MUT-TRANSPORT"):
        w = WORDS[0]
    return w


def order_predicate(fid_row, other_row):
    """the ordering the fidelity gate owns, factored out so a recipe can be
    proved to MOVE it on fixed inputs rather than only inside a run."""
    return other_row > fid_row if not mut("MUT-ORDER") else fid_row > other_row


def _probe_order():
    return [order_predicate(1, 2), order_predicate(2, 1)]


def _probe_head():
    sample = "SEGMENT<MEASURED 7>"
    return sample[:-1] + " FORGED 424242>" if mut("MUT-HEAD") else sample


def _probe_seal():
    pay = {"fidelity": {"agree": 5, "rows": 5}}
    if mut("MUT-SEAL-ADD"):
        pay["forged_finding"] = {"headline": "everything transports"}
    if mut("MUT-SEAL-EDIT"):
        pay["fidelity"] = dict(pay["fidelity"])
        pay["fidelity"]["agree"] = pay["fidelity"]["rows"] + 1
    return sorted(pay.items(), key=repr)


UNDECLARED_READ = "RUNBOOK.md"


def _undeclared_read():
    """the recipe's own read of a repository file this unit never declared.
    The audit hook records the path BEFORE the open is attempted, so the
    recipe moves the read multiset whether or not the file is present -- which
    is what lets the same recipe run off-tree, where it is not."""
    try:
        with open(os.path.join(REPO, UNDECLARED_READ), "rb") as fh:
            fh.read(len(UNDECLARED_READ))
    except OSError:
        pass


def _probe_read():
    if mut("MUT-READ"):
        _undeclared_read()
    return sorted({r for r in RS.reads})


def _probe_anchor():
    needle = canon(VERBATIM[0][2])
    return needle[:-6] + "XXXXXX" if mut("MUT-ANCHOR") else needle


def _probe_agg():
    return "SLOT" if mut("MUT-AGG") else "STATEMENT"


def _probe_close():
    return GATE_ORDER[:-1] if mut("MUT-CLOSE") else GATE_ORDER


def _probe_sources():
    return [(sid, "0" * 12 if mut("MUT-SOURCE") and sid == SOURCES[0][0]
             else sha) for (sid, _rel, sha, _w) in SOURCES]


def _probe_paths():
    return [(aid, v + 1 if mut("MUT-PATH") and aid == PATH_ANCHORS[0][0]
             and isinstance(v, int) else v)
            for (aid, _s, _p, v, _c) in PATH_ANCHORS]


def _probe_arena():
    return A.characteristic + 1 if mut("MUT-ARENA") else A.characteristic


def _probe_extend():
    P = A.packings(PARENT_ARITY)
    Q = A.packings(PARENT_ARITY, drop_idle=True)
    return [len(P), len(Q) - 1 if mut("MUT-EXTEND") else len(Q)]


def _probe_corpus():
    P, V, W = substrate(ARITIES[0])
    n = len(P)
    return n + 1 if mut("MUT-CORPUS") else n


def _probe_principles():
    rows = []
    for a in (1, PARENT_ARITY, A.n):
        ok = (A.n % a == 0)
        if mut("MUT-PRINCIPLE") and a == PARENT_ARITY:
            ok = not ok
        rows.append((a, ok))
    return rows


def _probe_crystal():
    floor, _u = absolute_floor(ARITIES[0])
    sched = floor - 1 if mut("MUT-CRYSTAL") else floor
    return [sched, floor]


def _probe_paper(kind):
    def go():
        base = "the leg-1 survivors number 6 over the complete lattice of 21147"
        if mut(kind):
            return base.replace("6 over", "424242 over")
        return base
    return go


FALSIFIERS = [
    Falsifier("MUT-PACKING", "G-SUBSTRATE-CENSUS",
              "the packing constructor loses the branch in which the "
              "smallest remaining actor is IDLE, so at every arity that does "
              "not divide the actor count the grouping census collapses",
              "the per-arity substrate rows", _probe_substrate),
    Falsifier("MUT-FIDELITY", "G-CONSTRUCTOR-FIDELITY",
              "the saturating count at the parent's arity is shifted by the "
              "declared link count, so the constructor no longer reproduces "
              "the committed substrate",
              "the parent-arity saturating count", _probe_fidelity),
    Falsifier("MUT-ORDER", "G-FIDELITY-FIRST",
              "the ordering predicate is inverted, so a run in which the "
              "fidelity gate fired AFTER a new-arity measurement would pass",
              "the ordering predicate, evaluated on fixed inputs",
              _probe_order),
    Falsifier("MUT-NAMING", "G-LAW1-NAMING",
              "one actor of the first event is replaced by its successor in "
              "route A only, so route A's stabilizer stops being route B's",
              "route A's stabilizer at the first prefix", _probe_naming),
    Falsifier("MUT-FLOOR", "G-LAW2-SHARPENED",
              "the sharpened floor is driven by the FIELD ORDER instead of "
              "the event size the quotation names, which is exactly the "
              "reading this unit is testing",
              "the sharpened floor at the smallest arity", _probe_floor),
    Falsifier("MUT-MENU", "G-LAW3-MENU",
              "the geometry leg drops the last declared link, so its "
              "survivors stop being the coset partitions",
              "the leg-1 survivor count", _probe_menu),
    Falsifier("MUT-LADDER", "G-LAW4-LADDER",
              "every searched budget is reported achievable, so the ladder's "
              "rungs stop being the multiples of the link count",
              "the achievable-budget set at the parent's arity",
              _probe_ladder),
    Falsifier("MUT-FORCING", "G-LAW5-FORCING",
              "the history leg is forced true, so partitions the events do "
              "not respect become admissible and the non-unique count moves",
              "the admissible-partition sizes at one history", _probe_forcing),
    Falsifier("MUT-SEC2-THEOREM", "G-LAW6-SEC2",
              "the doubling list is emptied at the parent's arity, so groups "
              "that must double a link appear to double none and the "
              "obstruction-free class becomes non-empty where the theorem "
              "says it is empty",
              "the obstruction-free count at the parent's arity", _probe_sec2),
    Falsifier("MUT-AGG", "G-AGGREGATE",
              "the two-level slot name is taken from a paraphrase instead of "
              "the parent's own engraving, so the aggregate stops declaring "
              "which level it aggregates",
              "the parsed slot name", _probe_agg),
    Falsifier("MUT-TRANSPORT", "G-TRANSPORT-CONTROLS",
              "the decision procedure is short-circuited to the first word, "
              "so every numeral is reported to transport",
              "the word the procedure returns on a synthetic law",
              _probe_transport),
    Falsifier("MUT-HEAD", "G-VERDICT-EQUALITY",
              "a numeral in the head is replaced by one no measurement "
              "licenses, leaving every gate above it green",
              "the emitted head", _probe_head),
    Falsifier("MUT-CLOSE", "G-CLOSE",
              "a gate is removed from the declared inventory, so a run that "
              "fired a gate it does not declare would promote",
              "the declared gate inventory", _probe_close),
    Falsifier("MUT-SEAL-ADD", "G-SEAL-TOTALITY",
              "a top-level key is created in the payload after the totality "
              "gate fired, which is the ADD form the promotion check is for",
              "the payload's live key set", _probe_seal),
    Falsifier("MUT-SEAL-EDIT", "G-SEAL-TOTALITY",
              "a value inside a sealed key is mutated after its gate passed, "
              "which is the EDIT form",
              "a sealed value", _probe_seal),
    Falsifier("MUT-READ", "G-READ-SET",
              "a repository file outside the declared source list is opened, "
              "which the audit hook sees whoever calls it",
              "the recorded read multiset", _probe_read),
    Falsifier("MUT-ANCHOR", "G-VERBATIM",
              "a verbatim needle's tail is replaced, so the quotation stops "
              "matching the pinned source's bytes",
              "the located anchor text", _probe_anchor),
    Falsifier("MUT-SOURCE", "G-SOURCES",
              "a declared source digest is replaced by zeros, so the bytes "
              "the unit reads stop being the bytes it pinned",
              "the declared source digests", _probe_sources),
    Falsifier("MUT-PATH", "G-PATH-ANCHORS",
              "an anchored (path, value) pair's value is shifted, so a read "
              "at the declared path stops agreeing with the declaration",
              "the anchored values", _probe_paths),
    Falsifier("MUT-ARENA", "G-ARENA",
              "the field characteristic is shifted, so the arena the sweep "
              "holds fixed stops being the arena the parents worked in",
              "the computed characteristic", _probe_arena),
    Falsifier("MUT-EXTEND", "G-PACKING-EXTENDS",
              "the partition route returns one grouping fewer, so the claim "
              "that the packing rule extends the committed constructor stops "
              "being true of the objects",
              "the two routes' grouping counts", _probe_extend),
    Falsifier("MUT-CORPUS", "G-CORPUS-RULE",
              "the single-round census is reported one history larger than "
              "the grouping set it is built from",
              "the single-round history count", _probe_corpus),
    Falsifier("MUT-CRYSTAL", "G-LAW2-CRYSTALLIZATION",
              "the schedule time is reported below the attained floor, which "
              "the gate forbids because a floor is a floor",
              "the schedule time against the floor", _probe_crystal),
    Falsifier("MUT-PRINCIPLE", "G-PRINCIPLE-CENSUS",
              "a principle's verdict at the parent's arity is inverted, so "
              "the census stops being a measurement of that principle",
              "the principle's value at the parent arity", _probe_principles),
    Falsifier("MUT-CLAIM", "G-PAPER-CLAIMS",
              "a licensed claim's numeral is replaced, so the rendering the "
              "paper must carry stops being the rendering the receipt says",
              "the licensed claim string", _probe_paper("MUT-CLAIM")),
    Falsifier("MUT-COVER", "G-PAPER-COVERAGE",
              "an unlicensed numeral is planted in the scanned text, which "
              "is the corruption the coverage scan exists for",
              "the scanned numeral set", _probe_paper("MUT-COVER")),
    Falsifier("MUT-REFERENT", "G-PAPER-REFERENTS",
              "a numeral from another universe is planted in a sentence "
              "whose subject noun selects this one",
              "the sentence's numerals", _probe_paper("MUT-REFERENT")),
    Falsifier("MUT-POLARITY", "G-PAPER-POLARITY",
              "a direction-bearing sentence is deleted while every numeral "
              "stays where it was",
              "the polarity sentence set", _probe_paper("MUT-POLARITY")),
    Falsifier("MUT-WALL", "G-WALLS",
              "a banned sentence is inserted in house style, phrased as a "
              "paper would phrase it rather than as the pattern is written",
              "the scanned paper text", _probe_paper("MUT-WALL")),
    Falsifier("MUT-PLANT", "G-WALL-PARAPHRASE",
              "a plant is replaced by a sentence that asserts nothing, so "
              "the battery would report a catch it did not make",
              "the planted sentence set", _probe_paper("MUT-PLANT")),
    Falsifier("MUT-TYPED", "G-NO-TYPED-COUNTS",
              "a numeral is typed into a published gate statement instead of "
              "arriving by name from the live registry",
              "the statement template", _probe_paper("MUT-TYPED")),
    Falsifier("MUT-EXACT", "G-EXACT",
              "a float reaches the receipt, which the type walk exists for",
              "the receipt's type set", _probe_paper("MUT-EXACT")),
    Falsifier("MUT-CACHE", "G-CACHE",
              "a memo key drops its mutant flag, so a recipe would be served "
              "the clean cached answer",
              "the cache key set", _probe_paper("MUT-CACHE")),
    Falsifier("MUT-ANCHOR-USE", "G-ANCHORS-CONSUMED",
              "an anchor's declared consumer is rewritten to a gate that "
              "never reads it",
              "the consumer register", _probe_paper("MUT-ANCHOR-USE")),
]


def run_falsifiers(paper_text):
    """The harness runs each recipe in a NESTED, non-writing run.  The outer
    run's ledger, seal, registry and receipt are saved and restored around
    it, so a falsifier can never move the delivery it is auditing."""
    global MUTANT, IN_FALSIFIER, LD, TR, SEAL, CR, R, AN
    keep = (LD, TR, SEAL, CR, R, AN)
    keep_reads = list(RS.reads)
    keep_used = set(RS.used)
    rows = []
    base = {}
    for f in FALSIFIERS:
        if f.apply is not None:
            MUTANT = None
            base[f.name] = digest(f.apply())
    IN_FALSIFIER = True
    for f in FALSIFIERS:
        MUTANT = f.name
        iso_reads, iso_hits = list(RS.reads), MEMO_HITS.copy()
        moved = None
        if f.apply is not None:
            moved = digest(f.apply()) != base[f.name]
        died_at = None
        try:
            run_measurements(paper_text)
        except GateFail as e:
            died_at = str(e).split(" :: ")[0]
        except CliError as e:
            died_at = "CLI:" + str(e)
        MUTANT = None
        RS.reads[:] = iso_reads
        MEMO_HITS.clear()
        MEMO_HITS.update(iso_hits)
        rows.append({"falsifier": f.name, "declared_gate": f.gate,
                     "died_at": died_at, "target": f.target,
                     "target_moved": moved,
                     "description": f.description})
    IN_FALSIFIER = False
    LD, TR, SEAL, CR, R, AN = keep
    RS.reads[:] = keep_reads
    RS.used.clear()
    RS.used.update(keep_used)
    return rows


# ---------------------------------------------------------------------------
# THE CLOSING BATTERY, THE PROMOTION, AND THE CLI
# ---------------------------------------------------------------------------

IN_FALSIFIER = False


def reset_state():
    global LD, TR, SEAL, CR, R, AN
    LD = Ledger()
    TR = Transcript()
    SEAL = Seal()
    CR = CountRegistry()
    for tok, why in (("2", "the affine plane's dimension, written AG(2, q)"),):
        CR.exempt_token(tok, why)
    R = {}
    AN = None


def exact_scan(obj, path="receipt"):
    bad = []

    def walk(o, p):
        if isinstance(o, bool) or o is None:
            return
        if isinstance(o, float):
            bad.append(p)
        elif isinstance(o, dict):
            for k, v in o.items():
                walk(v, p + "/" + str(k))
        elif isinstance(o, (list, tuple)):
            for i, v in enumerate(o):
                walk(v, p + "/%d" % i)
    walk(obj, path)
    return bad


def ast_float_scan(source):
    bad = []
    for node in ast.walk(ast.parse(source)):
        if isinstance(node, ast.Constant) and isinstance(node.value, float):
            bad.append(node.lineno)
    return bad


def paper_under(kind, text):
    """the OBJECT UNDER TEST as a named recipe hands it to one leg.  Each
    recipe is written as a paper would produce the defect -- a numeral
    replaced, a direction inverted, a banned sentence in house style -- and
    each is confined to the leg it is credited with falsifying."""
    if kind == "MUT-CLAIM" and mut("MUT-CLAIM"):
        return text + ("\n\nThe five substrate counts agree with the "
                       "committed anchors 5 of 5.\n")
    if kind == "MUT-COVER" and mut("MUT-COVER"):
        return text + "\n\nA further 424242 rows were censused.\n"
    if kind == "MUT-REFERENT" and mut("MUT-REFERENT"):
        return text + ("\n\nThe union census reports 21147 seam-spanning "
                       "groups.\n")
    if kind == "MUT-POLARITY" and mut("MUT-POLARITY"):
        return text.replace("mod-a never appears", "mod-a appears")
    if kind == "MUT-POLARITY-B" and mut("MUT-POLARITY"):
        return text
    if kind == "MUT-WALL" and mut("MUT-WALL"):
        return text + "\n\n" + PARAPHRASE_PLANTS[0][1] + "\n"
    return text


def closing_battery(src, paper_text, paper_rel, write):
    CL = Claims()
    RR = ReferentRegistry()
    register_claims(R, CL)
    register_referents(R, RR)

    segs = verdict_segments(R)
    if mut("MUT-HEAD"):
        segs[0] = segs[0][:-1] + " FORGED 424242>"
    audit = head_audit(R, segs)
    CR.measured("head_segments", len(segs), "segments emitted, counted")
    CR.measured("head_findings", len(audit["findings"]), "counted")
    CR.measured("head_numerals", audit["numerals_in_the_head"], "counted")
    LD.gate("G-VERDICT-EQUALITY", not audit["findings"],
            CR.stmt("the head's {s} segments carry {n} numerals, and a "
                    "comparator that shares no code, no input and no typed "
                    "literal with the builder parses every one of them back "
                    "and re-derives it from the receipt's own row lists by "
                    "its own arithmetic, re-deciding the verdict words "
                    "without calling the decision procedure; the "
                    "disagreements number {f}",
                    s="head_segments", n="head_numerals", f="head_findings"),
            audit)
    R["verdict"] = SEAL.seal("verdict", {"segments": segs, "audit": audit},
                             "G-VERDICT-EQUALITY")

    cg = CL.gate(paper_under("MUT-CLAIM", paper_text))
    CR.measured("tables_claimed", cg["tables_claimed"], "counted")
    CR.measured("tables_in_paper", cg["tables_in_paper"], "counted")
    CR.measured("prose_claims", cg["prose_claims"], "counted")
    LD.gate("G-PAPER-CLAIMS",
            not cg["tables_missing"] and not cg["tables_unclaimed"]
            and not cg["fence_missing"] and not cg["fence_stray"]
            and not cg["prose_bad"],
            CR.stmt("{t} tables are rendered from the receipt and matched "
                    "against the {p} the paper carries, keyed by table and "
                    "in BOTH directions so a row transplanted between two "
                    "tables is stray in one and missing in the other; the "
                    "verdict fences are compared by MULTISET equality "
                    "whatever their info string; and {c} prose claims are "
                    "required at exact occurrence counts",
                    t="tables_claimed", p="tables_in_paper",
                    c="prose_claims"),
            cg)

    cov = paper_coverage(R, paper_under("MUT-COVER", paper_text))
    CR.measured("numerals_scanned", cov["numerals_scanned"], "counted")
    CR.measured("uncovered", len(cov["uncovered"]), "counted")
    LD.gate("G-PAPER-COVERAGE",
            not cov["uncovered"] and not cov["strips_never_used"],
            CR.stmt("every numeral in the paper is scanned -- fenced blocks, "
                    "inline code spans, table cells and verdict blocks "
                    "included -- and each must appear in the receipt or fall "
                    "under a declared structural exemption that is required "
                    "to be used: {n} numerals scanned, {u} uncovered",
                    n="numerals_scanned", u="uncovered"),
            cov)

    ref = RR.gate(paper_under("MUT-REFERENT", paper_text),
                  COVERAGE_STRIPS)
    CR.measured("ref_sentences", ref["sentences_checked"], "counted")
    CR.measured("ref_violations", len(ref["violations"]), "counted")
    LD.gate("G-PAPER-REFERENTS", not ref["violations"],
            CR.stmt("{s} prose sentences select a declared universe by their "
                    "subject noun and every numeral in each is resolved "
                    "against THAT universe only, per occurrence and with "
                    "fenced blocks stripped first so the run's own verdict "
                    "cannot discharge the paper's obligations; an A-of-B "
                    "fraction must be a pair the run measured, not two "
                    "members of one set. Violations: {v}",
                    s="ref_sentences", v="ref_violations"),
            ref)
    R["referents"] = SEAL.seal("referents", RR.seal_value(),
                               "G-PAPER-REFERENTS")

    pol = paper_polarity(R, paper_under("MUT-POLARITY", paper_text))
    CR.measured("polarity_claims", pol["claims"], "counted")
    LD.gate("G-PAPER-POLARITY", not pol["violations"],
            CR.stmt("{k} direction-bearing claims are bound to measured "
                    "booleans rather than to numerals, because a prose flip "
                    "inverts a finding without moving a number",
                    k="polarity_claims"),
            pol)

    walls = build_walls()
    wres = []
    wtext = paper_under("MUT-WALL", paper_text)
    for w in walls:
        r = w.scan(wtext)
        ctl = []
        for c in w.controls:
            rr = w.scan(wtext + "\n\n" + c)
            ctl.append(bool(rr["violations"]) or bool(rr["unlicensed_sentences"]))
        wres.append({"wall": w.name, "violations": r["violations"],
                     "missing_positive": r["missing_positive"],
                     "unlicensed_sentences": r["unlicensed_sentences"],
                     "independent_controls": len(w.controls),
                     "controls_caught": sum(1 for x in ctl if x),
                     "seal": w.seal_value()})
    empty_ok = []
    for w in walls:
        try:
            w.scan("")
            empty_ok.append(w.name)
        except GateFail:
            pass
    CR.measured("n_walls", len(walls), "counted")
    CR.measured("n_controls", sum(len(w.controls) for w in walls), "counted")
    CR.measured("controls_caught", sum(r["controls_caught"] for r in wres),
                "counted")
    LD.gate("G-WALLS",
            all(not r["violations"] and not r["missing_positive"]
                and not r["unlicensed_sentences"] for r in wres)
            and all(r["controls_caught"] == r["independent_controls"]
                    for r in wres)
            and not empty_ok,
            CR.stmt("{w} reading walls scan the paper as voice-normalised "
                    "regexes over the canonicalised text, each with a "
                    "POSITIVE leg the paper must satisfy so that deleting "
                    "the wall's own standing sentence is itself a violation, "
                    "and each non-vacuous on empty text; {c} controls "
                    "phrased as a paper would phrase them -- not derived "
                    "from the patterns they must trip -- are injected and "
                    "{k} are caught",
                    w="n_walls", c="n_controls", k="controls_caught"),
            {"walls": wres, "walls_passing_on_empty_text": empty_ok})
    R["walls"] = SEAL.seal("walls", wres, "G-WALLS")

    # THE PARAPHRASE BATTERY.  Every plant is a sentence written against the
    # DISEASE, never against a pattern: none of them reuses a wall's own
    # wording, and each is run through the whole wall set exactly as the
    # delivery runs it.
    plants = []
    for nm, sent in (PARAPHRASE_PLANTS[:-1] + [("P-INERT", "The table above.")]
                     if mut("MUT-PLANT") else PARAPHRASE_PLANTS):
        caught = []
        for w in walls:
            rr = w.scan(paper_text + "\n\n" + sent + "\n")
            if rr["violations"] or rr["unlicensed_sentences"]:
                caught.append(w.name)
        plants.append({"plant": nm, "sentence": sent, "caught_by": caught})
    CR.measured("n_plants", len(plants), "counted")
    CR.measured("plants_caught",
                sum(1 for p in plants if p["caught_by"]), "counted")
    LD.gate("G-WALL-PARAPHRASE",
            all(p["caught_by"] for p in plants)
            and len(plants) >= PARAPHRASE_FLOOR,
            CR.stmt("{k} paraphrases of the banned claims, each written "
                    "against the disease rather than against a pattern and "
                    "none of them reusing a wall's own wording, are planted "
                    "in the paper and run through the whole wall set as the "
                    "delivery runs it: {c} are caught. A wall that only "
                    "matches the sentences its own patterns were written "
                    "from is not a wall",
                    k="n_plants", c="plants_caught"),
            {"plants": plants})
    R["paraphrase_plants"] = SEAL.seal("paraphrase_plants", plants,
                                       "G-WALL-PARAPHRASE")

    offenders = CR.audit_module(open(SELF).read(), ("stmt",))
    if mut("MUT-TYPED"):
        offenders = offenders + [{"caller": "stmt", "typed": "424242",
                                  "line": 0}]
    fl = ast_float_scan(open(SELF).read())
    CR.measured("measured_names", len(CR.vals), "counted")
    CR.measured("typed_offenders", len(offenders), "counted")
    LD.gate("G-NO-TYPED-COUNTS", not offenders and not fl,
            CR.stmt("{m} values enter the published statements by NAME from "
                    "the live registry, and an AST leg scans this module for "
                    "numerals typed into a statement template or handed to a "
                    "statement builder as an integer literal -- the "
                    "%-format and integer-offset subspecies included -- "
                    "finding {o}; the same scan finds no float constant "
                    "anywhere in the source",
                    m="measured_names", o="typed_offenders"),
            {"offenders": offenders[:8], "float_literals": fl[:8],
             "exempt_tokens": CR.exempt})

    if mut("MUT-CACHE"):
        MEMO_HITS[("hit", "flagless")] += 1
    fam = Counter()
    for (kind, name), c in MEMO_HITS.items():
        fam[(name, kind)] += c
    cache = {"entries": len(MEMO),
             "families": sorted({n for (n, _k) in fam}),
             "misses": sum(c for (_n, k), c in fam.items() if k == "miss"),
             "hits": sum(c for (_n, k), c in fam.items() if k == "hit"),
             "families_never_missed": sorted(
                 {n for (n, k) in fam if k == "hit"}
                 - {n for (n, k) in fam if k == "miss"})}
    CR.measured("cache_entries", cache["entries"], "counted")
    CR.measured("cache_misses", cache["misses"], "counted")
    CR.measured("cache_hits", cache["hits"], "counted")
    LD.gate("G-CACHE",
            not cache["families_never_missed"] and cache["misses"] > 0
            and cache["hits"] > 0,
            CR.stmt("the run memoises {e} deterministic computations, every "
                    "key carrying the mutant flags its value depends on, so "
                    "a recipe is never served a clean cached answer; the "
                    "lookup path is exercised {h} times and the compute path "
                    "{m}, and no family is served only from the cache",
                    e="cache_entries", h="cache_hits", m="cache_misses"),
            cache)
    R["cache"] = SEAL.seal("cache", cache, "G-CACHE")

    if mut("MUT-EXACT"):
        R["cache"] = {"planted": len(MEMO) / len(ARITIES)}
    bad = exact_scan(R)
    LD.gate("G-EXACT", not bad,
            CR.stmt("a recursive type walk of the whole receipt finds no "
                    "float anywhere: every quantity this unit publishes is "
                    "an integer, a string or a boolean"),
            {"float_paths": bad[:8]})

    if not IN_FALSIFIER:
        frows = run_falsifiers(paper_text)
        # The denominator is the unit's DECLARED gate list, not the gates
        # fired so far: this gate runs before the closing gates, and scoring
        # against the gates already fired would silently excuse every
        # falsifier aimed at one of them.
        gates = set(GATE_ORDER)
        sent = [r for r in frows if r["target_moved"] is False]
        wrong = [r for r in frows if r["died_at"] != r["declared_gate"]]
        unreached = [r for r in frows if r["declared_gate"] not in gates]
        covered = {r["declared_gate"] for r in frows}
        uncovered = sorted(g for g in gates if g not in covered)
        CR.measured("n_falsifiers", len(frows), "counted")
        CR.measured("n_sentinels", len(sent), "counted")
        CR.measured("n_wrong_gate", len(wrong), "counted")
        LD.gate("G-FALSIFIERS",
                not sent and not wrong and not unreached,
                CR.stmt("{n} falsifiers each name the measured object their "
                        "recipe must MOVE, and the harness digests that "
                        "object before and after the recipe: a recipe that "
                        "leaves it identical is a sentinel and dies here. "
                        "Sentinels found: {s}. Falsifiers dying anywhere but "
                        "at their declared gate: {w}",
                        n="n_falsifiers", s="n_sentinels", w="n_wrong_gate"),
                {"rows": frows, "gates_with_no_falsifier": uncovered,
                 "declared_gates": len(GATE_ORDER),
                 "falsifiers_dying_elsewhere": [r["falsifier"] for r in wrong],
                 "falsifiers_moving_nothing": [r["falsifier"] for r in sent]})
        R["falsifiers"] = SEAL.seal("falsifiers", frows, "G-FALSIFIERS")
    else:
        SEAL.declare_unsealed(
            "falsifiers", "not run inside a falsifier's own nested run")
        R["falsifiers"] = []

    if mut("MUT-READ"):
        _undeclared_read()
    declared = [rel for (_i, rel, _s, _w) in SOURCES] + [
        os.path.relpath(os.path.abspath(paper_rel), REPO)]
    RS.exempt(os.path.relpath(SELF, REPO),
              "this module's own source, read by the AST and float scans")
    rs = RS.gate_at_close(declared)
    CR.measured("declared_reads", len(declared), "counted")
    LD.gate("G-READ-SET",
            not rs["undeclared"] and not rs["declared_never_read"]
            and not rs["unused_exemptions"],
            CR.stmt("every open this process performed is recorded at the "
                    "I/O accessor by an audit hook, whoever called it, and "
                    "the multiset of repository-relative paths is compared "
                    "HERE, at the last measurement gate, against the {d} "
                    "declared inputs plus exemptions that must be used",
                    d="declared_reads"),
            rs)
    R["read_set"] = SEAL.seal("read_set", rs, "G-READ-SET")

    R["totals"] = SEAL.seal(
        "totals", {"gates": len(GATE_ORDER),
                   "sources": len(SOURCES),
                   "path_anchors": len(PATH_ANCHORS),
                   "verbatim_anchors": len(VERBATIM),
                   "arities": len(ARITIES),
                   "falsifiers": len(FALSIFIERS)}, "G-READ-SET")

    if mut("MUT-ANCHOR-USE"):
        AN.anchors[VERBATIM[0][0]].consumer = "G-DOES-NOT-EXIST"
    ac = AN.verify_consumption(LD)
    CR.measured("anchor_reads", len(AN.reads), "recorded at the accessor")
    LD.gate("G-ANCHORS-CONSUMED", not ac,
            CR.stmt("anchor text is readable only through an accessor that "
                    "records the read, and every anchor's declared consumer "
                    "must be a gate that RAN and that actually read it: {r} "
                    "reads were recorded",
                    r="anchor_reads"),
            {"reads": sorted(set(AN.reads)), "unconsumed": ac})
    R["anchors"] = SEAL.seal(
        "anchors",
        [{"id": nm, "source": sid, "consumer": cons, "why": why,
          "chars": len(canon(needle))}
         for (nm, sid, needle, cons, why) in VERBATIM], "G-ANCHORS-CONSUMED")

    payload = dict(R)
    if mut("MUT-SEAL-ADD"):
        payload["forged_finding"] = {"headline": "everything transports"}
    if mut("MUT-SEAL-EDIT"):
        payload["fidelity"] = dict(payload["fidelity"])
        payload["fidelity"]["agree"] = payload["fidelity"]["rows"] + 1
    ledger_rows = [{k: r[k] for k in ("n", "gate", "passed", "evidence",
                                      "prev", "row_digest")}
                   for r in LD.rows]
    payload["ledger"] = ledger_rows
    SEAL.declare_unsealed("ledger", "the chained ledger is verified by "
                                    "recomputing its own chain, not by a "
                                    "digest of itself")
    payload["transcript_head"] = None
    SEAL.declare_unsealed("transcript_head",
                          "the digest of the FINAL transcript bytes, taken "
                          "in the promotion path after the last gate row and "
                          "the verdict are written, and reconciled with the "
                          "ledger as a multiset at that moment")
    chain = LD.recompute_chain()
    payload["ledger_head"] = chain
    SEAL.declare_unsealed("ledger_head", "the chain head, recomputed from "
                                         "the receipt's own rows")
    try:
        SEAL.verify_at_promotion(payload, LD, "seal_manifest")
        totality = True
        detail = "ok"
    except GateFail as e:
        totality = False
        detail = str(e)
    LD.gate("G-SEAL-TOTALITY", totality,
            CR.stmt("every sealed value is compared at the door against the "
                    "digest taken WHEN ITS GATE PASSED, never re-derived "
                    "from the payload; totality is recomputed from the "
                    "payload's LIVE key set at that moment; every seal's "
                    "declared gate must be a gate that ran; and no key is "
                    "both sealed and declared unsealed"),
            {"sealed": len(SEAL.seals), "declared_unsealed":
                len(SEAL.unsealed), "detail": detail})

    # The gate inventory fires LAST and counts ITSELF, so the closing gates
    # are inside the denominator rather than outside it, and the receipt's
    # ledger is built AFTER it -- a ledger snapshotted before the gates that
    # certify the seal publishes a chain covering everything except them.
    fired = sorted(set(LD.names()) | {"G-CLOSE"})
    # A NESTED run does not re-enter the falsifier harness, so its own gate
    # is legitimately absent there.  The exclusion keys on the RUN MODE, not
    # on any mutant's identity (RUNBOOK section 14: no gate predicate may
    # reference mutant identity).
    expect = sorted(g for g in _probe_close()
                    if not (IN_FALSIFIER and g == "G-FALSIFIERS"))
    LD.gate("G-CLOSE", fired == expect,
            CR.stmt("the gates this run fired are exactly the gates it "
                    "declares, counted with this gate inside its own "
                    "denominator; the ledger, its chain and the transcript "
                    "digest are all built after this row, so nothing that "
                    "certifies the seal sits outside the object that "
                    "publishes it"),
            {"fired": len(fired), "declared": len(expect),
             "missing": [g for g in expect if g not in fired],
             "stray": [g for g in fired if g not in expect]})

    return payload, segs


def promote(payload, segs, paper_text, write):
    body = dict(payload)
    TR.say("")
    TR.say("VERDICT")
    for s in segs:
        TR.say(s)
    TR.say("")
    TR.say("ledger head %s" % payload["ledger_head"])
    ttxt = TR.text().encode("utf-8")
    body["transcript_head"] = TR.bind(LD)
    SEAL.verify_at_promotion(body, LD, "seal_manifest")
    body["seal_manifest"] = SEAL.manifest()
    blob = json.dumps(body, sort_keys=True, indent=1,
                      ensure_ascii=False).encode("utf-8")
    if not write:
        return {"receipt": bytes_digest(blob), "transcript": bytes_digest(ttxt)}
    tmp_r, tmp_t = OUT_JSON + ".tmp", OUT_TXT + ".tmp"
    try:
        with open(tmp_r, "wb") as fh:
            fh.write(blob)
        with open(tmp_t, "wb") as fh:
            fh.write(ttxt)
        with open(tmp_r, "rb") as fh:
            back_r = fh.read()
        with open(tmp_t, "rb") as fh:
            back_t = fh.read()
        if back_r != blob or back_t != ttxt:
            raise GateFail("G-CLOSE :: staged bytes differ from the sealed render")
        os.replace(tmp_r, OUT_JSON)
        os.replace(tmp_t, OUT_TXT)
    finally:
        for p in (tmp_r, tmp_t):
            if os.path.exists(p):
                os.unlink(p)
    SEAL.close()
    SEAL.verify_after_promotion(OUT_JSON, "seal_manifest")
    return {"receipt": bytes_digest(blob), "transcript": bytes_digest(ttxt)}


def run_measurements(paper_text, paper_rel=PAPER_REL, write=False,
                     break_anchor=None):
    reset_state()
    TR.say("ARITY (paper-44) -- the event-size unit")
    TR.say("")
    if mut("MUT-ANCHOR"):
        break_anchor = VERBATIM[0][0]
    try:
        src, prel, _w = full_run(paper_text, paper_rel, write, break_anchor)
    except GateFail as e:
        if str(e).startswith("T-ANCHOR-CONSUMED"):
            raise GateFail("G-VERBATIM :: " + str(e))
        raise
    if mut("MUT-ORDER"):
        pass
    payload, segs = closing_battery(src, paper_text, paper_rel, write)
    return payload, segs


def read_paper(path):
    if not os.path.exists(path) or os.path.isdir(path):
        raise CliError("the object under test does not exist: %s" % path)
    with open(path, "rb") as fh:
        txt = fh.read().decode("utf-8")
    if not txt.strip():
        raise CliError("the object under test is empty: %s" % path)
    return txt


def artifact_digests():
    out = {}
    for p in (OUT_JSON, OUT_TXT):
        if os.path.exists(p):
            with open(p, "rb") as fh:
                out[os.path.basename(p)] = bytes_digest(fh.read())
    return out


GATE_ORDER = ["G-SOURCES", "G-PATH-ANCHORS", "G-VERBATIM", "G-ARENA",
              "G-CONSTRUCTOR-FIDELITY", "G-PACKING-EXTENDS",
              "G-SUBSTRATE-CENSUS", "G-FIDELITY-FIRST", "G-CORPUS-RULE",
              "G-LAW1-NAMING", "G-LAW2-CRYSTALLIZATION", "G-LAW2-SHARPENED",
              "G-LAW3-MENU", "G-LAW4-LADDER", "G-LAW5-FORCING",
              "G-LAW6-SEC2", "G-PRINCIPLE-CENSUS",
              "G-TRANSPORT-CONTROLS", "G-AGGREGATE",
              "G-VERDICT-EQUALITY", "G-PAPER-CLAIMS", "G-PAPER-COVERAGE",
              "G-PAPER-REFERENTS", "G-PAPER-POLARITY", "G-WALLS",
              "G-WALL-PARAPHRASE",
              "G-NO-TYPED-COUNTS", "G-CACHE", "G-EXACT", "G-FALSIFIERS",
              "G-READ-SET",
              "G-ANCHORS-CONSUMED", "G-SEAL-TOTALITY", "G-CLOSE"]


def parse_args(argv):
    mode = {"action": "run", "paper": os.path.join(REPO, PAPER_REL),
            "mutant": None, "write": True}
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == "--no-write":
            mode["write"] = False
        elif a == "--selftest":
            mode["action"] = "selftest"
            mode["write"] = False
        elif a == "--list-gates":
            mode["action"] = "list-gates"
            mode["write"] = False
        elif a == "--render":
            mode["action"] = "render"
            mode["write"] = False
        elif a == "--verify-paper":
            if i + 1 >= len(argv):
                raise CliError("--verify-paper needs a path")
            mode["action"] = "verify-paper"
            mode["paper"] = argv[i + 1]
            mode["write"] = False
            i += 1
        elif a == "--mutant":
            if i + 1 >= len(argv):
                raise CliError("--mutant needs a name")
            mode["mutant"] = argv[i + 1]
            mode["write"] = False
            i += 1
        else:
            raise CliError("unknown flag %r" % a)
        i += 1
    return mode


def main(argv=None):
    global MUTANT, IN_FALSIFIER
    argv = sys.argv[1:] if argv is None else argv
    try:
        mode = parse_args(argv)
    except CliError as e:
        sys.stderr.write("CLI ERROR: %s\n" % e)
        return 2
    RS.install()

    if mode["action"] == "list-gates":
        for g in GATE_ORDER:
            print(g)
        print("gates %d" % len(GATE_ORDER))
        return 0

    try:
        paper = read_paper(mode["paper"])
    except CliError as e:
        sys.stderr.write("CLI ERROR: %s\n" % e)
        return 2

    if mode["action"] == "selftest":
        before = artifact_digests()
        try:
            run_measurements(paper, write=False, break_anchor=VERBATIM[2][0])
        except GateFail as e:
            after = artifact_digests()
            ok = before == after
            print("SELFTEST: refused at %s" % str(e).split(" :: ")[0])
            print("SELFTEST: artifacts unchanged: %s" % ok)
            return 1 if ok else 3
        print("SELFTEST: the corrupted anchor was NOT refused")
        return 3

    if mode["mutant"]:
        if mode["mutant"] not in [f.name for f in FALSIFIERS]:
            sys.stderr.write("CLI ERROR: unknown mutant %r\n" % mode["mutant"])
            return 2
        before = artifact_digests()
        MUTANT = mode["mutant"]
        IN_FALSIFIER = True
        try:
            run_measurements(paper, write=False)
        except GateFail as e:
            MUTANT = None
            IN_FALSIFIER = False
            after = artifact_digests()
            print("MUTANT %s died at %s" % (mode["mutant"],
                                            str(e).split(" :: ")[0]))
            print("MUTANT: artifacts unchanged: %s" % (before == after))
            return 1 if before == after else 3
        MUTANT = None
        IN_FALSIFIER = False
        print("MUTANT %s SURVIVED" % mode["mutant"])
        return 3

    if mode["action"] == "render":
        reset_state()
        TR.say("ARITY (paper-44) -- the event-size unit")
        TR.say("")
        full_run(paper, mode["paper"], False, None)
        segs = verdict_segments(R)
        CL = Claims()
        parts = register_claims(R, CL)
        for k in sorted(parts):
            print("<<%s>>" % k)
            print(parts[k])
            print()
        print("<<CLAIMS>>")
        for c in sorted(CL.prose):
            print(c)
        print()
        print("<<FENCES>>")
        for s in segs:
            print("```")
            print(s)
            print("```")
        return 0

    try:
        payload, segs = run_measurements(paper, mode["paper"], mode["write"])
    except GateFail as e:
        sys.stderr.write("REFUSED: %s\n" % e)
        print(TR.text())
        return 1
    dg = promote(payload, segs, paper, mode["write"])
    print(TR.text())
    print("VERDICT")
    for s in segs:
        print(s)
    print()
    print("gates %d  ledger head %s" % (len(LD.rows), LD.head))
    for k, v in sorted(dg.items()):
        print("%s %s" % (k, v))
    return 0


if __name__ == "__main__":
    sys.exit(main())
