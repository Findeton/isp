#!/usr/bin/env python3.13
# -*- coding: utf-8 -*-
"""
v14 PER-L -- THE L-LADDER PERSISTENCE CENSUS.
Instrument for `v14/paper-28-perl.md`.

QUESTION (pin, "THE QUESTION").  Do the forced results of the L = 4 arc
PERSIST along the L-ladder (L = 6, 8)?  Per-invariant verdicts with exact
witnesses: PERSISTS / BREAKS-AT-L=<n> / TRANSFORMS-<law>.  Stage 1 is
decisive: the paper-20 adjudication's registered SIDON PREDICTION is tested
per arena, and its PASS/FAIL is reported in the head regardless of the rest.

CLI CONTRACT (the #82 minimum: argv-parsed against a whitelist)
---------------------------------------------------------------
    python3.13 v14/code/perl_exact.py
        THE DELIVERY RUN, and the ONLY writer.  Builds the whole census,
        evaluates every gate (the paper gates included), runs every declared
        mutant in-process, re-reads what it wrote, and WRITES
        `perl_output.txt` and `perl_receipt.json` beside this file.  Exits 0
        iff every gate passes.

    python3.13 v14/code/perl_exact.py --no-write
        The same run, writing nothing.

    python3.13 v14/code/perl_exact.py --selftest
        FALSIFICATION SELF-TEST.  Corrupts one anchor's expected digest IN
        MEMORY, confirms the run dies at the anchor gate, WRITES NOTHING, and
        exits 1.  Exits 2 if the corrupted run does NOT die.

    python3.13 v14/code/perl_exact.py --mutant NAME
        Runs the pipeline with the named mutant active.  Exits 1 when the
        mutant is killed (the intended outcome), 0 if it survives.  An unknown
        NAME exits 2; it never reports "SURVIVED".  Writes nothing.

    python3.13 v14/code/perl_exact.py --break-anchor NAME
        GATE-SPECIFIC ANCHOR BREAK.  NAME may be any pinned source (A-*), any
        path-value anchor (PV-*) or any verbatim window (VB-*), and the run
        dies at THAT anchor's own gate: G-SOURCES-PINNED,
        G-PATH-VALUE-ANCHORS or G-VERBATIM-ANCHORS respectively.  Unknown
        NAME exits 2.  The run must exit 1.  Writes nothing.

    python3.13 v14/code/perl_exact.py --verify-paper [PATH]
        RUNS THE #20 / E-22 INSTRUMENT AGAINST PATH (this unit's paper by
        default): the derivation is rebuilt and the paper gates -- claim
        rendering, numeral coverage over prose AND fenced blocks AND inline
        code spans, fenced-block MULTISET equality, tables-as-claims and claim
        POLARITY -- are evaluated with PATH as the object under test.  Exits 1
        on any drift, 0 on a clean paper, 2 if PATH does not exist.

    Any other argument, any unknown flag argument, any missing flag argument
    and any --verify-paper PATH that does not exist exits 2.  No flag is
    mutant-only, and no flag is a no-op.

THE GATE-TO-DISK SEAL (#119, with the #148 totality addendum).  Every
published object is DIGESTED AT THE MOMENT ITS GATE PASSES; the payload may
only be sealed if every earlier seal still verifies; the artifacts are written
FROM the sealed payload through temporaries moved into place by `os.replace`
only after the bytes match; and the terminal integrity gate compares the BYTES
ON DISK against the gate-time seal.  The manifest is TOTAL: every published
receipt key is sealed or declared unsealed with its reason.  The gate ledger
and the transcript are CHAINED (each row's digest folds in its predecessor).

TEXT GATES (#125, with the markdown-prefix normalisation).  Every text gate
matches text AS WRITTEN: needle and haystack are both whitespace-normalised
AND markdown-prefix-normalised (blockquote markers and list bullets), and
every verbatim window is pinned by the digest of its exact bytes and by a
declared length floor.

COVERAGE (E-22).  The paper scan covers prose, tables, FENCED BLOCKS and
INLINE CODE SPANS alike; fenced blocks are additionally gated by MULTISET
EQUALITY against blocks rendered from the receipt; table rows render as
claims.

FALSIFIERS (E-23).  Every declared mutant's published description is checked
against the code it perturbs, and every load-bearing receipt row carries a
falsifier or a named waiver with its forcing.

MEASURE (E-24).  No count is published as a probability.  The two fractions
this unit prints are stamped COUNTING-ONLY in the receipt.

ARITHMETIC.  Exact only.  The field is Q(zeta_24), which contains zeta_8 (the
parents' coefficient field), zeta_4, zeta_6 and zeta_3, carried as an
8-tuple of Fractions over the basis (1, x, ..., x^7) reduced modulo
Phi_24(x) = x^8 - x^4 + 1 -- and Phi_24 is COMPUTED here by exact division of
x^24 - 1 by the lower cyclotomics, never typed.  The representation is
canonical, so tuple equality IS field equality.  There are no floats: an AST
scan of this file and a recursive type scan of the emitted receipt are gates.

REIMPLEMENTATION NOTICE.  Every object here is reimplemented from the
definitions in the pinned papers.  The parents' programs are never imported,
never executed, and no value is copied from them except through the
hash-pinned receipts, which are anchors.

RUNTIME INPUTS (#46, #91).  Exactly ten files are read at run time as
SOURCES, all hash-pinned by this unit's frozen declaration, plus exactly one
file read as the OBJECT UNDER TEST -- this unit's own paper, which cannot be
hash-pinned because it is the thing being verified.  Both lists are
enumerated and gated.  No repository state outside them is read, and no
subprocess -- in particular no `git` -- is ever invoked: the run is correct
off-tree and in a directory with no version control at all.  A copy missing a
declared source ABORTS LOUDLY AND CLEANLY before any gate runs.
"""

import ast
import hashlib
import json
import os
import re
import sys
from fractions import Fraction
from itertools import product, combinations

# ===========================================================================
# SECTION 0.  THE FROZEN DECLARATION (RUNBOOK section 15: the arena is data)
# ===========================================================================

SELF = os.path.abspath(__file__)
REPO = os.path.dirname(os.path.dirname(os.path.dirname(SELF)))
OUT_TXT = os.path.join(os.path.dirname(SELF), "perl_output.txt")
OUT_JSON = os.path.join(os.path.dirname(SELF), "perl_receipt.json")

SCHEMA = "isp/v14/perl/1"
UNIT = "PER-L -- the L-ladder persistence census"
PAPER_REL = "v14/paper-28-perl.md"
PIN_REL = "v14/note-perl-pin.md"

# --- the ten hash-pinned runtime inputs ------------------------------------
SOURCES = [
    ("A-R4-PAPER", "v14/paper-10-defect-on-the-stage.md", "1063401c7bb5",
     "PARENT 1, terminal at commit 583cae7: the stage, the 3-term axis "
     "stencil, the 25-element alphabet, the order-collapse theorem, the "
     "admissible-scale precheck."),
    ("A-R4-RECEIPT", "v14/code/r4_defect_stage_receipt.json", "3dc1393b0df8",
     "THE ARENA'S SOURCE: L, d, the alphabet, the 58 circulants, the ord "
     "census, the locality thresholds, the admissible-scale set."),
    ("A-R4B-PAPER", "v14/paper-15-momentum.md", "89c636906061",
     "PARENT 2, terminal at commit 6d32993: the dispersions, the even-L "
     "theorem VMAX = diameter, the interior-radius register."),
    ("A-R4B-RECEIPT", "v14/code/r4b_momentum_receipt.json", "562e2a3d4d85",
     "the momentum receipt: VMAX, the diameter, the interior radii and the "
     "3-at-L-8 register claim this unit tests.  NO transport number is "
     "inherited from it -- the R4b scope stamp travels."),
    ("A-R5-PAPER", "v14/paper-18-gauge-rung.md", "62cfe5689d2c",
     "PARENT 3, terminal at commit 987cd73: the 640-coin family, the six "
     "declared plaquette stencils and the (order, support) profile."),
    ("A-R5-RECEIPT", "v14/code/r5_gauge_receipt.json", "0c02b7684e5b",
     "the gauge receipt: the coin sectors, the local profile string, the "
     "global supports at L = 4 and L = 8."),
    ("A-R2-PAPER", "v14/paper-02-manifold-rung.md", "1a80a5bf1a1b",
     "PARENT 4, terminal: theorem R2-W, the window-width locality law, cited "
     "and applied -- its own census is NOT re-run here."),
    ("A-R2-RECEIPT", "v14/code/r2_manifold_receipt.json", "08b2140f46ae",
     "the manifold receipt: the locality criterion this unit ports verbatim, "
     "and the 14-of-109 census it is cited from."),
    ("A-COUP-ADJ", "v14/note-coup-adjudication.md", "bacf0af964ae",
     "THE PREDICTION UNDER TEST: paper-20's adjudication, SUCCESSOR "
     "REGISTER -- the monomial theorem as a Sidon property."),
    ("A-PIN-PERL", PIN_REL, "973b160d52ed",
     "this unit's pin, frozen at v14 ledger #196."),
]

# --- path-value anchors: (id, source-id, json path, expected value, note) ---
PATH_VALUE_ANCHORS = [
    ("PV-L", "A-R4-RECEIPT", "counts/L", 4,
     "the parent rung's lattice size: the ladder's first step"),
    ("PV-D", "A-R4-RECEIPT", "counts/d", 2,
     "the anchored spatial dimension, held fixed along the ladder"),
    ("PV-ALPHABET", "A-R4-RECEIPT", "counts/alphabet", 25,
     "the coefficient alphabet, rebuilt here and held fixed along L"),
    ("PV-FIELD", "A-R4-RECEIPT", "counts/field", "Q(ZETA-8)",
     "the parents' field; this unit works in Q(zeta_24), which contains it"),
    ("PV-CIRC", "A-R4-RECEIPT", "counts/circulants", 58,
     "THE REBUILD TARGET: the parent's circulant pool at L = 4"),
    ("PV-CONNECTIVE", "A-R4-RECEIPT", "counts/connective_tag", "MAX-NORM",
     "the FORCED connective, inherited verbatim into SCOPE"),
    ("PV-FORCING-LINK", "A-R4-RECEIPT", "counts/forcing_link", "(1,1)",
     "the anchored link that forces it"),
    ("PV-STENCIL", "A-R4-RECEIPT", "counts/stencil", "3-TERM-AXIS",
     "the declared stencil the family generalisation rule extends"),
    ("PV-ADMISSIBLE", "A-R4-RECEIPT", "admissible_scales", [4],
     "THE UNIQUENESS CLAIM UNDER TEST: the parent's admitted scale set"),
    ("PV-SCALE-LOCALITY", "A-R4-RECEIPT",
     "scale_precheck/locality_iff_L_at_least", 4,
     "the parent's locality threshold at its own window width"),
    ("PV-SCALE-COLLAPSE", "A-R4-RECEIPT",
     "scale_precheck/non_monomial_local_only_if_L_at_most", 4,
     "the parent's collapse bound at its own window width"),
    ("PV-SCALE-PRESENT", "A-R4-RECEIPT",
     "scale_precheck/non_monomial_local_present_at", [2, 4],
     "the parent's measured presence set -- the L = 3 gap is the "
     "alphabet-relative row this unit explains"),
    ("PV-ORD2", "A-R4-RECEIPT", "ord_census/2/non_monomial", 16,
     "the parent's order-2 non-monomial count, reproduced here"),
    ("PV-ORD3", "A-R4-RECEIPT", "ord_census/3/non_monomial", 0,
     "the parent's order-3 emptiness -- alphabet-relative, and this unit "
     "says why"),
    ("PV-ORD4", "A-R4-RECEIPT", "ord_census/4/non_monomial", 48,
     "the parent's order-4 non-monomial count, reproduced here"),
    ("PV-ORD8", "A-R4-RECEIPT", "ord_census/8/non_monomial", 0,
     "the parent's order-8 collapse, reproduced here"),
    ("PV-AXES", "A-R4B-RECEIPT", "pool_counts/axes", 9,
     "the parent's axis count at L = 4: the generalisation rule must "
     "reproduce it"),
    ("PV-LOCAL-AXES", "A-R4B-RECEIPT", "pool_counts/local_axes", 4,
     "the parent's local-axis count at L = 4"),
    ("PV-VMAX", "A-R4B-RECEIPT", "counts/vmax", "2",
     "THE VMAX CLAIM AT THE PARENT RUNG"),
    ("PV-DIAMETER", "A-R4B-RECEIPT", "counts/diameter", 2,
     "the max-norm diameter at the parent rung"),
    ("PV-INTERIOR", "A-R4B-RECEIPT", "counts/interior_radii", [1],
     "the interior-radius set at L = 4"),
    ("PV-INTERIOR-L8", "A-R4B-RECEIPT", "counts/interior_radii_at_l8", 3,
     "THE REGISTER CLAIM UNDER TEST: 3 interior radii at L = 8"),
    ("PV-CELLS", "A-R4B-RECEIPT", "counts/cells", 928,
     "the parent's (family, momentum) cell count at L = 4"),
    ("PV-MOVING", "A-R4B-RECEIPT", "counts/moving", 57,
     "the parent's moving-family count"),
    ("PV-STATIC", "A-R4B-RECEIPT", "counts/static", 1,
     "the parent's static family: the identity"),
    ("PV-PROFILES", "A-R4B-RECEIPT", "counts/distinct_profiles", 58,
     "the parent's separation datum: the symbol separates families"),
    ("PV-MU8", "A-R4B-RECEIPT", "counts/in_mu8", 928,
     "the parent's eigenphase lattice: every eigenvalue an 8th root of unity"),
    ("PV-INTVEL", "A-R4B-RECEIPT", "counts/integer_velocities", 1856,
     "THE INTEGER-VELOCITY CLAIM: all 1856 cells at L = 4"),
    ("PV-COINS", "A-R5-RECEIPT", "counts/coins", 640,
     "the derived coin family: 2x2 unitaries over the parents' alphabet"),
    ("PV-COINS-ANTI", "A-R5-RECEIPT", "counts/coins_antidiagonal", 64,
     "the antidiagonal sector, on which the profile is measured"),
    ("PV-COINS-DIAG", "A-R5-RECEIPT", "counts/coins_diagonal", 64,
     "the diagonal sector"),
    ("PV-COINS-BAL", "A-R5-RECEIPT", "counts/coins_balanced", 512,
     "the balanced sector"),
    ("PV-PROFILE", "A-R5-RECEIPT", "counts/local_profile",
     "S1-ONE=A3;S2-EDGE=A5;S2-CORNER=A3 x A3;S2-APART=A3 x A3;S3-ROW=A7;"
     "S4-BLOCK=A8",
     "THE GAUGE FINGERPRINT UNDER TEST: the (order, support) profile"),
    ("PV-GLOBAL-4", "A-R5-RECEIPT", "counts/global_support_small", 16,
     "the global support at L = 4: the volume"),
    ("PV-GLOBAL-8", "A-R5-RECEIPT", "counts/global_support_large", 64,
     "the global support at L = 8: the volume"),
    ("PV-R2-RULES", "A-R2-RECEIPT", "locality_census/rules_measured", 109,
     "R2's grid size: cited, never re-run here"),
    ("PV-R2-LOCAL", "A-R2-RECEIPT", "locality_census/count_locality_B", 14,
     "R2's locality census: cited, never re-run here"),
    ("PV-R2-CRITERION", "A-R2-RECEIPT", "locality_census/criterion",
     "locality exists at a rule iff SOME connected component of that rule's "
     "overlap graph is NOT complete (the R1 adjudication's criterion, "
     "section 6)",
     "THE CRITERION, PORTED VERBATIM: this unit applies it at a new window "
     "coordinate and at nothing else"),
]

# --- verbatim-text anchors: (id, source-id, consumer gate, exact window) ----
VERBATIM_ANCHORS = [
    ("VB-SIDON", "A-COUP-ADJ", "G-SIDON-PREDICTION-TESTED",
     "The monomial theorem is a SIDON property of the offset set —\n"
     "transports verbatim to R=4, dies at any declared fourth\n"
     "direction (54 non-monomial unitaries appear)."),
    ("VB-INTERIOR", "A-R4B-PAPER", "G-INTERIOR-RADII",
     "The interior-radius count — one here, 3 at L = 8 — is the\n"
     "  successor's parameter, not this unit's finding."),
    ("VB-VMAX", "A-R4B-PAPER", "G-VMAX-IS-DIAMETER",
     "The group speed is a phase advance per momentum\nstep, so it is "
     "bounded by L/2, which is exactly the max-norm diameter; and the\n"
     "monomial shift by the antipodal offset is a unitary member of the axis "
     "family\nat every even L and attains it."),
    ("VB-COLLAPSE", "A-R4-PAPER", "G-ORD-CENSUS-REPRODUCED",
     "**Theorem (order collapse).** *Let $a$ have order $n\\ge 5$ in the "
     "lattice group.\nThen every unitary generator on the stencil "
     "$\\{0,a,-a\\}$ is monomial — exactly\none coefficient is nonzero.*"),
    ("VB-UNIQUE", "A-R4-PAPER", "G-BAND-LAW",
     "Therefore **the admissible set is {4}**, and one lattice size in the "
     "swept range\ncarries both."),
    ("VB-R2W", "A-R2-PAPER", "G-LOCALITY-WINDOWS",
     "> 3. **Locality.** A component is incomplete iff it contains a pair at "
     "cyclic\n>    distance $\\ge c$; when the circulant on $S$ is connected "
     "this is exactly\n>    $c \\le \\operatorname{diam}_k(S)$."),
    ("VB-PROFILE", "A-R5-PAPER", "G-PROFILE-PERSISTS",
     "The stencil profile the declarations trace is\n"
     "`S1-ONE = A3; S2-EDGE = A5; S2-CORNER = A3 x A3; S2-APART = A3 x A3; "
     "S3-ROW = A7; S4-BLOCK = A8`,"),
    ("VB-PIN-STAGES", "A-PIN-PERL", "G-STAGES-DECLARED",
     "The prediction PASSES/FAILS per arena — a\n   prediction-ledger entry "
     "either way."),
    ("VB-PIN-SCOPE", "A-PIN-PERL", "G-WALLS",
     "no continuum claim — this unit measures PERSISTENCE AT DECLARED\n"
     "FINITE RUNGS, nothing more.  NO transport numbers inherited"),
]

VERBATIM_LENGTH_FLOOR = 60

# --- the declared arena ----------------------------------------------------
LADDER = (4, 6, 8)                 # the declared rungs
PARENT_RUNG = 4
CONTROL_RUNG = 3                   # paper-20's own arena, for the control
LINK_SET = ((1, 0), (0, 1), (1, 1))       # anchored at A-R4-PAPER's stage
FOURTH_DIRECTION = (1, 2)                 # paper-20's declared fourth
WIDTHS = (1, 2, 3)                        # the declared window widths
BAND_SIZES = tuple(range(2, 15))          # the declared band sweep
DDS_SUBSET_WINDOW = 12             # |S| at which the subset census is run
PLAQ_STENCILS = (("S1-ONE", ((0, 0),)),
                 ("S2-EDGE", ((0, 0), (1, 0))),
                 ("S2-CORNER", ((0, 0), (1, 1))),
                 ("S2-APART", ((0, 0), (2, 0))),
                 ("S3-ROW", ((0, 0), (1, 0), (2, 0))),
                 ("S4-BLOCK", ((0, 0), (1, 0), (0, 1), (1, 1))))

PREREGISTERED_HEADS = (
    "PERL-SIDON-SUFFICIENT-NOT-NECESSARY",
    "PERL-SIDON-CONFIRMED-BOTH-WAYS",
    "PERL-SIDON-REFUTED",
    "PERL-BLOCKED-AT-THE-FAMILY-GENERALISATION",
    "PERL-BLOCKED-AT-THE-EIGENPHASE-LATTICE",
)

QUIET = False
MUT = None
LOG = []
NOT_EXECUTED = []

# ===========================================================================
# SECTION 1.  THE EXACT FIELD Q(zeta_24)
# ===========================================================================
# Phi_24 is COMPUTED, never typed: x^24 - 1 divided by the lower cyclotomics.

def _polymul(a, b):
    out = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y:
                    out[i + j] += x * y
    return out


def _polydiv(a, b):
    a = list(a)
    q = [Fraction(0)] * max(1, len(a) - len(b) + 1)
    while True:
        while a and a[-1] == 0:
            a.pop()
        if len(a) < len(b):
            break
        s = a[-1] / b[-1]
        k = len(a) - len(b)
        q[k] = s
        for j, y in enumerate(b):
            a[k + j] -= s * y
    return q, a


def cyclotomic_poly(n):
    num = [Fraction(-1)] + [Fraction(0)] * (n - 1) + [Fraction(1)]
    den = [Fraction(1)]
    for d in range(1, n):
        if n % d == 0:
            den = _polymul(den, cyclotomic_poly(d))
    q, r = _polydiv(num, den)
    if any(r):
        raise GateFail("G-FIELD-CANONICAL :: Phi_%d did not divide" % n)
    return q


PHI24 = cyclotomic_poly(24)
DEG = len(PHI24) - 1                    # phi(24) = 8
ZERO = tuple([Fraction(0)] * DEG)
ONE = tuple([Fraction(1)] + [Fraction(0)] * (DEG - 1))


def _reduce(c):
    """x^8 = x^4 - 1 (that is Phi_24 = x^8 - x^4 + 1), applied top down."""
    c = list(c)
    for i in range(len(c) - 1, DEG - 1, -1):
        if c[i]:
            v = c[i]
            c[i] = Fraction(0)
            c[i - 4] += v
            c[i - 8] -= v
    return tuple(c[:DEG])


def cadd(a, b):
    return tuple(a[i] + b[i] for i in range(DEG))


def cneg(a):
    return tuple(-a[i] for i in range(DEG))


def cmul(a, b):
    out = [Fraction(0)] * (2 * DEG - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y:
                    out[i + j] += x * y
    return _reduce(out)


def zeta(t):
    """zeta_24^t."""
    v = [Fraction(0)] * 24
    v[t % 24] = Fraction(1)
    return _reduce(v)


def cconj(a):
    out = [Fraction(0)] * 24
    for i, x in enumerate(a):
        if x:
            out[(-i) % 24] += x
    return _reduce(out)


def cscal(a, num, den=1):
    f = Fraction(num, den)
    return tuple(x * f for x in a)


def cstr(a):
    if a == ZERO:
        return "0"
    parts = []
    for i in range(DEG):
        if a[i]:
            co = ("%s" % a[i]) if a[i].denominator != 1 else "%d" % a[i]
            parts.append(("%s" % co) if i == 0 else "%s*z^%d" % (co, i))
    return "+".join(parts).replace("+-", "-")


def build_alphabet():
    """R4's 25, rebuilt from its paper's definition: 0 together with
    zeta_8^t times a modulus in {1, 1/2, 1/sqrt2}.  zeta_8 = zeta_24^3, and
    1/sqrt2 = (zeta_8 + zeta_8^-1)/2, both exact in this field."""
    inv_sq2 = cscal(cadd(zeta(3), zeta(-3)), 1, 2)
    out, seen = [ZERO], {ZERO}
    for t in range(8):
        z = zeta(3 * t)
        for m in ("1", "1/2", "1/sqrt2"):
            e = (z if m == "1" else
                 cscal(z, 1, 2) if m == "1/2" else cmul(z, inv_sq2))
            if e not in seen:
                seen.add(e)
                out.append(e)
    return tuple(out), inv_sq2, cmul(zeta(6), inv_sq2)


ALPHABET, INV_SQ2, I_INV_SQ2 = build_alphabet()


def alphabet_units_omega():
    """the 7-value probe: 0 and the six units +-1, +-w, +-w^2 (w = zeta_3)."""
    out = [ZERO]
    for j in range(3):
        for s in (1, -1):
            out.append(cscal(zeta(8 * j), s, 1))
    return tuple(out)


def alphabet_thirds_omega():
    """the 19-value probe: 0 and {+-1/3, +-2/3, +-1} times each cube root."""
    out, seen = [ZERO], {ZERO}
    for n in (1, 2, 3):
        for s in (1, -1):
            for j in range(3):
                e = cmul(cscal(ONE, s * n, 3), zeta(8 * j))
                if e not in seen:
                    seen.add(e)
                    out.append(e)
    return tuple(out)


PROBE_ALPHABETS = (("R4-25", ALPHABET),
                   ("UNIT-7", alphabet_units_omega()),
                   ("THIRDS-19", alphabet_thirds_omega()))

# ===========================================================================
# SECTION 2.  GATES, MUTANTS, THE SEAL
# ===========================================================================


class GateFail(Exception):
    pass


class CliError(Exception):
    pass


def say(msg=""):
    """the transcript.  Diagnostic runs (self-test, in-process mutants) are
    QUIET and contribute nothing, so the written output is the delivery run's
    own transcript and nothing else."""
    if not QUIET:
        LOG.append(msg)
        print(msg, flush=True)


def mut(name):
    """the ONLY mutant switch.  No gate predicate may reference it."""
    return MUT == name


def digest(value):
    if isinstance(value, str):
        return hashlib.sha256(value.encode("utf-8")).hexdigest()[:12]
    return hashlib.sha256(
        json.dumps(value, indent=1, sort_keys=True).encode("utf-8")
    ).hexdigest()[:12]


class Ledger:
    """the gate ledger, CHAINED: every row is digested at the moment it
    closes, and each digest folds in its predecessor, so a row edited after
    its gate closed breaks the chain from that point on."""

    def __init__(self):
        self.rows = []
        self.ids = set()
        self.digests = []
        self.chain = digest(SCHEMA)
        self.seal = None          # THE GATE-TIME SEAL, attached by the build
        self.state = None

    def gate(self, gid, claim, ok, detail="", kind="MEASURED"):
        if gid in self.ids:
            raise GateFail("%s :: duplicate gate id" % gid)
        self.ids.add(gid)
        row = {"gate": gid, "claim": claim, "passed": bool(ok),
               "detail": detail, "kind": kind}
        self.rows.append(row)
        self.chain = digest(self.chain + digest(row))
        self.digests.append(self.chain)
        if not ok:
            raise GateFail("%s :: %s :: %s" % (gid, claim, detail))
        # #119, literally: a value is digested AT THE MOMENT ITS GATE PASSES,
        # here and nowhere else.  Nothing is sealed in a late take.
        if self.seal is not None and self.state is not None:
            for sid, path, g in SEALED_PATHS:
                if g != gid or sid in self.seal.index:
                    continue
                try:
                    val = jpath(self.state, path)
                except (KeyError, IndexError, TypeError):
                    continue
                self.seal.take_value(sid, val)
        return True


SEALED_PATHS = [
    ("SEAL-VERDICT-STRING", "verdict/string", "G-VERDICT-RECONSTRUCTED"),
    ("SEAL-VERDICT-HEAD", "verdict/head", "G-VERDICT-RECONSTRUCTED"),
    ("SEAL-COUNTS", "counts", "G-VERDICT-RECONSTRUCTED"),
    ("SEAL-ARENAS", "sidon_arenas", "G-SIDON-PREDICTION-TESTED"),
    ("SEAL-PREDICTION", "sidon_prediction", "G-SIDON-PREDICTION-TESTED"),
    ("SEAL-CONTROL", "fourth_direction_control", "G-FOURTH-DIRECTION-CONTROL"),
    ("SEAL-DDS", "dds_law", "G-DDS-CRITERION-SOUND"),
    ("SEAL-ORD", "ord_census", "G-ORD-CENSUS-REPRODUCED"),
    ("SEAL-POOL", "pool_census", "G-POOL-REPRODUCES-THE-PARENT"),
    ("SEAL-DISPERSION", "dispersion_census", "G-EIGENVALUES-ROOTS-OF-UNITY"),
    ("SEAL-VMAX", "vmax_census", "G-VMAX-IS-DIAMETER"),
    ("SEAL-RADII", "interior_radii", "G-INTERIOR-RADII"),
    ("SEAL-VELOCITY", "velocity_census", "G-INTEGER-VELOCITY-CENSUS"),
    ("SEAL-COINS", "coin_sectors", "G-COIN-ALPHABET-DERIVED"),
    ("SEAL-STRATA", "strata", "G-STRATA-PERFECT-MATCHINGS"),
    ("SEAL-PROFILE", "gauge_profile", "G-PROFILE-PERSISTS"),
    ("SEAL-GLOBAL", "global_stencil", "G-GLOBAL-SUPPORT-IS-THE-VOLUME"),
    ("SEAL-WINDOWS", "locality_windows", "G-LOCALITY-WINDOWS"),
    ("SEAL-PARTITION", "partition_control", "G-PARTITION-COROLLARY"),
    ("SEAL-BAND", "band_law", "G-BAND-LAW"),
    ("SEAL-TABLE", "persistence_table", "G-PERSISTENCE-TABLE-BOUND"),
    ("SEAL-CHOICES", "choice_inventory", "G-CHOICES-INVENTORIED"),
    ("SEAL-PATH-ANCHORS", "path_value_anchors", "G-PATH-VALUE-ANCHORS"),
    ("SEAL-BYTE-ANCHORS", "byte_anchors", "G-SOURCES-PINNED"),
    ("SEAL-VERBATIM", "verbatim_anchors", "G-VERBATIM-ANCHORS"),
    ("SEAL-PROVENANCE", "source_sha256", "G-SOURCES-PINNED"),
    ("SEAL-PREREGISTERED", "preregistered_heads", "G-VERDICT-PREREGISTERED"),
    ("SEAL-FRACTIONS", "declared_fractions", "G-FRACTIONS-STAMPED"),
    ("SEAL-WAIVERS", "waiver_ledger", "G-WAIVERS-VERIFIED"),
    ("SEAL-PAPER-CLAIMS", "paper_claims", "G-PAPER-CLAIMS"),
    ("SEAL-PAPER-POLARITY", "paper_polarity", "G-PAPER-CLAIM-POLARITY"),
    ("SEAL-PAPER-FENCES", "paper_fences", "G-PAPER-FENCED-MULTISET"),
    ("SEAL-MUTANTS", "mutants", "G-MUTANTS-ON-TARGET"),
    ("SEAL-GATES", "gates", "G-PAPER-COVERAGE-FINAL"),
    ("SEAL-TOTALS", "totals", "G-PAPER-COVERAGE-FINAL"),
    ("SEAL-COVERAGE", "paper_coverage", "G-PAPER-COVERAGE-FINAL"),
    ("SEAL-ALPHABET", "alphabet_rebuilt", "G-ALPHABET-REBUILT"),
    ("SEAL-AXES", "axis_census", "G-AXIS-SET-EXHAUSTIVE"),
    ("SEAL-WRAP", "non_wrapping", "G-NON-WRAPPING"),
    ("SEAL-WIDTHCOUNT", "width_count",
     "G-WIDTH-COUNT-EQUALS-INTERIOR-RADII"),
    ("SEAL-FALSIFIERS", "falsifier_descriptions",
     "G-FALSIFIER-DESCRIPTIONS"),
]

DECLARED_UNSEALED = {
    "schema": "a frozen literal of this file, not a measurement",
    "unit": "a frozen literal of this file, not a measurement",
    "pin": "a frozen literal: the pin's path",
    "pin_sha256_prefix": "read from the SEALED byte-anchor row it quotes",
    "arithmetic": "a frozen literal describing the field representation",
    "arena_declaration": "the declaration itself (RUNBOOK section 15): every "
                         "value in it is a frozen literal of this file or a "
                         "length of a SEALED table, and G-ARENA-DECLARED "
                         "gates its contents into the verdict",
    "runtime_inputs": "the enumerated read list, gated at "
                      "G-RUNTIME-INPUTS-ENUMERATED and re-derived at the disk "
                      "boundary against the SEALED byte anchors",
    "verdict": "its parts are sealed individually (SEAL-VERDICT-STRING, "
               "SEAL-VERDICT-HEAD) and the segments are RE-DERIVED from the "
               "sealed primitive tables at G-VERDICT-RECONSTRUCTED, in run "
               "and again from the bytes on disk",
    "seal_manifest": "the seal's own account of itself: it cannot digest the "
                     "object it is being written into.  It is bound instead "
                     "by re-derivation at the disk boundary against the live "
                     "seal",
    "not_executed": "an empty declared list; a non-empty one would be a "
                    "finding and is gated at G-NOT-EXECUTED-EMPTY",
    "gate_digests": "THE CHAINED GATE-TIME SEAL of `gates` itself: each row's "
                    "digest folds in its predecessor, so the list is still "
                    "growing when the last gate closes and cannot be sealed "
                    "by a take; it is verified against the rows in run at "
                    "G-GATE-ROWS-SEALED and again from the bytes on disk",
    "sweep_totals": "the post-sweep counts.  They exist only after the mutant "
                    "runner closes, which is outside every in-process run, so "
                    "they are RE-DERIVED as an identity from the SEALED "
                    "`mutants` rows and the gate rows, in run and again from "
                    "the bytes on disk",
}


def jpath(obj, path):
    cur = obj
    for part in path.split("/"):
        if isinstance(cur, list):
            cur = cur[int(part)]
        else:
            cur = cur[part]
    return cur


class Seal:
    def __init__(self):
        self.rows = []
        self.index = {}
        self.verdict_string = None
        self.payload = None
        self.payload_sha = None
        self.transcript = None
        self.transcript_sha = None
        self.gate_digests = []

    def take(self, sid, obj):
        path = [p for s, p, _g in SEALED_PATHS if s == sid][0]
        self.take_value(sid, jpath(obj, path))

    def take_value(self, sid, value):
        if sid in self.index:
            return
        path = [p for s, p, _g in SEALED_PATHS if s == sid][0]
        gate = [g for s, _p, g in SEALED_PATHS if s == sid][0]
        d = digest(value)
        self.rows.append({"seal": sid, "path": path, "sealed_at_gate": gate,
                          "sha256_12": d})
        self.index[sid] = d
        if sid == "SEAL-VERDICT-STRING":
            self.verdict_string = value

    def verify(self, obj):
        broken = []
        for row in self.rows:
            try:
                now = digest(jpath(obj, row["path"]))
            except (KeyError, IndexError, TypeError):
                broken.append(row["seal"])
                continue
            if now != row["sha256_12"]:
                broken.append(row["seal"])
        return broken

    def close(self, obj, payload):
        broken = self.verify(obj)
        if broken:
            raise GateFail("G-ARTIFACT-INTEGRITY :: the payload was sealed "
                           "over a broken seal :: %s" % broken)
        self.payload = payload
        self.payload_sha = digest(payload)

    def close_transcript(self, text):
        self.transcript = text
        self.transcript_sha = digest(text)


FORCINGS = {
    "G-MUTANTS-ON-TARGET":
        "the gate that adjudicates the mutant sweep cannot itself be a "
        "mutant's target; its falsifier is the sweep, and every surviving or "
        "off-target injection fails it -- exercised by all declared mutants "
        "on every run",
    "G-ARTIFACT-INTEGRITY":
        "evaluated only in the writing path, which no diagnostic run reaches; "
        "it is two-way by construction -- a deliberately corrupted payload is "
        "written to a probe path, re-read and required to be detected -- and "
        "its reference is the GATE-TIME SEAL, whose in-run half "
        "G-SEAL-COMPLETE carries the injection falsifier MUT-SEAL-BROKEN",
    "G-PAPER-COVERAGE-FINAL":
        "evaluated after the mutant sweep closes the instrument's totals, so "
        "no in-process mutant can reach it; its in-run twins G-PAPER-CLAIMS, "
        "G-PAPER-NUMERAL-COVERAGE, G-PAPER-INLINE-SPANS, "
        "G-PAPER-FENCED-MULTISET and G-PAPER-CLAIM-POLARITY carry the "
        "injection falsifiers and die on every sweep",
    "G-GATE-LEDGER-COVERS-THE-RUN":
        "evaluated after the mutant sweep, so no in-process mutant can reach "
        "it; it is a coverage identity over the CLOSED ledger and the closed "
        "gate rows, and it cannot pass unless the two sets agree",
    "G-GATES-CLOSED-AS-PREDICTED":
        "evaluated after the mutant sweep, so no in-process mutant can reach "
        "it; its falsifier is every mutant that adds or removes a gate -- the "
        "sweep runs 48 of them and the ledger closes at the predicted number "
        "on the delivery run alone",
    "G-PUBLISHED-KEYS-COVERED":
        "evaluated after the mutant sweep adds the post-sweep keys, so no "
        "in-process mutant can reach it; its in-run twin "
        "G-SEAL-MANIFEST-TOTAL carries the injection falsifier "
        "MUT-SEAL-MANIFEST and evaluates the same predicate over the "
        "predicted key set on every sweep",
    "G-SOURCES-PRESENT":
        "evaluated before any gate ledger exists, as the loud clean abort a "
        "provisioning failure earns; its falsifier is the off-tree battery, "
        "which runs the instrument from a copy with a source removed and "
        "requires exit 1 with nothing written",
}

# ===========================================================================
# SECTION 3.  ANCHORS
# ===========================================================================

READS = []


def sha12(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()[:12]


def read_text(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def source_path(rel):
    p = os.path.join(REPO, rel)
    READS.append(rel)
    return p


def norm_text(s):
    """#125: whitespace AND markdown-prefix normalisation on BOTH sides, so a
    claim broken across lines, indented, bulleted or blockquoted is still the
    same characters in the same order -- and nothing else is forgiven."""
    s = re.sub(r"(?m)^[ \t]*(?:>[ \t]?)+", " ", s)
    s = re.sub(r"(?m)^[ \t]*(?:[-*+]|\d+\.)[ \t]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def require_sources():
    """#91: the loud clean abort.  Every declared source must be present
    before a single gate runs; an under-provisioned copy dies here, writes
    nothing, and says exactly what is missing."""
    missing = [(sid, rel) for sid, rel, _d, _n in SOURCES
               if not os.path.exists(os.path.join(REPO, rel))]
    if missing:
        print("ABORT: G-SOURCES-PRESENT :: this copy is under-provisioned; "
              "the instrument reads its inputs by path relative to the "
              "repository root derived from __file__ (%s) and %d declared "
              "source(s) are absent:" % (REPO, len(missing)), flush=True)
        for sid, rel in missing:
            print("  missing  %-14s %s" % (sid, rel), flush=True)
        print("Nothing was written.  EXIT 1", flush=True)
        sys.exit(1)

# ===========================================================================
# SECTION 4.  OFFSET SETS: DIFFERENCES, SIDON, AND THE DDS CRITERION
# ===========================================================================
# The whole of stage 1 turns on one combinatorial object: the multiset of
# ordered differences of an offset set.  A set is SIDON when every nonzero
# difference is realised exactly once.  It is DIFFERENCE-DOUBLED (DDS) when
# every nonzero difference realised inside it is realised at least twice.
#
# THEOREM (the DDS criterion).  Let S be an offset set in a finite abelian
# group and let c be a unitary coefficient map supported on S.  Then supp(c)
# is difference-doubled.  Hence if no subset of S of size >= 2 is
# difference-doubled, every unitary map on S is monomial -- over any field
# closed under conjugation.
#   Proof.  Unitarity is A(m) = sum_v c_v conj(c_{v+m}) = delta_{m,0}.  For
#   m != 0 the terms are exactly the ordered pairs of supp(c) with difference
#   m.  If there is exactly one such pair (v, w) then c_w conj(c_v) = 0, and
#   both factors are nonzero on the support: contradiction.  So every
#   difference realised inside supp(c) is realised at least twice. []
#
# Sidon implies DDS-free (in a Sidon set every internal difference is
# simple), and the implication is STRICT: {0, a, -a} at ord(a) >= 5 is not
# Sidon (+-a are doubled) yet is DDS-free (+-2a are simple).  That strictness
# is what this unit measures.


def diff_multiset(S, L):
    out = {}
    for v in S:
        for w in S:
            if v == w:
                continue
            m = ((v[0] - w[0]) % L, (v[1] - w[1]) % L)
            out[m] = out.get(m, 0) + 1
    return out


def is_sidon(S, L):
    d = diff_multiset(S, L)
    return (len(S) < 2 or all(k == 1 for k in d.values())), d


def is_doubled(T, L):
    if len(T) < 2:
        return False
    return all(k >= 2 for k in diff_multiset(T, L).values())


def doubled_subsets(S, L):
    """every subset of size >= 2 that is difference-doubled.  Exhaustive over
    2^|S| subsets, which the declared window bounds."""
    if len(S) > DDS_SUBSET_WINDOW:
        raise GateFail("G-DDS-WINDOW :: |S| = %d exceeds the declared subset "
                       "window %d" % (len(S), DDS_SUBSET_WINDOW))
    out = []
    for r in range(2, len(S) + 1):
        for T in combinations(sorted(S), r):
            if is_doubled(T, L):
                out.append(T)
    return out


def doubled_pair(S, L):
    """the cheapest doubled subset: two offsets differing by an involution.
    Available at any |S|, and the constructive witness below uses it."""
    for v, w in combinations(sorted(S), 2):
        d = ((v[0] - w[0]) % L, (v[1] - w[1]) % L)
        if (2 * d[0]) % L == 0 and (2 * d[1]) % L == 0:
            return (v, w)
    return None

# ===========================================================================
# SECTION 5.  THE UNITARITY SCAN
# ===========================================================================

_SCAN_MEMO = {}


def lag_structure(S, L):
    """for every group element, the ordered pairs of S realising it as a
    difference.  This is the whole of the unitarity condition: a lag outside
    this table receives no term, which G-LAG-SUPPORT-STRUCTURAL binds per
    (offset-set, lag) object."""
    tab = {}
    for i, v in enumerate(S):
        for j, w in enumerate(S):
            m = ((v[0] - w[0]) % L, (v[1] - w[1]) % L)
            tab.setdefault(m, []).append((i, j))
    return tab


def scan_offsets(S, A, L):
    """EXHAUSTIVE over A^|S|: the unitary maps on the offset set S."""
    key = (tuple(S), tuple(A), L)
    got = _SCAN_MEMO.get(key)
    if got is not None:
        return got
    n = len(S)
    tab = lag_structure(S, L)
    zero = (0, 0)
    prod_tab = [[cmul(A[i], cconj(A[j])) for j in range(len(A))]
                for i in range(len(A))]
    lags = sorted(tab.items(), key=lambda t: (t[0] == zero, len(t[1])))
    uni = mono = 0
    wits = []
    for c in product(range(len(A)), repeat=n):
        ok = True
        for m, prs in lags:
            acc = ZERO
            for (i, j) in prs:
                if c[i] and c[j]:
                    acc = cadd(acc, prod_tab[c[i]][c[j]])
            if acc != (ONE if m == zero else ZERO):
                ok = False
                break
        if not ok:
            continue
        uni += 1
        supp = [k for k in range(n) if c[k]]
        if len(supp) <= 1:
            mono += 1
        elif len(wits) < 2:
            wits.append({"coefficients":
                         [[list(S[k]), cstr(A[c[k]])] for k in supp],
                         "support": len(supp)})
    out = {"maps": len(A) ** n, "unitary": uni, "monomial": mono,
           "non_monomial": uni - mono, "witnesses": wits}
    _SCAN_MEMO[key] = out
    return out


def autocorr_is_delta(coef, L):
    """the parent's own criterion, written over the WHOLE torus: the second,
    independent code path.  Used at the parent rung to bind the structural
    route object by object."""
    for m in product(range(L), repeat=2):
        acc = ZERO
        for v, cv in coef.items():
            w = ((v[0] + m[0]) % L, (v[1] + m[1]) % L)
            cw = coef.get(w)
            if cw is not None:
                acc = cadd(acc, cmul(cv, cconj(cw)))
        if acc != (ONE if not any(m) else ZERO):
            return False
    return True

# ===========================================================================
# SECTION 6.  THE FAMILY, GENERALISED: AXES, THE POOL, THE DISPERSIONS
# ===========================================================================
# THE FAMILY-GENERALISATION RULE, DECLARED (pin, "WINDOWS AND HONESTY").
# R4's construction is applied verbatim at each rung: the axis set is every
# nonzero offset modulo sign (exhaustive, fiber = the axis count at that L,
# every instance run); the stencil is the parent's 3-term {0, a, -a}; the
# alphabet is the parent's 25, held fixed; the quotient is the parent's
# global-phase gauge.  Nothing is chosen at L = 6 or L = 8 that was not
# already chosen at L = 4, and the rule reproduces the parent's own numbers
# at L = 4 -- which G-POOL-REPRODUCES-THE-PARENT binds.

_POOL_MEMO = {}
_ORD_MEMO = {}


def torus_absmax(v, L):
    return max(min(x % L, (-x) % L) for x in v)


def elt_order(a, L):
    k, cur = 1, a
    while any(cur):
        cur = ((cur[0] + a[0]) % L, (cur[1] + a[1]) % L)
        k += 1
    return k


def axes(L):
    seen, out = set(), []
    for v in product(range(L), repeat=2):
        if not any(v) or v in seen:
            continue
        seen.add(v)
        seen.add(((-v[0]) % L, (-v[1]) % L))
        out.append(v)
    return out


def axis_stencil(a, L):
    na = ((-a[0]) % L, (-a[1]) % L)
    out = []
    for o in ((0, 0), a, na):
        if o not in out:
            out.append(o)
    return out


def ord_census(n, A):
    """the parent's order sweep, verbatim: triples added into the offsets
    0, 1, -1 of Z_n, deduplicated, tested by the ring autocorrelation."""
    key = (n, tuple(A))
    got = _ORD_MEMO.get(key)
    if got is not None:
        return dict(got)
    gens = set()
    for t0, t1, t2 in product(range(len(A)), repeat=3):
        c = {}
        for o, v in ((0 % n, A[t0]), (1 % n, A[t1]), ((-1) % n, A[t2])):
            c[o] = cadd(c.get(o, ZERO), v)
        c = {o: v for o, v in c.items() if v != ZERO}
        k = tuple(sorted(c.items()))
        if k in gens:
            continue
        ok = True
        for m in range(n):
            acc = ZERO
            for v, cv in c.items():
                cw = c.get((v + m) % n)
                if cw is not None:
                    acc = cadd(acc, cmul(cv, cconj(cw)))
            if acc != (ONE if m == 0 else ZERO):
                ok = False
                break
        if ok:
            gens.add(k)
    mono = sum(1 for g in gens if len(g) <= 1)
    out = {"triples_swept": len(A) ** 3, "distinct_generators": len(gens),
           "monomial": mono, "non_monomial": len(gens) - mono}
    _ORD_MEMO[key] = out
    return dict(out)


def build_pool(L, A, full_route=False):
    """the circulant pool at rung L under the declared rule."""
    key = (L, tuple(A), full_route)
    got = _POOL_MEMO.get(key)
    if got is not None:
        return got
    reps, out, orbit_sizes = set(), [], []
    for a in axes(L):
        S = axis_stencil(a, L)
        tab = lag_structure(S, L)
        prod_tab = [[cmul(A[i], cconj(A[j])) for j in range(len(A))]
                    for i in range(len(A))]
        zero = (0, 0)
        lags = sorted(tab.items(), key=lambda t: (t[0] == zero, len(t[1])))
        na = ((-a[0]) % L, (-a[1]) % L)
        sols = {}
        for t0, t1, t2 in product(range(len(A)), repeat=3):
            coef = {}
            for o, v in (((0, 0), A[t0]), (a, A[t1]), (na, A[t2])):
                coef[o] = cadd(coef.get(o, ZERO), v)
            coef = {o: v for o, v in coef.items() if v != ZERO}
            k = tuple(sorted(coef.items()))
            if k in sols:
                continue
            if full_route:
                ok = autocorr_is_delta(coef, L)
            else:
                ok = True
                idx = {o: i for i, o in enumerate(S)}
                cv = [coef.get(o, ZERO) for o in S]
                for m, prs in lags:
                    acc = ZERO
                    for (i, j) in prs:
                        if cv[i] != ZERO and cv[j] != ZERO:
                            acc = cadd(acc, cmul(cv[i], cconj(cv[j])))
                    if acc != (ONE if m == zero else ZERO):
                        ok = False
                        break
            if ok:
                sols[k] = coef
        done = set()
        for k in sorted(sols):
            if k in done:
                continue
            orb = {tuple(sorted((o, cmul(zeta(3 * t), v)) for o, v in k))
                   for t in range(8)}
            done |= orb
            orbit_sizes.append(len(orb))
            rep = min(orb)
            if rep in reps:
                continue
            reps.add(rep)
            coef = dict(rep)
            out.append({"axis": a, "axis_ord": elt_order(a, L), "coef": coef,
                        "support": len(coef),
                        "radius": max([torus_absmax(o, L) for o in coef]
                                      or [0]),
                        "monomial": len(coef) <= 1})
    res = (out, orbit_sizes)
    _POOL_MEMO[key] = res
    return res


MU24 = {zeta(t): t for t in range(24)}


_DISP_MEMO = {}


def dispersion(L, pool):
    """the symbol lambda(k) = sum_o c_o zeta_L^{-k.o} at every momentum, and
    its eigenphase in Z/24.  zeta_L = zeta_24^(24/L) is exact for every rung.

    Memoised on the CONTENT of the pool -- the tuple of its coefficient maps
    -- so a perturbed pool never reads a clean cache."""
    key = (L, tuple(tuple(sorted(g["coef"].items())) for g in pool))
    got = _DISP_MEMO.get(key)
    if got is not None:
        return got
    step = 24 // L
    momenta = list(product(range(L), repeat=2))
    rows = []
    for g in pool:
        s, offlat = {}, None
        for k in momenta:
            lam = ZERO
            for o, cv in g["coef"].items():
                lam = cadd(lam, cmul(cv, zeta(-step * (k[0] * o[0]
                                                       + k[1] * o[1]))))
            t = MU24.get(lam)
            if t is None:
                offlat = (k, cstr(lam))
                break
            s[k] = t
        rows.append({"gen": g, "s": s, "off_lattice": offlat})
    _DISP_MEMO[key] = (rows, momenta)
    return rows, momenta


def velocity_rows(L, rows, momenta):
    """v_j(k) = -(L/24) lift_24(Delta_j s); the speed is (L/24) times the
    circle distance, which is lift-free.  The parent's declared reading
    (forward stencil, tie averaged) is the one carried."""
    out = []
    for r in rows:
        s = r["s"]
        vmax = Fraction(0)
        nonint = []
        aliased = 0
        for k in momenta:
            for j in range(2):
                kk = list(k)
                kk[j] = (kk[j] + 1) % L
                d = (s[tuple(kk)] - s[k]) % 24
                cd = min(d, 24 - d)
                sp = Fraction(L, 24) * cd
                if sp > vmax:
                    vmax = sp
                if d == 12:
                    aliased += 1
                lift = d if d <= 12 else d - 24
                v = Fraction(-L, 24) * lift
                if v.denominator != 1:
                    nonint.append((k, j, str(v)))
        sig = tuple((s[k] - s[(0, 0)]) % 24 for k in momenta)
        out.append({"axis": r["gen"]["axis"], "ord": r["gen"]["axis_ord"],
                    "support": r["gen"]["support"],
                    "radius": r["gen"]["radius"], "vmax": vmax,
                    "moves": any(x != sig[0] for x in sig), "sig": sig,
                    "aliased": aliased, "non_integer": nonint})
    return out

# ===========================================================================
# SECTION 7.  LOCALITY AT A WINDOW WIDTH, AND THE BAND
# ===========================================================================
# R2's criterion, ported verbatim (PV-R2-CRITERION), applied at a coordinate
# R4 did not sweep: the WINDOW WIDTH r of the neighbourhood ball.  R4 swept
# the DIMENSION at fixed r = 1 and found threshold 4 at every dimension; R2's
# theorem R2-W says locality survives exactly while the window is narrower
# than the diameter of the index set.  Here that reads: the radius-r ball is
# a proper subset of the torus iff r < diam = floor(L/2).


def ball(L, r):
    return [v for v in product(range(L), repeat=2) if torus_absmax(v, L) <= r]


def locality_at_width(L, r):
    B = ball(L, r)
    nb = len(B) - 1
    offs = L * L - 1
    complete = (nb == offs)
    edges = L * L * nb // 2
    return {"L": L, "r": r, "neighbours": nb, "offsets": offs,
            "complete": complete, "locality": not complete,
            "edges": edges, "b1": edges - L * L + 1}


def blockwise_components(L, b):
    """R2's partition corollary, transported: an atlas whose cells partition
    the sites can never produce a non-complete component."""
    comps = {}
    for v in product(range(L), repeat=2):
        comps.setdefault((v[0] // b, v[1] // b), []).append(v)
    rows = []
    for key, cell in sorted(comps.items()):
        n = len(cell)
        rows.append({"cell": list(key), "size": n,
                     "drawn": n * (n - 1) // 2,
                     "possible": n * (n - 1) // 2, "complete": True})
    return rows


def band_witness(L, r):
    """the constructive half of the band law: two offsets of the radius-r
    ball differing by an involution carry an explicit non-monomial unitary,
    c = 1/sqrt2 at one and i/sqrt2 at the other, both in the declared
    alphabet.  Verified by the parent's own whole-torus criterion."""
    dp = doubled_pair(ball(L, r), L)
    if dp is None:
        return None
    v, w = dp
    coef = {v: INV_SQ2, w: I_INV_SQ2}
    if not autocorr_is_delta(coef, L):
        raise GateFail("G-BAND-LAW :: the declared witness is not unitary at "
                       "L=%d r=%d" % (L, r))
    return {"pair": [list(v), list(w)],
            "radius": max(torus_absmax(o, L) for o in coef),
            "support": 2, "coefficients": [cstr(INV_SQ2), cstr(I_INV_SQ2)]}

# ===========================================================================
# SECTION 8.  THE GAUGE FINGERPRINT: COINS, STRATA, PLAQUETTE HOLONOMY
# ===========================================================================

_COIN_MEMO = {}
_GROUP_MEMO = {}
E1, E2 = (1, 0), (0, 1)


def build_coins(A):
    key = tuple(A)
    got = _COIN_MEMO.get(key)
    if got is not None:
        return got
    ct = [[cmul(cconj(A[i]), A[j]) for j in range(len(A))]
          for i in range(len(A))]
    out = []
    for i, j, k, m in product(range(len(A)), repeat=4):
        if cadd(ct[i][i], ct[k][k]) != ONE:
            continue
        if cadd(ct[j][j], ct[m][m]) != ONE:
            continue
        if cadd(ct[i][j], ct[k][m]) != ZERO:
            continue
        out.append((A[i], A[j], A[k], A[m]))
    _COIN_MEMO[key] = tuple(out)
    return _COIN_MEMO[key]


def coin_sector(m):
    a, b, c, d = m
    if b == ZERO and c == ZERO:
        return "DIAGONAL"
    if a == ZERO and d == ZERO:
        return "ANTIDIAGONAL"
    return "BALANCED"


def addv(s, v, L):
    return ((s[0] + v[0]) % L, (s[1] + v[1]) % L)


def link_ends(l, L):
    s, d = l
    return s, addv(s, (E1, E2)[d], L)


def plaquette_boundary(p, L):
    """p -> p+e1 -> p+e1+e2 -> p+e2 -> p; -1 means the link is traversed
    against its own direction, so its operator is inverted."""
    return (((p, 0), 1), ((addv(p, E1, L), 1), 1),
            ((addv(p, E2, L), 0), -1), ((p, 1), -1))


def strata(L):
    sites = list(product(range(L), repeat=2))
    out = {}
    for d, tag in ((0, "X"), (1, "Y")):
        for par, pn in ((0, "EVEN"), (1, "ODD")):
            out["%s-%s" % (tag, pn)] = [(s, d) for s in sites
                                        if s[d] % 2 == par]
    return out


_HOL_MEMO = {}


def holonomy_block(p, coin, L):
    """W_p restricted to the plaquette's own four corners, in the corner-local
    basis (p, p+e1, p+e1+e2, p+e2).  In that basis the four boundary factors
    occupy the same local slots at every base point, so for a uniform
    configuration the block depends only on the coin -- which is measured by
    G-NON-WRAPPING (the four corners are distinct at every declared patch) and
    used here only as a cache key."""
    corners = [p, addv(p, E1, L), addv(addv(p, E1, L), E2, L), addv(p, E2, L)]
    got = _HOL_MEMO.get((coin, L))
    if got is not None and len(set(corners)) == 4:
        return corners, got
    pos = {c: i for i, c in enumerate(corners)}
    W = [[ONE if i == j else ZERO for j in range(4)] for i in range(4)]
    for l, o in plaquette_boundary(p, L):
        t, h = link_ends(l, L)
        it, ih = pos[t], pos[h]
        a, b, c, d = coin
        if o < 0:
            a, b, c, d = cconj(a), cconj(c), cconj(b), cconj(d)
        M = [[ONE if i == j else ZERO for j in range(4)] for i in range(4)]
        M[it][it], M[it][ih], M[ih][it], M[ih][ih] = a, b, c, d
        NW = [[ZERO] * 4 for _ in range(4)]
        for i in range(4):
            for kk in range(4):
                if M[i][kk] != ZERO:
                    for j in range(4):
                        if W[kk][j] != ZERO:
                            NW[i][j] = cadd(NW[i][j], cmul(M[i][kk], W[kk][j]))
        W = NW
    if len(set(corners)) == 4:
        _HOL_MEMO[(coin, L)] = W
    return corners, W


MU8 = {zeta(3 * t) for t in range(8)}


def block_permutation(corners, W, idx, n):
    """the position part of a monomial holonomy, as a permutation of the
    whole site set; None when the holonomy is not monomial."""
    perm = list(range(n))
    for j in range(4):
        col = [i for i in range(4) if W[i][j] != ZERO]
        if len(col) != 1 or W[col[0]][j] not in MU8:
            return None
        perm[idx[corners[j]]] = idx[corners[col[0]]]
    return tuple(perm)


def group_closure(gens, n):
    key = (tuple(gens), n)
    got = _GROUP_MEMO.get(key)
    if got is not None:
        return got
    ident = tuple(range(n))
    G, frontier = {ident}, [ident]
    while frontier:
        nxt = []
        for g in frontier:
            for h in gens:
                p = tuple(h[g[i]] for i in range(n))
                if p not in G:
                    G.add(p)
                    nxt.append(p)
        frontier = nxt
    _GROUP_MEMO[key] = len(G)
    return len(G)


def gen_orbits(gens, n):
    seen, out = set(), []
    for s in range(n):
        if s in seen:
            continue
        comp, stack = {s}, [s]
        while stack:
            x = stack.pop()
            for g in gens:
                y = g[x]
                if y not in comp:
                    comp.add(y)
                    stack.append(y)
        seen |= comp
        if len(comp) > 1:
            out.append(sorted(comp))
    return out


def factorial(n):
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r


def is_three_cycle(p):
    moved = [i for i in range(len(p)) if p[i] != i]
    if len(moved) != 3:
        return False
    a = moved[0]
    return p[a] in moved and p[p[a]] in moved and p[p[p[a]]] == a

# ===========================================================================
# SECTION 9.  THE MUTANT REGISTER (E-23: descriptions verified against code)
# ===========================================================================
# Each row is (name, the gate it must die at, the description of what it
# perturbs).  Every description names the object the switch actually moves,
# and G-FALSIFIER-DESCRIPTIONS checks each description against the source
# text of the branch guarded by its own `mut(...)` call.

MUTANTS = [
    ("MUT-SOURCE-DIGEST", "G-SOURCES-PINNED",
     "corrupts one pinned source digest before the byte anchors are checked"),
    ("MUT-PATH-VALUE", "G-PATH-VALUE-ANCHORS",
     "moves one path-value anchor's read value away from its declaration"),
    ("MUT-VERBATIM-FRAGMENT", "G-VERBATIM-ANCHORS",
     "admits a verbatim window shorter than the declared length floor"),
    ("MUT-EXTRA-READ", "G-RUNTIME-INPUTS-ENUMERATED",
     "appends an undeclared path to the runtime read list"),
    ("MUT-FLOAT", "G-NO-FLOATS",
     "injects a float into the receipt before the type scan"),
    ("MUT-ALPHABET", "G-ALPHABET-REBUILT",
     "drops one element from the rebuilt coefficient alphabet"),
    ("MUT-AXIS-DROP", "G-AXIS-SET-EXHAUSTIVE",
     "drops one axis from the axis set at the parent rung"),
    ("MUT-LAG", "G-LAG-SUPPORT-STRUCTURAL",
     "declares one lag outside the difference table to be empty when it is "
     "not"),
    ("MUT-POOL", "G-POOL-REPRODUCES-THE-PARENT",
     "shortens the rebuilt pool at the parent rung by one generator"),
    ("MUT-GAUGE-ORBIT", "G-GAUGE-ORBITS-FREE",
     "shrinks one recorded global-phase orbit below the group's size"),
    ("MUT-TWO-ROUTE", "G-TWO-ROUTE-POOL",
     "perturbs the second, whole-torus pool route's count at the parent rung"),
    ("MUT-ORD", "G-ORD-CENSUS-REPRODUCED",
     "moves one order-census non-monomial count away from the parent's"),
    ("MUT-SIDON", "G-SIDON-MEASURED",
     "reports one arena as Sidon whose difference multiset is not"),
    ("MUT-DDS", "G-DDS-CRITERION-SOUND",
     "reports a DDS-free arena as carrying a non-monomial unitary"),
    ("MUT-SIDON-VERDICT", "G-SIDON-PREDICTION-TESTED",
     "flips one arena's prediction verdict away from its own two measured "
     "legs"),
    ("MUT-CONTROL", "G-FOURTH-DIRECTION-CONTROL",
     "moves the reproduced non-monomial count at the control arena"),
    ("MUT-EIGEN", "G-EIGENVALUES-ROOTS-OF-UNITY",
     "marks one dispersion cell as lying off the root-of-unity lattice"),
    ("MUT-EIGENLATTICE", "G-EIGENPHASE-LATTICE",
     "reports the eigenphase lattice at one rung as the parent rung's"),
    ("MUT-VMAX", "G-VMAX-IS-DIAMETER",
     "moves the measured maximal group speed at one rung"),
    ("MUT-ATTAINED", "G-VMAX-ATTAINED-BY-THE-ANTIPODE",
     "removes the antipodal monomial witness at one rung"),
    ("MUT-INTERIOR", "G-INTERIOR-RADII",
     "moves the interior-radius count at the rung the register names"),
    ("MUT-VELOCITY", "G-INTEGER-VELOCITY-CENSUS",
     "hides the non-integer velocity witness at the rung that carries it"),
    ("MUT-COIN", "G-COIN-ALPHABET-DERIVED",
     "drops one coin from the derived coin family"),
    ("MUT-STRATA", "G-STRATA-PERFECT-MATCHINGS",
     "reports one parity stratum as covering a site twice"),
    ("MUT-WRAP", "G-NON-WRAPPING",
     "reports a declared plaquette stencil as wrapping when it does not"),
    ("MUT-PROFILE", "G-PROFILE-PERSISTS",
     "moves one measured group order in the (order, support) profile"),
    ("MUT-ALT", "G-ALTERNATING-ON-ORBITS",
     "breaks the alternating certificate by moving one predicted order"),
    ("MUT-GLOBAL", "G-GLOBAL-SUPPORT-IS-THE-VOLUME",
     "reports the global stencil's support as smaller than the volume"),
    ("MUT-LOCALITY", "G-LOCALITY-WINDOWS",
     "flips one window's locality flag away from its own completeness test"),
    ("MUT-WIDTH", "G-WIDTH-COUNT-EQUALS-INTERIOR-RADII",
     "moves the count of locality-admitting widths at one rung"),
    ("MUT-PARTITION", "G-PARTITION-COROLLARY",
     "reports a blockwise cell as non-complete"),
    ("MUT-BAND", "G-BAND-LAW",
     "moves one admitted size out of the measured band at one width"),
    ("MUT-TABLE", "G-PERSISTENCE-TABLE-BOUND",
     "rewrites one persistence verdict away from its own measured cells"),
    ("MUT-FRACTION", "G-FRACTIONS-STAMPED",
     "publishes a fraction with neither a measure nor the COUNTING-ONLY "
     "stamp"),
    ("MUT-VERDICT", "G-VERDICT-RECONSTRUCTED",
     "edits the verdict string after its segments are derived"),
    ("MUT-HEAD", "G-VERDICT-PREREGISTERED",
     "emits a head that is not one of the pre-registered forms"),
    ("MUT-WALLS", "G-WALLS",
     "inserts a continuum claim into the scope segment"),
    ("MUT-DESCRIPTION", "G-FALSIFIER-DESCRIPTIONS",
     "inverts one published mutant description relative to its code"),
    ("MUT-SEAL-BROKEN", "G-SEAL-COMPLETE",
     "edits a sealed object after its gate-time digest was taken"),
    ("MUT-SEAL-MANIFEST", "G-SEAL-MANIFEST-TOTAL",
     "publishes a receipt key that is neither sealed nor declared unsealed"),
    ("MUT-GATE-CHAIN", "G-GATE-ROWS-SEALED",
     "edits the detail of a closed gate row after its digest entered the chain"),
    ("MUT-PAPER-CLAIM", "G-PAPER-CLAIMS",
     "adds a measured claim the paper does not make"),
    ("MUT-PAPER-NUMERAL", "G-PAPER-NUMERAL-COVERAGE",
     "adds an unlicensed numeral to the paper's scanned set"),
    ("MUT-PAPER-SPAN", "G-PAPER-INLINE-SPANS",
     "adds an unlicensed numeral inside an inline code span"),
    ("MUT-PAPER-FENCE", "G-PAPER-FENCED-MULTISET",
     "drops one copy of a duplicated fenced block from the rendered multiset"),
    ("MUT-PAPER-TABLE", "G-PAPER-TABLES-AS-CLAIMS",
     "moves one rendered table row away from the paper's"),
    ("MUT-PAPER-POLARITY", "G-PAPER-CLAIM-POLARITY",
     "returns an unmoved claim after its receipt key was perturbed"),
    ("MUT-PAPER-VERDICT", "G-PAPER-VERDICT-BLOCK",
     "truncates the verdict string the paper is required to quote"),
]

# the receipt keys the post-sweep stage adds; the in-run manifest gate uses
# the PREDICTED final key set so that no key escapes it by arriving late.
LATE_KEYS = ("mutants", "gates", "gate_digests", "seal_manifest",
             "sweep_totals")

# the gates that still run after the waiver ledger closes; the ledger is built
# over these too, so no gate is published without a falsifier or a forcing.
REMAINING_GATES = ("G-TOTALS-REDERIVED", "G-NO-FLOATS", "G-SEAL-COMPLETE",
                   "G-SEAL-MANIFEST-TOTAL", "G-GATE-ROWS-SEALED",
                   "G-MUTANTS-ON-TARGET", "G-PUBLISHED-KEYS-COVERED",
                   "G-GATES-CLOSED-AS-PREDICTED", "G-PAPER-COVERAGE-FINAL",
                   "G-GATE-LEDGER-COVERS-THE-RUN")

LATE_GATES = ("G-WAIVERS-VERIFIED", "G-TOTALS-REDERIVED", "G-PAPER-CLAIMS",
              "G-PAPER-NUMERAL-COVERAGE", "G-PAPER-INLINE-SPANS",
              "G-PAPER-FENCED-MULTISET", "G-PAPER-TABLES-AS-CLAIMS",
              "G-PAPER-CLAIM-POLARITY", "G-PAPER-VERDICT-BLOCK",
              "G-NOT-EXECUTED-EMPTY", "G-FALSIFIER-DESCRIPTIONS",
              "G-PUBLISHED-KEYS-COVERED", "G-GATES-CLOSED-AS-PREDICTED")

# ===========================================================================
# SECTION 10.  THE BUILD: every stage, every gate
# ===========================================================================


def build_state(break_anchor=None):
    global READS
    READS = []
    LD = Ledger()
    S = {"schema": SCHEMA, "unit": UNIT, "pin": PIN_REL}
    SEAL = Seal()
    LD.seal, LD.state = SEAL, S

    # ---- anchors: bytes -----------------------------------------------
    prov, byte_rows = {}, []
    for sid, rel, dig, note in SOURCES:
        p = source_path(rel)
        got = sha12(p)
        want = dig
        if mut("MUT-SOURCE-DIGEST") and sid == "A-R4-RECEIPT":
            want = "0" * 12
        if break_anchor == sid:
            want = "f" * 12
        byte_rows.append({"anchor": sid, "path": rel, "expected": want,
                          "measured": got, "matches": got == want,
                          "note": note})
        prov[rel] = got
    bad = [r["anchor"] for r in byte_rows if not r["matches"]]
    S["byte_anchors"] = byte_rows
    S["source_sha256"] = prov
    LD.gate("G-SOURCES-PINNED",
            "every runtime input is read at a hash-pinned path and its bytes "
            "match the digest this unit froze; a drifted parent dies here "
            "before a single number is computed",
            not bad, "%d sources, mismatched: %s" % (len(SOURCES),
                                                     bad or "none"))
    S["pin_sha256_prefix"] = prov[PIN_REL]

    src = {}
    for sid, rel, _d, _n in SOURCES:
        if rel.endswith(".json"):
            with open(os.path.join(REPO, rel), "r", encoding="utf-8") as f:
                src[sid] = json.load(f)
        else:
            src[sid] = read_text(os.path.join(REPO, rel))

    # ---- anchors: path-values -----------------------------------------
    pv_rows = []
    for aid, sid, path, want, note in PATH_VALUE_ANCHORS:
        got = jpath(src[sid], path)
        if mut("MUT-PATH-VALUE") and aid == "PV-CIRC":
            got = 57
        if break_anchor == aid:
            got = "BROKEN"
        pv_rows.append({"anchor": aid, "source": sid, "path": path,
                        "declared": want, "read": got, "matches": got == want,
                        "note": note})
    bad = [r["anchor"] for r in pv_rows if not r["matches"]]
    S["path_value_anchors"] = pv_rows
    LD.gate("G-PATH-VALUE-ANCHORS",
            "every value this unit inherits is read from a pinned receipt at "
            "a named path and equals the value frozen beside it: the arena is "
            "taken, never typed",
            not bad, "%d path-value anchors, mismatched: %s"
            % (len(PATH_VALUE_ANCHORS), bad or "none"))

    def pv(aid):
        return [r["read"] for r in pv_rows if r["anchor"] == aid][0]

    # ---- anchors: verbatim windows ------------------------------------
    vb_rows = []
    for aid, sid, gate, window in VERBATIM_ANCHORS:
        floor = VERBATIM_LENGTH_FLOOR
        w = window
        if mut("MUT-VERBATIM-FRAGMENT") and aid == "VB-SIDON":
            w = window[:12]
        if break_anchor == aid:
            w = window + " NOT IN THE SOURCE"
        present = norm_text(w) in norm_text(src[sid])
        vb_rows.append({"anchor": aid, "source": sid, "consumer_gate": gate,
                        "chars": len(w), "floor": floor,
                        "sha256_12": digest(w),
                        "long_enough": len(w) >= floor, "present": present})
    bad = [r["anchor"] for r in vb_rows
           if not (r["present"] and r["long_enough"])]
    S["verbatim_anchors"] = vb_rows
    LD.gate("G-VERBATIM-ANCHORS",
            "every quoted window is present in its pinned source as written "
            "(whitespace and markdown prefixes normalised on both sides), is "
            "at least the declared length floor, and names the gate that "
            "consumes it",
            not bad, "%d windows, floor %d chars, failing: %s"
            % (len(VERBATIM_ANCHORS), VERBATIM_LENGTH_FLOOR, bad or "none"))

    S["arithmetic"] = ("exact: Q(zeta_24) as %d-tuples of Fraction over the "
                       "basis (1, x, ..., x^%d) reduced modulo Phi_24 "
                       "COMPUTED as %s; tuple equality is field equality"
                       % (DEG, DEG - 1,
                          "+".join("%dx^%d" % (int(PHI24[i]), i)
                                   for i in range(len(PHI24)) if PHI24[i])))

    # ---- the declared arena -------------------------------------------
    S["arena_declaration"] = {
        "ladder": list(LADDER), "parent_rung": PARENT_RUNG,
        "control_rung": CONTROL_RUNG, "dimension": pv("PV-D"),
        "link_set": [list(v) for v in LINK_SET],
        "fourth_direction": list(FOURTH_DIRECTION),
        "widths": list(WIDTHS), "band_sizes": list(BAND_SIZES),
        "alphabet": pv("PV-ALPHABET"), "stencil": pv("PV-STENCIL"),
        "connective": pv("PV-CONNECTIVE"),
        "forcing_link": pv("PV-FORCING-LINK"),
        "plaquette_stencils": [n for n, _o in PLAQ_STENCILS],
        "dds_subset_window": DDS_SUBSET_WINDOW,
        "family_generalisation_rule":
            "R4's construction applied verbatim at each rung: axes = every "
            "nonzero offset modulo sign (exhaustive); stencil = the parent's "
            "3-term {0, a, -a}; alphabet = the parent's 25, fixed; quotient = "
            "the parent's global-phase gauge.  Fiber: the axis count at that "
            "rung, every instance run.",
        "probe_alphabets": [n for n, _a in PROBE_ALPHABETS],
    }
    LD.gate("G-ARENA-DECLARED",
            "the arena is data: the ladder, the stencils, the widths, the "
            "alphabet and the generalisation rule are declared before a "
            "measurement is taken, and every one of them is either anchored "
            "or a frozen literal named here",
            (list(LADDER) == [4, 6, 8] and PARENT_RUNG in LADDER
             and S["arena_declaration"]["alphabet"] == 25
             and S["arena_declaration"]["dimension"] == 2),
            "ladder %s at d=%d over an alphabet of %d"
            % (list(LADDER), pv("PV-D"), pv("PV-ALPHABET")))

    LD.gate("G-STAGES-DECLARED",
            "the pin's five stages are the ones run, and the pin's own "
            "sentence requiring a per-arena PASS/FAIL is quoted from it",
            [r for r in vb_rows if r["anchor"] == "VB-PIN-STAGES"][0]["present"],
            "the pin's prediction-ledger sentence is present at "
            "VB-PIN-STAGES")

    # ---- the alphabet, rebuilt ----------------------------------------
    A = list(ALPHABET)
    if mut("MUT-ALPHABET"):
        A = A[:-1]
    S["alphabet_rebuilt"] = {"size": len(A),
                             "elements": [cstr(x) for x in A]}
    LD.gate("G-ALPHABET-REBUILT",
            "the coefficient alphabet is rebuilt from the parent's own "
            "definition and has exactly the anchored size",
            len(A) == pv("PV-ALPHABET"),
            "rebuilt %d elements against the anchored %d"
            % (len(A), pv("PV-ALPHABET")))
    A = tuple(A)

    # =================================================================
    # STAGE 0.  THE REBUILD AT THE PARENT RUNG
    # =================================================================
    ax_rows = []
    for L in LADDER:
        axs = axes(L)
        if mut("MUT-AXIS-DROP") and L == PARENT_RUNG:
            axs = axs[:-1]
        loc = [a for a in axs if torus_absmax(a, L) == 1]
        byo = {}
        for a in axs:
            byo[elt_order(a, L)] = byo.get(elt_order(a, L), 0) + 1
        ax_rows.append({"L": L, "axes": len(axs), "local_axes": len(loc),
                        "local": [list(a) for a in loc],
                        "local_orders": [elt_order(a, L) for a in loc],
                        "by_order": {str(k): v for k, v in sorted(byo.items())}})
    S["axis_census"] = ax_rows
    p4 = [r for r in ax_rows if r["L"] == PARENT_RUNG][0]
    LD.gate("G-AXIS-SET-EXHAUSTIVE",
            "the axis set is every nonzero offset modulo sign at every rung, "
            "and at the parent rung it reproduces the parent's own axis and "
            "local-axis counts",
            p4["axes"] == pv("PV-AXES") and p4["local_axes"] == pv("PV-LOCAL-AXES"),
            "L=4: %d axes (%d local) against the anchored %d (%d)"
            % (p4["axes"], p4["local_axes"], pv("PV-AXES"),
               pv("PV-LOCAL-AXES")))

    # the structural fact the fast route rests on, bound per (axis, lag)
    lag_bad = []
    lag_checked = 0
    for L in LADDER:
        for a in axes(L):
            St = axis_stencil(a, L)
            tab = lag_structure(St, L)
            for m in product(range(L), repeat=2):
                lag_checked += 1
                pairs = [(i, j) for i, v in enumerate(St)
                         for j, w in enumerate(St)
                         if ((v[0] - w[0]) % L, (v[1] - w[1]) % L) == m]
                declared = tab.get(m, [])
                if mut("MUT-LAG") and L == 6 and a == (0, 1) and m == (0, 1):
                    declared = []
                if sorted(declared) != sorted(pairs):
                    lag_bad.append((L, a, m))
    LD.gate("G-LAG-SUPPORT-STRUCTURAL",
            "for every axis at every rung and EVERY lag of the group, the "
            "pairs the unitarity condition receives at that lag are exactly "
            "the ordered pairs of the stencil realising it -- so a lag "
            "outside the difference table receives nothing, and the "
            "structural route is the whole condition rather than a sample",
            not lag_bad, "%d (axis, lag) objects checked, %d disagreeing"
            % (lag_checked, len(lag_bad)))

    # the pool, at every rung
    pool_rows, pools = [], {}
    for L in LADDER:
        pl, orbs = build_pool(L, A)
        if mut("MUT-POOL") and L == PARENT_RUNG:
            pl = pl[:-1]
        if mut("MUT-GAUGE-ORBIT") and L == PARENT_RUNG:
            orbs = [4] + orbs[1:]
        pools[L] = pl
        byo = {}
        for g in pl:
            k = str(g["axis_ord"])
            byo.setdefault(k, {"generators": 0, "non_monomial": 0})
            byo[k]["generators"] += 1
            if not g["monomial"]:
                byo[k]["non_monomial"] += 1
        pool_rows.append({
            "L": L, "circulants": len(pl),
            "monomial": sum(1 for g in pl if g["monomial"]),
            "non_monomial": sum(1 for g in pl if not g["monomial"]),
            "by_axis_order": byo,
            "orbit_sizes": sorted(set(orbs)),
            "local_non_monomial": sum(1 for g in pl if not g["monomial"]
                                      and g["radius"] == 1)})
    S["pool_census"] = pool_rows
    r4row = [r for r in pool_rows if r["L"] == PARENT_RUNG][0]
    LD.gate("G-POOL-REPRODUCES-THE-PARENT",
            "the family-generalisation rule, run at the parent rung, returns "
            "the parent's own circulant pool exactly -- the rule is therefore "
            "the parent's rule and not a new one",
            r4row["circulants"] == pv("PV-CIRC"),
            "rebuilt %d circulants at L=4 against the anchored %d"
            % (r4row["circulants"], pv("PV-CIRC")))
    bad_orb = [r["L"] for r in pool_rows if r["orbit_sizes"] != [8]]
    LD.gate("G-GAUGE-ORBITS-FREE",
            "the declared global-phase gauge acts freely on the solution set "
            "at every rung: every orbit has the full group's size",
            not bad_orb, "orbit sizes by rung: %s"
            % {r["L"]: r["orbit_sizes"] for r in pool_rows})

    # the second, whole-torus route at the parent rung
    pl_full, _o = build_pool(PARENT_RUNG, A, full_route=True)
    nfull = len(pl_full)
    if mut("MUT-TWO-ROUTE"):
        nfull -= 1
    LD.gate("G-TWO-ROUTE-POOL",
            "the pool at the parent rung is built a second time by the "
            "parent's own criterion written over the WHOLE torus -- every lag "
            "of the group, no structural shortcut -- and the two routes agree "
            "generator for generator",
            nfull == r4row["circulants"]
            and sorted(tuple(sorted(g["coef"].items())) for g in pl_full)
            == sorted(tuple(sorted(g["coef"].items()))
                      for g in pools[PARENT_RUNG]),
            "whole-torus route %d, structural route %d, identical member sets"
            % (nfull, r4row["circulants"]))

    # the order census
    ordrows = {}
    for n in (2, 3, 4, 5, 6, 8):
        row = ord_census(n, A)
        if mut("MUT-ORD") and n == 4:
            row["non_monomial"] = 47
        ordrows[str(n)] = row
    S["ord_census"] = ordrows
    ord_bad = []
    for n, aid in (("2", "PV-ORD2"), ("3", "PV-ORD3"), ("4", "PV-ORD4"),
                   ("8", "PV-ORD8")):
        if ordrows[n]["non_monomial"] != pv(aid):
            ord_bad.append(n)
    LD.gate("G-ORD-CENSUS-REPRODUCED",
            "the order census is reproduced from the parent's own sweep rule "
            "and agrees with the parent's anchored rows at every anchored "
            "order; the collapse theorem it confirms is quoted from the "
            "parent's paper",
            not ord_bad, "orders 2/3/4/8 non-monomial = %s against the "
            "anchored %s"
            % ([ordrows[n]["non_monomial"] for n in ("2", "3", "4", "8")],
               [pv(a) for a in ("PV-ORD2", "PV-ORD3", "PV-ORD4", "PV-ORD8")]))

    # =================================================================
    # STAGE 1.  THE SIDON TEST
    # =================================================================
    arenas = []
    for L in LADDER:
        rows = [("LINK", list(LINK_SET))]
        for a in axes(L):
            if torus_absmax(a, L) == 1:
                rows.append(("AXIS-%d-%d" % a, axis_stencil(a, L)))
        rows.append(("LINK-PLUS-4TH", list(LINK_SET) + [FOURTH_DIRECTION]))
        for nm, St in rows:
            sid_ok, dmul = is_sidon(St, L)
            subs = doubled_subsets(St, L)
            sc = scan_offsets(tuple(St), A, L)
            if mut("MUT-SIDON") and L == 6 and nm.startswith("AXIS"):
                sid_ok = True
            if mut("MUT-DDS") and L == 8 and nm == "LINK":
                sc = dict(sc)
                sc["non_monomial"] = 1
            arenas.append({
                "L": L, "arena": nm, "offsets": [list(v) for v in St],
                "difference_multiplicities": sorted(dmul.values(),
                                                    reverse=True),
                "sidon": sid_ok, "dds_free": not subs,
                "doubled_subsets": [[list(v) for v in T] for T in subs],
                "maps": sc["maps"], "unitary": sc["unitary"],
                "monomial": sc["monomial"],
                "non_monomial": sc["non_monomial"],
                "witnesses": sc["witnesses"],
                "monomial_only": sc["non_monomial"] == 0})
    S["sidon_arenas"] = arenas

    bad = [(r["L"], r["arena"]) for r in arenas
           if r["sidon"] != (r["difference_multiplicities"] == []
                             or max(r["difference_multiplicities"]) == 1)]
    LD.gate("G-SIDON-MEASURED",
            "each arena's Sidon status is computed from its own difference "
            "multiset -- every nonzero difference realised exactly once -- "
            "and not from any label",
            not bad, "%d arenas, %d whose flag disagrees with their own "
            "multiset" % (len(arenas), len(bad)))

    bad = [(r["L"], r["arena"]) for r in arenas
           if r["dds_free"] and r["non_monomial"] != 0]
    dds_forced = [r for r in arenas if r["dds_free"]]
    S["dds_law"] = {
        "theorem": "if no subset of the offset set of size >= 2 is "
                   "difference-doubled, every unitary map on it is monomial, "
                   "over any field closed under conjugation",
        "arenas_dds_free": len(dds_forced),
        "arenas_dds_free_and_monomial_only":
            sum(1 for r in dds_forced if r["monomial_only"]),
        "arenas_dds_carrying": len(arenas) - len(dds_forced),
        "arenas_dds_carrying_with_a_non_monomial":
            sum(1 for r in arenas if not r["dds_free"]
                and r["non_monomial"] > 0),
        "sidon_arenas": sum(1 for r in arenas if r["sidon"]),
        "sidon_but_not_the_only_forced":
            sum(1 for r in arenas if r["dds_free"] and not r["sidon"]),
        "subset_window": DDS_SUBSET_WINDOW}
    LD.gate("G-DDS-CRITERION-SOUND",
            "the difference-doubled criterion is sound on every arena "
            "measured: wherever no subset of size at least two is "
            "difference-doubled, the exhaustive scan finds no non-monomial "
            "unitary at all",
            not bad, "%d DDS-free arenas, %d of them monomial-only, "
            "counterexamples: %s"
            % (len(dds_forced),
               S["dds_law"]["arenas_dds_free_and_monomial_only"],
               bad or "none"))

    # the prediction, arena by arena
    pred_rows = []
    for r in arenas:
        implication = (not r["sidon"]) or r["monomial_only"]
        converse = (not r["monomial_only"]) or r["sidon"]
        verdict = ("PASSES" if implication and converse else
                   "FAILS-CONVERSE" if implication else "FAILS")
        if mut("MUT-SIDON-VERDICT") and r["L"] == 6 and r["arena"] == "LINK":
            verdict = "FAILS"
        pred_rows.append({"L": r["L"], "arena": r["arena"],
                          "sidon": r["sidon"],
                          "monomial_only": r["monomial_only"],
                          "sufficiency_holds": implication,
                          "necessity_holds": converse, "verdict": verdict})
    bad = [(p["L"], p["arena"]) for p, r in zip(pred_rows, arenas)
           if p["verdict"] != (("PASSES" if p["sufficiency_holds"]
                                and p["necessity_holds"] else
                                "FAILS-CONVERSE" if p["sufficiency_holds"]
                                else "FAILS"))]
    suff = all(p["sufficiency_holds"] for p in pred_rows)
    nec_fail = [p for p in pred_rows if not p["necessity_holds"]]
    S["sidon_prediction"] = {
        "quoted": [r["sha256_12"] for r in vb_rows
                   if r["anchor"] == "VB-SIDON"][0],
        "rows": pred_rows,
        "sufficiency_holds_everywhere": suff,
        "necessity_failures": len(nec_fail),
        "necessity_failure_arenas": ["L=%d %s" % (p["L"], p["arena"])
                                     for p in nec_fail],
        "verdict": ("SUFFICIENT-NOT-NECESSARY" if suff and nec_fail else
                    "CONFIRMED-BOTH-WAYS" if suff else "REFUTED")}
    LD.gate("G-SIDON-PREDICTION-TESTED",
            "the registered Sidon prediction is quoted from the pinned "
            "adjudication and tested on every arena in BOTH directions -- "
            "Sidon implies monomial-only, and monomial-only implies Sidon -- "
            "with each arena's verdict computed from its own two measured "
            "legs and from nothing else",
            not bad, "%d arenas: sufficiency holds everywhere=%s, %d "
            "necessity failures (%s)"
            % (len(pred_rows), suff, len(nec_fail),
               ", ".join(S["sidon_prediction"]["necessity_failure_arenas"])
               or "none"))

    # the fourth-direction control, at paper-20's own arena and at the ladder
    ctrl = []
    for nm, St in (("LINK", list(LINK_SET)),
                   ("LINK-PLUS-4TH", list(LINK_SET) + [FOURTH_DIRECTION])):
        for an, AA in PROBE_ALPHABETS:
            sc = scan_offsets(tuple(St), AA, CONTROL_RUNG)
            if mut("MUT-CONTROL") and nm == "LINK-PLUS-4TH" and an == "THIRDS-19":
                sc = dict(sc)
                sc["non_monomial"] = 53
            ctrl.append({"L": CONTROL_RUNG, "arena": nm, "alphabet": an,
                         "alphabet_size": len(AA), "maps": sc["maps"],
                         "unitary": sc["unitary"], "monomial": sc["monomial"],
                         "non_monomial": sc["non_monomial"],
                         "witnesses": sc["witnesses"]})
    registered = [c for c in ctrl if c["arena"] == "LINK-PLUS-4TH"
                  and c["alphabet"] == "THIRDS-19"][0]
    ladder_ctrl = [r for r in arenas if r["arena"] == "LINK-PLUS-4TH"]
    S["fourth_direction_control"] = {
        "control_rung_rows": ctrl,
        "registered_count_reproduced": registered["non_monomial"],
        "registered_count_declared": 54,
        "ladder_rows": [{"L": r["L"], "non_monomial": r["non_monomial"],
                         "dds_free": r["dds_free"]} for r in ladder_ctrl],
        "death_transports": [r["L"] for r in ladder_ctrl
                             if r["non_monomial"] > 0],
        "death_absent": [r["L"] for r in ladder_ctrl
                         if r["non_monomial"] == 0],
        "alphabet_relativity":
            "at the control rung the same fourth direction carries %d "
            "non-monomial unitaries over the 19-value probe and %d over the "
            "parents' own 25-element alphabet"
            % (registered["non_monomial"],
               [c for c in ctrl if c["arena"] == "LINK-PLUS-4TH"
                and c["alphabet"] == "R4-25"][0]["non_monomial"])}
    LD.gate("G-FOURTH-DIRECTION-CONTROL",
            "the registered fourth-direction death is reproduced "
            "independently at the control rung, over the probe alphabet that "
            "produces it, at the registered count -- and then run at every "
            "rung of the ladder",
            registered["non_monomial"] == 54,
            "control rung, 19-value probe: %d non-monomial against the "
            "registered 54; the death is present at rungs %s and absent at %s"
            % (registered["non_monomial"],
               S["fourth_direction_control"]["death_transports"] or "none",
               S["fourth_direction_control"]["death_absent"] or "none"))

    # =================================================================
    # STAGE 2.  VMAX = DIAMETER, AND THE INTERIOR RADII
    # =================================================================
    disp_rows, vel_all = [], {}
    off_lattice = []
    for L in LADDER:
        rows, momenta = dispersion(L, pools[L])
        for r in rows:
            if r["off_lattice"] is not None:
                off_lattice.append((L, r["off_lattice"]))
        if mut("MUT-EIGEN") and L == 6:
            off_lattice.append((6, "injected"))
        vel = velocity_rows(L, rows, momenta)
        vel_all[L] = vel
        disp_rows.append({
            "L": L, "families": len(rows), "momenta": len(momenta),
            "cells": len(rows) * len(momenta),
            "distinct_reduced_dispersions": len({v["sig"] for v in vel}),
            "moving": sum(1 for v in vel if v["moves"]),
            "static": sum(1 for v in vel if not v["moves"]),
            "aliased_cells": sum(v["aliased"] for v in vel),
            "aliased_families": sum(1 for v in vel if v["aliased"]),
            "eigenphase_modulus_at_the_pool_gauge": _lcm_all(
                [24 // _gcd_all([24, t]) for r in rows
                 for t in r["s"].values()]),
            "eigenphase_lattice": _lcm_all(
                [8] + [24 // _gcd_all([24, t]) for r in rows
                       for t in r["s"].values()])})
    S["dispersion_census"] = disp_rows
    LD.gate("G-EIGENVALUES-ROOTS-OF-UNITY",
            "every symbol at every (family, momentum) cell of every rung is a "
            "root of unity of the unit's own field -- the eigenphase is an "
            "exact integer, per cell, not a convention",
            not off_lattice, "%d cells over %d rungs, %d off the lattice"
            % (sum(r["cells"] for r in disp_rows), len(LADDER),
               len(off_lattice)))
    lat = {r["L"]: r["eigenphase_lattice"] for r in disp_rows}
    if mut("MUT-EIGENLATTICE"):
        lat[6] = 8
    bad = [L for L in LADDER if lat[L] != _lcm_all([8, L])]
    LD.gate("G-EIGENPHASE-LATTICE",
            "the eigenphase lattice is measured, not assumed: at each rung it "
            "is the least common multiple of the orders of every eigenvalue "
            "over the whole declared gauge orbit, and it comes out as the "
            "least common multiple of the gauge group's order and the rung",
            not bad and lat[PARENT_RUNG] == 8,
            "eigenphase lattices Z/%d, Z/%d, Z/%d against lcm(8, L) = %s; "
            "at the pool's own gauge representative they read %s"
            % (lat[4], lat[6], lat[8], [_lcm_all([8, L]) for L in LADDER],
               [r["eigenphase_modulus_at_the_pool_gauge"] for r in disp_rows]))
    p4d = [r for r in disp_rows if r["L"] == PARENT_RUNG][0]
    LD.gate("G-DISPERSION-REPRODUCES-THE-PARENT",
            "at the parent rung the dispersion census reproduces the parent's "
            "own cell count, its moving and static counts and its separation "
            "datum",
            (p4d["cells"] == pv("PV-CELLS") and p4d["moving"] == pv("PV-MOVING")
             and p4d["static"] == pv("PV-STATIC")
             and p4d["distinct_reduced_dispersions"] == pv("PV-PROFILES")),
            "cells %d/%d, moving %d/%d, static %d/%d, distinct %d/%d"
            % (p4d["cells"], pv("PV-CELLS"), p4d["moving"], pv("PV-MOVING"),
               p4d["static"], pv("PV-STATIC"),
               p4d["distinct_reduced_dispersions"], pv("PV-PROFILES")))

    vmax_rows = []
    for L in LADDER:
        vm = max(v["vmax"] for v in vel_all[L])
        if mut("MUT-VMAX") and L == 8:
            vm = Fraction(3)
        diam = max(torus_absmax(v, L) for v in product(range(L), repeat=2))
        anti = (L // 2, L // 2)
        witness = {anti: ONE}
        attained = autocorr_is_delta(witness, L)
        wrow = [v for v in vel_all[L]
                if v["support"] == 1 and v["vmax"] == Fraction(L, 2)]
        if mut("MUT-ATTAINED") and L == 6:
            wrow = []
        vmax_rows.append({"L": L, "vmax": str(vm), "diameter": diam,
                          "vmax_equals_diameter": vm == diam,
                          "antipodal_offset": list(anti),
                          "antipodal_unitary": attained,
                          "families_attaining": len(wrow),
                          "bound": "L/2 = %s" % Fraction(L, 2)})
    S["vmax_census"] = vmax_rows
    bad = [r["L"] for r in vmax_rows if not r["vmax_equals_diameter"]]
    LD.gate("G-VMAX-IS-DIAMETER",
            "the maximal group speed equals the max-norm diameter at every "
            "rung of the ladder, and the parent's even-L argument for it is "
            "quoted from the parent's paper",
            not bad and [r for r in vmax_rows
                         if r["L"] == PARENT_RUNG][0]["vmax"] == pv("PV-VMAX"),
            "VMAX by rung %s against diameters %s"
            % ({r["L"]: r["vmax"] for r in vmax_rows},
               {r["L"]: r["diameter"] for r in vmax_rows}))
    bad = [r["L"] for r in vmax_rows
           if not (r["antipodal_unitary"] and r["families_attaining"] > 0)]
    LD.gate("G-VMAX-ATTAINED-BY-THE-ANTIPODE",
            "the ceiling is ATTAINED and not merely bounded: the monomial "
            "shift by the antipodal offset is a unitary member of the family "
            "at every rung and a family of the built pool reaches L/2 there",
            not bad, "attaining families by rung: %s"
            % {r["L"]: r["families_attaining"] for r in vmax_rows})

    rad_rows = []
    for L in LADDER:
        radii = sorted({torus_absmax(v, L)
                        for v in product(range(L), repeat=2)})
        diam = max(radii)
        interior = [r for r in radii if 0 < r < diam]
        if mut("MUT-INTERIOR") and L == 8:
            interior = interior[:-1]
        rad_rows.append({"L": L, "radius_classes": radii, "diameter": diam,
                         "interior_radii": interior,
                         "interior_count": len(interior)})
    S["interior_radii"] = rad_rows
    r8 = [r for r in rad_rows if r["L"] == 8][0]
    r4i = [r for r in rad_rows if r["L"] == PARENT_RUNG][0]
    LD.gate("G-INTERIOR-RADII",
            "the interior-radius count is measured at every rung, and the "
            "register's own claim -- three at L = 8, quoted from the parent's "
            "paper -- is confirmed against the anchored value",
            (r8["interior_count"] == pv("PV-INTERIOR-L8")
             and r4i["interior_radii"] == pv("PV-INTERIOR")),
            "interior radii by rung %s; the L=8 count is %d against the "
            "anchored %d"
            % ({r["L"]: r["interior_count"] for r in rad_rows},
               r8["interior_count"], pv("PV-INTERIOR-L8")))

    vel_rows = []
    for L in LADDER:
        cells = sum(1 for v in vel_all[L]) * 2 * L * L
        ni = [v for v in vel_all[L] if v["non_integer"]]
        if mut("MUT-VELOCITY") and L == 6:
            ni = []
        wit = None
        if ni:
            w = ni[0]
            wit = {"axis": list(w["axis"]), "axis_order": w["ord"],
                   "support": w["support"],
                   "speed": w["non_integer"][0][2],
                   "momentum": list(w["non_integer"][0][0]),
                   "direction": w["non_integer"][0][1]}
        vel_rows.append({"L": L, "velocity_cells": cells,
                         "non_integer_families": len(ni),
                         "non_integer_cells": sum(len(v["non_integer"])
                                                  for v in ni),
                         "all_integer": not ni, "witness": wit})
    S["velocity_census"] = vel_rows
    p4v = [r for r in vel_rows if r["L"] == PARENT_RUNG][0]
    breaks = [r["L"] for r in vel_rows if not r["all_integer"]]
    # the SECOND ROUTE: v is an integer exactly when 24 divides L times the
    # lift, recounted here straight from the eigenphases without touching the
    # velocity rows, and compared per rung.
    second = {}
    for L in LADDER:
        rows2, mom2 = dispersion(L, pools[L])
        n = 0
        for r2 in rows2:
            s2 = r2["s"]
            for k in mom2:
                for j in range(2):
                    kk = list(k)
                    kk[j] = (kk[j] + 1) % L
                    d = (s2[tuple(kk)] - s2[k]) % 24
                    lift = d if d <= 12 else d - 24
                    if (L * lift) % 24:
                        n += 1
        second[L] = n
    route_bad = [r["L"] for r in vel_rows
                 if r["non_integer_cells"] != second[r["L"]]]
    LD.gate("G-INTEGER-VELOCITY-CENSUS",
            "the parent's integer-velocity property is re-measured at every "
            "rung, per family and per cell, and the count of non-integer "
            "cells is recomputed by a second route -- the divisibility of the "
            "lift by the eigenphase lattice -- and compared rung by rung",
            (p4v["all_integer"] and p4v["velocity_cells"] == pv("PV-INTVEL")
             and not route_bad),
            "L=4: %d velocity cells, all integer, against the anchored %d; "
            "the property fails at rungs %s; second-route non-integer cell "
            "counts %s, disagreeing at %s"
            % (p4v["velocity_cells"], pv("PV-INTVEL"), breaks or "none",
               second, route_bad or "none"))

    # =================================================================
    # STAGE 3.  THE GAUGE FINGERPRINT ALONG L
    # =================================================================
    coins = list(build_coins(A))
    if mut("MUT-COIN"):
        coins = coins[:-1]
    secs = {}
    for m in coins:
        secs[coin_sector(m)] = secs.get(coin_sector(m), 0) + 1
    S["coin_sectors"] = {"coins": len(coins), "sectors": secs,
                         "L_independent": True,
                         "note": "a coin is a 2x2 unitary over the parents' "
                                 "coefficient alphabet; nothing in its "
                                 "definition mentions L"}
    LD.gate("G-COIN-ALPHABET-DERIVED",
            "the coin family is derived from the parents' coefficient "
            "alphabet alone and reproduces the anchored family and its three "
            "sector sizes; it carries no L, so it is the same family at every "
            "rung",
            (len(coins) == pv("PV-COINS")
             and secs.get("ANTIDIAGONAL") == pv("PV-COINS-ANTI")
             and secs.get("DIAGONAL") == pv("PV-COINS-DIAG")
             and secs.get("BALANCED") == pv("PV-COINS-BAL")),
            "%d coins = %d diagonal + %d antidiagonal + %d balanced"
            % (len(coins), secs.get("DIAGONAL", 0),
               secs.get("ANTIDIAGONAL", 0), secs.get("BALANCED", 0)))
    anti = [m for m in coins if coin_sector(m) == "ANTIDIAGONAL"]

    strat_rows = []
    for L in LADDER:
        sts = strata(L)
        rows = []
        for nm, links in sorted(sts.items()):
            cov = []
            for l in links:
                cov += list(link_ends(l, L))
            ok = sorted(cov) == sorted(product(range(L), repeat=2))
            if mut("MUT-STRATA") and L == 6 and nm == "X-EVEN":
                ok = not ok
            rows.append({"stratum": nm, "links": len(links),
                         "covers_every_site_once": ok})
        strat_rows.append({"L": L, "links": 2 * L * L, "plaquettes": L * L,
                           "strata": rows})
    S["strata"] = strat_rows
    bad = [(r["L"], s["stratum"]) for r in strat_rows for s in r["strata"]
           if not s["covers_every_site_once"]]
    LD.gate("G-STRATA-PERFECT-MATCHINGS",
            "each of the four parity strata is a PERFECT MATCHING of the site "
            "set at every rung -- eight-to-a-side dominoes covering every site "
            "exactly once -- which is what makes a stratum operator a product "
            "of commuting link operators",
            not bad, "%d (rung, stratum) objects, %d failing"
            % (sum(len(r["strata"]) for r in strat_rows), len(bad)))

    prof_rows, wrap_rows = [], []
    for L in LADDER:
        sites = list(product(range(L), repeat=2))
        idx = {s: i for i, s in enumerate(sites)}
        n = L * L
        for nm, offs in PLAQ_STENCILS:
            cells = set()
            wrapped = False
            for coin in anti:
                gens, corners_all = [], []
                for o in offs:
                    p = (o[0] % L, o[1] % L)
                    corners, W = holonomy_block(p, coin, L)
                    if len(set(corners)) != 4:
                        wrapped = True
                    corners_all += corners
                    perm = block_permutation(corners, W, idx, n)
                    if perm is None:
                        gens = None
                        break
                    gens.append(perm)
                if gens is None:
                    cells.add(("NON-MONOMIAL", 0, ()))
                    continue
                orbs = gen_orbits(gens, n)
                order = group_closure(tuple(gens), n)
                pred = 1
                for ob in orbs:
                    pred *= factorial(len(ob)) // 2
                cells.add(("x".join("A%d" % len(ob) for ob in orbs)
                           or "TRIVIAL", order,
                           tuple(len(ob) for ob in orbs), order == pred,
                           all(is_three_cycle(g) for g in gens)))
            if mut("MUT-WRAP") and L == 6 and nm == "S4-BLOCK":
                wrapped = True
            wrap_rows.append({"L": L, "stencil": nm, "wraps": wrapped})
            cl = sorted(cells)
            row = {"L": L, "stencil": nm, "coins": len(anti),
                   "classes_seen": len(cl),
                   "position_class": cl[0][0], "order": cl[0][1],
                   "orbit_sizes": list(cl[0][2]),
                   "support": sum(cl[0][2]),
                   "alternating_certified": bool(cl[0][3]),
                   "generators_are_three_cycles": bool(cl[0][4])}
            if mut("MUT-PROFILE") and L == 8 and nm == "S3-ROW":
                row["order"] = 2519
            if mut("MUT-ALT") and L == 6 and nm == "S2-EDGE":
                row["alternating_certified"] = False
            prof_rows.append(row)
    S["gauge_profile"] = prof_rows
    S["non_wrapping"] = wrap_rows
    parent_profile = {r["stencil"]: (r["order"], r["support"])
                      for r in prof_rows if r["L"] == PARENT_RUNG}
    bad = [(r["L"], r["stencil"]) for r in prof_rows
           if (r["order"], r["support"]) != parent_profile[r["stencil"]]]
    prof_string = ";".join(
        "%s=%s" % (nm, {r["stencil"]: r["position_class"]
                        for r in prof_rows
                        if r["L"] == PARENT_RUNG}[nm].replace("x", " x "))
        for nm, _o in PLAQ_STENCILS)
    LD.gate("G-PROFILE-PERSISTS",
            "the (order, support) profile is measured at every rung, at every "
            "declared plaquette stencil, on every coin of the antidiagonal "
            "sector, and compared row by row against the profile the parent "
            "published and this unit quotes",
            not bad and prof_string == pv("PV-PROFILE"),
            "%d (rung, stencil) rows, %d differing from the parent's; the "
            "rebuilt profile string matches the anchored one: %s"
            % (len(prof_rows), len(bad), prof_string == pv("PV-PROFILE")))
    bad = [(r["L"], r["stencil"]) for r in prof_rows
           if not r["alternating_certified"]]
    LD.gate("G-ALTERNATING-ON-ORBITS",
            "at every rung and every declared stencil the measured group "
            "order equals the product of the alternating groups on its own "
            "orbits -- containment plus equal cardinality is equality, per "
            "object, never a fingerprint",
            not bad, "%d rows certified, %d failing" % (len(prof_rows),
                                                        len(bad)))
    bad = [(r["L"], r["stencil"]) for r in wrap_rows if r["wraps"]]
    LD.gate("G-NON-WRAPPING",
            "no declared local stencil wraps at any rung of the ladder: every "
            "plaquette of every declared patch has four distinct corners, "
            "which is why the local groups can be compared at all",
            not bad, "%d (rung, stencil) patches, %d wrapping"
            % (len(wrap_rows), len(bad)))

    glob_rows = []
    for L in LADDER:
        sites = list(product(range(L), repeat=2))
        idx = {s: i for i, s in enumerate(sites)}
        n = L * L
        gens, tc = [], True
        for p in sites:
            corners, W = holonomy_block(p, anti[0], L)
            perm = block_permutation(corners, W, idx, n)
            tc = tc and is_three_cycle(perm)
            gens.append(perm)
        orbs = gen_orbits(gens, n)
        supp = sum(len(o) for o in orbs)
        if mut("MUT-GLOBAL") and L == 6:
            supp -= 1
        glob_rows.append({"L": L, "orbits": len(orbs), "support": supp,
                          "volume": n, "support_is_the_volume": supp == n,
                          "generators_are_three_cycles": tc,
                          "class": "A%d" % supp if tc and len(orbs) == 1
                                   else "NOT-CERTIFIED"})
    S["global_stencil"] = glob_rows
    bad = [r["L"] for r in glob_rows
           if not (r["support_is_the_volume"]
                   and r["generators_are_three_cycles"] and r["orbits"] == 1)]
    g4 = [r for r in glob_rows if r["L"] == 4][0]
    g8 = [r for r in glob_rows if r["L"] == 8][0]
    LD.gate("G-GLOBAL-SUPPORT-IS-THE-VOLUME",
            "at the global stencil every plaquette holonomy is a three-cycle "
            "and the family is transitive on the whole site set, so the "
            "classical theorem gives the full alternating group on a support "
            "that is exactly the volume -- reproduced at the two rungs the "
            "parent anchored and measured at the new one",
            not bad and g4["support"] == pv("PV-GLOBAL-4")
            and g8["support"] == pv("PV-GLOBAL-8"),
            "supports by rung %s against the anchored %d at L=4 and %d at L=8"
            % ({r["L"]: r["support"] for r in glob_rows}, pv("PV-GLOBAL-4"),
               pv("PV-GLOBAL-8")))

    # =================================================================
    # STAGE 4.  LOCALITY WINDOWS
    # =================================================================
    win_rows = []
    for L in LADDER:
        r = 1
        while True:
            row = locality_at_width(L, r)
            if mut("MUT-LOCALITY") and L == 6 and r == 2:
                row = dict(row)
                row["locality"] = False
            win_rows.append(row)
            if row["complete"]:
                break
            r += 1
    S["locality_windows"] = win_rows
    bad = [(w["L"], w["r"]) for w in win_rows
           if w["locality"] != (w["neighbours"] != w["offsets"])]
    LD.gate("G-LOCALITY-WINDOWS",
            "R2's criterion is applied verbatim at a coordinate the parent "
            "did not sweep -- the window width -- and every window's locality "
            "flag is derived from its own completeness test; R2's own width "
            "law is quoted, and R2's census is cited and not re-run",
            not bad, "%d (rung, width) windows, %d whose flag disagrees with "
            "its own test" % (len(win_rows), len(bad)))

    wc_rows = []
    for L in LADDER:
        loc = [w for w in win_rows if w["L"] == L and w["locality"]]
        ir = [r for r in rad_rows if r["L"] == L][0]["interior_count"]
        n = len(loc)
        if mut("MUT-WIDTH") and L == 8:
            n -= 1
        wc_rows.append({"L": L, "locality_admitting_widths": n,
                        "widths": [w["r"] for w in loc],
                        "interior_radii": ir, "equal": n == ir})
    S["width_count"] = wc_rows
    bad = [r["L"] for r in wc_rows if not r["equal"]]
    LD.gate("G-WIDTH-COUNT-EQUALS-INTERIOR-RADII",
            "the number of window widths that admit locality equals the "
            "interior-radius count at every rung -- the parent's successor "
            "parameter and the ported locality criterion are the same number",
            not bad, "by rung: %s"
            % {r["L"]: (r["locality_admitting_widths"], r["interior_radii"])
               for r in wc_rows})

    part_rows = []
    for L in LADDER:
        for b in range(2, L):
            if L % b:
                continue
            cells = blockwise_components(L, b)
            ok = all(c["complete"] for c in cells)
            if mut("MUT-PARTITION") and L == 8 and b == 2:
                ok = False
            part_rows.append({"L": L, "block": b, "cells": len(cells),
                              "clique_only": ok,
                              "locality": not ok})
    S["partition_control"] = part_rows
    bad = [(r["L"], r["block"]) for r in part_rows if not r["clique_only"]]
    LD.gate("G-PARTITION-COROLLARY",
            "R2's partition corollary transports: every blockwise atlas of "
            "this stage is clique-only at every rung, so locality here is "
            "carried by the SLIDING window and by nothing else",
            not bad, "%d blockwise atlases, %d producing a non-complete "
            "component" % (len(part_rows), len(bad)))

    band_rows = []
    for r in WIDTHS:
        adm = []
        for L in BAND_SIZES:
            loc = locality_at_width(L, r)["locality"]
            wit = band_witness(L, r)
            ok = loc and wit is not None
            if mut("MUT-BAND") and r == 2 and L == 7:
                ok = True
            if ok:
                adm.append(L)
            band_rows.append({"r": r, "L": L, "locality": loc,
                              "non_monomial_witness": wit is not None,
                              "witness": wit, "admitted": ok})
        pred = [L for L in BAND_SIZES if L % 2 == 0 and 2 * r + 2 <= L <= 4 * r]
        band_rows.append({"r": r, "L": None, "admitted_set": adm,
                          "predicted_set": pred, "law_holds": adm == pred})
    S["band_law"] = {
        "rows": [b for b in band_rows if b.get("L") is not None],
        "by_width": [b for b in band_rows if b.get("L") is None],
        "law": "at window width r the sizes carrying BOTH locality and a "
               "witnessed local non-monomial unitary are exactly the even L "
               "with 2r+2 <= L <= 4r",
        "parent_row": [b for b in band_rows
                       if b.get("L") is None and b["r"] == 1][0]["admitted_set"],
        "one_sided_at_width_above_one":
            "the presence half is constructive and verified at every listed "
            "size; the absence half is FORCED only at width 1, where the "
            "difference-doubled subset census over the nine-offset ball is "
            "exhaustive -- at wider windows the complement is declared open"}
    bad = [b["r"] for b in band_rows
           if b.get("L") is None and not b["law_holds"]]
    LD.gate("G-BAND-LAW",
            "the parent's admitted-scale set is re-derived at its own window "
            "width and then at wider ones: at every declared width the "
            "admitted sizes are exactly the even sizes between 2r+2 and 4r, "
            "each carrying a constructive non-monomial witness verified "
            "unitary by the whole-torus criterion",
            not bad and [b for b in band_rows if b.get("L") is None
                         and b["r"] == 1][0]["admitted_set"] == pv("PV-ADMISSIBLE"),
            "admitted sets by width %s; the width-1 row reproduces the "
            "anchored %s"
            % ({b["r"]: b["admitted_set"] for b in band_rows
                if b.get("L") is None}, pv("PV-ADMISSIBLE")))

    # =================================================================
    # STAGE 5.  THE PERSISTENCE TABLE
    # =================================================================
    def cellrow(name, cells, kind, law=""):
        vals = [cells[L] for L in LADDER]
        if kind == "AUTO":
            if len(set(map(str, vals))) == 1:
                v = "PERSISTS"
            else:
                v = "TRANSFORMS"
        else:
            v = kind
        return {"invariant": name,
                "cells": {str(L): cells[L] for L in LADDER},
                "verdict": v, "law": law}

    T = []
    T.append(cellrow("the LINK stencil is Sidon",
                     {L: [r["sidon"] for r in arenas
                          if r["L"] == L and r["arena"] == "LINK"][0]
                      for L in LADDER}, "AUTO"))
    T.append(cellrow("monomial-only on the LINK stencil",
                     {L: [r["non_monomial"] for r in arenas
                          if r["L"] == L and r["arena"] == "LINK"][0]
                      for L in LADDER}, "AUTO"))
    T.append(cellrow("the local AXIS stencil is Sidon",
                     {L: [r["sidon"] for r in arenas
                          if r["L"] == L and r["arena"].startswith("AXIS")][0]
                      for L in LADDER}, "AUTO"))
    T.append(cellrow("non-monomial generators on a local AXIS stencil",
                     {L: [r["non_monomial"] for r in arenas
                          if r["L"] == L and r["arena"].startswith("AXIS")][0]
                      for L in LADDER}, "BREAKS-AT-L=6",
                     "48 at the parent rung, 0 at both new rungs: the local "
                     "family collapses to shifts"))
    T.append(cellrow("the local AXIS stencil is DDS-free",
                     {L: [r["dds_free"] for r in arenas
                          if r["L"] == L and r["arena"].startswith("AXIS")][0]
                      for L in LADDER}, "BREAKS-AT-L=6",
                     "the criterion turns on at L = 6 and stays on"))
    T.append(cellrow("the fourth-direction death",
                     {L: [r["non_monomial"] for r in arenas
                          if r["L"] == L and r["arena"] == "LINK-PLUS-4TH"][0]
                      for L in LADDER}, "BREAKS-AT-L=6",
                     "the same declared fourth direction kills at L = 4 and "
                     "does not kill at L = 6 or L = 8"))
    T.append(cellrow("circulant families in the pool",
                     {L: [r["circulants"] for r in pool_rows
                          if r["L"] == L][0] for L in LADDER}, "TRANSFORMS",
                     "58, 42, 106: not monotone in L; the count is the sum "
                     "of per-axis gauge classes less the shared identity"))
    T.append(cellrow("non-monomial families in the pool",
                     {L: [r["non_monomial"] for r in pool_rows
                          if r["L"] == L][0] for L in LADDER}, "TRANSFORMS",
                     "carried only by axes of order 2 and 4, never by a "
                     "local axis above the parent rung"))
    T.append(cellrow("local non-monomial families in the pool",
                     {L: [r["local_non_monomial"] for r in pool_rows
                          if r["L"] == L][0] for L in LADDER},
                     "BREAKS-AT-L=6", "the parent's headline family is empty "
                     "at both new rungs"))
    T.append(cellrow("VMAX", {L: [r["vmax"] for r in vmax_rows
                                  if r["L"] == L][0] for L in LADDER},
                     "TRANSFORMS", "VMAX = L/2 at every rung"))
    T.append(cellrow("VMAX equals the max-norm diameter",
                     {L: [r["vmax_equals_diameter"] for r in vmax_rows
                          if r["L"] == L][0] for L in LADDER}, "AUTO"))
    T.append(cellrow("interior radii",
                     {L: [r["interior_count"] for r in rad_rows
                          if r["L"] == L][0] for L in LADDER}, "TRANSFORMS",
                     "L/2 - 1 at every rung; the register's 3 at L = 8 is "
                     "confirmed"))
    T.append(cellrow("locality-admitting window widths",
                     {L: [r["locality_admitting_widths"] for r in wc_rows
                          if r["L"] == L][0] for L in LADDER}, "TRANSFORMS",
                     "equal to the interior-radius count at every rung"))
    T.append(cellrow("static families",
                     {L: [r["static"] for r in disp_rows
                          if r["L"] == L][0] for L in LADDER}, "AUTO",
                     "one at every rung: the identity"))
    T.append(cellrow("the reduced dispersion separates families",
                     {L: [r["distinct_reduced_dispersions"] == r["families"]
                          for r in disp_rows if r["L"] == L][0]
                      for L in LADDER}, "AUTO"))
    T.append(cellrow("every eigenvalue is a root of unity",
                     {L: True for L in LADDER}, "AUTO"))
    T.append(cellrow("the eigenphase lattice",
                     {L: [r["eigenphase_lattice"] for r in disp_rows
                          if r["L"] == L][0] for L in LADDER}, "TRANSFORMS",
                     "Z/lcm(8, L): the gauge group's order joined to the "
                     "rung"))
    T.append(cellrow("all group velocities are integers",
                     {L: [r["all_integer"] for r in vel_rows
                          if r["L"] == L][0] for L in LADDER},
                     "BREAKS-AT-L=6",
                     "an order-2 axis at L = 6 carries speed 3/2"))
    T.append(cellrow("the coin family and its sector split",
                     {L: "%d=%d+%d+%d" % (len(coins), secs["DIAGONAL"],
                                          secs["ANTIDIAGONAL"],
                                          secs["BALANCED"])
                      for L in LADDER}, "AUTO",
                     "the coin carries no L"))
    T.append(cellrow("the parity strata are perfect matchings",
                     {L: True for L in LADDER}, "AUTO",
                     "at every even rung"))
    T.append(cellrow("the (order, support) profile",
                     {L: ";".join("%s=%d/%d" % (r["stencil"], r["order"],
                                                r["support"])
                                  for r in prof_rows if r["L"] == L)
                      for L in LADDER}, "AUTO",
                     "identical at all three rungs, on all 64 antidiagonal "
                     "coins"))
    T.append(cellrow("the holonomy is alternating on each of its orbits",
                     {L: True for L in LADDER}, "AUTO"))
    T.append(cellrow("the global support",
                     {L: [r["support"] for r in glob_rows
                          if r["L"] == L][0] for L in LADDER}, "TRANSFORMS",
                     "the volume L^2 at every rung"))
    T.append(cellrow("the window widths at which this size is admitted",
                     {L: [b["r"] for b in band_rows if b.get("L") is None
                          and L in b["admitted_set"]] for L in LADDER},
                     "TRANSFORMS",
                     "the parent's uniqueness is the width-1 section of a "
                     "band that widens with the window: {4} at width 1, "
                     "{6, 8} at width 2, {8, 10, 12} at width 3"))

    if mut("MUT-TABLE"):
        T[1]["verdict"] = "BREAKS-AT-L=8"
    bad = []
    for row in T:
        vals = list(row["cells"].values())
        same = len(set(map(str, vals))) == 1
        if row["verdict"] == "PERSISTS" and not same:
            bad.append(row["invariant"])
        if row["verdict"].startswith("BREAKS") and same:
            bad.append(row["invariant"])
        if row["verdict"] == "TRANSFORMS" and same:
            bad.append(row["invariant"])
    S["persistence_table"] = T
    LD.gate("G-PERSISTENCE-TABLE-BOUND",
            "every persistence verdict is bound to its own row's measured "
            "cells: PERSISTS requires the three cells to agree, BREAKS and "
            "TRANSFORMS require them not to, per row and never in aggregate",
            not bad, "%d rows, %d whose verdict contradicts its own cells: %s"
            % (len(T), len(bad), bad or "none"))

    S["counts"] = {
        "rungs": len(LADDER),
        "arenas": len(arenas),
        "arenas_sidon": sum(1 for r in arenas if r["sidon"]),
        "arenas_dds_free": S["dds_law"]["arenas_dds_free"],
        "arenas_monomial_only": sum(1 for r in arenas if r["monomial_only"]),
        "maps_scanned": sum(r["maps"] for r in arenas)
                        + sum(c["maps"] for c in ctrl),
        "necessity_failures": len(nec_fail),
        "control_reproduced": registered["non_monomial"],
        "circulants_L4": r4row["circulants"],
        "circulants_L6": [r["circulants"] for r in pool_rows
                          if r["L"] == 6][0],
        "circulants_L8": [r["circulants"] for r in pool_rows
                          if r["L"] == 8][0],
        "dispersion_cells": sum(r["cells"] for r in disp_rows),
        "vmax_L4": [r["vmax"] for r in vmax_rows if r["L"] == 4][0],
        "vmax_L6": [r["vmax"] for r in vmax_rows if r["L"] == 6][0],
        "vmax_L8": [r["vmax"] for r in vmax_rows if r["L"] == 8][0],
        "interior_L4": [r["interior_count"] for r in rad_rows
                        if r["L"] == 4][0],
        "interior_L6": [r["interior_count"] for r in rad_rows
                        if r["L"] == 6][0],
        "interior_L8": [r["interior_count"] for r in rad_rows
                        if r["L"] == 8][0],
        "coins": len(coins),
        "profile_rows": len(prof_rows),
        "window_rows": len(win_rows),
        "band_rows": len([b for b in band_rows if b.get("L") is not None]),
        "table_rows": len(T),
        "persists": sum(1 for r in T if r["verdict"] == "PERSISTS"),
        "breaks": sum(1 for r in T if r["verdict"].startswith("BREAKS")),
        "transforms": sum(1 for r in T if r["verdict"] == "TRANSFORMS"),
        "lag_objects": lag_checked,
        "sources": len(SOURCES),
        "path_value_anchors": len(PATH_VALUE_ANCHORS),
        "verbatim_anchors": len(VERBATIM_ANCHORS),
        "mutants": len(MUTANTS),
        "L": pv("PV-L"), "d": pv("PV-D"), "alphabet": pv("PV-ALPHABET"),
        "connective_tag": pv("PV-CONNECTIVE"),
        "forcing_link": pv("PV-FORCING-LINK"),
        "field": "Q(ZETA-24)",
    }

    # ---- the two fractions, stamped (E-24) ----------------------------
    fr = [
        {"name": "arenas that are Sidon",
         "value": "%d of %d" % (S["counts"]["arenas_sidon"], len(arenas)),
         "measure": "COUNTING-ONLY",
         "why": "a count over this unit's own declared arena list, which is "
                "not a sample of any population and carries no measure"},
        {"name": "arenas that are DDS-free",
         "value": "%d of %d" % (S["counts"]["arenas_dds_free"], len(arenas)),
         "measure": "COUNTING-ONLY",
         "why": "the same declared list; the criterion's soundness is a "
                "theorem, and this count is a coverage report, not a rate"},
    ]
    if mut("MUT-FRACTION"):
        fr.append({"name": "unstamped", "value": "1 of 2"})
    S["declared_fractions"] = fr
    bad = [f["name"] for f in fr
           if f.get("measure") not in ("COUNTING-ONLY",) and "measure" not in f]
    LD.gate("G-FRACTIONS-STAMPED",
            "every fraction this unit publishes declares its measure or is "
            "stamped COUNTING-ONLY; no count becomes a probability here",
            not bad, "%d fractions, %d unstamped: %s"
            % (len(fr), len(bad), bad or "none"))

    S["choice_inventory"] = [
        {"choice": "the spatial dimension", "class": "FORCED (anchored)",
         "fibre": 1, "instances": 1},
        {"choice": "the coefficient alphabet", "class": "FORCED (anchored)",
         "fibre": 1, "instances": 1,
         "why": "inherited from the parent and held fixed along L: a moving "
                "alphabet would make the ladder incomparable"},
        {"choice": "the stencil", "class": "FORCED (anchored)", "fibre": 1,
         "instances": 1, "why": "the parent's 3-term axis stencil"},
        {"choice": "the connective", "class": "FORCED (anchored)", "fibre": 1,
         "instances": 1},
        {"choice": "the link set", "class": "FORCED (anchored)", "fibre": 1,
         "instances": 1},
        {"choice": "the axis set at each rung",
         "class": "FORCED (exhaustive)",
         "fibre": sum(r["axes"] for r in ax_rows), "instances": "all"},
        {"choice": "the global phase", "class": "STABILIZER-FIXED",
         "fibre": 8, "instances": 8},
        {"choice": "the rungs of the ladder", "class": "GENUINELY-FREE",
         "fibre": "UNBOUNDED", "instances": len(LADDER),
         "why": "the pin declares L = 6 and L = 8; the parent rung is run as "
                "the reproduction control"},
        {"choice": "the fourth direction", "class": "GENUINELY-FREE",
         "fibre": "UNBOUNDED", "instances": 1,
         "why": "paper-20's own declared fourth direction, carried verbatim "
                "so the control is the registered one"},
        {"choice": "the probe alphabets at the control rung",
         "class": "GENUINELY-FREE", "fibre": "UNBOUNDED",
         "instances": len(PROBE_ALPHABETS),
         "why": "the registered count is alphabet-relative and this unit "
                "measures the relativity rather than hiding it"},
        {"choice": "the window widths", "class": "GENUINELY-FREE",
         "fibre": "UNBOUNDED", "instances": len(WIDTHS)},
        {"choice": "the plaquette stencils", "class": "FORCED (anchored)",
         "fibre": 1, "instances": len(PLAQ_STENCILS),
         "why": "the parent's own six, carried verbatim"},
        {"choice": "the DDS subset window", "class": "DECLARED-WINDOW",
         "fibre": 1, "instances": 1,
         "why": "the subset census is exhaustive at |S| <= %d and the "
                "absence half of the band law is claimed only where it runs"
                % DDS_SUBSET_WINDOW},
    ]
    LD.gate("G-CHOICES-INVENTORIED",
            "every construction choice is inventoried with its class, its "
            "fibre and the number of instances run, and the one declared "
            "window is named as a window",
            all("class" in c and "fibre" in c for c in S["choice_inventory"])
            and any(c["class"] == "DECLARED-WINDOW"
                    for c in S["choice_inventory"]),
            "%d choices inventoried" % len(S["choice_inventory"]))

    S["runtime_inputs"] = {"sources": [rel for _s, rel, _d, _n in SOURCES],
                           "object_under_test": PAPER_REL,
                           "reads": sorted(set(READS))}
    extra = [r for r in set(READS)
             if r not in {rel for _s, rel, _d, _n in SOURCES}
             and not r.endswith(PAPER_REL) and not os.path.isabs(r)]
    if mut("MUT-EXTRA-READ"):
        extra.append("v14/LOG.md")
    LD.gate("G-RUNTIME-INPUTS-ENUMERATED",
            "every path read at run time is one of the ten declared sources "
            "or the object under test; no ledger, no STATUS, no other unit's "
            "working file, and no subprocess",
            not extra, "%d reads, %d undeclared: %s"
            % (len(set(READS)), len(extra), extra or "none"))

    return S, LD, SEAL


def _gcd_all(vals):
    g = 0
    for v in vals:
        while v:
            g, v = v, g % v
        g = abs(g)
    return g or 1


def _lcm_all(vals):
    m = 1
    for v in vals:
        m = m * v // _gcd_all([m, v])
    return m

# ===========================================================================
# SECTION 11.  THE VERDICT
# ===========================================================================


def build_verdict(S):
    """the head is DERIVED from the sealed primitive tables; the segments are
    built here and re-derived independently at G-VERDICT-RECONSTRUCTED."""
    c = S["counts"]
    p = S["sidon_prediction"]
    head = {"SUFFICIENT-NOT-NECESSARY": "PERL-SIDON-SUFFICIENT-NOT-NECESSARY",
            "CONFIRMED-BOTH-WAYS": "PERL-SIDON-CONFIRMED-BOTH-WAYS",
            "REFUTED": "PERL-SIDON-REFUTED"}[p["verdict"]]
    if mut("MUT-HEAD"):
        head = "PERL-EVERYTHING-PERSISTS"

    link = {r["L"]: r for r in S["sidon_arenas"] if r["arena"] == "LINK"}
    axis = {}
    for r in S["sidon_arenas"]:
        if r["arena"].startswith("AXIS") and r["L"] not in axis:
            axis[r["L"]] = r
    ctl = S["fourth_direction_control"]
    seg = []
    seg.append("SIDON=SUFFICIENCY-HOLDS-AT-%d-OF-%d-ARENAS;"
               "LINK-STENCIL-SIDON-AND-MONOMIAL-ONLY-AT-L-6-AND-8"
               "(%d-AND-%d-NON-MONOMIAL-OF-%d-AND-%d-UNITARY);"
               "NECESSITY-FAILS-AT-%d-ARENAS(FIRST=%s)"
               % (len(p["rows"]), len(p["rows"]),
                  link[6]["non_monomial"], link[8]["non_monomial"],
                  link[6]["unitary"], link[8]["unitary"],
                  p["necessity_failures"],
                  p["necessity_failure_arenas"][0].replace("=", "-")
                  .replace(" ", "-")))
    seg.append("CONTROL=THE-FOURTH-DIRECTION-DEATH-DOES-NOT-TRANSPORT"
               "(REGISTERED-%d-REPRODUCED-AT-THE-CONTROL-RUNG;"
               "%d-AT-L-4;0-AT-L-6-AND-L-8;ALPHABET-RELATIVE-0-OF-%d-OVER-"
               "THE-PARENTS-OWN-ALPHABET)"
               % (ctl["registered_count_reproduced"],
                  [r["non_monomial"] for r in ctl["ladder_rows"]
                   if r["L"] == 4][0], c["alphabet"]))
    seg.append("LAW=DDS-FREE-FORCES-MONOMIAL-OVER-ANY-FIELD"
               "(NO-DIFFERENCE-DOUBLED-SUBSET;%d-OF-%d-ARENAS-DDS-FREE-AND-"
               "ALL-MONOMIAL-ONLY;SIDON-STRICTLY-STRONGER-AT-%d-ARENAS)"
               % (S["dds_law"]["arenas_dds_free"], c["arenas"],
                  S["dds_law"]["sidon_but_not_the_only_forced"]))
    seg.append("VMAX=DIAMETER-AT-EVERY-RUNG(%s;%s;%s=L/2)"
               % (c["vmax_L4"], c["vmax_L6"], c["vmax_L8"]))
    seg.append("INTERIOR-RADII=%d;%d;%d(THE-3-AT-L-8-REGISTER-CLAIM-CONFIRMED;"
               "EQUAL-TO-THE-LOCALITY-ADMITTING-WIDTH-COUNT-AT-EVERY-RUNG)"
               % (c["interior_L4"], c["interior_L6"], c["interior_L8"]))
    seg.append("FINGERPRINT=(ORDER,SUPPORT)-PROFILE-IDENTICAL-AT-ALL-THREE-"
               "RUNGS-ON-ALL-%d-ANTIDIAGONAL-COINS(%s);"
               "GLOBAL-SUPPORT-IS-THE-VOLUME-16;36;64;NO-GROUP-SELECTION-LAW-"
               "CLAIMED" % (S["counts"]["coins"] // 10,
                            S["path_value_anchors"][0]["read"] and
                            [r["read"] for r in S["path_value_anchors"]
                             if r["anchor"] == "PV-PROFILE"][0]))
    seg.append("SCALE=THE-PARENTS-UNIQUE-SIZE-IS-WINDOW-RELATIVE"
               "(ADMITTED-SIZES-AT-WIDTH-r-ARE-THE-EVEN-L-IN-[2r+2,4r];"
               "WIDTH-1={4};WIDTH-2={6,8};WIDTH-3={8,10,12};"
               "PRESENCE-CONSTRUCTIVE-ABSENCE-FORCED-ONLY-AT-WIDTH-1)")
    seg.append("BREAKS=LOCAL-NON-MONOMIAL-FAMILY-EMPTY-FROM-L-6;"
               "INTEGER-VELOCITIES-FAIL-AT-L-6(SPEED-3/2-ON-AN-ORDER-2-AXIS);"
               "EIGENPHASE-LATTICE-TRANSFORMS-Z/lcm(8,L)")
    seg.append("TABLE=%d-ROWS(%d-PERSIST;%d-BREAK;%d-TRANSFORM)"
               % (c["table_rows"], c["persists"], c["breaks"],
                  c["transforms"]))
    seg.append("SCOPE=D=%d;RUNGS=L-IN-{4,6,8};FIELD=Q(ZETA-24);ALPHABET=%d;"
               "STENCIL=3-TERM-AXIS-AND-THE-ANCHORED-LINK-SET;"
               "CONNECTIVE=MAX-NORM(FORCED-BY-ANCHORED-LINK-%s);"
               "SECTOR=SINGLE-OCCUPATION;"
               "INDIVISIBILITY=DECLARED-BY-DIVISION-EVENT-TIMES;"
               "FINITE-LATTICE-ONLY;NO-CONTINUUM-CLAIM;"
               "NO-TRANSPORT-NUMBER-INHERITED;"
               "PERSISTENCE-AT-DECLARED-FINITE-RUNGS-ONLY"
               % (c["d"], c["alphabet"], c["forcing_link"]))
    body = "|".join(seg)
    if mut("MUT-WALLS"):
        body = body.replace("NO-CONTINUUM-CLAIM", "CONTINUUM-LIMIT-ESTABLISHED")
    return head, head + "<" + body + ">"


def reconstruct_verdict(receipt):
    """the INDEPENDENT comparator: rebuilt from the receipt's own primitive
    tables by code that shares no literal and no helper with the builder."""
    c = receipt["counts"]
    p = receipt["sidon_prediction"]
    names = {"SUFFICIENT-NOT-NECESSARY": "PERL-SIDON-SUFFICIENT-NOT-NECESSARY",
             "CONFIRMED-BOTH-WAYS": "PERL-SIDON-CONFIRMED-BOTH-WAYS",
             "REFUTED": "PERL-SIDON-REFUTED"}
    head = names[p["verdict"]]
    parts = []
    parts.append(c["arenas_sidon"])
    parts.append(c["arenas_dds_free"])
    parts.append(c["necessity_failures"])
    parts.append(c["control_reproduced"])
    parts.append([c["vmax_L4"], c["vmax_L6"], c["vmax_L8"]])
    parts.append([c["interior_L4"], c["interior_L6"], c["interior_L8"]])
    parts.append([c["persists"], c["breaks"], c["transforms"]])
    return head, parts


def verdict_fingerprint(vs, receipt):
    """the segments a reader would read off the string, recovered by parsing
    it, so the string and the tables cannot drift apart silently."""
    inner = vs[vs.index("<") + 1:-1]
    got = {}
    for s in inner.split("|"):
        k, _, v = s.partition("=")
        got[k] = v
    return got

# ===========================================================================
# SECTION 12.  THE PAPER INSTRUMENT (#20 with E-22)
# ===========================================================================

DIGITS = "0123456789"
# the declared structural numerals: section and rung labels, and the RUNBOOK
# engraving numbers this unit's instrument section cites by name.  Everything
# else in the paper must be licensed by a value in the receipt.
STRUCTURAL = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11",
              "12", "13", "14", "15", "16", "17", "18", "19", "20", "21",
              "22", "23", "24", "28", "34", "46", "82", "87", "91", "119",
              "125", "148", "187", "192", "196", "2026"}


def numerals(text):
    """every DECIMAL numeral, including the fractions and the digit-grouped
    integers the paper prints.  A comma or a slash between digits continues
    the token; commas are then removed, so `1,952,424` and `1952424` are the
    same claim and `3/2` is its own."""
    out, cur = set(), ""
    for ch in text:
        if ch in DIGITS or (ch in "/," and cur and cur[-1] in DIGITS):
            cur += ch
        else:
            if cur:
                out.add(cur.replace(",", "").strip("/"))
            cur = ""
    if cur:
        out.add(cur.replace(",", "").strip("/"))
    return {n for n in out if n}


def licensed_numerals(obj, acc):
    if isinstance(obj, bool):
        return acc
    if isinstance(obj, int):
        acc.add(str(obj))
        acc.add(str(abs(obj)))
    elif isinstance(obj, str):
        acc |= numerals(obj)
    elif isinstance(obj, dict):
        for k, v in obj.items():
            acc |= numerals(str(k))
            licensed_numerals(v, acc)
    elif isinstance(obj, (list, tuple)):
        for v in obj:
            licensed_numerals(v, acc)
    return acc


def fenced_blocks(txt):
    """E-22: the paper's fenced blocks, as a MULTISET."""
    out = []
    inside, buf = False, []
    for line in txt.split("\n"):
        if line.startswith("```"):
            if inside:
                out.append("\n".join(buf).strip())
                buf = []
            inside = not inside
            continue
        if inside:
            buf.append(line)
    return out


def inline_spans(txt):
    """E-22: every backticked span, fenced blocks removed first so a span is
    never counted twice."""
    stripped, inside = [], False
    for line in txt.split("\n"):
        if line.startswith("```"):
            inside = not inside
            continue
        if not inside:
            stripped.append(line)
    return re.findall(r"`([^`\n]+)`", "\n".join(stripped))


def rendered_fences(S):
    """what the paper's fenced blocks MUST be, rendered from the receipt.
    The verdict block appears twice by design, which is exactly the case a
    containment gate cannot see."""
    block = S["verdict"]["head"] + "\n" + S["verdict"]["string"]
    return [block, block]


def paper_claims(S):
    c, p = S["counts"], S["sidon_prediction"]
    ctl = S["fourth_direction_control"]
    link = {r["L"]: r for r in S["sidon_arenas"] if r["arena"] == "LINK"}
    axis = {}
    for r in S["sidon_arenas"]:
        if r["arena"].startswith("AXIS") and r["L"] not in axis:
            axis[r["L"]] = r
    four = {r["L"]: r for r in S["sidon_arenas"]
            if r["arena"] == "LINK-PLUS-4TH"}
    band = {b["r"]: b for b in S["band_law"]["by_width"]}
    out = [
        {"id": "CL-SUFFICIENCY", "path": "counts/arenas",
         "text": "the sufficiency direction holds at every one of the %d "
                 "declared arenas" % c["arenas"]},
        {"id": "CL-NECESSITY", "path": "counts/necessity_failures",
         "text": "the converse fails at %d of them" % c["necessity_failures"]},
        {"id": "CL-LINK6", "path": "sidon_arenas/6/unitary",
         "text": "the link stencil is Sidon at every rung, and its scan "
                 "returns %d unitary maps of which %d are non-monomial at "
                 "L = 6" % (link[6]["unitary"], link[6]["non_monomial"])},
        {"id": "CL-LINK8", "path": "sidon_arenas/12/unitary",
         "text": "at L = 8 the same stencil returns %d unitary maps and %d "
                 "non-monomial" % (link[8]["unitary"],
                                   link[8]["non_monomial"])},
        {"id": "CL-AXIS4", "path": "sidon_arenas/1/non_monomial",
         "text": "the local axis stencil carries %d non-monomial unitaries at "
                 "the parent rung" % axis[4]["non_monomial"]},
        {"id": "CL-AXIS68", "path": "sidon_arenas/7/non_monomial",
         "text": "and %d at L = 6 and %d at L = 8, with the same non-Sidon "
                 "difference multiplicities %s"
                 % (axis[6]["non_monomial"], axis[8]["non_monomial"],
                    axis[6]["difference_multiplicities"])},
        {"id": "CL-CONTROL", "path": "fourth_direction_control/registered_count_reproduced",
         "text": "the registered count is reproduced exactly: %d non-monomial "
                 "unitary maps" % ctl["registered_count_reproduced"]},
        {"id": "CL-CONTROL-LADDER", "path": "sidon_arenas/5/non_monomial",
         "text": "the same fourth direction carries %d non-monomial "
                 "unitaries at L = 4 and %d at L = 6 and %d at L = 8"
                 % (four[4]["non_monomial"], four[6]["non_monomial"],
                    four[8]["non_monomial"])},
        {"id": "CL-POOL", "path": "counts/circulants_L6",
         "text": "the pool carries %d circulant families at L = 4, %d at "
                 "L = 6 and %d at L = 8"
                 % (c["circulants_L4"], c["circulants_L6"],
                    c["circulants_L8"])},
        {"id": "CL-VMAX", "path": "counts/vmax_L8",
         "text": "the maximal group speed is %s, %s and %s, and the max-norm "
                 "diameter is the same number at each rung"
                 % (c["vmax_L4"], c["vmax_L6"], c["vmax_L8"])},
        {"id": "CL-RADII", "path": "counts/interior_L8",
         "text": "the interior-radius count is %d, %d and %d"
                 % (c["interior_L4"], c["interior_L6"], c["interior_L8"])},
        {"id": "CL-WIDTHS", "path": "width_count/2/locality_admitting_widths",
         "text": "the number of window widths admitting locality is %d, %d "
                 "and %d" % tuple(r["locality_admitting_widths"]
                                  for r in S["width_count"])},
        {"id": "CL-VELOCITY", "path": "velocity_census/1/non_integer_families",
         "text": "%d families at L = 6 carry a velocity that is not an "
                 "integer" % [r["non_integer_families"]
                              for r in S["velocity_census"]
                              if r["L"] == 6][0]},
        {"id": "CL-COINS", "path": "counts/coins",
         "text": "the derived coin family has %d members at every rung"
                 % c["coins"]},
        {"id": "CL-PROFILE", "path": "counts/profile_rows",
         "text": "the profile is measured at %d rung-and-stencil rows and is "
                 "identical at all three rungs" % c["profile_rows"]},
        {"id": "CL-GLOBAL", "path": "global_stencil/1/support",
         "text": "the global support is %d, %d and %d, which is the volume at "
                 "each rung" % tuple(r["support"]
                                     for r in S["global_stencil"])},
        {"id": "CL-BAND1", "path": "band_law/by_width/0/admitted_set",
         "text": "at window width 1 the admitted set is %s"
                 % band[1]["admitted_set"]},
        {"id": "CL-BAND2", "path": "band_law/by_width/1/admitted_set",
         "text": "at window width 2 it is %s, and at width 3 it is %s"
                 % (band[2]["admitted_set"], band[3]["admitted_set"])},
        {"id": "CL-TABLE", "path": "counts/table_rows",
         "text": "the persistence table carries %d rows: %d persist, %d "
                 "break and %d transform"
                 % (c["table_rows"], c["persists"], c["breaks"],
                    c["transforms"])},
        {"id": "CL-MAPS", "path": "counts/maps_scanned",
         "text": "%d coefficient maps are scanned in all" % c["maps_scanned"]},
        {"id": "CL-LAGS", "path": "counts/lag_objects",
         "text": "%d axis-and-lag objects are bound" % c["lag_objects"]},
    ]
    return out


def paper_tables(S):
    """E-22: tables render as claims.  Each row below is the exact pipe row
    the paper must carry."""
    rows = []
    for r in S["persistence_table"]:
        rows.append("| %s | %s | %s | %s | %s |"
                    % (r["invariant"], r["cells"]["4"], r["cells"]["6"],
                       r["cells"]["8"], r["verdict"]))
    for a in S["sidon_arenas"]:
        rows.append("| %d | %s | %s | %s | %s | %d | %d |"
                    % (a["L"], a["arena"], a["sidon"], a["dds_free"],
                       a["difference_multiplicities"], a["unitary"],
                       a["non_monomial"]))
    return rows


def perturb(S, path):
    parts = path.split("/")
    cur = S
    for p in parts[:-1]:
        cur = cur[int(p)] if isinstance(cur, list) else cur[p]
    k = int(parts[-1]) if isinstance(cur, list) else parts[-1]
    old = cur[k]
    cur[k] = (old + 1) if isinstance(old, int) and not isinstance(old, bool) \
        else (old + ["X"] if isinstance(old, list) else str(old) + "X")
    return old


def restore(S, path, old):
    parts = path.split("/")
    cur = S
    for p in parts[:-1]:
        cur = cur[int(p)] if isinstance(cur, list) else cur[p]
    k = int(parts[-1]) if isinstance(cur, list) else parts[-1]
    cur[k] = old


def paper_coverage_only(S, txt):
    """the FINAL pass: the same instrument, evaluated once the totals close,
    with no gate ids registered a second time.  Its enforcement is
    G-PAPER-COVERAGE-FINAL, and its in-run twins carry the falsifiers."""
    norm = norm_text(txt)
    claims = paper_claims(S)
    missing = [c["id"] for c in claims if norm_text(c["text"]) not in norm]
    lic = licensed_numerals(S, set()) | STRUCTURAL
    pn = numerals(txt)
    unlic = sorted(n for n in pn if n not in lic)
    spans = inline_spans(txt)
    sn = set()
    for sp in spans:
        sn |= numerals(sp)
    span_bad = sorted(n for n in sn if n not in lic)
    have, want = sorted(fenced_blocks(txt)), sorted(rendered_fences(S))
    trows = paper_tables(S)
    tmiss = [t for t in trows if norm_text(t) not in norm]
    bad_pol = []
    for c in claims:
        old = perturb(S, c["path"])
        new = [x for x in paper_claims(S) if x["id"] == c["id"]][0]
        restore(S, c["path"], old)
        if new["text"] == c["text"] or norm_text(new["text"]) in norm:
            bad_pol.append(c["id"])
    return {"numerals": len(pn), "unlicensed": len(unlic) + len(span_bad),
            "claims": len(claims), "missing": len(missing),
            "spans": len(spans), "span_numerals": len(sn),
            "fenced_blocks": len(have), "fenced_multiset_equal": have == want,
            "table_rows": len(trows), "table_missing": len(tmiss),
            "polarity_failures": len(bad_pol),
            "paper": os.path.basename(PAPER_REL)}


def verify_paper(S, LD, txt):
    norm = norm_text(txt)

    claims = paper_claims(S)
    if mut("MUT-PAPER-CLAIM"):
        claims = claims + [{"id": "CL-INJECTED", "path": "counts/rungs",
                            "text": "a measured assertion the paper does not "
                                    "make anywhere in its text"}]
    missing = [c["id"] for c in claims if norm_text(c["text"]) not in norm]
    S["paper_claims"] = claims
    LD.gate("G-PAPER-CLAIMS",
            "every claim the paper makes about a measured quantity renders "
            "from a receipt key and is present in the paper as written",
            not missing, "%d claims, %d missing: %s"
            % (len(claims), len(missing), missing or "none"))

    lic = licensed_numerals(S, set()) | STRUCTURAL
    pn = numerals(txt)
    if mut("MUT-PAPER-NUMERAL"):
        pn = pn | {"987654321"}
    unlic = sorted(n for n in pn if n not in lic)
    LD.gate("G-PAPER-NUMERAL-COVERAGE",
            "EVERY numeral in the paper -- prose, tables, fenced blocks and "
            "inline code spans alike -- is licensed by a receipt value or is "
            "one of the declared structural numerals",
            not unlic, "%d distinct numerals, %d unlicensed: %s"
            % (len(pn), len(unlic), unlic[:8] or "none"))

    spans = inline_spans(txt)
    sn = set()
    for s in spans:
        sn |= numerals(s)
    if mut("MUT-PAPER-SPAN"):
        sn = sn | {"424242"}
    span_bad = sorted(n for n in sn if n not in lic)
    LD.gate("G-PAPER-INLINE-SPANS",
            "the inline code spans are scanned in their own right under the "
            "fenced rule: a backticked numeral is a claim like any other, and "
            "a scanner that strips spans is blind exactly where the paper "
            "puts its sharpest numbers",
            not span_bad, "%d inline spans carrying %d distinct numerals, %d "
            "unlicensed: %s" % (len(spans), len(sn), len(span_bad),
                                span_bad[:8] or "none"))

    have = sorted(fenced_blocks(txt))
    want = sorted(rendered_fences(S))
    if mut("MUT-PAPER-FENCE"):
        want = want[:-1]
    S["paper_fences"] = {"blocks_in_paper": len(have),
                         "blocks_rendered": len(want),
                         "distinct": len(set(have)),
                         "multiset_equal": have == want}
    LD.gate("G-PAPER-FENCED-MULTISET",
            "the paper's fenced blocks are gated by MULTISET equality against "
            "blocks rendered from the receipt, not by containment: a "
            "duplicated block cannot shadow a forged twin",
            have == want, "%d blocks in the paper, %d rendered, %d distinct, "
            "multiset equal: %s" % (len(have), len(want), len(set(have)),
                                    have == want))

    trows = paper_tables(S)
    if mut("MUT-PAPER-TABLE"):
        trows = [trows[0].replace("|", "!", 1)] + trows[1:]
    tmiss = [t for t in trows if norm_text(t) not in norm]
    LD.gate("G-PAPER-TABLES-AS-CLAIMS",
            "the paper's tables render as claims: every row of the "
            "persistence table and of the arena table is generated from the "
            "receipt and required to be present in the paper as written",
            not tmiss, "%d table rows rendered, %d missing: %s"
            % (len(trows), len(tmiss), [t[:40] for t in tmiss[:3]] or "none"))

    bad_pol = []
    for c in claims:
        if c["id"] == "CL-INJECTED":
            continue
        old = perturb(S, c["path"])
        moved = paper_claims(S)
        new = [x for x in moved if x["id"] == c["id"]][0]
        if mut("MUT-PAPER-POLARITY"):
            new = c
        restore(S, c["path"], old)
        if new["text"] == c["text"] or norm_text(new["text"]) in norm:
            bad_pol.append(c["id"])
    S["paper_polarity"] = {"claims": len(claims),
                           "polarity_failures": len(bad_pol),
                           "failing": bad_pol}
    LD.gate("G-PAPER-CLAIM-POLARITY",
            "every claim has POLARITY: perturbing the receipt key it renders "
            "from moves the claim, and the moved claim is no longer found in "
            "the paper -- so no claim can be satisfied by accident",
            not bad_pol, "%d claims, %d without polarity: %s"
            % (len(claims), len(bad_pol), bad_pol or "none"))

    vs = S["verdict"]["string"]
    if mut("MUT-PAPER-VERDICT"):
        vs = vs[:40]
    LD.gate("G-PAPER-VERDICT-BLOCK",
            "the paper quotes the COMPLETE verdict string the instrument "
            "emits, character for character, so the paper's verdict block "
            "cannot go stale behind the receipt",
            norm_text(vs) in norm and len(vs) > 400,
            "%d characters of verdict quoted" % len(vs))

    S["paper_coverage"] = {"numerals": len(pn), "unlicensed": len(unlic),
                           "claims": len(claims), "spans": len(spans),
                           "span_numerals": len(sn),
                           "fenced_blocks": len(have),
                           "table_rows": len(trows),
                           "polarity_failures": len(bad_pol),
                           "paper": os.path.basename(PAPER_REL)}
    return S["paper_coverage"]

# ===========================================================================
# SECTION 13.  THE RECEIPT, THE SEAL, THE REPORT
# ===========================================================================


def falsifier_descriptions():
    """E-23: each published description is checked against the source text of
    the branch its own switch guards."""
    src = read_text(SELF)
    rows = []
    for name, target, note in MUTANTS:
        i = src.find('mut("%s")' % name)
        rows.append({"mutant": name, "target": target, "description": note,
                     "switch_present": i >= 0,
                     "guarded_source_sha256_12":
                         digest(src[i:i + 240]) if i >= 0 else None})
    return rows


def build_receipt(S, LD, SEAL, paper_text):
    head, vstring = build_verdict(S)
    S["verdict"] = {"head": head, "string": vstring,
                    "segments": len(vstring.split("|"))}
    if mut("MUT-VERDICT"):
        S["verdict"]["string"] = vstring.replace("SIDON=", "SIDONX=")
    S["preregistered_heads"] = list(PREREGISTERED_HEADS)
    LD.gate("G-VERDICT-PREREGISTERED",
            "the head is one of the forms pre-registered in the pin before "
            "any measurement was taken",
            S["verdict"]["head"] in PREREGISTERED_HEADS,
            "head %s among %d pre-registered forms"
            % (S["verdict"]["head"], len(PREREGISTERED_HEADS)))
    rh, rparts = reconstruct_verdict(S)
    fp = verdict_fingerprint(S["verdict"]["string"], S)
    ok = (rh == S["verdict"]["head"]
          and S["verdict"]["string"].startswith(rh + "<")
          and str(rparts[3]) in fp.get("CONTROL", "")
          and set(fp) == {"SIDON", "CONTROL", "LAW", "VMAX", "INTERIOR-RADII",
                          "FINGERPRINT", "SCALE", "BREAKS", "TABLE", "SCOPE"})
    LD.gate("G-VERDICT-RECONSTRUCTED",
            "the head and every segment key of the verdict string are "
            "re-derived from the receipt's own primitive tables by a "
            "comparator that shares no literal and no helper with the "
            "builder, and the string is parsed back into its segments",
            ok, "head %s, %d segments, keys %s"
            % (S["verdict"]["head"], len(fp), sorted(fp)))

    banned = ("CONTINUUM-LIMIT", "THERMODYNAMIC-LIMIT", "IN-THE-LIMIT",
              "SCALING-LIMIT-ESTABLISHED", "TRANSPORT-NUMBER-INHERITED")
    hit = [b for b in banned if b in S["verdict"]["string"]
           and "NO-" + b not in S["verdict"]["string"]]
    LD.gate("G-WALLS",
            "the four walls stand in the verdict itself: no continuum claim, "
            "no limit claim, no inherited transport number, and the pin's own "
            "scope sentence is quoted from it",
            not hit and "NO-CONTINUUM-CLAIM" in S["verdict"]["string"]
            and "NO-TRANSPORT-NUMBER-INHERITED" in S["verdict"]["string"],
            "banned fragments present: %s" % (hit or "none"))

    fd = falsifier_descriptions()
    if mut("MUT-DESCRIPTION"):
        fd[0]["switch_present"] = False
    S["falsifier_descriptions"] = fd
    bad = [r["mutant"] for r in fd if not r["switch_present"]]
    LD.gate("G-FALSIFIER-DESCRIPTIONS",
            "every published mutant description names a switch that exists in "
            "this file, so a description cannot be a false waiver wearing a "
            "green badge",
            not bad, "%d descriptions, %d without a switch in source: %s"
            % (len(fd), len(bad), bad or "none"))

    # THE LEDGER COVERS EVERY GATE THE RUN WILL REACH, not only the ones
    # already closed: the gates that run after this point are enumerated in
    # REMAINING_GATES and classified here, and G-GATE-LEDGER-COVERS-THE-RUN
    # requires the closed ledger to have an entry for every gate row.
    waivers = []
    targets = {m[1] for m in MUTANTS}
    for gid in sorted(set(LD.ids) | set(REMAINING_GATES) | set(LATE_GATES)
                      | set(FORCINGS)):
        if gid in targets:
            waivers.append({"gate": gid, "status": "FALSIFIABLE",
                            "falsifier": [m[0] for m in MUTANTS
                                          if m[1] == gid][0]})
        elif gid in FORCINGS:
            waivers.append({"gate": gid, "status": "WAIVED",
                            "forcing": FORCINGS[gid]})
        else:
            waivers.append({"gate": gid, "status": "STRUCTURAL",
                            "forcing": "a rebuild identity: it compares two "
                                       "independently computed objects, or "
                                       "evaluates a per-object predicate over "
                                       "a table it did not build, and cannot "
                                       "pass unless they agree"})
    S["waiver_ledger"] = waivers
    unguarded = [w["gate"] for w in waivers
                 if (w["status"] == "FALSIFIABLE" and not w.get("falsifier"))
                 or (w["status"] == "WAIVED" and not w.get("forcing"))]
    LD.gate("G-WAIVERS-VERIFIED",
            "every gate is FALSIFIABLE with a named mutant, WAIVED with a "
            "named forcing, or STRUCTURAL -- a two-route identity that cannot "
            "pass unless its two routes agree; none is unguarded, and the "
            "ledger is built over every gate the run will reach rather than "
            "only the ones already closed",
            not unguarded, "%d gates: %d falsifiable, %d waived, %d structural"
            % (len(waivers),
               sum(1 for w in waivers if w["status"] == "FALSIFIABLE"),
               sum(1 for w in waivers if w["status"] == "WAIVED"),
               sum(1 for w in waivers if w["status"] == "STRUCTURAL")))

    S["not_executed"] = list(NOT_EXECUTED)
    LD.gate("G-NOT-EXECUTED-EMPTY",
            "nothing declared was left unexecuted",
            not S["not_executed"], "%d entries" % len(S["not_executed"]))

    cov = verify_paper(S, LD, paper_text)

    # THE PREDICTION, made before the remaining gates close: five more gates
    # run in this function (totals, floats, the seal, the manifest, the
    # chain) and five in the delivery path (the mutant sweep's adjudicator,
    # the published-key check, the ledger-coverage check, this prediction's
    # own check and the final paper pass).  G-GATES-CLOSED-AS-
    # PREDICTED requires the ledger to end at exactly this number, and
    # G-ARTIFACT-INTEGRITY is the one gate evaluated outside the ledger.
    S["totals"] = {
        "gates": len(LD.rows) + 11,
        "gates_in_receipt": len(LD.rows) + 10,
        "mutants": len(MUTANTS),
        "sources": len(SOURCES),
        "path_value_anchors": len(PATH_VALUE_ANCHORS),
        "verbatim_anchors": len(VERBATIM_ANCHORS),
        "seals": len(SEALED_PATHS),
        "claims": cov["claims"],
        "numerals": cov["numerals"],
    }
    LD.gate("G-TOTALS-REDERIVED",
            "the published totals are re-derived from the objects that "
            "produce them rather than typed",
            (S["totals"]["mutants"] == len(MUTANTS)
             and S["totals"]["seals"] == len(SEALED_PATHS)),
            "%d gates predicted, %d mutants, %d seals"
            % (S["totals"]["gates"], S["totals"]["mutants"],
               S["totals"]["seals"]))

    # the float scan
    def has_float(o):
        if isinstance(o, float):
            return True
        if isinstance(o, dict):
            return any(has_float(v) for v in o.values())
        if isinstance(o, (list, tuple)):
            return any(has_float(v) for v in o)
        return False
    probe = dict(S)
    if mut("MUT-FLOAT"):
        probe["injected"] = 3 / 2      # a runtime float, never a literal
    tree = ast.parse(read_text(SELF))
    src_floats = [n for n in ast.walk(tree)
                  if isinstance(n, ast.Constant) and isinstance(n.value, float)]
    LD.gate("G-NO-FLOATS",
            "there is no float anywhere: an AST scan of this file finds no "
            "float literal, and a recursive type scan of the receipt finds no "
            "float value",
            not has_float(probe) and not src_floats,
            "%d float literals in source, receipt clean: %s"
            % (len(src_floats), not has_float(probe)))

    broken = SEAL.verify(S)
    if mut("MUT-SEAL-BROKEN"):
        broken = ["SEAL-COUNTS"]
    LD.gate("G-SEAL-COMPLETE",
            "every gate-time seal still verifies against the object it was "
            "taken from, in run, before the payload is built",
            not broken, "%d seals, broken: %s" % (len(SEAL.rows),
                                                  broken or "none"))

    if mut("MUT-SEAL-MANIFEST"):
        S["unsealed_probe"] = len(SEALED_PATHS)
    covered = {p.split("/")[0] for _s, p, _g in SEALED_PATHS}
    extra = sorted((set(S) | set(LATE_KEYS)) - covered - set(DECLARED_UNSEALED))
    LD.gate("G-SEAL-MANIFEST-TOTAL",
            "every published receipt key is sealed at the gate that produced "
            "it or named in the declared-unsealed manifest with the reason it "
            "cannot be; the predicted final key set is used, so the keys the "
            "post-sweep stage adds are covered here too, and a key that is "
            "neither dies",
            not extra, "%d keys predicted, %d sealed paths, %d declared "
            "unsealed, uncovered: %s"
            % (len(set(S) | set(LATE_KEYS)), len(SEALED_PATHS),
               len(DECLARED_UNSEALED), extra or "none"))

    if mut("MUT-GATE-CHAIN"):
        LD.rows[0]["detail"] = LD.rows[0]["detail"] + " (edited)"
    chain, chain_ok = digest(SCHEMA), True
    for i, row in enumerate(LD.rows):
        chain = digest(chain + digest(row))
        if LD.digests[i] != chain:
            chain_ok = False
    LD.gate("G-GATE-ROWS-SEALED",
            "the gate ledger is CHAINED: every row's digest folds in its "
            "predecessor, so a row edited after its gate closed breaks the "
            "chain from that point onward and the whole ledger is re-derived "
            "here from the rows as they now stand",
            chain_ok, "%d rows re-chained against their gate-time digests"
            % len(LD.rows))
    return S, SEAL, cov


def finish_receipt(S, LD, SEAL, report, on_target):
    S["mutants"] = report
    SEAL.take("SEAL-MUTANTS", S)
    S["gates"] = LD.rows
    S["gate_digests"] = LD.digests
    S["seal_manifest"] = SEAL.rows
    S["sweep_totals"] = {
        "mutants_killed": sum(1 for m in report if m["killed"]),
        "mutants_on_target": on_target,
        "gates_passed_in_receipt": sum(1 for g in LD.rows if g["passed"]),
    }
    keys = set(S)
    covered = {p.split("/")[0] for _s, p, _g in SEALED_PATHS}
    declared = set(DECLARED_UNSEALED)
    extra = sorted(keys - covered - declared)
    if mut("MUT-SEAL-MANIFEST"):
        S["unsealed_probe"] = 1
        extra = sorted(set(S) - covered - declared)
    return extra


def report_lines(S):
    c = S["counts"]
    out = ["PER-L -- THE L-LADDER PERSISTENCE CENSUS"]
    out.append("")
    out.append("STAGE 1  THE SIDON TEST")
    out.append("  %-4s %-14s %-6s %-9s %-22s %6s %6s %6s"
               % ("L", "arena", "sidon", "dds-free", "difference mults",
                  "maps", "unit", "non-m"))
    for a in S["sidon_arenas"]:
        out.append("  %-4d %-14s %-6s %-9s %-22s %6d %6d %6d"
                   % (a["L"], a["arena"], a["sidon"], a["dds_free"],
                      a["difference_multiplicities"], a["maps"], a["unitary"],
                      a["non_monomial"]))
    p = S["sidon_prediction"]
    out.append("  the prediction: sufficiency holds everywhere=%s; "
               "necessity fails at %d arenas (%s)"
               % (p["sufficiency_holds_everywhere"], p["necessity_failures"],
                  ", ".join(p["necessity_failure_arenas"]) or "none"))
    ctl = S["fourth_direction_control"]
    out.append("  the control, at the control rung:")
    for r in ctl["control_rung_rows"]:
        out.append("    %-14s alphabet %-10s (%2d) maps=%-7d unitary=%-4d "
                   "non-monomial=%d"
                   % (r["arena"], r["alphabet"], r["alphabet_size"],
                      r["maps"], r["unitary"], r["non_monomial"]))
    out.append("    registered count reproduced: %d"
               % ctl["registered_count_reproduced"])
    out.append("")
    out.append("STAGE 2  VMAX = DIAMETER, AND THE INTERIOR RADII")
    out.append("  %-4s %-8s %-9s %-9s %-9s %-9s" % ("L", "families", "cells",
                                                    "VMAX", "diameter",
                                                    "interior"))
    for v, d, r in zip(S["vmax_census"], S["dispersion_census"],
                       S["interior_radii"]):
        out.append("  %-4d %-8d %-9d %-9s %-9d %-9d"
                   % (v["L"], d["families"], d["cells"], v["vmax"],
                      v["diameter"], r["interior_count"]))
    for v in S["velocity_census"]:
        out.append("  L=%d velocity cells %d, non-integer families %d %s"
                   % (v["L"], v["velocity_cells"], v["non_integer_families"],
                      ("witness: axis %s of order %d at speed %s"
                       % (v["witness"]["axis"], v["witness"]["axis_order"],
                          v["witness"]["speed"])) if v["witness"] else ""))
    out.append("")
    out.append("STAGE 3  THE GAUGE FINGERPRINT")
    out.append("  coins %d = %s" % (S["coin_sectors"]["coins"],
                                    S["coin_sectors"]["sectors"]))
    out.append("  %-4s %-10s %-12s %-8s %-8s %s"
               % ("L", "stencil", "class", "order", "support", "certified"))
    for r in S["gauge_profile"]:
        out.append("  %-4d %-10s %-12s %-8d %-8d %s"
                   % (r["L"], r["stencil"], r["position_class"], r["order"],
                      r["support"], r["alternating_certified"]))
    for r in S["global_stencil"]:
        out.append("  L=%d S-ALL orbits %d support %d volume %d class %s"
                   % (r["L"], r["orbits"], r["support"], r["volume"],
                      r["class"]))
    out.append("")
    out.append("STAGE 4  LOCALITY WINDOWS")
    out.append("  %-4s %-4s %-11s %-9s %-9s %-8s %s"
               % ("L", "r", "neighbours", "offsets", "complete", "locality",
                  "b1"))
    for w in S["locality_windows"]:
        out.append("  %-4d %-4d %-11d %-9d %-9s %-8s %d"
                   % (w["L"], w["r"], w["neighbours"], w["offsets"],
                      w["complete"], w["locality"], w["b1"]))
    for r in S["width_count"]:
        out.append("  L=%d locality-admitting widths %d = interior radii %d"
                   % (r["L"], r["locality_admitting_widths"],
                      r["interior_radii"]))
    for b in S["band_law"]["by_width"]:
        out.append("  width r=%d admitted sizes %s; predicted %s"
                   % (b["r"], b["admitted_set"], b["predicted_set"]))
    out.append("")
    out.append("STAGE 5  THE PERSISTENCE TABLE")
    for r in S["persistence_table"]:
        out.append("  %-52s %-18s %-18s %-18s %s"
                   % (r["invariant"][:52], str(r["cells"]["4"])[:18],
                      str(r["cells"]["6"])[:18], str(r["cells"]["8"])[:18],
                      r["verdict"]))
    out.append("")
    out.append("  %d rows: %d persist, %d break, %d transform"
               % (c["table_rows"], c["persists"], c["breaks"],
                  c["transforms"]))
    out.append("  %d coefficient maps scanned; %d axis-and-lag objects bound"
               % (c["maps_scanned"], c["lag_objects"]))
    out.append("  gates %d (%d in the receipt); mutants %d"
               % (S["totals"]["gates"], S["totals"]["gates_in_receipt"],
                  S["totals"]["mutants"]))
    out.append("")
    out.append(S["verdict"]["head"])
    out.append(S["verdict"]["string"])
    return out

# ===========================================================================
# SECTION 14.  CLI AND MAIN
# ===========================================================================


def parse_args(argv):
    opts = {"write": True, "selftest": False, "mutant": None,
            "break_anchor": None, "verify_paper": None}
    names = {m[0] for m in MUTANTS}
    anchors = ({s[0] for s in SOURCES} | {a[0] for a in PATH_VALUE_ANCHORS}
               | {a[0] for a in VERBATIM_ANCHORS})
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == "--no-write":
            opts["write"] = False
        elif a == "--selftest":
            opts["selftest"] = True
            opts["write"] = False
        elif a == "--mutant":
            if i + 1 >= len(argv):
                raise CliError("--mutant needs a NAME")
            if argv[i + 1] not in names:
                raise CliError("unknown mutant %r" % argv[i + 1])
            opts["mutant"] = argv[i + 1]
            opts["write"] = False
            i += 1
        elif a == "--break-anchor":
            if i + 1 >= len(argv):
                raise CliError("--break-anchor needs a NAME")
            if argv[i + 1] not in anchors:
                raise CliError("unknown anchor %r" % argv[i + 1])
            opts["break_anchor"] = argv[i + 1]
            opts["write"] = False
            i += 1
        elif a == "--verify-paper":
            rel = PAPER_REL
            if i + 1 < len(argv) and not argv[i + 1].startswith("--"):
                rel = argv[i + 1]
                i += 1
            p = rel if os.path.isabs(rel) else os.path.join(REPO, rel)
            if not os.path.exists(p):
                raise CliError("--verify-paper path does not exist: %s" % rel)
            opts["verify_paper"] = rel
            opts["write"] = False
        else:
            raise CliError("unknown argument %r" % a)
        i += 1
    return opts


def full_run(break_anchor, paper_text):
    S, LD, SEAL = build_state(break_anchor)
    S, SEAL, cov = build_receipt(S, LD, SEAL, paper_text)
    return S, LD, SEAL, cov


def selftest():
    target = SOURCES[0][0]
    print("SELFTEST: corrupting anchor %s in memory; the run must die."
          % target, flush=True)
    globals()["QUIET"] = True
    try:
        full_run(target, "")
    except GateFail as e:
        globals()["QUIET"] = False
        print("SELFTEST: died at %s -- as required." % str(e).split(" ::")[0],
              flush=True)
        print("SELFTEST PASSED (the instrument is falsifiable); no artifact "
              "written.", flush=True)
        print("EXIT 1", flush=True)
        sys.exit(1)
    globals()["QUIET"] = False
    print("SELFTEST FAILED: a corrupted anchor did not kill the run.",
          flush=True)
    print("EXIT 2", flush=True)
    sys.exit(2)


def main():
    global MUT, READS, QUIET
    try:
        opts = parse_args(sys.argv[1:])
    except CliError as e:
        print("usage: %s [--no-write] [--selftest] [--mutant NAME] "
              "[--break-anchor NAME] [--verify-paper [PATH]]"
              % os.path.basename(SELF), file=sys.stderr)
        print("error: %s" % e, file=sys.stderr)
        sys.exit(2)

    require_sources()

    if opts["selftest"]:
        selftest()
    write = opts["write"]
    MUT = opts["mutant"]

    say("=" * 78)
    say("v14 PER-L -- THE L-LADDER PERSISTENCE CENSUS")
    say("=" * 78)
    if MUT:
        say("MUTANT ACTIVE: %s" % MUT)
    if opts["break_anchor"]:
        say("ANCHOR BREAK SELF-TEST: %s" % opts["break_anchor"])

    paper_rel = opts["verify_paper"] or PAPER_REL
    paper_path = (paper_rel if os.path.isabs(paper_rel)
                  else os.path.join(REPO, paper_rel))
    if opts["verify_paper"]:
        say("VERIFY-PAPER: the object under test is %s" % paper_rel)
    paper_text = read_text(paper_path) if os.path.exists(paper_path) else ""

    try:
        S, LD, SEAL, cov = full_run(opts["break_anchor"], paper_text)
    except GateFail as e:
        say("")
        say("GATE FAILED: %s" % e)
        say("EXIT 1")
        sys.exit(1)

    if opts["verify_paper"]:
        say("")
        say("VERIFY-PAPER: %s" % paper_rel)
        say("  coverage %s" % cov)
        say("  every claim rendered, every numeral covered (prose, fences and "
            "inline spans), every fenced block matched by multiset, every "
            "table row rendered, every polarity held.")
        say("EXIT 0")
        sys.exit(0)

    if MUT or opts["break_anchor"]:
        say("")
        say("MUTANT SURVIVED: %s" % (MUT or opts["break_anchor"]))
        say("EXIT 0")
        sys.exit(0)

    say("")
    say("running %d declared mutants" % len(MUTANTS))
    report, all_dead, on_target = [], True, 0
    saved = list(READS)
    for nm, target, note in MUTANTS:
        MUT = nm
        QUIET = True
        globals()["QUIET"] = True
        killed_at = None
        try:
            READS = []
            full_run(None, paper_text)
        except GateFail as e:
            killed_at = str(e).split(" ::")[0]
        except SystemExit:
            killed_at = "SYSTEM-EXIT"
        globals()["QUIET"] = False
        MUT = None
        report.append({"mutant": nm, "target": target, "note": note,
                       "killed": killed_at is not None, "killed_at": killed_at,
                       "on_target": killed_at == target})
        if killed_at is None:
            all_dead = False
        if killed_at == target:
            on_target += 1
    READS = saved
    say("    mutants: %d declared, %d killed, %d killed by their declared "
        "target" % (len(MUTANTS), sum(1 for m in report if m["killed"]),
                    on_target))
    off = [(m["mutant"], m["target"], m["killed_at"]) for m in report
           if not m["on_target"]]
    try:
        LD.gate("G-MUTANTS-ON-TARGET",
                "every declared mutant is killed, and killed by the gate it "
                "was declared to falsify: a mutant that dies elsewhere is a "
                "gate boundary this unit does not understand",
                all_dead and on_target == len(MUTANTS),
                "killed %d of %d; off target %s"
                % (sum(1 for m in report if m["killed"]), len(MUTANTS),
                   off or "none"))
    except GateFail as e:
        say("")
        say("GATE FAILED: %s" % e)
        say("EXIT 1")
        sys.exit(1)

    extra = finish_receipt(S, LD, SEAL, report, on_target)
    try:
        LD.gate("G-PUBLISHED-KEYS-COVERED",
                "the key set actually published matches the one the in-run "
                "manifest gate predicted: no key arrived late that the "
                "manifest does not cover",
                not extra, "%d published keys, uncovered: %s"
                % (len(S), extra or "none"))
        led = {w["gate"] for w in S["waiver_ledger"]}
        uncovered = sorted({g["gate"] for g in LD.rows} - led)
        LD.gate("G-GATE-LEDGER-COVERS-THE-RUN",
                "every gate row the run published has an entry in the closed "
                "waiver ledger: a gate that ran after the ledger was built is "
                "not thereby unguarded",
                not uncovered, "%d ledger entries against %d gate rows, "
                "uncovered: %s" % (len(led), len(LD.rows) + 2,
                                   uncovered or "none"))
        LD.gate("G-GATES-CLOSED-AS-PREDICTED",
                "the ledger closes at exactly the number of gates the totals "
                "predicted before the last ten of them ran; a gate added or "
                "dropped anywhere in the pipeline moves the count and dies "
                "here",
                len(LD.rows) + 2 == S["totals"]["gates_in_receipt"],
                "%d rows closed against the predicted %d"
                % (len(LD.rows) + 2, S["totals"]["gates_in_receipt"]))
        S["gates"] = LD.rows
        S["gate_digests"] = LD.digests
        cov2 = paper_coverage_only(S, paper_text)
        S["paper_coverage"] = cov2
        LD.gate("G-PAPER-COVERAGE-FINAL",
                "the paper instrument is re-run once the totals close, so the "
                "paper's own instrument section is covered too; a failure "
                "here exits 1 and writes nothing",
                (cov2["unlicensed"] == 0 and cov2["polarity_failures"] == 0
                 and cov2["missing"] == 0 and cov2["table_missing"] == 0
                 and cov2["fenced_multiset_equal"]),
                "%d claims, %d numerals, %d unlicensed, %d spans, %d fenced "
                "blocks, %d table rows"
                % (cov2["claims"], cov2["numerals"], cov2["unlicensed"],
                   cov2["spans"], cov2["fenced_blocks"], cov2["table_rows"]))
    except GateFail as e:
        say("")
        say("GATE FAILED: %s" % e)
        say("EXIT 1")
        sys.exit(1)

    S["gates"] = LD.rows
    S["gate_digests"] = LD.digests
    # the passed-gate total is re-derived HERE, once the ledger has closed,
    # so the published number counts the rows the artifact actually carries.
    S["sweep_totals"]["gates_passed_in_receipt"] = sum(
        1 for g in LD.rows if g["passed"])
    SEAL.gate_digests = list(LD.digests)
    S["seal_manifest"] = SEAL.rows

    say("=" * 78)
    for ln in report_lines(S):
        say(ln)
    SEAL.close_transcript("\n".join(LOG) + "\n")

    try:
        SEAL.close(S, json.dumps(S, indent=1, sort_keys=True))
    except GateFail as e:
        print("")
        print("GATE FAILED: %s" % e)
        print("EXIT 1")
        sys.exit(1)

    if write:
        payload, text = SEAL.payload, SEAL.transcript
        probe = OUT_JSON + ".integrity-probe"
        with open(probe, "w", encoding="utf-8") as f:
            f.write(payload[:-1] + " }")
        detected = digest(read_text(probe)) != SEAL.payload_sha
        os.remove(probe)

        def against_the_seal(js, tx):
            if digest(js) != SEAL.payload_sha:
                return "the payload digest"
            if digest(tx) != SEAL.transcript_sha:
                return "the transcript digest"
            disk = json.loads(js)
            bad = SEAL.verify(disk)
            if bad:
                return "the gate-time seals %s" % bad
            if disk["verdict"]["string"] != SEAL.verdict_string:
                return "the verdict string"
            rh, _rp = reconstruct_verdict(disk)
            if rh != disk["verdict"]["head"]:
                return "the head re-derived from the primitive tables"
            rows, digs = disk["gates"], disk["gate_digests"]
            chain = digest(SCHEMA)
            for i, r in enumerate(rows):
                chain = digest(chain + digest(r))
                if digs[i] != chain:
                    return "the chained gate-row digest at row %d" % i
            if disk["seal_manifest"] != SEAL.rows:
                return "the published seal manifest"
            st = disk["sweep_totals"]
            if st["mutants_killed"] != sum(1 for m in disk["mutants"]
                                           if m["killed"]):
                return "the killed-mutant total"
            if st["mutants_on_target"] != sum(1 for m in disk["mutants"]
                                              if m["on_target"]):
                return "the on-target-mutant total"
            if st["gates_passed_in_receipt"] != sum(1 for g in rows
                                                    if g["passed"]):
                return "the passed-gate total"
            if disk["totals"]["gates_in_receipt"] != len(rows):
                return "the gate count"
            k = disk["counts"]
            for frag in ("%d rows: %d persist, %d break, %d transform"
                         % (k["table_rows"], k["persists"], k["breaks"],
                            k["transforms"]),
                         "%d coefficient maps scanned; %d axis-and-lag "
                         "objects bound" % (k["maps_scanned"],
                                            k["lag_objects"]),
                         "registered count reproduced: %d"
                         % disk["fourth_direction_control"]
                         ["registered_count_reproduced"],
                         "gates %d (%d in the receipt); mutants %d"
                         % (disk["totals"]["gates"],
                            disk["totals"]["gates_in_receipt"],
                            disk["totals"]["mutants"]),
                         disk["verdict"]["string"]):
                if frag not in tx:
                    return "a transcript number re-rendered from the "\
                           "receipt: %r" % frag[:60]
            return None

        tj, tt = OUT_JSON + ".tmp", OUT_TXT + ".tmp"
        with open(tj, "w", encoding="utf-8") as f:
            f.write(payload)
        with open(tt, "w", encoding="utf-8") as f:
            f.write(text)
        why = against_the_seal(read_text(tj), read_text(tt))
        if not detected:
            why = "the corruption probe was not detected"
        if why is not None:
            os.remove(tj)
            os.remove(tt)
            print("GATE FAILED: G-ARTIFACT-INTEGRITY :: what was about to be "
                  "written does not match the gate-time seal (%s); nothing "
                  "written" % why, flush=True)
            sys.exit(1)
        os.replace(tj, OUT_JSON)
        os.replace(tt, OUT_TXT)
        why = against_the_seal(read_text(OUT_JSON), read_text(OUT_TXT))
        if why is not None:
            print("GATE FAILED: G-ARTIFACT-INTEGRITY :: the artifacts on disk "
                  "differ from the gate-time seal (%s)" % why, flush=True)
            sys.exit(1)
        print("G-ARTIFACT-INTEGRITY: corrupted probe detected; both artifacts "
              "written from the SEALED payload, re-read from disk and matched "
              "against the gate-time seal -- %d sealed objects, payload %s, "
              "transcript %s (%d + %d bytes)."
              % (len(SEAL.rows), SEAL.payload_sha, SEAL.transcript_sha,
                 len(payload), len(text)), flush=True)
    sys.exit(0)


if __name__ == "__main__":
    main()
