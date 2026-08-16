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

S-1 BY CONSTRUCTION (TEMPLATE.md Sec.11, the registered-unimplemented family).
Three code regions, disjoint by machine check at G-S1-DISJOINT-CODE:
  n_*   THE NULL         -- a plain coined walk; no record object of any kind
                            appears in its region, by AST;
  i_*   THE ISP MODEL    -- paper-20's coupled walk, rebuilt from its own
                            definitions, never imported;
  k_*   THE COMPARATOR   -- decides agreement and difference; calls neither
                            builder, and re-derives the head from the payload.
The two builders are cross-validated against each other where they must agree
(ticks 1 and 2, at every fiber point) and against paper-20's sealed numbers
where the ISP arm must reproduce a parent.

EXACTNESS.  Integers and fractions.Fraction only.  Cyclotomic amplitudes are
carried as integer 4-tuples over the basis (1, z, z^2, z^3) of Z[zeta_12]
reduced modulo z^4 - z^2 + 1.  No float appears anywhere and an AST scan plus
a recursive receipt type scan are gates.

TEMPLATE.  E-25...E-33 adopted; the nine families are imported from
v14/code/era_template.py and used, not copied.  TPL-2's registered items:
gate-time seals recomputed at promotion, no %-format or integer-offset typed
counts, wall controls written independently of their patterns, move-proofs
real, no carried-and-unused family.

CLI (#82).  --run | --no-write | --selftest | --list-gates | --list-mutants
            | --mutant NAME | --render
Anything else exits 2.
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
# the null does not, together with the count of adjustable numbers it
# introduces -- which is zero at every row, and is exactly why the comparison
# is an ablation rather than a fit.
STRUCTURE_PRICE = (
    ("the count field", "one non-negative integer per cell, initialised "
     "uniform and monotone thereafter", 0),
    ("the feedback rule", "the coin at a site is multiplied by the diagonal "
     "of phases the site's own counts determine", 0),
    ("the emission rule", "one division event per step, on a cell drawn with "
     "that cell's own post-coin weight", 0),
    ("the branch structure", "the state is an ensemble over emission "
     "histories rather than a single trajectory", 0),
    ("the phase character", "the map from a count to a phase, taken to be a "
     "character of the arena's own scalar group", 0),
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

    def __init__(self, q):
        self.q = q
        self.sites = [(a, b) for a in range(q) for b in range(q)]
        self.index = {x: i for i, x in enumerate(self.sites)}
        self.ns = len(self.sites)
        self.ncell = 3 * self.ns
        self.dim = 3 * self.ns
        self.shift = [0] * self.dim
        for s, x in enumerate(self.sites):
            for l, v in enumerate(LINKDIRS):
                y = ((x[0] + v[0]) % q, (x[1] + v[1]) % q)
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

def i_coin_apply(arena, psi, record, modulus, coin):
    out = [R0] * arena.dim
    for s in range(arena.ns):
        b = s * 3
        if modulus == 1:
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
            out[b + i] = tot
    return out


def i_walk_step(arena, psi, record, modulus, coin):
    post = i_coin_apply(arena, psi, record, modulus, coin)
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
             reading="A", coupled=True, record0=None, want_frontier=False):
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
            newpsi, post = i_walk_step(arena, list(psi), rec, modulus, coin)
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
            s2 = arena.index[((x[0] + LINKDIRS[0][0]) % arena.q,
                              (x[1] + LINKDIRS[0][1]) % arena.q)]
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
    """
    rows = []
    for q in qs:
        good = []
        for m in ms:
            descends = all((n % m) == ((n % q) % m) for n in range(4 * q))
            separates = len({n % m for n in range(q)}) == q
            if descends and (separates or not require_separation):
                good.append(m)
        rows.append((q, tuple(good)))
    return rows


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


def k_rebuild_head(payload):
    """THE COMPARATOR'S OWN ROUTE TO THE HEAD.  It reads the receipt payload
    and nothing else, uses its own segment order and its own separators, and
    knows nothing about how the builder rendered anything."""
    d = payload["discriminant"]
    nul = payload["null_model"]
    cen = payload["q155_census"]
    mod = payload["modulus"]
    per = payload["lattice_perimeter"]
    cfm = payload["lattice_closed_form"]
    plq = payload["lattice_plaquette"]
    qrt = payload["lattice_quartic"]
    pri = payload["structure_price"]
    seg = []
    seg.append(d["verdict_word"])
    seg.append("CLASS=%s;NULL=%s;RULES=%d;SHARED-WITH-ISP=%s;ABLATED=%s"
               % (payload["scope"]["class_word"], nul["word"], nul["rules"],
                  nul["shared"], nul["dropped"]))
    seg.append("PRIMARY=THE-RECORD-FREE-NULL-REPRODUCES-%d-OF-%d-TESTED-"
               "RESULTS;%d-NOT-REPRODUCED;%d-NOT-EXPRESSIBLE;REPRODUCED="
               "PERIMETER-LAW+CLOSED-FORM+GAP+PLAQUETTE+QUARTIC-SIGN+"
               "COIN-REGISTER-RESTRICTION+THE-FIRST-TWO-TICKS"
               % (cen["reproduced"], cen["rows_count"],
                  cen["not_reproduced"], cen["not_expressible"]))
    seg.append("LATTICE=PERIMETER-%s;CLOSED-FORM-%s;GAP-%s;PLAQUETTE-%s;"
               "QUARTIC-%s"
               % (per["word"], cfm["word_closed"], cfm["word_gap"],
                  plq["word"], qrt["word"]))
    seg.append("AGREEMENT=%d-OF-%d-SITE-BY-TICK-CHECKS-EQUAL-THROUGH-TICK-%d"
               % (d["agree_checks"] - d["agree_violations"],
                  d["agree_checks"], d["agree_upto"]))
    seg.append("ABLATION-EFFECT=FIRST-AT-TICK-%d-AT-%d-OF-%d-NON-TRIVIAL-"
               "FIBER-POINTS;NEVER-AT-%d-TRIVIAL-COIN-POINTS"
               % (d["first_difference_tick"], d["nontrivial_at_tick"],
                  d["nontrivial_points"], d["trivial_points"]))
    seg.append("VALUES-AT-AG-2-3=ISP-%s-VS-NULL-%s;TV=%s"
               % (d["q3"]["isp_ipr"], d["q3"]["null_ipr"], d["q3"]["tv"]))
    seg.append("VALUES-AT-AG-2-2=ISP-%s-VS-NULL-%s;TV=%s"
               % (d["q2"]["isp_ipr"], d["q2"]["null_ipr"], d["q2"]["tv"]))
    seg.append("M-EQUALS-Q=%s;INTERNAL-CHECK-CLOSING-THE-PARENTS-REGISTERED-"
               "TEST-NOT-AN-EXTERNAL-PREDICTION;CONSTRUCTION-DEPENDENT;"
               "OBSERVABLE-AT-%d-OF-%d-DECLARED-MODULI"
               % (mod["word"], mod["distinct_values"], mod["moduli_run"]))
    seg.append("PRICE=ISP-CARRIES-%d-STRUCTURES-THE-NULL-DOES-NOT-AND-%d-"
               "ADJUSTABLE-NUMBERS;PARAMETER-FREE-IS-NOT-STRUCTURE-FREE"
               % (pri["structures"], pri["adjustable_numbers"]))
    seg.append("FALSIFIER=%s;SHOTS=%d-AT-AG-2-3-AND-%d-AT-AG-2-2"
               % (payload["falsifier"]["word"],
                  payload["falsifier"]["shots_q3"],
                  payload["falsifier"]["shots_q2"]))
    seg.append("SUCCESSOR=%s" % payload["scope"]["successor_word"])
    seg.append("SCOPE=%s" % payload["scope"]["word"])
    return " -- ".join(seg)


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

# The walls are written from the FINDING, in the voices a paper would use, and
# each control below was written before the pattern it exercises (TPL-2: wall
# controls written independently).
_BE = r"(?:is|was|are|were|has been|have been|can be|could be|remains?)"

WALL_EXHAUSTIVE = ET.SemanticWall(
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
        r"the null is one model and not a class",
        r"no operational mapping to laboratory units exists in this corpus",
    ],
)

WALL_PARAMFREE = ET.SemanticWall(
    "W-PARAMETER-FREE-IS-RELATIVE",
    negative=[
        r"(?:isp|the theory|the model) has no (?:free )?(?:parameters?|"
        r"declarations?|choices?)(?![\w\s]{0,30}(?:the null|beyond))",
        r"(?:nothing|no datum|no quantity) %s declared" % _BE,
        r"(?:the|this) prediction %s (?:wholly |entirely |completely )?"
        r"(?:free of|without) (?:any )?declarations?" % _BE,
        r"(?:derived|forced) from first principles alone",
    ],
    positive=[
        r"the prediction is free of every parameter the null does not also "
        r"carry",
    ],
)

WALL_ABLATION = ET.SemanticWall(
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
    ],
    positive=[
        r"this unit is a model-ablation benchmark",
        r"the null compared here is memoryless",
        r"parameter-free is not structure-free",
    ],
)

WALLS = (WALL_EXHAUSTIVE, WALL_PARAMFREE, WALL_ABLATION)

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
    tree = ast.parse(source_text)
    region = {}
    calls = collections.defaultdict(set)
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            pre = node.name.split("_")[0]
            if pre in ("n", "i", "k"):
                region[node.name] = pre
            for sub in ast.walk(node):
                if isinstance(sub, ast.Call):
                    nm = (getattr(sub.func, "id", None)
                          or getattr(sub.func, "attr", None))
                    if nm:
                        calls[node.name].add(nm)
    s1_offences = []
    for fn, pre in sorted(region.items()):
        for callee in sorted(calls[fn]):
            cpre = region.get(callee)
            if cpre is None:
                continue
            if pre == "k" and cpre in ("n", "i"):
                s1_offences.append("%s (comparator) calls %s" % (fn, callee))
            if pre == "n" and cpre == "i":
                s1_offences.append("%s (null) calls %s" % (fn, callee))
    if mut("MUT-S1"):
        # a REAL misclassification: the ISP builder is entered in the region
        # map as a comparator, so the live call-graph predicate runs again
        # over the source as it stands and finds the edges it forbids
        region["i_ladder"] = "k"
        s1_offences = []
        for fn, pre in sorted(region.items()):
            for callee in sorted(calls[fn]):
                cpre = region.get(callee)
                if cpre is None:
                    continue
                if pre == "k" and cpre in ("n", "i"):
                    s1_offences.append("%s (comparator) calls %s"
                                       % (fn, callee))
                if pre == "n" and cpre == "i":
                    s1_offences.append("%s (null) calls %s" % (fn, callee))
    REG.measured("null_fns", sum(1 for v in region.values() if v == "n"),
                 "AST count of functions in the n_ region")
    REG.measured("isp_fns", sum(1 for v in region.values() if v == "i"),
                 "AST count of functions in the i_ region")
    REG.measured("cmp_fns", sum(1 for v in region.values() if v == "k"),
                 "AST count of functions in the k_ region")
    R["s1_regions"] = {"null": REG.values["null_fns"],
                       "isp": REG.values["isp_fns"],
                       "comparator": REG.values["cmp_fns"],
                       "offences": s1_offences}
    SEAL.seal("s1_regions", R["s1_regions"], "G-S1-DISJOINT-CODE")
    gate("G-S1-DISJOINT-CODE",
         REG.stmt("the null's {null_fns} functions, the ISP model's "
                  "{isp_fns} and the comparator's {cmp_fns} are disjoint "
                  "regions of this source: the comparator calls neither "
                  "builder and the null calls nothing of the ISP model's, "
                  "by an abstract-syntax-tree walk of the call graph",
                  null_fns=1, isp_fns=1, cmp_fns=1),
         not s1_offences, "regions %d/%d/%d offences %s"
         % (REG.values["null_fns"], REG.values["isp_fns"],
            REG.values["cmp_fns"], s1_offences or "none"))

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
    shared = ["ARENA", "REGISTER", "COIN", "SHIFT", "STATE", "HORIZON"]
    if mut("MUT-NULL-RULE"):
        rule_ids = rule_ids[:-1]
    REG.measured("null_rules", len(rule_ids), "len(NULL_RULE)")
    REG.measured("null_shared", len(shared), "len(shared)")
    REG.measured("null_dropped", len(dropped),
                 "the structures the pin's own sentence names as absent")
    R["null_model"] = {
        "word": "PLAIN-COINED-WALK",
        "rules": len(rule_ids), "rule_ids": list(rule_ids),
        "rule_text": {r[0]: r[2] for r in NULL_RULE},
        "shared": "-".join(shared), "dropped": "-".join(dropped),
        "pin_sentence_terms_missing": missing,
        "dimension_read_from_the_pin": pin_dimension,
        "shared_count": len(shared), "dropped_count": len(dropped)}
    SEAL.seal("null_model", R["null_model"], "G-NULL-RULE-TOTAL")
    gate("G-NULL-RULE-TOTAL",
         REG.stmt("the null's parameters are fixed by {null_rules} rules "
                  "declared before any row runs; {null_shared} of its data "
                  "are the ISP model's own and {null_dropped} structures are "
                  "dropped, and the two dropped structures are exactly the "
                  "ones the pin's own sentence names",
                  null_rules=1, null_shared=1, null_dropped=1),
         len(rule_ids) == len(NULL_RULE) and not missing
         and len(dropped) == len(("record", "price"))
         and pin_dimension == DECLARED_DIMENSION,
         "rules %d shared %d dropped %s missing %s pin-dimension %s"
         % (len(rule_ids), len(shared), dropped, missing or "none",
            pin_dimension))

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

    # the canonical coin: the non-trivial class of least index at each arena
    canonical = {}
    for q in ARENAS:
        nt = [r for r in censuses[q][1] if not coin_is_trivial(r[1])]
        canonical[q] = coin_matrix(*nt[0]) if q == 2 else coin_matrix(
            rscale(R1, -3), rscale(R1, 2))
    # at both arenas the canonical coin is +-Grover, written 3C = -I + 2J
    GROVER = coin_matrix(rscale(R1, -3), rscale(R1, 2))
    GROVER_INT = ((-1, 2, 2), (2, -1, 2), (2, 2, -1))
    for q in ARENAS:
        canonical[q] = GROVER

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
    # the anchor's CONTENT enters the predicate: the parent's sentence says
    # the control runs on counts that never update, and the control's own
    # record is measured to have stayed at its initial value everywhere while
    # the coupled arm's has not
    frozen_rec = i_record_observables(
        arenas[3], i_ladder(A3, FIB_T, 3, GROVER, (0, 0), 0, "A",
                            coupled=False, want_frontier=True)["frontier"], 3)
    coupled_rec = i_record_observables(
        arenas[3], i_ladder(A3, FIB_T, 3, GROVER, (0, 0), 0, "A",
                            coupled=True, want_frontier=True)["frontier"], 3)
    never_updates = ("counts that never update" in ET.canon(a_frozen)
                     and frozen_rec["max_cell_count"] == 1
                     and coupled_rec["max_cell_count"] > 1)
    fid_ok = (got_c == parent_coupled and got_f == parent_frozen
              and fid_c["ipr"][FID_T] == parent_ipr_c
              and fid_f["ipr"][FID_T] == parent_ipr_f
              and never_updates)
    REG.measured("fid_leaves", got_c[-1], "the coupled arm's leaf count")
    REG.measured("fid_leaves_frozen", got_f[-1], "the frozen arm's leaf count")
    REG.measured("fid_matched", 4,
                 "the parent quantities this rebuild reproduces: two branch "
                 "ladders and two horizon inverse-participation ratios")
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
        "coupled_max_cell_count": coupled_rec["max_cell_count"]}
    SEAL.seal("isp_fidelity", R["isp_fidelity"], "G-ISP-FIDELITY-PARENT")
    gate("G-ISP-FIDELITY-PARENT",
         REG.stmt("this unit's independent rebuild of the coupled walk "
                  "reproduces {fid_matched} of the parent's sealed "
                  "quantities exactly -- both branch ladders and both "
                  "horizon inverse-participation ratios, the coupled arm "
                  "landing on {fid_leaves} leaves against the control's "
                  "{fid_leaves_frozen}", fid_matched=1, fid_leaves=1,
                  fid_leaves_frozen=1),
         fid_ok, "coupled %s frozen %s ipr %s / %s control-max-count %d"
         % (got_c, got_f, fid_c["ipr"][FID_T], fid_f["ipr"][FID_T],
            frozen_rec["max_cell_count"]))

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
    R["null_two_routes"] = dict(two_route)
    SEAL.seal("null_two_routes", R["null_two_routes"], "G-NULL-TWO-ROUTES")
    gate("G-NULL-TWO-ROUTES",
         REG.stmt("the null's cyclotomic route and its integer route agree "
                  "at {route_checks} site-by-tick comparisons; the two share "
                  "the declared arena and no arithmetic whatever",
                  route_checks=1),
         two_route["violations"] == 0,
         "checks %d violations %d" % (two_route["checks"],
                                      two_route["violations"]))

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
                        isp = i_ladder(A, sweep_horizon, q, C, start,
                                       direction, reading)
                        nul = n_ladder_ring(A, sweep_horizon, C, start,
                                            direction)
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
        "verdict_word": ("RECORD-BACKREACTION-DETECTED-AT-TICK-%d"
                         % first_tick) if disc_found
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

    # -- the modulus leg: NDEP's untested prediction, RUN --------------------
    a_conn = ASET.read("A-COUP-CONNECTION", "G-MODULUS-DESCENT-THEOREM")
    # a REAL weakening: the separation condition is dropped, so the sweep
    # runs again and admits every modulus that merely descends
    desc = i_modulus_descent(PRIME_ORDERS, MODULUS_WINDOW,
                             require_separation=not mut("MUT-DESCENT"))
    desc_ok = all(g == (q,) for (q, g) in desc)
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
        "parent_sentence_located": bool(conn_ok)}
    SEAL.seal("modulus_descent", R["modulus_descent"],
              "G-MODULUS-DESCENT-THEOREM")
    gate("G-MODULUS-DESCENT-THEOREM",
         REG.stmt("the parent derives the connection from the arena's own "
                  "scalar group; over {descent_arenas} field orders and "
                  "{descent_moduli} moduli the phase map descends to that "
                  "group and separates its elements at exactly one modulus, "
                  "the field order itself, so the parent's derivation read at "
                  "the smaller arena is a determinate prediction and not a "
                  "convention", descent_arenas=1, descent_moduli=1),
         desc_ok and conn_ok, "rows %s parent-sentence %s"
         % ([(q, list(g)) for (q, g) in desc], conn_ok))

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
            # instead of by their perimeter, so the equal-group comparisons
            # genuinely disagree
            key = max(a, b) if mut("MUT-PERIMETER") else a + b
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
        "null_coin_in_family": bool(had_in),
        "null_coin_sector": i_sector(HAD),
        "word": "REPRODUCED-BY-THE-NULL" if (per_bad == 0 and had_in)
        else "NOT-REPRODUCED"}
    SEAL.seal("lattice_perimeter", R["lattice_perimeter"],
              "G-PERIMETER-LAW-BOTH")
    gate("G-PERIMETER-LAW-BOTH",
         REG.stmt("the parent's perimeter-only law is a per-configuration "
                  "statement about a uniform configuration: over "
                  "{perimeter_comparisons} equal-perimeter comparisons at "
                  "every one of the {link_coins} coins of the shared family "
                  "the loop observable is constant, and the null's own coin "
                  "is one of those coins, so the law is the null's too",
                  perimeter_comparisons=1, link_coins=1),
         per_bad == 0 and had_in and "takes the same value" in ET.canon(a_per),
         "comparisons %d disagreements %d null-coin-in-family %s"
         % (per_comps, per_bad, had_in))
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
                  "{link_coins} coins -- the null's own coin among them, its "
                  "coefficients measured here", halving_coins=1,
                  link_coins=1),
         cf_fail == 0 and had_halving and ratio_ok,
         "closed-form failures %d halving %d of %d null-coin %s ratio %s"
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
                  "twists reverse it at every coin, and the null's counting "
                  "measure returns the parent's own single value",
                  quartic_zero_coins=1, quartic_plus=1, quartic_minus=1),
         q_exp == 0 and odd_full and qdist[2] == qdist[-2]
         and parent_power is not None
         and "single value zero" in ET.canon(a_q1),
         "distribution %s counting expectation %s odd-twists %s"
         % (dict(sorted(qdist.items())), q_exp, odd_full))

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
    EXPR_CLASSES = ("MEASURABLE", "DEFINITIONAL")
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
        "class_words": list(EXPR_CLASSES), "unruled": unruled}
    SEAL.seal("expressibility", R["expressibility"],
              "G-EXPRESSIBILITY-CENSUS")
    gate("G-EXPRESSIBILITY-CENSUS",
         REG.stmt("every one of {expr_rows} declared observables is classed "
                  "and the classes are total: {expr_both} are formable in "
                  "both models and {expr_only} are formable only where a "
                  "record exists, and a row of the second kind is a "
                  "definitional absence and never a discriminant",
                  expr_rows=1, expr_both=1, expr_only=1),
         both + only == len(EXPR) and both > 0 and only > 0
         and not unruled
         and all(w.casefold() in ET.canon(a_expr) for w in EXPR_CLASSES),
         "rows %d both %d isp-only %d unruled %s"
         % (len(EXPR), both, only, unruled or "none"))

    # -- Q155: the reproduction census --------------------------------------
    CENSUS = [
        ("paper-36 the rectangle ladder is a function of the perimeter alone",
         "REPRODUCED",
         "per-configuration at %d equal-perimeter comparisons, %d "
         "disagreements; the null's own coin is in the family"
         % (per_comps, per_bad)),
        ("paper-36 the three-term closed form at every coin", "REPRODUCED",
         "%d closed-form failures over %d coins" % (cf_fail, len(lcoins))),
        ("paper-36 the halving mode and its gap", "REPRODUCED",
         "present at %d of %d coins, the null's own among them with "
         "coefficients %s" % (halving, len(lcoins),
                              " ".join(str(x) for x in had_sol[0]))),
        ("paper-36 the plaquette counting expectation", "REPRODUCED",
         "%d distinct values, expectation %s, %d non-flat diagonal coins"
         % (p_distinct, p_exp_rat, nonflat)),
        ("paper-34 the off-diagonal quartic sign pinned to a single value",
         "REPRODUCED",
         "the null's counting measure returns %s; the odd twists reverse "
         "the observable at every coin" % q_exp),
        ("paper-20 the coin register is forced on this offset set",
         "REPRODUCED",
         "%d unitary and %d non-monomial over %d maps: arena-carried"
         % (link_scan["unitary"], link_scan["non_monomial"],
            len(ALPHA3) ** 3)),
        ("paper-20 the walk's distribution at the first two ticks",
         "REPRODUCED",
         "%d site-by-tick comparisons, %d violations, over all %d points "
         "of the sweep"
         % (agree_checks, agree_viol, nontrivial_pts + trivial_pts)),
        ("paper-20 the walk's distribution from the third tick on",
         "NOT-REPRODUCED",
         "unequal at both arenas; the first difference arrives at the same "
         "tick at %d of %d interfering points of the sweep"
         % (nontrivial_at3, nontrivial_pts)),
        ("paper-39 the connection modulus read at the smaller arena",
         "NOT-REPRODUCED",
         "the null is the modulus-one point of the family; the tick-three "
         "distribution takes %d distinct values over %d moduli"
         % (distinct, len(mdist))),
        ("paper-20 the record-side observable set", "NOT-EXPRESSIBLE",
         "%d of %d observables of the classification are formable only where "
         "a record exists" % (only, len(EXPR))),
    ]
    if mut("MUT-CENSUS"):
        CENSUS = [(a, "REPRODUCED", c) if b == "NOT-REPRODUCED" else (a, b, c)
                  for (a, b, c) in CENSUS]
    rep = sum(1 for r in CENSUS if r[1] == "REPRODUCED")
    nrep = sum(1 for r in CENSUS if r[1] == "NOT-REPRODUCED")
    nexp = sum(1 for r in CENSUS if r[1] == "NOT-EXPRESSIBLE")
    REG.measured("census_rows", len(CENSUS), "len(CENSUS)")
    REG.measured("census_reproduced", rep, "rows ruled reproduced")
    REG.measured("census_not_reproduced", nrep, "rows ruled not reproduced")
    REG.measured("census_not_expressible", nexp,
                 "rows the null cannot form at all")
    R["q155_census"] = {
        "rows": [{"result": a, "ruling": b, "evidence": c}
                 for (a, b, c) in CENSUS],
        "rows_count": len(CENSUS), "reproduced": rep,
        "not_reproduced": nrep, "not_expressible": nexp}
    SEAL.seal("q155_census", R["q155_census"], "G-Q155-CENSUS-TOTAL")
    gate("G-Q155-CENSUS-TOTAL",
         REG.stmt("every one of {census_rows} declared sealed results is "
                  "ruled by a measurement taken in this run: "
                  "{census_reproduced} are reproduced by the null and are "
                  "demotion candidates, {census_not_reproduced} are not, and "
                  "{census_not_expressible} cannot be formed by a model "
                  "without a record at all", census_rows=1,
                  census_reproduced=1, census_not_reproduced=1,
                  census_not_expressible=1),
         rep + nrep + nexp == len(CENSUS) and nrep > 0,
         "rows %d reproduced %d not %d not-expressible %d"
         % (len(CENSUS), rep, nrep, nexp))

    # -- the falsifier and the finite experiment ----------------------------
    shots3 = k_shots(head_vals[3]["_gap"], 100)
    shots2 = k_shots(head_vals[2]["_gap"], 100)
    ops3 = head_vals[3]["branches"]
    ops2 = head_vals[2]["branches"]
    if mut("MUT-FALSIFIER"):
        shots3 = shots3 + 1
    R["falsifier"] = {
        "word": "COMPUTATIONAL-REGRESSION-TEST-ON-A-PROPOSED-REALIZATION",
        "statement": "a proposed realization of this model is refuted at the "
                     "declared arena if the site-occupation distribution at "
                     "the third tick equals the record-free null's, or any "
                     "value other than the one published here; the test is a "
                     "regression test on a realization and not an empirical "
                     "test of nature, because this corpus supplies no "
                     "mapping from ticks and sites to laboratory units",
        "kind": "REGRESSION-TEST-NOT-EMPIRICAL",
        "max_gap_q3": head_vals[3]["max_gap"],
        "max_gap_q2": head_vals[2]["max_gap"],
        "shots_q3": shots3, "shots_q2": shots2,
        "confidence_denominator": 100,
        "simulation_branches_q3": ops3, "simulation_branches_q2": ops2,
        "operational_units": "ABSENT-IN-THIS-CORPUS"}
    SEAL.seal("falsifier", R["falsifier"], "G-FALSIFIER-SPECIFIED")
    REG.measured("shots_q3", shots3, "Chebyshev at the measured gap")
    REG.measured("shots_q2", shots2, "Chebyshev at the measured gap")
    REG.measured("sim_branches_q3", ops3, "the exhaustive emission tree")
    gate("G-FALSIFIER-SPECIFIED",
         REG.stmt("the falsifier is the discriminating observable itself and "
                  "the experiment is finite twice over: the exhaustive "
                  "simulation closes at {sim_branches_q3} branches, and a "
                  "repeated preparation separates the two values in "
                  "{shots_q3} shots at the larger arena and {shots_q2} at "
                  "the smaller, both by Chebyshev on the measured gap and "
                  "both in exact rational arithmetic", sim_branches_q3=1,
                  shots_q3=1, shots_q2=1),
         shots3 == k_shots(head_vals[3]["_gap"], 100)
         and shots2 == k_shots(head_vals[2]["_gap"], 100),
         "shots %d / %d branches %d / %d" % (shots3, shots2, ops3, ops2))

    # -- scope ---------------------------------------------------------------
    R["scope"] = {
        "word": "ONE-MEMORYLESS-NULL-NOT-A-CLASS;D=2;"
                "ARENAS=AG-2-2-AND-AG-2-3;READINGS=A-AND-B;"
                "AT-FINITE-HORIZON-A-RECORD-IS-ABSORBABLE-INTO-AN-ENLARGED-"
                "STATE;NO-OPERATIONAL-UNITS;NO-LABORATORY-CLAIM;"
                "NOT-AN-EXTERNAL-PREDICTION",
        "class_word": "MODEL-ABLATION-BENCHMARK",
        "successor_word": "DISC-2-THE-SIMPLEST-MEMORY-BEARING-NULL",
        "null_weakness": "the null compared here is MEMORYLESS: its coin is "
                         "constant in space and in time. At a finite horizon "
                         "a record is always absorbable into an enlarged "
                         "state description, so a memory-bearing null is not "
                         "excluded by anything measured here and is "
                         "registered as the successor opponent.",
        "successor": "DISC-2: the simplest memory-bearing null -- a "
                     "finite-memory coin, a state-dependent coin, a "
                     "dynamically updated phase field, or an enlarged "
                     "internal register -- named here and not attempted "
                     "here.",
        "arenas": list(ARENAS), "readings": ["A", "B"],
        "horizons": {"fiber": FIB_T, "fidelity": FID_T, "head": HEAD_T},
        "declared_free_axes": ["coin class", "start site", "coin direction",
                               "emission reading", "arena", "modulus"]}
    SEAL.seal("scope", R["scope"], "G-SCOPE-DECLARED")
    REG.measured("free_axes", len(R["scope"]["declared_free_axes"]),
                 "the declared free axes of the arena (RUNBOOK 15)")
    gate("G-SCOPE-DECLARED",
         REG.stmt("the declared arena is data: {free_axes} free axes are "
                  "named and the difference is gated across every one of "
                  "them that this unit sweeps, so the finding is stated at "
                  "its own scope and not beyond it", free_axes=1),
         len(R["scope"]["declared_free_axes"]) > 0
         and R["scope"]["class_word"] == "MODEL-ABLATION-BENCHMARK",
         "axes %s class %s"
         % (R["scope"]["declared_free_axes"], R["scope"]["class_word"]))

    # -- the structure price -------------------------------------------------
    price_rows = list(STRUCTURE_PRICE)
    if mut("MUT-PRICE"):
        # a REAL under-pricing: one structure the null does not carry is
        # dropped from the priced list, so the census stops being total
        price_rows = price_rows[:-1]
    adjustable = sum(n for (_a, _b, n) in price_rows)
    priced_names = {a for (a, _b, _n) in price_rows}
    price_missing = [a for (a, _b, _n) in STRUCTURE_PRICE
                     if a not in priced_names]
    REG.measured("priced_structures", len(price_rows), "len(price_rows)")
    REG.measured("adjustable_numbers", adjustable,
                 "the adjustable numbers the priced structures introduce")
    R["structure_price"] = {
        "structures": len(price_rows), "adjustable_numbers": adjustable,
        "rows": [{"structure": a, "what it is": b, "adjustable numbers": n}
                 for (a, b, n) in price_rows],
        "unpriced": price_missing,
        "reading": "parameter-free is not structure-free: the record-carrying "
                   "model carries these structures and the null does not, and "
                   "the comparison prices them here even though none of them "
                   "introduces an adjustable number"}
    SEAL.seal("structure_price", R["structure_price"], "G-STRUCTURE-PRICED")
    gate("G-STRUCTURE-PRICED",
         REG.stmt("the {priced_structures} structures this model carries and "
                  "the null does not are listed with what each one is, and "
                  "the adjustable numbers they introduce between them total "
                  "{adjustable_numbers}: parameter-free is not structure-free "
                  "and the difference is priced rather than left implicit",
                  priced_structures=1, adjustable_numbers=1),
         not price_missing and adjustable == 0,
         "structures %d adjustable %d unpriced %s"
         % (len(price_rows), adjustable, price_missing or "none"))

    # -- the verdict --------------------------------------------------------
    head = k_rebuild_head(R)
    if mut("MUT-HEAD"):
        head = head.replace("TICK-3", "TICK-4")
    if mut("MUT-CLASS"):
        head = head.replace("MODEL-ABLATION-BENCHMARK",
                            "FIRST-PARAMETER-FREE-PREDICTION")
    R["verdict"] = {"head": head}
    SEAL.seal("verdict", R["verdict"], "G-VERDICT-EQUALITY")
    rebuilt = k_rebuild_head(R)
    gate("G-VERDICT-EQUALITY",
         REG.stmt("the delivered head and an independent reconstruction over "
                  "the receipt payload are compared for string equality, so "
                  "a stale head cannot be delivered"),
         head == rebuilt, "head %d chars equal %s"
         % (len(head), head == rebuilt))

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
    T_CENSUS = CL.table("T-Q155", ("parent result", "ruling", "evidence"),
                        [(a, b, c) for (a, b, c) in CENSUS])
    T_PRICE = CL.table(
        "T-PRICE", ("structure", "what it is", "adjustable numbers"),
        [(a, b, n) for (a, b, n) in price_rows])
    T_FALS = CL.table(
        "T-FALSIFIER", ("arena", "largest site gap", "shots", "branches"),
        [("AG(2, 3)", head_vals[3]["max_gap"], shots3, ops3),
         ("AG(2, 2)", head_vals[2]["max_gap"], shots2, ops2)])
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
    C2 = CL.claim("the null is one model and not a class", 2)
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

    R["rendered"] = {
        "tables": [T_NULL, T_COIN, T_FID, T_FIBER, T_VALUES, T_DIST3, T_DIST2,
                   T_MOD, T_DESC, T_LAT, T_EXPR, T_CENSUS, T_PRICE, T_FALS,
                   T_STENCIL],
        "claims": [C1, C2, C3, C4, C5, C6, C7, C8, C9],
        "fences": [F1]}
    if render:
        RS.active = False
        return R, TR, LD, SEAL, None

    paper_r = paper
    if mut("MUT-PAPER-CLAIM"):
        paper_r = paper_r.replace("the null is one model and not a class",
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
    fiber_row_points = {d for (_a, _b, _c, d) in fiber_rows}
    RR.universe("the fiber",
                ["fiber point", "fiber points"],
                {nontrivial_pts + trivial_pts, nontrivial_pts, trivial_pts,
                 nontrivial_at3, trivial_never, agree_checks, agree_viol,
                 first_tick, agree_upto} | fiber_row_points | set(ARENAS),
                {(nontrivial_at3, nontrivial_pts),
                 (trivial_never, trivial_pts),
                 (agree_checks - agree_viol, agree_checks)})
    RR.universe("the coin family",
                ["coin of the carrier", "coins of the shared family",
                 "link coin", "link coins"],
                {len(lcoins), halving, p_distinct, nonflat, qdist[0],
                 qdist[2], qdist[-2], per_comps, per_bad, cf_fail,
                 len(alphabet), len(lrows), len(twist_rows)}
                | set(sectors.values()),
                {(halving, len(lcoins)), (per_bad, per_comps),
                 (cf_fail, len(lcoins)), (nonflat, len(lcoins))})
    RR.universe("the census",
                ["sealed result", "sealed results", "census row",
                 "census rows"],
                {len(CENSUS), rep, nrep, nexp},
                {(rep, len(CENSUS)), (nrep, len(CENSUS)),
                 (nexp, len(CENSUS))})
    RR.universe("the observable census",
                ["declared observable", "declared observables"],
                {len(EXPR), both, only},
                {(both, len(EXPR)), (only, len(EXPR))})
    RR.universe("the modulus sweep",
                ["declared modulus", "declared moduli"],
                set(MODULI) | {len(mdist), distinct, len(MODULI), first_tick},
                {(distinct, len(mdist))})
    RR.universe("the coin census",
                ["covariant coin", "covariant coins"],
                {len(censuses[3][0]), len(censuses[3][1]),
                 len(censuses[2][0]), len(censuses[2][1])} | set(ARENAS),
                {(len(censuses[3][1]), len(censuses[3][0])),
                 (len(censuses[2][1]), len(censuses[2][0]))})
    paper_rr = stripped
    if mut("MUT-REFERENT"):
        paper_rr = paper_rr.replace(
            "declared observables", "declared observables 4242", 1)
    try:
        rr = RR.gate(paper_rr)
        rprob = None
    except ET.CheckFail as exc:
        rr, rprob = {"occurrences_checked": 0}, exc.detail
    R["paper_referents"] = dict(rr, problem=rprob or "none",
                                exemptions_unused=exempt_missing,
                                section_ordinals_removed=section_ordinals,
                                universes=RR.seal_value())
    SEAL.seal("paper_referents", R["paper_referents"], "G-PAPER-REFERENTS")
    gate("G-PAPER-REFERENTS",
         REG.stmt("every numeral of every prose sentence whose subject noun "
                  "names a declared universe is resolved against that "
                  "universe alone, per occurrence and outside the fences, "
                  "with the declared identifier exemptions removed first and "
                  "every one of them required to occur"),
         rprob is None and not exempt_missing,
         "occurrences %d unused exemptions %s %s"
         % (rr["occurrences_checked"], exempt_missing or "none",
            rprob or "bound"))

    # -- walls --------------------------------------------------------------
    paper_w = paper
    if mut("MUT-WALL"):
        paper_w = paper_w + ("\n\nNo simpler model can reproduce this "
                             "difference, and it rules out every competing "
                             "account.\n")
    if mut("MUT-WALL-POSITIVE"):
        # every voicing of the wall's own standing sentence is removed, not
        # only the lower-case one: a sentence-initial capital left the leg
        # satisfied by the surviving copy and the recipe proved nothing
        paper_w = re.sub(r"[Tt]he null is one model and not a class", "",
                         paper_w)
    wprob = None
    for w in WALLS:
        try:
            w.scan(paper_w, R["rendered"]["claims"])
        except ET.CheckFail as exc:
            wprob = exc.detail
            break
    R["walls"] = {"walls": [w.seal_value() for w in WALLS],
                  "problem": wprob or "none"}
    SEAL.seal("walls", R["walls"], "G-PAPER-WALLS")
    REG.measured("wall_count", len(WALLS), "len(WALLS)")
    REG.measured("wall_patterns", sum(len(w.negative) + len(w.positive)
                                      for w in WALLS),
                 "negative plus positive legs")
    gate("G-PAPER-WALLS",
         REG.stmt("{wall_count} semantic walls with {wall_patterns} legs run "
                  "against the canonicalised paper: no banned reading in any "
                  "voice, and every standing sentence still carried, so "
                  "deleting a wall's own verdict fails it",
                  wall_count=1, wall_patterns=1),
         wprob is None, "walls %d legs %d %s"
         % (len(WALLS), REG.values["wall_patterns"], wprob or "clean"))

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
    typed = REG.audit_module(audit_source, ("stmt", "gate", "claim"))
    R["typed_counts"] = {"offenders": typed,
                         "measured_names": len(REG.values),
                         "exemptions": len(REG.exempt)}
    SEAL.seal("typed_counts", R["typed_counts"], "G-TYPED-COUNTS")
    REG.measured("measured_names", len(REG.values), "len(REG.values)")
    gate("G-TYPED-COUNTS",
         REG.stmt("an abstract-syntax-tree scan of this source finds no "
                  "string literal handed to a statement or claim builder "
                  "that types a numeral, and every published statement's "
                  "numerals arrive by name from the {measured_names} "
                  "measured values", measured_names=1),
         not typed, "measured %d offenders %s"
         % (len(REG.values), typed or "none"))

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

    # -- reads --------------------------------------------------------------
    rev = RS.gate_at_close(reads)
    R["reads"] = {"declared": sorted(set(reads)), "reads": rev["reads"],
                  "distinct": rev["distinct"]}
    SEAL.seal("reads", R["reads"], "G-READS-DECLARED")
    REG.measured("declared_reads", len(set(reads)), "len(set(reads))")
    gate("G-READS-DECLARED",
         REG.stmt("the repository reads this run actually performed, "
                  "recorded at the interpreter's own open hook rather than "
                  "in a helper, are exactly the {declared_reads} declared "
                  "paths, compared as a multiset at the last gate",
                  declared_reads=1),
         True, "reads %d distinct %d" % (rev["reads"], rev["distinct"]))

    # -- falsifier coverage --------------------------------------------------
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
    waivers = {
        "G-SCOPE-DECLARED": "a declaration census with no measured predicate "
                            "to corrupt; its content is the axis list, which "
                            "G-VERDICT-EQUALITY carries into the head",
        "G-READS-DECLARED": "enforced by the interpreter's audit hook, whose "
                            "own falsification is the raw-open leg of the "
                            "template's read-set demo",
    }
    forcings = {
        "G-SCOPE-DECLARED": len(R["scope"]["declared_free_axes"]) > 0,
        "G-READS-DECLARED": rev["reads"] > 0,
    }
    try:
        cov = HARNESS.coverage(LD, waivers, forcings)
        fprob = None
    except ET.CheckFail as exc:
        cov, fprob = {"gates": len(LD.rows), "falsified": 0,
                      "waived": len(waivers)}, exc.detail
    R["falsifier_coverage"] = dict(cov, sentinels=sentinels,
                                   problem=fprob or "none",
                                   waivers=sorted(waivers))
    SEAL.seal("falsifier_coverage", R["falsifier_coverage"],
              "T-FALSIFIER-COVERAGE")
    REG.measured("mutant_rows", len(MUTANTS), "len(MUTANTS)")
    gate("T-FALSIFIER-COVERAGE",
         REG.stmt("every gate that fired carries a falsifier or a waiver "
                  "with a machine-checked forcing, the {mutant_rows} "
                  "recipes each name the measured key they must move, and no "
                  "recipe is sentinel-shaped by an abstract-syntax-tree scan "
                  "of its own body", mutant_rows=1),
         fprob is None and not sentinels,
         "gates %d falsified %d waived %d sentinels %s"
         % (cov["gates"], cov["falsified"], cov["waived"],
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
    R["template"] = {"families_adopted": fam_checks,
                     "families_missing": fam_missing,
                     "families_resolved": len(fam_classes),
                     "engravings": "E-25 through E-33 with TPL-2's items"}
    SEAL.seal("template", R["template"], "G-TEMPLATE-ADOPTED")
    REG.measured("families", len(ET.FAMILIES), "len(ET.FAMILIES)")
    gate("G-TEMPLATE-ADOPTED",
         REG.stmt("all {families} template families are imported from the "
                  "reference implementation and used rather than copied, and "
                  "each one's check name appears in this run's own ledger or "
                  "in a gate this run fired", families=1),
         not fam_missing and len(fam_classes) == len(ET.FAMILIES),
         "families %d resolved %d missing %s"
         % (len(fam_checks), len(fam_classes), fam_missing or "none"))

    # -- close ---------------------------------------------------------------
    TR.bind(LD)
    gate("G-TRANSCRIPT-BOUND",
         REG.stmt("every gate row of the finished transcript is parsed back "
                  "out of the text that will be promoted and reconciled with "
                  "the ledger as a multiset, evidence strings included, in "
                  "both directions, and the ledger's own chain is recomputed "
                  "from the receipt's bytes"),
         True, "rows %d chain %s" % (len(LD.rows), LD.head[:12]))
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
     "the comparator's call-graph check is disabled and a comparator "
     "function that calls a builder is added to the region map"),
    ("MUT-NULL-RECORD", "G-NULL-HAS-NO-RECORD", "null_no_record",
     "a record-vocabulary leak is injected into the null's region report"),
    ("MUT-NULL-RULE", "G-NULL-RULE-TOTAL", "null_model",
     "one pre-registered rule is dropped, so the null's parameters stop "
     "being total"),
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
    ("MUT-FALSIFIER", "G-FALSIFIER-SPECIFIED", "falsifier",
     "the published shot count is moved off the value the measured gap "
     "forces"),
    ("MUT-PRICE", "G-STRUCTURE-PRICED", "structure_price",
     "one structure the record-carrying model carries and the null does not "
     "is dropped from the priced list, so the price stops being total"),
    ("MUT-CLASS", "G-VERDICT-EQUALITY", "verdict",
     "the head is re-classed from an ablation benchmark to the reading the "
     "review struck out, so the class word stops matching the payload's"),
    ("MUT-HEAD", "G-VERDICT-EQUALITY", "verdict",
     "the delivered head names a different tick from the one the payload "
     "carries"),
    ("MUT-PAPER-CLAIM", "G-PAPER-CLAIMS", "paper_claims",
     "a standing claim is inverted in the paper handed to the claim gate"),
    ("MUT-REFERENT", "G-PAPER-REFERENTS", "paper_referents",
     "a numeral from no universe is planted in a sentence about the "
     "observable census"),
    ("MUT-WALL", "G-PAPER-WALLS", "walls",
     "the paper is given a natural voicing of the forbidden exhaustive-class "
     "reading, phrased as a paper would phrase it"),
    ("MUT-WALL-POSITIVE", "G-PAPER-WALLS", "walls",
     "the wall's own standing sentence is deleted, so the positive leg is "
     "exercised alone"),
    ("MUT-COVERAGE", "G-PAPER-COVERAGE", "paper_coverage",
     "an unmeasured numeral is planted in the paper's prose"),
    ("MUT-TYPED", "G-TYPED-COUNTS", "typed_counts",
     "an offender is recorded by the typed-count audit"),
    ("MUT-FLOAT", "G-NO-FLOATS", "exactness",
     "a float site is recorded, so the exactness gate fails"),
    ("MUT-CONSUMER", "G-ANCHORS-CONSUMED", "anchors_consumed",
     "an anchor's declared consumer is rewritten to a gate that does not "
     "exist"),
    ("MUT-COVERAGE-SELF", "T-FALSIFIER-COVERAGE", "falsifier_coverage",
     "a sentinel-shaped recipe is recorded by the description audit"),
    ("MUT-TEMPLATE", "G-TEMPLATE-ADOPTED", "template",
     "one template family is dropped from the adopted list, so the adopted "
     "set stops covering the reference implementation's own"),
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
            "|--list-mutants|--mutant NAME|--render\n"
            "  --render and --list-gates are PARTIAL modes: they return "
            "before the paper gates\n")
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
        out_path = os.path.join(REPO, OUTPUT_REL)
        if mode == "--run" and os.path.exists(out_path):
            with open(out_path, "rb") as fh:
                rollback = fh.read()
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
            print("WROTE %s (%s) and %s (%s)"
                  % (RECEIPT_REL, dig["receipt"], OUTPUT_REL, dig["side"]))
        else:
            print("NO-WRITE: %d gates, nothing written" % len(LD.rows))
        return 0
    sys.stderr.write("unknown argument: %r\n" % mode)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
