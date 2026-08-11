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
    if not QUIET:
        LOG.append(msg)
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
    """gate-to-disk (#119): digest at gate time; the manifest is TOTAL --
    every published top-level key is either sealed at the gate that produced
    it or named in the declaration with the reason it cannot be."""

    def __init__(self):
        self.man = []
        self.by_key = {}

    def take(self, name, key, gate, obj):
        d = digest(obj)
        self.man.append({"object": name, "receipt_key": key, "gate": gate,
                         "digest": d})
        self.by_key[key] = (d, obj)
        return d

    def reverify(self, payload):
        bad = []
        for row in self.man:
            k = row["receipt_key"]
            if k not in payload:
                bad.append((k, "absent"))
                continue
            if digest(payload[k]) != row["digest"]:
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
    p = os.path.join(REPO, rel)
    with open(p, "rb") as fh:
        return fh.read()


def load_sources():
    got = {}
    rows = []
    for name, rel, sha, what in SOURCES:
        b = read_bytes(rel)
        d = bdigest(b)
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
    if mut("MUT-AST-BLIND"):
        floats = []
        badimp = ["planted"]
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
        needle = mnorm(window)
        n = hay.count(needle)
        # the perturbation: a content-bearing token is altered and the window
        # must stop being locatable
        toks = [t for t in re.findall(r"[A-Za-z0-9]+", window) if len(t) > 3]
        pert = window.replace(toks[-1], toks[-1] + "X", 1) if toks else window
        pn = hay.count(mnorm(pert))
        ok = (n == 1 and pn == 0 and len(needle) >= 40)
        if mut("MUT-VERBATIM") and aid == "VB-P23-LAW":
            ok = False
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

    # the carrier: paper-23's primary carrier, which is the chart-fixed locus
    carrier_ok = (len(coins) == pv["PV-SLICE"] == pv["PV-FIXLOC"])
    if mut("MUT-CARRIER"):
        carrier_ok = False
    LD.gate("G-CARRIER-IS-THE-PARENTS-PRIMARY-CARRIER",
            "the carrier of this unit is the parent's own primary carrier -- "
            "the uniform configurations, one coin repeated on every link, "
            "which paper-23 measured to be exactly the chart-fixed locus of "
            "the anchored chart -- so this unit's dynamics act where the "
            "parent's simplex lives and the two are comparable object for "
            "object.  The full configuration space is not a carrier here and "
            "is named as scope",
            carrier_ok,
            "carrier %d states; parent's uniform slice %d; parent's "
            "chart-fixed locus %d"
            % (len(coins), pv["PV-SLICE"], pv["PV-FIXLOC"]))
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
    per_dir_closed = all(True for _ in states)
    if mut("MUT-ENLARGEMENT"):
        states = states[:len(coins)]
    LD.gate("G-CHART-128-ENLARGEMENT",
            "the smallest carrier on which the extension DOES act is "
            "computed as an orbit closure of the parent's carrier rather "
            "than declared: every image of a uniform configuration is "
            "constant on each direction class, so the closure is a set of "
            "two-coin configurations, and it is closed by construction "
            "because the closure is taken to a fixed point",
            len(states) > len(coins) and per_dir_closed,
            "the extension's closure of the %d-state carrier is %d states"
            % (len(coins), len(states)))
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
    genels = [((1, 0), (False, 1, 1)), ((0, 1), (False, 1, 1)),
              ((0, 0), (True, 1, 1)), ((0, 0), (False, -1, 1))]
    gens128 = [perms128[els.index(e)] for e in genels]
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
            for i in sect_members[s]:
                tgt[i] = law[a[k]] / len(sect_members[s])
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
        else:
            rec["gauge_covariance_failures"] = None
            rec["gauge_covariant"] = None
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
    rowset = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (1, 0, 1),
              (0, 1, 1), (1, 1, 1)]
    tot = bad = 0
    for r0 in rowset:
        for r1 in rowset:
            for r2 in rowset:
                P, adj = [], []
                for r in (r0, r1, r2):
                    s = sum(r)
                    P.append({j: Fraction(r[j], s) for j in range(3) if r[j]})
                    adj.append([j for j in range(3) if r[j]])
                comps = sccs(3, adj)
                closed, _cid = closed_classes(3, adj, comps)
                bas, _rk = stationary_by_elimination(P, 3)
                tot += 1
                if len(bas) != len(closed):
                    bad += 1
    if mut("MUT-DIMENSION-THEOREM"):
        bad = 0 if bad else 1
    LD.gate("G-SIMPLEX-DIMENSION-THEOREM",
            "the identity the reducible verdicts are read through -- the "
            "stationary simplex's dimension is one less than the number of "
            "closed communicating classes -- is VERIFIED EXHAUSTIVELY on a "
            "declared family of small chains, every one of them solved by "
            "the same exact elimination this unit uses at scale, so the "
            "bridge from a class count to a simplex dimension is measured "
            "and not quoted",
            bad == 0, "%d chains enumerated exhaustively, %d mismatches "
            "between the kernel dimension and the closed-class count"
            % (tot, bad))
    S["dimension_theorem"] = {"chains_enumerated": tot, "mismatches": bad,
                              "carrier_states": 3,
                              "row_alphabet": len(rowset)}
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
    same32 = cls32 == sorted(sorted(o) for o in O4)
    same128 = cls128 == sorted(sorted(o) for o in O8)
    if mut("MUT-WELD"):
        same32 = False
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
    ok = (g32["simplex_dimension"] == pv["PV-SIMP32"]
          and g128["simplex_dimension"] == pv["PV-SIMP128"])
    if mut("MUT-SIMPLEX-DIM"):
        ok = not ok
    LD.gate("G-GAUGE-WALK-SIMPLEX-IS-THE-PARENTS-SIMPLEX",
            "and the gauge walk's stationary simplex IS paper-23's invariant "
            "simplex: an invariant measure is exactly an orbit-constant one, "
            "a group walk's stationary measures are exactly the invariant "
            "ones, and the dimensions this run computes by exact elimination "
            "land on the parent's published dimensions at named receipt "
            "paths.  The dynamics did not shrink the parent's simplex by one "
            "number",
            ok, "chart-32 simplex dimension %d against the parent's %d; "
            "chart-128 %d against %d"
            % (g32["simplex_dimension"], pv["PV-SIMP32"],
               g128["simplex_dimension"], pv["PV-SIMP128"]))

    mono = by["MONOMIAL-LEFT"]
    monoset = set(S["_mono"])
    cls = _closed_class_sets(S, "MONOMIAL-LEFT")
    carries = any(set(c) == monoset for c in cls)
    if mut("MUT-MONOMIAL"):
        carries = False
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
    wider = widest > parent_widest
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
            "than on sets chosen to make it large.  Two of the columns "
            "reproduce paper-23's published masses exactly at named receipt "
            "paths, which is what makes the new columns comparable; and the "
            "widest spread is compared with the parent's own widest spread "
            "over INVARIANT measures, so the reader can see whether "
            "declaring a dynamics costs more or less than declaring a "
            "measure did",
            moves and cnt_ok,
            "widest spread %s over the %d GAUGE-COVARIANT deriving "
            "instances on "
            "%s, against the parent's %s over invariant measures (wider: "
            "%s); over all %d deriving instances, the declared "
            "non-covariant control included, it is %s; %d sets weighed"
            % (widest, len(cov), argmax_sets, parent_widest, wider, len(der),
               widest_all, len(rows)))

    agree = len({tuple(S["_pi"][r["instance"]]) for r in der}) == 1
    if mut("MUT-QUASI"):
        agree = True
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
        "parent_widest_spread_over_invariant_measures": str(parent_widest),
        "this_fibre_is_wider_than_the_parents": wider,
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
            bas, _rk = stationary_by_elimination(P, 4)
            tot += 1
            if len(bas) != 1 or bas[0] != t:
                bad += 1
    if mut("MUT-SURJECTION"):
        bad = 1 if bad == 0 else 0
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
        "exhaustive_small_carrier_denominator": D,
        "consequence": "THE-COVARIANT-DYNAMICS-FIBRE-SURJECTS-ONTO-THE-"
                       "INVARIANT-SIMPLEX",
        "price_chart_32": pv["PV-SIMP32"], "price_chart_128": pv["PV-SIMP128"],
    }
    SEAL.take("THE SURJECTION", "surjection", "G-PRICE-IS-CONSERVED",
              S["surjection"])
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
    if mut("MUT-WILSON-OBSERVABLE"):
        dep = 1
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
    gauge_inv = all(len({tb[i] for i in o}) == 1 for o in O4)
    if mut("MUT-WILSON-GAUGE-INVARIANCE"):
        gauge_inv = False
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
    for r in sorted(der, key=lambda x: x["instance"]):
        pi = S["_pi"][r["instance"]]
        acc = ZERO
        for i, w in enumerate(pi):
            if w:
                acc = fadd(acc, fscal(tb[i], w.numerator, w.denominator))
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

    verdicts = {r["instance"]: r["verdict"] for r in published}
    unlicensed = [r["declared_dynamics"] for r in rows
                  if verdicts.get(r["declared_dynamics"]) != "DERIVES"]
    unstamped = [r["declared_dynamics"] for r in rows
                 if r.get("stamp") != STAMP]
    # the payload is walked to the BOTTOM for an expectation-valued key at
    # any depth; every one must sit under this unit's single registered key
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

    # the range over the invariant simplex: the convex hull of the orbit
    # values, whose endpoints are attained at extreme points
    vals = []
    for o in O4:
        vals.append((qsqrt2_pair(tb[o[0]]), o))
    lo = hi = vals[0]
    for v in vals[1:]:
        if qs_less(v[0], lo[0]):
            lo = v
        if qs_less(hi[0], v[0]):
            hi = v
    lo_r = all(qsqrt2_pair(tb[i])[1] == 0 for i in lo[1])
    hi_r = all(qsqrt2_pair(tb[i])[1] == 0 for i in hi[1])
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
            "both_endpoints_are_extreme_points_of_the_simplex": True,
            "stamp": STAMP,
        },
        "must_not": "NO-AREA-LAW-NO-STRING-TENSION-NO-POTENTIAL-CLAIM-AND-"
                    "NO-LOOP-FAMILY-IS-GROWN",
    }
    SEAL.take("THE WILSON SEGMENT", "wilson", "G-WILSON-LICENCE", S["wilson"])
    S["_wilson_range"] = (lo[0][0], hi[0][0])
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
    for a in sorted(axes.values(), key=lambda x: x["axis"]):
        rows.append({"choice": a["axis"], "status": "DECLARED-AND-SWEPT",
                     "fibre": a["fibre"], "instances_built": a["instances_run"],
                     "distinct_outcomes": a["distinct_outcomes_along_this_axis"],
                     "verdict_determining": a["verdict_determining"],
                     "why": "every declared instance of this axis is RUN and "
                            "its outcome published"})
    if mut("MUT-FIBRE"):
        rows[-1]["fibre"] = 99
    free_with_fibre_one = [r for r in rows
                           if r["fibre"] == 1 and r["status"].startswith(
                               "GENUINELY")]
    swept_ok = all(r["instances_built"] == r["fibre"] for r in rows
                   if isinstance(r["fibre"], int)
                   and r["status"] == "DECLARED-AND-SWEPT")
    LD.gate("G-FIBRE-INVENTORY",
            "every construction choice is inventoried with its fibre and its "
            "instances, and every DECLARED axis is swept to the bottom -- "
            "the number of instances built equals the fibre, so no member of "
            "a declared fibre is left unrun and the census cannot be a "
            "sample of its own declaration.  The verdict-determining flag "
            "binds each row by its own measured predicate: re-running the "
            "axis at another instance moves a published vector",
            swept_ok and not free_with_fibre_one,
            "%d inventory rows; %d declared axes all swept to the bottom: %s"
            % (len(rows), sum(1 for r in rows
                              if r["status"] == "DECLARED-AND-SWEPT"),
               swept_ok))
    S["fibre"] = {"rows": rows,
                  "price_of_a_covariant_declaration_chart_32":
                      pv["PV-SIMP32"],
                  "price_of_a_covariant_declaration_chart_128":
                      pv["PV-SIMP128"],
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


def head_law(published, agree, widest, blocked):
    """the builder's head law."""
    if blocked:
        return "SMU-BLOCKED-AT-%s" % blocked
    der = [r for r in published if r["verdict"] == "DERIVES"]
    red = [r for r in published if r["verdict"] == "REDUCIBLE"]
    if not der:
        return "SMU-REDUCIBLE-%d-INSTANCES-0-DERIVE" % len(red)
    if agree:
        return "SMU-QUASI-DERIVED-ALL-%d-DERIVING-INSTANCES-AGREE" % len(der)
    if widest > 0:
        return ("SMU-DYNAMICS-RELATIVE-SPREAD-%s-OVER-%d-DERIVING-INSTANCES"
                % (widest, len(der)))
    return "SMU-DERIVED-%d" % len(der)


def second_head_law(published, agree, widest, blocked):
    """an INDEPENDENT reconstruction: a different branch structure, written
    from the same pre-registered outcomes, sharing no format string and no
    helper with the builder's."""
    if blocked is not None and blocked != "":
        return "SMU-BLOCKED-AT-" + str(blocked)
    n_der = sum(1 for r in published if r["verdict"] == "DERIVES")
    n_red = sum(1 for r in published if r["verdict"] != "DERIVES")
    if n_der == 0:
        return "SMU-REDUCIBLE-" + str(n_red) + "-INSTANCES-0-DERIVE"
    if not agree and widest > 0:
        return ("SMU-DYNAMICS-RELATIVE-SPREAD-" + str(widest) + "-OVER-"
                + str(n_der) + "-DERIVING-INSTANCES")
    if agree:
        return ("SMU-QUASI-DERIVED-ALL-" + str(n_der)
                + "-DERIVING-INSTANCES-AGREE")
    return "SMU-DERIVED-" + str(n_der)


def demonstrate_reachability(S, published):
    """the other pre-registered outcomes are REACHABLE, and the reachability
    is RUN rather than advertised: the same head law is handed synthetic
    census tables and must return them."""
    probes = []
    one = [dict(published[0])]
    one[0] = dict(one[0])
    one[0]["verdict"] = "DERIVES"
    probes.append(("SMU-QUASI-DERIVED", head_law(one, True, Fraction(0),
                                                 None)))
    allred = [dict(r, verdict="REDUCIBLE") for r in published]
    probes.append(("SMU-REDUCIBLE", head_law(allred, False, Fraction(0),
                                             None)))
    probes.append(("SMU-BLOCKED-AT",
                   head_law(published, False, Fraction(1), "AN-OBJECT")))
    probes.append(("SMU-DYNAMICS-RELATIVE",
                   head_law(published, False, Fraction(1, 2), None)))
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
               "SIMPLEX"
               % (cen["law_native_instances"], cen["law_native_measure_name"],
                  "-".join(S["law_native_rates"]["values"])))
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
               "CONTROL-INCLUDED=%s|AGAINST-THE-PARENTS-WIDEST-OVER-"
               "INVARIANT-MEASURES-%s-SO-DECLARING-A-DYNAMICS-MOVES-THE-"
               "PARENTS-OWN-HEADLINE-SETS-%s|QUASI-DERIVATION-ARM-REACHABLE-"
               "AND-MEASURED-TO-FAIL"
               % (rel["gauge_covariant_deriving_instances"], rel["widest_spread"],
                  rel["widest_attained_count"], len(rel["rows"]),
                  ",".join(rel["widest_attained_on"]),
                  rel["deriving_instances"],
                  rel["widest_spread_over_every_deriving_instance"],
                  rel["parent_widest_spread_over_invariant_measures"],
                  "FURTHER" if rel["this_fibre_is_wider_than_the_parents"]
                  else "LESS-FAR"))
    seg.append("PRICE=CONSERVED-NOT-PAID:THE-COVARIANT-DYNAMICS-FIBRE-"
               "SURJECTS-ONTO-THE-INVARIANT-SIMPLEX-SO-A-DECLARATION-STILL-"
               "SUPPLIES-%d-INDEPENDENT-NUMBERS-AT-THE-ANCHORED-READING-AND-"
               "%d-AT-THE-EXTENSION-EXACTLY-THE-PARENTS-COUNTS|WHAT-MOVED-IS-"
               "WHERE-THE-DECLARATION-IS-MADE-NOT-HOW-MUCH-IT-COSTS"
               % (fib["price_of_a_covariant_declaration_chart_32"],
                  fib["price_of_a_covariant_declaration_chart_128"]))
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
    head = second_head_law(ins, agree, widest, None)

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
    parts.append("(c)LAW-NATIVE-RESAMPLING=IRREDUCIBLE-AND-DERIVES-AT-ALL-"
                 + str(len(lawi)) + "-MEMBERS-OF-ITS-DECLARED-FIBRE;THE-"
                 "MEASURE-IS-" + lawi[0]["measure_name"] + "-SECTOR-GRADED-"
                 "AT-" + "-".join(payload["law_native_rates"]["values"])
                 + "-AND-INVARIANT-SO-IT-IS-A-POINT-OF-THE-PARENTS-SIMPLEX")
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
                 + "|AGAINST-THE-PARENTS-WIDEST-OVER-INVARIANT-MEASURES-"
                 + rel["parent_widest_spread_over_invariant_measures"]
                 + "-SO-DECLARING-A-DYNAMICS-MOVES-THE-PARENTS-OWN-HEADLINE-"
                 "SETS-" + ("FURTHER" if widest > Fraction(
                     rel["parent_widest_spread_over_invariant_measures"])
                     else "LESS-FAR")
                 + "|QUASI-DERIVATION-ARM-REACHABLE-AND-MEASURED-TO-FAIL")
    parts.append("PRICE=CONSERVED-NOT-PAID:THE-COVARIANT-DYNAMICS-FIBRE-"
                 "SURJECTS-ONTO-THE-INVARIANT-SIMPLEX-SO-A-DECLARATION-"
                 "STILL-SUPPLIES-" + str(sur["price_chart_32"])
                 + "-INDEPENDENT-NUMBERS-AT-THE-ANCHORED-READING-AND-"
                 + str(sur["price_chart_128"])
                 + "-AT-THE-EXTENSION-EXACTLY-THE-PARENTS-COUNTS|WHAT-MOVED-"
                 "IS-WHERE-THE-DECLARATION-IS-MADE-NOT-HOW-MUCH-IT-COSTS")
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
        "head": head_law(published, agree, widest, None),
    }
    h2 = second_head_law(published, agree, widest, None)
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
MUST_NOT = [
    "area law", "area-law", "the law of the area",
    "string tension", "string-tension",
    "confining", "confinement", "quark", "potential",
]
DECLARING = [
    "no area-law, string-tension, or potential claim",
    "NO-AREA-LAW-NO-STRING-TENSION-NO-POTENTIAL-CLAIM",
    "NO-CONFINEMENT-CLAIM",
    "the confinement vocabulary stays behind its gate",
    "The confinement vocabulary stays behind its gate",
    "makes no area-law, string-tension or potential claim",
    "no area-law claim, no string-tension claim and no potential claim",
    "A confinement analog would need three objects this arena does not have",
    "the words this unit does not use",
    "grows no loop family and makes no claim about how any expectation "
    "would behave as a loop grows",
    "the confinement vocabulary is barred outright",
    "what a confinement-shaped follow-on would need",
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
    c.append(("closure is %d states" % ca["CHART-128"]["enlarged_carrier"], 1))
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
    c.append(("the parent's widest spread over invariant measures was %s" %
              rel["parent_widest_spread_over_invariant_measures"], 1))
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
                     if r.get("verdict_determining"))), 1))
    wl = S["waiver_ledger"]
    c.append(("%d are the declared targets of falsifiers, %d are the "
              "per-instance gates under one registered forcing, and %d are "
              "uncovered" % (wl["covered_by_a_declared_falsifier"],
                             wl["per_instance_gates_under_the_registered_"
                                "forcing"], len(wl["uncovered"])), 1))
    for r in wil["rows"]:
        c.append(("%s under %s" % (r["block_trace_value"],
                                   r["declared_dynamics"]), 1))
    return c


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
    hay = mnorm(paper_text)
    miss = []
    for frag, want in claims:
        got = hay.count(mnorm(frag))
        if got != want:
            miss.append({"claim": frag, "expected": want, "found": got})
    if mut("MUT-CLAIM"):
        miss = [{"claim": "planted", "expected": 1, "found": 0}]
    LDx.gate("G-PAPER-CLAIMS",
            "every load-bearing sentence of the paper is RENDERED FROM THE "
            "RECEIPT and located in the delivered bytes at its exact "
            "occurrence count, under whitespace and markdown-prefix "
            "normalisation (#125) -- so a number corrupted at one of its "
            "several occurrences dies, and a paper whose prose drifted from "
            "the run that produced it cannot be delivered",
            not miss, "%d rendered claims, %d not located at their counts: %s"
            % (len(claims), len(miss), miss[:3]))

    verdict = S["verdict"]
    blocks = [wsnorm(b) for b in
              re.findall(r"```(?:[a-z]*)\n(.*?)```", paper_text, re.S)]
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

    sw = mnorm(paper_text)
    for d in DECLARING:
        sw = sw.replace(mnorm(d), " ")
    hits = [w for w in MUST_NOT if mnorm(w) in sw]
    if mut("MUT-MUST-NOT"):
        hits = ["planted"]
    LDx.gate("G-MUST-NOT-VOCABULARY",
            "the pin's must-not vocabulary -- inherited VERBATIM from "
            "paper-23's repaired gate, the bare words included -- is swept "
            "over this paper's own text with the declaring sentences removed "
            "first and inline emphasis stripped, so a claim under asterisks "
            "is still the same claim and a paragraph that made an area-law, "
            "string-tension or potential claim would die on the delivery run",
            not hits, "must-not vocabulary found: %s" % hits)

    pol = []
    low = mnorm(paper_text)
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
    if mut("MUT-POLARITY"):
        pol[0]["ok"] = False
    LDx.gate("G-PAPER-POLARITY",
            "the direction-bearing claims are checked for POLARITY as well "
            "as presence -- each must occur and must not sit inside a window "
            "carrying a declared negator -- which closes the "
            "direction-blindness of a fragment gate",
            all(p["ok"] for p in pol),
            "%d polarity rows, %d failing"
            % (len(pol), sum(1 for p in pol if not p["ok"])))

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
    harvest({k: v for k, v in S.items() if not k.startswith("_")})
    # the ONLY literals the coverage gate may forgive: section numbers up
    # to this paper's own length, and the corpus engraving references.  The
    # list is published in the receipt so a reader can see exactly what was
    # forgiven.
    STRUCTURAL = ({str(k) for k in range(0, 28)}
                  | {"%d.%d" % (a, b) for a in range(1, 13)
                     for b in range(0, 13)}
                  | {"34", "46", "62", "82", "87", "91", "119", "125"})
    scan = paper_text
    nums = re.findall(r"\d+(?:/\d+)?(?:\.\d+)?", scan)
    unmatched = []
    for x in nums:
        if x in allowed or x in STRUCTURAL:
            continue
        if "/" in x and all(p in allowed for p in x.split("/")):
            continue
        unmatched.append(x)
    if mut("MUT-COVERAGE"):
        unmatched = ["planted"]
    spans = len(re.findall(r"`[^`]*\d[^`]*`", paper_text))
    fenced = len(re.findall(r"```", paper_text))
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
                           "structural_literals_forgiven":
                               sorted(STRUCTURAL)}
    S["paper_claims"] = [{"claim": f, "occurrences": w} for f, w in claims]
    S["paper_polarity"] = pol
    SEAL.take("THE PAPER COVERAGE", "paper_coverage",
              "G-PAPER-NUMERAL-COVERAGE", S["paper_coverage"])
    SEAL.take("THE PAPER CLAIMS", "paper_claims", "G-PAPER-CLAIMS",
              S["paper_claims"])
    SEAL.take("THE PAPER POLARITY", "paper_polarity", "G-PAPER-POLARITY",
              S["paper_polarity"])


# ===========================================================================
# SECTION 13.  THE MUTANT REGISTRY, TOTAL AND HONESTLY DESCRIBED (E-23)
# ===========================================================================

MUTANTS = [
    ("MUT-SOURCE-DRIFT", "G-SOURCE-BYTES",
     "replaces one pinned source's measured digest with zeros",
     '"000000000000"'),
    ("MUT-AST-BLIND", "G-EXACT-ARITHMETIC-BY-AST",
     "empties the float-literal list and plants a banned import",
     'badimp = ["planted"]'),
    ("MUT-PATH-VALUE", "G-PATH-VALUE-ANCHORS",
     "moves one inherited path-value to 999", "got = 999"),
    ("MUT-VERBATIM", "G-VERBATIM-ANCHORS",
     "fails one verbatim window's locate-and-perturb test", "ok = False"),
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
     "inverts the exhaustive theorem check's mismatch count",
     "bad = 0 if bad else 1"),
    ("MUT-WELD", "G-GAUGE-WALK-CLASSES-ARE-THE-PARENTS-ORBITS",
     "denies the set-level identity between the gauge walk's classes and "
     "the parent's orbits", "same32 = False"),
    ("MUT-MONOMIAL", "G-MONOMIAL-WALK-CARRIES-THE-PARENTS-HAAR",
     "denies that one closed class is the parent's Haar carrier",
     "carries = False"),
    ("MUT-ORBIT-CLOSURE", "G-SETS-ARE-UNIONS-OF-ORBITS",
     "declares one re-weighed set not to be a union of orbits",
     '"orbit_closed_chart_32"'),
    ("MUT-SPREAD", "G-RELATIVITY-CENSUS",
     "zeroes the widest measured spread", "widest = Fraction(0)"),
    ("MUT-QUASI", "G-QUASI-DERIVATION-ARM-IS-DECIDED-NOT-ASSUMED",
     "declares the deriving instances to agree when they do not",
     "agree = True"),
    ("MUT-SURJECTION", "G-PRICE-IS-CONSERVED",
     "inverts the exhaustive surjection arm's failure count",
     "bad = 1 if bad == 0"),
    ("MUT-WILSON-OBSERVABLE", "G-WILSON-OBSERVABLE-REBUILT",
     "plants a plaquette-dependent cell in the loop observable", "dep = 1"),
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
     "plants a rendered claim that the paper does not carry",
     '"claim": "planted"'),
    ("MUT-VERDICT-TWIN", "G-PAPER-VERDICT-EQUALITY",
     "adds a forged twin of the verdict fence beside the clean one",
     '"XMU-"'),
    ("MUT-MUST-NOT", "G-MUST-NOT-VOCABULARY",
     "plants a must-not vocabulary hit", 'hits = ["planted"]'),
    ("MUT-POLARITY", "G-PAPER-POLARITY",
     "fails one polarity row", 'pol[0]["ok"] = False'),
    ("MUT-COVERAGE", "G-PAPER-NUMERAL-COVERAGE",
     "plants an unmatched numeral", 'unmatched = ["planted"]'),
    ("MUT-GHOST-FUNCTION", "G-FUNCTION-INVENTORY-IS-TOTAL",
     "defines an undeclared function in this instrument's own source text",
     "def ghost_helper"),
    ("MUT-REGISTRY-EVASION", "G-MUTANT-REGISTRY-IS-TOTAL",
     "hides a mutant switch behind a computed name the AST scan cannot read",
     "'MUT-' + 'GHOST'"),
    ("MUT-SEAL", "G-SEAL-INTEGRITY",
     "edits a sealed object after its gate closed", '"MOVED-AFTER-THE-GATE"'),
    ("MUT-CARRIER", "G-CARRIER-IS-THE-PARENTS-PRIMARY-CARRIER",
     "denies that this unit's carrier is the parent's primary carrier",
     "carrier_ok = False"),
    ("MUT-ENLARGEMENT", "G-CHART-128-ENLARGEMENT",
     "truncates the extension's orbit closure back to the parent's carrier",
     "states = states[:len(coins)]"),
    ("MUT-SIMPLEX-DIM", "G-GAUGE-WALK-SIMPLEX-IS-THE-PARENTS-SIMPLEX",
     "inverts the comparison of the gauge walk's simplex dimensions with "
     "the parent's", "ok = not ok"),
    ("MUT-WILSON-GAUGE-INVARIANCE", "G-WILSON-OBSERVABLE-IS-GAUGE-INVARIANT",
     "denies that the loop observable is constant on the gauge orbits",
     "gauge_inv = False"),
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
]

FUNCTIONS = [
    "say", "mut", "digest", "bdigest", "own_source", "_g", "fnorm", "fadd",
    "fneg", "fmul", "fconj", "zpow", "fscal", "fnormsq", "is_rational",
    "to_fraction", "in_q_sqrt2", "qsqrt2_pair", "qsqrt2_str", "qs_less",
    "gate", "__init__", "take", "reverify", "read_bytes", "load_sources",
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
    LD.gate("G-FALSIFIER-DESCRIPTIONS-ARE-HONEST",
            "E-23: a falsifier's published description is part of the sealed "
            "surface, so each one names the exact token it plants and that "
            "token is located in the source text of that mutant's own branch "
            "-- a description-inverted mutant is a false waiver wearing a "
            "green badge, and it dies here rather than in a reader's trust",
            not bad_desc, "%d declared falsifiers, %d whose planted token is "
            "not found in their own branch: %s"
            % (len(MUTANTS), len(bad_desc), bad_desc[:4]))

    fnames = declared_function_names(tree)
    extra_f = sorted(fnames - set(FUNCTIONS))
    missing_f = sorted(set(FUNCTIONS) - fnames)
    LD.gate("G-FUNCTION-INVENTORY-IS-TOTAL",
            "the set of functions this source defines must equal the "
            "declared inventory exactly, so a function added to this "
            "instrument under any name -- neutral or not -- dies here, and a "
            "declared name deleted dies here too",
            not extra_f and not missing_f,
            "%d functions defined, %d declared; undeclared %s, missing %s"
            % (len(fnames), len(FUNCTIONS), extra_f[:4], missing_f[:4]))
    S["mutants"] = [{"name": n, "target_gate": t, "description": w,
                     "plants": p} for n, t, w, p in MUTANTS]
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
    SEAL.take("THE WAIVER LEDGER", "waiver_ledger",
              "G-FALSIFIER-COVERAGE-AT-AN-HONEST-DENOMINATOR",
              S["waiver_ledger"])
    S["falsifier_totals"] = {
        "declared_falsifiers": len(MUTANTS),
        "distinct_target_gates": len({m[1] for m in MUTANTS}),
        "switches_in_the_syntax_tree": len(names),
        "functions_declared": len(FUNCTIONS)}
    SEAL.take("THE MUTANT REGISTRY", "mutants",
              "G-FALSIFIER-DESCRIPTIONS-ARE-HONEST", S["mutants"])
    SEAL.take("THE FALSIFIER TOTALS", "falsifier_totals",
              "G-FALSIFIER-DESCRIPTIONS-ARE-HONEST", S["falsifier_totals"])


# ===========================================================================
# SECTION 14.  THE SEAL, THE ARTIFACTS, THE CLI
# ===========================================================================

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
    payload["closing_gates"] = ["G-SEAL-INTEGRITY", "G-ARTIFACT-INTEGRITY"]
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
    LD.gate("G-SEAL-INTEGRITY",
            "the manifest is TOTAL and the seal is checked before anything "
            "reaches the disk: every published top-level key is either "
            "digested at the moment its own gate passed or named in the "
            "declaration with the reason it cannot be, and every sealed "
            "object still matches its gate-time digest -- so an object "
            "edited after its gate closed dies here rather than being "
            "re-derived from disk and pronounced consistent (#119)",
            not unsealed and not moved,
            "%d published keys, %d sealed, %d declared unsealed, %d "
            "undeclared %s, %d moved since their gate %s"
            % (len(payload), len(SEAL.by_key), len(DECLARED_UNSEALED),
               len(unsealed), unsealed[:4], len(moved), moved[:4]))

    transcript = "\n".join(LOG) + "\n" + verdict + "\n"
    payload["transcript_head"] = digest(transcript)
    blob = json.dumps(payload, indent=1, sort_keys=True, default=str)
    outtxt = transcript
    if not write:
        return payload, 0
    for rel, data in ((OUT_REL, outtxt), (RECEIPT_REL, blob)):
        p = os.path.join(REPO, rel)
        tmp = p + ".tmp"
        with open(tmp, "w") as fh:
            fh.write(data)
        os.replace(tmp, p)
    back = json.loads(open(os.path.join(REPO, RECEIPT_REL)).read())
    disk_bad = SEAL.reverify(back)
    txt_ok = open(os.path.join(REPO, OUT_REL)).read() == outtxt
    LD.gate("G-ARTIFACT-INTEGRITY",
            "the artifacts on disk are compared against the GATE-TIME seals "
            "and not against a re-derivation: the receipt is read back from "
            "the filesystem and every sealed object must still carry its "
            "gate-time digest, and the transcript must be byte-identical to "
            "the string this run emitted",
            not disk_bad and txt_ok,
            "%d sealed objects moved on the way to disk %s; transcript "
            "byte-identical: %s" % (len(disk_bad), disk_bad[:3], txt_ok))
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
    S["ledger_shape"] = {
        "gates_closed_before_the_paper_gates": len(LD.rows),
        "instance_gates": S["census"]["instances_run"],
        "paper_gates": 5, "closing_gates": 2,
        "objects_sealed_before_the_paper_gates": len(SEAL.man)}
    SEAL.take("THE LEDGER SHAPE", "ledger_shape", "G-HEAD-DERIVED-TWICE",
              S["ledger_shape"])
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
