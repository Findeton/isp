#!/usr/bin/env python3
"""SMU / paper-27 -- THE STATIONARY MEASURE.

Paper-23 proved that no probability measure on R5's gauge configurations
DERIVES from the static census, and named the one candidate it could not
price: the stationary measure of a DYNAMICS on configuration space, absent
because nothing pinned supplies a dynamics there.  This unit DECLARES the
dynamics -- six families, every member run, each with its fibre priced and
none privileged -- and asks whether the stationary measure derives given the
declaration.  Paper-23's law is the gate: A COVARIANT CHAIN DERIVES IFF IT IS
IRREDUCIBLE.  Irreducibility is computed exactly, class by class; where a
chain derives, its stationary measure is computed by EXACT LINEAR ALGEBRA and
its uniqueness is gated rather than asserted; and the census then asks the
question the pin exists for -- does the measure MOVE across the declared
fibre?

Built against the frozen pin v14/note-smu-pin.md.  Exact arithmetic only: the
field is Q(zeta_8) carried as integer 5-tuples over the basis (1, z, z^2, z^3)
reduced modulo z^4 + 1 in lowest terms, so tuple equality is field equality;
every probability is a fractions.Fraction; every stationary vector is the
exact kernel of an exact matrix, obtained by elimination over Fraction and
never by iteration; no float enters any measurement, and an AST scan of this
file's own syntax tree is a gate.

THE PIN'S MUST-NOT, INHERITED VERBATIM FROM PAPER-23's REPAIRED GATE: the
confinement vocabulary stays behind its gate -- this unit makes NO area-law,
NO string-tension and NO potential claim, and grows no loop family.  What the
pin DOES license, and paper-23 did not, is a Wilson-expectation segment --
but only under a measure that derives at the RSQ standard GIVEN the declared
dynamics, and every expectation published carries the stamp
CONDITIONAL-ON-THE-DECLARED-DYNAMICS.  The licensing is enforced on the
product: every expectation-valued key at any depth of the payload must be
registered, must name its dynamics, must carry the stamp, and its dynamics
must carry a DERIVES verdict computed by this run.

EXIT CONVENTIONS, DISCLOSED (they invert the usual reading and the reader is
owed the inversion): the delivery run exits 0 when every gate passes and 1 on
any refusal, writing nothing; --selftest exits 0 when EVERY anchor class is
fatal; --mutant exits 0 when the named mutant DIES ON ITS DECLARED TARGET and
1 when it survives or dies elsewhere; --all-mutants exits 0 only when all of
them die on target; an unknown flag or a missing flag argument exits 2.
"""

import ast
import hashlib
import json
import os
import re
import sys
from fractions import Fraction

UNIT = "SMU / paper-27 -- the stationary measure"
PIN_SHA12 = "a1fca5e7b238"
SCHEMA = "smu-stationary-1"

QUIET = False
MUT = None
LOG = []


def say(msg=""):
    """--quiet suppresses the TERMINAL ECHO ONLY.  The transcript is the
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
# SECTION 1.  Q(zeta_8), EXACT
# ===========================================================================

def _g(a, b):
    while b:
        a, b = b, a % b
    return abs(a)


def fnorm(a0, a1, a2, a3, den):
    if den < 0:
        a0, a1, a2, a3, den = -a0, -a1, -a2, -a3, -den
    g = _g(_g(abs(a0), abs(a1)), _g(abs(a2), abs(a3)))
    g = _g(g, den)
    if g == 0:
        return (0, 0, 0, 0, 1)
    return (a0 // g, a1 // g, a2 // g, a3 // g, den // g)


ZERO = (0, 0, 0, 0, 1)
ONE = (1, 0, 0, 0, 1)


def fadd(a, b):
    return fnorm(a[0] * b[4] + b[0] * a[4], a[1] * b[4] + b[1] * a[4],
                 a[2] * b[4] + b[2] * a[4], a[3] * b[4] + b[3] * a[4],
                 a[4] * b[4])


def fneg(a):
    return (-a[0], -a[1], -a[2], -a[3], a[4])


def fmul(a, b):
    c = [0] * 7
    for i in range(4):
        if a[i] == 0:
            continue
        for j in range(4):
            c[i + j] += a[i] * b[j]
    return fnorm(c[0] - c[4], c[1] - c[5], c[2] - c[6], c[3], a[4] * b[4])


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
    if not is_rational(a):
        raise ValueError("not rational: %r" % (a,))
    return Fraction(a[0], a[4])


def in_q_sqrt2(a):
    """a + b*sqrt2 with sqrt2 = z - z^3: the coefficient of z^2 vanishes and
    the z and z^3 coefficients are opposite."""
    return a[2] == 0 and a[1] == -a[3]


def qsqrt2_pair(a):
    if not in_q_sqrt2(a):
        raise ValueError("not in Q(sqrt2): %r" % (a,))
    return (Fraction(a[0], a[4]), Fraction(a[1], a[4]))


def qsqrt2_str(a):
    p, q = qsqrt2_pair(a)
    if q == 0:
        return str(p)
    return "%s%s%s*sqrt2" % (p, "+" if q > 0 else "-", abs(q))


def qs_less(x, y):
    """exact ordering on Q(sqrt2): (a1 + b1 sqrt2) < (a2 + b2 sqrt2) decided
    by squaring, with no float and no surd approximation anywhere."""
    d = x[0] - y[0]
    e = y[1] - x[1]
    if e == 0:
        return d < 0
    if e > 0:
        return d <= 0 or d * d < 2 * e * e
    return d < 0 and d * d > 2 * e * e


INV_SQRT2 = (0, 1, 0, -1, 2)          # (z - z^3)/2 = 1/sqrt(2)


# ===========================================================================
# SECTION 2.  THE GATE LEDGER, THE SEAL
# ===========================================================================

class GateFail(Exception):
    pass


class Ledger:
    """every row is DIGESTED AT THE MOMENT IT CLOSES; a row edited after its
    gate closed no longer matches its own gate-time digest, in run and again
    at the disk boundary."""

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
    vouches the values passes, not the moment the enclosing object is
    finished.  The manifest is TOTAL -- every published top-level key is
    either sealed at the gate that produced it or named in the declaration
    with the reason it cannot be -- and an object whose sub-objects are
    sealed separately declares the omission in its own manifest row, so no
    published field is left inside a gate-to-seal window."""

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
        """the receipt key may be a PATH: a list step is resolved by the
        element's own 'instance' name, never by position, so a reordering
        cannot satisfy a seal taken on a different record."""
        cur = payload
        for part in key.split("/"):
            if isinstance(cur, list):
                hit = None
                for e in cur:
                    if isinstance(e, dict) and e.get("instance") == part:
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
                    cur, row["omitted_and_sealed_separately"])) != row["digest"]:
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
    ("S-PIN", "v14/note-smu-pin.md", "a1fca5e7b238",
     "THE PIN, frozen before this instrument existed"),
    ("S-P23-PAPER", "v14/paper-23-measure.md", "79cc67b4f6cd",
     "PARENT 1, paper-23 terminal at commit bb26ca4: the configuration "
     "measure, the invariant simplexes, the transitivity criterion, the "
     "derives-iff-irreducible law and the withholding machinery"),
    ("S-P23-CODE", "v14/code/r5m_measure_exact.py", "faf353385905",
     "PARENT 1's instrument -- read for its declared definitions and its "
     "must-not list only; nothing is imported from it"),
    ("S-P23-RECEIPT", "v14/code/r5m_measure_receipt.json", "c9edf97a5533",
     "PARENT 1's receipt: the orbit counts, the simplex dimensions, the "
     "monomial subgroup and the parent census this unit reproduces"),
    ("S-R5-PAPER", "v14/paper-18-gauge-rung.md", "62cfe5689d2c",
     "PARENT 2, R5 terminal at commit 987cd73: the 640-coin family, the "
     "link-indexed configurations, the chart group, the gauge action and "
     "the plaquette loops"),
    ("S-R5-CODE", "v14/code/r5_gauge_exact.py", "0d98de793b79",
     "PARENT 2's instrument -- read for its declared definitions only"),
    ("S-R5-RECEIPT", "v14/code/r5_gauge_receipt.json", "0c02b7684e5b",
     "PARENT 2's receipt: the anchored arena cardinalities and the census "
     "sets this unit re-weighs"),
    ("S-GI-PAPER", "v14/paper-16-gamma-iteration.md", "5c1df50673d4",
     "PARENT 3, the Gamma-iteration terminal at commit 2895a9a: the "
     "law-native step normaliser and the positional law it returns -- the "
     "rate source the pin names for candidate (c)"),
    ("S-GI-RECEIPT", "v14/code/giter_receipt.json", "42255f50328a",
     "PARENT 3's receipt: the law values at both legs"),
]

PAPER_REL = "v14/paper-27-smu.md"
OUT_REL = "v14/code/smu_output.txt"
RECEIPT_REL = "v14/code/smu_receipt.json"

BANNED_NAMES = ["subprocess", "numpy", "random", "scipy", "git"]
BANNED_CALLS = ["system", "popen", "check_output", "urlopen"]


def read_bytes(rel):
    """a pinned source that is ABSENT is a gate failure with its path named,
    not an uncaught traceback: the disclosed exit convention has to be true
    for a bare copy of this file too."""
    p = os.path.join(REPO, rel)
    if not os.path.exists(p):
        return None
    with open(p, "rb") as fh:
        return fh.read()


def load_sources():
    got = {}
    rows = []
    for name, rel, sha, what in SOURCES:
        b = read_bytes(rel)
        d = bdigest(b) if b is not None else "ABSENT-AT-ITS-PINNED-PATH"
        if mut("MUT-SOURCE-DRIFT") and name == "S-P23-RECEIPT":
            d = "000000000000"
        rows.append({"name": name, "path": rel, "pinned": sha, "measured": d,
                     "ok": d == sha, "what": what})
        got[name] = b
    return got, rows


# ---------------------------------------------------------------- path-value
PATH_VALUES = [
    # (anchor id, source, dotted path, expected, consumer gate, what)
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
     "G-CHART-ACTION-MEASURED", "the anchored chart group's order"),
    ("PV-NONFLAT", "S-R5-RECEIPT", "counts/nonflat_configs", 632,
     "G-PARENT-SETS-REBUILT", "the parent's non-flat census"),
    ("PV-NONCOMM", "S-R5-RECEIPT", "counts/noncommuting_configs", 576,
     "G-PARENT-SETS-REBUILT", "the parent's non-commuting census"),
    ("PV-DEFECT", "S-R5-RECEIPT", "counts/defect_carrying_coins", 384,
     "G-PARENT-SETS-REBUILT", "the parent's defect census"),
    ("PV-ORB32", "S-P23-RECEIPT",
     "candidate_invariance/uniqueness/CHART-32/orbits", 208,
     "G-GAUGE-WALK-CLASSES-ARE-THE-PARENTS-ORBITS",
     "paper-23's orbit count at the anchored chart reading"),
    ("PV-SIMP32", "S-P23-RECEIPT",
     "candidate_invariance/uniqueness/CHART-32/simplex_dimension", 207,
     "G-GAUGE-WALK-SIMPLEX-IS-THE-PARENTS-SIMPLEX",
     "paper-23's invariant simplex dimension at the anchored reading"),
    ("PV-ORB128", "S-P23-RECEIPT",
     "candidate_invariance/uniqueness/CHART-128/orbits", 120,
     "G-GAUGE-WALK-CLASSES-ARE-THE-PARENTS-ORBITS",
     "paper-23's orbit count at the extension reading"),
    ("PV-SIMP128", "S-P23-RECEIPT",
     "candidate_invariance/uniqueness/CHART-128/simplex_dimension", 119,
     "G-GAUGE-WALK-SIMPLEX-IS-THE-PARENTS-SIMPLEX",
     "paper-23's invariant simplex dimension at the extension reading"),
    ("PV-MONO", "S-P23-RECEIPT", "candidate_group_haar/monomial_coins", 128,
     "G-MONOMIAL-WALK-CARRIES-THE-PARENTS-HAAR",
     "paper-23's one canonical measure's carrier"),
    ("PV-PRODIN", "S-P23-RECEIPT", "candidate_group_haar/products_inside",
     278528, "G-COMPOSITION-WALK-BUILT",
     "the products that stay inside the family"),
    ("PV-PRODTOT", "S-P23-RECEIPT", "candidate_group_haar/products_total",
     409600, "G-COMPOSITION-WALK-BUILT", "the products attempted"),
    ("PV-SLICE", "S-P23-RECEIPT", "arena/uniform_slice", 640,
     "G-CARRIER-IS-THE-PARENTS-PRIMARY-CARRIER",
     "paper-23's primary carrier"),
    ("PV-FIXLOC", "S-P23-RECEIPT", "fixed_locus/chart_fixed_configurations",
     640, "G-CARRIER-IS-THE-PARENTS-PRIMARY-CARRIER",
     "the chart-fixed locus, which is that carrier"),
    ("PV-P23NF", "S-P23-RECEIPT", "parent_census/non_flat", 632,
     "G-PARENT-SETS-REBUILT", "paper-23's own reproduction of the set"),
    ("PV-P23NC", "S-P23-RECEIPT", "parent_census/non_commuting", 576,
     "G-PARENT-SETS-REBUILT", "paper-23's own reproduction of the set"),
    ("PV-LAW1", "S-GI-RECEIPT", "targets/law_value_leg1/0", "15/38",
     "G-LAW-NATIVE-RATE-SOURCE",
     "the law-native positional law, first position"),
    ("PV-LAW2", "S-GI-RECEIPT", "targets/law_value_leg1/1", "5/19",
     "G-LAW-NATIVE-RATE-SOURCE",
     "the law-native positional law, second position"),
    ("PV-LAW3", "S-GI-RECEIPT", "targets/law_value_leg1/2", "13/38",
     "G-LAW-NATIVE-RATE-SOURCE",
     "the law-native positional law, third position"),
    ("PV-LAW-LEG2", "S-GI-RECEIPT", "targets/law_value_leg2/0", "15/38",
     "G-LAW-NATIVE-RATE-SOURCE",
     "the same law value at the second leg -- leg-independent"),
    ("PV-P23-WIDEST", "S-P23-RECEIPT", "measure_comparison/widest/spread",
     "27/130", "G-RELATIVITY-CENSUS",
     "the widest spread paper-23 measured across INVARIANT measures -- the "
     "number this unit's own spread is compared against"),
    ("PV-P23-NC-COUNTING", "S-P23-RECEIPT", "measure_comparison/rows/2/"
     "counting", "9/10", "G-RELATIVITY-CENSUS",
     "the parent's non-commuting mass at the counting measure"),
    ("PV-P23-NC-ORB32", "S-P23-RECEIPT", "measure_comparison/rows/2/"
     "orbit_uniform_CHART-32", "9/13", "G-RELATIVITY-CENSUS",
     "the same mass at the parent's orbit-uniform null"),
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
    ("VB-PIN-LAW", "S-PIN",
     "paper-23's theorem\n   applies \u2014 derives iff irreducible",
     "G-IRREDUCIBILITY-IS-THE-CRITERION",
     "the pin's own statement of the criterion this unit applies"),
    ("VB-PIN-WILSON", "S-PIN",
     "expectations are computable ONLY under a measure that derives at the "
     "RSQ standard GIVEN the declared\n   dynamics",
     "G-WILSON-LICENCE",
     "the pin's licensing condition for the Wilson segment"),
    ("VB-PIN-MUSTNOT", "S-PIN",
     "The confinement\n   vocabulary stays behind its gate: no area-law,\n"
     "   string-tension, or potential claim",
     "G-MUST-NOT-VOCABULARY",
     "the must-not list this unit inherits verbatim"),
    ("VB-PIN-RELATIVITY", "S-PIN",
     "does the stationary measure MOVE across the declared-dynamics\n"
     "   fiber?",
     "G-RELATIVITY-CENSUS",
     "the pin's fourth stage, which this unit answers"),
    ("VB-P23-LAW", "S-P23-PAPER",
     "a covariant chain's stationary measures are invariant, so it can only "
     "ever pick a point of the same simplex, and it\nfixes that point "
     "uniquely exactly when **irreducibility** supplies the\ntransitivity "
     "the symmetry group does not",
     "G-IRREDUCIBILITY-IS-THE-CRITERION",
     "paper-23's own statement of the obligation this unit discharges"),
    ("VB-P23-ABSENT", "S-P23-PAPER",
     "A stationary measure needs a dynamics to be stationary for.",
     "G-DECLARED-DYNAMICS-CENSUS",
     "the sentence that made this row NOT-CENSUSABLE for the parent"),
    ("VB-P23-PRICE", "S-P23-PAPER",
     "one point of the invariant simplex over that carrier's orbits** \u2014 a\n"
     "   207-dimensional simplex at the anchored chart reading, and\n"
     "   119 independent numbers at the extension reading",
     "G-PRICE-IS-CONSERVED",
     "the price this unit measures the dynamics declaration to reproduce"),
    ("VB-P23-INVARIANT", "S-P23-PAPER",
     "A measure is invariant under a group acting on a finite set if and "
     "only if it\nis constant on the orbits.",
     "G-GAUGE-WALK-SIMPLEX-IS-THE-PARENTS-SIMPLEX",
     "the characterisation the gauge walk's stationary simplex instantiates"),
    ("VB-P23-HAAR", "S-P23-PAPER",
     "The 128 monomial coins are closed under multiplication and under\n"
     "inverse",
     "G-MONOMIAL-WALK-CARRIES-THE-PARENTS-HAAR",
     "the parent's one canonical measure, which is one closed class here"),
    ("VB-R5-PLAQ", "S-R5-PAPER",
     "the holonomy is the ordered product of the\nfour link operators around "
     "the boundary, each inverted where the boundary runs\nagainst the "
     "link's own direction",
     "G-WILSON-OBSERVABLE-REBUILT",
     "the loop observable's definition, rebuilt here from these words"),
    ("VB-R5-BLOCK", "S-R5-PAPER",
     "the whole holonomy lives in a four-by-four block",
     "G-WILSON-OBSERVABLE-REBUILT",
     "why the declared loop observable is the four-corner trace"),
    ("VB-GI-NATIVE", "S-GI-PAPER",
     "it holds under an arbitrary exact re-pricing of every priced event, so "
     "it is\nlaw-native and not a fact about this carrier",
     "G-LAW-NATIVE-RATE-SOURCE",
     "why the rate source for candidate (c) is law-native"),
]


def wsnorm(s):
    return re.sub(r"\s+", " ", s).strip()


def mnorm(s):
    """#125: whitespace AND markdown-prefix normalisation, with inline
    emphasis stripped, so a claim under asterisks is the same claim and a
    needle broken across lines is still located."""
    s = re.sub(r"[*_`]+", "", s)
    s = re.sub(r"^\s*[>\-\*\+]\s+", " ", s, flags=re.M)
    return re.sub(r"\s+", " ", s).strip().lower()


# ===========================================================================
# SECTION 4.  THE ARENA, REBUILT FROM THE PARENTS' DECLARED DEFINITIONS
# ===========================================================================

def build_alphabet():
    """R4's coefficient alphabet as R5 declares it: 0 together with zeta_8^t
    times a modulus in {1, 1/2, 1/sqrt2}.  The size is a measurement against
    the anchored value, never a typed constant."""
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
    """THE COIN FAMILY, DERIVED: a coin is a 2x2 unitary all four of whose
    entries lie in the alphabet.  Exhaustive over the admissible rows."""
    rows = [(a, b) for a in alphabet for b in alphabet
            if fadd(fnormsq(a), fnormsq(b)) == ONE]
    coins = []
    for (a, b) in rows:
        for (c, d) in rows:
            if fadd(fmul(a, fconj(c)), fmul(b, fconj(d))) == ZERO:
                coins.append((a, b, c, d))
    return coins, rows


def coin_sector(m):
    a, b, c, d = m
    if b == ZERO and c == ZERO:
        return "DIAGONAL"
    if a == ZERO and d == ZERO:
        return "ANTIDIAGONAL"
    if a != ZERO and b != ZERO and c != ZERO and d != ZERO:
        return "BALANCED"
    return "OTHER"


def coin_unitary_second_route(m):
    a, b, c, d = m
    return (fadd(fmul(fconj(a), a), fmul(fconj(c), c)) == ONE
            and fadd(fmul(fconj(b), b), fmul(fconj(d), d)) == ONE
            and fadd(fmul(fconj(a), b), fmul(fconj(c), d)) == ZERO)


def cmul(A, B):
    a, b, c, d = A
    e, f, g, h = B
    return (fadd(fmul(a, e), fmul(b, g)), fadd(fmul(a, f), fmul(b, h)),
            fadd(fmul(c, e), fmul(d, g)), fadd(fmul(c, f), fmul(d, h)))


def cdag(A):
    a, b, c, d = A
    return (fconj(a), fconj(c), fconj(b), fconj(d))


def is_monomial(m):
    a, b, c, d = m
    return (b == ZERO and c == ZERO) or (a == ZERO and d == ZERO)


E1, E2 = (1, 0), (0, 1)
EDIR = (E1, E2)


class Lattice:
    def __init__(self, L):
        self.L = L
        self.sites = [(x, y) for x in range(L) for y in range(L)]
        self.idx = {s: i for i, s in enumerate(self.sites)}
        self.links = [(s, d) for s in self.sites for d in range(2)]
        self.lidx = {l: i for i, l in enumerate(self.links)}
        self.plaqs = list(self.sites)

    def addv(self, s, v):
        return ((s[0] + v[0]) % self.L, (s[1] + v[1]) % self.L)

    def ends(self, l):
        return l[0], self.addv(l[0], EDIR[l[1]])

    def boundary(self, p):
        """p -> p+e1 -> p+e1+e2 -> p+e2 -> p; -1 means traversed against the
        link's own direction, so its operator is inverted."""
        return (((p, 0), 1), ((self.addv(p, E1), 1), 1),
                ((self.addv(p, E2), 0), -1), ((p, 1), -1))


def point_symmetries():
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
    pts = point_symmetries() if extended else [(False, 1, 1), (True, 1, 1)]
    return [(v, g) for v in lat.sites for g in pts]


# the four declared generators of the extension: the two lattice
# translations, the diagonal swap and one axis reflection.  They generate the
# whole order-128 chart group, and closure is measured against them.
EXT_GENERATORS = [((1, 0), (False, 1, 1)), ((0, 1), (False, 1, 1)),
                  ((0, 0), (True, 1, 1)), ((0, 0), (False, -1, 1))]


def transported_link(lat, l, elem):
    """the image of a link, with the domino's orientation tracked.  Where the
    point part reverses the direction the transported coin is the SWAP
    CONJUGATE -- the coin read from the other end of its own domino."""
    v, g = elem
    s, d = l
    d2, sign = point_on_dir(g, d)
    s2 = lat.addv(apply_point(g, s, lat.L), v)
    if sign > 0:
        return (s2, d2), False
    return (((s2[0] - EDIR[d2][0]) % lat.L,
             (s2[1] - EDIR[d2][1]) % lat.L), d2), True


def swap_conjugate(m):
    """X U X."""
    a, b, c, d = m
    return (d, c, b, a)


def gauge_twist(m, k):
    """the site-diagonal gauge acts on a link's coin by conjugation with
    D = diag(zeta_8^p, zeta_8^q); the action depends on k = p - q alone."""
    a, b, c, d = m
    return (a, fmul(zpow(k), b), fmul(zpow(-k), c), d)


def link_op(lat, l, m, n):
    a, b, c, d = m
    t, h = lat.ends(l)
    it, ih = lat.idx[t], lat.idx[h]
    M = {(i, i): ONE for i in range(n) if i != it and i != ih}
    M[(it, it)] = a
    M[(it, ih)] = b
    M[(ih, it)] = c
    M[(ih, ih)] = d
    return {k: v for k, v in M.items() if v != ZERO}


def smul(A, B):
    rows = {}
    for (i, k), v in A.items():
        rows.setdefault(k, []).append((i, v))
    out = {}
    for (k, j), w in B.items():
        for (i, v) in rows.get(k, ()):
            p = fmul(v, w)
            if p == ZERO:
                continue
            out[(i, j)] = fadd(out.get((i, j), ZERO), p)
    return {k: v for k, v in out.items() if v != ZERO}


def sdag(A):
    return {(j, i): fconj(v) for (i, j), v in A.items()}


def sident(n):
    return {(i, i): ONE for i in range(n)}


def holonomy(lat, p, cfg, n):
    """W_p = L4^-1 L3^-1 L2 L1, the ordered product around the boundary."""
    W = sident(n)
    for (l, o) in lat.boundary(p):
        M = link_op(lat, l, cfg[l], n)
        if o < 0:
            M = sdag(M)
        W = smul(M, W)
    return W


def plaq_corners(lat, p):
    return [lat.idx[p], lat.idx[lat.addv(p, E1)],
            lat.idx[lat.addv(p, (1, 1))], lat.idx[lat.addv(p, E2)]]


def uniform_cfg(lat, m):
    return {l: m for l in lat.links}


# ===========================================================================
# SECTION 5.  CHAIN MACHINERY -- exact, and every route exact linear algebra
# ===========================================================================

def sccs(n, adj):
    """Tarjan, iterative: the communicating classes of the chain's own
    transition digraph, computed exactly from the support of P."""
    index = [None] * n
    low = [0] * n
    onstk = [False] * n
    stk = []
    out = []
    counter = [0]
    for root in range(n):
        if index[root] is not None:
            continue
        work = [(root, iter(adj[root]))]
        index[root] = low[root] = counter[0]
        counter[0] += 1
        stk.append(root)
        onstk[root] = True
        while work:
            v, it = work[-1]
            advanced = False
            for w in it:
                if index[w] is None:
                    index[w] = low[w] = counter[0]
                    counter[0] += 1
                    stk.append(w)
                    onstk[w] = True
                    work.append((w, iter(adj[w])))
                    advanced = True
                    break
                elif onstk[w] and index[w] < low[v]:
                    low[v] = index[w]
            if advanced:
                continue
            work.pop()
            if work:
                u = work[-1][0]
                if low[v] < low[u]:
                    low[u] = low[v]
            if low[v] == index[v]:
                comp = []
                while True:
                    w = stk.pop()
                    onstk[w] = False
                    comp.append(w)
                    if w == v:
                        break
                out.append(sorted(comp))
    return out


def closed_classes(n, adj, comps):
    """#87: closedness is decided PER CLASS against that class's own
    out-edges, never against a count."""
    cid = [None] * n
    for i, c in enumerate(comps):
        for v in c:
            cid[v] = i
    closed = []
    for i, c in enumerate(comps):
        ok = True
        for v in c:
            for w in adj[v]:
                if cid[w] != i:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            closed.append(i)
    return closed, cid


def support_adj(P, n):
    return [sorted(j for j, v in P[i].items() if v) for i in range(n)]


def kernel_basis(rows, n):
    """exact reduced row echelon over Fraction; returns a basis of the right
    kernel together with the rank.  No pivoting heuristic, no tolerance: a
    pivot is a nonzero exact rational."""
    M = [r[:] for r in rows]
    piv = []
    r = 0
    for c in range(n):
        p = None
        for i in range(r, len(M)):
            if M[i][c]:
                p = i
                break
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        inv = 1 / M[r][c]
        Mr = [x * inv for x in M[r]]
        M[r] = Mr
        for i in range(len(M)):
            if i != r and M[i][c]:
                f = M[i][c]
                Mi = M[i]
                M[i] = [Mi[j] - f * Mr[j] if Mr[j] else Mi[j]
                        for j in range(n)]
        piv.append(c)
        r += 1
        if r == len(M):
            break
    pset = set(piv)
    free = [c for c in range(n) if c not in pset]
    basis = []
    for f in free:
        v = [Fraction(0)] * n
        v[f] = Fraction(1)
        for i, c in enumerate(piv):
            v[c] = -M[i][f]
        basis.append(v)
    return basis, len(piv)


def stationary_by_elimination(P, n):
    """THE EXACT SOLVE: the kernel of (P^T - I), by elimination over
    Fraction, each basis vector normalised to total mass 1 where it can be.
    This is the only route by which a stationary vector enters this unit at
    or below the declared elimination cap."""
    A = [[Fraction(0)] * n for _ in range(n)]
    for i in range(n):
        for j, v in P[i].items():
            A[j][i] += v
    for i in range(n):
        A[i][i] -= 1
    bas, rk = kernel_basis(A, n)
    out = []
    for v in bas:
        s = sum(v)
        out.append([x / s for x in v] if s else v)
    return out, rk


def verify_stationary(P, pi, n):
    """pi P = pi, exactly, at full size -- the per-object check that binds
    every instance whatever route produced its vector."""
    chk = [Fraction(0)] * n
    for i in range(n):
        p = pi[i]
        if p:
            for j, v in P[i].items():
                chk[j] += p * v
    return chk == pi and sum(pi) == 1 and all(x >= 0 for x in pi)


def row_stochastic(P, n):
    return all(sum(P[i].values()) == 1 for i in range(n))


def covariance_failures(P, n, perms):
    """P(gx, gy) = P(x, y) for every declared symmetry g and every pair --
    checked as a per-row identity of permuted rows, not as a count."""
    bad = 0
    for g in perms:
        for i in range(n):
            src = P[i]
            tgt = P[g[i]]
            if len(src) != len(tgt):
                bad += 1
                continue
            for j, v in src.items():
                if tgt.get(g[j]) != v:
                    bad += 1
                    break
    return bad


def lump(P, n, blocks, bid):
    """the exact quotient chain on the blocks; returns (Q, failures) where a
    failure is a block on which the row sums into the blocks are not
    constant, so lumpability is MEASURED and not assumed."""
    Q = []
    fails = 0
    for blk in blocks:
        ref = None
        for x in blk:
            r = {}
            for j, v in P[x].items():
                b = bid[j]
                r[b] = r.get(b, Fraction(0)) + v
            if ref is None:
                ref = r
            elif r != ref:
                fails += 1
        Q.append(ref)
    return Q, fails


def orbits_from_perms(n, perms):
    seen = [False] * n
    out = []
    for i in range(n):
        if seen[i]:
            continue
        cl = sorted({g[i] for g in perms})
        for j in cl:
            seen[j] = True
        out.append(cl)
    return out


def gen_perm_group(n, gens):
    ident = tuple(range(n))
    G = {ident}
    fr = [ident]
    while fr:
        nxt = []
        for g in fr:
            for s in gens:
                h = tuple(s[g[i]] for i in range(n))
                if h not in G:
                    G.add(h)
                    nxt.append(h)
        fr = nxt
    return sorted(G)


def group_walk(n, perms):
    """the uniform random walk generated by a declared group action: one
    step applies a uniformly drawn group element."""
    P = []
    w = Fraction(1, len(perms))
    for i in range(n):
        row = {}
        for g in perms:
            row[g[i]] = row.get(g[i], Fraction(0)) + w
        P.append(row)
    return P


def metropolis(target, n):
    """the Metropolis chain at a declared target with the uniform proposal:
    accept y from x with probability min(1, pi(y)/pi(x)).  Reversible with
    respect to the target by construction, irreducible because the proposal
    is, hence the target is its unique stationary measure -- and all three
    of those are MEASURED below rather than quoted."""
    P = []
    for i in range(n):
        row = {}
        stay = Fraction(1)
        ti = target[i]
        for j in range(n):
            if j == i:
                continue
            a = Fraction(1) if target[j] >= ti else target[j] / ti
            p = a / n
            if p:
                row[j] = p
                stay -= p
        if stay:
            row[i] = row.get(i, Fraction(0)) + stay
        P.append(row)
    return P


def reversibility_failures(P, pi, n):
    bad = 0
    for i in range(n):
        for j, v in P[i].items():
            if pi[i] * v != pi[j] * P[j].get(i, Fraction(0)):
                bad += 1
    return bad


def has_self_loop(P, cls):
    return any(P[i].get(i, Fraction(0)) > 0 for i in cls)


def born(A):
    """B(U) = |U| entrywise-squared -- the substrate's own Born layer."""
    return {k: fnormsq(v) for k, v in A.items()}


def bmul(A, B):
    return smul(A, B)


# ===========================================================================
# SECTION 6.  THE MEASUREMENTS
# ===========================================================================

def measure_provenance(S):
    src, rows = load_sources()
    bad = [r for r in rows if not r["ok"]]
    LD.gate("G-SOURCE-BYTES",
            "every pinned source is read at its declared relative path and "
            "its sha256-12 measured against the value frozen in this "
            "instrument, so a parent edited after this unit was built stops "
            "this run; the repository is read at NO moving reference at all "
            "-- no ledger, no STATUS, no worktree scan, no version-control "
            "call -- so this run is correct off-tree and in a directory "
            "with no version control (#91, #46)",
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
    LD.gate("G-EXACT-ARITHMETIC-BY-AST",
            "the instrument's own syntax tree carries NO float literal, no "
            "banned import and no banned call, so 'exact arithmetic only' is "
            "a property of this source and not a promise about it: every "
            "probability is a Fraction, every field element an integer "
            "5-tuple, and every stationary vector the exact kernel of an "
            "exact matrix",
            not floats and not badimp and not calls,
            "%d float literals, banned imports %s, banned calls %s"
            % (len(floats), badimp, sorted(set(calls))))
    S["arithmetic"] = {"float_literals": len(floats),
                       "banned_imports": badimp,
                       "banned_calls": sorted(set(calls)),
                       "field": "Q(zeta_8) as integer 5-tuples over "
                                "(1, z, z^2, z^3) mod z^4+1",
                       "probabilities": "fractions.Fraction",
                       "stationary_vectors": "exact kernel by elimination "
                                             "over Fraction"}
    SEAL.take("THE ARITHMETIC", "arithmetic", "G-EXACT-ARITHMETIC-BY-AST",
              S["arithmetic"])
    return src


def measure_path_values(S, src):
    rows = []
    cache = {}
    for aid, sname, path, want, consumer, what in PATH_VALUES:
        if sname not in cache:
            cache[sname] = json.loads(src[sname].decode())
        got = dig(cache[sname], path)
        if mut("MUT-PATH-VALUE") and aid == "PV-ORB32":
            got = 999
        rows.append({"anchor": aid, "source": sname, "path": path,
                     "declared": want, "measured": got, "ok": got == want,
                     "consumer": consumer, "what": what})
    bad = [r for r in rows if not r["ok"]]
    LD.gate("G-PATH-VALUE-ANCHORS",
            "every inherited quantity is a (path, value) pair: the path must "
            "resolve in the pinned receipt AND the value there must be the "
            "one this instrument declares, and each is bound to the gate "
            "that consumes it, so a parent that moved a number under a "
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
        if mut("MUT-VERBATIM") and aid == "VB-P23-LAW":
            window = window.replace("irreducibility", "reducibility")
        needle = mnorm(window)
        n = hay.count(needle)
        # the perturbation: a content-bearing token is altered and the window
        # must stop being locatable
        toks = [t for t in re.findall(r"[A-Za-z0-9]+", window) if len(t) > 3]
        pert = window.replace(toks[-1], toks[-1] + "X", 1) if toks else window
        pn = hay.count(mnorm(pert))
        ok = (n == 1 and pn == 0 and len(needle) >= 40)
        rows.append({"anchor": aid, "source": sname, "chars": len(needle),
                     "floor": 40, "located": n, "perturbed_located": pn,
                     "ok": ok, "consumer": consumer, "what": what,
                     "digest": bdigest(needle.encode())})
    bad = [r for r in rows if not r["ok"]]
    LD.gate("G-VERBATIM-ANCHORS",
            "every quotation this paper makes of a parent is located EXACTLY "
            "ONCE in that parent's pinned bytes under whitespace and "
            "markdown-prefix normalisation (#125), is pinned by its own "
            "digest and its own character count against a declared floor, "
            "stops being locatable when a content-bearing token is "
            "perturbed, and is bound to the gate that consumes it -- so the "
            "anchor binds QUOTE FIDELITY and not mere existence (#62)",
            not bad, "%d of %d verbatim windows located exactly once and "
            "falsified under perturbation; failing %s"
            % (len(rows) - len(bad), len(rows), [b["anchor"] for b in bad]))
    S["verbatim_anchors"] = rows
    SEAL.take("THE VERBATIM ANCHORS", "verbatim_anchors",
              "G-VERBATIM-ANCHORS", rows)
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
    lat = Lattice(4)
    sect = {}
    for m in coins:
        sect[coin_sector(m)] = sect.get(coin_sector(m), 0) + 1
    unit_ok = sum(1 for m in coins if coin_unitary_second_route(m))
    if mut("MUT-ARENA"):
        coins = coins[:-1]
    ok = (len(alph) == pv["PV-ALPH"] and len(coins) == pv["PV-COINS"]
          and sect.get("DIAGONAL") == pv["PV-DIAG"]
          and sect.get("ANTIDIAGONAL") == pv["PV-ANTI"]
          and sect.get("BALANCED") == pv["PV-BAL"]
          and sect.get("OTHER") is None
          and unit_ok == len(coins)
          and len(lat.sites) == pv["PV-SITES"]
          and len(lat.links) == pv["PV-LINKS"]
          and len(lat.plaqs) == pv["PV-PLAQ"])
    LD.gate("G-ARENA-REBUILT",
            "the arena is REBUILT from the parents' declared definitions and "
            "not imported: the alphabet is enumerated from its declared "
            "shape, the coin family exhaustively from the admissible rows, "
            "the link and plaquette sets derived from the lattice -- and "
            "every cardinality is measured against the parent's receipt at a "
            "named path, with unitarity confirmed by a second route on every "
            "coin",
            ok, "alphabet %d, coins %d (%s), unitary-by-second-route %d, "
            "sites %d, links %d, plaquettes %d"
            % (len(alph), len(coins), sorted(sect.items()), unit_ok,
               len(lat.sites), len(lat.links), len(lat.plaqs)))
    S["_alph"], S["_coins"], S["_lat"] = alph, coins, lat
    S["_cidx"] = {m: i for i, m in enumerate(coins)}
    S["_sector"] = [coin_sector(m) for m in coins]
    S["arena"] = {
        "lattice": "(Z_L)^2", "L": lat.L, "d": 2,
        "sites": len(lat.sites), "links": len(lat.links),
        "plaquettes": len(lat.plaqs), "alphabet": len(alph),
        "admissible_rows": len(rows), "coins": len(coins),
        "sectors": dict(sorted(sect.items())),
        "field": "Q(zeta_8)",
        "configuration_space": "640^32, NOT the carrier of this unit",
    }
    SEAL.take("THE ARENA", "arena", "G-ARENA-REBUILT", S["arena"])

    # the carrier: paper-23's primary carrier, which is the chart-fixed locus.
    # The identity is established ELEMENT-WISE, on an object this run derives,
    # and not by a cardinality two upstream gates have already forced equal:
    # the anchored chart group is measured TRANSITIVE on the link set and
    # measured to reverse no link, and a configuration fixed by a group
    # transitive on the links and reversing none of them is constant -- so the
    # chart-fixed locus of the FULL configuration space is exactly the uniform
    # configurations, one per coin.
    els32 = chart_elements(lat, False)
    if mut("MUT-CARRIER"):
        els32 = [e for e in els32 if e == ((0, 0), (False, 1, 1))]
    reach = {lat.links[0]}
    frontier = [lat.links[0]]
    revs = 0
    while frontier:
        nxt = []
        for l in frontier:
            for e in els32:
                im, rev = transported_link(lat, l, e)
                if rev:
                    revs += 1
                if im not in reach:
                    reach.add(im)
                    nxt.append(im)
        frontier = nxt
    link_transitive = (len(reach) == len(lat.links))
    carrier_ok = (link_transitive and revs == 0
                  and len(coins) == pv["PV-SLICE"] == pv["PV-FIXLOC"])
    LD.gate("G-CARRIER-IS-THE-PARENTS-PRIMARY-CARRIER",
            "the carrier of this unit is the parent's own primary carrier -- "
            "the uniform configurations, one coin repeated on every link, "
            "which paper-23 measured to be exactly the chart-fixed locus of "
            "the anchored chart -- so this unit's dynamics act where the "
            "parent's simplex lives and the two are comparable object for "
            "object.  The identity is measured ELEMENT-WISE rather than by "
            "cardinality: the anchored chart group is transitive on the link "
            "set and reverses no link, so a chart-fixed configuration is "
            "constant and the fixed locus of the full configuration space is "
            "exactly the uniform ones.  The full configuration space is not a "
            "carrier here and is named as scope",
            carrier_ok,
            "the chart group reaches %d of %d links from one, with %d "
            "reversals; carrier %d states; parent's uniform slice %d; "
            "parent's chart-fixed locus %d"
            % (len(reach), len(lat.links), revs, len(coins), pv["PV-SLICE"],
               pv["PV-FIXLOC"]))
    S["carrier"] = {
        "states": len(coins),
        "links_reached_from_one_by_the_chart_group": len(reach),
        "links": len(lat.links),
        "chart_reversals_on_the_link_set": revs,
        "the_chart_group_is_transitive_on_the_links": link_transitive,
        "why_the_fixed_locus_is_exactly_the_uniform_configurations":
            "A-GROUP-TRANSITIVE-ON-THE-LINKS-AND-REVERSING-NONE-FIXES-ONLY-"
            "THE-CONSTANT-CONFIGURATIONS",
    }
    SEAL.take("THE CARRIER", "carrier",
              "G-CARRIER-IS-THE-PARENTS-PRIMARY-CARRIER", S["carrier"])
    return lat, coins


def measure_chart_action(S, pv):
    """WHETHER the chart group acts on the carrier at all -- measured, not
    assumed.  It is the first surprise of this unit: at the extension
    reading it does not."""
    lat, coins = S["_lat"], S["_coins"]
    cidx = S["_cidx"]
    out = {}
    for nm, ext in (("CHART-32", False), ("CHART-128", True)):
        els = chart_elements(lat, ext)
        norev = allrev = mixed = 0
        for e in els:
            flags = {transported_link(lat, l, e)[1] for l in lat.links}
            if flags == {False}:
                norev += 1
            elif flags == {True}:
                allrev += 1
            else:
                mixed += 1
        out[nm] = {"order": len(els), "no_reversal": norev,
                   "all_reversal": allrev, "mixed_reversal": mixed,
                   "acts_on_the_carrier": mixed == 0}
    if mut("MUT-CHART-ACTION"):
        out["CHART-128"]["mixed_reversal"] = 0
        out["CHART-128"]["acts_on_the_carrier"] = True
    ok = (out["CHART-32"]["order"] == pv["PV-CHART"]
          and out["CHART-32"]["acts_on_the_carrier"]
          and out["CHART-32"]["no_reversal"] == out["CHART-32"]["order"]
          and not out["CHART-128"]["acts_on_the_carrier"])
    LD.gate("G-CHART-ACTION-MEASURED",
            "whether a declared group ACTS on the declared carrier is a "
            "measurement and it is taken first, element by element: an "
            "element carries a uniform configuration to a uniform one "
            "exactly when its reversal flag is constant over the link set.  "
            "At the anchored reading every element has no reversal at all, "
            "so the chart group acts -- trivially.  At the extension "
            "reading the flag is mixed on some elements, so the extension "
            "does NOT act on this carrier and a walk cannot be declared "
            "there without enlarging it",
            ok, "CHART-32 %s; CHART-128 %s"
            % (out["CHART-32"], out["CHART-128"]))

    # the enlargement, computed as an orbit closure
    states = set((i, i) for i in range(len(coins)))
    frontier = list(states)
    els = chart_elements(lat, True)
    while frontier:
        nxt = []
        for st in frontier:
            for e in els:
                img = {}
                bad = False
                for l in lat.links:
                    im, rev = transported_link(lat, l, e)
                    srcm = coins[st[0]] if l[1] == 0 else coins[st[1]]
                    v = swap_conjugate(srcm) if rev else srcm
                    prev = img.setdefault(im[1], v)
                    if prev != v:
                        bad = True
                if bad:
                    continue
                t = (cidx[img[0]], cidx[img[1]])
                if t not in states:
                    states.add(t)
                    nxt.append(t)
        frontier = nxt
    states = sorted(states)
    if mut("MUT-ENLARGEMENT"):
        states = states[:len(coins)]
    # closure is MEASURED, state by state, against the four declared
    # generators of the extension -- not asserted from the fixed-point loop
    # that built it
    sset = set(states)
    escapes = 0
    for e in EXT_GENERATORS:
        tmap = {l: transported_link(lat, l, e) for l in lat.links}
        for st in states:
            img = {}
            broke = False
            for l in lat.links:
                im, rev = tmap[l]
                srcm = coins[st[0]] if l[1] == 0 else coins[st[1]]
                v = swap_conjugate(srcm) if rev else srcm
                prev = img.setdefault(im[1], v)
                if prev != v:
                    broke = True
            if broke or (cidx[img[0]], cidx[img[1]]) not in sset:
                escapes += 1
    LD.gate("G-CHART-128-ENLARGEMENT",
            "the smallest carrier on which the extension DOES act is "
            "computed as an orbit closure of the parent's carrier rather "
            "than declared: every image of a uniform configuration is "
            "constant on each direction class, so the closure is a set of "
            "two-coin configurations -- and its closure is MEASURED state by "
            "state against the four declared generators of the extension, "
            "every image required to be constant on each direction class and "
            "to lie in the set, rather than asserted from the loop that "
            "built it",
            len(states) > len(coins) and escapes == 0,
            "the extension's closure of the %d-state carrier is %d states; "
            "%d escapes over %d generators"
            % (len(coins), len(states), escapes, len(EXT_GENERATORS)))
    S["_chart128_states"] = states
    out["CHART-128"]["enlarged_carrier"] = len(states)
    S["chart_action"] = out
    SEAL.take("THE CHART ACTION", "chart_action", "G-CHART-ACTION-MEASURED",
              out)
    return out


def measure_gauge_group(S, pv):
    """the residual gauge group on the carrier, and its orbits -- which are
    paper-23's orbits, reproduced here from the definitions."""
    lat, coins = S["_lat"], S["_coins"]
    cidx = S["_cidx"]
    n = len(coins)
    tw = []
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
            tw.append(c)
    gens = [tuple(cidx[gauge_twist(m, k)] for m in coins) for k in tw]
    G4 = gen_perm_group(n, gens)
    O4 = orbits_from_perms(n, G4)
    G8 = gen_perm_group(n, gens + [tuple(cidx[swap_conjugate(m)]
                                         for m in coins)])
    O8 = orbits_from_perms(n, G8)
    if mut("MUT-GAUGE-ORBITS"):
        O4 = O4[:-1]
    ok = (len(O4) == pv["PV-ORB32"] and len(O8) == pv["PV-ORB128"]
          and sum(len(o) for o in O4) == n and sum(len(o) for o in O8) == n)
    LD.gate("G-GAUGE-GROUP-REBUILT",
            "the residual gauge group on the carrier is measured by "
            "PROPAGATION -- which constant link twists a site-diagonal gauge "
            "can realise on the torus -- and its orbits are enumerated; both "
            "counts land on paper-23's own orbit counts at a named receipt "
            "path, so the two units are weighing the same partition",
            ok, "realisable twists %s; residual group orders %d and %d; "
            "orbits %d and %d against the parent's %d and %d"
            % (tw, len(G4), len(G8), len(O4), len(O8), pv["PV-ORB32"],
               pv["PV-ORB128"]))
    S["_G4"], S["_G8"], S["_O4"], S["_O8"] = G4, G8, O4, O8
    S["_twists"] = tw
    S["gauge"] = {
        "realisable_constant_twists": tw,
        "residual_group_order_chart_32": len(G4),
        "residual_group_order_chart_128": len(G8),
        "orbits_chart_32": len(O4), "orbits_chart_128": len(O8),
        "orbit_size_profile_chart_32": sorted(
            {s: sum(1 for o in O4 if len(o) == s)
             for s in {len(o) for o in O4}}.items()),
        "orbit_size_profile_chart_128": sorted(
            {s: sum(1 for o in O8 if len(o) == s)
             for s in {len(o) for o in O8}}.items()),
    }
    SEAL.take("THE GAUGE GROUP", "gauge", "G-GAUGE-GROUP-REBUILT", S["gauge"])
    return G4, G8, O4, O8


def measure_composition(S, pv):
    """the family's multiplication table: what stays, what leaves, whether
    the family is closed under inverse (which is what makes the composition
    walk doubly stochastic), and the monomial subgroup."""
    coins = S["_coins"]
    cidx = S["_cidx"]
    n = len(coins)
    prod = [[None] * n for _ in range(n)]
    stay = 0
    for i, A in enumerate(coins):
        row = prod[i]
        for j, B in enumerate(coins):
            k = cidx.get(cmul(A, B))
            row[j] = k
            if k is not None:
                stay += 1
    inv_in = sum(1 for m in coins if cdag(m) in cidx)
    mono = [i for i, m in enumerate(coins) if is_monomial(m)]
    mono_set = set(mono)
    mono_fail = sum(1 for i in mono for j in mono
                    if prod[i][j] not in mono_set)
    mono_leave = sum(1 for i in mono for j in range(n)
                     if prod[i][j] is None)
    if mut("MUT-COMPOSITION"):
        stay = stay - 1
    ok = (stay == pv["PV-PRODIN"] and n * n == pv["PV-PRODTOT"]
          and inv_in == n and len(mono) == pv["PV-MONO"]
          and mono_fail == 0 and mono_leave == 0)
    LD.gate("G-COMPOSITION-WALK-BUILT",
            "the family's multiplication table is built entry by entry in "
            "exact arithmetic and three separate facts are measured on it: "
            "how many products stay inside the family (the parent's number, "
            "at a named path), that the family IS closed under inverse -- "
            "which is the identity that makes the composition walk doubly "
            "stochastic and is measured rather than assumed -- and that the "
            "monomial coins are closed under multiplication and never carry "
            "a product out of the family",
            ok, "products inside %d of %d; inverse-closed %d of %d; "
            "monomial coins %d, closure failures %d, exits %d"
            % (stay, n * n, inv_in, n, len(mono), mono_fail, mono_leave))
    S["_prod"], S["_mono"] = prod, mono
    S["composition"] = {"products_inside": stay, "products_total": n * n,
                        "inverse_closed": inv_in, "monomial_coins": len(mono),
                        "monomial_closure_failures": mono_fail,
                        "monomial_exits_from_the_family": mono_leave}
    SEAL.take("THE COMPOSITION TABLE", "composition",
              "G-COMPOSITION-WALK-BUILT", S["composition"])
    return prod, mono


def measure_parent_sets(S, pv):
    """the parent's headline sets, REPRODUCED from the definitions: the sets
    whose masses this unit re-weighs under every derived measure."""
    lat, coins = S["_lat"], S["_coins"]
    n = len(lat.sites)
    base = lat.plaqs[0]
    edge = lat.addv(base, E1)
    I = sident(n)
    nonflat, noncomm, defect = set(), set(), set()
    for i, m in enumerate(coins):
        cfg = uniform_cfg(lat, m)
        W1 = holonomy(lat, base, cfg, n)
        W2 = holonomy(lat, edge, cfg, n)
        if W1 != I:
            nonflat.add(i)
        if smul(W1, W2) != smul(W2, W1):
            noncomm.add(i)
        U = link_op(lat, lat.links[0], m, n)
        if born(smul(U, U)) != bmul(born(U), born(U)):
            defect.add(i)
    if mut("MUT-PARENT-SETS"):
        nonflat = set(sorted(nonflat)[:-1])
    ok = (len(nonflat) == pv["PV-NONFLAT"] == pv["PV-P23NF"]
          and len(noncomm) == pv["PV-NONCOMM"] == pv["PV-P23NC"]
          and len(defect) == pv["PV-DEFECT"])
    LD.gate("G-PARENT-SETS-REBUILT",
            "the three sets this unit re-weighs are REPRODUCED from their "
            "definitions -- the non-flat configurations, the non-commuting "
            "ones and the coins carrying a composition defect -- and each is "
            "measured against BOTH parents' receipts at named paths, because "
            "a unit that proposes to move a number must first be able to "
            "build the set that number weighs",
            ok, "non-flat %d, non-commuting %d, defect-carrying %d"
            % (len(nonflat), len(noncomm), len(defect)))
    S["_sets"] = {
        "NON-FLAT": nonflat, "NON-COMMUTING": noncomm,
        "DEFECT-CARRYING": defect,
        "DIAGONAL": {i for i, s in enumerate(S["_sector"])
                     if s == "DIAGONAL"},
    }
    S["parent_sets"] = {k: len(v) for k, v in sorted(S["_sets"].items())}
    SEAL.take("THE PARENT SETS", "parent_sets", "G-PARENT-SETS-REBUILT",
              S["parent_sets"])
    return S["_sets"]


def measure_law_native_rates(S, pv):
    """the rate source the pin names for candidate (c): the Gamma-iteration's
    step-normalised positional law, whose normaliser that unit proved
    LAW-NATIVE -- true under an arbitrary re-pricing, hence not a fact about
    its carrier."""
    vals = [Fraction(pv["PV-LAW1"]), Fraction(pv["PV-LAW2"]),
            Fraction(pv["PV-LAW3"])]
    leg2 = Fraction(pv["PV-LAW-LEG2"])
    if mut("MUT-LAW-RATES"):
        vals = [Fraction(1, 3)] * 3
    ok = (sum(vals) == 1 and all(v > 0 for v in vals)
          and vals[0] == leg2 and len(set(vals)) == 3)
    LD.gate("G-LAW-NATIVE-RATE-SOURCE",
            "the rates of candidate (c) are NOT invented here: they are the "
            "Gamma-iteration terminal's own step-normalised positional law, "
            "read at named receipt paths at both legs, measured to be a "
            "probability vector, measured to agree leg to leg, and measured "
            "to be non-degenerate -- three distinct positive values.  That "
            "unit proved the normaliser law-native, so what enters here is a "
            "law value and not a carrier statistic",
            ok, "law values %s summing to %s; leg 2 first value %s; "
            "distinct values %d"
            % ([str(v) for v in vals], sum(vals), leg2, len(set(vals))))
    S["_law"] = vals
    S["law_native_rates"] = {"values": [str(v) for v in vals],
                             "sum": str(sum(vals)),
                             "source": "the Gamma-iteration terminal's "
                                       "step-normalised readout k1 = q/M",
                             "measure_label": "A-LAW-VALUE-NOT-A-FREQUENCY"}
    SEAL.take("THE LAW-NATIVE RATES", "law_native_rates",
              "G-LAW-NATIVE-RATE-SOURCE", S["law_native_rates"])
    return vals


# ===========================================================================
# SECTION 7.  THE DECLARED-DYNAMICS CENSUS
#
# Six families.  Every member is DECLARED in code -- its carrier, its
# transition law and its fibre -- and every member is RUN.  None is
# privileged: the census reports what each one derives, and the pin's fourth
# stage then asks whether they agree.
# ===========================================================================

# the elimination cap is the parent's own orbit count, so every exact solve
# this unit performs is at or below the size of the parent's simplex.
ELIMINATION_CAP = 208

MEASURE_NAMES = ["COUNTING", "ORBIT-UNIFORM-CHART-32",
                 "ORBIT-UNIFORM-CHART-128",
                 "HAAR-ON-THE-128-MONOMIAL-SUBGROUP"]


def named_nulls(S):
    """the measures the corpus has already named, rebuilt here so that a
    'NEW' verdict is a measured non-identity and not an absence of memory."""
    n = len(S["_coins"])
    out = {}
    out["COUNTING"] = [Fraction(1, n)] * n
    for nm, O in (("ORBIT-UNIFORM-CHART-32", S["_O4"]),
                  ("ORBIT-UNIFORM-CHART-128", S["_O8"])):
        v = [Fraction(0)] * n
        for o in O:
            for i in o:
                v[i] = Fraction(1, len(O) * len(o))
        out[nm] = v
    v = [Fraction(0)] * n
    for i in S["_mono"]:
        v[i] = Fraction(1, len(S["_mono"]))
    out["HAAR-ON-THE-128-MONOMIAL-SUBGROUP"] = v
    return out


def name_the_measure(S, pi, nulls):
    for nm in MEASURE_NAMES:
        if nulls[nm] == pi:
            return nm
    return "NEW"


def solve_instance(S, rec, P, n, blocks, bid, gperms, nulls):
    """THE EXACT SOLVE, per instance.  Communicating classes from the support
    of P; closed classes decided per class; then the stationary simplex, by
    exact elimination at or below the declared cap on every route, and the
    full-size identity pi P = pi verified for every vector published."""
    adj = support_adj(P, n)
    comps = sccs(n, adj)
    closed, cid = closed_classes(n, adj, comps)
    rec["communicating_classes"] = len(comps)
    rec["closed_classes"] = len(closed)
    rec["transient_classes"] = len(comps) - len(closed)
    rec["irreducible"] = (len(comps) == 1)
    if mut("MUT-IRREDUCIBILITY") and rec["instance"] == "COMPOSITION-LEFT":
        rec["irreducible"] = not rec["irreducible"]
    rec["unique_stationary"] = (len(closed) == 1)
    rec["simplex_dimension"] = len(closed) - 1
    rec["class_size_profile"] = sorted(
        {s: sum(1 for k in closed if len(comps[k]) == s)
         for s in {len(comps[k]) for k in closed}}.items())
    rec["aperiodic_by_self_loop"] = bool(
        closed and all(has_self_loop(P, comps[k]) for k in closed))

    routes = []
    vectors = []
    bad_kernels = 0
    if all(len(comps[k]) <= ELIMINATION_CAP for k in closed) and blocks is None:
        routes.append("ROUTE-CLASS")
        rec["largest_class_solved"] = max(len(comps[k]) for k in closed)
        for k in closed:
            cls = comps[k]
            m = len(cls)
            loc = {x: t for t, x in enumerate(cls)}
            Pl = [{loc[j]: v for j, v in P[x].items()} for x in cls]
            bas, rk = stationary_by_elimination(Pl, m)
            if len(bas) != 1:
                bad_kernels += 1
                continue
            v = [Fraction(0)] * n
            for t, x in enumerate(cls):
                v[x] = bas[0][t]
            vectors.append(v)
    else:
        routes.append("ROUTE-LUMP")
        Q, fails = lump(P, n, blocks, bid)
        rec["lumpability_failures"] = fails
        rec["quotient_size"] = len(blocks)
        if mut("MUT-CAP"):
            rec["quotient_size"] = ELIMINATION_CAP + 1
        if fails == 0:
            bas, rk = stationary_by_elimination(Q, len(blocks))
            rec["quotient_rank"] = rk
            if len(bas) != 1:
                bad_kernels += 1
            else:
                v = [Fraction(0)] * n
                for b, blk in enumerate(blocks):
                    for x in blk:
                        v[x] = bas[0][b] / len(blk)
                vectors.append(v)
    rec["routes"] = routes
    rec["largest_exact_solve"] = max(rec.get("quotient_size", 0),
                                     rec.get("largest_class_solved", 0))
    rec["closed_classes_with_a_non_unique_kernel"] = bad_kernels

    ver = [verify_stationary(P, v, n) for v in vectors]
    rec["published_vectors"] = len(vectors)
    rec["vectors_verified_at_full_size"] = sum(1 for x in ver if x)
    rec["verified_at_full_size"] = (bool(vectors) and all(ver)
                                    and bad_kernels == 0
                                    and len(vectors) == len(closed))
    rec["extreme_points"] = len(vectors)
    if rec["unique_stationary"]:
        pi = vectors[0]
        rec["measure_name"] = name_the_measure(S, pi, nulls)
        rec["measure_is_invariant_chart_32"] = all(
            len({pi[i] for i in o}) == 1 for o in S["_O4"])
        rec["measure_is_invariant_chart_128"] = all(
            len({pi[i] for i in o}) == 1 for o in S["_O8"])
        rec["distinct_values"] = len(set(pi))
        rec["value_profile"] = sorted(
            {str(x): sum(1 for y in pi if y == x) for x in set(pi)}.items())
        S["_pi"][rec["instance"]] = pi
        rec["verdict"] = "DERIVES"
    else:
        rec["measure_name"] = "A-SIMPLEX-NOT-A-POINT"
        names = [name_the_measure(S, v, nulls) for v in vectors]
        rec["extreme_point_names"] = sorted(
            {x: names.count(x) for x in set(names)}.items())
        rec["verdict"] = "REDUCIBLE"
        S["_simplex"][rec["instance"]] = vectors
    return rec


def build_dynamics_census(S, pv):
    """the six families, declared and run."""
    coins = S["_coins"]
    lat = S["_lat"]
    cidx = S["_cidx"]
    n = len(coins)
    G4, G8, O4, O8 = S["_G4"], S["_G8"], S["_O4"], S["_O8"]
    prod, mono = S["_prod"], S["_mono"]
    law = S["_law"]
    nulls = named_nulls(S)
    S["_nulls"] = nulls
    S["_pi"], S["_simplex"] = {}, {}
    bid4 = [None] * n
    for k, o in enumerate(O4):
        for i in o:
            bid4[i] = k

    rows = []

    # ---------------------------------------------------------------- (a)
    # the induced permutations are MEASURED from the chart action; that they
    # are all the identity is this family's first finding and not a typed
    # transition law
    perms32 = []
    for e in chart_elements(lat, False):
        p = [None] * n
        for i, m in enumerate(coins):
            img = {}
            for l in lat.links:
                im, rev = transported_link(lat, l, e)
                img[im[1]] = swap_conjugate(m) if rev else m
            p[i] = cidx[img[0]]
        perms32.append(tuple(p))
    Pa = group_walk(n, perms32)
    rows.append(dict(
        family="(a) THE CHART-GROUP WALK", instance="CHART-32",
        carrier="THE-UNIFORM-SLICE", carrier_size=n,
        declaration="one step applies a uniformly drawn element of the "
                    "anchored chart group",
        fibre_axis="WHICH-CHART-GROUP", fibre=2,
        covariance_group="THE-CHART-32-GROUP-AND-THE-RESIDUAL-GAUGE-GROUP",
        _P=Pa, _n=n, _blocks=None, _bid=None, _perms=G4, _gens=G4,
        induced_identity=sum(1 for p in perms32
                              if p == tuple(range(n)))))

    st = S["_chart128_states"]
    sidx = {s: k for k, s in enumerate(st)}
    els = chart_elements(lat, True)
    perms128 = []
    for e in els:
        p = [None] * len(st)
        for s in st:
            img = {}
            for l in lat.links:
                im, rev = transported_link(lat, l, e)
                srcm = coins[s[0]] if l[1] == 0 else coins[s[1]]
                img[im[1]] = swap_conjugate(srcm) if rev else srcm
            p[sidx[s]] = sidx[(cidx[img[0]], cidx[img[1]])]
        perms128.append(tuple(p))
    Pb = group_walk(len(st), perms128)
    gens128 = [perms128[els.index(e)] for e in EXT_GENERATORS]
    rows.append(dict(
        family="(a) THE CHART-GROUP WALK", instance="CHART-128",
        carrier="THE-EXTENSIONS-CLOSURE-OF-THE-UNIFORM-SLICE",
        carrier_size=len(st),
        declaration="one step applies a uniformly drawn element of the "
                    "declared extension -- on the enlarged carrier, because "
                    "the extension does not act on the parent's",
        fibre_axis="WHICH-CHART-GROUP", fibre=2,
        covariance_group="THE-CHART-128-GROUP",
        _P=Pb, _n=len(st), _blocks=None, _bid=None, _perms=perms128,
        _gens=gens128))

    # ---------------------------------------------------------------- (b)
    for nm, G in (("GAUGE-CHART-32", G4), ("GAUGE-CHART-128", G8)):
        rows.append(dict(
            family="(b) THE GAUGE-ACTION WALK", instance=nm,
            carrier="THE-UNIFORM-SLICE", carrier_size=n,
            declaration="one step applies a uniformly drawn element of the "
                        "residual gauge group on the carrier at this "
                        "chart reading",
            fibre_axis="WHICH-RESIDUAL-READING", fibre=2,
            covariance_group=nm,
            _P=group_walk(n, G), _n=n, _blocks=None, _bid=None, _perms=G))

    # ---------------------------------------------------------------- (c)
    SECT_ORDER = ["DIAGONAL", "ANTIDIAGONAL", "BALANCED"]
    sect_members = {s: [i for i in range(n) if S["_sector"][i] == s]
                    for s in SECT_ORDER}
    perms_of_three = [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1),
                      (2, 1, 0)]
    for a in perms_of_three:
        tgt = [Fraction(0)] * n
        for k, s in enumerate(SECT_ORDER):
            mem = sect_members[s]
            for q, i in enumerate(mem):
                tgt[i] = law[a[k]] / len(mem)
            if mut("MUT-K1-B"):
                wsum = sum(1 + (t % 3) for t in range(len(mem)))
                for q, i in enumerate(mem):
                    tgt[i] = law[a[k]] * Fraction(1 + (q % 3), wsum)
        P = [dict(enumerate(tgt)) for _ in range(n)]
        P = [{j: v for j, v in row.items() if v} for row in P]
        rows.append(dict(
            family="(c) THE LAW-NATIVE RESAMPLING",
            instance="LAW-NATIVE-%d%d%d" % a,
            carrier="THE-UNIFORM-SLICE", carrier_size=n,
            declaration="one step discards the current coin and draws a new "
                        "one: a sector by the Gamma-iteration's law-native "
                        "positional law, then uniformly inside it",
            fibre_axis="WHICH-SECTOR-CARRIES-WHICH-POSITION", fibre=6,
            covariance_group="THE-RESIDUAL-GAUGE-GROUP-CHART-32",
            _P=P, _n=n, _blocks=O4, _bid=bid4, _perms=G4))

    # ---------------------------------------------------------------- (d)
    for side in ("LEFT", "RIGHT"):
        P = []
        for i in range(n):
            row = {}
            rej = 0
            for j in range(n):
                k = prod[i][j] if side == "LEFT" else prod[j][i]
                if k is None:
                    rej += 1
                else:
                    row[k] = row.get(k, 0) + 1
            if rej:
                row[i] = row.get(i, 0) + rej
            P.append({k: Fraction(v, n) for k, v in row.items()})
        rows.append(dict(
            family="(d) THE COMPOSITION WALK", instance="COMPOSITION-" + side,
            carrier="THE-UNIFORM-SLICE", carrier_size=n,
            declaration="one step composes the current coin with a uniformly "
                        "drawn member of the family on the %s and stays put "
                        "when the product leaves the family" % side.lower(),
            fibre_axis="WHICH-SIDE-COMPOSES", fibre=2,
            covariance_group="THE-RESIDUAL-GAUGE-GROUP-CHART-32",
            _P=P, _n=n, _blocks=O4, _bid=bid4, _perms=G4))

    # ---------------------------------------------------------------- (e)
    for side in ("LEFT", "RIGHT"):
        P = []
        w = Fraction(1, len(mono))
        for j in range(n):
            row = {}
            for i in mono:
                k = prod[i][j] if side == "LEFT" else prod[j][i]
                if k is None:
                    raise GateFail("monomial walk left the family")
                row[k] = row.get(k, Fraction(0)) + w
            P.append(row)
        rows.append(dict(
            family="(e) THE MONOMIAL-HAAR WALK", instance="MONOMIAL-" + side,
            carrier="THE-UNIFORM-SLICE", carrier_size=n,
            declaration="one step multiplies the current coin on the %s by a "
                        "uniformly drawn member of the arena's one group -- "
                        "the 128 monomial coins, whose Haar measure is the "
                        "one measure paper-23 found the arena hands over"
                        % side.lower(),
            fibre_axis="WHICH-SIDE-MULTIPLIES", fibre=2,
            covariance_group="THE-RESIDUAL-GAUGE-GROUP-CHART-32",
            _P=P, _n=n, _blocks=None, _bid=None, _perms=G4))

    # ---------------------------------------------------------------- (f)
    for nm in ("COUNTING", "ORBIT-UNIFORM-CHART-32",
               "ORBIT-UNIFORM-CHART-128"):
        rows.append(dict(
            family="(f) THE COVARIANT METROPOLIS FAMILY",
            instance="METROPOLIS-AT-" + nm,
            carrier="THE-UNIFORM-SLICE", carrier_size=n,
            declaration="one step proposes a uniformly drawn configuration "
                        "and accepts it with probability min(1, pi(y)/pi(x)) "
                        "at the declared invariant target " + nm,
            fibre_axis="WHICH-INVARIANT-TARGET",
            fibre="THE-INVARIANT-SIMPLEX-ITSELF",
            covariance_group="THE-RESIDUAL-GAUGE-GROUP-CHART-32",
            _P=metropolis(nulls[nm], n), _n=n, _blocks=O4, _bid=bid4,
            _perms=G4))

    # the declared NON-covariant control: the same construction at a target
    # that is measured NOT to be constant on the parent's orbits
    nb = 4
    bs = n // nb
    ctrl_blocks = [list(range(b * bs, (b + 1) * bs)) for b in range(nb)]
    ctrl_bid = [None] * n
    for b, blk in enumerate(ctrl_blocks):
        for i in blk:
            ctrl_bid[i] = b
    wts = [Fraction(1, 10), Fraction(2, 10), Fraction(3, 10),
           Fraction(4, 10)]
    ctrl_t = [Fraction(0)] * n
    for b, blk in enumerate(ctrl_blocks):
        for i in blk:
            ctrl_t[i] = wts[b] / len(blk)
    shift = tuple(ctrl_blocks[ctrl_bid[i]][
        (i - ctrl_blocks[ctrl_bid[i]][0] + 1) % bs] for i in range(n))
    rows.append(dict(
        family="(f) THE COVARIANT METROPOLIS FAMILY",
        instance="METROPOLIS-AT-A-NON-INVARIANT-TARGET",
        carrier="THE-UNIFORM-SLICE", carrier_size=n,
        declaration="the same construction at a declared target measured NOT "
                    "to be constant on the parent's orbits -- the control "
                    "that shows what covariance is doing and what it is not",
        fibre_axis="WHICH-TARGET-THE-CONTROL",
        fibre="THE-WHOLE-SIMPLEX",
        covariance_group="THE-DECLARED-BLOCK-CYCLE-NOT-THE-GAUGE-GROUP",
        _P=metropolis(ctrl_t, n), _n=n, _blocks=ctrl_blocks, _bid=ctrl_bid,
        _perms=[tuple(range(n)), shift], _control=True))
    S["_ctrl_target"] = ctrl_t
    S["_ctrl_blocks"] = ctrl_blocks
    return rows


def run_the_census(S, rows, pv):
    """every declared member is RUN.  Each instance is gated on its own
    objects: its transition law is row-stochastic, its declared covariance
    group is verified on its own rows, its classes are computed from its own
    support, and its stationary vectors are verified against its own P."""
    nulls = S["_nulls"]
    published = []
    for rec in rows:
        P, n = rec.pop("_P"), rec.pop("_n")
        blocks, bidv = rec.pop("_blocks"), rec.pop("_bid")
        perms = rec.pop("_perms")
        gens = rec.pop("_gens", None) or perms
        rec.pop("_control", None)
        if mut("MUT-STOCHASTIC") and rec["instance"] == "GAUGE-CHART-32":
            P = [dict(r) for r in P]
            k = sorted(P[0])[0]
            P[0][k] = P[0][k] / 2
        rec["row_stochastic"] = row_stochastic(P, n)
        cf = covariance_failures(P, n, gens)
        if mut("MUT-COVARIANCE") and rec["instance"] == "LAW-NATIVE-012":
            cf = 0 if cf else 1
        rec["covariance_generators"] = len(gens)
        rec["covariance_failures"] = cf
        rec["covariant"] = (cf == 0)
        # covariance under THE RESIDUAL GAUGE GROUP is a separate and
        # sharper question: it is the class paper-23's law speaks about, and
        # a chain can be covariant under a group of its own choosing while
        # breaking the arena's
        if n == len(S["_coins"]):
            gf = covariance_failures(P, n, S["_G4"])
            rec["gauge_covariance_failures"] = gf
            rec["gauge_covariant"] = (gf == 0)
            # K2's second column: covariance under the ORDER-8 residual
            # group -- the extension reading -- MEASURED at every instance on
            # this carrier rather than inherited from the parent's receipt
            P8 = P
            if mut("MUT-G8-COVARIANCE") and rec["instance"].endswith("-128"):
                P8 = [dict(r) for r in P]
                P8[0] = {0: Fraction(1)}
            gf8 = covariance_failures(P8, n, S["_G8"])
            rec["gauge_covariance_failures_chart_128"] = gf8
            rec["gauge_covariant_chart_128"] = (gf8 == 0)
        else:
            rec["gauge_covariance_failures"] = None
            rec["gauge_covariant"] = None
            rec["gauge_covariance_failures_chart_128"] = None
            rec["gauge_covariant_chart_128"] = None
        trans = True
        if blocks is not None:
            G = gen_perm_group(n, gens)
            trans = all(sorted({g[blk[0]] for g in G}) == sorted(blk)
                        for blk in blocks)
            rec["lumping_blocks"] = len(blocks)
            rec["lumping_group_order"] = len(G)
            rec["lumping_group_transitive_on_every_block"] = trans
        solve_instance(S, rec, P, n, blocks, bidv, perms, nulls)
        S["_P"][rec["instance"]] = (P, n)
        LD.gate("G-INSTANCE-" + rec["instance"],
                "this declared instance is gated on its OWN objects and never "
                "on an aggregate (#87): its transition law is row-stochastic "
                "row by row; its declared covariance group is verified "
                "generator by generator and row by row; where the exact solve "
                "goes through a quotient, that quotient's lumpability is "
                "measured block by block and its blocks are the orbits of a "
                "group measured transitive on each of them; every closed "
                "class it publishes has a one-dimensional stationary kernel "
                "computed by exact elimination; and every vector it publishes "
                "satisfies pi P = pi at FULL size",
                (rec["row_stochastic"] and rec["covariant"]
                 and trans and rec["verified_at_full_size"]),
                "row-stochastic %s; covariance failures %d over %d "
                "generators; lumping transitive %s; %d closed classes, %d "
                "vectors, %d verified at full size"
                % (rec["row_stochastic"], rec["covariance_failures"],
                   rec["covariance_generators"], trans,
                   rec["closed_classes"], rec["published_vectors"],
                   rec["vectors_verified_at_full_size"]))
        # #119 AT VALUE-CLOSE: this record is digested at the gate that
        # vouches ITS values, not fifteen gates later when the enclosing
        # census object is finished
        SEAL.take("INSTANCE RECORD " + rec["instance"],
                  "census/instances/" + rec["instance"],
                  "G-INSTANCE-" + rec["instance"], rec)
        published.append(rec)
        say("    %-42s %-11s classes=%-4d closed=%-4d %s"
            % (rec["instance"], rec["verdict"], rec["communicating_classes"],
               rec["closed_classes"], rec["measure_name"]))

    if mut("MUT-CENSUS-SHORT"):
        published = published[:-1]
    fams = sorted({r["family"] for r in published})
    ok = (len(published) == len(rows)
          and all(r["row_stochastic"] for r in published)
          and all(r["verified_at_full_size"] for r in published)
          and all(r["covariant"] for r in published
                  if "NON-INVARIANT" not in r["instance"]))
    LD.gate("G-DECLARED-DYNAMICS-CENSUS",
            "the census is DECLARED and every member of it is RUN.  Each "
            "instance carries its own carrier, its own transition law "
            "written out in this instrument, its own fibre axis and its own "
            "declared covariance group -- and each is gated on its own "
            "objects: row-stochasticity per row, covariance per generator "
            "and per row, communicating classes from its own support, and "
            "the identity pi P = pi verified at full size for every vector "
            "it publishes.  None of the six families is privileged",
            ok, "%d families, %d instances, all run; %d row-stochastic, "
            "%d verified at full size"
            % (len(fams), len(published),
               sum(1 for r in published if r["row_stochastic"]),
               sum(1 for r in published if r["verified_at_full_size"])))

    der = [r for r in published if r["verdict"] == "DERIVES"]
    red = [r for r in published if r["verdict"] == "REDUCIBLE"]
    irr = [r for r in published if r["irreducible"]]
    LD.gate("G-IRREDUCIBILITY-IS-THE-CRITERION",
            "paper-23's law is applied as the criterion and not as a "
            "slogan: a chain fixes a measure exactly when its stationary "
            "simplex is a point, which happens exactly when it has one "
            "closed communicating class.  Irreducibility is the parent's "
            "stated form of that condition and it is measured separately, "
            "because it is SUFFICIENT and not necessary -- the sharp "
            "condition is the closed-class count, and a chain with one "
            "closed class and a transient class derives without being "
            "irreducible",
            len(der) == len(irr) and all(r["closed_classes"] == 1
                                         for r in der),
            "%d instances derive, %d are irreducible, %d reducible; "
            "transient classes across the census: %d"
            % (len(der), len(irr), len(red),
               sum(r["transient_classes"] for r in published)))

    # ---- the declared elimination cap, ENFORCED per record (not published
    # as a claim and left ungated)
    over = [r["instance"] for r in published
            if r["largest_exact_solve"] > ELIMINATION_CAP]
    LD.gate("G-ELIMINATION-CAP-IS-ENFORCED",
            "the declared elimination cap is a GATE and not a remark: every "
            "instance's own largest exact solve -- the size of the quotient "
            "it lumped to, or of the largest closed class it solved directly "
            "-- is compared against the cap record by record (#87), so the "
            "published claim that every exact solve in this unit is at or "
            "below the parent's own orbit count is measured rather than "
            "asserted",
            not over,
            "cap %d; largest exact solve over the census %d; %d instances "
            "above the cap %s"
            % (ELIMINATION_CAP,
               max(r["largest_exact_solve"] for r in published), len(over),
               over[:3]))

    # ---- K2's second covariance column: the EXTENSION reading, measured
    on_carrier = [r for r in published
                  if r["gauge_covariant_chart_128"] is not None]
    cov4 = sorted(r["instance"] for r in on_carrier
                  if r["verdict"] == "DERIVES" and r["gauge_covariant"])
    cov8 = sorted(r["instance"] for r in on_carrier
                  if r["verdict"] == "DERIVES"
                  and r["gauge_covariant_chart_128"])
    ou128 = [r for r in published
             if r["instance"] == "METROPOLIS-AT-ORBIT-UNIFORM-CHART-128"][0]
    LD.gate("G-EXTENSION-COVARIANCE-IS-MEASURED-NOT-INHERITED",
            "the extension half of the price sentence is MEASURED here and "
            "not inherited: covariance is tested against the ORDER-8 residual "
            "group at every instance living on the parent's carrier, row by "
            "row and generator by generator, and the extension's price may "
            "be quoted only because a covariant irreducible chain was built "
            "at that reading and measured covariant under that group -- the "
            "Metropolis chain at the orbit-uniform chart-128 target.  The "
            "covariant deriving population is reported at both readings, so "
            "a count that was reading-relative could not pass unlabelled",
            ou128["gauge_covariant_chart_128"] and cov4 == cov8,
            "%d instances on the parent's carrier; covariant deriving under "
            "the order-4 group %d, under the order-8 group %d, identical as "
            "sets: %s; the chart-128 target's chain is covariant under the "
            "order-8 group: %s (failures %s)"
            % (len(on_carrier), len(cov4), len(cov8), cov4 == cov8,
               ou128["gauge_covariant_chart_128"],
               ou128["gauge_covariance_failures_chart_128"]))
    S["extension_covariance"] = {
        "instances_tested_on_the_parents_carrier": len(on_carrier),
        "covariant_deriving_under_the_order_4_group": len(cov4),
        "covariant_deriving_under_the_order_8_group": len(cov8),
        "the_two_populations_are_identical_as_sets": cov4 == cov8,
        "chart_128_target_chain_is_covariant_under_the_order_8_group":
            ou128["gauge_covariant_chart_128"],
        "the_control_fails_both": [
            r["gauge_covariance_failures"] for r in published
            if "NON-INVARIANT" in r["instance"]] + [
            r["gauge_covariance_failures_chart_128"] for r in published
            if "NON-INVARIANT" in r["instance"]],
    }
    SEAL.take("THE EXTENSION COVARIANCE", "extension_covariance",
              "G-EXTENSION-COVARIANCE-IS-MEASURED-NOT-INHERITED",
              S["extension_covariance"])

    # ---- K2's privilege ruling, measured on the object: the law-native
    # chain's kernel is RANK ONE
    lawi = [r for r in published if r["family"].startswith("(c)")]
    same_rows, draw_law = 0, 0
    for r in lawi:
        Pl, m = S["_P"][r["instance"]]
        rows_of_P = Pl
        if mut("MUT-RANK-ONE") and r["instance"] == "LAW-NATIVE-012":
            rows_of_P = [dict(x) for x in Pl]
            rows_of_P[0] = {0: Fraction(1)}
        if all(rows_of_P[i] == rows_of_P[0] for i in range(1, m)):
            same_rows += 1
        draw = [rows_of_P[0].get(j, Fraction(0)) for j in range(m)]
        if draw == S["_pi"][r["instance"]]:
            draw_law += 1
    LD.gate("G-THE-LAW-NATIVE-KERNEL-IS-RANK-ONE",
            "the privilege question is settled ON THE OBJECT and published "
            "rather than left to a reader: every row of the law-native "
            "chain's transition law is the SAME vector, so its kernel is "
            "rank one and its unique stationary measure is the declared draw "
            "law read back -- the dynamics does no work.  What the family "
            "contributes is a transported LAW VALUE, not a measure derived "
            "by a dynamics, and the row is stamped accordingly",
            same_rows == len(lawi) and draw_law == len(lawi) and lawi,
            "%d law-native instances; %d with every row identical; %d whose "
            "stationary measure is exactly the declared draw law"
            % (len(lawi), same_rows, draw_law))
    S["privilege"] = {
        "family": "(c) THE LAW-NATIVE RESAMPLING",
        "instances": len(lawi),
        "every_row_of_the_transition_law_is_the_same_vector":
            same_rows == len(lawi),
        "instances_whose_stationary_measure_is_the_declared_draw_law":
            draw_law,
        "what_the_dynamics_contributes":
            "NOTHING-THE-DERIVED-MEASURE-IS-THE-DECLARED-DRAW-LAW-READ-BACK",
        "what_the_law_contributes":
            "THREE-RATES-CONFIRMED-LAW-NATIVE-BY-THE-GAMMA-ITERATION-TERMINAL",
        "the_unpinned_step":
            "THE-IDENTIFICATION-OF-THE-TRANSPORT-LAWS-THREE-POSITIONS-WITH-"
            "THIS-ARENAS-THREE-COIN-SECTORS",
        "stamp": "LAW-RATED-CONSTRUCTION-DECLARED-AT-AN-UNPINNED-"
                 "IDENTIFICATION",
        "pricing_not_evidence": "A-CHAIN-BUILT-FROM-THE-MEASURE-IT-SELECTS-"
                                "IS-PRICING-AND-NOT-EVIDENCE-AND-THIS-FAMILY-"
                                "IS-COUNTED-BESIDE-THE-METROPOLIS-FAMILY",
    }
    SEAL.take("THE PRIVILEGE RULING", "privilege",
              "G-THE-LAW-NATIVE-KERNEL-IS-RANK-ONE", S["privilege"])
    return published


def exhibit_the_gap_in_the_inherited_law(S):
    """the inherited law says DERIVES IFF IRREDUCIBLE.  The sharp condition
    is one closed class.  They differ, and the difference is EXHIBITED on a
    declared synthetic chain rather than argued: a chain with a transient
    state derives and is not irreducible."""
    P = [{1: Fraction(1, 2), 2: Fraction(1, 2)},
         {1: Fraction(1, 2), 2: Fraction(1, 2)},
         {1: Fraction(1, 2), 2: Fraction(1, 2)}]
    adj = support_adj(P, 3)
    comps = sccs(3, adj)
    closed, cid = closed_classes(3, adj, comps)
    bas, rk = stationary_by_elimination(P, 3)
    if mut("MUT-GAP-WITNESS"):
        comps = comps[:1]
    ok = (len(comps) > 1 and len(closed) == 1 and len(bas) == 1)
    LD.gate("G-THE-INHERITED-LAW-IS-SUFFICIENT-NOT-NECESSARY",
            "the gap between the inherited law and the sharp one is "
            "EXHIBITED rather than asserted: a declared three-state chain "
            "with one transient state has more than one communicating class "
            "-- so it is not irreducible -- yet exactly one closed class and "
            "a stationary simplex of dimension zero, computed by the same "
            "exact elimination every instance uses.  It derives.  The "
            "parent's form is therefore sufficient and not necessary, and "
            "this unit says so rather than inheriting the stronger reading",
            ok, "communicating classes %d, closed classes %d, kernel "
            "dimension %d" % (len(comps), len(closed), len(bas)))
    S["law_refinement"] = {
        "inherited": "A-COVARIANT-CHAIN-DERIVES-IFF-IT-IS-IRREDUCIBLE",
        "sharp": "A-COVARIANT-CHAIN-DERIVES-IFF-IT-HAS-EXACTLY-ONE-CLOSED-"
                 "COMMUNICATING-CLASS",
        "witness_states": 3, "witness_communicating_classes": len(comps),
        "witness_closed_classes": len(closed),
        "witness_simplex_dimension": len(bas) - 1,
        "relation": "IRREDUCIBLE-IMPLIES-ONE-CLOSED-CLASS-AND-NOT-CONVERSELY",
    }
    SEAL.take("THE LAW REFINEMENT", "law_refinement",
              "G-THE-INHERITED-LAW-IS-SUFFICIENT-NOT-NECESSARY",
              S["law_refinement"])


def verify_the_dimension_theorem(S):
    """the theorem the reducible instances rest on -- the stationary simplex
    has dimension (closed classes - 1) -- verified EXHAUSTIVELY on a declared
    family of small chains, by the same exact elimination."""
    tot = bad = 0
    layers = []
    for m in (3, 4):
        rowset = [tuple((k >> j) & 1 for j in range(m))
                  for k in range(1, 2 ** m)]
        R = len(rowset)
        for code in range(R ** m):
            combo, c = [], code
            for _ in range(m):
                combo.append(rowset[c % R])
                c //= R
            P, adj = [], []
            for r in combo:
                s = sum(r)
                P.append({j: Fraction(r[j], s) for j in range(m) if r[j]})
                adj.append([j for j in range(m) if r[j]])
            if mut("MUT-DIMENSION-THEOREM") and tot == 0:
                P = [{i: Fraction(1)} for i in range(m)]
            comps = sccs(m, adj)
            closed, _cid = closed_classes(m, adj, comps)
            bas, _rk = stationary_by_elimination(P, m)
            tot += 1
            if len(bas) != len(closed):
                bad += 1
        layers.append({"carrier_states": m, "row_alphabet": R,
                       "chains": R ** m})
    LD.gate("G-SIMPLEX-DIMENSION-THEOREM",
            "the identity the reducible verdicts are read through -- the "
            "stationary simplex's dimension is one less than the number of "
            "closed communicating classes -- is VERIFIED EXHAUSTIVELY on a "
            "declared family of small chains, every one of them solved by "
            "the same exact elimination this unit uses at scale, so the "
            "bridge from a class count to a simplex dimension is measured "
            "and not quoted",
            bad == 0, "%d chains enumerated exhaustively over the %d-state "
            "and %d-state layers, %d mismatches between the kernel dimension "
            "and the closed-class count"
            % (tot, layers[0]["carrier_states"], layers[1]["carrier_states"],
               bad))
    S["dimension_theorem"] = {"chains_enumerated": tot, "mismatches": bad,
                              "carrier_states": [ly["carrier_states"]
                                                 for ly in layers],
                              "layers": layers}
    SEAL.take("THE DIMENSION THEOREM", "dimension_theorem",
              "G-SIMPLEX-DIMENSION-THEOREM", S["dimension_theorem"])


def measure_the_welds(S, published, pv):
    """three identities between this unit's decompositions and the parent's
    published objects, each gated on the objects and not on a count."""
    by = {r["instance"]: r for r in published}
    g32, g128 = by["GAUGE-CHART-32"], by["GAUGE-CHART-128"]
    O4, O8 = S["_O4"], S["_O8"]
    cls32 = sorted(sorted(c) for c in _closed_class_sets(S, "GAUGE-CHART-32"))
    cls128 = sorted(sorted(c) for c in
                    _closed_class_sets(S, "GAUGE-CHART-128"))
    if mut("MUT-WELD"):
        cls32 = [c[:-1] if i == 0 else c for i, c in enumerate(cls32)]
    same32 = cls32 == sorted(sorted(o) for o in O4)
    same128 = cls128 == sorted(sorted(o) for o in O8)
    LD.gate("G-GAUGE-WALK-CLASSES-ARE-THE-PARENTS-ORBITS",
            "the gauge walk's closed communicating classes are compared with "
            "paper-23's orbits AS SETS, class by class and not by "
            "cardinality (#87): the two partitions are identical at both "
            "readings, so the dynamics layer's decomposition and the static "
            "layer's orbit census are the same object arrived at twice",
            same32 and same128,
            "chart-32: %d classes against %d parent orbits, identical %s; "
            "chart-128: %d against %d, identical %s"
            % (len(cls32), pv["PV-ORB32"], same32, len(cls128),
               pv["PV-ORB128"], same128))
    # the dimension is certified by an EXHIBITED BASIS -- the extreme points
    # this run solved, each verified at full size, their supports measured
    # pairwise disjoint and therefore linearly independent -- and not by a
    # class count two earlier gates have already forced equal to the
    # parent's orbit count
    dim_rows = []
    for inst, want in (("GAUGE-CHART-32", pv["PV-SIMP32"]),
                       ("GAUGE-CHART-128", pv["PV-SIMP128"])):
        r = by[inst]
        vecs = S["_simplex"][inst]
        sup = [{i for i, x in enumerate(v) if x} for v in vecs]
        if mut("MUT-SIMPLEX-DIM") and inst == "GAUGE-CHART-32":
            sup[1] = set(sup[0])
        union = set()
        for s in sup:
            union |= s
        indep = (sum(len(s) for s in sup) == len(union))
        dim_rows.append({
            "instance": inst,
            "extreme_points_exhibited": len(vecs),
            "supports_are_pairwise_disjoint_hence_independent": indep,
            "vectors_verified_at_full_size":
                r["vectors_verified_at_full_size"],
            "simplex_dimension_from_the_exhibited_basis": len(vecs) - 1,
            "the_parents_dimension": want,
            "ok": (indep and r["vectors_verified_at_full_size"] == len(vecs)
                   and len(vecs) - 1 == want
                   and r["simplex_dimension"] == want)})
    ok = all(d["ok"] for d in dim_rows)
    LD.gate("G-GAUGE-WALK-SIMPLEX-IS-THE-PARENTS-SIMPLEX",
            "and the gauge walk's stationary simplex IS paper-23's invariant "
            "simplex: an invariant measure is exactly an orbit-constant one, "
            "a group walk's stationary measures are exactly the invariant "
            "ones, and the dimension is certified by an EXHIBITED BASIS -- "
            "every extreme point solved by exact elimination, verified at "
            "full size against its own chain, and measured to have a support "
            "disjoint from every other, hence independent -- which lands on "
            "the parent's published dimensions at named receipt paths.  The "
            "dynamics did not shrink the parent's simplex by one number",
            ok, "chart-32: %d independent extreme points exhibited, "
            "dimension %d against the parent's %d; chart-128: %d, dimension "
            "%d against %d; supports disjoint %s"
            % (dim_rows[0]["extreme_points_exhibited"],
               dim_rows[0]["simplex_dimension_from_the_exhibited_basis"],
               pv["PV-SIMP32"], dim_rows[1]["extreme_points_exhibited"],
               dim_rows[1]["simplex_dimension_from_the_exhibited_basis"],
               pv["PV-SIMP128"],
               [d["supports_are_pairwise_disjoint_hence_independent"]
                for d in dim_rows]))

    mono = by["MONOMIAL-LEFT"]
    monoset = set(S["_mono"])
    if mut("MUT-MONOMIAL"):
        monoset = set(sorted(monoset)[:-1])
    cls = _closed_class_sets(S, "MONOMIAL-LEFT")
    carries = any(set(c) == monoset for c in cls)
    LD.gate("G-MONOMIAL-WALK-CARRIES-THE-PARENTS-HAAR",
            "the monomial walk's decomposition is compared with paper-23's "
            "one canonical measure AS A SET: one of its closed classes is "
            "exactly the 128 monomial coins, so the corpus's single "
            "handed-over measure appears here as one extreme point of one "
            "declared dynamics' stationary simplex -- and the other extreme "
            "points are the classes the parent's Haar does not reach",
            carries and mono["closed_classes"] > 1,
            "%d closed classes of sizes %s; one is exactly the %d monomial "
            "coins: %s" % (mono["closed_classes"], mono["class_size_profile"],
                           pv["PV-MONO"], carries))
    S["welds"] = {
        "gauge_classes_equal_the_parents_orbits_chart_32": same32,
        "gauge_classes_equal_the_parents_orbits_chart_128": same128,
        "gauge_simplex_dimension_chart_32": g32["simplex_dimension"],
        "gauge_simplex_dimension_chart_128": g128["simplex_dimension"],
        "simplex_dimension_certified_by_an_exhibited_basis": dim_rows,
        "monomial_walk_carries_the_parents_haar": carries,
        "monomial_closed_classes": mono["closed_classes"],
    }
    SEAL.take("THE WELDS", "welds",
              "G-GAUGE-WALK-CLASSES-ARE-THE-PARENTS-ORBITS", S["welds"])


def _closed_class_sets(S, inst):
    P, n = S["_P"][inst]
    adj = support_adj(P, n)
    comps = sccs(n, adj)
    closed, _cid = closed_classes(n, adj, comps)
    return [comps[k] for k in closed]


# ===========================================================================
# SECTION 8.  THE DYNAMICS-RELATIVITY CENSUS (E-24's teeth)
# ===========================================================================

def measure_relativity(S, published, pv):
    """does the stationary measure MOVE across the declared-dynamics fibre?
    Every mass below is labelled with the measure that produces it, and the
    column that is not a probability is stamped COUNTING-ONLY (E-24)."""
    sets = S["_sets"]
    O4, O8 = S["_O4"], S["_O8"]
    der = [r for r in published if r["verdict"] == "DERIVES"]
    n = len(S["_coins"])

    closure = {}
    for nm, mem in sorted(sets.items()):
        c32 = all(len({i in mem for i in o}) == 1 for o in O4)
        c128 = all(len({i in mem for i in o}) == 1 for o in O8)
        closure[nm] = {"orbit_closed_chart_32": c32,
                       "orbit_closed_chart_128": c128}
    if mut("MUT-ORBIT-CLOSURE"):
        closure["NON-FLAT"]["orbit_closed_chart_32"] = False
    LD.gate("G-SETS-ARE-UNIONS-OF-ORBITS",
            "every set re-weighed below is checked to be a UNION OF ORBITS "
            "at both readings, orbit by orbit and never by a cardinality "
            "(#87), so its mass is well defined under every invariant "
            "measure compared -- without which the comparison would be "
            "between measures answering different questions",
            all(v["orbit_closed_chart_32"] and v["orbit_closed_chart_128"]
                for v in closure.values()),
            "%d sets, all orbit-closed at both readings: %s"
            % (len(closure), sorted(closure)))

    cov = [r for r in der if r["gauge_covariant"]]
    rows = []
    for nm, mem in sorted(sets.items()):
        row = {"set": nm, "configurations_COUNTING_ONLY": len(mem)}
        masses = {}
        for r in der:
            pi = S["_pi"][r["instance"]]
            masses[r["instance"]] = sum(pi[i] for i in mem)
        row["mass_by_declared_dynamics"] = {
            k: str(v) for k, v in sorted(masses.items())}
        lo, hi = min(masses.values()), max(masses.values())
        row["spread_over_every_deriving_instance"] = str(hi - lo)
        row["_spread_all"] = hi - lo
        cm = [masses[r["instance"]] for r in cov]
        row["spread_over_the_covariant_instances"] = str(max(cm) - min(cm))
        row["_spread"] = max(cm) - min(cm)
        row["argmin"] = sorted(k for k, v in masses.items() if v == lo)
        row["argmax"] = sorted(k for k, v in masses.items() if v == hi)
        rows.append(row)

    widest = max(r["_spread"] for r in rows)
    widest_all = max(r["_spread_all"] for r in rows)
    argmax_sets = sorted(r["set"] for r in rows if r["_spread"] == widest)
    parent_widest = Fraction(pv["PV-P23-WIDEST"])
    if mut("MUT-SPREAD"):
        widest = Fraction(0)
    moves = widest > 0

    # ---- K2's MAJOR-1, measured: HELD AT THE PARENT'S OWN COMPARISON CLASS
    # this census reproduces the parent's number exactly.  max over a
    # superset >= max over a subset is arithmetic, so the rise is priced to
    # the six new measures entering the comparison and not to the dynamics.
    PARENT_THREE = ["COUNTING", "ORBIT-UNIFORM-CHART-32",
                    "ORBIT-UNIFORM-CHART-128"]
    rep = {}
    for r in der:
        if r["measure_name"] in PARENT_THREE and r["measure_name"] not in rep:
            rep[r["measure_name"]] = (r["instance"], S["_pi"][r["instance"]])
    if mut("MUT-RESTRICTED"):
        rep["COUNTING"] = ("PLANTED", S["_pi"]["LAW-NATIVE-012"])
    restricted = Fraction(0)
    restricted_on = []
    for r in rows:
        memb = sets[r["set"]]
        ms = [sum(v[i] for i in memb)
              for _nm, (_inst, v) in sorted(rep.items())]
        sp = max(ms) - min(ms) if ms else Fraction(0)
        r["spread_at_the_parents_own_three_measures"] = str(sp)
        if sp > restricted:
            restricted, restricted_on = sp, [r["set"]]
        elif sp == restricted and sp > 0:
            restricted_on.append(r["set"])
    rest_ok = (len(rep) == len(PARENT_THREE) and restricted == parent_widest)
    LD.gate("G-THE-RESTRICTED-COMPARISON-REPRODUCES-THE-PARENTS-NUMBER",
            "the parent's comparison class is a SUBSET of this one, so the "
            "two spreads are not like for like and the comparison is made at "
            "a fixed comparison class instead: all three of the parent's own "
            "named measures are present in this census, and restricted to "
            "exactly those three the widest spread over the parent's own "
            "headline sets is measured and must reproduce the parent's "
            "published number EXACTLY.  Held at fixed comparison class, "
            "declaring a dynamics moved the parent's sets by nothing; the "
            "rise is the new measures entering the same comparison",
            rest_ok,
            "%d of %d of the parent's measures present in this census; "
            "restricted widest spread %s against the parent's published %s, "
            "attained on %s"
            % (len(rep), len(PARENT_THREE), restricted, parent_widest,
               restricted_on))

    # ---- and the theorem-level answer to 'how far can a declaration move
    # these sets?': every headline set contains a whole orbit and its
    # complement contains a whole orbit, so the two orbit point masses are
    # invariant measures -- extreme points of the parent's simplex -- at
    # which the set's mass is 1 and 0.  The reachable range is [0, 1].
    ranges = []
    for nm, memb in sorted(sets.items()):
        inside = [o for o in O4 if all(i in memb for i in o)]
        outside = [o for o in O4 if all(i not in memb for i in o)]
        row = {"set": nm, "an_orbit_inside_the_set": len(inside),
               "an_orbit_in_the_complement": len(outside)}
        for tag, pick in (("inside", inside), ("outside", outside)):
            if not pick:
                row["mass_at_the_point_mass_" + tag] = "NO-WITNESS"
                continue
            w = [Fraction(0)] * n
            for i in pick[0]:
                w[i] = Fraction(1, len(pick[0]))
            if mut("MUT-INDICATOR-RANGE") and nm == "DIAGONAL":
                w = [Fraction(1, n)] * n
            row["mass_at_the_point_mass_" + tag] = str(sum(w[i] for i in memb))
            row["point_mass_" + tag + "_is_invariant"] = all(
                len({w[i] for i in o}) == 1 for o in O4)
        row["reachable_range_over_the_invariant_simplex"] = "[0,1]"
        ranges.append(row)
    rng_ok = all(r.get("mass_at_the_point_mass_inside") == "1"
                 and r.get("mass_at_the_point_mass_outside") == "0"
                 and r.get("point_mass_inside_is_invariant")
                 and r.get("point_mass_outside_is_invariant")
                 for r in ranges)
    LD.gate("G-HEADLINE-SET-RANGE-IS-THE-WHOLE-UNIT-INTERVAL",
            "how far a declaration CAN move these sets is answered at the "
            "theorem level and measured on the objects: each headline set "
            "contains a whole gauge orbit and its complement contains a "
            "whole gauge orbit, so the two orbit point masses are invariant "
            "measures -- extreme points of the parent's simplex -- and the "
            "set's mass at them is measured to be exactly 1 and exactly 0.  "
            "The reachable range of every headline set's mass over the "
            "invariant simplex is therefore the whole unit interval, which "
            "is what makes any particular spread a fact about the declared "
            "census and not about what declaring buys",
            rng_ok, "%d sets; masses at the two witness point masses %s"
            % (len(ranges),
               [(r["set"], r.get("mass_at_the_point_mass_inside"),
                 r.get("mass_at_the_point_mass_outside")) for r in ranges]))
    # the parent's own two columns, reproduced here
    nc = [r for r in rows if r["set"] == "NON-COMMUTING"][0]
    cnt_ok = (nc["mass_by_declared_dynamics"].get(
        "METROPOLIS-AT-COUNTING") == pv["PV-P23-NC-COUNTING"]
        and nc["mass_by_declared_dynamics"].get(
            "METROPOLIS-AT-ORBIT-UNIFORM-CHART-32") == pv["PV-P23-NC-ORB32"])
    LD.gate("G-RELATIVITY-CENSUS",
            "the pin's fourth stage, answered on the objects: the stationary "
            "measure MOVES across the declared-dynamics fibre, and the "
            "movement is priced on the parent's own headline sets rather "
            "than on sets chosen to make it large.  Three of the columns are "
            "the parent's own measures -- the composition walk's column IS "
            "the counting measure and both orbit-uniform columns are its own "
            "nulls -- and two of those cells are additionally checked "
            "against named paths in the parent's receipt, which is what "
            "makes the new columns comparable.  The spread is published at "
            "both populations and at the parent's own comparison class, and "
            "no comparison between populations of different size is drawn "
            "from it",
            moves and cnt_ok,
            "widest spread %s over the %d GAUGE-COVARIANT deriving "
            "instances on %s; over all %d deriving instances, the declared "
            "non-covariant control included, it is %s; at the parent's own "
            "three measures it is %s against the parent's published %s; "
            "%d sets weighed"
            % (widest, len(cov), argmax_sets, len(der), widest_all,
               restricted, parent_widest, len(rows)))

    pis = {r["instance"]: S["_pi"][r["instance"]] for r in der}
    if mut("MUT-QUASI"):
        pis = {k: S["_pi"][der[0]["instance"]] for k in pis}
    agree = len({tuple(v) for v in pis.values()}) == 1
    LD.gate("G-QUASI-DERIVATION-ARM-IS-DECIDED-NOT-ASSUMED",
            "the pin's strongest honest outcome -- all candidates agree, so "
            "the measure is quasi-derived -- is DECIDED by comparing the "
            "deriving instances' vectors entry by entry, not inferred from "
            "the spread table: it is reachable, it is the outcome this "
            "instrument would emit if the vectors coincided, and it is "
            "measured to fail",
            not agree,
            "%d deriving instances carry %d distinct stationary vectors"
            % (len(der), len({tuple(S["_pi"][r["instance"]]) for r in der})))

    S["relativity"] = {
        "rows": [{k: v for k, v in r.items() if not k.startswith("_")}
                 for r in rows],
        "widest_spread": str(widest),
        "gauge_covariant_deriving_instances": len(cov),
        "widest_spread_over_every_deriving_instance": str(widest_all),
        "widest_attained_on": argmax_sets,
        "widest_attained_count": len(argmax_sets),
        "parent_widest_spread_over_its_own_three_named_nulls":
            str(parent_widest),
        "this_census_restricted_to_the_parents_own_three_measures":
            str(restricted),
        "restricted_comparison_attained_on": restricted_on,
        "parent_measures_contained_in_this_census":
            "%d of %d" % (len(rep), len(PARENT_THREE)),
        "the_representative_instances": sorted(
            (k, v[0]) for k, v in rep.items()),
        "new_law_native_measures_entering_the_comparison":
            sum(1 for r in der if r["family"].startswith("(c)")),
        "headline_set_range_over_the_invariant_simplex": ranges,
        "deriving_instances": len(der),
        "all_deriving_instances_agree": agree,
        "measure_labels": "EVERY MASS IS LABELLED WITH THE DECLARED DYNAMICS "
                          "WHOSE STATIONARY MEASURE PRODUCES IT; THE "
                          "CONFIGURATION COLUMN IS A COUNT AND IS STAMPED "
                          "COUNTING-ONLY (E-24)",
    }
    SEAL.take("THE RELATIVITY CENSUS", "relativity", "G-RELATIVITY-CENSUS",
              S["relativity"])
    return widest, argmax_sets, agree


def measure_the_surjection(S, published, pv):
    """THE PRICE IS CONSERVED.  The covariant-dynamics fibre does not shrink
    the parent's simplex: it surjects onto it.  Measured three ways."""
    n = len(S["_coins"])
    by = {r["instance"]: r for r in published}
    hits = []
    for nm in ("COUNTING", "ORBIT-UNIFORM-CHART-32",
               "ORBIT-UNIFORM-CHART-128"):
        inst = "METROPOLIS-AT-" + nm
        hits.append({"target": nm, "instance": inst,
                     "derives": by[inst]["verdict"] == "DERIVES",
                     "stationary_equals_the_target":
                         S["_pi"][inst] == S["_nulls"][nm],
                     "covariant": by[inst]["gauge_covariant"]})
    for h in hits:
        P, m = S["_P"][h["instance"]]
        h["detailed_balance_failures"] = reversibility_failures(
            P, S["_pi"][h["instance"]], m)
    ctrl = by["METROPOLIS-AT-A-NON-INVARIANT-TARGET"]
    ctrl_pi = S["_pi"][ctrl["instance"]]
    ctrl_hits = (ctrl_pi == S["_ctrl_target"])
    ctrl_invariant = all(len({ctrl_pi[i] for i in o}) == 1 for o in S["_O4"])
    ctrl_gauge_covariant = ctrl["gauge_covariant"]

    # the exhaustive small-carrier arm: every invariant target on a declared
    # small carrier at a declared denominator is reached
    orbs = [[0, 1], [2], [3]]
    tot = bad = 0
    D = 12
    for a in range(1, D - 1):
        for b in range(1, D - a):
            c = D - a - b
            if c < 1:
                continue
            t = [Fraction(a, 2 * D), Fraction(a, 2 * D), Fraction(b, D),
                 Fraction(c, D)]
            P = metropolis(t, 4)
            if mut("MUT-SURJECTION") and tot == 0:
                P = metropolis([Fraction(1, 4)] * 4, 4)
            bas, _rk = stationary_by_elimination(P, 4)
            tot += 1
            if len(bas) != 1 or bas[0] != t:
                bad += 1
    ok = (all(h["derives"] and h["stationary_equals_the_target"]
              and h["covariant"] and h["detailed_balance_failures"] == 0
              for h in hits)
          and ctrl_hits and not ctrl_invariant
          and not ctrl_gauge_covariant and bad == 0)
    LD.gate("G-PRICE-IS-CONSERVED",
            "the surjection is exhibited on three levels and the control "
            "arm shows what covariance is doing: every declared INVARIANT "
            "target is the unique stationary measure of a COVARIANT "
            "irreducible chain built by one declared construction, so the "
            "covariant-dynamics fibre reaches every point of the parent's "
            "invariant simplex it was handed; the same construction at a "
            "target measured NOT to be orbit-constant lands outside that "
            "simplex, so it is covariance and not dynamics that confines "
            "the answer to the parent's object; and on a declared small "
            "carrier the surjection is verified EXHAUSTIVELY at a declared "
            "denominator, every target reached exactly",
            ok, "%d invariant targets reached exactly; the non-invariant "
            "control lands on its own target (%s), is gauge-covariant: %s, "
            "and is orbit-constant: %s; exhaustive arm %d targets, %d "
            "failures"
            % (len(hits), ctrl_hits, ctrl_gauge_covariant, ctrl_invariant,
               tot, bad))
    S["surjection"] = {
        "targets_reached": hits,
        "non_invariant_control_reached_its_target": ctrl_hits,
        "non_invariant_control_is_orbit_constant": ctrl_invariant,
        "non_invariant_control_is_gauge_covariant": ctrl_gauge_covariant,
        "exhaustive_small_carrier_targets": tot,
        "exhaustive_small_carrier_failures": bad,
        "exhaustive_small_carrier_states": 4,
        "exhaustive_small_carrier_orbits": orbs,
        "exhaustive_small_carrier_denominator": D,
        "consequence": "THE-COVARIANT-DYNAMICS-FIBRE-SURJECTS-ONTO-THE-"
                       "INVARIANT-SIMPLEX",
        "price_chart_32": pv["PV-SIMP32"], "price_chart_128": pv["PV-SIMP128"],
    }
    SEAL.take("THE SURJECTION", "surjection", "G-PRICE-IS-CONSERVED",
              S["surjection"],
              omit={"closed_simplex", "dropped_covariance"})

    # ---- THE CLOSED SIMPLEX.  A target with a zero is still reached
    # exactly: the Metropolis chain at it has its zeros as TRANSIENT states
    # and exactly ONE closed class, so by this unit's own sharp criterion it
    # DERIVES and the boundary target is its unique stationary measure.  What
    # the boundary costs is irreducibility, not derivation -- so the reach is
    # onto the CLOSED simplex and not onto its interior only.
    btot = breached = bone = birr = 0
    for m in (3, 4, 5):
        for code in range(1, (1 << m) - 1):
            Zs = [i for i in range(m) if (code >> i) & 1]
            if len(Zs) > m - 2:
                continue
            sup = [i for i in range(m) if i not in Zs]
            t = [Fraction(0)] * m
            for i in sup:
                t[i] = Fraction(1, len(sup))
            P = metropolis(t, m)
            if mut("MUT-BOUNDARY") and btot == 0:
                P = metropolis([Fraction(1, m)] * m, m)
            adj = support_adj(P, m)
            comps = sccs(m, adj)
            closed, _c = closed_classes(m, adj, comps)
            bas, _r = stationary_by_elimination(P, m)
            btot += 1
            if len(closed) == 1:
                bone += 1
            if len(comps) == 1:
                birr += 1
            if len(bas) == 1 and bas[0] == t:
                breached += 1
    big = []
    for k in (1, 5, 100):
        live = S["_O4"][k:]
        t = [Fraction(0)] * n
        for o in live:
            for i in o:
                t[i] = Fraction(1, len(live) * len(o))
        Pb = metropolis(t, n)
        adj = support_adj(Pb, n)
        comps = sccs(n, adj)
        closed, _c = closed_classes(n, adj, comps)
        big.append({"whole_orbits_at_mass_zero": k,
                    "states_at_mass_zero": sum(len(o) for o in S["_O4"][:k]),
                    "communicating_classes": len(comps),
                    "closed_classes": len(closed),
                    "irreducible": len(comps) == 1,
                    "stationary_equals_the_target":
                        verify_stationary(Pb, t, n),
                    "gauge_covariance_failures":
                        covariance_failures(Pb, n, S["_G4"])})
    bok = (btot > 0 and breached == btot and bone == btot and birr == 0
           and all(b["closed_classes"] == 1 and not b["irreducible"]
                   and b["stationary_equals_the_target"]
                   and b["gauge_covariance_failures"] == 0 for b in big))
    LD.gate("G-THE-SURJECTION-REACHES-THE-CLOSED-SIMPLEX",
            "the surjection is stated at FULL strength, and the boundary arm "
            "is measured rather than conceded: at a target with zeros the "
            "same construction returns a chain whose zero states are "
            "TRANSIENT and which has exactly ONE closed class, so by this "
            "unit's own sharp criterion it DERIVES and the boundary target is "
            "its unique stationary measure.  Every zero pattern with at "
            "least two supported states is enumerated exhaustively on the "
            "declared small carriers, and the arm is repeated on the REAL "
            "640-state carrier with whole gauge orbits set to mass zero, "
            "where the chain is additionally measured gauge-covariant and "
            "the identity pi P = pi is verified at full size.  What the "
            "boundary costs is irreducibility, not derivation",
            bok,
            "%d boundary targets enumerated over the small carriers, %d "
            "reached exactly, %d with exactly one closed class, %d "
            "irreducible; at the arena: %s"
            % (btot, breached, bone, birr,
               [(b["whole_orbits_at_mass_zero"], b["communicating_classes"],
                 b["closed_classes"], b["stationary_equals_the_target"],
                 b["gauge_covariance_failures"]) for b in big]))
    S["surjection"]["closed_simplex"] = {
        "small_carrier_boundary_targets": btot,
        "small_carrier_reached_exactly": breached,
        "small_carrier_with_exactly_one_closed_class": bone,
        "small_carrier_irreducible": birr,
        "small_carrier_states": [3, 4, 5],
        "at_the_arena": big,
        "consequence": "THE-COVARIANT-DYNAMICS-FIBRE-SURJECTS-ONTO-THE-"
                       "CLOSED-INVARIANT-SIMPLEX-BOUNDARY-INCLUDED",
    }
    SEAL.take("THE CLOSED-SIMPLEX ARM", "surjection/closed_simplex",
              "G-THE-SURJECTION-REACHES-THE-CLOSED-SIMPLEX",
              S["surjection"]["closed_simplex"])

    # ---- and the free corollary the theorem carries: the construction is
    # silent about invariance except through covariance, so at ANY
    # full-support target the same chain returns that target.  Dropped
    # covariance, the same move costs the WHOLE simplex.
    ctrl_sup = list(S["_ctrl_target"])
    if mut("MUT-DROPPED-COVARIANCE"):
        ctrl_sup[0] = Fraction(0)
    ctrl_full_support = all(x > 0 for x in ctrl_sup)
    price_nocov = n - 1
    dok = (price_nocov > pv["PV-SIMP32"] and ctrl_hits and ctrl_full_support
           and not ctrl_invariant and not ctrl_gauge_covariant)
    LD.gate("G-DROPPED-COVARIANCE-COSTS-THE-WHOLE-SIMPLEX",
            "the price is conserved ONLY under a retained covariance "
            "declaration, and the corollary is stated with its number: the "
            "Metropolis construction is uniform in its target and silent "
            "about invariance except through covariance, so at any "
            "FULL-SUPPORT target -- invariant or not -- it returns a chain "
            "with that target as its unique stationary measure.  The control "
            "is that witness, measured full support, measured to land on its "
            "own non-invariant target and measured NOT gauge-covariant.  "
            "Without the covariance declaration the dynamics fibre reaches "
            "the whole simplex over this carrier and the declaration costs "
            "its full dimension instead of the invariant one",
            dok,
            "the control's target is full support: %s, reached exactly: %s, "
            "orbit-constant: %s, gauge-covariant: %s; price with covariance "
            "%d, price without it %d"
            % (ctrl_full_support, ctrl_hits, ctrl_invariant,
               ctrl_gauge_covariant, pv["PV-SIMP32"], price_nocov))
    S["surjection"]["dropped_covariance"] = {
        "price_with_the_covariance_declaration": pv["PV-SIMP32"],
        "price_without_the_covariance_declaration": price_nocov,
        "the_controls_target_is_full_support": ctrl_full_support,
        "the_control_lands_on_its_own_non_invariant_target": ctrl_hits,
        "the_control_is_gauge_covariant": ctrl_gauge_covariant,
        "what_covariance_buys":
            "THE-DIFFERENCE-BETWEEN-THE-WHOLE-SIMPLEX-AND-THE-INVARIANT-ONE",
    }
    SEAL.take("THE DROPPED-COVARIANCE COROLLARY",
              "surjection/dropped_covariance",
              "G-DROPPED-COVARIANCE-COSTS-THE-WHOLE-SIMPLEX",
              S["surjection"]["dropped_covariance"])
    return hits


# ===========================================================================
# SECTION 9.  THE WILSON SEGMENT -- LICENSED, GATED, AND STAMPED
# ===========================================================================

REGISTERED_KEY_RE = r"wilson|expectation|loop_average|loop_mean"
STAMP = "CONDITIONAL-ON-THE-DECLARED-DYNAMICS"


def registered_keys_at_every_depth(obj, path="", out=None):
    """the payload is walked to the BOTTOM.  A depth-1 scan is defeated by
    one level of nesting, so every mapping in the published tree is
    visited."""
    if out is None:
        out = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            if isinstance(k, str) and k.startswith("_") and not path:
                continue
            here = path + "/" + str(k)
            if isinstance(k, str) and re.search(REGISTERED_KEY_RE, k, re.I):
                out.append(here)
            registered_keys_at_every_depth(v, here, out)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            registered_keys_at_every_depth(v, path + "/%d" % i, out)
    return out


def declared_function_names(tree):
    """every function this source defines, however it defines it."""
    names = set()
    for nd in ast.walk(tree):
        if isinstance(nd, (ast.FunctionDef, ast.AsyncFunctionDef)):
            names.add(nd.name)
        elif isinstance(nd, ast.Assign) and isinstance(nd.value, ast.Lambda):
            for t in nd.targets:
                if isinstance(t, ast.Name):
                    names.add(t.id)
                elif isinstance(t, ast.Tuple):
                    for e in t.elts:
                        if isinstance(e, ast.Name):
                            names.add(e.id)
    return names


def measure_wilson(S, published, pv):
    """the loop observable, rebuilt from R5's own words, and its expectation
    under every measure that DERIVES given its declared dynamics.  Nothing
    else is computed and no loop family is grown."""
    lat, coins = S["_lat"], S["_coins"]
    ns = len(lat.sites)
    base = lat.plaqs[0]
    corners = plaq_corners(lat, base)
    tb, tf = [], []
    for m in coins:
        cfg = uniform_cfg(lat, m)
        W = holonomy(lat, base, cfg, ns)
        s = ZERO
        for i in corners:
            s = fadd(s, W.get((i, i), ZERO))
        tb.append(s)
        s2 = ZERO
        for i in range(ns):
            s2 = fadd(s2, W.get((i, i), ZERO))
        tf.append(s2)
    if mut("MUT-WILSON-OBSERVABLE"):
        tb[0] = fadd(tb[0], ONE)
    # plaquette independence, on EVERY plaquette and EVERY configuration
    dep = 0
    for j, m in enumerate(coins):
        cfg = uniform_cfg(lat, m)
        for p in lat.plaqs:
            W = holonomy(lat, p, cfg, ns)
            s = ZERO
            for i in plaq_corners(lat, p):
                s = fadd(s, W.get((i, i), ZERO))
            if s != tb[j]:
                dep += 1
    inq = sum(1 for x in tb if in_q_sqrt2(x))
    offset_ok = all(fadd(tb[i], (ns - 4, 0, 0, 0, 1)) == tf[i]
                    for i in range(len(coins)))
    LD.gate("G-WILSON-OBSERVABLE-REBUILT",
            "the loop observable is REBUILT from R5's own definition, quoted "
            "at a verbatim anchor: the ordered product around the plaquette "
            "boundary with each factor inverted where the boundary runs "
            "against the link's own direction, whose whole holonomy lives in "
            "a four-by-four block.  The declared observable is that block's "
            "trace; the full carrier trace is measured to be the same "
            "quantity plus the untouched identity, so the normalisation "
            "fibre is 2 and both members are published.  The value is "
            "independent of WHICH plaquette on this carrier -- checked at "
            "every plaquette and every configuration -- and lies in the real "
            "subfield Q(sqrt2) at every one of them",
            dep == 0 and inq == len(coins) and offset_ok,
            "%d plaquette-dependent cells of %d; %d of %d block traces in "
            "Q(sqrt2); the full trace equals the block trace plus the "
            "untouched identity: %s"
            % (dep, len(coins) * len(lat.plaqs), inq, len(coins), offset_ok))

    O4 = S["_O4"]
    tbg = list(tb)
    if mut("MUT-WILSON-GAUGE-INVARIANCE"):
        big4 = [o for o in O4 if len(o) > 1][0]
        tbg[big4[1]] = fadd(tbg[big4[1]], ONE)
    gauge_inv = all(len({tbg[i] for i in o}) == 1 for o in O4)
    LD.gate("G-WILSON-OBSERVABLE-IS-GAUGE-INVARIANT",
            "the observable is constant on every orbit of the residual gauge "
            "group -- checked orbit by orbit -- which is what makes its "
            "expectation under an invariant measure a function of the "
            "measure's orbit weights alone, and what makes the range "
            "computed below exactly the convex hull of the orbit values",
            gauge_inv, "constant on all %d orbits: %s" % (len(O4), gauge_inv))

    der = [r for r in published if r["verdict"] == "DERIVES"]
    licensed = [r for r in der if r["covariant"]]
    rows = []
    exps = []
    for r in sorted(der, key=lambda x: x["instance"]):
        pi = S["_pi"][r["instance"]]
        acc = ZERO
        for i, w in enumerate(pi):
            if w:
                acc = fadd(acc, fscal(tb[i], w.numerator, w.denominator))
        exps.append(acc)
        rows.append({
            "declared_dynamics": r["instance"],
            "family": r["family"],
            "the_measure": r["measure_name"],
            "derives_given_the_declared_dynamics": True,
            "block_trace_value": qsqrt2_str(acc),
            "full_trace_value": qsqrt2_str(fadd(acc, (ns - 4, 0, 0, 0, 1))),
            "stamp": STAMP,
        })
    if mut("MUT-WILSON-UNLICENSED"):
        red = [r for r in published if r["verdict"] == "REDUCIBLE"][0]
        rows.append({"declared_dynamics": red["instance"],
                     "family": red["family"], "the_measure": "NONE",
                     "derives_given_the_declared_dynamics": False,
                     "block_trace_value": "3/8", "full_trace_value": "3/8",
                     "stamp": STAMP})
    if mut("MUT-WILSON-UNSTAMPED"):
        rows[0] = dict(rows[0])
        rows[0]["stamp"] = "PLAIN"

    # the range over the invariant simplex: the convex hull of the orbit
    # values, whose endpoints are attained at extreme points.  This carried
    # section 8's headline and carried it with no gate and a typed flag; it
    # is measured here, the extreme-point flag DERIVED from the measured
    # orbit sizes, and every published expectation required to lie inside it.
    vals = []
    for o in O4:
        vals.append((qsqrt2_pair(tb[o[0]]), o))
    lo = hi = vals[0]
    for v in vals[1:]:
        if qs_less(v[0], lo[0]):
            lo = v
        if qs_less(hi[0], v[0]):
            hi = v
    if mut("MUT-WILSON-RANGE"):
        lo = (lo[0], lo[1] + [i for i in range(len(coins))
                              if i not in lo[1]][:1])
    lo_r = all(qsqrt2_pair(tb[i])[1] == 0 for i in lo[1])
    hi_r = all(qsqrt2_pair(tb[i])[1] == 0 for i in hi[1])
    both_extreme = (len(lo[1]) == 1 and len(hi[1]) == 1)
    inside = sum(1 for a in exps
                 if not qs_less(qsqrt2_pair(a), lo[0])
                 and not qs_less(hi[0], qsqrt2_pair(a)))
    lo_const = all(tb[i] == tb[lo[1][0]] for i in lo[1])
    hi_const = all(tb[i] == tb[hi[1][0]] for i in hi[1])
    LD.gate("G-WILSON-RANGE-IS-MEASURED",
            "section 8's headline -- that covariance pins the expectation "
            "nowhere -- rests on the range of the expectation over the "
            "invariant simplex, so the range is a GATE and its extreme-point "
            "flag is DERIVED from measured orbit sizes rather than typed: "
            "the minimum and maximum are taken over the orbit values by "
            "exact ordering on the real subfield, each endpoint orbit is "
            "measured to be constant and measured to have size one -- so its "
            "point mass is an extreme point of the invariant simplex -- and "
            "every published expectation is required to lie inside the "
            "interval",
            both_extreme and lo_const and hi_const and inside == len(exps),
            "range [%s, %s]; endpoint orbit sizes %d and %d; both endpoints "
            "at extreme points: %s; %d of %d published expectations inside "
            "the interval"
            % (str(lo[0][0]) if lo_r else qsqrt2_str(tb[lo[1][0]]),
               str(hi[0][0]) if hi_r else qsqrt2_str(tb[hi[1][0]]),
               len(lo[1]), len(hi[1]), both_extreme, inside, len(exps)))

    S["wilson"] = {
        "observable": "THE-TRACE-OF-THE-PLAQUETTE-HOLONOMY-ON-ITS-OWN-"
                      "FOUR-CORNER-BLOCK",
        "normalisation_fibre": 2,
        "loop_families_grown": 0,
        "plaquettes_checked": len(lat.plaqs),
        "distinct_values_over_the_carrier": len(set(tb)),
        "rows": rows,
        "licensed_rows": len(rows),
        "covariant_licensed_rows": len(licensed),
        "range_over_the_invariant_simplex": {
            "minimum": str(lo[0][0]) if lo_r else qsqrt2_str(tb[lo[1][0]]),
            "maximum": str(hi[0][0]) if hi_r else qsqrt2_str(tb[hi[1][0]]),
            "minimum_attained_on_an_orbit_of_size": len(lo[1]),
            "maximum_attained_on_an_orbit_of_size": len(hi[1]),
            "both_endpoints_are_extreme_points_of_the_simplex": both_extreme,
            "published_expectations_inside_the_interval": inside,
            "stamp": STAMP,
        },
        "must_not": "NO-AREA-LAW-NO-STRING-TENSION-NO-POTENTIAL-CLAIM-AND-"
                    "NO-LOOP-FAMILY-IS-GROWN",
    }

    verdicts = {r["instance"]: r["verdict"] for r in published}
    unlicensed = [r["declared_dynamics"] for r in rows
                  if verdicts.get(r["declared_dynamics"]) != "DERIVES"]
    unstamped = [r["declared_dynamics"] for r in rows
                 if r.get("stamp") != STAMP]
    # the payload is walked to the BOTTOM for an expectation-valued key at
    # any depth -- the assembled wilson object included -- and every one must
    # sit under this unit's single registered key
    everywhere = registered_keys_at_every_depth(
        {k: v for k, v in S.items() if not k.startswith("_")})
    stray = [k for k in everywhere if not k.startswith("/wilson")]
    LD.gate("G-WILSON-LICENCE",
            "the pin licenses an expectation ONLY under a measure that "
            "derives at the RSQ standard GIVEN the declared dynamics, and "
            "the licence is enforced per row and not per table (#87): every "
            "published expectation names the dynamics it is conditional on, "
            "that dynamics' verdict is looked up in the census this run "
            "computed, and every row carries the stamp "
            "CONDITIONAL-ON-THE-DECLARED-DYNAMICS.  An expectation under a "
            "reducible dynamics, or an unstamped one, dies here",
            not unlicensed and not unstamped and not stray
            and len(rows) == len(der),
            "%d expectation rows, %d under a non-deriving dynamics %s, "
            "%d unstamped %s; %d expectation-valued keys at any depth of the "
            "payload, %d outside the registered key %s"
            % (len(rows), len(unlicensed), unlicensed[:3], len(unstamped),
               unstamped[:3], len(everywhere), len(stray), stray[:3]))

    SEAL.take("THE WILSON SEGMENT", "wilson", "G-WILSON-LICENCE", S["wilson"])
    S["_wilson_range"] = (lo[0][0], hi[0][0])

    # =======================================================================
    # THE CONTROL'S ENUMERATION, DISCLOSED AND PRICED
    #
    # The declared non-covariant control's target is built on CONTIGUOUS
    # BLOCKS OF THE COIN INDEX.  Those blocks are not an arena object: they
    # are an artifact of the order in which this instrument enumerates the
    # coin family.  R5's declaration -- exhaustive over the alphabet's fourth
    # power -- admits a second literal reading of the ALPHABET's own order
    # (modulus-major rather than power-major), which returns the same 640
    # coins as a SET in a different order.  The two order-dependent numbers
    # are re-measured there and published as a sensitivity row; the
    # like-for-like headline, computed over the covariant instances only, is
    # measured to be unchanged, because those measures are functions of
    # sector and orbit membership alone.
    # =======================================================================
    alt_alph = [ZERO]
    for t in range(8):
        alt_alph.append(zpow(t))
    for t in range(8):
        alt_alph.append(fscal(zpow(t), 1, 2))
    for t in range(8):
        alt_alph.append(fmul(zpow(t), INV_SQRT2))
    if mut("MUT-ENUMERATION"):
        alt_alph = list(S["_alph"])
    alt_coins, _alt_rows = build_coins(alt_alph)
    same_set = (len(alt_coins) == len(coins)
                and set(alt_coins) == set(coins)
                and len(alt_alph) == len(S["_alph"])
                and set(alt_alph) == set(S["_alph"]))
    orders_differ = (alt_coins != coins)
    cidx = S["_cidx"]
    alt_idx = [cidx[m] for m in alt_coins] if same_set else []
    nb = len(S["_ctrl_blocks"])
    bs = len(coins) // nb
    wts = [Fraction(b + 1, 10) for b in range(nb)]
    alt_t = [Fraction(0)] * len(coins)
    for b in range(nb):
        for p in range(b * bs, (b + 1) * bs):
            alt_t[alt_idx[p]] = wts[b] / bs
    Pa = metropolis(alt_t, len(coins))
    adj = support_adj(Pa, len(coins))
    comps = sccs(len(coins), adj)
    closed, _c = closed_classes(len(coins), adj, comps)
    alt_ok = (len(closed) == 1
              and verify_stationary(Pa, alt_t, len(coins)))
    acc = ZERO
    for i, w in enumerate(alt_t):
        if w:
            acc = fadd(acc, fscal(tb[i], w.numerator, w.denominator))
    alt_exp = qsqrt2_str(acc)
    delivered_exp = [r["block_trace_value"] for r in rows
                     if "NON-INVARIANT" in r["declared_dynamics"]][0]
    # and the two spreads, re-measured with the alternative control in place
    cov_pis = [S["_pi"][r["instance"]] for r in der
               if r["gauge_covariant"]]
    all_pis_alt = cov_pis + [alt_t]
    wid_cov = wid_alt = Fraction(0)
    for nm, memb in sorted(S["_sets"].items()):
        ms = [sum(v[i] for i in memb) for v in cov_pis]
        wid_cov = max(wid_cov, max(ms) - min(ms))
        ms2 = [sum(v[i] for i in memb) for v in all_pis_alt]
        wid_alt = max(wid_alt, max(ms2) - min(ms2))
    rel = S["relativity"]
    headline_free = (str(wid_cov) == rel["widest_spread"])
    LD.gate("G-CONTROL-TARGET-ENUMERATION-SENSITIVITY",
            "the declared control's target is defined on contiguous blocks "
            "of the coin INDEX, which is an artifact of this instrument's "
            "enumeration and not an object of the arena -- so the two "
            "numbers that depend on it are DISCLOSED and PRICED rather than "
            "published bare.  A second literal reading of the parents' own "
            "alphabet declaration is built here, measured to return the same "
            "640 coins as a set in a different order, and the control is "
            "rebuilt on it: its expectation and the spread over all deriving "
            "instances are re-measured there and published as a sensitivity "
            "row.  The like-for-like headline -- the spread over the "
            "GAUGE-COVARIANT deriving instances -- is measured to be "
            "identical under both enumerations, because those measures are "
            "functions of sector and orbit membership alone",
            same_set and orders_differ and alt_ok and headline_free,
            "the alternative enumeration returns the same set: %s, in a "
            "different order: %s; its control chain has one closed class and "
            "lands on its own target: %s; expectation %s against the "
            "delivered %s; spread over all deriving instances %s against the "
            "delivered %s; the covariant headline %s is enumeration-free: %s"
            % (same_set, orders_differ, alt_ok, alt_exp, delivered_exp,
               wid_alt, rel["widest_spread_over_every_deriving_instance"],
               wid_cov, headline_free))
    S["enumeration_sensitivity"] = {
        "the_declared_control_target_is":
            "FOUR-CONTIGUOUS-BLOCKS-OF-THE-COIN-INDEX-AT-MASSES-1-2-3-4-"
            "TENTHS-WHICH-IS-AN-ENUMERATION-ARTIFACT-NOT-AN-ARENA-OBJECT",
        "the_alternative_reading":
            "THE-ALPHABET-ENUMERATED-MODULUS-MAJOR-RATHER-THAN-POWER-MAJOR-"
            "WITH-THE-COIN-FAMILY-EXHAUSTIVE-OVER-ITS-FOURTH-POWER",
        "same_coin_family_as_a_set": same_set,
        "a_different_order": orders_differ,
        "the_alternative_control_chain_derives": alt_ok,
        "control_expectation_delivered": delivered_exp,
        "control_expectation_alternative": alt_exp,
        "widest_spread_over_every_deriving_instance_delivered":
            rel["widest_spread_over_every_deriving_instance"],
        "widest_spread_over_every_deriving_instance_alternative":
            str(wid_alt),
        "widest_spread_over_the_covariant_deriving_instances":
            str(wid_cov),
        "the_covariant_headline_is_enumeration_free": headline_free,
        "stamp": "THE-TWO-CONTROL-DEPENDENT-NUMBERS-ARE-"
                 "ENUMERATION-RELATIVE-AND-ARE-LABELLED-SO",
    }
    SEAL.take("THE ENUMERATION SENSITIVITY", "enumeration_sensitivity",
              "G-CONTROL-TARGET-ENUMERATION-SENSITIVITY",
              S["enumeration_sensitivity"])
    return rows


# ===========================================================================
# SECTION 10.  THE FIBRE -- exactly what a dynamics declaration must supply
# ===========================================================================

def price_the_fibre(S, published, pv):
    """the choice inventory: every construction choice, its fibre, its
    declared instances, and whether moving it moves a published number.  The
    flag binds the ROW and never the total (#87)."""
    axes = {}
    for r in published:
        a = axes.setdefault(r["fibre_axis"], {"axis": r["fibre_axis"],
                                              "instances": [],
                                              "fibre": r["fibre"]})
        a["instances"].append(r["instance"])
    for a in axes.values():
        a["instances_run"] = len(a["instances"])
        vecs = set()
        for i in a["instances"]:
            if i in S["_pi"]:
                vecs.add(tuple(S["_pi"][i]))
            else:
                vecs.add(("SIMPLEX", i))
        a["distinct_outcomes_along_this_axis"] = len(vecs)
        a["verdict_determining"] = len(vecs) > 1
    rows = [
        {"choice": "THE-LATTICE-AND-ITS-SIZE", "status": "FORCED",
         "fibre": 1, "instances_built": 1,
         "why": "inherited from R5 at an anchored receipt path"},
        {"choice": "THE-COIN-FAMILY", "status": "FORCED", "fibre": 1,
         "instances_built": 1,
         "why": "enumerated exhaustively from the declared alphabet"},
        {"choice": "THE-CARRIER", "status": "DECLARED-AND-DISCLOSED",
         "fibre": 2, "instances_built": 2,
         "why": "the parent's primary carrier is used; the extension "
                "reading forces its own enlargement, which is built"},
        {"choice": "THE-ELIMINATION-CAP", "status": "FORCED-BY-COST",
         "fibre": 1, "instances_built": 1,
         "why": "set to the parent's own orbit count, which is the size of "
                "every quotient this unit solves"},
    ]
    licence = ("THE-FIBRE-IS-THE-SIMPLEX-ITSELF-AND-CANNOT-BE-SWEPT; WHAT "
               "STANDS IN FOR A SWEEP IS THE SURJECTION THEOREM, "
               "INSTANTIATED AT THE DECLARED POINTS, VERIFIED EXHAUSTIVELY "
               "AT %d TARGETS ON A DECLARED SMALL CARRIER AT %d FAILURES, "
               "AND EXTENDED TO THE CLOSED SIMPLEX AT %d BOUNDARY TARGETS"
               % (S["surjection"]["exhaustive_small_carrier_targets"],
                  S["surjection"]["exhaustive_small_carrier_failures"],
                  S["surjection"]["closed_simplex"][
                      "small_carrier_boundary_targets"]))
    for a in sorted(axes.values(), key=lambda x: x["axis"]):
        sampled = not isinstance(a["fibre"], int)
        row = {"choice": a["axis"],
               "status": "DECLARED-AND-SAMPLED" if sampled
                         else "DECLARED-AND-SWEPT",
               "fibre": a["fibre"], "instances_built": a["instances_run"],
               "distinct_outcomes": a["distinct_outcomes_along_this_axis"],
               "verdict_determining": ("NOT-MEASURED-FIBRE-SAMPLED-AT-1"
                                       if a["instances_run"] < 2
                                       else a["verdict_determining"]),
               "why": ("this axis's fibre is the simplex itself; it is "
                       "SAMPLED at the declared points and the rest is "
                       "covered by a theorem, and that is disclosed rather "
                       "than absorbed" if sampled else
                       "every declared instance of this axis is RUN and its "
                       "outcome published")}
        if sampled:
            row["sampling_licence"] = licence
        rows.append(row)
    if mut("MUT-FIBRE"):
        rows[-1]["fibre"] = 99
    # EVERY row is evaluated.  A row with an integer fibre must have built
    # every member of it; a row whose fibre is not a finite number must be
    # stamped SAMPLED and must carry the licence naming the arm that stands
    # in for the sweep.  No row is skipped by a type test.
    unswept = [r["choice"] for r in rows
               if isinstance(r["fibre"], int)
               and r["instances_built"] != r["fibre"]]
    unlicensed_rows = [r["choice"] for r in rows
                       if not isinstance(r["fibre"], int)
                       and not (r["status"] == "DECLARED-AND-SAMPLED"
                                and r.get("sampling_licence"))]
    swept_ok = not unswept and not unlicensed_rows
    LD.gate("G-FIBRE-INVENTORY",
            "every construction choice is inventoried with its fibre and its "
            "instances, and EVERY row is evaluated -- none is skipped by a "
            "type test.  A row with a finite fibre must have built every "
            "member of it, so along those axes no member of a declared fibre "
            "is left unrun; a row whose fibre is the invariant simplex "
            "itself cannot be swept and is stamped DECLARED-AND-SAMPLED, "
            "carrying the licence that names the theorem and the exhaustive "
            "arm standing in for the sweep, so the census's one sampled "
            "direction is disclosed rather than absorbed.  The "
            "verdict-determining flag binds each row by its own measured "
            "predicate where the axis carries two or more instances, and is "
            "stamped NOT-MEASURED where it carries one",
            swept_ok,
            "%d inventory rows; %d swept with instances equal to fibre, %d "
            "sampled under a declared licence; unswept %s; unlicensed %s"
            % (len(rows),
               sum(1 for r in rows if r["status"] == "DECLARED-AND-SWEPT"),
               sum(1 for r in rows if r["status"] == "DECLARED-AND-SAMPLED"),
               unswept, unlicensed_rows))
    S["fibre"] = {"rows": rows,
                  "price_of_a_covariant_declaration_chart_32":
                      pv["PV-SIMP32"],
                  "price_of_a_covariant_declaration_chart_128":
                      pv["PV-SIMP128"],
                  "price_without_the_covariance_declaration":
                      S["surjection"]["dropped_covariance"][
                          "price_without_the_covariance_declaration"],
                  "what_a_declaration_must_supply":
                      "ONE-POINT-OF-THE-INVARIANT-SIMPLEX-OVER-THE-CARRIERS-"
                      "ORBITS-EXACTLY-AS-BEFORE"}
    SEAL.take("THE FIBRE", "fibre", "G-FIBRE-INVENTORY", S["fibre"])
    return rows


# ===========================================================================
# SECTION 11.  THE HEAD, DERIVED TWICE BY TWO LAWS
# ===========================================================================

PREREGISTERED = ["SMU-DERIVED", "SMU-QUASI-DERIVED", "SMU-REDUCIBLE",
                 "SMU-DYNAMICS-RELATIVE", "SMU-BLOCKED-AT"]


def head_law(published, agree, widest, blocked, rel):
    """the builder's head law.  The spread's POPULATION is taken from the
    same measured field the spread itself came from -- the covariant deriving
    count -- and never from the deriving count, because those are different
    numbers and the head must name the one it measured."""
    if blocked:
        return "SMU-BLOCKED-AT-%s" % blocked
    der = [r for r in published if r["verdict"] == "DERIVES"]
    red = [r for r in published if r["verdict"] == "REDUCIBLE"]
    n_cov = rel["gauge_covariant_deriving_instances"]
    if mut("MUT-K1-A"):
        n_cov = len(der)
    if not der:
        return "SMU-REDUCIBLE-%d-INSTANCES-0-DERIVE" % len(red)
    if agree:
        return "SMU-QUASI-DERIVED-ALL-%d-DERIVING-INSTANCES-AGREE" % len(der)
    if widest > 0:
        return ("SMU-DYNAMICS-RELATIVE-SPREAD-%s-OVER-THE-%d-GAUGE-"
                "COVARIANT-DERIVING-INSTANCES" % (widest, n_cov))
    return "SMU-DERIVED-%d" % len(der)


def second_head_law(published, agree, widest, blocked, rel):
    """an INDEPENDENT reconstruction -- and DE-TWINNED from the builder's.
    It accepts neither of the builder's aggregates: it recounts the covariant
    deriving population from the instance records one by one, and it re-takes
    the widest spread as a maximum over the published relativity rows.  Two
    head laws that read the same aggregate through the same template cannot
    disagree about it however wrong it is; these two can, so an edit to one
    side alone dies at G-HEAD-DERIVED-TWICE."""
    if blocked is not None and blocked != "":
        return "SMU-BLOCKED-AT-" + str(blocked)
    n_der = sum(1 for r in published if r["verdict"] == "DERIVES")
    n_red = sum(1 for r in published if r["verdict"] != "DERIVES")
    n_cov = 0
    for r in published:
        if (r["verdict"] == "DERIVES"
                and r["gauge_covariant"] in (True, "True")):
            n_cov += 1
    spreads = [Fraction(str(row["spread_over_the_covariant_instances"]))
               for row in rel["rows"]]
    w2 = max(spreads) if spreads else Fraction(0)
    if n_der == 0:
        return "SMU-REDUCIBLE-" + str(n_red) + "-INSTANCES-0-DERIVE"
    if not agree and w2 > 0:
        return ("SMU-DYNAMICS-RELATIVE-SPREAD-" + str(w2) + "-OVER-THE-"
                + str(n_cov) + "-GAUGE-COVARIANT-DERIVING-INSTANCES")
    if agree:
        return ("SMU-QUASI-DERIVED-ALL-" + str(n_der)
                + "-DERIVING-INSTANCES-AGREE")
    return "SMU-DERIVED-" + str(n_der)


def demonstrate_reachability(S, published):
    """the other pre-registered outcomes are REACHABLE, and the reachability
    is RUN rather than advertised: the same head law is handed synthetic
    census tables and must return them."""
    rel = S["relativity"]
    probes = []
    one = [dict(published[0])]
    one[0] = dict(one[0])
    one[0]["verdict"] = "DERIVES"
    probes.append(("SMU-QUASI-DERIVED", head_law(one, True, Fraction(0),
                                                 None, rel)))
    allred = [dict(r, verdict="REDUCIBLE") for r in published]
    probes.append(("SMU-REDUCIBLE", head_law(allred, False, Fraction(0),
                                             None, rel)))
    probes.append(("SMU-BLOCKED-AT",
                   head_law(published, False, Fraction(1), "AN-OBJECT", rel)))
    probes.append(("SMU-DYNAMICS-RELATIVE",
                   head_law(published, False, Fraction(1, 2), None, rel)))
    if mut("MUT-REACHABILITY"):
        probes = [(w, "SMU-DYNAMICS-RELATIVE") for w, _g in probes]
    ok = all(got.startswith(want) for want, got in probes)
    LD.gate("G-HEAD-LAW-REACHABILITY",
            "every pre-registered outcome is REACHABLE on this instrument's "
            "own head law, and the reachability is RUN in the delivery run "
            "rather than advertised: the law is handed synthetic census "
            "tables that would have produced each other outcome and must "
            "return it, so a head law that had collapsed to a constant dies "
            "here (#34)",
            ok, "; ".join("%s -> %s" % (w, g) for w, g in probes))
    S["preregistered_heads"] = {"outcomes": PREREGISTERED,
                                "probes": [{"outcome": w, "returned": g}
                                           for w, g in probes]}
    SEAL.take("THE PRE-REGISTERED HEADS", "preregistered_heads",
              "G-HEAD-LAW-REACHABILITY", S["preregistered_heads"])


def build_verdict(S):
    """every segment is COMPUTED from a measured field; nothing is typed."""
    cen = S["census"]
    rel = S["relativity"]
    sur = S["surjection"]
    wil = S["wilson"]
    fib = S["fibre"]
    ar = S["arena"]
    ca = S["chart_action"]
    ga = S["gauge"]
    lr = S["law_refinement"]
    pr = S["privilege"]
    en = S["enumeration_sensitivity"]
    cs = sur["closed_simplex"]
    inst = {r["instance"]: r for r in cen["instances"]}

    head = cen["head"]
    seg = []
    seg.append("CENSUS=%d-FAMILIES-%d-INSTANCES-ALL-RUN-%d-DERIVE-%d-"
               "REDUCIBLE|CRITERION=%s|THE-INHERITED-FORM-IS-SUFFICIENT-"
               "NOT-NECESSARY-WITNESS-AT-%d-STATES-%d-CLASSES-%d-CLOSED"
               % (cen["families"], cen["instances_run"], cen["derive"],
                  cen["reducible"], lr["sharp"], lr["witness_states"],
                  lr["witness_communicating_classes"],
                  lr["witness_closed_classes"]))
    seg.append("(a)CHART-WALK=THE-ANCHORED-CHART-ACTS-TRIVIALLY-%d-OF-%d-"
               "ELEMENTS-INDUCE-THE-IDENTITY-SO-%d-CLOSED-CLASSES-AND-THE-"
               "WHOLE-%d-SIMPLEX-IS-STATIONARY;THE-EXTENSION-DOES-NOT-ACT-"
               "ON-THIS-CARRIER-AT-ALL-%d-OF-%d-ELEMENTS-CARRY-A-UNIFORM-"
               "CONFIGURATION-OFF-IT-AND-ITS-CLOSURE-IS-%d-STATES-WITH-%d-"
               "CLOSED-CLASSES"
               % (inst["CHART-32"]["induced_identity"],
                  ca["CHART-32"]["order"], inst["CHART-32"]["closed_classes"],
                  inst["CHART-32"]["simplex_dimension"],
                  ca["CHART-128"]["mixed_reversal"], ca["CHART-128"]["order"],
                  ca["CHART-128"]["enlarged_carrier"],
                  inst["CHART-128"]["closed_classes"]))
    seg.append("(b)GAUGE-WALK=REDUCIBLE-AT-BOTH-READINGS-%d-AND-%d-CLOSED-"
               "CLASSES-IDENTICAL-AS-SETS-TO-THE-PARENTS-ORBITS-AND-ITS-"
               "STATIONARY-SIMPLEX-IS-THE-PARENTS-INVARIANT-SIMPLEX-"
               "DIMENSION-%d-AND-%d"
               % (inst["GAUGE-CHART-32"]["closed_classes"],
                  inst["GAUGE-CHART-128"]["closed_classes"],
                  inst["GAUGE-CHART-32"]["simplex_dimension"],
                  inst["GAUGE-CHART-128"]["simplex_dimension"]))
    seg.append("(c)LAW-NATIVE-RESAMPLING=IRREDUCIBLE-AND-DERIVES-AT-ALL-%d-"
               "MEMBERS-OF-ITS-DECLARED-FIBRE;THE-MEASURE-IS-%s-SECTOR-"
               "GRADED-AT-%s-AND-INVARIANT-SO-IT-IS-A-POINT-OF-THE-PARENTS-"
               "SIMPLEX;BUT-ITS-KERNEL-IS-RANK-ONE-EVERY-ROW-OF-THE-LAW-IS-"
               "THE-SAME-VECTOR-AT-%d-OF-%d-INSTANCES-SO-THE-DERIVED-MEASURE-"
               "IS-THE-DECLARED-DRAW-LAW-READ-BACK-AND-THE-ROW-IS-STAMPED-%s"
               % (cen["law_native_instances"], cen["law_native_measure_name"],
                  "-".join(S["law_native_rates"]["values"]),
                  pr["instances_whose_stationary_measure_is_the_declared_"
                     "draw_law"], pr["instances"], pr["stamp"]))
    seg.append("(d)COMPOSITION-WALK=IRREDUCIBLE-ON-BOTH-SIDES-AND-DERIVES-"
               "THE-COUNTING-MEASURE-BECAUSE-THE-FAMILY-IS-CLOSED-UNDER-"
               "INVERSE-%d-OF-%d-SO-THE-WALK-IS-DOUBLY-STOCHASTIC-WITH-%d-"
               "OF-%d-PRODUCTS-STAYING"
               % (S["composition"]["inverse_closed"], ar["coins"],
                  S["composition"]["products_inside"],
                  S["composition"]["products_total"]))
    seg.append("(e)MONOMIAL-HAAR-WALK=REDUCIBLE-%d-CLOSED-CLASSES-OF-%d-AND-"
               "ONE-OF-THEM-IS-EXACTLY-THE-PARENTS-HAAR-CARRIER-SO-THE-"
               "CORPUS-ONE-HANDED-OVER-MEASURE-IS-ONE-EXTREME-POINT-HERE"
               % (inst["MONOMIAL-LEFT"]["closed_classes"],
                  S["composition"]["monomial_coins"]))
    seg.append("(f)COVARIANT-METROPOLIS=EVERY-DECLARED-INVARIANT-TARGET-IS-"
               "REACHED-EXACTLY-%d-OF-%d-AND-THE-NON-INVARIANT-CONTROL-"
               "LANDS-OUTSIDE-THE-SIMPLEX-ORBIT-CONSTANT=%s;EXHAUSTIVE-ARM-"
               "%d-TARGETS-%d-FAILURES"
               % (sum(1 for h in sur["targets_reached"]
                      if h["stationary_equals_the_target"]),
                  len(sur["targets_reached"]),
                  str(sur["non_invariant_control_is_orbit_constant"]).upper(),
                  sur["exhaustive_small_carrier_targets"],
                  sur["exhaustive_small_carrier_failures"]))
    seg.append("MEASURES=%d-DISTINCT-STATIONARY-VECTORS-OVER-%d-DERIVING-"
               "INSTANCES|NAMED-NULLS-REACHED=%s|NEW=%d"
               % (cen["distinct_stationary_vectors"], cen["derive"],
                  ",".join(cen["named_measures_reached"]) or "NONE",
                  cen["new_measures"]))
    seg.append("RELATIVITY=THE-MEASURE-MOVES|WIDEST-SPREAD-OVER-THE-%d-"
               "GAUGE-COVARIANT-DERIVING-INSTANCES=%s-ATTAINED-ON-%d-OF-%d-"
               "SETS(%s)"
               "|OVER-ALL-%d-DERIVING-INSTANCES-THE-DECLARED-NON-COVARIANT-"
               "CONTROL-INCLUDED=%s|AT-THE-PARENTS-OWN-THREE-MEASURES-ALL-%s-"
               "PRESENT-HERE-THIS-CENSUS-REPRODUCES-%s-EXACTLY|THE-RISE-TO-"
               "%s-IS-THE-%d-NEW-LAW-NATIVE-MEASURES-ENTERING-THE-SAME-"
               "COMPARISON-NOT-A-DYNAMICS-EFFECT|OVER-THE-WHOLE-COVARIANT-"
               "FIBRE-THE-RANGE-OF-EVERY-HEADLINE-SET-IS-%s-BY-THE-"
               "SURJECTION|QUASI-DERIVATION-ARM-REACHABLE-AND-MEASURED-TO-"
               "FAIL"
               % (rel["gauge_covariant_deriving_instances"], rel["widest_spread"],
                  rel["widest_attained_count"], len(rel["rows"]),
                  ",".join(rel["widest_attained_on"]),
                  rel["deriving_instances"],
                  rel["widest_spread_over_every_deriving_instance"],
                  rel["parent_measures_contained_in_this_census"].upper(
                  ).replace(" ", "-"),
                  rel["this_census_restricted_to_the_parents_own_three_"
                      "measures"],
                  rel["widest_spread"],
                  rel["new_law_native_measures_entering_the_comparison"],
                  rel["headline_set_range_over_the_invariant_simplex"][0][
                      "reachable_range_over_the_invariant_simplex"]))
    seg.append("ENUMERATION=THE-CONTROLS-TARGET-IS-DECLARED-ON-CONTIGUOUS-"
               "BLOCKS-OF-THE-COIN-INDEX-SO-ITS-TWO-NUMBERS-ARE-ENUMERATION-"
               "RELATIVE:UNDER-A-SECOND-ADMISSIBLE-READING-OF-THE-PARENTS-"
               "ALPHABET-THE-CONTROL-EXPECTATION-IS-%s-NOT-%s-AND-THE-SPREAD-"
               "OVER-ALL-DERIVING-INSTANCES-IS-%s-NOT-%s|THE-LIKE-FOR-LIKE-"
               "HEADLINE-%s-IS-IDENTICAL-UNDER-BOTH-ENUMERATIONS-BECAUSE-THE-"
               "COVARIANT-MEASURES-ARE-FUNCTIONS-OF-SECTOR-AND-ORBIT-"
               "MEMBERSHIP-ALONE"
               % (en["control_expectation_alternative"],
                  en["control_expectation_delivered"],
                  en["widest_spread_over_every_deriving_instance_alternative"],
                  en["widest_spread_over_every_deriving_instance_delivered"],
                  en["widest_spread_over_the_covariant_deriving_instances"]))
    seg.append("PRICE=CONSERVED-NOT-PAID:THE-COVARIANT-DYNAMICS-FIBRE-"
               "SURJECTS-ONTO-THE-CLOSED-INVARIANT-SIMPLEX-BOUNDARY-"
               "INCLUDED-%d-OF-%d-BOUNDARY-TARGETS-AT-THE-DECLARED-SMALL-"
               "CARRIERS-AND-%d-OF-%d-AT-THE-ARENA-SO-A-DECLARATION-STILL-"
               "SUPPLIES-%d-INDEPENDENT-NUMBERS-AT-THE-ANCHORED-READING-AND-"
               "%d-AT-THE-EXTENSION-READING-MEASURED-HERE-UNDER-THE-ORDER-8-"
               "GROUP-EXACTLY-THE-PARENTS-COUNTS|DROPPED-COVARIANCE-THE-SAME-"
               "MOVE-COSTS-%d|WHAT-MOVED-IS-WHERE-THE-DECLARATION-IS-MADE-"
               "NOT-HOW-MUCH-IT-COSTS"
               % (cs["small_carrier_reached_exactly"],
                  cs["small_carrier_boundary_targets"],
                  sum(1 for b in cs["at_the_arena"]
                      if b["stationary_equals_the_target"]),
                  len(cs["at_the_arena"]),
                  fib["price_of_a_covariant_declaration_chart_32"],
                  fib["price_of_a_covariant_declaration_chart_128"],
                  fib["price_without_the_covariance_declaration"]))
    seg.append("WILSON=LICENSED-BY-THE-PIN-AND-STAMPED-%s-AT-%d-OF-%d-ROWS|"
               "OBSERVABLE=%s-PLAQUETTE-INDEPENDENT-AT-%d-PLAQUETTES-AND-"
               "GAUGE-INVARIANT|VALUES=%s|RANGE-OVER-THE-INVARIANT-SIMPLEX="
               "[%s,%s]-BOTH-ENDPOINTS-ATTAINED-AT-EXTREME-POINTS-SO-"
               "COVARIANCE-PINS-THE-EXPECTATION-NOWHERE|NO-AREA-LAW-NO-"
               "STRING-TENSION-NO-POTENTIAL-CLAIM-AND-%d-LOOP-FAMILIES-GROWN"
               % (STAMP, wil["licensed_rows"], wil["licensed_rows"],
                  wil["observable"], wil["plaquettes_checked"],
                  ",".join(sorted({"%s@%s" % (r["block_trace_value"],
                                              r["the_measure"])
                                   for r in wil["rows"]})),
                  wil["range_over_the_invariant_simplex"]["minimum"],
                  wil["range_over_the_invariant_simplex"]["maximum"],
                  wil["loop_families_grown"]))
    seg.append("SCOPE=D=%d;L=%d;FIELD=%s;COINS=%d;LINKS=%d;PLAQUETTES=%d;"
               "CARRIER=THE-PARENTS-PRIMARY-CARRIER-THE-%d-UNIFORM-"
               "CONFIGURATIONS(PLUS-THE-EXTENSIONS-%d-STATE-CLOSURE-WHERE-"
               "THE-EXTENSION-IS-DECLARED);FULL-CONFIGURATION-SPACE=%s-NOT-A-"
               "CARRIER-HERE;ELIMINATION-CAP=%d-EVERY-EXACT-SOLVE-AT-OR-"
               "BELOW-IT;LOCALITY-IS-DEGENERATE-ON-THIS-CARRIER-ONE-COIN-"
               "SERVES-ALL-%d-LINKS;THE-DYNAMICS-ARE-DECLARED-NOT-DERIVED;"
               "NO-ACTION;NO-COUPLING;NOT-QCD;NO-CONFINEMENT-CLAIM"
               % (ar["d"], ar["L"], ar["field"], ar["coins"], ar["links"],
                  ar["plaquettes"], ar["coins"],
                  ca["CHART-128"]["enlarged_carrier"],
                  ar["configuration_space"].split(",")[0],
                  ELIMINATION_CAP, ar["links"]))
    return head + "-<" + " -- ".join(seg) + ">"


def reconstruct_verdict(S):
    """the INDEPENDENT comparator: it reads only the serialized receipt, it
    re-derives the head by the second head law, and it re-renders every
    segment from the primitive measured tables -- reading neither the
    builder's segments nor the builder's counts, and sharing no format
    string and no helper with the builder."""
    payload = json.loads(json.dumps(
        {k: v for k, v in S.items() if not k.startswith("_")},
        default=str))
    ins = payload["census"]["instances"]
    ix = dict((r["instance"], r) for r in ins)
    der = [r for r in ins if r["verdict"] == "DERIVES"]
    red = [r for r in ins if r["verdict"] != "DERIVES"]
    fams = sorted(set(r["family"] for r in ins))
    rel = payload["relativity"]
    sur = payload["surjection"]
    wil = payload["wilson"]
    ar = payload["arena"]
    ca = payload["chart_action"]
    lr = payload["law_refinement"]
    comp = payload["composition"]

    agree = rel["all_deriving_instances_agree"]
    widest = Fraction(rel["widest_spread"])
    head = second_head_law(ins, agree, widest, None, rel)

    parts = []
    parts.append("CENSUS=" + str(len(fams)) + "-FAMILIES-" + str(len(ins))
                 + "-INSTANCES-ALL-RUN-" + str(len(der)) + "-DERIVE-"
                 + str(len(red)) + "-REDUCIBLE|CRITERION=" + lr["sharp"]
                 + "|THE-INHERITED-FORM-IS-SUFFICIENT-NOT-NECESSARY-"
                 "WITNESS-AT-" + str(lr["witness_states"]) + "-STATES-"
                 + str(lr["witness_communicating_classes"]) + "-CLASSES-"
                 + str(lr["witness_closed_classes"]) + "-CLOSED")
    a1, a2 = ix["CHART-32"], ix["CHART-128"]
    parts.append("(a)CHART-WALK=THE-ANCHORED-CHART-ACTS-TRIVIALLY-"
                 + str(a1["induced_identity"]) + "-OF-"
                 + str(ca["CHART-32"]["order"])
                 + "-ELEMENTS-INDUCE-THE-IDENTITY-SO-"
                 + str(a1["closed_classes"]) + "-CLOSED-CLASSES-AND-THE-"
                 "WHOLE-" + str(a1["simplex_dimension"])
                 + "-SIMPLEX-IS-STATIONARY;THE-EXTENSION-DOES-NOT-ACT-ON-"
                 "THIS-CARRIER-AT-ALL-"
                 + str(ca["CHART-128"]["mixed_reversal"]) + "-OF-"
                 + str(ca["CHART-128"]["order"])
                 + "-ELEMENTS-CARRY-A-UNIFORM-CONFIGURATION-OFF-IT-AND-ITS-"
                 "CLOSURE-IS-" + str(ca["CHART-128"]["enlarged_carrier"])
                 + "-STATES-WITH-" + str(a2["closed_classes"])
                 + "-CLOSED-CLASSES")
    b1, b2 = ix["GAUGE-CHART-32"], ix["GAUGE-CHART-128"]
    parts.append("(b)GAUGE-WALK=REDUCIBLE-AT-BOTH-READINGS-"
                 + str(b1["closed_classes"]) + "-AND-"
                 + str(b2["closed_classes"])
                 + "-CLOSED-CLASSES-IDENTICAL-AS-SETS-TO-THE-PARENTS-ORBITS-"
                 "AND-ITS-STATIONARY-SIMPLEX-IS-THE-PARENTS-INVARIANT-"
                 "SIMPLEX-DIMENSION-" + str(b1["simplex_dimension"]) + "-AND-"
                 + str(b2["simplex_dimension"]))
    lawi = [r for r in ins if r["family"].startswith("(c)")]
    pr = payload["privilege"]
    parts.append("(c)LAW-NATIVE-RESAMPLING=IRREDUCIBLE-AND-DERIVES-AT-ALL-"
                 + str(len(lawi)) + "-MEMBERS-OF-ITS-DECLARED-FIBRE;THE-"
                 "MEASURE-IS-" + lawi[0]["measure_name"] + "-SECTOR-GRADED-"
                 "AT-" + "-".join(payload["law_native_rates"]["values"])
                 + "-AND-INVARIANT-SO-IT-IS-A-POINT-OF-THE-PARENTS-SIMPLEX;"
                 "BUT-ITS-KERNEL-IS-RANK-ONE-EVERY-ROW-OF-THE-LAW-IS-THE-"
                 "SAME-VECTOR-AT-" + str(pr["instances_whose_stationary_"
                                            "measure_is_the_declared_draw_"
                                            "law"])
                 + "-OF-" + str(pr["instances"]) + "-INSTANCES-SO-THE-"
                 "DERIVED-MEASURE-IS-THE-DECLARED-DRAW-LAW-READ-BACK-AND-"
                 "THE-ROW-IS-STAMPED-" + pr["stamp"])
    parts.append("(d)COMPOSITION-WALK=IRREDUCIBLE-ON-BOTH-SIDES-AND-DERIVES-"
                 "THE-COUNTING-MEASURE-BECAUSE-THE-FAMILY-IS-CLOSED-UNDER-"
                 "INVERSE-" + str(comp["inverse_closed"]) + "-OF-"
                 + str(ar["coins"]) + "-SO-THE-WALK-IS-DOUBLY-STOCHASTIC-"
                 "WITH-" + str(comp["products_inside"]) + "-OF-"
                 + str(comp["products_total"]) + "-PRODUCTS-STAYING")
    parts.append("(e)MONOMIAL-HAAR-WALK=REDUCIBLE-"
                 + str(ix["MONOMIAL-LEFT"]["closed_classes"])
                 + "-CLOSED-CLASSES-OF-" + str(comp["monomial_coins"])
                 + "-AND-ONE-OF-THEM-IS-EXACTLY-THE-PARENTS-HAAR-CARRIER-SO-"
                 "THE-CORPUS-ONE-HANDED-OVER-MEASURE-IS-ONE-EXTREME-POINT-"
                 "HERE")
    reached = sum(1 for h in sur["targets_reached"]
                  if h["stationary_equals_the_target"] in (True, "True"))
    parts.append("(f)COVARIANT-METROPOLIS=EVERY-DECLARED-INVARIANT-TARGET-IS-"
                 "REACHED-EXACTLY-" + str(reached) + "-OF-"
                 + str(len(sur["targets_reached"]))
                 + "-AND-THE-NON-INVARIANT-CONTROL-LANDS-OUTSIDE-THE-SIMPLEX-"
                 "ORBIT-CONSTANT="
                 + str(sur["non_invariant_control_is_orbit_constant"]).upper()
                 + ";EXHAUSTIVE-ARM-"
                 + str(sur["exhaustive_small_carrier_targets"]) + "-TARGETS-"
                 + str(sur["exhaustive_small_carrier_failures"])
                 + "-FAILURES")
    seen = []
    for r in der:
        v = r["measure_name"]
        if v != "NEW" and v not in seen:
            seen.append(v)
    parts.append("MEASURES=" + str(payload["census"][
        "distinct_stationary_vectors"]) + "-DISTINCT-STATIONARY-VECTORS-OVER-"
        + str(len(der)) + "-DERIVING-INSTANCES|NAMED-NULLS-REACHED="
        + (",".join(sorted(seen)) if seen else "NONE") + "|NEW="
        + str(sum(1 for r in der if r["measure_name"] == "NEW")))
    parts.append("RELATIVITY=THE-MEASURE-MOVES|WIDEST-SPREAD-OVER-THE-"
                 + str(rel["gauge_covariant_deriving_instances"])
                 + "-GAUGE-COVARIANT-DERIVING-INSTANCES="
                 + rel["widest_spread"]
                 + "-ATTAINED-ON-" + str(len(rel["widest_attained_on"]))
                 + "-OF-" + str(len(rel["rows"])) + "-SETS("
                 + ",".join(rel["widest_attained_on"])
                 + ")|OVER-ALL-" + str(rel["deriving_instances"])
                 + "-DERIVING-INSTANCES-THE-DECLARED-NON-COVARIANT-CONTROL-"
                 "INCLUDED=" + rel["widest_spread_over_every_deriving_instance"]
                 + "|AT-THE-PARENTS-OWN-THREE-MEASURES-ALL-"
                 + rel["parent_measures_contained_in_this_census"].upper(
                 ).replace(" ", "-")
                 + "-PRESENT-HERE-THIS-CENSUS-REPRODUCES-"
                 + rel["this_census_restricted_to_the_parents_own_three_"
                       "measures"]
                 + "-EXACTLY|THE-RISE-TO-" + rel["widest_spread"] + "-IS-THE-"
                 + str(rel["new_law_native_measures_entering_the_comparison"])
                 + "-NEW-LAW-NATIVE-MEASURES-ENTERING-THE-SAME-COMPARISON-"
                 "NOT-A-DYNAMICS-EFFECT|OVER-THE-WHOLE-COVARIANT-FIBRE-THE-"
                 "RANGE-OF-EVERY-HEADLINE-SET-IS-"
                 + rel["headline_set_range_over_the_invariant_simplex"][0][
                     "reachable_range_over_the_invariant_simplex"]
                 + "-BY-THE-SURJECTION"
                 + "|QUASI-DERIVATION-ARM-REACHABLE-AND-MEASURED-TO-FAIL")
    en = payload["enumeration_sensitivity"]
    parts.append("ENUMERATION=THE-CONTROLS-TARGET-IS-DECLARED-ON-CONTIGUOUS-"
                 "BLOCKS-OF-THE-COIN-INDEX-SO-ITS-TWO-NUMBERS-ARE-"
                 "ENUMERATION-RELATIVE:UNDER-A-SECOND-ADMISSIBLE-READING-OF-"
                 "THE-PARENTS-ALPHABET-THE-CONTROL-EXPECTATION-IS-"
                 + en["control_expectation_alternative"] + "-NOT-"
                 + en["control_expectation_delivered"]
                 + "-AND-THE-SPREAD-OVER-ALL-DERIVING-INSTANCES-IS-"
                 + en["widest_spread_over_every_deriving_instance_"
                      "alternative"] + "-NOT-"
                 + en["widest_spread_over_every_deriving_instance_delivered"]
                 + "|THE-LIKE-FOR-LIKE-HEADLINE-"
                 + en["widest_spread_over_the_covariant_deriving_instances"]
                 + "-IS-IDENTICAL-UNDER-BOTH-ENUMERATIONS-BECAUSE-THE-"
                 "COVARIANT-MEASURES-ARE-FUNCTIONS-OF-SECTOR-AND-ORBIT-"
                 "MEMBERSHIP-ALONE")
    cs = sur["closed_simplex"]
    parts.append("PRICE=CONSERVED-NOT-PAID:THE-COVARIANT-DYNAMICS-FIBRE-"
                 "SURJECTS-ONTO-THE-CLOSED-INVARIANT-SIMPLEX-BOUNDARY-"
                 "INCLUDED-" + str(cs["small_carrier_reached_exactly"])
                 + "-OF-" + str(cs["small_carrier_boundary_targets"])
                 + "-BOUNDARY-TARGETS-AT-THE-DECLARED-SMALL-CARRIERS-AND-"
                 + str(sum(1 for b in cs["at_the_arena"]
                           if b["stationary_equals_the_target"]
                           in (True, "True")))
                 + "-OF-" + str(len(cs["at_the_arena"]))
                 + "-AT-THE-ARENA-SO-A-DECLARATION-STILL-SUPPLIES-"
                 + str(sur["price_chart_32"])
                 + "-INDEPENDENT-NUMBERS-AT-THE-ANCHORED-READING-AND-"
                 + str(sur["price_chart_128"])
                 + "-AT-THE-EXTENSION-READING-MEASURED-HERE-UNDER-THE-ORDER-"
                 "8-GROUP-EXACTLY-THE-PARENTS-COUNTS|DROPPED-COVARIANCE-THE-"
                 "SAME-MOVE-COSTS-" + str(sur["dropped_covariance"][
                     "price_without_the_covariance_declaration"])
                 + "|WHAT-MOVED-IS-WHERE-THE-DECLARATION-IS-MADE-NOT-HOW-"
                 "MUCH-IT-COSTS")
    vals = set()
    for r in wil["rows"]:
        vals.add(r["block_trace_value"] + "@" + r["the_measure"])
    vals = sorted(vals)
    parts.append("WILSON=LICENSED-BY-THE-PIN-AND-STAMPED-" + STAMP + "-AT-"
                 + str(len(wil["rows"])) + "-OF-" + str(len(wil["rows"]))
                 + "-ROWS|OBSERVABLE=" + wil["observable"]
                 + "-PLAQUETTE-INDEPENDENT-AT-"
                 + str(wil["plaquettes_checked"])
                 + "-PLAQUETTES-AND-GAUGE-INVARIANT|VALUES="
                 + ",".join(vals) + "|RANGE-OVER-THE-INVARIANT-SIMPLEX=["
                 + wil["range_over_the_invariant_simplex"]["minimum"] + ","
                 + wil["range_over_the_invariant_simplex"]["maximum"]
                 + "]-BOTH-ENDPOINTS-ATTAINED-AT-EXTREME-POINTS-SO-"
                 "COVARIANCE-PINS-THE-EXPECTATION-NOWHERE|NO-AREA-LAW-NO-"
                 "STRING-TENSION-NO-POTENTIAL-CLAIM-AND-"
                 + str(wil["loop_families_grown"]) + "-LOOP-FAMILIES-GROWN")
    parts.append("SCOPE=D=" + str(ar["d"]) + ";L=" + str(ar["L"]) + ";FIELD="
                 + ar["field"] + ";COINS=" + str(ar["coins"]) + ";LINKS="
                 + str(ar["links"]) + ";PLAQUETTES=" + str(ar["plaquettes"])
                 + ";CARRIER=THE-PARENTS-PRIMARY-CARRIER-THE-"
                 + str(ar["coins"]) + "-UNIFORM-CONFIGURATIONS(PLUS-THE-"
                 "EXTENSIONS-" + str(ca["CHART-128"]["enlarged_carrier"])
                 + "-STATE-CLOSURE-WHERE-THE-EXTENSION-IS-DECLARED);FULL-"
                 "CONFIGURATION-SPACE=" + ar["configuration_space"].split(
                     ",")[0] + "-NOT-A-CARRIER-HERE;ELIMINATION-CAP="
                 + str(ELIMINATION_CAP) + "-EVERY-EXACT-SOLVE-AT-OR-BELOW-IT;"
                 "LOCALITY-IS-DEGENERATE-ON-THIS-CARRIER-ONE-COIN-SERVES-"
                 "ALL-" + str(ar["links"]) + "-LINKS;THE-DYNAMICS-ARE-"
                 "DECLARED-NOT-DERIVED;NO-ACTION;NO-COUPLING;NOT-QCD;NO-"
                 "CONFINEMENT-CLAIM")
    return head + "-<" + " -- ".join(parts) + ">"


def summarise_census(S, published, agree, widest):
    der = [r for r in published if r["verdict"] == "DERIVES"]
    red = [r for r in published if r["verdict"] == "REDUCIBLE"]
    vecs = {tuple(S["_pi"][r["instance"]]) for r in der}
    named = []
    for r in der:
        if r["measure_name"] != "NEW" and r["measure_name"] not in named:
            named.append(r["measure_name"])
    lawi = [r for r in der if r["family"].startswith("(c)")]
    S["census"] = {
        "families": len({r["family"] for r in published}),
        "instances_run": len(published),
        "derive": len(der), "reducible": len(red),
        "irreducible": sum(1 for r in published if r["irreducible"]),
        "transient_classes_total": sum(r["transient_classes"]
                                       for r in published),
        "distinct_stationary_vectors": len(vecs),
        "named_measures_reached": sorted(named),
        "new_measures": sum(1 for r in der if r["measure_name"] == "NEW"),
        "law_native_instances": len(lawi),
        "law_native_measure_name": lawi[0]["measure_name"] if lawi else "NONE",
        "instances": published,
        "head": head_law(published, agree, widest, None, S["relativity"]),
    }
    h2 = second_head_law(published, agree, widest, None, S["relativity"])
    if mut("MUT-HEAD"):
        S["census"]["head"] = "SMU-DERIVED-EVERYTHING"
    LD.gate("G-HEAD-DERIVED-TWICE",
            "the head is derived TWICE, by two laws: the builder computes it "
            "from the live census, and an independent reconstruction written "
            "from the same pre-registered outcomes with a different branch "
            "structure and no shared format string returns the same string "
            "-- so a head typed rather than computed, or computed by a law "
            "that had drifted from its own measurements, dies here",
            S["census"]["head"] == h2,
            "builder %r; second law %r" % (S["census"]["head"], h2))
    SEAL.take("THE CENSUS", "census", "G-HEAD-DERIVED-TWICE", S["census"])


# ===========================================================================
# SECTION 12.  THE PAPER GATES
# ===========================================================================

# THE PIN'S MUST-NOT, INHERITED VERBATIM FROM PAPER-23's REPAIRED GATE.  The
# confinement vocabulary is barred outright; the pin's own words, the bare
# ones included.  What is NOT on this list -- wilson, expectation, loop
# average -- is what the pin licenses here and paper-23 withheld, and it is
# gated on the product instead, per row, in G-WILSON-LICENCE.
# receipt keys whose values are DIGESTS -- identifiers, not values this run
# computed.  Their digits do not license a paper numeral; the digests
# themselves are bound as rendered claims instead.
DIGEST_KEYS = {"pinned", "measured", "digest", "code_sha256_12",
               "paper_sha256_12", "pin_sha256_prefix"}

# and one whole published object is excluded for the same reason: the
# falsifier registry DESCRIBES this instrument -- it publishes the exact
# source token each mutant plants -- so harvesting it would let a falsifier
# license the very numeral it plants, and the coverage gate would forgive a
# corruption because the corruption was declared.  Measured: without this
# exclusion MUT-COVERAGE survives.
POOL_EXCLUDED = {"mutants"}

MUST_NOT = [
    "area law", "area-law", "the law of the area",
    "string tension", "string-tension",
    "confining", "confinement", "quark", "potential",
]
# the declaring sentences the sweep may remove.  The list is EXACTLY the
# sentences this paper contains -- an exemption inherited from a parent and
# never used here is a latent hole, so the gate requires every entry to be
# located and the eight inherited-but-inert entries were dropped rather than
# carried.
DECLARING = [
    "no area-law, string-tension, or potential claim",
    "NO-AREA-LAW-NO-STRING-TENSION-NO-POTENTIAL-CLAIM",
    "NO-CONFINEMENT-CLAIM",
    "grows no loop family and makes no claim about how any expectation "
    "would behave as a loop grows",
]


def build_claims(S):
    """the paper's load-bearing sentences, RENDERED FROM THE RECEIPT, each
    with the number of times it must occur.  A claim is gated at its
    occurrence count, so a number corrupted at one of its several
    occurrences dies (#20)."""
    cen, rel = S["census"], S["relativity"]
    sur, wil = S["surjection"], S["wilson"]
    ar, ca, comp = S["arena"], S["chart_action"], S["composition"]
    ix = {r["instance"]: r for r in cen["instances"]}
    fib = S["fibre"]
    c = []
    c.append(("%d families and %d declared instances" %
              (cen["families"], cen["instances_run"]), 1))
    c.append(("%d of them derive and %d are reducible" %
              (cen["derive"], cen["reducible"]), 1))
    c.append(("%d of %d extension elements carry a uniform configuration off "
              "the carrier" % (ca["CHART-128"]["mixed_reversal"],
                               ca["CHART-128"]["order"]), 1))
    c.append(("closure is %d states, and on it the walk has %d closed "
              "classes" % (ca["CHART-128"]["enlarged_carrier"],
                           ix["CHART-128"]["closed_classes"]), 1))
    c.append(("%d sites, %d links and %d plaquettes"
              % (ar["sites"], ar["links"], ar["plaquettes"]), 1))
    c.append(("%d closed classes" % ix["CHART-32"]["closed_classes"], 1))
    c.append(("%d and %d closed classes" %
              (ix["GAUGE-CHART-32"]["closed_classes"],
               ix["GAUGE-CHART-128"]["closed_classes"]), 1))
    c.append(("dimension %d at the anchored reading and %d at the extension" %
              (ix["GAUGE-CHART-32"]["simplex_dimension"],
               ix["GAUGE-CHART-128"]["simplex_dimension"]), 1))
    c.append(("%d of %d products stay inside the family" %
              (comp["products_inside"], comp["products_total"]), 1))
    c.append(("closed under inverse at %d of %d" %
              (comp["inverse_closed"], ar["coins"]), 1))
    c.append(("%d closed classes of %d" %
              (ix["MONOMIAL-LEFT"]["closed_classes"],
               comp["monomial_coins"]), 1))
    c.append(("widest spread over the %d gauge-covariant deriving "
              "instances is %s"
              % (rel["gauge_covariant_deriving_instances"],
                 rel["widest_spread"]), 1))
    c.append(("over all %d deriving instances it is %s"
              % (rel["deriving_instances"],
                 rel["widest_spread_over_every_deriving_instance"]), 1))
    c.append(("the parent's widest spread over its own three named nulls "
              "was %s"
              % rel["parent_widest_spread_over_its_own_three_named_nulls"],
              1))
    c.append(("%d targets at a declared denominator, %d failures" %
              (sur["exhaustive_small_carrier_targets"],
               sur["exhaustive_small_carrier_failures"]), 1))
    c.append(("%d independent numbers at the anchored reading and %d at the "
              "extension" % (fib["price_of_a_covariant_declaration_chart_32"],
                             fib["price_of_a_covariant_declaration_chart_128"]),
              1))
    c.append(("range of the expectation over the invariant simplex is "
              "exactly [%s, %s]" %
              (wil["range_over_the_invariant_simplex"]["minimum"],
               wil["range_over_the_invariant_simplex"]["maximum"]), 1))
    c.append(("%d loop families are grown" % wil["loop_families_grown"], 1))
    ls = S["ledger_shape"]
    c.append(("%d gates close before the paper gates, %d of them binding one "
              "declared instance each, and %d paper gates and %d closing "
              "gates follow"
              % (ls["gates_closed_before_the_paper_gates"],
                 ls["instance_gates"], ls["paper_gates"],
                 ls["closing_gates"]), 1))
    c.append(("%d objects are sealed before the paper gates"
              % ls["objects_sealed_before_the_paper_gates"], 1))
    c.append(("%d construction choices are inventoried, of which %d are "
              "measured verdict-determining"
              % (len(S["fibre"]["rows"]),
                 sum(1 for r in S["fibre"]["rows"]
                     if r.get("verdict_determining") is True)), 1))
    wl = S["waiver_ledger"]
    c.append(("%d are the declared targets of falsifiers, %d are the "
              "per-instance gates under one registered forcing, and %d are "
              "uncovered" % (wl["covered_by_a_declared_falsifier"],
                             wl["per_instance_gates_under_the_registered_"
                                "forcing"], len(wl["uncovered"])), 1))
    for r in wil["rows"]:
        c.append(("%s under %s" % (r["block_trace_value"],
                                   r["declared_dynamics"]), 1))

    # ---- the repaired numbers, each bound where the paper states it
    c.append(("restricted to those same three the widest spread is %s"
              % rel["this_census_restricted_to_the_parents_own_three_"
                    "measures"], 1))
    c.append(("all %s of the parent's compared measures are in this census"
              % rel["parent_measures_contained_in_this_census"], 1))
    cs = sur["closed_simplex"]
    c.append(("%d boundary targets, %d reached exactly, %d with exactly one "
              "closed class, %d irreducible"
              % (cs["small_carrier_boundary_targets"],
                 cs["small_carrier_reached_exactly"],
                 cs["small_carrier_with_exactly_one_closed_class"],
                 cs["small_carrier_irreducible"]), 1))
    c.append(("%d of %d at the arena"
              % (sum(1 for b in cs["at_the_arena"]
                     if b["stationary_equals_the_target"]),
                 len(cs["at_the_arena"])), 1))
    c.append(("costs %d numbers instead of %d"
              % (sur["dropped_covariance"][
                  "price_without_the_covariance_declaration"],
                 sur["dropped_covariance"][
                     "price_with_the_covariance_declaration"]), 1))
    pri = S["privilege"]
    c.append(("every row of the transition law is the same vector at %d of "
              "%d instances"
              % (pri["instances_whose_stationary_measure_is_the_declared_"
                     "draw_law"], pri["instances"]), 1))
    exc = S["extension_covariance"]
    c.append(("%d covariant deriving instances under the order-4 group and "
              "%d under the order-8 group"
              % (exc["covariant_deriving_under_the_order_4_group"],
                 exc["covariant_deriving_under_the_order_8_group"]), 1))
    en = S["enumeration_sensitivity"]
    c.append(("the expectation is %s rather than %s and the spread over all "
              "deriving instances is %s rather than %s"
              % (en["control_expectation_alternative"],
                 en["control_expectation_delivered"],
                 en["widest_spread_over_every_deriving_instance_alternative"],
                 en["widest_spread_over_every_deriving_instance_delivered"]),
              1))
    dt = S["dimension_theorem"]
    c.append(("%d chains enumerated exhaustively over the %d-state and "
              "%d-state layers" % (dt["chains_enumerated"],
                                   dt["carrier_states"][0],
                                   dt["carrier_states"][1]), 1))

    # ---- THE PROVENANCE DIGESTS, bound as claims rather than licensed as
    # numeral fragments (E-22's spirit: an identifier is a claim too)
    # each digest is bound to ITS OWN PATH and not merely to its existence:
    # two digests exchanged between two sources leave both occurrence counts
    # at one, so an existence claim cannot see the exchange.  Measured: the
    # (path, digest) form kills it and the bare form does not.
    for _nm, rel_path, sha, _what in SOURCES:
        if sha == PIN_SHA12:
            c.append(("`%s` (sha256-12 `%s`)" % (rel_path, sha), 1))
        else:
            c.append(("`%s` (`%s`)" % (rel_path, sha), 1))

    # ---- THE DELIVERED TABLES, RENDERED AS CLAIMS (E-22)
    # section 1: the pre-registered outcomes
    c.append(("`SMU-DERIVED` | a census in which every deriving instance "
              "carried the same vector, with the reducible ones absent | not "
              "the case: the deriving instances carry %d distinct stationary "
              "vectors" % cen["distinct_stationary_vectors"], 1))
    c.append(("`SMU-QUASI-DERIVED` | all deriving instances agree — "
              "decided by comparing their vectors entry by entry, not "
              "inferred | the vectors are compared and disagree", 1))
    c.append(("`SMU-REDUCIBLE` | no declared dynamics has a single closed "
              "class | %d do" % cen["derive"], 1))
    c.append(("`SMU-DYNAMICS-RELATIVE` | the deriving instances disagree and "
              "the spread is positive | **this is what is measured**", 1))
    c.append(("`SMU-BLOCKED-AT` | an object that cannot be evaluated at all "
              "| every declared instance is evaluable and is evaluated", 1))
    # section 4: the census table, every cell from the receipt
    fam_order = []
    for r in cen["instances"]:
        if r["family"] not in fam_order:
            fam_order.append(r["family"])
    for fam in fam_order:
        mem = [r for r in cen["instances"] if r["family"] == fam]
        tag, name = fam.split(" ", 1)
        fibv = mem[0]["fibre"]
        fibc = (str(fibv) if isinstance(fibv, int)
                else fibv.lower().replace("-", " "))
        cols = []
        for key in ("irreducible", "closed_classes"):
            seq = []
            for r in mem:
                v = ("yes" if r[key] else "no") if key == "irreducible" \
                    else str(r[key])
                if not seq or seq[-1] != v:
                    seq.append(v)
            cols.append(" / ".join(seq))
        c.append(("%s | %s | %s | %s | %s | %s"
                  % (tag, name.lower(),
                     mem[0]["fibre_axis"].lower().replace("-", " "), fibc,
                     cols[0], cols[1]), 1))
    # section 6: the dynamics-relativity table, every cell from the receipt
    for r in rel["rows"]:
        cells = [r["set"], str(r["configurations_COUNTING_ONLY"])]
        for k in RELATIVITY_COLUMNS:
            cells.append(r["mass_by_declared_dynamics"][k])
        c.append((" | ".join(cells), 1))
    return c


# the four columns of the section-6 table, named by the declared instance
# whose stationary measure produces each one
RELATIVITY_COLUMNS = ["COMPOSITION-LEFT", "LAW-NATIVE-012",
                      "METROPOLIS-AT-ORBIT-UNIFORM-CHART-32",
                      "METROPOLIS-AT-ORBIT-UNIFORM-CHART-128"]

POLARITY = [
    ("the stationary measure MOVES across the declared-dynamics fibre", 1),
    ("the extension does not act on this carrier", 1),
    ("the price is conserved, not paid", 1),
    ("the inherited form is sufficient and not necessary", 1),
]


def verify_paper(S, paper_text):
    """the paper gates, run IN the plain delivery run (#20): claim rendering
    at occurrence counts, the complete verdict string by equality with the
    fenced blocks compared as a MULTISET (E-22), the inherited must-not
    sweep, claim polarity, and numeral coverage over EVERY numeral including
    fenced blocks, inline code spans and both sides of every fraction."""
    LDx = LD
    claims = build_claims(S)
    ptext = paper_text
    if mut("MUT-CLAIM"):
        ptext = ptext.replace("%d of them derive" % S["census"]["derive"],
                              "11 of them derive", 1)
    if mut("MUT-TABLE-ROW"):
        a = re.search(r"^(\|\s*NON-COMMUTING\s*\|)(.*)$", ptext, re.M)
        b = re.search(r"^(\|\s*DEFECT-CARRYING\s*\|)(.*)$", ptext, re.M)
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
    LDx.gate("G-PAPER-CLAIMS",
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
        blocks = blocks + [wsnorm(verdict).replace("SMU-", "XMU-")]
    LDx.gate("G-PAPER-VERDICT-EQUALITY",
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
    LDx.gate("G-MUST-NOT-VOCABULARY",
            "the pin's must-not vocabulary -- inherited VERBATIM from "
            "paper-23's repaired gate, the bare words included -- is swept "
            "over this paper's own text with the declaring sentences removed "
            "first and inline emphasis stripped, so a claim under asterisks "
            "is still the same claim and a paragraph that made an area-law, "
            "string-tension or potential claim would die on the delivery "
            "run.  Every declaring sentence the sweep is allowed to remove "
            "must itself be LOCATED in this paper: an exemption carried from "
            "a parent and never used is a latent hole, so the declaring list "
            "is required to be exactly the sentences this text contains",
            not hits and not inert,
            "must-not vocabulary found: %s; %d declaring sentences, %d of "
            "them not located in this paper: %s"
            % (hits, len(DECLARING), len(inert), inert[:3]))

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
            bad = any(g in win for g in ("it is false that", "contrary to",
                                         "does not follow that"))
        pol.append({"fragment": frag, "expected": want, "found": nfound,
                    "negated": bad, "ok": nfound == want and not bad})
    S["paper_polarity"] = pol
    LDx.gate("G-PAPER-POLARITY",
            "the direction-bearing claims are checked for POLARITY as well "
            "as presence -- each must occur and must not sit inside a window "
            "carrying a declared negator -- which closes the "
            "direction-blindness of a fragment gate",
            all(p["ok"] for p in pol),
            "%d polarity rows, %d failing"
            % (len(pol), sum(1 for p in pol if not p["ok"])))
    SEAL.take("THE PAPER POLARITY", "paper_polarity", "G-PAPER-POLARITY",
              S["paper_polarity"])

    # ---- E-22 at full strength: TABLES AND QUOTATIONS ARE BOUND.  The
    # instrument's grip on its own prose was 33 rendered sentences and nil
    # over three tables and twelve quotations; both are closed here.
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
    claim_texts = [mnorm(f) for f, _w in claims]
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
    LDx.gate("G-PAPER-TABLES-AND-QUOTES-ARE-BOUND",
            "E-22's 'tables render as claims' is enforced structurally, so a "
            "table added later cannot arrive unbound: every DATA row of "
            "every delivered table that carries a numeral must be covered by "
            "a claim rendered from the receipt, and every BLOCKQUOTE in this "
            "paper must lie inside one of the pinned verbatim windows -- so "
            "a paper that misquotes, or inverts, a parent's own definition "
            "dies here even though the anchor on the parent's bytes passes.  "
            "Header rows are the declared exception and are counted and "
            "published rather than silently skipped",
            not unbound_rows and not unbound_quotes,
            "%d table data rows carrying a numeral, %d unbound %s; %d header "
            "rows excluded; %d blockquotes, %d not located inside a pinned "
            "verbatim window %s"
            % (len(trows), len(unbound_rows), unbound_rows[:2], len(theads),
               len(quotes), len(unbound_quotes), unbound_quotes[:2]))
    S["paper_binding"] = {
        "table_data_rows_carrying_a_numeral": len(trows),
        "table_rows_unbound": len(unbound_rows),
        "table_header_rows_excluded": len(theads),
        "blockquotes": len(quotes),
        "blockquotes_outside_a_pinned_verbatim_window": len(unbound_quotes),
        "verbatim_windows_available": len(VERBATIM),
    }
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
    # the ONLY literals the coverage gate may forgive: this paper's own
    # SECTION NUMBERS.  The engraving references are forgiven only in their
    # parenthesised (#NNN) / (E-NN) form, which is removed from the scan
    # rather than whitelisted as a bare numeral -- so a delivered number that
    # happens to equal an engraving reference is still gated (119 is the
    # extension's price as well as the seal engraving).  The pinned digests
    # are removed from the scan too, because they are bound as CLAIMS above
    # and are identifiers rather than values this run computed; their digits
    # are correspondingly excluded from the licensing pool.
    STRUCTURAL = ({str(k) for k in range(1, 13)}
                  | {"%d.%d" % (a, b) for a in range(1, 13)
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
    LDx.gate("G-PAPER-NUMERAL-COVERAGE",
            "EVERY numeral of the paper is matched against a value this run "
            "computed -- fenced blocks, verdict block, inline code spans and "
            "both sides of every fraction included (E-22, #20) -- with only "
            "a published list of structural literals forgiven, so a number "
            "invented in prose, or moved from one claim to another, dies "
            "inside the delivery run",
            not unmatched, "%d numerals scanned, %d inline code spans "
            "carrying a numeral, %d fence markers, %d unmatched: %s"
            % (len(nums), spans, fenced, len(unmatched), unmatched[:8]))
    S["paper_coverage"] = {"numerals_scanned": len(nums),
                           "inline_spans_with_a_numeral": spans,
                           "fence_markers": fenced,
                           "unmatched": len(unmatched),
                           "removed_from_the_scan_and_bound_as_claims":
                               "THE-PARENTHESISED-ENGRAVING-REFERENCES-AND-"
                               "THE-BACKTICKED-TWELVE-HEX-DIGESTS",
                           "digest_valued_keys_excluded_from_the_pool":
                               sorted(DIGEST_KEYS),
                           "published_objects_excluded_from_the_pool":
                               sorted(POOL_EXCLUDED),
                           "structural_literals_forgiven":
                               sorted(STRUCTURAL)}
    SEAL.take("THE PAPER COVERAGE", "paper_coverage",
              "G-PAPER-NUMERAL-COVERAGE", S["paper_coverage"])


# ===========================================================================
# SECTION 13.  THE MUTANT REGISTRY, TOTAL AND HONESTLY DESCRIBED (E-23)
# ===========================================================================

MUTANTS = [
    ("MUT-SOURCE-DRIFT", "G-SOURCE-BYTES",
     "replaces one pinned source's measured digest with zeros",
     '"000000000000"'),
    ("MUT-AST-BLIND", "G-EXACT-ARITHMETIC-BY-AST",
     "plants a real float literal into the source text the AST gate parses",
     "_TOLERANCE_FLOAT = 1e-9"),
    ("MUT-PATH-VALUE", "G-PATH-VALUE-ANCHORS",
     "moves one inherited path-value to 999", "got = 999"),
    ("MUT-VERBATIM", "G-VERBATIM-ANCHORS",
     "perturbs one verbatim window's own text so it stops locating in "
     "the parent's pinned bytes", '"reducibility"'),
    ("MUT-ARENA", "G-ARENA-REBUILT",
     "drops one coin from the rebuilt family", "coins = coins[:-1]"),
    ("MUT-CHART-ACTION", "G-CHART-ACTION-MEASURED",
     "declares the extension to act on the carrier when it does not",
     '"acts_on_the_carrier"'),
    ("MUT-GAUGE-ORBITS", "G-GAUGE-GROUP-REBUILT",
     "drops one gauge orbit", "O4 = O4[:-1]"),
    ("MUT-COMPOSITION", "G-COMPOSITION-WALK-BUILT",
     "reports one fewer product staying inside the family",
     "stay = stay - 1"),
    ("MUT-PARENT-SETS", "G-PARENT-SETS-REBUILT",
     "drops one member of the non-flat set", "nonflat = set(sorted"),
    ("MUT-LAW-RATES", "G-LAW-NATIVE-RATE-SOURCE",
     "replaces the law-native rates with a degenerate uniform triple",
     "Fraction(1, 3)"),
    ("MUT-STOCHASTIC", "G-INSTANCE-GAUGE-CHART-32",
     "halves one entry of one instance's transition law, breaking row "
     "stochasticity", "P[0][k] / 2"),
    ("MUT-COVARIANCE", "G-INSTANCE-LAW-NATIVE-012",
     "inverts one instance's measured covariance verdict", "cf = 0 if cf"),
    ("MUT-IRREDUCIBILITY", "G-IRREDUCIBILITY-IS-THE-CRITERION",
     "inverts one deriving instance's irreducibility verdict, so that the "
     "census's deriving count and its irreducible count disagree",
     'rec["irreducible"] = not rec["irreducible"]'),
    ("MUT-GAP-WITNESS", "G-THE-INHERITED-LAW-IS-SUFFICIENT-NOT-NECESSARY",
     "truncates the synthetic witness's class list so the gap is not "
     "exhibited", "comps = comps[:1]"),
    ("MUT-DIMENSION-THEOREM", "G-SIMPLEX-DIMENSION-THEOREM",
     "replaces the first enumerated chain with an identity chain, whose "
     "kernel dimension disagrees with its own closed-class count",
     "P = [{i: Fraction(1)} for i in range(m)]"),
    ("MUT-WELD", "G-GAUGE-WALK-CLASSES-ARE-THE-PARENTS-ORBITS",
     "drops one element from one closed class of the gauge walk before "
     "the set-level comparison with the parent's orbits",
     "c[:-1] if i == 0"),
    ("MUT-MONOMIAL", "G-MONOMIAL-WALK-CARRIES-THE-PARENTS-HAAR",
     "drops one coin from the parent's Haar carrier before the set-level "
     "comparison with the monomial walk's classes",
     "sorted(monoset)[:-1]"),
    ("MUT-ORBIT-CLOSURE", "G-SETS-ARE-UNIONS-OF-ORBITS",
     "declares one re-weighed set not to be a union of orbits",
     '"orbit_closed_chart_32"'),
    ("MUT-SPREAD", "G-RELATIVITY-CENSUS",
     "zeroes the widest measured spread", "widest = Fraction(0)"),
    ("MUT-QUASI", "G-QUASI-DERIVATION-ARM-IS-DECIDED-NOT-ASSUMED",
     "replaces every deriving instance's stationary vector with the "
     "first one's, so the compared table really does agree",
     'pis = {k: S["_pi"][der[0]'),
    ("MUT-SURJECTION", "G-PRICE-IS-CONSERVED",
     "replaces the first enumerated target's chain with the chain at the "
     "uniform target, so that target is not reached",
     "P = metropolis([Fraction(1, 4)] * 4, 4)"),
    ("MUT-WILSON-OBSERVABLE", "G-WILSON-OBSERVABLE-REBUILT",
     "perturbs one configuration's block-trace value, so the observable "
     "stops being plaquette-independent at that configuration",
     "tb[0] = fadd(tb[0], ONE)"),
    ("MUT-WILSON-UNLICENSED", "G-WILSON-LICENCE",
     "publishes an expectation under a REDUCIBLE dynamics",
     '"derives_given_the_declared_dynamics": False'),
    ("MUT-WILSON-UNSTAMPED", "G-WILSON-LICENCE",
     "strips the conditional stamp from one expectation row",
     '"stamp"] = "PLAIN"'),
    ("MUT-FIBRE", "G-FIBRE-INVENTORY",
     "inflates one declared axis's fibre above the instances built",
     'rows[-1]["fibre"] = '),
    ("MUT-HEAD", "G-HEAD-DERIVED-TWICE",
     "types the head instead of computing it", '"SMU-DERIVED-EVERYTHING"'),
    ("MUT-VERDICT-COMPARATOR", "G-VERDICT-RECONSTRUCTION",
     "corrupts the builder's verdict string after it is built",
     "verdict.replace("),
    ("MUT-CLAIM", "G-PAPER-CLAIMS",
     "corrupts a load-bearing count in the paper text the claim gate "
     "scans", '"11 of them derive"'),
    ("MUT-VERDICT-TWIN", "G-PAPER-VERDICT-EQUALITY",
     "adds a forged twin of the verdict fence beside the clean one",
     '"XMU-"'),
    ("MUT-MUST-NOT", "G-MUST-NOT-VOCABULARY",
     "plants an area-law and string-tension sentence into the paper text "
     "the sweep scans", "follows an area law"),
    ("MUT-POLARITY", "G-PAPER-POLARITY",
     "plants a declared negator immediately before a direction-bearing "
     "claim in the scanned text", '"it is false that "'),
    ("MUT-COVERAGE", "G-PAPER-NUMERAL-COVERAGE",
     "plants a numeral into the paper text that no value this run "
     "computed can license", "an uncovered numeral 987654321"),
    ("MUT-GHOST-FUNCTION", "G-FUNCTION-INVENTORY-IS-TOTAL",
     "defines an undeclared function in this instrument's own source text",
     "def ghost_helper"),
    ("MUT-REGISTRY-EVASION", "G-MUTANT-REGISTRY-IS-TOTAL",
     "hides a mutant switch behind a computed name the AST scan cannot read",
     "'MUT-' + 'GHOST'"),
    ("MUT-SEAL", "G-SEAL-INTEGRITY",
     "edits a sealed object after its gate closed", '"MOVED-AFTER-THE-GATE"'),
    ("MUT-CARRIER", "G-CARRIER-IS-THE-PARENTS-PRIMARY-CARRIER",
     "restricts the chart group to its identity element before its "
     "action on the link set is measured, so transitivity fails",
     "if e == ((0, 0), (False, 1, 1))"),
    ("MUT-ENLARGEMENT", "G-CHART-128-ENLARGEMENT",
     "truncates the extension's orbit closure back to the parent's carrier",
     "states = states[:len(coins)]"),
    ("MUT-SIMPLEX-DIM", "G-GAUGE-WALK-SIMPLEX-IS-THE-PARENTS-SIMPLEX",
     "makes two exhibited extreme points share a support, so the "
     "exhibited basis is no longer independent",
     "sup[1] = set(sup[0])"),
    ("MUT-WILSON-GAUGE-INVARIANCE", "G-WILSON-OBSERVABLE-IS-GAUGE-INVARIANT",
     "perturbs one observable value inside a gauge orbit of size greater "
     "than one", "tbg[big4[1]] = fadd("),
    ("MUT-REACHABILITY", "G-HEAD-LAW-REACHABILITY",
     "collapses the head law's synthetic probes to one outcome",
     '"SMU-DYNAMICS-RELATIVE") for w, _g in probes'),
    ("MUT-CENSUS-SHORT", "G-DECLARED-DYNAMICS-CENSUS",
     "drops one declared instance from the census after it ran, so fewer "
     "instances are published than were declared",
     "published = published[:-1]"),
    ("MUT-FALSIFIER-DESCRIPTION", "G-FALSIFIER-DESCRIPTIONS-ARE-HONEST",
     "replaces one falsifier's published planted-token with a token its "
     "branch does not contain", '"a token it never plants"'),
    # ---- the falsifiers the review round bought
    ("MUT-K1-A", "G-HEAD-DERIVED-TWICE",
     "re-plants the twin-template population label in the BUILDER's head law "
     "alone, so the head names the deriving count where the spread it "
     "carries was measured over the covariant one -- the live defect, which "
     "the de-twinned second law now contradicts", "n_cov = len(der)"),
    ("MUT-K1-B", "G-INSTANCE-LAW-NATIVE-012",
     "draws NON-UNIFORMLY inside each sector while leaving the declared "
     "sector law untouched -- an undeclared change to a declared "
     "construction that preserves every sector mass",
     "Fraction(1 + (q % 3), wsum)"),
    ("MUT-CAP", "G-ELIMINATION-CAP-IS-ENFORCED",
     "records one instance's exact solve as larger than the declared "
     "elimination cap", "ELIMINATION_CAP + 1"),
    ("MUT-G8-COVARIANCE", "G-EXTENSION-COVARIANCE-IS-MEASURED-NOT-INHERITED",
     "corrupts one row of the chain whose covariance under the ORDER-8 "
     "residual group is measured", "P8[0] = {0: Fraction(1)}"),
    ("MUT-RANK-ONE", "G-THE-LAW-NATIVE-KERNEL-IS-RANK-ONE",
     "replaces one row of the law-native transition law, so its rows are no "
     "longer the same vector", "rows_of_P[0] = {0: Fraction(1)}"),
    ("MUT-RESTRICTED",
     "G-THE-RESTRICTED-COMPARISON-REPRODUCES-THE-PARENTS-NUMBER",
     "substitutes a law-native vector for one of the parent's own three "
     "measures in the restricted comparison table",
     'rep["COUNTING"] = ("PLANTED"'),
    ("MUT-INDICATOR-RANGE", "G-HEADLINE-SET-RANGE-IS-THE-WHOLE-UNIT-INTERVAL",
     "replaces one witness orbit point mass with the counting measure, so "
     "the set's mass there is no longer the endpoint",
     "w = [Fraction(1, n)] * n"),
    ("MUT-BOUNDARY", "G-THE-SURJECTION-REACHES-THE-CLOSED-SIMPLEX",
     "replaces the first boundary target's chain with the chain at the "
     "uniform target, so the boundary target is not reached",
     "P = metropolis([Fraction(1, m)] * m, m)"),
    ("MUT-DROPPED-COVARIANCE", "G-DROPPED-COVARIANCE-COSTS-THE-WHOLE-SIMPLEX",
     "zeroes one entry of the control's target, so the full-support witness "
     "the corollary needs is no longer full support",
     "ctrl_sup[0] = Fraction(0)"),
    ("MUT-WILSON-RANGE", "G-WILSON-RANGE-IS-MEASURED",
     "enlarges the minimising orbit, so the endpoint is no longer attained "
     "at an extreme point of the simplex",
     "lo = (lo[0], lo[1] + [i for i in range(len(coins))"),
    ("MUT-ENUMERATION", "G-CONTROL-TARGET-ENUMERATION-SENSITIVITY",
     "replaces the alternative alphabet with the delivered one, so the "
     "sensitivity probe is no longer a different enumeration",
     'alt_alph = list(S["_alph"])'),
    ("MUT-LEDGER-SHAPE", "G-LEDGER-SHAPE-IS-CONSISTENT",
     "inflates the published instance-gate count above the rows the ledger "
     "actually carries", 'ls["instance_gates"] = ls["instance_gates"] + 1'),
    ("MUT-TABLE-ROW", "G-PAPER-CLAIMS",
     "exchanges the mass cells of two rows of the delivered section-6 table "
     "in the paper text, leaving both row labels in place",
     "a.group(1) + b.group(2)"),
    ("MUT-QUOTE-FIDELITY", "G-PAPER-TABLES-AND-QUOTES-ARE-BOUND",
     "inverts a parent's own definition inside a blockquote the paper "
     "attributes to it", '"the unordered sum of the four link"'),
    ("MUT-TABLE-BINDING", "G-PAPER-TABLES-AND-QUOTES-ARE-BOUND",
     "plants a table data row carrying a numeral that no rendered claim "
     "covers", "| planted | 4242 |"),
]

FUNCTIONS = [
    "say", "mut", "digest", "bdigest", "own_source", "_g", "fnorm", "fadd",
    "fneg", "fmul", "fconj", "zpow", "fscal", "fnormsq", "is_rational",
    "to_fraction", "in_q_sqrt2", "qsqrt2_pair", "qsqrt2_str", "qs_less",
    "gate", "__init__", "project", "resolve", "take", "reverify",
    "read_bytes", "load_sources",
    "dig", "wsnorm", "mnorm", "build_alphabet", "build_coins", "coin_sector",
    "coin_unitary_second_route", "cmul", "cdag", "is_monomial", "addv",
    "ends", "boundary", "point_symmetries", "apply_point", "point_on_dir",
    "chart_elements", "transported_link", "swap_conjugate", "gauge_twist",
    "link_op", "smul", "sdag", "sident", "holonomy", "plaq_corners",
    "uniform_cfg", "sccs", "closed_classes", "support_adj", "kernel_basis",
    "stationary_by_elimination", "verify_stationary", "row_stochastic",
    "covariance_failures", "lump", "orbits_from_perms", "gen_perm_group",
    "group_walk", "metropolis", "reversibility_failures", "has_self_loop",
    "born", "bmul", "measure_provenance", "measure_path_values",
    "measure_verbatim", "build_arena", "measure_chart_action",
    "measure_gauge_group", "measure_composition", "measure_parent_sets",
    "measure_law_native_rates", "named_nulls", "name_the_measure",
    "solve_instance", "build_dynamics_census", "run_the_census",
    "exhibit_the_gap_in_the_inherited_law", "verify_the_dimension_theorem",
    "measure_the_welds", "_closed_class_sets", "measure_relativity",
    "measure_the_surjection", "registered_keys_at_every_depth",
    "declared_function_names", "measure_wilson", "price_the_fibre",
    "head_law", "second_head_law", "demonstrate_reachability",
    "build_verdict", "reconstruct_verdict", "summarise_census",
    "build_claims", "verify_paper", "add", "harvest", "declared_mutants",
    "check_the_registry", "seal_and_write", "run", "selftest", "main",
]


def declared_mutants(tree):
    """every mutant switch this source contains, read off the syntax tree: a
    switch the scan cannot read -- mut() on a variable, or a bare MUT
    comparison outside mut's own body -- is FATAL rather than forgiven."""
    names, unreadable = set(), []
    inside_mut = set()
    for nd in ast.walk(tree):
        if isinstance(nd, ast.FunctionDef) and nd.name == "mut":
            for sub in ast.walk(nd):
                inside_mut.add(id(sub))
    for nd in ast.walk(tree):
        if id(nd) in inside_mut:
            continue
        if isinstance(nd, ast.Call) and getattr(nd.func, "id", None) == "mut":
            if (nd.args and isinstance(nd.args[0], ast.Constant)
                    and isinstance(nd.args[0].value, str)):
                names.add(nd.args[0].value)
            else:
                unreadable.append(ast.dump(nd)[:60])
        elif isinstance(nd, ast.Compare):
            lt = getattr(nd.left, "id", None)
            if lt == "MUT":
                unreadable.append("bare MUT comparison")
    return names, unreadable


def check_the_registry(S):
    src = own_source()
    tree = ast.parse(src)
    names, unreadable = declared_mutants(tree)
    declared = {m[0] for m in MUTANTS}
    extra = sorted(names - declared)
    missing = sorted(declared - names)
    LD.gate("G-MUTANT-REGISTRY-IS-TOTAL",
            "the mutant registry is checked TOTAL against this instrument's "
            "own syntax tree: every switch the source contains is declared "
            "and every declared falsifier has a branch to fire, and a switch "
            "the scan cannot read -- mut() on a computed name, or a bare MUT "
            "comparison outside mut's own body -- is fatal rather than "
            "forgiven, so a falsifier cannot exist as an unswept branch",
            not extra and not missing and not unreadable,
            "%d switches in the tree, %d declared; undeclared %s, missing "
            "%s, unreadable %s" % (len(names), len(declared), extra, missing,
                                   unreadable[:2]))

    # E-23: the published description is checked AGAINST THE CODE
    lines = src.split("\n")
    bad_desc = []
    reg = list(MUTANTS)
    if mut("MUT-FALSIFIER-DESCRIPTION"):
        reg[0] = (reg[0][0], reg[0][1], reg[0][2], "a token it never plants")
    for name, target, what, planted in reg:
        idx = [i for i, l in enumerate(lines) if 'mut("%s")' % name in l]
        window = ""
        for i in idx:
            window += "\n".join(lines[i:i + 8])
        if planted not in window:
            bad_desc.append(name)
    if mut("MUT-GHOST-FUNCTION"):
        pass
    S["mutants"] = [{"name": n, "target_gate": t, "description": w,
                     "plants": p} for n, t, w, p in MUTANTS]
    LD.gate("G-FALSIFIER-DESCRIPTIONS-ARE-HONEST",
            "E-23: a falsifier's published description is part of the sealed "
            "surface, so each one names the exact token it plants and that "
            "token is located in the source text of that mutant's own branch "
            "-- a description-inverted mutant is a false waiver wearing a "
            "green badge, and it dies here rather than in a reader's trust",
            not bad_desc, "%d declared falsifiers, %d whose planted token is "
            "not found in their own branch: %s"
            % (len(MUTANTS), len(bad_desc), bad_desc[:4]))
    SEAL.take("THE MUTANT REGISTRY", "mutants",
              "G-FALSIFIER-DESCRIPTIONS-ARE-HONEST", S["mutants"])

    fnames = declared_function_names(tree)
    extra_f = sorted(fnames - set(FUNCTIONS))
    missing_f = sorted(set(FUNCTIONS) - fnames)
    S["falsifier_totals"] = {
        "declared_falsifiers": len(MUTANTS),
        "distinct_target_gates": len({m[1] for m in MUTANTS}),
        "switches_in_the_syntax_tree": len(names),
        "functions_declared": len(FUNCTIONS),
        "the_sweep_result": "ALL-MUTANTS-IS-AN-EXTERNAL-BATTERY-RESULT-NOT-A-"
                            "PRODUCT-OF-THIS-RUN-AND-IS-REPORTED-AS-ONE"}
    LD.gate("G-FUNCTION-INVENTORY-IS-TOTAL",
            "the set of functions this source defines must equal the "
            "declared inventory exactly, so a function added to this "
            "instrument under any name -- neutral or not -- dies here, and a "
            "declared name deleted dies here too; and the published "
            "falsifier totals are checked against the same two scans that "
            "produced them, so no tally reaches the receipt unvouched",
            not extra_f and not missing_f
            and S["falsifier_totals"]["functions_declared"] == len(fnames)
            and S["falsifier_totals"]["switches_in_the_syntax_tree"]
            == len(names),
            "%d functions defined, %d declared; undeclared %s, missing %s"
            % (len(fnames), len(FUNCTIONS), extra_f[:4], missing_f[:4]))
    SEAL.take("THE FALSIFIER TOTALS", "falsifier_totals",
              "G-FUNCTION-INVENTORY-IS-TOTAL", S["falsifier_totals"])
    # #34 / E-23: HONEST DENOMINATORS.  Every gate closed in this run is
    # either the declared target of a falsifier, or carries a registered
    # forcing, or is named with the reason no falsifier reaches it.
    targets = {m[1] for m in MUTANTS}
    closed_gates = [r["gate"] for r in LD.rows]
    covered = [g for g in closed_gates if g in targets]
    inst_gates = [g for g in closed_gates
                  if g.startswith("G-INSTANCE-") and g not in targets]
    named = {
        "G-ARTIFACT-INTEGRITY": "fires only on a run that writes, and a "
                                "mutant run never writes; the seal it "
                                "checks against is falsified by MUT-SEAL "
                                "at the gate before it",
        "G-PAPER-PRESENT": "the else-branch of a paper that exists; it "
                           "cannot close in a run whose paper is present, "
                           "and it is reported here rather than counted as "
                           "covered",
    }
    uncovered = [g for g in closed_gates
                 if g not in targets and g not in inst_gates
                 and g not in named]
    # the registered forcing, machine-checked: the per-instance gate's
    # predicate mentions no instance by name, so the two falsifiers that
    # fire it -- at two DIFFERENT instances -- fire the same predicate every
    # instance is judged by
    src_lines = own_source().split("\n")
    gi = [i for i, l in enumerate(src_lines)
          if 'LD.gate("G-INSTANCE-" + rec["instance"]' in l]
    pred = "\n".join(src_lines[gi[0]:gi[0] + 26]) if gi else ""
    named_in_pred = [r["instance"] for r in S["census"]["instances"]
                     if '"%s"' % r["instance"] in pred]
    inst_falsified = sorted({m[1] for m in MUTANTS
                             if m[1].startswith("G-INSTANCE-")})
    S["waiver_ledger"] = {
        "gates_closed": len(closed_gates),
        "covered_by_a_declared_falsifier": len(covered),
        "per_instance_gates_under_the_registered_forcing": len(inst_gates),
        "named_unreachable": named,
        "uncovered": uncovered,
        "the_forcing": "THE-PER-INSTANCE-GATE-PREDICATE-NAMES-NO-INSTANCE-"
                       "SO-ONE-FALSIFIER-AT-ONE-INSTANCE-FALSIFIES-THE-"
                       "PREDICATE-AT-ALL-OF-THEM",
        "instances_named_inside_the_predicate": named_in_pred,
        "per_instance_gates_carrying_their_own_falsifier": inst_falsified,
    }
    LD.gate("G-FALSIFIER-COVERAGE-AT-AN-HONEST-DENOMINATOR",
            "the falsifier ledger is published at an honest denominator "
            "(#34): every gate this run closed is either the declared "
            "target of a mutant, or a per-instance gate covered by a "
            "REGISTERED FORCING, or named with the reason no falsifier "
            "reaches it -- and the forcing is machine-checked rather than "
            "asserted, because the per-instance gate's predicate is "
            "verified to mention no instance by name, so the two mutants "
            "that fire it at two DIFFERENT instances fire the identical "
            "predicate every instance is judged by",
            not uncovered and not named_in_pred and len(inst_falsified) >= 2,
            "%d gates closed; %d are declared mutant targets, %d are "
            "per-instance gates under the forcing, %d are named unreachable, "
            "%d uncovered %s; the per-instance predicate names %d instances; "
            "%d distinct per-instance gates carry a mutant"
            % (len(closed_gates), len(covered), len(inst_gates), len(named),
               len(uncovered), uncovered[:3], len(named_in_pred),
               len(inst_falsified)))
    SEAL.take("THE WAIVER LEDGER", "waiver_ledger",
              "G-FALSIFIER-COVERAGE-AT-AN-HONEST-DENOMINATOR",
              S["waiver_ledger"])


# ===========================================================================
# SECTION 14.  THE SEAL, THE ARTIFACTS, THE CLI
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
    "totals": "the closing tallies, derived from sealed objects",
    "transcript_head": "the transcript digest, taken at the disk boundary",
}


def seal_and_write(S, write, paper_bytes):
    verdict = S["verdict"]
    S["verdict_head"] = S["census"]["head"]
    SEAL.take("THE VERDICT STRING", "verdict", "G-VERDICT-RECONSTRUCTION",
              verdict)
    SEAL.take("THE VERDICT HEAD", "verdict_head",
              "G-VERDICT-RECONSTRUCTION", S["verdict_head"])
    S["unit"] = UNIT
    S["schema"] = SCHEMA
    S["pin_sha256_prefix"] = PIN_SHA12
    S["python"] = "%d.%d" % sys.version_info[:2]
    S["paper_sha256_12"] = bdigest(paper_bytes)
    S["exit_conventions"] = (
        "the delivery run exits 0 on success and 1 on any refusal writing "
        "nothing; --selftest exits 0 when every anchor class is fatal; "
        "--mutant exits 0 when the named mutant dies on its declared target; "
        "an unknown flag exits 2")
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
        "mutants": len(MUTANTS),
        "sources": len(SOURCES),
        "path_value_anchors": len(PATH_VALUES),
        "verbatim_anchors": len(VERBATIM),
        "anchors": len(SOURCES) + len(PATH_VALUES) + len(VERBATIM),
        "sealed_objects": len(SEAL.man),
        "instances_run": S["census"]["instances_run"],
    }
    if mut("MUT-SEAL"):
        payload["arena"] = dict(payload["arena"])
        payload["arena"]["coins"] = "MOVED-AFTER-THE-GATE"

    unsealed = [k for k in payload
                if k not in SEAL.by_key and k not in DECLARED_UNSEALED]
    moved = SEAL.reverify(payload)
    ids = [r["gate"] for r in LD.rows]
    ls = S.get("ledger_shape", {})
    shape_ok = ("paper_coverage" not in S) or (
        all(g in ids for g in PAPER_GATE_IDS)
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
            "seals are taken AT VALUE-CLOSE -- each instance record at its "
            "own gate, each sub-object at the gate that vouches it, with "
            "every omission declared in the manifest row -- so there is no "
            "window between a gate and its seal for a published field to be "
            "edited in; and the ledger's own published shape is checked "
            "against the ledger it describes",
            not unsealed and not moved and shape_ok,
            "%d published keys, %d sealed, %d declared unsealed, %d "
            "undeclared %s, %d moved since their gate %s; ledger shape "
            "consistent with the %d rows closed: %s"
            % (len(payload), len(SEAL.by_key), len(DECLARED_UNSEALED),
               len(unsealed), unsealed[:4], len(moved), moved[:4],
               len(LD.rows), shape_ok))

    transcript = "\n".join(LOG) + "\n" + verdict + "\n"
    payload["transcript_head"] = digest(transcript)
    blob = json.dumps(payload, indent=1, sort_keys=True, default=str)
    outtxt = transcript
    if not write:
        return payload, 0
    # THE PROMOTION ORDER: both temporaries are written, both are READ BACK
    # from the filesystem and compared against the gate-time seals, and only
    # then is either moved into place.  A refusing integrity gate therefore
    # promotes NOTHING and leaves no temporary behind -- the disclosed
    # convention 'exits 1 on any refusal, writing nothing' is true at the one
    # gate built for the disk boundary too.
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
            "passing check promotes them into place.  A refusal removes the "
            "temporaries and leaves the published artifacts untouched",
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
    measure_chart_action(S, pv)
    measure_gauge_group(S, pv)
    measure_composition(S, pv)
    measure_parent_sets(S, pv)
    measure_law_native_rates(S, pv)
    say("  arena: %d coins, %d links, %d plaquettes; gauge orbits %d and %d"
        % (S["arena"]["coins"], S["arena"]["links"], S["arena"]["plaquettes"],
           S["gauge"]["orbits_chart_32"], S["gauge"]["orbits_chart_128"]))
    S["_P"] = {}
    rows = build_dynamics_census(S, pv)
    say("  THE DECLARED-DYNAMICS CENSUS -- %d instances:" % len(rows))
    published = run_the_census(S, rows, pv)
    exhibit_the_gap_in_the_inherited_law(S)
    verify_the_dimension_theorem(S)
    measure_the_welds(S, published, pv)
    widest, argmax, agree = measure_relativity(S, published, pv)
    measure_the_surjection(S, published, pv)
    measure_wilson(S, published, pv)
    price_the_fibre(S, published, pv)
    summarise_census(S, published, agree, widest)
    demonstrate_reachability(S, published)
    check_the_registry(S)

    verdict = build_verdict(S)
    if mut("MUT-VERDICT-COMPARATOR"):
        verdict = verdict.replace("SMU-", "SMU-X-", 1)
    recon = reconstruct_verdict(dict(S, verdict=verdict))
    LD.gate("G-VERDICT-RECONSTRUCTION",
            "the complete verdict string is compared for equality against an "
            "INDEPENDENT reconstruction that reads only the serialized "
            "receipt, derives the head by a second head law, and re-renders "
            "every segment from the primitive measured tables -- reading "
            "neither the builder's segments nor the builder's counts and "
            "sharing no format string and no helper with it, so 'the same "
            "concatenation written twice' cannot pass",
            verdict == recon,
            "builder %d characters, reconstruction %d, equal: %s%s"
            % (len(verdict), len(recon), verdict == recon,
               "" if verdict == recon else
               " || first divergence at %d" % next(
                   (i for i in range(min(len(verdict), len(recon)))
                    if verdict[i] != recon[i]), -1)))
    S["verdict"] = verdict

    S["code_sha256_12"] = bdigest(
        open(os.path.abspath(__file__), "rb").read())
    ls = {"gates_closed_before_the_paper_gates": len(LD.rows) + 1,
          "instance_gates": S["census"]["instances_run"],
          "paper_gates": len(PAPER_GATE_IDS),
          "closing_gates": len(CLOSING_GATE_IDS),
          "objects_sealed_before_the_paper_gates": len(SEAL.man)}
    if mut("MUT-LEDGER-SHAPE"):
        ls["instance_gates"] = ls["instance_gates"] + 1
    inst_rows = len([r for r in LD.rows if r["gate"].startswith("G-INSTANCE-")])
    LD.gate("G-LEDGER-SHAPE-IS-CONSISTENT",
            "the ledger's own published shape is a MEASUREMENT of the ledger "
            "and not a description of it: the instance-gate count is "
            "recounted from the rows themselves, the sealed-object count "
            "from the manifest itself, and the gate total includes this gate "
            "-- so a shape row that drifted from the ledger it describes "
            "dies here rather than being read as a summary a reader can "
            "trust",
            ls["instance_gates"] == inst_rows
            and ls["objects_sealed_before_the_paper_gates"] == len(SEAL.man)
            and ls["gates_closed_before_the_paper_gates"] == len(LD.rows) + 1,
            "%d instance gates published against %d rows; %d sealed objects "
            "published against a manifest of %d; %d gates closed including "
            "this one"
            % (ls["instance_gates"], inst_rows,
               ls["objects_sealed_before_the_paper_gates"], len(SEAL.man),
               ls["gates_closed_before_the_paper_gates"]))
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
            "VERBATIM", [(V0[0][0], V0[0][1], "a window that is not there "
                          "in any of the pinned sources at all whatsoever",
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


USAGE = """usage: smu_exact.py [--no-write] [--selftest] [--mutant NAME]
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
        for g in sorted({m[1] for m in MUTANTS}):
            print(g)
        return 0
    if args.get("list-mutants"):
        for n, t, w, p in MUTANTS:
            print("%-32s -> %-52s %s" % (n, t, w))
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
        print("MUTANT %-32s target %-52s died at %s :: artifacts unchanged "
              "%s :: %s" % (name, target, died_at, unchanged,
                            "DEAD-ON-TARGET" if ok else "FAILED"))
        return 0 if ok else 1
    if args.get("all-mutants"):
        bad = []
        for n, t, w, p in MUTANTS:
            globals()["LD"] = Ledger()
            globals()["SEAL"] = Seal()
            globals()["MUT"] = n
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
            if died != t:
                bad.append((n, died))
            print("%-32s %s" % (n, "DEAD-ON-TARGET" if died == t
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
        run(write=not args.get("no-write"),
            paper_gates=True)
    except GateFail as e:
        sys.stderr.write("REFUSED :: %s\n" % e)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
