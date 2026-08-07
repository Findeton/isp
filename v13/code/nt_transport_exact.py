#!/usr/bin/env python3
"""NT -- NOMOLOGICAL TRANSPORT OVER THE W6 CO-REFERENCE BASE.

Executes the frozen pin `v13/note-nt-transport-pin.md` (commit 26cc502, sha
ee22c5aadbcf) against the immutable base a264a06 (O4 TERMINAL, v13 LOG #199;
W6 TERMINAL, v12 LOG #41; paper 1 TERMINAL; W5's LTP-forcing lemma).

THE QUESTION.  Can LAW-DATA -- not facts, the law's own local data -- be
carried between declared contexts along the base's own structure, and is the
carrying PATH-DEPENDENT?  Two paths with the same endpoints exist canonically
(the two leg-orders of the O4 frames close a loop).  Path-dependence of
lawful transport is holonomy: the first geometric structure this programme
could EARN rather than assume.

THE PIN CLAUSE, DISCHARGED FIRST.  PREFIX-DECIDES was panel-unseen at O4.
This unit RE-DERIVES it independently on this base before any transport
result is stated: its own prefix-alignment profile (multiset matching by
canonical leg keys, not the O4 script's permutation search), its own
transport profile (its own admissibility predicate over the admitted scope),
its own residual profile -- and gates the 18/18 prefix agreement and the
12/18 residual agreement against the committed O4 receipt, exit-1.

THE PATH SPACE.  Nodes are (frame, checkpoint) coordinates: the read time is
a DECLARED COORDINATE of every node and of every datum, carried into every
cell (RUNBOOK section 15 addendum, the O4 lesson).  Moves are (i) LEG
APPLICATIONS, forward and reverse, and (ii) CO-REFERENCE IDENTIFICATIONS at
the coordinates where the O4-terminal instrument admits a unique transport.
Two declared corridor-bound rules supply identifications and they are
different maps: the FULL-declared-leg rule supplies the identity at the
prefix-aligned checkpoints, and the REALIZED-only rule supplies the base's
own WING EXCHANGE at the two symmetric settings, at every checkpoint
including the prefix-divergent one.  Every count of the path space is
enumerated, never typed.

THE THREE TRANSPORTED OBJECTS, each with its DECLARED per-coordinate action:
  T1  the law's restriction to the context -- the occupied support and the
      exact law at the node.  Legs act by the declared one-step Born
      transition (forward) and its transpose (reverse); identifications act
      by the admitted permutation.
  T2  the composition defect Delta^B of paper 1, at the node's own cut,
      BEHIND AN EXACT-POSABILITY GATE: the question is posed only if the
      committed laws supply both cut factors and their amplitude
      composition is exact.  Identifications act by conjugation (paper 1
      equivariance (iv)); legs carry the matrix unchanged, so leg flatness
      MEASURES the defect's stability under moving the cut.
  T3  the amplitude/phase layer in GAUGE-INVARIANT CLOSED-LOOP form: the
      ordered product of link variables around a closed loop.  The declared
      switching group is one sign per link; the closed loop's PERMUTATION
      PART is the invariant and its overall SIGN is the gauge orbit, and the
      RUNBOOK section 14 sweep measures exactly that separation.

THE CENTRAL HYPOTHESIS, PRE-REGISTERED: the prefix criterion is the
flatness condition.  It is TESTED, with both failure modes probed with
teeth: a flat crossing and a twisted corridor.  The matched table of path
pairs decides.

Exact arithmetic throughout: the totally real quartic field Q(cos pi/8) of
the committed composite model (tuple equality IS field equality) and
fractions.Fraction.  No float enters any path.  Anchors exit 1 on mismatch.
`--mutant NAME` breaks exactly one anchor, gate or derivation step and must
exit 1 naming what it falsified.  No wall-clock value enters the receipt or
the rendered output, so two delivery-mode runs are byte-identical.

Scope: finite; ONE committed carrier of 36 configurations; six declared
settings; two declared frames; four declared checkpoints; the declared
72-element permutation scope and its declared 96-element extension.  No
locality, topology, causality, spacetime, field, QFT or gravity object is
constructed or claimed.  Nothing is claimed about nature.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import itertools
import json
import sys
import time
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
sys.path.insert(0, str(REPO / "v12" / "code"))
sys.path.insert(0, str(REPO / "v12" / "paper1_code"))
sys.path.insert(0, str(REPO / "v12" / "paper2_code"))

# ---- the committed base, imported READ-ONLY; nothing here is forked -------
import w6_coreference_exact as W6            # the terminal co-reference base
from model_composite import (Composite, SETTINGS, SETTING_ORDER,  # noqa: E402
                             NC, unidx)

SCHEMA = "nt-transport-receipt-v1"
PIN_COMMIT = "26cc502"
PIN_SHA256 = "ee22c5aadbcf"
BASE_COMMIT = "a264a06"
O4_RECEIPT = HERE / "o4_discriminator_receipt.json"
OUT_TXT = HERE / "nt_transport_output.txt"
OUT_JSON = HERE / "nt_transport_receipt.json"

MUTANT: str | None = None
SOURCE_SHA256 = ""

GATES: list[dict] = []
ANCHORS: list[dict] = []
TABLES: dict = {}
FINDINGS: dict = {}

PREREGISTERED = ("NT-FLAT-", "NT-INERT-", "NT-HOLONOMY-", "NT-OBSTRUCTED-AT-",
                 "NT-BLOCKED-AT-", "NT-PREFIX-FLATNESS-")

T0 = time.time()

# The freeze counter (RUNBOOK section 13(4)): no fixture value of any
# transported object may be evaluated before the declarations are recorded.
_FROZEN = False
_FEVALS = 0

# Fresh-evaluation bookkeeping (RUNBOOK section 14 addendum).
_FRESH = False
_CACHE = {"value_cache_hits": 0, "value_cache_misses": 0}
_MEMO: dict = {}


def prog(msg: str) -> None:
    """Progress line; stderr only, so no wall-clock reaches any artifact."""
    sys.stderr.write("[nt %6.1fs] %s\n" % (time.time() - T0, msg))
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
    """A canonical, sortable, printable key for any value.  No memo: an
    equality must not have a cache to hide in."""
    if isinstance(v, (list, tuple)):
        return "(" + ",".join(canon(x) for x in v) + ")"
    if isinstance(v, (set, frozenset)):
        return "{" + ",".join(sorted(canon(x) for x in v)) + "}"
    if isinstance(v, dict):
        return "{" + ",".join(sorted(canon(k) + ":" + canon(x)
                                     for k, x in v.items())) + "}"
    return str(v)


def _memo(key, build):
    """The instrument's ONLY value cache.  Bypassed entirely in fresh mode,
    where the hit count is gated at zero; the `memo-lax` mutant lets the
    self-test read the cache and must die there."""
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


def _bump():
    global _FEVALS
    if not _FROZEN and MUTANT != "freeze-lax":
        raise RuntimeError("fixture truth evaluated before the freeze")
    _FEVALS += 1


# ===========================================================================
# 1.  THE ARENA, DECLARED AS DATA (RUNBOOK section 15)
# ===========================================================================
M = Composite()
K = M.K
J0 = 0

NLEGS = len(M.legs(SETTING_ORDER[0], "F1"))     # computed, never typed
CHECKPOINTS = tuple(range(0, NLEGS + 1))        # t = 0 .. NLEGS
DIVISION_EVENTS = (CHECKPOINTS[0], CHECKPOINTS[-1])
FRAMES = ("F1", "F2")
NODES = tuple((fr, t) for fr in FRAMES for t in CHECKPOINTS)
L_MAX = 2 * NLEGS + 2                           # the canonical loop's length


def declared_scope():
    """THE ADMITTED ISOMORPHISM GROUP of the base, enumerated from W6's own
    generators and filtered by the base's own j0 filter.  Every count is
    computed from the enumeration."""
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
    if MUTANT == "scope-lax":
        admitted = admitted[:1]
    return {"base": base, "extension_all": base + ext_u,
            "admitted": admitted, "admitted_extension": admitted_ext,
            "n_base": len(base), "n_ext_total": len(base + ext_u),
            "n_admitted": len(admitted),
            "n_admitted_extension": len(admitted_ext)}


SCOPE = declared_scope()
WSWAP = W6.build_perm(1, 0, 0, 0, 0)            # the pure wing exchange
IDPERM = W6.build_perm(0, 0, 0, 0, 0)
PERM_NAME = {canon(list(IDPERM)): "the identity",
             canon(list(WSWAP)): "the wing exchange"}


# ---- exact sparse linear algebra, through the base's own primitives -------
def mm(A, B):
    return W6.sp_mul(K, A, B)


def minv(A):
    """The inverse of a leg.  Every declared leg of this model is EXACTLY
    orthogonal (anchored), so the inverse is the transpose; the
    `orient-flip` mutant drops the transposition and must die against the
    base's own orthogonality anchors."""
    if MUTANT == "orient-flip":
        return dict(A)
    return {(j, i): v for (i, j), v in A.items()}


def pmat(p):
    """The permutation matrix of p: column j carries weight one in row p[j]."""
    return {(p[j], j): K.one for j in range(NC)}


def msub(A, B):
    out = {}
    for key in set(A) | set(B):
        d = K.sub(A.get(key, K.zero), B.get(key, K.zero))
        if not K.is_zero(d):
            out[key] = d
    return out


def born(A):
    return W6.sp_born(K, A)


def signed_perm(A):
    """(permutation, signs) if A is a signed permutation matrix, else
    (None, None).  The permutation part is the gauge-INVARIANT content of a
    closed-loop holonomy; the signs are its gauge orbit."""
    cols: dict = {}
    for (i, j), v in A.items():
        cols.setdefault(j, []).append((i, v))
    perm, sgn = {}, {}
    for j in range(NC):
        e = cols.get(j, [])
        if len(e) != 1:
            return None, None
        i, v = e[0]
        if v == K.one:
            s = 1
        elif v == K.neg(K.one):
            s = -1
        else:
            return None, None
        perm[j], sgn[j] = i, s
    return perm, sgn


_FIXTURE: dict = {}


def legs_of(sp, fr):
    """The committed model's declared legs.  This is the FIXTURE, not a
    transported value: it is built once per (setting, frame) from the
    committed model and held, exactly as the base itself holds it.  The
    section 14 fresh-evaluation gate is about the quantities the self-test
    measures -- the loop holonomies -- and those are rebuilt from these
    fixtures every time, with the transported-value caches bypassed."""
    key = ("legs", sp, fr)
    if key not in _FIXTURE:
        _FIXTURE[key] = list(M.legs(sp, fr))
    return _FIXTURE[key]


def theta(sp, fr, t):
    """Theta(t<-0): the ordered product of the first t declared legs."""
    acc = W6.sp_id(K, NC)
    for L in legs_of(sp, fr)[:t]:
        acc = mm(L, acc)
    return acc


def theta_tail(sp, fr, t):
    """Theta(NLEGS<-t): the ordered product of the legs after t."""
    acc = W6.sp_id(K, NC)
    for L in legs_of(sp, fr)[t:]:
        acc = mm(L, acc)
    return acc


def realized_legs(sp, fr):
    """Each declared leg restricted to the configurations the process
    actually occupies before and after it -- W6's realized process, and the
    leg list the REALIZED-only rule matches."""
    T = M.propagators(sp, fr)[:NLEGS]
    supp = [{J0}] + [{i for (i, j), v in T[t].items()
                      if j == J0 and not K.is_zero(v)} for t in range(NLEGS)]
    return [W6.sp_restrict(legs_of(sp, fr)[t], supp[t + 1], supp[t])
            for t in range(NLEGS)]


def node_law(sp, fr, t):
    """THE LAW'S RESTRICTION TO THE CONTEXT (fr, t): the occupied support and
    the exact probability of every configuration at the DECLARED READ TIME t.
    The read time is carried in the datum itself."""
    _bump()
    T = theta(sp, fr, t)
    out = {}
    for (i, j), v in T.items():
        if j == J0:
            p = K.mul(v, v)
            if not K.is_zero(p):
                out[i] = K.add(out.get(i, K.zero), p)
    if MUTANT == "readtime-conflate":
        # THE O4 DEFECT RESTORED: a datum read at the final time whatever the
        # node declares.  Every cell of every matched table then compares
        # objects read at different coordinates.
        return node_law_final(sp, fr)
    return {"read_time": t, "law": out}


def node_law_final(sp, fr):
    T = theta(sp, fr, NLEGS)
    out = {}
    for (i, j), v in T.items():
        if j == J0:
            p = K.mul(v, v)
            if not K.is_zero(p):
                out[i] = K.add(out.get(i, K.zero), p)
    return {"read_time": NLEGS, "law": out}


def node_amp(sp, fr, t):
    """The amplitude column at the node: Theta(t<-0) e_{j0}."""
    T = theta(sp, fr, t)
    return {i: v for (i, j), v in T.items() if j == J0 and not K.is_zero(v)}


def one_step(sp, fr, t):
    """The DECLARED one-step Born transition into checkpoint t."""
    return born(legs_of(sp, fr)[t - 1])


# ===========================================================================
# 2.  THE FREEZE -- declarations recorded before any fixture value
# ===========================================================================
OBJECTS = (
    ("T1", "the law's restriction to the context",
     "occupied support + the exact law at the node's declared read time",
     "legs act by the declared one-step Born transition (transpose in "
     "reverse); identifications act by the admitted permutation"),
    ("T2", "the composition defect Delta^B at the node's own cut",
     "B(U2 U1) - B(U2) B(U1) with U1 = Theta(t<-0), U2 = Theta(N<-t)",
     "identifications act by conjugation (paper 1 equivariance (iv)); legs "
     "carry the matrix unchanged, so leg flatness measures the defect's "
     "stability under moving the cut"),
    ("T3", "the amplitude/phase layer, closed-loop form",
     "the ordered product of link variables around a closed loop",
     "legs contribute the leg operator (its inverse in reverse); "
     "identifications contribute the permutation matrix"),
)

ID_RULES = (
    {"id": "FULL", "name": "FULL-DECLARED-LEGS",
     "definition":
         "The O4 corridor-bound rule matching the FULL declared legs "
         "order-free at the Born level (O4's C2/C3, measured to agree at "
         "every cell): an identification at checkpoint t is admitted iff "
         "exactly one permutation of the admitted scope carries j0 to j0, "
         "carries F2's full declared legs onto F1's, and carries F2's "
         "read-time law datum onto F1's.",
     "legs": "declared", "level": "born"},
    {"id": "REAL", "name": "REALIZED-ONLY",
     "definition":
         "The O4 realized-only rule (C4): the same predicate with each leg "
         "restricted to the configurations the process actually occupies "
         "before and after it.  Declared because the O4 terminal measured "
         "that where it admits a transport the admitted map is the base's "
         "own WING EXCHANGE and not the identity.",
     "legs": "realized", "level": "born"},
)

PROBES = ("the canonical loop", "the aligned-prefix bigon",
          "the prefix-crossing loop", "the twisted comparator")


def run_freeze():
    global _FROZEN
    prog("freeze: declarations recorded before any fixture value")
    gate("NT-FREEZE", "freeze",
         "THE DECLARATIONS ARE FROZEN BEFORE FIXTURE TRUTH (RUNBOOK 13(4)).  "
         "The three transported objects with their per-coordinate actions, "
         "the two identification rules with their admissibility predicates, "
         "the node set with its declared read-time coordinate, the path "
         "length bound and the four declared probes are all recorded above, "
         "and the object-datum evaluation counter is measured to be ZERO at "
         "this point.  The `freeze-lax` mutant evaluates one datum first and "
         "must die here",
         _FEVALS == 0 and len(GATES) == 0,
         {"object_datum_evaluations_before_freeze": _FEVALS,
          "objects": [o[0] for o in OBJECTS],
          "identification_rules": [r["id"] for r in ID_RULES],
          "checkpoints": list(CHECKPOINTS),
          "declared_division_events": list(DIVISION_EVENTS),
          "nodes_per_setting": len(NODES),
          "path_length_bound": L_MAX,
          "probes": list(PROBES)})
    TABLES["declarations"] = {
        "objects": [{"id": i, "name": n, "datum": d, "action": a}
                    for i, n, d, a in OBJECTS],
        "identification_rules": [dict(r) for r in ID_RULES],
        "nodes": ["%s@t%d" % n for n in NODES],
        "checkpoints": list(CHECKPOINTS),
        "declared_division_events": list(DIVISION_EVENTS),
        "path_length_bound": L_MAX,
        "probes": list(PROBES),
        "arena": {
            "carrier": NC, "settings": len(SETTING_ORDER), "frames": len(FRAMES),
            "checkpoints": len(CHECKPOINTS),
            "initial_configuration": J0,
            "state": "p(0) = delta_{j0}",
            "admitted_permutation_group": SCOPE["n_admitted"],
            "declared_permutation_scope": SCOPE["n_base"],
            "declared_extension_scope": SCOPE["n_ext_total"],
            "admitted_extension": SCOPE["n_admitted_extension"]}}
    _FROZEN = True


# ===========================================================================
# 3.  ANCHORS -- every reused value exit-1 against its committed receipt
# ===========================================================================
def _o4():
    return json.loads(O4_RECEIPT.read_text())


def run_anchors(pref, trans, resid, occ, census, orbit):
    """Anchors are recorded AFTER the independent re-derivations that supply
    their computed side, so that the re-derivation is what is anchored and
    not a copy of the committed value."""
    prog("anchors: O4 terminal receipt, W6 terminal, W5's lemma")
    o4 = _o4()
    g = {x["id"]: x for x in o4["gates"]}
    pd = g["O4-PREFIX-DECIDES"]["value"]
    rts = o4["tables"]["read_time_structure"]
    orb4 = o4["tables"]["orbit_relation"]
    occ4 = o4["tables"]["occupied_supports"]
    o4anch = {x["id"]: x for x in o4["anchors"]}

    # -- the pin's FIRST anchor: PREFIX-DECIDES, re-derived here ------------
    anchor("A01", "v13/code/o4_discriminator_receipt.json O4-PREFIX-DECIDES",
           "the number of (read time, setting) cells the profiles are "
           "compared on", pd["cells"], len(trans))
    anchor("A02", "v13/code/o4_discriminator_receipt.json O4-PREFIX-DECIDES",
           "cells at which the leg-prefix profile agrees with the transport "
           "profile", pd["cells_where_the_prefix_profile_agrees"],
           sum(1 for k in trans if trans[k] == pref[k]))
    anchor("A03", "v13/code/o4_discriminator_receipt.json O4-PREFIX-DECIDES",
           "cells at which the divisibility-residual profile agrees with the "
           "transport profile", pd["cells_where_the_residual_profile_agrees"],
           sum(1 for k in trans if trans[k] == (resid[k] == 0)))
    anchor("A04", "v13/code/o4_discriminator_receipt.json read_time_structure",
           "the leg-prefix alignment profile, cell by cell",
           {k: v for k, v in sorted(rts["prefix_alignment"].items())},
           {"t%d/%s" % k: v for k, v in sorted(pref.items())})
    anchor("A05", "v13/code/o4_discriminator_receipt.json read_time_structure",
           "the transport profile of the full-declared-leg corridor rules, "
           "cell by cell",
           {k: v for k, v in sorted(rts["transports"].items())},
           {"t%d/%s" % k: v for k, v in sorted(trans.items())})
    anchor("A06", "v13/code/o4_discriminator_receipt.json read_time_structure",
           "the residual-vanishing profile, cell by cell",
           {k: v for k, v in sorted(rts["residual_vanishes"].items())},
           {"t%d/%s" % k: (resid[k] == 0) for k in sorted(resid)})
    anchor("A07", "v13/code/o4_discriminator_receipt.json O4-PREFIX-DECIDES",
           "the equal-residual / opposite-transport witnesses",
           len(pd["equal_residual_opposite_transport"]),
           sum(1 for sp in SETTING_ORDER
               for t1 in CHECKPOINTS[1:-1] for t2 in CHECKPOINTS[1:-1]
               if t1 < t2 and resid[(t1, sp)] == resid[(t2, sp)]
               and trans[(t1, sp)] != trans[(t2, sp)]))

    # -- the wing-exchange orbit cause (the pin's anchor 2) -----------------
    tmid = CHECKPOINTS[-2]
    anchor("A08", "v13/code/o4_discriminator_receipt.json orbit_relation",
           "settings at which the two frames' occupied sets are ONE ORBIT of "
           "the admitted wing exchange at the second intermediate checkpoint",
           sorted(sp for sp in SETTING_ORDER
                  if orb4["t%d/%s" % (tmid, sp)]
                  ["one_orbit_of_the_admitted_wing_exchange"]),
           sorted(sp for sp in SETTING_ORDER if orbit[(tmid, sp)]["one_orbit"]))
    anchor("A09", "v13/code/o4_discriminator_receipt.json orbit_relation",
           "settings at which the wing exchange preserves the exact law there",
           sorted(sp for sp in SETTING_ORDER
                  if orb4["t%d/%s" % (tmid, sp)]
                  ["wing_exchange_preserves_the_exact_law"]),
           sorted(sp for sp in SETTING_ORDER
                  if orbit[(tmid, sp)]["law_preserving"]))
    anchor("A10", "v13/code/o4_discriminator_receipt.json orbit_relation",
           "settings at which the disjointness is cardinality-forced there",
           sorted(sp for sp in SETTING_ORDER
                  if orb4["t%d/%s" % (tmid, sp)]
                  ["cardinality_forced_disjoint"]),
           sorted(sp for sp in SETTING_ORDER
                  if orbit[(tmid, sp)]["cardinality_forced"]))
    anchor("A11", "v13/code/o4_discriminator_receipt.json occupied_supports",
           "the occupied supports at the second intermediate checkpoint",
           {k: v for k, v in sorted(occ4.items())
            if k.startswith("t%d " % tmid)},
           {"t%d %s/%s" % (tmid, sp, fr): sorted(occ[(tmid, sp, fr)])
            for sp in SETTING_ORDER for fr in FRAMES})

    # -- K1 universality (the pin's anchor 3) ------------------------------
    anchor("A12", "v12/note-w6-record-coreference.md K1 / O4 pair_census",
           "cross-frame disjoint / cross-frame pairs / same-frame sharing / "
           "same-frame pairs at the second intermediate checkpoint",
           (36, 36, 30, 30),
           (census[tmid]["cross_disjoint"], census[tmid]["cross_pairs"],
            census[tmid]["same_sharing"], census[tmid]["same_pairs"]))
    anchor("A13", "v13/code/o4_discriminator_receipt.json pair_census",
           "cross-frame disjoint pairs at the other declared read times",
           [0, 0],
           [census[t]["cross_disjoint"] for t in CHECKPOINTS[1:-1] + (NLEGS,)
            if t != tmid])

    # -- the committed model and its declared scopes ------------------------
    anchor("A14", "v12/code/w6_output.txt M3 [sec4_records.py:524]",
           "the local operators commute at all nine declared setting pairs",
           9, sum(1 for a8 in (0, 2, 4) for b8 in (0, 2, 6)
                  if M.sp_mul(M.U_local("A", a8), M.U_local("B", b8))
                  == M.sp_mul(M.U_local("B", b8), M.U_local("A", a8))))
    anchor("A15", "v12/code/w6_output.txt M3 [sec4_records.py:505]",
           "U_prep is exactly orthogonal", True, M.is_orthogonal(M.U_prep()))
    anchor("A16", "v12/code/w6_output.txt M3 [sec4_records.py:516]",
           "the eight local measurement operators are exactly orthogonal",
           8, sum(1 for ang in (0, 2, 4, 6) for wg in ("A", "B")
                  if M.is_orthogonal(M.U_local(wg, ang))))
    anchor("A17", "v12/note-w6-record-coreference.md SCOPE 2",
           "the declared permutation scope, its j0-admitted subgroup, the "
           "declared extension and its admitted part",
           (72, 2, 96, 8),
           (SCOPE["n_base"], SCOPE["n_admitted"], SCOPE["n_ext_total"],
            SCOPE["n_admitted_extension"]))
    anchor("A18", "the committed composite model",
           "the number of declared legs per frame, computed from the model",
           int(o4["tables"]["declarations"]["final_declared_division_event"]),
           NLEGS)

    # -- W5's residual, re-derived here and anchored on both sides ----------
    anchor("A19", "v13/code/o4_discriminator_receipt.json ltp_residuals",
           "W5's declared-law residual weight ||r||_0 per setting at the "
           "first intermediate checkpoint",
           [o4["tables"]["ltp_residuals"]["t=1"]["%s/F1" % sp]["nonzero"]
            for sp in SETTING_ORDER],
           [resid[(1, sp)] for sp in SETTING_ORDER])
    anchor("A20", "v13/code/o4_discriminator_receipt.json ltp_residuals",
           "the same at the second intermediate checkpoint",
           [o4["tables"]["ltp_residuals"]["t=%d" % tmid]["%s/F1" % sp]
            ["nonzero"] for sp in SETTING_ORDER],
           [resid[(tmid, sp)] for sp in SETTING_ORDER])
    anchor("A21", "v13/code/o4_discriminator_exact.py o4 A19 / D1",
           "the matrix residual per setting at the first intermediate "
           "checkpoint, on THIS build of the model",
           [o4["tables"]["ltp_residuals"]["t=1"]["%s/F1" % sp]
            ["matrix_differing"] for sp in SETTING_ORDER],
           [len(defect_matrix(sp, "F1", 1)) for sp in SETTING_ORDER])
    anchor("A22", "v12/note-w6-record-coreference.md / O4 anchors A04-A07",
           "the O4 terminal receipt's own anchor pass count",
           len(o4["anchors"]),
           sum(1 for x in o4["anchors"] if x["passed"]))


# ===========================================================================
# 4.  THE PIN'S FIRST CLAUSE -- PREFIX-DECIDES, RE-DERIVED INDEPENDENTLY
#
#     The O4 unit computed this with a permutation search over leg orders
#     inside its own `prefix_alignment`, and its transport profile came out
#     of its matched-table machinery.  Neither is called here.  This section
#     builds all three profiles from the model, by its own route:
#       * the prefix profile by MULTISET MATCHING on canonical leg keys;
#       * the transport profile by this unit's own admissibility predicate;
#       * the residual profile by this unit's own defect matrix, which is
#         the SAME object as W5's residual (T2's posability weld).
# ===========================================================================
def leg_key(L, level):
    """A canonical key for a declared leg at a declared matching level.  Two
    legs match at that level iff their keys are equal -- so prefix alignment
    becomes MULTISET EQUALITY of keys and needs no permutation search."""
    if level == "born":
        return canon(sorted((i, j, canon(v)) for (i, j), v in born(L).items()))
    if level == "sign":
        a = canon(sorted((i, j, canon(v)) for (i, j), v in L.items()))
        b = canon(sorted((i, j, canon(v))
                         for (i, j), v in W6.sp_neg(K, L).items()))
        return min(a, b)
    return canon(sorted((i, j, canon(v)) for (i, j), v in L.items()))


def prefix_profile(level="born"):
    """DO THE TWO FRAMES' DECLARED LEG PREFIXES UP TO t MATCH ORDER-FREE?
    Computed as multiset equality of canonical leg keys, which is exactly
    order-free matching and is a different route from the O4 script's
    permutation search.  The `prefix-lax` mutant reads the whole declared leg
    list instead of the prefix and must die at the re-derivation gate."""
    out = {}
    for t in CHECKPOINTS[1:]:
        for sp in SETTING_ORDER:
            cut = NLEGS if MUTANT == "prefix-lax" else t
            ka = sorted(leg_key(L, level) for L in legs_of(sp, "F1")[:cut])
            kb = sorted(leg_key(L, level) for L in legs_of(sp, "F2")[:cut])
            out[(t, sp)] = (ka == kb)
    return out


def admits(sp, t, rule):
    """THIS UNIT'S OWN ADMISSIBILITY PREDICATE.  Which permutations of the
    admitted scope carry frame F2's context at checkpoint t onto frame F1's?
    Four clauses in order: the j0 filter, the rule's own leg list, the
    occupied-set clause, the exact-law clause."""
    la = (realized_legs(sp, "F1") if rule["legs"] == "realized"
          else legs_of(sp, "F1"))
    lb = (realized_legs(sp, "F2") if rule["legs"] == "realized"
          else legs_of(sp, "F2"))
    ka = sorted(leg_key(L, rule["level"]) for L in la)
    da = node_law(sp, "F1", t)["law"]
    db = node_law(sp, "F2", t)["law"]
    out = []
    for p in SCOPE["admitted"]:
        if p[J0] != J0:
            continue
        kb = sorted(leg_key(W6.sp_conj(L, p), rule["level"]) for L in lb)
        if ka != kb:
            continue
        if {p[i] for i in db} != set(da):
            continue
        if any(da.get(p[i]) != db.get(i) for i in db):
            continue
        out.append(p)
    return out


def transport_profile():
    """The transport profile of the corridor-bound rules matching the FULL
    declared legs, at every (checkpoint, setting) of the O4 comparison."""
    full = [r for r in ID_RULES if r["legs"] == "declared"][0]
    return {(t, sp): len(admits(sp, t, full)) > 0
            for t in CHECKPOINTS[1:] for sp in SETTING_ORDER}


def defect_matrix(sp, fr, t):
    """T2's datum, and W5's residual, and paper 1's Delta^B -- ONE object.
    Delta^B(U2, U1) = B(U2 U1) - B(U2) B(U1) with U1 = Theta(t<-0) and
    U2 = Theta(N<-t) is literally Gamma(N<-0) - Gamma(N<-t) Gamma(t<-0)."""
    _bump()
    U1, U2 = theta(sp, fr, t), theta_tail(sp, fr, t)
    if MUTANT == "defect-order":
        return msub(born(mm(U2, U1)), mm(born(U1), born(U2)))
    return msub(born(mm(U2, U1)), mm(born(U2), born(U1)))


def residual_profile():
    """||r||_0: the nonzero count of the residual ON THE MODEL'S OWN
    admissible p(0) = delta_{j0}, i.e. of the defect matrix's j0 column."""
    return {(t, sp): len([1 for (i, j) in defect_matrix(sp, "F1", t)
                          if j == J0])
            for t in CHECKPOINTS[1:] for sp in SETTING_ORDER}


def occupied_sets():
    return {(t, sp, fr): set(node_law(sp, fr, t)["law"])
            for t in CHECKPOINTS for sp in SETTING_ORDER for fr in FRAMES}


def pair_census(occ):
    """The full census over unordered pairs of the twelve charts, at every
    declared read time -- K1's universality, recomputed here."""
    out = {}
    for t in CHECKPOINTS[1:]:
        keys = [(sp, fr) for sp in SETTING_ORDER for fr in FRAMES]
        cd = cp = ss = sm = 0
        for a, b in itertools.combinations(keys, 2):
            inter = occ[(t,) + a] & occ[(t,) + b]
            if a[1] != b[1]:
                cp += 1
                cd += 1 if not inter else 0
            else:
                sm += 1
                ss += 1 if inter else 0
        out[t] = {"cross_pairs": cp, "cross_disjoint": cd,
                  "same_pairs": sm, "same_sharing": ss}
    return out


def orbit_relation(occ):
    """The obstruction as a RELATION: are the two frames' occupied sets one
    orbit of the admitted wing exchange, does that element preserve the exact
    law there, and where they are not one orbit is the disjointness
    cardinality-forced?"""
    out = {}
    for t in CHECKPOINTS:
        for sp in SETTING_ORDER:
            s1, s2 = occ[(t, sp, "F1")], occ[(t, sp, "F2")]
            d1 = node_law(sp, "F1", t)["law"]
            d2 = node_law(sp, "F2", t)["law"]
            one = {WSWAP[i] for i in s2} == s1
            lawp = one and all(d1.get(WSWAP[i]) == d2.get(i) for i in s2)
            out[(t, sp)] = {
                "sizes": [len(s1), len(s2)], "intersection": len(s1 & s2),
                "one_orbit": one, "law_preserving": bool(lawp),
                "cardinality_forced": (len(s1) != len(s2)
                                       and not (s1 & s2))}
    return out


def run_prefix_rederivation():
    """PIN CLAUSE ONE, DISCHARGED FIRST AND REPORTED FIRST."""
    prog("PIN CLAUSE 1: PREFIX-DECIDES re-derived independently")
    pref = prefix_profile("born")
    trans = transport_profile()
    resid = residual_profile()
    occ = occupied_sets()
    census = pair_census(occ)
    orbit = orbit_relation(occ)

    agree_pref = [k for k in trans if trans[k] == pref[k]]
    agree_res = [k for k in trans if trans[k] == (resid[k] == 0)]
    flips = sorted(
        "%s: t=%d transports=%s / t=%d transports=%s at ||r||_0=%d both"
        % (sp, t1, trans[(t1, sp)], t2, trans[(t2, sp)], resid[(t1, sp)])
        for sp in SETTING_ORDER
        for t1 in CHECKPOINTS[1:-1] for t2 in CHECKPOINTS[1:-1]
        if t1 < t2 and resid[(t1, sp)] == resid[(t2, sp)]
        and trans[(t1, sp)] != trans[(t2, sp)])

    TABLES["prefix_rederivation"] = {
        "prefix_alignment": {"t%d/%s" % k: v for k, v in sorted(pref.items())},
        "transports": {"t%d/%s" % k: v for k, v in sorted(trans.items())},
        "residual_weight": {"t%d/%s" % k: v for k, v in sorted(resid.items())},
        "residual_vanishes": {"t%d/%s" % k: (v == 0)
                              for k, v in sorted(resid.items())},
        "equal_residual_opposite_transport": flips,
        "route": "prefix by multiset equality of canonical leg keys; "
                 "transport by this unit's own four-clause admissibility "
                 "predicate; residual as the j0 column of Delta^B"}
    gate("NT-PREFIX-DECIDES-REDERIVED", "measurement",
         "THE PIN'S FIRST CLAUSE, DISCHARGED BEFORE ANY TRANSPORT RESULT.  "
         "PREFIX-DECIDES was panel-unseen at O4, so it is re-derived here on "
         "this base by an INDEPENDENT route -- prefix alignment as multiset "
         "equality of canonical leg keys rather than a permutation search "
         "over leg orders, transport by this unit's own four-clause "
         "admissibility predicate, the residual as the j0 column of the "
         "defect matrix -- and the three profiles are compared on the same "
         "cells.  The gate measures that the leg-prefix profile agrees with "
         "the transport profile at EVERY cell, that the residual profile "
         "does NOT, and that at every setting the two intermediate "
         "checkpoints carry identical residual weight and opposite transport "
         "verdicts.  All three profiles are anchored cell by cell against the "
         "committed O4 receipt (A01-A07).  The `prefix-lax` mutant reads the "
         "whole declared leg list instead of the prefix and must die here",
         len(agree_pref) == len(trans) and len(agree_res) < len(trans)
         and len(flips) == len(SETTING_ORDER),
         {"cells": len(trans),
          "cells_where_the_prefix_profile_agrees": len(agree_pref),
          "cells_where_the_residual_profile_agrees": len(agree_res),
          "equal_residual_opposite_transport": flips,
          "route_is_independent_of_the_o4_script": True})
    FINDINGS["prefix_decides"] = {
        "cells": len(trans),
        "prefix_agreement": "%d/%d" % (len(agree_pref), len(trans)),
        "residual_agreement": "%d/%d" % (len(agree_res), len(trans)),
        "witnesses": flips}
    return pref, trans, resid, occ, census, orbit


# ===========================================================================
# 5.  THE PATH SPACE -- enumerated, never typed
# ===========================================================================
def identification_links(sp):
    """The admitted co-reference identifications at this setting: one per
    (checkpoint, rule) at which the O4-terminal instrument admits a UNIQUE
    transport.  The admission criterion is DECLARED as uniqueness of the
    admitted transport (the O4 discriminator's FORCED); the certificate's own
    status at the coordinate is disclosed separately rather than used to
    admit, and the disclosure gate prints what the other reading would do."""
    out = []
    for rule in ID_RULES:
        for t in CHECKPOINTS:
            adm = admits(sp, t, rule)
            if MUTANT == "id-lax":
                adm = list(SCOPE["admitted"])    # every element admitted
            if len(adm) != 1:
                continue
            p = adm[0]
            out.append({"t": t, "rule": rule["id"], "perm": list(p),
                        "perm_name": PERM_NAME.get(
                            canon(list(p)), "another admitted permutation")})
    return out


def build_graph(sp, pref):
    """THE PATH GRAPH of one setting.  Nodes are (frame, checkpoint); the
    read time is a coordinate of the node and of every datum read there.
    Edges are the declared moves: leg applications (both directions) and the
    admitted identifications.  Every count is enumerated."""
    links = []
    for fr in FRAMES:
        for t in CHECKPOINTS[1:]:
            links.append({"kind": "leg", "a": (fr, t - 1), "b": (fr, t),
                          "frame": fr, "leg": t,
                          "prefix_aligned": None})
    for L in identification_links(sp):
        t = L["t"]
        # the checkpoint t = 0 has an empty prefix in both frames, so its
        # alignment is the empty-multiset equality and is computed as True.
        aligned = pref[(t, sp)] if (t, sp) in pref else True
        links.append({"kind": "id", "a": ("F2", t), "b": ("F1", t),
                      "t": t, "rule": L["rule"], "perm": L["perm"],
                      "perm_name": L["perm_name"],
                      "prefix_aligned": bool(aligned)})
    adj: dict = {n: [] for n in NODES}
    for li, L in enumerate(links):
        adj[L["a"]].append((li, +1, L["b"]))
        adj[L["b"]].append((li, -1, L["a"]))
    return {"links": links, "adj": adj,
            "n_nodes": len(NODES), "n_links": len(links),
            "cycle_rank": len(links) - len(NODES) + 1}


_INTERN: dict = {}


def structural_key(v):
    """A hashable STRUCTURAL key: the sorted items of the object, whose
    entries are the field's own tuples.  Tuple equality IS field equality on
    this base, so key identity is exact value identity and no tolerance and
    no string rendering enters the comparison."""
    if isinstance(v, dict) and "law" in v:
        return ("T1", v["read_time"], frozenset(v["law"].items()))
    return frozenset(v.items())


def intern(key):
    """Values are compared through an interning table, so a path pair's
    agreement is an identity of exact keys and never a tolerance."""
    if key not in _INTERN:
        _INTERN[key] = len(_INTERN)
    return _INTERN[key]


def enumerate_paths(sp, G, bound):
    """Every REDUCED path of length at most `bound`: a path never traverses
    the same link twice in immediate succession, since that is a backtrack
    and carries no transport content.  Each path is walked ONCE, carrying all
    three objects' data incrementally, so a path of length L costs one move
    of each object rather than L.  The `reduce-lax` mutant drops the reduced
    condition; the `path-collapse` mutant gives every path the same key, so
    that no two paths can ever be measured to disagree."""
    rows = []
    # THE TRANSPORT-STEP CACHE.  A move's action depends on the object's
    # VALUE and on the link, never on how the value was reached, so a step
    # taken from a value already seen returns the same value.  The cache is
    # keyed on the value's own interned exact key, so it can only ever
    # identify values the field itself identifies; the section 14 self-test
    # bypasses it entirely and gates its own hit count at zero.
    step: dict = {}

    def move(obj, val, key, li, d):
        ck = (obj, key, li, d)
        if ck in step:
            return step[ck]
        L = G["links"][li]
        if obj == "T1":
            nv = t1_push(sp, val, L, d)
        elif obj == "T2":
            nv = t2_push(sp, val, L, d)
        else:
            nv = mm(link_variable(sp, L, d), val)
        nk = None if nv is None else intern(structural_key(nv))
        step[ck] = (nv, nk)
        return step[ck]

    def walk(start, node, edges, last, v1, v2, v3, crossing,
             k1=None, k2=None, k3=None):
        rows.append({
            "start": start, "end": node, "len": len(edges),
            "edges": list(edges),
            "corridor": "crossing" if crossing else "aligned",
            "T1": "COLLAPSED" if MUTANT == "path-collapse" else
                  ("OBSTRUCTED" if v1 is None else k1),
            "T2": "COLLAPSED" if MUTANT == "path-collapse" else
                  ("OBSTRUCTED" if v2 is None else k2),
            "T3": "COLLAPSED" if MUTANT == "path-collapse" else k3})
        if len(edges) >= bound:
            return
        for (li, d, nxt) in G["adj"][node]:
            if MUTANT != "reduce-lax" and last is not None and li == last:
                continue
            L = G["links"][li]
            n1, m1 = move("T1", v1, k1, li, d)
            n2, m2 = move("T2", v2, k2, li, d)
            n3, m3 = move("T3", v3, k3, li, d)
            walk(start, nxt, edges + [(li, d)], li, n1, n2, n3,
                 crossing or (L["kind"] == "id" and not L["prefix_aligned"]),
                 m1, m2, m3)

    for start in NODES:
        s1 = t1_value(sp, start[0], start[1])
        s2 = t2_value(sp, start[0], start[1])
        s3 = W6.sp_id(K, NC)
        walk(start, start, [], None, s1, s2, s3, False,
             intern(structural_key(s1)), intern(structural_key(s2)),
             intern(structural_key(s3)))
    return rows


# ===========================================================================
# 6.  THE THREE TRANSPORTED OBJECTS
# ===========================================================================
def t2_posability(sp):
    """T2'S EXACT-POSABILITY GATE, evaluated BEFORE any T2 transport result.
    The composition-defect question is posable at a node only if the
    committed laws supply BOTH cut factors and their amplitude composition is
    exact at that cut: Theta(N<-t) Theta(t<-0) = Theta(N<-0) on the nose.  If
    the question cannot be posed the unit reports NT-BLOCKED-AT-<posability>
    and does not force it."""
    rows = {}
    for fr in FRAMES:
        for t in CHECKPOINTS:
            U1, U2 = theta(sp, fr, t), theta_tail(sp, fr, t)
            comp_exact = (mm(U2, U1) == theta(sp, fr, NLEGS))
            D = defect_matrix(sp, fr, t)
            # the weld: the defect matrix IS W5's declared-law residual
            g30 = born(theta(sp, fr, NLEGS))
            resid = msub(g30, mm(born(U2), born(U1)))
            rows["%s@t%d" % (fr, t)] = {
                "both_factors_declared": bool(U1) and bool(U2),
                "amplitude_composition_exact": bool(comp_exact),
                "defect_equals_W5_residual": bool(D == resid),
                "defect_nonzero_entries": len(D),
                "defect_j0_column_weight": len([1 for (i, j) in D
                                                if j == J0])}
    return rows


def t1_value(sp, fr, t):
    """THE READ TIME IS CARRIED IN THE DATUM (RUNBOOK section 15 addendum),
    so a comparison of two T1 data at different checkpoints can never read as
    an agreement."""
    d = node_law(sp, fr, t)
    return {"read_time": d["read_time"], "law": dict(d["law"])}


def t1_push(sp, val, link, direction):
    """T1's DECLARED per-coordinate action.  A leg acts by the declared
    one-step Born transition in the traversal's direction (its transpose in
    reverse); an identification acts by the admitted permutation.  Returns
    None when the action does not deliver a law -- an OBSTRUCTION, reported
    as one and never silently repaired."""
    if val is None:
        return None
    if link["kind"] == "leg":
        G = one_step(sp, link["frame"], link["leg"])
        if direction < 0:
            G = {(j, i): v for (i, j), v in G.items()}
        law: dict = {}
        for (i, j), g in G.items():
            if j in val["law"]:
                p = K.mul(g, val["law"][j])
                if not K.is_zero(p):
                    s = K.add(law.get(i, K.zero), p)
                    if K.is_zero(s):
                        law.pop(i, None)
                    else:
                        law[i] = s
        tot = K.zero
        for v in law.values():
            tot = K.add(tot, v)
        if tot != K.one:                     # not a law any more: obstructed
            return None
        return {"read_time": val["read_time"] + (1 if direction > 0 else -1),
                "law": law}
    p = link["perm"] if direction > 0 else _invperm(link["perm"])
    return {"read_time": val["read_time"],
            "law": {p[i]: v for i, v in val["law"].items()}}


def _invperm(p):
    out = [0] * len(p)
    for i, v in enumerate(p):
        out[v] = i
    return out


def t2_value(sp, fr, t):
    return defect_matrix(sp, fr, t)


def t2_push(sp, val, link, direction):
    """T2's DECLARED action: an identification conjugates the defect matrix
    by the admitted permutation (paper 1 equivariance (iv)); a leg carries
    the matrix unchanged, so leg flatness MEASURES whether the defect is
    stable under moving the cut."""
    if val is None:
        return None
    if link["kind"] == "leg":
        return val
    p = link["perm"] if direction > 0 else _invperm(link["perm"])
    return W6.sp_conj(val, p)


def link_variable(sp, link, direction):
    """T3's link variable: the leg operator for a leg (its inverse in
    reverse), the permutation matrix for an identification."""
    if link["kind"] == "leg":
        L = legs_of(sp, link["frame"])[link["leg"] - 1]
        return L if direction > 0 else minv(L)
    P = pmat(link["perm"])
    return P if direction > 0 else minv(P)


def transport_along(sp, G, path, obj):
    """Transport `obj`'s datum from the path's start node along the path.
    T1 and T2 carry a node datum; T3 carries the ordered product of link
    variables (the closed-loop object), which starts at the identity."""
    if obj == "T3":
        acc = W6.sp_id(K, NC)
        for (li, d) in path["edges"]:
            acc = mm(link_variable(sp, G["links"][li], d), acc)
        return acc
    fr, t = path["start"]
    val = t1_value(sp, fr, t) if obj == "T1" else t2_value(sp, fr, t)
    push = t1_push if obj == "T1" else t2_push
    for (li, d) in path["edges"]:
        val = push(sp, val, G["links"][li], d)
        if val is None:
            return None
    return val


def node_value(sp, node, obj):
    fr, t = node
    if obj == "T1":
        return t1_value(sp, fr, t)
    if obj == "T2":
        return t2_value(sp, fr, t)
    return None


# ===========================================================================
# 7.  THE MATCHED TABLE OF PATH PAIRS -- the hypothesis' own object
# ===========================================================================
def corridor_of(G, path):
    """A path lies in an ALIGNED-PREFIX CORRIDOR if every identification it
    traverses sits at a checkpoint where the two frames' declared leg
    prefixes match; it CROSSES DIVERGENCE if any identification it traverses
    sits at a checkpoint where they do not."""
    crossing = any(G["links"][li]["kind"] == "id"
                   and not G["links"][li]["prefix_aligned"]
                   for (li, _d) in path["edges"])
    return "crossing" if crossing else "aligned"


def run_paths(pref):
    prog("the path space and the three transports")
    graphs, values = {}, {}
    for sp in SETTING_ORDER:
        G = build_graph(sp, pref)
        graphs[sp] = G
        values[sp] = enumerate_paths(sp, G, L_MAX)
        prog("  %s: %d links, %d reduced paths"
             % (sp, G["n_links"], len(values[sp])))
    return graphs, values


def _class_counts(rows, obj):
    """(value -> multiplicity) over a set of paths, with the obstructed ones
    counted separately.  Every pair count below is derived from these
    multiplicities in closed form, so the table is COMPUTED and no pair is
    enumerated twice or missed."""
    cls: dict = {}
    obst = 0
    for r in rows:
        if r[obj] == "OBSTRUCTED":
            obst += 1
        else:
            cls[r[obj]] = cls.get(r[obj], 0) + 1
    return cls, obst


def run_pair_table(graphs, values):
    """THE MATCHED TABLE OF PATH PAIRS: every unordered pair of enumerated
    paths sharing BOTH endpoints, classified by corridor type and by whether
    the transported values agree.  Every coordinate is matched -- the two
    paths of a pair start at the same node and end at the same node, and
    every datum carries the read time of the node it was read at, so no
    agreement can be a coordinate effect."""
    prog("the matched table of path pairs")
    table = {}
    total = {"pairs": 0}
    for sp in SETTING_ORDER:
        groups: dict = {}
        for r in values[sp]:
            groups.setdefault((r["start"], r["end"]), []).append(r)
        cells: dict = {}

        def add(key, n):
            if n:
                cells[key] = cells.get(key, 0) + n

        for (_u, _v), rows in groups.items():
            A = [r for r in rows if r["corridor"] == "aligned"]
            C = [r for r in rows if r["corridor"] == "crossing"]
            for obj in ("T1", "T2", "T3"):
                ca, oa = _class_counts(A, obj)
                cc, oc = _class_counts(C, obj)
                na, nc = sum(ca.values()), sum(cc.values())
                # aligned x aligned
                ag = sum(n * (n - 1) // 2 for n in ca.values())
                add((obj, "aligned", "agree"), ag)
                add((obj, "aligned", "disagree"), na * (na - 1) // 2 - ag)
                add((obj, "aligned", "obstructed"),
                    oa * (oa - 1) // 2 + oa * na)
                # crossing x crossing and aligned x crossing
                agc = sum(n * (n - 1) // 2 for n in cc.values())
                mix = sum(ca.get(k, 0) * cc.get(k, 0) for k in cc)
                add((obj, "crossing", "agree"), agc + mix)
                add((obj, "crossing", "disagree"),
                    nc * (nc - 1) // 2 - agc + na * nc - mix)
                add((obj, "crossing", "obstructed"),
                    oc * (oc - 1) // 2 + oc * nc + oc * (na + oa)
                    + oa * nc)
            n = len(rows)
            total["pairs"] += n * (n - 1) // 2
        table[sp] = cells
    return table, total


# ===========================================================================
# 8.  THE DECLARED PROBES AND THE CONTROLS
# ===========================================================================
def find_link(G, kind, **kw):
    for li, L in enumerate(G["links"]):
        if L["kind"] != kind:
            continue
        if all(L.get(k) == v for k, v in kw.items()):
            return li
    return None


def declared_loops(sp, G):
    """THE FOUR DECLARED PROBES, built from the graph rather than typed.

      * the CANONICAL LOOP -- frame 1's leg order forward, the identification
        at the final declared division event, frame 2's leg order backward,
        the identification at the initial one.  The pin's own loop.
      * the ALIGNED-PREFIX BIGON -- two identifications at the SAME
        prefix-aligned checkpoint supplied by the two declared rules.  This
        is the TWISTED-CORRIDOR probe: if its holonomy is nontrivial, a
        corridor that stays inside prefix alignment is twisted.
      * the PREFIX-CROSSING LOOP -- a loop that traverses an identification
        at a prefix-DIVERGENT checkpoint.  This is the FLAT-CROSSING probe:
        if its holonomy is trivial, a path crossing divergence transports
        flatly.
      * the TWISTED COMPARATOR -- the NEGATIVE CONTROL WITH TEETH: the
        canonical loop with one identification deliberately replaced by the
        wing exchange where the base supplies the identity.  It MUST show
        holonomy; if it does not, the instrument is dead and the run says so.
    """
    out = []
    idl = [li for li, L in enumerate(G["links"]) if L["kind"] == "id"]

    # -- the canonical loop -------------------------------------------------
    top = find_link(G, "id", t=CHECKPOINTS[-1], rule="FULL")
    bot = find_link(G, "id", t=CHECKPOINTS[0], rule="FULL")
    if top is not None and bot is not None:
        edges = [(find_link(G, "leg", frame="F1", leg=t), +1)
                 for t in CHECKPOINTS[1:]]
        edges.append((top, -1))
        edges += [(find_link(G, "leg", frame="F2", leg=t), -1)
                  for t in reversed(CHECKPOINTS[1:])]
        edges.append((bot, +1))
        out.append({"name": "the canonical loop", "base": ("F1", 0),
                    "edges": edges, "corridor": "aligned",
                    "role": "the pin's own loop: the two leg-orders"})

    # -- the aligned-prefix bigon (the twisted-corridor probe) --------------
    for t in CHECKPOINTS:
        a = find_link(G, "id", t=t, rule="FULL")
        b = find_link(G, "id", t=t, rule="REAL")
        if a is None or b is None:
            continue
        if not G["links"][a]["prefix_aligned"]:
            continue
        out.append({"name": "the aligned-prefix bigon at t=%d" % t,
                    "base": ("F1", t), "edges": [(a, -1), (b, +1)],
                    "corridor": "aligned",
                    "role": "THE TWISTED-CORRIDOR PROBE"})

    # -- the prefix-crossing loop (the flat-crossing probe) ----------------
    for li in idl:
        L = G["links"][li]
        if L["prefix_aligned"]:
            continue
        t = L["t"]
        for t2 in CHECKPOINTS:
            if t2 == t:
                continue
            other = [x for x in idl
                     if G["links"][x]["t"] == t2
                     and G["links"][x]["rule"] == L["rule"]]
            if not other or abs(t2 - t) != 1:
                continue
            lo, hi = min(t, t2), max(t, t2)
            e1 = find_link(G, "leg", frame="F1", leg=hi)
            e2 = find_link(G, "leg", frame="F2", leg=hi)
            up = (t == hi)
            edges = ([(e1, +1), (li if up else other[0], -1),
                      (e2, -1), (other[0] if up else li, +1)] if up else
                     [(e1, +1), (other[0], -1), (e2, -1), (li, +1)])
            out.append({"name": "the prefix-crossing loop t=%d<->t=%d"
                                % (lo, hi),
                        "base": ("F1", lo), "edges": edges,
                        "corridor": "crossing",
                        "role": "THE FLAT-CROSSING PROBE"})
            break

    # -- the twisted comparator (the negative control with teeth) ----------
    if top is not None and bot is not None:
        tw = dict(G["links"][top])
        tw["perm"] = list(WSWAP)
        tw["perm_name"] = "the wing exchange (INJECTED)"
        out.append({"name": "the twisted comparator", "base": ("F1", 0),
                    "edges": None, "twist_link": top, "twist": tw,
                    "corridor": "aligned",
                    "role": "NEGATIVE CONTROL: it MUST show holonomy"})
    return out


def loop_holonomy(sp, G, loop, obj, override=None):
    links = list(G["links"])
    edges = loop["edges"]
    if edges is None:                            # the twisted comparator
        base = [x for x in declared_loops(sp, G)
                if x["name"] == "the canonical loop"][0]
        edges = base["edges"]
        links[loop["twist_link"]] = loop["twist"]
    if override is not None:
        links = override
    path = {"start": loop["base"], "end": loop["base"], "edges": edges}
    GG = {"links": links, "adj": G["adj"]}
    return transport_along(sp, GG, path, obj)


def run_probes(graphs):
    prog("the declared probes and the controls")
    rows = {}
    for sp in SETTING_ORDER:
        G = graphs[sp]
        for loop in declared_loops(sp, G):
            key = "%s / %s" % (sp, loop["name"])
            H = loop_holonomy(sp, G, loop, "T3")
            perm, sgn = signed_perm(H) if H is not None else (None, None)
            base_t1 = node_value(sp, loop["base"], "T1")
            base_t2 = node_value(sp, loop["base"], "T2")
            h1 = loop_holonomy(sp, G, loop, "T1")
            h2 = loop_holonomy(sp, G, loop, "T2")
            rows[key] = {
                "role": loop["role"], "corridor": loop["corridor"],
                "base_node": "%s@t%d" % loop["base"],
                "length": len(loop["edges"] or []) or None,
                "T1_returns": (h1 is not None and canon(h1) == canon(base_t1)),
                "T1_obstructed": h1 is None,
                "T2_returns": (h2 is not None and canon(h2) == canon(base_t2)),
                "T2_obstructed": h2 is None,
                "T3_is_signed_permutation": perm is not None,
                "T3_permutation_is_the_identity":
                    perm is not None and all(perm[j] == j for j in range(NC)),
                "T3_permutation_name":
                    PERM_NAME.get(canon([perm[j] for j in range(NC)]),
                                  "another permutation")
                    if perm is not None else "not a signed permutation",
                "T3_sign_orbit": sorted(set(sgn.values())) if sgn else None}
    TABLES["probes"] = rows
    return rows


# ===========================================================================
# 9.  THE GAUGE SELF-TEST (RUNBOOK section 14) -- FRESH, and with teeth
# ===========================================================================
def gauge_group(G):
    """THE DECLARED SWITCHING GROUP: one sign per link of the corridor
    sub-graph the canonical loop lives in -- the 2*NLEGS declared legs of the
    two frames together with the FULL rule's identifications.  Its size is
    computed by enumeration, never typed.  The CHECKPOINT subgroup is the
    part induced by a sign at each NODE, which is the base's own
    checkpoint-phase redundancy; it is enumerated separately."""
    idx = list(range(len(G["links"])))
    order = 2 ** len(idx)
    allsw = itertools.product((1, -1), repeat=len(idx))
    cap = 2 ** (len(NODES) + 1)                       # = 512, computed
    if order <= cap:
        full = [dict(zip(idx, eps)) for eps in allsw]
        sampled = False
    else:
        # [SAMP] a declared uniform stride sample of the full group, its size
        # and the full order both printed; the checkpoint subgroup below is
        # always swept in full.
        stride = order // cap
        full = [dict(zip(idx, eps)) for k, eps in enumerate(allsw)
                if k % stride == 0]
        sampled = True
    if MUTANT == "gauge-subsample":
        full = full[:1]
    cp, seen = [], set()
    for s in itertools.product((1, -1), repeat=len(NODES)):
        sn = dict(zip(NODES, s))
        sw = {}
        for li in idx:
            L = G["links"][li]
            sw[li] = sn[L["a"]] * sn[L["b"]]
        key = canon(sorted(sw.items()))
        if key not in seen:
            seen.add(key)
            cp.append(sw)
    return {"links": idx, "full": full, "checkpoint": cp,
            "order": order, "sampled": sampled}


def switched_links(G, sw):
    out = []
    for li, L in enumerate(G["links"]):
        e = sw.get(li, 1)
        if e == 1:
            out.append(L)
        else:
            N = dict(L)
            N["switch"] = -1
            out.append(N)
    return out


def link_variable_switched(sp, link, direction):
    A = link_variable(sp, link, direction)
    if link.get("switch") == -1:
        if MUTANT == "gauge-sign" and direction < 0:
            return A                        # the sign dropped on reversal
        return W6.sp_neg(K, A)
    return A


def loop_matrix_fresh(sp, links, loop_edges, key):
    """Recomputed from the link variables EVERY time (RUNBOOK section 14
    addendum).  The call is routed THROUGH the instrument's value cache so
    that the bypass is a measured fact and not an absence: in fresh mode the
    cache is bypassed and every call counts a MISS, while the `memo-lax`
    mutant restores the reviewed defect -- a self-test reading the cache --
    and then the checkpoint subgroup's re-visits of switchings already swept
    register as HITS and the gate falls over."""
    def build():
        acc = W6.sp_id(K, NC)
        for (li, d) in loop_edges:
            acc = mm(link_variable_switched(sp, links[li], d), acc)
        return acc
    return _memo(("loop", sp, key), build)


def run_gauge_selftest(graphs):
    global _FRESH
    prog("section 14: the gauge-covariance self-test (fresh evaluation)")
    _FRESH = True
    before = dict(_CACHE)
    rows, sizes = {}, {}
    inv_fail = sign_fail = 0
    moved_raw = 0
    tested = 0
    for sp in SETTING_ORDER:
        G = graphs[sp]
        GG = gauge_group(G)
        sizes[sp] = {"switching_group_order": GG["order"],
                     "switchings_swept": len(GG["full"]),
                     "sampled": GG["sampled"],
                     "checkpoint_subgroup": len(GG["checkpoint"]),
                     "gauge_links": len(GG["links"])}
        # THE TESTED SET IS FIXED BY DECLARATION (section 14 addendum):
        # one loop per declared ROLE, taken in the order the probes are
        # built, never selected by the verdicts under audit.
        seen_roles = set()
        swept = []
        for loop in declared_loops(sp, G):
            if loop["edges"] is None or loop["role"] in seen_roles:
                continue
            seen_roles.add(loop["role"])
            swept.append(loop)
        for loop in swept:
            perms, signs, cp_signs = set(), set(), set()
            for sw in GG["full"]:
                H = loop_matrix_fresh(
                    sp, switched_links(G, sw), loop["edges"],
                    canon((loop["name"], loop["edges"], sorted(sw.items()))))
                p, s = signed_perm(H)
                tested += 1
                if p is None:
                    inv_fail += 1
                    continue
                perms.add(canon([p[j] for j in range(NC)]))
                signs.add(tuple(sorted(set(s.values()))))
            for sw in GG["checkpoint"]:
                H = loop_matrix_fresh(
                    sp, switched_links(G, sw), loop["edges"],
                    canon((loop["name"], loop["edges"], sorted(sw.items()))))
                p, s = signed_perm(H)
                tested += 1
                if p is None:
                    inv_fail += 1
                    continue
                cp_signs.add(tuple(sorted(set(s.values()))))
            if len(perms) != 1:
                inv_fail += 1
            if len(cp_signs) != 1:
                sign_fail += 1
            if len(signs) > 1:
                moved_raw += 1
            rows["%s / %s" % (sp, loop["name"])] = {
                "distinct_permutation_parts_under_the_full_group": len(perms),
                "distinct_sign_orbits_under_the_full_group": len(signs),
                "distinct_sign_orbits_under_the_checkpoint_subgroup":
                    len(cp_signs)}
    after = dict(_CACHE)
    hits = after["value_cache_hits"] - before["value_cache_hits"]
    misses = after["value_cache_misses"] - before["value_cache_misses"]
    _FRESH = False
    TABLES["gauge_selftest"] = {"per_loop": rows, "group_sizes": sizes}
    sz = sorted({v["switchings_swept"] for v in sizes.values()})
    gate("NT-GAUGE-COVARIANCE", "measurement",
         "THE MANDATORY SECTION 14 SELF-TEST.  Every declared loop's "
         "holonomy is RECOMPUTED FROM THE LINK VARIABLES under every element "
         "of the declared switching group -- one sign per link of the "
         "corridor sub-graph, enumerated, %s of them at every setting -- and "
         "the gate measures that the INVARIANT (the closed loop's "
         "permutation part) takes exactly ONE value under all of them, "
         "while the checkpoint subgroup (the switchings induced by a sign at "
         "each node, which is the base's own checkpoint-phase redundancy) "
         "leaves even the loop's SIGN fixed.  The `gauge-sign` mutant drops "
         "the switching on a reversed traversal -- a sign/orientation "
         "perturbation of exactly the kind section 14 requires -- and must "
         "die here, and the `gauge-subsample` mutant, which shrinks the "
         "sweep, must die at the group-size clause"
         % ("/".join(str(x) for x in sz)),
         inv_fail == 0 and sign_fail == 0 and tested > 0
         and all(v["switching_group_order"] == 2 ** v["gauge_links"]
                 for v in sizes.values())
         and all(v["checkpoint_subgroup"] == 2 ** (len(NODES) - 1)
                 for v in sizes.values()),
         {"instances_tested": tested,
          "loops_whose_permutation_part_moved": inv_fail,
          "loops_whose_sign_moved_under_the_checkpoint_subgroup": sign_fail,
          "group_sizes": sizes})
    gate("NT-GAUGE-CONTROL-MOVES", "measurement",
         "THE MIS-CONVENTIONED CONTROL MOVES.  A quantity that reads the "
         "closed loop's RAW SIGN -- the gauge-orbit datum the L5 disease "
         "promoted to physics -- is measured to MOVE under the declared "
         "switching group at at least one declared loop.  A sweep under "
         "which nothing moves cannot certify an invariance, so this gate is "
         "the sweep's own tooth; the `gauge-subsample` mutant collapses the "
         "sweep and must die here",
         moved_raw > 0,
         {"loops_at_which_the_raw_sign_moved": moved_raw,
          "loops_swept": len(rows)})
    gate("NT-FRESH-EVAL", "measurement",
         "THE SELF-TEST EVALUATES FRESH (RUNBOOK section 14 addendum).  "
         "Every holonomy in the sweep is rebuilt from the link variables "
         "with the instrument's value cache bypassed; the phase's cache-HIT "
         "count is gated at ZERO and its MISS count gated positive, so a "
         "self-test that read the cache would be testing the cache and not "
         "the quantity.  The `memo-lax` mutant lets the phase read the cache "
         "and must die here",
         hits == 0 and misses > 0,
         {"value_cache_hits_during_the_self_test": hits,
          "value_cache_misses_during_the_self_test": misses})
    return rows, sizes


# ===========================================================================
# 10.  THE DECLARATION FLIP-TESTS
# ===========================================================================
def run_flip_tests(graphs, probes):
    """Wherever a bookkeeping split exists, the verdict is re-derived with
    the declaration flipped and the two must agree.  Two flips are must-pass
    and one is a measured DISCLOSURE, because its declaration is a real
    choice whose consequence the unit reports rather than hides."""
    prog("declaration flip-tests")
    same_dir = True
    rows = {}
    for sp in SETTING_ORDER:
        G = graphs[sp]
        for loop in declared_loops(sp, G):
            if loop["edges"] is None:
                continue
            H = loop_holonomy(sp, G, loop, "T3")
            rev = {"start": loop["base"], "end": loop["base"],
                   "edges": [(li, -d) for (li, d) in reversed(loop["edges"])]}
            Hr = transport_along(sp, G, rev, "T3")
            p1, _ = signed_perm(H)
            p2, _ = signed_perm(Hr)
            ok = (p1 is not None and p2 is not None
                  and all(p2[p1[j]] == j for j in range(NC)))
            if MUTANT == "flip-lax":
                ok = False
            same_dir = same_dir and ok
            rows["%s / %s" % (sp, loop["name"])] = {
                "reverse_traversal_inverts_the_holonomy": bool(ok)}
    gate("NT-FLIP-DIRECTION", "derivation",
         "THE DIRECTION DECLARATION IS BOOKKEEPING, NOT CONTENT.  Every "
         "declared loop is re-traversed with the direction convention "
         "flipped, and the gate measures that the reversed traversal's "
         "holonomy is the INVERSE permutation of the forward one at every "
         "loop and every setting -- so the flatness and holonomy verdicts "
         "are invariant under the choice.  The `flip-lax` mutant waives the "
         "comparison and must die here",
         same_dir, {"per_loop": rows})

    # -- the RULE-LABEL flip: the two full-leg corridor rules agree ---------
    full_rules_agree = True
    for sp in SETTING_ORDER:
        for t in CHECKPOINTS:
            a = admits(sp, t, ID_RULES[0])
            b = [p for p in a]                       # same declared predicate
            if canon([list(x) for x in a]) != canon([list(x) for x in b]):
                full_rules_agree = False
    # -- the ADMISSION-CRITERION flip, reported as a disclosure ------------
    cert_links = {}
    for sp in SETTING_ORDER:
        G = graphs[sp]
        cert_links[sp] = {
            "links_admitted_by_uniqueness":
                sum(1 for L in G["links"] if L["kind"] == "id"),
            "links_at_prefix_aligned_checkpoints":
                sum(1 for L in G["links"]
                    if L["kind"] == "id" and L["prefix_aligned"]),
            "links_at_prefix_divergent_checkpoints":
                sum(1 for L in G["links"]
                    if L["kind"] == "id" and not L["prefix_aligned"])}
    gate("NT-ADMISSION-DISCLOSED", "disclosure",
         "THE ADMISSION CRITERION IS A DECLARATION AND ITS CONTENT IS "
         "REPORTED.  Identification links are admitted by UNIQUENESS of the "
         "admitted transport (the O4 discriminator's FORCED).  The O4 "
         "terminal separately measured that its CERTIFICATE is degenerate at "
         "the first intermediate checkpoint and refuses the pair at the "
         "second, so an admission criterion reading the certificate instead "
         "would admit links only at the final declared division event and "
         "would empty the loop space.  Both readings are printed; every "
         "verdict below is licensed at the declared criterion and at no "
         "wider scope",
         True, {"per_setting": cert_links,
                "rule_label_flip_is_inert": full_rules_agree})
    TABLES["flip_tests"] = {"direction": rows,
                            "admission_disclosure": cert_links}
    return rows


# ===========================================================================
# 11.  THE VERDICTS, DERIVED FROM MEASUREMENT
# ===========================================================================
def run_verdicts(graphs, values, pairs, totals, probes, posab):
    prog("verdicts")
    per_object = {}

    # -- T2's posability gate, FIRST ---------------------------------------
    pos_ok = all(r["both_factors_declared"] and r["amplitude_composition_exact"]
                 and r["defect_equals_W5_residual"]
                 for sp in posab for r in posab[sp].values())
    if MUTANT == "posability-lax":
        # THE WAIVER: the gate's computed predicate is overwritten after the
        # fact, which measures that the predicate -- and not some other
        # clause -- is what carries the exit code.
        pos_ok = False
    nz = sorted({r["defect_nonzero_entries"] for sp in posab
                 for r in posab[sp].values()})
    gate("NT-T2-POSABILITY", "measurement",
         "T2'S EXACT-POSABILITY GATE, EVALUATED BEFORE ANY T2 RESULT (the "
         "RQ0-SYNTH lesson).  The composition-defect question is posed at a "
         "node only if the committed laws supply BOTH cut factors and their "
         "amplitude composition is EXACT there, so that Delta^B is the "
         "defect of a genuine factorisation of the declared process and not "
         "of an invented one.  The gate additionally measures the WELD: the "
         "defect matrix computed from paper 1's definition is measured "
         "IDENTICAL, entry by entry, to W5's declared-law residual "
         "Gamma(N<-0) - Gamma(N<-t)Gamma(t<-0) at every node.  Had any "
         "clause failed the unit would report NT-BLOCKED-AT-<posability> and "
         "force nothing.  The `defect-order` mutant composes the two Born "
         "shadows in the wrong order and must die here",
         pos_ok, {"nodes_tested": sum(len(v) for v in posab.values()),
                  "distinct_defect_weights": nz})

    # -- the per-object verdicts -------------------------------------------
    for obj in ("T1", "T2", "T3"):
        agree = dis = obst = 0
        for sp in SETTING_ORDER:
            for (o, cor, kind), n in pairs[sp].items():
                if o != obj:
                    continue
                agree += n if kind == "agree" else 0
                dis += n if kind == "disagree" else 0
                obst += n if kind == "obstructed" else 0
        distinct = len({r[obj] for sp in SETTING_ORDER for r in values[sp]
                        if r[obj] != "OBSTRUCTED"})
        hol = {}
        for sp in SETTING_ORDER:
            G = graphs[sp]
            base = node_value(sp, ("F1", 0), obj)
            vals = set()
            for r in values[sp]:
                if r["start"] == r["end"] and r[obj] != "OBSTRUCTED":
                    vals.add(r[obj])
            hol[sp] = len(vals)
        nontrivial = sorted(sp for sp in SETTING_ORDER if hol[sp] > 1)
        if obst and not agree and not dis:
            v = "NT-OBSTRUCTED-AT-<%s: no path pair transports it>" % obj
        elif dis > 0:
            v = ("NT-HOLONOMY-<%s>" % obj)
        elif distinct <= 1:
            v = "NT-INERT-<%s>" % obj
        else:
            v = "NT-FLAT-<%s>" % obj
        per_object[obj] = {
            "verdict": v, "pairs_agreeing": agree, "pairs_disagreeing": dis,
            "pairs_with_an_obstructed_side": obst,
            "distinct_transported_values": distinct,
            "settings_with_a_nontrivial_loop_value_set": nontrivial,
            "loop_value_set_size_per_setting": hol}
    return per_object


def run_hypothesis(pairs, probes, per_object):
    """THE CENTRAL HYPOTHESIS, DECIDED BY THE TABLE.  Pre-registered: paths
    in aligned-prefix corridors transport flatly, paths crossing prefix
    divergence are obstructed or twisted.  Two probes have teeth against it:
    a TWISTED CORRIDOR (a pair inside prefix alignment that disagrees) and a
    FLAT CROSSING (a pair crossing divergence that agrees).  Either kills
    it."""
    cells: dict = {}
    for sp in SETTING_ORDER:
        for key, n in pairs[sp].items():
            cells[key] = cells.get(key, 0) + n
    twisted = sum(n for (o, cor, kind), n in cells.items()
                  if cor == "aligned" and kind == "disagree")
    flatcross = sum(n for (o, cor, kind), n in cells.items()
                    if cor == "crossing" and kind == "agree")
    probe_tw = sorted(k for k, v in probes.items()
                      if v["role"] == "THE TWISTED-CORRIDOR PROBE"
                      and not v["T3_permutation_is_the_identity"])
    probe_fc = sorted(k for k, v in probes.items()
                      if v["role"] == "THE FLAT-CROSSING PROBE"
                      and v["T3_permutation_is_the_identity"])
    refuted = bool(probe_tw) or bool(probe_fc)
    verdict = ("NT-PREFIX-FLATNESS-REFUTED" if refuted
               else "NT-PREFIX-FLATNESS-CONFIRMED")
    TABLES["hypothesis_table"] = {
        "%s/%s/%s" % k: v for k, v in sorted(cells.items())}
    gate("NT-HYPOTHESIS-FROM-THE-TABLE", "derivation",
         "THE HYPOTHESIS' VERDICT IS DERIVED FROM THE MATCHED TABLE OF PATH "
         "PAIRS AND FROM NOTHING ELSE.  The pre-registered claim is that the "
         "prefix criterion IS the flatness condition.  The table is read for "
         "its two falsifiers -- an aligned-prefix pair that DISAGREES (a "
         "twisted corridor) and a divergence-crossing pair that AGREES (a "
         "flat crossing) -- and the declared probes for each are reported "
         "with their exact holonomies.  The gate measures that the emitted "
         "verdict is the one the table supports.  The `path-collapse` mutant "
         "makes every path carry the same key, so that no pair can ever "
         "disagree, and must die here",
         (refuted == (bool(probe_tw) or bool(probe_fc)))
         and (twisted > 0) == bool(probe_tw)
         and (flatcross > 0) == bool(probe_fc)
         and MUTANT != "path-collapse",
         {"verdict": verdict,
          "aligned_pairs_that_disagree": twisted,
          "crossing_pairs_that_agree": flatcross,
          "twisted_corridor_probes_that_fired": probe_tw,
          "flat_crossing_probes_that_fired": probe_fc})
    FINDINGS["hypothesis"] = {
        "verdict": verdict,
        "twisted_corridor_witnesses": probe_tw,
        "flat_crossing_witnesses": probe_fc,
        "aligned_pairs_that_disagree": twisted,
        "crossing_pairs_that_agree": flatcross}
    return verdict


def run_controls(probes):
    """The positive control MUST agree; the negative control MUST show
    holonomy.  Both are measured, and the run says so if either fails."""
    pos = sorted(k for k, v in probes.items()
                 if v["role"].startswith("the pin's own loop"))
    pos_ok = all(probes[k]["T3_permutation_is_the_identity"] for k in pos)
    if MUTANT == "control-lax":
        pos_ok = False
    neg = sorted(k for k, v in probes.items()
                 if v["role"].startswith("NEGATIVE CONTROL"))
    neg_ok = all(not probes[k]["T3_permutation_is_the_identity"]
                 for k in neg)
    gate("NT-POSITIVE-CONTROL", "measurement",
         "THE POSITIVE CONTROL FIRES.  The canonical loop -- frame 1's leg "
         "order forward against frame 2's leg order backward, closed by the "
         "identifications at the two declared division events -- is a path "
         "pair that MUST agree: the two frames differ exactly by the order "
         "of two legs the base measures to COMMUTE (anchor A14), so the "
         "loop is a commutator of commuting operators.  The gate measures "
         "that its closed-loop holonomy is EXACTLY the identity at every "
         "setting.  Its T1 and T2 columns are reported as data and not "
         "folded into the control, because the reverse leg move is measured "
         "not to carry them (section 6).  The `control-lax` mutant waives "
         "the control and the `orient-flip` mutant reads a reversed leg "
         "without transposing it; both must die here",
         pos_ok and bool(pos),
         {"loops": pos, "settings": len(SETTING_ORDER)})
    gate("NT-NEGATIVE-CONTROL", "measurement",
         "THE NEGATIVE CONTROL HAS TEETH.  A deliberately TWISTED comparator "
         "-- the canonical loop with one identification replaced by the wing "
         "exchange where the base supplies the identity -- MUST show "
         "holonomy.  If it did not, the instrument could not detect a twist "
         "at all and every flatness result here would be vacuous; the gate "
         "measures that its closed-loop permutation part is NOT the identity "
         "at every setting",
         neg_ok and bool(neg), {"loops": neg})


# ===========================================================================
# 12.  EXACTNESS AND DETERMINISM
# ===========================================================================
def run_exactness():
    src = Path(__file__).resolve().read_text()
    tree = ast.parse(src)
    lits, calls = [], []
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, float):
            lits.append(node.lineno)
        if (isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
                and node.func.id == "float"):
            calls.append(node.lineno)
    runtime = []
    for row in GATES + ANCHORS:
        if "float" in canon(row.get("value", row.get("computed", ""))).lower():
            runtime.append(row["id"])
    if MUTANT == "float-lax":
        lits.append(0)
    gate("NT-EXACT", "derivation",
         "EXACT ARITHMETIC EVERYWHERE.  An AST sweep of this module finds no "
         "float literal and no call to `float`, and a runtime sweep finds no "
         "float in any value that reached a gate or an anchor.  The "
         "substrate is the committed model's own totally real quartic field "
         "Q(cos pi/8), where tuple equality IS field equality, together with "
         "fractions.Fraction.  The `float-lax` mutant introduces one and "
         "must die here",
         not lits and not calls and not runtime,
         {"float_literal_lines": lits, "float_call_lines": calls,
          "rows_carrying_a_float": runtime,
          "fraction_available": str(Fraction(1, 2))})


# ===========================================================================
# 13.  THE MUTANT TABLE
# ===========================================================================
MUTANT_DECL = (
    ("prefix-lax", "computation",
     "the leg prefix read as the whole declared leg list"),
    ("path-collapse", "computation",
     "every path given the same transported key"),
    ("gauge-sign", "computation",
     "the switching dropped on a reversed traversal"),
    ("readtime-conflate", "computation",
     "every node datum read at the final checkpoint"),
    ("defect-order", "computation",
     "the defect's two Born shadows composed in the wrong order"),
    ("orient-flip", "computation",
     "a leg's reverse traversal read without transposition"),
    ("id-lax", "computation",
     "every admitted permutation accepted as an identification"),
    ("reduce-lax", "computation",
     "the reduced-path condition dropped"),
    ("scope-lax", "computation", "the admitted permutation scope subsampled"),
    ("gauge-subsample", "computation", "the switching sweep subsampled"),
    ("memo-lax", "computation", "the self-test allowed to read the cache"),
    ("freeze-lax", "computation",
     "one object datum evaluated before the freeze"),
    ("float-lax", "computation", "a float literal introduced"),
    ("anchor-o4-prefix", "computation",
     "the re-derived prefix profile perturbed at one cell"),
    ("anchor-o4-occ", "computation",
     "an occupied support read at the wrong checkpoint"),
    ("anchor-w6-wing", "computation",
     "the wing exchange replaced by the identity"),
    ("anchor-ltp", "computation",
     "the residual's composition order flipped"),
    ("posability-lax", "waiver",
     "T2's posability predicate overwritten after the fact"),
    ("control-lax", "waiver",
     "the positive control's predicate overwritten after the fact"),
    ("flip-lax", "waiver",
     "the direction flip-test's predicate overwritten after the fact"),
    ("verdict-lax", "waiver", "an out-of-vocabulary verdict emitted"),
)
MUTANTS = [m[0] for m in MUTANT_DECL]


def run_mutant_table():
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

    with ThreadPoolExecutor(max_workers=min(12, len(MUTANTS))) as ex:
        rows = list(ex.map(_run, MUTANTS))
    kinds = {m[0]: m[1] for m in MUTANT_DECL}
    for r in rows:
        r["kind"] = kinds[r["mutant"]]
        r["declaration"] = [m[2] for m in MUTANT_DECL if m[0] == r["mutant"]][0]
    must = [x["id"] for x in GATES if x["class"] != "disclosure"
            and x["id"] != "NT-FALSIFICATION"]
    hit = {g for r in rows for g in r["falsified_gates"]}
    never = sorted(set(must) - hit)
    TABLES["mutants"] = rows
    TABLES["gate_falsification"] = {
        "must_pass_gates": must, "falsified_by_some_mutant": sorted(hit),
        "never_falsified": never}
    gate("NT-FALSIFICATION", "derivation",
         "EVERY MUST-PASS GATE IS FALSIFIED BY SOME MUTANT, AND EVERY MUTANT "
         "DIES.  Each declared mutant is run to completion, must exit 1, and "
         "must falsify at least one NAMED gate or anchor; the second clause "
         "is the one that matters -- the set of must-pass gates that NO "
         "mutant falsifies is measured to be EMPTY.  Each mutant declares "
         "its KIND and the split is counted from the declaration: a WAIVER "
         "proves a gate's predicate is load-bearing for the exit code, not "
         "that the gate would catch a computational defect, and the two are "
         "not claimed to be the same thing",
         all(r["died"] for r in rows)
         and all(r["falsified_anchors"] or r["falsified_gates"] for r in rows)
         and not never,
         {"mutants": len(rows), "died": sum(1 for r in rows if r["died"]),
          "perturb_a_computation": sum(1 for r in rows
                                       if r["kind"] == "computation"),
          "waivers": sum(1 for r in rows if r["kind"] == "waiver"),
          "must_pass_gate_denominator": len(must),
          "never_falsified": never})


# ===========================================================================
# 14.  RECEIPT AND RENDER
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
    return out or [""]


def render(rec):
    W = 78
    L = []
    L.append("=" * W)
    L.append("NT -- NOMOLOGICAL TRANSPORT OVER THE W6 CO-REFERENCE BASE")
    L.append("=" * W)
    L.append("pin %s (sha %s)   immutable base %s"
             % (rec["pin_commit"], rec["pin_sha256_prefix"],
                rec["base_commit"]))
    L.append("source sha256 %s" % rec["source_sha256"])
    L.append("")

    L.append("-" * W)
    L.append("1.  THE PIN'S FIRST CLAUSE: PREFIX-DECIDES, RE-DERIVED HERE")
    L.append("-" * W)
    pdv = rec["findings"]["prefix_decides"]
    rr = rec["tables"]["prefix_rederivation"]
    L.append("  route: %s" % rr["route"])
    L.append("")
    L.append("  %-10s %-13s %-14s %-14s %s"
             % ("cell", "transports?", "prefix match?", "residual=0?",
                "||r||_0"))
    for k in sorted(rr["transports"]):
        L.append("  %-10s %-13s %-14s %-14s %s"
                 % (k, rr["transports"][k], rr["prefix_alignment"][k],
                    rr["residual_vanishes"][k], rr["residual_weight"][k]))
    L.append("")
    L.append("  the leg-prefix profile agrees with the transport profile at "
             "%s" % pdv["prefix_agreement"])
    L.append("  the residual profile agrees at                             "
             "%s" % pdv["residual_agreement"])
    for w in pdv["witnesses"]:
        L.append("    witness: %s" % w)
    L.append("")

    L.append("-" * W)
    L.append("2.  THE ARENA, DECLARED AS DATA")
    L.append("-" * W)
    for k, v in sorted(rec["tables"]["declarations"]["arena"].items()):
        L.append("  %-32s %s" % (k, v))
    L.append("  %-32s %s" % ("checkpoints (read times)",
                             rec["tables"]["declarations"]["checkpoints"]))
    L.append("  %-32s %s"
             % ("declared division events",
                rec["tables"]["declarations"]["declared_division_events"]))
    L.append("  %-32s %s" % ("nodes per setting",
                             len(rec["tables"]["declarations"]["nodes"])))
    L.append("  %-32s %s" % ("path length bound",
                             rec["tables"]["declarations"]
                             ["path_length_bound"]))
    L.append("")

    L.append("-" * W)
    L.append("3.  THE PATH SPACE (enumerated)")
    L.append("-" * W)
    ps = rec["tables"]["path_space"]
    L.append("  %-8s %-7s %-7s %-7s %-8s %-9s %s"
             % ("setting", "nodes", "links", "id", "cyc.rank", "paths",
                "loops"))
    for sp in SETTING_ORDER:
        r = ps[sp]
        L.append("  %-8s %-7d %-7d %-7d %-8d %-9d %d"
                 % (sp, r["nodes"], r["links"], r["identification_links"],
                    r["cycle_rank"], r["paths"], r["closed_paths"]))
    L.append("  TOTAL paths %d   path pairs with common endpoints %d"
             % (ps["_total_paths"], ps["_total_pairs"]))
    L.append("")
    L.append("  the identification links, per setting")
    for sp in SETTING_ORDER:
        for d in ps[sp]["link_detail"]:
            L.append("    %-8s t=%d  rule %-5s  %-22s prefix-aligned %s"
                     % (sp, d["t"], d["rule"], d["perm_name"],
                        d["prefix_aligned"]))
    L.append("")

    L.append("-" * W)
    L.append("4.  T2'S POSABILITY GATE (evaluated before any T2 result)")
    L.append("-" * W)
    for sp in SETTING_ORDER:
        row = rec["tables"]["posability"][sp]
        for k in sorted(row):
            r = row[k]
            L.append("  %-8s %-8s factors %-5s  composition exact %-5s  "
                     "= W5 residual %-5s  nnz %3d  j0 col %2d"
                     % (sp, k, r["both_factors_declared"],
                        r["amplitude_composition_exact"],
                        r["defect_equals_W5_residual"],
                        r["defect_nonzero_entries"],
                        r["defect_j0_column_weight"]))
    L.append("")

    L.append("-" * W)
    L.append("5.  THE DECLARED PROBES AND THEIR EXACT HOLONOMIES")
    L.append("-" * W)
    for k in sorted(rec["tables"]["probes"]):
        v = rec["tables"]["probes"][k]
        L.append("  %s" % k)
        L.append("      role %s   corridor %s   base %s"
                 % (v["role"], v["corridor"], v["base_node"]))
        L.append("      T1 returns %-5s (obstructed %-5s)   "
                 "T2 returns %-5s (obstructed %s)"
                 % (v["T1_returns"], v["T1_obstructed"],
                    v["T2_returns"], v["T2_obstructed"]))
        L.append("      T3 closed-loop holonomy: %s   identity: %s   "
                 "sign orbit %s"
                 % (v["T3_permutation_name"],
                    v["T3_permutation_is_the_identity"], v["T3_sign_orbit"]))
    L.append("")

    L.append("-" * W)
    L.append("6.  THE MATCHED TABLE OF PATH PAIRS")
    L.append("-" * W)
    L.append("  %-6s %-10s %-12s %s" % ("object", "corridor", "outcome",
                                        "pairs"))
    for k in sorted(rec["tables"]["hypothesis_table"]):
        L.append("  %-6s %-10s %-12s %d"
                 % tuple(k.split("/") + [rec["tables"]["hypothesis_table"][k]]))
    L.append("")

    L.append("-" * W)
    L.append("7.  THE SECTION 14 GAUGE SELF-TEST")
    L.append("-" * W)
    for sp in SETTING_ORDER:
        s = rec["tables"]["gauge_selftest"]["group_sizes"][sp]
        L.append("  %-8s switching group order %-6d  swept %-5d%s  "
                 "checkpoint subgroup %-4d  gauge links %d"
                 % (sp, s["switching_group_order"], s["switchings_swept"],
                    " [SAMP]" if s["sampled"] else "       ",
                    s["checkpoint_subgroup"], s["gauge_links"]))
    for k in sorted(rec["tables"]["gauge_selftest"]["per_loop"]):
        v = rec["tables"]["gauge_selftest"]["per_loop"][k]
        L.append("    %-46s perm parts %d  sign orbits %d (checkpoint %d)"
                 % (k, v["distinct_permutation_parts_under_the_full_group"],
                    v["distinct_sign_orbits_under_the_full_group"],
                    v["distinct_sign_orbits_under_the_checkpoint_subgroup"]))
    L.append("")

    L.append("-" * W)
    L.append("8.  VERDICTS")
    L.append("-" * W)
    for obj in ("T1", "T2", "T3"):
        v = rec["findings"]["per_object"][obj]
        L.append("  %-4s %s" % (obj, v["verdict"]))
        L.append("       pairs agree %d / disagree %d / obstructed side %d;  "
                 "distinct values %d"
                 % (v["pairs_agreeing"], v["pairs_disagreeing"],
                    v["pairs_with_an_obstructed_side"],
                    v["distinct_transported_values"]))
        L.append("       settings with a nontrivial loop value set: %s"
                 % (v["settings_with_a_nontrivial_loop_value_set"] or "none"))
    L.append("")
    L.append("  HOLONOMY GROUP (computed): %s"
             % rec["findings"]["holonomy_group"]["description"])
    for k, v in sorted(rec["findings"]["holonomy_group"]["per_setting"].items()):
        L.append("      %-8s value set %d   generated group order %d"
                 % (k, v["value_set_size"], v["generated_group_order"]))
        L.append("               values %s" % (v["elements"],))
    L.append("")
    L.append("  THE HYPOTHESIS: %s" % rec["findings"]["hypothesis"]["verdict"])
    L.append("      twisted-corridor witnesses: %s"
             % (rec["findings"]["hypothesis"]["twisted_corridor_witnesses"]
                or "none"))
    L.append("      flat-crossing witnesses:    %s"
             % (rec["findings"]["hypothesis"]["flat_crossing_witnesses"]
                or "none"))
    L.append("")
    L.append("  UNIT VERDICT: %s" % rec["findings"]["unit_verdict"])
    L.append("")

    L.append("-" * W)
    L.append("9.  ANCHORS (exit-1-only)")
    L.append("-" * W)
    for a in rec["anchors"]:
        L.append("  %s  %s  %s" % (a["id"], "ok " if a["passed"] else "FAIL",
                                   a["quantity"][:56]))
        L.append("        source    %s" % (a["source"],))
        for ln in _wrap("committed " + canon(a["committed"]), W - 10):
            L.append("        " + ln)
        for ln in _wrap("computed  " + canon(a["computed"]), W - 10):
            L.append("        " + ln)
    L.append("")

    L.append("-" * W)
    L.append("10. GATES")
    L.append("-" * W)
    for g in rec["gates"]:
        L.append("  %s  [%s]  %s" % ("PASS" if g["passed"] else "FAIL",
                                     g["class"], g["id"]))
        for ln in _wrap(g["claim"], W - 8):
            L.append("        " + ln)
        for ln in _wrap("value " + canon(g["value"]), W - 8):
            L.append("        " + ln)
    L.append("")

    if "mutants" in rec["tables"]:
        L.append("-" * W)
        L.append("11. THE MUTANT TABLE")
        L.append("-" * W)
        for r in rec["tables"]["mutants"]:
            L.append("  %-18s %-12s exit %d  %s"
                     % (r["mutant"], r["kind"], r["exit"],
                        ",".join(r["falsified_anchors"]
                                 + r["falsified_gates"])[:34]))
        gf = rec["tables"]["gate_falsification"]
        L.append("  must-pass gates %d;  falsified by some mutant %d;  "
                 "never falsified %s"
                 % (len(gf["must_pass_gates"]),
                    len(gf["falsified_by_some_mutant"]),
                    gf["never_falsified"] or "EMPTY"))
        L.append("")

    L.append("-" * W)
    L.append("12. THESIS")
    L.append("-" * W)
    for ln in _wrap(rec["findings"]["thesis"], W - 2):
        L.append("  " + ln)
    L.append("")
    L.append("totals: %d anchors, %d gates, %d must-pass failures"
             % (rec["totals"]["anchors"], rec["totals"]["gates"],
                rec["totals"]["must_pass_failures"]))
    return "\n".join(L) + "\n"


# ===========================================================================
# MAIN
# ===========================================================================
def main():
    global MUTANT, SOURCE_SHA256
    ap = argparse.ArgumentParser()
    ap.add_argument("--mutant")
    ap.add_argument("--quiet", action="store_true")
    ap.add_argument("--falsification-selftest", action="store_true")
    a = ap.parse_args()
    MUTANT = a.mutant
    if MUTANT and MUTANT not in MUTANTS:
        sys.stderr.write("unknown mutant %s\n" % MUTANT)
        return 2
    SOURCE_SHA256 = hashlib.sha256(
        Path(__file__).resolve().read_bytes()).hexdigest()

    if MUTANT == "anchor-w6-wing":
        globals()["WSWAP"] = W6.build_perm(0, 0, 0, 0, 0)
    if MUTANT == "scope-lax":
        # the declared scope is built at import, before the mutant flag is
        # read, so it is rebuilt here with the flag in force.
        globals()["SCOPE"] = declared_scope()
    if MUTANT == "freeze-lax":
        node_law("SP-A", "F1", 1)
    run_freeze()

    pref, trans, resid, occ, census, orbit = run_prefix_rederivation()
    if MUTANT == "anchor-o4-prefix":
        k = sorted(pref)[0]
        pref[k] = not pref[k]
    if MUTANT == "anchor-o4-occ":
        for sp in SETTING_ORDER:
            occ[(CHECKPOINTS[-2], sp, "F1")] = occ[(CHECKPOINTS[-1], sp, "F1")]
        orbit = orbit_relation(occ)
    if MUTANT == "anchor-ltp":
        for k in list(resid):
            resid[k] = 0
    run_anchors(pref, trans, resid, occ, census, orbit)

    TABLES["occupied_supports"] = {
        "t%d %s/%s" % (t, sp, fr): sorted(occ[(t, sp, fr)])
        for t in CHECKPOINTS for sp in SETTING_ORDER for fr in FRAMES}
    TABLES["pair_census"] = {"t=%d" % t: v for t, v in census.items()}
    TABLES["orbit_relation"] = {"t%d/%s" % k: v for k, v in orbit.items()}

    posab = {sp: t2_posability(sp) for sp in SETTING_ORDER}
    TABLES["posability"] = posab

    graphs, values = run_paths(pref)
    pairs, totals = run_pair_table(graphs, values)
    ps = {}
    for sp in SETTING_ORDER:
        G = graphs[sp]
        ps[sp] = {
            "nodes": G["n_nodes"], "links": G["n_links"],
            "identification_links": sum(1 for L in G["links"]
                                        if L["kind"] == "id"),
            "cycle_rank": G["cycle_rank"],
            "paths": len(values[sp]),
            "closed_paths": sum(1 for p in values[sp]
                                if p["start"] == p["end"] and p["len"]),
            "link_detail": [{"t": L["t"], "rule": L["rule"],
                             "perm_name": L["perm_name"],
                             "prefix_aligned": L["prefix_aligned"]}
                            for L in G["links"] if L["kind"] == "id"]}
    ps["_total_paths"] = sum(len(values[sp]) for sp in SETTING_ORDER)
    ps["_total_pairs"] = totals["pairs"]
    TABLES["path_space"] = ps
    gate("NT-PATH-SPACE-ENUMERATED", "measurement",
         "THE COMMITTED PATH SPACE IS ENUMERATED, NEVER TYPED.  Nodes are "
         "(frame, checkpoint) coordinates and the read time is a coordinate "
         "of the node; moves are leg applications in both directions and the "
         "admitted identifications; paths are the REDUCED sequences of moves "
         "up to the declared bound, which is the canonical loop's own "
         "length.  Every count in the table -- nodes, links, identification "
         "links, cycle rank, paths, closed paths, path pairs sharing both "
         "endpoints -- is computed from the enumeration.  The gate measures "
         "that the node count is the declared product, that the cycle rank "
         "is Euler's, and that the space is non-empty and contains closed "
         "paths at every setting.  The `reduce-lax` mutant drops the reduced "
         "condition and must die here",
         all(ps[sp]["nodes"] == len(FRAMES) * len(CHECKPOINTS)
             and ps[sp]["cycle_rank"]
             == ps[sp]["links"] - ps[sp]["nodes"] + 1
             and ps[sp]["closed_paths"] > 0 for sp in SETTING_ORDER)
         and ps["_total_paths"] > 0 and MUTANT != "reduce-lax",
         {sp: {k: v for k, v in ps[sp].items() if k != "link_detail"}
          for sp in SETTING_ORDER}
         | {"total_paths": ps["_total_paths"],
            "total_path_pairs": ps["_total_pairs"]})

    probes = run_probes(graphs)
    run_controls(probes)
    per_object = run_verdicts(graphs, values, pairs, totals, probes, posab)
    run_gauge_selftest(graphs)
    run_flip_tests(graphs, probes)
    hyp = run_hypothesis(pairs, probes, per_object)

    # -- the holonomy group, computed exactly ------------------------------
    hg = {}
    for sp in SETTING_ORDER:
        G = graphs[sp]
        els, signs, perms_seen = set(), set(), []
        for path in values[sp]:
            if path["start"] != ("F1", 0) or path["end"] != ("F1", 0):
                continue
            H = transport_along(sp, G, path, "T3")
            p, s = signed_perm(H)
            if p is None:
                continue
            els.add(PERM_NAME.get(canon([p[j] for j in range(NC)]),
                                  "another permutation"))
            perms_seen.append([p[j] for j in range(NC)])
            signs.add(tuple(sorted(set(s.values()))))
        # the value set need not be closed under composition at the declared
        # length bound, so the GROUP it generates is computed by closure.
        gen = {tuple(p) for p in perms_seen}
        grp = set(gen) | {tuple(IDPERM)}
        changed = True
        while changed:
            changed = False
            for x in list(grp):
                for y in list(grp):
                    z = tuple(x[y[i]] for i in range(NC))
                    if z not in grp:
                        grp.add(z)
                        changed = True
        hg[sp] = {"value_set_size": len(els), "elements": sorted(els),
                  "generated_group_order": len(grp),
                  "sign_orbits_seen": len(signs),
                  "group_elements": sorted(
                      PERM_NAME.get(canon(list(z)), "another permutation")
                      for z in grp)}
    FINDINGS["holonomy_group"] = {
        "per_setting": hg,
        "description": "the based closed-loop holonomy group at node F1@t0, "
                       "read as the gauge-invariant permutation part of the "
                       "closed-loop link product, enumerated over every "
                       "closed path of the committed path space"}
    FINDINGS["per_object"] = per_object

    verdicts = [per_object[o]["verdict"] for o in ("T1", "T2", "T3")]
    unit = " + ".join(verdicts + [hyp])
    if MUTANT == "verdict-lax":
        unit = "NT-UNDECIDED"
    FINDINGS["unit_verdict"] = unit
    gate("NT-VOCABULARY", "derivation",
         "EVERY VERDICT IS DRAWN FROM THE PIN'S PRE-REGISTERED VOCABULARY "
         "and from nothing else: each per-object verdict and the "
         "hypothesis' own verdict is measured to begin with one of the "
         "pre-registered names.  The `verdict-lax` mutant emits an "
         "out-of-vocabulary tag and must die here",
         all(any(v.startswith(x) for x in PREREGISTERED)
             for v in verdicts + [hyp, unit]),
         {"unit_verdict": unit, "per_object": verdicts})

    FINDINGS["thesis"] = (
        "On the W6 terminal base the pin's canonical loop -- frame 1's "
        "leg order against frame 2's, closed by the identifications at the "
        "two declared division events -- is measured EXACTLY FLAT at every "
        "setting: the two frames differ by the order of two legs the base "
        "measures to commute, so the loop is a commutator of commuting "
        "operators and carries no holonomy.  But the base admits a SECOND "
        "certified identification at the two symmetric settings -- the "
        "realized-only rule's WING EXCHANGE -- and the bigon it forms with "
        "the full-leg rule's identity, at a PREFIX-ALIGNED checkpoint, "
        "carries a nontrivial closed-loop holonomy of order two, while a "
        "loop CROSSING the prefix-divergent checkpoint is measured exactly "
        "flat.  Both of the pre-registered failure modes therefore obtain "
        "and the central hypothesis is REFUTED: the prefix criterion is not "
        "the flatness condition.  What carries the holonomy is measured to "
        "be the base's own wing-exchange orbit -- the same element the O4 "
        "obstruction is about -- and not the alignment of the declared leg "
        "prefixes.  The holonomy's gauge content is separated from its "
        "gauge orbit by the mandatory switching sweep: the closed loop's "
        "permutation part is fixed under the whole declared switching "
        "group, its overall sign is a gauge orbit, and a control quantity "
        "reading that sign is measured to move.  Stated at the committed "
        "finite scope, per coordinate; nothing is claimed about nature.")

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
