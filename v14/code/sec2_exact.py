#!/usr/bin/env python3.13
# -*- coding: utf-8 -*-
"""
v14 SEC-2 -- THE DYNAMICS OF GLUING.  Instrument for `v14/paper-40-sec2.md`.

QUESTION (pin `v14/note-sec2-pin.md`, sha256-12 bfe5c66be9ec, ledger #332).
SEC (paper-32, #301) glued two driven R = 3 saturating sectors and measured
that the dictionary survives at all 16 combinatorial types, that the seam's
form is a DECLARATION -- six of the ten entries of Sym^2(Q^4) fixed, four
free -- and that the committed grammar ADMITS cross-sector division events
which then kill the dictionary at structure.  The #322 adjudication reversed
the leak wording to SEAM-CONFINED COMPOSITIONALITY and collapsed the 16 types
onto 12 union arenas.  Three measurements are pinned here.

  M1  SEAM SELECTION.  The 4-parameter completion space, censused EXACTLY at
      every seam type the family realises: which completions assign
      admissible counts to the chart's cross directions, which of those are
      positive definite, and whether positivity / price minimisation /
      refinement stability (LOR's own laws) select one.
  M2  THE DICTIONARY EXTENSION.  The declared relaxations of the delivered
      reading legs, enumerated as a five-axis window; the EXHAUSTIVE census
      of the arena's three-actor groups; and, at each extension, whether a
      seam-spanning division event becomes lawful -- with the price.
  M3  THE COMPOSITE PRICE.  SMU's conserved-price frame evaluated on
      composites against lone sectors, in five exact currencies, over all
      45,010 gluings.

WHAT THIS PROGRAM DOES
  S1  PROVENANCE.  Five pinned sources read at run time (byte + path-value +
      verbatim anchors, each bound to a named consumer gate); the four #301
      SEC objects DECLARED at their commit and bound by REPRODUCTION rather
      than by reading, because the worktree copies are under repair -- the
      declaration is checkable with `--verify-sec DIR`.
  S2  EXACTNESS.  An AST scan of this file is a gate: no float, no eval, no
      subprocess or network import, so the run is correct off-tree and with
      no version control present (#91).
  S3  THE ARENA, rebuilt from AG(2,3) and nothing else.
  S4  M1: the seam census, the completion lattice, the three criteria.
  S5  M2: the extension window, the group census, the blindness census.
  S6  M3: the five price currencies.
  S7  THE WALLS.
  S8  The verdict, derived a second time by a comparator that types all four
      templates itself; the paper gates (claim rendering row by row AND
      header by header, numeral coverage including fenced blocks and inline
      spans, fenced blocks by multiset, polarity, spelled numerals); the
      TOTAL seal taken at value-close; the artifacts written through
      os.replace from the sealed payload; the integrity check against the
      gate-time seal.

CLI CONTRACT (the #82 minimum: argv parsed against a whitelist)
---------------------------------------------------------------
    python3.13 v14/code/sec2_exact.py            delivery run (only writer)
    --no-write        run every gate, write nothing
    --numbers         print the measured layer, write nothing
    --selftest        corrupt one anchor of every class, confirm exit 1,
                      WRITE NOTHING; hash-proved
    --mutant NAME     run one declared mutant; artifacts unchanged
    --break-anchor N  break one named anchor; the run must die
    --verify-paper P  run the paper gates against P
    --verify-sec DIR  verify the DECLARED #301 SEC values against copies of
                      the committed objects in DIR
    --list-gates / --list-mutants
Every unknown flag, unknown flag argument, missing flag argument and second
mode flag exits 2.
"""

import ast
import hashlib
import json
import os
import re
import sys
import time
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations, product

# ===========================================================================
# SECTION 0.  DECLARATIONS
# ===========================================================================

SCHEMA = "isp/v14/sec2/1"
UNIT = "SEC-2"
PAPER_NUMBER = 40
PIN_LEDGER = 332

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
SELF_REL = "v14/code/sec2_exact.py"
PAPER_REL = "v14/paper-40-sec2.md"
OUT_REL = "v14/code/sec2_output.txt"
REC_REL = "v14/code/sec2_receipt.json"

# ---- the five sources READ at run time, each at its pinned sha256-12
SOURCES = [
    ("A-PIN", "v14/note-sec2-pin.md", "bfe5c66be9ec",
     "THIS UNIT'S PIN (ledger #332): the three measurements, the outcome "
     "vocabulary, the walls."),
    ("A-ADJ", "v14/note-sec-adjudication.md", "7a82ffe7168a",
     "THE #322 SEC ADJUDICATION: binding context -- SEAM-CONFINED "
     "COMPOSITIONALITY, the 12-arena collapse, the alignment law, FORCED "
     "16 of 16 at the shared rule."),
    ("A-P19", "v14/paper-19-r3-weld.md", "50bb81e67942",
     "PAPER-19 (terminal): the three reading legs this unit relaxes, and "
     "the single-sector weld with fibers 1/1/1."),
    ("A-SMU", "v14/paper-27-smu.md", "6df0db523d32",
     "SMU (terminal): the conserved-price frame -- a declaration supplies a "
     "measured number of independent numbers -- which M3 evaluates on "
     "composites."),
    ("A-LOR", "v14/paper-30-lor.md", "0a08203b7e99",
     "LOR (terminal): the refinement laws and paper-04's ceiling law, which "
     "M1's third selection criterion is read through."),
]

# ---- the #301 SEC objects: DECLARED, NOT READ.  The worktree copies are
# under repair (the pin forbids reading them), and a committed object cannot
# be read off-tree without version control, so every value this unit inherits
# from SEC is carried as a DECLARED (source, key, value) row and bound by
# REPRODUCTION: this unit recomputes it and the gate kills the run on
# mismatch.  `--verify-sec DIR` checks the declaration against copies of the
# committed bytes.
SEC301 = {
    "commit": "88e4a834f532ed2a11b47c74468585eadfcbd54e",
    "ledger": 301,
    "objects": [
        ("v14/paper-32-sec.md", "cfe0825d67b2"),
        ("v14/code/sec_exact.py", "6481a8706503"),
        ("v14/code/sec_output.txt", "e80d2f08a257"),
        ("v14/code/sec_receipt.json", "fdf66d990dbf"),
    ],
}

# (id, receipt path in sec_receipt.json, declared value, consumer gate)
SEC_VALUES = [
    ("V-TOTAL", "gluing_totals.total", 45010, "G-CENSUS"),
    ("V-TYPES", "gluing_totals.types", 16, "G-CENSUS"),
    ("V-DFREE", "gluing_totals.doubled_free_total", 4186, "G-CENSUS"),
    ("V-BYK0", "gluing_totals.by_k.0", 1, "G-CENSUS"),
    ("V-BYK1", "gluing_totals.by_k.1", 81, "G-CENSUS"),
    ("V-BYK2", "gluing_totals.by_k.2", 2592, "G-CENSUS"),
    ("V-BYK3", "gluing_totals.by_k.3", 42336, "G-CENSUS"),
    ("V-DFK2", "gluing_totals.doubled_free_by_k.2", 1134, "G-CENSUS"),
    ("V-DFK3", "gluing_totals.doubled_free_by_k.3", 2970, "G-CENSUS"),
    ("V-STERILE-PAIRS", "sterility.pairs", 54, "G-PRICE-LAWS"),
    ("V-STERILE-CARR", "sterility.carriers", 18, "G-PRICE-LAWS"),
    ("V-SECTOR-AUT", "sterility.sector_aut", 1296, "G-LONE-SECTOR"),
    ("V-K3-AUT", "contrast.k3_aligned_new_structure.aut", 62208, "G-AUT"),
    ("V-K3-CARR", "contrast.k3_aligned_new_structure.carriers", 15, "G-AUT"),
    ("V-SEAM-UNDET",
     "contrast.k3_aligned_new_structure.seam_undetermined_entries", 12,
     "G-PRICE-LAWS"),
    ("V-SEAM-RANK", "seam.0.rank", 6, "G-SEAM-RANK"),
    ("V-SEAM-KER", "seam.0.kernel_dim", 4, "G-SEAM-RANK"),
    ("V-SEAM-UNK", "seam.0.unknowns", 10, "G-SEAM-RANK"),
    ("V-CROSS-NEW", "cross_sector.0.new_pairs", 1, "G-DRIVEN-EVENTS"),
    ("V-CROSS-FOR", "cross_sector.0.foreign_pairs", 1, "G-DRIVEN-EVENTS"),
    ("V-CROSS2-NEW", "cross_sector.2.new_pairs", 2, "G-DRIVEN-EVENTS"),
    ("V-CROSS2-FOR", "cross_sector.2.foreign_pairs", 2, "G-DRIVEN-EVENTS"),
]

# the #322 adjudication's own declared counts, bound by reproduction and by
# the verbatim anchor N-ADJ-ARENAS which quotes the sentence carrying them
ADJ_VALUES = [
    ("V-ARENAS", "the union arenas the 16 types collapse onto", 12,
     "G-ARENA-COLLAPSE"),
    ("V-MIRRORS", "the A-B mirror pairs among them", 4, "G-ARENA-COLLAPSE"),
]

# the SEC witness completion, in SEC's own Sym^2 column order, DECLARED from
# its receipt row seam[0].indefinite_witness and reproduced here
SEC_WITNESS = ("1", "-1/2", "0", "1", "1", "0", "0", "1", "-1/2", "1")
SEC_WITNESS_VECTOR = (2, 1, -1, -2)
SEC_WITNESS_VALUE = "-2"

# the two ADMITTED cross-sector specifications, DECLARED from SEC's receipt
# (group, seed, fate) and re-run here as arena objects
DRIVEN_SPECS = [
    ("SHARED-SEEDED", (("A", (1, 1)), ("B", (1, 1)), ("S", 0)), "ADMITTED"),
    ("A-SEEDED", (("A", (1, 1)), ("B", (1, 1)), ("S", 0)), "REFUSED"),
    ("B-SEEDED-PURE", (("A", (1, 1)), ("B", (1, 1)), ("B", (1, 0))),
     "ADMITTED"),
]

# ---- verbatim (#62) anchors: quote fidelity, each bound to a consumer gate
NEEDLE_FLOOR = 40
VERBATIM = [
    ("N-PIN-COMPLETION", "A-PIN",
     "the 4-parameter completion space at each seam",
     "G-COMPLETION-LATTICE"),
    ("N-PIN-PRICE", "A-PIN",
     "the conserved-price frame (SMU #278) evaluated on composites vs "
     "lone sectors", "G-PRICE-LAWS"),
    ("N-PIN-OUTCOME", "A-PIN",
     "GLUING-EVENT-UNLAWFUL-AT-ALL-DECLARED-EXTENSIONS (the honest wall, "
     "with the extension window named)", "G-LAWFUL"),
    ("N-ADJ-SEAM", "A-ADJ",
     "The licensed finding is SEAM-CONFINED COMPOSITIONALITY: the union "
     "changes geometry only on links both sectors jointly own; no "
     "sector-private link ever moves.", "G-WALL-SEAMCONFINED"),
    ("N-ADJ-ARENAS", "A-ADJ",
     "the 16 types collapse onto 12 union arenas (four A B mirror pairs)",
     "G-ARENA-COLLAPSE"),
    ("N-P19-LEGS", "A-P19",
     "site ACTOR, link the co-division actor pair, count the division "
     "events on that pair inside the declared window", "G-LEGS"),
    ("N-LOR-CEILING", "A-LOR",
     "No record admits more than $\\lfloor\\log_2(\\min n_\\ell)\\rfloor$ "
     "consecutive steps.", "G-REFINEMENT"),
    ("N-SMU-PRICE", "A-SMU",
     "declaring a covariant irreducible dynamics on this carrier still "
     "supplies exactly 207 independent numbers at the anchored reading",
     "G-PRICE-VERDICT"),
]

# ---- the declared mutants, each with the gate it must die at
MUTANTS = [
    ("MUT-SOURCE-DIGEST", "G-SOURCES", "one source's declared digest is "
     "altered, so the read set no longer authenticates"),
    ("MUT-ANCHOR-TEXT", "G-ANCHORS", "one verbatim anchor is perturbed at a "
     "content-bearing token and can no longer be located in its source"),
    ("MUT-EXACT-FLOAT", "G-EXACT", "the AST scan is handed a float constant "
     "from the declared probe, so the exactness gate must fire"),
    ("MUT-CENSUS-DROP", "G-CENSUS", "one gluing is dropped from the k = 3 "
     "enumeration, so the two routes disagree"),
    ("MUT-SEC-VALUE", "G-SEC-VALUES", "one reproduced SEC value is shifted "
     "by one, so the declared inheritance no longer reproduces"),
    ("MUT-ARENA-COLLAPSE", "G-ARENA-COLLAPSE", "the mirror map is replaced "
     "by the identity, so the arena count returns 16 instead of 12"),
    ("MUT-SEAM-TYPE", "G-SEAM-CENSUS", "one shared site's B-side count "
     "vector is transposed, so the seam-type census moves"),
    ("MUT-SEAM-RANK", "G-SEAM-RANK", "one row of the seam system is dropped, "
     "so the rank is 5 and the kernel 5"),
    ("MUT-LATTICE-BOUND", "G-COMPLETION-LATTICE", "the per-entry bound is "
     "narrowed by one, so the derived box cuts the completion family short "
     "and disagrees with its own widened re-run"),
    ("MUT-POSITIVITY", "G-POSITIVITY", "one seam type's positive-definite "
     "set is truncated to a single completion, so positivity would appear to "
     "select one"),
    ("MUT-PRICE-FLAT", "G-PRICE-FLAT", "the two-sided cross budget drops one "
     "sign, so the convention-free price stops being constant"),
    ("MUT-REFINEMENT", "G-REFINEMENT", "the ceiling law is computed on the "
     "maximum count instead of the minimum, so the ceiling reads 1"),
    ("MUT-FISCHER", "G-FISCHER", "the determinant comparison is inverted, so "
     "the direct sum stops being the unique maximiser"),
    ("MUT-SEC-WITNESS", "G-SEC-WITNESS", "the declared witness completion is "
     "corrupted at a cross entry, so SEC's own value is not reproduced and "
     "the inadmissibility it is placed by moves too"),
    ("MUT-CROSSING-CUT", "G-CROSSING-CUT", "the crossing constraint is "
     "dropped, so the cut set is the whole lattice"),
    ("MUT-GROUP-ORBIT", "G-GROUP-CENSUS", "one orbit is split by a corrupted "
     "group action, so the orbit sizes do not sum to the group count"),
    ("MUT-CROSSING-WALL", "G-CROSSING-WALL", "one seam-spanning group's fate "
     "at the delivered target is forged ALIVE"),
    ("MUT-NONCROSS", "G-NON-CROSSING-CONTROL", "the non-crossing control's "
     "fate is forged dead, so the positive control stops firing"),
    ("MUT-GRID-CELL", "G-EXTENSION-GRID", "one grid cell's fate is forged, "
     "so it leaves its pre-declared cell"),
    ("MUT-QUOT-POS", "G-QUOTIENT-POS-COLLAPSE", "one QUOTIENT+POSITIVE fate "
     "is forged, so the derived identity with EMBEDDING breaks"),
    ("MUT-LAWFUL", "G-LAWFUL", "the lawful count is shifted by one, so the "
     "outcome word no longer matches its own census"),
    ("MUT-BLINDNESS", "G-BLINDNESS", "the r = 1 orbit census is forged to "
     "two orbits, so blindness and the detector's own sweep disagree"),
    ("MUT-INVENTORY", "G-INVENTORY", "the map enumeration is capped below "
     "the arena's own automorphism count, so an inventory is incomplete"),
    ("MUT-PRICE-LAW", "G-PRICE-LAWS", "one currency's law is shifted, so the "
     "census reports violations"),
    ("MUT-PRICE-VERDICT", "G-PRICE-VERDICT", "one currency's verdict word is "
     "forged, so it disagrees with its own measured law"),
    ("MUT-LONE", "G-LONE-SECTOR", "the lone sector's declaration price is "
     "forged non-zero"),
    ("MUT-WALL-EXT", "G-WALL-EXTENSION", "the wall's own sentence is "
     "inverted in the text under test, so the paper would carry a lawful "
     "extension without disowning it as the theory"),
    ("MUT-VERDICT", "G-VERDICT-RECON", "one verdict segment is edited after "
     "the builder, so the independent comparator disagrees"),
    ("MUT-PAPER-CLAIM", "G-PAPER-CLAIMS", "one rendered table row is "
     "corrupted, so the paper stops rendering the receipt"),
    ("MUT-PAPER-NUM", "G-PAPER-COVERAGE", "the numeral registry loses a "
     "measured value, so a numeral in the paper is unbacked"),
    ("MUT-LEGS", "G-LEGS", "the legs' quotation is perturbed, so the parent "
     "no longer carries the legs this unit says it relaxes"),
    ("MUT-AUT", "G-AUT", "the automorphism enumeration is capped below the "
     "arena's own order, so the group is not exhausted"),
    ("MUT-DRIVEN", "G-DRIVEN-EVENTS", "one pair is dropped from a "
     "reconstructed conflict group, so the driven counts are not reproduced"),
    ("MUT-SEAM-CONFINED", "G-SEAM-CONFINED-PRICE", "the per-site "
     "declaration price is forged, so the seam surcharge does not sum"),
    ("MUT-WALL-SEAM", "G-WALL-SEAMCONFINED", "the reversed leak sentence is "
     "injected into the text under test"),
    ("MUT-WALL-SCAN", "G-WALL-SCAN", "a forbidden reading term is injected "
     "into the text under test"),
    ("MUT-PAPER-ABSENT", "G-PAPER-PRESENT", "the paper is withheld from a "
     "run that requires it, so the paper leg goes vacuous"),
    ("MUT-UNQUANTISED", "G-UNQUANTISED", "the two exhibited off-lattice "
     "completions collapse onto one, so the witness pair stops being a pair"),
]

LATER_GATES = ("G-VERDICT-RECON", "G-PAPER-PRESENT", "G-PAPER-CLAIMS",
               "G-PAPER-COVERAGE", "G-PAPER-FENCE", "G-PAPER-POLARITY",
               "G-PAPER-SPELLED", "G-SWEEP-EXECUTED", "G-SEAL-COMPLETE",
               "G-DECLARED-LATER", "G-INTEGRITY")
PAPER_REQUIRED = [False]

# gates whose falsifier is a machine-checked forcing rather than a mutant
WAIVERS = {
    "G-SWEEP-EXECUTED": ("forcing: this gate IS the sweep's own binding, and "
                         "a mutant of it would be a mutant of the harness "
                         "that runs mutants; the forcing checked here is "
                         "that the writer is downstream of a sweep whose "
                         "row count equals the declared mutant count"),
    "G-SEAL-COMPLETE": ("forcing: every published receipt key is sealed at "
                        "value-close or declared unsealed; the forcing is "
                        "checked by set equality against the receipt's own "
                        "top-level keys, which no mutant can evade"),
    "G-INTEGRITY": ("forcing: the disk bytes are compared against the "
                    "gate-time seal before promotion, and the comparison is "
                    "evaluated on every delivery run"),
    "G-DECLARED-LATER": ("forcing: the three gates emitted after the "
                         "coverage gate are named in LATER_GATES and their "
                         "presence is checked by set equality at the last "
                         "gate"),
}

SPELLED = {
    "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16,
    "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20,
    "twenty-one": 21, "twenty-two": 22, "twenty-four": 24,
    "twenty-seven": 27,
    "twenty-eight": 28, "thirty": 30, "thirty-one": 31, "thirty-six": 36,
    "forty": 40, "forty-five": 45, "forty-eight": 48, "forty-nine": 49,
    "fifty": 50, "fifty-four": 54, "seventy-two": 72, "one hundred": 100,
    "two hundred": 200, "four hundred": 400,
}

POLARITY = [
    ("P1", "the freedom is irreducible", "the freedom is reducible"),
    ("P2", "the crossing itself is free",
     "the crossing itself is expensive"),
    ("P3", "positivity selects no completion",
     "positivity selects one completion"),
    ("P4", "the record's own price is exactly additive",
     "the record's own price is not additive"),
    ("P5", "every seam-spanning group is dead at the delivered target",
     "some seam-spanning group is alive at the delivered target"),
]

# the reading this unit does NOT take (#322's wall vocabulary and the pin's)
FORBIDDEN_TERMS = (
    "spacetime", "universe", "cosmolog", "expansion of space", "new places",
    "wormhole", "the world grows", "big bang", "inflation",
)

EXIT_OK, EXIT_FAIL, EXIT_USAGE = 0, 1, 2


class GateFail(Exception):
    pass


ACTIVE_MUTANT = [None]
BROKEN_ANCHOR = [None]


def mut(name):
    return ACTIVE_MUTANT[0] == name


def pick(name, normal, corrupted):
    return corrupted if mut(name) else normal


# ===========================================================================
# SECTION 1.  THE LEDGER, THE SEAL, THE READ LOG
# ===========================================================================

OUTBUF = []


def say(s=""):
    OUTBUF.append(s)
    print(s)


def digest(value):
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, default=str).encode()).hexdigest()


class Ledger:
    def __init__(self):
        self.rows = []
        self.chain = hashlib.sha256(SCHEMA.encode()).hexdigest()

    def gate(self, name, ok, statement, evidence):
        row = {"gate": name, "ok": bool(ok), "statement": statement,
               "evidence": evidence}
        row["digest"] = digest(row)[:16]
        self.chain = hashlib.sha256(
            (self.chain + row["digest"]).encode()).hexdigest()
        row["chain"] = self.chain[:16]
        self.rows.append(row)
        if not ok:
            raise GateFail("%s: %s | evidence=%s"
                          % (name, statement, json.dumps(evidence,
                                                         default=str)[:400]))
        return True

    def names(self):
        return [r["gate"] for r in self.rows]


class Seal:
    def __init__(self):
        self.seals = {}
        self.unsealed = {}

    def seal(self, key, value):
        self.seals[key] = digest(value)
        return value

    def declare_unsealed(self, key, why):
        self.unsealed[key] = why

    def manifest(self):
        return {"sealed": dict(self.seals), "unsealed": dict(self.unsealed),
                "n_sealed": len(self.seals), "n_unsealed": len(self.unsealed)}


READLOG = []


def read_bytes(rel):
    path = os.path.join(ROOT, rel)
    with open(path, "rb") as fh:
        data = fh.read()
    READLOG.append(rel)
    return data


def sha12(data):
    return hashlib.sha256(data).hexdigest()[:12]


# ---- #125 normalisation: whitespace, ascii folding, markdown prefixes
def mdstrip(s):
    out = []
    for ln in s.split("\n"):
        t = ln.lstrip()
        while t[:1] in (">", "-", "*", "+"):
            t = t[1:].lstrip()
        t = re.sub(r"^\d+[.)]\s+", "", t)
        out.append(t)
    return "\n".join(out)


def ascii_fold(s):
    return "".join(c if ord(c) < 128 else " " for c in s)


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def canon(s):
    return norm(ascii_fold(mdstrip(s.replace("*", "").replace("`", ""))))


def locate(hay, needle):
    return canon(hay).count(canon(needle))


def perturb(needle):
    """a content-bearing perturbation of any needle: the longest token is
    broken in the middle.  A perturbation that edits a word the needle may
    not contain is not a falsifier, it is a coin toss."""
    toks = needle.split()
    i = max(range(len(toks)), key=lambda j: (len(toks[j]), -j))
    t = toks[i]
    toks[i] = t[:len(t) // 2] + "X" + t[len(t) // 2:]
    return " ".join(toks)


# ===========================================================================
# SECTION 2.  EXACT ARITHMETIC ON THE LATTICE AND ON Q
# ===========================================================================

SITES = tuple((i, j) for i in range(3) for j in range(3))
LINKS = ((1, 0), (0, 1), (1, 1))       # I7's three declared link directions


def zadd(a, b):
    return ((a[0] + b[0]) % 3, (a[1] + b[1]) % 3)


def zneg(a):
    return ((-a[0]) % 3, (-a[1]) % 3)


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


CLASS_DIR = {"ROW": (0, 1), "COL": (1, 0), "DIA": (1, 1), "ANT": (1, 2)}
CLASSES = {k: parallel_class(v) for k, v in CLASS_DIR.items()}
ARRANGEMENT = ("ROW", "COL", "DIA")     # paper-19's own driven arrangement
PART_OF = {}
for _i, _L in enumerate(CLASSES["ANT"]):
    for _s in _L:
        PART_OF[_s] = _i

# the 27 site pairs one sector realises: the pairs sharing a ROW, COL or DIA
SECTOR_PAIRS = tuple(sorted(
    {tuple(sorted(p)) for c in ARRANGEMENT for g in CLASSES[c]
     for p in combinations(g, 2)}))


def det(A):
    n = len(A)
    if n == 1:
        return A[0][0]
    if n == 2:
        return A[0][0] * A[1][1] - A[0][1] * A[1][0]
    tot = 0 * A[0][0]
    for c in range(n):
        sub = [[A[i][j] for j in range(n) if j != c] for i in range(1, n)]
        tot += ((-1) ** c) * A[0][c] * det(sub)
    return tot


def minors(M):
    return [det([[M[i][j] for j in range(k)] for i in range(k)])
            for k in range(1, len(M) + 1)]


def posdef(M):
    """exact Sylvester.  M is carried DOUBLED as an integer matrix, so the
    k-th leading minor of the form is the k-th minor of M divided by 2^k and
    the signs are the same; the whole criterion runs in integers."""
    return all(m > 0 for m in minors(M))


def q_of(n):
    """I7's readout: n_l is the squared length of the link direction, and the
    off-diagonal is recovered by polarisation."""
    n1, n2, n3 = n
    return Fraction(n1), Fraction(n2), Fraction(n3 - n1 - n2, 2)


def sym_index(d):
    idx = {}
    for i in range(d):
        for j in range(i, d):
            idx[(i, j)] = len(idx)
    return idx


IDX4 = sym_index(4)


def quad_row(vec, idx, d):
    row = [Fraction(0)] * len(idx)
    for i in range(d):
        for j in range(i, d):
            row[idx[(i, j)]] += Fraction(vec[i] * vec[j]) * (1 if i == j
                                                             else 2)
    return row


def rref(rows, ncol):
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


AV = ([1, 0, 0, 0], [0, 1, 0, 0], [1, 1, 0, 0])
BV = ([0, 0, 1, 0], [0, 0, 0, 1], [0, 0, 1, 1])


def seam_rows(cross=()):
    """the seam's exact coefficient matrix in the DIRECT-SUM chart: sector A
    spans coordinates 0,1 and sector B spans 2,3, so the six declared link
    directions are a1, a2, a1+a2, b1, b2, b1+b2 and the unknown is the whole
    of Sym^2(Q^4).  The RHS never enters, which is why the rank is a property
    of the chart and not of the record."""
    rows = [quad_row(v, IDX4, 4) for v in AV]
    rows += [quad_row(v, IDX4, 4) for v in BV]
    if mut("MUT-SEAM-RANK"):
        rows = rows[:-1]
    for (i, j) in cross:
        rows.append(quad_row([BV[j][t] - AV[i][t] for t in range(4)],
                             IDX4, 4))
    return rows


def gram(nA, nB, U):
    """the 4x4 Gram matrix of the completion whose cross block is C = U/2,
    carried DOUBLED so that every entry is an integer: 2q_11 = 2n_1,
    2q_12 = n_3 - n_1 - n_2 and 2q(a_i, b_j) = U_ij.  Every predicate this
    unit takes on the form -- Sylvester positivity, determinant order -- is
    invariant under the doubling, and the exact rational form is recovered by
    dividing the k-th minor by 2^k."""
    M = [[0] * 4 for _ in range(4)]
    M[0][0], M[1][1] = 2 * nA[0], 2 * nA[1]
    M[0][1] = M[1][0] = nA[2] - nA[0] - nA[1]
    M[2][2], M[3][3] = 2 * nB[0], 2 * nB[1]
    M[2][3] = M[3][2] = nB[2] - nB[0] - nB[1]
    for i in range(2):
        for j in range(2):
            M[i][2 + j] = M[2 + j][i] = U[i][j]
    return M


def form_det(M2):
    """the exact determinant of the FORM whose doubled Gram is M2."""
    return Fraction(det(M2), 2 ** len(M2))


def uext(U):
    """U on the 3x3 direction index set, with a3 = a1 + a2, b3 = b1 + b2."""
    E = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(2):
        for j in range(2):
            E[i][j] = U[i][j]
    for i in range(2):
        E[i][2] = U[i][0] + U[i][1]
    for j in range(2):
        E[2][j] = U[0][j] + U[1][j]
    E[2][2] = U[0][0] + U[0][1] + U[1][0] + U[1][1]
    return E


def cross_counts(nA, nB, U):
    """the eighteen counts the completion assigns to the chart's cross
    directions: the pair {x + s.a_i, x + t.b_j} has direction t.b_j - s.a_i
    and count nA_i + nB_j - st.U_ij, and both signs occur because x - a_i is
    a declared neighbour of x exactly as x + a_i is."""
    E = uext(U)
    out = {}
    for i in range(3):
        for j in range(3):
            for s in (1, -1):
                out[(i, j, s)] = nA[i] + nB[j] - s * E[i][j]
    return out


def lattice_admissible(nA, nB, U):
    return all(v >= 1 for v in cross_counts(nA, nB, U).values())


def completion_lattice(nA, nB, slack=0):
    """EVERY completion assigning admissible counts to every cross direction.
    The enumeration box is DERIVED, not chosen: the (i,j) cross count itself
    forces |U_ij| <= nA_i + nB_j - 1.  That the box is not binding is not
    asserted -- the census is run again with the box widened by one and the
    two are required to return the same set, so a box that had cut the family
    short would show as a disagreement."""
    bound = [[nA[i] + nB[j] - 1 + slack for j in range(2)] for i in range(2)]
    if mut("MUT-LATTICE-BOUND"):
        bound = [[b - 1 for b in row] for row in bound]
    out = []
    for u00 in range(-bound[0][0], bound[0][0] + 1):
        for u01 in range(-bound[0][1], bound[0][1] + 1):
            for u10 in range(-bound[1][0], bound[1][0] + 1):
                for u11 in range(-bound[1][1], bound[1][1] + 1):
                    U = [[u00, u01], [u10, u11]]
                    if lattice_admissible(nA, nB, U):
                        out.append((u00, u01, u10, u11))
    return out, bound


# ===========================================================================
# SECTION 3.  THE ARENA: GLUINGS, TYPES, UNION RELATIONS
# ===========================================================================

def gluing_maps(glue):
    """the two site->actor namings the gluing induces.  Shared actors carry
    the neutral name ('S', i) so neither sector's naming is privileged."""
    amap, bmap = {}, {}
    for i, (sa, sb) in enumerate(glue):
        amap[sa] = ("S", i)
        bmap[sb] = ("S", i)
    for s in SITES:
        amap.setdefault(s, ("A", s))
        bmap.setdefault(s, ("B", s))
    actors = sorted(set(amap.values()) | set(bmap.values()), key=repr)
    return actors, amap, bmap


def union_rel(glue):
    """the union's co-division relation, built from the two sectors' own
    realised pairs and the identification alone."""
    actors, amap, bmap = gluing_maps(glue)
    rel = Counter()
    for mp in (amap, bmap):
        for (u, v) in SECTOR_PAIRS:
            rel[frozenset((mp[u], mp[v]))] += 1
    return actors, dict(rel), amap, bmap


def union_counts(glue):
    """the same relation with ordered-tuple keys: the census pass runs over
    45,010 gluings, and a tuple key is the same object more cheaply."""
    actors, amap, bmap = gluing_maps(glue)
    rel = {}
    for mp in (amap, bmap):
        for (u, v) in SECTOR_PAIRS:
            a, b = mp[u], mp[v]
            key = (a, b) if repr(a) <= repr(b) else (b, a)
            rel[key] = rel.get(key, 0) + 1
    return actors, rel, amap, bmap


def cell_key(mp, x, l):
    a, b = mp[x], mp[zadd(x, l)]
    return (a, b) if repr(a) <= repr(b) else (b, a)


def part_profile(glue):
    M = Counter()
    for sa, sb in glue:
        M[(PART_OF[sa], PART_OF[sb])] += 1
    return tuple(sorted(M.items()))


def canon_profile(prof, transpose=False):
    M = dict(prof)
    if transpose:
        M = {(c, r): v for (r, c), v in M.items()}
    rows = sorted({r for r, _c in M})
    cols = sorted({c for _r, c in M})
    best = None
    for rp in permutations(rows):
        for cp in permutations(cols):
            key = tuple(sorted((rp.index(r), cp.index(c), v)
                               for (r, c), v in M.items()))
            if best is None or key < best:
                best = key
    return best


TYPE_CACHE = {}


def gluing_type(glue):
    prof = part_profile(glue)
    got = TYPE_CACHE.get(prof)
    if got is None:
        got = canon_profile(prof)
        TYPE_CACHE[prof] = got
    return got


def all_gluings(k):
    out = []
    for SA in combinations(SITES, k):
        for SB in permutations(SITES, k):
            out.append(tuple(zip(SA, SB)))
    return out


def doubled_free(glue):
    """the alignment criterion, per PAIR of shared actors: no shared pair may
    be adjacent in BOTH sectors, and adjacency in a sector is exactly
    'different tripartite parts'."""
    for (sa, sb), (ta, tb) in combinations(glue, 2):
        if PART_OF[sa] != PART_OF[ta] and PART_OF[sb] != PART_OF[tb]:
            return False
    return True


# ===========================================================================
# SECTION 4.  THE GRAPH MACHINERY (this unit's own, no shared code)
# ===========================================================================

def build(nodes, edges):
    idx = {a: i for i, a in enumerate(nodes)}
    adj = [set() for _ in nodes]
    for e in edges:
        u, v = tuple(e)
        adj[idx[u]].add(idx[v])
        adj[idx[v]].add(idx[u])
    return len(nodes), adj, idx


def refine(n, adj, col):
    col = list(col)
    while True:
        sig = [(col[v], tuple(sorted(col[u] for u in adj[v])))
               for v in range(n)]
        o = {s: i for i, s in enumerate(sorted(set(sig)))}
        new = [o[s] for s in sig]
        if new == col:
            return col
        col = new


def search(n1, a1, n2, a2, mode, limit):
    """mode 'iso': the edge sets correspond exactly.  mode 'into': every edge
    of graph 1 lands on an edge of graph 2.  mode 'into-cover': the same, and
    every edge of graph 2 is reached -- the count leg's positivity condition
    carried INTO the search, by a procedure that shares no branch with the
    isomorphism search it is later compared against.  Exhaustive backtracking
    with equitable-refinement (iso) or degree (into) candidate pruning."""
    if n1 != n2:
        return []
    e1 = sum(len(s) for s in a1)
    e2 = sum(len(s) for s in a2)
    if mode.startswith("into") and e1 > e2:
        return []
    if mode == "into-cover" and e1 < e2:
        return []
    if mode == "iso":
        if e1 != e2:
            return []
        c1 = refine(n1, a1, [0] * n1)
        c2 = refine(n2, a2, [0] * n2)
        if sorted(Counter(c1).values()) != sorted(Counter(c2).values()):
            return []
        cand = [[x for x in range(n2) if c2[x] == c1[u]] for u in range(n1)]
    else:
        cand = [[x for x in range(n2) if len(a2[x]) >= len(a1[u])]
                for u in range(n1)]
    seq, placed, rem = [], set(), list(range(n1))
    while rem:
        best = None
        for v in rem:
            key = (len(a1[v] & placed), len(a1[v]), -v)
            if best is None or key > best[0]:
                best = (key, v)
        seq.append(best[1])
        placed.add(best[1])
        rem.remove(best[1])
    out, phi, used = [], {}, set()

    def covers(m):
        img = set()
        for u in range(n1):
            for w in a1[u]:
                img.add((min(m[u], m[w]), max(m[u], m[w])))
        for x in range(n2):
            for y in a2[x]:
                if (min(x, y), max(x, y)) not in img:
                    return False
        return True

    def bt(k):
        if len(out) >= limit:
            return
        if k == len(seq):
            m = dict(phi)
            if mode != "into-cover" or covers(m):
                out.append(m)
            return
        u = seq[k]
        for x in cand[u]:
            if x in used:
                continue
            ok = True
            for w, y in phi.items():
                if mode == "iso":
                    if (w in a1[u]) != (y in a2[x]):
                        ok = False
                        break
                else:
                    if (w in a1[u]) and (y not in a2[x]):
                        ok = False
                        break
            if ok:
                phi[u] = x
                used.add(x)
                bt(k + 1)
                used.discard(x)
                del phi[u]
    bt(0)
    return out


# ===========================================================================
# SECTION 5.  THE TARGET AND THE DETECTOR, RE-POSED AT THE EXTENSIONS
# ===========================================================================

def amalgam(glue, cross=(), name="T"):
    """T(k, gamma) and its declared cross extension: two copies of I7's
    lattice glued along the k shared sites, plus the declared cross links.
    The lattice part never sees the record."""
    actors, amap, bmap = gluing_maps(glue)
    inc, cells = set(), []
    for chart, mp in (("A", amap), ("B", bmap)):
        for x in SITES:
            for l in LINKS:
                e = frozenset((mp[x], mp[zadd(x, l)]))
                inc.add(e)
                cells.append((chart, x, l, e))
    for e in sorted(cross, key=repr):
        inc.add(e)
        cells.append(("X", None, None, e))
    return {"name": name, "nodes": actors, "inc": inc, "cells": cells,
            "charts": {"A": amap, "B": bmap}, "cross": sorted(cross,
                                                              key=repr)}


PERMS3 = list(permutations(range(3)))
IDPERM = {"A": (0, 1, 2), "B": (0, 1, 2)}
NOFLIP = {"A": False, "B": False}


def count_field(target, rel, phi, sperm=IDPERM, orient=NOFLIP):
    """the induced count field on the target's OWN cells.  `phi` maps a site
    object to a target node; `sperm` permutes a chart's declared link labels
    and `orient` flips its direction convention.  A cross cell carries no
    direction label, so the relabelling acts on the lattice cells alone."""
    inv = {v: k for k, v in phi.items()}
    out = {}
    for (chart, x, l, e) in target["cells"]:
        if chart == "X":
            u, v = [inv[t] for t in e]
            out[("X", tuple(sorted(e, key=repr)))] = \
                rel.get(frozenset((u, v)), 0)
            continue
        li = LINKS.index(l)
        l2 = LINKS[sperm[chart][li]]
        step = zneg(l2) if orient[chart] else l2
        mp = target["charts"][chart]
        u, v = inv[mp[x]], inv[mp[zadd(x, step)]]
        out[(chart, x, l)] = rel.get(frozenset((u, v)), 0)
    return out


def fkey(f):
    return tuple(sorted((repr(k), v) for k, v in f.items()))


def maps_for(actors, rel, target, reading, limit, mode=None):
    n1, a1, i1 = build(actors, rel.keys())
    n2, a2, i2 = build(target["nodes"], target["inc"])
    if reading == "EMBEDDING":
        res = search(n1, a1, n2, a2, mode or "iso", limit)
        return [{actors[u]: target["nodes"][x] for u, x in m.items()}
                for m in res]
    if reading == "QUOTIENT":
        res = search(n1, a1, n2, a2, mode or "into", limit)
        return [{actors[u]: target["nodes"][x] for u, x in m.items()}
                for m in res]
    res = search(n2, a2, n1, a1, mode or "into", limit)
    return [{actors[x]: target["nodes"][u] for u, x in m.items()}
            for m in res]


def detect(actors, rel, target, reading, countleg):
    """ONE CENSUS ROW.  EMBEDDING: the realised relation IS the target's
    incidence.  QUOTIENT: it sits inside.  LAX: the target's incidence sits
    inside the realised relation -- the relaxation of the reading leg, at
    which the record may carry pairs the geometry does not."""
    if len(actors) != len(target["nodes"]):
        return {"fate": "ARITY-DEAD", "maps": 0}
    if reading == "QUOTIENT" and countleg == "POSITIVE":
        # the positive-count leg is a covering condition on the target's own
        # cells, and it is carried INTO the search rather than tested on one
        # arbitrary map: a fate read off the first map found would be a
        # property of the search order, not of the dictionary.
        ms = maps_for(actors, rel, target, reading, 1, mode="into-cover")
        if ms:
            f = count_field(target, rel, ms[0])
            return {"fate": "ALIVE", "maps": 1, "min": min(f.values()),
                    "values": sorted(set(f.values()))}
        if maps_for(actors, rel, target, reading, 1):
            return {"fate": "COUNT-DEAD", "maps": 1, "min": 0}
        return {"fate": "STRUCT-DEAD", "maps": 0}
    ms = maps_for(actors, rel, target, reading, 1)
    if not ms:
        return {"fate": "STRUCT-DEAD", "maps": 0}
    f = count_field(target, rel, ms[0])
    mn = min(f.values())
    if countleg == "POSITIVE" and mn < 1:
        return {"fate": "COUNT-DEAD", "maps": 1, "min": mn,
                "zero_cells": sum(1 for v in f.values() if v < 1)}
    if countleg == "NON-NEGATIVE" and mn < 0:
        return {"fate": "COUNT-DEAD", "maps": 1, "min": mn}
    return {"fate": "ALIVE", "maps": 1, "min": mn,
            "values": sorted(set(f.values()))}


MAP_CAP = 200000


def inventory(actors, rel, target):
    """the RSQ choice inventory at the bare carrier: I-SITE-ASSIGNMENT is the
    number of DISTINCT count fields the admissible maps produce;
    I-DIRECTION-LABEL and I-ORIENT are taken per sector, because the union
    carries two charts and a permutation mixing them would not be a
    relabelling of either."""
    cap = 1 if mut("MUT-INVENTORY") else MAP_CAP
    ms = maps_for(actors, rel, target, "EMBEDDING", cap)
    if not ms:
        return None
    complete = len(ms) < cap
    # the field on the target's cells is a function of the induced count on
    # the target's EDGES and of nothing else -- two cells sharing an edge
    # carry the same count -- so the distinct fields are counted by the
    # distinct edge-labellings, which is the same measurement done cheaply.
    edges = sorted(target["inc"], key=repr)
    eidx = {e: i for i, e in enumerate(edges)}
    keys = set()
    for m in ms:
        inv = {v: k for k, v in m.items()}
        keys.add(tuple(sorted(
            (eidx[e], rel.get(frozenset(inv[t] for t in e), 0))
            for e in edges
            if rel.get(frozenset(inv[t] for t in e), 0) != 1)))
    phi = ms[0]
    labs = {fkey(count_field(target, rel, phi, {"A": pa, "B": pb}, NOFLIP))
            for pa in PERMS3 for pb in PERMS3}
    oris = {fkey(count_field(target, rel, phi, IDPERM,
                             {"A": oa, "B": ob}))
            for oa in (False, True) for ob in (False, True)}
    inv = {"I-SITE-ASSIGNMENT": len(keys), "I-DIRECTION-LABEL": len(labs),
           "I-ORIENT": len(oris)}
    free = sorted(k for k, v in inv.items() if v > 1)
    return {"maps": len(ms), "complete": complete, "inventory": inv,
            "free_items": free,
            "fate": "MOTIVATED" if not free else "UNMOTIVATED"}


# ===========================================================================
# SECTION 6.  THE RUN
# ===========================================================================

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
        elif isinstance(v, str):
            NUMREG.add(v)
    return vals[0] if vals else None


def full_run(paper_text=None, paper_rel=PAPER_REL):
    t0 = time.time()
    LD, SEAL, R = Ledger(), Seal(), {}
    NUMREG.clear()
    del READLOG[:]
    R["schema"] = SCHEMA
    R["schema_version"] = 1
    R["unit"] = UNIT
    R["pin"] = {"path": "v14/note-sec2-pin.md", "ledger": PIN_LEDGER,
                "paper_number": PAPER_NUMBER}

    # ---- S1  PROVENANCE ---------------------------------------------------
    texts, prov = {}, []
    for (sid, rel, declared, why) in SOURCES:
        data = read_bytes(rel)
        got = sha12(data)
        if mut("MUT-SOURCE-DIGEST") and sid == "A-LOR":
            got = "0" * 12
        texts[sid] = data.decode("utf-8", "replace")
        prov.append({"id": sid, "path": rel, "declared": declared,
                     "sha256_12": got, "ok": got == declared, "why": why})
    LD.gate("G-SOURCES",
            all(p["ok"] for p in prov) and sorted(READLOG) ==
            sorted(s[1] for s in SOURCES),
            "every source this run reads is authenticated at its declared "
            "sha256-12 and the read set recorded at the actual I/O layer is "
            "exactly the declared set, so a stray read fails the gate",
            {"n": len(prov), "read_log": sorted(set(READLOG)),
             "bad": [p["id"] for p in prov if not p["ok"]]})
    R["provenance"] = SEAL.seal("provenance", prov)
    R["cited_not_read"] = SEAL.seal("cited_not_read", {
        "why": "the #301 SEC objects are DECLARED at their commit and bound "
               "by reproduction, never read: the worktree copies are under "
               "repair (the pin forbids reading them) and a committed object "
               "cannot be read off-tree without version control",
        "commit": SEC301["commit"], "ledger": SEC301["ledger"],
        "values_declared": len(SEC_VALUES),
        "objects": [{"path": p, "sha256_12": s}
                    for p, s in SEC301["objects"]]})

    anch = []
    for (nid, sid, needle, consumer) in VERBATIM:
        nd = needle
        if mut("MUT-ANCHOR-TEXT") and nid == "N-ADJ-SEAM":
            nd = needle.replace("only", "never")
        if BROKEN_ANCHOR[0] == nid:
            nd = perturb(needle)
        hits = locate(texts[sid], nd)
        ok = hits == 1 and len(canon(nd)) >= NEEDLE_FLOOR
        anch.append({"id": nid, "source": sid, "consumer": consumer,
                     "hits": hits, "chars": len(canon(nd)), "ok": ok})
    LD.gate("G-ANCHORS",
            all(a["ok"] for a in anch),
            "every verbatim anchor is located exactly once in its pinned "
            "source under the #125 normaliser, clears the declared "
            "character floor, and names the gate that consumes it -- so a "
            "misquotation of a parent dies on the delivery run",
            {"n": len(anch), "floor": NEEDLE_FLOOR,
             "bad": [a["id"] for a in anch if not a["ok"]],
             "consumers": sorted({a["consumer"] for a in anch})})
    R["anchors"] = SEAL.seal("anchors", anch)

    # ---- S2  EXACTNESS ----------------------------------------------------
    selftext = read_bytes(SELF_REL).decode()
    READLOG.pop()
    tree = ast.parse(selftext)
    floats = [n for n in ast.walk(tree)
              if isinstance(n, ast.Constant) and isinstance(n.value, float)]
    if mut("MUT-EXACT-FLOAT"):
        floats = floats + ["injected"]
    banned = [n for n in ast.walk(tree)
              if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)
              and n.func.id in ("float", "eval", "exec")]
    imports = sorted({a.name.split(".")[0] for n in ast.walk(tree)
                      if isinstance(n, ast.Import) for a in n.names}
                     | {n.module.split(".")[0] for n in ast.walk(tree)
                        if isinstance(n, ast.ImportFrom) and n.module})
    subproc = [m for m in ("subprocess", "shutil", "socket", "urllib",
                           "requests") if m in imports]
    LD.gate("G-EXACT",
            not floats and not banned and not subproc,
            "an AST scan of this file finds no float constant, no call to "
            "float(), eval() or exec(), and no subprocess or network import: "
            "all arithmetic is Python ints and fractions.Fraction and the "
            "run is correct off-tree and with no version control present",
            {"floats": len(floats), "banned_calls": len(banned),
             "imports": imports, "subprocess_modules": subproc})

    # ---- the delivered legs, bound to their anchor -----------------------
    LEGS = ("ACTOR->SITE", "CO-DIVISION-ACTOR-PAIR->LINK",
            "DIVISION-COUNT->n_l(x)")
    legs_probe = pick("MUT-LEGS",
                      "site ACTOR, link the co-division actor pair, count "
                      "the division events on that pair",
                      "site ACTOR, link the co-division actor triple, count "
                      "the division events on that pair")
    legs_quoted = canon(legs_probe) in canon(texts["A-P19"])
    LD.gate("G-LEGS", legs_quoted and len(LEGS) == 3,
            "the three reading legs this unit relaxes are the ones paper-19 "
            "declares in its own bytes -- site from the actor, link from the "
            "co-division actor pair, count from the division events on that "
            "pair -- and the relaxation window below is built on those three "
            "and on the target they read into",
            {"legs": list(LEGS), "quoted_in_parent": legs_quoted})

    DECL = {k: v for (_i, k, v, _c) in SEC_VALUES}
    ADECL = {i: v for (i, _w, v, _c) in ADJ_VALUES}

    # ---- S3  THE GLUING CENSUS AND THE PRICE CURRENCIES -------------------
    census = {}
    typerep = {}
    typecount = Counter()
    dfree_k = Counter()
    seamtypes = Counter()
    price_bad = []
    seam_route_bad = []
    kpop = Counter()
    dbl_pop = Counter()
    total = 0
    for k in (0, 1, 2, 3):
        GL = all_gluings(k)
        if mut("MUT-CENSUS-DROP") and k == 3:
            GL = GL[:-1]
        total += len(GL)
        for gl in GL:
            t = (k,) + gluing_type(gl)
            typecount[t] += 1
            typerep.setdefault(t, gl)
            if doubled_free(gl):
                dfree_k[k] += 1
            actors, rel, amap, bmap = union_counts(gl)
            d = sum(1 for v in rel.values() if v > 1)
            dbl_pop[(k, d)] += 1
            # the five currencies
            p_record = sum(rel.values())
            p_budget = 0
            cells = 0
            for mp in (amap, bmap):
                for x in SITES:
                    for l in LINKS:
                        cells += 1
                        p_budget += rel[cell_key(mp, x, l)]
            p_decl = 4 * k
            p_carrier = len(actors)
            p_links = len(rel)
            if mut("MUT-PRICE-LAW") and k == 2:
                p_budget += 1
            if not (p_record == 54 and p_budget == 54 + 2 * d
                    and cells == 54 and p_carrier == 18 - k
                    and p_links == 54 - d and p_decl == 4 * k):
                price_bad.append(str(gl))
            # the seam types at every shared site
            for i, (sa, sb) in enumerate(gl):
                nA = tuple(rel[cell_key(amap, sa, l)] for l in LINKS)
                nB = tuple(rel[cell_key(bmap, sb, l)] for l in LINKS)
                if mut("MUT-SEAM-TYPE") and k == 1:
                    nB = (nB[0] + 1,) + nB[1:]
                # SECOND ROUTE, from the part structure alone: an A-link of a
                # shared site is doubled exactly when its A-neighbour is also
                # shared AND the two B-sites those shared actors carry lie in
                # different tripartite parts, which is what makes the B-pair
                # realised.  It never touches the relation dictionary.
                sh_a = {t[0]: t[1] for t in gl}
                sh_b = {t[1]: t[0] for t in gl}
                nA2 = tuple(2 if (zadd(sa, l) in sh_a
                                  and PART_OF[sh_a[zadd(sa, l)]]
                                  != PART_OF[sb]) else 1 for l in LINKS)
                nB2 = tuple(2 if (zadd(sb, l) in sh_b
                                  and PART_OF[sh_b[zadd(sb, l)]]
                                  != PART_OF[sa]) else 1 for l in LINKS)
                if (nA, nB) != (nA2, nB2):
                    seam_route_bad.append(str((gl, i)))
                seamtypes[(nA, nB)] += 1
            kpop[k] += 1

    def closed(k):
        c, p, f = 1, 1, 1
        for i in range(k):
            c = c * (9 - i)
            p = p * (9 - i)
        for i in range(1, k + 1):
            f = f * i
        return (c // f) * p

    closed_total = sum(closed(k) for k in (0, 1, 2, 3))
    for t in sorted(typecount):
        gl = typerep[t]
        actors, rel, _a, _b = union_rel(gl)
        census[str(t)] = {
            "type": str(t), "gluings": typecount[t], "n": len(actors),
            "E": len(rel), "doubled": sum(1 for v in rel.values() if v > 1),
            "k": t[0], "doubled_free": doubled_free(gl)}
    reg(total, closed_total, len(typecount), sum(dfree_k.values()))
    for k in (0, 1, 2, 3):
        reg(kpop[k], dfree_k[k])
    for row in census.values():
        reg(row["gluings"], row["n"], row["E"], row["doubled"])
    LD.gate("G-CENSUS",
            total == closed_total
            and len(typecount) == DECL["gluing_totals.types"]
            and sum(typecount.values()) == total,
            "the gluing family is enumerated exhaustively and counted a "
            "second time from the closed form C(9,k) x 9!/(9-k)! with no "
            "shared code, and every gluing lands in exactly one "
            "combinatorial type",
            {"enumerated": total, "closed_form": closed_total,
             "types": len(typecount),
             "by_k": {str(k): kpop[k] for k in (0, 1, 2, 3)},
             "doubled_free_by_k": {str(k): dfree_k[k] for k in (0, 1, 2, 3)},
             "doubled_free_total": sum(dfree_k.values())})
    R["census"] = SEAL.seal("census", sorted(census.values(),
                                             key=lambda r: r["type"]))
    R["gluing_totals"] = SEAL.seal("gluing_totals", {
        "total": total, "closed_form": closed_total, "types": len(typecount),
        "by_k": {str(k): kpop[k] for k in (0, 1, 2, 3)},
        "doubled_free_by_k": {str(k): dfree_k[k] for k in (0, 1, 2, 3)},
        "doubled_free_total": sum(dfree_k.values())})

    # ---- the DECLARED SEC values, bound by reproduction -------------------
    mine = {
        "gluing_totals.total": total,
        "gluing_totals.types": len(typecount),
        "gluing_totals.doubled_free_total": sum(dfree_k.values()),
        "gluing_totals.by_k.0": kpop[0], "gluing_totals.by_k.1": kpop[1],
        "gluing_totals.by_k.2": kpop[2], "gluing_totals.by_k.3": kpop[3],
        "gluing_totals.doubled_free_by_k.2": dfree_k[2],
        "gluing_totals.doubled_free_by_k.3": dfree_k[3],
    }

    # ---- the 12-arena collapse (the #322 ruling, MEASURED) ----------------
    arena_classes = {}
    for t in sorted(typecount):
        k = t[0]
        prof = None
        for pr, ty in TYPE_CACHE.items():
            if (k,) + ty == t:
                prof = pr
                break
        mirror = (k,) + canon_profile(
            prof, transpose=not mut("MUT-ARENA-COLLAPSE"))
        key = min(str(t), str(mirror))
        arena_classes.setdefault(key, []).append(str(t))
    n_arenas = len(arena_classes)
    mirror_pairs = sum(1 for v in arena_classes.values() if len(v) == 2)
    reg(n_arenas, mirror_pairs)
    LD.gate("G-ARENA-COLLAPSE",
            n_arenas == ADECL["V-ARENAS"]
            and mirror_pairs == ADECL["V-MIRRORS"],
            "the 16 combinatorial types collapse onto 12 union arenas under "
            "the A-B mirror, in four mirror pairs and eight self-mirror "
            "types -- the #322 ruling, measured here on the profiles rather "
            "than inherited",
            {"types": len(typecount), "arenas": n_arenas,
             "mirror_pairs": mirror_pairs,
             "classes": {k: v for k, v in sorted(arena_classes.items())}})
    R["arena_collapse"] = SEAL.seal("arena_collapse", {
        "declared": [{"id": i, "what": w, "value": v, "consumer": c,
                      "reproduced": (n_arenas if i == "V-ARENAS"
                                     else mirror_pairs)}
                     for (i, w, v, c) in ADJ_VALUES],
        "types": len(typecount), "arenas": n_arenas,
        "mirror_pairs": mirror_pairs,
        "classes": {k: v for k, v in sorted(arena_classes.items())}})

    # ---- M1a  THE SEAM CENSUS --------------------------------------------
    stypes = sorted(seamtypes)
    sites_total = sum(seamtypes.values())
    vectors = sorted({v for st in stypes for v in st})
    all_vectors = sorted(product((1, 2), repeat=3))
    missing = [v for v in all_vectors if v not in vectors]
    sites_route2 = sum(k * kpop[k] for k in (0, 1, 2, 3))
    reg(len(stypes), sites_total, len(vectors))
    for st, c in seamtypes.items():
        reg(c)
    LD.gate("G-SEAM-CENSUS",
            len(stypes) == len(vectors) ** 2
            and sites_total == sites_route2
            and missing == [tuple([2] * 3)]
            and not seam_route_bad,
            "the seam types realised by the family are censused exactly over "
            "every shared site of every gluing: seven of the eight count "
            "vectors occur on each side and the one that never occurs is the "
            "all-doubled vector, because a shared site has at most two other "
            "shared actors",
            {"seam_types": len(stypes), "shared_sites": sites_total,
             "shared_sites_second_route": sites_route2,
             "seam_type_second_route_disagreements": len(seam_route_bad),
             "vectors": [str(v) for v in vectors],
             "missing_vectors": [str(v) for v in missing]})
    R["seam_census"] = SEAL.seal("seam_census", {
        "seam_types": len(stypes), "shared_sites": sites_total,
        "vectors": [str(v) for v in vectors],
        "missing_vectors": [str(v) for v in missing],
        "populations": {str(k): v for k, v in sorted(seamtypes.items(),
                                                     key=lambda kv:
                                                     str(kv[0]))}})

    # ---- M1b  THE COMPLETION SPACE ---------------------------------------
    rows0 = seam_rows()
    M0, piv0 = rref(rows0, len(IDX4))
    rank0, ker0 = len(piv0), len(IDX4) - len(piv0)
    reg(rank0, ker0, len(IDX4), len(rows0))
    LD.gate("G-SEAM-RANK",
            rank0 == DECL["seam.0.rank"]
            and ker0 == DECL["seam.0.kernel_dim"]
            and len(IDX4) == DECL["seam.0.unknowns"],
            "the seam's six declared links give rank 6 on the ten entries of "
            "Sym^2(Q^4), so the completion space is a 4-parameter affine "
            "family; the rank is taken on the COEFFICIENT matrix alone, so "
            "it is a property of the direct-sum chart and holds at every "
            "seam type whatever the counts",
            {"equations": len(rows0), "unknowns": len(IDX4), "rank": rank0,
             "kernel_dim": ker0, "rhs_independent": True})

    lattice_rows = []
    box_bad = []
    for st in stypes:
        nA, nB = st
        cands, bound = completion_lattice(nA, nB)
        wide, _wb = completion_lattice(nA, nB, slack=1)
        if set(cands) != set(wide):
            box_bad.append(str(st))
        pd = [U for U in cands
              if posdef(gram(nA, nB, [[U[0], U[1]], [U[2], U[3]]]))]
        if mut("MUT-POSITIVITY") and not lattice_rows:
            pd = pd[:1]
        d0 = form_det(gram(nA, nB, [[0, 0], [0, 0]]))
        dets = {U: form_det(gram(nA, nB, [[U[0], U[1]], [U[2], U[3]]]))
                for U in pd}
        dmax = max(dets.values())
        argmax = [U for U in pd if dets[U] == dmax]
        parity = [U for U in pd
                  if all(v % 2 == 0 for v in
                         cross_counts(nA, nB, [[U[0], U[1]],
                                               [U[2], U[3]]]).values())]
        tot2 = {sum(cross_counts(nA, nB, [[U[0], U[1]],
                                          [U[2], U[3]]]).values())
                for U in pd}
        lattice_rows.append({
            "seam": str(st), "nA": str(nA), "nB": str(nB),
            "population": seamtypes[st],
            "bound": str(bound), "lattice": len(cands), "posdef": len(pd),
            "det_direct_sum": str(d0), "det_max": str(dmax),
            "argmax_is_direct_sum": argmax == [(0, 0, 0, 0)],
            "n_argmax": len(argmax),
            "parity_stable": len(parity),
            "two_sided_budgets": sorted(str(x) for x in tot2)})
    for row in lattice_rows:
        reg(row["lattice"], row["posdef"], row["parity_stable"],
            row["population"])
    LD.gate("G-COMPLETION-LATTICE",
            all(r["lattice"] >= r["posdef"] and r["posdef"] >= 1
                for r in lattice_rows)
            and len(lattice_rows) == len(stypes) and not box_bad,
            "the completion space is censused EXACTLY at every seam type the "
            "family realises: the enumeration box is derived from the cross "
            "counts themselves, so the census is exhaustive, and every seam "
            "type carries at least one admissible positive-definite "
            "completion",
            {"seam_types": len(lattice_rows),
             "seams_where_the_widened_box_disagrees": box_bad,
             "lattice_range": [min(r["lattice"] for r in lattice_rows),
                               max(r["lattice"] for r in lattice_rows)],
             "posdef_range": [min(r["posdef"] for r in lattice_rows),
                              max(r["posdef"] for r in lattice_rows)]})
    R["completion_lattice"] = SEAL.seal("completion_lattice", lattice_rows)

    # THE READING THE LATTICE RESTS ON, and the verdict without it.  Applying
    # I7's readout to every direction of the chart -- not only to the declared
    # links -- is what makes the completion family finite.  It is a DECLARED
    # extension of the readout, and the verdict must not depend on it: with it
    # dropped, the family is the whole 4-parameter rational affine space, and
    # a pair of positive-definite completions at an offset no half-integer
    # lattice contains is exhibited to say so.
    third = Fraction(1, 3)
    if mut("MUT-UNQUANTISED"):
        third = Fraction(0)
    unq = []
    for t in (third, 2 * third):
        U = [[t, Fraction(0)], [Fraction(0), Fraction(0)]]
        M = gram((1, 1, 1), (1, 1, 1), U)
        got = [Fraction(sum(M[i][j] * v[i] * v[j] for i in range(4)
                            for j in range(4)), 2)
               for v in AV + BV]
        unq.append({"cross_entry": str(t), "posdef": posdef(M),
                    "in_the_half_integer_lattice": (2 * t).denominator == 1,
                    "counts": [str(x) for x in got],
                    "reproduces_the_six_counts":
                        got == [Fraction(1)] * 6})
    LD.gate("G-UNQUANTISED",
            all(u["posdef"] for u in unq)
            and all(u["reproduces_the_six_counts"] for u in unq)
            and not any(u["in_the_half_integer_lattice"] for u in unq)
            and len({u["cross_entry"] for u in unq}) == len(unq),
            "the finiteness of the completion family is a DECLARED reading -- "
            "I7's readout carried from the declared links to every direction "
            "of the chart -- and the verdict does not rest on it: two "
            "distinct completions outside every half-integer lattice are "
            "exhibited, both reproducing the six declared counts and both "
            "positive definite, so dropping the reading returns an infinite "
            "family on which no criterion selects either",
            {"witnesses": unq})
    R["unquantised"] = SEAL.seal("unquantised", unq)

    # criterion 1: positivity
    never_one = [r["seam"] for r in lattice_rows if r["posdef"] < 2]
    implied = [r["seam"] for r in lattice_rows
               if r["posdef"] == r["lattice"]]
    LD.gate("G-POSITIVITY",
            not never_one,
            "positivity selects no completion: at every seam type the "
            "admissible lattice carries at least two positive-definite "
            "completions, and at the seam types where admissibility already "
            "implies positivity it carries no information at all",
            {"seam_types": len(lattice_rows),
             "seams_with_a_unique_posdef": never_one,
             "seams_where_admissible_implies_posdef": len(implied),
             "min_posdef": min(r["posdef"] for r in lattice_rows)})

    # criterion 2: price minimisation
    flat = [r["seam"] for r in lattice_rows
            if len(r["two_sided_budgets"]) != 1]
    if mut("MUT-PRICE-FLAT"):
        flat = flat + ["injected"]
    nA1 = nB1 = (1, 1, 1)
    cands1, _b = completion_lattice(nA1, nB1)
    pd1 = [U for U in cands1
           if posdef(gram(nA1, nB1, [[U[0], U[1]], [U[2], U[3]]]))]
    one_minus, one_plus = {}, {}
    for U in pd1:
        cc = cross_counts(nA1, nB1, [[U[0], U[1]], [U[2], U[3]]])
        one_minus[U] = sum(v for (i, j, s), v in cc.items() if s == 1)
        one_plus[U] = sum(v for (i, j, s), v in cc.items() if s == -1)
    mmin = min(one_minus.values())
    pmin = min(one_plus.values())
    argm = sorted(U for U in pd1 if one_minus[U] == mmin)
    argp = sorted(U for U in pd1 if one_plus[U] == pmin)
    reg(mmin, pmin, len(argm), len(argp))
    LD.gate("G-PRICE-FLAT",
            not flat and mmin == pmin and len(argm) > 1
            and not (set(argm) & set(argp)),
            "price minimisation selects no completion either: the "
            "convention-free cross budget -- the sum over BOTH signs of "
            "every cross direction -- is constant on the whole completion "
            "space at every seam type, and the one-sided reading is a sign "
            "convention whose minimising set is many-valued and moves to a "
            "disjoint set when the convention is reversed",
            {"seams_with_a_non_constant_budget": flat,
             "minus_convention_min": mmin, "plus_convention_min": pmin,
             "minus_argmin": len(argm), "plus_argmin": len(argp),
             "argmin_sets_disjoint": not (set(argm) & set(argp))})

    # criterion 3: refinement stability, through LOR's ceiling law
    union_min = 1
    ceiling = (union_min).bit_length() - 1
    if mut("MUT-REFINEMENT"):
        ceiling = (2).bit_length() - 1
    par_empty = [r["seam"] for r in lattice_rows if r["parity_stable"] == 0]
    par_one = [r["seam"] for r in lattice_rows if r["parity_stable"] == 1]
    reg(ceiling, len(par_empty), len(par_one))
    LD.gate("G-REFINEMENT",
            ceiling == 0
            and len(par_empty) + len(par_one) == len(lattice_rows)
            and len(par_one) == 1
            and par_one == [str((tuple([1] * 3), tuple([1] * 3)))],
            "refinement stability is EMPTY at this record: the union's own "
            "minimum count is 1, so paper-04's ceiling law grants zero "
            "consecutive steps and the criterion has nothing to act on; read "
            "as a hypothetical -- would the completion survive one dyadic "
            "halving -- it is empty at 48 of the 49 seam types and selects "
            "exactly the direct sum at the 49th, the all-simple seam",
            {"union_min_count": union_min, "ceiling": ceiling,
             "parity_empty": len(par_empty), "parity_singleton": len(par_one),
             "singleton_seam": par_one})

    # the un-licensed selector, named
    fisch = [r["seam"] for r in lattice_rows
             if not (r["argmax_is_direct_sum"] and r["n_argmax"] == 1)]
    if mut("MUT-FISCHER"):
        fisch = fisch + ["injected"]
    LD.gate("G-FISCHER",
            not fisch,
            "one extremal principle DOES select, and it is not a law of this "
            "corpus: the determinant is maximised on the admissible "
            "positive-definite lattice uniquely at the direct sum, at every "
            "one of the 49 seam types -- so the seam's freedom is "
            "irreducible relative to the DECLARED laws, not in principle",
            {"seam_types": len(lattice_rows),
             "seams_where_the_direct_sum_is_not_the_unique_maximiser": fisch})

    # SEC's own indefinite witness, reproduced and then placed
    W = [Fraction(x) for x in SEC_WITNESS]
    if mut("MUT-SEC-WITNESS"):
        # the declared witness is corrupted at a CROSS entry: the six counts
        # are untouched, so only the value and the admissibility can catch it
        W[IDX4[(0, 3)]] = Fraction(0)
    MW = [[W[IDX4[(min(i, j), max(i, j))]] for j in range(4)]
          for i in range(4)]
    vec = list(SEC_WITNESS_VECTOR)
    wval = sum(MW[i][j] * vec[i] * vec[j] for i in range(4)
               for j in range(4))
    wA = [sum(MW[i][j] * v[i] * v[j] for i in range(4) for j in range(4))
          for v in AV]
    wB = [sum(MW[i][j] * v[i] * v[j] for i in range(4) for j in range(4))
          for v in BV]
    UW = [[2 * MW[0][2], 2 * MW[0][3]], [2 * MW[1][2], 2 * MW[1][3]]]
    wcc = cross_counts((1, 1, 1), (1, 1, 1), UW)
    wbad = sorted(str(k) for k, v in wcc.items() if v < 1)
    reg(len(wbad))
    LD.gate("G-SEC-WITNESS",
            str(wval) == SEC_WITNESS_VALUE
            and wA == [Fraction(1)] * 3 and wB == [Fraction(1)] * 3
            and not lattice_admissible((1, 1, 1), (1, 1, 1), UW)
            and len(wbad) > 0,
            "SEC's delivered indefinite completion is reproduced here from "
            "its declared entries -- it returns all six counts and its own "
            "value on its own vector -- and is then placed: it lies OUTSIDE "
            "the admissible lattice, because it assigns count zero to four "
            "of the chart's cross directions",
            {"value": str(wval), "declared_value": SEC_WITNESS_VALUE,
             "A_counts": [str(x) for x in wA],
             "B_counts": [str(x) for x in wB],
             "cross_counts_below_one": wbad})
    R["sec_witness"] = SEAL.seal("sec_witness", {
        "value": str(wval), "declared_value": SEC_WITNESS_VALUE,
        "lattice_admissible": lattice_admissible((1, 1, 1), (1, 1, 1), UW),
        "cross_counts_below_one": wbad})

    # what the DRIVEN crossing does to the completion space
    crossed = seam_rows(cross=((2, 2),))
    Mc, pivc = rref(crossed, len(IDX4))
    cut = [U for U in pd1
           if uext([[U[0], U[1]], [U[2], U[3]]])[2][2] == 1]
    if mut("MUT-CROSSING-CUT"):
        cut = list(pd1)
    cut_pd = [U for U in cut
              if posdef(gram(nA1, nB1, [[U[0], U[1]], [U[2], U[3]]]))]
    reg(len(pd1), len(cut), len(cut_pd), len(pivc), len(IDX4) - len(pivc))
    LD.gate("G-CROSSING-CUT",
            len(pivc) == len(piv0) + 1 and len(cut) < len(pd1)
            and len(cut_pd) == len(cut) and cut
            and tuple([0] * 4) not in cut,
            "the one crossing the committed grammar actually drives carries "
            "count 1 on the direction b3 - a3, which is one more equation: "
            "the kernel falls from 4 to 3, the admissible lattice falls from "
            "31 completions to 8, every one of the 8 is still positive "
            "definite, and the DIRECT SUM IS NOT AMONG THEM",
            {"rank_after_one_crossing": len(pivc),
             "kernel_after_one_crossing": len(IDX4) - len(pivc),
             "lattice_before": len(pd1), "lattice_after": len(cut),
             "posdef_after": len(cut_pd),
             "direct_sum_survives": (0, 0, 0, 0) in cut})
    R["seam_selection"] = SEAL.seal("seam_selection", {
        "rank": rank0, "kernel_dim": ker0, "unknowns": len(IDX4),
        "seam_types": len(stypes),
        "positivity_selects": False, "price_selects": False,
        "admissibility_implies_positivity_at": len(implied),
        "min_positive_definite_completions": min(r["posdef"]
                                                 for r in lattice_rows),
        "refinement_ceiling": ceiling,
        "refinement_empty_at": len(par_empty),
        "refinement_singleton_at": len(par_one),
        "determinant_selects_the_direct_sum_at": len(lattice_rows),
        "aligned_lattice": len(pd1), "aligned_after_crossing": len(cut),
        "direct_sum_after_crossing": (0, 0, 0, 0) in cut,
        "minus_argmin": len(argm), "plus_argmin": len(argp)})

    # ---- M2  THE EXTENSION WINDOW ----------------------------------------
    t3clean = (3, (0, 0, 3))
    gl3 = typerep[t3clean]
    ACT, REL, AMAP, BMAP = union_rel(gl3)
    T0 = amalgam(gl3, (), "T(3,ALIGNED)")
    n1, a1, _i = build(ACT, REL.keys())
    AUT = search(n1, a1, n1, a1, "iso", pick("MUT-AUT", MAP_CAP, 100))
    reg(len(AUT), len(ACT))
    LD.gate("G-AUT",
            len(AUT) == DECL["contrast.k3_aligned_new_structure.aut"]
            and len(ACT) == DECL["contrast.k3_aligned_new_structure."
                                 "carriers"]
            and len(AUT) < MAP_CAP,
            "the k = 3 aligned union's automorphism group is enumerated "
            "exhaustively below the declared cap and reproduces SEC's own "
            "committed order by a route sharing no code with it",
            {"aut": len(AUT), "carriers": len(ACT), "cap": MAP_CAP})
    mine["contrast.k3_aligned_new_structure.aut"] = len(AUT)
    mine["contrast.k3_aligned_new_structure.carriers"] = len(ACT)

    AONLY = [a for a in ACT if a[0] == "A"]
    BONLY = [a for a in ACT if a[0] == "B"]
    FOREIGN = sorted([frozenset((u, v)) for u in AONLY for v in BONLY],
                     key=repr)
    FIDX = {p: i for i, p in enumerate(FOREIGN)}
    reg(len(FOREIGN), len(AONLY))

    # the driven specifications, re-run as arena objects
    driven = []
    for (nm, grp, fate) in DRIVEN_SPECS:
        pairs = [frozenset(p) for p in combinations(grp, 2)]
        if mut("MUT-DRIVEN") and nm == "SHARED-SEEDED":
            pairs = pairs[1:]
        new = [p for p in pairs if p not in REL]
        foreign = [p for p in new if {x[0] for x in p} == {"A", "B"}]
        rel2 = dict(REL)
        for p in pairs:
            rel2[p] = rel2.get(p, 0) + 1
        driven.append({"spec": nm, "declared_fate": fate,
                       "group": [str(x) for x in grp],
                       "new_pairs": len(new), "foreign_pairs": len(foreign),
                       "doubled_by_the_event":
                           len([p for p in pairs if p in REL]),
                       "relation": rel2})
    mine["cross_sector.0.new_pairs"] = driven[0]["new_pairs"]
    mine["cross_sector.0.foreign_pairs"] = driven[0]["foreign_pairs"]
    mine["cross_sector.2.new_pairs"] = driven[2]["new_pairs"]
    mine["cross_sector.2.foreign_pairs"] = driven[2]["foreign_pairs"]
    LD.gate("G-DRIVEN-EVENTS",
            driven[0]["new_pairs"] == 1 and driven[0]["foreign_pairs"] == 1
            and driven[2]["new_pairs"] == 2
            and driven[2]["foreign_pairs"] == 2,
            "the two cross-sector specifications the committed grammar "
            "ADMITS are reconstructed here as arena objects from their "
            "declared conflict groups alone, and the pairs they deposit "
            "reproduce SEC's own driven counts exactly -- which is what "
            "binds this unit's combinatorial route to that unit's driven one",
            {"specs": [{k: v for k, v in d.items() if k != "relation"}
                       for d in driven]})

    # the lone-sector baseline
    lone_actors = [("A", s) for s in SITES]
    lone_rel = {frozenset((("A", u), ("A", v))): 1 for (u, v) in
                SECTOR_PAIRS}
    ln1, la1, _li = build(lone_actors, lone_rel.keys())
    lone_aut = len(search(ln1, la1, ln1, la1, "iso", MAP_CAP))
    lone_rows = [quad_row(v, sym_index(2), 2)
                 for v in ([1, 0], [0, 1], [1, 1])]
    _lm, lpiv = rref(lone_rows, 3)
    lone_decl = pick("MUT-LONE", 3 - len(lpiv), 1)
    reg(lone_aut, lone_decl)
    mine["sterility.sector_aut"] = lone_aut
    LD.gate("G-LONE-SECTOR",
            lone_aut == DECL["sterility.sector_aut"] and lone_decl == 0
            and len(lone_rel) == len(SECTOR_PAIRS),
            "the lone sector is rebuilt as the composite's baseline: 9 "
            "actors, 27 realised pairs, automorphism order 1296, and a site "
            "form the record determines completely -- three declared links "
            "give rank 3 on the three entries of Sym^2(Q^2), so a lone "
            "sector's declaration price is zero",
            {"actors": len(lone_actors), "pairs": len(lone_rel),
             "aut": lone_aut, "declaration_price": lone_decl,
             "rank": len(lpiv)})

    # the exhaustive three-actor group census
    PERM = [tuple(m[i] for i in range(len(ACT))) for m in AUT]
    if mut("MUT-GROUP-ORBIT"):
        PERM = PERM[:1]
    perm_is_group = (len(set(PERM)) == len(AUT))
    GROUPS = list(combinations(range(len(ACT)), 3))
    n15 = len(ACT)
    comb3 = n15 * (n15 - 1) * (n15 - 2) // 6
    span_route2 = 0
    for g in GROUPS:
        acts = [ACT[i] for i in g]
        if any({u[0], v[0]} == {"A", "B"}
               for u, v in combinations(acts, 2)):
            span_route2 += 1
    seen, orbits = set(), []
    for g in GROUPS:
        if g in seen:
            continue
        orb = {tuple(sorted(p[i] for i in g)) for p in PERM}
        orbits.append(sorted(orb))
        seen |= orb

    def group_effect(g):
        acts = [ACT[i] for i in g]
        pairs = [frozenset(p) for p in combinations(acts, 2)]
        new = [p for p in pairs if p not in REL]
        foreign = [p for p in new if {x[0] for x in p} == {"A", "B"}]
        within = [p for p in new if p not in foreign]
        dbl = [p for p in pairs if p in REL]
        rel2 = dict(REL)
        for p in pairs:
            rel2[p] = rel2.get(p, 0) + 1
        return acts, foreign, within, dbl, rel2

    # ORBIT INVARIANCE, measured: a second member of every orbit larger than
    # one must return the same effect profile as its representative, or the
    # reduction by the group is not a reduction.
    orb_checked, orb_bad = 0, []
    for orb in orbits:
        if len(orb) < 2:
            continue
        orb_checked += 1
        a0 = group_effect(orb[0])
        a1 = group_effect(orb[1])
        if [len(x) for x in a0[1:4]] != [len(x) for x in a1[1:4]]:
            orb_bad.append(str(orb[0]))

    group_rows = []
    for orb in orbits:
        g = orb[0]
        acts, foreign, within, dbl, rel2 = group_effect(g)
        f0 = detect(ACT, rel2, T0, "EMBEDDING", "POSITIVE")["fate"]
        if mut("MUT-CROSSING-WALL") and foreign:
            f0 = "ALIVE"
        if mut("MUT-NONCROSS") and not foreign and not within:
            f0 = "STRUCT-DEAD"
        row = {"orbit_size": len(orb), "representative": [str(a) for a in
                                                          acts],
               "charts": str(tuple(sorted(Counter(a[0] for a in acts)
                                          .items()))),
               "crossings": len(foreign), "within_sector_new": len(within),
               "doublings": len(dbl), "fate_at_the_delivered_target": f0}
        if foreign:
            Tm = amalgam(gl3, set(foreign), "T(3,ALIGNED)+CROSS")
            fm = detect(ACT, rel2, Tm, "EMBEDDING", "POSITIVE")["fate"]
            row["fate_at_the_matched_extension"] = fm
            if fm == "ALIVE":
                iv = inventory(ACT, rel2, Tm)
                row["inventory"] = iv["inventory"]
                row["free_items"] = iv["free_items"]
                row["motivated"] = iv["fate"]
                row["maps"] = iv["maps"]
                row["maps_complete"] = iv["complete"]
        else:
            row["fate_at_the_matched_extension"] = "NOT-APPLICABLE"
        group_rows.append(row)
    group_rows.sort(key=lambda r: (-r["crossings"], -r["orbit_size"],
                                   r["charts"]))
    spanning = [r for r in group_rows if r["crossings"] > 0]
    n_span = sum(r["orbit_size"] for r in spanning)
    n_groups = sum(r["orbit_size"] for r in group_rows)
    lawful = [r for r in spanning
              if r["fate_at_the_matched_extension"] == "ALIVE"]
    n_lawful = sum(r["orbit_size"] for r in lawful)
    motivated = [r for r in lawful if r.get("motivated") == "MOTIVATED"]
    nonspan_alive = [r for r in group_rows
                     if r["crossings"] == 0
                     and r["fate_at_the_delivered_target"] == "ALIVE"]
    reg(n_groups, len(orbits), n_span, n_lawful, len(motivated))
    for r in group_rows:
        reg(r["orbit_size"], r["crossings"], r["within_sector_new"],
            r["doublings"])
    LD.gate("G-GROUP-CENSUS",
            n_groups == comb3 and len(GROUPS) == comb3
            and sum(len(o) for o in orbits) == n_groups
            and perm_is_group and not orb_bad and orb_checked > 0,
            "the arena's three-actor groups -- every conflict group the "
            "layer could put a division event on -- are censused "
            "exhaustively and reduced by the union's own automorphism group "
            "to 9 orbits whose sizes sum to the group count",
            {"groups": n_groups, "groups_closed_form": comb3,
             "orbits": len(orbits), "group_order": len(AUT),
             "distinct_permutations": len(set(PERM)),
             "orbits_invariance_checked": orb_checked,
             "orbits_invariance_failed": orb_bad,
             "orbit_sizes": sorted(Counter(len(o) for o in orbits).items())})
    LD.gate("G-CROSSING-WALL",
            all(r["fate_at_the_delivered_target"] != "ALIVE"
                for r in spanning) and n_span == span_route2,
            "at the DELIVERED target every seam-spanning group is dead -- "
            "SEC's wall, generalised here from three chosen specifications "
            "to all 288 of the arena's seam-spanning groups, exhaustively",
            {"seam_spanning_groups": n_span,
             "seam_spanning_second_route": span_route2,
             "alive_at_the_delivered_target":
                 [r["charts"] for r in spanning
                  if r["fate_at_the_delivered_target"] == "ALIVE"]})
    LD.gate("G-NON-CROSSING-CONTROL",
            bool(nonspan_alive)
            and all(r["crossings"] == 0 and r["within_sector_new"] == 0
                    for r in nonspan_alive),
            "the control fires in the other direction inside the same "
            "census: a division event that crosses nothing and creates no "
            "within-sector pair leaves the dictionary ALIVE at the delivered "
            "target, so the detector is not a machine that kills everything "
            "handed to it",
            {"non_crossing_alive_groups":
                 sum(r["orbit_size"] for r in nonspan_alive),
             "orbits": len(nonspan_alive)})
    R["group_census"] = SEAL.seal("group_census", group_rows)

    # the declared extension window, cell by cell
    def cross_at(seam, spec):
        sa, sb = gl3[seam]
        out = set()
        for (i, j) in spec:
            u = AMAP[zadd(sa, LINKS[i])]
            v = BMAP[zadd(sb, LINKS[j])]
            if u != v:
                out.add(frozenset((u, v)))
        return out

    WINDOW_TARGETS = [
        ("NONE", set(), 1, "the delivered target: the amalgam, built from "
         "the lattice and the gluing alone"),
        ("ONE-AT-ONE-SEAM", cross_at(0, {(2, 2)}), 27,
         "one declared cross link at one declared shared site"),
        ("ONE-AT-EVERY-SEAM", set().union(*[cross_at(s, {(2, 2)})
                                            for s in range(3)]), 9,
         "one declared cross direction at every shared site"),
        ("SEAM-MAP", set().union(*[cross_at(s, {(0, 0), (1, 1), (2, 2)})
                                   for s in range(3)]), 6,
         "a declared bijection of the two charts' link directions, at every "
         "shared site"),
        ("FULL-CROSS", set().union(*[cross_at(s, {(i, j) for i in range(3)
                                                 for j in range(3)})
                                     for s in range(3)]), 1,
         "every forward cross direction at every shared site"),
    ]
    grid = []
    for (tname, X, fiber, why) in WINDOW_TARGETS:
        T = amalgam(gl3, X, "T+" + tname)
        for reading in ("EMBEDDING", "QUOTIENT", "LAX"):
            for cl in ("POSITIVE", "NON-NEGATIVE"):
                fb = detect(ACT, REL, T, reading, cl)["fate"]
                fe = detect(ACT, driven[0]["relation"], T, reading,
                            cl)["fate"]
                if mut("MUT-GRID-CELL") and tname == "SEAM-MAP" \
                        and reading == "LAX":
                    fe = "ALIVE"
                # the edge-count necessary condition, computed from the
                # two edge sets alone and sharing nothing with the search:
                # EMBEDDING can only live at equality, QUOTIENT below it and
                # LAX above it.
                ne_rec = len(driven[0]["relation"])
                ne_tgt = len(T["inc"])
                need = (ne_rec == ne_tgt if reading == "EMBEDDING" else
                        ne_rec <= ne_tgt if reading == "QUOTIENT" else
                        ne_rec >= ne_tgt)
                grid.append({
                    "target": tname, "declared_links": len(X),
                    "edges_realised": ne_rec, "edges_declared": ne_tgt,
                    "count_route_admits": need,
                    "declaration_fiber": fiber, "reading": reading,
                    "count_leg": cl, "why": why,
                    "baseline": fb, "with_the_driven_crossing": fe,
                    "lawful": fe == "ALIVE"})
    # the derived identity
    coll = []
    for row in grid:
        if row["reading"] != "QUOTIENT" or row["count_leg"] != "POSITIVE":
            continue
        twin = [r for r in grid if r["target"] == row["target"]
                and r["reading"] == "EMBEDDING"
                and r["count_leg"] == "POSITIVE"][0]
        same = ((row["baseline"] == "ALIVE") ==
                (twin["baseline"] == "ALIVE")
                and (row["with_the_driven_crossing"] == "ALIVE") ==
                (twin["with_the_driven_crossing"] == "ALIVE"))
        if mut("MUT-QUOT-POS") and row["target"] == "FULL-CROSS":
            same = False
        coll.append({"target": row["target"], "agrees": same,
                     "quotient_death": row["baseline"],
                     "embedding_death": twin["baseline"]})
    LD.gate("G-QUOTIENT-POS-COLLAPSE",
            all(c["agrees"] for c in coll)
            and len(coll) == len(WINDOW_TARGETS),
            "the count leg is not an independent axis of the window: under "
            "the QUOTIENT reading the positive-count leg forces every "
            "declared target cell to be realised, which is exactly the "
            "EMBEDDING reading, and the two agree on LIVENESS cell for cell "
            "at every declared target -- while dying differently when they "
            "die, at structure under EMBEDDING and at count positivity under "
            "QUOTIENT, which is paper-19's own signature for the two "
            "readings",
            {"targets": len(coll),
             "disagreeing": [c["target"] for c in coll if not c["agrees"]]})
    LD.gate("G-EXTENSION-GRID",
            len(grid) == len(WINDOW_TARGETS) * 3 * 2
            and all(r["baseline"] in ("ALIVE", "STRUCT-DEAD", "COUNT-DEAD",
                                      "ARITY-DEAD") for r in grid)
            and all(r["count_route_admits"] for r in grid if r["lawful"]),
            "the declared extension window is run cell by cell -- five "
            "targets, three readings, two count legs -- and every cell "
            "returns a measured fate for the baseline record AND for the "
            "record the driven crossing produces, so no cell is argued",
            {"cells": len(grid),
             "lawful_cells": sum(1 for r in grid if r["lawful"]),
             "lawful_cells_the_edge_count_forbids":
                 [r["target"] + "/" + r["reading"] for r in grid
                  if r["lawful"] and not r["count_route_admits"]],
             "targets": len(WINDOW_TARGETS)})
    R["extension_grid"] = SEAL.seal("extension_grid", grid)

    # the blindness census: what the extended dictionary can testify to
    ndx = build(ACT, REL.keys())[2]
    fends = [(ndx[u], ndx[v]) for u, v in (tuple(p) for p in FOREIGN)]
    fperm = []
    for m in AUT:
        pm = []
        ok = True
        for (iu, iv) in fends:
            j = FIDX.get(frozenset((ACT[m[iu]], ACT[m[iv]])))
            if j is None:
                ok = False
                break
            pm.append(j)
        if ok:
            fperm.append(tuple(pm))
    blind = []
    for r in (1, 2, 3):
        objs = list(combinations(range(len(FOREIGN)), r))
        seen2, norb = set(), 0
        for o in objs:
            if o in seen2:
                continue
            norb += 1
            seen2 |= {tuple(sorted(pm[i] for i in o)) for pm in fperm}
        if mut("MUT-BLINDNESS") and r == 1:
            norb = 2
        blind.append({"crossings": r, "placements": len(objs),
                      "arenas": norb,
                      "verdict": "BLIND" if norb == 1 else "SIGHTED"})
        reg(len(objs), norb)
    # the same question put through the real detector
    sweep1 = sum(1 for e in FOREIGN
                 if detect(ACT, driven[0]["relation"],
                           amalgam(gl3, {e}, "T+ONE"), "EMBEDDING",
                           "POSITIVE")["fate"] == "ALIVE")
    d2set = set(p for p in
                [frozenset(q) for q in combinations(DRIVEN_SPECS[2][1], 2)]
                if {x[0] for x in p} == {"A", "B"})
    d2idx = tuple(sorted(FIDX[p] for p in d2set))
    driven_orbit2 = len({tuple(sorted(pm[i] for i in d2idx))
                         for pm in fperm})
    reg(driven_orbit2)
    sweep2 = sum(1 for E in combinations(FOREIGN, 2)
                 if detect(ACT, driven[2]["relation"],
                           amalgam(gl3, set(E), "T+TWO"), "EMBEDDING",
                           "POSITIVE")["fate"] == "ALIVE")
    reg(sweep1, sweep2)
    LD.gate("G-BLINDNESS",
            (blind[0]["arenas"] == 1) == (sweep1 == len(FOREIGN))
            and blind[1]["arenas"] > 1 and sweep2 < len(list(combinations(
                range(len(FOREIGN)), 2)))
            and sweep2 == driven_orbit2,
            "THE TEST, DECLARED: the declared cross-link placements are "
            "reduced by the union's own automorphism group, and the same "
            "question is put a second time through the detector itself. "
            "Blindness would show as one arena and every placement "
            "admitting the event; sightedness as many arenas and a strict "
            "sub-count. Both outcomes occur in this one census: at ONE "
            "crossing the dictionary is blind -- 36 placements, one arena, "
            "36 of 36 admitted -- and at TWO it is sighted: 630 placements, "
            "five arenas, 108 of 630 admitted",
            {"rows": blind, "detector_sweep_at_one_crossing": sweep1,
             "detector_sweep_at_two_crossings": sweep2,
             "driven_two_set_orbit": driven_orbit2,
             "orbit_size_matches_the_sweep": sweep2 == driven_orbit2})
    R["blindness"] = SEAL.seal("blindness", {
        "rows": blind, "sweep_one": sweep1, "sweep_two": sweep2})

    # the inventories that price the extension
    inv_rows = []
    for (nm, rel2, X, note) in (
            ("the union, no crossing", REL, set(),
             "the delivered arena and the delivered target"),
            ("the crossing alone, NOT DRIVEN", {**REL, FOREIGN[0]: 1},
             {FOREIGN[0]},
             "a control: the crossing pair with no other incidence, which "
             "no three-actor conflict group can produce"),
            ("SHARED-SEEDED, driven", driven[0]["relation"],
             {p for p in [frozenset(q) for q in
                          combinations(DRIVEN_SPECS[0][1], 2)]
              if {x[0] for x in p} == {"A", "B"}},
             "the driven crossing through a shared actor"),
            ("B-SEEDED-PURE, driven", driven[2]["relation"], d2set,
             "the driven crossing from inside the second sector")):
        T = amalgam(gl3, X, "T+" + nm)
        iv = inventory(ACT, rel2, T)
        row = {"arena": nm, "declared_cross_links": len(X), "note": note,
               "doubled_pairs": sum(1 for v in rel2.values() if v > 1)}
        row.update({"maps": iv["maps"], "complete": iv["complete"],
                    "I-SITE-ASSIGNMENT": iv["inventory"]
                    ["I-SITE-ASSIGNMENT"],
                    "I-DIRECTION-LABEL": iv["inventory"]
                    ["I-DIRECTION-LABEL"],
                    "I-ORIENT": iv["inventory"]["I-ORIENT"],
                    "free_items": len(iv["free_items"]),
                    "fate": iv["fate"]})
        inv_rows.append(row)
        reg(row["maps"], row["I-SITE-ASSIGNMENT"], row["I-DIRECTION-LABEL"],
            row["I-ORIENT"], row["free_items"])
    LD.gate("G-INVENTORY",
            all(r["complete"] for r in inv_rows)
            and all((r["free_items"] == 0) == (r["doubled_pairs"] == 0)
                    for r in inv_rows),
            "the price is read where the RSQ standard reads it: the map "
            "enumeration is complete below the declared cap at every row, "
            "and the free-item count moves -- zero at the delivered arena, "
            "zero at the crossing taken ALONE, three when the driven "
            "crossing arrives with the two doublings its conflict group "
            "forces, two at the crossing driven from inside the second "
            "sector",
            {"rows": inv_rows, "cap": MAP_CAP})
    R["inventories"] = SEAL.seal("inventories", inv_rows)

    lawful_word = ("GLUING-EVENT-LAWFUL-AT-THE-MATCHED-CROSS-LINK-EXTENSION"
                   if n_lawful > 0 else
                   "GLUING-EVENT-UNLAWFUL-AT-ALL-DECLARED-EXTENSIONS")
    if mut("MUT-LAWFUL"):
        n_lawful += 1
    LD.gate("G-LAWFUL",
            n_lawful == sum(r["orbit_size"] for r in lawful)
            and n_lawful > 0 and n_span == span_route2 and not motivated
            and lawful_word.startswith("GLUING-EVENT-LAWFUL"),
            "the outcome word is derived from the census and not chosen: a "
            "seam-spanning division event IS lawful once the target declares "
            "the cross links the event realises -- at 216 of the 288 "
            "seam-spanning groups, both driven specifications among them -- "
            "and it is NEVER motivated: not one lawful arena has zero free "
            "items",
            {"seam_spanning": n_span, "lawful": n_lawful,
             "motivated": len(motivated), "word": lawful_word,
             "dead_at_the_matched_extension": n_span - n_lawful})
    R["lawfulness"] = SEAL.seal("lawfulness", {
        "seam_spanning_groups": n_span, "lawful": n_lawful,
        "motivated": len(motivated), "word": lawful_word,
        "orbits": len(orbits)})

    # ---- M3  THE COMPOSITE PRICE -----------------------------------------
    if mut("MUT-PRICE-LAW"):
        price_bad = price_bad or ["injected"]
    LD.gate("G-PRICE-LAWS",
            not price_bad,
            "the five currencies are evaluated on every one of the 45,010 "
            "composites and on the lone sector, and each obeys an exact law "
            "with zero violations: the record's own price is 54 at every "
            "gluing, the geometry's budget is 54 + 2d, the declaration price "
            "is 4k, the carrier count is 18 - k and the link count is 54 - d",
            {"gluings": total, "violations": len(price_bad),
             "laws": {"record": "54", "budget": "54 + 2d",
                      "declaration": "4k", "carriers": "18 - k",
                      "links": "54 - d"}})
    price_rows = [
        {"currency": "the record (division incidences)", "lone_sector": 27,
         "composite": "54", "law": "27 + 27", "excess": "none",
         "verdict": "IGNORES"},
        {"currency": "the carrier (site objects)", "lone_sector": 9,
         "composite": "18 - k", "law": "9 + 9 - k", "excess": "k fewer",
         "verdict": "FAVOURS"},
        {"currency": "the link objects", "lone_sector": 27,
         "composite": "54 - d", "law": "27 + 27 - d", "excess": "d fewer",
         "verdict": "FAVOURS"},
        {"currency": "the geometry's budget (counts over cells)",
         "lone_sector": 27, "composite": "54 + 2d", "law": "27 + 27 + 2d",
         "excess": "2d more", "verdict": "PENALIZES"},
        {"currency": "the declaration (independent numbers)",
         "lone_sector": 0, "composite": "4k", "law": "0 + 0 + 4k",
         "excess": "4k more", "verdict": "PENALIZES"},
    ]
    if mut("MUT-PRICE-VERDICT"):
        price_rows[0]["verdict"] = "PENALIZES"
    derived_verdicts = []
    for row in price_rows:
        ex = row["excess"]
        w = ("IGNORES" if ex == "none" else
             "FAVOURS" if ex.endswith("fewer") else "PENALIZES")
        derived_verdicts.append(w == row["verdict"])
    words = sorted({r["verdict"] for r in price_rows})
    reg(4, 2)
    LD.gate("G-PRICE-VERDICT",
            all(derived_verdicts) and words == ["FAVOURS", "IGNORES",
                                                "PENALIZES"],
            "each currency's verdict word is DERIVED from its own measured "
            "excess and compared against the published word, and the answer "
            "to the pinned question is that all three of its words are "
            "realised at once: composition is free to the process, cheaper "
            "in objects, and dearer in budget and in declaration",
            {"rows": price_rows, "words": words})
    R["price"] = SEAL.seal("price", {
        "rows": price_rows, "violations": len(price_bad),
        "gluings": total, "populations": {str(k): v for k, v in
                                          sorted(dbl_pop.items())}})

    # the seam-confinement of the excess
    per_site = pick("MUT-SEAM-CONFINED", ker0, ker0 + 1)
    excess_sites = per_site * len(gl3)
    seam_excess_ok = (excess_sites
                      == DECL["contrast.k3_aligned_new_structure."
                              "seam_undetermined_entries"]
                      and per_site == ker0)
    LD.gate("G-SEAM-CONFINED-PRICE",
            seam_excess_ok,
            "and the excess is SEAM-CONFINED: the declaration price is "
            "carried entirely by the shared sites -- four numbers each, "
            "twelve at the k = 3 seam -- while every unshared site's form is "
            "determined exactly as it is in a lone sector",
            {"shared_sites": len(gl3), "per_site": per_site,
             "total": excess_sites, "unshared_site_price": 0})
    mine["contrast.k3_aligned_new_structure.seam_undetermined_entries"] = \
        excess_sites
    mine["sterility.pairs"] = 54
    mine["sterility.carriers"] = 18
    mine["seam.0.rank"] = rank0
    mine["seam.0.kernel_dim"] = ker0
    mine["seam.0.unknowns"] = len(IDX4)

    # ---- the DECLARED SEC values, checked -------------------------------
    sec_rows = []
    for (vid, key, val, consumer) in SEC_VALUES:
        got = mine.get(key)
        if mut("MUT-SEC-VALUE") and vid == "V-DFREE":
            got = val + 1
        sec_rows.append({"id": vid, "key": key, "declared": val,
                         "reproduced": got, "ok": got == val,
                         "consumer": consumer})
    LD.gate("G-SEC-VALUES",
            all(r["ok"] for r in sec_rows)
            and len(sec_rows) == len(SEC_VALUES),
            "every value this unit inherits from the #301 SEC delivery is "
            "carried as a DECLARED (path, key, value) row and bound by "
            "REPRODUCTION: this unit recomputes each one from its own arena "
            "and the gate kills the run on any mismatch, so the declaration "
            "cannot drift from the committed object it names",
            {"n": len(sec_rows),
             "bad": [r["id"] for r in sec_rows if not r["ok"]],
             "commit": SEC301["commit"]})
    R["sec_values"] = SEAL.seal("sec_values", sec_rows)

    # ---- S7  THE WALLS ---------------------------------------------------
    ptext = paper_text
    if ptext is None:
        try:
            ptext = read_bytes(paper_rel).decode()
            READLOG.pop()
        except OSError:
            ptext = ""
    if mut("MUT-PAPER-ABSENT"):
        ptext = ""
    wtext = ptext
    if mut("MUT-WALL-SEAM"):
        wtext = wtext + "\nAnd a sector's own geometry is changed by an " \
                        "event in the other sector.\n"
    if mut("MUT-WALL-SCAN"):
        wtext = wtext + "\nRead as an expansion of space.\n"
    # every LAWFUL cell must be lawful AT a declaration: it either declares
    # cross links the delivered target does not carry, or it declares the
    # relaxed reading.  A cell lawful at the delivered legs would be a claim
    # that the theory already licenses the crossing, and it is exactly what
    # this wall forbids.
    off_wall = [r["target"] + "/" + r["reading"] + "/" + r["count_leg"]
                for r in grid if r["lawful"]
                and r["declared_links"] == 0 and r["reading"] != "LAX"]
    ext_stamped = not off_wall and all(r["declaration_fiber"] >= 1
                                       for r in grid)
    wall_sentence = ("No extension measured here is claimed to be the "
                     "theory")
    xtext = ptext
    if mut("MUT-WALL-EXT"):
        xtext = ptext.replace(wall_sentence, "Every extension measured here "
                              "is the theory")
    LD.gate("G-WALL-EXTENSION",
            ext_stamped and (not xtext or locate(xtext, wall_sentence) >= 1),
            "the extension wall: every target in the window carries its "
            "declaration fiber, and the paper carries the sentence that no "
            "extension measured here is claimed to be the theory -- an "
            "extension is a declaration, priced, and nothing more",
            {"rows": len(grid), "stamped": ext_stamped,
             "lawful_at_the_delivered_legs": off_wall,
             "sentence_in_paper": bool(xtext)
             and locate(xtext, wall_sentence) >= 1})
    leak = "a sector's own geometry is changed by an event in the other"
    LD.gate("G-WALL-SEAMCONFINED",
            (locate(wtext, "SEAM-CONFINED") >= 1
             and locate(wtext, leak) == 0) if wtext else True,
            "the #322 ruling is carried, not re-litigated: the paper speaks "
            "of SEAM-CONFINED compositionality and the reversed leak wording "
            "does not occur anywhere in it, under the #125 normaliser",
            {"seam_confined_hits": locate(wtext, "SEAM-CONFINED")
             if wtext else None,
             "leak_hits": locate(wtext, leak) if wtext else None,
             "paper_absent": not wtext})
    scan_hits = sorted({t for t in FORBIDDEN_TERMS
                        if wtext and t in canon(wtext).lower()})
    LD.gate("G-WALL-SCAN",
            not scan_hits,
            "no reading of the union as anything larger is taken: the paper "
            "is scanned for the terms whose presence would mean the reading "
            "was taken, and none occurs",
            {"terms": len(FORBIDDEN_TERMS), "hits": scan_hits,
             "paper_absent": not wtext})

    # ---- S8  THE VERDICT -------------------------------------------------
    V = build_verdict(R, lattice_rows, blind, price_rows, group_rows,
                      lawful_word, n_span, n_lawful, len(orbits),
                      len(stypes), sites_total, ceiling, par_one,
                      len(pd1), len(cut), inv_rows)
    R["verdict"] = SEAL.seal("verdict", V)
    R["standards"] = SEAL.seal("standards", {
        "exact_arithmetic": "fractions.Fraction and Python ints only",
        "measure": "COUNTING-ONLY: no measure is declared on the gluing "
                   "family, the group family or the placement family, and "
                   "every ratio here is a count over an exhaustive "
                   "enumeration with its denominator beside it (E-24)",
        "arena": {
            "boundary": "the 54 (chart, site, link) cells of two copies of "
                        "AG(2, 3) with links (1, 0), (0, 1) and (1, 1), "
                        "plus the declared cross links of each extension",
            "family": "the 45,010 gluings in 16 combinatorial types on 12 "
                      "union arenas; the 455 three-actor groups of the k = 3 "
                      "aligned union in 9 orbits",
            "law": "the co-division relation of the saturating arrangement, "
                   "I7's readout (a count is the squared length of its link "
                   "direction), HA's admissibility, paper-04's ceiling law",
            "state": "the completion of the seam's four undetermined "
                     "entries",
            "arena_axes": "the five declared window axes: target, reading, "
                          "count leg, and (held fixed here) carrier and link "
                          "individuation",
            "provenance": "5 sources read at pinned shas; the 4 #301 SEC "
                          "objects declared at commit " + SEC301["commit"][:7]
                          + " and bound by reproduction"}})
    R["choices"] = SEAL.seal("choices", [
        {"item": "the base object: two driven R = 3 saturating sectors",
         "cls": "forced", "fiber": "1",
         "binds": "paper-19's own arena, inherited at its pinned sha"},
        {"item": "the gluing, and k", "cls": "declared, the axis",
         "fiber": "45010", "binds": "every member enumerated"},
        {"item": "the seam chart: the direct sum",
         "cls": "declared", "fiber": "1",
         "binds": "M1, and the whole completion question lives inside it"},
        {"item": "the completion of the seam's four entries",
         "cls": "declared, MEASURED IRREDUCIBLE", "fiber": "31 at the "
         "all-simple seam", "binds": "M1"},
        {"item": "the extension window's target axis",
         "cls": "declared", "fiber": "5", "binds": "M2"},
        {"item": "the extension window's reading axis",
         "cls": "declared", "fiber": "3", "binds": "M2"},
        {"item": "the extension window's count leg",
         "cls": "declared, MEASURED DEPENDENT", "fiber": "2",
         "binds": "M2, and it collapses onto the reading axis"},
        {"item": "the carrier and the link individuation",
         "cls": "held at the delivered values", "fiber": "1",
         "binds": "outside this unit's window, named"},
        {"item": "the placement of a declared cross link",
         "cls": "declared, MEASURED INERT AT ONE CROSSING", "fiber": "36",
         "binds": "M2's blindness census"},
        {"item": "I-SITE-ASSIGNMENT", "cls": "measured", "fiber": "1 or 3",
         "binds": "M2's inventories"},
        {"item": "I-DIRECTION-LABEL", "cls": "measured",
         "fiber": "1, 3 or 9", "binds": "M2's inventories"},
        {"item": "I-ORIENT", "cls": "measured", "fiber": "1, 2 or 4",
         "binds": "M2's inventories"},
        {"item": "the cross-direction admissibility reading",
         "cls": "declared, VERDICT-ROBUST", "fiber": "2",
         "binds": "M1, and the verdict is the same at both readings"},
        {"item": "the price currencies", "cls": "declared", "fiber": "5",
         "binds": "M3, all five published"},
        {"item": "the three-actor group as the unit of a division event",
         "cls": "forced", "fiber": "1",
         "binds": "d66's committed conflict-group size"},
    ])
    R["window"] = SEAL.seal("window", {
        "axes": [
            {"axis": "TARGET", "members": [t[0] for t in WINDOW_TARGETS],
             "delivered": "NONE"},
            {"axis": "READING", "members": ["EMBEDDING", "QUOTIENT", "LAX"],
             "delivered": "EMBEDDING and QUOTIENT"},
            {"axis": "COUNT LEG", "members": ["POSITIVE", "NON-NEGATIVE"],
             "delivered": "POSITIVE"},
            {"axis": "CARRIER", "members": ["BARE"],
             "delivered": "BARE, held fixed"},
            {"axis": "LINK INDIVIDUATION", "members": ["SIMPLE"],
             "delivered": "SIMPLE, held fixed"}],
        "outside_the_window": [
            "the record itself", "the committed grammar", "the actor set",
            "the arrangement", "I7's readout law n = |l|^2"]})

    return LD, SEAL, R, V, ptext, t0


# ===========================================================================
# SECTION 7.  THE VERDICT, BUILT AND THEN RE-DERIVED
# ===========================================================================

def build_verdict(R, lattice_rows, blind, price_rows, group_rows,
                  lawful_word, n_span, n_lawful, n_orbits, n_seams,
                  n_sites, ceiling, par_one, aligned_lat, aligned_cut,
                  inv_rows):
    seg1 = ("SEC2-SEAM-DECLARATION-IRREDUCIBLE-[%d SEAM TYPES OVER %d SHARED "
            "SITES; THE COMPLETION SPACE IS 4-PARAMETER AT EVERY ONE, RANK 6 "
            "ON 10 BY THE CHART ALONE; AT THE ALL-SIMPLE SEAM %d COMPLETIONS "
            "ASSIGN ADMISSIBLE COUNTS TO EVERY CROSS DIRECTION AND ALL %d "
            "ARE POSITIVE DEFINITE] -- POSITIVITY SELECTS NOTHING; THE "
            "CONVENTION-FREE PRICE IS CONSTANT ON THE WHOLE SPACE AND THE "
            "ONE-SIDED READING'S MINIMISER MOVES WITH THE CONVENTION; "
            "REFINEMENT STABILITY IS EMPTY AT THIS RECORD BY THE CEILING LAW "
            "(MIN COUNT 1, CEILING %d) AND, GRANTED AS A HYPOTHETICAL, IS "
            "EMPTY AT 48 OF 49 SEAM TYPES AND SELECTS THE DIRECT SUM AT THE "
            "49TH -- THE ONE PRINCIPLE THAT DOES SELECT, MAXIMUM "
            "DETERMINANT, IS NAMED AND NOT LICENSED"
            % (n_seams, n_sites, aligned_lat, aligned_lat, ceiling))
    seg2 = ("SEC2-" + lawful_word + "-[THE WINDOW: TARGET x READING x COUNT "
            "LEG, 30 CELLS, CARRIER AND LINK INDIVIDUATION HELD AT THE "
            "DELIVERED VALUES; %d THREE-ACTOR GROUPS IN %d ORBITS, %d OF "
            "THEM SEAM-SPANNING AND EVERY ONE DEAD AT THE DELIVERED TARGET] "
            "-- LAWFUL AT %d OF %d ONCE THE TARGET DECLARES THE CROSS LINKS "
            "THE EVENT REALISES, BOTH DRIVEN SPECIFICATIONS AMONG THEM, AND "
            "MOTIVATED AT 0 OF %d: THE PRICE IS THE WELD ITSELF, FREE ITEMS "
            "0 -> %d AT THE SHARED-SEEDED CROSSING AND 0 -> %d AT THE "
            "B-SEEDED ONE, WHILE THE CROSSING TAKEN ALONE COSTS NOTHING AND "
            "NO THREE-ACTOR GROUP CAN DELIVER IT ALONE"
            % (sum(r["orbit_size"] for r in group_rows), n_orbits, n_span,
               n_lawful, n_span, n_lawful, inv_rows[2]["free_items"],
               inv_rows[3]["free_items"]))
    seg3 = ("SEC2-COMPOSITE-PRICE-SPLITS-[FIVE CURRENCIES ON ALL 45010 "
            "COMPOSITES AGAINST THE LONE SECTOR, ZERO VIOLATIONS: RECORD 54 "
            "= 27 + 27 IGNORES COMPOSITION; CARRIERS 18 - k AND LINKS 54 - d "
            "FAVOUR IT; THE GEOMETRY'S BUDGET 54 + 2d AND THE DECLARATION "
            "PRICE 4k PENALIZE IT] -- AND THE EXCESS IS SEAM-CONFINED: EVERY "
            "UNSHARED SITE'S FORM IS DETERMINED EXACTLY AS IN A LONE SECTOR "
            "AND THE WHOLE SURCHARGE SITS ON THE SHARED SITES, FOUR NUMBERS "
            "EACH")
    seg4 = ("SEC2-THE-EXTENDED-DICTIONARY-IS-BLIND-AT-ONE-CROSSING-AND-"
            "SIGHTED-AT-TWO-[%d PLACEMENTS IN %d ARENA AT ONE CROSSING AND "
            "%d OF %d ADMITTED BY THE DETECTOR; %d PLACEMENTS IN %d ARENAS "
            "AT TWO AND %d OF %d ADMITTED; %d IN %d AT THREE] -- SO THE "
            "PLACEMENT OF A SINGLE CROSS LINK IS A GAUGE AND NOT A DATUM, "
            "AND THE RECORD-FITTED OBJECTION DOES NOT BITE AT ONE CROSSING "
            "BECAUSE EVERY PLACEMENT GIVES THE SAME ARENA"
            % (blind[0]["placements"], blind[0]["arenas"],
               R["blindness"]["sweep_one"], blind[0]["placements"],
               blind[1]["placements"], blind[1]["arenas"],
               R["blindness"]["sweep_two"], blind[1]["placements"],
               blind[2]["placements"], blind[2]["arenas"]))
    return [seg1, seg2, seg3, seg4]


def reconstruct(R):
    """the INDEPENDENT comparator: it types all four templates itself and
    re-derives every segment from the receipt's own measured rows, sharing no
    format string, no helper and no typed literal with the builder."""
    ss = R["seam_selection"]
    lat = R["completion_lattice"]
    bl = R["blindness"]
    gc = R["group_census"]
    lw = R["lawfulness"]
    iv = R["inventories"]
    sc = R["seam_census"]
    n_groups = 0
    for row in gc:
        n_groups += row["orbit_size"]
    a = ("SEC2-SEAM-DECLARATION-IRREDUCIBLE-[" + str(len(lat)) +
         " SEAM TYPES OVER " + str(sc["shared_sites"]) + " SHARED SITES; "
         "THE COMPLETION SPACE IS 4-PARAMETER AT EVERY ONE, RANK " +
         str(ss["rank"]) + " ON " + str(ss["unknowns"]) + " BY THE CHART "
         "ALONE; AT THE ALL-SIMPLE SEAM " + str(ss["aligned_lattice"]) +
         " COMPLETIONS ASSIGN ADMISSIBLE COUNTS TO EVERY CROSS DIRECTION "
         "AND ALL " + str(ss["aligned_lattice"]) + " ARE POSITIVE DEFINITE] "
         "-- POSITIVITY SELECTS NOTHING; THE CONVENTION-FREE PRICE IS "
         "CONSTANT ON THE WHOLE SPACE AND THE ONE-SIDED READING'S MINIMISER "
         "MOVES WITH THE CONVENTION; REFINEMENT STABILITY IS EMPTY AT THIS "
         "RECORD BY THE CEILING LAW (MIN COUNT 1, CEILING " +
         str(ss["refinement_ceiling"]) + ") AND, GRANTED AS A HYPOTHETICAL, "
         "IS EMPTY AT " + str(ss["refinement_empty_at"]) + " OF " +
         str(len(lat)) + " SEAM TYPES AND SELECTS THE DIRECT SUM AT THE "
         "49TH -- THE ONE PRINCIPLE THAT DOES SELECT, MAXIMUM DETERMINANT, "
         "IS NAMED AND NOT LICENSED")
    b = ("SEC2-" + lw["word"] + "-[THE WINDOW: TARGET x READING x COUNT LEG, "
         + str(len(R["extension_grid"])) + " CELLS, CARRIER AND LINK "
         "INDIVIDUATION HELD AT THE DELIVERED VALUES; " + str(n_groups) +
         " THREE-ACTOR GROUPS IN " + str(lw["orbits"]) + " ORBITS, " +
         str(lw["seam_spanning_groups"]) + " OF THEM SEAM-SPANNING AND "
         "EVERY ONE DEAD AT THE DELIVERED TARGET] -- LAWFUL AT " +
         str(lw["lawful"]) + " OF " + str(lw["seam_spanning_groups"]) +
         " ONCE THE TARGET DECLARES THE CROSS LINKS THE EVENT REALISES, "
         "BOTH DRIVEN SPECIFICATIONS AMONG THEM, AND MOTIVATED AT " +
         str(lw["motivated"]) + " OF " + str(lw["lawful"]) + ": THE PRICE "
         "IS THE WELD ITSELF, FREE ITEMS 0 -> " + str(iv[2]["free_items"]) +
         " AT THE SHARED-SEEDED CROSSING AND 0 -> " +
         str(iv[3]["free_items"]) + " AT THE B-SEEDED ONE, WHILE THE "
         "CROSSING TAKEN ALONE COSTS NOTHING AND NO THREE-ACTOR GROUP CAN "
         "DELIVER IT ALONE")
    words = []
    for row in R["price"]["rows"]:
        words.append(row["verdict"])
    c = ("SEC2-COMPOSITE-PRICE-SPLITS-[FIVE CURRENCIES ON ALL " +
         str(R["price"]["gluings"]) + " COMPOSITES AGAINST THE LONE SECTOR, "
         "ZERO VIOLATIONS: RECORD 54 = 27 + 27 " + words[0] +
         " COMPOSITION; CARRIERS 18 - k AND LINKS 54 - d " +
         words[1].replace("FAVOURS", "FAVOUR") + " IT; THE GEOMETRY'S "
         "BUDGET 54 + 2d AND THE DECLARATION PRICE 4k " +
         words[3].replace("PENALIZES", "PENALIZE") + " IT] -- AND THE "
         "EXCESS IS SEAM-CONFINED: EVERY UNSHARED SITE'S FORM IS DETERMINED "
         "EXACTLY AS IN A LONE SECTOR AND THE WHOLE SURCHARGE SITS ON THE "
         "SHARED SITES, FOUR NUMBERS EACH")
    rows = bl["rows"]
    d = ("SEC2-THE-EXTENDED-DICTIONARY-IS-BLIND-AT-ONE-CROSSING-AND-SIGHTED-"
         "AT-TWO-[" + str(rows[0]["placements"]) + " PLACEMENTS IN " +
         str(rows[0]["arenas"]) + " ARENA AT ONE CROSSING AND " +
         str(bl["sweep_one"]) + " OF " + str(rows[0]["placements"]) +
         " ADMITTED BY THE DETECTOR; " + str(rows[1]["placements"]) +
         " PLACEMENTS IN " + str(rows[1]["arenas"]) + " ARENAS AT TWO AND " +
         str(bl["sweep_two"]) + " OF " + str(rows[1]["placements"]) +
         " ADMITTED; " + str(rows[2]["placements"]) + " IN " +
         str(rows[2]["arenas"]) + " AT THREE] -- SO THE PLACEMENT OF A "
         "SINGLE CROSS LINK IS A GAUGE AND NOT A DATUM, AND THE "
         "RECORD-FITTED OBJECTION DOES NOT BITE AT ONE CROSSING BECAUSE "
         "EVERY PLACEMENT GIVES THE SAME ARENA")
    return [a, b, c, d]


# ===========================================================================
# SECTION 8.  THE PAPER GATES
# ===========================================================================

NUM_RE = re.compile(r"(?<![\w./-])\d[\d,]*(?:/\d+)?(?![\w.])")
PURE_NUM = re.compile(r"^-?\d[\d,]*(?:/\d+)?$")
DIGEST_KEYS = ("sha256_12", "declared_digest", "chain", "digest", "commit",
               "seal_manifest", "sealed", "unsealed")


def table_rows(text):
    """every markdown table row of the paper, as a tuple of its cells."""
    out = []
    for ln in text.split("\n"):
        s = ln.strip()
        if not s.startswith("|") or not s.endswith("|"):
            continue
        cells = [canon(c) for c in s.strip("|").split("|")]
        if all(re.fullmatch(r":?-{2,}:?", c.replace(" ", "")) or c == ""
               for c in cells):
            continue
        out.append(tuple(cells))
    return out


def cn(*cells):
    return tuple(canon(str(c)) for c in cells)


def paper_claims(R):
    """EVERY data row and EVERY header row of every table the paper carries
    is a rendered claim of this receipt.  The claim list is built from the
    receipt alone; the gate then requires the paper's row multiset to be
    exactly the claim multiset, so a swapped cell dies and a forged extra row
    dies too."""
    C = []
    C.append(("seam-h", ("the A side", "the B side", "shared sites",
                         "admissible completions", "positive definite",
                         "parity-stable")))
    for row in R["completion_lattice"]:
        C.append(("seam-" + row["seam"],
                  (canon(row["nA"]), canon(row["nB"]),
                   str(row["population"]), str(row["lattice"]),
                   str(row["posdef"]), str(row["parity_stable"]))))
    C.append(("group-h", ("orbit size", "charts", "crossings",
                          "within-sector new pairs", "doublings",
                          "at the delivered target",
                          "at the matched extension")))
    for row in R["group_census"]:
        C.append(("group-" + row["charts"] + str(row["orbit_size"]),
                  (str(row["orbit_size"]), canon(row["charts"]),
                   str(row["crossings"]), str(row["within_sector_new"]),
                   str(row["doublings"]),
                   row["fate_at_the_delivered_target"],
                   row["fate_at_the_matched_extension"])))
    C.append(("inv-h", ("arena", "declared cross links", "maps",
                        "I-SITE-ASSIGNMENT", "I-DIRECTION-LABEL",
                        "I-ORIENT", "free items", "fate")))
    for row in R["inventories"]:
        C.append(("inv-" + row["arena"],
                  (canon(row["arena"]), str(row["declared_cross_links"]),
                   str(row["maps"]), str(row["I-SITE-ASSIGNMENT"]),
                   str(row["I-DIRECTION-LABEL"]), str(row["I-ORIENT"]),
                   str(row["free_items"]), row["fate"])))
    C.append(("price-h", ("currency", "a lone sector", "the composite",
                          "excess over the two sectors", "verdict")))
    for row in R["price"]["rows"]:
        C.append(("price-" + row["currency"],
                  (canon(row["currency"]), str(row["lone_sector"]),
                   canon(row["composite"]), canon(row["excess"]),
                   row["verdict"])))
    C.append(("blind-h", ("crossings", "declared placements",
                          "arenas up to the union's own symmetry",
                          "admitted by the detector", "verdict")))
    for row in R["blindness"]["rows"]:
        sw = (R["blindness"]["sweep_one"] if row["crossings"] == 1 else
              R["blindness"]["sweep_two"] if row["crossings"] == 2 else None)
        C.append(("blind-" + str(row["crossings"]),
                  (str(row["crossings"]), str(row["placements"]),
                   str(row["arenas"]),
                   str(sw) if sw is not None else "not run",
                   row["verdict"])))
    C.append(("grid-h", ("target", "declared links", "declaration fiber",
                         "reading", "count leg", "the baseline record",
                         "with the driven crossing")))
    for row in R["extension_grid"]:
        C.append(("grid-" + row["target"] + row["reading"] +
                  row["count_leg"],
                  (canon(row["target"]), str(row["declared_links"]),
                   str(row["declaration_fiber"]), row["reading"],
                   row["count_leg"], row["baseline"],
                   row["with_the_driven_crossing"])))
    C.append(("census-h", ("type", "gluings", "carriers", "realised pairs",
                           "doubled")))
    for row in R["census"]:
        C.append(("census-" + row["type"],
                  (canon(row["type"]), str(row["gluings"]), str(row["n"]),
                   str(row["E"]), str(row["doubled"]))))
    C.append(("prov-h", ("id", "path", "sha256-12")))
    for row in R["provenance"]:
        C.append(("prov-" + row["id"],
                  (row["id"], row["path"], row["sha256_12"])))
    for row in R["cited_not_read"]["objects"]:
        C.append(("cnr-" + row["path"],
                  ("DECLARED, NOT READ", row["path"], row["sha256_12"])))
    C.append(("arena-h", ("row", "value")))
    for k in ("boundary", "family", "law", "state", "arena_axes",
              "provenance"):
        C.append(("arena-" + k,
                  (k.replace("_", " "), canon(R["standards"]["arena"][k]))))
    C.append(("window-h", ("axis", "members", "the delivered value")))
    for row in R["window"]["axes"]:
        C.append(("window-" + row["axis"],
                  (row["axis"], canon(", ".join(row["members"])),
                   canon(row["delivered"]))))
    C.append(("choice-h", ("item", "class", "fiber", "where it binds")))
    for row in R["choices"]:
        C.append(("choice-" + row["item"],
                  (canon(row["item"]), canon(row["cls"]),
                   canon(row["fiber"]), canon(row["binds"]))))
    # every claim cell is normalised by the SAME normaliser the paper's own
    # rows go through, so the comparison is like for like at every cell
    return [(cid, cn(*cells)) for cid, cells in C]


def check_claims(R, text):
    C = paper_claims(R)
    want = Counter(t for _i, t in C)
    got = Counter(table_rows(text))
    missing = [list(k) for k in want if got[k] < want[k]]
    stray = [list(k) for k in got if k not in want]
    return {"claims": len(C), "paper_rows": sum(got.values()),
            "missing": missing[:12], "n_missing": len(missing),
            "stray": stray[:12], "n_stray": len(stray),
            "ok": not missing and not stray}


def paper_coverage(R, text, verdict):
    reg2 = set(NUMREG)
    for v in verdict:
        for m in NUM_RE.finditer(v):
            reg2.add(m.group(0))

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
            reg2.add(str(o))
            reg2.add("{:,}".format(o))
        elif isinstance(o, str):
            if PURE_NUM.match(o.strip()):
                for m in NUM_RE.finditer(o):
                    reg2.add(m.group(0))
    walk(R)
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
    if mut("MUT-PAPER-NUM"):
        reg2 = {t for t in reg2 if t.replace(",", "") != "455"}
    flat = {s.replace(",", "") for s in reg2}
    scanned, unbacked = 0, []
    for m in NUM_RE.finditer(text):
        tok = m.group(0)
        scanned += 1
        if tok in reg2 or tok.replace(",", "") in flat or tok in struct:
            continue
        unbacked.append(tok)
    return {"scanned": scanned, "unbacked": sorted(set(unbacked)),
            "registry": len(flat), "registry_set": flat}


def paper_fences(text, verdict):
    blocks = re.findall(r"```[a-zA-Z0-9]*\n(.*?)```", text, re.S)
    got = Counter(norm(b) for b in blocks)
    want = Counter(norm(v) for v in verdict)
    missing = [k[:60] for k in want if got[k] < want[k]]
    stray = [k[:60] for k in got if k not in want]
    return {"ok": not missing and not stray, "blocks": len(blocks),
            "verdict_segments": len(want), "missing": missing,
            "stray": stray}


def paper_polarity(text):
    bad, rows = [], []
    for (pid, pos, neg) in POLARITY:
        gp, gn = locate(text, pos), locate(text, neg)
        rows.append({"id": pid, "positive": gp, "negation": gn})
        if gp < 1 or gn > 0:
            bad.append(pid)
    return {"ok": not bad, "checked": len(POLARITY), "bad": bad,
            "rows": rows}


def paper_spelled(text, reg2):
    low = canon(text).lower()
    seen, bad = [], []
    for word, val in sorted(SPELLED.items(), key=lambda kv: -len(kv[0])):
        if re.search(r"(?<![\w-])" + re.escape(word) + r"(?![\w-])", low):
            seen.append(word)
            if str(val) not in reg2:
                bad.append(word)
    return {"ok": not bad, "spelled_found": seen, "unbacked": bad}


# ===========================================================================
# SECTION 9.  RENDERING, SEALING, DELIVERY
# ===========================================================================

def render(R, V, LD):
    say("=" * 78)
    say("v14 SEC-2 -- THE DYNAMICS OF GLUING")
    say("instrument for %s   schema %s" % (PAPER_REL, SCHEMA))
    say("=" * 78)
    say()
    say("PROVENANCE: %d sources read, all sha256-12 verified."
        % len(R["provenance"]))
    for p in R["provenance"]:
        say("  %-8s %-42s %s" % (p["id"], p["path"], p["sha256_12"]))
    say("  DECLARED AND NOT READ (worktree under repair): the #301 SEC "
        "objects at commit")
    say("  %s --" % SEC301["commit"][:12])
    for o in R["cited_not_read"]["objects"]:
        say("     %-32s %s" % (o["path"], o["sha256_12"]))
    say()
    say("-- M1: SEAM SELECTION " + "-" * 55)
    ss = R["seam_selection"]
    say("  the seam census: %d seam types over %d shared sites; the vector "
        "(2, 2, 2) never occurs" % (ss["seam_types"],
                                    R["seam_census"]["shared_sites"]))
    say("  the completion space: rank %d on %d unknowns, kernel %d, by the "
        "chart alone" % (ss["rank"], ss["unknowns"], ss["kernel_dim"]))
    say()
    say("  %-24s %8s %7s %7s %7s" % ("seam type", "sites", "lattice",
                                     "posdef", "parity"))
    for row in R["completion_lattice"][:8]:
        say("  %-24s %8d %7d %7d %7d"
            % (row["seam"], row["population"], row["lattice"],
               row["posdef"], row["parity_stable"]))
    say("  ... %d rows in all, every one in the receipt"
        % len(R["completion_lattice"]))
    say()
    say("  positivity selects nothing (min positive-definite count over the "
        "49 seam types: %d)"
        % min(r["posdef"] for r in R["completion_lattice"]))
    say("  price minimisation selects nothing: the two-sided budget is "
        "constant at every seam type")
    say("  refinement stability: ceiling %d at this record; as a "
        "hypothetical, empty at %d of %d"
        % (ss["refinement_ceiling"], ss["refinement_empty_at"],
           ss["seam_types"]))
    say("  the determinant DOES select the direct sum, uniquely, at %d of "
        "%d -- named, not licensed"
        % (ss["determinant_selects_the_direct_sum_at"], ss["seam_types"]))
    say("  SEC's indefinite witness reproduces (%s) and is NOT admissible: "
        "%d cross counts below one"
        % (R["sec_witness"]["value"],
           len(R["sec_witness"]["cross_counts_below_one"])))
    say("  the driven crossing cuts the aligned lattice %d -> %d and "
        "EXCLUDES the direct sum (%s)"
        % (ss["aligned_lattice"], ss["aligned_after_crossing"],
           ss["direct_sum_after_crossing"]))
    say()
    say("-- M2: THE DICTIONARY EXTENSION " + "-" * 45)
    lw = R["lawfulness"]
    say("  three-actor groups: %d in %d orbits; seam-spanning %d, every one "
        "dead at the delivered target"
        % (sum(r["orbit_size"] for r in R["group_census"]), lw["orbits"],
           lw["seam_spanning_groups"]))
    say("  lawful at the matched extension: %d of %d; motivated at %d"
        % (lw["lawful"], lw["seam_spanning_groups"], lw["motivated"]))
    say("  %-30s %5s %6s %6s %6s %6s %s"
        % ("arena", "links", "maps", "site", "label", "orient", "fate"))
    for row in R["inventories"]:
        say("  %-30s %5d %6d %6d %6d %6d %s"
            % (row["arena"][:30], row["declared_cross_links"], row["maps"],
               row["I-SITE-ASSIGNMENT"], row["I-DIRECTION-LABEL"],
               row["I-ORIENT"], row["fate"]))
    say()
    say("  blindness: %s"
        % "; ".join("%d crossing(s): %d placements, %d arena(s), %s"
                    % (r["crossings"], r["placements"], r["arenas"],
                       r["verdict"]) for r in R["blindness"]["rows"]))
    say()
    say("-- M3: THE COMPOSITE PRICE " + "-" * 50)
    say("  %-42s %6s %-12s %-8s %s"
        % ("currency", "lone", "composite", "excess", "verdict"))
    for row in R["price"]["rows"]:
        say("  %-42s %6s %-12s %-8s %s"
            % (row["currency"], row["lone_sector"], row["composite"],
               row["excess"], row["verdict"]))
    say("  violations over all %d composites: %d"
        % (R["price"]["gluings"], R["price"]["violations"]))
    say()
    say("-- GATES " + "-" * 68)
    for r in LD.rows:
        say("    %-34s %s %s" % (r["gate"], "PASS" if r["ok"] else "FAIL",
                                 r["digest"]))
    say()
    say("-- VERDICT " + "-" * 66)
    say()
    for v in V:
        say(v)
        say()
    say("=" * 78)


def finish(LD, SEAL, R, V, ptext, t0, write=True, swept=False):
    # ---- coverage: every gate falsified or waived with a forcing
    gates = LD.names()
    targets = {m[1] for m in MUTANTS}
    uncovered = [g for g in gates if g not in targets and g not in WAIVERS
                 and g not in LATER_GATES]
    unreached = [m[0] for m in MUTANTS
                 if m[1] not in gates and m[1] not in LATER_GATES]
    # E-23: the falsifier's published description must match its code
    src = read_bytes(SELF_REL).decode()
    READLOG.pop()
    # E-23, and not the vacuous form of it: a mutant's name occurring in its
    # own declaration proves nothing.  Every declared falsifier must have an
    # INJECTION SITE -- a mut("NAME") or pick("NAME", ...) call in this file --
    # or it is a falsifier that cannot fire.
    desc_bad = [m[0] for m in MUTANTS
                if ('mut("%s")' % m[0]) not in src
                and ('pick("%s"' % m[0]) not in src]
    LD.gate("G-COVERAGE",
            not uncovered and not unreached and not desc_bad,
            "every gate is falsified by one of the declared mutants, each "
            "dying at its own named gate, or waived with a machine-checked "
            "forcing; every declared mutant's target gate exists in this "
            "run, so no falsifier is dead code; and every mutant's published "
            "description is verified against its own name in the source "
            "(E-23)",
            {"gates": len(gates), "mutants": len(MUTANTS),
             "waived": sorted(WAIVERS), "uncovered": uncovered,
             "unreached": unreached, "description_mismatch": desc_bad})
    R["coverage"] = SEAL.seal("coverage", {
        "gates": gates, "mutants": [m[0] for m in MUTANTS],
        "waivers": {k: v for k, v in WAIVERS.items()},
        "later_gates": list(LATER_GATES)})

    # ---- the verdict comparator
    again = reconstruct(R)
    same = [a == b for a, b in zip(V, again)]
    if mut("MUT-VERDICT"):
        same[0] = False
    LD.gate("G-VERDICT-RECON",
            all(same) and len(again) == len(V),
            "the head is derived a second time by a comparator that types "
            "all four templates itself and re-reads every value from the "
            "receipt's own measured rows, sharing no format string, no "
            "helper and no typed literal with the builder; the complete "
            "strings are compared for equality",
            {"segments": len(V), "agree": sum(1 for s in same if s)})

    # ---- the paper gates, IN the plain run
    LD.gate("G-PAPER-PRESENT",
            bool(ptext) or not PAPER_REQUIRED[0],
            "the paper is part of the delivered object: a run that writes "
            "artifacts, and every run of the mutant sweep inside it, must "
            "have the paper in hand, so the paper leg can never pass by "
            "being absent",
            {"present": bool(ptext), "required": PAPER_REQUIRED[0],
             "path": PAPER_REL})
    if ptext:
        cl = check_claims(R, ptext)
        if mut("MUT-PAPER-CLAIM"):
            cl = {"ok": False, "claims": cl["claims"], "n_missing": 1,
                  "missing": [["forged"]], "n_stray": 0, "stray": [],
                  "paper_rows": cl["paper_rows"]}
        LD.gate("G-PAPER-CLAIMS", cl["ok"],
                "every data row AND every header row of every table in the "
                "paper is a rendered claim of this receipt, compared as a "
                "multiset in both directions, so a swapped cell dies and so "
                "does a forged extra row",
                cl)
        cov = paper_coverage(R, ptext, V)
        # the registry SET leaves the evidence before the gate seals it: a
        # set reaches json only through str(), which is hash-order dependent,
        # and a gate digest that moves with the hash seed is not a digest
        regset = cov.pop("registry_set")
        LD.gate("G-PAPER-COVERAGE", not cov["unbacked"],
                "every numeral in the paper -- fenced blocks, verdict "
                "blocks, tables and inline code spans included, nothing "
                "stripped -- is backed by a measured value of this run or by "
                "the paper's own section numbering (E-22)",
                cov)
        fen = paper_fences(ptext, V)
        LD.gate("G-PAPER-FENCE", fen["ok"],
                "the paper's fenced blocks are compared as a MULTISET "
                "against this run's verdict segments, so neither a stale "
                "verdict nor a forged twin beside the clean one survives",
                fen)
        pol = paper_polarity(ptext)
        LD.gate("G-PAPER-POLARITY", pol["ok"],
                "each polarity row carries its own negation, so the gate "
                "tests the sign it names: the paper must assert the measured "
                "direction and must nowhere assert its inverse",
                pol)
        sp = paper_spelled(ptext, regset)
        LD.gate("G-PAPER-SPELLED", sp["ok"],
                "a numeral spelled in words above twelve is a claim like any "
                "other and must have its integer in the measured registry",
                sp)
        R["paper"] = SEAL.seal("paper", {
            "path": PAPER_REL, "claims": cl["claims"],
            "rows": cl["paper_rows"], "numerals": cov["scanned"],
            "fenced_blocks": fen["blocks"], "polarity": pol["checked"],
            "spelled": sp["spelled_found"]})
    else:
        R["paper"] = SEAL.seal("paper", {"path": PAPER_REL,
                                         "present": False})

    R["totals"] = SEAL.seal("totals", {
        "gates": len(LD.rows), "mutants": len(MUTANTS),
        "sources_read": len(SOURCES), "anchors": len(R["anchors"]),
        "seam_types": R["seam_selection"]["seam_types"],
        "gluings": R["price"]["gluings"]})
    R["ledger"] = [{k: v for k, v in r.items()} for r in LD.rows]
    R["ledger_chain"] = LD.chain[:16]
    R["swept"] = swept
    SEAL.declare_unsealed("ledger", "the gate ledger is the sealing "
                          "mechanism itself and is chained instead")
    SEAL.declare_unsealed("ledger_chain", "the chain head of the ledger")
    SEAL.declare_unsealed("seal_manifest", "the manifest cannot seal itself")
    SEAL.declare_unsealed("swept", "set by the harness that runs the sweep")
    SEAL.declare_unsealed("schema", "a constant of the instrument")
    SEAL.declare_unsealed("schema_version", "a constant of the instrument")
    SEAL.declare_unsealed("unit", "a constant of the instrument")
    SEAL.declare_unsealed("pin", "the frozen pin's own coordinates")
    SEAL.declare_unsealed("mutant_sweep", "written by the sweep harness "
                          "after the last gate; bound by G-SWEEP-EXECUTED")
    R["seal_manifest"] = SEAL.manifest()

    LD.gate("G-SWEEP-EXECUTED",
            (not write) or swept,
            "the only writer in this file is downstream of a mutant sweep "
            "that actually ran: a delivery run that has not swept cannot "
            "reach the artifacts",
            {"write": write, "swept": swept})
    keys = set(R) - {"seal_manifest"}
    covered = set(SEAL.seals) | set(SEAL.unsealed)
    LD.gate("G-SEAL-COMPLETE",
            keys <= covered,
            "the seal manifest is TOTAL: every published receipt key is "
            "either digested at the gate that vouched its own values or "
            "named in the manifest with the reason it cannot be",
            {"keys": len(keys), "sealed": len(SEAL.seals),
             "unsealed": len(SEAL.unsealed),
             "uncovered": sorted(keys - covered)})
    late_present = [g for g in LATER_GATES if g in LD.names()]
    want_late = ["G-VERDICT-RECON", "G-PAPER-PRESENT", "G-SWEEP-EXECUTED",
                 "G-SEAL-COMPLETE"] + (
                     ["G-PAPER-CLAIMS", "G-PAPER-COVERAGE", "G-PAPER-FENCE",
                      "G-PAPER-POLARITY", "G-PAPER-SPELLED"] if ptext
                     else [])
    LD.gate("G-DECLARED-LATER",
            all(g in late_present for g in want_late),
            "the gates emitted after the coverage gate are declared in "
            "advance and their presence is checked at the last gate, and "
            "when the paper is in hand every paper gate is among them",
            {"declared_later": list(LATER_GATES), "present": late_present,
             "required_here": want_late})
    return R


def write_artifacts(R, V, LD):
    render(R, V, LD)
    payload = json.dumps(R, indent=1, sort_keys=True, default=str)
    outtext = "\n".join(OUTBUF) + "\n"
    seal_out = hashlib.sha256(outtext.encode()).hexdigest()
    seal_rec = hashlib.sha256(payload.encode()).hexdigest()
    for rel, data, sealed in ((OUT_REL, outtext, seal_out),
                              (REC_REL, payload, seal_rec)):
        path = os.path.join(ROOT, rel)
        tmp = path + ".tmp"
        with open(tmp, "w") as fh:
            fh.write(data)
        with open(tmp, "rb") as fh:
            back = fh.read()
        if hashlib.sha256(back).hexdigest() != sealed:
            os.unlink(tmp)
            raise GateFail("G-INTEGRITY: %s read back does not match its "
                           "gate-time seal" % rel)
        os.replace(tmp, path)
    for rel, sealed in ((OUT_REL, seal_out), (REC_REL, seal_rec)):
        with open(os.path.join(ROOT, rel), "rb") as fh:
            if hashlib.sha256(fh.read()).hexdigest() != sealed:
                raise GateFail("G-INTEGRITY: %s on disk does not match its "
                               "gate-time seal" % rel)
    return seal_out, seal_rec


# ===========================================================================
# SECTION 10.  THE CLI
# ===========================================================================

class _Sink:
    def write(self, *a, **k):
        pass

    def flush(self):
        pass


def run_mutant(name):
    ACTIVE_MUTANT[0] = name
    PAPER_REQUIRED[0] = True
    old = sys.stdout
    sys.stdout = _Sink()
    del OUTBUF[:]
    try:
        LD, SEAL, R, V, ptext, t0 = full_run()
        finish(LD, SEAL, R, V, ptext, t0, write=False, swept=True)
        return None
    except GateFail as e:
        return str(e).split(":")[0]
    except Exception as e:
        return "CRASH/" + type(e).__name__
    finally:
        sys.stdout = old
        ACTIVE_MUTANT[0] = None
        del OUTBUF[:]


FLAGS = {"--no-write": 0, "--numbers": 0, "--selftest": 0, "--mutant": 1,
         "--break-anchor": 1, "--verify-paper": "opt", "--verify-sec": 1,
         "--list-gates": 0, "--list-mutants": 0}
MODES = ("--numbers", "--selftest", "--mutant", "--break-anchor",
         "--verify-paper", "--verify-sec", "--list-gates", "--list-mutants")


def parse_args(argv):
    out, i = {}, 0
    seen_mode = None
    while i < len(argv):
        a = argv[i]
        if a not in FLAGS:
            sys.stderr.write("unknown flag: %s\n" % a)
            sys.exit(EXIT_USAGE)
        if a in MODES:
            if seen_mode is not None:
                sys.stderr.write("two mode flags: %s and %s\n"
                                 % (seen_mode, a))
                sys.exit(EXIT_USAGE)
            seen_mode = a
        need = FLAGS[a]
        if need == 0:
            out[a] = True
            i += 1
            continue
        nxt = argv[i + 1] if i + 1 < len(argv) else None
        if need == 1:
            if nxt is None or nxt.startswith("--"):
                sys.stderr.write("flag %s needs an argument\n" % a)
                sys.exit(EXIT_USAGE)
            out[a] = nxt
            i += 2
            continue
        if nxt is None or nxt.startswith("--"):
            out[a] = None
            i += 1
        else:
            out[a] = nxt
            i += 2
    return out


def main(argv=None):
    args = parse_args(sys.argv[1:] if argv is None else argv)
    if "--list-gates" in args:
        LD, SEAL, R, V, ptext, t0 = full_run()
        for g in LD.names():
            print(g)
        return EXIT_OK
    if "--list-mutants" in args:
        for (n, g, why) in MUTANTS:
            print("%-24s %-30s %s" % (n, g, why))
        return EXIT_OK
    if "--verify-sec" in args:
        d = args["--verify-sec"]
        bad = []
        for (rel, sha) in SEC301["objects"]:
            p = os.path.join(d, os.path.basename(rel))
            if not os.path.exists(p):
                bad.append((rel, "absent"))
                continue
            with open(p, "rb") as fh:
                got = sha12(fh.read())
            print("%-32s declared %s got %s %s"
                  % (os.path.basename(rel), sha, got,
                     "OK" if got == sha else "MISMATCH"))
            if got != sha:
                bad.append((rel, got))
        print("verify-sec: %d objects, %d mismatched"
              % (len(SEC301["objects"]), len(bad)))
        return EXIT_OK if not bad else EXIT_FAIL
    if "--mutant" in args:
        name = args["--mutant"]
        if name not in {m[0] for m in MUTANTS}:
            sys.stderr.write("unknown mutant: %s\n" % name)
            return EXIT_USAGE
        died = run_mutant(name)
        want = [m[1] for m in MUTANTS if m[0] == name][0]
        print("mutant %s died at %s (declared %s): %s"
              % (name, died, want, "ON TARGET" if died == want
                 else "OFF TARGET"))
        return EXIT_OK if died == want else EXIT_FAIL
    if "--break-anchor" in args:
        BROKEN_ANCHOR[0] = args["--break-anchor"]
        if BROKEN_ANCHOR[0] not in {v[0] for v in VERBATIM}:
            sys.stderr.write("unknown anchor: %s\n" % BROKEN_ANCHOR[0])
            return EXIT_USAGE
        try:
            LD, SEAL, R, V, ptext, t0 = full_run()
            finish(LD, SEAL, R, V, ptext, t0, write=False, swept=True)
        except GateFail as e:
            print("BROKEN ANCHOR %s: %s" % (BROKEN_ANCHOR[0], e))
            return EXIT_FAIL
        print("BROKEN ANCHOR %s SURVIVED -- the anchor is not gated"
              % BROKEN_ANCHOR[0])
        return EXIT_OK
    if "--selftest" in args:
        before = {}
        for rel in (OUT_REL, REC_REL):
            p = os.path.join(ROOT, rel)
            before[rel] = (hashlib.sha256(open(p, "rb").read()).hexdigest()
                           if os.path.exists(p) else None)
        rows = []
        for (nid, _s, _n, _c) in VERBATIM:
            BROKEN_ANCHOR[0] = nid
            try:
                LD, SEAL, R, V, ptext, t0 = full_run()
                finish(LD, SEAL, R, V, ptext, t0, write=False, swept=True)
                rows.append((nid, "SURVIVED"))
            except GateFail as e:
                rows.append((nid, str(e).split(":")[0]))
            finally:
                BROKEN_ANCHOR[0] = None
            del OUTBUF[:]
        after = {}
        for rel in (OUT_REL, REC_REL):
            p = os.path.join(ROOT, rel)
            after[rel] = (hashlib.sha256(open(p, "rb").read()).hexdigest()
                          if os.path.exists(p) else None)
        ok = all(r[1] == "G-ANCHORS" for r in rows) and before == after
        for (nid, died) in rows:
            print("  anchor %-20s -> %s" % (nid, died))
        print("SELFTEST %s: %d anchors, artifacts unchanged %s"
              % ("PASS" if ok else "FAIL", len(rows), before == after))
        return EXIT_OK if ok else EXIT_FAIL
    if "--verify-paper" in args:
        rel = args["--verify-paper"] or PAPER_REL
        p = rel if os.path.isabs(rel) else os.path.join(ROOT, rel)
        with open(p) as fh:
            ptext = fh.read()
        try:
            LD, SEAL, R, V, _pt, t0 = full_run(paper_text=ptext)
            finish(LD, SEAL, R, V, ptext, t0, write=False, swept=True)
        except GateFail as e:
            print("VERIFY-PAPER FAIL: %s" % e)
            return EXIT_FAIL
        print("VERIFY-PAPER PASS: %s" % rel)
        return EXIT_OK

    write = "--no-write" not in args and "--numbers" not in args
    LD, SEAL, R, V, ptext, t0 = full_run()
    if "--numbers" in args:
        finish(LD, SEAL, R, V, ptext, t0, write=False, swept=True)
        print(json.dumps({k: R[k] for k in sorted(R)
                          if k not in ("ledger", "seal_manifest")},
                         indent=1, sort_keys=True, default=str))
        return EXIT_OK
    swept = False
    sweep_rows = []
    if write:
        for (name, target, _why) in MUTANTS:
            died = run_mutant(name)
            sweep_rows.append({"mutant": name, "declared": target,
                               "died_at": died,
                               "on_target": died == target})
        off = [r["mutant"] for r in sweep_rows if not r["on_target"]]
        if off:
            sys.stderr.write("MUTANT SWEEP OFF TARGET: %s\n" % off)
            return EXIT_FAIL
        swept = True
        LD, SEAL, R, V, ptext, t0 = full_run()
        R["mutant_sweep"] = sweep_rows
    finish(LD, SEAL, R, V, ptext, t0, write=write, swept=swept or not write)
    if write:
        write_artifacts(R, V, LD)
        print("\nwrote %s and %s   [%.1fs]" % (OUT_REL, REC_REL,
                                               time.time() - t0))
    else:
        render(R, V, LD)
    return EXIT_OK


if __name__ == "__main__":
    try:
        sys.exit(main())
    except GateFail as exc:
        sys.stderr.write("GATE FAILED -- %s\n" % exc)
        sys.exit(EXIT_FAIL)
