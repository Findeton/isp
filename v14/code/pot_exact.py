#!/usr/bin/env python3
"""POT (paper-36) -- THE POTENTIAL UNIT: the loop family, the discriminator,
the price binding and the spectral door, on the record-borne gauge arena.

Built against the frozen pin v14/note-pot-pin.md.  Exact arithmetic only:
the field is Q(zeta_8) carried as integer four-tuples over the basis
(1, z, z^2, z^3) reduced modulo z^4 + 1, with a per-row power-of-two scale;
every expectation is a ratio of exact rational sums; no logarithm, no
exponential and no square root is called anywhere in this source, which is a
gate rather than a promise.

The four artifacts are v14/paper-36-pot.md, this file, v14/code/pot_output.txt
and v14/code/pot_receipt.json.  The delivery run is the only writer.
"""

import ast
import hashlib
import json
import os
import sys
from fractions import Fraction

QUIET = False
MUT = None
LOG = []


def say(msg=""):
    """--quiet suppresses the TERMINAL ECHO ONLY.  The transcript is a
    published artifact, so it accumulates whatever the flag says: a flag that
    changed the delivered bytes would be a byte-reproducibility hazard
    wearing a convenience label."""
    LOG.append(msg)
    if not QUIET:
        print(msg, flush=True)


def mut(name):
    """the ONLY mutant switch.  No gate predicate may reference it."""
    return MUT == name


def digest(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, default=str).encode()).hexdigest()[:12]


def bdigest(b):
    return hashlib.sha256(b).hexdigest()[:12]


def own_source():
    """the instrument's OWN source text, as the AST gates read it.  The
    source-planting mutants insert a real definition into exactly this text,
    so what they falsify is the object a gate measures and not the gate's own
    verdict variable."""
    src = open(os.path.abspath(__file__), "rb").read().decode()
    if mut("MUT-GHOST-FUNCTION"):
        src = src + "\n\ndef ghost_helper(S):\n    return Fraction(5, 9)\n"
    if mut("MUT-REGISTRY-EVASION"):
        src = src + "\n\n_gn = 'MUT-' + 'GHOST'\nif mut(_gn):\n    pass\n"
    if mut("MUT-AST-BLIND"):
        src = src + "\n\n_EPSILON_FLOAT = 1e-12\n"
    return src


# ===========================================================================
# SECTION 1.  THE EXACT FIELD Q(zeta_8)
# ===========================================================================
# A field element is an integer four-tuple (a0, a1, a2, a3) standing for
# a0 + a1 z + a2 z^2 + a3 z^3 SCALED by a power of two carried outside it.
# Coin entries are exactly the half-integer combinations, so every coin entry
# doubled is integral; carrying the scale per matrix row keeps the whole
# holonomy census in machine integers and makes tuple equality field equality
# once the scales agree.  Traces leave this section as Fraction four-tuples.

IZ = (0, 0, 0, 0)
IONE = (1, 0, 0, 0)


def imul(a, b):
    """multiplication modulo z^4 + 1, written out."""
    a0, a1, a2, a3 = a
    b0, b1, b2, b3 = b
    return (a0 * b0 - (a1 * b3 + a2 * b2 + a3 * b1),
            a0 * b1 + a1 * b0 - (a2 * b3 + a3 * b2),
            a0 * b2 + a1 * b1 + a2 * b0 - a3 * b3,
            a0 * b3 + a1 * b2 + a2 * b1 + a3 * b0)


def iadd(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2], a[3] + b[3])


def iconj(a):
    """conj(z) = -z^3, conj(z^2) = -z^2, conj(z^3) = -z."""
    return (a[0], -a[3], -a[2], -a[1])


def ishift(a, d):
    return (a[0] << d, a[1] << d, a[2] << d, a[3] << d)


def izpow(t):
    t %= 8
    v = [0, 0, 0, 0]
    if t < 4:
        v[t] = 1
    else:
        v[t - 4] = -1
    return (v[0], v[1], v[2], v[3])


SQRT2 = (0, 1, 0, -1)                      # z - z^3 = sqrt 2


def in_real_subfield(t):
    """an element of Q(sqrt 2) inside Q(zeta_8): the z^2 coefficient vanishes
    and the z and z^3 coefficients are opposite, since sqrt 2 = z - z^3."""
    return t[2] == 0 and t[1] == -t[3]


def qs(t):
    """the pair (p, q) meaning p + q sqrt 2, for an element already measured
    to lie in the real subfield."""
    return (t[0], t[1])


def sym_qs(t):
    """THE CONJUGATION-SYMMETRIC PART of a trace, which is the parent's own
    admissible object: (t + conj t)/2 lies in the fixed field of the
    conjugation, and that field is Q(sqrt 2), so the value is a pair by
    construction and not by luck.  Where the raw trace is already real the
    restriction costs nothing, and how often that happens is measured."""
    return (t[0], (t[1] - t[3]) / 2)


def qs_add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def qs_mul(x, y):
    return (x[0] * y[0] + 2 * x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def qs_is_zero(x):
    return x[0] == 0 and x[1] == 0


def qs_div(x, y):
    """exact division in Q(sqrt 2) by the conjugate; the caller has already
    gated the denominator non-zero."""
    p, q = x
    r, s = y
    d = r * r - 2 * s * s
    return ((p * r - 2 * q * s) / d, (q * r - p * s) / d)


def qs_less(x, y):
    """the real order on Q(sqrt 2), decided by integer comparison alone: no
    square root is extracted anywhere."""
    dp = x[0] - y[0]
    dq = x[1] - y[1]
    if dq == 0:
        return dp < 0
    if dp <= 0 and dq < 0:
        return True
    if dp >= 0 and dq > 0:
        return False
    return (dq < 0) == (dp * dp < 2 * dq * dq)


def qs_str(x):
    """the canonical rendering: the rational part alone where the surd part
    vanishes, and p+q*sqrt2 otherwise."""
    if x[1] == 0:
        return str(x[0])
    return "%s+%s*sqrt2" % (x[0], x[1])


NUMWORD_UNITS = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
                 "six": 6, "seven": 7, "eight": 8, "nine": 9}
NUMWORD_TEENS = {"ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13,
                 "fourteen": 14, "fifteen": 15, "sixteen": 16,
                 "seventeen": 17, "eighteen": 18, "nineteen": 19}
NUMWORD_TENS = {"twenty": 20, "thirty": 30, "forty": 40, "fifty": 50,
                "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90}
NUMWORD_SCALES = {"hundred": 100, "thousand": 1000}


# ===========================================================================
# SECTION 2.  THE CHAINED GATE LEDGER AND THE TOTAL SEAL
# ===========================================================================

class GateFail(Exception):
    pass


class Ledger:
    """every gate is a row; every row carries the digest of its predecessor,
    so a row edited after its gate closed no longer matches the chain, and
    the chain is VERIFIED in the run and again from the bytes read back."""

    def __init__(self):
        self.rows = []
        self.ids = []
        self.chain = "GENESIS"

    def gate(self, gid, claim, ok, detail="", kind="MEASURED"):
        if gid in self.ids:
            raise GateFail("%s :: duplicate gate id" % gid)
        row = {"gate": gid, "claim": claim, "passed": bool(ok),
               "detail": detail, "kind": kind, "prev": self.chain}
        row["link"] = digest(row)
        self.chain = row["link"]
        self.rows.append(row)
        self.ids.append(gid)
        say("  [%s] %s :: %s" % ("PASS" if ok else "FAIL", gid, detail))
        if not ok:
            raise GateFail("%s :: %s" % (gid, detail))
        return True

    def verify_chain(self, rows=None):
        rows = self.rows if rows is None else rows
        prev = "GENESIS"
        for r in rows:
            body = {k: r[k] for k in
                    ("gate", "claim", "passed", "detail", "kind", "prev")}
            if r["prev"] != prev or digest(body) != r["link"]:
                return False
            prev = r["link"]
        return True


class Seal:
    """#119, native and TOTAL: every published object is digested at the very
    moment the gate that vouches ITS OWN VALUES passes; the manifest is total
    over the receipt's top-level keys; the artifacts are written to
    temporaries, read back and compared against the gate-time digests BEFORE
    either is moved into place."""

    def __init__(self):
        self.rows = []

    @staticmethod
    def resolve(payload, key):
        obj = payload
        for part in key.split("/"):
            obj = obj[int(part)] if isinstance(obj, list) else obj[part]
        return obj

    def take(self, name, key, gate, obj):
        self.rows.append({"object": name, "receipt_key": key,
                          "vouching_gate": gate, "digest": digest(obj)})

    def reverify(self, payload):
        bad = []
        for r in self.rows:
            try:
                got = digest(self.resolve(payload, r["receipt_key"]))
            except (KeyError, IndexError, TypeError):
                bad.append((r["receipt_key"], "MISSING"))
                continue
            if got != r["digest"]:
                bad.append((r["receipt_key"], got))
        return bad


LD = Ledger()
SEAL = Seal()

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.dirname(ROOT)

PAPER_REL = "v14/paper-36-pot.md"
OUT_REL = "v14/code/pot_output.txt"
RECEIPT_REL = "v14/code/pot_receipt.json"

SOURCES = [
    ("S-PIN", "v14/note-pot-pin.md", "df2f15efa7b0",
     "THE PIN, frozen before this instrument existed"),
    ("S-ACT-PAPER", "v14/paper-34-act.md", "d933221780ed",
     "PARENT 1, ACT terminal: the allowed weight systems, the coupling "
     "inventory, the extreme points, the odd twist, the merging-index law "
     "and the loop-family obligation this unit discharges"),
    ("S-ACT-CODE", "v14/code/act_exact.py", "a90559ee0e0f",
     "PARENT 1's instrument -- read for its declared definitions only; "
     "nothing is imported from it"),
    ("S-ACT-RECEIPT", "v14/code/act_receipt.json", "7fd1267bddc7",
     "PARENT 1's receipt: the census counts, the class profile, the extreme "
     "point split, the expectations and the law-native stamp"),
    ("S-SMU-PAPER", "v14/paper-27-smu.md", "6df0db523d32",
     "PARENT 2, SMU terminal: the conserved price frame and the law-native "
     "control whose stamp is carried verbatim and never spent"),
    ("S-P23-PAPER", "v14/paper-23-measure.md", "79cc67b4f6cd",
     "PARENT 3, paper-23 terminal: the withholding machinery this unit "
     "inverts, and the transitivity criterion"),
    ("S-R5-PAPER", "v14/paper-18-gauge-rung.md", "62cfe5689d2c",
     "PARENT 4, R5 terminal: the lattice, the link operator, the holonomy "
     "definition this unit rebuilds, and the loop family it named absent"),
    ("S-R5-CODE", "v14/code/r5_gauge_exact.py", "0d98de793b79",
     "PARENT 4's instrument -- read for its declared definitions only"),
    ("S-R5-RECEIPT", "v14/code/r5_gauge_receipt.json", "0c02b7684e5b",
     "PARENT 4's receipt: the curvature census and the arena cardinalities"),
]

BANNED_NAMES = ["subprocess", "numpy", "random", "scipy", "math", "decimal"]
BANNED_CALLS = ["system", "popen", "check_output", "urlopen", "log", "exp",
                "sqrt", "log2", "log10", "pow", "isqrt"]


def read_bytes(rel):
    p = os.path.join(REPO, rel)
    if not os.path.exists(p):
        return None
    with open(p, "rb") as fh:
        return fh.read()


def load_sources():
    got, rows = {}, []
    for name, rel, sha, what in SOURCES:
        b = read_bytes(rel)
        d = bdigest(b) if b is not None else "ABSENT-AT-ITS-PINNED-PATH"
        if mut("MUT-SOURCE-SWAP") and name == "S-ACT-RECEIPT":
            d = bdigest(read_bytes("v14/paper-34-act.md") or b"")
        got[name] = b
        rows.append({"anchor": name, "path": rel, "expected": sha,
                     "measured": d, "agrees": d == sha, "what": what})
    ok = all(r["agrees"] for r in rows)
    LD.gate("G-SOURCES-AT-THEIR-PINNED-DIGESTS",
            "every parent this unit reads is verified BY ITS OWN PATH "
            "against a digest frozen in the pin, so a pair of sources "
            "exchanged between two paths stops matching and the delivery "
            "run refuses; a source absent at its pinned path is a named "
            "gate failure and not an uncaught traceback",
            ok,
            "%d sources, %d at their pinned digests"
            % (len(rows), sum(1 for r in rows if r["agrees"])))
    SEAL.take("THE PROVENANCE", "provenance",
              "G-SOURCES-AT-THEIR-PINNED-DIGESTS", rows)
    return got, rows


# ===========================================================================
# SECTION 3.  THE PATH-VALUE AND VERBATIM ANCHORS
# ===========================================================================
# An anchor is a (path, value) pair or a (window, consumer) pair, never only
# a file digest: a parent whose bytes match but whose named field has moved
# stops the run, and a window is bound to the gate that consumes it.

PATH_VALUES = [
    ("PV-ACT-COINS", "S-ACT-RECEIPT", "arena/coins", 640,
     "G-ARENA-REBUILT"),
    ("PV-ACT-LINKS", "S-ACT-RECEIPT", "arena/links", 32,
     "G-ARENA-REBUILT"),
    ("PV-ACT-PLAQ", "S-ACT-RECEIPT", "arena/plaquettes", 16,
     "G-ARENA-REBUILT"),
    ("PV-ACT-SITES", "S-ACT-RECEIPT", "arena/sites", 16,
     "G-ARENA-REBUILT"),
    ("PV-ACT-L", "S-ACT-RECEIPT", "arena/L", 4,
     "G-ARENA-REBUILT"),
    ("PV-ACT-ALPHABET", "S-ACT-RECEIPT", "arena/alphabet", 25,
     "G-ARENA-REBUILT"),
    ("PV-ACT-WILSON-N", "S-ACT-RECEIPT", "wilson/distinct_values_over_the_"
     "carrier", 11, "G-PLAQUETTE-ROW-REPRODUCED"),
    ("PV-ACT-ORBITS", "S-ACT-RECEIPT", "form_census/rows/0/orbits", 136,
     "G-THE-CLASSES-REBUILT"),
    ("PV-ACT-COUPLINGS", "S-ACT-RECEIPT", "form_census/rows/0/coupling_"
     "count", 135, "G-THE-CLASSES-REBUILT"),
    ("PV-ACT-COUPLINGS-EXT", "S-ACT-RECEIPT", "form_census/rows/1/coupling_"
     "count", 79, "G-THE-ORIENTATION-READING-IS-PRICED"),
    ("PV-ACT-PARENT-ORBITS", "S-ACT-RECEIPT",
     "gibbs/rows/0/the_parents_orbits", 208, "G-THE-CLASSES-REBUILT"),
    ("PV-ACT-VERTICES", "S-ACT-RECEIPT",
     "gibbs/rows/0/extreme_points_that_are_vertices_of_the_parents_simplex",
     64, "G-THE-EXTREME-POINTS-REBUILT"),
    ("PV-ACT-MIDPOINTS", "S-ACT-RECEIPT",
     "gibbs/rows/0/extreme_points_that_are_edge_midpoints_of_it", 72,
     "G-THE-EXTREME-POINTS-REBUILT"),
    ("PV-ACT-MERGED", "S-ACT-RECEIPT", "price/orbit_pairs_merged_anchored",
     72, "G-THE-EXTREME-POINTS-REBUILT"),
    ("PV-ACT-EXPONENT", "S-ACT-RECEIPT", "gibbs/rows/0/exponent", 32,
     "G-THE-DECLARED-ROWS-BUILT"),
    ("PV-ACT-NULL", "S-ACT-RECEIPT", "expectations/rows/0/expectation",
     "13/10", "G-PLAQUETTE-ROW-REPRODUCED"),
    ("PV-ACT-WITNESS", "S-ACT-RECEIPT", "expectations/rows/1/expectation",
     "4294967399/4294967375", "G-THE-DECLARED-ROWS-BUILT"),
    ("PV-ACT-WILSONEXP", "S-ACT-RECEIPT", "expectations/rows/2/expectation",
     "262244/65615", "G-THE-DECLARED-ROWS-BUILT"),
    ("PV-ACT-STAMP", "S-ACT-RECEIPT", "law_native_control/stamp",
     "LAW-RATED-CONSTRUCTION-DECLARED-AT-AN-UNPINNED-IDENTIFICATION",
     "G-THE-CONTROL-STAMP-CARRIED"),
    ("PV-ACT-LAW1", "S-ACT-RECEIPT", "law_native_control/sector_law/0",
     "15/38", "G-THE-CONTROL-STAMP-CARRIED"),
    ("PV-ACT-LAW2", "S-ACT-RECEIPT", "law_native_control/sector_law/1",
     "5/19", "G-THE-CONTROL-STAMP-CARRIED"),
    ("PV-ACT-LAW3", "S-ACT-RECEIPT", "law_native_control/sector_law/2",
     "13/38", "G-THE-CONTROL-STAMP-CARRIED"),
    ("PV-ACT-LOOPFAM", "S-ACT-RECEIPT", "wilson/loop_families_grown", 0,
     "G-THE-LOOP-FAMILY-IS-THE-MISSING-OBJECT"),
    ("PV-ACT-MERGEIDX", "S-ACT-RECEIPT",
     "merging_index_law/rows/1/the_merging_index", 2,
     "G-THE-MERGING-INDEX-LAW-REPRODUCED"),
    ("PV-R5-NONFLAT-DIAG", "S-R5-RECEIPT", "curvature_census/DIAGONAL/"
     "nonflat", 56, "G-PLAQUETTE-ROW-REPRODUCED"),
    ("PV-R5-COINS-BAL", "S-R5-RECEIPT", "coin_sectors/BALANCED", 512,
     "G-ARENA-REBUILT"),
    ("PV-R5-COINS-DIAG", "S-R5-RECEIPT", "coin_sectors/DIAGONAL", 64,
     "G-ARENA-REBUILT"),
    ("PV-R5-COINS-ANTI", "S-R5-RECEIPT", "coin_sectors/ANTIDIAGONAL", 64,
     "G-ARENA-REBUILT"),
    ("PV-R5-CHART", "S-R5-RECEIPT", "counts/chart_group", 32,
     "G-THE-LOOP-FAMILY-IS-CLOSED-UNDER-THE-ACTING-GROUP"),
]


def dig(obj, path):
    for part in path.split("/"):
        obj = obj[int(part)] if isinstance(obj, list) else obj[part]
    return obj


def measure_path_values(S, src):
    rows, out = [], {}
    for name, source, path, expect, consumer in PATH_VALUES:
        raw = src[source]
        try:
            val = dig(json.loads(raw.decode()), path)
        except (KeyError, IndexError, TypeError, ValueError):
            val = "ABSENT"
        if mut("MUT-PATH-VALUE") and name == "PV-ACT-COUPLINGS":
            val = 134
        out[name] = val
        rows.append({"anchor": name, "source": source, "path": path,
                     "expected": expect, "measured": val,
                     "agrees": val == expect, "consumer": consumer})
    ok = all(r["agrees"] for r in rows)
    LD.gate("G-PATH-VALUE-ANCHORS",
            "every number this unit inherits is read at a NAMED PATH inside "
            "a named parent's receipt and required to equal the value the "
            "pin froze, and every anchor names the gate that consumes it, "
            "so a parent field that moved -- or an anchor no consumer "
            "reads -- stops the delivery run",
            ok,
            "%d path-value anchors, %d agreeing"
            % (len(rows), sum(1 for r in rows if r["agrees"])))
    S["path_value_anchors"] = rows
    SEAL.take("THE PATH-VALUE ANCHORS", "path_value_anchors",
              "G-PATH-VALUE-ANCHORS", rows)
    return out


def wsnorm(s):
    return " ".join(s.split())


def mnorm(s):
    """#125: text gates match text AS WRITTEN -- whitespace AND markdown
    prefixes (blockquote markers, list bullets, emphasis) normalised, so a
    quotation that is reflowed or re-indented still matches and a quotation
    whose CONTENT moved does not."""
    out = []
    for line in s.split("\n"):
        t = line.strip()
        while t[:1] in (">", "-", "*", "|"):
            t = t[1:].strip()
        out.append(t)
    return wsnorm(" ".join(out)).replace("**", "").replace("`", "")


VERBATIM = [
    ("VB-R5-HOLONOMY", "S-R5-PAPER",
     "the holonomy is the ordered product of the four link operators around "
     "the boundary, each inverted where the boundary runs against the link's "
     "own direction", 60, "G-PLAQUETTE-ROW-REPRODUCED"),
    ("VB-R5-BLOCK", "S-R5-PAPER",
     "the whole holonomy lives in a four-by-four block", 30,
     "G-PLAQUETTE-ROW-REPRODUCED"),
    ("VB-R5-LINKOP", "S-R5-PAPER",
     "acts as $U$ on the two-dimensional span of the link's own domino and "
     "as the identity on every other site", 50,
     "G-ARENA-REBUILT"),
    ("VB-R5-NEEDS", "S-R5-PAPER",
     "a family of loops whose size can grow", 25,
     "G-THE-LOOP-FAMILY-IS-THE-MISSING-OBJECT"),
    ("VB-ACT-ABSENT", "S-ACT-PAPER",
     "a family of loops whose size can grow \u2014 is recorded as **still "
     "absent**, and it is the gate on everything beyond", 60,
     "G-THE-LOOP-FAMILY-IS-THE-MISSING-OBJECT"),
    ("VB-ACT-ALLOWED", "S-ACT-PAPER",
     "the allowed space is the direct power of the multiplicative positive "
     "rationals with one factor per orbit", 60,
     "G-THE-CLASSES-REBUILT"),
    ("VB-ACT-EXTREME", "S-ACT-PAPER",
     "64 of the reachable set's extreme points are vertices of the parent's "
     "simplex and the other 72 are midpoints of its edges", 60,
     "G-THE-EXTREME-POINTS-REBUILT"),
    ("VB-ACT-BOUNDARY", "S-ACT-PAPER",
     "The merging index is $8/\\gcd(L,8)$, and at every L divisible by eight "
     "it is 1, and there the price is not reduced, no orbit pair is "
     "identified and no observable is pinned", 60,
     "G-THE-MERGING-INDEX-LAW-REPRODUCED"),
    ("VB-ACT-STAMP", "S-ACT-PAPER",
     "ACT must not treat it as a derived measure and must not spend it as", 40,
     "G-THE-CONTROL-STAMP-CARRIED"),
    ("VB-ACT-GATE", "S-ACT-PAPER",
     "The confinement vocabulary REMAINS BEHIND POT'S GATE", 40,
     "G-THE-CONFINEMENT-LICENCE-WALL"),
    ("VB-PIN-LICENCE", "S-PIN",
     "every confinement word in prose must sit in a sentence carrying its "
     "measured discriminator value", 50,
     "G-THE-CONFINEMENT-LICENCE-WALL"),
    ("VB-PIN-LBOUND", "S-PIN",
     "the merging-index law 8/gcd(L,8) means family-level pinning dies at "
     "L \u2261 0 mod 8", 40, "G-THE-MERGING-INDEX-LAW-REPRODUCED"),
    ("VB-PIN-DISCRIM", "S-PIN",
     "The discriminator's own well-definedness (nonzero denominators; enough "
     "ladder rungs at the declared L) is itself a gated measurement", 60,
     "G-THE-DISCRIMINATOR-IS-WELL-DEFINED"),
    ("VB-P23-TRANSITIVE", "S-P23-PAPER",
     "acts **transitively** on that carrier", 25,
     "G-THE-LOOP-FAMILY-IS-CLOSED-UNDER-THE-ACTING-GROUP"),
    ("VB-SMU-PRICE", "S-SMU-PAPER",
     "The covariant-dynamics fibre therefore surjects onto the invariant "
     "simplex", 50, "G-THE-PRICE-BINDING"),
]


def measure_verbatim(S, src):
    rows = []
    for name, source, text, floor, consumer in VERBATIM:
        hay = mnorm(src[source].decode())
        needle = mnorm(text)
        if mut("MUT-VERBATIM") and name == "VB-R5-HOLONOMY":
            needle = needle.replace("inverted", "conjugated")
        hits = hay.count(needle)
        perturbed = needle
        toks = [t for t in needle.split() if len(t) > 3]
        if toks:
            perturbed = needle.replace(toks[len(toks) // 2],
                                       toks[len(toks) // 2] + "X", 1)
        rows.append({"anchor": name, "source": source, "chars": len(needle),
                     "floor": floor, "hits": hits,
                     "located_exactly_once": hits == 1,
                     "long_enough": len(needle) >= floor,
                     "perturbation_is_lost": hay.count(perturbed) == 0,
                     "digest": hashlib.sha256(
                         needle.encode()).hexdigest()[:12],
                     "located_text": needle if hits == 1 else "",
                     "consumer": consumer})
    ok = all(r["located_exactly_once"] and r["long_enough"]
             and r["perturbation_is_lost"] for r in rows)
    LD.gate("G-VERBATIM-ANCHORS",
            "every window this unit quotes from a parent is pinned by the "
            "digest of its exact bytes, by its own character count against a "
            "declared floor, is located EXACTLY ONCE under whitespace and "
            "markdown-prefix normalisation, is perturbed at a "
            "content-bearing token and required to stop being locatable, "
            "and is bound to the gate that consumes it",
            ok,
            "%d windows, %d located exactly once, %d above their floors"
            % (len(rows), sum(1 for r in rows if r["located_exactly_once"]),
               sum(1 for r in rows if r["long_enough"])))
    S["verbatim_anchors"] = rows
    SEAL.take("THE VERBATIM ANCHORS", "verbatim_anchors",
              "G-VERBATIM-ANCHORS", rows)
    return {r["anchor"]: r for r in rows}


VB_READS = []


def vbwin(vb, name, gate, token):
    """THE VERBATIM CONSUMPTION.  A gate that names a window as its own reads
    the window's located text HERE and takes a content token out of it, so
    the anchor enters that gate's own predicate instead of decorating a
    column.  Every read is recorded with the gate that made it and the whole
    register is reconciled against the declared consumer column at
    G-CONSUMER-REGISTER-IS-REAL, so a window no gate reads is fatal."""
    row = vb[name]
    got = token in row["located_text"]
    VB_READS.append({"anchor": name, "read_by": gate, "token": token,
                     "token_located_in_the_window": got})
    return got


def measure_consumers(S):
    """#82 / K3's ruling at ACT: a named consumer gate that does not exist in
    this run's own ledger is fatal, so the consumer column is a real binding
    and not a decoration -- and, since K3's MAJOR-9 at this unit, a window
    whose named consumer never READ it is fatal too."""
    named = sorted({c for _n, _s, _p, _e, c in PATH_VALUES}
                   | {c for _n, _s, _t, _f, c in VERBATIM})
    if mut("MUT-CONSUMER-GHOST"):
        named = named + ["G-A-GATE-THIS-INSTRUMENT-DOES-NOT-HAVE"]
    missing = [c for c in named if c not in LD.ids]
    reads = list(VB_READS)
    if mut("MUT-CONSUMER-UNREAD"):
        reads = [r for r in reads if r["anchor"] != "VB-SMU-PRICE"]
    by_anchor = {}
    for r in reads:
        by_anchor.setdefault(r["anchor"], []).append(r)
    unread, misread = [], []
    for nm, _s, _t, _f, cons in VERBATIM:
        got = by_anchor.get(nm, [])
        if not got:
            unread.append(nm)
            continue
        if any(r["read_by"] != cons or not r["token_located_in_the_window"]
               for r in got):
            misread.append(nm)
    LD.gate("G-CONSUMER-REGISTER-IS-REAL",
            "every gate named as an anchor's consumer is checked against "
            "THIS RUN'S OWN closed-gate ledger, and every verbatim window is "
            "required to have been READ by exactly the gate its own column "
            "names, with the token it supplied located inside it: an anchor "
            "naming a gate this instrument does not have, and a window no "
            "gate consumed, both stop the run",
            not missing and not unread and not misread,
            "%d named consumers, %d missing; %d verbatim windows, %d read by "
            "their own consumer over %d reads, %d unread %s, %d misread %s"
            % (len(named), len(missing), len(VERBATIM),
               len(VERBATIM) - len(unread) - len(misread), len(reads),
               len(unread), unread, len(misread), misread))
    S["consumer_register"] = {"named": named, "missing": missing,
                              "all_present": not missing,
                              "verbatim_windows": len(VERBATIM),
                              "verbatim_reads": reads,
                              "windows_never_read": unread,
                              "windows_read_by_another_gate": misread}
    SEAL.take("THE CONSUMER REGISTER", "consumer_register",
              "G-CONSUMER-REGISTER-IS-REAL", S["consumer_register"])


# ===========================================================================
# SECTION 4.  THE ARENA, REBUILT
# ===========================================================================

def build_alphabet():
    """R4's coefficient alphabet as R5 declares it, carried DOUBLED so that
    every entry is integral: zero, and zeta_8^t at each of the three declared
    moduli."""
    cands = [IZ]
    for t in range(8):
        cands.append(tuple(2 * x for x in izpow(t)))
        cands.append(izpow(t))
        cands.append(imul(izpow(t), SQRT2))
    out, seen = [], set()
    for a in cands:
        if a not in seen:
            seen.add(a)
            out.append(a)
    return out


FOUR = (4, 0, 0, 0)


def build_coins(alphabet):
    """THE COIN FAMILY, DERIVED: a two-by-two unitary all four of whose
    entries lie in the alphabet, enumerated exhaustively over the alphabet's
    fourth power and pruned by the row conditions.  In doubled coordinates
    |a|^2 + |b|^2 = 1 reads (2a)(2a)bar + (2b)(2b)bar = 4."""
    rows = [(a, b) for a in alphabet for b in alphabet
            if iadd(imul(a, iconj(a)), imul(b, iconj(b))) == FOUR]
    coins = []
    for (a, b) in rows:
        for (c, d) in rows:
            if iadd(imul(a, iconj(c)), imul(b, iconj(d))) == IZ:
                coins.append((a, b, c, d))
    if mut("MUT-ARENA"):
        coins = coins[:-1]
    return coins, rows


def coin_sector(m):
    a, b, c, d = m
    if b == IZ and c == IZ:
        return "DIAGONAL"
    if a == IZ and d == IZ:
        return "ANTIDIAGONAL"
    return "BALANCED"


def coin_unitary_second_route(m):
    a, b, c, d = m
    return (iadd(imul(iconj(a), a), imul(iconj(c), c)) == FOUR
            and iadd(imul(iconj(b), b), imul(iconj(d), d)) == FOUR
            and iadd(imul(iconj(a), b), imul(iconj(c), d)) == IZ)


def gauge_twist(m, k):
    """the site-diagonal gauge acts on a link's coin by conjugation with
    diag(zeta_8^p, zeta_8^q); the action depends on k = p - q alone, and it
    multiplies the two off-diagonal entries by opposite powers."""
    a, b, c, d = m
    return (a, imul(izpow(k), b), imul(izpow(-k), c), d)


E1, E2 = (1, 0), (0, 1)
EDIR = (E1, E2)


class Lattice:
    def __init__(self, L):
        self.L = L
        self.sites = [(x, y) for x in range(L) for y in range(L)]
        self.links = [(s, d) for s in self.sites for d in range(2)]
        self.plaquettes = list(self.sites)

    def addv(self, s, v):
        return ((s[0] + v[0]) % self.L, (s[1] + v[1]) % self.L)

    def ends(self, l):
        return l[0], self.addv(l[0], EDIR[l[1]])


def build_arena(S, pv, vb):
    alpha = build_alphabet()
    coins, rows = build_coins(alpha)
    lat = Lattice(pv["PV-ACT-L"])
    sect = {}
    for m in coins:
        sect[coin_sector(m)] = sect.get(coin_sector(m), 0) + 1
    unit = sum(1 for m in coins if coin_unitary_second_route(m))
    ok = (len(alpha) == pv["PV-ACT-ALPHABET"]
          and len(coins) == pv["PV-ACT-COINS"]
          and unit == len(coins)
          and len(lat.sites) == pv["PV-ACT-SITES"]
          and len(lat.links) == pv["PV-ACT-LINKS"]
          and len(lat.plaquettes) == pv["PV-ACT-PLAQ"]
          and sect.get("DIAGONAL") == pv["PV-R5-COINS-DIAG"]
          and sect.get("ANTIDIAGONAL") == pv["PV-R5-COINS-ANTI"]
          and sect.get("BALANCED") == pv["PV-R5-COINS-BAL"]
          and vbwin(vb, "VB-R5-LINKOP", "G-ARENA-REBUILT",
                    "the identity on every other site"))
    LD.gate("G-ARENA-REBUILT",
            "the alphabet, the coin family, the lattice, the link set and "
            "the plaquette set are REBUILT here from the parents' own "
            "declarations -- nothing is imported -- and every cardinality is "
            "required to equal the parent's published one at a named receipt "
            "path, with unitarity confirmed by a second route on every coin "
            "and the link operator's own window read here for the clause "
            "that fixes what the operator does away from its link",
            ok,
            "alphabet %d, coins %d (%s), unitary by a second route %d, "
            "sites %d, links %d, plaquettes %d"
            % (len(alpha), len(coins),
               ", ".join("%s %d" % (k, sect[k]) for k in sorted(sect)),
               unit, len(lat.sites), len(lat.links), len(lat.plaquettes)))
    S["_alpha"], S["_coins"], S["_lat"] = alpha, coins, lat
    S["_cidx"] = {c: i for i, c in enumerate(coins)}
    S["arena"] = {
        "L": lat.L, "d": 2, "alphabet": len(alpha), "coins": len(coins),
        "admissible_rows": len(rows), "sites": len(lat.sites),
        "links": len(lat.links), "plaquettes": len(lat.plaquettes),
        "sectors": sect, "unitary_by_a_second_route": unit,
        "field": "Q(zeta_8)",
        "carrier": "THE-640-UNIFORM-CONFIGURATIONS",
        "configuration_space": "640^32",
        "the_carrier_is_the_parents": True}
    SEAL.take("THE ARENA", "arena", "G-ARENA-REBUILT", S["arena"])
    return lat, coins


# ===========================================================================
# SECTION 5.  THE LOOP FAMILY -- THE OBJECT ACT RECORDED STILL ABSENT
# ===========================================================================
# A loop is a closed lattice path carried as its CYCLE OF SITES, consecutive
# sites adjacent on the torus.  The declared family has three generators --
# the rectangle circuit, the straight winding cycle and the staircase -- and
# the window is named in the verdict: RECTANGLE-CIRCUITS-PLUS-STRAIGHT-AND-
# STAIRCASE-WINDING-CYCLES, not all closed paths.

def rect_cycle(lat, base, a, b):
    """the a-by-b rectangle circuit based at base, traversed
    base -> +a e1 -> +b e2 -> -a e1 -> -b e2."""
    cyc, cur = [], base
    for _ in range(a):
        cyc.append(cur)
        cur = lat.addv(cur, E1)
    for _ in range(b):
        cyc.append(cur)
        cur = lat.addv(cur, E2)
    for _ in range(a):
        cyc.append(cur)
        cur = lat.addv(cur, (-1, 0))
    for _ in range(b):
        cyc.append(cur)
        cur = lat.addv(cur, (0, -1))
    return tuple(cyc), cur == base


def wind_cycle(lat, base, d, k):
    """the straight cycle that wraps the torus k times in direction d."""
    cyc, cur = [], base
    for _ in range(k * lat.L):
        cyc.append(cur)
        cur = lat.addv(cur, EDIR[d])
    return tuple(cyc), cur == base


def stair_cycle(lat, base):
    """the staircase: one wrap in each direction, concatenated at base."""
    h, okh = wind_cycle(lat, base, 0, 1)
    v, okv = wind_cycle(lat, base, 1, 1)
    return h + v, okh and okv


def rotations(c):
    m = len(c)
    return [tuple(c[(i + r) % m] for i in range(m)) for r in range(m)]


def canon(c):
    """the canonical name of a loop: least over rotations of the cycle AND of
    its reversal.  Reversal is admitted because the reversed loop's holonomy
    is the inverse, whose trace is the conjugate -- equal on this carrier,
    which is MEASURED at G-THE-LOOP-OBSERVABLE-IS-REVERSAL-BLIND rather than
    assumed."""
    if mut("MUT-CANON"):
        return min(rotations(c))
    return min(rotations(c) + rotations(tuple(reversed(c))))


def steps_of(lat, cyc):
    """the (link, orientation) steps of a site cycle; orientation -1 means
    the step runs against the link's own direction, so its operator
    inverts."""
    st = []
    for i in range(len(cyc)):
        u, w = cyc[i], cyc[(i + 1) % len(cyc)]
        found = None
        for d in (0, 1):
            if lat.addv(u, EDIR[d]) == w:
                found = ((u, d), 1)
                break
            if lat.addv(w, EDIR[d]) == u:
                found = ((w, d), -1)
                break
        if found is None:
            raise GateFail("G-THE-LOOP-FAMILY-IS-A-FAMILY-OF-LOOPS :: "
                           "a declared cycle has a non-adjacent step")
        st.append(found)
    return st


def homology(lat, cyc):
    """the winding class in H_1 of the torus: net displacement over L."""
    h = [0, 0]
    for i in range(len(cyc)):
        u, w = cyc[i], cyc[(i + 1) % len(cyc)]
        for d in (0, 1):
            dv = (w[d] - u[d]) % lat.L
            if dv == 1:
                h[d] += 1
            elif dv == lat.L - 1:
                h[d] -= 1
    return (h[0] // lat.L, h[1] // lat.L)


def holonomy_trace(lat, steps, coin):
    """the trace of the loop holonomy on its own site block, rebuilt from
    R5's definition: the ordered product of the link operators around the
    loop, each inverted where the loop runs against the link's own direction.
    Every factor is the identity off the loop's own sites, so the product is
    too and the restriction is exact.  Doubled coin entries make every entry
    integral; the power of two each row carries is tracked and divided out
    once, at the end."""
    a, b, c, d = coin
    inv = (iconj(a), iconj(c), iconj(b), iconj(d))
    sites = []
    for (l, o) in steps:
        t, h = lat.ends(l)
        for s in (t, h):
            if s not in sites:
                sites.append(s)
    pos = {s: i for i, s in enumerate(sites)}
    n = len(sites)
    W = [[IONE if i == j else IZ for j in range(n)] for i in range(n)]
    scale = [0] * n
    step = 0
    for (l, o) in steps:
        t, h = lat.ends(l)
        it, ih = pos[t], pos[h]
        if scale[it] < step:
            W[it] = [ishift(x, step - scale[it]) for x in W[it]]
            scale[it] = step
        if scale[ih] < step:
            W[ih] = [ishift(x, step - scale[ih]) for x in W[ih]]
            scale[ih] = step
        A, B, C, D = coin if o > 0 else inv
        r1, r2 = W[it], W[ih]
        n1, n2 = [], []
        for j in range(n):
            x, y = r1[j], r2[j]
            if x == IZ and y == IZ:
                n1.append(IZ)
                n2.append(IZ)
                continue
            n1.append(iadd(imul(A, x), imul(B, y)))
            n2.append(iadd(imul(C, x), imul(D, y)))
        W[it], W[ih] = n1, n2
        step += 1
        scale[it] = scale[ih] = step
    top = max(scale)
    tr = IZ
    for i in range(n):
        tr = iadd(tr, ishift(W[i][i], top - scale[i]))
    den = 1 << top
    return (Fraction(tr[0], den), Fraction(tr[1], den),
            Fraction(tr[2], den), Fraction(tr[3], den)), n


RECT_KINDS = "RECTANGLE-CIRCUIT"
WIND_KINDS = "STRAIGHT-WINDING-CYCLE"
STAIR_KIND = "STAIRCASE-WINDING-CYCLE"


def enumerate_family(lat):
    """the declared family, enumerated with NO SILENT CAP: the rectangle
    extents are swept to the lattice period itself and the simple ones are
    MEASURED rather than assumed, so which sizes exist is a finding."""
    simple_rows, fam = [], []
    for a in range(1, lat.L + 1):
        for b in range(1, lat.L + 1):
            cyc, closes = rect_cycle(lat, (0, 0), a, b)
            st = steps_of(lat, cyc)
            links = {l for (l, _o) in st}
            sites = {s for s in cyc}
            simple = (len(links) == len(st) and len(sites) == len(st)
                      and closes)
            simple_rows.append({
                "a": a, "b": b, "steps": len(st), "distinct_links": len(links),
                "distinct_sites": len(sites), "closes": closes,
                "simple": simple})
    if mut("MUT-SIMPLICITY"):
        simple_rows[0]["simple"] = False
    extents = sorted({r["a"] for r in simple_rows if r["simple"]})
    for r in simple_rows:
        if not r["simple"]:
            continue
        a, b = r["a"], r["b"]
        for x in range(lat.L):
            for y in range(lat.L):
                cyc, _ = rect_cycle(lat, (x, y), a, b)
                fam.append({"kind": RECT_KINDS, "a": a, "b": b,
                            "base": (x, y), "cycle": cyc})
    for k in range(1, lat.L + 1):
        for y in range(lat.L):
            cyc, _ = wind_cycle(lat, (0, y), 0, k)
            fam.append({"kind": WIND_KINDS, "a": k, "b": 0,
                        "base": (0, y), "cycle": cyc})
        for x in range(lat.L):
            cyc, _ = wind_cycle(lat, (x, 0), 1, k)
            fam.append({"kind": WIND_KINDS, "a": 0, "b": k,
                        "base": (x, 0), "cycle": cyc})
    for x in range(lat.L):
        for y in range(lat.L):
            cyc, _ = stair_cycle(lat, (x, y))
            fam.append({"kind": STAIR_KIND, "a": 1, "b": 1,
                        "base": (x, y), "cycle": cyc})
    for f in fam:
        f["name"] = canon(f["cycle"])
        f["homology"] = homology(lat, f["cycle"])
        f["length"] = len(f["cycle"])
        f["support"] = len(set(f["cycle"]))
    return simple_rows, extents, fam


def point_symmetries(extended):
    if not extended:
        return [(False, 1, 1), (True, 1, 1)]
    return [(sw, sx, sy) for sw in (False, True)
            for sx in (1, -1) for sy in (1, -1)]


def apply_point(g, s, L):
    sw, sx, sy = g
    x, y = s
    if sw:
        x, y = y, x
    return ((sx * x) % L, (sy * y) % L)


def chart_elements(lat, extended):
    return [(v, g) for v in lat.sites for g in point_symmetries(extended)]


def transport_loop(lat, el, cyc):
    v, g = el
    return canon(tuple(lat.addv(apply_point(g, s, lat.L), v) for s in cyc))


def measure_loop_family(S, pv, vb):
    lat = S["_lat"]
    simple_rows, extents, fam = enumerate_family(lat)
    names = {f["name"] for f in fam}
    kinds = {}
    for f in fam:
        kinds[f["kind"]] = kinds.get(f["kind"], 0) + 1
    hom = {}
    for f in fam:
        hom[str(f["homology"])] = hom.get(str(f["homology"]), 0) + 1
    contractible = sum(1 for f in fam if f["homology"] == (0, 0))
    winding = len(fam) - contractible
    n_simple = sum(1 for r in simple_rows if r["simple"])
    ok = (len(names) == len(fam) and n_simple == len(extents) ** 2
          and contractible == n_simple * len(lat.sites)
          and winding > 0 and len(fam) > 0)
    LD.gate("G-THE-LOOP-FAMILY-IS-A-FAMILY-OF-LOOPS",
            "the declared family is enumerated with no silent cap -- the "
            "rectangle extents are swept to the lattice period itself and "
            "the SIMPLE ones are measured rather than assumed -- every "
            "member closes, every step is an adjacency, every placement "
            "carries a distinct canonical name, and the winding arm is "
            "populated as well as the contractible one",
            ok,
            "%d placements, %d distinct loops, %d contractible and %d "
            "winding, simple extents %s at %d of %d swept sizes"
            % (len(fam), len(names), contractible, winding, extents,
               n_simple, len(simple_rows)))
    orbit_rows = []
    for extended, reading in ((False, "ANCHORED"), (True, "EXTENSION")):
        G = chart_elements(lat, extended)
        seen, orbits, escapes = set(), [], 0
        for f in sorted(fam, key=lambda z: str(z["name"])):
            if f["name"] in seen:
                continue
            orb = {transport_loop(lat, el, f["cycle"]) for el in G}
            escapes += len(orb - names)
            inside = orb & names
            seen |= inside
            orbits.append(sorted(inside))
        orbit_rows.append({
            "reading": reading, "chart_order": len(G),
            "distinct_loops": len(names), "orbits": len(orbits),
            "orbit_sizes": sorted({len(o) for o in orbits}),
            "images_outside_the_declared_family": escapes,
            "closed_under_the_acting_group": escapes == 0})
    if mut("MUT-FAMILY-CLOSURE"):
        orbit_rows[0]["closed_under_the_acting_group"] = False
    anchored = orbit_rows[0]
    ok2 = (anchored["chart_order"] == pv["PV-R5-CHART"]
           and anchored["closed_under_the_acting_group"]
           and anchored["orbits"] < len(names)
           and vbwin(vb, "VB-P23-TRANSITIVE",
                     "G-THE-LOOP-FAMILY-IS-CLOSED-UNDER-THE-ACTING-GROUP",
                     "transitively"))
    LD.gate("G-THE-LOOP-FAMILY-IS-CLOSED-UNDER-THE-ACTING-GROUP",
            "distinctness is measured under the acting group at both "
            "declared readings: the anchored chart group is the parent's "
            "own, the declared family is required to be CLOSED under it, "
            "and the orbit count -- which is how many loops this arena "
            "really has, as against how many placements -- is computed, not "
            "typed.  The extension reading's escape count is published "
            "rather than absorbed",
            ok2,
            "; ".join("%s: order %d, %d loops, %d orbits, sizes %s, escapes "
                      "%d" % (r["reading"], r["chart_order"],
                              r["distinct_loops"], r["orbits"],
                              r["orbit_sizes"],
                              r["images_outside_the_declared_family"])
                      for r in orbit_rows))
    S["_fam"] = fam
    S["loop_family"] = {
        "the_window": "RECTANGLE-CIRCUITS-PLUS-STRAIGHT-AND-STAIRCASE-"
                      "WINDING-CYCLES-NOT-ALL-CLOSED-PATHS",
        "every_integer_here_is_a_count": "COUNTING-ONLY-E-24",
        "placements": len(fam), "distinct_loops": len(names),
        "contractible": contractible, "winding": winding,
        "kinds": kinds, "homology_classes": hom,
        "simple_rectangle_extents": extents,
        "simple_rectangle_shapes": n_simple,
        "rectangle_sizes_swept": len(simple_rows),
        "simplicity_rows": simple_rows,
        "orbit_rows": orbit_rows,
        "the_missing_object": "ACT-RECORDED-THE-LOOP-FAMILY-STILL-ABSENT-"
                              "AND-THIS-UNIT-BUILDS-IT"}
    SEAL.take("THE LOOP FAMILY", "loop_family",
              "G-THE-LOOP-FAMILY-IS-CLOSED-UNDER-THE-ACTING-GROUP",
              S["loop_family"])
    return fam


# ===========================================================================
# SECTION 6.  THE CLASSES, THE PARENT'S ORBITS AND THE EXTREME POINTS
# ===========================================================================

def twist_orbits(coins, cidx, twists):
    seen = [-1] * len(coins)
    out = []
    for i in range(len(coins)):
        if seen[i] >= 0:
            continue
        orb = sorted({cidx[gauge_twist(coins[i], k)] for k in twists})
        for j in orb:
            seen[j] = len(out)
        out.append(orb)
    return out


def phase_order():
    """the order of the declared field's root of unity, DERIVED from the
    field arithmetic rather than typed: the least positive power of z that
    returns the identity."""
    e = 1
    while izpow(e) != IONE:
        e += 1
    return e


def realisable_twists(L):
    """a constant link twist t closes around a cycle of length L exactly when
    the phase order divides L t, so the residual gauge group on the carrier
    has order gcd(L, phase order) while the link stencil's gauge image is the
    full phase order."""
    ph = phase_order()
    return [t for t in range(ph) if (L * t) % ph == 0]


def measure_classes(S, pv, vb):
    coins, cidx, lat = S["_coins"], S["_cidx"], S["_lat"]
    res = realisable_twists(lat.L)
    parent = twist_orbits(coins, cidx, res)
    classes = twist_orbits(coins, cidx, range(phase_order()))
    if mut("MUT-CLASSES"):
        classes = classes[:-2] + [classes[-1] + classes[-2]]
    prof = {}
    for c in classes:
        prof[len(c)] = prof.get(len(c), 0) + 1
    coarsens = all(any(set(o) <= set(c) for c in classes) for o in parent)
    merged = len(parent) - len(classes)
    ok = (len(classes) == pv["PV-ACT-ORBITS"]
          and len(parent) == pv["PV-ACT-PARENT-ORBITS"]
          and coarsens and merged == pv["PV-ACT-MERGED"]
          and sum(prof.values()) == len(classes)
          and vbwin(vb, "VB-ACT-ALLOWED", "G-THE-CLASSES-REBUILT",
                    "one factor per orbit"))
    LD.gate("G-THE-CLASSES-REBUILT",
            "the induced classes on the carrier are rebuilt from the twist "
            "action alone and required to land on the parent's published "
            "counts: the residual gauge group of the torus gives the "
            "parent's orbits, the full link-stencil gauge image gives the "
            "classes, the classes are measured to COARSEN the orbits, and "
            "the number of merged pairs is the parent's own",
            ok,
            "%d classes with size profile %s, %d parent orbits, coarsening "
            "%s, %d pairs merged"
            % (len(classes), sorted(prof.items()), len(parent), coarsens,
               merged))
    vertices = [c for c in classes if len(c) == 1]
    midpoints = [c for c in classes if len(c) > 1]
    if mut("MUT-EXTREME-SPLIT"):
        midpoints = midpoints[1:]
    ok2 = (len(vertices) == pv["PV-ACT-VERTICES"]
           and len(midpoints) == pv["PV-ACT-MIDPOINTS"]
           and len(vertices) + len(midpoints) == len(classes)
           and vbwin(vb, "VB-ACT-EXTREME", "G-THE-EXTREME-POINTS-REBUILT",
                     "%d of the reachable set's extreme points are vertices"
                     % len(vertices))
           and vbwin(vb, "VB-ACT-EXTREME", "G-THE-EXTREME-POINTS-REBUILT",
                     "the other %d are midpoints" % len(midpoints)))
    LD.gate("G-THE-EXTREME-POINTS-REBUILT",
            "the extreme points of the reachable set are the uniform "
            "measures on the classes: a class the odd twist fixes is a "
            "VERTEX of the parent's simplex and a class it merges is a "
            "MIDPOINT of one of its edges, and the split is required to "
            "equal the parent's published one -- read out of the parent's "
            "own sentence here, so THIS run's two counts must be the two "
            "integers that sentence carries",
            ok2,
            "%d extreme points: %d vertices and %d edge midpoints"
            % (len(classes), len(vertices), len(midpoints)))
    S["_classes"], S["_parent_orbits"] = classes, parent
    S["_vertices"], S["_midpoints"] = vertices, midpoints
    S["classes"] = {
        "every_integer_here_is_a_count": "COUNTING-ONLY-E-24",
        "classes": len(classes), "parent_orbits": len(parent),
        "class_size_profile": sorted(prof.items()),
        "the_classes_coarsen_the_parents_orbits": coarsens,
        "orbit_pairs_merged": merged,
        "extreme_points": len(classes),
        "extreme_points_that_are_vertices": len(vertices),
        "extreme_points_that_are_edge_midpoints": len(midpoints),
        "realisable_constant_twists": res,
        "the_couplings_the_parent_hands_over": pv["PV-ACT-COUPLINGS"]}
    SEAL.take("THE CLASSES", "classes", "G-THE-EXTREME-POINTS-REBUILT",
              S["classes"])
    return classes, parent


# ===========================================================================
# SECTION 7.  THE LOOP OBSERVABLE ON THE CARRIER
# ===========================================================================

def measure_the_loop_observable(S, pv, vb):
    """the trace of the loop holonomy on its own site block, evaluated at
    every coin of the carrier, for every placement of the declared family.
    Three properties are MEASURED rather than assumed and each is a gate: the
    trace lies in the real subfield, it is independent of the base point, and
    it is blind to the reversal of the loop."""
    lat, coins = S["_lat"], S["_coins"]
    fam = S["_fam"]
    by_shape = {}
    for f in fam:
        by_shape.setdefault((f["kind"], f["a"], f["b"]), []).append(f)
    TR, TRF, base_rows = {}, {}, []
    rawreal, outside, shapes_real = 0, 0, 0
    for key in sorted(by_shape, key=str):
        places = sorted(by_shape[key], key=lambda z: z["base"])
        first = places[0]
        st = steps_of(lat, first["cycle"])
        vals, full = [], []
        here = 0
        for m in coins:
            t, _n = holonomy_trace(lat, st, m)
            full.append(t)
            if in_real_subfield(t):
                rawreal += 1
                here += 1
            v = sym_qs(t)
            if not in_real_subfield((v[0], v[1], Fraction(0), -v[1])):
                outside += 1
            vals.append(v)
        if here == len(coins):
            shapes_real += 1
        TR[key] = vals
        TRF[key] = full
        mism = 0
        for other in places[1:]:
            st2 = steps_of(lat, other["cycle"])
            for i, m in enumerate(coins):
                t2, _n = holonomy_trace(lat, st2, m)
                if sym_qs(t2) != vals[i]:
                    mism += 1
        if mut("MUT-BASEPOINT") and key == ("RECTANGLE-CIRCUIT", 1, 1):
            mism = 1
        base_rows.append({"shape": "%s-%d-%d" % key, "placements": len(places),
                          "coins": len(coins), "mismatches": mism,
                          "support": first["support"],
                          "length": first["length"]})
    ok = outside == 0 and all(r["mismatches"] == 0 for r in base_rows)
    LD.gate("G-THE-LOOP-OBSERVABLE-IS-BASE-POINT-BLIND",
            "the loop observable is rebuilt from R5's own definition and is "
            "the parent's own admissible object -- the CONJUGATION-SYMMETRIC "
            "part of the loop trace, which lies in the real subfield by "
            "construction -- measured on the whole carrier at EVERY "
            "placement of every declared shape: the value at one base point "
            "equals the value at every other, which is what makes an "
            "expectation over the family a function of the shape and not of "
            "where the loop was put, and how many shapes have an already "
            "real raw trace is published rather than assumed",
            ok,
            "%d shapes, %d placement-by-coin comparisons, %d mismatches, %d "
            "values outside the real subfield, %d of %d shapes whose raw "
            "trace is already real at every coin (%d of %d shape-by-coin "
            "traces)"
            % (len(base_rows),
               sum((r["placements"] - 1) * r["coins"] for r in base_rows),
               sum(r["mismatches"] for r in base_rows), outside,
               shapes_real, len(base_rows), rawreal,
               len(base_rows) * len(coins)))
    rev_bad = 0
    rev_checked = 0
    for key in sorted(by_shape, key=str):
        cyc = sorted(by_shape[key], key=lambda z: z["base"])[0]["cycle"]
        st = steps_of(lat, tuple(reversed(cyc)))
        for i, m in enumerate(coins):
            t, _n = holonomy_trace(lat, st, m)
            rev_checked += 1
            if sym_qs(t) != TR[key][i]:
                rev_bad += 1
    if mut("MUT-REVERSAL"):
        rev_bad = 1
    LD.gate("G-THE-LOOP-OBSERVABLE-IS-REVERSAL-BLIND",
            "the canonical name of a loop admits its reversal, and that "
            "admission is EARNED rather than declared: the reversed loop's "
            "holonomy is the inverse, whose trace is the conjugate, and on "
            "this carrier every trace is real -- so the reversed loop's "
            "trace is measured equal at every shape and every coin",
            rev_bad == 0,
            "%d reversed-loop comparisons, %d disagreements"
            % (rev_checked, rev_bad))
    plaq = TR[("RECTANGLE-CIRCUIT", 1, 1)]
    distinct = sorted(set(plaq), key=lambda z: (z[0], z[1]))
    flat = sum(1 for v in plaq if v == (Fraction(4), Fraction(0)))
    nonflat_diag = sum(1 for i, m in enumerate(coins)
                       if coin_sector(m) == "DIAGONAL"
                       and plaq[i] != (Fraction(4), Fraction(0)))
    tot = (sum(v[0] for v in plaq) / len(plaq),
           sum(v[1] for v in plaq) / len(plaq))
    if mut("MUT-PLAQUETTE"):
        distinct = distinct[:-1]
    ok3 = (len(distinct) == pv["PV-ACT-WILSON-N"]
           and qs_str(tot) == pv["PV-ACT-NULL"]
           and nonflat_diag == pv["PV-R5-NONFLAT-DIAG"]
           and vbwin(vb, "VB-R5-HOLONOMY", "G-PLAQUETTE-ROW-REPRODUCED",
                     "inverted where the boundary runs against")
           and vbwin(vb, "VB-R5-BLOCK", "G-PLAQUETTE-ROW-REPRODUCED",
                     "four-by-four block"))
    LD.gate("G-PLAQUETTE-ROW-REPRODUCED",
            "the one member of this family the parents already measured is "
            "reproduced from these primitives before anything new is said: "
            "the plaquette's trace takes the parent's own number of distinct "
            "values on the carrier, its counting-measure expectation is the "
            "parent's published number, and the count of non-flat diagonal "
            "coins is the grandparent's -- with the two windows that fix the "
            "holonomy's own definition read here, at the orientation clause "
            "and at the block the census runs in",
            ok3,
            "%d distinct values, counting expectation %s, %d non-flat "
            "diagonal coins, %d flat coins"
            % (len(distinct), qs_str(tot), nonflat_diag, flat))
    S["_TR"], S["_TRF"] = TR, TRF
    S["_shapes"] = sorted(by_shape, key=str)
    S["loop_observable"] = {
        "observable": "THE-TRACE-OF-THE-LOOP-HOLONOMY-ON-ITS-OWN-SITE-BLOCK",
        "rebuilt_from": "R5-ORDERED-PRODUCT-EACH-INVERTED-AGAINST-ITS-OWN-"
                        "DIRECTION",
        "the_declared_observable": "THE-CONJUGATION-SYMMETRIC-PART-OF-THE-"
                                   "TRACE",
        "values_outside_the_real_subfield": outside,
        "shapes_whose_raw_trace_is_already_real": shapes_real,
        "shape_by_coin_traces_already_real": rawreal,
        "base_point_rows": base_rows,
        "reversal_comparisons": rev_checked,
        "reversal_disagreements": rev_bad,
        "plaquette_distinct_values": len(distinct),
        "plaquette_counting_expectation": qs_str(tot),
        "plaquette_flat_coins": flat,
        "plaquette_nonflat_diagonal_coins": nonflat_diag,
        "the_reference_value_at_a_flat_configuration":
            "THE-BLOCK-DIMENSION-WHICH-IS-THE-LOOPS-OWN-SITE-COUNT"}
    SEAL.take("THE LOOP OBSERVABLE", "loop_observable",
              "G-PLAQUETTE-ROW-REPRODUCED", S["loop_observable"])
    return TR


# ===========================================================================
# SECTION 8.  THE DISCRIMINATOR -- DEFINED AND GATED BEFORE ANY ROW RUNS
# ===========================================================================
# The exact finite analogue of area against perimeter, in three legs, all
# multiplicative and all in exact arithmetic.  It is a PURE FUNCTION of a
# ladder table, which is what lets the control arms drive it with declared
# synthetic tables through the same code the delivered rows go through.
#
#   LEG-AREA     at equal perimeter, does the expectation move with the area?
#   LEG-CREUTZ   the Creutz ratio chi(a,b) = W(a,b) W(a-1,b-1) /
#                ( W(a,b-1) W(a-1,b) ), which is one for a law geometric in
#                the perimeter and constant and not one for a law geometric
#                in the area.
#   LEG-WINDING  the winding-cycle expectation, the order-parameter analogue.

def area_comparisons(shapes):
    """the pairs of ladder shapes with the SAME perimeter and DIFFERENT
    area: the only comparisons at which an area law can show itself without
    a model."""
    out = []
    for (a, b) in shapes:
        for (p, q) in shapes:
            if (a, b) < (p, q) and a + b == p + q and a * b != p * q:
                out.append(((a, b), (p, q)))
    return out


def creutz_rungs(shapes):
    st = set(shapes)
    return [(a, b) for (a, b) in shapes
            if a >= 2 and b >= 2 and (a - 1, b) in st and (a, b - 1) in st
            and (a - 1, b - 1) in st]


def classify(table, wind, shapes):
    """THE DISCRIMINATOR.  table maps a ladder shape to an exact element of
    Q(sqrt 2); wind is the winding-cycle expectation; the verdict is derived
    from the three legs and nothing else."""
    comps = area_comparisons(shapes)
    rungs = creutz_rungs(shapes)
    missing = [s for s in shapes if s not in table]
    area_seen = None
    if not missing:
        area_seen = any(table[x] != table[y] for x, y in comps)
    chis, zero_den = {}, []
    for (a, b) in rungs:
        if missing:
            break
        den = qs_mul(table[(a, b - 1)], table[(a - 1, b)])
        if qs_is_zero(den):
            zero_den.append((a, b))
            continue
        chis[(a, b)] = qs_div(qs_mul(table[(a, b)], table[(a - 1, b - 1)]),
                              den)
    vals = list(chis.values())
    defined = (not missing) and (not zero_den) and len(vals) == len(rungs) \
        and len(rungs) > 0 and len(comps) > 0
    unit = defined and all(v == (Fraction(1), Fraction(0)) for v in vals)
    const = defined and len(set(vals)) == 1
    branch = "NOT-DEGENERATE"
    if missing:
        word = "BLOCKED-AT-THE-LADDER"
    elif not defined:
        word = "DISCRIMINATOR-DEGENERATE"
        branch = "THE-DISCRIMINATORS-OWN-WELL-DEFINEDNESS-FAILS"
    elif area_seen and const and not unit:
        word = "CONFINES"
    elif (not area_seen) and unit:
        word = "DECONFINES"
    else:
        word = "DISCRIMINATOR-DEGENERATE"
        branch = "WELL-DEFINED-AND-MATCHING-NEITHER-SHAPE-OF-LAW"
    return {"area_comparisons": len(comps), "creutz_rungs": len(rungs),
            "missing_shapes": len(missing), "degenerate_branch": branch,
            "area_seen": area_seen,
            "creutz": {"%d-%d" % k: qs_str(v) for k, v in sorted(chis.items())},
            "creutz_zero_denominators": len(zero_den),
            "creutz_defined": defined, "creutz_is_unit": unit,
            "creutz_is_constant": const,
            "winding": qs_str(wind),
            "winding_word": ("WINDING-ORDER-ZERO" if qs_is_zero(wind)
                             else "WINDING-ORDER-NONZERO"),
            "ladder_word": word}


def measure_the_discriminator(S, pv, vb):
    """the discriminator's OWN well-definedness at the declared lattice,
    gated before a single expectation is computed: how many
    area-discriminating comparisons the ladder carries, how many Creutz
    rungs, and what the merging-index law says about how far a
    family-invariant claim may be carried."""
    lat = S["_lat"]
    extents = S["loop_family"]["simple_rectangle_extents"]
    shapes = [(a, b) for a in extents for b in extents]
    comps = area_comparisons(shapes)
    rungs = creutz_rungs(shapes)
    if mut("MUT-DISCRIMINATOR-RUNGS"):
        rungs = []
    perim = {}
    for (a, b) in shapes:
        perim.setdefault(a + b, []).append((a, b))
    ok = (len(comps) >= 1 and len(rungs) >= 1
          and vbwin(vb, "VB-PIN-DISCRIM", "G-THE-DISCRIMINATOR-IS-WELL-"
                    "DEFINED", "nonzero denominators; enough ladder rungs"))
    LD.gate("G-THE-DISCRIMINATOR-IS-WELL-DEFINED",
            "the discriminator's own well-definedness at the declared "
            "lattice is a MEASUREMENT taken before any row runs: the ladder "
            "must carry at least one comparison at equal perimeter and "
            "unequal area, and at least one Creutz rung; if it carried "
            "neither, the honest verdict would be that the discriminator is "
            "degenerate at this lattice and no row could rescue it",
            ok,
            "%d ladder shapes over extents %s; %d area-discriminating "
            "comparisons %s; %d Creutz rungs %s"
            % (len(shapes), extents, len(comps),
               ["%d-%d/%d-%d" % (x[0], x[1], y[0], y[1]) for x, y in comps],
               len(rungs), ["%d-%d" % r for r in rungs]))
    coins, cidx = S["_coins"], S["_cidx"]
    gimg = len({tuple(cidx[gauge_twist(m, k)] for m in coins)
                for k in range(phase_order())})
    lrows = []
    for Lv in (2, 4, 8, 16):
        res = realisable_twists(Lv)
        lrows.append({"L": Lv, "residual_order_on_the_torus": len(res),
                      "the_link_stencils_gauge_image": gimg,
                      "the_merging_index": gimg // len(res),
                      "the_odd_twist_is_a_gauge_transformation_here":
                          (gimg // len(res)) == 1})
    if mut("MUT-MERGING-LAW"):
        lrows[1]["the_merging_index"] = 1
    here = [r for r in lrows if r["L"] == lat.L][0]
    ok2 = (here["the_merging_index"] == pv["PV-ACT-MERGEIDX"]
           and gimg == phase_order()
           and all(r["the_merging_index"] == gimg // r[
               "residual_order_on_the_torus"] for r in lrows)
           and [r["the_merging_index"] for r in lrows if r["L"] == 8] == [1]
           and vbwin(vb, "VB-ACT-BOUNDARY",
                     "G-THE-MERGING-INDEX-LAW-REPRODUCED",
                     "it is %d" % [r["the_merging_index"] for r in lrows
                                   if r["L"] == 8][0])
           and vbwin(vb, "VB-PIN-LBOUND", "G-THE-MERGING-INDEX-LAW-"
                     "REPRODUCED", "8/gcd(L,8)"))
    LD.gate("G-THE-MERGING-INDEX-LAW-REPRODUCED",
            "the L-boundary is stated as a measured law and not as a quoted "
            "one: the merging index is eight over the greatest common "
            "divisor of L and eight, it is the parent's own value at the "
            "declared size, and it is one at every L divisible by eight -- "
            "where no class merges, so every claim this unit makes about "
            "the class structure carries its lattice scope",
            ok2,
            "the link stencil's gauge image is measured at %d distinct "
            "actions and the phase order is %d; %s"
            % (gimg, phase_order(),
               "; ".join("L=%d index %d" % (r["L"], r["the_merging_index"])
                         for r in lrows)))
    S["_shapes_ladder"] = shapes
    S["discriminator"] = {
        "definition": "AREA-AGAINST-PERIMETER-IN-THREE-LEGS-ALL-EXACT",
        "leg_area": "AT-EQUAL-PERIMETER-DOES-THE-EXPECTATION-MOVE-WITH-THE-"
                    "AREA",
        "leg_creutz": "CHI(A,B)=W(A,B)W(A-1,B-1)/(W(A,B-1)W(A-1,B))-ONE-FOR-"
                      "A-LAW-GEOMETRIC-IN-THE-PERIMETER",
        "leg_winding": "THE-WINDING-CYCLE-EXPECTATION-AS-THE-ORDER-"
                       "PARAMETER-ANALOGUE",
        "ladder_shapes": len(shapes),
        "ladder_extents": extents,
        "perimeter_classes": {str(k): len(v) for k, v in sorted(perim.items())},
        "area_discriminating_comparisons": len(comps),
        "the_comparisons": ["%d-%d/%d-%d" % (x[0], x[1], y[0], y[1])
                            for x, y in comps],
        "creutz_rungs": len(rungs),
        "the_rungs": ["%d-%d" % r for r in rungs],
        "well_defined_at_the_declared_L": ok,
        "the_L_boundary": lrows,
        "the_L_boundary_law": "THE-MERGING-INDEX-IS-8/GCD(L,8)",
        "family_level_pinning_dies_at": "L-DIVISIBLE-BY-EIGHT"}
    SEAL.take("THE DISCRIMINATOR", "discriminator",
              "G-THE-MERGING-INDEX-LAW-REPRODUCED", S["discriminator"])
    return shapes


# ===========================================================================
# SECTION 9.  THE SPECTRAL DECOMPOSITION OF THE LADDER
# ===========================================================================
# The ladder's dependence on the perimeter is fitted EXACTLY, from three
# points, to A + B s + C 2^(-s) -- the signature of a transfer object whose
# spectrum is {1, 1, 1/2} with the eigenvalue one carrying a two-block -- and
# then VERIFIED at every remaining point.  Nothing is fitted numerically and
# no exponential is called: 2^(-s) is an exact rational.

def mode_fit(f2, f3, f4):
    C = qs_add(qs_add(f2, f4), (-2 * f3[0], -2 * f3[1]))
    C = (16 * C[0], 16 * C[1])
    B = ((C[0] / 8) - (f2[0] - f3[0]), (C[1] / 8) - (f2[1] - f3[1]))
    A = (f2[0] - 2 * B[0] - C[0] / 4, f2[1] - 2 * B[1] - C[1] / 4)
    return A, B, C


def mode_value(A, B, C, s):
    return (A[0] + B[0] * s + C[0] / Fraction(2 ** s),
            A[1] + B[1] * s + C[1] / Fraction(2 ** s))


def perimeter_table(TR, coins_weight, shapes):
    """the expectation of the loop observable at each ladder shape under a
    declared measure on the carrier, as an exact element of Q(sqrt 2)."""
    out = {}
    for (a, b) in shapes:
        vals = TR[("RECTANGLE-CIRCUIT", a, b)]
        p = Fraction(0)
        q = Fraction(0)
        for i, w in coins_weight:
            p += w * vals[i][0]
            q += w * vals[i][1]
        out[(a, b)] = (p, q)
    return out


def support_pairs(mu):
    return [(i, w) for i, w in enumerate(mu) if w]


def measure_the_closed_form(S, pv):
    """the ladder's exact closed form, measured at every coin of the carrier
    before any measure is declared: three coefficients fitted from three
    points and verified at the rest, at BOTH declared lattice sizes."""
    lat, coins, TR = S["_lat"], S["_coins"], S["_TR"]
    extents = S["loop_family"]["simple_rectangle_extents"]
    shapes = S["_shapes_ladder"]
    per = {}
    for (a, b) in shapes:
        per.setdefault(a + b, []).append((a, b))
    ss = sorted(per)
    rep = {s: sorted(per[s])[0] for s in ss}
    perim_only, checked, selfcmp = 0, 0, 0
    for s in ss:
        base = TR[("RECTANGLE-CIRCUIT",) + rep[s]]
        for (a, b) in per[s]:
            v = TR[("RECTANGLE-CIRCUIT", a, b)]
            if (a, b) == rep[s]:
                selfcmp += len(coins)
            for i in range(len(coins)):
                checked += 1
                if v[i] != base[i]:
                    perim_only += 1
    pairs = [((a, b), (p, q)) for s in ss for (a, b) in per[s]
             for (p, q) in per[s] if (a, b) < (p, q)]
    pair_checked, pair_bad = 0, 0
    for x, y in pairs:
        vx, vy = TR[("RECTANGLE-CIRCUIT",) + x], TR[("RECTANGLE-CIRCUIT",) + y]
        for i in range(len(coins)):
            pair_checked += 1
            if vx[i] != vy[i]:
                pair_bad += 1
    acmp = area_comparisons(shapes)
    area_checked, area_bad = 0, 0
    for x, y in acmp:
        vx, vy = TR[("RECTANGLE-CIRCUIT",) + x], TR[("RECTANGLE-CIRCUIT",) + y]
        for i in range(len(coins)):
            area_checked += 1
            if vx[i] != vy[i]:
                area_bad += 1
    if mut("MUT-PERIMETER-ONLY"):
        perim_only = 1
    LD.gate("G-THE-LADDER-IS-A-FUNCTION-OF-THE-PERIMETER-ALONE",
            "at every coin of the carrier and at every pair of ladder "
            "shapes of equal perimeter, the loop observable takes the SAME "
            "value -- the area does not enter it.  This is measured "
            "per-configuration, not per-expectation, so it holds under "
            "every measure on this carrier without a second census.  The "
            "count is published on THREE bases, because the scheme reads "
            "each shape against its perimeter class's representative and so "
            "counts the representative against itself: the shape-by-coin "
            "count, the genuine cross-shape count inside it, and the "
            "complete unordered-pair count, of which the "
            "area-discriminating comparisons are the sub-basis the area "
            "finding is claimed on",
            perim_only == 0 and pair_bad == 0 and area_bad == 0,
            "%d shape-by-coin comparisons at equal perimeter, %d "
            "disagreements (%d of them a shape against itself, %d genuine "
            "cross-shape); %d unordered-pair-by-coin comparisons, %d "
            "disagreements; %d area-discriminating comparison-by-coin "
            "checks, %d disagreements"
            % (checked, perim_only, selfcmp, checked - selfcmp, pair_checked,
               pair_bad, area_checked, area_bad))
    modes, bad = [], 0
    f = {s: TR[("RECTANGLE-CIRCUIT",) + rep[s]] for s in ss}
    for i in range(len(coins)):
        A, B, C = mode_fit(f[ss[0]][i], f[ss[1]][i], f[ss[2]][i])
        for s in ss[3:]:
            if mode_value(A, B, C, s) != f[s][i]:
                bad += 1
        modes.append((A, B, C))
    if mut("MUT-CLOSED-FORM"):
        bad = len(coins)
    LD.gate("G-THE-LADDER-CLOSED-FORM",
            "the ladder's dependence on the perimeter is fitted EXACTLY "
            "from three points to a constant, a term proportional to the "
            "perimeter and a term halving with it, and then VERIFIED at "
            "every remaining point of the ladder at every coin -- an "
            "over-determined test, not a fit",
            bad == 0,
            "%d coins, ladder over perimeters %s, %d verification points "
            "each, %d failures"
            % (len(coins), ss, len(ss) - 3, bad))
    prof = {"A": {}, "B": {}, "C": {}}
    for (A, B, C) in modes:
        for nm, v in (("A", A), ("B", B), ("C", C)):
            prof[nm][qs_str(v)] = prof[nm].get(qs_str(v), 0) + 1
    sect_of_C = {}
    for i, m in enumerate(coins):
        key = (coin_sector(m), qs_str(modes[i][2]))
        sect_of_C[key] = sect_of_C.get(key, 0) + 1
    S["_modes"] = modes
    S["_perim_reps"] = rep
    S["_perims"] = ss
    S["closed_form"] = {
        "the_form": "W(A,B)=A+B*(A+B)+C*2^-(A+B)",
        "the_ladder_is_a_function_of_the_perimeter_alone": perim_only == 0,
        "equal_perimeter_comparisons": checked,
        "equal_perimeter_disagreements": perim_only,
        "equal_perimeter_self_comparisons": selfcmp,
        "equal_perimeter_cross_shape_comparisons": checked - selfcmp,
        "unordered_equal_perimeter_pairs": len(pairs),
        "unordered_pair_by_coin_comparisons": pair_checked,
        "unordered_pair_disagreements": pair_bad,
        "area_discriminating_comparisons": len(acmp),
        "area_discriminating_comparison_by_coin_checks": area_checked,
        "area_discriminating_disagreements": area_bad,
        "perimeters": ss,
        "verification_points_per_coin": len(ss) - 3,
        "closed_form_failures": bad,
        "coefficient_profile": {k: dict(sorted(v.items())) for k, v in
                                prof.items()},
        "the_halving_mode_by_sector": {("%s/%s" % k): v for k, v in
                                       sorted(sect_of_C.items())},
        "the_transfer_spectrum": "{1,1,1/2}",
        "the_gap": "1/2",
        "why_the_eigenvalue_one_appears_twice":
            "THE-TERM-PROPORTIONAL-TO-THE-PERIMETER-IS-A-TWO-BLOCK-AT-"
            "EIGENVALUE-ONE"}
    SEAL.take("THE CLOSED FORM", "closed_form", "G-THE-LADDER-CLOSED-FORM",
              S["closed_form"])
    return modes


# ===========================================================================
# SECTION 10.  MODE (a) -- THE EXPECTATIONS AT THE DECLARED ROWS
# ===========================================================================

def gibbs(weights, e):
    raw = [w ** e for w in weights]
    Z = sum(raw)
    return [r / Z for r in raw]


def measure_declared_rows(S, pv, vb):
    """four declared weight systems, each stamped on its own row: the null,
    the conjugation-symmetric Wilson shape at a declared coupling, an
    exhibited witness, and the law-native CONTROL whose stamp is carried
    verbatim from the parent's receipt and never spent as derived."""
    coins, TR = S["_coins"], S["_TR"]
    classes = S["_classes"]
    shapes = S["_shapes_ladder"]
    n = len(coins)
    e_link = pv["PV-ACT-EXPONENT"]
    e_plaq = len(S["_lat"].plaquettes)
    plaq = TR[("RECTANGLE-CIRCUIT", 1, 1)]
    top = max(plaq, key=lambda v: (v[0], v[1]))
    one, two = Fraction(1), Fraction(2)
    rows, mus = [], {}

    mu_null = gibbs([one] * n, e_link)
    mus["THE-NULL"] = mu_null
    rows.append({"row": "THE-NULL",
                 "weight_system": "W-IDENTICALLY-ONE",
                 "grain": "LINK", "exponent": e_link,
                 "the_measure": "COUNTING"})

    w_wil = [two if plaq[i] == top else one for i in range(n)]
    conj_sym = all((w_wil[i] == w_wil[j]) for i in range(n)
                   for j in range(n) if plaq[i] == plaq[j])
    mus["THE-WILSON-CONJUGATION-SYMMETRIC"] = gibbs(w_wil, e_plaq)
    rows.append({"row": "THE-WILSON-CONJUGATION-SYMMETRIC",
                 "weight_system": "TWO-AT-THE-TOP-TRACE-VALUE-AND-ONE-"
                                  "ELSEWHERE",
                 "grain": "PLAQUETTE", "exponent": e_plaq,
                 "the_measure": "NEW"})

    w_wit = [two if i in set(classes[1]) else one for i in range(n)]
    mus["THE-EXHIBITED-WITNESS"] = gibbs(w_wit, e_link)
    rows.append({"row": "THE-EXHIBITED-WITNESS",
                 "weight_system": "TWO-ON-ONE-CLASS-AND-ONE-ELSEWHERE",
                 "grain": "LINK", "exponent": e_link,
                 "the_measure": "NEW"})

    sect = {}
    for i, m in enumerate(coins):
        sect.setdefault(coin_sector(m), []).append(i)
    lawv = {"DIAGONAL": Fraction(pv["PV-ACT-LAW1"]),
            "ANTIDIAGONAL": Fraction(pv["PV-ACT-LAW2"]),
            "BALANCED": Fraction(pv["PV-ACT-LAW3"])}
    mu_law = [Fraction(0)] * n
    for k, idx in sect.items():
        for i in idx:
            mu_law[i] = lawv[k] / len(idx)
    mus["THE-LAW-NATIVE-CONTROL"] = mu_law
    rows.append({"row": "THE-LAW-NATIVE-CONTROL",
                 "weight_system": "THE-TRANSPORTED-SECTOR-LAW",
                 "grain": "SECTOR", "exponent": 1,
                 "the_measure": "TRANSPORTED-NOT-DERIVED"})

    plaq_exp = {}
    for r in rows:
        mu = mus[r["row"]]
        sup = support_pairs(mu)
        tab = perimeter_table(TR, sup, shapes)
        wind = (Fraction(0), Fraction(0))
        wv = TR[("STRAIGHT-WINDING-CYCLE", 1, 0)]
        p = Fraction(0)
        q = Fraction(0)
        for i, w in sup:
            p += w * wv[i][0]
            q += w * wv[i][1]
        wind = (p, q)
        v = classify(tab, wind, shapes)
        A, B, C = mode_fit(*[tab[S["_perim_reps"][s]] for s in S["_perims"][:3]])
        modeok = all(mode_value(A, B, C, s) == tab[S["_perim_reps"][s]]
                     for s in S["_perims"][3:])
        r.update(v)
        r["plaquette_expectation"] = qs_str(tab[(1, 1)])
        r["ladder"] = {str(s): qs_str(tab[S["_perim_reps"][s]])
                       for s in S["_perims"]}
        r["mode_A"] = qs_str(A)
        r["mode_B"] = qs_str(B)
        r["mode_C"] = qs_str(C)
        r["closed_form_holds"] = modeok
        r["stamp"] = "CONDITIONAL-ON-THE-DECLARED-WEIGHTS"
        plaq_exp[r["row"]] = qs_str(tab[(1, 1)])
    if mut("MUT-ROW-UNSTAMPED"):
        rows[2]["stamp"] = "PLAIN"
    stamped = all(r["stamp"] == "CONDITIONAL-ON-THE-DECLARED-WEIGHTS"
                  for r in rows)
    ok = (stamped and conj_sym
          and plaq_exp["THE-NULL"] == pv["PV-ACT-NULL"]
          and plaq_exp["THE-EXHIBITED-WITNESS"] == pv["PV-ACT-WITNESS"]
          and plaq_exp["THE-WILSON-CONJUGATION-SYMMETRIC"]
          == pv["PV-ACT-WILSONEXP"]
          and all(r["closed_form_holds"] for r in rows))
    LD.gate("G-THE-DECLARED-ROWS-BUILT",
            "each declared weight system is rebuilt here and its "
            "plaquette expectation is required to equal the parent's own "
            "published number at a named receipt path before any larger "
            "loop is believed; the Wilson weight is measured to be a "
            "function of the trace's conjugation-symmetric invariant; every "
            "row carries the stamp CONDITIONAL-ON-THE-DECLARED-WEIGHTS on "
            "its own row, so an unstamped expectation stops the run",
            ok,
            "%d rows, all stamped %s, conjugation-symmetric %s; plaquette "
            "expectations %s" % (len(rows), stamped, conj_sym,
                                 sorted(plaq_exp.items())))
    stamp = pv["PV-ACT-STAMP"]
    ctrl = [r for r in rows if r["row"] == "THE-LAW-NATIVE-CONTROL"][0]
    if mut("MUT-CONTROL-SPENT"):
        ctrl = dict(ctrl, the_measure="DERIVED")
    ok2 = (stamp == "LAW-RATED-CONSTRUCTION-DECLARED-AT-AN-UNPINNED-"
                    "IDENTIFICATION"
           and ctrl["the_measure"] == "TRANSPORTED-NOT-DERIVED"
           and sum(mu_law) == 1
           and vbwin(vb, "VB-ACT-STAMP", "G-THE-CONTROL-STAMP-CARRIED",
                     "must not treat it as a derived measure"))
    LD.gate("G-THE-CONTROL-STAMP-CARRIED",
            "the law-native row enters this unit AS A CONTROL: its stamp is "
            "carried VERBATIM from the parent's receipt, its three sector "
            "masses are read at a named path and required to normalise, and "
            "its row is published as a TRANSPORTED law value and never as a "
            "derived measure -- a row that called it derived would stop the "
            "run",
            ok2,
            "stamp %r; the row's measure field is %s; the sector law %s "
            "sums to %s" % (stamp, ctrl["the_measure"],
                            [pv["PV-ACT-LAW1"], pv["PV-ACT-LAW2"],
                             pv["PV-ACT-LAW3"]], sum(mu_law)))
    S["_mus"] = mus
    t1, w1 = {}, {}
    for r in rows:
        t1[r["ladder_word"]] = t1.get(r["ladder_word"], 0) + 1
        w1[r["winding_word"]] = w1.get(r["winding_word"], 0) + 1
    S["conditional_rows"] = {
        "mode": "(a)-CONDITIONAL-AT-THE-DECLARED-ROWS",
        "ladder_word_tally": dict(sorted(t1.items())),
        "winding_word_tally": dict(sorted(w1.items())),
        "stamp": "CONDITIONAL-ON-THE-DECLARED-WEIGHTS",
        "rows": rows,
        "the_control_stamp": stamp,
        "the_control_is_never_spent_as_derived": True,
        "the_wilson_weight_is_conjugation_symmetric": conj_sym}
    SEAL.take("THE CONDITIONAL ROWS", "conditional_rows",
              "G-THE-CONTROL-STAMP-CARRIED", S["conditional_rows"])
    return rows


# ===========================================================================
# SECTION 11.  MODE (b) -- THE FAMILY SWEEP OVER THE EXTREME POINTS
# ===========================================================================

def measure_family_sweep(S, pv):
    """every extreme point of the reachable set is a declared measure and
    every one is run: the uniform measure on each class.  E-24: the integers
    here are COUNTS over the extreme points, and no count becomes a
    probability without a declared measure."""
    TR, classes = S["_TR"], S["_classes"]
    shapes = S["_shapes_ladder"]
    wv = TR[("STRAIGHT-WINDING-CYCLE", 1, 0)]
    rows = []
    for k, c in enumerate(classes):
        sup = [(i, Fraction(1, len(c))) for i in c]
        tab = perimeter_table(TR, sup, shapes)
        p = sum(Fraction(1, len(c)) * wv[i][0] for i in c)
        q = sum(Fraction(1, len(c)) * wv[i][1] for i in c)
        v = classify(tab, (p, q), shapes)
        A, B, C = mode_fit(*[tab[S["_perim_reps"][s]]
                             for s in S["_perims"][:3]])
        rows.append({
            "extreme_point": k, "size": len(c),
            "kind": "VERTEX" if len(c) == 1 else "EDGE-MIDPOINT",
            "area_seen": v["area_seen"],
            "ladder_word": v["ladder_word"],
            "creutz_defined": v["creutz_defined"],
            "creutz_is_unit": v["creutz_is_unit"],
            "creutz_is_constant": v["creutz_is_constant"],
            "degenerate_branch": v["degenerate_branch"],
            "winding_word": v["winding_word"],
            "winding": v["winding"],
            "mode_A": qs_str(A), "mode_B": qs_str(B), "mode_C": qs_str(C),
            "ladder_is_constant_in_the_perimeter":
                qs_is_zero(B) and qs_is_zero(C),
            "active_modes": sum(1 for x in (A, B, C) if not qs_is_zero(x))})
    if mut("MUT-SWEEP-TRUNCATED"):
        rows = rows[:-1]
    def tally(key):
        d = {}
        for r in rows:
            d[str(r[key])] = d.get(str(r[key]), 0) + 1
        return dict(sorted(d.items()))
    area = tally("area_seen")
    ladder = tally("ladder_word")
    windw = tally("winding_word")
    modes = tally("active_modes")
    branches = tally("degenerate_branch")
    flat = tally("ladder_is_constant_in_the_perimeter")
    invariant, dependent = [], []
    for key in ("area_seen", "ladder_word", "creutz_is_unit", "winding_word",
                "mode_A", "mode_B", "mode_C", "active_modes"):
        (invariant if len({str(r[key]) for r in rows}) == 1
         else dependent).append(key)
    ok = (len(rows) == len(classes) and len(rows) == pv["PV-ACT-ORBITS"]
          and area.get("False") == len(rows) and len(invariant) >= 1
          and len(dependent) >= 1)
    LD.gate("G-THE-FAMILY-SWEEP-IS-TOTAL",
            "the sweep runs EVERY extreme point of the reachable set, not a "
            "sample: each observable is then classified FAMILY-INVARIANT or "
            "coupling-dependent by whether its value moves across those "
            "extreme points, and both arms are required to be populated so "
            "that neither classification is vacuous",
            ok,
            "%d extreme points swept; area-seen tally %s; ladder tally %s; "
            "winding tally %s; %d family-invariant and %d coupling-dependent "
            "observables" % (len(rows), area, ladder, windw, len(invariant),
                             len(dependent)))
    S["_sweep"] = rows
    t2, w2 = {}, {}
    for r in rows:
        t2[r["ladder_word"]] = t2.get(r["ladder_word"], 0) + 1
        w2[r["winding_word"]] = w2.get(r["winding_word"], 0) + 1
    S["family_sweep"] = {
        "mode": "(b)-FAMILY-SWEPT-OVER-THE-EXTREME-POINTS",
        "ladder_word_tally": dict(sorted(t2.items())),
        "winding_word_tally": dict(sorted(w2.items())),
        "every_integer_here_is_a_count": "COUNTING-ONLY-E-24-NO-MEASURE-"
                                         "OVER-THE-FAMILY-IS-DECLARED",
        "extreme_points": len(rows),
        "vertices": sum(1 for r in rows if r["kind"] == "VERTEX"),
        "edge_midpoints": sum(1 for r in rows if r["kind"] == "EDGE-MIDPOINT"),
        "area_seen_tally": area,
        "ladder_word_tally": ladder,
        "winding_word_tally": windw,
        "active_mode_tally": modes,
        "degenerate_branch_tally": branches,
        "constant_in_the_perimeter_tally": flat,
        "family_invariant_observables": invariant,
        "coupling_dependent_observables": dependent,
        "rows": rows}
    SEAL.take("THE FAMILY SWEEP", "family_sweep",
              "G-THE-FAMILY-SWEEP-IS-TOTAL", S["family_sweep"])
    return rows


def measure_the_constant_ladder_identity(S, pv):
    """WHICH 24?  The Creutz leg returns one at 24 of the 136 extreme points,
    and this unit measures WHICH 24 rather than asserting it: the set on
    which the ratio is one is required to be, elementwise, the set on which
    the ladder does not move with the perimeter at all.  The mechanism is
    measured as well, by driving the REAL discriminator with three synthetic
    single-mode ladders -- so 'a single mode is active' is separated from
    'the ratio is one' by a measurement and not by a sentence."""
    rows, shapes = S["_sweep"], S["_shapes_ladder"]
    unit = {r["extreme_point"] for r in rows if r["creutz_is_unit"]}
    const = {r["extreme_point"] for r in rows
             if r["ladder_is_constant_in_the_perimeter"]}
    if mut("MUT-CONSTANT-SET"):
        const = set(sorted(const)[1:])
    single = [r["extreme_point"] for r in rows if r["active_modes"] == 1]
    onlyB = [r["extreme_point"] for r in rows
             if r["active_modes"] == 1 and r["mode_B"] != "0"]
    Avals = {}
    for r in rows:
        if r["extreme_point"] in const:
            Avals[r["mode_A"]] = Avals.get(r["mode_A"], 0) + 1
    mech = []
    for nm, fn in (("THE-CONSTANT-MODE-ALONE", lambda p: Fraction(1)),
                   ("THE-PERIMETER-PROPORTIONAL-MODE-ALONE",
                    lambda p: Fraction(2 * p)),
                   ("THE-HALVING-MODE-ALONE",
                    lambda p: Fraction(1, 2 ** p))):
        tab = {(a, b): (fn(a + b), Fraction(0)) for (a, b) in shapes}
        v = classify(tab, (Fraction(0), Fraction(0)), shapes)
        mech.append({"single_mode_ladder": nm,
                     "creutz_by_rung": v["creutz"],
                     "creutz_is_unit": v["creutz_is_unit"],
                     "ladder_word": v["ladder_word"]})
    byA = [m for m in mech if m["single_mode_ladder"].endswith(
        "THE-CONSTANT-MODE-ALONE")][0]
    byB = [m for m in mech if "PERIMETER-PROPORTIONAL" in
           m["single_mode_ladder"]][0]
    byC = [m for m in mech if "HALVING" in m["single_mode_ladder"]][0]
    halving_only = [r["extreme_point"] for r in rows
                    if r["active_modes"] == 1 and r["mode_C"] != "0"]
    ok = (unit == const
          and len(onlyB) == len(single) - len(unit)
          and all(r["mode_A"] != "0" for r in rows
                  if r["extreme_point"] in const)
          and byA["creutz_is_unit"] and byC["creutz_is_unit"]
          and not byB["creutz_is_unit"])
    LD.gate("G-THE-CREUTZ-UNIT-SET-IS-THE-CONSTANT-LADDER-SET",
            "the extreme points where the Creutz ratio is one are "
            "characterised BY A MEASUREMENT and elementwise: that set is "
            "required to be exactly the set at which the ladder is constant "
            "in the perimeter, so the word the classifier prints there "
            "records a flat ladder and nothing else.  The mechanism is "
            "measured too, through the real discriminator on three "
            "synthetic single-mode ladders: a constant ladder and a halving "
            "ladder both return one at every rung, a perimeter-proportional "
            "ladder does not, and a single active mode therefore does NOT "
            "imply the ratio is one",
            ok,
            "the ratio is one at %d extreme points and the ladder is "
            "constant in the perimeter at %d, the two sets equal %s; a "
            "single mode is active at %d, of which %d carry the "
            "perimeter-proportional mode alone %s; the constant values "
            "there are %s; the synthetic single-mode ladders return unit "
            "%s and the perimeter-proportional one returns %s"
            % (len(unit), len(const), unit == const, len(single), len(onlyB),
               onlyB, dict(sorted(Avals.items())),
               [m["creutz_is_unit"] for m in mech], byB["creutz_by_rung"]))
    S["constant_ladder_identity"] = {
        "every_integer_here_is_a_count": "COUNTING-ONLY-E-24",
        "the_creutz_ratio_is_one_at": len(unit),
        "the_ladder_is_constant_in_the_perimeter_at": len(const),
        "the_two_sets_are_equal": unit == const,
        "single_mode_extreme_points": len(single),
        "single_mode_but_perimeter_proportional": len(onlyB),
        "which_ones": onlyB,
        "single_mode_and_halving_only": len(halving_only),
        "the_constant_values_on_that_set": dict(sorted(Avals.items())),
        "the_mechanism_at_single_mode_ladders": mech,
        "the_reading": "DECONFINES-RECORDS-A-FLAT-LADDER-AT-THIS-ARENA-AND-"
                       "IS-NOT-A-FINDING-THAT-ANYTHING-DECONFINES"}
    SEAL.take("THE CONSTANT-LADDER IDENTITY", "constant_ladder_identity",
              "G-THE-CREUTZ-UNIT-SET-IS-THE-CONSTANT-LADDER-SET",
              S["constant_ladder_identity"])
    return unit


def measure_the_length_reading(S, pv):
    """THE SCOPE OF THE PERIMETER-ONLY THEOREM, measured at its boundary.
    The theorem is about the RECTANGLE LADDER.  Over the wider declared
    family the loop's own length is measured NOT to determine the
    observable: the declared shapes are grouped by step count and every
    group with more than one member is read coin by coin."""
    TR, coins = S["_TR"], S["_coins"]
    rows = S["loop_observable"]["base_point_rows"]
    key = {"%s-%d-%d" % k: k for k in S["_shapes"]}
    bylen = {}
    for r in rows:
        bylen.setdefault(r["length"], []).append(r["shape"])
    out, witness = [], None
    for ln in sorted(bylen):
        names = sorted(bylen[ln])
        ks = [key[n] for n in names]
        dis = 0
        for i in range(len(coins)):
            if len({TR[k][i] for k in ks}) > 1:
                dis += 1
                if witness is None and len(names) > 1:
                    lo = sorted(ks, key=str)
                    witness = {"step_count": ln, "coin": i,
                               "coin_sector": coin_sector(coins[i]),
                               "shape": "%s-%d-%d" % lo[0],
                               "value": qs_str(TR[lo[0]][i]),
                               "other_shape": "%s-%d-%d" % lo[-1],
                               "other_value": qs_str(TR[lo[-1]][i])}
        out.append({"step_count": ln, "shapes_of_that_length": len(names),
                    "the_shapes": names, "coins_at_which_they_disagree": dis,
                    "coins": len(coins)})
    if mut("MUT-LENGTH-READING"):
        out = [dict(r, coins_at_which_they_disagree=0) for r in out]
    groups = [r for r in out if r["shapes_of_that_length"] > 1]
    split = [r for r in groups if r["coins_at_which_they_disagree"] > 0]
    rect_only = [r for r in groups
                 if all(n.startswith("RECTANGLE-CIRCUIT") for n in
                        r["the_shapes"])]
    ok = (len(groups) > 0 and len(split) > 0
          and all(r["coins_at_which_they_disagree"] == 0 for r in rect_only)
          and all(any(not n.startswith("RECTANGLE-CIRCUIT")
                      for n in r["the_shapes"]) for r in split)
          and witness is not None)
    LD.gate("G-THE-LENGTH-DOES-NOT-DETERMINE-THE-OBSERVABLE",
            "the perimeter-only theorem's SCOPE is measured at its own "
            "boundary: over the wider declared family the loop's own length "
            "is required NOT to determine the observable, so the theorem is "
            "the rectangle ladder's and is not carried to the family.  "
            "Every group of shapes sharing a step count is read coin by "
            "coin, every group on which only rectangles occur is required "
            "to agree everywhere, and at least one mixed group is required "
            "to disagree -- with an explicit witness published",
            ok,
            "%d step-count groups with more than one shape, %d of them "
            "disagreeing at some coin, %d rectangle-only groups agreeing "
            "everywhere; witness %s"
            % (len(groups), len(split), len(rect_only), witness))
    S["length_reading"] = {
        "every_integer_here_is_a_count": "COUNTING-ONLY-E-24",
        "rows": out,
        "groups_with_more_than_one_shape": len(groups),
        "groups_disagreeing_at_some_coin": len(split),
        "rectangle_only_groups": len(rect_only),
        "the_witness": witness,
        "the_reading": "THE-PERIMETER-ONLY-THEOREM-IS-THE-RECTANGLE-LADDERS-"
                       "AND-THE-LENGTH-DOES-NOT-DETERMINE-THE-OBSERVABLE-ON-"
                       "THE-WIDER-FAMILY"}
    SEAL.take("THE LENGTH READING", "length_reading",
              "G-THE-LENGTH-DOES-NOT-DETERMINE-THE-OBSERVABLE",
              S["length_reading"])
    return out


LCG_MODULUS = (1 << 31) - 1
LCG_MULTIPLIER = 1103515245
LCG_INCREMENT = 12345
LCG_SEED = 20260815
INTERIOR_MEASURES = 1500
INTERIOR_WEIGHT_RANGE = 1024


def measure_the_universal_over_measures(S, pv):
    """THE AREA-BLINDNESS UNIVERSAL, grounded where it actually lives.  The
    per-configuration identity of section 5 says the two shapes of an
    area-discriminating comparison take the SAME value at every coin.  The
    difference of expectations is then a ratio whose numerator is LINEAR in
    the measure, so vanishing at each of the 640 point masses forces it to
    vanish at every measure on this carrier.  Both ends are executed: the
    640 Dirac measures, which are the point masses themselves, and 1500
    declared interior measures of full support, drawn by a declared integer
    recurrence so that the draw is reproducible to the byte."""
    TR, coins, shapes = S["_TR"], S["_coins"], S["_shapes_ladder"]
    comps = area_comparisons(shapes)
    need = sorted({s for pair in comps for s in pair})
    den = 1
    for sh in need:
        for v in TR[("RECTANGLE-CIRCUIT",) + sh]:
            for c in v:
                d = c.denominator
                g, x = den, d
                while x:
                    g, x = x, g % x
                den = den // g * d
    ints = {sh: [(int(v[0] * den), int(v[1] * den))
                 for v in TR[("RECTANGLE-CIRCUIT",) + sh]] for sh in need}
    exact = all(Fraction(a, den) == v[0] and Fraction(b, den) == v[1]
                for sh in need
                for (a, b), v in zip(ints[sh],
                                     TR[("RECTANGLE-CIRCUIT",) + sh]))
    dirac, dirac_bad = 0, 0
    for i in range(len(coins)):
        for x, y in comps:
            dirac += 1
            if TR[("RECTANGLE-CIRCUIT",) + x][i] != \
                    TR[("RECTANGLE-CIRCUIT",) + y][i]:
                dirac_bad += 1
    st = LCG_SEED
    interior, interior_bad, full = 0, 0, 0
    rng = range(len(coins))
    for _m in range(INTERIOR_MEASURES):
        w = []
        for _i in rng:
            st = (LCG_MULTIPLIER * st + LCG_INCREMENT) % LCG_MODULUS
            w.append(1 + (st % INTERIOR_WEIGHT_RANGE))
        if all(x > 0 for x in w):
            full += 1
        tot = {}
        for sh in need:
            vs = ints[sh]
            p, q = 0, 0
            for i in rng:
                wi = w[i]
                p += wi * vs[i][0]
                q += wi * vs[i][1]
            tot[sh] = (p, q)
        for x, y in comps:
            interior += 1
            if tot[x] != tot[y]:
                interior_bad += 1
    if mut("MUT-UNIVERSAL"):
        interior_bad = 1
    ok = (exact and dirac_bad == 0 and interior_bad == 0
          and full == INTERIOR_MEASURES
          and dirac == len(coins) * len(comps)
          and interior == INTERIOR_MEASURES * len(comps))
    LD.gate("G-THE-AREA-BLINDNESS-IS-UNIVERSAL-OVER-MEASURES",
            "the universal is licensed where it lives: the difference of "
            "two expectations at an area-discriminating comparison is a "
            "ratio whose NUMERATOR IS LINEAR in the measure, so vanishing "
            "at the point masses forces it to vanish on their whole hull.  "
            "Both ends are executed rather than argued -- every one of the "
            "carrier's Dirac measures, and a declared block of interior "
            "measures of full support drawn by an integer recurrence, "
            "compared on exact integer numerators over one common "
            "denominator",
            ok,
            "common denominator %d, the rescaling is exact %s; %d Dirac "
            "comparisons, %d mismatches; %d interior comparisons at %d "
            "measures of full support, %d mismatches"
            % (den, exact, dirac, dirac_bad, interior, INTERIOR_MEASURES,
               interior_bad))
    S["the_universal"] = {
        "the_ground": "THE-PER-CONFIGURATION-IDENTITY-PLUS-LINEARITY-OF-THE-"
                      "NUMERATOR-OF-THE-DIFFERENCE-OF-EXPECTATIONS",
        "area_discriminating_comparisons": len(comps),
        "dirac_measures": len(coins),
        "dirac_comparisons": dirac,
        "dirac_mismatches": dirac_bad,
        "interior_measures": INTERIOR_MEASURES,
        "interior_measures_of_full_support": full,
        "interior_comparisons": interior,
        "interior_mismatches": interior_bad,
        "comparisons_in_all": dirac + interior,
        "mismatches_in_all": dirac_bad + interior_bad,
        "the_draw": "AN-INTEGER-RECURRENCE-WITH-A-DECLARED-SEED-NO-LIBRARY-"
                    "RANDOMNESS",
        "the_seed": LCG_SEED,
        "the_common_denominator": den,
        "the_scope": "EVERY-MEASURE-ON-THIS-CARRIER-NOT-ONLY-THE-ALLOWED-"
                     "WEIGHT-SYSTEMS"}
    SEAL.take("THE UNIVERSAL", "the_universal",
              "G-THE-AREA-BLINDNESS-IS-UNIVERSAL-OVER-MEASURES",
              S["the_universal"])
    return interior


def measure_family_slices(S, pv):
    """exact one-parameter slices of the allowed space: the weight system
    taking a declared value on one class and one elsewhere, at three exact
    rational couplings.  A slice is not an extreme point, so it tests
    whether the sweep's verdict is a property of the corners alone."""
    TR, classes, coins = S["_TR"], S["_classes"], S["_coins"]
    shapes = S["_shapes_ladder"]
    e = pv["PV-ACT-EXPONENT"]
    wv = TR[("STRAIGHT-WINDING-CYCLE", 1, 0)]
    rows = []
    for ci in (0, 1, 2):
        for t in (Fraction(1, 2), Fraction(2), Fraction(4)):
            w = [t if i in set(classes[ci]) else Fraction(1)
                 for i in range(len(coins))]
            mu = gibbs(w, e)
            sup = support_pairs(mu)
            tab = perimeter_table(TR, sup, shapes)
            p = sum(x * wv[i][0] for i, x in sup)
            q = sum(x * wv[i][1] for i, x in sup)
            v = classify(tab, (p, q), shapes)
            rows.append({"class": ci, "coupling": str(t),
                         "class_size": len(classes[ci]),
                         "class_sector": sorted({coin_sector(coins[i])
                                                 for i in classes[ci]})[0],
                         "area_seen": v["area_seen"],
                         "ladder_word": v["ladder_word"],
                         "winding_word": v["winding_word"],
                         "ladder": {str(s): qs_str(tab[S["_perim_reps"][s]])
                                    for s in S["_perims"]},
                         "plaquette_expectation": qs_str(tab[(1, 1)])})
    if mut("MUT-SLICES"):
        rows[0]["area_seen"] = True
    ladders = {str(sorted(r["ladder"].items())) for r in rows}
    ok = (len(rows) == 9 and all(r["area_seen"] is False for r in rows)
          and len({r["plaquette_expectation"] for r in rows}) > 1)
    LD.gate("G-THE-FAMILY-SLICES",
            "the interior of the allowed space is sampled by exact "
            "one-parameter slices as well as its corners -- one class raised "
            "to three declared exact rational couplings -- and the "
            "area leg's verdict is required to be the same there, while the "
            "expectations themselves are required to MOVE, so the slice is "
            "not a constant row wearing a parameter",
            ok,
            "%d slices; distinct plaquette expectations %d; %d distinct "
            "ladders over %d classes of sizes %s in sectors %s; area-seen "
            "at %d of them"
            % (len(rows), len({r["plaquette_expectation"] for r in rows}),
               len(ladders), len({r["class"] for r in rows}),
               sorted({r["class_size"] for r in rows}),
               sorted({r["class_sector"] for r in rows}),
               sum(1 for r in rows if r["area_seen"])))
    S["family_slices"] = {"slices": len(rows), "rows": rows,
                          "the_coupling_values": ["1/2", "2", "4"],
                          "distinct_classes_raised": len({r["class"]
                                                          for r in rows}),
                          "distinct_ladders_returned": len(ladders),
                          "distinct_plaquette_expectations":
                              len({r["plaquette_expectation"] for r in rows}),
                          "the_classes_raised_are_of_one_kind":
                              len({(r["class_size"], r["class_sector"])
                                   for r in rows}) == 1}
    SEAL.take("THE FAMILY SLICES", "family_slices", "G-THE-FAMILY-SLICES",
              S["family_slices"])
    return rows


# ===========================================================================
# SECTION 12.  THE PRICE BINDING
# ===========================================================================
# Does the discriminator's verdict PARTITION the coupling inventory the
# parent handed over?  A coupling is a coordinate of the allowed space modulo
# normalisation: fixing the first class as the normalisation base leaves one
# coupling per remaining class, and the coupling's own strong limit is the
# extreme point on that class.  The partition is therefore a count over the
# extreme points, taken leg by leg, and it is measured rather than argued.

def measure_the_price_binding(S, pv, vb):
    rows = S["_sweep"]
    classes = S["_classes"]
    base = 0
    couplings = [r for r in rows if r["extreme_point"] != base]
    legs = []
    for name, key in (("LEG-AREA", "area_seen"),
                      ("LEG-CREUTZ-WORD", "ladder_word"),
                      ("LEG-CREUTZ-UNIT", "creutz_is_unit"),
                      ("LEG-CREUTZ-DEFINED", "creutz_defined"),
                      ("LEG-WINDING", "winding_word"),
                      ("MODE-A-CONSTANT", "mode_A"),
                      ("MODE-B-PERIMETER", "mode_B"),
                      ("MODE-C-HALVING", "mode_C"),
                      ("ACTIVE-MODES", "active_modes")):
        tal, tal_c = {}, {}
        for r in rows:
            tal[str(r[key])] = tal.get(str(r[key]), 0) + 1
        for r in couplings:
            tal_c[str(r[key])] = tal_c.get(str(r[key]), 0) + 1
        legs.append({
            "leg": name, "field": key,
            "distinct_values_over_the_extreme_points": len(tal),
            "partitions": len(tal) > 1,
            "tally_over_the_136_extreme_points": dict(sorted(tal.items())),
            "tally_over_the_couplings": dict(sorted(tal_c.items())),
            "verdict": ("PARTITIONS-THE-INVENTORY" if len(tal) > 1
                        else "FAMILY-INVARIANT")})
    if mut("MUT-PRICE-PARTITION"):
        legs[0]["verdict"] = "PARTITIONS-THE-INVENTORY"
    zeroC = sum(1 for r in rows if r["mode_C"] == "0")
    zeroB = sum(1 for r in rows if r["mode_B"] == "0")
    windzero = sum(1 for r in rows if r["winding_word"] == "WINDING-ORDER-ZERO")
    undef = sum(1 for r in rows if not r["creutz_defined"])
    area_leg = [l for l in legs if l["leg"] == "LEG-AREA"][0]
    wind_leg = [l for l in legs if l["leg"] == "LEG-WINDING"][0]
    ok = (len(couplings) == pv["PV-ACT-COUPLINGS"]
          and area_leg["verdict"] == "FAMILY-INVARIANT"
          and wind_leg["partitions"]
          and sum(area_leg["tally_over_the_136_extreme_points"].values())
          == len(classes)
          and vbwin(vb, "VB-SMU-PRICE", "G-THE-PRICE-BINDING",
                    "surjects onto the invariant simplex"))
    LD.gate("G-THE-PRICE-BINDING",
            "the partition question is answered LEG BY LEG and by counting, "
            "never by argument: the inventory the parent handed over is one "
            "coupling per class after the normalisation base is fixed, each "
            "coupling's strong limit is the extreme point on its own class, "
            "and each leg of the discriminator is asked how many couplings "
            "fall on each side.  A leg whose value never moves is "
            "FAMILY-INVARIANT and a leg whose value moves partitions the "
            "inventory exactly",
            ok,
            "%d couplings against %d extreme points; %d legs, %d of them "
            "partitioning; the area leg is %s"
            % (len(couplings), len(classes), len(legs),
               sum(1 for l in legs if l["partitions"]), area_leg["verdict"]))
    S["price_binding"] = {
        "every_integer_here_is_a_count": "COUNTING-ONLY-E-24",
        "the_inventory": pv["PV-ACT-COUPLINGS"],
        "the_extreme_points": len(classes),
        "the_normalisation_base": "THE-FIRST-CLASS-IN-THE-COIN-FAMILYS-OWN-"
                                  "ENUMERATION-ORDER",
        "couplings_counted": len(couplings),
        "legs": legs,
        "extreme_points_with_no_halving_mode": zeroC,
        "extreme_points_with_a_halving_mode": len(rows) - zeroC,
        "extreme_points_with_no_perimeter_mode": zeroB,
        "extreme_points_with_a_zero_winding_expectation": windzero,
        "extreme_points_where_the_creutz_ratio_is_undefined": undef,
        "the_reading": "THE-AREA-LEG-IS-FAMILY-INVARIANT-AND-THE-OTHER-"
                       "LEGS-PARTITION"}
    SEAL.take("THE PRICE BINDING", "price_binding", "G-THE-PRICE-BINDING",
              S["price_binding"])
    return legs


def hull(vals):
    """the range of an exact family of elements of Q(sqrt 2), decided by the
    real order and by integer comparison alone."""
    lo = hi = vals[0]
    for v in vals:
        if qs_less(v, lo):
            lo = v
        if qs_less(hi, v):
            hi = v
    return lo, hi


def measure_the_order_parameter_range(S, pv):
    """ACT's falsifier, put to the order-parameter analogue: is the winding
    expectation's range over the REACHABLE set narrower than its range over
    the parent's invariant simplex?  An observable is pinned by the action
    route exactly when it is, and this one is measured rather than assumed."""
    TR = S["_TR"]
    wv = TR[("STRAIGHT-WINDING-CYCLE", 1, 0)]
    own = list(wv)

    def averages(parts):
        out = []
        for c in parts:
            p = sum(wv[i][0] for i in c) / len(c)
            q = sum(wv[i][1] for i in c) / len(c)
            out.append((p, q))
        return out
    par = averages(S["_parent_orbits"])
    rea = averages(S["_classes"])
    lo0, hi0 = hull(own)
    lo1, hi1 = hull(par)
    lo2, hi2 = hull(rea)
    pinned = (lo2, hi2) != (lo1, hi1)
    if mut("MUT-ORDER-RANGE"):
        pinned = True
    LD.gate("G-THE-ORDER-PARAMETER-RANGE",
            "the parent's falsifier is put to the order-parameter analogue: "
            "the winding expectation's range is measured three times -- over "
            "its own values on the carrier, over the parent's invariant "
            "simplex where it is the hull of the orbit averages, and over "
            "the reachable set where it is the hull of the CLASS averages -- "
            "and an observable is pinned by the action route exactly when "
            "the third is narrower than the second",
            not pinned,
            "own range [%s, %s]; over the invariant simplex [%s, %s]; over "
            "the reachable set [%s, %s]; pinned %s"
            % (qs_str(lo0), qs_str(hi0), qs_str(lo1), qs_str(hi1),
               qs_str(lo2), qs_str(hi2), pinned))
    S["order_parameter_range"] = {
        "observable": "THE-WINDING-CYCLE-EXPECTATION",
        "range_of_the_observable_itself": [qs_str(lo0), qs_str(hi0)],
        "range_over_the_invariant_simplex": [qs_str(lo1), qs_str(hi1)],
        "range_over_the_reachable_set": [qs_str(lo2), qs_str(hi2)],
        "pinned_by_the_action_route": pinned,
        "the_reading": "THE-ORDER-PARAMETER-IS-NOT-PINNED-THE-LOCALITY-"
                       "DECLARATION-DOES-NOT-NARROW-ITS-RANGE"}
    SEAL.take("THE ORDER PARAMETER RANGE", "order_parameter_range",
              "G-THE-ORDER-PARAMETER-RANGE", S["order_parameter_range"])
    return pinned


# ===========================================================================
# SECTION 13.  THE SPECTRAL DOOR
# ===========================================================================
# Three legs.  The door itself is NAMED with its exact cost.  The finite form
# the window does reach is MEASURED.  And the holonomy's own spectrum is
# measured through its power-sum ladder, by Newton's identities in exact
# arithmetic, so that what carries the decay is identified rather than
# assumed.

FONE = (Fraction(1), Fraction(0), Fraction(0), Fraction(0))
FZ = (Fraction(0), Fraction(0), Fraction(0), Fraction(0))


def newton_char_poly(power_sums):
    """the elementary symmetric functions from the power sums, exactly, in
    the full field: the characteristic polynomial of a matrix from the traces
    of its powers.  imul and iadd are the same reduction modulo z^4+1 the
    integer census uses, evaluated here on exact rationals."""
    e = [FONE]
    for k in range(1, len(power_sums) + 1):
        acc = FZ
        for i in range(1, k + 1):
            term = imul(e[k - i], power_sums[i - 1])
            if i % 2 == 0:
                term = tuple(-x for x in term)
            acc = iadd(acc, term)
        e.append(tuple(x / k for x in acc))
    return e


def measure_the_spectral_door(S, pv):
    lat, coins, TR = S["_lat"], S["_coins"], S["_TR"]
    rows = S["_sweep"]
    n_slice_states = len(coins) ** lat.L
    door = {
        "the_object": "THE-TRANSFER-MATRIX-ON-A-TIME-SLICE-OF-THE-FULL-"
                      "CONFIGURATION-SPACE",
        "a_time_slice_is": "THE-%d-LINKS-OF-ONE-ROW" % lat.L,
        "states_per_slice": str(n_slice_states),
        "entries_in_the_matrix": str(n_slice_states ** 2),
        "in_the_window": False,
        "why": "OUT-OF-REACH-BY-COST-AT-THIS-ARENA-AND-NAMED-RATHER-THAN-"
               "APPROXIMATED"}
    ladder_gap = "1/2"
    spec = "{1,1,1/2}"
    universal = S["closed_form"]["closed_form_failures"] == 0
    TRF = S["_TRF"]
    ps = [TRF[("STRAIGHT-WINDING-CYCLE", k, 0)] for k in range(1, lat.L + 1)]
    selfinv, modone, checked = 0, 0, 0
    for i in range(len(coins)):
        e = newton_char_poly([ps[k][i] for k in range(lat.L)])
        det = e[lat.L]
        checked += 1
        if imul(det, iconj(det)) == FONE:
            modone += 1
        if all(e[lat.L - k] == imul(det, iconj(e[k]))
               for k in range(lat.L + 1)):
            selfinv += 1
    if mut("MUT-SPECTRAL-UNITARY"):
        modone -= 1
    ok = (modone == checked and selfinv == checked and universal)
    LD.gate("G-THE-SPECTRAL-DOOR",
            "the transfer object's own spectrum is measured rather than "
            "assumed: the winding cycle's power-sum ladder gives the "
            "characteristic polynomial of the winding holonomy by Newton's "
            "identities in exact arithmetic, its determinant is required to "
            "have modulus one and its coefficient sequence to be "
            "self-inversive -- the signature of a matrix whose spectrum lies "
            "on the unit circle, which is what settles WHERE the ladder's "
            "decay can and cannot live",
            ok,
            "%d holonomies; determinant of modulus one at %d; "
            "self-inversive at %d; the ladder spectrum %s with gap %s"
            % (checked, modone, selfinv, spec, ladder_gap))
    per_row = []
    for r in S["conditional_rows"]["rows"]:
        per_row.append({"row": r["row"], "mode_A": r["mode_A"],
                        "mode_B": r["mode_B"], "mode_C": r["mode_C"],
                        "the_gap": ladder_gap,
                        "the_spectrum": spec,
                        "closed_form_holds": r["closed_form_holds"]})
    S["spectral_door"] = {
        "the_door_named": door,
        "the_finite_form_measured": {
            "the_object": "THE-LADDERS-OWN-TRANSFER-SPECTRUM-READ-OFF-ITS-"
                          "EXACT-CLOSED-FORM",
            "the_spectrum": spec, "the_gap": ladder_gap,
            "eigenvalue_one_carries_a_two_block": True,
            "universal_on_the_carrier": universal,
            "rows": per_row},
        "the_holonomys_own_spectrum": {
            "holonomies_tested": checked,
            "determinant_of_modulus_one": modone,
            "self_inversive_characteristic_polynomial": selfinv,
            "the_reading": "THE-WINDING-HOLONOMY-IS-UNITARY-SO-ITS-SPECTRUM-"
                           "LIES-ON-THE-UNIT-CIRCLE-AND-CARRIES-NO-DECAYING-"
                           "DIRECTION"},
        "the_support_of_the_halving_mode": {
            "the_spectrum_is_the_closed_forms_ansatz_not_the_true_transfer_"
            "matrixs": True,
            "the_form_holds_at_coins": S["arena"]["coins"]
            - S["closed_form"]["closed_form_failures"],
            "coins": S["arena"]["coins"],
            "the_halving_mode_is_present_at_coins": S["closed_form"][
                "coefficient_profile"]["C"].get("1", 0),
            "the_halving_mode_is_absent_at_coins": S["closed_form"][
                "coefficient_profile"]["C"].get("0", 0),
            "the_halving_mode_is_present_at_extreme_points":
                S["price_binding"]["extreme_points_with_a_halving_mode"],
            "the_halving_mode_is_absent_at_extreme_points":
                S["price_binding"]["extreme_points_with_no_halving_mode"],
            "extreme_points": S["family_sweep"]["extreme_points"],
            "where_the_halving_coefficient_vanishes_the_realised_ladder_is":
                "A+B*P-WHOSE-MINIMAL-TRANSFER-OBJECT-HAS-NO-GAP-1/2-AT-ALL"},
        "SPC_inherits":
            "THE-GAP-%s-IS-THE-CLOSED-FORM-ANSATZS-AND-IS-THE-MASS-GAP-"
            "QUESTIONS-FINITE-FORM-AT-THIS-ARENA-ONLY-AT-THE-SUPPORT-OF-THE-"
            "HALVING-MODE-WHICH-IS-%d-OF-%d-COINS-AND-%d-OF-%d-EXTREME-POINTS"
            % (ladder_gap,
               S["closed_form"]["coefficient_profile"]["C"].get("1", 0),
               S["arena"]["coins"],
               S["price_binding"]["extreme_points_with_a_halving_mode"],
               S["family_sweep"]["extreme_points"])}
    SEAL.take("THE SPECTRAL DOOR", "spectral_door", "G-THE-SPECTRAL-DOOR",
              S["spectral_door"])
    return door


# ===========================================================================
# SECTION 13b.  THE ORIENTATION READING -- A DECLARED ALTERNATIVE STANDARD
# ===========================================================================
# The chart group contains orientation-REVERSING elements, and they are what
# make the conjugation-odd part of a loop trace unlawful: a reflection sends
# a loop to its reverse, whose holonomy is the inverse, whose trace is the
# conjugate.  Declaring the ORIENTED subgroup instead is a DECLARATION and
# never a derivation -- neither standard is the true one, and this unit says
# so -- but it is a declaration with an exact price, and both the price and
# what it buys are measured here.

def odd_qs(t):
    """THE CONJUGATION-ODD PART of a trace, written as the real pair (p, q)
    meaning i(p + q sqrt 2): (t - conj t)/2 is purely imaginary, and the
    purely imaginary part of Q(zeta_8) is i times its real subfield, since
    z^2 = i and z + z^3 = i sqrt 2."""
    return (t[2], (t[1] + t[3]) / 2)


def point_on_dir(g, d):
    sw, sx, sy = g
    x, y = EDIR[d]
    if sw:
        x, y = y, x
    x, y = sx * x, sy * y
    if (abs(x), abs(y)) == (1, 0):
        return 0, (1 if x > 0 else -1)
    return 1, (1 if y > 0 else -1)


def transported_link(lat, l, elem):
    """the image of a link under a chart element, with the domino's own
    orientation tracked: where the point part reverses the direction the
    image is read the other way round and the transported coin is the swap
    conjugate."""
    v, g = elem
    s, d = l
    d2, sign = point_on_dir(g, d)
    s2 = lat.addv(apply_point(g, s, lat.L), v)
    if sign > 0:
        return (s2, d2), False
    back = ((s2[0] - EDIR[d2][0]) % lat.L, (s2[1] - EDIR[d2][1]) % lat.L)
    return (back, d2), True


def swap_conjugate(m):
    """X U X: the coin read from the other end of its own domino."""
    a, b, c, d = m
    return (d, c, b, a)


def orientation_sign(g):
    sw, sx, sy = g
    return (-1 if sw else 1) * sx * sy


def link_stencil_orbits(lat, coins, cidx, elems):
    """the orbits of the link stencil's own acting group on the coin family:
    the gauge image together with whatever the chart stabiliser of that link
    induces on its coin."""
    link = (lat.sites[0], 0)
    stab = []
    for el in elems:
        img, swapped = transported_link(lat, link, el)
        if img == link:
            stab.append(swapped)
    maps = set()
    for swapped in set(stab):
        for k in range(phase_order()):
            perm = []
            for m in coins:
                mm = swap_conjugate(m) if swapped else m
                perm.append(cidx[gauge_twist(mm, k)])
            maps.add(tuple(perm))
    seen = [-1] * len(coins)
    orbits = 0
    for i in range(len(coins)):
        if seen[i] >= 0:
            continue
        frontier, comp = [i], {i}
        while frontier:
            j = frontier.pop()
            for perm in maps:
                k = perm[j]
                if k not in comp:
                    comp.add(k)
                    frontier.append(k)
        for j in comp:
            seen[j] = orbits
        orbits += 1
    return len(stab), len(maps), orbits


def measure_the_orientation_reading(S, pv):
    lat, coins, cidx = S["_lat"], S["_coins"], S["_cidx"]
    TR, TRF = S["_TR"], S["_TRF"]
    shapes = S["_shapes"]
    dec = []
    for extended, base in ((False, "ANCHORED"), (True, "EXTENSION")):
        elems = chart_elements(lat, extended)
        oriented = [e for e in elems if orientation_sign(e[1]) > 0]
        for name, es in ((base, elems), (base + "-ORIENTED", oriented)):
            stab, maps, orbits = link_stencil_orbits(lat, coins, cidx, es)
            dec.append({
                "reading": name,
                "declaration_status": "DECLARED-NEVER-DERIVED",
                "chart_group_order": len(es),
                "orientation_reversing_elements": len(elems) - len(oriented),
                "index_of_the_oriented_subgroup": len(elems) // len(oriented),
                "the_link_stencils_chart_stabilizer": stab,
                "the_acting_group_order": maps,
                "orbits": orbits, "coupling_count": orbits - 1,
                "stamp": "DECLARATION-RELATIVE-AT-THE-ORIENTATION-READING"})
    if mut("MUT-ORIENTATION-STAMP"):
        dec[1]["declaration_status"] = "DERIVED"
    if mut("MUT-ORIENTATION-UNSTAMPED"):
        dec[3]["stamp"] = "PLAIN"
    anch = [r for r in dec if r["reading"] == "ANCHORED"][0]
    ext = [r for r in dec if r["reading"] == "EXTENSION"][0]
    ok = (anch["coupling_count"] == pv["PV-ACT-COUPLINGS"]
          and ext["coupling_count"] == pv["PV-ACT-COUPLINGS-EXT"]
          and all(r["index_of_the_oriented_subgroup"] == 2 for r in dec)
          and all(r["declaration_status"] == "DECLARED-NEVER-DERIVED"
                  for r in dec)
          and all(r["stamp"] == "DECLARATION-RELATIVE-AT-THE-ORIENTATION-"
                  "READING" for r in dec))
    LD.gate("G-THE-ORIENTATION-READING-IS-PRICED",
            "the oriented chart subgroup is DECLARED as an alternative "
            "symmetry standard and never derived, and its price is measured "
            "rather than argued: the index of the oriented subgroup in the "
            "chart group is the convention purchased, and the form census at "
            "the link grain is re-run at all four readings so that what the "
            "smaller covariance group costs -- or fails to cost -- in "
            "couplings is a number.  Every row carries the declaration stamp",
            ok,
            "; ".join("%s: chart %d, stabiliser %d, acting %d, orbits %d, "
                      "couplings %d, index %d"
                      % (r["reading"], r["chart_group_order"],
                         r["the_link_stencils_chart_stabilizer"],
                         r["the_acting_group_order"], r["orbits"],
                         r["coupling_count"],
                         r["index_of_the_oriented_subgroup"]) for r in dec))
    split_bad, oddloops, oddshapes = 0, 0, []
    for key in shapes:
        nz = 0
        for i in range(len(coins)):
            t = TRF[key][i]
            sy = sym_qs(t)
            od = odd_qs(t)
            recon = iadd((sy[0], sy[1], Fraction(0), -sy[1]),
                         imul((Fraction(0), Fraction(0), Fraction(1),
                               Fraction(0)),
                              (od[0], od[1], Fraction(0), -od[1])))
            if recon != t:
                split_bad += 1
            if not qs_is_zero(od):
                nz += 1
        if nz:
            oddshapes.append({"shape": "%s-%d-%d" % key,
                              "coins_with_a_non_zero_odd_part": nz})
        oddloops += nz
    if mut("MUT-ODD-SPLIT"):
        split_bad = 1
    LD.gate("G-THE-CONJUGATION-SPLIT-IS-EXACT",
            "every loop trace is split exactly into its conjugation-"
            "symmetric and conjugation-odd parts and the two are required to "
            "reconstruct it in the full field at every shape and every coin, "
            "so the odd part this reading makes lawful is the parent's own "
            "trace minus the parent's own admissible object and not a new "
            "quantity",
            split_bad == 0,
            "%d shape-by-coin traces split, %d reconstruction failures, %d "
            "carrying a non-zero odd part at %d of %d shapes"
            % (len(shapes) * len(coins), split_bad, oddloops,
               len(oddshapes), len(shapes)))
    rev_odd_bad, rev_checked = 0, 0
    by_shape = {}
    for f in S["_fam"]:
        by_shape.setdefault((f["kind"], f["a"], f["b"]), []).append(f)
    for key in shapes:
        cyc = sorted(by_shape[key], key=lambda z: z["base"])[0]["cycle"]
        st = steps_of(lat, tuple(reversed(cyc)))
        for i, m in enumerate(coins):
            t, _n = holonomy_trace(lat, st, m)
            rev_checked += 1
            o1 = odd_qs(t)
            o0 = odd_qs(TRF[key][i])
            if o1 != (-o0[0], -o0[1]):
                rev_odd_bad += 1
    if mut("MUT-ORIENTATION-ODDNESS"):
        rev_odd_bad = 1
    LD.gate("G-THE-ODD-PART-IS-ORIENTATION-ODD",
            "the odd part is measured to change sign under the reversal a "
            "reflection performs, at every shape and every coin -- which is "
            "exactly why it is unlawful at the full chart standard and "
            "lawful at the oriented one, and it makes the declaration's "
            "content a measurement rather than a definition",
            rev_odd_bad == 0,
            "%d reversed comparisons, %d that did not negate"
            % (rev_checked, rev_odd_bad))
    rowvals = []
    for r in S["conditional_rows"]["rows"]:
        mu = S["_mus"][r["row"]]
        sup = support_pairs(mu)
        vals = {}
        for key in shapes:
            p = sum(w * odd_qs(TRF[key][i])[0] for i, w in sup)
            q = sum(w * odd_qs(TRF[key][i])[1] for i, w in sup)
            if not (p == 0 and q == 0):
                vals["%s-%d-%d" % key] = "i*(%s)" % qs_str((p, q))
        rowvals.append({"row": r["row"],
                        "non_zero_odd_observables": len(vals),
                        "values": vals,
                        "stamp": "DECLARATION-RELATIVE-AT-THE-ORIENTATION-"
                                 "READING"})
    ptvals = []
    for k, c in enumerate(S["_classes"]):
        nz = 0
        for key in shapes:
            p = sum(odd_qs(TRF[key][i])[0] for i in c)
            q = sum(odd_qs(TRF[key][i])[1] for i in c)
            if not (p == 0 and q == 0):
                nz += 1
        ptvals.append(nz)
    pts_with = sum(1 for x in ptvals if x)
    if mut("MUT-ODD-UNSTAMPED"):
        rowvals[0]["stamp"] = "PLAIN"
    ok2 = all(r["stamp"] == "DECLARATION-RELATIVE-AT-THE-ORIENTATION-READING"
              for r in rowvals)
    LD.gate("G-THE-ODD-OBSERVABLES-CARRY-THEIR-DECLARATION",
            "what the oriented declaration buys is published as values, and "
            "every one of them carries the stamp DECLARATION-RELATIVE-AT-"
            "THE-ORIENTATION-READING on its own row: an odd-part value "
            "rendered without its declaration stops the delivery run, "
            "because outside that declaration it is not an observable of "
            "this arena at all",
            ok2,
            "%d declared rows carry odd observables at %s of the family's "
            "shapes; %d of %d extreme points carry at least one"
            % (len(rowvals),
               [r["non_zero_odd_observables"] for r in rowvals],
               pts_with, len(ptvals)))
    S["orientation_reading"] = {
        "the_declaration": "THE-ORIENTED-CHART-SUBGROUP-AS-AN-ALTERNATIVE-"
                           "SYMMETRY-STANDARD",
        "status": "DECLARED-NEVER-DERIVED-NEITHER-STANDARD-IS-CLAIMED-TRUE",
        "stamp": "DECLARATION-RELATIVE-AT-THE-ORIENTATION-READING",
        "every_integer_here_is_a_count": "COUNTING-ONLY-E-24-NO-MEASURE-OVER-"
                                         "THE-FAMILY-IS-DECLARED",
        "readings": dec,
        "the_price_in_convention": "ONE-BINARY-CHOICE-THE-INDEX-IS-2-AT-"
                                   "BOTH-READINGS",
        "the_price_in_couplings": "UNCHANGED-AT-EVERY-READING",
        "the_conjugation_split": {
            "traces_split": len(shapes) * len(coins),
            "reconstruction_failures": split_bad,
            "shape_by_coin_traces_with_a_non_zero_odd_part": oddloops,
            "shapes_carrying_an_odd_part": len(oddshapes),
            "shapes": oddshapes},
        "the_odd_part_is_orientation_odd": rev_odd_bad == 0,
        "reversed_comparisons": rev_checked,
        "what_becomes_lawful": rowvals,
        "extreme_points_carrying_an_odd_observable": pts_with,
        "extreme_points": len(ptvals)}
    SEAL.take("THE ORIENTATION READING", "orientation_reading",
              "G-THE-ODD-OBSERVABLES-CARRY-THEIR-DECLARATION",
              S["orientation_reading"])
    return dec


# ===========================================================================
# SECTION 14.  THE L-BOUNDARY, RUN
# ===========================================================================
# The pin requires the boundary STATED; this section makes it a measurement.
# A second declared lattice size -- the smallest at which the merging index
# is one -- is built and the loop legs are re-run there, so which findings
# survive the boundary and which do not is measured and not projected.

def measure_the_boundary_lattice(S, pv):
    coins, cidx = S["_coins"], S["_cidx"]
    L2 = 8
    lat2 = Lattice(L2)
    ext2 = list(range(1, L2))
    shapes2 = [(a, b) for a in ext2 for b in ext2]
    simple = 0
    for a in range(1, L2 + 1):
        for b in range(1, L2 + 1):
            cyc, closes = rect_cycle(lat2, (0, 0), a, b)
            st = steps_of(lat2, cyc)
            if closes and len({l for (l, _o) in st}) == len(st) \
                    and len(set(cyc)) == len(st):
                simple += 1
    per = {}
    for (a, b) in shapes2:
        per.setdefault(a + b, []).append((a, b))
    ss = sorted(per)
    rep = {s: sorted(per[s])[0] for s in ss}
    TR2 = {}
    for s in ss:
        a, b = rep[s]
        cyc, _ = rect_cycle(lat2, (0, 0), a, b)
        st = steps_of(lat2, cyc)
        TR2[s] = [sym_qs(holonomy_trace(lat2, st, m)[0]) for m in coins]
    comps = area_comparisons(shapes2)
    viol, checked = 0, 0
    seen_shapes = {}
    for (a, b) in shapes2:
        cyc, _ = rect_cycle(lat2, (0, 0), a, b)
        st = steps_of(lat2, cyc)
        seen_shapes[(a, b)] = [sym_qs(holonomy_trace(lat2, st, m)[0])
                               for m in coins]
    for (x, y) in comps:
        for i in range(len(coins)):
            checked += 1
            if seen_shapes[x][i] != seen_shapes[y][i]:
                viol += 1
    if mut("MUT-BOUNDARY-AREA"):
        viol = 1
    bad = 0
    for i in range(len(coins)):
        A, B, C = mode_fit(TR2[ss[0]][i], TR2[ss[1]][i], TR2[ss[2]][i])
        for s in ss[3:]:
            if mode_value(A, B, C, s) != TR2[s][i]:
                bad += 1
    same = 0
    for i in range(len(coins)):
        A, B, C = mode_fit(TR2[ss[0]][i], TR2[ss[1]][i], TR2[ss[2]][i])
        if (A, B, C) == S["_modes"][i]:
            same += 1
    res2 = realisable_twists(L2)
    parent2 = twist_orbits(coins, cidx, res2)
    classes2 = twist_orbits(coins, cidx, range(phase_order()))
    merged2 = len(parent2) - len(classes2)
    ok = (viol == 0 and bad == 0 and same == len(coins)
          and merged2 == 0 and len(comps) > len(
              S["discriminator"]["the_comparisons"]))
    LD.gate("G-THE-BOUNDARY-LATTICE-RUN",
            "the L-boundary is RUN and not projected: at the smallest "
            "lattice size where the merging index is one, the ladder is "
            "still a function of the perimeter alone across every "
            "area-discriminating comparison, the closed form still holds "
            "over a strictly longer ladder with the SAME coefficients coin "
            "by coin, and the class structure loses its merges entirely -- "
            "so the two halves of this unit's findings are measured to "
            "carry different lattice scopes",
            ok,
            "L=%d: %d simple shapes, %d area-discriminating comparisons "
            "against %d here, %d comparison-by-coin checks with %d "
            "disagreements, closed-form failures %d, identical coefficients "
            "at %d of %d coins, %d parent orbits and %d classes with %d "
            "merges"
            % (L2, simple, len(comps),
               len(S["discriminator"]["the_comparisons"]), checked, viol,
               bad, same, len(coins), len(parent2), len(classes2), merged2))
    S["boundary_lattice"] = {
        "L": L2,
        "why_this_size": "THE-SMALLEST-L-DIVISIBLE-BY-EIGHT-WHERE-THE-"
                         "MERGING-INDEX-IS-ONE",
        "simple_rectangle_shapes": simple,
        "ladder_perimeters": ss,
        "area_discriminating_comparisons": len(comps),
        "comparison_by_coin_checks": checked,
        "area_disagreements": viol,
        "closed_form_failures": bad,
        "coins_with_identical_coefficients": same,
        "parent_orbits": len(parent2), "classes": len(classes2),
        "orbit_pairs_merged": merged2,
        "the_comparison_table": [
            {"quantity": "simple rectangle shapes",
             "at_the_declared_L": S["loop_family"]["simple_rectangle_shapes"],
             "at_the_boundary_L": simple},
            {"quantity": "area-discriminating comparisons",
             "at_the_declared_L":
                 S["discriminator"]["area_discriminating_comparisons"],
             "at_the_boundary_L": len(comps)},
            {"quantity": "the longest ladder perimeter",
             "at_the_declared_L": max(S["closed_form"]["perimeters"]),
             "at_the_boundary_L": max(ss)},
            {"quantity": "the merging index",
             "at_the_declared_L": [r["the_merging_index"] for r in
                                   S["discriminator"]["the_L_boundary"]
                                   if r["L"] == S["arena"]["L"]][0],
             "at_the_boundary_L": [r["the_merging_index"] for r in
                                   S["discriminator"]["the_L_boundary"]
                                   if r["L"] == L2][0]},
            {"quantity": "the parents orbits",
             "at_the_declared_L": S["classes"]["parent_orbits"],
             "at_the_boundary_L": len(parent2)},
            {"quantity": "the induced classes",
             "at_the_declared_L": S["classes"]["classes"],
             "at_the_boundary_L": len(classes2)},
            {"quantity": "orbit pairs merged",
             "at_the_declared_L": S["classes"]["orbit_pairs_merged"],
             "at_the_boundary_L": merged2}],
        "what_survives": "AREA-BLINDNESS-AND-THE-CLOSED-FORM-AND-THE-GAP",
        "what_does_not": "THE-CLASS-MERGING-AND-EVERY-COUNT-BUILT-ON-IT"}
    SEAL.take("THE BOUNDARY LATTICE", "boundary_lattice",
              "G-THE-BOUNDARY-LATTICE-RUN", S["boundary_lattice"])
    return S["boundary_lattice"]


# ===========================================================================
# SECTION 15.  THE HEAD LAW, AND ITS INDEPENDENT SECOND
# ===========================================================================

PREREGISTERED = ["POT-CONFINES-AT", "POT-DECONFINES-AT",
                 "POT-SPLIT-BY-WEIGHT", "POT-DISCRIMINATOR-DEGENERATE-AT",
                 "POT-BLOCKED-AT"]


def head_law(row_words, sweep_words, blocked):
    """the selector, from the leg verdicts alone.  row_words and sweep_words
    are lists of (ladder_word, winding_word) pairs."""
    if blocked:
        return "POT-BLOCKED-AT"
    allw = list(row_words) + list(sweep_words)
    if not allw:
        return "POT-BLOCKED-AT"
    if any(a == "BLOCKED-AT-THE-LADDER" for a, _b in allw):
        return "POT-BLOCKED-AT"
    if len(set(allw)) > 1:
        return "POT-SPLIT-BY-WEIGHT"
    ladder = allw[0][0]
    if ladder == "CONFINES":
        return "POT-CONFINES-AT"
    if ladder == "DECONFINES":
        return "POT-DECONFINES-AT"
    return "POT-DISCRIMINATOR-DEGENERATE-AT"


def second_head_law(payload):
    """an INDEPENDENT second law over the same question, reading only the
    serialized receipt and only its TALLIES -- never the row lists the first
    law reads, and never the first law's own output."""
    if any(not g["passed"] for g in payload["gates"]):
        return "POT-BLOCKED-AT"
    t1 = payload["conditional_rows"]["ladder_word_tally"]
    t2 = payload["family_sweep"]["ladder_word_tally"]
    w1 = payload["conditional_rows"]["winding_word_tally"]
    w2 = payload["family_sweep"]["winding_word_tally"]
    if "BLOCKED-AT-THE-LADDER" in t1 or "BLOCKED-AT-THE-LADDER" in t2:
        return "POT-BLOCKED-AT"
    lad = set(t1) | set(t2)
    win = set(w1) | set(w2)
    if len(lad) > 1 or len(win) > 1:
        return "POT-SPLIT-BY-WEIGHT"
    only = list(lad)[0]
    if only == "CONFINES":
        return "POT-CONFINES-AT"
    if only == "DECONFINES":
        return "POT-DECONFINES-AT"
    return "POT-DISCRIMINATOR-DEGENERATE-AT"


def measure_the_control_arms(S, pv):
    """THE SELECTOR MADE REAL: declared synthetic ladder tables are driven
    through the SAME classify() and the SAME head_law() the delivered rows go
    through -- no field of any delivered row is overwritten and no outcome is
    asserted -- and every pre-registered word is required to come back out."""
    shapes = S["_shapes_ladder"]
    half = Fraction(1, 2)
    one, zero = (Fraction(1), Fraction(0)), (Fraction(0), Fraction(0))

    def area_table(r):
        return {(a, b): (r ** (a * b), Fraction(0)) for (a, b) in shapes}

    def perim_table(r):
        return {(a, b): (r ** (a + b), Fraction(0)) for (a, b) in shapes}

    def holed_table(r):
        t = perim_table(r)
        t[sorted(shapes)[1]] = zero
        return t

    def short_table(r):
        t = perim_table(r)
        del t[sorted(shapes)[-1]]
        return t

    arms = [
        ("SYN-AREA-LAW", "A-LAW-GEOMETRIC-IN-THE-AREA",
         area_table(half), one, "CONFINES", "POT-CONFINES-AT"),
        ("SYN-PERIMETER-LAW", "A-LAW-GEOMETRIC-IN-THE-PERIMETER",
         perim_table(half), one, "DECONFINES", "POT-DECONFINES-AT"),
        ("SYN-ZERO-DENOMINATOR", "A-LADDER-WITH-A-VANISHING-RUNG",
         holed_table(half), one, "DISCRIMINATOR-DEGENERATE",
         "POT-DISCRIMINATOR-DEGENERATE-AT"),
        ("SYN-MISSING-SHAPE", "A-LADDER-THE-FAMILY-DOES-NOT-COVER",
         short_table(half), one, "BLOCKED-AT-THE-LADDER", "POT-BLOCKED-AT"),
    ]
    rows, reached = [], {}
    for name, what, tab, wind, expect_leg, expect_head in arms:
        v = classify(tab, wind, shapes)
        h = head_law([(v["ladder_word"], v["winding_word"])], [], False)
        rows.append({"arm": name, "the_synthetic_law": what,
                     "ladder_word": v["ladder_word"],
                     "expected_ladder_word": expect_leg,
                     "head_word": h, "expected_head_word": expect_head,
                     "creutz": v["creutz"],
                     "area_seen": v["area_seen"],
                     "agrees": v["ladder_word"] == expect_leg
                     and h == expect_head})
        reached[expect_head] = True
    va = classify(area_table(half), one, shapes)
    vp = classify(perim_table(half), one, shapes)
    hs = head_law([(va["ladder_word"], va["winding_word"]),
                   (vp["ladder_word"], vp["winding_word"])], [], False)
    rows.append({"arm": "SYN-TWO-ROWS-THAT-DISAGREE",
                 "the_synthetic_law": "ONE-AREA-ROW-BESIDE-ONE-PERIMETER-ROW",
                 "ladder_word": "%s|%s" % (va["ladder_word"],
                                           vp["ladder_word"]),
                 "expected_ladder_word": "CONFINES|DECONFINES",
                 "head_word": hs, "expected_head_word": "POT-SPLIT-BY-WEIGHT",
                 "creutz": {}, "area_seen": None,
                 "agrees": hs == "POT-SPLIT-BY-WEIGHT"})
    reached["POT-SPLIT-BY-WEIGHT"] = True
    if mut("MUT-CONTROL-ARM"):
        rows[0]["agrees"] = True
        rows[0]["head_word"] = "POT-DECONFINES-AT"
    ok = (all(r["agrees"] for r in rows)
          and sorted(reached) == sorted(PREREGISTERED)
          and len({r["head_word"] for r in rows}) == len(PREREGISTERED))
    LD.gate("G-EVERY-PREREGISTERED-WORD-IS-EMITTABLE",
            "the head law is measured multi-way rather than declared so: "
            "each pre-registered word is produced by driving a DECLARED "
            "synthetic ladder -- a law geometric in the area, a law "
            "geometric in the perimeter, a ladder with a vanishing rung, a "
            "ladder the family does not cover, and two rows that disagree -- "
            "through the same discriminator and the same head law the "
            "delivered rows go through, with no delivered field overwritten "
            "and no row forged",
            ok,
            "%d control arms, %d agreeing; %d distinct head words against "
            "%d pre-registered" % (len(rows), sum(1 for r in rows
                                                  if r["agrees"]),
                                   len({r["head_word"] for r in rows}),
                                   len(PREREGISTERED)))
    S["control_arms"] = {
        "the_pattern": "SYNTHETIC-LADDERS-THROUGH-THE-REAL-DISCRIMINATOR-"
                       "AND-THE-REAL-HEAD-LAW",
        "preregistered_words": PREREGISTERED,
        "arms": rows,
        "every_word_reached": sorted(reached)}
    SEAL.take("THE CONTROL ARMS", "control_arms",
              "G-EVERY-PREREGISTERED-WORD-IS-EMITTABLE", S["control_arms"])
    return rows


def measure_the_verdict(S, pv):
    rows = S["conditional_rows"]["rows"]
    sweep = S["_sweep"]
    rw = [(r["ladder_word"], r["winding_word"]) for r in rows]
    sw = [(r["ladder_word"], r["winding_word"]) for r in sweep]
    if mut("MUT-HEAD"):
        rw = [("DECONFINES", "WINDING-ORDER-NONZERO")]
        sw = []
    word = head_law(rw, sw, False)
    if mut("MUT-HEAD-WORD"):
        word = "POT-A-WORD-THE-PIN-NEVER-PREREGISTERED"
    t1 = S["conditional_rows"]["ladder_word_tally"]
    t2 = S["family_sweep"]["ladder_word_tally"]
    ok = word in PREREGISTERED
    LD.gate("G-THE-HEAD-IS-DERIVED",
            "the head word is DERIVED by the selector from the leg verdicts "
            "of every declared row and every extreme point, and it is "
            "required to be one of the words the pin pre-registered -- so a "
            "head that is not the measurement's own is not utterable here",
            ok,
            "the head law returns %s from %d declared rows and %d extreme "
            "points; row tally %s; sweep tally %s"
            % (word, len(rows), len(sweep), t1, t2))
    S["_head_word"] = word
    SEAL.take("THE HEAD WORD", "verdict_head", "G-THE-HEAD-IS-DERIVED", word)
    return word


# ===========================================================================
# SECTION 16.  THE VERDICT STRING, AND ITS DE-TWINNED RECONSTRUCTION
# ===========================================================================

def render_verdict(S):
    """the builder's rendering.  Every value is a measured receipt field."""
    lf, dc = S["loop_family"], S["discriminator"]
    cr, fs = S["conditional_rows"], S["family_sweep"]
    pb, sd = S["price_binding"], S["spectral_door"]
    bl, cf = S["boundary_lattice"], S["closed_form"]
    ar, cl = S["arena"], S["classes"]
    ci = S["constant_ladder_identity"]
    wz = fs["winding_word_tally"].get("WINDING-ORDER-ZERO", 0)
    wn = fs["winding_word_tally"].get("WINDING-ORDER-NONZERO", 0)
    rz = cr["winding_word_tally"].get("WINDING-ORDER-ZERO", 0)
    rn = cr["winding_word_tally"].get("WINDING-ORDER-NONZERO", 0)
    nrows = len(cr["rows"])
    npts = fs["extreme_points"]
    nsl = S["family_slices"]["slices"]
    head = ("%s-THE-WINDING-LEG-SPLITS-%d-NONZERO-AND-%d-ZERO-OF-%d-EXTREME-"
            "POINTS-AND-%d-OF-%d-DECLARED-ROWS-WHILE-THE-AREA-LEG-IS-"
            "FAMILY-INVARIANT-AREA-BLIND-AT-%d-OF-%d-MEASURED-ROWS"
            % (S["_head_word"], wn, wz, npts, rn, nrows,
               nrows + npts + nsl, nrows + npts + nsl))
    seg = []
    seg.append(head)
    seg.append("LOOP-FAMILY=%d-PLACEMENTS-%d-DISTINCT-LOOPS-%d-CONTRACTIBLE-"
               "AND-%d-WINDING;RECTANGLE-EXTENTS=%s-MEASURED-SIMPLE-AT-%d-OF-"
               "%d-SWEPT-SIZES;ORBITS-UNDER-THE-ANCHORED-CHART-GROUP-OF-"
               "ORDER-%d=%d-CLOSED-%s;THE-WINDOW=%s"
               % (lf["placements"], lf["distinct_loops"], lf["contractible"],
                  lf["winding"],
                  "-".join(str(x) for x in lf["simple_rectangle_extents"]),
                  lf["simple_rectangle_shapes"], lf["rectangle_sizes_swept"],
                  lf["orbit_rows"][0]["chart_order"],
                  lf["orbit_rows"][0]["orbits"],
                  str(lf["orbit_rows"][0]["closed_under_the_acting_group"]
                      ).upper(), lf["the_window"]))
    seg.append("DISCRIMINATOR=WELL-DEFINED-AT-L-%d-WITH-%d-AREA-"
               "DISCRIMINATING-COMPARISONS-AND-%d-CREUTZ-RUNGS;LEG-AREA="
               "BLIND-EVERYWHERE;LEG-CREUTZ=DEFINED-AT-%d-OF-%d-EXTREME-"
               "POINTS-AND-EQUAL-TO-ONE-AT-%d;LEG-WINDING=THE-ORDER-"
               "PARAMETER-ANALOGUE"
               % (ar["L"], dc["area_discriminating_comparisons"],
                  dc["creutz_rungs"],
                  npts - pb["extreme_points_where_the_creutz_ratio_is_"
                            "undefined"], npts,
                  fs["ladder_word_tally"].get("DECONFINES", 0)))
    seg.append("(a)CONDITIONAL=%d-ROWS-ALL-STAMPED-%s;PLAQUETTE-"
               "EXPECTATIONS=%s;WINDING=%d-ZERO-AND-%d-NONZERO;THE-CONTROL-"
               "CARRIES-%s-AND-IS-NEVER-SPENT-AS-DERIVED"
               % (nrows, cr["stamp"],
                  ",".join("%s@%s" % (r["plaquette_expectation"], r["row"])
                           for r in cr["rows"]), rz, rn,
                  cr["the_control_stamp"]))
    seg.append("(b)FAMILY-SWEPT=%d-EXTREME-POINTS-%d-VERTICES-AND-%d-EDGE-"
               "MIDPOINTS-ALL-RUN;FAMILY-INVARIANT=%s;COUPLING-DEPENDENT=%s;"
               "SLICES=%d-EXACT-ONE-PARAMETER-ROWS-AGREE-AT-THE-AREA-LEG"
               % (npts, fs["vertices"], fs["edge_midpoints"],
                  "+".join(fs["family_invariant_observables"]),
                  "+".join(fs["coupling_dependent_observables"]), nsl))
    seg.append("PRICE=THE-INVENTORY-IS-%d-COUPLINGS-AND-THE-AREA-LEG-"
               "PARTITIONS-NONE-OF-THEM;THE-WINDING-LEG-PARTITIONS-%d-"
               "AGAINST-%d-OF-%d;THE-HALVING-MODE-IS-ABSENT-AT-%d-OF-%d;THE-"
               "PERIMETER-MODE-IS-ABSENT-AT-%d-OF-%d;THE-CREUTZ-RATIO-IS-"
               "UNDEFINED-AT-%d-OF-%d;THE-CREUTZ-RATIO-IS-ONE-AT-%d-WHICH-"
               "ARE-EXACTLY-THE-%d-LADDERS-CONSTANT-IN-THE-PERIMETER"
               % (pb["the_inventory"], wn, wz, npts,
                  pb["extreme_points_with_no_halving_mode"], npts,
                  pb["extreme_points_with_no_perimeter_mode"], npts,
                  pb["extreme_points_where_the_creutz_ratio_is_undefined"],
                  npts, ci["the_creutz_ratio_is_one_at"],
                  ci["the_ladder_is_constant_in_the_perimeter_at"]))
    seg.append("SPECTRAL-DOOR=THE-TRANSFER-MATRIX-ON-A-TIME-SLICE-IS-NAMED-"
               "NOT-RUN-AT-%s-STATES-PER-SLICE;THE-FINITE-FORM-IS-MEASURED-"
               "AT-%d-OF-%d-COINS=W=A+B*P+C*2^-P;THE-ANSATZS-SPECTRUM-IS-%s-"
               "WITH-GAP-%s-AND-ITS-HALVING-MODE-IS-PRESENT-AT-%d-OF-%d-"
               "COINS-AND-%d-OF-%d-EXTREME-POINTS;THE-WINDING-HOLONOMY-IS-"
               "UNITARY-AT-%d-OF-%d-SO-ITS-SPECTRUM-CARRIES-NO-DECAY;SPC-"
               "INHERITS-THE-GAP-AT-THAT-SUPPORT"
               % (sd["the_door_named"]["states_per_slice"],
                  ar["coins"] - cf["closed_form_failures"], ar["coins"],
                  cf["the_transfer_spectrum"], cf["the_gap"],
                  cf["coefficient_profile"]["C"].get("1", 0), ar["coins"],
                  pb["extreme_points_with_a_halving_mode"], npts,
                  sd["the_holonomys_own_spectrum"][
                      "self_inversive_characteristic_polynomial"],
                  sd["the_holonomys_own_spectrum"]["holonomies_tested"]))
    orr = S["orientation_reading"]
    seg.append("ORIENTATION=%s-%s;THE-ORIENTED-SUBGROUP-HAS-INDEX-%d-AT-"
               "BOTH-READINGS;COUPLINGS=%d-AT-ANCHORED-AND-%d-AT-ANCHORED-"
               "ORIENTED-AND-%d-AT-THE-EXTENSION-AND-%d-AT-EXTENSION-"
               "ORIENTED-SO-THE-DECLARATION-BUYS-OBSERVABLES-AND-COSTS-NO-"
               "COUPLING;THE-ODD-PART-IS-LAWFUL-ONLY-THERE-AND-IS-NON-ZERO-"
               "AT-%d-OF-%d-SHAPE-BY-COIN-TRACES-AT-%d-OF-%d-SHAPES-AND-AT-"
               "%d-OF-%d-EXTREME-POINTS"
               % (orr["status"], orr["stamp"],
                  orr["readings"][0]["index_of_the_oriented_subgroup"],
                  orr["readings"][0]["coupling_count"],
                  orr["readings"][1]["coupling_count"],
                  orr["readings"][2]["coupling_count"],
                  orr["readings"][3]["coupling_count"],
                  orr["the_conjugation_split"][
                      "shape_by_coin_traces_with_a_non_zero_odd_part"],
                  orr["the_conjugation_split"]["traces_split"],
                  orr["the_conjugation_split"]["shapes_carrying_an_odd_part"],
                  len(S["_shapes"]),
                  orr["extreme_points_carrying_an_odd_observable"],
                  orr["extreme_points"]))
    seg.append("L-BOUNDARY=THE-MERGING-INDEX-IS-8/GCD(L,8)-WHICH-IS-%d-HERE-"
               "AND-%d-AT-L-%d;AREA-BLINDNESS-AND-THE-CLOSED-FORM-AND-THE-"
               "GAP-SURVIVE-THE-BOUNDARY-%d-DISAGREEMENTS-OVER-%d-CHECKS-"
               "AND-%d-OF-%d-COINS-CARRY-IDENTICAL-COEFFICIENTS;THE-CLASS-"
               "MERGING-DOES-NOT-%d-MERGES-AT-L-%d-AGAINST-%d-HERE"
               % ([r["the_merging_index"] for r in dc["the_L_boundary"]
                   if r["L"] == ar["L"]][0],
                  [r["the_merging_index"] for r in dc["the_L_boundary"]
                   if r["L"] == bl["L"]][0], bl["L"],
                  bl["area_disagreements"], bl["comparison_by_coin_checks"],
                  bl["coins_with_identical_coefficients"], ar["coins"],
                  bl["orbit_pairs_merged"], bl["L"], cl["orbit_pairs_merged"]))
    seg.append("SCOPE=D=2;L=%d;BOUNDARY-L=%d;FIELD=%s;COINS=%d;LINKS=%d;"
               "PLAQUETTES=%d;CARRIER=%s;FULL-CONFIGURATION-SPACE=%s-NOT-A-"
               "CARRIER-HERE;WEIGHTS=POSITIVE-EXACT-RATIONALS-NO-LOGS-NO-"
               "FLOATS;THE-POTENTIAL-IS-NOMINAL-AND-CARRIED-"
               "MULTIPLICATIVELY;CONFINEMENT-VOCABULARY-IS-LICENSED-FOR-"
               "THIS-UNIT-ONLY-AND-ONLY-IN-MEASURED-SENTENCES;NO-CONTINUUM-"
               "CLAIM;NO-SI-NUMBERS;NOT-QCD"
               % (ar["L"], bl["L"], ar["field"], ar["coins"], ar["links"],
                  ar["plaquettes"], ar["carrier"],
                  ar["configuration_space"]))
    return " -- ".join(seg)


def rerender_verdict(payload):
    """THE DE-TWINNED COMPARATOR.  It reads ONLY the receipt payload -- the
    same object that is about to be serialized, not the builder's working
    state -- derives the head by the second head law over the tallies rather
    than the rows, re-renders every segment from the measured tables, and
    shares no format string and no helper with the builder above.  What it
    therefore guards is the RENDERING and the staleness of the string, not
    the measurement underneath it, and it is said here to do exactly that."""
    A = payload["arena"]
    LFm = payload["loop_family"]
    D = payload["discriminator"]
    CR = payload["conditional_rows"]
    FS = payload["family_sweep"]
    PB = payload["price_binding"]
    SD = payload["spectral_door"]
    BL = payload["boundary_lattice"]
    CF = payload["closed_form"]
    CL = payload["classes"]
    SL = payload["family_slices"]
    hw = second_head_law(payload)
    wn = FS["winding_word_tally"].get("WINDING-ORDER-NONZERO", 0)
    wz = FS["winding_word_tally"].get("WINDING-ORDER-ZERO", 0)
    rn = CR["winding_word_tally"].get("WINDING-ORDER-NONZERO", 0)
    rz = CR["winding_word_tally"].get("WINDING-ORDER-ZERO", 0)
    nr = len(CR["rows"])
    np_ = FS["extreme_points"]
    ns = SL["slices"]
    tot = nr + np_ + ns
    out = []
    out.append("".join([hw, "-THE-WINDING-LEG-SPLITS-", str(wn),
                        "-NONZERO-AND-", str(wz), "-ZERO-OF-", str(np_),
                        "-EXTREME-POINTS-AND-", str(rn), "-OF-", str(nr),
                        "-DECLARED-ROWS-WHILE-THE-AREA-LEG-IS-FAMILY-"
                        "INVARIANT-AREA-BLIND-AT-", str(tot), "-OF-",
                        str(tot), "-MEASURED-ROWS"]))
    o0 = LFm["orbit_rows"][0]
    out.append("".join([
        "LOOP-FAMILY=", str(LFm["placements"]), "-PLACEMENTS-",
        str(LFm["distinct_loops"]), "-DISTINCT-LOOPS-",
        str(LFm["contractible"]), "-CONTRACTIBLE-AND-", str(LFm["winding"]),
        "-WINDING;RECTANGLE-EXTENTS=",
        "-".join([str(x) for x in LFm["simple_rectangle_extents"]]),
        "-MEASURED-SIMPLE-AT-", str(LFm["simple_rectangle_shapes"]), "-OF-",
        str(LFm["rectangle_sizes_swept"]),
        "-SWEPT-SIZES;ORBITS-UNDER-THE-ANCHORED-CHART-GROUP-OF-ORDER-",
        str(o0["chart_order"]), "=", str(o0["orbits"]), "-CLOSED-",
        str(o0["closed_under_the_acting_group"]).upper(), ";THE-WINDOW=",
        LFm["the_window"]]))
    undef = PB["extreme_points_where_the_creutz_ratio_is_undefined"]
    out.append("".join([
        "DISCRIMINATOR=WELL-DEFINED-AT-L-", str(A["L"]), "-WITH-",
        str(D["area_discriminating_comparisons"]),
        "-AREA-DISCRIMINATING-COMPARISONS-AND-", str(D["creutz_rungs"]),
        "-CREUTZ-RUNGS;LEG-AREA=BLIND-EVERYWHERE;LEG-CREUTZ=DEFINED-AT-",
        str(np_ - undef), "-OF-", str(np_), "-EXTREME-POINTS-AND-EQUAL-TO-"
        "ONE-AT-", str(FS["ladder_word_tally"].get("DECONFINES", 0)),
        ";LEG-WINDING=THE-ORDER-PARAMETER-ANALOGUE"]))
    out.append("".join([
        "(a)CONDITIONAL=", str(nr), "-ROWS-ALL-STAMPED-", CR["stamp"],
        ";PLAQUETTE-EXPECTATIONS=",
        ",".join([r["plaquette_expectation"] + "@" + r["row"]
                  for r in CR["rows"]]),
        ";WINDING=", str(rz), "-ZERO-AND-", str(rn),
        "-NONZERO;THE-CONTROL-CARRIES-", CR["the_control_stamp"],
        "-AND-IS-NEVER-SPENT-AS-DERIVED"]))
    out.append("".join([
        "(b)FAMILY-SWEPT=", str(np_), "-EXTREME-POINTS-",
        str(FS["vertices"]), "-VERTICES-AND-", str(FS["edge_midpoints"]),
        "-EDGE-MIDPOINTS-ALL-RUN;FAMILY-INVARIANT=",
        "+".join(FS["family_invariant_observables"]), ";COUPLING-DEPENDENT=",
        "+".join(FS["coupling_dependent_observables"]), ";SLICES=", str(ns),
        "-EXACT-ONE-PARAMETER-ROWS-AGREE-AT-THE-AREA-LEG"]))
    CI = payload["constant_ladder_identity"]
    out.append("".join([
        "PRICE=THE-INVENTORY-IS-", str(PB["the_inventory"]),
        "-COUPLINGS-AND-THE-AREA-LEG-PARTITIONS-NONE-OF-THEM;THE-WINDING-"
        "LEG-PARTITIONS-", str(wn), "-AGAINST-", str(wz), "-OF-", str(np_),
        ";THE-HALVING-MODE-IS-ABSENT-AT-",
        str(PB["extreme_points_with_no_halving_mode"]), "-OF-", str(np_),
        ";THE-PERIMETER-MODE-IS-ABSENT-AT-",
        str(PB["extreme_points_with_no_perimeter_mode"]), "-OF-", str(np_),
        ";THE-CREUTZ-RATIO-IS-UNDEFINED-AT-", str(undef), "-OF-", str(np_),
        ";THE-CREUTZ-RATIO-IS-ONE-AT-",
        str(CI["the_creutz_ratio_is_one_at"]), "-WHICH-ARE-EXACTLY-THE-",
        str(CI["the_ladder_is_constant_in_the_perimeter_at"]),
        "-LADDERS-CONSTANT-IN-THE-PERIMETER"]))
    hs = SD["the_holonomys_own_spectrum"]
    out.append("".join([
        "SPECTRAL-DOOR=THE-TRANSFER-MATRIX-ON-A-TIME-SLICE-IS-NAMED-NOT-RUN-"
        "AT-", SD["the_door_named"]["states_per_slice"],
        "-STATES-PER-SLICE;THE-FINITE-FORM-IS-MEASURED-AT-",
        str(A["coins"] - CF["closed_form_failures"]), "-OF-",
        str(A["coins"]), "-COINS=W=A+B*P+C*2^-P;THE-ANSATZS-SPECTRUM-IS-",
        CF["the_transfer_spectrum"], "-WITH-GAP-", CF["the_gap"],
        "-AND-ITS-HALVING-MODE-IS-PRESENT-AT-",
        str(CF["coefficient_profile"]["C"].get("1", 0)), "-OF-",
        str(A["coins"]), "-COINS-AND-",
        str(PB["extreme_points_with_a_halving_mode"]), "-OF-", str(np_),
        "-EXTREME-POINTS;THE-WINDING-HOLONOMY-IS-UNITARY-AT-",
        str(hs["self_inversive_characteristic_polynomial"]), "-OF-",
        str(hs["holonomies_tested"]),
        "-SO-ITS-SPECTRUM-CARRIES-NO-DECAY;SPC-INHERITS-THE-GAP-AT-THAT-"
        "SUPPORT"]))
    OR = payload["orientation_reading"]
    cs = OR["the_conjugation_split"]
    out.append("".join([
        "ORIENTATION=", OR["status"], "-", OR["stamp"],
        ";THE-ORIENTED-SUBGROUP-HAS-INDEX-",
        str(OR["readings"][0]["index_of_the_oriented_subgroup"]),
        "-AT-BOTH-READINGS;COUPLINGS=",
        str(OR["readings"][0]["coupling_count"]), "-AT-ANCHORED-AND-",
        str(OR["readings"][1]["coupling_count"]),
        "-AT-ANCHORED-ORIENTED-AND-",
        str(OR["readings"][2]["coupling_count"]), "-AT-THE-EXTENSION-AND-",
        str(OR["readings"][3]["coupling_count"]),
        "-AT-EXTENSION-ORIENTED-SO-THE-DECLARATION-BUYS-OBSERVABLES-AND-"
        "COSTS-NO-COUPLING;THE-ODD-PART-IS-LAWFUL-ONLY-THERE-AND-IS-NON-"
        "ZERO-AT-", str(cs["shape_by_coin_traces_with_a_non_zero_odd_part"]),
        "-OF-", str(cs["traces_split"]), "-SHAPE-BY-COIN-TRACES-AT-",
        str(cs["shapes_carrying_an_odd_part"]), "-OF-",
        str(len(payload["loop_observable"]["base_point_rows"])),
        "-SHAPES-AND-AT-",
        str(OR["extreme_points_carrying_an_odd_observable"]), "-OF-",
        str(OR["extreme_points"]), "-EXTREME-POINTS"]))
    mi = {r["L"]: r["the_merging_index"] for r in D["the_L_boundary"]}
    out.append("".join([
        "L-BOUNDARY=THE-MERGING-INDEX-IS-8/GCD(L,8)-WHICH-IS-",
        str(mi[A["L"]]), "-HERE-AND-", str(mi[BL["L"]]), "-AT-L-",
        str(BL["L"]), ";AREA-BLINDNESS-AND-THE-CLOSED-FORM-AND-THE-GAP-"
        "SURVIVE-THE-BOUNDARY-", str(BL["area_disagreements"]),
        "-DISAGREEMENTS-OVER-", str(BL["comparison_by_coin_checks"]),
        "-CHECKS-AND-", str(BL["coins_with_identical_coefficients"]), "-OF-",
        str(A["coins"]), "-COINS-CARRY-IDENTICAL-COEFFICIENTS;THE-CLASS-"
        "MERGING-DOES-NOT-", str(BL["orbit_pairs_merged"]), "-MERGES-AT-L-",
        str(BL["L"]), "-AGAINST-", str(CL["orbit_pairs_merged"]), "-HERE"]))
    out.append("".join([
        "SCOPE=D=2;L=", str(A["L"]), ";BOUNDARY-L=", str(BL["L"]), ";FIELD=",
        A["field"], ";COINS=", str(A["coins"]), ";LINKS=", str(A["links"]),
        ";PLAQUETTES=", str(A["plaquettes"]), ";CARRIER=", A["carrier"],
        ";FULL-CONFIGURATION-SPACE=", A["configuration_space"],
        "-NOT-A-CARRIER-HERE;WEIGHTS=POSITIVE-EXACT-RATIONALS-NO-LOGS-NO-"
        "FLOATS;THE-POTENTIAL-IS-NOMINAL-AND-CARRIED-MULTIPLICATIVELY;"
        "CONFINEMENT-VOCABULARY-IS-LICENSED-FOR-THIS-UNIT-ONLY-AND-ONLY-IN-"
        "MEASURED-SENTENCES;NO-CONTINUUM-CLAIM;NO-SI-NUMBERS;NOT-QCD"]))
    return " -- ".join(out)


# ===========================================================================
# SECTION 17.  THE INSTRUMENT'S OWN SYNTAX TREE
# ===========================================================================

MUTANTS = [
    ("MUT-ARENA", "G-ARENA-REBUILT",
     "drops one coin from the derived family",
     "coins = coins[:-1]"),
    ("MUT-SOURCE-SWAP", "G-SOURCES-AT-THEIR-PINNED-DIGESTS",
     "reads one parent's digest from another parent's path",
     'bdigest(read_bytes("v14/paper-34-act.md")'),
    ("MUT-PATH-VALUE", "G-PATH-VALUE-ANCHORS",
     "moves an inherited coupling count by one",
     "val = 134"),
    ("MUT-VERBATIM", "G-VERBATIM-ANCHORS",
     "inverts a word inside a quoted definition",
     'needle.replace("inverted", "conjugated")'),
    ("MUT-CONSUMER-GHOST", "G-CONSUMER-REGISTER-IS-REAL",
     "names a consumer gate this instrument does not have",
     '"G-A-GATE-THIS-INSTRUMENT-DOES-NOT-HAVE"'),
    ("MUT-SIMPLICITY", "G-THE-LOOP-FAMILY-IS-A-FAMILY-OF-LOOPS",
     "calls a simple rectangle circuit non-simple",
     'simple_rows[0]["simple"] = False'),
    ("MUT-CANON", "G-THE-LOOP-FAMILY-IS-CLOSED-UNDER-THE-ACTING-GROUP",
     "drops the reversal from a loop's canonical name",
     "return min(rotations(c))"),
    ("MUT-FAMILY-CLOSURE", "G-THE-LOOP-FAMILY-IS-CLOSED-UNDER-THE-ACTING-"
     "GROUP", "declares the closed family unclosed",
     'orbit_rows[0]["closed_under_the_acting_group"] = False'),
    ("MUT-CLASSES", "G-THE-CLASSES-REBUILT",
     "fuses two induced classes into one",
     "classes[-1] + classes[-2]"),
    ("MUT-BASEPOINT", "G-THE-LOOP-OBSERVABLE-IS-BASE-POINT-BLIND",
     "reports a base-point disagreement on the plaquette",
     "mism = 1"),
    ("MUT-REVERSAL", "G-THE-LOOP-OBSERVABLE-IS-REVERSAL-BLIND",
     "reports a reversal disagreement",
     "rev_bad = 1"),
    ("MUT-PLAQUETTE", "G-PLAQUETTE-ROW-REPRODUCED",
     "drops one distinct plaquette trace value",
     "distinct = distinct[:-1]"),
    ("MUT-DISCRIMINATOR-RUNGS", "G-THE-DISCRIMINATOR-IS-WELL-DEFINED",
     "empties the Creutz rung list before the well-definedness gate",
     "rungs = []"),
    ("MUT-MERGING-LAW", "G-THE-MERGING-INDEX-LAW-REPRODUCED",
     "sets the merging index at the declared size to one",
     'lrows[1]["the_merging_index"] = 1'),
    ("MUT-PERIMETER-ONLY", "G-THE-LADDER-IS-A-FUNCTION-OF-THE-PERIMETER-"
     "ALONE", "reports an equal-perimeter disagreement",
     "perim_only = 1"),
    ("MUT-CLOSED-FORM", "G-THE-LADDER-CLOSED-FORM",
     "reports a closed-form verification failure at every coin",
     "bad = len(coins)"),
    ("MUT-ROW-UNSTAMPED", "G-THE-DECLARED-ROWS-BUILT",
     "strips the conditional stamp from one declared row",
     'rows[2]["stamp"] = "PLAIN"'),
    ("MUT-CONTROL-SPENT", "G-THE-CONTROL-STAMP-CARRIED",
     "spends the law-native control as a derived measure",
     'the_measure="DERIVED"'),
    ("MUT-SWEEP-TRUNCATED", "G-THE-FAMILY-SWEEP-IS-TOTAL",
     "drops one extreme point from the total sweep",
     "rows = rows[:-1]"),
    ("MUT-SLICES", "G-THE-FAMILY-SLICES",
     "reports an area-dependent slice",
     'rows[0]["area_seen"] = True'),
    ("MUT-PRICE-PARTITION", "G-THE-PRICE-BINDING",
     "claims the area leg partitions the inventory",
     'legs[0]["verdict"] = "PARTITIONS-THE-INVENTORY"'),
    ("MUT-ORDER-RANGE", "G-THE-ORDER-PARAMETER-RANGE",
     "claims the order parameter is pinned by the action route",
     "pinned = True"),
    ("MUT-SPECTRAL-UNITARY", "G-THE-SPECTRAL-DOOR",
     "breaks one holonomy's unit determinant",
     "modone -= 1"),
    ("MUT-ORIENTATION-STAMP", "G-THE-ORIENTATION-READING-IS-PRICED",
     "calls the oriented declaration a derivation",
     'dec[1]["declaration_status"] = "DERIVED"'),
    ("MUT-ORIENTATION-UNSTAMPED", "G-THE-ORIENTATION-READING-IS-PRICED",
     "strips the declaration stamp from an orientation row",
     'dec[3]["stamp"] = "PLAIN"'),
    ("MUT-ODD-SPLIT", "G-THE-CONJUGATION-SPLIT-IS-EXACT",
     "reports a conjugation split that does not reconstruct its trace",
     "split_bad = 1"),
    ("MUT-ODD-UNSTAMPED", "G-THE-ODD-OBSERVABLES-CARRY-THEIR-DECLARATION",
     "renders an odd-part value without its declaration stamp",
     'rowvals[0]["stamp"] = "PLAIN"'),
    ("MUT-ORIENTATION-ODDNESS", "G-THE-ODD-PART-IS-ORIENTATION-ODD",
     "reports an odd part that does not negate under reversal",
     "rev_odd_bad = 1"),
    ("MUT-BOUNDARY-AREA", "G-THE-BOUNDARY-LATTICE-RUN",
     "reports an area disagreement at the boundary lattice",
     "viol = 1"),
    ("MUT-CONTROL-ARM", "G-EVERY-PREREGISTERED-WORD-IS-EMITTABLE",
     "forges agreement on a control arm whose head word it also changes",
     'rows[0]["head_word"] = "POT-DECONFINES-AT"'),
    ("MUT-HEAD", "G-THE-TWO-HEAD-LAWS-AGREE",
     "feeds the head law a row list that is not the measurement's",
     'rw = [("DECONFINES", "WINDING-ORDER-NONZERO")]'),
    ("MUT-MUTANT-DESCRIPTION", "G-EVERY-MUTANT-DESCRIPTION-IS-TRUE",
     "drifts one mutant's published token away from the code it names",
     'token = token + "-DRIFTED"'),
    ("MUT-LOOPFAM-FIELD", "G-THE-LOOP-FAMILY-IS-THE-MISSING-OBJECT",
     "claims the parent already grew a loop family",
     "ok_missing = False"),
    ("MUT-EXTREME-SPLIT", "G-THE-EXTREME-POINTS-REBUILT",
     "moves one extreme point from the midpoints to the vertices",
     "midpoints = midpoints[1:]"),
    ("MUT-HEAD-WORD", "G-THE-HEAD-IS-DERIVED",
     "returns a head word the pin never pre-registered",
     'word = "POT-A-WORD-THE-PIN-NEVER-PREREGISTERED"'),
    ("MUT-GHOST-FUNCTION", "G-THE-FUNCTION-INVENTORY-IS-TOTAL",
     "plants a function the inventory does not declare",
     "def ghost_helper(S):"),
    ("MUT-REGISTRY-EVASION", "G-THE-MUTANT-REGISTRY-IS-TOTAL",
     "plants a mutant switch built from a computed name",
     "_gn = 'MUT-' + 'GHOST'"),
    ("MUT-AST-BLIND", "G-THE-ARITHMETIC-IS-EXACT",
     "plants a floating-point literal in the source",
     "_EPSILON_FLOAT = 1e-12"),
    ("MUT-PAPER-CLAIM", "G-PAPER-CLAIMS-RENDERED",
     "renders one paper claim at a value the receipt does not carry",
     'c["text"] = c["text"] + "X"'),
    ("MUT-PAPER-VERDICT", "G-PAPER-VERDICT-BLOCK",
     "licenses a verdict block the paper does not carry",
     "lic = lic + \"-TWIN\""),
    ("MUT-PAPER-POLARITY", "G-PAPER-POLARITY",
     "admits a direction-bearing headline and its inverse together",
     "flips = flips[:-1]"),
    ("MUT-PAPER-HEADER", "G-PAPER-HEADERS-BOUND",
     "drops a header row from the bound set",
     "heads = heads[:-1]"),
    ("MUT-PAPER-NUMERAL", "G-PAPER-NUMERALS-COVERED",
     "drops a measured numeral from the registry so a real one goes "
     "uncovered", 'reg.discard("640")'),
    ("MUT-PAPER-SPELLED", "G-PAPER-SPELLED-NUMERALS",
     "leaves a spelled numeral out of the scan",
     "words = words[:-1]"),
    ("MUT-LICENCE-WALL", "G-THE-CONFINEMENT-LICENCE-WALL",
     "admits a confinement word in a sentence carrying no measured value",
     "unlicensed = []"),
    ("MUT-MUSTNOT", "G-PAPER-MUST-NOT",
     "empties the declaring-sentence register the sweep is taken against",
     "decl = []"),
    ("MUT-SEAL", "G-THE-SEAL-IS-TOTAL",
     "leaves a published key out of the seal manifest",
     "declared = declared[:-1]"),
    ("MUT-LEDGER-CHAIN", "G-THE-LEDGER-CHAIN-VERIFIES",
     "edits a ledger row after its gate closed",
     'rows[1]["detail"] = rows[1]["detail"] + " "'),
    ("MUT-TABLE-ROW", "G-PAPER-TABLE-ROWS-COVERED",
     "drops a licensed data row from the rendered row multiset",
     "data = data[:-1]"),
    ("MUT-CONSUMER-UNREAD", "G-CONSUMER-REGISTER-IS-REAL",
     "leaves a verbatim window unread by the gate that names it",
     'r["anchor"] != "VB-SMU-PRICE"'),
    ("MUT-CONSTANT-SET", "G-THE-CREUTZ-UNIT-SET-IS-THE-CONSTANT-LADDER-SET",
     "drops one point from the constant-ladder set the identity is taken "
     "against", "const = set(sorted(const)[1:])"),
    ("MUT-LENGTH-READING", "G-THE-LENGTH-DOES-NOT-DETERMINE-THE-OBSERVABLE",
     "reports that no two shapes of equal length disagree at any coin",
     "coins_at_which_they_disagree=0"),
    ("MUT-UNIVERSAL", "G-THE-AREA-BLINDNESS-IS-UNIVERSAL-OVER-MEASURES",
     "reports an interior measure at which the area is seen",
     "interior_bad = 1"),
    ("MUT-PAPER-CLAIM-COUNT", "G-PAPER-CLAIMS-RENDERED",
     "raises one claim's declared occurrence count above the rendering",
     'C[1]["need"] = C[1]["need"] + 1'),
    ("MUT-PAPER-SPAN", "G-PAPER-INLINE-SPANS-LICENSED",
     "drops a declared path the paper spans from the licensed set",
     "licensed_spans.discard(RECEIPT_REL)"),
    ("MUT-PAPER-SHORT-NUMERAL", "G-PAPER-SHORT-NUMERALS-IN-CONTEXT",
     "drops a rendered short numeral from the context registry",
     'ctx.discard("24")'),
    ("MUT-PAPER-QUOTES", "G-PAPER-QUOTES-INSIDE-THE-WINDOWS",
     "drops one pinned window from the set the quotations are read against",
     "windows = windows[1:]"),
    ("MUT-MUSTNOT-CONTENT", "G-PAPER-MUST-NOT",
     "plants a continuum phrase in the swept body",
     "The lattice spacing goes to zero."),
    ("MUT-COVERAGE", "G-COVERAGE-AT-AN-HONEST-DENOMINATOR",
     "puts a gate with neither a falsifier nor a forcing on the clean path",
     '"G-A-GATE-WITH-NEITHER-A-FALSIFIER-NOR-A-FORCING"'),
    ("MUT-RECEIPT-HEADER", "G-THE-RECEIPT-HEADER-IS-BOUND",
     "publishes a paper digest the bytes do not have",
     'paper = "0" * 12'),
    ("MUT-TRANSCRIPT", "G-THE-TRANSCRIPT-RECONCILES",
     "fabricates a transcript line for a gate that never ran",
     '"G-A-GATE-THAT-NEVER-RAN"'),
]

FUNCTION_INVENTORY = [
    "say", "mut", "digest", "bdigest", "own_source", "imul", "iadd",
    "iconj", "ishift", "izpow", "in_real_subfield", "qs", "qs_add",
    "qs_mul", "qs_is_zero", "qs_div", "qs_less", "qs_str", "sym_qs", "hull",
    "measure_the_order_parameter_range", "odd_qs", "point_on_dir",
    "transported_link", "swap_conjugate", "orientation_sign",
    "link_stencil_orbits", "measure_the_orientation_reading",
    "hdr", "read_bytes",
    "load_sources", "dig", "measure_path_values", "wsnorm", "mnorm",
    "measure_verbatim", "vbwin", "measure_consumers", "build_alphabet",
    "build_coins", "cell", "build_paper_tables", "value_pairs",
    "spelled_values", "measure_the_constant_ladder_identity",
    "measure_the_length_reading", "measure_the_universal_over_measures",
    "measure_coverage", "measure_the_receipt_header",
    "measure_the_transcript", "addspan",
    "coin_sector", "coin_unitary_second_route", "gauge_twist", "build_arena",
    "rect_cycle", "wind_cycle", "stair_cycle", "rotations", "canon",
    "steps_of", "homology", "holonomy_trace", "enumerate_family",
    "point_symmetries", "apply_point", "chart_elements", "transport_loop",
    "measure_loop_family", "twist_orbits", "realisable_twists",
    "phase_order", "measure_classes", "measure_the_loop_observable",
    "area_comparisons",
    "creutz_rungs", "classify", "measure_the_discriminator", "mode_fit",
    "mode_value", "perimeter_table", "support_pairs",
    "measure_the_closed_form", "gibbs", "measure_declared_rows",
    "measure_family_sweep", "measure_family_slices",
    "measure_the_price_binding", "newton_char_poly",
    "measure_the_spectral_door", "measure_the_boundary_lattice", "head_law",
    "second_head_law", "measure_the_control_arms", "measure_the_verdict",
    "render_verdict", "rerender_verdict", "scan_syntax_tree",
    "sentences_of", "number_tokens", "receipt_number_registry",
    "build_paper_claims", "measure_paper", "measure_totals", "write_out",
    "run", "selftest", "main", "tree_state",
    "__init__", "gate", "verify_chain", "resolve", "take", "reverify",
    "addv", "ends", "add", "walk", "tally", "averages", "area_table",
    "perim_table", "holed_table", "short_table",
]


def scan_syntax_tree(S):
    src = own_source()
    tree = ast.parse(src)
    funcs, calls, names, floats = [], set(), set(), 0
    muts = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            funcs.append(node.name)
        if isinstance(node, ast.Call):
            f = node.func
            nm = getattr(f, "id", None) or getattr(f, "attr", None)
            if nm:
                calls.add(nm)
            if nm == "mut":
                if node.args and isinstance(node.args[0], ast.Constant):
                    muts.add(node.args[0].value)
                else:
                    muts.add("UNREADABLE-SWITCH")
        if isinstance(node, ast.Name):
            names.add(node.id)
        if isinstance(node, ast.Constant) and isinstance(node.value, float):
            floats += 1
    banned = sorted(set(BANNED_CALLS) & calls)
    bannedn = sorted(set(BANNED_NAMES) & names)
    LD.gate("G-THE-ARITHMETIC-IS-EXACT",
            "an AST scan of this instrument's own syntax tree is a gate, and "
            "it carries the clause the pin's multiplicative framing needs: "
            "no call to a logarithm, an exponential, a square root or a "
            "power exists in this source at all, no floating-point literal "
            "occurs anywhere, and no banned module is named -- so exact "
            "arithmetic is a property of the instrument rather than a "
            "promise about it",
            not banned and not bannedn and floats == 0,
            "%d functions; banned calls %s; banned names %s; float literals "
            "%d" % (len(funcs), banned, bannedn, floats))
    declared = {m[0] for m in MUTANTS}
    unregistered = sorted(muts - declared)
    unused = sorted(declared - muts)
    LD.gate("G-THE-MUTANT-REGISTRY-IS-TOTAL",
            "the mutant registry is checked TOTAL against the instrument's "
            "own syntax tree: every switch the scan can read is declared and "
            "every declared mutant is present in the source, and a switch "
            "the scan CANNOT read is fatal rather than forgiven, so a "
            "falsifier cannot exist as an unswept branch",
            not unregistered and not unused,
            "%d switches in the tree, %d declared; unregistered %s; unused "
            "%s" % (len(muts), len(declared), unregistered, unused))
    extra = sorted(set(funcs) - set(FUNCTION_INVENTORY))
    gone = sorted(set(FUNCTION_INVENTORY) - set(funcs))
    LD.gate("G-THE-FUNCTION-INVENTORY-IS-TOTAL",
            "the function inventory is checked total the same way, so a "
            "helper that appeared after the inventory was written -- or one "
            "that vanished from it -- stops the delivery run",
            not extra and not gone,
            "%d functions in the tree, %d declared; undeclared %s; missing "
            "%s" % (len(funcs), len(FUNCTION_INVENTORY), extra, gone))
    described = []
    for nm, tg, what, token in MUTANTS:
        if mut("MUT-MUTANT-DESCRIPTION") and nm == "MUT-ARENA":
            token = token + "-DRIFTED"
        described.append({"mutant": nm, "target": tg, "what": what,
                          "token": token, "token_in_source": token in src})
    bad = [d["mutant"] for d in described if not d["token_in_source"]]
    LD.gate("G-EVERY-MUTANT-DESCRIPTION-IS-TRUE",
            "E-23: each mutant's published description names the exact token "
            "it plants or changes, and that token is located in this "
            "instrument's own source text -- a description that has drifted "
            "from the code it describes stops the run",
            not bad,
            "%d mutants, %d with their named token located, %s"
            % (len(described), sum(1 for d in described
                                   if d["token_in_source"]),
               "none missing" if not bad else "missing %s" % bad))
    S["arithmetic"] = {
        "field": "Q(zeta_8)-AS-INTEGER-FOUR-TUPLES-WITH-A-PER-ROW-POWER-OF-"
                 "TWO-SCALE",
        "float_literals": floats, "banned_calls_present": banned,
        "banned_names_present": bannedn,
        "functions": len(funcs), "mutant_switches": len(muts),
        "no_logarithm_no_exponential_no_square_root_no_power": True}
    S["mutants"] = {"declared": len(MUTANTS), "rows": described,
                    "swept_by": "THE-EXTERNAL-ALL-MUTANTS-BATTERY-NOT-THE-"
                                "DELIVERY-RUN"}
    SEAL.take("THE ARITHMETIC", "arithmetic", "G-THE-ARITHMETIC-IS-EXACT",
              S["arithmetic"])
    SEAL.take("THE MUTANTS", "mutants", "G-EVERY-MUTANT-DESCRIPTION-IS-TRUE",
              S["mutants"])


# ===========================================================================
# SECTION 18.  THE PAPER GATES
# ===========================================================================

CONFINEMENT_WORDS = ["confinement", "confines", "confining", "confined",
                     "deconfinement", "deconfines", "deconfining",
                     "area law", "string tension", "static potential",
                     "order parameter",
                     "enclosed area", "flux tube", "linear potential",
                     "grows linearly", "tension per unit", "quark",
                     "screening", "wilson loop"]

DECLARING_MARKERS = [
    "licensed for this unit only",
    "every sentence that uses one of them",
    "the pin's own wall",
    "the vocabulary this unit is licensed to use",
]

JOINING_PHRASES = ["-of-the-", "-of-", "-against-", " of the ", " of ",
                   " against ", "-at-", " at "]

SI_UNITS = ["metre", "metres", "meter", "meters", "second", "seconds",
            "kilogram", "kilograms", "joule", "joules", "kelvin", "newton",
            "newtons", "electronvolt", "fermi", "femtometre", "GeV", "MeV",
            "eV"]

CONTINUUM_PHRASES = ["continuum limit", "in the continuum",
                     "lattice spacing goes", "as a goes to zero",
                     "the spacing to zero", "physical units"]

MUST_NOT = SI_UNITS + CONTINUUM_PHRASES

MUST_NOT_DECLARERS = ["no SI number", "no continuum claim",
                      "is swept over this paper's own text"]

POLARITY = [
    ("the area does not enter it", "the area enters it"),
    ("is a function of the perimeter alone", "is a function of the area"),
    ("FAMILY-INVARIANT", "partitions the inventory at the area leg"),
    ("partitions the inventory", "partitions none of the inventory"),
    ("carries no decaying direction", "carries a decaying direction"),
    ("is named and not run", "is run and not named"),
    ("survive the boundary", "die at the boundary"),
    ("never spent as derived", "is spent as derived"),
    ("no silent cap", "a silent cap"),
]


def sentences_of(text):
    """sentences, not lines: a markdown paragraph is reflowed across lines,
    so the blocks are joined first and only then split at sentence ends --
    otherwise a wall gate would be measuring the typesetting."""
    out = []
    for block in text.split("\n\n"):
        joined = " ".join(x.strip() for x in block.split("\n"))
        cur = []
        for ch in joined:
            cur.append(ch)
            if ch in ".!?":
                t = "".join(cur).strip()
                if t:
                    out.append(t)
                cur = []
        t = "".join(cur).strip()
        if t:
            out.append(t)
    return out


def number_tokens(text):
    toks, cur = [], []
    for ch in text:
        if ch.isdigit():
            cur.append(ch)
        else:
            if cur:
                toks.append("".join(cur))
            cur = []
    if cur:
        toks.append("".join(cur))
    return toks


def receipt_number_registry(payload):
    reg = set()

    def walk(o):
        if isinstance(o, dict):
            for k, v in o.items():
                for t in number_tokens(str(k)):
                    reg.add(t)
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)
        else:
            for t in number_tokens(str(o)):
                reg.add(t)
    walk(payload)
    if mut("MUT-PAPER-NUMERAL"):
        reg.discard("640")
    return reg


def hdr(*keys):
    return "| " + " | ".join(k.replace("_", " ") for k in keys) + " |"


def cell(v):
    """one table cell, rendered from a receipt value: booleans become the
    words the tables use, tallies become 'value count' lists, and everything
    else is its own string."""
    if isinstance(v, bool):
        return "yes" if v else "no"
    if isinstance(v, dict):
        return ", ".join("%s %s" % (k, v[k]) for k in sorted(v))
    if isinstance(v, list):
        return ", ".join(str(x) for x in v)
    return str(v)


def build_paper_tables(S):
    """THE TABLES, RENDERED FROM THE RECEIPT'S OWN ROW OBJECTS -- header and
    data alike.  K3's MAJOR-5 at this unit: a header bound while its cells
    are free lets a row label or a verdict word be exchanged in the paper
    without the run noticing, so every data row is rendered here from the
    row object it reports and the paper's rows are compared against this
    rendering as a MULTISET, exactly as the headers already were.  The
    columns are the receipt keys themselves, and that correspondence is
    checked rather than trusted."""
    lf, dc = S["loop_family"], S["discriminator"]
    cr, pb = S["conditional_rows"], S["price_binding"]
    bl, orr = S["boundary_lattice"], S["orientation_reading"]
    lr = S["length_reading"]
    tables = [
        ("THE-SIMPLICITY-CENSUS", lf["simplicity_rows"],
         ["a", "b", "steps", "distinct_links", "distinct_sites", "simple"]),
        ("THE-ORBIT-CLOSURE", lf["orbit_rows"],
         ["reading", "chart_order", "distinct_loops", "orbits",
          "images_outside_the_declared_family"]),
        ("THE-EQUAL-LENGTH-READING", lr["rows"],
         ["step_count", "shapes_of_that_length",
          "coins_at_which_they_disagree", "coins"]),
        ("THE-MERGING-INDEX-LAW", dc["the_L_boundary"],
         ["L", "residual_order_on_the_torus", "the_link_stencils_gauge_image",
          "the_merging_index",
          "the_odd_twist_is_a_gauge_transformation_here"]),
        ("THE-DECLARED-ROWS", cr["rows"],
         ["row", "weight_system", "exponent", "plaquette_expectation",
          "ladder_word", "winding_word"]),
        ("THE-DECLARED-ROWS-MODES", cr["rows"],
         ["row", "mode_A", "mode_B", "mode_C", "closed_form_holds"]),
        ("THE-PRICE-PARTITION", pb["legs"],
         ["leg", "distinct_values_over_the_extreme_points", "partitions",
          "tally_over_the_136_extreme_points", "verdict"]),
        ("THE-CONTROL-ARMS", S["control_arms"]["arms"],
         ["arm", "the_synthetic_law", "ladder_word", "head_word", "agrees"]),
        ("THE-BOUNDARY-COMPARISON", bl["the_comparison_table"],
         ["quantity", "at_the_declared_L", "at_the_boundary_L"]),
        ("THE-ORIENTATION-PRICE", orr["readings"],
         ["reading", "chart_group_order",
          "the_link_stencils_chart_stabilizer", "orbits", "coupling_count"]),
    ]
    heads, data, unbound = [], [], []
    for name, rows, keys in tables:
        for k in keys:
            if any(k not in r for r in rows):
                unbound.append("%s/%s" % (name, k))
        heads.append(hdr(*keys))
        for r in rows:
            data.append("| " + " | ".join(cell(r.get(k)) for k in keys) + " |")
    if mut("MUT-PAPER-HEADER"):
        heads = heads[:-1]
    if mut("MUT-TABLE-ROW"):
        data = data[:-1]
    return heads, data, unbound, tables


def value_pairs(text):
    """the (value, value) pairs a string states TOGETHER -- two numerals
    separated by nothing but one of the declared joining phrases.  '96 of
    136' is what a reader carries away, and a pair is licensed only if this
    run measured those two values AND JOINED THEM THE SAME WAY; a sentence
    that pairs two separately measured numbers into a relation nothing
    measured stops the delivery run.  The pair carries the joining phrase
    and NOT the subject it is said about, so referent binding is outside
    this function and outside the wall that uses it."""
    t = text.lower()
    for j in JOINING_PHRASES:
        t = t.replace(j, "\x00")
    parts = t.split("\x00")
    out = set()
    for i in range(len(parts) - 1):
        left, right = parts[i], parts[i + 1]
        a, b = [], []
        for ch in reversed(left):
            if ch.isdigit():
                a.append(ch)
            else:
                break
        for ch in right:
            if ch.isdigit():
                b.append(ch)
            else:
                break
        if a and b:
            out.add(("".join(reversed(a)), "".join(b)))
    return out


def spelled_values(text):
    """a general spelled-number reader, so that a count written in words is
    read the way a reader reads it: units, teens and tens compose, 'hundred'
    and 'thousand' scale, and the resolved VALUE is what the gate then asks
    the receipt for."""
    words, cur = [], []
    for ch in text.lower():
        if ch.isalpha():
            cur.append(ch)
        else:
            if cur:
                words.append("".join(cur))
            cur = []
    if cur:
        words.append("".join(cur))
    out, acc, live = [], 0, False
    for w in words:
        if w in NUMWORD_TENS:
            if live:
                out.append(acc)
            acc, live = NUMWORD_TENS[w], True
        elif w in NUMWORD_TEENS:
            if live:
                out.append(acc)
            acc, live = NUMWORD_TEENS[w], True
        elif w in NUMWORD_UNITS:
            if live and acc in NUMWORD_TENS.values():
                acc = acc + NUMWORD_UNITS[w]
            else:
                if live:
                    out.append(acc)
                acc = NUMWORD_UNITS[w]
            live = True
        elif w in NUMWORD_SCALES:
            acc = (acc if live else 1) * NUMWORD_SCALES[w]
            live = True
        elif w == "and":
            continue
        else:
            if live:
                out.append(acc)
            acc, live = 0, False
    if live:
        out.append(acc)
    return out


def build_paper_claims(S):
    """every number the paper states, rendered here from the receipt.  Each
    claim carries the number of times the licensed rendering occurs in the
    delivered text, and the gate compares that count for EQUALITY -- so a
    second occurrence corrupted, or a rendering deleted, both stop the run.
    The multiplicity is a declaration about the rendering, not a count of
    anything measured."""
    lf, dc = S["loop_family"], S["discriminator"]
    cr, fs = S["conditional_rows"], S["family_sweep"]
    pb, sd = S["price_binding"], S["spectral_door"]
    bl, cf = S["boundary_lattice"], S["closed_form"]
    ar, cl = S["arena"], S["classes"]
    ci, lr, un = (S["constant_ladder_identity"], S["length_reading"],
                  S["the_universal"])
    C = []

    def add(cid, text, need=1):
        C.append({"claim": cid, "text": text, "need": need})

    add("C-ARENA", "%d sites, %d links and %d plaquettes"
        % (ar["sites"], ar["links"], ar["plaquettes"]))
    add("C-ALPHABET", "returns %d elements" % ar["alphabet"])
    add("C-COINS", "returns %d coins splitting into %d diagonal, %d "
        "antidiagonal and %d balanced"
        % (ar["coins"], ar["sectors"]["DIAGONAL"],
           ar["sectors"]["ANTIDIAGONAL"], ar["sectors"]["BALANCED"]))
    add("C-SHAPES", "%d of the %d declared shapes"
        % (S["loop_observable"]["shapes_whose_raw_trace_is_already_real"],
           len(S["_shapes"])))
    add("C-PLAQ-VALUES", "takes %d distinct values"
        % S["loop_observable"]["plaquette_distinct_values"])
    add("C-PLAQ-COUNT", "counting expectation is %s"
        % S["loop_observable"]["plaquette_counting_expectation"])
    add("C-PLAQ-DIAG", "%d of the diagonal coins are non-flat"
        % S["loop_observable"]["plaquette_nonflat_diagonal_coins"])
    add("C-CONSTANT-SINGLE", "a single mode is active at %d"
        % ci["single_mode_extreme_points"], 2)
    add("C-CONSTANT-ONLY-B", "at the remaining %d"
        % ci["single_mode_but_perimeter_proportional"])
    add("C-LENGTH", "%d of the %d coins"
        % (lr["rows"][0]["coins_at_which_they_disagree"], ar["coins"]), 2)
    add("C-UNIVERSAL", "%d Dirac measures and %d interior measures"
        % (un["dirac_measures"], un["interior_measures"]))
    add("C-UNIVERSAL-CHECKS", "%d comparisons and %d mismatches"
        % (un["comparisons_in_all"], un["mismatches_in_all"]))
    add("C-AREA-BASIS", "%d area-discriminating comparison-by-coin checks"
        % cf["area_discriminating_comparison_by_coin_checks"], 3)
    add("C-CROSS-BASIS", "%d of them are a shape compared with itself and %d "
        "are cross-shape" % (cf["equal_perimeter_self_comparisons"],
                             cf["equal_perimeter_cross_shape_comparisons"]))
    add("C-HALVING-SUPPORT", "present at %d of the %d coins and at %d of the "
        "%d extreme points"
        % (cf["coefficient_profile"]["C"].get("1", 0), ar["coins"],
           pb["extreme_points_with_a_halving_mode"],
           fs["extreme_points"]), 3)
    add("C-WALL-WORDS", "%d declared words" % len(CONFINEMENT_WORDS), 2)
    add("C-EXIT", "exits %s" % EXIT_CONVENTIONS["delivery"])
    add("C-EXIT-UNKNOWN", "Unknown flags exit %s"
        % EXIT_CONVENTIONS["unknown_flag"])
    add("C-SLICE-CLASSES", "%d couplings against %d classes"
        % (len(S["family_slices"]["the_coupling_values"]),
           S["family_slices"]["distinct_classes_raised"]))
    add("C-FAMILY", "%d placements and %d distinct loops"
        % (lf["placements"], lf["distinct_loops"]), 2)
    add("C-FAMILY-SPLIT", "%d contractible and %d winding"
        % (lf["contractible"], lf["winding"]), 2)
    add("C-EXTENTS", "simple at %d of the %d sizes swept"
        % (lf["simple_rectangle_shapes"], lf["rectangle_sizes_swept"]))
    add("C-ORBITS", "%d orbits under a chart group of order %d"
        % (lf["orbit_rows"][0]["orbits"],
           lf["orbit_rows"][0]["chart_order"]), 2)
    add("C-ESCAPES", "%d images outside the declared family"
        % lf["orbit_rows"][1]["images_outside_the_declared_family"], 3)
    add("C-COMPARISONS", "%d area-discriminating comparisons and %d Creutz "
        "rungs" % (dc["area_discriminating_comparisons"],
                   dc["creutz_rungs"]), 2)
    add("C-PERIM-ONLY", "%d shape-by-coin comparisons at equal perimeter "
        "and %d disagreements" % (cf["equal_perimeter_comparisons"],
                                  cf["equal_perimeter_disagreements"]))
    add("C-CLOSED-FORM", "%d closed-form failures over %d coins"
        % (cf["closed_form_failures"], ar["coins"]))
    add("C-SPECTRUM", "spectrum %s and gap %s"
        % (cf["the_transfer_spectrum"], cf["the_gap"]), 3)
    add("C-CLASSES", "%d classes against %d parent orbits, %d pairs merged"
        % (cl["classes"], cl["parent_orbits"], cl["orbit_pairs_merged"]))
    add("C-EXTREME", "%d vertices and %d edge midpoints"
        % (cl["extreme_points_that_are_vertices"],
           cl["extreme_points_that_are_edge_midpoints"]), 3)
    for r in cr["rows"]:
        add("C-ROW-" + r["row"], "%s at %s"
            % (r["plaquette_expectation"], r["row"]))
    add("C-ROW-WINDING", "%d of the %d declared rows carries a non-zero "
        "winding expectation"
        % (cr["winding_word_tally"].get("WINDING-ORDER-NONZERO", 0),
           len(cr["rows"])))
    add("C-SWEEP", "%d extreme points swept, %d vertices and %d edge "
        "midpoints" % (fs["extreme_points"], fs["vertices"],
                       fs["edge_midpoints"]), 2)
    add("C-SWEEP-WIND", "%d with a non-zero winding expectation and %d with "
        "zero" % (fs["winding_word_tally"].get("WINDING-ORDER-NONZERO", 0),
                  fs["winding_word_tally"].get("WINDING-ORDER-ZERO", 0)))
    add("C-SWEEP-UNIT", "%d of the %d extreme points where the ratio is one"
        % (fs["ladder_word_tally"].get("DECONFINES", 0),
           fs["extreme_points"]), 3)
    add("C-PRICE", "the inventory of %d couplings" % pb["the_inventory"], 3)
    add("C-PRICE-C", "absent at %d of the %d"
        % (pb["extreme_points_with_no_halving_mode"],
           fs["extreme_points"]), 2)
    add("C-PRICE-B", "absent at %d of them"
        % pb["extreme_points_with_no_perimeter_mode"], 2)
    add("C-PRICE-UNDEF", "undefined at %d of them"
        % pb["extreme_points_where_the_creutz_ratio_is_undefined"])
    add("C-DOOR", "%s states per time slice"
        % sd["the_door_named"]["states_per_slice"], 2)
    add("C-DOOR-UNITARY", "%d of %d holonomies"
        % (sd["the_holonomys_own_spectrum"][
            "self_inversive_characteristic_polynomial"],
           sd["the_holonomys_own_spectrum"]["holonomies_tested"]), 2)
    add("C-BOUNDARY", "%d comparison-by-coin checks at L = %d with %d "
        "disagreements" % (bl["comparison_by_coin_checks"], bl["L"],
                           bl["area_disagreements"]), 2)
    add("C-BOUNDARY-MODES", "%d of the %d coins carry identical coefficients"
        % (bl["coins_with_identical_coefficients"], ar["coins"]))
    add("C-BOUNDARY-MERGE", "%d merges at L = %d against %d here"
        % (bl["orbit_pairs_merged"], bl["L"], cl["orbit_pairs_merged"]))
    add("C-ARMS", "%d control arms" % len(S["control_arms"]["arms"]))
    add("C-SLICES", "%d exact one-parameter slices"
        % S["family_slices"]["slices"])
    orr = S["orientation_reading"]
    cs = orr["the_conjugation_split"]
    add("C-ORIENT-INDEX", "the index of the oriented subgroup is %d at both "
        "readings" % orr["readings"][0]["index_of_the_oriented_subgroup"])
    add("C-ORIENT-PRICE", "%d couplings at the anchored reading and %d at "
        "the oriented one" % (orr["readings"][0]["coupling_count"],
                              orr["readings"][1]["coupling_count"]))
    add("C-ORIENT-ODD", "%d of %d shape-by-coin traces carry a non-zero odd "
        "part at %d of the %d shapes"
        % (cs["shape_by_coin_traces_with_a_non_zero_odd_part"],
           cs["traces_split"], cs["shapes_carrying_an_odd_part"],
           len(S["_shapes"])), 2)
    add("C-ORIENT-POINTS", "%d of the %d extreme points carry at least one"
        % (orr["extreme_points_carrying_an_odd_observable"],
           orr["extreme_points"]))
    add("C-ORIENT-ROWS", "%d non-zero odd observables at every declared row"
        % max(r["non_zero_odd_observables"]
              for r in orr["what_becomes_lawful"]), 2)
    T = S["totals"]
    add("C-ANCHORS", "%d file-bytes anchors, %d path-value anchors and %d "
        "verbatim-text anchors, %d anchors in all"
        % (T["sources"], T["path_value_anchors"], T["verbatim_anchors"],
           T["anchors"]))
    add("C-GATES", "%d gates close before the paper gates"
        % T["gates_closed"])
    add("C-SEALED", "%d objects are sealed before the paper gates"
        % T["sealed_objects"])
    add("C-MUTANTS", "%d declared mutants" % T["mutants_declared"])
    if mut("MUT-PAPER-CLAIM"):
        C[0]["text"] = C[0]["text"] + "X"
    if mut("MUT-PAPER-CLAIM-COUNT"):
        C[1]["need"] = C[1]["need"] + 1
    return C


def measure_paper(S, payload, verdict, vb):
    raw = read_bytes(PAPER_REL)
    if raw is None:
        raise GateFail("G-PAPER-CLAIMS-RENDERED :: the paper is absent at "
                       "its declared path")
    text = raw.decode()
    norm = mnorm(text)

    claims = build_paper_claims(S)
    for c in claims:
        c["hits"] = norm.count(mnorm(c["text"]))
        c["covered"] = c["hits"] == c["need"]
    missing = [c["claim"] for c in claims if not c["covered"]]
    LD.gate("G-PAPER-CLAIMS-RENDERED",
            "every number the paper states is RENDERED FROM THE RECEIPT and "
            "located in the delivered text at its declared occurrence count "
            "BY EQUALITY and not by a floor, so a claim rendered twice and "
            "corrupted at one of the two -- which a floor would forgive -- "
            "stops the delivery run, and so does a rendering deleted",
            not missing,
            "%d claims, %d at their declared occurrence counts, %d "
            "occurrences in all, missing %s"
            % (len(claims), sum(1 for c in claims if c["covered"]),
               sum(c["hits"] for c in claims),
               [(c["claim"], c["hits"], c["need"]) for c in claims
                if not c["covered"]][:6]))

    blocks, inblk, cur = [], False, []
    for line in text.split("\n"):
        if line.strip().startswith("```"):
            if inblk:
                blocks.append("\n".join(cur))
                cur = []
            inblk = not inblk
            continue
        if inblk:
            cur.append(line)
    lic = verdict
    if mut("MUT-PAPER-VERDICT"):
        lic = lic + "-TWIN"
    got = [wsnorm(b) for b in blocks]
    want = [wsnorm(lic)]
    LD.gate("G-PAPER-VERDICT-BLOCK",
            "the paper's fenced blocks are compared as a MULTISET against "
            "the single verdict block this run licenses, so neither a stale "
            "verdict nor a forged twin beside the clean one can be "
            "delivered, and the licensed string is itself required to equal "
            "an independent reconstruction that reads only the receipt",
            sorted(got) == sorted(want),
            "%d fenced blocks in the paper, %d licensed, equal as multisets "
            "%s" % (len(got), len(want), sorted(got) == sorted(want)))

    flips = list(POLARITY)
    if mut("MUT-PAPER-POLARITY"):
        flips = flips[:-1]
    pol = []
    for good, bad in flips:
        pol.append({"kept": good, "flip": bad,
                    "kept_present": mnorm(good) in norm,
                    "flip_absent": mnorm(bad) not in norm})
    badpol = [p for p in pol if not (p["kept_present"] and p["flip_absent"])]
    LD.gate("G-PAPER-POLARITY",
            "every direction-bearing headline is bound by a polarity list: "
            "the sentence as measured must be present and its inverse must "
            "be absent, so a headline inverted in the paper stops being "
            "locatable and the run refuses",
            not badpol and len(pol) == len(POLARITY),
            "%d polarity pairs, %d clean" % (len(pol), len(pol) - len(badpol)))

    heads, datarows, unbound, tbl_spec = build_paper_tables(S)
    hrows = []
    all_lines = [wsnorm(l) for l in text.split("\n")]
    for i, l in enumerate(all_lines):
        if l.startswith("|") and i + 1 < len(all_lines):
            nxt = all_lines[i + 1]
            if nxt.startswith("|") and set(
                    nxt.replace("|", "").replace(" ", "")) <= {"-", ":"}:
                hrows.append(l)
    want_h = sorted(wsnorm(h) for h in heads)
    LD.gate("G-PAPER-HEADERS-BOUND",
            "column headers are bound AS CLAIMS: every header row of every "
            "delivered table is rendered from the receipt keys its own "
            "columns are -- and that correspondence is CHECKED, every column "
            "name being required to be a key of every row object the table "
            "reports -- and the paper's header rows are compared as a "
            "multiset against that rendering, so two semantically opposed "
            "columns exchanged in the paper stop matching",
            sorted(hrows) == want_h and not unbound,
            "%d header rows in the paper, %d licensed over %d tables, equal "
            "as multisets %s; %d columns naming no receipt key %s"
            % (len(hrows), len(want_h), len(tbl_spec),
               sorted(hrows) == want_h, len(unbound), unbound[:3]))

    stripped = []
    for line in text.split("\n"):
        t = line
        if t.startswith("#"):
            parts = t.split(" ", 2)
            if len(parts) == 3 and parts[1].rstrip(".").isdigit():
                t = parts[0] + " " + parts[2]
        stripped.append(t)
    reg = receipt_number_registry(payload)
    uncovered = []
    for t in number_tokens("\n".join(stripped)):
        if t not in reg:
            uncovered.append(t)
    LD.gate("G-PAPER-NUMERALS-COVERED",
            "the numeral sweep covers EVERY numeral in the delivered text "
            "including the fenced verdict block, the inline code spans and "
            "both sides of every fraction, against a registry built from "
            "the receipt's own values -- section numbers alone are stripped "
            "from headings, and that stripping is declared here rather than "
            "silently applied.  This registry is a flat set of digit runs, "
            "so it has teeth at three digits and up and is published as "
            "having none below that: the short numerals are gated next, "
            "against a registry of a different kind",
            not uncovered,
            "%d numerals scanned, %d uncovered %s; %d registry tokens, %d of "
            "them three digits or longer"
            % (len(number_tokens("\n".join(stripped))), len(uncovered),
               sorted(set(uncovered))[:8], len(reg),
               sum(1 for t in reg if len(t) >= 3)))

    unfenced, infence = [], False
    for line in text.split("\n"):
        if line.strip().startswith("```"):
            infence = not infence
            continue
        if not infence:
            unfenced.append(line)
    spans, inspan, cur = [], False, []
    for ch in "\n".join(unfenced):
        if ch == "`":
            if inspan:
                spans.append("".join(cur))
                cur = []
            inspan = not inspan
            continue
        if inspan:
            cur.append(ch)
    licensed_spans = set()

    def addspan(o):
        if isinstance(o, dict):
            for k, v in o.items():
                licensed_spans.add(str(k))
                addspan(v)
        elif isinstance(o, list):
            for v in o:
                addspan(v)
        else:
            licensed_spans.add(str(o))
    addspan(payload)
    for rel in (PAPER_REL, OUT_REL, RECEIPT_REL,
                "v14/code/" + os.path.basename(os.path.abspath(__file__))):
        licensed_spans.add(rel)
    for f in FLAGS:
        licensed_spans.add(f)
    licensed_spans.add("--mutant")
    licensed_spans.add(DELIVERY_STATUS)
    for c in claims:
        licensed_spans.add(c["text"])
    for g in CLOSING_GATE_IDS + REFUSAL_ONLY_GATES:
        licensed_spans.add(g)
    if mut("MUT-PAPER-SPAN"):
        licensed_spans.discard(RECEIPT_REL)
    badspans = sorted({s for s in spans if s not in licensed_spans})
    LD.gate("G-PAPER-INLINE-SPANS-LICENSED",
            "every inline code span in the delivered text is required to be "
            "a string this run measured or declared -- a receipt key, a "
            "receipt value, a gate id, a mutant name, a declared path or a "
            "declared flag -- so a numeral cannot be smuggled into the paper "
            "inside a code span, and a span naming an object this run does "
            "not have stops the delivery run",
            not badspans,
            "%d inline spans, %d distinct, %d unlicensed %s"
            % (len(spans), len(set(spans)), len(badspans), badspans[:4]))

    ctx = set()
    for src in ([verdict] + [c["text"] for c in claims] + heads + datarows):
        for t in number_tokens(src):
            ctx.add(t)
    masked, fenced = [], False
    for line in text.split("\n"):
        if line.strip().startswith("```"):
            fenced = not fenced
            masked.append("")
            continue
        if fenced or line.strip().startswith("|"):
            masked.append("")
            continue
        out2, code, dollar, ref = [], False, False, False
        for ch in line:
            if ch == "`":
                code = not code
                continue
            if ch == "$":
                dollar = not dollar
                continue
            if code or dollar:
                continue
            if ch in ("#", "§", "-"):
                ref = True
                out2.append(" ")
                continue
            if ch.isdigit() and ref:
                continue
            ref = False
            out2.append(ch)
        masked.append("".join(out2))
    mtext = "\n".join(masked)
    short = [t for t in number_tokens(mtext) if len(t) <= 2]
    if mut("MUT-PAPER-SHORT-NUMERAL"):
        ctx.discard("24")
    shortbad = sorted({t for t in short if t not in ctx})
    LD.gate("G-PAPER-SHORT-NUMERALS-IN-CONTEXT",
            "the short numerals are gated against a registry of a different "
            "kind, because a flat registry of digit runs contains every one- "
            "and two-digit value and therefore backs nothing: a numeral of "
            "one or two digits in the paper's PROSE must be a token this run "
            "rendered IN CONTEXT -- inside a claim, a table row, a table "
            "header or the verdict string.  The declared exemptions are the "
            "fenced blocks, the table rows and the inline spans, each bound "
            "by its own gate, the mathematical spans between dollar signs, "
            "and the era references written with a hash or a section sign",
            not shortbad,
            "%d short numerals in prose after the declared exemptions, %d "
            "context tokens, %d unbacked %s"
            % (len(short), len(ctx), len(shortbad), shortbad[:8]))

    words = spelled_values(mnorm(mtext))
    if mut("MUT-PAPER-SPELLED"):
        words = words[:-1]
    spelled = sorted({v for v in words if str(v) not in ctx})
    LD.gate("G-PAPER-SPELLED-NUMERALS",
            "spelled numerals are read the way a reader reads them -- units, "
            "teens and tens compose, hundred and thousand scale -- and the "
            "RESOLVED VALUE is required to be a token this run rendered in "
            "context, so a count written in words cannot slip past the "
            "numeral gates and the scan is not confined to a declared list "
            "of words that happen to be backed",
            not spelled and len(words) == len(spelled_values(mnorm(mtext))),
            "%d spelled numbers read in the prose, %d distinct values, %d "
            "unbacked %s"
            % (len(words), len(set(words)), len(spelled), spelled))

    pairs = set()
    for src in ([verdict] + [c["text"] for c in claims] + heads + datarows):
        pairs |= value_pairs(src)
    wall_text = "\n".join("" if l.strip().startswith("|") else l
                          for l in text.split("\n"))
    wsents = sentences_of(wall_text)
    ctexts = [mnorm(c["text"]) for c in claims]
    declaring, unlicensed, policed = [], [], []
    for s in wsents:
        sl = s.lower()
        if not any(w in sl for w in CONFINEMENT_WORDS):
            continue
        policed.append(s)
        if any(m in sl for m in DECLARING_MARKERS):
            declaring.append(s)
            continue
        sn = mnorm(s)
        vp = value_pairs(s)
        carries = any(t and t in sn for t in ctexts) or bool(vp & pairs)
        if not carries or (vp - pairs):
            unlicensed.append(s[:90])
    if mut("MUT-LICENCE-WALL"):
        unlicensed = []
        declaring = []
    ok = ((not unlicensed) and len(declaring) >= 1
          and vbwin(vb, "VB-PIN-LICENCE", "G-THE-CONFINEMENT-LICENCE-WALL",
                    "carrying its measured discriminator value")
          and vbwin(vb, "VB-ACT-GATE", "G-THE-CONFINEMENT-LICENCE-WALL",
                    "REMAINS BEHIND POT'S GATE"))
    LD.gate("G-THE-CONFINEMENT-LICENCE-WALL",
            "the confinement vocabulary is licensed FOR THIS UNIT ONLY and "
            "only inside measured sentences, on the pin's own terms, which "
            "are read here from its window: a sentence of the delivered "
            "prose that uses one of the declared words must CARRY A "
            "MEASUREMENT -- a claim this run rendered, or a pair of values "
            "this run measured and joined as the sentence joins them -- and "
            "every value pair it states must be one this run measured, so a "
            "sentence built from the classifier's own words licenses "
            "nothing, and a sentence that pairs two separately measured "
            "numbers into a relation nothing measured dies here.  What this "
            "gate does NOT bind is the subject a licensed pair is attached "
            "to: a sentence carrying a pair this run measured, said about "
            "the wrong thing, is outside its reach and is published as "
            "outside it.  The table rows are excluded from this scan "
            "because they are bound, cell by cell, against the receipt's "
            "own row objects at their own gate",
            ok,
            "%d prose sentences scanned, %d carrying a declared word of %d, "
            "%d declaring the wall, %d licensed pairs, %d unlicensed %s"
            % (len(wsents), len(policed), len(CONFINEMENT_WORDS),
               len(declaring), len(pairs), len(unlicensed), unlicensed[:2]))

    sents = sentences_of(text)
    decl = list(MUST_NOT_DECLARERS)
    if mut("MUT-MUSTNOT"):
        decl = []
    keep = []
    for s in sents:
        if any(d in s for d in decl):
            continue
        keep.append(s)
    hits = []
    body = " ".join(keep)
    if mut("MUT-MUSTNOT-CONTENT"):
        body = body + " The lattice spacing goes to zero."
    for w in SI_UNITS:
        at = 0
        while True:
            at = body.find(w, at)
            if at < 0:
                break
            before = body[max(0, at - 6):at]
            if any(ch.isdigit() for ch in before):
                hits.append(w)
                break
            at += 1
    for w in CONTINUUM_PHRASES:
        if w in body:
            hits.append(w)
    declared_here = sum(1 for s in sents if any(d in s for d in decl))
    LD.gate("G-PAPER-MUST-NOT",
            "the pin's must-nots are swept over this paper's own text with "
            "the declaring sentences removed first, and every declaring "
            "sentence is required to be located here: no SI number and no "
            "continuum claim survives the sweep",
            not hits and declared_here >= 1,
            "%d forbidden tokens scanned over %d sentences, %d present %s, "
            "%d declaring sentences located"
            % (len(MUST_NOT), len(keep), len(hits), hits, declared_here))

    tbl_rows = []
    for i, l in enumerate(all_lines):
        if l.startswith("|") and l not in hrows and not (
                set(l.replace("|", "").replace(" ", "")) <= {"-", ":"}):
            tbl_rows.append(l)
    want_rows = sorted(wsnorm(r) for r in datarows)
    got_rows = sorted(tbl_rows)
    LD.gate("G-PAPER-TABLE-ROWS-COVERED",
            "every DATA row of every delivered table is bound the way its "
            "header is: the licensed row multiset is rendered from the "
            "receipt's own row objects, cell by cell, and the paper's data "
            "rows are compared against it as a multiset.  So a verdict word "
            "exchanged inside a cell, a row label swapped between two "
            "readings, a tally rewritten, and a whole row fabricated all "
            "stop the delivery run -- none of which a numeral-membership "
            "test can see",
            got_rows == want_rows,
            "%d data rows in the paper, %d licensed, equal as multisets %s; "
            "first difference %s"
            % (len(got_rows), len(want_rows), got_rows == want_rows,
               ([g for g in got_rows if g not in want_rows][:1]
                + [w for w in want_rows if w not in got_rows][:1])[:2]))

    quotes = [l for l in text.split("\n") if l.strip().startswith(">")]
    windows = [mnorm(t) for _n, _s, t, _f, _c in VERBATIM]
    if mut("MUT-PAPER-QUOTES"):
        windows = windows[1:]
    outside = []
    for q in quotes:
        qq = mnorm(q)
        if qq and not any(qq in w or w in qq for w in windows):
            outside.append(qq[:60])
    LD.gate("G-PAPER-QUOTES-INSIDE-THE-WINDOWS",
            "every quotation the paper makes of a parent is required to lie "
            "INSIDE one of the pinned verbatim windows, so a paper that "
            "misquotes -- or inverts -- a definition it attributes to a "
            "parent dies on the delivery run",
            not outside,
            "%d quoted lines, %d outside every pinned window %s"
            % (len(quotes), len(outside), outside[:2]))

    S["paper_binding"] = {
        "claims": claims, "polarity": pol,
        "claim_occurrences": sum(c["hits"] for c in claims),
        "header_rows": len(hrows), "licensed_headers": len(want_h),
        "tables_bound": len(tbl_spec),
        "numerals_scanned": len(number_tokens("\n".join(stripped))),
        "numerals_uncovered": len(uncovered),
        "registry_tokens": len(reg),
        "registry_tokens_of_three_digits_or_more":
            sum(1 for t in reg if len(t) >= 3),
        "short_numerals_in_prose": len(short),
        "context_registry_tokens": len(ctx),
        "short_numerals_unbacked": len(shortbad),
        "inline_spans": len(spans),
        "inline_spans_unlicensed": len(badspans),
        "spelled_numbers_read": len(words),
        "spelled_numbers_unbacked": len(spelled),
        "sentences": len(sents),
        "wall_sentences": len(wsents),
        "the_declared_words": len(CONFINEMENT_WORDS),
        "confinement_sentences": len(policed),
        "wall_declaring_sentences": len(declaring),
        "licensed_value_pairs": len(pairs),
        "unlicensed_confinement_sentences": len(unlicensed),
        "must_not_tokens": len(MUST_NOT), "must_not_hits": len(hits),
        "table_data_rows": len(tbl_rows), "licensed_table_rows":
            len(want_rows),
        "table_rows_bound_as_a_multiset": got_rows == want_rows,
        "quoted_lines": len(quotes), "quotes_outside_windows": len(outside),
        "fenced_blocks": len(got)}
    SEAL.take("THE PAPER BINDING", "paper_binding",
              "G-PAPER-QUOTES-INSIDE-THE-WINDOWS", S["paper_binding"])


# ===========================================================================
# SECTION 19.  TOTALS, COVERAGE, THE SEAL AND THE DISK BOUNDARY
# ===========================================================================

CLOSING_GATE_IDS = ["G-THE-SEAL-IS-TOTAL", "G-ARTIFACT-INTEGRITY"]
LATE_GATE_IDS = ["G-COVERAGE-AT-AN-HONEST-DENOMINATOR",
                 "G-THE-RECEIPT-HEADER-IS-BOUND",
                 "G-THE-TRANSCRIPT-RECONCILES"]
REFUSAL_ONLY_GATES = ["G-THE-LOOP-FAMILY-IS-A-FAMILY-OF-LOOPS-STEP-CHECK"]

DELIVERY_STATUS = "DELIVERED"

EXIT_CONVENTIONS = {
    "delivery": "0 on success, 1 on any refusal, writing nothing",
    "selftest": "0 when every anchor class is fatal and nothing is written",
    "mutant": "0 when the named mutant DIES on its declared target with the "
              "artifacts unchanged",
    "unknown_flag": "2"}

FORCINGS = {
    "G-THE-SEAL-IS-TOTAL":
        "closes over the manifest the ledger snapshot is taken from, so it "
        "cannot be inside the ledger it closes",
    "G-ARTIFACT-INTEGRITY":
        "closes at the disk boundary after the ledger is serialized",
    "G-THE-LEDGER-CHAIN-VERIFIES":
        "verifies the chain the other gates wrote, and a falsifier for it "
        "is MUT-LEDGER-CHAIN, which edits a row after its gate closed",
}


def measure_totals(S, verdict, second):
    ok = verdict == second
    LD.gate("G-THE-TWO-HEAD-LAWS-AGREE",
            "the complete verdict string -- head included -- is compared for "
            "equality against an INDEPENDENT reconstruction that reads only "
            "the serialized receipt, derives the head by a second head law "
            "of its own over the tallies rather than the rows, and "
            "re-renders every segment with its own format strings, sharing "
            "no helper with the builder",
            ok,
            "the builder's string and the comparator's string agree: %s "
            "(%d characters)" % (ok, len(verdict)))
    SEAL.take("THE VERDICT", "verdict", "G-THE-TWO-HEAD-LAWS-AGREE", verdict)
    chain = LD.verify_chain()
    rows = [dict(r) for r in LD.rows]
    if mut("MUT-LEDGER-CHAIN"):
        rows[1]["detail"] = rows[1]["detail"] + " "
        chain = LD.verify_chain(rows)
    LD.gate("G-THE-LEDGER-CHAIN-VERIFIES",
            "the gate ledger is chained row by row and the chain is "
            "VERIFIED rather than published beside an unperformed claim, so "
            "a row edited after its gate closed no longer matches the digest "
            "of its own predecessor",
            chain,
            "%d ledger rows, chain verifies %s" % (len(rows), chain))
    S["totals"] = {
        "gates_closed": len(LD.ids),
        "gates_failed": 0,
        "closing_gates": len(CLOSING_GATE_IDS),
        "mutants_declared": len(MUTANTS),
        "sources": len(SOURCES),
        "path_value_anchors": len(PATH_VALUES),
        "verbatim_anchors": len(VERBATIM),
        "anchors": len(SOURCES) + len(PATH_VALUES) + len(VERBATIM),
        "sealed_objects": len(SEAL.rows),
        "the_two_head_laws_agree": ok,
        "the_ledger_chain_verifies": chain,
        "verdict_characters": len(verdict)}


def measure_coverage(S):
    """the coverage gate closes AT THE END OF THE DELIVERY PATH, not before
    the paper leg: K3's MAJOR-8 at this unit measured the old denominator at
    38 of the 50 gates the delivery run actually closes, which is exactly
    the shape #34 forbids.  The denominator here is every gate this run
    closes, the ones after this one named explicitly."""
    targets = {m[1] for m in MUTANTS}
    clean = list(LD.ids) + list(LATE_GATE_IDS) + list(CLOSING_GATE_IDS)
    if mut("MUT-COVERAGE"):
        clean = clean + ["G-A-GATE-WITH-NEITHER-A-FALSIFIER-NOR-A-FORCING"]
    uncovered = [g for g in clean
                 if g not in targets and g not in FORCINGS]
    dupes = sorted({g for g in clean if clean.count(g) > 1})
    LD.gate("G-COVERAGE-AT-AN-HONEST-DENOMINATOR",
            "the falsifier coverage is published at an honest denominator "
            "(#34): the denominator is EVERY gate the delivery run closes, "
            "this gate and the ones after it included and named one by one, "
            "and each is either a declared falsifier's target or carries a "
            "registered forcing -- so the denominator cannot be made "
            "flattering by taking it early",
            not uncovered and not dupes,
            "%d gates on the clean path, %d of them closing at or after this "
            "one %s, %d falsifier targets, %d registered forcings, %d "
            "uncovered %s"
            % (len(clean), len(LATE_GATE_IDS) + len(CLOSING_GATE_IDS),
               LATE_GATE_IDS + CLOSING_GATE_IDS, len(targets), len(FORCINGS),
               len(uncovered), uncovered[:4]))
    S["waiver_ledger"] = {"registered_forcings": FORCINGS,
                          "refusal_only_gates": REFUSAL_ONLY_GATES}
    S["coverage"] = {"clean_path_gates": clean,
                     "gates_closing_at_or_after_this_one":
                         LATE_GATE_IDS + CLOSING_GATE_IDS,
                     "falsifier_targets": sorted(targets),
                     "uncovered": uncovered}
    S["totals"]["gates_on_the_clean_path"] = len(clean)
    SEAL.take("THE COVERAGE", "coverage",
              "G-COVERAGE-AT-AN-HONEST-DENOMINATOR", S["coverage"])
    SEAL.take("THE WAIVER LEDGER", "waiver_ledger",
              "G-COVERAGE-AT-AN-HONEST-DENOMINATOR", S["waiver_ledger"])
    SEAL.take("THE TOTALS", "totals",
              "G-COVERAGE-AT-AN-HONEST-DENOMINATOR", S["totals"])


def measure_the_receipt_header(S, payload):
    """the receipt's own header keys -- the digests it publishes of itself,
    of the paper and of the pin, and the exit conventions -- are VOUCHED and
    then sealed, so the forgeable half of the declared-unsealed manifest
    shrinks to the objects that genuinely cannot be sealed in order."""
    code = bdigest(open(os.path.abspath(__file__), "rb").read())
    pb = read_bytes(PAPER_REL)
    paper = bdigest(pb) if pb else "ABSENT"
    pin = [r["expected"] for r in payload["provenance"]
           if r["path"] == "v14/note-pot-pin.md"][0]
    if mut("MUT-RECEIPT-HEADER"):
        paper = "0" * 12
    ok = (payload["code_sha256_12"] == code
          and payload["paper_sha256_12"] == paper
          and payload["pin_sha256_prefix"] == pin
          and payload["exit_conventions"] == EXIT_CONVENTIONS
          and payload["preregistered_heads"] == PREREGISTERED
          and payload["verdict_head"] == S["_head_word"]
          and payload["schema"] == "POT-V1" and payload["unit"] ==
          "POT-PAPER-36")
    LD.gate("G-THE-RECEIPT-HEADER-IS-BOUND",
            "the receipt's header keys are VOUCHED rather than declared "
            "unsealable: the instrument's own digest and the paper's are "
            "recomputed here from the bytes, the pin's prefix is required to "
            "be the one the provenance row verified, and the exit "
            "conventions, the pre-registered head list, the derived head "
            "word and the schema are required to be the objects this run "
            "carries -- and all of them are then sealed",
            ok,
            "code %s, paper %s, pin %s, exit conventions and head list bound "
            "%s" % (code, paper, pin, ok))
    for key in ("schema", "unit", "code_sha256_12",
                "paper_sha256_12", "pin_sha256_prefix", "exit_conventions",
                "preregistered_heads"):
        SEAL.take("THE RECEIPT HEADER :: " + key, key,
                  "G-THE-RECEIPT-HEADER-IS-BOUND", payload[key])


def measure_the_transcript(S, payload):
    """K3's MAJOR-7 at this unit: nothing bound the transcript to the run,
    so a fabricated PASS line for a gate that never existed was delivered at
    exit 0.  The transcript's PASS lines are reconciled here against THIS
    run's own ledger, in order and as a sequence, and the head is sealed."""
    seen = []
    for line in LOG:
        t = line.strip()
        if t.startswith("[PASS] ") or t.startswith("[FAIL] "):
            seen.append(t[7:].split(" :: ")[0])
    if mut("MUT-TRANSCRIPT"):
        seen = seen + ["G-A-GATE-THAT-NEVER-RAN"]
    ok = seen == list(LD.ids)
    LD.gate("G-THE-TRANSCRIPT-RECONCILES",
            "the delivered transcript is bound to the run: the gate ids its "
            "PASS lines carry are required to equal this run's own ledger "
            "ids AS A SEQUENCE, so a line fabricated into the transcript -- "
            "for a gate that never ran, or for one that ran elsewhere -- "
            "stops the delivery run instead of being published",
            ok,
            "%d transcript gate lines against %d ledger rows, equal as a "
            "sequence %s%s"
            % (len(seen), len(LD.ids), ok,
               "" if ok else "; first difference %s"
               % [a for a, b in zip(seen + [""], list(LD.ids) + [""])
                  if a != b][:1]))
    S["transcript"] = {"gate_lines_reconciled": len(seen),
                       "reconciles_against_the_ledger": ok,
                       "head": LOG[0],
                       "the_binding": "THE-PASS-LINES-ARE-THE-LEDGER-IDS-IN-"
                                      "ORDER-AND-THE-WHOLE-FILE-IS-COMPARED-"
                                      "BYTE-FOR-BYTE-AT-THE-DISK-BOUNDARY"}
    SEAL.take("THE TRANSCRIPT", "transcript", "G-THE-TRANSCRIPT-RECONCILES",
              S["transcript"])


DECLARED_UNSEALED = {
    "gates": "the ledger rows themselves; sealing them would seal the "
             "object that records the seal -- and they are compared against "
             "this run's own ledger from the read-back bytes at "
             "G-ARTIFACT-INTEGRITY",
    "gate_digests": "derived from the ledger after the snapshot; recomputed "
                    "from the read-back rows at G-ARTIFACT-INTEGRITY",
    "ledger_shape": "derived from the ledger after the snapshot; compared "
                    "against this run's own chain head from the read-back "
                    "bytes at G-ARTIFACT-INTEGRITY",
    "seal_manifest": "the manifest cannot seal itself; it is compared "
                     "against this run's own manifest object from the "
                     "read-back bytes at G-ARTIFACT-INTEGRITY",
    "declared_unsealed": "this declaration; compared against the "
                         "instrument's own registry from the read-back "
                         "bytes at G-ARTIFACT-INTEGRITY",
    "python": "the interpreter's own version string; compared against this "
              "run's own interpreter at G-ARTIFACT-INTEGRITY",
}

POST_SNAPSHOT_KEYS = ["gates", "gate_digests", "ledger_shape",
                      "seal_manifest", "declared_unsealed", "python"]


def write_out(S, verdict, payload, write):
    snapshot = [dict(r) for r in LD.rows]
    declared = sorted(DECLARED_UNSEALED)
    if mut("MUT-SEAL"):
        declared = declared[:-1]
    sealed_keys = {r["receipt_key"].split("/")[0] for r in SEAL.rows}
    top = sorted(payload)
    unaccounted = [k for k in top
                   if k not in sealed_keys and k not in declared]
    bad = SEAL.reverify(payload)
    LD.gate("G-THE-SEAL-IS-TOTAL",
            "the manifest is TOTAL: every top-level key of the receipt is "
            "either sealed at the gate that vouched its own values or named "
            "in the declaration with the reason it cannot be, every sealed "
            "object is re-verified against its gate-time digest before "
            "anything is written, and the declared-unsealed half is now only "
            "the keys with a genuine ordering impossibility -- each of "
            "which is compared against the object this run built it from, "
            "from the READ-BACK bytes, at the disk boundary",
            not unaccounted and not bad,
            "%d top-level keys, %d sealed, %d declared unsealed, %d "
            "unaccounted %s, %d digest mismatches"
            % (len(top), len(sealed_keys), len(declared), len(unaccounted),
               unaccounted[:4], len(bad)))
    out_text = "\n".join(LOG) + "\n"
    rec_text = json.dumps(payload, indent=1, sort_keys=True,
                          default=str) + "\n"
    if not write:
        return out_text, rec_text
    tmp_o = os.path.join(REPO, OUT_REL + ".tmp")
    tmp_r = os.path.join(REPO, RECEIPT_REL + ".tmp")
    moved = False
    try:
        with open(tmp_o, "wb") as fh:
            fh.write(out_text.encode())
        with open(tmp_r, "wb") as fh:
            fh.write(rec_text.encode())
        back_o = open(tmp_o, "rb").read().decode()
        back_r = open(tmp_r, "rb").read().decode()
        same = (back_o == out_text and back_r == rec_text)
        reread = json.loads(back_r)
        bad2 = SEAL.reverify(reread)
        keys_ok = sorted(reread) == top
        chain_ok = LD.verify_chain(reread["gates"])
        post = {"gates": snapshot,
                "gate_digests": {r["gate"]: r["link"] for r in snapshot},
                "ledger_shape": {"rows": len(snapshot),
                                 "head": snapshot[-1]["link"]},
                "seal_manifest": SEAL.rows,
                "declared_unsealed": DECLARED_UNSEALED,
                "python": "%d.%d" % (sys.version_info[0],
                                     sys.version_info[1])}
        post_bad = [k for k in POST_SNAPSHOT_KEYS if reread[k] != post[k]]
        lines = []
        for line in back_o.split("\n"):
            t = line.strip()
            if t.startswith("[PASS] ") or t.startswith("[FAIL] "):
                lines.append(t[7:].split(" :: ")[0])
        trans_ok = lines == list(LD.ids)
        ok = (same and not bad2 and keys_ok and chain_ok and not post_bad
              and trans_ok)
        LD.gate("G-ARTIFACT-INTEGRITY",
                "the artifacts are written to temporaries, READ BACK and "
                "compared against the gate-time digests before either is "
                "moved into place -- the receipt by total byte equality as "
                "well as by its seals, and every declared-unsealed key by "
                "EQUALITY AGAINST THE OBJECT THIS RUN BUILT IT FROM, so a "
                "value forged into the ledger, the manifest, the digests or "
                "the declaration after the seal no longer verifies; the "
                "transcript's own gate lines are reconciled again from the "
                "bytes on disk; and a refusing integrity gate promotes "
                "nothing and leaves no staging file behind",
                ok,
                "byte equality %s; %d seal mismatches from disk; top-level "
                "keys identical %s; the ledger chain verifies from disk %s; "
                "%d declared-unsealed keys re-verified, %d forged %s; the "
                "transcript reconciles from disk %s"
                % (same, len(bad2), keys_ok, chain_ok,
                   len(POST_SNAPSHOT_KEYS), len(post_bad), post_bad,
                   trans_ok))
        os.replace(tmp_o, os.path.join(REPO, OUT_REL))
        os.replace(tmp_r, os.path.join(REPO, RECEIPT_REL))
        moved = True
    finally:
        if not moved:
            for p in (tmp_o, tmp_r):
                if os.path.exists(p):
                    os.remove(p)
    return out_text, rec_text


# ===========================================================================
# SECTION 20.  THE RUN
# ===========================================================================

def run(write=True, paper_gates=True):
    S = {}
    del VB_READS[:]
    say("POT (paper-36) :: the potential unit -- the loop family, the "
        "discriminator, the price binding and the spectral door")
    say("=" * 78)
    src, prov = load_sources()
    S["provenance"] = prov
    pv = measure_path_values(S, src)
    vb = measure_verbatim(S, src)
    scan_syntax_tree(S)
    say("-- the arena --")
    build_arena(S, pv, vb)
    say("-- the loop family, the object ACT recorded still absent --")
    ok_missing = (pv["PV-ACT-LOOPFAM"] == 0
                  and vbwin(vb, "VB-R5-NEEDS",
                            "G-THE-LOOP-FAMILY-IS-THE-MISSING-OBJECT",
                            "loops whose size can grow")
                  and vbwin(vb, "VB-ACT-ABSENT",
                            "G-THE-LOOP-FAMILY-IS-THE-MISSING-OBJECT",
                            "still absent"))
    if mut("MUT-LOOPFAM-FIELD"):
        ok_missing = False
    LD.gate("G-THE-LOOP-FAMILY-IS-THE-MISSING-OBJECT",
            "the parent's own receipt records ZERO loop families grown, and "
            "its paper names the family of loops whose size can grow as the "
            "gate on everything beyond; this unit reads that field at its "
            "named path, reads both windows that record the gap, and builds "
            "the object rather than quoting it",
            ok_missing,
            "the parent grew %d loop families; this unit builds the family "
            "and gates it" % pv["PV-ACT-LOOPFAM"])
    measure_loop_family(S, pv, vb)
    say("-- the classes and the extreme points --")
    measure_classes(S, pv, vb)
    say("-- the loop observable on the carrier --")
    measure_the_loop_observable(S, pv, vb)
    say("-- the scope of the perimeter reading, at the family's own lengths --")
    measure_the_length_reading(S, pv)
    say("-- the discriminator, defined and gated before any row runs --")
    measure_the_discriminator(S, pv, vb)
    say("-- the ladder's exact closed form --")
    measure_the_closed_form(S, pv)
    say("-- the area-blindness universal, over every measure on the carrier --")
    measure_the_universal_over_measures(S, pv)
    say("-- mode (a): the declared rows --")
    measure_declared_rows(S, pv, vb)
    say("-- mode (b): the family sweep --")
    measure_family_sweep(S, pv)
    measure_the_constant_ladder_identity(S, pv)
    measure_family_slices(S, pv)
    say("-- the price binding --")
    measure_the_price_binding(S, pv, vb)
    say("-- the order parameter's range --")
    measure_the_order_parameter_range(S, pv)
    say("-- the spectral door --")
    measure_the_spectral_door(S, pv)
    say("-- the orientation reading, declared and priced --")
    measure_the_orientation_reading(S, pv)
    say("-- the L-boundary, run --")
    measure_the_boundary_lattice(S, pv)
    say("-- the control arms --")
    measure_the_control_arms(S, pv)
    say("-- the verdict --")
    measure_the_verdict(S, pv)

    payload = {k: v for k, v in S.items() if not k.startswith("_")}
    payload["schema"] = "POT-V1"
    payload["unit"] = "POT-PAPER-36"
    payload["python"] = "%d.%d" % (sys.version_info[0], sys.version_info[1])
    payload["pin_sha256_prefix"] = "df2f15efa7b0"
    payload["code_sha256_12"] = bdigest(
        open(os.path.abspath(__file__), "rb").read())
    pb = read_bytes(PAPER_REL)
    payload["paper_sha256_12"] = bdigest(pb) if pb else "ABSENT"
    payload["preregistered_heads"] = PREREGISTERED
    payload["verdict_head"] = S["_head_word"]
    payload["exit_conventions"] = EXIT_CONVENTIONS
    verdict = render_verdict(S)
    payload["verdict"] = verdict
    payload["gates"] = [dict(r) for r in LD.rows]
    payload["gate_digests"] = {r["gate"]: r["link"] for r in LD.rows}
    payload["ledger_shape"] = {"rows": len(LD.rows), "head": LD.chain}
    payload["seal_manifest"] = SEAL.rows
    payload["declared_unsealed"] = DECLARED_UNSEALED
    second = rerender_verdict(payload)
    measure_totals(S, verdict, second)
    if paper_gates:
        say("-- the paper gates --")
        payload["totals"] = S["totals"]
        measure_paper(S, payload, verdict, vb)
        measure_consumers(S)
        payload["paper_binding"] = S["paper_binding"]
        payload["consumer_register"] = S["consumer_register"]
    measure_coverage(S)
    measure_the_receipt_header(S, payload)
    measure_the_transcript(S, payload)
    payload["transcript"] = S["transcript"]
    payload["totals"] = S["totals"]
    payload["coverage"] = S["coverage"]
    payload["waiver_ledger"] = S["waiver_ledger"]
    payload["gates"] = [dict(r) for r in LD.rows]
    payload["gate_digests"] = {r["gate"]: r["link"] for r in LD.rows}
    payload["ledger_shape"] = {"rows": len(LD.rows), "head": LD.chain}
    payload["seal_manifest"] = SEAL.rows
    say("")
    say("THE VERDICT")
    say(verdict)
    say("")
    write_out(S, verdict, payload, write)
    say("POT :: %d gates closed, %d anchors, %d sealed objects, %d declared "
        "mutants" % (len(LD.ids), S["totals"]["anchors"], len(SEAL.rows),
                     len(MUTANTS)))
    return payload


ANCHOR_CLASSES = [("FILE-BYTES", "G-SOURCES-AT-THEIR-PINNED-DIGESTS"),
                  ("PATH-VALUE", "G-PATH-VALUE-ANCHORS"),
                  ("VERBATIM-TEXT", "G-VERBATIM-ANCHORS")]


def tree_state():
    """the artifact DIRECTORY, not only the two artifact paths: 'a refusing
    run writes nothing' is checked against the listing as well as the bytes,
    so a staging temporary left behind by a refusal is a failure rather than
    an invisible."""
    d = os.path.dirname(os.path.join(REPO, OUT_REL))
    arte = {}
    for rel in (OUT_REL, RECEIPT_REL):
        p = os.path.join(REPO, rel)
        arte[rel] = (bdigest(open(p, "rb").read())
                     if os.path.exists(p) else None)
    return {"names": sorted(os.listdir(d)), "artifacts": arte}


def selftest():
    """the falsification self-test: one anchor class is corrupted IN MEMORY
    at a time, the run is required to die AT THAT CLASS'S OWN GATE, and the
    corruption is restored before the next class so that no class is tested
    through the wreckage of another."""
    before = tree_state()
    keep_s, keep_p, keep_v = list(SOURCES), list(PATH_VALUES), list(VERBATIM)
    results = []
    for cls, target in ANCHOR_CLASSES:
        globals()["LD"] = Ledger()
        globals()["SEAL"] = Seal()
        globals()["LOG"] = []
        globals()["QUIET"] = True
        globals()["SOURCES"] = list(keep_s)
        globals()["PATH_VALUES"] = list(keep_p)
        globals()["VERBATIM"] = list(keep_v)
        if cls == "FILE-BYTES":
            globals()["SOURCES"] = [(n, p, "0" * 12, w) if n == "S-ACT-PAPER"
                                    else (n, p, s, w)
                                    for n, p, s, w in keep_s]
        elif cls == "PATH-VALUE":
            globals()["PATH_VALUES"] = [
                (n, s, p, 0, c) if n == "PV-ACT-COINS" else (n, s, p, e, c)
                for n, s, p, e, c in keep_p]
        else:
            globals()["VERBATIM"] = [
                (n, s, "a sentence no parent of this unit contains anywhere "
                 "at all", f, c) if n == "VB-R5-BLOCK" else (n, s, t, f, c)
                for n, s, t, f, c in keep_v]
        died = None
        try:
            run(write=False, paper_gates=False)
        except GateFail as e:
            died = str(e).split(" :: ")[0]
        except Exception as e:                       # noqa: BLE001
            died = "EXCEPTION:%s" % type(e).__name__
        results.append((cls, target, died))
    globals()["SOURCES"] = keep_s
    globals()["PATH_VALUES"] = keep_p
    globals()["VERBATIM"] = keep_v
    globals()["QUIET"] = False
    unchanged = tree_state() == before
    ontarget = all(d == t for _c, t, d in results)
    for cls, target, died in results:
        print("SELFTEST %-14s target %-34s -> %s" % (cls, target, died))
    print("SELFTEST :: %d of %d anchor classes fatal at their own gate :: "
          "the artifact directory is unchanged %s"
          % (sum(1 for _c, t, d in results if d == t), len(results),
             unchanged))
    return 0 if (ontarget and unchanged) else 1


USAGE = """usage: pot_exact.py [--no-write] [--selftest] [--mutant NAME]
                    [--all-mutants] [--list-gates] [--list-mutants]
                    [--verify-paper] [--quiet] [--help]

exit conventions (they invert the usual reading and are therefore stated):
  delivery       0 on success, 1 on any refusal, writing nothing
  --selftest     0 when EVERY anchor class is fatal and nothing is written
  --mutant NAME  0 when the named mutant DIES at its declared target
  unknown flag   2

flag precedence, declared rather than left to the reading order: --help,
then --list-gates, --list-mutants, --selftest, --mutant, --all-mutants,
--verify-paper, then the delivery run.  The first of those present wins and
the rest are inert, so --verify-paper --mutant NAME runs the mutant and
--selftest --no-write runs the self-test, which writes nothing anyway.
"""

FLAGS = {"--no-write": "no-write", "--selftest": "selftest",
         "--all-mutants": "all-mutants", "--list-gates": "list-gates",
         "--list-mutants": "list-mutants", "--verify-paper": "verify-paper",
         "--quiet": "quiet", "--help": "help"}


def main(argv):
    global QUIET, MUT
    args = {}
    i = 1
    while i < len(argv):
        a = argv[i]
        if a in FLAGS:
            args[FLAGS[a]] = True
        elif a == "--mutant":
            if i + 1 >= len(argv):
                sys.stderr.write("--mutant needs a NAME\n%s" % USAGE)
                return 2
            args["mutant"] = argv[i + 1]
            i += 1
        else:
            sys.stderr.write("unknown flag %r\n%s" % (a, USAGE))
            return 2
        i += 1
    if args.get("help"):
        sys.stdout.write(USAGE)
        return 0
    QUIET = bool(args.get("quiet"))
    if args.get("list-gates"):
        globals()["QUIET"] = True
        try:
            run(write=False, paper_gates=True)
        except GateFail as e:
            sys.stderr.write("REFUSED :: %s\n" % e)
            return 1
        for g in LD.ids:
            print(g)
        for g in CLOSING_GATE_IDS:
            if g not in LD.ids:
                print("%s   (closes after the ledger snapshot)" % g)
        for g in REFUSAL_ONLY_GATES:
            print("%s   (refusal only; closes on no clean path)" % g)
        return 0
    if args.get("list-mutants"):
        for nm, tg, wh, _t in MUTANTS:
            print("%-28s -> %-52s %s" % (nm, tg, wh))
        return 0
    if args.get("selftest"):
        return selftest()
    if args.get("mutant"):
        name = args["mutant"]
        if name not in {m[0] for m in MUTANTS}:
            sys.stderr.write("unknown mutant %r\n" % name)
            return 2
        target = [m[1] for m in MUTANTS if m[0] == name][0]
        before = tree_state()
        MUT = name
        died = None
        try:
            run(write=False, paper_gates=True)
        except GateFail as e:
            died = str(e).split(" :: ")[0]
        except Exception as e:                       # noqa: BLE001
            died = "EXCEPTION:%s" % type(e).__name__
        MUT = None
        unchanged = tree_state() == before
        ok = (died == target) and unchanged
        print("MUTANT %-28s target %-52s died at %s :: the artifact "
              "directory is unchanged %s :: %s" % (name, target, died,
                                                   unchanged,
                            "DEAD-ON-TARGET" if ok else "FAILED"))
        return 0 if ok else 1
    if args.get("all-mutants"):
        bad = []
        for nm, tg, _w, _t in MUTANTS:
            globals()["LD"] = Ledger()
            globals()["SEAL"] = Seal()
            globals()["LOG"] = []
            globals()["MUT"] = nm
            globals()["QUIET"] = True
            died = None
            try:
                run(write=False, paper_gates=True)
            except GateFail as e:
                died = str(e).split(" :: ")[0]
            except Exception as e:                   # noqa: BLE001
                died = "EXCEPTION:%s" % type(e).__name__
            globals()["MUT"] = None
            globals()["QUIET"] = False
            if died != tg:
                bad.append((nm, died))
            print("%-28s %s" % (nm, "DEAD-ON-TARGET" if died == tg
                                else "FAILED (died at %s)" % died))
        print("ALL-MUTANTS :: %d of %d dead on target"
              % (len(MUTANTS) - len(bad), len(MUTANTS)))
        return 0 if not bad else 1
    if args.get("verify-paper"):
        try:
            run(write=False, paper_gates=True)
        except GateFail as e:
            sys.stderr.write("REFUSED :: %s\n" % e)
            return 1
        return 0
    try:
        run(write=not args.get("no-write"), paper_gates=True)
    except GateFail as e:
        sys.stderr.write("REFUSED :: %s\n" % e)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
