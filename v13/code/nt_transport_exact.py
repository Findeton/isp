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
      by the admitted permutation.  The read time is a coordinate of T1's
      datum.
  T2  the composition defect Delta^B of paper 1, at the node's own cut,
      BEHIND AN EXACT-POSABILITY GATE: the question is posed only if the
      committed laws supply both cut factors and their amplitude
      composition is exact.  Identifications act by conjugation, which is
      paper 1's OUTER-SLOT equivariance law (iv) read at an INVOLUTIVE
      permutation (measured: every admitted map squares to the identity);
      legs carry the matrix unchanged, so leg flatness MEASURES the
      defect's stability under moving the cut.  The read time is NOT a
      coordinate of T2's datum, and T2 data read at different checkpoints
      are measured to compare equal; the matched table pairs only paths
      sharing both endpoints, so every T2 comparison is nonetheless at
      matched coordinates.
  T3  the amplitude/phase layer in GAUGE-INVARIANT CLOSED-LOOP form: the
      ordered product of link variables around a closed loop.  The declared
      switching group is one sign per link.  The sweep MEASURES that the
      switching acts on a closed loop by the global scalar (prod eps); the
      invariance of the loop's PERMUTATION PART is then FORCED by that
      measured action and is reported as a disclosure, not as a must-pass
      measurement.  The sweep's teeth are the scalar-action clause, the
      checkpoint-subgroup telescoping clause, and the signed-permutation
      clause.  The relative-sign class, not the raw sign set, is the
      invariant sign content.

WHAT THE HOLONOMY IS.  The based holonomy group at F1@t0 is computed from
PERMUTATION CONTENT (the matrix), never from name labels; at the two
symmetric settings it is the KLEIN FOUR-GROUP {1, W, X, WX} with
W = X . WX, X the qubit-only wing swap and WX the pointer-only wing swap,
and the value set is measured already closed at the declared length bound.
X and WX are measured to lie OUTSIDE the declared 72-element permutation
scope and its declared 96-element extension: the connection is NOT
PRINCIPAL for the base's admitted isomorphisms.

WHAT GENERATES IT.  Two sources, both measured.  (i) Two admitted
identification rules differing by the wing exchange at one coordinate --
SUFFICIENT for holonomy, never necessary.  (ii) The wing exchange fails to
intertwine the PREPARATION leg at every setting, so the single-rule
sub-connection, whose every coordinate has multiplicity one, is already
non-flat.  T1 is excluded from both: its path-dependence is Born-level
non-inversion (B(L)^T B(L) != I), present at every setting.

THE CENTRAL HYPOTHESIS, PRE-REGISTERED: the prefix criterion is the
flatness condition.  It is TESTED, with both failure modes probed with
teeth: a flat crossing and a twisted corridor.  The matched table of path
pairs decides.

Exact arithmetic throughout: the totally real quartic field Q(cos pi/8) of
the committed composite model (tuple equality IS field equality) and
fractions.Fraction.  No float enters any path.  Anchors exit 1 on mismatch.
`--mutant NAME` breaks exactly one anchor, gate or derivation step and must
exit 1 naming what it falsified.  NO GATE PREDICATE REFERENCES MUTANT
IDENTITY (RUNBOOK section 14 addendum): a mutation is injected where the
computation happens and every declared falsifier dies by a gate's own
predicate evaluated blind.  An AST sweep of this module measures that no
`MUTANT !=` comparison exists anywhere in it.  No wall-clock value enters
the receipt or the rendered output, so two delivery-mode runs are
byte-identical.

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
import io
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
                             NC, idx, unidx)

W5_SOURCE = REPO / "v12" / "code" / "w5_ltp_lemma_exact.py"


def _w5_committed():
    """W5'S COMMITTED IMPLEMENTATION, LOADED FROM ITS OWN FILE.

    The declared-law residual Gamma(N<-0) - Gamma(N<-t)Gamma(t<-0) that T2's
    weld compares against is NOT re-typed here: it is built with W5's own
    committed Born shadow (`gam`), its own matrix product (`mmul`) and its
    own subtraction (`ksub`), taken from the terminal v12 script.  W5's file
    is a script that ends in `sys.exit(0)`, so it is executed in its own
    namespace with its stdout captured and that exit caught; nothing it
    writes reaches this run and it writes no file.  Its own committed
    numbers (the residual weight per cell, `VN`) anchor this unit's defect
    exit-1."""
    ns = {"__name__": "w5_ltp_lemma_committed", "__file__": str(W5_SOURCE)}
    buf, old = io.StringIO(), sys.stdout
    sys.stdout = buf
    try:
        exec(compile(W5_SOURCE.read_text(), str(W5_SOURCE), "exec"), ns)
    except SystemExit:
        pass
    finally:
        sys.stdout = old
    return ns


W5 = _w5_committed()

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
    self-test read the cache and must die there.  The mutation is injected
    HERE, in the computation; no gate predicate names it."""
    read_cache_in_fresh_mode = (MUTANT == "memo-lax")
    if _FRESH and not read_cache_in_fresh_mode:
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
    evaluate_before_the_freeze = (MUTANT == "freeze-lax")
    if not _FROZEN and not evaluate_before_the_freeze:
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


def _cfg_perm(f):
    """A permutation of the 36 configurations, written in the committed
    model's own coordinates (qA, qB, pA, pB)."""
    return [idx(*f(*unidx(j))) for j in range(NC)]


# THE TWO FACTORS OF THE WING EXCHANGE, built from the model's coordinates.
# The wing exchange swaps the qubit pair AND the pointer pair; these are its
# two halves, and the factorisation W = XQ . XP is MEASURED below, never
# assumed.  Neither factor is in the base's declared permutation scope --
# that scope's `swap` flag always moves both pairs together -- and that
# measured fact is the escape gate.
XQSWAP = _cfg_perm(lambda qa, qb, pa, pb: (qb, qa, pa, pb))   # qubit-only
XPSWAP = _cfg_perm(lambda qa, qb, pa, pb: (qa, qb, pb, pa))   # pointer-only

PERM_NAME = {canon(list(IDPERM)): "the identity",
             canon(list(WSWAP)): "the wing exchange",
             canon(list(XQSWAP)): "the qubit-only wing swap",
             canon(list(XPSWAP)): "the pointer-only wing swap"}


_NAMES_OF_THE_TWO_DECLARED_MAPS = {canon(list(IDPERM)): "the identity",
                                   canon(list(WSWAP)): "the wing exchange"}


def perm_tuple(p):
    """A holonomy's VALUE: the permutation itself, as the tuple of images.
    This is MATRIX CONTENT.  The `label-collapse` mutant returns a NAME
    drawn from the two declared identification maps instead, so that every
    other permutation collapses onto one string and the value set is
    counted as a set of labels -- a count of the wrong object.  The
    mutation is injected here, in the computation; no gate predicate names
    it, and the corrected count gate must catch it blind."""
    t = tuple(p[j] for j in range(NC))
    count_labels_instead_of_permutations = (MUTANT == "label-collapse")
    if count_labels_instead_of_permutations:
        return _NAMES_OF_THE_TWO_DECLARED_MAPS.get(canon(list(t)),
                                                   "another permutation")
    return t


def perm_compose(x, y):
    """(x . y)(i) = x(y(i)), on tuples of images."""
    return tuple(x[y[i]] for i in range(NC))


def fixed_points(p):
    return sum(1 for i in range(NC) if p[i] == i)


def perm_order(p):
    q, n = tuple(p), 1
    ident = tuple(range(NC))
    while q != ident:
        q = perm_compose(tuple(p), q)
        n += 1
        if n > NC:
            return None
    return n


# ---- exact sparse linear algebra, through the base's own primitives -------
def mm(A, B):
    return W6.sp_mul(K, A, B)


_KMUL: dict = {}
_KADD: dict = {}


def mm_memo(A, B):
    """The same sparse product as `mm`, with the FIELD's own products and
    sums memoised.  The committed model's matrices carry very few distinct
    field values -- the caches hold a few hundred entries for the whole run
    -- so the sweep spends its time on structure rather than on recomputing
    the same exact products.  Nothing is approximated and nothing is
    cached at the level of a transported value: the memo is of + and x in
    Q(cos pi/8), where tuple equality IS field equality.  The two
    implementations are measured against each other on EVERY swept
    instance: the section 14 gate compares each switched holonomy, built
    here, against the unswitched holonomy built by the base's own
    `W6.sp_mul`, so an all-positive switching is an exact equality test of
    this routine against the committed primitive."""
    bycol: dict = {}
    for (i, k), v in A.items():
        bycol.setdefault(k, []).append((i, v))
    out: dict = {}
    zero = K.zero
    for (k, j), v in B.items():
        col = bycol.get(k)
        if not col:
            continue
        for (i, u) in col:
            mk = (u, v)
            t = _KMUL.get(mk)
            if t is None:
                t = K.mul(u, v)
                _KMUL[mk] = t
            if t == zero:
                continue
            key = (i, j)
            s = out.get(key)
            if s is None:
                out[key] = t
            else:
                ak = (s, t)
                r = _KADD.get(ak)
                if r is None:
                    r = K.add(s, t)
                    _KADD[ak] = r
                if r == zero:
                    del out[key]
                else:
                    out[key] = r
    return out


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
    """Theta(t<-0): the ordered product of the first t declared legs.  Held
    in the FIXTURE cache with the legs it is built from (D6): it is a
    function of (setting, frame, checkpoint) and of nothing else, and the
    section 14 self-test does not read it -- that test's own cache is
    `_memo`, which it bypasses."""
    key = ("theta", sp, fr, t)
    if key not in _FIXTURE:
        acc = W6.sp_id(K, NC)
        for L in legs_of(sp, fr)[:t]:
            acc = mm(L, acc)
        _FIXTURE[key] = acc
    return _FIXTURE[key]


def theta_tail(sp, fr, t):
    """Theta(NLEGS<-t): the ordered product of the legs after t."""
    key = ("theta_tail", sp, fr, t)
    if key not in _FIXTURE:
        acc = W6.sp_id(K, NC)
        for L in legs_of(sp, fr)[t:]:
            acc = mm(L, acc)
        _FIXTURE[key] = acc
    return _FIXTURE[key]


def realized_legs(sp, fr):
    """Each declared leg restricted to the configurations the process
    actually occupies before and after it -- W6's realized process, and the
    leg list the REALIZED-only rule matches."""
    key = ("realized", sp, fr)
    if key in _FIXTURE:
        return _FIXTURE[key]
    T = M.propagators(sp, fr)[:NLEGS]
    supp = [{J0}] + [{i for (i, j), v in T[t].items()
                      if j == J0 and not K.is_zero(v)} for t in range(NLEGS)]
    _FIXTURE[key] = [W6.sp_restrict(legs_of(sp, fr)[t], supp[t + 1], supp[t])
                     for t in range(NLEGS)]
    return _FIXTURE[key]


def node_law(sp, fr, t):
    """THE LAW'S RESTRICTION TO THE CONTEXT (fr, t): the occupied support and
    the exact probability of every configuration at the DECLARED READ TIME t.
    The read time is carried in the datum itself."""
    _bump()
    key = ("node_law", sp, fr, t)
    if key in _FIXTURE:
        return _FIXTURE[key]
    T = theta(sp, fr, t)
    out = {}
    for (i, j), v in T.items():
        if j == J0:
            p = K.mul(v, v)
            if not K.is_zero(p):
                out[i] = K.add(out.get(i, K.zero), p)
    # THE O4 DEFECT RESTORED by `readtime-conflate`: a datum read at the
    # final time whatever the node declares.  Every cell of every matched
    # table then compares objects read at different coordinates.
    read_every_datum_at_the_final_checkpoint = (MUTANT == "readtime-conflate")
    _FIXTURE[key] = (node_law_final(sp, fr)
                     if read_every_datum_at_the_final_checkpoint
                     else {"read_time": t, "law": out})
    return _FIXTURE[key]


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
    pc4 = o4["tables"]["pair_census"]["t=%d" % tmid]
    anchor("A12", "v13/code/o4_discriminator_receipt.json pair_census",
           "cross-frame disjoint / cross-frame pairs / same-frame sharing / "
           "same-frame pairs at the second intermediate checkpoint",
           (pc4["cross_frame_disjoint"], pc4["cross_frame_pairs"],
            pc4["same_frame_sharing"], pc4["same_frame_pairs"]),
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
    anchor("A18",
           "v13/code/o4_discriminator_receipt.json declarations "
           "final_declared_division_event",
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
    anchor("A22", "v13/code/o4_discriminator_receipt.json anchors "
                  "(A SOURCE HEALTH CHECK, not a reused NT quantity: both "
                  "sides are read from the same committed file)",
           "the O4 terminal receipt's own anchor pass count",
           len(o4["anchors"]),
           sum(1 for x in o4["anchors"] if x["passed"]))

    # -- the cross-corpus anchors: W5's own committed numbers --------------
    anchor("A23", "v12/code/w5_ltp_lemma_exact.py VN (W5's own committed "
                  "declared-law residual weight, computed by W5's own code)",
           "W5's residual weight per (setting, frame) at the cut it records, "
           "against this unit's own defect j0-column weight there",
           {"%s/%s" % k: v for k, v in sorted(W5["VN"].items())},
           {"%s/%s" % (sp, fr):
            len([1 for (i, j) in defect_matrix(sp, fr, tmid) if j == J0])
            for sp in SETTING_ORDER for fr in FRAMES})


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


def admits(sp, t, rule, scope="admitted"):
    """THIS UNIT'S OWN ADMISSIBILITY PREDICATE.  Which permutations of the
    admitted scope carry frame F2's context at checkpoint t onto frame F1's?
    Four clauses in order: the j0 filter, the rule's own leg list, the
    occupied-set clause, the exact-law clause.

    THE SCOPE IS THE NARROW ONE, AND IT IS DECLARED.  Every call that feeds
    a link, a profile or a verdict passes the default: the 2 elements of
    the declared 72-element scope that survive the j0 filter.  The declared
    96-element extension (8 admitted) is searched only through the explicit
    `scope="admitted_extension"` argument, in the scope disclosure, and
    that measurement is folded into no verdict."""
    la = (realized_legs(sp, "F1") if rule["legs"] == "realized"
          else legs_of(sp, "F1"))
    lb = (realized_legs(sp, "F2") if rule["legs"] == "realized"
          else legs_of(sp, "F2"))
    kA = ("legkeys", sp, rule["id"], "F1")
    if kA not in _FIXTURE:
        _FIXTURE[kA] = sorted(leg_key(L, rule["level"]) for L in la)
    ka = _FIXTURE[kA]
    da = node_law(sp, "F1", t)["law"]
    db = node_law(sp, "F2", t)["law"]
    out = []
    for p in SCOPE[scope]:
        if p[J0] != J0:
            continue
        kB = ("legkeys", sp, rule["id"], "F2", canon(list(p)))
        if kB not in _FIXTURE:
            _FIXTURE[kB] = sorted(leg_key(W6.sp_conj(L, p), rule["level"])
                                  for L in lb)
        kb = _FIXTURE[kB]
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
    key = ("defect", sp, fr, t)
    if key in _FIXTURE:
        return _FIXTURE[key]
    U1, U2 = theta(sp, fr, t), theta_tail(sp, fr, t)
    compose_the_born_shadows_in_the_wrong_order = (MUTANT == "defect-order")
    if compose_the_born_shadows_in_the_wrong_order:
        _FIXTURE[key] = msub(born(mm(U2, U1)), mm(born(U1), born(U2)))
    else:
        _FIXTURE[key] = msub(born(mm(U2, U1)), mm(born(U2), born(U1)))
    return _FIXTURE[key]


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


_INTERN_VALUE: dict = {}


def intern(key):
    """Values are compared through an interning table, so a path pair's
    agreement is an identity of exact keys and never a tolerance.  The
    table is kept invertible: a transported value's exact structural key can
    be read back from its interned identifier, so a census over the
    enumerated paths reads the SAME values the enumeration carried and does
    not rebuild them by a second route."""
    if key not in _INTERN:
        _INTERN[key] = len(_INTERN)
        _INTERN_VALUE[_INTERN[key]] = key
    return _INTERN[key]


_HOL_CLASS: dict = {}


def holonomy_class_of_interned(t3key):
    """The signed-permutation class of an interned T3 value.  T3's datum IS
    the ordered product of link variables, so the interned key is the exact
    matrix and this is a reading of it, not a recomputation.  A key that was
    never interned carries no matrix to read -- the `path-collapse` mutation
    replaces every path's transported key with one token -- and is reported
    as unreadable so that the gates measure the collapse instead of the run
    dying on it."""
    if t3key not in _INTERN_VALUE:
        return (None, None, "not a readable transported value")
    if t3key not in _HOL_CLASS:
        A = dict(_INTERN_VALUE[t3key])
        p, s = signed_perm(A)
        _HOL_CLASS[t3key] = (
            None if p is None else tuple(p[j] for j in range(NC)),
            None if s is None else relative_sign_class(s),
            "not a signed permutation" if p is None else
            PERM_NAME.get(canon([p[j] for j in range(NC)]),
                          "another permutation"))
    return _HOL_CLASS[t3key]


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
        drop_the_reduced_condition = (MUTANT == "reduce-lax")
        for (li, d, nxt) in G["adj"][node]:
            if (not drop_the_reduced_condition
                    and last is not None and li == last):
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
def w5_residual(sp, fr, t):
    """W5'S DECLARED-LAW RESIDUAL, BUILT BY W5'S OWN COMMITTED CODE.

    Gamma(N<-0) - Gamma(N<-t) Gamma(t<-0), where Gamma is W5's own Born
    shadow `gam`, the product is W5's own `mmul` and the subtraction is
    W5's own `ksub` -- all three imported from the committed v12 script and
    applied to THIS unit's propagators.  Nothing about the residual is
    re-typed here.  (W5's carrier and this unit's are both the 36
    configurations of the committed composite model and its field elements
    are the same 4-tuples; the agreement of the two codebases' arithmetic on
    these matrices is itself measured, below.)"""
    TH, TH2, TH1 = theta(sp, fr, NLEGS), theta_tail(sp, fr, t), theta(sp,
                                                                     fr, t)
    dense = [[TH.get((i, j), K.zero) for j in range(NC)] for i in range(NC)]
    d2 = [[TH2.get((i, j), K.zero) for j in range(NC)] for i in range(NC)]
    d1 = [[TH1.get((i, j), K.zero) for j in range(NC)] for i in range(NC)]
    G30, G2, G1 = W5["gam"](dense), W5["gam"](d2), W5["gam"](d1)
    P = W5["mmul"](G2, G1)
    out = {}
    for i in range(NC):
        for j in range(NC):
            v = W5["ksub"](G30[i][j], P[i][j])
            if not W5["kzero"](v):
                out[(i, j)] = v
    return out


def t2_posability(sp):
    """T2'S EXACT-POSABILITY GATE, evaluated BEFORE any T2 transport result.
    The composition-defect question is posable at a node only if the
    committed laws supply BOTH cut factors and their amplitude composition is
    exact at that cut: Theta(N<-t) Theta(t<-0) = Theta(N<-0) on the nose.  If
    the question cannot be posed the unit reports NT-BLOCKED-AT-<posability>
    and does not force it.

    THE WELD, AND WHAT IT IS.  Clause 3 measures the defect matrix built
    from paper 1's definition to be W5's declared-law residual, entry by
    entry, at every node.  IT FOLLOWS FROM CLAUSE 2: both objects subtract
    the same B(U2)B(U1), and clause 2 gates their minuends B(U2 U1) and
    B(Theta(N<-0)) equal on the nose, so the two differences coincide the
    moment clause 2 holds.  This is the single case paper 1 engraved as the
    exemption to its own scope statement -- Delta^B is not the residual of a
    declared stochastic law UNLESS that law is declared to be B(U2), which
    is exactly what this base declares -- and W5's committed M4 recorded the
    coincidence, with its cause, at the one cut t = 2.  What is added here
    is the extension to all four cuts in both frames, and the comparison is
    made against W5's OWN COMMITTED IMPLEMENTATION rather than a
    re-transcription of its formula."""
    rows = {}
    for fr in FRAMES:
        for t in CHECKPOINTS:
            U1, U2 = theta(sp, fr, t), theta_tail(sp, fr, t)
            comp_exact = (mm(U2, U1) == theta(sp, fr, NLEGS))
            D = defect_matrix(sp, fr, t)
            resid = w5_residual(sp, fr, t)
            # the entailment, measured rather than asserted: with clause 2
            # holding, the two minuends are equal, so clause 3 cannot fail.
            entailed = (born(mm(U2, U1)) == born(theta(sp, fr, NLEGS)))
            rows["%s@t%d" % (fr, t)] = {
                "both_factors_declared": bool(U1) and bool(U2),
                "amplitude_composition_exact": bool(comp_exact),
                "defect_equals_W5_residual": bool(D == resid),
                "clause_3_is_entailed_by_clause_2": bool(entailed),
                "defect_nonzero_entries": len(D),
                "defect_j0_column_weight": len([1 for (i, j) in D
                                                if j == J0])}
    return rows


def admitted_maps_are_involutions():
    """PAPER 1'S EQUIVARIANCE (iv) IS AN OUTER-SLOT LAW,
    Delta^B(P U2, U1 P) = P Delta^B(U2, U1) P, not a conjugation law.  It
    delivers T2's declared conjugation action exactly when P = P^-1.  That
    is measured here over the base's admitted scope, and stated as the
    caveat it is: the citation licenses the action at involutive P, and
    every admitted map is measured involutive."""
    rows = {}
    for p in SCOPE["admitted"]:
        t = tuple(p)
        rows[PERM_NAME.get(canon(list(t)), canon(list(t)))] = {
            "order": perm_order(t), "is_an_involution": perm_order(t) <= 2}
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
                "T3_sign_orbit": sorted(set(sgn.values())) if sgn else None,
                "T3_relative_signs_are_mixed":
                    (len(set(relative_sign_class(sgn))) > 1)
                    if sgn else None}
    TABLES["probes"] = rows
    return rows


# ===========================================================================
# 8A. THE MECHANISM, THE STRUCTURE GROUP, AND THE DECLARED SCOPES
#
#     Everything in this section is a measurement of the delivered base.
#     It answers three questions the pair table alone does not:
#       * WHAT GENERATES the holonomy -- and in particular whether the
#         multiplicity of admitted identifications is necessary for it
#         (measured: it is not);
#       * WHAT GROUP the loops generate, and whether that group is inside
#         the base's own declared permutation scopes (measured: it is not);
#       * WHAT THE DECLARED SCOPES DO -- both the 2-element admitted scope
#         every search in this unit runs over, and the declared 8-element
#         admitted extension, which is searched here and reported.
# ===========================================================================
def path_holonomy(sp, G, edges):
    """The closed-loop link product of an edge list, and its signed-
    permutation decomposition."""
    acc = W6.sp_id(K, NC)
    for (li, d) in edges:
        acc = mm(link_variable(sp, G["links"][li], d), acc)
    return acc, signed_perm(acc)


def relative_sign_class(sgn):
    """THE INVARIANT SIGN CONTENT of a signed permutation.  A switching
    multiplies a closed loop's matrix by a global +-1, which flips every
    entry of `sgn` together; the RELATIVE signs s_j * s_0 survive that
    action, while the raw set of signs does not (it flips between [1] and
    [-1] on a uniform-sign loop).  Mixed relative signs are gauge-invariant
    content and are reported as such."""
    s0 = sgn[0]
    return tuple(sgn[j] * s0 for j in range(NC))


def identification_multiplicity(sp):
    """How many DISTINCT admitted maps the base draws at each coordinate.
    A rule contributes only where it admits UNIQUELY, which is the declared
    admission criterion."""
    out = {}
    for t in CHECKPOINTS:
        maps = set()
        per_rule = {}
        for rule in ID_RULES:
            adm = admits(sp, t, rule)
            per_rule[rule["id"]] = len(adm)
            if len(adm) == 1:
                maps.add(tuple(adm[0]))
        out[t] = {"admitted_maps": sorted(
            PERM_NAME.get(canon(list(m)), "another permutation")
            for m in maps),
            "multiplicity": len(maps),
            "admitted_count_per_rule": per_rule}
    return out


def subconnection(sp, pref, rule_ids):
    """THE SUB-CONNECTION built from a chosen subset of the declared rules.
    The REALIZED rule alone is the decisive diagnostic for the mechanism
    question: every coordinate of that connection has multiplicity exactly
    one, so if it is already non-flat then multiplicity is not necessary
    for holonomy."""
    G = build_graph(sp, pref)
    keep = [L for L in G["links"]
            if L["kind"] == "leg" or L["rule"] in rule_ids]
    adj: dict = {n: [] for n in NODES}
    for li, L in enumerate(keep):
        adj[L["a"]].append((li, +1, L["b"]))
        adj[L["b"]].append((li, -1, L["a"]))
    GG = {"links": keep, "adj": adj, "n_nodes": len(NODES),
          "n_links": len(keep),
          "cycle_rank": len(keep) - len(NODES) + 1}
    base = ("F1", 0)
    loops, seen_classes = [], {}
    stack = [(base, [], None)]
    while stack:
        node, edges, last = stack.pop()
        if node == base and edges:
            _H, (p, s) = path_holonomy(sp, GG, edges)
            nm = ("not a signed permutation" if p is None else
                  PERM_NAME.get(canon([p[j] for j in range(NC)]),
                                "another permutation"))
            seen_classes[nm] = seen_classes.get(nm, 0) + 1
            loops.append((tuple(edges), nm, None if p is None
                          else tuple(p[j] for j in range(NC))))
        if len(edges) >= L_MAX:
            continue
        for (li, d, nxt) in GG["adj"][node]:
            if last is not None and li == last:
                continue
            stack.append((nxt, edges + [(li, d)], li))
    grp = {tuple(IDPERM)} | {v for (_e, _n, v) in loops if v is not None}
    changed = True
    while changed:
        changed = False
        for x in list(grp):
            for y in list(grp):
                z = perm_compose(x, y)
                if z not in grp:
                    grp.add(z)
                    changed = True
    mult = identification_multiplicity(sp)
    drawn = {L["t"] for L in keep if L["kind"] == "id"}
    mx = 0
    for t in drawn:
        n = sum(1 for L in keep if L["kind"] == "id" and L["t"] == t)
        mx = max(mx, n)
    return {"rules": sorted(rule_ids), "links": len(keep),
            "identification_links": sum(1 for L in keep if L["kind"] == "id"),
            "cycle_rank": GG["cycle_rank"],
            "closed_paths_at_F1_t0": len(loops),
            "holonomy_classes": dict(sorted(seen_classes.items())),
            "non_identity_closed_paths":
                sum(n for c, n in seen_classes.items()
                    if c != "the identity"),
            "generated_group_order": len(grp),
            "max_identification_multiplicity_at_one_coordinate": mx,
            "multiplicity_map": {t: mult[t]["multiplicity"]
                                 for t in CHECKPOINTS}}


def intertwining_table():
    """DOES THE WING EXCHANGE INTERTWINE THE TWO FRAMES' LEGS?
    P_W L^{F2} P_W versus L^{F1}, leg by leg, setting by setting.  This is
    the SECOND source of curvature: at the PREPARATION leg the answer is no
    at every setting, so a loop that crosses between the frames by the wing
    exchange at one checkpoint and returns at the next picks up
    P_W U_prep^-1 P_W U_prep, which is not the identity."""
    rows = {}
    PW = pmat(WSWAP)
    for sp in SETTING_ORDER:
        for leg in range(1, NLEGS + 1):
            L1 = legs_of(sp, "F1")[leg - 1]
            L2 = legs_of(sp, "F2")[leg - 1]
            rows["%s/leg%d" % (sp, leg)] = {
                "wing_exchange_intertwines_the_leg":
                    bool(mm(PW, mm(L2, PW)) == L1)}
    return rows


def prep_defect_element():
    """P_W U_prep^-1 P_W U_prep, the element the non-intertwining of the
    preparation leg produces, measured at every setting and named."""
    rows = {}
    PW = pmat(WSWAP)
    for sp in SETTING_ORDER:
        U = legs_of(sp, "F1")[0]
        X = mm(PW, mm(minv(U), mm(PW, U)))
        p, s = signed_perm(X)
        rows[sp] = {
            "is_a_signed_permutation": p is not None,
            "name": ("not a signed permutation" if p is None else
                     PERM_NAME.get(canon([p[j] for j in range(NC)]),
                                   "another permutation")),
            "is_the_identity": p is not None and all(p[j] == j
                                                     for j in range(NC))}
    return rows


def closed_path_census(sp, G, values):
    """EVERY CLOSED PATH OF THE COMMITTED PATH SPACE, classified.

    Four things this measures that the pair table does not:
      * how many closed paths carry a holonomy that is NOT a signed
        permutation -- for those the declared invariant is UNDEFINED, and
        the based enumeration drops them.  The count is reported, never
        dropped silently;
      * the holonomy distribution split by corridor, which is what makes
        the flat crossing a statement about ONE COMPARATOR rather than
        about crossing;
      * how many non-flat closed paths never traverse two different rules
        at one coordinate -- the counterexamples to the necessity reading
        of the mechanism;
      * the same census restricted to the declared base point F1@t0."""
    by = {"all": {}, "aligned": {}, "crossing": {},
          "no_two_rules_at_one_coordinate": {}, "based_at_F1_t0": {}}
    drops = {"all": 0, "based_at_F1_t0": 0}
    for r in values:
        if r["start"] != r["end"] or not r["len"]:
            continue
        p, _rel, nm = holonomy_class_of_interned(r["T3"])
        if p is None:
            drops["all"] += 1
        by["all"][nm] = by["all"].get(nm, 0) + 1
        by[r["corridor"]][nm] = by[r["corridor"]].get(nm, 0) + 1
        rules_at: dict = {}
        for (li, _d) in r["edges"]:
            L = G["links"][li]
            if L["kind"] == "id":
                rules_at.setdefault(L["t"], set()).add(L["rule"])
        if not any(len(v) > 1 for v in rules_at.values()):
            by["no_two_rules_at_one_coordinate"][nm] = \
                by["no_two_rules_at_one_coordinate"].get(nm, 0) + 1
        if r["start"] == ("F1", 0):
            by["based_at_F1_t0"][nm] = by["based_at_F1_t0"].get(nm, 0) + 1
            if p is None:
                drops["based_at_F1_t0"] += 1
    out = {k: dict(sorted(v.items())) for k, v in by.items()}
    for k in ("all", "aligned", "crossing", "no_two_rules_at_one_coordinate",
              "based_at_F1_t0"):
        out[k + "_total"] = sum(out[k].values())
        out[k + "_non_identity"] = sum(
            n for c, n in out[k].items() if c != "the identity")
    out["holonomy_not_a_signed_permutation"] = drops["all"]
    out["holonomy_not_a_signed_permutation_based_at_F1_t0"] = \
        drops["based_at_F1_t0"]
    return out


def crossing_counter_loops(sp, G):
    """EVERY MINIMAL LOOP THROUGH A PREFIX-DIVERGENT LINK that this
    instrument can build: the divergent identification paired with an
    identification one checkpoint away, by EITHER rule, in either
    direction.  The declared flat-crossing probe is one row of this table;
    the others are its comparators, and they are not all flat."""
    rows = {}
    idl = [li for li, L in enumerate(G["links"]) if L["kind"] == "id"]
    for li in idl:
        L = G["links"][li]
        if L["prefix_aligned"]:
            continue
        t = L["t"]
        for t2 in CHECKPOINTS:
            if abs(t2 - t) != 1:
                continue
            for other in [x for x in idl if G["links"][x]["t"] == t2]:
                lo, hi = min(t, t2), max(t, t2)
                e1 = find_link(G, "leg", frame="F1", leg=hi)
                e2 = find_link(G, "leg", frame="F2", leg=hi)
                up = (t == hi)
                edges = ([(e1, +1), (li if up else other, -1),
                          (e2, -1), (other if up else li, +1)] if up else
                         [(e1, +1), (other, -1), (e2, -1), (li, +1)])
                _H, (p, s) = path_holonomy(sp, G, edges)
                key = ("t=%d<->t=%d closed by %s at t=%d"
                       % (lo, hi, G["links"][other]["rule"], t2))
                rows[key] = {
                    "holonomy": ("not a signed permutation" if p is None else
                                 PERM_NAME.get(
                                     canon([p[j] for j in range(NC)]),
                                     "another permutation")),
                    "is_the_declared_probe":
                        G["links"][other]["rule"] == L["rule"] and t2 == t - 1}
    return rows


def extension_scope_search(pref):
    """THE DECLARED 96/8 EXTENSION SCOPE, SEARCHED.

    Every admission search that feeds a verdict in this unit runs over the
    2 elements of the declared 72-element scope that survive the j0 filter.
    The declared 96-element extension admits 8, and it is searched HERE and
    nowhere else: the measurement is reported as a result and folded into
    no verdict.  What it shows is that the admission-scope choice is
    LOAD-BEARING -- at the wider scope the uniqueness criterion refuses
    links the narrow scope draws, and the pin's own canonical loop does not
    exist at two settings."""
    rows, changed = {}, []
    for sp in SETTING_ORDER:
        for rule in ID_RULES:
            for t in CHECKPOINTS:
                narrow = len(admits(sp, t, rule))
                wide = len(admits(sp, t, rule, scope="admitted_extension"))
                rows["%s/%s/t%d" % (sp, rule["id"], t)] = {
                    "admitted_at_the_narrow_scope": narrow,
                    "admitted_at_the_declared_extension": wide}
                if narrow != wide:
                    changed.append("%s %s t=%d: %d -> %d"
                                   % (sp, rule["id"], t, narrow, wide))
    wide_links, canonical = {}, {}
    for sp in SETTING_ORDER:
        n = 0
        have = set()
        for rule in ID_RULES:
            for t in CHECKPOINTS:
                if len(admits(sp, t, rule, scope="admitted_extension")) == 1:
                    n += 1
                    have.add((rule["id"], t))
        wide_links[sp] = n
        canonical[sp] = (("FULL", CHECKPOINTS[0]) in have
                         and ("FULL", CHECKPOINTS[-1]) in have)
    return {"per_cell": rows, "cells_where_the_scope_changes_admission":
            sorted(changed),
            "identification_links_at_the_declared_extension": wide_links,
            "the_canonical_loop_exists_at_the_declared_extension": canonical,
            "settings_where_the_canonical_loop_would_not_exist":
                sorted(sp for sp in SETTING_ORDER if not canonical[sp])}


def structure_group(hg):
    """THE ESCAPE, MEASURED.  The based holonomy group's elements are
    tested for membership in the base's OWN declared permutation scopes --
    the admitted 2, the declared 72, the declared 96-element extension and
    its admitted 8.  Two of the four are measured to lie outside ALL of
    them, so the group the connection generates around loops is not a
    subgroup of the base's admitted isomorphisms: THE CONNECTION IS NOT
    PRINCIPAL for the base's own structure group.  The wing exchange's
    factorisation W = X . WX into those two outside elements is measured
    here as well, and so is the mixed-relative-sign content."""
    base = {tuple(p) for p in SCOPE["base"]}
    ext = {tuple(p) for p in SCOPE["extension_all"]}
    adm = {tuple(p) for p in SCOPE["admitted"]}
    admext = {tuple(p) for p in SCOPE["admitted_extension"]}
    rows, outside = {}, {}
    for sp in SETTING_ORDER:
        els = [tuple(e) for e in hg[sp]["group_element_permutations"]]
        per = {}
        n_out = 0
        for e in els:
            nm = PERM_NAME.get(canon(list(e)), "another permutation")
            inside = (e in base) or (e in ext)
            n_out += 0 if inside else 1
            per[nm] = {
                "in_the_admitted_2": e in adm,
                "in_the_declared_72": e in base,
                "in_the_declared_96_extension": e in ext,
                "in_the_admitted_extension_8": e in admext,
                "fixed_points": fixed_points(e), "order": perm_order(e),
                "mixed_relative_signs":
                    bool(hg[sp]["mixed_relative_sign_elements"].get(nm,
                                                                   False))}
        rows[sp] = per
        outside[sp] = n_out
    wing_factorises = (perm_compose(tuple(XQSWAP), tuple(XPSWAP))
                       == tuple(WSWAP))
    return {"per_setting": rows,
            "elements_outside_every_declared_scope": outside,
            "the_wing_exchange_factorises_as_XQ_XP": bool(wing_factorises),
            "factor_fixed_points": {
                "the wing exchange": fixed_points(WSWAP),
                "the qubit-only wing swap": fixed_points(XQSWAP),
                "the pointer-only wing swap": fixed_points(XPSWAP)},
            "the_two_factors_are_in_the_declared_72": [
                tuple(XQSWAP) in base, tuple(XPSWAP) in base],
            "the_two_factors_are_in_the_declared_96": [
                tuple(XQSWAP) in ext, tuple(XPSWAP) in ext]}


def t1_cause_table():
    """T1'S OWN CAUSE, measured by construction and separately from the
    geometric mechanism: the declared one-step Born transition is not
    orthogonal, so its transpose does not invert it.  B(L)^T B(L) = I iff
    B(L) is a permutation matrix, and U_prep's Born shadow carries entries
    that are not 0 or 1.  Also measured: whether the forward Born push of a
    node's law reproduces the NEXT node's own law, cell by cell -- it does
    not at every cell, so 'transports flatly along the law's own forward
    steps' is false where it fails, and those cells are named."""
    legs_fail, push_fail, cells = [], [], 0
    for sp in SETTING_ORDER:
        for fr in FRAMES:
            for leg in range(1, NLEGS + 1):
                cells += 1
                B = born(legs_of(sp, fr)[leg - 1])
                BT = {(j, i): v for (i, j), v in B.items()}
                if mm(BT, B) != W6.sp_id(K, NC):
                    legs_fail.append("%s/%s/leg%d" % (sp, fr, leg))
                pushed = t1_push(sp, t1_value(sp, fr, leg - 1),
                                 {"kind": "leg", "frame": fr, "leg": leg}, +1)
                own = t1_value(sp, fr, leg)
                if pushed is None or canon(pushed) != canon(own):
                    push_fail.append("%s/%s/leg%d" % (sp, fr, leg))
    return {"cells": cells,
            "legs_whose_transposed_Born_step_does_not_invert_it": legs_fail,
            "legs_where_the_forward_push_is_not_the_next_node's_own_law":
                push_fail}


def t2_readtime_census():
    """THE READ TIME IS A COORDINATE OF T1'S DATUM AND NOT OF T2'S.
    T1 carries its checkpoint inside the datum, so two T1 data read at
    different checkpoints can never compare equal.  T2's datum is the
    defect matrix at the node's own cut and carries no such tag: measured
    here, T2 data read at different checkpoints DO compare equal, at every
    setting.  No comparison in this unit is affected -- the matched table
    pairs only paths sharing both endpoints, so every compared pair is read
    at one coordinate -- but the claim is corrected to what is measured."""
    equal_pairs, t1_equal = {}, {}
    for sp in SETTING_ORDER:
        for fr in FRAMES:
            eq, e1 = [], []
            for a, b in itertools.combinations(CHECKPOINTS, 2):
                if t2_value(sp, fr, a) == t2_value(sp, fr, b):
                    eq.append("(%d,%d)" % (a, b))
                if (canon(t1_value(sp, fr, a)["law"])
                        == canon(t1_value(sp, fr, b)["law"])):
                    e1.append("(%d,%d)" % (a, b))
            equal_pairs["%s/%s" % (sp, fr)] = eq
            t1_equal["%s/%s" % (sp, fr)] = e1
    keys_with = {structural_key(t2_value(sp, fr, t))
                 for sp in SETTING_ORDER for fr in FRAMES
                 for t in CHECKPOINTS}
    return {"T2_pairs_of_checkpoints_whose_data_are_equal": equal_pairs,
            "T1_pairs_of_checkpoints_whose_LAWS_are_equal_before_the_tag":
                t1_equal,
            "distinct_T2_node_data_without_a_read_time": len(keys_with),
            "distinct_T1_node_data_with_the_read_time":
                len({structural_key(t1_value(sp, fr, t))
                     for sp in SETTING_ORDER for fr in FRAMES
                     for t in CHECKPOINTS}),
            "distinct_T1_node_data_without_the_read_time":
                len({canon(t1_value(sp, fr, t)["law"])
                     for sp in SETTING_ORDER for fr in FRAMES
                     for t in CHECKPOINTS})}


def t2_conjugation_table():
    """WHERE CONJUGATION BY THE WING EXCHANGE MOVES THE DEFECT, at every
    (setting, checkpoint) cell of frame F1 -- and, separately, where that
    element is an ADMITTED identification.  T2's holonomy needs both, which
    is why it is carried by one setting alone."""
    rows = {}
    for sp in SETTING_ORDER:
        for t in CHECKPOINTS:
            D = defect_matrix(sp, "F1", t)
            moved = (W6.sp_conj(D, WSWAP) != D)
            admitted = any(len(admits(sp, t, r)) == 1
                           and tuple(admits(sp, t, r)[0]) == tuple(WSWAP)
                           for r in ID_RULES)
            rows["%s/t%d" % (sp, t)] = {
                "defect_is_nonzero": bool(D),
                "conjugation_moves_the_defect": bool(moved),
                "the_wing_exchange_is_admitted_here": bool(admitted),
                "both": bool(moved and admitted)}
    return rows


# ===========================================================================
# 9.  THE GAUGE SELF-TEST (RUNBOOK section 14) -- FRESH, and with teeth
# ===========================================================================
def gauge_group(G):
    """THE DECLARED SWITCHING GROUP: one sign per link of the setting's own
    graph -- every link, legs and identifications alike.  Its size is
    computed by enumeration, never typed, and the sweep is COMPLETE at
    every setting: 2^9 = 512 where only the full-leg rule supplies
    identifications and 2^13 = 8192 where the realized rule supplies four
    more.  The CHECKPOINT subgroup is the part induced by a sign at each
    NODE, which is the base's own checkpoint-phase redundancy; it is
    enumerated separately and is also complete."""
    ix = list(range(len(G["links"])))
    order = 2 ** len(ix)
    full = [dict(zip(ix, eps))
            for eps in itertools.product((1, -1), repeat=len(ix))]
    if MUTANT == "gauge-subsample":
        full = full[:1]
    cp, seen = [], set()
    for s in itertools.product((1, -1), repeat=len(NODES)):
        sn = dict(zip(NODES, s))
        sw = {}
        for li in ix:
            L = G["links"][li]
            sw[li] = sn[L["a"]] * sn[L["b"]]
        key = canon(sorted(sw.items()))
        if key not in seen:
            seen.add(key)
            cp.append(sw)
    return {"links": ix, "full": full, "checkpoint": cp,
            "order": order, "swept": len(full)}


def loop_edge_variables(sp, G, edges):
    """The loop's link variables in traversal order, and their negatives.
    These are the FIXTURE the switching acts on -- the committed model's own
    operators and permutation matrices, built once per loop exactly as the
    base itself holds them (D6).  Every holonomy the self-test measures is
    rebuilt from them, product by product, for every switching."""
    A = [link_variable(sp, G["links"][li], d) for (li, d) in edges]
    return A, [W6.sp_neg(K, X) for X in A]


def switched_signs(edges, sw):
    """The sign the switching puts on each traversal of the loop.  The
    `gauge-sign` mutant drops the switching on a REVERSED traversal -- the
    sign/orientation perturbation RUNBOOK section 14 requires -- and the
    mutation is injected here, in the computation."""
    drop_the_sign_on_a_reversed_traversal = (MUTANT == "gauge-sign")
    out = []
    for (li, d) in edges:
        e = sw.get(li, 1)
        if drop_the_sign_on_a_reversed_traversal and d < 0:
            e = 1
        out.append(e)
    return out


def loop_matrix_fresh(sp, A, negA, signs, key):
    """Recomputed from the link variables EVERY time (RUNBOOK section 14
    addendum).  The call is routed THROUGH the instrument's value cache so
    that the bypass is a measured fact and not an absence: in fresh mode the
    cache is bypassed and every call counts a MISS, while the `memo-lax`
    mutant restores the reviewed defect -- a self-test reading the cache --
    and then the checkpoint subgroup's re-visits of switchings already swept
    register as HITS and the gate falls over."""
    def build():
        acc = W6.sp_id(K, NC)
        for k in range(len(A)):
            acc = mm_memo(A[k] if signs[k] > 0 else negA[k], acc)
        return acc
    return _memo(("loop", sp, key), build)


def run_gauge_selftest(graphs):
    global _FRESH
    prog("section 14: the gauge-covariance self-test (fresh evaluation)")
    _FRESH = True
    before = dict(_CACHE)
    rows, sizes = {}, {}
    not_signed = perm_moved = sign_fail = scalar_dev = 0
    moved_raw = 0
    tested = comparisons = 0
    for sp in SETTING_ORDER:
        G = graphs[sp]
        GG = gauge_group(G)
        sizes[sp] = {"switching_group_order": GG["order"],
                     "switchings_swept": GG["swept"],
                     "sweep_is_complete": GG["swept"] == GG["order"],
                     "checkpoint_subgroup": len(GG["checkpoint"]),
                     "gauge_links": len(GG["links"])}
        # THE TESTED SET IS FIXED BY DECLARATION (section 14 addendum):
        # EVERY declared loop that carries an edge list, taken in the order
        # the probes are built, never selected by the verdicts under audit.
        # The twisted comparator is the one declared probe with no edge list
        # of its own -- it is the canonical loop with one link overwritten --
        # and it is named here as the exclusion it is.
        swept = [x for x in declared_loops(sp, G) if x["edges"] is not None]
        for loop in swept:
            A, negA = loop_edge_variables(sp, G, loop["edges"])
            H0 = W6.sp_id(K, NC)
            for X in A:
                H0 = mm(X, H0)
            perms, signs, cp_signs, rels = set(), set(), set(), set()
            for phase, group in (("full", GG["full"]),
                                 ("checkpoint", GG["checkpoint"])):
                for sw in group:
                    sg = switched_signs(loop["edges"], sw)
                    H = loop_matrix_fresh(sp, A, negA, sg,
                                          (loop["name"], tuple(sg)))
                    tested += 1
                    # THE MEASURED ACTION: a switching multiplies a closed
                    # loop's link product by the product of the signs it
                    # puts on the traversals -- a GLOBAL SCALAR.  This is
                    # the sweep's substantive measurement; the invariance
                    # of the permutation part is its consequence.
                    tot = 1
                    for e in sg:
                        tot *= e
                    comparisons += 1
                    if H != (H0 if tot > 0 else W6.sp_neg(K, H0)):
                        scalar_dev += 1
                    p, s = signed_perm(H)
                    if p is None:
                        not_signed += 1
                        continue
                    if phase == "full":
                        perms.add(canon([p[j] for j in range(NC)]))
                        signs.add(tuple(sorted(set(s.values()))))
                        rels.add(relative_sign_class(s))
                    else:
                        cp_signs.add(tuple(sorted(set(s.values()))))
            if len(perms) != 1:
                perm_moved += 1
            if len(cp_signs) != 1:
                sign_fail += 1
            if len(signs) > 1:
                moved_raw += 1
            rows["%s / %s" % (sp, loop["name"])] = {
                "distinct_permutation_parts_under_the_full_group": len(perms),
                "distinct_sign_orbits_under_the_full_group": len(signs),
                "distinct_relative_sign_classes_under_the_full_group":
                    len(rels),
                "distinct_sign_orbits_under_the_checkpoint_subgroup":
                    len(cp_signs)}
    after = dict(_CACHE)
    hits = after["value_cache_hits"] - before["value_cache_hits"]
    misses = after["value_cache_misses"] - before["value_cache_misses"]
    _FRESH = False
    TABLES["gauge_selftest"] = {
        "per_loop": rows, "group_sizes": sizes,
        "loops_swept_per_setting": {sp: sum(1 for k in rows
                                            if k.startswith(sp + " /"))
                                    for sp in SETTING_ORDER},
        "the_declared_probe_excluded_from_the_sweep":
            "the twisted comparator: it carries no edge list of its own, "
            "being the canonical loop with one link overwritten"}
    gate("NT-GAUGE-COVARIANCE", "measurement",
         "THE MANDATORY SECTION 14 SELF-TEST, STATED AT WHAT IT MEASURES.  "
         "Every declared loop that has an edge list -- ALL of them, not one "
         "per role -- has its holonomy RECOMPUTED FROM THE LINK VARIABLES "
         "under EVERY element of the declared switching group: the sweep is "
         "COMPLETE at every setting, 512 where only the full-leg rule "
         "supplies identifications and 8192 where the realized rule "
         "supplies four more, and the checkpoint subgroup (128) is complete "
         "everywhere.  The gate measures four things that CAN fail: (1) the "
         "declared switching acts on a closed loop by the GLOBAL SCALAR "
         "given by the product of the signs it puts on the traversals -- "
         "every swept holonomy is compared, exactly, against that scalar "
         "times the unswitched holonomy; (2) every swept holonomy is a "
         "SIGNED PERMUTATION at all, which for the eight-link canonical "
         "loop of non-permutation matrices is a real fact; (3) the loop's "
         "SIGN is fixed under the whole checkpoint subgroup -- the "
         "telescoping property a wrong sign convention breaks; (4) the "
         "group orders are the enumerated powers of two.  The `gauge-sign` "
         "mutant drops the switching on a reversed traversal -- the "
         "sign/orientation perturbation section 14 requires -- and must die "
         "at clauses (1) and (3); the `gauge-subsample` mutant shrinks the "
         "sweep and must die at clause (4).  THE INVARIANCE OF THE "
         "PERMUTATION PART IS NOT A CLAUSE OF THIS GATE: it FOLLOWS from "
         "clause (1), and is reported as the disclosure "
         "NT-GAUGE-PERMUTATION-FORCED",
         scalar_dev == 0 and not_signed == 0 and sign_fail == 0
         and tested > 0
         and all(v["sweep_is_complete"] for v in sizes.values())
         and all(v["switching_group_order"] == 2 ** v["gauge_links"]
                 for v in sizes.values())
         and all(v["checkpoint_subgroup"] == 2 ** (len(NODES) - 1)
                 for v in sizes.values()),
         {"instances_tested": tested,
          "exact_matrix_comparisons_against_the_scalar_action": comparisons,
          "deviations_from_the_global_scalar_action": scalar_dev,
          "swept_holonomies_that_are_not_signed_permutations": not_signed,
          "loops_whose_sign_moved_under_the_checkpoint_subgroup": sign_fail,
          "group_sizes": sizes})
    gate("NT-GAUGE-PERMUTATION-FORCED", "disclosure",
         "AN ANALYTICALLY FORCED CLAUSE, REPORTED AS A DISCLOSURE AND NOT "
         "AS A MUST-PASS MEASUREMENT.  The declared switching assigns one "
         "sign per link, so it acts on a CLOSED loop's link product by the "
         "product of those signs -- a global +-1 (measured: clause (1) of "
         "NT-GAUGE-COVARIANCE, %d exact comparisons, %d deviations).  A "
         "signed permutation matrix and its negative have the SAME "
         "permutation part.  Therefore the permutation part of a closed "
         "loop's holonomy is invariant under the whole switching group BY "
         "ALGEBRA, for every loop, every setting and every switching, "
         "whether or not anything else in this instrument is right: no "
         "switching and no mutant could make this clause fail, and it is "
         "not claimed as a measurement.  The sweep confirms it -- exactly "
         "one permutation part at every swept loop, over the COMPLETE "
         "group -- and that confirmation is what is reported here.  The "
         "same algebra makes the RELATIVE sign class s_j*s_0 invariant "
         "while the raw sign set is not, which is why the relative class is "
         "the sign content this unit reports"
         % (comparisons, scalar_dev),
         True,
         {"loops_whose_permutation_part_moved_under_the_full_group":
              perm_moved,
          "loops_swept": len(rows),
          "distinct_relative_sign_classes_per_loop":
              sorted({v["distinct_relative_sign_classes_under_the_full_group"]
                      for v in rows.values()})})
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
    skipped = 0
    for sp in SETTING_ORDER:
        G = graphs[sp]
        for loop in declared_loops(sp, G):
            if loop["edges"] is None:
                skipped += 1
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
         "comparison and must die here.  COVERAGE, stated: the test runs on "
         "every declared loop that carries an edge list, and the loops it "
         "does not reach are named -- the twisted comparators, which are "
         "the canonical loop with one link overwritten and have no edge "
         "list of their own, so the negative control is not flip-tested",
         same_dir, {"per_loop": rows, "loops_tested": len(rows),
                    "declared_loops_without_an_edge_list_skipped": skipped})

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
    o4 = _o4()
    certrow = [g for g in o4["gates"] if g["id"] == "O4-CERT-BITES"][0]
    cert_at_division = {
        "t=%d" % NLEGS: certrow["value"]["per_class_and_time"]
        ["F-CFG@t%d" % NLEGS]}
    gate("NT-ADMISSION-DISCLOSED", "disclosure",
         "THE ADMISSION CRITERION IS A DECLARATION AND ITS CONTENT IS "
         "REPORTED.  Identification links are admitted by UNIQUENESS of the "
         "admitted transport (the O4 discriminator's FORCED), and this "
         "unit's vocabulary says FORCED, never `certified': the O4 terminal "
         "CERTIFICATE refuses these transports at the coordinates that carry "
         "the result.  Read from the committed O4 receipt and printed here: "
         "the certificate is degenerate at the first intermediate "
         "checkpoint, refuses the pair at the second, and at the FINAL "
         "declared division event it is VACUOUS at SP-E.  An admission "
         "criterion reading the certificate instead would therefore admit "
         "links at the final division event alone -- and at SP-E, one of "
         "the two settings that carry the entire result, not even there, so "
         "that setting's loop space would be empty outright.  Both readings "
         "are printed; every verdict below is licensed at the declared "
         "criterion and at no wider scope.  A rule-label flip is not "
         "applicable: one full-leg rule is declared, so there is nothing to "
         "flip it against",
         True, {"per_setting": cert_links,
                "the_O4_certificate_at_the_final_division_event":
                    cert_at_division,
                "rule_label_flip": "not applicable: one full-leg rule is "
                                   "declared"})
    TABLES["flip_tests"] = {"direction": rows,
                            "admission_disclosure": cert_links,
                            "the_O4_certificate_at_the_final_division_event":
                                cert_at_division}
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
    inv = admitted_maps_are_involutions()
    gate("NT-T2-POSABILITY", "measurement",
         "T2'S EXACT-POSABILITY GATE, EVALUATED BEFORE ANY T2 RESULT (the "
         "RQ0-SYNTH lesson).  The composition-defect question is posed at a "
         "node only if the committed laws supply BOTH cut factors and their "
         "amplitude composition is EXACT there, so that Delta^B is the "
         "defect of a genuine factorisation of the declared process and not "
         "of an invented one.  Had either clause failed the unit would "
         "report NT-BLOCKED-AT-<posability> and force nothing.  THE WELD, "
         "third clause, WITH ITS SOURCES AND ITS ENTAILMENT STATED: the "
         "defect matrix computed from paper 1's definition is measured "
         "IDENTICAL, entry by entry, at every node, to the declared-law "
         "residual Gamma(N<-0) - Gamma(N<-t)Gamma(t<-0) built by W5's OWN "
         "COMMITTED CODE (its `gam`, `mmul` and `ksub`, imported from "
         "v12/code/w5_ltp_lemma_exact.py and applied to this unit's "
         "propagators), and W5's own committed residual weights anchor it "
         "exit-1 (A23).  That identity FOLLOWS FROM CLAUSE 2 -- same "
         "subtrahend, minuends gated equal -- and the entailment is itself "
         "measured and printed rather than left for the reader to find.  It "
         "is the case paper 1 ENGRAVED in advance as the one exemption to "
         "its own scope statement (Delta^B is not the residual of a "
         "declared stochastic law UNLESS that law is declared to be B(U2), "
         "which is what this base declares), and W5's committed M4 recorded "
         "it, with its cause, at the single cut t = 2.  What is measured "
         "HERE and not there is the extension to all four cuts in both "
         "frames.  The `defect-order` mutant composes the two Born shadows "
         "in the wrong order and must die here",
         pos_ok, {"nodes_tested": sum(len(v) for v in posab.values()),
                  "distinct_defect_weights": nz,
                  "clause_3_is_entailed_by_clause_2_at_every_node":
                      all(r["clause_3_is_entailed_by_clause_2"]
                          for sp in posab for r in posab[sp].values()),
                  "the_residual_is_built_by_W5's_committed_code":
                      str(W5_SOURCE.relative_to(REPO)),
                  "sources_of_the_identity": [
                      "paper 1 section 2.3, the engraved clause: Delta^B is "
                      "not the residual of any declared stochastic law "
                      "unless that law is declared to be B(U2)",
                      "v12/code/w5_ltp_lemma_exact.py check M4, at the cut "
                      "t = 2"],
                  "this_unit's_extension": "all four cuts, both frames",
                  "every_admitted_map_is_an_involution_so_paper_1's_"
                  "outer-slot_law_(iv)_delivers_the_conjugation_action":
                      inv})

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
            # NOT a based holonomy: this counts distinct closed-path values
            # over ALL eight base points, so a setting can enter it because
            # closed paths based at different nodes carry different data,
            # with no move transporting anything.  Named for what it counts.
            "settings_where_closed_path_values_differ_across_base_points":
                nontrivial,
            "closed_path_value_set_size_over_all_base_points": hol}
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
    # THE O4 READ TIMES, read from the committed receipt: the checkpoints at
    # which O4 evaluated anything.  t = 0 is OUTSIDE them -- it is this
    # unit's own extension of the coordinate set -- so the witnesses are
    # counted separately at O4's coordinates and at this unit's.
    o4t = sorted({int(k.split("/")[0][1:])
                  for k in _o4()["tables"]["read_time_structure"]
                  ["prefix_alignment"]})
    probe_tw_o4 = sorted(k for k in probe_tw
                         if int(k.split("t=")[-1]) in o4t)
    probe_tw_ext = sorted(k for k in probe_tw if k not in probe_tw_o4)
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
         "verdict is the one the table supports, that each probe class "
         "agrees with its own column of the table, and that the twisted "
         "corridor survives at O4'S OWN READ TIMES -- the checkpoints the "
         "committed base evaluated -- and not only at the coordinate this "
         "unit added.  The `path-collapse` mutant makes every path carry "
         "the same key, so that no pair can ever disagree while the probes "
         "still fire, and must die at the agreement clauses",
         (refuted == (bool(probe_tw) or bool(probe_fc)))
         and (twisted > 0) == bool(probe_tw)
         and (flatcross > 0) == bool(probe_fc)
         and bool(probe_tw_o4),
         {"verdict": verdict,
          "aligned_pairs_that_disagree": twisted,
          "crossing_pairs_that_agree": flatcross,
          "twisted_corridor_probes_that_fired": probe_tw,
          "flat_crossing_probes_that_fired": probe_fc,
          "the_O4_read_times": o4t,
          "twisted_corridor_probes_at_O4's_own_read_times": probe_tw_o4,
          "twisted_corridor_probes_at_this_unit's_added_coordinate":
              probe_tw_ext})
    FINDINGS["hypothesis"] = {
        "verdict": verdict,
        "twisted_corridor_witnesses": probe_tw,
        "twisted_corridor_witnesses_at_O4's_own_read_times": probe_tw_o4,
        "twisted_corridor_witnesses_at_the_added_coordinate_t0":
            probe_tw_ext,
        "flat_crossing_witnesses": probe_fc,
        "aligned_pairs_that_disagree": twisted,
        "crossing_pairs_that_agree": flatcross}
    return verdict


def run_mechanism(graphs, values, pref, probes):
    """WHAT GENERATES THE HOLONOMY -- measured, and scoped to what the
    measurement supports."""
    prog("the mechanism: multiplicity, the single-rule sub-connections, "
         "the prep leg")
    mult = {sp: identification_multiplicity(sp) for sp in SETTING_ORDER}
    hi = sorted("%s/t%d" % (sp, t) for sp in SETTING_ORDER
                for t in CHECKPOINTS if mult[sp][t]["multiplicity"] > 1)
    sub = {}
    for sp in SETTING_ORDER:
        for rules in (("FULL",), ("REAL",), ("FULL", "REAL")):
            sub["%s/%s" % (sp, "+".join(rules))] = subconnection(sp, pref,
                                                                 set(rules))
        prog("  sub-connections %s" % sp)
    inter = intertwining_table()
    prep = prep_defect_element()
    census, cross = {}, {}
    for sp in SETTING_ORDER:
        census[sp] = closed_path_census(sp, graphs[sp], values[sp])
        cross[sp] = crossing_counter_loops(sp, graphs[sp])
        prog("  closed-path census %s" % sp)
    TABLES["mechanism"] = {
        "identification_multiplicity": {
            "%s/t%d" % (sp, t): mult[sp][t]
            for sp in SETTING_ORDER for t in CHECKPOINTS},
        "coordinates_of_multiplicity_at_least_two": hi,
        "single_rule_subconnections": sub,
        "wing_exchange_intertwining_per_leg": inter,
        "the_prep_leg_defect_element": prep}
    TABLES["closed_path_census"] = census
    TABLES["crossing_counter_loops"] = cross

    # SUFFICIENCY: at every coordinate of multiplicity >= 2 the bigon fires.
    bigons = {k: v for k, v in probes.items()
              if v["role"] == "THE TWISTED-CORRIDOR PROBE"}
    fired = sorted(k for k, v in bigons.items()
                   if not v["T3_permutation_is_the_identity"])
    # NECESSITY FAILS, three ways, all measured.
    single = {k: v for k, v in sub.items() if k.endswith("/REAL")}
    # the realized rule supplies identifications at two settings only; the
    # sub-connection is a connection at all six, but it is only a
    # sub-connection WITH LINKS where the rule admits, and the necessity
    # question is asked exactly there.
    single_active = {k: v for k, v in single.items()
                     if v["identification_links"] > 0}
    single_nonflat = {k: v["non_identity_closed_paths"]
                      for k, v in single.items()}
    single_mult1 = all(
        v["max_identification_multiplicity_at_one_coordinate"] <= 1
        for v in single.values())
    nonflat_without = {sp: census[sp]["no_two_rules_at_one_coordinate_"
                                      "non_identity"]
                       for sp in SETTING_ORDER}
    prep_fails = sorted(k for k, v in inter.items()
                        if k.endswith("/leg1")
                        and not v["wing_exchange_intertwines_the_leg"])
    gate("NT-MECHANISM-SUFFICIENT-NOT-NECESSARY", "measurement",
         "WHAT GENERATES THE HOLONOMY, MEASURED IN BOTH DIRECTIONS.  "
         "SUFFICIENCY: the base admits two DIFFERENT identifications at one "
         "coordinate exactly where the full-leg rule and the realized-only "
         "rule both admit uniquely and their maps differ by the wing "
         "exchange, and at every such coordinate the bigon they form is "
         "measured non-flat -- the gate counts those coordinates and "
         "measures that a twisted-corridor probe fires at each.  NECESSITY "
         "FAILS, and the gate measures the failure rather than asserting "
         "the converse: (a) the SINGLE-RULE sub-connection built from the "
         "realized rule alone, in which EVERY coordinate has multiplicity "
         "exactly one, already carries non-identity closed-path holonomy; "
         "(b) in the delivered graph, closed paths that never traverse two "
         "different rules at one coordinate are non-flat in quantity, "
         "counted per setting; (c) the proximate cause is measured -- the "
         "wing exchange does NOT intertwine the PREPARATION leg at any "
         "setting, so a loop crossing between the frames by it at one "
         "checkpoint and returning at the next picks up "
         "P_W U_prep^-1 P_W U_prep, which is measured to be a non-identity "
         "permutation.  THE CLAIM IS THEREFORE SUFFICIENT, NEVER "
         "BICONDITIONAL, and it is a claim about the geometric layer (T3) "
         "and T2's single cell only: T1 is excluded, its path-dependence "
         "having a different and weaker cause (NT-T1-CAUSE).  The `id-lax` "
         "mutant admits every element of the scope, so no rule admits "
         "uniquely and no bigon fires, and must die at the sufficiency "
         "clause",
         len(hi) > 0 and len(fired) == len(hi)
         and single_mult1
         and len(single_active) > 0
         and all(v["non_identity_closed_paths"] > 0
                 for v in single_active.values())
         and sum(1 for sp in SETTING_ORDER if nonflat_without[sp] > 0) > 0
         and all(nonflat_without[sp] > 0
                 for sp in SETTING_ORDER
                 if sub["%s/FULL+REAL" % sp]["generated_group_order"] > 1)
         and len(prep_fails) == len(SETTING_ORDER),
         {"coordinates_of_multiplicity_at_least_two": hi,
          "twisted_corridor_probes_that_fired": fired,
          "single_rule_realized_subconnection_non_identity_closed_paths":
              single_nonflat,
          "single_rule_subconnections_with_links":
              sorted(single_active),
          "single_rule_subconnection_multiplicity_is_one_everywhere":
              bool(single_mult1),
          "non_flat_closed_paths_that_never_use_two_rules_at_one_coordinate":
              nonflat_without,
          "settings_where_the_wing_exchange_fails_to_intertwine_the_prep_leg":
              prep_fails,
          "the_prep_leg_defect_element": prep})
    return sub, inter, census, cross


def run_structure_group(hg_full):
    """THE HOLONOMY GROUP, ITS FACTORISATION, AND ITS ESCAPE FROM THE
    DECLARED SCOPES."""
    sg = structure_group(hg_full)
    TABLES["structure_group"] = sg
    FINDINGS["structure_group"] = {
        "the_group_at_the_two_symmetric_settings":
            sorted(sg["per_setting"]["SP-E"]),
        "elements_outside_every_declared_scope":
            sg["elements_outside_every_declared_scope"],
        "the_wing_exchange_factorises_as_XQ_XP":
            sg["the_wing_exchange_factorises_as_XQ_XP"]}
    sym = [sp for sp in SETTING_ORDER
           if hg_full[sp]["generated_group_order"] > 1]
    orders = {sp: hg_full[sp]["generated_group_order"]
              for sp in SETTING_ORDER}
    vs = {sp: hg_full[sp]["value_set_size"] for sp in SETTING_ORDER}
    mixed = {sp: len(hg_full[sp]["elements_with_mixed_relative_signs"])
             for sp in SETTING_ORDER}
    gate("NT-HOLONOMY-GROUP", "measurement",
         "THE HOLONOMY VALUE SET IS COUNTED AS PERMUTATIONS, NEVER AS NAME "
         "LABELS.  The value set is the set of permutation parts realized "
         "by closed paths of the committed path space based at F1@t0; a set "
         "of NAMES counts as many elements as the naming table happens to "
         "know, which is a count of the wrong object.  The gate measures "
         "(1) that the value set has the same cardinality as the group it "
         "generates by closure -- so the value set is already CLOSED at the "
         "declared length bound, which is a measurement and not an "
         "assumption; (2) that the group is abelian with every element of "
         "order dividing two, i.e. elementary abelian; (3) that the number "
         "of closed paths based there whose holonomy is not a signed "
         "permutation, and which the value set therefore cannot contain, is "
         "counted and printed rather than silently dropped.  The "
         "`label-collapse` mutant counts labels instead of permutations and "
         "must die at clause (1)",
         all(vs[sp] == orders[sp] for sp in SETTING_ORDER)
         and all(hg_full[sp]["the_value_set_is_the_generated_group"]
                 for sp in SETTING_ORDER)
         and all(hg_full[sp]["the_group_is_abelian"]
                 and hg_full[sp]["every_element_squares_to_the_identity"]
                 for sp in SETTING_ORDER),
         {"value_set_size_per_setting": vs,
          "generated_group_order_per_setting": orders,
          "settings_with_a_nontrivial_holonomy_group": sym,
          "closed_paths_based_at_F1_t0_whose_holonomy_is_not_a_signed_"
          "permutation": {sp: hg_full[sp]["closed_paths_whose_holonomy_is_"
                                          "not_a_signed_permutation"]
                          for sp in SETTING_ORDER},
          "elements_with_mixed_relative_signs":
              {sp: hg_full[sp]["elements_with_mixed_relative_signs"]
               for sp in SETTING_ORDER}})
    gate("NT-STRUCTURE-GROUP-ESCAPES-THE-SCOPE", "measurement",
         "THE CONNECTION IS NOT PRINCIPAL FOR THE BASE'S OWN ADMITTED "
         "ISOMORPHISMS.  The links of this connection are transports the "
         "base admits; the GROUP THEY GENERATE AROUND LOOPS is measured "
         "against the base's own declared permutation scopes, element by "
         "element.  At the two symmetric settings that group is the Klein "
         "four-group {1, W, X, WX}: W is the base's wing exchange, X is the "
         "QUBIT-ONLY wing swap and WX the POINTER-ONLY wing swap, and the "
         "factorisation W = X . WX is measured, not assumed.  The gate "
         "measures that exactly TWO of the four elements lie outside the "
         "declared 72-element scope AND outside its declared 96-element "
         "extension AND outside both admitted sets -- the declared scope's "
         "wing flag always moves the qubit pair and the pointer pair "
         "TOGETHER, so neither half of W is in it.  It also measures the "
         "gauge-invariant SIGN content: the relative sign class s_j*s_0 "
         "survives the switching action (the raw sign set does not), and "
         "exactly two of the four elements are measured to carry MIXED "
         "relative signs.  A theory that earns a structure group half of "
         "whose elements its own base does not certify as isomorphisms has "
         "earned a structure group the base does not recognise, and that is "
         "reported as the result it is.  The `scope-lax` mutant subsamples "
         "the admitted scope, the realized rule then admits nothing, the "
         "group collapses to the identity, and it must die here",
         sg["the_wing_exchange_factorises_as_XQ_XP"]
         and all(sg["elements_outside_every_declared_scope"][sp] == 2
                 for sp in sym)
         and all(sg["elements_outside_every_declared_scope"][sp] == 0
                 for sp in SETTING_ORDER if sp not in sym)
         and len(sym) > 0
         and all(orders[sp] == 4 for sp in sym)
         and not any(sg["the_two_factors_are_in_the_declared_72"])
         and not any(sg["the_two_factors_are_in_the_declared_96"])
         and all(mixed[sp] == 2 for sp in sym),
         {"per_setting": sg["per_setting"],
          "elements_outside_every_declared_scope":
              sg["elements_outside_every_declared_scope"],
          "the_wing_exchange_factorises_as_XQ_XP":
              sg["the_wing_exchange_factorises_as_XQ_XP"],
          "fixed_points": sg["factor_fixed_points"],
          "elements_carrying_mixed_relative_signs": mixed})


def run_scopes(pref):
    """THE DECLARED SCOPES, AND WHAT DEPENDS ON THEM."""
    prog("the declared scopes: the narrow one used, the extension searched")
    ext = extension_scope_search(pref)
    TABLES["admission_scope"] = ext
    gate("NT-ADMISSION-SCOPE-IS-LOAD-BEARING", "disclosure",
         "THE ADMISSION SCOPE IS A CHOICE, AND IT IS LOAD-BEARING.  Every "
         "admission search that feeds a link, a profile or a verdict in "
         "this unit runs over the 2 elements of the declared 72-element "
         "permutation scope that survive the j0 filter; every negative in "
         "this unit is a negative at THAT scope.  The declared 96-element "
         "extension, which admits 8, is SEARCHED HERE -- the same "
         "four-clause predicate, the wider set -- and the measurement is "
         "reported and folded into no verdict.  What it shows: at the wider "
         "scope the full-leg rule admits TWO permutations at the cells "
         "printed below, so the uniqueness criterion REFUSES those links, "
         "and the settings at which the pin's own canonical loop would then "
         "not exist at all are named.  The admission criterion's FORCED "
         "reading is therefore scope-dependent, and this unit's results "
         "stand at the narrow scope it declares and at no other",
         True,
         {"cells_where_the_scope_changes_admission":
              ext["cells_where_the_scope_changes_admission"],
          "identification_links_at_the_declared_extension":
              ext["identification_links_at_the_declared_extension"],
          "the_canonical_loop_exists_at_the_declared_extension":
              ext["the_canonical_loop_exists_at_the_declared_extension"],
          "settings_where_the_canonical_loop_would_not_exist":
              ext["settings_where_the_canonical_loop_would_not_exist"]})


def run_layers():
    """T1'S OWN CAUSE AND T2'S OWN COORDINATES -- the two layer statements
    the mechanism section is NOT about."""
    prog("the layers: T1's cause, T2's read time, T2's conjugation")
    t1c = t1_cause_table()
    rt = t2_readtime_census()
    cj = t2_conjugation_table()
    TABLES["layers"] = {"t1_cause": t1c, "t2_read_time": rt,
                        "t2_conjugation": cj}
    gate("NT-T1-CAUSE", "disclosure",
         "T1'S PATH-DEPENDENCE HAS ITS OWN CAUSE, AND IT IS NOT THE "
         "GEOMETRIC ONE.  T1 is carried forward by the declared one-step "
         "Born transition and backward by its transpose, and the gate "
         "measures BY CONSTRUCTION that the transpose does not invert the "
         "forward step: B(L)^T B(L) = I would require B(L) to be a "
         "permutation matrix, and the preparation leg's Born shadow is "
         "measured not to be one at any setting or frame.  That is why T1 "
         "fails to return around a loop at every setting, including the "
         "four where no coordinate admits two identifications -- so T1 is "
         "excluded from the identification-multiplicity mechanism.  It "
         "also measures, cell by cell, where the forward Born push of a "
         "node's law is NOT the next node's own law: the cells are named, "
         "because a sentence saying T1 transports flatly along the law's "
         "own forward steps is false exactly there.  THIS IS A DISCLOSURE, "
         "NOT A MUST-PASS GATE, and for a stated reason: no declared mutant "
         "falsifies it -- a mutation that made the declared Born step "
         "orthogonal would not be a perturbation of this instrument but a "
         "different model -- so it is reported as a measurement of the "
         "committed base rather than counted in the falsification census.  "
         "No verdict rests on it: T1's verdict is read off the matched "
         "table of path pairs and from nothing else",
         len(t1c["legs_whose_transposed_Born_step_does_not_invert_it"]) > 0
         and t1c["cells"] == len(SETTING_ORDER) * len(FRAMES) * NLEGS,
         {"cells": t1c["cells"],
          "legs_whose_transposed_Born_step_does_not_invert_it":
              len(t1c["legs_whose_transposed_Born_step_does_not_invert_it"]),
          "cells_where_the_forward_push_is_not_the_next_node's_own_law":
              t1c["legs_where_the_forward_push_is_not_the_next_node's_own_"
                  "law"]})
    gate("NT-READ-TIME-COORDINATE", "disclosure",
         "WHICH DATA CARRY THE READ TIME, MEASURED.  T1's datum carries the "
         "checkpoint it was read at, inside the datum, so two T1 data read "
         "at different checkpoints can never compare equal -- the O4 lesson "
         "(RUNBOOK section 15 addendum) built into the type, and the "
         "`readtime-conflate` mutant, which reads every datum at the final "
         "checkpoint, dies against it.  T2's datum is the defect matrix at "
         "the node's own cut and is NOT so tagged: measured here, T2 data "
         "read at different checkpoints DO compare equal, at every setting, "
         "and the pairs are printed.  Nothing in this unit compares data "
         "across coordinates all the same -- the matched table pairs only "
         "paths sharing both endpoints, so every compared pair is read at "
         "one coordinate -- but T2's distinct-value count is a count on "
         "read-time-blind keys and is flagged as one.  T3 is a path "
         "functional and has no read time",
         True,
         {"T2_pairs_of_checkpoints_whose_data_are_equal":
              rt["T2_pairs_of_checkpoints_whose_data_are_equal"],
          "distinct_T2_node_data_without_a_read_time":
              rt["distinct_T2_node_data_without_a_read_time"],
          "distinct_T1_node_data_with_the_read_time":
              rt["distinct_T1_node_data_with_the_read_time"],
          "distinct_T1_node_data_without_the_read_time":
              rt["distinct_T1_node_data_without_the_read_time"]})
    gate("NT-T2-CONJUGATION-SCOPED", "disclosure",
         "WHERE CONJUGATION BY THE WING EXCHANGE MOVES THE COMPOSITION "
         "DEFECT, AND WHERE THAT MATTERS.  Measured at all 24 (setting, "
         "checkpoint) cells of frame F1: conjugation moves the defect at "
         "more cells than the transport can use, and the two conditions are "
         "reported separately -- the defect must be MOVED by the element "
         "AND the element must be an ADMITTED identification there.  Only "
         "where both hold does any path carry the difference, which is why "
         "T2's holonomy is carried by one setting",
         True,
         {"cells_where_conjugation_moves_the_defect":
              sorted(k for k, v in cj.items()
                     if v["conjugation_moves_the_defect"]),
          "cells_where_the_wing_exchange_is_an_admitted_identification":
              sorted(k for k, v in cj.items()
                     if v["the_wing_exchange_is_admitted_here"]),
          "cells_where_both_hold": sorted(k for k, v in cj.items()
                                          if v["both"])})


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
def run_exemption_sweep():
    """RUNBOOK section 14 addendum: NO GATE PREDICATE MAY REFERENCE MUTANT
    IDENTITY.  A gate that special-cases a named mutant exempts its own
    falsifier and tests nothing.  This sweep parses THIS module and counts
    every comparison of the global MUTANT against anything with `!=` -- the
    exemption pattern -- anywhere in the source, gate or not.  The
    `exempt-lax` mutant registers one and must die here."""
    src = Path(__file__).resolve().read_text()
    found = []
    for node in ast.walk(ast.parse(src)):
        if not isinstance(node, ast.Compare):
            continue
        names = [node.left] + list(node.comparators)
        touches = any(isinstance(x, ast.Name) and x.id == "MUTANT"
                      for x in names)
        if touches and any(isinstance(op, ast.NotEq) for op in node.ops):
            found.append(node.lineno)
    if MUTANT == "exempt-lax":
        found.append(0)
    gate("NT-NO-MUTANT-EXEMPTION", "derivation",
         "NO GATE PREDICATE REFERENCES MUTANT IDENTITY (RUNBOOK section 14 "
         "addendum).  An AST sweep of this module counts every `MUTANT != "
         "...` comparison anywhere in the source -- the pattern by which a "
         "gate can exempt its own falsifier -- and the gate measures that "
         "count to be ZERO.  Every mutation in this instrument is injected "
         "where the computation happens, and every declared falsifier dies "
         "by a gate's own predicate evaluated blind.  The `exempt-lax` "
         "mutant registers one such comparison and must die here",
         not found, {"mutant_exemption_comparisons": found,
                     "comparisons_found": len(found)})


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
    ("label-collapse", "computation",
     "the holonomy value set counted as name labels, not permutations"),
    ("exempt-lax", "computation",
     "a mutant-identity exemption registered in a gate predicate"),
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
    comp_hit = {g for r in rows if r["kind"] == "computation"
                for g in r["falsified_gates"]}
    never = sorted(set(must) - hit)
    only_waiver = sorted(set(must) & hit - comp_hit)
    TABLES["mutants"] = rows
    TABLES["gate_falsification"] = {
        "must_pass_gates": must, "falsified_by_some_mutant": sorted(hit),
        "never_falsified": never,
        "falsified_by_a_computation_mutant": sorted(set(must) & comp_hit),
        "falsified_only_by_a_waiver": only_waiver,
        "per_gate_falsifiers": {
            g: {"computation": sorted(r["mutant"] for r in rows
                                      if r["kind"] == "computation"
                                      and g in r["falsified_gates"]),
                "waiver": sorted(r["mutant"] for r in rows
                                 if r["kind"] == "waiver"
                                 and g in r["falsified_gates"])}
            for g in must}}
    gate("NT-FALSIFICATION", "derivation",
         "EVERY MUST-PASS GATE IS FALSIFIED BY SOME MUTANT, AND EVERY MUTANT "
         "DIES.  Each declared mutant is run to completion, must exit 1, and "
         "must falsify at least one NAMED gate or anchor; the second clause "
         "is the one that matters -- the set of must-pass gates that NO "
         "mutant falsifies is measured to be EMPTY.  Each mutant declares "
         "its KIND and the split is counted from the declaration: a WAIVER "
         "proves a gate's predicate is load-bearing for the exit code, not "
         "that the gate would catch a computational defect, and the two are "
         "not claimed to be the same thing.  BOTH DENOMINATORS ARE "
         "REPORTED, because they differ: the count of must-pass gates "
         "falsified by SOME mutant, and the smaller count falsified by a "
         "mutant that perturbs a COMPUTATION.  The gates carried by a "
         "waiver alone are named, not averaged away.  The one gate excluded "
         "from the denominator is this one: `run_mutant_table` does not run "
         "inside a mutant, so the census gate does not exist there and "
         "cannot be falsified by this mechanism at all -- it is a "
         "measurement that can come out otherwise, and did, but not one "
         "this suite can test",
         all(r["died"] for r in rows)
         and all(r["falsified_anchors"] or r["falsified_gates"] for r in rows)
         and not never,
         {"mutants": len(rows), "died": sum(1 for r in rows if r["died"]),
          "perturb_a_computation": sum(1 for r in rows
                                       if r["kind"] == "computation"),
          "waivers": sum(1 for r in rows if r["kind"] == "waiver"),
          "must_pass_gate_denominator": len(must),
          "falsified_by_some_mutant": len(set(must) & hit),
          "falsified_by_a_computation_mutant": len(set(must) & comp_hit),
          "falsified_only_by_a_waiver": only_waiver,
          "the_gate_excluded_from_the_denominator": "NT-FALSIFICATION",
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
    L.append("6A. THE MECHANISM (sufficient, not necessary)")
    L.append("-" * W)
    mech = rec["tables"]["mechanism"]
    L.append("  coordinates where the base admits TWO different maps: %s"
             % (mech["coordinates_of_multiplicity_at_least_two"] or "none"))
    L.append("")
    L.append("  the single-rule sub-connections (multiplicity 1 everywhere)")
    L.append("  %-18s %-6s %-6s %-9s %-7s %s"
             % ("setting / rules", "links", "rank", "closed@F1t0", "group",
                "non-identity closed paths"))
    for k in sorted(mech["single_rule_subconnections"]):
        v = mech["single_rule_subconnections"][k]
        L.append("  %-18s %-6d %-6d %-9d   %-7d %d"
                 % (k, v["links"], v["cycle_rank"],
                    v["closed_paths_at_F1_t0"], v["generated_group_order"],
                    v["non_identity_closed_paths"]))
    L.append("")
    L.append("  does the wing exchange intertwine the leg?")
    for k in sorted(mech["wing_exchange_intertwining_per_leg"]):
        L.append("    %-16s %s"
                 % (k, mech["wing_exchange_intertwining_per_leg"][k]
                    ["wing_exchange_intertwines_the_leg"]))
    L.append("")
    L.append("  P_W U_prep^-1 P_W U_prep, the prep-leg defect element")
    for sp in SETTING_ORDER:
        v = mech["the_prep_leg_defect_element"][sp]
        L.append("    %-8s %-28s identity %s"
                 % (sp, v["name"], v["is_the_identity"]))
    L.append("")
    L.append("  every closed path of the path space, by holonomy class")
    cpc = rec["tables"]["closed_path_census"]
    for sp in SETTING_ORDER:
        c = cpc[sp]
        L.append("    %s  total %d  aligned %d  crossing %d  "
                 "not a signed permutation %d"
                 % (sp, c["all_total"], c["aligned_total"],
                    c["crossing_total"],
                    c["holonomy_not_a_signed_permutation"]))
        for cor in ("aligned", "crossing", "no_two_rules_at_one_coordinate",
                    "based_at_F1_t0"):
            L.append("        %-32s %s" % (cor, canon(c[cor])))
    L.append("")
    L.append("  every minimal loop through a prefix-divergent link")
    for sp in SETTING_ORDER:
        for k in sorted(rec["tables"]["crossing_counter_loops"][sp]):
            v = rec["tables"]["crossing_counter_loops"][sp][k]
            L.append("    %-8s %-38s %-28s declared probe %s"
                     % (sp, k, v["holonomy"], v["is_the_declared_probe"]))
    L.append("")

    L.append("-" * W)
    L.append("6B. THE HOLONOMY GROUP AND THE DECLARED SCOPES")
    L.append("-" * W)
    sg = rec["tables"]["structure_group"]
    L.append("  the wing exchange factorises as (qubit-only).(pointer-only): "
             "%s" % sg["the_wing_exchange_factorises_as_XQ_XP"])
    for k, v in sorted(sg["factor_fixed_points"].items()):
        L.append("      %-28s fixed points %d" % (k, v))
    for sp in SETTING_ORDER:
        L.append("    %s  elements outside every declared scope: %d"
                 % (sp, sg["elements_outside_every_declared_scope"][sp]))
        for nm in sorted(sg["per_setting"][sp]):
            e = sg["per_setting"][sp][nm]
            L.append("        %-28s in72 %-5s in96 %-5s adm %-5s admext %-5s "
                     "fix %-3d ord %-2s mixed-signs %s"
                     % (nm, e["in_the_declared_72"],
                        e["in_the_declared_96_extension"],
                        e["in_the_admitted_2"],
                        e["in_the_admitted_extension_8"],
                        e["fixed_points"], e["order"],
                        e["mixed_relative_signs"]))
    L.append("")
    asc = rec["tables"]["admission_scope"]
    L.append("  the declared 96/8 extension, searched (folded into no "
             "verdict)")
    for c in asc["cells_where_the_scope_changes_admission"]:
        L.append("      %s" % c)
    L.append("      identification links at the extension: %s"
             % canon(asc["identification_links_at_the_declared_extension"]))
    L.append("      the canonical loop exists there: %s"
             % canon(asc["the_canonical_loop_exists_at_the_declared_"
                         "extension"]))
    L.append("")

    L.append("-" * W)
    L.append("7.  THE SECTION 14 GAUGE SELF-TEST (COMPLETE SWEEP)")
    L.append("-" * W)
    for sp in SETTING_ORDER:
        s = rec["tables"]["gauge_selftest"]["group_sizes"][sp]
        L.append("  %-8s switching group order %-6d  swept %-6d complete %-5s"
                 "  checkpoint subgroup %-4d  gauge links %d"
                 % (sp, s["switching_group_order"], s["switchings_swept"],
                    s["sweep_is_complete"],
                    s["checkpoint_subgroup"], s["gauge_links"]))
    for k in sorted(rec["tables"]["gauge_selftest"]["per_loop"]):
        v = rec["tables"]["gauge_selftest"]["per_loop"][k]
        L.append("    %-46s perm parts %d  sign orbits %d (checkpoint %d)  "
                 "relative-sign classes %d"
                 % (k, v["distinct_permutation_parts_under_the_full_group"],
                    v["distinct_sign_orbits_under_the_full_group"],
                    v["distinct_sign_orbits_under_the_checkpoint_subgroup"],
                    v["distinct_relative_sign_classes_under_the_full_group"]))
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
        L.append("       settings where closed-path values differ across "
                 "base points: %s"
                 % (v["settings_where_closed_path_values_differ_across_"
                      "base_points"] or "none"))
    L.append("")
    L.append("  HOLONOMY GROUP (computed): %s"
             % rec["findings"]["holonomy_group"]["description"])
    for k, v in sorted(rec["findings"]["holonomy_group"]["per_setting"].items()):
        L.append("      %-8s value set %d   generated group order %d   "
                 "value set closed %s   value set = group %s"
                 % (k, v["value_set_size"], v["generated_group_order"],
                    v["the_value_set_is_closed_under_composition"],
                    v["the_value_set_is_the_generated_group"]))
        L.append("               values %s" % (v["elements"],))
        L.append("               mixed relative signs %s;  dropped "
                 "(not a signed permutation) %d"
                 % (v["elements_with_mixed_relative_signs"],
                    v["closed_paths_whose_holonomy_is_not_a_signed_"
                      "permutation"]))
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
                 "by a computation mutant %d;  never falsified %s"
                 % (len(gf["must_pass_gates"]),
                    len(gf["falsified_by_some_mutant"]),
                    len(gf["falsified_by_a_computation_mutant"]),
                    gf["never_falsified"] or "EMPTY"))
        L.append("  falsified only by a waiver: %s"
                 % (gf["falsified_only_by_a_waiver"] or "none"))
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

    # -- the gate's own predicates, recomputed HERE from the enumerated
    #    rows and from the graph, so that each one is a property of the
    #    delivered path space rather than a restatement of a constructor
    #    argument.  No predicate below refers to any mutant.
    audit = {}
    for sp in SETTING_ORDER:
        G, rows = graphs[sp], values[sp]
        backtracks = walk_breaks = end_breaks = 0
        for r in rows:
            e = r["edges"]
            for k in range(1, len(e)):
                if e[k][0] == e[k - 1][0]:
                    backtracks += 1
            node = r["start"]
            for (li, d) in e:
                L = G["links"][li]
                tail, head = ((L["a"], L["b"]) if d > 0
                              else (L["b"], L["a"]))
                if node != tail:
                    walk_breaks += 1
                node = head
            if node != r["end"]:
                end_breaks += 1
        # connectivity, by union-find over the enumerated links; the cycle
        # rank is then Euler's WITH the measured component count, so the
        # clause measures that the graph is connected instead of repeating
        # the constructor's assumption that it is.
        parent = {n: n for n in NODES}

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        for L in G["links"]:
            ra, rb = find(L["a"]), find(L["b"])
            if ra != rb:
                parent[ra] = rb
        comps = len({find(n) for n in NODES})
        audit[sp] = {
            "paths_that_traverse_one_link_twice_in_succession": backtracks,
            "steps_that_do_not_follow_the_graph": walk_breaks,
            "paths_whose_walk_does_not_reach_the_declared_end": end_breaks,
            "connected_components": comps,
            "cycle_rank_recomputed_from_the_measured_components":
                ps[sp]["links"] - len(NODES) + comps,
            "nodes_reached_by_the_enumeration":
                len({r["start"] for r in rows} | {r["end"] for r in rows})}
    TABLES["path_space_audit"] = audit
    gate("NT-PATH-SPACE-ENUMERATED", "measurement",
         "THE COMMITTED PATH SPACE IS ENUMERATED, NEVER TYPED, AND THE "
         "DECLARED PROPERTY OF ITS PATHS IS MEASURED ON THE ROWS "
         "THEMSELVES.  Nodes are (frame, checkpoint) coordinates and the "
         "read time is a coordinate of the node; moves are leg applications "
         "in both directions and the admitted identifications; paths are "
         "the REDUCED sequences of moves up to the declared bound, which is "
         "the canonical loop's own length.  Every count in the table is "
         "computed from the enumeration.  FOUR PREDICATES, EACH RECOMPUTED "
         "HERE FROM THE DELIVERED ROWS: (1) the REDUCED condition, read off "
         "the enumerated edge lists -- no enumerated path traverses the "
         "same link twice in immediate succession, which is the declared "
         "condition itself and is what makes the path counts what they are; "
         "(2) every enumerated path is a genuine walk in the graph, step by "
         "step, ending at the node it declares; (3) the graph is CONNECTED, "
         "measured by union-find over the links, and the cycle rank is "
         "Euler's with that measured component count; (4) the enumeration "
         "reaches every declared node and contains closed paths at every "
         "setting.  The `reduce-lax` mutant drops the reduced condition and "
         "must die at predicate (1), which counts its backtracks",
         all(audit[sp]["paths_that_traverse_one_link_twice_in_succession"]
             == 0
             and audit[sp]["steps_that_do_not_follow_the_graph"] == 0
             and audit[sp]["paths_whose_walk_does_not_reach_the_declared_"
                           "end"] == 0
             and audit[sp]["connected_components"] == 1
             and audit[sp]["nodes_reached_by_the_enumeration"] == len(NODES)
             and ps[sp]["cycle_rank"]
             == audit[sp]["cycle_rank_recomputed_from_the_measured_"
                          "components"]
             and ps[sp]["closed_paths"] > 0 for sp in SETTING_ORDER)
         and ps["_total_paths"] > 0,
         {sp: {k: v for k, v in ps[sp].items() if k != "link_detail"}
          for sp in SETTING_ORDER}
         | {"total_paths": ps["_total_paths"],
            "total_path_pairs": ps["_total_pairs"],
            "audit": audit})

    probes = run_probes(graphs)
    run_controls(probes)
    per_object = run_verdicts(graphs, values, pairs, totals, probes, posab)
    run_mechanism(graphs, values, pref, probes)
    run_scopes(pref)
    run_layers()
    run_gauge_selftest(graphs)
    run_flip_tests(graphs, probes)
    hyp = run_hypothesis(pairs, probes, per_object)

    # -- the holonomy group, computed exactly, FROM PERMUTATIONS -----------
    #    The value set is a set of PERMUTATIONS -- matrix content -- and
    #    never a set of name labels: a label set counts as many elements as
    #    the naming table happens to know, which is a count of the wrong
    #    object.  Names are derived from the permutations afterwards, for
    #    printing only.
    hg = {}
    for sp in SETTING_ORDER:
        G = graphs[sp]
        els, signs, perms_seen, dropped = set(), set(), [], 0
        mixed: dict = {}
        for path in values[sp]:
            if path["start"] != ("F1", 0) or path["end"] != ("F1", 0):
                continue
            if not path["len"]:
                continue
            t, rel, nm = holonomy_class_of_interned(path["T3"])
            if t is None:
                dropped += 1
                continue
            els.add(perm_tuple({j: t[j] for j in range(NC)}))
            perms_seen.append(list(t))
            signs.add(rel)
            mixed[nm] = mixed.get(nm, False) or (len(set(rel)) > 1)
        # the value set need not be closed under composition at the declared
        # length bound; whether it IS closed here is MEASURED, and the group
        # it generates is computed separately by closure.
        gen = {tuple(p) for p in perms_seen}
        grp = set(gen) | {tuple(IDPERM)}
        changed = True
        while changed:
            changed = False
            for x in list(grp):
                for y in list(grp):
                    z = perm_compose(x, y)
                    if z not in grp:
                        grp.add(z)
                        changed = True
        closed = all(perm_compose(x, y) in gen for x in gen for y in gen) \
            and bool(gen)
        abelian = all(perm_compose(x, y) == perm_compose(y, x)
                      for x in grp for y in grp)
        exponent2 = all(perm_compose(z, z) == tuple(IDPERM) for z in grp)
        hg[sp] = {"value_set_size": len(els),
                  "elements": sorted(
                      PERM_NAME.get(canon(list(z)), "another permutation")
                      for z in gen),
                  "generated_group_order": len(grp),
                  "the_value_set_is_closed_under_composition": bool(closed),
                  "the_value_set_is_the_generated_group":
                      bool(gen | {tuple(IDPERM)} == grp),
                  "the_group_is_abelian": bool(abelian),
                  "every_element_squares_to_the_identity": bool(exponent2),
                  "distinct_relative_sign_classes_seen": len(signs),
                  "closed_paths_whose_holonomy_is_not_a_signed_permutation":
                      dropped,
                  "mixed_relative_sign_elements": mixed,
                  "elements_with_mixed_relative_signs":
                      sorted(k for k, v in mixed.items() if v),
                  "group_element_permutations": sorted(list(z) for z in grp),
                  "group_elements": sorted(
                      PERM_NAME.get(canon(list(z)), "another permutation")
                      for z in grp)}
    FINDINGS["holonomy_group"] = {
        "per_setting": {sp: {k: v for k, v in hg[sp].items()
                             if k not in ("group_element_permutations",
                                          "mixed_relative_sign_elements")}
                        for sp in SETTING_ORDER},
        "description": "the based closed-loop holonomy group at node F1@t0, "
                       "read as the permutation part of the closed-loop link "
                       "product, enumerated over every closed path of the "
                       "committed path space based there, counted as "
                       "PERMUTATIONS and not as name labels"}
    FINDINGS["per_object"] = per_object
    run_structure_group(hg)

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
        "identification at the two symmetric settings -- the realized-only "
        "rule's WING EXCHANGE, admitted in the discriminator's FORCED sense "
        "and refused by its certificate -- and the bigon it forms with the "
        "full-leg rule's identity, at a PREFIX-ALIGNED checkpoint, carries "
        "a nontrivial closed-loop holonomy of order two, while a loop "
        "CROSSING the prefix-divergent checkpoint by the same rule at both "
        "of its two crossings is measured exactly flat.  Both of the "
        "pre-registered failure modes therefore obtain and the central "
        "hypothesis is REFUTED: the prefix criterion is not the flatness "
        "condition, and prefix alignment governs whether an identification "
        "EXISTS, not whether the identifications that exist AGREE.  Two "
        "sources of the twist are measured and neither is the alignment of "
        "the declared leg prefixes: two admitted rules differing by the "
        "wing exchange at one coordinate -- SUFFICIENT, never necessary -- "
        "and the wing exchange's measured failure to intertwine the "
        "PREPARATION leg at every setting, which already makes the "
        "single-rule sub-connection non-flat at multiplicity one.  The "
        "group the loops generate at the two symmetric settings is the "
        "KLEIN FOUR-GROUP {1, W, X, WX} with W = X . WX, counted as "
        "permutations and measured already closed at the declared length "
        "bound; and TWO OF ITS FOUR ELEMENTS -- the qubit-only and "
        "pointer-only wing swaps -- are measured to lie OUTSIDE the "
        "declared 72-element scope and its declared 96-element extension, "
        "so the connection is NOT PRINCIPAL for the base's own admitted "
        "isomorphisms.  T1's path-dependence is excluded from that "
        "mechanism: its cause is the measured non-inversion of the declared "
        "Born-level step, present at every setting.  The gauge layer is "
        "separated from its orbit by the mandatory switching sweep, swept "
        "COMPLETE at every setting: the switching is MEASURED to act on a "
        "closed loop by a global scalar, from which the invariance of the "
        "permutation part follows by algebra and is reported as a "
        "disclosure rather than as a measurement; the teeth are the "
        "scalar-action, checkpoint-telescoping and signed-permutation "
        "clauses, and the relative sign class, not the raw sign set, is the "
        "invariant sign content.  Stated at the committed finite scope, at "
        "the declared narrow admission scope, per coordinate; nothing is "
        "claimed about nature.")

    run_exemption_sweep()
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
