#!/usr/bin/env python3
"""
w6_coreference_exact.py -- v12 W6: RECORD CO-REFERENCE AND EFFECTIVE DESCENT.

Runs the STEP-0 referent census, the three sub-problems (A: fact co-reference,
B: event-token co-reference, C: effective descent) and the six mandatory
controls of the pin (v12/note-w6-record-coreference-pin.md, commit 2efd05e),
plus three declared additions (M7 accidental agreement, M8 phase blindness,
M9 the descent-detector validation).

Substrate: exact arithmetic only.  Cyclotomic field Q(zeta_8) for the
dimension 4 and 8 models; the totally real quartic field Q(cos pi/8) for the
committed 36-configuration composite model.  No floats anywhere.

Committed instruments imported READ-ONLY from ../paper1_code:
  exact.py           the fields, born(), the Receipts harness
  sec4_records.py    h_avail / h_corr / merge_partition / support_of
  sec7_descent.py    the cut-coherence tensor and its counters
  model_composite.py the 36-configuration two-measurement two-frame model

ANCHOR rows reuse a number committed elsewhere in the corpus: a mismatch is a
corpus contradiction and exits 1.  GATE rows are W6's own measurements
pre-registered against the value this unit claims: a mismatch means the claim
is wrong and exits 1.  A substantive negative (a co-reference that fails, a
descent that does not obtain) is a RESULT, not a failure, and exits 0.
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
            if len(s) > 88:
                s = s[:85] + "..."
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
# PART 1 -- THE TYPED OBJECTS
#
#   Prov     provenance of a record token (W6-B's primitive)
#   Token    a chart-local stable record token: a partition of the chart's
#            configurations into value-labelled sectors, plus provenance,
#            plus its occurrence and availability status
#   Chart    a finite Barandes-style process (legs, initial configuration)
#            together with its declared record tokens and the joint law of
#            their ACTUAL values
#   Rec      the chart-local record algebra: the finite Boolean algebra on the
#            positive-probability value tuples, carried by Chart.law
# ===========================================================================
class Prov:
    """(generating interaction, local support, causal ancestry, copying
    lineage, erasure history).  Every field is read off the chart's declared
    leg list; nothing cross-chart enters."""

    def __init__(self, gen, support, anc, lineage, erased):
        self.gen = gen
        self.support = frozenset(support)
        self.anc = tuple(anc)
        self.lineage = tuple(lineage)
        self.erased = bool(erased)

    def key(self):
        return (self.gen, tuple(sorted(map(str, self.support))), self.anc,
                self.lineage, self.erased)

    def __repr__(self):
        return "Prov%s" % (self.key(),)


class Token:
    def __init__(self, tid, part, values, write_leg, prov):
        self.tid = tid              # the token's chart-local name
        self.part = list(part)      # configuration -> sector label
        self.values = dict(values)  # sector label -> declared record VALUE
        self.write_leg = write_leg  # index of the leg that writes it
        self.prov = prov
        self.occurred = None        # (H-corr) at the write leg
        self.avail = None           # (H-avail) under the declared later legs

    def __repr__(self):
        return "Token(%s)" % self.tid


class Chart:
    """a chart = one finite process + its declared record tokens."""

    def __init__(self, name, K, n, legs, j0, tokens, note=""):
        self.name = name
        self.K = K
        self.n = n
        self.legs = legs            # ordered list of exact matrices
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
        K, n = self.K, self.n
        pre = self._compose(self.legs[:t.write_leg + 1])
        t.occurred = h_corr(support_of(K, pre), n, t.part)
        post = self._compose(self.legs[t.write_leg + 1:])
        t.avail = t.occurred and h_avail(support_of(K, post), n, t.part)
        t.prov.erased = bool(t.occurred and not t.avail)

    def _compose(self, legs):
        K, n = self.K, self.n
        M = [[K.one if i == j else K.zero for j in range(n)] for i in range(n)]
        for L in legs:
            M = mat_mul(K, L, M)
        return M

    def final(self):
        return self._compose(self.legs)

    def dist(self, upto=None):
        """the exact distribution over configurations from j0, after `upto`
        legs (default: all of them)."""
        K = self.K
        T = self._compose(self.legs if upto is None else self.legs[:upto])
        return [K.mul(T[i][self.j0], K.conj(T[i][self.j0])) for i in range(self.n)]

    def _law(self):
        """the joint law of the tokens' values, ACTUAL values only, read at the
        time every token has been written.  Reading it at the FINAL time would
        be wrong for an erased token: after erasure the later dynamics have
        moved amplitude across the record sectors, so the final distribution is
        not the record's law.  For an available record the two times agree --
        that is what availability means -- so this choice changes nothing
        anywhere else."""
        K = self.K
        upto = max((t.write_leg for t in self.tokens), default=0) + 1
        p = self.dist(upto)
        out = {}
        for i in range(self.n):
            if K.is_zero(p[i]):
                continue
            key = tuple(t.values[t.part[i]] for t in self.tokens)
            out[key] = K.add(out.get(key, K.zero), p[i])
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

    def __repr__(self):
        return "Chart(%s)" % self.name


# --- a chart given directly by its record data (used for the 36-config model,
#     where the process is carried by the committed Composite class) ---------
class DataChart:
    def __init__(self, name, K, tokens, law, note=""):
        self.name = name
        self.K = K
        self.tokens = tokens
        self.law = law
        self.note = note

    marginal = Chart.marginal
    live = Chart.live

    def __repr__(self):
        return "Chart(%s)" % self.name


# ===========================================================================
# PART 2 -- PROCESS ISOMORPHISMS (what grounds a token label)
#
# A frame-isomorphism psi : b -> a is a bijection of configurations carrying
# b's initial configuration to a's, b's leg MULTISET to a's leg multiset under
# some matching (order is NOT preserved -- two frames of one experiment differ
# exactly by the order of two commuting legs, so order cannot be part of the
# invariant), and each of b's record partitions to one of a's.  It induces a
# token map tau.  W6-B admits exactly the token maps so induced: provenance,
# local support, ancestry, lineage and erasure history are then preserved
# automatically, because psi carries the whole generating structure.
# ===========================================================================
def perm_conj(K, L, p):
    """(P L P^-1)[p[i]][p[j]] = L[i][j]."""
    n = len(L)
    M = [[K.zero] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            M[p[i]][p[j]] = L[i][j]
    return M


def push_part(part, p):
    n = len(part)
    out = [None] * n
    for k in range(n):
        out[p[k]] = part[k]
    return out


def same_partition(pa, pb):
    """equality of partitions of the configuration set (sector names free)."""
    m = {}
    seen = {}
    for x, y in zip(pa, pb):
        if x in m and m[x] != y:
            return False
        if y in seen and seen[y] != x:
            return False
        m[x] = y
        seen[y] = x
    return True


def iso_token_maps(ca, cb, perms):
    """all token maps tau : cb.tokens -> ca.tokens induced by a
    frame-isomorphism cb -> ca, searched over the declared permutation scope
    `perms`.  Returns a set of tuples tau[i_b] = i_a."""
    K, n = ca.K, ca.n
    if cb.n != n or len(cb.legs) != len(ca.legs):
        return set()
    out = set()
    nl = len(ca.legs)
    for p in perms:
        if p[cb.j0] != ca.j0:
            continue
        conj = [perm_conj(K, L, p) for L in cb.legs]
        # match the leg multisets (order free)
        matched = False
        for sigma in itertools.permutations(range(nl)):
            if all(conj[t] == ca.legs[sigma[t]] for t in range(nl)):
                matched = True
                break
        if not matched:
            continue
        tau = {}
        ok = True
        for ib, tb in enumerate(cb.tokens):
            pushed = push_part(tb.part, p)
            hits = [ia for ia, ta in enumerate(ca.tokens)
                    if same_partition(pushed, ta.part)]
            if len(hits) != 1:
                ok = False
                break
            tau[ib] = hits[0]
        if ok and len(set(tau.values())) == len(tau) == len(ca.tokens):
            out.add(tuple(tau[i] for i in range(len(cb.tokens))))
    return out


def all_perms(n):
    return list(itertools.permutations(range(n)))


# ===========================================================================
# PART 3 -- THE PRESERVATION LIST AND THE PHI SETS
#
#   1 Boolean operations      -- automatic for a value-preserving token map
#   2 definite record values  -- values are declared data carried by the token
#   3 probabilities on the shared algebra -- exact equality of the marginals
#   4 persistence/availability
#   5 provenance              -- level B only, via a frame-isomorphism
#   6 original vs copy        -- level B only, ditto
#
# PHASE IS NOT ON THE LIST.  No item consults an amplitude phase or any phase
# invariant; the record-descent limit (W7-4 sec 23) makes that a category error.
# ===========================================================================
def phi_set(ca, cb, level, scope="available", perms=None):
    """all admissible partial co-reference maps phi_ab : R_b -> R_a, presented
    as token bijections tau (index of b -> index of a)."""
    K = ca.K
    ta = ca.live(scope)
    tb = cb.live(scope)
    if len(ta) != len(tb):
        return []
    isos = None
    if level == "B":
        isos = iso_token_maps(ca, cb, perms)
    out = []
    for perm in itertools.permutations(ta):
        tau = {tb[i]: perm[i] for i in range(len(tb))}
        # item 2: definite record values (as sets, per matched token)
        if any(sorted(map(str, cb.tokens[b].values.values()))
               != sorted(map(str, ca.tokens[a].values.values()))
               for b, a in tau.items()):
            continue
        # item 4: availability
        if any(cb.tokens[b].avail != ca.tokens[a].avail for b, a in tau.items()):
            continue
        # item 3: probabilities on the shared algebra, value-matched
        mb = cb.marginal(tb)
        ma = ca.marginal([tau[b] for b in tb])
        if len(mb) != len(ma):
            continue
        good = True
        for key, v in mb.items():
            if ma.get(key) != v:
                good = False
                break
        if not good:
            continue
        # items 5, 6: provenance and lineage, via a frame-isomorphism
        if level == "B":
            full = tuple(tau[i] for i in range(len(cb.tokens))) \
                if len(tau) == len(cb.tokens) else None
            if full is None or full not in isos:
                continue
        out.append(tuple(sorted(tau.items())))
    return out


def route_ext(K, joint):
    """ROUTE-EXT: in a declared common record-preserving extension, are the two
    record variables perfectly correlated ALONG THE IDENTITY OF VALUES?  The
    joint law must be supported on the graph of a value-preserving bijection."""
    pos = [(x, y) for (x, y), v in joint.items() if not K.is_zero(v)]
    fwd, bwd = {}, {}
    for x, y in pos:
        if fwd.setdefault(x, y) != y or bwd.setdefault(y, x) != x:
            return (False, len(pos), False)
    bij = len(fwd) == len(bwd) == len(pos)
    ident = all(x == y for x, y in pos)
    return (bij and ident, len(pos), bij)


# ===========================================================================
# PART 4 -- THE DESCENT SOLVER (W6-C)
#
# coherence laws: phi_aa = id; phi_ba = phi_ab^-1; phi_ab o phi_bc = phi_ac on
# triple overlaps, modulo the DECLARED gauge only (the declared gauge is
# configuration relabelling, which acts trivially on the record algebra -- see
# the M1 control -- so the triple law is judged on the nose).
# ===========================================================================
def compose(tau_ab, tau_bc):
    return {c: tau_ab[b] for c, b in tau_bc.items() if b in tau_ab}


def invert(tau):
    return {v: k for k, v in tau.items()}


def descent(names, phis, auts):
    """phis[(a,b)] = list of tau dicts (b -> a); auts[a] = list of tau dicts
    (a -> a).  Returns a verdict dict."""
    edges = sorted({tuple(sorted(k)) for k in phis})
    fams = []
    choices = [phis[(x, y)] for (x, y) in edges]
    if any(len(c) == 0 for c in choices):
        return dict(verdict="ABSENT-PAIR", families=0, orbits=0,
                    edges=len(edges), triples=0, transitive=None)
    ntrip = 0
    for pick in itertools.product(*choices):
        fam = {}
        for (x, y), tau in zip(edges, pick):
            fam[(x, y)] = dict(tau)
            fam[(y, x)] = invert(dict(tau))
        ok = True
        cnt = 0
        for a, b, c in itertools.permutations(names, 3):
            if (a, b) in fam and (b, c) in fam and (a, c) in fam:
                cnt += 1
                comp = compose(fam[(a, b)], fam[(b, c)])
                direct = fam[(a, c)]
                for k, v in comp.items():
                    if direct.get(k) != v:
                        ok = False
                        break
            if not ok:
                break
        ntrip = max(ntrip, cnt)
        if ok:
            fams.append(fam)
    if not fams:
        return dict(verdict="NO-DESCENT", families=0, orbits=0,
                    edges=len(edges), triples=ntrip, transitive=False)
    # the gauge action of the automorphism groups
    keys = [tuple(sorted((k, tuple(sorted(v.items()))) for k, v in f.items()))
            for f in fams]
    index = {k: i for i, k in enumerate(keys)}
    seen = set()
    orbits = 0
    for i, f in enumerate(fams):
        if i in seen:
            continue
        orbits += 1
        stack = [i]
        seen.add(i)
        while stack:
            cur = fams[stack.pop()]
            for g in itertools.product(*[auts[nm] for nm in names]):
                gm = dict(zip(names, [dict(x) for x in g]))
                new = {}
                for (x, y), tau in cur.items():
                    ginv = invert(gm[y])          # tokens of y -> tokens of y
                    new[(x, y)] = {t: gm[x][tau[ginv[t]]]
                                   for t in ginv if ginv[t] in tau}
                kk = tuple(sorted((k, tuple(sorted(v.items())))
                                  for k, v in new.items()))
                if kk in index and index[kk] not in seen:
                    seen.add(index[kk])
                    stack.append(index[kk])
    trivial_aut = all(len(auts[nm]) == 1 for nm in names)
    if len(fams) == 1 and trivial_aut:
        v = "SET-AMALGAM"
    elif orbits == 1 and not trivial_aut:
        v = "GROUPOID-AMALGAM"
    elif orbits == 1:
        v = "SET-AMALGAM"
    else:
        v = "UNDERDETERMINED"
    return dict(verdict=v, families=len(fams), orbits=orbits,
                edges=len(edges), triples=ntrip, transitive=(orbits == 1))


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


# ===========================================================================
# PART 5 -- THE COMMON MATERIAL (dimension 4 and 8, Q(zeta_8))
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


# ===========================================================================
# STEP 0 -- THE REFERENT CENSUS (the computational half; the four gates are
# written out in the note)
# ===========================================================================
def step0():
    hr()
    print("STEP 0 -- THE REFERENT CENSUS")
    hr()

    # -- object 1: the chart-local stable record algebra ---------------------
    # located: sec4_records.py:48 (h_avail), :53 (h_corr), :62 (merge_partition)
    # the record structure is a label list k -> part[k]; the algebra is the
    # Boolean algebra on its ACTUAL value tuples.
    U1 = mat_mul(K8, CNOT, kron(K8, H, I2))
    U2 = kron(K8, H, I2)
    part = [0, 1, 0, 1]
    S1, S2 = support_of(K8, U1), support_of(K8, U2)
    R.anchor("census/record H-corr  [sec4_records.py:198]",
             h_corr(S1, 4, part), True)
    R.anchor("census/record H-avail [sec4_records.py:199]",
             h_avail(S2, 4, part), True)

    tok = Token("R", part, {0: "0", 1: "1"}, 0,
                Prov("CX", {"q0", "q1"}, ("PREP-H",), ("original",), False))
    ch = Chart("census", K8, 4, [U1, U2], 0, [tok])
    R.gate("census/record algebra atoms", sorted(ch.law), [("0",), ("1",)])
    R.gate("census/record algebra law",
           [str(K8.to_rat(ch.law[k])) for k in sorted(ch.law)], ["1/2", "1/2"])
    R.gate("census/record occurred", ch.tokens[0].occurred, True)
    R.gate("census/record available", ch.tokens[0].avail, True)
    say("object 1: chart-local record algebra R_a -- LOCATED and typed")

    # -- object 6: the insertion-vs-co-reference discriminator ---------------
    # |Phi| is the discriminator: 1 = forced (genuine), >=2 = any named map is
    # inserted, 0 = absent.  Exhibited on the census chart against itself.
    perms4 = all_perms(4)
    self_iso = iso_token_maps(ch, ch, perms4)
    R.gate("census/self-isomorphisms of the census chart", len(self_iso), 1)
    R.gate("census/Phi(a,a) at level B", len(phi_set(ch, ch, "B", perms=perms4)), 1)
    say("object 6: the discriminator |Phi| -- CONSTRUCTED")
    return ch


# ===========================================================================
# M1 -- RELABELLED SAME RECORD (co-reference MUST succeed)
# ===========================================================================
def m1():
    hr()
    print("M1 -- RELABELLED SAME RECORD  (control 1)")
    hr()
    U1 = mat_mul(K8, CNOT, kron(K8, H, I2))
    U2 = kron(K8, H, I2)
    part = [0, 1, 0, 1]
    perms4 = all_perms(4)

    def build(name, p):
        legs = [perm_conj(K8, U1, p), perm_conj(K8, U2, p)]
        tok = Token("R", push_part(part, p), {0: "0", 1: "1"}, 0,
                    Prov("CX", {"q0", "q1"}, ("PREP-H",), ("original",), False))
        return Chart(name, K8, 4, legs, p[0], [tok])

    pid = (0, 1, 2, 3)
    p1 = (1, 2, 3, 0)
    p2 = (2, 3, 0, 1)
    a, b, c = build("a", pid), build("b", p1), build("c", p2)

    # the declared gauge (configuration relabelling) acts trivially on the
    # record algebra: that is why control 1 must succeed.
    R.gate("M1/law invariant under relabelling",
           (a.law == b.law, a.law == c.law), (True, True))
    R.gate("M1/legs actually differ",
           (a.legs != b.legs, a.legs != c.legs), (True, True))
    nA = len(phi_set(a, b, "A"))
    nB = len(phi_set(a, b, "B", perms=perms4))
    R.gate("M1/|Phi_A| a<-b", nA, 1)
    R.gate("M1/|Phi_B| a<-b", nB, 1)

    # ROUTE-EXT: the common extension is the one process; the joint law of the
    # two presentations' record variables is the graph of the identity on values
    K = K8
    joint = {}
    for i in range(4):
        pv = a.dist()[i]
        if K.is_zero(pv):
            continue
        key = (a.tokens[0].values[a.tokens[0].part[i]],
               b.tokens[0].values[b.tokens[0].part[p1[i]]])
        joint[key] = K.add(joint.get(key, K.zero), pv)
    ok, npos, bij = route_ext(K, joint)
    R.gate("M1/ROUTE-EXT perfect value-correlation", (ok, npos, bij),
           (True, 2, True))

    names = ["a", "b", "c"]
    charts = {"a": a, "b": b, "c": c}
    phis, auts = {}, {}
    for x, y in itertools.permutations(names, 2):
        phis[(x, y)] = [dict(t) for t in
                        phi_set(charts[x], charts[y], "B", perms=perms4)]
    for x in names:
        auts[x] = [dict(t) for t in
                   phi_set(charts[x], charts[x], "B", perms=perms4)]
    # soundness of the solver: the preservation list is symmetric, so the
    # coherence law phi_ba = phi_ab^-1 uses only admissible maps; and the
    # identity is always an automorphism.
    R.gate("M1/Phi sets inverse-closed",
           all(tuple(sorted(invert(dict(t)).items())) in
               [tuple(sorted(dict(u).items()))
                for u in phi_set(charts[y], charts[x], "B", perms=perms4)]
               for x, y in itertools.permutations(names, 2)
               for t in phi_set(charts[x], charts[y], "B", perms=perms4)), True)
    R.gate("M1/identity is in every Aut set",
           all({i: i for i in range(len(charts[x].tokens))}
               in [dict(t) for t in
                   phi_set(charts[x], charts[x], "B", perms=perms4)]
               for x in names), True)
    d = descent(names, phis, auts)
    sz, inj = amalgam(names, charts, {k: v[0] for k, v in phis.items()})
    R.gate("M1/descent verdict", d["verdict"], "SET-AMALGAM")
    R.gate("M1/coherent families, orbits", (d["families"], d["orbits"]), (1, 1))
    R.gate("M1/triples tested per family", d["triples"], 6)
    R.gate("M1/amalgam size, injective", (sz, inj), (1, True))
    TABLE.append(("M1 relabelled same record", "SUCCEEDS-FORCED",
                  "SUCCEEDS-FORCED", "SET-AMALGAM",
                  "gauge acts trivially on the record algebra"))
    say("M1 done")


# ===========================================================================
# M2 -- REDUNDANT COPIES (A succeeds, B fails)
# ===========================================================================
def m2():
    hr()
    print("M2 -- REDUNDANT COPIES  (control 2)")
    hr()
    L1 = mat_mul(K8, cnot3(0, 1), h3(0))     # writes copy 1
    L2 = cnot3(0, 2)                         # writes copy 2, later
    p1 = bit_part(8, 1, 3)
    p2 = bit_part(8, 2, 3)
    provA = Prov("CX1", {"q0", "q1"}, ("PREP-H",), ("original",), False)
    provB = Prov("CX2", {"q0", "q2"}, ("PREP-H", "CX1"), ("copy-of", "CX1"),
                 False)
    a = Chart("a", K8, 8, [L1, L2], 0,
              [Token("R1", p1, {0: "0", 1: "1"}, 0, provA)])
    b = Chart("b", K8, 8, [L1, L2], 0,
              [Token("R2", p2, {0: "0", 1: "1"}, 1, provB)])
    R.gate("M2/both tokens occurred",
           (a.tokens[0].occurred, b.tokens[0].occurred), (True, True))
    R.gate("M2/both tokens available",
           (a.tokens[0].avail, b.tokens[0].avail), (True, True))
    R.gate("M2/identical record laws", a.law == b.law, True)

    perms8 = all_perms(8)
    t0 = time.time()
    nA = len(phi_set(a, b, "A"))
    nB = len(phi_set(a, b, "B", perms=perms8))
    say("M2 isomorphism search over 8! permutations  %.1fs" % (time.time() - t0))
    R.gate("M2/|Phi_A| a<-b", nA, 1)
    R.gate("M2/|Phi_B| a<-b", nB, 0)
    # POSITIVE CONTROL: the search is not vacuously empty -- it finds the
    # identity on each chart against itself.  And the zero is caused by the LEG
    # structure specifically: the swap of the two copy registers DOES carry the
    # second copy's partition onto the first's, but does NOT fix the leg
    # multiset, so no frame-isomorphism exists.
    R.gate("M2/positive control: iso(a,a), iso(b,b)",
           (len(iso_token_maps(a, a, perms8)), len(iso_token_maps(b, b, perms8))),
           (1, 1))
    sg = [0] * 8
    for j in range(8):
        bb = [(j >> (2 - t)) & 1 for t in range(3)]
        bb[1], bb[2] = bb[2], bb[1]
        sg[j] = (bb[0] << 2) | (bb[1] << 1) | bb[2]
    R.gate("M2/the swap carries R2's partition onto R1's",
           same_partition(push_part(p2, sg), p1), True)
    R.gate("M2/but the swap does not fix the leg multiset",
           perm_conj(K8, L1, sg) in (L1, L2), False)

    # ROUTE-EXT on the ONE process carrying both tokens
    K = K8
    joint = {}
    full = Chart("ab", K8, 8, [L1, L2], 0,
                 [Token("R1", p1, {0: "0", 1: "1"}, 0, provA),
                  Token("R2", p2, {0: "0", 1: "1"}, 1, provB)])
    for key, v in full.law.items():
        joint[key] = K.add(joint.get(key, K.zero), v)
    ok, npos, bij = route_ext(K, joint)
    R.gate("M2/ROUTE-EXT perfect value-correlation", (ok, npos, bij),
           (True, 2, True))
    # the provenance data that separate the tokens
    R.gate("M2/provenance differs",
           full.tokens[0].prov.key() != full.tokens[1].prov.key(), True)
    R.gate("M2/lineage original vs copy",
           (full.tokens[0].prov.lineage, full.tokens[1].prov.lineage),
           (("original",), ("copy-of", "CX1")))

    # C: the fact algebra over {a, b, a-relabelled}
    p = tuple([0, 1, 2, 3, 4, 5, 6, 7][::-1])
    ar = Chart("c", K8, 8, [perm_conj(K8, L1, p), perm_conj(K8, L2, p)], p[0],
               [Token("R1", push_part(p1, p), {0: "0", 1: "1"}, 0, provA)])
    names = ["a", "b", "c"]
    charts = {"a": a, "b": b, "c": ar}
    phis = {(x, y): [dict(t) for t in phi_set(charts[x], charts[y], "A")]
            for x, y in itertools.permutations(names, 2)}
    auts = {x: [dict(t) for t in phi_set(charts[x], charts[x], "A")]
            for x in names}
    d = descent(names, phis, auts)
    R.gate("M2/fact-level descent verdict", d["verdict"], "SET-AMALGAM")

    # -- ROUTE-WIT: the pin's second route, a specified common-record witness.
    #    Four qubits: three copies of one alternative.  t3 is the witness that
    #    identifies t1 with t2.
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
                     ("original",) if t == 1 else ("copy-of", "CX1"), False))
          for t in (1, 2, 3)]
    W = Chart("wit", K8, 16, [Lw], 0, wt)
    R.gate("M2/witness model joint law", sorted(W.law),
           [("0", "0", "0"), ("1", "1", "1")])
    j13 = {}
    j23 = {}
    for key, v in W.law.items():
        j13[(key[0], key[2])] = K8.add(j13.get((key[0], key[2]), K8.zero), v)
        j23[(key[1], key[2])] = K8.add(j23.get((key[1], key[2]), K8.zero), v)
    R.gate("M2/ROUTE-WIT t1 vs witness", route_ext(K8, j13), (True, 2, True))
    R.gate("M2/ROUTE-WIT t2 vs witness", route_ext(K8, j23), (True, 2, True))
    R.gate("M2/witness identifies t1 with t2",
           route_ext(K8, j13)[0] and route_ext(K8, j23)[0], True)

    TABLE.append(("M2 redundant copies", "SUCCEEDS-FORCED", "FAILS-ABSENT",
                  "SET-AMALGAM (fact level); token level has no edges",
                  "one fact, two tokens: exactly the pin's demand"))
    say("M2 done")


# ===========================================================================
# the committed 36-configuration composite model (M3, M4, M7)
# ===========================================================================
POINTER = {1: "+", 2: "-"}


def composite_charts(M):
    """the twelve committed charts (6 settings x 2 frames) at the FINAL record,
    and the twelve at the INTERMEDIATE slice."""
    K = M.K
    finals, inters, legs = {}, {}, {}
    for sp in SETTING_ORDER:
        a8, b8 = SETTINGS[sp]
        for fr in ("F1", "F2"):
            L1, L2, L3 = M.legs(sp, fr)
            legs[(sp, fr)] = (L1, L2, L3)
            provA = Prov("MEAS-A@%d" % a8, {"qA", "pA"}, ("PREP",),
                         ("original",), False)
            provB = Prov("MEAS-B@%d" % b8, {"qB", "pB"}, ("PREP",),
                         ("original",), False)
            tA = Token("R_A", [], {}, 1, provA)
            tB = Token("R_B", [], {}, 2, provB)
            tA.values = {1: "+", 2: "-"}
            tB.values = {1: "+", 2: "-"}
            tA.occurred = tB.occurred = True
            tA.avail = tB.avail = True
            law = {}
            for (pa, pb), v in M.outcome_law(sp, fr).items():
                if K.is_zero(v):
                    continue
                law[(POINTER[pa], POINTER[pb])] = v
            finals[(sp, fr)] = DataChart("%s/%s" % (sp, fr), K, [tA, tB], law)
            # the intermediate slice: only the wing measured by leg 2
            T1, T2, T3, _ = M.propagators(sp, fr)
            col = {}
            for (i, j), v in T2.items():
                if j == 0:
                    col[i] = K.add(col.get(i, K.zero), K.mul(v, v))
            wing = "A" if fr == "F1" else "B"
            tok = Token("R_%s" % wing, [], {1: "+", 2: "-"}, 1,
                        provA if wing == "A" else provB)
            tok.tid = "R_%s" % wing
            tok.occurred = True
            tok.avail = True
            ilaw = {}
            for i, v in col.items():
                qa, qb, pa, pb = unidx(i)
                ptr = pa if wing == "A" else pb
                if ptr == 0:
                    continue
                key = (POINTER[ptr],)
                ilaw[key] = K.add(ilaw.get(key, K.zero), v)
            inters[(sp, fr)] = DataChart("%s/%s@t2" % (sp, fr), K, [tok], ilaw)
    return finals, inters, legs


def m3_m4_m7(M):
    hr()
    print("M3 / M4 / M7 -- THE COMMITTED TWO-FRAME BELL STRUCTURE")
    hr()
    K = M.K
    finals, inters, legs = composite_charts(M)
    say("twelve committed charts built")

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

    # the two frames share the FINAL propagator exactly
    same_T3 = all(M.propagators(sp, "F1")[2] == M.propagators(sp, "F2")[2]
                  for sp in SETTING_ORDER)
    R.gate("M3/T3 identical in both frames, all settings", same_T3, True)
    diffs = []
    for sp in SETTING_ORDER:
        t2a = M.propagators(sp, "F1")[1]
        t2b = M.propagators(sp, "F2")[1]
        ks = set(t2a) | set(t2b)
        diffs.append(sum(1 for k in ks
                         if t2a.get(k, K.zero) != t2b.get(k, K.zero)))
    R.gate("M3/intermediate propagators differ, per setting", diffs,
           [270, 270, 432, 432, 108, 432])
    R.gate("M3/every setting's intermediate slices differ",
           all(d > 0 for d in diffs), True)
    say("frame structure measured")

    # -- M3: fact-candidate matching vs law agreement -----------------------
    keys = sorted(finals)
    lawclass = {}
    for k in keys:
        sig = tuple(sorted((kk, vv) for kk, vv in finals[k].law.items()))
        lawclass.setdefault(sig, []).append(k)
    R.gate("M3/final-law classes", sorted(len(v) for v in lawclass.values()),
           [2, 4, 6])
    agree = cand = 0
    for x, y in itertools.product(keys, repeat=2):
        same = finals[x].law == finals[y].law
        n = len(phi_set(finals[x], finals[y], "A"))
        agree += 1 if same else 0
        cand += 1 if n > 0 else 0
        if same != (n > 0):
            R.gate("M3/BICONDITIONAL BROKEN at %s,%s" % (x, y), same, n > 0)
    R.gate("M3/ordered pairs with agreeing final laws", agree, 56)
    R.gate("M3/ordered pairs admitting a fact-candidate map", cand, 56)
    counts = {len(phi_set(finals[x], finals[y], "A"))
              for x, y in itertools.product(keys, repeat=2)
              if finals[x].law == finals[y].law}
    R.gate("M3/|Phi_A| on every law-agreeing pair", sorted(counts), [2])
    say("M3 fact level measured: 56 agreeing pairs, |Phi_A| = 2 on each")

    # -- M3 at level B: frame-isomorphisms of the committed model ------------
    # declared permutation scope: the wing exchange, composed with the pointer
    # 3-cycles on each wing and the two qubit flips (72 declared permutations).
    def build_perm(swap, sa, sb, fa, fb):
        sh = {0: 1, 1: 2, 2: 0}

        def shift(v, t):
            for _ in range(t):
                v = sh[v]
            return v
        p = [0] * NC
        for i in range(NC):
            qa, qb, pa, pb = unidx(i)
            qa2, qb2 = (qa ^ fa), (qb ^ fb)
            pa2, pb2 = shift(pa, sa), shift(pb, sb)
            p[i] = idx(qb2, qa2, pb2, pa2) if swap else idx(qa2, qb2, pa2, pb2)
        return p

    scope = [build_perm(sw, sa, sb, fa, fb)
             for sw in (0, 1) for sa in range(3) for sb in range(3)
             for fa in (0, 1) for fb in (0, 1)]
    R.gate("M3/declared permutation scope size", len(scope), 72)

    def sp_conj(L, p):
        return {(p[i], p[j]): v for (i, j), v in L.items()}

    def frame_isos(x, y, level):
        """token maps induced by a frame-isomorphism y -> x, over the declared
        scope; `level` in {'amplitude','born'}."""
        Lx = legs[x]
        Ly = legs[y]
        out = set()
        for p in scope:
            if p[0] != 0:
                continue
            cy = [sp_conj(L, p) for L in Ly]
            if level == "born":
                cy = [M.born_sparse(L) for L in cy]
                tgt = [M.born_sparse(L) for L in Lx]
            else:
                tgt = list(Lx)
            hit = None
            for sg in itertools.permutations(range(3)):
                if all(cy[t] == tgt[sg[t]] for t in range(3)):
                    hit = sg
                    break
            if hit is None:
                continue
            # the induced token map: the wing exchange swaps R_A and R_B
            swapped = (unidx(p[idx(0, 0, 1, 0)])[3] == 1)
            out.add(((0, 1), (1, 0))[swapped])
        return out

    amp_iso, born_iso = {}, {}
    for sp in SETTING_ORDER:
        x, y = (sp, "F1"), (sp, "F2")
        amp_iso[sp] = frame_isos(x, y, "amplitude")
        born_iso[sp] = frame_isos(x, y, "born")
    R.gate("M3/amplitude-level frame-isomorphism token maps, per setting",
           [sorted(amp_iso[sp]) for sp in SETTING_ORDER], [[(0, 1)]] * 6)
    R.gate("M3/born-level frame-isomorphism token maps, per setting",
           [sorted(born_iso[sp]) for sp in SETTING_ORDER], [[(0, 1)]] * 6)
    say("M3 frame-isomorphisms measured (amplitude and Born levels)")

    # -- level B on the committed model: the A-level maps that a
    #    frame-isomorphism induces.  The wing exchange is NOT one of them.
    nB = {}
    for sp in SETTING_ORDER:
        x, y = (sp, "F1"), (sp, "F2")
        cands = phi_set(finals[x], finals[y], "A")
        keep = []
        for t in cands:
            tau = dict(t)
            full = tuple(tau[i] for i in range(2))
            if full in amp_iso[sp]:
                keep.append(t)
        nB[sp] = len(keep)
    R.gate("M3/|Phi_B| F1<-F2, per setting",
           [nB[sp] for sp in SETTING_ORDER], [1] * 6)

    # the leg matching must be ORDER-FREE: two frames of one experiment differ
    # exactly by the order of two commuting legs.  If order were required, the
    # committed model would have no frame-isomorphism at all.
    ordered = []
    for sp in SETTING_ORDER:
        Lx, Ly = legs[(sp, "F1")], legs[(sp, "F2")]
        ordered.append(sum(1 for p in scope if p[0] == 0
                           and all(sp_conj(Ly[t], p) == Lx[t] for t in range(3))))
    R.gate("M3/frame-isomorphisms if leg ORDER were required", ordered, [0] * 6)
    R.gate("M3/|Phi_A| exceeds |Phi_B| at every setting",
           all(len(phi_set(finals[(sp, "F1")], finals[(sp, "F2")], "A"))
               == 2 and nB[sp] == 1 for sp in SETTING_ORDER), True)

    # -- the token-overlap graph on the twelve committed charts, MEASURED ----
    t0 = time.time()
    edgesB = 0
    cross = 0
    adj = {x: set() for x in keys}
    for x, y in itertools.product(keys, repeat=2):
        if frame_isos(x, y, "amplitude"):
            edgesB += 1
            adj[x].add(y)
            if x[0] != y[0]:
                cross += 1
    say("token-overlap graph measured over 144 ordered pairs  %.1fs"
        % (time.time() - t0))
    R.gate("M3/ordered pairs admitting a frame-isomorphism", edgesB, 24)
    R.gate("M3/cross-setting pairs admitting one", cross, 0)
    comps = {}
    for x in keys:
        comps.setdefault(x[0], []).append(x)
    R.gate("M3/token-overlap graph: components and their sizes",
           (len(comps), sorted({len(v) for v in comps.values()})), (6, [2]))
    R.gate("M3/committed charts in a nonvacuous triple overlap",
           sum(1 for c in comps.values() if len(c) >= 3), 0)

    # -- the preservation list BITES: each item rejects some candidate -------
    R.gate("M3/list item 3 (probabilities) bites: SP-A <- SP-B",
           len(phi_set(finals[("SP-A", "F1")], finals[("SP-B", "F1")], "A")), 0)
    R.gate("M3/list item 1 (Boolean/atom count) bites: SP-A <- SP-E",
           (len(finals[("SP-A", "F1")].law), len(finals[("SP-E", "F1")].law),
            len(phi_set(finals[("SP-A", "F1")], finals[("SP-E", "F1")], "A"))),
           (4, 2, 0))

    # -- WHICH LAYER GROUNDS THE WING LABELLING (disclosure) -----------------
    w = [0] * NC
    for i in range(NC):
        qa, qb, pa, pb = unidx(i)
        w[i] = idx(qb, qa, pb, pa)

    def col_of(T, sq):
        d = {}
        for (i, j), v in T.items():
            if j == 0 and not K.is_zero(v):
                d[i] = K.mul(v, v) if sq else v
        return d
    layer = []
    for sp in SETTING_ORDER:
        Ta = M.propagators(sp, "F1")[:3]
        Tb = M.propagators(sp, "F2")[:3]
        amp = all({w[i]: v for i, v in col_of(tb, False).items()}
                  == col_of(ta, False) for ta, tb in zip(Ta, Tb))
        bor = all({w[i]: v for i, v in col_of(tb, True).items()}
                  == col_of(ta, True) for ta, tb in zip(Ta, Tb))
        law = finals[(sp, "F1")].law
        sym = all(law.get((x, y)) == law.get((y, x))
                  for x in ("+", "-") for y in ("+", "-"))
        layer.append((amp, bor, sym))
    R.gate("M3/wing swap on (amplitude j0 history, Born j0 history, final law)",
           layer, [(False, False, True), (False, False, True),
                   (False, False, True), (False, False, True),
                   (False, True, True), (False, True, True)])
    R.gate("M3/settings whose whole Born j0 history is wing-swap symmetric",
           [sp for sp, L in zip(SETTING_ORDER, layer) if L[1]],
           ["SP-E", "SP-F"])
    R.gate("M3/final law is wing-swap symmetric at every setting",
           all(L[2] for L in layer), True)
    say("M3 layer analysis measured (what grounds the wing labelling)")

    # -- M3 ROUTE-EXT: same-setting frames vs accidental agreement (M7) ------
    # the common extension is the ONE process: read each final configuration
    # through F1's record map and through F2's, and compare configuration by
    # configuration.  The certificate rests on a measured fact -- the two
    # frames assign every final configuration the same probability.
    sp = "SP-A"
    T3a = M.propagators(sp, "F1")[2]
    T3b = M.propagators(sp, "F2")[2]
    joint = {}
    agreecfg = 0
    for i in range(NC):
        va = T3a.get((i, 0), K.zero)
        vb = T3b.get((i, 0), K.zero)
        pa, pb = K.mul(va, va), K.mul(vb, vb)
        if pa != pb:
            continue
        agreecfg += 1
        if K.is_zero(pa):
            continue
        _, _, ppa, ppb = unidx(i)
        if ppa == 0 or ppb == 0:
            continue
        key = ((POINTER[ppa], POINTER[ppb]), (POINTER[ppa], POINTER[ppb]))
        joint[key] = K.add(joint.get(key, K.zero), pa)
    R.gate("M3/final configurations given equal probability by both frames",
           agreecfg, 36)
    ok, npos, bij = route_ext(K, joint)
    R.gate("M3/ROUTE-EXT same-setting frames", (ok, npos, bij), (True, 4, True))

    # M7: SP-A and SP-C have the same final law and DIFFERENT settings; the
    # only available common extension is the product of two independent runs
    xa, xc = ("SP-A", "F1"), ("SP-C", "F1")
    R.gate("M7/SP-A and SP-C final laws agree", finals[xa].law == finals[xc].law,
           True)
    R.gate("M7/SP-A and SP-C are different settings",
           SETTINGS["SP-A"] != SETTINGS["SP-C"], True)
    prod = {}
    for k1, v1 in finals[xa].law.items():
        for k2, v2 in finals[xc].law.items():
            prod[(k1, k2)] = K.mul(v1, v2)
    ok7, npos7, bij7 = route_ext(K, prod)
    R.gate("M7/ROUTE-EXT on the product extension", (ok7, bij7), (False, False))
    R.gate("M7/positive entries in the product joint law", npos7, 16)
    R.gate("M7/|Phi_A| SP-A <- SP-C", len(phi_set(finals[xa], finals[xc], "A")), 2)
    say("M7 accidental agreement measured inside the committed model")

    # -- M4: the intermediate slice -----------------------------------------
    for sp in SETTING_ORDER:
        x, y = (sp, "F1"), (sp, "F2")
        nA = len(phi_set(inters[x], inters[y], "A"))
        R.gate("M4/|Phi_A-candidate| intermediate %s" % sp, nA, 1)
    R.gate("M4/intermediate marginals both uniform",
           all(sorted(str(K.to_rat(v)) if K.to_rat(v) is not None else str(v)
                      for v in inters[(sp, fr)].law.values()) == ["1/2", "1/2"]
               for sp in SETTING_ORDER for fr in ("F1", "F2")), True)
    # the overlap datum at t=2: F1 has written {PREP, MEAS-A}, F2 {PREP, MEAS-B}
    shared = {"PREP"}
    forced = []
    for sp in SETTING_ORDER:
        x, y = (sp, "F1"), (sp, "F2")
        # a token is in the overlap subalgebra iff its whole provenance is shared
        ov_a = [t for t in inters[x].tokens
                if {t.prov.gen} | set(t.prov.anc) <= shared]
        ov_b = [t for t in inters[y].tokens
                if {t.prov.gen} | set(t.prov.anc) <= shared]
        forced.append((len(ov_a), len(ov_b)))
    R.gate("M4/overlap subalgebra at the intermediate slice is trivial",
           set(forced), {(0, 0)})
    # ROUTE-EXT at the final time, where both pointers exist: the joint law of
    # A's and B's outcomes is NOT the graph of a value-preserving bijection
    ext = {}
    for (al, be), v in finals[("SP-A", "F1")].law.items():
        ext[(al, be)] = v
    ok4, npos4, bij4 = route_ext(K, ext)
    R.gate("M4/ROUTE-EXT A-outcome vs B-outcome at SP-A", (ok4, npos4, bij4),
           (False, 4, False))
    extE = {}
    for (al, be), v in finals[("SP-E", "F1")].law.items():
        extE[(al, be)] = v
    okE, nposE, bijE = route_ext(K, extE)
    R.gate("M4/ROUTE-EXT at SP-E: bijection-supported but value-reversing",
           (okE, nposE, bijE), (False, 2, True))
    say("M4 intermediate content measured")

    # -- the reachable-subprocess control: is the grounding an artifact of
    #    U_prep's arbitrary orthogonal completion?  Restrict every leg to the
    #    configurations reachable from j0 and re-run the search.
    reach_iso = []
    for sp in SETTING_ORDER:
        reach = {0}
        for fr in ("F1", "F2"):
            for T in M.propagators(sp, fr)[:3]:
                for (i, j), v in T.items():
                    if j == 0 and not K.is_zero(v):
                        reach.add(i)
        rs = set(reach)

        def restrict(L):
            return {(i, j): v for (i, j), v in L.items()
                    if i in rs and j in rs and not K.is_zero(v)}
        La = [restrict(L) for L in legs[(sp, "F1")]]
        Lb = [restrict(L) for L in legs[(sp, "F2")]]
        hits = 0
        for p in scope:
            if p[0] != 0 or sorted(p[i] for i in reach) != sorted(reach):
                continue
            cy = [{(p[i], p[j]): v for (i, j), v in L.items()} for L in Lb]
            for sg in itertools.permutations(range(3)):
                if all(cy[t] == La[sg[t]] for t in range(3)):
                    hits += 1
                    break
        reach_iso.append((len(reach), hits))
    R.gate("M3/reachable-subprocess isomorphisms (size, count) per setting",
           reach_iso, [(21, 1), (21, 1), (35, 1), (35, 1), (9, 1), (27, 1)])

    # -- M3 descent over a committed triple ---------------------------------
    # the third chart is F2 under a configuration relabelling: the declared
    # gauge acts trivially on the record algebra, so its record data are F2's.
    sp = "SP-A"
    names = ["F1", "F2", "F2r"]
    charts = {"F1": finals[(sp, "F1")], "F2": finals[(sp, "F2")],
              "F2r": finals[(sp, "F2")]}
    phis, auts = {}, {}
    for u, v in itertools.permutations(names, 2):
        phis[(u, v)] = [dict(t) for t in phi_set(charts[u], charts[v], "A")]
    for u in names:
        auts[u] = [dict(t) for t in phi_set(charts[u], charts[u], "A")]
    d = descent(names, phis, auts)
    R.gate("M3/fact-level descent over a committed triple", d["verdict"],
           "GROUPOID-AMALGAM")
    R.gate("M3/fact-level coherent families, orbits",
           (d["families"], d["orbits"]), (4, 1))
    # the same triple at level B: only the isomorphism-induced map survives
    idmap = {0: 0, 1: 1}
    phisB = {k: [dict(idmap)] for k in phis}
    autsB = {u: [dict(idmap)] for u in names}
    dB = descent(names, phisB, autsB)
    R.gate("M3/token-level descent over the same triple", dB["verdict"],
           "SET-AMALGAM")
    szB, injB = amalgam(names, charts, {k: v[0] for k, v in phisB.items()})
    R.gate("M3/token-level amalgam size, injective", (szB, injB), (2, True))
    say("M3 descent measured")

    TABLE.append(("M3 two-frame final outcomes", "SUCCEEDS (|Phi_A|=2)",
                  "SUCCEEDS-FORCED (|Phi_B|=1)", "SET-AMALGAM at level B",
                  "fact-candidate map exists on exactly the 56 law-agreeing "
                  "ordered pairs of 144; the wing tie is broken by provenance"))
    TABLE.append(("M4 intermediate frame content", "NOT FORCED (overlap "
                  "trivial)", "FAILS-ABSENT", "vacuous (no shared token)",
                  "a probability-preserving map exists and is REJECTED: "
                  "frame-relativity respected"))
    TABLE.append(("M7 accidental agreement", "FAILS ROUTE-EXT", "FAILS-ABSENT",
                  "N/A", "SP-A and SP-C: same final law, different settings; "
                  "the product extension is not bijection-supported"))
    return finals, inters, amp_iso, born_iso


# ===========================================================================
# M5 -- RECORD ERASURE
# ===========================================================================
def m5():
    hr()
    print("M5 -- RECORD ERASURE  (control 5)")
    hr()
    U1 = mat_mul(K8, CNOT, kron(K8, H, I2))
    part = [0, 1, 0, 1]
    prov = Prov("CX", {"q0", "q1"}, ("PREP-H",), ("original",), False)
    keep = kron(K8, H, I2)
    erase = mat_mul(K8, kron(K8, H, I2), CNOT)
    nore = kron(K8, H, I2)

    P = Chart("P", K8, 4, [U1, keep], 0,
              [Token("R", part, {0: "0", 1: "1"}, 0, prov)])
    E = Chart("E", K8, 4, [U1, erase], 0,
              [Token("R", part, {0: "0", 1: "1"}, 0,
                     Prov("CX", {"q0", "q1"}, ("PREP-H",), ("original",), False))])
    N = Chart("N", K8, 4, [nore, keep], 0,
              [Token("R", part, {0: "0", 1: "1"}, 0,
                     Prov("CX", {"q0", "q1"}, ("PREP-H",), ("original",), False))])

    # committed anchors
    R.anchor("M5/eraser H-corr holds [sec4_records.py:634]",
             h_corr(support_of(K8, U1), 4, part), True)
    R.anchor("M5/eraser H-avail fails [sec4_records.py:635]",
             h_avail(support_of(K8, erase), 4, part), False)
    R.anchor("M5/no-record H-corr fails [sec4_records.py:209]",
             h_corr(support_of(K8, nore), 4, part), False)
    De = delta_field(K8, erase, U1)
    R.anchor("M5/eraser defect values [sec4_records.py:633]",
             sorted({str(K8.to_rat(v)) for r in De for v in r}),
             ["-1/2", "0", "1/2"])
    R.anchor("M5/preserving defect zero [sec4_records.py:632]",
             zero_mat(K8, delta_field(K8, keep, U1)), True)
    Ce = tensor(K8, erase, U1, 4)
    R.anchor("M5/eraser cross-sector tensor entries [sec7_descent.py:139]",
             cross_sector(K8, Ce, part, 4), 16)
    R.gate("M5/eraser off-diagonal tensor entries (W6's own)",
           off_diagonal(K8, Ce, 4), 16)
    Cp = tensor(K8, keep, U1, 4)
    R.anchor("M5/preserving cross-sector entries [sec7_descent.py:137]",
             cross_sector(K8, Cp, part, 4), 0)

    # W6's own reading: occurrence vs availability
    occ = (len(P.tokens) == 1, len(E.tokens) == 1, len(N.tokens) == 0)
    R.gate("M5/historical occurrence P,E,N", occ, (True, True, True))
    R.gate("M5/availability P,E",
           (P.tokens[0].avail, E.tokens[0].avail), (True, False))
    R.gate("M5/erased flag P,E",
           (P.tokens[0].prov.erased, E.tokens[0].prov.erased), (False, True))
    R.gate("M5/available token counts P,E,N",
           (len(P.live("available")), len(E.live("available")),
            len(N.live("available"))), (1, 0, 0))
    R.gate("M5/historical token counts P,E,N",
           (len(P.live("historical")), len(E.live("historical")),
            len(N.live("historical"))), (1, 1, 0))

    perms4 = all_perms(4)
    # E vs N at the available level: both algebras trivial -- VACUOUS, not equal
    R.gate("M5/|Phi_A(available)| E<-N", len(phi_set(E, N, "A")), 1)
    R.gate("M5/|Phi_A(historical)| E<-N",
           len(phi_set(E, N, "A", scope="historical")), 0)
    R.gate("M5/|Phi_B(historical)| E<-N",
           len(phi_set(E, N, "B", scope="historical", perms=perms4)), 0)
    R.gate("M5/|Phi_B(historical)| P<-E",
           len(phi_set(P, E, "B", scope="historical", perms=perms4)), 0)
    R.gate("M5/|Phi_A(historical)| P<-E",
           len(phi_set(P, E, "A", scope="historical")), 0)
    # POSITIVE CONTROL: the zero above must be caused by the availability item
    # and by nothing else.  P and E carry the same record law -- the record is
    # written by the same leg -- so forcing availability equal must give 1.
    R.gate("M5/P and E carry the same record law", P.law == E.law, True)
    E.tokens[0].avail = True
    R.gate("M5/availability forced equal: |Phi_A(historical)| P<-E",
           len(phi_set(P, E, "A", scope="historical")), 1)
    E.tokens[0].avail = False
    R.gate("M5/availability restored: |Phi_A(historical)| P<-E",
           len(phi_set(P, E, "A", scope="historical")), 0)
    TABLE.append(("M5 record erasure", "AVAILABILITY-SPLIT", "FAILS-ABSENT",
                  "N/A (no triple)",
                  "erased token != no event: historical counts 1,1,0"))
    say("M5 done")


# ===========================================================================
# M6 -- SYMMETRIC DUPLICATE
# ===========================================================================
def m6():
    hr()
    print("M6 -- SYMMETRIC DUPLICATE  (control 6)")
    hr()
    L = mat_mul(K8, mat_mul(K8, cnot3(0, 2), cnot3(0, 1)), h3(0))
    R.gate("M6/single leg unitary", is_unitary(K8, L), True)
    R.gate("M6/the two CNOTs commute",
           mat_mul(K8, cnot3(0, 1), cnot3(0, 2))
           == mat_mul(K8, cnot3(0, 2), cnot3(0, 1)), True)
    sig = [0] * 8
    for j in range(8):
        b = [(j >> (2 - t)) & 1 for t in range(3)]
        b[1], b[2] = b[2], b[1]
        sig[j] = (b[0] << 2) | (b[1] << 1) | b[2]
    R.gate("M6/sigma is an automorphism of the leg (amplitudes)",
           perm_conj(K8, L, sig) == L, True)
    R.gate("M6/sigma fixes j0", sig[0] == 0, True)
    # sigma preserves every committed observable AND the phase invariants
    R.gate("M6/sigma preserves the Born shadow",
           perm_conj(K8, born(K8, L), sig) == born(K8, L), True)

    def haag(Mx, i, ip, j, jp):
        return K8.mul(K8.mul(Mx[i][j], Mx[ip][jp]),
                      K8.mul(K8.conj(Mx[i][jp]), K8.conj(Mx[ip][j])))
    quads = [(i, ip, j, jp) for i in range(8) for ip in range(i + 1, 8)
             for j in range(8) for jp in range(j + 1, 8)]
    Ls = perm_conj(K8, L, sig)
    bad = sum(1 for (i, ip, j, jp) in quads
              if haag(L, i, ip, j, jp) != haag(Ls, i, ip, j, jp))
    R.gate("M6/four-cycle phase invariants preserved by sigma (784 quadruples)",
           (len(quads), bad), (784, 0))

    p1, p2 = bit_part(8, 1, 3), bit_part(8, 2, 3)
    provA = Prov("CX-A", {"q0", "q1"}, ("PREP-H",), ("original",), False)
    provB = Prov("CX-B", {"q0", "q2"}, ("PREP-H",), ("original",), False)

    def build(name):
        return Chart(name, K8, 8, [L], 0,
                     [Token("t1", p1, {0: "0", 1: "1"}, 0, provA),
                      Token("t2", p2, {0: "0", 1: "1"}, 0, provB)])

    a, b, c = build("a"), build("b"), build("c")
    R.gate("M6/both tokens occurred and are available",
           [(t.occurred, t.avail) for t in a.tokens], [(True, True)] * 2)
    R.gate("M6/joint law is the perfectly correlated pair",
           sorted(a.law), [("0", "0"), ("1", "1")])

    perms8 = all_perms(8)
    t0 = time.time()
    isos = iso_token_maps(a, b, perms8)
    say("M6 isomorphism search over 8! permutations  %.1fs" % (time.time() - t0))
    R.gate("M6/frame-isomorphism token maps", sorted(isos), [(0, 1), (1, 0)])
    nA = len(phi_set(a, b, "A"))
    nB = len(phi_set(a, b, "B", perms=perms8))
    R.gate("M6/|Phi_A| a<-b", nA, 2)
    R.gate("M6/|Phi_B| a<-b", nB, 2)
    R.gate("M6/no committed datum distinguishes the tokens", nB > 1, True)

    names = ["a", "b", "c"]
    charts = {"a": a, "b": b, "c": c}
    phis = {(x, y): [dict(t) for t in
                     phi_set(charts[x], charts[y], "B", perms=perms8)]
            for x, y in itertools.permutations(names, 2)}
    auts = {x: [dict(t) for t in phi_set(charts[x], charts[x], "B",
                                         perms=perms8)] for x in names}
    R.gate("M6/|Aut| per chart", [len(auts[x]) for x in names], [2, 2, 2])
    R.gate("M6/Phi sets inverse-closed",
           all(tuple(sorted(invert(dict(t)).items())) in
               [tuple(sorted(dict(u).items())) for u in
                phi_set(charts[y], charts[x], "B", perms=perms8)]
               for x, y in itertools.permutations(names, 2)
               for t in phi_set(charts[x], charts[y], "B", perms=perms8)), True)
    R.gate("M6/identity is in every Aut set",
           all({0: 0, 1: 1} in auts[x] for x in names), True)
    d = descent(names, phis, auts)
    R.gate("M6/descent verdict", d["verdict"], "GROUPOID-AMALGAM")
    R.gate("M6/coherent families of 8 selections", d["families"], 4)
    R.gate("M6/gauge orbits on coherent families", d["orbits"], 1)
    TABLE.append(("M6 symmetric duplicate", "SUCCEEDS-FORCED",
                  "UNDERDETERMINED (|Phi|=2)", "GROUPOID-AMALGAM",
                  "the tie survives every committed observable AND the phase "
                  "invariants"))
    say("M6 done")
    return charts, phis, auts


# ===========================================================================
# M8 -- PHASE BLINDNESS (the pin's HARD RULE, measured)
# ===========================================================================
def m8():
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

    def haag(Mx, i, ip, j, jp):
        return K8.mul(K8.mul(Mx[i][j], Mx[ip][jp]),
                      K8.mul(K8.conj(Mx[i][jp]), K8.conj(Mx[ip][j])))
    R.anchor("M8/composites differ in the four-cycle invariant "
             "[sec7_descent.py:242]",
             haag(P1, 0, 2, 0, 2) != haag(P2, 0, 2, 0, 2), True)

    # every record-level datum agrees
    R.gate("M8/leg Born shadows agree", born(K8, U2w) == born(K8, U2wp), True)
    R.gate("M8/composite Born shadows agree", born(K8, P1) == born(K8, P2), True)
    part = [0, 0, 1, 1]
    prov = Prov("W", {"c0", "c1"}, ("PREP",), ("original",), False)
    a = Chart("a", K8, 4, [U1w, U2w], 0,
              [Token("R", part, {0: "0", 1: "1"}, 0, prov)])
    b = Chart("b", K8, 4, [U1w, U2wp], 0,
              [Token("R", part, {0: "0", 1: "1"}, 0,
                     Prov("W", {"c0", "c1"}, ("PREP",), ("original",), False))])
    R.gate("M8/record algebras identical", a.law == b.law, True)
    nA = len(phi_set(a, b, "A"))
    R.gate("M8/|Phi_A| a<-b (phase NOT consulted)", nA, 1)
    # what a phase-consulting rule would return
    phase_ok = (haag(P1, 0, 2, 0, 2) == haag(P2, 0, 2, 0, 2))
    R.gate("M8/|Phi_A| if phase were on the preservation list",
           nA if phase_ok else 0, 0)
    TABLE.append(("M8 phase blindness", "SUCCEEDS-FORCED", "N/A",
                  "N/A (criterion test)",
                  "a phase-consulting phi returns 0 where the record level "
                  "returns 1: category error, measured"))
    say("M8 done")


# ===========================================================================
# M9 -- THE DESCENT DETECTOR, VALIDATED (declared addition)
# ===========================================================================
def m9(charts, phis, auts):
    hr()
    print("M9 -- DESCENT DETECTOR VALIDATION  (declared addition)")
    hr()
    names = ["a", "b", "c"]
    # consistent declaration: every edge free (the M6 groupoid)
    d0 = descent(names, phis, auts)
    R.gate("M9/consistent declaration verdict", d0["verdict"],
           "GROUPOID-AMALGAM")
    # twisted declaration: two edges pinned to the identity, the third to the
    # swap.  Each pinned edge is a legitimate member of its Phi set; the
    # triangle holonomy is the transposition.
    ident_ = {0: 0, 1: 1}
    swap_ = {0: 1, 1: 0}
    tw = {}
    for x, y in itertools.permutations(names, 2):
        tw[(x, y)] = [dict(ident_)]
    tw[("a", "c")] = [dict(swap_)]
    tw[("c", "a")] = [dict(swap_)]
    d1 = descent(names, tw, {x: [dict(ident_)] for x in names})
    R.gate("M9/twisted declaration verdict", d1["verdict"], "NO-DESCENT")
    R.gate("M9/twisted coherent families", d1["families"], 0)
    # the same three charts, consistent pinning
    tw2 = {k: [dict(ident_)] for k in tw}
    d2 = descent(names, tw2, {x: [dict(ident_)] for x in names})
    R.gate("M9/consistent pinning verdict", d2["verdict"], "SET-AMALGAM")
    # the fourth branch: two coherent families, trivial automorphisms, so the
    # gauge cannot relate them -- UNDERDETERMINED, not GROUPOID.
    two = ["a", "b"]
    d3 = descent(two, {("a", "b"): [dict(ident_), dict(swap_)]},
                 {"a": [dict(ident_)], "b": [dict(ident_)]})
    R.gate("M9/two families with trivial Aut", (d3["verdict"], d3["families"],
                                                d3["orbits"]),
           ("UNDERDETERMINED", 2, 2))
    # and the classification's fifth branch: an empty Phi on some pair
    d4 = descent(two, {("a", "b"): []}, {"a": [dict(ident_)],
                                         "b": [dict(ident_)]})
    R.gate("M9/empty Phi on a pair", d4["verdict"], "ABSENT-PAIR")
    TABLE.append(("M9 detector validation", "N/A", "N/A",
                  "NO-DESCENT (twisted) / SET-AMALGAM (consistent)",
                  "the triple law has power: the SAME charts descend or fail "
                  "by the declaration alone"))
    say("M9 done")


# ===========================================================================
def main():
    print("=" * 78)
    print("v12 W6 -- RECORD CO-REFERENCE AND EFFECTIVE DESCENT")
    print("exact arithmetic: Q(zeta_8) and Q(cos pi/8); no floats")
    print("=" * 78)
    step0()
    m1()
    m2()
    M = Composite()
    finals, inters, amp_iso, born_iso = m3_m4_m7(M)
    m5()
    charts, phis, auts = m6()
    m8()
    m9(charts, phis, auts)

    hr("=")
    print("THE DESCENT TABLE")
    hr("=")
    print("  %-28s %-20s %-26s %-46s" % ("model", "A (fact)", "B (event token)",
                                         "C (effective descent)"))
    hr()
    for row in TABLE:
        print("  %-28s %-20s %-26s %-46s" % row[:4])
        print("      %s" % row[4])
    hr()

    nfail = R.finish()
    sys.exit(1 if nfail else 0)


if __name__ == "__main__":
    main()
