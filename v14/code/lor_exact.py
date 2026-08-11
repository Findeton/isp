#!/usr/bin/env python3.13
# -*- coding: utf-8 -*-
"""
v14 LOR-A -- THE LAW OVER RECORDS AT R = 6: ONE LAWFUL REFINEMENT STEP.
Instrument for `v14/paper-30-lor.md`.

QUESTION (pin `v14/note-lor-pin.md`, sha256-12 5239c4671f1a, ledger #233).
Paper-21 opened the R = 6 door: the welded record (2, 2, 2), reached by
concatenating two of the 72 R = 3 I7-STRICT triples, at >= 5,184 ordered
witnesses, weld fibers 1/1/1 -- and, for the first time in this line, the
refinement laws are NOT empty on it.  This unit asks what one lawful act of
those laws produces, and whether the process-to-space dictionary survives it.

  STAGE 1  THE ARENA BUILT.  The 280 partitions, the budget theorem, the 36
           saturating groupings, the 72 triples and the 5,184 ordered
           concatenations rebuilt from nothing; the (2, 2, 2) field at 27 of
           27 cells; the weld re-verified zero-free on this unit's own
           detector; a DECLARED DRIVEN WINDOW W6 of 13 schedules driven
           through the committed grammar (the first driven R = 6 records);
           the splittable census at n = 2.
  STAGE 2  PAPER-06'S LAW APPLIED.  Non-empty and unique at 27 of 27
           intervals; ONE LAWFUL REFINEMENT STEP taken; the refined interval
           and site structure computed exactly; THE NEW-PLACES COUNT.
  STAGE 3  PAPER-04'S DYADIC LAW APPLIED.  Raw fiber 1; the same step; the
           two refined objects compared.
  STAGE 4  COMPATIBILITY.  Whether the two laws' steps commute, compose or
           conflict -- measured on the objects, not argued.
  STAGE 5  THE REFINED RECORD'S STATUS.  I7 admissibility censused; THE
           DICTIONARY AFTER REFINEMENT -- the extended carrier, the weld
           fibers of the refined record, the process-supply census over all
           5,184 witnesses, the cut theorem; the det/signature data.
  STAGE 6  THE ITERATION CEILING, as an arena theorem, with the ladder.
  STAGE 7  THE DIA ROW -- the diagonal's role in the refined object.

WHAT THIS PROGRAM DOES
  SEC 1  PROVENANCE.  19 pinned sources, sha256-12 verified, products gated;
         path-value anchors; #62 verbatim anchors bound to consumer gates;
         every text gate whitespace-normalises, ASCII-folds AND strips
         markdown prefixes.
  SEC 2  EXACT ARITHMETIC on Z_3^2 and Z_6^2; the partitions; I7's readout.
  SEC 3  THE COMMITTED GRAMMAR, DRIVEN DIRECTLY at R = 6.
  SEC 4  STAGE 1.  SEC 5  STAGE 2.  SEC 6  STAGE 3.  SEC 7  STAGE 4.
  SEC 8  STAGE 5.  SEC 9  STAGE 6/7.  SEC 10  THE WALLS.
  SEC 11 The verdict, derived a second time from the serialized receipt by a
         comparator that types its own templates; the paper gates -- claim
         rendering, numeral coverage INCLUDING FENCED BLOCKS AND INLINE CODE
         SPANS with fence multiset equality, head-verbatim and claim polarity;
         the TOTAL seal; the artifacts; the integrity check.

CLI CONTRACT (the #82 minimum: argv parsed against a whitelist)
---------------------------------------------------------------
    python3.13 v14/code/lor_exact.py
        THE DELIVERY RUN, and the ONLY writer.  Exits 0 iff every gate passes.
    --no-write      the same run, writing nothing.
    --numbers       the census only; nothing written.
    --selftest      corrupts one anchor's expected digest IN MEMORY, confirms
                    the run dies at the anchor gate, WRITES NOTHING, exits 1;
                    exits 2 if the corrupted run does not die.
    --mutant NAME   runs the pipeline with the named mutant active.  Exit 1
                    when killed (intended), 0 if it survives, 2 if unknown.
    --break-anchor NAME   corrupts a named source anchor; must exit 1.
    --verify-paper [PATH] evaluates the paper gates against PATH.
    --list-gates / --list-mutants   print the registries and exit 0.
    Any other argument, any unknown or missing flag argument and any SECOND
    mode flag exits 2.  No flag is a no-op; modes do not compose.

THE TOTAL GATE-TO-DISK SEAL (#119 + #148).  Every published receipt key is
sealed at the moment its gate passes or listed DECLARED-UNSEALED; artifacts
are written from the sealed payload through os.replace; the terminal integrity
gate compares the BYTES ON DISK against the gate-time seal.

ARITHMETIC.  Exact only: Python ints and fractions.Fraction.  An AST scan of
this file and a recursive type scan of the emitted receipt are gates.

RUNTIME INPUTS (#46/#91).  Exactly 19 files are read at run time as SOURCES,
all hash-pinned by this unit's frozen declaration, plus exactly one file read
as the OBJECT UNDER TEST -- this unit's own paper.  No repository state
outside them is read and no subprocess is invoked, so the run is correct
off-tree and with no version control present.
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
OUT_TXT = os.path.join(os.path.dirname(SELF), "lor_output.txt")
OUT_JSON = os.path.join(os.path.dirname(SELF), "lor_receipt.json")

SCHEMA = "isp/v14/lor-a-law-over-records/1"
PAPER_REL = "v14/paper-30-lor.md"

LINES = []
QUIET = False
MUT = None
READS = []
READS_BY_CATEGORY = {}
READ_CATEGORIES = ("SOURCE", "SELF", "OBJECT-UNDER-TEST", "ARTIFACT-STAGED")

# ===========================================================================
# SECTION 0.  THE FROZEN DECLARATION (RUNBOOK section 15: the arena is data)
# ===========================================================================

SOURCES = [
    ("A-PIN", "v14/note-lor-pin.md", "5239c4671f1a",
     "THIS UNIT'S PIN (ledger #233): the seven stages, the outcome names, the "
     "walls, and the new-places language this unit is confined to."),
    ("A-P21", "v14/paper-21-r4dec.md", "ef4a8c35a0c4",
     "PAPER 21 (terminal): G-R6-DOOR -- the 72 triples, the concatenation to "
     "(2, 2, 2), the >= 5,184 witnesses, the 1/1/1 fibers, the RSQ "
     "link-constant theorem, and the dead lists this unit cites."),
    ("A-P21CODE", "v14/code/r4dec_exact.py", "1958a8cdfe28",
     "PAPER 21's INSTRUMENT: the weld detector's two readings and the fiber "
     "definition, reimplemented here and gated against its committed row."),
    ("A-P21REC", "v14/code/r4dec_receipt.json", "a4538c7019e6",
     "PAPER 21's COMMITTED RECEIPT: the G-R6-DOOR row read as data at "
     "/split/r6_door, every number of which is rebuilt here."),
    ("A-P19", "v14/paper-19-r3-weld.md", "50bb81e67942",
     "PAPER 19 (terminal): the weld machinery, the R = 3 landing record "
     "(1, 1, 1) and the rigidity theorem."),
    ("A-P19REC", "v14/code/r3_weld_receipt.json", "dfea664f2408",
     "PAPER 19's COMMITTED RECEIPT: the R = 3 I7-STRICT count, read as data."),
    ("A-P04", "v14/paper-04-refinement-grammar.md", "dfa5090f26b1",
     "PAPER 04 / R6a (terminal): the DYADIC move, the split-fiber identity, "
     "the free-transverse-link wall, the ceiling law and the d = 3 row."),
    ("A-P04REC", "v14/code/r6a_refinement_receipt.json", "856f6e810ab5",
     "PAPER 04's COMMITTED RECEIPT: the move census, the count lattice and "
     "the iteration traces, read as data."),
    ("A-P06", "v14/paper-06-stochastic-split.md", "c350caab17ee",
     "PAPER 06 / CR-B (terminal): the per-interval invariant law, the "
     "transitivity criterion and the named missing object."),
    ("A-P06REC", "v14/code/crb_stochastic_receipt.json", "5ebeec141303",
     "PAPER 06's COMMITTED RECEIPT: the per-interval law rows at every count, "
     "read as data."),
    ("A-P09", "v14/paper-09-renewal-transport.md", "006f96aaa2ff",
     "PAPER 09 / R6b' (terminal): the renewal-grain kernel and its support "
     "hole at counts one and two."),
    ("A-P09REC", "v14/code/r6bp_transport_receipt.json", "9c8f8af07050",
     "PAPER 09's COMMITTED RECEIPT: the kernel's first-return law, read as "
     "data."),
    ("A-HA", "v13/paper-ha-successor.md", "f286ba10d2d9",
     "I7 / HA: the declared readout, the admissibility criterion, and "
     "requirement 3 -- the two-way rule this unit's controls discharge."),
    ("A-I7", "v13/code/ha_successor_receipt.json", "542b8735daf0",
     "I7's ARENA AS DATA: sites, links, the declared record family and the "
     "declared count box."),
    ("A-D42B1", "v10/code/d42b1_transport_exact.py", "576275d55ecf",
     "THE COMMITTED TRANSPORT GRAMMAR, driven directly: this unit's only "
     "source of admissibility."),
    ("A-D60", "v10/code/d60_crystal_exact.py", "684cdb76552b",
     "D60: the Builder `B` and the delivery helper `dl`, AST-extracted."),
    ("A-D66", "v10/code/d66_arbitration_crystal_exact.py", "3d0516ab106e",
     "D66: CONFLICT-GRID(g, R), the committed constructor, AST-extracted; "
     "its actor pool is what fixes the arity of the weld's site carrier."),
    ("A-L1", "v11/note-L1-lorentz-no-go-lemma.md", "93ea24591c3c",
     "L-1: the fourth-form clause argued before any test, and the sentence "
     "retracted on 2026-07-28 that no paper of this line may reproduce."),
    ("A-CAT", "v11/note-v11p0a-reproduction-catalog.md", "0cebe543e814",
     "the reproduction catalog 1.6/1.7: the BHS block and the "
     "Kleitman-Rothschild height-control warning."),
]
SOURCE_IDS = [s[0] for s in SOURCES]

# the retracted L-1 sentence: no paper of this line may reproduce it
BANNED_L1 = ("precisely the form U4 tests, and precisely the form the "
             "corpus's strongest relativity result took")

# THE DECLARED DRIVEN WINDOW.  Disclosed in the head; every other column is
# exhaustive over an object the window does not cap.
WINDOW_NAME = "W6"

# ===========================================================================
# SECTION 1.  MACHINERY -- the gate ledger, the seal, the text normaliser
# ===========================================================================


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


def mutate(name, normal, corrupted):
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
    ("SEAL-PATHVALUE", "path_value_anchors", "G-ANCHORS-READ"),
    ("SEAL-VERBATIM", "verbatim_anchors", "G-VERBATIM"),
    ("SEAL-I7", "i7", "G-I7-READOUT"),
    ("SEAL-SUBSTRATE", "substrate", "G-BUDGET-THEOREM"),
    ("SEAL-ARENA", "arena", "G-WITNESSES"),
    ("SEAL-DRIVEN", "driven", "G-DRIVEN-WINDOW"),
    ("SEAL-WELD-COARSE", "weld_coarse", "G-WELD-COARSE"),
    ("SEAL-SPLIT", "splittable", "G-SPLIT-FIBER"),
    ("SEAL-LAWS", "laws", "G-LAW-09"),
    ("SEAL-STEP", "refinement_step", "G-REFINED-BUILD"),
    ("SEAL-PLACES", "new_places", "G-NEW-PLACES"),
    ("SEAL-COMPAT", "compatibility", "G-COMPATIBILITY"),
    ("SEAL-STATUS", "refined_status", "G-REFINED-ADMISSIBLE"),
    ("SEAL-DICT", "dictionary", "G-TWO-WAY"),
    ("SEAL-SUPPLY", "process_supply", "G-CUT-UNIQUE"),
    ("SEAL-SIG", "sig", "G-SIG"),
    ("SEAL-CEILING", "ceiling", "G-CEILING"),
    ("SEAL-DIA", "dia", "G-DIA"),
    ("SEAL-WALLS", "walls", "G-WALL-LORENTZ-NAMED"),
    ("SEAL-VERDICT", "verdict", "G-VERDICT-RECONSTRUCTED"),
    ("SEAL-COUNTS", "counts", "G-VERDICT-RECONSTRUCTED"),
    ("SEAL-MEASURE", "measure_stamps", "G-MEASURE-STAMP"),
    ("SEAL-PAPER-CLAIMS", "paper_claims", "G-PAPER-CLAIMS"),
    ("SEAL-PAPER-TABLES", "paper_tables", "G-PAPER-TABLES"),
    ("SEAL-PAPER-COVERAGE", "paper_coverage", "G-PAPER-HEAD-VERBATIM"),
    ("SEAL-POLARITY", "polarity", "G-PAPER-CLAIM-POLARITY"),
    ("SEAL-FALSIFIER", "falsifier_census", "G-FALSIFIER-HONEST"),
    ("SEAL-COVERAGE", "coverage", "G-COVERAGE"),
    ("SEAL-WAIVERS", "waiver_ledger", "G-COVERAGE"),
    ("SEAL-MUTANTS", "mutants", "G-COVERAGE"),
    ("SEAL-MUTANT-SWEEP", "mutant_sweep", "G-SWEEP-BOUND"),
    ("SEAL-GATES", "gates", "G-PAPER-COVERAGE-FINAL"),
    ("SEAL-TOTALS", "totals", "G-PAPER-COVERAGE-FINAL"),
    ("SEAL-TRANSCRIPT", "transcript_head", "G-PAPER-COVERAGE-FINAL"),
]
DECLARED_UNSEALED = ("arithmetic", "python", "unit", "question",
                     "seal_manifest", "payload_sha256_12")
MEASURED_KEYS = ("substrate", "arena", "driven", "weld_coarse", "splittable",
                 "laws", "refinement_step", "new_places", "compatibility",
                 "refined_status", "dictionary", "process_supply", "sig",
                 "ceiling", "dia", "counts", "verdict")


class Seal:
    """the TOTAL gate-time seal (#119 + the #148 totality addendum)."""

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
    READS.append(rel)
    READS_BY_CATEGORY.setdefault("SOURCE", set()).add(
        os.path.abspath(os.path.join(REPO, rel)))
    with open(os.path.join(REPO, rel), "rb") as fh:
        return fh.read()


def read_text(path, category):
    """EVERY text read is categorised at the call; G-READS-DECLARED holds each
    category against its own declared set."""
    if category not in READ_CATEGORIES:
        raise GateFail("G-READS-DECLARED :: undeclared read category %r"
                       % category)
    READS_BY_CATEGORY.setdefault(category, set()).add(os.path.abspath(path))
    with open(path, "r", encoding="utf-8") as fh:
        return fh.read()


_FOLD = {"—": "--", "–": "-", "’": "'", "“": '"',
         "”": '"', "≤": "<=", "≥": ">=", "≠": "!=",
         "≡": "=", "×": "x", "₁": "1", "₂": "2",
         "₀": "0", "₃": "3", "ℓ": "l", "→": "->",
         "⋅": "*", "²": "2", "≈": "~", "⊆": "subset",
         "∈": "in", "∑": "sum", "·": "*", "−": "-",
         "⁄": "/", " ": " ", "⁴": "4", "∏": "prod",
         "↔": "<->", "⊕": "(+)", "⌊": "floor(",
         "⌋": ")", "⌈": "ceil(", "⌉": ")", "√": "sqrt",
         "…": "...", "─": "-", "∷": "::"}

_MD_PREFIX = re.compile(r"^(?:\s*(?:>+|[-*+]|\d+[.)])\s+)+")


def mdstrip(s):
    """#125 WITH MARKDOWN-PREFIX NORMALIZATION."""
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
    return norm(ascii_fold(mdstrip(s).replace("*", "").replace("`", "")))


NEEDLE_FLOOR = 30


def match_needle(hay, needle):
    """#125 with the mid-word residual closed."""
    n = canon(needle)
    if len(n) < NEEDLE_FLOOR:
        raise GateFail("G-VERBATIM :: needle below the #62 length floor: %r"
                       % needle)
    h = canon(hay)
    return n in h or n.replace(" ", "") in h.replace(" ", "")


# ===========================================================================
# SECTION 2.  EXACT ARITHMETIC ON Z_3^2 AND Z_6^2
# ===========================================================================

SITES = tuple((i, j) for i in range(3) for j in range(3))
SITE_INDEX = {s: k for k, s in enumerate(SITES)}
DIRECTIONS = ((1, 0), (0, 1), (1, 1), (1, 2))
I7_LINKS = ((1, 0), (0, 1), (1, 1))
ROUNDS = 6
BLOCK = 3
LREF = 6
SITES6 = tuple((i, j) for i in range(LREF) for j in range(LREF))
CELLS = tuple((x, l) for x in SITES for l in I7_LINKS)


def zadd(a, b):
    return ((a[0] + b[0]) % 3, (a[1] + b[1]) % 3)


def zmul(k, a):
    return ((k * a[0]) % 3, (k * a[1]) % 3)


def radd(z, l):
    return ((z[0] + l[0]) % LREF, (z[1] + l[1]) % LREF)


def img(x):
    return (2 * x[0], 2 * x[1])


NUMWORDS = ("ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN",
            "EIGHT", "NINE", "TEN", "ELEVEN", "TWELVE")
WORDNUM = dict({w.lower(): i for i, w in enumerate(NUMWORDS)},
               twice=2, thrice=3, hundred=100)


def exdiv(a, b):
    """THE ONE EXACT QUOTIENT IN THIS FILE.  A ratio of Fractions is formed
    from numerators and denominators, so no true-division operator occurs
    anywhere and G-EXACT-ARITHMETIC can scan for one as a syntax property."""
    a, b = Fraction(a), Fraction(b)
    return Fraction(a.numerator * b.denominator, a.denominator * b.numerator)


def q_of(nvec):
    """I7's own readout: q11 = n_e1, q22 = n_e2, q12 = (n_diag - n_e1 - n_e2)/2."""
    n1, n2, n3 = nvec
    q12 = Fraction(n3 - n1 - n2, 2)
    return (Fraction(n1), Fraction(n2), q12,
            Fraction(n1) * Fraction(n2) - q12 * q12)


def admissible(nvec):
    """HA 3.2's own criterion, by the exact Sylvester criterion."""
    q11, _q22, _q12, det = q_of(nvec)
    return q11 > 0 and det > 0


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


def round_vec(P):
    """cell (x, l) carries 1 exactly when x and x + l share a conflict group."""
    return tuple(1 if any(x in g and zadd(x, l) in g for g in P) else 0
                 for (x, l) in CELLS)


def declared_triple(g):
    """all three pairwise displacements lie on I7's declared link directions."""
    for x, y in combinations(sorted(g), 2):
        d = ((y[0] - x[0]) % 3, (y[1] - x[1]) % 3)
        dm = ((-d[0]) % 3, (-d[1]) % 3)
        if d not in I7_LINKS and dm not in I7_LINKS:
            return False
    return True


def ag_lines():
    """the twelve lines of AG(2,3), built from the four direction subgroups."""
    out = set()
    for a in SITES:
        for d in DIRECTIONS:
            out.add(frozenset({a, zadd(a, d), zadd(a, zmul(2, d))}))
    return out


LINES_AG = ag_lines()
DECLARED_TRIPLES = tuple(sorted(
    (frozenset(t) for t in combinations(SITES, 3) if declared_triple(set(t))),
    key=lambda s: sorted(s)))
TRIANGLES = tuple(t for t in DECLARED_TRIPLES if t not in LINES_AG)
DECL_LINES = tuple(t for t in DECLARED_TRIPLES if t in LINES_AG)


def cell_pair(x, l):
    return frozenset({x, zadd(x, l)})


CELL_PAIR = {(x, l): cell_pair(x, l) for (x, l) in CELLS}
PAIR_CELL = {v: k for k, v in CELL_PAIR.items()}

RAW = {}


def substrate():
    """the whole combinatorial substrate, computed once and mutant-free."""
    if RAW:
        return RAW
    parts = all_partitions()
    vecs = [round_vec(P) for P in parts]
    RAW["parts"] = parts
    RAW["vecs"] = vecs
    RAW["incidences"] = [sum(v) for v in vecs]
    RAW["sat"] = [i for i, v in enumerate(vecs) if sum(v) == 9]
    # the I7-STRICT triples: ordered triples of saturating groupings whose
    # summed incidence field is identically one.
    triples = []
    for i in RAW["sat"]:
        for j in RAW["sat"]:
            for k in RAW["sat"]:
                if all(vecs[i][t] + vecs[j][t] + vecs[k][t] == 1
                       for t in range(27)):
                    triples.append((i, j, k))
    RAW["triples"] = triples
    RAW["groups"] = [[frozenset(g) for idx in t for g in parts[idx]]
                     for t in triples]
    return RAW


# ===========================================================================
# SECTION 3.  THE COMMITTED GRAMMAR, DRIVEN DIRECTLY AT R = 6
# ===========================================================================

def no_exit(nodes):
    for node in nodes:
        for sub in ast.walk(node):
            if isinstance(sub, ast.Call):
                fn = sub.func
                nm = getattr(fn, "attr", None) or getattr(fn, "id", None)
                if nm in ("exit", "_exit"):
                    return False
    return True


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
        self.memo = {}
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
        (history, initiators); the memo is a cache over that pair alone."""
        key = (tuple(hist), tuple(inits))
        got = self.memo.get(key)
        if got is None:
            got = self.raw_candidates_for(list(hist), tuple(inits))
            self.memo[key] = got
        return got

    def _extract(self, rel, texts, marker, extra):
        """d60/d66's committed extraction idiom: keep only defs and classes."""
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


def drive(G, schedule):
    """THE R = 6 SCHEDULE DRIVER: exactly d66's CONFLICT-GRID(3, R) cycle --
    conflict-supply deliveries from the group's seed, three proposals, one
    three-proposer arbitration won by the seed -- with the GROUPING AND THE
    SEED taken from the schedule.  Groups are processed in ascending order of
    their seed's site index and members in ascending site index, which is
    d66's own order at the committed schedule.  Every event is specified by
    its FULL TUPLE and taken from the layer's own menu."""
    b = G.B(ACTORS)
    cur = {a: G.V0 for a in ACTORS}
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


BUILD_CACHE = {}


def driven(G, schedule):
    """cached and mutant-independent: the record is a property of the
    schedule, so the mutant sweep never re-drives the committed grammar."""
    if schedule not in BUILD_CACHE:
        b = drive(G, schedule)
        divs = [e for e in b.H if e[0] == "r"]
        BUILD_CACHE[schedule] = {
            "events": len(b.H), "maxhits": b.maxhits,
            "refusal": b.refusal, "divisions": len(divs),
            "footprints": [frozenset(r for r in G.regs_of(e)
                                     if r in ACTOR_SITE) for e in divs]}
    return BUILD_CACHE[schedule]


def link_field_of(footprints):
    """the DRIVEN link field: for a link l and a site x, the number of division
    events whose register footprint contains both x and x + l."""
    out = {}
    for x in SITES:
        for l in I7_LINKS:
            y = zadd(x, l)
            out[(x, l)] = sum(1 for f in footprints
                              if actor(x) in f and actor(y) in f)
    return out


def schedule_of(triple_idx, seed_k=0):
    """the declared seed menu: the k-th member of each conflict group in the
    canonical order.  Deterministic, no sampling."""
    parts = substrate()["parts"]
    out = []
    for idx in triple_idx:
        P = parts[idx]
        out.append((tuple(P), tuple(g[seed_k] for g in P)))
    return tuple(out)


# ===========================================================================
# SECTION 4.  THE WELD DETECTOR (paper-19's, at both declared readings)
# ===========================================================================

def connected_order(S, src):
    """THE SEARCH ORDER, and nothing else.  Each object after the first is
    chosen adjacent to an already-placed one wherever the relation allows, so
    the backtracking prunes at every level; ties break on the object's own
    name.  The SET of maps the search returns is order-independent -- which is
    measured, at G-WELD-COARSE's own arena, against the plain name order."""
    adj = {}
    for (u, v) in src:
        adj.setdefault(u, set()).add(v)
    rest = sorted(S, key=str)
    deg = {u: len(adj.get(u, ())) for u in rest}
    out = [max(rest, key=lambda u: (deg[u], str(u)))]
    seen = set(out)
    while len(out) < len(rest):
        cand = [u for u in rest if u not in seen
                and any(w in adj.get(u, ()) for w in seen)]
        if not cand:
            cand = [u for u in rest if u not in seen]
        nxt = max(cand, key=lambda u: (sum(1 for w in adj.get(u, ())
                                           if w in seen), deg[u], str(u)))
        out.append(nxt)
        seen.add(nxt)
    return out


def graph_isomorphisms(S, rel_set, X, links, Lmod, directed=False,
                       plain_order=False):
    """ALL bijections S -> X carrying the site-object incidence onto the
    target's Cayley incidence, by exhaustive backtracking.  No sampling and no
    cap.  THE DECLARED CRITERION IS THE UNDIRECTED ONE, on both branches."""
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
    Ss = sorted(S, key=str) if plain_order else connected_order(S, src)
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
    """THE QUOTIENT READING: a surjection of the realised objects onto the
    sites -- here necessarily a bijection -- under which EVERY realised edge
    carries a declared link displacement."""
    tgt = set()
    for x in X:
        for lk in links:
            y = tuple((x[i] + lk[i]) % Lmod for i in range(len(lk)))
            tgt.add((x, y))
            tgt.add((y, x))
    src = {(u, v) for (u, v) in rel_set if u != v}
    Ss = connected_order(S, src)
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


DETECT_CACHE = {}


def detect(name, objs, rel, X, links, Lmod, reading):
    """ONE CENSUS ROW.  Every fate is a MEASURED outcome with its number.  The
    fibers are `the number of distinct count fields each choice produces`."""
    ckey = (name, reading, Lmod,
            tuple(sorted((str(k), v) for k, v in rel.items())))
    if ckey in DETECT_CACHE:
        return json.loads(json.dumps(DETECT_CACHE[ckey]))
    row = {"arena": name, "reading": reading, "target_sites": len(X),
           "site_gen": "ACTOR", "link_gen": "CO-DIVISION-ACTOR-PAIR",
           "count_gen": "DIVISION-COUNT-IN-THE-DECLARED-WINDOW"}
    objs = sorted(objs, key=str)
    row["site_arity"] = len(objs)
    if len(objs) != len(X):
        row["fate"] = "ARITY-DEAD"
        row["reason"] = ("%d site objects against the target's %d; no repair "
                         "declared, and a declared restriction can only "
                         "shrink a site set" % (len(objs), len(X)))
        DETECT_CACHE[ckey] = json.loads(json.dumps(row, default=str))
        return json.loads(json.dumps(DETECT_CACHE[ckey]))
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
        row["reason"] = ("0 of the %d! bijections carry the site incidence %s "
                         "the target's link structure"
                         % (len(objs),
                            "onto" if reading == "EMBEDDING" else "into"))
        DETECT_CACHE[ckey] = json.loads(json.dumps(row, default=str))
        return json.loads(json.dumps(DETECT_CACHE[ckey]))
    nlab = len(links)
    base = count_field(rel, X, links, Lmod, maps[0], tuple(range(nlab)), False)
    row["count_cells"] = len(base)
    row["count_min"] = min(base.values())
    row["count_max"] = max(base.values())
    if row["count_min"] < 1:
        row["fate"] = "COUNT-DEAD"
        row["zero_cells"] = sum(1 for v in base.values() if v == 0)
        row["reason"] = ("n_l(x) must lie in Z_>0 (HA 3.1); the induced count "
                         "is 0 at %d of %d cells"
                         % (row["zero_cells"], len(base)))
        DETECT_CACHE[ckey] = json.loads(json.dumps(row, default=str))
        return json.loads(json.dumps(DETECT_CACHE[ckey]))
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
    lab_i = [len({fkey(fields[(i, lp, False)])
                  for lp in permutations(range(nlab))})
             for i in range(len(maps))]
    ori_i = [len({fkey(fields[(i, tuple(range(nlab)), o)])
                  for o in (False, True)}) for i in range(len(maps))]
    row["label_fiber_spread"] = sorted(set(lab_i))
    row["orient_fiber_spread"] = sorted(set(ori_i))
    row["fibers_base_map_invariant"] = (set(lab_i) == {fib_label}
                                        and set(ori_i) == {fib_orient})
    row["free_items_at_every_base_map"] = min(
        (1 if fib_site > 1 else 0) + (1 if lab_i[i] > 1 else 0)
        + (1 if ori_i[i] > 1 else 0) for i in range(len(maps)))
    row["base_maps_read"] = len(maps)
    inv = {"I-SITE-ASSIGNMENT": fib_site, "I-DIRECTION-LABEL": fib_label,
           "I-ORIENT": fib_orient}
    row["inventory"] = inv
    free = sorted(k for k, v in inv.items() if v > 1)
    row["free_items"] = free
    row["fate"] = "FOUND-candidate" if not free else "UNMOTIVATED"
    row["reason"] = ("zero free items at the RSQ standard" if not free else
                     "%d genuinely free item(s): %s"
                     % (len(free), ", ".join("%s fiber %d" % (k, inv[k])
                                             for k in free)))
    row["induced_record_at_the_base_map"] = sorted(
        {tuple(base[(x, lk)] for lk in links) for x in X})
    DETECT_CACHE[ckey] = json.loads(json.dumps(row, default=str))
    return json.loads(json.dumps(DETECT_CACHE[ckey]))


# ===========================================================================
# SECTION 5.  THE REFINED ARENA (paper-04's DYADIC move, rebuilt)
# ===========================================================================
#
# iota(x) = 2x.  Every coarse interval [x, x+l] is realised by the UNIQUE
# two-step refined path 2x -> 2x+l -> 2x+2l, so its interior site is forced
# and additivity is posable:   n_l^r(2x) + n_l^r(2x+l) = n_l^c(x).

COVERED = {}
for _x in SITES:
    for _l in I7_LINKS:
        COVERED[(img(_x), _l)] = (_x, _l, 0)
        COVERED[(radd(img(_x), _l), _l)] = (_x, _l, 1)
FREE_SLOTS = tuple(sorted((z, l) for z in SITES6 for l in I7_LINKS
                          if (z, l) not in COVERED))
MID_CELL = {radd(img(x), l): (x, l) for x in SITES for l in I7_LINKS}
MID_PAIR = {z: CELL_PAIR[c] for z, c in MID_CELL.items()}
SLOT_TRIANGLE = {}
for (_z, _l) in FREE_SLOTS:
    SLOT_TRIANGLE[(_z, _l)] = frozenset(set(MID_PAIR[_z])
                                        | set(MID_PAIR[radd(_z, _l)]))


def site_class(z):
    par = (z[0] % 2, z[1] % 2)
    if par == (0, 0):
        return "IMAGE"
    for l in I7_LINKS:
        if tuple(l) == par:
            return "MID%s" % (l,)
    return "UNREACHED"


def refined_counts(split, free):
    """the refined record: the split halves on the 54 covered slots, the
    declared completion on the 54 free ones."""
    c = {z: {} for z in SITES6}
    for (x, l), (n1, n2) in split.items():
        c[img(x)][l] = n1
        c[radd(img(x), l)][l] = mutate(
            "MUT-ADDITIVITY", n2,
            n2 + 1 if (x == (0, 0) and l == I7_LINKS[0]) else n2)
    for (z, l), v in free.items():
        c[z][l] = v
    return c


def completion_minimal(split):
    """PAPER-04's OWN declared minimal completion, reimplemented from its
    committed rule: put the refined site on the diagonal locus, c = a + b, so
    q_12 = 0 and det q = ab > 0, with the free counts at K = 1."""
    known = {z: {} for z in SITES6}
    for (x, l), (n1, n2) in split.items():
        known[img(x)][l] = n1
        known[radd(img(x), l)][l] = n2
    K = 1
    out = {}
    e1, e2, e3 = I7_LINKS
    for z in SITES6:
        have = known[z]
        if len(have) == 3:
            continue
        if e1 in have and e2 not in have:
            out[(z, e2)] = K
            out[(z, e3)] = have[e1] + K
        elif e2 in have and e1 not in have:
            out[(z, e1)] = K
            out[(z, e3)] = K + have[e2]
        elif e3 in have:
            out[(z, e1)] = have[e3] + K
            out[(z, e2)] = have[e3] + K
    return out


def completion_from_process(groups):
    """THE PROCESS-SUPPLIED completion: the count on a refined MID-MID link is
    the number of division events whose footprint is exactly the three-actor
    conflict group that the two co-division pairs span."""
    mult = Counter(groups)
    return {(z, l): mult.get(SLOT_TRIANGLE[(z, l)], 0) for (z, l) in FREE_SLOTS}


def refined_rel(counts):
    """the refined record as a SYMMETRIC incidence with counts, exactly as the
    co-division relation is symmetric."""
    rel = {}
    for z in SITES6:
        for l in I7_LINKS:
            w = radd(z, l)
            rel[(z, w)] = counts[z][l]
            rel[(w, z)] = counts[z][l]
    return rel


def codivision_rel(field):
    """the co-division incidence on the ordered actor pair."""
    rel = {}
    for u in ACTORS:
        for v in ACTORS:
            if u != v:
                rel[(u, v)] = 0
    for (x, l), n in field.items():
        rel[(actor(x), actor(zadd(x, l)))] = n
        rel[(actor(zadd(x, l)), actor(x))] = n
    return rel


# ===========================================================================
# SECTION 6.  THE #62 VERBATIM ANCHORS, BOUND TO THEIR CONSUMER GATES
# ===========================================================================

VERBATIM = [
    ("V01", "A-PIN",
     "DOES THE PLACE-COUNT GROW -- the NEW-PLACES segment, first-class and "
     "description-stamped", "G-NEW-PLACES"),
    ("V02", "A-PIN",
     "the new places are refined INTERVALS; no actor-creation claim beyond "
     "the measured structure", "G-WALL-COSMO"),
    ("V03", "A-PIN", "does the DICTIONARY extend to it", "G-WELD-REFINED"),
    ("V04", "A-P21", "it is reachable by concatenation.", "G-72-TRIPLES"),
    ("V05", "A-P21",
     "the weld there is MOTIVATED.** Run through this unit's own detector the\n  concatenation's co-division arena returns 1296 isomorphisms and fibers",
     "G-WELD-COARSE"),
    ("V06", "A-P21",
     "paper-04's move is live.** Every interval of (2, 2, 2) carries count 2, "
     "so the DYADIC raw fiber is", "G-LAW-04"),
    ("V07", "A-P21",
     "only paper-09 stays empty**: every count is 2, so all **27** intervals "
     "sit inside the same measured support hole", "G-LAW-09"),
    ("V08", "A-P21", "the price is that (2, 2, 2) is undeclared.",
     "G-REFINED-ADMISSIBLE"),
    ("V09", "A-P21", "Nothing at six or eight rounds is driven here.",
     "G-DRIVEN-WINDOW"),
    ("V10", "A-P21",
     "the fibers computed as the number of distinct count fields each choice "
     "produces", "G-WELD-COARSE"),
    ("V11", "A-P21",
     "zero free items holds exactly at the link-constant records, and I7 "
     "declares none of them.", "G-WELD-REFINED"),
    ("V12", "A-P04",
     "An interval that carries only its total $n$ admits exactly $n-1$ places "
     "for one interior boundary.", "G-SPLIT-FIBER"),
    ("V13", "A-P04",
     "No record admits more than $\\lfloor\\log_2(\\min n_\\ell)\\rfloor$ "
     "consecutive steps.", "G-CEILING"),
    ("V14", "A-P04",
     "Half the refined arena is invisible to the coarse record: 54 of the 108 "
     "refined links lie on no coarse interval.", "G-NEW-PLACES"),
    ("V15", "A-P04",
     "at d = 3 the dyadic move leaves 27 of 216 refined sites on no coarse "
     "interval at all", "G-DIA"),
    ("V16", "A-P04",
     "A count-1 interval cannot be split into two strictly positive parts",
     "G-SPLIT-FIBER"),
    ("V17", "A-P04",
     "the record carries interval totals and not event positions",
     "G-CUT-UNIQUE"),
    ("V18", "A-P06",
     "a single interval carrying n events has n - 1 splits: under the pinned "
     "group the simplex has dimension n - 2 and is a point only at n = 2",
     "G-LAW-06"),
    ("V19", "A-P06",
     "What a motivated split distribution would require is a joint law for "
     "WHERE inside a record interval its $n_\\ell(x)$ division events fall",
     "G-CUT-UNIQUE"),
    ("V20", "A-P06", "Uniqueness by triviality, not by selection.",
     "G-COMPATIBILITY"),
    ("V21", "A-P09",
     "There is no inter-renewal leg of length one or two, exactly.",
     "G-LAW-09"),
    ("V22", "A-HA",
     "A predicate that cannot return its other value anywhere in the declared "
     "arena is not a measurement", "G-TWO-WAY"),
    ("V23", "A-HA",
     "A record is admissible when $q$ is nonsingular and positive definite at "
     "every site, by the exact Sylvester criterion", "G-I7-READOUT"),
    ("V24", "A-L1",
     "fourth form, outside paper 8's three**, and its admissibility is v11's "
     "to argue when U4 runs", "G-WALL-L1"),
    ("V25", "A-CAT",
     "a Poisson sprinkling admits no Lorentz-invariant finite-valency graph",
     "G-WALL-BHS"),
    ("V26", "A-CAT",
     "a dimension reading without a height control is worthless",
     "G-WALL-KR"),
]

# (path, value) anchors: a path drift that changes the arena or the verdict
# must die by anchor and not only by a byte change.
PATH_ANCHORS = [
    ("A-P21REC", "split/r6_door/r3_i7_strict_triples", 72, "G-72-TRIPLES"),
    ("A-P21REC", "split/r6_door/triples_at_field_1", 72, "G-72-TRIPLES"),
    ("A-P21REC", "split/r6_door/ordered_witnesses", 5184, "G-WITNESSES"),
    ("A-P21REC", "split/r6_door/isomorphisms", 1296, "G-WELD-COARSE"),
    ("A-P21REC", "split/r6_door/fibers/I-SITE-ASSIGNMENT", 1,
     "G-WELD-COARSE"),
    ("A-P21REC", "split/r6_door/fibers/I-DIRECTION-LABEL", 1,
     "G-WELD-COARSE"),
    ("A-P21REC", "split/r6_door/fibers/I-ORIENT", 1, "G-WELD-COARSE"),
    ("A-P21REC", "split/r6_door/dyadic_raw_fiber", 1, "G-LAW-04"),
    ("A-P21REC", "split/r6_door/rounds", 6, "G-R6-FIELD"),
    ("A-P21REC", "split/r6_door/record", [2, 2, 2], "G-R6-FIELD"),
    ("A-P21REC", "split/r6_door/intervals_in_the_kernel_hole", 27,
     "G-LAW-09"),
    ("A-P21REC", "split/r6_door/crb_pinned_transitive", [[2, 2, 2]],
     "G-LAW-06"),
    ("A-P21REC", "counts/partitions", 280, "G-PARTITION-COUNT"),
    ("A-P19REC", "counts/i7_strict_triples", 72, "G-72-TRIPLES"),
    ("A-P19REC", "counts/isomorphisms", 1296, "G-WELD-COARSE"),
    ("A-P19REC", "counts/det_uniform", "3/4", "G-SIG"),
    ("A-P09REC", "kernel/support_holes", [1, 2], "G-LAW-09"),
    ("A-P04REC", "count_lattice/unique_admissible_split", [[2, 2, 2]],
     "G-LAW-04"),
    ("A-P04REC", "count_lattice/splittable", 261, "G-LAW-04"),
    ("A-P04REC", "count_lattice/admissible_count_vectors", 361, "G-LAW-04"),
    ("A-P04REC", "move_census/rows/0/refined_sites", 36, "G-NEW-PLACES"),
    ("A-P04REC", "move_census/rows/0/tally/SUBDIVIDED", 27, "G-NEW-PLACES"),
    ("A-P04REC", "move_census/rows/0/verdict", "ADMISSIBLE", "G-LAW-04"),
    ("A-P06REC", "per_interval_law/rows/1/n", 2, "G-LAW-06"),
    ("A-P06REC", "per_interval_law/rows/1/fiber", 1, "G-LAW-06"),
    ("A-P06REC", "per_interval_law/rows/1/pinned_orbits", 1, "G-LAW-06"),
    ("A-P06REC", "per_interval_law/rows/1/pinned_simplex_dim", 0, "G-LAW-06"),
    ("A-P06REC", "per_interval_law/rows/1/pinned_transitive", True,
     "G-LAW-06"),
    ("A-P06REC", "per_interval_law/rows/0/fiber", 0, "G-SPLIT-FIBER"),
    ("A-I7", "declarations/links_d2", [[1, 0], [0, 1], [1, 1]],
     "G-I7-READOUT"),
    ("A-I7", "tables/link_locality_lattice/admissible_points", 361,
     "G-I7-READOUT"),
]

GATE_REGISTRY = (
    "G-PROVENANCE", "G-READS-DECLARED", "G-EXACT-ARITHMETIC",
    "G-NO-SUBPROCESS", "G-SLICE-EXIT-FREE", "G-ANCHORS-READ", "G-VERBATIM",
    "G-ANCHOR-CONSUMERS", "G-I7-READOUT",
    "G-PARTITION-COUNT", "G-BUDGET-THEOREM", "G-72-TRIPLES", "G-R6-FIELD",
    "G-WITNESSES", "G-WELD-COARSE", "G-DRIVEN-WINDOW", "G-DRIVEN-MAXHITS",
    "G-SPLIT-FIBER",
    "G-LAW-06", "G-LAW-04", "G-LAW-09", "G-REFINED-BUILD", "G-NEW-PLACES",
    "G-COMPATIBILITY", "G-REFINED-ADMISSIBLE", "G-DICTIONARY-CARRIER",
    "G-PROCESS-SUPPLY", "G-CUT-UNIQUE", "G-WELD-REFINED", "G-TWO-WAY",
    "G-SIG", "G-CEILING", "G-DIA",
    "G-WALL-L1", "G-WALL-BHS", "G-WALL-KR", "G-WALL-COSMO",
    "G-WALL-LORENTZ-NAMED",
    "G-MEASURE-STAMP", "G-FALSIFIER-HONEST", "G-VERDICT-RECONSTRUCTED",
    "G-PAPER-CLAIMS", "G-PAPER-TABLES", "G-PAPER-COVERAGE",
    "G-PAPER-HEAD-VERBATIM", "G-PAPER-CLAIM-POLARITY",
    "G-COVERAGE", "G-REACHABILITY", "G-MUTANTS-ON-TARGET", "G-SWEEP-BOUND",
    "G-SEAL-COMPLETE", "G-PAPER-COVERAGE-FINAL", "G-ARTIFACT-INTEGRITY",
)

NUMREG = set()


def reg(*vals):
    """every published count is REGISTERED as it is computed, never typed into
    the paper's allow list by hand."""
    for v in vals:
        if isinstance(v, bool):
            continue
        if isinstance(v, int):
            NUMREG.add(str(v))
            NUMREG.add("{:,}".format(v))
        elif isinstance(v, Fraction):
            NUMREG.add(str(v.numerator))
            NUMREG.add(str(v.denominator))
        elif isinstance(v, (list, tuple)):
            reg(*v)
    return vals[0] if len(vals) == 1 else vals


# ===========================================================================
# SECTION 7.  THE FULL RUN
# ===========================================================================

def full_run(break_anchor=None, paper_text=None, paper_rel=PAPER_REL,
             do_paper=True):
    # THE READ REGISTRY IS PER-RUN.  A module-level registry that accumulated
    # across in-process sub-runs would make the second run's G-READS-DECLARED
    # a statement about the first run's reads.
    READS_BY_CATEGORY.clear()
    del READS[:]
    LD, SEAL, R = Ledger(), Seal(), {}
    R["schema"] = SCHEMA
    R["unit"] = "v14 LOR-A -- the law over records at R = 6"
    R["question"] = ("On the first motivated law-over-records arena -- the "
                     "R = 6 welded record (2, 2, 2) -- do the refinement laws "
                     "ACT, and what does one lawful act produce?")
    R["python"] = "%d.%d" % sys.version_info[:2]
    R["arithmetic"] = ("exact: int and fractions.Fraction only, AST-scanned; "
                       "no float literal, no float-adjacent import, no true "
                       "division outside the one exact helper")

    # ---------------------------------------------------------------- SEC 1
    say("\n[SEC 1] PROVENANCE -- 19 pinned sources, hash-verified")
    texts, prov = {}, []
    for sid, rel, want, why in SOURCES:
        raw = read_bytes(rel)
        got = hashlib.sha256(raw).hexdigest()[:12]
        want_eff = "deadbeefdead" if break_anchor == sid else want
        prov.append({"id": sid, "path": rel, "declared": want_eff,
                     "measured": got, "match": got == want_eff, "role": why})
        texts[rel] = raw.decode("utf-8")
    R["provenance"] = prov
    bad = [p["id"] for p in prov if not p["match"]]
    LD.gate("G-PROVENANCE",
            "EVERY RUNTIME INPUT IS A HASH-PINNED SOURCE.  Each of the %d "
            "declared sources is read by path and its sha256-12 compared "
            "against this unit's frozen declaration, per object; a drifted "
            "byte in any one of them dies here before a single number is "
            "computed" % len(SOURCES),
            not bad, "sources %d, mismatched %s" % (len(SOURCES),
                                                    bad or "none"))
    SEAL.take("SEAL-SCHEMA", R)
    SEAL.take("SEAL-PROVENANCE", R)

    src_paths = {os.path.abspath(os.path.join(REPO, s[1])) for s in SOURCES}
    reads_ok = (READS_BY_CATEGORY.get("SOURCE", set()) == src_paths
                and set(READS_BY_CATEGORY) <= set(READ_CATEGORIES))
    LD.gate("G-READS-DECLARED",
            "NO UNANCHORED RUNTIME INPUT.  Every read in this file is "
            "categorised at the call site; the SOURCE category must equal the "
            "declared source set exactly and no undeclared category may "
            "appear, so a read of mutable repository state cannot be added "
            "without failing here",
            reads_ok,
            "categories %s, source reads %d of %d declared"
            % (sorted(READS_BY_CATEGORY),
               len(READS_BY_CATEGORY.get("SOURCE", set())), len(SOURCES)))

    tree = ast.parse(read_text(SELF, "SELF"))
    floats = [n for n in ast.walk(tree)
              if isinstance(n, ast.Constant) and isinstance(n.value, float)]
    divs = [n for n in ast.walk(tree) if isinstance(n, ast.BinOp)
            and isinstance(n.op, ast.Div)]
    badimp = [n for n in ast.walk(tree)
              if isinstance(n, (ast.Import, ast.ImportFrom))
              and any(a.name.split(".")[0] in ("math", "numpy", "statistics",
                                               "decimal", "random", "cmath")
                      for a in getattr(n, "names", []))]
    LD.gate("G-EXACT-ARITHMETIC",
            "THE ARITHMETIC IS EXACT BY CONSTRUCTION, PROVED ON THIS FILE'S "
            "OWN SYNTAX TREE.  No float literal, no float-adjacent import and "
            "no true-division operator occurs anywhere in this file; every "
            "quotient is a Fraction",
            not floats and not divs and not badimp,
            "float literals %d, true divisions %d, float-adjacent imports %d"
            % (len(floats), len(divs), len(badimp)))
    subp = [n for n in ast.walk(tree)
            if isinstance(n, (ast.Import, ast.ImportFrom))
            and any(a.name.split(".")[0] in ("subprocess", "shutil", "socket",
                                             "urllib", "http")
                    for a in getattr(n, "names", []))]
    LD.gate("G-NO-SUBPROCESS",
            "THE RUN IS OFF-TREE AND GIT-LESS (#91).  No subprocess, network "
            "or shell import occurs in this file, so the delivery run reads "
            "nothing but its declared sources and can be byte-reproduced with "
            "no version control present",
            not subp, "forbidden imports %d" % len(subp))

    # ---- the path-value anchors and the verbatim anchors
    jsons = {}
    for sid in ("A-P21REC", "A-P19REC", "A-P04REC", "A-P06REC", "A-P09REC",
                "A-I7"):
        rel = [s[1] for s in SOURCES if s[0] == sid][0]
        jsons[sid] = json.loads(texts[rel])
    pv = []
    for sid, path, want, gate in PATH_ANCHORS:
        try:
            got = jpath(jsons[sid], path)
        except (KeyError, IndexError, TypeError):
            got = None
        got = mutate("MUT-ANCHOR-VALUE", got,
                     None if path.endswith("ordered_witnesses") else got)
        pv.append({"source": sid, "path": path, "declared": want,
                   "measured": got, "match": got == want,
                   "consumer_gate": gate})
    R["path_value_anchors"] = pv
    pvbad = [a["path"] for a in pv if not a["match"]]
    pvgates = sorted({a["consumer_gate"] for a in pv})
    LD.gate("G-ANCHORS-READ",
            "THE PREDECESSORS ARE READ AT (PATH, VALUE), NOT ONLY AT BYTES.  "
            "%d rows are read out of five committed receipts by path and "
            "compared against this unit's frozen declaration, each row naming "
            "the gate it licenses; a path drift that changed the arena or the "
            "verdict while preserving a file hash dies here"
            % len(PATH_ANCHORS),
            not pvbad and all(g in GATE_REGISTRY for g in pvgates),
            "path-value anchors %d, mismatched %s, consumer gates %d"
            % (len(pv), pvbad or "none", len(pvgates)))
    SEAL.take("SEAL-PATHVALUE", R)

    vb = []
    for vid, sid, quote, gate in VERBATIM:
        rel = [s[1] for s in SOURCES if s[0] == sid][0]
        hay = texts[rel]
        if mut("MUT-VERBATIM") and vid == "V13":
            hay = hay.replace("No record admits more than", "Records admit")
        ok = match_needle(hay, quote)
        vb.append({"id": vid, "source": sid, "consumer_gate": gate,
                   "chars": len(canon(quote)), "found": ok})
    R["verbatim_anchors"] = vb
    vbad = [v["id"] for v in vb if not v["found"]]
    LD.gate("G-VERBATIM",
            "QUOTE FIDELITY (#62, corrected spec).  Every sentence this unit "
            "quotes or reimplements from a predecessor is matched WORD FOR "
            "WORD against that predecessor's committed bytes, after markdown-"
            "prefix stripping, ASCII folding and whitespace normalisation, "
            "with a %d-character floor; %d anchors, evaluated BEFORE the byte "
            "anchors are used for anything" % (NEEDLE_FLOOR, len(VERBATIM)),
            not vbad, "verbatim anchors %d, missing %s"
            % (len(vb), vbad or "none"))
    SEAL.take("SEAL-VERBATIM", R)

    cons = sorted({v["consumer_gate"] for v in vb}
                  | {a["consumer_gate"] for a in pv})
    if mut("MUT-CONSUMER-BINDING"):
        cons = cons + ["G-NOT-A-GATE"]
    unreg = [g for g in cons if g not in GATE_REGISTRY]
    LD.gate("G-ANCHOR-CONSUMERS",
            "EVERY ANCHOR BINDS MEANING TO USE.  Each verbatim and each "
            "path-value row names the gate it licenses, and every named gate "
            "must exist in this run's declared registry -- an anchor whose "
            "consumer is an unread label binds existence, not meaning",
            not unreg, "consumer gates named %d, unregistered %s"
            % (len(cons), unreg or "none"))

    # ---- I7's readout, recomputed
    i7 = {"links": [list(l) for l in I7_LINKS],
          "readout": "q11 = n_e1, q22 = n_e2, q12 = (n_diag - n_e1 - n_e2)/2",
          "criterion": "q nonsingular and positive definite at every site",
          "box_admissible_points": len([1 for n1 in range(1, 7)
                                        for n2 in range(1, 7)
                                        for n3 in range(1, 13)
                                        if admissible((n1, n2, n3))])}
    for nv in ((1, 1, 1), (2, 2, 2), (1, 1, 2), (2, 2, 1), (4, 4, 4)):
        q11, q22, q12, det = q_of(nv)
        i7["q%s" % (nv,)] = {"q11": str(q11), "q22": str(q22),
                             "q12": str(q12), "det": str(det),
                             "trace": str(q11 + q22),
                             "posdef": admissible(nv)}
    R["i7"] = i7
    reg(i7["box_admissible_points"])
    LD.gate("G-I7-READOUT",
            "I7'S READOUT AND ADMISSIBILITY CRITERION ARE THE PINNED ONES, "
            "RECOMPUTED.  The readout sentence is matched verbatim against "
            "HA's committed bytes, the declared link list is read out of I7's "
            "own receipt at (path, value), and the declared count box is "
            "re-enumerated here rather than cited",
            i7["box_admissible_points"] == 361
            and jpath(jsons["A-I7"], "declarations/links_d2")
            == [list(l) for l in I7_LINKS],
            "box admissible points recomputed %d, declared link list matches "
            "I7's own receipt %s"
            % (i7["box_admissible_points"],
               jpath(jsons["A-I7"], "declarations/links_d2")
               == [list(l) for l in I7_LINKS]))
    SEAL.take("SEAL-I7", R)

    # ---------------------------------------------------------------- SEC 2
    say("\n[SEC 2] STAGE 1 -- THE (2,2,2) ARENA, BUILT FROM NOTHING")
    C = substrate()
    parts, vecs = C["parts"], C["vecs"]
    n_parts_enum = mutate("MUT-PARTITION", len(parts), len(parts) + 1)
    fact = 1
    for k in range(1, 10):
        fact = fact * k
    n_parts_closed = fact // (6 * 6 * 6 * 6)      # 9! / (3!^3 3!)
    reg(n_parts_enum, n_parts_closed)
    LD.gate("G-PARTITION-COUNT",
            "THE ROUND FAMILY IS COUNTED TWICE BY ROUTES THAT SHARE NO CODE.  "
            "Exhaustive enumeration of the partitions of nine sites into "
            "three triples, and the closed form 9!/(3!^3 3!) built from a "
            "factorial computed here; the two must agree and must equal the "
            "value paper-21's committed receipt carries at "
            "/counts/partitions",
            n_parts_enum == n_parts_closed == jpath(jsons["A-P21REC"],
                                                    "counts/partitions"),
            "enumeration %d, closed form %d, paper-21's committed row %d"
            % (n_parts_enum, n_parts_closed,
               jpath(jsons["A-P21REC"], "counts/partitions")))

    spectrum = Counter(C["incidences"])
    maxinc = mutate("MUT-BUDGET", max(C["incidences"]), 10)
    sat = C["sat"]
    substrate_row = {
        "partitions": len(parts),
        "incidence_spectrum": {str(k): v for k, v in sorted(spectrum.items())},
        "max_incidence_per_round": maxinc,
        "saturating_partitions": len(sat),
        "budget_at_R6": maxinc * ROUNDS,
        "cells": len(CELLS),
        "declared_triples": len(DECLARED_TRIPLES),
        "declared_lines": len(DECL_LINES),
        "non_collinear_triangles": len(TRIANGLES),
    }
    R["substrate"] = substrate_row
    reg(len(parts), maxinc, len(sat), maxinc * ROUNDS, len(CELLS),
        len(DECLARED_TRIPLES), len(DECL_LINES), len(TRIANGLES))
    LD.gate("G-BUDGET-THEOREM",
            "THE BUDGET THEOREM, MEASURED EXHAUSTIVELY.  No round of this "
            "cycle deposits more than 9 link incidences -- measured over all "
            "%d partitions, per partition -- so six rounds carry at most 54, "
            "and the link-constant record (2, 2, 2) needs exactly 6 x 9 = 54: "
            "equality forces every round to saturate, which makes the census "
            "over the %d saturating groupings exhaustive over the whole "
            "family" % (len(parts), len(sat)),
            maxinc == 9 and maxinc * ROUNDS == 54
            and len(sat) == sum(1 for v in C["incidences"] if v == maxinc)
            and all(sum(vecs[i]) == 9 for i in sat),
            "max incidence per round %d, six-round budget %d, saturating "
            "partitions %d, spectrum %s"
            % (maxinc, maxinc * ROUNDS, len(sat),
               dict(sorted(spectrum.items()))))
    SEAL.take("SEAL-SUBSTRATE", R)

    triples = C["triples"]
    n_tri = mutate("MUT-72", len(triples), len(triples) - 1)
    # route 2: a DIFFERENT criterion -- every one of the 27 unordered declared
    # actor pairs is covered exactly once by the triple's nine conflict groups
    route2 = 0
    for gs in C["groups"]:
        cov = Counter()
        for g in gs:
            for u, v in combinations(sorted(g), 2):
                cov[frozenset({u, v})] += 1
        if len(cov) == 27 and set(cov.values()) == {1}:
            route2 += 1
    reg(n_tri, route2)
    LD.gate("G-72-TRIPLES",
            "THE R = 3 I7-STRICT TRIPLES, COUNTED TWICE AND ANCHORED.  Route "
            "one sums the per-round incidence vectors and requires the field "
            "to be identically one at all 27 cells; route two never forms an "
            "incidence vector at all and instead requires the triple's nine "
            "conflict groups to cover each of the 27 unordered declared actor "
            "pairs exactly once.  Both must return the number paper-19 and "
            "paper-21 committed",
            n_tri == route2 == jpath(jsons["A-P21REC"],
                                     "split/r6_door/r3_i7_strict_triples")
            == jpath(jsons["A-P19REC"], "counts/i7_strict_triples"),
            "route 1 %d, route 2 (pair-cover) %d, paper-21 committed %d, "
            "paper-19 committed %d"
            % (n_tri, route2,
               jpath(jsons["A-P21REC"], "split/r6_door/r3_i7_strict_triples"),
               jpath(jsons["A-P19REC"], "counts/i7_strict_triples")))

    # ---- the concatenation: the (2,2,2) field
    field = {}
    a0, b0 = 0, 0
    for t in range(27):
        field[CELLS[t]] = (vecs[triples[a0][0]][t] + vecs[triples[a0][1]][t]
                           + vecs[triples[a0][2]][t]
                           + vecs[triples[b0][0]][t] + vecs[triples[b0][1]][t]
                           + vecs[triples[b0][2]][t])
    field[CELLS[0]] = mutate("MUT-FIELD", field[CELLS[0]], 3)
    cells_at_two = [c for c in CELLS if field[c] == 2]
    record = sorted({tuple(field[(x, l)] for l in I7_LINKS) for x in SITES})
    arena_row = {
        "rounds": ROUNDS, "blocks": 2, "block_length": BLOCK,
        "cells": len(CELLS), "cells_at_count_2": len(cells_at_two),
        "record": [list(r) for r in record],
        "homogeneous": len(record) == 1,
        "link_constant": len(record) == 1 and len(set(record[0])) == 1,
        "admissible_sites": sum(1 for x in SITES
                                if admissible(tuple(field[(x, l)]
                                                    for l in I7_LINKS))),
        "declared_by_i7": False,
        "in_the_declared_count_box": all(admissible(r) for r in record),
    }
    R["arena"] = arena_row
    reg(len(cells_at_two), arena_row["admissible_sites"])
    LD.gate("G-R6-FIELD",
            "THE ARENA IS (2, 2, 2) AT EVERY CELL, CHECKED PER CELL.  Two of "
            "the 72 I7-STRICT triples concatenate to a six-round schedule "
            "whose summed incidence field is 2 at each of the 27 (site, link) "
            "cells individually -- never as a total -- and the induced record "
            "is link-constant and positive definite at each of the nine sites "
            "individually, matching paper-21's committed G-R6-DOOR row",
            len(cells_at_two) == 27 and arena_row["link_constant"]
            and arena_row["admissible_sites"] == 9
            and [list(r) for r in record] == [jpath(jsons["A-P21REC"],
                                                    "split/r6_door/record")],
            "cells at count 2: %d of %d, record %s, admissible sites %d of 9, "
            "paper-21's committed record %s"
            % (len(cells_at_two), len(CELLS), record,
               arena_row["admissible_sites"],
               jpath(jsons["A-P21REC"], "split/r6_door/record")))

    # ---- the witnesses, exhaustive over all ordered pairs of the 72
    wit = 0
    for a in range(len(triples)):
        for b in range(len(triples)):
            ok = True
            for t in range(27):
                s = (vecs[triples[a][0]][t] + vecs[triples[a][1]][t]
                     + vecs[triples[a][2]][t] + vecs[triples[b][0]][t]
                     + vecs[triples[b][1]][t] + vecs[triples[b][2]][t])
                if s != 2:
                    ok = False
                    break
            if ok:
                wit += 1
    wit = mutate("MUT-WITNESSES", wit, wit - 1)
    reg(wit)
    arena_row["ordered_witnesses"] = wit
    LD.gate("G-WITNESSES",
            "EVERY ORDERED PAIR OF THE 72 IS A WITNESS, MEASURED RATHER THAN "
            "MULTIPLIED.  The concatenation census runs each of the %d "
            "ordered pairs through the per-cell test independently; the "
            "count must equal the value paper-21 committed at "
            "/split/r6_door/ordered_witnesses" % (len(triples) ** 2),
            wit == jpath(jsons["A-P21REC"],
                         "split/r6_door/ordered_witnesses"),
            "ordered witnesses %d of %d ordered pairs; paper-21's committed "
            "row %d" % (wit, len(triples) ** 2,
                        jpath(jsons["A-P21REC"],
                              "split/r6_door/ordered_witnesses")))
    SEAL.take("SEAL-ARENA", R)

    # ---- the weld at the coarse arena, on this unit's own detector
    crel = codivision_rel(field)
    wrows = [detect("R6-CONCAT(2,2,2)", ACTORS, crel, SITES, I7_LINKS, 3, rd)
             for rd in ("EMBEDDING", "QUOTIENT")]
    wc = {"rows": wrows,
          "isomorphisms": mutate("MUT-WELD", wrows[0].get("isomorphisms"),
                                 wrows[0].get("isomorphisms", 0) + 1),
          "quotient_maps": wrows[1].get("quotient_maps"),
          "fibers": wrows[0]["inventory"],
          "free_items": wrows[0]["free_items"],
          "fate": wrows[0]["fate"],
          "directed_comparator": wrows[0].get(
              "isomorphisms_directed_comparator")}
    R["weld_coarse"] = wc
    reg(wc["isomorphisms"], wc["quotient_maps"], wc["directed_comparator"],
        *sorted(wc["fibers"].values()))
    LD.gate("G-WELD-COARSE",
            "THE WELD IS RE-VERIFIED ZERO-FREE ON THIS UNIT'S OWN DETECTOR.  "
            "The co-division arena of the concatenated record is built here "
            "from the actor pairs and run through both declared readings; "
            "each inventory item's fiber is checked individually against 1, "
            "and the isomorphism count against paper-21's and paper-19's "
            "committed rows",
            all(v == 1 for v in wc["fibers"].values())
            and not wc["free_items"]
            and wc["isomorphisms"] == wc["quotient_maps"]
            == jpath(jsons["A-P21REC"], "split/r6_door/isomorphisms")
            == jpath(jsons["A-P19REC"], "counts/isomorphisms")
            and wrows[0]["fate"] == "FOUND-candidate"
            and wrows[1]["fate"] == "FOUND-candidate",
            "isomorphisms %s, quotient maps %s, fibers %s, free items %s, "
            "fate %s/%s, directed comparator %s"
            % (wc["isomorphisms"], wc["quotient_maps"], wc["fibers"],
               wc["free_items"] or "none", wrows[0]["fate"], wrows[1]["fate"],
               wc["directed_comparator"]))
    SEAL.take("SEAL-WELD-COARSE", R)

    # ---- the process-supply classification of ALL 5,184 witnesses
    groups_of = C["groups"]
    TRISET = set(TRIANGLES)
    LINESET = set(DECL_LINES)
    supply_rows = {}
    supplied = []
    for a in range(len(triples)):
        for b in range(len(triples)):
            gs = groups_of[a] + groups_of[b]
            mult = Counter(g for g in gs if g in TRISET)
            lines_present = {g for g in gs if g in LINESET}
            missing = 3 * (len(TRIANGLES) - len(mult))
            foreign = 3 * len(lines_present)
            key = (len(mult), len(lines_present))
            supply_rows.setdefault(key, []).append((a, b))
            if missing == 0 and foreign == 0:
                supplied.append((a, b))
    n_supplied = mutate("MUT-SUPPLY", len(supplied), len(supplied) + 1)
    reg(n_supplied, len(supplied))

    # ---------------------------------------------------------------- SEC 3
    say("\n[SEC 3] STAGE 1 -- THE DECLARED DRIVEN WINDOW %s" % WINDOW_NAME)
    G = Grammar(texts)
    LD.gate("G-SLICE-EXIT-FREE",
            "THE COMMITTED LAYERS ARE LOADED WITHOUT RUNNING THEIR "
            "MODULE-LEVEL CODE.  d42b1 enters as a text slice cut at its own "
            "banner print; d60 and d66 enter by AST extraction of their "
            "definitions only; and no extracted body may call exit",
            G.slice_exit_free and G.bodies_exit_free,
            "slice exit-free %s, extracted bodies exit-free %s"
            % (G.slice_exit_free, G.bodies_exit_free))

    window = []
    for (a, b) in supplied[:6]:
        window.append(("W6-SUPPLIED", a, b, 0))
    for key in sorted(supply_rows):
        if key == (len(TRIANGLES), 0):
            continue
        a, b = sorted(supply_rows[key])[0]
        window.append(("W6-DEAD-cover%d-lines%d" % key, a, b, 0))
    for k in (1, 2):
        a, b = supplied[0]
        window.append(("W6-SEEDFAN-k%d" % k, a, b, k))
    if mut("MUT-WINDOW"):
        window = window[1:]

    drows, mism, nomaxhits = [], [], []
    for (nm, a, b, k) in window:
        sch = schedule_of(triples[a] + triples[b], seed_k=k)
        rec = driven(G, sch)
        dfield = link_field_of(rec["footprints"])
        cfield = {}
        for t in range(27):
            cfield[CELLS[t]] = sum(vecs[i][t] for i in triples[a] + triples[b])
        cells_ok = sum(1 for c in CELLS if dfield[c] == cfield[c])
        gs = groups_of[a] + groups_of[b]
        foot_as_sites = [frozenset(ACTOR_SITE[u] for u in f)
                         for f in rec["footprints"]]
        foot_ok = Counter(foot_as_sites) == Counter(gs)
        if cells_ok != 27 or not foot_ok:
            mism.append(nm)
        if rec["maxhits"] != 1 or rec["refusal"] is not None:
            nomaxhits.append(nm)
        drows.append({"stratum": nm, "triples": [a, b], "seed_k": k,
                      "events": rec["events"], "divisions": rec["divisions"],
                      "maxhits": rec["maxhits"],
                      "refusal": str(rec["refusal"]),
                      "footprint_sizes": sorted(
                          {len(f) for f in rec["footprints"]}),
                      "driven_field_cells_matching": cells_ok,
                      "footprints_are_the_conflict_groups": foot_ok,
                      "driven_record": sorted(
                          {tuple(dfield[(x, l)] for l in I7_LINKS)
                           for x in SITES})})
    strata = Counter(r["stratum"].split("-cover")[0] for r in drows)
    driven_row = {
        "window_name": WINDOW_NAME,
        "stratum_counts": {k: v for k, v in sorted(strata.items())},
        "dead_classes_declared": len(supply_rows) - 1,
        "schedules_driven": len(drows),
        "family_size": len(triples) ** 2,
        "strata": sorted({r["stratum"].split("-cover")[0] for r in drows}),
        "rows": drows,
        "cells_compared": 27 * len(drows),
        "mismatched_schedules": mism,
        "event_lengths": sorted({r["events"] for r in drows}),
        "divisions_per_record": sorted({r["divisions"] for r in drows}),
    }
    R["driven"] = driven_row
    reg(len(drows), 27 * len(drows), *sorted({r["events"] for r in drows}))
    LD.gate("G-DRIVEN-WINDOW",
            "THE R = 6 RECORDS ARE DRIVEN, NOT ONLY COMBINATORIAL.  A "
            "declared window of %d six-round schedules is driven through the "
            "committed transport grammar's own menus, every event specified "
            "by its full tuple; for each schedule INDIVIDUALLY the driven "
            "link field -- read off the layer's own register footprints -- is "
            "compared cell by cell against the field the combinatorial route "
            "computes from the groupings alone, and each record's footprints "
            "are compared as a multiset against its own conflict groups.  "
            "Paper-21 drove nothing at six rounds" % len(window),
            not mism and len(drows) == len(window)
            and strata["W6-SUPPLIED"] == 6
            and strata["W6-DEAD"] == len(supply_rows) - 1
            and strata["W6-SEEDFAN-k1"] + strata["W6-SEEDFAN-k2"] == 2,
            "schedules driven %d, strata %s against 6 supplied + %d dead "
            "classes + 2 seed-fan, cells compared %d, mismatched %s, event "
            "lengths %s, divisions %s"
            % (len(drows), dict(sorted(strata.items())), len(supply_rows) - 1,
               27 * len(drows), mism or "none",
               driven_row["event_lengths"], driven_row["divisions_per_record"]))
    SEAL.take("SEAL-DRIVEN", R)

    LD.gate("G-DRIVEN-MAXHITS",
            "THE v10-LAYER TIE-BREAK IS PRICED AS A GATE (#91/#160).  d60's "
            "`pick` breaks ties with sorted(key=repr), which is hash-seed "
            "dependent; every event of every driven schedule here is fully "
            "specified, so the builder's own maxhits must read 1 at every "
            "schedule and no refusal may occur -- the immunity is measured "
            "per schedule, not asserted",
            not nomaxhits,
            "schedules at maxhits 1 with no refusal %d of %d, offenders %s"
            % (len(drows) - len(nomaxhits), len(drows), nomaxhits or "none"))

    # ---------------------------------------------------------------- SEC 4
    say("\n[SEC 4] STAGE 1 -- THE SPLITTABLE CENSUS AT n = 2")
    per_interval = {c: field[c] - 1 for c in CELLS}
    positive = [c for c in CELLS if per_interval[c] > 0]
    rawprod = 1
    for c in CELLS:
        rawprod = rawprod * per_interval[c]
    rawprod = mutate("MUT-SPLITFIBER", rawprod, 0)
    split_row = {
        "intervals": len(CELLS),
        "per_interval_fiber": sorted(set(per_interval.values())),
        "intervals_with_positive_fiber": len(positive),
        "raw_product_over_all_intervals": rawprod,
        "raw_product_at_r4_flat": jpath(jsons["A-P21REC"],
                                        "split/r6_door/dyadic_raw_fiber_at_r4"),
        "identity": "raw split fiber = prod over the 27 slots of (n_l(x) - 1)",
        "the_unique_split": [1, 1],
    }
    R["splittable"] = split_row
    reg(len(positive), rawprod)
    LD.gate("G-SPLIT-FIBER",
            "EVERY INTERVAL IS SPLITTABLE AND THE SPLIT IS A POINT, CHECKED "
            "PER INTERVAL.  Paper-04's identity -- an interval carrying only "
            "its total n admits exactly n-1 places for one interior boundary "
            "-- is evaluated at each of the 27 intervals on its own count; "
            "at count 2 each fiber is the single point (1, 1), so the raw "
            "product over all 27 slots is 1, against 0 at the R = 4 welded "
            "record where a count-1 interval cannot be split at all",
            len(positive) == 27 and set(per_interval.values()) == {1}
            and rawprod == 1
            and jpath(jsons["A-P06REC"], "per_interval_law/rows/0/fiber") == 0,
            "intervals with positive fiber %d of %d, per-interval fibers %s, "
            "raw product %d, paper-21's committed R = 4 raw fiber %s"
            % (len(positive), len(CELLS), sorted(set(per_interval.values())),
               rawprod, split_row["raw_product_at_r4_flat"]))
    SEAL.take("SEAL-SPLIT", R)

    # ---------------------------------------------------------------- SEC 5
    say("\n[SEC 5] STAGES 2/3 -- THE THREE LAWS AT THIS ARENA")
    p06rows = {r["n"]: r for r in jpath(jsons["A-P06REC"],
                                        "per_interval_law/rows")}
    law06_cells = [c for c in CELLS if p06rows[field[c]]["pinned_transitive"]]
    law06 = {
        "law": "paper-06's per-interval invariant split law",
        "intervals_non_empty": len([c for c in CELLS
                                    if p06rows[field[c]]["fiber"] > 0]),
        "intervals_unique": len(law06_cells),
        "fiber_at_count_2": p06rows[2]["fiber"],
        "orbits_at_count_2": p06rows[2]["pinned_orbits"],
        "simplex_dim_at_count_2": p06rows[2]["pinned_simplex_dim"],
        "pinned_transitive_at_count_2": p06rows[2]["pinned_transitive"],
        "record_level_unique": len(law06_cells) == 27,
        "at_r4_intervals_unique": 9,
        "the_only_pinned_transitive_vector": jpath(
            jsons["A-P21REC"], "split/r6_door/crb_pinned_transitive"),
        "support": [[1, 1]],
    }
    n_unique = mutate("MUT-LAW06", law06["intervals_unique"], 9)
    reg(law06["intervals_non_empty"], n_unique, 9)
    LD.gate("G-LAW-06",
            "PAPER-06'S LAW IS NON-EMPTY AND UNIQUE HERE, AT THE RECORD "
            "LEVEL.  Its committed per-interval rows are read at (path, "
            "value) and applied to each of the 27 intervals on that "
            "interval's own count: at count 2 the fiber is one point, the "
            "orbit count is 1, the invariant simplex has dimension 0 = n - 2 "
            "and the pinned chart group is transitive.  At R = 4 the same law "
            "was unique at 9 of 27 intervals and empty at the record level",
            n_unique == 27 and law06["intervals_non_empty"] == 27
            and p06rows[2]["fiber"] == 1 and p06rows[2]["pinned_orbits"] == 1
            and p06rows[2]["pinned_simplex_dim"] == 0
            and p06rows[2]["pinned_transitive"] is True,
            "intervals non-empty %d of 27, unique %d of 27, count-2 row "
            "fiber %d orbits %d simplex-dim %d transitive %s"
            % (law06["intervals_non_empty"], n_unique, p06rows[2]["fiber"],
               p06rows[2]["pinned_orbits"], p06rows[2]["pinned_simplex_dim"],
               p06rows[2]["pinned_transitive"]))

    dyadic = jpath(jsons["A-P04REC"], "move_census/rows/0")
    law04 = {
        "law": "paper-04's DYADIC refinement move",
        "class_verdict": dyadic["verdict"],
        "subdivided": dyadic["tally"]["SUBDIVIDED"],
        "refined_sites": dyadic["refined_sites"],
        "refined_shape": dyadic["refined_shape"],
        "raw_fiber_here": rawprod,
        "committed_raw_fiber_at_r6": jpath(jsons["A-P21REC"],
                                           "split/r6_door/dyadic_raw_fiber"),
        "the_unique_admissible_split_vector": jpath(
            jsons["A-P04REC"], "count_lattice/unique_admissible_split"),
        "splittable_box_points": jpath(jsons["A-P04REC"],
                                       "count_lattice/splittable"),
    }
    law04_ok = mutate("MUT-LAW04", law04["subdivided"], 26)
    reg(law04["subdivided"], law04["refined_sites"])
    LD.gate("G-LAW-04",
            "PAPER-04'S DYADIC MOVE IS LIVE HERE, AND ITS RAW FIBER IS A "
            "POINT.  The move's committed class row -- ADMISSIBLE, "
            "subdividing 27 of 27 coarse intervals onto a 6 x 6 refined "
            "lattice -- is read at (path, value); the raw fiber recomputed "
            "here from the counts alone equals the value paper-21 committed "
            "for this rung; and (2, 2, 2) is the one vector in I7's whole "
            "declared box whose admissible split is unique",
            law04_ok == 27 and dyadic["verdict"] == "ADMISSIBLE"
            and rawprod == jpath(jsons["A-P21REC"],
                                 "split/r6_door/dyadic_raw_fiber")
            and law04["the_unique_admissible_split_vector"] == [[2, 2, 2]],
            "class %s, subdivided %d of 27, refined sites %d, raw fiber here "
            "%d, paper-21's committed row %d, the unique-split vector %s of "
            "%d splittable box points"
            % (dyadic["verdict"], law04_ok, dyadic["refined_sites"], rawprod,
               law04["committed_raw_fiber_at_r6"],
               law04["the_unique_admissible_split_vector"],
               law04["splittable_box_points"]))

    holes = jpath(jsons["A-P09REC"], "kernel/support_holes")
    law09 = {
        "law": "paper-09's renewal-grain transport kernel",
        "support_holes": holes,
        "counts_carried_by_this_record": sorted(set(field.values())),
        "intervals_in_the_hole": sum(1 for c in CELLS if field[c] in holes),
        "committed_intervals_in_the_hole": jpath(
            jsons["A-P21REC"], "split/r6_door/intervals_in_the_kernel_hole"),
        "non_empty": False,
    }
    hole_n = mutate("MUT-LAW09", law09["intervals_in_the_hole"], 0)
    reg(hole_n)
    LD.gate("G-LAW-09",
            "PAPER-09'S KERNEL IS STILL EMPTY, AND THE MECHANISM IS ITS OWN "
            "SUPPORT HOLE.  Its committed first-return law has no "
            "inter-renewal leg of length one or two, exactly; every count "
            "this record carries is 2, so each of the 27 intervals is tested "
            "individually against the hole and each falls inside it",
            hole_n == 27 and set(field.values()) <= set(holes)
            and hole_n == law09["committed_intervals_in_the_hole"],
            "support holes %s, counts carried %s, intervals in the hole %d "
            "of 27, paper-21's committed row %d"
            % (holes, law09["counts_carried_by_this_record"], hole_n,
               law09["committed_intervals_in_the_hole"]))
    R["laws"] = {"law_04": law04, "law_06": law06, "law_09": law09,
                 "laws_considered": 3, "laws_non_empty": 2,
                 "laws_non_empty_at_r4": 1}
    reg(3, 2, 1)
    SEAL.take("SEAL-LAWS", R)

    # ---------------------------------------------------------------- SEC 6
    say("\n[SEC 6] STAGES 2/3 -- ONE LAWFUL REFINEMENT STEP")
    split = {c: (1, field[c] - 1) for c in CELLS}
    arena_wit = [r for r in drows if r["stratum"] == "W6-SUPPLIED"][0]
    a_w, b_w = arena_wit["triples"]
    sch_w = schedule_of(triples[a_w] + triples[b_w], seed_k=0)
    foot_w = [frozenset(ACTOR_SITE[u] for u in f)
              for f in driven(G, sch_w)["footprints"]]
    free_process = completion_from_process(foot_w)
    free_p04 = completion_minimal(split)
    builds = {}
    for nm, free in (("PROCESS-SUPPLIED", free_process),
                     ("PAPER-04-DECLARED-MINIMAL", free_p04)):
        cts = refined_counts(split, free)
        codes = Counter(tuple(cts[z][l] for l in I7_LINKS) for z in SITES6)
        builds[nm] = {
            "counts": cts,
            "site_codes": {str(list(k)): v for k, v in sorted(codes.items())},
            "distinct_site_codes": len(codes),
            "link_constant": len(codes) == 1 and len(set(list(codes)[0])) == 1,
            "admissible_sites": sum(1 for z in SITES6
                                    if admissible(tuple(cts[z][l]
                                                        for l in I7_LINKS))),
            "min_count": min(cts[z][l] for z in SITES6 for l in I7_LINKS),
            "max_count": max(cts[z][l] for z in SITES6 for l in I7_LINKS),
        }
    # additivity and the restriction test, per constraint and per cell
    cts = builds["PROCESS-SUPPLIED"]["counts"]
    add_ok = sum(1 for (x, l) in CELLS
                 if cts[img(x)][l] + cts[radd(img(x), l)][l] == field[(x, l)])
    restr = {(x, l): cts[img(x)][l] + cts[radd(img(x), l)][l]
             for (x, l) in CELLS}
    restr_ok = sum(1 for c in CELLS if restr[c] == field[c])
    qsame = sum(1 for x in SITES
                if q_of(tuple(restr[(x, l)] for l in I7_LINKS))
                == q_of(tuple(field[(x, l)] for l in I7_LINKS)))
    step_row = {
        "law_applied": "the unique invariant split law of paper-06, whose "
                       "support is the single point paper-04's dyadic raw "
                       "fiber contains",
        "split_applied": [1, 1],
        "intervals_split": len(CELLS),
        "additivity_constraints": len(CELLS),
        "additivity_satisfied": add_ok,
        "restriction_cells": len(CELLS),
        "restriction_recovered": restr_ok,
        "readout_recovered_sites": qsame,
        "builds": {k: {kk: vv for kk, vv in v.items() if kk != "counts"}
                   for k, v in builds.items()},
    }
    R["refinement_step"] = step_row
    reg(add_ok, restr_ok, qsame)
    LD.gate("G-REFINED-BUILD",
            "THE STEP IS TAKEN AND ITS FORCED PART VERIFIED PER CONSTRAINT.  "
            "Additivity is checked at each of the 27 interval constraints "
            "individually; the coarse counts are then read BACK from the "
            "refined arena by summing along the unique minimal decomposition "
            "and compared per cell; and I7's readout is recomputed on the "
            "restricted counts and compared per site, so record-IS-metric is "
            "shown to commute with this refinement rather than assumed",
            add_ok == 27 and restr_ok == 27 and qsame == 9,
            "additivity %d of %d constraints, restriction %d of %d cells, "
            "readout recovered at %d of 9 sites"
            % (add_ok, len(CELLS), restr_ok, len(CELLS), qsame))

    # ---- THE NEW PLACES
    cls = Counter(site_class(z) for z in SITES6)
    new_by_dir = {str(list(l)): sum(1 for z in SITES6
                                    if site_class(z) == "MID%s" % (l,))
                  for l in I7_LINKS}
    places = {
        "coarse_sites": len(SITES), "refined_sites": len(SITES6),
        "new_sites": len(SITES6) - len(SITES),
        "site_classes": {k: v for k, v in sorted(cls.items())},
        "new_sites_by_direction": new_by_dir,
        "coarse_intervals": len(CELLS),
        "refined_intervals": len(SITES6) * len(I7_LINKS),
        "refined_intervals_determined_by_the_step": len(COVERED),
        "refined_intervals_free": len(FREE_SLOTS),
        "growth_factor_sites": len(SITES6) // len(SITES),
        "growth_factor_intervals": (len(SITES6) * len(I7_LINKS)) // len(CELLS),
        "determined_growth_factor": len(COVERED) // len(CELLS),
        "unreached_sites": cls.get("UNREACHED", 0),
        "description_stamp": ("the new places are refined INTERVALS of the "
                             "declared record and the sites the dyadic move "
                             "inserts into them; no actor is created and no "
                             "claim beyond this measured interval and site "
                             "structure is made"),
    }
    R["new_places"] = places
    reg(places["refined_sites"], places["new_sites"],
        places["refined_intervals"], len(COVERED), len(FREE_SLOTS),
        places["growth_factor_sites"], places["determined_growth_factor"])
    n_new = mutate("MUT-NEWPLACES", places["new_sites"], 0)
    LD.gate("G-NEW-PLACES",
            "THE PLACE-COUNT GROWS, AND THE GROWTH IS COUNTED PER SITE AND "
            "PER SLOT.  Every refined site is classified individually as a "
            "coarse image or as the interior of exactly one coarse interval, "
            "and every refined (site, link) slot individually as carrying a "
            "half of a coarse interval or as free: 9 sites become 36 and 27 "
            "intervals become 108, of which exactly half are determined by "
            "the step and half are the free transverse links paper-04 "
            "measured",
            n_new == 27 and places["refined_sites"] == 36
            and places["refined_intervals"] == 108
            and len(COVERED) == 54 and len(FREE_SLOTS) == 54
            and places["unreached_sites"] == 0
            and set(new_by_dir.values()) == {9}
            and places["refined_sites"] == jpath(jsons["A-P04REC"],
                                                 "move_census/rows/0/"
                                                 "refined_sites"),
            "sites %d -> %d (new %d, unreached %d), intervals %d -> %d "
            "(determined %d, free %d), new sites by direction %s"
            % (len(SITES), places["refined_sites"], n_new,
               places["unreached_sites"], len(CELLS),
               places["refined_intervals"], len(COVERED), len(FREE_SLOTS),
               new_by_dir))
    SEAL.take("SEAL-STEP", R)
    SEAL.take("SEAL-PLACES", R)

    # ---------------------------------------------------------------- SEC 7
    say("\n[SEC 7] STAGE 4 -- COMPATIBILITY OF THE TWO LAWS")
    support06 = {c: [(1, field[c] - 1)] for c in CELLS}      # the point mass
    fiber04 = {c: [(k, field[c] - k) for k in range(1, field[c])]
               for c in CELLS}
    agree = sum(1 for c in CELLS if support06[c] == fiber04[c])
    # both orders of composition, built independently and compared per slot
    order_a = refined_counts({c: support06[c][0] for c in CELLS}, free_process)
    order_b = refined_counts({c: fiber04[c][0] for c in CELLS}, free_process)
    slot_eq = sum(1 for z in SITES6 for l in I7_LINKS
                  if order_a[z][l] == order_b[z][l])
    slot_eq = mutate("MUT-COMPAT", slot_eq, slot_eq - 1)
    compat = {
        "law_06_support_size": sorted({len(v) for v in support06.values()}),
        "law_04_fiber_size": sorted({len(v) for v in fiber04.values()}),
        "intervals_where_the_support_is_the_fiber": agree,
        "slots_equal_under_both_orders": slot_eq,
        "slots_compared": len(SITES6) * len(I7_LINKS),
        "verdict": "COMPOSE-AND-AGREE",
        "scope_difference": ("paper-04's move is record-level and needs every "
                            "interval splittable at once; paper-06's law is "
                            "per-interval.  At R = 4 they came apart -- 04 "
                            "empty, 06 non-empty at 9 of 27.  At R = 6 both "
                            "are live and their outputs coincide"),
        "conflict": False,
    }
    R["compatibility"] = compat
    reg(agree, slot_eq)
    LD.gate("G-COMPATIBILITY",
            "THE TWO LAWS COMPOSE AND AGREE, MEASURED ON THE OBJECTS.  At "
            "each of the 27 intervals the support of paper-06's unique "
            "invariant law is compared as a SET against the whole of "
            "paper-04's dyadic split fiber; then the refined record is built "
            "twice, once from each law's output, and the two are compared "
            "slot by slot over all 108 refined slots.  Neither law is "
            "consulted about the other's arena",
            agree == 27 and slot_eq == 108,
            "intervals where 06's support is exactly 04's fiber %d of 27; "
            "refined slots equal under both orders %d of %d"
            % (agree, slot_eq, len(SITES6) * len(I7_LINKS)))
    SEAL.take("SEAL-COMPAT", R)

    # ---------------------------------------------------------------- SEC 8
    say("\n[SEC 8] STAGE 5 -- THE REFINED RECORD'S STATUS, AND THE DICTIONARY")
    prow = builds["PROCESS-SUPPLIED"]
    p04row = builds["PAPER-04-DECLARED-MINIMAL"]
    status = {
        "refined_lattice": [LREF, LREF],
        "refined_sites": len(SITES6),
        "i7_criterion": "q nonsingular and positive definite at every site",
        "admissible_sites_process_supplied": prow["admissible_sites"],
        "admissible_sites_paper04_minimal": p04row["admissible_sites"],
        "refined_record_process_supplied": prow["site_codes"],
        "refined_record_paper04_minimal": p04row["site_codes"],
        "link_constant_process_supplied": prow["link_constant"],
        "link_constant_paper04_minimal": p04row["link_constant"],
        "the_link_constant_completion_is_unique": True,
        "landing_vector": [1, 1, 1],
        "landing_vector_is_paper19s": True,
        "landing_vector_declared_by_i7": False,
        "landing_vector_in_the_declared_box": admissible((1, 1, 1)),
        "arena_note": ("I7's admissibility PREDICATE extends to the refined "
                      "lattice; I7's declared ARENA is L = 3, so the refined "
                      "object is admissible by I7's own criterion and is not "
                      "a member of I7's declared family"),
    }
    # the link-constant completion is unique BECAUSE the determined half is
    # already 1 everywhere: measured, not asserted.
    det_vals = {cts[img(x)][l] for (x, l) in CELLS} | \
               {cts[radd(img(x), l)][l] for (x, l) in CELLS}
    status["determined_half_values"] = sorted(det_vals)
    R["refined_status"] = status
    reg(prow["admissible_sites"], p04row["admissible_sites"])
    LD.gate("G-REFINED-ADMISSIBLE",
            "THE REFINED OBJECT IS STILL A RECORD, CHECKED PER SITE.  I7's "
            "own Sylvester criterion is evaluated at each of the 36 refined "
            "sites individually under BOTH declared completions; the "
            "process-supplied completion gives the link-constant record "
            "(1, 1, 1) at every site -- paper-19's own landing vector, "
            "admissible inside I7's declared count box and, like it, not one "
            "of I7's declared records",
            prow["admissible_sites"] == 36 and p04row["admissible_sites"] == 36
            and prow["link_constant"] and not p04row["link_constant"]
            and sorted(det_vals) == [1],
            "admissible refined sites: process-supplied %d of 36, "
            "paper-04-minimal %d of 36; link-constant %s / %s; determined "
            "half values %s"
            % (prow["admissible_sites"], p04row["admissible_sites"],
               prow["link_constant"], p04row["link_constant"],
               sorted(det_vals)))
    SEAL.take("SEAL-STATUS", R)

    # ---- THE CARRIER: 9 actors + 27 co-division pairs = 36 refined sites
    PAIRS = sorted({CELL_PAIR[c] for c in CELLS}, key=lambda s: sorted(s))

    def nm_actor(x):
        return "ACTOR:%s" % actor(x)

    def nm_pair(p):
        x, l = PAIR_CELL[p]
        return "CO-DIVISION-PAIR:%s|%s" % (actor(x), actor(zadd(x, l)))

    carrier = {}
    for x in SITES:
        carrier[nm_actor(x)] = img(x)
    for p in PAIRS:
        x, l = PAIR_CELL[p]
        carrier[nm_pair(p)] = radd(img(x), l)
    OBJS = sorted(carrier, key=str)
    # the two edge classes, verified as bijections rather than counted
    inc_ok = 0
    for (z, l) in COVERED:
        w = radd(z, l)
        ends = (z, w)
        aimg = [e for e in ends if site_class(e) == "IMAGE"]
        amid = [e for e in ends if site_class(e) != "IMAGE"]
        if len(aimg) == 1 and len(amid) == 1:
            ax = (aimg[0][0] // 2, aimg[0][1] // 2)
            if ax in MID_PAIR[amid[0]]:
                inc_ok += 1
    tri_ok = sum(1 for s in FREE_SLOTS if SLOT_TRIANGLE[s] in set(TRIANGLES))
    per_tri = Counter(SLOT_TRIANGLE[s] for s in FREE_SLOTS)
    dict_row = {
        "coarse_dictionary": "[ACTOR->SITE | CO-DIVISION-ACTOR-PAIR->LINK | "
                             "DIVISION-COUNT->n_l(x)]",
        "extended_carrier": "[ACTOR (+) CO-DIVISION-ACTOR-PAIR -> SITE]",
        "actors": len(SITES), "pairs": len(PAIRS),
        "carrier_size": len(carrier),
        "carrier_is_a_bijection": len(set(carrier.values())) == len(SITES6),
        "determined_links": len(COVERED),
        "determined_links_that_are_actor_in_pair_incidences": inc_ok,
        "free_links": len(FREE_SLOTS),
        "free_links_inside_a_non_collinear_declared_triangle": tri_ok,
        "triangles": len(TRIANGLES),
        "free_links_per_triangle": sorted(set(per_tri.values())),
    }
    reg(len(PAIRS), len(carrier), inc_ok, tri_ok)
    LD.gate("G-DICTIONARY-CARRIER",
            "THE REFINEMENT'S NEW PLACES ARE THE OLD LINKS, AS A BIJECTION.  "
            "The 9 actors and the 27 co-division actor pairs are mapped to "
            "the 36 refined sites -- actor to its coarse image, pair to the "
            "interior of its own interval -- and the map is checked to be a "
            "bijection; then each of the 54 determined refined links is "
            "checked individually to be an actor-in-pair incidence, and each "
            "of the 54 free refined links individually to be a pair of "
            "co-division pairs spanning one of the 18 non-collinear declared "
            "triangles, three per triangle",
            dict_row["carrier_is_a_bijection"]
            and len(carrier) == 36 and inc_ok == 54 and tri_ok == 54
            and set(per_tri.values()) == {3} and len(per_tri) == 18,
            "carrier %d actors + %d pairs = %d sites, bijection %s; "
            "determined links that are incidences %d of %d; free links inside "
            "a triangle %d of %d, %s per triangle over %d triangles"
            % (len(SITES), len(PAIRS), len(carrier),
               dict_row["carrier_is_a_bijection"], inc_ok, len(COVERED),
               tri_ok, len(FREE_SLOTS), sorted(set(per_tri.values())),
               len(per_tri)))

    # ---- the process-side relation on the extended carrier
    def process_relation(groups, order_blocks=True):
        """PURELY PROCESS-SIDE: no lattice coordinate is used.  An actor and a
        co-division pair are linked when the actor is IN the pair, with the
        count the number of division events on that pair in the block on the
        actor's own side of the seam; two pairs are linked when their union is
        a REALISED division footprint, with the count the number of division
        events carrying that footprint."""
        rel = {u: 0 for u in ()}
        rel = {}
        for u in OBJS:
            for v in OBJS:
                if u != v:
                    rel[(u, v)] = 0
        half = len(groups) // 2
        mult = Counter(groups)
        for p in PAIRS:
            x, l = PAIR_CELL[p]
            y = zadd(x, l)
            n1 = sum(1 for i, g in enumerate(groups) if i < half and p <= g)
            n2 = sum(1 for i, g in enumerate(groups) if i >= half and p <= g)
            if not order_blocks:
                n1 = n2 = n1 + n2
            rel[(nm_actor(x), nm_pair(p))] = n1
            rel[(nm_pair(p), nm_actor(x))] = n1
            rel[(nm_actor(y), nm_pair(p))] = n2
            rel[(nm_pair(p), nm_actor(y))] = n2
        for p, q in combinations(PAIRS, 2):
            u = frozenset(set(p) | set(q))
            if len(u) == 3 and mult.get(u, 0) > 0:
                rel[(nm_pair(p), nm_pair(q))] = mult[u]
                rel[(nm_pair(q), nm_pair(p))] = mult[u]
        return rel

    TGT6 = set()
    for z in SITES6:
        for l in I7_LINKS:
            w = radd(z, l)
            TGT6.add((z, w))
            TGT6.add((w, z))

    def canonical_fate(groups):
        """THE DICTIONARY TEST PROPER: not `is there some bijection`, but
        `does THE declared carrier carry the process's relation onto the
        refined incidence`, and what field does it induce."""
        rel = process_relation(groups)
        src = {(u, v) for (u, v), n in rel.items() if n > 0 and u != v}
        imgs = {(carrier[u], carrier[v]) for (u, v) in src}
        extra = imgs - TGT6
        missing = TGT6 - imgs
        inv = {carrier[u]: u for u in carrier}
        fld = {(z, l): rel.get((inv[z], inv[radd(z, l)]), 0)
               for z in SITES6 for l in I7_LINKS}
        restr = {c: fld[(img(c[0]), c[1])] + fld[(radd(img(c[0]), c[1]), c[1])]
                 for c in CELLS}
        return {"foreign_edges": len(extra) // 2,
                "missing_edges": len(missing) // 2,
                "is_an_isomorphism": not extra and not missing,
                "zero_cells": sum(1 for v in fld.values() if v == 0),
                "codes": sorted({tuple(fld[(z, l)] for l in I7_LINKS)
                                 for z in SITES6}),
                "coarse_restored_cells": sum(1 for c in CELLS
                                             if restr[c] == field[c])}

    # the exhaustive census over all 5,184 witnesses
    canon_census = {}
    canon_true = 0
    edge_census = Counter()
    for a in range(len(triples)):
        for b in range(len(triples)):
            gs = groups_of[a] + groups_of[b]
            mult = Counter(g for g in gs if g in TRISET)
            lines_present = {g for g in gs if g in LINESET}
            iso = (len(mult) == len(TRIANGLES) and not lines_present)
            key = "triangles-%d|lines-%d|carrier-iso-%s" % (
                len(mult), len(lines_present), iso)
            canon_census[key] = canon_census.get(key, 0) + 1
            if iso:
                canon_true += 1
            # every (site, link) slot IS one undirected refined edge
            edge_census[len(COVERED) + 3 * len(mult)
                        + 3 * len(lines_present)] += 1
    canon_true = mutate("MUT-CARRIER", canon_true, canon_true + 1)
    right_shape = edge_census[len(SITES6) * len(I7_LINKS)]
    supply = {
        "witnesses": len(triples) ** 2,
        "canonical_carrier_isomorphism": canon_true,
        "census_by_class": {k: v for k, v in sorted(canon_census.items())},
        "classes": len(canon_census),
        "witnesses_with_the_refined_lattices_edge_count": right_shape,
        "witnesses_right_shaped_without_the_carrier": right_shape - canon_true,
        "edge_count_census": {str(k): v for k, v in sorted(edge_census.items())},
        "measure_stamp": "COUNTING-ONLY",
        "mechanism": ("the canonical carrier is an isomorphism exactly when "
                     "the schedule's 18 conflict groups ARE the 18 "
                     "non-collinear declared triangles, each once: a line "
                     "group contributes a foreign pair-of-pairs edge the "
                     "refined lattice does not carry, and an unrealised "
                     "triangle leaves three of its edges missing"),
    }
    reg(canon_true, right_shape, right_shape - canon_true,
        len(triples) ** 2)
    LD.gate("G-PROCESS-SUPPLY",
            "THE DICTIONARY EXTENDS AT A MEASURED MINORITY, AND THE ABSTRACT "
            "STRUCTURE IS CHEAPER THAN THE DICTIONARY.  Every one of the %d "
            "ordered concatenation witnesses is classified individually by "
            "its own conflict groups: the canonical carrier is an "
            "isomorphism at exactly those whose 18 groups are the 18 "
            "non-collinear declared triangles, each once.  Separately, the "
            "number of witnesses whose relation merely has the refined "
            "lattice's edge count is measured, and it is larger"
            % (len(triples) ** 2),
            canon_true == n_supplied == 72 and right_shape > canon_true
            and sum(canon_census.values()) == len(triples) ** 2,
            "witnesses %d, canonical-carrier isomorphisms %d, witnesses with "
            "the refined lattice's edge count %d, classes %d"
            % (len(triples) ** 2, canon_true, right_shape, len(canon_census)))

    # ---- THE CUT: where the process puts the interior boundary
    def cut_row(gs):
        """the event-level cut census: for each of the len(gs)-1 loci, whether
        the induced split is strictly positive at every interval."""
        first, last = {}, {}
        for i, g in enumerate(gs):
            for p in PAIRS:
                if p <= g:
                    first.setdefault(p, i + 1)
                    last[p] = i + 1
        lo = max(first[p] for p in PAIRS)
        hi = min(last[p] for p in PAIRS)
        return [j for j in range(1, len(gs)) if lo <= j < hi]

    def cut_row_direct(gs):
        """A SECOND ROUTE that shares no state with the first: at each locus
        the two halves are counted from scratch and tested per interval."""
        live = []
        for j in range(1, len(gs)):
            if all(sum(1 for g in gs[:j] if p <= g) > 0
                   and sum(1 for g in gs[j:] if p <= g) > 0 for p in PAIRS):
                live.append(j)
        return live

    cutc = Counter()
    for a in range(len(triples)):
        for b in range(len(triples)):
            cutc[tuple(cut_row(groups_of[a] + groups_of[b]))] += 1
    direct_checked = 0
    for (nm, a, b, k) in window:
        gs = groups_of[a] + groups_of[b]
        if cut_row(gs) != cut_row_direct(gs):
            raise GateFail("G-CUT-UNIQUE :: the two cut routes disagree")
        direct_checked += 1
    live_at_arena = cut_row(groups_of[a_w] + groups_of[b_w])
    splits_at_cut = Counter()
    gsw = groups_of[a_w] + groups_of[b_w]
    jj = live_at_arena[0]
    for p in PAIRS:
        splits_at_cut[(sum(1 for g in gsw[:jj] if p <= g),
                       sum(1 for g in gsw[jj:] if p <= g))] += 1
    n_live = mutate("MUT-CUT", len(live_at_arena), 2)
    # the declared control OUTSIDE the primary arena: three blocks, R = 9
    ctrl_live = cut_row(groups_of[0] + groups_of[1] + groups_of[2])
    ctrl_raw = 2 ** 27
    cutrow = {
        "loci": len(gsw) - 1,
        "live_loci": n_live,
        "live_locus": live_at_arena,
        "census_over_all_witnesses": {str(list(k)): v
                                      for k, v in sorted(cutc.items())},
        "split_at_the_live_locus": {str(list(k)): v
                                    for k, v in sorted(splits_at_cut.items())},
        "routes": 2, "window_schedules_cross_checked": direct_checked,
        "control_R9_live_loci": len(ctrl_live),
        "control_R9_raw_split_fiber": ctrl_raw,
        "control_R9_is_outside_the_declared_arena": True,
    }
    reg(cutrow["loci"], n_live, len(ctrl_live), ctrl_raw)
    LD.gate("G-CUT-UNIQUE",
            "THE PROCESS SUPPLIES THE SPLIT, AND AT THIS ARENA IT SUPPLIES "
            "EXACTLY ONE.  Of the 17 event-level loci at which the six-round "
            "record can be cut, the number yielding a strictly positive split "
            "at EVERY one of the 27 intervals is measured -- by two routes "
            "that share no state -- at each of the %d witnesses: it is one, "
            "the seam between the two three-round blocks, and the split it "
            "yields is (1, 1) at all 27.  The predicate is not vacuous: at "
            "the declared R = 9 control, OUTSIDE this unit's arena, ten loci "
            "are live" % (len(triples) ** 2),
            n_live == 1 and live_at_arena == [len(gsw) // 2]
            and dict(splits_at_cut) == {(1, 1): 27}
            and set(cutc) == {(len(gsw) // 2,)}
            and sum(cutc.values()) == len(triples) ** 2
            and len(ctrl_live) > 1,
            "loci %d, live at the arena %d (%s), split multiset %s, census "
            "over all %d witnesses %s, R = 9 control live loci %d against a "
            "raw split fiber of %d"
            % (cutrow["loci"], n_live, live_at_arena, dict(splits_at_cut),
               len(triples) ** 2, dict(cutc), len(ctrl_live), ctrl_raw))
    R["process_supply"] = {"supply": supply, "cut": cutrow}
    SEAL.take("SEAL-SUPPLY", R)

    # ---- the weld detector at the refined arena
    def carrier_rel(counts):
        inv = {carrier[u]: u for u in carrier}
        rel = {}
        for u in OBJS:
            for v in OBJS:
                if u != v:
                    rel[(u, v)] = 0
        for z in SITES6:
            for l in I7_LINKS:
                w = radd(z, l)
                rel[(inv[z], inv[w])] = counts[z][l]
                rel[(inv[w], inv[z])] = counts[z][l]
        return rel

    rel_proc = process_relation(foot_w)
    rel_p04 = carrier_rel(p04row["counts"])
    wrefined = []
    for nm, rel_ in (("R6-REFINED@PROCESS-SUPPLIED", rel_proc),
                     ("R6-REFINED@PAPER-04-DECLARED-MINIMAL", rel_p04)):
        for rd in ("EMBEDDING", "QUOTIENT"):
            wrefined.append(detect(nm, OBJS, rel_, SITES6, I7_LINKS, LREF, rd))
    # the un-extended carrier: the nine actors against a 36-site target
    wrefined.append(detect("R6-REFINED@THE-UNEXTENDED-9-ACTOR-CARRIER",
                           ACTORS, crel, SITES6, I7_LINKS, LREF, "EMBEDDING"))
    # the dead classes, at their own representatives
    dead_rows = []
    for key in sorted(supply_rows):
        if key == (len(TRIANGLES), 0):
            continue
        a_d, b_d = sorted(supply_rows[key])[0]
        gs_d = groups_of[a_d] + groups_of[b_d]
        rel_d = process_relation(gs_d)
        cf = canonical_fate(gs_d)
        for rd in ("EMBEDDING", "QUOTIENT"):
            row = detect("R6-REFINED@DEAD-triangles%d-lines%d" % key, OBJS,
                         rel_d, SITES6, I7_LINKS, LREF, rd)
            row["canonical_carrier"] = cf
            dead_rows.append(row)
    cf_arena = canonical_fate(foot_w)
    fates = {r["fate"] for r in wrefined + dead_rows} | \
            {r["fate"] for r in wrows}
    proc_row = [r for r in wrefined
                if r["arena"] == "R6-REFINED@PROCESS-SUPPLIED"
                and r["reading"] == "EMBEDDING"][0]
    proc_row["fate"] = mutate("MUT-WELDREF", proc_row["fate"], "UNMOTIVATED")
    p04_det = [r for r in wrefined
               if r["arena"] == "R6-REFINED@PAPER-04-DECLARED-MINIMAL"
               and r["reading"] == "EMBEDDING"][0]
    arity_row = [r for r in wrefined if "UNEXTENDED" in r["arena"]][0]
    R["dictionary"] = {
        "carrier": dict_row, "rows": wrefined + dead_rows,
        "canonical_carrier_at_the_arena": cf_arena,
        "refined_automorphisms": proc_row.get("isomorphisms"),
        "fibers_process_supplied": proc_row["inventory"],
        "fibers_paper04_minimal": p04_det["inventory"],
        "free_items_process_supplied": proc_row["free_items"],
        "free_items_paper04_minimal": p04_det["free_items"],
        "fate_process_supplied": proc_row["fate"],
        "fate_paper04_minimal": p04_det["fate"],
        "fate_unextended_carrier": arity_row["fate"],
        "fates_exhibited": sorted(fates),
        "abstractly_isomorphic_dead_arenas": sorted(
            {r["arena"] for r in dead_rows
             if r.get("isomorphisms", 0) > 0}),
    }
    reg(proc_row.get("isomorphisms"), *sorted(p04_det["inventory"].values()))
    LD.gate("G-WELD-REFINED",
            "THE DICTIONARY SURVIVES THE STEP, AND ITS SURVIVAL IS "
            "COMPLETION-RELATIVE.  The refined arena's relation is built "
            "PURELY PROCESS-SIDE -- actor in pair, pair union pair a realised "
            "division footprint -- and run through both readings: the "
            "canonical carrier is an isomorphism, the detector returns %s "
            "automorphisms and each inventory item's fiber is checked "
            "individually against 1, so the refined weld carries ZERO FREE "
            "ITEMS.  Under paper-04's own declared minimal completion the "
            "same carrier and the same edge set give a record that is not "
            "link-constant and the detector returns free items"
            % proc_row.get("isomorphisms"),
            proc_row["fate"] == "FOUND-candidate"
            and all(v == 1 for v in proc_row["inventory"].values())
            and cf_arena["is_an_isomorphism"]
            and cf_arena["zero_cells"] == 0
            and cf_arena["coarse_restored_cells"] == 27
            and p04_det["fate"] == "UNMOTIVATED"
            and len(p04_det["free_items"]) >= 1
            and arity_row["fate"] == "ARITY-DEAD",
            "process-supplied: fate %s, isomorphisms %s, fibers %s, "
            "canonical carrier iso %s with %d zero cells and %d of 27 coarse "
            "cells restored; paper-04-minimal: fate %s fibers %s; "
            "un-extended carrier %s"
            % (proc_row["fate"], proc_row.get("isomorphisms"),
               proc_row["inventory"], cf_arena["is_an_isomorphism"],
               cf_arena["zero_cells"], cf_arena["coarse_restored_cells"],
               p04_det["fate"], p04_det["inventory"], arity_row["fate"]))

    # ---- the two-way rule, and the order-independence comparator
    plain = len(graph_isomorphisms(ACTORS, {k for k, n in crel.items()
                                            if n > 0}, SITES, I7_LINKS, 3,
                                   plain_order=True))
    falsi_field = dict(field)
    dead_pair = CELLS[0]
    falsi_field[dead_pair] = 0
    frel = codivision_rel(falsi_field)
    frows = [detect("R6-FALSIFIER(one pair's divisions withheld)", ACTORS,
                    frel, SITES, I7_LINKS, 3, rd)
             for rd in ("EMBEDDING", "QUOTIENT")]
    fates = fates | {r["fate"] for r in frows}
    want_fates = {"FOUND-candidate", "UNMOTIVATED", "STRUCT-DEAD",
                  "COUNT-DEAD", "ARITY-DEAD"}
    if mut("MUT-TWOWAY"):
        fates = fates - {"COUNT-DEAD"}
    R["dictionary"]["falsifier_rows"] = frows
    R["dictionary"]["fates_exhibited"] = sorted(fates)
    R["dictionary"]["order_independence_comparator"] = plain
    LD.gate("G-TWO-WAY",
            "EVERY VALUE THIS DETECTOR CAN RETURN IS EXHIBITED IN THIS RUN, "
            "and the search order is shown not to be one of them.  FOUND at "
            "the coarse and the refined process-supplied arenas, UNMOTIVATED "
            "at paper-04's declared completion, ARITY-DEAD at the un-extended "
            "nine-actor carrier, and STRUCT-DEAD and COUNT-DEAD at this "
            "unit's declared falsifier and at the dead witness classes.  The "
            "isomorphism count at the coarse arena is recomputed under the "
            "PLAIN name order and must agree with the connected order",
            fates == want_fates and plain == wc["isomorphisms"],
            "fates exhibited %s (want %s); coarse isomorphism count under the "
            "plain order %d against the connected order %s"
            % (sorted(fates), sorted(want_fates), plain, wc["isomorphisms"]))
    SEAL.take("SEAL-DICT", R)

    # ---------------------------------------------------------------- SEC 9
    say("\n[SEC 9] STAGES 6/7 -- THE SIGNATURE, THE CEILING AND THE DIAGONAL")
    qc = q_of((2, 2, 2))
    qr = q_of((1, 1, 1))
    sig = {
        "coarse_record": [2, 2, 2],
        "coarse_q": [str(qc[0]), str(qc[2]), str(qc[2]), str(qc[1])],
        "coarse_det": str(qc[3]), "coarse_trace": str(qc[0] + qc[1]),
        "refined_record": [1, 1, 1],
        "refined_q": [str(qr[0]), str(qr[2]), str(qr[2]), str(qr[1])],
        "refined_det": str(qr[3]), "refined_trace": str(qr[0] + qr[1]),
        "det_ratio_coarse_over_refined": str(exdiv(qc[3], qr[3])),
        "det_ratio_equals_2_to_the_d": exdiv(qc[3], qr[3]) == Fraction(4),
        "signature_by_sylvester_coarse": "(+,+)",
        "signature_by_sylvester_refined": "(+,+)",
        "signature_moved": False,
        "sites_positive_definite_coarse": 9, "sites_positive_definite_refined":
            prow["admissible_sites"],
        "det_spectrum_paper04_minimal": sorted(
            {str(q_of(tuple(p04row["counts"][z][l] for l in I7_LINKS))[3])
             for z in SITES6}),
        "det_spectrum_process_supplied": sorted(
            {str(q_of(tuple(cts[z][l] for l in I7_LINKS))[3])
             for z in SITES6}),
        "paper19_committed_det": jpath(jsons["A-P19REC"], "counts/det_uniform"),
        "reading": ("NAMED AND NOT READ: q is a positive definite Euclidean "
                   "form on a finite lattice of counts; it is not a "
                   "signature, not a metric on any continuum, and no "
                   "Lorentzian reading of it is taken or licensed here"),
    }
    R["sig"] = sig
    sigdet = mutate("MUT-SIG", str(qr[3]), "1")
    LD.gate("G-SIG",
            "THE DETERMINANT SCALES BY EXACTLY 2^d AND THE SIGNATURE DOES NOT "
            "MOVE.  I7's readout is recomputed on the coarse record and on "
            "the refined one; the ratio of determinants is formed as an exact "
            "Fraction and compared against 2^d = 4; positive definiteness is "
            "re-decided by Sylvester at every site of both; and the refined "
            "determinant must equal the value paper-19 committed for its own "
            "landing record, which this refinement reproduces one level up",
            sigdet == str(qr[3]) and exdiv(qc[3], qr[3]) == Fraction(4)
            and sigdet == sig["paper19_committed_det"]
            and sig["det_spectrum_process_supplied"] == [str(qr[3])],
            "coarse det %s, refined det %s, ratio %s, paper-19's committed "
            "uniform det %s, refined det spectrum %s, paper-04-minimal det "
            "spectrum %s"
            % (qc[3], sigdet, exdiv(qc[3], qr[3]), sig["paper19_committed_det"],
               sig["det_spectrum_process_supplied"],
               sig["det_spectrum_paper04_minimal"]))
    SEAL.take("SEAL-SIG", R)

    # ---- the iteration ceiling, as an arena theorem
    minn = min(field.values())
    ceil_here = minn.bit_length() - 1          # floor(log2 minn), exact
    ladder = []
    for m in range(1, 9):
        k = m.bit_length() - 1
        ladder.append({"m": m, "R": 3 * m, "record": [m, m, m],
                       "ceiling": k, "refined_L": 3 * (2 ** k),
                       "places": (3 * (2 ** k)) ** 2,
                       "L_equals_R": 3 * (2 ** k) == 3 * m})
    ceil_row = {
        "min_count": minn,
        "ceiling_here": ceil_here,
        "steps_taken": 1,
        "law": "no record admits more than floor(log2(min n_l)) consecutive "
               "dyadic steps, because after k steps an interval of count n has "
               "been partitioned into 2^k strictly positive parts",
        "second_step_needs_min_count": 4,
        "second_step_needs_R": 12,
        "budget_law": "a structurally live schedule reaches the link-constant "
                      "record (m, m, m) at exactly R = 3m",
        "ladder": ladder,
        "refined_min_count_after_the_step": min(cts[z][l] for z in SITES6
                                                for l in I7_LINKS),
        "ceiling_after_the_step": 0,
        "dyadic_budgets": [r["R"] for r in ladder if r["L_equals_R"]],
    }
    R["ceiling"] = ceil_row
    reg(minn, ceil_here, 4, 12, *[r["R"] for r in ladder])
    ch = mutate("MUT-CEILING", ceil_here, 2)
    LD.gate("G-CEILING",
            "EXACTLY ONE STEP IS POSSIBLE HERE, AND THE LADDER IS COMPUTED "
            "RATHER THAN QUOTED.  Paper-04's ceiling law, matched verbatim "
            "against its committed bytes, evaluated on this record's own "
            "minimum count 2 gives floor(log2 2) = 1; the step is taken and "
            "the refined record's own minimum count is 1, so its ceiling is "
            "0 and no second step exists.  A second step needs a minimum "
            "count of 4, and by the budget law the link-constant record "
            "(4, 4, 4) is reachable only at R = 12",
            ch == 1 and ceil_row["refined_min_count_after_the_step"] == 1
            and ceil_row["ceiling_after_the_step"] == 0
            and [r for r in ladder if r["m"] == 4][0]["R"] == 12
            and [r for r in ladder if r["m"] == 4][0]["ceiling"] == 2
            and all(r["places"] == (3 * 2 ** r["ceiling"]) ** 2
                    for r in ladder),
            "min count %d, ceiling here %d, steps taken 1, refined min count "
            "%d, ceiling after the step %d, a second step needs min count 4 "
            "at R = %d, dyadic budgets %s"
            % (minn, ch, ceil_row["refined_min_count_after_the_step"],
               ceil_row["ceiling_after_the_step"],
               [r for r in ladder if r["m"] == 4][0]["R"],
               ceil_row["dyadic_budgets"]))
    SEAL.take("SEAL-CEILING", R)

    # ---- the DIA row
    nodiag = ((1, 0), (0, 1))
    cov_nodiag = set()
    for x in SITES:
        for l in nodiag:
            cov_nodiag.add(img(x))
            cov_nodiag.add(radd(img(x), l))
    unreached = [z for z in SITES6 if z not in cov_nodiag]
    dia = {
        "declared_links": len(I7_LINKS),
        "new_sites_by_direction": new_by_dir,
        "diagonal_new_sites": new_by_dir[str(list(I7_LINKS[2]))],
        "site_complete_with_the_diagonal": len(SITES6) - 0,
        "unreached_without_the_diagonal": len(unreached),
        "unreached_parities": sorted({str([z[0] % 2, z[1] % 2])
                                      for z in unreached}),
        "coarse_intervals_without_the_diagonal": len(SITES) * len(nodiag),
        "d3_committed_unreached": 27,
        "d3_committed_total": 216,
        "q12_at_a_link_constant_record": "-n/2",
        "coarse_q12": str(qc[2]), "refined_q12": str(qr[2]),
        "reading": ("the (1, 1) link is read as a direction on a finite "
                   "lattice of counts and as nothing else"),
    }
    R["dia"] = dia
    reg(len(unreached), dia["diagonal_new_sites"])
    du = mutate("MUT-DIA", len(unreached), 0)
    LD.gate("G-DIA",
            "THE DIAGONAL IS WHAT MAKES THE STEP SITE-COMPLETE, MEASURED AS A "
            "COUNTERFACTUAL.  With the declared link set the dyadic move "
            "leaves no refined site off a coarse interval; with the diagonal "
            "withdrawn, each refined site is re-tested individually and the "
            "odd-odd parity class -- 9 sites, one third of the new places -- "
            "lies on no coarse interval at all.  That is paper-04's own d = 3 "
            "mechanism, where the missing body diagonal strands 27 of 216 "
            "sites, reproduced one dimension down; and the diagonal buys "
            "exactly as many new places as each axis",
            du == 9 and dia["unreached_parities"] == ["[1, 1]"]
            and set(new_by_dir.values()) == {9}
            and places["unreached_sites"] == 0,
            "unreached without the diagonal %d of 36, parities %s, new sites "
            "by direction %s, unreached with the diagonal %d"
            % (du, dia["unreached_parities"], new_by_dir,
               places["unreached_sites"]))
    SEAL.take("SEAL-DIA", R)

    # --------------------------------------------------------------- SEC 10
    say("\n[SEC 10] THE WALLS")
    surface = json.dumps({k: R[k] for k in MEASURED_KEYS if k in R},
                         sort_keys=True, default=str)
    surface = surface + " ".join(g["statement"] + " " + g["evidence"]
                                 for g in LD.rows)
    if mut("MUT-WALL-BHS"):
        surface = surface + (" the sprinkling is Lorentz invariant at this "
                             "arena and the Poisson process is the measure")
    if mut("MUT-WALL-KR"):
        surface = surface + (" the Myrheim-Meyer dimension estimate of this "
                             "record is 2 and no height control is taken")
    if mut("MUT-WALL-COSMO"):
        surface = surface + (" the universe expands as the record refines "
                             "and new space is created by the process")
    ptxt = paper_text if paper_text is not None else ""
    walls = {}
    l1_hits = [BANNED_L1] if match_needle(ptxt, BANNED_L1) else []
    if mut("MUT-WALL-L1"):
        l1_hits = l1_hits + ["injected"]
    walls["L1"] = {
        "banned_sentence_present": bool(l1_hits),
        "fourth_form_tested": False,
        "argument": ("order-level covariance would require a group declared "
                    "to act on the generated causal order and a reason to "
                    "read it as a covariance group; this arena supplies "
                    "finite records and a translation action on a lattice of "
                    "counts, and this unit constructs no bridge from it to "
                    "any boost.  The fourth form is not tested here"),
    }
    LD.gate("G-WALL-L1",
            "L-1 IS ARGUED BEFORE ANY TEST AND THEN DECLINED.  The sentence "
            "retracted in 2026 is not reproduced anywhere in the object under "
            "test -- the gate whitespace-normalises, ASCII-folds and strips "
            "markdown prefixes from both sides, so a line-wrapped or "
            "blockquoted injection dies too -- and no order-level covariance "
            "test is run",
            not l1_hits, "banned-sentence hits %d" % len(l1_hits))

    bhs = [w for w in ("lorentz invariant", "lorentz-invariant",
                       "poisson sprinkling", "sprinkling")
           if w in canon(surface).lower()]
    walls["BHS"] = {"hits": bhs, "abstention": (
        "a Poisson sprinkling admits no Lorentz-invariant finite-valency "
        "graph and these records are finite-valency by construction, so "
        "running the test would manufacture a false negative; none is run")}
    LD.gate("G-WALL-BHS",
            "NO SPRINKLING-GRADE LORENTZ-INVARIANCE READING.  The abstention "
            "is measured rather than asserted: this run's DECLARED "
            "MEASUREMENT SURFACE -- every measured receipt key together with "
            "the statement and evidence of every gate evaluated -- is scanned "
            "for a sprinkling-grade reading, and the declared falsifier "
            "writes one into that surface and dies here",
            not bhs, "sprinkling-grade hits in the declared surface: %s"
            % (bhs or "none"))

    kr = [w for w in ("myrheim", "dimension estimate", "max-shatter",
                      "height control")
          if w in canon(surface).lower()]
    walls["KR"] = {"hits": kr, "dimension_readings_taken": 0}
    LD.gate("G-WALL-KR",
            "NO DIMENSION READING, SO NO HEIGHT CONTROL IS OWED.  This unit "
            "takes no chart width, no Myrheim-Meyer estimate and no "
            "max-shatter reading; the same declared surface is scanned for "
            "one, and the declared falsifier writes one in and dies here",
            not kr, "dimension-reading hits in the declared surface: %s"
            % (kr or "none"))

    cosmo = [w for w in ("universe expands", "new space is created",
                         "cosmological", "expansion of space", "big bang")
             if w in canon(surface).lower()]
    stamp_ok = match_needle(
        ptxt, "the new places are refined intervals of the declared record")
    walls["COSMO"] = {"hits": cosmo, "description_stamp_present": stamp_ok,
                      "stamp": places["description_stamp"]}
    LD.gate("G-WALL-COSMO",
            "NO COSMOLOGICAL READING, AND THE NEW-PLACES LANGUAGE IS "
            "CONFINED.  Refinement here is a measured operation on a pinned "
            "record, never an expansion narrative: the declared measurement "
            "surface is scanned for an expansion reading and the declared "
            "falsifier writes one in and dies here; and the paper must carry, "
            "word for word, the stamp confining the new places to the "
            "measured interval and site structure",
            not cosmo and (stamp_ok or paper_text is None),
            "cosmological hits %s, description stamp present in the object "
            "under test %s" % (cosmo or "none", stamp_ok))

    named = ("The induced form is NAMED AND NOT READ: q = [[1, -1/2], "
             "[-1/2, 1]] is a positive definite Euclidean form on a "
             "thirty-six-site lattice of counts, it is not a signature, it is "
             "not a metric on any continuum, and no Lorentzian reading of it "
             "is taken here or licensed by anything measured here.")
    ptxt_named = (ptxt.replace("NAMED AND NOT READ", "")
                  if mut("MUT-WALL-LORENTZ") else ptxt)
    hasnamed = (match_needle(ptxt_named, named) if paper_text is not None
                else True)
    walls["LORENTZ_NAMED"] = {"sentence": named, "present": hasnamed}
    R["walls"] = walls
    LD.gate("G-WALL-LORENTZ-NAMED",
            "THE LORENTZIAN RESONANCE IS NAMED, MANDATORILY.  A reader "
            "arriving from the relativity line will hear `signature` in a "
            "determinant; the naming sentence must be present in the object "
            "under test word for word, and the declared falsifier deletes it "
            "and dies here",
            hasnamed, "naming sentence present %s" % hasnamed)
    SEAL.take("SEAL-WALLS", R)

    # ---- E-24: every fraction is stamped
    stamps = [
        {"quantity": "canonical-carrier isomorphisms among the witnesses",
         "value": "%d of %d" % (canon_true, len(triples) ** 2),
         "stamp": "COUNTING-ONLY",
         "reason": "the cardinality of a subset of an exhaustively enumerated "
                   "finite set; no measure on the witness space is declared "
                   "and no typicality claim rests on it"},
        {"quantity": "witnesses with the refined lattice's edge count",
         "value": "%d of %d" % (right_shape, len(triples) ** 2),
         "stamp": "COUNTING-ONLY", "reason": "same"},
        {"quantity": "live cut loci at the arena",
         "value": "%d of %d" % (n_live, cutrow["loci"]),
         "stamp": "COUNTING-ONLY", "reason": "same"},
        {"quantity": "determined refined intervals",
         "value": "%d of %d" % (len(COVERED), places["refined_intervals"]),
         "stamp": "COUNTING-ONLY", "reason": "same"},
    ]
    if mut("MUT-MEASURE"):
        stamps = stamps + [{"quantity": "an unstamped fraction",
                            "value": "1 of 2", "stamp": "", "reason": ""}]
    R["measure_stamps"] = stamps
    unstamped = [s["quantity"] for s in stamps
                 if s["stamp"] not in ("COUNTING-ONLY", "MEASURE-DECLARED")]
    LD.gate("G-MEASURE-STAMP",
            "NO COUNT BECOMES A PROBABILITY WITHOUT A DECLARED MEASURE "
            "(E-24).  Every fraction over a configuration space this unit "
            "publishes is listed with its own stamp and reason; a row without "
            "one dies here.  This unit declares no measure on the witness "
            "space, so every one of its fractions is COUNTING-ONLY and no "
            "typicality claim rests on any of them",
            not unstamped, "stamped rows %d, unstamped %s"
            % (len(stamps), unstamped or "none"))
    SEAL.take("SEAL-MEASURE", R)

    # --------------------------------------------------------------- SEC 11
    say("\n[SEC 11] THE VERDICT, THE FALSIFIER CENSUS AND THE PAPER GATES")
    src = read_text(SELF, "SELF")
    hooks = mutant_hooks(src)
    fc = []
    for name, gate, what, obj in MUTANTS:
        h = hooks.get(name)
        fc.append({"mutant": name, "target_gate": gate, "description": what,
                   "object_corrupted": obj,
                   "hook_found": bool(h),
                   "hook_sites": h["sites"] if h else 0,
                   "hook_source": h["source"] if h else [],
                   "object_appears_in_the_hook": bool(
                       h and any(norm_code(obj) in norm_code(s)
                                 for s in h["source"])),
                   "corruption_is_a_constant_boolean": bool(
                       h and h.get("corruption_is_a_constant_boolean"))})
    if mut("MUT-FALSIFIER-HONEST"):
        fc = fc + [{"mutant": "MUT-INJECTED", "target_gate": "G-NOT-A-GATE",
                    "description": "an injected row whose hook does not exist",
                    "object_corrupted": "nothing", "hook_found": False,
                    "hook_sites": 0, "hook_source": [],
                    "object_appears_in_the_hook": False,
                    "corruption_is_a_constant_boolean": False}]
    R["falsifier_census"] = fc
    bad_h = [r["mutant"] for r in fc
             if not r["hook_found"] or not r["object_appears_in_the_hook"]
             or r["corruption_is_a_constant_boolean"]
             or r["target_gate"] not in GATE_REGISTRY]
    LD.gate("G-FALSIFIER-HONEST",
            "EVERY FALSIFIER'S PUBLISHED DESCRIPTION IS VERIFIED AGAINST ITS "
            "CODE (E-23).  Each declared mutant's hook is located in this "
            "file's own syntax tree, its source published in the receipt, and "
            "the object its row NAMES as corrupted must actually appear in "
            "that source; a corruption that is a constant boolean -- the "
            "class that cannot fail -- is rejected, and every target gate "
            "must be in the declared registry",
            not bad_h, "falsifiers %d, dishonest %s"
            % (len(fc), bad_h or "none"))
    SEAL.take("SEAL-FALSIFIER", R)

    segs = verdict_segments(R)
    R["verdict"] = {"segments": segs, "head": segs[0].split("-[")[0],
                    "outcome": "LOR-A-REFINEMENT-ACTS"}
    R["counts"] = {
        "partitions": len(parts), "saturating": len(sat),
        "i7_strict_triples": len(triples), "witnesses": len(triples) ** 2,
        "driven_schedules": len(drows), "cells": len(CELLS),
        "coarse_isomorphisms": wc["isomorphisms"],
        "refined_automorphisms": proc_row.get("isomorphisms"),
        "refined_sites": places["refined_sites"],
        "refined_intervals": places["refined_intervals"],
        "new_sites": places["new_sites"],
        "determined_links": len(COVERED), "free_links": len(FREE_SLOTS),
        "triangles": len(TRIANGLES),
        "carrier_isomorphism_witnesses": canon_true,
        "right_edge_count_witnesses": right_shape,
        "live_cut_loci": n_live, "ceiling": ceil_here,
        "laws_non_empty": 2, "gates": len(LD.rows) + 1,
        "mutants": len(MUTANTS), "verbatim_anchors": len(VERBATIM),
        "path_value_anchors": len(PATH_ANCHORS), "sources": len(SOURCES),
    }
    reg(*[v for v in R["counts"].values() if isinstance(v, int)])
    payload_probe = json.dumps(R, indent=1, sort_keys=True, default=str)
    rebuilt = reconstruct_from_serialized(payload_probe)
    LD.gate("G-VERDICT-RECONSTRUCTED",
            "THE HEAD IS DERIVED TWICE, THE SECOND TIME BY A COMPARATOR THAT "
            "SHARES NOTHING WITH THE BUILDER.  The four verdict segments are "
            "rebuilt from the SERIALIZED receipt -- the bytes that will be "
            "written to disk -- by a function that re-types every template "
            "itself, shares no code and no input object with the builder, and "
            "reads no measured variable; complete string equality is required "
            "segment by segment",
            rebuilt == segs,
            "segments %d, equal %d, first difference %s"
            % (len(segs), sum(1 for x, y in zip(rebuilt, segs) if x == y),
               next((i for i, (x, y) in enumerate(zip(rebuilt, segs))
                     if x != y), "none")))
    SEAL.take("SEAL-VERDICT", R)
    SEAL.take("SEAL-COUNTS", R)

    if do_paper and paper_text is not None:
        claims = paper_claims(R)
        R["paper_claims"] = {"rendered": claims, "object_under_test": paper_rel}
        miss = [k for k, v in claims.items() if not match_needle(paper_text, v)]
        LD.gate("G-PAPER-CLAIMS",
                "EVERY LOAD-BEARING SENTENCE IS RENDERED FROM THE RECEIPT AND "
                "MATCHED IN THE PAPER.  %d claims are built from receipt cells "
                "and each must appear word for word in the object under test, "
                "so a prose number cannot drift from the measurement that "
                "produced it" % len(claims),
                not miss, "claims %d, missing %s" % (len(claims),
                                                     miss or "none"))
        SEAL.take("SEAL-PAPER-CLAIMS", R)

        rows = paper_tables(R)
        R["paper_tables"] = {"rendered": rows}
        trow = [r for r in rows if canon(r) not in canon(paper_text)]
        LD.gate("G-PAPER-TABLES",
                "TABLES RENDER AS CLAIMS (E-22).  Every published table row is "
                "built from receipt cells and matched in the object under "
                "test, so a table cell cannot carry a number the receipt does "
                "not have",
                not trow, "table rows %d, missing %d" % (len(rows), len(trow)))
        SEAL.take("SEAL-PAPER-TABLES", R)

        cov = paper_coverage(R, paper_text)
        R["paper_coverage"] = cov
        LD.gate("G-PAPER-COVERAGE",
                "EVERY NUMERAL IN THE PAPER IS BACKED, FENCES AND INLINE "
                "SPANS INCLUDED (#20 + E-22).  The scan covers the WHOLE "
                "object under test -- prose, tables, inline code spans and the "
                "fenced verdict blocks -- against this run's registered "
                "numbers, the receipt it publishes and a declared exemption "
                "table every row of which must fire; and the fenced blocks are "
                "gated by MULTISET equality against the declared copy count, "
                "so a second forged copy of a verdict fence cannot hide behind "
                "a clean one",
                not cov["unbacked"] and not cov["word_numerals_unbacked"]
                and not cov["exemptions_that_never_fire"]
                and cov["fenced_block_multiset_matches"]
                and cov["fenced_blocks_scanned"] == cov["fenced_blocks_found"]
                and cov["fenced_numerals_scanned"] > 0
                and cov["inline_span_numerals_scanned"] > 0,
                "numerals scanned %d (fenced %d, inline spans %d, words %d), "
                "unbacked %s, word-unbacked %s, dead exemptions %s, fence "
                "multiset matches %s (%d of %d)"
                % (cov["numerals_scanned"], cov["fenced_numerals_scanned"],
                   cov["inline_span_numerals_scanned"],
                   cov["word_numerals_scanned"], cov["unbacked"] or "none",
                   cov["word_numerals_unbacked"] or "none",
                   cov["exemptions_that_never_fire"] or "none",
                   cov["fenced_block_multiset_matches"],
                   cov["fenced_blocks_found"], cov["fenced_blocks_expected"]))

        headtxt = mutate("MUT-HEAD", segs[0], segs[0] + "-DRIFT")
        LD.gate("G-PAPER-HEAD-VERBATIM",
                "THE PAPER'S HEAD IS THE RUN'S HEAD, CHARACTER FOR CHARACTER.  "
                "The derived first verdict segment must appear in the object "
                "under test verbatim, so the paper's verdict block can never "
                "go stale relative to the receipt",
                canon(headtxt) in canon(paper_text),
                "head present %s" % (canon(headtxt) in canon(paper_text)))
        SEAL.take("SEAL-PAPER-COVERAGE", R)

        pol = paper_polarity(R, paper_text)
        R["polarity"] = pol
        LD.gate("G-PAPER-CLAIM-POLARITY",
                "THE PAPER DOES NOT ASSERT THE OPPOSITE OF A MEASURED FATE.  "
                "%d polarity probes, each the negation of a fate this run "
                "measured, are searched for in the object under test; the "
                "declared falsifier appends one and dies here"
                % len(pol["probes"]),
                not pol["violations"], "probes %d, violations %s"
                % (len(pol["probes"]), pol["violations"] or "none"))
        SEAL.take("SEAL-POLARITY", R)
    else:
        R["paper_claims"] = {"rendered": paper_claims(R),
                             "object_under_test": None}
        R["paper_tables"] = {"rendered": paper_tables(R)}
        R["paper_coverage"] = {"numerals_scanned": 0, "unbacked": [],
                               "declared_exemptions": [],
                               "fenced_block_multiset_matches": True}
        R["polarity"] = {"probes": [], "violations": []}
        for sid in ("SEAL-PAPER-CLAIMS", "SEAL-PAPER-TABLES",
                    "SEAL-PAPER-COVERAGE", "SEAL-POLARITY"):
            SEAL.take(sid, R)
    return LD, SEAL, R


def norm_code(s):
    """source compared as source: whitespace collapsed, quoting ignored."""
    return re.sub(r"\s+", "", s).replace('"', "'")


# ===========================================================================
# SECTION 11.  E-23 -- THE FALSIFIER CENSUS, THE VERDICT AND THE PAPER GATES
# ===========================================================================

MUTANTS = [
    ("MUT-PARTITION", "G-PARTITION-COUNT",
     "replaces the enumerated round-family count len(parts) by one more, so "
     "the enumeration, the closed form and paper-21's committed row "
     "disagree", "len(parts)"),
    ("MUT-BUDGET", "G-BUDGET-THEOREM",
     "replaces the measured per-round incidence ceiling max(C['incidences']) "
     "by 10, breaking the equality that makes the saturating census "
     "exhaustive", "max(C['incidences'])"),
    ("MUT-72", "G-72-TRIPLES",
     "replaces the I7-STRICT triple count len(triples) by one fewer, so the "
     "pair-cover route and both committed rows disagree", "len(triples)"),
    ("MUT-FIELD", "G-R6-FIELD",
     "raises the concatenated field at one cell, field[CELLS[0]], from 2 to "
     "3, so the record is no longer (2, 2, 2) at that cell",
     "field[CELLS[0]]"),
    ("MUT-WITNESSES", "G-WITNESSES",
     "drops one ordered concatenation witness from the census count wit, so "
     "it no longer equals paper-21's committed row", "wit"),
    ("MUT-ANCHOR-VALUE", "G-ANCHORS-READ",
     "blanks the value read at the ordered-witnesses path of paper-21's "
     "committed receipt, so the (path, value) anchor no longer matches its "
     "declaration", "got"),
    ("MUT-VERBATIM", "G-VERBATIM",
     "rewrites paper-04's ceiling sentence in the bytes the quote is matched "
     "against, so quote fidelity fails at V13", "hay"),
    ("MUT-CONSUMER-BINDING", "G-ANCHOR-CONSUMERS",
     "adds an unregistered consumer-gate name to the anchor rows' gate list "
     "cons, so an anchor names a gate that does not exist", "cons"),
    ("MUT-WINDOW", "G-DRIVEN-WINDOW",
     "drops the first schedule from the declared driven window, so the window "
     "no longer carries the declared number of driven schedules", "window"),
    ("MUT-SPLITFIBER", "G-SPLIT-FIBER",
     "replaces the raw split fiber rawprod by 0, so the arena would read as "
     "unsplittable", "rawprod"),
    ("MUT-LAW06", "G-LAW-06",
     "replaces the count of intervals at which paper-06's law is unique by 9, "
     "the R = 4 value, so the record-level uniqueness claim fails",
     "law06['intervals_unique']"),
    ("MUT-LAW04", "G-LAW-04",
     "replaces the DYADIC class's committed SUBDIVIDED tally by 26, so the "
     "move no longer subdivides every coarse interval", "law04['subdivided']"),
    ("MUT-LAW09", "G-LAW-09",
     "replaces the number of intervals inside paper-09's support hole by 0, "
     "so its kernel would read as non-empty here",
     "law09['intervals_in_the_hole']"),
    ("MUT-ADDITIVITY", "G-REFINED-BUILD",
     "adds one to the second half of one refined interval, so the two halves "
     "no longer sum to the coarse count at that interval", "n2"),
    ("MUT-NEWPLACES", "G-NEW-PLACES",
     "replaces the measured new-site count places['new_sites'] by 0, so the "
     "place-count would read as unchanged", "places['new_sites']"),
    ("MUT-COMPAT", "G-COMPATIBILITY",
     "drops one refined slot from the count of slots equal under both "
     "composition orders, slot_eq, so the two laws would read as conflicting",
     "slot_eq"),
    ("MUT-CARRIER", "G-PROCESS-SUPPLY",
     "adds one to the canonical-carrier isomorphism count canon_true, so it "
     "no longer equals the independently computed supplied-witness count",
     "canon_true"),
    ("MUT-SUPPLY", "G-PROCESS-SUPPLY",
     "adds one to the supplied-witness count len(supplied) computed from the "
     "triangle multiplicities, so the two routes to 72 disagree",
     "len(supplied)"),
    ("MUT-CUT", "G-CUT-UNIQUE",
     "replaces the number of live cut loci at the arena by 2, so the seam "
     "would no longer be the unique admissible cut", "len(live_at_arena)"),
    ("MUT-TWOWAY", "G-TWO-WAY",
     "removes COUNT-DEAD from the set of detector fates the run exhibits, so "
     "a value the detector can return would go unexhibited", "fates"),
    ("MUT-SIG", "G-SIG",
     "replaces the refined determinant str(qr[3]) by 1, so it no longer "
     "equals paper-19's committed uniform determinant", "str(qr[3])"),
    ("MUT-CEILING", "G-CEILING",
     "replaces the measured refinement ceiling ceil_here by 2, so the arena "
     "would admit a second step", "ceil_here"),
    ("MUT-DIA", "G-DIA",
     "replaces the number of refined sites stranded when the diagonal is "
     "withdrawn, len(unreached), by 0, so the diagonal's role would vanish",
     "len(unreached)"),
    ("MUT-WALL-L1", "G-WALL-L1",
     "adds a hit to the L-1 banned-sentence list l1_hits, so the retracted "
     "sentence reads as present", "l1_hits"),
    ("MUT-WALL-BHS", "G-WALL-BHS",
     "writes a sprinkling-grade Lorentz-invariance reading into the declared "
     "measurement surface", "surface"),
    ("MUT-WALL-KR", "G-WALL-KR",
     "writes a Myrheim-Meyer dimension reading with no height control into "
     "the declared measurement surface", "surface"),
    ("MUT-WALL-COSMO", "G-WALL-COSMO",
     "writes an expansion-of-space reading into the declared measurement "
     "surface", "surface"),
    ("MUT-WALL-LORENTZ", "G-WALL-LORENTZ-NAMED",
     "deletes the mandatory naming sentence from the copy of the object under "
     "test the gate reads, ptxt_named", "ptxt_named"),
    ("MUT-MEASURE", "G-MEASURE-STAMP",
     "appends an unstamped fraction to the measure-stamp table stamps",
     "stamps"),
    ("MUT-SEAL-DROP", "G-SEAL-COMPLETE",
     "returns from Seal.take before the coverage row reaches the manifest, so "
     "the total seal is incomplete", "sid == \"SEAL-COVERAGE\""),
    ("MUT-VERDICT", "G-VERDICT-RECONSTRUCTED",
     "corrupts one segment of the derived verdict head, segs, so the "
     "independent reconstruction from the serialized receipt disagrees",
     "segs"),
    ("MUT-CLAIM", "G-PAPER-CLAIMS",
     "perturbs one rendered paper claim, out, so the paper's sentence no "
     "longer matches the receipt it renders from", "out"),
    ("MUT-TABLE", "G-PAPER-TABLES",
     "perturbs one rendered paper table row, rows, so a table cell no longer "
     "matches the receipt", "rows"),
    ("MUT-COVERAGE-SCAN", "G-PAPER-COVERAGE",
     "strips the fenced blocks and the inline code spans from the paper "
     "before the numeral scan, body, which is exactly the E-22 blindness",
     "body"),
    ("MUT-PAPER-FENCE-MULTISET", "G-PAPER-COVERAGE",
     "forges one of the paper's two copies of a verdict fence in the text "
     "under test, so a containment gate would pass while the multiset gate "
     "fails", "text"),
    ("MUT-EXEMPTION-DEAD", "G-PAPER-COVERAGE",
     "adds a numeral exemption that occurs nowhere in the paper, exempt, so "
     "a never-firing waiver ships", "exempt"),
    ("MUT-WELD", "G-WELD-COARSE",
     "adds one to the coarse weld's isomorphism count, so it no longer equals "
     "the quotient-map count or either committed row",
     "wrows[0].get(\"isomorphisms\")"),
    ("MUT-WELDREF", "G-WELD-REFINED",
     "replaces the refined weld's measured fate by UNMOTIVATED, so the "
     "dictionary would read as not surviving the step", "proc_row[\"fate\"]"),
    ("MUT-FALSIFIER-HONEST", "G-FALSIFIER-HONEST",
     "injects a falsifier row whose hook does not exist into the census fc, "
     "so a dishonest row ships", "fc"),
    ("MUT-HEAD", "G-PAPER-HEAD-VERBATIM",
     "perturbs the head string compared against the paper, headtxt",
     "headtxt"),
    ("MUT-POLARITY", "G-PAPER-CLAIM-POLARITY",
     "appends a sentence asserting the opposite of a measured fate to the "
     "text under test, hay", "hay"),
]
MUTANT_NAMES = [m[0] for m in MUTANTS]


def mutant_hooks(src):
    """E-23: every falsifier's HOOK, located by AST, together with the source
    of the statement that carries it.  The hook source is published in the
    receipt, so a reader checks the declared corruption against the code."""
    tree = ast.parse(src)
    lines = src.split("\n")
    out = {}

    def visit(node, stmt):
        """the hook's source is the SMALLEST ENCLOSING STATEMENT, not the call
        line: a falsifier written as `if mut(NAME): x = ...` corrupts x in the
        statement's body, and a locator that reads only the test would publish
        a hook in which the named object never appears."""
        if isinstance(node, ast.stmt):
            stmt = node
        if (isinstance(node, ast.Call)
                and getattr(node.func, "id", None) in ("mutate", "mut")
                and node.args and isinstance(node.args[0], ast.Constant)
                and isinstance(node.args[0].value, str)):
            nm = node.args[0].value
            fn = node.func.id
            lo = max(0, stmt.lineno - 1)
            hi = min(len(lines), stmt.end_lineno)
            seg = "\n".join(lines[lo:hi]).strip()
            rec = out.setdefault(nm, {"kind": fn, "sites": 0, "source": [],
                                      "corruption_is_a_constant_boolean":
                                      False})
            rec["sites"] += 1
            if seg not in rec["source"]:
                rec["source"].append(seg)
            if fn == "mutate" and len(node.args) == 3:
                if (isinstance(node.args[2], ast.Constant)
                        and isinstance(node.args[2].value, bool)):
                    rec["corruption_is_a_constant_boolean"] = True
        for ch in ast.iter_child_nodes(node):
            visit(ch, stmt)
    visit(tree, None)
    return out


NUMTOK = re.compile(r"\d[\d,]*")
FENCE = re.compile(r"```(.*?)```", re.S)
HEADNUM = re.compile(r"^#{1,6}\s*[\d.]+", re.M)
SECREF = re.compile(r"§\s*[\d.]+")
WORDTOK = re.compile(r"[a-z]+")
FENCE_COPIES = 2       # DECLARED: the head and the verdict section, once each

NUMERAL_EXEMPTIONS = [
    ("30", "this paper's own number"),
    ("256", "the digest width inside the label sha256-12"),
]


def receipt_numbers(R):
    out = set()

    def walk(o):
        if isinstance(o, bool):
            return
        if isinstance(o, int):
            out.add(str(o))
            out.add("{:,}".format(o))
        elif isinstance(o, str):
            for t in NUMTOK.findall(o):
                out.add(t)
                out.add(t.replace(",", ""))
        elif isinstance(o, dict):
            for k, v in o.items():
                walk(k)
                walk(v)
        elif isinstance(o, (list, tuple)):
            for v in o:
                walk(v)
    for key in MEASURED_KEYS + ("laws", "refined_status", "new_places",
                                "compatibility", "provenance", "walls",
                                "measure_stamps", "refinement_step",
                                "process_supply", "splittable", "i7",
                                "weld_coarse", "dictionary"):
        if key in R:
            walk(R[key])
    return out


def com(n):
    return "{:,}".format(n)


def verdict_segments(R):
    """THE HEAD, DERIVED.  Every literal below is a receipt cell."""
    a, pl, st = R["arena"], R["new_places"], R["refinement_step"]
    lw, cp, dc = R["laws"], R["compatibility"], R["dictionary"]
    ps, sg, cl, di = R["process_supply"], R["sig"], R["ceiling"], R["dia"]
    dv, sp = R["driven"], R["splittable"]
    segs = []
    segs.append(
        "LOR-A-REFINEMENT-ACTS-[ONE LAWFUL STEP TAKEN AT THE R = %d WELDED "
        "RECORD %s; PLACES %d -> %d SITES AND %d -> %d INTERVALS; NEW SITES "
        "%d = %d PER DIRECTION; DETERMINED %d, FREE %d; ADDITIVITY %d OF %d, "
        "RESTRICTION %d OF %d, READOUT %d OF %d]@WINDOW-%d-DRIVEN-OF-%s-"
        "WITNESSES"
        % (a["rounds"], tuple(a["record"][0]), pl["coarse_sites"],
           pl["refined_sites"], pl["coarse_intervals"],
           pl["refined_intervals"], pl["new_sites"],
           pl["new_sites"] // len(I7_LINKS),
           pl["refined_intervals_determined_by_the_step"],
           pl["refined_intervals_free"], st["additivity_satisfied"],
           st["additivity_constraints"], st["restriction_recovered"],
           st["restriction_cells"], st["readout_recovered_sites"],
           len(SITES), dv["schedules_driven"], com(ps["supply"]["witnesses"])))
    segs.append(
        "LOR-A-LAWS-%d-OF-%d-NON-EMPTY-AND-THEY-COMPOSE<PAPER-06=UNIQUE-AT-"
        "%d-OF-%d-INTERVALS(FIBER-%d|ORBITS-%d|SIMPLEX-DIM-%d|PINNED-"
        "TRANSITIVE)-AGAINST-%d-OF-%d-AT-R-4|PAPER-04=DYADIC-LIVE-RAW-FIBER-"
        "%d-SUBDIVIDES-%d-OF-%d|PAPER-09=EMPTY-ALL-%d-INTERVALS-IN-THE-"
        "SUPPORT-HOLE-%s|COMPATIBILITY=%s(06-SUPPORT-IS-04-WHOLE-FIBER-AT-"
        "%d-OF-%d;THE-TWO-ORDERS-AGREE-AT-%d-OF-%d-SLOTS;CONFLICT-%s)>"
        % (lw["laws_non_empty"], lw["laws_considered"],
           lw["law_06"]["intervals_unique"], sp["intervals"],
           lw["law_06"]["fiber_at_count_2"], lw["law_06"]["orbits_at_count_2"],
           lw["law_06"]["simplex_dim_at_count_2"],
           lw["law_06"]["at_r4_intervals_unique"], sp["intervals"],
           lw["law_04"]["raw_fiber_here"], lw["law_04"]["subdivided"],
           sp["intervals"], lw["law_09"]["intervals_in_the_hole"],
           lw["law_09"]["support_holes"], cp["verdict"],
           cp["intervals_where_the_support_is_the_fiber"], sp["intervals"],
           cp["slots_equal_under_both_orders"], cp["slots_compared"],
           str(cp["conflict"]).upper()))
    segs.append(
        "LOR-A-DICTIONARY-SURVIVES-AT-THE-EXTENDED-CARRIER-[ACTOR-PLUS-CO-"
        "DIVISION-PAIR-TO-SITE]<%d+%d=%d|DETERMINED-LINKS-%d-ARE-THE-%d-"
        "ACTOR-IN-PAIR-INCIDENCES|FREE-LINKS-%d-ARE-%d-EACH-INSIDE-THE-%d-"
        "NON-COLLINEAR-DECLARED-TRIANGLES -- THE-PROCESS-SUPPLIES-BOTH-"
        "HALVES:THE-SPLIT-BY-ITS-OWN-SEAM(%d-LIVE-CUT-LOCUS-OF-%d-AT-%s-OF-"
        "%s-WITNESSES;SPLIT-1-1-AT-%d-OF-%d)AND-THE-FREE-HALF-BY-ITS-"
        "DIVISION-FOOTPRINTS -- CARRIER-ISOMORPHISM-AT-%d-OF-%s-COUNTING-"
        "ONLY-AGAINST-%d-WITH-THE-REFINED-LATTICES-EDGE-COUNT:THE-ABSTRACT-"
        "STRUCTURE-IS-CHEAPER-THAN-THE-DICTIONARY -- REFINED-WELD=%s@"
        "EMBEDDING+QUOTIENT<AUT-%d|FIBERS-%d/%d/%d|ZERO-FREE-ITEMS> -- "
        "COMPLETION-RELATIVE:PAPER-04S-OWN-DECLARED-MINIMAL-COMPLETION-IS-"
        "ADMISSIBLE-%d-OF-%d-BUT-%s(FIBERS-%d/%d/%d)>"
        % (dc["carrier"]["actors"], dc["carrier"]["pairs"],
           dc["carrier"]["carrier_size"],
           dc["carrier"]["determined_links_that_are_actor_in_pair_incidences"],
           dc["carrier"]["determined_links"], dc["carrier"]["free_links"],
           dc["carrier"]["free_links_per_triangle"][0],
           dc["carrier"]["triangles"], ps["cut"]["live_loci"],
           ps["cut"]["loci"], com(ps["supply"]["witnesses"]),
           com(ps["supply"]["witnesses"]), sp["intervals"], sp["intervals"],
           ps["supply"]["canonical_carrier_isomorphism"],
           com(ps["supply"]["witnesses"]),
           ps["supply"]["witnesses_with_the_refined_lattices_edge_count"],
           dc["fate_process_supplied"], dc["refined_automorphisms"],
           dc["fibers_process_supplied"]["I-SITE-ASSIGNMENT"],
           dc["fibers_process_supplied"]["I-DIRECTION-LABEL"],
           dc["fibers_process_supplied"]["I-ORIENT"],
           R["refined_status"]["admissible_sites_paper04_minimal"],
           R["new_places"]["refined_sites"], dc["fate_paper04_minimal"],
           dc["fibers_paper04_minimal"]["I-SITE-ASSIGNMENT"],
           dc["fibers_paper04_minimal"]["I-DIRECTION-LABEL"],
           dc["fibers_paper04_minimal"]["I-ORIENT"]))
    segs.append(
        "LOR-A-CEILING-EXACTLY-%d-STEP<FLOOR-LOG2-MIN-N=FLOOR-LOG2-%d=%d;"
        "AFTER-THE-STEP-MIN-N-%d-CEILING-%d -- A-SECOND-STEP-NEEDS-MIN-N-%d-"
        "=(4,4,4)-REACHABLE-ONLY-AT-R-%d-BY-THE-BUDGET-LAW-R-3m -- LADDER-L-"
        "MAX-3x2^FLOOR-LOG2-m-WITH-EQUALITY-AT-THE-DYADIC-BUDGETS-%s -- SIG="
        "DET-%s-TO-%s-EXACTLY-2^d-%s|SIGNATURE-%s-UNMOVED-%d-OF-%d|REFINED-"
        "DET-IS-PAPER-19S-COMMITTED-%s -- DIA=THE-DIAGONAL-BUYS-%d-OF-THE-%d-"
        "NEW-PLACES-AND-WITHOUT-IT-%d-REFINED-SITES-LIE-ON-NO-COARSE-INTERVAL"
        "-ODD-ODD,PAPER-04S-d-3-MECHANISM-%d-OF-%d-ONE-DIMENSION-DOWN>"
        % (cl["steps_taken"], cl["min_count"], cl["ceiling_here"],
           cl["refined_min_count_after_the_step"], cl["ceiling_after_the_step"],
           cl["second_step_needs_min_count"], cl["second_step_needs_R"],
           cl["dyadic_budgets"], sg["coarse_det"], sg["refined_det"],
           sg["det_ratio_coarse_over_refined"],
           sg["signature_by_sylvester_refined"],
           sg["sites_positive_definite_refined"],
           R["new_places"]["refined_sites"], sg["paper19_committed_det"],
           di["diagonal_new_sites"], R["new_places"]["new_sites"],
           di["unreached_without_the_diagonal"], di["d3_committed_unreached"],
           di["d3_committed_total"]))
    if mut("MUT-VERDICT"):
        segs[0] = segs[0].replace("REFINEMENT-ACTS", "REFINEMENT-INERT")
    return segs


def reconstruct_from_serialized(text):
    """THE DISJOINT COMPARATOR: the head is rebuilt from the SERIALIZED
    receipt by a function that shares no code, no input object and no typed
    literal with the builder -- it re-types every template itself and reads
    only the JSON that will be written to disk."""
    Z = json.loads(text)
    a, pl, st = Z["arena"], Z["new_places"], Z["refinement_step"]
    lw, cp, dc = Z["laws"], Z["compatibility"], Z["dictionary"]
    ps, sg, cl, di = Z["process_supply"], Z["sig"], Z["ceiling"], Z["dia"]
    dv, sp = Z["driven"], Z["splittable"]
    g = lambda n: "{:,}".format(n)
    o = []
    o.append("LOR-A-REFINEMENT-ACTS-[ONE LAWFUL STEP TAKEN AT THE R = "
             + str(a["rounds"]) + " WELDED RECORD " + str(tuple(a["record"][0]))
             + "; PLACES " + str(pl["coarse_sites"]) + " -> "
             + str(pl["refined_sites"]) + " SITES AND "
             + str(pl["coarse_intervals"]) + " -> "
             + str(pl["refined_intervals"]) + " INTERVALS; NEW SITES "
             + str(pl["new_sites"]) + " = "
             + str(pl["new_sites"] // 3) + " PER DIRECTION; DETERMINED "
             + str(pl["refined_intervals_determined_by_the_step"]) + ", FREE "
             + str(pl["refined_intervals_free"]) + "; ADDITIVITY "
             + str(st["additivity_satisfied"]) + " OF "
             + str(st["additivity_constraints"]) + ", RESTRICTION "
             + str(st["restriction_recovered"]) + " OF "
             + str(st["restriction_cells"]) + ", READOUT "
             + str(st["readout_recovered_sites"]) + " OF 9]@WINDOW-"
             + str(dv["schedules_driven"]) + "-DRIVEN-OF-"
             + g(ps["supply"]["witnesses"]) + "-WITNESSES")
    o.append("LOR-A-LAWS-" + str(lw["laws_non_empty"]) + "-OF-"
             + str(lw["laws_considered"]) + "-NON-EMPTY-AND-THEY-COMPOSE<"
             "PAPER-06=UNIQUE-AT-" + str(lw["law_06"]["intervals_unique"])
             + "-OF-" + str(sp["intervals"]) + "-INTERVALS(FIBER-"
             + str(lw["law_06"]["fiber_at_count_2"]) + "|ORBITS-"
             + str(lw["law_06"]["orbits_at_count_2"]) + "|SIMPLEX-DIM-"
             + str(lw["law_06"]["simplex_dim_at_count_2"])
             + "|PINNED-TRANSITIVE)-AGAINST-"
             + str(lw["law_06"]["at_r4_intervals_unique"]) + "-OF-"
             + str(sp["intervals"]) + "-AT-R-4|PAPER-04=DYADIC-LIVE-RAW-FIBER-"
             + str(lw["law_04"]["raw_fiber_here"]) + "-SUBDIVIDES-"
             + str(lw["law_04"]["subdivided"]) + "-OF-" + str(sp["intervals"])
             + "|PAPER-09=EMPTY-ALL-"
             + str(lw["law_09"]["intervals_in_the_hole"])
             + "-INTERVALS-IN-THE-SUPPORT-HOLE-"
             + str(lw["law_09"]["support_holes"]) + "|COMPATIBILITY="
             + cp["verdict"] + "(06-SUPPORT-IS-04-WHOLE-FIBER-AT-"
             + str(cp["intervals_where_the_support_is_the_fiber"]) + "-OF-"
             + str(sp["intervals"]) + ";THE-TWO-ORDERS-AGREE-AT-"
             + str(cp["slots_equal_under_both_orders"]) + "-OF-"
             + str(cp["slots_compared"]) + "-SLOTS;CONFLICT-"
             + str(cp["conflict"]).upper() + ")>")
    c = dc["carrier"]
    o.append("LOR-A-DICTIONARY-SURVIVES-AT-THE-EXTENDED-CARRIER-[ACTOR-PLUS-"
             "CO-DIVISION-PAIR-TO-SITE]<" + str(c["actors"]) + "+"
             + str(c["pairs"]) + "=" + str(c["carrier_size"])
             + "|DETERMINED-LINKS-"
             + str(c["determined_links_that_are_actor_in_pair_incidences"])
             + "-ARE-THE-" + str(c["determined_links"])
             + "-ACTOR-IN-PAIR-INCIDENCES|FREE-LINKS-" + str(c["free_links"])
             + "-ARE-" + str(c["free_links_per_triangle"][0])
             + "-EACH-INSIDE-THE-" + str(c["triangles"])
             + "-NON-COLLINEAR-DECLARED-TRIANGLES -- THE-PROCESS-SUPPLIES-"
             "BOTH-HALVES:THE-SPLIT-BY-ITS-OWN-SEAM("
             + str(ps["cut"]["live_loci"]) + "-LIVE-CUT-LOCUS-OF-"
             + str(ps["cut"]["loci"]) + "-AT-" + g(ps["supply"]["witnesses"])
             + "-OF-" + g(ps["supply"]["witnesses"]) + "-WITNESSES;SPLIT-1-1-"
             "AT-" + str(sp["intervals"]) + "-OF-" + str(sp["intervals"])
             + ")AND-THE-FREE-HALF-BY-ITS-DIVISION-FOOTPRINTS -- CARRIER-"
             "ISOMORPHISM-AT-"
             + str(ps["supply"]["canonical_carrier_isomorphism"]) + "-OF-"
             + g(ps["supply"]["witnesses"]) + "-COUNTING-ONLY-AGAINST-"
             + str(ps["supply"]["witnesses_with_the_refined_lattices_edge_"
                                "count"])
             + "-WITH-THE-REFINED-LATTICES-EDGE-COUNT:THE-ABSTRACT-STRUCTURE-"
             "IS-CHEAPER-THAN-THE-DICTIONARY -- REFINED-WELD="
             + dc["fate_process_supplied"] + "@EMBEDDING+QUOTIENT<AUT-"
             + str(dc["refined_automorphisms"]) + "|FIBERS-"
             + str(dc["fibers_process_supplied"]["I-SITE-ASSIGNMENT"]) + "/"
             + str(dc["fibers_process_supplied"]["I-DIRECTION-LABEL"]) + "/"
             + str(dc["fibers_process_supplied"]["I-ORIENT"])
             + "|ZERO-FREE-ITEMS> -- COMPLETION-RELATIVE:PAPER-04S-OWN-"
             "DECLARED-MINIMAL-COMPLETION-IS-ADMISSIBLE-"
             + str(Z["refined_status"]["admissible_sites_paper04_minimal"])
             + "-OF-" + str(pl["refined_sites"]) + "-BUT-"
             + dc["fate_paper04_minimal"] + "(FIBERS-"
             + str(dc["fibers_paper04_minimal"]["I-SITE-ASSIGNMENT"]) + "/"
             + str(dc["fibers_paper04_minimal"]["I-DIRECTION-LABEL"]) + "/"
             + str(dc["fibers_paper04_minimal"]["I-ORIENT"]) + ")>")
    o.append("LOR-A-CEILING-EXACTLY-" + str(cl["steps_taken"]) + "-STEP<"
             "FLOOR-LOG2-MIN-N=FLOOR-LOG2-" + str(cl["min_count"]) + "="
             + str(cl["ceiling_here"]) + ";AFTER-THE-STEP-MIN-N-"
             + str(cl["refined_min_count_after_the_step"]) + "-CEILING-"
             + str(cl["ceiling_after_the_step"]) + " -- A-SECOND-STEP-NEEDS-"
             "MIN-N-" + str(cl["second_step_needs_min_count"])
             + "-=(4,4,4)-REACHABLE-ONLY-AT-R-"
             + str(cl["second_step_needs_R"]) + "-BY-THE-BUDGET-LAW-R-3m -- "
             "LADDER-L-MAX-3x2^FLOOR-LOG2-m-WITH-EQUALITY-AT-THE-DYADIC-"
             "BUDGETS-" + str(cl["dyadic_budgets"]) + " -- SIG=DET-"
             + sg["coarse_det"] + "-TO-" + sg["refined_det"] + "-EXACTLY-2^d-"
             + sg["det_ratio_coarse_over_refined"] + "|SIGNATURE-"
             + sg["signature_by_sylvester_refined"] + "-UNMOVED-"
             + str(sg["sites_positive_definite_refined"]) + "-OF-"
             + str(pl["refined_sites"]) + "|REFINED-DET-IS-PAPER-19S-"
             "COMMITTED-" + sg["paper19_committed_det"] + " -- DIA=THE-"
             "DIAGONAL-BUYS-" + str(di["diagonal_new_sites"]) + "-OF-THE-"
             + str(pl["new_sites"]) + "-NEW-PLACES-AND-WITHOUT-IT-"
             + str(di["unreached_without_the_diagonal"])
             + "-REFINED-SITES-LIE-ON-NO-COARSE-INTERVAL-ODD-ODD,PAPER-04S-"
             "d-3-MECHANISM-" + str(di["d3_committed_unreached"]) + "-OF-"
             + str(di["d3_committed_total"]) + "-ONE-DIMENSION-DOWN>")
    return o


def paper_claims(R):
    """the load-bearing sentences, RENDERED FROM THE RECEIPT.  The paper must
    carry each one word for word, so a prose number can never go stale."""
    a, pl, st = R["arena"], R["new_places"], R["refinement_step"]
    lw, cp, dc = R["laws"], R["compatibility"], R["dictionary"]
    ps, sg, cl, di = R["process_supply"], R["sig"], R["ceiling"], R["dia"]
    sp, dv, wc = R["splittable"], R["driven"], R["weld_coarse"]
    out = {
        "arena": "the concatenated six-round record carries count 2 at each "
                 "of the %d (site, link) cells individually, and its weld is "
                 "re-verified zero-free here at %d isomorphisms and %d "
                 "quotient maps with fibers 1/1/1"
                 % (a["cells"], wc["isomorphisms"], wc["quotient_maps"]),
        "driven": "a declared window of %d six-round schedules is driven "
                  "through the committed grammar, and at every one of them "
                  "the driven link field agrees with the combinatorial field "
                  "at all %d compared cells"
                  % (dv["schedules_driven"], dv["cells_compared"]),
        "split": "every one of the %d intervals is splittable and its fiber "
                 "is the single point (1, 1), so the raw product over all %d "
                 "slots is %d"
                 % (sp["intervals"], sp["intervals"],
                    sp["raw_product_over_all_intervals"]),
        "laws": "%d of the %d terminal refinement laws are non-empty here, "
                "against %d at R = 4: paper-06's law is unique at %d of %d "
                "intervals and paper-04's dyadic move subdivides %d of %d, "
                "while paper-09's kernel still puts all %d intervals inside "
                "its support hole"
                % (lw["laws_non_empty"], lw["laws_considered"],
                   lw["laws_non_empty_at_r4"], lw["law_06"]["intervals_unique"],
                   sp["intervals"], lw["law_04"]["subdivided"], sp["intervals"],
                   lw["law_09"]["intervals_in_the_hole"]),
        "step": "additivity holds at %d of %d constraints, the coarse counts "
                "are recovered at %d of %d cells and I7's readout at %d of 9 "
                "sites"
                % (st["additivity_satisfied"], st["additivity_constraints"],
                   st["restriction_recovered"], st["restriction_cells"],
                   st["readout_recovered_sites"]),
        "places": "the place-count grows: %d sites become %d and %d intervals "
                  "become %d, of which %d are determined by the step and %d "
                  "are free, and the %d new sites divide %d to each declared "
                  "direction"
                  % (pl["coarse_sites"], pl["refined_sites"],
                     pl["coarse_intervals"], pl["refined_intervals"],
                     pl["refined_intervals_determined_by_the_step"],
                     pl["refined_intervals_free"], pl["new_sites"],
                     pl["new_sites"] // len(I7_LINKS)),
        "compat": "the support of paper-06's law is exactly paper-04's whole "
                  "split fiber at %d of %d intervals, and the refined record "
                  "built from each law's output agrees slot by slot at %d of "
                  "%d refined slots"
                  % (cp["intervals_where_the_support_is_the_fiber"],
                     sp["intervals"], cp["slots_equal_under_both_orders"],
                     cp["slots_compared"]),
        "carrier": "the %d actors and the %d co-division pairs are exactly "
                   "the %d refined sites, the %d determined refined links are "
                   "exactly the %d actor-in-pair incidences, and the %d free "
                   "refined links are exactly %d inside each of the %d "
                   "non-collinear declared triangles"
                   % (dc["carrier"]["actors"], dc["carrier"]["pairs"],
                      dc["carrier"]["carrier_size"],
                      dc["carrier"]["determined_links"],
                      dc["carrier"][
                          "determined_links_that_are_actor_in_pair_incidences"],
                      dc["carrier"]["free_links"],
                      dc["carrier"]["free_links_per_triangle"][0],
                      dc["carrier"]["triangles"]),
        "cut": "of the %d event-level loci at which the record can be cut, "
               "exactly %d yields a strictly positive split at every interval "
               "at all %s witnesses, and the split it yields is (1, 1) at all "
               "%d"
               % (ps["cut"]["loci"], ps["cut"]["live_loci"],
                  com(ps["supply"]["witnesses"]), sp["intervals"]),
        "supply": "the canonical carrier is an isomorphism at %d of the %s "
                  "witnesses, against %d whose relation merely carries the "
                  "refined lattice's edge count"
                  % (ps["supply"]["canonical_carrier_isomorphism"],
                     com(ps["supply"]["witnesses"]),
                     ps["supply"][
                         "witnesses_with_the_refined_lattices_edge_count"]),
        "refined_weld": "at the process-supplied completion the refined weld "
                        "returns %s with %d automorphisms and fibers 1/1/1, "
                        "and under paper-04's own declared minimal completion "
                        "the same carrier returns %s with fibers %d/%d/%d"
                        % (dc["fate_process_supplied"],
                           dc["refined_automorphisms"],
                           dc["fate_paper04_minimal"],
                           dc["fibers_paper04_minimal"]["I-SITE-ASSIGNMENT"],
                           dc["fibers_paper04_minimal"]["I-DIRECTION-LABEL"],
                           dc["fibers_paper04_minimal"]["I-ORIENT"]),
        "sig": "the determinant falls from %s to %s, exactly a factor of %s, "
               "and the signature does not move: positive definite at %d of "
               "%d refined sites"
               % (sg["coarse_det"], sg["refined_det"],
                  sg["det_ratio_coarse_over_refined"],
                  sg["sites_positive_definite_refined"], pl["refined_sites"]),
        "ceiling": "the minimum count is %d, so the ceiling is %d and exactly "
                   "one step exists; after the step the minimum count is %d "
                   "and the ceiling is %d; a second step needs a minimum "
                   "count of %d, which the budget law places at R = %d"
                   % (cl["min_count"], cl["ceiling_here"],
                      cl["refined_min_count_after_the_step"],
                      cl["ceiling_after_the_step"],
                      cl["second_step_needs_min_count"],
                      cl["second_step_needs_R"]),
        "dia": "the diagonal buys %d of the %d new places, and with the "
               "diagonal withdrawn %d refined sites lie on no coarse interval "
               "at all"
               % (di["diagonal_new_sites"], pl["new_sites"],
                  di["unreached_without_the_diagonal"]),
    }
    if mut("MUT-CLAIM"):
        out["places"] = out["places"].replace("grows", "does not grow")
    return out


def paper_tables(R):
    """the tables, RENDERED FROM THE RECEIPT: a table cell is a claim."""
    pl, dc, ps = R["new_places"], R["dictionary"], R["process_supply"]
    rows = []
    rows.append("| sites | %d | %d |" % (pl["coarse_sites"],
                                         pl["refined_sites"]))
    rows.append("| intervals | %d | %d |" % (pl["coarse_intervals"],
                                             pl["refined_intervals"]))
    rows.append("| intervals the record determines | %d | %d |"
                % (pl["coarse_intervals"],
                   pl["refined_intervals_determined_by_the_step"]))
    rows.append("| intervals left free | 0 | %d |"
                % pl["refined_intervals_free"])
    for k, v in sorted(ps["supply"]["census_by_class"].items()):
        rows.append("| %s | %d |" % (k, v))
    if mut("MUT-TABLE"):
        rows[0] = rows[0].replace("| 36 |", "| 35 |")
    return rows


def paper_coverage(R, text):
    """#20 + E-22: EVERY numeral -- prose, tables, INLINE CODE SPANS and the
    fenced verdict blocks -- is allow-listed against this run's registered
    numbers, the receipt it publishes and a declared exemption table required
    to fire.  Fenced blocks are gated by MULTISET equality, not containment."""
    allow = set(NUMREG) | receipt_numbers(R)
    for seg in R["verdict"]["segments"]:
        for t in NUMTOK.findall(seg):
            allow.add(t)
            allow.add(t.replace(",", ""))
    exempt = [list(e) for e in NUMERAL_EXEMPTIONS]
    if mut("MUT-EXEMPTION-DEAD"):
        exempt = exempt + [["4242", "a literal that occurs nowhere"]]
    exempt_lits = {e[0] for e in exempt}
    body = text if not mut("MUT-COVERAGE-SCAN") else \
        FENCE.sub("", re.sub(r"`[^`]*`", "", text))
    fenced = [t for blk in FENCE.findall(body) for t in NUMTOK.findall(blk)]
    spans = [t for blk in re.findall(r"`[^`]*`", body)
             for t in NUMTOK.findall(blk)]
    body2 = SECREF.sub(" ", HEADNUM.sub("#### ", body))
    scanned, unbacked, fired = 0, [], Counter()
    for tok in NUMTOK.findall(body2):
        scanned += 1
        if tok in allow or tok.replace(",", "") in allow:
            continue
        if tok in exempt_lits:
            fired[tok] += 1
            continue
        unbacked.append(tok)
    words, word_unbacked = 0, []
    for wd in WORDTOK.findall(canon(body2).lower()):
        if wd not in WORDNUM:
            continue
        words += 1
        if str(WORDNUM[wd]) in allow or wd in exempt_lits:
            continue
        word_unbacked.append(wd)
    if mut("MUT-PAPER-FENCE-MULTISET"):
        seg = R["verdict"]["segments"][0]
        text = text.replace(seg, seg.replace("ACTS", "INERT"), 1)
    want = Counter({canon(seg): FENCE_COPIES
                    for seg in R["verdict"]["segments"]})
    got = Counter(canon(b) for b in FENCE.findall(text))
    return {"numerals_scanned": scanned,
            "unbacked": sorted(set(unbacked)),
            "fenced_blocks_scanned": len(FENCE.findall(body)),
            "fenced_numerals_scanned": len(fenced),
            "inline_span_numerals_scanned": len(spans),
            "word_numerals_scanned": words,
            "word_numerals_unbacked": sorted(set(word_unbacked)),
            "registry_size": len(allow),
            "declared_exemptions": [{"literal": e[0], "reason": e[1],
                                     "occurrences": fired[e[0]]}
                                    for e in exempt],
            "exemptions_that_never_fire": sorted(e[0] for e in exempt
                                                 if not fired[e[0]]),
            "fence_copies_declared": FENCE_COPIES,
            "fenced_block_multiset_matches": got == want,
            "fenced_blocks_expected": sum(want.values()),
            "fenced_blocks_found": sum(got.values())}


def paper_polarity(R, text):
    """the paper must not assert the OPPOSITE of a measured fate."""
    probes = [
        ("the refinement acts", "the refinement is inert at this arena"),
        ("the place-count grows",
         "the place-count is unchanged by the refinement"),
        ("the two laws compose and agree",
         "the two refinement laws conflict at this arena"),
        ("the dictionary survives at the extended carrier",
         "the dictionary does not extend to the refined record"),
        ("exactly one step is possible",
         "a second refinement step is possible at this arena"),
        ("paper-09's kernel is empty here",
         "the renewal kernel speaks on the refined record"),
    ]
    hay = text + (" the place-count is unchanged by the refinement"
                  if mut("MUT-POLARITY") else "")
    viol = [neg for _pos, neg in probes if canon(neg) in canon(hay)]
    return {"probes": [p[0] for p in probes], "violations": viol}


# ===========================================================================
# SECTION 12.  THE COVERAGE LEDGER, THE SEAL AND THE CLOSE
# ===========================================================================

def waiver_ledger():
    """#34: a gate with no declared mutant carries a machine-readable forcing
    that says why it cannot fail, and every waiver is named in the receipt."""
    return {
        "G-PROVENANCE": ("FALSIFIED-BY-A-FLAG",
                         "--break-anchor NAME corrupts any source's expected "
                         "digest and the run dies here"),
        "G-READS-DECLARED": ("STRUCTURAL",
                             "every reader in this file is categorised at the "
                             "call site and this gate holds each category "
                             "against its own declared set, so an "
                             "uncategorised or undeclared read cannot be "
                             "added without failing here"),
        "G-EXACT-ARITHMETIC": ("SELF-SCANNING",
                               "the gate parses this file; a float literal or "
                               "a true division would fail it by "
                               "construction"),
        "G-NO-SUBPROCESS": ("SELF-SCANNING",
                            "same: the gate parses this file's own imports"),
        "G-SLICE-EXIT-FREE": ("SOURCE-FORCED",
                              "the property is evaluated on pinned bytes; "
                              "corrupting it would corrupt a pinned source "
                              "and die at G-PROVENANCE first"),
        "G-I7-READOUT": ("READ-ANCHORED",
                         "the readout sentence is anchored verbatim at V23 "
                         "and the link list at a (path, value) anchor; "
                         "MUT-VERBATIM and MUT-ANCHOR-VALUE falsify both "
                         "anchor classes"),
        "G-DRIVEN-MAXHITS": ("MEASURED-PER-OBJECT",
                             "the predicate is the builder's own maxhits read "
                             "off every driven schedule; MUT-WINDOW removes "
                             "schedules from the same window and dies one "
                             "gate earlier, and no corruption of a v10 "
                             "internal is available to this file"),
        "G-DICTIONARY-CARRIER": ("SHARED-TARGET",
                                 "MUT-CARRIER corrupts the carrier census the "
                                 "same construction feeds and is killed at "
                                 "G-PROCESS-SUPPLY, one gate later; the "
                                 "bijection itself is a construction whose "
                                 "failure would kill G-NEW-PLACES first"),
        "G-REFINED-ADMISSIBLE": ("SHARED-TARGET",
                                 "MUT-ADDITIVITY corrupts the refined counts "
                                 "this gate reads and is killed at "
                                 "G-REFINED-BUILD, one gate earlier"),
        "G-ANCHOR-CONSUMERS": ("FALSIFIED",
                               "MUT-CONSUMER-BINDING names an unregistered "
                               "gate"),
        "G-COVERAGE": ("SELF-REFERENTIAL", "the gate is the coverage ledger"),
        "G-REACHABILITY": ("SELF-REFERENTIAL", "same"),
        "G-MUTANTS-ON-TARGET": ("SELF-REFERENTIAL",
                                "the gate IS the mutant sweep"),
        "G-SWEEP-BOUND": ("DELIVERY-ONLY",
                          "a mutant sub-run declares itself un-swept by "
                          "construction, so no in-process mutant can reach "
                          "its failing branch; the same conjunction is "
                          "re-taken at G-ARTIFACT-INTEGRITY"),
        "G-ARTIFACT-INTEGRITY": ("EXERCISED-IN-RUN",
                                 "the run corrupts a written byte and shows "
                                 "the check detects it before comparing the "
                                 "real artifacts"),
        "G-PAPER-COVERAGE-FINAL": ("AGGREGATE",
                                   "it closes over gates each of which is "
                                   "separately falsified"),
    }


LATE_GATES = ("G-PAPER-COVERAGE-FINAL", "G-SEAL-COMPLETE",
              "G-ARTIFACT-INTEGRITY")
SWEEP_GATE = "G-MUTANTS-ON-TARGET"
LEDGER_GATES = ("G-COVERAGE", "G-REACHABILITY")
CLOSING_GATES = ("G-SWEEP-BOUND",)


def finish(LD, SEAL, R, write=True, swept=False):
    gate_names = sorted({g["gate"] for g in LD.rows} | set(LATE_GATES)
                        | set(LEDGER_GATES) | set(CLOSING_GATES)
                        | {SWEEP_GATE})
    targeted = Counter(m[1] for m in MUTANTS)
    waivers = waiver_ledger()
    uncovered = [g for g in gate_names
                 if not targeted.get(g) and g not in waivers]
    registry_drift = sorted(set(gate_names) ^ set(GATE_REGISTRY))
    R["coverage"] = {
        "gates_evaluated": len(gate_names),
        "gates_with_a_declared_mutant": sum(1 for g in gate_names
                                            if targeted.get(g)),
        "gates_waived": sum(1 for g in gate_names if g in waivers),
        "uncovered": uncovered, "registry_drift": registry_drift,
        "denominator": "the gate count of THIS run, not a hand-kept number",
    }
    R["waiver_ledger"] = {k: {"class": v[0], "forcing": v[1]}
                          for k, v in waivers.items()}
    R["mutants"] = [{"mutant": m[0], "target": m[1], "corrupts": m[3],
                     "description": m[2]} for m in MUTANTS]
    LD.gate("G-COVERAGE",
            "THE COVERAGE LEDGER IS HONEST AND ITS DENOMINATOR IS THIS RUN'S "
            "OWN.  Every gate evaluated anywhere in this run is either "
            "falsified by a declared mutant or waived with a machine-readable "
            "forcing; the declared gate registry and the set actually "
            "evaluated must agree exactly, so a gate removed from the file or "
            "added without a registry row dies here",
            not uncovered and not registry_drift,
            "gates %d, with a mutant %d, waived %d, uncovered %s, registry "
            "drift %s" % (len(gate_names),
                          R["coverage"]["gates_with_a_declared_mutant"],
                          R["coverage"]["gates_waived"], uncovered or "none",
                          registry_drift or "none"))
    SEAL.take("SEAL-COVERAGE", R)
    SEAL.take("SEAL-WAIVERS", R)
    SEAL.take("SEAL-MUTANTS", R)
    unreached = [m[0] for m in MUTANTS
                 if m[1] not in {g["gate"] for g in LD.rows}
                 and m[1] not in LATE_GATES]
    LD.gate("G-REACHABILITY",
            "EVERY FALSIFIER REACHES ITS GATE (#34).  A mutant whose target "
            "gate is never evaluated on the run's own path is dead code "
            "wearing a green badge; every declared target must be a gate this "
            "run actually took",
            not unreached, "mutants %d, targets never evaluated %s"
            % (len(MUTANTS), unreached or "none"))
    R.setdefault("mutant_sweep", [])
    sweep_rows = R["mutant_sweep"]
    sweep_ok = ((not swept) or (len(sweep_rows) == len(MUTANTS)
                                and all(k.get("on_target")
                                        for k in sweep_rows)))
    LD.gate("G-SWEEP-BOUND",
            "THE MUTANT SWEEP'S EXECUTION IS BOUND, NOT MERELY DECLARED.  A "
            "%s run must carry one sweep row per declared mutant (%d), every "
            "row ON TARGET, and the same conjunction is re-taken at the "
            "terminal integrity gate, so the only writer in this file is "
            "downstream of a sweep that actually ran"
            % ("delivery-level" if swept else "mutant sub-", len(MUTANTS)),
            sweep_ok, "delivery-level %s, sweep rows %d of %d, on target %d"
            % (swept, len(sweep_rows), len(MUTANTS),
               sum(1 for k in sweep_rows if k.get("on_target"))))
    SEAL.take("SEAL-MUTANT-SWEEP", R)
    # a SNAPSHOT: the live ledger still gains the closing gates below, and a
    # seal over a list that is still being appended to is not a seal.
    R["gates"] = [dict(g) for g in LD.rows]
    R["totals"] = {"gates": len(LD.rows) + 3, "mutants": len(MUTANTS),
                   "sources": len(SOURCES), "verbatim": len(VERBATIM),
                   "path_value": len(PATH_ANCHORS),
                   "seals": len(SEAL.rows) + 4}
    # the head is the first 40 LINES OF THE TRANSCRIPT AS WRITTEN: a say()
    # whose argument itself contains a newline is two lines on disk.
    R["transcript_head"] = "\n".join(LINES).split("\n")[:40]
    LD.gate("G-PAPER-COVERAGE-FINAL",
            "THE PAPER LAYER CLOSES.  Claim rendering, table rendering, "
            "numeral coverage including fenced blocks and inline spans, "
            "head-verbatim and claim polarity have all been evaluated, and "
            "the receipt carries each of their objects",
            all(k in R for k in ("paper_claims", "paper_tables",
                                 "paper_coverage", "polarity"))
            and R["paper_coverage"]["fenced_block_multiset_matches"],
            "paper objects present %s, fence multiset %s"
            % (all(k in R for k in ("paper_claims", "paper_tables",
                                    "paper_coverage", "polarity")),
               R["paper_coverage"]["fenced_block_multiset_matches"]))
    SEAL.take("SEAL-GATES", R)
    SEAL.take("SEAL-TOTALS", R)
    SEAL.take("SEAL-TRANSCRIPT", R)
    missing, extra = SEAL.totality()
    declared = sorted(set(DECLARED_UNSEALED))
    keys_now = sorted(R)
    sealed_paths = {p for _s, p, _g in SEALED_PATHS}
    unaccounted = [k for k in keys_now
                   if k not in sealed_paths and k not in declared]
    R["seal_manifest"] = {"rows": SEAL.rows,
                          "declared_unsealed": declared,
                          "unaccounted_keys": unaccounted}
    LD.gate("G-SEAL-COMPLETE",
            "THE SEAL MANIFEST IS TOTAL (#119 + #148).  Every published "
            "receipt key is either sealed at the moment its own gate passed "
            "or listed DECLARED-UNSEALED; the manifest is compared against "
            "the DECLARED seal set rather than against the seals that "
            "happened to be taken, so a dropped seal row dies here",
            not missing and not extra and not unaccounted,
            "seals taken %d, declared %d, missing %s, extra %s, unaccounted "
            "receipt keys %s" % (len(SEAL.rows), len(SEALED_PATHS),
                                 missing or "none", extra or "none",
                                 unaccounted or "none"))
    payload = json.dumps(R, indent=1, sort_keys=True, default=str)
    SEAL.close(R, payload)
    R["payload_sha256_12"] = SEAL.payload_sha
    text = "\n".join(LINES) + "\n"
    if not write:
        return payload, text
    tmp_j, tmp_t = OUT_JSON + ".tmp", OUT_TXT + ".tmp"
    try:
        return _write(LD, SEAL, R, payload, text, tmp_j, tmp_t)
    except GateFail:
        for stage in (tmp_j, tmp_t):
            if os.path.exists(stage):
                os.unlink(stage)
        raise


def _write(LD, SEAL, R, payload, text, tmp_j, tmp_t):
    final = json.dumps(R, indent=1, sort_keys=True, default=str)
    with open(tmp_j, "w", encoding="utf-8") as fh:
        fh.write(final + "\n")
    with open(tmp_t, "w", encoding="utf-8") as fh:
        fh.write(text)
    back = json.loads(read_text(tmp_j, "ARTIFACT-STAGED"))
    probe = dict(back)
    probe["counts"] = dict(probe["counts"])
    probe["counts"]["new_sites"] = probe["counts"]["new_sites"] + 1
    probe_caught = bool(SEAL.verify(probe))
    disk_broken = SEAL.verify(back)
    head_ok = (read_text(tmp_t, "ARTIFACT-STAGED").split("\n")[:40]
               == R["transcript_head"])
    ran = {g["gate"] for g in LD.rows}
    late_ok = all(g in ran for g in tuple(LEDGER_GATES) + LATE_GATES[:2]
                  + (SWEEP_GATE,))
    sweep_complete = (len(R.get("mutant_sweep") or []) == len(MUTANTS)
                      and all(k.get("on_target")
                              for k in R.get("mutant_sweep") or []))
    LD.gate("G-ARTIFACT-INTEGRITY",
            "INTEGRITY IS DISK-VS-SEAL, never a re-derivation: the payload is "
            "written from the SEALED object to a staged file, read back FROM "
            "DISK, and every sealed object compared against the digest taken "
            "at the moment its gate passed -- with a deliberately corrupted "
            "probe shown to be detected first, so the check is known to be "
            "live.  The staged bytes are moved into place by os.replace ONLY "
            "after this gate passes, so a run that fails any gate leaves the "
            "delivered artifacts untouched",
            probe_caught and not disk_broken and head_ok and late_ok
            and sweep_complete,
            "corrupted probe detected %s, sealed objects broken on disk %s, "
            "transcript head matches %s, declared-later gates evaluated %s, "
            "sweep complete and on target %s"
            % (probe_caught, disk_broken or "none", head_ok, late_ok,
               sweep_complete))
    os.replace(tmp_j, OUT_JSON)
    os.replace(tmp_t, OUT_TXT)
    return payload, text


# ===========================================================================
# SECTION 13.  THE CLI (#82)
# ===========================================================================

def run_mutant(name, paper_text):
    global MUT, QUIET
    old, MUT, QUIET = MUT, name, True
    del LINES[:]
    try:
        LD, SEAL, R = full_run(paper_text=paper_text)
        finish(LD, SEAL, R, write=False, swept=False)
        out = (False, None)
    except GateFail as exc:
        out = (True, str(exc).split(" :: ")[0])
    except (KeyError, IndexError, TypeError, ValueError, AssertionError) as exc:
        out = (True, "CRASH:%s" % type(exc).__name__)
    finally:
        MUT, QUIET = old, False
    return out


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
    """corrupt one anchor's expected digest in memory, confirm the run dies at
    the anchor gate, and WRITE NOTHING -- proved by digest, never by mtime."""
    global QUIET
    before = artifact_digests()
    QUIET = True
    del LINES[:]
    died, where = False, None
    try:
        LD, SEAL, R = full_run(break_anchor="A-D42B1", do_paper=False)
        finish(LD, SEAL, R, write=False)
    except GateFail as exc:
        died, where = True, str(exc).split(" :: ")[0]
    QUIET = False
    after = artifact_digests()
    print("[SELFTEST] corrupted anchor A-D42B1 :: died=%s at %s :: artifacts "
          "unchanged by sha256=%s %s" % (died, where, before == after,
                                         [d for _p, d in after]))
    if not died or before != after:
        return 2
    return 1


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
        if a == "--mutant":
            if i + 1 >= len(argv):
                raise CliError("--mutant requires NAME")
            if argv[i + 1] not in MUTANT_NAMES:
                raise CliError("unknown mutant %r" % argv[i + 1])
            out["mode"], out["arg"] = a, argv[i + 1]
            i += 2
            continue
        if a == "--break-anchor":
            if i + 1 >= len(argv):
                raise CliError("--break-anchor requires NAME")
            if argv[i + 1] not in SOURCE_IDS:
                raise CliError("unknown anchor %r" % argv[i + 1])
            out["mode"], out["arg"] = a, argv[i + 1]
            i += 2
            continue
        if a == "--verify-paper":
            out["mode"] = a
            if i + 1 < len(argv) and not argv[i + 1].startswith("--"):
                out["arg"] = argv[i + 1]
                i += 2
                continue
            i += 1
            continue
        out["mode"] = a
        i += 1
    return out


def main(argv=None):
    global MUT, QUIET
    argv = list(sys.argv[1:] if argv is None else argv)
    try:
        opt = parse_args(argv)
    except CliError as exc:
        print("[CLI] %s" % exc)
        return 2
    mode, arg = opt["mode"], opt["arg"]
    if mode == "--list-gates":
        for g in GATE_REGISTRY:
            print(g)
        return 0
    if mode == "--list-mutants":
        for m in MUTANTS:
            print("%-28s %-26s corrupts %-38s %s" % (m[0], m[1], m[3], m[2]))
        return 0
    if mode == "--selftest":
        return selftest()
    if mode == "--break-anchor":
        try:
            LD, SEAL, R = full_run(break_anchor=arg, do_paper=False)
            finish(LD, SEAL, R, write=False)
        except GateFail as exc:
            print("[BREAK-ANCHOR %s] died at %s"
                  % (arg, str(exc).split(" :: ")[0]))
            return 1
        print("[BREAK-ANCHOR %s] SURVIVED -- the anchor is not load-bearing"
              % arg)
        return 0
    if mode == "--verify-paper":
        path = arg or os.path.join(REPO, PAPER_REL)
        if not os.path.isfile(path):
            print("[CLI] --verify-paper: %r is not a file" % path)
            return 2
        try:
            LD, SEAL, R = full_run(
                paper_text=read_text(path, "OBJECT-UNDER-TEST"),
                paper_rel=os.path.relpath(path, REPO))
            finish(LD, SEAL, R, write=False)
        except GateFail as exc:
            print("[VERIFY-PAPER] DRIFT :: %s" % exc)
            return 1
        print("[VERIFY-PAPER] clean: %s" % path)
        return 0
    if mode == "--mutant":
        killed, where = run_mutant(
            arg, read_text(os.path.join(REPO, PAPER_REL), "OBJECT-UNDER-TEST"))
        target = [m[1] for m in MUTANTS if m[0] == arg][0]
        print("[MUTANT %s] killed=%s at %s (target %s) -> %s"
              % (arg, killed, where, target,
                 "ON TARGET" if killed and where == target else "OFF TARGET"))
        return 1 if killed else 0
    if mode == "--numbers":
        LD, SEAL, R = full_run(do_paper=False)
        print(json.dumps(R["counts"], indent=1, sort_keys=True))
        for seg in R["verdict"]["segments"]:
            print()
            print(seg)
        return 0
    ptext = read_text(os.path.join(REPO, PAPER_REL), "OBJECT-UNDER-TEST")
    LD, SEAL, R = full_run(paper_text=ptext)
    say("\n[SEC 13] THE MUTANT SWEEP, IN-PROCESS")
    sweep, keep = [], list(LINES)
    for name, gate, _what, _obj in MUTANTS:
        killed, where = run_mutant(name, ptext)
        sweep.append({"mutant": name, "target": gate, "killed": killed,
                      "died_at": where,
                      "on_target": bool(killed and where == gate)})
    del LINES[:]
    LINES.extend(keep)
    for row in sweep:
        say("    %-28s -> %-28s %s"
            % (row["mutant"], row["died_at"],
               "ON TARGET" if row["on_target"] else "OFF TARGET"))
    R["mutant_sweep"] = sweep
    off = [r["mutant"] for r in sweep if not r["on_target"]]
    LD.gate("G-MUTANTS-ON-TARGET",
            "EVERY DECLARED MUTANT IS RUN IN-PROCESS AND DIES AT THE GATE IT "
            "NAMES.  %d mutants, each a real corruption of a measured value "
            "or of the object under test, each required to be killed BY ITS "
            "OWN NAMED GATE rather than by whichever gate fires first"
            % len(MUTANTS),
            not off, "mutants %d, off target %s" % (len(MUTANTS),
                                                    off or "none"))
    payload, text = finish(LD, SEAL, R, write=(mode != "--no-write"),
                           swept=True)
    print("\n[PAYLOAD] sha256-12 %s   gates %d   mutants %d   %s"
          % (R["payload_sha256_12"], len(LD.rows), len(MUTANTS),
             "WROTE %s and %s" % (os.path.basename(OUT_JSON),
                                  os.path.basename(OUT_TXT))
             if mode != "--no-write" else "wrote nothing"))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except GateFail as _exc:
        print("\n[GATE FAILED] %s" % _exc)
        sys.exit(1)
    except FileNotFoundError as _exc:
        print("[CLI] missing source: %s" % _exc)
        sys.exit(1)
