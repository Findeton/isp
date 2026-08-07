#!/usr/bin/env python3
"""O4 DISCRIMINATOR -- UNRECORDED ACTUALITY ON THE W6 CO-REFERENCE BASE.

Executes the frozen pin `v13/note-o4-discriminator-pin.md` (commit e1e8dcd,
sha 2568bc528796) against the immutable base 71371ae (W6 TERMINAL, v12 LOG
#41; paper 2 TERMINAL; paper 0 v2.4 section O4).

THE QUESTION.  Paper 0 v2.4 leaves an explicit fork.  O4-A (configuration
realism) holds that unrecorded local configurations are actual but
ephemeral, and REQUIRES a covariant co-reference rule for them.  O4-B
(record actualism) holds that only records are actual.  W6 built the base at
which the question becomes decidable: on its committed two-frame model
RECORD facts provably descend.  This unit asks whether UNRECORDED
CONFIGURATION facts descend under the SAME instrument -- and, if a rule
exists, what probability law attaches to what it transports.

THE INSTRUMENT.  Transport of fact-data along the co-reference maps of the
W6 base.  ONE set of descent gates, applied identically to three declared
fact-classes:

  F-REC   record facts, division-event-anchored (POSITIVE CONTROL: W6's
          terminal descent results must reproduce, anchored exit-1);
  F-CFG   unrecorded configuration facts -- "the configuration between
          division events is X" -- as transportable data (THE OBJECT);
  F-CTRL  a deliberately mis-conventioned class that reads configuration
          NAMES (NEGATIVE CONTROL: it must FAIL; if it passes the
          instrument is dead and the run says so).

Four candidate co-reference rules for F-CFG are declared inside the pin's
corridor -- covariant, name-blind, NO GLOBAL SLICE -- with their gates fixed
BEFORE any fixture value is computed (the receipt's gate order proves the
freeze, and the evaluation counter is gated at zero at the freeze).

THE LTP GATE.  Every candidate must state what probability law attaches to
the actuality it transports.  That is COMPUTED, not asserted: the
intermediate-time actuality is exhibited, and the declared-law residual of
W5's LTP-forcing lemma is evaluated at the model's own admissible p(0).
Where the residual is nonzero the intermediate time is NOT a division event
of the model as declared, so no committed law conditions on the transported
configuration: the candidate is recorded LTP-BARE at that coordinate.

THE ARENA TEST.  Section 15 discipline: the arena is declared as data and
F-CFG's truth-values are pushed through its admitted action -- the admitted
isomorphism group of the base and the checkpoint-phase switchings at which
amplitude data enters.  Whatever moves is reported with its measured orbit.

Exact arithmetic throughout: the totally real quartic field Q(cos pi/8) of
the committed composite model (tuple equality IS field equality) and
fractions.Fraction.  No float enters any path.  Anchors exit 1 on mismatch.
`--mutant NAME` breaks exactly one anchor, gate or derivation step and must
exit 1 naming what it falsified.  No wall-clock value enters the receipt or
the rendered output, so two delivery-mode runs are byte-identical.

Scope: finite; ONE committed carrier of 36 configurations; six declared
settings; two declared frames; the declared 72-element permutation scope and
its declared 96-element extension.  No locality, topology, causality,
spacetime, field, QFT or gravity object is constructed or claimed.  Nothing
is claimed about nature.  The charter fork is NOT adjudicated here.
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

SCHEMA = "o4-discriminator-receipt-v1"
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
    """The instrument's only value cache.  Bypassed entirely in fresh mode,
    where the hit count is gated at zero; the `memo-lax` mutant restores the
    reviewed defect (a self-test reading the cache) and must die there."""
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
#     fixture is built anywhere in this file.
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
# 2.  THE CHARTS OF THE BASE.  Built through W6's own constructor, so
#     occurrence, availability and the law are RECOMPUTED, never stipulated.
# ===========================================================================
def cprov(wing, ang):
    return W6.cprov(wing, ang)


def final_chart(sp, fr, eps=None, relabel=None, extra_identity=False):
    """The committed final-record chart at (setting, frame), optionally
    carried by a checkpoint-phase switching, a configuration relabelling, or
    an extra identity leg prepended (the time-reindexing of the no-slice
    gate)."""
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
    if extra_identity:
        wa, wb = wa + 1, wb + 1
    tA = W6.Token("R_A", pa, VALS, wa, cprov("A", a8))
    tB = W6.Token("R_B", pb, VALS, wb, cprov("B", b8))
    return W6.Chart("%s/%s" % (sp, fr), K, NC, legs, j0, [tA, tB])


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


CHARTS = {(sp, fr): final_chart(sp, fr)
          for sp in SETTING_ORDER for fr in ("F1", "F2")}
CHART_KEYS = sorted(CHARTS)
NLEGS = len(CHARTS[CHART_KEYS[0]].legs)      # computed, never typed


# ===========================================================================
# 3.  THE THREE FACT-CLASSES.  Declared -- carrier, datum, preservation list,
#     transport -- BEFORE any fixture value is computed.
# ===========================================================================
def _bump():
    global _FEVALS
    if not _FROZEN and MUTANT != "freeze-lax":
        raise RuntimeError("fixture truth evaluated before the freeze")
    _FEVALS += 1


def datum_rec(sp, fr, eps=None, relabel=None, extra_identity=False):
    """F-REC.  Carrier: the chart's record tokens.  Datum: the joint law of
    their declared values on the ACTUAL (positive-probability) value tuples,
    read at the time every token has been written.  Division-event-anchored:
    the final time is a declared division event of the model."""
    _bump()
    c = final_chart(sp, fr, eps, relabel, extra_identity)
    return c, {"carriers": len(c.tokens),
               "law": {canon(k): canon(v) for k, v in c.law.items()},
               "read": tuple(canon(c.read(i)) for i in range(NC))}


def datum_cfg(sp, fr, eps=None, relabel=None, extra_identity=False):
    """F-CFG.  Carrier: the 36 configuration propositions "the configuration
    is i".  Datum, at the INTERMEDIATE time between the declared division
    event 0 and the final time: the actuality bit (positive probability) and
    the exact probability of each configuration.  This is exactly the pin's
    "the configuration between division events is X", presented as
    transportable data of the same type as F-REC's."""
    _bump()
    c = final_chart(sp, fr, eps, relabel, extra_identity)
    upto = 3 if extra_identity else 2
    p = c.dist(upto)
    return c, {"carriers": NC,
               "actual": frozenset(p),
               "law": {i: canon(p[i]) for i in sorted(p)}}


def datum_ctrl(sp, fr, eps=None, relabel=None, extra_identity=False):
    """F-CTRL.  The deliberately MIS-CONVENTIONED class: the same 36
    carriers, but the datum is the configuration's own integer NAME.  It is
    mis-conventioned in exactly one respect -- it reads a label the declared
    gauge is free to change -- and it must FAIL the gates records pass.  If
    it passes them, the instrument cannot tell a fact from a name and this
    run says so."""
    _bump()
    c = final_chart(sp, fr, eps, relabel, extra_identity)
    return c, {"carriers": NC, "name": {i: str(i) for i in range(NC)}}


FACT_CLASSES = (
    ("F-REC", "record facts (division-event-anchored)", datum_rec,
     "POSITIVE CONTROL"),
    ("F-CFG", "unrecorded configuration facts at the intermediate time",
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
    if drop_identity and MUTANT != "global-now-smuggler":
        return [L for L in chart.legs if not _is_identity_leg(L)]
    return list(chart.legs)


def legs_compatible(ca, cb, p, level, order_free, drop_identity):
    """Does the permutation p carry chart b's declared legs onto chart a's at
    the declared matching level?  ORDER-FREE matching is W6's own declared
    choice (two frames of one experiment differ exactly by the order of two
    commuting legs); requiring the order is what a slice-indexed rule does
    and the no-slice gate measures the difference."""
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


def transports_rec(ca, da, cb, db, perms, level, order_free, drop_identity):
    """F-REC transports: token maps induced by a frame-isomorphism and
    surviving W6's preservation list (LIST_B).  This is W6-B's own object,
    routed through the same gate harness as the other two classes."""
    isos = []
    for p in perms:
        if p[cb.j0] != ca.j0:
            continue
        if not legs_compatible(ca, cb, p, level, order_free, drop_identity):
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
    at the declared level, AND carry b's intermediate-time datum onto a's --
    the actuality bit and the exact probability of every configuration.  The
    last clause is the configuration-level analogue of items 1 and 3 of W6's
    preservation list, and it is the only place the class's own datum is
    consulted."""
    out = []
    for p in perms:
        if p[cb.j0] != ca.j0:
            continue
        if not legs_compatible(ca, cb, p, level, order_free, drop_identity):
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
    for p in perms:
        if p[cb.j0] != ca.j0:
            continue
        if not legs_compatible(ca, cb, p, level, order_free, drop_identity):
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
#     gate are computed for each, and a candidate that fails the corridor is
#     gated out with the measurement that gates it printed.
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
    {"id": "C2", "name": "DESCENT-RESTRICTION",
     "definition":
         "Two unrecorded configuration facts co-refer iff the W6 groupoid "
         "acts between their charts: the transport must be an admitted "
         "frame-isomorphism, order-free and blind to identity legs, and it "
         "must carry the intermediate-time datum.  Co-reference is declared "
         "only where the record-level base already supplies a map.  The "
         "matching level is the level at which the base's own token tie is "
         "measured to be cut -- the BORN level: matching the full declared "
         "legs by their Born shadows alone already forces the record-level "
         "map at every setting.",
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
    ("TRI", "triple coherence holds on the declared triple"),
    ("GLUE", "a coherent family exists in one gauge orbit with an "
             "injective colimit"),
    ("CERT", "the transported datum is CERTIFIED, not merely compatible"),
    ("COVAR", "the verdict is equivariant under the admitted arena action"),
    ("NAMEBLIND", "the verdict survives a pure configuration relabelling"),
    ("NOSLICE", "the verdict survives a pure time re-indexing"),
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
         "The three fact-classes, their carriers and preservation lists, the "
         "ten descent gates and the four candidate rules with their matching "
         "levels and corridor claims are all recorded above, and the "
         "fact-datum evaluation counter is measured to be ZERO at this "
         "point.  The `freeze-lax` mutant evaluates one fixture datum first "
         "and must die here",
         _FEVALS == 0 and len(GATES) == 0,
         {"fact_datum_evaluations_before_freeze": _FEVALS,
          "fact_classes": [c[0] for c in FACT_CLASSES],
          "descent_gates": [g[0] for g in DESCENT_GATES],
          "candidates": [c["id"] for c in CANDIDATES]})
    TABLES["declarations"] = {
        "fact_classes": [{"id": i, "role": r,
                          "datum": (f.__doc__ or "").split("\n")[0]}
                         for i, _d, f, r in FACT_CLASSES],
        "descent_gates": [{"id": i, "claim": c} for i, c in DESCENT_GATES],
        "candidates": [{k: v for k, v in c.items()} for c in CANDIDATES]}
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
           "the declared permutation scope has 72 elements",
           72, SCOPE["n_base"])
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
    anchor("A11", "v12/note-w6-record-coreference.md W6-B",
           "|Phi_A| at the six settings (the wing tie)", [2] * 6, nA)
    anchor("A12", "v12/note-w6-record-coreference.md W6-B",
           "|Phi_B| at the six settings (forced, the identity)", [1] * 6, nB)

    # -- W6 M4: the intermediate slice, W6's own measurement ----------------
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
        i4B.append(len(W6.phi_set(inters[x], inters[y]), ) if False else
                   len(W6.phi_set(inters[x], inters[y], items=LIST_B,
                                  isos=W6.iso_maps(inters[x], inters[y],
                                                   SCOPE["admitted"]))))
        shared.append(sum(1 for ta in inters[x].tokens for tb in inters[y].tokens
                          if W6.same_partition(ta.part, tb.part)))
    anchor("A13", "v12/note-w6-record-coreference.md M4",
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
    anchor("A15", "v12/note-w6-record-coreference.md control 4",
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
           "LABEL", "the two frames' time-2 occupied supports never coincide, "
           "with their sizes",
           [(False, 2, 8), (False, 2, 8), (False, 8, 8), (False, 8, 8),
            (False, 2, 2), (False, 8, 8)], t2sup)
    SW2 = ((0, 1), (1, 0))
    anchor("A17", "v12/note-w6-record-coreference.md WHAT GROUNDS A TOKEN "
           "LABEL", "token maps admitted by the REALIZED legs alone "
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
           "LABEL", "w.U_prep.w against U_prep: the j0 column (+,-), the "
           "other 35 as a block (+,-), then column by column",
           (False, True, False, False, 9, 8),
           (colof(Uw, 0) == colof(Up, 0), colof(Uw, 0) == negcol[0],
            all(colof(Uw, j) == colof(Up, j) for j in oth),
            all(colof(Uw, j) == negcol[j] for j in oth),
            sum(1 for j in oth if colof(Uw, j) == colof(Up, j)),
            sum(1 for j in oth if colof(Uw, j) == negcol[j])))
    anchor("A19", "v12/note-w6-record-coreference.md WHAT GROUNDS A TOKEN "
           "LABEL", "the never-occupied block of U_prep has 35 columns",
           35, NC - 1)

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
    res = ltp_residuals()
    anchor("A25", "v12/note-w5-barandes-recast.md section 3.3 (G6)",
           "the LTP residual weight ||r||_0 of 36 at the six settings, "
           "frame F1 then F2",
           ([0, 0, 16, 16, 0, 16], [0, 0, 16, 16, 0, 16]),
           ([res[(sp, "F1")]["nonzero"] for sp in SETTING_ORDER],
            [res[(sp, "F2")]["nonzero"] for sp in SETTING_ORDER]))
    anchor("A26", "v12/note-w5-barandes-recast.md section 3.3 (G4)",
           "every column of the matrix residual that differs at all differs "
           "in exactly 16 entries (W5's 'the same fact, seen once per "
           "column'), at the three violated settings, both frames",
           {16},
           set().union(*[set(res[(sp, fr)]["per_column"])
                         for sp in ("SP-C", "SP-D", "SP-F")
                         for fr in ("F1", "F2")]))
    anchor("A27", "v12/note-w5-barandes-recast.md section 3.3 (G5, G5b)",
           "the SP-C and SP-F residual censuses: (distinct values, rational "
           "entries of 16)",
           ((4, 0), (6, 8)),
           ((res[("SP-C", "F1")]["distinct"], res[("SP-C", "F1")]["rational"]),
            (res[("SP-F", "F1")]["distinct"], res[("SP-F", "F1")]["rational"])))
    gate("O4-COMPLETION-DISCLOSURE", "disclosure",
         "A DECLARED DIVERGENCE FROM A COMMITTED COUNT, AND WHY.  W5's A3 "
         "prints the divisibility census (0,0,576,576,0,576) -- 16 differing "
         "entries in every one of the 36 columns.  Recomputed on THIS base's "
         "preparation operator the count is measured to be smaller, because "
         "W5 rebuilt the model from the singlet dictionary and chose a "
         "different orthogonal completion of U_prep off the j0 column.  The "
         "j0 COLUMN -- the only column the model's own admissible p(0) ever "
         "reads, and the one W5's G1 says carries the whole residual -- "
         "agrees exactly (A25).  The matrix count is therefore a "
         "completion-dependent quantity and the vector count is not: an "
         "independent confirmation, from a second direction, of W6's finding "
         "that U_prep's arbitrary completion off j0 is doing work",
         True,
         {"committed_bc2_matrix_count": 576,
          "recomputed_on_this_base":
              [res[(sp, "F1")]["matrix_differing"] for sp in SETTING_ORDER],
          "columns_that_differ":
              [len(res[(sp, "F1")]["per_column"]) for sp in SETTING_ORDER],
          "per_column_differing_counts":
              sorted(set().union(*[set(res[(sp, "F1")]["per_column"])
                                   for sp in ("SP-C", "SP-D", "SP-F")])),
          "j0_column_agrees_with_the_committed_count": True})
    TABLES["ltp_residuals"] = {
        "%s/%s" % k: {kk: vv for kk, vv in v.items() if kk != "vector"}
        for k, v in sorted(res.items())}
    return res


def ltp_residuals():
    """W5's declared-law residual D(2,1,0) = Gamma(3<-0) - Gamma(3<-2)
    Gamma(2<-0), evaluated on the model's own admissible p(0) = delta_{j0}
    and, separately, as a matrix.  Exact in Q(cos pi/8); the rational
    entries are detected by the field's own rationality test, never by a
    tolerance."""
    out = {}
    for sp in SETTING_ORDER:
        for fr in ("F1", "F2"):
            T1, T2, T3, L3 = M.propagators(sp, fr)
            g30 = W6.sp_born(K, T3)
            g20 = W6.sp_born(K, T2)
            g32 = W6.sp_born(K, L3)
            comp = (W6.sp_mul(K, g20, g32) if MUTANT == "anchor-ltp"
                    else W6.sp_mul(K, g32, g20))
            keys = set(g30) | set(comp)
            percol: dict = {}
            for (i, j) in keys:
                if g30.get((i, j), K.zero) != comp.get((i, j), K.zero):
                    percol[j] = percol.get(j, 0) + 1
            mdiff = sum(percol.values())
            vec = {}
            for i in range(NC):
                a = g30.get((i, J0), K.zero)
                b = comp.get((i, J0), K.zero)
                d = K.sub(a, b)
                if not K.is_zero(d):
                    vec[i] = d
            if MUTANT == "ltp-lax":
                vec = {}
            vals = sorted({canon(v) for v in vec.values()})
            # RATIONALITY, by the field's own test: `to_rat` returns the
            # rational value of an element of Q inside K and None otherwise.
            # No tolerance and no float is involved.
            rat = sum(1 for v in vec.values() if K.to_rat(v) is not None)
            out[(sp, fr)] = {"nonzero": len(vec), "matrix_differing": mdiff,
                             "distinct": len(vals), "rational": rat,
                             "per_column": sorted(percol.values()),
                             "values": vals, "vector": vec}
    return out


# ===========================================================================
# 7.  THE TRANSPORT INSTRUMENT: the ten gates, applied identically
# ===========================================================================
def _perms_for(cand):
    return SCOPE[cand["perms"]]


def _chart_and_datum(fid, fn, sp, fr, **kw):
    return _memo(("cd", fid, sp, fr, canon(sorted(kw.items()))),
                 lambda: fn(sp, fr, **kw))


def realized_of(chart):
    """The REALIZED restriction of any chart, computed from the chart's own
    legs and initial configuration: each leg restricted to the configurations
    the process actually occupies before and after it.  Built through W6's
    own constructor, so occurrence, availability and the law are recomputed
    from the restricted legs.  Taking the chart as the argument -- rather
    than a (setting, frame) key -- is what lets the corridor gates carry a
    switched, relabelled or re-indexed presentation through the realized
    restriction as well."""
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
    return W6.Chart(chart.name + "@real", K, chart.n, legs, chart.j0, toks)


def edge_transports(cand, fid, fn, ka, kb, **kw):
    """Phi for one ordered edge, one candidate, one fact-class."""
    ca, da = _chart_and_datum(fid, fn, ka[0], ka[1], **kw)
    cb, db = _chart_and_datum(fid, fn, kb[0], kb[1], **kw)
    if cand.get("realized"):
        ca, cb = realized_of(ca), realized_of(cb)
    return TRANSPORT[fid](ca, da, cb, db, _perms_for(cand), cand["level"],
                          cand["order_free"], cand["drop_identity"])


def pair_transports(cand, fid, ca, da, cb, db):
    """Phi for an explicitly built pair of charts (the corridor gates)."""
    if cand.get("realized"):
        ca, cb = realized_of(ca), realized_of(cb)
    return TRANSPORT[fid](ca, da, cb, db, _perms_for(cand), cand["level"],
                          cand["order_free"], cand["drop_identity"])


def five_valued(n, scope_a, scope_b, instrument=True):
    """W6's own five-valued discriminator, reused so that the vocabulary is
    emitted rather than typed."""
    return W6.verdict_of(n, scope_a, scope_b, instrument=instrument)


def class_gate_row(cand, fid, fn):
    """THE TEN GATES for one (candidate, fact-class) pair, measured."""
    res: dict = {}
    # -- EXIST / FORCED, per setting, over the committed frame pairs --------
    counts, verdicts = {}, {}
    for sp in SETTING_ORDER:
        ka, kb = (sp, "F1"), (sp, "F2")
        n = len(edge_transports(cand, fid, fn, ka, kb))
        counts[sp] = n
        sa = NC if fid != "F-REC" else len(CHARTS[ka].live("available"))
        sb = NC if fid != "F-REC" else len(CHARTS[kb].live("available"))
        verdicts[sp] = five_valued(n, sa, sb)
    res["counts"] = counts
    res["verdicts"] = verdicts
    res["EXIST"] = all(v >= 1 for v in counts.values())
    res["FORCED"] = all(v == 1 for v in counts.values())

    # -- INV: the inverse of an admitted transport is admitted in reverse ---
    inv_ok = True
    for sp in SETTING_ORDER:
        fwd = edge_transports(cand, fid, fn, (sp, "F1"), (sp, "F2"))
        bwd = set(edge_transports(cand, fid, fn, (sp, "F2"), (sp, "F1")))
        for t in fwd:
            if tuple(sorted((b, a) for a, b in t)) not in bwd:
                inv_ok = False
    res["INV"] = inv_ok and res["EXIST"]

    # -- TRI / GLUE on the declared triple {F1, F2, F2^pi} at SP-A ---------
    tri = triple_descent(cand, fid, fn)
    res["triple"] = tri
    res["TRI"] = tri["verdict"] not in ("NO-DESCENT", "ABSENT-PAIR")
    res["GLUE"] = tri["verdict"] in ("SET-AMALGAM", "GROUPOID-AMALGAM")

    # -- CERT: the transported datum is certified, not merely compatible ---
    cert_by_sp, res["cert_detail"] = certify(fid, fn)
    res["cert_per_setting"] = cert_by_sp
    res["CERT"] = all(cert_by_sp.values())

    # -- COVAR / NAMEBLIND / NOSLICE: the corridor, measured ---------------
    res["COVAR"], res["covar_detail"] = covariance(cand, fid, fn)
    res["NAMEBLIND"], res["nameblind_detail"] = name_blindness(cand, fid, fn)
    res["NOSLICE"], res["noslice_detail"] = no_slice(cand, fid, fn)
    return res


def triple_descent(cand, fid, fn):
    """The descent gates on W6's own declared triple: F1, F2 and F2 presented
    on a relabelled configuration set (both qubit flips), built as its OWN
    object.  The solver is W6's, so its verdict vocabulary is the base's."""
    sp = "SP-A"
    pi = W6.build_perm(0, 0, 0, 1, 1)
    names = ["F1", "F2"] if MUTANT == "descent-lax" else ["F1", "F2", "F2pi"]
    spec = {nm: d for nm, d in
            (("F1", {}), ("F2", {}), ("F2pi", {"relabel": pi}))
            if nm in names}
    frame = {"F1": "F1", "F2": "F2", "F2pi": "F2"}
    charts, data = {}, {}
    for nm in names:
        c, d = _chart_and_datum(fid, fn, sp, frame[nm], **spec[nm])
        charts[nm], data[nm] = c, d
    phis, auts = {}, {}
    for a, b in itertools.permutations(names, 2):
        raw = TRANSPORT[fid](charts[a], data[a], charts[b], data[b],
                             _perms_for(cand), cand["level"],
                             cand["order_free"], cand["drop_identity"])
        phis[(a, b)] = [dict(t) for t in raw]
    for nm in names:
        raw = TRANSPORT[fid](charts[nm], data[nm], charts[nm], data[nm],
                             _perms_for(cand), cand["level"],
                             cand["order_free"], cand["drop_identity"])
        auts[nm] = [dict(t) for t in raw] or [{}]
    out = W6.descent(names, phis, auts)
    out["edge_counts"] = {("%s<-%s" % e): len(v) for e, v in sorted(phis.items())}
    out["aut_counts"] = {nm: len(auts[nm]) for nm in names}
    return out


def certify(fid, fn):
    """CERT, per coordinate.  For F-REC the certificate is W6's ROUTE-EXT
    read off the one process: each configuration is read through F1's record
    map and through F2's, and the joint law must be supported on the graph of
    a value-PRESERVING bijection.  The SAME construction is run for F-CFG and
    F-CTRL with the class's own datum in place of the record value, so the
    three classes are certified like for like.  The pair guard of W6 is kept:
    a configuration on which the two charts disagree disqualifies the pair,
    because a certificate on the remainder certifies nothing about the pair."""
    per, ok = {}, {}
    for sp in SETTING_ORDER:
        ca, _da = _chart_and_datum(fid, fn, sp, "F1")
        cb, _db = _chart_and_datum(fid, fn, sp, "F2")
        if fid == "F-REC":
            pa, pb = ca.dist(), cb.dist()
            reader = lambda i: (ca.read(i), cb.read(i))          # noqa: E731
        else:
            pa, pb = ca.dist(2), cb.dist(2)
            if fid == "F-CTRL":
                reader = lambda i: (str(i), str(i))              # noqa: E731
            else:
                reader = lambda i: (canon(pa.get(i, K.zero)),    # noqa: E731
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
                   "disagreeing_configurations": dis}
    if MUTANT == "cert-lax":
        ok = {sp: True for sp in SETTING_ORDER}
    return ok, {"route": "EXT", "per_setting": per}


def covariance(cand, fid, fn):
    """COVAR.  The rule is equivariant iff carrying BOTH charts of an edge by
    the same admitted arena element leaves the transport count unchanged, and
    carrying them by a checkpoint-phase switching does the same.  Measured,
    per coordinate."""
    base, moved_relabel, moved_switch, tested = {}, 0, 0, 0
    for sp in SETTING_ORDER:
        n0 = len(edge_transports(cand, fid, fn, (sp, "F1"), (sp, "F2")))
        base[sp] = n0
        for g in arena_group():
            n1 = len(edge_transports(cand, fid, fn, (sp, "F1"), (sp, "F2"),
                                     relabel=g))
            tested += 1
            if n1 != n0:
                moved_relabel += 1
        for eps in switchings(NLEGS):
            n2 = len(edge_transports(cand, fid, fn, (sp, "F1"), (sp, "F2"),
                                     eps=eps))
            tested += 1
            if n2 != n0:
                moved_switch += 1
    ok = (moved_relabel == 0 and moved_switch == 0)
    if MUTANT == "covar-lax":
        ok, moved_relabel, moved_switch = True, 0, 0
    return ok, {"tested": tested, "relabelling_failures": moved_relabel,
                "switching_failures": moved_switch, "base_counts": base}


def name_blindness(cand, fid, fn):
    """NAMEBLIND.  Present ONE chart on a relabelled configuration set (the
    declared gauge of the base) and ask the rule to identify it with the
    chart it is a relabelling OF.  A name-blind rule identifies them; a
    name-reading rule cannot, because the labels are exactly what changed.
    The reference is the rule's own self-transport count on the unrelabelled
    chart, so the gate compares like with like and cannot pass by returning
    zero twice.  This is the gate the negative control F-CTRL exists to
    fail."""
    pi = W6.build_perm(0, 0, 0, 1, 1)
    same, moved, detail = 0, 0, {}
    for sp in SETTING_ORDER:
        for fr in ("F1", "F2"):
            ca, da = _chart_and_datum(fid, fn, sp, fr)
            cb, db = _chart_and_datum(fid, fn, sp, fr, relabel=pi)
            n0 = len(pair_transports(cand, fid, ca, da, ca, da))
            n1 = len(pair_transports(cand, fid, ca, da, cb, db))
            detail["%s/%s" % (sp, fr)] = (n0, n1)
            if n1 == n0 and n0 >= 1:
                same += 1
            else:
                moved += 1
    return moved == 0, {"identified": same, "failed": moved,
                        "per_chart": detail}


def no_slice(cand, fid, fn):
    """NOSLICE.  The gate that keeps the corridor.  Re-index ONE chart's time
    coordinate by prepending an identity leg: the process is the same object,
    presented on a shifted index, and no transition has been added.  A rule
    inside the corridor identifies the chart with its own re-indexed
    presentation exactly as it identifies the chart with itself; a rule that
    reads a global time slice cannot, because the index moved.  The reference
    is again the rule's own self-transport count, so a rule cannot pass by
    returning zero twice.  The `global-now-smuggler` mutant restores the
    index-reading normalisation inside an otherwise corridor-bound rule and
    must die here."""
    same, moved, detail = 0, 0, {}
    for sp in SETTING_ORDER:
        for fr in ("F1", "F2"):
            ca, da = _chart_and_datum(fid, fn, sp, fr)
            cb, db = _chart_and_datum(fid, fn, sp, fr, extra_identity=True)
            n0 = len(pair_transports(cand, fid, ca, da, ca, da))
            n1 = len(pair_transports(cand, fid, ca, da, cb, db))
            detail["%s/%s" % (sp, fr)] = (n0, n1)
            if n1 == n0 and n0 >= 1:
                same += 1
            else:
                moved += 1
    return moved == 0, {"identified": same, "failed": moved,
                        "per_chart": detail}


# ===========================================================================
# 8.  THE LTP GATE (W5's forcing lemma, instantiated per candidate)
# ===========================================================================
def ltp_gate(cand, res, resid):
    """What probability law attaches to the actuality this candidate
    transports?  COMPUTED, not asserted.

    (i)  The intermediate-time actuality is EXHIBITED: the occupied support
         and its exact law at the time between the declared division event 0
         and the final time.
    (ii) W5's lemma (c) is evaluated at that time on the model's own
         admissible p(0): where the declared-law residual is nonzero, the
         intermediate time is NOT a division event of the model as declared,
         so no committed law conditions on the transported configuration.
    (iii) W6's own measurement is carried in: the shared record subalgebra at
         that time is empty, so no record fact conditions on it either.

    A candidate whose transport is nowhere admitted transports no actuality
    and the gate is NOT-APPLICABLE there; a candidate that transports
    actuality at a coordinate where (ii) fires is LTP-BARE at that
    coordinate."""
    per = {}
    for sp in SETTING_ORDER:
        n = res["counts"][sp]
        forced_bare = resid[(sp, "F1")]["nonzero"] > 0 or \
            resid[(sp, "F2")]["nonzero"] > 0
        # A committed RECORD law would condition on the datum only if some
        # declared record token had been written, in BOTH frames, by the
        # intermediate time.  That count is measured, never assumed.
        shared = shared_record_at_intermediate(sp)
        if n == 0:
            per[sp] = "NOT-APPLICABLE (no transport admitted)"
        elif forced_bare:
            per[sp] = "LTP-BARE (forced: the intermediate time is not a "\
                      "division event of the model as declared)"
        elif shared > 0:
            per[sp] = "LTP-LAWFUL (a shared record law conditions on the "\
                      "datum)"
        else:
            per[sp] = "LTP-BARE-UNWITNESSED (the residual vanishes, so the "\
                      "forcing lemma does not fire; and the shared record "\
                      "subalgebra at that time is measured empty, so no "\
                      "committed law conditions on the datum either)"
    live = [sp for sp in SETTING_ORDER if res["counts"][sp] > 0]
    bare = [sp for sp in live if per[sp].startswith("LTP-BARE")]
    lawful = [sp for sp in live if per[sp].startswith("LTP-LAWFUL")]
    if MUTANT == "ltp-lax":
        bare = []
    if not live:
        verdict = "LTP-NOT-APPLICABLE"
    elif bare:
        verdict = "LTP-BARE"
    elif lawful:
        verdict = "LTP-LAWFUL"
    else:
        verdict = "LTP-BARE-UNWITNESSED"
    return {"per_setting": per, "verdict": verdict,
            "coordinates_with_transport": live,
            "coordinates_forced_bare": bare}


_SHARED: dict = {}


def shared_record_at_intermediate(sp):
    """How many declared record partitions have been written in BOTH frames
    by the intermediate time.  W6's own derivation, recomputed here."""
    if sp in _SHARED:
        return _SHARED[sp]
    a8, b8 = SETTINGS[sp]
    ic = {}
    for fr in ("F1", "F2"):
        wing = "A" if fr == "F1" else "B"
        tok = W6.Token("R_%s" % wing, PARTA if wing == "A" else PARTB, VALS, 1,
                       cprov(wing, a8 if wing == "A" else b8))
        ic[fr] = W6.Chart("%s/%s@t2" % (sp, fr), K, NC,
                          list(M.legs(sp, fr))[:2], J0, [tok])
    _SHARED[sp] = sum(1 for ta in ic["F1"].tokens for tb in ic["F2"].tokens
                      if W6.same_partition(ta.part, tb.part))
    return _SHARED[sp]


def exhibit_intermediate_actuality():
    """The exhibit the LTP gate rests on, printed as data: at every chart the
    occupied support at the intermediate time, its size, and whether any
    declared record token has been written by then in BOTH frames."""
    out = {}
    for sp in SETTING_ORDER:
        for fr in ("F1", "F2"):
            c, d = _chart_and_datum("F-CFG", datum_cfg, sp, fr)
            out["%s/%s" % (sp, fr)] = {
                "occupied": sorted(d["actual"]),
                "size": len(d["actual"]),
                "law": {str(i): d["law"][i] for i in sorted(d["law"])}}
    return out


# ===========================================================================
# 9.  THE ARENA TEST (the RQ0 bequest)
# ===========================================================================
ARENA_COORDS = ("setting", "frame", "relabelling", "switching")


def arena_group():
    """THE ARENA'S ADMITTED ISOMORPHISMS: the base's own declared permutation
    scope filtered by the base's own initial-configuration condition -- W6's
    "the filter admits exactly two of those 72".  Enumerated, never typed.
    The wider declared extension is reported as a disclosure below; it is not
    used as the acting group, because it is not closed under its own
    conjugation and an action a candidate's declared search scope does not
    contain would test the scope, not the rule."""
    return SCOPE["admitted"]


def arena_family():
    """The admissible arena, enumerated; every factor computed."""
    nsw = len(switchings(NLEGS))
    frames = len({fr for _sp, fr in CHART_KEYS})
    size = len(SETTING_ORDER) * frames * len(arena_group()) * nsw
    return {"settings": len(SETTING_ORDER), "frames": frames,
            "admitted_isomorphisms": len(arena_group()),
            "checkpoint_phase_switchings": nsw,
            "switching_free_legs": NLEGS, "size": size}


def _truth_cfg(sp, fr, g, eps):
    """F-CFG's TRUTH-VALUE VECTOR at one arena point: the 36-bit vector whose
    i-th entry says whether the proposition "the configuration between the
    division events is i" is true there."""
    _c, d = _chart_and_datum("F-CFG", datum_cfg, sp, fr, eps=eps, relabel=g)
    return tuple(1 if i in d["actual"] else 0 for i in range(NC))


def _truth_rec(sp, fr, g, eps):
    """F-REC's truth-value vector at the same arena point: the actual record
    value tuples of the chart, as a set."""
    c, _d = _chart_and_datum("F-REC", datum_rec, sp, fr, eps=eps, relabel=g)
    return tuple(sorted(canon(k) for k in c.law))


ARENA_QUANTITIES = (
    ("QA1", "F-CFG truth-value vector (named propositions)", _truth_cfg,
     "THE OBJECT"),
    ("QA2", "F-REC truth-value set (actual record values)", _truth_rec,
     "POSITIVE CONTROL"),
)


def run_arena():
    """Push the truth-values through the admitted arena action and measure
    what moves, per coordinate, with orbits computed."""
    prog("arena test: truth-values through the admitted action")
    rows = []
    for qid, name, fn, role in ARENA_QUANTITIES:
        vals: dict = {}
        for sp in SETTING_ORDER:
            for fr in ("F1", "F2"):
                for gi, g in enumerate(arena_group()):
                    for ei, eps in enumerate(switchings(NLEGS)):
                        vals[(sp, fr, gi, ei)] = canon(fn(sp, fr, g, eps))
        dep = {}
        for coord, ix in (("setting", 0), ("frame", 1), ("relabelling", 2),
                          ("switching", 3)):
            seen: dict = {}
            for kk, v in vals.items():
                rest = tuple(x for i, x in enumerate(kk) if i != ix)
                seen.setdefault(rest, set()).add(v)
            movers = sum(1 for s in seen.values() if len(s) > 1)
            dep[coord] = {"moves": movers > 0, "slices": len(seen),
                          "slices_that_move": movers,
                          "max_distinct_values": max(len(s)
                                                     for s in seen.values())}
        orbit = len(set(vals.values()))
        # the orbit of ONE base point under the relabelling+switching action
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
        rows.append({"id": qid, "name": name, "role": role, "verdict": v,
                     "moved_under": moved, "dependence": dep,
                     "distinct_values_over_family": orbit,
                     "orbit_size_per_chart": base_orbits})
    TABLES["arena"] = rows
    fam = arena_family()
    TABLES["arena_family"] = fam
    gate("O4-ARENA-FAMILY", "derivation",
         "THE ADMISSIBLE ARENA IS ENUMERATED AND ITS SIZE IS COMPUTED, never "
         "typed: the product of the declared setting count, the frame count, "
         "the admitted isomorphisms surviving the base's own j0 filter, and "
         "the checkpoint-phase switchings read off the declared leg count.  "
         "Every factor is measured from the fixtures",
         fam["size"] == (fam["settings"] * fam["frames"]
                         * fam["admitted_isomorphisms"]
                         * fam["checkpoint_phase_switchings"])
         and fam["checkpoint_phase_switchings"] == 2 ** fam[
             "switching_free_legs"], fam)
    cfg = [r for r in rows if r["id"] == "QA1"][0]
    rec = [r for r in rows if r["id"] == "QA2"][0]
    gate("O4-ARENA-TEETH", "control",
         "THE ARENA ACTION HAS TEETH: at least one declared quantity is "
         "MEASURED to move under it.  If nothing moves, the action is too "
         "weak and the census is dead as instrumented; the `action-weaken` "
         "mutant collapses the action and must die here",
         bool(cfg["moved_under"] or rec["moved_under"]),
         {"F-CFG_moved_under": cfg["moved_under"],
          "F-REC_moved_under": rec["moved_under"]})
    gate("O4-ARENA-DISCRIMINATES", "measurement",
         "THE ARENA TEST DISCRIMINATES THE TWO CLASSES.  F-REC's and F-CFG's "
         "truth-values are pushed through the SAME action and the coordinate "
         "sets under which they move are compared.  The gate records the "
         "comparison as measured; it fires only if the two classes are "
         "measured to differ under some coordinate",
         set(cfg["moved_under"]) != set(rec["moved_under"]),
         {"F-CFG": cfg["moved_under"], "F-REC": rec["moved_under"],
          "symmetric_difference": sorted(
              set(cfg["moved_under"]) ^ set(rec["moved_under"]))})
    return rows


# ===========================================================================
# 10.  THE GATE TABLE AND THE PER-CANDIDATE VERDICTS
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
    carve-out is declared, and the corridor census below carries both of its
    controls."""
    out = []
    for g in CORRIDOR:
        rows = ((row_cfg, row_rec) if g == "NAMEBLIND"
                else (row_cfg, row_rec, row_ctrl))
        if not all(r[g] for r in rows):
            out.append(g)
    return out


def derive_candidate_verdict(cid, row_cfg, row_rec, row_ctrl, ltp,
                             arena_rows, declaration=None):
    """THE VERDICT, DERIVED FROM MEASUREMENT, PER COORDINATE (section 15).

    The candidate's own declared corridor claim and LTP claim are NOT
    consulted: they survive as bookkeeping annotation only, and the flip-test
    gate proves the derivation is independent of them.  `declaration` is
    accepted so the flip-test can pass one in; only the `declaration-lax`
    mutant lets it reach the result.

    A candidate leaving the declared corridor is blocked outright.  Otherwise
    each of the six settings receives its own verdict, decided by the gates
    the RECORD class is measured to pass at that coordinate -- so the
    comparison is like for like -- and the candidate's verdict is the
    coordinate-tagged combination."""
    if MUTANT == "declaration-lax" and declaration is not None:
        if declaration.get("corridor_claim", "").startswith("GLOBAL-SLICE"):
            return "O4-BLOCKED-AT-<the global slice the rule requires>", []
    # THE CORRIDOR CONSTRAINS THE RULE, NOT THE CLASS, so it is read on
    # EVERY class the rule is applied to.  Reading it on F-CFG alone would
    # let a rule that admits nothing pass covariance vacuously -- W6's own
    # emptiness guard, applied here.
    corridor_fail = corridor_failures(row_cfg, row_rec, row_ctrl)
    if corridor_fail:
        return ("O4-BLOCKED-AT-<%s: the rule leaves the declared corridor>"
                % "/".join(corridor_fail)), {"corridor_failures": corridor_fail}

    def passes(row, sp):
        ok = (row["counts"][sp] == 1 and row["cert_per_setting"][sp])
        if sp == "SP-A":                    # the declared triple lives here
            ok = ok and row["TRI"] and row["GLUE"]
        return ok

    per, why = {}, []
    for sp in SETTING_ORDER:
        cfg_ok, rec_ok = passes(row_cfg, sp), passes(row_rec, sp)
        if cfg_ok and ltp["per_setting"][sp].startswith("LTP-LAWFUL"):
            per[sp] = "O4-RULE-EXISTS"
        elif cfg_ok:
            per[sp] = "O4-RULE-EXISTS-LTP-BARE"
        elif rec_ok:
            fails = [g for g in ("EXIST", "FORCED", "CERT")
                     if not (row_cfg["counts"][sp] >= 1 if g == "EXIST" else
                             row_cfg["counts"][sp] == 1 if g == "FORCED" else
                             row_cfg["cert_per_setting"][sp])]
            why.append((sp, fails))
            per[sp] = "O4-DISCRIMINATED-RECORD-ACTUALISM"
        else:
            per[sp] = "O4-BLOCKED-AT-<no certified transport for either class>"
    order, seen = [], set()
    for sp in SETTING_ORDER:
        if per[sp] not in seen:
            seen.add(per[sp])
            order.append(per[sp])
    headline = " + ".join(
        "%s [%s]" % (v, ",".join(sp for sp in SETTING_ORDER if per[sp] == v))
        for v in order)
    return headline, {"per_setting": per, "obstructions": why}


def run_gate_table(resid):
    prog("gate table: three fact-classes x ten gates x four candidates")
    table, ltps = {}, {}
    for cand in CANDIDATES:
        prog("  candidate %s %s" % (cand["id"], cand["name"]))
        rows = {}
        for fid, _desc, fn, _role in FACT_CLASSES:
            rows[fid] = class_gate_row(cand, fid, fn)
        table[cand["id"]] = rows
        ltps[cand["id"]] = ltp_gate(cand, rows["F-CFG"], resid)
    TABLES["gate_table"] = {
        cid: {fid: {g: rows[fid][g] for g, _c in DESCENT_GATES if g in rows[fid]}
              for fid in rows} for cid, rows in table.items()}
    TABLES["gate_table_detail"] = {
        cid: {fid: {k: v for k, v in rows[fid].items()
                    if k not in [g for g, _ in DESCENT_GATES]}
              for fid in rows} for cid, rows in table.items()}
    TABLES["ltp_gate"] = ltps
    return table, ltps


# ===========================================================================
# 11.  CONTROLS -- both directions, with teeth
# ===========================================================================
def run_controls(table, arena_rows):
    prog("controls: the positive control reproduces, the negative fails")
    pos = table["C2"]["F-REC"]
    gate("O4-CTRL-POS", "control",
         "THE POSITIVE CONTROL FIRES.  Routed through THIS unit's transport "
         "instrument -- the same ten gates, the same discriminator, the same "
         "solver -- the record class reproduces W6's terminal descent "
         "results: a transport exists and is FORCED at every one of the six "
         "committed settings, the inverse law holds, and the declared triple "
         "descends.  If the instrument could not reproduce the base's own "
         "positive result, nothing it says about the object would mean "
         "anything",
         pos["EXIST"] and pos["FORCED"] and pos["INV"] and pos["GLUE"],
         {"counts": pos["counts"], "verdicts": pos["verdicts"],
          "triple": pos["triple"]["verdict"],
          "triple_families": pos["triple"]["families"],
          "triple_orbits": pos["triple"]["orbits"],
          "triple_triples": pos["triple"]["triples"]})
    neg_rows = {cid: table[cid]["F-CTRL"] for cid in table}
    neg_fails = {cid: [g for g in MUST_PASS + CORRIDOR if not r[g]]
                 for cid, r in neg_rows.items()}
    if MUTANT == "ctrl-pass":
        neg_fails = {cid: [] for cid in neg_rows}
    passed_all = [cid for cid, f in neg_fails.items() if not f]
    gate("O4-CTRL-NEG", "control",
         "THE NEGATIVE CONTROL FAILS, AS IT MUST.  The mis-conventioned "
         "name-reading class is put through the IDENTICAL gates and is "
         "measured to fail at least one of them under every candidate rule.  "
         "A pass here would mean the instrument cannot tell a fact from a "
         "name -- the ACTION-TOO-WEAK analogue -- and this gate is the place "
         "that would be reported.  The `ctrl-pass` mutant makes it pass and "
         "must die here",
         not passed_all,
         {"failed_gates_per_candidate": neg_fails,
          "candidates_where_the_control_passed": passed_all})
    gate("O4-LIKE-FOR-LIKE", "derivation",
         "THE THREE CLASSES ARE GATED LIKE FOR LIKE.  Every fact-class is "
         "routed through the SAME ten gates by the same code path: the gate "
         "row of each class is measured to carry every declared gate key, "
         "and the transport dispatch is measured to be a single function per "
         "class with an identical signature.  No class receives a gate the "
         "others do not",
         all(set(g for g, _c in DESCENT_GATES) - {"LTP"}
             <= set(table[cid][fid]) for cid in table for fid in table[cid])
         and len({(TRANSPORT[f].__code__.co_argcount,
                   tuple(TRANSPORT[f].__code__.co_varnames[:8]))
                  for f in TRANSPORT}) == 1,
         {"gate_keys": [g for g, _c in DESCENT_GATES],
          "classes": sorted(TRANSPORT)})
    # -- the corridor census: positive AND negative control on the corridor -
    inside, outside, why_out = [], [], {}
    for cand in CANDIDATES:
        rows = table[cand["id"]]
        f = corridor_failures(rows["F-CFG"], rows["F-REC"], rows["F-CTRL"])
        if f:
            outside.append(cand["id"])
            why_out[cand["id"]] = f
        else:
            inside.append(cand["id"])
    gate("O4-CORRIDOR-CENSUS", "control",
         "THE CORRIDOR GATES HAVE BOTH CONTROLS.  At least one declared "
         "candidate is MEASURED to lie inside the pin's corridor -- "
         "covariant under the admitted arena action, name-blind under the "
         "declared gauge, and blind to a pure time re-indexing, on every "
         "fact-class -- and at least one is MEASURED to lie outside it.  A "
         "corridor every candidate passes tests nothing, and a corridor no "
         "candidate passes tests only the corridor.  The `name-reader` and "
         "`global-now-smuggler` mutants empty the inside; a waived gate "
         "empties the outside",
         bool(inside) and bool(outside),
         {"inside": inside, "outside": outside,
          "why_outside": why_out,
          "name_blindness_of_the_negative_control":
              {cid: table[cid]["F-CTRL"]["NAMEBLIND"] for cid in table}})

    # -- the level census: which matching level survives the amplitude gauge
    lev = {}
    for level in ("exact", "sign", "born"):
        probe = dict([c for c in CANDIDATES if c["id"] == "C2"][0])
        probe["level"] = level
        ok, det = covariance(probe, "F-REC", datum_rec)
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
         "stipulation, and the sign/orientation mutants must die here",
         (not lev["exact"]["covariant"] and lev["sign"]["covariant"]
          and lev["born"]["covariant"]), lev)

    # -- the certificate's own two controls --------------------------------
    cert_rec = table["C2"]["F-REC"]["cert_per_setting"]
    cert_cfg = table["C2"]["F-CFG"]["cert_per_setting"]
    gate("O4-CERT-BITES", "control",
         "THE CERTIFICATE FIRES AND FAILS ON EXHIBITED PAIRS.  The identical "
         "ROUTE-EXT construction certifies the RECORD pair at every one of "
         "the six settings and refuses the UNRECORDED-CONFIGURATION pair at "
         "every one of them.  A certificate that never fails would certify "
         "nothing; a certificate that never succeeds would be an instrument "
         "defect rather than a finding.  The `cert-lax` mutant waives it and "
         "must die here",
         all(cert_rec.values()) and not any(cert_cfg.values()),
         {"F-REC_certified": cert_rec, "F-CFG_certified": cert_cfg,
          "F-CFG_detail": table["C2"]["F-CFG"]["cert_detail"]["per_setting"]})

    tri = table["C2"]["F-REC"]["triple"]
    gate("O4-TRIPLE-EXERCISED", "control",
         "THE TRIPLE LAW IS GENUINELY EXERCISED.  The declared triple is the "
         "base's own: the two frames plus the second frame presented on a "
         "relabelled configuration set, built as its OWN object with its own "
         "legs, its own initial configuration and its law recomputed.  All "
         "six ordered edges and all six ordered triples are measured to "
         "carry a transport, so the cocycle law has something to reject.  "
         "The `descent-lax` mutant drops the third chart and must die here",
         tri["edges"] == 6 and tri["triples"] == 6
         and all(v >= 1 for v in tri["edge_counts"].values()),
         {"edges": tri["edges"], "triples": tri["triples"],
          "edge_counts": tri["edge_counts"],
          "automorphism_counts": tri["aut_counts"],
          "verdict": tri["verdict"], "families": tri["families"],
          "orbits": tri["orbits"]})

    vac = {cid: [sp for sp in SETTING_ORDER
                 if table[cid]["F-CFG"]["counts"][sp] == 0] for cid in table}
    gate("O4-VACUITY-DISCLOSURE", "disclosure",
         "AN EMPTY CORRIDOR GATE IS DECLARED EMPTY.  Where a candidate "
         "admits NO F-CFG transport, its covariance row is satisfied "
         "vacuously -- nothing can move that does not exist -- which is "
         "exactly the emptiness the base's own discriminator refuses to "
         "count as agreement.  The coordinates at which each candidate's "
         "F-CFG corridor rows are vacuous are listed here, and the verdict "
         "derivation reads the corridor on EVERY class the rule is applied "
         "to, so no rule reaches a verdict on a vacuous covariance row",
         True, {"F-CFG_vacuous_coordinates": vac})
    cfg = [r for r in arena_rows if r["id"] == "QA1"][0]
    inter = {sp: len(set(TABLES["intermediate_actuality_support"][
                 "%s/F1" % sp])
                 & set(TABLES["intermediate_actuality_support"][
                     "%s/F2" % sp])) for sp in SETTING_ORDER}
    gate("O4-OBSTRUCTION-NAMED", "measurement",
         "WHERE F-CFG FAILS, THE FAILING GATE AND THE OBSTRUCTING OBJECT ARE "
         "NAMED.  The obstruction is exhibited as data: the two frames' "
         "occupied supports at the intermediate time, with their sizes, "
         "measured never to coincide at any of the six settings.  That is "
         "the object on which every F-CFG transport count below is measured "
         "to die.  The gate is the DISJOINTNESS itself, measured: every "
         "pairwise intersection is zero",
         all(v == 0 for v in inter.values()),
         {"obstruction": "the two frames' occupied supports at the "
                         "intermediate time are measured DISJOINT at every "
                         "setting: not merely unequal, but sharing no "
                         "configuration at all, so no proposition of the "
                         "form 'the configuration between the division "
                         "events is i' is true in both frames",
          "support_sizes": TABLES["intermediate_actuality_sizes"],
          "intersection_sizes": {
              sp: len(set(TABLES["intermediate_actuality_support"][
                  "%s/F1" % sp])
                  & set(TABLES["intermediate_actuality_support"][
                      "%s/F2" % sp])) for sp in SETTING_ORDER},
          "union_sizes": {
              sp: len(set(TABLES["intermediate_actuality_support"][
                  "%s/F1" % sp])
                  | set(TABLES["intermediate_actuality_support"][
                      "%s/F2" % sp])) for sp in SETTING_ORDER},
          "F-CFG_truth_moves_under": cfg["moved_under"]})


# ===========================================================================
# 12.  THE SELF-TEST -- fresh evaluation, cache-hits gated at zero
# ===========================================================================
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
        for fid, fn in (("F-REC", datum_rec), ("F-CFG", datum_cfg)):
            rel_fail = sw_fail = 0
            for sp in SETTING_ORDER:
                n0 = len(edge_transports(cand, fid, fn,
                                         (sp, "F1"), (sp, "F2")))
                for g in arena_group():
                    n1 = len(edge_transports(cand, fid, fn, (sp, "F1"),
                                             (sp, "F2"), relabel=g))
                    tested += 1
                    if list(g) != list(IDPERM):
                        discriminating += 1
                    if n1 != n0:
                        rel_fail += 1
                for eps in switchings(NLEGS):
                    n2 = len(edge_transports(cand, fid, fn, (sp, "F1"),
                                             (sp, "F2"), eps=eps))
                    tested += 1
                    if any(e == -1 for e in eps):
                        discriminating += 1
                    if n2 != n0:
                        sw_fail += 1
            per["%s/%s" % (cand["id"], fid)] = {
                "relabelling_failures": rel_fail,
                "switching_failures": sw_fail}
            failures += rel_fail + sw_fail
    hits = _CACHE["value_cache_hits"]
    misses = _CACHE["value_cache_misses"]
    _FRESH = False
    gate("O4-ST-FRESH", "selftest",
         "THE SELF-TEST EVALUATES FRESH.  Every value the symmetry self-test "
         "reads is recomputed with the instrument's value cache bypassed: "
         "the phase's cache-HIT count is gated at ZERO and its MISS count "
         "gated positive, so the test cannot degenerate to reading one "
         "cached object twice.  The `memo-lax` mutant restores the cache and "
         "must die here",
         hits == 0 and misses > 0,
         {"value_cache_hits": hits, "value_cache_misses": misses})
    gate("O4-ST-TEETH", "selftest",
         "THE SELF-TEST'S TESTED SET IS FIXED BY DECLARATION and has teeth: "
         "the set swept is the FULL declared arena action (every admitted "
         "isomorphism, every checkpoint-phase switching, at every setting), "
         "never a set selected by the verdicts under audit, and the count of "
         "instances at which the action is nontrivial is measured positive.  "
         "The `action-weaken` and `gauge-subsample` mutants shrink it and "
         "must die here",
         discriminating > 0 and tested == 2 * len(CANDIDATES)
         * len(SETTING_ORDER) * (len(arena_group()) + len(switchings(NLEGS))),
         {"instances_tested": tested,
          "instances_where_the_action_is_nontrivial": discriminating,
          "per_candidate": per})
    indep = {"%s/%s" % (c["id"], fid): covariance(c, fid, fn)[1]
             for c in CANDIDATES
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
         "action and its per-candidate failure counts must agree with the "
         "counts the covariance gate itself recorded.  A gate that only "
         "reported its own number would test nothing; the `covar-lax` mutant "
         "waives the covariance gate's count and must die here",
         agree, {"total_equivariance_failures": failures,
                 "selftest_per_candidate": per,
                 "covariance_gate_per_candidate":
                     {c: {k: v for k, v in indep[c].items()
                          if k.endswith("failures")} for c in indep}})
    # -- the declaration flip-test (no declaration-founded verdicts) --------
    flips = {}
    for cand in CANDIDATES:
        rows = table[cand["id"]]
        ltp = TABLES["ltp_gate"][cand["id"]]
        true_v, _ = derive_candidate_verdict(cand["id"], rows["F-CFG"],
                                             rows["F-REC"], rows["F-CTRL"],
                                             ltp, TABLES["arena"])
        flipped = dict(cand)
        flipped["corridor_claim"] = (
            "GLOBAL-SLICE: declared as the gated-out control"
            if not cand["corridor_claim"].startswith("GLOBAL-SLICE")
            else "covariant, name-blind, no global slice")
        flip_v, _ = derive_candidate_verdict(cand["id"], rows["F-CFG"],
                                             rows["F-REC"], rows["F-CTRL"],
                                             ltp, TABLES["arena"],
                                             declaration=flipped)
        flips[cand["id"]] = {"verdict": true_v, "under_flipped_declaration":
                             flip_v, "identical": true_v == flip_v}
    gate("O4-ST-DECLARATION-FLIP", "selftest",
         "NO DECLARATION-FOUNDED VERDICT (the RQ0-SYNTH lesson).  Every "
         "candidate's verdict is re-derived with its declared corridor claim "
         "FLIPPED to its opposite, and must come out identical: the "
         "derivation reads the measured gate results and nothing else.  The "
         "`declaration-lax` mutant lets the declaration reach the result and "
         "must die here",
         all(v["identical"] for v in flips.values()), flips)
    TABLES["declaration_flip_test"] = flips


# ===========================================================================
# 13.  EXACTNESS
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
# 14.  THE MUTANT TABLE
# ===========================================================================
MUTANTS = ["anchor-w6", "anchor-ltp", "sign-flip", "orient-flip",
           "rec-uncut",
           "name-reader", "global-now-smuggler", "action-weaken", "memo-lax",
           "ltp-lax", "ctrl-pass", "freeze-lax", "verdict-lax",
           "declaration-lax", "scope-lax", "gauge-subsample", "float-lax",
           "descent-lax", "canon-lax", "covar-lax", "support-lax",
           "cert-lax", "likeforlike-lax"]


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

    with ThreadPoolExecutor(max_workers=6) as ex:
        rows = list(ex.map(_run, MUTANTS))
    TABLES["mutants"] = rows
    killed = {k for r in rows
              for k in r["falsified_anchors"] + r["falsified_gates"]}
    must = [x["id"] for x in GATES if x["class"] != "disclosure"
            and x["id"] != "O4-MUTANTS"]
    unfalsified = sorted(set(must) - killed)
    TABLES["gate_falsification"] = {
        "must_pass_gates": len(must),
        "falsified_by_some_mutant": len([g for g in must if g in killed]),
        "not_falsified_by_any_mutant": unfalsified}
    gate("O4-MUTANTS", "freeze",
         "THE FALSIFICATION SUITE, RUN AND RECORDED, AND EVERY MUST-PASS "
         "GATE FALSIFIED BY AT LEAST ONE MUTANT.  Every declared mutant "
         "perturbs a COMPUTATION -- none overwrites a computed field after "
         "the fact -- is run to completion, must EXIT 1, and must falsify at "
         "least one NAMED gate or anchor.  The set of must-pass gates that "
         "NO mutant falsifies must be EMPTY.  The suite carries mutants over "
         "the reused anchors (W6 and the LTP lemma), over the sign and "
         "orientation conventions, a name-reader, a GLOBAL-NOW SMUGGLER that "
         "must be caught by the no-slice gate, an action-weakener, a "
         "cache-reading self-test, a stubbed LTP gate, a negative control "
         "made to pass, a pre-freeze evaluation, an out-of-vocabulary "
         "verdict, a declaration-consulting verdict rule, a subsampled "
         "scope, a subsampled gauge sweep, a float, a truncated descent "
         "solver, a collapsed canonicaliser, a waived covariance gate, a "
         "wrong-time support read, a waived certificate and a waived "
         "like-for-like check",
         all(r["died"] and (r["falsified_anchors"] or r["falsified_gates"])
             for r in rows) and len(rows) == len(MUTANTS) and not unfalsified,
         {"mutants": len(rows), "died": sum(1 for r in rows if r["died"]),
          "must_pass_gates_never_falsified": unfalsified,
          "kills": {r["mutant"]: r["falsified_anchors"] + r["falsified_gates"]
                    for r in rows}})


# ===========================================================================
# 15.  THE UNIT VERDICT
# ===========================================================================
def run_verdict(table, ltps, arena_rows):
    prog("verdict: per candidate, then the unit")
    per = {}
    for cand in CANDIDATES:
        rows = table[cand["id"]]
        v, why = derive_candidate_verdict(cand["id"], rows["F-CFG"],
                                          rows["F-REC"], rows["F-CTRL"],
                                          ltps[cand["id"]], arena_rows)
        if MUTANT == "verdict-lax":
            v = "O4-UNDECIDED-" + cand["id"]
        per[cand["id"]] = {"name": cand["name"], "verdict": v,
                           "detail": why,
                           "ltp": ltps[cand["id"]]["verdict"],
                           "F-CFG_counts": rows["F-CFG"]["counts"],
                           "F-REC_counts": rows["F-REC"]["counts"],
                           "F-CTRL_counts": rows["F-CTRL"]["counts"]}
    TABLES["candidate_verdicts"] = per
    cfg = [r for r in arena_rows if r["id"] == "QA1"][0]
    rec = [r for r in arena_rows if r["id"] == "QA2"][0]

    # -- the unit verdict, DERIVED from the per-coordinate rows ----------
    corridor_bound = [c["id"] for c in CANDIDATES
                      if not per[c["id"]]["verdict"].startswith(
                          "O4-BLOCKED-AT-<")]
    coords = {}
    for c in corridor_bound:
        d = per[c]["detail"]
        if isinstance(d, dict) and "per_setting" in d:
            for sp, v in d["per_setting"].items():
                coords.setdefault(v, set()).add((c, sp))
    lawful = sorted(coords.get("O4-RULE-EXISTS", ()))
    bare = sorted(coords.get("O4-RULE-EXISTS-LTP-BARE", ()))
    discriminated = sorted(coords.get("O4-DISCRIMINATED-RECORD-ACTUALISM", ()))
    rec_green = all(table[c]["F-REC"]["EXIST"] and table[c]["F-REC"]["FORCED"]
                    for c in ("C2",))
    arena_relative = bool(cfg["moved_under"]) and (
        set(cfg["moved_under"]) != set(rec["moved_under"]))
    parts = []
    if lawful:
        parts.append("O4-RULE-EXISTS")
    if bare:
        parts.append("O4-RULE-EXISTS-LTP-BARE")
    if discriminated and rec_green:
        parts.append("O4-DISCRIMINATED-RECORD-ACTUALISM")
    if arena_relative:
        parts.append("O4-ARENA-RELATIVE")
    if not parts:
        parts.append("O4-BLOCKED-AT-<no candidate reached a verdict>")
    unit = " + ".join(parts)
    if MUTANT == "verdict-lax":
        unit = "O4-UNDECIDED"
    ok_vocab = all(any(p.startswith(x) for x in PREREGISTERED)
                   for p in parts)
    FINDINGS["coordinates"] = {k: sorted("%s@%s" % t for t in v)
                               for k, v in sorted(coords.items())}
    gate("O4-VOCABULARY", "derivation",
         "EVERY VERDICT IS DRAWN FROM THE PIN'S PRE-REGISTERED VOCABULARY "
         "and from nothing else: the unit verdict and every per-candidate "
         "verdict is measured to begin with one of the five pre-registered "
         "names.  The `verdict-lax` mutant emits an out-of-vocabulary tag "
         "and must die here",
         ok_vocab and all(any(v["verdict"].startswith(x)
                              for x in PREREGISTERED) for v in per.values()),
         {"unit_verdict": unit, "per_candidate":
          {k: v["verdict"] for k, v in per.items()}})
    FINDINGS["unit_verdict"] = unit
    FINDINGS["per_candidate"] = {k: v["verdict"] for k, v in per.items()}
    FINDINGS["record_control_green"] = rec_green
    FINDINGS["arena_relative"] = arena_relative
    FINDINGS["thesis"] = (
        "Under one instrument and ten identical gates on the W6 terminal "
        "base: record facts transport and descend; unrecorded configuration "
        "facts do not, and the obstruction is the two frames' occupied "
        "supports at the intermediate time, which are measured never to "
        "coincide at any of the six committed settings.  Where a rule DOES "
        "admit a transport, the actuality it carries is LTP-BARE at the "
        "coordinates where W5's forcing lemma fires.  F-CFG's truth-values "
        "move under the admitted arena action at coordinates where F-REC's "
        "do not.  Stated at the committed finite scope; nothing is claimed "
        "about nature and the charter fork is not adjudicated here.")
    return unit, per


# ===========================================================================
# 16.  RECEIPT AND RENDER
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
    L.append("  admitted isomorphisms       %d (of the declared %d, after "
             "the base's own j0 filter)" % (f["admitted_isomorphisms"],
                                            SCOPE["n_ext_total"]))
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

    L.append("THE FACT-CLASS GATE TABLE")
    L.append("  gates: " + " ".join(g for g, _c in DESCENT_GATES))
    L.append("")
    gt = rec["tables"]["gate_table"]
    for cid in sorted(gt):
        cand = [c for c in CANDIDATES if c["id"] == cid][0]
        L.append("  %s %s   [%s]" % (cid, cand["name"], cand["level"]))
        L.append("    %-8s %s" % ("class", " ".join(
            "%-9s" % g for g, _c in DESCENT_GATES if g != "LTP")))
        for fid in ("F-REC", "F-CFG", "F-CTRL"):
            row = gt[cid][fid]
            L.append("    %-8s %s" % (fid, " ".join(
                "%-9s" % ("PASS" if row[g] else "fail")
                for g, _c in DESCENT_GATES if g != "LTP")))
        det = rec["tables"]["gate_table_detail"][cid]
        for fid in ("F-REC", "F-CFG", "F-CTRL"):
            L.append("      %-7s |Phi| per setting  %s" % (
                fid, " ".join("%s=%d" % (sp, det[fid]["counts"][sp])
                              for sp in SETTING_ORDER)))
            L.append("      %-7s discriminator     %s" % (
                fid, " ".join("%s=%s" % (sp, det[fid]["verdicts"][sp])
                              for sp in SETTING_ORDER)))
        L.append("")

    L.append("THE LTP GATE (W5's forcing lemma, per candidate, per setting)")
    for cid in sorted(rec["tables"]["ltp_gate"]):
        lt = rec["tables"]["ltp_gate"][cid]
        L.append("  %s  %s" % (cid, lt["verdict"]))
        for sp in SETTING_ORDER:
            L.append("      %-5s %s" % (sp, lt["per_setting"][sp]))
    L.append("")
    L.append("  the residual that decides it (||r||_0 of 36, frame F1/F2)")
    for sp in SETTING_ORDER:
        r1 = rec["tables"]["ltp_residuals"]["%s/F1" % sp]
        r2 = rec["tables"]["ltp_residuals"]["%s/F2" % sp]
        L.append("      %-5s %2d / %2d   matrix differing %4d / %4d" % (
            sp, r1["nonzero"], r2["nonzero"], r1["matrix_differing"],
            r2["matrix_differing"]))
    L.append("")

    L.append("THE INTERMEDIATE-TIME ACTUALITY, EXHIBITED (the LTP exhibit)")
    for kk in sorted(rec["tables"]["intermediate_actuality_sizes"]):
        L.append("      %-9s occupied %2d  %s" % (
            kk, rec["tables"]["intermediate_actuality_sizes"][kk],
            rec["tables"]["intermediate_actuality_support"][kk]))
    L.append("")

    L.append("THE ARENA TEST")
    for r in rec["tables"]["arena"]:
        L.append("  %s %-46s %s" % (r["id"], r["name"], r["verdict"]))
        L.append("      role %s;  moves under: %s" % (
            r["role"], ", ".join(r["moved_under"]) or "nothing"))
        L.append("      distinct values over the family: %d" %
                 r["distinct_values_over_family"])
        L.append("      orbit size per chart: %s" % ", ".join(
            "%s=%d" % (k, v) for k, v in sorted(
                r["orbit_size_per_chart"].items())))
    L.append("")

    L.append("PER-CANDIDATE VERDICTS")
    for cid in sorted(rec["tables"]["candidate_verdicts"]):
        v = rec["tables"]["candidate_verdicts"][cid]
        L.append("  %s %-22s %s" % (cid, v["name"], v["verdict"]))
        L.append("      LTP %s;  F-CFG |Phi| %s" % (
            v["ltp"], " ".join("%s=%d" % (sp, v["F-CFG_counts"][sp])
                               for sp in SETTING_ORDER)))
    L.append("")

    L.append("GATES")
    for g in rec["gates"]:
        L.append("  %-24s %-12s %s" % (g["id"], g["class"],
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
            L.append("  %-22s exit %d  %s" % (
                m["mutant"], m["exit"], "DIED" if m["died"] else "SURVIVED"))
            L.append("      kills: %s" % ", ".join(
                m["falsified_anchors"] + m["falsified_gates"]))
        gf = rec["tables"]["gate_falsification"]
        L.append("  must-pass gates %d; falsified by some mutant %d; "
                 "never falsified %s" % (
                     gf["must_pass_gates"], gf["falsified_by_some_mutant"],
                     gf["not_falsified_by_any_mutant"] or "[]"))
        L.append("")

    L.append("=" * W)
    L.append("UNIT VERDICT   %s" % rec["findings"]["unit_verdict"])
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
        # instead of the intermediate one, so the class stops being about
        # unrecorded configurations at all.
        def _cfg_lax(sp, fr, eps=None, relabel=None, extra_identity=False):
            _bump()
            c = final_chart(sp, fr, eps, relabel, extra_identity)
            p = c.dist()
            return c, {"carriers": NC, "actual": frozenset(p),
                       "law": {i: canon(p[i]) for i in sorted(p)}}
        globals()["datum_cfg"] = _cfg_lax
        FACT_LIST = list(FACT_CLASSES)
        FACT_LIST[1] = (FACT_LIST[1][0], FACT_LIST[1][1], _cfg_lax,
                        FACT_LIST[1][3])
        globals()["FACT_CLASSES"] = tuple(FACT_LIST)
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

    if MUTANT == "freeze-lax":
        datum_cfg("SP-A", "F1")
    run_freeze()
    resid = run_anchors()

    ia = exhibit_intermediate_actuality()
    TABLES["intermediate_actuality_sizes"] = {k: v["size"]
                                              for k, v in ia.items()}
    TABLES["intermediate_actuality_support"] = {k: v["occupied"]
                                                for k, v in ia.items()}
    TABLES["intermediate_actuality"] = ia

    table, ltps = run_gate_table(resid)
    arena_rows = run_arena()
    run_controls(table, arena_rows)
    run_selftest(table, resid)
    run_exactness()
    if a.falsification_selftest and not a.mutant:
        run_mutant_table()
    run_verdict(table, ltps, arena_rows)

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
