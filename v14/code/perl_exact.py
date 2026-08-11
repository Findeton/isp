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
from itertools import product, combinations, permutations

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

# THE SUPPORT-SIZE CEILING.  The declared alphabet's squared moduli lie in
# {0, 1/4, 1/2, 1}, so a unitary map's squared moduli sum to 1 with at most
# SUPPORT_CEILING nonzero coefficients.  The ceiling is COMPUTED from the
# rebuilt alphabet at G-SUPPORT-CEILING, never assumed -- it is what makes the
# band's ABSENCE half a finite census rather than a declared window.
SUPPORT_CEILING = 4

# THE CONTROL COSET: the order-3 coset inside the radius-3 ball at L = 9, the
# ALPHABET-RELATIVE odd-L datum.  Declared here so the disclosure the SCALE
# clause carries is measured and not asserted.
ODD_COSET_RUNG = 9
ODD_COSET_WIDTH = 3
ODD_COSET = ((0, 0), (3, 0), (6, 0))

# THE (7,4,2) DIFFERENCE-SET WITNESS: the in-alphabet, in-ball, non-monomial
# unitary at L = 7 and width 2 that the involution-pair search is structurally
# blind to (Z_7^2 has no involution at all).  Verified two ways in-run.
L7_RUNG = 7
L7_WIDTH = 2
L7_SUPPORT = ((0, 0), (0, 1), (0, 2), (0, 5))
L7_SIGNS = (1, 1, -1, 1)

# THE NINE-CHARACTERISTIC EXERCISE (the DDS theorem is field-free, and this
# unit exercises it outside characteristic zero).  The involution is the
# FROBENIUS COMPUTED IN THE FIELD -- never assumed to be b -> -b, which is
# false in characteristic 2 -- and is verified to be an order-2 (or trivial)
# field automorphism before a single map is scanned.
CHAR_P_FIELDS = (2, 3, 5, 7, 11, 4, 9, 25, 49)
CHAR_P_SCAN_WINDOW = 150000        # |F|^|S| at which a scan is run

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
    # #148: a seal is taken at the gate that CLOSES ITS VALUE.  `totals` is
    # complete at G-TOTALS-REDERIVED and is sealed there, not four hundred
    # lines and a whole mutant sweep later.
    ("SEAL-TOTALS", "totals", "G-TOTALS-REDERIVED"),
    ("SEAL-COVERAGE", "paper_coverage", "G-PAPER-COVERAGE-FINAL"),
    ("SEAL-SUCCESSOR", "successor_register", "G-SUCCESSOR-REGISTER-WRITTEN"),
    ("SEAL-BAND-CENSUS", "band_law", "G-BAND-ABSENCE-FORCED"),
    ("SEAL-L7", "l7_witness", "G-L7-DIFFERENCE-SET-WITNESS"),
    ("SEAL-ODD-COSET", "odd_coset", "G-ODD-COSET-ALPHABET-RELATIVE"),
    ("SEAL-CEILING", "support_ceiling", "G-SUPPORT-CEILING"),
    ("SEAL-INJECTIVITY", "injectivity_theorem", "G-BAND-INJECTIVITY"),
    ("SEAL-CHAR-P", "char_p_census", "G-CHAR-P-FIELD-FREE"),
    ("SEAL-JOIN", "width_radius_join",
     "G-WIDTH-RADIUS-JOIN-IS-AN-IDENTITY"),
    ("SEAL-FORCING", "persistence_forcing",
     "G-PERSISTENCE-FORCING-DECLARED"),
    ("SEAL-INSTANCES", "declared_instances",
     "G-DECLARED-INSTANCES-EXECUTED"),
    ("SEAL-DDS-WINDOW", "dds_window", "G-DDS-WINDOW"),
    ("SEAL-FRACTION-CENSUS", "fraction_census", "G-FRACTIONS-STAMPED"),
    ("SEAL-SEAL-WINDOWS", "seal_windows", "G-SEAL-WINDOWS-DECLARED"),
    ("SEAL-STRUCTURAL", "structural_registry", "G-STRUCTURAL-REGISTERED"),
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
    "G-STAGES-DECLARED":
        "a REAL binding to a pinned verbatim window rather than a rebuild "
        "identity, so it does not belong in the structural bucket: its "
        "falsifier is `--break-anchor VB-PIN-STAGES`, which corrupts the "
        "quoted window and kills the run at this gate.  No in-process mutant "
        "is declared for it because the anchor-break harness is the honest "
        "falsifier and is exercised by name",
}

# E-23, repaired.  STRUCTURAL is an EXPLICIT REGISTRY, not a default `else`:
# a gate enters it only by naming the TWO INDEPENDENTLY COMPUTED OBJECTS its
# predicate compares.  A gate that is neither a mutant target, nor waived
# with a forcing, nor registered here is UNCLASSIFIED and dies at
# G-WAIVERS-VERIFIED -- which is what the delivered default branch could not
# do.
STRUCTURAL_REGISTRY = {
    "G-DISPERSION-REPRODUCES-THE-PARENT":
        ("this unit's rebuilt cell, moving, static and distinct-profile "
         "counts at the parent rung, computed from a pool it built itself",
         "four path-value anchors read from the momentum parent's receipt at "
         "named paths"),
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
    Available at any |S|, and ONE of the two mechanisms the band carries."""
    for v, w in combinations(sorted(S), 2):
        d = ((v[0] - w[0]) % L, (v[1] - w[1]) % L)
        if (2 * d[0]) % L == 0 and (2 * d[1]) % L == 0:
            return (v, w)
    return None


_DDS4_MEMO = {}


def dds_subsets_bounded(S, L, kmax):
    """EVERY difference-doubled subset of S of size 2..kmax.

    The criterion is rewritten so that a ball of 49 offsets is a finite
    census rather than a 2^49 one: an ordered difference d and its negative
    -d are realised the same number of times unless d is an involution, in
    which case one unordered pair already realises d twice.  So

        T is difference-doubled  <=>  every unordered pair difference of T
        is an involution, or its +-class is carried by at least two of T's
        unordered pairs.

    Equivalent to `is_doubled` by construction, and G-DDS-CRITERION-AGREES
    binds the two routes against each other over every arena and every ball
    small enough to admit the naive census."""
    key = (tuple(sorted(S)), L, kmax)
    got = _DDS4_MEMO.get(key)
    if got is not None:
        return got
    B = sorted(S)
    n = len(B)
    inv = [[False] * n for _ in range(n)]
    cls = [[None] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            d = ((B[i][0] - B[j][0]) % L, (B[i][1] - B[j][1]) % L)
            nd = ((-d[0]) % L, (-d[1]) % L)
            inv[i][j] = (d == nd)
            cls[i][j] = min(d, nd)
    out = []
    for r in range(2, min(kmax, n) + 1):
        for T in combinations(range(n), r):
            ps = tuple(combinations(T, 2))
            ok = True
            for a, b in ps:
                if inv[a][b]:
                    continue
                c = cls[a][b]
                if sum(1 for x, y in ps if cls[x][y] == c) < 2:
                    ok = False
                    break
            if ok:
                out.append(tuple(B[i] for i in T))
    _DDS4_MEMO[key] = out
    return out

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


def matrix_unitary(coef, L):
    """the THIRD route, and the most literal one: build the full L^2 x L^2
    matrix U (U[s+v][s] = c_v) and check U^dag U = I entry by entry.  No
    autocorrelation identity is used -- this is the definition of unitarity
    evaluated on every one of the L^4 entries."""
    sites = list(product(range(L), repeat=2))
    idx = {s: i for i, s in enumerate(sites)}
    n = len(sites)
    U = [[ZERO] * n for _ in range(n)]
    for s in sites:
        for v, cv in coef.items():
            t = idx[((s[0] + v[0]) % L, (s[1] + v[1]) % L)]
            U[t][idx[s]] = cadd(U[t][idx[s]], cv)
    cols = [[(k, cconj(U[k][j])) for k in range(n) if U[k][j] != ZERO]
            for j in range(n)]
    checked = bad = 0
    for i in range(n):
        for j in range(n):
            acc = ZERO
            for k, cu in cols[i]:
                if U[k][j] != ZERO:
                    acc = cadd(acc, cmul(cu, U[k][j]))
            checked += 1
            if acc != (ONE if i == j else ZERO):
                bad += 1
    return {"entries": checked, "mismatches": bad, "unitary": bad == 0,
            "dimension": n}


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
# SECTION 5b.  THE DDS THEOREM OUTSIDE CHARACTERISTIC ZERO
# ===========================================================================
# The DDS theorem's proof uses exactly two properties -- the coefficient field
# has no zero divisors, and the involution takes nonzero to nonzero -- so it
# holds over ANY field equipped with an involution, the trivial involution
# included.  The delivered proof is read in characteristic 0 and nowhere else,
# so this section exercises it in nine finite fields, with the involution
# taken as the FROBENIUS COMPUTED IN THE FIELD and verified to be an order-2
# (or trivial) field automorphism.  F_4 is the hardest case and the one
# characteristic 0 cannot see: there 1 = -1, so b -> -b is the identity while
# the Frobenius is not.

_FIELD_MEMO = {}


def finite_field(q):
    """F_q for q a prime or the square of a prime, with the Frobenius.
    Returns (elements, add, mul, one, zero, frobenius, p, degree).  The
    irreducible quadratic is FOUND by exhaustion, never typed."""
    got = _FIELD_MEMO.get(q)
    if got is not None:
        return got
    prime = q > 1 and all(q % d for d in range(2, q))
    if prime:
        els = tuple(range(q))
        res = (els, lambda a, b, p=q: (a + b) % p,
               lambda a, b, p=q: (a * b) % p, 1, 0, (lambda a: a), q, 1)
        _FIELD_MEMO[q] = res
        return res
    p = None
    for cand in range(2, q):
        if cand * cand == q and all(cand % d for d in range(2, cand)):
            p = cand
    if p is None:
        raise GateFail("G-CHAR-P-FIELDS :: %d is neither a prime nor a prime "
                       "square" % q)
    u = v = None
    for uu in range(p):
        for vv in range(p):
            if all((r * r + uu * r + vv) % p for r in range(p)):
                u, v = uu, vv
                break
        if u is not None:
            break
    els = tuple((a, b) for a in range(p) for b in range(p))

    def fadd(x, y, p=p):
        return ((x[0] + y[0]) % p, (x[1] + y[1]) % p)

    def fmul(x, y, p=p, u=u, v=v):
        a, b, c = x[0] * y[0], x[0] * y[1] + x[1] * y[0], x[1] * y[1]
        return ((a - c * v) % p, (b - c * u) % p)

    def frob(x, p=p, fmul=fmul):
        r, base, e = (1, 0), x, p
        while e:
            if e & 1:
                r = fmul(r, base)
            base = fmul(base, base)
            e >>= 1
        return r

    res = (els, fadd, fmul, (1, 0), (0, 0), frob, p, 2)
    _FIELD_MEMO[q] = res
    return res


def field_involution_report(q):
    """the involution is VERIFIED, not declared: order 2 or 1, additive,
    multiplicative, exhaustively over the whole field."""
    els, fadd, fmul, one, zero, frob, p, k = finite_field(q)
    invol = all(frob(frob(e)) == e for e in els)
    additive = all(frob(fadd(a, b)) == fadd(frob(a), frob(b))
                   for a in els for b in els)
    multiplicative = all(frob(fmul(a, b)) == fmul(frob(a), frob(b))
                         for a in els for b in els)
    return {"q": q, "characteristic": p, "degree": k,
            "involution_order": 1 if all(frob(e) == e for e in els) else 2,
            "is_an_involution": invol, "additive": additive,
            "multiplicative": multiplicative,
            "one_equals_minus_one": fadd(one, one) == zero,
            "pairs_checked": len(els) * len(els) * 2}


def char_p_scan(S, q, L, dim):
    """EXHAUSTIVE over F_q^|S|: the unitary maps on the offset set S in
    (Z_L)^dim, with the Frobenius as the involution."""
    els, fadd, fmul, one, zero, frob, p, k = finite_field(q)
    if dim == 1:
        def sub(a, b):
            return (a - b) % L
    else:
        def sub(a, b):
            return ((a[0] - b[0]) % L, (a[1] - b[1]) % L)
    tab = {}
    for i, v in enumerate(S):
        for j, w in enumerate(S):
            tab.setdefault(sub(v, w), []).append((i, j))
    zd = sub(S[0], S[0])
    lags = sorted(((m, pr) for m, pr in tab.items() if m != zd),
                  key=lambda t: len(t[1]))
    cj = {e: frob(e) for e in els}
    pt = {(a, b): fmul(a, cj[b]) for a in els for b in els}
    uni = mono = 0
    for c in product(els, repeat=len(S)):
        ok = True
        for m, prs in lags:
            acc = zero
            for (i, j) in prs:
                if c[i] != zero and c[j] != zero:
                    acc = fadd(acc, pt[(c[i], c[j])])
            if acc != zero:
                ok = False
                break
        if not ok:
            continue
        acc = zero
        for (i, j) in tab[zd]:
            if c[i] != zero and c[j] != zero:
                acc = fadd(acc, pt[(c[i], c[j])])
        if acc != one:
            continue
        uni += 1
        if sum(1 for x in c if x != zero) <= 1:
            mono += 1
    return {"maps": len(els) ** len(S), "unitary": uni, "monomial": mono,
            "non_monomial": uni - mono}


def char_p_arenas():
    """the arenas the char-p exercise runs: the parent's own 3-term stencil at
    every order the order census sweeps, and the anchored link set (and the
    fourth direction) on small tori.  DDS-freeness is computed for each."""
    out = []
    for n in range(2, 9):
        S = tuple(sorted({0 % n, 1 % n, (-1) % n}))
        lift = [(x, 0) for x in S]
        free = not dds_subsets_bounded(lift, n, len(S))
        out.append(("ORD-%d" % n, S, n, 1, free))
    for L in (3, 4, 5):
        S = tuple(sorted(LINK_SET))
        out.append(("LINK-L%d" % L, S, L, 2,
                    not dds_subsets_bounded(S, L, len(S))))
    for L in (3, 4):
        S = tuple(sorted(list(LINK_SET) + [FOURTH_DIRECTION]))
        out.append(("LINK-PLUS-4TH-L%d" % L, S, L, 2,
                    not dds_subsets_bounded(S, L, len(S))))
    return out

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
    """R2's partition corollary, transported.  The adjacency is EVALUATED,
    not asserted: two sites share a chart iff they fall in the same block, so
    `drawn` counts the pairs actually found adjacent by that test and
    `possible` counts the pairs of the cell.  A cell is complete iff the two
    agree, and `cross` counts the pairs the test finds adjacent across two
    different cells -- which must be zero for a partition."""
    comps = {}
    for v in product(range(L), repeat=2):
        comps.setdefault((v[0] // b, v[1] // b), []).append(v)

    def same_chart(x, y):
        return (x[0] // b, x[1] // b) == (y[0] // b, y[1] // b)

    rows = []
    for key, cell in sorted(comps.items()):
        n = len(cell)
        drawn = sum(1 for x, y in combinations(sorted(cell), 2)
                    if same_chart(x, y))
        rows.append({"cell": list(key), "size": n, "drawn": drawn,
                     "possible": n * (n - 1) // 2,
                     "complete": drawn == n * (n - 1) // 2})
    keys = sorted(comps)
    cross = 0
    for i, j in combinations(range(len(keys)), 2):
        for x in comps[keys[i]]:
            for y in comps[keys[j]]:
                if same_chart(x, y):
                    cross += 1
    return rows, cross


def band_witness(L, r):
    """ONE of the two mechanisms the band carries: two offsets of the radius-r
    ball differing by an involution carry an explicit non-monomial unitary,
    c = 1/sqrt2 at one and i/sqrt2 at the other, both in the declared
    alphabet.  Verified by the parent's own whole-torus criterion.  This is
    NOT a decision procedure for admission -- see `band_census`, which is."""
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


# ---------------------------------------------------------------------------
# THE COMPLETED, TWO-SIDED BAND CENSUS
# ---------------------------------------------------------------------------
# The delivered band was the section of ONE construction -- the
# involution-separated pair -- and its closed form asserted evenness.  The
# census below decides admission outright, at every declared width and size,
# and both of its halves are forced:
#
#   ABSENCE, above 4r.  THEOREM (injectivity).  Lift the radius-r ball to
#   {-r..r}^2 in Z^2.  Two lifted differences lie in {-2r..2r}^2 and are
#   congruent mod L only if they differ by L.e with |L.e_i| <= 4r, so e = 0
#   whenever L >= 4r+1; the lifted difference map is then injective on the
#   ball's differences, every internal difference is realised by exactly one
#   ordered pair, and the ball is DDS-free.  `injective_lift` evaluates the
#   hypothesis directly, over the whole lifted difference box.
#
#   ABSENCE, below 4r+1.  THEOREM (the support-size ceiling).  The declared
#   alphabet's squared moduli lie in {0, 1/4, 1/2, 1}, so a unitary map's
#   squared moduli sum to 1 with at most four nonzero coefficients and the
#   profile is forced.  The whole admission question is then a FINITE census
#   over the ball's subsets of size 2, 3 and 4, which is what runs.
#
#   PRESENCE.  Constructive: an explicit map, verified by the parent's own
#   whole-torus criterion.
#
# Two mechanisms occur in the declared sweep -- the involution-separated pair
# (even L <= 4r) and the PERFECT DIFFERENCE SET (L = 7 at r = 2, the (7,4,2)
# set, in a group with no involution at all).  Evenness is NOT a law.

_CEIL_MEMO = {}


def support_ceiling(A):
    """the ceiling, COMPUTED from the rebuilt alphabet: the multisets of
    nonzero squared moduli that sum to 1, and the largest support any of them
    admits."""
    key = tuple(A)
    got = _CEIL_MEMO.get(key)
    if got is not None:
        return got
    mods = sorted({cmul(a, cconj(a)) for a in A if a != ZERO})
    vals = []
    for m in mods:
        f = m[0]
        if any(m[i] for i in range(1, DEG)) or f <= 0 or f > 1:
            raise GateFail("G-SUPPORT-CEILING :: a squared modulus is not a "
                           "rational in (0, 1]: %s" % cstr(m))
        vals.append(f)
    vals = sorted(set(vals))
    sols = []

    def rec(cur, rem, start):
        if rem == 0:
            sols.append(tuple(cur))
            return
        if rem < 0 or len(cur) > 16:
            return
        for i in range(start, len(vals)):
            rec(cur + [vals[i]], rem - vals[i], i)

    rec([], Fraction(1), 0)
    by_size = {}
    for s in sols:
        by_size.setdefault(len(s), []).append([str(x) for x in s])
    res = {"squared_moduli": [str(v) for v in vals],
           "profiles": {str(k): v for k, v in sorted(by_size.items())},
           "ceiling": max(len(s) for s in sols)}
    _CEIL_MEMO[key] = res
    return res


def injective_lift(L, r):
    """the injectivity theorem's hypothesis, evaluated: distinct lifted
    differences in {-2r..2r}^2 stay distinct modulo L."""
    seen = {}
    collisions = 0
    for d in product(range(-2 * r, 2 * r + 1), repeat=2):
        k = (d[0] % L, d[1] % L)
        if k in seen and seen[k] != d:
            collisions += 1
        else:
            seen[k] = d
    return {"L": L, "r": r, "box": (4 * r + 1) ** 2, "collisions": collisions,
            "injective": collisions == 0, "threshold": 4 * r + 1}


_BAND_MEMO = {}


def band_census(L, r, A):
    """DECIDES admission at (L, r) over the declared alphabet: is there a
    non-monomial unitary supported inside the radius-r ball?

    Exhaustive by the ceiling: every difference-doubled subset of the ball of
    size 2..SUPPORT_CEILING is enumerated, and on each the coefficient maps
    with the forced modulus profile are scanned, the global phase fixed.  A
    witness is verified by the parent's own whole-torus criterion before it
    is returned.  When none is found the scan is exhaustive and the ABSENCE
    is measured, not declared."""
    key = (L, r, tuple(A))
    got = _BAND_MEMO.get(key)
    if got is not None:
        return got
    B = ball(L, r)
    subs = dds_subsets_bounded(B, L, SUPPORT_CEILING)
    by_mod = {}
    for i, a in enumerate(A):
        if a == ZERO:
            continue
        m = cmul(a, cconj(a))
        by_mod.setdefault(m[0], []).append(i)
    ceil = support_ceiling(A)
    prof = {int(k): [[Fraction(x) for x in p] for p in v]
            for k, v in ceil["profiles"].items()}
    pt = [[cmul(A[i], cconj(A[j])) for j in range(len(A))]
          for i in range(len(A))]
    tested = 0
    witness = None
    for T in subs:
        k = len(T)
        if k not in prof or witness is not None:
            continue
        tab = lag_structure(list(T), L)
        lags = sorted(((m, pr) for m, pr in tab.items() if m != (0, 0)),
                      key=lambda t: len(t[1]))
        for profile in prof[k]:
            for perm in set(permutations(profile)):
                pools = [by_mod.get(slot, []) for slot in perm]
                if not all(pools):
                    continue
                pools = [pools[0][:1]] + pools[1:]     # the global phase
                for c in product(*pools):
                    tested += 1
                    ok = True
                    for m, prs in lags:
                        acc = ZERO
                        for (i, j) in prs:
                            acc = cadd(acc, pt[c[i]][c[j]])
                        if acc != ZERO:
                            ok = False
                            break
                    if not ok:
                        continue
                    coef = {T[i]: A[c[i]] for i in range(k)}
                    if not autocorr_is_delta(coef, L):
                        raise GateFail(
                            "G-BAND-CENSUS :: a census witness fails the "
                            "parent's whole-torus criterion at L=%d r=%d"
                            % (L, r))
                    witness = {"support": [list(v) for v in T],
                               "size": k,
                               "coefficients": [cstr(A[c[i]])
                                                for i in range(k)],
                               "radius": max(torus_absmax(v, L) for v in T),
                               "difference_multiplicities":
                                   sorted(diff_multiset(list(T), L).values(),
                                          reverse=True),
                               "mechanism": ("INVOLUTION-PAIR" if k == 2 else
                                             "PERFECT-DIFFERENCE-SET" if
                                             len(set(diff_multiset(
                                                 list(T), L).values())) == 1
                                             and k == 4 else
                                             "DIFFERENCE-DOUBLED-SUBSET")}
                    break
                if witness is not None:
                    break
            if witness is not None:
                break
    res = {"L": L, "r": r, "ball": len(B), "dds_subsets": len(subs),
           "maps_tested": tested, "witness": witness,
           "carries_a_non_monomial": witness is not None,
           "exhaustive": witness is None,
           "injectivity": injective_lift(L, r)}
    _BAND_MEMO[key] = res
    return res

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

# E-23, REPAIRED.  A published description is bound to its branch TWO ways:
#   (1) its leading VERB must lie in the verb set of its declared EFFECT
#       CLASS, so an inverted description ("drops" -> "adds") changes the
#       class and dies -- which is the injection the delivered gate survived;
#   (2) the source text of the branch its own switch guards is DIGESTED and
#       the digest is PINNED in this frozen table, so editing the code
#       without editing the description dies too.
# The switch-existence test that used to stand alone is kept as the third leg.
VERB_CLASSES = {
    "SHRINK": ("drops", "shortens", "shrinks", "removes", "truncates",
               "hides", "deletes", "narrows"),
    "GROW": ("adds", "appends", "publishes", "emits", "widens", "inserts",
             "admits"),
    "MOVE": ("moves", "edits", "flips", "rewrites", "reports", "marks",
             "returns", "inverts", "corrupts", "breaks", "injects",
             "declares", "perturbs", "replaces"),
}

MUTANTS = [
    ("MUT-SOURCE-DIGEST", "G-SOURCES-PINNED", "MOVE",
     "corrupts one pinned source digest before the byte anchors are checked"),
    ("MUT-PATH-VALUE", "G-PATH-VALUE-ANCHORS", "MOVE",
     "moves one path-value anchor's read value away from its declaration"),
    ("MUT-VERBATIM-FRAGMENT", "G-VERBATIM-ANCHORS", "SHRINK",
     "shortens one verbatim window below the declared length floor"),
    ("MUT-EXTRA-READ", "G-RUNTIME-INPUTS-ENUMERATED", "GROW",
     "appends an undeclared path to the runtime read list"),
    ("MUT-FLOAT", "G-NO-FLOATS", "MOVE",
     "injects a float into the receipt before the type scan"),
    ("MUT-ALPHABET", "G-ALPHABET-REBUILT", "SHRINK",
     "drops one element from the rebuilt coefficient alphabet"),
    ("MUT-AXIS-DROP", "G-AXIS-SET-EXHAUSTIVE", "SHRINK",
     "drops one axis from the axis set at the parent rung"),
    ("MUT-LAG", "G-LAG-SUPPORT-STRUCTURAL", "MOVE",
     "declares one lag of the difference table to be empty when it is not"),
    ("MUT-POOL", "G-POOL-REPRODUCES-THE-PARENT", "SHRINK",
     "shortens the rebuilt pool at the parent rung by one generator"),
    ("MUT-GAUGE-ORBIT", "G-GAUGE-ORBITS-FREE", "SHRINK",
     "shrinks one recorded global-phase orbit below the group's size"),
    ("MUT-TWO-ROUTE", "G-TWO-ROUTE-POOL", "MOVE",
     "perturbs the second, whole-torus pool route's count at the parent rung"),
    ("MUT-ORD", "G-ORD-CENSUS-REPRODUCED", "MOVE",
     "moves one order-census non-monomial count away from the parent's"),
    ("MUT-SIDON", "G-SIDON-MEASURED", "MOVE",
     "reports one arena as Sidon whose difference multiset is not"),
    ("MUT-DDS", "G-DDS-CRITERION-SOUND", "MOVE",
     "reports a DDS-free arena as carrying a non-monomial unitary"),
    ("MUT-SIDON-VERDICT", "G-SIDON-PREDICTION-TESTED", "MOVE",
     "flips one arena's prediction verdict away from its own two measured "
     "legs"),
    ("MUT-SUFFICIENCY-SPLIT", "G-SUFFICIENCY-DENOMINATOR-HONEST", "MOVE",
     "moves the count of substantively holding Sidon arenas away from the "
     "per-arena legs it is summed from"),
    ("MUT-CONTROL", "G-FOURTH-DIRECTION-CONTROL", "MOVE",
     "moves the reproduced non-monomial count at the control arena"),
    ("MUT-FROBENIUS", "G-CHAR-P-INVOLUTIONS", "MOVE",
     "reports the Frobenius of a quadratic extension as the trivial "
     "involution"),
    ("MUT-CHAR-P", "G-CHAR-P-FIELD-FREE", "MOVE",
     "reports one finite-field scan as DDS-free while carrying a "
     "non-monomial unitary"),
    ("MUT-EIGEN", "G-EIGENVALUES-ROOTS-OF-UNITY", "MOVE",
     "marks one dispersion cell as lying off the root-of-unity lattice"),
    ("MUT-EIGENLATTICE", "G-EIGENPHASE-LATTICE", "MOVE",
     "reports the eigenphase lattice at one rung as the parent rung's"),
    ("MUT-VMAX", "G-VMAX-IS-DIAMETER", "MOVE",
     "moves the measured maximal group speed at one rung"),
    ("MUT-ATTAINED", "G-VMAX-ATTAINED-BY-THE-ANTIPODE", "SHRINK",
     "removes the antipodal monomial witness at one rung"),
    ("MUT-INTERIOR", "G-INTERIOR-RADII", "SHRINK",
     "drops one interior radius at the rung the register names"),
    ("MUT-VELOCITY", "G-INTEGER-VELOCITY-CENSUS", "SHRINK",
     "hides the non-integer velocity witness at the rung that carries it"),
    ("MUT-ONE-MECHANISM", "G-MONOMIAL-VELOCITY-IS-AN-INTEGER", "MOVE",
     "reports a monomial family as carrying a non-integer velocity"),
    ("MUT-COIN", "G-COIN-ALPHABET-DERIVED", "SHRINK",
     "drops one coin from the derived coin family"),
    ("MUT-STRATA", "G-STRATA-PERFECT-MATCHINGS", "MOVE",
     "reports one parity stratum as covering a site twice"),
    ("MUT-WRAP", "G-NON-WRAPPING", "MOVE",
     "reports a declared plaquette stencil as wrapping when it does not"),
    ("MUT-PROFILE", "G-PROFILE-PERSISTS", "MOVE",
     "moves one measured group order in the (order, support) profile"),
    ("MUT-ALT", "G-ALTERNATING-ON-ORBITS", "MOVE",
     "moves the predicted alternating order at one rung and stencil, so the "
     "certificate no longer closes"),
    ("MUT-GLOBAL", "G-GLOBAL-SUPPORT-IS-THE-VOLUME", "SHRINK",
     "shrinks the global stencil's measured support below the volume"),
    ("MUT-LOCALITY", "G-LOCALITY-WINDOWS", "MOVE",
     "flips one window's locality flag away from its own completeness test"),
    ("MUT-WIDTH", "G-WIDTH-COUNT-EQUALS-INTERIOR-RADII", "MOVE",
     "moves the count of locality-admitting widths at one rung"),
    ("MUT-JOIN", "G-WIDTH-RADIUS-JOIN-IS-AN-IDENTITY", "SHRINK",
     "drops one width from the measured locality-admitting set at one size, "
     "so it no longer equals the interior radii"),
    ("MUT-PARTITION", "G-PARTITION-COROLLARY", "SHRINK",
     "drops one drawn adjacency from a blockwise cell, so the cell is no "
     "longer a clique"),
    ("MUT-CEILING", "G-SUPPORT-CEILING", "MOVE",
     "moves the computed support ceiling away from the declared one"),
    ("MUT-INJECTIVITY", "G-BAND-INJECTIVITY", "GROW",
     "adds a collision to one lifted difference box, so its measured "
     "injectivity leaves the 4r+1 threshold"),
    ("MUT-DDS-ROUTES", "G-DDS-CRITERION-AGREES", "SHRINK",
     "drops one subset from the naive difference-doubled census, so the two "
     "routes no longer agree"),
    ("MUT-DDS-WINDOW", "G-DDS-WINDOW", "MOVE",
     "reports an arena wider than the declared subset window"),
    ("MUT-BAND", "G-BAND-LAW", "SHRINK",
     "drops one admitted size out of the measured band at one width"),
    ("MUT-BAND-ABSENCE", "G-BAND-ABSENCE-FORCED", "MOVE",
     "reports one excluded cell as neither locality-blocked nor exhausted"),
    ("MUT-BAND-PAIR", "G-BAND-PAIR-MECHANISM", "MOVE",
     "moves one size out of the involution-pair mechanism's own section"),
    ("MUT-L7-WITNESS", "G-L7-DIFFERENCE-SET-WITNESS", "MOVE",
     "flips one sign of the difference-set witness's coefficient map"),
    ("MUT-L7-SECTION", "G-L7-IN-THE-SECTION", "MOVE",
     "reports the difference-set cell as carrying an involution pair"),
    ("MUT-ODD-COSET", "G-ODD-COSET-ALPHABET-RELATIVE", "MOVE",
     "moves the order-3 coset's non-monomial count over the probe alphabet"),
    ("MUT-TABLE", "G-PERSISTENCE-TABLE-BOUND", "MOVE",
     "rewrites one persistence verdict away from its own measured cells"),
    ("MUT-FORCING", "G-PERSISTENCE-FORCING-DECLARED", "MOVE",
     "marks a BREAKS row FORCED, which names no theorem and is not a "
     "survival"),
    ("MUT-SUCCESSOR", "G-SUCCESSOR-REGISTER-WRITTEN", "SHRINK",
     "drops one part from the three-part record of the registered "
     "prediction"),
    ("MUT-ARENA-DECLARED", "G-ARENA-DECLARED", "MOVE",
     "moves the declared control rung away from the one the run uses"),
    ("MUT-CHOICES", "G-CHOICES-INVENTORIED", "MOVE",
     "moves a priced choice's instance count away from the number of "
     "instances its sweep executed"),
    ("MUT-INSTANCE-PLAN", "G-DECLARED-INSTANCES-EXECUTED", "GROW",
     "adds a planned instance to a declared sweep that the run never "
     "executes"),
    ("MUT-NOT-EXECUTED", "G-NOT-EXECUTED-EMPTY", "GROW",
     "appends a declared instance to the not-executed list"),
    ("MUT-VACUOUS-GATE", "G-WAIVERS-VERIFIED", "GROW",
     "adds a gate that binds nothing to the set the waiver ledger must "
     "classify"),
    ("MUT-STRUCTURAL-STALE", "G-STRUCTURAL-REGISTERED", "SHRINK",
     "removes a registered structural gate from the set of gates the run "
     "reaches"),
    ("MUT-TOTALS", "G-TOTALS-REDERIVED", "MOVE",
     "moves one published total away from the object that produces it"),
    ("MUT-FRACTION", "G-FRACTIONS-STAMPED", "GROW",
     "adds a fraction to the paper's scanned text with neither a measure nor "
     "the COUNTING-ONLY stamp"),
    ("MUT-VERDICT", "G-VERDICT-RECONSTRUCTED", "MOVE",
     "edits the verdict string after its segments are derived"),
    ("MUT-HEAD", "G-VERDICT-PREREGISTERED", "MOVE",
     "replaces the head with one that is not a pre-registered form"),
    ("MUT-WALLS", "G-WALLS", "GROW",
     "inserts a continuum claim into the scope segment"),
    ("MUT-DESCRIPTION", "G-FALSIFIER-DESCRIPTIONS", "MOVE",
     "inverts the leading verb of one published mutant description, leaving "
     "its code untouched"),
    ("MUT-SEAL-BROKEN", "G-SEAL-COMPLETE", "MOVE",
     "edits a sealed object after its gate-time digest was taken"),
    ("MUT-SEAL-WINDOW", "G-SEAL-WINDOWS-DECLARED", "SHRINK",
     "removes one declared seal from the takes the run performed, as a seal "
     "homed to a gate that closes before its value exists would be"),
    ("MUT-SEAL-MANIFEST", "G-SEAL-MANIFEST-TOTAL", "GROW",
     "publishes a receipt key that is neither sealed nor declared unsealed"),
    ("MUT-GATE-CHAIN", "G-GATE-ROWS-SEALED", "MOVE",
     "edits the detail of a closed gate row after its digest entered the "
     "chain"),
    ("MUT-PAPER-CLAIM", "G-PAPER-CLAIMS", "GROW",
     "adds a measured claim the paper does not make"),
    ("MUT-PAPER-NUMERAL", "G-PAPER-NUMERAL-COVERAGE", "GROW",
     "adds an unlicensed numeral to the paper's scanned set"),
    ("MUT-PAPER-SPAN", "G-PAPER-INLINE-SPANS", "GROW",
     "adds an inline code span carrying an unlicensed numeral to the scanned "
     "span list"),
    ("MUT-PAPER-FENCE", "G-PAPER-FENCED-MULTISET", "SHRINK",
     "drops one copy of a duplicated fenced block from the rendered "
     "multiset"),
    ("MUT-PAPER-TABLE", "G-PAPER-TABLES-AS-CLAIMS", "MOVE",
     "moves one rendered table row away from the paper's"),
    ("MUT-PAPER-POLARITY", "G-PAPER-CLAIM-POLARITY", "MOVE",
     "returns an unmoved claim after its receipt key was perturbed"),
    ("MUT-PAPER-VERDICT", "G-PAPER-VERDICT-BLOCK", "SHRINK",
     "truncates the verdict string the paper is required to quote"),
]

# The digest of the 240 source characters beginning at each switch, PINNED.
# Editing a branch without editing its published description moves the digest
# and dies at G-FALSIFIER-DESCRIPTIONS; editing the description without
# editing the branch changes the verb class and dies at the same gate.
MUTANT_CODE_DIGESTS = {
    "MUT-SOURCE-DIGEST": "7e6cd1e223bc",
    "MUT-PATH-VALUE": "d50a99ba4ddb",
    "MUT-VERBATIM-FRAGMENT": "405c1952166d",
    "MUT-EXTRA-READ": "9d7cf3ec8e8a",
    "MUT-FLOAT": "f627494873b9",
    "MUT-ALPHABET": "0077707563e6",
    "MUT-AXIS-DROP": "d37401db9e6f",
    "MUT-LAG": "be114659153a",
    "MUT-POOL": "5cb9bd82e0dc",
    "MUT-GAUGE-ORBIT": "ad5c75b6f924",
    "MUT-TWO-ROUTE": "c7bb87ab0b2b",
    "MUT-ORD": "4f12fff3a44d",
    "MUT-SIDON": "406d09d44b69",
    "MUT-DDS": "fa514afb73cd",
    "MUT-SIDON-VERDICT": "c1cb0df8a47c",
    "MUT-SUFFICIENCY-SPLIT": "37b489c1dfff",
    "MUT-CONTROL": "628ab9dbf735",
    "MUT-FROBENIUS": "11f3523423ec",
    "MUT-CHAR-P": "f2c81f0acd82",
    "MUT-EIGEN": "c9419d7326eb",
    "MUT-EIGENLATTICE": "c34f96b0e092",
    "MUT-VMAX": "2e755ecf25d6",
    "MUT-ATTAINED": "be8559e4afe2",
    "MUT-INTERIOR": "1e6f8bc54e40",
    "MUT-VELOCITY": "51b8c6f568cd",
    "MUT-ONE-MECHANISM": "a537bf9520c1",
    "MUT-COIN": "26c5dc528091",
    "MUT-STRATA": "9adf674d9d2f",
    "MUT-WRAP": "9ca644b963d8",
    "MUT-PROFILE": "d132fd527d76",
    "MUT-ALT": "578992fb2852",
    "MUT-GLOBAL": "adea165eabd2",
    "MUT-LOCALITY": "097c4cabbc3a",
    "MUT-WIDTH": "a18210c35960",
    "MUT-JOIN": "c587a38be0c7",
    "MUT-PARTITION": "8dcf5bedcfdd",
    "MUT-CEILING": "b555962527cf",
    "MUT-INJECTIVITY": "9e64a6ec685e",
    "MUT-DDS-ROUTES": "6c0961472412",
    "MUT-DDS-WINDOW": "b6d1e821bcee",
    "MUT-BAND": "677e1ea91b9d",
    "MUT-BAND-ABSENCE": "39f02498bf3c",
    "MUT-BAND-PAIR": "0973c3eef4ae",
    "MUT-L7-WITNESS": "3f871fe96a4c",
    "MUT-L7-SECTION": "9229e9a98a91",
    "MUT-ODD-COSET": "c7560407d589",
    "MUT-TABLE": "aaed360df6ab",
    "MUT-FORCING": "92c9153c33e3",
    "MUT-SUCCESSOR": "51f376dd7eed",
    "MUT-ARENA-DECLARED": "fbbb45aad495",
    "MUT-CHOICES": "a2484bab63ad",
    "MUT-INSTANCE-PLAN": "749c657494c2",
    "MUT-NOT-EXECUTED": "a89754cefc5f",
    "MUT-VACUOUS-GATE": "19cf25222d09",
    "MUT-STRUCTURAL-STALE": "fd2096c8458a",
    "MUT-TOTALS": "8895d577e545",
    "MUT-FRACTION": "908f85a3fe7e",
    "MUT-VERDICT": "57be912094ab",
    "MUT-HEAD": "15569405a56a",
    "MUT-WALLS": "7926bd22ab66",
    "MUT-DESCRIPTION": "8973a61823bd",
    "MUT-SEAL-BROKEN": "b506d7b08d1b",
    "MUT-SEAL-WINDOW": "6f097b05b66d",
    "MUT-SEAL-MANIFEST": "c0e4d175463a",
    "MUT-GATE-CHAIN": "ebd45f64db48",
    "MUT-PAPER-CLAIM": "58896be0bf3a",
    "MUT-PAPER-NUMERAL": "9c5e9329aa19",
    "MUT-PAPER-SPAN": "191b8206491b",
    "MUT-PAPER-FENCE": "0e215bbc25b9",
    "MUT-PAPER-TABLE": "a4b73c675b9d",
    "MUT-PAPER-POLARITY": "cf996157a909",
    "MUT-PAPER-VERDICT": "495fbfc6e9d2",
}

# the receipt keys the post-sweep stage adds; the in-run manifest gate uses
# the PREDICTED final key set so that no key escapes it by arriving late.
LATE_KEYS = ("mutants", "gates", "gate_digests", "seal_manifest",
             "sweep_totals")

# the gates that still run after the waiver ledger closes; the ledger is built
# over these too, so no gate is published without a falsifier or a forcing.
REMAINING_GATES = ("G-TOTALS-REDERIVED", "G-NO-FLOATS", "G-SEAL-COMPLETE",
                   "G-SEAL-WINDOWS-DECLARED", "G-SEAL-MANIFEST-TOTAL",
                   "G-GATE-ROWS-SEALED", "G-STRUCTURAL-REGISTERED",
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
    global READS, NOT_EXECUTED
    READS = []
    NOT_EXECUTED = []
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
        "support_ceiling": SUPPORT_CEILING,
        "char_p_fields": list(CHAR_P_FIELDS),
        "char_p_scan_window": CHAR_P_SCAN_WINDOW,
        "odd_coset": {"L": ODD_COSET_RUNG, "width": ODD_COSET_WIDTH,
                      "support": [list(v) for v in ODD_COSET]},
        "difference_set_witness": {"L": L7_RUNG, "width": L7_WIDTH,
                                   "support": [list(v) for v in L7_SUPPORT]},
        "family_generalisation_rule":
            "R4's construction applied verbatim at each rung: axes = every "
            "nonzero offset modulo sign (exhaustive); stencil = the parent's "
            "3-term {0, a, -a}; alphabet = the parent's 25, fixed; quotient = "
            "the parent's global-phase gauge.  Fiber: the axis count at that "
            "rung, every instance run.",
        "probe_alphabets": [n for n, _a in PROBE_ALPHABETS],
    }
    ad = S["arena_declaration"]
    if mut("MUT-ARENA-DECLARED"):
        ad = dict(ad)
        ad["control_rung"] = PARENT_RUNG
    # #15: the declaration must match EVERY coordinate the run uses -- the
    # control rung included, which the delivered scope segment omitted.
    ad_bad = [k for k, v in (
        ("ladder", list(LADDER)), ("parent_rung", PARENT_RUNG),
        ("control_rung", CONTROL_RUNG),
        ("link_set", [list(v) for v in LINK_SET]),
        ("fourth_direction", list(FOURTH_DIRECTION)),
        ("widths", list(WIDTHS)), ("band_sizes", list(BAND_SIZES)),
        ("dds_subset_window", DDS_SUBSET_WINDOW),
        ("plaquette_stencils", [n for n, _o in PLAQ_STENCILS]),
        ("probe_alphabets", [n for n, _a in PROBE_ALPHABETS]),
        ("dimension", pv("PV-D")), ("alphabet", pv("PV-ALPHABET")),
        ("stencil", pv("PV-STENCIL")), ("connective", pv("PV-CONNECTIVE")),
        ("forcing_link", pv("PV-FORCING-LINK"))) if ad.get(k) != v]
    ad_bad += [k for k in ("family_generalisation_rule", "support_ceiling",
                           "char_p_fields") if not ad.get(k)]
    ad_bad += ([] if ad["control_rung"] not in ad["ladder"]
               else ["control_rung-collides-with-the-ladder"])
    LD.gate("G-ARENA-DECLARED",
            "the arena is data and the declaration matches EVERY coordinate "
            "the run uses: the ladder, the parent rung, the CONTROL RUNG, the "
            "link set, the fourth direction, the widths, the band sweep, the "
            "subset window, the plaquette stencils, the probe alphabets, the "
            "dimension, the alphabet, the stencil, the connective, the "
            "forcing link and the generalisation rule are each compared "
            "against the value the run carries, one by one",
            not ad_bad, "%d declared coordinates checked, failing: %s"
            % (len(ad), ad_bad or "none"))

    stages_row = [r for r in vb_rows if r["anchor"] == "VB-PIN-STAGES"][0]
    LD.gate("G-STAGES-DECLARED",
            "the pin's five stages are the ones run, and the pin's own "
            "sentence requiring a per-arena PASS/FAIL is quoted from it -- a "
            "real binding, falsifiable by breaking that anchor",
            stages_row["present"] and stages_row["long_enough"],
            "the pin's prediction-ledger sentence is present at "
            "VB-PIN-STAGES (%d chars, floor %d)"
            % (stages_row["chars"], stages_row["floor"]))

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
                   "over any FIELD EQUIPPED WITH AN INVOLUTION (the trivial "
                   "involution included).  The proof uses exactly two "
                   "properties: a product of two nonzero elements is nonzero, "
                   "and the involution takes nonzero to nonzero",
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

    # ---- the theorem OUTSIDE characteristic zero -------------------------
    fld_rows = [field_involution_report(q) for q in CHAR_P_FIELDS]
    if mut("MUT-FROBENIUS"):
        fld_rows[5] = dict(fld_rows[5])
        fld_rows[5]["involution_order"] = 1
    bad_f = [r["q"] for r in fld_rows
             if not (r["is_an_involution"] and r["additive"]
                     and r["multiplicative"])]
    non_trivial = [r["q"] for r in fld_rows if r["involution_order"] == 2]
    char2 = [r["q"] for r in fld_rows
             if r["one_equals_minus_one"] and r["involution_order"] == 2]
    LD.gate("G-CHAR-P-INVOLUTIONS",
            "the involution used outside characteristic zero is the FROBENIUS "
            "COMPUTED IN THE FIELD, verified exhaustively to be an order-2 "
            "(or trivial) field automorphism -- never assumed to be b -> -b, "
            "which is the identity in characteristic 2 -- and at least one "
            "declared field has 1 = -1 with a NON-TRIVIAL involution, which "
            "is the case characteristic zero cannot exhibit",
            not bad_f and char2,
            "%d fields, %d with a non-trivial involution (%s), %d with "
            "1 = -1 and a non-trivial involution (%s), %d failing: %s"
            % (len(fld_rows), len(non_trivial), non_trivial, len(char2),
               char2, len(bad_f), bad_f or "none"))

    cp_rows, cp_skipped = [], []
    for q in CHAR_P_FIELDS:
        for nm, St, n, dim, free in char_p_arenas():
            if len(finite_field(q)[0]) ** len(St) > CHAR_P_SCAN_WINDOW:
                cp_skipped.append({"q": q, "arena": nm,
                                   "maps": len(finite_field(q)[0]) ** len(St),
                                   "window": CHAR_P_SCAN_WINDOW})
                continue
            sc = char_p_scan(list(St), q, n, dim)
            cp_rows.append({"q": q, "arena": nm, "group_order": n,
                            "dimension": dim, "dds_free": free,
                            "maps": sc["maps"], "unitary": sc["unitary"],
                            "monomial": sc["monomial"],
                            "non_monomial": sc["non_monomial"]})
    if mut("MUT-CHAR-P"):
        cp_rows[0] = dict(cp_rows[0])
        cp_rows[0]["dds_free"] = True
        cp_rows[0]["non_monomial"] = 1
    S["char_p_census"] = {
        "fields": fld_rows, "rows": cp_rows,
        "scan_window": CHAR_P_SCAN_WINDOW,
        "scans": len(cp_rows),
        "outside_the_window": cp_skipped,
        "dds_free_rows": sum(1 for r in cp_rows if r["dds_free"]),
        "violations": [(r["q"], r["arena"]) for r in cp_rows
                       if r["dds_free"] and r["non_monomial"]],
        "note": "the DDS theorem's field-freeness EXERCISED, not merely "
                "proved: every scan is exhaustive over F_q^|S| with the "
                "Frobenius as the involution"}
    LD.gate("G-CHAR-P-FIELD-FREE",
            "the DDS theorem is exercised outside characteristic zero: at "
            "every declared finite field and every declared arena small "
            "enough for an exhaustive scan, a DDS-free offset set carries no "
            "non-monomial unitary -- the field-freeness is measured in nine "
            "characteristics rather than read off a proof written in one",
            not S["char_p_census"]["violations"],
            "%d exhaustive scans over %d fields, %d of them DDS-free, %d "
            "violations: %s"
            % (len(cp_rows), len(CHAR_P_FIELDS),
               S["char_p_census"]["dds_free_rows"],
               len(S["char_p_census"]["violations"]),
               S["char_p_census"]["violations"] or "none"))

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
    # E-24 / #34: the sufficiency direction is a material implication, so at
    # every arena whose antecedent is FALSE it holds VACUOUSLY.  The honest
    # denominator is the Sidon arenas, and the split is published.
    subst = [p for p in pred_rows if p["sidon"]]
    vac = [p for p in pred_rows if not p["sidon"]]
    n_subst = sum(1 for p in subst if p["sufficiency_holds"])
    if mut("MUT-SUFFICIENCY-SPLIT"):
        n_subst -= 1
    S["sidon_prediction"] = {
        "quoted": [r["sha256_12"] for r in vb_rows
                   if r["anchor"] == "VB-SIDON"][0],
        "rows": pred_rows,
        "sufficiency_holds_everywhere": suff,
        "sufficiency_substantive": len(subst),
        "sufficiency_substantive_holding": n_subst,
        "sufficiency_vacuous": len(vac),
        "sufficiency_split_note":
            "the sufficiency direction is the material implication "
            "(not Sidon) or monomial-only, so it holds VACUOUSLY at every "
            "arena that is not Sidon.  It is substantively tested at the "
            "Sidon arenas alone",
        "necessity_failures": len(nec_fail),
        "necessity_failure_arenas": ["L=%d %s" % (p["L"], p["arena"])
                                     for p in nec_fail],
        "necessity_failure_rungs": sorted({p["L"] for p in nec_fail}),
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
    sp = S["sidon_prediction"]
    LD.gate("G-SUFFICIENCY-DENOMINATOR-HONEST",
            "the sufficiency count is split at its own antecedent: the "
            "material implication holds VACUOUSLY at every non-Sidon arena, "
            "so the substantive denominator is the Sidon arenas and the "
            "vacuous confirmations are published beside it rather than "
            "folded into the headline",
            (sp["sufficiency_substantive"] + sp["sufficiency_vacuous"]
             == len(pred_rows)
             and sp["sufficiency_substantive"]
             == sum(1 for r in arenas if r["sidon"])
             and sp["sufficiency_substantive_holding"]
             == sp["sufficiency_substantive"]),
            "%d substantive (all holding: %s) + %d vacuous = %d arenas"
            % (sp["sufficiency_substantive"],
               sp["sufficiency_substantive_holding"]
               == sp["sufficiency_substantive"],
               sp["sufficiency_vacuous"], len(pred_rows)))

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
                   "velocity": w["non_integer"][0][2],
                   "speed": w["non_integer"][0][2].lstrip("-"),
                   "momentum": list(w["non_integer"][0][0]),
                   "direction": w["non_integer"][0][1]}
        # THE ONE MECHANISM.  A monomial generator is a shift by an offset o,
        # whose symbol advances by a fixed step per momentum step, so its
        # velocity is -o -- an INTEGER at every rung, by the parent's own
        # forced normalisation.  Every non-integer velocity therefore lives
        # on the NON-MONOMIAL residue, which is exactly the residue the DDS
        # criterion still permits.  Both halves are measured here.
        mono_ni = [g for g, v in zip(pools[L], vel_all[L])
                   if g["monomial"] and v["non_integer"]]
        if mut("MUT-ONE-MECHANISM") and L == 6:
            mono_ni = [pools[L][0]]
        nm_fams = [g for g in pools[L] if not g["monomial"]]
        ni_are_nm = all(not g["monomial"]
                        for g, v in zip(pools[L], vel_all[L])
                        if v["non_integer"])
        vel_rows.append({"L": L, "velocity_cells": cells,
                         "non_integer_families": len(ni),
                         "non_integer_cells": sum(len(v["non_integer"])
                                                  for v in ni),
                         "monomial_with_a_non_integer_velocity": len(mono_ni),
                         "non_monomial_families": len(nm_fams),
                         "non_integer_families_are_non_monomial": ni_are_nm,
                         "non_integer_is_all_of_the_non_monomial":
                             len(ni) == len(nm_fams),
                         "all_integer": not ni, "witness": wit})
    S["velocity_census"] = vel_rows
    bad = [r["L"] for r in vel_rows
           if r["monomial_with_a_non_integer_velocity"]
           or not r["non_integer_families_are_non_monomial"]]
    LD.gate("G-MONOMIAL-VELOCITY-IS-AN-INTEGER",
            "the fifth break is not independent of the first four.  A "
            "monomial generator is a shift, and under the parent's own forced "
            "normalisation its velocity is the negated offset -- an integer "
            "at every rung.  Measured per family at every rung: NO monomial "
            "family anywhere carries a non-integer velocity, so every "
            "non-integer velocity sits on the non-monomial residue, which is "
            "exactly what the DDS criterion still permits",
            not bad, "monomial families with a non-integer velocity by rung "
            "%s; at L=6 the %d non-integer families are the %d non-monomial "
            "families: %s"
            % ({r["L"]: r["monomial_with_a_non_integer_velocity"]
                for r in vel_rows},
               [r["non_integer_families"] for r in vel_rows if r["L"] == 6][0],
               [r["non_monomial_families"] for r in vel_rows if r["L"] == 6][0],
               [r["non_integer_is_all_of_the_non_monomial"]
                for r in vel_rows if r["L"] == 6][0]))
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
                if mut("MUT-ALT") and L == 6 and nm == "S2-EDGE":
                    pred *= 2
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

    # THE JOIN IS AN IDENTITY OF SETS, FORCED BY THE TWO DEFINITIONS, and it
    # is measured as such: completeness is "the ball covers the torus", so the
    # locality-admitting widths are {1, ..., diam-1}; the interior radii are
    # the radius classes strictly between 0 and diam, i.e. the same set.  It
    # therefore holds at ODD sizes too -- the one result here that says
    # anything about odd rungs -- and the sweep runs over every band size.
    wc_rows = []
    for L in LADDER:
        loc = [w for w in win_rows if w["L"] == L and w["locality"]]
        ir = [r for r in rad_rows if r["L"] == L][0]
        n = len(loc)
        if mut("MUT-WIDTH") and L == 8:
            n -= 1
        wc_rows.append({"L": L, "locality_admitting_widths": n,
                        "widths": [w["r"] for w in loc],
                        "interior_radii": ir["interior_count"],
                        "width_set": [w["r"] for w in loc],
                        "interior_radius_set": ir["interior_radii"],
                        "sets_equal": [w["r"] for w in loc]
                                      == ir["interior_radii"],
                        "equal": n == ir["interior_count"]})
    S["width_count"] = wc_rows
    bad = [r["L"] for r in wc_rows if not (r["equal"] and r["sets_equal"])]
    LD.gate("G-WIDTH-COUNT-EQUALS-INTERIOR-RADII",
            "the number of window widths that admit locality equals the "
            "interior-radius count at every rung -- the parent's successor "
            "parameter and the ported locality criterion are the same number",
            not bad, "by rung: %s"
            % {r["L"]: (r["locality_admitting_widths"], r["interior_radii"])
               for r in wc_rows})

    join_rows = []
    for L in BAND_SIZES:
        diam = max(torus_absmax(v, L) for v in product(range(L), repeat=2))
        widths = []
        r = 1
        while True:
            row = locality_at_width(L, r)
            if row["locality"]:
                widths.append(r)
            if row["complete"]:
                break
            r += 1
        radii = sorted({torus_absmax(v, L)
                        for v in product(range(L), repeat=2)})
        interior = [x for x in radii if 0 < x < diam]
        expect = list(range(1, diam))
        join_rows.append({"L": L, "diameter": diam, "widths": widths,
                          "interior_radii": interior,
                          "both_are_1_to_diam_minus_1":
                              widths == interior == expect,
                          "odd": L % 2 == 1})
    if mut("MUT-JOIN"):
        r0 = dict(join_rows[3])
        r0["widths"] = r0["widths"][:-1] or [0]
        r0["both_are_1_to_diam_minus_1"] = (
            r0["widths"] == r0["interior_radii"]
            == list(range(1, r0["diameter"])))
        join_rows[3] = r0
    S["width_radius_join"] = {
        "rows": join_rows,
        "status": "FORCED-BY-THE-TWO-DEFINITIONS",
        "identity": "both sets are {1, ..., diam-1}: completeness is 'the "
                    "radius-r ball covers the torus', so locality survives "
                    "exactly while r < diam; and the interior radii are the "
                    "radius classes strictly between 0 and diam.  This is an "
                    "identity of SETS for any connective and any L, odd or "
                    "even -- not a cross-instrument coincidence at three "
                    "rungs",
        "odd_sizes_covered": sum(1 for r in join_rows if r["odd"])}
    bad = [r["L"] for r in join_rows if not r["both_are_1_to_diam_minus_1"]]
    LD.gate("G-WIDTH-RADIUS-JOIN-IS-AN-IDENTITY",
            "the join is an identity of SETS forced by the two definitions, "
            "not a coincidence of counts at three rungs: at every size of the "
            "whole band sweep -- ODD sizes included, where nothing else here "
            "speaks -- the locality-admitting widths and the interior radii "
            "are the same set, and both are {1, ..., diam-1}",
            not bad, "%d sizes (%d of them odd), %d disagreeing: %s"
            % (len(join_rows), S["width_radius_join"]["odd_sizes_covered"],
               len(bad), bad or "none"))

    part_rows = []
    for L in LADDER:
        for b in range(2, L):
            if L % b:
                continue
            cells, cross = blockwise_components(L, b)
            if mut("MUT-PARTITION") and L == 8 and b == 2:
                cells = [dict(c) for c in cells]
                cells[0]["drawn"] = cells[0]["drawn"] - 1
                cells[0]["complete"] = False
            ok = all(c["drawn"] == c["possible"] for c in cells)
            part_rows.append({"L": L, "block": b, "cells": len(cells),
                              "pairs_drawn": sum(c["drawn"] for c in cells),
                              "pairs_possible": sum(c["possible"]
                                                    for c in cells),
                              "cross_cell_adjacencies": cross,
                              "clique_only": ok and cross == 0,
                              "locality": not (ok and cross == 0)})
    S["partition_control"] = part_rows
    bad = [(r["L"], r["block"]) for r in part_rows if not r["clique_only"]]
    LD.gate("G-PARTITION-COROLLARY",
            "R2's partition corollary transports, and the adjacency is "
            "EVALUATED rather than asserted: at every rung and every divisor "
            "block size, every pair inside a cell is found adjacent by the "
            "same-chart test and no pair across two cells is, so every "
            "component is a clique and locality here is carried by the "
            "SLIDING window and by nothing else",
            not bad, "%d blockwise atlases, %d pairs drawn of %d possible, "
            "%d cross-cell adjacencies, %d producing a non-complete component"
            % (len(part_rows), sum(r["pairs_drawn"] for r in part_rows),
               sum(r["pairs_possible"] for r in part_rows),
               sum(r["cross_cell_adjacencies"] for r in part_rows), len(bad)))

    # ---- the support-size ceiling: what makes the absence half finite ----
    ceil = support_ceiling(A)
    if mut("MUT-CEILING"):
        ceil = dict(ceil)
        ceil["ceiling"] = ceil["ceiling"] + 1
    S["support_ceiling"] = ceil
    LD.gate("G-SUPPORT-CEILING",
            "the largest support a unitary map can have over the declared "
            "alphabet is COMPUTED from the alphabet itself: the squared "
            "moduli are enumerated, every multiset of them summing to one is "
            "found, and the ceiling is the largest such multiset -- which is "
            "what turns the band's absence half into a finite census",
            ceil["ceiling"] == SUPPORT_CEILING,
            "squared moduli %s; profiles %s; ceiling %d against the declared "
            "%d" % (ceil["squared_moduli"], ceil["profiles"], ceil["ceiling"],
                    SUPPORT_CEILING))

    # ---- the injectivity theorem, evaluated over the whole sweep ---------
    inj_rows = []
    for r in WIDTHS:
        for L in BAND_SIZES:
            row = injective_lift(L, r)
            row["predicted"] = L >= 4 * r + 1
            row["agrees"] = row["injective"] == row["predicted"]
            inj_rows.append(row)
    if mut("MUT-INJECTIVITY"):
        k = [i for i, r in enumerate(inj_rows) if r["injective"]][0]
        r0 = dict(inj_rows[k])
        r0["collisions"] = r0["collisions"] + 1
        r0["injective"] = r0["collisions"] == 0
        r0["agrees"] = r0["injective"] == r0["predicted"]
        inj_rows[k] = r0
    S["injectivity_theorem"] = {
        "statement": "lift the radius-r ball to {-r..r}^2 in Z^2; two lifted "
                     "differences lie in {-2r..2r}^2 and are congruent mod L "
                     "only if they differ by L.e with |L.e_i| <= 4r, so e = 0 "
                     "whenever L >= 4r+1, the ball's differences are all "
                     "simple, and the ball is DDS-FREE at every width",
        "rows": inj_rows,
        "threshold_by_width": {str(r): 4 * r + 1 for r in WIDTHS}}
    bad = [(r["L"], r["r"]) for r in inj_rows if not r["agrees"]]
    LD.gate("G-BAND-INJECTIVITY",
            "the injectivity theorem's hypothesis is EVALUATED over the whole "
            "lifted difference box at every declared width and size, and the "
            "measured injectivity agrees with the theorem's threshold "
            "L >= 4r+1 at every one of them",
            not bad, "%d (width, size) boxes, %d disagreeing with 4r+1: %s"
            % (len(inj_rows), len(bad), bad or "none"))

    # ---- the census: the band DECIDED, both halves -----------------------
    band_rows = []
    for r in WIDTHS:
        adm, pair_adm = [], []
        for L in BAND_SIZES:
            loc = locality_at_width(L, r)["locality"]
            cen = band_census(L, r, A)
            pw = band_witness(L, r)
            ok = loc and cen["carries_a_non_monomial"]
            if mut("MUT-BAND") and r == 1 and L == PARENT_RUNG:
                ok = False
            if ok:
                adm.append(L)
            if loc and pw is not None and not (mut("MUT-BAND-PAIR")
                                               and r == 3 and L == 10):
                pair_adm.append(L)
            exh = cen["exhaustive"]
            if mut("MUT-BAND-ABSENCE") and r == 2 and L == 9:
                exh = False
            pairw = pw is not None
            if mut("MUT-L7-SECTION") and r == L7_WIDTH and L == L7_RUNG:
                pairw = True
            band_rows.append({
                "r": r, "L": L, "locality": loc,
                "ball": cen["ball"], "dds_subsets": cen["dds_subsets"],
                "maps_tested": cen["maps_tested"],
                "carries_a_non_monomial": cen["carries_a_non_monomial"],
                "absence_is_exhaustive": exh,
                "lift_is_injective": cen["injectivity"]["injective"],
                "witness": cen["witness"],
                "involution_pair_witness": pairw,
                "admitted": ok})
        pair_pred = [L for L in BAND_SIZES
                     if L % 2 == 0 and 2 * r + 2 <= L <= 4 * r]
        band_rows.append({"r": r, "L": None, "admitted_set": adm,
                          "involution_pair_set": pair_adm,
                          "involution_pair_closed_form": pair_pred,
                          "pair_law_holds": pair_adm == pair_pred,
                          "beyond_the_pair_mechanism":
                              [L for L in adm if L not in pair_adm]})
    S["band_law"] = {
        "rows": [b for b in band_rows if b.get("L") is not None],
        "by_width": [b for b in band_rows if b.get("L") is None],
        "law": "at window width r the admitted sizes are exactly the L with "
               "L >= 2r+2 (locality) whose radius-r ball carries a "
               "difference-doubled subset REALISED over the declared "
               "alphabet.  Two mechanisms occur in the declared sweep: the "
               "involution-separated pair (even L <= 4r) and the perfect "
               "difference set (L = 7 at r = 2).  EVENNESS IS NOT A LAW.",
        "absence_is_forced":
            "below 2r+2 by locality; above 4r by the injectivity theorem "
            "(G-BAND-INJECTIVITY); in between by an EXHAUSTIVE census over "
            "the ball's difference-doubled subsets of size at most the "
            "computed support ceiling (G-SUPPORT-CEILING).  Nothing in the "
            "declared sweep is open.",
        "alphabet_relativity":
            "admission is a joint property of the ball and the ALPHABET: a "
            "difference-doubled subset is a permission, and what converts a "
            "permission into a realisation is the alphabet.  The order-3 "
            "coset in the radius-3 ball at L = 9 is the measured witness "
            "(G-ODD-COSET-ALPHABET-RELATIVE)",
        "parent_row": [b for b in band_rows
                       if b.get("L") is None and b["r"] == 1][0]["admitted_set"],
        "sections": {str(b["r"]): b["admitted_set"] for b in band_rows
                     if b.get("L") is None}}
    bad = [b["r"] for b in band_rows
           if b.get("L") is None and not b["pair_law_holds"]]
    LD.gate("G-BAND-PAIR-MECHANISM",
            "the involution-separated pair is ONE mechanism and its own "
            "section is exactly the even sizes between 2r+2 and 4r -- a true "
            "combinatorial identity about that construction, and NOT the "
            "admitted set",
            not bad, "involution-pair sections by width %s against the closed "
            "form %s"
            % ({b["r"]: b["involution_pair_set"] for b in band_rows
                if b.get("L") is None},
               {b["r"]: b["involution_pair_closed_form"] for b in band_rows
                if b.get("L") is None}))
    sect = {b["r"]: b["admitted_set"] for b in band_rows if b.get("L") is None}
    LD.gate("G-BAND-LAW",
            "the parent's admitted-scale set is re-derived at its own window "
            "width and then at wider ones by a census that DECIDES admission "
            "rather than exhibiting one construction: every admitted size "
            "carries a witness verified unitary by the whole-torus criterion, "
            "and every excluded size is excluded by a theorem or an "
            "exhausted census",
            (sect[1] == pv("PV-ADMISSIBLE")
             and all(len(v) > 0 for v in sect.values())
             and all(all(L >= 2 * r + 2 for L in v) for r, v in sect.items())),
            "admitted sets by width %s; the width-1 row reproduces the "
            "anchored %s" % (sect, pv("PV-ADMISSIBLE")))

    unforced = [(b["L"], b["r"]) for b in band_rows
                if b.get("L") is not None and not b["admitted"]
                and not (not b["locality"] or b["absence_is_exhaustive"])]
    LD.gate("G-BAND-ABSENCE-FORCED",
            "EVERY non-admitted cell of the sweep is forced and not merely "
            "unwitnessed: either locality fails by the threshold theorem, or "
            "the census over the ball's difference-doubled subsets up to the "
            "computed support ceiling ran to exhaustion and found nothing.  "
            "The band is two-sided at every declared width",
            not unforced, "%d cells, %d not forced: %s"
            % (len([b for b in band_rows if b.get("L") is not None]),
               len(unforced), unforced or "none"))
    # ---- the (7,4,2) witness: the species the pair search cannot see -----
    l7 = {v: cscal(ONE, s, 2) for v, s in zip(L7_SUPPORT, L7_SIGNS)}
    if mut("MUT-L7-WITNESS"):
        l7[L7_SUPPORT[2]] = cscal(ONE, 1, 2)
    l7_mat = matrix_unitary(l7, L7_RUNG)
    l7_row = {
        "L": L7_RUNG, "width": L7_WIDTH,
        "support": [list(v) for v in L7_SUPPORT],
        "coefficients": [cstr(l7[v]) for v in L7_SUPPORT],
        "in_the_declared_alphabet": all(c in A for c in l7.values()),
        "radii": [torus_absmax(v, L7_RUNG) for v in L7_SUPPORT],
        "inside_the_ball": all(torus_absmax(v, L7_RUNG) <= L7_WIDTH
                               for v in L7_SUPPORT),
        "difference_multiplicities":
            sorted(diff_multiset(list(L7_SUPPORT), L7_RUNG).values(),
                   reverse=True),
        "sidon": is_sidon(list(L7_SUPPORT), L7_RUNG)[0],
        "autocorrelation_is_a_delta": autocorr_is_delta(l7, L7_RUNG),
        "matrix_entries_checked": l7_mat["entries"],
        "matrix_mismatches": l7_mat["mismatches"],
        "matrix_dimension": l7_mat["dimension"],
        "locality": locality_at_width(L7_RUNG, L7_WIDTH)["locality"],
        "involutions_in_the_group":
            sum(1 for v in product(range(L7_RUNG), repeat=2)
                if any(v) and (2 * v[0]) % L7_RUNG == 0
                and (2 * v[1]) % L7_RUNG == 0),
        "note": "a (7,4,2) perfect difference set -- every nonzero difference "
                "realised exactly twice -- carrying a non-monomial unitary "
                "inside the radius-2 ball over the parents' own alphabet.  "
                "The involution-pair search is structurally blind to it: "
                "Z_7^2 has no involution at all."}
    S["l7_witness"] = l7_row
    LD.gate("G-L7-DIFFERENCE-SET-WITNESS",
            "the odd size the delivered band excluded carries an explicit "
            "in-alphabet non-monomial unitary inside the radius-2 ball, "
            "verified TWICE -- the periodic autocorrelation is a delta, and "
            "the full L^2 x L^2 matrix satisfies U^dag U = I entry by entry "
            "-- in a group that contains no involution, so no pair mechanism "
            "can account for it",
            (l7_row["in_the_declared_alphabet"] and l7_row["inside_the_ball"]
             and l7_row["locality"]
             and l7_row["autocorrelation_is_a_delta"]
             and l7_row["matrix_mismatches"] == 0
             and l7_row["involutions_in_the_group"] == 0
             and set(l7_row["difference_multiplicities"]) == {2}),
            "L=%d support %s, radii %s, multiplicities %s, %d matrix entries "
            "checked with %d mismatches, %d involutions in the group"
            % (L7_RUNG, l7_row["support"], l7_row["radii"],
               l7_row["difference_multiplicities"],
               l7_row["matrix_entries_checked"], l7_row["matrix_mismatches"],
               l7_row["involutions_in_the_group"]))
    in_census = [b for b in band_rows
                 if b.get("L") == L7_RUNG and b["r"] == L7_WIDTH][0]
    LD.gate("G-L7-IN-THE-SECTION",
            "the census reaches the same cell independently: L = 7 is in the "
            "width-2 section, its witness is a difference-doubled subset of "
            "the ball, and no involution pair exists there",
            (in_census["admitted"] and in_census["carries_a_non_monomial"]
             and not in_census["involution_pair_witness"]),
            "L=7 at r=2: admitted %s, census witness %s, involution pair %s"
            % (in_census["admitted"],
               in_census["witness"] and in_census["witness"]["support"],
               in_census["involution_pair_witness"]))

    # ---- the alphabet-relativity of the SCALE clause, MEASURED ------------
    coset_rows = []
    for an, AA in PROBE_ALPHABETS:
        sc = scan_offsets(tuple(ODD_COSET), AA, ODD_COSET_RUNG)
        if mut("MUT-ODD-COSET") and an == "THIRDS-19":
            sc = dict(sc)
            sc["non_monomial"] = 0
        coset_rows.append({"alphabet": an, "alphabet_size": len(AA),
                           "maps": sc["maps"], "unitary": sc["unitary"],
                           "non_monomial": sc["non_monomial"]})
    S["odd_coset"] = {
        "L": ODD_COSET_RUNG, "width": ODD_COSET_WIDTH,
        "support": [list(v) for v in ODD_COSET],
        "radii": [torus_absmax(v, ODD_COSET_RUNG) for v in ODD_COSET],
        "inside_the_ball": all(torus_absmax(v, ODD_COSET_RUNG)
                               <= ODD_COSET_WIDTH for v in ODD_COSET),
        "locality": locality_at_width(ODD_COSET_RUNG,
                                      ODD_COSET_WIDTH)["locality"],
        "difference_multiplicities":
            sorted(diff_multiset(list(ODD_COSET), ODD_COSET_RUNG).values(),
                   reverse=True),
        "rows": coset_rows,
        "reading": "the same difference-doubled subset in the same ball at "
                   "the same size carries no non-monomial unitary over the "
                   "parents' 25 and over the 7-value probe, and the control's "
                   "own count over the 19-value probe.  The SCALE clause is "
                   "ALPHABET-RELATIVE, exactly as the CONTROL clause is."}
    thirds = [r for r in coset_rows if r["alphabet"] == "THIRDS-19"][0]
    parents = [r for r in coset_rows if r["alphabet"] == "R4-25"][0]
    LD.gate("G-ODD-COSET-ALPHABET-RELATIVE",
            "the band's admitted set is a joint property of the ball and the "
            "alphabet, and the witness is measured rather than asserted: the "
            "order-3 coset inside the radius-3 ball at L = 9 is "
            "difference-doubled, locality holds there, and it carries "
            "non-monomial unitaries over the control's probe alphabet and "
            "none over the parents' own",
            (S["odd_coset"]["inside_the_ball"] and S["odd_coset"]["locality"]
             and parents["non_monomial"] == 0
             and thirds["non_monomial"] == registered["non_monomial"]),
            "L=9 r=3 coset %s: %d non-monomial over the parents' %d-element "
            "alphabet, %d over the %d-value probe (the control's own count)"
            % (S["odd_coset"]["support"], parents["non_monomial"],
               parents["alphabet_size"], thirds["non_monomial"],
               thirds["alphabet_size"]))

    # ---- the two DDS routes, bound against each other --------------------
    route_bad, route_checked = [], 0
    for r in arenas:
        St = [tuple(v) for v in r["offsets"]]
        naive = {tuple(sorted(T)) for T in doubled_subsets(St, r["L"])}
        fast = {tuple(sorted(T)) for T in
                dds_subsets_bounded(St, r["L"], len(St))}
        if mut("MUT-DDS-ROUTES") and r["L"] == PARENT_RUNG and naive:
            naive = set(sorted(naive)[1:])
        route_checked += 1
        if naive != fast:
            route_bad.append((r["L"], r["arena"]))
    for L in BAND_SIZES:
        B = ball(L, 1)
        naive = {tuple(sorted(T)) for T in doubled_subsets(B, L)}
        fast = {tuple(sorted(T)) for T in dds_subsets_bounded(B, L, len(B))}
        route_checked += 1
        if naive != fast:
            route_bad.append((L, "BALL-r1"))
    LD.gate("G-DDS-CRITERION-AGREES",
            "the fast difference-doubled census used on the balls and the "
            "naive one used on the arenas are bound against each other, SET "
            "for SET, on every declared arena and on every radius-one ball of "
            "the sweep -- the reduction that makes a 49-offset ball finite is "
            "not taken on trust",
            not route_bad, "%d objects, %d disagreeing: %s"
            % (route_checked, len(route_bad), route_bad or "none"))

    # ---- G-DDS-WINDOW: the hard stop, exercised ---------------------------
    widest = max(len(r["offsets"]) for r in arenas)
    if mut("MUT-DDS-WINDOW"):
        widest = DDS_SUBSET_WINDOW + 1
    S["dds_window"] = {
        "window": DDS_SUBSET_WINDOW,
        "largest_arena": widest,
        "ball_census_ceiling": SUPPORT_CEILING,
        "why": "the naive subset census is exhaustive at |S| <= %d, which "
               "covers every declared arena (largest %d) and every "
               "radius-one ball; the BALL census at wider windows is run by "
               "the bounded route up to the COMPUTED support ceiling %d, "
               "which is exhaustive for unitarity by G-SUPPORT-CEILING"
               % (DDS_SUBSET_WINDOW,
                  max(len(r["offsets"]) for r in arenas), SUPPORT_CEILING)}
    LD.gate("G-DDS-WINDOW",
            "the declared subset window is a real hard stop and it covers "
            "what this unit asks of it: every arena the naive census runs on "
            "is within the window, and nothing outside it is decided by that "
            "route",
            S["dds_window"]["largest_arena"] <= DDS_SUBSET_WINDOW,
            "window %d, largest arena %d, ball ceiling %d"
            % (DDS_SUBSET_WINDOW, S["dds_window"]["largest_arena"],
               SUPPORT_CEILING))

    # =================================================================
    # STAGE 5.  THE PERSISTENCE TABLE
    # =================================================================
    # m6: a PERSISTS row that is FORCED is a theorem restated at three rungs,
    # not a survival.  Each row carries its status and, when forced, the
    # theorem that forces it; G-PERSISTENCE-FORCING-DECLARED binds the split.
    FORCED_ROWS = {
        "the LINK stencil is Sidon":
            "the anchored link set is Sidon at every L >= 3 -- one line from "
            "its six differences",
        "monomial-only on the LINK stencil":
            "Sidon implies DDS-free implies monomial-only, over any field "
            "with an involution (section 3.1)",
        "the local AXIS stencil is Sidon":
            "the 3-term stencil {0, a, -a} realises +-a twice at every order "
            ">= 3, so it is non-Sidon at every rung of the ladder",
        "VMAX equals the max-norm diameter":
            "the momentum parent's even-L theorem, quoted at VB-VMAX",
        "the coin family and its sector split":
            "the coin is a 2x2 unitary over the coefficient alphabet and its "
            "definition mentions no L (G-COIN-ALPHABET-DERIVED)",
        "the (order, support) profile":
            "no declared local stencil wraps at any rung (G-NON-WRAPPING), "
            "so the generators are the same maps on the same relative "
            "coordinates -- the gauge parent's own argument",
        "the holonomy is alternating on each of its orbits":
            "the same non-wrapping argument: the local groups are literally "
            "the same groups at the three rungs",
    }

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
                "verdict": v, "law": law,
                "status": ("FORCED" if name in FORCED_ROWS else
                           "MEASURED-AT-THE-DECLARED-RUNGS"),
                "forcing": FORCED_ROWS.get(name, "")}

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
    T.append(cellrow("the local AXIS stencil carries a difference-doubled "
                     "subset",
                     {L: not [r["dds_free"] for r in arenas
                              if r["L"] == L
                              and r["arena"].startswith("AXIS")][0]
                      for L in LADDER}, "BREAKS-AT-L=6",
                     "the permission the parent rung had is withdrawn at "
                     "L = 6 and stays withdrawn: the criterion turns on"))
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
                     "band that widens with the window; every exclusion in "
                     "this row is FORCED -- by locality at L=4 for r>=2 and "
                     "at L=6 for r=3, and by the exhausted ball census at "
                     "L=6 and L=8 for r=1"))

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

    persists = [r for r in T if r["verdict"] == "PERSISTS"]
    forced = [r for r in persists if r["status"] == "FORCED"]
    contingent = [r for r in persists if r["status"] != "FORCED"]
    unlabelled = [r["invariant"] for r in T
                  if r["status"] == "FORCED" and not r["forcing"]]
    stray = [r["invariant"] for r in T
             if r["status"] == "FORCED" and r["verdict"] != "PERSISTS"]
    if mut("MUT-FORCING"):
        brk = [r for r in T if r["verdict"].startswith("BREAKS")][0]
        brk["status"] = "FORCED"
        unlabelled = [r["invariant"] for r in T
                      if r["status"] == "FORCED" and not r["forcing"]]
        stray = [r["invariant"] for r in T
                 if r["status"] == "FORCED" and r["verdict"] != "PERSISTS"]
    S["persistence_forcing"] = {
        "persist_rows": len(persists),
        "forced": len(forced), "contingent": len(contingent),
        "forced_rows": [r["invariant"] for r in forced],
        "contingent_rows": [r["invariant"] for r in contingent],
        "note": "a FORCED row is a theorem restated at three rungs, not a "
                "survival.  The licensed reading of the PERSISTS count is "
                "%d contingent survivals and %d theorems"
                % (len(contingent), len(forced))}
    LD.gate("G-PERSISTENCE-FORCING-DECLARED",
            "the PERSISTS count is split at its own modality: every row "
            "labelled FORCED names the theorem that forces it, no forced "
            "label sits on a row that is not a survival, and the honest "
            "reading -- so many contingent survivals and so many theorems "
            "restated -- is published beside the count",
            not unlabelled and not stray and len(forced) + len(contingent)
            == len(persists),
            "%d PERSISTS rows: %d forced, %d contingent; unlabelled %s, "
            "stray %s" % (len(persists), len(forced), len(contingent),
                          unlabelled or "none", stray or "none"))

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
        "control_rung": CONTROL_RUNG,
        "rungs_declared": list(LADDER),
        "arenas_sidon_substantive": S["sidon_prediction"]
                                     ["sufficiency_substantive"],
        "arenas_sidon_vacuous": S["sidon_prediction"]["sufficiency_vacuous"],
        "band_widths": len(WIDTHS),
        "band_sweep_low": min(BAND_SIZES), "band_sweep_high": max(BAND_SIZES),
        "support_ceiling": ceil["ceiling"],
        "band_dds_subsets": sum(b["dds_subsets"] for b in band_rows
                                if b.get("L") is not None),
        "band_maps_tested": sum(b["maps_tested"] for b in band_rows
                                if b.get("L") is not None),
        "char_p_fields": len(CHAR_P_FIELDS),
        "char_p_scans": len(cp_rows),
        "char_p_dds_free_rows": sum(1 for r in cp_rows if r["dds_free"]),
        "char_p_outside_window": len(cp_skipped),
        "join_sizes": len(join_rows),
        "join_odd_sizes": sum(1 for r in join_rows if r["odd"]),
        "l7_matrix_entries": l7_row["matrix_entries_checked"],
        "l7_matrix_dimension": l7_row["matrix_dimension"],
        "persists_forced": len(forced),
        "persists_contingent": len(contingent),
        "coins_antidiagonal": secs.get("ANTIDIAGONAL", 0),
        "global_L4": [r["support"] for r in glob_rows if r["L"] == 4][0],
        "global_L6": [r["support"] for r in glob_rows if r["L"] == 6][0],
        "global_L8": [r["support"] for r in glob_rows if r["L"] == 8][0],
        "eigenphase_L4": [r["eigenphase_lattice"] for r in disp_rows
                          if r["L"] == 4][0],
        "eigenphase_L6": [r["eigenphase_lattice"] for r in disp_rows
                          if r["L"] == 6][0],
        "eigenphase_L8": [r["eigenphase_lattice"] for r in disp_rows
                          if r["L"] == 8][0],
        "non_integer_families_L6": [r["non_integer_families"]
                                    for r in vel_rows if r["L"] == 6][0],
        "gauge_group_order": pool_rows[0]["orbit_sizes"][0],
        "sources": len(SOURCES),
        "path_value_anchors": len(PATH_VALUE_ANCHORS),
        "verbatim_anchors": len(VERBATIM_ANCHORS),
        "mutants": len(MUTANTS),
        "L": pv("PV-L"), "d": pv("PV-D"), "alphabet": pv("PV-ALPHABET"),
        "connective_tag": pv("PV-CONNECTIVE"),
        "forcing_link": pv("PV-FORCING-LINK"),
        "field": "Q(ZETA-24)",
    }

    # =================================================================
    # THE SUCCESSOR REGISTER (ruling 1 and ruling 2 of the adjudication)
    # =================================================================
    # A half-right prediction is recorded as its PARTS, never as a fraction.
    link_all = [r for r in arenas if r["arena"] == "LINK"]
    link_sidon_everywhere = all(r["sidon"] for r in link_all)
    link_clean = all(r["non_monomial"] == 0 for r in link_all)
    dl = S["dds_law"]
    conv_rows = [r for r in arenas if not r["dds_free"]]
    S["successor_register"] = {
        "the_registered_prediction": {
            "quoted_at": "VB-SIDON",
            "recorded_as": "THREE PARTS, not a fraction",
            "parts": [
                {"part": "g1 MECHANISM",
                 "claim": "the monomial theorem is a Sidon property of the "
                          "offset set (sufficiency direction)",
                 "status": "CONFIRMED AND STRENGTHENED",
                 "measured": "holds at %d of %d declared arenas, "
                             "substantively at the %d Sidon ones; and it is "
                             "now a theorem with a weaker hypothesis, since "
                             "DDS-free is strictly weaker than Sidon (%d "
                             "arenas are DDS-free and not Sidon)"
                             % (len(pred_rows), len(pred_rows),
                                sp["sufficiency_substantive"],
                                dl["sidon_but_not_the_only_forced"])},
                {"part": "g2 TRANSPORT TO THE R = 4 ARENA",
                 "claim": "the theorem transports verbatim to R = 4",
                 "status": "CLOSED BY THEOREM, NOT BY MEASUREMENT",
                 "measured": "the anchored link set is Sidon at every rung "
                             "measured here (%s), hence DDS-free, hence "
                             "monomial-only over ANY field with an "
                             "involution.  The register's named target needs "
                             "no scan and no R-ladder run; PER-R inherits it "
                             "as a corollary and must not spend a census on "
                             "it.  This unit did NOT enter the R-ladder"
                             % link_sidon_everywhere},
                {"part": "g3 CONTROL",
                 "claim": "dies at ANY declared fourth direction (54 "
                          "non-monomial unitaries appear)",
                 "status": "REFUTED AS STATED",
                 "measured": "the %d is reproduced exactly with the same "
                             "witness support at the control rung L = %d, "
                             "and it is ALPHABET-RELATIVE (%d over the "
                             "parents' 25, %d over the 7-value probe); the "
                             "death does not transport up the L-ladder, and "
                             "there BY THEOREM -- the L = 6 and L = 8 "
                             "LINK-PLUS-4TH sets are DDS-free, so 0 holds "
                             "over any field"
                             % (registered["non_monomial"], CONTROL_RUNG,
                                [c for c in ctrl
                                 if c["arena"] == "LINK-PLUS-4TH"
                                 and c["alphabet"] == "R4-25"][0]
                                ["non_monomial"],
                                [c for c in ctrl
                                 if c["arena"] == "LINK-PLUS-4TH"
                                 and c["alphabet"] == "UNIT-7"][0]
                                ["non_monomial"])},
            ],
            "score": "one confirmed, one closed by theorem, one refuted as "
                     "stated.  Not a fraction",
            "governance_note":
                "the universal quantifier ('any declared fourth direction') "
                "entered at the COMPRESSION from the seat finding to the "
                "register, not at the measurement: the seat finding named "
                "the specific fourth direction, the specific probe alphabet "
                "and the mechanism.  That is a governance datum, and the "
                "record of what was registered is not edited"},
        "this_units_result_column": {
            "theorem": "DDS-FREE IMPLIES MONOMIAL-ONLY is a THEOREM, "
                       "registered as a RESULT and not as a bet: it has a "
                       "proof, it is field-free (exercised in %d "
                       "characteristics at G-CHAR-P-FIELD-FREE), and no "
                       "measurement can falsify it" % len(CHAR_P_FIELDS)},
        "the_new_prediction": {
            "prediction": "DDS-CARRYING IMPLIES INTERFERENCE PRESENT (the "
                          "CONVERSE of the theorem)",
            "strength": "NECESSARY-NOT-SUFFICIENT",
            "measured_here": "%d of %d DDS-carrying arenas on the declared "
                             "list carry a non-monomial unitary"
                             % (dl["arenas_dds_carrying_with_a_non_monomial"],
                                dl["arenas_dds_carrying"]),
            "already_falsified_alphabet_relatively":
                "the order-3 coset in the radius-3 ball at L = %d is "
                "DDS-carrying and carries %d non-monomial unitaries over the "
                "parents' 25 and %d over the 7-value probe, against %d over "
                "the 19-value probe (S['odd_coset'])"
                % (ODD_COSET_RUNG,
                   [r for r in coset_rows if r["alphabet"] == "R4-25"][0]
                   ["non_monomial"],
                   [r for r in coset_rows if r["alphabet"] == "UNIT-7"][0]
                   ["non_monomial"],
                   [r for r in coset_rows if r["alphabet"] == "THIRDS-19"][0]
                   ["non_monomial"]),
            "falsification_condition_stated_forward":
                "a difference-doubled offset set whose non-monomial unitaries "
                "are empty over EVERY alphabet closed under the declared "
                "field's involution would refute it structurally.  A "
                "difference-doubled set is a PERMISSION; what converts a "
                "permission into a realisation is the alphabet"},
        "per_r_inherits": [
            "g2 above: the R-ladder's link register is forced at every R >= 3 "
            "by theorem, so PER-R must not spend a scan on it and must ask "
            "instead what its OWN offset set is",
            "the alphabet-relativity discipline: every count of non-monomial "
            "unitaries in this corpus is a joint property of the offset set "
            "and the alphabet, and the R-ladder's alphabet is not the "
            "parents' 25",
            "the coset mechanism as the R-ladder's live danger: paper-20's "
            "arena is over F_3, so cosets of order-3 subgroups are cheap "
            "there and the criterion will bite",
            "NOT inherited: the L-ladder's window band, VMAX = L/2, the "
            "eigenphase law Z/lcm(%d, L) and the interior-radius count -- all "
            "four are statements about (Z_L)^2 with this alphabet and none "
            "has been asked of the R-ladder"
            % pool_rows[0]["orbit_sizes"][0]],
        "the_odd_rung_gap":
            "correctly declared open for the ladder, with two exceptions "
            "measured here: the width/interior-radius identity holds at odd "
            "sizes by theorem (G-WIDTH-RADIUS-JOIN-IS-AN-IDENTITY), and the "
            "band's width-2 section CONTAINS the odd size %d "
            "(G-L7-DIFFERENCE-SET-WITNESS).  The odd-L blade, when it runs, "
            "starts there" % L7_RUNG,
    }
    if mut("MUT-SUCCESSOR"):
        S["successor_register"]["the_registered_prediction"]["parts"] = \
            S["successor_register"]["the_registered_prediction"]["parts"][:-1]
    sr = S["successor_register"]
    LD.gate("G-SUCCESSOR-REGISTER-WRITTEN",
            "the unit built to test a predecessor's successor register "
            "carries one of its own: the registered prediction is recorded as "
            "its three PARTS with each part's status measured, the theorem is "
            "filed as a RESULT rather than a bet, and the falsifiable "
            "successor is the CONVERSE with its falsification condition "
            "stated forward and its first counterexample already measured",
            (len(sr["the_registered_prediction"]["parts"]) == 3
             and {p["status"] for p in sr["the_registered_prediction"]["parts"]}
             == {"CONFIRMED AND STRENGTHENED",
                 "CLOSED BY THEOREM, NOT BY MEASUREMENT",
                 "REFUTED AS STATED"}
             and link_sidon_everywhere and link_clean
             and sr["the_new_prediction"]["strength"]
             == "NECESSARY-NOT-SUFFICIENT"
             and dl["arenas_dds_carrying_with_a_non_monomial"]
             == dl["arenas_dds_carrying"]),
            "three parts recorded; the link set Sidon at every rung: %s, "
            "monomial-only: %s; the converse holds %d of %d here and is "
            "falsified alphabet-relatively at L = %d"
            % (link_sidon_everywhere, link_clean,
               dl["arenas_dds_carrying_with_a_non_monomial"],
               dl["arenas_dds_carrying"], ODD_COSET_RUNG))

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
         "fibre": "UNBOUNDED", "instances": len(WIDTHS),
         "why": "the band is the contested row, so its free coordinate is "
                "priced here: widths 1, 2 and 3 are run because width 1 is "
                "the parent's own and the two above it are the smallest that "
                "still admit locality on this ladder.  Nothing above width 3 "
                "is measured, and the SCALE clause is scoped to the widths "
                "run"},
        {"choice": "the band sweep range", "class": "GENUINELY-FREE",
         "fibre": "UNBOUNDED", "instances": len(BAND_SIZES),
         "why": "sizes %d to %d, chosen to contain every size the closed "
                "forms of both mechanisms can reach at the declared widths "
                "(4r <= 12) with two sizes of margin.  Above the sweep the "
                "injectivity theorem forces absence at every width, so the "
                "range is a presentation choice and not a scope limit"
                % (min(BAND_SIZES), max(BAND_SIZES))},
        {"choice": "the plaquette stencils", "class": "FORCED (anchored)",
         "fibre": 1, "instances": len(PLAQ_STENCILS),
         "why": "the parent's own six, carried verbatim"},
        {"choice": "the DDS subset window", "class": "DECLARED-WINDOW",
         "fibre": 1, "instances": 1,
         "why": "the NAIVE subset census (all 2^|S| subsets) is exhaustive at "
                "|S| <= %d and runs on the declared arenas and the "
                "radius-one balls, which is everything it is asked for.  The "
                "BALL census at wider windows runs by the bounded route up "
                "to the COMPUTED support ceiling %d, which is exhaustive for "
                "unitarity by G-SUPPORT-CEILING, and the two routes are bound "
                "against each other at G-DDS-CRITERION-AGREES.  No absence "
                "claim rests on the window"
                % (DDS_SUBSET_WINDOW, SUPPORT_CEILING)},
        {"choice": "the char-p scan window", "class": "DECLARED-WINDOW",
         "fibre": 1, "instances": 1,
         "why": "the nine-characteristic exercise runs every (field, arena) "
                "pair with |F|^|S| <= %d exhaustively -- %d scans -- and the "
                "%d pairs above it are listed rather than run.  The theorem "
                "is proved, not established by this exercise; the exercise "
                "is what stops the proof from being read in one "
                "characteristic only"
                % (CHAR_P_SCAN_WINDOW, len(cp_rows), len(cp_skipped))},
    ]
    live = {"the axis set at each rung": sum(r["axes"] for r in ax_rows),
            "the rungs of the ladder": len(LADDER),
            "the probe alphabets at the control rung": len(ctrl) // 2,
            "the window widths": len({b["r"] for b in band_rows}),
            "the band sweep range": len({b["L"] for b in band_rows
                                         if b.get("L") is not None}),
            "the plaquette stencils": len({r["stencil"]
                                           for r in prof_rows}),
            "the char-p scan window": 1}
    ci_bad = [c["choice"] for c in S["choice_inventory"]
              if "class" not in c or "fibre" not in c
              or (c["class"] in ("GENUINELY-FREE", "DECLARED-WINDOW")
                  and not c.get("why"))
              or (c["choice"] in live and c["instances"] != "all"
                  and c["instances"] != live[c["choice"]])]
    if mut("MUT-CHOICES"):
        S["choice_inventory"] = [dict(c) for c in S["choice_inventory"]]
        for c in S["choice_inventory"]:
            if c["choice"] == "the window widths":
                c["instances"] = c["instances"] + 1
        ci_bad = [c["choice"] for c in S["choice_inventory"]
                  if "class" not in c or "fibre" not in c
                  or (c["class"] in ("GENUINELY-FREE", "DECLARED-WINDOW")
                      and not c.get("why"))
                  or (c["choice"] in live and c["instances"] != "all"
                      and c["instances"] != live[c["choice"]])]
    LD.gate("G-CHOICES-INVENTORIED",
            "every construction choice is inventoried with its class and its "
            "fibre; every FREE or WINDOWED choice carries the reason it was "
            "made; and every inventoried instance count is checked against "
            "the number of instances the run actually executed, so a choice "
            "cannot be priced at a number the sweep did not reach",
            not ci_bad and any(c["class"] == "DECLARED-WINDOW"
                               for c in S["choice_inventory"]),
            "%d choices inventoried, %d instance counts checked against the "
            "live sweeps, failing: %s"
            % (len(S["choice_inventory"]), len(live), ci_bad or "none"))

    # ---- the declared-instance registry: NOT_EXECUTED has a WRITER -------
    # Every declared sweep states its planned instance set before it runs and
    # the executed set is read back off the published rows; anything planned
    # and not reached is APPENDED to NOT_EXECUTED, which G-NOT-EXECUTED-EMPTY
    # then reports.  Without a writer that gate could not fail on any input.
    plans = [
        ("the arenas", {(L, nm) for L in LADDER
                        for nm in ["LINK"]
                        + ["AXIS-%d-%d" % a for a in axes(L)
                           if torus_absmax(a, L) == 1]
                        + ["LINK-PLUS-4TH"]},
         {(r["L"], r["arena"]) for r in arenas}),
        ("the control rows", {(nm, an) for nm in ("LINK", "LINK-PLUS-4TH")
                              for an, _a in PROBE_ALPHABETS},
         {(c["arena"], c["alphabet"]) for c in ctrl}),
        ("the band cells", {(r, L) for r in WIDTHS for L in BAND_SIZES},
         {(b["r"], b["L"]) for b in band_rows if b.get("L") is not None}),
        ("the profile rows", {(L, nm) for L in LADDER
                              for nm, _o in PLAQ_STENCILS},
         {(r["L"], r["stencil"]) for r in prof_rows}),
        ("the char-p scans",
         {(q, nm) for q in CHAR_P_FIELDS for nm, St, _n, _d, _f
          in char_p_arenas()
          if len(finite_field(q)[0]) ** len(St) <= CHAR_P_SCAN_WINDOW},
         {(r["q"], r["arena"]) for r in cp_rows}),
        ("the persistence rows", {r["invariant"] for r in T},
         {r["invariant"] for r in T if r["verdict"]}),
    ]
    if mut("MUT-INSTANCE-PLAN"):
        plans[0] = (plans[0][0], plans[0][1] | {(99, "PLANNED-NEVER-RUN")},
                    plans[0][2])
    S["declared_instances"] = []
    for nm, planned, done in plans:
        missed = sorted(str(x) for x in (planned - done))
        S["declared_instances"].append({"sweep": nm, "planned": len(planned),
                                        "executed": len(done),
                                        "not_executed": missed})
        for x in missed:
            NOT_EXECUTED.append("%s :: %s" % (nm, x))
    LD.gate("G-DECLARED-INSTANCES-EXECUTED",
            "every declared sweep states its planned instance set and the "
            "executed set is read back off the rows it published; the two are "
            "compared instance by instance, and anything planned but not "
            "reached is written into the not-executed list rather than "
            "silently dropped",
            all(not d["not_executed"] for d in S["declared_instances"]),
            "%d sweeps, %d planned instances, %d executed"
            % (len(plans), sum(d["planned"] for d in S["declared_instances"]),
               sum(d["executed"] for d in S["declared_instances"])))

    S["runtime_inputs"] = {"sources": [rel for _s, rel, _d, _n in SOURCES],
                           "object_under_test": PAPER_REL,
                           "reads": sorted(set(READS))}
    if mut("MUT-EXTRA-READ"):
        READS.append("v14/LOG.md")
    extra = [r for r in set(READS)
             if r not in {rel for _s, rel, _d, _n in SOURCES}
             and not r.endswith(PAPER_REL) and not os.path.isabs(r)]
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


def _setstr(xs):
    """{a,b,c} rendered from a measured list -- never typed."""
    return "{" + ",".join(str(x) for x in xs) + "}"


def build_verdict(S):
    """the head is DERIVED from the sealed primitive tables; the segments are
    built here and re-derived independently at G-VERDICT-RECONSTRUCTED.
    NO segment carries a typed measurement: every number and every set below
    is rendered from a receipt table."""
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
    band = {b["r"]: b for b in S["band_law"]["by_width"]}
    vel = {r["L"]: r for r in S["velocity_census"]}
    eig = {r["L"]: r for r in S["dispersion_census"]}
    glob = {r["L"]: r for r in S["global_stencil"]}
    br = LADDER[1]                                # the rung the breaks name
    velw = vel[br]["witness"]
    seg = []
    seg.append("SIDON=SUFFICIENCY-HOLDS-AT-%d-OF-%d-SIDON-ARENAS"
               "(VACUOUS-AT-THE-OTHER-%d;THE-IMPLICATION-HOLDS-AT-ALL-%d);"
               "LINK-STENCIL-SIDON-AND-MONOMIAL-ONLY-AT-L-%d-AND-%d"
               "(%d-AND-%d-NON-MONOMIAL-OF-%d-AND-%d-UNITARY);"
               "NECESSITY-FAILS-AT-%d-ARENAS(FIRST-IN-THE-DECLARED-ORDER=%s;"
               "ALL-%d-LOCAL-AXES-AT-L-%d-FAIL-TOGETHER)"
               % (p["sufficiency_substantive_holding"],
                  p["sufficiency_substantive"], p["sufficiency_vacuous"],
                  len(p["rows"]), LADDER[1], LADDER[2],
                  link[LADDER[1]]["non_monomial"],
                  link[LADDER[2]]["non_monomial"],
                  link[LADDER[1]]["unitary"], link[LADDER[2]]["unitary"],
                  p["necessity_failures"],
                  p["necessity_failure_arenas"][0].replace("=", "-")
                  .replace(" ", "-"),
                  sum(1 for r in S["sidon_arenas"]
                      if r["L"] == LADDER[1] and r["arena"].startswith("AXIS")
                      and not r["sidon"] and r["monomial_only"]),
                  LADDER[1]))
    seg.append("CONTROL=THE-FOURTH-DIRECTION-DEATH-DOES-NOT-TRANSPORT"
               "(REGISTERED-%d-REPRODUCED-AT-THE-CONTROL-RUNG-L-%d;"
               "%d-AT-L-%d;%d-AND-%d-AT-L-%d-AND-L-%d-BY-THEOREM-OVER-ANY-"
               "FIELD-WITH-AN-INVOLUTION;ALPHABET-RELATIVE-%d-NON-MONOMIAL-"
               "OVER-THE-%d-ELEMENT-ALPHABET-OF-THE-PARENTS)"
               % (ctl["registered_count_reproduced"], c["control_rung"],
                  [r["non_monomial"] for r in ctl["ladder_rows"]
                   if r["L"] == LADDER[0]][0], LADDER[0],
                  [r["non_monomial"] for r in ctl["ladder_rows"]
                   if r["L"] == LADDER[1]][0],
                  [r["non_monomial"] for r in ctl["ladder_rows"]
                   if r["L"] == LADDER[2]][0], LADDER[1], LADDER[2],
                  [r["non_monomial"] for r in ctl["control_rung_rows"]
                   if r["arena"] == "LINK-PLUS-4TH"
                   and r["alphabet"] == "R4-25"][0], c["alphabet"]))
    seg.append("LAW=DDS-FREE-FORCES-MONOMIAL-OVER-ANY-FIELD-WITH-AN-"
               "INVOLUTION(NO-DIFFERENCE-DOUBLED-SUBSET;%d-OF-%d-ARENAS-DDS-"
               "FREE-AND-ALL-MONOMIAL-ONLY;SIDON-STRICTLY-STRONGER-AT-%d-"
               "ARENAS;EXERCISED-IN-%d-FINITE-FIELDS-AT-%d-EXHAUSTIVE-SCANS)"
               % (S["dds_law"]["arenas_dds_free"], c["arenas"],
                  S["dds_law"]["sidon_but_not_the_only_forced"],
                  c["char_p_fields"], c["char_p_scans"]))
    seg.append("VMAX=DIAMETER-AT-EVERY-RUNG(%s;%s;%s=L/2)"
               % (c["vmax_L4"], c["vmax_L6"], c["vmax_L8"]))
    seg.append("INTERIOR-RADII=%d;%d;%d(THE-%d-AT-L-%d-REGISTER-CLAIM-"
               "RE-DERIVED-FROM-A-POOL-BUILT-HERE;EQUAL-TO-THE-LOCALITY-"
               "ADMITTING-WIDTH-SET-BY-THEOREM(BOTH-ARE-{1..diam-1}))"
               % (c["interior_L4"], c["interior_L6"], c["interior_L8"],
                  c["interior_L8"], LADDER[2]))
    seg.append("FINGERPRINT=(ORDER,SUPPORT)-PROFILE-IDENTICAL-AT-ALL-%d-"
               "RUNGS-ON-ALL-%d-ANTIDIAGONAL-COINS(%s);"
               "GLOBAL-SUPPORT-IS-THE-VOLUME-%d;%d;%d;NO-GROUP-SELECTION-LAW-"
               "CLAIMED" % (c["rungs"], c["coins_antidiagonal"],
                            [r["read"] for r in S["path_value_anchors"]
                             if r["anchor"] == "PV-PROFILE"][0],
                            glob[LADDER[0]]["support"],
                            glob[LADDER[1]]["support"],
                            glob[LADDER[2]]["support"]))
    seg.append("SCALE=THE-PARENTS-UNIQUE-SIZE-IS-WINDOW-RELATIVE"
               "(ADMITTED-SIZES-AT-WIDTH-r-ARE-THE-L-WITH-L>=2r+2-WHOSE-"
               "RADIUS-r-BALL-CARRIES-A-DIFFERENCE-DOUBLED-SUBSET-REALISED-"
               "OVER-THE-ALPHABET;%s;TWO-MECHANISMS(INVOLUTION-PAIR-EVEN-L<="
               "4r;PERFECT-DIFFERENCE-SET-AT-L-%d-r-%d);EVENNESS-IS-NOT-A-"
               "LAW;BOTH-HALVES-FORCED(LOCALITY-BELOW-2r+2;INJECTIVITY-ABOVE-"
               "4r;EXHAUSTED-CENSUS-TO-SUPPORT-CEILING-%d-BETWEEN);"
               "ALPHABET-RELATIVE(THE-ORDER-3-COSET-AT-L-%d-r-%d-CARRIES-%d-"
               "OVER-THE-PARENTS-%d-AND-%d-OVER-THE-%d-VALUE-PROBE))"
               % (";".join("WIDTH-%d=%s" % (r, _setstr(band[r]["admitted_set"]))
                           for r in sorted(band)),
                  S["l7_witness"]["L"], S["l7_witness"]["width"],
                  c["support_ceiling"], S["odd_coset"]["L"],
                  S["odd_coset"]["width"],
                  [r["non_monomial"] for r in S["odd_coset"]["rows"]
                   if r["alphabet"] == "R4-25"][0], c["alphabet"],
                  [r["non_monomial"] for r in S["odd_coset"]["rows"]
                   if r["alphabet"] == "THIRDS-19"][0],
                  [r["alphabet_size"] for r in S["odd_coset"]["rows"]
                   if r["alphabet"] == "THIRDS-19"][0]))
    seg.append("BREAKS=LOCAL-NON-MONOMIAL-FAMILY-EMPTY-FROM-L-%d;"
               "INTEGER-VELOCITIES-FAIL-AT-L-%d(SPEED-%s-ON-AN-ORDER-%d-AXIS;"
               "THE-%d-NON-INTEGER-FAMILIES-ARE-THE-%d-DDS-PERMITTED-NON-"
               "MONOMIAL-FAMILIES);EIGENPHASE-LATTICE-TRANSFORMS-Z/lcm(%d,L)"
               "(%d;%d;%d)"
               % (br, br, velw["speed"], velw["axis_order"],
                  vel[br]["non_integer_families"],
                  vel[br]["non_monomial_families"], c["gauge_group_order"],
                  eig[LADDER[0]]["eigenphase_lattice"],
                  eig[LADDER[1]]["eigenphase_lattice"],
                  eig[LADDER[2]]["eigenphase_lattice"]))
    seg.append("TABLE=%d-ROWS(%d-PERSIST(%d-FORCED;%d-CONTINGENT);%d-BREAK;"
               "%d-TRANSFORM)"
               % (c["table_rows"], c["persists"], c["persists_forced"],
                  c["persists_contingent"], c["breaks"], c["transforms"]))
    seg.append("SCOPE=D=%d;RUNGS=L-IN-%s+CONTROL-RUNG-L-%d;FIELD=Q(ZETA-24);"
               "ALPHABET=%d;WIDTHS=%s;BAND-SWEEP=L-IN-%d..%d;"
               "STENCIL=3-TERM-AXIS-AND-THE-ANCHORED-LINK-SET;"
               "CONNECTIVE=MAX-NORM(FORCED-BY-ANCHORED-LINK-%s);"
               "SECTOR=SINGLE-OCCUPATION;"
               "INDIVISIBILITY=DECLARED-BY-DIVISION-EVENT-TIMES;"
               "FINITE-LATTICE-ONLY;NO-CONTINUUM-CLAIM;"
               "NO-TRANSPORT-NUMBER-INHERITED;"
               "PERSISTENCE-AT-DECLARED-FINITE-RUNGS-ONLY"
               % (c["d"], _setstr(c["rungs_declared"]), c["control_rung"],
                  c["alphabet"], _setstr(sorted(band)),
                  c["band_sweep_low"], c["band_sweep_high"],
                  c["forcing_link"]))
    body = "|".join(seg)
    if mut("MUT-WALLS"):
        body = body.replace("NO-CONTINUUM-CLAIM", "CONTINUUM-LIMIT-ESTABLISHED")
    return head, head + "<" + body + ">"


def reconstruct_verdict(receipt):
    """the INDEPENDENT comparator: rebuilt from the receipt's own primitive
    tables by code that shares no literal and no helper with the builder.
    Every part below is recovered from a table the builder did not consult in
    the same way, and each is compared BY EQUALITY against the segment parsed
    out of the emitted string -- never by membership."""
    c = receipt["counts"]
    p = receipt["sidon_prediction"]
    names = {"SUFFICIENT-NOT-NECESSARY": "PERL-SIDON-SUFFICIENT-NOT-NECESSARY",
             "CONFIRMED-BOTH-WAYS": "PERL-SIDON-CONFIRMED-BOTH-WAYS",
             "REFUTED": "PERL-SIDON-REFUTED"}
    head = names[p["verdict"]]
    rungs = sorted({r["L"] for r in receipt["sidon_arenas"]})
    link = {r["L"]: r for r in receipt["sidon_arenas"]
            if r["arena"] == "LINK"}
    four = {r["L"]: r for r in receipt["sidon_arenas"]
            if r["arena"] == "LINK-PLUS-4TH"}
    ctlrows = receipt["fourth_direction_control"]["control_rung_rows"]
    vel = {r["L"]: r for r in receipt["velocity_census"]}
    eig = {r["L"]: r for r in receipt["dispersion_census"]}
    glob = {r["L"]: r for r in receipt["global_stencil"]}
    tab = receipt["persistence_table"]
    parts = {}
    parts["SIDON"] = [
        sum(1 for r in p["rows"] if r["sidon"] and r["sufficiency_holds"]),
        sum(1 for r in p["rows"] if r["sidon"]),
        sum(1 for r in p["rows"] if not r["sidon"]), len(p["rows"]),
        [link[rungs[1]]["non_monomial"], link[rungs[2]]["non_monomial"]],
        [link[rungs[1]]["unitary"], link[rungs[2]]["unitary"]],
        sum(1 for r in p["rows"] if not r["necessity_holds"])]
    parts["CONTROL"] = [
        [r["non_monomial"] for r in ctlrows
         if r["arena"] == "LINK-PLUS-4TH" and r["alphabet"] == "THIRDS-19"][0],
        receipt["counts"]["control_rung"],
        [four[L]["non_monomial"] for L in rungs],
        [r["non_monomial"] for r in ctlrows
         if r["arena"] == "LINK-PLUS-4TH" and r["alphabet"] == "R4-25"][0]]
    parts["LAW"] = [sum(1 for r in receipt["sidon_arenas"] if r["dds_free"]),
                    len(receipt["sidon_arenas"]),
                    sum(1 for r in receipt["sidon_arenas"]
                        if r["dds_free"] and not r["sidon"]),
                    len(receipt["char_p_census"]["fields"]),
                    len(receipt["char_p_census"]["rows"])]
    parts["VMAX"] = [r["vmax"] for r in receipt["vmax_census"]]
    parts["INTERIOR-RADII"] = [r["interior_count"]
                               for r in receipt["interior_radii"]]
    parts["FINGERPRINT"] = [
        len(rungs),
        receipt["coin_sectors"]["sectors"]["ANTIDIAGONAL"],
        [glob[L]["support"] for L in rungs]]
    parts["SCALE"] = [
        {str(b["r"]): b["admitted_set"] for b in receipt["band_law"]
         ["by_width"]},
        [receipt["l7_witness"]["L"], receipt["l7_witness"]["width"]],
        receipt["support_ceiling"]["ceiling"],
        [receipt["odd_coset"]["L"], receipt["odd_coset"]["width"]],
        [[r["non_monomial"] for r in receipt["odd_coset"]["rows"]
          if r["alphabet"] == "R4-25"][0],
         [r["non_monomial"] for r in receipt["odd_coset"]["rows"]
          if r["alphabet"] == "THIRDS-19"][0],
         [r["alphabet_size"] for r in receipt["odd_coset"]["rows"]
          if r["alphabet"] == "THIRDS-19"][0]]]
    parts["BREAKS"] = [
        min(r["L"] for r in receipt["pool_census"]
            if r["local_non_monomial"] == 0),
        vel[rungs[1]]["witness"]["speed"],
        vel[rungs[1]]["witness"]["axis_order"],
        vel[rungs[1]]["non_integer_families"],
        vel[rungs[1]]["non_monomial_families"],
        receipt["pool_census"][0]["orbit_sizes"][0],
        [eig[L]["eigenphase_lattice"] for L in rungs]]
    parts["TABLE"] = [
        len(tab), sum(1 for r in tab if r["verdict"] == "PERSISTS"),
        sum(1 for r in tab if r["verdict"] == "PERSISTS"
            and r["status"] == "FORCED"),
        sum(1 for r in tab if r["verdict"] == "PERSISTS"
            and r["status"] != "FORCED"),
        sum(1 for r in tab if r["verdict"].startswith("BREAKS")),
        sum(1 for r in tab if r["verdict"] == "TRANSFORMS")]
    parts["SCOPE"] = [
        c["d"], rungs, receipt["counts"]["control_rung"], c["alphabet"],
        sorted(int(b["r"]) for b in receipt["band_law"]["by_width"]),
        [min(b["L"] for b in receipt["band_law"]["rows"]),
         max(b["L"] for b in receipt["band_law"]["rows"])]]
    return head, parts


def parse_verdict_parts(fp):
    """READ THE STRING BACK.  Each segment is parsed into the structured
    values a reader would take off it, so the emitted string and the receipt's
    tables can be compared BY EQUALITY rather than by membership.  This is a
    parser, not a second copy of the builder's concatenation: it shares no
    format string and no helper with `build_verdict`, and a segment whose
    shape has drifted fails to parse rather than passing silently."""
    def grab(key, pattern, cast=int):
        m = re.search(pattern, fp.get(key, ""))
        if m is None:
            raise GateFail("G-VERDICT-RECONSTRUCTED :: the %s segment does "
                           "not parse against %r" % (key, pattern))
        return [cast(g) for g in m.groups()]

    def ints(s):
        return [int(x) for x in s.split(",") if x.strip()]

    out = {}
    a = grab("SIDON", r"SUFFICIENCY-HOLDS-AT-(\d+)-OF-(\d+)-SIDON-ARENAS"
                      r"\(VACUOUS-AT-THE-OTHER-(\d+);"
                      r"THE-IMPLICATION-HOLDS-AT-ALL-(\d+)\)")
    b = grab("SIDON", r"\((\d+)-AND-(\d+)-NON-MONOMIAL-OF-(\d+)-AND-(\d+)"
                      r"-UNITARY\)")
    d = grab("SIDON", r"NECESSITY-FAILS-AT-(\d+)-ARENAS")
    out["SIDON"] = a + [[b[0], b[1]], [b[2], b[3]]] + d
    a = grab("CONTROL", r"REGISTERED-(\d+)-REPRODUCED-AT-THE-CONTROL-RUNG-"
                        r"L-(\d+)")
    b = grab("CONTROL", r";(\d+)-AT-L-\d+;(\d+)-AND-(\d+)-AT-L-\d+-AND-L-\d+"
                        r"-BY-THEOREM")
    d = grab("CONTROL", r"ALPHABET-RELATIVE-(\d+)-NON-MONOMIAL-OVER-THE-\d+"
                        r"-ELEMENT")
    out["CONTROL"] = a + [b] + d
    out["LAW"] = grab("LAW", r"\(NO-DIFFERENCE-DOUBLED-SUBSET;(\d+)-OF-(\d+)"
                             r"-ARENAS-DDS-FREE-AND-ALL-MONOMIAL-ONLY;"
                             r"SIDON-STRICTLY-STRONGER-AT-(\d+)-ARENAS;"
                             r"EXERCISED-IN-(\d+)-FINITE-FIELDS-AT-(\d+)"
                             r"-EXHAUSTIVE-SCANS\)")
    v = grab("VMAX", r"DIAMETER-AT-EVERY-RUNG\(([^)]*)\)", str)[0]
    out["VMAX"] = [x.split("=")[0] for x in v.split(";")]
    out["INTERIOR-RADII"] = grab("INTERIOR-RADII", r"^(\d+);(\d+);(\d+)\(")
    a = grab("FINGERPRINT", r"IDENTICAL-AT-ALL-(\d+)-RUNGS-ON-ALL-(\d+)"
                            r"-ANTIDIAGONAL-COINS")
    b = grab("FINGERPRINT", r"GLOBAL-SUPPORT-IS-THE-VOLUME-(\d+);(\d+);(\d+)")
    out["FINGERPRINT"] = a + [b]
    sec = dict((r, ints(s)) for r, s in
               re.findall(r"WIDTH-(\d+)=\{([^}]*)\}", fp.get("SCALE", "")))
    a = grab("SCALE", r"PERFECT-DIFFERENCE-SET-AT-L-(\d+)-r-(\d+)")
    b = grab("SCALE", r"SUPPORT-CEILING-(\d+)")
    d = grab("SCALE", r"THE-ORDER-3-COSET-AT-L-(\d+)-r-(\d+)-CARRIES-(\d+)"
                      r"-OVER-THE-PARENTS-\d+-AND-(\d+)-OVER-THE-(\d+)"
                      r"-VALUE-PROBE")
    out["SCALE"] = [sec, a, b[0], d[:2], d[2:]]
    a = grab("BREAKS", r"LOCAL-NON-MONOMIAL-FAMILY-EMPTY-FROM-L-(\d+)")
    sp = grab("BREAKS", r"INTEGER-VELOCITIES-FAIL-AT-L-\d+\(SPEED-([\d/]+)"
                        r"-ON-AN-ORDER-(\d+)-AXIS;THE-(\d+)-NON-INTEGER-"
                        r"FAMILIES-ARE-THE-(\d+)-DDS-PERMITTED", str)
    e = grab("BREAKS", r"Z/lcm\((\d+),L\)\((\d+);(\d+);(\d+)\)")
    out["BREAKS"] = (a + [sp[0]] + [int(x) for x in sp[1:]] + [e[0]]
                     + [e[1:]])
    out["TABLE"] = grab("TABLE", r"(\d+)-ROWS\((\d+)-PERSIST\((\d+)-FORCED;"
                                 r"(\d+)-CONTINGENT\);(\d+)-BREAK;(\d+)"
                                 r"-TRANSFORM\)")
    a = grab("SCOPE", r"^D=(\d+);RUNGS=L-IN-\{([^}]*)\}\+CONTROL-RUNG-L-"
                      r"(\d+)", str)
    b = grab("SCOPE", r"ALPHABET=(\d+);WIDTHS=\{([^}]*)\};BAND-SWEEP=L-IN-"
                      r"(\d+)\.\.(\d+)", str)
    out["SCOPE"] = [int(a[0]), ints(a[1]), int(a[2]), int(b[0]), ints(b[1]),
                    [int(b[2]), int(b[3])]]
    return out


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

# E-22, repaired.  The delivered licence set admitted EVERY integer 0-24
# unconditionally, so 24 of the paper's numerals were licensed by range alone
# and a forged `14 of 18` survived at exit 0.  The blanket is gone.  A numeral
# is structural only if it is
#   (a) a heading number, COMPUTED from the paper's own heading lines;
#   (b) a digit run inside a commit-sha token the paper cites, COMPUTED from
#       the paper's own text;
#   (c) one of the named engravings and ledger entries below, each with the
#       reason it is cited.
# Everything else must be licensed by a value in the receipt.
ENGRAVINGS = {
    "20": "engraving #20: paper coverage includes fenced blocks",
    "22": "engraving E-22: inline-span coverage; blocks by multiset",
    "23": "engraving E-23: falsifier honesty",
    "24": "engraving E-24: measure-relativity of counts",
    "34": "engraving #34: honest denominators",
    "46": "engraving #46: the runtime-input rule",
    "82": "engraving #82: the CLI contract",
    "87": "engraving #87: gates bind objects, not cardinalities",
    "91": "engraving #91: no moving refs, off-tree and git-less",
    "119": "engraving #119: the gate-to-disk seal",
    "125": "engraving #125: text gates match text as written",
    "148": "engraving #148: the seal manifest is total",
    "196": "the v14 ledger entry at which this unit's pin was frozen",
    "228": "the v14 ledger entry that carries this unit's adjudication",
    "2026": "the year in the dateline",
}
PAPER_REFERENCES = {
    "02": "paper 02, the manifold rung (R2)",
    "29": "paper 29, PER-R, the successor unit named in the register",
}


def heading_numerals(txt):
    """(a) the paper's own section and subsection labels, read off its
    heading lines rather than declared as a range."""
    out = set()
    for line in txt.split("\n"):
        if line.startswith("#"):
            out |= numerals(line)
    return out


def sha_numerals(txt):
    """(b) the digit runs inside the commit-sha tokens the paper cites.  A
    sha fragment is a provenance reference, not a claim."""
    out = set()
    for tok in re.findall(r"\b(?=[0-9a-f]{7,12}\b)(?=[a-f0-9]*[a-f])"
                          r"[0-9a-f]{7,12}\b", txt):
        out |= numerals(tok)
    return out


def structural_numerals(txt):
    return (heading_numerals(txt) | sha_numerals(txt) | set(ENGRAVINGS)
            | set(PAPER_REFERENCES))


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
        {"id": "CL-SUFFICIENCY-SPLIT",
         "path": "sidon_prediction/sufficiency_substantive",
         "text": "the implication is substantively tested at the %d Sidon "
                 "arenas and holds vacuously at the other %d"
                 % (p["sufficiency_substantive"], p["sufficiency_vacuous"])},
        {"id": "CL-DDS-FRACTION", "path": "declared_fractions/0/value",
         "text": "the count %s is stamped COUNTING-ONLY"
                 % S["declared_fractions"][0]["value"]},
        {"id": "CL-BAND7", "path": "l7_witness/matrix_entries_checked",
         "text": "the full %d by %d matrix satisfies U-dagger-U = I, all %d "
                 "entries checked, %d mismatches"
                 % (S["l7_witness"]["matrix_dimension"],
                    S["l7_witness"]["matrix_dimension"],
                    S["l7_witness"]["matrix_entries_checked"],
                    S["l7_witness"]["matrix_mismatches"])},
        {"id": "CL-BAND-CEILING", "path": "support_ceiling/ceiling",
         "text": "a unitary map over this alphabet has at most %d nonzero "
                 "coefficients" % S["support_ceiling"]["ceiling"]},
        {"id": "CL-ODD-COSET", "path": "odd_coset/rows/2/non_monomial",
         "text": "carries %d non-monomial unitaries over the parents' 25 and "
                 "%d over the 19-value probe"
                 % ([r["non_monomial"] for r in S["odd_coset"]["rows"]
                     if r["alphabet"] == "R4-25"][0],
                    [r["non_monomial"] for r in S["odd_coset"]["rows"]
                     if r["alphabet"] == "THIRDS-19"][0])},
        {"id": "CL-CHAR-P", "path": "char_p_census/scans",
         "text": "%d exhaustive scans over %d finite fields, %d violations"
                 % (S["char_p_census"]["scans"],
                    len(S["char_p_census"]["fields"]),
                    len(S["char_p_census"]["violations"]))},
        {"id": "CL-FORCING", "path": "persistence_forcing/forced",
         "text": "%d of the %d PERSISTS rows are theorems restated at three "
                 "rungs and %d are contingent survivals"
                 % (S["persistence_forcing"]["forced"],
                    S["persistence_forcing"]["persist_rows"],
                    S["persistence_forcing"]["contingent"])},
        {"id": "CL-ONE-MECHANISM",
         "path": "velocity_census/1/non_monomial_families",
         "text": "the %d non-integer-velocity families at L = 6 are the %d "
                 "non-monomial families"
                 % ([r["non_integer_families"] for r in S["velocity_census"]
                     if r["L"] == 6][0],
                    [r["non_monomial_families"] for r in S["velocity_census"]
                     if r["L"] == 6][0])},
    ]
    return out


def paper_tables(S):
    """E-22: tables render as claims.  Each row below is the exact pipe row
    the paper must carry.  ALL SEVEN of the paper's tables render here -- the
    delivered instrument rendered two of them and left the band table, the
    one the paper itself nominated for attack, unbound."""
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
    # the control table (section 3.4)
    for r in S["fourth_direction_control"]["control_rung_rows"]:
        rows.append("| %s | %s | %d | %d | %d | %d |"
                    % (r["arena"], r["alphabet"], r["alphabet_size"],
                       r["maps"], r["unitary"], r["non_monomial"]))
    # the VMAX / dispersion table (section 4)
    for v, d, r in zip(S["vmax_census"], S["dispersion_census"],
                       S["interior_radii"]):
        rows.append("| %d | %d | %d | %s | %d | %d | %d |"
                    % (v["L"], d["families"], d["cells"], v["vmax"],
                       v["diameter"], r["interior_count"],
                       d["eigenphase_lattice"]))
    # the gauge profile table (section 5)
    for r in S["gauge_profile"]:
        if r["L"] != PARENT_RUNG:
            continue
        rows.append("| %s | %d | %d | %s | %s | same | same | same |"
                    % (r["stencil"], r["order"], r["support"],
                       " + ".join(str(x) for x in r["orbit_sizes"]),
                       r["position_class"].replace("x", " x ")))
    # the locality-window table (section 6)
    for w in S["locality_windows"]:
        rows.append("| %d | %d | %d | %d | %s | %s | %d |"
                    % (w["L"], w["r"], w["neighbours"], w["offsets"],
                       "yes" if w["complete"] else "no",
                       "yes" if w["locality"] else "no", w["b1"]))
    # THE BAND TABLE (section 7) -- the row the panel forged twice at exit 0
    for b in S["band_law"]["by_width"]:
        rows.append("| %d | %s | %s | %s |"
                    % (b["r"], b["admitted_set"], b["involution_pair_set"],
                       b["beyond_the_pair_mechanism"] or "-"))
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
    lic = licensed_numerals(S, set()) | structural_numerals(txt)
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

    lic = licensed_numerals(S, set()) | structural_numerals(txt)
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
    if mut("MUT-PAPER-SPAN"):
        spans = spans + ["the forged span 424242"]
    sn = set()
    for s in spans:
        sn |= numerals(s)
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
    """E-23, three-legged: each published description is bound to the branch
    its own switch guards by (1) the switch existing, (2) the digest of the
    guarded source matching the PINNED digest, and (3) the description's
    leading VERB lying in the verb set of its declared effect class."""
    src = read_text(SELF)
    rows = []
    for name, target, effect, note in MUTANTS:
        i = src.find('mut("%s")' % name)
        live = digest(src[i:i + 240]) if i >= 0 else None
        pinned = MUTANT_CODE_DIGESTS.get(name)
        verb = note.split()[0].lower()
        rows.append({"mutant": name, "target": target, "description": note,
                     "effect_class": effect, "verb": verb,
                     "switch_present": i >= 0,
                     "guarded_source_sha256_12": live,
                     "pinned_source_sha256_12": pinned,
                     "code_matches_its_pin": bool(pinned) and live == pinned,
                     "verb_matches_its_class":
                         verb in VERB_CLASSES.get(effect, ())})
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
    read_back = parse_verdict_parts(fp)
    if mut("MUT-COMPARATOR"):
        read_back = dict(read_back)
        read_back["TABLE"] = list(read_back["TABLE"])
        read_back["TABLE"][0] += 1
    mismatched = sorted(k for k in rparts
                        if json.dumps(read_back.get(k), sort_keys=True)
                        != json.dumps(rparts[k], sort_keys=True))
    ok = (rh == S["verdict"]["head"]
          and S["verdict"]["string"].startswith(rh + "<")
          and not mismatched
          and set(fp) == set(rparts))
    LD.gate("G-VERDICT-RECONSTRUCTED",
            "the head and EVERY segment of the verdict string are bound "
            "twice: the segments are re-derived from the receipt's own "
            "primitive tables by a comparator that shares no literal, no "
            "format string and no helper with the builder, and the emitted "
            "string is PARSED BACK into structured values which are compared "
            "against them BY EQUALITY, value for value -- not by membership, "
            "and not by re-writing the same concatenation twice",
            ok, "head %s, %d segments, %d parts compared by equality, "
            "mismatched: %s"
            % (S["verdict"]["head"], len(fp), len(rparts),
               mismatched or "none"))

    # ---- E-24: the fraction census SCANS, it does not self-select --------
    # The delivered gate checked a hand-written two-row list and could not
    # discover an unstamped fraction.  This one scans the rendered paper AND
    # the emitted verdict string for every fraction-shaped construction and
    # requires each hit to be covered by a stamped row built from a receipt
    # value; a row that no hit reaches is a dead declaration and also fails.
    c = S["counts"]
    fr = [
        {"name": "arenas that are DDS-free",
         "value": "%d of %d" % (c["arenas_dds_free"], c["arenas"]),
         "forms": ["%d of %d" % (c["arenas_dds_free"], c["arenas"]),
                   "%d-OF-%d" % (c["arenas_dds_free"], c["arenas"])],
         "measure": "COUNTING-ONLY",
         "why": "a coverage report over this unit's own declared arena list, "
                "which is not a sample of any population and carries no "
                "measure; the criterion's soundness is a theorem"},
        {"name": "Sidon arenas at which sufficiency is substantively tested",
         "value": "%d of %d" % (c["arenas_sidon_substantive"],
                                c["arenas_sidon"]),
         "forms": ["%d of %d" % (c["arenas_sidon_substantive"],
                                 c["arenas_sidon"]),
                   "%d-OF-%d" % (c["arenas_sidon_substantive"],
                                 c["arenas_sidon"])],
         "measure": "COUNTING-ONLY",
         "why": "the honest denominator of the sufficiency direction: the "
                "implication is vacuous wherever its antecedent is false, so "
                "the Sidon arenas are the ones it is tested at"},
        {"name": "arenas at which necessity fails",
         "value": "%d of %d" % (c["necessity_failures"], c["arenas"]),
         "forms": ["%d of them" % c["necessity_failures"]],
         "measure": "COUNTING-ONLY",
         "why": "the same declared list, read the other way; a count of "
                "arenas, not a rate over any space of arenas"},
        {"name": "odd sizes in the width/radius join sweep",
         "value": "%d of %d" % (c["join_odd_sizes"], c["join_sizes"]),
         "forms": ["%d of them" % c["join_odd_sizes"]],
         "measure": "COUNTING-ONLY",
         "why": "a count over the declared band sweep, which is a "
                "presentation range and not a sample; the identity it "
                "reports is a theorem at every size, odd or even"},
    ]
    fr_txt = paper_text + " " + S["verdict"]["string"]
    if mut("MUT-FRACTION"):
        fr_txt = fr_txt + "  an unstamped 5 of 7 slipped into the prose"
    hits = sorted(set(re.findall(r"\d+ of \d+", fr_txt))
                  | set(re.findall(r"\d+-OF-\d+", fr_txt))
                  | set(re.findall(r"\d+ of them", fr_txt)))
    covered = {f for row in fr for f in row["forms"]}
    unstamped = [h for h in hits if h not in covered]
    dead = [row["name"] for row in fr
            if not any(f in fr_txt for f in row["forms"])]
    nomeasure = [row["name"] for row in fr if not row.get("measure")]
    S["declared_fractions"] = fr
    S["fraction_census"] = {"scanned": ["the rendered paper", "the verdict "
                                        "string"],
                            "patterns": ["N of M", "N-OF-M", "N of them"],
                            "hits": hits, "covered": sorted(covered),
                            "unstamped": unstamped, "dead_rows": dead}
    LD.gate("G-FRACTIONS-STAMPED",
            "the fraction census SCANS rather than self-selects: every "
            "fraction-shaped construction in the rendered paper and in the "
            "emitted verdict string is found by pattern, and each hit must be "
            "covered by a row that carries its measure or the COUNTING-ONLY "
            "stamp.  A declared row no hit reaches is a dead declaration and "
            "fails here too, so the census has a denominator",
            not unstamped and not dead and not nomeasure,
            "%d fraction-shaped hits over %d stamped rows; unstamped %s, "
            "dead %s, unmeasured %s"
            % (len(hits), len(fr), unstamped or "none", dead or "none",
               nomeasure or "none"))

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
        # inverts the DESCRIPTION's leading verb and nothing else: the code
        # is untouched, which is exactly the injection a switch-existence
        # gate cannot see.
        inv = {"drops": "adds", "adds": "drops", "shortens": "lengthens",
               "moves": "pins", "reports": "conceals"}
        fd[0] = dict(fd[0])
        old_verb = fd[0]["verb"]
        fd[0]["description"] = fd[0]["description"].replace(
            old_verb, inv.get(old_verb, "preserves"), 1)
        fd[0]["verb"] = fd[0]["description"].split()[0].lower()
        fd[0]["verb_matches_its_class"] = (
            fd[0]["verb"] in VERB_CLASSES.get(fd[0]["effect_class"], ()))
    S["falsifier_descriptions"] = fd
    no_switch = [r["mutant"] for r in fd if not r["switch_present"]]
    drifted = [r["mutant"] for r in fd if not r["code_matches_its_pin"]]
    misdescribed = [r["mutant"] for r in fd
                    if not r["verb_matches_its_class"]]
    LD.gate("G-FALSIFIER-DESCRIPTIONS",
            "every published mutant description is bound to the branch its "
            "own switch guards THREE ways: the switch exists in this file; "
            "the digest of the guarded source equals the digest PINNED in "
            "the frozen registry, so code cannot move away from its "
            "description; and the description's leading verb lies in the "
            "verb set of its declared effect class, so a description cannot "
            "be inverted while its code stands still",
            not no_switch and not drifted and not misdescribed,
            "%d descriptions: %d without a switch (%s), %d whose guarded "
            "source has drifted from its pin (%s), %d whose verb does not "
            "match its declared effect class (%s)"
            % (len(fd), len(no_switch), no_switch or "none", len(drifted),
               drifted or "none", len(misdescribed), misdescribed or "none"))

    # THE LEDGER COVERS EVERY GATE THE RUN WILL REACH, not only the ones
    # already closed: the gates that run after this point are enumerated in
    # REMAINING_GATES and classified here, and G-GATE-LEDGER-COVERS-THE-RUN
    # requires the closed ledger to have an entry for every gate row.
    # E-23, repaired: STRUCTURAL is NO LONGER AN UNCONDITIONAL `else`.  A gate
    # enters that bucket only through the explicit registry above, which names
    # its two independently computed sides; a gate that is neither a mutant
    # target, nor waived with a forcing, nor registered STRUCTURAL is
    # UNCLASSIFIED and dies at G-WAIVERS-VERIFIED.
    waivers, unclassified = [], []
    targets = {m[1] for m in MUTANTS}
    reach = sorted(set(LD.ids) | set(REMAINING_GATES) | set(LATE_GATES)
                   | set(FORCINGS))
    if mut("MUT-VACUOUS-GATE"):
        reach = reach + ["G-INJECTED-VACUOUS"]
    if mut("MUT-STRUCTURAL-STALE"):
        reach = [g for g in reach
                 if g != "G-DISPERSION-REPRODUCES-THE-PARENT"]
    for gid in reach:
        if gid in targets:
            waivers.append({"gate": gid, "status": "FALSIFIABLE",
                            "falsifier": [m[0] for m in MUTANTS
                                          if m[1] == gid][0]})
        elif gid in FORCINGS:
            waivers.append({"gate": gid, "status": "WAIVED",
                            "forcing": FORCINGS[gid]})
        elif gid in STRUCTURAL_REGISTRY:
            sides = STRUCTURAL_REGISTRY[gid]
            waivers.append({"gate": gid, "status": "STRUCTURAL",
                            "route_a": sides[0], "route_b": sides[1],
                            "forcing": "a rebuild identity between two "
                                       "independently computed objects: %s "
                                       "against %s" % sides})
        else:
            unclassified.append(gid)
            waivers.append({"gate": gid, "status": "UNCLASSIFIED"})
    S["waiver_ledger"] = waivers
    S["structural_registry"] = [{"gate": g, "route_a": a, "route_b": b}
                                for g, (a, b)
                                in sorted(STRUCTURAL_REGISTRY.items())]
    stale = sorted((set(STRUCTURAL_REGISTRY) - set(reach))
                   | (set(STRUCTURAL_REGISTRY) & (targets | set(FORCINGS))))
    LD.gate("G-STRUCTURAL-REGISTERED",
            "the STRUCTURAL bucket is an explicit registry and not a default "
            "branch: each of its gates names the two independently computed "
            "objects its predicate compares, and no registered entry is dead "
            "-- every one is a gate this run reaches, and none of them is "
            "already covered by a mutant or a forcing, so the registry says "
            "exactly which gates rest on a rebuild identity and no more",
            not stale, "%d structural gates registered, %d of them dead "
            "(unreached, or already falsifiable or waived): %s"
            % (len(STRUCTURAL_REGISTRY), len(stale), stale or "none"))
    unguarded = [w["gate"] for w in waivers
                 if (w["status"] == "FALSIFIABLE" and not w.get("falsifier"))
                 or (w["status"] == "WAIVED" and not w.get("forcing"))
                 or (w["status"] == "STRUCTURAL"
                     and not (w.get("route_a") and w.get("route_b")))
                 or w["status"] == "UNCLASSIFIED"]
    LD.gate("G-WAIVERS-VERIFIED",
            "every gate is FALSIFIABLE with a named mutant, WAIVED with a "
            "named forcing, or STRUCTURAL through the explicit registry that "
            "names its two independently computed sides.  A gate that fits "
            "none of the three is UNCLASSIFIED and dies here -- there is no "
            "default branch that can bless it -- and the ledger is built over "
            "every gate the run will reach rather than only the ones already "
            "closed",
            not unguarded, "%d gates: %d falsifiable, %d waived, %d "
            "structural, %d unclassified: %s"
            % (len(waivers),
               sum(1 for w in waivers if w["status"] == "FALSIFIABLE"),
               sum(1 for w in waivers if w["status"] == "WAIVED"),
               sum(1 for w in waivers if w["status"] == "STRUCTURAL"),
               len(unclassified), unclassified or "none"))

    if mut("MUT-NOT-EXECUTED"):
        NOT_EXECUTED.append("the arenas :: (99, 'PLANNED-NEVER-RUN')")
    S["not_executed"] = list(NOT_EXECUTED)
    LD.gate("G-NOT-EXECUTED-EMPTY",
            "nothing declared was left unexecuted: the declared-instance "
            "registry writes every planned-but-unreached instance into this "
            "list as the sweeps close, and the list is required to be empty",
            not S["not_executed"], "%d entries: %s"
            % (len(S["not_executed"]), S["not_executed"] or "none"))

    cov = verify_paper(S, LD, paper_text)

    # THE PREDICTION, made before the remaining gates close: SIX more gates
    # run in this function (the totals, the floats, the seal, the seal
    # windows, the manifest and the chain) and FIVE in the delivery path (the
    # mutant sweep's adjudicator, the published-key check, the
    # ledger-coverage check, this prediction's own check and the final paper
    # pass).  G-GATES-CLOSED-AS-PREDICTED requires the ledger to end at
    # exactly this number, and G-ARTIFACT-INTEGRITY is the one gate evaluated
    # outside the ledger, which is why `gates` exceeds `gates_in_receipt` by
    # exactly one.
    S["totals"] = {
        "gates": len(LD.rows) + 12,
        "gates_in_receipt": len(LD.rows) + 11,
        "mutants": len(MUTANTS),
        "sources": len(SOURCES),
        "path_value_anchors": len(PATH_VALUE_ANCHORS),
        "verbatim_anchors": len(VERBATIM_ANCHORS),
        "seals": len(SEALED_PATHS),
        "claims": cov["claims"],
        "numerals": cov["numerals"],
    }
    # #87: EVERY totals key is re-derived from its own source, per key.  The
    # delivered gate bound two of nine, and a typed `9` survived.
    sources_of = {
        "gates": len(LD.rows) + 12,
        "gates_in_receipt": len(LD.rows) + 11,
        "mutants": len(MUTANTS),
        "sources": len(SOURCES),
        "path_value_anchors": len(PATH_VALUE_ANCHORS),
        "verbatim_anchors": len(VERBATIM_ANCHORS),
        "seals": len(SEALED_PATHS),
        "claims": len(S["paper_claims"]),
        "numerals": len(numerals(paper_text)),
    }
    if mut("MUT-TOTALS"):
        S["totals"] = dict(S["totals"])
        S["totals"]["sources"] = len(SOURCES) + 1
    typed = sorted(k for k, v in sources_of.items()
                   if S["totals"].get(k) != v)
    missing = sorted(set(S["totals"]) - set(sources_of))
    LD.gate("G-TOTALS-REDERIVED",
            "EVERY published total is re-derived from the object that "
            "produces it and compared per key -- the gate count from the "
            "closed ledger, the mutants from the registry, the sources and "
            "the anchors from their declarations, the seals from the sealed "
            "paths, the claims from the rendered claim list and the numerals "
            "from a fresh scan of the paper -- and no key is published that "
            "the re-derivation does not cover",
            not typed and not missing,
            "%d totals keys, all re-derived: typed %s, uncovered %s"
            % (len(S["totals"]), typed or "none", missing or "none"))

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

    # MUT-SEAL-BROKEN edits an ACTUAL SEALED OBJECT after its gate-time
    # digest was taken -- exactly what its description says -- rather than
    # faking the gate's input.
    if mut("MUT-SEAL-BROKEN"):
        S["counts"]["arenas"] = S["counts"]["arenas"] + 900
    broken = SEAL.verify(S)
    LD.gate("G-SEAL-COMPLETE",
            "every gate-time seal still verifies against the object it was "
            "taken from, in run, before the payload is built",
            not broken, "%d seals, broken: %s" % (len(SEAL.rows),
                                                  broken or "none"))

    # #148: the seal WINDOW -- the distance between the gate that closes a
    # value and the gate that seals it -- is published for every seal, and
    # the three seals whose values only exist at the final gate are named as
    # such rather than left to be discovered.
    # #148: a seal homed to a gate that closes BEFORE its value exists never
    # fires -- `Ledger.gate` skips the take when the path is not yet there --
    # and the delivered manifest gate could not see that, because it checks
    # key coverage by path root rather than that the take happened.  This gate
    # binds the two sides against each other: the DECLARED homing in
    # SEALED_PATHS, and the takes the run actually performed, seal by seal.
    # The split between "must already have fired" and "fires later" is READ
    # OFF THE LIVE LEDGER -- a seal is DUE exactly when its declared gate has
    # already closed -- so nothing here is typed and the two sides are
    # genuinely independent: SEALED_PATHS on one, the takes the run performed
    # and the gates it has actually closed on the other.
    LATE_BY_NECESSITY = ("SEAL-MUTANTS", "SEAL-GATES", "SEAL-COVERAGE",
                         "SEAL-SEAL-WINDOWS")
    closed = set(LD.ids)
    taken = {r["seal"]: r["sealed_at_gate"] for r in SEAL.rows}
    if mut("MUT-SEAL-WINDOW"):
        taken.pop("SEAL-BAND-CENSUS", None)
    win_rows2 = []
    for sid, path, g in SEALED_PATHS:
        win_rows2.append({
            "seal": sid, "path": path, "declared_gate": g,
            "its_gate_has_closed": g in closed,
            "taken_at_gate": taken.get(sid),
            "fired": sid in taken,
            "homed_as_declared": taken.get(sid) == g if sid in taken else None,
            "still_to_fire": g not in closed})
    never_fired = [r["seal"] for r in win_rows2
                   if r["its_gate_has_closed"] and not r["fired"]]
    mishomed = [r["seal"] for r in win_rows2
                if r["fired"] and not r["homed_as_declared"]]
    early = [r["seal"] for r in win_rows2
             if not r["its_gate_has_closed"] and r["fired"]]
    deferred = sorted(r["seal"] for r in win_rows2 if r["still_to_fire"])
    unreachable = [r["seal"] for r in win_rows2
                   if r["still_to_fire"]
                   and r["declared_gate"] not in set(REMAINING_GATES)]
    S["seal_windows"] = {
        "rows": win_rows2,
        "due_and_fired": sum(1 for r in win_rows2
                             if r["its_gate_has_closed"] and r["fired"]),
        "still_to_fire": deferred,
        "late_by_necessity": list(LATE_BY_NECESSITY),
        "note": "a seal is taken at the gate that CLOSES ITS VALUE.  A seal "
                "homed to a gate that closes before its value exists is "
                "silently skipped by the take and never fires at all -- that "
                "is the failure this gate catches.  The seals still to fire "
                "when this gate runs are exactly the four whose values do not "
                "exist yet, and each is homed to a gate the run will still "
                "reach"}
    LD.gate("G-SEAL-WINDOWS-DECLARED",
            "every seal whose gate HAS ALREADY CLOSED has actually fired, and "
            "fired at the gate it was declared to fire at; no seal has fired "
            "ahead of its gate; and every seal still to fire is homed to a "
            "gate the run will still reach.  A seal homed to a gate that "
            "closes before its value exists never fires, and the manifest "
            "gate cannot see that because it checks key coverage rather than "
            "the take -- so the declared homing and the takes actually "
            "performed are compared here, seal by seal",
            not never_fired and not mishomed and not early and not unreachable
            and deferred == sorted(LATE_BY_NECESSITY),
            "%d declared seals, %d due and fired, %d never fired (%s), %d "
            "homed elsewhere (%s), %d fired early (%s); still to fire: %s "
            "against the declared %s, %d of them homed to a gate the run "
            "never reaches"
            % (len(win_rows2), S["seal_windows"]["due_and_fired"],
               len(never_fired), never_fired or "none", len(mishomed),
               mishomed or "none", len(early), early or "none", deferred,
               sorted(LATE_BY_NECESSITY), len(unreachable)))

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
    # `mutants` is placed BEFORE G-MUTANTS-ON-TARGET closes, so the ledger's
    # own take seals it at that gate -- here and nowhere else, exactly as the
    # seal mechanism's comment says.  Nothing is sealed in a late take.
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
        out.append("  width r=%d admitted %s; involution-pair section %s; "
                   "beyond that mechanism %s"
                   % (b["r"], b["admitted_set"], b["involution_pair_set"],
                      b["beyond_the_pair_mechanism"] or "-"))
    w7 = S["l7_witness"]
    out.append("  the difference-set witness at L=%d r=%d: support %s, "
               "coefficients %s, multiplicities %s"
               % (w7["L"], w7["width"], w7["support"], w7["coefficients"],
                  w7["difference_multiplicities"]))
    out.append("    autocorrelation is a delta: %s; U-dagger-U = I over %d "
               "entries with %d mismatches; involutions in the group: %d"
               % (w7["autocorrelation_is_a_delta"],
                  w7["matrix_entries_checked"], w7["matrix_mismatches"],
                  w7["involutions_in_the_group"]))
    out.append("  the support ceiling, computed: %d  (profiles %s)"
               % (S["support_ceiling"]["ceiling"],
                  S["support_ceiling"]["profiles"]))
    out.append("  the odd coset at L=%d r=%d: %s"
               % (S["odd_coset"]["L"], S["odd_coset"]["width"],
                  {r["alphabet"]: r["non_monomial"]
                   for r in S["odd_coset"]["rows"]}))
    out.append("")
    out.append("THE DDS THEOREM OUTSIDE CHARACTERISTIC ZERO")
    for f in S["char_p_census"]["fields"]:
        out.append("  F%-3d char %-3d degree %d  involution order %d  "
                   "1 = -1: %s"
                   % (f["q"], f["characteristic"], f["degree"],
                      f["involution_order"], f["one_equals_minus_one"]))
    out.append("  %d exhaustive scans, %d of them DDS-free, %d violations"
               % (S["char_p_census"]["scans"],
                  S["char_p_census"]["dds_free_rows"],
                  len(S["char_p_census"]["violations"])))
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
    out.append("  of the %d PERSISTS rows, %d are FORCED and %d contingent"
               % (S["persistence_forcing"]["persist_rows"],
                  S["persistence_forcing"]["forced"],
                  S["persistence_forcing"]["contingent"]))
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
        # MINOR-13, repaired: the flag a reviewer is invited to use now runs
        # the SAME final coverage pass the delivery path runs, so it is not
        # strictly weaker than the path it stands in for.
        S["gates"] = LD.rows
        S["gate_digests"] = LD.digests
        cov2 = paper_coverage_only(S, paper_text)
        ok = (cov2["unlicensed"] == 0 and cov2["polarity_failures"] == 0
              and cov2["missing"] == 0 and cov2["table_missing"] == 0
              and cov2["fenced_multiset_equal"])
        say("")
        say("VERIFY-PAPER: %s" % paper_rel)
        say("  coverage %s" % cov)
        say("  final pass %s" % cov2)
        if not ok:
            say("")
            say("GATE FAILED: G-PAPER-COVERAGE-FINAL :: the final pass does "
                "not close on %s" % paper_rel)
            say("EXIT 1")
            sys.exit(1)
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
    for nm, target, effect, note in MUTANTS:
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
        report.append({"mutant": nm, "target": target, "effect": effect,
                       "note": note, "killed": killed_at is not None,
                       "killed_at": killed_at,
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
    S["mutants"] = report
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
        # A FAILING RUN WRITES NOTHING -- including on this path.  The
        # pre-existing artifacts are copied aside before `os.replace` and
        # restored if the post-write check fires, so a corrupt artifact is
        # never left promoted.
        prior = {}
        for p in (OUT_JSON, OUT_TXT):
            if os.path.exists(p):
                with open(p, "rb") as f:
                    prior[p] = f.read()
        os.replace(tj, OUT_JSON)
        os.replace(tt, OUT_TXT)
        why = against_the_seal(read_text(OUT_JSON), read_text(OUT_TXT))
        if why is not None:
            for p, blob in prior.items():
                with open(p, "wb") as f:
                    f.write(blob)
            for p in (OUT_JSON, OUT_TXT):
                if p not in prior and os.path.exists(p):
                    os.remove(p)
            print("GATE FAILED: G-ARTIFACT-INTEGRITY :: the artifacts on disk "
                  "differ from the gate-time seal (%s); the previous "
                  "artifacts have been restored and nothing of this run "
                  "remains on disk" % why, flush=True)
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
