#!/usr/bin/env python3
"""O4 DISCRIMINATOR -- UNRECORDED ACTUALITY ON THE W6 CO-REFERENCE BASE.

Executes the frozen pin `v13/note-o4-discriminator-pin.md` (commit e1e8dcd,
sha 2568bc528796) against the immutable base 71371ae (W6 TERMINAL, v12 LOG
#41; paper 2 TERMINAL; paper 0 v2.4 section O4), RE-DERIVED under the
adjudication's order RD-1..RD-6 (v13 LOG #196).

THE QUESTION.  Paper 0 v2.4 leaves an explicit fork.  O4-A (configuration
realism) holds that unrecorded local configurations are actual but
ephemeral, and REQUIRES a covariant co-reference rule for them.  O4-B
(record actualism) holds that only records are actual.  W6 built the base at
which the question becomes decidable: on its committed two-frame model
RECORD facts provably descend.  This unit asks whether UNRECORDED
CONFIGURATION facts descend under the SAME instrument, AT THE SAME
COORDINATES -- and, where a rule exists, what probability law attaches to
what it transports.

THE MATCHED TABLE (RUNBOOK section 15 addendum; RD-1).  The central object is
a table with EVERY coordinate matched: three declared fact-classes x every
declared READ TIME x every candidate rule x every setting, one gate set, one
naming convention, name-free matched representatives in the arena test.  The
read time is a DECLARED COORDINATE of the datum, carried in the datum itself
and gated for equality across classes in every cell: a class-versus-class
contrast whose classes are read at different times is a coordinate effect in
disguise, and this instrument cannot produce one without a gate failing (the
`readtime-conflate` mutant restores the reviewed defect and must die).

THE INSTRUMENT.  Transport of fact-data along the co-reference maps of the
W6 base.  ONE set of descent gates, applied identically to three declared
fact-classes at every read time:

  F-REC   record facts, division-event-anchored (POSITIVE CONTROL: W6's
          terminal descent results must reproduce, anchored exit-1);
  F-CFG   unrecorded configuration facts -- "the configuration at read time
          t is X" -- as transportable data (THE OBJECT, at the read times
          strictly before the final declared division event);
  F-CTRL  a deliberately mis-conventioned class that reads configuration
          NAMES (NEGATIVE CONTROL: it must FAIL; if it passes the
          instrument is dead and the run says so).

Candidate co-reference rules for F-CFG are declared inside the pin's
corridor -- covariant, name-blind, NO GLOBAL SLICE -- with their gates fixed
BEFORE any fixture value is computed (the receipt's gate order proves the
freeze, and the evaluation counter is gated at zero at the freeze).

THE LTP GATE.  Every candidate must state what probability law attaches to
the actuality it transports.  That is COMPUTED, not asserted: the actuality
at each read time is exhibited, and the declared-law residual of W5's
LTP-forcing lemma is evaluated AT THAT TIME on the model's own admissible
p(0).  Where the residual is nonzero the read time is NOT a division event
of the model as declared, so no committed law conditions on the transported
configuration: the candidate is recorded LTP-BARE at that coordinate.  The
LAWFUL branch is not a stipulation either: it is measured to fire at the
final declared division event, where a shared record law does condition on
the datum, and an injection mutant proves the selector reaches it.

THE CAUSE.  Where transport fails the failing clause is DECOMPOSED and the
obstructing object is measured as a relation, not as a bare zero: the two
frames' occupied sets at the second read time lie in ONE ORBIT of the base's
own admitted wing exchange at four of six settings (law-preserving at two of
them), and where they do not the disjointness is cardinality-forced.

THE ARENA TEST.  Section 15 discipline, at NAME-FREE MATCHED
REPRESENTATIVES: every quantity is declared in both representative types
(name-indexed and name-free) so that the relabelling coordinate is measured
for what it separates -- representative types -- rather than credited to a
fact-class difference.

Exact arithmetic throughout: the totally real quartic field Q(cos pi/8) of
the committed composite model (tuple equality IS field equality) and
fractions.Fraction.  No float enters any path.  Anchors exit 1 on mismatch.
`--mutant NAME` breaks exactly one anchor, gate or derivation step and must
exit 1 naming what it falsified.  No wall-clock value enters the receipt or
the rendered output, so two delivery-mode runs are byte-identical.

Scope: finite; ONE committed carrier of 36 configurations; six declared
settings; two declared frames; three declared read times; the declared
72-element permutation scope and its declared 96-element extension.  No
locality, topology, causality, spacetime, field, QFT or gravity object is
constructed or claimed.  Nothing is claimed about nature.  The charter fork
is NOT adjudicated here.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import itertools
import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
sys.path.insert(0, str(REPO / "v12" / "code"))
sys.path.insert(0, str(REPO / "v12" / "paper1_code"))
sys.path.insert(0, str(REPO / "v12" / "paper2_code"))

# ---- the W6 base, imported READ-ONLY; nothing here is forked --------------
import w6_coreference_exact as W6          # the terminal co-reference base
from model_composite import (Composite, SETTINGS, SETTING_ORDER,  # noqa: E402
                             NC, idx, unidx)
import core as P2                          # paper 2's exact descent machinery
import models as P2M                       # paper 2's exact witness fixtures

SCHEMA = "o4-discriminator-receipt-v2"
PIN_COMMIT = "e1e8dcd"
PIN_SHA256 = "2568bc528796"
BASE_COMMIT = "71371ae"
OUT_TXT = HERE / "o4_discriminator_output.txt"
OUT_JSON = HERE / "o4_discriminator_receipt.json"

MUTANT: str | None = None
SOURCE_SHA256 = ""

GATES: list[dict] = []
ANCHORS: list[dict] = []
TABLES: dict = {}
FINDINGS: dict = {}

T0 = time.time()
_LAST_PROG = [time.time()]

# The freeze counter (RUNBOOK section 13(4)): no fixture value of any
# fact-class may be evaluated before the declarations are recorded.
_FROZEN = False
_FEVALS = 0

# Fresh-evaluation bookkeeping (RUNBOOK section 14 addendum).
_FRESH = False
_CACHE = {"value_cache_hits": 0, "value_cache_misses": 0}
_MEMO: dict = {}


def prog(msg: str) -> None:
    """Progress line; stderr only, so no wall-clock reaches any artifact."""
    now = time.time()
    _LAST_PROG[0] = now
    sys.stderr.write("[o4 %6.1fs] %s\n" % (now - T0, msg))
    sys.stderr.flush()


def gate(gid: str, cls: str, claim: str, ok: bool, value=None) -> bool:
    GATES.append({"id": gid, "class": cls, "claim": claim,
                  "passed": bool(ok), "value": value})
    return ok


def anchor(aid: str, source: str, quantity: str, committed, computed) -> None:
    ANCHORS.append({"id": aid, "source": source, "quantity": quantity,
                    "committed": committed, "computed": computed,
                    "passed": committed == computed})


def canon(v) -> str:
    """A canonical, sortable, printable key for any value.  No memo: this
    instrument's sweeps are small enough that a cache would only be a place
    for an equality to hide."""
    if isinstance(v, (list, tuple)):
        return "(" + ",".join(canon(x) for x in v) + ")"
    if isinstance(v, (set, frozenset)):
        return "{" + ",".join(sorted(canon(x) for x in v)) + "}"
    if isinstance(v, dict):
        return "{" + ",".join(sorted(canon(k) + ":" + canon(x)
                                     for k, x in v.items())) + "}"
    return str(v)


def _memo(key, build):
    """The instrument's ONLY value cache, and the only cache on any path the
    self-test can reach.  Bypassed entirely in fresh mode, where the hit count
    is gated at zero; the `memo-lax` mutant restores the reviewed defect (a
    self-test reading the cache) and must die there."""
    if _FRESH and MUTANT != "memo-lax":
        _CACHE["value_cache_misses"] += 1
        return build()
    if key in _MEMO:
        if _FRESH:
            _CACHE["value_cache_hits"] += 1
        return _MEMO[key]
    if _FRESH:
        _CACHE["value_cache_misses"] += 1
    _MEMO[key] = build()
    return _MEMO[key]


# ===========================================================================
# 1.  THE ARENA, DECLARED AS DATA (RUNBOOK section 15)
#
#     Carrier, boundary, family, law, state, arena -- every one of them the
#     W6 terminal committed configuration, enumerated from the base.  No new
#     fixture is built anywhere in this file.  The READ TIME is declared here
#     as a coordinate of the same standing as the setting and the frame.
# ===========================================================================
M = Composite()
K = M.K
J0 = 0

POINTER3 = W6.POINTER3
PARTA, PARTB = W6.PARTA, W6.PARTB
VALS = W6.VALS
LIST_A, LIST_B = W6.LIST_A, W6.LIST_B


def declared_scope():
    """THE ADMITTED ISOMORPHISM GROUP of the base, enumerated from W6's own
    generator (wing exchange x pointer 3-cycles x the two qubit flips) and
    its declared extension (the pointer transposition, which fixes the ready
    state).  Every count below is computed from the enumeration."""
    base = [W6.build_perm(sw, sa, sb, fa, fb)
            for sw in (0, 1) for sa in range(3) for sb in range(3)
            for fa in (0, 1) for fb in (0, 1)]
    ext = [W6.build_perm_tr(sw, ta, tb, fa, fb)
           for sw in (0, 1) for ta in (0, 1) for tb in (0, 1)
           for fa in (0, 1) for fb in (0, 1)]
    seen, ext_u = {tuple(p) for p in base}, []
    for p in ext:
        if tuple(p) not in seen:
            seen.add(tuple(p))
            ext_u.append(p)
    admitted = [p for p in base if p[J0] == J0]
    admitted_ext = [p for p in base + ext_u if p[J0] == J0]
    search_ext = base + ext_u
    if MUTANT == "scope-lax":
        base = base[:2]
        search_ext = search_ext[:2]
    return {"base": base, "extension": ext, "extension_all": search_ext,
            "admitted": admitted, "admitted_extension": admitted_ext,
            "n_base": len(base), "n_ext_total": len(search_ext),
            "n_admitted": len(admitted),
            "n_admitted_extension": len(admitted_ext)}


SCOPE = declared_scope()
WSWAP = W6.build_perm(1, 0, 0, 0, 0)          # the pure wing exchange
IDPERM = W6.build_perm(0, 0, 0, 0, 0)


def switchings(nlegs: int):
    """THE CHECKPOINT-PHASE SWITCHINGS at which amplitude data enters this
    base.  W6's declared matching levels quotient the amplitude layer by an
    overall SIGN PER LEG -- a real orthogonal propagator and its negative
    generate one stochastic process -- so the switching group of a chart with
    `nlegs` declared legs is {+1,-1}^nlegs, enumerated here and never typed.
    The Born shadow is invariant under it by construction, which is exactly
    what makes it the gauge and not a perturbation."""
    out = list(itertools.product((1, -1), repeat=nlegs))
    if MUTANT == "gauge-subsample":
        out = out[:1]
    return out


def apply_switching(legs, eps):
    return [L if e == 1 else W6.sp_neg(K, L) for L, e in zip(legs, eps)]


# ===========================================================================
# 2.  THE CHARTS OF THE BASE, AT A DECLARED READ TIME.  Built through W6's
#     own constructor, so occurrence, availability and the law are
#     RECOMPUTED, never stipulated.
#
#     THE READ TIME t is the number of declared legs applied: t = 0 is the
#     initial time, t = NLEGS the final time, and both are declared division
#     events of the model.  A chart READ AT t is the same process -- the same
#     declared legs, the same law -- presented with the record tokens that
#     have been written by then.  W6's own Chart._law reads the joint record
#     law at the time the last visible token was written, so the read time
#     propagates into the record datum through the base's own semantics.
# ===========================================================================
def cprov(wing, ang):
    return W6.cprov(wing, ang)


def _legkey(sp, fr, eps, relabel, extra_identity):
    return canon((sp, fr, eps, tuple(relabel) if relabel is not None else None,
                  extra_identity))


def chart_at(sp, fr, t, eps=None, relabel=None, extra_identity=False):
    """The committed chart at (setting, frame), carrying the record tokens
    VISIBLE at read time t, optionally carried by a checkpoint-phase
    switching, a configuration relabelling, or an extra identity leg
    prepended (the time re-indexing of the no-slice gate, under which every
    write index and the read time itself shift by one)."""
    a8, b8 = SETTINGS[sp]
    legs = list(M.legs(sp, fr))
    if eps is not None:
        legs = apply_switching(legs, eps)
    j0 = J0
    pa, pb = PARTA, PARTB
    if relabel is not None:
        legs = [W6.sp_conj(L, relabel) for L in legs]
        j0 = relabel[J0]
        pa, pb = W6.push_part(PARTA, relabel), W6.push_part(PARTB, relabel)
    if extra_identity:
        legs = [W6.sp_id(K, NC)] + legs
    wa = 1 if fr == "F1" else 2
    wb = 2 if fr == "F1" else 1
    shift = 1 if extra_identity else 0
    wa, wb = wa + shift, wb + shift
    tA = W6.Token("R_A", pa, VALS, wa, cprov("A", a8))
    tB = W6.Token("R_B", pb, VALS, wb, cprov("B", b8))
    # `t` is the read index IN THIS PRESENTATION'S OWN INDEXING: the caller
    # has already carried it across the re-indexing, exactly as the write
    # indices above are carried, so no second shift is applied here.
    visible = [tk for tk in (tA, tB)
               if MUTANT == "chart-time-lax" or tk.write_leg + 1 <= t]
    c = W6.Chart("%s/%s@t%d%s" % (sp, fr, t, "+i" if extra_identity else ""),
                 K, NC, legs, j0, visible)
    c.lk = _legkey(sp, fr, eps, relabel, extra_identity)
    return c


def _restrict_in_time(L, rows_after, cols_before):
    """THE TIME-ORIENTATION CONVENTION (RUNBOOK section 14).  A leg restricted
    to the realized process keeps the rows the process can occupy AFTER it and
    the columns it occupies BEFORE it.  The `orient-flip` mutant exchanges the
    two -- the same restriction read backwards in time -- and must die against
    the base's own realized-legs anchor."""
    if MUTANT == "orient-flip":
        return W6.sp_restrict(L, cols_before, rows_after)
    return W6.sp_restrict(L, rows_after, cols_before)


def realized_legs(sp, fr):
    """Each declared leg restricted to the configurations the process
    actually occupies before and after it -- W6's realized process."""
    T = M.propagators(sp, fr)[:3]
    supp = [{J0}] + [{i for (i, j), v in T[t].items()
                      if j == J0 and not K.is_zero(v)} for t in range(3)]
    return [_restrict_in_time(M.legs(sp, fr)[t], supp[t + 1], supp[t])
            for t in range(3)], supp


NLEGS = len(M.legs(SETTING_ORDER[0], "F1"))   # computed, never typed
READ_TIMES = tuple(range(1, NLEGS + 1))       # 1 .. NLEGS
FINAL_TIME = READ_TIMES[-1]                   # the final declared division event
OBJECT_TIMES = READ_TIMES[:-1]                # strictly before it: the pin's object
CHARTS = {(sp, fr): chart_at(sp, fr, FINAL_TIME)
          for sp in SETTING_ORDER for fr in ("F1", "F2")}
CHART_KEYS = sorted(CHARTS)


# ===========================================================================
# 3.  THE THREE FACT-CLASSES.  Declared -- carrier, datum, preservation list,
#     transport -- BEFORE any fixture value is computed.  All three take the
#     READ TIME as their first coordinate after the chart's, all three record
#     the time at which they were read in the datum itself, and the
#     like-for-like gate measures that equality cell by cell.
# ===========================================================================
def _bump():
    global _FEVALS
    if not _FROZEN and MUTANT != "freeze-lax":
        raise RuntimeError("fixture truth evaluated before the freeze")
    _FEVALS += 1


def _read_index(t, extra_identity, compensate):
    """The index at which a re-indexed presentation is read.  Prepending an
    identity leg shifts every index by one, so the SAME MOMENT is read at
    t + 1 there.  A rule that reads the same INDEX instead of the same moment
    is index-bound, and the no-slice gate's second clause measures exactly
    that difference; the `global-now-smuggler` mutant makes every rule read
    the index."""
    if MUTANT == "global-now-smuggler":
        compensate = False
    return t + (1 if (extra_identity and compensate) else 0)


def datum_rec(sp, fr, t, eps=None, relabel=None, extra_identity=False,
              compensate=True):
    """F-REC.  Carrier: the record tokens WRITTEN BY READ TIME t.  Datum: the
    joint law of their declared values on the ACTUAL (positive-probability)
    value tuples at that time -- W6's own Chart law, which reads at the time
    the last visible token was written.  Division-event-anchored: at
    t = NLEGS every declared token has been written and the time is a
    declared division event of the model."""
    _bump()
    rt = _read_index(t, extra_identity, compensate)
    if MUTANT == "readtime-conflate":
        rt = FINAL_TIME + (1 if extra_identity else 0)
    c = chart_at(sp, fr, rt, eps, relabel, extra_identity)
    return c, {"carriers": len(c.tokens), "read_time": rt,
               "law": {canon(k): canon(v) for k, v in c.law.items()},
               "read": tuple(canon(c.read(i)) for i in range(NC))}


def datum_cfg(sp, fr, t, eps=None, relabel=None, extra_identity=False,
              compensate=True):
    """F-CFG.  Carrier: the 36 configuration propositions "the configuration
    at read time t is i".  Datum: the actuality bit (positive probability)
    and the exact probability of each configuration at that time.  At the
    read times strictly before the final declared division event this is
    exactly the pin's "the configuration between division events is X",
    presented as transportable data of the same type as F-REC's."""
    _bump()
    rt = _read_index(t, extra_identity, compensate)
    c = chart_at(sp, fr, rt, eps, relabel, extra_identity)
    p = c.dist(rt)
    return c, {"carriers": NC, "read_time": rt,
               "actual": frozenset(p),
               "law": {i: canon(p[i]) for i in sorted(p)}}


def datum_ctrl(sp, fr, t, eps=None, relabel=None, extra_identity=False,
               compensate=True):
    """F-CTRL.  The deliberately MIS-CONVENTIONED class: the same 36
    carriers, but the datum is the configuration's own integer NAME.  It is
    mis-conventioned in exactly one respect -- it reads a label the declared
    gauge is free to change -- and it must FAIL the gates records pass.  A
    name has no read time, which is itself part of the mis-convention: the
    class's row is measured constant in the read-time coordinate."""
    _bump()
    rt = _read_index(t, extra_identity, compensate)
    c = chart_at(sp, fr, rt, eps, relabel, extra_identity)
    return c, {"carriers": NC, "read_time": rt,
               "name": {i: str(i) for i in range(NC)}}


FACT_CLASSES = (
    ("F-REC", "record facts (division-event-anchored)", datum_rec,
     "POSITIVE CONTROL"),
    ("F-CFG", "unrecorded configuration facts at the read time",
     datum_cfg, "THE OBJECT"),
    ("F-CTRL", "the name-reading mis-conventioned class", datum_ctrl,
     "NEGATIVE CONTROL"),
)


# ---- transport admissibility, ONE implementation per class ----------------
def _is_identity_leg(L):
    """A leg that carries every configuration in its own domain to itself is
    no transition at all.  Stated on the domain, so that a leg restricted to
    a realized support is recognised as well as the full identity matrix."""
    return bool(L) and all(i == j and v == K.one for (i, j), v in L.items())


def _legs_of(chart, drop_identity: bool):
    """The declared legs of a chart, with identity legs dropped when the rule
    is index-free.  Dropping an identity leg is the canonical normalisation
    that makes a rule blind to a re-indexing of the chart's time coordinate."""
    if drop_identity:
        return [L for L in chart.legs if not _is_identity_leg(L)]
    return list(chart.legs)


def _legs_compatible_raw(ca, cb, p, level, order_free, drop_identity):
    la, lb = _legs_of(ca, drop_identity), _legs_of(cb, drop_identity)
    if len(la) != len(lb):
        return False
    conj = [W6.sp_conj(L, p) for L in lb]
    orders = (list(itertools.permutations(range(len(la)))) if order_free
              else [tuple(range(len(la)))])
    if MUTANT == "sign-flip" and level == "sign":
        return any(all(conj[t] == la[sg[t]] for t in range(len(la)))
                   for sg in orders)
    return any(all(W6.leg_match(K, conj[t], la[sg[t]], level)
                   for t in range(len(la))) for sg in orders)


def legs_compatible(ca, cb, p, level, order_free, drop_identity, pidx=None):
    """Does the permutation p carry chart b's declared legs onto chart a's at
    the declared matching level?  ORDER-FREE matching is W6's own declared
    choice (two frames of one experiment differ exactly by the order of two
    commuting legs); requiring the order is what a slice-indexed rule does
    and the no-slice gate measures the difference.

    The answer depends on the two charts' LEGS alone -- never on the read
    time, the record set or the fact-class -- so it is memoised on the legs'
    own declared key through the instrument's single value cache, which the
    fresh-evaluation phase bypasses like every other cached value."""
    if pidx is None or not hasattr(ca, "lk") or not hasattr(cb, "lk"):
        return _legs_compatible_raw(ca, cb, p, level, order_free,
                                    drop_identity)
    return _memo(("legs", ca.lk, cb.lk, pidx, level, order_free,
                  drop_identity),
                 lambda: _legs_compatible_raw(ca, cb, p, level, order_free,
                                              drop_identity))


def transports_rec(ca, da, cb, db, perms, level, order_free, drop_identity):
    """F-REC transports: token maps induced by a frame-isomorphism and
    surviving W6's preservation list (LIST_B).  This is W6-B's own object,
    routed through the same gate harness as the other two classes."""
    isos = []
    for pidx, p in enumerate(perms):
        if p[cb.j0] != ca.j0:
            continue
        if not legs_compatible(ca, cb, p, level, order_free, drop_identity,
                               pidx):
            continue
        tau, ok = {}, True
        for ib, tb in enumerate(cb.tokens):
            pushed = W6.push_part(tb.part, p)
            hits = [ia for ia, ta in enumerate(ca.tokens)
                    if W6.same_partition(pushed, ta.part)]
            if len(hits) != 1:
                ok = False
                break
            tau[ib] = hits[0]
        if ok and len(set(tau.values())) == len(tau) == len(ca.tokens):
            if tau not in isos:
                isos.append(tau)
    if MUTANT == "rec-uncut" and isos:
        # THE RECORD-LEVEL TIE LEFT UNCUT: the wing exchange admitted at the
        # token level without a frame-isomorphism to license it, so the base's
        # own FORCED result becomes UNDERDETERMINED.
        for tau in list(isos):
            sw = {b: (1 - a) for b, a in tau.items()} if len(tau) == 2 else None
            if sw and sw not in isos:
                isos.append(sw)
    return [tuple(sorted(t.items()))
            for t in W6.phi_set(ca, cb, items=LIST_B, isos=isos)]


def transports_cfg(ca, da, cb, db, perms, level, order_free, drop_identity):
    """F-CFG transports: configuration bijections in the admitted scope that
    carry b's initial configuration to a's, carry b's declared legs onto a's
    at the declared level, AND carry b's read-time datum onto a's -- the
    actuality bit and the exact probability of every configuration.  The last
    clause is the configuration-level analogue of items 1 and 3 of W6's
    preservation list, and it is the only place the class's own datum is
    consulted."""
    out = []
    for pidx, p in enumerate(perms):
        if p[cb.j0] != ca.j0:
            continue
        if not legs_compatible(ca, cb, p, level, order_free, drop_identity,
                               pidx):
            continue
        if MUTANT == "name-reader" and any(p[i] != i for i in range(NC)):
            continue
        if {p[i] for i in db["actual"]} != set(da["actual"]):
            continue
        if any(da["law"].get(p[i]) != db["law"].get(i) for i in range(NC)):
            continue
        out.append(tuple((i, p[i]) for i in range(NC)))
    return out


def transports_ctrl(ca, da, cb, db, perms, level, order_free, drop_identity):
    """F-CTRL transports: the same shape, but the preserved datum is the
    configuration NAME.  A bijection is admitted only if it carries every
    name to itself."""
    out = []
    for pidx, p in enumerate(perms):
        if p[cb.j0] != ca.j0:
            continue
        if not legs_compatible(ca, cb, p, level, order_free, drop_identity,
                               pidx):
            continue
        if any(da["name"].get(p[i]) != db["name"].get(i) for i in range(NC)):
            continue
        out.append(tuple((i, p[i]) for i in range(NC)))
    return out


TRANSPORT = {"F-REC": transports_rec, "F-CFG": transports_cfg,
             "F-CTRL": transports_ctrl}


# ===========================================================================
# 4.  THE CANDIDATE RULES, DECLARED WITH THEIR GATES BEFORE FIXTURE TRUTH
#
#     Every candidate lives inside the pin's corridor by DECLARATION and is
#     then MEASURED against it: covariance, name-blindness and the no-slice
#     gate are computed for each, at every read time, and a candidate that
#     fails the corridor is gated out with the measurement that gates it
#     printed.  C1 and C1a are the two declared OUTSIDE controls: C1a
#     separates the slice reading from the leg-order convention, so that
#     what empties C1 is measured rather than asserted.
# ===========================================================================
CANDIDATES = (
    {"id": "C1", "name": "NAIVE-SLICE",
     "definition":
         "Two unrecorded configuration facts co-refer iff they carry the "
         "same configuration label at the same declared time index.  The "
         "rule matches legs IN ORDER and counts identity legs, so it reads "
         "a single external time coordinate shared by all contexts.",
     "level": "exact", "order_free": False, "drop_identity": False,
     "perms": "base",
     "corridor_claim": "GLOBAL-SLICE: declared as the gated-out control",
     "ltp_claim": "none stated"},
    {"id": "C1a", "name": "NAIVE-SLICE-ORDER-FREE",
     "definition":
         "C1 with ONE declaration changed: the legs are matched order-free "
         "while identity legs are still counted, so the rule still reads a "
         "time index but no longer fails merely because the two frames of "
         "one experiment order two commuting legs differently.  Declared so "
         "that what empties C1 is MEASURED -- the leg-order convention or "
         "the slice reading -- rather than attributed.",
     "level": "exact", "order_free": True, "drop_identity": False,
     "perms": "base",
     "corridor_claim": "GLOBAL-SLICE: declared as the gated-out control",
     "ltp_claim": "none stated"},
    {"id": "C2", "name": "DESCENT-RESTRICTION",
     "definition":
         "Two unrecorded configuration facts co-refer iff the W6 groupoid "
         "acts between their charts: the transport must be an admitted "
         "frame-isomorphism, order-free and blind to identity legs, and it "
         "must carry the read-time datum.  Co-reference is declared only "
         "where the record-level base already supplies a map.  The matching "
         "level is the level at which the base's own token tie is measured "
         "to be cut -- the BORN level: matching the full declared legs by "
         "their Born shadows alone already forces the record-level map at "
         "every setting.",
     "level": "born", "order_free": True, "drop_identity": True,
     "perms": "base",
     "corridor_claim": "covariant, name-blind, no global slice",
     "ltp_claim": "the law of the recorded level, if it reaches"},
    {"id": "C2X", "name": "DESCENT-RESTRICTION-AT-THE-AMPLITUDE-LEVEL",
     "definition":
         "C2's rule with one declaration changed: the legs must match on the "
         "nose, at the exact amplitude level, rather than by their Born "
         "shadows.  Declared as a variant so that what the corridor's "
         "covariance gate does to the matching level is REPORTED rather than "
         "chosen: a rule reading amplitudes on the nose is being asked to be "
         "invariant under the checkpoint-phase switchings, which are exactly "
         "the amplitude gauge.",
     "level": "exact", "order_free": True, "drop_identity": True,
     "perms": "base",
     "corridor_claim": "covariant, name-blind, no global slice",
     "ltp_claim": "the law of the recorded level, if it reaches"},
    {"id": "C3", "name": "MODAL-CARRIER",
     "definition":
         "The base's own structure suggests it: W6 measured that what "
         "identifies the record tokens at the symmetric settings is carried "
         "by U_prep's columns on the configurations the process never "
         "occupies -- the identification is carried by transitions the "
         "process never takes.  C3 tests whether F-CFG transport can be "
         "carried by the same modal structure: the FULL declared legs, "
         "including never-taken transitions, matched up to the per-leg sign "
         "(the level at which the amplitude gauge acts).",
     "level": "sign", "order_free": True, "drop_identity": True,
     "perms": "extension_all",
     "corridor_claim": "covariant, name-blind, no global slice",
     "ltp_claim": "must be computed: modal structure carries no law by "
                  "itself"},
    {"id": "C4", "name": "REALIZED-ONLY",
     "definition":
         "The mirror of C3: transport carried by the REALIZED process "
         "alone -- each leg restricted to the configurations actually "
         "occupied before and after it -- matched at the Born level, which "
         "is the level at which the record-level tie is cut.  Nothing "
         "counterfactual is consulted.",
     "level": "born", "order_free": True, "drop_identity": True,
     "perms": "base", "realized": True,
     "corridor_claim": "covariant, name-blind, no global slice",
     "ltp_claim": "must be computed"},
)

DESCENT_GATES = (
    ("EXIST", "a transport exists on every declared edge"),
    ("FORCED", "the transport is unique on every declared edge"),
    ("INV", "the inverse of an admitted transport is admitted in reverse"),
    ("TRI", "triple coherence holds on the declared triple [SP-A]"),
    ("GLUE", "a coherent family exists in one gauge orbit with an "
             "injective colimit [SP-A]"),
    ("CERT", "the transported datum is CERTIFIED, not merely compatible"),
    ("COVAR", "the verdict is equivariant under the admitted arena action"),
    ("NAMEBLIND", "the verdict survives a pure configuration relabelling"),
    ("NOSLICE", "the verdict survives a pure time re-indexing, in both "
                "clauses: identity-leg normalisation and index compensation"),
    ("LTP", "a committed probability law conditions on the transported "
            "datum"),
)


# ===========================================================================
# 5.  THE FREEZE
# ===========================================================================
def run_freeze():
    global _FROZEN
    prog("freeze: declarations recorded before any fixture value")
    gate("O4-FREEZE", "freeze",
         "THE DECLARATIONS ARE FROZEN BEFORE FIXTURE TRUTH (RUNBOOK 13(4)).  "
         "The three fact-classes with their read-time coordinate, their "
         "carriers and preservation lists, the ten descent gates, the six "
         "candidate rules with their matching levels and corridor claims, "
         "and the declared read times are all recorded above, and the "
         "fact-datum evaluation counter is measured to be ZERO at this "
         "point.  The `freeze-lax` mutant evaluates one fixture datum first "
         "and must die here",
         _FEVALS == 0 and len(GATES) == 0,
         {"fact_datum_evaluations_before_freeze": _FEVALS,
          "fact_classes": [c[0] for c in FACT_CLASSES],
          "descent_gates": [g[0] for g in DESCENT_GATES],
          "candidates": [c["id"] for c in CANDIDATES],
          "read_times": list(READ_TIMES),
          "object_read_times": list(OBJECT_TIMES)})
    TABLES["declarations"] = {
        "fact_classes": [{"id": i, "role": r,
                          "datum": (f.__doc__ or "").split("\n")[0]}
                         for i, _d, f, r in FACT_CLASSES],
        "descent_gates": [{"id": i, "claim": c} for i, c in DESCENT_GATES],
        "candidates": [{k: v for k, v in c.items()} for c in CANDIDATES],
        "read_times": list(READ_TIMES),
        "object_read_times": list(OBJECT_TIMES),
        "final_declared_division_event": FINAL_TIME}
    _FROZEN = True


# ===========================================================================
# 6.  ANCHORS -- every reused value exit-1 against its committed receipt
# ===========================================================================
def run_anchors():
    prog("anchors: W6 terminal, paper 2 terminal, W5 LTP lemma")

    # -- the committed model itself (paper 1 / W6 census) -------------------
    anchor("A01", "v12/code/w6_output.txt M3 [sec4_records.py:516]",
           "the eight local measurement operators are exactly orthogonal",
           8, sum(1 for ang in (0, 2, 4, 6) for wg in ("A", "B")
                  if M.is_orthogonal(M.U_local(wg, ang))))
    anchor("A02", "v12/code/w6_output.txt M3 [sec4_records.py:524]",
           "the local operators commute at all nine setting pairs",
           9, sum(1 for a8 in (0, 2, 4) for b8 in (0, 2, 6)
                  if M.sp_mul(M.U_local("A", a8), M.U_local("B", b8))
                  == M.sp_mul(M.U_local("B", b8), M.U_local("A", a8))))
    anchor("A03", "v12/code/w6_output.txt M3 [sec4_records.py:505]",
           "U_prep is exactly orthogonal", True, M.is_orthogonal(M.U_prep()))

    # -- W6's declared permutation scope and its j0 filter ------------------
    anchor("A04", "v12/note-w6-record-coreference.md SCOPE 2",
           "the declared permutation scope has 72 elements, all distinct",
           (72, 72), (SCOPE["n_base"], len({tuple(p) for p in SCOPE["base"]})))
    anchor("A05", "v12/note-w6-record-coreference.md SCOPE 2",
           "the j0 filter admits exactly 2 of the 72",
           2, SCOPE["n_admitted"])
    anchor("A06", "v12/note-w6-record-coreference.md SCOPE 2",
           "the declared extension admits exactly 8",
           8, SCOPE["n_admitted_extension"])
    anchor("A07", "v12/note-w6-record-coreference.md SCOPE 2",
           "the extension's comprehension bound is 96 -- the declared base "
           "scope together with the pointer-transposition elements it does "
           "not already contain, counted by enumeration",
           96, SCOPE["n_ext_total"])

    # -- W6-A: the biconditional over the 144 ordered pairs -----------------
    agree = cand = 0
    viol = []
    for x, y in itertools.product(CHART_KEYS, repeat=2):
        same = CHARTS[x].law == CHARTS[y].law
        n = len(W6.phi_set(CHARTS[x], CHARTS[y]))
        agree += 1 if same else 0
        cand += 1 if n > 0 else 0
        if same != (n > 0):
            viol.append((x, y))
    anchor("A08", "v12/note-w6-record-coreference.md W6-A",
           "law-agreeing / candidate-admitting ordered pairs of 144, and "
           "violations of the biconditional",
           (56, 56, 0), (agree, cand, len(viol)))
    same_exp = sum(1 for x, y in itertools.product(CHART_KEYS, repeat=2)
                   if CHARTS[x].law == CHARTS[y].law and x[0] == y[0])
    anchor("A09", "v12/note-w6-record-coreference.md W6-A",
           "of the 56, same-experiment pairs and accidental agreements",
           (24, 32), (same_exp, agree - same_exp))
    lawclass: dict = {}
    for k in CHART_KEYS:
        lawclass.setdefault(tuple(sorted(str(x) for x in CHARTS[k].law.items())),
                            []).append(k)
    anchor("A10", "v12/note-w6-record-coreference.md W6-A",
           "the final-law class sizes",
           [2, 4, 6], sorted(len(v) for v in lawclass.values()))

    # -- W6-B: the wing tie, and what cuts it -------------------------------
    nA, nB = [], []
    for sp in SETTING_ORDER:
        x, y = (sp, "F1"), (sp, "F2")
        isos = W6.iso_maps(CHARTS[x], CHARTS[y], SCOPE["base"])
        nA.append(len(W6.phi_set(CHARTS[x], CHARTS[y])))
        nB.append(len(W6.phi_set(CHARTS[x], CHARTS[y], items=LIST_B,
                                 isos=isos)))
    anchor("A11", "v12/note-w6-record-coreference.md W6-B "
           "[v12/code/w6_output.txt:116]",
           "|Phi_A| at the six settings (the wing tie)", [2] * 6, nA)
    anchor("A12", "v12/note-w6-record-coreference.md W6-B "
           "[v12/code/w6_output.txt:126]",
           "|Phi_B| at the six settings (forced, the identity)", [1] * 6, nB)

    # -- W6 M4: the intermediate slice, W6's own measurement ----------------
    #    Built the base's own way -- the TRUNCATED process with the tokens
    #    written by then -- so that this unit's read-time construction (the
    #    full declared process with the visible record set) is anchored
    #    against an independent reading of the same words.
    inters = {}
    for sp in SETTING_ORDER:
        for fr in ("F1", "F2"):
            a8, b8 = SETTINGS[sp]
            wing = "A" if fr == "F1" else "B"
            tok = W6.Token("R_%s" % wing, PARTA if wing == "A" else PARTB,
                           VALS, 1, cprov(wing, a8 if wing == "A" else b8))
            inters[(sp, fr)] = W6.Chart("%s/%s@t2" % (sp, fr), K, NC,
                                        list(M.legs(sp, fr))[:2], J0, [tok])
    i4A, i4B, shared = [], [], []
    for sp in SETTING_ORDER:
        x, y = (sp, "F1"), (sp, "F2")
        i4A.append(len(W6.phi_set(inters[x], inters[y])))
        i4B.append(len(W6.phi_set(inters[x], inters[y], items=LIST_B,
                                  isos=W6.iso_maps(inters[x], inters[y],
                                                   SCOPE["admitted"]))))
        shared.append(sum(1 for ta in inters[x].tokens for tb in inters[y].tokens
                          if W6.same_partition(ta.part, tb.part)))
    anchor("A13", "v12/note-w6-record-coreference.md M4 "
           "[v12/code/w6_output.txt:145]",
           "|Phi_A| and |Phi_B| at the intermediate slice, per setting",
           ([1] * 6, [0] * 6), (i4A, i4B))
    anchor("A14", "v12/note-w6-record-coreference.md M4",
           "shared record subalgebra at the intermediate time, per setting",
           [0] * 6, shared)
    diffs = []
    for sp in SETTING_ORDER:
        t2a, t2b = M.propagators(sp, "F1")[1], M.propagators(sp, "F2")[1]
        ks = set(t2a) | set(t2b)
        diffs.append(sum(1 for kk in ks
                         if t2a.get(kk, K.zero) != t2b.get(kk, K.zero)))
    anchor("A15", "v12/note-w6-record-coreference.md control 4 "
           "[v12/code/w6_output.txt:113]",
           "differing entries of the intermediate propagators, per setting",
           [270, 270, 432, 432, 108, 432], diffs)

    # -- W6's deepest finding: the realized legs and U_prep's 35 columns ----
    t2sup, realmaps = [], []
    for sp in SETTING_ORDER:
        rl, sup2 = {}, {}
        for fr in ("F1", "F2"):
            legs, supp = realized_legs(sp, fr)
            rl[fr] = legs
            sup2[fr] = frozenset(supp[2])
        t2sup.append((sup2["F1"] == sup2["F2"], len(sup2["F1"]),
                      len(sup2["F2"])))
        row = []
        for lv in ("exact", "sign", "born"):
            rc = {}
            for fr in ("F1", "F2"):
                a8, b8 = SETTINGS[sp]
                tA = W6.Token("R_A", PARTA, VALS, 1 if fr == "F1" else 2,
                              cprov("A", a8))
                tB = W6.Token("R_B", PARTB, VALS, 2 if fr == "F1" else 1,
                              cprov("B", b8))
                rc[fr] = W6.Chart("%s/%s@real" % (sp, fr), K, NC, rl[fr], J0,
                                  [tA, tB])
            isos = W6.iso_maps(rc["F1"], rc["F2"], SCOPE["admitted"], level=lv)
            row.append(sorted(tuple(sorted(t.items()))
                              for t in W6.phi_set(rc["F1"], rc["F2"],
                                                  items=LIST_B, isos=isos)))
        realmaps.append(row)
    anchor("A16", "v12/note-w6-record-coreference.md WHAT GROUNDS A TOKEN "
           "LABEL [v12/code/w6_output.txt:135]",
           "the two frames' time-2 occupied supports never coincide, "
           "with their sizes",
           [(False, 2, 8), (False, 2, 8), (False, 8, 8), (False, 8, 8),
            (False, 2, 2), (False, 8, 8)], t2sup)
    SW2 = ((0, 1), (1, 0))
    anchor("A17", "v12/note-w6-record-coreference.md WHAT GROUNDS A TOKEN "
           "LABEL [v12/code/w6_output.txt:137]",
           "token maps admitted by the REALIZED legs alone "
           "(exact / sign / Born), per setting",
           [[[], [], []]] * 4 + [[[], [SW2], [SW2]]] * 2,
           [[[tuple(x) for x in lv] for lv in row] for row in realmaps])
    Up = M.U_prep()
    Uw = W6.sp_conj(Up, WSWAP)

    def colof(A, j):
        return {i: v for (i, jj), v in A.items() if jj == j}
    negcol = {j: {i: K.neg(v) for i, v in colof(Up, j).items()}
              for j in range(NC)}
    oth = range(1, NC)
    anchor("A18", "v12/note-w6-record-coreference.md WHAT GROUNDS A TOKEN "
           "LABEL [v12/code/w6_output.txt:139]",
           "w.U_prep.w against U_prep: the j0 column (+,-), the "
           "other 35 as a block (+,-), then column by column",
           (False, True, False, False, 9, 8),
           (colof(Uw, 0) == colof(Up, 0), colof(Uw, 0) == negcol[0],
            all(colof(Uw, j) == colof(Up, j) for j in oth),
            all(colof(Uw, j) == negcol[j] for j in oth),
            sum(1 for j in oth if colof(Uw, j) == colof(Up, j)),
            sum(1 for j in oth if colof(Uw, j) == negcol[j])))
    # A19 REPAIRED (R3-F7): the never-occupied block is computed FROM
    # OCCUPANCY -- the columns of U_prep that no chart's process ever reads,
    # i.e. the configurations never occupied at the time U_prep acts --
    # instead of from the carrier size.
    occ_at_prep = set()
    for sp in SETTING_ORDER:
        for fr in ("F1", "F2"):
            occ_at_prep |= set(chart_at(sp, fr, FINAL_TIME).dist(0))
    anchor("A19", "v12/note-w6-record-coreference.md WHAT GROUNDS A TOKEN "
           "LABEL", "the never-occupied block of U_prep, computed from "
           "occupancy: the columns U_prep is never applied to",
           35, NC - len(occ_at_prep))

    # -- paper 2's terminal descent machinery, reused not forked ------------
    phi_set3 = {(a, b): ((0,),) for a in range(3) for b in range(3) if a != b}
    r_set = P2.solve_descent([1, 1, 1], phi_set3, [((0,),)] * 3)
    S2 = tuple(tuple(p) for p in itertools.permutations(range(2)))
    phi_g = {(a, b): S2 for a in range(3) for b in range(3) if a != b}
    r_g = P2.solve_descent([2, 2, 2], phi_g, [S2, S2, S2])
    r_u = P2.solve_descent([2, 2, 2], phi_g, [((0, 1),)] * 3)
    id2, sw2 = (0, 1), (1, 0)
    phi_tw = {(0, 1): (id2,), (1, 0): (id2,), (1, 2): (id2,), (2, 1): (id2,),
              (0, 2): (sw2,), (2, 0): (sw2,)}
    r_tw = P2.solve_descent([2, 2, 2], phi_tw, [((0, 1),)] * 3)
    phi_ms = dict(phi_tw)
    phi_ms[(0, 2)] = ()
    r_ms = P2.solve_descent([2, 2, 2], phi_ms, [((0, 1),)] * 3)
    anchor("A20", "v12/paper2_code/RUN.txt section 3",
           "paper 2's four descent verdicts (set / groupoid / "
           "underdetermined / twisted / missing)",
           ("SET-AMALGAM", "GROUPOID-AMALGAM", "UNDERDETERMINED",
            "NO-DESCENT", "ABSENT-PAIR"),
           (r_set.verdict, r_g.verdict, r_u.verdict, r_tw.verdict,
            r_ms.verdict))
    anchor("A21", "v12/paper2_code/RUN.txt section 3",
           "paper 2's groupoid model: families, orbits, stabiliser, "
           "injective colimit",
           (4, 1, 2, True), (r_g.coherent_families, r_g.gauge_orbits,
                             r_g.representative_stabilizer,
                             r_g.injective_colimit))
    anchor("A22", "v12/paper2_code/RUN.txt section 4",
           "no canonical map survives independent S2 automorphisms",
           0, len(P2.canonical_maps(S2, S2, S2)))
    A2c, B_id, B_swap, Pperm = P2M.counterfactual_completion_charts()
    anchor("A23", "v12/paper2_code/RUN.txt section 5",
           "paper 2's completion witness: realized candidate counts, full "
           "isomorphism counts, and the two opposite full token maps",
           (4, 4, 1, 1, (0, 1), (1, 0)),
           (len(P2.realized_isomorphisms(A2c, B_id)),
            len(P2.realized_isomorphisms(A2c, B_swap)),
            len(P2.full_isomorphisms(A2c, B_id)),
            len(P2.full_isomorphisms(A2c, B_swap)),
            P2.full_isomorphisms(A2c, B_id)[0][1],
            P2.full_isomorphisms(A2c, B_swap)[0][1]))
    anchor("A24", "v12/paper2_code/RUN.txt section 5",
           "the swap completion is generated by the declared permutation P",
           Pperm, P2.full_isomorphisms(A2c, B_swap)[0][0])

    # -- W5's LTP-forcing lemma, recomputed on the committed model ----------
    #    W5 states it at the declared intermediate time; the anchors are read
    #    there, and the same residual is then computed at EVERY read time as
    #    a measurement of this unit's own (below).
    res = ltp_residuals()
    r2 = res[2]
    anchor("A25", "v12/note-w5-barandes-recast.md section 3.3 (G6)",
           "the LTP residual weight ||r||_0 of 36 at the six settings, "
           "frame F1 then F2, at the declared intermediate time",
           ([0, 0, 16, 16, 0, 16], [0, 0, 16, 16, 0, 16]),
           ([r2[(sp, "F1")]["nonzero"] for sp in SETTING_ORDER],
            [r2[(sp, "F2")]["nonzero"] for sp in SETTING_ORDER]))
    anchor("A26", "v12/note-w5-barandes-recast.md section 3.3 (G4)",
           "every column of the matrix residual that differs at all differs "
           "in exactly 16 entries (W5's 'the same fact, seen once per "
           "column'), at the three violated settings, both frames",
           {16},
           set().union(*[set(r2[(sp, fr)]["per_column"])
                         for sp in ("SP-C", "SP-D", "SP-F")
                         for fr in ("F1", "F2")]))
    anchor("A27", "v12/note-w5-barandes-recast.md section 3.3 (G5, G5b)",
           "the SP-C and SP-F residual censuses: (distinct values, rational "
           "entries of 16)",
           ((4, 0), (6, 8)),
           ((r2[("SP-C", "F1")]["distinct"], r2[("SP-C", "F1")]["rational"]),
            (r2[("SP-F", "F1")]["distinct"], r2[("SP-F", "F1")]["rational"])))
    gate("O4-COMPLETION-DISCLOSURE", "disclosure",
         "A DECLARED DIVERGENCE FROM A COMMITTED COUNT, AND WHY.  W5's A3 "
         "prints the divisibility census (0,0,576,576,0,576) -- 16 differing "
         "entries in every one of the 36 columns.  Recomputed on THIS base's "
         "preparation operator the count is measured to be smaller, because "
         "W5 rebuilt the model from the singlet dictionary and chose a "
         "different orthogonal completion of U_prep off the j0 column.  The "
         "j0 COLUMN -- the only column the model's own admissible p(0) ever "
         "reads, and the one W5's G1 says carries the whole residual -- "
         "agrees exactly (A25), as do both value censuses (A27) and A26's "
         "completion-independent form.  What is MEASURED here is therefore "
         "the divergence itself and what survives it: two builds of the SAME "
         "declared j0 column give different matrix counts and the same vector "
         "count, so the matrix census is completion-dependent and the vector "
         "census is not, and W5's A3/G4 matrix count is not determined by "
         "anything W5 anchors.  No claim is entered here about W6's own "
         "quantity: the base's note states in terms that its finding is NOT "
         "an artifact of U_prep's arbitrary orthogonal completion, so this "
         "divergence is not carried as a second confirmation of it",
         True,
         {"committed_bc2_matrix_count": 576,
          "recomputed_on_this_base":
              [r2[(sp, "F1")]["matrix_differing"] for sp in SETTING_ORDER],
          "columns_that_differ":
              [len(r2[(sp, "F1")]["per_column"]) for sp in SETTING_ORDER],
          "per_column_differing_counts":
              sorted(set().union(*[set(r2[(sp, "F1")]["per_column"])
                                   for sp in ("SP-C", "SP-D", "SP-F")])),
          "j0_column_agrees_with_the_committed_count": True})
    TABLES["ltp_residuals"] = {
        "t=%d" % t: {"%s/%s" % k: {kk: vv for kk, vv in v.items()
                                   if kk != "vector"}
                     for k, v in sorted(res[t].items())}
        for t in READ_TIMES}
    return res


def ltp_residuals():
    """W5's declared-law residual D(t) = Gamma(T<-0) - Gamma(T<-t)
    Gamma(t<-0), evaluated on the model's own admissible p(0) = delta_{j0}
    and, separately, as a matrix -- AT EVERY DECLARED READ TIME t, so that
    the lemma is read at the same coordinate as the fact-data.  Exact in
    Q(cos pi/8); the rational entries are detected by the field's own
    rationality test, never by a tolerance."""
    out = {t: {} for t in READ_TIMES}
    for sp in SETTING_ORDER:
        for fr in ("F1", "F2"):
            T = M.propagators(sp, fr)
            legs = list(M.legs(sp, fr))
            g30 = W6.sp_born(K, T[NLEGS - 1])
            for t in READ_TIMES:
                gt0 = W6.sp_born(K, T[t - 1])
                acc = W6.sp_id(K, NC)
                for L in legs[t:]:
                    acc = W6.sp_mul(K, L, acc)
                g3t = W6.sp_born(K, acc)
                comp = (W6.sp_mul(K, gt0, g3t) if MUTANT == "anchor-ltp"
                        else W6.sp_mul(K, g3t, gt0))
                keys = set(g30) | set(comp)
                percol: dict = {}
                for (i, j) in keys:
                    if g30.get((i, j), K.zero) != comp.get((i, j), K.zero):
                        percol[j] = percol.get(j, 0) + 1
                mdiff = sum(percol.values())
                vec = {}
                for i in range(NC):
                    d = K.sub(g30.get((i, J0), K.zero),
                              comp.get((i, J0), K.zero))
                    if not K.is_zero(d):
                        vec[i] = d
                if MUTANT == "ltp-lax":
                    vec = {}
                vals = sorted({canon(v) for v in vec.values()})
                # RATIONALITY, by the field's own test: `to_rat` returns the
                # rational value of an element of Q inside K and None
                # otherwise.  No tolerance and no float is involved.
                rat = sum(1 for v in vec.values() if K.to_rat(v) is not None)
                out[t][(sp, fr)] = {
                    "nonzero": len(vec), "matrix_differing": mdiff,
                    "distinct": len(vals), "rational": rat,
                    "per_column": sorted(percol.values()),
                    "values": vals, "vector": vec}
    return out


# ===========================================================================
# 7.  THE TRANSPORT INSTRUMENT: the ten gates, applied identically to every
#     fact-class AT A DECLARED READ TIME.  Every function below takes the
#     read time as an explicit argument; none of them can read one class at
#     one time and another at another, and the like-for-like gate measures
#     that in the data themselves.
# ===========================================================================
def _perms_for(cand):
    return SCOPE[cand["perms"]]


def _chart_and_datum(fid, fn, sp, fr, t, **kw):
    return _memo(("cd", fid, sp, fr, t, canon(sorted(kw.items()))),
                 lambda: fn(sp, fr, t, **kw))


def _realized_of_raw(chart):
    supp = [{chart.j0}]
    acc = W6.sp_id(K, chart.n)
    for L in chart.legs:
        acc = W6.sp_mul(K, L, acc)
        supp.append({i for (i, j), v in acc.items()
                     if j == chart.j0 and not K.is_zero(v)})
    legs = [_restrict_in_time(L, supp[t + 1], supp[t])
            for t, L in enumerate(chart.legs)]
    toks = [W6.Token(t.tid, t.part, t.values, t.write_leg, t.prov)
            for t in chart.tokens]
    c = W6.Chart(chart.name + "@real", K, chart.n, legs, chart.j0, toks)
    c.lk = getattr(chart, "lk", chart.name) + "@real"
    return c


def realized_of(chart):
    """The REALIZED restriction of any chart, computed from the chart's own
    legs and initial configuration: each leg restricted to the configurations
    the process actually occupies before and after it.  Built through W6's
    own constructor, so occurrence, availability and the law are recomputed
    from the restricted legs.  Taking the chart as the argument -- rather
    than a (setting, frame) key -- is what lets EVERY gate, including the
    triple, carry a switched, relabelled or re-indexed presentation through
    the realized restriction as well."""
    return _realized_of_raw(chart)


def apply_rule(cand, ca, cb, where="edge"):
    """THE CANDIDATE'S OWN RULE, applied to a pair of charts.  Every gate
    reaches its charts through this one function, so no gate can be computed
    under another candidate's rule; `O4-CANDIDATE-RULE-CONSISTENCY` measures
    that by comparing two gates that must see the same object, and the
    `triple-unrealized` mutant restores the reviewed defect -- the declared
    triple computed without the candidate's own restriction while the edge
    gates keep it -- and must die there."""
    if MUTANT == "triple-unrealized" and where == "triple":
        return ca, cb
    if cand.get("realized"):
        return realized_of(ca), realized_of(cb)
    return ca, cb


def edge_transports(cand, fid, fn, ka, kb, t, **kw):
    """Phi for one ordered edge, one candidate, one fact-class, one time."""
    ca, da = _chart_and_datum(fid, fn, ka[0], ka[1], t, **kw)
    cb, db = _chart_and_datum(fid, fn, kb[0], kb[1], t, **kw)
    ca, cb = apply_rule(cand, ca, cb)
    return TRANSPORT[fid](ca, da, cb, db, _perms_for(cand), cand["level"],
                          cand["order_free"], cand["drop_identity"])


def pair_transports(cand, fid, ca, da, cb, db):
    """Phi for an explicitly built pair of charts (the corridor gates)."""
    ca, cb = apply_rule(cand, ca, cb)
    return TRANSPORT[fid](ca, da, cb, db, _perms_for(cand), cand["level"],
                          cand["order_free"], cand["drop_identity"])


def five_valued(n, scope_a, scope_b, instrument=True):
    """W6's own five-valued discriminator, reused so that the vocabulary is
    emitted rather than typed.  An EMPTY carrier set is called VACUOUS, not
    FORCED -- which is what the record class's carrier set is at the read
    times before its tokens are written."""
    return W6.verdict_of(n, scope_a, scope_b, instrument=instrument)


def _carriers(fid, sp, fr, t):
    """The class's carrier count at a coordinate, fed to the discriminator:
    the live record tokens for F-REC, the 36 configuration propositions for
    the two configuration-carrier classes."""
    if fid != "F-REC":
        return NC
    c, _d = _chart_and_datum(fid, datum_rec, sp, fr, t)
    return len(c.live("available"))


def class_gate_row(cand, fid, fn, t):
    """THE TEN GATES for one (candidate, fact-class, read time), measured."""
    res: dict = {"read_time": t}
    counts, verdicts, rtimes = {}, {}, set()
    for sp in SETTING_ORDER:
        ka, kb = (sp, "F1"), (sp, "F2")
        n = len(edge_transports(cand, fid, fn, ka, kb, t))
        counts[sp] = n
        _ca, da = _chart_and_datum(fid, fn, sp, "F1", t)
        _cb, db = _chart_and_datum(fid, fn, sp, "F2", t)
        rtimes.add(da["read_time"])
        rtimes.add(db["read_time"])
        verdicts[sp] = five_valued(n, _carriers(fid, sp, "F1", t),
                                   _carriers(fid, sp, "F2", t))
    res["counts"] = counts
    res["verdicts"] = verdicts
    res["datum_read_times"] = sorted(rtimes)
    res["EXIST"] = all(v >= 1 for v in counts.values()) and \
        all(verdicts[sp] != "VACUOUS" for sp in SETTING_ORDER)
    res["FORCED"] = all(verdicts[sp] == "FORCED" for sp in SETTING_ORDER)

    # -- INV: the inverse of an admitted transport is admitted in reverse ---
    inv_ok = True
    for sp in SETTING_ORDER:
        fwd = edge_transports(cand, fid, fn, (sp, "F1"), (sp, "F2"), t)
        bwd = set(edge_transports(cand, fid, fn, (sp, "F2"), (sp, "F1"), t))
        for x in fwd:
            if tuple(sorted((b, a) for a, b in x)) not in bwd:
                inv_ok = False
    res["INV"] = inv_ok and res["EXIST"]

    # -- TRI / GLUE on the declared triple {F1, F2, F2^pi} at SP-A ---------
    tri = triple_descent(cand, fid, fn, t)
    res["triple"] = tri
    res["TRI"] = tri["verdict"] not in ("NO-DESCENT", "ABSENT-PAIR")
    res["GLUE"] = tri["verdict"] in ("SET-AMALGAM", "GROUPOID-AMALGAM")

    # -- CERT: the transported datum is certified, not merely compatible ---
    cert_by_sp, res["cert_detail"] = certify(fid, fn, t)
    res["cert_per_setting"] = {sp: v["verdict"] for sp, v in
                               res["cert_detail"]["per_setting"].items()}
    res["cert_ok"] = cert_by_sp
    res["CERT"] = all(cert_by_sp.values())

    # -- COVAR / NAMEBLIND / NOSLICE: the corridor, measured ---------------
    res["COVAR"], res["covar_detail"] = covariance(cand, fid, fn, t)
    res["NAMEBLIND"], res["nameblind_detail"] = name_blindness(cand, fid, fn, t)
    res["NOSLICE"], res["noslice_detail"] = no_slice(cand, fid, fn, t)
    return res


TRIPLE_SETTING = SETTING_ORDER[0]


def triple_descent(cand, fid, fn, t):
    """The descent gates on W6's own declared triple: F1, F2 and F2 presented
    on a relabelled configuration set (both qubit flips), built as its OWN
    object, at the read time under audit.  The charts pass through the
    CANDIDATE'S OWN RULE (`apply_rule`) exactly as the edge gates do.  The
    solver is W6's, so its verdict vocabulary is the base's."""
    sp = TRIPLE_SETTING
    pi = W6.build_perm(0, 0, 0, 1, 1)
    names = ["F1", "F2"] if MUTANT == "descent-lax" else ["F1", "F2", "F2pi"]
    spec = {nm: d for nm, d in
            (("F1", {}), ("F2", {}), ("F2pi", {"relabel": pi}))
            if nm in names}
    frame = {"F1": "F1", "F2": "F2", "F2pi": "F2"}
    charts, data = {}, {}
    for nm in names:
        c, d = _chart_and_datum(fid, fn, sp, frame[nm], t, **spec[nm])
        charts[nm], data[nm] = c, d
    phis, auts = {}, {}
    for a, b in itertools.permutations(names, 2):
        ca, cb = apply_rule(cand, charts[a], charts[b], where="triple")
        raw = TRANSPORT[fid](ca, data[a], cb, data[b],
                             _perms_for(cand), cand["level"],
                             cand["order_free"], cand["drop_identity"])
        phis[(a, b)] = [dict(x) for x in raw]
    for nm in names:
        ca, cb = apply_rule(cand, charts[nm], charts[nm], where="triple")
        raw = TRANSPORT[fid](ca, data[nm], cb, data[nm],
                             _perms_for(cand), cand["level"],
                             cand["order_free"], cand["drop_identity"])
        auts[nm] = [dict(x) for x in raw] or [{}]
    out = W6.descent(names, phis, auts)
    out["edge_counts"] = {("%s<-%s" % e): len(v) for e, v in sorted(phis.items())}
    out["aut_counts"] = {nm: len(auts[nm]) for nm in names}
    out["setting"] = sp
    out["read_time"] = t
    return out


def certify(fid, fn, t):
    """CERT, per coordinate, AT THE READ TIME THE CELL DECLARES.  For F-REC
    the certificate is W6's ROUTE-EXT read off the one process: each
    configuration is read through F1's record map and through F2's, and the
    joint law must be supported on the graph of a value-PRESERVING bijection.
    The SAME construction is run for F-CFG and F-CTRL with the class's own
    datum in place of the record value, at the SAME time, so the three
    classes are certified like for like.  The pair guard of W6 is kept: a
    configuration on which the two charts disagree disqualifies the pair.
    W6's DEGENERACY GUARD is kept too, and it is load-bearing here: a joint
    law with fewer than two positive entries certifies nothing and is
    reported VACUOUS -- neither a certificate nor a refusal."""
    per, ok = {}, {}
    for sp in SETTING_ORDER:
        ca, _da = _chart_and_datum(fid, fn, sp, "F1", t)
        cb, _db = _chart_and_datum(fid, fn, sp, "F2", t)
        pa, pb = ca.dist(t), cb.dist(t)
        if fid == "F-REC":
            reader = lambda i: (ca.read(i), cb.read(i))          # noqa: E731
        elif fid == "F-CTRL":
            reader = lambda i: (str(i), str(i))                  # noqa: E731
        else:
            reader = lambda i: (canon(pa.get(i, K.zero)),        # noqa: E731
                                canon(pb.get(i, K.zero)))
        dis = sum(1 for i in range(NC)
                  if pa.get(i, K.zero) != pb.get(i, K.zero))
        joint: dict = {}
        for i, pv in pa.items():
            kk = reader(i)
            joint[kk] = K.add(joint.get(kk, K.zero), pv)
        cert = W6.route_ext_pair(K, joint, dis)
        ok[sp] = cert[0] is True
        per[sp] = {"verdict": str(cert[0]), "positive_entries": cert[1],
                   "bijection_supported": cert[2],
                   "disagreeing_configurations": dis, "read_time": t}
    if MUTANT == "cert-lax":
        ok = {sp: True for sp in SETTING_ORDER}
    return ok, {"route": "EXT", "read_time": t, "per_setting": per}


def covariance(cand, fid, fn, t):
    """COVAR.  The rule is equivariant iff carrying BOTH charts of an edge by
    the same admitted arena element leaves the transport count unchanged, and
    carrying them by a checkpoint-phase switching does the same.  Measured,
    per coordinate, at the read time the cell declares."""
    base, moved_relabel, moved_switch, tested = {}, 0, 0, 0
    for sp in SETTING_ORDER:
        n0 = len(edge_transports(cand, fid, fn, (sp, "F1"), (sp, "F2"), t))
        base[sp] = n0
        for g in arena_group():
            n1 = len(edge_transports(cand, fid, fn, (sp, "F1"), (sp, "F2"),
                                     t, relabel=g))
            tested += 1
            if n1 != n0:
                moved_relabel += 1
        for eps in switchings(NLEGS):
            n2 = len(edge_transports(cand, fid, fn, (sp, "F1"), (sp, "F2"),
                                     t, eps=eps))
            tested += 1
            if n2 != n0:
                moved_switch += 1
    ok = (moved_relabel == 0 and moved_switch == 0)
    if MUTANT == "covar-lax":
        ok, moved_relabel, moved_switch = True, 0, 0
    return ok, {"tested": tested, "relabelling_failures": moved_relabel,
                "switching_failures": moved_switch, "base_counts": base,
                "read_time": t}


NAMEBLIND_PERM = W6.build_perm(0, 0, 0, 1, 1)


def name_blindness(cand, fid, fn, t):
    """NAMEBLIND.  Present ONE chart on a relabelled configuration set (the
    declared gauge of the base) and ask the rule to identify it with the
    chart it is a relabelling OF.  A name-blind rule identifies them; a
    name-reading rule cannot, because the labels are exactly what changed.
    The reference is the rule's own self-transport count on the unrelabelled
    chart, so the gate compares like with like and cannot pass by returning
    zero twice.  This is the gate the negative control F-CTRL exists to
    fail.  [SAMP: one declared relabelling; the whole declared scope is swept
    at the declared representative coordinates in `O4-NAMEBLIND-SWEEP`.]"""
    pi = NAMEBLIND_PERM
    same, moved, detail = 0, 0, {}
    for sp in SETTING_ORDER:
        for fr in ("F1", "F2"):
            ca, da = _chart_and_datum(fid, fn, sp, fr, t)
            cb, db = _chart_and_datum(fid, fn, sp, fr, t, relabel=pi)
            n0 = len(pair_transports(cand, fid, ca, da, ca, da))
            n1 = len(pair_transports(cand, fid, ca, da, cb, db))
            detail["%s/%s" % (sp, fr)] = (n0, n1)
            if n1 == n0 and n0 >= 1:
                same += 1
            else:
                moved += 1
    return moved == 0, {"identified": same, "failed": moved,
                        "per_chart": detail, "read_time": t}


def _datum_key(d):
    """A datum's substantive content, with the read-time bookkeeping field
    removed -- so that comparing two readings of a datum compares the data
    and not the labels of the two readings."""
    return canon({k: v for k, v in d.items() if k != "read_time"})


def no_slice(cand, fid, fn, t):
    """NOSLICE, IN TWO MEASURED CLAUSES.  Re-index ONE chart's time
    coordinate by prepending an identity leg: the process is the same object
    presented on a shifted index, and no transition has been added.

    CLAUSE N (normalisation).  A rule inside the corridor identifies the
    chart with its own re-indexed presentation exactly as it identifies the
    chart with itself.  The reference is the rule's own self-transport count,
    so a rule cannot pass by returning zero twice.  Measured: this clause is
    sensitive to the identity-leg normalisation alone (the sweep in
    `O4-NOSLICE-SENSITIVITY` reports what each clause moves under).

    CLAUSE I (index).  The SAME MOMENT lives at index t+1 in the re-indexed
    presentation and at index t in the original, so reading the INDEX and
    reading the MOMENT are two different readings.  The clause measures that
    difference where it exists: at every chart whose datum is measured to
    differ between the two readings, the rule must NOT identify the
    uncompensated pair as it identifies the compensated one -- a rule that
    does is reading the index, not the moment.  Where the two readings give
    the same datum the probe has no teeth and the chart is declared
    DEGENERATE rather than passed; that is what happens for the name-reading
    control, whose datum has no read time at all, and the count is disclosed.
    This clause is what makes clause N's pass substantive rather than free;
    the `global-now-smuggler` mutant makes every rule read the index and must
    die at the corridor census."""
    same, moved, idx_bound, degen, teeth, detail = 0, 0, 0, 0, 0, {}
    for sp in SETTING_ORDER:
        for fr in ("F1", "F2"):
            ca, da = _chart_and_datum(fid, fn, sp, fr, t)
            cb, db = _chart_and_datum(fid, fn, sp, fr, t, extra_identity=True)
            cc, dc = _chart_and_datum(fid, fn, sp, fr, t, extra_identity=True,
                                      compensate=False)
            n0 = len(pair_transports(cand, fid, ca, da, ca, da))
            n1 = len(pair_transports(cand, fid, ca, da, cb, db))
            n2 = len(pair_transports(cand, fid, ca, da, cc, dc))
            detail["%s/%s" % (sp, fr)] = (n0, n1, n2)
            if n1 == n0 and n0 >= 1:
                same += 1
            else:
                moved += 1
            if _datum_key(db) == _datum_key(dc):
                degen += 1
            elif n2 == n1:
                idx_bound += 1
            else:
                teeth += 1
    return (moved == 0 and idx_bound == 0), {
        "identified": same, "clause_N_failures": moved,
        "clause_I_index_bound": idx_bound,
        "clause_I_discriminating_charts": teeth,
        "clause_I_degenerate_charts": degen, "per_chart": detail,
        "read_time": t}


# ===========================================================================
# 8.  THE LTP GATE (W5's forcing lemma, instantiated per candidate and per
#     READ TIME -- the lemma is evaluated at the same coordinate as the
#     fact-data it is asked about)
# ===========================================================================
def ltp_gate(cand, res, resid, t):
    """What probability law attaches to the actuality this candidate
    transports AT READ TIME t?  COMPUTED, not asserted.

    (i)  The actuality at that time is EXHIBITED: the occupied support and
         its exact law.
    (ii) W5's lemma (c) is evaluated AT THAT TIME on the model's own
         admissible p(0): where the declared-law residual is nonzero, t is
         NOT a division event of the model as declared, so no committed law
         conditions on the transported configuration.  (The lemma is
         one-directional: a vanishing residual does not establish a division
         event, and no such claim is made.)
    (iii) W6's own measurement is carried in at the same time: how many
         declared record partitions have been written in BOTH frames by then.
         Where that count is positive a shared record law does condition on
         the datum, and the LAWFUL branch fires -- which it is measured to do
         at the final declared division event.

    A candidate whose transport is nowhere admitted transports no actuality
    and the gate is NOT-APPLICABLE there."""
    per = {}
    for sp in SETTING_ORDER:
        n = res["counts"][sp]
        forced_bare = resid[t][(sp, "F1")]["nonzero"] > 0 or \
            resid[t][(sp, "F2")]["nonzero"] > 0
        shared = shared_record_at(sp, t)
        if n == 0:
            per[sp] = "NOT-APPLICABLE (no transport admitted)"
        elif forced_bare:
            per[sp] = "LTP-BARE (forced: the read time is not a division "\
                      "event of the model as declared)"
        elif shared > 0:
            per[sp] = "LTP-LAWFUL (a shared record law conditions on the "\
                      "datum)"
        else:
            per[sp] = "LTP-BARE-UNWITNESSED (the residual vanishes, so the "\
                      "forcing lemma does not fire; and the shared record "\
                      "subalgebra at that time is measured empty, so no "\
                      "committed law conditions on the datum either)"
    live = [sp for sp in SETTING_ORDER if res["counts"][sp] > 0]
    bare = [sp for sp in live if per[sp].startswith("LTP-BARE (")]
    unwit = [sp for sp in live if per[sp].startswith("LTP-BARE-UNWITNESSED")]
    lawful = [sp for sp in live if per[sp].startswith("LTP-LAWFUL")]
    if MUTANT == "ltp-stub":
        bare, unwit = [], []
    if not live:
        verdict = "LTP-NOT-APPLICABLE"
    elif bare:
        verdict = "LTP-BARE"
    elif lawful:
        verdict = "LTP-LAWFUL"
    else:
        verdict = "LTP-BARE-UNWITNESSED"
    return {"per_setting": per, "verdict": verdict, "read_time": t,
            "coordinates_with_transport": live,
            "coordinates_forced_bare": bare,
            "coordinates_bare_unwitnessed": unwit,
            "coordinates_lawful": lawful}


_SHARED: dict = {}


def shared_record_at(sp, t):
    """How many declared record partitions have been written in BOTH frames
    by read time t.  W6's own derivation, recomputed here at every declared
    time.  The `ltp-shared-lax` mutant injects a shared partition where the
    base has none -- the reachability witness for the LAWFUL branch, run as a
    falsification probe."""
    if MUTANT == "ltp-shared-lax":
        return 1
    if (sp, t) in _SHARED:
        return _SHARED[(sp, t)]
    ca, cb = chart_at(sp, "F1", t), chart_at(sp, "F2", t)
    _SHARED[(sp, t)] = sum(1 for ta in ca.tokens for tb in cb.tokens
                           if W6.same_partition(ta.part, tb.part))
    return _SHARED[(sp, t)]


def exhibit_actuality():
    """The exhibit the LTP gate rests on, printed as data: at every chart and
    every declared read time, the occupied support, its size, and its exact
    law."""
    out = {}
    for t in READ_TIMES:
        for sp in SETTING_ORDER:
            for fr in ("F1", "F2"):
                _c, d = _chart_and_datum("F-CFG", datum_cfg, sp, fr, t)
                out["t%d %s/%s" % (t, sp, fr)] = {
                    "occupied": sorted(d["actual"]),
                    "size": len(d["actual"]),
                    "law": {str(i): d["law"][i] for i in sorted(d["law"])}}
    return out


# ===========================================================================
# 9.  THE ARENA TEST, AT NAME-FREE MATCHED REPRESENTATIVES (the RQ0 bequest;
#     RD-4).  Each fact-class supplies its quantity in BOTH representative
#     types -- name-indexed and name-free -- so that the relabelling
#     coordinate is measured for what it separates.  A name-indexed object
#     must move under a relabelling and a name-free one cannot: that is a
#     fact about representatives, and crediting it to a fact-class is the
#     error this declaration exists to prevent.
# ===========================================================================
ARENA_COORDS = ("setting", "frame", "relabelling", "switching")


def arena_group():
    """THE ARENA'S ADMITTED ISOMORPHISMS: the base's own declared permutation
    scope filtered by the base's own initial-configuration condition -- W6's
    "the filter admits exactly two of those 72".  Enumerated, never typed.
    The wider declared extension is reported as a disclosure; it is not used
    as the acting group, because it is not closed under its own conjugation
    and an action a candidate's declared search scope does not contain would
    test the scope, not the rule."""
    return SCOPE["admitted"]


def arena_family():
    """The admissible arena, enumerated; every factor computed."""
    nsw = len(switchings(NLEGS))
    frames = len({fr for _sp, fr in CHART_KEYS})
    size = len(SETTING_ORDER) * frames * len(arena_group()) * nsw
    return {"settings": len(SETTING_ORDER), "frames": frames,
            "admitted_isomorphisms": len(arena_group()),
            "checkpoint_phase_switchings": nsw,
            "switching_free_legs": NLEGS, "size": size,
            "read_times": len(READ_TIMES)}


def _truth_cfg_named(sp, fr, g, eps, t):
    """F-CFG, NAME-INDEXED: the 36-bit vector whose i-th entry says whether
    the proposition "the configuration at read time t is i" is true here."""
    _c, d = _chart_and_datum("F-CFG", datum_cfg, sp, fr, t, eps=eps, relabel=g)
    return tuple(1 if i in d["actual"] else 0 for i in range(NC))


def _truth_cfg_free(sp, fr, g, eps, t):
    """F-CFG, NAME-FREE: the same datum with the configuration names
    quotiented out -- the sorted multiset of the exact probabilities on the
    occupied support.  This is the like-for-like counterpart of F-REC's
    value set, built by the same construction that makes F-REC's quantity
    name-free."""
    _c, d = _chart_and_datum("F-CFG", datum_cfg, sp, fr, t, eps=eps, relabel=g)
    if MUTANT == "arena-namemix":
        return tuple(1 if i in d["actual"] else 0 for i in range(NC))
    return tuple(sorted(d["law"][i] for i in sorted(d["actual"])))


def _truth_rec_free(sp, fr, g, eps, t):
    """F-REC, NAME-FREE: the actual record VALUE tuples of the chart at read
    time t, as a set -- carrying no configuration name at all."""
    c, _d = _chart_and_datum("F-REC", datum_rec, sp, fr, t, eps=eps, relabel=g)
    return tuple(sorted(canon(k) for k in c.law))


def _truth_rec_named(sp, fr, g, eps, t):
    """F-REC, NAME-INDEXED: the record-value reading of every configuration
    NAME at read time t -- the record class's quantity in the object's
    representative type."""
    _c, d = _chart_and_datum("F-REC", datum_rec, sp, fr, t, eps=eps, relabel=g)
    return d["read"]


ARENA_QUANTITIES = (
    ("QA1", "F-CFG actuality, NAME-INDEXED (the 36 named propositions)",
     _truth_cfg_named, "THE OBJECT", "F-CFG", "name-indexed"),
    ("QA1f", "F-CFG actuality, NAME-FREE (the law multiset on the support)",
     _truth_cfg_free, "THE OBJECT", "F-CFG", "name-free"),
    ("QA2", "F-REC truth-values, NAME-FREE (the actual record values)",
     _truth_rec_free, "POSITIVE CONTROL", "F-REC", "name-free"),
    ("QA2n", "F-REC truth-values, NAME-INDEXED (the reading of every name)",
     _truth_rec_named, "POSITIVE CONTROL", "F-REC", "name-indexed"),
)


def run_arena():
    """Push both classes' truth-values, in BOTH representative types, through
    the admitted arena action at every declared read time, and measure what
    moves, per coordinate, with orbits computed."""
    prog("arena test: both representative types, every read time")
    rows = []
    for qid, name, fn, role, cls, rep in ARENA_QUANTITIES:
        for t in READ_TIMES:
            vals: dict = {}
            for sp in SETTING_ORDER:
                for fr in ("F1", "F2"):
                    for gi, g in enumerate(arena_group()):
                        for ei, eps in enumerate(switchings(NLEGS)):
                            vals[(sp, fr, gi, ei)] = canon(fn(sp, fr, g, eps, t))
            dep = {}
            for coord, ix in (("setting", 0), ("frame", 1),
                              ("relabelling", 2), ("switching", 3)):
                seen: dict = {}
                for kk, v in vals.items():
                    rest = tuple(x for i, x in enumerate(kk) if i != ix)
                    seen.setdefault(rest, set()).add(v)
                movers = sum(1 for s in seen.values() if len(s) > 1)
                dep[coord] = {"moves": movers > 0, "slices": len(seen),
                              "slices_that_move": movers,
                              "max_distinct_values":
                                  max(len(s) for s in seen.values())}
            base_orbits = {}
            for sp in SETTING_ORDER:
                for fr in ("F1", "F2"):
                    o = {vals[(sp, fr, gi, ei)]
                         for gi in range(len(arena_group()))
                         for ei in range(len(switchings(NLEGS)))}
                    base_orbits["%s/%s" % (sp, fr)] = len(o)
            moved = [c for c in ARENA_COORDS if dep[c]["moves"]]
            if MUTANT == "canon-lax":
                moved = []
            v = ("O4-ARENA-ARTIFACT" if moved else "O4-ARENA-INVARIANT")
            frame_diff = sorted(
                sp for sp in SETTING_ORDER
                if vals[(sp, "F1", 0, 0)] != vals[(sp, "F2", 0, 0)])
            rows.append({"id": qid, "name": name, "role": role,
                         "fact_class": cls, "representative": rep,
                         "read_time": t, "verdict": v, "moved_under": moved,
                         "dependence": dep,
                         "distinct_values_over_family": len(set(vals.values())),
                         "orbit_size_per_chart": base_orbits,
                         "settings_where_the_two_frames_differ": frame_diff})
    TABLES["arena"] = rows
    fam = arena_family()
    TABLES["arena_family"] = fam
    gate("O4-ARENA-FAMILY", "derivation",
         "THE ADMISSIBLE ARENA IS ENUMERATED AND ITS SIZE IS COMPUTED, never "
         "typed: the product of the declared setting count, the frame count, "
         "the admitted isomorphisms surviving the base's own j0 filter, and "
         "the checkpoint-phase switchings read off the declared leg count.  "
         "Every factor is measured from the fixtures.  The `action-weaken` "
         "and `gauge-subsample` mutants shrink a factor and must die here",
         fam["size"] == (fam["settings"] * fam["frames"]
                         * fam["admitted_isomorphisms"]
                         * fam["checkpoint_phase_switchings"])
         and fam["checkpoint_phase_switchings"] == 2 ** fam[
             "switching_free_legs"]
         and fam["admitted_isomorphisms"] == SCOPE["n_admitted"], fam)
    gate("O4-ARENA-TEETH", "control",
         "THE ARENA ACTION HAS TEETH: at least one declared quantity is "
         "MEASURED to move under it.  If nothing moves, the action is too "
         "weak and the census is dead as instrumented.  The `canon-lax` "
         "mutant collapses the canonicaliser so that nothing can be seen to "
         "move, and must die here",
         any(r["moved_under"] for r in rows),
         {"quantities_that_move": [("%s@t%d" % (r["id"], r["read_time"]),
                                    r["moved_under"])
                                   for r in rows if r["moved_under"]]})

    # -- the like-for-like reading of the relabelling coordinate ------------
    def moved_rel(qid, t):
        r = [x for x in rows if x["id"] == qid and x["read_time"] == t][0]
        return "relabelling" in r["moved_under"]
    named = {(q, t): moved_rel(q, t) for q in ("QA1", "QA2n")
             for t in READ_TIMES}
    free = {(q, t): moved_rel(q, t) for q in ("QA1f", "QA2")
            for t in READ_TIMES}
    lfl = (all(named[("QA1", t)] == named[("QA2n", t)] for t in READ_TIMES)
           and all(free[("QA1f", t)] == free[("QA2", t)] for t in READ_TIMES)
           and any(named.values()) and not any(free.values()))
    gate("O4-ARENA-LIKE-FOR-LIKE", "measurement",
         "THE RELABELLING COORDINATE SEPARATES REPRESENTATIVE TYPES, NOT "
         "FACT-CLASSES (RUNBOOK section 15 addendum).  Each class's quantity "
         "is declared in BOTH representative types and swept through the "
         "same action at the same read times.  Measured: the two "
         "NAME-INDEXED quantities agree with each other in the relabelling "
         "coordinate at every read time, the two NAME-FREE quantities agree "
         "with each other, the name-indexed ones move and the name-free ones "
         "do not.  A class contrast drawn in this coordinate is therefore a "
         "representative artifact.  The `arena-namemix` mutant reads names "
         "inside a name-free quantity and must die here",
         lfl,
         {"name_indexed_move_under_relabelling":
              {"%s@t%d" % (q, t): named[(q, t)] for (q, t) in sorted(named)},
          "name_free_move_under_relabelling":
              {"%s@t%d" % (q, t): free[(q, t)] for (q, t) in sorted(free)}})
    return rows


def run_arena_residual(rows, obstruction):
    """RD-4: does the arena test carry any fact the obstruction does not?
    Measured, at name-free matched representatives, by comparing coordinate
    sets rather than by argument."""
    arena_set = set()
    for r in rows:
        if r["id"] == "QA1f":
            for sp in r["settings_where_the_two_frames_differ"]:
                arena_set.add((r["read_time"], sp))
    obs_set = {(t, sp) for (t, sp), v in obstruction.items() if v == 0}
    residual = sorted(arena_set - obs_set)
    gate("O4-ARENA-NO-RESIDUAL", "measurement",
         "THE ARENA TEST CARRIES NO FACT THE OBSTRUCTION DOES NOT, MEASURED. "
         "At name-free matched representatives the coordinates at which the "
         "unrecorded-configuration datum differs between the two frames are "
         "compared with the coordinates at which the two frames' occupied "
         "sets are measured disjoint.  The first set is measured to be a "
         "SUBSET of the second, and a proper one, so the arena reading is "
         "the obstruction restated in truth-value language and weaker: it is "
         "reported once, in section 6, and no second outcome is drawn from "
         "it.  The `arena-namemix` mutant reads names in the name-free "
         "quantity, which puts the relabelling artifact back into the "
         "comparison, and must die here",
         not residual and arena_set < obs_set,
         {"name_free_frame_difference_coordinates":
              sorted("t%d/%s" % c for c in arena_set),
          "obstruction_coordinates": sorted("t%d/%s" % c for c in obs_set),
          "coordinates_the_arena_adds": [str(c) for c in residual],
          "proper_subset": arena_set < obs_set})


# ===========================================================================
# 10.  THE MATCHED TABLE AND THE PER-COORDINATE VERDICTS
#
#      RD-1: three fact-classes x every declared read time x every candidate
#      x every setting, identical gates, one naming convention.  RD-2: the
#      unit verdict is DERIVED from this table and from nothing else.
# ===========================================================================
PREREGISTERED = ("O4-RULE-EXISTS", "O4-RULE-EXISTS-LTP-BARE",
                 "O4-DISCRIMINATED-RECORD-ACTUALISM", "O4-ARENA-RELATIVE",
                 "O4-BLOCKED-AT")

MUST_PASS = ("EXIST", "FORCED", "INV", "TRI", "GLUE", "CERT")
CORRIDOR = ("COVAR", "NAMEBLIND", "NOSLICE")


def corridor_failures(row_cfg, row_rec, row_ctrl):
    """THE CORRIDOR CONSTRAINS THE RULE, NOT THE CLASS, so covariance and the
    no-slice gate are read on EVERY class the rule is applied to -- reading
    them on F-CFG alone would let a rule admitting nothing pass vacuously,
    which is W6's own emptiness guard.  NAME-BLINDNESS is the one gate that
    is a property of the (rule, class) pair rather than of the rule: the
    negative control is DEFINED as the class that reads names, so its failure
    there is the control firing and not the rule leaving the corridor.  That
    carve-out is declared, and the corridor census carries both controls."""
    out = []
    for g in CORRIDOR:
        rows = ((row_cfg, row_rec) if g == "NAMEBLIND"
                else (row_cfg, row_rec, row_ctrl))
        if not all(r[g] for r in rows):
            out.append(g)
    return out


def derive_candidate_verdict(cid, row_cfg, row_rec, row_ctrl, ltp, t,
                             declaration=None):
    """THE VERDICT, DERIVED FROM MEASUREMENT, PER COORDINATE (section 15),
    at ONE read time, with the classes read at that same time.

    The candidate's own declared corridor claim and LTP claim are NOT
    consulted: they survive as bookkeeping annotation only, and the flip-test
    gate proves the derivation is independent of them.

    A candidate leaving the declared corridor at this read time is blocked
    outright there.  Otherwise each setting receives its own verdict, decided
    by the gates each class is measured to pass AT THAT COORDINATE -- so the
    comparison is like for like in every coordinate -- and the blocking
    object, where nothing passes, is NAMED from the measurement."""
    if MUTANT == "declaration-lax" and declaration is not None:
        if declaration.get("corridor_claim", "").startswith("GLOBAL-SLICE"):
            return "O4-BLOCKED-AT-<the global slice the rule requires>", {}
    corridor_fail = corridor_failures(row_cfg, row_rec, row_ctrl)
    if corridor_fail:
        return ("O4-BLOCKED-AT-<%s: the rule leaves the declared corridor>"
                % "/".join(corridor_fail)), {"corridor_failures": corridor_fail}

    def passes(row, sp):
        ok = (row["verdicts"][sp] == "FORCED" and row["cert_ok"][sp])
        if sp == TRIPLE_SETTING:            # the declared triple lives here
            ok = ok and row["TRI"] and row["GLUE"]
        return ok

    def why_not(row, sp):
        if row["verdicts"][sp] == "VACUOUS":
            return "the class has no carriers at this coordinate"
        if row["verdicts"][sp] != "FORCED":
            return "no unique transport (%s)" % row["verdicts"][sp]
        if row["cert_per_setting"][sp] == "DISAGREEMENT":
            return "the certificate refuses the pair"
        if row["cert_per_setting"][sp] == "VACUOUS":
            return ("the certificate is degenerate: the transported datum "
                    "takes one value on the whole occupied support")
        return "the declared triple does not descend"

    per, why = {}, {}
    for sp in SETTING_ORDER:
        cfg_ok, rec_ok = passes(row_cfg, sp), passes(row_rec, sp)
        if cfg_ok and ltp["per_setting"][sp].startswith("LTP-LAWFUL"):
            per[sp] = "O4-RULE-EXISTS"
        elif cfg_ok:
            per[sp] = "O4-RULE-EXISTS-LTP-BARE"
        elif rec_ok:
            per[sp] = "O4-DISCRIMINATED-RECORD-ACTUALISM"
            why[sp] = why_not(row_cfg, sp)
        else:
            per[sp] = ("O4-BLOCKED-AT-<%s>" % why_not(row_cfg, sp))
            why[sp] = why_not(row_rec, sp)
    order, seen = [], set()
    for sp in SETTING_ORDER:
        if per[sp] not in seen:
            seen.add(per[sp])
            order.append(per[sp])
    headline = " + ".join(
        "%s [%s]" % (v, ",".join(sp for sp in SETTING_ORDER if per[sp] == v))
        for v in order)
    return headline, {"per_setting": per, "obstructions": why, "read_time": t}


def run_matched_table(resid):
    """THE MATCHED TABLE (RD-1): every fact-class at every declared read time
    under every candidate rule, through the identical gate set."""
    prog("the matched table: %d candidates x %d classes x %d read times"
         % (len(CANDIDATES), len(FACT_CLASSES), len(READ_TIMES)))
    table, ltps = {}, {}
    for cand in CANDIDATES:
        for t in READ_TIMES:
            prog("  %s %s at read time %d" % (cand["id"], cand["name"], t))
            rows = {}
            for fid, _desc, fn, _role in FACT_CLASSES:
                rows[fid] = class_gate_row(cand, fid, fn, t)
            table[(cand["id"], t)] = rows
            ltps[(cand["id"], t)] = ltp_gate(cand, rows["F-CFG"], resid, t)
    TABLES["matched_table"] = {
        "%s@t%d" % (cid, t): {
            fid: {g: rows[fid][g] for g, _c in DESCENT_GATES if g in rows[fid]}
            for fid in rows} for (cid, t), rows in table.items()}
    TABLES["matched_table_counts"] = {
        "%s@t%d" % (cid, t): {
            fid: {"counts": rows[fid]["counts"],
                  "discriminator": rows[fid]["verdicts"],
                  "certificate": rows[fid]["cert_per_setting"],
                  "datum_read_times": rows[fid]["datum_read_times"]}
            for fid in rows} for (cid, t), rows in table.items()}
    TABLES["matched_table_detail"] = {
        "%s@t%d" % (cid, t): {
            fid: {k: v for k, v in rows[fid].items()
                  if k not in [g for g, _ in DESCENT_GATES]}
            for fid in rows} for (cid, t), rows in table.items()}
    TABLES["ltp_gate"] = {"%s@t%d" % k: v for k, v in ltps.items()}
    cells = len(table) * len(FACT_CLASSES)
    gate("O4-MATCHED-TABLE", "derivation",
         "THE MATCHED TABLE IS COMPLETE AND ITS CELLS ARE COUNTED, NEVER "
         "TYPED.  Every fact-class is measured at every declared read time "
         "under every declared candidate rule through the identical gate "
         "set; the cell count is the product of the declared candidate, "
         "class and read-time counts -- the read-time count itself gated "
         "against the declared leg count, so a table computed at fewer "
         "coordinates than the model declares cannot pass -- and every cell "
         "carries every gate key.  This is the object the unit verdict is "
         "derived from, and the `table-clip` mutant, which computes it at one "
         "coordinate fewer, must die here",
         cells == len(CANDIDATES) * len(FACT_CLASSES) * len(READ_TIMES)
         and len(READ_TIMES) == NLEGS
         and all(set(g for g, _c in DESCENT_GATES) - {"LTP"} <= set(r)
                 for rows in table.values() for r in rows.values()),
         {"cells": cells, "candidates": len(CANDIDATES),
          "fact_classes": len(FACT_CLASSES), "read_times": len(READ_TIMES),
          "declared_read_times": NLEGS,
          "gate_cells": cells * (len(DESCENT_GATES) - 1)})
    return table, ltps


# ===========================================================================
# 11.  THE CAUSE, MEASURED (RD-3): the obstruction as a RELATION between the
#      two occupied sets, the clause that actually excludes each admitted
#      map, and the read-time structure that decides transportability.
# ===========================================================================
def occupied_sets():
    """The occupied support of every chart at every declared read time."""
    out = {}
    for t in READ_TIMES:
        for sp in SETTING_ORDER:
            for fr in ("F1", "F2"):
                _c, d = _chart_and_datum("F-CFG", datum_cfg, sp, fr, t)
                out[(t, sp, fr)] = (frozenset(d["actual"]),
                                    {i: d["law"][i] for i in d["actual"]})
    return out


def pair_census(occ):
    """K1, COMPLETED BEYOND THE COMMITTED PAIRS (the panel's strengthening):
    all unordered pairs of the twelve charts at every read time, split into
    cross-frame and same-frame."""
    out = {}
    keys = [(sp, fr) for sp in SETTING_ORDER for fr in ("F1", "F2")]
    for t in READ_TIMES:
        cross = cross_dis = same = same_share = 0
        for i in range(len(keys)):
            for j in range(i + 1, len(keys)):
                a, b = keys[i], keys[j]
                sa = occ[(t, a[0], a[1])][0]
                sb = occ[(t, b[0], b[1])][0]
                if a[1] != b[1]:
                    cross += 1
                    cross_dis += 1 if not (sa & sb) else 0
                else:
                    same += 1
                    same_share += 1 if (sa & sb) else 0
        out[t] = {"cross_frame_pairs": cross, "cross_frame_disjoint": cross_dis,
                  "same_frame_pairs": same, "same_frame_sharing": same_share}
    return out


def orbit_relation(occ):
    """THE OBSTRUCTION AS A RELATION.  For every read time and setting: are
    the two frames' occupied sets one orbit of the base's own admitted wing
    exchange, does that element preserve the exact law, and -- where they are
    not one orbit -- is the disjointness cardinality-forced?"""
    out = {}
    for t in READ_TIMES:
        for sp in SETTING_ORDER:
            s1, l1 = occ[(t, sp, "F1")]
            s2, l2 = occ[(t, sp, "F2")]
            carried = {WSWAP[i] for i in s2} == set(s1)
            lawpres = carried and all(l1.get(WSWAP[i]) == l2.get(i)
                                      for i in s2)
            out[(t, sp)] = {
                "sizes": (len(s1), len(s2)),
                "intersection": len(s1 & s2),
                "one_orbit_of_the_admitted_wing_exchange": carried,
                "wing_exchange_preserves_the_exact_law": bool(lawpres),
                "cardinality_forced_disjoint":
                    len(s1) != len(s2) and not (s1 & s2)}
    return out


def clause_census(cand, t):
    """WHICH CLAUSE EXCLUDES THE MAP.  The F-CFG transport predicate is four
    successive clauses -- the j0 filter, leg compatibility, the actual-set
    clause and the law clause -- and this census reports, for each admitted
    isomorphism of the base, the FIRST clause that excludes it.  It is what
    turns "the transport dies" into "the transport dies HERE"."""
    out = {}
    perms = _perms_for(cand)
    named = {canon(list(IDPERM)): "identity", canon(list(WSWAP)): "wing swap"}
    for sp in SETTING_ORDER:
        ca, da = _chart_and_datum("F-CFG", datum_cfg, sp, "F1", t)
        cb, db = _chart_and_datum("F-CFG", datum_cfg, sp, "F2", t)
        ca, cb = apply_rule(cand, ca, cb)
        rows = {}
        for pidx, p in enumerate(perms):
            nm = named.get(canon(list(p)))
            if nm is None:
                continue
            if p[cb.j0] != ca.j0:
                rows[nm] = "j0"
            elif not legs_compatible(ca, cb, p, cand["level"],
                                     cand["order_free"],
                                     cand["drop_identity"], pidx):
                rows[nm] = "legs"
            elif {p[i] for i in db["actual"]} != set(da["actual"]):
                rows[nm] = "actual-set"
            elif any(da["law"].get(p[i]) != db["law"].get(i)
                     for i in range(NC)):
                rows[nm] = "law"
            else:
                rows[nm] = "ADMITTED"
        out[sp] = rows
    return out


def prefix_alignment(level):
    """THE READ-TIME STRUCTURE.  Do the two frames' DECLARED LEG PREFIXES up
    to a read time match order-free at a declared level?  The two frames of
    one experiment differ exactly by the order of two commuting legs, so
    their prefixes coincide before either local event and again after both,
    and differ strictly between: at the second read time each frame has
    performed a DIFFERENT local event, so the two charts' index-2 moments are
    not the same moment."""
    out = {}
    for t in READ_TIMES:
        for sp in SETTING_ORDER:
            la = list(M.legs(sp, "F1"))[:(NLEGS if MUTANT == "prefix-lax"
                                          else t)]
            lb = list(M.legs(sp, "F2"))[:(NLEGS if MUTANT == "prefix-lax"
                                          else t)]
            out[(t, sp)] = any(
                all(W6.leg_match(K, lb[x], la[sg[x]], level)
                    for x in range(len(la)))
                for sg in itertools.permutations(range(len(la))))
    return out


def run_cause(table, resid):
    """RD-3: the obstruction disclosed as a relation and GATED as one; and
    RD-2's bequest -- what actually decides transportability across the read
    times, measured against the divisibility residual."""
    prog("the cause: orbit relation, clause census, read-time structure")
    occ = occupied_sets()
    census = pair_census(occ)
    orb = orbit_relation(occ)
    obstruction = {(t, sp): orb[(t, sp)]["intersection"]
                   for t in READ_TIMES for sp in SETTING_ORDER}
    clauses = {"%s@t%d" % (c["id"], t): clause_census(c, t)
               for c in CANDIDATES for t in OBJECT_TIMES}
    TABLES["occupied_supports"] = {
        "t%d %s/%s" % (t, sp, fr): sorted(occ[(t, sp, fr)][0])
        for t in READ_TIMES for sp in SETTING_ORDER for fr in ("F1", "F2")}
    TABLES["pair_census"] = {"t=%d" % t: v for t, v in census.items()}
    TABLES["orbit_relation"] = {"t%d/%s" % k: v for k, v in orb.items()}
    TABLES["clause_census"] = clauses

    t_obs = [t for t in READ_TIMES
             if all(orb[(t, sp)]["intersection"] == 0 for sp in SETTING_ORDER)]
    one_orbit = [sp for sp in SETTING_ORDER
                 for t in t_obs
                 if orb[(t, sp)]["one_orbit_of_the_admitted_wing_exchange"]]
    forced = [sp for sp in SETTING_ORDER for t in t_obs
              if not orb[(t, sp)]["one_orbit_of_the_admitted_wing_exchange"]]
    # every setting at which the two sets are NOT one orbit must have its
    # disjointness cardinality-forced: that is the structural implication
    # this gate measures, rather than the bare zero.
    forced_ok = all(orb[(t, sp)]["cardinality_forced_disjoint"]
                    for t in t_obs for sp in forced)
    census_ok = all(census[t]["cross_frame_disjoint"]
                    == census[t]["cross_frame_pairs"]
                    and census[t]["same_frame_sharing"]
                    == census[t]["same_frame_pairs"] for t in t_obs)
    # and the clause that excludes the wing swap for the corridor-bound,
    # full-leg rules is measured to be the LEG clause, not the support clause
    legs_kill = {cid: {sp: clauses[cid][sp].get("wing swap")
                       for sp in SETTING_ORDER}
                 for cid in clauses if cid.startswith(("C2@", "C2X@", "C3@"))}
    legs_ok = all(v == "legs" for row in legs_kill.values()
                  for v in row.values())
    gate("O4-CAUSE-MEASURED", "measurement",
         "THE OBSTRUCTION IS MEASURED AS A RELATION, NOT AS A BARE ZERO.  At "
         "the read time at which the two frames' occupied sets are disjoint, "
         "the gate measures (i) that EVERY cross-frame pair of the twelve "
         "charts is disjoint there and EVERY same-frame pair shares, so the "
         "disjointness tracks the frame coordinate exactly and is not an "
         "artifact of the committed pair; (ii) that at the settings where "
         "the two sets are ONE ORBIT of the base's own admitted wing "
         "exchange the disjointness is a statement about that group element, "
         "and that wherever they are not one orbit the disjointness is "
         "CARDINALITY-FORCED, which is the structural implication a bare "
         "intersection count cannot carry; and (iii) that for the "
         "corridor-bound rules matching the FULL declared legs the wing "
         "exchange is excluded by the LEG clause -- one clause earlier than "
         "the support -- so the disjointness is decisive through the "
         "certificate rather than through the transport predicate.  The "
         "`support-lax` mutant reads the datum at the wrong time and must "
         "die here",
         bool(t_obs) and census_ok and forced_ok and legs_ok,
         {"read_times_at_which_every_cross_frame_pair_is_disjoint": t_obs,
          "pair_census": {"t=%d" % t: census[t] for t in READ_TIMES},
          "settings_that_are_one_orbit_of_the_wing_exchange":
              sorted(set(one_orbit)),
          "settings_where_disjointness_is_cardinality_forced":
              sorted(set(forced)),
          "law_preserving_at": sorted(
              sp for t in t_obs for sp in SETTING_ORDER
              if orb[(t, sp)]["wing_exchange_preserves_the_exact_law"]),
          "clause_excluding_the_wing_swap_for_the_full_leg_rules": legs_kill})

    # -- what C4's admitted transport IS -----------------------------------
    c4 = [c for c in CANDIDATES if c["id"] == "C4"][0]
    c4map = {}
    for t in READ_TIMES:
        for sp in SETTING_ORDER:
            tr = edge_transports(c4, "F-CFG", datum_cfg, (sp, "F1"),
                                 (sp, "F2"), t)
            c4map["t%d/%s" % (t, sp)] = [
                ("the wing exchange" if [b for _a, b in x] == list(WSWAP)
                 else "the identity" if [b for _a, b in x] == list(IDPERM)
                 else "another admitted permutation") for x in tr]
    gate("O4-C4-MAP-NAMED", "measurement",
         "THE ONE ADMITTED F-CFG TRANSPORT IS NAMED, NOT JUST COUNTED.  "
         "Where the realized-only rule admits a transport of the unrecorded "
         "class, the admitted permutation is identified against the base's "
         "own group elements.  It is measured to be the WING EXCHANGE -- the "
         "element the base's deepest finding is about -- and not the "
         "identity, so what it delivers is a re-identification of "
         "configurations rather than a co-reference of them",
         all(all(x == "the wing exchange" for x in v)
             for v in c4map.values() if v),
         {"C4_admitted_maps": {k: v for k, v in c4map.items() if v}})

    # -- RD-2's bequest: what decides transportability across read times ----
    align = prefix_alignment("born")
    # THE RULES THIS COMPARISON IS ABOUT, selected from the declarations and
    # not by hand: the corridor-bound candidates that match the FULL declared
    # legs (no realized restriction).  The realized-restriction rule matches a
    # different leg list, so a statement about the declared leg prefix is not
    # a statement about it, and its own profile is reported alongside.
    full_leg = [c["id"] for c in CANDIDATES
                if not c.get("realized")
                and not c["corridor_claim"].startswith("GLOBAL-SLICE")]
    realized = [c["id"] for c in CANDIDATES if c.get("realized")]
    transports = {(t, sp): table[(full_leg[0], t)]["F-CFG"]["counts"][sp] > 0
                  for t in READ_TIMES for sp in SETTING_ORDER}
    full_leg_agree = all(
        (table[(cid, t)]["F-CFG"]["counts"][sp] > 0) == transports[(t, sp)]
        for cid in full_leg for t in READ_TIMES for sp in SETTING_ORDER)
    realized_profile = {"%s@t%d" % (cid, t):
                        [table[(cid, t)]["F-CFG"]["counts"][sp]
                         for sp in SETTING_ORDER]
                        for cid in realized for t in READ_TIMES}
    resid_zero = {(t, sp): (resid[t][(sp, "F1")]["nonzero"] == 0
                            and resid[t][(sp, "F2")]["nonzero"] == 0)
                  for t in READ_TIMES for sp in SETTING_ORDER}
    agree_prefix = [k for k in transports if transports[k] == align[k]]
    agree_resid = [k for k in transports if transports[k] == resid_zero[k]]
    # the sharpest pair: equal residual, opposite transport, same setting
    flips = sorted("%s: t=%d transports=%s / t=%d transports=%s at "
                   "||r||_0=%d both" % (
                       sp, t1, transports[(t1, sp)], t2, transports[(t2, sp)],
                       resid[t1][(sp, "F1")]["nonzero"])
                   for sp in SETTING_ORDER
                   for t1 in OBJECT_TIMES for t2 in OBJECT_TIMES
                   if t1 < t2
                   and resid[t1][(sp, "F1")]["nonzero"]
                   == resid[t2][(sp, "F1")]["nonzero"]
                   and transports[(t1, sp)] != transports[(t2, sp)])
    TABLES["read_time_structure"] = {
        "rules_compared": full_leg,
        "realized_restriction_profile": realized_profile,
        "prefix_alignment": {"t%d/%s" % k: v for k, v in align.items()},
        "transports": {"t%d/%s" % k: v for k, v in transports.items()},
        "residual_vanishes": {"t%d/%s" % k: v for k, v in resid_zero.items()},
        "equal_residual_opposite_transport": flips}
    gate("O4-PREFIX-DECIDES", "measurement",
         "TRANSPORTABILITY IS DECIDED BY THE LEG PREFIX, NOT BY THE "
         "DIVISIBILITY RESIDUAL -- measured on the same cells, and scoped to "
         "the rules the statement is about.  The rules compared are the "
         "corridor-bound candidates that match the FULL declared legs, "
         "selected from the declarations; they are measured to agree with "
         "each other at every cell.  For every (read time, setting) the gate "
         "compares three profiles: whether those rules transport the "
         "unrecorded class there, whether the two frames' declared leg "
         "PREFIXES up to that time match order-free, and whether W5's "
         "divisibility residual vanishes there.  The prefix profile is "
         "measured to agree with the transport profile at EVERY cell; the "
         "residual profile is measured NOT to, and the witnesses are "
         "exhibited: at the same setting and at IDENTICAL residual weight, "
         "the two intermediate read times have opposite transport verdicts.  "
         "Transportability therefore does not reduce to the divisibility "
         "residual.  The realized-restriction rule matches a RESTRICTED leg "
         "list, so this statement is not about it and its own profile is "
         "printed here rather than folded in: it is measured constant in the "
         "read time and carried by the wing exchange.  The `prefix-lax` "
         "mutant -- which reads the whole leg list instead of the prefix -- "
         "must die here",
         full_leg_agree and len(agree_prefix) == len(transports)
         and len(agree_resid) < len(transports) and bool(flips),
         {"cells": len(transports), "rules_compared": full_leg,
          "the_compared_rules_agree_at_every_cell": full_leg_agree,
          "realized_restriction_profile": realized_profile,
          "cells_where_the_prefix_profile_agrees": len(agree_prefix),
          "cells_where_the_residual_profile_agrees": len(agree_resid),
          "equal_residual_opposite_transport": flips})
    return obstruction


# ===========================================================================
# 12.  CONTROLS -- both directions, with teeth, at matched coordinates
# ===========================================================================
def trunc_reading(cand, fid, t):
    """THE SECOND READING OF "READ AT TIME t": the base's own truncated
    process (the first t declared legs) carrying the tokens written by then,
    instead of the full declared process carrying the visible record set.
    Computed so that the read-time construction is anchored against an
    independent reading of the same words rather than declared."""
    out = []
    for sp in SETTING_ORDER:
        chs = {}
        for fr in ("F1", "F2"):
            a8, b8 = SETTINGS[sp]
            tA = W6.Token("R_A", PARTA, VALS, 1 if fr == "F1" else 2,
                          cprov("A", a8))
            tB = W6.Token("R_B", PARTB, VALS, 2 if fr == "F1" else 1,
                          cprov("B", b8))
            toks = [tk for tk in (tA, tB) if tk.write_leg + 1 <= t]
            chs[fr] = W6.Chart("%s/%s@trunc%d" % (sp, fr, t), K, NC,
                               list(M.legs(sp, fr))[:t], J0, toks)
        ca, cb = chs["F1"], chs["F2"]
        if fid == "F-REC":
            da = {"carriers": len(ca.tokens)}
            db = {"carriers": len(cb.tokens)}
        else:
            pa, pb = ca.dist(t), cb.dist(t)
            da = {"carriers": NC, "actual": frozenset(pa),
                  "law": {i: canon(pa[i]) for i in pa}}
            db = {"carriers": NC, "actual": frozenset(pb),
                  "law": {i: canon(pb[i]) for i in pb}}
        out.append(len(TRANSPORT[fid](ca, da, cb, db, _perms_for(cand),
                                      cand["level"], cand["order_free"],
                                      cand["drop_identity"])))
    return out


def run_controls(table, ltps, arena_rows):
    prog("controls: matched-coordinate positive, negative and corridor")
    c2 = [c for c in CANDIDATES if c["id"] == "C2"][0]

    # -- the read-time construction, anchored against a second reading -----
    two_readings = {}
    for fid in ("F-REC", "F-CFG"):
        for t in READ_TIMES:
            two_readings["%s@t%d" % (fid, t)] = {
                "full_declared_process_with_the_visible_record_set":
                    [table[("C2", t)][fid]["counts"][sp]
                     for sp in SETTING_ORDER],
                "the_truncated_process": trunc_reading(c2, fid, t)}
    agree = sum(1 for v in two_readings.values()
                for a, b in zip(v["full_declared_process_with_the_visible_"
                                  "record_set"], v["the_truncated_process"])
                if a == b)
    total = sum(len(v["the_truncated_process"]) for v in two_readings.values())
    gate("O4-READ-TIME-ROBUST", "measurement",
         "THE READ-TIME CONSTRUCTION IS NOT A CHOICE THE RESULT DEPENDS ON.  "
         "\"Read at time t\" is computed two independent ways -- the full "
         "declared process carrying the record set visible at t (this "
         "unit's), and the base's own truncated process on its first t legs "
         "(W6's, the construction its M4 control uses) -- and the two are "
         "measured to agree in every cell of both substantive classes at "
         "every declared read time.  The `chart-time-lax` mutant drops the "
         "read time from the record set and must die here",
         agree == total and total > 0,
         {"cells": total, "cells_agreeing": agree,
          "per_cell": two_readings})

    # -- the positive control, at the coordinate where it is green ---------
    pos = table[("C2", FINAL_TIME)]["F-REC"]
    mid = {t: table[("C2", t)]["F-REC"]["counts"] for t in OBJECT_TIMES}
    gate("O4-CTRL-POS", "control",
         "THE POSITIVE CONTROL FIRES AT ITS OWN COORDINATE, AND IS MEASURED "
         "ABSENT AT THE OTHERS.  Routed through THIS unit's transport "
         "instrument -- the same ten gates, the same discriminator, the same "
         "solver -- the record class reproduces W6's terminal descent "
         "results at the FINAL declared division event: a transport exists "
         "and is FORCED at every one of the six committed settings, the "
         "inverse law holds, and the declared triple descends.  At the "
         "intermediate read times the same class is measured to have no "
         "transport at all, which is the base's own A13 (|Phi_B| = 0 at the "
         "intermediate slice) reproduced through this instrument.  The "
         "`rec-uncut` mutant leaves the record-level tie uncut and must die "
         "here",
         pos["EXIST"] and pos["FORCED"] and pos["INV"] and pos["GLUE"]
         and all(v == 0 for t in OBJECT_TIMES if t > 1
                 for v in mid[t].values()),
         {"final_time_counts": pos["counts"],
          "final_time_discriminator": pos["verdicts"],
          "intermediate_time_counts": {"t=%d" % t: mid[t] for t in mid},
          "triple": pos["triple"]["verdict"],
          "triple_families": pos["triple"]["families"],
          "triple_orbits": pos["triple"]["orbits"],
          "triple_triples": pos["triple"]["triples"]})

    # -- the negative control ----------------------------------------------
    neg_fails = {"%s@t%d" % (cid, t):
                 [g for g in MUST_PASS + CORRIDOR
                  if not table[(cid, t)]["F-CTRL"][g]]
                 for (cid, t) in table}
    if MUTANT == "ctrl-pass":
        neg_fails = {k: [] for k in neg_fails}
    passed_all = [k for k, f in neg_fails.items() if not f]
    nb_fail = {"%s@t%d" % (cid, t): not table[(cid, t)]["F-CTRL"]["NAMEBLIND"]
               for (cid, t) in table}
    gate("O4-CTRL-NEG", "control",
         "THE NEGATIVE CONTROL FAILS, AS IT MUST, AT EVERY MATCHED "
         "COORDINATE.  The mis-conventioned name-reading class is put "
         "through the IDENTICAL gates at every candidate and every read time "
         "and is measured to fail at least one of them everywhere.  Its "
         "tooth is measured to be the right one: it fails NAME-BLINDNESS -- "
         "the gate its mis-convention was built to fail -- under every "
         "candidate at every read time, including where it admits a "
         "transport.  A pass here would mean the instrument cannot tell a "
         "fact from a name (the ACTION-TOO-WEAK analogue).  The `ctrl-pass` "
         "mutant makes it pass and must die here",
         not passed_all and all(nb_fail.values()),
         {"failed_gates_per_cell": neg_fails,
          "cells_where_the_control_passed": passed_all,
          "name_blindness_fails_at_every_cell": all(nb_fail.values())})

    # -- like-for-like, SEMANTIC: the coordinates, not the signatures -------
    rt_ok, rt_detail = True, {}
    for (cid, t), rows in table.items():
        seen = {fid: rows[fid]["datum_read_times"] for fid in rows}
        cert_t = {fid: rows[fid]["cert_detail"]["read_time"] for fid in rows}
        ok = (all(v == [t] for v in seen.values())
              and all(v == t for v in cert_t.values()))
        rt_detail["%s@t%d" % (cid, t)] = {"datum_read_times": seen,
                                          "certificate_read_time": cert_t,
                                          "matched": ok}
        rt_ok = rt_ok and ok
    gate("O4-LIKE-FOR-LIKE", "derivation",
         "THE THREE CLASSES ARE GATED LIKE FOR LIKE IN EVERY COORDINATE, NOT "
         "MERELY IN THEIR SIGNATURES (RUNBOOK section 15 addendum).  Every "
         "fact-class is routed through the SAME ten gates by the same code "
         "path with the same signature -- and, the clause that matters, the "
         "READ TIME at which each class's datum was evaluated is carried in "
         "the datum itself and measured EQUAL across the three classes, and "
         "equal to the cell's declared read time, in every cell of the "
         "matched table, including inside the certificate.  A class-versus-"
         "class contrast whose classes are read at different times is a "
         "coordinate effect in disguise; this gate is what makes that "
         "impossible here.  The `readtime-conflate` mutant reads the record "
         "class at the final time whatever the cell declares -- the defect "
         "the panel found -- and must die here, as must `likeforlike-lax`",
         rt_ok
         and all(set(g for g, _c in DESCENT_GATES) - {"LTP"}
                 <= set(table[k][fid]) for k in table for fid in table[k])
         and len({(TRANSPORT[f].__code__.co_argcount,
                   tuple(TRANSPORT[f].__code__.co_varnames[:8]))
                  for f in TRANSPORT}) == 1,
         {"gate_keys": [g for g, _c in DESCENT_GATES],
          "classes": sorted(TRANSPORT),
          "read_time_match_per_cell": rt_detail})

    # -- one candidate's gates are computed under that candidate's rule -----
    cons, cons_detail = True, {}
    for (cid, t), rows in table.items():
        cand = [c for c in CANDIDATES if c["id"] == cid][0]
        for fid in rows:
            tri = rows[fid]["triple"]
            e = tri["edge_counts"].get("F1<-F2")
            n = rows[fid]["counts"][TRIPLE_SETTING]
            cons_detail["%s@t%d/%s" % (cid, t, fid)] = {
                "triple_edge_F1<-F2": e, "edge_gate_count": n, "equal": e == n}
            cons = cons and (e == n)
    gate("O4-CANDIDATE-RULE-CONSISTENCY", "derivation",
         "EVERY GATE OF A CANDIDATE IS COMPUTED UNDER THAT CANDIDATE'S OWN "
         "RULE.  The declared triple and the edge gates measure the same "
         "object on the same pair at the same setting and read time, so "
         "their F1<-F2 counts must agree cell by cell; where a gate reached "
         "its charts without the candidate's declared restriction the two "
         "would diverge.  This is the check that was missing when the "
         "realized-only rule's triple was computed under another "
         "candidate's rule, and the `triple-unrealized` mutant restores that "
         "defect and must die here",
         cons, {"cells": len(cons_detail), "per_cell": cons_detail})

    # -- the corridor census, per read time --------------------------------
    inside, outside, why_out = [], [], {}
    for (cid, t), rows in sorted(table.items()):
        f = corridor_failures(rows["F-CFG"], rows["F-REC"], rows["F-CTRL"])
        if f:
            outside.append("%s@t%d" % (cid, t))
            why_out["%s@t%d" % (cid, t)] = f
        else:
            inside.append("%s@t%d" % (cid, t))
    gate("O4-CORRIDOR-CENSUS", "control",
         "THE CORRIDOR GATES HAVE BOTH CONTROLS, AT EVERY READ TIME.  At "
         "least one declared candidate is MEASURED to lie inside the pin's "
         "corridor -- covariant under the admitted arena action, name-blind "
         "under the declared gauge, and blind to a pure time re-indexing in "
         "both of the no-slice clauses, on every fact-class -- and at least "
         "one is MEASURED to lie outside it.  A corridor every candidate "
         "passes tests nothing, and a corridor no candidate passes tests "
         "only the corridor.  The `name-reader` and `global-now-smuggler` "
         "mutants empty the inside; a waived gate empties the outside",
         bool(inside) and bool(outside),
         {"inside": inside, "outside": outside, "why_outside": why_out})

    # -- the no-slice gate's own sensitivity, measured ---------------------
    sens = {}
    for level in ("exact", "sign", "born"):
        for of in (False, True):
            for di in (False, True):
                probe = dict(c2)
                probe.update({"level": level, "order_free": of,
                              "drop_identity": di})
                _ok, det = no_slice(probe, "F-CFG", datum_cfg,
                                    OBJECT_TIMES[-1])
                sens["%s/order_free=%s/drop_identity=%s" % (level, of, di)] = {
                    "clause_N_failures": det["clause_N_failures"],
                    "clause_I_index_bound": det["clause_I_index_bound"],
                    "clause_I_discriminating_charts":
                        det["clause_I_discriminating_charts"]}
    nsens = {k: v["clause_N_failures"] == 0 for k, v in sens.items()}
    gate("O4-NOSLICE-SENSITIVITY", "disclosure",
         ("WHAT EACH NO-SLICE CLAUSE IS SENSITIVE TO, SWEPT AND DISCLOSED.  "
          "The gate is run at all %d combinations of the declared matching "
          "levels, the order-free stipulation and the identity-leg "
          "normalisation, the count computed from the sweep itself.  "
          % len(sens)) +
         "Clause N is measured sensitive to the identity-leg "
         "normalisation alone -- it is the leg-normalisation clause, and the "
         "corridor's order-free stipulation is NOT what it tests -- while "
         "clause I is the clause that measures index-reading and is what "
         "bites the global-now smuggler.  Disclosed so that the gate's scope "
         "is on the page rather than inferred from its name",
         True, {"sweep": sens, "clause_N_passes": nsens})

    # -- the level census --------------------------------------------------
    lev = {}
    for level in ("exact", "sign", "born"):
        probe = dict(c2)
        probe["level"] = level
        ok, det = covariance(probe, "F-REC", datum_rec, FINAL_TIME)
        lev[level] = {"switching_failures": det["switching_failures"],
                      "relabelling_failures": det["relabelling_failures"],
                      "covariant": ok}
    gate("O4-LEVEL-CENSUS", "measurement",
         "THE CORRIDOR SELECTS THE MATCHING LEVEL, MEASURED.  The same rule "
         "is run at all three of the base's declared matching levels and its "
         "invariance under the checkpoint-phase switchings is measured at "
         "each.  The EXACT amplitude level is measured NOT invariant -- the "
         "switchings are exactly the amplitude gauge -- while the SIGN and "
         "BORN levels are measured invariant.  This row is what makes the "
         "corridor's covariance clause a measurement rather than a "
         "stipulation, and the `sign-flip` mutant, which matches at the sign "
         "level on the nose, must die here",
         (not lev["exact"]["covariant"] and lev["sign"]["covariant"]
          and lev["born"]["covariant"]), lev)

    # -- the certificate's three outcomes, all exhibited --------------------
    cert_out, cert_recon = {}, True
    for (cid, t), rows in sorted(table.items()):
        for fid in ("F-REC", "F-CFG", "F-CTRL"):
            for sp in SETTING_ORDER:
                if rows[fid]["cert_ok"][sp] != (
                        rows[fid]["cert_per_setting"][sp] == "True"):
                    cert_recon = False
        if cid != "C2":
            continue
        for fid in ("F-REC", "F-CFG", "F-CTRL"):
            cert_out["%s@t%d" % (fid, t)] = rows[fid]["cert_per_setting"]
    kinds = {v for row in cert_out.values() for v in row.values()}
    gate("O4-CERT-BITES", "control",
         "THE CERTIFICATE FIRES, REFUSES AND DECLARES ITSELF DEGENERATE -- "
         "all three outcomes exhibited on measured pairs.  The identical "
         "ROUTE-EXT construction certifies the record pair at the final "
         "declared division event at every setting, REFUSES both substantive "
         "classes at the second intermediate read time at every setting "
         "(where the two charts disagree on a configuration), and reports "
         "VACUOUS -- W6's own degeneracy guard -- where the datum takes one "
         "value on the whole occupied support.  A certificate that never "
         "fails would certify nothing; one that never succeeds would be an "
         "instrument defect rather than a finding.  The gate reads the "
         "certificate's own verdict strings AND the booleans the gate row "
         "carries, and measures them reconciled cell by cell, so a waived "
         "certificate cannot pass by leaving the strings intact: the "
         "`cert-lax` mutant waives it and must die here",
         cert_recon and {"True", "DISAGREEMENT", "VACUOUS"} <= kinds
         and all(v == "True" for v in cert_out["F-REC@t%d" % FINAL_TIME].values())
         and all(v == "DISAGREEMENT"
                 for t in OBJECT_TIMES if t > 1
                 for v in cert_out["F-CFG@t%d" % t].values()),
         {"per_class_and_time": cert_out, "outcomes_exhibited": sorted(kinds),
          "booleans_reconciled_with_the_verdict_strings": cert_recon})

    tri = table[("C2", FINAL_TIME)]["F-REC"]["triple"]
    gate("O4-TRIPLE-EXERCISED", "control",
         "THE TRIPLE LAW IS GENUINELY EXERCISED.  The declared triple is the "
         "base's own: the two frames plus the second frame presented on a "
         "relabelled configuration set, built as its OWN object with its own "
         "legs, its own initial configuration and its law recomputed.  At "
         "the control coordinate all six ordered edges and all six ordered "
         "triples are measured to carry a transport, so the cocycle law has "
         "something to reject.  The `descent-lax` mutant drops the third "
         "chart and must die here",
         tri["edges"] == 6 and tri["triples"] == 6
         and all(v >= 1 for v in tri["edge_counts"].values()),
         {"edges": tri["edges"], "triples": tri["triples"],
          "edge_counts": tri["edge_counts"],
          "automorphism_counts": tri["aut_counts"],
          "verdict": tri["verdict"], "families": tri["families"],
          "orbits": tri["orbits"], "setting": tri["setting"],
          "read_time": tri["read_time"]})

    # -- vacuity and degeneracy, declared ----------------------------------
    vac = {"%s@t%d" % (cid, t): {
        fid: [sp for sp in SETTING_ORDER
              if rows[fid]["verdicts"][sp] == "VACUOUS"] for fid in rows}
        for (cid, t), rows in sorted(table.items())}
    deg = {"%s@t%d" % (cid, t): {
        fid: [sp for sp in SETTING_ORDER
              if rows[fid]["cert_per_setting"][sp] == "VACUOUS"]
        for fid in rows} for (cid, t), rows in sorted(table.items())}
    gate("O4-VACUITY-DISCLOSURE", "disclosure",
         "EVERY VACUOUS AND EVERY DEGENERATE CELL IS DECLARED AS ONE.  A "
         "class with no carriers at a coordinate is VACUOUS there and is "
         "never counted as passing: the discriminator emits the word and the "
         "verdict derivation requires FORCED, not merely a count of one.  "
         "The record class has no carriers before its tokens are written, "
         "and the certificate is degenerate wherever the transported datum "
         "takes a single value on the whole occupied support; both lists are "
         "printed here rather than rendered as passes",
         True, {"vacuous_discriminator_cells": vac,
                "degenerate_certificate_cells": deg})

    # -- the name-blindness sweep over the WHOLE declared scope -------------
    sweep = {}
    for cid in ("C2", "C3"):
        cand = [c for c in CANDIDATES if c["id"] == cid][0]
        perms = _perms_for(cand)
        for fid, fn in FACT_CLASSES_BY_ID.items():
            t = FINAL_TIME if fid == "F-REC" else OBJECT_TIMES[-1]
            ca, da = _chart_and_datum(fid, fn, TRIPLE_SETTING, "F1", t)
            n0 = len(pair_transports(cand, fid, ca, da, ca, da))
            good = 0
            for g in perms:
                cb, db = _chart_and_datum(fid, fn, TRIPLE_SETTING, "F1", t,
                                          relabel=g)
                if len(pair_transports(cand, fid, ca, da, cb, db)) == n0 >= 1:
                    good += 1
            sweep["%s/%s@t%d" % (cid, fid, t)] = {
                "scope": len(perms), "identified_at": good}
    gate("O4-NAMEBLIND-SWEEP", "disclosure",
         "NAME-BLINDNESS OVER THE WHOLE DECLARED SCOPE, not one relabelling. "
         "The gate itself is decided at one declared relabelling [SAMP]; "
         "this row sweeps the entire declared permutation scope at the "
         "declared representative coordinates and reports how many elements "
         "the rule identifies the relabelled chart under.  The corridor "
         "verdict is measured uniform over the scope, and the negative "
         "control is measured to survive only at the trivial element",
         True, {"sweep": sweep})
    return None


FACT_CLASSES_BY_ID = {i: f for i, _d, f, _r in FACT_CLASSES}


def run_ltp_gates(table, ltps):
    """The LTP clause is a MANDATORY gate of the pin, so it carries its own
    falsification coverage: one gate reconciles the aggregate against the
    per-setting strings, and one measures that the LAWFUL branch is reachable
    and where it fires."""
    recon, ok = {}, True
    for key, lt in sorted(ltps.items()):
        per = lt["per_setting"]
        live = [sp for sp in SETTING_ORDER
                if not per[sp].startswith("NOT-APPLICABLE")]
        if not live:
            expect = "LTP-NOT-APPLICABLE"
        elif any(per[sp].startswith("LTP-BARE (") for sp in live):
            expect = "LTP-BARE"
        elif any(per[sp].startswith("LTP-LAWFUL") for sp in live):
            expect = "LTP-LAWFUL"
        else:
            expect = "LTP-BARE-UNWITNESSED"
        recon["%s@t%d" % key] = {"aggregate": lt["verdict"],
                                 "reconciled_from_the_per_setting_strings":
                                     expect, "equal": expect == lt["verdict"]}
        ok = ok and (expect == lt["verdict"])
    gate("O4-LTP-RECONCILED", "measurement",
         "THE LTP GATE HAS FALSIFICATION COVERAGE OF ITS OWN.  The pin makes "
         "the LTP clause mandatory, so the aggregate verdict of every "
         "(candidate, read time) cell is re-derived from that cell's own "
         "per-setting strings by a second reader and measured equal.  A "
         "stubbed selector that empties the bare list while the per-setting "
         "strings still name it is exactly what this reconciliation catches, "
         "and the `ltp-stub` mutant -- which stubs the selector and nothing "
         "else -- must die here",
         ok, {"cells": len(recon), "per_cell": recon})

    lawful = sorted(k for k, lt in ltps.items() if lt["coordinates_lawful"])
    lawful_obj = [k for k in lawful if k[1] in OBJECT_TIMES]
    shared = {"t=%d" % t: [shared_record_at(sp, t) for sp in SETTING_ORDER]
              for t in READ_TIMES}
    gate("O4-LTP-LAWFUL-WITNESSED", "measurement",
         "THE LAWFUL BRANCH IS REACHABLE, AND WHERE IT FIRES IS MEASURED.  A "
         "verdict the instrument cannot emit is no verdict, so the branch is "
         "witnessed rather than asserted: the shared record subalgebra is "
         "measured EMPTY at both intermediate read times and POSITIVE at the "
         "final declared division event, and the gate fires LTP-LAWFUL there "
         "and nowhere before it.  So `never obtains at the intermediate "
         "times` is a measured negative on this base, not a structural "
         "impossibility of the selector, and the `ltp-shared-lax` mutant -- "
         "which injects a shared record partition where the base has none, "
         "the reachability injection run as a falsification probe -- makes "
         "the branch fire at the intermediate times and must die here",
         bool(lawful) and not lawful_obj,
         {"cells_emitting_LTP-LAWFUL": ["%s@t%d" % k for k in lawful],
          "cells_at_the_object_read_times": ["%s@t%d" % k for k in lawful_obj],
          "shared_record_partitions_per_read_time": shared})


# ===========================================================================
# 13.  THE SELF-TEST -- fresh evaluation, cache-hits gated at zero
# ===========================================================================
def declared_action_size():
    """The DECLARED size of the arena action, enumerated from W6's own
    generators independently of any mutation of the running scope, so that a
    gate on the sweep size cannot shrink in step with the sweep it gates."""
    base = [W6.build_perm(sw, sa, sb, fa, fb)
            for sw in (0, 1) for sa in range(3) for sb in range(3)
            for fa in (0, 1) for fb in (0, 1)]
    return len([p for p in base if p[J0] == J0]), 2 ** NLEGS


def run_selftest(table, resid):
    """RUNBOOK section 14 and its addendum.  The instrument enforces an
    invariance (COVAR under the admitted action), so it carries a self-test
    that measures that invariance under the symmetry's own action, evaluated
    FRESH with the value cache bypassed and the hit count gated at zero."""
    global _FRESH
    prog("self-test: fresh evaluation under the symmetry's own action")
    _FRESH = True
    _CACHE["value_cache_hits"] = 0
    _CACHE["value_cache_misses"] = 0
    tested = failures = discriminating = 0
    per = {}
    for cand in CANDIDATES:
        for t in READ_TIMES:
            for fid, fn in (("F-REC", datum_rec), ("F-CFG", datum_cfg)):
                rel_fail = sw_fail = 0
                for sp in SETTING_ORDER:
                    n0 = len(edge_transports(cand, fid, fn, (sp, "F1"),
                                             (sp, "F2"), t))
                    for g in arena_group():
                        n1 = len(edge_transports(cand, fid, fn, (sp, "F1"),
                                                 (sp, "F2"), t, relabel=g))
                        tested += 1
                        if list(g) != list(IDPERM):
                            discriminating += 1
                        if n1 != n0:
                            rel_fail += 1
                    for eps in switchings(NLEGS):
                        n2 = len(edge_transports(cand, fid, fn, (sp, "F1"),
                                                 (sp, "F2"), t, eps=eps))
                        tested += 1
                        if any(e == -1 for e in eps):
                            discriminating += 1
                        if n2 != n0:
                            sw_fail += 1
                per["%s@t%d/%s" % (cand["id"], t, fid)] = {
                    "relabelling_failures": rel_fail,
                    "switching_failures": sw_fail}
                failures += rel_fail + sw_fail
    hits = _CACHE["value_cache_hits"]
    misses = _CACHE["value_cache_misses"]
    _FRESH = False
    gate("O4-ST-FRESH", "selftest",
         "THE SELF-TEST EVALUATES FRESH.  Every value the symmetry self-test "
         "reads is recomputed with the instrument's value cache bypassed -- "
         "including the leg-compatibility cache, which is the same cache -- "
         "so the phase's cache-HIT count is gated at ZERO and its MISS count "
         "gated positive and the test cannot degenerate to reading one "
         "cached object twice.  The `memo-lax` mutant restores the cache and "
         "must die here",
         hits == 0 and misses > 0,
         {"value_cache_hits": hits, "value_cache_misses": misses})
    n_adm, n_sw = declared_action_size()
    expect = (2 * len(CANDIDATES) * len(READ_TIMES) * len(SETTING_ORDER)
              * (n_adm + n_sw))
    gate("O4-ST-TEETH", "selftest",
         "THE SELF-TEST'S TESTED SET IS FIXED BY DECLARATION, GATED AGAINST "
         "THE DECLARED ARENA, and has teeth.  The set swept is the FULL "
         "declared arena action -- every admitted isomorphism and every "
         "checkpoint-phase switching, at every setting, every candidate and "
         "every declared read time, for both substantive classes -- never a "
         "set selected by the verdicts under audit.  The expected size is "
         "computed from the DECLARED action enumerated independently of the "
         "running scope, so a subsampled action or gauge cannot shrink the "
         "gate in step with the sweep: the `action-weaken` and "
         "`gauge-subsample` mutants must die here",
         discriminating > 0 and tested == expect,
         {"instances_tested": tested, "declared_expected": expect,
          "instances_where_the_action_is_nontrivial": discriminating,
          "declared_admitted_isomorphisms": n_adm,
          "declared_switchings": n_sw, "per_cell": per})
    indep = {"%s@t%d/%s" % (c["id"], t, fid):
             covariance(c, fid, fn, t)[1]
             for c in CANDIDATES for t in READ_TIMES
             for fid, fn in (("F-REC", datum_rec), ("F-CFG", datum_cfg))}
    agree = all(per[c]["relabelling_failures"]
                == indep[c]["relabelling_failures"]
                and per[c]["switching_failures"]
                == indep[c]["switching_failures"] for c in per)
    gate("O4-ST-INVARIANCE", "selftest",
         "THE ENFORCED INVARIANT IS MEASURED UNDER ITS OWN ACTION, AND THE "
         "MEASUREMENT IS RECONCILED.  The instrument enforces equivariance "
         "of the transport count under the admitted arena action; the "
         "self-test recomputes that count FRESH under every element of the "
         "action at every read time, and its per-cell failure counts must "
         "agree with the counts the covariance gate itself recorded.  A gate "
         "that only reported its own number would test nothing; the "
         "`covar-lax` mutant waives the covariance gate's count and must die "
         "here",
         agree, {"total_equivariance_failures": failures,
                 "selftest_per_cell": per,
                 "covariance_gate_per_cell":
                     {c: {k: v for k, v in indep[c].items()
                          if k.endswith("failures")} for c in indep}})
    # -- the declaration flip-test (no declaration-founded verdicts) --------
    flips = {}
    for cand in CANDIDATES:
        for t in READ_TIMES:
            rows = table[(cand["id"], t)]
            ltp = TABLES["_ltps"][(cand["id"], t)]
            true_v, _ = derive_candidate_verdict(
                cand["id"], rows["F-CFG"], rows["F-REC"], rows["F-CTRL"],
                ltp, t)
            flipped = dict(cand)
            flipped["corridor_claim"] = (
                "GLOBAL-SLICE: declared as the gated-out control"
                if not cand["corridor_claim"].startswith("GLOBAL-SLICE")
                else "covariant, name-blind, no global slice")
            flip_v, _ = derive_candidate_verdict(
                cand["id"], rows["F-CFG"], rows["F-REC"], rows["F-CTRL"],
                ltp, t, declaration=flipped)
            flips["%s@t%d" % (cand["id"], t)] = {
                "verdict": true_v, "under_flipped_declaration": flip_v,
                "identical": true_v == flip_v}
    gate("O4-ST-DECLARATION-FLIP", "selftest",
         "NO DECLARATION-FOUNDED VERDICT (the RQ0-SYNTH lesson).  Every "
         "candidate's verdict at every read time is re-derived with its "
         "declared corridor claim FLIPPED to its opposite, and must come out "
         "identical: the derivation reads the measured gate results and "
         "nothing else.  The `declaration-lax` mutant lets the declaration "
         "reach the result and must die here",
         all(v["identical"] for v in flips.values()), flips)
    TABLES["declaration_flip_test"] = flips


# ===========================================================================
# 14.  EXACTNESS
# ===========================================================================
def run_exactness():
    """No float in any substantive path: an AST sweep of this module for
    float literals and for the float() constructor, plus a runtime type sweep
    of every value that reached a gate or an anchor."""
    src = Path(__file__).resolve().read_text()
    tree = ast.parse(src)
    lits, calls = [], []
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, float):
            lits.append(node.lineno)
        if isinstance(node, ast.Call) and getattr(node.func, "id", "") == "float":
            calls.append(node.lineno)
    if MUTANT == "float-lax":
        lits.append(-1)

    def walk(v, depth=0):
        if depth > 8:
            return False
        if isinstance(v, float):
            return True
        if isinstance(v, dict):
            return any(walk(x, depth + 1) for x in v.keys()) or \
                any(walk(x, depth + 1) for x in v.values())
        if isinstance(v, (list, tuple, set, frozenset)):
            return any(walk(x, depth + 1) for x in v)
        return False
    runtime = [g["id"] for g in GATES if walk(g.get("value"))]
    runtime += [a["id"] for a in ANCHORS
                if walk(a["committed"]) or walk(a["computed"])]
    gate("O4-EXACT", "derivation",
         "EXACT ARITHMETIC EVERYWHERE.  An AST sweep of this module finds no "
         "float literal and no call to `float` outside the progress line's "
         "own formatting, and a runtime type sweep finds no float in any "
         "value that reached a gate or an anchor.  The substrate is the "
         "committed model's own totally real quartic field, where tuple "
         "equality IS field equality, and fractions.Fraction",
         not lits and not calls and not runtime,
         {"float_literal_lines": lits, "float_call_lines": calls,
          "rows_carrying_a_float": runtime})


# ===========================================================================
# 15.  THE MUTANT TABLE.  Each mutant is declared with its KIND -- whether it
#      perturbs a COMPUTATION or waives a computed field after the fact --
#      and the split is counted from the declaration, never typed.
# ===========================================================================
MUTANT_DECL = (
    ("anchor-w6", "computation", "the wing exchange replaced by the identity"),
    ("anchor-ltp", "computation", "the residual's composition order flipped"),
    ("sign-flip", "computation", "sign-level matching done on the nose"),
    ("orient-flip", "computation", "the realized restriction read backwards"),
    ("rec-uncut", "computation", "the record-level tie left uncut"),
    ("name-reader", "computation", "a rule that admits only the identity"),
    ("global-now-smuggler", "computation",
     "every rule reads the time index instead of the moment"),
    ("readtime-conflate", "computation",
     "the record class read at the final time whatever the cell declares"),
    ("chart-time-lax", "computation",
     "the record set of a chart taken without its read time"),
    ("triple-unrealized", "computation",
     "the declared triple computed without the candidate's restriction"),
    ("prefix-lax", "computation",
     "the leg prefix read as the whole leg list"),
    ("table-clip", "computation",
     "the matched table computed at one declared read time fewer"),
    ("arena-namemix", "computation",
     "a name-free arena quantity made to read names"),
    ("action-weaken", "computation", "the arena action collapsed"),
    ("gauge-subsample", "computation", "the switching sweep subsampled"),
    ("scope-lax", "computation", "the permutation scope subsampled"),
    ("memo-lax", "computation", "the self-test allowed to read the cache"),
    ("descent-lax", "computation", "the declared triple truncated"),
    ("freeze-lax", "computation", "one fixture datum evaluated before freeze"),
    ("float-lax", "computation", "a float literal introduced"),
    ("support-lax", "computation", "the class datum read at the wrong time"),
    ("ltp-lax", "computation", "the LTP residual vector zeroed"),
    ("ltp-shared-lax", "computation",
     "a shared record partition injected where the base has none"),
    ("likeforlike-lax", "computation",
     "one class's transport given a different signature"),
    ("canon-lax", "waiver", "the arena canonicaliser's mover list emptied"),
    ("covar-lax", "waiver", "the covariance gate's counts waived"),
    ("cert-lax", "waiver", "the certificate waived"),
    ("ctrl-pass", "waiver", "the negative control's failures waived"),
    ("ltp-stub", "waiver", "the LTP selector's bare list stubbed"),
    ("verdict-lax", "waiver", "an out-of-vocabulary verdict emitted"),
    ("declaration-lax", "waiver", "the declaration allowed to reach the "
     "verdict"),
)
MUTANTS = [m[0] for m in MUTANT_DECL]


def run_mutant_table():
    """Every declared mutant is run to completion, must EXIT 1, and must
    falsify at least one NAMED gate or anchor.  The second half of the
    predicate is the one that matters: the set of must-pass gates that NO
    mutant falsifies must be EMPTY."""
    import subprocess
    from concurrent.futures import ThreadPoolExecutor
    prog("mutant table (%d mutants)" % len(MUTANTS))

    def _run(m):
        r = subprocess.run([sys.executable, str(Path(__file__).resolve()),
                            "--mutant", m, "--quiet"],
                           capture_output=True, text=True)
        kill = {"failed_anchors": [], "failed_gates": [], "crashed": True}
        for ln in r.stdout.splitlines():
            if ln.startswith("KILL-JSON "):
                kill = json.loads(ln[len("KILL-JSON "):])
                kill["crashed"] = False
        prog("  %s: exit %d, kills %s" % (m, r.returncode,
                                          kill["failed_anchors"]
                                          + kill["failed_gates"]))
        return {"mutant": m, "exit": r.returncode, "died": r.returncode == 1,
                "falsified_anchors": kill["failed_anchors"],
                "falsified_gates": kill["failed_gates"],
                "crashed_before_reporting": kill["crashed"]}

    with ThreadPoolExecutor(max_workers=8) as ex:
        rows = list(ex.map(_run, MUTANTS))
    kinds = {}
    for m, kind, what in MUTANT_DECL:
        kinds.setdefault(kind, []).append(m)
    for r in rows:
        d = [x for x in MUTANT_DECL if x[0] == r["mutant"]][0]
        r["kind"], r["perturbs"] = d[1], d[2]
    TABLES["mutants"] = rows
    killed = {k for r in rows
              for k in r["falsified_anchors"] + r["falsified_gates"]}
    must = [x["id"] for x in GATES if x["class"] != "disclosure"
            and x["id"] != "O4-MUTANTS"]
    unfalsified = sorted(set(must) - killed)
    TABLES["gate_falsification"] = {
        "must_pass_gates": len(must),
        "falsified_by_some_mutant": len([g for g in must if g in killed]),
        "not_falsified_by_any_mutant": unfalsified,
        "mutant_kinds": {k: len(v) for k, v in sorted(kinds.items())}}
    gate("O4-MUTANTS", "freeze",
         "THE FALSIFICATION SUITE, RUN AND RECORDED, AND EVERY MUST-PASS "
         "GATE FALSIFIED BY AT LEAST ONE MUTANT.  Every declared mutant is "
         "run to completion, must EXIT 1, and must falsify at least one "
         "NAMED gate or anchor; the set of must-pass gates that NO mutant "
         "falsifies must be EMPTY.  Each mutant declares its KIND and the "
         "split is COUNTED from the declaration, never claimed: a "
         "COMPUTATION mutant perturbs a computed quantity, a WAIVER "
         "overwrites a computed field after the fact and proves only that "
         "the gate's predicate is load-bearing for the exit code.  The suite "
         "carries mutants over the reused anchors, the sign and orientation "
         "conventions, the read-time coordinate (a class read at the wrong "
         "time, a record set taken without its time), the candidate-rule "
         "consistency of the declared triple, a name-reader, a global-now "
         "smuggler, a name-mixing arena quantity, a leg-prefix widener, an "
         "action-weakener, a subsampled gauge and scope, a cache-reading "
         "self-test, a stubbed LTP selector, an injected shared record law, "
         "a wrong-time support read, a truncated descent triple, a float, "
         "and waivers of the certificate, the covariance gate, the negative "
         "control, the canonicaliser, the vocabulary and the declaration",
         all(r["died"] and (r["falsified_anchors"] or r["falsified_gates"])
             for r in rows) and len(rows) == len(MUTANTS) and not unfalsified,
         {"mutants": len(rows), "died": sum(1 for r in rows if r["died"]),
          "kinds": {k: len(v) for k, v in sorted(kinds.items())},
          "must_pass_gates_never_falsified": unfalsified,
          "kills": {r["mutant"]: r["falsified_anchors"] + r["falsified_gates"]
                    for r in rows}})


# ===========================================================================
# 16.  THE UNIT VERDICT, DERIVED FROM THE MATCHED TABLE
# ===========================================================================
def run_verdict(table, ltps, arena_rows):
    prog("verdict: per cell of the matched table, then the unit")
    per = {}
    for cand in CANDIDATES:
        for t in READ_TIMES:
            rows = table[(cand["id"], t)]
            v, why = derive_candidate_verdict(
                cand["id"], rows["F-CFG"], rows["F-REC"], rows["F-CTRL"],
                ltps[(cand["id"], t)], t)
            if MUTANT == "verdict-lax":
                v = "O4-UNDECIDED-" + cand["id"]
            per["%s@t%d" % (cand["id"], t)] = {
                "candidate": cand["id"], "name": cand["name"], "read_time": t,
                "verdict": v, "detail": why,
                "ltp": ltps[(cand["id"], t)]["verdict"],
                "F-CFG_counts": rows["F-CFG"]["counts"],
                "F-REC_counts": rows["F-REC"]["counts"],
                "F-CTRL_counts": rows["F-CTRL"]["counts"]}
    TABLES["cell_verdicts"] = per

    # -- the unit verdict, DERIVED from the object's own read times --------
    coords: dict = {}
    for key, row in per.items():
        d = row["detail"]
        if not (isinstance(d, dict) and "per_setting" in d):
            continue
        for sp, v in d["per_setting"].items():
            head = v.split("-<")[0] if v.startswith("O4-BLOCKED-AT-<") else v
            coords.setdefault(head, set()).add((row["candidate"],
                                                row["read_time"], sp))
    obj = {k: sorted(x for x in v if x[1] in OBJECT_TIMES)
           for k, v in coords.items()}
    lawful = obj.get("O4-RULE-EXISTS", [])
    bare = obj.get("O4-RULE-EXISTS-LTP-BARE", [])
    discriminated = obj.get("O4-DISCRIMINATED-RECORD-ACTUALISM", [])
    blocked_reasons: dict = {}
    for key, row in per.items():
        d = row["detail"]
        if not (isinstance(d, dict) and "per_setting" in d):
            continue
        if row["read_time"] not in OBJECT_TIMES:
            continue
        for sp, v in d["per_setting"].items():
            if v.startswith("O4-BLOCKED-AT-<"):
                blocked_reasons.setdefault(row["read_time"], set()).add(
                    v[len("O4-BLOCKED-AT-<"):-1])
    parts = []
    if lawful:
        parts.append("O4-RULE-EXISTS")
    if bare:
        parts.append("O4-RULE-EXISTS-LTP-BARE")
    if discriminated:
        parts.append("O4-DISCRIMINATED-RECORD-ACTUALISM")
    if not parts:
        parts.append("O4-BLOCKED-AT-<the intermediate read times: %s>"
                     % "; ".join("t=%d: %s" % (t, " / ".join(
                         sorted(blocked_reasons[t])))
                         for t in sorted(blocked_reasons)))
    unit = " + ".join(parts)
    if MUTANT == "verdict-lax":
        unit = "O4-UNDECIDED"
    ok_vocab = all(any(p.startswith(x) for x in PREREGISTERED) for p in parts)
    FINDINGS["coordinates"] = {k: sorted("%s@t%d/%s" % x for x in v)
                               for k, v in sorted(coords.items())}
    FINDINGS["unit_verdict"] = unit
    FINDINGS["object_read_times"] = list(OBJECT_TIMES)
    FINDINGS["per_cell"] = {k: v["verdict"] for k, v in sorted(per.items())}
    disc_all = sorted("%s@t%d/%s" % x
                      for x in coords.get("O4-DISCRIMINATED-RECORD-ACTUALISM",
                                          ()))
    FINDINGS["discriminated_coordinates_anywhere_in_the_table"] = disc_all
    FINDINGS["discriminated_coordinates_at_the_object_read_times"] = sorted(
        "%s@t%d/%s" % x for x in discriminated)
    gate("O4-VOCABULARY", "derivation",
         "EVERY VERDICT IS DRAWN FROM THE PIN'S PRE-REGISTERED VOCABULARY "
         "and from nothing else: the unit verdict and every per-cell verdict "
         "is measured to begin with one of the five pre-registered names.  "
         "The `verdict-lax` mutant emits an out-of-vocabulary tag and must "
         "die here",
         ok_vocab and all(any(v["verdict"].startswith(x)
                              for x in PREREGISTERED) for v in per.values()),
         {"unit_verdict": unit,
          "per_cell": {k: v["verdict"] for k, v in sorted(per.items())}})
    FINDINGS["thesis"] = (
        "On the W6 terminal base, under one instrument and ten identical "
        "gates applied at MATCHED COORDINATES -- three fact-classes, every "
        "declared read time, every candidate rule: transportability is "
        "TIME-INDEXED, not class-indexed.  At the second intermediate read "
        "time NO fact-class transports, the record class included, and the "
        "obstructing object is the two frames' occupied sets, which are "
        "measured disjoint at every cross-frame pair of the twelve charts "
        "and lie in one orbit of the base's own admitted wing exchange at "
        "four of six settings.  At the first intermediate read time the "
        "unrecorded class is FORCED at every setting under every "
        "corridor-bound rule while the certificate is degenerate there, so "
        "no rule is certified at either intermediate time.  What decides "
        "transportability across the read times is measured to be the two "
        "frames' declared LEG PREFIX, not W5's divisibility residual: at "
        "identical residual weight the two intermediate times have opposite "
        "transport verdicts.  Where a transport exists at an intermediate "
        "time, what it would carry is LTP-BARE.  Stated at the committed "
        "finite scope, per coordinate; nothing is claimed about nature and "
        "the charter fork is not adjudicated here.")
    return unit, per


# ===========================================================================
# 17.  RECEIPT AND RENDER
# ===========================================================================
def build_receipt():
    must = [x for x in GATES if x["class"] != "disclosure"]
    fails = sum(1 for x in must if not x["passed"])
    fails += sum(1 for x in ANCHORS if not x["passed"])
    return {"schema": SCHEMA, "pin_commit": PIN_COMMIT,
            "pin_sha256_prefix": PIN_SHA256, "base_commit": BASE_COMMIT,
            "source_sha256": SOURCE_SHA256, "anchors": ANCHORS,
            "gates": GATES, "tables": TABLES, "findings": FINDINGS,
            "totals": {"anchors": len(ANCHORS), "gates": len(GATES),
                       "must_pass_failures": fails}}


def _wrap(s, w):
    out, cur = [], ""
    for word in s.split():
        if len(cur) + len(word) + 1 > w:
            out.append(cur)
            cur = word
        else:
            cur = (cur + " " + word).strip()
    if cur:
        out.append(cur)
    return out


def render(rec) -> str:
    W = 78
    L = ["=" * W,
         "O4 DISCRIMINATOR -- UNRECORDED ACTUALITY ON THE W6 CO-REFERENCE BASE",
         "=" * W,
         "pin %s (sha %s)  base %s" % (rec["pin_commit"],
                                       rec["pin_sha256_prefix"],
                                       rec["base_commit"]),
         "source sha256 %s" % rec["source_sha256"][:16], ""]

    f = rec["tables"]["arena_family"]
    L.append("THE DECLARED ARENA (section 15; every count computed)")
    L.append("  carrier                     %d configurations, j0 = %d" % (NC, J0))
    L.append("  settings x frames           %d x %d" % (f["settings"],
                                                        f["frames"]))
    L.append("  declared read times         %s   (the object's: %s)" % (
        list(READ_TIMES), list(OBJECT_TIMES)))
    L.append("  admitted isomorphisms       %d of the declared %d base scope "
             "(%d of the %d extension)" % (
                 SCOPE["n_admitted"], SCOPE["n_base"],
                 SCOPE["n_admitted_extension"], SCOPE["n_ext_total"]))
    L.append("  checkpoint-phase switchings %d (2^%d, one sign per declared "
             "leg)" % (f["checkpoint_phase_switchings"],
                       f["switching_free_legs"]))
    L.append("  ARENA SIZE                  %d" % f["size"])
    L.append("")

    L.append("ANCHORS (exit-1-only)")
    for a in rec["anchors"]:
        L.append("  %s  %s  %s" % (a["id"], "ok " if a["passed"] else "FAIL",
                                   a["quantity"][:56]))
        L.append("        source    %s" % (a["source"],))
        for ln in _wrap("committed " + canon(a["committed"]), W - 10):
            L.append("        " + ln)
        for ln in _wrap("computed  " + canon(a["computed"]), W - 10):
            L.append("        " + ln)
    L.append("")

    L.append("THE MATCHED TABLE -- every fact-class at every declared read")
    L.append("time under every candidate rule, through the identical gates")
    L.append("  gates: " + " ".join(g for g, _c in DESCENT_GATES))
    L.append("")
    gt = rec["tables"]["matched_table"]
    ct = rec["tables"]["matched_table_counts"]
    for cand in CANDIDATES:
        cid = cand["id"]
        L.append("  %s %s   [%s]" % (cid, cand["name"], cand["level"]))
        for t in READ_TIMES:
            key = "%s@t%d" % (cid, t)
            L.append("    read time t=%d%s" % (
                t, "   (the final declared division event)"
                if t == FINAL_TIME else "   (intermediate)"))
            L.append("      %-8s %s" % ("class", " ".join(
                "%-9s" % g for g, _c in DESCENT_GATES if g != "LTP")))
            for fid in ("F-REC", "F-CFG", "F-CTRL"):
                row = gt[key][fid]
                L.append("      %-8s %s" % (fid, " ".join(
                    "%-9s" % ("PASS" if row[g] else "fail")
                    for g, _c in DESCENT_GATES if g != "LTP")))
            for fid in ("F-REC", "F-CFG", "F-CTRL"):
                d = ct[key][fid]
                L.append("        %-7s |Phi|  %s" % (
                    fid, " ".join("%s=%d" % (sp, d["counts"][sp])
                                  for sp in SETTING_ORDER)))
                L.append("        %-7s vrdct  %s" % (
                    fid, " ".join("%s=%s" % (sp, d["discriminator"][sp][:5])
                                  for sp in SETTING_ORDER)))
                L.append("        %-7s cert   %s" % (
                    fid, " ".join("%s=%s" % (sp, d["certificate"][sp][:5])
                                  for sp in SETTING_ORDER)))
        L.append("")

    L.append("THE OBSTRUCTION AS A RELATION (per read time and setting)")
    orb = rec["tables"]["orbit_relation"]
    for k in sorted(orb):
        v = orb[k]
        L.append("  %-10s sizes %-8s |cap|=%d  one orbit of the wing "
                 "exchange: %-5s  law-preserving: %-5s  cardinality-forced: "
                 "%s" % (k, canon(v["sizes"]), v["intersection"],
                         v["one_orbit_of_the_admitted_wing_exchange"],
                         v["wing_exchange_preserves_the_exact_law"],
                         v["cardinality_forced_disjoint"]))
    L.append("")
    L.append("  the pair census over all unordered pairs of the twelve charts")
    for t in READ_TIMES:
        c = rec["tables"]["pair_census"]["t=%d" % t]
        L.append("      t=%d  cross-frame %d/%d disjoint;  same-frame %d/%d "
                 "sharing" % (t, c["cross_frame_disjoint"],
                              c["cross_frame_pairs"],
                              c["same_frame_sharing"], c["same_frame_pairs"]))
    L.append("")

    L.append("WHAT DECIDES TRANSPORTABILITY (the read-time structure)")
    rs = rec["tables"]["read_time_structure"]
    L.append("  %-10s %-12s %-12s %s" % ("cell", "transports?",
                                         "prefix match?", "residual = 0?"))
    for t in READ_TIMES:
        for sp in SETTING_ORDER:
            k = "t%d/%s" % (t, sp)
            L.append("  %-10s %-12s %-12s %s" % (
                k, rs["transports"][k], rs["prefix_alignment"][k],
                rs["residual_vanishes"][k]))
    L.append("")

    L.append("THE LTP GATE (W5's forcing lemma at every read time)")
    for key in sorted(rec["tables"]["ltp_gate"]):
        lt = rec["tables"]["ltp_gate"][key]
        L.append("  %-10s %s" % (key, lt["verdict"]))
        for sp in SETTING_ORDER:
            L.append("      %-5s %s" % (sp, lt["per_setting"][sp]))
    L.append("")
    L.append("  the residual that decides it (||r||_0 of 36, frame F1/F2)")
    for t in READ_TIMES:
        for sp in SETTING_ORDER:
            r1 = rec["tables"]["ltp_residuals"]["t=%d" % t]["%s/F1" % sp]
            r2 = rec["tables"]["ltp_residuals"]["t=%d" % t]["%s/F2" % sp]
            L.append("      t=%d %-5s %2d / %2d   matrix differing %4d / %4d"
                     % (t, sp, r1["nonzero"], r2["nonzero"],
                        r1["matrix_differing"], r2["matrix_differing"]))
    L.append("")

    L.append("THE ACTUALITY, EXHIBITED (the LTP exhibit)")
    for kk in sorted(rec["tables"]["occupied_supports"]):
        L.append("      %-14s occupied %2d  %s" % (
            kk, len(rec["tables"]["occupied_supports"][kk]),
            rec["tables"]["occupied_supports"][kk]))
    L.append("")

    L.append("THE ARENA TEST AT MATCHED REPRESENTATIVES")
    for r in rec["tables"]["arena"]:
        L.append("  %-5s t=%d %-52s %s" % (r["id"], r["read_time"],
                                           r["name"], r["verdict"]))
        L.append("        %s / %s;  moves under: %s;  distinct %d" % (
            r["fact_class"], r["representative"],
            ", ".join(r["moved_under"]) or "nothing",
            r["distinct_values_over_family"]))
    L.append("")

    L.append("PER-CELL VERDICTS")
    for key in sorted(rec["tables"]["cell_verdicts"]):
        v = rec["tables"]["cell_verdicts"][key]
        L.append("  %-10s %-24s %s" % (key, v["name"], v["verdict"]))
        L.append("      LTP %s;  F-CFG |Phi| %s" % (
            v["ltp"], " ".join("%s=%d" % (sp, v["F-CFG_counts"][sp])
                               for sp in SETTING_ORDER)))
    L.append("")

    L.append("GATES")
    for g in rec["gates"]:
        L.append("  %-30s %-12s %s" % (g["id"], g["class"],
                                       "PASS" if g["passed"] else "FAIL"))
        for ln in _wrap(g["claim"], W - 6):
            L.append("      " + ln)
        if g["value"] is not None:
            for ln in _wrap(json.dumps(g["value"], sort_keys=True,
                                       default=str), W - 8):
                L.append("        " + ln)
    L.append("")

    if "mutants" in rec["tables"]:
        L.append("MUTANT TABLE")
        for m in rec["tables"]["mutants"]:
            L.append("  %-22s %-12s exit %d  %s" % (
                m["mutant"], m["kind"], m["exit"],
                "DIED" if m["died"] else "SURVIVED"))
            L.append("      perturbs: %s" % m["perturbs"])
            L.append("      kills: %s" % ", ".join(
                m["falsified_anchors"] + m["falsified_gates"]))
        gf = rec["tables"]["gate_falsification"]
        L.append("  must-pass gates %d; falsified by some mutant %d; "
                 "never falsified %s" % (
                     gf["must_pass_gates"], gf["falsified_by_some_mutant"],
                     gf["not_falsified_by_any_mutant"] or "[]"))
        L.append("  mutant kinds: %s" % canon(gf["mutant_kinds"]))
        L.append("")

    L.append("=" * W)
    L.append("UNIT VERDICT")
    for ln in _wrap(rec["findings"]["unit_verdict"], W - 4):
        L.append("  " + ln)
    L.append("=" * W)
    for ln in _wrap(rec["findings"]["thesis"], W - 2):
        L.append("  " + ln)
    L.append("")
    L.append("  anchors %d  gates %d  must-pass failures %d" % (
        rec["totals"]["anchors"], rec["totals"]["gates"],
        rec["totals"]["must_pass_failures"]))
    return "\n".join(L) + "\n"


# ===========================================================================
def main() -> int:
    global MUTANT, SOURCE_SHA256, _FROZEN
    ap = argparse.ArgumentParser()
    ap.add_argument("--mutant", default=None)
    ap.add_argument("--quiet", action="store_true")
    ap.add_argument("--falsification-selftest", action="store_true")
    a = ap.parse_args()
    MUTANT = a.mutant
    SOURCE_SHA256 = hashlib.sha256(
        Path(__file__).resolve().read_bytes()).hexdigest()

    # -- MUTANT HOOKS.  Every hook is installed BEFORE the freeze and before
    #    the anchors, so that a mutant which perturbs a fixture is measured by
    #    the anchors rather than slipping past them.
    global SCOPE, WSWAP
    SCOPE = declared_scope()
    WSWAP = W6.build_perm(1, 0, 0, 0, 0)
    if MUTANT == "support-lax":
        # THE WRONG-TIME SUPPORT READ: F-CFG's datum taken at the FINAL time
        # whatever the cell declares, so the class stops being about
        # unrecorded configurations at all.
        def _cfg_lax(sp, fr, t, eps=None, relabel=None, extra_identity=False,
                     compensate=True):
            _bump()
            rt = FINAL_TIME + (1 if extra_identity else 0)
            c = chart_at(sp, fr, rt, eps, relabel, extra_identity)
            p = c.dist(rt)
            return c, {"carriers": NC, "read_time": t,
                       "actual": frozenset(p),
                       "law": {i: canon(p[i]) for i in sorted(p)}}
        globals()["datum_cfg"] = _cfg_lax
        FL = list(FACT_CLASSES)
        FL[1] = (FL[1][0], FL[1][1], _cfg_lax, FL[1][3])
        globals()["FACT_CLASSES"] = tuple(FL)
        globals()["FACT_CLASSES_BY_ID"] = {i: f for i, _d, f, _r in FL}
    if MUTANT == "likeforlike-lax":
        def _extra(ca, da, cb, db, perms, level, order_free, drop_identity,
                   _x=None):
            return transports_cfg(ca, da, cb, db, perms, level, order_free,
                                  drop_identity)
        TRANSPORT["F-CFG"] = _extra
    if MUTANT == "anchor-w6":
        # THE REUSED-ANCHOR MUTANT: the wing exchange replaced by the
        # identity, so the base's own realized-legs and never-occupied-block
        # measurements are recomputed against the wrong group element.
        WSWAP = W6.build_perm(0, 0, 0, 0, 0)
    if MUTANT == "action-weaken":
        # THE ARENA ACTION COLLAPSED to the identity relabelling and the
        # trivial switching, so that NOTHING can be seen to move.
        SCOPE["admitted"] = SCOPE["admitted"][:1]
        SCOPE["n_admitted"] = 1
        globals()["switchings"] = lambda n: [tuple([1] * n)]

    if MUTANT == "table-clip":
        # THE UNMATCHED TABLE: one declared read time dropped, so the table is
        # computed at fewer coordinates than the model declares -- the habit
        # this unit's re-derivation exists to remove.
        clipped = READ_TIMES[:-1]
        globals()["READ_TIMES"] = clipped
        globals()["OBJECT_TIMES"] = clipped[:-1]
        globals()["FINAL_TIME"] = clipped[-1]
        globals()["CHARTS"] = {(sp, fr): chart_at(sp, fr, clipped[-1])
                               for sp in SETTING_ORDER for fr in ("F1", "F2")}

    if MUTANT == "freeze-lax":
        datum_cfg("SP-A", "F1", OBJECT_TIMES[-1])
    run_freeze()
    resid = run_anchors()

    TABLES["actuality"] = exhibit_actuality()
    table, ltps = run_matched_table(resid)
    obstruction = run_cause(table, resid)
    arena_rows = run_arena()
    run_arena_residual(arena_rows, obstruction)
    run_controls(table, ltps, arena_rows)
    run_ltp_gates(table, ltps)
    TABLES["_ltps"] = ltps
    run_selftest(table, resid)
    del TABLES["_ltps"]
    run_verdict(table, ltps, arena_rows)
    run_exactness()
    if a.falsification_selftest and not a.mutant:
        run_mutant_table()

    rec = build_receipt()
    txt = render(rec)
    if a.falsification_selftest and not a.mutant:
        OUT_TXT.write_text(txt)
        OUT_JSON.write_text(json.dumps(rec, indent=1, sort_keys=True,
                                       default=str) + "\n")
    if not a.quiet:
        sys.stdout.write("\n" + txt)
    fail = rec["totals"]["must_pass_failures"]
    if a.quiet:
        sys.stdout.write("KILL-JSON " + json.dumps(
            {"failed_anchors": [x["id"] for x in ANCHORS if not x["passed"]],
             "failed_gates": [x["id"] for x in GATES
                              if x["class"] != "disclosure"
                              and not x["passed"]]}) + "\n")
    prog("done: %d anchors, %d gates, %d must-pass failures"
         % (rec["totals"]["anchors"], rec["totals"]["gates"], fail))
    return 1 if fail else 0


if __name__ == "__main__":
    raise SystemExit(main())
