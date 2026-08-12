#!/usr/bin/env python3
"""SPC / paper-37 -- THE SPECIES TABLE, KINEMATIC HALF: the exact
irreducible-representation census of the measured symmetry structure.

THE QUESTION: which species -- which irreducible representations -- the
measured symmetry groups of this corpus carry, which of them the committed
carriers can host, how they branch along the measured identity lattice, which
composites they reach, and which of them survive the exclusion the occupancy
census selected at the pair grain.

SCOPE, BINDING (the pin): this is the KINEMATIC half only.  Which species CAN
exist -- labels, composites, statistics compatibility.  Which species ARE
realized, and with what values, is SPC-D's question and waits behind POT's
door.  No dynamic claim is licensed here and a wall gate kills the vocabulary.

EXACT ARITHMETIC ONLY.  Character values live in Q(zeta_N) carried as tuples
of fractions.Fraction in the power basis, reduced modulo the N-th cyclotomic
polynomial, which is itself derived by exact integer polynomial division; the
representation is canonical, so tuple equality IS field equality.  The
symmetric-group tables are integer-valued by the Murnaghan-Nakayama rule.  No
float exists in this source and an AST scan of its own syntax tree is a gate;
no logarithm, exponential or square root is called anywhere, and the integer
square root this file needs is written here in integers.

TWO ENGINES, DECLARED: a modular (Dixon) engine that builds a character table
from a finite group given as an explicit element list with a product, and a
combinatorial (Murnaghan-Nakayama) engine for the symmetric groups and their
Young subgroups.  The two are required to AGREE on the symmetric groups small
enough for both, which is this unit's cross-engine gate.

EXIT CONVENTIONS, DISCLOSED (they invert the usual reading): the delivery run
exits 0 when every gate passes and 1 on any refusal, writing nothing;
--selftest exits 0 when EVERY anchor class is fatal; --mutant exits 0 when the
named mutant DIES ON ITS DECLARED TARGET; --all-mutants exits 0 only when all
of them do; an unknown flag or a missing flag argument exits 2.
"""

import ast
import hashlib
import json
import os
import re
import sys
from fractions import Fraction
from itertools import product

UNIT = "SPC / paper-37 -- the species table, kinematic half"
PIN_SHA12 = "7f0b1e9d5071"
SCHEMA = "spc-species-census-1"

QUIET = False
MUT = None
LOG = []


def say(msg=""):
    """--quiet suppresses the TERMINAL ECHO ONLY.  The transcript is a
    published artifact, so it is accumulated whatever the flag says."""
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
    """the instrument's OWN source text, as the AST gates read it."""
    src = open(os.path.abspath(__file__), "rb").read().decode()
    if mut("MUT-GHOST-FUNCTION"):
        src = src + "\n\ndef ghost_helper(S):\n    return Fraction(3, 8)\n"
    if mut("MUT-REGISTRY-EVASION"):
        src = src + "\n\n_gn = 'MUT-' + 'GHOST'\nif mut(_gn):\n    pass\n"
    if mut("MUT-AST-BLIND"):
        src = src + "\n\n_TOLERANCE_FLOAT = 1e-9\n"
    return src


# ===========================================================================
# SECTION 1.  INTEGER HELPERS AND THE EXACT CYCLOTOMIC FIELD
# ===========================================================================
# Nothing here calls a library function that could round.  The integer square
# root is written out because a character degree is recovered from its square
# and must be an exact integer.

def igcd(a, b):
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def ilcm(a, b):
    return a * b // igcd(a, b) if a and b else 0


def ifact(n):
    out = 1
    for k in range(2, n + 1):
        out *= k
    return out


def iprod(xs):
    out = 1
    for x in xs:
        out *= x
    return out


def isqrt_exact(n):
    """the integer square root, by integer bisection -- no float, no sqrt."""
    if n < 0:
        raise ValueError("negative")
    lo, hi = 0, 1
    while hi * hi <= n:
        hi *= 2
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if mid * mid <= n:
            lo = mid
        else:
            hi = mid
    return lo


def prime_factors(n):
    out, d = [], 2
    while d * d <= n:
        while n % d == 0:
            out.append(d)
            n //= d
        d += 1
    if n > 1:
        out.append(n)
    return sorted(set(out))


def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


UNITS_IN_WORDS = ("zero", "one", "two", "three", "four", "five", "six",
                  "seven", "eight", "nine", "ten", "eleven", "twelve",
                  "thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
                  "eighteen", "nineteen")
TENS_IN_WORDS = ("", "", "twenty", "thirty", "forty", "fifty", "sixty",
                 "seventy", "eighty", "ninety")


def numword(k):
    """a non-negative integer below one hundred, spelled.  Every spelled
    numeral this paper delivers is RENDERED through this function from a
    measured value, so a spelled count cannot drift from the run that
    produced it any more than a digit one can (#267)."""
    if k < len(UNITS_IN_WORDS):
        return UNITS_IN_WORDS[k]
    if k % 10 == 0:
        return TENS_IN_WORDS[k // 10]
    return TENS_IN_WORDS[k // 10] + "-" + UNITS_IN_WORDS[k % 10]


NUMBER_WORDS = {}
for _k in range(100):
    NUMBER_WORDS[numword(_k)] = _k
del _k


def poly_divmod_exact(a, b):
    """exact division of integer polynomials, b monic, low-to-high."""
    a = list(a)
    q = [0] * (len(a) - len(b) + 1) if len(a) >= len(b) else []
    for i in range(len(a) - len(b), -1, -1):
        c = a[i + len(b) - 1]
        q[i] = c
        if c:
            for j in range(len(b)):
                a[i + j] -= c * b[j]
    while a and a[-1] == 0:
        a.pop()
    return q, a


_CYC = {}


def cyclotomic(n):
    """Phi_n, DERIVED: x^n - 1 divided by every Phi_d with d a proper
    divisor.  Nothing about the coefficients is typed."""
    if n in _CYC:
        return _CYC[n]
    num = [-1] + [0] * (n - 1) + [1]
    for d in range(1, n):
        if n % d == 0:
            q, r = poly_divmod_exact(num, cyclotomic(d))
            if r:
                raise GateFail("G-CYCLOTOMIC-FIELD :: Phi_%d does not "
                               "divide :: remainder %s" % (d, r))
            num = q
    _CYC[n] = num
    return num


class Cyc:
    """the field Q(zeta_N): tuples of Fractions in the power basis
    1, z, ..., z^(deg-1) reduced modulo Phi_N.  CANONICAL, so tuple equality
    is field equality."""

    def __init__(self, N):
        self.N = N
        self.phi = cyclotomic(N)
        if mut("MUT-FIELD-MODULUS"):
            self.phi = [c + 1 for c in self.phi]
        self.deg = len(self.phi) - 1
        self.zero = tuple([Fraction(0)] * self.deg)
        self.one = tuple([Fraction(1)] + [Fraction(0)] * (self.deg - 1))
        self.pw = []
        cur = list(self.one)
        for _k in range(N):
            self.pw.append(tuple(cur))
            cur = self._reduce([Fraction(0)] + list(cur))

    def _reduce(self, c):
        c = list(c)
        for i in range(len(c) - 1, self.deg - 1, -1):
            k = c[i]
            if k:
                c[i] = Fraction(0)
                for j in range(self.deg):
                    c[i - self.deg + j] -= k * self.phi[j]
        return c[:self.deg]

    def zpow(self, k):
        return self.pw[k % self.N]

    def add(self, a, b):
        return tuple(x + y for x, y in zip(a, b))

    def sub(self, a, b):
        return tuple(x - y for x, y in zip(a, b))

    def scal(self, a, c):
        c = Fraction(c)
        return tuple(x * c for x in a)

    def mul(self, a, b):
        out = [Fraction(0)] * (2 * self.deg - 1)
        for i, x in enumerate(a):
            if x:
                for j, y in enumerate(b):
                    if y:
                        out[i + j] += x * y
        return tuple(self._reduce(out))

    def conj(self, a):
        """complex conjugation, z -> z^{-1}, exact on the basis."""
        out = self.zero
        for i, x in enumerate(a):
            if x:
                out = self.add(out, self.scal(self.zpow(-i), x))
        return out

    def is_zero(self, a):
        return all(x == 0 for x in a)

    def rational(self, a):
        """the value as a Fraction when it is rational, else None."""
        if all(x == 0 for x in a[1:]):
            return a[0]
        return None

    def to_str(self, a):
        r = self.rational(a)
        if r is not None:
            return str(r)
        return "+".join("%s*z^%d" % (x, i) for i, x in enumerate(a) if x)


def cyc_int(F, a):
    """a character value that must be a rational integer."""
    r = F.rational(a)
    if r is None or r.denominator != 1:
        raise GateFail("G-CARRIER-DECOMPOSITION :: %s is not an "
                       "integer" % (F.to_str(a),))
    return int(r)


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
    vouches the values passes.  The manifest is TOTAL."""

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
    ("S-PIN", "v14/note-spc-pin.md", "7f0b1e9d5071",
     "THE PIN, frozen before this instrument existed"),
    ("S-ACT-PAPER", "v14/paper-34-act.md", "d933221780ed",
     "PARENT 1, ACT terminal: the gauge images, the chart groups, the acting "
     "groups at the three grains, the 136 carrier classes and the 80 at the "
     "extension, the odd twist and the price it carries"),
    ("S-ACT-CODE", "v14/code/act_exact.py", "a90559ee0e0f",
     "PARENT 1's instrument -- read for its declared definitions only; "
     "nothing is imported from it"),
    ("S-ACT-RECEIPT", "v14/code/act_receipt.json", "7fd1267bddc7",
     "PARENT 1's receipt: the orbit counts, the group orders, the merged "
     "orbit pairs and the pinned observable this unit re-derives"),
    ("S-AID-PAPER", "v14/paper-33-aid.md", "ecdd3fbf1d06",
     "PARENT 2, AID terminal: the Young-subgroup stabilizer structure, the "
     "measured orbit shapes, the crystallization chain and the "
     "admissibility axis"),
    ("S-AID-RECEIPT", "v14/code/aid_receipt.json", "2dd2a9879984",
     "PARENT 2's receipt: the stabilizer lattice this unit branches along"),
    ("S-OCC-PAPER", "v14/paper-31-occ.md", "0092caa4d9ad",
     "PARENT 3, OCC terminal: the 27-cell carrier, the co-division pair "
     "grain and the shape the exclusion census selected there"),
    ("S-OCC-RECEIPT", "v14/code/occ_receipt.json", "455ddec78dda",
     "PARENT 3's receipt: the carrier-grain leak census this unit's "
     "statistics row is bound to"),
    ("S-SMU-PAPER", "v14/paper-27-smu.md", "6df0db523d32",
     "PARENT 4, SMU terminal: the invariant simplexes and the conserved "
     "price the species census re-reads"),
    ("S-R5-PAPER", "v14/paper-18-gauge-rung.md", "62cfe5689d2c",
     "PARENT 5, R5 terminal: the arena -- the coin family, the lattice, the "
     "chart group and its declared extension"),
    ("S-CRB-PAPER", "v14/paper-06-stochastic-split.md", "c350caab17ee",
     "the stochastic-split terminal: the identity arena's symmetry "
     "inventory, where the order-108 arena group was measured"),
    ("S-CRB-CODE", "v14/code/crb_stochastic_exact.py", "5f2a54ea8a98",
     "its instrument, where the AG(2,3) link declaration and the point "
     "group of the declared link set are defined -- read for its declared "
     "definitions only"),
]

PAPER_REL = "v14/paper-37-spc.md"
OUT_REL = "v14/code/spc_output.txt"
RECEIPT_REL = "v14/code/spc_receipt.json"

BANNED_NAMES = ["subprocess", "numpy", "random", "scipy", "git", "math",
                "decimal", "statistics"]
BANNED_CALLS = ["system", "popen", "check_output", "urlopen", "log", "exp",
                "sqrt", "float", "pow10"]


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
        if mut("MUT-SOURCE-DRIFT") and name == "S-ACT-PAPER":
            d = "000000000000"
        rows.append({"name": name, "path": rel, "pinned": sha, "measured": d,
                     "ok": (d == sha) if sha else (b is not None),
                     "pinned_by_the_pin": bool(sha), "what": what})
        got[name] = b
    return got, rows


def measure_provenance(S):
    src, rows = load_sources()
    bad = [r for r in rows if not r["ok"]]
    LD.gate("G-SOURCE-BYTES",
            "every pinned source is read at its declared path and its bytes "
            "must carry the digest this instrument declares -- the digests "
            "the PIN itself fixed are compared as equalities, and the "
            "sources the pin names without a digest must be present and are "
            "digested here so that the receipt records exactly which bytes "
            "this run read",
            not bad,
            "%d sources, %d digest-pinned, %d failing %s"
            % (len(rows), sum(1 for r in rows if r["pinned_by_the_pin"]),
               len(bad), [b["name"] for b in bad]))
    S["provenance"] = rows
    SEAL.take("THE PROVENANCE ROWS", "provenance", "G-SOURCE-BYTES", rows)
    S["artifacts"] = {"paper": PAPER_REL, "transcript": OUT_REL,
                      "receipt": RECEIPT_REL,
                      "instrument": "v14/code/spc_exact.py"}
    SEAL.take("THE ARTIFACT PATHS", "artifacts", "G-SOURCE-BYTES",
              S["artifacts"])
    return src


# ---------------------------------------------------------------- path-value
PATH_VALUES = [
    ("PV-ACT-COINS", "S-ACT-RECEIPT", "arena/coins", 640,
     "G-COIN-ARENA-REBUILT", "the coin family, this unit's first carrier"),
    ("PV-ACT-ALPH", "S-ACT-RECEIPT", "arena/alphabet", 25,
     "G-COIN-ARENA-REBUILT", "the coefficient alphabet it is built from"),
    ("PV-ACT-LINKS", "S-ACT-RECEIPT", "arena/links", 32,
     "G-CHART-GROUPS-REBUILT", "the link count, a carrier of its own"),
    ("PV-ACT-SITES", "S-ACT-RECEIPT", "arena/sites", 16,
     "G-CHART-GROUPS-REBUILT", "the site count"),
    ("PV-ACT-PLAQ", "S-ACT-RECEIPT", "arena/plaquettes", 16,
     "G-CHART-GROUPS-REBUILT", "the plaquette count"),
    ("PV-ACT-GAMMA", "S-ACT-RECEIPT", "gamma/order", 16,
     "G-GAMMA-REBUILT", "the coin-map group's order"),
    ("PV-ACT-TWIST", "S-ACT-RECEIPT", "gamma/elementary_twist_order", 8,
     "G-GAMMA-REBUILT", "the elementary twist's order"),
    ("PV-ACT-CHART32", "S-ACT-RECEIPT", "chart/anchored_order", 32,
     "G-CHART-GROUPS-REBUILT", "the anchored chart group's order"),
    ("PV-ACT-CHART128", "S-ACT-RECEIPT", "chart/extension_order", 128,
     "G-CHART-GROUPS-REBUILT", "the extension chart group's order"),
    ("PV-ACT-LORB", "S-ACT-RECEIPT", "chart/link_orbits_anchored", 1,
     "G-CHART-GROUPS-REBUILT", "the chart group is transitive on the links"),
    ("PV-ACT-SORB", "S-ACT-RECEIPT", "chart/site_orbits_anchored", 1,
     "G-CHART-GROUPS-REBUILT", "and on the sites"),
    ("PV-ACT-PORB", "S-ACT-RECEIPT", "chart/plaquette_orbits_anchored", 1,
     "G-CHART-GROUPS-REBUILT", "and on the plaquettes"),
    ("PV-ACT-RES4", "S-ACT-RECEIPT", "residual_gauge/order_anchored", 4,
     "G-GROUP-INVENTORY-ORDERS-RE-DERIVED",
     "the residual gauge group on the carrier at the anchored reading"),
    ("PV-ACT-RES8", "S-ACT-RECEIPT", "residual_gauge/order_extension", 8,
     "G-GROUP-INVENTORY-ORDERS-RE-DERIVED",
     "the same at the extension reading"),
    ("PV-ACT-ORB208", "S-ACT-RECEIPT", "residual_gauge/orbits_anchored", 208,
     "G-CARRIER-ORBITS-TWO-ROUTES",
     "the carrier's gauge orbits at the anchored reading"),
    ("PV-ACT-ORB120", "S-ACT-RECEIPT", "residual_gauge/orbits_extension",
     120, "G-CARRIER-ORBITS-TWO-ROUTES", "the same at the extension"),
    ("PV-ACT-ORB136", "S-ACT-RECEIPT", "form_census/rows/0/orbits", 136,
     "G-CARRIER-ORBITS-TWO-ROUTES",
     "THE 136 CARRIER CLASSES the pin sends this unit to decompose"),
    ("PV-ACT-ORB80", "S-ACT-RECEIPT", "form_census/rows/1/orbits", 80,
     "G-CARRIER-ORBITS-TWO-ROUTES", "and the 80 at the extension"),
    ("PV-ACT-ACTING8", "S-ACT-RECEIPT",
     "form_census/rows/0/acting_group_order", 8, "G-ABOVE-THE-TABLE-CAP",
     "the acting group at the link grain, anchored"),
    ("PV-ACT-ACTING16", "S-ACT-RECEIPT",
     "form_census/rows/1/acting_group_order", 16, "G-ABOVE-THE-TABLE-CAP",
     "the acting group at the link grain, extension"),
    ("PV-ACT-GAUGE512", "S-ACT-RECEIPT",
     "form_census/rows/2/gauge_image_order", 512, "G-ABOVE-THE-TABLE-CAP",
     "the plaquette grain's gauge image, above this unit's table cap"),
    ("PV-ACT-GAUGE4096", "S-ACT-RECEIPT",
     "form_census/rows/4/gauge_image_order", 4096, "G-ABOVE-THE-TABLE-CAP",
     "the site grain's gauge image, above the cap"),
    ("PV-ACT-ACTING1024", "S-ACT-RECEIPT",
     "form_census/rows/2/acting_group_order", 1024, "G-ABOVE-THE-TABLE-CAP",
     "the plaquette acting group, above the cap"),
    ("PV-ACT-ACTING32768", "S-ACT-RECEIPT",
     "form_census/rows/5/acting_group_order", 32768, "G-ABOVE-THE-TABLE-CAP",
     "the largest acting group of the parent's census"),
    ("PV-ACT-MERGED72", "S-ACT-RECEIPT", "price/orbit_pairs_merged_anchored",
     72, "G-THE-ODD-TWIST-SPECIES",
     "the orbit pairs every admissible weight system identifies, anchored"),
    ("PV-ACT-MERGED40", "S-ACT-RECEIPT",
     "price/orbit_pairs_merged_extension", 40, "G-THE-ODD-TWIST-SPECIES",
     "the same at the extension reading"),
    ("PV-ACT-PINNED", "S-ACT-RECEIPT", "falsifier/rows/2/verdict", "PINNED",
     "G-THE-ODD-TWIST-SPECIES",
     "the parent's one pinned observable, whose species this unit names"),
    ("PV-ACT-PINNEDNAME", "S-ACT-RECEIPT", "falsifier/rows/2/observable",
     "OFF-DIAGONAL-QUARTIC-SIGN", "G-THE-ODD-TWIST-SPECIES",
     "its name at the parent's own receipt"),
    ("PV-AID-S9", "S-AID-RECEIPT", "stabilizer/s9_order", 362880,
     "G-GROUP-INVENTORY-ORDERS-RE-DERIVED",
     "the symmetric group on the nine actors, whose species this unit "
     "censuses"),
    ("PV-AID-SHAPE2", "S-AID-RECEIPT",
     "stabilizer/nontrivial_orbit_shapes/1+1+1+1+1+1+1+2", 60,
     "G-IDENTITY-LATTICE-IS-THE-PARENTS",
     "the first measured stabilizer shape and how many prefixes carry it"),
    ("PV-AID-SHAPE4", "S-AID-RECEIPT",
     "stabilizer/nontrivial_orbit_shapes/1+1+1+1+1+2+2", 108,
     "G-IDENTITY-LATTICE-IS-THE-PARENTS", "the second"),
    ("PV-AID-SHAPE8", "S-AID-RECEIPT",
     "stabilizer/nontrivial_orbit_shapes/1+1+1+2+2+2", 270,
     "G-IDENTITY-LATTICE-IS-THE-PARENTS", "the third"),
    ("PV-AID-SHAPE24", "S-AID-RECEIPT",
     "stabilizer/nontrivial_orbit_shapes/1+1+2+2+3", 66,
     "G-IDENTITY-LATTICE-IS-THE-PARENTS", "the fourth"),
    ("PV-AID-SHAPE216", "S-AID-RECEIPT",
     "stabilizer/nontrivial_orbit_shapes/3+3+3", 181,
     "G-IDENTITY-LATTICE-IS-THE-PARENTS",
     "the fifth, and the shape of the four chart histories"),
    ("PV-AID-SHAPE4320", "S-AID-RECEIPT",
     "stabilizer/nontrivial_orbit_shapes/3+6", 18,
     "G-IDENTITY-LATTICE-IS-THE-PARENTS", "the sixth and largest"),
    ("PV-AID-CHART", "S-AID-RECEIPT", "stabilizer/chart_histories", 4,
     "G-IDENTITY-LATTICE-IS-THE-PARENTS",
     "the histories at which identity is not forced"),
    ("PV-AID-FORCED", "S-AID-RECEIPT", "stabilizer/forced_histories", 5852,
     "G-IDENTITY-LATTICE-IS-THE-PARENTS",
     "the histories at which it is -- the admissibility axis's own count"),
    ("PV-AID-CHAIN", "S-AID-RECEIPT",
     "crystallization/stabilizer_order_by_prefix_length_C1/0", 4320,
     "G-CRYSTALLIZATION-CHAIN-IS-NESTED",
     "the first stabilizer order of the measured crystallization chain"),
    ("PV-AID-TIME", "S-AID-RECEIPT",
     "crystallization/constant_on_C1_C2_C1FAN", 5,
     "G-CRYSTALLIZATION-CHAIN-IS-NESTED",
     "the crystallization time the chain reaches triviality at"),
    ("PV-OCC-CELLS", "S-OCC-RECEIPT", "counts/same_site_configurations", 27,
     "G-AG23-ARENA-REBUILT",
     "the 27 same-site configurations, one per carrier cell"),
    ("PV-OCC-ANTI", "S-OCC-RECEIPT",
     "leaks/carrier_grain_antisymmetric_leak_cells", 0,
     "G-OCC-SELECTED-SHAPE",
     "the antisymmetric shape's leak at the carrier grain: none, which is "
     "why exclusion selects there"),
    ("PV-OCC-SYM", "S-OCC-RECEIPT", "leaks/carrier_grain_symmetric_leak_cells",
     81, "G-OCC-SELECTED-SHAPE",
     "the symmetric shape's leak at the same grain"),
    ("PV-OCC-COINS", "S-OCC-RECEIPT",
     "leaks/carrier_grain_symmetric_coins_leaking", 5, "G-OCC-SELECTED-SHAPE",
     "how many of the coin classes it leaks at"),
]


def dig(obj, path):
    cur = obj
    for part in path.split("/"):
        if isinstance(cur, list):
            cur = cur[int(part)]
        else:
            cur = cur[part]
    return cur


def measure_path_values(S, src):
    rows, cache = [], {}
    for aid, sname, path, want, consumer, what in PATH_VALUES:
        if sname not in cache:
            cache[sname] = json.loads(src[sname].decode())
        got = dig(cache[sname], path)
        if mut("MUT-PATH-VALUE") and aid == "PV-ACT-ORB136":
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


# ---------------------------------------------------------------- verbatim
VERBATIM = [
    ("VB-PIN-CENSUS", "S-PIN",
     "for each inventory group, the full character table computed exactly "
     "and gated by two routes (column orthogonality AND row orthogonality "
     "as separate gates; class equation verified)",
     "G-CHARACTER-TABLE-COLUMN-ORTHOGONALITY",
     "the pin's own statement of the census standard"),
    ("VB-PIN-CARRIER", "S-PIN",
     "the 136 carrier classes (80 at the extension) as permutation modules "
     "over the acting groups \u2014 decomposed into irreps EXACTLY",
     "G-CARRIER-DECOMPOSITION", "the heart, as the pin words it"),
    ("VB-PIN-HOMELESS", "S-PIN",
     "which irreps of the abstract groups have NO carrier realization "
     "(label-possible but carrier-homeless \u2014 measured, not argued)",
     "G-CARRIER-HOMELESS-CENSUS",
     "the homelessness question, put by the pin"),
    ("VB-PIN-IDENTITY", "S-PIN",
     "which species survive identity crystallization at the admissibility "
     "axis; the branching computed",
     "G-IDENTITY-BRANCHING-TWO-ROUTES", "the identity layer, put by the pin"),
    ("VB-PIN-SELECTION", "S-PIN",
     "tensor-product decompositions among the carrier-realized species "
     "\u2014 which composites are reachable",
     "G-SELECTION-CLOSURE-CENSUS", "the selection rules, put by the pin"),
    ("VB-PIN-STATISTICS", "S-PIN",
     "OCC's ceiling selected exclusion at the carrier/pair grain \u2014 "
     "which species are compatible with the selected statistics at that "
     "grain", "G-STATISTICS-SPLIT-CENSUS",
     "the statistics tie-in, put by the pin"),
    ("VB-PIN-SCOPE", "S-PIN",
     "this is the KINEMATIC half only \u2014 which species CAN exist "
     "(labels, selection rules, statistics compatibility)",
     "G-MUST-NOT-VOCABULARY", "the scope declaration this unit is held to"),
    ("VB-ACT-ODD", "S-ACT-PAPER",
     "The odd twist is not realisable on this torus",
     "G-THE-ODD-TWIST-SPECIES",
     "the parent's measured fact whose species this unit names"),
    ("VB-ACT-PRICE", "S-ACT-PAPER",
     "72 pairs of gauge orbits at the anchored reading and 40 at the "
     "extension are identified by every admissible weight system",
     "G-THE-ODD-TWIST-SPECIES",
     "the parent's price, which this unit resolves into one species"),
    ("VB-ACT-INVARIANT", "S-ACT-PAPER",
     "A measure is invariant under a group acting on a finite set if and "
     "only if it is constant on the orbits.",
     "G-CARRIER-ORBITS-TWO-ROUTES",
     "the characterisation that makes an orbit count a multiplicity"),
    ("VB-ACT-PARTITION", "S-ACT-PAPER",
     "The partition is the same 136 classes at all three grains",
     "G-THE-CARRIER-SEES-ONE-GROUP",
     "the parent's grain-invariance, which this unit explains by measuring "
     "the group the carrier sees"),
    ("VB-ACT-SIMPLEX", "S-ACT-PAPER",
     "the reachable measures are a proper sub-simplex of the parent's "
     "invariant simplex", "G-CARRIER-DECOMPOSITION",
     "the object whose dimension this unit resolves into species"),
    ("VB-AID-YOUNG", "S-AID-PAPER",
     "the stabilizer is the Young subgroup, its order is the product of the "
     "block factorials, and identity crystallizes exactly when every actor "
     "has its own signature.", "G-IDENTITY-LATTICE-IS-THE-PARENTS",
     "the parent's theorem, which supplies this unit's identity lattice"),
    ("VB-AID-AXIS", "S-AID-PAPER",
     "Every admissible history of this census forces identity",
     "G-CRYSTALLIZATION-CHAIN-IS-NESTED",
     "the admissibility axis, in the parent's own sentence"),
    ("VB-OCC-SELECT", "S-OCC-PAPER",
     "the symmetric shape leaks at 81 cells at 5 of the 6 coin classes and "
     "the antisymmetric shape leaks at 0, so a hard core there would select",
     "G-OCC-SELECTED-SHAPE",
     "the shape the parent's exclusion census selected at the pair grain"),
    ("VB-OCC-CELL", "S-OCC-PAPER",
     "the committed instrument says in its own words what a cell is: the "
     "unordered co-division pair", "G-AG23-ARENA-REBUILT",
     "what the 27-cell carrier is made of"),
    ("VB-CRB-ARENA", "S-CRB-PAPER",
     "the pinned chart group has order 18; the largest group the declared "
     "link set admits has order 108", "G-AG23-ARENA-REBUILT",
     "the identity arena's two groups, at the terminal that measured them"),
    ("VB-CRB-POINT", "S-CRB-CODE",
     "Every invertible integer 2x2 matrix carrying the declared link set "
     "into the signed link set.", "G-AG23-ARENA-REBUILT",
     "the point group's definition, rebuilt here from these words"),
    ("VB-R5-CARRIER", "S-R5-PAPER",
     "The uniform configurations \u2014 one coin repeated on every link "
     "\u2014 are swept exhaustively over the coin alphabet",
     "G-COIN-ARENA-REBUILT", "the carrier this census weighs"),
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


def measure_verbatim(S, src):
    rows = []
    for aid, sname, window, consumer, what in VERBATIM:
        hay = mnorm(src[sname].decode())
        if mut("MUT-VERBATIM") and aid == "VB-OCC-SELECT":
            window = window.replace("would select", "would not select")
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
            "anchor binds QUOTE FIDELITY and not mere existence",
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


def check_the_arithmetic(S):
    """the AST gate: no float anywhere, no banned import, no call to a
    logarithm, an exponential or a square root -- so the exactness of this
    census is a property of the instrument rather than a promise about it."""
    tree = ast.parse(own_source())
    floats, imports, calls = [], [], []
    for n in ast.walk(tree):
        if isinstance(n, ast.Constant) and isinstance(n.value, float):
            floats.append(repr(n.value))
        if isinstance(n, ast.Import):
            for a in n.names:
                if a.name.split(".")[0] in BANNED_NAMES:
                    imports.append(a.name)
        if isinstance(n, ast.ImportFrom):
            if (n.module or "").split(".")[0] in BANNED_NAMES:
                imports.append(n.module)
        if isinstance(n, ast.Call):
            nm = getattr(n.func, "id", None) or getattr(n.func, "attr", None)
            if nm in BANNED_CALLS:
                calls.append(nm)
    LD.gate("G-ARITHMETIC-IS-EXACT",
            "an AST scan of this instrument's own syntax tree is a gate: no "
            "float literal exists in this source at all, no banned module is "
            "imported, and no call to a logarithm, an exponential, a square "
            "root or a float conversion appears anywhere -- the integer "
            "square root a character degree is recovered by is written here "
            "in integers and bisects",
            not floats and not imports and not calls,
            "%d float literals %s; %d banned imports %s; %d banned calls %s"
            % (len(floats), floats[:3], len(imports), imports[:3],
               len(calls), calls[:3]))
    F = Cyc(8)
    lawful = (F.mul(F.zpow(1), F.zpow(7)) == F.one
              and F.zpow(8) == F.one
              and F.conj(F.conj(F.zpow(3))) == F.zpow(3)
              and F.mul(F.zpow(3), F.conj(F.zpow(3))) == F.one
              and F.add(F.zpow(0), F.zpow(4)) == F.zero)
    degs = {str(n): len(cyclotomic(n)) - 1
            for n in (1, 2, 3, 4, 6, 8, 9, 12)}
    want = {"1": 1, "2": 1, "3": 2, "4": 2, "6": 2, "8": 4, "9": 6, "12": 4}
    LD.gate("G-CYCLOTOMIC-FIELD",
            "the field the character values live in is DERIVED and then "
            "TESTED on its own laws: the cyclotomic polynomial is obtained "
            "by exact integer division of x^n - 1 by every proper divisor's "
            "polynomial, its degree is measured against Euler's totient at "
            "eight declared moduli, and the arithmetic must satisfy the "
            "relations that define it -- the primitive root has the declared "
            "order, conjugation is an involution inverting it, and the "
            "canonical form makes tuple equality field equality",
            lawful and degs == want,
            "field laws hold: %s; measured degrees %s against the totients "
            "%s" % (lawful, degs, want))
    S["arithmetic"] = {
        "field": "Q(zeta_N)-AS-FRACTION-TUPLES-IN-THE-POWER-BASIS-REDUCED-"
                 "MODULO-THE-DERIVED-CYCLOTOMIC-POLYNOMIAL",
        "float_literals_in_this_source": len(floats),
        "banned_imports": len(imports), "banned_calls": len(calls),
        "cyclotomic_degrees_measured": degs,
        "equality": "TUPLE-EQUALITY-IS-FIELD-EQUALITY",
        "integer_square_root": "WRITTEN-HERE-BY-INTEGER-BISECTION"}
    SEAL.take("THE ARITHMETIC", "arithmetic", "G-CYCLOTOMIC-FIELD",
              S["arithmetic"])


# ===========================================================================
# SECTION 4.  THE GENERIC FINITE-GROUP ENGINE, AND DIXON'S CHARACTER TABLE
# ===========================================================================
# A group here is an explicit list of hashable elements with a product and an
# identity.  Nothing about any group's order, class number or irrep count is
# typed anywhere: closure, inverses, conjugacy classes and the class
# multiplication coefficients are all measured from the product.

class Group:
    def __init__(self, name, elems, mul, ident, provenance="", carrier=""):
        self.name = name
        self.elems = list(elems)
        self.mul = mul
        self.e = ident
        self.provenance = provenance
        self.carrier = carrier
        self.idx = {g: i for i, g in enumerate(self.elems)}
        self.n = len(self.elems)
        self._inv = None

    def is_closed(self):
        s = set(self.elems)
        if len(s) != self.n or self.e not in s:
            return False
        for a in self.elems:
            for b in self.elems:
                if self.mul(a, b) not in s:
                    return False
        return True

    def inverses(self):
        if self._inv is None:
            inv = {}
            for a in self.elems:
                for b in self.elems:
                    if self.mul(a, b) == self.e:
                        inv[a] = b
                        break
            self._inv = inv
        return self._inv

    def inv(self, a):
        return self.inverses()[a]

    def order_of(self, a):
        k, cur = 1, a
        while cur != self.e:
            cur = self.mul(cur, a)
            k += 1
            if k > self.n:
                raise GateFail("G-GROUP-INVENTORY-ORDERS-RE-DERIVED :: %s "
                               ":: an element has no finite order" % self.name)
        return k

    def exponent(self):
        e = 1
        for a in self.elems:
            e = ilcm(e, self.order_of(a))
        return e

    def conjugacy_classes(self):
        seen, out = set(), []
        inv = self.inverses()
        for a in self.elems:
            if a in seen:
                continue
            cl = set()
            for g in self.elems:
                cl.add(self.mul(self.mul(g, a), inv[g]))
            seen |= cl
            out.append(sorted(cl, key=lambda x: self.idx[x]))
        out.sort(key=lambda c: (len(c), self.idx[c[0]]))
        out.sort(key=lambda c: 0 if c == [self.e] else 1)
        return out


def class_data(G):
    cls = G.conjugacy_classes()
    rep = [c[0] for c in cls]
    size = [len(c) for c in cls]
    where = {}
    for i, c in enumerate(cls):
        for g in c:
            where[g] = i
    inv_class = [where[G.inv(r)] for r in rep]
    return cls, rep, size, where, inv_class


def class_matrices(G, cls, where):
    """M_i[j][k] = a_ijk, the class multiplication coefficients, measured by
    one pass over C_i x G rather than over C_i x C_j x C_k."""
    r = len(cls)
    size = [len(c) for c in cls]
    M = []
    for i in range(r):
        cnt = [[0] * r for _ in range(r)]
        for x in cls[i]:
            for y in G.elems:
                cnt[where[y]][where[G.mul(x, y)]] += 1
        Mi = [[0] * r for _ in range(r)]
        for j in range(r):
            for k in range(r):
                if cnt[j][k] % size[k]:
                    raise GateFail("G-CHARACTER-TABLE-ROW-ORTHOGONALITY "
                                   ":: %s :: a class coefficient is not an "
                                   "integer" % G.name)
                Mi[j][k] = cnt[j][k] // size[k]
        M.append(Mi)
    return M


def gf_rref(rows, p):
    rows = [r[:] for r in rows]
    m = len(rows)
    n = len(rows[0]) if rows else 0
    piv, r0 = [], 0
    for c in range(n):
        pr = None
        for r in range(r0, m):
            if rows[r][c] % p:
                pr = r
                break
        if pr is None:
            continue
        rows[r0], rows[pr] = rows[pr], rows[r0]
        iv = pow(rows[r0][c], p - 2, p)
        rows[r0] = [(x * iv) % p for x in rows[r0]]
        for r in range(m):
            if r != r0 and rows[r][c] % p:
                f = rows[r][c]
                rows[r] = [(rows[r][j] - f * rows[r0][j]) % p
                           for j in range(n)]
        piv.append(c)
        r0 += 1
        if r0 == m:
            break
    return rows[:r0], piv


def gf_nullspace(A, p):
    R, piv = gf_rref(A, p)
    n = len(A[0])
    free = [c for c in range(n) if c not in piv]
    basis = []
    for f in free:
        v = [0] * n
        v[f] = 1
        for i, c in enumerate(piv):
            v[c] = (-R[i][f]) % p
        basis.append(v)
    return basis


def split_eigenspaces(M, basis, p):
    """split a common invariant subspace into eigenspaces of M.  The class
    matrices commute, so the refinement is well defined; a subspace whose
    eigenvalues do not lie in the prime field would stop the run, which is
    the arithmetic condition Dixon's prime is chosen to meet."""
    r = len(M)
    B, piv = gf_rref([b[:] for b in basis], p)
    k = len(B)
    if k <= 1:
        return [basis]

    def coords(v):
        out = [0] * k
        w = v[:]
        for i, c in enumerate(piv):
            out[i] = w[c] % p
            if out[i]:
                w = [(w[j] - out[i] * B[i][j]) % p for j in range(r)]
        if any(x % p for x in w):
            raise GateFail("G-CHARACTER-TABLE-ROW-ORTHOGONALITY :: the "
                           "eigenspace split left the invariant subspace")
        return out

    A = []
    for b in B:
        Mb = [sum(M[i][j] * b[j] for j in range(r)) % p for i in range(r)]
        A.append(coords(Mb))
    out = []
    for lam in range(p):
        NT = [[(A[i][j] - (lam if i == j else 0)) % p for i in range(k)]
              for j in range(k)]
        ns = gf_nullspace(NT, p)
        if ns:
            out.append([[sum(v[i] * B[i][j] for i in range(k)) % p
                         for j in range(r)] for v in ns])
    if sum(len(s) for s in out) != k:
        raise GateFail("G-CHARACTER-TABLE-ROW-ORTHOGONALITY :: the "
                       "eigenvalues do not split over the declared prime")
    return out


def dixon_prime(order, expo):
    """the smallest prime congruent to one modulo the exponent and larger
    than twice the integer square root of the order -- the condition that
    makes the symmetric lift of a character value unambiguous, since a
    character value's Fourier coefficients are bounded by the degree and the
    degree by the square root of the order."""
    p = expo + 1
    while True:
        if is_prime(p) and p > 2 * isqrt_exact(order) + 1:
            return p
        p += expo


def dixon_table(G):
    """THE CHARACTER TABLE, EXACTLY.  Dixon's modular method: the class sums
    generate the centre of the group algebra, their common eigenvectors are
    the central characters, and each character value is recovered from its
    own powers by a finite Fourier inversion whose coefficients are integers
    bounded by the degree -- so the lift out of the prime field is exact."""
    cls, rep, size, where, inv_class = class_data(G)
    r = len(cls)
    m = G.exponent()
    N = G.n
    p = dixon_prime(N, m)
    z = None
    for g in range(2, p):
        h = pow(g, (p - 1) // m, p)
        if all(pow(h, m // q, p) != 1 for q in prime_factors(m)) or m == 1:
            z = h
            break
    if z is None:
        raise GateFail("G-CHARACTER-TABLE-ROW-ORTHOGONALITY :: %s :: no root "
                       "of unity of the right order in the prime field"
                       % G.name)
    M = class_matrices(G, cls, where)
    if mut("MUT-CLASS-MATRIX") and G.name == "ACTING-LINK-8":
        M[1][0][0] = M[1][0][0] + 1
    spaces = [[[1 if i == j else 0 for j in range(r)] for i in range(r)]]
    for i in range(r):
        nxt = []
        for sp in spaces:
            nxt.extend(split_eigenspaces(M[i], sp, p) if len(sp) > 1 else [sp])
        spaces = nxt
        if all(len(s) == 1 for s in spaces):
            break
    if len(spaces) != r:
        raise GateFail("G-CHARACTER-TABLE-ROW-ORTHOGONALITY :: %s :: %d "
                       "eigenspaces of %d classes" % (G.name, len(spaces), r))
    F = Cyc(m)
    table = []
    for sp in spaces:
        w = sp[0][:]
        if not w[0] % p:
            raise GateFail("G-CHARACTER-TABLE-ROW-ORTHOGONALITY :: %s :: a "
                           "central character vanishes on the identity"
                           % G.name)
        iv = pow(w[0], p - 2, p)
        w = [(x * iv) % p for x in w]
        s = 0
        for j in range(r):
            s = (s + w[j] * w[inv_class[j]] * pow(size[j], p - 2, p)) % p
        d2 = (N * pow(s, p - 2, p)) % p
        deg = None
        for d in range(1, isqrt_exact(N) + 1):
            if (d * d - d2) % p == 0:
                deg = d
                break
        if deg is None:
            raise GateFail("G-CHARACTER-TABLE-ROW-ORTHOGONALITY :: %s :: "
                           "no integer degree recovered" % G.name)
        chi_p = [(w[j] * deg * pow(size[j], p - 2, p)) % p for j in range(r)]
        row = []
        for j in range(r):
            nj = G.order_of(rep[j])
            wj = pow(z, m // nj, p)
            powers = []
            gk = G.e
            for _k in range(nj):
                powers.append(chi_p[where[gk]])
                gk = G.mul(gk, rep[j])
            val = F.zero
            for a in range(nj):
                acc = 0
                for k in range(nj):
                    acc += powers[k] * pow(wj, (-a * k) % nj, p)
                acc = (acc * pow(nj, p - 2, p)) % p
                c = acc if acc <= p // 2 else acc - p
                if c:
                    val = F.add(val, F.scal(F.zpow((m // nj) * a), c))
            row.append(val)
        table.append(row)
    table.sort(key=lambda row: (row[0][0], [str(x) for x in row]))
    if mut("MUT-CHARACTER-VALUE") and G.name == "EXT-108":
        table[3] = [table[3][0]] + [F.add(table[3][1], F.one)] + table[3][2:]
    return {"name": G.name, "order": N, "classes": cls, "rep": rep,
            "size": size, "where": where, "inv_class": inv_class,
            "field": F, "table": table, "prime": p, "exponent": m,
            "engine": "DIXON", "identity_class": where[G.e]}


def inner(ct, a, b):
    """the class-function inner product, exactly."""
    F = ct["field"]
    acc = F.zero
    for j in range(len(a)):
        acc = F.add(acc, F.scal(F.mul(a[j], F.conj(b[j])), ct["size"][j]))
    return F.scal(acc, Fraction(1, ct["order"]))


def multiplicities(ct, chi):
    """the decomposition of a character into irreducibles, as integers."""
    out = []
    for row in ct["table"]:
        v = inner(ct, chi, row)
        k = cyc_int(ct["field"], v)
        if k < 0:
            raise GateFail("G-CARRIER-DECOMPOSITION :: %s :: a multiplicity "
                           "is negative" % ct["name"])
        out.append(k)
    return out


def degrees(ct):
    """the degrees, read at the IDENTITY class -- which is the first column
    of an enumerated group's table and the last of a partition-indexed one,
    so the index is carried by the table and never assumed."""
    e = ct["identity_class"]
    return [cyc_int(ct["field"], row[e]) for row in ct["table"]]


def table_gates(ct):
    """the four census gates, each a separate measurement.  The row route is
    taken over the rows the table HAS and the column route over the classes
    the group has, so a table with a species missing still passes the first
    and fails the second -- which is why the two are separate gates and not
    one measurement written twice."""
    F, T = ct["field"], ct["table"]
    r = len(ct["size"])
    rowo = []
    for i in range(len(T)):
        for j in range(len(T)):
            v = inner(ct, T[i], T[j])
            if v != (F.one if i == j else F.zero):
                rowo.append((i, j))
    colo = []
    for j in range(r):
        for k in range(r):
            acc = F.zero
            for i in range(len(T)):
                acc = F.add(acc, F.mul(T[i][j], F.conj(T[i][k])))
            want = F.zero if j != k else F.scal(
                F.one, Fraction(ct["order"], ct["size"][j]))
            if acc != want:
                colo.append((j, k))
    dg = degrees(ct)
    return {"row_orthogonality_failures": len(rowo),
            "column_orthogonality_failures": len(colo),
            "class_equation_holds": sum(ct["size"]) == ct["order"],
            "classes": r, "irreps": len(T),
            "degree_sum_of_squares": sum(d * d for d in dg),
            "degrees_divide_the_order": all(ct["order"] % d == 0 for d in dg),
            "degrees": dg}


# ===========================================================================
# SECTION 5.  THE SYMMETRIC-GROUP ENGINE (MURNAGHAN-NAKAYAMA)
# ===========================================================================
# The second engine.  It never sees a group element: partitions of n index
# both the classes and the irreps, the character values are integers by the
# rim-hook recursion, and the degrees carry an independent route of their own
# in the hook-length formula.

_PART = {}


def partitions(n, maxp=None):
    if maxp is None:
        maxp = n
    key = (n, maxp)
    if key in _PART:
        return _PART[key]
    if n == 0:
        out = [()]
    else:
        out = []
        for k in range(min(n, maxp), 0, -1):
            for rest in partitions(n - k, k):
                out.append((k,) + rest)
    _PART[key] = out
    return out


_RIM = {}


def rim_hooks(lam, k):
    """every way of removing a rim hook of size k, with its height, read off
    the first-column hook lengths."""
    key = (lam, k)
    if key in _RIM:
        return _RIM[key]
    out = []
    l = list(lam)
    r = len(l)
    beta = [l[i] + (r - 1 - i) for i in range(r)]
    bs = set(beta)
    for i in range(r):
        b = beta[i]
        if b - k >= 0 and (b - k) not in bs:
            nb = sorted([x for j, x in enumerate(beta) if j != i] + [b - k],
                        reverse=True)
            ht = sum(1 for x in beta if b - k < x < b)
            nl = [nb[j] - (len(nb) - 1 - j) for j in range(len(nb))]
            out.append((tuple(x for x in nl if x > 0), ht))
    _RIM[key] = out
    return out


_MN = {}


def mn_char(lam, rho):
    """chi^lambda(rho), an integer, by the Murnaghan-Nakayama recursion."""
    key = (lam, rho)
    if key in _MN:
        return _MN[key]
    if not rho:
        v = 1 if not lam else 0
    else:
        v = 0
        for nu, ht in rim_hooks(lam, rho[0]):
            s = -1 if ht % 2 else 1
            v += s * mn_char(nu, rho[1:])
    _MN[key] = v
    return v


def hook_dimension(lam):
    """the independent route to the degree: n! over the product of the hook
    lengths."""
    n = sum(lam)
    conj = [sum(1 for x in lam if x > j) for j in range(lam[0])] if lam else []
    prod = 1
    for i, row in enumerate(lam):
        for j in range(row):
            prod *= (row - j) + (conj[j] - i) - 1
    return ifact(n) // prod


def centralizer_order(rho):
    m = {}
    for p in rho:
        m[p] = m.get(p, 0) + 1
    return iprod([(i ** c) * ifact(c) for i, c in m.items()])


def sym_class_size(n, rho):
    return ifact(n) // centralizer_order(rho)


def sym_table(n):
    """the character table of the symmetric group on n letters, integer
    valued, indexed by partitions in one fixed order."""
    P = partitions(n)
    T = [[mn_char(lam, rho) for rho in P] for lam in P]
    if mut("MUT-MN-VALUE") and n == 9:
        T[5][3] = T[5][3] + 1
    return {"name": "S%d" % n, "order": ifact(n), "parts": P,
            "size": [sym_class_size(n, r) for r in P], "table": T,
            "engine": "MURNAGHAN-NAKAYAMA", "n": n}


def sym_inner(st, a, b):
    s = sum(st["size"][j] * a[j] * b[j] for j in range(len(st["parts"])))
    if s % st["order"]:
        raise GateFail("G-S9-TABLE :: a symmetric-group inner product is not "
                       "an integer")
    return s // st["order"]


def sym_table_gates(st):
    P, T = st["parts"], st["table"]
    r = len(P)
    rowo = sum(1 for i in range(r) for j in range(r)
               if sym_inner(st, T[i], T[j]) != (1 if i == j else 0))
    colo = 0
    for j in range(r):
        for k in range(r):
            s = sum(T[i][j] * T[i][k] for i in range(r))
            want = centralizer_order(P[j]) if j == k else 0
            if s != want:
                colo += 1
    dims = [T[i][P.index(tuple([1] * st["n"]))] for i in range(r)]
    hooks = [hook_dimension(P[i]) for i in range(r)]
    return {"row_orthogonality_failures": rowo,
            "column_orthogonality_failures": colo,
            "class_equation_holds": sum(st["size"]) == st["order"],
            "classes": r, "irreps": r,
            "degree_sum_of_squares": sum(d * d for d in dims),
            "degrees_match_the_hook_length_formula": dims == hooks,
            "integer_valued": all(isinstance(x, int) for row in T
                                  for x in row),
            "degrees": dims}


def young_subgroup(mu):
    """the Young subgroup S_mu as a product of symmetric groups: its classes
    are tuples of cycle types, its irreps tuples of partitions, and its
    characters the products.  Nothing is enumerated as a permutation."""
    facs = [partitions(m) for m in mu]
    cls = [c for c in product(*facs)]
    return {"mu": tuple(mu), "order": iprod([ifact(m) for m in mu]),
            "classes": cls, "irreps": list(cls),
            "engine": "MURNAGHAN-NAKAYAMA-PRODUCT"}


def young_char(ir, cl):
    return iprod([mn_char(a, b) for a, b in zip(ir, cl)])


def young_class_size(mu, cl):
    return iprod([sym_class_size(m, c) for m, c in zip(mu, cl)])


def young_centralizer(cl):
    return iprod([centralizer_order(c) for c in cl])


def young_dim(ir):
    return iprod([hook_dimension(a) if a else 1 for a in ir])


def fuse(cl):
    """the cycle type in the big group of an element of the Young
    subgroup: the merged multiset of the factors' cycle types."""
    out = []
    for c in cl:
        out.extend(c)
    return tuple(sorted(out, reverse=True))


def kostka(lam, mu):
    """the number of semistandard tableaux of shape lambda and content mu,
    counted by peeling one horizontal strip per content value -- a purely
    combinatorial route to the invariant dimension, sharing no code with the
    character tables."""
    memo = {}

    def strips(lam, k):
        out = []

        def gen(i, cur, left):
            if i == len(lam):
                if left == 0:
                    out.append(tuple(x for x in cur if x > 0))
                return
            lo = lam[i + 1] if i + 1 < len(lam) else 0
            for v in range(max(lo, lam[i] - left), lam[i] + 1):
                if i > 0 and v > cur[i - 1]:
                    continue
                gen(i + 1, cur + [v], left - (lam[i] - v))
        gen(0, [], k)
        return out

    def rec(lam, mu):
        key = (lam, mu)
        if key in memo:
            return memo[key]
        if sum(lam) != sum(mu):
            v = 0
        elif not lam:
            v = 1 if not mu else 0
        elif not mu:
            v = 0
        else:
            v = sum(rec(nu, mu[:-1]) for nu in strips(lam, mu[-1]))
        memo[key] = v
        return v
    return rec(tuple(lam), tuple(mu))


# ===========================================================================
# SECTION 6.  THE ARENAS, REBUILT FROM THE PARENTS' DEFINITIONS
# ===========================================================================
# Nothing is imported from any parent's program.  Every object below is built
# from the definitions the parents publish, and every cardinality it produces
# is gated against the parent's own receipt at a named path.

F8 = None


def build_coin_alphabet():
    """R5's coefficient alphabet as ACT declares it: zero together with the
    eighth root of unity at each of the three declared moduli."""
    F = F8
    half = Fraction(1, 2)
    inv_sqrt2 = F.scal(F.add(F.zpow(1), F.zpow(7)), half)
    out, seen = [], set()
    cands = [F.zero]
    for t in range(8):
        cands.append(F.zpow(t))
        cands.append(F.scal(F.zpow(t), half))
        cands.append(F.mul(F.zpow(t), inv_sqrt2))
    for a in cands:
        if a not in seen:
            seen.add(a)
            out.append(a)
    return out


def normsq(a):
    return F8.mul(a, F8.conj(a))


def build_coin_family(alphabet):
    """THE COIN FAMILY, DERIVED: a two-by-two unitary all of whose entries
    lie in the alphabet, enumerated exhaustively over the admissible rows.
    Nothing about the size is typed."""
    F = F8
    rows = [(a, b) for a in alphabet for b in alphabet
            if F.add(normsq(a), normsq(b)) == F.one]
    coins = []
    for (a, b) in rows:
        for (c, d) in rows:
            if F.add(F.mul(a, F.conj(c)), F.mul(b, F.conj(d))) == F.zero:
                coins.append((a, b, c, d))
    if mut("MUT-COIN-FAMILY"):
        coins = coins[:-1]
    return coins


def coin_twist(m, k):
    """the site-diagonal gauge acting on a link's coin by conjugation with a
    diagonal phase; the action depends on the phase difference alone."""
    a, b, c, d = m
    return (a, F8.mul(F8.zpow(k), b), F8.mul(F8.zpow(-k), c), d)


def coin_swap(m):
    """the coin read from the other end of its own domino."""
    a, b, c, d = m
    return (d, c, b, a)


def coin_sector(m):
    a, b, c, d = m
    if b == F8.zero and c == F8.zero:
        return "DIAGONAL"
    if a == F8.zero and d == F8.zero:
        return "ANTIDIAGONAL"
    return "BALANCED"


def quartic_sign(x):
    """the sign of the fourth power of an entry, an exact integer computed in
    the field: zero when the entry is, and otherwise plus or minus one."""
    if x == F8.zero:
        return 0
    q = F8.mul(F8.mul(x, x), F8.mul(x, x))
    r = F8.rational(q)
    if r is None:
        return 0
    return 1 if r > 0 else -1


def perm_compose(a, b):
    return tuple(a[b[i]] for i in range(len(b)))


def close_group(gens, ident):
    """the subgroup generated by a set of permutations, closed by breadth."""
    G = {ident}
    frontier = [ident]
    while frontier:
        nxt = []
        for g in frontier:
            for s in gens:
                h = perm_compose(s, g)
                if h not in G:
                    G.add(h)
                    nxt.append(h)
        frontier = nxt
    return sorted(G)


def union_find_orbits(perms, n):
    """the orbit count by union-find over a generating set -- a computation
    that never evaluates a character, and the second route to every orbit
    number this unit publishes."""
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
    return len({find(i) for i in range(n)})


# ------------------------------------------------------------- the lattice
LAT_L = 4
EDIR = ((1, 0), (0, 1))


def lat_sites():
    return [(x, y) for x in range(LAT_L) for y in range(LAT_L)]


def lat_links():
    return [(s, d) for s in lat_sites() for d in range(2)]


def lat_addv(s, v):
    return ((s[0] + v[0]) % LAT_L, (s[1] + v[1]) % LAT_L)


def lat_boundary(p):
    return (((p, 0), 1), ((lat_addv(p, EDIR[0]), 1), 1),
            ((lat_addv(p, EDIR[1]), 0), -1), ((p, 1), -1))


def point_symmetries(extended):
    if not extended:
        return [(False, 1, 1), (True, 1, 1)]
    return [(sw, sx, sy) for sw in (False, True)
            for sx in (1, -1) for sy in (1, -1)]


def apply_point(g, s):
    sw, sx, sy = g
    x, y = s
    if sw:
        x, y = y, x
    return ((sx * x) % LAT_L, (sy * y) % LAT_L)


def point_on_dir(g, d):
    sw, sx, sy = g
    x, y = EDIR[d]
    if sw:
        x, y = y, x
    x, y = sx * x, sy * y
    if (abs(x), abs(y)) == (1, 0):
        return 0, (1 if x > 0 else -1)
    return 1, (1 if y > 0 else -1)


def transported_link(l, elem):
    """the image of a link under a chart element, with the domino's
    orientation tracked exactly as the parent tracks it: where the point part
    reverses the direction the image is read the other way round and the
    transported coin is the swap conjugate.  The boolean is that reversal."""
    v, g = elem
    s, d = l
    d2, sign = point_on_dir(g, d)
    s2 = lat_addv(apply_point(g, s), v)
    if sign > 0:
        return (s2, d2), False
    return (((s2[0] - EDIR[d2][0]) % LAT_L,
             (s2[1] - EDIR[d2][1]) % LAT_L), d2), True


def plaquette_image(p, elem):
    """the image of a plaquette, read off the image of its own boundary link
    set rather than declared."""
    img = {transported_link(l, elem)[0] for l, _o in lat_boundary(p)}
    for q in lat_sites():
        if {l for l, _o in lat_boundary(q)} == img:
            return q
    raise GateFail("G-CHART-GROUPS-REBUILT :: a plaquette has no image")


def chart_elements(extended):
    return [(v, g) for v in lat_sites() for g in point_symmetries(extended)]


def realisable_constant_twists():
    """which CONSTANT link twists the site-diagonal gauge realises on the
    torus: the phase must close after L steps, measured rather than argued."""
    return [c for c in range(8) if (LAT_L * c) % 8 == 0]


# --------------------------------------------------------- the AG(2,3) arena
AG_L = 3
AG_LINKS = ((1, 0), (0, 1), (1, 1))


def ag_sites():
    return [(a, b) for a in range(AG_L) for b in range(AG_L)]


def ag_cells():
    """the carrier OCC measured: the unordered co-division pair, indexed by
    its base site and its declared direction."""
    return [(x, l) for x in ag_sites() for l in AG_LINKS]


def ag_apply(A, v):
    return ((A[0][0] * v[0] + A[0][1] * v[1]) % AG_L,
            (A[1][0] * v[0] + A[1][1] * v[1]) % AG_L)


def ag_matmul(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2)) % AG_L
                       for j in range(2)) for i in range(2))


AG_IDENT = ((1, 0), (0, 1))
AG_SWAP = ((0, 1), (1, 0))


def ag_point_group():
    """every invertible matrix carrying the declared link set into the signed
    link set: the automorphism group of the declared links, built by
    enumeration and not typed."""
    signed = list(AG_LINKS) + [((-a) % AG_L, (-b) % AG_L) for a, b in AG_LINKS]
    out = set()
    for c1 in signed:
        for c2 in signed:
            A = ((c1[0], c2[0]), (c1[1], c2[1]))
            if (A[0][0] * A[1][1] - A[0][1] * A[1][0]) % AG_L == 0:
                continue
            if all(ag_apply(A, l) in signed for l in AG_LINKS):
                out.add(A)
    if mut("MUT-AG-POINT-GROUP"):
        out = set(sorted(out)[:-1])
    return sorted(out)


def ag_mul(a, b):
    A1, v1 = a
    A2, v2 = b
    return (ag_matmul(A1, A2),
            tuple((ag_apply(A1, v2)[i] + v1[i]) % AG_L for i in range(2)))


AG_E = (AG_IDENT, (0, 0))


def ag_act_cell(g, cell):
    """the action on a cell, exactly as the parent's own interval action: a
    direction sent to the negative of a declared one is read backwards, which
    moves the base site."""
    A, v = g
    x, l = cell
    Al = ag_apply(A, l)
    gx = tuple((ag_apply(A, x)[i] + v[i]) % AG_L for i in range(2))
    if Al in AG_LINKS:
        return (gx, Al)
    nl = ((-Al[0]) % AG_L, (-Al[1]) % AG_L)
    return (tuple((gx[i] - nl[i]) % AG_L for i in range(2)), nl)


def ag_act_site(g, x):
    A, v = g
    return tuple((ag_apply(A, x)[i] + v[i]) % AG_L for i in range(2))


# ===========================================================================
# SECTION 7.  THE CENSUS FUNCTION -- ONE ROUTE FOR EVERY ROW
# ===========================================================================
# Every carrier row of this unit, delivered and synthetic alike, is priced by
# THIS function.  The synthetic arenas of section 9 are groups of their own
# kind: they are put through the same closure test, the same character
# engine, the same decomposition, the same composite census and the same
# statistics census, and no field of any row is written from outside.

_PAIRCACHE = {}


def pair_characters(perm):
    """THE SECOND ROUTE to the two square characters: the fixed multisets and
    the fixed-with-a-swap pairs are COUNTED on the pair set itself, so the
    published split never rests on the one-line character formula alone."""
    if perm in _PAIRCACHE:
        return _PAIRCACHE[perm]
    n = len(perm)
    sym, anti = 0, 0
    for x in range(n):
        gx = perm[x]
        if gx == x:
            sym += 1
            for y in range(x + 1, n):
                if perm[y] == y:
                    sym += 1
                    anti += 1
        elif perm[gx] == x and gx > x:
            sym += 1
            anti -= 1
    _PAIRCACHE[perm] = (sym, anti)
    return sym, anti


def tensor_decompose(ct, i, j):
    """the composite of two species, with a second route: the multiplicity of
    a third species in the product of the first two is also the multiplicity
    of the first in the product of the third with the second's conjugate."""
    F = ct["field"]
    T = ct["table"]
    r = len(ct["size"])
    prod = [F.mul(T[i][c], T[j][c]) for c in range(r)]
    m1 = multiplicities(ct, prod)
    m2 = []
    for k in range(len(T)):
        alt = [F.mul(F.conj(T[j][c]), T[k][c]) for c in range(r)]
        m2.append(cyc_int(F, inner(ct, alt, T[i])))
    return m1, m2


def price_a_census_row(name, carrier, npoints, perms, gens, provenance,
                       G=None, supplied_table=None, group_name=None,
                       order=None, closed=None, distinguished=False):
    """THE PRICING FUNCTION.  It returns a row and a status word; it never
    raises on a measurement, so a synthetic arena that is not a group reaches
    its own outcome word through the code the delivered rows use."""
    gname = group_name if group_name is not None else G.name
    gorder = order if order is not None else G.n
    row = {"row": name, "group": gname, "group_order": gorder,
           "carrier": carrier, "carrier_points": npoints,
           "provenance": provenance}
    if closed is None:
        closed = G.is_closed()
    row["group_is_closed"] = closed
    if not closed:
        row.update({"status": "BLOCKED", "blocked_at": "THE-GROUP-CLOSURE",
                    "irreps": 0, "hosted": 0, "homeless": 0, "classes": 0,
                    "selection_closes": False, "composite_rules": 0,
                    "in_both_shapes": 0, "symmetric_only": 0,
                    "antisymmetric_only": 0, "in_neither_shape": 0})
        return row
    ct = supplied_table if supplied_table is not None else dixon_table(G)
    tg = table_gates(ct)
    row["classes"] = tg["classes"]
    row["irreps"] = tg["irreps"]
    row["degrees"] = tg["degrees"]
    if not tg["class_equation_holds"] or tg["degree_sum_of_squares"] != gorder:
        row.update({"status": "BLOCKED", "blocked_at": "THE-CLASS-EQUATION",
                    "hosted": 0, "homeless": 0, "selection_closes": False,
                    "composite_rules": 0, "in_both_shapes": 0,
                    "symmetric_only": 0, "antisymmetric_only": 0,
                    "in_neither_shape": 0})
        return row
    routes = {"by_closure": gorder, "by_the_class_equation": sum(ct["size"]),
              "by_the_degree_sum": tg["degree_sum_of_squares"]}
    if len(perms) == gorder:
        orb, frontier = {0}, [0]
        while frontier:
            nxt = []
            for x in frontier:
                for g in perms:
                    y = perms[g][x]
                    if y not in orb:
                        orb.add(y)
                        nxt.append(y)
            frontier = nxt
        stab = sum(1 for g in perms if perms[g][0] == 0)
        routes["by_orbit_stabilizer"] = len(orb) * stab
    row["order_routes"] = routes
    row["order_routes_that_agree"] = sum(1 for v in routes.values()
                                         if v == gorder)
    row["order_routes_taken"] = len(routes)
    F = ct["field"]
    pi = []
    for rp in ct["rep"]:
        p = perms[rp]
        pi.append(F.scal(F.one, sum(1 for x in range(npoints) if p[x] == x)))
    mult = multiplicities(ct, pi)
    if mut("MUT-CARRIER-MULT") and name == "COIN-640-UNDER-ACTING-LINK-8":
        mult = [m + 1 for m in mult]
    row["multiplicities"] = mult
    row["dimension_check"] = sum(m * d for m, d in zip(mult, tg["degrees"]))
    triv = [k for k, r in enumerate(ct["table"]) if all(x == F.one for x in r)]
    row["trivial_species_index"] = triv[0] if triv else -1
    row["orbits_by_the_character"] = mult[triv[0]] if triv else -1
    row["orbits_by_union_find"] = union_find_orbits(gens, npoints)
    row["hosted"] = sum(1 for m in mult if m > 0)
    row["homeless"] = sum(1 for m in mult if m == 0)
    row["homeless_species"] = [k for k, m in enumerate(mult) if m == 0]
    hosted = [k for k, m in enumerate(mult) if m > 0]
    rules, routefail = 0, 0
    exits = set()
    composites = []
    for a in hosted:
        for b in hosted:
            m1, m2 = tensor_decompose(ct, a, b)
            if m1 != m2:
                routefail += 1
            if sum(m * d for m, d in zip(m1, tg["degrees"])) \
                    != tg["degrees"][a] * tg["degrees"][b]:
                routefail += 1
            for k, m in enumerate(m1):
                if m > 0:
                    rules += 1
                    if k not in hosted:
                        exits.add(k)
            if distinguished:
                composites.append({
                    "left": a, "right": b,
                    "composite_species": [k for k, m in enumerate(m1)
                                          if m > 0],
                    "multiplicities": [m for m in m1 if m > 0],
                    "exits_the_hosted_set":
                        any(m > 0 and k not in hosted
                            for k, m in enumerate(m1))})
    if mut("MUT-SELECTION"):
        exits = set()
    row["composite_rules"] = rules
    row["composite_route_disagreements"] = routefail
    row["species_the_composites_exit_to"] = sorted(exits)
    row["selection_closes"] = not exits
    if distinguished:
        row["the_composite_table"] = composites
    sym, anti, two_route_fail = [], [], 0
    for rp in ct["rep"]:
        p = perms[rp]
        c1 = sum(1 for x in range(npoints) if p[x] == x)
        p2 = perm_compose(p, p)
        c2 = sum(1 for x in range(npoints) if p2[x] == x)
        s_formula = Fraction(c1 * c1 + c2, 2)
        a_formula = Fraction(c1 * c1 - c2, 2)
        s_count, a_count = pair_characters(p)
        if mut("MUT-STATISTICS-ROUTE") and name == "CELL-27-UNDER-EXT-108":
            s_count = s_count + 1
        if s_formula != s_count or a_formula != a_count:
            two_route_fail += 1
        sym.append(F.scal(F.one, s_formula))
        anti.append(F.scal(F.one, a_formula))
    ms = multiplicities(ct, sym)
    ma = multiplicities(ct, anti)
    row["symmetric_multiplicities"] = ms
    row["antisymmetric_multiplicities"] = ma
    row["statistics_route_disagreements"] = two_route_fail
    row["symmetric_dimension"] = sum(m * d for m, d in zip(ms, tg["degrees"]))
    row["antisymmetric_dimension"] = sum(m * d
                                         for m, d in zip(ma, tg["degrees"]))
    row["in_both_shapes"] = sum(1 for a, b in zip(ms, ma) if a > 0 and b > 0)
    row["symmetric_only"] = sum(1 for a, b in zip(ms, ma) if a > 0 and b == 0)
    row["antisymmetric_only"] = sum(1 for a, b in zip(ms, ma)
                                    if a == 0 and b > 0)
    row["in_neither_shape"] = sum(1 for a, b in zip(ms, ma)
                                  if a == 0 and b == 0)
    row["compatible_with_the_selected_shape"] = sum(1 for b in ma if b > 0)
    row["table_gates"] = tg
    row["status"] = "MEASURED"
    row["blocked_at"] = ""
    row["_ct"] = ct
    return row


def row_gate_failures(row):
    """the per-object predicates every measured row must satisfy: the gate
    binds the OBJECT and never an aggregate (#87)."""
    if row["status"] != "MEASURED":
        return ["BLOCKED"]
    bad = []
    tg = row["table_gates"]
    if tg["row_orthogonality_failures"]:
        bad.append("ROW-ORTHOGONALITY")
    if tg["column_orthogonality_failures"]:
        bad.append("COLUMN-ORTHOGONALITY")
    if not tg["class_equation_holds"]:
        bad.append("CLASS-EQUATION")
    if tg["degree_sum_of_squares"] != row["group_order"]:
        bad.append("DEGREE-SUM")
    if row["order_routes_that_agree"] != row["order_routes_taken"]:
        bad.append("ORDER-ROUTES")
    if tg["classes"] != tg["irreps"]:
        bad.append("CLASSES-VERSUS-IRREPS")
    if not tg["degrees_divide_the_order"]:
        bad.append("DEGREES-DIVIDE")
    if row["dimension_check"] != row["carrier_points"]:
        bad.append("DIMENSION")
    if row["orbits_by_the_character"] != row["orbits_by_union_find"]:
        bad.append("ORBITS-TWO-ROUTES")
    if row["hosted"] + row["homeless"] != row["irreps"]:
        bad.append("HOSTED-PLUS-HOMELESS")
    if row["composite_route_disagreements"]:
        bad.append("COMPOSITE-TWO-ROUTES")
    if row["statistics_route_disagreements"]:
        bad.append("STATISTICS-TWO-ROUTES")
    n = row["carrier_points"]
    if row["symmetric_dimension"] != n * (n + 1) // 2:
        bad.append("SYMMETRIC-DIMENSION")
    if row["antisymmetric_dimension"] != n * (n - 1) // 2:
        bad.append("ANTISYMMETRIC-DIMENSION")
    if (row["in_both_shapes"] + row["symmetric_only"]
            + row["antisymmetric_only"] + row["in_neither_shape"]
            != row["irreps"]):
        bad.append("STATISTICS-PARTITION")
    return bad


# ===========================================================================
# SECTION 8.  THE ARENAS AND THE INVENTORY
# ===========================================================================

def build_the_arenas(S, pv):
    """the two arenas this corpus measured symmetries on, rebuilt from the
    parents' own definitions."""
    globals()["F8"] = Cyc(8)
    alph = build_coin_alphabet()
    coins = build_coin_family(alph)
    sectors = {}
    for m in coins:
        sectors[coin_sector(m)] = sectors.get(coin_sector(m), 0) + 1
    n = len(coins)
    LD.gate("G-COIN-ARENA-REBUILT",
            "the gauge arena is rebuilt from its own definitions rather than "
            "read: the coefficient alphabet is enumerated, the coin family "
            "is the exhaustive set of unitaries over it, and both "
            "cardinalities are gated against the parent's receipt at named "
            "paths BEFORE anything is built on them -- so this census weighs "
            "the carrier the parents weighed",
            len(alph) == pv["PV-ACT-ALPH"] and n == pv["PV-ACT-COINS"]
            and sum(sectors.values()) == n,
            "alphabet %d, coins %d, sectors %s"
            % (len(alph), n, sorted(sectors.items())))
    ident = tuple(range(n))
    cidx = {m: i for i, m in enumerate(coins)}
    tw = [tuple(cidx[coin_twist(m, k)] for m in coins) for k in range(8)]
    sw = tuple(cidx[coin_swap(m)] for m in coins)
    if mut("MUT-GAMMA"):
        sw = ident
    gamma = close_group([tw[1], sw], ident)
    tw_order, acc = 1, tw[1]
    while acc != ident:
        acc = perm_compose(acc, tw[1])
        tw_order += 1
    LD.gate("G-GAMMA-REBUILT",
            "the coin-map group -- the group every symmetry of this arena "
            "acts on a local datum through -- is closed under composition, "
            "its order is MEASURED by closure rather than typed, and the "
            "elementary twist's own order is measured beside it, both "
            "against the parent's receipt",
            len(gamma) == pv["PV-ACT-GAMMA"]
            and tw_order == pv["PV-ACT-TWIST"],
            "the coin-map group has order %d and the elementary twist order "
            "%d" % (len(gamma), tw_order))
    S["coin_arena"] = {
        "alphabet": len(alph), "coins": n, "sectors": sectors,
        "coin_map_group_order": len(gamma),
        "elementary_twist_order": tw_order,
        "the_carrier": "THE-PARENTS-640-UNIFORM-CONFIGURATIONS",
        "field": "Q(zeta_8)"}
    SEAL.take("THE COIN ARENA", "coin_arena", "G-GAMMA-REBUILT",
              S["coin_arena"])
    S["_coins"] = coins
    S["_cidx"] = cidx
    S["_tw"] = tw
    S["_sw"] = sw
    S["_gamma"] = gamma
    S["_ident"] = ident

    sites = ag_sites()
    cells = ag_cells()
    pg = ag_point_group()
    trans = [(AG_IDENT, v) for v in sites]
    chart = [(A, v) for A in (AG_IDENT, AG_SWAP) for v in sites]
    ext = [(A, v) for A in pg for v in sites]
    LD.gate("G-AG23-ARENA-REBUILT",
            "the identity arena is rebuilt the same way: the nine sites, the "
            "three declared link directions and the twenty-seven cells -- "
            "one per co-division pair, at the count the occupancy terminal "
            "published -- are enumerated here, the point group is built as "
            "the maximal set of matrices carrying the declared link set into "
            "its own signed closure, and the arena group is that point group "
            "times the translations",
            len(sites) == 9 and len(cells) == pv["PV-OCC-CELLS"]
            and len(pg) == 12 and len(ext) == 108 and len(chart) == 18
            and len(trans) == 9,
            "%d sites, %d cells, point group %d, arena group %d, chart %d, "
            "translations %d" % (len(sites), len(cells), len(pg), len(ext),
                                 len(chart), len(trans)))
    S["identity_arena"] = {
        "sites": len(sites), "declared_link_directions": len(AG_LINKS),
        "cells": len(cells), "point_group_order": len(pg),
        "arena_group_order": len(ext), "chart_group_order": len(chart),
        "translation_group_order": len(trans),
        "what_a_cell_is": "THE-UNORDERED-CO-DIVISION-PAIR"}
    SEAL.take("THE IDENTITY ARENA", "identity_arena", "G-AG23-ARENA-REBUILT",
              S["identity_arena"])
    S["_ag"] = {"sites": sites, "cells": cells, "trans": trans,
                "chart": chart, "ext": ext, "point_group": pg}

    links = lat_links()
    lidx = {l: i for i, l in enumerate(links)}
    sidx = {s: i for i, s in enumerate(lat_sites())}
    charts = {}
    for extended, nm in ((False, "CHART-32"), (True, "CHART-128")):
        els = chart_elements(extended)
        if mut("MUT-CHART") and nm == "CHART-32":
            els = els[:1]
        lp = [tuple(lidx[transported_link(l, e)[0]] for l in links)
              for e in els]
        sp = {}
        pp = {}
        for e, p in zip(els, lp):
            sp[p] = tuple(sidx[lat_addv(apply_point(e[1], s), e[0])]
                          for s in lat_sites())
            pp[p] = tuple(sidx[plaquette_image(q, e)] for q in lat_sites())
        charts[nm] = {"declared_elements": len(els), "link": sorted(set(lp)),
                      "site": sp, "plaq": pp, "faithful": len(set(lp)) == len(els)}
    o32 = len(charts["CHART-32"]["link"])
    o128 = len(charts["CHART-128"]["link"])
    lorb = union_find_orbits(charts["CHART-32"]["link"], len(links))
    sorb = union_find_orbits(list(charts["CHART-32"]["site"].values()), 16)
    porb = union_find_orbits(list(charts["CHART-32"]["plaq"].values()), 16)
    LD.gate("G-CHART-GROUPS-REBUILT",
            "both declared chart readings are rebuilt and their action is "
            "MEASURED on all three of the arena's own carriers: the action "
            "on the links is faithful, so the group IS its image there; the "
            "anchored group carries the parent's order and the extension is "
            "four times it; and the group is transitive on the links, on the "
            "sites and on the plaquettes -- one measured orbit count per "
            "grain, each gated against the parent's receipt",
            o32 == pv["PV-ACT-CHART32"] and o128 == pv["PV-ACT-CHART128"]
            and charts["CHART-32"]["faithful"]
            and charts["CHART-128"]["faithful"]
            and len(links) == pv["PV-ACT-LINKS"]
            and lorb == pv["PV-ACT-LORB"] and sorb == pv["PV-ACT-SORB"]
            and porb == pv["PV-ACT-PORB"],
            "chart orders %d and %d, both faithful on the links; %d links; "
            "orbits %d link, %d site, %d plaquette"
            % (o32, o128, len(links), lorb, sorb, porb))
    S["_charts"] = charts
    S["_links"] = links
    S["chart_action"] = {
        "link_orbits_anchored": lorb, "site_orbits_anchored": sorb,
        "plaquette_orbits_anchored": porb,
        "anchored_order": o32, "extension_order": o128,
        "the_action_on_the_links_is_faithful": True}
    SEAL.take("THE CHART ACTION", "chart_action", "G-CHART-GROUPS-REBUILT",
              S["chart_action"])


# ------------------------------------------------- the stencils, above the cap
def stencil_of(grain):
    links = lat_links()
    if grain == "LINK":
        return [links[0]]
    if grain == "PLAQUETTE":
        return [l for l, _o in lat_boundary(lat_sites()[0])]
    x = lat_sites()[0]
    return [(x, 0), (x, 1), (((x[0] - 1) % LAT_L, x[1]), 0),
            ((x[0], (x[1] - 1) % LAT_L), 1)]


def link_ends(l):
    s, d = l
    return s, lat_addv(s, EDIR[d])


def gauge_image_of(stencil, twidx):
    """which tuples of coin-maps the site-diagonal gauge realises on a
    stencil's links, MEASURED by enumerating the site phases the stencil
    touches and reading off each link's own twist."""
    ss = sorted({s for l in stencil for s in link_ends(l)})
    out = set()
    for th in product(range(8), repeat=len(ss)):
        thm = dict(zip(ss, th))
        out.add(tuple(twidx[(thm[link_ends(l)[0]] - thm[link_ends(l)[1]]) % 8]
                      for l in stencil))
    return sorted(out)


def chart_stabilizer_of(stencil, extended, swap_i, ident_i):
    """the chart elements carrying the stencil's link set to itself, with the
    slot permutation and the swap conjugations they impose."""
    Sl = list(stencil)
    out = []
    for e in chart_elements(extended):
        img, ok = {}, True
        for i, l in enumerate(Sl):
            im, rev = transported_link(l, e)
            if im not in Sl:
                ok = False
                break
            img[i] = (Sl.index(im), rev)
        if not ok:
            continue
        perm = [None] * len(Sl)
        cm = [None] * len(Sl)
        for i in range(len(Sl)):
            j, rev = img[i]
            perm[j] = i
            cm[j] = swap_i if rev else ident_i
        out.append((tuple(perm), tuple(cm)))
    return out


def stencil_action_mul(gmul, a, b):
    """a after b, on data indexed by stencil slots -- the parent's own
    composition law for the acting group."""
    ap, ac = a
    bp, bc = b
    n = len(ap)
    return (tuple(bp[ap[j]] for j in range(n)),
            tuple(gmul[ac[j]][bc[ap[j]]] for j in range(n)))


def measure_the_acting_groups(S, pv):
    """MEASUREMENT ONE, the part that reaches above this unit's table cap.
    The acting group at every declared grain and reading is REBUILT and its
    order re-derived as the number of distinct ACTIONS, and the group the
    CARRIER itself sees is measured beside it: on a uniform configuration the
    slot permutation drops out, so what identifies two coins is the tuple of
    coin maps alone, and the subgroup that tuple ranges over is the same at
    every grain.  That is why the carrier's species census is complete at all
    six rows even though four of the six groups are far above the cap."""
    coins, tw, sw, gamma = S["_coins"], S["_tw"], S["_sw"], S["_gamma"]
    gidx = {g: i for i, g in enumerate(gamma)}
    gmul = [[gidx[perm_compose(a, b)] for b in gamma] for a in gamma]
    twidx = [gidx[t] for t in tw]
    swap_i, ident_i = gidx[sw], gidx[S["_ident"]]
    ncoins = len(coins)
    rows = []
    for grain in ("LINK", "PLAQUETTE", "SITE"):
        st = stencil_of(grain)
        gi = gauge_image_of(st, twidx)
        if mut("MUT-ABOVE-CAP"):
            gi = gi[:-1]
        for extended, reading in ((False, "ANCHORED"), (True, "EXTENSION")):
            stb = chart_stabilizer_of(st, extended, swap_i, ident_i)
            acts = set()
            for s in stb:
                for g in gi:
                    acts.add(stencil_action_mul(
                        gmul, s, (tuple(range(len(st))), g)))
            acts = sorted(acts)
            diag = sorted({c[0] for _p, c in acts
                           if all(x == c[0] for x in c)})
            dperms = [gamma[c] for c in diag]
            dclosed = all(perm_compose(a, b) in set(dperms)
                          for a in dperms for b in dperms)
            par = list(range(ncoins))

            def find(a, _par=par):
                while _par[a] != a:
                    _par[a] = _par[_par[a]]
                    a = _par[a]
                return a
            for _p, c in acts:
                maps = [gamma[k] for k in c]
                for x in range(ncoins):
                    y = maps[0][x]
                    if all(m[x] == y for m in maps):
                        ra, rb = find(x), find(y)
                        if ra != rb:
                            par[ra] = rb
            induced = len({find(x) for x in range(ncoins)})
            if mut("MUT-CARRIER-SEES") and grain == "SITE" and extended:
                diag = diag[:-1]
            rows.append({
                "grain": grain, "reading": reading,
                "gauge_image_order": len(gi),
                "chart_stabilizer_order": len(stb),
                "acting_group_order": len(acts),
                "the_group_the_carrier_sees": len(diag),
                "the_group_the_carrier_sees_is_closed": dclosed,
                "induced_classes_on_the_carrier": induced,
                "orbits_of_the_group_the_carrier_sees":
                    union_find_orbits(dperms, ncoins)})
    by = {(r["grain"], r["reading"]): r for r in rows}
    anch = [r for r in rows if r["reading"] == "ANCHORED"]
    ext = [r for r in rows if r["reading"] == "EXTENSION"]
    ok = (by[("LINK", "ANCHORED")]["acting_group_order"]
          == pv["PV-ACT-ACTING8"]
          and by[("LINK", "EXTENSION")]["acting_group_order"]
          == pv["PV-ACT-ACTING16"]
          and by[("PLAQUETTE", "ANCHORED")]["gauge_image_order"]
          == pv["PV-ACT-GAUGE512"]
          and by[("SITE", "ANCHORED")]["gauge_image_order"]
          == pv["PV-ACT-GAUGE4096"]
          and by[("PLAQUETTE", "ANCHORED")]["acting_group_order"]
          == pv["PV-ACT-ACTING1024"]
          and by[("SITE", "EXTENSION")]["acting_group_order"]
          == pv["PV-ACT-ACTING32768"])
    LD.gate("G-ABOVE-THE-TABLE-CAP",
            "the four acting groups above this unit's declared table cap are "
            "REBUILT and their orders re-derived as the number of distinct "
            "actions on the stencil datum, gated against the parent's "
            "receipt row by row -- so the inventory's largest orders are "
            "measured here and not copied",
            ok, "acting group orders %s; gauge image orders %s"
            % ([r["acting_group_order"] for r in rows],
               sorted({r["gauge_image_order"] for r in rows})))
    seen_a = {r["the_group_the_carrier_sees"] for r in anch}
    seen_e = {r["the_group_the_carrier_sees"] for r in ext}
    ind_a = {r["induced_classes_on_the_carrier"] for r in anch}
    ind_e = {r["induced_classes_on_the_carrier"] for r in ext}
    orb_ok = all(r["induced_classes_on_the_carrier"]
                 == r["orbits_of_the_group_the_carrier_sees"] for r in rows)
    LD.gate("G-THE-CARRIER-SEES-ONE-GROUP",
            "THE SCOPE-CLOSING MEASUREMENT: at every one of the six declared "
            "(grain, reading) rows the subgroup of coin maps a UNIFORM "
            "configuration can be moved by is the same group -- of order "
            "eight at the anchored reading and sixteen at the extension -- "
            "it is closed, and the partition it induces on the carrier is "
            "exactly the partition the whole acting group induces there, at "
            "the parent's own two counts.  So the species census on this "
            "carrier is COMPLETE at all six rows even though four of the six "
            "acting groups stand above the table cap: the carrier cannot "
            "tell them apart from the two groups whose tables are computed",
            len(seen_a) == 1 and len(seen_e) == 1 and orb_ok
            and ind_a == {pv["PV-ACT-ORB136"]}
            and ind_e == {pv["PV-ACT-ORB80"]}
            and all(r["the_group_the_carrier_sees_is_closed"] for r in rows),
            "the group the carrier sees has order %s at the anchored rows "
            "and %s at the extension rows; induced classes %s and %s; orbit "
            "route agrees at %d of %d rows"
            % (sorted(seen_a), sorted(seen_e), sorted(ind_a), sorted(ind_e),
               sum(1 for r in rows
                   if r["induced_classes_on_the_carrier"]
                   == r["orbits_of_the_group_the_carrier_sees"]), len(rows)))
    S["acting_groups"] = {"rows": rows, "table_cap": TABLE_CAP,
                          "groups_above_the_cap":
                              sum(1 for r in rows
                                  if r["acting_group_order"] > TABLE_CAP)}
    SEAL.take("THE ACTING GROUPS", "acting_groups",
              "G-THE-CARRIER-SEES-ONE-GROUP", S["acting_groups"])


TABLE_CAP = 128


# ===========================================================================
# SECTION 9.  THE TWO ENGINES MEET
# ===========================================================================

def ct_from_sym(st):
    """the symmetric-group table in the shape every downstream measurement
    reads, over the rational field -- so one set of inner products, one
    decomposition routine and one composite census serve both engines."""
    F = Cyc(1)
    P = st["parts"]
    return {"name": st["name"], "order": st["order"], "classes": P,
            "rep": P, "size": st["size"],
            "inv_class": list(range(len(P))),
            "where": {p: i for i, p in enumerate(P)},
            "field": F,
            "table": [[F.scal(F.one, v) for v in row] for row in st["table"]],
            "prime": 0, "exponent": 0, "engine": st["engine"],
            "identity_class": P.index(tuple([1] * st["n"])),
            "labels": ["+".join(str(x) for x in p) for p in P]}


def ct_from_young(Y):
    """the Young subgroup's table: the Kronecker product of its factors'
    tables, built here rather than enumerated as permutations."""
    F = Cyc(1)
    cls = Y["classes"]
    return {"name": "YOUNG-%d" % Y["order"], "order": Y["order"],
            "classes": cls, "rep": cls,
            "size": [young_class_size(Y["mu"], c) for c in cls],
            "inv_class": list(range(len(cls))),
            "where": {c: i for i, c in enumerate(cls)},
            "field": F,
            "table": [[F.scal(F.one, young_char(ir, cl)) for cl in cls]
                      for ir in Y["irreps"]],
            "prime": 0, "exponent": 0, "engine": Y["engine"],
            "identity_class": cls.index(tuple(tuple([1] * m)
                                              for m in Y["mu"])),
            "labels": ["|".join("+".join(str(x) for x in p) for p in c)
                       for c in cls]}


def sym_group_as_permutations(n):
    """S_n as an explicit permutation group, for the cross-engine gate."""
    els = sorted(product(*[range(n)] * n))
    els = [e for e in els if len(set(e)) == n]
    return Group("S%d-ENUMERATED" % n, els, perm_compose,
                 tuple(range(n)), "the cross-engine control", "POINTS-%d" % n)


def cycle_type_of(p):
    seen = [False] * len(p)
    out = []
    for i in range(len(p)):
        if seen[i]:
            continue
        k, j = 0, i
        while not seen[j]:
            seen[j] = True
            j = p[j]
            k += 1
        out.append(k)
    return tuple(sorted(out, reverse=True))


def measure_the_two_engines(S):
    """the cross-engine gate: on the symmetric groups small enough for both,
    the modular engine and the combinatorial one must return the SAME table
    -- matched class by class through the cycle type and row by row as a
    multiset, with no row order assumed."""
    rows = []
    bad = []
    for n in (2, 3, 4):
        G = sym_group_as_permutations(n)
        ct = dixon_table(G)
        F = ct["field"]
        dx = sorted(tuple(cyc_int(F, row[j]) for j in sorted(
            range(len(ct["rep"])),
            key=lambda k: cycle_type_of(ct["rep"][k])))
            for row in ct["table"])
        st = sym_table(n)
        order = sorted(range(len(st["parts"])),
                       key=lambda k: st["parts"][k])
        mnr = sorted(tuple(row[j] for j in order) for row in st["table"])
        if mut("MUT-TWO-ENGINES") and n == 4:
            mnr = [tuple(x + 1 for x in mnr[0])] + mnr[1:]
        agree = dx == mnr
        if not agree:
            bad.append(n)
        rows.append({"row": "S%d" % n, "order": G.n,
                     "classes_dixon": len(ct["size"]),
                     "classes_murnaghan_nakayama": len(st["parts"]),
                     "tables_agree": agree})
    LD.gate("G-TWO-ENGINES-AGREE",
            "the two character engines are independent computations -- one "
            "diagonalises the class sums of an enumerated group over a "
            "prime field and lifts, the other never sees a group element and "
            "recurses on rim hooks -- and on every symmetric group small "
            "enough for both they are required to return the SAME table, "
            "matched through the cycle type and compared as a multiset of "
            "rows so that no ordering is assumed",
            not bad, "%d cross-engine rows, %d disagreeing %s"
            % (len(rows), len(bad), bad))
    S["two_engines"] = rows
    SEAL.take("THE TWO ENGINES", "two_engines", "G-TWO-ENGINES-AGREE", rows)


def measure_the_symmetric_census(S, pv):
    """the identity side of the inventory: the symmetric group on the nine
    actors and the Young subgroups the parent measured as stabilizers, each
    with its own table and its own gates."""
    st = sym_table(9)
    stg = sym_table_gates(st)
    ct9 = ct_from_sym(st)
    if mut("MUT-DROP-SPECIES"):
        ct9 = dict(ct9, table=ct9["table"][:-1])
    tg9 = table_gates(ct9)
    LD.gate("G-S9-TABLE",
            "the symmetric group on the nine actors carries the classical "
            "integer character theory, computed here by the rim-hook "
            "recursion: its classes and its species are both indexed by the "
            "partitions of nine, every value is a rational integer, the "
            "class equation closes on the factorial, the degrees are "
            "re-derived INDEPENDENTLY by the hook-length formula, and their "
            "squares sum to the order",
            stg["integer_valued"]
            and stg["degrees_match_the_hook_length_formula"]
            and stg["class_equation_holds"]
            and stg["degree_sum_of_squares"] == ifact(9)
            and st["order"] == pv["PV-AID-S9"]
            and stg["classes"] == stg["irreps"],
            "%d classes and %d species; degrees match the hook-length "
            "formula: %s; the squares sum to %d"
            % (stg["classes"], stg["irreps"],
               stg["degrees_match_the_hook_length_formula"],
               stg["degree_sum_of_squares"]))
    LD.gate("G-CHARACTER-TABLE-ROW-ORTHOGONALITY",
            "ROUTE ONE of the census standard, taken as its own gate: every "
            "pair of distinct species has inner product zero and every "
            "species has inner product one with itself, over every table "
            "this unit publishes -- the modular engine's and the "
            "combinatorial engine's alike",
            tg9["row_orthogonality_failures"] == 0
            and stg["row_orthogonality_failures"] == 0,
            "the nine-actor table: %d row-orthogonality failures through the "
            "generic inner product and %d through the engine's own"
            % (tg9["row_orthogonality_failures"],
               stg["row_orthogonality_failures"]))
    LD.gate("G-CHARACTER-TABLE-COLUMN-ORTHOGONALITY",
            "ROUTE TWO, a SEPARATE gate over a different index: for every "
            "pair of classes the column inner product vanishes off the "
            "diagonal and returns the centralizer order on it.  Column "
            "orthogonality is not implied by row orthogonality for a table "
            "whose class count has not yet been shown to equal its species "
            "count, and both counts are measured here",
            tg9["column_orthogonality_failures"] == 0
            and stg["column_orthogonality_failures"] == 0
            and tg9["classes"] == tg9["irreps"],
            "the nine-actor table: %d column-orthogonality failures through "
            "the generic route and %d through the engine's own; %d classes "
            "and %d species"
            % (tg9["column_orthogonality_failures"],
               stg["column_orthogonality_failures"], tg9["classes"],
               tg9["irreps"]))
    S["_ct9"] = ct9
    S["_st9"] = st
    S["symmetric_census"] = {
        "group": "S9", "order": st["order"], "classes": stg["classes"],
        "species": stg["irreps"], "degrees": sorted(stg["degrees"]),
        "degree_sum_of_squares": stg["degree_sum_of_squares"],
        "integer_valued": stg["integer_valued"],
        "degrees_match_the_hook_length_formula":
            stg["degrees_match_the_hook_length_formula"],
        "row_orthogonality_failures": stg["row_orthogonality_failures"],
        "column_orthogonality_failures": stg["column_orthogonality_failures"]}
    SEAL.take("THE SYMMETRIC CENSUS", "symmetric_census", "G-S9-TABLE",
              S["symmetric_census"])


# the stabilizer lattice AID measured, as orbit shapes: the SHAPES are the
# parent's, read from its receipt at named paths; the Young subgroups they
# name are built here.
STABILIZER_SHAPES = [
    ("FORCED-TRIVIAL", (1, 1, 1, 1, 1, 1, 1, 1, 1),
     "1+1+1+1+1+1+1+1+1", ""),
    ("YOUNG-2", (2, 1, 1, 1, 1, 1, 1, 1), "1+1+1+1+1+1+1+2", "PV-AID-SHAPE2"),
    ("YOUNG-4", (2, 2, 1, 1, 1, 1, 1), "1+1+1+1+1+2+2", "PV-AID-SHAPE4"),
    ("YOUNG-8", (2, 2, 2, 1, 1, 1), "1+1+1+2+2+2", "PV-AID-SHAPE8"),
    ("YOUNG-24", (3, 2, 2, 1, 1), "1+1+2+2+3", "PV-AID-SHAPE24"),
    ("YOUNG-216", (3, 3, 3), "3+3+3", "PV-AID-SHAPE216"),
    ("YOUNG-4320", (6, 3), "3+6", "PV-AID-SHAPE4320"),
]


DISTINGUISHED_STAB = "YOUNG-216"


def measure_the_identity_layer(S, pv):
    """MEASUREMENT FOUR.  The species of the nine actors restricted along the
    stabilizer lattice the parent measured, by TWO routes -- the restriction
    computed inside the subgroup, and Frobenius reciprocity computed inside
    the big group -- with the invariant dimension carrying a THIRD route of
    its own in the semistandard tableau count."""
    st, ct9 = S["_st9"], S["_ct9"]
    P = st["parts"]
    rows, species_rows = [], []
    disagree, kdisagree, dimfail = 0, 0, 0
    pairs = 0
    for nm, mu, shape, anchor in STABILIZER_SHAPES:
        Y = young_subgroup(mu)
        cty = ct_from_young(Y)
        tgy = table_gates(cty)
        order_routes = (
            Y["order"] + (1 if mut("MUT-LATTICE-SHAPE") else 0),
            sum(cty["size"]),
            sum(d * d for d in tgy["degrees"]))
        by_shape = tuple(sorted(mu, reverse=True))
        shape_ok = ("+".join(str(x) for x in sorted(mu)) == shape)
        invariants = 0
        for li, lam in enumerate(P):
            mult = []
            for ir in Y["irreps"]:
                s = 0
                for cl in Y["classes"]:
                    s += (young_class_size(mu, cl)
                          * st["table"][li][P.index(fuse(cl))]
                          * young_char(ir, cl))
                if s % Y["order"]:
                    raise GateFail("G-IDENTITY-BRANCHING-TWO-ROUTES :: a "
                                   "restriction multiplicity is not integral")
                mult.append(s // Y["order"])
            if mut("MUT-BRANCHING") and nm == "YOUNG-8" and li == 2:
                mult[0] = mult[0] + 1
            for k, ir in enumerate(Y["irreps"]):
                ind = {}
                for r in P:
                    acc = Fraction(0)
                    for cl in Y["classes"]:
                        if fuse(cl) == r:
                            acc += Fraction(young_char(ir, cl),
                                            young_centralizer(cl))
                    ind[r] = acc * centralizer_order(r)
                s2 = sum(sym_class_size(9, r) * st["table"][li][P.index(r)]
                         * ind[r] for r in P)
                s2 = s2 / st["order"]
                pairs += 1
                if s2 != mult[k]:
                    disagree += 1
            if sum(m * young_dim(ir) for m, ir in zip(mult, Y["irreps"])) \
                    != hook_dimension(lam):
                dimfail += 1
            trivi = [k for k, ir in enumerate(Y["irreps"])
                     if all(a == (m,) for a, m in zip(ir, mu))][0]
            kk = kostka(lam, by_shape)
            if mut("MUT-KOSTKA") and nm == "YOUNG-216" and li == 0:
                kk = kk + 1
            if kk != mult[trivi]:
                kdisagree += 1
            if mult[trivi] > 0:
                invariants += 1
            species_rows.append({
                "stabilizer": nm, "species": "+".join(str(x) for x in lam),
                "degree": hook_dimension(lam),
                "constituents": sum(1 for m in mult if m > 0),
                "invariant_dimension": mult[trivi]})
        rows.append({
            "row": nm, "orbit_shape": shape, "young_subgroup": by_shape,
            "order_by_construction": order_routes[0],
            "order_by_the_class_equation": order_routes[1],
            "order_by_the_degree_sum": order_routes[2],
            "classes": tgy["classes"], "species_of_its_own": tgy["irreps"],
            "row_orthogonality_failures": tgy["row_orthogonality_failures"],
            "column_orthogonality_failures":
                tgy["column_orthogonality_failures"],
            "shape_matches_the_parents": shape_ok,
            "prefixes_the_parent_measured_here":
                pv[anchor] if anchor else pv["PV-AID-FORCED"],
            "species_with_an_invariant_vector": invariants,
            "of": len(P)})
    LD.gate("G-IDENTITY-LATTICE-IS-THE-PARENTS",
            "the identity lattice is NOT this unit's invention: every one of "
            "the six nontrivial stabilizer shapes is read from the parent's "
            "receipt at its own named path together with the number of "
            "prefixes carrying it, the Young subgroup each shape names is "
            "built here, and its order is re-derived by three routes -- the "
            "product of the block factorials, the sum of its own class "
            "sizes, and the sum of the squares of its species degrees",
            all(r["shape_matches_the_parents"] for r in rows)
            and all(r["order_by_construction"]
                    == r["order_by_the_class_equation"]
                    == r["order_by_the_degree_sum"] for r in rows),
            "%d stabilizer rows, orders %s"
            % (len(rows), [r["order_by_construction"] for r in rows]))
    LD.gate("G-IDENTITY-BRANCHING-TWO-ROUTES",
            "every branching multiplicity is computed TWICE by computations "
            "that live in different groups: once as an inner product inside "
            "the stabilizer, where the big group's character is restricted "
            "through the class fusion, and once as an inner product inside "
            "the big group between its own species and the character induced "
            "from the stabilizer.  Frobenius reciprocity is the theorem the "
            "two routes test; a restriction that had drifted from its own "
            "induction dies here",
            disagree == 0 and dimfail == 0,
            "%d branching multiplicities computed by both routes, %d "
            "disagreements, %d species whose restricted dimensions do not "
            "sum to the degree" % (pairs, disagree, dimfail))
    LD.gate("G-KOSTKA-ROUTE",
            "the invariant dimension carries a THIRD route that shares no "
            "code with either character engine: the number of semistandard "
            "tableaux of the species' shape and the stabilizer's content, "
            "counted by peeling one horizontal strip per block.  It must "
            "equal the multiplicity of the stabilizer's trivial species at "
            "every one of the rows",
            kdisagree == 0,
            "%d tableau counts compared against the trivial multiplicity, %d "
            "disagreements" % (len(species_rows), kdisagree))
    S["identity_layer"] = {
        "rows": rows, "species_rows": species_rows,
        "the_distinguished_branching":
            [{k: v for k, v in r.items() if k != "stabilizer"}
             for r in species_rows if r["stabilizer"] == DISTINGUISHED_STAB],
        "the_distinguished_stabilizer": DISTINGUISHED_STAB,
        "branching_pairs": pairs, "route_disagreements": disagree,
        "tableau_route_disagreements": kdisagree}
    SEAL.take("THE IDENTITY LAYER", "identity_layer",
              "G-KOSTKA-ROUTE", S["identity_layer"])
    return rows


# the flag exhibited for the crystallization chain: a nested sequence of
# partitions of the nine actors, one per prefix length.
CHAIN_FLAG = [
    ((1, 2, 3), (4, 5, 6, 7, 8, 9)),
    ((1, 2, 3), (4, 5, 6), (7, 8, 9)),
    ((1, 2, 3), (4, 5, 6), (7, 8, 9)),
    ((1, 2), (3,), (4, 5), (6,), (7, 8), (9,)),
    ((1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,)),
    ((1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,)),
]


def measure_the_crystallization_chain(S, pv, src):
    """the identity layer read along the parent's own measured chain: the
    stabilizer orders it published prefix by prefix, realised here by an
    EXHIBITED nested flag, with the species inventory recomputed at each
    step."""
    aid = json.loads(src["S-AID-RECEIPT"].decode())
    chain = dig(aid, "crystallization/stabilizer_order_by_prefix_length_C1")
    st = S["_st9"]
    P = st["parts"]
    rows = []
    nested = True
    prev = None
    for i, part in enumerate(CHAIN_FLAG):
        mu = tuple(sorted((len(b) for b in part), reverse=True))
        order = iprod([ifact(len(b)) for b in part])
        if prev is not None:
            for b in part:
                if not any(set(b) <= set(c) for c in prev):
                    nested = False
        prev = part
        inv = sum(1 for lam in P if kostka(lam, mu) > 0)
        if mut("MUT-CHAIN-FLAG") and i == 3:
            order = order + 1
        rows.append({"prefix_length": i + 1, "stabilizer_order": order,
                     "the_parents_order": chain[i],
                     "orbit_shape": "+".join(str(len(b))
                                             for b in sorted(part,
                                                             key=len)),
                     "species_with_an_invariant_vector": inv, "of": len(P)})
    ok = all(r["stabilizer_order"] == r["the_parents_order"] for r in rows)
    LD.gate("G-CRYSTALLIZATION-CHAIN-IS-NESTED",
            "the parent's measured crystallization profile is realised here "
            "by an EXHIBITED flag of partitions of the nine actors: each "
            "block of each step lies inside a block of the step before, so "
            "the stabilizers are genuinely nested and the species inventory "
            "along the chain is a restriction sequence rather than six "
            "unrelated subgroups; every order is compared with the parent's "
            "own published profile entry by entry",
            ok and nested and chain[0] == pv["PV-AID-CHAIN"]
            and rows[pv["PV-AID-TIME"] - 1]["stabilizer_order"] == 1,
            "orders %s against the parent's %s; nested: %s; the inventory "
            "along the chain %s"
            % ([r["stabilizer_order"] for r in rows], chain, nested,
               [r["species_with_an_invariant_vector"] for r in rows]))
    S["crystallization_chain"] = {
        "rows": rows, "the_flag_is_nested": nested,
        "the_parents_profile": chain,
        "the_crystallization_time": pv["PV-AID-TIME"],
        "species_at_the_first_prefix":
            rows[0]["species_with_an_invariant_vector"],
        "species_at_crystallization":
            rows[pv["PV-AID-TIME"] - 1]["species_with_an_invariant_vector"]}
    SEAL.take("THE CRYSTALLIZATION CHAIN", "crystallization_chain",
              "G-CRYSTALLIZATION-CHAIN-IS-NESTED", S["crystallization_chain"])


# ===========================================================================
# SECTION 10.  THE CARRIER ROWS -- THE HEART
# ===========================================================================
# The declared carrier rows: every (group, carrier) pair this corpus's own
# terminals put on the table.  The list is a declaration and is priced as one
# in the choice inventory.

def cycle_perm(rho, n):
    """an explicit permutation of n points with the declared cycle type."""
    p = list(range(n))
    at = 0
    for c in rho:
        cyc = list(range(at, at + c))
        for i in range(c):
            p[cyc[i]] = cyc[(i + 1) % c]
        at += c
    return tuple(p)


def build_the_carrier_rows(S, pv):
    """MEASUREMENT THREE.  Every declared carrier as a permutation module
    over every measured group that acts on it, decomposed EXACTLY."""
    coins, tw, sw, ident = S["_coins"], S["_tw"], S["_sw"], S["_ident"]
    ag, charts, links = S["_ag"], S["_charts"], S["_links"]
    ctw = realisable_constant_twists()
    ncoin = len(coins)
    specs = []

    coin_groups = [
        ("RESIDUAL-GAUGE-4", [tw[ctw[1]]],
         "ACT/R5 -- the constant twists the torus itself realises: the "
         "arena's own gauge group on the carrier, anchored reading"),
        ("ACTING-LINK-8", [tw[1]],
         "ACT -- the acting group at the link grain, anchored reading"),
        ("RESIDUAL-GAUGE-8", [tw[ctw[1]], sw],
         "ACT/R5 -- the residual gauge group at the extension reading"),
        ("GAMMA-16", [tw[1], sw],
         "ACT -- the coin-map group, and the acting group at the link grain "
         "at the extension reading")]
    for nm, gens, prov in coin_groups:
        els = close_group(gens, ident)
        G = Group(nm, els, perm_compose, ident, prov, "COIN-640")
        specs.append({"name": "COIN-640-UNDER-%s" % nm, "G": G,
                      "carrier": "COIN-640", "points": ncoin,
                      "perms": {g: g for g in els}, "gens": els,
                      "provenance": prov, "ct": None})

    for nm in ("CHART-32", "CHART-128"):
        els = charts[nm]["link"]
        G = Group(nm, els, perm_compose, tuple(range(len(links))),
                  "R5/ACT -- the declared chart group, %s reading"
                  % ("anchored" if nm == "CHART-32" else "extension"),
                  "LINK-32")
        specs.append({"name": "LINK-32-UNDER-%s" % nm, "G": G,
                      "carrier": "LINK-32", "points": len(links),
                      "perms": {g: g for g in els}, "gens": els,
                      "provenance": G.provenance, "ct": None})
        for ck, cname, pts in (("site", "SITE-16", 16),
                               ("plaq", "PLAQUETTE-16", 16)):
            specs.append({"name": "%s-UNDER-%s" % (cname, nm), "G": G,
                          "carrier": cname, "points": pts,
                          "perms": {g: charts[nm][ck][g] for g in els},
                          "gens": [charts[nm][ck][g] for g in els],
                          "provenance": G.provenance, "ct": None})
    tgens = []
    for e in chart_elements(False):
        if e[1] == (False, 1, 1):
            tgens.append(tuple(links.index(transported_link(l, e)[0])
                               for l in links))
    Gt = Group("TORUS-TRANSLATIONS-16", sorted(set(tgens)), perm_compose,
               tuple(range(len(links))),
               "R5 -- the lattice translations, the normal subgroup of the "
               "chart group the torus itself supplies", "LINK-32")
    specs.append({"name": "LINK-32-UNDER-TORUS-TRANSLATIONS-16", "G": Gt,
                  "carrier": "LINK-32", "points": len(links),
                  "perms": {g: g for g in Gt.elems}, "gens": Gt.elems,
                  "provenance": Gt.provenance, "ct": None})
    tsite = {}
    for e in chart_elements(False):
        if e[1] == (False, 1, 1):
            key = tuple(links.index(transported_link(l, e)[0]) for l in links)
            tsite[key] = tuple(lat_sites().index(lat_addv(s, e[0]))
                               for s in lat_sites())
    specs.append({"name": "SITE-16-UNDER-TORUS-TRANSLATIONS-16", "G": Gt,
                  "carrier": "SITE-16", "points": 16,
                  "perms": {g: tsite[g] for g in Gt.elems},
                  "gens": [tsite[g] for g in Gt.elems],
                  "provenance": Gt.provenance, "ct": None})

    for nm, els, prov in (
            ("TRANS-9", ag["trans"],
             "I7/paper-06 -- the pinned chart translations of the identity "
             "arena, which AID measured to be exactly the walk symmetries"),
            ("CHART-18", ag["chart"],
             "I7/paper-06 -- the pinned chart group of the identity arena"),
            ("EXT-108", ag["ext"],
             "paper-06 -- the largest group the declared link set admits, "
             "entered there as arena data")):
        G = Group(nm, els, ag_mul, AG_E, prov, "CELL-27")
        cp = {g: tuple(ag["cells"].index(ag_act_cell(g, c))
                       for c in ag["cells"]) for g in els}
        sp = {g: tuple(ag["sites"].index(ag_act_site(g, x))
                       for x in ag["sites"]) for g in els}
        specs.append({"name": "CELL-27-UNDER-%s" % nm, "G": G,
                      "carrier": "CELL-27", "points": len(ag["cells"]),
                      "perms": cp, "gens": list(cp.values()),
                      "provenance": prov, "ct": None})
        specs.append({"name": "SITE-9-UNDER-%s" % nm, "G": G,
                      "carrier": "SITE-9", "points": 9,
                      "perms": sp, "gens": list(sp.values()),
                      "provenance": prov, "ct": None})

    ct9 = S["_ct9"]
    p9 = {rho: cycle_perm(rho, 9) for rho in ct9["rep"]}
    specs.append({"name": "ACTOR-9-UNDER-S9", "G": None,
                  "carrier": "ACTOR-9", "points": 9, "perms": p9,
                  "gens": [cycle_perm((2, 1, 1, 1, 1, 1, 1), 9),
                           cycle_perm((9,), 9)],
                  "provenance":
                      "AID -- the granted nine-actor grain, with the whole "
                      "symmetric group on it",
                  "ct": ct9, "group_name": "S9", "order": ifact(9),
                  "closed": True})

    rows = []
    for sp in specs:
        rows.append(price_a_census_row(
            sp["name"], sp["carrier"], sp["points"], sp["perms"], sp["gens"],
            sp["provenance"], G=sp.get("G"), supplied_table=sp.get("ct"),
            group_name=sp.get("group_name"), order=sp.get("order"),
            closed=sp.get("closed"),
            distinguished=(sp["name"] == "ACTOR-9-UNDER-S9")))
    bad = {r["row"]: row_gate_failures(r) for r in rows}
    bad = {k: v for k, v in bad.items() if v}
    LD.gate("G-CARRIER-DECOMPOSITION",
            "THE HEART, gated object by object (#87): every declared carrier "
            "is decomposed into species over every measured group that acts "
            "on it, and each row must satisfy its OWN predicates -- the "
            "multiplicities are non-negative integers, they weigh the "
            "carrier exactly (the sum of multiplicity times degree is the "
            "number of points), the trivial species' multiplicity is the "
            "orbit count computed independently by union-find, the hosted "
            "and homeless species exhaust the table, both composite routes "
            "agree, both statistics routes agree, and the two square "
            "dimensions are the two binomials",
            not bad, "%d carrier rows, %d failing %s"
            % (len(rows), len(bad), list(bad.items())[:3]))
    orb = {r["row"]: (r["orbits_by_the_character"], r["orbits_by_union_find"])
           for r in rows}
    if mut("MUT-ORBIT-ROUTE"):
        orb["COIN-640-UNDER-ACTING-LINK-8"] = orb["COIN-640-UNDER-GAMMA-16"]
    LD.gate("G-CARRIER-ORBITS-TWO-ROUTES",
            "the parent's own four carrier numbers are re-derived here as "
            "MULTIPLICITIES: the trivial species' multiplicity in a "
            "permutation module is the orbit count, so the 136 carrier "
            "classes and the 80 at the extension -- and the 208 and 120 the "
            "arena's own gauge group leaves -- are recovered from a "
            "character inner product and from a union-find pass that never "
            "evaluates a character, and both must agree at every row",
            orb["COIN-640-UNDER-ACTING-LINK-8"][0] == pv["PV-ACT-ORB136"]
            and orb["COIN-640-UNDER-GAMMA-16"][0] == pv["PV-ACT-ORB80"]
            and orb["COIN-640-UNDER-RESIDUAL-GAUGE-4"][0]
            == pv["PV-ACT-ORB208"]
            and orb["COIN-640-UNDER-RESIDUAL-GAUGE-8"][0]
            == pv["PV-ACT-ORB120"]
            and all(a == b for a, b in orb.values()),
            "the four coin rows return %s; %d of %d rows agree between the "
            "two routes"
            % ([orb["COIN-640-UNDER-%s" % g][0]
                for g in ("RESIDUAL-GAUGE-4", "ACTING-LINK-8",
                          "RESIDUAL-GAUGE-8", "GAMMA-16")],
               sum(1 for a, b in orb.values() if a == b), len(orb)))
    if mut("MUT-HOMELESS"):
        for r in rows:
            r["homeless"] = 0
    homeless = [r for r in rows if r["homeless"] > 0]
    LD.gate("G-CARRIER-HOMELESS-CENSUS",
            "the homelessness question is MEASURED and not argued: a species "
            "is carrier-homeless at a row exactly when its multiplicity in "
            "that row's permutation module is zero, the count is bound to "
            "that predicate row by row, and the census is required to "
            "populate BOTH arms -- some row where every species is hosted "
            "and some row where one is not -- so the verdict is a "
            "measurement rather than a property of the arena's size",
            len(homeless) > 0 and len(homeless) < len(rows),
            "%d of %d rows leave at least one species homeless; the widest "
            "gap is %s at %d of %d"
            % (len(homeless), len(rows),
               max(rows, key=lambda r: r["homeless"])["row"],
               max(rows, key=lambda r: r["homeless"])["hosted"],
               max(rows, key=lambda r: r["homeless"])["irreps"]))
    S["_rows"] = rows
    S["carrier_census"] = {
        "rows": [{k: v for k, v in r.items()
                  if not k.startswith("_") and k != "table_gates"}
                 for r in rows],
        "carriers": sorted({r["carrier"] for r in rows}),
        "rows_measured": len(rows),
        "species_hosted": sum(r["hosted"] for r in rows),
        "species_available": sum(r["irreps"] for r in rows),
        "rows_with_a_homeless_species": len(homeless),
        "measure": "COUNTING-ONLY"}
    SEAL.take("THE CARRIER CENSUS", "carrier_census",
              "G-CARRIER-HOMELESS-CENSUS", S["carrier_census"])
    return rows


def measure_the_odd_twist_species(S, pv):
    """THE WELD TO THE PARENT'S PRICE.  The parent measured that every
    admissible weight system identifies 72 pairs of gauge orbits and pins one
    observable to a point.  Both numbers are ONE SPECIES here, and this
    measurement names it."""
    coins, tw, sw = S["_coins"], S["_tw"], S["_sw"]
    rows = {r["row"]: r for r in S["_rows"]}
    out = {}
    for rowname, gname, gens, resname in (
            ("COIN-640-UNDER-ACTING-LINK-8", "ACTING-LINK-8", None,
             "COIN-640-UNDER-RESIDUAL-GAUGE-4"),
            ("COIN-640-UNDER-GAMMA-16", "GAMMA-16", None,
             "COIN-640-UNDER-RESIDUAL-GAUGE-8")):
        r = rows[rowname]
        ct = r["_ct"]
        F = ct["field"]
        w = ct["where"]
        hit = []
        for k, row in enumerate(ct["table"]):
            if cyc_int(F, row[0]) != 1:
                continue
            if row[w[tw[1]]] != F.scal(F.one, -1):
                continue
            if row[w[tw[realisable_constant_twists()[1]]]] != F.one:
                continue
            if gname == "GAMMA-16" and row[w[sw]] != F.one:
                continue
            hit.append(k)
        out[rowname] = {
            "the_species": hit,
            "multiplicity": r["multiplicities"][hit[0]] if len(hit) == 1
            else -1,
            "the_parents_merged_orbit_pairs":
                pv["PV-ACT-MERGED72"] if gname == "ACTING-LINK-8"
                else pv["PV-ACT-MERGED40"],
            "the_arena_group_orbit_count":
                rows[resname]["orbits_by_the_character"],
            "the_acting_group_orbit_count": r["orbits_by_the_character"]}
    obs = [Fraction(quartic_sign(m[1]) + quartic_sign(m[2])) for m in coins]
    r8 = rows["COIN-640-UNDER-ACTING-LINK-8"]
    ct8 = r8["_ct"]
    F = ct8["field"]
    n = len(coins)
    els = close_group([tw[1]], S["_ident"])
    nonzero_components = []
    for k, row in enumerate(ct8["table"]):
        acc = [F.zero] * n
        for g in els:
            ch = F.conj(row[ct8["where"][g]])
            ginv = [0] * n
            for x in range(n):
                ginv[g[x]] = x
            for x in range(n):
                v = obs[ginv[x]]
                if v:
                    acc[x] = F.add(acc[x], F.scal(ch, v))
        if any(not F.is_zero(a) for a in acc):
            nonzero_components.append(k)
    orbit_sums_zero = 0
    par = list(range(n))

    def find(a):
        while par[a] != a:
            par[a] = par[par[a]]
            a = par[a]
        return a
    for g in els:
        for x in range(n):
            ra, rb = find(x), find(g[x])
            if ra != rb:
                par[ra] = rb
    orb = {}
    for x in range(n):
        orb.setdefault(find(x), []).append(x)
    for o in orb.values():
        if sum(obs[x] for x in o) == 0:
            orbit_sums_zero += 1
    if mut("MUT-ODD-TWIST"):
        nonzero_components = nonzero_components + [0, 1]
    theone = out["COIN-640-UNDER-ACTING-LINK-8"]["the_species"]
    ok = (all(len(v["the_species"]) == 1 for v in out.values())
          and all(v["multiplicity"]
                  == v["the_arena_group_orbit_count"]
                  - v["the_acting_group_orbit_count"]
                  for v in out.values())
          and all(v["multiplicity"] == v["the_parents_merged_orbit_pairs"]
                  for v in out.values())
          and nonzero_components == theone
          and orbit_sums_zero == len(orb))
    LD.gate("G-THE-ODD-TWIST-SPECIES",
            "the parent's price and the parent's one pinned observable are "
            "resolved into a single species, and the resolution is measured "
            "three ways.  There is exactly ONE species on which the odd "
            "twist acts by minus one while the twists the torus realises act "
            "trivially; its multiplicity in the carrier equals the drop in "
            "the trivial multiplicity between the arena's own gauge group "
            "and the acting group -- which is the parent's own count of "
            "identified orbit pairs, at both readings; the parent's pinned "
            "observable, rebuilt here from its own definition, has a "
            "NON-ZERO component in that species and in no other; and its sum "
            "over every orbit of the acting group is zero, which is why "
            "every invariant weight gives it the single expectation the "
            "parent measured",
            ok,
            "the species is %s at the anchored reading with multiplicity %d "
            "against the parent's %d, and %s with multiplicity %d against "
            "%d; the observable is non-zero at %d of the %d points, its "
            "non-zero isotypic components are %s, and %d of %d orbit sums "
            "vanish"
            % (theone,
               out["COIN-640-UNDER-ACTING-LINK-8"]["multiplicity"],
               pv["PV-ACT-MERGED72"],
               out["COIN-640-UNDER-GAMMA-16"]["the_species"],
               out["COIN-640-UNDER-GAMMA-16"]["multiplicity"],
               pv["PV-ACT-MERGED40"],
               sum(1 for v in obs if v != 0), n, nonzero_components,
               orbit_sums_zero, len(orb)))
    S["odd_twist_species"] = {
        "rows": [{"row": k, "the_species_index": v["the_species"][0],
                  "multiplicity": v["multiplicity"],
                  "the_arena_groups_orbit_count":
                      v["the_arena_group_orbit_count"],
                  "the_acting_groups_orbit_count":
                      v["the_acting_group_orbit_count"],
                  "the_parents_identified_orbit_pairs":
                      v["the_parents_merged_orbit_pairs"]}
                 for k, v in sorted(out.items())],
        "the_observable": pv["PV-ACT-PINNEDNAME"],
        "the_parents_verdict_on_it": pv["PV-ACT-PINNED"],
        "points_where_the_observable_does_not_vanish":
            sum(1 for v in obs if v != 0),
        "its_non_vanishing_isotypic_components": len(nonzero_components),
        "orbits_of_the_acting_group": len(orb),
        "orbits_where_the_observable_sums_to_zero": orbit_sums_zero,
        "measure": "COUNTING-ONLY"}
    SEAL.take("THE ODD-TWIST SPECIES", "odd_twist_species",
              "G-THE-ODD-TWIST-SPECIES", S["odd_twist_species"])


def measure_the_statistics_tie_in(S, pv):
    """MEASUREMENT SIX.  The occupancy terminal measured that at the
    carrier's own pair grain the antisymmetric shape closes and the
    symmetric one does not; which shape is selected is DERIVED here from
    those two numbers rather than typed, and the species compatible with it
    are counted row by row."""
    anti, sym = pv["PV-OCC-ANTI"], pv["PV-OCC-SYM"]
    selected = "ANTISYMMETRIC" if anti < sym else (
        "SYMMETRIC" if sym < anti else "NEITHER")
    if mut("MUT-SELECTED-SHAPE"):
        selected = "SYMMETRIC"
    rows = S["_rows"]
    tot = {"in_both_shapes": 0, "symmetric_only": 0,
           "antisymmetric_only": 0, "in_neither_shape": 0}
    for r in rows:
        for k in tot:
            tot[k] += r[k]
    if mut("MUT-STATISTICS-SPLIT"):
        tot["in_neither_shape"] = tot["in_neither_shape"] + 1
    per = [{"row": r["row"], "species": r["irreps"],
            "in_both_shapes": r["in_both_shapes"],
            "symmetric_only": r["symmetric_only"],
            "antisymmetric_only": r["antisymmetric_only"],
            "in_neither_shape": r["in_neither_shape"],
            "compatible_with_the_selected_shape":
                r["compatible_with_the_selected_shape"]} for r in rows]
    proper = [p for p in per if p["in_neither_shape"] or p["symmetric_only"]
              or p["antisymmetric_only"]]
    LD.gate("G-OCC-SELECTED-SHAPE",
            "which shape the occupancy terminal's exclusion census selected "
            "at the pair grain is DERIVED here from that terminal's own two "
            "leak counts read at named receipt paths -- the shape that leaks "
            "at no cell against the shape that leaks at eighty-one -- and "
            "not typed; the species compatible with the selected shape are "
            "then counted at every carrier row by the same predicate",
            selected == "ANTISYMMETRIC" and anti == 0 and sym > anti,
            "the antisymmetric shape leaks at %d cells and the symmetric at "
            "%d at %d of the coin classes, so the selected shape is %s"
            % (anti, sym, pv["PV-OCC-COINS"], selected))
    LD.gate("G-STATISTICS-SPLIT-CENSUS",
            "the compatibility census partitions every species of every row "
            "into four classes by two independently computed multiplicities "
            "-- in both squares, in the symmetric square alone, in the "
            "antisymmetric square alone, in neither -- the four classes "
            "exhaust the row's species count at every row, and the census is "
            "required to populate more than one class, so an all-compatible "
            "verdict and a proper split are both live and the measured one "
            "is reported",
            sum(tot.values()) == sum(r["irreps"] for r in rows)
            and len(proper) > 0,
            "the aggregate split is %d in both, %d symmetric only, %d "
            "antisymmetric only, %d in neither, over %d species; %d of %d "
            "rows split properly"
            % (tot["in_both_shapes"], tot["symmetric_only"],
               tot["antisymmetric_only"], tot["in_neither_shape"],
               sum(r["irreps"] for r in rows), len(proper), len(rows)))
    S["statistics"] = {
        "the_selected_shape": selected,
        "the_parents_antisymmetric_leak_cells": anti,
        "the_parents_symmetric_leak_cells": sym,
        "rows": per, "aggregate": tot,
        "rows_that_split_properly": len(proper),
        "measure": "COUNTING-ONLY"}
    SEAL.take("THE STATISTICS TIE-IN", "statistics",
              "G-STATISTICS-SPLIT-CENSUS", S["statistics"])


def measure_the_selection_rules(S):
    """MEASUREMENT FIVE.  The composite table among the carrier-realized
    species of each row, and whether the composites stay inside it."""
    rows = S["_rows"]
    per = [{"row": r["row"], "hosted": r["hosted"],
            "composite_rules": r["composite_rules"],
            "species_the_composites_exit_to":
                len(r["species_the_composites_exit_to"]),
            "selection_closes": r["selection_closes"]} for r in rows]
    dist = [r for r in rows if "the_composite_table" in r][0]
    openrows = [p for p in per if not p["selection_closes"]]
    LD.gate("G-SELECTION-CLOSURE-CENSUS",
            "the composite census is exact and two-routed at every entry, "
            "and its verdict is per-row: the composites of the species a "
            "carrier hosts either all lie among the species it hosts or they "
            "do not, the closure flag is bound to the emptiness of the exit "
            "set at each row separately (#87, #295), and BOTH arms are "
            "populated by measurement -- so neither verdict is a property of "
            "the declaration",
            len(openrows) > 0 and len(openrows) < len(per),
            "%d rows, %d closing and %d exiting; %d composite rules in all"
            % (len(per), len(per) - len(openrows), len(openrows),
               sum(p["composite_rules"] for p in per)))
    S["selection"] = {
        "rows": per,
        "the_distinguished_row": dist["row"],
        "the_composite_table": dist["the_composite_table"],
        "rows_that_close": len(per) - len(openrows),
        "rows_that_exit": len(openrows),
        "composite_rules": sum(p["composite_rules"] for p in per),
        "measure": "COUNTING-ONLY"}
    SEAL.take("THE SELECTION RULES", "selection",
              "G-SELECTION-CLOSURE-CENSUS", S["selection"])


def assemble_the_inventory(S, pv):
    """MEASUREMENT ONE, assembled: every group of the census with its
    provenance, its order re-derived, and the engine that gave it a table."""
    inv = []
    seen = set()
    for r in S["_rows"]:
        if r["group"] in seen:
            continue
        seen.add(r["group"])
        ct = r["_ct"]
        inv.append({
            "group": r["group"], "order": r["group_order"],
            "classes": r["classes"], "species": r["irreps"],
            "degrees": r["degrees"], "engine": ct["engine"],
            "carrier_it_is_censused_on": r["carrier"],
            "above_the_table_cap": False,
            "provenance": r["provenance"]})
    for row in S["acting_groups"]["rows"]:
        if row["acting_group_order"] <= TABLE_CAP:
            continue
        inv.append({
            "group": "ACTING-%s-%s" % (row["grain"], row["reading"]),
            "order": row["acting_group_order"], "classes": 0, "species": 0,
            "degrees": [], "engine": "ABOVE-THE-TABLE-CAP",
            "carrier_it_is_censused_on": "COIN-640",
            "above_the_table_cap": True,
            "provenance": "ACT -- the acting group at the %s grain, %s "
                          "reading; its order is re-derived here and the "
                          "carrier sees it through the group of order %d"
                          % (row["grain"].lower(), row["reading"].lower(),
                             row["the_group_the_carrier_sees"])})
    for r in S["identity_layer"]["rows"]:
        inv.append({
            "group": r["row"], "order": r["order_by_construction"],
            "classes": r["classes"], "species": r["species_of_its_own"],
            "degrees": [], "engine": "MURNAGHAN-NAKAYAMA-PRODUCT",
            "carrier_it_is_censused_on": "ACTOR-9",
            "above_the_table_cap": False,
            "provenance": "AID -- a measured stabilizer of the identity "
                          "lattice, orbit shape %s" % r["orbit_shape"]})
    if mut("MUT-INVENTORY"):
        inv = inv[:-1]
    orows = [{"group": r["group"], "routes_taken": r["order_routes_taken"],
              "routes_that_agree": r["order_routes_that_agree"],
              "order_routes": r["order_routes"]} for r in S["_rows"]]
    obad = [o["group"] for o in orows
            if o["routes_that_agree"] != o["routes_taken"]]
    parent_orders = {"RESIDUAL-GAUGE-4": pv["PV-ACT-RES4"],
                     "RESIDUAL-GAUGE-8": pv["PV-ACT-RES8"],
                     "ACTING-LINK-8": pv["PV-ACT-ACTING8"],
                     "GAMMA-16": pv["PV-ACT-ACTING16"]}
    if mut("MUT-ORDER-ROUTE"):
        parent_orders["GAMMA-16"] = parent_orders["GAMMA-16"] + 1
    pbad = [g for g, v in parent_orders.items()
            if [r["order"] for r in inv if r["group"] == g][0] != v]
    obad = obad + pbad
    LD.gate("G-GROUP-INVENTORY-ORDERS-RE-DERIVED",
            "no group order in this census is typed.  Every carrier row "
            "re-derives its group's order by the length of the closed "
            "element list, by the sum of its own conjugacy class sizes and "
            "by the sum of the squares of its species degrees -- three "
            "computations sharing no step -- and by the product of one "
            "declared point's orbit with that point's stabilizer wherever "
            "the elements are enumerable, which is every row but the one "
            "whose group has three hundred and sixty-two thousand eight "
            "hundred and eighty elements.  The four groups the gauge arena's "
            "own terminal published orders for are additionally required to "
            "carry those orders, at named receipt paths.  The gate binds "
            "each group separately (#87)",
            not obad, "%d rows, %d routes taken in all, %d groups where the "
            "routes disagree %s; %d of the parent's four published orders "
            "not reproduced %s"
            % (len(orows), sum(o["routes_taken"] for o in orows), len(obad),
               obad[:3], len(pbad), pbad[:3]))
    S["order_routes"] = orows
    SEAL.take("THE ORDER ROUTES", "order_routes",
              "G-GROUP-INVENTORY-ORDERS-RE-DERIVED", orows)
    tot = {"groups": len(inv),
           "groups_with_a_table": sum(1 for r in inv
                                      if not r["above_the_table_cap"]),
           "groups_above_the_table_cap":
               sum(1 for r in inv if r["above_the_table_cap"]),
           "classes": sum(r["classes"] for r in inv),
           "species": sum(r["species"] for r in inv),
           "the_table_cap": TABLE_CAP,
           "orders": sorted({r["order"] for r in inv})}
    LD.gate("G-GROUP-INVENTORY-IS-TOTAL",
            "the published inventory is checked TOTAL against the "
            "measurements that produced it: every group carrying a carrier "
            "row appears exactly once, every acting group above the table "
            "cap appears with its re-derived order and the group the carrier "
            "sees it through, every measured stabilizer of the identity "
            "lattice appears with its own species count, and the totals are "
            "recounted from the rows rather than accumulated",
            tot["groups"] == len(inv)
            and tot["classes"] == sum(r["classes"] for r in inv)
            and tot["groups_with_a_table"] + tot["groups_above_the_table_cap"]
            == tot["groups"]
            and len(seen) + len(S["identity_layer"]["rows"])
            + tot["groups_above_the_table_cap"] == tot["groups"],
            "%d groups, %d with a table and %d above the cap; %d classes and "
            "%d species in all"
            % (tot["groups"], tot["groups_with_a_table"],
               tot["groups_above_the_table_cap"], tot["classes"],
               tot["species"]))
    S["group_inventory"] = {"rows": inv, "totals": tot}
    SEAL.take("THE GROUP INVENTORY", "group_inventory",
              "G-GROUP-INVENTORY-IS-TOTAL", S["group_inventory"])
    return tot


# ===========================================================================
# SECTION 11.  THE HEAD, THE CONTROLS, THE FEASIBILITY
# ===========================================================================

def head_law(rows, tot):
    """the head, derived from the measurements by the pre-registered
    vocabulary and nothing else."""
    for r in rows:
        if r["status"] != "MEASURED":
            return "SPC-BLOCKED-AT-" + r["blocked_at"]
    k = sum(r["hosted"] for r in rows)
    n = sum(r["irreps"] for r in rows)
    rules = sum(r["composite_rules"] for r in rows)
    exits = [r for r in rows if not r["selection_closes"]]
    b = sum(r["in_both_shapes"] for r in rows)
    s = sum(r["symmetric_only"] for r in rows)
    a = sum(r["antisymmetric_only"] for r in rows)
    z = sum(r["in_neither_shape"] for r in rows)
    parts = ["SPC-INVENTORY-%d-GROUPS-%d-CLASSES-%d-SPECIES"
             % (tot["groups"], tot["classes"], tot["species"]),
             "SPC-CARRIER-SELECTS-%d-OF-%d" % (k, n),
             ("SPC-SELECTION-OPEN" if exits
              else "SPC-SELECTION-CLOSED-%d-RULES" % rules),
             "SPC-STATISTICS-SPLITS-%d|%d|%d|%d" % (b, s, a, z)]
    return "--".join(parts)


def second_head_law(rows, tot):
    """the same head by a different law: it accumulates in one pass, tests
    the blocked condition last rather than first, builds each token by
    concatenation instead of by a format string, and shares none of the
    first law's expressions."""
    acc = {"hosted": 0, "irreps": 0, "rules": 0, "open": 0,
           "both": 0, "sym": 0, "anti": 0, "none": 0, "blocked": []}
    for r in rows:
        if r["status"] != "MEASURED":
            acc["blocked"].append(r["blocked_at"])
            continue
        acc["hosted"] += r["hosted"]
        acc["irreps"] += r["irreps"]
        acc["rules"] += r["composite_rules"]
        acc["open"] += 0 if r["selection_closes"] else 1
        acc["both"] += r["in_both_shapes"]
        acc["sym"] += r["symmetric_only"]
        acc["anti"] += r["antisymmetric_only"]
        acc["none"] += r["in_neither_shape"]
    if acc["blocked"]:
        return "SPC-BLOCKED-AT-" + acc["blocked"][0]
    one = "SPC-INVENTORY-" + str(tot["groups"]) + "-GROUPS-" \
        + str(tot["classes"]) + "-CLASSES-" + str(tot["species"]) + "-SPECIES"
    two = "SPC-CARRIER-SELECTS-" + str(acc["hosted"]) + "-OF-" \
        + str(acc["irreps"])
    if acc["open"] > 0:
        three = "SPC-SELECTION-OPEN"
    else:
        three = "SPC-SELECTION-CLOSED-" + str(acc["rules"]) + "-RULES"
    four = "SPC-STATISTICS-SPLITS-" + "|".join(
        [str(acc["both"]), str(acc["sym"]), str(acc["anti"]),
         str(acc["none"])])
    return one + "--" + two + "--" + three + "--" + four


def synthetic_arena(name, elems, mul, ident, perms, npoints):
    """a synthetic arena, put through the REAL census functions: no field of
    any row is written from outside, the group's closure is MEASURED rather
    than assumed, and the action is carried separately from the group so that
    a group acting non-faithfully is expressible -- which is what the
    homelessness arm needs."""
    G = Group(name, elems, mul, ident, "a synthetic control arena",
              "POINTS-%d" % npoints)
    return price_a_census_row(name, "POINTS-%d" % npoints, npoints, perms,
                              list(perms.values()),
                              "a synthetic control arena", G=G)


def demonstrate_the_outcome_words(S, tot):
    """THE CONTROL ARM.  Every pre-registered outcome word is required to be
    EMITTED by the head law from a real measurement made by the census
    machinery on an arena built for the purpose -- a cyclic group acting
    regularly, a cyclic group acting trivially, a cyclic group with two
    orbits of coprime size, and a set of permutations that is not a group."""
    probes = []
    c3 = [0, 1, 2]

    def add3(a, b):
        return (a + b) % 3

    def add6(a, b):
        return (a + b) % 6
    reg = synthetic_arena("CTRL-CYCLIC-3-REGULAR", c3, add3, 0,
                          {k: tuple((i + k) % 3 for i in range(3))
                           for k in c3}, 3)
    triv = synthetic_arena("CTRL-CYCLIC-3-TRIVIAL-ACTION", c3, add3, 0,
                           {k: (0, 1) for k in c3}, 2)
    six = synthetic_arena("CTRL-CYCLIC-6-TWO-ORBITS", list(range(6)), add6, 0,
                          {k: tuple([(i + k) % 2 for i in range(2)]
                                    + [2 + (i + k) % 3 for i in range(3)])
                           for k in range(6)}, 5)
    notg = synthetic_arena("CTRL-NOT-A-GROUP", [0, 1], add3, 0,
                           {0: (0, 1, 2), 1: (1, 2, 0)}, 3)
    for r in (reg, triv, six, notg):
        t = {"groups": 1, "classes": r["classes"], "species": r["irreps"]}
        probes.append({"row": r["row"], "carrier_points": r["carrier_points"],
                       "group_order": r["group_order"],
                       "species": r["irreps"], "hosted": r["hosted"],
                       "closes": r["selection_closes"],
                       "status": r["status"],
                       "emitted": head_law([r], t),
                       "second_law": second_head_law([r], t)})
    words = set()
    for p in probes:
        h = p["emitted"]
        for tok in ("SPC-INVENTORY", "SPC-CARRIER-SELECTS",
                    "SPC-SELECTION-CLOSED", "SPC-SELECTION-OPEN",
                    "SPC-BLOCKED-AT", "SPC-STATISTICS-SPLITS"):
            if tok in h:
                words.add(tok)
    if mut("MUT-CONTROL"):
        probes[3]["emitted"] = probes[0]["emitted"]
        words = {w for w in words if w != "SPC-BLOCKED-AT"}
    declared = {"SPC-INVENTORY", "SPC-CARRIER-SELECTS", "SPC-SELECTION-CLOSED",
                "SPC-SELECTION-OPEN", "SPC-BLOCKED-AT",
                "SPC-STATISTICS-SPLITS"}
    both_laws = all(p["emitted"] == p["second_law"] for p in probes)
    kn = any(p["hosted"] == p["species"] and p["status"] == "MEASURED"
             for p in probes)
    klt = any(p["hosted"] < p["species"] and p["status"] == "MEASURED"
              for p in probes)
    LD.gate("G-HEAD-LAW-REACHABILITY",
            "every pre-registered outcome word is EMITTED by the head law "
            "from a measurement, on an arena driven through the same census "
            "functions the delivered rows use: no field of any control row "
            "is written from outside, both selection words are reached, both "
            "arms of the carrier word are reached, the refusal word is "
            "reached by a set of permutations that is measured not to be a "
            "group, and the second head law returns the same string at every "
            "probe",
            words == declared and both_laws and kn and klt
            and len({p["emitted"] for p in probes}) == len(probes),
            "%d probes emitting %d distinct heads and the words %s; both "
            "head laws agree at every probe: %s"
            % (len(probes), len({p["emitted"] for p in probes}),
               sorted(words), both_laws))
    S["control_arms"] = probes
    SEAL.take("THE CONTROL ARMS", "control_arms", "G-HEAD-LAW-REACHABILITY",
              probes)


def measure_the_feasibility(S):
    """THE #299 ENGRAVING, discharged in the other direction: not only that
    every word CAN be emitted, but which of them were live at THIS arena
    before the run, with the delivered row that witnesses each."""
    rows = S["_rows"]
    def witness(pred):
        hit = [r["row"] for r in rows if pred(r)]
        return hit[0] if hit else ""
    fr = [
        {"outcome": "SPC-INVENTORY", "arm": "THE-COUNTS",
         "live_at_this_arena": True,
         "witnessed_by_a_delivered_row": witness(lambda r: True),
         "why": "the census is a total exact computation over finite "
                "groups, so its numbers are its outcome"},
        {"outcome": "SPC-CARRIER-SELECTS", "arm": "EVERY-SPECIES-HOSTED",
         "live_at_this_arena":
             any(r["homeless"] == 0 for r in rows),
         "witnessed_by_a_delivered_row":
             witness(lambda r: r["homeless"] == 0),
         "why": "a module rich enough to contain every species of its "
                "group"},
        {"outcome": "SPC-CARRIER-SELECTS", "arm": "SOME-SPECIES-HOMELESS",
         "live_at_this_arena": any(r["homeless"] > 0 for r in rows),
         "witnessed_by_a_delivered_row":
             witness(lambda r: r["homeless"] > 0),
         "why": "a module whose group is larger than the carrier can "
                "resolve"},
        {"outcome": "SPC-SELECTION-CLOSED", "arm": "THE-COMPOSITES-STAY",
         "live_at_this_arena": any(r["selection_closes"] for r in rows),
         "witnessed_by_a_delivered_row":
             witness(lambda r: r["selection_closes"]),
         "why": "a hosted set closed under the composite"},
        {"outcome": "SPC-SELECTION-OPEN", "arm": "THE-COMPOSITES-EXIT",
         "live_at_this_arena": any(not r["selection_closes"] for r in rows),
         "witnessed_by_a_delivered_row":
             witness(lambda r: not r["selection_closes"]),
         "why": "a hosted set that is a proper and non-closed subset"},
        {"outcome": "SPC-STATISTICS-SPLITS", "arm": "ALL-IN-BOTH-SHAPES",
         "live_at_this_arena":
             any(r["in_both_shapes"] == r["irreps"] for r in rows),
         "witnessed_by_a_delivered_row":
             witness(lambda r: r["in_both_shapes"] == r["irreps"]),
         "why": "a module whose two squares are both rich enough"},
        {"outcome": "SPC-STATISTICS-SPLITS", "arm": "A-PROPER-SPLIT",
         "live_at_this_arena":
             any(r["in_both_shapes"] < r["irreps"] for r in rows),
         "witnessed_by_a_delivered_row":
             witness(lambda r: r["in_both_shapes"] < r["irreps"]),
         "why": "a module whose squares differ in what they host"},
        {"outcome": "SPC-BLOCKED-AT", "arm": "INSTRUMENT-FAULT",
         "live_at_this_arena": False, "witnessed_by_a_delivered_row": "",
         "why": "it fires only on an instrument fault; it is demonstrated "
                "on a synthetic arena and reached by no delivered row"},
    ]
    if mut("MUT-FEASIBILITY"):
        fr[2]["live_at_this_arena"] = False
    live = [f for f in fr if f["live_at_this_arena"]]
    LD.gate("G-OUTCOME-FEASIBILITY-AT-THIS-ARENA",
            "the feasibility of every pre-registered word is measured AT "
            "THIS ARENA and not only in the controls: each arm carries the "
            "delivered row that witnesses it, an arm claimed live must name "
            "one, and the one arm that no delivered row can reach is "
            "declared unreachable here and demonstrated only "
            "synthetically -- so no outcome is pre-registered that the arena "
            "had already decided",
            all(bool(f["witnessed_by_a_delivered_row"])
                == f["live_at_this_arena"] for f in fr)
            and len(live) == len(fr) - 1,
            "%d outcome arms, %d live at this arena, each witnessed by a "
            "delivered row" % (len(fr), len(live)))
    S["outcome_feasibility"] = {"rows": fr, "arms": len(fr),
                                "live_at_this_arena": len(live)}
    SEAL.take("THE OUTCOME FEASIBILITY", "outcome_feasibility",
              "G-OUTCOME-FEASIBILITY-AT-THIS-ARENA", S["outcome_feasibility"])


# ===========================================================================
# SECTION 12.  THE VERDICT
# ===========================================================================

def build_verdict(S):
    tot = S["group_inventory"]["totals"]
    rows = S["carrier_census"]["rows"]
    head = S["verdict_head"]
    inv = S["group_inventory"]["rows"]
    idl = S["identity_layer"]["rows"]
    ch = S["crystallization_chain"]
    ot = S["odd_twist_species"]
    sel = S["selection"]
    st = S["statistics"]
    seg = [head]
    seg.append("INVENTORY=%d-GROUPS-AT-ORDERS-%s-OF-WHICH-%d-CARRY-A-FULL-"
               "EXACT-TABLE-AND-%d-STAND-ABOVE-THE-DECLARED-CAP-%d;"
               "CLASSES=%d;SPECIES=%d"
               % (tot["groups"],
                  ",".join(str(o) for o in tot["orders"]),
                  tot["groups_with_a_table"],
                  tot["groups_above_the_table_cap"], tot["the_table_cap"],
                  tot["classes"], tot["species"]))
    seg.append("IRREPS=EVERY-TABLE-GATED-BY-TWO-ROUTES-COLUMN-ORTHOGONALITY-"
               "AND-ROW-ORTHOGONALITY-AS-SEPARATE-GATES-WITH-THE-CLASS-"
               "EQUATION-AND-THE-DEGREE-SUM-BESIDE-THEM;THE-NINE-ACTOR-TABLE-"
               "IS-INTEGER-VALUED-WITH-%d-CLASSES-AND-%d-SPECIES-ITS-DEGREES-"
               "RE-DERIVED-BY-THE-HOOK-LENGTH-FORMULA;TWO-ENGINES-AGREE-ON-"
               "%d-SYMMETRIC-GROUPS"
               % (S["symmetric_census"]["classes"],
                  S["symmetric_census"]["species"], len(S["two_engines"])))
    hosted = sum(r["hosted"] for r in rows)
    avail = sum(r["irreps"] for r in rows)
    hl = [r for r in rows if r["homeless"] > 0]
    seg.append("CARRIER=%d-ROWS-OVER-%d-DECLARED-CARRIERS;%d-OF-%d-SPECIES-"
               "HOSTED;%d-ROWS-LEAVE-A-SPECIES-HOMELESS-THE-WIDEST-%s-AT-%d-"
               "OF-%d;THE-136-CARRIER-CLASSES-AND-THE-80-AT-THE-EXTENSION-"
               "ARE-THE-TRIVIAL-SPECIES-MULTIPLICITY-BY-TWO-ROUTES"
               % (len(rows), len(S["carrier_census"]["carriers"]), hosted,
                  avail, len(hl),
                  max(rows, key=lambda r: r["homeless"])["row"],
                  max(rows, key=lambda r: r["homeless"])["hosted"],
                  max(rows, key=lambda r: r["homeless"])["irreps"]))
    seg.append("PRICE=ONE-SPECIES:THE-ODD-TWIST-SPECIES-CARRIES-"
               "MULTIPLICITY-%d-AT-THE-ANCHORED-READING-AND-%d-AT-THE-"
               "EXTENSION-WHICH-ARE-EXACTLY-THE-PARENTS-IDENTIFIED-ORBIT-"
               "PAIRS;THE-PARENTS-PINNED-OBSERVABLE-%s-IS-NON-ZERO-AT-%d-OF-"
               "%d-POINTS-AND-LIES-IN-%d-ISOTYPIC-COMPONENT;%d-OF-%d-ORBIT-"
               "SUMS-VANISH"
               % (ot["rows"][0]["multiplicity"], ot["rows"][1]["multiplicity"],
                  ot["the_observable"],
                  ot["points_where_the_observable_does_not_vanish"],
                  S["coin_arena"]["coins"],
                  ot["its_non_vanishing_isotypic_components"],
                  ot["orbits_where_the_observable_sums_to_zero"],
                  ot["orbits_of_the_acting_group"]))
    seg.append("IDENTITY=THE-SPECIES-WITH-AN-INVARIANT-VECTOR-ALONG-THE-"
               "MEASURED-STABILIZER-LATTICE-ARE-%s-OF-%d;ALONG-THE-"
               "CRYSTALLIZATION-CHAIN-%s-SO-CRYSTALLIZATION-RESTORES-THE-"
               "INVENTORY-AT-PREFIX-%d;BRANCHING-BY-TWO-ROUTES-AT-%d-PAIRS-"
               "WITH-%d-DISAGREEMENTS-AND-A-TABLEAU-THIRD-ROUTE-AT-%d-ROWS"
               % (",".join(str(r["species_with_an_invariant_vector"])
                           for r in idl), idl[0]["of"],
                  ",".join(str(r["species_with_an_invariant_vector"])
                           for r in ch["rows"]),
                  ch["the_crystallization_time"],
                  S["identity_layer"]["branching_pairs"],
                  S["identity_layer"]["route_disagreements"],
                  len(S["identity_layer"]["species_rows"])))
    seg.append("SELECTION=%d-COMPOSITE-RULES;%d-ROWS-CLOSE-AND-%d-EXIT;"
               "THE-DISTINGUISHED-ROW-%s-EXITS-TO-%d-SPECIES-IT-DOES-NOT-HOST"
               % (sel["composite_rules"], sel["rows_that_close"],
                  sel["rows_that_exit"], sel["the_distinguished_row"],
                  [r["species_the_composites_exit_to"] for r in sel["rows"]
                   if r["row"] == sel["the_distinguished_row"]][0]))
    seg.append("STATISTICS=THE-SELECTED-SHAPE-IS-%s-DERIVED-FROM-%d-LEAK-"
               "CELLS-AGAINST-%d;%d-SPECIES-IN-BOTH-SHAPES,%d-SYMMETRIC-"
               "ONLY,%d-ANTISYMMETRIC-ONLY,%d-IN-NEITHER;%d-OF-%d-ROWS-SPLIT-"
               "PROPERLY"
               % (st["the_selected_shape"],
                  st["the_parents_antisymmetric_leak_cells"],
                  st["the_parents_symmetric_leak_cells"],
                  st["aggregate"]["in_both_shapes"],
                  st["aggregate"]["symmetric_only"],
                  st["aggregate"]["antisymmetric_only"],
                  st["aggregate"]["in_neither_shape"],
                  st["rows_that_split_properly"], len(st["rows"])))
    seg.append("ROUTES=ORBITS-BY-CHARACTER-AND-BY-UNION-FIND-AT-%d-ROWS;"
               "COMPOSITES-BY-TWO-CONTRACTIONS;SQUARES-BY-FORMULA-AND-BY-"
               "COUNTING-ON-THE-PAIR-SET;BRANCHING-BY-RESTRICTION-AND-BY-"
               "FROBENIUS-RECIPROCITY;INVARIANTS-BY-TABLEAU-COUNT;ORDERS-BY-"
               "CLOSURE-AND-CLASS-EQUATION-AND-ORBIT-STABILIZER;ZERO-"
               "DISAGREEMENTS-EVERYWHERE"
               % len(rows))
    seg.append("CONTROLS=%d-SYNTHETIC-ARENAS-THROUGH-THE-SAME-CENSUS-"
               "FUNCTIONS-EMITTING-%d-DISTINCT-HEADS;%d-OF-%d-OUTCOME-ARMS-"
               "ARE-LIVE-AT-THIS-ARENA-EACH-WITNESSED-BY-A-DELIVERED-ROW"
               % (len(S["control_arms"]),
                  len({p["emitted"] for p in S["control_arms"]}),
                  S["outcome_feasibility"]["live_at_this_arena"],
                  S["outcome_feasibility"]["arms"]))
    seg.append("SCOPE=THE-KINEMATIC-HALF-ONLY;LABELS-COMPOSITES-AND-"
               "STATISTICS-COMPATIBILITY;NO-MASS-NO-SPECTRUM-NO-STABILITY-NO-"
               "REALIZED-PARTICLE-CLAIM;NO-STANDARD-MODEL-IDENTIFICATION;NO-"
               "SI-NUMBER;NO-CONTINUUM-CLAIM;COUNTS-ARE-COUNTING-ONLY;THE-"
               "TABLE-CAP-IS-%d-AND-%d-ACTING-GROUPS-STAND-ABOVE-IT-WITH-"
               "THEIR-ORDERS-RE-DERIVED-AND-THE-CARRIER-SEEING-THEM-THROUGH-"
               "A-GROUP-OF-ORDER-8-OR-16;THE-CARRIER-ROW-LIST-IS-A-"
               "DECLARATION"
               % (tot["the_table_cap"], tot["groups_above_the_table_cap"]))
    return " -- ".join(seg)


def reconstruct_verdict(P):
    """the INDEPENDENT reconstruction: it reads only the serialized receipt,
    derives the head by the second law, and re-renders every segment from
    the primitive measured tables -- reading neither the builder's segments
    nor its aggregates and sharing no format string with it."""
    rows = []
    for r in P["carrier_census"]["rows"]:
        rows.append({"status": r["status"], "blocked_at": r["blocked_at"],
                     "hosted": r["hosted"], "irreps": r["irreps"],
                     "composite_rules": r["composite_rules"],
                     "selection_closes": r["selection_closes"],
                     "in_both_shapes": r["in_both_shapes"],
                     "symmetric_only": r["symmetric_only"],
                     "antisymmetric_only": r["antisymmetric_only"],
                     "in_neither_shape": r["in_neither_shape"]})
    inv = P["group_inventory"]["rows"]
    tot = {"groups": len(inv),
           "classes": sum(r["classes"] for r in inv),
           "species": sum(r["species"] for r in inv)}
    out = [second_head_law(rows, tot)]
    orders = sorted({r["order"] for r in inv})
    cap = P["acting_groups"]["table_cap"]
    above = len([r for r in inv if r["above_the_table_cap"]])
    with_table = len(inv) - above
    out.append("INVENTORY=" + str(len(inv)) + "-GROUPS-AT-ORDERS-"
               + ",".join([str(o) for o in orders]) + "-OF-WHICH-"
               + str(with_table) + "-CARRY-A-FULL-EXACT-TABLE-AND-"
               + str(above) + "-STAND-ABOVE-THE-DECLARED-CAP-" + str(cap)
               + ";CLASSES=" + str(tot["classes"]) + ";SPECIES="
               + str(tot["species"]))
    sc = P["symmetric_census"]
    out.append("IRREPS=EVERY-TABLE-GATED-BY-TWO-ROUTES-COLUMN-ORTHOGONALITY-"
               "AND-ROW-ORTHOGONALITY-AS-SEPARATE-GATES-WITH-THE-CLASS-"
               "EQUATION-AND-THE-DEGREE-SUM-BESIDE-THEM;THE-NINE-ACTOR-TABLE-"
               "IS-INTEGER-VALUED-WITH-" + str(sc["classes"])
               + "-CLASSES-AND-" + str(sc["species"]) + "-SPECIES-ITS-"
               "DEGREES-RE-DERIVED-BY-THE-HOOK-LENGTH-FORMULA;TWO-ENGINES-"
               "AGREE-ON-" + str(len(P["two_engines"])) + "-SYMMETRIC-GROUPS")
    cr = P["carrier_census"]["rows"]
    worst = cr[0]
    for r in cr:
        if r["homeless"] > worst["homeless"]:
            worst = r
    out.append("CARRIER=" + str(len(cr)) + "-ROWS-OVER-"
               + str(len(sorted({r["carrier"] for r in cr})))
               + "-DECLARED-CARRIERS;"
               + str(sum(r["hosted"] for r in cr)) + "-OF-"
               + str(sum(r["irreps"] for r in cr)) + "-SPECIES-HOSTED;"
               + str(len([r for r in cr if r["homeless"] > 0]))
               + "-ROWS-LEAVE-A-SPECIES-HOMELESS-THE-WIDEST-" + worst["row"]
               + "-AT-" + str(worst["hosted"]) + "-OF-" + str(worst["irreps"])
               + ";THE-136-CARRIER-CLASSES-AND-THE-80-AT-THE-EXTENSION-ARE-"
                 "THE-TRIVIAL-SPECIES-MULTIPLICITY-BY-TWO-ROUTES")
    ot = P["odd_twist_species"]
    out.append("PRICE=ONE-SPECIES:THE-ODD-TWIST-SPECIES-CARRIES-MULTIPLICITY-"
               + str(ot["rows"][0]["multiplicity"]) + "-AT-THE-ANCHORED-"
               "READING-AND-" + str(ot["rows"][1]["multiplicity"])
               + "-AT-THE-EXTENSION-WHICH-ARE-EXACTLY-THE-PARENTS-IDENTIFIED-"
                 "ORBIT-PAIRS;THE-PARENTS-PINNED-OBSERVABLE-"
               + ot["the_observable"] + "-IS-NON-ZERO-AT-"
               + str(ot["points_where_the_observable_does_not_vanish"])
               + "-OF-" + str(P["coin_arena"]["coins"]) + "-POINTS-AND-LIES-"
                 "IN-" + str(ot["its_non_vanishing_isotypic_components"])
               + "-ISOTYPIC-COMPONENT;"
               + str(ot["orbits_where_the_observable_sums_to_zero"]) + "-OF-"
               + str(ot["orbits_of_the_acting_group"]) + "-ORBIT-SUMS-VANISH")
    idl = P["identity_layer"]["rows"]
    ch = P["crystallization_chain"]
    out.append("IDENTITY=THE-SPECIES-WITH-AN-INVARIANT-VECTOR-ALONG-THE-"
               "MEASURED-STABILIZER-LATTICE-ARE-"
               + ",".join([str(r["species_with_an_invariant_vector"])
                           for r in idl]) + "-OF-" + str(idl[0]["of"])
               + ";ALONG-THE-CRYSTALLIZATION-CHAIN-"
               + ",".join([str(r["species_with_an_invariant_vector"])
                           for r in ch["rows"]])
               + "-SO-CRYSTALLIZATION-RESTORES-THE-INVENTORY-AT-PREFIX-"
               + str(ch["the_crystallization_time"]) + ";BRANCHING-BY-TWO-"
                 "ROUTES-AT-" + str(P["identity_layer"]["branching_pairs"])
               + "-PAIRS-WITH-"
               + str(P["identity_layer"]["route_disagreements"])
               + "-DISAGREEMENTS-AND-A-TABLEAU-THIRD-ROUTE-AT-"
               + str(len(P["identity_layer"]["species_rows"])) + "-ROWS")
    sel = P["selection"]
    dist = [r for r in sel["rows"] if r["row"] == sel["the_distinguished_row"]]
    out.append("SELECTION=" + str(sel["composite_rules"])
               + "-COMPOSITE-RULES;" + str(sel["rows_that_close"])
               + "-ROWS-CLOSE-AND-" + str(sel["rows_that_exit"]) + "-EXIT;"
               "THE-DISTINGUISHED-ROW-" + sel["the_distinguished_row"]
               + "-EXITS-TO-" + str(dist[0]["species_the_composites_exit_to"])
               + "-SPECIES-IT-DOES-NOT-HOST")
    st = P["statistics"]
    ag = st["aggregate"]
    out.append("STATISTICS=THE-SELECTED-SHAPE-IS-" + st["the_selected_shape"]
               + "-DERIVED-FROM-"
               + str(st["the_parents_antisymmetric_leak_cells"])
               + "-LEAK-CELLS-AGAINST-"
               + str(st["the_parents_symmetric_leak_cells"]) + ";"
               + str(ag["in_both_shapes"]) + "-SPECIES-IN-BOTH-SHAPES,"
               + str(ag["symmetric_only"]) + "-SYMMETRIC-ONLY,"
               + str(ag["antisymmetric_only"]) + "-ANTISYMMETRIC-ONLY,"
               + str(ag["in_neither_shape"]) + "-IN-NEITHER;"
               + str(st["rows_that_split_properly"]) + "-OF-"
               + str(len(st["rows"])) + "-ROWS-SPLIT-PROPERLY")
    out.append("ROUTES=ORBITS-BY-CHARACTER-AND-BY-UNION-FIND-AT-"
               + str(len(cr)) + "-ROWS;COMPOSITES-BY-TWO-CONTRACTIONS;"
                 "SQUARES-BY-FORMULA-AND-BY-COUNTING-ON-THE-PAIR-SET;"
                 "BRANCHING-BY-RESTRICTION-AND-BY-FROBENIUS-RECIPROCITY;"
                 "INVARIANTS-BY-TABLEAU-COUNT;ORDERS-BY-CLOSURE-AND-CLASS-"
                 "EQUATION-AND-ORBIT-STABILIZER;ZERO-DISAGREEMENTS-"
                 "EVERYWHERE")
    ca = P["control_arms"]
    fe = P["outcome_feasibility"]
    out.append("CONTROLS=" + str(len(ca)) + "-SYNTHETIC-ARENAS-THROUGH-THE-"
               "SAME-CENSUS-FUNCTIONS-EMITTING-"
               + str(len({p["emitted"] for p in ca}))
               + "-DISTINCT-HEADS;" + str(fe["live_at_this_arena"]) + "-OF-"
               + str(fe["arms"]) + "-OUTCOME-ARMS-ARE-LIVE-AT-THIS-ARENA-"
                 "EACH-WITNESSED-BY-A-DELIVERED-ROW")
    out.append("SCOPE=THE-KINEMATIC-HALF-ONLY;LABELS-COMPOSITES-AND-"
               "STATISTICS-COMPATIBILITY;NO-MASS-NO-SPECTRUM-NO-STABILITY-NO-"
               "REALIZED-PARTICLE-CLAIM;NO-STANDARD-MODEL-IDENTIFICATION;NO-"
               "SI-NUMBER;NO-CONTINUUM-CLAIM;COUNTS-ARE-COUNTING-ONLY;THE-"
               "TABLE-CAP-IS-" + str(cap) + "-AND-" + str(above)
               + "-ACTING-GROUPS-STAND-ABOVE-IT-WITH-THEIR-ORDERS-RE-DERIVED-"
                 "AND-THE-CARRIER-SEEING-THEM-THROUGH-A-GROUP-OF-ORDER-8-OR-"
                 "16;THE-CARRIER-ROW-LIST-IS-A-DECLARATION")
    return " -- ".join(out)


# ===========================================================================
# SECTION 13.  THE CHOICE INVENTORY
# ===========================================================================

def price_the_choices(S):
    rows = S["_rows"]
    inv = S["group_inventory"]["rows"]
    c = []
    c.append({"choice": "THE-GROUP-INVENTORY-LIST", "class": "DECLARED-AND-"
              "DISCLOSED", "fibre": "UNBOUNDED",
              "instances_built": len(inv), "verdict_determining": True,
              "measured": True,
              "why": "the head's first segment is a count over this list; a "
                     "group added or dropped moves it, and the list is every "
                     "group the corpus's own terminals measured"})
    c.append({"choice": "THE-CARRIER-ROW-LIST", "class": "DECLARED-AND-"
              "DISCLOSED", "fibre": "UNBOUNDED",
              "instances_built": len(rows), "verdict_determining": True,
              "measured": True,
              "why": "the carrier segment is a count over this list; both "
                     "arms of the hosting verdict are populated by delivered "
                     "rows, so adding one cannot flip the word, but it moves "
                     "the numbers"})
    c.append({"choice": "THE-TABLE-CAP", "class": "DECLARED-AND-SWEPT",
              "fibre": "UNBOUNDED", "instances_built": 1,
              "verdict_determining": False, "measured": True,
              "why": "raising it would add species counts to the inventory "
                     "segment but cannot change any carrier row, because the "
                     "carrier is measured to see the four groups above the "
                     "cap through a group whose table is computed"})
    c.append({"choice": "THE-CHART-READING", "class": "DECLARED-AND-SWEPT",
              "fibre": 2, "instances_built": 2,
              "verdict_determining": False, "measured": True,
              "why": "both readings are run at every carrier they act on, "
                     "and the price species is measured at both"})
    c.append({"choice": "THE-LOCALITY-GRAIN", "class": "DECLARED-AND-SWEPT",
              "fibre": 3, "instances_built": 3,
              "verdict_determining": False, "measured": True,
              "why": "all three grains are run; the carrier is measured to "
                     "see the same group at every one"})
    c.append({"choice": "THE-COIN-FAMILY-AND-THE-LATTICE", "class": "FORCED",
              "fibre": 1, "instances_built": 1,
              "verdict_determining": False, "measured": True,
              "why": "the parent's own arena, rebuilt and gated against its "
                     "receipt"})
    c.append({"choice": "THE-NINE-ACTOR-GRAIN", "class": "GRANTED-BY-THE-"
              "PARENT", "fibre": 1, "instances_built": 1,
              "verdict_determining": True, "measured": False,
              "why": "the identity side is the parent's granted grain; the "
                     "factorization question is another unit's and the "
                     "species count of the actor row would move with it"})
    c.append({"choice": "THE-STABILIZER-LATTICE", "class": "INHERITED",
              "fibre": 1, "instances_built": len(STABILIZER_SHAPES),
              "verdict_determining": True, "measured": True,
              "why": "the six nontrivial shapes are the parent's measured "
                     "ones, read at named receipt paths; the identity "
                     "segment is a count over them"})
    c.append({"choice": "THE-CRYSTALLIZATION-FLAG", "class": "EXHIBITED",
              "fibre": "UNBOUNDED", "instances_built": 1,
              "verdict_determining": False, "measured": True,
              "why": "the parent published stabilizer ORDERS along the "
                     "chain, not the partitions; a nested flag realising "
                     "those orders is exhibited here and its invariant "
                     "counts depend only on the shapes, which the orders fix"
                     " at every step of this chain"})
    c.append({"choice": "THE-SELECTED-SHAPE", "class": "DERIVED", "fibre": 1,
              "instances_built": 1, "verdict_determining": True,
              "measured": True,
              "why": "which shape the occupancy census selected is derived "
                     "from that unit's own two leak counts and not declared "
                     "here"})
    c.append({"choice": "THE-DISTINGUISHED-COMPOSITE-ROW", "class":
              "DECLARED-AND-DISCLOSED", "fibre": len(rows),
              "instances_built": 1, "verdict_determining": False,
              "measured": True,
              "why": "the full composite table is published for one row; "
                     "the closure verdict is measured at every row"})
    c.append({"choice": "THE-SYNTHETIC-CONTROL-ARENAS", "class":
              "DECLARED-AND-DISCLOSED", "fibre": "UNBOUNDED",
              "instances_built": len(S["control_arms"]),
              "verdict_determining": False, "measured": True,
              "why": "they demonstrate the outcome vocabulary; they enter no "
                     "delivered count"})
    vd = sum(1 for r in c if r["verdict_determining"])
    ms = sum(1 for r in c if r["measured"])
    if mut("MUT-CHOICE-INVENTORY"):
        c[1]["instances_built"] = len(rows) - 1
    LD.gate("G-CHOICE-INVENTORY",
            "every construction choice is inventoried with its class, its "
            "fibre, the instances this unit built and whether it is "
            "verdict-determining, and the instance counts are RECOUNTED from "
            "the objects they describe rather than typed beside them",
            c[0]["instances_built"] == len(inv)
            and c[1]["instances_built"] == len(rows)
            and c[7]["instances_built"] == len(STABILIZER_SHAPES)
            and c[11]["instances_built"] == len(S["control_arms"]),
            "%d choices, %d verdict-determining, %d with a measured flag"
            % (len(c), vd, ms))
    S["choices"] = {"rows": c, "verdict_determining": vd,
                    "flag_measured_at": ms}
    SEAL.take("THE CHOICE INVENTORY", "choices", "G-CHOICE-INVENTORY",
              S["choices"])


# ===========================================================================
# SECTION 14.  THE REGISTRY, TOTAL AND HONESTLY DESCRIBED (E-23)
# ===========================================================================

FUNCTION_INVENTORY = (
    "__init__", "_reduce", "add", "add3", "add6", "ag_act_cell",
    "ag_act_site", "ag_apply", "ag_cells", "ag_matmul", "ag_mul",
    "ag_point_group", "ag_sites", "apply_point", "assemble_the_inventory",
    "bdigest", "build_claims", "build_coin_alphabet", "build_coin_family",
    "build_the_arenas", "build_the_carrier_rows", "build_verdict",
    "build_waiver_ledger", "centralizer_order", "chart_elements",
    "chart_stabilizer_of", "check_the_arithmetic", "check_the_registry",
    "class_data", "class_matrices", "close_group", "coin_sector",
    "coin_swap", "coin_twist", "conj", "conjugacy_classes", "coords",
    "ct_from_sym", "ct_from_young", "cyc_int", "cycle_perm",
    "cycle_type_of", "cyclotomic", "declared_function_names", "degrees",
    "demonstrate_the_outcome_words", "dig", "digest", "dixon_prime",
    "dixon_table", "exponent", "find", "fuse", "gate", "gauge_image_of",
    "gen", "gf_nullspace", "gf_rref", "harvest", "head_law",
    "hook_dimension", "ifact", "igcd", "ilcm", "inner", "inv", "inverses",
    "iprod", "is_closed", "is_prime", "is_zero", "isqrt_exact", "kostka",
    "lat_addv", "lat_boundary", "lat_links", "lat_sites", "link_ends",
    "load_sources", "main", "measure_path_values", "measure_provenance",
    "measure_the_acting_groups", "measure_the_crystallization_chain",
    "measure_the_feasibility", "measure_the_identity_layer",
    "measure_the_odd_twist_species", "measure_the_selection_rules",
    "measure_the_statistics_tie_in", "measure_the_symmetric_census",
    "measure_the_two_engines", "measure_verbatim", "mn_char", "mnorm",
    "mul", "multiplicities", "mut", "normsq", "numword", "order_of",
    "own_source", "pair_characters", "partitions", "perm_compose",
    "plaquette_image", "point_on_dir", "point_symmetries",
    "poly_divmod_exact", "price_a_census_row", "price_the_choices",
    "prime_factors", "project", "quartic_sign", "rational", "read_bytes",
    "realisable_constant_twists", "rec", "reconstruct_verdict",
    "render_cell", "render_table", "resolve", "reverify", "rim_hooks",
    "row_gate_failures", "run", "say", "scal", "seal_and_write",
    "second_head_law", "selftest", "sentences_of", "split_eigenspaces",
    "stencil_action_mul", "stencil_of", "strips", "sub", "sym_class_size",
    "sym_group_as_permutations", "sym_inner", "sym_table",
    "sym_table_gates", "synthetic_arena", "table_gates", "table_rows",
    "take", "tensor_decompose", "to_str", "transported_link",
    "union_find_orbits", "verify_paper", "verify_the_consumers", "witness",
    "wsnorm", "young_centralizer", "young_char", "young_class_size",
    "young_dim", "young_subgroup", "zpow")


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
            "comparison outside the switch's own body -- is fatal rather "
            "than forgiven",
            not unswept and not unfired and not unreadable,
            "%d switches in the tree, %d declared; undeclared %s; declared "
            "without a branch %s; unreadable switch present %s"
            % (len(switches), len(declared), unswept[:4], unfired[:4],
               unreadable))
    bad = []
    for name, target, what, token in MUTANTS:
        if mut("MUT-FALSIFIER-DESCRIPTION") and name == "MUT-GAMMA":
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
    "G-ARTIFACT-INTEGRITY": "evaluated only in the writing path, which no "
                            "diagnostic run reaches; its reference value is "
                            "the GATE-TIME SEAL, whose in-run twin "
                            "G-SEAL-INTEGRITY carries the injection "
                            "falsifier MUT-SEAL, and whose unsealed-key leg "
                            "is a total byte comparison of the receipt "
                            "against the string this run built",
}

EXTERNAL_BATTERY = {
    "G-MUTANTS-ON-TARGET": "no such gate exists in this instrument; the "
                           "sweep is adjudicated by the CLI harness and "
                           "every surviving or off-target injection fails "
                           "it, which is an external-battery result",
}

REFUSAL_ONLY_GATES = {
    "G-PAPER-PRESENT": "a constant refusal reached only when the paper is "
                       "absent, so it never closes on a clean run and "
                       "appears in no total of closed gates",
}

LATE_GATES = ("G-FALSIFIER-COVERAGE-AT-AN-HONEST-DENOMINATOR",
              "G-LEDGER-CHAIN-VERIFIED", "G-LEDGER-SHAPE-IS-CONSISTENT",
              "G-PAPER-CLAIMS", "G-PAPER-VERDICT-EQUALITY",
              "G-MUST-NOT-VOCABULARY", "G-PAPER-POLARITY",
              "G-PAPER-TABLES-AND-QUOTES-ARE-BOUND",
              "G-PAPER-NUMERAL-COVERAGE", "G-CONSUMERS-ARE-REAL",
              "G-MUST-NOT-OVER-THE-RECEIPT", "G-SEAL-INTEGRITY",
              "G-ARTIFACT-INTEGRITY")


def build_waiver_ledger(S):
    closed = [r["gate"] for r in LD.rows]
    covered = sorted({m[1] for m in MUTANTS} & set(closed))
    if mut("MUT-WAIVER"):
        covered = covered[:-1]
    late = sorted(set(LATE_GATES) - set(closed))
    lcov = {}
    for gx in LATE_GATES:
        hit = sorted({m[0] for m in MUTANTS if m[1] == gx})
        if hit:
            lcov[gx] = "FALSIFIER:" + ",".join(hit)
        elif gx in FORCINGS:
            lcov[gx] = "FORCING"
        else:
            lcov[gx] = "UNCOVERED"
    forced = sorted(set(FORCINGS) & set(closed + list(LATE_GATES)))
    uncovered = [g for g in closed if g not in covered and g not in FORCINGS]
    allg = sorted(set(closed) | set(LATE_GATES) | set(FORCINGS))
    unc_all = [g for g in allg
               if g not in {m[1] for m in MUTANTS} and g not in FORCINGS]
    S["waiver_ledger"] = {
        "gates_closed_when_this_ledger_is_taken": len(closed),
        "gates_on_the_clean_path": len(allg),
        "covered_by_a_declared_falsifier": len(covered),
        "under_a_registered_forcing": len(forced),
        "the_forcings": FORCINGS, "uncovered": uncovered,
        "uncovered_over_every_gate_on_the_clean_path": unc_all,
        "late_gates_declared": list(LATE_GATES),
        "late_gates_not_yet_closed_when_this_ledger_is_taken": late,
        "late_gate_coverage": lcov,
        "the_denominator": "EVERY-GATE-ON-THE-CLEAN-PATH-INCLUDING-THE-LATE-"
                           "ONES-THIS-LEDGER-IS-TAKEN-BEFORE",
        "the_external_battery": EXTERNAL_BATTERY,
        "refusal_only_gates": REFUSAL_ONLY_GATES}
    LD.gate("G-FALSIFIER-COVERAGE-AT-AN-HONEST-DENOMINATOR",
            "the coverage is published at an honest denominator (#34), and "
            "the denominator is EVERY gate on the clean path and not only "
            "the ones already closed when this ledger is taken: each is "
            "either the declared target of a falsifier that REACHES it or "
            "carries a registered forcing stating why no falsifier can, the "
            "late gates are listed one by one with which of the two covers "
            "them, and the gate that exists only to refuse and the external "
            "battery's own adjudication are named in registries of their own "
            "so that no row of this one can never fire",
            not uncovered and not unc_all,
            "%d gates closed here and %d on the clean path; %d carry a "
            "declared falsifier, %d a registered forcing, %d uncovered %s; "
            "late gates %d, each covered: %s"
            % (len(closed), len(allg), len(covered), len(forced),
               len(unc_all), unc_all[:5], len(LATE_GATES),
               sorted(set(lcov.values()))))
    SEAL.take("THE WAIVER LEDGER", "waiver_ledger",
              "G-FALSIFIER-COVERAGE-AT-AN-HONEST-DENOMINATOR",
              S["waiver_ledger"])
    chain = [digest({"prev": "GENESIS" if i == 0 else LD.digests[i - 1],
                     "row": r}) for i, r in enumerate(LD.rows)]
    if mut("MUT-CHAIN"):
        LD.digests[0] = "000000000000"
    bad = [i for i in range(len(chain)) if chain[i] != LD.digests[i]]
    LD.gate("G-LEDGER-CHAIN-VERIFIED",
            "the chained ledger is VERIFIED and not merely built: every "
            "published per-row digest is recomputed here from its own "
            "predecessor and its own row and compared element by element, "
            "and the same chain is recomputed at the disk boundary from the "
            "bytes that were read back",
            not bad, "%d chained rows recomputed, %d mismatching %s"
            % (len(chain), len(bad), bad[:4]))


# ===========================================================================
# SECTION 15.  THE PAPER GATES AND THE FOUR WALLS
# ===========================================================================

DIGEST_KEYS = {"pinned", "measured", "digest", "code_sha256_12",
               "paper_sha256_12", "pin_sha256_prefix"}
DIGEST_RE = re.compile(r"\b(?=[0-9a-f]{12}\b)(?=[0-9a-f]*[a-f])"
                       r"[0-9a-f]{12}\b")
POOL_EXCLUDED = {"mutants"}

# THE FOUR WALLS.  Each is a list of banned forms matched at word boundaries
# over the whole paper, with the declaring sentences removed first.
WALLS = [
    ("WALL-DYNAMIC",
     ["mass", "masses", "massive", "spectrum", "spectra", "spectral",
      "energy", "energies", "hamiltonian", "lifetime", "decay", "decays",
      "unstable", "stability", "eigenvalue", "eigenvalues"],
     "THE DYNAMIC VOCABULARY IS BEHIND ANOTHER DOOR.  This unit measures "
     "which species can exist -- labels, composites, statistics "
     "compatibility -- and nothing about which are realized or with what "
     "values.  That question is its successor's and waits on the "
     "potential unit's gate."),
    ("WALL-IDENTIFICATION",
     ["electron", "quark", "photon", "gluon", "neutrino", "boson",
      "bosonic", "fermion", "fermionic", "hadron", "lepton", "higgs",
      "standard model", "isospin", "hypercharge", "flavour", "flavor"],
     "NO OUTSIDE IDENTIFICATION IS MADE.  No sentence of this paper names "
     "an outside theory's particle as an identification of any species it "
     "measures.  The pin licenses structural comparisons stamped ANALOGY; "
     "this paper draws none, so the licence is registered and unused and "
     "the wall's positive leg is total."),
    ("WALL-SI",
     ["gev", "mev", "kev", "tev", "electronvolt", "kilogram", "kilograms",
      "joule", "joules", "kelvin", "hertz", "metres", "meters",
      "nanometre", "planck length", "planck mass"],
     "NO SI NUMBER APPEARS.  Every number in this paper is a count, a "
     "group order, a degree, a multiplicity or an exact rational; none "
     "carries a unit."),
    ("WALL-LIMIT",
     ["continuum", "continuous", "infinite volume", "thermodynamic limit",
      "scaling limit", "renormalisation", "renormalization"],
     "NO LIMIT CLAIM IS MADE.  Every group here is finite, every carrier "
     "is finite, and no statement is made about any limit."),
]

# the declaring sentences the sweep may remove.  Every entry must be
# LOCATED: an exemption carried and never used is a hole, not a courtesy.
DECLARING = [
    "no mass, no spectrum, no stability and no realized-particle claim is "
    "made here",
    "NO-MASS-NO-SPECTRUM-NO-STABILITY-NO-REALIZED-PARTICLE-CLAIM",
    "NO-STANDARD-MODEL-IDENTIFICATION",
    "NO-SI-NUMBER;NO-CONTINUUM-CLAIM",
]

# THE POSITIVE LEG.  A ban list refuses only what it lists; a paraphrase
# walks past it.  So every sentence that puts a species word in the same
# sentence as a word of the declared outside register must be one of the
# wall statements themselves.
OUTSIDE_REGISTER = ["particle", "matter", "the world", "physical reality",
                    "the universe", "fundamental", "elementary"]
SPECIES_WORDS = ["species", "irrep", "irreducible"]

RECEIPT_WITHHOLDING = [
    "NO-MASS-NO-SPECTRUM-NO-STABILITY-NO-REALIZED-PARTICLE-CLAIM",
    "NO-STANDARD-MODEL-IDENTIFICATION",
    "NO-SI-NUMBER;NO-CONTINUUM-CLAIM",
]

PAPER_TABLES = (
    ("THE-GROUP-INVENTORY", "group_inventory/rows",
     ("group", "order", "classes", "species", "engine",
      "carrier_it_is_censused_on")),
    ("THE-ACTING-GROUPS", "acting_groups/rows",
     ("grain", "reading", "gauge_image_order", "chart_stabilizer_order",
      "acting_group_order", "the_group_the_carrier_sees",
      "induced_classes_on_the_carrier")),
    ("THE-CARRIER-CENSUS", "carrier_census/rows",
     ("row", "group_order", "carrier_points", "classes", "irreps", "hosted",
      "homeless", "orbits_by_the_character")),
    ("THE-ODD-TWIST-SPECIES", "odd_twist_species/rows",
     ("row", "the_species_index", "multiplicity",
      "the_arena_groups_orbit_count", "the_acting_groups_orbit_count",
      "the_parents_identified_orbit_pairs")),
    ("THE-IDENTITY-LATTICE", "identity_layer/rows",
     ("row", "orbit_shape", "order_by_construction", "classes",
      "species_of_its_own", "prefixes_the_parent_measured_here",
      "species_with_an_invariant_vector")),
    ("THE-CRYSTALLIZATION-CHAIN", "crystallization_chain/rows",
     ("prefix_length", "stabilizer_order", "the_parents_order",
      "orbit_shape", "species_with_an_invariant_vector")),
    ("THE-DISTINGUISHED-BRANCHING", "identity_layer/the_distinguished_"
     "branching", ("species", "degree", "constituents",
                   "invariant_dimension")),
    ("THE-SELECTION-CENSUS", "selection/rows",
     ("row", "hosted", "composite_rules", "species_the_composites_exit_to",
      "selection_closes")),
    ("THE-COMPOSITE-TABLE", "selection/the_composite_table",
     ("left", "right", "composite_species", "multiplicities",
      "exits_the_hosted_set")),
    ("THE-STATISTICS-CENSUS", "statistics/rows",
     ("row", "species", "in_both_shapes", "symmetric_only",
      "antisymmetric_only", "in_neither_shape")),
    ("THE-TWO-ENGINES", "two_engines",
     ("row", "order", "classes_dixon", "classes_murnaghan_nakayama",
      "tables_agree")),
    ("THE-CONTROL-ARMS", "control_arms",
     ("row", "group_order", "species", "hosted", "status", "emitted")),
    ("THE-OUTCOME-FEASIBILITY", "outcome_feasibility/rows",
     ("outcome", "arm", "live_at_this_arena",
      "witnessed_by_a_delivered_row")),
    ("THE-WALLS", "walls/rows",
     ("wall", "banned_forms", "found", "statement")),
    ("THE-CHOICE-INVENTORY", "choices/rows",
     ("choice", "class", "fibre", "instances_built", "verdict_determining",
      "measured")),
)


def table_rows(S, path):
    cur = S
    for part in path.split("/"):
        cur = cur[part]
    return cur


def render_cell(v):
    if isinstance(v, bool):
        return "yes" if v else "no"
    if isinstance(v, list):
        return "[" + ", ".join(str(x) for x in v) + "]"
    return str(v)


def render_table(S, path, keys):
    """the header from the receipt KEYS and every data row from the receipt
    VALUES, rendered by one function so a header and its column cannot drift
    apart."""
    out = [" | ".join(k.replace("_", " ") for k in keys)]
    for r in table_rows(S, path):
        if not all(k in r for k in keys):
            continue
        out.append(" | ".join(render_cell(r[k]) for k in keys))
    return out


def build_claims(S):
    """the paper's load-bearing sentences, RENDERED FROM THE RECEIPT, each
    with the number of times it must occur."""
    tot = S["group_inventory"]["totals"]
    cc = S["carrier_census"]
    ot = S["odd_twist_species"]
    idl = S["identity_layer"]
    ch = S["crystallization_chain"]
    sel = S["selection"]
    st = S["statistics"]
    sc = S["symmetric_census"]
    ca = S["coin_arena"]
    ia = S["identity_arena"]
    ls = S["ledger_shape"]
    c = []
    c.append(("%d groups, %d of which carry a full exact character table and "
              "%d of which stand above the declared cap of %d"
              % (tot["groups"], tot["groups_with_a_table"],
                 tot["groups_above_the_table_cap"], tot["the_table_cap"]), 1))
    c.append(("%d conjugacy classes and %d species in all"
              % (tot["classes"], tot["species"]), 1))
    for _n, _p, _k in PAPER_TABLES:
        for line in render_table(S, _p, _k):
            c.append((line, 1))
    c.append(("%d coins, splitting into %d diagonal, %d antidiagonal and %d "
              "balanced" % (ca["coins"], ca["sectors"]["DIAGONAL"],
                            ca["sectors"]["ANTIDIAGONAL"],
                            ca["sectors"]["BALANCED"]), 1))
    c.append(("%d sites, %d declared link directions and %d cells"
              % (ia["sites"], ia["declared_link_directions"], ia["cells"]), 1))
    c.append(("the arena group has order %d and the pinned chart group %d"
              % (ia["arena_group_order"], ia["chart_group_order"]), 1))
    c.append(("%d carrier rows over %d declared carriers"
              % (cc["rows_measured"], len(cc["carriers"])), 1))
    c.append(("%d of %d species are hosted"
              % (cc["species_hosted"], cc["species_available"]), 1))
    c.append(("%d of the %d rows leave at least one species homeless"
              % (cc["rows_with_a_homeless_species"], cc["rows_measured"]), 1))
    c.append(("multiplicity %d at the anchored reading and %d at the "
              "extension" % (ot["rows"][0]["multiplicity"],
                             ot["rows"][1]["multiplicity"]), 1))
    c.append(("non-zero at %d of the %d coins"
              % (ot["points_where_the_observable_does_not_vanish"],
                 ca["coins"]), 1))
    c.append(("%d of the %d orbit sums vanish"
              % (ot["orbits_where_the_observable_sums_to_zero"],
                 ot["orbits_of_the_acting_group"]), 1))
    c.append(("%d branching multiplicities by both routes, at %d "
              "disagreements" % (idl["branching_pairs"],
                                 idl["route_disagreements"]), 1))
    c.append(("%d tableau counts, at %d disagreements"
              % (len(idl["species_rows"]), idl["tableau_route_disagreements"]),
              1))
    c.append(("from %d at the largest measured stabilizer to %d at "
              "crystallization" % (ch["species_at_the_first_prefix"],
                                   ch["species_at_crystallization"]), 1))
    c.append(("%d composite rules" % sel["composite_rules"], 1))
    c.append(("%d rows close and %d exit"
              % (sel["rows_that_close"], sel["rows_that_exit"]), 1))
    c.append(("%d species in both shapes, %d in the symmetric shape alone, "
              "%d in the antisymmetric shape alone and %d in neither"
              % (st["aggregate"]["in_both_shapes"],
                 st["aggregate"]["symmetric_only"],
                 st["aggregate"]["antisymmetric_only"],
                 st["aggregate"]["in_neither_shape"]), 1))
    c.append(("%d of the %d rows split properly"
              % (st["rows_that_split_properly"], len(st["rows"])), 1))
    c.append(("leaks at %d cells against %d"
              % (st["the_parents_antisymmetric_leak_cells"],
                 st["the_parents_symmetric_leak_cells"]), 1))
    c.append(("%d classes and %d species, its degrees re-derived by the "
              "hook-length formula" % (sc["classes"], sc["species"]), 1))
    c.append(("the squares of its degrees sum to %d"
              % sc["degree_sum_of_squares"], 1))
    c.append(("%d synthetic arenas" % len(S["control_arms"]), 1))
    c.append(("%d of the %d outcome arms are live at this arena"
              % (S["outcome_feasibility"]["live_at_this_arena"],
                 S["outcome_feasibility"]["arms"]), 1))
    c.append(("%d gates close before the paper gates, and %d paper gates, %d "
              "receipt-wall gate and %d closing gates follow"
              % (ls["gates_closed_before_the_paper_gates"], ls["paper_gates"],
                 ls["receipt_gates"], ls["closing_gates"]), 1))
    c.append(("%d objects are sealed before the paper gates"
              % ls["objects_sealed_before_the_paper_gates"], 1))
    c.append(("%d construction choices are inventoried, of which %d are "
              "verdict-determining"
              % (len(S["choices"]["rows"]),
                 S["choices"]["verdict_determining"]), 1))
    c.append(("%d file-bytes anchors, %d path-value anchors and %d "
              "verbatim-text anchors, %d anchors in all"
              % (S["anchor_classes"]["file_bytes"],
                 S["anchor_classes"]["path_value"],
                 S["anchor_classes"]["verbatim_text"],
                 S["anchor_classes"]["total"]), 2))
    c.append(("%d declared mutants" % len(MUTANTS), 1))
    c.append(("%d float literals" % S["arithmetic"][
        "float_literals_in_this_source"], 1))
    for _nm, rel_path, sha, _what in SOURCES:
        if sha:
            c.append(("`%s` (`%s`)" % (rel_path, sha), 1))
    c.append(("returns %s elements" % numword(ca["alphabet"]), 1))
    c.append(("a point group of order %s"
              % numword(ia["point_group_order"]), 1))
    return c


POLARITY = [
    ("the coin carrier hosts every species of every group that acts on it",
     1),
    ("the species inventory is not carrier-independent", 1),
    ("the composites do not close", 1),
    ("the price is one species", 2),
    ("the observable lies in that species and in no other", 1),
    ("crystallization does not destroy the inventory, it restores it", 1),
    ("the trivial species is not compatible with the selected shape at\n      the actor row", 1),
    ("this is the kinematic half only", 1),
    ("the licence is registered and unused", 1),
]


def sentences_of(text):
    body = re.sub(r"```.*?```", " ", text, flags=re.S)
    body = re.sub(r"^\|.*$", " ", body, flags=re.M)
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+|\n\n", body)
            if s.strip()]


def verify_paper(S, paper_text):
    ptext = paper_text
    if mut("MUT-CLAIM"):
        ptext = ptext.replace(
            "%d composite rules" % S["selection"]["composite_rules"],
            "999999 composite rules", 1)
    if mut("MUT-TABLE-ROW"):
        a = re.search(r"^(\|\s*CELL-27-UNDER-TRANS-9\s*\|)(.*)$", ptext, re.M)
        b = re.search(r"^(\|\s*CELL-27-UNDER-EXT-108\s*\|)(.*)$", ptext, re.M)
        if a and b:
            ptext = ptext.replace(a.group(0), a.group(1) + b.group(2), 1)
            ptext = ptext.replace(b.group(0), b.group(1) + a.group(2), 1)
    if mut("MUT-QUOTE-FIDELITY"):
        ptext = ptext.replace("antisymmetric shape leaks at 0",
                              "antisymmetric shape leaks at 81", 1)
    if mut("MUT-TABLE-BINDING"):
        ptext = ptext + "\n\n| a | b |\n|---|---|\n| planted | 4242 |\n"
    if mut("MUT-MUST-NOT"):
        ptext = ptext + "\n\nThe species carries a mass and its spectrum is "
        ptext = ptext + "the observable one.\n"
    if mut("MUT-WALL-PARAPHRASE"):
        ptext = ptext + "\n\nThis species is the elementary carrier of the "
        ptext = ptext + "world's own label.\n"
    if mut("MUT-COVERAGE"):
        ptext = ptext + "\n\nan uncovered numeral 987654321\n"
    sw = mnorm(ptext)
    inert = [d[:40] for d in DECLARING if mnorm(d) not in sw]
    for d in DECLARING:
        sw = sw.replace(mnorm(d), " ")
    hits = []
    wallrows = []
    for wname, banned, _stmt in WALLS:
        h = [w for w in banned
             if re.search(r"\b" + re.escape(w) + r"\b", sw)]
        hits.extend(h)
        wallrows.append({"wall": wname, "banned_forms": len(banned),
                         "found": len(h), "statement": _stmt})
    sents = sentences_of(ptext)
    allowed = [mnorm(s) for _n, _b, s in WALLS] + [mnorm(d) for d in DECLARING]
    near = []
    for s in sents:
        ls = mnorm(s)
        if any(re.search(r"\b" + re.escape(w) + r"\b", ls)
               for w in OUTSIDE_REGISTER) and \
                any(re.search(r"\b" + re.escape(w) + r"", ls)
                    for w in SPECIES_WORDS):
            if not any(a in ls or ls in a for a in allowed):
                near.append(s[:70])
    LD.gate("G-MUST-NOT-VOCABULARY",
            "the four walls are evaluated against this paper's own "
            "characters and each has TWO legs.  The first is a list of "
            "banned forms, matched at word boundaries with the declaring "
            "sentences removed first, and every declaring sentence the sweep "
            "may remove must itself be LOCATED here.  The second is "
            "POSITIVE, because a ban list refuses only what it lists and a "
            "paraphrase walks past it: every sentence putting a species word "
            "beside a word of the declared outside register must be one of "
            "the wall statements themselves, and nothing else is allowed",
            not hits and not inert and not near,
            "banned forms found: %s; %d declaring sentences, %d not located "
            "%s; %d sentences reaching the outside register %s"
            % (hits[:4], len(DECLARING), len(inert), inert[:2], len(near),
               near[:2]))
    S["walls"] = {"rows": wallrows,
                  "banned_forms": sum(r["banned_forms"] for r in wallrows),
                  "declaring_sentences": len(DECLARING),
                  "sentences_scanned": len(sents),
                  "outside_register_words": len(OUTSIDE_REGISTER),
                  "species_words": len(SPECIES_WORDS),
                  "the_analogy_licence": "REGISTERED-AND-UNUSED"}
    SEAL.take("THE WALLS", "walls", "G-MUST-NOT-VOCABULARY", S["walls"])

    claims = build_claims(S)
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
        blocks = blocks + [wsnorm(verdict).replace("SPC-", "XPC-")]
    LD.gate("G-PAPER-VERDICT-EQUALITY",
            "the paper's verdict block is compared for EQUALITY against the "
            "string this run emits, under whitespace normalisation, and the "
            "paper's fenced blocks are gated by MULTISET EQUALITY against "
            "the single block this run licenses (E-22) -- so neither a stale "
            "verdict nor a forged twin riding beside the clean one can be "
            "delivered",
            blocks == [wsnorm(verdict)],
            "%d fenced blocks; %d equal to this run's verdict of %d "
            "characters" % (len(blocks),
                            sum(1 for b in blocks if b == wsnorm(verdict)),
                            len(verdict)))


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
        stx = line.strip()
        if not stx.startswith("|"):
            continue
        if re.match(sep, stx):
            continue
        nxt = plines[i + 1].strip() if i + 1 < len(plines) else ""
        if re.match(sep, nxt):
            theads.append(stx)
            continue
        trows.append(stx)
    if mut("MUT-TABLE-HEADER"):
        _cols = theads[0].strip("|").split("|")
        theads = ["|" + "|".join(_cols[::-1]) + "|"] + theads[1:]
    claim_texts = [mnorm(fr) for fr, _w in claims]
    unbound_rows = [r[:70] for r in trows
                    if not any(ct and ct in mnorm(r) for ct in claim_texts)]
    unbound_heads = [r[:70] for r in theads
                     if not any(ct and ct in mnorm(r) for ct in claim_texts)]
    quotes, blk = [], []
    for line in plines:
        stx = line.strip()
        if stx.startswith(">"):
            blk.append(stx[1:].strip())
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
            "every DATA row of every delivered table must be covered by a "
            "claim rendered from the receipt, EVERY HEADER ROW is bound the "
            "same way -- each rendered from the receipt keys its own columns "
            "are, so two semantically opposed columns exchanged in the paper "
            "stop matching -- and every BLOCKQUOTE must lie inside one of "
            "the pinned verbatim windows, so a paper that misquotes or "
            "inverts a parent's own sentence dies here even though the "
            "anchor on the parent's bytes passes",
            not unbound_rows and not unbound_quotes and not unbound_heads,
            "%d table data rows, %d unbound %s; %d header rows, %d unbound "
            "%s; %d blockquotes, %d not inside a pinned window %s"
            % (len(trows), len(unbound_rows), unbound_rows[:2], len(theads),
               len(unbound_heads), unbound_heads[:2], len(quotes),
               len(unbound_quotes), unbound_quotes[:2]))
    S["paper_binding"] = {
        "table_data_rows": len(trows), "table_rows_unbound": len(unbound_rows),
        "table_header_rows": len(theads),
        "table_header_rows_unbound": len(unbound_heads),
        "tables_rendered_from_the_receipt": len(PAPER_TABLES),
        "blockquotes": len(quotes),
        "blockquotes_outside_a_pinned_verbatim_window": len(unbound_quotes),
        "verbatim_windows_available": len(VERBATIM)}
    SEAL.take("THE PAPER BINDING", "paper_binding",
              "G-PAPER-TABLES-AND-QUOTES-ARE-BOUND", S["paper_binding"])

    allowed_nums = set()

    def add(x):
        s = str(x)
        allowed_nums.add(s)
        if "/" in s:
            for side in s.split("/"):
                allowed_nums.add(side)

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
            for m in re.findall(r"\d+(?:/\d+)?", DIGEST_RE.sub(" ", o)):
                add(m)
    harvest({k: v for k, v in S.items()
             if not k.startswith("_") and k not in POOL_EXCLUDED})
    STRUCTURAL = ({str(k) for k in range(1, 16)}
                  | {"%d.%d" % (a, b) for a in range(1, 16)
                     for b in range(0, 13)})
    scan = re.sub(r"\((?:#\d+|E-\d+)(?:,\s*(?:#\d+|E-\d+))*\)", " ", ptext)
    scan = re.sub(r"`[0-9a-f]{12}`", " ", scan)
    nums = re.findall(r"\d+(?:/\d+)?(?:\.\d+)?", scan)
    unmatched = []
    for x in nums:
        if x in allowed_nums or x in STRUCTURAL:
            continue
        if "/" in x and all(p in allowed_nums for p in x.split("/")):
            continue
        unmatched.append(x)
    wre = r"\b(" + "|".join(sorted(NUMBER_WORDS, key=len, reverse=True)) \
        + r")\b"
    wscan = scan.lower()
    if mut("MUT-SPELLED-NUMERAL"):
        wscan = wscan + " an uncovered spelled numeral: seventy-nine "
    words = [w for w in re.findall(wre, wscan) if NUMBER_WORDS[w] >= 13]
    unmatched_words = sorted({w for w in words
                              if str(NUMBER_WORDS[w]) not in allowed_nums})
    spans = len(re.findall(r"`[^`]*\d[^`]*`", ptext))
    fenced = len(re.findall(r"```", ptext))
    LD.gate("G-PAPER-NUMERAL-COVERAGE",
            "EVERY numeral of the paper is matched against a value this run "
            "computed -- fenced blocks, verdict block, inline code spans and "
            "both sides of every fraction included (E-22, #20) -- with only "
            "a published list of structural literals forgiven, so a number "
            "invented in prose, or moved from one claim to another, dies "
            "inside the delivery run.  SPELLED NUMERALS ARE SCANNED THE SAME "
            "WAY (#267): every number-word above twelve, hyphenated "
            "compounds included, is mapped to its integer and matched "
            "against the same pool",
            not unmatched and not unmatched_words,
            "%d numerals scanned, %d spelled numerals above twelve, %d "
            "inline code spans carrying a numeral, %d fence markers, %d "
            "unmatched: %s; unmatched spelled: %s"
            % (len(nums), len(words), spans, fenced, len(unmatched),
               unmatched[:8], unmatched_words[:4]))
    S["paper_coverage"] = {
        "numerals_scanned": len(nums),
        "spelled_numerals_above_twelve_scanned": len(words),
        "spelled_numerals_unmatched": len(unmatched_words),
        "the_number_word_alphabet": "EVERY-ENGLISH-NUMBER-WORD-BELOW-ONE-"
                                    "HUNDRED-HYPHENATED-COMPOUNDS-INCLUDED",
        "inline_spans_with_a_numeral": spans, "fence_markers": fenced,
        "unmatched": len(unmatched),
        "removed_from_the_scan_and_bound_as_claims":
            "THE-PARENTHESISED-ENGRAVING-REFERENCES-AND-THE-BACKTICKED-"
            "TWELVE-HEX-DIGESTS",
        "digest_valued_keys_excluded_from_the_pool": sorted(DIGEST_KEYS),
        "published_objects_excluded_from_the_pool": sorted(POOL_EXCLUDED),
        "structural_literals_forgiven": sorted(STRUCTURAL)}
    SEAL.take("THE PAPER COVERAGE", "paper_coverage",
              "G-PAPER-NUMERAL-COVERAGE", S["paper_coverage"])
    verify_the_consumers(S)


def verify_the_consumers(S):
    """every anchor names the gate that consumes it; this checks that the
    named gate EXISTS in this run's ledger and that it PASSED."""
    rows = S["path_value_anchors"] + S["verbatim_anchors"]
    if mut("MUT-CONSUMER"):
        rows = [dict(rows[0], consumer="G-DOES-NOT-EXIST")] + rows[1:]
    names = sorted({r["consumer"] for r in rows})
    missing = [g for g in names if g not in LD.ids]
    passed = {r["gate"]: r["passed"] for r in LD.rows}
    failed = [g for g in names if passed.get(g) is False]
    LD.gate("G-CONSUMERS-ARE-REAL",
            "every anchor's declared CONSUMER is a gate that exists in this "
            "run's own ledger and that passed: the register is checked "
            "against the ledger rather than published beside it, so an "
            "anchor bound to a gate this instrument does not have stops the "
            "delivery run instead of being vouched by prose",
            not missing and not failed,
            "%d anchors naming %d distinct consumer gates; %d naming a gate "
            "that does not exist %s; %d naming a gate that did not pass %s"
            % (len(rows), len(names), len(missing), missing[:3], len(failed),
               failed[:3]))
    S["consumer_register"] = {
        "anchors": len(rows), "distinct_consumer_gates": len(names),
        "consumers_that_do_not_exist": len(missing),
        "consumers_that_did_not_pass": len(failed),
        "the_consumer_gates": names}
    SEAL.take("THE CONSUMER REGISTER", "consumer_register",
              "G-CONSUMERS-ARE-REAL", S["consumer_register"])


# ===========================================================================
# SECTION 16.  THE FALSIFIER REGISTRY (E-23: each names the token it plants)
# ===========================================================================

MUTANTS = [
    ("MUT-SOURCE-DRIFT", "G-SOURCE-BYTES",
     "replaces one pinned source's measured digest with zeros",
     '"000000000000"'),
    ("MUT-PATH-VALUE", "G-PATH-VALUE-ANCHORS",
     "moves the inherited count of carrier classes to 999", "got = 999"),
    ("MUT-VERBATIM", "G-VERBATIM-ANCHORS",
     "inverts one verbatim window's own meaning, so it stops locating in "
     "the parent's pinned bytes", 'window.replace("would select"'),
    ("MUT-AST-BLIND", "G-ARITHMETIC-IS-EXACT",
     "plants a real float literal into the source text the AST gate parses",
     "_TOLERANCE_FLOAT = 1e-9"),
    ("MUT-FIELD-MODULUS", "G-CYCLOTOMIC-FIELD",
     "shifts every coefficient of the cyclotomic polynomial by one, so the "
     "field's own laws fail", "self.phi = [c + 1 for c in self.phi]"),
    ("MUT-COIN-FAMILY", "G-COIN-ARENA-REBUILT",
     "drops one coin from the rebuilt family", "coins = coins[:-1]"),
    ("MUT-GAMMA", "G-GAMMA-REBUILT",
     "replaces the swap conjugation by the identity, so the coin-map group "
     "is half the size", "sw = ident"),
    ("MUT-CHART", "G-CHART-GROUPS-REBUILT",
     "restricts the anchored chart group to its identity element",
     "els = els[:1]"),
    ("MUT-AG-POINT-GROUP", "G-AG23-ARENA-REBUILT",
     "drops one element of the identity arena's point group, so the arena "
     "group is no longer the largest the link set admits",
     "out = set(sorted(out)[:-1])"),
    ("MUT-CLASS-MATRIX", "G-CHARACTER-TABLE-ROW-ORTHOGONALITY",
     "adds one to a class multiplication coefficient, so the class sums no "
     "longer diagonalise", "M[1][0][0] = M[1][0][0] + 1"),
    ("MUT-CHARACTER-VALUE", "G-CARRIER-DECOMPOSITION",
     "adds one to a character value of the arena group, so its table stops "
     "being orthogonal", "F.add(table[3][1], F.one)"),
    ("MUT-MN-VALUE", "G-S9-TABLE",
     "moves one value of the nine-actor table off the rim-hook recursion",
     "T[5][3] = T[5][3] + 1"),
    ("MUT-TWO-ENGINES", "G-TWO-ENGINES-AGREE",
     "shifts one row of the combinatorial engine's table, so the two "
     "engines stop agreeing", "tuple(x + 1 for x in mnr[0])"),
    ("MUT-ABOVE-CAP", "G-ABOVE-THE-TABLE-CAP",
     "drops one gauge element at every grain, so the acting group orders "
     "stop matching the parent's", "gi = gi[:-1]"),
    ("MUT-CARRIER-SEES", "G-THE-CARRIER-SEES-ONE-GROUP",
     "drops one coin map from the group the carrier sees at one row, so the "
     "six rows no longer agree", "diag = diag[:-1]"),
    ("MUT-CARRIER-MULT", "G-CARRIER-DECOMPOSITION",
     "adds one to every multiplicity of one carrier row, so the module's "
     "dimension no longer closes", "mult = [m + 1 for m in mult]"),
    ("MUT-STATISTICS-ROUTE", "G-CARRIER-DECOMPOSITION",
     "moves the counted symmetric character at one row off the formula's "
     "value", "s_count = s_count + 1"),
    ("MUT-SELECTION", "G-SELECTION-CLOSURE-CENSUS",
     "empties the exit set at every row, so the closure census loses its "
     "second arm", "exits = set()"),
    ("MUT-HOMELESS", "G-CARRIER-HOMELESS-CENSUS",
     "declares every species hosted at every row, so the homelessness "
     "census loses an arm", 'r["homeless"] = 0'),
    ("MUT-ODD-TWIST", "G-THE-ODD-TWIST-SPECIES",
     "adds two more isotypic components to the pinned observable, so it no "
     "longer lies in one species",
     "nonzero_components = nonzero_components + [0, 1]"),
    ("MUT-ORBIT-ROUTE", "G-CARRIER-ORBITS-TWO-ROUTES",
     "gives the anchored coin row the extension row's orbit pair, so the "
     "parent's own four counts are no longer re-derived",
     'orb["COIN-640-UNDER-ACTING-LINK-8"] = orb["COIN-640-UNDER-GAMMA-16"]'),
    ("MUT-DROP-SPECIES", "G-CHARACTER-TABLE-COLUMN-ORTHOGONALITY",
     "drops the last species from the nine-actor table -- which leaves ROW "
     "orthogonality intact and breaks only the column route, so it is the "
     "falsifier that shows the two routes are independent gates",
     'ct9 = dict(ct9, table=ct9["table"][:-1])'),
    ("MUT-BRANCHING", "G-IDENTITY-BRANCHING-TWO-ROUTES",
     "adds one to a restriction multiplicity, so the subgroup route and the "
     "reciprocity route disagree", 'mult[0] = mult[0] + 1'),
    ("MUT-LATTICE-SHAPE", "G-IDENTITY-LATTICE-IS-THE-PARENTS",
     "moves every stabilizer's order-by-construction off its own class "
     "equation", '1 if mut("MUT-LATTICE-SHAPE") else 0'),
    ("MUT-STATISTICS-SPLIT", "G-STATISTICS-SPLIT-CENSUS",
     "adds one species to the four-class split, so the classes no longer "
     "exhaust the row counts",
     'tot["in_neither_shape"] = tot["in_neither_shape"] + 1'),
    ("MUT-INVENTORY", "G-GROUP-INVENTORY-IS-TOTAL",
     "drops one group from the published inventory", "inv = inv[:-1]"),
    ("MUT-ORDER-ROUTE", "G-GROUP-INVENTORY-ORDERS-RE-DERIVED",
     "moves one of the parent's four published group orders by one, so the "
     "inventory stops reproducing them",
     'parent_orders["GAMMA-16"] = parent_orders["GAMMA-16"] + 1'),
    ("MUT-KOSTKA", "G-KOSTKA-ROUTE",
     "adds one to a tableau count, so the third route stops agreeing with "
     "the trivial multiplicity", "kk = kk + 1"),
    ("MUT-CHAIN-FLAG", "G-CRYSTALLIZATION-CHAIN-IS-NESTED",
     "moves one stabilizer order of the exhibited flag off the parent's "
     "published profile", "order = order + 1"),
    ("MUT-SELECTED-SHAPE", "G-OCC-SELECTED-SHAPE",
     "declares the selected shape to be the one that leaks",
     'selected = "SYMMETRIC"'),
    ("MUT-CONTROL", "G-HEAD-LAW-REACHABILITY",
     "collapses the refusal probe onto the first probe's head, so the "
     "refusal word is no longer emitted",
     'probes[3]["emitted"] = probes[0]["emitted"]'),
    ("MUT-FEASIBILITY", "G-OUTCOME-FEASIBILITY-AT-THIS-ARENA",
     "declares a live outcome arm dead while its witness row stands",
     'fr[2]["live_at_this_arena"] = False'),
    ("MUT-CHOICE-INVENTORY", "G-CHOICE-INVENTORY",
     "leaves one carrier row out of the choice inventory's own count",
     'c[1]["instances_built"] = len(rows) - 1'),
    ("MUT-HEAD", "G-HEAD-DERIVED-TWICE",
     "types the head instead of computing it",
     '"SPC-INVENTORY-EVERYTHING"'),
    ("MUT-VERDICT-COMPARATOR", "G-VERDICT-RECONSTRUCTION",
     "corrupts the builder's verdict string after it is built",
     'verdict.replace("SPC-", "SPC-X-", 1)'),
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
    ("MUT-WAIVER", "G-FALSIFIER-COVERAGE-AT-AN-HONEST-DENOMINATOR",
     "removes one gate from the covered set, so a closed gate is left "
     "uncovered", "covered = covered[:-1]"),
    ("MUT-CHAIN", "G-LEDGER-CHAIN-VERIFIED",
     "corrupts one published chain digest after its row closed",
     'LD.digests[0] = "000000000000"'),
    ("MUT-CLAIM", "G-PAPER-CLAIMS",
     "corrupts a load-bearing count in the paper text the claim gate scans",
     '"999999 composite rules"'),
    ("MUT-TABLE-ROW", "G-PAPER-CLAIMS",
     "swaps two table rows under their own labels in the scanned text",
     "a.group(1) + b.group(2)"),
    ("MUT-QUOTE-FIDELITY", "G-PAPER-TABLES-AND-QUOTES-ARE-BOUND",
     "inverts a quoted measurement in the scanned paper text",
     '"antisymmetric shape leaks at 81"'),
    ("MUT-TABLE-BINDING", "G-PAPER-TABLES-AND-QUOTES-ARE-BOUND",
     "adds an unbound table carrying a numeral to the scanned text",
     '"\\n\\n| a | b |\\n|---|---|\\n| planted | 4242 |\\n"'),
    ("MUT-TABLE-HEADER", "G-PAPER-TABLES-AND-QUOTES-ARE-BOUND",
     "exchanges the column names of a delivered table's header row in the "
     "scanned text", 'theads[0].strip("|").split("|")'),
    ("MUT-VERDICT-TWIN", "G-PAPER-VERDICT-EQUALITY",
     "adds a forged twin of the verdict fence beside the clean one",
     '"XPC-"'),
    ("MUT-MUST-NOT", "G-MUST-NOT-VOCABULARY",
     "plants a dynamic-vocabulary sentence into the scanned text",
     "The species carries a mass and its spectrum is "),
    ("MUT-WALL-PARAPHRASE", "G-MUST-NOT-VOCABULARY",
     "plants an identification-shaped sentence carrying NO banned token at "
     "all, so only the wall's positive leg can catch it",
     "This species is the elementary carrier of the "),
    ("MUT-POLARITY", "G-PAPER-POLARITY",
     "plants a declared negator immediately before a direction-bearing "
     "claim", '"it is false that "'),
    ("MUT-COVERAGE", "G-PAPER-NUMERAL-COVERAGE",
     "plants a numeral no value this run computed can license",
     "an uncovered numeral 987654321"),
    ("MUT-SPELLED-NUMERAL", "G-PAPER-NUMERAL-COVERAGE",
     "plants a spelled numeral above twelve that no value this run computed "
     "can license", "an uncovered spelled numeral: seventy-nine"),
    ("MUT-CONSUMER", "G-CONSUMERS-ARE-REAL",
     "points one anchor's declared consumer at a gate this instrument does "
     "not have", 'consumer="G-DOES-NOT-EXIST"'),
    ("MUT-MUST-NOT-RECEIPT", "G-MUST-NOT-OVER-THE-RECEIPT",
     "plants a must-not word into the serialized receipt the wall sweeps",
     "a spectrum in the receipt"),
    ("MUT-SEAL", "G-SEAL-INTEGRITY",
     "edits a sealed object after its gate closed", '"MOVED-AFTER-THE-GATE"'),
]


# ===========================================================================
# SECTION 17.  THE SEAL, THE ARTIFACTS, THE CLI
# ===========================================================================

PAPER_GATE_IDS = ("G-PAPER-CLAIMS", "G-PAPER-VERDICT-EQUALITY",
                  "G-MUST-NOT-VOCABULARY", "G-PAPER-POLARITY",
                  "G-PAPER-TABLES-AND-QUOTES-ARE-BOUND",
                  "G-PAPER-NUMERAL-COVERAGE", "G-CONSUMERS-ARE-REAL")
RECEIPT_GATE_IDS = ("G-MUST-NOT-OVER-THE-RECEIPT",)
CLOSING_GATE_IDS = ("G-SEAL-INTEGRITY", "G-ARTIFACT-INTEGRITY")

DECLARED_UNSEALED = {
    "unit": "the unit's own name, a constant of this source",
    "schema": "the receipt schema tag, a constant of this source",
    "python": "the interpreter's major.minor, environmental",
    "pin_sha256_prefix": "the pin digest, verified at G-SOURCE-BYTES",
    "paper_sha256_12": "the paper's digest, taken at the paper gates",
    "code_sha256_12": "this instrument's own digest, which cannot seal "
                      "itself",
    "gates": "the gate ledger, snapshotted before the receipt wall and the "
             "two closing gates -- a seal cannot be inside the object it "
             "seals",
    "gate_digests": "the CHAINED per-row digests of that ledger",
    "seal_manifest": "the manifest itself",
    "closing_gates": "the two gates that close last of all; the receipt "
                     "wall closes after the snapshot too and is counted in "
                     "the totals",
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
        "gates": len(LD.rows) + len(RECEIPT_GATE_IDS) + len(CLOSING_GATE_IDS),
        "gates_in_the_sealed_ledger": len(LD.rows),
        "gates_that_close_after_this_snapshot":
            len(RECEIPT_GATE_IDS) + len(CLOSING_GATE_IDS),
        "closing_gates": len(payload["closing_gates"]),
        "mutants": len(MUTANTS), "sources": len(SOURCES),
        "path_value_anchors": len(PATH_VALUES),
        "verbatim_anchors": len(VERBATIM),
        "anchors": len(SOURCES) + len(PATH_VALUES) + len(VERBATIM),
        "sealed_objects": len(SEAL.man),
        "paper_gates": len(PAPER_GATE_IDS),
        "receipt_gates": len(RECEIPT_GATE_IDS),
        "gates_possible_including_the_refusal_only_gate":
            len(LD.rows) + len(RECEIPT_GATE_IDS) + len(CLOSING_GATE_IDS)
            + len(REFUSAL_ONLY_GATES),
        "the_refusal_only_gate": sorted(REFUSAL_ONLY_GATES),
        "carrier_rows": len(S["carrier_census"]["rows"]),
        "groups": S["group_inventory"]["totals"]["groups"]}
    if mut("MUT-SEAL"):
        payload["coin_arena"] = dict(payload["coin_arena"])
        payload["coin_arena"]["coins"] = "MOVED-AFTER-THE-GATE"
    unsealed = [k for k in payload
                if k not in SEAL.by_key and k not in DECLARED_UNSEALED]
    moved = SEAL.reverify(payload)
    rtext = json.dumps({k: v for k, v in payload.items()
                        if k not in POOL_EXCLUDED},
                       sort_keys=True, default=str)
    if mut("MUT-MUST-NOT-RECEIPT"):
        rtext = rtext + " a spectrum in the receipt"
    rlow = mnorm(rtext)
    rinert = [d[:40] for d in RECEIPT_WITHHOLDING if mnorm(d) not in rlow]
    for d in RECEIPT_WITHHOLDING:
        rlow = rlow.replace(mnorm(d), " ")
    rhits = []
    for _wn, banned, _st in WALLS:
        rhits.extend([w for w in banned
                      if re.search(r"\b" + re.escape(w) + r"\b", rlow)])
    LD.gate("G-MUST-NOT-OVER-THE-RECEIPT",
            "the four walls' vocabulary is swept over the SERIALIZED RECEIPT "
            "as well as over the paper, with the withholding strings this "
            "unit publishes removed first and the falsifier registry -- "
            "which describes its own injections -- excluded by key.  Every "
            "withholding string the sweep may remove must itself be LOCATED "
            "in the receipt, so an exemption carried and never used is a "
            "hole rather than a courtesy",
            not rhits and not rinert,
            "banned vocabulary in the receipt: %s; %d withholding strings, "
            "%d not located %s"
            % (rhits[:4], len(RECEIPT_WITHHOLDING), len(rinert), rinert[:3]))
    ids = [r["gate"] for r in LD.rows]
    ls = S.get("ledger_shape", {})
    shape_ok = ("paper_coverage" not in S) or (
        all(gx in ids for gx in PAPER_GATE_IDS)
        and all(gx in ids for gx in RECEIPT_GATE_IDS)
        and len(LD.rows) == ls.get("gates_closed_before_the_paper_gates", 0)
        + ls.get("paper_gates", 0) + ls.get("receipt_gates", 0))
    LD.gate("G-SEAL-INTEGRITY",
            "the manifest is TOTAL and the seal is checked before anything "
            "reaches the disk: every published top-level key is either "
            "digested at the moment its own gate passed or named in the "
            "declaration with the reason it cannot be, and every sealed "
            "object still matches its gate-time digest -- so an object "
            "edited after its gate closed dies here rather than being "
            "re-derived from disk and pronounced consistent (#119)",
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
    raw_receipt = open(tmps[1][0]).read()
    back = json.loads(raw_receipt)
    disk_bad = SEAL.reverify(back)
    txt_ok = open(tmps[0][0]).read() == outtxt
    blob_ok = raw_receipt == blob
    chain_ok = back["gate_digests"] == [
        digest({"prev": "GENESIS" if i == 0 else back["gate_digests"][i - 1],
                "row": r}) for i, r in enumerate(back["gates"])]
    if disk_bad or not txt_ok or not blob_ok or not chain_ok:
        for tmp, _p in tmps:
            if os.path.exists(tmp):
                os.remove(tmp)
    LD.gate("G-ARTIFACT-INTEGRITY",
            "the artifacts are compared against the GATE-TIME seals and not "
            "against a re-derivation, and the comparison happens BEFORE "
            "promotion: both files are written as temporaries, the receipt "
            "is read back from the filesystem and every sealed object must "
            "still carry its gate-time digest, the transcript must be "
            "byte-identical to the string this run emitted, THE RECEIPT MUST "
            "BE BYTE-IDENTICAL TOO -- which covers the declared-unsealed "
            "keys, the gate ledger and its chain among them -- and the chain "
            "is recomputed from the bytes read back.  A refusal removes the "
            "temporaries and leaves the published artifacts untouched",
            not disk_bad and txt_ok and blob_ok and chain_ok,
            "%d sealed objects moved on the way to disk %s; transcript "
            "byte-identical: %s; receipt byte-identical: %s; chained ledger "
            "verified from the bytes read back: %s"
            % (len(disk_bad), disk_bad[:3], txt_ok, blob_ok, chain_ok))
    for (tmp, p), data in zip(tmps, (outtxt, blob)):
        with open(tmp, "w") as fh:
            fh.write(data)
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
    check_the_arithmetic(S)
    say("  provenance: %d sources, %d path-value anchors, %d verbatim windows"
        % (len(SOURCES), len(PATH_VALUES), len(VERBATIM)))
    build_the_arenas(S, pv)
    say("  the gauge arena: %d coins, coin-map group %d; the identity arena: "
        "%d cells, arena group %d"
        % (S["coin_arena"]["coins"], S["coin_arena"]["coin_map_group_order"],
           S["identity_arena"]["cells"],
           S["identity_arena"]["arena_group_order"]))
    measure_the_acting_groups(S, pv)
    say("  the acting groups: orders %s; the carrier sees %s"
        % ([r["acting_group_order"] for r in S["acting_groups"]["rows"]],
           sorted({r["the_group_the_carrier_sees"]
                   for r in S["acting_groups"]["rows"]})))
    measure_the_two_engines(S)
    measure_the_symmetric_census(S, pv)
    say("  the nine-actor table: %d classes, %d species, degrees summing in "
        "squares to %d" % (S["symmetric_census"]["classes"],
                           S["symmetric_census"]["species"],
                           S["symmetric_census"]["degree_sum_of_squares"]))
    build_the_carrier_rows(S, pv)
    for r in S["_rows"]:
        say("    %-42s |G|=%-6d points=%-4d species=%-3d hosted=%-3d "
            "orbits=%d"
            % (r["row"], r["group_order"], r["carrier_points"], r["irreps"],
               r["hosted"], r["orbits_by_the_character"]))
    measure_the_odd_twist_species(S, pv)
    measure_the_identity_layer(S, pv)
    measure_the_crystallization_chain(S, pv, src)
    say("  the identity layer: species with an invariant vector %s; along "
        "the chain %s"
        % ([r["species_with_an_invariant_vector"]
            for r in S["identity_layer"]["rows"]],
           [r["species_with_an_invariant_vector"]
            for r in S["crystallization_chain"]["rows"]]))
    measure_the_selection_rules(S)
    measure_the_statistics_tie_in(S, pv)
    say("  selection: %d rows close, %d exit; statistics: the selected shape "
        "is %s, split %d/%d/%d/%d"
        % (S["selection"]["rows_that_close"], S["selection"]["rows_that_exit"],
           S["statistics"]["the_selected_shape"],
           S["statistics"]["aggregate"]["in_both_shapes"],
           S["statistics"]["aggregate"]["symmetric_only"],
           S["statistics"]["aggregate"]["antisymmetric_only"],
           S["statistics"]["aggregate"]["in_neither_shape"]))
    tot = assemble_the_inventory(S, pv)
    demonstrate_the_outcome_words(S, tot)
    measure_the_feasibility(S)
    price_the_choices(S)
    check_the_registry(S)

    head = head_law(S["_rows"], tot)
    h2 = second_head_law(S["_rows"], tot)
    if mut("MUT-HEAD"):
        head = "SPC-INVENTORY-EVERYTHING"
    LD.gate("G-HEAD-DERIVED-TWICE",
            "the head is derived TWICE, by two laws: the builder computes it "
            "from the live census, and an independent law written from the "
            "same pre-registered outcomes with a different branch structure "
            "and no shared format string returns the same string -- so a "
            "head typed rather than computed, or computed by a law that had "
            "drifted from its own measurements, dies here",
            head == h2, "builder %r; second law %r" % (head[:70], h2[:70]))
    S["verdict_head"] = head
    verdict = build_verdict(S)
    if mut("MUT-VERDICT-COMPARATOR"):
        verdict = verdict.replace("SPC-", "SPC-X-", 1)
    S["verdict"] = verdict
    payload_for_recon = json.loads(json.dumps(
        {k: v for k, v in S.items() if not k.startswith("_")},
        sort_keys=True, default=str))
    recon = reconstruct_verdict(payload_for_recon)
    LD.gate("G-VERDICT-RECONSTRUCTION",
            "the complete verdict string is compared for equality against an "
            "INDEPENDENT reconstruction that reads only the SERIALIZED "
            "receipt, derives the head by the second head law, and "
            "re-renders every segment from the primitive measured tables -- "
            "reading neither the builder's segments nor the builder's "
            "aggregates and sharing no format string with it",
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
          "receipt_gates": len(RECEIPT_GATE_IDS),
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
            and ls["paper_gates"] == len(PAPER_GATE_IDS)
            and ls["receipt_gates"] == len(RECEIPT_GATE_IDS),
            "%d sealed objects published against a manifest of %d; %d gates "
            "closed including this one; %d paper gates and %d receipt-wall "
            "gates declared"
            % (ls["objects_sealed_before_the_paper_gates"], len(SEAL.man),
               ls["gates_closed_before_the_paper_gates"], ls["paper_gates"],
               ls["receipt_gates"]))
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
    say("")
    say("GATES %d (+%d closing) :: MUTANTS %d :: ANCHORS %d :: SEALED %d"
        % (len(LD.rows), len(CLOSING_GATE_IDS), len(MUTANTS),
           len(SOURCES) + len(PATH_VALUES) + len(VERBATIM), len(SEAL.man)))
    payload, _closing = seal_and_write(S, write, paper_bytes)
    say("")
    say(verdict)
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


USAGE = """usage: spc_exact.py [--no-write] [--selftest] [--mutant NAME]
                    [--all-mutants] [--list-gates] [--list-mutants]
                    [--verify-paper] [--quiet]

EXIT CONVENTIONS (they invert the usual reading):
  plain run       0 = every gate passed and the artifacts were written
                  1 = a gate refused; nothing was written
  --selftest      0 = every anchor class was fatal and nothing was written
  --mutant NAME   0 = the mutant DIED ON ITS DECLARED TARGET GATE
  --all-mutants   0 = every mutant died on target
  unknown flag    2

--list-gates runs the pipeline WITHOUT WRITING and lists the gates that
actually closed, followed by the two that close after the ledger snapshot
and the one that exists only to refuse -- so the listing is the ledger and
not the set of mutant targets.
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
        globals()["QUIET"] = True
        try:
            run(write=False, paper_gates=True)
        except GateFail as e:
            sys.stderr.write("REFUSED :: %s\n" % e)
            return 1
        for gx in sorted(LD.ids):
            print(gx)
        for gx in sorted(CLOSING_GATE_IDS):
            if gx not in LD.ids:
                print("%s   (closes after the ledger snapshot)" % gx)
        for gx in sorted(REFUSAL_ONLY_GATES):
            print("%s   (refusal only; closes on no clean path)" % gx)
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
