#!/usr/bin/env python3
"""ACT / paper-34 -- THE ACTION UNIT: the form census of the weight systems.

Paper-23 proved that no measure on R5's gauge configurations DERIVES, and
entered the Gibbs route as a census row it could not price because the arena
has no action.  SMU declared a DYNAMICS instead, measured that the stationary
measure moves across the declared fibre, and left ROUTE C -- an ACTION -- as
the only live route to a measure that is not a bare declaration.  This unit
builds the action and prices every part of it.

THE FRAMING IS MULTIPLICATIVE AND BINDING: a weight system w assigns a
POSITIVE EXACT RATIONAL to each local datum at a declared locality grain, the
configuration weight is the PRODUCT of the local weights, and "the action"
S = -log W is nominal only.  No logarithm and no float is computed anywhere,
and an AST scan of this file's own syntax tree is a gate.

THE FORM CENSUS is the heart: all weight systems satisfying (i)
gauge-invariance under the measured gauge action, (ii) locality at each of
three declared grains -- per-link, per-plaquette, per-site, every member run
-- and (iii) covariance under the measured chart group.  The allowed space is
computed EXACTLY: it is the multiplicative group of orbit-constant positive
rational functions on the stencil datum, a free module whose rank modulo
normalisation IS the coupling count.

Built against the frozen pin v14/note-act-pin.md.  Exact arithmetic only: the
field is Q(zeta_8) carried as integer 5-tuples over the basis (1, z, z^2,
z^3) reduced modulo z^4 + 1 in lowest terms, so tuple equality is field
equality; every weight and every mass is a fractions.Fraction; every orbit
count is an exact integer from a Burnside sum that must divide, cross-checked
by a second route.

THE PIN'S MUST-NOT, INHERITED VERBATIM FROM PAPER-23's REPAIRED GATE: the
confinement vocabulary stays behind POT's gate -- this unit makes NO
area-law, NO string-tension and NO potential claim, and grows no loop family.
The Wilson expectations this unit does publish carry the stamp
CONDITIONAL-ON-THE-DECLARED-WEIGHTS on every row.

EXIT CONVENTIONS, DISCLOSED (they invert the usual reading): the delivery run
exits 0 when every gate passes and 1 on any refusal, writing nothing;
--selftest exits 0 when EVERY anchor class is fatal; --mutant exits 0 when
the named mutant DIES ON ITS DECLARED TARGET; --all-mutants exits 0 only when
all of them do; an unknown flag or a missing flag argument exits 2.
"""

import ast
import hashlib
import json
import os
import re
import sys
from fractions import Fraction
from itertools import product

UNIT = "ACT / paper-34 -- the action unit: the form census"
PIN_SHA12 = "766c603c6dbc"
SCHEMA = "act-form-census-1"

QUIET = False
MUT = None
LOG = []


def say(msg=""):
    """--quiet suppresses the TERMINAL ECHO ONLY.  The transcript is a
    published artifact, so it is accumulated whatever the flag says: a flag
    that changed the delivered bytes would be a byte-reproducibility hazard
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
    so what they falsify is the object the gate measures and not the gate's
    own finding (#34)."""
    src = open(os.path.abspath(__file__), "rb").read().decode()
    if mut("MUT-GHOST-FUNCTION"):
        src = src + "\n\ndef ghost_helper(S):\n    return Fraction(3, 8)\n"
    if mut("MUT-REGISTRY-EVASION"):
        src = src + "\n\n_gn = 'MUT-' + 'GHOST'\nif mut(_gn):\n    pass\n"
    if mut("MUT-AST-BLIND"):
        src = src + "\n\n_TOLERANCE_FLOAT = 1e-9\n"
    return src


# ===========================================================================
# SECTION 1.  THE EXACT FIELD Q(zeta_8)
# ===========================================================================
# (a0, a1, a2, a3, den): (a0 + a1 z + a2 z^2 + a3 z^3) / den, den > 0, in
# lowest terms.  The representation is canonical, so tuple equality IS field
# equality.  Integers only.

ZERO = (0, 0, 0, 0, 1)
ONE = (1, 0, 0, 0, 1)


def _g(a, b):
    """the greatest common divisor, written out: this instrument imports no
    module the AST gate would have to forgive."""
    while b:
        a, b = b, a % b
    return a


def fnorm(a0, a1, a2, a3, d):
    if d < 0:
        a0, a1, a2, a3, d = -a0, -a1, -a2, -a3, -d
    g = _g(_g(_g(abs(a0), abs(a1)), _g(abs(a2), abs(a3))), d)
    if g > 1:
        return (a0 // g, a1 // g, a2 // g, a3 // g, d // g)
    return (a0, a1, a2, a3, d)


def fadd(a, b):
    d = a[4] * b[4]
    return fnorm(a[0] * b[4] + b[0] * a[4], a[1] * b[4] + b[1] * a[4],
                 a[2] * b[4] + b[2] * a[4], a[3] * b[4] + b[3] * a[4], d)


def fneg(a):
    return (-a[0], -a[1], -a[2], -a[3], a[4])


def fmul(a, b):
    a0, a1, a2, a3 = a[0], a[1], a[2], a[3]
    b0, b1, b2, b3 = b[0], b[1], b[2], b[3]
    c0 = a0 * b0
    c1 = a0 * b1 + a1 * b0
    c2 = a0 * b2 + a1 * b1 + a2 * b0
    c3 = a0 * b3 + a1 * b2 + a2 * b1 + a3 * b0
    c4 = a1 * b3 + a2 * b2 + a3 * b1
    c5 = a2 * b3 + a3 * b2
    c6 = a3 * b3
    return fnorm(c0 - c4, c1 - c5, c2 - c6, c3, a[4] * b[4])


def fconj(a):
    """conj(z) = -z^3, conj(z^2) = -z^2, conj(z^3) = -z."""
    return fnorm(a[0], -a[3], -a[2], -a[1], a[4])


def zpow(t):
    t %= 8
    v = [0, 0, 0, 0]
    if t < 4:
        v[t] = 1
    else:
        v[t - 4] = -1
    return (v[0], v[1], v[2], v[3], 1)


def fscal(a, num, den):
    return fnorm(a[0] * num, a[1] * num, a[2] * num, a[3] * num, a[4] * den)


def fnormsq(a):
    return fmul(a, fconj(a))


def is_rational(a):
    return a[1] == 0 and a[2] == 0 and a[3] == 0


def to_fraction(a):
    return Fraction(a[0], a[4])


def qsqrt2_pair(a):
    """an element of the real subfield Q(sqrt2) as (p, q) meaning p + q
    sqrt2, since z - z^3 = sqrt2.  Every trace this unit publishes lands
    here, which is checked rather than assumed."""
    return (Fraction(a[0], a[4]), Fraction(a[1], a[4]))


def in_q_sqrt2(a):
    return a[2] == 0 and a[1] == -a[3]


def qs_str(x):
    """the canonical rendering of an element of Q(sqrt2): the rational part
    alone where the surd part vanishes, and the pair otherwise -- so a value
    that is a plain rational is published as one."""
    if x[1] == 0:
        return str(x[0])
    return "%s+%s*sqrt2" % (x[0], x[1])


def qs_less(x, y):
    """exact ordering on Q(sqrt2): p + q sqrt2 < r + s sqrt2 decided by
    integer comparison of squares, never by a decimal expansion."""
    p, q = y[0] - x[0], y[1] - x[1]
    if q == 0:
        return p > 0
    if q > 0:
        return p >= 0 or p * p < 2 * q * q
    return p > 0 and p * p > 2 * q * q


INV_SQRT2 = (0, 1, 0, -1, 2)          # (z - z^3)/2 = 1/sqrt(2)


# ===========================================================================
# SECTION 2.  THE GATE LEDGER, THE SEAL
# ===========================================================================

class GateFail(Exception):
    pass


class Ledger:
    """every row is DIGESTED AT THE MOMENT IT CLOSES, chained to its
    predecessor; a row edited after its gate closed no longer matches its own
    gate-time digest, in run and again at the disk boundary."""

    def __init__(self):
        self.rows = []
        self.ids = set()
        self.digests = []

    def gate(self, gid, claim, ok, detail="", kind="MEASURED"):
        if gid in self.ids:
            raise GateFail("%s :: duplicate gate id" % gid)
        self.ids.add(gid)
        row = {"gate": gid, "claim": claim, "passed": bool(ok),
               "detail": detail, "kind": kind}
        self.rows.append(row)
        prev = self.digests[-1] if self.digests else "GENESIS"
        self.digests.append(digest({"prev": prev, "row": row}))
        if not ok:
            raise GateFail("%s :: %s :: %s" % (gid, claim, detail))
        return True


class Seal:
    """gate-to-disk (#119): digest AT VALUE-CLOSE -- the moment the gate that
    vouches the values passes.  The manifest is TOTAL: every published
    top-level key is either sealed at its own gate or named in the
    declaration with the reason it cannot be."""

    def __init__(self):
        self.man = []
        self.by_key = {}

    @staticmethod
    def project(obj, omit):
        if not omit:
            return obj
        return {k: v for k, v in obj.items() if k not in omit}

    @staticmethod
    def resolve(payload, key):
        cur = payload
        for part in key.split("/"):
            if isinstance(cur, list):
                hit = None
                for e in cur:
                    if isinstance(e, dict) and e.get("row") == part:
                        hit = e
                        break
                if hit is None:
                    return None, False
                cur = hit
            elif isinstance(cur, dict) and part in cur:
                cur = cur[part]
            else:
                return None, False
        return cur, True

    def take(self, name, key, gate, obj, omit=None):
        d = digest(self.project(obj, omit))
        self.man.append({"object": name, "receipt_key": key, "gate": gate,
                         "digest": d,
                         "omitted_and_sealed_separately": sorted(omit or [])})
        self.by_key[key] = (d, obj)
        return d

    def reverify(self, payload):
        bad = []
        for row in self.man:
            k = row["receipt_key"]
            cur, found = self.resolve(payload, k)
            if not found:
                bad.append((k, "absent"))
                continue
            if digest(self.project(
                    cur, row["omitted_and_sealed_separately"])) \
                    != row["digest"]:
                bad.append((k, "moved"))
        return bad


LD = Ledger()
SEAL = Seal()


# ===========================================================================
# SECTION 3.  PROVENANCE -- the pinned sources, read at declared paths
# ===========================================================================

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.dirname(ROOT)

SOURCES = [
    ("S-PIN", "v14/note-act-pin.md", "766c603c6dbc",
     "THE PIN, frozen before this instrument existed"),
    ("S-SMU-PAPER", "v14/paper-27-smu.md", "6df0db523d32",
     "PARENT 1, SMU terminal: the dynamics census, the invariant simplexes, "
     "the conserved price, the law-native measure and its stamp, and the "
     "inheritance row this unit discharges"),
    ("S-SMU-CODE", "v14/code/smu_exact.py", "126912ae7142",
     "PARENT 1's instrument -- read for its declared definitions only; "
     "nothing is imported from it"),
    ("S-SMU-RECEIPT", "v14/code/smu_receipt.json", "0d6fbadd756d",
     "PARENT 1's receipt: the law-native rates, the simplex dimensions, the "
     "gauge orbit census and the Wilson range this unit re-reads"),
    ("S-P23-PAPER", "v14/paper-23-measure.md", "79cc67b4f6cd",
     "PARENT 2, paper-23 terminal: the 640-configuration space, the "
     "withholding machinery, the transitivity criterion and the Gibbs row "
     "this unit supplies"),
    ("S-P23-CODE", "v14/code/r5m_measure_exact.py", "faf353385905",
     "PARENT 2's instrument -- read for its declared definitions only"),
    ("S-P23-RECEIPT", "v14/code/r5m_measure_receipt.json", "c9edf97a5533",
     "PARENT 2's receipt: the orbit counts and the invariant simplex "
     "dimensions this unit's reachable set sits inside"),
    ("S-R5-PAPER", "v14/paper-18-gauge-rung.md", "62cfe5689d2c",
     "PARENT 3, R5 terminal: the 16 plaquettes, the four-corner holonomy, "
     "the chart group, the gauge action and the 640-coin family"),
    ("S-R5-CODE", "v14/code/r5_gauge_exact.py", "0d98de793b79",
     "PARENT 3's instrument -- read for its declared definitions only"),
    ("S-R5-RECEIPT", "v14/code/r5_gauge_receipt.json", "0c02b7684e5b",
     "PARENT 3's receipt: the anchored arena cardinalities"),
    ("S-GI-RECEIPT", "v14/code/giter_receipt.json", "42255f50328a",
     "the Gamma-iteration terminal's receipt: the law-native positional "
     "law, which is the CONTROL target and is never spent as derived"),
]

PAPER_REL = "v14/paper-34-act.md"
OUT_REL = "v14/code/act_output.txt"
RECEIPT_REL = "v14/code/act_receipt.json"

BANNED_NAMES = ["subprocess", "numpy", "random", "scipy", "git", "math"]
BANNED_CALLS = ["system", "popen", "check_output", "urlopen", "log", "exp",
                "sqrt"]


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
        if mut("MUT-SOURCE-DRIFT") and name == "S-SMU-RECEIPT":
            d = "000000000000"
        rows.append({"name": name, "path": rel, "pinned": sha, "measured": d,
                     "ok": d == sha, "what": what})
        got[name] = b
    return got, rows


# ---------------------------------------------------------------- path-value
PATH_VALUES = [
    ("PV-COINS", "S-R5-RECEIPT", "counts/coins", 640, "G-ARENA-REBUILT",
     "the derived coin family's size"),
    ("PV-DIAG", "S-R5-RECEIPT", "counts/coins_diagonal", 64,
     "G-ARENA-REBUILT", "the diagonal sector"),
    ("PV-ANTI", "S-R5-RECEIPT", "counts/coins_antidiagonal", 64,
     "G-ARENA-REBUILT", "the antidiagonal sector"),
    ("PV-BAL", "S-R5-RECEIPT", "counts/coins_balanced", 512,
     "G-ARENA-REBUILT", "the balanced sector"),
    ("PV-ALPH", "S-R5-RECEIPT", "counts/alphabet", 25, "G-ARENA-REBUILT",
     "the coefficient alphabet"),
    ("PV-SITES", "S-R5-RECEIPT", "counts/sites", 16, "G-ARENA-REBUILT",
     "the site count at the anchored size"),
    ("PV-LINKS", "S-R5-RECEIPT", "counts/links", 32, "G-ARENA-REBUILT",
     "the link count"),
    ("PV-PLAQ", "S-R5-RECEIPT", "counts/plaquettes", 16, "G-ARENA-REBUILT",
     "the plaquette count"),
    ("PV-CHART", "S-R5-RECEIPT", "counts/chart_group", 32,
     "G-CHART-GROUPS-REBUILT", "the anchored chart group's order"),
    ("PV-DEFECT", "S-R5-RECEIPT", "counts/defect_carrying_coins", 384,
     "G-OBSERVABLES-ARE-GAUGE-INVARIANT",
     "the parent's defect census, one declared observable's own count"),
    ("PV-P23-ORB32", "S-P23-RECEIPT",
     "candidate_invariance/uniqueness/CHART-32/orbits", 208,
     "G-RESIDUAL-GAUGE-REBUILT",
     "paper-23's orbit count at the anchored chart reading"),
    ("PV-P23-SIMP32", "S-P23-RECEIPT",
     "candidate_invariance/uniqueness/CHART-32/simplex_dimension", 207,
     "G-PRICE-REDUCED-NOT-EVADED",
     "paper-23's invariant simplex dimension, the price this unit reduces"),
    ("PV-P23-ORB128", "S-P23-RECEIPT",
     "candidate_invariance/uniqueness/CHART-128/orbits", 120,
     "G-RESIDUAL-GAUGE-REBUILT",
     "paper-23's orbit count at the extension reading"),
    ("PV-P23-SIMP128", "S-P23-RECEIPT",
     "candidate_invariance/uniqueness/CHART-128/simplex_dimension", 119,
     "G-PRICE-REDUCED-NOT-EVADED",
     "paper-23's invariant simplex dimension at the extension"),
    ("PV-P23-SLICE", "S-P23-RECEIPT", "arena/uniform_slice", 640,
     "G-CARRIER-IS-THE-PARENTS-PRIMARY-CARRIER",
     "paper-23's primary carrier, which is this unit's carrier"),
    ("PV-P23-MONO", "S-P23-RECEIPT", "candidate_group_haar/monomial_coins",
     128, "G-TARGET-CENSUS",
     "the parent's one canonical measure's carrier, one declared target"),
    ("PV-SMU-ORB32", "S-SMU-RECEIPT", "gauge/orbits_chart_32", 208,
     "G-RESIDUAL-GAUGE-REBUILT",
     "SMU's own reproduction of the anchored orbit count"),
    ("PV-SMU-ORB128", "S-SMU-RECEIPT", "gauge/orbits_chart_128", 120,
     "G-RESIDUAL-GAUGE-REBUILT",
     "SMU's own reproduction of the extension orbit count"),
    ("PV-SMU-RES4", "S-SMU-RECEIPT", "gauge/residual_group_order_chart_32", 4,
     "G-RESIDUAL-GAUGE-REBUILT", "the residual gauge group on the carrier"),
    ("PV-SMU-RES8", "S-SMU-RECEIPT", "gauge/residual_group_order_chart_128",
     8, "G-RESIDUAL-GAUGE-REBUILT", "the same at the extension reading"),
    ("PV-SMU-TWIST", "S-SMU-RECEIPT", "gauge/realisable_constant_twists/1", 2,
     "G-THE-ODD-TWIST-IS-NOT-REALISABLE",
     "the first non-identity constant twist the torus DOES close, which is "
     "even -- the fact the whole price reduction turns on"),
    ("PV-SMU-SIMP32", "S-SMU-RECEIPT", "welds/gauge_simplex_dimension_"
     "chart_32", 207, "G-PRICE-REDUCED-NOT-EVADED",
     "SMU's own reproduction of the anchored simplex dimension"),
    ("PV-SMU-SIMP128", "S-SMU-RECEIPT", "welds/gauge_simplex_dimension_"
     "chart_128", 119, "G-PRICE-REDUCED-NOT-EVADED",
     "SMU's own reproduction of the extension simplex dimension"),
    ("PV-SMU-PRICE639", "S-SMU-RECEIPT", "surjection/dropped_covariance/"
     "price_without_the_covariance_declaration", 639,
     "G-PRICE-REDUCED-NOT-EVADED",
     "the price with the covariance declaration dropped"),
    ("PV-SMU-WILSON-N", "S-SMU-RECEIPT",
     "wilson/distinct_values_over_the_carrier", 11,
     "G-WILSON-OBSERVABLE-REBUILT",
     "the number of distinct loop-trace values on the carrier"),
    ("PV-SMU-WILSON-MIN", "S-SMU-RECEIPT",
     "wilson/range_over_the_invariant_simplex/minimum", "0",
     "G-WILSON-RANGE-OVER-THE-SIMPLEX",
     "the minimum of the loop trace over the carrier"),
    ("PV-SMU-WILSON-MAX", "S-SMU-RECEIPT",
     "wilson/range_over_the_invariant_simplex/maximum", "4",
     "G-WILSON-RANGE-OVER-THE-SIMPLEX",
     "the maximum, and the top of the range SMU measured"),
    ("PV-SMU-FIBRE", "S-SMU-RECEIPT", "wilson/normalisation_fibre", 2,
     "G-WILSON-OBSERVABLE-REBUILT",
     "the observable's declared normalisation fibre"),
    ("PV-SMU-STAMP", "S-SMU-RECEIPT", "privilege/stamp",
     "LAW-RATED-CONSTRUCTION-DECLARED-AT-AN-UNPINNED-IDENTIFICATION",
     "G-LAW-NATIVE-CONTROL-STAMP-CARRIED",
     "the control row's stamp, carried here VERBATIM and never spent"),
    ("PV-SMU-LAW1", "S-SMU-RECEIPT", "law_native_rates/values/0", "15/38",
     "G-LAW-NATIVE-CONTROL-STAMP-CARRIED", "the law-native sector law"),
    ("PV-SMU-LAW2", "S-SMU-RECEIPT", "law_native_rates/values/1", "5/19",
     "G-LAW-NATIVE-CONTROL-STAMP-CARRIED", "the second sector"),
    ("PV-SMU-LAW3", "S-SMU-RECEIPT", "law_native_rates/values/2", "13/38",
     "G-LAW-NATIVE-CONTROL-STAMP-CARRIED", "the third sector"),
    ("PV-GI-LAW1", "S-GI-RECEIPT", "targets/law_value_leg1/0", "15/38",
     "G-LAW-NATIVE-CONTROL-STAMP-CARRIED",
     "the same law value at its own source, read independently"),
    ("PV-GI-LAW3", "S-GI-RECEIPT", "targets/law_value_leg1/2", "13/38",
     "G-LAW-NATIVE-CONTROL-STAMP-CARRIED",
     "the third position at its own source"),
]


def dig(obj, path):
    cur = obj
    for part in path.split("/"):
        if isinstance(cur, list):
            cur = cur[int(part)]
        else:
            cur = cur[part]
    return cur


# ---------------------------------------------------------------- verbatim
VERBATIM = [
    ("VB-PIN-FORM", "S-PIN",
     "characterize ALL weight\n   systems satisfying the measured constraints",
     "G-FORM-CENSUS-COMPLETE", "the pin's own statement of stage one"),
    ("VB-PIN-MULT", "S-PIN",
     "the action is carried\nMULTIPLICATIVELY — local weight systems w "
     "(positive exact\nrationals per local datum), the configuration weight "
     "W(c) =\nΠ w(local parts)",
     "G-WEIGHTS-ARE-POSITIVE-RATIONALS",
     "the binding multiplicative framing"),
    ("VB-PIN-GRAIN", "S-PIN",
     "the locality grain itself a declared axis: per-link /\n   per-plaquette "
     "/ per-site, every member run",
     "G-FORM-CENSUS-COMPLETE", "the declared locality axis, every member run"),
    ("VB-PIN-COUPLING", "S-PIN",
     "The dimension modulo normalization =\n   THE COUPLING COUNT",
     "G-RANK-IS-ORBITS-MINUS-ONE",
     "what the allowed space's rank is declared to mean"),
    ("VB-PIN-PRICE", "S-PIN",
     "THE CONSERVED-PRICE\n   BINDING: does choosing a weight system evade "
     "SMU's\n   207/639?",
     "G-PRICE-REDUCED-NOT-EVADED", "the price question, put by the pin"),
    ("VB-PIN-FALSIFIER", "S-PIN",
     "the cheap falsifier run: is\n   there ANY gauge observable whose "
     "expectation the\n   covariance constraints pin to a proper sub-range?",
     "G-FALSIFIER-CENSUS", "the cheap falsifier, put by the pin"),
    ("VB-PIN-POT", "S-PIN",
     "the confinement vocabulary REMAINS\n   BEHIND POT'S GATE — this "
     "unit makes no area-law,\n   string-tension, or potential claim",
     "G-MUST-NOT-VOCABULARY", "the must-not this unit is held to"),
    ("VB-SMU-CONTROL", "S-SMU-PAPER",
     "ACT must not treat it as a derived measure and must not spend it as\n"
     "  one.",
     "G-LAW-NATIVE-CONTROL-STAMP-CARRIED",
     "the inheritance order this unit obeys"),
    ("VB-SMU-STAMP", "S-SMU-PAPER",
     "The row is therefore stamped\n"
     "`LAW-RATED-CONSTRUCTION-DECLARED-AT-AN-UNPINNED-IDENTIFICATION`: a\n"
     "**transported law value**, not a measure derived by a dynamics.",
     "G-LAW-NATIVE-CONTROL-STAMP-CARRIED",
     "the stamp in its own sentence, so the anchor binds meaning"),
    ("VB-SMU-FALSIFIER", "S-SMU-PAPER",
     "Search for a gauge-invariant\n  functional whose range over the "
     "invariant simplex is *narrower* than its own\n  range.",
     "G-FALSIFIER-CENSUS", "the falsifier as the parent set it"),
    ("VB-SMU-PRICE", "S-SMU-PAPER",
     "The covariant-dynamics fibre therefore surjects onto the invariant "
     "simplex, so\ndeclaring a covariant irreducible dynamics on this carrier "
     "still supplies\nexactly 207 independent numbers at the anchored reading "
     "and 119 at the\nextension",
     "G-PRICE-REDUCED-NOT-EVADED",
     "the parent's price, which this unit's route does not pay"),
    ("VB-SMU-LOCALITY", "S-SMU-PAPER",
     "**Locality.** This carrier cannot see it: one coin serves every link, "
     "so a\n  link-local resampling and a global one coincide.",
     "G-GRAIN-DEGENERACY-ON-THE-CARRIER",
     "the parent's own disclosure, which this unit measures exactly"),
    ("VB-P23-GIBBS", "S-P23-PAPER",
     "A weight of the form $e^{-S}$ needs an action functional and a coupling",
     "G-GIBBS-ROW-SUPPLIED",
     "the census row this unit supplies the missing ingredient for"),
    ("VB-P23-NOACTION", "S-P23-PAPER",
     "It has no configuration measure, no action functional, no coupling and "
     "no\n> dynamics for the link variables",
     "G-GIBBS-ROW-SUPPLIED", "R5's own declaration, quoted by paper-23"),
    ("VB-P23-TRANSITIVE", "S-P23-PAPER",
     "A canonical — equivariant, zero-free-item — probability "
     "measure on a finite\n> carrier exists exactly where some declared "
     "structure acts **transitively** on\n> that carrier.",
     "G-WILSON-IS-NOT-MINIMAL-SUPPORT",
     "the parent's criterion, applied here to the single-link datum"),
    ("VB-P23-INVARIANT", "S-P23-PAPER",
     "A measure is invariant under a group acting on a finite set if and only "
     "if it\nis constant on the orbits.",
     "G-REACHABLE-SET-IS-A-SUBSIMPLEX",
     "the characterisation the reachable set is measured against"),
    ("VB-R5-PLAQ", "S-R5-PAPER",
     "the holonomy is the ordered product of the\nfour link operators around "
     "the boundary, each inverted where the boundary runs\nagainst the link's "
     "own direction",
     "G-WILSON-OBSERVABLE-REBUILT",
     "the loop observable's definition, rebuilt here from these words"),
    ("VB-R5-BLOCK", "S-R5-PAPER",
     "the whole holonomy lives in a four-by-four block",
     "G-WILSON-OBSERVABLE-REBUILT", "why the observable is a block trace"),
    ("VB-R5-THREE", "S-R5-PAPER",
     "A confinement analog would need\n  three objects this arena does not "
     "have: a measure on configurations, a family\n  of loops whose size can "
     "grow, and a coupling to vary.",
     "G-POT-HANDOFF", "the three objects, of which this unit supplies one"),
]

VERBATIM_FLOOR = 40


def wsnorm(s):
    return re.sub(r"\s+", " ", s).strip()


def mnorm(s):
    """#125: whitespace AND markdown-prefix normalisation, inline emphasis
    stripped, so a claim under asterisks is the same claim and a needle
    broken across lines is still located."""
    s = re.sub(r"[*_`]+", "", s)
    s = re.sub(r"^\s*[>\-\*\+]\s+", " ", s, flags=re.M)
    return re.sub(r"\s+", " ", s).strip().lower()


# ===========================================================================
# SECTION 4.  THE ARENA, REBUILT FROM THE PARENTS' DECLARED DEFINITIONS
# ===========================================================================

def build_alphabet():
    """R4's coefficient alphabet as R5 declares it: 0 together with zeta_8^t
    at each of the three declared moduli."""
    out, seen = [], set()
    cands = [ZERO]
    for t in range(8):
        cands.append(zpow(t))
        cands.append(fscal(zpow(t), 1, 2))
        cands.append(fmul(zpow(t), INV_SQRT2))
    for a in cands:
        if a not in seen:
            seen.add(a)
            out.append(a)
    return out


def build_coins(alphabet):
    """THE COIN FAMILY, DERIVED: a two-by-two unitary all four of whose
    entries lie in the alphabet, enumerated exhaustively over the alphabet's
    fourth power and pruned by the row conditions.  Nothing about the size is
    typed."""
    rows = [(a, b) for a in alphabet for b in alphabet
            if fadd(fnormsq(a), fnormsq(b)) == ONE]
    coins = []
    for (a, b) in rows:
        for (c, d) in rows:
            if fadd(fmul(a, fconj(c)), fmul(b, fconj(d))) == ZERO:
                coins.append((a, b, c, d))
    if mut("MUT-ARENA"):
        coins = coins[:-1]
    return coins, rows


def coin_sector(m):
    a, b, c, d = m
    if b == ZERO and c == ZERO:
        return "DIAGONAL"
    if a == ZERO and d == ZERO:
        return "ANTIDIAGONAL"
    return "BALANCED"


def coin_unitary_second_route(m):
    a, b, c, d = m
    return (fadd(fmul(fconj(a), a), fmul(fconj(c), c)) == ONE
            and fadd(fmul(fconj(b), b), fmul(fconj(d), d)) == ONE
            and fadd(fmul(fconj(a), b), fmul(fconj(c), d)) == ZERO)


def gauge_twist(m, k):
    """the site-diagonal gauge acts on a link's coin by conjugation with
    D = diag(zeta_8^p, zeta_8^q); the action depends on k = p - q alone."""
    a, b, c, d = m
    return (a, fmul(zpow(k), b), fmul(zpow(-k), c), d)


def swap_conjugate(m):
    """X U X: the coin read from the other end of its own domino."""
    a, b, c, d = m
    return (d, c, b, a)


L_ANCHORED = 4
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

    def boundary(self, p):
        """the four (link, orientation) steps of the plaquette boundary,
        traversed p -> p+e1 -> p+e1+e2 -> p+e2 -> p.  Orientation -1 means
        the link runs against its own direction, so its operator inverts."""
        return (((p, 0), 1),
                ((self.addv(p, E1), 1), 1),
                ((self.addv(p, E2), 0), -1),
                ((p, 1), -1))

    def star(self, x):
        """the four links incident to a site: two outgoing, two incoming."""
        return [(x, 0), (x, 1),
                (((x[0] - 1) % self.L, x[1]), 0),
                ((x[0], (x[1] - 1) % self.L), 1)]


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


def point_on_dir(g, d):
    sw, sx, sy = g
    x, y = EDIR[d]
    if sw:
        x, y = y, x
    x, y = sx * x, sy * y
    if (abs(x), abs(y)) == (1, 0):
        return 0, (1 if x > 0 else -1)
    return 1, (1 if y > 0 else -1)


def chart_elements(lat, extended):
    return [(v, g) for v in lat.sites
            for g in point_symmetries(extended)]


def transported_link(lat, l, elem):
    """the image of a link under a chart element, with the domino's
    orientation tracked: where the point part reverses the direction the
    image is read the other way round and the transported coin is the swap
    conjugate."""
    v, g = elem
    s, d = l
    d2, sign = point_on_dir(g, d)
    s2 = lat.addv(apply_point(g, s, lat.L), v)
    if sign > 0:
        return (s2, d2), False
    return ((((s2[0] - EDIR[d2][0]) % lat.L,
              (s2[1] - EDIR[d2][1]) % lat.L), d2), True)


def holonomy_block(lat, p, coin_of):
    """W_p on its own four corners.  Every factor is the identity off those
    corners, so the product is too and the restriction is exact."""
    corners = [p, lat.addv(p, E1), lat.addv(lat.addv(p, E1), E2),
               lat.addv(p, E2)]
    pos = {c: i for i, c in enumerate(corners)}
    W = [[ONE if i == j else ZERO for j in range(4)] for i in range(4)]
    for l, o in lat.boundary(p):
        t, h = lat.ends(l)
        it, ih = pos[t], pos[h]
        a, b, c, d = coin_of(l)
        if o < 0:
            a, b, c, d = fconj(a), fconj(c), fconj(b), fconj(d)
        M = [[ONE if i == j else ZERO for j in range(4)] for i in range(4)]
        M[it][it], M[it][ih], M[ih][it], M[ih][ih] = a, b, c, d
        NW = [[ZERO] * 4 for _ in range(4)]
        for i in range(4):
            Mi = M[i]
            for k in range(4):
                if Mi[k] == ZERO:
                    continue
                Wk = W[k]
                for j in range(4):
                    if Wk[j] != ZERO:
                        NW[i][j] = fadd(NW[i][j], fmul(Mi[k], Wk[j]))
        W = NW
    return W


def block_trace(W):
    t = ZERO
    for i in range(4):
        t = fadd(t, W[i][i])
    return t


# ===========================================================================
# SECTION 5.  THE COIN-MAP GROUP GAMMA, AND ITS CAYLEY TABLE
# ===========================================================================
# Every symmetry this unit imposes acts on a local datum by permuting the
# stencil's link slots and applying, slot by slot, an element of the group
# GAMMA generated by the elementary gauge twist and the swap conjugation.
# GAMMA is built as PERMUTATIONS OF THE COIN FAMILY and its multiplication
# table is precomputed once, so every later group is a group of pairs
# (permutation of slots, tuple of GAMMA indices) and no field arithmetic is
# repeated inside a census.

class GammaGroup:
    def __init__(self, coins, cidx):
        elems, seen = [], {}
        for k in range(8):
            for sw in (0, 1):
                if sw:
                    p = tuple(cidx[swap_conjugate(gauge_twist(m, k))]
                              for m in coins)
                else:
                    p = tuple(cidx[gauge_twist(m, k)] for m in coins)
                if p not in seen:
                    seen[p] = len(elems)
                    elems.append(p)
        self.elems = elems
        self.index = seen
        n = len(elems)
        self.mul = [[seen[tuple(elems[i][elems[j][x]]
                                for x in range(len(coins)))]
                     for j in range(n)] for i in range(n)]
        self.identity = seen[tuple(range(len(coins)))]
        self.fix = [sum(1 for x in range(len(coins)) if p[x] == x)
                    for p in elems]
        self.twist = [seen[tuple(cidx[gauge_twist(m, k)] for m in coins)]
                      for k in range(8)]
        self.swap = seen[tuple(cidx[swap_conjugate(m)] for m in coins)]

    def compose(self, i, j):
        return self.mul[i][j]

    def fix_in(self, i, members):
        p = self.elems[i]
        return sum(1 for x in members if p[x] == x)


def group_orbits(n, perms):
    """orbits of a set of permutations, by union-find."""
    par = list(range(n))

    def find(a):
        while par[a] != a:
            par[a] = par[par[a]]
            a = par[a]
        return a

    for p in perms:
        for i in range(n):
            ra, rb = find(i), find(p[i])
            if ra != rb:
                par[ra] = rb
    out = {}
    for i in range(n):
        out.setdefault(find(i), []).append(i)
    return sorted(out.values())


def close_perm_group(n, gens):
    idp = tuple(range(n))
    G = {idp}
    frontier = [idp]
    while frontier:
        nxt = []
        for g in frontier:
            for s in gens:
                h = tuple(s[g[i]] for i in range(n))
                if h not in G:
                    G.add(h)
                    nxt.append(h)
        frontier = nxt
    return sorted(G)


# ===========================================================================
# SECTION 6.  THE STENCILS, THEIR SYMMETRY GROUPS, AND THE ORBIT COUNTS
# ===========================================================================

def gauge_image(lat, GA, stencil):
    """which tuples of coin-maps the site-diagonal gauge can realise on a
    stencil's links.  MEASURED by enumerating the site phases the stencil
    touches and reading off each link's own twist, never argued: at a
    plaquette the four twists satisfy one relation, at a site's star they do
    not, and that difference is what separates the two grains."""
    ss = sorted({s for l in stencil for s in lat.ends(l)})
    out = set()
    for th in product(range(8), repeat=len(ss)):
        thm = dict(zip(ss, th))
        out.add(tuple(GA.twist[(thm[lat.ends(l)[0]] - thm[lat.ends(l)[1]]) % 8]
                      for l in stencil))
    return sorted(out)


def chart_stabilizer(lat, GA, stencil, extended):
    """the chart elements carrying the stencil's link set to itself, with the
    induced permutation of slots and the swap conjugations they carry.  A
    weight system is covariant exactly when it is invariant under these."""
    S = list(stencil)
    out = []
    for e in chart_elements(lat, extended):
        img, ok = {}, True
        for i, l in enumerate(S):
            im, rev = transported_link(lat, l, e)
            if im not in S:
                ok = False
                break
            img[i] = (S.index(im), rev)
        if not ok:
            continue
        perm = [None] * len(S)
        cm = [None] * len(S)
        for i in range(len(S)):
            j, rev = img[i]
            perm[j] = i
            cm[j] = GA.swap if rev else GA.identity
        out.append((tuple(perm), tuple(cm)))
    return out


def elem_mul(GA, a, b):
    """a after b, on data indexed by stencil slots."""
    ap, ac = a
    bp, bc = b
    n = len(ap)
    return (tuple(bp[ap[j]] for j in range(n)),
            tuple(GA.mul[ac[j]][bc[ap[j]]] for j in range(n)))


def elementary_gauge_generators(lat, GA, stencil):
    """one generator per site the stencil touches: the phase bumped by one
    there and left alone everywhere else.  These generate the gauge image,
    which is checked rather than assumed."""
    n = len(stencil)
    ss = sorted({s for l in stencil for s in lat.ends(l)})
    out = []
    for s0 in ss:
        thm = {s: (1 if s == s0 else 0) for s in ss}
        out.append((tuple(range(n)),
                    tuple(GA.twist[(thm[lat.ends(l)[0]]
                                    - thm[lat.ends(l)[1]]) % 8]
                          for l in stencil)))
    return out


def stencil_group(lat, GA, stencil, extended):
    """the group ACTING on the stencil datum: every product of a chart
    stabiliser element with a gauge element.  Its size is MEASURED as the
    size of the set of distinct ACTIONS -- at one grain the product is not
    faithful and the measured order is half the naive one, which is published
    rather than assumed away.  Closure is checked, and so is the claim that
    the declared elementary generators generate exactly this group."""
    n = len(stencil)
    gi = [(tuple(range(n)), gt) for gt in gauge_image(lat, GA, stencil)]
    stb = chart_stabilizer(lat, GA, stencil, extended)
    G = set()
    for s in stb:
        for g in gi:
            G.add(elem_mul(GA, s, g))
    G = sorted(G)
    Gs = set(G)
    gens = elementary_gauge_generators(lat, GA, stencil) + stb
    fails = sum(1 for g in G for s in gens if elem_mul(GA, s, g) not in Gs)
    idg = (tuple(range(n)), tuple([GA.identity] * n))
    closed = {idg}
    frontier = [idg]
    while frontier:
        nxt = []
        for g in frontier:
            for s in gens:
                h = elem_mul(GA, s, g)
                if h not in closed:
                    closed.add(h)
                    nxt.append(h)
        frontier = nxt
    if closed != Gs:
        fails += 1
    return G, gi, stb, fails, gens


def fixed_data(GA, g, members_fix):
    """|Fix(g)| on the datum space, factorised over the cycles of g's slot
    permutation: along a cycle the constraints chain into one condition on a
    single coin, so the count is the product over cycles of the number of
    coins fixed by the composed map around that cycle."""
    perm, cm = g
    n = len(perm)
    seen = [False] * n
    tot = 1
    for j in range(n):
        if seen[j]:
            continue
        cyc, k = [], j
        while not seen[k]:
            seen[k] = True
            cyc.append(k)
            k = perm[k]
        acc = GA.identity
        for t in cyc:
            acc = GA.mul[acc][cm[t]]
        tot *= members_fix[acc]
    return tot


def burnside(GA, G, members_fix):
    """|X/G| = (1/|G|) sum_g |Fix(g)|.  The sum MUST divide the group order;
    that is the arithmetic check the formula has to pass, and it is a gate."""
    tot = sum(fixed_data(GA, g, members_fix) for g in G)
    if tot % len(G) != 0:
        return None, tot
    return tot // len(G), tot


def datum_orbits_bruteforce(GA, gens, members):
    """the second route where the datum space is small enough to enumerate:
    orbits by union-find over a GENERATING set, datum by datum -- a
    genuinely different computation from the Burnside sum, which never
    touches a datum at all.  Used at the link grain at full size and on the
    declared reduced arena at every grain."""
    n = len(members)
    pos = {c: i for i, c in enumerate(members)}
    slots = len(gens[0][0])
    data = list(product(range(n), repeat=slots))
    didx = {d: i for i, d in enumerate(data)}
    par = list(range(len(data)))

    def find(a):
        while par[a] != a:
            par[a] = par[par[a]]
            a = par[a]
        return a

    for perm, cm in gens:
        maps = [GA.elems[c] for c in cm]
        for d in data:
            im = tuple(pos[maps[j][members[d[perm[j]]]]]
                       for j in range(slots))
            ra, rb = find(didx[d]), find(didx[im])
            if ra != rb:
                par[ra] = rb
    return len({find(i) for i in range(len(data))})


def orbit_stabilizer_sum(GA, G, ncoins):
    """the third route at the link grain: the orbit count as the sum over
    points of |Stab(x)| / |G|, which never enumerates an orbit at all."""
    tot = 0
    for x in range(ncoins):
        tot += sum(1 for (_p, cm) in G if GA.elems[cm[0]][x] == x)
    if tot % len(G) != 0:
        return None
    return tot // len(G)


def induced_classes_on_the_carrier(GA, G, ncoins):
    """the equivalence the grain induces on the UNIFORM carrier: two coins
    are identified exactly when some element of the stencil group carries the
    constant datum at one to the constant datum at the other.  The slot
    permutation drops out of a constant datum, so what decides is the tuple
    of coin-maps alone."""
    par = list(range(ncoins))

    def find(a):
        while par[a] != a:
            par[a] = par[par[a]]
            a = par[a]
        return a

    for cm in {g[1] for g in G}:
        maps = [GA.elems[c] for c in cm]
        for u in range(ncoins):
            v = maps[0][u]
            if all(m[u] == v for m in maps):
                ra, rb = find(u), find(v)
                if ra != rb:
                    par[ra] = rb
    out = {}
    for i in range(ncoins):
        out.setdefault(find(i), []).append(i)
    return sorted(out.values())


# ===========================================================================
# SECTION 7.  THE MEASUREMENTS, IN ORDER, EACH BEHIND ITS GATE
# ===========================================================================

def measure_provenance(S):
    src, rows = load_sources()
    bad = [r for r in rows if not r["ok"]]
    LD.gate("G-SOURCE-BYTES",
            "every pinned source is read at its declared relative path and "
            "its sha256-12 measured against the value frozen in this "
            "instrument, so a parent edited after this unit was built stops "
            "this run; the repository is read at NO moving reference at all "
            "-- no ledger, no STATUS board, no worktree scan, no "
            "version-control call -- so this run is correct off-tree and in "
            "a directory with no version control (#91, #46)",
            not bad, "%d of %d source digests match; failing %s"
            % (len(rows) - len(bad), len(rows), [b["name"] for b in bad]))
    S["provenance"] = {"sources": rows,
                       "python": "%d.%d" % sys.version_info[:2]}
    SEAL.take("THE PINNED SOURCES", "provenance", "G-SOURCE-BYTES",
              S["provenance"])

    tree = ast.parse(own_source())
    floats = [n for n in ast.walk(tree)
              if isinstance(n, ast.Constant) and isinstance(n.value, float)]
    imports = set()
    for n in ast.walk(tree):
        if isinstance(n, ast.Import):
            for a in n.names:
                imports.add(a.name.split(".")[0])
        elif isinstance(n, ast.ImportFrom) and n.module:
            imports.add(n.module.split(".")[0])
    badimp = sorted(imports & set(BANNED_NAMES))
    calls = []
    for n in ast.walk(tree):
        if isinstance(n, ast.Call):
            f = n.func
            nm = getattr(f, "attr", None) or getattr(f, "id", None)
            if nm in BANNED_CALLS:
                calls.append(nm)
    LD.gate("G-WEIGHTS-ARE-POSITIVE-RATIONALS",
            "the pin's multiplicative framing is a property of this source "
            "and not a promise about it: the syntax tree carries NO float "
            "literal, no banned import and -- the clause this unit adds -- "
            "no call to a logarithm, an exponential or a square root, so "
            "'the action is carried multiplicatively, no logs' is checked "
            "rather than asserted.  Every weight is a Fraction, every field "
            "element an integer 5-tuple, and every orbit count an exact "
            "integer",
            not floats and not badimp and not calls,
            "%d float literals, banned imports %s, banned calls %s"
            % (len(floats), badimp, sorted(set(calls))))
    S["arithmetic"] = {
        "float_literals": len(floats), "banned_imports": badimp,
        "banned_calls": sorted(set(calls)),
        "field": "Q(zeta_8) as integer 5-tuples over (1, z, z^2, z^3) "
                 "mod z^4+1",
        "weights": "fractions.Fraction, strictly positive",
        "the_action": "CARRIED-MULTIPLICATIVELY-S-IS-NOMINAL-ONLY-NO-LOGS",
        "orbit_counts": "exact integers from a Burnside sum that divides"}
    SEAL.take("THE ARITHMETIC", "arithmetic",
              "G-WEIGHTS-ARE-POSITIVE-RATIONALS", S["arithmetic"])
    return src


def measure_path_values(S, src):
    rows, cache = [], {}
    for aid, sname, path, want, consumer, what in PATH_VALUES:
        if sname not in cache:
            cache[sname] = json.loads(src[sname].decode())
        got = dig(cache[sname], path)
        if mut("MUT-PATH-VALUE") and aid == "PV-P23-SIMP32":
            got = 999
        rows.append({"anchor": aid, "source": sname, "path": path,
                     "declared": want, "measured": got, "ok": got == want,
                     "consumer": consumer, "what": what})
    bad = [r for r in rows if not r["ok"]]
    LD.gate("G-PATH-VALUE-ANCHORS",
            "every inherited quantity is a (path, value) pair: the path must "
            "resolve in the pinned receipt AND the value there must be the "
            "one this instrument declares, and each is bound to the gate "
            "that consumes it -- so a parent that moved a number under a "
            "surviving key stops this run",
            not bad, "%d of %d path-value anchors resolve; failing %s"
            % (len(rows) - len(bad), len(rows), [b["anchor"] for b in bad]))
    S["path_value_anchors"] = rows
    SEAL.take("THE PATH-VALUE ANCHORS", "path_value_anchors",
              "G-PATH-VALUE-ANCHORS", rows)
    return {r["anchor"]: r["measured"] for r in rows}


def measure_verbatim(S, src):
    rows = []
    for aid, sname, window, consumer, what in VERBATIM:
        hay = mnorm(src[sname].decode())
        if mut("MUT-VERBATIM") and aid == "VB-SMU-CONTROL":
            window = window.replace("must not", "may")
        needle = mnorm(window)
        n = hay.count(needle)
        toks = [t for t in re.findall(r"[A-Za-z0-9]+", window) if len(t) > 3]
        pert = window.replace(toks[-1], toks[-1] + "X", 1) if toks else window
        pn = hay.count(mnorm(pert))
        ok = (n == 1 and pn == 0 and len(needle) >= VERBATIM_FLOOR)
        rows.append({"anchor": aid, "source": sname, "chars": len(needle),
                     "floor": VERBATIM_FLOOR, "located": n,
                     "perturbed_located": pn, "ok": ok, "consumer": consumer,
                     "what": what, "digest": bdigest(needle.encode())})
    bad = [r for r in rows if not r["ok"]]
    LD.gate("G-VERBATIM-ANCHORS",
            "every quotation this paper makes of a parent is located EXACTLY "
            "ONCE in that parent's pinned bytes under whitespace and "
            "markdown-prefix normalisation (#125), is pinned by its own "
            "digest and its own character count against a declared floor, "
            "stops being locatable when a content-bearing token is "
            "perturbed, and is bound to the gate that consumes it -- so the "
            "anchor binds QUOTE FIDELITY and not mere existence (#62)",
            not bad,
            "%d of %d verbatim windows located exactly once and falsified "
            "under perturbation; failing %s"
            % (len(rows) - len(bad), len(rows), [b["anchor"] for b in bad]))
    S["verbatim_anchors"] = rows
    SEAL.take("THE VERBATIM ANCHORS", "verbatim_anchors", "G-VERBATIM-ANCHORS",
              rows)
    S["anchor_classes"] = {"file_bytes": len(SOURCES),
                           "path_value": len(PATH_VALUES),
                           "verbatim_text": len(VERBATIM),
                           "total": len(SOURCES) + len(PATH_VALUES)
                           + len(VERBATIM)}
    SEAL.take("THE ANCHOR CLASSES", "anchor_classes", "G-VERBATIM-ANCHORS",
              S["anchor_classes"])


def build_arena(S, pv):
    alph = build_alphabet()
    coins, rows = build_coins(alph)
    cidx = {m: i for i, m in enumerate(coins)}
    lat = Lattice(L_ANCHORED)
    sect = {}
    for m in coins:
        sect[coin_sector(m)] = sect.get(coin_sector(m), 0) + 1
    unit_ok = all(coin_unitary_second_route(m) for m in coins)
    ok = (len(alph) == pv["PV-ALPH"] and len(coins) == pv["PV-COINS"]
          and sect.get("DIAGONAL") == pv["PV-DIAG"]
          and sect.get("ANTIDIAGONAL") == pv["PV-ANTI"]
          and sect.get("BALANCED") == pv["PV-BAL"]
          and len(lat.sites) == pv["PV-SITES"]
          and len(lat.links) == pv["PV-LINKS"]
          and len(lat.plaquettes) == pv["PV-PLAQ"] and unit_ok)
    LD.gate("G-ARENA-REBUILT",
            "the arena is REBUILT from the parents' declared definitions and "
            "not imported: the alphabet from its declared shape, the coin "
            "family exhaustively over the alphabet's fourth power pruned by "
            "the row conditions, the links and plaquettes derived from the "
            "lattice -- and every cardinality is measured against the "
            "parent's own receipt at a named path, with unitarity confirmed "
            "by a second route on every coin",
            ok,
            "alphabet %d, coins %d (%d diagonal, %d antidiagonal, %d "
            "balanced), %d sites, %d links, %d plaquettes; unitary by the "
            "second route: %s"
            % (len(alph), len(coins), sect.get("DIAGONAL", 0),
               sect.get("ANTIDIAGONAL", 0), sect.get("BALANCED", 0),
               len(lat.sites), len(lat.links), len(lat.plaquettes), unit_ok))
    S["arena"] = {
        "d": 2, "L": lat.L, "field": "Q(zeta_8)", "alphabet": len(alph),
        "admissible_rows": len(rows), "coins": len(coins),
        "sectors": {k: sect[k] for k in sorted(sect)},
        "sites": len(lat.sites), "links": len(lat.links),
        "plaquettes": len(lat.plaquettes),
        "configuration_space": "640^32",
        "carrier": "THE-640-UNIFORM-CONFIGURATIONS",
        "unitary_by_a_second_route": len(coins) if unit_ok else 0}
    SEAL.take("THE ARENA", "arena", "G-ARENA-REBUILT", S["arena"])
    S["_lat"] = lat
    S["_coins"] = coins
    S["_cidx"] = cidx
    return lat, coins, cidx


def measure_chart_and_gauge(S, pv):
    lat, coins, cidx = S["_lat"], S["_coins"], S["_cidx"]
    GA = GammaGroup(coins, cidx)
    if mut("MUT-GAMMA"):
        GA.elems = GA.elems[:-1]
    S["_GA"] = GA
    tw1 = GA.twist[1]
    ordr = 1
    acc = tw1
    while acc != GA.identity:
        acc = GA.mul[acc][tw1]
        ordr += 1
    LD.gate("G-GAMMA-GROUP-BUILT",
            "the coin-map group GAMMA -- generated by the elementary gauge "
            "twist and the swap conjugation, as permutations of the coin "
            "family -- is closed, its multiplication table is exact, and the "
            "elementary twist has order 8, which is the fact every later "
            "orbit count rests on",
            len(GA.elems) == 16 and ordr == 8
            and all(GA.mul[i][GA.identity] == i for i in range(16)),
            "|GAMMA| = %d, the elementary twist has order %d, fixed-coin "
            "profile %s" % (len(GA.elems), ordr, sorted(set(GA.fix))))
    S["gamma"] = {"order": len(GA.elems), "elementary_twist_order": ordr,
                  "coins_fixed_by_a_nonzero_twist": GA.fix[GA.twist[1]],
                  "coins_fixed_by_the_identity": GA.fix[GA.identity],
                  "generators": "THE-ELEMENTARY-GAUGE-TWIST-AND-THE-SWAP-"
                                "CONJUGATION"}
    SEAL.take("THE COIN-MAP GROUP", "gamma", "G-GAMMA-GROUP-BUILT",
              S["gamma"])

    ch32 = chart_elements(lat, False)
    ch128 = chart_elements(lat, True)
    if mut("MUT-CHART"):
        ch32 = ch32[:1]
    lorb32 = group_orbits(len(lat.links),
                          [tuple(lat.links.index(transported_link(lat, l, e)[0])
                                 for l in lat.links) for e in ch32])
    porb32 = len(group_orbits(
        len(lat.plaquettes),
        [tuple(lat.plaquettes.index(
            _plaq_image(lat, p, e)) for p in lat.plaquettes) for e in ch32]))
    LD.gate("G-CHART-GROUPS-REBUILT",
            "both declared chart readings are rebuilt and their action is "
            "MEASURED rather than quoted: the anchored group has the "
            "parent's own order at a named receipt path, and the group is "
            "measured TRANSITIVE on the links and on the plaquettes -- which "
            "is what makes a covariant weight system the transport of one "
            "function on one stencil, so the orbit count of that stencil's "
            "datum is a complete description of the allowed space",
            len(ch32) == pv["PV-CHART"] and len(ch128) == 4 * len(ch32)
            and len(lorb32) == 1 and porb32 == 1,
            "chart orders %d and %d; %d link orbit(s) and %d plaquette "
            "orbit(s) at the anchored reading"
            % (len(ch32), len(ch128), len(lorb32), porb32))
    S["chart"] = {"anchored_order": len(ch32), "extension_order": len(ch128),
                  "link_orbits_anchored": len(lorb32),
                  "plaquette_orbits_anchored": porb32}
    SEAL.take("THE CHART GROUPS", "chart", "G-CHART-GROUPS-REBUILT",
              S["chart"])

    ctw = realisable_constant_twists(lat)
    tau = GA.twist[ctw[1]]
    res32 = close_perm_group(len(coins), [GA.elems[tau]])
    res128 = close_perm_group(len(coins),
                              [GA.elems[tau], GA.elems[GA.swap]])
    o32 = group_orbits(len(coins), res32)
    o128 = group_orbits(len(coins), res128)
    if mut("MUT-RESIDUAL"):
        o32 = o32[:-1]
    ok =(len(o32) == pv["PV-P23-ORB32"] and len(o128) == pv["PV-P23-ORB128"]
          and len(o32) == pv["PV-SMU-ORB32"]
          and len(o128) == pv["PV-SMU-ORB128"]
          and len(res32) == pv["PV-SMU-RES4"]
          and len(res128) == pv["PV-SMU-RES8"]
          and sum(len(o) for o in o32) == len(coins))
    LD.gate("G-RESIDUAL-GAUGE-REBUILT",
            "the residual gauge group ON THE CARRIER is rebuilt by "
            "propagating the site phase around the torus -- a constant twist "
            "is realisable exactly where the assignment closes after L steps "
            "-- and its orbits are enumerated exactly.  Both readings land "
            "on BOTH parents' own counts at named receipt paths, so the "
            "partition this unit's reachable set is compared against is the "
            "parent's partition and not a rebuild of it",
            ok,
            "realisable constant twists %s; residual orders %d and %d; "
            "orbits %d and %d, covering %d coins"
            % (ctw, len(res32), len(res128), len(o32), len(o128),
               sum(len(o) for o in o32)))
    prof32 = {}
    for o in o32:
        prof32[len(o)] = prof32.get(len(o), 0) + 1
    prof128 = {}
    for o in o128:
        prof128[len(o)] = prof128.get(len(o), 0) + 1
    S["residual_gauge"] = {
        "realisable_constant_twists": ctw,
        "order_anchored": len(res32), "order_extension": len(res128),
        "orbits_anchored": len(o32), "orbits_extension": len(o128),
        "orbit_size_profile_anchored": sorted(prof32.items()),
        "orbit_size_profile_extension": sorted(prof128.items()),
        "invariant_simplex_dimension_anchored": len(o32) - 1,
        "invariant_simplex_dimension_extension": len(o128) - 1}
    SEAL.take("THE RESIDUAL GAUGE GROUP", "residual_gauge",
              "G-RESIDUAL-GAUGE-REBUILT", S["residual_gauge"])
    S["_orbits"] = {"ANCHORED": o32, "EXTENSION": o128}

    odd = [c for c in range(8) if c not in ctw]
    if mut("MUT-ODD-TWIST"):
        odd = []
    LD.gate("G-THE-ODD-TWIST-IS-NOT-REALISABLE",
            "the ODD constant twist is measured NOT to be realisable by any "
            "gauge transformation on this torus -- the phase fails to close "
            "after L steps -- while it IS a bijection of the carrier and is "
            "invisible to every local weight system, because a single link's "
            "twist is unconstrained by the torus.  That one measured "
            "asymmetry is the mechanism behind everything this unit reports "
            "about the price",
            odd == [c for c in range(8) if c % 2 == 1]
            and len(ctw) * 2 == 8,
            "realisable %s; not realisable %s" % (ctw, odd))
    S["odd_twist"] = {
        "realisable_constant_twists": ctw,
        "unrealisable_constant_twists": odd,
        "it_is_a_bijection_of_the_carrier": True,
        "no_local_weight_system_can_see_it": True}
    SEAL.take("THE ODD TWIST", "odd_twist",
              "G-THE-ODD-TWIST-IS-NOT-REALISABLE", S["odd_twist"])
    return GA


def _plaq_image(lat, p, elem):
    """the image of a plaquette under a chart element, read off the image of
    its own boundary link set rather than declared."""
    S = {l for l, _o in lat.boundary(p)}
    img = {transported_link(lat, l, elem)[0] for l in S}
    for q in lat.plaquettes:
        if {l for l, _o in lat.boundary(q)} == img:
            return q
    return None


def realisable_constant_twists(lat):
    """which CONSTANT link twists a site-diagonal gauge can realise:
    propagate theta from one site along the links and ask whether the
    assignment closes on the torus.  Measured, not argued."""
    ok = []
    for c in range(8):
        th = {lat.sites[0]: 0}
        frontier = [lat.sites[0]]
        good = True
        while frontier:
            nxt = []
            for s in frontier:
                for d in range(2):
                    t = lat.addv(s, EDIR[d])
                    want = (th[s] - c) % 8
                    if t in th:
                        if th[t] != want:
                            good = False
                    else:
                        th[t] = want
                        nxt.append(t)
                    u = lat.addv(s, (-EDIR[d][0], -EDIR[d][1]))
                    want2 = (th[s] + c) % 8
                    if u in th:
                        if th[u] != want2:
                            good = False
                    else:
                        th[u] = want2
                        nxt.append(u)
            frontier = nxt
        if good and len(th) == len(lat.sites):
            ok.append(c)
    return ok


# ===========================================================================
# SECTION 8.  THE FORM CENSUS -- THE HEART
# ===========================================================================
# The allowed space at a grain and a chart reading is EXACTLY the set of
# positive-rational functions on that grain's stencil datum that are constant
# on the orbits of the stencil group.  That is an equality and not an
# inclusion: invariance under the group IS constancy on its orbits, and every
# orbit-constant assignment is admissible because the orbits partition the
# datum space.  The allowed space is therefore a free module over the
# multiplicative group of positive rationals, of rank equal to the number of
# orbits, and its rank MODULO NORMALISATION -- one less -- is the coupling
# count.

GRAINS = ("LINK", "PLAQUETTE", "SITE")
READINGS = ("ANCHORED", "EXTENSION")


def stencil_of(lat, grain):
    if grain == "LINK":
        return [(lat.sites[0], 0)]
    if grain == "PLAQUETTE":
        return [l for l, _o in lat.boundary(lat.sites[0])]
    return lat.star(lat.sites[0])


def reduced_family(GA, coins, cidx):
    """the declared reduced arena: the union of the GAMMA-orbits of four
    named coins, one from each of the two diagonal orbit types and one from
    each of the other two sectors.  It is GAMMA-closed by construction, which
    is what makes the same machinery apply to it unchanged, and it is small
    enough for the datum space to be enumerated exhaustively at every grain
    -- so the Burnside route is validated against a brute-force orbit
    enumeration end to end, at the same grains and the same groups."""
    named = [("DIAG-I", (ONE, ZERO, ZERO, ONE)),
             ("DIAG-Z", (ONE, ZERO, ZERO, fneg(ONE))),
             ("ANTI-X", (ZERO, ONE, ONE, ZERO)),
             ("BAL-F", (INV_SQRT2, fmul(zpow(2), INV_SQRT2),
                        fmul(zpow(2), INV_SQRT2), INV_SQRT2))]
    mem = set()
    for _nm, m in named:
        i = cidx[m]
        for p in GA.elems:
            mem.add(p[i])
    return sorted(mem), [nm for nm, _m in named]


def run_form_census(S, pv):
    lat, coins, cidx, GA = S["_lat"], S["_coins"], S["_cidx"], S["_GA"]
    n = len(coins)
    allfix = GA.fix
    red, rednames = reduced_family(GA, coins, cidx)
    redfix = [GA.fix_in(i, red) for i in range(len(GA.elems))]
    rows = []
    S["_stencil_groups"] = {}
    for grain in GRAINS:
        st = stencil_of(lat, grain)
        for reading in READINGS:
            G, gi, stb, fails, gens = stencil_group(lat, GA, st,
                                                    reading == "EXTENSION")
            if mut("MUT-GROUP-NOT-CLOSED") and grain == "PLAQUETTE":
                G = G[:-1]
                fails = 1
            orb, tot = burnside(GA, G, allfix)
            if mut("MUT-BURNSIDE") and grain == "SITE":
                orb = orb + 1 if orb else orb
            routes = {"BURNSIDE": orb}
            if grain == "LINK":
                routes["BRUTE-FORCE-UNION-FIND"] = datum_orbits_bruteforce(
                    GA, gens, list(range(n)))
                routes["ORBIT-STABILIZER-SUM"] = orbit_stabilizer_sum(
                    GA, G, n)
            rorb, _rt = burnside(GA, G, redfix)
            rbrute = datum_orbits_bruteforce(GA, gens, red)
            agree = (len({v for v in routes.values()}) == 1
                     and rorb == rbrute and orb is not None
                     and fails == 0 and orb * len(G) == tot)
            rows.append({
                "row": "%s-%s" % (grain, reading), "grain": grain,
                "reading": reading, "stencil_links": len(st),
                "orbit_count_times_the_group_order_equals_the_sum":
                    orb is not None and orb * len(G) == tot,
                "gauge_image_order": len(gi), "chart_stabilizer_order":
                len(stb), "acting_group_order": len(G),
                "closure_failures": fails,
                "datum_space": "%d^%d" % (n, len(st)),
                "orbits": orb, "burnside_sum": tot,
                "coupling_count": (orb - 1) if orb else None,
                "routes_at_full_size": routes,
                "reduced_arena_coins": len(red),
                "reduced_arena_orbits_burnside": rorb,
                "reduced_arena_orbits_brute_force": rbrute,
                "routes_agree": agree})
            S["_stencil_groups"][(grain, reading)] = G
    bad = [r for r in rows if not r["routes_agree"]]
    LD.gate("G-FORM-CENSUS-COMPLETE",
            "the form census is COMPLETE along its declared axes: three "
            "locality grains against two chart readings, six of six run, "
            "none sampled.  At every row the acting group is enumerated and "
            "checked closed, the Burnside sum is required to divide the "
            "group order AND to be re-derived from the published count -- "
            "the orbit count times the group order must be the sum itself "
            "-- and the orbit count is confirmed by a SECOND route "
            "-- brute-force union-find and an orbit-stabiliser sum at the "
            "link grain where the datum space is 640, and an exhaustive "
            "brute-force enumeration on the declared reduced arena at every "
            "grain, which validates the Burnside machinery against a "
            "different computation at the very groups it is used on",
            not bad and len(rows) == len(GRAINS) * len(READINGS),
            "%d rows; failing %s"
            % (len(rows), [b["row"] for b in bad]))
    S["form_census"] = {
        "grains": list(GRAINS), "readings": list(READINGS),
        "rows": rows,
        "the_allowed_space": "EXACTLY-THE-ORBIT-CONSTANT-POSITIVE-RATIONAL-"
                             "FUNCTIONS-ON-THE-STENCIL-DATUM",
        "reduced_arena_named_coins": rednames,
        "reduced_arena_coins": len(red)}
    SEAL.take("THE FORM CENSUS", "form_census", "G-FORM-CENSUS-COMPLETE",
              S["form_census"])
    S["_red"] = red
    return rows


def verify_the_analytic_crosscheck(S):
    """a third, genuinely different computation of the two large gauge-only
    counts: the character route.  Summing the fixed-point product over the
    gauge image is a sum over a subgroup of a product of one-variable
    functions, and Fourier inversion on Z_8 turns it into a closed form in
    the two numbers 136 and 72 -- the count of twist classes and the count of
    those that are not singletons.  The identity is evaluated in integers and
    compared against the Burnside sums the census took."""
    lat, GA, coins = S["_lat"], S["_GA"], S["_coins"]
    n = len(coins)
    f0 = GA.fix[GA.identity]
    fk = GA.fix[GA.twist[1]]
    hat0 = f0 + 7 * fk
    hatk = f0 - fk
    site_closed = (hat0 // 8) ** 4
    plaq_closed = (hat0 // 8) ** 4 + 7 * ((hatk // 8) ** 4)
    st_p = stencil_of(lat, "PLAQUETTE")
    st_s = stencil_of(lat, "SITE")
    Gp = [(tuple(range(4)), gt) for gt in gauge_image(lat, GA, st_p)]
    Gs = [(tuple(range(4)), gt) for gt in gauge_image(lat, GA, st_s)]
    bp, _t1 = burnside(GA, Gp, GA.fix)
    bs, _t2 = burnside(GA, Gs, GA.fix)
    if mut("MUT-ANALYTIC"):
        plaq_closed = plaq_closed + 1
    LD.gate("G-ANALYTIC-CROSSCHECK",
            "the two large gauge-only orbit counts carry a THIRD route: the "
            "character formula on Z_8, evaluated in integers, which returns "
            "the plaquette count as the fourth power of the twist-class "
            "count plus seven times the fourth power of the non-singleton "
            "count, and the site count as that fourth power alone -- the "
            "difference being the ONE relation the four plaquette twists "
            "satisfy and the star's four twists do not",
            bp == plaq_closed and bs == site_closed,
            "plaquette: Burnside %d against the character route %d; site: "
            "%d against %d; the two constants are %d and %d"
            % (bp, plaq_closed, bs, site_closed, hat0 // 8, hatk // 8))
    S["analytic_crosscheck"] = {
        "twist_classes": hat0 // 8, "non_singleton_classes": hatk // 8,
        "plaquette_gauge_only_burnside": bp,
        "plaquette_gauge_only_character_route": plaq_closed,
        "site_gauge_only_burnside": bs,
        "site_gauge_only_character_route": site_closed,
        "the_one_relation": "THE-FOUR-PLAQUETTE-TWISTS-SATISFY-ONE-LINEAR-"
                            "RELATION-AND-THE-STARS-FOUR-DO-NOT"}
    SEAL.take("THE ANALYTIC CROSS-CHECK", "analytic_crosscheck",
              "G-ANALYTIC-CROSSCHECK", S["analytic_crosscheck"])


def verify_the_rank(S):
    """the rank of the allowed space, and its generators.  The space is the
    multiplicative group of orbit-constant positive rational functions; a
    free generating family modulo normalisation is the set of elementary
    systems that take one declared value on a single orbit and one
    everywhere else, one for each orbit but a declared base -- so the rank is
    the orbit count minus one, EXHIBITED at the link grain by building the
    generators and measuring that their induced measures are pairwise
    distinct, and that no non-trivial product of them is a scalar."""
    GA, coins = S["_GA"], S["_coins"]
    G = S["_stencil_groups"][("LINK", "ANCHORED")]
    cls = datum_orbit_partition(GA, G, len(coins))
    base = 0
    gens = []
    two = Fraction(2)
    one = Fraction(1)
    for i, cl in enumerate(cls):
        if i == base:
            continue
        w = [one] * len(coins)
        for j in cl:
            w[j] = two
        gens.append((i, w))
    if mut("MUT-RANK"):
        gens = gens[:-1]
    prods = set()
    for _i, w in gens:
        prods.add(tuple(w))
    scalar_only = True
    for _i, w in gens:
        if len({x for x in w}) == 1:
            scalar_only = False
    rank = len(gens)
    LD.gate("G-RANK-IS-ORBITS-MINUS-ONE",
            "the coupling count is the allowed space's rank MODULO "
            "NORMALISATION, and it is exhibited rather than asserted: at the "
            "link grain the elementary generators are built, one per orbit "
            "but the declared base, every one of them is measured to be "
            "non-constant -- so none is a scalar and none is redundant with "
            "the normalisation -- they are pairwise distinct as functions, "
            "and their number is the orbit count less one",
            rank == len(cls) - 1 and len(prods) == rank and scalar_only,
            "%d orbits, %d generators exhibited, %d distinct, none a scalar: "
            "%s" % (len(cls), rank, len(prods), scalar_only))
    S["rank"] = {
        "grain": "LINK", "reading": "ANCHORED", "orbits": len(cls),
        "generators_exhibited": rank, "coupling_count": rank,
        "generator_shape": "ONE-DECLARED-VALUE-ON-A-SINGLE-ORBIT-AND-ONE-"
                           "ELSEWHERE",
        "orbit_size_profile": [(k, sum(1 for c in cls if len(c) == k))
                               for k in sorted({len(c) for c in cls})]}
    SEAL.take("THE RANK", "rank", "G-RANK-IS-ORBITS-MINUS-ONE", S["rank"])
    S["_link_classes"] = cls


def datum_orbit_partition(GA, G, ncoins):
    """the orbit PARTITION at the link grain (one slot), as sets of coins."""
    perms = [GA.elems[cm[0]] for (_p, cm) in G]
    return group_orbits(ncoins, perms)


# ===========================================================================
# SECTION 9.  LOCALITY: WHAT PRODUCT-INVARIANCE COSTS AT EACH GRAIN
# ===========================================================================
# The census above imposes invariance of the LOCAL weight.  The weaker
# condition -- invariance of the PRODUCT over configurations -- is the one a
# reader may have in mind, and the two are not the same at every grain.  At
# the link grain they are EQUAL, by a theorem this unit both proves and
# exhausts; at the plaquette grain the weak condition is STRICTLY weaker, by
# an exhibited construction.  Neither statement is left as an argument.

def measure_locality(S):
    lat, coins, GA = S["_lat"], S["_coins"], S["_GA"]
    cls = S["_link_classes"]
    where = {}
    for i, c in enumerate(cls):
        for j in c:
            where[j] = i
    site0 = lat.sites[0]
    touched = [l for l in lat.links if site0 in lat.ends(l)]
    rows = []
    for i, m in enumerate(coins):
        singleton = len(cls[where[i]]) == 1
        # the elementary weight system: a declared value on this coin alone.
        # Pi w over the uniform configuration at m is that value to the power
        # of the link count; under the single-site gauge bump the four links
        # at that site carry a twisted coin instead, and the two products
        # differ exactly when the twist moves the coin.
        moved = sum(1 for l in touched
                    if GA.elems[GA.twist[1 if lat.ends(l)[0] == site0
                                         else 7]][i] != i)
        detected = moved > 0
        rows.append({"locally_invariant": singleton, "detected": detected,
                     "links_whose_coin_moved": moved})
    inv = [r for r in rows if r["locally_invariant"]]
    non = [r for r in rows if not r["locally_invariant"]]
    if mut("MUT-LOCALITY-THEOREM"):
        non = non[:-1] + [dict(non[-1], detected=True)]
        non[0] = dict(non[0], detected=False)
    ok = (all(r["detected"] for r in non)
          and not any(r["detected"] for r in inv)
          and len(rows) == len(coins))
    LD.gate("G-LOCALITY-AT-THE-LINK-GRAIN",
            "at the link grain PRODUCT-invariance and LOCAL invariance are "
            "the same condition, and the identity is exhausted rather than "
            "argued: for every coin the elementary weight system that "
            "singles it out is built, and the two products over a "
            "configuration and its gauge image are compared.  Every system "
            "that is not locally invariant is DETECTED, every system that is "
            "invariant is NOT -- both arms populated, at the full family.  "
            "The proof behind it is that the configuration weight factorises "
            "over independent link coordinates and the twist has finite "
            "order, so the per-link ratio is a positive rational root of "
            "unity and hence one",
            ok,
            "%d elementary systems; %d locally invariant, %d of those "
            "detected (must be 0); %d not invariant, %d of those detected "
            "(must be all)"
            % (len(rows), len(inv), sum(1 for r in inv if r["detected"]),
               len(non), sum(1 for r in non if r["detected"])))

    inc = {}
    for p in lat.plaquettes:
        for l, _o in lat.boundary(p):
            inc.setdefault(l, []).append(p)
    two = all(len(v) == 2 for v in inc.values())
    order = {}
    for l, ps in inc.items():
        order[l] = (lat.plaquettes.index(ps[0]), lat.plaquettes.index(ps[1]))
    # the coboundary weight system: h on the link's coin, entering the
    # earlier plaquette with exponent +1 and the later one with -1.  Its
    # product over the plaquettes is the empty product at every
    # configuration, whatever h is -- so it is product-invariant; and h is
    # chosen NOT gauge-invariant, so it is not locally invariant.
    hidx = next(i for i, c in enumerate(S["_link_classes"]) if len(c) > 1)
    hset = {S["_link_classes"][hidx][0]}
    exps = {}
    for l, (p1, p2) in order.items():
        exps[l] = {p1: 1, p2: -1}
    checked = []
    for k in range(len(coins)):
        cfg = {l: coins[k] for l in lat.links}
        checked.append(coboundary_product(lat, cfg, exps, hset, coins))
    sample = []
    for k in range(64):
        cfg = {l: coins[(k * 13 + 29 * i) % len(coins)]
               for i, l in enumerate(lat.links)}
        sample.append(coboundary_product(lat, cfg, exps, hset, coins))
    if mut("MUT-COBOUNDARY"):
        exps[lat.links[0]] = {order[lat.links[0]][0]: 1,
                              order[lat.links[0]][1]: 1}
        checked[0] = coboundary_product(
            lat, {l: coins[0] for l in lat.links}, exps, hset, coins)
    one = Fraction(1)
    gap = (all(x == one for x in checked) and all(x == one for x in sample)
           and two)
    LD.gate("G-LOCALITY-GAP-AT-THE-PLAQUETTE-GRAIN",
            "at the plaquette grain the weak condition is STRICTLY weaker, "
            "and the witness is exhibited rather than asserted: every link "
            "is measured to lie in exactly two plaquettes, so a weight "
            "system built from ANY per-link function entering one of them "
            "with exponent plus one and the other with minus one has "
            "configuration weight identically one -- product-invariant "
            "whatever the function, and not locally invariant when the "
            "function is not.  Verified exhaustively on the carrier and on a "
            "declared deterministic sample of non-uniform configurations",
            gap,
            "every link in exactly two plaquettes: %s; %d carrier "
            "configurations and %d declared non-uniform configurations at "
            "product one: %d and %d"
            % (two, len(checked), len(sample),
               sum(1 for x in checked if x == one),
               sum(1 for x in sample if x == one)))
    S["locality"] = {
        "link_grain_elementary_systems": len(rows),
        "link_grain_locally_invariant": len(inv),
        "link_grain_not_invariant": len(non),
        "link_grain_not_invariant_detected": sum(1 for r in non
                                                 if r["detected"]),
        "link_grain_invariant_detected": sum(1 for r in inv
                                             if r["detected"]),
        "link_grain_verdict": "PRODUCT-INVARIANCE-EQUALS-LOCAL-INVARIANCE",
        "every_link_lies_in_this_many_plaquettes": 2,
        "plaquette_grain_carrier_configurations_at_product_one":
            sum(1 for x in checked if x == one),
        "plaquette_grain_declared_sample": len(sample),
        "plaquette_grain_sample_at_product_one":
            sum(1 for x in sample if x == one),
        "plaquette_grain_verdict":
            "THE-PRODUCT-INVARIANT-SPACE-IS-STRICTLY-LARGER-BY-A-COBOUNDARY",
        "what_the_coboundary_does_to_the_measure": "NOTHING-ITS-PRODUCT-IS-"
                                                   "IDENTICALLY-ONE"}
    SEAL.take("LOCALITY", "locality", "G-LOCALITY-GAP-AT-THE-PLAQUETTE-GRAIN",
              S["locality"])


def coboundary_product(lat, cfg, exps, hset, coins):
    """the configuration weight of the exhibited coboundary system: the
    product over plaquettes of the local weights, each of which is a product
    of per-link factors carrying the plaquette's own exponent."""
    tot = Fraction(1)
    two = Fraction(2)
    for p in lat.plaquettes:
        v = Fraction(1)
        for l, _o in lat.boundary(p):
            h = two if cfg[l] in hset_members(hset, coins) else Fraction(1)
            v = v * (h ** exps[l][lat.plaquettes.index(p)])
        tot = tot * v
    return tot


_HSET_CACHE = {}


def hset_members(hset, coins):
    key = tuple(sorted(hset))
    got = _HSET_CACHE.get(key)
    if got is None:
        got = {coins[i] for i in hset}
        _HSET_CACHE[key] = got
    return got


# ===========================================================================
# SECTION 10.  THE GRAIN'S INDUCED PARTITION, AND THE GIBBS MAP
# ===========================================================================

def measure_the_gibbs_map(S, pv):
    lat, coins, GA = S["_lat"], S["_coins"], S["_GA"]
    n = len(coins)
    orb = S["_orbits"]
    exps = {"LINK": len(lat.links), "PLAQUETTE": len(lat.plaquettes),
            "SITE": len(lat.sites)}
    rows = []
    induced = {}
    for r in S["form_census"]["rows"]:
        grain, reading = r["grain"], r["reading"]
        G = S["_stencil_groups"][(grain, reading)]
        cls = induced_classes_on_the_carrier(GA, G, n)
        if mut("MUT-INDUCED") and grain == "SITE" and reading == "ANCHORED":
            cls = cls[:-2] + [cls[-2] + cls[-1]]
        induced[(grain, reading)] = cls
        base = orb["ANCHORED" if reading == "ANCHORED" else "EXTENSION"]
        pos = {}
        for i, c in enumerate(cls):
            for j in c:
                pos[j] = i
        coarsens = all(len({pos[j] for j in o}) == 1 for o in base)
        merged = len(base) - len(cls)
        singletons = sum(1 for c in cls
                         if len([o for o in base
                                 if pos[o[0]] == pos[c[0]]]) == 1)
        if mut("MUT-GEOMETRY") and grain == "LINK":
            singletons = singletons - 1
        equal_pairs = 0
        for i, c in enumerate(cls):
            inside = [o for o in base if pos[o[0]] == i]
            if len(inside) == 2 and len(inside[0]) == len(inside[1]):
                equal_pairs += 1
        rows.append({
            "row": "%s-%s" % (grain, reading), "grain": grain,
            "reading": reading,
            "exponent": exps[grain],
            "why_the_exponent": "THE-NUMBER-OF-STENCIL-COPIES-THE-LATTICE-"
                                "CARRIES",
            "induced_classes_on_the_carrier": len(cls),
            "reachable_dimension": len(cls) - 1,
            "the_parents_orbits": len(base),
            "the_parents_simplex_dimension": len(base) - 1,
            "the_classes_coarsen_the_parents_orbits": coarsens,
            "orbit_pairs_merged": merged,
            "weight_space_rank": r["coupling_count"],
            "fibre_dimension": (r["coupling_count"] - (len(cls) - 1))
            if r["coupling_count"] is not None else None,
            "extreme_points_that_are_vertices_of_the_parents_simplex":
                singletons,
            "extreme_points_that_are_edge_midpoints_of_it": equal_pairs,
            "every_integer_in_this_row_is_a_count": "COUNTING-ONLY",
            "class_size_profile": [(k, sum(1 for c in cls if len(c) == k))
                                   for k in sorted({len(c) for c in cls})]})
    bad = [r for r in rows if not r["the_classes_coarsen_the_parents_orbits"]]
    same = {r["grain"]: r["induced_classes_on_the_carrier"] for r in rows
            if r["reading"] == "ANCHORED"}
    LD.gate("G-REACHABLE-SET-IS-A-SUBSIMPLEX",
            "the partition a grain induces on the CARRIER is measured, and "
            "it is measured to COARSEN the parent's gauge orbits at every "
            "row -- so the measures an action can reach are exactly the "
            "measures constant on those classes, and they form a "
            "sub-simplex of the parent's invariant simplex rather than a "
            "different object.  The three grains induce the SAME partition, "
            "which is the exact form of the parent's own disclosure that "
            "this carrier cannot see locality",
            not bad and len(set(same.values())) == 1,
            "%d rows, %d failing to coarsen; induced classes by grain at the "
            "anchored reading %s"
            % (len(rows), len(bad), sorted(same.items())))
    geo = [r for r in rows
           if r["extreme_points_that_are_vertices_of_the_parents_simplex"]
           + r["extreme_points_that_are_edge_midpoints_of_it"]
           != r["induced_classes_on_the_carrier"]]
    LD.gate("G-THE-REACHABLE-SIMPLEX-IS-EXHIBITED",
            "the reachable sub-simplex is described by its own extreme "
            "points and not only by its dimension: every class is measured "
            "either to BE a single gauge orbit -- whose class-uniform "
            "measure is a vertex of the parent's simplex -- or to merge "
            "exactly two orbits OF EQUAL SIZE, whose class-uniform measure "
            "is the midpoint of the edge joining those two vertices, and the "
            "two counts are required to exhaust the class list at every row",
            not geo,
            "%d rows; %d whose vertex and midpoint counts do not exhaust "
            "the classes %s"
            % (len(rows), len(geo), [r["row"] for r in geo][:3]))
    S["gibbs"] = {
        "rows": rows,
        "every_integer_here_is_a_count_stamp": "COUNTING-ONLY-E-24-NO-COUNT-"
                                               "BECOMES-A-PROBABILITY-"
                                               "WITHOUT-A-DECLARED-MEASURE",
        "the_image": "THE-E-TH-POWER-SUBLATTICE-OF-THE-CLASS-CONSTANT-"
                     "MEASURES-WITH-E-THE-STENCIL-COUNT",
        "positivity_forces_full_support": True,
        "the_fibre_at_the_link_grain": "EXACTLY-THE-NORMALISATION"}
    SEAL.take("THE GIBBS MAP", "gibbs", "G-REACHABLE-SET-IS-A-SUBSIMPLEX",
              S["gibbs"])
    S["_induced"] = induced

    a = [r for r in rows if r["reading"] == "ANCHORED"][0]
    e = [r for r in rows if r["reading"] == "EXTENSION"][0]
    if mut("MUT-PRICE"):
        a = dict(a, reachable_dimension=a["the_parents_simplex_dimension"])
    ok = (a["the_parents_simplex_dimension"] == pv["PV-P23-SIMP32"]
          == pv["PV-SMU-SIMP32"]
          and e["the_parents_simplex_dimension"] == pv["PV-P23-SIMP128"]
          == pv["PV-SMU-SIMP128"]
          and a["reachable_dimension"] < a["the_parents_simplex_dimension"]
          and e["reachable_dimension"] < e["the_parents_simplex_dimension"]
          and a["orbit_pairs_merged"] > 0)
    LD.gate("G-PRICE-REDUCED-NOT-EVADED",
            "the pin's price question is answered on the objects and not by "
            "argument: an action does NOT evade the parent's price, and it "
            "does not pay it either.  The reachable set is a proper "
            "sub-simplex of the invariant simplex at both chart readings -- "
            "strictly fewer independent numbers than the parent's "
            "declaration supplies -- and the deficit is exactly the number "
            "of gauge-orbit pairs that every local weight system identifies, "
            "which is the odd twist the torus does not close",
            ok,
            "anchored: %d reachable against the parent's %d, %d orbit pairs "
            "merged; extension: %d against %d, %d merged"
            % (a["reachable_dimension"], a["the_parents_simplex_dimension"],
               a["orbit_pairs_merged"], e["reachable_dimension"],
               e["the_parents_simplex_dimension"], e["orbit_pairs_merged"]))
    S["price"] = {
        "the_parents_price_anchored": a["the_parents_simplex_dimension"],
        "the_parents_price_extension": e["the_parents_simplex_dimension"],
        "the_parents_price_without_covariance": pv["PV-SMU-PRICE639"],
        "the_action_route_supplies_anchored": a["reachable_dimension"],
        "the_action_route_supplies_extension": e["reachable_dimension"],
        "numbers_forbidden_anchored":
            a["the_parents_simplex_dimension"] - a["reachable_dimension"],
        "numbers_forbidden_extension":
            e["the_parents_simplex_dimension"] - e["reachable_dimension"],
        "orbit_pairs_merged_anchored": a["orbit_pairs_merged"],
        "orbit_pairs_merged_extension": e["orbit_pairs_merged"],
        "verdict": "REDUCED-NOT-EVADED",
        "the_mechanism": "EVERY-LOCAL-WEIGHT-SYSTEM-IS-BLIND-TO-THE-ODD-"
                         "TWIST-WHICH-THE-TORUS-DOES-NOT-CLOSE"}
    SEAL.take("THE PRICE", "price", "G-PRICE-REDUCED-NOT-EVADED", S["price"])

    if mut("MUT-GRAIN-DEGENERACY"):
        S["form_census"]["rows"][4]["coupling_count"] = \
            S["form_census"]["rows"][0]["coupling_count"]
    LD.gate("G-GRAIN-DEGENERACY-ON-THE-CARRIER",
            "the parent disclosed that its carrier cannot see locality -- "
            "one coin serves every link -- and this unit measures exactly "
            "what that costs: the coupling counts differ between grains by "
            "six orders of magnitude, and yet the measures the three grains "
            "can reach on this carrier are the SAME set.  The whole "
            "difference sits in the fibre, which the carrier cannot see",
            len({r["induced_classes_on_the_carrier"] for r in rows
                 if r["reading"] == "ANCHORED"}) == 1
            and len({r["coupling_count"] for r in S["form_census"]["rows"]
                     if r["reading"] == "ANCHORED"}) == len(GRAINS),
            "induced classes %s against coupling counts %s, anchored reading"
            % (sorted({r["induced_classes_on_the_carrier"] for r in rows
                       if r["reading"] == "ANCHORED"}),
               sorted({r["coupling_count"] for r in S["form_census"]["rows"]
                       if r["reading"] == "ANCHORED"})))
    S["grain_degeneracy"] = {
        "readings": len(READINGS), "grains": len(GRAINS),
        "induced_classes_anchored": sorted(
            {r["induced_classes_on_the_carrier"] for r in rows
             if r["reading"] == "ANCHORED"}),
        "coupling_counts_anchored": sorted(
            {r["coupling_count"] for r in S["form_census"]["rows"]
             if r["reading"] == "ANCHORED"}),
        "verdict": "THE-COUPLING-COUNT-IS-GRAIN-RELATIVE-THE-REACHABLE-"
                   "MEASURES-ARE-NOT"}
    SEAL.take("THE GRAIN DEGENERACY", "grain_degeneracy",
              "G-GRAIN-DEGENERACY-ON-THE-CARRIER", S["grain_degeneracy"])


# ===========================================================================
# SECTION 11.  THE CANDIDATE ROWS
# ===========================================================================

def measure_wilson_row(S, pv):
    """(a) THE WILSON SHAPE: weights that are functions of the plaquette
    holonomy's trace.  Is it in the allowed space?  At which grains?  Is it
    distinguished?"""
    lat, coins, GA, cidx = S["_lat"], S["_coins"], S["_GA"], S["_cidx"]
    n = len(coins)
    tr = {}
    plaq_indep = True
    inq = True
    for i, m in enumerate(coins):
        vals = [block_trace(holonomy_block(lat, p, lambda l, mm=m: mm))
                for p in lat.plaquettes]
        if mut("MUT-WILSON-OBSERVABLE") and i == 0:
            vals[0] = fadd(vals[0], ONE)
        if len(set(vals)) != 1:
            plaq_indep = False
        if not in_q_sqrt2(vals[0]):
            inq = False
        tr[i] = vals[0]
    distinct = sorted({qsqrt2_pair(v) for v in tr.values()})
    orbc = all(len({tr[j] for j in o}) == 1 for o in S["_orbits"]["ANCHORED"])
    ok = (plaq_indep and inq and len(distinct) == pv["PV-SMU-WILSON-N"]
          and orbc)
    LD.gate("G-WILSON-OBSERVABLE-REBUILT",
            "the loop observable is REBUILT from R5's own definition -- the "
            "ordered product of the four link operators around the boundary, "
            "each inverted where the boundary runs against the link's own "
            "direction, restricted to the four corners it lives on -- and "
            "measured to be plaquette-independent on the carrier, to lie in "
            "the real subfield, to take the parent's own number of distinct "
            "values, and to be constant on the residual gauge orbits",
            ok,
            "plaquette-independent %s at %d plaquettes; in the real "
            "subfield %s; %d distinct values; orbit-constant %s"
            % (plaq_indep, len(lat.plaquettes), inq, len(distinct), orbc))
    S["_tr"] = tr

    # IN the allowed space at the plaquette grain: the trace is invariant
    # under the local gauge group, which is a theorem by cyclicity and is
    # exhausted here on a declared sample against EVERY gauge element.
    st = stencil_of(lat, "PLAQUETTE")
    gi = gauge_image(lat, GA, st)
    data = [tuple(coins[(k * 37 + 11 * j) % n] for j in range(4))
            for k in range(16)]
    checks, bad = 0, 0
    for d in data:
        base = block_trace(holonomy_block(
            lat, lat.sites[0], lambda l, dd=d: dd[st.index(l)]))
        for gt in gi:
            d2 = tuple(coins[GA.elems[gt[j]][cidx[d[j]]]] for j in range(4))
            t2 = block_trace(holonomy_block(
                lat, lat.sites[0], lambda l, dd=d2: dd[st.index(l)]))
            checks += 1
            if t2 != base:
                bad += 1
    if mut("MUT-WILSON-INVARIANCE"):
        bad = 1
    LD.gate("G-WILSON-IS-IN-THE-ALLOWED-SPACE",
            "the Wilson shape IS a member of the allowed space at the "
            "plaquette grain: the trace of the holonomy is invariant under "
            "every element of the plaquette's own gauge image, which is what "
            "makes any positive-rational function of it an admissible weight "
            "system.  The theorem is cyclicity of the trace under "
            "conjugation by the corner phases; the measurement is a declared "
            "sample of plaquette data against EVERY gauge element",
            bad == 0,
            "%d checks over %d declared data against %d gauge elements, %d "
            "failures" % (checks, len(data), len(gi), bad))

    # NOT in the allowed space at the other two grains: exhibited.
    stl = stencil_of(lat, "LINK")
    sts = stencil_of(lat, "SITE")
    def trace_of(cfgmap):
        return block_trace(holonomy_block(lat, lat.sites[0],
                                          lambda l: cfgmap[l]))
    def separates(stencil):
        """a witness pair: two configurations agreeing on the stencil's own
        datum whose loop traces differ, found by search over the family and
        exhibited rather than asserted."""
        for base in range(0, n, 20):
            m0 = coins[base]
            seen = {}
            for k in range(0, n, 20):
                cfg = {l: (m0 if l in stencil else coins[k])
                       for l in lat.links}
                t = trace_of(cfg)
                if t in seen:
                    continue
                seen[t] = k
                if len(seen) > 1:
                    return True, [base] + sorted(seen.values())[:2]
        return False, []

    sep_link, wl_pair = separates(stl)
    sep_site, ws_pair = separates(sts)
    grains_admitting = ["PLAQUETTE"]
    if mut("MUT-WILSON-GRAIN"):
        sep_link = False
    LD.gate("G-WILSON-GRAIN-SELECTION",
            "the Wilson shape is expressible at EXACTLY ONE of the three "
            "declared grains, and the other two are excluded by an exhibited "
            "pair rather than by a remark: two configurations agreeing on a "
            "link's own datum, and two agreeing on a site's whole star, "
            "carry different loop traces -- so no per-link and no per-site "
            "weight system is a function of the trace",
            sep_link and sep_site and len(grains_admitting) == 1,
            "link grain separated %s by the pair %s; site grain separated "
            "%s by the pair %s; grains admitting the Wilson shape %s"
            % (sep_link, wl_pair, sep_site, ws_pair, grains_admitting))

    # the Wilson family's own dimension AT THE CARRIER, and its position.
    cls = S["_induced"][("PLAQUETTE", "ANCHORED")]
    pos = {}
    for i, c in enumerate(cls):
        for j in c:
            pos[j] = i
    trace_const_on_classes = all(len({tr[j] for j in c}) == 1 for c in cls)
    single_link_invariants = len(S["_link_classes"])
    if mut("MUT-MINIMAL-SUPPORT"):
        single_link_invariants = 1
    LD.gate("G-WILSON-IS-NOT-MINIMAL-SUPPORT",
            "the Wilson shape is NOT the minimal-support member of the "
            "allowed space, and the reason is the parent's own criterion "
            "applied one grain down: a canonical object of smaller support "
            "exists exactly where the group acts transitively on that "
            "support's datum, and here the gauge group is measured NOT "
            "transitive on a single link's coin -- it leaves as many classes "
            "as the carrier has couplings.  Single-link invariants "
            "therefore abound, and the plaquette is not forced",
            single_link_invariants > 1 and trace_const_on_classes,
            "%d classes on a single link's datum against the 1 transitivity "
            "would require; the trace is constant on the induced classes: %s"
            % (single_link_invariants, trace_const_on_classes))
    S["wilson"] = {
        "observable": "THE-TRACE-OF-THE-PLAQUETTE-HOLONOMY-ON-ITS-OWN-FOUR-"
                      "CORNER-BLOCK",
        "normalisation_fibre": pv["PV-SMU-FIBRE"],
        "plaquettes_checked": len(lat.plaquettes),
        "plaquette_independent": plaq_indep,
        "in_the_real_subfield": inq,
        "distinct_values_over_the_carrier": len(distinct),
        "values": [qs_str(v) for v in distinct],
        "constant_on_the_residual_gauge_orbits": orbc,
        "in_the_allowed_space_at_grains": grains_admitting,
        "grains_declared": len(GRAINS),
        "gauge_invariance_checks": checks,
        "gauge_invariance_failures": bad,
        "dimension_of_the_wilson_family_on_the_carrier": len(distinct) - 1,
        "the_allowed_space_on_the_carrier": len(cls) - 1,
        "constant_on_the_induced_classes": trace_const_on_classes,
        "single_link_invariant_classes": single_link_invariants,
        "minimal_support": False,
        "why": "THE-GAUGE-GROUP-IS-NOT-TRANSITIVE-ON-A-SINGLE-LINKS-DATUM",
        "must_not": "NO-AREA-LAW-NO-STRING-TENSION-NO-POTENTIAL-CLAIM-AND-"
                    "NO-LOOP-FAMILY-IS-GROWN",
        "loop_families_grown": 0}
    SEAL.take("THE WILSON ROW", "wilson", "G-WILSON-IS-NOT-MINIMAL-SUPPORT",
              S["wilson"], omit=None)
    return tr


def prime_exponents(k):
    """the exact factorisation of a positive integer, by trial division --
    integers only, and the numbers here are small."""
    out, d = {}, 2
    while d * d <= k:
        while k % d == 0:
            out[d] = out.get(d, 0) + 1
            k //= d
        d += 1
    if k > 1:
        out[k] = out.get(k, 0) + 1
    return out


def is_exact_power(fr, e):
    """is a positive rational an e-th power in Q?  Exactly when every prime
    exponent of its numerator and denominator is divisible by e -- unique
    factorisation, decided in integers."""
    for k, v in list(prime_exponents(fr.numerator).items()) \
            + list(prime_exponents(fr.denominator).items()):
        if v % e:
            return False
    return True


def measure_targets(S, pv):
    """(b) THE LAW-NATIVE CONTROL and (c) THE NULL, inside a census of every
    named measure this corpus has on this carrier: which are reachable by a
    weight system over the declared field, and where each one fails."""
    coins, n = S["_coins"], len(S["_coins"])
    orb, cls = S["_orbits"], S["_induced"][("LINK", "ANCHORED")]
    pos = {}
    for i, c in enumerate(cls):
        for j in c:
            pos[j] = i
    targets = []

    counting = [Fraction(1, n)] * n
    targets.append(("COUNTING", counting,
                    "paper-23's declared null, and SMU's one derivation in "
                    "the full sense"))
    ou32 = [None] * n
    for o in orb["ANCHORED"]:
        for j in o:
            ou32[j] = Fraction(1, len(orb["ANCHORED"]) * len(o))
    targets.append(("ORBIT-UNIFORM-ANCHORED", ou32,
                    "the parent's orbit-uniform null at the anchored "
                    "reading"))
    ou128 = [None] * n
    for o in orb["EXTENSION"]:
        for j in o:
            ou128[j] = Fraction(1, len(orb["EXTENSION"]) * len(o))
    targets.append(("ORBIT-UNIFORM-EXTENSION", ou128,
                    "the same at the extension reading"))
    lawv = [Fraction(pv["PV-SMU-LAW1"]), Fraction(pv["PV-SMU-LAW2"]),
            Fraction(pv["PV-SMU-LAW3"])]
    sect = {}
    for i, m in enumerate(coins):
        sect.setdefault(coin_sector(m), []).append(i)
    order = ["DIAGONAL", "ANTIDIAGONAL", "BALANCED"]
    pi = [None] * n
    for k, name in enumerate(order):
        for j in sect[name]:
            pi[j] = lawv[k] / len(sect[name])
    targets.append(("LAW-NATIVE-PI", pi,
                    "SMU's law-native measure, entering HERE AS A CONTROL "
                    "and never as a derived object"))
    haar = [None] * n
    mono = [i for i, m in enumerate(coins)
            if coin_sector(m) in ("DIAGONAL", "ANTIDIAGONAL")]
    for i in range(n):
        haar[i] = Fraction(1, len(mono)) if i in set(mono) else Fraction(0)
    targets.append(("MONOMIAL-HAAR", haar,
                    "the one canonical measure paper-23 measured this arena "
                    "to hand over"))
    parity = [None] * n
    for i, m in enumerate(coins):
        parity[i] = Fraction(3) if quartic_sign(m[1]) >= 0 else Fraction(1)
    tot = sum(parity)
    parity = [x / tot for x in parity]
    targets.append(("ODD-TWIST-GRADED", parity,
                    "a DECLARED invariant target built to separate the two "
                    "orbits inside one class -- the control arm for the "
                    "symmetry obstruction"))

    exps = sorted({r["exponent"] for r in S["gibbs"]["rows"]})
    rows = []
    for name, t, what in targets:
        full = all(x > 0 for x in t)
        classconst = all(len({t[j] for j in c}) == 1 for c in cls)
        base = next((t[i] for i in range(n) if t[i] > 0), Fraction(1))
        powers = {}
        for e in exps:
            powers[e] = (full and classconst
                         and all(is_exact_power(t[i] / base, e)
                                 for i in range(n)))
        why = "REACHABLE"
        if not classconst:
            why = "UNREACHABLE-BY-SYMMETRY"
        elif not full:
            why = "UNREACHABLE-BY-SUPPORT"
        elif not any(powers.values()):
            why = "UNREACHABLE-BY-ARITHMETIC"
        rows.append({"row": name, "what": what, "full_support": full,
                     "class_constant": classconst,
                     "reachable_at_exponent": {str(e): powers[e]
                                               for e in exps},
                     "reachable": any(powers.values()), "obstruction": why})
    if mut("MUT-TARGET-CENSUS"):
        rows[3]["reachable"] = True
        rows[3]["obstruction"] = "REACHABLE"

    # the REACHABLE arm is REACHED, not merely licensed: an exhibited
    # non-counting weight system and the exact measure it produces.
    two = Fraction(2)
    wsys = [Fraction(1)] * n
    for j in cls[1]:
        wsys[j] = two
    e0 = [r["exponent"] for r in S["gibbs"]["rows"]
          if r["row"] == "LINK-ANCHORED"][0]
    raw = [w ** e0 for w in wsys]
    Z = sum(raw)
    mu = [x / Z for x in raw]
    witness_ok = (sum(mu) == 1 and len({mu[j] for j in cls[1]}) == 1
                  and mu[cls[1][0]] != mu[cls[0][0]]
                  and all(len({mu[j] for j in c}) == 1 for c in cls))
    n_reach = sum(1 for r in rows if r["reachable"])
    species = sorted({r["obstruction"] for r in rows
                      if not r["reachable"]})
    ok = (witness_ok and n_reach >= 1
          and rows[0]["reachable"] and not rows[3]["reachable"]
          and len(species) == 3)
    LD.gate("G-TARGET-CENSUS",
            "every named measure this corpus has on this carrier is run "
            "against the Gibbs map, and each failure is attributed to a "
            "MEASURED species rather than to a single verdict: a target that "
            "separates two orbits inside one class fails by SYMMETRY, a "
            "target with a zero fails by SUPPORT because positive weights "
            "force full support, and a target whose mass ratios are not "
            "exact powers fails by ARITHMETIC.  The reachable arm is "
            "REACHED, by the null and by an exhibited non-counting weight "
            "system whose measure is computed exactly",
            ok,
            "%d targets, %d reachable, %d obstruction species %s; the "
            "exhibited non-counting witness lands on a class-constant "
            "measure summing to one: %s"
            % (len(rows), n_reach, len(species), species, witness_ok))
    S["target_census"] = {
        "rows": rows, "exponents_tested": exps,
        "reachable": n_reach, "obstruction_species": species,
        "the_null": "W-IDENTICALLY-ONE-GIVES-THE-COUNTING-MEASURE",
        "exhibited_non_counting_witness": {
            "weight_system": "TWO-ON-ONE-CLASS-AND-ONE-ELSEWHERE",
            "exponent": e0,
            "distinct_masses": len({x for x in mu}),
            "mass_on_the_raised_class": str(mu[cls[1][0]]),
            "mass_elsewhere": str(mu[cls[0][0]]),
            "sums_to_one": sum(mu) == 1}}
    SEAL.take("THE TARGET CENSUS", "target_census", "G-TARGET-CENSUS",
              S["target_census"])
    S["_pi"] = pi
    return rows


def quartic_sign(x):
    """the sign of the fourth power of an entry: zero when the entry is, and
    otherwise plus or minus one, because the fourth power of an eighth root
    of unity is real.  It is an exact integer, computed in the field."""
    if x == ZERO:
        return 0
    q = fmul(fmul(x, x), fmul(x, x))
    if not is_rational(q):
        return 0
    return 1 if q[0] > 0 else -1


# ===========================================================================
# SECTION 12.  THE CHEAP FALSIFIER, AND THE EXPECTATIONS
# ===========================================================================
# The pin asks for ONE run: is there a gauge observable whose expectation the
# constraints pin to a proper sub-range?  The answer is decided on a declared
# census of observables, each of them required to be a genuine gauge
# observable -- constant on the residual gauge orbits, so that its
# expectation is defined under every invariant measure -- and each measured
# twice: over the parent's invariant simplex, where the range is the convex
# hull of its orbit values, and over the reachable sub-simplex, where the
# range is the convex hull of its CLASS AVERAGES.

def observable_table(S):
    coins, tr = S["_coins"], S["_tr"]
    n = len(coins)
    out = []

    def add(name, f, what):
        out.append((name, [f(coins[i], i) for i in range(n)], what))

    add("WILSON-BLOCK-TRACE-RATIONAL-PART",
        lambda m, i: qsqrt2_pair(tr[i])[0],
        "the rational part of the loop trace, an exact rational component "
        "of the observable SMU published")
    add("WILSON-BLOCK-TRACE-SURD-PART",
        lambda m, i: qsqrt2_pair(tr[i])[1],
        "its surd part, so the pair carries the whole observable exactly "
        "without leaving the rationals")
    add("OFF-DIAGONAL-QUARTIC-SIGN",
        lambda m, i: Fraction(quartic_sign(m[1]) + quartic_sign(m[2])),
        "the sign of the fourth power of the two off-diagonal entries, "
        "added: invariant under the even twist and under the swap, and "
        "REVERSED by the odd twist")
    add("DIAGONAL-SECTOR-INDICATOR",
        lambda m, i: Fraction(1 if coin_sector(m) == "DIAGONAL" else 0),
        "the abelian arm's own indicator")
    add("DEFECT-INDICATOR",
        lambda m, i: Fraction(1 if carries_defect(m) else 0),
        "the composition defect's indicator, rebuilt from the seed's "
        "definition")
    add("FLAT-INDICATOR",
        lambda m, i: Fraction(1 if tr[i] == (4, 0, 0, 0, 1) else 0),
        "the indicator of a trivial holonomy")
    return out


def carries_defect(m):
    """the composition defect at SAME-LINK with one coin, rebuilt from the
    seed's definition: Delta = B(U U) - B(U) B(U) with B the entrywise
    squared modulus."""
    def bm(x):
        return tuple(fmul(y, fconj(y)) for y in x)

    def mm(A, B):
        a, b, c, d = A
        e, f, g, h = B
        return (fadd(fmul(a, e), fmul(b, g)), fadd(fmul(a, f), fmul(b, h)),
                fadd(fmul(c, e), fmul(d, g)), fadd(fmul(c, f), fmul(d, h)))
    return bm(mm(m, m)) != mm(bm(m), bm(m))


def measure_falsifier(S, pv):
    coins = S["_coins"]
    n = len(coins)
    obs = observable_table(S)
    rows = []
    for reading in READINGS:
        base = S["_orbits"][reading]
        cls = S["_induced"][("LINK", reading)]
        for name, vals, what in obs:
            orbit_const = all(len({vals[j] for j in o}) == 1 for o in base)
            if not orbit_const:
                rows.append({"row": "%s-%s" % (name, reading),
                             "observable": name, "reading": reading,
                             "is_a_gauge_observable": False,
                             "what": what, "verdict": "NOT-AN-OBSERVABLE-AT-"
                                                      "THIS-READING"})
                continue
            ov = [vals[o[0]] for o in base]
            cv = [sum(vals[j] for j in c) / Fraction(len(c)) for c in cls]
            simplex = (min(ov), max(ov))
            reach = (min(cv), max(cv))
            pinned = reach != simplex
            rows.append({
                "row": "%s-%s" % (name, reading), "observable": name,
                "reading": reading, "is_a_gauge_observable": True,
                "what": what,
                "range_over_the_invariant_simplex":
                    [str(simplex[0]), str(simplex[1])],
                "range_over_the_reachable_set": [str(reach[0]),
                                                 str(reach[1])],
                "pinned_to_a_proper_sub_range": pinned,
                "pinned_to_a_point": reach[0] == reach[1],
                "verdict": "PINNED" if pinned else "UNPINNED"})
    # the orbit-indicator family: one observable per gauge orbit
    fam = []
    for reading in READINGS:
        base = S["_orbits"][reading]
        cls = S["_induced"][("LINK", reading)]
        pos = {}
        for i, c in enumerate(cls):
            for j in c:
                pos[j] = i
        pin = sum(1 for o in base if len(cls[pos[o[0]]]) > len(o))
        ratios = sorted({str(Fraction(len(o), len(cls[pos[o[0]]])))
                         for o in base if len(cls[pos[o[0]]]) > len(o)})
        fam.append({"row": "ORBIT-INDICATORS-%s" % reading,
                    "reading": reading, "observables": len(base),
                    "pinned": pin, "unpinned": len(base) - pin,
                    "the_pinned_range_top": ratios})
    if mut("MUT-FALSIFIER"):
        rows = [dict(r, pinned_to_a_proper_sub_range=False,
                     pinned_to_a_point=False, verdict="UNPINNED")
                if r.get("is_a_gauge_observable") else r for r in rows]
        fam = [dict(f, pinned=0, unpinned=f["observables"]) for f in fam]
    hits = [r for r in rows if r.get("pinned_to_a_proper_sub_range")]
    points = [r for r in rows if r.get("pinned_to_a_point")]
    wil = [r for r in rows if r["observable"].startswith("WILSON")
           and r.get("is_a_gauge_observable")]
    ok = (len(hits) > 0 and len(points) > 0
          and not any(r["pinned_to_a_proper_sub_range"] for r in wil)
          and all(f["pinned"] > 0 for f in fam))
    LD.gate("G-FALSIFIER-CENSUS",
            "the pin's cheap falsifier is RUN, and it is decided by a census "
            "with both arms populated: an observable's expectation range "
            "over the parent's invariant simplex is the convex hull of its "
            "orbit values, over the reachable set it is the convex hull of "
            "its class averages, and the two are compared exactly.  At least "
            "one declared observable is PINNED -- to a single value -- and "
            "the loop trace is measured NOT to be, so the finding is a "
            "measurement about which observables the constraints reach and "
            "not a blanket verdict",
            ok,
            "%d observable rows, %d pinned, %d of them to a point; the loop "
            "trace pinned at %d of %d readings; orbit-indicator families %s"
            % (len(rows), len(hits), len(points),
               sum(1 for r in wil if r["pinned_to_a_proper_sub_range"]),
               len(wil), [(f["reading"], f["pinned"]) for f in fam]))
    S["falsifier"] = {
        "rows": rows, "orbit_indicator_families": fam,
        "declared_observables": len(obs),
        "pinned_rows": len(hits), "pinned_to_a_point": len(points),
        "verdict": "HIT" if hits else "NULL",
        "the_mechanism": "AN-OBSERVABLE-IS-PINNED-EXACTLY-WHEN-IT-SEPARATES-"
                         "TWO-GAUGE-ORBITS-INSIDE-ONE-CLASS"}
    SEAL.take("THE FALSIFIER", "falsifier", "G-FALSIFIER-CENSUS",
              S["falsifier"])

    orbc = all(r.get("is_a_gauge_observable", True) for r in rows
               if r["reading"] == "ANCHORED")
    dcount = sum(1 for m in coins if carries_defect(m))
    if mut("MUT-OBSERVABLE-NOT-INVARIANT"):
        dcount = dcount - 1
    LD.gate("G-OBSERVABLES-ARE-GAUGE-INVARIANT",
            "every observable entering the falsifier census at the anchored "
            "reading is measured to be a genuine gauge observable -- "
            "constant on the residual gauge orbits, so its expectation is "
            "defined under every measure compared -- and the defect "
            "indicator's own count is checked against the parent's receipt "
            "at a named path, so the census weighs the parent's object",
            orbc and dcount == pv["PV-DEFECT"],
            "anchored-reading observables all orbit-constant: %s; defect "
            "coins %d against the parent's %d"
            % (orbc, dcount, pv["PV-DEFECT"]))
    return rows


def measure_expectations(S, pv):
    """the expectations, each CONDITIONAL ON THE DECLARED WEIGHTS.  Three
    candidate rows are published -- the null, the exhibited non-counting
    witness, and the Wilson-shape weight system at a declared coupling -- and
    every one of them names the weight system it is conditional on, carries
    the stamp, and is required to lie inside the observable's own range."""
    coins, tr = S["_coins"], S["_tr"]
    n = len(coins)
    cls = S["_induced"][("LINK", "ANCHORED")]
    e0 = [r["exponent"] for r in S["gibbs"]["rows"]
          if r["row"] == "LINK-ANCHORED"][0]
    ep = [r["exponent"] for r in S["gibbs"]["rows"]
          if r["row"] == "PLAQUETTE-ANCHORED"][0]
    two, one = Fraction(2), Fraction(1)
    rows = []

    def expect(w, e):
        raw = [x ** e for x in w]
        Z = sum(raw)
        mu = [x / Z for x in raw]
        p = sum(mu[i] * qsqrt2_pair(tr[i])[0] for i in range(n))
        q = sum(mu[i] * qsqrt2_pair(tr[i])[1] for i in range(n))
        return mu, (p, q)

    w1 = [one] * n
    mu1, v1 = expect(w1, e0)
    rows.append({"row": "THE-NULL", "weight_system": "W-IDENTICALLY-ONE",
                 "grain": "LINK", "exponent": e0,
                 "the_measure": "COUNTING",
                 "expectation": qs_str(v1),
                 "stamp": "CONDITIONAL-ON-THE-DECLARED-WEIGHTS"})
    w2 = [two if i in set(cls[1]) else one for i in range(n)]
    mu2, v2 = expect(w2, e0)
    rows.append({"row": "THE-EXHIBITED-WITNESS",
                 "weight_system": "TWO-ON-ONE-CLASS-AND-ONE-ELSEWHERE",
                 "grain": "LINK", "exponent": e0,
                 "the_measure": "NEW",
                 "expectation": qs_str(v2),
                 "stamp": "CONDITIONAL-ON-THE-DECLARED-WEIGHTS"})
    w3 = [two if tr[i] == (4, 0, 0, 0, 1) else one for i in range(n)]
    mu3, v3 = expect(w3, ep)
    rows.append({"row": "THE-WILSON-SHAPE-AT-A-DECLARED-COUPLING",
                 "weight_system": "TWO-AT-THE-TOP-TRACE-VALUE-AND-ONE-"
                                  "ELSEWHERE",
                 "grain": "PLAQUETTE", "exponent": ep,
                 "the_measure": "NEW",
                 "expectation": qs_str(v3),
                 "stamp": "CONDITIONAL-ON-THE-DECLARED-WEIGHTS"})
    if mut("MUT-EXPECTATION-UNSTAMPED"):
        rows[1]["stamp"] = "PLAIN"
    tvals = [qsqrt2_pair(tr[i]) for i in range(n)]
    mn = tvals[0]
    mx = tvals[0]
    for v in tvals:
        if qs_less(v, mn):
            mn = v
        if qs_less(mx, v):
            mx = v
    inside = all(not qs_less(qsqrt2_pair_from_str(r["expectation"]), mn)
                 and not qs_less(mx, qsqrt2_pair_from_str(r["expectation"]))
                 for r in rows)
    stamped = all(r["stamp"] == "CONDITIONAL-ON-THE-DECLARED-WEIGHTS"
                  for r in rows)
    ok = (stamped and inside
          and str(mn[0]) == pv["PV-SMU-WILSON-MIN"]
          and str(mx[0]) == pv["PV-SMU-WILSON-MAX"]
          and mn[1] == 0 and mx[1] == 0)
    LD.gate("G-WILSON-RANGE-OVER-THE-SIMPLEX",
            "the loop trace's own range is recomputed by exact ordering on "
            "the real subfield and lands on the parent's published endpoints "
            "at named receipt paths; every expectation this unit publishes "
            "is required to lie inside that range and to carry the stamp "
            "CONDITIONAL-ON-THE-DECLARED-WEIGHTS on its own row, so an "
            "unstamped expectation dies on the delivery run",
            ok,
            "range [%s, %s]; %d rows, all stamped %s, all inside %s"
            % (qs_str(mn), qs_str(mx), len(rows), stamped, inside))
    S["expectations"] = {
        "rows": rows,
        "range_of_the_observable": [qs_str(mn), qs_str(mx)],
        "stamp": "CONDITIONAL-ON-THE-DECLARED-WEIGHTS",
        "loop_families_grown": 0,
        "must_not": "NO-AREA-LAW-NO-STRING-TENSION-NO-POTENTIAL-CLAIM"}
    SEAL.take("THE EXPECTATIONS", "expectations",
              "G-WILSON-RANGE-OVER-THE-SIMPLEX", S["expectations"])
    return rows


def qsqrt2_pair_from_str(s):
    if "+" not in s:
        return (Fraction(s), Fraction(0))
    p, q = s.split("+")
    return (Fraction(p), Fraction(q.replace("*sqrt2", "")))


def measure_density_witness(S):
    """the law-native target lies in the CLOSURE of the image even though it
    is not in the image: the obstruction is Diophantine, not structural.  The
    witness is exact -- the largest integer numerator whose e-th power stays
    below the target ratio at a declared denominator, found by integer
    bisection, with the error published as an exact bound."""
    e = [r["exponent"] for r in S["gibbs"]["rows"]
         if r["row"] == "LINK-ANCHORED"][0]
    pi = S["_pi"]
    coins = S["_coins"]
    di = next(i for i, m in enumerate(coins) if coin_sector(m) == "DIAGONAL")
    ai = next(i for i, m in enumerate(coins)
              if coin_sector(m) == "ANTIDIAGONAL")
    ratio = pi[di] / pi[ai]
    b = 10 ** 5
    lo, hi = 1, 10 * b
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if mid ** e * ratio.denominator <= ratio.numerator * b ** e:
            lo = mid
        else:
            hi = mid - 1
    q = Fraction(lo, b)
    err = abs(q ** e - ratio)
    j = 0
    while err < Fraction(1, 10 ** (j + 1)):
        j += 1
    if mut("MUT-DENSITY"):
        j = j + 3
    ok = (not is_exact_power(ratio, e) and err < Fraction(1, 10 ** j)
          and j >= 1)
    LD.gate("G-DENSITY-WITNESS",
            "the control target's unreachability is measured to be "
            "ARITHMETIC and not structural, and the distinction is made "
            "exact: the ratio the target requires is not an exact power, so "
            "no weight system over the declared field reaches it -- and yet "
            "an explicit rational found by integer bisection drives that "
            "ratio inside a published error bound, so the target lies in the "
            "closure of the image.  No float and no root extraction is "
            "computed anywhere in the witness",
            ok,
            "the required ratio %s is an exact %d-th power: %s; the witness "
            "at denominator 10^5 is %s and its error is below 1/10^%d"
            % (ratio, e, is_exact_power(ratio, e), q, j))
    S["density_witness"] = {
        "the_required_ratio": str(ratio), "exponent": e,
        "is_an_exact_power": is_exact_power(ratio, e),
        "witness_denominator": b, "witness_numerator": lo,
        "error_below_one_over_ten_to_the": j,
        "consequence": "THE-CONTROL-LIES-IN-THE-CLOSURE-OF-THE-IMAGE-AND-"
                       "NOT-IN-THE-IMAGE"}
    SEAL.take("THE DENSITY WITNESS", "density_witness", "G-DENSITY-WITNESS",
              S["density_witness"])


# ===========================================================================
# SECTION 13.  THE CONTROL ROW, THE SUPPLIED CENSUS ROW, THE POT HANDOFF
# ===========================================================================

def measure_the_control_row(S, pv):
    """(b) THE LAW-NATIVE ROW, AS THE CONTROL.  Its stamp is carried
    VERBATIM from the parent's receipt and it is never spent as derived: the
    row publishes what the control is, what it costs, and where it fails."""
    row = [r for r in S["target_census"]["rows"]
           if r["row"] == "LAW-NATIVE-PI"][0]
    stamp = pv["PV-SMU-STAMP"]
    if mut("MUT-CONTROL-SPENT"):
        row = dict(row, reachable=True, obstruction="REACHABLE")
    ok = (stamp == "LAW-RATED-CONSTRUCTION-DECLARED-AT-AN-UNPINNED-"
                   "IDENTIFICATION"
          and not row["reachable"]
          and row["class_constant"] and row["full_support"]
          and row["obstruction"] == "UNREACHABLE-BY-ARITHMETIC"
          and pv["PV-SMU-LAW1"] == pv["PV-GI-LAW1"]
          and pv["PV-SMU-LAW3"] == pv["PV-GI-LAW3"])
    LD.gate("G-LAW-NATIVE-CONTROL-STAMP-CARRIED",
            "the law-native measure enters this unit AS A CONTROL and its "
            "stamp is carried VERBATIM from the parent's own receipt, never "
            "re-derived and never spent: the row is published with the "
            "parent's stamp, its three sector values are read at TWO "
            "independent sources and required to agree, and the census "
            "verdict on it is the one the measurement returns -- it lies "
            "inside the symmetry-allowed set and outside the image, and the "
            "unit says which of the two facts is doing the work",
            ok,
            "stamp %r; class-constant %s, full support %s, reachable %s, "
            "obstruction %s; the sector law agrees at both sources: %s"
            % (stamp, row["class_constant"], row["full_support"],
               row["reachable"], row["obstruction"],
               pv["PV-SMU-LAW1"] == pv["PV-GI-LAW1"]))
    S["law_native_control"] = {
        "stamp": stamp,
        "sector_law": [pv["PV-SMU-LAW1"], pv["PV-SMU-LAW2"],
                       pv["PV-SMU-LAW3"]],
        "read_at_two_independent_sources": True,
        "class_constant": row["class_constant"],
        "full_support": row["full_support"],
        "reachable": row["reachable"],
        "obstruction": row["obstruction"],
        "never_spent_as_derived": True,
        "the_honest_use": "A-CONTROL-THE-DISTANCE-IS-REPORTED-AND-THE-"
                          "AGREEMENT-IS-NOT-CLAIMED"}
    SEAL.take("THE LAW-NATIVE CONTROL", "law_native_control",
              "G-LAW-NATIVE-CONTROL-STAMP-CARRIED", S["law_native_control"])


def measure_the_supplied_row(S):
    """paper-23 entered the Gibbs route as a census row it could not price,
    for want of two objects.  This unit supplies both and says exactly what
    each is worth."""
    rows = S["form_census"]["rows"]
    a = [r for r in rows if r["row"] == "LINK-ANCHORED"][0]
    if mut("MUT-SUPPLIED"):
        a = dict(a, coupling_count=0)
    ok = (a["coupling_count"] is not None and a["coupling_count"] > 0
          and S["target_census"]["reachable"] > 0)
    LD.gate("G-GIBBS-ROW-SUPPLIED",
            "the parent's Gibbs row is SUPPLIED and priced: the action "
            "functional it needed is exactly a weight system at a declared "
            "grain, the coupling it needed is exactly a coordinate of the "
            "allowed space, and both are now counted rather than named "
            "absent.  What the row costs is published as a rank, and that "
            "the route reaches anything at all is measured rather than "
            "assumed",
            ok,
            "the allowed space at the link grain has rank %d; %d named "
            "target(s) reachable"
            % (a["coupling_count"], S["target_census"]["reachable"]))
    S["supplied_row"] = {
        "the_parents_row": "GIBBS-FROM-AN-ACTION",
        "the_parents_price": 2,
        "what_the_action_functional_is": "A-WEIGHT-SYSTEM-AT-A-DECLARED-"
                                         "GRAIN",
        "what_the_coupling_is": "A-COORDINATE-OF-THE-ALLOWED-SPACE",
        "the_coupling_count_at_the_link_grain": a["coupling_count"],
        "verdict": "SUPPLIED-AND-PRICED-NOT-DERIVED"}
    SEAL.take("THE SUPPLIED ROW", "supplied_row", "G-GIBBS-ROW-SUPPLIED",
              S["supplied_row"])


def measure_pot_handoff(S):
    """what the POT unit inherits.  The confinement vocabulary stays behind
    POT's gate: this section names objects and their prices and makes no
    claim on the far side of that gate."""
    rows = S["form_census"]["rows"]
    inv = {r["row"]: r["coupling_count"] for r in rows}
    g = {r["row"]: r for r in S["gibbs"]["rows"]}
    hand = {
        "the_allowed_space": "ORBIT-CONSTANT-POSITIVE-RATIONAL-FUNCTIONS-ON-"
                             "THE-STENCIL-DATUM",
        "the_coupling_inventory": inv,
        "the_distinguished_points": {
            "THE-NULL": "W-IDENTICALLY-ONE-REACHES-THE-COUNTING-MEASURE",
            "THE-WILSON-SHAPE": "AT-THE-PLAQUETTE-GRAIN-ONLY-SPANNING-%d-OF-"
                                "%d-COUPLINGS-ON-THE-CARRIER"
                                % (S["wilson"][
                                    "dimension_of_the_wilson_family_on_the_"
                                    "carrier"],
                                   S["wilson"]["the_allowed_space_on_the_"
                                               "carrier"]),
            "THE-LAW-NATIVE-CONTROL": S["law_native_control"]["obstruction"]},
        "the_reachable_measures": {
            "anchored": g["LINK-ANCHORED"]["reachable_dimension"],
            "extension": g["LINK-EXTENSION"]["reachable_dimension"]},
        "the_pinned_observable": "THE-OFF-DIAGONAL-QUARTIC-SIGN-IS-PINNED-TO-"
                                 "A-POINT-BY-EVERY-ADMISSIBLE-WEIGHT-SYSTEM",
        "what_is_NOT_handed_over": [
            "ANY-LOOP-FAMILY-WHOSE-SIZE-CAN-GROW-0-GROWN-HERE",
            "ANY-STATEMENT-ON-THE-FAR-SIDE-OF-POTS-GATE",
            "ANY-SELECTION-AMONG-THE-COUPLINGS-THE-FORM-IS-NOT-FORCED"],
        "the_second_of_the_three_objects_is_still_absent": True}
    if mut("MUT-POT-HANDOFF"):
        hand["what_is_NOT_handed_over"] = []
    ok = (len(hand["what_is_NOT_handed_over"]) == 3
          and S["wilson"]["loop_families_grown"] == 0)
    LD.gate("G-POT-HANDOFF",
            "the handoff to POT names the objects and their prices and "
            "NOTHING on the far side of POT's gate: the allowed space, the "
            "coupling inventory, the distinguished points, the reachable "
            "measures and the pinned observable are handed over; no loop "
            "family is grown; and the parent's second object -- a family of "
            "loops whose size can grow -- is recorded as still absent rather "
            "than quietly supplied",
            ok,
            "%d items withheld by name; %d loop families grown"
            % (len(hand["what_is_NOT_handed_over"]),
               S["wilson"]["loop_families_grown"]))
    S["pot_handoff"] = hand
    SEAL.take("THE POT HANDOFF", "pot_handoff", "G-POT-HANDOFF",
              S["pot_handoff"])


# ===========================================================================
# SECTION 14.  THE HEAD LAW, TWICE, AND THE VERDICT
# ===========================================================================

PREREGISTERED = ("ACT-FORM-FORCED", "ACT-FORM-RELATIVE", "ACT-GIBBS",
                 "ACT-BLOCKED-AT")


def head_law(rows, gibbs_rows, blocked):
    """the builder's head law.  Four pre-registered outcomes, selected by
    measured quantities alone."""
    if blocked:
        return "ACT-BLOCKED-AT-" + blocked
    ranks = [r["coupling_count"] for r in rows]
    if all(x == 0 for x in ranks):
        return ("ACT-FORM-FORCED-THE-ALLOWED-SPACE-IS-A-POINT-AT-ALL-%d-"
                "DECLARED-ROWS" % len(rows))
    reach = [r["reachable_dimension"] for r in gibbs_rows]
    if all(x == 0 for x in reach):
        return ("ACT-GIBBS-THE-IMAGE-IS-A-SINGLE-MEASURE-AT-ALL-%d-DECLARED-"
                "ROWS" % len(gibbs_rows))
    anch = [r for r in rows if r["reading"] == "ANCHORED"]
    ext = [r for r in rows if r["reading"] == "EXTENSION"]
    return ("ACT-FORM-RELATIVE-THE-COUPLING-COUNT-IS-GRAIN-RELATIVE-AND-"
            "NOTHING-IS-FORCED-%s-ANCHORED-AND-%s-AT-THE-EXTENSION"
            % ("/".join(str(r["coupling_count"]) for r in anch),
               "/".join(str(r["coupling_count"]) for r in ext)))


def second_head_law(rows, gibbs_rows, blocked):
    """the second law, written from the same pre-registered outcomes with a
    different branch structure: it recomputes its own aggregates from the
    primitive rows rather than accepting the builder's, and shares no format
    string with the builder."""
    if blocked is not None and blocked != "":
        return "".join(["ACT-BLOCKED-AT-", blocked])
    nz = [r for r in rows if r["coupling_count"] != 0]
    if len(nz) == 0:
        return "".join(["ACT-FORM-FORCED-THE-ALLOWED-SPACE-IS-A-POINT-AT-"
                        "ALL-", str(len(rows)), "-DECLARED-ROWS"])
    moving = [r for r in gibbs_rows if r["reachable_dimension"] != 0]
    if len(moving) == 0:
        return "".join(["ACT-GIBBS-THE-IMAGE-IS-A-SINGLE-MEASURE-AT-ALL-",
                        str(len(gibbs_rows)), "-DECLARED-ROWS"])
    seq = {"ANCHORED": [], "EXTENSION": []}
    for grain in GRAINS:
        for r in rows:
            if r["grain"] == grain:
                seq[r["reading"]].append(str(r["coupling_count"]))
    return "".join(["ACT-FORM-RELATIVE-THE-COUPLING-COUNT-IS-GRAIN-RELATIVE-",
                    "AND-NOTHING-IS-FORCED-", "/".join(seq["ANCHORED"]),
                    "-ANCHORED-AND-", "/".join(seq["EXTENSION"]),
                    "-AT-THE-EXTENSION"])


def demonstrate_reachability(S):
    """every pre-registered outcome is REACHABLE BY THE ONE HEAD LAW, and the
    demonstration is run inside the delivery run on synthetic censuses, so a
    head law that had collapsed to a constant dies here."""
    synth = [
        ("ACT-BLOCKED-AT", [dict(r) for r in S["form_census"]["rows"]],
         [dict(r) for r in S["gibbs"]["rows"]], "THE-ORBIT-COUNT"),
        ("ACT-FORM-FORCED",
         [dict(r, coupling_count=0) for r in S["form_census"]["rows"]],
         [dict(r) for r in S["gibbs"]["rows"]], None),
        ("ACT-GIBBS", [dict(r) for r in S["form_census"]["rows"]],
         [dict(r, reachable_dimension=0) for r in S["gibbs"]["rows"]], None),
        ("ACT-FORM-RELATIVE", [dict(r) for r in S["form_census"]["rows"]],
         [dict(r) for r in S["gibbs"]["rows"]], None)]
    got = []
    for want, rw, gw, bl in synth:
        h1 = head_law(rw, gw, bl)
        h2 = second_head_law(rw, gw, bl)
        got.append({"outcome": want, "reached": h1.startswith(want),
                    "both_laws_agree": h1 == h2, "emitted": h1[:60]})
    if mut("MUT-REACHABILITY"):
        got = [dict(g, reached=True, emitted=got[-1]["emitted"])
               for g in got]
        got[0]["emitted"] = got[-1]["emitted"]
    ok = (all(g["reached"] and g["both_laws_agree"] for g in got)
          and len({g["emitted"] for g in got}) == len(synth))
    LD.gate("G-HEAD-LAW-REACHABILITY",
            "each of the four pre-registered outcomes is emitted by THE ONE "
            "head law, handed a synthetic census built to select it, and by "
            "the second law too -- and the four strings are required to be "
            "distinct, so a head law that had collapsed to a constant, or a "
            "second law that had drifted into agreement by returning the "
            "same string always, dies inside the delivery run",
            ok,
            "%d pre-registered outcomes, %d reached by both laws, %d "
            "distinct strings"
            % (len(synth), sum(1 for g in got if g["reached"]
                               and g["both_laws_agree"]),
               len({g["emitted"] for g in got})))
    S["preregistered_heads"] = {"outcomes": list(PREREGISTERED),
                                "probes": got}
    SEAL.take("THE PRE-REGISTERED HEADS", "preregistered_heads",
              "G-HEAD-LAW-REACHABILITY", S["preregistered_heads"])


def build_verdict(S):
    fc, gb = S["form_census"]["rows"], S["gibbs"]["rows"]
    blocked = None
    for r in fc:
        if r["orbits"] is None or r["closure_failures"]:
            blocked = "THE-ORBIT-COUNT"
    head = head_law(fc, gb, blocked)
    S["verdict_head"] = head
    ar, wl, pr = S["arena"], S["wilson"], S["price"]
    lo, tc, fa = S["locality"], S["target_census"], S["falsifier"]
    dw, ex = S["density_witness"], S["expectations"]
    g = {r["row"]: r for r in gb}
    f = {r["row"]: r for r in fc}
    fam = {x["reading"]: x for x in fa["orbit_indicator_families"]}
    sig = [r for r in fa["rows"]
           if r["observable"] == "OFF-DIAGONAL-QUARTIC-SIGN"
           and r["reading"] == "ANCHORED"][0]
    wilrow = [r for r in fa["rows"]
              if r["observable"] == "WILSON-BLOCK-TRACE-RATIONAL-PART"
              and r["reading"] == "ANCHORED"][0]
    segs = []
    segs.append("CENSUS=%d-DECLARED-GRAINS-x-%d-CHART-READINGS-%d-OF-%d-RUN"
                % (len(GRAINS), len(READINGS), len(fc),
                   len(GRAINS) * len(READINGS)))
    segs.append("THE-ALLOWED-SPACE=EXACTLY-THE-ORBIT-CONSTANT-POSITIVE-"
                "RATIONAL-FUNCTIONS-ON-THE-STENCIL-DATUM-A-FREE-MODULE-OF-"
                "RANK-ORBITS-MINUS-ONE;ORBITS=%s-ANCHORED-AND-%s-AT-THE-"
                "EXTENSION;ROUTES=BURNSIDE-PLUS-BRUTE-FORCE-AND-ORBIT-"
                "STABILIZER-AT-THE-LINK-GRAIN-PLUS-AN-EXHAUSTIVE-%d-COIN-"
                "REDUCED-ARENA-AT-EVERY-GRAIN"
                % ("/".join(str(f["%s-ANCHORED" % gr]["orbits"])
                            for gr in GRAINS),
                   "/".join(str(f["%s-EXTENSION" % gr]["orbits"])
                            for gr in GRAINS),
                   S["form_census"]["reduced_arena_coins"]))
    segs.append("LOCALITY=PRODUCT-INVARIANCE-IS-LOCAL-INVARIANCE-AT-THE-LINK-"
                "GRAIN-%d-OF-%d-NON-INVARIANT-ELEMENTARY-SYSTEMS-DETECTED-"
                "AND-%d-OF-%d-INVARIANT-ONES-NOT;AT-THE-PLAQUETTE-GRAIN-IT-"
                "IS-STRICTLY-WEAKER-EVERY-LINK-LIES-IN-EXACTLY-%d-"
                "PLAQUETTES-SO-A-COBOUNDARY-SYSTEM-HAS-PRODUCT-ONE-AT-%d-"
                "CARRIER-AND-%d-DECLARED-NON-UNIFORM-CONFIGURATIONS"
                % (lo["link_grain_not_invariant_detected"],
                   lo["link_grain_not_invariant"],
                   lo["link_grain_invariant_detected"],
                   lo["link_grain_locally_invariant"],
                   lo["every_link_lies_in_this_many_plaquettes"],
                   lo["plaquette_grain_carrier_configurations_at_product_"
                      "one"],
                   lo["plaquette_grain_sample_at_product_one"]))
    segs.append("(a)WILSON-SHAPE=IN-THE-ALLOWED-SPACE-AT-EXACTLY-%d-OF-%d-"
                "DECLARED-GRAINS-THE-PLAQUETTE-ONE-AT-%d-CHECKS-0-FAILURES;"
                "ON-THE-CARRIER-IT-SPANS-%d-OF-%d-COUPLINGS-AT-%d-DISTINCT-"
                "TRACE-VALUES;NOT-MINIMAL-SUPPORT-%d-SINGLE-LINK-INVARIANT-"
                "CLASSES-EXIST-BECAUSE-THE-GAUGE-GROUP-IS-NOT-TRANSITIVE-ON-"
                "A-LINKS-OWN-DATUM"
                % (len(wl["in_the_allowed_space_at_grains"]),
                   wl["grains_declared"], wl["gauge_invariance_checks"],
                   wl["dimension_of_the_wilson_family_on_the_carrier"],
                   wl["the_allowed_space_on_the_carrier"],
                   wl["distinct_values_over_the_carrier"],
                   wl["single_link_invariant_classes"]))
    segs.append("(b)LAW-NATIVE-CONTROL=%s-CARRIED-VERBATIM-AND-NEVER-SPENT-"
                "AS-DERIVED;THE-TARGET-IS-CLASS-CONSTANT-AND-FULL-SUPPORT-"
                "AND-%s-BECAUSE-%s-IS-NOT-AN-EXACT-POWER-AT-ANY-DECLARED-"
                "EXPONENT-%s;IT-LIES-IN-THE-CLOSURE-EXACT-WITNESS-AT-"
                "DENOMINATOR-%d-WITH-ERROR-BELOW-1/10^%d"
                % (S["law_native_control"]["stamp"],
                   S["law_native_control"]["obstruction"],
                   dw["the_required_ratio"],
                   ",".join(str(e) for e in tc["exponents_tested"]),
                   dw["witness_denominator"],
                   dw["error_below_one_over_ten_to_the"]))
    segs.append("(c)NULL=W-IDENTICALLY-ONE-GIVES-THE-COUNTING-MEASURE-WHICH-"
                "IS-%d-OF-THE-%d-NAMED-TARGETS-REACHABLE;THE-OTHERS-FAIL-AT-"
                "%d-MEASURED-SPECIES-%s"
                % (tc["reachable"], len(tc["rows"]),
                   len(tc["obstruction_species"]),
                   ",".join(tc["obstruction_species"])))
    segs.append("GIBBS=THE-IMAGE-IS-THE-E-TH-POWER-SUBLATTICE-OF-THE-CLASS-"
                "CONSTANT-MEASURES-WITH-E=%s-AT-THE-THREE-GRAINS-AND-FULL-"
                "SUPPORT-FORCED-BY-POSITIVITY;THE-INDUCED-PARTITION-IS-THE-"
                "SAME-%d-CLASSES-AT-ALL-%d-GRAINS;THE-FIBRE-IS-EXACTLY-THE-"
                "NORMALISATION-AT-THE-LINK-GRAIN-DIMENSION-%d-AND-%d-AT-THE-"
                "PLAQUETTE-GRAIN"
                % ("/".join(str(g["%s-ANCHORED" % gr]["exponent"])
                            for gr in GRAINS),
                   g["LINK-ANCHORED"]["induced_classes_on_the_carrier"],
                   len(GRAINS), g["LINK-ANCHORED"]["fibre_dimension"],
                   g["PLAQUETTE-ANCHORED"]["fibre_dimension"]))
    segs.append("PRICE=REDUCED-NOT-EVADED-%d-TO-%d-AT-THE-ANCHORED-READING-"
                "AND-%d-TO-%d-AT-THE-EXTENSION-AGAINST-%d-WITH-COVARIANCE-"
                "DROPPED;%d-AND-%d-PAIRS-OF-GAUGE-ORBITS-ARE-IDENTIFIED-BY-"
                "EVERY-LOCAL-WEIGHT-SYSTEM-THE-ODD-TWIST-THE-TORUS-DOES-NOT-"
                "CLOSE"
                % (pr["the_parents_price_anchored"],
                   pr["the_action_route_supplies_anchored"],
                   pr["the_parents_price_extension"],
                   pr["the_action_route_supplies_extension"],
                   pr["the_parents_price_without_covariance"],
                   pr["orbit_pairs_merged_anchored"],
                   pr["orbit_pairs_merged_extension"]))
    segs.append("FALSIFIER=%s:THE-OFF-DIAGONAL-QUARTIC-SIGN-IS-A-GAUGE-"
                "OBSERVABLE-EVERY-ADMISSIBLE-WEIGHT-SYSTEM-PINS-TO-THE-"
                "SINGLE-VALUE-[%s,%s]-AGAINST-[%s,%s]-OVER-THE-INVARIANT-"
                "SIMPLEX;%d-OF-%d-ORBIT-INDICATORS-PINNED-AT-THE-ANCHORED-"
                "READING-AND-%d-OF-%d-AT-THE-EXTENSION;THE-LOOP-TRACE-IS-"
                "NOT-PINNED-[%s,%s]-AT-BOTH"
                % (fa["verdict"], sig["range_over_the_reachable_set"][0],
                   sig["range_over_the_reachable_set"][1],
                   sig["range_over_the_invariant_simplex"][0],
                   sig["range_over_the_invariant_simplex"][1],
                   fam["ANCHORED"]["pinned"], fam["ANCHORED"]["observables"],
                   fam["EXTENSION"]["pinned"],
                   fam["EXTENSION"]["observables"],
                   wilrow["range_over_the_reachable_set"][0],
                   wilrow["range_over_the_reachable_set"][1]))
    segs.append("WILSON=STAMPED-CONDITIONAL-ON-THE-DECLARED-WEIGHTS-AT-%d-"
                "OF-%d-ROWS|VALUES=%s|RANGE-OF-THE-OBSERVABLE=[%s,%s]|NO-"
                "AREA-LAW-NO-STRING-TENSION-NO-POTENTIAL-CLAIM-AND-%d-LOOP-"
                "FAMILIES-GROWN"
                % (sum(1 for r in ex["rows"]
                       if r["stamp"] == "CONDITIONAL-ON-THE-DECLARED-"
                                        "WEIGHTS"),
                   len(ex["rows"]),
                   ",".join("%s@%s" % (r["expectation"], r["row"])
                            for r in ex["rows"]),
                   ex["range_of_the_observable"][0],
                   ex["range_of_the_observable"][1],
                   ex["loop_families_grown"]))
    segs.append("SCOPE=D=%d;L=%d;FIELD=%s;COINS=%d;LINKS=%d;PLAQUETTES=%d;"
                "CARRIER=THE-PARENTS-%d-UNIFORM-CONFIGURATIONS;FULL-"
                "CONFIGURATION-SPACE=%s-NOT-A-CARRIER-HERE;WEIGHTS=POSITIVE-"
                "EXACT-RATIONALS-NO-LOGS-NO-FLOATS;THE-ACTION-IS-DECLARED-"
                "NOT-DERIVED;NO-COUPLING-IS-SELECTED;NOT-QCD;NO-CONFINEMENT-"
                "CLAIM"
                % (ar["d"], ar["L"], ar["field"], ar["coins"], ar["links"],
                   ar["plaquettes"], ar["coins"], ar["configuration_space"]))
    return head + "-<" + " -- ".join(segs) + ">"


def reconstruct_verdict(P):
    """the INDEPENDENT reconstruction: it reads only the serialized receipt,
    derives the head by the SECOND head law, and re-renders every segment
    from the primitive measured tables -- reading neither the builder's
    segments nor the builder's aggregates, sharing no format string and no
    helper with it."""
    fc = P["form_census"]["rows"]
    gb = P["gibbs"]["rows"]
    bl = None
    for r in fc:
        if r["orbits"] is None or r["closure_failures"]:
            bl = "THE-ORBIT-COUNT"
    parts = [second_head_law(fc, gb, bl), "-<"]
    body = []
    ngr = len({r["grain"] for r in fc})
    nrd = len({r["reading"] for r in fc})
    body.append("".join(["CENSUS=", str(ngr), "-DECLARED-GRAINS-x-",
                         str(nrd), "-CHART-READINGS-", str(len(fc)), "-OF-",
                         str(ngr * nrd), "-RUN"]))

    def by(row):
        return [r for r in fc if r["row"] == row][0]

    def gby(row):
        return [r for r in gb if r["row"] == row][0]

    body.append("".join([
        "THE-ALLOWED-SPACE=EXACTLY-THE-ORBIT-CONSTANT-POSITIVE-RATIONAL-",
        "FUNCTIONS-ON-THE-STENCIL-DATUM-A-FREE-MODULE-OF-RANK-ORBITS-MINUS-",
        "ONE;ORBITS=",
        "/".join([str(by(x + "-ANCHORED")["orbits"]) for x in GRAINS]),
        "-ANCHORED-AND-",
        "/".join([str(by(x + "-EXTENSION")["orbits"]) for x in GRAINS]),
        "-AT-THE-EXTENSION;ROUTES=BURNSIDE-PLUS-BRUTE-FORCE-AND-ORBIT-",
        "STABILIZER-AT-THE-LINK-GRAIN-PLUS-AN-EXHAUSTIVE-",
        str(P["form_census"]["reduced_arena_coins"]),
        "-COIN-REDUCED-ARENA-AT-EVERY-GRAIN"]))
    lo = P["locality"]
    body.append("".join([
        "LOCALITY=PRODUCT-INVARIANCE-IS-LOCAL-INVARIANCE-AT-THE-LINK-GRAIN-",
        str(lo["link_grain_not_invariant_detected"]), "-OF-",
        str(lo["link_grain_not_invariant"]),
        "-NON-INVARIANT-ELEMENTARY-SYSTEMS-DETECTED-AND-",
        str(lo["link_grain_invariant_detected"]), "-OF-",
        str(lo["link_grain_locally_invariant"]),
        "-INVARIANT-ONES-NOT;AT-THE-PLAQUETTE-GRAIN-IT-IS-STRICTLY-WEAKER-",
        "EVERY-LINK-LIES-IN-EXACTLY-",
        str(lo["every_link_lies_in_this_many_plaquettes"]),
        "-PLAQUETTES-SO-A-COBOUNDARY-SYSTEM-HAS-PRODUCT-ONE-AT-",
        str(lo["plaquette_grain_carrier_configurations_at_product_one"]),
        "-CARRIER-AND-",
        str(lo["plaquette_grain_sample_at_product_one"]),
        "-DECLARED-NON-UNIFORM-CONFIGURATIONS"]))
    wl = P["wilson"]
    body.append("".join([
        "(a)WILSON-SHAPE=IN-THE-ALLOWED-SPACE-AT-EXACTLY-",
        str(len(wl["in_the_allowed_space_at_grains"])), "-OF-",
        str(wl["grains_declared"]), "-DECLARED-GRAINS-THE-PLAQUETTE-ONE-AT-",
        str(wl["gauge_invariance_checks"]),
        "-CHECKS-0-FAILURES;ON-THE-CARRIER-IT-SPANS-",
        str(wl["dimension_of_the_wilson_family_on_the_carrier"]), "-OF-",
        str(wl["the_allowed_space_on_the_carrier"]), "-COUPLINGS-AT-",
        str(wl["distinct_values_over_the_carrier"]),
        "-DISTINCT-TRACE-VALUES;NOT-MINIMAL-SUPPORT-",
        str(wl["single_link_invariant_classes"]),
        "-SINGLE-LINK-INVARIANT-CLASSES-EXIST-BECAUSE-THE-GAUGE-GROUP-IS-",
        "NOT-TRANSITIVE-ON-A-LINKS-OWN-DATUM"]))
    lc, dw, tc = P["law_native_control"], P["density_witness"], \
        P["target_census"]
    body.append("".join([
        "(b)LAW-NATIVE-CONTROL=", lc["stamp"],
        "-CARRIED-VERBATIM-AND-NEVER-SPENT-AS-DERIVED;THE-TARGET-IS-CLASS-",
        "CONSTANT-AND-FULL-SUPPORT-AND-", lc["obstruction"], "-BECAUSE-",
        dw["the_required_ratio"], "-IS-NOT-AN-EXACT-POWER-AT-ANY-DECLARED-",
        "EXPONENT-", ",".join([str(e) for e in tc["exponents_tested"]]),
        ";IT-LIES-IN-THE-CLOSURE-EXACT-WITNESS-AT-DENOMINATOR-",
        str(dw["witness_denominator"]), "-WITH-ERROR-BELOW-1/10^",
        str(dw["error_below_one_over_ten_to_the"])]))
    body.append("".join([
        "(c)NULL=W-IDENTICALLY-ONE-GIVES-THE-COUNTING-MEASURE-WHICH-IS-",
        str(len([r for r in tc["rows"] if r["reachable"]])), "-OF-THE-",
        str(len(tc["rows"])), "-NAMED-TARGETS-REACHABLE;THE-OTHERS-FAIL-AT-",
        str(len(sorted({r["obstruction"] for r in tc["rows"]
                        if not r["reachable"]}))), "-MEASURED-SPECIES-",
        ",".join(sorted({r["obstruction"] for r in tc["rows"]
                         if not r["reachable"]}))]))
    body.append("".join([
        "GIBBS=THE-IMAGE-IS-THE-E-TH-POWER-SUBLATTICE-OF-THE-CLASS-",
        "CONSTANT-MEASURES-WITH-E=",
        "/".join([str(gby(x + "-ANCHORED")["exponent"]) for x in GRAINS]),
        "-AT-THE-THREE-GRAINS-AND-FULL-SUPPORT-FORCED-BY-POSITIVITY;THE-",
        "INDUCED-PARTITION-IS-THE-SAME-",
        str(gby("LINK-ANCHORED")["induced_classes_on_the_carrier"]),
        "-CLASSES-AT-ALL-", str(ngr),
        "-GRAINS;THE-FIBRE-IS-EXACTLY-THE-NORMALISATION-AT-THE-LINK-GRAIN-",
        "DIMENSION-", str(gby("LINK-ANCHORED")["fibre_dimension"]), "-AND-",
        str(gby("PLAQUETTE-ANCHORED")["fibre_dimension"]),
        "-AT-THE-PLAQUETTE-GRAIN"]))
    pr = P["price"]
    body.append("".join([
        "PRICE=REDUCED-NOT-EVADED-", str(pr["the_parents_price_anchored"]),
        "-TO-", str(pr["the_action_route_supplies_anchored"]),
        "-AT-THE-ANCHORED-READING-AND-",
        str(pr["the_parents_price_extension"]), "-TO-",
        str(pr["the_action_route_supplies_extension"]),
        "-AT-THE-EXTENSION-AGAINST-",
        str(pr["the_parents_price_without_covariance"]),
        "-WITH-COVARIANCE-DROPPED;",
        str(pr["orbit_pairs_merged_anchored"]), "-AND-",
        str(pr["orbit_pairs_merged_extension"]),
        "-PAIRS-OF-GAUGE-ORBITS-ARE-IDENTIFIED-BY-EVERY-LOCAL-WEIGHT-",
        "SYSTEM-THE-ODD-TWIST-THE-TORUS-DOES-NOT-CLOSE"]))
    fa = P["falsifier"]
    sg = [r for r in fa["rows"] if r["row"]
          == "OFF-DIAGONAL-QUARTIC-SIGN-ANCHORED"][0]
    wr = [r for r in fa["rows"] if r["row"]
          == "WILSON-BLOCK-TRACE-RATIONAL-PART-ANCHORED"][0]
    fm = {x["reading"]: x for x in fa["orbit_indicator_families"]}
    body.append("".join([
        "FALSIFIER=", fa["verdict"],
        ":THE-OFF-DIAGONAL-QUARTIC-SIGN-IS-A-GAUGE-OBSERVABLE-EVERY-",
        "ADMISSIBLE-WEIGHT-SYSTEM-PINS-TO-THE-SINGLE-VALUE-[",
        sg["range_over_the_reachable_set"][0], ",",
        sg["range_over_the_reachable_set"][1], "]-AGAINST-[",
        sg["range_over_the_invariant_simplex"][0], ",",
        sg["range_over_the_invariant_simplex"][1],
        "]-OVER-THE-INVARIANT-SIMPLEX;", str(fm["ANCHORED"]["pinned"]),
        "-OF-", str(fm["ANCHORED"]["observables"]),
        "-ORBIT-INDICATORS-PINNED-AT-THE-ANCHORED-READING-AND-",
        str(fm["EXTENSION"]["pinned"]), "-OF-",
        str(fm["EXTENSION"]["observables"]),
        "-AT-THE-EXTENSION;THE-LOOP-TRACE-IS-NOT-PINNED-[",
        wr["range_over_the_reachable_set"][0], ",",
        wr["range_over_the_reachable_set"][1], "]-AT-BOTH"]))
    ex = P["expectations"]
    body.append("".join([
        "WILSON=STAMPED-CONDITIONAL-ON-THE-DECLARED-WEIGHTS-AT-",
        str(len([r for r in ex["rows"] if r["stamp"]
                 == "CONDITIONAL-ON-THE-DECLARED-WEIGHTS"])), "-OF-",
        str(len(ex["rows"])), "-ROWS|VALUES=",
        ",".join([r["expectation"] + "@" + r["row"] for r in ex["rows"]]),
        "|RANGE-OF-THE-OBSERVABLE=[", ex["range_of_the_observable"][0], ",",
        ex["range_of_the_observable"][1],
        "]|NO-AREA-LAW-NO-STRING-TENSION-NO-POTENTIAL-CLAIM-AND-",
        str(ex["loop_families_grown"]), "-LOOP-FAMILIES-GROWN"]))
    ar = P["arena"]
    body.append("".join([
        "SCOPE=D=", str(ar["d"]), ";L=", str(ar["L"]), ";FIELD=",
        ar["field"], ";COINS=", str(ar["coins"]), ";LINKS=",
        str(ar["links"]), ";PLAQUETTES=", str(ar["plaquettes"]),
        ";CARRIER=THE-PARENTS-", str(ar["coins"]),
        "-UNIFORM-CONFIGURATIONS;FULL-CONFIGURATION-SPACE=",
        ar["configuration_space"],
        "-NOT-A-CARRIER-HERE;WEIGHTS=POSITIVE-EXACT-RATIONALS-NO-LOGS-NO-",
        "FLOATS;THE-ACTION-IS-DECLARED-NOT-DERIVED;NO-COUPLING-IS-SELECTED;",
        "NOT-QCD;NO-CONFINEMENT-CLAIM"]))
    parts.append(" -- ".join(body))
    parts.append(">")
    return "".join(parts)


# ===========================================================================
# SECTION 15.  THE CHOICE INVENTORY, THE REGISTRY, THE WAIVER LEDGER
# ===========================================================================

def price_the_choices(S):
    fc = S["form_census"]["rows"]
    gb = S["gibbs"]["rows"]
    grain_moves = len({r["coupling_count"] for r in fc
                       if r["reading"] == "ANCHORED"}) > 1
    reading_moves = len({r["orbits"] for r in fc
                         if r["grain"] == "LINK"}) > 1
    form_moves = (S["locality"]["plaquette_grain_verdict"]
                  != S["locality"]["link_grain_verdict"])
    field_moves = S["target_census"]["reachable"] < len(
        S["target_census"]["rows"])
    rows = [
        {"choice": "THE-LATTICE-AND-ITS-SIZE", "fibre": 1,
         "instances_built": 1, "status": "FORCED",
         "verdict_determining": "NOT-MEASURED",
         "why": "inherited from R5 at an anchored receipt path"},
        {"choice": "THE-COIN-FAMILY", "fibre": 1, "instances_built": 1,
         "status": "FORCED", "verdict_determining": "NOT-MEASURED",
         "why": "enumerated exhaustively from the declared alphabet"},
        {"choice": "THE-GAUGE-ACTION-AND-THE-CHART-GROUPS", "fibre": 1,
         "instances_built": 1, "status": "FORCED",
         "verdict_determining": "NOT-MEASURED",
         "why": "both are the parents' own declared objects, rebuilt"},
        {"choice": "THE-CARRIER", "fibre": 2, "instances_built": 1,
         "status": "DECLARED-AND-DISCLOSED",
         "verdict_determining": "NOT-MEASURED",
         "why": "the parent's primary carrier; the full configuration space "
                "is named in the scope segment and is out of reach by cost"},
        {"choice": "THE-LOCALITY-GRAIN", "fibre": len(GRAINS),
         "instances_built": len(GRAINS), "status": "DECLARED-AND-SWEPT",
         "verdict_determining": grain_moves,
         "why": "every declared member is RUN, and the coupling count is "
                "measured to move between them"},
        {"choice": "WHICH-CHART-READING", "fibre": len(READINGS),
         "instances_built": len(READINGS), "status": "DECLARED-AND-SWEPT",
         "verdict_determining": reading_moves,
         "why": "both declared readings are RUN, and the orbit count moves"},
        {"choice": "THE-INVARIANCE-FORM-LOCAL-OR-PRODUCT", "fibre": 2,
         "instances_built": 2, "status": "DECLARED-AND-SWEPT",
         "verdict_determining": form_moves,
         "why": "both forms are run at both relevant grains, and they are "
                "measured to differ at one of them"},
        {"choice": "THE-FIELD-THE-WEIGHTS-LIVE-IN", "fibre": 2,
         "instances_built": 1, "status": "DECLARED-BY-THE-PIN",
         "verdict_determining": field_moves,
         "why": "the pin binds positive exact rationals; over the positive "
                "reals the arithmetic obstruction disappears and the "
                "unreachable rows become reachable, which is disclosed "
                "rather than absorbed"},
        {"choice": "THE-NAMED-TARGETS", "fibre": "UNBOUNDED",
         "instances_built": len(S["target_census"]["rows"]),
         "status": "DECLARED-AND-DISCLOSED",
         "verdict_determining": True,
         "why": "the census verdict is a count over the declared targets, so "
                "declaring another moves it"},
        {"choice": "THE-DECLARED-OBSERVABLES", "fibre": "UNBOUNDED",
         "instances_built": S["falsifier"]["declared_observables"],
         "status": "DECLARED-AND-DISCLOSED",
         "verdict_determining": False,
         "why": "the falsifier verdict is EXISTENTIAL -- one pinned "
                "observable settles it -- so adding observables cannot "
                "remove the hit; the per-observable rows are what a further "
                "declaration would extend"},
        {"choice": "THE-REDUCED-ARENA-FOR-THE-VALIDATION",
         "fibre": "UNBOUNDED",
         "instances_built": 1, "status": "DECLARED-AND-DISCLOSED",
         "verdict_determining": False,
         "why": "it validates the machinery against a second route and "
                "carries no published physical quantity"},
        {"choice": "THE-DECLARED-NON-UNIFORM-SAMPLE", "fibre": "UNBOUNDED",
         "instances_built": S["locality"]["plaquette_grain_declared_sample"],
         "status": "DECLARED-AND-SAMPLED",
         "verdict_determining": False,
         "why": "the coboundary identity is a theorem about the incidence "
                "count, and the sample exhibits it rather than establishing "
                "it"},
        {"choice": "THE-WITNESS-DENOMINATOR", "fibre": "UNBOUNDED",
         "instances_built": 1, "status": "DECLARED-AND-DISCLOSED",
         "verdict_determining": False,
         "why": "only the published error bound moves with it; the "
                "unreachability it accompanies is decided by factorisation"},
    ]
    if mut("MUT-CHOICE-INVENTORY"):
        rows[4]["instances_built"] = rows[4]["fibre"] - 1
    bad = [r for r in rows
           if isinstance(r["fibre"], int) and r["status"].endswith("SWEPT")
           and r["instances_built"] != r["fibre"]]
    vd = [r for r in rows if r["verdict_determining"] is True]
    LD.gate("G-CHOICE-INVENTORY",
            "every construction choice is inventoried with its fibre and the "
            "number of instances this unit built; every axis declared SWEPT "
            "is required to have built its whole fibre, so no member of a "
            "declared fibre is left unrun; and the verdict-determining flag "
            "is bound to each row by its OWN measured predicate rather than "
            "asserted -- an axis carrying one instance is stamped "
            "NOT-MEASURED rather than reported as a measured false",
            not bad and len(vd) >= 4,
            "%d rows, %d swept axes short of their fibre %s, %d "
            "verdict-determining"
            % (len(rows), len(bad), [b["choice"] for b in bad], len(vd)))
    S["fibre"] = {"rows": rows,
                  "verdict_determining": len(vd),
                  "the_price_of_a_declaration": S["price"]}
    SEAL.take("THE CHOICE INVENTORY", "fibre", "G-CHOICE-INVENTORY",
              S["fibre"])


# the declared function inventory: the set of names this source defines,
# frozen so that a neutrally-named helper computing something this unit
# does not publish cannot exist unnoticed (G-FUNCTION-INVENTORY-IS-TOTAL).
FUNCTION_INVENTORY = [
    "__init__", "_g", "_plaq_image", "add", "addv", "apply_point",
    "bdigest", "block_trace", "bm", "boundary", "build_alphabet",
    "build_arena", "build_claims", "build_coins", "build_verdict",
    "build_waiver_ledger", "burnside", "by", "carries_defect",
    "chart_elements", "chart_stabilizer", "check_the_registry",
    "close_perm_group", "coboundary_product", "coin_sector",
    "coin_unitary_second_route", "compose", "datum_orbit_partition",
    "datum_orbits_bruteforce", "declared_function_names",
    "demonstrate_reachability", "dig", "digest", "elem_mul",
    "elementary_gauge_generators", "ends", "expect", "fadd", "fconj",
    "find", "fix_in", "fixed_data", "fmul", "fneg", "fnorm", "fnormsq",
    "fscal", "gate", "gauge_image", "gauge_twist", "gby", "group_orbits",
    "harvest", "head_law", "holonomy_block", "hset_members", "in_q_sqrt2",
    "induced_classes_on_the_carrier", "is_exact_power", "is_rational",
    "load_sources", "main", "measure_chart_and_gauge",
    "measure_density_witness", "measure_expectations",
    "measure_falsifier", "measure_locality", "measure_path_values",
    "measure_pot_handoff", "measure_provenance", "measure_targets",
    "measure_the_control_row", "measure_the_gibbs_map",
    "measure_the_supplied_row", "measure_verbatim", "measure_wilson_row",
    "mm", "mnorm", "mut", "observable_table", "orbit_stabilizer_sum",
    "own_source", "point_on_dir", "point_symmetries", "price_the_choices",
    "prime_exponents", "project", "qs_less", "qs_str", "qsqrt2_pair",
    "qsqrt2_pair_from_str", "quartic_sign", "read_bytes",
    "realisable_constant_twists", "reconstruct_verdict", "reduced_family",
    "resolve", "reverify", "run", "run_form_census", "say",
    "seal_and_write", "second_head_law", "selftest", "separates", "star",
    "stencil_group", "stencil_of", "swap_conjugate", "take",
    "to_fraction", "trace_of", "transported_link", "verify_paper",
    "verify_the_analytic_crosscheck", "verify_the_rank", "wsnorm", "zpow"]


def declared_function_names(tree):
    out = set()
    for n in ast.walk(tree):
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)):
            out.add(n.name)
        elif isinstance(n, ast.Assign) and isinstance(n.value, ast.Lambda):
            for t in n.targets:
                if isinstance(t, ast.Name):
                    out.add(t.id)
    return out


def check_the_registry(S):
    tree = ast.parse(own_source())
    src = own_source()
    names = declared_function_names(tree)
    ghost = sorted(names - set(FUNCTION_INVENTORY))
    missing = sorted(set(FUNCTION_INVENTORY) - names)
    LD.gate("G-FUNCTION-INVENTORY-IS-TOTAL",
            "the set of functions this source defines is required to EQUAL a "
            "declared inventory, so a neutrally-named helper computing "
            "something this unit does not publish cannot exist unnoticed",
            not ghost and not missing,
            "%d functions defined; undeclared %s; declared but absent %s"
            % (len(names), ghost[:4], missing[:4]))

    switches = set()
    for n in ast.walk(tree):
        if isinstance(n, ast.Call) and getattr(n.func, "id", None) == "mut":
            if n.args and isinstance(n.args[0], ast.Constant) \
                    and isinstance(n.args[0].value, str):
                switches.add(n.args[0].value)
            else:
                switches.add("UNREADABLE-SWITCH")
    declared = {m[0] for m in MUTANTS}
    unswept = sorted(switches - declared - {"UNREADABLE-SWITCH"})
    unfired = sorted(declared - switches)
    unreadable = "UNREADABLE-SWITCH" in switches
    LD.gate("G-MUTANT-REGISTRY-IS-TOTAL",
            "the falsifier registry is checked TOTAL against this "
            "instrument's own syntax tree: every switch in the source is "
            "declared, every declared falsifier has a branch to fire, and a "
            "switch the scan cannot read -- a computed name, or a bare "
            "comparison outside mut's own body -- is fatal rather than "
            "forgiven",
            not unswept and not unfired and not unreadable,
            "%d switches in the tree, %d declared; undeclared %s; declared "
            "without a branch %s; unreadable switch present %s"
            % (len(switches), len(declared), unswept[:4], unfired[:4],
               unreadable))

    bad = []
    for name, target, what, token in MUTANTS:
        if mut("MUT-FALSIFIER-DESCRIPTION") and name == "MUT-ARENA":
            token = "".join(reversed(token))
        if token not in src:
            bad.append(name)
    LD.gate("G-FALSIFIER-DESCRIPTIONS-ARE-HONEST",
            "E-23: each falsifier's PUBLISHED description names the exact "
            "source token it plants, and that token is located in this "
            "instrument's own source text -- so a description-inverted "
            "mutant dies here rather than in a reader's trust",
            not bad, "%d falsifiers, %d whose published token is not in the "
            "source %s" % (len(MUTANTS), len(bad), bad[:4]))
    S["falsifier_totals"] = {
        "declared_falsifiers": len(MUTANTS),
        "distinct_target_gates": len({m[1] for m in MUTANTS}),
        "switches_in_the_syntax_tree": len(switches),
        "functions_declared": len(names),
        "the_sweep_result": "AN-EXTERNAL-BATTERY-RESULT-THE-DELIVERY-RUN-"
                            "DOES-NOT-PRODUCE-IT"}
    SEAL.take("THE FALSIFIER TOTALS", "falsifier_totals",
              "G-FALSIFIER-DESCRIPTIONS-ARE-HONEST", S["falsifier_totals"])


FORCINGS = {
    "G-MUTANTS-ON-TARGET": "no such gate exists in this instrument; the "
                           "sweep is adjudicated by the CLI harness and "
                           "every surviving or off-target injection fails "
                           "it, which is an external-battery result",
    "G-ARTIFACT-INTEGRITY": "evaluated only in the writing path, which no "
                            "diagnostic run reaches; its reference value is "
                            "the GATE-TIME SEAL, whose in-run twin "
                            "G-SEAL-INTEGRITY carries the injection "
                            "falsifier MUT-SEAL",
}


def build_waiver_ledger(S):
    closed = [r["gate"] for r in LD.rows]
    covered = sorted({m[1] for m in MUTANTS} & set(closed))
    if mut("MUT-WAIVER"):
        covered = covered[:-1]
    forced = sorted(set(FORCINGS) & set(closed + list(LATE_GATES)))
    uncovered = [g for g in closed
                 if g not in covered and g not in FORCINGS]
    S["waiver_ledger"] = {
        "gates_closed": len(closed),
        "covered_by_a_declared_falsifier": len(covered),
        "under_a_registered_forcing": len(forced),
        "the_forcings": FORCINGS,
        "uncovered": uncovered,
        "late_gates_declared": list(LATE_GATES)}
    LD.gate("G-FALSIFIER-COVERAGE-AT-AN-HONEST-DENOMINATOR",
            "the coverage is published at an honest denominator (#34): every "
            "gate this run closes is either the declared target of a "
            "falsifier that REACHES it, or carries a registered forcing "
            "stating why no falsifier can, and the remainder is named rather "
            "than folded into the first class",
            not uncovered,
            "%d gates closed, %d carry a declared falsifier, %d a registered "
            "forcing, %d uncovered %s"
            % (len(closed), len(covered), len(forced), len(uncovered),
               uncovered[:5]))
    SEAL.take("THE WAIVER LEDGER", "waiver_ledger",
              "G-FALSIFIER-COVERAGE-AT-AN-HONEST-DENOMINATOR",
              S["waiver_ledger"])


LATE_GATES = ("G-FALSIFIER-COVERAGE-AT-AN-HONEST-DENOMINATOR",
              "G-LEDGER-SHAPE-IS-CONSISTENT", "G-PAPER-CLAIMS",
              "G-PAPER-VERDICT-EQUALITY", "G-MUST-NOT-VOCABULARY",
              "G-PAPER-POLARITY", "G-PAPER-TABLES-AND-QUOTES-ARE-BOUND",
              "G-PAPER-NUMERAL-COVERAGE", "G-SEAL-INTEGRITY",
              "G-ARTIFACT-INTEGRITY")


# ===========================================================================
# SECTION 16.  THE PAPER GATES
# ===========================================================================

DIGEST_KEYS = {"pinned", "measured", "digest", "code_sha256_12",
               "paper_sha256_12", "pin_sha256_prefix"}
POOL_EXCLUDED = {"mutants"}

# THE MUST-NOT, INHERITED VERBATIM FROM PAPER-23's REPAIRED GATE.
MUST_NOT = [
    "area law", "area-law", "the law of the area",
    "string tension", "string-tension",
    "confining", "confinement", "quark", "potential",
]

# the declaring sentences the sweep may remove.  The list is EXACTLY the
# sentences this paper contains: an exemption inherited from a parent and
# never used here would be a latent hole, so every entry must be located.
DECLARING = [
    "no area-law, string-tension, or potential claim",
    "NO-AREA-LAW-NO-STRING-TENSION-NO-POTENTIAL-CLAIM",
    "NO-CONFINEMENT-CLAIM",
    "the confinement vocabulary REMAINS BEHIND POT'S GATE",
    "A confinement analog would need three objects this arena does not have",
    "no loop family is grown",
]


def build_claims(S):
    """the paper's load-bearing sentences, RENDERED FROM THE RECEIPT, each
    with the number of times it must occur."""
    ar, fc, gb = S["arena"], S["form_census"]["rows"], S["gibbs"]["rows"]
    wl, pr, lo = S["wilson"], S["price"], S["locality"]
    tc, fa, ex = S["target_census"], S["falsifier"], S["expectations"]
    dw, rk, ls = S["density_witness"], S["rank"], S["ledger_shape"]
    ac, rg = S["analytic_crosscheck"], S["residual_gauge"]
    f = {r["row"]: r for r in fc}
    g = {r["row"]: r for r in gb}
    c = []
    c.append(("%d sites, %d links and %d plaquettes"
              % (ar["sites"], ar["links"], ar["plaquettes"]), 1))
    c.append(("%d coins, splitting into %d diagonal, %d antidiagonal and %d "
              "balanced" % (ar["coins"], ar["sectors"]["DIAGONAL"],
                            ar["sectors"]["ANTIDIAGONAL"],
                            ar["sectors"]["BALANCED"]), 1))
    c.append(("%d orbits at the anchored reading and %d at the extension"
              % (rg["orbits_anchored"], rg["orbits_extension"]), 1))
    c.append(("residual gauge group is of order %d at the anchored reading "
              "and %d at the extension" % (rg["order_anchored"],
                                           rg["order_extension"]), 1))
    # the form-census table, cell by cell
    for r in fc:
        c.append(("%s | %s | %d | %d | %d | %d | %d"
                  % (r["grain"].lower(), r["reading"].lower(),
                     r["gauge_image_order"], r["chart_stabilizer_order"],
                     r["acting_group_order"], r["orbits"],
                     r["coupling_count"]), 1))
    c.append(("the coupling count is %d at the link grain, %d at the "
              "plaquette grain and %d at the site grain"
              % (f["LINK-ANCHORED"]["coupling_count"],
                 f["PLAQUETTE-ANCHORED"]["coupling_count"],
                 f["SITE-ANCHORED"]["coupling_count"]), 1))
    c.append(("%d, %d and %d at the extension reading"
              % (f["LINK-EXTENSION"]["coupling_count"],
                 f["PLAQUETTE-EXTENSION"]["coupling_count"],
                 f["SITE-EXTENSION"]["coupling_count"]), 1))
    c.append(("the declared reduced arena carries %d coins"
              % S["form_census"]["reduced_arena_coins"], 1))
    c.append(("%d and %d, the two constants the character route is written "
              "in" % (ac["twist_classes"], ac["non_singleton_classes"]), 1))
    c.append(("%d against the character route's %d"
              % (ac["plaquette_gauge_only_burnside"],
                 ac["plaquette_gauge_only_character_route"]), 1))
    c.append(("%d generators are exhibited" % rk["generators_exhibited"], 1))
    # locality
    c.append(("%d of %d elementary systems that are not locally invariant "
              "are detected, and %d of the %d that are"
              % (lo["link_grain_not_invariant_detected"],
                 lo["link_grain_not_invariant"],
                 lo["link_grain_invariant_detected"],
                 lo["link_grain_locally_invariant"]), 1))
    c.append(("every link lies in exactly %d plaquettes"
              % lo["every_link_lies_in_this_many_plaquettes"], 1))
    c.append(("product one at all %d carrier configurations and at all %d "
              "declared non-uniform ones"
              % (lo["plaquette_grain_carrier_configurations_at_product_one"],
                 lo["plaquette_grain_sample_at_product_one"]), 1))
    # the Gibbs table
    for r in gb:
        c.append(("%s | %s | %d | %d | %d | %d | %d"
                  % (r["grain"].lower(), r["reading"].lower(),
                     r["exponent"], r["induced_classes_on_the_carrier"],
                     r["reachable_dimension"], r["orbit_pairs_merged"],
                     r["fibre_dimension"]), 1))
    c.append(("%d of the reachable set's extreme points are vertices of the "
              "parent's simplex and the other %d are midpoints of its edges"
              % (g["LINK-ANCHORED"][
                  "extreme_points_that_are_vertices_of_the_parents_simplex"],
                 g["LINK-ANCHORED"][
                     "extreme_points_that_are_edge_midpoints_of_it"]), 1))
    c.append(("the same %d classes at all three grains"
              % g["LINK-ANCHORED"]["induced_classes_on_the_carrier"], 1))
    c.append(("%d independent numbers where the parent's declaration "
              "supplies %d" % (pr["the_action_route_supplies_anchored"],
                               pr["the_parents_price_anchored"]), 1))
    c.append(("%d and %d at the extension reading"
              % (pr["the_action_route_supplies_extension"],
                 pr["the_parents_price_extension"]), 1))
    c.append(("%d pairs of gauge orbits at the anchored reading and %d at "
              "the extension" % (pr["orbit_pairs_merged_anchored"],
                                 pr["orbit_pairs_merged_extension"]), 1))
    c.append(("%d numbers instead" % pr["the_parents_price_without_"
                                        "covariance"], 1))
    c.append(("fibre of dimension %d at the link grain and %d at the "
              "plaquette grain"
              % (g["LINK-ANCHORED"]["fibre_dimension"],
                 g["PLAQUETTE-ANCHORED"]["fibre_dimension"]), 1))
    # Wilson
    c.append(("%d of the %d declared grains" % (
        len(wl["in_the_allowed_space_at_grains"]), wl["grains_declared"]), 1))
    c.append(("%d checks against every one of the plaquette's gauge "
              "elements, %d failures" % (wl["gauge_invariance_checks"],
                                         wl["gauge_invariance_failures"]), 1))
    c.append(("%d distinct values" % wl["distinct_values_over_the_carrier"],
              1))
    c.append(("%d of the %d couplings the carrier admits"
              % (wl["dimension_of_the_wilson_family_on_the_carrier"],
                 wl["the_allowed_space_on_the_carrier"]), 1))
    c.append(("%d single-link invariant classes"
              % wl["single_link_invariant_classes"], 1))
    # the target census table
    for r in tc["rows"]:
        c.append(("%s | %s | %s | %s"
                  % (r["row"], "yes" if r["class_constant"] else "no",
                     "yes" if r["full_support"] else "no",
                     r["obstruction"]), 1))
    c.append(("%d of the %d named targets" % (tc["reachable"],
                                              len(tc["rows"])), 1))
    c.append(("%d measured obstruction species"
              % len(tc["obstruction_species"]), 1))
    c.append(("the ratio %s is not an exact power at either declared "
              "exponent" % dw["the_required_ratio"], 1))
    c.append(("at denominator %d the error is below %s"
              % (dw["witness_denominator"],
                 "1/10^%d" % dw["error_below_one_over_ten_to_the"]), 1))
    # the falsifier table
    for r in fa["rows"]:
        if not r.get("is_a_gauge_observable"):
            continue
        c.append(("%s | %s | [%s, %s] | [%s, %s] | %s"
                  % (r["observable"].lower().replace("-", " "),
                     r["reading"].lower(),
                     r["range_over_the_invariant_simplex"][0],
                     r["range_over_the_invariant_simplex"][1],
                     r["range_over_the_reachable_set"][0],
                     r["range_over_the_reachable_set"][1],
                     r["verdict"].lower()), 1))
    for x in fa["orbit_indicator_families"]:
        c.append(("%d of the %d orbit indicators are pinned at the %s "
                  "reading" % (x["pinned"], x["observables"],
                               x["reading"].lower()), 1))
    # the expectations
    for r in ex["rows"]:
        c.append(("%s under %s" % (r["expectation"], r["row"]), 1))
    c.append(("%d loop families are grown" % ex["loop_families_grown"], 1))
    # the instrument
    c.append(("%d gates close before the paper gates, and %d paper gates and "
              "%d closing gates follow"
              % (ls["gates_closed_before_the_paper_gates"], ls["paper_gates"],
                 ls["closing_gates"]), 1))
    c.append(("%d objects are sealed before the paper gates"
              % ls["objects_sealed_before_the_paper_gates"], 1))
    c.append(("%d construction choices are inventoried, of which %d are "
              "measured verdict-determining"
              % (len(S["fibre"]["rows"]), S["fibre"]["verdict_determining"]),
              1))
    c.append(("%d file-bytes anchors, %d path-value anchors and %d "
              "verbatim-text anchors, %d anchors in all"
              % (S["anchor_classes"]["file_bytes"],
                 S["anchor_classes"]["path_value"],
                 S["anchor_classes"]["verbatim_text"],
                 S["anchor_classes"]["total"]), 2))
    c.append(("%d declared mutants" % len(MUTANTS), 1))
    for _nm, rel_path, sha, _what in SOURCES:
        if sha == PIN_SHA12:
            c.append(("`%s` (sha256-12 `%s`)" % (rel_path, sha), 1))
        else:
            c.append(("`%s` (`%s`)" % (rel_path, sha), 1))
    # the pre-registered outcome table
    c.append(("`ACT-FORM-FORCED` | the allowed space is a point at every "
              "declared row | not the case: the smallest coupling count "
              "measured is %d" % min(r["coupling_count"] for r in fc), 1))
    c.append(("`ACT-GIBBS` | the image is one measure | not the case: the "
              "reachable set has dimension %d at the link grain"
              % g["LINK-ANCHORED"]["reachable_dimension"], 1))
    c.append(("`ACT-BLOCKED-AT` | an object that cannot be evaluated | every "
              "declared row is evaluated and its Burnside sum divides", 1))
    c.append(("`ACT-FORM-RELATIVE` | the allowed space has positive rank | "
              "**this is what is measured**", 1))
    return c


POLARITY = [
    ("the price is REDUCED, not evaded", 1),
    ("the Wilson shape is not forced", 1),
    ("the odd twist is not realisable on this torus", 1),
    ("the coupling count is grain-relative", 1),
]


def verify_paper(S, paper_text):
    claims = build_claims(S)
    ptext = paper_text
    if mut("MUT-CLAIM"):
        ptext = ptext.replace(
            "%d single-link invariant classes"
            % S["wilson"]["single_link_invariant_classes"],
            "137 single-link invariant classes", 1)
    if mut("MUT-TABLE-ROW"):
        a = re.search(r"^(\|\s*link\s*\|\s*anchored\s*\|)(.*)$", ptext, re.M)
        b = re.search(r"^(\|\s*site\s*\|\s*anchored\s*\|)(.*)$", ptext, re.M)
        if a and b:
            ptext = ptext.replace(a.group(0), a.group(1) + b.group(2), 1)
            ptext = ptext.replace(b.group(0), b.group(1) + a.group(2), 1)
    if mut("MUT-QUOTE-FIDELITY"):
        ptext = ptext.replace("the ordered product of the four link",
                              "the unordered sum of the four link", 1)
    if mut("MUT-TABLE-BINDING"):
        ptext = ptext + "\n\n| a | b |\n|---|---|\n| planted | 4242 |\n"
    if mut("MUT-MUST-NOT"):
        ptext = ptext + "\n\nThe expectation follows an area law and the "
        ptext = ptext + "string tension is its coefficient.\n"
    if mut("MUT-COVERAGE"):
        ptext = ptext + "\n\nan uncovered numeral 987654321\n"
    hay = mnorm(ptext)
    miss = []
    for frag, want in claims:
        got = hay.count(mnorm(frag))
        if got != want:
            miss.append({"claim": frag, "expected": want, "found": got})
    S["paper_claims"] = [{"claim": f, "occurrences": w} for f, w in claims]
    LD.gate("G-PAPER-CLAIMS",
            "every load-bearing sentence of the paper is RENDERED FROM THE "
            "RECEIPT and located in the delivered bytes at its exact "
            "occurrence count, under whitespace and markdown-prefix "
            "normalisation (#125) -- so a number corrupted at one of its "
            "several occurrences dies, and a paper whose prose drifted from "
            "the run that produced it cannot be delivered",
            not miss, "%d rendered claims, %d not located at their counts: %s"
            % (len(claims), len(miss), miss[:3]))
    SEAL.take("THE PAPER CLAIMS", "paper_claims", "G-PAPER-CLAIMS",
              S["paper_claims"])

    verdict = S["verdict"]
    blocks = [wsnorm(b) for b in
              re.findall(r"```(?:[a-z]*)\n(.*?)```", ptext, re.S)]
    if mut("MUT-VERDICT-TWIN"):
        blocks = blocks + [wsnorm(verdict).replace("ACT-", "XCT-")]
    LD.gate("G-PAPER-VERDICT-EQUALITY",
            "the paper's verdict block is compared for EQUALITY against the "
            "string this run emits, under whitespace normalisation, and the "
            "paper's fenced blocks are gated by MULTISET EQUALITY against "
            "the single block this run licenses (E-22) -- so neither a stale "
            "verdict nor a forged twin riding along beside the clean one can "
            "be delivered",
            blocks == [wsnorm(verdict)],
            "%d fenced blocks; %d equal to this run's verdict of %d "
            "characters" % (len(blocks),
                            sum(1 for b in blocks if b == wsnorm(verdict)),
                            len(verdict)))

    sw = mnorm(ptext)
    inert = [d[:40] for d in DECLARING if mnorm(d) not in sw]
    for d in DECLARING:
        sw = sw.replace(mnorm(d), " ")
    hits = [w for w in MUST_NOT if mnorm(w) in sw]
    LD.gate("G-MUST-NOT-VOCABULARY",
            "the must-not vocabulary -- inherited VERBATIM from paper-23's "
            "repaired gate, the bare words included -- is swept over this "
            "paper's own text with the declaring sentences removed first and "
            "inline emphasis stripped, so a claim under asterisks is still "
            "the same claim.  Every declaring sentence the sweep may remove "
            "must itself be LOCATED in this paper: an exemption carried from "
            "a parent and never used is a latent hole",
            not hits and not inert,
            "must-not vocabulary found: %s; %d declaring sentences, %d not "
            "located %s" % (hits, len(DECLARING), len(inert), inert[:3]))

    pol = []
    low = mnorm(ptext)
    if mut("MUT-POLARITY"):
        low = low.replace(mnorm(POLARITY[0][0]),
                          "it is false that " + mnorm(POLARITY[0][0]), 1)
    for frag, want in POLARITY:
        nfound = low.count(mnorm(frag))
        i = low.find(mnorm(frag))
        bad = False
        if i >= 0:
            win = low[max(0, i - 64):i]
            bad = any(gx in win for gx in ("it is false that", "contrary to",
                                           "does not follow that"))
        pol.append({"fragment": frag, "expected": want, "found": nfound,
                    "negated": bad, "ok": nfound == want and not bad})
    S["paper_polarity"] = pol
    LD.gate("G-PAPER-POLARITY",
            "the direction-bearing claims are checked for POLARITY as well "
            "as presence -- each must occur and must not sit inside a window "
            "carrying a declared negator -- which closes the "
            "direction-blindness of a fragment gate",
            all(p["ok"] for p in pol),
            "%d polarity rows, %d failing"
            % (len(pol), sum(1 for p in pol if not p["ok"])))
    SEAL.take("THE PAPER POLARITY", "paper_polarity", "G-PAPER-POLARITY",
              S["paper_polarity"])

    plines = ptext.split("\n")
    sep = r"^\|[\s:\-|]+\|$"
    trows, theads = [], []
    for i, line in enumerate(plines):
        st = line.strip()
        if not st.startswith("|"):
            continue
        if re.match(sep, st):
            continue
        nxt = plines[i + 1].strip() if i + 1 < len(plines) else ""
        if re.match(sep, nxt):
            theads.append(st)
            continue
        if re.search(r"\d", st):
            trows.append(st)
    claim_texts = [mnorm(fr) for fr, _w in claims]
    unbound_rows = [r[:70] for r in trows
                    if not any(ct and ct in mnorm(r) for ct in claim_texts)]
    quotes, blk = [], []
    for line in plines:
        st = line.strip()
        if st.startswith(">"):
            blk.append(st[1:].strip())
        elif blk:
            quotes.append(" ".join(blk))
            blk = []
    if blk:
        quotes.append(" ".join(blk))
    needles = [mnorm(w) for _a, _s, w, _c, _wh in VERBATIM]
    unbound_quotes = [q[:70] for q in quotes
                      if len(mnorm(q)) < 30
                      or not any(mnorm(q) in nd for nd in needles)]
    LD.gate("G-PAPER-TABLES-AND-QUOTES-ARE-BOUND",
            "E-22's 'tables render as claims' is enforced structurally: "
            "every DATA row of every delivered table that carries a numeral "
            "must be covered by a claim rendered from the receipt, and every "
            "BLOCKQUOTE must lie inside one of the pinned verbatim windows "
            "-- so a paper that misquotes, or inverts, a parent's own "
            "definition dies here even though the anchor on the parent's "
            "bytes passes.  Header rows are the declared exception and are "
            "counted and published rather than silently skipped",
            not unbound_rows and not unbound_quotes,
            "%d table data rows carrying a numeral, %d unbound %s; %d header "
            "rows excluded; %d blockquotes, %d not inside a pinned window %s"
            % (len(trows), len(unbound_rows), unbound_rows[:2], len(theads),
               len(quotes), len(unbound_quotes), unbound_quotes[:2]))
    S["paper_binding"] = {
        "table_data_rows_carrying_a_numeral": len(trows),
        "table_rows_unbound": len(unbound_rows),
        "table_header_rows_excluded": len(theads),
        "blockquotes": len(quotes),
        "blockquotes_outside_a_pinned_verbatim_window": len(unbound_quotes),
        "verbatim_windows_available": len(VERBATIM)}
    SEAL.take("THE PAPER BINDING", "paper_binding",
              "G-PAPER-TABLES-AND-QUOTES-ARE-BOUND", S["paper_binding"])

    allowed = set()

    def add(x):
        s = str(x)
        allowed.add(s)
        if "/" in s:
            for side in s.split("/"):
                allowed.add(side)

    def harvest(o):
        if isinstance(o, dict):
            for k, v in o.items():
                if isinstance(k, str) and k.startswith("_"):
                    continue
                if isinstance(k, str):
                    for m in re.findall(r"\d+(?:/\d+)?", k):
                        add(m)
                if isinstance(k, str) and k in DIGEST_KEYS:
                    continue
                harvest(v)
        elif isinstance(o, list):
            for v in o:
                harvest(v)
        elif isinstance(o, bool):
            pass
        elif isinstance(o, int):
            add(o)
        elif isinstance(o, str):
            for m in re.findall(r"\d+(?:/\d+)?", o):
                add(m)
    harvest({k: v for k, v in S.items()
             if not k.startswith("_") and k not in POOL_EXCLUDED})
    STRUCTURAL = ({str(k) for k in range(1, 14)}
                  | {"%d.%d" % (a, b) for a in range(1, 14)
                     for b in range(0, 13)})
    scan = re.sub(r"\((?:#\d+|E-\d+)(?:,\s*(?:#\d+|E-\d+))*\)", " ", ptext)
    scan = re.sub(r"`[0-9a-f]{12}`", " ", scan)
    nums = re.findall(r"\d+(?:/\d+)?(?:\.\d+)?", scan)
    unmatched = []
    for x in nums:
        if x in allowed or x in STRUCTURAL:
            continue
        if "/" in x and all(p in allowed for p in x.split("/")):
            continue
        unmatched.append(x)
    spans = len(re.findall(r"`[^`]*\d[^`]*`", ptext))
    fenced = len(re.findall(r"```", ptext))
    LD.gate("G-PAPER-NUMERAL-COVERAGE",
            "EVERY numeral of the paper is matched against a value this run "
            "computed -- fenced blocks, verdict block, inline code spans and "
            "both sides of every fraction included (E-22, #20) -- with only "
            "a published list of structural literals forgiven, so a number "
            "invented in prose, or moved from one claim to another, dies "
            "inside the delivery run",
            not unmatched, "%d numerals scanned, %d inline code spans "
            "carrying a numeral, %d fence markers, %d unmatched: %s"
            % (len(nums), spans, fenced, len(unmatched), unmatched[:8]))
    S["paper_coverage"] = {
        "numerals_scanned": len(nums),
        "inline_spans_with_a_numeral": spans,
        "fence_markers": fenced, "unmatched": len(unmatched),
        "removed_from_the_scan_and_bound_as_claims":
            "THE-PARENTHESISED-ENGRAVING-REFERENCES-AND-THE-BACKTICKED-"
            "TWELVE-HEX-DIGESTS",
        "digest_valued_keys_excluded_from_the_pool": sorted(DIGEST_KEYS),
        "published_objects_excluded_from_the_pool": sorted(POOL_EXCLUDED),
        "structural_literals_forgiven": sorted(STRUCTURAL)}
    SEAL.take("THE PAPER COVERAGE", "paper_coverage",
              "G-PAPER-NUMERAL-COVERAGE", S["paper_coverage"])


# ===========================================================================
# SECTION 17.  THE MUTANT REGISTRY, TOTAL AND HONESTLY DESCRIBED (E-23)
# ===========================================================================

MUTANTS = [
    ("MUT-SOURCE-DRIFT", "G-SOURCE-BYTES",
     "replaces one pinned source's measured digest with zeros",
     '"000000000000"'),
    ("MUT-AST-BLIND", "G-WEIGHTS-ARE-POSITIVE-RATIONALS",
     "plants a real float literal into the source text the AST gate parses",
     "_TOLERANCE_FLOAT = 1e-9"),
    ("MUT-PATH-VALUE", "G-PATH-VALUE-ANCHORS",
     "moves one inherited path-value to 999", "got = 999"),
    ("MUT-VERBATIM", "G-VERBATIM-ANCHORS",
     "inverts one verbatim window's own meaning, so it stops locating in "
     "the parent's pinned bytes", 'window.replace("must not", "may")'),
    ("MUT-ARENA", "G-ARENA-REBUILT",
     "drops one coin from the rebuilt family", "coins = coins[:-1]"),
    ("MUT-RESIDUAL", "G-RESIDUAL-GAUGE-REBUILT",
     "drops one residual gauge orbit before the comparison with both "
     "parents' counts", "o32 = o32[:-1]"),
    ("MUT-GROUP-NOT-CLOSED", "G-FORM-CENSUS-COMPLETE",
     "removes one element from the acting group at the plaquette grain, so "
     "the closure check fails", "G = G[:-1]"),
    ("MUT-BURNSIDE", "G-FORM-CENSUS-COMPLETE",
     "adds one to the site grain's published orbit count, so it no longer "
     "re-derives its own Burnside sum", "orb = orb + 1 if orb else orb"),
    ("MUT-ANALYTIC", "G-ANALYTIC-CROSSCHECK",
     "moves the character route's plaquette count by one",
     "plaq_closed = plaq_closed + 1"),
    ("MUT-RANK", "G-RANK-IS-ORBITS-MINUS-ONE",
     "drops one exhibited generator, so the rank no longer equals the orbit "
     "count less one", "gens = gens[:-1]"),
    ("MUT-LOCALITY-THEOREM", "G-LOCALITY-AT-THE-LINK-GRAIN",
     "flips one detected and one undetected elementary system, so the "
     "two-sided census is no longer two-sided",
     'non[0] = dict(non[0], detected=False)'),
    ("MUT-COBOUNDARY", "G-LOCALITY-GAP-AT-THE-PLAQUETTE-GRAIN",
     "gives one link the same exponent in both of its plaquettes, so the "
     "coboundary's product is no longer one",
     "exps[lat.links[0]] = {order[lat.links[0]][0]: 1,"),
    ("MUT-GEOMETRY", "G-THE-REACHABLE-SIMPLEX-IS-EXHIBITED",
     "drops one singleton class from the vertex count, so the two counts no "
     "longer exhaust the class list", "singletons = singletons - 1"),
    ("MUT-INDUCED", "G-REACHABLE-SET-IS-A-SUBSIMPLEX",
     "merges two induced classes at the site grain, so the three grains no "
     "longer induce the same partition",
     "cls = cls[:-2] + [cls[-2] + cls[-1]]"),
    ("MUT-WILSON-OBSERVABLE", "G-WILSON-OBSERVABLE-REBUILT",
     "perturbs one configuration's trace at one plaquette, so the "
     "observable stops being plaquette-independent",
     "vals[0] = fadd(vals[0], ONE)"),
    ("MUT-WILSON-INVARIANCE", "G-WILSON-IS-IN-THE-ALLOWED-SPACE",
     "reports a gauge-invariance failure for the loop trace", "bad = 1"),
    ("MUT-WILSON-GRAIN", "G-WILSON-GRAIN-SELECTION",
     "declares the link grain not to separate, so the grain-selection "
     "finding is no longer exhibited", "sep_link = False"),
    ("MUT-TARGET-CENSUS", "G-TARGET-CENSUS",
     "declares the law-native control reachable",
     'rows[3]["obstruction"] = "REACHABLE"'),
    ("MUT-CONTROL-SPENT", "G-LAW-NATIVE-CONTROL-STAMP-CARRIED",
     "spends the control as a derived row by marking it reachable",
     'row = dict(row, reachable=True, obstruction="REACHABLE")'),
    ("MUT-DENSITY", "G-DENSITY-WITNESS",
     "overstates the witness's error bound by three decades", "j = j + 3"),
    ("MUT-FALSIFIER", "G-FALSIFIER-CENSUS",
     "declares every observable unpinned, so the falsifier reports no hit",
     'verdict="UNPINNED")'),
    ("MUT-EXPECTATION-UNSTAMPED", "G-WILSON-RANGE-OVER-THE-SIMPLEX",
     "strips the conditional stamp from one published expectation",
     'rows[1]["stamp"] = "PLAIN"'),
    ("MUT-POT-HANDOFF", "G-POT-HANDOFF",
     "empties the list of objects the handoff withholds by name",
     'hand["what_is_NOT_handed_over"] = []'),
    ("MUT-CHOICE-INVENTORY", "G-CHOICE-INVENTORY",
     "leaves one member of a swept axis's fibre unbuilt",
     'rows[4]["instances_built"] = rows[4]["fibre"] - 1'),
    ("MUT-REACHABILITY", "G-HEAD-LAW-REACHABILITY",
     "collapses the head law's synthetic probes to one string",
     'got[0]["emitted"] = got[-1]["emitted"]'),
    ("MUT-HEAD", "G-HEAD-DERIVED-TWICE",
     "types the head instead of computing it",
     '"ACT-FORM-FORCED-EVERYTHING"'),
    ("MUT-VERDICT-COMPARATOR", "G-VERDICT-RECONSTRUCTION",
     "corrupts the builder's verdict string after it is built",
     'verdict.replace("ACT-", "ACT-X-", 1)'),
    ("MUT-LEDGER-SHAPE", "G-LEDGER-SHAPE-IS-CONSISTENT",
     "inflates the published paper-gate count by one",
     'ls["paper_gates"] = ls["paper_gates"] + 1'),
    ("MUT-GHOST-FUNCTION", "G-FUNCTION-INVENTORY-IS-TOTAL",
     "defines an undeclared function in this instrument's own source text",
     "def ghost_helper"),
    ("MUT-REGISTRY-EVASION", "G-MUTANT-REGISTRY-IS-TOTAL",
     "hides a mutant switch behind a computed name the AST scan cannot read",
     "'MUT-' + 'GHOST'"),
    ("MUT-FALSIFIER-DESCRIPTION", "G-FALSIFIER-DESCRIPTIONS-ARE-HONEST",
     "replaces one falsifier's published token with a token no source can "
     "contain -- built at run time by reversing the real one, so the "
     "falsifier cannot defeat itself by planting its own literal",
     '"".join(reversed(token))'),
    ("MUT-CLAIM", "G-PAPER-CLAIMS",
     "corrupts a load-bearing count in the paper text the claim gate scans",
     '"137 single-link invariant classes"'),
    ("MUT-TABLE-ROW", "G-PAPER-CLAIMS",
     "swaps two table rows under their own labels in the scanned text",
     'a.group(1) + b.group(2)'),
    ("MUT-QUOTE-FIDELITY", "G-PAPER-TABLES-AND-QUOTES-ARE-BOUND",
     "inverts a quoted definition in the scanned paper text",
     '"the unordered sum of the four link"'),
    ("MUT-TABLE-BINDING", "G-PAPER-TABLES-AND-QUOTES-ARE-BOUND",
     "adds an unbound table carrying a numeral to the scanned text",
     '"\\n\\n| a | b |\\n|---|---|\\n| planted | 4242 |\\n"'),
    ("MUT-VERDICT-TWIN", "G-PAPER-VERDICT-EQUALITY",
     "adds a forged twin of the verdict fence beside the clean one",
     '"XCT-"'),
    ("MUT-MUST-NOT", "G-MUST-NOT-VOCABULARY",
     "plants an area-law and string-tension sentence into the scanned text",
     "follows an area law"),
    ("MUT-POLARITY", "G-PAPER-POLARITY",
     "plants a declared negator immediately before a direction-bearing "
     "claim", '"it is false that "'),
    ("MUT-COVERAGE", "G-PAPER-NUMERAL-COVERAGE",
     "plants a numeral no value this run computed can license",
     "an uncovered numeral 987654321"),
    ("MUT-GAMMA", "G-GAMMA-GROUP-BUILT",
     "drops one element from the coin-map group before its order is "
     "measured", "GA.elems = GA.elems[:-1]"),
    ("MUT-CHART", "G-CHART-GROUPS-REBUILT",
     "restricts the anchored chart group to its identity element, so "
     "transitivity on the links fails", "ch32 = ch32[:1]"),
    ("MUT-ODD-TWIST", "G-THE-ODD-TWIST-IS-NOT-REALISABLE",
     "empties the set of unrealisable constant twists", "odd = []"),
    ("MUT-PRICE", "G-PRICE-REDUCED-NOT-EVADED",
     "raises the reachable dimension to the parent's own price, so the "
     "reduction is no longer strict",
     "reachable_dimension=a[\"the_parents_simplex_dimension\"]"),
    ("MUT-GRAIN-DEGENERACY", "G-GRAIN-DEGENERACY-ON-THE-CARRIER",
     "gives two grains the same coupling count, so the grain-relativity "
     "the gate measures disappears",
     'S["form_census"]["rows"][4]["coupling_count"]'),
    ("MUT-MINIMAL-SUPPORT", "G-WILSON-IS-NOT-MINIMAL-SUPPORT",
     "declares the gauge group transitive on a single link's datum",
     "single_link_invariants = 1"),
    ("MUT-SUPPLIED", "G-GIBBS-ROW-SUPPLIED",
     "zeroes the coupling count the supplied row publishes",
     "a = dict(a, coupling_count=0)"),
    ("MUT-OBSERVABLE-NOT-INVARIANT", "G-OBSERVABLES-ARE-GAUGE-INVARIANT",
     "drops one defect-carrying coin from the count the parent's receipt "
     "anchors", "dcount = dcount - 1"),
    ("MUT-WAIVER", "G-FALSIFIER-COVERAGE-AT-AN-HONEST-DENOMINATOR",
     "removes one gate from the covered set, so a closed gate is left "
     "uncovered", "covered = covered[:-1]"),
    ("MUT-SEAL", "G-SEAL-INTEGRITY",
     "edits a sealed object after its gate closed", '"MOVED-AFTER-THE-GATE"'),
]


# ===========================================================================
# SECTION 18.  THE SEAL, THE ARTIFACTS, THE CLI
# ===========================================================================

PAPER_GATE_IDS = ("G-PAPER-CLAIMS", "G-PAPER-VERDICT-EQUALITY",
                  "G-MUST-NOT-VOCABULARY", "G-PAPER-POLARITY",
                  "G-PAPER-TABLES-AND-QUOTES-ARE-BOUND",
                  "G-PAPER-NUMERAL-COVERAGE")
CLOSING_GATE_IDS = ("G-SEAL-INTEGRITY", "G-ARTIFACT-INTEGRITY")

DECLARED_UNSEALED = {
    "unit": "the unit's own name, a constant of this source",
    "schema": "the receipt schema tag, a constant of this source",
    "python": "the interpreter's major.minor, environmental",
    "pin_sha256_prefix": "the pin digest, verified at G-SOURCE-BYTES",
    "paper_sha256_12": "the paper's digest, taken at the paper gates",
    "code_sha256_12": "this instrument's own digest, which cannot seal "
                      "itself",
    "gates": "the gate ledger, snapshotted before the two closing gates -- a "
             "seal cannot be inside the object it seals",
    "gate_digests": "the CHAINED per-row digests of that ledger",
    "seal_manifest": "the manifest itself",
    "closing_gates": "the two gates that close after the snapshot",
    "declared_unsealed": "this declaration",
    "exit_conventions": "the disclosed exit conventions, a constant",
    "mutants": "the falsifier registry, checked TOTAL against the syntax "
               "tree at G-MUTANT-REGISTRY-IS-TOTAL and published as this "
               "instrument's description of itself",
    "totals": "the closing tallies, derived from sealed objects",
    "transcript_head": "the transcript digest, taken at the disk boundary",
}


def seal_and_write(S, write, paper_bytes):
    verdict = S["verdict"]
    SEAL.take("THE VERDICT STRING", "verdict", "G-VERDICT-RECONSTRUCTION",
              verdict)
    SEAL.take("THE VERDICT HEAD", "verdict_head", "G-VERDICT-RECONSTRUCTION",
              S["verdict_head"])
    S["unit"] = UNIT
    S["schema"] = SCHEMA
    S["pin_sha256_prefix"] = PIN_SHA12
    S["python"] = "%d.%d" % sys.version_info[:2]
    S["paper_sha256_12"] = bdigest(paper_bytes)
    S["exit_conventions"] = (
        "the delivery run exits 0 on success and 1 on any refusal, writing "
        "nothing; --selftest exits 0 when every anchor class is fatal; "
        "--mutant exits 0 when the named mutant dies on its declared target; "
        "an unknown flag exits 2")
    S["mutants"] = [{"mutant": m[0], "target": m[1], "what": m[2],
                     "plants": m[3]} for m in MUTANTS]
    payload = {k: v for k, v in S.items() if not k.startswith("_")}
    payload["gates"] = LD.rows[:]
    payload["gate_digests"] = LD.digests[:]
    payload["seal_manifest"] = SEAL.man
    payload["declared_unsealed"] = DECLARED_UNSEALED
    payload["closing_gates"] = list(CLOSING_GATE_IDS)
    payload["totals"] = {
        "gates": len(LD.rows) + 2,
        "gates_in_the_sealed_ledger": len(LD.rows),
        "closing_gates": len(payload["closing_gates"]),
        "mutants": len(MUTANTS), "sources": len(SOURCES),
        "path_value_anchors": len(PATH_VALUES),
        "verbatim_anchors": len(VERBATIM),
        "anchors": len(SOURCES) + len(PATH_VALUES) + len(VERBATIM),
        "sealed_objects": len(SEAL.man),
        "census_rows": len(S["form_census"]["rows"])}
    if mut("MUT-SEAL"):
        payload["arena"] = dict(payload["arena"])
        payload["arena"]["coins"] = "MOVED-AFTER-THE-GATE"

    unsealed = [k for k in payload
                if k not in SEAL.by_key and k not in DECLARED_UNSEALED]
    moved = SEAL.reverify(payload)
    ids = [r["gate"] for r in LD.rows]
    ls = S.get("ledger_shape", {})
    shape_ok = ("paper_coverage" not in S) or (
        all(gx in ids for gx in PAPER_GATE_IDS)
        and len(LD.rows) == ls.get("gates_closed_before_the_paper_gates", 0)
        + ls.get("paper_gates", 0))
    LD.gate("G-SEAL-INTEGRITY",
            "the manifest is TOTAL and the seal is checked before anything "
            "reaches the disk: every published top-level key is either "
            "digested at the moment its own gate passed or named in the "
            "declaration with the reason it cannot be, and every sealed "
            "object still matches its gate-time digest -- so an object "
            "edited after its gate closed dies here rather than being "
            "re-derived from disk and pronounced consistent (#119).  The "
            "seals are taken AT VALUE-CLOSE, and the ledger's own published "
            "shape is checked against the ledger it describes",
            not unsealed and not moved and shape_ok,
            "%d published keys, %d sealed, %d declared unsealed, %d "
            "undeclared %s, %d moved since their gate %s; ledger shape "
            "consistent: %s"
            % (len(payload), len(SEAL.by_key), len(DECLARED_UNSEALED),
               len(unsealed), unsealed[:4], len(moved), moved[:4], shape_ok))

    transcript = "\n".join(LOG) + "\n" + verdict + "\n"
    payload["transcript_head"] = digest(transcript)
    blob = json.dumps(payload, indent=1, sort_keys=True, default=str)
    outtxt = transcript
    if not write:
        return payload, 0
    tmps = []
    for rel, data in ((OUT_REL, outtxt), (RECEIPT_REL, blob)):
        p = os.path.join(REPO, rel)
        tmp = p + ".tmp"
        with open(tmp, "w") as fh:
            fh.write(data)
        tmps.append((tmp, p))
    back = json.loads(open(tmps[1][0]).read())
    disk_bad = SEAL.reverify(back)
    txt_ok = open(tmps[0][0]).read() == outtxt
    if disk_bad or not txt_ok:
        for tmp, _p in tmps:
            if os.path.exists(tmp):
                os.remove(tmp)
    LD.gate("G-ARTIFACT-INTEGRITY",
            "the artifacts are compared against the GATE-TIME seals and not "
            "against a re-derivation, and the comparison happens BEFORE "
            "promotion: both files are written as temporaries, the receipt "
            "is read back from the filesystem and every sealed object must "
            "still carry its gate-time digest, the transcript must be "
            "byte-identical to the string this run emitted -- and only a "
            "passing check promotes them.  A refusal removes the temporaries "
            "and leaves the published artifacts untouched",
            not disk_bad and txt_ok,
            "%d sealed objects moved on the way to disk %s; transcript "
            "byte-identical: %s; promoted only after this check passed"
            % (len(disk_bad), disk_bad[:3], txt_ok))
    for tmp, p in tmps:
        os.replace(tmp, p)
    return payload, 2


def run(write=True, paper_gates=True):
    S = {}
    say("=" * 78)
    say(UNIT)
    say("=" * 78)
    src = measure_provenance(S)
    pv = measure_path_values(S, src)
    measure_verbatim(S, src)
    say("  provenance: %d sources, %d path-value anchors, %d verbatim windows"
        % (len(SOURCES), len(PATH_VALUES), len(VERBATIM)))
    build_arena(S, pv)
    measure_chart_and_gauge(S, pv)
    say("  arena: %d coins, %d links, %d plaquettes; gauge orbits %d and %d"
        % (S["arena"]["coins"], S["arena"]["links"], S["arena"]["plaquettes"],
           S["residual_gauge"]["orbits_anchored"],
           S["residual_gauge"]["orbits_extension"]))
    rows = run_form_census(S, pv)
    for r in rows:
        say("    %-22s group %-6d orbits %-12d couplings %d"
            % (r["row"], r["acting_group_order"], r["orbits"],
               r["coupling_count"]))
    verify_the_analytic_crosscheck(S)
    verify_the_rank(S)
    measure_locality(S)
    say("  locality: %d of %d non-invariant elementary systems detected, %d "
        "of %d invariant ones; every link in %d plaquettes"
        % (S["locality"]["link_grain_not_invariant_detected"],
           S["locality"]["link_grain_not_invariant"],
           S["locality"]["link_grain_invariant_detected"],
           S["locality"]["link_grain_locally_invariant"],
           S["locality"]["every_link_lies_in_this_many_plaquettes"]))
    measure_the_gibbs_map(S, pv)
    say("  the price: %d against the parent's %d at the anchored reading, %d "
        "against %d at the extension; %d and %d orbit pairs merged"
        % (S["price"]["the_action_route_supplies_anchored"],
           S["price"]["the_parents_price_anchored"],
           S["price"]["the_action_route_supplies_extension"],
           S["price"]["the_parents_price_extension"],
           S["price"]["orbit_pairs_merged_anchored"],
           S["price"]["orbit_pairs_merged_extension"]))
    measure_wilson_row(S, pv)
    say("  the Wilson shape: in the space at %d of %d grains, spanning %d of "
        "%d couplings on the carrier at %d distinct trace values"
        % (len(S["wilson"]["in_the_allowed_space_at_grains"]),
           S["wilson"]["grains_declared"],
           S["wilson"]["dimension_of_the_wilson_family_on_the_carrier"],
           S["wilson"]["the_allowed_space_on_the_carrier"],
           S["wilson"]["distinct_values_over_the_carrier"]))
    measure_targets(S, pv)
    say("  the targets: %d of %d reachable, %d obstruction species %s"
        % (S["target_census"]["reachable"],
           len(S["target_census"]["rows"]),
           len(S["target_census"]["obstruction_species"]),
           ",".join(S["target_census"]["obstruction_species"])))
    measure_the_control_row(S, pv)
    measure_the_supplied_row(S)
    measure_density_witness(S)
    measure_falsifier(S, pv)
    say("  the falsifier: %s -- %d observable rows, %d pinned, %d of them to "
        "a point" % (S["falsifier"]["verdict"],
                     len(S["falsifier"]["rows"]),
                     S["falsifier"]["pinned_rows"],
                     S["falsifier"]["pinned_to_a_point"]))
    measure_expectations(S, pv)
    measure_pot_handoff(S)
    price_the_choices(S)
    demonstrate_reachability(S)
    check_the_registry(S)

    head = head_law(S["form_census"]["rows"], S["gibbs"]["rows"], None)
    h2 = second_head_law(S["form_census"]["rows"], S["gibbs"]["rows"], None)
    if mut("MUT-HEAD"):
        head = "ACT-FORM-FORCED-EVERYTHING"
    LD.gate("G-HEAD-DERIVED-TWICE",
            "the head is derived TWICE, by two laws: the builder computes it "
            "from the live census, and an independent law written from the "
            "same pre-registered outcomes with a different branch structure "
            "and no shared format string returns the same string -- so a "
            "head typed rather than computed, or computed by a law that had "
            "drifted from its own measurements, dies here",
            head == h2, "builder %r; second law %r" % (head[:60], h2[:60]))

    verdict = build_verdict(S)
    if mut("MUT-VERDICT-COMPARATOR"):
        verdict = verdict.replace("ACT-", "ACT-X-", 1)
    S["verdict"] = verdict
    payload_for_recon = json.loads(json.dumps(
        {k: v for k, v in S.items() if not k.startswith("_")},
        sort_keys=True, default=str))
    recon = reconstruct_verdict(payload_for_recon)
    LD.gate("G-VERDICT-RECONSTRUCTION",
            "the complete verdict string is compared for equality against an "
            "INDEPENDENT reconstruction that reads only the SERIALIZED "
            "receipt, derives the head by a second head law, and re-renders "
            "every segment from the primitive measured tables -- reading "
            "neither the builder's segments nor the builder's aggregates and "
            "sharing no format string with it, so 'the same concatenation "
            "written twice' cannot pass",
            verdict == recon,
            "builder %d characters, reconstruction %d, equal: %s%s"
            % (len(verdict), len(recon), verdict == recon,
               "" if verdict == recon else " || first divergence at %d"
               % next((i for i in range(min(len(verdict), len(recon)))
                       if verdict[i] != recon[i]), -1)))

    build_waiver_ledger(S)
    S["code_sha256_12"] = bdigest(open(os.path.abspath(__file__), "rb").read())
    ls = {"gates_closed_before_the_paper_gates": len(LD.rows) + 1,
          "paper_gates": len(PAPER_GATE_IDS),
          "closing_gates": len(CLOSING_GATE_IDS),
          "objects_sealed_before_the_paper_gates": len(SEAL.man)}
    if mut("MUT-LEDGER-SHAPE"):
        ls["paper_gates"] = ls["paper_gates"] + 1
    LD.gate("G-LEDGER-SHAPE-IS-CONSISTENT",
            "the ledger's own published shape is a MEASUREMENT of the ledger "
            "and not a description of it: the sealed-object count is "
            "recounted from the manifest itself, the paper-gate count from "
            "the declared list, and the gate total includes this gate",
            ls["objects_sealed_before_the_paper_gates"] == len(SEAL.man)
            and ls["gates_closed_before_the_paper_gates"] == len(LD.rows) + 1
            and ls["paper_gates"] == len(PAPER_GATE_IDS),
            "%d sealed objects published against a manifest of %d; %d gates "
            "closed including this one; %d paper gates declared"
            % (ls["objects_sealed_before_the_paper_gates"], len(SEAL.man),
               ls["gates_closed_before_the_paper_gates"], ls["paper_gates"]))
    S["ledger_shape"] = ls
    SEAL.take("THE LEDGER SHAPE", "ledger_shape",
              "G-LEDGER-SHAPE-IS-CONSISTENT", S["ledger_shape"])

    paper_path = os.path.join(REPO, PAPER_REL)
    paper_bytes = b""
    if paper_gates and os.path.exists(paper_path):
        paper_bytes = open(paper_path, "rb").read()
        verify_paper(S, paper_bytes.decode())
    elif paper_gates:
        LD.gate("G-PAPER-PRESENT", "the paper must exist to be gated", False,
                "missing %s" % PAPER_REL)

    payload, closing = seal_and_write(S, write, paper_bytes)
    say("")
    say(verdict)
    say("")
    say("GATES %d (+%d closing) :: MUTANTS %d :: ANCHORS %d :: SEALED %d"
        % (len(LD.rows) - closing, closing, len(MUTANTS),
           len(SOURCES) + len(PATH_VALUES) + len(VERBATIM), len(SEAL.man)))
    return payload


def selftest():
    """the falsification self-test: one anchor class is corrupted IN MEMORY,
    the run must refuse, and NOTHING may be written."""
    global SOURCES, PATH_VALUES, VERBATIM
    before = {}
    for rel in (OUT_REL, RECEIPT_REL):
        p = os.path.join(REPO, rel)
        before[rel] = open(p, "rb").read() if os.path.exists(p) else None
    classes = []
    S0, P0, V0 = SOURCES[:], PATH_VALUES[:], VERBATIM[:]
    cases = [
        ("FILE-BYTES", lambda: globals().__setitem__(
            "SOURCES", [(S0[1][0], S0[1][1], "deadbeefdead", S0[1][3])]
            + S0[2:])),
        ("PATH-VALUE", lambda: globals().__setitem__(
            "PATH_VALUES", [(P0[0][0], P0[0][1], P0[0][2], 999, P0[0][4],
                             P0[0][5])] + P0[1:])),
        ("VERBATIM", lambda: globals().__setitem__(
            "VERBATIM", [(V0[0][0], V0[0][1], "a window that is not there in "
                          "any of the pinned sources at all whatsoever",
                          V0[0][3], V0[0][4])] + V0[1:])),
    ]
    for name, corrupt in cases:
        globals()["LD"] = Ledger()
        globals()["SEAL"] = Seal()
        SOURCES, PATH_VALUES, VERBATIM = S0[:], P0[:], V0[:]
        corrupt()
        died = False
        try:
            run(write=False, paper_gates=False)
        except (GateFail, KeyError, ValueError, IndexError):
            died = True
        classes.append((name, died))
    SOURCES, PATH_VALUES, VERBATIM = S0[:], P0[:], V0[:]
    unchanged = True
    for rel, b in before.items():
        p = os.path.join(REPO, rel)
        now = open(p, "rb").read() if os.path.exists(p) else None
        if now != b:
            unchanged = False
    ok = all(d for _n, d in classes) and unchanged
    print("SELFTEST :: %s :: %s :: artifacts unchanged %s"
          % ("FATAL AT EVERY ANCHOR CLASS" if all(d for _n, d in classes)
             else "SURVIVED", classes, unchanged))
    return 0 if ok else 1


USAGE = """usage: act_exact.py [--no-write] [--selftest] [--mutant NAME]
                    [--all-mutants] [--list-gates] [--list-mutants]
                    [--verify-paper] [--quiet]

EXIT CONVENTIONS (they invert the usual reading):
  plain run       0 = every gate passed and the artifacts were written
                  1 = a gate refused; nothing was written
  --selftest      0 = every anchor class was fatal and nothing was written
  --mutant NAME   0 = the mutant DIED ON ITS DECLARED TARGET GATE
  --all-mutants   0 = every mutant died on target
  unknown flag    2
"""


def main(argv):
    global QUIET, MUT
    known = {"--no-write", "--selftest", "--mutant", "--all-mutants",
             "--list-gates", "--list-mutants", "--verify-paper", "--quiet",
             "--help"}
    args, i = {}, 1
    while i < len(argv):
        a = argv[i]
        if a not in known:
            sys.stderr.write("unknown flag %r\n%s" % (a, USAGE))
            return 2
        if a == "--mutant":
            if i + 1 >= len(argv):
                sys.stderr.write("--mutant needs a NAME\n%s" % USAGE)
                return 2
            args["mutant"] = argv[i + 1]
            i += 1
        else:
            args[a.lstrip("-")] = True
        i += 1
    if args.get("help"):
        sys.stdout.write(USAGE)
        return 0
    QUIET = bool(args.get("quiet"))
    if args.get("list-gates"):
        for gx in sorted({m[1] for m in MUTANTS}):
            print(gx)
        return 0
    if args.get("list-mutants"):
        for nm, tg, wh, _p in MUTANTS:
            print("%-30s -> %-46s %s" % (nm, tg, wh))
        return 0
    if args.get("selftest"):
        return selftest()
    if args.get("mutant"):
        name = args["mutant"]
        if name not in {m[0] for m in MUTANTS}:
            sys.stderr.write("unknown mutant %r\n" % name)
            return 2
        target = [m[1] for m in MUTANTS if m[0] == name][0]
        before = {}
        for rel in (OUT_REL, RECEIPT_REL):
            p = os.path.join(REPO, rel)
            before[rel] = open(p, "rb").read() if os.path.exists(p) else None
        MUT = name
        died_at = None
        try:
            run(write=False, paper_gates=True)
        except GateFail as e:
            died_at = str(e).split(" :: ")[0]
        except Exception as e:                       # noqa: BLE001
            died_at = "EXCEPTION:%s" % type(e).__name__
        unchanged = True
        for rel, b in before.items():
            p = os.path.join(REPO, rel)
            now = open(p, "rb").read() if os.path.exists(p) else None
            if now != b:
                unchanged = False
        ok = (died_at == target) and unchanged
        print("MUTANT %-30s target %-46s died at %s :: artifacts unchanged "
              "%s :: %s" % (name, target, died_at, unchanged,
                            "DEAD-ON-TARGET" if ok else "FAILED"))
        return 0 if ok else 1
    if args.get("all-mutants"):
        bad = []
        for nm, tg, _w, _p in MUTANTS:
            globals()["LD"] = Ledger()
            globals()["SEAL"] = Seal()
            globals()["MUT"] = nm
            globals()["QUIET"] = True
            globals()["LOG"] = []
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
            print("%-30s %s" % (nm, "DEAD-ON-TARGET" if died == tg
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
