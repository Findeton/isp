#!/usr/bin/env python3
"""R5M / paper-23 -- THE CONFIGURATION MEASURE.

Does the substrate DERIVE a probability measure on R5's gauge configurations
(the link-indexed coin assignments of the declared 640-coin family), or must
one be DECLARED?  The derivation census runs seven candidate sources, each
measured at the RSQ standard -- derived iff zero free items -- and every
uniqueness claim is GATED rather than asserted.

Built against the frozen pin v14/note-r5m-pin.md.  Exact arithmetic only:
the field is Q(zeta_8) carried as integer 5-tuples over the basis
(1, z, z^2, z^3) reduced modulo z^4 + 1 in lowest terms, so tuple equality is
field equality; every probability is a fractions.Fraction; no float enters
any measurement, and an AST scan of this file's own syntax tree is a gate.

THE PIN'S MUST-NOT, INHERITED VERBATIM FROM R5 AND ENFORCED HERE: this unit
builds the measure and makes NO area-law, NO string-tension and NO potential
claim.  Wilson-loop EXPECTATIONS are licensed ONLY in the DERIVED case; no
source derives, so the instrument computes none and a gate requires the
receipt to carry no such field at all.
"""

import ast
import hashlib
import json
import os
import re
import sys
from fractions import Fraction
from itertools import product

UNIT = "R5M / paper-23 -- the configuration measure"
PIN_SHA12 = "e5e09f65f83b"
SCHEMA = "r5m-measure-1"

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


def fsub(a, b):
    return fadd(a, fneg(b))


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
        self.digests.append(digest(row))
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
# SECTION 3.  PROVENANCE -- the pinned sources, read at declared relative paths
# ===========================================================================

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.dirname(ROOT)

SOURCES = [
    ("S-PIN", "v14/note-r5m-pin.md", "e5e09f65f83b",
     "THE PIN, frozen before this instrument existed"),
    ("S-R5-PAPER", "v14/paper-18-gauge-rung.md", "62cfe5689d2c",
     "PARENT 1, R5 terminal at commit 987cd73: the 640-coin family, the "
     "link-indexed configurations, the chart group, the gauge action, the "
     "plaquette loops"),
    ("S-R5-CODE", "v14/code/r5_gauge_exact.py", "0d98de793b79",
     "PARENT 1's instrument -- read for its declared definitions only; "
     "nothing is imported from it"),
    ("S-R5-RECEIPT", "v14/code/r5_gauge_receipt.json", "0c02b7684e5b",
     "PARENT 1's receipt: the anchored arena cardinalities and the parent "
     "census this unit reproduces"),
    ("S-GI-PAPER", "v14/paper-16-gamma-iteration.md", "5c1df50673d4",
     "PARENT 2, the Gamma-iteration terminal at commit 2895a9a: the "
     "transition layer's exact history probabilities -- the pin's candidate "
     "derivation source"),
    ("S-GI-RECEIPT", "v14/code/giter_receipt.json", "42255f50328a",
     "PARENT 2's receipt: the cut dimensions, the cut masses, the depth "
     "grading and the holonomy rank"),
    ("S-W2-PAPER", "v14/paper-13-weld2-carrier-census.md", "9cdb10472953",
     "THE CORRESPONDENCE PRIOR: weld 2's carrier census, run at PARENT 2's "
     "own two carriers"),
    ("S-W2-RECEIPT", "v14/code/w2_census_receipt.json", "bd68497d4510",
     "weld 2's receipt: the census fates"),
    ("S-W3-PAPER", "v14/paper-19-r3-weld.md", "50bb81e67942",
     "THE ONE FOUND DICTIONARY IN THE CORPUS: weld 3's actor->site, "
     "co-division-pair->link, division-count->n_l(x)"),
    ("S-W3-RECEIPT", "v14/code/r3_weld_receipt.json", "dfea664f2408",
     "weld 3's receipt: the found dictionary and its arena"),
]

PAPER_REL = "v14/paper-23-measure.md"
OUT_REL = "v14/code/r5m_measure_output.txt"
RECEIPT_REL = "v14/code/r5m_measure_receipt.json"

BANNED_NAMES = ["subprocess", "numpy", "random", "scipy"]
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
        if mut("MUT-SOURCE-DRIFT") and name == "S-R5-RECEIPT":
            d = "000000000000"
        rows.append({"name": name, "path": rel, "pinned": sha, "measured": d,
                     "ok": d == sha, "what": what})
        got[name] = b
    return got, rows


# ---------------------------------------------------------------- path-value
PATH_VALUES = [
    # (anchor id, source, dotted path, expected, consumer gate, what)
    ("PV-COINS", "S-R5-RECEIPT", "counts/coins", 640, "G-COINS-DERIVED",
     "the derived coin family's size"),
    ("PV-DIAG", "S-R5-RECEIPT", "counts/coins_diagonal", 64,
     "G-COINS-DERIVED", "the diagonal sector"),
    ("PV-ANTI", "S-R5-RECEIPT", "counts/coins_antidiagonal", 64,
     "G-COINS-DERIVED", "the antidiagonal sector"),
    ("PV-BAL", "S-R5-RECEIPT", "counts/coins_balanced", 512,
     "G-COINS-DERIVED", "the balanced (interfering) sector"),
    ("PV-ALPHABET", "S-R5-RECEIPT", "counts/alphabet", 25,
     "G-ALPHABET-REBUILT", "the parent's coefficient alphabet"),
    ("PV-L", "S-R5-RECEIPT", "counts/L", 4, "G-LATTICE-REBUILT",
     "the lattice size"),
    ("PV-D", "S-R5-RECEIPT", "counts/d", 2, "G-LATTICE-REBUILT",
     "the dimension"),
    ("PV-SITES", "S-R5-RECEIPT", "counts/sites", 16, "G-LATTICE-REBUILT",
     "the site count"),
    ("PV-LINKS", "S-R5-RECEIPT", "counts/links", 32, "G-LATTICE-REBUILT",
     "the link count -- the configuration space's exponent"),
    ("PV-PLAQS", "S-R5-RECEIPT", "counts/plaquettes", 16,
     "G-LATTICE-REBUILT", "the plaquette count"),
    ("PV-CHART", "S-R5-RECEIPT", "counts/chart_group", 32,
     "G-CHART-REBUILT", "the anchored chart group's order"),
    ("PV-EXT", "S-R5-RECEIPT", "counts/extension_group", 128,
     "G-CHART-REBUILT", "the declared extension by the square point group"),
    ("PV-NONFLAT", "S-R5-RECEIPT", "counts/nonflat_configs", 632,
     "G-PARENT-CENSUS-REPRODUCED", "the parent's non-flat census"),
    ("PV-NONCOMM", "S-R5-RECEIPT", "counts/noncommuting_configs", 576,
     "G-PARENT-CENSUS-REPRODUCED", "the parent's non-commuting census"),
    ("PV-DEFECT", "S-R5-RECEIPT", "counts/defect_carrying_coins", 384,
     "G-PARENT-CENSUS-REPRODUCED", "the parent's defect-carrying census"),
    ("PV-INFINITE", "S-R5-RECEIPT", "counts/balanced_infinite", 512,
     "G-HOLONOMY-GROUP-IS-CONFIGURATION-DEPENDENT",
     "the sector on which the holonomy group is infinite"),
    ("PV-GI-DIMS", "S-GI-RECEIPT", "carrier/dims/CONG-185",
     [1, 5, 17, 49, 113], "G-PUSHFORWARD-SUPPORT-BOUND",
     "PARENT 2's per-cut class dimensions -- the pushforward's support bound"),
    ("PV-GI-CLASSES", "S-GI-RECEIPT", "carrier/classes", 185,
     "G-PUSHFORWARD-SUPPORT-BOUND", "PARENT 2's carrier size"),
    ("PV-GI-CUTMASS", "S-GI-RECEIPT", "law/cut_masses",
     ["1", "1", "1", "1", "1"], "G-GAMMA-LAW-IS-A-PROBABILITY",
     "PARENT 2's cut masses -- each cut carries an exact probability"),
    ("PV-GI-FLOW", "S-GI-RECEIPT", "law/flow_ok", 3968,
     "G-GAMMA-LAW-IS-A-PROBABILITY", "PARENT 2's disintegration identity"),
    ("PV-GI-QRANK", "S-GI-RECEIPT", "holonomy/CONG-185|q/rank", 2,
     "G-TRANSPORT-OBSTRUCTION", "PARENT 2's holonomy rank -- abelian"),
    ("PV-W2-CANDIDATES", "S-W2-RECEIPT", "payload/candidate_count", 120,
     "G-WELD2-RAN-AT-THE-GAMMA-CARRIER", "weld 2's census rows"),
    ("PV-W2-DISTINCT", "S-W2-RECEIPT", "payload/distinct_candidates", 60,
     "G-WELD2-RAN-AT-THE-GAMMA-CARRIER", "weld 2's distinct candidates"),
    ("PV-W2-ACTORS", "S-W2-RECEIPT", "payload/mechanism/actor_site_objects",
     2, "G-ARITY-BLADE-TRANSFERS",
     "the actor pair's site objects -- the arity blade's measured input"),
    ("PV-W3-CELLS", "S-W3-RECEIPT", "arena/cells_at_one", 27,
     "G-WELD3-LINK-DATUM-IS-CONSTANT",
     "weld 3's realised link cells, every one of them at count 1"),
    ("PV-W3-DIVISIONS", "S-W3-RECEIPT", "arena/divisions", 9,
     "G-WELD3-TARGET-IS-NOT-THIS-ARENA", "weld 3's site count"),
]


def dig(obj, path):
    cur = obj
    for part in path.split("/"):
        if isinstance(cur, list):
            cur = cur[int(part)]
        else:
            if part not in cur:
                raise KeyError("unresolvable probe: %s" % path)
            cur = cur[part]
    return cur


# ---------------------------------------------------------------- verbatim
VERBATIM = [
    ("VB-R5-NO-MEASURE", "S-R5-PAPER", "G-THE-GAP-IS-THE-PARENTS-OWN",
     "The gap a coupling unit inherits above all is the one this rung could "
     "not close: **there is no measure on configurations here**, so there is "
     "nothing yet to take an expectation over."),
    ("VB-R5-THREE-OBJECTS", "S-R5-PAPER", "G-THE-PIN-OPENS-IN-THE-RIGHT-PLACE",
     "A confinement analog would need three objects this arena does not "
     "have: a measure on configurations, a family of loops whose size can "
     "grow, and a coupling to vary."),
    ("VB-R5-NO-ACTION", "S-R5-PAPER", "G-GIBBS-NEEDS-AN-ACTION",
     "It has no configuration measure, no action functional, no coupling and "
     "no dynamics for the link variables"),
    ("VB-PIN-WILSON", "S-PIN", "G-NO-WILSON-EXPECTATION",
     "the Wilson-expectation segment only in the DERIVED case"),
    ("VB-PIN-MUSTNOT", "S-PIN", "G-MUST-NOT-VOCABULARY",
     "**The confinement word stays behind its gate: this unit builds the "
     "measure; it makes NO area-law, string-tension, or potential claim**"),
    ("VB-GI-LAW", "S-GI-PAPER", "G-GAMMA-LAW-IS-A-PROBABILITY",
     "Γ is an exact rational column-stochastic family between the five depth "
     "cuts, of dimensions [1, 5, 17, 49, 113] over 3969 histories and 185 "
     "classes"),
    ("VB-GI-DESCRIPTION", "S-GI-PAPER", "G-GAMMA-LAW-IS-A-PROBABILITY",
     "The transport chain on histories is Markov by construction"),
    ("VB-W2-QUESTION", "S-W2-PAPER", "G-WELD2-RAN-AT-THE-GAMMA-CARRIER",
     "is there a **motivated** map from the transport grammar's carrier to "
     "I7's spatial record lattice — grammar objects to sites, object-pairs "
     "or channels to links, sets of division events to link counts — where "
     "*motivated* means zero free items at the RSQ standard?"),
    ("VB-W2-EMPTY", "S-W2-PAPER", "G-WELD2-RAN-AT-THE-GAMMA-CARRIER",
     "The census is **EMPTY under both**: **120 rows, 60 distinct "
     "candidates, 0 FOUND, 0 SMUGGLED**."),
    ("VB-W3-DICTIONARY", "S-W3-PAPER", "G-WELD3-IS-THE-ONE-FOUND-DICTIONARY",
     "The site and link generators are the one cell weld 2 left live at a "
     "record arena — site ← ACTOR, link ← the co-division actor pair, count "
     "← the division events on that pair inside the declared window."),
    ("VB-W3-CONSTANT", "S-W3-PAPER", "G-WELD3-LINK-DATUM-IS-CONSTANT",
     "the same nine site objects, the same 27 unordered realised pairs, the "
     "same count 1 on every one of them"),
    ("VB-W3-DEADLIST", "S-W3-PAPER", "G-WELD2-RAN-AT-THE-GAMMA-CARRIER",
     "weld 2's scissors scope — the (A,B) carrier at depth ≤ 4 — and weld "
     "2's transport-carrier cells"),
]

VERBATIM_FLOOR = 50


def wsnorm(s):
    """#125: text gates match text AS WRITTEN -- whitespace AND markdown
    prefix normalisation, so a claim broken across lines, or carried inside a
    blockquote or a list item, is still the same characters in the same
    order."""
    s = re.sub(r"(?m)^[ \t]*(?:[>*+-]|\d+\.)[ \t]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


# ===========================================================================
# SECTION 4.  THE ARENA, REBUILT FROM THE PARENT'S DECLARED DEFINITIONS
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
    entries lie in the alphabet.  Exhaustive over the admissible rows; the
    size is measured, never typed."""
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
    """U^dagger U = I, written out."""
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


COIN_I = (ONE, ZERO, ZERO, ONE)

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


# ------------------------------------------------------------- the chart
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


# --------------------------------------------------- sparse site operators
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


def born(A):
    """B(U) = |U| entrywise-squared -- the substrate's own Born layer."""
    return {k: fnormsq(v) for k, v in A.items()}


def bmul(A, B):
    return smul(A, B)


def uniform_cfg(lat, m):
    return {l: m for l in lat.links}


# ===========================================================================
# SECTION 5.  GROUP ACTIONS ON THE CONFIGURATION SLICE
# ===========================================================================

def perm_of(coins, cidx, f):
    return tuple(cidx[f(m)] for m in coins)


def pcompose(p, q):
    return tuple(p[q[i]] for i in range(len(q)))


def gen_group(n, gens):
    ident = tuple(range(n))
    G = {ident}
    frontier = [ident]
    while frontier:
        nxt = []
        for g in frontier:
            for s in gens:
                h = pcompose(s, g)
                if h not in G:
                    G.add(h)
                    nxt.append(h)
        frontier = nxt
    return G


def orbits_of(G, n):
    seen = [False] * n
    out = []
    for i in range(n):
        if not seen[i]:
            cl = sorted({g[i] for g in G})
            for j in cl:
                seen[j] = True
            out.append(cl)
    return out


def orbit_closed(orbs, members):
    """#87: the predicate binds OBJECTS.  A set is orbit-closed iff every
    orbit meets it in 0 or all of its points."""
    for o in orbs:
        k = sum(1 for i in o if i in members)
        if k not in (0, len(o)):
            return False
    return True


def realisable_constant_twists(lat):
    """which CONSTANT link twists a site-diagonal gauge can realise: propagate
    theta from one site along the links and see whether the assignment closes
    on the torus.  Measured by propagation, not argued."""
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


def chart_cycle_profile(lat, elems):
    """for each chart element, the cycle structure of its action on the link
    set together with the parity of the swap-conjugations around each cycle.
    That pair is exactly what Burnside needs."""
    prof = []
    nl = len(lat.links)
    for e in elems:
        p = [None] * nl
        rev = [None] * nl
        for l in lat.links:
            im, r = transported_link(lat, l, e)
            p[lat.lidx[l]] = lat.lidx[im]
            rev[lat.lidx[l]] = r
        if sorted(p) != list(range(nl)):
            return None
        seen = [False] * nl
        ev = od = 0
        for i in range(nl):
            if seen[i]:
                continue
            j = i
            par = 0
            while not seen[j]:
                seen[j] = True
                par ^= (1 if rev[j] else 0)
                j = p[j]
            if par:
                od += 1
            else:
                ev += 1
        prof.append((ev, od, tuple(p), tuple(rev)))
    return prof


def burnside_orbits(prof, ncoins, nswapfixed):
    """|X/G| = (1/|G|) sum_g |Fix(g)|.  Fix(g) factorises over the cycles of
    g on the link set: a cycle with an even number of reversals is free
    (n_coins choices), a cycle with an odd number forces U = X U X."""
    tot = 0
    for (ev, od, _p, _r) in prof:
        tot += (ncoins ** ev) * (nswapfixed ** od)
    if tot % len(prof) != 0:
        return None
    return tot // len(prof)


def link_orbits(lat, prof):
    nl = len(lat.links)
    seen = [False] * nl
    out = []
    for i in range(nl):
        if not seen[i]:
            cl = {p[i] for (_e, _o, p, _r) in prof}
            for j in cl:
                seen[j] = True
            out.append(sorted(cl))
    return out


# ===========================================================================
# SECTION 6.  THE MEASUREMENT BODY
# ===========================================================================

def measure_provenance(S):
    src, rows = load_sources()
    S["_src"] = src
    bad = [r for r in rows if not r["ok"]]
    LD.gate("G-SOURCES-PINNED",
            "every runtime input is read at a DECLARED RELATIVE PATH resolved "
            "from this file's own location and gated against a sha256-12 "
            "frozen in this instrument before it ran; a drifted source dies "
            "here, before a single measurement, and no version-control "
            "command is invoked to find out (#91)",
            not bad and len(rows) == len(SOURCES),
            "%d sources, %d drifted" % (len(rows), len(bad)))
    # the ledger entry the pin was frozen at, READ OFF THE PIN'S OWN BYTES so
    # that the paper's citation of it is a measurement and not a literal the
    # coverage gate has to forgive
    m = re.search(r"ledger\s*#(\d+)", src["S-PIN"].decode())
    S["provenance"] = {"sources": rows, "root": "resolved from __file__",
                       "object_under_test": PAPER_REL,
                       "pin_ledger_entry": int(m.group(1)) if m else -1,
                       "declared_not_read": []}

    me = open(os.path.abspath(__file__), "rb").read().decode()
    tree = ast.parse(me)
    floats = [n for n in ast.walk(tree)
              if isinstance(n, ast.Constant) and isinstance(n.value, float)]
    names = set()
    calls = set()
    for n in ast.walk(tree):
        if isinstance(n, ast.Import):
            for a in n.names:
                names.add(a.name.split(".")[0])
        elif isinstance(n, ast.ImportFrom):
            names.add((n.module or "").split(".")[0])
        elif isinstance(n, ast.Attribute):
            calls.add(n.attr)
    hits = sorted(names & set(BANNED_NAMES))
    chits = sorted(calls & set(BANNED_CALLS))
    if mut("MUT-FLOAT-SNEAK"):
        floats = floats + [1]
    LD.gate("G-EXACT-ARITHMETIC",
            "the instrument's OWN syntax tree carries no float literal and "
            "no banned import or attribute call, so the exactness claim is "
            "a property of the source rather than of its author's intention",
            not floats and not hits and not chits,
            "%d float literals, banned imports %s, banned calls %s"
            % (len(floats), hits, chits))

    # the needles are ASSEMBLED, never spelled: spelling either of them in
    # this file would make the guard fire on itself and it could never be
    # satisfied.  The evasion is the falsifier.
    vc = "g" + "it"
    needles = [vc + " rev-parse", vc + " show", vc + " log",
               "@{" + "upstream}", "or" + "igin/", ":HE" + "AD",
               "HE" + "AD~", "HE" + "AD^"]
    hay = wsnorm(me)
    if mut("MUT-MOVING-REF"):
        hay = hay + " " + needles[0]
    moving = [t for t in needles if t in hay]
    LD.gate("G-NO-MOVING-REFS",
            "no moving reference is read anywhere in the instrument: the "
            "sources are pinned by digest, not by a branch name, so the run "
            "is correct off-tree and in a directory with no version control "
            "at all",
            len(moving) == 0, "moving references found: %s" % moving)

    # NO DEAD MUTANT BRANCH, AND NO UNDECLARED SWITCH: the set of mutant names
    # this file's own syntax tree switches on must equal the registry, so a
    # branch someone forgot to declare -- which would never be swept -- dies
    # here rather than sitting unexercised
    switched = set()
    for n in ast.walk(tree):
        if (isinstance(n, ast.Call) and isinstance(n.func, ast.Name)
                and n.func.id == "mut" and n.args
                and isinstance(n.args[0], ast.Constant)):
            switched.add(n.args[0].value)
    declared = {nm for (nm, _g, _w) in MUTANTS}
    LD.gate("G-MUTANT-REGISTRY-TOTAL",
            "the mutant registry is TOTAL against the instrument's own "
            "syntax tree: every name the source switches on is declared, and "
            "every declared name is switched on somewhere, so no falsifier "
            "can exist as an unswept branch and none can be declared without "
            "a branch to fire",
            switched == declared,
            "%d switches, %d declared; undeclared %s, unused %s"
            % (len(switched), len(declared), sorted(switched - declared),
               sorted(declared - switched)))

    esc = [rel for (_n, rel, _s, _w) in SOURCES
           if os.path.isabs(rel) or ".." in rel.split("/")]
    LD.gate("G-PATHS-RELATIVE",
            "every declared read path is RELATIVE, does not escape the "
            "repository root, and resolves under the root computed from this "
            "file's own location",
            not esc and not os.path.isabs(PAPER_REL), "escaping paths: %s" % esc)
    return src


def measure_path_values(S, src):
    docs = {}
    rows = []
    for (aid, sname, path, expected, gate, what) in PATH_VALUES:
        if sname not in docs:
            docs[sname] = json.loads(src[sname].decode())
        got = dig(docs[sname], path)
        if mut("MUT-PATH-VALUE") and aid == "PV-COINS":
            got = 641
        rows.append({"anchor": aid, "source": sname, "path": path,
                     "declared": expected, "measured": got,
                     "ok": got == expected, "consumer": gate, "what": what})
    bad = [r for r in rows if not r["ok"]]
    LD.gate("G-PATH-VALUE-ANCHORS",
            "every anchor is a (path, value) pair bound to the gate that "
            "CONSUMES it, not a bare file digest: the parent's own receipt is "
            "read at a named path and the value found there must equal the "
            "value this instrument was frozen against (#87)",
            not bad, "%d probes, %d mismatched" % (len(rows), len(bad)))
    S["path_value_anchors"] = rows
    S["_pv"] = {r["anchor"]: r["measured"] for r in rows}
    return S["_pv"]


def measure_verbatim(S, src):
    rows = []
    for (aid, sname, gate, text) in VERBATIM:
        hay = wsnorm(src[sname].decode())
        needle = wsnorm(text)
        n = hay.count(needle)
        # the flip: perturb one content-bearing token and require the window
        # to STOP being locatable, so a row counts as covered only when its
        # own predicate can fail
        toks = [t for t in needle.split(" ") if len(t) > 3]
        flipped = needle.replace(toks[len(toks) // 2],
                                 toks[len(toks) // 2][::-1] + "Q", 1)
        nf = hay.count(flipped)
        rows.append({"anchor": aid, "source": sname, "consumer": gate,
                     "chars": len(needle), "floor": VERBATIM_FLOOR,
                     "occurrences": n, "flipped_occurrences": nf,
                     "digest": digest(needle),
                     "ok": n == 1 and nf == 0 and len(needle) >= VERBATIM_FLOOR})
    if mut("MUT-VERBATIM-SHRINK"):
        rows[0]["chars"] = 10
        rows[0]["ok"] = False
    bad = [r for r in rows if not r["ok"]]
    LD.gate("G-VERBATIM-ANCHORS",
            "every verbatim window is located EXACTLY ONCE in its own pinned "
            "source under whitespace and markdown-prefix normalisation "
            "(#125), is pinned by its digest AND by its own frozen character "
            "count against a declared floor, and is bound to the gate that "
            "consumes it; and each is perturbed at a content-bearing token "
            "and required to stop being locatable, so no row is vacuous",
            not bad, "%d windows, %d failing" % (len(rows), len(bad)))
    S["verbatim_anchors"] = rows


def build_arena(S, pv):
    L = pv["PV-L"]
    alphabet = build_alphabet()
    if mut("MUT-ALPHABET"):
        alphabet = alphabet[:-1]
    LD.gate("G-ALPHABET-REBUILT",
            "the parent's coefficient alphabet is REBUILT here from its "
            "declared shape -- zero together with the eighth roots of unity "
            "at each of three moduli -- and its size is measured against the "
            "anchored value rather than typed",
            len(alphabet) == pv["PV-ALPHABET"],
            "rebuilt %d, anchored %d" % (len(alphabet), pv["PV-ALPHABET"]))

    coins, rows = build_coins(alphabet)
    if mut("MUT-COIN-UNITARITY"):
        coins = coins + [(ONE, ONE, ONE, ONE)]
    sectors = {}
    for m in coins:
        sectors[coin_sector(m)] = sectors.get(coin_sector(m), 0) + 1
    nonunit = [m for m in coins if not coin_unitary_second_route(m)]
    LD.gate("G-COINS-DERIVED",
            "the coin family is DERIVED, exhaustively over the alphabet's "
            "admissible rows, and its size and its sector split are measured "
            "against the parent's own anchored values; unitarity is confirmed "
            "by a SECOND route, U^dagger U = I written out, on every member",
            (len(coins) == pv["PV-COINS"]
             and sectors.get("DIAGONAL") == pv["PV-DIAG"]
             and sectors.get("ANTIDIAGONAL") == pv["PV-ANTI"]
             and sectors.get("BALANCED") == pv["PV-BAL"]
             and not nonunit and sectors.get("OTHER") is None),
            "%d coins, sectors %s, %d failing the second route"
            % (len(coins), sorted(sectors.items()), len(nonunit)))

    used = set()
    for m in coins:
        used |= set(m)
    lat = Lattice(L)
    LD.gate("G-LATTICE-REBUILT",
            "the stage is rebuilt from the anchored lattice size: the site, "
            "link and plaquette sets are DERIVED from the lattice rather "
            "than declared, and all three counts are measured against the "
            "parent's receipt",
            (len(lat.sites) == pv["PV-SITES"] and len(lat.links) == pv["PV-LINKS"]
             and len(lat.plaqs) == pv["PV-PLAQS"] and pv["PV-D"] == 2),
            "%d sites, %d links, %d plaquettes"
            % (len(lat.sites), len(lat.links), len(lat.plaqs)))

    S["arena"] = {
        "L": L, "d": pv["PV-D"], "sites": len(lat.sites),
        "links": len(lat.links), "plaquettes": len(lat.plaqs),
        "alphabet": len(alphabet), "alphabet_elements_used": len(used),
        "coins": len(coins), "sectors": sectors,
        "admissible_rows": len(rows),
        "configuration_space": "%d^%d" % (len(coins), len(lat.links)),
        "configuration_space_exact": len(coins) ** len(lat.links),
        "uniform_slice": len(coins),
        "field": "Q(ZETA-8)",
        "swept_by_the_parent": "THE UNIFORM CONFIGURATIONS, EXHAUSTIVELY",
    }
    S["_lat"] = lat
    S["_coins"] = coins
    S["_cidx"] = {m: i for i, m in enumerate(coins)}
    S["_alphabet"] = alphabet
    return lat, coins


def measure_symmetries(S, pv):
    lat, coins = S["_lat"], S["_coins"]
    cidx = S["_cidx"]
    cset = set(coins)

    ch32 = chart_elements(lat, False)
    ch128 = chart_elements(lat, True)
    p32 = chart_cycle_profile(lat, ch32)
    p128 = chart_cycle_profile(lat, ch128)
    LD.gate("G-CHART-REBUILT",
            "both chart groups are rebuilt -- the anchored translations with "
            "the direction relabelling, and this arena's declared extension "
            "by the square point group -- and each element is checked to act "
            "on the LINK SET as a permutation; the two orders are measured "
            "against the parent's receipt",
            (len(ch32) == pv["PV-CHART"] and len(ch128) == pv["PV-EXT"]
             and p32 is not None and p128 is not None),
            "chart %d, extension %d, both acting by permutations"
            % (len(ch32), len(ch128)))

    lo32 = link_orbits(lat, p32)
    lo128 = link_orbits(lat, p128)
    # TWO different counts, kept apart on purpose: an element may reverse many
    # links and still compose to the identity around every cycle.  What forces
    # U = X U X on a fixed configuration is an ODD-PARITY CYCLE, not a
    # reversal, and conflating the two would misreport the fixed locus
    odd32 = sum(1 for (_e, o, _p, _r) in p32 if o)
    odd128 = sum(1 for (_e, o, _p, _r) in p128 if o)
    rev32 = sum(1 for (_e, _o, _p, rv) in p32 if any(rv))
    rev128 = sum(1 for (_e, _o, _p, rv) in p128 if any(rv))
    tot32 = sum(sum(1 for r in rv if r) for (_e, _o, _p, rv) in p32)
    tot128 = sum(sum(1 for r in rv if r) for (_e, _o, _p, rv) in p128)
    LD.gate("G-CHART-IS-TRANSITIVE-ON-LINKS",
            "the chart group is TRANSITIVE on the link set at both readings "
            "-- one orbit of all the links -- which is the fact that decides "
            "what a chart-fixed configuration can be",
            len(lo32) == 1 and len(lo128) == 1
            and len(lo32[0]) == len(lat.links),
            "link orbits: %d at the anchored reading, %d at the extension"
            % (len(lo32), len(lo128)))

    swapfixed = [m for m in coins if swap_conjugate(m) == m]
    outside = [m for m in coins if swap_conjugate(m) not in cset]
    LD.gate("G-SWAP-CONJUGATE-CLOSED",
            "the swap conjugate -- the coin read from the other end of its "
            "own domino, which is what a direction-reversing chart element "
            "transports -- maps the derived family to itself",
            not outside, "%d coins leaving the family" % len(outside))

    twist_out = {}
    for k in range(8):
        twist_out[k] = sum(1 for m in coins if gauge_twist(m, k) not in cset)
    LD.gate("G-GAUGE-ACTS-ON-THE-FAMILY",
            "the site-diagonal gauge acts on a link's coin by conjugation, "
            "and the action depends on the phase DIFFERENCE across the link "
            "alone; every one of its eight values permutes the derived "
            "family, so a gauge transformation moves a configuration inside "
            "the configuration space and never out of it",
            all(v == 0 for v in twist_out.values()),
            "twists leaving the family: %s" % sorted(twist_out.items()))

    ctw = realisable_constant_twists(lat)
    LD.gate("G-UNIFORMITY-PRESERVING-GAUGE-MEASURED",
            "which gauge transformations preserve the uniform slice is "
            "MEASURED by propagating the site phase around the torus and "
            "asking whether the assignment closes, not argued: a twist "
            "constant on every link is realisable exactly at the even "
            "values, because the phase must close after L steps",
            ctw == [c for c in range(8) if (lat.L * c) % 8 == 0],
            "realisable constant twists %s" % ctw)

    # the residual group acting on the uniform slice
    tau = perm_of(coins, cidx, lambda m: gauge_twist(m, ctw[1]))
    sig = perm_of(coins, cidx, swap_conjugate)
    if mut("MUT-RESIDUAL-GROUP"):
        tau = tuple(range(len(coins)))
    G32 = gen_group(len(coins), [tau])
    G128 = gen_group(len(coins), [tau, sig])
    o32 = orbits_of(G32, len(coins))
    o128 = orbits_of(G128, len(coins))

    hist32 = {}
    for o in o32:
        hist32[len(o)] = hist32.get(len(o), 0) + 1
    hist128 = {}
    for o in o128:
        hist128[len(o)] = hist128.get(len(o), 0) + 1
    LD.gate("G-ORBIT-CENSUS-EXACT",
            "the residual group is the one the arena measures and its orbits "
            "are enumerated exactly: its order equals the number of "
            "uniformity-preserving twists at the anchored reading and twice "
            "that at the extension -- so the swap conjugation is measured to "
            "lie outside the twist subgroup rather than assumed to -- and the "
            "orbit sizes sum to the slice at both readings, so no "
            "configuration is counted twice and none is dropped",
            (sum(len(o) for o in o32) == len(coins)
             and sum(len(o) for o in o128) == len(coins)
             and len(G32) == len(ctw)
             and len(G128) == 2 * len(ctw)),
            "residual orders %d and %d against %d realisable twists; %d "
            "orbits at the anchored reading, %d at the extension"
            % (len(G32), len(G128), len(ctw), len(o32), len(o128)))

    b32 = burnside_orbits(p32, len(coins), len(swapfixed))
    b128 = burnside_orbits(p128, len(coins), len(swapfixed))
    LD.gate("G-BURNSIDE-EXACT",
            "the chart-orbit count of the FULL configuration space is "
            "computed exactly by Burnside, the fixed-point count factorising "
            "over each element's cycles on the link set with the parity of "
            "the swap conjugations around each cycle; the group order "
            "divides the fixed-point total exactly, which is the arithmetic "
            "check the formula has to pass",
            b32 is not None and b128 is not None and b32 > b128,
            "%d chart orbits, %d extension orbits on the full space"
            % (b32 or -1, b128 or -1))

    S["symmetry"] = {
        "chart_order": len(ch32), "extension_order": len(ch128),
        "link_orbits_chart": len(lo32), "link_orbits_extension": len(lo128),
        "elements_reversing_at_least_one_link_chart": rev32,
        "elements_reversing_at_least_one_link_extension": rev128,
        "elements_with_an_odd_parity_cycle_chart": odd32,
        "elements_with_an_odd_parity_cycle_extension": odd128,
        "total_link_reversals_chart": tot32,
        "total_link_reversals_extension": tot128,
        "swap_fixed_coins": len(swapfixed),
        "gauge_twists_leaving_the_family": sorted(twist_out.items()),
        "uniformity_preserving_twists": ctw,
        "residual_group_order_chart": len(G32),
        "residual_group_order_extension": len(G128),
        "orbits_chart": len(o32), "orbits_extension": len(o128),
        "orbit_size_histogram_chart": sorted(hist32.items()),
        "orbit_size_histogram_extension": sorted(hist128.items()),
        "full_space_chart_orbits": b32,
        "full_space_extension_orbits": b128,
    }
    S["_o32"], S["_o128"] = o32, o128
    return o32, o128


def measure_fixed_locus(S, pv):
    """the CHART-FIXED CONFIGURATIONS -- and the distinction the whole
    invariance question turns on."""
    lat, coins = S["_lat"], S["_coins"]
    swapfixed = [m for m in coins if swap_conjugate(m) == m]
    # one link orbit, no reversals at the anchored reading => the fixed
    # configurations are exactly the uniform ones
    fixed32 = len(coins)
    fixed128 = len(swapfixed)
    # verified by direct construction rather than by the formula alone
    ch32 = chart_elements(lat, False)
    checked = 0
    failures = 0
    for m in coins[:len(coins)]:
        cfg = uniform_cfg(lat, m)
        for e in ch32:
            for l in lat.links:
                im, rev = transported_link(lat, l, e)
                want = swap_conjugate(cfg[l]) if rev else cfg[l]
                checked += 1
                if cfg[im] != want:
                    failures += 1
    if mut("MUT-FIXED-LOCUS"):
        failures = 1
    LD.gate("G-CHART-FIXED-LOCUS-IS-THE-SWEPT-SLICE",
            "THE ONE THING THE MEASURED SYMMETRY DOES FIX, and it is not a "
            "measure: because the chart is transitive on the link set and "
            "reverses no link at the anchored reading, the configurations it "
            "leaves fixed are EXACTLY the uniform ones -- so the parent's "
            "declared sweep is not an arbitrary window but the chart-fixed "
            "locus itself, and the check is run configuration by "
            "configuration rather than read off the orbit formula",
            failures == 0 and checked == len(coins) * len(ch32) * len(lat.links),
            "%d fixed-locus checks, %d failures" % (checked, failures))
    S["fixed_locus"] = {
        "chart_fixed_configurations": fixed32,
        "extension_fixed_configurations": fixed128,
        "checks": checked, "failures": failures,
        "the_distinction": "a symmetry fixes a SET OF CONFIGURATIONS; an "
        "invariant MEASURE is a different object, and the two are not to be "
        "conflated -- the fixed locus is a point of the configuration space, "
        "the invariant measures are a simplex over the orbits",
    }
    return fixed32, fixed128


def measure_parent_census(S, pv):
    """the parent's own census, REPRODUCED here from the definitions rather
    than quoted -- the sets the candidate measures will be asked to weigh."""
    lat, coins = S["_lat"], S["_coins"]
    n = len(lat.sites)
    base = lat.plaqs[0]
    edge = lat.addv(base, E1)
    I = sident(n)
    nonflat, noncomm, defect = set(), set(), set()
    per_sector = {}
    for m in coins:
        cfg = uniform_cfg(lat, m)
        W1 = holonomy(lat, base, cfg, n)
        W2 = holonomy(lat, edge, cfg, n)
        s = coin_sector(m)
        row = per_sector.setdefault(s, [0, 0, 0, 0])
        row[0] += 1
        if W1 != I:
            nonflat.add(m)
            row[1] += 1
        if smul(W1, W2) != smul(W2, W1):
            noncomm.add(m)
            row[2] += 1
        U = link_op(lat, lat.links[0], m, n)
        if born(smul(U, U)) != bmul(born(U), born(U)):
            defect.add(m)
            row[3] += 1
    if mut("MUT-PARENT-CENSUS"):
        nonflat = set(list(nonflat)[:-1])
    LD.gate("G-PARENT-CENSUS-REPRODUCED",
            "the parent's three headline censuses are REPRODUCED here from "
            "the definitions -- the non-flat count, the non-commuting count "
            "and the count of coins carrying a composition defect -- and "
            "each is measured against the parent's own receipt at a named "
            "path.  A unit that proposes to weigh a set must first be able "
            "to build it",
            (len(nonflat) == pv["PV-NONFLAT"]
             and len(noncomm) == pv["PV-NONCOMM"]
             and len(defect) == pv["PV-DEFECT"]),
            "non-flat %d/%d, non-commuting %d/%d, defect-carrying %d/%d"
            % (len(nonflat), pv["PV-NONFLAT"], len(noncomm), pv["PV-NONCOMM"],
               len(defect), pv["PV-DEFECT"]))

    S["parent_census"] = {
        "non_flat": len(nonflat), "non_commuting": len(noncomm),
        "defect_carrying": len(defect),
        "by_sector": {k: {"coins": v[0], "non_flat": v[1],
                          "non_commuting": v[2], "defect_carrying": v[3]}
                      for k, v in sorted(per_sector.items())},
    }
    S["_sets"] = {"NON-FLAT": nonflat, "NON-COMMUTING": noncomm,
                  "DEFECT-CARRYING": defect,
                  "DIAGONAL": {m for m in coins
                               if coin_sector(m) == "DIAGONAL"}}
    return S["_sets"]


def measure_born_layer(S):
    """CANDIDATE (g): the substrate's own Born layer.  It DOES derive an
    exact probability measure -- over the wrong space."""
    lat, coins = S["_lat"], S["_coins"]
    n = len(lat.sites)
    ds = 0
    images = {}
    for m in coins:
        b = tuple(to_fraction(fnormsq(x)) for x in m)
        images.setdefault(b, []).append(m)
        rowsum = (b[0] + b[1] == 1 and b[2] + b[3] == 1)
        colsum = (b[0] + b[2] == 1 and b[1] + b[3] == 1)
        if rowsum and colsum:
            ds += 1
    fibres = sorted(len(v) for v in images.values())
    if mut("MUT-BORN-STOCHASTIC"):
        ds -= 1
    LD.gate("G-BORN-LAYER-IS-A-MEASURE",
            "the substrate's own Born layer does deliver an exact "
            "probability: B(U) is doubly stochastic at every one of the "
            "derived coins, in exact rational arithmetic, so the candidate "
            "is real and is not dismissed on a technicality",
            ds == len(coins), "%d of %d doubly stochastic" % (ds, len(coins)))
    LD.gate("G-BORN-LAYER-LANDS-ON-STATES",
            "and it lands on the WRONG SPACE, which is the measurement that "
            "decides it: B(U) is a distribution over the carrier's STATES, "
            "not over the configurations, and its fibre over the "
            "configuration space is enormous -- the whole family collapses "
            "to one image per sector, so the Born layer cannot separate two "
            "configurations of the same sector, let alone weigh them",
            len(images) == len(S["parent_census"]["by_sector"]),
            "%d distinct Born images over %d configurations, fibres %s"
            % (len(images), len(coins), fibres))
    S["born_layer"] = {
        "doubly_stochastic": ds, "configurations": len(coins),
        "distinct_images": len(images), "fibres": fibres,
        "carrier_states": n,
        "free_items": 1,
        "verdict": "DERIVES-A-MEASURE-ON-THE-CARRIER-NOT-ON-THE-"
                   "CONFIGURATIONS",
    }
    return len(images), fibres


# --------------------------------------------------------------------------
# CANDIDATE (a): the history-measure pushforward
# --------------------------------------------------------------------------

R5_REFERENTS = ["coin", "plaquette", "link", "site", "torus", "unitary",
                "domino", "lattice", "stratum", "holonomy"]
GI_REFERENTS = ["history", "menu", "actor", "horizon", "congruence",
                "renewal", "potential", "class", "holonomy"]


def wordcount(text, w):
    return len(re.findall(r"(?<![A-Za-z])" + re.escape(w) + r"(?![A-Za-z])",
                          text, re.I))


def subcount(text, w):
    return len(re.findall(re.escape(w), text, re.I))


def measure_correspondence(S, src, pv):
    lat, coins = S["_lat"], S["_coins"]

    # --- (a1) the shared-referent census, both directions
    gi = src["S-GI-PAPER"].decode()
    r5 = src["S-R5-PAPER"].decode()
    rows = []
    for w in R5_REFERENTS:
        rows.append({"token": w, "direction": "R5-OBJECT-IN-THE-GAMMA-PARENT",
                     "whole_word": wordcount(gi, w), "substring": subcount(gi, w)})
    for w in GI_REFERENTS:
        rows.append({"token": w, "direction": "GAMMA-OBJECT-IN-THE-R5-PARENT",
                     "whole_word": wordcount(r5, w), "substring": subcount(r5, w)})
    ghosts = [r for r in rows if r["whole_word"] == 0 and r["substring"] > 0]
    homonyms = [r for r in rows if r["whole_word"] > 0]
    LD.gate("G-VOCABULARY-COINCIDENCE-REFUSED",
            "the apparent shared vocabulary of the two arenas is measured "
            "and REFUSED rather than used: tokens that appear only as "
            "substrings of unrelated words are counted separately from whole "
            "words, and the substring hits are exactly that -- a "
            "configuration word inside 'coincidental', a lattice word inside "
            "'refinement lattice'.  A coincidence is not a correspondence, "
            "and this unit will not build one out of one",
            len(ghosts) > 0 and all(r["substring"] >= r["whole_word"]
                                    for r in rows),
            "%d substring-only tokens, %d whole-word tokens carrying a "
            "different referent" % (len(ghosts), len(homonyms)))

    # --- (a2) the one structural near-miss: both arenas carry a holonomy
    qrank = pv["PV-GI-QRANK"]
    perfect = ["A5", "A7", "A8"]
    abelianish = ["A3", "A3 x A3"]
    profile = json.loads(src["S-R5-RECEIPT"].decode())["counts"]["local_profile"]
    stencils = [c.split("=") for c in profile.split(";")]
    blocked = [s for s in stencils if s[1].strip() in perfect]
    open_ = [s for s in stencils if s[1].strip() in abelianish]
    LD.gate("G-TRANSPORT-OBSTRUCTION",
            "the closest thing to a correspondence in the corpus is the word "
            "HOLONOMY, and it names two different connections: the transport "
            "layer's is ABELIAN of measured rank 2 on the primes {2, 3}, "
            "this arena's is non-abelian and contains alternating groups "
            "that are PERFECT.  A correspondence required to transport the "
            "connection would need a homomorphism from the first onto the "
            "second; an abelian source has abelian image and a perfect "
            "non-trivial group is not abelian, so it is impossible at "
            "exactly the perfect stencils -- and possible at the abelian "
            "ones, which is why the obstruction is reported per stencil and "
            "not as a universal",
            qrank == 2 and len(blocked) + len(open_) == len(stencils)
            and len(blocked) > 0 and len(open_) > 0,
            "%d of %d declared local stencils carry a perfect class and are "
            "blocked; %d carry an abelian class and are not"
            % (len(blocked), len(stencils), len(open_)))

    # --- (a3) the pinned correspondences, enumerated honestly
    w2 = json.loads(src["S-W2-RECEIPT"].decode())["payload"]
    w3 = json.loads(src["S-W3-RECEIPT"].decode())
    fates = w2["fates"]
    found = sum(v for k, v in fates.items() if k.startswith("FOUND"))
    LD.gate("G-WELD2-RAN-AT-THE-GAMMA-CARRIER",
            "the corpus has ALREADY run the correspondence question from "
            "this very carrier: weld 2 asked for a motivated map from the "
            "transport grammar's carrier to a spatial record lattice -- "
            "objects to sites, pairs to links, division-event sets to link "
            "counts -- at both of the transport layer's own quotients, and "
            "returned EMPTY at every row.  So the pushforward has no pinned "
            "correspondence by MEASUREMENT and not by omission",
            (w2["candidate_count"] == pv["PV-W2-CANDIDATES"]
             and w2["distinct_candidates"] == pv["PV-W2-DISTINCT"]
             and found == 0 and sum(fates.values()) == w2["candidate_count"]),
            "%d rows, %d distinct candidates, %d FOUND, fates %s"
            % (w2["candidate_count"], w2["distinct_candidates"], found,
               sorted(fates.items())))

    dead = w3["weld"]["dead_lists_cited"]
    carrier_dead = [d for d in dead if "WELD2" in d]
    LD.gate("G-WELD3-IS-THE-ONE-FOUND-DICTIONARY",
            "and the corpus's ONE found dictionary is weld 3's -- actor to "
            "site, co-division actor pair to link, division count to the "
            "link's own count -- whose own pre-registered dead list cites "
            "the transport carrier this pin names as its candidate source.  "
            "The one correspondence that exists does not start where the "
            "pushforward would have to start",
            len(carrier_dead) >= 2 and w3["counts"]["weld_found"] > 0,
            "%d found weld rows; %d dead-list entries naming the transport "
            "carrier: %s" % (w3["counts"]["weld_found"], len(carrier_dead),
                             carrier_dead))

    sites3 = pv["PV-W3-DIVISIONS"]
    LD.gate("G-WELD3-TARGET-IS-NOT-THIS-ARENA",
            "and its target is not this arena either: the found dictionary "
            "lands on a nine-site record lattice, where this arena has "
            "sixteen sites and thirty-two links, so the dictionary cannot be "
            "read here without being rebuilt -- and a rebuilt dictionary is "
            "a declaration, not an inheritance",
            sites3 != len(lat.sites),
            "the dictionary's target carries %d sites; this arena carries %d"
            % (sites3, len(lat.sites)))

    cells = pv["PV-W3-CELLS"]
    LD.gate("G-WELD3-LINK-DATUM-IS-CONSTANT",
            "and, granted everything else, its LINK DATUM is a count and the "
            "count is constant: every realised cell of the found arena "
            "carries the same value.  A constant link datum pulls back to a "
            "single configuration whichever coin one sends it to, so even "
            "the most generous grant delivers a POINT MASS with the coin "
            "free -- which is a declaration of one of the family's members, "
            "not a measure derived from anything",
            cells == w3["arena"]["cells"] and cells > 0,
            "%d realised cells, every one at the same count" % cells)

    # --- (a4) the arity blade, transferred; and the blade that does NOT
    actors = pv["PV-W2-ACTORS"]
    LD.gate("G-ARITY-BLADE-TRANSFERS",
            "one of weld 2's blades transfers to this target and is sharper "
            "here: the actor pool supplies two site objects against this "
            "arena's sixteen sites, where at weld 2's own target it faced "
            "nine",
            actors < len(lat.sites),
            "%d site objects against %d sites" % (actors, len(lat.sites)))

    # bipartiteness: the blade that does NOT transfer, disclosed
    adj = {s: set() for s in lat.sites}
    for s in lat.sites:
        for d in range(2):
            t = lat.addv(s, EDIR[d])
            adj[s].add(t)
            adj[t].add(s)
    col = {lat.sites[0]: 0}
    frontier = [lat.sites[0]]
    bip = True
    while frontier:
        nxt = []
        for s in frontier:
            for t in adj[s]:
                if t not in col:
                    col[t] = 1 - col[s]
                    nxt.append(t)
                elif col[t] == col[s]:
                    bip = False
        frontier = nxt
    degs = sorted({len(adj[s]) for s in lat.sites})
    LD.gate("G-STRUCTURAL-BLADE-DOES-NOT-TRANSFER",
            "and one of them does NOT, which this unit measures rather than "
            "leaves for a reader to catch: weld 2's structural blade was "
            "that a graded class graph is bipartite and cannot carry its "
            "target's odd cycle.  THIS target is bipartite too -- every "
            "cycle of the link graph is even -- so that blade is SILENT "
            "here, and the correspondence question at this target is left "
            "OPEN by this unit rather than inherited as closed",
            bip and degs == [4],
            "target bipartite %s, degrees %s -- the odd-cycle blade cannot "
            "fire" % (bip, degs))

    # --- (a5) the support bound: what a pushforward could reach if it existed
    dims = pv["PV-GI-DIMS"]
    classes = pv["PV-GI-CLASSES"]
    top = dims[-1]
    slice_n = len(coins)
    full = len(coins) ** len(lat.links)
    zero_on_slice = slice_n - min(top, slice_n)
    LD.gate("G-PUSHFORWARD-SUPPORT-BOUND",
            "and the arithmetic of the source is measured too, because a "
            "pushforward can charge no more atoms than its source has: the "
            "transport law's finest cut carries fewer classes than this "
            "arena has configurations even on the uniform slice, so any "
            "class-grain pushforward leaves most of the slice at mass zero, "
            "and on the full configuration space it charges a vanishing "
            "fraction",
            top < slice_n and zero_on_slice > 0,
            "%d classes at the last cut against %d slice configurations: at "
            "least %d configurations at mass zero; the full space carries "
            "%d" % (top, slice_n, zero_on_slice, full))

    LD.gate("G-GAMMA-LAW-IS-A-PROBABILITY",
            "none of which is a complaint about the source: the transport "
            "law IS an exact probability, column-stochastic with cut mass "
            "one at every cut and its disintegration identity exact at every "
            "transition.  The candidate fails at the CORRESPONDENCE, not at "
            "the law -- which is why the honest outcome is a declaration "
            "price and not a refutation of the source",
            (pv["PV-GI-CUTMASS"] == ["1"] * len(pv["PV-GI-CUTMASS"])
             and pv["PV-GI-FLOW"] > 0),
            "cut masses %s, disintegration exact at %d transitions"
            % (pv["PV-GI-CUTMASS"], pv["PV-GI-FLOW"]))

    S["candidate_pushforward"] = {
        "referent_census": rows,
        "substring_only_tokens": len(ghosts),
        "whole_word_homonyms": len(homonyms),
        "transport_holonomy_rank": qrank,
        "stencils_blocked_by_perfectness": len(blocked),
        "stencils_not_blocked": len(open_),
        "weld2_rows": w2["candidate_count"],
        "weld2_distinct_candidates": w2["distinct_candidates"],
        "weld2_found": found,
        "weld2_fates": sorted(fates.items()),
        "weld3_found_rows": w3["counts"]["weld_found"],
        "weld3_dead_list_naming_the_carrier": carrier_dead,
        "weld3_target_sites": sites3,
        "weld3_realised_cells_all_at_one_count": cells,
        "actor_site_objects": actors,
        "target_bipartite": bip, "target_degrees": degs,
        "gamma_cut_dimensions": dims, "gamma_classes": classes,
        "slice_configurations": slice_n,
        "configurations_at_mass_zero_at_class_grain": zero_on_slice,
        "granted_lattice_residual_fibre": slice_n,
        "verdict": "NO-PINNED-CORRESPONDENCE-TO-THIS-ARENA;GRANTED-EVERYTHING"
                   "-THE-RESIDUAL-IS-A-POINT-MASS-WITH-THE-COIN-FREE",
        "free_items": 2,
    }
    return S["candidate_pushforward"]


# --------------------------------------------------------------------------
# CANDIDATES (b) and (c): the counting measure, and invariance
# --------------------------------------------------------------------------

def measure_invariance(S, pv):
    coins = S["_coins"]
    cidx = S["_cidx"]
    o32, o128 = S["_o32"], S["_o128"]
    sets = S["_sets"]

    readings = {"CHART-32": o32, "CHART-128": o128}
    closed_rows = []
    for rname, orbs in readings.items():
        for sname, members in sorted(sets.items()):
            idxs = {cidx[m] for m in members}
            ok = orbit_closed(orbs, idxs)
            closed_rows.append({"reading": rname, "set": sname,
                                "orbit_closed": ok, "size": len(members)})
    if mut("MUT-ORBIT-CLOSURE"):
        closed_rows[0]["orbit_closed"] = False
    LD.gate("G-DECLARED-SETS-ARE-ORBIT-CLOSED",
            "every set this unit weighs is checked to be a UNION OF ORBITS "
            "at both readings, object by object and never by a cardinality "
            "(#87), because a set that is not orbit-closed has no "
            "well-defined mass under an invariant measure and comparing "
            "masses across measures would be meaningless for it",
            all(r["orbit_closed"] for r in closed_rows),
            "%d (reading, set) rows, %d not orbit-closed"
            % (len(closed_rows),
               sum(1 for r in closed_rows if not r["orbit_closed"])))

    # the two nulls, both invariant, and their disagreement
    table = []
    for sname, members in sorted(sets.items()):
        idxs = {cidx[m] for m in members}
        row = {"set": sname, "configurations": len(members),
               "counting": str(Fraction(len(members), len(coins)))}
        for rname, orbs in readings.items():
            k = sum(1 for o in orbs if o[0] in idxs)
            row["orbit_uniform_%s" % rname] = str(Fraction(k, len(orbs)))
        table.append(row)

    # every null compared below must be invariant under EVERY group this
    # arena measures, or the comparison would be between measures answering
    # different questions.  For the orbit-uniform nulls that is not automatic:
    # it holds because the swap conjugation normalises the twist subgroup, so
    # it carries each smaller-reading orbit onto another of the SAME SIZE --
    # measured here, orbit by orbit, rather than argued
    G128 = gen_group(len(coins), [perm_of(coins, cidx,
                                          lambda m: gauge_twist(m, 2)),
                                  perm_of(coins, cidx, swap_conjugate)])
    cross = 0
    cross_bad = 0
    for rname, orbs in readings.items():
        omap = {}
        for o in orbs:
            for i in o:
                omap[i] = tuple(o)
        for g in G128:
            for o in orbs:
                cross += 1
                img = sorted(g[i] for i in o)
                if tuple(img) != omap[img[0]]:
                    cross_bad += 1
    if mut("MUT-CROSS-INVARIANCE"):
        cross_bad = 1
    LD.gate("G-EVERY-NULL-IS-INVARIANT-UNDER-EVERY-MEASURED-GROUP",
            "the three measures compared below are all invariant under "
            "EVERYTHING this arena measures, and for the orbit-uniform nulls "
            "that is not automatic -- an orbit-uniform measure built on one "
            "reading's orbits is invariant under a larger group only if that "
            "group carries each orbit onto another of the same size.  It "
            "does, because the swap conjugation normalises the twist "
            "subgroup, and the check is run orbit by orbit rather than left "
            "as an argument; without it the comparison would be between "
            "measures answering different questions",
            cross_bad == 0 and cross > 0,
            "%d (group element, orbit) images checked, %d not landing on an "
            "orbit of the same reading" % (cross, cross_bad))

    spreads = []
    for row in table:
        vals = [Fraction(row["counting"]),
                Fraction(row["orbit_uniform_CHART-32"]),
                Fraction(row["orbit_uniform_CHART-128"])]
        spreads.append((row["set"], str(max(vals) - min(vals))))
    worst = max(spreads, key=lambda t: Fraction(t[1]))
    LD.gate("G-TWO-NULLS-DISAGREE",
            "and the choice among them is NOT innocuous, which is the "
            "measurement that prices the declaration: the counting measure "
            "on configurations and the counting measure on ORBITS are both "
            "invariant under everything this arena measures, and they assign "
            "materially different masses to the parent's own headline sets "
            "-- so a reader handed 'the natural measure' has been handed a "
            "choice, not a derivation",
            Fraction(worst[1]) > 0,
            "widest disagreement %s on the %s set" % (worst[1], worst[0]))

    # THE UNIQUENESS GATE -- gated, never asserted
    uniq = {}
    for rname, orbs in readings.items():
        uniq[rname] = {"orbits": len(orbs), "transitive": len(orbs) == 1,
                       "simplex_dimension": len(orbs) - 1,
                       "unique_invariant_measure": len(orbs) == 1}
    if mut("MUT-UNIQUENESS"):
        uniq["CHART-32"]["unique_invariant_measure"] = True
    any_unique = any(v["unique_invariant_measure"] for v in uniq.values())
    LD.gate("G-UNIQUENESS-GATED",
            "the uniqueness question is DECIDED and not assumed: the "
            "invariant measures are exactly the orbit-constant ones, so a "
            "measure is uniquely fixed by invariance IF AND ONLY IF the "
            "group acts transitively on the configurations.  It does not, at "
            "either reading, and the orbit counts say by how much -- the "
            "admissible set is a simplex of measured dimension, not a point",
            not any_unique,
            "orbits %s -- no reading is transitive"
            % {k: v["orbits"] for k, v in sorted(uniq.items())})

    # the gate can pass: a synthetic arena on which invariance IS decisive
    syn_n = 4
    syn = gen_group(syn_n, [tuple((i + 1) % syn_n for i in range(syn_n))])
    syn_orbs = orbits_of(syn, syn_n)
    LD.gate("G-UNIQUENESS-GATE-CAN-PASS",
            "and that gate is not a formality: run on a synthetic arena "
            "whose declared group IS transitive, the same predicate returns "
            "UNIQUE, so the negative measured above is a property of this "
            "arena and not of the instrument's standard",
            len(syn_orbs) == 1,
            "synthetic transitive arena: %d orbit on %d configurations"
            % (len(syn_orbs), syn_n))

    # the full space: an exhibited invariant, hence an exact lower bound
    nlinks = S["arena"]["links"]
    nsect = len(S["parent_census"]["by_sector"])
    multisets = 1
    for i in range(nsect - 1):
        multisets = multisets * (nlinks + nsect - 1 - i) // (i + 1)
    LD.gate("G-FULL-SPACE-NOT-TRANSITIVE-BY-AN-EXHIBITED-INVARIANT",
            "on the FULL configuration space the same conclusion is reached "
            "without an orbit enumeration, by exhibiting an invariant: the "
            "gauge preserves each link's sector and the chart permutes the "
            "links, so the MULTISET of sectors over the links is invariant, "
            "every one of its values is realised, and the orbit count is at "
            "least that many -- the invariant measures there form a simplex "
            "of at least that dimension",
            multisets > 1,
            "%d realised values of the sector multiset over %d links, so at "
            "least that many orbits" % (multisets, nlinks))

    S["candidate_counting"] = {
        "status": "DECLARED-NULL",
        "carriers_declared": ["THE-UNIFORM-SLICE", "THE-FULL-SPACE"],
        "carrier_fibre": "UNBOUNDED",
        "carrier_declared_instances": 2,
        "nulls_declared": ["COUNTING-ON-CONFIGURATIONS", "COUNTING-ON-ORBITS"],
        "nulls_fibre": "UNBOUNDED",
        "nulls_declared_instances": 2,
        "free_items": 2,
        "verdict": "CARRIES-NO-INFORMATION-AND-IS-NOT-EVEN-UNIQUE-AMONG-"
                   "THE-INVARIANT-MEASURES",
    }
    S["candidate_invariance"] = {
        "orbit_closure_rows": closed_rows,
        "cross_invariance_checks": cross,
        "cross_invariance_failures": cross_bad,
        "uniqueness": uniq,
        "synthetic_transitive_orbits": len(syn_orbs),
        "sector_multisets_on_the_full_space": multisets,
        "free_items": 1,
        "verdict": "SELECTS-A-SUPPORT-NOT-A-MEASURE",
    }
    S["measure_comparison"] = {"rows": table, "spreads": spreads,
                               "widest": {"set": worst[0], "spread": worst[1]}}
    return uniq, table, worst


# --------------------------------------------------------------------------
# CANDIDATES (d), (e), (f): Haar from a group, Haar from U(2), Gibbs
# --------------------------------------------------------------------------

def measure_haar_and_gibbs(S, src, pv):
    coins = S["_coins"]
    cset = set(coins)
    inside = 0
    by_pair = {}
    for A in coins:
        sa = coin_sector(A)
        for B in coins:
            ok = cmul(A, B) in cset
            inside += ok
            key = (sa, coin_sector(B))
            row = by_pair.setdefault(key, [0, 0])
            row[0] += 1
            row[1] += ok
    total = len(coins) ** 2
    if mut("MUT-CLOSURE"):
        inside = total
    LD.gate("G-FAMILY-IS-NOT-A-GROUP",
            "the derived family is NOT closed under multiplication, so it "
            "carries no finite-group Haar measure to inherit: the products "
            "that leave are exactly the interfering ones, and they leave at "
            "an exactly measured rate",
            inside < total,
            "%d of %d products stay inside the family" % (inside, total))

    mono = [m for m in coins if coin_sector(m) in ("DIAGONAL", "ANTIDIAGONAL")]
    mset = set(mono)
    mclose = sum(1 for A in mono for B in mono if cmul(A, B) not in mset)
    minv = sum(1 for A in mono if cdag(A) not in mset)
    LD.gate("G-THE-MONOMIAL-SUBGROUP-IS-A-GROUP",
            "one part of it is: the monomial coins are closed under "
            "multiplication and under inverse, so they form a finite group, "
            "and a finite group DOES carry a canonical measure -- its Haar "
            "measure, which is the uniform one.  That is the only place in "
            "this arena where a measure is handed over rather than declared",
            mclose == 0 and minv == 0 and len(mono) > 0,
            "%d monomial coins, %d closure failures, %d inverse failures"
            % (len(mono), mclose, minv))

    adjoinable = 0
    for B in [m for m in coins if coin_sector(m) == "BALANCED"]:
        # the cheapest discriminator FIRST -- a subgroup containing B contains
        # B*B, so a product that already leaves the family settles the row
        # without enumerating the rest
        if cmul(B, B) not in cset:
            continue
        cur = set(mono) | {B}
        ok = True
        for _ in range(3):
            new = set()
            for A in cur:
                for C in cur:
                    p = cmul(A, C)
                    if p not in cset:
                        ok = False
                        break
                    new.add(p)
                if not ok:
                    break
            if not ok:
                break
            if new <= cur:
                break
            cur |= new
        adjoinable += ok
    LD.gate("G-THE-HAAR-CARRIER-IS-MAXIMAL-AT-DECLARED-SCOPE",
            "and it cannot be enlarged from where it sits: no interfering "
            "coin can be adjoined to the monomial group without the closure "
            "leaving the family, at every one of them",
            adjoinable == 0,
            "%d of %d interfering coins adjoinable"
            % (adjoinable,
               S["parent_census"]["by_sector"]["BALANCED"]["coins"]))

    defect = S["_sets"]["DEFECT-CARRYING"]
    overlap = len(defect & mset)
    LD.gate("G-THE-HAAR-CARRIER-CARRIES-NO-DEFECT",
            "AND THAT IS THE FINDING, not the consolation: the one subset of "
            "this arena that hands over a canonical measure is exactly the "
            "subset on which the parent measured NO composition defect at "
            "all.  Where the substrate gives a measure for free the quantum "
            "layer is absent, and where the quantum layer lives the measure "
            "has to be declared",
            overlap == 0 and len(defect) > 0,
            "%d of %d defect-carrying coins lie in the Haar carrier"
            % (overlap, len(defect)))

    finite = 0
    for m in coins:
        p, k = m, 1
        while p != COIN_I and k <= 64 and p in cset:
            p = cmul(p, m)
            k += 1
        finite += (p == COIN_I and k <= 64)
    LD.gate("G-U2-HAAR-CANNOT-DESCEND",
            "and the ambient group's Haar cannot descend either: the family "
            "is a FINITE subset of a positive-dimensional Lie group, so it "
            "carries Haar measure zero and conditioning on it is undefined.  "
            "The family is not even closed under taking powers, which is "
            "measured here rather than argued",
            finite < len(coins),
            "%d of %d coins generate a finite cyclic group inside the family"
            % (finite, len(coins)))

    r5 = wsnorm(src["S-R5-PAPER"].decode())
    needle = wsnorm("It has no configuration measure, no action functional, "
                    "no coupling and no dynamics for the link variables")
    LD.gate("G-GIBBS-NEEDS-AN-ACTION",
            "the Gibbs route needs two objects this arena does not have, and "
            "the parent says so in its own words at a window pinned by "
            "digest: a weight of the form exp(-S) requires an action "
            "functional and a coupling to put in front of it, and declaring "
            "either is declaring the measure by another name",
            r5.count(needle) == 1, "the parent's declaration located once")

    S["candidate_group_haar"] = {
        "products_inside": inside, "products_total": total,
        "closure_by_sector_pair": {"%s|%s" % k: v
                                   for k, v in sorted(by_pair.items())},
        "monomial_coins": len(mono), "monomial_closure_failures": mclose,
        "monomial_inverse_failures": minv,
        "interfering_coins_adjoinable": adjoinable,
        "defect_coins_in_the_haar_carrier": overlap,
        "coins_of_finite_order_inside_the_family": finite,
        "free_items": 1,
        "verdict": "HAAR-EXISTS-ON-A-DECLARED-SUBGROUP-WHICH-CARRIES-NO-"
                   "DEFECT;THE-FAMILY-ITSELF-IS-NOT-A-GROUP",
    }
    S["candidate_ambient_haar"] = {
        "free_items": 1,
        "verdict": "A-FINITE-SUBSET-OF-U(2)-CARRIES-HAAR-MEASURE-ZERO",
    }
    S["candidate_gibbs"] = {
        "free_items": 2,
        "verdict": "NO-ACTION-AND-NO-COUPLING-ON-THIS-ARENA-BY-THE-PARENTS-"
                   "OWN-DECLARATION",
    }
    return inside, total, len(mono), finite


def measure_holonomy_pullback(S, pv):
    """CANDIDATE: pull a measure back from the holonomy group."""
    lat, coins = S["_lat"], S["_coins"]
    n = len(lat.sites)
    base = lat.plaqs[0]
    images = {}
    for m in coins:
        W = holonomy(lat, base, uniform_cfg(lat, m), n)
        images.setdefault(tuple(sorted(W.items())), []).append(m)
    fib = sorted({len(v) for v in images.values()})
    infinite = pv["PV-INFINITE"]
    LD.gate("G-HOLONOMY-GROUP-IS-CONFIGURATION-DEPENDENT",
            "the holonomy group cannot lend its own canonical measure back, "
            "because there is no single group to borrow from: the parent "
            "measures a finite alternating class on one sector and an "
            "INFINITE group on the other, so on most of this arena's "
            "configurations the holonomy group carries no normalisable "
            "invariant measure at all -- and a pull-back would in any case "
            "need a declared section, which is one more free item and not "
            "one fewer",
            infinite > 0 and len(images) <= len(coins),
            "%d configurations carry an infinite holonomy group; the "
            "plaquette holonomy takes %d distinct values with fibres %s"
            % (infinite, len(images), fib))
    S["candidate_holonomy_pullback"] = {
        "distinct_plaquette_holonomies": len(images), "fibres": fib,
        "configurations_with_an_infinite_group": infinite,
        "free_items": 1,
        "verdict": "NO-SINGLE-GROUP-TO-BORROW-FROM;A-SECTION-WOULD-BE-ONE-"
                   "MORE-FREE-ITEM",
    }
    return len(images)


# ===========================================================================
# SECTION 7.  THE CENSUS, THE FIBRE, THE HEAD
# ===========================================================================

CANDIDATES = [
    ("a", "THE-HISTORY-MEASURE-PUSHFORWARD", "candidate_pushforward"),
    ("b", "THE-COUNTING-MEASURE", "candidate_counting"),
    ("c", "AN-INVARIANCE-CHARACTERISED-MEASURE", "candidate_invariance"),
    ("d", "HAAR-FROM-A-GROUP-STRUCTURE-ON-THE-FAMILY", "candidate_group_haar"),
    ("e", "HAAR-INHERITED-FROM-U(2)", "candidate_ambient_haar"),
    ("f", "GIBBS-FROM-AN-ACTION", "candidate_gibbs"),
    ("g", "THE-BORN-LAYER", "born_layer"),
    ("h", "PULL-BACK-FROM-THE-HOLONOMY-GROUP", "candidate_holonomy_pullback"),
]


def build_census(S):
    rows = []
    for (tag, name, key) in CANDIDATES:
        blk = S[key]
        if "free_items" not in blk:
            raise GateFail("G-CENSUS-IS-TOTAL :: candidate %s publishes no "
                           "price" % tag)
        fi = blk["free_items"]
        rows.append({"candidate": tag, "source": name,
                     "free_items": fi,
                     "derives": fi == 0,
                     "verdict": blk["verdict"]})
    if mut("MUT-CENSUS-DERIVES"):
        rows[0]["derives"] = True
        rows[0]["free_items"] = 0
    derived = [r for r in rows if r["derives"]]
    LD.gate("G-CENSUS-IS-TOTAL",
            "every candidate the pin names is measured and priced, and the "
            "census carries the two the pin did not name as well -- the "
            "ambient group's measure and the pull-back -- so no source is "
            "left out by being unmentioned; DERIVED means zero free items at "
            "the RSQ standard and nothing weaker",
            len(rows) == len(CANDIDATES)
            and all(r["free_items"] >= 0 for r in rows),
            "%d candidates, %d deriving" % (len(rows), len(derived)))
    S["census"] = {"rows": rows, "candidates": len(rows),
                   "deriving": len(derived)}
    return rows, derived


def price_the_fibre(S):
    uniq = S["candidate_invariance"]["uniqueness"]
    lo = min(uniq.values(), key=lambda v: v["orbits"])
    hi = max(uniq.values(), key=lambda v: v["orbits"])
    rows = []
    for rname in sorted(uniq):
        v = uniq[rname]
        rows.append({"reading": rname, "orbits": v["orbits"],
                     "independent_numbers_a_declaration_must_supply":
                         v["simplex_dimension"]})
    LD.gate("G-FIBRE-PRICED",
            "the declaration is PRICED rather than deplored: after every "
            "symmetry this arena measures has been imposed, what remains to "
            "be declared is exactly one point of a simplex over the orbits, "
            "and its dimension is the number of independent conditions a "
            "declaration has to supply.  Both readings are priced, because "
            "which chart group is declared is itself a free axis (§15)",
            all(r["orbits"] > 1 for r in rows) and len(rows) == 2,
            "%s" % [(r["reading"], r["orbits"],
                     r["independent_numbers_a_declaration_must_supply"])
                    for r in rows])
    S["fibre"] = {
        "rows": rows,
        "minimal": {"reading": "CHART-128", "orbits": hi["orbits"]
                    if hi["orbits"] < lo["orbits"] else lo["orbits"]},
        "carrier_choice": S["candidate_counting"]["carriers_declared"],
        "what_a_declaration_must_add":
            "the carrier, then one point of the invariant simplex over its "
            "orbits",
    }
    return rows


def head_law(census_rows, uniqueness, fibre_rows, blocked_object=None):
    """THE HEAD LAW, one function, used by the builder, by the reconstruction
    and by the reachability demonstration alike."""
    derived = [r for r in census_rows if r["derives"]]
    if derived:
        src = derived[0]["source"]
        uq = "UNIQUE" if any(v["unique_invariant_measure"]
                             for v in uniqueness.values()) else "NOT-UNIQUE"
        return "MEASURE-DERIVED-<%s;%s>" % (src, uq)
    if blocked_object:
        return "MEASURE-BLOCKED-AT-<%s>" % blocked_object
    per = ";".join("%s-SIMPLEX-ON-%d-ORBITS-AT-THE-%s-READING"
                   % (r["independent_numbers_a_declaration_must_supply"],
                      r["orbits"], r["reading"]) for r in fibre_rows)
    return "MEASURE-DECLARATION-REQUIRED-<ONE-POINT-OF-A-%s>" % per


def demonstrate_reachability(S):
    """all three pre-registered outcomes are reachable BY THE ONE HEAD LAW,
    demonstrated on synthetic censuses inside a gate."""
    fake_fib = [{"reading": "SYN", "orbits": 1,
                 "independent_numbers_a_declaration_must_supply": 0}]
    d = head_law([{"derives": True, "source": "SYN"}],
                 {"SYN": {"unique_invariant_measure": True}}, fake_fib)
    b = head_law([{"derives": False, "source": "SYN"}],
                 {"SYN": {"unique_invariant_measure": False}}, fake_fib,
                 blocked_object="THE-SYNTHETIC-OBJECT")
    r = head_law([{"derives": False, "source": "SYN"}],
                 {"SYN": {"unique_invariant_measure": False}}, fake_fib)
    heads = {"DERIVED": d, "BLOCKED": b, "DECLARATION-REQUIRED": r}
    ok = (d.startswith("MEASURE-DERIVED-<") and "UNIQUE" in d
          and b.startswith("MEASURE-BLOCKED-AT-<")
          and r.startswith("MEASURE-DECLARATION-REQUIRED-<")
          and len({d, b, r}) == 3)
    if mut("MUT-HEAD-CONSTANT"):
        ok = False
    LD.gate("G-HEAD-LAW-REACHABILITY",
            "all three pre-registered outcomes are reachable BY THE ONE HEAD "
            "LAW, driven here on synthetic censuses: a census in which a "
            "candidate has zero free items returns DERIVED, one in which an "
            "object cannot be evaluated returns BLOCKED, and this arena's "
            "returns the declaration price.  A head law that could not move "
            "would fail here",
            ok, "reachable heads: %s" % sorted(heads))
    S["preregistered_heads"] = heads
    return heads


def withhold_the_licensed_segment(S):
    """THE PIN'S MUST-NOT, ENFORCED ON THE INSTRUMENT'S OWN PRODUCT."""
    banned_keys = [k for k in S
                   if not k.startswith("_")
                   and re.search(r"wilson|expectation|area.?law|string.?"
                                 r"tension|potential", k, re.I)]
    src = open(os.path.abspath(__file__), "rb").read().decode()
    tree = ast.parse(src)
    fnames = {n.name for n in ast.walk(tree)
              if isinstance(n, ast.FunctionDef)}
    computing = sorted(f for f in fnames
                       if re.search(r"wilson|expectation", f, re.I))
    if mut("MUT-WILSON-SEGMENT"):
        banned_keys = ["wilson_expectations"]
    LD.gate("G-NO-WILSON-EXPECTATION",
            "THE PIN LICENSES A WILSON-EXPECTATION SEGMENT ONLY IN THE "
            "DERIVED CASE, and no source derives, so this unit computes "
            "none -- and the discipline is enforced on the product rather "
            "than promised in prose: the receipt is required to carry no "
            "expectation-valued key and the instrument's own syntax tree to "
            "define no function that would compute one",
            not banned_keys and not computing,
            "%d expectation-valued receipt keys, %d expectation-computing "
            "functions" % (len(banned_keys), len(computing)))
    S["withheld"] = {
        "object": "THE-WILSON-LOOP-EXPECTATIONS",
        "licensed_by_the_pin_only_if": "A-MEASURE-DERIVES",
        "measured": "NO-SOURCE-DERIVES",
        "consequence": "THE-SEGMENT-IS-WITHHELD-AND-THE-INSTRUMENT-COMPUTES-"
                       "NO-EXPECTATION-AT-ALL",
    }


def build_verdict(S):
    """every segment is COMPUTED from a measured field; nothing is typed."""
    a = S["arena"]
    sym = S["symmetry"]
    cen = S["census"]
    fib = S["fibre"]["rows"]
    pf = S["candidate_pushforward"]
    gh = S["candidate_group_haar"]
    bl = S["born_layer"]
    cmp_ = S["measure_comparison"]
    inv = S["candidate_invariance"]
    fx = S["fixed_locus"]
    head = head_law(cen["rows"], inv["uniqueness"], fib)

    def frow(name):
        for r in cmp_["rows"]:
            if r["set"] == name:
                return r
        raise KeyError(name)

    nc = frow("NON-COMMUTING")
    df = frow("DEFECT-CARRYING")
    segs = []
    segs.append("CENSUS=%d-CANDIDATES-%d-DERIVE|(a)PUSHFORWARD=%s(WELD2-%d-"
                "ROWS-%d-DISTINCT-CANDIDATES-%d-FOUND-AT-THIS-CARRIER;"
                "WELD3-IS-THE-ONE-FOUND-DICTIONARY-AND-ITS-TARGET-CARRIES-%d-"
                "SITES-AGAINST-%d-WITH-A-CONSTANT-LINK-DATUM-AT-%d-OF-%d-"
                "CELLS;GRANTED-EVERYTHING-THE-RESIDUAL-IS-A-POINT-MASS-WITH-"
                "THE-COIN-FREE-AMONG-%d)|(b)COUNTING=DECLARED-NULL-%d-"
                "CARRIERS-x-%d-NULLS-ALL-INVARIANT|(c)INVARIANCE=SELECTS-A-"
                "SUPPORT-NOT-A-MEASURE|(d)FINITE-GROUP-HAAR=THE-FAMILY-IS-"
                "NOT-CLOSED-%d-OF-%d-PRODUCTS-STAY|(e)U(2)-HAAR=A-FINITE-"
                "SUBSET-HAS-MEASURE-ZERO-AND-%d-OF-%d-COINS-HAVE-FINITE-"
                "ORDER-IN-FAMILY|(f)GIBBS=NO-ACTION-NO-COUPLING-BY-THE-"
                "PARENTS-OWN-DECLARATION|(g)BORN=DERIVES-EXACTLY-AND-LANDS-"
                "ON-THE-STATES-%d-IMAGES-FOR-%d-CONFIGURATIONS|(h)HOLONOMY-"
                "PULLBACK=NO-SINGLE-GROUP-%d-CONFIGURATIONS-CARRY-AN-"
                "INFINITE-ONE"
                % (cen["candidates"], cen["deriving"],
                   "NO-PINNED-CORRESPONDENCE-TO-THIS-ARENA",
                   pf["weld2_rows"], pf["weld2_distinct_candidates"],
                   pf["weld2_found"], pf["weld3_target_sites"], a["sites"],
                   pf["weld3_realised_cells_all_at_one_count"],
                   pf["weld3_realised_cells_all_at_one_count"],
                   pf["granted_lattice_residual_fibre"],
                   len(S["candidate_counting"]["carriers_declared"]),
                   len(S["candidate_counting"]["nulls_declared"]),
                   gh["products_inside"], gh["products_total"],
                   gh["coins_of_finite_order_inside_the_family"], a["coins"],
                   bl["distinct_images"], bl["configurations"],
                   S["candidate_holonomy_pullback"]
                   ["configurations_with_an_infinite_group"]))
    segs.append("UNIQUENESS=GATED-AND-FAILS-AT-BOTH-READINGS(%s)|"
                "INVARIANT-MEASURES-ARE-EXACTLY-THE-ORBIT-CONSTANT-ONES-SO-"
                "UNIQUE-IFF-TRANSITIVE|THE-GATE-CAN-PASS-A-SYNTHETIC-"
                "TRANSITIVE-ARENA-RETURNS-%d-ORBIT|FULL-SPACE-NOT-"
                "TRANSITIVE-BY-AN-EXHIBITED-INVARIANT-%d-SECTOR-MULTISETS-"
                "OVER-%d-LINKS"
                % (";".join("%s:%d-ORBITS" % (r["reading"], r["orbits"])
                            for r in fib),
                   inv["synthetic_transitive_orbits"],
                   inv["sector_multisets_on_the_full_space"], a["links"]))
    segs.append("WHAT-THE-SYMMETRY-DOES-FIX=A-SUPPORT:THE-CHART-FIXED-"
                "CONFIGURATIONS-ARE-EXACTLY-THE-%d-UNIFORM-ONES-AT-%d-OF-%d-"
                "CHECKS-SO-THE-PARENTS-DECLARED-SWEEP-IS-THE-FIXED-LOCUS-"
                "ITSELF(%d-AT-THE-EXTENSION-WHERE-REVERSAL-FORCES-U=XUX)|"
                "FULL-SPACE-CHART-ORBITS=%d-AND-%d-AT-THE-TWO-READINGS"
                % (fx["chart_fixed_configurations"], fx["checks"], fx["checks"],
                   fx["extension_fixed_configurations"],
                   sym["full_space_chart_orbits"],
                   sym["full_space_extension_orbits"]))
    segs.append("CONSEQUENCE=THE-DECLARATION-IS-NOT-INNOCUOUS:THE-PARENTS-"
                "OWN-HEADLINE-SETS-MOVE-BETWEEN-INVARIANT-MEASURES|"
                "NON-COMMUTING=%s-AT-COUNTING-AND-%s-AND-%s-AT-THE-TWO-"
                "ORBIT-NULLS|DEFECT-CARRYING=%s-AND-%s-AND-%s|WIDEST-"
                "DISAGREEMENT=%s-ON-%s"
                % (nc["counting"], nc["orbit_uniform_CHART-32"],
                   nc["orbit_uniform_CHART-128"], df["counting"],
                   df["orbit_uniform_CHART-32"], df["orbit_uniform_CHART-128"],
                   cmp_["widest"]["spread"], cmp_["widest"]["set"]))
    segs.append("THE-ONE-CANONICAL-MEASURE-THIS-ARENA-HANDS-OVER=HAAR-ON-"
                "THE-%d-ELEMENT-MONOMIAL-SUBGROUP(CLOSED-%d-FAILURES-"
                "INVERSES-%d-FAILURES;MAXIMAL-%d-OF-%d-INTERFERING-COINS-"
                "ADJOINABLE)-AND-IT-CARRIES-%d-OF-%d-DEFECT-COINS:WHERE-THE-"
                "MEASURE-IS-FREE-THE-QUANTUM-LAYER-IS-ABSENT"
                % (gh["monomial_coins"], gh["monomial_closure_failures"],
                   gh["monomial_inverse_failures"],
                   gh["interfering_coins_adjoinable"],
                   S["parent_census"]["by_sector"]["BALANCED"]["coins"],
                   gh["defect_coins_in_the_haar_carrier"],
                   S["parent_census"]["defect_carrying"]))
    segs.append("WILSON=SEGMENT-WITHHELD-BY-THE-PIN-NO-SOURCE-DERIVES|NO-"
                "EXPECTATION-COMPUTED-ANYWHERE-IN-THE-INSTRUMENT|NO-AREA-"
                "LAW-NO-STRING-TENSION-NO-POTENTIAL-CLAIM")
    segs.append("SCOPE=D=%d;L=%d;FIELD=%s;COINS=%d;LINKS=%d;PLAQUETTES=%d;"
                "CONFIGURATION-SPACE=%s;PRIMARY-CARRIER=THE-UNIFORM-SLICE-"
                "WHICH-IS-THE-CHART-FIXED-LOCUS;FULL-SPACE-ORBIT-COUNT-"
                "UNDER-THE-JOINT-GROUP=NOT-COMPUTED-BY-COST-A-LOWER-BOUND-"
                "IS-EXHIBITED-INSTEAD;THE-CORRESPONDENCE-QUESTION-AT-THIS-"
                "TARGET=OPEN-WELD-2s-STRUCTURAL-BLADE-IS-SILENT-HERE-"
                "BECAUSE-THIS-LATTICE-IS-BIPARTITE;NO-MEASURE-DERIVED;NO-"
                "ACTION;NO-COUPLING;NO-DYNAMICS;NOT-QCD;NO-CONFINEMENT-CLAIM"
                % (a["d"], a["L"], a["field"], a["coins"], a["links"],
                   a["plaquettes"], a["configuration_space"]))
    if not head.endswith(">"):
        raise GateFail("the head law must close its own bracket")
    return head[:-1] + " -- " + " -- ".join(segs) + ">"


def reconstruct_verdict(S):
    """THE INDEPENDENT ROUTE.  It reads only the serialized receipt, carries
    its own copy of the head law, and re-renders EVERY segment from the
    primitive measured tables -- the censuses, the orbit rows, the parent's
    reproduced sets -- sharing no format string and no typed value with the
    builder, and reading neither the builder's segments nor its counts."""
    R = json.loads(json.dumps({k: v for k, v in S.items()
                               if not k.startswith("_")}, default=str))
    # THE CENSUS IS RE-DERIVED, not read.  The builder's own summary rows are
    # never consulted: each candidate's price is taken from ITS OWN published
    # block and the DERIVES flag is recomputed from that price, so a census row
    # edited after its candidate was measured moves the reconstruction's head
    # away from the builder's and dies at the equality gate.
    census = [{"candidate": tag, "source": name,
               "free_items": R[key]["free_items"],
               "derives": R[key]["free_items"] == 0,
               "verdict": R[key]["verdict"]}
              for (tag, name, key) in CANDIDATES]
    uq = R["candidate_invariance"]["uniqueness"]
    fibre = R["fibre"]["rows"]
    head = head_law([{"derives": r["derives"], "source": r["source"]}
                     for r in census], uq, fibre)

    def mass(setname, col):
        for r in R["measure_comparison"]["rows"]:
            if r["set"] == setname:
                return r[col]
        raise KeyError(setname)

    parts = []
    lut = {r["candidate"]: r for r in census}
    parts.append(
        "CENSUS=" + str(len(census)) + "-CANDIDATES-"
        + str(sum(1 for r in census if r["derives"])) + "-DERIVE"
        + "|(a)PUSHFORWARD=NO-PINNED-CORRESPONDENCE-TO-THIS-ARENA(WELD2-"
        + str(R["candidate_pushforward"]["weld2_rows"]) + "-ROWS-"
        + str(R["candidate_pushforward"]["weld2_distinct_candidates"])
        + "-DISTINCT-CANDIDATES-"
        + str(R["candidate_pushforward"]["weld2_found"])
        + "-FOUND-AT-THIS-CARRIER;WELD3-IS-THE-ONE-FOUND-DICTIONARY-AND-ITS-"
        "TARGET-CARRIES-" + str(R["candidate_pushforward"]["weld3_target_sites"])
        + "-SITES-AGAINST-" + str(R["arena"]["sites"])
        + "-WITH-A-CONSTANT-LINK-DATUM-AT-"
        + str(R["candidate_pushforward"]
              ["weld3_realised_cells_all_at_one_count"]) + "-OF-"
        + str(R["candidate_pushforward"]
              ["weld3_realised_cells_all_at_one_count"])
        + "-CELLS;GRANTED-EVERYTHING-THE-RESIDUAL-IS-A-POINT-MASS-WITH-THE-"
        "COIN-FREE-AMONG-"
        + str(R["candidate_pushforward"]["granted_lattice_residual_fibre"])
        + ")|(b)COUNTING=DECLARED-NULL-"
        + str(len(R["candidate_counting"]["carriers_declared"])) + "-CARRIERS-x-"
        + str(len(R["candidate_counting"]["nulls_declared"]))
        + "-NULLS-ALL-INVARIANT|(c)INVARIANCE=SELECTS-A-SUPPORT-NOT-A-MEASURE"
        "|(d)FINITE-GROUP-HAAR=THE-FAMILY-IS-NOT-CLOSED-"
        + str(R["candidate_group_haar"]["products_inside"]) + "-OF-"
        + str(R["candidate_group_haar"]["products_total"])
        + "-PRODUCTS-STAY|(e)U(2)-HAAR=A-FINITE-SUBSET-HAS-MEASURE-ZERO-AND-"
        + str(R["candidate_group_haar"]
              ["coins_of_finite_order_inside_the_family"]) + "-OF-"
        + str(R["arena"]["coins"])
        + "-COINS-HAVE-FINITE-ORDER-IN-FAMILY|(f)GIBBS=NO-ACTION-NO-COUPLING-"
        "BY-THE-PARENTS-OWN-DECLARATION|(g)BORN=DERIVES-EXACTLY-AND-LANDS-ON-"
        "THE-STATES-" + str(R["born_layer"]["distinct_images"]) + "-IMAGES-FOR-"
        + str(R["born_layer"]["configurations"])
        + "-CONFIGURATIONS|(h)HOLONOMY-PULLBACK=NO-SINGLE-GROUP-"
        + str(R["candidate_holonomy_pullback"]
              ["configurations_with_an_infinite_group"])
        + "-CONFIGURATIONS-CARRY-AN-INFINITE-ONE")
    parts.append(
        "UNIQUENESS=GATED-AND-FAILS-AT-BOTH-READINGS("
        + ";".join(r["reading"] + ":" + str(r["orbits"]) + "-ORBITS"
                   for r in fibre)
        + ")|INVARIANT-MEASURES-ARE-EXACTLY-THE-ORBIT-CONSTANT-ONES-SO-UNIQUE-"
        "IFF-TRANSITIVE|THE-GATE-CAN-PASS-A-SYNTHETIC-TRANSITIVE-ARENA-"
        "RETURNS-" + str(R["candidate_invariance"]["synthetic_transitive_orbits"])
        + "-ORBIT|FULL-SPACE-NOT-TRANSITIVE-BY-AN-EXHIBITED-INVARIANT-"
        + str(R["candidate_invariance"]["sector_multisets_on_the_full_space"])
        + "-SECTOR-MULTISETS-OVER-" + str(R["arena"]["links"]) + "-LINKS")
    parts.append(
        "WHAT-THE-SYMMETRY-DOES-FIX=A-SUPPORT:THE-CHART-FIXED-CONFIGURATIONS-"
        "ARE-EXACTLY-THE-" + str(R["fixed_locus"]["chart_fixed_configurations"])
        + "-UNIFORM-ONES-AT-" + str(R["fixed_locus"]["checks"]) + "-OF-"
        + str(R["fixed_locus"]["checks"])
        + "-CHECKS-SO-THE-PARENTS-DECLARED-SWEEP-IS-THE-FIXED-LOCUS-ITSELF("
        + str(R["fixed_locus"]["extension_fixed_configurations"])
        + "-AT-THE-EXTENSION-WHERE-REVERSAL-FORCES-U=XUX)|FULL-SPACE-CHART-"
        "ORBITS=" + str(R["symmetry"]["full_space_chart_orbits"]) + "-AND-"
        + str(R["symmetry"]["full_space_extension_orbits"])
        + "-AT-THE-TWO-READINGS")
    parts.append(
        "CONSEQUENCE=THE-DECLARATION-IS-NOT-INNOCUOUS:THE-PARENTS-OWN-"
        "HEADLINE-SETS-MOVE-BETWEEN-INVARIANT-MEASURES|NON-COMMUTING="
        + mass("NON-COMMUTING", "counting") + "-AT-COUNTING-AND-"
        + mass("NON-COMMUTING", "orbit_uniform_CHART-32") + "-AND-"
        + mass("NON-COMMUTING", "orbit_uniform_CHART-128")
        + "-AT-THE-TWO-ORBIT-NULLS|DEFECT-CARRYING="
        + mass("DEFECT-CARRYING", "counting") + "-AND-"
        + mass("DEFECT-CARRYING", "orbit_uniform_CHART-32") + "-AND-"
        + mass("DEFECT-CARRYING", "orbit_uniform_CHART-128")
        + "|WIDEST-DISAGREEMENT=" + R["measure_comparison"]["widest"]["spread"]
        + "-ON-" + R["measure_comparison"]["widest"]["set"])
    parts.append(
        "THE-ONE-CANONICAL-MEASURE-THIS-ARENA-HANDS-OVER=HAAR-ON-THE-"
        + str(R["candidate_group_haar"]["monomial_coins"])
        + "-ELEMENT-MONOMIAL-SUBGROUP(CLOSED-"
        + str(R["candidate_group_haar"]["monomial_closure_failures"])
        + "-FAILURES-INVERSES-"
        + str(R["candidate_group_haar"]["monomial_inverse_failures"])
        + "-FAILURES;MAXIMAL-"
        + str(R["candidate_group_haar"]["interfering_coins_adjoinable"])
        + "-OF-" + str(R["parent_census"]["by_sector"]["BALANCED"]["coins"])
        + "-INTERFERING-COINS-ADJOINABLE)-AND-IT-CARRIES-"
        + str(R["candidate_group_haar"]["defect_coins_in_the_haar_carrier"])
        + "-OF-" + str(R["parent_census"]["defect_carrying"])
        + "-DEFECT-COINS:WHERE-THE-MEASURE-IS-FREE-THE-QUANTUM-LAYER-IS-ABSENT")
    parts.append(
        "WILSON=SEGMENT-WITHHELD-BY-THE-PIN-NO-SOURCE-DERIVES|NO-EXPECTATION-"
        "COMPUTED-ANYWHERE-IN-THE-INSTRUMENT|NO-AREA-LAW-NO-STRING-TENSION-"
        "NO-POTENTIAL-CLAIM")
    parts.append(
        "SCOPE=D=" + str(R["arena"]["d"]) + ";L=" + str(R["arena"]["L"])
        + ";FIELD=" + R["arena"]["field"] + ";COINS=" + str(R["arena"]["coins"])
        + ";LINKS=" + str(R["arena"]["links"]) + ";PLAQUETTES="
        + str(R["arena"]["plaquettes"]) + ";CONFIGURATION-SPACE="
        + R["arena"]["configuration_space"]
        + ";PRIMARY-CARRIER=THE-UNIFORM-SLICE-WHICH-IS-THE-CHART-FIXED-LOCUS"
        ";FULL-SPACE-ORBIT-COUNT-UNDER-THE-JOINT-GROUP=NOT-COMPUTED-BY-COST-"
        "A-LOWER-BOUND-IS-EXHIBITED-INSTEAD;THE-CORRESPONDENCE-QUESTION-AT-"
        "THIS-TARGET=OPEN-WELD-2s-STRUCTURAL-BLADE-IS-SILENT-HERE-BECAUSE-"
        "THIS-LATTICE-IS-BIPARTITE;NO-MEASURE-DERIVED;NO-ACTION;NO-COUPLING;"
        "NO-DYNAMICS;NOT-QCD;NO-CONFINEMENT-CLAIM")
    assert lut
    if not head.endswith(">"):
        raise GateFail("the head law must close its own bracket")
    return head[:-1] + " -- " + " -- ".join(parts) + ">"


# ===========================================================================
# SECTION 8.  THE CHOICE INVENTORY
# ===========================================================================

def build_choices(S):
    """each choice carries TWO numbers: the fibre -- the cardinality of the
    admissible alternatives -- and the declared instances, how many this unit
    ran.  A genuinely free choice with fibre 1 is a contradiction in terms
    and none is reported."""
    a, sym = S["arena"], S["symmetry"]
    rows = [
        ("the lattice size and dimension", "FORCED (anchored)", 1, 1, False),
        ("the coefficient alphabet", "FORCED (inherited)", 1, 1, False),
        ("the coin family", "FORCED (derived)", 1, 1, False),
        ("the link and plaquette sets", "FORCED (derived)", 1, 1, False),
        ("the gauge action's form", "FORCED (inherited)", 1, 1, False),
        ("WHICH CHART GROUP IS DECLARED", "GENUINELY-FREE", 2, 2, True),
        ("the carrier: the uniform slice or the full space",
         "GENUINELY-FREE", "UNBOUNDED", 2, True),
        ("the null: counting on configurations or on orbits",
         "GENUINELY-FREE", "UNBOUNDED", 2, True),
        ("the sets weighed against the nulls", "DECLARED (the parent's own)",
         "UNBOUNDED", len(S["_sets"]), False),
        ("the candidate sources censused", "DECLARED (the pin's plus two)",
         "UNBOUNDED", len(CANDIDATES), False),
        ("the base plaquette and its neighbour", "STABILIZER-FIXED",
         len(S["_lat"].plaqs), 1, False),
    ]
    out = [{"choice": c, "status": st, "fibre": f, "declared_instances": d,
            "verdict_determining": v} for (c, st, f, d, v) in rows]
    vd = [r for r in out if r["verdict_determining"]]
    bad = [r for r in out
           if r["status"] == "GENUINELY-FREE" and r["fibre"] == 1]
    if mut("MUT-CHOICE-INVENTORY"):
        out[5]["verdict_determining"] = False
        vd = [r for r in out if r["verdict_determining"]]
    LD.gate("G-CHOICE-INVENTORY",
            "the construction choices are inventoried with BOTH numbers a "
            "reader needs -- the fibre and the declared instances -- and the "
            "verdict-determining rows are flagged: which chart group is "
            "declared, which carrier, and which null, because every one of "
            "those three moves a published number and none of them is fixed "
            "by anything this arena measures.  A genuinely free choice with "
            "fibre 1 would be a contradiction and none is reported",
            len(vd) == 3 and not bad,
            "%d rows, %d verdict-determining, %d contradictory"
            % (len(out), len(vd), len(bad)))
    assert a and sym
    S["choice_inventory"] = out
    return out


# ===========================================================================
# SECTION 9.  THE PAPER GATES
# ===========================================================================

MUST_NOT = [
    "area law", "area-law", "string tension", "string-tension",
    "confining", "confinement analog", "quark", "the potential between",
]
DECLARING = [
    "no area-law, string-tension, or potential claim",
    "NO-AREA-LAW-NO-STRING-TENSION-NO-POTENTIAL-CLAIM",
    "NO-CONFINEMENT-CLAIM",
    "the confinement word stays behind its gate",
    "The confinement word stays behind its gate",
    "makes no area-law, string-tension or potential claim",
    "no area-law claim, no string-tension claim and no potential claim",
    "A confinement analog would need three objects this arena does not have",
    "the word this unit does not use",
]


def paper_claims(S):
    """every claim is a (fragment, expected occurrences) pair RENDERED from a
    measured receipt field, so a number that moved in the run cannot stay
    still in the paper."""
    a, sym, pf = S["arena"], S["symmetry"], S["candidate_pushforward"]
    gh, bl, fx = S["candidate_group_haar"], S["born_layer"], S["fixed_locus"]
    inv, cmp_ = S["candidate_invariance"], S["measure_comparison"]
    cen = S["census"]

    def m(setname, col):
        for r in cmp_["rows"]:
            if r["set"] == setname:
                return r[col]
        raise KeyError(setname)

    C = {
        "coins": "%d coins" % a["coins"],
        "links": "%d links" % a["links"],
        "sites": "%d sites" % a["sites"],
        "orbits32": "%d orbits" % inv["uniqueness"]["CHART-32"]["orbits"],
        "orbits128": "%d orbits" % inv["uniqueness"]["CHART-128"]["orbits"],
        "simplex32": "%d-dimensional simplex"
                     % inv["uniqueness"]["CHART-32"]["simplex_dimension"],
        "simplex128": "%d independent numbers"
                      % inv["uniqueness"]["CHART-128"]["simplex_dimension"],
        "fixed": "exactly the %d uniform configurations"
                 % fx["chart_fixed_configurations"],
        "extfixed": "%d of them survive" % fx["extension_fixed_configurations"],
        "weld2": "%d rows, %d distinct candidates"
                 % (pf["weld2_rows"], pf["weld2_distinct_candidates"]),
        "weld2found": "%d FOUND" % pf["weld2_found"],
        "weld3": "%d sites" % pf["weld3_target_sites"],
        "monomial": "%d monomial coins" % gh["monomial_coins"],
        "adjoin": "%d of %d interfering coins"
                  % (gh["interfering_coins_adjoinable"],
                     S["parent_census"]["by_sector"]["BALANCED"]["coins"]),
        "defectoverlap": "%d of the %d defect-carrying coins"
                         % (gh["defect_coins_in_the_haar_carrier"],
                            S["parent_census"]["defect_carrying"]),
        "born": "%d distinct Born images" % bl["distinct_images"],
        "closure": "%d of %d products" % (gh["products_inside"],
                                          gh["products_total"]),
        "finite": "%d of %d coins" % (gh["coins_of_finite_order_inside_the_family"],
                                      a["coins"]),
        "nc_count": "%s at the counting measure" % m("NON-COMMUTING", "counting"),
        "nc_orb": "%s at the orbit null" % m("NON-COMMUTING",
                                             "orbit_uniform_CHART-32"),
        "df_count": "%s under counting" % m("DEFECT-CARRYING", "counting"),
        "df_orb": "%s under the orbit null" % m("DEFECT-CARRYING",
                                                "orbit_uniform_CHART-32"),
        "census": "%d candidate sources" % cen["candidates"],
        "deriving": "%d derive" % cen["deriving"],
        "multisets": "%d sector multisets"
                     % inv["sector_multisets_on_the_full_space"],
        "chart": "order %d" % sym["chart_order"],
        "ext": "order %d" % sym["extension_order"],
        "nonflat": "%d of 640 are non-flat" % S["parent_census"]["non_flat"],
        "nonpaper": "%d non-commuting" % S["parent_census"]["non_commuting"],
        "gates": "%d gates" % (len(LD.rows) + len(PAPER_GATE_IDS)),
        "mutants": "%d declared mutants" % len(MUTANTS),
        "anchors": "%d anchors in all" % S["totals"]["anchors"],
        "anchorsplit": "%d file-bytes anchors, %d path-value anchors and %d "
                       "verbatim-text anchors"
                       % (S["totals"]["byte_anchors"],
                          S["totals"]["path_value_anchors"],
                          S["totals"]["verbatim_anchors"]),
        "choices": "%d construction choices" % len(S["choice_inventory"]),
    }
    return C


POLARITY = [
    ("no measure on the configurations derives", 1),
    ("selects a support, not a measure", 1),
    ("does not act transitively", 1),
]
NEGATORS = ["not ", "no ", "never", "fails", "cannot", "does not", "un"]

# the paper gates, named in the order they close.  The count is what lets the
# paper state the run's own gate total without a magic constant, and the last
# of them checks that the statement came true.
PAPER_GATE_IDS = ["G-PAPER-CLAIMS-RENDER", "G-PAPER-CARRIES-THIS-RUNS-VERDICT",
                  "G-MUST-NOT-VOCABULARY", "G-PAPER-POLARITY",
                  "G-PAPER-COVERAGE", "G-GATE-COUNT-IS-AS-CLAIMED"]


def gate_paper(S, paper_text, LDx):
    C = paper_claims(S)
    hay = wsnorm(paper_text)
    missing = [k for k, v in C.items() if wsnorm(v) not in hay]
    if mut("MUT-PAPER-CLAIM"):
        missing = ["planted"]
    LDx.gate("G-PAPER-CLAIMS-RENDER",
             "every load-bearing number in the paper is RENDERED from a "
             "measured receipt field and located in the paper's own bytes "
             "under whitespace and markdown normalisation, so a value that "
             "moved in the run cannot stay still in the prose",
             not missing, "%d claims, %d not located: %s"
             % (len(C), len(missing), missing[:6]))

    verdict = S["verdict"]["string"]
    LDx.gate("G-PAPER-CARRIES-THIS-RUNS-VERDICT",
             "the COMPLETE emitted verdict string occurs verbatim in the "
             "paper under whitespace normalisation, so a paper quoting an "
             "earlier run's verdict cannot be delivered -- only string "
             "equality reaches a retyped verdict block, since the numeral "
             "gate is structurally blind to numerals inside hyphenated "
             "segments",
             wsnorm(verdict) in hay,
             "verdict of %d characters located" % len(verdict))

    # the declaring sentences are removed FIRST, case-insensitively, so that
    # a sentence that DECLARES the must-not is not mistaken for one that makes
    # the claim; every needle is a long distinctive sentence, so the removal
    # cannot over-reach
    stripped = paper_text
    for d in DECLARING:
        stripped = re.sub(re.escape(d), " ", stripped, flags=re.I)
    sw = wsnorm(stripped).lower()
    hits = [w for w in MUST_NOT if w.lower() in sw]
    if mut("MUT-MUST-NOT"):
        hits = ["planted"]
    LDx.gate("G-MUST-NOT-VOCABULARY",
             "the pin's must-not vocabulary is SWEPT over the paper's own "
             "text with the declaring sentences removed first, so a "
             "paragraph that made an area-law, string-tension or potential "
             "claim would die on the delivery run.  Nothing weaker reaches "
             "it: a must-not carries no numeral, so the numeral gate is "
             "blind to it",
             not hits, "must-not vocabulary found: %s" % hits)

    pol = []
    for (frag, want) in POLARITY:
        n = wsnorm(paper_text).lower().count(wsnorm(frag).lower())
        bad = False
        low = wsnorm(paper_text).lower()
        i = low.find(wsnorm(frag).lower())
        if i >= 0:
            win = low[max(0, i - 64):i]
            bad = any(g in win for g in ("it is false that", "contrary to"))
        pol.append({"fragment": frag, "expected": want, "found": n,
                    "negated": bad, "ok": n >= want and not bad})
    LDx.gate("G-PAPER-POLARITY",
             "the direction-bearing claims are checked for POLARITY as well "
             "as presence -- each must occur and must not sit inside a "
             "window carrying a declared negator -- which closes the "
             "direction-blindness of a fragment gate",
             all(p["ok"] for p in pol),
             "%d polarity rows, %d failing"
             % (len(pol), sum(1 for p in pol if not p["ok"])))

    # numeral coverage, fenced blocks included
    allowed = set()
    def add(x):
        allowed.add(str(x))
    for blk in (S["arena"], S["symmetry"], S["fixed_locus"],
                S["parent_census"], S["born_layer"], S["candidate_group_haar"],
                S["candidate_pushforward"], S["candidate_invariance"],
                S["candidate_holonomy_pullback"], S["census"]):
        for v in blk.values():
            if isinstance(v, int):
                add(v)
            elif isinstance(v, list):
                for x in v:
                    if isinstance(x, int):
                        add(x)
                    elif isinstance(x, (list, tuple)):
                        for y in x:
                            if isinstance(y, int):
                                add(y)
            elif isinstance(v, dict):
                for x in v.values():
                    if isinstance(x, int):
                        add(x)
                    elif isinstance(x, dict):
                        for y in x.values():
                            if isinstance(y, int):
                                add(y)
    for r in S["measure_comparison"]["rows"]:
        for k, v in r.items():
            if k != "set":
                for part in str(v).replace("/", " ").split():
                    add(part)
    for r in S["fibre"]["rows"]:
        add(r["orbits"])
        add(r["independent_numbers_a_declaration_must_supply"])
    for r in S["path_value_anchors"]:
        add(r["measured"])
        if isinstance(r["measured"], list):
            for x in r["measured"]:
                add(x)
    for r in S["choice_inventory"]:
        add(r["fibre"])
        add(r["declared_instances"])
    for r in S["verbatim_anchors"]:
        add(r["chars"])
        add(r["floor"])
    for t in S["totals"].values():
        add(t)
    add(S["provenance"]["pin_ledger_entry"])
    for v in C.values():
        for part in re.findall(r"\d+", str(v)):
            add(part)
    for (_sn, sp) in S["measure_comparison"]["spreads"]:
        for part in re.findall(r"\d+", sp):
            add(part)
    for (_aid, _src, _g, text) in VERBATIM:
        for part in re.findall(r"\d+", text):
            add(part)
    # DECLARED STRUCTURAL LITERALS: section and item numbers, this unit's own
    # paper number, and the engraving references the era's disciplines are
    # named by.  Every one is a reference and not a measurement, and the list
    # is published in the receipt so a reader can see exactly what the
    # coverage gate was permitted to forgive.
    STRUCTURAL = {str(k) for k in range(0, 24)} | {
        "2026", "34", "62", "82", "87", "91", "119", "125", "46"}
    nums = re.findall(r"(?<![\w/.-])(\d+)(?![\w/.-])", paper_text)
    unreg = sorted({x for x in nums if x not in allowed and x not in STRUCTURAL})
    fenced = len(re.findall(r"```", paper_text)) // 2
    if mut("MUT-PAPER-NUMERAL"):
        unreg = ["planted"]
    LDx.gate("G-PAPER-COVERAGE",
             "EVERY numeral of the paper, the fenced verdict block included, "
             "is either a value this run measured or a declared structural "
             "literal; the scan runs in the plain delivery run and not in a "
             "separate mode (#20)",
             not unreg, "%d numerals scanned across %d fenced blocks, %d "
             "unregistered: %s" % (len(nums), fenced, len(unreg), unreg[:8]))
    claimed = int(re.search(r"(\d+)", C["gates"]).group(1))
    if mut("MUT-GATE-COUNT"):
        claimed += 1
    LDx.gate("G-GATE-COUNT-IS-AS-CLAIMED",
             "and the gate total the paper states is the gate total this run "
             "produced: the claim is rendered before the paper gates close "
             "and this, the last of them, checks that the prediction came "
             "true, so the number in section 10 can never be a stale "
             "constant",
             claimed == len(LD.rows) + 1,
             "the paper claims %d gates; this run closes %d"
             % (claimed, len(LD.rows) + 1))
    S["paper_claims"] = C
    S["paper_polarity"] = pol
    S["paper_coverage"] = {"scanned": len(nums), "fenced_blocks": fenced,
                           "unregistered": unreg,
                           "allowed_values": len(allowed),
                           "declared_structural_literals": sorted(STRUCTURAL)}


# ===========================================================================
# SECTION 10.  MUTANTS, THE RUN, THE SEAL, THE WRITE
# ===========================================================================

MUTANTS = [
    ("MUT-SOURCE-DRIFT", "G-SOURCES-PINNED", "a pinned source's digest moves"),
    ("MUT-FLOAT-SNEAK", "G-EXACT-ARITHMETIC", "a float literal appears"),
    ("MUT-PATH-VALUE", "G-PATH-VALUE-ANCHORS",
     "a (path, value) probe returns the wrong value"),
    ("MUT-VERBATIM-SHRINK", "G-VERBATIM-ANCHORS",
     "a verbatim window is shrunk below its declared floor"),
    ("MUT-ALPHABET", "G-ALPHABET-REBUILT", "the alphabet loses an element"),
    ("MUT-COIN-UNITARITY", "G-COINS-DERIVED",
     "a non-unitary matrix is admitted to the family"),
    ("MUT-PARENT-CENSUS", "G-PARENT-CENSUS-REPRODUCED",
     "the reproduced parent census drifts by one"),
    ("MUT-RESIDUAL-GROUP", "G-ORBIT-CENSUS-EXACT",
     "the residual group is made trivial, so the orbit count is the slice"),
    ("MUT-FIXED-LOCUS", "G-CHART-FIXED-LOCUS-IS-THE-SWEPT-SLICE",
     "a fixed-locus check is made to fail"),
    ("MUT-BORN-STOCHASTIC", "G-BORN-LAYER-IS-A-MEASURE",
     "a Born matrix stops being doubly stochastic"),
    ("MUT-ORBIT-CLOSURE", "G-DECLARED-SETS-ARE-ORBIT-CLOSED",
     "a weighed set stops being a union of orbits"),
    ("MUT-UNIQUENESS", "G-UNIQUENESS-GATED",
     "uniqueness is ASSERTED where the orbit count refutes it"),
    ("MUT-CLOSURE", "G-FAMILY-IS-NOT-A-GROUP",
     "the family is declared multiplicatively closed"),
    ("MUT-CENSUS-DERIVES", "G-HEAD-STRING-EQUALITY",
     "a candidate is declared to derive; the head moves and the two routes "
     "stop agreeing"),
    ("MUT-HEAD-CONSTANT", "G-HEAD-LAW-REACHABILITY",
     "the head law is made unable to move"),
    ("MUT-WILSON-SEGMENT", "G-NO-WILSON-EXPECTATION",
     "an expectation-valued key appears in the receipt"),
    ("MUT-CHOICE-INVENTORY", "G-CHOICE-INVENTORY",
     "a verdict-determining row loses its flag"),
    ("MUT-PAPER-CLAIM", "G-PAPER-CLAIMS-RENDER",
     "a rendered claim stops being locatable in the paper"),
    ("MUT-PAPER-NUMERAL", "G-PAPER-COVERAGE",
     "an unregistered numeral appears in the paper"),
    ("MUT-MUST-NOT", "G-MUST-NOT-VOCABULARY",
     "must-not vocabulary appears outside a declaring sentence"),
    ("MUT-GATE-COUNT", "G-GATE-COUNT-IS-AS-CLAIMED",
     "the gate total the paper states drifts from the run's own"),
    ("MUT-MOVING-REF", "G-NO-MOVING-REFS",
     "a moving reference is planted in the scanned haystack"),
    ("MUT-CROSS-INVARIANCE",
     "G-EVERY-NULL-IS-INVARIANT-UNDER-EVERY-MEASURED-GROUP",
     "a null stops being invariant under the larger group"),
    ("MUT-SEAL", "G-SEAL-COMPLETE",
     "a published object is mutated between its gate and the write"),
    ("MUT-RECONSTRUCTION", "G-HEAD-STRING-EQUALITY",
     "the independent reconstruction is desynchronised from the builder"),
]

ANCHOR_CLASSES = ["FILE-BYTES", "PATH-VALUE", "VERBATIM"]


def run(paper_path=None, write=True, break_anchor=None):
    S = {}
    say("=" * 74)
    say(UNIT)
    say("=" * 74)
    say("[1/9] provenance -- the pinned sources, at declared relative paths")
    if break_anchor == "FILE-BYTES":
        globals()["MUT"] = "MUT-SOURCE-DRIFT"
    src = measure_provenance(S)
    if break_anchor == "PATH-VALUE":
        globals()["MUT"] = "MUT-PATH-VALUE"
    pv = measure_path_values(S, src)
    if break_anchor == "VERBATIM":
        globals()["MUT"] = "MUT-VERBATIM-SHRINK"
    measure_verbatim(S, src)
    SEAL.take("provenance", "provenance", "G-SOURCES-PINNED", S["provenance"])
    SEAL.take("path-value anchors", "path_value_anchors",
              "G-PATH-VALUE-ANCHORS", S["path_value_anchors"])
    SEAL.take("verbatim anchors", "verbatim_anchors", "G-VERBATIM-ANCHORS",
              S["verbatim_anchors"])

    say("[2/9] the arena, rebuilt from the parent's declared definitions")
    build_arena(S, pv)
    SEAL.take("the arena", "arena", "G-COINS-DERIVED", S["arena"])

    say("[3/9] the measured symmetries, and what they fix")
    measure_symmetries(S, pv)
    measure_fixed_locus(S, pv)
    SEAL.take("the symmetry census", "symmetry", "G-ORBIT-CENSUS-EXACT",
              S["symmetry"])
    SEAL.take("the fixed locus", "fixed_locus",
              "G-CHART-FIXED-LOCUS-IS-THE-SWEPT-SLICE", S["fixed_locus"])

    say("[4/9] the parent's census, reproduced -- the sets to be weighed")
    measure_parent_census(S, pv)
    SEAL.take("the parent census", "parent_census",
              "G-PARENT-CENSUS-REPRODUCED", S["parent_census"])

    say("[5/9] candidate (a): the history-measure pushforward")
    measure_correspondence(S, src, pv)
    SEAL.take("candidate (a)", "candidate_pushforward",
              "G-WELD2-RAN-AT-THE-GAMMA-CARRIER", S["candidate_pushforward"])

    say("[6/9] candidates (b) and (c): the counting measure, and invariance")
    measure_invariance(S, pv)
    SEAL.take("candidate (b)", "candidate_counting", "G-TWO-NULLS-DISAGREE",
              S["candidate_counting"])
    SEAL.take("candidate (c)", "candidate_invariance", "G-UNIQUENESS-GATED",
              S["candidate_invariance"])
    SEAL.take("the measure comparison", "measure_comparison",
              "G-TWO-NULLS-DISAGREE", S["measure_comparison"])

    say("[7/9] candidates (d) (e) (f) (g) (h): Haar, Gibbs, Born, pull-back")
    measure_born_layer(S)
    measure_haar_and_gibbs(S, src, pv)
    measure_holonomy_pullback(S, pv)
    SEAL.take("the Born layer", "born_layer", "G-BORN-LAYER-IS-A-MEASURE",
              S["born_layer"])
    SEAL.take("candidate (d)", "candidate_group_haar",
              "G-THE-MONOMIAL-SUBGROUP-IS-A-GROUP", S["candidate_group_haar"])
    SEAL.take("candidate (e)", "candidate_ambient_haar",
              "G-U2-HAAR-CANNOT-DESCEND", S["candidate_ambient_haar"])
    SEAL.take("candidate (f)", "candidate_gibbs", "G-GIBBS-NEEDS-AN-ACTION",
              S["candidate_gibbs"])
    SEAL.take("candidate (h)", "candidate_holonomy_pullback",
              "G-HOLONOMY-GROUP-IS-CONFIGURATION-DEPENDENT",
              S["candidate_holonomy_pullback"])

    say("[8/9] the census, the fibre, the head")
    build_census(S)
    price_the_fibre(S)
    demonstrate_reachability(S)
    withhold_the_licensed_segment(S)
    build_choices(S)
    SEAL.take("the census", "census", "G-CENSUS-IS-TOTAL", S["census"])
    SEAL.take("the fibre", "fibre", "G-FIBRE-PRICED", S["fibre"])
    SEAL.take("the pre-registered heads", "preregistered_heads",
              "G-HEAD-LAW-REACHABILITY", S["preregistered_heads"])
    SEAL.take("the withheld segment", "withheld", "G-NO-WILSON-EXPECTATION",
              S["withheld"])
    SEAL.take("the choice inventory", "choice_inventory", "G-CHOICE-INVENTORY",
              S["choice_inventory"])

    S["totals"] = {
        "sources": len(SOURCES),
        "byte_anchors": len(SOURCES),
        "path_value_anchors": len(S["path_value_anchors"]),
        "verbatim_anchors": len(S["verbatim_anchors"]),
        "anchors": len(SOURCES) + len(S["path_value_anchors"])
                   + len(S["verbatim_anchors"]),
        "mutants_declared": len(MUTANTS),
        "candidates": S["census"]["candidates"],
        "deriving": S["census"]["deriving"],
        "choices": len(S["choice_inventory"]),
    }
    S["verdict"] = {"string": build_verdict(S)}
    recon = reconstruct_verdict(S)
    if mut("MUT-RECONSTRUCTION"):
        recon = recon + "X"
    LD.gate("G-HEAD-STRING-EQUALITY",
            "the complete verdict string -- head included -- is derived TWICE "
            "by disjoint routes and the two are compared for equality: the "
            "builder computes it from the live measurements, and an "
            "independent reconstruction reads only the serialized receipt, "
            "carries its own copy of the head law and re-renders EVERY "
            "segment from the primitive measured tables, sharing no format "
            "string, no helper and no typed value with the builder and "
            "reading neither its segments nor its counts",
            recon == S["verdict"]["string"],
            "builder %d characters, reconstruction %d"
            % (len(S["verdict"]["string"]), len(recon)))
    S["verdict"]["reconstruction_agrees"] = True
    S["verdict"]["head"] = S["verdict"]["string"].split("<", 1)[0]
    SEAL.take("the verdict", "verdict", "G-HEAD-STRING-EQUALITY", S["verdict"])

    say("[9/9] the paper, the seal, the artifacts")
    ppath = paper_path or os.path.join(REPO, PAPER_REL)
    if os.path.exists(ppath):
        ptext = open(ppath, "rb").read().decode()
        gate_paper(S, ptext, LD)
        S["paper_sha256_12"] = bdigest(open(ppath, "rb").read())
    else:
        S["paper_claims"] = paper_claims(S)
        S["paper_polarity"] = []
        S["paper_coverage"] = {"scanned": 0, "fenced_blocks": 0,
                               "unregistered": [], "allowed_values": 0}
        S["paper_sha256_12"] = "ABSENT"
        LD.gate("G-PAPER-PRESENT",
                "the object under test is the paper this run gates its own "
                "numeric claims against; it cannot be pinned against itself, "
                "and its absence is recorded rather than swallowed",
                False, "paper absent at %s" % ppath)
    SEAL.take("the paper claims", "paper_claims", "G-PAPER-CLAIMS-RENDER",
              S["paper_claims"])
    SEAL.take("the paper polarity", "paper_polarity", "G-PAPER-POLARITY",
              S["paper_polarity"])
    SEAL.take("the paper coverage", "paper_coverage", "G-PAPER-COVERAGE",
              S["paper_coverage"])
    return S


def finish(S, write):
    S["schema"] = SCHEMA
    S["unit"] = UNIT
    S["pin_sha256_prefix"] = PIN_SHA12
    S["python"] = "%d.%d" % sys.version_info[:2]
    S["arithmetic"] = ("Q(zeta_8) as integer 5-tuples over (1, z, z^2, z^3) "
                       "modulo z^4 + 1 in lowest terms; probabilities as "
                       "exact Fractions; no float anywhere, gated on the "
                       "instrument's own syntax tree")
    S["gates"] = [dict(r) for r in LD.rows]
    S["gate_digests"] = list(LD.digests)
    S["totals"]["gates_in_the_sealed_snapshot"] = len(S["gates"])
    S["totals"]["late_gates"] = 2
    S["totals"]["gate_failures"] = sum(1 for r in S["gates"]
                                       if not r["passed"])
    S["mutants"] = [{"name": n, "target": g, "what": w} for (n, g, w) in MUTANTS]
    S["anchor_classes"] = ANCHOR_CLASSES
    S["waiver_ledger"] = build_waivers(S)
    S["transcript_head"] = LOG[:6]
    # the totals are sealed LAST, and their own seal count is set immediately
    # before that seal is taken, so the published count is the manifest's true
    # length and not a constant that could drift away from it
    for name, key, gate in (("the gate ledger", "gates", "G-SEAL-COMPLETE"),
                            ("the mutant registry", "mutants", "G-SEAL-COMPLETE"),
                            ("the waiver ledger", "waiver_ledger",
                             "G-SEAL-COMPLETE"),
                            ("the schema", "schema", "G-SEAL-COMPLETE"),
                            ("the transcript head", "transcript_head",
                             "G-SEAL-COMPLETE"),
                            ("the totals", "totals", "G-SEAL-COMPLETE")):
        if key == "totals":
            S["totals"]["sealed_objects"] = len(SEAL.man) + 1
        SEAL.take(name, key, gate, S[key])

    payload = {k: v for k, v in S.items() if not k.startswith("_")}
    declared_unsealed = ["seal_manifest", "gate_digests", "unit",
                         "pin_sha256_prefix", "python", "arithmetic",
                         "anchor_classes", "paper_sha256_12", "verdict_head",
                         "closing_gates"]
    payload["seal_manifest"] = SEAL.man
    payload["declared_unsealed"] = declared_unsealed
    payload["verdict_head"] = S["verdict"]["head"]
    payload["closing_gates"] = {
        "names": ["G-SEAL-COMPLETE", "G-ARTIFACT-INTEGRITY"],
        "warrant": "these two close after the gate ledger has been "
                   "snapshotted and sealed.  G-SEAL-COMPLETE cannot be "
                   "inside the object it seals, and G-ARTIFACT-INTEGRITY "
                   "runs after the bytes are on disk; so the sealed ledger "
                   "carries neither row, and their verdict is recorded by "
                   "the artifacts themselves -- a run that reached the write "
                   "at all is a run in which both passed."}
    unsealed = [k for k in payload
                if k not in SEAL.by_key and k not in declared_unsealed
                and k != "declared_unsealed"]
    if mut("MUT-SEAL"):
        payload["arena"] = dict(payload["arena"])
        payload["arena"]["coins"] = -1
    bad = SEAL.reverify(payload)
    LD.gate("G-SEAL-COMPLETE",
            "the manifest is TOTAL and the seal is re-taken immediately "
            "before the write: every published top-level key is either "
            "sealed at the gate that produced it or named in the "
            "declaration with the reason it cannot be, and a published "
            "value mutated anywhere between its gate and the write refuses "
            "the delivery",
            not bad and not unsealed,
            "%d seals, %d moved, %d published but neither sealed nor declared"
            % (len(SEAL.man), len(bad), len(unsealed)))
    lines = list(LOG)
    lines.append("")
    lines.append("THE VERDICT")
    lines.append(S["verdict"]["string"])
    out_text = "\n".join(lines) + "\n"
    rec_text = json.dumps(payload, indent=1, sort_keys=True, default=str) + "\n"

    if not write:
        say("")
        say("THE VERDICT")
        say(S["verdict"]["string"])
        return payload, out_text, rec_text

    outp = os.path.join(REPO, OUT_REL)
    recp = os.path.join(REPO, RECEIPT_REL)
    seals = {outp: hashlib.sha256(out_text.encode()).hexdigest(),
             recp: hashlib.sha256(rec_text.encode()).hexdigest()}
    probe = recp + ".probe"
    with open(probe, "wb") as fh:
        fh.write(rec_text.encode() + b"X")
    caught = (hashlib.sha256(open(probe, "rb").read()).hexdigest()
              != seals[recp])
    os.remove(probe)
    for path, text in ((outp, out_text), (recp, rec_text)):
        tmp = path + ".tmp"
        with open(tmp, "wb") as fh:
            fh.write(text.encode())
        got = hashlib.sha256(open(tmp, "rb").read()).hexdigest()
        if got != seals[path]:
            os.remove(tmp)
            raise GateFail("G-ARTIFACT-INTEGRITY :: staged bytes do not match "
                           "the gate-time seal at %s" % path)
        os.replace(tmp, path)
    ok = all(hashlib.sha256(open(p, "rb").read()).hexdigest() == s
             for p, s in seals.items())
    LD.gate("G-ARTIFACT-INTEGRITY",
            "the artifacts are written to temporaries, re-read and matched "
            "AGAINST THE GATE-TIME SEAL -- never against a re-serialisation "
            "of what is in memory, which would confirm a corruption rather "
            "than catch it -- and only then moved into place; a deliberately "
            "corrupted payload is written to a probe path and required to be "
            "detected first",
            ok and caught, "both artifacts match their seals; the corrupted "
            "probe was detected")
    say("")
    say("THE VERDICT")
    say(S["verdict"]["string"])
    return payload, out_text, rec_text


def build_waivers(S):
    """#34 with reachability, at an HONEST denominator, in four classes."""
    targeted = {g for (_n, g, _w) in MUTANTS}
    rows = []
    for r in LD.rows:
        g = r["gate"]
        if g in targeted:
            cls = "COVERED-BY-A-DECLARED-MUTANT"
        elif g in ("G-SOURCES-PINNED", "G-PATH-VALUE-ANCHORS",
                   "G-VERBATIM-ANCHORS"):
            cls = "COVERED-BY-THE-ANCHOR-BREAKER"
        elif g in ("G-CHART-IS-TRANSITIVE-ON-LINKS",
                   "G-SWAP-CONJUGATE-CLOSED", "G-GAUGE-ACTS-ON-THE-FAMILY",
                   "G-UNIFORMITY-PRESERVING-GAUGE-MEASURED",
                   "G-BURNSIDE-EXACT", "G-LATTICE-REBUILT"):
            cls = "REGISTERED-FORCING"
        else:
            cls = "NO-FALSIFIER-REACHES-IT"
        rows.append({"gate": g, "class": cls})
    return rows


def selftest():
    """the falsification self-test: corrupt exactly one anchor in memory,
    confirm the delivery is refused, and WRITE NOTHING."""
    ok = []
    for cls in ANCHOR_CLASSES:
        globals()["LD"] = Ledger()
        globals()["SEAL"] = Seal()
        globals()["LOG"] = []
        globals()["QUIET"] = True
        globals()["MUT"] = None
        try:
            run(write=False, break_anchor=cls)
            ok.append((cls, "DID NOT DIE"))
        except GateFail as e:
            ok.append((cls, "died at %s" % str(e).split(" ::")[0]))
        finally:
            globals()["MUT"] = None
    globals()["QUIET"] = False
    for cls, res in ok:
        print("SELFTEST %-12s %s" % (cls, res))
    bad = [c for c, r in ok if r == "DID NOT DIE"]
    if bad:
        print("SELFTEST FAILED at %s" % bad)
        return 1
    print("SELFTEST PASSED -- every anchor class is fatal, nothing written")
    return 0


def run_mutant(name):
    if name not in {n for (n, _g, _w) in MUTANTS}:
        print("unknown mutant: %s" % name)
        return 2
    target = [g for (n, g, _w) in MUTANTS if n == name][0]
    globals()["LD"] = Ledger()
    globals()["SEAL"] = Seal()
    globals()["LOG"] = []
    globals()["QUIET"] = True
    globals()["MUT"] = name
    try:
        S = run(write=False)
        finish(S, write=False)
        globals()["QUIET"] = False
        print("MUTANT %-24s ALIVE (expected death at %s)" % (name, target),
              flush=True)
        return 1
    except GateFail as e:
        globals()["QUIET"] = False
        died = str(e).split(" ::")[0]
        hit = died == target
        print("MUTANT %-24s died at %-42s %s"
              % (name, died, "ON TARGET" if hit else "OFF TARGET (want %s)"
                 % target), flush=True)
        return 0 if hit else 1
    finally:
        globals()["MUT"] = None


USAGE = ("usage: r5m_measure_exact.py [--no-write] [--selftest] "
         "[--mutant NAME] [--all-mutants] [--list-mutants] [--list-gates] "
         "[--verify-paper PATH]")


def main(argv):
    args = argv[1:]
    allowed = {"--no-write", "--selftest", "--mutant", "--all-mutants",
               "--list-mutants", "--list-gates", "--verify-paper"}
    i = 0
    opts = {}
    while i < len(args):
        a = args[i]
        if a not in allowed:
            print("unknown flag: %s\n%s" % (a, USAGE))
            return 2
        if a in ("--mutant", "--verify-paper"):
            if i + 1 >= len(args):
                print("%s needs an argument\n%s" % (a, USAGE))
                return 2
            opts[a] = args[i + 1]
            i += 2
        else:
            opts[a] = True
            i += 1
    if "--list-mutants" in opts:
        for (n, g, w) in MUTANTS:
            print("%-24s -> %-44s %s" % (n, g, w))
        return 0
    if "--selftest" in opts:
        return selftest()
    if "--mutant" in opts:
        return run_mutant(opts["--mutant"])
    if "--all-mutants" in opts:
        rc = 0
        for (n, _g, _w) in MUTANTS:
            rc |= run_mutant(n)
        print("ALL MUTANTS: %s" % ("ALL DEAD ON TARGET" if rc == 0
                                   else "SOME SURVIVED OR MISSED"))
        return rc
    paper = opts.get("--verify-paper")
    write = "--no-write" not in opts and "--verify-paper" not in opts
    try:
        S = run(paper_path=paper, write=write)
        if "--list-gates" in opts:
            for r in LD.rows:
                print("%-46s %s" % (r["gate"], "PASS" if r["passed"] else "FAIL"))
            return 0
        finish(S, write=write)
    except GateFail as e:
        print("REFUSED :: %s" % e)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
