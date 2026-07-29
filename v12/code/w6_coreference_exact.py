#!/usr/bin/env python3
"""
w6_coreference_exact.py -- v12 W6: RECORD CO-REFERENCE AND EFFECTIVE DESCENT.

Runs the STEP-0 referent census, the three sub-problems (A: fact co-reference,
B: event-token co-reference, C: effective descent) and the six mandatory
controls of the pin (v12/note-w6-record-coreference-pin.md), plus three
declared additions (M7 accidental agreement, M8 the phase rule, M9 the
descent-detector validation).

Substrate: exact arithmetic only.  Cyclotomic field Q(zeta_8) for the
dimension 4, 8 and 16 models; the totally real quartic field Q(cos pi/8) for
the committed 36-configuration composite model.  No floats anywhere.

Committed instruments imported READ-ONLY from ../paper1_code:
  exact.py           the fields, born(), mat_mul, is_unitary
  sec4_records.py    h_avail / h_corr / merge_partition / support_of
  sec7_descent.py    the cut-coherence tensor and its counters
  model_composite.py the 36-configuration two-measurement two-frame model

ANCHOR rows reuse a number committed elsewhere in the corpus: a mismatch is a
corpus contradiction and exits 1.  GATE rows are W6's own measurements
pre-registered against the value this unit claims: a mismatch means the claim
is wrong and exits 1.  A substantive negative (a co-reference that fails, a
descent that does not obtain) is a RESULT, not a failure, and exits 0.

EVERY row below is either an ANCHOR or a measurement whose value could have
come out otherwise.  Values restated downstream are referenced, never
re-gated.
"""

from __future__ import annotations

import itertools
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "paper1_code"))

from exact import Q, Cyc, born, hr, is_unitary, mat_mul                 # noqa
from sec4_records import (h_avail, h_corr, kron, merge_partition,       # noqa
                          support_of, delta_field, zero_mat)
from sec7_descent import tensor, off_diagonal, cross_sector             # noqa
from model_composite import (Composite, SETTINGS, SETTING_ORDER, NC,    # noqa
                             idx, unidx)

T0 = time.time()


def el():
    return "%.1fs" % (time.time() - T0)


def say(msg):
    print("  %-64s [%s]" % (msg, el()))
    sys.stdout.flush()


# ===========================================================================
# PART 0 -- the receipt harness
# ===========================================================================
class W6Receipts:
    def __init__(self, title):
        self.title = title
        self.rows = []

    def _add(self, kind, label, computed, expected):
        ok = (computed == expected)
        self.rows.append((kind, label, computed, expected, ok))
        if not ok:
            print("  !! %s FAIL  %s : computed %r != expected %r"
                  % (kind, label, computed, expected))
        return ok

    def anchor(self, label, computed, expected):
        """a number committed elsewhere in the corpus."""
        return self._add("ANCHOR", label, computed, expected)

    def gate(self, label, computed, expected):
        """a measurement of W6's own, pre-registered against this unit's claim."""
        return self._add("GATE", label, computed, expected)

    def finish(self):
        hr("=")
        print("RECEIPTS -- %s" % self.title)
        hr("=")
        w = max(len(r[1]) for r in self.rows)
        for kind, label, comp, exp, ok in self.rows:
            mark = "ok  " if ok else "FAIL"
            s = repr(comp)
            if len(s) > 200:
                s = s[:197] + "..."
            if ok:
                print("  %s %-6s %-*s  %s" % (mark, kind, w, label, s))
            else:
                print("  %s %-6s %-*s  computed %s != expected %r"
                      % (mark, kind, w, label, s, exp))
        na = sum(1 for r in self.rows if r[0] == "ANCHOR")
        ng = sum(1 for r in self.rows if r[0] == "GATE")
        npass = sum(1 for r in self.rows if r[4])
        nfail = len(self.rows) - npass
        hr("-")
        print("  %d rows (%d ANCHOR, %d GATE) : %d pass, %d fail   [%s]"
              % (len(self.rows), na, ng, npass, nfail, el()))
        return nfail


R = W6Receipts("W6 -- record co-reference and effective descent")

# the descent table accumulates here: (model, A, B, C, remark)
TABLE = []


# ===========================================================================
# PART 1 -- SPARSE EXACT LINEAR ALGEBRA (one representation for every model)
#
# Every chart's legs are sparse dicts {(row, col): field element}.  The
# dimension-4/8/16 models and the committed 36-configuration model therefore
# run through ONE code path; nothing is special-cased by model.
# ===========================================================================
def sp_of_dense(K, M):
    return {(i, j): v for i, row in enumerate(M)
            for j, v in enumerate(row) if not K.is_zero(v)}


def sp_dense(K, A, n):
    D = [[K.zero] * n for _ in range(n)]
    for (i, j), v in A.items():
        D[i][j] = v
    return D


def sp_mul(K, A, B):
    bycol = {}
    for (i, k), v in A.items():
        bycol.setdefault(k, []).append((i, v))
    out = {}
    for (k, j), v in B.items():
        for (i, u) in bycol.get(k, ()):
            t = K.mul(u, v)
            if K.is_zero(t):
                continue
            key = (i, j)
            s = K.add(out.get(key, K.zero), t)
            if K.is_zero(s):
                out.pop(key, None)
            else:
                out[key] = s
    return out


def sp_id(K, n):
    return {(i, i): K.one for i in range(n)}


def sp_conj(A, p):
    """(P A P^-1)[p[i]][p[j]] = A[i][j]."""
    return {(p[i], p[j]): v for (i, j), v in A.items()}


def sp_neg(K, A):
    return {k: K.neg(v) for k, v in A.items()}


def sp_born(K, A):
    return {k: K.mul(v, K.conj(v)) for k, v in A.items()}


def sp_restrict(A, rows, cols):
    return {(i, j): v for (i, j), v in A.items() if i in rows and j in cols}


# ===========================================================================
# PART 2 -- THE TYPED OBJECTS
#
#   Prov     provenance of a record token (W6-B's primitive)
#   Token    a chart-local stable record token: a partition of the chart's
#            configurations into value-labelled sectors, plus provenance,
#            plus its occurrence and availability status
#   Chart    a finite Barandes-style process (legs, initial configuration)
#            together with its declared record tokens and the joint law of
#            their ACTUAL values
# ===========================================================================
class Prov:
    """(generating interaction, local support, causal ancestry, copying
    lineage, erasure history).  Every field is read off the chart's own
    declared leg list; nothing cross-chart enters."""

    def __init__(self, gen, support, anc, lineage, erased=False):
        self.gen = gen
        self.support = frozenset(support)
        self.anc = tuple(anc)
        self.lineage = tuple(lineage)
        self.erased = bool(erased)

    def nominal_key(self):
        """the NAME-COMPARING key.  W6-B never uses it; M6 measures what it
        would do if it did."""
        return (self.gen, tuple(sorted(map(str, self.support))), self.anc)

    def structural_key(self):
        """the fields W6-B's post-filter compares: copying lineage (declared
        chart-locally, and only ever a ground for REJECTION) and erasure
        history (computed by (H-avail), not declared)."""
        return (self.lineage, self.erased)

    def __repr__(self):
        return "Prov(%s)" % (self.gen,)


class Token:
    def __init__(self, tid, part, values, write_leg, prov):
        self.tid = tid              # the token's chart-local name
        self.part = list(part)      # configuration -> sector label
        self.values = dict(values)  # sector label -> declared record VALUE
        self.write_leg = write_leg  # index of the leg that writes it
        self.prov = prov
        self.occurred = None        # (H-corr) at the writing leg
        self.avail = None           # (H-avail) under the declared later legs

    def valset(self):
        return tuple(sorted(map(str, self.values.values())))

    def __repr__(self):
        return "Token(%s)" % self.tid


class Chart:
    """a chart = one finite process (sparse legs + initial configuration) plus
    its declared record tokens."""

    def __init__(self, name, K, n, legs, j0, tokens, note=""):
        self.name = name
        self.K = K
        self.n = n
        self.legs = list(legs)
        self.j0 = j0
        self.note = note
        self.tokens = []
        for t in tokens:
            self._classify(t)
            if t.occurred:
                self.tokens.append(t)      # a record token EXISTS iff it occurred
        self.law = self._law()

    # -- occurrence and availability, by the committed instruments -----------
    def _classify(self, t):
        """(H-corr) is a property of the WRITING LEG (sec4_records.py:53 takes
        U1, the leg that writes); (H-avail) a property of the composition of
        the declared later legs (sec4_records.py:48)."""
        K, n = self.K, self.n
        Sw = support_of(K, sp_dense(K, self.legs[t.write_leg], n))
        t.occurred = h_corr(Sw, n, t.part)
        post = self.compose(self.legs[t.write_leg + 1:])
        t.avail = bool(t.occurred and h_avail(support_of(K, sp_dense(K, post, n)),
                                              n, t.part))
        t.prov.erased = bool(t.occurred and not t.avail)

    def compose(self, legs):
        M = sp_id(self.K, self.n)
        for L in legs:
            M = sp_mul(self.K, L, M)
        return M

    def final(self):
        return self.compose(self.legs)

    def dist(self, upto=None):
        """the exact distribution over configurations from j0, after `upto`
        legs (default: all of them)."""
        K = self.K
        T = self.compose(self.legs if upto is None else self.legs[:upto])
        out = {}
        for (i, j), v in T.items():
            if j == self.j0:
                p = K.mul(v, K.conj(v))
                if not K.is_zero(p):
                    out[i] = K.add(out.get(i, K.zero), p)
        return out

    def _law(self):
        """the joint law of the tokens' values, ACTUAL values only, read at the
        time every token has been written.  Reading it at the FINAL time would
        be wrong for an erased token: after erasure the later dynamics have
        moved amplitude across the record sectors, so the final distribution is
        not the record's law.  For an available record the two times agree --
        that is what availability means."""
        K = self.K
        upto = max((t.write_leg for t in self.tokens), default=-1) + 1
        p = self.dist(upto)
        out = {}
        for i, v in p.items():
            key = tuple(t.values[t.part[i]] for t in self.tokens)
            out[key] = K.add(out.get(key, K.zero), v)
        return {k: v for k, v in out.items() if not K.is_zero(v)}

    def marginal(self, tix):
        """the law marginalized onto the token indices tix (the probabilities
        on the shared record algebra)."""
        K = self.K
        out = {}
        for key, v in self.law.items():
            sub = tuple(key[i] for i in tix)
            out[sub] = K.add(out.get(sub, K.zero), v)
        return {k: v for k, v in out.items() if not K.is_zero(v)}

    def live(self, scope):
        """token indices in scope: 'available' = present records, 'historical'
        = records that occurred, erased or not."""
        if scope == "historical":
            return list(range(len(self.tokens)))
        return [i for i, t in enumerate(self.tokens) if t.avail]

    def read(self, i):
        """the value tuple this chart's record map assigns to configuration i."""
        return tuple(t.values[t.part[i]] for t in self.tokens)

    def __repr__(self):
        return "Chart(%s)" % self.name


def push_part(part, p):
    n = len(part)
    out = [None] * n
    for k in range(n):
        out[p[k]] = part[k]
    return out


def same_partition(pa, pb):
    """equality of partitions of the configuration set (sector names free)."""
    m, seen = {}, {}
    for x, y in zip(pa, pb):
        if x in m and m[x] != y:
            return False
        if y in seen and seen[y] != x:
            return False
        m[x] = y
        seen[y] = x
    return True


# ===========================================================================
# PART 3 -- PROCESS ISOMORPHISMS (what grounds a token label)
#
# A frame-isomorphism psi : b -> a is a bijection of configurations carrying
# b's initial configuration to a's, b's leg MULTISET to a's leg multiset under
# some matching (order is NOT preserved -- two frames of one experiment differ
# exactly by the order of two commuting legs, so order cannot be part of the
# invariant), and each of b's record partitions to one of a's.  It induces a
# token map tau.
#
# The MATCHING LEVEL is a declared parameter, because which level does the
# work is exactly what W6-B has to measure:
#   "exact" -- the amplitudes on the nose
#   "sign"  -- the amplitudes up to an overall sign per leg (a real orthogonal
#              propagator and its negative generate the same stochastic process)
#   "born"  -- the Born shadows only (the stochastic layer)
# ===========================================================================
def leg_match(K, X, Y, level):
    if X == Y:
        return True
    if level == "exact":
        return False
    if level == "sign":
        return X == sp_neg(K, Y)
    return sp_born(K, X) == sp_born(K, Y)


_ISO_CACHE = {}


def iso_maps(ca, cb, perms, level="exact", cache_key=None):
    """all token maps tau : cb.tokens -> ca.tokens induced by a
    frame-isomorphism cb -> ca, searched over the declared permutation scope
    `perms`.  Returns a list of dicts tau[i_b] = i_a."""
    if cache_key is not None and cache_key in _ISO_CACHE:
        return _ISO_CACHE[cache_key]
    K, n = ca.K, ca.n
    out = []
    if cb.n != n or len(cb.legs) != len(ca.legs):
        if cache_key is not None:
            _ISO_CACHE[cache_key] = out
        return out
    nl = len(ca.legs)
    orders = list(itertools.permutations(range(nl)))
    seen = set()
    for p in perms:
        if p[cb.j0] != ca.j0:
            continue
        conj = [sp_conj(L, p) for L in cb.legs]
        if not any(all(leg_match(K, conj[t], ca.legs[sg[t]], level)
                       for t in range(nl)) for sg in orders):
            continue
        tau, ok = {}, True
        for ib, tb in enumerate(cb.tokens):
            pushed = push_part(tb.part, p)
            hits = [ia for ia, ta in enumerate(ca.tokens)
                    if same_partition(pushed, ta.part)]
            if len(hits) != 1:
                ok = False
                break
            tau[ib] = hits[0]
        if ok and len(set(tau.values())) == len(tau) == len(ca.tokens):
            key = tuple(sorted(tau.items()))
            if key not in seen:
                seen.add(key)
                out.append(tau)
    if cache_key is not None:
        _ISO_CACHE[cache_key] = out
    return out


def all_perms(n):
    return list(itertools.permutations(range(n)))


# ===========================================================================
# PART 4 -- THE PRESERVATION LIST AND THE PHI SETS
#
#   1 Boolean operations      -- the induced map of record ATOMS is a bijection
#   2 definite record values  -- the declared value RANGE of each token
#   3 probabilities on the shared algebra -- exact equality of the marginals
#   4 persistence/availability
#   5+6 provenance and original-vs-copy -- level B only: the token map must be
#       induced by a frame-isomorphism AND survive the structural provenance
#       post-filter (copying lineage; erasure history)
#
# PHASE IS NOT ON THE LIST.  No item consults an amplitude phase or any phase
# invariant; the record-descent limit (W7 sec 23) makes that a category error.
# M8 constructs the phase-consulting item and runs it, to measure what it does.
# ===========================================================================
def push_key(key, tb, tau, ta):
    """re-index a value tuple of b (ordered by tb) into a's token order ta."""
    d = {tau[b]: key[i] for i, b in enumerate(tb)}
    return tuple(d[a] for a in ta)


def it_bool(ca, cb, tau, ta, tb):
    """item 1: the induced map of record atoms is a bijection."""
    A = set(ca.marginal(ta))
    B = {push_key(k, tb, tau, ta) for k in cb.marginal(tb)}
    return A == B and len(B) == len(cb.marginal(tb))


def it_values(ca, cb, tau, ta, tb):
    """item 2: the declared value range of each matched token agrees."""
    return all(cb.tokens[b].valset() == ca.tokens[tau[b]].valset() for b in tb)


def it_prob(ca, cb, tau, ta, tb):
    """item 3: exact equality of the marginals on the shared record algebra."""
    ma, mb = ca.marginal(ta), cb.marginal(tb)
    if len(ma) != len(mb):
        return False
    for k, v in mb.items():
        if ma.get(push_key(k, tb, tau, ta)) != v:
            return False
    return True


def it_avail(ca, cb, tau, ta, tb):
    """item 4: persistence / availability."""
    return all(cb.tokens[b].avail == ca.tokens[tau[b]].avail for b in tb)


def it_prov(ca, cb, tau, ta, tb):
    """items 5+6: the structural provenance post-filter -- copying lineage and
    erasure history.  Only ever a ground for rejection; it can never create an
    identification, so it cannot smuggle cross-chart identity in."""
    return all(cb.tokens[b].prov.structural_key()
               == ca.tokens[tau[b]].prov.structural_key() for b in tb)


def it_nominal(ca, cb, tau, ta, tb):
    """NOT on the list: provenance compared BY NAME.  Disclosed contrast only
    (M6): the names are exactly what is in question."""
    return all(cb.tokens[b].prov.nominal_key()
               == ca.tokens[tau[b]].prov.nominal_key() for b in tb)


LIST_A = [("1 boolean", it_bool), ("2 values", it_values),
          ("3 probabilities", it_prob), ("4 availability", it_avail)]
LIST_B = LIST_A + [("5+6 provenance", it_prov)]


def phi_set(ca, cb, scope="available", items=LIST_A, isos=None):
    """all admissible partial co-reference maps phi_ab : R_b -> R_a on `scope`,
    presented as token maps tau (index of b -> index of a).

    If `isos` is given (level B) the map must be the RESTRICTION TO THE SCOPE
    of a frame-isomorphism-induced token map.  Keying by restriction is what
    makes a scope-filtered chart (an erased token) behave correctly instead of
    silently returning zero."""
    ta, tb = ca.live(scope), cb.live(scope)
    if len(ta) != len(tb):
        return []
    out = []
    for perm in itertools.permutations(ta):
        tau = {tb[i]: perm[i] for i in range(len(tb))}
        if isos is not None:
            if not any(all(iso.get(b) == a for b, a in tau.items())
                       for iso in isos):
                continue
        if all(f(ca, cb, tau, ta, tb) for _, f in items):
            out.append(tau)
    return out


def bite_profile(ca, cb, scope="available", items=LIST_A):
    """which single item, ON ITS OWN, rejects every candidate token map."""
    ta, tb = ca.live(scope), cb.live(scope)
    if len(ta) != len(tb):
        return ["scope size"]
    kills = []
    for nm, f in items:
        if not any(f(ca, cb, {tb[i]: perm[i] for i in range(len(tb))}, ta, tb)
                   for perm in itertools.permutations(ta)):
            kills.append(nm)
    return kills


# --- the discriminator (census object 6) -----------------------------------
def verdict_of(nphi, na, nb, instrument=True):
    """|Phi| in the unit's own vocabulary.  The EMPTY SCOPE is called what it
    is -- a comparison of two trivial algebras is VACUOUS, not FORCED."""
    if not instrument:
        return "NO-INSTRUMENT"
    if na == 0 and nb == 0:
        return "VACUOUS"
    if nphi == 0:
        return "ABSENT"
    if nphi == 1:
        return "FORCED"
    return "UNDERDETERMINED"


# the descent table's cells are EMITTED by the discriminator, never typed as
# literals: a cell for which this unit runs no instrument gets the word the
# vocabulary reserves for it.
NOINST = verdict_of(0, 0, 0, instrument=False)


def route_ext(K, joint):
    """ROUTE-EXT: in a declared common record-preserving extension, are the two
    record variables perfectly correlated ALONG THE IDENTITY OF VALUES?  The
    joint law must be supported on the graph of a value-preserving bijection.
    Returns (certified, positive entries, bijection-supported); the third
    component is DERIVED from the same support and is reported only where the
    certificate fails and the reason matters.

    DEGENERACY GUARD.  A joint law with fewer than two positive entries
    certifies nothing: one point is trivially the graph of a bijection and the
    empty support is trivially value-preserving.  Certifying either would be
    the emptiness error the discriminator refuses at census 6, so the same
    word is used -- VACUOUS, not True."""
    pos = [(x, y) for (x, y), v in joint.items() if not K.is_zero(v)]
    if len(pos) < 2:
        return ("VACUOUS", len(pos), False)
    fwd, bwd = {}, {}
    for x, y in pos:
        if fwd.setdefault(x, y) != y or bwd.setdefault(y, x) != x:
            return (False, len(pos), False)
    bij = len(fwd) == len(bwd) == len(pos)
    ident = all(x == y for x, y in pos)
    return (bij and ident, len(pos), bij)


def route_ext_pair(K, joint, dis):
    """ROUTE-EXT as a verdict about a PAIR.  The common extension is built only
    where the two charts assign a configuration the same probability;
    configurations on which they DISAGREE are dropped by that construction, so
    a positive certificate on what remains certifies nothing about the pair.
    Where any configuration was dropped the verdict is DISAGREEMENT, not a
    certificate."""
    cert, npos, bij = route_ext(K, joint)
    return (cert if dis == 0 else "DISAGREEMENT", npos, bij)


# ===========================================================================
# PART 5 -- THE DESCENT SOLVER (W6-C)
#
# coherence laws: phi_aa = id; phi_ba = phi_ab^-1; phi_ab o phi_bc = phi_ac on
# triple overlaps, modulo the DECLARED gauge only.
#
# Every ORDERED edge that is declared is enumerated INDEPENDENTLY: the law
# phi_ba = phi_ab^-1 is a CONSTRAINT that a declared family can violate, not
# an identity imposed by the solver.  Triple equality is tested on the FULL
# domain, so a map with missing keys fails in both directions.
# ===========================================================================
def compose(tau_ab, tau_bc):
    """(a<-b) o (b<-c).  Keys absent from tau_ab are DROPPED here and caught by
    the full-domain equality test in descent()."""
    return {c: tau_ab[b] for c, b in tau_bc.items() if b in tau_ab}


def invert(tau):
    return {v: k for k, v in tau.items()}


def act(g, fam):
    """(g . phi)_{xy} = g_x o phi_xy o g_y^{-1}."""
    new = {}
    for (x, y), tau in fam.items():
        gy = invert(g[y])
        new[(x, y)] = {t: g[x][tau[gy[t]]] for t in gy
                       if gy[t] in tau and tau[gy[t]] in g[x]}
    return new


def famkey(fam):
    return tuple(sorted((k, tuple(sorted(v.items()))) for k, v in fam.items()))


def descent(names, phis, auts):
    """phis[(a,b)] = list of tau dicts (b -> a), ORDERED pairs; auts[a] = list
    of tau dicts (a -> a).  Returns a verdict dict."""
    edges = sorted(phis)
    ntri = sum(1 for a, b, c in itertools.permutations(names, 3)
               if (a, b) in phis and (b, c) in phis and (a, c) in phis)
    if any(len(phis[e]) == 0 for e in edges):
        return dict(verdict="ABSENT-PAIR", families=0, orbits=0,
                    edges=len(edges), triples=ntri, inverse_ok=None,
                    closed=None, moved=None, dupkeys=0)
    fams = []
    for pick in itertools.product(*[phis[e] for e in edges]):
        fam = {e: dict(t) for e, t in zip(edges, pick)}
        ok = True
        for (x, y) in edges:                       # law: phi_ba = phi_ab^-1
            if (y, x) in fam and fam[(y, x)] != invert(fam[(x, y)]):
                ok = False
                break
        if not ok:
            continue
        for a, b, c in itertools.permutations(names, 3):   # law: triples
            if (a, b) in fam and (b, c) in fam and (a, c) in fam:
                if compose(fam[(a, b)], fam[(b, c)]) != fam[(a, c)]:
                    ok = False
                    break
        if ok:
            fams.append(fam)
    if not fams:
        return dict(verdict="NO-DESCENT", families=0, orbits=0,
                    edges=len(edges), triples=ntri, inverse_ok=False,
                    closed=None, moved=None, dupkeys=0)
    keys = [famkey(f) for f in fams]
    dupkeys = len(keys) - len(set(keys))
    index = {k: i for i, k in enumerate(keys)}
    # the gauge action: is Phi closed under it?  (if not, the orbit count is
    # an over-count and the verdict must be scoped -- reported, not assumed)
    phikeys = {e: {tuple(sorted(t.items())) for t in phis[e]} for e in edges}
    closed, moved = True, False
    gs = list(itertools.product(*[auts[nm] for nm in names]))
    for f in fams:
        for g in gs:
            gm = dict(zip(names, [dict(x) for x in g]))
            gf = act(gm, f)
            for e, tau in gf.items():
                if tuple(sorted(tau.items())) not in phikeys[e]:
                    closed = False
            if famkey(gf) != famkey(f):
                moved = True
    seen, orbits = set(), 0
    for i in range(len(fams)):
        if i in seen:
            continue
        orbits += 1
        stack = [i]
        seen.add(i)
        while stack:
            cur = fams[stack.pop()]
            for g in gs:
                gm = dict(zip(names, [dict(x) for x in g]))
                kk = famkey(act(gm, cur))
                if kk in index and index[kk] not in seen:
                    seen.add(index[kk])
                    stack.append(index[kk])
    trivial_aut = all(len(auts[nm]) == 1 for nm in names)
    if orbits > 1:
        v = "UNDERDETERMINED"
    elif trivial_aut:
        v = "SET-AMALGAM"
    else:
        v = "GROUPOID-AMALGAM"
    return dict(verdict=v, families=len(fams), orbits=orbits,
                edges=len(edges), triples=ntri, inverse_ok=True,
                closed=closed, moved=moved, dupkeys=dupkeys)


def amalgam(names, charts, fam):
    """the set-level colimit of a coherent family: quotient the disjoint union
    of the charts' record tokens by the identifications.  Returns (size, ok)
    where ok is False if two tokens of ONE chart get identified."""
    par = {}

    def find(x):
        while par[x] != x:
            par[x] = par[par[x]]
            x = par[x]
        return x

    for nm in names:
        for i in range(len(charts[nm].tokens)):
            par[(nm, i)] = (nm, i)
    for (x, y), tau in fam.items():
        for b, a in tau.items():
            rx, ry = find((x, a)), find((y, b))
            if rx != ry:
                par[rx] = ry
    classes = {}
    for k in par:
        classes.setdefault(find(k), []).append(k)
    ok = all(len({nm for nm, _ in v}) == len(v) for v in classes.values())
    return len(classes), ok


def edge_sets(names, charts, **kw):
    """all ordered edges' Phi sets, and the automorphism sets."""
    phis = {(x, y): phi_set(charts[x], charts[y], **kw)
            for x, y in itertools.permutations(names, 2)}
    auts = {x: phi_set(charts[x], charts[x], **kw) for x in names}
    return phis, auts


# ===========================================================================
# PART 6 -- THE COMMON MATERIAL (dimension 4, 8, 16 over Q(zeta_8))
# ===========================================================================
K8 = Cyc(8)
ISQ2 = K8.scal(K8.add(K8.zpow(1), K8.zpow(-1)), Q(1, 2))
H = [[ISQ2, ISQ2], [ISQ2, K8.neg(ISQ2)]]
I2 = [[K8.one, K8.zero], [K8.zero, K8.one]]
CNOT = [[K8.one, K8.zero, K8.zero, K8.zero],
        [K8.zero, K8.one, K8.zero, K8.zero],
        [K8.zero, K8.zero, K8.zero, K8.one],
        [K8.zero, K8.zero, K8.one, K8.zero]]


def cnot3(ctrl, targ):
    M = [[K8.zero] * 8 for _ in range(8)]
    for j in range(8):
        b = [(j >> (2 - t)) & 1 for t in range(3)]
        if b[ctrl]:
            b[targ] ^= 1
        M[(b[0] << 2) | (b[1] << 1) | b[2]][j] = K8.one
    return M


def h3(q):
    M = [[K8.one]]
    for t in range(3):
        blk = H if t == q else I2
        M = kron(K8, M, blk) if len(M) > 1 else blk
    return M


def bit_part(n, which, nbits):
    return [(k >> (nbits - 1 - which)) & 1 for k in range(n)]


def haag(D, i, ip, j, jp):
    """the four-cycle (Bargmann / Haagerup) phase invariant of a dense matrix."""
    return K8.mul(K8.mul(D[i][j], D[ip][jp]),
                  K8.mul(K8.conj(D[i][jp]), K8.conj(D[ip][j])))


QUADS8 = [(i, ip, j, jp) for i in range(8) for ip in range(i + 1, 8)
          for j in range(8) for jp in range(j + 1, 8)]


# ===========================================================================
# STEP 0 -- THE REFERENT CENSUS (the computational half; the four gates are
# written out in the note)
# ===========================================================================
def step0():
    hr()
    print("STEP 0 -- THE REFERENT CENSUS")
    hr()

    # -- object 1: the chart-local stable record algebra ---------------------
    U1 = sp_of_dense(K8, mat_mul(K8, CNOT, kron(K8, H, I2)))
    U2 = sp_of_dense(K8, kron(K8, H, I2))
    part = [0, 1, 0, 1]
    S1 = support_of(K8, sp_dense(K8, U1, 4))
    S2 = support_of(K8, sp_dense(K8, U2, 4))
    R.anchor("census/record H-corr  [sec4_records.py:198]",
             h_corr(S1, 4, part), True)
    R.anchor("census/record H-avail [sec4_records.py:199]",
             h_avail(S2, 4, part), True)

    tok = Token("R", part, {0: "0", 1: "1"}, 0,
                Prov("CX", {"q0", "q1"}, ("PREP-H",), ("original",)))
    ch = Chart("census", K8, 4, [U1, U2], 0, [tok])
    R.gate("census/record algebra atoms and law",
           (sorted(ch.law), [str(K8.to_rat(ch.law[k])) for k in sorted(ch.law)]),
           ([("0",), ("1",)], ["1/2", "1/2"]))
    R.gate("census/occurrence and availability COMPUTED, not stipulated",
           (ch.tokens[0].occurred, ch.tokens[0].avail, ch.tokens[0].prov.erased),
           (True, True, False))
    say("object 1: chart-local record algebra R_a -- LOCATED and typed")

    # -- object 6: the insertion-vs-co-reference discriminator ---------------
    perms4 = all_perms(4)
    self_iso = iso_maps(ch, ch, perms4)
    nsa = len(phi_set(ch, ch, isos=self_iso, items=LIST_B))
    R.gate("census/discriminator on Phi(a,a): (|iso|, |Phi_B|, verdict)",
           (len(self_iso), nsa, verdict_of(nsa, 1, 1)), (1, 1, "FORCED"))
    # the vocabulary's four values are all realizable by the SAME function
    R.gate("census/discriminator vocabulary",
           (verdict_of(0, 1, 1), verdict_of(1, 1, 1), verdict_of(2, 1, 1),
            verdict_of(1, 0, 0), verdict_of(0, 1, 1, instrument=False)),
           ("ABSENT", "FORCED", "UNDERDETERMINED", "VACUOUS", "NO-INSTRUMENT"))
    # the same emptiness discipline on the CERTIFICATE side: a joint law with
    # fewer than two positive entries certifies nothing.  Unit probe: a
    # one-point joint and an empty joint must both come back VACUOUS.  Without
    # the guard both return (True, ...) -- a certificate obtained from nothing.
    R.gate("census/ROUTE-EXT degeneracy guard: one-point and empty joints",
           (route_ext(K8, {("0", "0"): K8.one}), route_ext(K8, {}),
            route_ext(K8, {("0", "0"): K8.zero})),
           (("VACUOUS", 1, False), ("VACUOUS", 0, False), ("VACUOUS", 0, False)))
    say("object 6: the discriminator |Phi| -- CONSTRUCTED")

    # -- REGRESSION GATE for the level-B scope keying ------------------------
    # a two-token chart one of whose tokens is erased.  Level B on the
    # AVAILABLE scope compares one token against one token; keying the
    # frame-isomorphism by its RESTRICTION to the scope is what stops this
    # from silently returning 0.
    L1 = sp_of_dense(K8, mat_mul(K8, cnot3(0, 1), h3(0)))
    L2 = sp_of_dense(K8, cnot3(0, 2))
    L3 = sp_of_dense(K8, h3(2))                        # erases the second token
    pv = Prov("CX1", {"q0", "q1"}, ("PREP-H",), ("original",))
    pw = Prov("CX2", {"q0", "q2"}, ("PREP-H",), ("original",))
    e1 = Chart("e1", K8, 8, [L1, L2, L3], 0,
               [Token("u", bit_part(8, 1, 3), {0: "0", 1: "1"}, 0, pv),
                Token("v", bit_part(8, 2, 3), {0: "0", 1: "1"}, 1, pw)])
    e2 = Chart("e2", K8, 8, [L1, L2, L3], 0,
               [Token("u", bit_part(8, 1, 3), {0: "0", 1: "1"}, 0,
                      Prov("CX1", {"q0", "q1"}, ("PREP-H",), ("original",))),
                Token("v", bit_part(8, 2, 3), {0: "0", 1: "1"}, 1,
                      Prov("CX2", {"q0", "q2"}, ("PREP-H",), ("original",)))])
    R.gate("census/regression model: (tokens, available, erased flags)",
           (len(e1.tokens), len(e1.live("available")),
            [t.prov.erased for t in e1.tokens]), (2, 1, [False, True]))
    perms8 = all_perms(8)
    iso12 = iso_maps(e1, e2, perms8, cache_key=("e1", "e2"))
    nav = len(phi_set(e1, e2, scope="available", items=LIST_B, isos=iso12))
    nhi = len(phi_set(e1, e2, scope="historical", items=LIST_B, isos=iso12))
    R.gate("census/REGRESSION scope-filtered level B does not zero: (avail, hist)",
           (nav, nhi), (1, 1))
    say("regression gate: level-B keying on a scope-filtered chart")
    return ch, perms4, perms8


# ===========================================================================
# M1 -- RELABELLED SAME RECORD (co-reference MUST succeed)
# ===========================================================================
def m1(perms4):
    hr()
    print("M1 -- RELABELLED SAME RECORD  (control 1)")
    hr()
    U1 = sp_of_dense(K8, mat_mul(K8, CNOT, kron(K8, H, I2)))
    U2 = sp_of_dense(K8, kron(K8, H, I2))
    part = [0, 1, 0, 1]

    def build(name, p):
        legs = [sp_conj(U1, p), sp_conj(U2, p)]
        tok = Token("R", push_part(part, p), {0: "0", 1: "1"}, 0,
                    Prov("CX", {"q0", "q1"}, ("PREP-H",), ("original",)))
        return Chart(name, K8, 4, legs, p[0], [tok])

    pid = (0, 1, 2, 3)
    p1 = (1, 2, 3, 0)
    p2 = (2, 3, 0, 1)
    a, b, c = build("a", pid), build("b", p1), build("c", p2)

    R.gate("M1/relabelling changes the presentation but not the record algebra",
           (a.legs != b.legs, a.j0 != b.j0, a.law == b.law, a.law == c.law),
           (True, True, True, True))
    isoab = iso_maps(a, b, perms4, cache_key=("m1a", "m1b"))
    nA = len(phi_set(a, b))
    nB = len(phi_set(a, b, items=LIST_B, isos=isoab))
    R.gate("M1/|Phi_A|, |Phi_B| and their verdicts a<-b",
           (nA, nB, verdict_of(nA, 1, 1), verdict_of(nB, 1, 1)),
           (1, 1, "FORCED", "FORCED"))

    # ROUTE-EXT: the common extension is the one process; configuration by
    # configuration, read a's record map and b's.  The relabelling p1 is the
    # identification of configurations, and it is USED, not assumed.
    K = K8

    def joint_of(rel):
        j = {}
        for i, pv in a.dist().items():
            key = (a.read(i), b.read(rel[i]))
            j[key] = K.add(j.get(key, K.zero), pv)
        return j
    ok, npos, _ = route_ext(K, joint_of(p1))
    okw, nposw, bijw = route_ext(K, joint_of(p2))
    R.gate("M1/ROUTE-EXT under the true relabelling vs a WRONG one",
           ((ok, npos), (okw, nposw, bijw)), ((True, 2), (False, 2, True)))

    names = ["a", "b", "c"]
    charts = {"a": a, "b": b, "c": c}
    isos = {(x, y): iso_maps(charts[x], charts[y], perms4,
                             cache_key=("m1", x, y))
            for x, y in itertools.product(names, repeat=2)}
    phis = {(x, y): phi_set(charts[x], charts[y], items=LIST_B,
                            isos=isos[(x, y)])
            for x, y in itertools.permutations(names, 2)}
    auts = {x: phi_set(charts[x], charts[x], items=LIST_B, isos=isos[(x, x)])
            for x in names}
    R.gate("M1/solver soundness: Phi inverse-closed, identity in every Aut",
           (all(invert(t) in phis[(y, x)]
                for (x, y) in phis for t in phis[(x, y)]),
            all({i: i for i in range(len(charts[x].tokens))} in auts[x]
                for x in names)), (True, True))
    d = descent(names, phis, auts)
    sz, inj = amalgam(names, charts, {k: v[0] for k, v in phis.items()})
    R.gate("M1/descent (verdict, families, orbits, edges, triples, closed)",
           (d["verdict"], d["families"], d["orbits"], d["edges"], d["triples"],
            d["closed"]), ("SET-AMALGAM", 1, 1, 6, 6, True))
    R.gate("M1/amalgam size, injective", (sz, inj), (1, True))
    TABLE.append(("M1 relabelled same record", "FORCED (certified)",
                  "FORCED", "SET-AMALGAM",
                  "the declared gauge acts trivially on the record algebra; "
                  "ROUTE-EXT fails under a wrong relabelling (gated)"))
    say("M1 done")


# ===========================================================================
# M2 -- REDUNDANT COPIES (A succeeds, B fails)
# ===========================================================================
def m2(perms8):
    hr()
    print("M2 -- REDUNDANT COPIES  (control 2)")
    hr()
    L1 = sp_of_dense(K8, mat_mul(K8, cnot3(0, 1), h3(0)))    # writes copy 1
    L2 = sp_of_dense(K8, cnot3(0, 2))                        # writes copy 2
    p1 = bit_part(8, 1, 3)
    p2 = bit_part(8, 2, 3)

    def pA():
        return Prov("CX1", {"q0", "q1"}, ("PREP-H",), ("original",))

    def pB():
        return Prov("CX2", {"q0", "q2"}, ("PREP-H", "CX1"), ("copy-of", "CX1"))

    a = Chart("a", K8, 8, [L1, L2], 0,
              [Token("R1", p1, {0: "0", 1: "1"}, 0, pA())])
    b = Chart("b", K8, 8, [L1, L2], 0,
              [Token("R2", p2, {0: "0", 1: "1"}, 1, pB())])
    R.gate("M2/both tokens occurred, available, laws identical",
           (a.tokens[0].occurred, b.tokens[0].occurred,
            a.tokens[0].avail, b.tokens[0].avail, a.law == b.law),
           (True, True, True, True, True))

    t0 = time.time()
    isoab = iso_maps(a, b, perms8, cache_key=("m2a", "m2b"))
    say("M2 isomorphism search over 8! permutations  %.1fs" % (time.time() - t0))
    nA = len(phi_set(a, b))
    nB = len(phi_set(a, b, items=LIST_B, isos=isoab))
    R.gate("M2/|Phi_A|, |Phi_B| and their verdicts a<-b",
           (nA, nB, verdict_of(nA, 1, 1), verdict_of(nB, 1, 1)),
           (1, 0, "FORCED", "ABSENT"))
    # WHICH layer refuses: the frame-isomorphism, or the provenance filter?
    nprov = len(phi_set(a, b, items=LIST_A + [("5+6 provenance", it_prov)]))
    R.gate("M2/DECOMPOSITION of the level-B zero: (iso alone, provenance alone)",
           (len(isoab), nprov), (0, 0))
    R.gate("M2/positive control: the searches are not vacuously empty",
           (len(iso_maps(a, a, perms8, cache_key=("m2a", "m2a"))),
            len(iso_maps(b, b, perms8, cache_key=("m2b", "m2b")))), (1, 1))
    sg = [0] * 8
    for j in range(8):
        bb = [(j >> (2 - t)) & 1 for t in range(3)]
        bb[1], bb[2] = bb[2], bb[1]
        sg[j] = (bb[0] << 2) | (bb[1] << 1) | bb[2]
    R.gate("M2/the register swap carries the partition but not the leg multiset",
           (same_partition(push_part(p2, sg), p1),
            sp_conj(L1, sg) in (L1, L2)), (True, False))

    # ROUTE-EXT on the ONE process carrying both tokens
    K = K8
    full = Chart("ab", K8, 8, [L1, L2], 0,
                 [Token("R1", p1, {0: "0", 1: "1"}, 0, pA()),
                  Token("R2", p2, {0: "0", 1: "1"}, 1, pB())])
    ok, npos, _ = route_ext(K, {k: v for k, v in full.law.items()})
    R.gate("M2/ROUTE-EXT perfect value-correlation on the one process",
           (ok, npos), (True, 2))
    R.gate("M2/the provenance data that separate the two tokens",
           (full.tokens[0].prov.structural_key(),
            full.tokens[1].prov.structural_key()),
           ((("original",), False), (("copy-of", "CX1"), False)))

    # -- ROUTE-WIT: the pin's second route, a specified common-record witness.
    def cnot4(ctrl, targ):
        Mx = [[K8.zero] * 16 for _ in range(16)]
        for j in range(16):
            bb = [(j >> (3 - t)) & 1 for t in range(4)]
            if bb[ctrl]:
                bb[targ] ^= 1
            Mx[(bb[0] << 3) | (bb[1] << 2) | (bb[2] << 1) | bb[3]][j] = K8.one
        return Mx
    H4 = kron(K8, kron(K8, kron(K8, H, I2), I2), I2)
    Lw = mat_mul(K8, cnot4(0, 3),
                 mat_mul(K8, cnot4(0, 2), mat_mul(K8, cnot4(0, 1), H4)))
    R.gate("M2/witness model unitary", is_unitary(K8, Lw), True)
    wt = [Token("t%d" % t, bit_part(16, t, 4), {0: "0", 1: "1"}, 0,
                Prov("CX%d" % t, {"q0", "q%d" % t}, ("PREP-H",),
                     ("original",) if t == 1 else ("copy-of", "CX1")))
          for t in (1, 2, 3)]
    W = Chart("wit", K8, 16, [sp_of_dense(K8, Lw)], 0, wt)
    R.gate("M2/witness model joint law", sorted(W.law),
           [("0", "0", "0"), ("1", "1", "1")])
    j13, j23, j12 = {}, {}, {}
    for key, v in W.law.items():
        j13[(key[0], key[2])] = K8.add(j13.get((key[0], key[2]), K8.zero), v)
        j23[(key[1], key[2])] = K8.add(j23.get((key[1], key[2]), K8.zero), v)
        j12[(key[0], key[1])] = K8.add(j12.get((key[0], key[1]), K8.zero), v)
    R.gate("M2/ROUTE-WIT: t1 vs witness, t2 vs witness, t1 vs t2",
           (route_ext(K8, j13)[0], route_ext(K8, j23)[0], route_ext(K8, j12)[0]),
           (True, True, True))

    # C: the atlas over {a, b, a-relabelled}, at BOTH levels
    p = tuple([0, 1, 2, 3, 4, 5, 6, 7][::-1])
    ar = Chart("c", K8, 8, [sp_conj(L1, p), sp_conj(L2, p)], p[0],
               [Token("R1", push_part(p1, p), {0: "0", 1: "1"}, 0, pA())])
    names = ["a", "b", "c"]
    charts = {"a": a, "b": b, "c": ar}
    phisA, autsA = edge_sets(names, charts)
    dA = descent(names, phisA, autsA)
    R.gate("M2/fact-level descent (verdict, families, triples)",
           (dA["verdict"], dA["families"], dA["triples"]), ("SET-AMALGAM", 1, 6))
    isos = {(x, y): iso_maps(charts[x], charts[y], perms8,
                             cache_key=("m2", x, y))
            for x, y in itertools.product(names, repeat=2)}
    phisB = {(x, y): phi_set(charts[x], charts[y], items=LIST_B,
                             isos=isos[(x, y)])
             for x, y in itertools.permutations(names, 2)}
    autsB = {x: phi_set(charts[x], charts[x], items=LIST_B, isos=isos[(x, x)])
             for x in names}
    R.gate("M2/THE FULL TOKEN-LEVEL EDGE SET |Phi_B| over the six ordered pairs",
           {e: len(v) for e, v in sorted(phisB.items())},
           {("a", "b"): 0, ("a", "c"): 1, ("b", "a"): 0, ("b", "c"): 0,
            ("c", "a"): 1, ("c", "b"): 0})
    dB = descent(names, phisB, autsB)
    R.gate("M2/token-level descent verdict", dB["verdict"], "ABSENT-PAIR")
    TABLE.append(("M2 redundant copies", "FORCED (certified twice)",
                  "ABSENT on the four copy edges, FORCED on the two "
                  "relabelling edges",
                  "SET-AMALGAM (fact) / ABSENT-PAIR (token)",
                  "one fact, two tokens; the two relabelling edges carry "
                  "|Phi_B| = 1, the four copy edges |Phi_B| = 0"))
    say("M2 done")


# ===========================================================================
# the committed 36-configuration composite model (M3, M4, M7)
# ===========================================================================
POINTER3 = {0: "r", 1: "+", 2: "-"}
PARTA = [unidx(i)[0] * 3 + unidx(i)[2] for i in range(NC)]     # sectors (qA, pA)
PARTB = [unidx(i)[1] * 3 + unidx(i)[3] for i in range(NC)]     # sectors (qB, pB)
PTRA = [unidx(i)[2] for i in range(NC)]                        # pointer A alone
PTRB = [unidx(i)[3] for i in range(NC)]                        # pointer B alone
VALS = {k: POINTER3[k % 3] for k in range(6)}


def cprov(wing, ang):
    return Prov("MEAS-%s@%d" % (wing, ang), {"q%s" % wing, "p%s" % wing},
                ("PREP",), ("original",))


def build_perm(swap, sa, sb, fa, fb):
    """the declared permutation scope: wing exchange x pointer 3-cycles x
    qubit flips."""
    sh = {0: 1, 1: 2, 2: 0}

    def shift(v, t):
        for _ in range(t):
            v = sh[v]
        return v
    p = [0] * NC
    for i in range(NC):
        qa, qb, pa, pb = unidx(i)
        qa2, qb2 = qa ^ fa, qb ^ fb
        pa2, pb2 = shift(pa, sa), shift(pb, sb)
        p[i] = idx(qb2, qa2, pb2, pa2) if swap else idx(qa2, qb2, pa2, pb2)
    return p


def build_perm_tr(swap, ta, tb, fa, fb):
    """the EXTENSION scope: the pointer TRANSPOSITION (+ <-> -) fixes the ready
    state r, so it survives the j0 filter where the 3-cycles do not."""
    tr = {0: 0, 1: 2, 2: 1}
    p = [0] * NC
    for i in range(NC):
        qa, qb, pa, pb = unidx(i)
        qa2, qb2 = qa ^ fa, qb ^ fb
        pa2 = tr[pa] if ta else pa
        pb2 = tr[pb] if tb else pb
        p[i] = idx(qb2, qa2, pb2, pa2) if swap else idx(qa2, qb2, pa2, pb2)
    return p


def composite_charts(M):
    """the twelve committed charts (6 settings x 2 frames) at the final record,
    the twelve at the intermediate slice, and the erasure variant."""
    finals, inters = {}, {}
    for sp in SETTING_ORDER:
        a8, b8 = SETTINGS[sp]
        for fr in ("F1", "F2"):
            legs = list(M.legs(sp, fr))
            wa = 1 if fr == "F1" else 2
            wb = 2 if fr == "F1" else 1
            tA = Token("R_A", PARTA, VALS, wa, cprov("A", a8))
            tB = Token("R_B", PARTB, VALS, wb, cprov("B", b8))
            finals[(sp, fr)] = Chart("%s/%s" % (sp, fr), M.K, NC, legs, 0,
                                     [tA, tB])
            # the intermediate slice: the process truncated after leg 2
            wing = "A" if fr == "F1" else "B"
            tok = Token("R_%s" % wing, PARTA if wing == "A" else PARTB, VALS, 1,
                        cprov(wing, a8 if wing == "A" else b8))
            inters[(sp, fr)] = Chart("%s/%s@t2" % (sp, fr), M.K, NC,
                                     legs[:2], 0, [tok])
    return finals, inters


def m3_m4_m7(M, finals, inters):
    hr()
    print("M3 / M4 / M7 -- THE COMMITTED TWO-FRAME BELL STRUCTURE")
    hr()
    K = M.K
    keys = sorted(finals)

    # -- committed anchors ---------------------------------------------------
    ops_ok = sum(1 for ang in (0, 2, 4, 6) for wg in ("A", "B")
                 if M.is_orthogonal(M.U_local(wg, ang)))
    R.anchor("M3/local operators orthogonal [sec4_records.py:516]", ops_ok, 8)
    comm = sum(1 for a8 in (0, 2, 4) for b8 in (0, 2, 6)
               if M.sp_mul(M.U_local("A", a8), M.U_local("B", b8))
               == M.sp_mul(M.U_local("B", b8), M.U_local("A", a8)))
    R.anchor("M3/local operators commute 9/9 [sec4_records.py:524]", comm, 9)
    R.anchor("M3/U_prep orthogonal [sec4_records.py:505]",
             M.is_orthogonal(M.U_prep()), True)

    # -- the record typing of the composite tokens, COMPUTED -----------------
    # (H-corr) fails for the pointer alone wherever the local operator is not
    # diagonal (the other wing's qubit is co-live); the (qX, pX) partition is
    # a genuine record structure at every setting.  Nothing is stipulated.
    prof = []
    for sp in SETTING_ORDER:
        a8, b8 = SETTINGS[sp]
        SA = support_of(K, sp_dense(K, M.U_local("A", a8), NC))
        SB = support_of(K, sp_dense(K, M.U_local("B", b8), NC))
        prof.append((h_corr(SA, NC, PTRA), h_corr(SA, NC, PARTA),
                     h_corr(SB, NC, PTRB), h_corr(SB, NC, PARTB)))
    R.gate("M3/(H-corr) pointer-alone vs (qX,pX), per setting", prof,
           [(True, True, False, True), (True, True, False, True),
            (False, True, False, True), (False, True, False, True),
            (True, True, True, True), (False, True, False, True)])
    R.gate("M3/all 24 composite tokens occurred and are available",
           (sum(len(finals[k].tokens) for k in keys),
            sum(len(finals[k].live("available")) for k in keys)), (24, 24))
    R.gate("M3/W6's chart law reproduces the committed outcome_law",
           all(finals[(sp, fr)].law
               == {(POINTER3[a], POINTER3[b]): v
                   for (a, b), v in M.outcome_law(sp, fr).items()
                   if not K.is_zero(v)}
               for sp in SETTING_ORDER for fr in ("F1", "F2")), True)
    say("the twelve committed charts built; record typing computed")

    # -- the frame structure -------------------------------------------------
    R.gate("M3/T3 identical in both frames, all settings",
           all(M.propagators(sp, "F1")[2] == M.propagators(sp, "F2")[2]
               for sp in SETTING_ORDER), True)
    diffs = []
    for sp in SETTING_ORDER:
        t2a, t2b = M.propagators(sp, "F1")[1], M.propagators(sp, "F2")[1]
        ks = set(t2a) | set(t2b)
        diffs.append(sum(1 for k in ks
                         if t2a.get(k, K.zero) != t2b.get(k, K.zero)))
    R.gate("M3/intermediate propagators differ, per setting", diffs,
           [270, 270, 432, 432, 108, 432])

    # -- M3 fact level: candidate maps vs law agreement ----------------------
    lawclass = {}
    for k in keys:
        lawclass.setdefault(tuple(sorted(finals[k].law.items())), []).append(k)
    R.gate("M3/final-law classes", sorted(len(v) for v in lawclass.values()),
           [2, 4, 6])
    agree, cand, viol = 0, 0, []
    for x, y in itertools.product(keys, repeat=2):
        same = finals[x].law == finals[y].law
        n = len(phi_set(finals[x], finals[y]))
        agree += 1 if same else 0
        cand += 1 if n > 0 else 0
        if same != (n > 0):
            viol.append((x, y))
    R.gate("M3/(law-agreeing pairs, candidate-admitting pairs, violations)",
           (agree, cand, viol), (56, 56, []))
    counts = {len(phi_set(finals[x], finals[y]))
              for x, y in itertools.product(keys, repeat=2)
              if finals[x].law == finals[y].law}
    R.gate("M3/|Phi_A| and its verdict on every law-agreeing pair",
           (sorted(counts), verdict_of(2, 2, 2)), ([2], "UNDERDETERMINED"))
    # DISCLOSED: on the committed twelve this biconditional is a ONE-ITEM
    # test.  Which items can bite at all, on this material?
    R.gate("M3/items that bite on two law-DISagreeing committed pairs "
           "(SP-A<-SP-B same atoms; SP-A<-SP-E 4 atoms vs 2)",
           (bite_profile(finals[("SP-A", "F1")], finals[("SP-B", "F1")]),
            bite_profile(finals[("SP-A", "F1")], finals[("SP-E", "F1")])),
           (["3 probabilities"], ["1 boolean", "3 probabilities"]))
    R.gate("M3/items 2 and 4 are CONSTANT on the committed twelve",
           (len({finals[k].tokens[t].valset() for k in keys for t in (0, 1)}),
            len({finals[k].tokens[t].avail for k in keys for t in (0, 1)})),
           (1, 1))
    say("M3 fact level measured: 56 agreeing pairs of 144")

    # -- the MULTI-ITEM controls: two variants on which items 2 and 4 bite ---
    # V2: the ready state of R_A is declared "z" rather than "r".  The ready
    # sector has probability zero at the final time, so the realized values and
    # the whole law are UNCHANGED -- only the declared value range differs.
    sp0 = ("SP-A", "F1")
    base = finals[sp0]
    v2 = Chart("V2", K, NC, base.legs, 0,
               [Token("R_A", PARTA, {k: ("z" if k % 3 == 0 else POINTER3[k % 3])
                                     for k in range(6)}, 1, cprov("A", 0)),
                Token("R_B", PARTB, VALS, 2, cprov("B", 2))])
    # V4: the same experiment continued by U_B twice more.  U_B^3 = 1, so the
    # final propagator, and the record law, are untouched -- but R_B is no
    # longer available: (H-avail) fails under U_B^2.  Erasure, computed.
    UB = M.U_local("B", SETTINGS["SP-A"][1])
    v4 = Chart("V4", K, NC, list(base.legs) + [UB, UB], 0,
               [Token("R_A", PARTA, VALS, 1, cprov("A", 0)),
                Token("R_B", PARTB, VALS, 2, cprov("B", 2))])
    R.gate("M3/V4 is a genuine erasure: (U_B^3 = 1, law kept, R_B available?)",
           (M.sp_mul(UB, M.sp_mul(UB, UB)) == sp_id(K, NC),
            v4.law == base.law, v4.tokens[1].avail), (True, True, False))
    R.gate("M3/V2 keeps the law and changes only the declared value range",
           (v2.law == base.law, v2.tokens[0].valset() == base.tokens[0].valset()),
           (True, False))
    n2 = len(phi_set(base, v2))
    n2d = len(phi_set(base, v2, items=[it for it in LIST_A
                                       if it[0] != "2 values"]))
    R.gate("M3/ITEM 2 BITES: |Phi_A(base<-V2)| with and without item 2",
           (n2, n2d, bite_profile(base, v2)), (0, 2, ["2 values"]))
    n4 = len(phi_set(base, v4, scope="historical"))
    n4d = len(phi_set(base, v4, scope="historical",
                      items=[it for it in LIST_A if it[0] != "4 availability"]))
    R.gate("M3/ITEM 4 BITES: |Phi_A(base<-V4)| historical, with and without it",
           (n4, n4d, bite_profile(base, v4, scope="historical")),
           (0, 2, ["4 availability"]))
    ext = dict(finals)
    ext[("V2", "-")] = v2
    ext[("V4", "-")] = v4
    ek = sorted(ext)
    viol2 = [(x, y) for x, y in itertools.product(ek, repeat=2)
             if (ext[x].law == ext[y].law) != (len(phi_set(ext[x], ext[y])) > 0)]
    R.gate("M3/the biconditional BREAKS on the 14-chart set (variant pairs)",
           len(viol2), 26)
    say("M3 multi-item controls measured (items 2 and 4 made to bite)")

    # -- M3 at level B: the declared scope, and its j0 filter ---------------
    scope = [build_perm(sw, sa, sb, fa, fb)
             for sw in (0, 1) for sa in range(3) for sb in range(3)
             for fa in (0, 1) for fb in (0, 1)]
    fixers = [(sw, sa, sb, fa, fb)
              for sw in (0, 1) for sa in range(3) for sb in range(3)
              for fa in (0, 1) for fb in (0, 1)
              if build_perm(sw, sa, sb, fa, fb)[0] == 0]
    R.gate("M3/SCOPE 72 (comprehension bound) and the j0 filter's fixers "
           "(the measured content)",
           (len(scope), fixers), (72, [(0, 0, 0, 0, 0), (1, 0, 0, 0, 0)]))
    # the extension: pointer TRANSPOSITIONS fix the ready state, so a wider
    # search survives the same filter.
    scope_x = sorted({tuple(p) for p in scope}
                     | {tuple(build_perm_tr(sw, ta, tb, fa, fb))
                        for sw in (0, 1) for ta in (0, 1) for tb in (0, 1)
                        for fa in (0, 1) for fb in (0, 1)})
    scope_x = [list(p) for p in scope_x]
    R.gate("M3/EXTENSION scope and its j0-fixing subset",
           (len(scope_x), sum(1 for p in scope_x if p[0] == 0)), (96, 8))

    nB, nBx, nBs, nBb, mapB = {}, {}, {}, {}, {}
    for sp in SETTING_ORDER:
        x, y = (sp, "F1"), (sp, "F2")
        i0 = iso_maps(finals[x], finals[y], scope)
        p0 = phi_set(finals[x], finals[y], items=LIST_B, isos=i0)
        nB[sp] = len(p0)
        mapB[sp] = sorted(tuple(sorted(t.items())) for t in p0)
        ix = iso_maps(finals[x], finals[y], scope_x)
        nBx[sp] = len(phi_set(finals[x], finals[y], items=LIST_B, isos=ix))
        isg = iso_maps(finals[x], finals[y], scope, level="sign")
        nBs[sp] = len(phi_set(finals[x], finals[y], items=LIST_B, isos=isg))
        ibo = iso_maps(finals[x], finals[y], scope, level="born")
        nBb[sp] = len(phi_set(finals[x], finals[y], items=LIST_B, isos=ibo))
    R.gate("M3/|Phi_B| F1<-F2 and the map itself, per setting: 2-element scope "
           "/ 8-element extension",
           ([nB[sp] for sp in SETTING_ORDER], [nBx[sp] for sp in SETTING_ORDER],
            sorted({tuple(mapB[sp]) for sp in SETTING_ORDER})),
           ([1] * 6, [1] * 6, [(((0, 0), (1, 1)),)]))
    R.gate("M3/|Phi_B| if legs were matched up to sign / at the Born level",
           ([nBs[sp] for sp in SETTING_ORDER], [nBb[sp] for sp in SETTING_ORDER]),
           ([1] * 6, [1] * 6))
    R.gate("M3/leg matching must be ORDER-FREE: isomorphisms if order required",
           [sum(1 for p in scope if p[0] == 0
                and all(sp_conj(M.legs(sp, "F2")[t], p) == M.legs(sp, "F1")[t]
                        for t in range(3))) for sp in SETTING_ORDER], [0] * 6)
    # does the provenance post-filter do any of the cutting here?
    R.gate("M3/DECOMPOSITION: |Phi_B| without the provenance item, per setting",
           [len(phi_set(finals[(sp, "F1")], finals[(sp, "F2")], items=LIST_A,
                        isos=iso_maps(finals[(sp, "F1")], finals[(sp, "F2")],
                                      scope))) for sp in SETTING_ORDER], [1] * 6)
    say("M3 level B measured at the true scope (2 permutations) and wider (8)")

    # -- the token-overlap graph, MEASURED and then CONSUMED ----------------
    t0 = time.time()
    adj = {x: set() for x in keys}
    for x, y in itertools.product(keys, repeat=2):
        if iso_maps(finals[x], finals[y], scope):
            adj[x].add(y)
    say("token-overlap graph measured over 144 ordered pairs  %.1fs"
        % (time.time() - t0))
    edgesB = sum(len(v) for v in adj.values())
    cross = sum(1 for x in keys for y in adj[x] if x[0] != y[0])
    # components by BFS ON THE GRAPH ITSELF
    und = {x: {y for y in adj[x] if y != x} | {y for y in keys if x in adj[y]
                                               and y != x} for x in keys}
    comps, seen = [], set()
    for x in keys:
        if x in seen:
            continue
        stack, comp = [x], []
        seen.add(x)
        while stack:
            u = stack.pop()
            comp.append(u)
            for v in und[u]:
                if v not in seen:
                    seen.add(v)
                    stack.append(v)
        comps.append(sorted(comp))
    tri = sum(1 for x, y, z in itertools.combinations(keys, 3)
              if y in und[x] and z in und[y] and z in und[x])
    R.gate("M3/overlap graph: (ordered edges, cross-setting, components, "
           "sizes, triangles)",
           (edgesB, cross, len(comps), sorted({len(c) for c in comps}), tri),
           (24, 0, 6, [2], 0))
    R.gate("M3/every component is one setting's two frames",
           all(len({v[0] for v in c}) == 1 for c in comps), True)

    # -- WHAT GROUNDS THE WING LABELLING: the layer measurement --------------
    w = build_perm(1, 0, 0, 0, 0)

    def col_of(T, sq):
        return {i: (K.mul(v, v) if sq else v) for (i, j), v in T.items()
                if j == 0 and not K.is_zero(v)}
    layer = []
    for sp in SETTING_ORDER:
        Ta = M.propagators(sp, "F1")[:3]
        Tb = M.propagators(sp, "F2")[:3]
        amp = all({w[i]: v for i, v in col_of(tb, False).items()}
                  == col_of(ta, False) for ta, tb in zip(Ta, Tb))
        sgn = all({w[i]: K.neg(v) for i, v in col_of(tb, False).items()}
                  == col_of(ta, False) for ta, tb in zip(Ta, Tb))
        bor = all({w[i]: v for i, v in col_of(tb, True).items()}
                  == col_of(ta, True) for ta, tb in zip(Ta, Tb))
        law = finals[(sp, "F1")].law
        sym = all(law.get((x, y)) == law.get((y, x))
                  for x in ("+", "-") for y in ("+", "-"))
        layer.append((amp, sgn, bor, sym))
    R.gate("M3/wing swap on (j0 amplitudes, up to sign, j0 Born, final law)",
           layer, [(False, False, False, True), (False, False, False, True),
                   (False, False, False, True), (False, False, False, True),
                   (False, True, True, True), (False, True, True, True)])

    # the TIME-INDEXED realized process: each leg restricted to the
    # configurations actually occupied before and after it.  This, and not the
    # time-independent reachable set, is the process the model realizes.
    # the DEFLATION CONTROL, kept from the pin's demand: restrict every leg to
    # the configurations reachable from j0 at ANY time (a time-INDEPENDENT
    # restriction).  If the wing-swap asymmetry were an artifact of U_prep's
    # arbitrary orthogonal completion it would vanish here.  It does not.
    reachctl = []
    for sp in SETTING_ORDER:
        rs = {0}
        for fr in ("F1", "F2"):
            for T in M.propagators(sp, fr)[:3]:
                for (i, j), v in T.items():
                    if j == 0 and not K.is_zero(v):
                        rs.add(i)
        LA = [sp_restrict(L, rs, rs) for L in M.legs(sp, "F1")]
        LB = [sp_restrict(L, rs, rs) for L in M.legs(sp, "F2")]
        ords = list(itertools.permutations(range(3)))
        reachctl.append((len(rs),) + tuple(
            any(all(leg_match(K, sp_conj(LB[t], w), LA[s[t]], lv)
                    for t in range(3)) for s in ords)
            for lv in ("exact", "sign", "born")))
    R.gate("M3/time-INDEPENDENT reachable-subprocess control: (size, wing swap "
           "exact/sign/Born)", reachctl,
           [(21, False, False, False), (21, False, False, False),
            (35, False, False, False), (35, False, False, False),
            (9, False, False, False), (27, False, False, False)])

    real, realB, realtype, t2sup = [], [], [], []
    for sp in SETTING_ORDER:
        rl, rc, sup2 = {}, {}, {}
        for fr in ("F1", "F2"):
            T = M.propagators(sp, fr)[:3]
            supp = [{0}] + [{i for (i, j), v in T[t].items()
                             if j == 0 and not K.is_zero(v)} for t in range(3)]
            rl[fr] = [sp_restrict(M.legs(sp, fr)[t], supp[t + 1], supp[t])
                      for t in range(3)]
            # the SAME charts, carried by the realized legs only -- and built
            # through the ORDINARY constructor, so that occurrence,
            # availability and the law are RECOMPUTED from the restricted legs
            # rather than stipulated.  That they come out as they do (two
            # tokens, both available, the same law) is then a measurement.
            tA = Token("R_A", PARTA, VALS, 1 if fr == "F1" else 2,
                       cprov("A", SETTINGS[sp][0]))
            tB = Token("R_B", PARTB, VALS, 2 if fr == "F1" else 1,
                       cprov("B", SETTINGS[sp][1]))
            rc[fr] = Chart("%s/%s@real" % (sp, fr), K, NC, rl[fr], 0, [tA, tB])
            realtype.append((len(rc[fr].tokens), len(rc[fr].live("available")),
                             rc[fr].law == finals[(sp, fr)].law))
            sup2[fr] = frozenset(supp[2])
        # WHY the identity cannot survive on the realized legs: at time 2 the
        # two frames have not occupied the same configurations -- one wing has
        # measured and the other has not.  Frame-relativity, and it is M4's own
        # content seen from the support side.
        t2sup.append((sup2["F1"] == sup2["F2"],
                      len(sup2["F1"]), len(sup2["F2"])))
        orders = list(itertools.permutations(range(3)))
        ex = any(all(sp_conj(rl["F2"][t], w) == rl["F1"][s[t]]
                     for t in range(3)) for s in orders)
        sg = any(all(leg_match(K, sp_conj(rl["F2"][t], w), rl["F1"][s[t]],
                               "sign") for t in range(3)) for s in orders)
        bo = any(all(leg_match(K, sp_conj(rl["F2"][t], w), rl["F1"][s[t]],
                               "born") for t in range(3)) for s in orders)
        real.append((ex, sg, bo))
        realB.append(tuple(
            sorted(tuple(sorted(t.items()))
                   for t in phi_set(rc["F1"], rc["F2"], items=LIST_B,
                                    isos=iso_maps(rc["F1"], rc["F2"], scope,
                                                  level=lv)))
            for lv in ("exact", "sign", "born")))
    R.gate("M3/the REALIZED charts, TYPED BY THE CONSTRUCTOR: (tokens, "
           "available, law == the full chart's law), all twelve",
           realtype, [(2, 2, True)] * 12)
    R.gate("M3/the two frames' TIME-2 occupied supports: (coincide?, sizes)",
           t2sup, [(False, 2, 8), (False, 2, 8), (False, 8, 8), (False, 8, 8),
                   (False, 2, 2), (False, 8, 8)])
    R.gate("M3/THE REALIZED PROCESS under the wing swap (exact, sign, Born)",
           real, [(False, False, False)] * 4 + [(False, True, True)] * 2)
    # THE ADJUDICATING MEASUREMENT: run level B on the realized legs alone.
    # Where the realized process is wing-symmetric the token tie is NOT cut --
    # so what cuts it on the full legs is declared structure the process never
    # exercises, and the level at which it cuts is the STOCHASTIC one.
    SWAP2 = ((0, 1), (1, 0))
    R.gate("M3/TOKEN MAPS admitted by the REALIZED legs alone "
           "(exact / up-to-sign / Born), per setting", realB,
           [([], [], [])] * 4 + [([], [SWAP2], [SWAP2])] * 2)
    # and WHICH declared leg refuses at the two symmetric settings
    refuse = []
    for sp in ("SP-E", "SP-F"):
        LA, LB = M.legs(sp, "F1"), M.legs(sp, "F2")
        refuse.append(tuple(any(leg_match(K, sp_conj(LB[t], w), LA[u], "born")
                                for u in range(3)) for t in range(3)))
    R.gate("M3/at SP-E,SP-F which FULL legs the wing swap matches (Born level)",
           refuse, [(False, True, True), (False, True, True)])
    # ISOLATED, column by column: the sole blocker is U_prep, and it blocks
    # OFF the j0 column.  On the j0 column w.U_prep.w is -U_prep -- a
    # sign-level match; on the other 35 columns it is neither +U_prep nor
    # -U_prep.  j0 = 0 is the only configuration ever occupied at time 0, so
    # those 35 columns are transitions the process never takes.
    Up = M.U_prep()
    Uw = sp_conj(Up, w)

    def colof(A, j):
        return {i: v for (i, jj), v in A.items() if jj == j}
    negcol = {j: {i: K.neg(v) for i, v in colof(Up, j).items()}
              for j in range(NC)}
    oth = range(1, NC)
    R.gate("M3/what blocks the wing swap on the FULL legs: w.U_prep.w vs "
           "U_prep, j0 column (+,-), the other 35 as a block (+,-), by column",
           (colof(Uw, 0) == colof(Up, 0), colof(Uw, 0) == negcol[0],
            all(colof(Uw, j) == colof(Up, j) for j in oth),
            all(colof(Uw, j) == negcol[j] for j in oth),
            sum(1 for j in oth if colof(Uw, j) == colof(Up, j)),
            sum(1 for j in oth if colof(Uw, j) == negcol[j])),
           (False, True, False, False, 9, 8))
    say("M3 layer analysis: the realized process vs the declared legs")

    # -- M3 ROUTE-EXT: the two frames' record maps, read off the one process -
    sp = "SP-A"
    T3a = M.propagators(sp, "F1")[2]
    T3b = M.propagators(sp, "F2")[2]
    f1, f2 = finals[(sp, "F1")], finals[(sp, "F2")]
    # a CORRUPTED partner: the same process with its two record partitions
    # exchanged.  If the joint were built diagonally by construction this
    # could not fail; it does.
    f2c = Chart("SP-A/F2*", K, NC, list(M.legs(sp, "F2")), 0,
                [Token("R_A", PARTB, VALS, 2, cprov("A", 0)),
                 Token("R_B", PARTA, VALS, 1, cprov("B", 2))])

    def joint_frames(other, Tb=T3b):
        j, dis = {}, 0
        for i in range(NC):
            va = T3a.get((i, 0), K.zero)
            vb = Tb.get((i, 0), K.zero)
            pa, pb = K.mul(va, va), K.mul(vb, vb)
            if pa != pb:
                dis += 1
                continue
            if K.is_zero(pa):
                continue
            if "r" in f1.read(i) or "r" in other.read(i):
                continue
            key = (f1.read(i), other.read(i))
            j[key] = K.add(j.get(key, K.zero), pa)
        return j, dis
    jt, dis = joint_frames(f2)
    jc, disc = joint_frames(f2c)
    ok, npos, _ = route_ext_pair(K, jt, dis)
    okc, nposc, bijc = route_ext_pair(K, jc, disc)
    R.gate("M3/ROUTE-EXT same-setting frames vs a CORRUPTED partner",
           ((ok, npos, dis), (okc, nposc, bijc)),
           ((True, 4, 0), (False, 4, False)))
    # POSITIVE CONTROL for the disagreement branch.  On same-experiment frames
    # dis is 0 and the branch is never taken, so it is exercised here against a
    # partner whose time-3 Born column genuinely differs: another setting's
    # frame.  The branch fires on 4 configurations -- and the raw certificate
    # computed on the 4 that remain is True, which is exactly why dropping
    # configurations must disqualify the pair rather than be silent.
    jd, disd = joint_frames(finals[("SP-B", "F2")],
                            M.propagators("SP-B", "F2")[2])
    R.gate("M3/the DISAGREEMENT branch EXERCISED on a Born-disagreeing partner",
           (disd, route_ext(K, jd)[0], route_ext_pair(K, jd, disd)),
           (4, True, ("DISAGREEMENT", 4, True)))

    # M7: SP-A and SP-C -- same final law, different experiments
    xa, xc = ("SP-A", "F1"), ("SP-C", "F1")
    R.gate("M7/same final law, different settings",
           (finals[xa].law == finals[xc].law, SETTINGS["SP-A"] != SETTINGS["SP-C"]),
           (True, True))
    prod = {}
    for k1, v1 in finals[xa].law.items():
        for k2, v2 in finals[xc].law.items():
            prod[(k1, k2)] = K.mul(v1, v2)
    ok7, npos7, bij7 = route_ext(K, prod)
    n7A = len(phi_set(finals[xa], finals[xc]))
    n7B = len(phi_set(finals[xa], finals[xc], items=LIST_B,
                      isos=iso_maps(finals[xa], finals[xc], scope)))
    R.gate("M7/(product-extension certificate, entries, |Phi_A|, |Phi_B|)",
           (ok7, bij7, npos7, n7A, n7B), (False, False, 16, 2, 0))
    R.gate("M7/verdicts A and B",
           (verdict_of(n7A, 2, 2), verdict_of(n7B, 2, 2)),
           ("UNDERDETERMINED", "ABSENT"))
    say("M7 accidental agreement measured inside the committed model")

    # -- M4: the intermediate slice -----------------------------------------
    nA4, nB4, cert4 = {}, {}, {}
    for sp in SETTING_ORDER:
        x, y = (sp, "F1"), (sp, "F2")
        nA4[sp] = len(phi_set(inters[x], inters[y]))
        nB4[sp] = len(phi_set(inters[x], inters[y], items=LIST_B,
                              isos=iso_maps(inters[x], inters[y], scope)))
        # ROUTE-EXT at t = 2 inside F1's own process: read the configuration
        # through F1's record map and through F2's.
        j = {}
        for i, pv in inters[x].dist().items():
            key = (inters[x].read(i), inters[y].read(i))
            j[key] = K.add(j.get(key, K.zero), pv)
        cert4[sp] = route_ext(K, j)[:2]
    R.gate("M4/|Phi_A| and |Phi_B| at the intermediate slice, per setting",
           ([nA4[sp] for sp in SETTING_ORDER], [nB4[sp] for sp in SETTING_ORDER]),
           ([1] * 6, [0] * 6))
    R.gate("M4/the candidate is NOT certified: ROUTE-EXT at t=2, per setting",
           [cert4[sp] for sp in SETTING_ORDER], [(False, 2)] * 6)
    R.gate("M4/both intermediate marginals uniform (the map is "
           "probability-preserving and still rejected)",
           all(sorted(str(K.to_rat(v)) for v in inters[(sp, fr)].law.values())
               == ["1/2", "1/2"] for sp in SETTING_ORDER for fr in ("F1", "F2")),
           True)
    # the shared record subalgebra, DERIVED: which declared record partitions
    # have occurred in BOTH charts by the slice time
    shared_int, shared_fin = [], []
    for sp in SETTING_ORDER:
        x, y = (sp, "F1"), (sp, "F2")
        shared_int.append(sum(1 for ta in inters[x].tokens
                              for tb in inters[y].tokens
                              if same_partition(ta.part, tb.part)))
        shared_fin.append(sum(1 for ta in finals[x].tokens
                              for tb in finals[y].tokens
                              if same_partition(ta.part, tb.part)))
    R.gate("M4/shared record subalgebra DERIVED: intermediate vs final",
           (shared_int, shared_fin), ([0] * 6, [2] * 6))
    # the rejection actually performed: which item kills the SP-E candidate
    extE = dict(finals[("SP-E", "F1")].law)
    okE, nposE, bijE = route_ext(K, extE)
    R.gate("M4/SP-E: bijection-supported but value-reversing, so REJECTED",
           (okE, nposE, bijE), (False, 2, True))
    say("M4 intermediate content measured")

    # -- M3 descent over a GENUINELY DISTINCT triple ------------------------
    # the third chart is F2 presented on a relabelled configuration set (the
    # declared gauge), built as its OWN object: its own legs, its own initial
    # configuration, its own token objects, its law RECOMPUTED.
    sp = "SP-A"
    pi = build_perm(0, 0, 0, 1, 1)
    f2 = finals[(sp, "F2")]
    f2r = Chart("SP-A/F2^pi", K, NC, [sp_conj(L, pi) for L in f2.legs], pi[0],
                [Token("R_A", push_part(PARTA, pi), VALS, 2, cprov("A", 0)),
                 Token("R_B", push_part(PARTB, pi), VALS, 1, cprov("B", 2))])
    R.gate("M3/the third chart is a DISTINCT object with derived record data",
           (f2r.legs != f2.legs, f2r.j0, f2.j0,
            f2r.tokens[0].part != f2.tokens[0].part, f2r.law == f2.law),
           (True, 27, 0, True, True))
    names = ["F1", "F2", "F2r"]
    charts = {"F1": finals[(sp, "F1")], "F2": f2, "F2r": f2r}
    phisA, autsA = edge_sets(names, charts)
    dA = descent(names, phisA, autsA)
    R.gate("M3/fact-level descent on the real triple "
           "(verdict, families, orbits, triples, moved, closed)",
           (dA["verdict"], dA["families"], dA["orbits"], dA["triples"],
            dA["moved"], dA["closed"]), ("GROUPOID-AMALGAM", 4, 1, 6, True, True))
    R.gate("M3/fact-level selections: 2 per ordered edge, 6 edges",
           ([len(phisA[e]) for e in sorted(phisA)],
            [len(autsA[x]) for x in names]), ([2] * 6, [2] * 3))
    isos3 = {(x, y): iso_maps(charts[x], charts[y], scope)
             for x, y in itertools.product(names, repeat=2)}
    phisB = {(x, y): phi_set(charts[x], charts[y], items=LIST_B,
                             isos=isos3[(x, y)])
             for x, y in itertools.permutations(names, 2)}
    autsB = {x: phi_set(charts[x], charts[x], items=LIST_B, isos=isos3[(x, x)])
             for x in names}
    R.gate("M3/token-level edge set on the real triple",
           ([len(phisB[e]) for e in sorted(phisB)],
            [len(autsB[x]) for x in names]), ([1] * 6, [1] * 3))
    dB = descent(names, phisB, autsB)
    szB, injB = amalgam(names, charts, {k: v[0] for k, v in phisB.items()})
    R.gate("M3/token-level descent on the real triple "
           "(verdict, families, triples, amalgam size, injective)",
           (dB["verdict"], dB["families"], dB["triples"], szB, injB),
           ("SET-AMALGAM", 1, 6, 2, True))
    say("M3 descent measured on a genuinely distinct triple")

    TABLE.append(("M3 two-frame final outcomes",
                  "UNDERDETERMINED (|Phi_A|=2), certified",
                  "FORCED (|Phi_B|=1, all 6 settings)",
                  "GROUPOID (fact) / SET-AMALGAM (token), at SP-A",
                  "candidate map on exactly the 56 law-agreeing ordered pairs "
                  "of 144; the wing tie is cut by dynamical provenance -- the "
                  "frame-isomorphism -- at the BORN level, not by the "
                  "structural provenance filter; on the REALIZED legs alone "
                  "the identity is inadmissible at every setting and SP-E, "
                  "SP-F admit exactly one map, the wing swap"))
    TABLE.append(("M4 intermediate frame content", "FORCED but NOT CERTIFIED",
                  "ABSENT (|Phi_B|=0)", NOINST + " -- no shared subalgebra",
                  "one token each, so |Phi_A|=1 carries no multiplicity; "
                  "ROUTE-EXT at t=2 refuses it at every setting"))
    TABLE.append(("M7 accidental agreement", "UNDERDETERMINED, NOT CERTIFIED",
                  "ABSENT (|Phi_B|=0)", NOINST + " -- no token edge",
                  "SP-A and SP-C: one law, two experiments; the product "
                  "extension has 16 positive entries"))
    return scope


# ===========================================================================
# M5 -- RECORD ERASURE
# ===========================================================================
def m5(perms4):
    hr()
    print("M5 -- RECORD ERASURE  (control 5)")
    hr()
    U1d = mat_mul(K8, CNOT, kron(K8, H, I2))
    U1 = sp_of_dense(K8, U1d)
    part = [0, 1, 0, 1]
    keepd = kron(K8, H, I2)
    erased = mat_mul(K8, kron(K8, H, I2), CNOT)
    nored = kron(K8, H, I2)
    keep, erase, nore = (sp_of_dense(K8, keepd), sp_of_dense(K8, erased),
                         sp_of_dense(K8, nored))

    def tk():
        return Token("R", part, {0: "0", 1: "1"}, 0,
                     Prov("CX", {"q0", "q1"}, ("PREP-H",), ("original",)))

    P = Chart("P", K8, 4, [U1, keep], 0, [tk()])
    E = Chart("E", K8, 4, [U1, erase], 0, [tk()])
    N = Chart("N", K8, 4, [nore, keep], 0, [tk()])

    # committed anchors
    R.anchor("M5/eraser H-corr holds [sec4_records.py:634]",
             h_corr(support_of(K8, U1d), 4, part), True)
    R.anchor("M5/eraser H-avail fails [sec4_records.py:635]",
             h_avail(support_of(K8, erased), 4, part), False)
    R.anchor("M5/no-record H-corr fails [sec4_records.py:209]",
             h_corr(support_of(K8, nored), 4, part), False)
    De = delta_field(K8, erased, U1d)
    R.anchor("M5/eraser defect values [sec4_records.py:633]",
             sorted({str(K8.to_rat(v)) for r in De for v in r}),
             ["-1/2", "0", "1/2"])
    R.anchor("M5/preserving defect zero [sec4_records.py:632]",
             zero_mat(K8, delta_field(K8, keepd, U1d)), True)
    Ce = tensor(K8, erased, U1d, 4)
    R.anchor("M5/eraser cross-sector tensor entries [sec7_descent.py:139]",
             cross_sector(K8, Ce, part, 4), 16)
    R.anchor("M5/preserving cross-sector entries [sec7_descent.py:137]",
             cross_sector(K8, tensor(K8, keepd, U1d, 4), part, 4), 0)
    R.gate("M5/eraser off-diagonal tensor entries (W6's own)",
           off_diagonal(K8, Ce, 4), 16)

    R.gate("M5/occurrence vs availability: (historical, available) counts P,E,N",
           ([len(x.live("historical")) for x in (P, E, N)],
            [len(x.live("available")) for x in (P, E, N)]),
           ([1, 1, 0], [1, 0, 0]))
    R.gate("M5/erased flags P,E",
           (P.tokens[0].prov.erased, E.tokens[0].prov.erased), (False, True))

    # LEVEL A and LEVEL B, both scopes, all three pairs -- real measurements
    def cell(ca, cb, scope):
        i = iso_maps(ca, cb, perms4, cache_key=("m5", ca.name, cb.name))
        na, nb = len(ca.live(scope)), len(cb.live(scope))
        a_ = len(phi_set(ca, cb, scope=scope))
        b_ = len(phi_set(ca, cb, scope=scope, items=LIST_B, isos=i))
        return (a_, verdict_of(a_, na, nb), b_, verdict_of(b_, na, nb))
    # the discriminator's emptiness guard: on an empty scope the single map is
    # the EMPTY map and the comparison is VACUOUS -- at both levels, whatever
    # the count.  (|Phi_B| = 0 here because no frame-isomorphism between the
    # whole charts exists at all: E has one historical token and N has none.)
    R.gate("M5/E<-N available: the EMPTY MAP is VACUOUS, not forced",
           cell(E, N, "available"), (1, "VACUOUS", 0, "VACUOUS"))
    R.gate("M5/E<-N historical: erased token is not 'no event'",
           cell(E, N, "historical"), (0, "ABSENT", 0, "ABSENT"))
    R.gate("M5/P<-E historical: availability separates them",
           cell(P, E, "historical"), (0, "ABSENT", 0, "ABSENT"))
    R.gate("M5/P<-E available: one available token against none",
           cell(P, E, "available"), (0, "ABSENT", 0, "ABSENT"))
    # POSITIVE CONTROL: the zero is caused by the availability item alone
    R.gate("M5/P and E carry the same record law", P.law == E.law, True)
    R.gate("M5/which item kills P<-E historical",
           bite_profile(P, E, scope="historical"), ["4 availability"])
    E.tokens[0].avail = True
    forced = len(phi_set(P, E, scope="historical"))
    E.tokens[0].avail = False
    restored = len(phi_set(P, E, scope="historical"))
    R.gate("M5/availability forced equal, then restored", (forced, restored),
           (1, 0))
    TABLE.append(("M5 record erasure", "ABSENT historical / VACUOUS available",
                  "ABSENT (|Phi_B|=0)", NOINST + " -- no triple declared",
                  "historical counts (1,1,0) against available (1,0,0); "
                  "the empty-scope comparison is called VACUOUS, not FORCED"))
    say("M5 done")


# ===========================================================================
# M6 -- SYMMETRIC DUPLICATE
# ===========================================================================
def m6(perms8):
    hr()
    print("M6 -- SYMMETRIC DUPLICATE  (control 6)")
    hr()
    L = mat_mul(K8, mat_mul(K8, cnot3(0, 2), cnot3(0, 1)), h3(0))
    # the wing-swapped BUILD: the same circuit with the roles of qubits 1 and 2
    # exchanged, assembled from the gate primitives.  It is MEASURED equal to
    # the original -- the two CNOTs commute -- which is a real symmetry of the
    # circuit, and it is that symmetry, not the assembly route, that the phase
    # sweep below tests.
    Lsw = mat_mul(K8, mat_mul(K8, cnot3(0, 1), cnot3(0, 2)), h3(0))
    R.gate("M6/leg unitary, and the swapped build is MEASURED equal to it",
           (is_unitary(K8, L), Lsw == L), (True, True))
    sig = [0] * 8
    for j in range(8):
        b = [(j >> (2 - t)) & 1 for t in range(3)]
        b[1], b[2] = b[2], b[1]
        sig[j] = (b[0] << 2) | (b[1] << 1) | b[2]
    R.gate("M6/sigma preserves the Born shadow",
           [[born(K8, L)[sig[i]][sig[j]] for j in range(8)] for i in range(8)]
           == born(K8, L), True)

    # THE PHASE SWEEP.  With the swapped build measured equal to L, the sweep
    # is the sigma-invariance of L's four-cycle invariants: the invariant at
    # sigma-relabelled indices against the invariant at the original indices.
    # The identical sweep is then run on a PERTURBED leg that differs from L by
    # a phase the Born shadow cannot see -- and it fails, so the sweep is not
    # a tautology.
    bad = sum(1 for (i, ip, j, jp) in QUADS8
              if haag(L, i, ip, j, jp)
              != haag(Lsw, sig[i], sig[ip], sig[j], sig[jp]))
    Lp = [row[:] for row in L]
    Lp[1][5] = K8.mul(Lp[1][5], K8.zpow(1))            # one entry, phase zeta_8
    badp = sum(1 for (i, ip, j, jp) in QUADS8
               if haag(Lp, i, ip, j, jp)
               != haag(Lp, sig[i], sig[ip], sig[j], sig[jp]))
    R.gate("M6/four-cycle sweep: (quadruples, violations on L, on a "
           "phase-perturbed L')", (len(QUADS8), bad, badp), (784, 0, 2))
    R.gate("M6/the perturbation is invisible to the Born shadow",
           (born(K8, Lp) == born(K8, L),
            sum(1 for q in QUADS8 if haag(L, *q) != haag(Lp, *q))), (True, 1))

    p1, p2 = bit_part(8, 1, 3), bit_part(8, 2, 3)

    def build(name):
        return Chart(name, K8, 8, [sp_of_dense(K8, L)], 0,
                     [Token("t1", p1, {0: "0", 1: "1"}, 0,
                            Prov("CX-A", {"q0", "q1"}, ("PREP-H",),
                                 ("original",))),
                      Token("t2", p2, {0: "0", 1: "1"}, 0,
                            Prov("CX-B", {"q0", "q2"}, ("PREP-H",),
                                 ("original",)))])

    a, b, c = build("a"), build("b"), build("c")
    R.gate("M6/both tokens occurred and available; the law is the correlated "
           "pair", ([(t.occurred, t.avail) for t in a.tokens], sorted(a.law)),
           ([(True, True)] * 2, [("0", "0"), ("1", "1")]))
    ok, npos, _ = route_ext(K8, dict(a.law))
    R.gate("M6/ROUTE-EXT inside one chart certifies ONE fact", (ok, npos),
           (True, 2))

    t0 = time.time()
    isoab = iso_maps(a, b, perms8, cache_key=("m6a", "m6b"))
    say("M6 isomorphism search over 8! permutations  %.1fs" % (time.time() - t0))
    nA = len(phi_set(a, b))
    nB = len(phi_set(a, b, items=LIST_B, isos=isoab))
    R.gate("M6/|Phi_A|, |Phi_B| and their verdicts a<-b",
           (nA, nB, verdict_of(nA, 2, 2), verdict_of(nB, 2, 2)),
           (2, 2, "UNDERDETERMINED", "UNDERDETERMINED"))
    # DISCLOSED CONTRAST: a name-comparing provenance filter WOULD choose.
    nname = len(phi_set(a, b, items=LIST_B + [("nominal", it_nominal)],
                        isos=isoab))
    R.gate("M6/what a NAME-comparing provenance filter would return", nname, 1)

    names = ["a", "b", "c"]
    charts = {"a": a, "b": b, "c": c}
    isos = {(x, y): iso_maps(charts[x], charts[y], perms8,
                             cache_key=("m6", x, y))
            for x, y in itertools.product(names, repeat=2)}
    phis = {(x, y): phi_set(charts[x], charts[y], items=LIST_B,
                            isos=isos[(x, y)])
            for x, y in itertools.permutations(names, 2)}
    auts = {x: phi_set(charts[x], charts[x], items=LIST_B, isos=isos[(x, x)])
            for x in names}
    R.gate("M6/solver soundness: |Aut| per chart, Phi inverse-closed, identity "
           "present",
           ([len(auts[x]) for x in names],
            all(invert(t) in phis[(y, x)] for (x, y) in phis
                for t in phis[(x, y)]),
            all({0: 0, 1: 1} in auts[x] for x in names)),
           ([2, 2, 2], True, True))
    d = descent(names, phis, auts)
    R.gate("M6/descent (verdict, families, orbits, gauge moves them, Phi "
           "gauge-closed, duplicate keys)",
           (d["verdict"], d["families"], d["orbits"], d["moved"], d["closed"],
            d["dupkeys"]), ("GROUPOID-AMALGAM", 4, 1, True, True, 0))
    # the selection space is ENUMERATED, not asserted: its size is the length
    # of the enumeration, and the inverse law's cut is counted on the same list.
    edg = sorted(phis)
    picks = list(itertools.product(*[phis[e] for e in edg]))
    ninv = sum(1 for pick in picks
               if all(pick[edg.index((y, x))] == invert(pick[edg.index((x, y))])
                      for (x, y) in edg))
    R.gate("M6/the enumerated selection space over the 6 ordered edges, and "
           "the inverse law's cut", (len(picks), ninv), (64, 8))
    TABLE.append(("M6 symmetric duplicate", "UNDERDETERMINED (|Phi_A|=2)",
                  "UNDERDETERMINED (|Phi_B|=2)", "GROUPOID-AMALGAM",
                  "the swapped build is measured equal to the original and "
                  "the 784 four-cycle invariants are then measured "
                  "sigma-invariant (a zeta_8 perturbation makes the sweep "
                  "fail); only a name-comparing rule would choose"))
    say("M6 done")


# ===========================================================================
# M8 -- PHASE IS NOT A CRITERION (the pin's HARD RULE, measured)
# ===========================================================================
def it_phase(ca, cb, tau, ta, tb):
    """NOT on the preservation list.  The phase-consulting item, constructed
    and actually run in M8: the two charts' composites must carry the same
    multiset of four-cycle invariants."""
    Da = sp_dense(ca.K, ca.final(), ca.n)
    Db = sp_dense(cb.K, cb.final(), cb.n)
    n = ca.n
    qs = [(i, ip, j, jp) for i in range(n) for ip in range(i + 1, n)
          for j in range(n) for jp in range(j + 1, n)]
    return (sorted(repr(haag(Da, *q)) for q in qs)
            == sorted(repr(haag(Db, *q)) for q in qs))


def m8(perms4):
    hr()
    print("M8 -- PHASE IS NOT A CRITERION  (declared addition)")
    hr()

    def embed(A, B, ra, ca, rb, cb):
        Mx = [[K8.zero] * 4 for _ in range(4)]
        for i in range(2):
            for j in range(2):
                Mx[ra[i]][ca[j]] = A[i][j]
                Mx[rb[i]][cb[j]] = B[i][j]
        return Mx

    Hd = [[K8.mul(H[i][j], K8.zpow(1) if j == 1 else K8.one) for j in range(2)]
          for i in range(2)]
    U2w = embed(H, H, [0, 1], [2, 3], [2, 3], [0, 1])
    U2wp = embed(H, Hd, [0, 1], [2, 3], [2, 3], [0, 1])
    U1w = embed(H, H, [0, 2], [2, 3], [1, 3], [0, 1])
    mp = merge_partition(support_of(K8, U2w), 4)
    R.anchor("M8/limit merge classes [sec7_descent.py:239]", mp, [1, 1, 3, 3])
    R.anchor("M8/limit has a record structure [sec7_descent.py:240]",
             h_corr(support_of(K8, U1w), 4, mp), True)
    R.anchor("M8/limit tensor fully diagonal [sec7_descent.py:241]",
             off_diagonal(K8, tensor(K8, U2w, U1w, 4), 4), 0)
    P1, P2 = mat_mul(K8, U2w, U1w), mat_mul(K8, U2wp, U1w)
    R.anchor("M8/composites differ in the four-cycle invariant "
             "[sec7_descent.py:242]",
             haag(P1, 0, 2, 0, 2) != haag(P2, 0, 2, 0, 2), True)

    R.gate("M8/every record-level datum agrees (leg and composite shadows)",
           (born(K8, U2w) == born(K8, U2wp), born(K8, P1) == born(K8, P2)),
           (True, True))
    part = [0, 0, 1, 1]

    def tk():
        return Token("R", part, {0: "0", 1: "1"}, 0,
                     Prov("W", {"c0", "c1"}, ("PREP",), ("original",)))
    a = Chart("a", K8, 4, [sp_of_dense(K8, U1w), sp_of_dense(K8, U2w)], 0, [tk()])
    b = Chart("b", K8, 4, [sp_of_dense(K8, U1w), sp_of_dense(K8, U2wp)], 0,
              [tk()])
    R.gate("M8/record algebras identical", a.law == b.law, True)
    nA = len(phi_set(a, b))
    # the phase-consulting phi, CONSTRUCTED and RUN
    nP = len(phi_set(a, b, items=LIST_A + [("phase", it_phase)]))
    R.gate("M8/|Phi_A| with the declared list, and with a phase item added",
           (nA, nP, verdict_of(nA, 1, 1), verdict_of(nP, 1, 1)),
           (1, 0, "FORCED", "ABSENT"))
    # the same phase item must NOT wrongly kill a legitimate identification
    U1r = sp_of_dense(K8, mat_mul(K8, CNOT, kron(K8, H, I2)))
    U2r = sp_of_dense(K8, kron(K8, H, I2))
    pr = (1, 2, 3, 0)
    r1 = Chart("r1", K8, 4, [U1r, U2r], 0,
               [Token("R", [0, 1, 0, 1], {0: "0", 1: "1"}, 0,
                      Prov("CX", {"q0"}, ("PREP",), ("original",)))])
    r2 = Chart("r2", K8, 4, [sp_conj(U1r, pr), sp_conj(U2r, pr)], pr[0],
               [Token("R", push_part([0, 1, 0, 1], pr), {0: "0", 1: "1"}, 0,
                      Prov("CX", {"q0"}, ("PREP",), ("original",)))])
    R.gate("M8/the phase item is not indiscriminate: it passes a relabelling",
           len(phi_set(r1, r2, items=LIST_A + [("phase", it_phase)])), 1)
    TABLE.append(("M8 phase blindness", "FORCED with the declared list; "
                  "ABSENT with phase added", NOINST,
                  NOINST + " -- criterion test, no descent claim",
                  "a phase-consulting item was built and run: it returns 0 on "
                  "this pair, where the declared list returns 1, and 1 on a "
                  "relabelling pair"))
    say("M8 done")


# ===========================================================================
# M9 -- THE DESCENT DETECTOR, VALIDATED (declared addition)
# ===========================================================================
def m9():
    hr()
    print("M9 -- DESCENT DETECTOR VALIDATION  (declared addition)")
    hr()
    names = ["a", "b", "c"]
    ident_, swap_ = {0: 0, 1: 1}, {0: 1, 1: 0}

    def edges(spec):
        return {k: [dict(v)] for k, v in spec.items()}

    def law_profile(fam):
        """WHICH coherence law rejects a declaration.  descent() stops at the
        first violation, so the two laws are counted here independently: a
        declaration rejected by the inverse law never reaches the triple law,
        and a control that claims the triple law must be inverse-consistent."""
        ninv = sum(1 for (x, y) in fam
                   if (y, x) in fam and fam[(y, x)] != invert(fam[(x, y)]))
        ntri = sum(1 for a, b, c in itertools.permutations(names, 3)
                   if (a, b) in fam and (b, c) in fam and (a, c) in fam
                   and compose(fam[(a, b)], fam[(b, c)]) != fam[(a, c)])
        return (ninv, ntri)
    base = {(x, y): ident_ for x, y in itertools.permutations(names, 2)}
    tw = dict(base)
    tw[("a", "c")] = swap_
    tw[("c", "a")] = swap_
    d1 = descent(names, edges(tw), {x: [dict(ident_)] for x in names})
    d2 = descent(names, edges(base), {x: [dict(ident_)] for x in names})
    R.gate("M9/holonomy: twisted vs consistent pinning of the SAME charts",
           ((d1["verdict"], d1["families"]), (d2["verdict"], d2["families"])),
           (("NO-DESCENT", 0), ("SET-AMALGAM", 1)))
    # NEGATIVE CONTROL: an ASYMMETRIC declaration.  The reverse leg is
    # consulted, not silently replaced by the inverse.
    asym = dict(base)
    asym[("b", "a")] = swap_
    d3 = descent(names, edges(asym), {x: [dict(ident_)] for x in names})
    R.gate("M9/asymmetric declaration (phi_ba != phi_ab^-1) must FAIL",
           (d3["verdict"], d3["families"]), ("NO-DESCENT", 0))
    # NEGATIVE CONTROL: a map with a MISSING KEY, declared INVERSE-CONSISTENTLY
    # (both directions truncated to the same domain) so that the inverse law
    # passes and the FULL-DOMAIN TRIPLE LAW is what rejects it -- which is what
    # this control's label claims.  Triple equality is tested on the full
    # domain, so the truncated map fails in both directions.
    part = dict(base)
    part[("a", "b")] = {0: 0}
    part[("b", "a")] = {0: 0}
    d4 = descent(names, edges(part), {x: [dict(ident_)] for x in names})
    R.gate("M9/an INVERSE-CONSISTENT partial-domain map must FAIL the "
           "full-domain triple law",
           (d4["verdict"], d4["families"]), ("NO-DESCENT", 0))
    # and WHICH law does the rejecting in each case, counted independently of
    # descent()'s early exit: the asymmetric declaration is caught by the
    # inverse law, the truncated one only by the triple law.
    R.gate("M9/WHICH law rejects: (inverse, triple) violations, the asymmetric "
           "declaration then the partial-domain one",
           (law_profile(asym), law_profile(part)), ((2, 3), (0, 6)))
    # the fourth branch: two coherent families, trivial automorphisms
    two = ["a", "b"]
    d5 = descent(two, {("a", "b"): [dict(ident_), dict(swap_)],
                       ("b", "a"): [dict(ident_), dict(swap_)]},
                 {"a": [dict(ident_)], "b": [dict(ident_)]})
    R.gate("M9/two families, trivial Aut: UNDERDETERMINED, gauge cannot move "
           "them", (d5["verdict"], d5["families"], d5["orbits"], d5["moved"]),
           ("UNDERDETERMINED", 2, 2, False))
    # the fifth branch
    d6 = descent(two, {("a", "b"): []}, {"a": [dict(ident_)],
                                         "b": [dict(ident_)]})
    R.gate("M9/empty Phi on a pair", d6["verdict"], "ABSENT-PAIR")
    # the LATENT case the classification must not misreport: one coherent
    # family, nontrivial Aut, gauge acting TRIVIALLY on it
    d7 = descent(two, {("a", "b"): [dict(ident_)], ("b", "a"): [dict(ident_)]},
                 {"a": [dict(ident_), dict(swap_)],
                  "b": [dict(ident_), dict(swap_)]})
    R.gate("M9/one family with nontrivial Aut: gauge action and closure "
           "reported, not assumed",
           (d7["verdict"], d7["families"], d7["moved"], d7["closed"]),
           ("GROUPOID-AMALGAM", 1, True, False))
    TABLE.append(("M9 detector validation", NOINST, NOINST,
                  "all five branches reached",
                  "the twisted declaration fails the triple law, the "
                  "asymmetric one the inverse law, the inverse-consistent "
                  "truncated one the full-domain triple law; gauge closure is "
                  "reported, not assumed"))
    say("M9 done")


# ===========================================================================
def main():
    print("=" * 78)
    print("v12 W6 -- RECORD CO-REFERENCE AND EFFECTIVE DESCENT")
    print("exact arithmetic: Q(zeta_8) and Q(cos pi/8); no floats")
    print("=" * 78)
    _, perms4, perms8 = step0()
    m1(perms4)
    m2(perms8)
    M = Composite()
    finals, inters = composite_charts(M)
    m3_m4_m7(M, finals, inters)
    m5(perms4)
    m6(perms8)
    m8(perms4)
    m9()

    hr("=")
    print("THE DESCENT TABLE")
    print("  vocabulary: FORCED |Phi|=1 / UNDERDETERMINED |Phi|>=2 / ABSENT")
    print("  |Phi|=0 / VACUOUS empty scope / NO-INSTRUMENT no measurement")
    hr("=")
    print("  %-28s %-38s %-42s %-38s" % ("model", "A (fact)", "B (event token)",
                                         "C (effective descent)"))
    hr()
    for row in TABLE:
        print("  %-28s %-38s %-42s %-38s" % row[:4])
        print("      %s" % row[4])
    hr()

    nfail = R.finish()
    sys.exit(1 if nfail else 0)


if __name__ == "__main__":
    main()
