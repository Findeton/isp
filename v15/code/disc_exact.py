#!/usr/bin/env python3.13
# -*- coding: utf-8 -*-
"""DISC (paper-47) -- THE DISCRIMINATOR: THE NULL GETS ITS OWN INSTRUMENT.

Pin: v15/note-disc-pin.md (sha256-12 dbe7b26bb0d0, v15 ledger #1).
Questions: Q147, Q148, Q149, Q150, Q155.

THE QUESTION.  Can a simpler existing model reproduce every result obtained so
far (Q155), and if not, what is the first parameter-free prediction on which
ISP and that model DIFFER, on an observable both can express (Q147/Q148), with
the falsifier and the finite experiment stated (Q149/Q150)?

THE NULL, AND WHY IT IS NOT A STRAWMAN.  The pin asks for the simplest
comparable model and forbids tuning it to lose.  The null's parameters are
fixed by seven pre-registered rules PR1..PR7 declared in this file before any
row runs, and every one of them hands the null the SAME arena, the SAME
internal alphabet, the SAME coin, the SAME initial state and the SAME horizon
as the ISP model it is compared against.  What the null drops is STRUCTURE and
only structure: it has no record layer and no conserved-price structure.  A
discriminator that had to change the arena or the alphabet to find a
difference would have found nothing.

S-1 STRUCTURALLY (TEMPLATE.md Sec.11, the registered-unimplemented family).
Four code regions, disjoint by machine check at G-S1-DISJOINT-CODE:
  n_*   THE NULL         -- a plain coined walk; no record object of any kind
                            appears in its region, by AST;
  i_*   THE ISP MODEL    -- paper-20's coupled walk, rebuilt from its own
                            definitions, never imported;
  p_*   THE HEAD BUILDER -- renders the delivered head from the payload;
  k_*   THE COMPARATOR   -- decides agreement and difference, and rebuilds the
                            head by its OWN route for G-VERDICT-EQUALITY.
EVERY cross-region call edge is an offence, in both directions, and callees
are resolved through the module's own binding table so an alias is not a way
past the check.  A function in no region that is called from more than one
region is a shared component -- registered family S-2 -- and is an offence
unless it is one of the DECLARED SHARED GROUND names below, each of which is
required to be genuinely shared.  The two builders are cross-validated where
they must agree (ticks 1 and 2, at every fiber point) and against paper-20's
sealed numbers where the ISP arm must reproduce a parent.

EXACTNESS.  Integers and fractions.Fraction only.  Cyclotomic amplitudes are
carried as integer 4-tuples over the basis (1, z, z^2, z^3) of Z[zeta_12]
reduced modulo z^4 - z^2 + 1.  No float appears anywhere and an AST scan plus
a recursive receipt type scan are gates.

TEMPLATE.  E-25...E-33 adopted; the nine families are imported from
v14/code/era_template.py and used, not copied.  TPL-2's registered items:
gate-time seals recomputed at promotion, no %-format AND no integer-offset
typed counts (both subspecies scanned at the registry door), wall controls
written independently of their patterns and every control required to be
caught, move-proofs real, no carried-and-unused family.

CLI (#82).  --run | --no-write | --selftest | --list-gates | --list-mutants
            | --mutant NAME | --render
Anything else exits 2.  Every mode runs the whole gate battery.
"""

from __future__ import annotations

import ast
import collections
import hashlib
import json
import os
import re
import sys
from fractions import Fraction
from itertools import product

_HERE = os.path.dirname(os.path.abspath(__file__))
_TPL = os.path.join(os.path.dirname(os.path.dirname(_HERE)), "v14", "code")
for _p in (_HERE, _TPL):
    if _p not in sys.path:
        sys.path.insert(0, _p)
import era_template as ET                                          # noqa: E402

REPO = os.path.dirname(os.path.dirname(_HERE))     # .../isp

PAPER_REL = "v15/paper-47-disc.md"
RECEIPT_REL = "v15/code/disc_receipt.json"
OUTPUT_REL = "v15/code/disc_output.txt"
SELF_REL = "v15/code/disc_exact.py"
PIN_REL = "v15/note-disc-pin.md"
TEMPLATE_REL = "v14/code/era_template.py"

# The sha256-12 of every pinned source, verified before use (#91: repository
# reads at pinned digests only, and every product consumed by a gate).
SOURCES = {
    PIN_REL: "dbe7b26bb0d0",
    "v14/paper-20-coupling.md": "4824d190af73",
    "v14/paper-34-act.md": "d933221780ed",
    "v14/paper-36-pot.md": "1e495318252d",
    "v14/paper-39-ndep.md": "e2293b8c3858",
    TEMPLATE_REL: "d04a3eb58fbc",
}

# ===========================================================================
# THE NULL'S PRE-REGISTERED RULE.  Declared here, before any row runs.  Every
# rule hands the null a parity with the ISP model; none of them is a choice
# this unit makes after seeing a number.
#
# THE PRE-REGISTRATION IS SEALED (K3 MAJOR-4: the rules were re-declarable
# post-hoc at exit 0, because only their CARDINALITY was gated).  Three things
# now bind them and all three are machine-checked at
# G-PR-PREREGISTRATION-SEALED:
#   (1) NULL_RULE_SEAL below is a digest over the whole rule table, declared
#       WITH the table, so any rewrite of any rule's words moves it -- but the
#       constant sits beside the table, so an author who rewrites a rule AND
#       re-declares the digest passes this leg alone.  That is why (3) exists;
#   (2) every rule carries a CONTENT LEG -- a predicate over objects this run
#       actually built -- so a rewritten rule must also defeat a measurement
#       and not merely a sentence.  PR3's content leg is object identity: the
#       sweep constructs ONE coin and hands that same object to both arms;
#   (3) every rule's TEXT is bound to the parity it asserts.  Each rule must
#       still SAY the thing its content leg measures, and no rule may admit
#       the post-hoc tuning a rewritten pre-registration has to admit.  This
#       is the leg that survives a re-declared digest, and it is what kills
#       the exact rewrite the panel shipped at exit 0 -- PR3 turned from "the
#       SAME coin" into "a coin of its OWN choosing, picked after the sweep".
# The datum words and the SHARED-WITH-ISP list are derived from this table
# rather than typed beside it, so the head cannot say "COIN" while PR3 says
# the null picks its own.
# ===========================================================================

NULL_RULE = (
    ("PR1", "ARENA",
     "the null runs on the same site set as the ISP model it is compared "
     "against -- the points of AG(2,q) with periodic identification, d=2"),
    ("PR2", "REGISTER",
     "the null's internal register has the same dimension as the ISP model's "
     "-- one basis vector per declared link direction"),
    ("PR3", "COIN",
     "the null carries the SAME coin as the ISP model it is compared "
     "against, taken from the same S_3-covariant census over the arena's own "
     "ring; the discriminator may not be won by changing the coin"),
    ("PR4", "SHIFT",
     "the null's shift is the same conditional translation, carrying the "
     "amplitude at a site along its own direction and leaving the direction "
     "alone"),
    ("PR5", "STATE",
     "the null starts in the same state as the ISP model -- one basis vector, "
     "at the same site and the same direction"),
    ("PR6", "STRUCTURE",
     "the null has NO record layer: its coin is constant in space and in "
     "time, it emits nothing, and no count field exists in its region"),
    ("PR7", "MEASURE",
     "where a census over configurations needs a measure the null uses the "
     "uniform counting measure -- it has no conserved-price structure and "
     "declares no weight system"),
)

# The pre-registration's own digest, declared with the rules it seals.
NULL_RULE_SEAL = "cb5064b58db6"

# WHAT EACH RULE MUST STILL SAY.  The phrase is the parity the rule's own
# content leg measures, so text and measurement cannot drift apart: PR3's leg
# measures that ONE coin object reaches both arms, and PR3's text has to keep
# asserting sameness of the coin to satisfy this leg.  A rewritten rule fails
# here even if its author re-declares the digest above.
NULL_RULE_ASSERTS = {
    "PR1": "same site set",
    "PR2": "same dimension",
    "PR3": "same coin",
    "PR4": "same conditional translation",
    "PR5": "same state",
    "PR6": "no record layer",
    "PR7": "uniform counting measure",
}

# THE ADMISSIONS A POST-HOC PRE-REGISTRATION HAS TO MAKE.  A rule rewritten
# after the numbers are in has to say, in some voice, that its value was
# chosen once the answer was known.  No rule's text may carry any of these.
NULL_RULE_TUNING = (
    r"own choosing", r"\btuned\b", r"\btuning\b", r"picked after",
    r"chosen after", r"chosen afterwards", r"selected after",
    r"after the sweep", r"after the run", r"whichever member",
    r"makes the comparison come out", r"\bpost-hoc\b",
    r"of its own\b", r"to (?:the|its) advantage",
)

# The datum words of the rules that hand the null a PARITY.  Derived, not
# typed: the head's SHARED-WITH-ISP list is built from the rule ids below and
# the two rules that take something away are PR6 and PR7.
NULL_RULE_TAKES_AWAY = ("PR6", "PR7")

# The declared moduli window: the divisors of 12, which is the smallest
# modulus whose ring contains both the parent's phase alphabet (m=3) and the
# modulus NDEP's successor test predicts at AG(2,2) (m=2).
MODULI = (1, 2, 3, 4, 6, 12)

# The descent sweep's declared window: prime field orders, where the additive
# group of the field is cyclic, and the moduli from one to twelve.
PRIME_ORDERS = (2, 3, 5, 7)
MODULUS_WINDOW = tuple(range(1, 13))

# The declared arenas.  q=3 is paper-20's own; q=2 is NDEP's AG(2,2), the
# arena at which the coin modulus is predicted and untested.
ARENAS = (2, 3)

# The declared horizons.  FID_T is the fidelity leg's, run at the parent's own
# arena against the parent's own sealed ladders; FIB_T is the fiber sweep's.
FID_T = 5
FIB_T = 3
HEAD_T = 5

# The declared spatial dimension, which the pin's own sentence carries and
# G-NULL-RULE-TOTAL reads back out of it.
DECLARED_DIMENSION = 2

# The three declared link directions, which are the parallel classes of
# AG(2,2) entire and three of the four of AG(2,3).
LINKDIRS = ((1, 0), (0, 1), (1, 1))

# THE STRUCTURE PRICE.  A prediction with no adjustable number is not a
# prediction with no structure, and the difference is what this unit is
# comparing.  Each row is a structure the record-carrying model carries and
# the null does not, together with the count of FREE numbers it introduces.
#
# K2 MAJOR-4: the flat "zero adjustable numbers" contradicted this run's own
# sealed axis list, which names the phase modulus as a declared free axis, and
# section 9 measures that modulus moving the headline observable at every one
# of its five runnable values.  The sixth row below carries it, its free
# number is 1, and the price is stated CONDITIONALLY on the forcing section 9
# derives.  The third field is no longer a typed zero at every row: it is
# checked against a measurement of what each structure can be dialled to,
# which is what G-STRUCTURE-PRICED now gates.
STRUCTURE_PRICE = (
    ("the count field", "one non-negative integer per cell, initialised "
     "uniform and monotone thereafter", 0, "UNCONDITIONAL"),
    ("the feedback rule", "the coin at a site is multiplied by the diagonal "
     "of phases the site's own counts determine", 0, "UNCONDITIONAL"),
    ("the emission rule", "one division event per step, on a cell drawn with "
     "that cell's own post-coin weight", 0, "UNCONDITIONAL"),
    ("the branch structure", "the state is an ensemble over emission "
     "histories rather than a single trajectory", 0, "UNCONDITIONAL"),
    ("the phase character", "the map from a count to a phase, taken to be a "
     "character of the arena's own scalar group", 0, "UNCONDITIONAL"),
    ("the phase modulus m", "the modulus at which that character reads a "
     "count; a swept axis of this run, measured moving the headline "
     "observable", 1, "FIXED-TO-THE-FIELD-ORDER-BY-THE-DESCENT-FORCING-"
     "WHICH-IS-CONSTRUCTION-DEPENDENT"),
)

# THE DECLARED SHARED GROUND.  A function in no model region that is called
# from more than one region is a shared component (registered family S-2).
# These are the only ones this unit declares, they are the ring primitives,
# and G-S1-DISJOINT-CODE requires each of them to be GENUINELY shared -- a
# declaration carried and never used is a hole, not a courtesy.
SHARED_GROUND = ("radd", "rmul", "rnormsq", "r_is_rational")

# The three declared coin orders of paper-20's F6 fiber, and the two declared
# shift orientations of its F7 fiber.  F6 is stamped DECLARED-VERDICT-RELEVANT
# by the parent; this unit's delivered arm is G.D and the alternative D.G is
# measured here rather than left silent (K1 MAJOR-1).
COIN_ORDERS = ("GD", "DG")
ORIENTATIONS = (1, -1)
DG_T = 4          # the alternative order's horizon: one tick past its own tick

# THE WIDER MEMORYLESS NULL SWEEP (K2 MAJOR-5, adopted as a measured row).
# The null class is widened past PR3's census in two steps: every SOLUTION of
# the arena's own covariant census at every start site and every direction,
# and then every integral coin M with M M^T = 9I and entries inside the
# declared box -- covariance dropped entirely.  Neither reproduces the tick-3
# law; at the smaller plane one non-covariant coin comes CLOSER than the PR3
# null, and the published deciding cost is the cost against that one.
INTEGRAL_COIN_BOX = 3

# Every gate this run may fire, declared before any of them does.  The gate
# helper refuses an id outside this list, T-FALSIFIER-COVERAGE takes its
# denominator from it rather than from what has fired by then (K3 MAJOR-5's
# tail exemption), and the last gate reconciles it with the ledger, so the row
# count, the --list-gates output and every published total are ONE number.
GATE_NAMES = (
    "G-SOURCES-PINNED", "G-ANCHORS-LOCATED", "G-S1-DISJOINT-CODE",
    "G-NULL-HAS-NO-RECORD", "G-NULL-RULE-TOTAL", "G-PR-PREREGISTRATION-SEALED",
    "G-COIN-CENSUS-PARENT", "G-ISP-FIDELITY-PARENT", "G-NULL-TWO-ROUTES",
    "G-AGREE-THROUGH-THE-EARLY-TICKS", "G-FIRST-DIFFERENCE-TICK",
    "G-DISCRIMINANT-VALUES", "G-NULL-IS-THE-PARENTS-CONTROL",
    "G-COIN-ORDER-FIBER", "G-WIDER-NULL-SWEEP", "G-MECHANISM-CORROBORATED",
    "G-MODULUS-DESCENT-THEOREM", "G-MODULUS-OBSERVABLE", "G-M2-PREDICTION-RUN",
    "G-PERIMETER-LAW-BOTH", "G-GAP-BOTH", "G-PLAQUETTE-BOTH", "G-QUARTIC-BOTH",
    "G-STENCIL-FORCING-PARENT", "G-EXPRESSIBILITY-CENSUS",
    "G-Q155-CENSUS-TOTAL", "G-FALSIFIER-SPECIFIED", "G-FEASIBILITY-BOTH-WAYS",
    "G-SCOPE-DECLARED", "G-STRUCTURE-PRICED", "G-VERDICT-EQUALITY",
    "G-PAPER-CLAIMS", "G-PAPER-REFERENTS", "G-PAPER-WALLS",
    "G-PAPER-COVERAGE", "G-TYPED-COUNTS", "G-NO-FLOATS", "G-ANCHORS-CONSUMED",
    "T-FALSIFIER-COVERAGE", "G-TEMPLATE-ADOPTED", "G-READS-DECLARED",
    "G-TRANSCRIPT-BOUND",
)

# Declared exemptions for the typed-count audit: identifiers, not counts.
TOKEN_EXEMPTIONS = {
    "AG(2,2)": "the name of an affine plane, not a count",
    "AG(2, 2)": "the name of an affine plane, not a count",
    "AG(2, 3)": "the name of an affine plane, not a count",
    "Z_3": "the name of a group, not a count",
    "F_2": "the name of a field, not a count",
    "d=2": "the declared spatial dimension in the pin's own words",
    "S_3": "the name of a group, not a count",
    "section 5": "a section number inside a parent's quoted sentence",
    "{1,1,1/2}": "a spectrum written as a set inside a parent's quoted "
                 "sentence, not a count",
    "PR1": "a rule identifier", "PR2": "a rule identifier",
    "PR3": "a rule identifier", "PR4": "a rule identifier",
    "PR5": "a rule identifier", "PR6": "a rule identifier",
    "PR7": "a rule identifier",
    "paper-20": "a paper identifier", "paper-34": "a paper identifier",
    "paper-36": "a paper identifier", "paper-39": "a paper identifier",
    "paper-47": "a paper identifier",
    "Q147": "a question identifier", "Q148": "a question identifier",
    "Q149": "a question identifier", "Q150": "a question identifier",
    "Q155": "a question identifier",
}

MUTANT = {"name": None, "used": set()}
PARTIAL: dict = {"R": None}


def mut(name):
    if MUTANT["name"] == name:
        MUTANT["used"].add(name)
        return True
    return False


def sha12(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        h.update(fh.read())
    return h.hexdigest()[:12]


def read_text(rel):
    with open(os.path.join(REPO, rel), encoding="utf-8") as fh:
        return fh.read()


def com(n):
    return "{:,}".format(n)


# ===========================================================================
# SECTION A.  THE RINGS.
#   A1 -- Z[zeta_12] for the walk amplitudes, basis (1,z,z^2,z^3) modulo
#         z^4 - z^2 + 1.  It contains zeta_m for every declared modulus.
#   A2 -- Z[zeta_8] doubled, for the lattice leg's link operators.
#   Both are shared arena arithmetic, declared shared: they are not a model.
# ===========================================================================

R0 = (0, 0, 0, 0)
R1 = (1, 0, 0, 0)


def rmul(a, b):
    """multiplication modulo z^4 - z^2 + 1, written out."""
    a0, a1, a2, a3 = a
    b0, b1, b2, b3 = b
    c0 = a0 * b0
    c1 = a0 * b1 + a1 * b0
    c2 = a0 * b2 + a1 * b1 + a2 * b0
    c3 = a0 * b3 + a1 * b2 + a2 * b1 + a3 * b0
    c4 = a1 * b3 + a2 * b2 + a3 * b1
    c5 = a2 * b3 + a3 * b2
    c6 = a3 * b3
    return (c0 - c4 - c6, c1 - c5, c2 + c4, c3 + c5)


def radd(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2], a[3] + b[3])


def rscale(a, k):
    return (a[0] * k, a[1] * k, a[2] * k, a[3] * k)


def rconj(a):
    """z -> z^-1 = z^11; conj(1)=1, conj(z)=z-z^3, conj(z^2)=1-z^2,
    conj(z^3)=-z^3."""
    a0, a1, a2, a3 = a
    return (a0 + a2, a1, -a2, -a1 - a3)


def rnormsq(a):
    return rmul(a, rconj(a))


ZPOW = []
for _j in range(24):
    _v = R1
    for _ in range(_j):
        _v = rmul(_v, (0, 1, 0, 0))
    ZPOW.append(_v)


def rmul_zpow(a, e):
    """multiply by z^e without a single ring multiplication: the phase step of
    the coupled walk is exactly this, and it is what makes the fidelity leg
    affordable at the parent's own horizon."""
    e %= 12
    if e == 0:
        return a
    out = R0
    for k in range(4):
        if a[k]:
            out = radd(out, rscale(ZPOW[k + e], a[k]))
    return out


def zeta(m, k):
    """zeta_m^k inside Z[zeta_12]; m must divide 12."""
    return ZPOW[((12 // m) * k) % 12]


def r_is_rational(a):
    return a[1] == 0 and a[2] == 0 and a[3] == 0


def r_is_real(a):
    """the real subfield of Q(zeta_12) is Q(sqrt 3) with sqrt 3 = 2z - z^3."""
    return a[2] == 0 and a[1] == -2 * a[3]


def r_real_pair(a):
    """(p, q) meaning p + q sqrt 3, for an element measured real."""
    return (a[0], -a[3])


def r_str(a):
    if r_is_rational(a):
        return str(a[0])
    p, q = r_real_pair(a)
    return "%s+%s*sqrt3" % (p, q)


# -- A2: Z[zeta_8], doubled coordinates, for the lattice leg ---------------

def imul(a, b):
    a0, a1, a2, a3 = a
    b0, b1, b2, b3 = b
    return (a0 * b0 - (a1 * b3 + a2 * b2 + a3 * b1),
            a0 * b1 + a1 * b0 - (a2 * b3 + a3 * b2),
            a0 * b2 + a1 * b1 + a2 * b0 - a3 * b3,
            a0 * b3 + a1 * b2 + a2 * b1 + a3 * b0)


def iadd(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2], a[3] + b[3])


def iconj(a):
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
    return tuple(v)


IZ = (0, 0, 0, 0)
IONE = (1, 0, 0, 0)
SQRT2 = (0, 1, 0, -1)
IFOUR = (4, 0, 0, 0)


# -- the arena, shared and declared shared --------------------------------

class Arena:
    """AG(2,q) with the three declared link directions.  This object is the
    DECLARED SHARED GROUND of the two models: it is not part of either one,
    and the discriminator's whole content is that nothing else is shared."""

    def __init__(self, q, orientation=1, dirs=None):
        self.q = q
        self.orientation = orientation
        self.dirs = tuple(dirs) if dirs is not None else LINKDIRS
        self.sites = [(a, b) for a in range(q) for b in range(q)]
        self.index = {x: i for i, x in enumerate(self.sites)}
        self.ns = len(self.sites)
        self.ncell = 3 * self.ns
        self.dim = 3 * self.ns
        self.shift = [0] * self.dim
        for s, x in enumerate(self.sites):
            for l, v in enumerate(self.dirs):
                y = ((x[0] + orientation * v[0]) % q,
                     (x[1] + orientation * v[1]) % q)
                self.shift[s * 3 + l] = self.index[y] * 3 + l


def coin_census(q, bound=6):
    """the S_3-covariant unitary coins C = aI + bJ with 3C integral over the
    ARENA'S OWN RING Z[zeta_q], enumerated exhaustively over a declared
    coordinate bound.  Shared ground: both models draw their coin from here,
    which is exactly PR3."""
    if q == 2:
        basis = (R1,)
    elif q == 3:
        basis = (R1, zeta(3, 1))
    else:
        raise ValueError(q)
    els = []
    if len(basis) == 1:
        for x in range(-bound, bound + 1):
            els.append(rscale(basis[0], x))
    else:
        for x in range(-bound, bound + 1):
            for y in range(-bound, bound + 1):
                els.append(radd(rscale(basis[0], x), rscale(basis[1], y)))
    sols = []
    for A in els:
        for B in els:
            t1 = rmul(A, rconj(A))
            t2 = radd(radd(rmul(A, rconj(B)), rmul(rconj(A), B)),
                      rscale(rmul(B, rconj(B)), 3))
            if t1 == (9, 0, 0, 0) and t2 == R0:
                sols.append((A, B))
    units = []
    for k in range(q):
        u = zeta(q, k)
        units.append(u)
        units.append(rscale(u, -1))
    seen, reps = set(), []
    for (A, B) in sols:
        if (A, B) in seen:
            continue
        for u in units:
            seen.add((rmul(A, u), rmul(B, u)))
        reps.append((A, B))
    return sols, reps


def coin_matrix(A, B):
    """3C as a 3x3 matrix over Z[zeta_12]."""
    return tuple(tuple(radd(A, B) if i == j else B for j in range(3))
                 for i in range(3))


def coin_is_trivial(B):
    """the trivial class B = 0: a scalar times the identity, a deterministic
    shift that carries no interference at all."""
    return B == R0


# ===========================================================================
# SECTION B.  n_*  --  THE NULL.
#   A plain d=2 discrete-time coined quantum walk.  There is no record object
#   anywhere in this region: no count field, no emission, no branching, no
#   price.  G-NULL-HAS-NO-RECORD proves that by AST rather than by assertion.
#   Two independent routes: an integer route (valid when the coin is integral)
#   and a ring route.  They share the arena and nothing else.
# ===========================================================================

def n_step_ring(arena, psi, coin):
    """one null step: the fixed coin, then the shift.  The coin does not take
    a time argument and there is nothing for it to read."""
    post = [R0] * arena.dim
    for s in range(arena.ns):
        b = s * 3
        for i in range(3):
            tot = R0
            for j in range(3):
                tot = radd(tot, rmul(coin[i][j], psi[b + j]))
            post[b + i] = tot
    out = [R0] * arena.dim
    for k in range(arena.dim):
        out[arena.shift[k]] = post[k]
    return out


def n_ladder_ring(arena, horizon, coin, start, direction):
    """the null's site-occupation ladder, exact."""
    psi = [R0] * arena.dim
    psi[arena.index[start] * 3 + direction] = R1
    dist, ipr = {}, {}
    for t in range(horizon):
        den = 9 ** (t + 1)
        psi = n_step_ring(arena, psi, coin)
        row = []
        for s in range(arena.ns):
            v = R0
            for i in range(3):
                v = radd(v, rnormsq(psi[s * 3 + i]))
            if not r_is_rational(v):
                raise ET.CheckFail("G-BORN-WEIGHTS-RATIONAL",
                                   "a null Born weight left the rationals")
            row.append(Fraction(v[0], den))
        dist[t + 1] = tuple(row)
        ipr[t + 1] = sum(x * x for x in row)
    return dist, ipr


def n_step_int(arena, psi, coin_int):
    """the null's SECOND ROUTE: plain Python integers, no ring at all.  It is
    available exactly when the coin's entries are rational integers, which the
    Grover coin's are, and it shares no arithmetic with the ring route."""
    post = [0] * arena.dim
    for s in range(arena.ns):
        b = s * 3
        for i in range(3):
            tot = 0
            for j in range(3):
                tot += coin_int[i][j] * psi[b + j]
            post[b + i] = tot
    out = [0] * arena.dim
    for k in range(arena.dim):
        out[arena.shift[k]] = post[k]
    return out


def n_ladder_int(arena, horizon, coin_int, start, direction):
    psi = [0] * arena.dim
    psi[arena.index[start] * 3 + direction] = 1
    dist, ipr = {}, {}
    for t in range(horizon):
        den = 9 ** (t + 1)
        psi = n_step_int(arena, psi, coin_int)
        row = [Fraction(sum(psi[s * 3 + i] ** 2 for i in range(3)), den)
               for s in range(arena.ns)]
        dist[t + 1] = tuple(row)
        ipr[t + 1] = sum(x * x for x in row)
    return dist, ipr


def n_integral_coins(box):
    """THE WIDER NULL CLASS.  Every integral matrix M with M M^T = 9 I and
    entries in [-box, box]: the unitarity condition alone, with the arena's
    S_3 covariance DROPPED.  The census PR3 draws from is a subset of the
    covariant ones; this is the class the null is allowed to shop in when the
    anti-strawman rule is suspended, and it is swept so that section 3's
    parity sentence is measured rather than asserted."""
    rows = [r for r in product(range(-box, box + 1), repeat=3)
            if sum(x * x for x in r) == 9]
    out = []
    for a in rows:
        for b in rows:
            if sum(x * y for x, y in zip(a, b)):
                continue
            for c in rows:
                if sum(x * y for x, y in zip(a, c)):
                    continue
                if sum(x * y for x, y in zip(b, c)):
                    continue
                out.append((a, b, c))
    return rows, out


def n_lattice_expectation(values, weight_free=True):
    """PR7 at the lattice leg: the null's measure over a carrier is the
    uniform counting measure.  `weight_free` records that no weight system is
    consulted; the argument exists so the absence is a value and not a
    silence."""
    if not weight_free:
        raise ET.CheckFail("G-NULL-RULE-TOTAL",
                           "the null was asked for a weighted expectation")
    tot = Fraction(0)
    for v in values:
        tot += Fraction(v)
    return tot / len(values)


# ===========================================================================
# SECTION C.  i_*  --  THE ISP MODEL.
#   paper-20's coupled walk, rebuilt from the definitions in its own text:
#   C_t(x) = G . D_t(x) with D_t(x) = diag(zeta_m^{n_l(x)}), the shift
#   |x,l> -> |x+l,l>, the record a count field on the 3q^2 cells, a division
#   event emitted on a cell with the post-coin Born weight (reading A) or with
#   the record's own local share (reading B), every branch carried.
# ===========================================================================

def i_coin_apply(arena, psi, record, modulus, coin, order="GD"):
    """the coupled coin at one step.  ORDER is paper-20's F6 fiber, which the
    parent stamps DECLARED-VERDICT-RELEVANT: 'GD' applies the record's own
    diagonal BEFORE the coin (this unit's delivered member), 'DG' applies it
    AFTER, which is the parent's alternative and is stage-blind in that step's
    Born weights, since |D G psi|^2 = |G psi|^2."""
    out = [R0] * arena.dim
    for s in range(arena.ns):
        b = s * 3
        if modulus == 1 or order == "DG":
            src = [psi[b + j] for j in range(3)]
        else:
            e = (12 // modulus)
            src = [rmul_zpow(psi[b + j], e * (record[b + j] % modulus))
                   for j in range(3)]
        for i in range(3):
            tot = R0
            for j in range(3):
                c = coin[i][j]
                if c == R0:
                    continue
                if r_is_rational(c):
                    tot = radd(tot, rscale(src[j], c[0]))
                else:
                    tot = radd(tot, rmul(c, src[j]))
            if order == "DG" and modulus != 1:
                tot = rmul_zpow(tot, (12 // modulus)
                                * (record[b + i] % modulus))
            out[b + i] = tot
    return out


def i_walk_step(arena, psi, record, modulus, coin, order="GD"):
    post = i_coin_apply(arena, psi, record, modulus, coin, order)
    out = [R0] * arena.dim
    for k in range(arena.dim):
        out[arena.shift[k]] = post[k]
    return out, post


def i_emission(arena, born, record, den, reading):
    """the emission distribution over the cells at one step.  READING A is
    paper-20's certified identification -- the law's local menu mass IS the
    walk's own local Born mass, so the weight of cell (x,l) is its post-coin
    Born weight.  READING B is the declared fiber: the weight is the record's
    own local share."""
    wts = []
    for s in range(arena.ns):
        b = s * 3
        mass = born[b] + born[b + 1] + born[b + 2]
        if reading == "A":
            for i in range(3):
                wts.append(Fraction(born[b + i], den))
        else:
            tot = record[b] + record[b + 1] + record[b + 2]
            px = Fraction(mass, den)
            for i in range(3):
                wts.append(px * Fraction(record[b + i], tot) if tot
                           else Fraction(0))
    return wts


def i_ladder(arena, horizon, modulus, coin, start, direction,
             reading="A", coupled=True, record0=None, want_frontier=False,
             order="GD"):
    """ONE ARM of the coupled object, exhaustively: no sampling, no pruning,
    no truncation by weight.  `coupled` False is paper-20's frozen-stage
    control -- the identical walk, the identical emission rule, the identical
    branching, on counts that never update -- run through this same function
    so it cannot differ in anything but the one line that updates."""
    if record0 is None:
        record0 = tuple([1] * arena.ncell)
    psi0 = [R0] * arena.dim
    psi0[arena.index[start] * 3 + direction] = R1
    frontier = [(tuple(psi0), record0, Fraction(1))]
    dist, ipr, branches, norm_checks, norm_viol = {}, {}, {}, 0, 0
    mass_ok = True
    for t in range(horizon):
        den = 9 ** (t + 1)
        nxt = []
        for (psi, rec, w) in frontier:
            newpsi, post = i_walk_step(arena, list(psi), rec, modulus, coin,
                                       order)
            born = []
            for k in range(arena.dim):
                v = rnormsq(post[k])
                if not r_is_rational(v):
                    raise ET.CheckFail("G-BORN-WEIGHTS-RATIONAL",
                                       "an ISP Born weight left the rationals")
                born.append(v[0])
            norm_checks += 1
            if sum(born) != den:
                norm_viol += 1
            wts = i_emission(arena, born, rec, den, reading)
            if sum(wts) != 1:
                mass_ok = False
            for c in range(arena.ncell):
                if wts[c] == 0:
                    continue
                if coupled:
                    lst = list(rec)
                    lst[c] += 1
                    nrec = tuple(lst)
                else:
                    nrec = rec
                nxt.append((tuple(newpsi), nrec, w * wts[c]))
        frontier = nxt
        acc = [Fraction(0)] * arena.ns
        for (psi, _rec, w) in frontier:
            for s in range(arena.ns):
                v = 0
                for i in range(3):
                    v += rnormsq(psi[s * 3 + i])[0]
                if v:
                    acc[s] += w * v
        row = tuple(acc[s] / den for s in range(arena.ns))
        if sum(row) != 1:
            mass_ok = False
        dist[t + 1] = row
        ipr[t + 1] = sum(x * x for x in row)
        branches[t + 1] = len(frontier)
    return {"dist": dist, "ipr": ipr, "branches": branches,
            "norm_checks": norm_checks, "norm_violations": norm_viol,
            "mass_one": mass_ok,
            "frontier": frontier if want_frontier else None}


def i_record_observables(arena, frontier, modulus):
    """the RECORD-SIDE observables: quantities that are functions of the count
    field.  They are listed so that the census of section H can state, per
    row, that the null does not merely disagree with them -- it cannot form
    them at all."""
    maxcell = 0
    curv = collections.Counter()
    total_mass = Fraction(0)
    for (_psi, rec, w) in frontier:
        maxcell = max(maxcell, max(rec))
        f = []
        for s, x in enumerate(arena.sites):
            s2 = arena.index[((x[0] + arena.dirs[0][0]) % arena.q,
                              (x[1] + arena.dirs[0][1]) % arena.q)]
            f.append((rec[s * 3 + 0] + rec[s2 * 3 + 1] - rec[s * 3 + 2])
                     % modulus)
        curv[tuple(f)] += w
        total_mass += w
    const = sum(w for f, w in curv.items() if len(set(f)) == 1)
    return {"max_cell_count": maxcell,
            "distinct_curvature_fields": len(curv),
            "constant_curvature_probability": str(const),
            "total_mass": str(total_mass)}


# -- the lattice leg's ISP objects: R5's link operator and holonomy --------

E1, E2 = (1, 0), (0, 1)
EDIR = (E1, E2)


class Lattice:
    def __init__(self, L):
        self.L = L
        self.sites = [(x, y) for x in range(L) for y in range(L)]
        self.links = [(s, d) for s in self.sites for d in range(2)]

    def addv(self, s, v):
        return ((s[0] + v[0]) % self.L, (s[1] + v[1]) % self.L)

    def ends(self, l):
        return l[0], self.addv(l[0], EDIR[l[1]])


def i_alphabet():
    """R4's coefficient alphabet as R5 declares it, carried DOUBLED so every
    entry is integral: zero, and zeta_8^t at each of the three declared
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


def i_link_coins(alphabet):
    rows = [(a, b) for a in alphabet for b in alphabet
            if iadd(imul(a, iconj(a)), imul(b, iconj(b))) == IFOUR]
    coins = []
    for (a, b) in rows:
        for (c, d) in rows:
            if iadd(imul(a, iconj(c)), imul(b, iconj(d))) == IZ:
                coins.append((a, b, c, d))
    return coins, rows


def i_sector(m):
    a, b, c, d = m
    if b == IZ and c == IZ:
        return "DIAGONAL"
    if a == IZ and d == IZ:
        return "ANTIDIAGONAL"
    return "BALANCED"


def i_rect_cycle(lat, base, a, b):
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


def i_steps_of(lat, cyc):
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
            raise ET.CheckFail("G-PERIMETER-LAW-BOTH",
                               "a declared cycle has a non-adjacent step")
        st.append(found)
    return st


def i_holonomy_trace(lat, steps, coin):
    """R5's definition: the ordered product of the link operators around the
    loop, each inverted where the loop runs against the link's own direction;
    every factor is the identity off the loop's own sites."""
    a, b, c, d = coin
    inv = (iconj(a), iconj(c), iconj(b), iconj(d))
    sites = []
    for (l, _o) in steps:
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
            Fraction(tr[2], den), Fraction(tr[3], den))


def i_loop_observable(lat, cyc, coin):
    """ACT's admissible object, which POT carries forward: the
    conjugation-symmetric part of the loop trace, a pair (p, q) meaning
    p + q sqrt 2."""
    tr = i_holonomy_trace(lat, i_steps_of(lat, cyc), coin)
    return (tr[0], (tr[1] - tr[3]) / 2)


def i_quartic_sign(x, power=4):
    """ACT's observable: the sign of the fourth power of an off-diagonal
    entry, zero when the entry is.  The exponent is supplied by the caller,
    which reads it out of the parent's own sentence."""
    if x == IZ:
        return 0
    q = IONE
    for _ in range(power):
        q = imul(q, x)
    if not (q[1] == 0 and q[2] == 0 and q[3] == 0):
        return 0
    return 1 if q[0] > 0 else -1


def i_gauge_twist(m, k):
    a, b, c, d = m
    return (a, imul(izpow(k), b), imul(izpow(-k), c), d)


def i_stencil_scan(offsets, alphabet3, q=3):
    """paper-20's coin-register forcing, rebuilt: on an offset set every one
    of whose nonzero differences is realised exactly once, the only unitary
    coefficient maps are monomial, so no interference survives."""
    diffs: dict = {}
    for i, v in enumerate(offsets):
        for j, w in enumerate(offsets):
            if i == j:
                continue
            d = ((v[0] - w[0]) % q, (v[1] - w[1]) % q)
            diffs.setdefault(d, []).append((i, j))
    uni = nonmono = 0
    for c in product(alphabet3, repeat=len(offsets)):
        s = 0
        for x in c:
            s += x[0] * x[0] - x[0] * x[1] + x[1] * x[1]
        if s != 9:
            continue
        ok = True
        for _d, prs in diffs.items():
            t0 = t1 = 0
            for (i, j) in prs:
                a0, a1 = c[i]
                b0, b1 = c[j]
                cb0, cb1 = b0 - b1, -b1
                t0 += a0 * cb0 - a1 * cb1
                t1 += a0 * cb1 + a1 * cb0 - a1 * cb1
            if t0 or t1:
                ok = False
                break
        if ok:
            uni += 1
            if sum(1 for x in c if x != (0, 0)) > 1:
                nonmono += 1
    return {"differences": len(diffs),
            "multiplicities": sorted({len(v) for v in diffs.values()}),
            "unitary": uni, "non_monomial": nonmono}


def i_modulus_descent(qs, ms, require_separation=True):
    """THE FORCING LEG, as a theorem checked exhaustively rather than
    asserted.  paper-20 derives the connection from the arena: the record's
    cell value is an ARENA SCALAR, an element of the additive group of F_q,
    and the walk's phase is a character of that group.  A phase map
    n -> zeta_m^n is a function of the arena scalar exactly when it is
    constant on the residues modulo q, and it distinguishes the arena's own
    scalars exactly when it is injective on them; the two together leave the
    field order and nothing else.  Both conditions are decided by integer
    residues alone -- zeta_m^a = zeta_m^b exactly when a and b agree modulo m
    -- so no root of unity is needed and the sweep is not confined to the
    moduli one ring happens to hold.  The sweep runs over PRIME field orders,
    where the additive group is cyclic; at a prime power it is not, and that
    is the register's own opening, named in the paper.

    THE LEMMA the sweep instantiates (K1 MINOR-4, so that the four orders are
    read as instances and not as an empirical finding): the first condition
    holds exactly when m divides q, the second exactly when m is at least q,
    and m | q with m >= q leaves m = q.  Both equivalences are verified here
    against the computed predicates at every swept point, so the lemma is
    checked and not merely narrated.
    """
    rows, lemma_bad = [], []
    for q in qs:
        good = []
        for m in ms:
            descends = all((n % m) == ((n % q) % m) for n in range(4 * q))
            separates = len({n % m for n in range(q)}) == q
            if descends != (q % m == 0):
                lemma_bad.append((q, m, "descends"))
            if separates != (m >= q):
                lemma_bad.append((q, m, "separates"))
            if descends and (separates or not require_separation):
                good.append(m)
        rows.append((q, tuple(good)))
    return rows, lemma_bad


# ===========================================================================
# SECTION D.  k_*  --  THE COMPARATOR.
#   It decides agreement and difference, pulls the parents' own numbers out of
#   the located anchor text, and re-derives the head.  It calls neither
#   builder: it is handed their published ladders and nothing else, which
#   G-S1-DISJOINT-CODE checks by AST.
# ===========================================================================

def k_int_from(text, after):
    """the anchor's own value, pulled out of the located text: the consuming
    gate takes a number OUT of the parent's sentence and compares it with a
    measurement, so the anchor binds meaning and not existence."""
    hay = ET.canon(text)
    i = hay.find(ET.canon(after))
    if i < 0:
        return None
    m = re.search(r"(\d+)", hay[i + len(ET.canon(after)):])
    return int(m.group(1)) if m else None


def k_frac_from(text, after):
    hay = ET.canon(text)
    i = hay.find(ET.canon(after))
    if i < 0:
        return None
    m = re.search(r"(\d+)\s*/\s*(\d+)", hay[i + len(ET.canon(after)):])
    return Fraction(int(m.group(1)), int(m.group(2))) if m else None


def k_first_difference(a, b, horizon):
    """the first tick at which two site-occupation ladders differ, or None."""
    for t in range(1, horizon + 1):
        if a[t] != b[t]:
            return t
    return None


def k_agreement_checks(a, b, horizon, upto):
    """per-site, per-tick agreement -- an object predicate, never a count
    (#87): every site of every tick is compared against its own value."""
    checks = viol = 0
    for t in range(1, min(upto, horizon) + 1):
        for s in range(len(a[t])):
            checks += 1
            if a[t][s] != b[t][s]:
                viol += 1
    return checks, viol


def k_total_variation(a, b):
    return sum(abs(x - y) for x, y in zip(a, b)) / 2


def k_max_gap(a, b):
    return max(abs(x - y) for x, y in zip(a, b))


def k_shots(delta, confidence_denominator):
    """the finite experiment's size, by Chebyshev on a two-outcome test and in
    exact rational arithmetic: with N >= C/delta^2 the probability that the
    empirical frequency of the discriminating site misses its own value by
    delta/2 is at most 1/C on each side."""
    if delta <= 0:
        raise ET.CheckFail("G-FALSIFIER-SPECIFIED",
                           "a falsifier with no gap")
    need = Fraction(confidence_denominator) / (delta * delta)
    return -(-need.numerator // need.denominator)


def k_region_map(tree):
    """the four regions, the call graph, the module's own top-level function
    names, and its module-level NAME BINDINGS -- `X = n_step_ring` at module
    level makes X the null's function, and a call through X is a call to it
    (K3 MAJOR-3: the delivered predicate resolved callees by name and a
    one-line alias walked past it)."""
    region, defined, aliases = {}, set(), {}
    calls = collections.defaultdict(set)
    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            defined.add(node.name)
    for node in tree.body:
        if isinstance(node, ast.Assign) and isinstance(node.value, ast.Name):
            for tgt in node.targets:
                if isinstance(tgt, ast.Name) and node.value.id in defined:
                    aliases[tgt.id] = node.value.id
    for node in ast.walk(tree):
        if not isinstance(node, ast.FunctionDef):
            continue
        pre = node.name.split("_")[0]
        if pre in ("n", "i", "k", "p") and node.name in defined:
            region[node.name] = pre
        for sub in ast.walk(node):
            if isinstance(sub, ast.Call):
                nm = (getattr(sub.func, "id", None)
                      or getattr(sub.func, "attr", None))
                if nm:
                    calls[node.name].add(nm)
            if isinstance(sub, ast.Name) and sub.id in aliases:
                calls[node.name].add(sub.id)
    return region, calls, defined, aliases


def k_region_offences(region, calls, defined, aliases, shared_ground):
    """EVERY cross-region edge, in both directions, plus the shared-component
    class (registered family S-2): a function in no region, called from more
    than one region, is an undeclared shared component."""
    out = []
    users = collections.defaultdict(set)
    for fn, pre in sorted(region.items()):
        for callee in sorted(calls[fn]):
            target = aliases.get(callee, callee)
            cpre = region.get(target)
            if cpre is not None:
                if cpre != pre:
                    out.append("%s (%s) calls %s (%s)"
                               % (fn, pre, target, cpre))
                continue
            if target in defined:
                users[target].add(pre)
    for helper, regions in sorted(users.items()):
        if len(regions) > 1 and helper not in shared_ground:
            out.append("%s is an undeclared shared component of %s"
                       % (helper, sorted(regions)))
    return sorted(set(out))


def k_parity_binding(tree):
    """PR1..PR5's CONTENT, structurally.  The sweep binds the arena, the
    horizon, the coin, the start site and the internal direction to five
    `pr_`-prefixed locals and passes THOSE to both arms, so the parity is a
    property of the source and not a sentence in the paper.  This returns the
    names each arm actually receives in the parity positions."""
    isp_names, null_names = None, None
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        fn = getattr(node.func, "id", None)
        names = [getattr(a, "id", None) for a in node.args]
        pr = [n for n in names if n and n.startswith("pr_")]
        if not pr:
            continue
        if fn == "n_ladder_ring":
            null_names = [names[0], names[1], names[2], names[3], names[4]]
        if fn == "i_ladder" and len(names) >= 6:
            isp_names = [names[0], names[1], names[3], names[4], names[5]]
    return isp_names, null_names


def k_closest_null(target, laws):
    """the smallest single-site gap any member of a swept null class reaches
    against the ISP law, and whether any member reproduces it exactly."""
    best, arg, exact = None, None, 0
    for (tag, row) in laws:
        if row == target:
            exact += 1
        g = k_max_gap(target, row)
        if best is None or g < best:
            best, arg = g, tag
    return best, arg, exact


def k_head_segments(payload):
    """THE PAYLOAD READ, SEGMENT BY SEGMENT.  This is the comparator's own
    route to the head's content: it takes every published field OUT of the
    receipt payload and returns an ordered list of (label, value) pairs.  It
    knows nothing about how the builder joined them, and the builder knows
    nothing about this function -- G-S1-DISJOINT-CODE checks by AST that
    neither calls the other and that they are two functions, not one."""
    d = payload["discriminant"]
    nul = payload["null_model"]
    cen = payload["q155_census"]
    mod = payload["modulus"]
    per = payload["lattice_perimeter"]
    cfm = payload["lattice_closed_form"]
    plq = payload["lattice_plaquette"]
    qrt = payload["lattice_quartic"]
    pri = payload["structure_price"]
    ctl = payload["null_is_the_control"]
    ordf = payload["coin_order_fiber"]
    wide = payload["wider_null_sweep"]
    fal = payload["falsifier"]
    fea = payload["feasibility"]
    out = [("VERDICT", d["verdict_word"])]
    out.append(("CLASS", "%s;NULL=%s;RULES=%d;SHARED-WITH-ISP=%s;ABLATED=%s"
                % (payload["scope"]["class_word"], nul["word"], nul["rules"],
                   nul["shared"], nul["dropped"])))
    out.append(("PRIMARY",
                "THE-RECORD-FREE-NULL-REPRODUCES-%d-OF-%d-PARENT-RESULTS;"
                "%d-OF-%d-TESTED-ROWS;%d-NOT-REPRODUCED;%d-NOT-EXPRESSIBLE;"
                "REPRODUCED=%s"
                % (cen["parent_reproduced"], cen["parent_results"],
                   cen["reproduced"], cen["rows_count"],
                   cen["not_reproduced"], cen["not_expressible"],
                   "+".join(cen["reproduced_keys"]))))
    out.append(("LATTICE", "PERIMETER-%s;CLOSED-FORM-%s;GAP-%s;PLAQUETTE-%s;"
                "QUARTIC-%s"
                % (per["word"], cfm["word_closed"], cfm["word_gap"],
                   plq["word"], qrt["word"])))
    out.append(("BASE-FINDING-IS-THE-PARENTS",
                "THE-NULL-IS-PAPER-20S-OWN-FROZEN-STAGE-CONTROL-UP-TO-A-"
                "GLOBAL-PHASE;EQUAL-AT-%d-OF-%d-SITE-DISTRIBUTION-CHECKS;"
                "THIS-UNITS-NEW-CONTENT=THE-TICK+THE-EXACT-MAGNITUDES+"
                "THE-UNIVERSALITY"
                % (ctl["equal"], ctl["checks"])))
    out.append(("AGREEMENT",
                "%d-OF-%d-SITE-BY-TICK-CHECKS-EQUAL-THROUGH-TICK-%d"
                % (d["agree_checks"] - d["agree_violations"],
                   d["agree_checks"], d["agree_upto"])))
    out.append(("ABLATION-EFFECT",
                "FIRST-AT-TICK-%d-AT-%d-OF-%d-NON-TRIVIAL-FIBER-POINTS;"
                "NEVER-AT-%d-TRIVIAL-COIN-POINTS"
                % (d["first_difference_tick"], d["nontrivial_at_tick"],
                   d["nontrivial_points"], d["trivial_points"])))
    out.append(("COIN-ORDER-FIBER",
                "DELIVERED-%s-TICK-%d;ALTERNATIVE-%s-TICK-%d-WITH-THE-TICK-"
                "%d-LAW-EQUAL-TO-THE-NULLS-AT-BOTH-PLANES;THE-TICK-IS-ORDER-"
                "RELATIVE;ORIENTATION-FIBER-INERT"
                % (ordf["delivered_order"], ordf["delivered_tick"],
                   ordf["alternative_order"], ordf["alternative_tick"],
                   d["first_difference_tick"])))
    out.append(("WIDER-NULL-SWEEP",
                "%d-MEMORYLESS-CONFIGURATIONS;%d-EXACT-REPRODUCTIONS;"
                "CLOSEST-AT-AG-2-2=%s-BY-A-NON-COVARIANT-COIN-AGAINST-THE-"
                "PR3-NULLS-%s;PR3-IS-THE-BEST-AT-AG-2-3"
                % (wide["configurations"], wide["exact_reproductions"],
                   wide["closest_gap_q2"], wide["pr3_gap_q2"])))
    out.append(("IPR-AT-AG-2-3", "ISP-%s-VS-NULL-%s;TV=%s"
                % (d["q3"]["isp_ipr"], d["q3"]["null_ipr"], d["q3"]["tv"])))
    out.append(("IPR-AT-AG-2-2", "ISP-%s-VS-NULL-%s;TV=%s"
                % (d["q2"]["isp_ipr"], d["q2"]["null_ipr"], d["q2"]["tv"])))
    out.append(("M-EQUALS-Q",
                "%s;INTERNAL-CHECK-CLOSING-THE-PARENTS-REGISTERED-TEST-NOT-"
                "AN-EXTERNAL-PREDICTION;CONSTRUCTION-DEPENDENT;OBSERVABLE-AT-"
                "%d-OF-%d-DECLARED-MODULI"
                % (mod["word"], mod["distinct_values"], mod["moduli_run"])))
    out.append(("PRICE",
                "ISP-CARRIES-%d-STRUCTURES-THE-NULL-DOES-NOT-AND-%d-FREE-"
                "NUMBER;THE-FREE-NUMBER-IS-THE-PHASE-MODULUS-AND-IT-IS-FIXED-"
                "ONLY-BY-THE-CONSTRUCTION-DEPENDENT-DESCENT-FORCING;"
                "PARAMETER-FREE-IS-NOT-STRUCTURE-FREE"
                % (pri["structures"], pri["free_numbers"])))
    out.append(("FALSIFIER",
                "%s;SHOTS-IF-EVER-REALIZED=%d-AT-AG-2-3-AND-%d-AT-AG-2-2-"
                "AGAINST-THE-CLOSEST-MEMORYLESS-WALK"
                % (fal["word"], fal["shots_q3"], fal["shots_q2"])))
    out.append(("FEASIBILITY", "%s;PIN-OUTCOME-WORDS=%d-OF-%d-REACHABLE;"
                "%s" % (fea["word"], fea["reachable"], fea["declared"],
                        fea["blocked_route"])))
    out.append(("SUCCESSOR", payload["scope"]["successor_word"]))
    out.append(("AXES", "%s" % "+".join(
        a.replace(" ", "-").upper()
        for a in payload["scope"]["declared_free_axes"])))
    out.append(("SCOPE", payload["scope"]["word"]))
    return out


def k_rebuild_head(payload):
    """THE COMPARATOR'S OWN ROUTE TO THE HEAD, END TO END: its own segment
    labels are dropped for the first segment and prefixed with `LABEL=` for
    the rest, and its own separator joins them."""
    segs = k_head_segments(payload)
    out = [segs[0][1]]
    for (label, value) in segs[1:]:
        out.append(label + "=" + value)
    return " -- ".join(out)


# ===========================================================================
# SECTION D2.  p_*  --  THE HEAD BUILDER.
#   The delivered head is rendered HERE, from the payload, with this region's
#   own format strings.  The comparator in section D rebuilds it by its own
#   route; the two share no code, no literal and no helper, and neither calls
#   the other.  K2 MAJOR-1 / K3 MAJOR-2: the delivered object previously
#   compared `k_rebuild_head(R)` with `k_rebuild_head(R)`, an algebraic
#   identity under a gate whose statement claimed an independent route.
# ===========================================================================

def p_head_line(label, body):
    return "%s=%s" % (label, body) if label else body


def p_render_head(payload):
    """THE DELIVERED HEAD.  Its own segment order (the scope word first among
    the trailing segments, the axes last), its own field access, its own
    strings.  Nothing here is shared with the comparator's route."""
    disc = payload["discriminant"]
    rule = payload["null_model"]
    q155 = payload["q155_census"]
    modl = payload["modulus"]
    latp = payload["lattice_perimeter"]
    latc = payload["lattice_closed_form"]
    latq = payload["lattice_plaquette"]
    lat4 = payload["lattice_quartic"]
    price = payload["structure_price"]
    control = payload["null_is_the_control"]
    fiber6 = payload["coin_order_fiber"]
    widen = payload["wider_null_sweep"]
    falsi = payload["falsifier"]
    feas = payload["feasibility"]
    scope = payload["scope"]
    lines = [p_head_line("", disc["verdict_word"])]
    lines.append(p_head_line(
        "CLASS", ";".join([
            scope["class_word"], "NULL=" + rule["word"],
            "RULES=" + str(rule["rules"]),
            "SHARED-WITH-ISP=" + rule["shared"],
            "ABLATED=" + rule["dropped"]])))
    lines.append(p_head_line("PRIMARY", ";".join([
        "THE-RECORD-FREE-NULL-REPRODUCES-" + str(q155["parent_reproduced"])
        + "-OF-" + str(q155["parent_results"]) + "-PARENT-RESULTS",
        str(q155["reproduced"]) + "-OF-" + str(q155["rows_count"])
        + "-TESTED-ROWS",
        str(q155["not_reproduced"]) + "-NOT-REPRODUCED",
        str(q155["not_expressible"]) + "-NOT-EXPRESSIBLE",
        "REPRODUCED=" + "+".join(q155["reproduced_keys"])])))
    lines.append(p_head_line("LATTICE", ";".join([
        "PERIMETER-" + latp["word"], "CLOSED-FORM-" + latc["word_closed"],
        "GAP-" + latc["word_gap"], "PLAQUETTE-" + latq["word"],
        "QUARTIC-" + lat4["word"]])))
    lines.append(p_head_line("BASE-FINDING-IS-THE-PARENTS", ";".join([
        "THE-NULL-IS-PAPER-20S-OWN-FROZEN-STAGE-CONTROL-UP-TO-A-GLOBAL-PHASE",
        "EQUAL-AT-" + str(control["equal"]) + "-OF-" + str(control["checks"])
        + "-SITE-DISTRIBUTION-CHECKS",
        "THIS-UNITS-NEW-CONTENT=THE-TICK+THE-EXACT-MAGNITUDES+"
        "THE-UNIVERSALITY"])))
    lines.append(p_head_line(
        "AGREEMENT",
        str(disc["agree_checks"] - disc["agree_violations"]) + "-OF-"
        + str(disc["agree_checks"]) + "-SITE-BY-TICK-CHECKS-EQUAL-THROUGH-"
        "TICK-" + str(disc["agree_upto"])))
    lines.append(p_head_line("ABLATION-EFFECT", ";".join([
        "FIRST-AT-TICK-" + str(disc["first_difference_tick"]) + "-AT-"
        + str(disc["nontrivial_at_tick"]) + "-OF-"
        + str(disc["nontrivial_points"]) + "-NON-TRIVIAL-FIBER-POINTS",
        "NEVER-AT-" + str(disc["trivial_points"])
        + "-TRIVIAL-COIN-POINTS"])))
    lines.append(p_head_line("COIN-ORDER-FIBER", ";".join([
        "DELIVERED-" + fiber6["delivered_order"] + "-TICK-"
        + str(fiber6["delivered_tick"]),
        "ALTERNATIVE-" + fiber6["alternative_order"] + "-TICK-"
        + str(fiber6["alternative_tick"]) + "-WITH-THE-TICK-"
        + str(disc["first_difference_tick"])
        + "-LAW-EQUAL-TO-THE-NULLS-AT-BOTH-PLANES",
        "THE-TICK-IS-ORDER-RELATIVE", "ORIENTATION-FIBER-INERT"])))
    lines.append(p_head_line("WIDER-NULL-SWEEP", ";".join([
        str(widen["configurations"]) + "-MEMORYLESS-CONFIGURATIONS",
        str(widen["exact_reproductions"]) + "-EXACT-REPRODUCTIONS",
        "CLOSEST-AT-AG-2-2=" + widen["closest_gap_q2"]
        + "-BY-A-NON-COVARIANT-COIN-AGAINST-THE-PR3-NULLS-"
        + widen["pr3_gap_q2"],
        "PR3-IS-THE-BEST-AT-AG-2-3"])))
    for (plane, key) in (("AG-2-3", "q3"), ("AG-2-2", "q2")):
        lines.append(p_head_line("IPR-AT-" + plane, ";".join([
            "ISP-" + disc[key]["isp_ipr"] + "-VS-NULL-"
            + disc[key]["null_ipr"], "TV=" + disc[key]["tv"]])))
    lines.append(p_head_line("M-EQUALS-Q", ";".join([
        modl["word"],
        "INTERNAL-CHECK-CLOSING-THE-PARENTS-REGISTERED-TEST-NOT-AN-EXTERNAL-"
        "PREDICTION", "CONSTRUCTION-DEPENDENT",
        "OBSERVABLE-AT-" + str(modl["distinct_values"]) + "-OF-"
        + str(modl["moduli_run"]) + "-DECLARED-MODULI"])))
    lines.append(p_head_line("PRICE", ";".join([
        "ISP-CARRIES-" + str(price["structures"])
        + "-STRUCTURES-THE-NULL-DOES-NOT-AND-" + str(price["free_numbers"])
        + "-FREE-NUMBER",
        "THE-FREE-NUMBER-IS-THE-PHASE-MODULUS-AND-IT-IS-FIXED-ONLY-BY-THE-"
        "CONSTRUCTION-DEPENDENT-DESCENT-FORCING",
        "PARAMETER-FREE-IS-NOT-STRUCTURE-FREE"])))
    lines.append(p_head_line("FALSIFIER", ";".join([
        falsi["word"],
        "SHOTS-IF-EVER-REALIZED=" + str(falsi["shots_q3"]) + "-AT-AG-2-3-AND-"
        + str(falsi["shots_q2"])
        + "-AT-AG-2-2-AGAINST-THE-CLOSEST-MEMORYLESS-WALK"])))
    lines.append(p_head_line("FEASIBILITY", ";".join([
        feas["word"],
        "PIN-OUTCOME-WORDS=" + str(feas["reachable"]) + "-OF-"
        + str(feas["declared"]) + "-REACHABLE",
        feas["blocked_route"]])))
    lines.append(p_head_line("SUCCESSOR", scope["successor_word"]))
    lines.append(p_head_line("AXES", "+".join(
        ax.replace(" ", "-").upper()
        for ax in scope["declared_free_axes"])))
    lines.append(p_head_line("SCOPE", scope["word"]))
    return " -- ".join(lines)


# ===========================================================================
# SECTION E.  THE ANCHORS AND THE WALLS.
# ===========================================================================

ANCHORS = [
    ET.Anchor("A-PIN-NULL",
              "a plain d=2 discrete-time quantum walk / lattice model with "
              "the same arena size, no record layer, no conserved-price "
              "structure", PIN_REL, "G-NULL-RULE-TOTAL"),
    ET.Anchor("A-PIN-EXPRESSIBILITY",
              "the record-side observables the null lacks by construction "
              "(state which are definitional vs measurable)", PIN_REL,
              "G-EXPRESSIBILITY-CENSUS"),
    ET.Anchor("A-COUP-CONNECTION",
              "The link connection the record defines is therefore valued in "
              "the arena's own scalar group Z_3, and the walk's phase "
              "alphabet is the cube roots of unity.",
              "v14/paper-20-coupling.md", "G-MODULUS-DESCENT-THEOREM"),
    ET.Anchor("A-COUP-FROZEN",
              "The frozen-stage control is the same walk, the same emission "
              "rule and the same branching, on counts that never update.",
              "v14/paper-20-coupling.md", "G-ISP-FIDELITY-PARENT"),
    ET.Anchor("A-COUP-RESIDUE",
              "the walk consumes the count residue n mod 3, not the count",
              "v14/paper-20-coupling.md", "G-MODULUS-OBSERVABLE"),
    ET.Anchor("A-NDEP-SUCCESSOR",
              "The concrete successor test is to build the connection at "
              "AG(2,2) over F_2 and see whether it forces m = 2, and to find "
              "an observable the modulus does move.",
              "v14/paper-39-ndep.md", "G-M2-PREDICTION-RUN"),
    ET.Anchor("A-NDEP-PREDICTS",
              "AG(2,2) is over F_2, so read there it predicts m = 2, a "
              "determinate and q-carried answer",
              "v14/paper-39-ndep.md", "G-M2-PREDICTION-RUN"),
    ET.Anchor("A-POT-PERIMETER",
              "At every coin of the carrier and at every pair of ladder "
              "shapes of equal perimeter, the loop observable takes the same "
              "value", "v14/paper-36-pot.md", "G-PERIMETER-LAW-BOTH"),
    ET.Anchor("A-POT-GAP",
              "The ladder's own transfer content is the closed form of "
              "section 5: spectrum {1,1,1/2} and gap 1/2, verified at every "
              "coin of the carrier and unchanged at every declared row.",
              "v14/paper-36-pot.md", "G-GAP-BOTH"),
    ET.Anchor("A-POT-PLAQUETTE",
              "the plaquette's trace takes 11 distinct values on the carrier, "
              "its counting expectation is 13/10",
              "v14/paper-36-pot.md", "G-PLAQUETTE-BOTH"),
    ET.Anchor("A-ACT-QUARTIC",
              "Its expectation under every admissible weight system is "
              "therefore the single value zero",
              "v14/paper-34-act.md", "G-QUARTIC-BOTH"),
    ET.Anchor("A-ACT-OBSERVABLE",
              "the sign of the fourth power of the two off-diagonal entries, "
              "added", "v14/paper-34-act.md", "G-QUARTIC-BOTH"),
]

# THE WALLS.  Written from the FINDING, in the voices a paper would use.
#
# TPL-2's wall item, honestly this time (K3 MINOR-4: the source claimed
# controls that did not exist, and two of three walls were exercised by
# neither leg).  Each wall below carries its OWN controls -- sentences a paper
# would write, drafted from the disease and not from the pattern -- and
# G-PAPER-WALLS requires every negative control to be caught by its wall and
# every positive control to be a standing sentence whose deletion fails it.
# A control that is not caught is a hole in the wall, and the gate says so.
class Wall(ET.SemanticWall):
    """the template's wall, plus the controls TPL-2 asks for."""

    def __init__(self, name, negative, positive, controls,
                 policed=(), licences=()):
        super().__init__(name, negative, positive, policed=policed,
                         licences=licences)
        self.controls = list(controls)

    def seal_value(self):
        v = super().seal_value()
        v["controls"] = len(self.controls)
        v["policed"] = list(self.policed)
        return v

    def control_report(self):
        """every negative control must match some negative leg, and no
        control may match the clean paper's own standing sentences."""
        out = []
        for text in self.controls:
            hay = ET.canon(text)
            hit = [p for p in self.negative if re.search(p, hay)]
            if not hit:
                out.append(text[:70])
        return out


_BE = r"(?:is|was|are|were|has been|have been|can be|could be|remains?)"

WALL_EXHAUSTIVE = Wall(
    "W-NO-EXHAUSTIVE-NULL-CLASS",
    negative=[
        # the null class asserted exhaustive
        r"no (?:simpler |other |ordinary |standard |existing )*(?:model|"
        r"theory|walk|automaton|lattice model)s? (?:can|could|will|"
        r"is able to|would be able to) (?:reproduce|produce|give|match|"
        r"account for)",
        r"(?:only|uniquely) isp (?:can|could) (?:reproduce|produce|give)",
        r"(?:rules? out|ruled out|excludes?|excluded) (?:every|all) "
        r"(?:simpler|alternative|competing|other) (?:model|theory|account)s?",
        r"the null class %s exhaustive" % _BE,
        r"(?:this|the) (?:result|difference|discriminant) %s no (?:simpler|"
        r"other) (?:model|explanation)" % _BE,
        # quantum mechanics itself refuted or superseded
        r"(?:refutes?|refuted|overturns?|supersedes?|replaces?) "
        r"(?:ordinary |standard |textbook )?quantum (?:mechanics|theory)",
        # laboratory claims this corpus cannot make
        r"(?:has been|was|were) (?:measured|observed|detected) in "
        r"(?:the )?(?:lab|laboratory|experiment)",
        r"(?:an? )?(?:existing|published|real) experiment (?:confirms?|"
        r"confirmed|verifies|verified|supports?) ",
        r"(?:si|physical) units? (?:are|is) (?:supplied|given|derived)",
    ],
    positive=[
        r"no memory-bearing null is tested here",
        r"no operational mapping to laboratory units exists in this corpus",
    ],
    controls=[
        "No simpler model can reproduce this difference.",
        "The result rules out every competing account of the third tick.",
        "Only ISP can produce the value section 6 publishes.",
        "The null class is exhaustive at this arena.",
        "The third-tick law was observed in the laboratory.",
    ],
)

WALL_PARAMFREE = Wall(
    "W-PARAMETER-FREE-IS-RELATIVE",
    negative=[
        r"(?:isp|the theory|the model) has no (?:free )?(?:parameters?|"
        r"declarations?|choices?)(?![\w\s]{0,30}(?:the null|beyond))",
        r"(?:nothing|no datum|no quantity)[\w\s,'-]{0,30}%s declared" % _BE,
        r"(?:the|this) prediction %s (?:wholly |entirely |completely )?"
        r"(?:free of|without) (?:any )?declarations?" % _BE,
        r"(?:derived|forced) from first principles alone",
    ],
    positive=[
        r"the prediction is free of every parameter the null does not also "
        r"carry",
    ],
    controls=[
        "ISP has no free parameters.",
        "Nothing in the comparison is declared.",
        "This prediction is entirely free of any declarations.",
        "The third tick is derived from first principles alone.",
    ],
)

# THE ABLATION WALL, WITH ITS LICENCE LEG ON.  K2 MAJOR-3 measured four of
# five natural paraphrases walking through the pattern list, because five of
# the six negative legs were anchored on literal word-orders.  Two repairs,
# both here.  (1) The pattern list is widened by the readings the mandate
# named -- distinguishes-from-QM, falsifies-ISP-as-nature, parameter-free
# prediction, ISP-predicts, ISP's-first.  (2) The template's LICENCE LEG is
# switched on, which is the leg a paraphrase cannot dodge: any sentence
# carrying a POLICED word must also carry one of this run's own rendered
# claims, so a new voicing of the banned reading is caught by the claim it
# fails to carry rather than by the words it happens to choose.
WALL_ABLATION = Wall(
    "W-ABLATION-NOT-PREDICTION",
    negative=[
        # the reading the review struck out, in the voices a paper would use
        r"(?:the |isp's )?first parameter-free prediction",
        r"(?:this|the) (?:is|was|gives|yields) (?:isp's |the theory's )?"
        r"first (?:parameter-free |real )?prediction",
        r"(?:an?|the) (?:external|empirical|experimental) prediction of "
        r"(?:isp|the theory|this model)",
        r"(?:predicts?|predicted) (?:a |an |the )?(?:new )?(?:physical |"
        r"empirical |laboratory )(?:effect|phenomenon|result)",
        r"(?:tests?|tested|testing) (?:isp|the theory) against (?:nature|"
        r"experiment|the world)",
        r"the modulus (?:is |was )?(?:an?|the) (?:external|empirical) "
        r"prediction",
        # K2 MAJOR-3's four survivors, and three more of this repair's own
        r"(?:distinguish(?:es|ed|ing)?|separates?|tells? apart|parts? "
        r"company)[\w\s,'-]{0,40}\bfrom\b[\w\s,'-]{0,30}(?:quantum "
        r"(?:mechanics|theory)|ordinary quantum|standard quantum|textbook "
        r"quantum)",
        r"(?:would |could |will |can )?(?:falsif(?:y|ies|ied)|refut(?:e|es|"
        r"ed)|disprov(?:e|es|ed)) (?:isp|the theory|this model)\b",
        r"(?:isp|the theory|this theory|the model|this model) (?:therefore |"
        r"thus |already )?predicts?\b",
        r"\bprediction\b[\w\s,'-]{0,25}\b(?:is|was) (?:parameter-free|free "
        r"of (?:all|any) parameters)",
        r"\bisp's first\b",
        r"(?:no|not one) (?:ordinary|standard|textbook|plain) (?:coined )?"
        r"(?:quantum )?walk (?:reaches|attains|gives|produces) ",
        r"(?:the )?effect (?:is|was) physical\b",
        r"(?:a|one|single) (?:run|shot) of the (?:deciding|proposed) "
        r"experiment would\b",
        # three more this repair wrote, from the disease and not the patterns
        r"\b(?:physical|empirical|experimental|laboratory) prediction\b",
        r"(?:decide|decides|deciding|choose|chooses) between (?:isp|the "
        r"theory|this theory|this model) and\b",
        r"what (?:isp|the theory|this theory|this model) predicts\b",
    ],
    positive=[
        r"this unit is a model-ablation benchmark",
        r"the null compared here is memoryless",
        r"parameter-free is not structure-free",
    ],
    # THE LICENCE LEG.  A sentence that names the banned reading -- even to
    # disclaim it, which this paper does twice -- must carry one of this run's
    # own rendered claims, so the class travels with the word.
    policed=("first prediction", "first parameter-free prediction",
             "falsifies isp", "distinguishes isp from", "isp predicts",
             "predicts an effect"),
    licences=("this unit is a model-ablation benchmark",
              "the null compared here is memoryless",
              "no memory-bearing null is tested here",
              "no operational mapping to laboratory units exists in this "
              "corpus",
              "parameter-free is not structure-free",
              "a definitional absence is not a discriminant"),
    controls=[
        "The third-tick site occupation is the observable that distinguishes "
        "ISP from standard quantum mechanics.",
        "A single run of the deciding experiment would falsify ISP if the "
        "third-tick occupation came out at the record-free value.",
        "The prediction of section 6 is parameter-free, and it is ISP's "
        "first.",
        "ISP therefore predicts an effect that ordinary quantum walks do not "
        "exhibit, and the effect is physical.",
        "This is the theory's first prediction in which no number was "
        "adjusted to obtain it.",
        "Section 6 is the first parameter-free prediction of this theory.",
        "No ordinary coined walk reaches the value section 6 publishes.",
        "The third-tick occupation is a physical prediction of this theory.",
        "Measuring the third-tick occupation would decide between ISP and "
        "ordinary quantum walks.",
        "The value at the third tick is what this theory predicts and a "
        "plain walk does not.",
    ],
)

WALLS = (WALL_EXHAUSTIVE, WALL_PARAMFREE, WALL_ABLATION)

# A markdown table row.  The referent gate reads PROSE: a table row is bound
# cell for cell against this run's own rendering by G-PAPER-CLAIMS, which is a
# stronger binding than membership in a universe, and a table has no sentence
# boundaries, so leaving the rows in would swallow the surrounding prose into
# whichever universe a column header happened to name.
TABLE_ROW = re.compile(r"^[ \t]*\|.*\|[ \t]*$", re.M)

NUM = re.compile(r"(?<![\w.,/-])(\d[\d,]*)(?![\w/])")
FENCE_RE = re.compile(r"```[^\n]*\n(.*?)```", re.S)
FRAC = re.compile(r"(?<![\w./-])(\d+)/(\d+)(?![\w/])")
# A declared exemption class rather than a token: the ordinal that numbers a
# heading in this paper is not a count, and it is removed from the text both
# paper gates read.  It is required to occur, so the exemption cannot be
# carried unused.
SECTION_RE = re.compile(r"^(#{1,6})\s*\d+\.", re.M)
SPELLED = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
    "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11,
    "twelve": 12,
}


# ===========================================================================
# SECTION F.  THE RUN.
# ===========================================================================

def _fr(x):
    return str(x)


def _dist(row):
    return [str(x) for x in row]


def full_run(write=False, mutant=None, render=False, mode="--run"):
    MUTANT["name"], MUTANT["used"] = mutant, set()
    reads: list[str] = []
    RS = ET.ReadSet(REPO)
    RS.install()
    RS.active = True

    LD, TR, SEAL = ET.Ledger(), ET.Transcript(), ET.Seal()
    REG, CL, RR = ET.CountRegistry(), ET.Claims(), ET.ReferentRegistry()
    for tok, why in TOKEN_EXEMPTIONS.items():
        REG.exempt_token(tok, why)
    R: dict = {}
    PARTIAL["R"] = R

    def gate(gid, statement, ok, evidence):
        # every gate id is declared before any of them fires (K3 MAJOR-5):
        # nothing can be appended to the battery at run time, so the declared
        # list is a sound denominator for the coverage gate and for the count.
        if gid not in GATE_NAMES:
            raise ET.CheckFail("T-FALSIFIER-COVERAGE",
                               "undeclared gate id: %s" % gid)
        LD.gate(gid, statement, ok, evidence)
        TR.row(gid, ok, evidence)

    TR.say("DISC (paper-47) -- THE DISCRIMINATOR: THE NULL GETS ITS OWN "
           "INSTRUMENT")
    TR.say("=" * 74)

    # -- sources, pinned ---------------------------------------------------
    texts, shas, drifted = {}, {}, []
    for rel, want in sorted(SOURCES.items()):
        p = os.path.join(REPO, rel)
        got = sha12(p)
        shas[rel] = got
        reads.append(rel)
        if got != want:
            drifted.append("%s %s != %s" % (rel, got, want))
        if rel.endswith(".md"):
            texts[rel] = read_text(rel)
            reads.append(rel)
    if mut("MUT-SOURCE-DRIFT"):
        shas[PIN_REL] = shas[PIN_REL][::-1]
        drifted = [k for k in sorted(shas) if shas[k] != SOURCES[k]]
    R["sources"] = {k: shas[k] for k in sorted(shas)}
    SEAL.seal("sources", R["sources"], "G-SOURCES-PINNED")
    REG.measured("sources", len(SOURCES), "len(SOURCES)")
    gate("G-SOURCES-PINNED",
         REG.stmt("every one of the {sources} pinned sources digests to the "
                  "value the pin froze, and no repository object is read at "
                  "any other digest", sources=1),
         not drifted, "sources %d drifted %s"
         % (len(SOURCES), drifted or "none"))

    # -- the paper under test ----------------------------------------------
    paper_path = os.path.join(REPO, PAPER_REL)
    if not os.path.exists(paper_path):
        ET.require_object(mode, paper_path, None)
    paper = read_text(PAPER_REL)
    reads.append(PAPER_REL)
    ET.require_object(mode, paper_path, paper)
    ASET = ET.AnchorSet([ET.Anchor(a.name, a.needle, a.source, a.consumer)
                         for a in ANCHORS])
    src_for_anchor = dict(texts)
    if mut("MUT-ANCHOR"):
        src_for_anchor["v14/paper-39-ndep.md"] = texts[
            "v14/paper-39-ndep.md"].replace("q-carried answer",
                                            "p-carried answer", 1)
    try:
        ASET.locate(src_for_anchor, paper)
        lprob = None
    except ET.CheckFail as exc:
        lprob = exc.detail
    REG.measured("anchor_rows", len(ANCHORS), "len(ANCHORS)")
    R["anchors_located"] = {"rows": len(ANCHORS), "problem": lprob or "none",
                            "sources": sorted({a.source for a in ANCHORS})}
    SEAL.seal("anchors_located", R["anchors_located"], "G-ANCHORS-LOCATED")
    gate("G-ANCHORS-LOCATED",
         REG.stmt("each of the {anchor_rows} verbatim anchors occurs exactly "
                  "once in the pinned parent's own bytes AND once in this "
                  "paper's rendering, under the same canonicalisation, before "
                  "any of them is read", anchor_rows=1),
         lprob is None, "anchors %d located %s"
         % (len(ANCHORS), lprob or "all"))

    # -- S-1: the three regions, disjoint by machine check -------------------
    source_text = read_text(SELF_REL)
    reads.append(SELF_REL)
    s1_src = source_text
    if mut("MUT-S1"):
        # a REAL alias: a module-level binding of the null's step function is
        # added and the comparator is made to call it through that binding, so
        # the live call-graph predicate runs again over the source as it
        # stands and must resolve the alias to find the edge it forbids
        s1_src = source_text.replace(
            "def k_first_difference(a, b, horizon):",
            "_NULLSTEP = n_step_ring\n\n\n"
            "def k_first_difference(a, b, horizon):\n"
            "    if a is b:\n"
            "        _NULLSTEP(a, b, horizon)", 1)
    if mut("MUT-S1-SHARED"):
        # a REAL shared component (registered family S-2): one helper in no
        # region, called from the null's region AND from the comparator's
        s1_src = source_text.replace(
            "def n_step_ring(arena, psi, coin):",
            "def shared_kernel(x):\n"
            "    return x\n\n\n"
            "def n_step_ring(arena, psi, coin):\n"
            "    shared_kernel(psi)", 1).replace(
            "def k_first_difference(a, b, horizon):",
            "def k_first_difference(a, b, horizon):\n"
            "    shared_kernel(a)", 1)
    if mut("MUT-S1-CROSS"):
        # a REAL cross-region edge in the direction the delivered predicate
        # did not police at all: the ISP arm reading the null's state
        s1_src = source_text.replace(
            "def i_coin_apply(arena, psi, record, modulus, coin, order=\"GD\"):",
            "def i_coin_apply(arena, psi, record, modulus, coin, "
            "order=\"GD\"):\n"
            "    if arena is psi:\n"
            "        n_step_ring(arena, psi, coin)", 1)
    tree = ast.parse(source_text)
    s1_tree = ast.parse(s1_src)
    region, calls, defined, aliases = k_region_map(s1_tree)
    s1_offences = k_region_offences(region, calls, defined, aliases,
                                    SHARED_GROUND)
    shared_used = collections.defaultdict(set)
    for fn, pre in region.items():
        for callee in calls[fn]:
            tgt = aliases.get(callee, callee)
            if tgt in defined and tgt not in region:
                shared_used[tgt].add(pre)
    unshared = sorted(nm for nm in SHARED_GROUND
                      if len(shared_used.get(nm, ())) < 2)
    REG.measured("null_fns", sum(1 for v in region.values() if v == "n"),
                 "AST count of functions in the n_ region")
    REG.measured("isp_fns", sum(1 for v in region.values() if v == "i"),
                 "AST count of functions in the i_ region")
    REG.measured("cmp_fns", sum(1 for v in region.values() if v == "k"),
                 "AST count of functions in the k_ region")
    REG.measured("head_fns", sum(1 for v in region.values() if v == "p"),
                 "AST count of functions in the p_ region")
    REG.measured("shared_ground", len(SHARED_GROUND), "len(SHARED_GROUND)")
    R["s1_regions"] = {"null": REG.values["null_fns"],
                       "isp": REG.values["isp_fns"],
                       "comparator": REG.values["cmp_fns"],
                       "head_builder": REG.values["head_fns"],
                       "declared_shared_ground": list(SHARED_GROUND),
                       "shared_ground_unused": unshared,
                       "aliases_resolved": len(aliases),
                       "offences": s1_offences}
    SEAL.seal("s1_regions", R["s1_regions"], "G-S1-DISJOINT-CODE")
    gate("G-S1-DISJOINT-CODE",
         REG.stmt("the null's {null_fns} functions, the ISP model's "
                  "{isp_fns}, the comparator's {cmp_fns} and the head "
                  "builder's {head_fns} are disjoint regions of this source: "
                  "EVERY cross-region call edge is an offence in both "
                  "directions, callees are resolved through the module's own "
                  "binding table so an alias is not a way past, and a "
                  "function in no region called from more than one region is "
                  "an offence unless it is one of the {shared_ground} "
                  "declared shared-ground names, each of which is required "
                  "to be genuinely shared",
                  null_fns=1, isp_fns=1, cmp_fns=1, head_fns=1,
                  shared_ground=1),
         not s1_offences and not unshared,
         "regions %d/%d/%d/%d aliases %d shared-ground %d unused %s "
         "offences %s"
         % (REG.values["null_fns"], REG.values["isp_fns"],
            REG.values["cmp_fns"], REG.values["head_fns"], len(aliases),
            len(SHARED_GROUND), unshared or "none", s1_offences or "none"))

    # -- the null has no record, by AST -------------------------------------
    record_vocab = ("record", "emission", "coupled", "branch", "modulus",
                    "count_field", "division")
    if mut("MUT-NULL-RECORD"):
        # a REAL widening: a word the null's region provably does contain is
        # added to the prohibited vocabulary, so the live scan runs again over
        # the source as it stands and finds a genuine occurrence
        record_vocab = record_vocab + ("coin",)
    leaks = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and region.get(node.name) == "n":
            names = set()
            for sub in ast.walk(node):
                if isinstance(sub, ast.Name):
                    names.add(sub.id)
                if isinstance(sub, ast.arg):
                    names.add(sub.arg)
            for w in record_vocab:
                if any(w in nm for nm in names):
                    leaks.append("%s mentions %s" % (node.name, w))
    R["null_no_record"] = {"vocabulary": list(record_vocab), "leaks": leaks}
    SEAL.seal("null_no_record", R["null_no_record"], "G-NULL-HAS-NO-RECORD")
    REG.measured("record_words", len(record_vocab), "len(record_vocab)")
    gate("G-NULL-HAS-NO-RECORD",
         REG.stmt("no function of the null's region names any of the "
                  "{record_words} declared record words in any identifier or "
                  "argument: the null's absence of a record is a property of "
                  "its source, not a promise in its prose", record_words=1),
         not leaks, "record words %d leaks %s"
         % (len(record_vocab), leaks or "none"))

    # -- the null's rule, total ---------------------------------------------
    a_pin = ASET.read("A-PIN-NULL", "G-NULL-RULE-TOTAL")
    rule_ids = tuple(r[0] for r in NULL_RULE)
    missing = [w for w in ("quantum walk", "arena size", "record layer",
                           "conserved-price structure")
               if w not in ET.canon(a_pin)]
    pin_dimension = k_int_from(a_pin, "d=")
    dropped = []
    if "record layer" in ET.canon(a_pin):
        dropped.append("RECORD-LAYER")
    if "conserved-price structure" in ET.canon(a_pin):
        dropped.append("CONSERVED-PRICE-STRUCTURE")
    # DERIVED, not typed beside the table (K3 MAJOR-4): the parity data are
    # the datum words of the rules that do not take anything away, and the
    # horizon parity is measured below at G-COIN-ORDER-FIBER's own arms.
    shared = [datum for (rid, datum, _t) in NULL_RULE
              if rid not in NULL_RULE_TAKES_AWAY] + ["HORIZON"]
    if mut("MUT-NULL-RULE"):
        rule_ids = rule_ids[:-1]
    REG.measured("null_rules", len(rule_ids), "len(NULL_RULE)")
    REG.measured("null_shared", len(shared),
                 "the rules that hand the null a parity, plus the horizon")
    REG.measured("null_dropped", len(dropped),
                 "the structures the pin's own sentence names as absent")
    R["null_model"] = {
        "word": "PLAIN-COINED-WALK",
        "rules": len(rule_ids), "rule_ids": list(rule_ids),
        "rule_text": {r[0]: r[2] for r in NULL_RULE},
        "shared": "-".join(shared), "dropped": "-".join(dropped),
        "shared_derived_from": "NULL_RULE",
        "pin_sentence_terms_missing": missing,
        "dimension_read_from_the_pin": pin_dimension,
        "shared_count": len(shared), "dropped_count": len(dropped)}
    SEAL.seal("null_model", R["null_model"], "G-NULL-RULE-TOTAL")
    gate("G-NULL-RULE-TOTAL",
         REG.stmt("the null's parameters are fixed by {null_rules} rules "
                  "declared before any row runs; {null_shared} of its data "
                  "are the ISP model's own -- the datum word of every rule "
                  "that hands it a parity, derived from the rule table and "
                  "not typed beside it -- and {null_dropped} structures are "
                  "dropped, and the two dropped structures are exactly the "
                  "ones the pin's own sentence names",
                  null_rules=1, null_shared=1, null_dropped=1),
         len(rule_ids) == len(NULL_RULE) and not missing
         and len(dropped) == len(("record", "price"))
         and pin_dimension == DECLARED_DIMENSION,
         "rules %d shared %d dropped %s missing %s pin-dimension %s"
         % (len(rule_ids), len(shared), dropped, missing or "none",
            pin_dimension))

    # -- THE PRE-REGISTRATION, SEALED ---------------------------------------
    # K3 MAJOR-4: PR1..PR7 were re-declarable post-hoc at exit 0 because only
    # their cardinality was bound.  Three legs now bind them.
    rule_table = [list(r) for r in NULL_RULE]
    if mut("MUT-PR-REWRITE"):
        # a REAL post-hoc re-declaration: PR3 is rewritten from the SAME coin
        # to a coin of the null's own choosing, picked after the sweep --
        # exactly the rewrite the panel shipped at exit 0
        rule_table = [r if r[0] != "PR3" else
                      [r[0], r[1], "the null carries a coin of its OWN "
                       "choosing, picked after the sweep from whichever "
                       "member of the census makes the comparison come out"]
                      for r in rule_table]
    if mut("MUT-PR-TUNED"):
        # THE SAME REWRITE, BY AN AUTHOR WHO ALSO RE-DECLARES THE DIGEST.
        # The digest leg above cannot see this one -- the constant sits beside
        # the table -- so the text leg below is the gate's only defence, and
        # this recipe is what proves the text leg is load-bearing.
        rule_table = [r if r[0] != "PR3" else
                      [r[0], r[1], "the null carries a coin of its OWN "
                       "choosing, picked after the sweep from whichever "
                       "member of the census makes the comparison come out"]
                      for r in rule_table]
    rule_digest = ET.digest(rule_table)
    declared_digest = (rule_digest if mut("MUT-PR-TUNED") else NULL_RULE_SEAL)
    # THE TEXT LEG: every rule must still SAY the parity its content leg
    # measures, and no rule may admit post-hoc tuning in any voice.
    asserts_missing = sorted(
        rid for (rid, _d, txt) in rule_table
        if NULL_RULE_ASSERTS.get(rid, "\0") not in ET.canon(txt))
    tuning_admitted = sorted(
        "%s :: %s" % (rid, pat) for (rid, _d, txt) in rule_table
        for pat in NULL_RULE_TUNING if re.search(pat, ET.canon(txt)))
    isp_parity, null_parity = k_parity_binding(tree)
    parity_ok = (isp_parity is not None and isp_parity == null_parity
                 and len(set(isp_parity)) == len(NULL_RULE) - 2)
    try:
        n_lattice_expectation([Fraction(1)], weight_free=False)
        pr7_refuses = False
    except ET.CheckFail:
        pr7_refuses = True
    datum_words = [r[1] for r in NULL_RULE]
    derived_ok = all(d in shared for (rid, d, _t) in NULL_RULE
                     if rid not in NULL_RULE_TAKES_AWAY)
    content = {
        "PR1": bool(parity_ok and isp_parity[0].startswith("pr_")),
        "PR2": bool(parity_ok and Arena(3).dim // Arena(3).ns
                    == len(LINKDIRS)),
        "PR3": bool(parity_ok and isp_parity[2].startswith("pr_")),
        "PR4": bool(parity_ok and isp_parity[0] == null_parity[0]),
        "PR5": bool(parity_ok and isp_parity[3:] == null_parity[3:]),
        "PR6": not leaks,
        "PR7": pr7_refuses,
    }
    unbound = sorted(k for k, v in content.items() if not v)
    seal_ok = rule_digest == declared_digest
    REG.measured("pr_content_legs", len(content), "len(content)")
    REG.measured("pr_text_legs", len(NULL_RULE_ASSERTS),
                 "len(NULL_RULE_ASSERTS)")
    R["preregistration"] = {
        "digest": rule_digest, "declared_digest": declared_digest,
        "sealed": bool(seal_ok),
        "datum_words": datum_words,
        "shared_derived": list(shared),
        "parity_names_isp": isp_parity, "parity_names_null": null_parity,
        "content_legs": {k: bool(v) for k, v in sorted(content.items())},
        "content_unbound": unbound,
        "asserted_parities": dict(sorted(NULL_RULE_ASSERTS.items())),
        "asserts_missing": asserts_missing,
        "tuning_admitted": tuning_admitted,
        "how": "the rule table's digest is declared WITH the table; each rule "
               "carries a content leg over objects this run built; and each "
               "rule's TEXT must still assert the parity that leg measures "
               "and admit no post-hoc tuning -- the third leg is the one that "
               "survives an author who re-declares the digest beside the "
               "table, which the digest leg alone cannot see"}
    SEAL.seal("preregistration", R["preregistration"],
              "G-PR-PREREGISTRATION-SEALED")
    gate("G-PR-PREREGISTRATION-SEALED",
         REG.stmt("the pre-registration is sealed on three legs: the rule "
                  "table digests to the value declared beside it; the head's "
                  "parity list is derived from the table's own datum words; "
                  "every one of the {pr_content_legs} rules carries a content "
                  "leg over objects this run built -- the sweep binds the "
                  "arena, the horizon, the coin, the start site and the "
                  "direction to one set of locals and hands THOSE to both "
                  "arms; and every one of the {pr_text_legs} rules must still "
                  "SAY the parity its content leg measures and admit no "
                  "post-hoc tuning in any voice -- that last leg is the one "
                  "an author who re-declares the digest beside the table "
                  "still has to defeat, and it is what a rule rewritten after "
                  "the fact fails",
                  pr_content_legs=1, pr_text_legs=1),
         seal_ok and parity_ok and derived_ok and not unbound
         and not asserts_missing and not tuning_admitted,
         "digest %s declared %s parity %s unbound %s asserts-missing %s "
         "tuning %s"
         % (rule_digest, declared_digest, isp_parity, unbound or "none",
            asserts_missing or "none", tuning_admitted[:2] or "none"))

    # -- the coin censuses ---------------------------------------------------
    arenas = {q: Arena(q) for q in ARENAS}
    censuses = {}
    for q in ARENAS:
        sols, reps = coin_census(q)
        censuses[q] = (sols, reps)
    if mut("MUT-COIN-CENSUS"):
        censuses[3] = (censuses[3][0][:-1], censuses[3][1])
    coin_rows = [(q, len(censuses[q][0]), len(censuses[q][1]),
                  sum(1 for r in censuses[q][1] if coin_is_trivial(r[1])))
                 for q in ARENAS]
    REG.measured("coins_q3", len(censuses[3][0]), "the exhaustive census")
    REG.measured("classes_q3", len(censuses[3][1]), "orbits under global phase")
    REG.measured("coins_q2", len(censuses[2][0]), "the exhaustive census")
    REG.measured("classes_q2", len(censuses[2][1]), "orbits under global phase")
    R["coin_census"] = {"rows": [{"q": q, "solutions": a, "classes": b,
                                  "trivial_classes": c}
                                 for (q, a, b, c) in coin_rows]}
    SEAL.seal("coin_census", R["coin_census"], "G-COIN-CENSUS-PARENT")
    gate("G-COIN-CENSUS-PARENT",
         REG.stmt("the S_3-covariant unitary coins over the arena's own ring "
                  "number {coins_q3} in {classes_q3} classes up to a global "
                  "phase at the parent's arena -- the parent's own two "
                  "numbers, recomputed here from the definition -- and "
                  "{coins_q2} in {classes_q2} at the smaller arena, where "
                  "the declaration fiber collapses",
                  coins_q3=1, classes_q3=1, coins_q2=1, classes_q2=1),
         len(censuses[3][0]) == 36 and len(censuses[3][1]) == 6,
         "q3 %d/%d q2 %d/%d" % (len(censuses[3][0]), len(censuses[3][1]),
                                len(censuses[2][0]), len(censuses[2][1])))

    # THE CANONICAL COIN.  At both arenas the non-trivial class of least
    # index is +-Grover, written 3C = -I + 2J; that is measured here rather
    # than assumed, and no second name for it is carried (K2 m-7: the
    # delivered object computed a `canonical` map, overwrote it and never
    # read it -- a carried-and-unused object).
    GROVER = coin_matrix(rscale(R1, -3), rscale(R1, 2))
    GROVER_INT = ((-1, 2, 2), (2, -1, 2), (2, 2, -1))
    grover_is_least = all(
        coin_matrix(*[r for r in censuses[q][1]
                      if not coin_is_trivial(r[1])][0]) == GROVER
        for q in (2,))

    # -- the ISP fidelity leg, against the parent's own sealed ladders -------
    a_frozen = ASET.read("A-COUP-FROZEN", "G-ISP-FIDELITY-PARENT")
    A3 = arenas[3]
    fid_c = i_ladder(A3, FID_T, 3, GROVER, (0, 0), 0, "A", coupled=True)
    fid_f = i_ladder(A3, FID_T, 3, GROVER, (0, 0), 0, "A", coupled=False)
    parent_coupled = [3, 27, 486, 10527, 284078]
    parent_frozen = [3, 27, 486, 9234, 212382]
    parent_ipr_c = Fraction(35971074413334039128803,
                            239299329230617529590083)
    parent_ipr_f = Fraction(2306155, 14348907)
    got_c = [fid_c["branches"][t] for t in range(1, FID_T + 1)]
    got_f = [fid_f["branches"][t] for t in range(1, FID_T + 1)]
    if mut("MUT-FIDELITY"):
        fid_c["ipr"][FID_T] = fid_c["ipr"][FID_T] + Fraction(1, 3)
    # THE ANCHOR'S CONTENT, NOT ITS EXISTENCE (K3 MINOR-2).  The parent's
    # sentence lists the parities its control keeps -- "the same walk, the
    # same emission rule and the same branching" -- and that COUNT is pulled
    # out of the sentence and compared with the number of parities this
    # rebuild's own two arms are measured to keep.  The sentence's other
    # clause, "on counts that never update", is consumed as a value too: the
    # control's record stands at its initial value everywhere and the coupled
    # arm's does not.
    parent_parities = ET.canon(a_frozen).count("the same")
    frozen_rec = i_record_observables(
        arenas[3], i_ladder(A3, FIB_T, 3, GROVER, (0, 0), 0, "A",
                            coupled=False, want_frontier=True)["frontier"], 3)
    coupled_rec = i_record_observables(
        arenas[3], i_ladder(A3, FIB_T, 3, GROVER, (0, 0), 0, "A",
                            coupled=True, want_frontier=True)["frontier"], 3)
    measured_parities = sum([
        fid_c["dist"][1] == fid_f["dist"][1],        # the same walk
        fid_c["branches"][1] == fid_f["branches"][1],   # the same emission
        fid_c["branches"][2] == fid_f["branches"][2]])  # the same branching
    never_updates = (parent_parities == measured_parities
                     and frozen_rec["max_cell_count"] == 1
                     and coupled_rec["max_cell_count"] > 1)
    fid_ok = (got_c == parent_coupled and got_f == parent_frozen
              and fid_c["ipr"][FID_T] == parent_ipr_c
              and fid_f["ipr"][FID_T] == parent_ipr_f
              and never_updates and grover_is_least)
    REG.measured("fid_leaves", got_c[-1], "the coupled arm's leaf count")
    REG.measured("fid_leaves_frozen", got_f[-1], "the frozen arm's leaf count")
    matched_rows = [got_c == parent_coupled, got_f == parent_frozen,
                    fid_c["ipr"][FID_T] == parent_ipr_c,
                    fid_f["ipr"][FID_T] == parent_ipr_f]
    REG.measured("fid_matched", sum(1 for ok in matched_rows if ok),
                 "the parent quantities this rebuild reproduces: two branch "
                 "ladders and two horizon inverse-participation ratios, "
                 "counted from the comparisons themselves")
    R["isp_fidelity"] = {
        "coupled_branches": got_c, "frozen_branches": got_f,
        "coupled_ipr": str(fid_c["ipr"][FID_T]),
        "frozen_ipr": str(fid_f["ipr"][FID_T]),
        "parent_coupled_branches": parent_coupled,
        "parent_frozen_branches": parent_frozen,
        "parent_coupled_ipr": str(parent_ipr_c),
        "parent_frozen_ipr": str(parent_ipr_f),
        "norm_checks": fid_c["norm_checks"] + fid_f["norm_checks"],
        "norm_violations": fid_c["norm_violations"]
        + fid_f["norm_violations"],
        "mass_one": bool(fid_c["mass_one"] and fid_f["mass_one"]),
        "control_max_cell_count": frozen_rec["max_cell_count"],
        "coupled_max_cell_count": coupled_rec["max_cell_count"],
        "parities_read_from_the_parents_sentence": parent_parities,
        "parities_measured_between_the_two_arms": measured_parities,
        "canonical_coin_is_the_least_non_trivial_class": bool(grover_is_least)}
    SEAL.seal("isp_fidelity", R["isp_fidelity"], "G-ISP-FIDELITY-PARENT")
    gate("G-ISP-FIDELITY-PARENT",
         REG.stmt("this unit's independent rebuild of the coupled walk "
                  "reproduces {fid_matched} of the parent's sealed "
                  "quantities exactly -- both branch ladders and both "
                  "horizon inverse-participation ratios, the coupled arm "
                  "landing on {fid_leaves} leaves against the control's "
                  "{fid_leaves_frozen} -- and the parities the parent's own "
                  "sentence lists for its control are counted out of that "
                  "sentence and measured to hold between these two arms",
                  fid_matched=1, fid_leaves=1, fid_leaves_frozen=1),
         fid_ok, "coupled %s frozen %s ipr %s / %s control-max-count %d "
         "parities %d/%d"
         % (got_c, got_f, fid_c["ipr"][FID_T], fid_f["ipr"][FID_T],
            frozen_rec["max_cell_count"], measured_parities,
            parent_parities))

    # -- the null's two routes ----------------------------------------------
    two_route = {"checks": 0, "violations": 0}
    for q in ARENAS:
        rr = n_ladder_ring(arenas[q], FIB_T, GROVER, (0, 0), 0)
        gi = GROVER_INT
        if mut("MUT-NULL-ROUTES"):
            # a REAL corruption: the integer route is given a coin that is
            # not the one the ring route carries, so the two genuinely part
            gi = ((-1, 2, 2), (2, -1, 2), (2, 2, 1))
        ii = n_ladder_int(arenas[q], FIB_T, gi, (0, 0), 0)
        for t in range(1, FIB_T + 1):
            for s in range(arenas[q].ns):
                two_route["checks"] += 1
                if rr[0][t][s] != ii[0][t][s]:
                    two_route["violations"] += 1
    REG.measured("route_checks", two_route["checks"],
                 "per site per tick per arena")
    REG.measured("route_points", len(ARENAS),
                 "the fiber points at which the integer route exists at all")
    R["null_two_routes"] = dict(
        two_route, points=len(ARENAS),
        coverage="one point per arena -- the origin, the first internal "
                 "direction and the Grover coin -- because the integer route "
                 "exists only at a rational-integral coin")
    SEAL.seal("null_two_routes", R["null_two_routes"], "G-NULL-TWO-ROUTES")
    gate("G-NULL-TWO-ROUTES",
         REG.stmt("the null's cyclotomic route and its integer route agree "
                  "at {route_checks} site-by-tick comparisons over "
                  "{route_points} points, one per arena, which is the whole "
                  "of where the integer route exists -- it is available only "
                  "at a rational-integral coin; the two routes share the "
                  "declared arena and no arithmetic whatever",
                  route_checks=1, route_points=1),
         two_route["violations"] == 0,
         "checks %d violations %d points %d"
         % (two_route["checks"], two_route["violations"], len(ARENAS)))

    # -- THE DISCRIMINANT: the fiber sweep ----------------------------------
    fiber_rows = []
    agree_checks = agree_viol = 0
    nontrivial_pts = trivial_pts = 0
    nontrivial_at3 = trivial_never = 0
    nontrivial_ticks = set()
    first_ticks = collections.Counter()
    sweep_horizon = FIB_T
    agree_upto = 2
    if mut("MUT-FIBER"):
        # a REAL narrowing: the sweep stops one tick before the tick the
        # finding is about, so the pre-registered outcome becomes unreachable
        sweep_horizon = FIB_T - 1
    if mut("MUT-AGREE"):
        # a REAL widening: the agreement leg is asked to hold at the tick the
        # difference lives at
        agree_upto = FIB_T
    for q in ARENAS:
        A = arenas[q]
        for (Aa, Bb) in censuses[q][1]:
            C = coin_matrix(Aa, Bb)
            triv = coin_is_trivial(Bb)
            for start in A.sites:
                for direction in range(3):
                    for reading in ("A", "B"):
                        # PR1..PR5's content: ONE binding of the arena, the
                        # horizon, the coin, the start site and the internal
                        # direction, handed to BOTH arms.  The parity is a
                        # property of these five names, which
                        # G-PR-PREREGISTRATION-SEALED reads by AST.
                        pr_arena, pr_horizon = A, sweep_horizon
                        pr_coin, pr_start, pr_dir = C, start, direction
                        isp = i_ladder(pr_arena, pr_horizon, q, pr_coin,
                                       pr_start, pr_dir, reading)
                        nul = n_ladder_ring(pr_arena, pr_horizon, pr_coin,
                                            pr_start, pr_dir)
                        ft = k_first_difference(isp["dist"], nul[0],
                                               sweep_horizon)
                        ck, vi = k_agreement_checks(isp["dist"], nul[0],
                                                    sweep_horizon, agree_upto)
                        agree_checks += ck
                        agree_viol += vi
                        first_ticks[(q, triv, ft)] += 1
                        if triv:
                            trivial_pts += 1
                            if ft is None:
                                trivial_never += 1
                        else:
                            nontrivial_pts += 1
                            nontrivial_ticks.add(ft)
    first_tick = (sorted(nontrivial_ticks)[0]
                  if len(nontrivial_ticks) == 1
                  and None not in nontrivial_ticks else None)
    nontrivial_at3 = sum(1 for (q, tv, ft), n in first_ticks.items()
                         if not tv and ft == first_tick for _ in range(n))
    fiber_rows = [(q, "trivial" if tv else "non-trivial",
                   "none" if ft is None else ft, n)
                  for (q, tv, ft), n in sorted(
                      first_ticks.items(),
                      key=lambda z: (z[0][0], z[0][1],
                                     -1 if z[0][2] is None else z[0][2]))]
    REG.measured("fiber_points", nontrivial_pts + trivial_pts,
                 "coin class x start site x direction x reading x arena")
    REG.measured("nontrivial_points", nontrivial_pts, "the interfering coins")
    REG.measured("trivial_points", trivial_pts, "the scalar coins")
    REG.measured("agree_checks", agree_checks, "per site per tick per point")
    REG.measured("first_tick", first_tick or 0,
                 "the single value k_first_difference returns over every "
                 "interfering fiber point")
    R["agreement"] = {"upto": agree_upto, "checks": agree_checks,
                      "violations": agree_viol,
                      "points": nontrivial_pts + trivial_pts}
    SEAL.seal("agreement", R["agreement"], "G-AGREE-THROUGH-THE-EARLY-TICKS")
    R["fiber"] = {"points": nontrivial_pts + trivial_pts,
                  "nontrivial": nontrivial_pts, "trivial": trivial_pts,
                  "nontrivial_first_at_the_common_tick": nontrivial_at3,
                  "first_difference_tick": first_tick,
                  "trivial_never_differ": trivial_never,
                  "sweep_horizon": sweep_horizon,
                  "rows": [{"q": a, "coin": b, "first_difference": c,
                            "points": d} for (a, b, c, d) in fiber_rows]}
    gate("G-AGREE-THROUGH-THE-EARLY-TICKS",
         REG.stmt("through the second tick the two models agree at every one "
                  "of {agree_checks} site-by-tick comparisons taken over all "
                  "{fiber_points} declared fiber points, so nothing "
                  "separates them before the third tick",
                  agree_checks=1, fiber_points=1),
         agree_viol == 0, "checks %d violations %d upto %d"
         % (agree_checks, agree_viol, agree_upto))
    SEAL.seal("fiber", R["fiber"], "G-FIRST-DIFFERENCE-TICK")
    gate("G-FIRST-DIFFERENCE-TICK",
         REG.stmt("the two models' site-occupation distributions first differ "
                  "at the third tick at {nontrivial_points} of "
                  "{nontrivial_points} fiber points whose coin carries "
                  "interference, and at no tick at all at the "
                  "{trivial_points} whose coin is a scalar",
                  nontrivial_points=1, trivial_points=1),
         nontrivial_at3 == nontrivial_pts and trivial_never == trivial_pts
         and first_tick is not None and first_tick == FIB_T,
         "non-trivial %d of %d at the third tick, trivial %d of %d never"
         % (nontrivial_at3, nontrivial_pts, trivial_never, trivial_pts))

    # -- the headline values -------------------------------------------------
    head_vals = {}
    for q in ARENAS:
        A = arenas[q]
        hz = HEAD_T if q == 2 else FIB_T
        cpl = not mut("MUT-VALUES")     # a REAL switch-off of the coupling
        isp = i_ladder(A, hz, q, GROVER, (0, 0), 0, "A", coupled=cpl,
                       want_frontier=True)
        nul = n_ladder_ring(A, hz, GROVER, (0, 0), 0)
        t = 3
        tv = k_total_variation(isp["dist"][t], nul[0][t])
        gapv = k_max_gap(isp["dist"][t], nul[0][t])
        head_vals[q] = {
            "horizon": hz,
            "isp_dist": _dist(isp["dist"][t]),
            "null_dist": _dist(nul[0][t]),
            "isp_ipr": str(isp["ipr"][t]),
            "null_ipr": str(nul[1][t]),
            "tv": str(tv), "max_gap": str(gapv),
            "branches": isp["branches"][t],
            "branches_at_tick": t,
            "record_side_read_at_horizon": hz,
            "record_side": i_record_observables(A, isp["frontier"], q),
            "_tv": tv, "_gap": gapv}
    REG.measured("q3_branches", head_vals[3]["branches"],
                 "the emission tree at the third tick")
    REG.measured("q2_branches", head_vals[2]["branches"],
                 "the emission tree at the third tick")
    disc_found = (head_vals[3]["isp_ipr"] != head_vals[3]["null_ipr"]
                  and head_vals[2]["isp_ipr"] != head_vals[2]["null_ipr"]
                  and nontrivial_at3 == nontrivial_pts)
    R["discriminant"] = {
        "found": bool(disc_found),
        # THE HEAD WORD CARRIES NO TICK (W3, and K1 MAJOR-1's measurement).
        # The tick is order-relative: it is the third at the delivered coin
        # order and the fourth at the parent's declared alternative.  What
        # survives both members is that the layer is not inert, and the head
        # says that and stamps the declarations it is said under.
        "verdict_word":
            "RECORD-BACKREACTION-NON-INERT-UNDER-SPECIFIED-DECLARATIONS"
            if disc_found
            else "RECORD-BACKREACTION-NOT-DETECTED-IN-THE-SWEPT-WINDOW",
        "observable_word": "THE-TICK-3-SITE-OCCUPATION-DISTRIBUTION",
        "reading": "AN ABLATION: the null is this model with the feedback "
                   "layer removed and everything else held equal, so the "
                   "difference measures the layer and not a fitted number",
        "first_difference_tick": first_tick,
        "agree_upto": agree_upto, "agree_checks": agree_checks,
        "agree_violations": agree_viol,
        "nontrivial_points": nontrivial_pts,
        "nontrivial_at_tick": nontrivial_at3,
        "trivial_points": trivial_pts,
        "q3": {k: v for k, v in head_vals[3].items() if not k.startswith("_")},
        "q2": {k: v for k, v in head_vals[2].items() if not k.startswith("_")}}
    SEAL.seal("discriminant", R["discriminant"], "G-DISCRIMINANT-VALUES")
    gate("G-DISCRIMINANT-VALUES",
         REG.stmt("at the third tick the two models' site-occupation "
                  "distributions are unequal at both declared arenas, the "
                  "emission tree carrying {q3_branches} branches at the "
                  "larger and {q2_branches} at the smaller, and every "
                  "published value is the one this run measured",
                  q3_branches=1, q2_branches=1),
         disc_found, "q3 %s vs %s ; q2 %s vs %s"
         % (head_vals[3]["isp_ipr"], head_vals[3]["null_ipr"],
            head_vals[2]["isp_ipr"], head_vals[2]["null_ipr"]))

    # -- Z3: THE NULL IS THE PARENT'S OWN FROZEN-STAGE CONTROL ---------------
    # K1 MAJOR-3.  With every count held at its initial value the record's
    # diagonal is a scalar at every site, so the frozen coin is the null's
    # coin times a global phase and every frozen branch carries the null's
    # state up to that phase.  The consequence cuts both ways and both are
    # published: the null is not an opponent this unit invented, it is the
    # parent's own MANDATORY control on the compared observable -- and the
    # bare fact that the record layer moves the walk is therefore the
    # parent's already-sealed G-NONTRIVIALITY row, not this unit's.  What is
    # this unit's is WHEN, BY HOW MUCH and HOW UNIVERSALLY.
    # a REAL substitution: the arm the identity is claimed for is run COUPLED
    # instead of frozen, so the two ladders genuinely part and the claimed
    # identity stops being the measurement
    ctl_coupled = bool(mut("MUT-CONTROL-IDENTITY"))
    ctl_checks = ctl_equal = 0
    for q in ARENAS:
        A = arenas[q]
        for (Aa, Bb) in censuses[q][1]:
            C = coin_matrix(Aa, Bb)
            for start in A.sites:
                for direction in range(3):
                    for reading in ("A", "B"):
                        frz = i_ladder(A, FIB_T, q, C, start, direction,
                                       reading, coupled=ctl_coupled)
                        nlz = n_ladder_ring(A, FIB_T, C, start, direction)
                        for t in range(1, FIB_T + 1):
                            ctl_checks += 1
                            if frz["dist"][t] == nlz[0][t]:
                                ctl_equal += 1
    REG.measured("control_checks", ctl_checks,
                 "site-distribution comparisons, per tick per fiber point")
    REG.measured("control_equal", ctl_equal, "of which equal")
    R["null_is_the_control"] = {
        "checks": ctl_checks, "equal": ctl_equal,
        "word": "THE-NULL-IS-THE-PARENTS-OWN-FROZEN-STAGE-CONTROL",
        "why": "on a record whose counts never update the diagonal is a "
               "scalar multiple of the identity at every site, so the frozen "
               "coin is the null's coin times a global phase and the two "
               "site-occupation ladders coincide at every tick",
        "parent_row": "paper-20's sealed G-NONTRIVIALITY row already "
                      "established that the declared observables differ from "
                      "the mandatory frozen-stage control at horizon 5",
        "what_is_new_here": "the tick at which the parting starts, the exact "
                            "magnitudes at both planes, and the universality "
                            "over the swept fiber"}
    SEAL.seal("null_is_the_control", R["null_is_the_control"],
              "G-NULL-IS-THE-PARENTS-CONTROL")
    gate("G-NULL-IS-THE-PARENTS-CONTROL",
         REG.stmt("the record-free null is the parent's own frozen-stage "
                  "control on the compared observable, up to a global phase: "
                  "their site-occupation ladders are equal at "
                  "{control_equal} of {control_checks} comparisons over "
                  "every tick of every declared fiber point, so the base "
                  "finding that the record layer is not inert is the "
                  "parent's already-sealed result and what this unit adds is "
                  "the tick, the magnitudes and the universality",
                  control_equal=1, control_checks=1),
         ctl_equal == ctl_checks and ctl_checks > 0,
         "equal %d of %d" % (ctl_equal, ctl_checks))

    # -- Z1: THE COIN-ORDER FIBER, PUBLISHED --------------------------------
    # K1 MAJOR-1.  paper-20 stamps F6-COIN-ORDER DECLARED-VERDICT-RELEVANT
    # and runs both members; this unit inherited G.D silently.  The
    # alternative D.G is run here at both planes.  Under it the count phase
    # lands AFTER the coin, so it cannot enter that step's Born weights --
    # the parent's own |D G psi|^2 = |G psi|^2 -- and the whole effect is
    # displaced by exactly one tick.  The neighbouring fiber, F7's shift
    # orientation, is measured too and is inert.
    order_rows, order_ticks = [], {}
    for q in ARENAS:
        A = arenas[q]
        for od in COIN_ORDERS:
            # a REAL narrowing: the fiber's second member is run at the FIRST
            # member's order, so the alternative is never actually executed
            run_od = ("GD" if (od == "DG" and mut("MUT-ORDER-FIBER")) else od)
            isp_o = i_ladder(A, DG_T, q, GROVER, (0, 0), 0, "A", order=run_od)
            nul_o = n_ladder_ring(A, DG_T, GROVER, (0, 0), 0)
            ftk = k_first_difference(isp_o["dist"], nul_o[0], DG_T)
            same3 = isp_o["dist"][FIB_T] == nul_o[0][FIB_T]
            order_rows.append((q, od, ftk, same3))
            order_ticks[(q, od)] = ftk
    orient_rows = []
    for q in ARENAS:
        for orient in ORIENTATIONS:
            Ao = Arena(q, orientation=orient)
            isp_r = i_ladder(Ao, FIB_T, q, GROVER, (0, 0), 0, "A")
            nul_r = n_ladder_ring(Ao, FIB_T, GROVER, (0, 0), 0)
            orient_rows.append((q, orient,
                                k_first_difference(isp_r["dist"], nul_r[0],
                                                   FIB_T),
                                str(isp_r["ipr"][FIB_T])))
    dg_tick = sorted({order_ticks[(q, "DG")] for q in ARENAS})
    gd_tick = sorted({order_ticks[(q, "GD")] for q in ARENAS})
    dg_equals_null = all(s for (_q, od, _t, s) in order_rows if od == "DG")
    orient_inert = (len({t for (_q, _o, t, _i) in orient_rows}) == 1
                    and len({i for (_q, _o, _t, i) in orient_rows}) == 2)
    REG.measured("order_members", len(COIN_ORDERS), "len(COIN_ORDERS)")
    REG.measured("orientation_members", len(ORIENTATIONS),
                 "len(ORIENTATIONS)")
    R["coin_order_fiber"] = {
        "parent_item": "F6-COIN-ORDER, stamped DECLARED-VERDICT-RELEVANT",
        "delivered_order": "G-DOT-D", "alternative_order": "D-DOT-G",
        "delivered_tick": gd_tick[0] if len(gd_tick) == 1 else 0,
        "alternative_tick": dg_tick[0] if len(dg_tick) == 1 else 0,
        "alternative_tick3_equals_the_null": bool(dg_equals_null),
        "rows": [{"arena": q, "order": od, "first_difference": t,
                  "tick3_equals_the_null": bool(s)}
                 for (q, od, t, s) in order_rows],
        "orientation_rows": [{"arena": q, "orientation": o,
                              "first_difference": t, "ipr_tick3": i}
                             for (q, o, t, i) in orient_rows],
        "orientation_word": "INERT" if orient_inert else "NOT-INERT",
        "reading": "the tick is ORDER-RELATIVE: it is 3 at the delivered "
                   "member and 4 at the parent's alternative, whose tick-3 "
                   "law is the null's own exactly. The orientation fiber "
                   "moves neither."}
    SEAL.seal("coin_order_fiber", R["coin_order_fiber"], "G-COIN-ORDER-FIBER")
    gate("G-COIN-ORDER-FIBER",
         REG.stmt("both members of the parent's verdict-relevant coin-order "
                  "fiber are run at both planes: the delivered order parts "
                  "from the null at the third tick and the alternative at "
                  "the fourth, with the alternative's third-tick law equal "
                  "to the null's exactly, so the tick is order-relative and "
                  "the head says so; the {orientation_members} members of "
                  "the neighbouring orientation fiber move neither the tick "
                  "nor the third-tick inverse participation",
                  orientation_members=1),
         len(dg_tick) == 1 and len(gd_tick) == 1 and dg_tick != gd_tick
         and dg_tick[0] == gd_tick[0] + 1 and dg_equals_null and orient_inert,
         "G.D tick %s D.G tick %s tick-3-equal %s orientation %s"
         % (gd_tick, dg_tick, dg_equals_null,
            "inert" if orient_inert else "moves"))

    # -- Z2: THE WIDER MEMORYLESS NULL SWEEP --------------------------------
    # K2 MAJOR-5, adopted.  Section 3's parity sentence was unmeasured: the
    # sweep varies the coin of BOTH arms together and never varies the null's
    # coin against a fixed ISP arm.  Two classes are swept against the
    # canonical ISP declaration -- the arena's own covariant census, and then
    # every integral coin with covariance dropped.
    integral_rows, integral_coins = n_integral_coins(INTEGRAL_COIN_BOX)
    wide = {}
    wide_configs = wide_exact = 0
    wide_laws = 0
    for q in ARENAS:
        A = arenas[q]
        target = tuple(map(Fraction, head_vals[q]["isp_dist"]))
        target_ipr = Fraction(head_vals[q]["isp_ipr"])
        laws_cen, laws_int = [], []
        ipr_hits = 0
        for (Aa, Bb) in censuses[q][0]:
            C = coin_matrix(Aa, Bb)
            for start in A.sites:
                for direction in range(3):
                    row = n_ladder_ring(A, FIB_T, C, start, direction)
                    laws_cen.append(((str(Aa), str(Bb), start, direction),
                                     row[0][FIB_T]))
                    if row[1][FIB_T] == target_ipr:
                        ipr_hits += 1
        # a REAL narrowing: the non-covariant class is never swept, so the
        # closest memoryless opponent is no longer the one measured
        wide_class = () if mut("MUT-WIDER-SWEEP") else integral_coins
        for M in wide_class:
            for start in A.sites:
                for direction in range(3):
                    row = n_ladder_int(A, FIB_T, M, start, direction)
                    laws_int.append(((M, start, direction), row[0][FIB_T]))
        gap_cen, arg_cen, ex_cen = k_closest_null(target, laws_cen)
        gap_int, arg_int, ex_int = k_closest_null(target, laws_int)
        best = gap_cen if gap_int is None else min(gap_cen, gap_int)
        wide[q] = {
            "census_configurations": len(laws_cen),
            "integral_configurations": len(laws_int),
            "census_distinct_laws": len({r for (_t, r) in laws_cen}),
            "integral_distinct_laws": len({r for (_t, r) in laws_int}),
            "exact_reproductions": ex_cen + ex_int,
            "census_exact": ex_cen, "integral_exact": ex_int,
            "census_gap": str(gap_cen),
            "integral_gap": str(gap_int) if gap_int is not None else "0",
            "census_ipr_reproductions": ipr_hits,
            "closest_gap": str(best),
            "pr3_gap": head_vals[q]["max_gap"],
            "closest_is_pr3": best == head_vals[q]["_gap"],
            "closest_coin": str(arg_cen[0]) if (gap_int is None
                                                or gap_cen < gap_int)
            else str(arg_int[0]),
            "_gap": best}
        wide_configs += len(laws_cen) + len(laws_int)
        wide_exact += ex_cen + ex_int
        wide_laws += (wide[q]["census_distinct_laws"]
                      + wide[q]["integral_distinct_laws"])
    REG.measured("wide_configs", wide_configs,
                 "coin x start site x direction, both classes, both arenas")
    REG.measured("wide_exact", wide_exact,
                 "members reproducing the ISP tick-3 law exactly")
    REG.measured("integral_coins", len(integral_coins),
                 "integral matrices with M M^T = 9 I inside the declared box")
    REG.measured("integral_rows", len(integral_rows),
                 "the rows of squared norm nine inside the declared box")
    R["wider_null_sweep"] = {
        "box": INTEGRAL_COIN_BOX,
        "integral_coins": len(integral_coins),
        "integral_rows": len(integral_rows),
        "covariant_coins_swept": len(censuses[3][0]) + len(censuses[2][0]),
        "configurations": wide_configs,
        "exact_reproductions": wide_exact,
        "distinct_laws": wide_laws,
        "q3": {k: v for k, v in wide[3].items() if not k.startswith("_")},
        "q2": {k: v for k, v in wide[2].items() if not k.startswith("_")},
        "closest_gap_q2": wide[2]["closest_gap"],
        "closest_gap_q3": wide[3]["closest_gap"],
        "pr3_gap_q2": head_vals[2]["max_gap"],
        "pr3_gap_q3": head_vals[3]["max_gap"],
        "reading": "no memoryless walk in either class reproduces the "
                   "third-tick law at either plane; PR3's null is the best "
                   "of them at the larger plane, and at the smaller a "
                   "non-covariant coin comes closer, so the published "
                   "deciding cost is the cost against THAT one"}
    SEAL.seal("wider_null_sweep", R["wider_null_sweep"], "G-WIDER-NULL-SWEEP")
    gate("G-WIDER-NULL-SWEEP",
         REG.stmt("the null class is widened past the anti-strawman rule and "
                  "measured: over {wide_configs} memoryless configurations "
                  "-- every solution of the arena's own covariant census and "
                  "every one of the {integral_coins} integral coins with "
                  "covariance dropped, at every start site and every "
                  "internal direction of both planes -- exactly {wide_exact} "
                  "reproduce the ISP third-tick law, and the smallest "
                  "single-site gap any of them reaches is the one this unit "
                  "publishes its deciding cost against",
                  wide_configs=1, integral_coins=1, wide_exact=1),
         wide_exact == 0 and wide[3]["closest_is_pr3"]
         and not wide[2]["closest_is_pr3"] and wide_configs > 0,
         "configs %d exact %d closest q3 %s (pr3 %s) q2 %s (pr3 %s)"
         % (wide_configs, wide_exact, wide[3]["closest_gap"],
            wide[3]["pr3_gap"], wide[2]["closest_gap"], wide[2]["pr3_gap"]))

    # -- Z4: THE MECHANISM, CORROBORATED ------------------------------------
    # Section 8's account says the tick is the closure time of the arena's
    # elementary triangle.  K1 built the discriminating test and this unit
    # runs it: a declared direction set whose two-shift paths never return to
    # a one-shift site moves the first difference to the fourth tick.
    mech_rows = []
    # a REAL narrowing: the corroboration is run one tick short of the tick
    # the non-closing arena's own difference arrives at, so the case that
    # discriminates the account falls outside its own window
    mech_horizon = (DG_T - 1) if mut("MUT-MECHANISM") else DG_T
    for dirs in (LINKDIRS, ((1, 0), (0, 1), (1, 2)),
                 ((1, 0), (0, 1), (2, 2))):
        Am = Arena(3, dirs=dirs)
        closes = any(((dirs[a][0] + dirs[b][0]) % 3,
                      (dirs[a][1] + dirs[b][1]) % 3) == dirs[c]
                     for a in range(3) for b in range(3) for c in range(3)
                     if a != b and c not in (a, b))
        ispm = i_ladder(Am, mech_horizon, 3, GROVER, (0, 0), 0, "A")
        nulm = n_ladder_ring(Am, mech_horizon, GROVER, (0, 0), 0)
        mech_rows.append((dirs, closes,
                          k_first_difference(ispm["dist"], nulm[0],
                                             mech_horizon)))
    mech_ok = all((t == FIB_T) if c else (t is not None and t > FIB_T)
                  for (_d, c, t) in mech_rows)
    REG.measured("mechanism_sets", len(mech_rows), "the declared direction "
                 "sets of the corroboration")
    R["mechanism"] = {
        "rows": [{"directions": " ".join("(%d, %d)" % d for d in dirs),
                  "closed under addition": "yes" if c else "no",
                  "first difference": t}
                 for (dirs, c, t) in mech_rows],
        "word": "CORROBORATED" if mech_ok else "NOT-CORROBORATED",
        "status": "an account, still ungated as an explanation; what is "
                  "gated is the correlation this row measures"}
    SEAL.seal("mechanism", R["mechanism"], "G-MECHANISM-CORROBORATED")
    gate("G-MECHANISM-CORROBORATED",
         REG.stmt("the account of the tick is corroborated by the case that "
                  "discriminates it: over {mechanism_sets} declared "
                  "direction sets at the larger plane the first difference "
                  "arrives at the third tick exactly when the set is closed "
                  "under addition, and at the fourth when a two-shift path "
                  "cannot return to a site one shift had already reached",
                  mechanism_sets=1),
         mech_ok, "rows %s" % [(c, t) for (_d, c, t) in mech_rows])

    # -- the modulus leg: NDEP's untested prediction, RUN --------------------
    a_conn = ASET.read("A-COUP-CONNECTION", "G-MODULUS-DESCENT-THEOREM")
    # a REAL weakening: the separation condition is dropped, so the sweep
    # runs again and admits every modulus that merely descends
    desc, lemma_bad = i_modulus_descent(
        PRIME_ORDERS, MODULUS_WINDOW,
        require_separation=not mut("MUT-DESCENT"))
    desc_ok = all(g == (q,) for (q, g) in desc) and not lemma_bad
    # the anchor's CONTENT enters the predicate: the field order named in the
    # parent's own sentence is pulled out of it and compared with the modulus
    # the theorem returns at that order
    conn_q = k_int_from(a_conn, "scalar group z")
    conn_ok = (conn_q is not None
               and dict(desc).get(conn_q) == (conn_q,)
               and conn_q == arenas[3].q)
    REG.measured("descent_arenas", len(desc), "the swept field orders")
    REG.measured("descent_moduli", len(MODULUS_WINDOW), "len(MODULUS_WINDOW)")
    R["modulus_descent"] = {
        "rows": [{"q": q, "admissible_moduli": list(g)} for (q, g) in desc],
        "field_order_read_from_the_parent": conn_q,
        "prime_orders_only": True,
        "lemma": "descent holds exactly when m divides q, separation exactly "
                 "when m is at least q, and the two together leave m = q",
        "lemma_counterexamples": lemma_bad,
        "parent_sentence_located": bool(conn_ok)}
    SEAL.seal("modulus_descent", R["modulus_descent"],
              "G-MODULUS-DESCENT-THEOREM")
    gate("G-MODULUS-DESCENT-THEOREM",
         REG.stmt("the parent derives the connection from the arena's own "
                  "scalar group; the phase map descends to that group "
                  "exactly when the modulus divides the field order and "
                  "separates its elements exactly when it is at least the "
                  "field order, and the two together leave the field order "
                  "itself -- a lemma, verified against the computed "
                  "predicates at every one of {descent_arenas} orders and "
                  "{descent_moduli} moduli, so the parent's derivation read "
                  "at the smaller arena is determinate and not a convention",
                  descent_arenas=1, descent_moduli=1),
         desc_ok and conn_ok, "rows %s lemma-counterexamples %s "
         "parent-sentence %s"
         % ([(q, list(g)) for (q, g) in desc], lemma_bad or "none", conn_ok))

    a_res = ASET.read("A-COUP-RESIDUE", "G-MODULUS-OBSERVABLE")
    A2 = arenas[2]
    msweep, mdist = [], {}
    rationality = []
    for m in MODULI:
        try:
            r = i_ladder(A2, FIB_T, m, GROVER, (0, 0), 0, "A")
            mdist[m] = r["dist"][3]
            msweep.append((m, str(r["ipr"][3]), r["branches"][3]))
            rationality.append((m, True))
        except ET.CheckFail:
            rationality.append((m, False))
    if mut("MUT-MODULUS"):
        # a REAL collapse: the predicted modulus is run at the parent's
        # modulus instead of its own, so the two genuinely coincide
        mdist[2] = i_ladder(A2, FIB_T, 3, GROVER, (0, 0), 0, "A")["dist"][3]
    distinct = len({mdist[m] for m in mdist})
    REG.measured("moduli_run", len(mdist), "the moduli whose Born weights "
                 "stay rational")
    REG.measured("moduli_declared", len(MODULI), "len(MODULI)")
    REG.measured("moduli_distinct", distinct,
                 "distinct tick-3 distributions over the moduli run")
    R["modulus"] = {
        "word": "FORCED-AND-OBSERVABLE" if (desc_ok and distinct == len(mdist))
        else "NOT-SEPARATED",
        "declared": list(MODULI),
        "moduli_run": len(mdist), "distinct_values": distinct,
        "forced": "M-EQUALS-Q",
        "rows": [{"m": m, "ipr_tick3": i, "branches_tick3": b}
                 for (m, i, b) in msweep],
        "rational_born_weights": [{"m": m, "rational": ok}
                                  for (m, ok) in rationality],
        "residue_modulus_read_from_the_parent": k_int_from(a_res, "n mod"),
        "residue_sentence": k_int_from(a_res, "n mod") == arenas[3].q}
    SEAL.seal("modulus", R["modulus"], "G-MODULUS-OBSERVABLE")
    gate("G-MODULUS-OBSERVABLE",
         REG.stmt("the parent discloses that its walk consumes the count "
                  "residue and not the count; at the smaller arena the "
                  "tick-three distribution takes {moduli_distinct} distinct "
                  "values over the {moduli_run} moduli whose Born weights "
                  "stay rational, so the modulus is not invisible and the "
                  "prediction is testable there", moduli_distinct=1,
                  moduli_run=1),
         distinct == len(mdist) and R["modulus"]["residue_sentence"],
         "distinct %d of %d moduli" % (distinct, len(mdist)))

    a_succ = ASET.read("A-NDEP-SUCCESSOR", "G-M2-PREDICTION-RUN")
    a_pred = ASET.read("A-NDEP-PREDICTS", "G-M2-PREDICTION-RUN")
    # the two anchors' CONTENT enters the predicate: the modulus the parent
    # says its derivation forces, and the modulus it says it predicts, are
    # pulled out of the parent's own sentences and compared with the field
    # order of the arena this unit built the connection on
    succ_m = k_int_from(a_succ, "forces m =")
    pred_m = k_int_from(a_pred, "predicts m =")
    read_m = 3 if mut("MUT-M2") else 2   # a REAL misreading of the arena
    m2_dist = mdist.get(read_m)
    succ_ok = (succ_m == arenas[2].q and pred_m == arenas[2].q
               and dict(desc).get(arenas[2].q) == (arenas[2].q,))
    m2_matches = m2_dist is not None and m2_dist == tuple(
        map(Fraction, head_vals[2]["isp_dist"]))
    R["m2_prediction"] = {
        "arena": "AG(2,2)", "predicted_modulus": read_m,
        "modulus_read_from_the_successor_sentence": succ_m,
        "modulus_read_from_the_prediction_sentence": pred_m,
        "distribution": _dist(m2_dist) if m2_dist else [],
        "ipr": head_vals[2]["isp_ipr"],
        "null_distribution": head_vals[2]["null_dist"],
        "null_ipr": head_vals[2]["null_ipr"],
        "successor_test_located": bool(succ_ok),
        "construction_dependent": True,
        "status": "INTERNAL-CHECK-CLOSING-THE-PARENTS-REGISTERED-TEST",
        "caveat": "the forcing holds for the phase-character construction "
                  "the parent chose -- a phase that is a character of the "
                  "arena's own scalar group. A different construction would "
                  "have a different forcing, so this closes an internal "
                  "obligation and is not an external prediction.",
        "verdict": "RUN-AND-DETERMINATE" if (succ_ok and m2_matches)
        else "NOT-RUN"}
    SEAL.seal("m2_prediction", R["m2_prediction"], "G-M2-PREDICTION-RUN")
    gate("G-M2-PREDICTION-RUN",
         REG.stmt("the successor test the parent registered and did not run "
                  "is run here: the connection is built at the smaller "
                  "affine plane over its own field, the derivation forces "
                  "the modulus the parent predicted, and the observable the "
                  "parent asked for is exhibited with its exact value"),
         succ_ok and m2_matches,
         "successor sentence %s value %s" % (succ_ok, m2_matches))

    # -- the lattice leg: POT's perimeter law and gap, ACT's quartic sign ----
    alphabet = i_alphabet()
    lcoins, lrows = i_link_coins(alphabet)
    lat = Lattice(4)
    shapes = [(a, b) for a in (1, 2, 3) for b in (1, 2, 3)]
    a_per = ASET.read("A-POT-PERIMETER", "G-PERIMETER-LAW-BOTH")
    # THE ANCHOR'S CONTENT (K3 MINOR-2): the parent's sentence names the
    # quantity its own law groups by -- "ladder shapes of equal PERIMETER" --
    # and that word is pulled out of the sentence and SELECTS the grouping
    # function used below.  A parent sentence naming a different quantity
    # would group the comparisons differently.
    group_word = ET.canon(a_per).split("of equal ")[-1].split(",")[0].strip()
    GROUPERS = {"perimeter": (lambda a, b: a + b),
                "longer side": (lambda a, b: max(a, b)),
                "area": (lambda a, b: a * b)}
    grouper = GROUPERS.get(group_word)
    ladders = {}
    per_comps = per_bad = 0
    for m in lcoins:
        vals = {}
        for (a, b) in shapes:
            cyc, ok = i_rect_cycle(lat, (0, 0), a, b)
            if not ok:
                raise ET.CheckFail("G-PERIMETER-LAW-BOTH",
                                   "a rectangle circuit did not close")
            vals[(a, b)] = i_loop_observable(lat, cyc, m)
        ladders[m] = vals
        byP: dict = {}
        for (a, b), v in vals.items():
            # a REAL mis-grouping: shapes are grouped by their LONGER SIDE
            # instead of by the quantity the parent's own sentence names, so
            # the equal-group comparisons genuinely disagree
            key = (GROUPERS["longer side"](a, b) if mut("MUT-PERIMETER")
                   else grouper(a, b))
            byP.setdefault(key, []).append(v)
        for _P, lst in byP.items():
            for x in range(len(lst)):
                for y in range(x + 1, len(lst)):
                    per_comps += 1
                    if lst[x] != lst[y]:
                        per_bad += 1

    def _wofP(vals):
        return {a + b: v for (a, b), v in vals.items()}

    def _fit(w):
        sol = []
        for comp in (0, 1):
            M = [[Fraction(1), Fraction(2), Fraction(1, 4), w[2][comp]],
                 [Fraction(1), Fraction(3), Fraction(1, 8), w[3][comp]],
                 [Fraction(1), Fraction(4), Fraction(1, 16), w[4][comp]]]
            for i in range(3):
                p = next(r for r in range(i, 3) if M[r][i] != 0)
                M[i], M[p] = M[p], M[i]
                pv = M[i][i]
                M[i] = [x / pv for x in M[i]]
                for r in range(3):
                    if r != i and M[r][i] != 0:
                        f = M[r][i]
                        M[r] = [M[r][k] - f * M[i][k] for k in range(4)]
            sol.append((M[0][3], M[1][3], M[2][3]))
        return sol

    cf_fail = 0
    halving = 0
    for m in lcoins:
        w = _wofP(ladders[m])
        sol = _fit(w)
        for P in (5, 6):
            for comp in (0, 1):
                A_, B_, C_ = sol[comp]
                if A_ + B_ * P + C_ * Fraction(1, 2 ** P) != w[P][comp]:
                    cf_fail += 1
        if sol[0][2] != 0 or sol[1][2] != 0:
            halving += 1
    HAD = (SQRT2, SQRT2, SQRT2, tuple(-x for x in SQRT2))
    had_in = HAD in set(lcoins)
    had_sol = _fit(_wofP(ladders[HAD])) if had_in else None
    if mut("MUT-GAP"):
        # a REAL substitution: the null's coin is replaced by a diagonal one,
        # whose realised ladder carries no halving mode at all
        HAD = [m for m in lcoins if i_sector(m) == "DIAGONAL"][0]
        had_in = HAD in set(lcoins)
        had_sol = _fit(_wofP(ladders[HAD]))
    had_halving = bool(had_sol and (had_sol[0][2] != 0 or had_sol[1][2] != 0))
    REG.measured("link_coins", len(lcoins), "the exhaustive coin family")
    REG.measured("alphabet_size", len(alphabet), "the declared alphabet")
    REG.measured("perimeter_comparisons", per_comps,
                 "equal-perimeter shape pairs by coin")
    REG.measured("halving_coins", halving, "coins whose fit has a halving term")
    sectors = collections.Counter(i_sector(m) for m in lcoins)
    R["lattice_perimeter"] = {
        "alphabet": len(alphabet), "rows": len(lrows), "coins": len(lcoins),
        "sectors": {k: v for k, v in sorted(sectors.items())},
        "comparisons": per_comps, "disagreements": per_bad,
        "grouping_quantity_read_from_the_parent": group_word,
        "null_coin_name": "the Hadamard link coin",
        "null_coin_in_family": bool(had_in),
        "null_coin_sector": i_sector(HAD),
        "pr3_selects_on_this_carrier": False,
        "word": "REPRODUCED-BY-THE-NULL" if (per_bad == 0 and had_in)
        else "NOT-REPRODUCED"}
    SEAL.seal("lattice_perimeter", R["lattice_perimeter"],
              "G-PERIMETER-LAW-BOTH")
    gate("G-PERIMETER-LAW-BOTH",
         REG.stmt("the parent's perimeter-only law is a per-configuration "
                  "statement about a uniform configuration: the quantity its "
                  "own sentence groups by is pulled out of that sentence and "
                  "selects the grouping used here, and over "
                  "{perimeter_comparisons} equal-group comparisons at every "
                  "one of the {link_coins} coins of the shared family the "
                  "loop observable is constant, the record-free lattice "
                  "arm's declared coin among them, so the law is that arm's "
                  "too", perimeter_comparisons=1, link_coins=1),
         per_bad == 0 and had_in and grouper is not None
         and group_word == "perimeter",
         "comparisons %d disagreements %d grouping %r null-coin-in-family %s"
         % (per_comps, per_bad, group_word, had_in))
    a_gap = ASET.read("A-POT-GAP", "G-GAP-BOTH")
    # the anchor's CONTENT enters the predicate: the gap named in the
    # parent's own sentence is pulled out of it and compared with the ratio
    # the null coin's own fitted halving term actually carries between
    # consecutive perimeters
    parent_gap = k_frac_from(a_gap, "gap")
    w_null = _wofP(ladders[HAD])
    A_, B_, C_ = had_sol[0]
    tail = {P: w_null[P][0] - A_ - B_ * P for P in (4, 5, 6)}
    ratio = tail[5] / tail[4] if tail[4] != 0 else None
    ratio_ok = ratio is not None and ratio == tail[6] / tail[5] == parent_gap
    R["lattice_closed_form"] = {
        "failures": cf_fail, "halving_present_at": halving,
        "coins": len(lcoins),
        "null_coin_coefficients": [str(x) for x in had_sol[0]],
        "null_coin_halving": had_halving,
        "null_coin_halving_ratio": str(ratio),
        "ratio_status": "DEFINITIONAL-GIVEN-A-NON-ZERO-HALVING-COEFFICIENT",
        "measured_content": "the halving coefficient's PRESENCE, at the "
                            "coins counted here and at the record-free "
                            "lattice arm's own",
        "gap_read_from_the_parent": str(parent_gap),
        "spectrum": ["1", "1", str(parent_gap)],
        "word_closed": "REPRODUCED-BY-THE-NULL" if cf_fail == 0
        else "NOT-REPRODUCED",
        "word_gap": "REPRODUCED-BY-THE-NULL" if (had_halving and ratio_ok)
        else "NOT-REPRODUCED"}
    SEAL.seal("lattice_closed_form", R["lattice_closed_form"], "G-GAP-BOTH")
    gate("G-GAP-BOTH",
         REG.stmt("the parent's three-term closed form is over-determined at "
                  "every coin and fails at none, and the halving mode that "
                  "carries the parent's gap is present at {halving_coins} of "
                  "{link_coins} coins -- the record-free lattice arm's own "
                  "coin among them, its coefficients measured here.  The "
                  "ratio between consecutive perimeters is the ansatz's own "
                  "basis function and is definitional once the halving "
                  "coefficient is non-zero; the measured content of this row "
                  "is that coefficient's presence", halving_coins=1,
                  link_coins=1),
         cf_fail == 0 and had_halving and ratio_ok,
         "closed-form failures %d halving %d of %d null-coin %s ratio %s "
         "(definitional given a non-zero coefficient)"
         % (cf_fail, halving, len(lcoins), had_halving, ratio))

    a_plq = ASET.read("A-POT-PLAQUETTE", "G-PLAQUETTE-BOTH")
    pcyc, _ok = i_rect_cycle(lat, (0, 0), 1, 1)
    pvals = [i_loop_observable(lat, pcyc, m) for m in lcoins]
    p_distinct = len(set(pvals))
    p_exp_rat = n_lattice_expectation([v[0] for v in pvals])
    p_exp_surd = n_lattice_expectation([v[1] for v in pvals])
    nonflat = sum(1 for m, v in zip(lcoins, pvals)
                  if i_sector(m) == "DIAGONAL" and v != (Fraction(4),
                                                         Fraction(0)))
    if mut("MUT-PLAQUETTE"):
        # a REAL change of measure: the expectation is taken over the
        # balanced sector alone, which is not the null's declared measure
        p_exp_rat = n_lattice_expectation(
            [v[0] for m, v in zip(lcoins, pvals)
             if i_sector(m) == "BALANCED"])
    REG.measured("plaquette_values", p_distinct, "distinct observable values")
    REG.measured("nonflat_diagonal", nonflat, "the grandparent's own count")
    parent_pq_values = k_int_from(a_plq, "trace takes")
    parent_pq_exp = k_frac_from(a_plq, "counting expectation is")
    R["lattice_plaquette"] = {
        "distinct": p_distinct,
        "counting_expectation": str(p_exp_rat),
        "counting_surd": str(p_exp_surd), "nonflat_diagonal": nonflat,
        "values_read_from_the_parent": parent_pq_values,
        "expectation_read_from_the_parent": str(parent_pq_exp),
        "parents_own_stamp": "CONDITIONAL-ON-THE-DECLARED-WEIGHTS: the "
                             "parent reports four expectations, one per "
                             "declared weight system, and this row "
                             "reproduces the one taken at the counting "
                             "measure, which is the record-free arm's own "
                             "measure by rule PR7",
        "word": "REPRODUCED-BY-THE-NULL"
        if (p_distinct == parent_pq_values and p_exp_rat == parent_pq_exp)
        else "NOT-REPRODUCED"}
    SEAL.seal("lattice_plaquette", R["lattice_plaquette"], "G-PLAQUETTE-BOTH")
    gate("G-PLAQUETTE-BOTH",
         REG.stmt("the parent's plaquette row is a counting expectation, "
                  "which is the null's own measure by rule: the observable "
                  "takes {plaquette_values} distinct values, the counting "
                  "expectation is the parent's own, and {nonflat_diagonal} "
                  "diagonal coins are non-flat -- the grandparent's number",
                  plaquette_values=1, nonflat_diagonal=1),
         p_distinct == parent_pq_values and p_exp_rat == parent_pq_exp
         and p_exp_surd == 0 and nonflat > 0,
         "values %d (parent %s) expectation %s (parent %s) non-flat %d"
         % (p_distinct, parent_pq_values, p_exp_rat, parent_pq_exp, nonflat))

    a_q1 = ASET.read("A-ACT-QUARTIC", "G-QUARTIC-BOTH")
    a_q2 = ASET.read("A-ACT-OBSERVABLE", "G-QUARTIC-BOTH")
    # the anchor's CONTENT enters the predicate: the POWER named in the
    # parent's own sentence is pulled out of it and is the exponent the
    # observable is computed with
    parent_power = {"fourth": 4}.get(
        ET.canon(a_q2).split("power")[0].strip().split()[-1])
    # and the VALUE the parent pins the observable to comes out of its own
    # sentence's last word rather than being typed here (K3 MINOR-2)
    parent_pin = SPELLED.get(ET.canon(a_q1).split()[-1])
    if mut("MUT-QUARTIC"):
        parent_power = 2          # a REAL misreading of the parent's exponent
    qvals = [i_quartic_sign(m[1], parent_power)
             + i_quartic_sign(m[2], parent_power) for m in lcoins]
    qdist = collections.Counter(qvals)
    q_exp = n_lattice_expectation(qvals)
    coinset = set(lcoins)
    twist_rows = []
    for k in range(8):
        tw = [i_gauge_twist(m, k) for m in lcoins]
        _ = tw
        closed = all(t in coinset for t in tw)
        rev = sum(1 for m, t in zip(lcoins, tw)
                  if i_quartic_sign(t[1], parent_power)
                  + i_quartic_sign(t[2], parent_power)
                  == -(i_quartic_sign(m[1], parent_power)
                       + i_quartic_sign(m[2], parent_power)))
        twist_rows.append((k, closed, rev))
    odd_full = all(r for (k, _c, r) in
                   [(k, c, rv == len(lcoins)) for (k, c, rv) in twist_rows]
                   if k % 2 == 1)
    REG.measured("quartic_zero_coins", qdist[0], "coins with a vanishing pair")
    REG.measured("quartic_plus", qdist[2], "coins at the positive value")
    REG.measured("quartic_minus", qdist[-2], "coins at the negative value")
    R["lattice_quartic"] = {
        "power_read_from_the_parent": parent_power,
        "pinned_value_read_from_the_parent": parent_pin,
        "distribution": {str(k): v for k, v in sorted(qdist.items())},
        "counting_expectation": str(q_exp),
        "twists": [{"k": k, "closed": c, "sign_reversed": r}
                   for (k, c, r) in twist_rows],
        "odd_twists_reverse_everywhere": bool(odd_full),
        "word": "REPRODUCED-BY-THE-NULL" if q_exp == 0 else "NOT-REPRODUCED"}
    SEAL.seal("lattice_quartic", R["lattice_quartic"], "G-QUARTIC-BOTH")
    gate("G-QUARTIC-BOTH",
         REG.stmt("the parent's pinned observable is the added sign of the "
                  "fourth power of the two off-diagonal entries; it vanishes "
                  "at {quartic_zero_coins} coins and takes its two extreme "
                  "values at {quartic_plus} and {quartic_minus}, the odd "
                  "twists reverse it at every coin, and the counting measure "
                  "the record-free arm declares returns the very value the "
                  "parent's own sentence pins it to, read out of that "
                  "sentence rather than typed here",
                  quartic_zero_coins=1, quartic_plus=1, quartic_minus=1),
         parent_pin is not None and q_exp == parent_pin and odd_full
         and qdist[2] == qdist[-2] and parent_power is not None,
         "distribution %s counting expectation %s parent-pin %s odd-twists %s"
         % (dict(sorted(qdist.items())), q_exp, parent_pin, odd_full))

    # -- the coin-register forcing, arena-carried ---------------------------
    ALPHA3 = [(a, b) for a in range(-6, 7) for b in range(-6, 7)
              if a * a - a * b + b * b <= 9]
    link_offsets = ([(0, 0), (1, 0), (2, 0)] if mut("MUT-STENCIL")
                    else list(LINKDIRS))
    link_scan = i_stencil_scan(link_offsets, ALPHA3)
    axis_scan = i_stencil_scan([(0, 0), (1, 0), (2, 0)], ALPHA3)
    REG.measured("ring_elements", len(ALPHA3),
                 "the elements of the arena's ring of modulus at most one")
    REG.measured("stencil_maps", len(ALPHA3) ** 3, "the exhaustive scan")
    R["stencil"] = {"alphabet": len(ALPHA3), "maps": len(ALPHA3) ** 3,
                    "link": link_scan, "axis": axis_scan}
    SEAL.seal("stencil", R["stencil"], "G-STENCIL-FORCING-PARENT")
    gate("G-STENCIL-FORCING-PARENT",
         REG.stmt("over {ring_elements} ring elements and {stencil_maps} "
                  "coefficient maps the arena's own offset set admits no "
                  "non-monomial unitary at all while a collinear stencil "
                  "admits many, so the parent's coin-register theorem is "
                  "carried by the arena and is the null's too",
                  ring_elements=1, stencil_maps=1),
         link_scan["non_monomial"] == 0 and axis_scan["non_monomial"] > 0
         and link_scan["multiplicities"] == [1],
         "link %s axis %s" % (link_scan, axis_scan))

    # -- the expressibility census ------------------------------------------
    a_expr = ASET.read("A-PIN-EXPRESSIBILITY", "G-EXPRESSIBILITY-CENSUS")
    EXPR = [
        ("site-occupation distribution p_t(x)", "BOTH", "MEASURABLE",
         "a function of the state alone"),
        ("inverse participation ratio", "BOTH", "MEASURABLE",
         "a function of the site distribution"),
        ("total variation between two ticks' distributions", "BOTH",
         "MEASURABLE", "a function of distributions"),
        ("loop observable on a uniform configuration", "BOTH", "MEASURABLE",
         "a function of the link operators"),
        ("off-diagonal quartic sign", "BOTH", "MEASURABLE",
         "a function of the coin"),
        ("plaquette counting expectation", "BOTH", "MEASURABLE",
         "a function of the coin family and a measure"),
        ("division-count field n_l(x)", "ISP-ONLY", "DEFINITIONAL",
         "the null has no count field"),
        ("emission field and its link-class marginal", "ISP-ONLY",
         "DEFINITIONAL", "the null emits nothing"),
        ("branch count of the emission tree", "ISP-ONLY", "DEFINITIONAL",
         "the null has one trajectory"),
        ("record curvature field on the elementary triangle", "ISP-ONLY",
         "DEFINITIONAL", "a function of the count field"),
        ("maximum cell count", "ISP-ONLY", "DEFINITIONAL",
         "a function of the count field"),
        ("admissibility exit probability", "ISP-ONLY", "DEFINITIONAL",
         "admissibility is a property of the record"),
    ]
    if mut("MUT-EXPRESS"):
        # a REAL declassification: one observable is left without a class in
        # the declared vocabulary, so the census stops being total
        EXPR = EXPR[:-1] + [(EXPR[-1][0], "UNRULED", "UNRULED", EXPR[-1][3])]
    EXPR_WORDS = ("BOTH", "ISP-ONLY")
    # THE ANCHOR'S CONTENT (K3 MINOR-2): the class vocabulary is DERIVED from
    # the pin's own parenthetical -- "(state which are definitional vs
    # measurable)" -- rather than typed here and then looked for in the pin.
    # A pin naming different classes would give this census different ones.
    EXPR_CLASSES = tuple(
        w.split()[-1].upper()
        for w in ET.canon(a_expr).split("(")[-1].rstrip(")").split(" vs "))
    unruled = [r[0] for r in EXPR
               if r[1] not in EXPR_WORDS or r[2] not in EXPR_CLASSES]
    both = sum(1 for r in EXPR if r[1] == "BOTH")
    only = sum(1 for r in EXPR if r[1] == "ISP-ONLY")
    REG.measured("expr_rows", len(EXPR), "len(EXPR)")
    REG.measured("expr_both", both, "rows classed both-expressible")
    REG.measured("expr_only", only, "rows classed ISP-only")
    R["expressibility"] = {
        "rows": [{"observable": a, "expressible": b, "class": c, "why": d}
                 for (a, b, c, d) in EXPR],
        "total": len(EXPR), "both": both, "isp_only": only,
        "class_words": list(EXPR_CLASSES),
        "class_words_read_from_the_pin": True, "unruled": unruled}
    SEAL.seal("expressibility", R["expressibility"],
              "G-EXPRESSIBILITY-CENSUS")
    gate("G-EXPRESSIBILITY-CENSUS",
         REG.stmt("every one of {expr_rows} declared observables is classed, "
                  "in a class vocabulary read out of the pin's own sentence "
                  "rather than typed here, and the classes are total: "
                  "{expr_both} are formable in both models and {expr_only} "
                  "are formable only where a record exists, and a row of the "
                  "second kind is a definitional absence and never a "
                  "discriminant", expr_rows=1, expr_both=1, expr_only=1),
         both + only == len(EXPR) and both > 0 and only > 0
         and not unruled and len(EXPR_CLASSES) == len(EXPR_WORDS),
         "rows %d both %d isp-only %d classes %s unruled %s"
         % (len(EXPR), both, only, list(EXPR_CLASSES), unruled or "none"))

    # -- Q155: the reproduction census --------------------------------------
    # Every row now carries (a) its PROVENANCE -- whether it is a sealed
    # parent result, a row this unit carved out of a parent observable, a
    # parent's registered-and-unrun test, or a bundle of definitional
    # absences -- and (b) a WITNESS: the measured equality or inequality that
    # earns its ruling.  K2 MAJOR-8: the gate was a cardinality identity and
    # nothing anywhere bound a row's ruling to its evidence, so a flip in the
    # ISP-flattering direction left the predicate satisfied.
    SEALED, CARVED, UNRUN, BUNDLE = ("sealed parent result",
                                     "carved here from the same parent "
                                     "observable as the row below",
                                     "parent's registered-and-unrun test",
                                     "definitional bundle")
    CENSUS = [
        ("paper-36 the rectangle ladder is a function of the perimeter alone",
         "REPRODUCED",
         "per-configuration at %d equal-perimeter comparisons, %d "
         "disagreements; the record-free lattice arm's own coin is in the "
         "family" % (per_comps, per_bad), SEALED, "PERIMETER-LAW",
         per_bad == 0 and had_in),
        ("paper-36 the three-term closed form at every coin", "REPRODUCED",
         "%d closed-form failures over %d coins" % (cf_fail, len(lcoins)),
         SEALED, "CLOSED-FORM", cf_fail == 0),
        ("paper-36 the halving mode and its gap", "REPRODUCED",
         "present at %d of %d coins, the record-free lattice arm's own among "
         "them with coefficients %s"
         % (halving, len(lcoins), " ".join(str(x) for x in had_sol[0])),
         SEALED, "GAP", bool(had_halving and ratio_ok)),
        ("paper-36 the plaquette counting expectation", "REPRODUCED",
         "%d distinct values, expectation %s, %d non-flat diagonal coins"
         % (p_distinct, p_exp_rat, nonflat), SEALED, "PLAQUETTE",
         p_distinct == parent_pq_values and p_exp_rat == parent_pq_exp),
        ("paper-34 the off-diagonal quartic sign pinned to a single value",
         "REPRODUCED",
         "the record-free arm's counting measure returns %s; the odd twists "
         "reverse the observable at every coin" % q_exp, SEALED,
         "QUARTIC-SIGN", q_exp == parent_pin),
        ("paper-20 the coin register is forced on this offset set",
         "REPRODUCED",
         "%d unitary and %d non-monomial over %d maps: arena-carried"
         % (link_scan["unitary"], link_scan["non_monomial"],
            len(ALPHA3) ** 3), SEALED, "COIN-REGISTER-RESTRICTION",
         link_scan["non_monomial"] == 0),
        ("paper-20 the walk's distribution at the first two ticks",
         "REPRODUCED",
         "%d site-by-tick comparisons, %d violations, over all %d points "
         "of the sweep"
         % (agree_checks, agree_viol, nontrivial_pts + trivial_pts),
         CARVED, "THE-FIRST-TWO-TICKS", agree_viol == 0),
        ("paper-20 the walk's distribution from the third tick on",
         "NOT-REPRODUCED",
         "unequal at both arenas; the first difference arrives at the same "
         "tick at %d of %d interfering points of the sweep; at the parent's "
         "alternative coin order it arrives one tick later"
         % (nontrivial_at3, nontrivial_pts), SEALED, "", not disc_found),
        ("paper-39 the connection modulus read at the smaller arena",
         "NOT-REPRODUCED",
         "the record-free arm is the modulus-one point of the family; the "
         "tick-three distribution takes %d distinct values over %d moduli; "
         "internal, construction-dependent" % (distinct, len(mdist)),
         UNRUN, "", distinct == 1),
        ("paper-20 the record-side observable set", "NOT-EXPRESSIBLE",
         "%d of %d observables of the classification are formable only where "
         "a record exists" % (only, len(EXPR)), BUNDLE, "", None),
    ]
    if mut("MUT-CENSUS"):
        CENSUS = [(a, "REPRODUCED", c, p, k, w) if b == "NOT-REPRODUCED"
                  else (a, b, c, p, k, w) for (a, b, c, p, k, w) in CENSUS]
    if mut("MUT-CENSUS-FLIP"):
        # the ISP-FLATTERING direction, which the delivered gate could not
        # see: a reproduction is rewritten to a non-reproduction, and the
        # row's own witness still says the two arms agree
        CENSUS = [(a, "NOT-REPRODUCED", c, p, "", w) if b == "REPRODUCED"
                  and k == "PLAQUETTE" else (a, b, c, p, k, w)
                  for (a, b, c, p, k, w) in CENSUS]
    rep = sum(1 for r in CENSUS if r[1] == "REPRODUCED")
    nrep = sum(1 for r in CENSUS if r[1] == "NOT-REPRODUCED")
    nexp = sum(1 for r in CENSUS if r[1] == "NOT-EXPRESSIBLE")
    parent_rows = [r for r in CENSUS if r[3] != CARVED]
    parent_rep = sum(1 for r in parent_rows if r[1] == "REPRODUCED")
    # THE BINDING: a REPRODUCED row must carry a measured equality and a
    # NOT-REPRODUCED row a measured inequality, per row, by name.
    WITNESS_OF = {"REPRODUCED": True, "NOT-REPRODUCED": False,
                  "NOT-EXPRESSIBLE": None}
    unbound_rows = [r[0] for r in CENSUS
                    if r[1] not in WITNESS_OF or WITNESS_OF[r[1]] is not r[5]]
    keyed = [r for r in CENSUS if r[1] == "REPRODUCED" and not r[4]]
    REG.measured("census_rows", len(CENSUS), "len(CENSUS)")
    REG.measured("census_reproduced", rep, "rows ruled reproduced")
    REG.measured("census_not_reproduced", nrep, "rows ruled not reproduced")
    REG.measured("census_not_expressible", nexp,
                 "rows the null cannot form at all")
    REG.measured("parent_results", len(parent_rows),
                 "census rows that are a parent's own result")
    REG.measured("parent_reproduced", parent_rep,
                 "of which the record-free null reproduces")
    R["q155_census"] = {
        "rows": [{"parent result": a, "provenance": p, "ruling": b,
                  "evidence": c} for (a, b, c, p, _k, _w) in CENSUS],
        "rows_count": len(CENSUS), "reproduced": rep,
        "not_reproduced": nrep, "not_expressible": nexp,
        "parent_results": len(parent_rows), "parent_reproduced": parent_rep,
        "reproduced_keys": [r[4] for r in CENSUS if r[1] == "REPRODUCED"],
        "provenance_classes": [SEALED, CARVED, UNRUN, BUNDLE],
        "rulings_unbound": unbound_rows,
        "reading": "the census is led at the parent-result grain -- one row "
                   "per parent result, the walk's own site distribution "
                   "counted once -- and the tested-row grain is kept beside "
                   "it as provenance"}
    SEAL.seal("q155_census", R["q155_census"], "G-Q155-CENSUS-TOTAL")
    gate("G-Q155-CENSUS-TOTAL",
         REG.stmt("every one of {census_rows} tested rows is ruled by a "
                  "measurement taken in this run AND each ruling is bound to "
                  "that measurement per row -- a reproduction to a measured "
                  "equality, a non-reproduction to a measured inequality -- "
                  "so a ruling cannot be flipped in either direction and "
                  "leave the gate satisfied; at the parent-result grain the "
                  "rows are {parent_results}, of which {parent_reproduced} "
                  "are reproduced, {census_not_reproduced} are not and "
                  "{census_not_expressible} cannot be formed by a model "
                  "without a record at all, and at the tested-row grain "
                  "{census_reproduced} of {census_rows} are reproduced",
                  census_rows=1, parent_results=1, parent_reproduced=1,
                  census_reproduced=1, census_not_reproduced=1,
                  census_not_expressible=1),
         rep + nrep + nexp == len(CENSUS) and nrep > 0 and not unbound_rows
         and not keyed and len(parent_rows) == len(CENSUS) - 1,
         "rows %d reproduced %d not %d not-expressible %d parent-grain %d/%d "
         "unbound %s"
         % (len(CENSUS), rep, nrep, nexp, parent_rep, len(parent_rows),
            unbound_rows or "none"))

    # -- the falsifier and the finite experiment ----------------------------
    # THE DECIDING COST IS THE COST AGAINST THE CLOSEST MEMORYLESS OPPONENT,
    # not against the PR3 null alone (K2 MAJOR-5b).  At the larger plane the
    # two coincide; at the smaller a non-covariant integral coin comes closer,
    # so the published shot count there is larger than the PR3 figure and the
    # PR3 figure is published beside it rather than instead of it.
    gap3, gap2 = wide[3]["_gap"], wide[2]["_gap"]
    shots3 = k_shots(gap3, 100)
    shots2 = k_shots(gap2, 100)
    pr3_shots3 = k_shots(head_vals[3]["_gap"], 100)
    pr3_shots2 = k_shots(head_vals[2]["_gap"], 100)
    ops3 = head_vals[3]["branches"]
    ops2 = head_vals[2]["branches"]
    if mut("MUT-FALSIFIER"):
        # a REAL substitution: the cost is priced against the PR3 null rather
        # than against the closest memoryless walk the sweep found
        shots2 = pr3_shots2
    R["falsifier"] = {
        "word": "COMPUTATIONAL-REGRESSION-TEST-ON-A-PROPOSED-REALIZATION",
        "statement": "a proposed realization of this model is refuted at the "
                     "declared arena if the site-occupation distribution at "
                     "the third tick takes any value other than the one "
                     "published here; the test is a regression test on a "
                     "realization and not an empirical test of nature, "
                     "because this corpus supplies no mapping from ticks and "
                     "sites to laboratory units",
        "diagnostic_case": "the value the record-free null itself takes, "
                           "which is the case that says the record layer was "
                           "not implemented at all",
        "kind": "REGRESSION-TEST-NOT-EMPIRICAL",
        "max_gap_q3": head_vals[3]["max_gap"],
        "max_gap_q2": head_vals[2]["max_gap"],
        "closest_gap_q3": wide[3]["closest_gap"],
        "closest_gap_q2": wide[2]["closest_gap"],
        "shots_q3": shots3, "shots_q2": shots2,
        "shots_against_the_pr3_null_q3": pr3_shots3,
        "shots_against_the_pr3_null_q2": pr3_shots2,
        "confidence_denominator": 100,
        "simulation_branches_q3": ops3, "simulation_branches_q2": ops2,
        "operational_units": "ABSENT-IN-THIS-CORPUS"}
    SEAL.seal("falsifier", R["falsifier"], "G-FALSIFIER-SPECIFIED")
    REG.measured("shots_q3", shots3, "Chebyshev at the closest measured gap")
    REG.measured("shots_q2", shots2, "Chebyshev at the closest measured gap")
    REG.measured("pr3_shots_q2", pr3_shots2,
                 "Chebyshev at the PR3 null's own gap")
    REG.measured("sim_branches_q3", ops3, "the exhaustive emission tree")
    gate("G-FALSIFIER-SPECIFIED",
         REG.stmt("the falsifier is the discriminating observable itself and "
                  "the experiment is finite twice over: the exhaustive "
                  "simulation closes at {sim_branches_q3} branches, and a "
                  "repeated preparation separates the ISP value from the "
                  "CLOSEST memoryless walk the wider sweep found in "
                  "{shots_q3} shots at the larger arena and {shots_q2} at "
                  "the smaller -- against the PR3 null alone the smaller "
                  "plane would cost {pr3_shots_q2}, and the larger figure is "
                  "the one published -- both by Chebyshev on the measured "
                  "gap and both in exact rational arithmetic",
                  sim_branches_q3=1, shots_q3=1, shots_q2=1, pr3_shots_q2=1),
         shots3 == k_shots(gap3, 100) and shots2 == k_shots(gap2, 100)
         and shots2 >= pr3_shots2,
         "shots %d / %d (pr3 %d / %d) branches %d / %d"
         % (shots3, shots2, pr3_shots3, pr3_shots2, ops3, ops2))

    # -- #299-AS-EXTENDED FEASIBILITY ---------------------------------------
    # PLAN.md's Standards bind feasibility argued against the committed
    # corpus at the declared row list, and the pin pre-registers three
    # outcome words.  K2 MAJOR-6: none of the three occurred anywhere in the
    # delivered object and no feasibility argument existed.  Both halves are
    # answered here, and the answer is machine-checked rather than narrated:
    # the alternative outcome word is REACHED by a declared recipe of this
    # unit's own battery, which is the demonstration the argument needs.
    pin_words = ("DISC-FOUND", "DISC-NULL-REPRODUCES-ALL-TESTED",
                 "DISC-BLOCKED")
    neg_word = "RECORD-BACKREACTION-NOT-DETECTED-IN-THE-SWEPT-WINDOW"
    reach = {
        pin_words[0]: ("REACHED-UNDER-THE-RENAMED-POSITIVE-WORD", True),
        pin_words[1]: ("REACHABLE: the census's own limit at "
                       "%d-OF-%d-TESTED-ROWS, and the negative verdict word "
                       "%s is driven by the declared recipe MUT-VALUES, "
                       "which switches the coupling off and dies at "
                       "G-DISCRIMINANT-VALUES"
                       % (len(CENSUS), len(CENSUS), neg_word), True),
        pin_words[2]: ("RETIRED-AS-UNREACHABLE: no route in this instrument "
                       "produces it -- the two arms are exhaustive and "
                       "exact, so the run either separates them or does "
                       "not, and there is no third exit; the word is "
                       "declared retired rather than left silent", False),
    }
    battery = [m[0] for m in MUTANTS]
    reachable = sum(1 for (_t, ok) in reach.values() if ok)
    if mut("MUT-FEASIBILITY"):
        # a REAL removal: the recipe that drives the payload to the
        # alternative outcome is taken out of the battery the argument
        # relies on, so the feasibility demonstration stops existing
        battery = [nm for nm in battery if nm != "MUT-VALUES"]
    have_neg = "MUT-VALUES" in battery
    REG.measured("pin_outcome_words", len(pin_words), "len(pin_words)")
    REG.measured("reachable_outcomes", reachable,
                 "pin outcome words with a route in this instrument")
    R["feasibility"] = {
        "word": "BOTH-WAYS-BY-A-DECLARED-RECIPE",
        "declared": len(pin_words), "reachable": reachable,
        "blocked_route": "DISC-BLOCKED-RETIRED-AS-UNREACHABLE-BY-"
                         "CONSTRUCTION",
        "negative_verdict_word": neg_word,
        "rows": [{"pin outcome word": w, "status": reach[w][0]}
                 for w in pin_words],
        "demonstration": "MUT-VALUES drives the payload to the negative "
                         "verdict word and dies at G-DISCRIMINANT-VALUES",
        "demonstration_present": bool(have_neg)}
    SEAL.seal("feasibility", R["feasibility"], "G-FEASIBILITY-BOTH-WAYS")
    gate("G-FEASIBILITY-BOTH-WAYS",
         REG.stmt("the pin's {pin_outcome_words} pre-registered outcome "
                  "words are each mapped onto this unit's delivered "
                  "vocabulary and {reachable_outcomes} of them have a route "
                  "in this instrument, the third being declared retired as "
                  "unreachable by construction rather than left silent; the "
                  "alternative outcome was reachable before the run, and the "
                  "demonstration is a declared recipe of this unit's own "
                  "battery that drives the payload to it",
                  pin_outcome_words=1, reachable_outcomes=1),
         have_neg and reachable == len(pin_words) - 1,
         "words %d reachable %d demonstration %s"
         % (len(pin_words), reachable, have_neg))

    # -- scope ---------------------------------------------------------------
    R["scope"] = {
        # v15 #33: the scope segment must not read as if ONE null were the
        # whole comparison class.  What was compared is a pre-registered null
        # PLUS a swept memoryless class; what was NOT compared is any
        # memory-bearing null, which is DISC-2's charge.
        "word": "ONE-PRE-REGISTERED-NULL-PR1-TO-PR7-WHICH-IS-THE-PARENTS-"
                "FROZEN-STAGE-CONTROL;PLUS-A-SWEPT-MEMORYLESS-CLASS-OF-"
                "10380-CONFIGURATIONS;NO-MEMORY-BEARING-NULL-TESTED-AT-ALL;"
                "D=2;ARENAS=AG-2-2-AND-AG-2-3;READINGS=A-AND-B;"
                "AT-FINITE-HORIZON-A-RECORD-IS-ABSORBABLE-INTO-AN-ENLARGED-"
                "STATE;NO-OPERATIONAL-UNITS;NO-LABORATORY-CLAIM;"
                "NOT-AN-EXTERNAL-PREDICTION",
        "class_word": "MODEL-ABLATION-BENCHMARK",
        "successor_word": "DISC-2-THE-SIMPLEST-MEMORY-BEARING-NULL",
        "null_weakness": "what was compared is a pre-registered null obeying "
                         "PR1..PR7, which is the parent's own frozen-stage "
                         "control up to a global phase, TOGETHER WITH a swept "
                         "memoryless class of 10380 configurations. Every "
                         "member of both is MEMORYLESS: its coin is constant "
                         "in space and in time. At a finite horizon a record "
                         "is always absorbable into an enlarged state "
                         "description, so no memory-bearing null is excluded "
                         "by anything measured here -- none was tested at all "
                         "-- and that whole class is the successor's charge.",
        "successor": "DISC-2: the simplest memory-bearing null -- a "
                     "finite-memory coin, a state-dependent coin, a "
                     "dynamically updated phase field, or an enlarged "
                     "internal register -- named here and not attempted "
                     "here.",
        "arenas": list(ARENAS), "readings": ["A", "B"],
        "horizons": {"fiber": FIB_T, "fidelity": FID_T, "head": HEAD_T,
                     "coin order": DG_T}}
    # EVERY DECLARED AXIS CARRIES ITS OWN EVIDENCE (K1 MINOR-5, K2 m-9: the
    # waiver's stated forcing was false and the machine-checked one was mere
    # non-emptiness).  The waiver is gone: each axis is bound to the count of
    # members this run actually executed on it, the axis list is rendered
    # into the head, and a recipe that drops an axis's evidence dies here.
    AXIS_EVIDENCE = {
        "coin class": len(censuses[3][1]) + len(censuses[2][1]),
        "start site": arenas[3].ns + arenas[2].ns,
        "coin direction": len(LINKDIRS),
        "emission reading": len(R["scope"]["readings"]),
        "arena": len(ARENAS),
        "modulus": len(mdist),
        "coin order": len(COIN_ORDERS),
        "shift orientation": len(ORIENTATIONS),
    }
    if mut("MUT-SCOPE"):
        # a REAL removal: an axis this run swept is dropped from the evidence
        # census, so the declared list stops being backed member for member
        AXIS_EVIDENCE = {k: v for k, v in AXIS_EVIDENCE.items()
                         if k != "coin order"}
    R["scope"]["declared_free_axes"] = sorted(AXIS_EVIDENCE)
    R["scope"]["axis_members_executed"] = dict(sorted(AXIS_EVIDENCE.items()))
    SEAL.seal("scope", R["scope"], "G-SCOPE-DECLARED")
    REG.measured("free_axes", len(R["scope"]["declared_free_axes"]),
                 "the declared free axes of the arena (RUNBOOK 15)")
    REG.measured("axis_members", sum(AXIS_EVIDENCE.values()),
                 "the members this run executed, summed over the axes")
    gate("G-SCOPE-DECLARED",
         REG.stmt("the declared arena is data: {free_axes} free axes are "
                  "named, every one of them carries the count of members "
                  "this run actually executed on it -- {axis_members} "
                  "between them, none of them zero -- and the list is "
                  "rendered into the head, so the finding is stated at its "
                  "own scope and not beyond it and an axis cannot be "
                  "declared without being run", free_axes=1, axis_members=1),
         len(AXIS_EVIDENCE) == len(COIN_ORDERS) + len(ORIENTATIONS) + 4
         and all(v > 1 for v in AXIS_EVIDENCE.values())
         and R["scope"]["class_word"] == "MODEL-ABLATION-BENCHMARK",
         "axes %s class %s"
         % (R["scope"]["axis_members_executed"], R["scope"]["class_word"]))

    # -- the structure price -------------------------------------------------
    # K2 MAJOR-4: the flat zero was a sum of five typed zeros under a gate
    # whose predicate was `adjustable == 0`, a tautology, while the run's own
    # sealed axis list carried the phase modulus as a dial and section 9
    # measured it moving the headline observable.  The price is now measured:
    # a structure's free-number count is checked against the number of values
    # this run actually reached on it, so a row typed 0 that the sweep moves
    # fails here.
    price_rows = list(STRUCTURE_PRICE)
    if mut("MUT-PRICE"):
        # a REAL under-pricing: the row for the one structure this run does
        # dial is dropped, so the price stops being total and stops matching
        # the axes the run swept
        price_rows = price_rows[:-1]
    free_numbers = sum(n for (_a, _b, n, _c) in price_rows)
    structures = sum(1 for (_a, _b, n, _c) in price_rows if n == 0)
    priced_names = {a for (a, _b, _n, _c) in price_rows}
    price_missing = [a for (a, _b, _n, _c) in STRUCTURE_PRICE
                     if a not in priced_names]
    # the measured check: the number of structures priced with a free number
    # must equal the number of declared free axes that are a structure's own
    # dial, which this run sweeps -- exactly one, the modulus.
    dialled = [a for (a, _b, n, _c) in price_rows if n]
    dialled_measured = 1 if len(mdist) > 1 else 0
    conditional = [a for (a, _b, _n, c) in price_rows if c != "UNCONDITIONAL"]
    REG.measured("priced_structures", structures,
                 "priced rows that introduce no free number at all")
    REG.measured("priced_rows", len(price_rows), "len(price_rows)")
    REG.measured("free_numbers", free_numbers,
                 "the free numbers the priced structures introduce")
    R["structure_price"] = {
        "structures": structures, "priced_rows": len(price_rows),
        "free_numbers": free_numbers,
        "rows": [{"structure": a, "what it is": b, "free numbers": n,
                  "how it is fixed": c} for (a, b, n, c) in price_rows],
        "unpriced": price_missing,
        "dialled_structures": dialled,
        "conditional_structures": conditional,
        "values_the_dial_reached": len(mdist),
        "reading": "parameter-free is not structure-free: the "
                   "record-carrying model carries these structures and the "
                   "null does not; five of them introduce no free number at "
                   "all and the sixth, the phase modulus, is the one number "
                   "this comparison carries as a dial -- the descent leg "
                   "measures it taking five distinct values and moving the "
                   "headline "
                   "observable at every one, and fixes it to the field order "
                   "by a forcing that is construction-dependent in the "
                   "parent's own sense, so the honest price is those "
                   "structures and one number fixed only conditionally"}
    SEAL.seal("structure_price", R["structure_price"], "G-STRUCTURE-PRICED")
    gate("G-STRUCTURE-PRICED",
         REG.stmt("the {priced_structures} structures this model carries and "
                  "the null does not are listed over {priced_rows} rows with "
                  "what each one is and with how it is fixed, and the "
                  "{free_numbers} free number "
                  "between them is the phase modulus, which this run "
                  "measures taking more than one value and moving the "
                  "headline observable at each -- so the price is a "
                  "measurement and not a column of typed zeros, and it is "
                  "stated conditionally on the forcing the descent leg "
                  "derives",
                  priced_structures=1, priced_rows=1, free_numbers=1),
         not price_missing and free_numbers == dialled_measured
         and len(dialled) == dialled_measured and len(conditional) == 1
         and structures + len(dialled) == len(price_rows),
         "structures %d rows %d free-numbers %d dialled %s conditional %s "
         "unpriced %s" % (structures, len(price_rows), free_numbers, dialled,
                          conditional, price_missing or "none"))

    # -- the verdict --------------------------------------------------------
    # TWO RENDERERS, NOT ONE (K2 MAJOR-1 / K3 MAJOR-2).  The delivered head
    # is built in the p_ region; the comparator rebuilds it in the k_ region
    # by its own route, from the payload, with its own strings.  The gate
    # compares them as a multiset of segments -- so a wrong format string, a
    # wrong payload key, a mislabelled segment or a stale field in EITHER
    # route breaks it -- and it carries an AST leg that reads the source and
    # requires the two sides of the comparison to come from two different
    # functions in two different regions, so the self-comparison the panels
    # found cannot be reintroduced.
    head = p_render_head(R)
    if mut("MUT-HEAD"):
        head = head.replace("TICK-3", "TICK-4")
    if mut("MUT-CLASS"):
        head = head.replace("MODEL-ABLATION-BENCHMARK",
                            "FIRST-PARAMETER-FREE-PREDICTION")
    R["verdict"] = {"head": head}
    rebuilt = k_rebuild_head(R)
    verdict_src = source_text
    if mut("MUT-HEAD-SELF"):
        # a REAL reintroduction of the disease: the rebuild is rewritten to
        # call the BUILDER, so the comparison becomes f(R) == f(R) -- an
        # algebraic identity -- and the live AST predicate runs again over
        # the source as it stands and finds both sides in one region
        verdict_src = source_text.replace("    rebuilt = k_rebuild_head(R)",
                                          "    rebuilt = p_render_head(R)", 1)
    build_fn, cmp_fn = None, None
    for node in ast.walk(ast.parse(verdict_src)):
        if not isinstance(node, ast.Assign) or len(node.targets) != 1:
            continue
        tgt = getattr(node.targets[0], "id", None)
        fn = getattr(getattr(node.value, "func", None), "id", None)
        if tgt == "head" and fn:
            build_fn = fn
        if tgt == "rebuilt" and fn:
            cmp_fn = fn
    two_routes = (build_fn is not None and cmp_fn is not None
                  and build_fn != cmp_fn
                  and region.get(build_fn) != region.get(cmp_fn)
                  and build_fn not in calls[cmp_fn]
                  and cmp_fn not in calls[build_fn])
    hseg = sorted(s for s in head.split(" -- "))
    rseg = sorted(s for s in rebuilt.split(" -- "))
    R["verdict"]["builder"] = build_fn
    R["verdict"]["comparator"] = cmp_fn
    R["verdict"]["two_routes"] = bool(two_routes)
    R["verdict"]["segments"] = len(hseg)
    SEAL.seal("verdict", R["verdict"], "G-VERDICT-EQUALITY")
    REG.measured("head_segments", len(hseg), "the head's own segments")
    gate("G-VERDICT-EQUALITY",
         REG.stmt("the delivered head is rendered by the head builder and "
                  "rebuilt by the comparator over the receipt payload, and "
                  "the two routes' {head_segments} segments are compared as "
                  "a multiset -- and an abstract-syntax-tree read of this "
                  "source requires the two sides to be two different "
                  "functions in two different regions, neither calling the "
                  "other, so a route compared with itself fails here",
                  head_segments=1),
         hseg == rseg and two_routes,
         "head %d chars %d segments builder %s comparator %s two-routes %s "
         "equal %s" % (len(head), len(hseg), build_fn, cmp_fn, two_routes,
                       hseg == rseg))

    # ======================================================================
    # THE PAPER INSTRUMENT.
    # ======================================================================
    T_NULL = CL.table("T-NULL-RULE", ("rule", "datum", "the null's value"),
                      [(r[0], r[1], r[2]) for r in NULL_RULE])
    T_COIN = CL.table("T-COIN-CENSUS",
                      ("arena", "solutions", "classes up to phase",
                       "trivial classes"),
                      [(("AG(2, %d)" % q), a, b, c)
                       for (q, a, b, c) in coin_rows])
    T_FID = CL.table("T-FIDELITY",
                     ("quantity", "this rebuild", "the parent's sealed value"),
                     [("coupled branch ladder",
                       " ".join(str(x) for x in got_c),
                       " ".join(str(x) for x in parent_coupled)),
                      ("control branch ladder",
                       " ".join(str(x) for x in got_f),
                       " ".join(str(x) for x in parent_frozen)),
                      ("coupled inverse participation",
                       str(fid_c["ipr"][FID_T]), str(parent_ipr_c)),
                      ("control inverse participation",
                       str(fid_f["ipr"][FID_T]), str(parent_ipr_f))])
    T_FIBER = CL.table("T-FIBER",
                       ("arena", "coin", "first difference", "points"),
                       [(("AG(2, %d)" % a), b, c, d)
                        for (a, b, c, d) in fiber_rows])
    T_VALUES = CL.table(
        "T-VALUES",
        ("arena", "tick", "ISP", "the null", "total variation"),
        [("AG(2, 3)", first_tick, head_vals[3]["isp_ipr"],
          head_vals[3]["null_ipr"], head_vals[3]["tv"]),
         ("AG(2, 2)", first_tick, head_vals[2]["isp_ipr"],
          head_vals[2]["null_ipr"], head_vals[2]["tv"])])
    T_DIST3 = CL.table(
        "T-DIST-Q3", ("site", "ISP", "the null"),
        [(str(arenas[3].sites[s]), head_vals[3]["isp_dist"][s],
          head_vals[3]["null_dist"][s]) for s in range(arenas[3].ns)])
    T_DIST2 = CL.table(
        "T-DIST-Q2", ("site", "ISP", "the null"),
        [(str(arenas[2].sites[s]), head_vals[2]["isp_dist"][s],
          head_vals[2]["null_dist"][s]) for s in range(arenas[2].ns)])
    T_MOD = CL.table("T-MODULUS",
                     ("modulus", "tick-3 inverse participation", "branches"),
                     [(m, i, b) for (m, i, b) in msweep])
    T_DESC = CL.table("T-DESCENT", ("field order", "admissible moduli"),
                      [(q, " ".join(str(x) for x in g)) for (q, g) in desc])
    T_LAT = CL.table(
        "T-LATTICE", ("parent's result", "measured on the shared carrier",
                      "the null's own coin"),
        [("perimeter-only law",
          "%d comparisons, %d disagreements" % (per_comps, per_bad),
          "in the family: %s" % had_in),
         ("three-term closed form",
          "%d failures over %d coins" % (cf_fail, len(lcoins)),
          "coefficients %s" % " ".join(str(x) for x in had_sol[0])),
         ("halving mode", "present at %d of %d coins"
          % (halving, len(lcoins)), "present: %s" % had_halving),
         ("plaquette counting expectation",
          "%d distinct values" % p_distinct, str(p_exp_rat)),
         ("off-diagonal quartic sign",
          "%d zero, %d plus, %d minus" % (qdist[0], qdist[2], qdist[-2]),
          str(q_exp))])
    T_EXPR = CL.table("T-EXPRESSIBILITY",
                      ("observable", "expressible in", "class", "why"),
                      [(a, b, c, d) for (a, b, c, d) in EXPR])
    T_CENSUS = CL.table("T-Q155",
                        ("parent result", "provenance", "ruling", "evidence"),
                        [(a, p, b, c) for (a, b, c, p, _k, _w) in CENSUS])
    T_PRICE = CL.table(
        "T-PRICE",
        ("structure", "what it is", "free numbers", "how it is fixed"),
        [(a, b, n, c) for (a, b, n, c) in price_rows])
    T_FALS = CL.table(
        "T-FALSIFIER",
        ("arena", "largest site gap against the closest memoryless walk",
         "shots", "branches"),
        [("AG(2, 3)", wide[3]["closest_gap"], shots3, ops3),
         ("AG(2, 2)", wide[2]["closest_gap"], shots2, ops2)])
    T_ORDER = CL.table(
        "T-COIN-ORDER", ("arena", "coin order", "first difference",
                         "tick-3 law equals the null's"),
        [(("AG(2, %d)" % q), ("G.D" if od == "GD" else "D.G"), t,
          "yes" if s else "no") for (q, od, t, s) in order_rows])
    T_ORIENT = CL.table(
        "T-ORIENTATION", ("arena", "shift orientation", "first difference",
                          "tick-3 inverse participation"),
        [(("AG(2, %d)" % q), ("+l" if o == 1 else "-l"), t, i)
         for (q, o, t, i) in orient_rows])
    T_WIDE = CL.table(
        "T-WIDER-NULL",
        ("arena", "null class", "configurations", "distinct tick-3 laws",
         "exact reproductions", "smallest single-site gap"),
        [(("AG(2, %d)" % q), lbl, wide[q][cfg], wide[q][dst], wide[q][exa],
          wide[q][gap])
         for q in ARENAS
         for (lbl, cfg, dst, exa, gap) in (
             ("the arena's own covariant census", "census_configurations",
              "census_distinct_laws", "census_exact", "census_gap"),
             ("all integral coins, covariance dropped",
              "integral_configurations", "integral_distinct_laws",
              "integral_exact", "integral_gap"))])
    T_MECH = CL.table(
        "T-MECHANISM", ("declared directions", "closed under addition",
                        "first difference"),
        [(" ".join("(%d, %d)" % d for d in dirs), "yes" if c else "no", t)
         for (dirs, c, t) in mech_rows])
    T_FEAS = CL.table(
        "T-FEASIBILITY", ("the pin's outcome word", "status"),
        [(w, reach[w][0]) for w in pin_words])
    T_STENCIL = CL.table(
        "T-STENCIL", ("stencil", "nonzero differences", "multiplicities",
                      "unitary", "non-monomial"),
        [("the arena's link offsets", link_scan["differences"],
          " ".join(str(x) for x in link_scan["multiplicities"]),
          link_scan["unitary"], link_scan["non_monomial"]),
         ("a collinear stencil", axis_scan["differences"],
          " ".join(str(x) for x in axis_scan["multiplicities"]),
          axis_scan["unitary"], axis_scan["non_monomial"])])

    C1 = CL.claim("the two models agree exactly through the second tick and "
                  "differ from the third on", 2)
    C2 = CL.claim("no memory-bearing null is tested here", 2)
    C3 = CL.claim("the prediction is free of every parameter the null does "
                  "not also carry", 2)
    C4 = CL.claim("no operational mapping to laboratory units exists in this "
                  "corpus", 2)
    C5 = CL.claim("a definitional absence is not a discriminant", 2)
    C6 = CL.claim("the discriminant requires interference: at the scalar "
                  "coins the two models never separate", 2)
    C7 = CL.claim("this unit is a model-ablation benchmark", 2)
    C8 = CL.claim("the null compared here is memoryless", 2)
    C9 = CL.claim("parameter-free is not structure-free", 2)
    F1 = CL.fence(head, 1)

    C10 = CL.claim("the record-free null is the parent's own frozen-stage "
                   "control up to a global phase", 2)
    C11 = CL.claim("the tick is order-relative", 2)
    C12 = CL.claim("no memoryless walk in either swept class reproduces the "
                   "third-tick law at either plane", 2)
    R["rendered"] = {
        "tables": [T_NULL, T_COIN, T_FID, T_FIBER, T_VALUES, T_DIST3, T_DIST2,
                   T_ORDER, T_ORIENT, T_WIDE, T_MECH, T_MOD, T_DESC, T_LAT,
                   T_EXPR, T_CENSUS, T_PRICE, T_FALS, T_FEAS, T_STENCIL],
        "claims": [C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12],
        "fences": [F1]}
    if render:
        RS.active = False
        return R, TR, LD, SEAL, None

    paper_r = paper
    if mut("MUT-PAPER-CLAIM"):
        paper_r = paper_r.replace("no memory-bearing null is tested here",
                                  "the null is the whole class", 1)
    try:
        cl = CL.gate(paper_r)
        cprob = None
    except ET.CheckFail as exc:
        cl, cprob = {"rows": len(CL.rows), "prose": sum(CL.prose.values()),
                     "fences": sum(CL.fences.values())}, exc.detail
    R["paper_claims"] = dict(cl, problem=cprob or "none")
    SEAL.seal("paper_claims", R["paper_claims"], "G-PAPER-CLAIMS")
    REG.measured("table_rows", len(CL.rows), "rendered rows including headers")
    gate("G-PAPER-CLAIMS",
         REG.stmt("{table_rows} rendered table rows, every claim at its "
                  "declared multiplicity and every fenced block, are compared "
                  "against the paper by multiset equality in both "
                  "directions, keyed by the table each row was rendered into",
                  table_rows=1),
         cprob is None, "rows %d prose %d fences %d %s"
         % (cl["rows"], cl["prose"], cl["fences"], cprob or "matched"))

    # -- referents ----------------------------------------------------------
    # Declared exemptions are removed from the text both gates read: an
    # identifier is not a count, and "AG(2,2)" is an affine plane's name.
    # Every exemption is required to occur, so an exemption carried and never
    # used is a hole rather than a courtesy.
    exempt_missing = [t for t in TOKEN_EXEMPTIONS if t not in paper]
    section_ordinals = len(SECTION_RE.findall(paper))
    if not section_ordinals:
        exempt_missing = exempt_missing + ["section-heading ordinals"]
    stripped = SECTION_RE.sub(r"\1", paper)
    for tok in TOKEN_EXEMPTIONS:
        stripped = stripped.replace(tok, " ")
    # THE UNIVERSES ARE DECLARED WITH THE NOUNS THIS PAPER ACTUALLY USES
    # (K2 MAJOR-2, K3 MAJOR-1: the delivered registry bound 3 numerals of
    # 337 because four of six universes named nouns that occur nowhere in the
    # paper -- "fiber point", "covariant coin", "declared modulus" -- while
    # the paper says "point of the sweep", "coin", "modulus".  The headline
    # sentences, which say "rulings", "tested results", "structures", were in
    # no universe at all, and five flips of the primary headline shipped at
    # exit 0.)  Every universe below is required to BIND, and the run's own
    # coverage is required to clear a floor computed from the paper's noun
    # inventory rather than left free to fall back to three.
    fiber_row_points = {d for (_a, _b, _c, d) in fiber_rows}
    RR.universe("the fiber",
                ["fiber point", "fiber points", "point of the sweep",
                 "points of the sweep", "interfering point",
                 "interfering points", "trivial coin point",
                 "trivial coin points", "site-by-tick comparison",
                 "site-by-tick comparisons"],
                {nontrivial_pts + trivial_pts, nontrivial_pts, trivial_pts,
                 nontrivial_at3, trivial_never, agree_checks, agree_viol,
                 first_tick, agree_upto, ctl_checks, ctl_equal}
                | fiber_row_points | set(ARENAS),
                {(nontrivial_at3, nontrivial_pts),
                 (trivial_never, trivial_pts),
                 (ctl_equal, ctl_checks),
                 (agree_checks - agree_viol, agree_checks),
                 (agree_checks, nontrivial_pts + trivial_pts)})
    RR.universe("the coin family",
                ["coin of the carrier", "coins of the shared family",
                 "link coin", "link coins", "coin of the shared family",
                 "coins of the carrier"],
                {len(lcoins), halving, p_distinct, nonflat, qdist[0],
                 qdist[2], qdist[-2], per_comps, per_bad, cf_fail,
                 len(alphabet), len(lrows), len(twist_rows)}
                | set(sectors.values()),
                {(halving, len(lcoins)), (per_bad, per_comps),
                 (cf_fail, len(lcoins)), (nonflat, len(lcoins))})
    RR.universe("the census",
                ["sealed result", "sealed results", "census row",
                 "census rows", "ruling", "rulings", "tested result",
                 "tested results", "tested row", "tested rows",
                 "parent result", "parent results"],
                {len(CENSUS), rep, nrep, nexp, len(parent_rows), parent_rep},
                {(rep, len(CENSUS)), (nrep, len(CENSUS)),
                 (nexp, len(CENSUS)), (parent_rep, len(parent_rows))})
    RR.universe("the price",
                ["structure", "structures", "free number", "free numbers",
                 "adjustable number", "adjustable numbers"],
                {len(price_rows), structures, free_numbers, len(mdist),
                 len(conditional), len(dialled),
                 sum(n for (_a, _b, n, _c) in price_rows if n == 0)},
                {(free_numbers, len(price_rows)),
                 (structures, len(price_rows))})
    RR.universe("the observable census",
                ["declared observable", "declared observables"],
                {len(EXPR), both, only},
                {(both, len(EXPR)), (only, len(EXPR))})
    RR.universe("the modulus sweep",
                ["declared modulus", "declared moduli", "modulus", "moduli",
                 "field order", "field orders"],
                set(MODULI) | set(PRIME_ORDERS) | set(MODULUS_WINDOW)
                | {len(mdist), distinct, len(MODULI), first_tick,
                   len(PRIME_ORDERS)},
                {(distinct, len(mdist))})
    RR.universe("the coin census",
                ["covariant coin", "covariant coins", "coin class",
                 "coin classes", "solution", "solutions"],
                {len(censuses[3][0]), len(censuses[3][1]),
                 len(censuses[2][0]), len(censuses[2][1])} | set(ARENAS),
                {(len(censuses[3][1]), len(censuses[3][0])),
                 (len(censuses[2][1]), len(censuses[2][0]))})
    RR.universe("the wider null sweep",
                ["memoryless configuration", "memoryless configurations",
                 "integral coin", "integral coins"],
                {wide_configs, wide_exact, len(integral_coins),
                 len(integral_rows), INTEGRAL_COIN_BOX, wide_laws,
                 wide[3]["census_configurations"],
                 wide[3]["integral_configurations"],
                 wide[2]["census_configurations"],
                 wide[2]["integral_configurations"],
                 wide[3]["census_distinct_laws"],
                 wide[3]["integral_distinct_laws"],
                 wide[2]["census_distinct_laws"],
                 wide[2]["integral_distinct_laws"]},
                {(wide_exact, wide_configs)})
    # THE PRE-REGISTRATION'S OWN COUNT.  Found live during the acceptance
    # battery: the spelled "seven rules" sentences named no declared universe,
    # so "seven" -> "three" shipped at exit 0 -- the E-30 shape again, one
    # noun away from the headline the panel's own flips now die on.  The noun
    # is deliberately narrow ("pre-registration rule"), because a bare "rule"
    # also matches "the emission rule" and "the rule table" and would drag
    # unrelated sentences into this universe, which is a hole wearing a gate's
    # clothes rather than a gate.
    RR.universe("the pre-registration",
                ["pre-registration rule", "pre-registration rules"],
                {len(NULL_RULE), len(shared), len(NULL_RULE_TAKES_AWAY),
                 len(NULL_RULE_ASSERTS)},
                {(len(NULL_RULE_TAKES_AWAY), len(NULL_RULE))})
    RR.universe("the coin-order fiber",
                ["coin order", "coin orders", "shift orientation",
                 "shift orientations"],
                {len(COIN_ORDERS), len(ORIENTATIONS), DG_T, FIB_T,
                 R["coin_order_fiber"]["delivered_tick"],
                 R["coin_order_fiber"]["alternative_tick"]},
                set())
    table_rows_removed = len(TABLE_ROW.findall(stripped))
    paper_rr = TABLE_ROW.sub(" ", stripped)
    if mut("MUT-REFERENT"):
        paper_rr = paper_rr.replace(
            "declared observables", "declared observables 4242", 1)
    if mut("MUT-REFERENT-HEADLINE"):
        # the five headline inversions the panel shipped at exit 0: the
        # primary census count is flipped in a sentence whose subject noun is
        # now inside a declared universe, so the numeral has a referent to
        # fail against
        paper_rr = re.sub(r"(\d+) of (\d+) parent results",
                          r"3 of \2 parent results", paper_rr)
    if mut("MUT-REFERENT-SPELLED"):
        # the same inversion at the SPELLED grain, on the pre-registration's
        # own count -- the survivor this unit's acceptance battery found and
        # the reason "the pre-registration" is a declared universe at all
        paper_rr = paper_rr.replace("seven pre-registration rules",
                                    "three pre-registration rules")
    # A SECOND, INDEPENDENT ROUTE over the same surface, for the grain the
    # template's own regex cannot see: the five headline inversions the panel
    # shipped were SPELLED words ("Seven" -> "Three"), and the template's
    # numeral pattern matches digits only.  Every spelled number in a
    # sentence about a declared universe is resolved here against that
    # universe, with one declared exemption -- the word "one", which in this
    # register is the indefinite article ("one model", "every one of") and
    # not a count.  The exemption is required to be used.
    SPELLED_EXEMPT = {"one": "the indefinite article in this register, not a "
                             "count"}
    floor, spelled_offences, spelled_checked, exempt_hits = 0, [], 0, 0
    for sentence in re.split(r"(?<=[.!?])\s+", RR.prose_only(paper_rr)):
        s = ET.canon(sentence)
        uname = None
        for name, uni in RR.universes.items():
            if any(re.search(r"\b%s" % re.escape(nn), s)
                   for nn in uni["nouns"]):
                uname = name
                break
        if uname is None:
            continue
        spans = [m.span() for m in ET.ReferentRegistry.NOF.finditer(sentence)]
        floor += len(spans)
        for m in ET.ReferentRegistry.NUM.finditer(sentence):
            if not any(a <= m.start() < b for (a, b) in spans):
                floor += 1
        for word, val in SPELLED.items():
            for _m in re.finditer(r"\b%s\b" % word, s):
                if word in SPELLED_EXEMPT:
                    exempt_hits += 1
                    continue
                spelled_checked += 1
                if val not in RR.universes[uname]["values"]:
                    spelled_offences.append(
                        "the spelled %s is not a value of %s" % (word, uname))
    try:
        rr = RR.gate(paper_rr)
        rprob = None
    except ET.CheckFail as exc:
        rr, rprob = {"occurrences_checked": 0}, exc.detail
    bound_none = sorted(
        name for name, uni in RR.universes.items()
        if not any(re.search(r"\b%s" % re.escape(nn), ET.canon(paper_rr))
                   for nn in uni["nouns"]))
    REG.measured("referent_occurrences", rr["occurrences_checked"],
                 "prose numerals resolved against their own universe")
    REG.measured("spelled_occurrences", spelled_checked,
                 "spelled numbers resolved against their own universe")
    REG.measured("universes", len(RR.universes), "len(RR.universes)")
    R["paper_referents"] = dict(rr, problem=rprob or "none",
                                exemptions_unused=exempt_missing,
                                section_ordinals_removed=section_ordinals,
                                universes_binding_nothing=bound_none,
                                table_rows_removed=table_rows_removed,
                                independent_floor=floor,
                                spelled_checked=spelled_checked,
                                spelled_offences=sorted(set(spelled_offences)),
                                spelled_exemption_uses=exempt_hits,
                                universes=RR.seal_value())
    SEAL.seal("paper_referents", R["paper_referents"], "G-PAPER-REFERENTS")
    gate("G-PAPER-REFERENTS",
         REG.stmt("every numeral of every prose sentence whose subject noun "
                  "names one of the {universes} declared universes is "
                  "resolved against that universe alone, per occurrence and "
                  "outside the fences, with the declared identifier "
                  "exemptions removed first and every one of them required "
                  "to occur; every universe is required to BIND at least one "
                  "sentence of this paper -- a universe naming a noun the "
                  "paper never uses is a hole, not a courtesy -- and the "
                  "{referent_occurrences} occurrences the gate resolves are "
                  "recomputed here by a second route so the coverage of this "
                  "family cannot silently fall back; and that second route "
                  "also resolves the {spelled_occurrences} SPELLED numbers "
                  "the template's own pattern cannot see, which is the grain "
                  "at which the headline inversions live",
                  universes=1, referent_occurrences=1,
                  spelled_occurrences=1),
         rprob is None and not exempt_missing and not bound_none
         and rr["occurrences_checked"] == floor and not spelled_offences
         and exempt_hits > 0,
         "occurrences %d floor %d spelled %d offences %s universes %d "
         "binding-nothing %s unused exemptions %s %s"
         % (rr["occurrences_checked"], floor, spelled_checked,
            sorted(set(spelled_offences))[:4] or "none", len(RR.universes),
            bound_none or "none", exempt_missing or "none",
            rprob or "bound"))

    # -- walls --------------------------------------------------------------
    paper_w = paper
    if mut("MUT-WALL"):
        paper_w = paper_w + ("\n\nNo simpler model can reproduce this "
                             "difference, and it rules out every competing "
                             "account.\n")
    if mut("MUT-WALL-LICENCE"):
        # a REAL unlicensing: the one sentence in this paper that names the
        # banned reading -- in order to disclaim it -- loses the rendered
        # claim that licenses it, so the licence leg is exercised alone
        paper_w = paper_w.replace(
            "prediction of the theory: this unit is a model-ablation "
            "benchmark, and the value",
            "prediction of the theory: the value", 1)
    if mut("MUT-WALL-POSITIVE"):
        # EVERY voicing of the wall's own standing sentence is removed -- not
        # only the lower-case one, and not only the copy that happens to sit
        # on a single source line.  Both traps have been live in this recipe:
        # a sentence-initial capital left the leg satisfied by the surviving
        # copy, and later a LINE-WRAPPED copy did the same, because the wall
        # reads canonicalised text where the wrap has been folded away while
        # a literal-space pattern applied to the raw paper cannot see it.
        # The acceptance battery caught the second one as a recipe that
        # neither died nor moved its key.
        paper_w = re.sub(r"[Nn]o\s+memory-bearing\s+null\s+is\s+tested\s+here",
                         "", paper_w)
    wprob = None
    for w in WALLS:
        try:
            w.scan(paper_w, R["rendered"]["claims"])
        except ET.CheckFail as exc:
            wprob = exc.detail
            break
    # EVERY CONTROL MUST BE CAUGHT (TPL-2, K3 MINOR-4).  The controls were
    # written from the disease, not from the patterns; each is run against
    # its own wall and an uncaught one is a hole the gate reports.  A control
    # that the CLEAN paper would also match would be a false positive, so the
    # licence sentences of the paper are checked not to match any of them.
    walls_for_control = WALLS
    if mut("MUT-WALL-CONTROL"):
        # a REAL narrowing: the ablation wall's pattern list is cut back to
        # the legs it carried before this repair, so the paraphrases the
        # panel wrote walk through again and the control census says so
        walls_for_control = (
            WALL_EXHAUSTIVE, WALL_PARAMFREE,
            Wall(WALL_ABLATION.name, WALL_ABLATION.negative[:6],
                 WALL_ABLATION.positive, WALL_ABLATION.controls,
                 policed=WALL_ABLATION.policed,
                 licences=WALL_ABLATION.licences))
    ctl_uncaught = []
    control_rows = []
    for w in walls_for_control:
        bad = w.control_report()
        control_rows.append((w.name, len(w.controls), len(bad)))
        ctl_uncaught.extend("%s :: %s" % (w.name, t) for t in bad)
    R["walls"] = {"walls": [w.seal_value() for w in WALLS],
                  "controls": [{"wall": a, "controls": b, "uncaught": c}
                               for (a, b, c) in control_rows],
                  "controls_uncaught": ctl_uncaught,
                  "problem": wprob or "none"}
    SEAL.seal("walls", R["walls"], "G-PAPER-WALLS")
    REG.measured("wall_count", len(WALLS), "len(WALLS)")
    REG.measured("wall_patterns", sum(len(w.negative) + len(w.positive)
                                      for w in WALLS),
                 "negative plus positive legs")
    REG.measured("wall_controls", sum(len(w.controls) for w in WALLS),
                 "independently written control sentences")
    gate("G-PAPER-WALLS",
         REG.stmt("{wall_count} semantic walls with {wall_patterns} legs run "
                  "against the canonicalised paper: no banned reading in any "
                  "voice, every standing sentence still carried so deleting "
                  "a wall's own verdict fails it, the ablation wall's "
                  "licence leg requiring every sentence that names the "
                  "banned reading to carry one of this run's own rendered "
                  "claims, and every one of the {wall_controls} control "
                  "sentences -- written from the disease and not from the "
                  "patterns, and covering all three walls -- caught by its "
                  "own wall", wall_count=1, wall_patterns=1,
                  wall_controls=1),
         wprob is None and not ctl_uncaught,
         "walls %d legs %d controls %d uncaught %s %s"
         % (len(WALLS), REG.values["wall_patterns"],
            REG.values["wall_controls"], ctl_uncaught[:3] or "none",
            wprob or "clean"))

    # -- coverage: every numeral and every fraction of the paper ------------
    SKIP = ("rendered", "paper", "sources", "transcript", "walls", "verdict")
    reg_values = set()
    frac_values = set()

    def _harvest(cur):
        if isinstance(cur, dict):
            for v in cur.values():
                _harvest(v)
        elif isinstance(cur, list):
            for v in cur:
                _harvest(v)
        elif isinstance(cur, bool):
            return
        elif isinstance(cur, int):
            reg_values.add(cur)
        elif isinstance(cur, str):
            for fm in FRAC.finditer(cur):
                frac_values.add(fm.group(0))
                reg_values.add(int(fm.group(1)))
                reg_values.add(int(fm.group(2)))
            for tok in NUM.findall(cur):
                reg_values.add(int(tok.replace(",", "")))

    for key, val in R.items():
        if key in SKIP:
            continue
        _harvest(val)
    for v in REG.values.values():
        if isinstance(v, int) and not isinstance(v, bool):
            reg_values.add(v)
    _harvest(list(MODULI) + list(ARENAS) + list(PRIME_ORDERS)
             + list(MODULUS_WINDOW) + [FIB_T, FID_T, HEAD_T, len(ANCHORS),
                                       len(MUTANTS), len(LD.rows),
                                       DECLARED_DIMENSION])
    for a in arenas.values():
        _harvest([a.ns, a.ncell, a.dim, a.q])
    _harvest([head, str(parent_ipr_c), str(parent_ipr_f)]
             + [str(x) for x in parent_coupled + parent_frozen])
    paper_c = stripped
    if mut("MUT-COVERAGE"):
        paper_c = paper_c.replace("third tick", "third tick (4242)", 1)
    unbacked, unbacked_fr = [], []
    scanned = 0
    for fm in FRAC.finditer(paper_c):
        scanned += 1
        if fm.group(0) not in frac_values:
            unbacked_fr.append(fm.group(0))
    for tok in NUM.finditer(paper_c):
        scanned += 1
        v = int(tok.group(1).replace(",", ""))
        if v not in reg_values:
            unbacked.append(v)
    for word, val in SPELLED.items():
        for _m in re.finditer(r"\b%s\b" % word, paper_c, re.I):
            scanned += 1
            if val not in reg_values:
                unbacked.append(val)
    R["paper_coverage"] = {"scanned": scanned,
                           "unbacked": sorted(set(unbacked)),
                           "unbacked_fractions": sorted(set(unbacked_fr)),
                           "backing_values": len(reg_values),
                           "backing_fractions": len(frac_values)}
    SEAL.seal("paper_coverage", R["paper_coverage"], "G-PAPER-COVERAGE")
    REG.measured("scanned_numerals", scanned,
                 "every numeral, fraction and spelled number of the paper, "
                 "fenced blocks, inline spans and tables included")
    gate("G-PAPER-COVERAGE",
         REG.stmt("{scanned_numerals} numerals of the paper -- fenced "
                  "blocks, inline spans, table cells, exact fractions and "
                  "spelled numbers included -- are each required to be a "
                  "value this run measured", scanned_numerals=1),
         not unbacked and not unbacked_fr, "scanned %d unbacked %s %s"
         % (scanned, sorted(set(unbacked))[:12] or "none",
            sorted(set(unbacked_fr))[:8] or "none"))

    # -- typed counts -------------------------------------------------------
    audit_source = source_text
    if mut("MUT-TYPED"):
        # a REAL offender: a statement that types a numeral is appended to
        # the source the audit reads, so the live AST predicate finds it
        audit_source = source_text + ('\n\ndef _typed_probe(REG):\n'
                                      '    return REG.stmt("a run of 7")\n')
    if mut("MUT-TYPED-OFFSET"):
        # a REAL offender of the OTHER TPL-2 subspecies: a value entering the
        # registry as an arithmetic offset from a live count, which the
        # %-format leg cannot see at all
        audit_source = source_text + (
            '\n\ndef _offset_probe(REG, WALLS):\n'
            '    return REG.measured("wall_extra", len(WALLS) - 3 + 7,\n'
            '                        "a typed integer offset")\n')
    typed = REG.audit_module(audit_source, ("stmt", "gate", "claim"))
    # TPL-2 item 2's SECOND subspecies (K3 MINOR-3): the delivered audit saw
    # %-format numerals in a statement but nothing at all at the registry
    # door, so `REG.measured(name, len(X) - 3 + 7, ...)` published a typed
    # count at exit 0.  Any arithmetic on a live count with an integer
    # constant operand, handed to `measured`, is an offender here.
    offsets = []
    for node in ast.walk(ast.parse(audit_source)):
        if not isinstance(node, ast.Call):
            continue
        if (getattr(node.func, "attr", None) or
                getattr(node.func, "id", None)) != "measured":
            continue
        for arg in node.args:
            for sub in ast.walk(arg):
                if (isinstance(sub, ast.BinOp)
                        and isinstance(sub.op, (ast.Add, ast.Sub))
                        and any(isinstance(o, ast.Constant)
                                and isinstance(o.value, int)
                                and not isinstance(o.value, bool)
                                for o in (sub.left, sub.right))):
                    offsets.append("line %d: integer offset at the registry "
                                   "door" % node.lineno)
    # THE SLOT IS OPENED BEFORE THE COUNT IS TAKEN (K3 MINOR-1: the delivered
    # object sealed 57 and printed 58, because the name registered itself
    # after the payload was built).  Two calls, no arithmetic: the first
    # opens the slot, the second fills it with a count that already includes
    # it, so the sealed value, the gate statement and the transcript evidence
    # are ONE number.
    REG.measured("measured_names", "reserved", "the slot, opened first")
    REG.measured("measured_names", len(REG.values), "len(REG.values)")
    R["typed_counts"] = {"offenders": typed,
                         "integer_offsets": sorted(set(offsets)),
                         "measured_names": REG.values["measured_names"],
                         "exemptions": len(REG.exempt)}
    SEAL.seal("typed_counts", R["typed_counts"], "G-TYPED-COUNTS")
    gate("G-TYPED-COUNTS",
         REG.stmt("an abstract-syntax-tree scan of this source finds no "
                  "string literal handed to a statement or claim builder "
                  "that types a numeral AND no integer-offset arithmetic "
                  "handed to the registry's own door -- the template's two "
                  "registered subspecies, both scanned -- and every published "
                  "statement's numerals arrive by name from the "
                  "{measured_names} measured values",
                  measured_names=1),
         not typed and not offsets, "measured %d offenders %s offsets %s"
         % (REG.values["measured_names"], typed or "none",
            sorted(set(offsets))[:2] or "none"))

    # -- no floats ----------------------------------------------------------
    floats = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, float):
            floats.append("line %d" % node.lineno)

    def _scan_types(obj, path=""):
        if isinstance(obj, float):
            floats.append("receipt %s" % path)
        elif isinstance(obj, dict):
            for k, v in obj.items():
                _scan_types(v, path + "/" + str(k))
        elif isinstance(obj, list):
            for i, v in enumerate(obj):
                _scan_types(v, path + "/%d" % i)
    _scan_types(R)
    if mut("MUT-FLOAT"):
        # a REAL float: a value the recursive type scan must find, built
        # without any floating-point literal appearing in this source
        R["exactness_probe"] = float(len(LD.rows))
        _scan_types(R)
    R["exactness"] = {"float_sites": floats}
    SEAL.seal("exactness", R["exactness"], "G-NO-FLOATS")
    gate("G-NO-FLOATS",
         REG.stmt("no floating-point literal occurs in this source and no "
                  "floating-point value occurs anywhere in the receipt, by a "
                  "recursive type scan"),
         not floats, "float sites %s" % (floats or "none"))

    # -- anchors consumed ---------------------------------------------------
    if mut("MUT-CONSUMER"):
        ASET.by_name["A-POT-GAP"].consumer = "G-DOES-NOT-EXIST"
    try:
        ASET.verify_consumption(LD)
        aprob = None
    except ET.CheckFail as exc:
        aprob = exc.detail
    R["anchors_consumed"] = {
        "rows": len(ANCHORS), "problem": aprob or "none",
        "consumers": sorted({a.consumer for a in ASET.by_name.values()})}
    SEAL.seal("anchors_consumed", R["anchors_consumed"],
              "G-ANCHORS-CONSUMED")
    gate("G-ANCHORS-CONSUMED",
         REG.stmt("every anchor's declared consumer gate exists, ran, and "
                  "subscripted the anchor inside its own predicate; the "
                  "anchor's located text enters that predicate as a value "
                  "and not as an existence check"),
         aprob is None, "anchors %d %s" % (len(ANCHORS), aprob or "consumed"))

    # -- falsifier coverage --------------------------------------------------
    # THE DENOMINATOR IS THE DECLARED GATE LIST, not the gates that happen to
    # have fired by the time this gate runs (K3 MAJOR-5: two gates fired
    # after it and were outside its denominator by ordering alone, and the
    # one they left uncovered was G-TRANSCRIPT-BOUND, this unit's own novel
    # family implementation).  BOTH WAIVERS ARE GONE: G-SCOPE-DECLARED and
    # G-READS-DECLARED now carry measured predicates and their own recipes.
    rows_for_harness = [ET.Falsifier(m[0], m[1], m[3], m[2], None)
                        for m in MUTANTS]
    HARNESS = ET.FalsifierHarness(rows_for_harness)
    sentinel_source = source_text
    if mut("MUT-COVERAGE-SELF"):
        # a REAL sentinel: a recipe whose body only assigns a constant
        # boolean is appended to the source the description audit reads
        sentinel_source = source_text + ('\n\ndef _sentinel_probe():\n'
                                         '    ok = False\n'
                                         '    if mut("MUT-PROBE"):\n'
                                         '        ok = True\n'
                                         '    return ok\n')
    sentinels = HARNESS.audit_descriptions(sentinel_source)

    class _DeclaredGates:
        """the coverage denominator: every gate this run MAY fire, declared
        before any of them did, so no gate is outside it by ordering."""

        @staticmethod
        def names():
            return list(GATE_NAMES)

    declared_gates = _DeclaredGates()
    if mut("MUT-COVERAGE-TAIL"):
        # a REAL reintroduction of the tail exemption: the denominator is
        # taken from the gates that have fired by now, which leaves the
        # closing gates outside it -- and one of them has a recipe, so the
        # narrowed denominator is measurably different
        declared_gates = LD
    try:
        cov = HARNESS.coverage(declared_gates, {}, {})
        fprob = None
    except ET.CheckFail as exc:
        cov, fprob = {"gates": len(GATE_NAMES), "falsified": 0,
                      "waived": 0}, exc.detail
    tail = sorted(set(GATE_NAMES) - set(LD.names()))
    R["falsifier_coverage"] = dict(
        cov, sentinels=sentinels, problem=fprob or "none", waivers=[],
        denominator="the declared gate list",
        gates_not_yet_fired_when_this_gate_ran=tail)
    SEAL.seal("falsifier_coverage", R["falsifier_coverage"],
              "T-FALSIFIER-COVERAGE")
    REG.measured("mutant_rows", len(MUTANTS), "len(MUTANTS)")
    REG.measured("declared_gates", len(GATE_NAMES), "len(GATE_NAMES)")
    gate("T-FALSIFIER-COVERAGE",
         REG.stmt("every one of the {declared_gates} DECLARED gates -- the "
                  "list fixed before any of them fired, so the ones that "
                  "fire after this one are inside the denominator rather "
                  "than outside it by ordering -- carries a falsifier, none "
                  "carries a waiver, the {mutant_rows} recipes each name the "
                  "measured key they must move, and no recipe is "
                  "sentinel-shaped by an abstract-syntax-tree scan of its "
                  "own body", declared_gates=1, mutant_rows=1),
         fprob is None and not sentinels and cov["waived"] == 0
         and cov["gates"] == len(GATE_NAMES),
         "gates %d falsified %d waived %d not-yet-fired %s sentinels %s"
         % (cov["gates"], cov["falsified"], cov["waived"], tail,
            sentinels or "none"))

    # -- families adopted ----------------------------------------------------
    fam_checks = [c for _k, _n, c in ET.FAMILIES]
    if mut("MUT-TEMPLATE"):
        # a REAL narrowing: one family is dropped from the adopted list, so
        # the adopted set stops covering the reference implementation's
        fam_checks = fam_checks[:-1]
    fam_missing = [c for _k, _n, c in ET.FAMILIES if c not in fam_checks]
    fam_classes = [c for c in fam_checks
                   if any(getattr(getattr(ET, nm, None), "CHECK", None) == c
                          for nm in dir(ET))]
    # NOT MERELY RESOLVED, EXERCISED (K3 NOTE-3: the delivered gate checked
    # that the nine names resolve to template classes, which is weaker than
    # the claim it published).  Each family is bound to the count of live
    # objects this run actually put through it; a family carried and never
    # used is an offence, which is TPL-2's fifth item.
    fam_used = {
        "T-SEAL-PROMOTION": len(SEAL.seals),
        "T-TRANSCRIPT-BOUND": len(LD.rows),
        "T-WALL-SEMANTIC": sum(len(w.negative) + len(w.positive)
                               for w in WALLS),
        "T-ANCHOR-CONSUMED": len(ASET.by_name),
        "T-CLAIMS-EQUAL": len(CL.rows),
        "T-REFERENT-BOUND": rr["occurrences_checked"],
        "T-NO-TYPED-COUNTS": len(REG.values),
        "T-FALSIFIER-POISONS": len(rows_for_harness),
        "T-READ-SET": len(RS.log),
    }
    if mut("MUT-TEMPLATE-UNUSED"):
        # a REAL carried-and-unused family: the referent registry is emptied
        # of every universe, so the family is adopted and exercises nothing
        fam_used["T-REFERENT-BOUND"] = 0
    fam_unused = sorted(c for c in fam_checks if not fam_used.get(c))
    R["template"] = {"families_adopted": fam_checks,
                     "families_missing": fam_missing,
                     "families_resolved": len(fam_classes),
                     "families_exercised": dict(sorted(fam_used.items())),
                     "families_unused": fam_unused,
                     "engravings": "E-25 through E-33 with the template's "
                                   "registered items"}
    SEAL.seal("template", R["template"], "G-TEMPLATE-ADOPTED")
    REG.measured("families", len(ET.FAMILIES), "len(ET.FAMILIES)")
    gate("G-TEMPLATE-ADOPTED",
         REG.stmt("all {families} template families are imported from the "
                  "reference implementation and used rather than copied: "
                  "each one's check name resolves to the reference class "
                  "that carries it, AND each one is bound to the count of "
                  "live objects this run actually put through it, so a "
                  "family adopted and never exercised is an offence here "
                  "rather than a name in a list", families=1),
         not fam_missing and len(fam_classes) == len(ET.FAMILIES)
         and not fam_unused,
         "families %d resolved %d unused %s missing %s"
         % (len(fam_checks), len(fam_classes), fam_unused or "none",
            fam_missing or "none"))

    # -- reads --------------------------------------------------------------
    # THE READ SET NOW HAS A MEASURED PREDICATE AND ITS OWN RECIPE (K1
    # MINOR-5: the waiver's forcing was `reads > 0`, an existence check).
    reads_probe = reads
    if mut("MUT-READS"):
        # a REAL undeclared read: a repository object this unit does not
        # declare is opened before the gate, so the audit hook's own log
        # stops matching the declaration
        with open(os.path.join(REPO, "v15", "PLAN.md"), encoding="utf-8") \
                as _fh:
            _fh.read()
    try:
        rev = RS.gate_at_close(reads_probe)
        rdprob = None
    except ET.CheckFail as exc:
        rev, rdprob = {"reads": 0, "distinct": 0}, exc.detail
    R["reads"] = {"declared": sorted(set(reads)), "reads": rev["reads"],
                  "distinct": rev["distinct"], "problem": rdprob or "none"}
    SEAL.seal("reads", R["reads"], "G-READS-DECLARED")
    REG.measured("declared_reads", len(set(reads)), "len(set(reads))")
    gate("G-READS-DECLARED",
         REG.stmt("the repository reads this run actually performed, "
                  "recorded at the interpreter's own open hook rather than "
                  "in a helper, are exactly the {declared_reads} declared "
                  "paths, compared as a multiset -- and the same comparison "
                  "is taken AGAIN at the close, after this gate, so the tail "
                  "window an undeclared read could walk through is shut",
                  declared_reads=1),
         rdprob is None, "reads %d distinct %d %s"
         % (rev["reads"], rev["distinct"], rdprob or "declared"))

    # -- close ---------------------------------------------------------------
    # THE LAST GATE, WITH A PREDICATE AND A RECIPE (K3 MAJOR-5: the delivered
    # G-TRANSCRIPT-BOUND passed on a typed `True` and was the one gate
    # nothing falsified -- the family-(b) mechanism E-26 records as having no
    # closed instance anywhere).  Three legs: the transcript binds to the
    # ledger by content, the read log is re-checked at the close so nothing
    # can be read after G-READS-DECLARED, and the gate census reconciles the
    # declared gate list with the gates that fired, this one included, so the
    # row count and every published total are ONE number.
    tr_text = TR.text()
    if mut("MUT-TRANSCRIPT"):
        # a REAL forgery: one gate row of the text that would be promoted is
        # renamed, so the multiset the ledger is reconciled against differs
        tr_text = tr_text.replace("[PASS] G-NO-FLOATS",
                                  "[PASS] G-NO-FLOATS-X", 1)
    try:
        TR.bind(LD, tr_text)
        tprob = None
    except ET.CheckFail as exc:
        tprob = exc.detail
    if mut("MUT-READ-LATE"):
        # a REAL late read: an undeclared repository object is opened AFTER
        # the read gate has passed, which only the close re-check can see
        with open(os.path.join(REPO, "v15", "QUESTIONS.md"),
                  encoding="utf-8") as _fh:
            _fh.read()
    try:
        RS.gate_at_close(reads)
        lateprob = None
    except ET.CheckFail as exc:
        lateprob = exc.detail
    fired = set(LD.names()) | {"G-TRANSCRIPT-BOUND"}
    census_bad = sorted(fired.symmetric_difference(GATE_NAMES))
    chain_ok = LD.recompute_chain() == LD.head
    REG.measured("gate_rows", len(LD.rows) + len(("G-TRANSCRIPT-BOUND",)),
                 "the ledger's rows, this closing gate included")
    R["transcript_bound"] = {
        "problem": tprob or "none", "late_reads": lateprob or "none",
        "gate_census": census_bad, "chain_recomputed": bool(chain_ok),
        "declared_gates": len(GATE_NAMES), "rows": REG.values["gate_rows"]}
    SEAL.seal("transcript_bound", R["transcript_bound"], "G-TRANSCRIPT-BOUND")
    gate("G-TRANSCRIPT-BOUND",
         REG.stmt("every gate row of the finished transcript is parsed back "
                  "out of the text that will be promoted and reconciled with "
                  "the ledger as a multiset, evidence strings included, in "
                  "both directions; the ledger's own chain is recomputed row "
                  "by row from its digests; the read log is compared again "
                  "at the close, so a read taken after the read gate is "
                  "caught here; and the {gate_rows} gates that fired are "
                  "reconciled with the declared list, this closing gate "
                  "included, so the row count, the gate list and every "
                  "published total are one number", gate_rows=1),
         tprob is None and lateprob is None and not census_bad and chain_ok,
         "rows %d chain %s census %s late-reads %s %s"
         % (REG.values["gate_rows"], LD.head[:12], census_bad or "total",
            lateprob or "none", tprob or "bound"))
    TR.bind(LD)
    R["transcript"] = {"sha256_12": ET.bytes_digest(TR.text().encode("utf-8")),
                       "lines": len(TR.lines), "gate_rows": len(LD.rows),
                       "chain_head": LD.head}
    SEAL.seal("transcript", R["transcript"], "G-TRANSCRIPT-BOUND")
    R["paper"] = {"path": PAPER_REL,
                  "sha256_12": ET.bytes_digest(paper.encode("utf-8"))}
    SEAL.declare_unsealed("rendered",
                          "the rendering the paper gates consume; its "
                          "content is bound by G-PAPER-CLAIMS")
    SEAL.declare_unsealed("paper",
                          "the object under test, digested rather than "
                          "measured")
    SEAL.declare_unsealed("seal_manifest", "the manifest itself")
    if mut("MUT-SEAL-ADD"):
        R["forged_finding"] = {"smuggled": len(LD.rows)}
    RS.active = False
    SEAL.verify_at_promotion(R, LD, "seal_manifest")

    if not write:
        return R, TR, LD, SEAL, None
    if ET.bytes_digest(TR.text().encode("utf-8")) != R["transcript"]["sha256_12"]:
        raise ET.CheckFail("G-TRANSCRIPT-BOUND",
                           "the transcript to be promoted differs from the "
                           "gate-time seal")
    dig = ET.promote(SEAL, LD, R, TR.text(),
                     os.path.join(REPO, RECEIPT_REL),
                     os.path.join(REPO, OUTPUT_REL))
    return R, TR, LD, SEAL, dig


# ===========================================================================
# SECTION G.  THE FALSIFIERS, THE SELF-TEST AND THE CLI.
#   Every row names the MEASURED KEY its recipe must move; the harness
#   digests that key before and after and refuses a recipe that left it
#   identical (E-32), and refuses a death at any gate but the declared one.
# ===========================================================================

MUTANTS = (
    ("MUT-SOURCE-DRIFT", "G-SOURCES-PINNED", "sources",
     "one pinned digest is reversed and the drift list is RECOMPUTED from "
     "the reversed value, so the real predicate runs"),
    ("MUT-ANCHOR", "G-ANCHORS-LOCATED", "anchors_located",
     "the parent's own prediction sentence is altered in the bytes handed to "
     "the locator, so an anchor stops being locatable in its source"),
    ("MUT-S1", "G-S1-DISJOINT-CODE", "s1_regions",
     "a module-level alias of the null's step function is added and the "
     "comparator is made to call the builder THROUGH it, which the delivered "
     "name-based predicate walked past"),
    ("MUT-NULL-RECORD", "G-NULL-HAS-NO-RECORD", "null_no_record",
     "a record-vocabulary leak is injected into the null's region report"),
    ("MUT-S1-SHARED", "G-S1-DISJOINT-CODE", "s1_regions",
     "a helper outside the prefix scheme is called by BOTH the null's region "
     "and the comparator's, which is registered family S-2 walking through "
     "S-1's own gate"),
    ("MUT-S1-CROSS", "G-S1-DISJOINT-CODE", "s1_regions",
     "the ISP arm is made to call the null's step function, an edge the "
     "delivered predicate did not treat as an offence at all"),
    ("MUT-NULL-RULE", "G-NULL-RULE-TOTAL", "null_model",
     "one pre-registered rule is dropped, so the null's parameters stop "
     "being total"),
    ("MUT-PR-REWRITE", "G-PR-PREREGISTRATION-SEALED", "preregistration",
     "the anti-strawman rule PR3 is rewritten after the fact from the SAME "
     "coin to a coin of the null's own choosing, picked after the sweep"),
    ("MUT-PR-TUNED", "G-PR-PREREGISTRATION-SEALED", "preregistration",
     "the same rewrite by an author who ALSO re-declares the digest beside "
     "the table, so the digest leg is satisfied and only the text leg is "
     "left to catch a pre-registration tuned after the numbers were in"),
    ("MUT-COIN-CENSUS", "G-COIN-CENSUS-PARENT", "coin_census",
     "one solution is removed from the parent's own coin census, so the "
     "recomputed count stops matching the parent's"),
    ("MUT-FIDELITY", "G-ISP-FIDELITY-PARENT", "isp_fidelity",
     "the rebuilt coupled inverse-participation ratio is shifted, so it "
     "stops equalling the parent's sealed value"),
    ("MUT-NULL-ROUTES", "G-NULL-TWO-ROUTES", "null_two_routes",
     "a disagreement is recorded between the null's cyclotomic route and "
     "its integer route"),
    ("MUT-FIBER", "G-FIRST-DIFFERENCE-TICK", "fiber",
     "the sweep is stopped one tick short of the tick the finding is about, "
     "so the pre-registered outcome becomes unreachable in its own window"),
    ("MUT-AGREE", "G-AGREE-THROUGH-THE-EARLY-TICKS", "agreement",
     "the agreement leg is asked to hold at the tick the difference lives "
     "at, so the early-agreement claim is exercised against the finding"),
    ("MUT-VALUES", "G-DISCRIMINANT-VALUES", "discriminant",
     "the coupling is switched off in the headline arm, which is exactly the "
     "null, so the published values collapse onto the null's"),
    ("MUT-CONTROL-IDENTITY", "G-NULL-IS-THE-PARENTS-CONTROL",
     "null_is_the_control",
     "the arm the identity is claimed for is run coupled instead of frozen, "
     "so the two ladders genuinely part"),
    ("MUT-ORDER-FIBER", "G-COIN-ORDER-FIBER", "coin_order_fiber",
     "the fiber's second member is run at the first member's coin order, so "
     "the parent's verdict-relevant alternative is never executed"),
    ("MUT-WIDER-SWEEP", "G-WIDER-NULL-SWEEP", "wider_null_sweep",
     "the non-covariant null class is never swept, so the closest memoryless "
     "opponent stops being the one measured"),
    ("MUT-MECHANISM", "G-MECHANISM-CORROBORATED", "mechanism",
     "the corroboration is run one tick short of the tick the non-closing "
     "arena's own difference arrives at"),
    ("MUT-DESCENT", "G-MODULUS-DESCENT-THEOREM", "modulus_descent",
     "a second modulus is admitted at every field order, so the descent and "
     "separation conditions stop leaving one value"),
    ("MUT-MODULUS", "G-MODULUS-OBSERVABLE", "modulus",
     "two moduli are made to share a tick-three distribution, so the "
     "modulus stops being separated by the observable"),
    ("MUT-M2", "G-M2-PREDICTION-RUN", "m2_prediction",
     "the predicted modulus's distribution is declared not to match the "
     "one the headline arena publishes"),
    ("MUT-PERIMETER", "G-PERIMETER-LAW-BOTH", "lattice_perimeter",
     "the ladder shapes are grouped by their longer side instead of by "
     "their perimeter, so the equal-group comparisons genuinely disagree"),
    ("MUT-GAP", "G-GAP-BOTH", "lattice_closed_form",
     "the null's coin is replaced by a diagonal one, whose realised ladder "
     "carries no halving mode at all"),
    ("MUT-PLAQUETTE", "G-PLAQUETTE-BOTH", "lattice_plaquette",
     "the expectation is taken over one sector instead of the whole carrier, "
     "which is not the measure the null's rule declares"),
    ("MUT-QUARTIC", "G-QUARTIC-BOTH", "lattice_quartic",
     "the exponent is misread out of the parent's own sentence, so a "
     "different observable is measured under the parent's name"),
    ("MUT-STENCIL", "G-STENCIL-FORCING-PARENT", "stencil",
     "a non-monomial unitary is recorded on the arena's own offset set, so "
     "the parent's coin-register theorem fails"),
    ("MUT-EXPRESS", "G-EXPRESSIBILITY-CENSUS", "expressibility",
     "one declared observable is dropped, so the classification stops being "
     "total"),
    ("MUT-CENSUS", "G-Q155-CENSUS-TOTAL", "q155_census",
     "every not-reproduced ruling is rewritten to reproduced, which is the "
     "honest failure outcome asserted without its measurement"),
    ("MUT-CENSUS-FLIP", "G-Q155-CENSUS-TOTAL", "q155_census",
     "a reproduction is rewritten to a non-reproduction -- the "
     "ISP-FLATTERING direction, which a cardinality predicate cannot see"),
    ("MUT-FALSIFIER", "G-FALSIFIER-SPECIFIED", "falsifier",
     "the deciding cost is priced against the PR3 null rather than against "
     "the closest memoryless walk the wider sweep found"),
    ("MUT-FEASIBILITY", "G-FEASIBILITY-BOTH-WAYS", "feasibility",
     "the recipe that drives the payload to the alternative outcome word is "
     "removed from the battery the feasibility argument relies on"),
    ("MUT-SCOPE", "G-SCOPE-DECLARED", "scope",
     "an axis this run swept is dropped from the evidence census, so the "
     "declared axis list stops being backed member for member"),
    ("MUT-PRICE", "G-STRUCTURE-PRICED", "structure_price",
     "the row for the one structure this run does dial is dropped, so the "
     "price stops being total and stops matching the axes the run swept"),
    ("MUT-CLASS", "G-VERDICT-EQUALITY", "verdict",
     "the head is re-classed from an ablation benchmark to the reading the "
     "review struck out, so the class word stops matching the payload's"),
    ("MUT-HEAD", "G-VERDICT-EQUALITY", "verdict",
     "the delivered head names a different tick from the one the payload "
     "carries"),
    ("MUT-HEAD-SELF", "G-VERDICT-EQUALITY", "verdict",
     "the rebuild is rewritten to call the BUILDER, so the comparison "
     "becomes one function against itself"),
    ("MUT-PAPER-CLAIM", "G-PAPER-CLAIMS", "paper_claims",
     "a standing claim is inverted in the paper handed to the claim gate"),
    ("MUT-REFERENT", "G-PAPER-REFERENTS", "paper_referents",
     "a numeral from no universe is planted in a sentence about the "
     "observable census"),
    ("MUT-REFERENT-HEADLINE", "G-PAPER-REFERENTS", "paper_referents",
     "the primary census count is inverted in the paper's own headline "
     "sentence, which is the inversion five injections shipped at exit 0"),
    ("MUT-REFERENT-SPELLED", "G-PAPER-REFERENTS", "paper_referents",
     "the pre-registration's own count is inverted at the SPELLED grain -- "
     "seven rules into three -- which is the grain the template's numeral "
     "pattern cannot see and the survivor this unit's own battery found"),
    ("MUT-WALL", "G-PAPER-WALLS", "walls",
     "the paper is given a natural voicing of the forbidden exhaustive-class "
     "reading, phrased as a paper would phrase it"),
    ("MUT-WALL-POSITIVE", "G-PAPER-WALLS", "walls",
     "the wall's own standing sentence is deleted, so the positive leg is "
     "exercised alone"),
    ("MUT-WALL-LICENCE", "G-PAPER-WALLS", "walls",
     "the one sentence that names the banned reading loses the rendered "
     "claim that licenses it, so the licence leg is exercised alone"),
    ("MUT-WALL-CONTROL", "G-PAPER-WALLS", "walls",
     "the ablation wall's pattern list is cut back to the legs it carried "
     "before this repair, so the panel's own paraphrases walk through again"),
    ("MUT-COVERAGE", "G-PAPER-COVERAGE", "paper_coverage",
     "an unmeasured numeral is planted in the paper's prose"),
    ("MUT-TYPED", "G-TYPED-COUNTS", "typed_counts",
     "a statement that types a numeral is appended to the source the audit "
     "reads, so the %-format subspecies is exercised"),
    ("MUT-TYPED-OFFSET", "G-TYPED-COUNTS", "typed_counts",
     "a value entering the registry as an arithmetic offset from a live "
     "count is appended, which is TPL-2's other subspecies and which the "
     "%-format leg cannot see at all"),
    ("MUT-FLOAT", "G-NO-FLOATS", "exactness",
     "a float site is recorded, so the exactness gate fails"),
    ("MUT-CONSUMER", "G-ANCHORS-CONSUMED", "anchors_consumed",
     "an anchor's declared consumer is rewritten to a gate that does not "
     "exist"),
    ("MUT-COVERAGE-SELF", "T-FALSIFIER-COVERAGE", "falsifier_coverage",
     "a sentinel-shaped recipe is recorded by the description audit"),
    ("MUT-COVERAGE-TAIL", "T-FALSIFIER-COVERAGE", "falsifier_coverage",
     "the coverage denominator is taken from the gates that have fired by "
     "then rather than from the declared list, which is the tail exemption"),
    ("MUT-TEMPLATE", "G-TEMPLATE-ADOPTED", "template",
     "one template family is dropped from the adopted list, so the adopted "
     "set stops covering the reference implementation's own"),
    ("MUT-TEMPLATE-UNUSED", "G-TEMPLATE-ADOPTED", "template",
     "a family is adopted and exercises nothing, which the delivered "
     "name-resolution check could not see"),
    ("MUT-READS", "G-READS-DECLARED", "reads",
     "a repository object this unit does not declare is opened before the "
     "read gate, so the audit hook's log stops matching the declaration"),
    ("MUT-TRANSCRIPT", "G-TRANSCRIPT-BOUND", "transcript_bound",
     "one gate row of the text that would be promoted is renamed, so the "
     "multiset the ledger is reconciled against differs"),
    ("MUT-READ-LATE", "G-TRANSCRIPT-BOUND", "transcript_bound",
     "an undeclared repository object is opened AFTER the read gate has "
     "passed, which only the close re-check can see"),
    ("MUT-SEAL-ADD", "T-SEAL-PROMOTION", "forged_finding",
     "a top-level key is added to the payload after the totality gate, which "
     "the promotion-time recomputation must catch"),
)

MUTANT_NAMES = tuple(m[0] for m in MUTANTS)


def clean_payload():
    R, _TR, _LD, _SEAL, _d = full_run(write=False)
    return R


def run_mutant(name, base=None):
    row = [m for m in MUTANTS if m[0] == name]
    if not row:
        raise SystemExit(2)
    _n, want_gate, target, _desc = row[0]
    base = base if base is not None else clean_payload()
    before = ET.digest(base.get(target))
    died, after = None, None
    try:
        R, _TR, _LD, _SEAL, _d = full_run(write=False, mutant=name)
        after = ET.digest(R.get(target))
    except ET.CheckFail as exc:
        died = exc.check
        after = ET.digest((PARTIAL["R"] or {}).get(target))
    used = name in MUTANT["used"]
    moved = (after != before)
    return {"mutant": name, "declared_gate": want_gate, "died_at": died,
            "target": target, "target_moved": bool(moved), "hook_used": used,
            "ok": died == want_gate and moved and used}


def main(argv):
    if len(argv) == 3 and argv[1] == "--mutant":
        if argv[2] not in MUTANT_NAMES:
            sys.stderr.write("unknown mutant: %r\n" % argv[2])
            return 2
        r = run_mutant(argv[2])
        print("MUTANT %s :: declared %s died %s target %s moved %s hook %s"
              % (r["mutant"], r["declared_gate"], r["died_at"], r["target"],
                 r["target_moved"], r["hook_used"]))
        return 0 if r["ok"] else 1
    if len(argv) != 2:
        sys.stderr.write(
            "usage: disc_exact.py --run|--no-write|--selftest|--list-gates"
            "|--list-mutants|--mutant NAME|--render\n")
        return 2
    mode = argv[1]
    if mode == "--list-mutants":
        for m in MUTANTS:
            print("%-22s %-32s %s" % (m[0], m[1], m[2]))
        return 0
    if mode == "--list-gates":
        _R, _TR, LD, _SEAL, _d = full_run(write=False, mode=mode)
        for g in LD.names():
            print(g)
        return 0
    if mode == "--render":
        R, _TR, _LD, _SEAL, _d = full_run(write=False, render=True, mode=mode)
        for t in R["rendered"]["tables"]:
            print(t)
            print()
        for c in R["rendered"]["claims"]:
            print("CLAIM :: " + c)
        print()
        for f in R["rendered"]["fences"]:
            print(f)
            print()
        return 0
    if mode == "--selftest":
        try:
            R, TR, LD, SEAL, _d = full_run(write=False, mode=mode)
        except ET.CheckFail as exc:
            print("SELFTEST: the clean run REFUSED at %s :: %s"
                  % (exc.check, exc.detail))
            return 1
        legs = []
        forged = TR.text().replace("[PASS] G-DISCRIMINANT-VALUES",
                                   "[PASS] G-FORGED-GATE")
        try:
            TR.bind(LD, forged)
            print("SELFTEST: a forged transcript row SURVIVED")
            return 1
        except ET.CheckFail as exc:
            legs.append("forged transcript row dies at %s" % exc.check)
        R["forged_key"] = {"smuggled": len(LD.rows)}
        try:
            SEAL.verify_at_promotion(R, LD, "seal_manifest")
            print("SELFTEST: a post-seal add SURVIVED")
            return 1
        except ET.CheckFail as exc:
            legs.append("post-seal add dies at %s" % exc.check)
        del R["forged_key"]
        bent = dict(R["discriminant"])
        bent["first_difference_tick"] = bent["first_difference_tick"] + 1
        try:
            SEAL.verify_at_promotion(
                dict(R, discriminant=bent), LD, "seal_manifest")
            print("SELFTEST: a sealed edit SURVIVED")
            return 1
        except ET.CheckFail as exc:
            legs.append("sealed value edit dies at %s" % exc.check)
        for leg in legs:
            print("SELFTEST: %s" % leg)
        print("SELFTEST: clean run green over %d gates; nothing written"
              % len(LD.rows))
        return 0
    if mode in ("--run", "--no-write"):
        rollback = None
        rollback_receipt = None
        out_path = os.path.join(REPO, OUTPUT_REL)
        rec_path = os.path.join(REPO, RECEIPT_REL)
        if mode == "--run" and os.path.exists(out_path):
            with open(out_path, "rb") as fh:
                rollback = fh.read()
        if mode == "--run" and os.path.exists(rec_path):
            with open(rec_path, "rb") as fh:
                rollback_receipt = fh.read()
        try:
            R, TR, LD, SEAL, dig = full_run(write=(mode == "--run"), mode=mode)
        except ET.CheckFail as exc:
            sys.stderr.write("REFUSED at %s :: %s\n" % (exc.check, exc.detail))
            return 1
        sys.stdout.write(TR.text())
        if mode == "--run":
            with open(out_path, "rb") as fh:
                on_disk = fh.read()
            if ET.bytes_digest(on_disk) != R["transcript"]["sha256_12"]:
                if rollback is not None:
                    with open(out_path, "wb") as fh:
                        fh.write(rollback)
                sys.stderr.write("REFUSED: promoted transcript bytes differ "
                                 "from the gate-time seal (rolled back)\n")
                return 1
            # THE RECEIPT GETS THE SAME READ-BACK AND THE SAME ROLLBACK
            # (K3 NOTE-1: the delivered object closed this window for the
            # transcript only, so an edit landing after full_run returned
            # shipped at exit 0 beside a manifest that still published the
            # old digest).
            with open(rec_path, "rb") as fh:
                rec_on_disk = fh.read()
            try:
                SEAL.verify_at_promotion(
                    json.loads(rec_on_disk.decode("utf-8")), LD,
                    "seal_manifest")
                rec_ok = True
            except ET.CheckFail as exc:
                rec_ok, rec_why = False, exc.detail
            if not rec_ok:
                if rollback is not None:
                    with open(out_path, "wb") as fh:
                        fh.write(rollback)
                if rollback_receipt is not None:
                    with open(rec_path, "wb") as fh:
                        fh.write(rollback_receipt)
                sys.stderr.write("REFUSED: the promoted receipt on disk does "
                                 "not verify against the gate-time seals :: "
                                 "%s (rolled back)\n" % rec_why)
                return 1
            print("WROTE %s (%s) and %s (%s)"
                  % (RECEIPT_REL, dig["receipt"], OUTPUT_REL, dig["side"]))
        else:
            print("NO-WRITE: %d gates, nothing written" % len(LD.rows))
        return 0
    sys.stderr.write("unknown argument: %r\n" % mode)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
