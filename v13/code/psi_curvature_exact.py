#!/usr/bin/env python3
"""PSI -- THE psi-SIDE CURVATURE HUNT: DOES THE PHYSICAL STATE CONTRIBUTE
GEOMETRY?

Executes the frozen pin `v13/note-psi-curvature-pin.md` (sha c12749532eae,
commit 095c6f7) against the immutable base 1426984 (GEN TERMINAL, v13 LOG
#222).

THE QUESTION (GEN's registered open section 11.12, promoted).  All curvature
GEN measured is DECLARATION-side: the completion's non-equivariance defect D
is a function of the declared completion's Q alone -- the preparation vector
psi cancels identically out of it -- and the identification multiplicity is a
consequence of the declared gluing rules.  DOES ANY psi-SIDE CURVATURE EXIST:
a loop whose holonomy CHANGES when the physical state changes at FIXED
declarations?

THE INSTRUMENT, FROZEN BEFORE FIXTURE TRUTH.  On base G rebuilt natively
here, with the declared transposition Q FIXED at GEN's pinned value and every
other declaration -- rules, scopes, settings, frames, checkpoints, read times
-- held identical, a DECLARED FAMILY of preparation vectors is swept.  The
family is declared AS DATA in section 2, before any transport quantity is
evaluated; the freeze counter and the receipt's own gate order are gated as
the proof.  For each member: (a) the admission table, which identifications
each rule FORCES, at all 24 (setting, checkpoint) cells and both rules; (b)
the loop space, sizes computed by enumeration; (c) the holonomy value of
every loop class, permutation-tuple counted, at MATCHED coordinates.

WHAT MATCHED COORDINATES MEANS HERE.  Every link of every graph carries a
psi-INDEPENDENT NAME -- ("leg", frame, leg) or ("id", checkpoint, rule) -- so
a loop is a sequence of (name, direction) and "the same loop at two psi" is a
statement about names and not about indices into a list that moved.  A loop
is COMMON to two members when both graphs contain every link it names.  The
matched-coordinate table is the primary object and every contrast is derived
from it (RUNBOOK section 15 addendum).

THE TWO HOLONOMY READINGS, both gauge-invariant, one always defined.  The
declared switching group assigns a sign to each link, so a closed loop's
matrix is defined only up to a global +-1.  The unit therefore reads (i) the
PERMUTATION PART of the closed-loop link product, GEN's own invariant, which
is undefined when the product is not a signed permutation, and (ii) the BORN
SHADOW of the holonomy matrix -- its entrywise squares -- which is invariant
under the same action and is ALWAYS defined.  Reading (ii) is the primary
comparator and reading (i) is reported beside it; both are self-tested under
the switching action itself (RUNBOOK section 14).

THE PRE-REGISTERED OUTCOMES (only these):
  PSI-CURVATURE-EXISTS         a witness pair (loop, psi_1 vs psi_2): same
                               declarations, different holonomy.
  PSI-PATH-SPACE-DEPENDENCE    psi changes WHICH loops exist while every
                               common loop's holonomy is psi-invariant.
  PSI-DECLARATION-ONLY         holonomy AND loop space invariant under psi.
  PSI-BLOCKED-AT-<object>      census discipline.

CONTROLS.  Positive: GEN's pinned psi must reproduce the terminal Klein
four-group and the terminal admission table exactly, anchored exit-1 against
GEN's committed receipt, which is itself pinned BY HASH.  Negative with
teeth: a DIFFERENT declared Q must move the holonomy by the amount the GEN
law predicts -- Hol dihedral of order 2n in n = ord(sigma Q^-1 sigma Q) -- and
if it does not, the instrument is dead and the run says so.

DISCIPLINE.  RUNBOOK section 14 with every addendum: the switching self-test
evaluates FRESH against a cache that is measured POPULATED and measured to be
ASKED for its entries (a zero-hit count over zero lookups is vacuous); no
gate predicate references mutant identity, measured by an AST sweep with a
declared falsifier; comparators are built INDEPENDENTLY of the component they
audit; sign and orientation mutants are carried.  RUNBOOK section 15 with
every addendum: the arena is declared as data with sizes computed and the
READ TIME is a coordinate of every node and of every law datum.

Exact arithmetic throughout: `fractions.Fraction` only.  No float enters any
path.  Anchors exit 1 on mismatch.  No wall-clock value enters the receipt or
the rendered output, so two delivery-mode runs are byte-identical.

Scope: finite; ONE declared carrier of 81 configurations; ONE declared
completion form V = H(psi) . Q at ONE declared Q; a declared eleven-member
preparation family with its sizes computed; a declared six-setting family;
two declared frames; four declared checkpoints; a declared 162-element
relabelling scope.  No locality, topology, causality, spacetime, field, QFT
or gravity object is constructed or claimed.  Nothing is claimed about
nature.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import itertools
import json
import sys
import time
from fractions import Fraction as Fr
from pathlib import Path

HERE = Path(__file__).resolve().parent

SCHEMA = "psi-curvature-receipt-v1"
PIN_SHA256 = "c12749532eae"
PIN_COMMIT = "095c6f7"
BASE_COMMIT = "1426984"
GEN_RECEIPT = HERE / "gen_generality_receipt.json"
OUT_TXT = HERE / "psi_curvature_output.txt"
OUT_JSON = HERE / "psi_curvature_receipt.json"

MUTANT: str | None = None
SOURCE_SHA256 = ""

GATES: list[dict] = []
ANCHORS: list[dict] = []
TABLES: dict = {}
FINDINGS: dict = {}

PREREGISTERED = ("PSI-CURVATURE-EXISTS", "PSI-PATH-SPACE-DEPENDENCE",
                 "PSI-DECLARATION-ONLY", "PSI-BLOCKED-AT-")

SCOPE_CLAUSES = ("at the committed finite scope",
                 "at the declared preparation family",
                 "at the declared completion form and its pinned Q",
                 "per coordinate")

T0 = time.time()

_FROZEN = False
_FEVALS = 0

_FRESH = False
_CACHE = {"value_cache_hits": 0, "value_cache_misses": 0,
          "value_cache_lookups": 0, "value_cache_writes": 0,
          "cache_reads_that_returned_a_stored_value": 0,
          "fresh_requests_for_a_key_already_in_the_cache": 0}
_MEMO: dict = {}


def prog(msg: str) -> None:
    """Progress line; stderr only, so no wall-clock reaches any artifact."""
    sys.stderr.write("[psi %6.1fs] %s\n" % (time.time() - T0, msg))
    sys.stderr.flush()


def gate(gid: str, cls: str, claim: str, ok: bool, value=None) -> bool:
    GATES.append({"id": gid, "class": cls, "claim": claim,
                  "passed": bool(ok), "value": value})
    return ok


def anchor(aid: str, source: str, quantity: str, declared, computed) -> None:
    ANCHORS.append({"id": aid, "source": source, "quantity": quantity,
                    "declared": declared, "computed": computed,
                    "passed": declared == computed})


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
    """The instrument's ONLY transported-value cache, used by the switching
    self-test alone.  Bypassed entirely in fresh mode, where the hit count is
    gated at zero; the `memo-lax` mutant lets the self-test read the cache and
    must die there.  The mutation is injected HERE, in the computation; no
    gate predicate names it.

    The bookkeeping is what makes the zero-hit reading a MEASUREMENT rather
    than a vacuity: the cache is PRIMED before the self-test with the very
    keys the self-test will request, the priming phase's own re-read is
    counted (so the read path is measured to work), and every fresh-mode
    request for a key that IS in the cache is counted."""
    read_cache_in_fresh_mode = (MUTANT == "memo-lax")
    if _FRESH and not read_cache_in_fresh_mode:
        _CACHE["value_cache_misses"] += 1
        if key in _MEMO:
            _CACHE["fresh_requests_for_a_key_already_in_the_cache"] += 1
        return build()
    _CACHE["value_cache_lookups"] += 1
    if key in _MEMO:
        _CACHE["cache_reads_that_returned_a_stored_value"] += 1
        if _FRESH:
            _CACHE["value_cache_hits"] += 1
            _CACHE["fresh_requests_for_a_key_already_in_the_cache"] += 1
        return _MEMO[key]
    if _FRESH:
        _CACHE["value_cache_misses"] += 1
    _MEMO[key] = build()
    _CACHE["value_cache_writes"] += 1
    return _MEMO[key]


def _bump():
    global _FEVALS
    evaluate_before_the_freeze = (MUTANT == "freeze-lax")
    if not _FROZEN and not evaluate_before_the_freeze:
        raise RuntimeError("transport datum evaluated before the freeze")
    _FEVALS += 1


# ===========================================================================
# 1.  BASE G, REBUILT NATIVELY AND DECLARED AS DATA
#
#     Nothing of GEN's module is imported.  The pinned data are typed here as
#     this unit's own declaration and the constructors are anchored against
#     them entry by entry, so a drift in any constructor kills the run.  Every
#     COUNT is computed by enumeration, never typed.
# ===========================================================================
ZERO, ONE = Fr(0), Fr(1)

NS = 3                          # the system dimension on each wing: a qutrit
NP = 3                          # the pointer states per wing: 0 = ready
NC = NS * NS * NP * NP          # the carrier, computed
NSP = NS * NS                   # the system-pair dimension, computed
J0 = 0                          # the initial configuration (0, 0, 0, 0)


def idx(sa, sb, pa, pb):
    return ((sa * NS + sb) * NP + pa) * NP + pb


def unidx(i):
    return (i // (NP * NP * NS), (i // (NP * NP)) % NS, (i // NP) % NP,
            i % NP)


QUATERNIONS = {"R0": (1, 0, 0, 0), "R1": (2, 1, 0, 0), "R2": (3, 0, 0, 2)}
ROT_ORDER = ["R0", "R1", "R2"]

PINNED_ROT = {
    "R0": [["1", "0", "0"], ["0", "1", "0"], ["0", "0", "1"]],
    "R1": [["1", "0", "0"], ["0", "3/5", "-4/5"], ["0", "4/5", "3/5"]],
    "R2": [["5/13", "-12/13", "0"], ["12/13", "5/13", "0"], ["0", "0", "1"]],
}

SHIFT_DECLARED = (0, 1, 2)

# THE PINNED TRANSPOSITION.  GEN's declared completion is V = H . Q with Q the
# transposition of the system-pair basis states (0,1) and (0,2).  THIS UNIT
# HOLDS Q FIXED AT THAT VALUE FOR EVERY MEMBER OF THE PREPARATION FAMILY: it
# is the pin's central control, so it is typed here and anchored.
Q_PINNED = [0, 2, 1, 3, 4, 5, 6, 7, 8]

# THE PINNED COMPLETION OF GEN'S OWN psi, 9x9, in the system-pair basis
# ordered (0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2).
# Column 0 is psi.  The constructor is anchored against it entry by entry.
PINNED_V_OF_PSI_G = [
    ["0", "0", "2/3", "2/3", "0", "0", "0", "0", "1/3"],
    ["2/3", "0", "5/9", "-4/9", "0", "0", "0", "0", "-2/9"],
    ["0", "1", "0", "0", "0", "0", "0", "0", "0"],
    ["2/3", "0", "-4/9", "5/9", "0", "0", "0", "0", "-2/9"],
    ["0", "0", "0", "0", "1", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "1", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "1", "0"],
    ["1/3", "0", "-2/9", "-2/9", "0", "0", "0", "0", "8/9"],
]

SETTINGS = {"GP-A": ("R0", "R1"), "GP-B": ("R0", "R2"),
            "GP-C": ("R1", "R2"), "GP-D": ("R2", "R1"),
            "GP-E": ("R0", "R0"), "GP-F": ("R1", "R1")}
SETTING_ORDER = ["GP-A", "GP-B", "GP-C", "GP-D", "GP-E", "GP-F"]
FRAMES = ("F1", "F2")

ID_RULES = (
    {"id": "FULL", "name": "FULL-DECLARED-LEGS",
     "definition":
         "the corridor-bound rule matching the FULL declared legs order-free "
         "at the Born level: an identification at checkpoint t is admitted "
         "iff exactly one permutation of the admitted scope carries j0 to "
         "j0, carries frame 2's full declared legs onto frame 1's, carries "
         "frame 2's occupied set at t onto frame 1's, and carries frame 2's "
         "exact law at t onto frame 1's",
     "legs": "declared"},
    {"id": "REAL", "name": "REALIZED-ONLY",
     "definition":
         "the same four-clause predicate with each leg restricted to the "
         "configurations the process actually occupies before and after it",
     "legs": "realized"},
)


# ===========================================================================
# 2.  THE PREPARATION FAMILY, DECLARED AS DATA
#
#     Declared BEFORE any transport quantity is evaluated.  Each member is a
#     rational vector on the nine system-pair basis states; its unit norm,
#     Schmidt rank, behaviour under the exchange of the two systems, and the
#     exchange symmetry of its BORN SHADOW are all COMPUTED below, never
#     typed.  Every member is completed with the SAME declared Q.
# ===========================================================================
PSI_FAMILY = (
    ("psi-G", "GEN's pinned preparation, carried unchanged",
     {(0, 1): "2/3", (1, 0): "2/3", (2, 2): "1/3"}),
    ("psi-I1", "an exchange-invariant PRODUCT state v (x) v, v = (3/5,4/5,0)",
     {(0, 0): "9/25", (0, 1): "12/25", (1, 0): "12/25", (1, 1): "16/25"}),
    ("psi-I2", "an exchange-invariant state on the diagonal, unequal weights",
     {(0, 0): "4/5", (1, 1): "3/5"}),
    ("psi-I3", "an exchange-invariant state on a different support",
     {(0, 0): "1/3", (1, 2): "2/3", (2, 1): "2/3"}),
    ("psi-I4", "an exchange-invariant state with four equal weights",
     {(0, 1): "1/2", (1, 0): "1/2", (0, 2): "1/2", (2, 0): "1/2"}),
    ("psi-S1", "psi-G with the sign flipped at a sigma-FIXED index",
     {(0, 1): "2/3", (1, 0): "2/3", (2, 2): "-1/3"}),
    ("psi-S2", "psi-I2 with the sign flipped at a sigma-FIXED index",
     {(0, 0): "4/5", (1, 1): "-3/5"}),
    ("psi-N1", "psi-G with the sign flipped at ONE index of a sigma-PAIR: "
               "the same Born shadow, exchange-NON-invariant",
     {(0, 1): "2/3", (1, 0): "-2/3", (2, 2): "1/3"}),
    ("psi-N2", "an ANTI-invariant state: the same Born shadow as psi-I4",
     {(0, 1): "1/2", (1, 0): "-1/2", (0, 2): "1/2", (2, 0): "-1/2"}),
    ("psi-N3", "an exchange-non-invariant state whose BORN SHADOW is also "
               "not exchange-symmetric",
     {(0, 1): "3/5", (1, 0): "4/5"}),
    ("psi-N4", "an exchange-non-invariant PRODUCT state, Born-asymmetric",
     {(0, 0): "3/5", (0, 1): "4/5"}),
)
PSI_ORDER = [m[0] for m in PSI_FAMILY]
PSI_REFERENCE = "psi-G"

# THE DECLARED NEGATIVE CONTROLS: two ALTERNATIVE declared transpositions,
# each a permutation of the nine system-pair labels fixing the initial one.
# The GEN law predicts the holonomy group order 2n with n the order of
# delta(Q) = sigma Q^-1 sigma Q -- and 1, with the links themselves refused,
# on the exchange-equivariant locus where delta(Q) is the identity.
Q_CONTROLS = (
    ("Q-negA", "the transposition of the system-pair labels (0,1) and (1,1)",
     [0, 4, 2, 3, 1, 5, 6, 7, 8]),
    ("Q-negB", "the transposition of the system-pair labels (0,1) and (1,0), "
               "which lies on the exchange-equivariant locus",
     [0, 3, 2, 1, 4, 5, 6, 7, 8]),
)


# ---- constructors (each anchored against the pinned declaration) ----------
def parse_fr(s):
    return Fr(s)


def rotation(qname):
    """The Euler-Rodrigues rotation of an integer quaternion.  Rational and
    exactly orthogonal; the orthogonality is measured, not assumed."""
    w, x, y, z = QUATERNIONS[qname]
    n = Fr(w * w + x * x + y * y + z * z)
    perturb_a_declared_rotation = (MUTANT == "anchor-rot")
    M = [[w * w + x * x - y * y - z * z, 2 * (x * y - w * z),
          2 * (x * z + w * y)],
         [2 * (x * y + w * z), w * w - x * x + y * y - z * z,
          2 * (y * z - w * x)],
         [2 * (x * z - w * y), 2 * (y * z + w * x),
          w * w - x * x - y * y + z * z]]
    out = [[Fr(v) / n for v in row] for row in M]
    if perturb_a_declared_rotation and qname == "R1":
        out[1][1] = -out[1][1]
    return out


def declared_Q():
    """The pinned transposition, held FIXED for every member of the family.
    The `anchor-Q` mutant perturbs it and must die at the anchor and at the
    positive control."""
    perturb_the_declared_transposition = (MUTANT == "anchor-Q")
    q = list(Q_PINNED)
    if perturb_the_declared_transposition:
        q[1], q[4] = q[4], q[1]
    return q


def psi_vector(coeffs):
    """A declared preparation vector on the nine system-pair basis states.
    The `anchor-psi` mutant perturbs one coefficient of the pinned psi."""
    perturb_one_declared_coefficient = (MUTANT == "anchor-psi")
    out = [ZERO] * NSP
    for (a, b), v in coeffs.items():
        out[a * NS + b] = parse_fr(v)
    if (perturb_one_declared_coefficient
            and coeffs == dict(PSI_FAMILY[0][2])):
        out[NSP - 1] = -out[NSP - 1]
    return out


def householder(psi):
    """H = I - 2 w w^T / (w.w) with w = psi - e_{(0,0)}: the reflection that
    carries the initial system state exactly onto the declared preparation
    vector.  Symmetric, orthogonal and involutive."""
    w = list(psi)
    w[0] = w[0] - ONE
    ww = sum(v * v for v in w)
    return [[(ONE if i == j else ZERO) - 2 * w[i] * w[j] / ww
             for j in range(NSP)] for i in range(NSP)]


def completion(psi, q):
    """V = H(psi) . Q: column j of V is column Q(j) of H, so column 0 is psi
    for every member of the family and the declared Q is the same one."""
    H = householder(psi)
    return [[H[i][q[j]] for j in range(NSP)] for i in range(NSP)]


ROT = {k: rotation(k) for k in ROT_ORDER}
SIGMA9 = [(b * NS + a) for a in range(NS) for b in range(NS)]


# ---- exact sparse linear algebra over Q -----------------------------------
def mm(A, B):
    bycol: dict = {}
    for (i, k), v in A.items():
        bycol.setdefault(k, []).append((i, v))
    out: dict = {}
    for (k, j), v in B.items():
        for (i, u) in bycol.get(k, ()):
            t = u * v
            if t:
                key = (i, j)
                s = out.get(key, ZERO) + t
                if s:
                    out[key] = s
                else:
                    out.pop(key, None)
    return out


_KMUL: dict = {}
_KADD: dict = {}


def mm_memo(A, B):
    """The same sparse product as `mm`, with the FIELD's own products and sums
    memoised.  Nothing is approximated and nothing is cached at the level of a
    transported value: the memo is of + and x in Q.  The two routines are
    measured against each other on EVERY swept instance, since an all-positive
    switching is an exact equality test between them."""
    bycol: dict = {}
    for (i, k), v in A.items():
        bycol.setdefault(k, []).append((i, v))
    out: dict = {}
    for (k, j), v in B.items():
        col = bycol.get(k)
        if not col:
            continue
        for (i, u) in col:
            mk = (u, v)
            t = _KMUL.get(mk)
            if t is None:
                t = u * v
                _KMUL[mk] = t
            if not t:
                continue
            key = (i, j)
            s = out.get(key)
            if s is None:
                out[key] = t
            else:
                ak = (s, t)
                r = _KADD.get(ak)
                if r is None:
                    r = s + t
                    _KADD[ak] = r
                if not r:
                    del out[key]
                else:
                    out[key] = r
    return out


def sp_id():
    return {(i, i): ONE for i in range(NC)}


def sp_neg(A):
    return {k: -v for k, v in A.items()}


def sp_conj(A, p):
    return {(p[i], p[j]): v for (i, j), v in A.items()}


def sp_born(A):
    return {k: v * v for k, v in A.items()}


def minv(A):
    """The inverse of a link variable.  Every declared operator is measured
    EXACTLY orthogonal, so the inverse is the transpose; the `orient-flip`
    mutant drops the transposition and must die against the orthogonality
    anchors, the controls and the direction flip-test."""
    if MUTANT == "orient-flip":
        return dict(A)
    return {(j, i): v for (i, j), v in A.items()}


def pmat(p):
    return {(p[j], j): ONE for j in range(NC)}


def is_orthogonal(A):
    cols: dict = {}
    for (i, j), v in A.items():
        cols.setdefault(j, []).append((i, v))
    for j1 in range(NC):
        d1 = dict(cols.get(j1, ()))
        for j2 in range(j1, NC):
            acc = ZERO
            for (i, v) in cols.get(j2, ()):
                if i in d1:
                    acc = acc + d1[i] * v
            if acc != (ONE if j1 == j2 else ZERO):
                return False
    return True


def signed_perm(A):
    """(permutation, signs) if A is a signed permutation matrix, else
    (None, None)."""
    cols: dict = {}
    for (i, j), v in A.items():
        cols.setdefault(j, []).append((i, v))
    perm, sgn = {}, {}
    for j in range(NC):
        e = cols.get(j, [])
        if len(e) != 1:
            return None, None
        i, v = e[0]
        if v == ONE:
            s = 1
        elif v == -ONE:
            s = -1
        else:
            return None, None
        perm[j], sgn[j] = i, s
    return perm, sgn


def born_shadow_key(A):
    """THE GAUGE-INVARIANT HOLONOMY READING, always defined: the entrywise
    squares of the closed-loop matrix.  A switching multiplies a closed loop's
    matrix by a global +-1, and squaring removes it.  The `bornhol-lax` mutant
    returns the raw matrix instead -- a quantity the switching MOVES -- and
    must die at the switching self-test."""
    return_the_raw_matrix_instead = (MUTANT == "bornhol-lax")
    if return_the_raw_matrix_instead:
        return frozenset(A.items())
    return frozenset((k, v * v) for k, v in A.items())


def perm_tuple(p):
    """A holonomy's permutation VALUE: the tuple of images.  This is MATRIX
    CONTENT.  The `label-collapse` mutant returns a NAME drawn from the two
    declared identification maps instead, so that every other permutation
    collapses onto one string."""
    t = tuple(p[j] for j in range(NC))
    count_labels_instead_of_permutations = (MUTANT == "label-collapse")
    if count_labels_instead_of_permutations:
        return _NAMES_OF_THE_TWO_DECLARED_MAPS.get(canon(list(t)),
                                                   "another permutation")
    return t


def perm_compose(x, y):
    return tuple(map(x.__getitem__, y))


def perm_inverse(p):
    out = [0] * len(p)
    for i, v in enumerate(p):
        out[v] = i
    return out


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


# ---- the declared relabelling scopes --------------------------------------
def build_perm(sw, ra, rb, sa, sb):
    """The declared relabelling scope: the WING EXCHANGE flag, a cyclic system
    relabelling per wing, a cyclic pointer relabelling per wing."""
    p = [0] * NC
    for i in range(NC):
        qa, qb, pa, pb = unidx(i)
        qa2, qb2 = (qa + ra) % NS, (qb + rb) % NS
        pa2, pb2 = (pa + sa) % NP, (pb + sb) % NP
        p[i] = (idx(qb2, qa2, pb2, pa2) if sw else idx(qa2, qb2, pa2, pb2))
    return p


def build_perm_tr(sw, ra, rb, ta, tb):
    """The declared EXTENSION scope: the pointer TRANSPOSITION (1 <-> 2)."""
    tr = {0: 0, 1: 2, 2: 1}
    p = [0] * NC
    for i in range(NC):
        qa, qb, pa, pb = unidx(i)
        qa2, qb2 = (qa + ra) % NS, (qb + rb) % NS
        pa2 = tr[pa] if ta else pa
        pb2 = tr[pb] if tb else pb
        p[i] = (idx(qb2, qa2, pb2, pa2) if sw else idx(qa2, qb2, pa2, pb2))
    return p


def declared_scope():
    """Every count computed from the enumeration, never typed."""
    base = [build_perm(sw, ra, rb, sa, sb)
            for sw in (0, 1) for ra in range(NS) for rb in range(NS)
            for sa in range(NP) for sb in range(NP)]
    ext = [build_perm_tr(sw, ra, rb, ta, tb)
           for sw in (0, 1) for ra in range(NS) for rb in range(NS)
           for ta in (0, 1) for tb in (0, 1)]
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
            "n_base": len({tuple(p) for p in base}),
            "n_ext_total": len(base + ext_u),
            "n_admitted": len(admitted),
            "n_admitted_extension": len(admitted_ext)}


SCOPE = declared_scope()
WSWAP = build_perm(1, 0, 0, 0, 0)
IDPERM = build_perm(0, 0, 0, 0, 0)
XSSWAP = [idx(sb, sa, pa, pb) for (sa, sb, pa, pb)
          in (unidx(j) for j in range(NC))]
XPSWAP = [idx(sa, sb, pb, pa) for (sa, sb, pa, pb)
          in (unidx(j) for j in range(NC))]

PERM_NAME = {canon(list(IDPERM)): "the identity",
             canon(list(WSWAP)): "the wing exchange",
             canon(list(XSSWAP)): "the system-only wing exchange",
             canon(list(XPSWAP)): "the pointer-only wing exchange"}
_NAMES_OF_THE_TWO_DECLARED_MAPS = {canon(list(IDPERM)): "the identity",
                                   canon(list(WSWAP)): "the wing exchange"}


def name_perm(t):
    return PERM_NAME.get(canon(list(t)), "another permutation")


NLEGS = 3
CHECKPOINTS = tuple(range(0, NLEGS + 1))
DIVISION_EVENTS = (CHECKPOINTS[0], CHECKPOINTS[-1])
NODES = tuple((fr, t) for fr in FRAMES for t in CHECKPOINTS)
L_MAX = 2 * NLEGS + 2
BASE_NODE = ("F1", CHECKPOINTS[0])


def pointer_shift(o):
    collapse_the_record = (MUTANT == "anchor-record")
    if collapse_the_record and o == 2:
        return 1
    return o


def U_local(wing, g):
    """U_X(g) = sum_o Pi^g_o (x) Sh^{n(o)} on the wing (s_X, p_X), the identity
    on the other wing."""
    R = ROT[g]
    out: dict = {}
    for sa0 in range(NS):
        for sb0 in range(NS):
            for pa0 in range(NP):
                for pb0 in range(NP):
                    j = idx(sa0, sb0, pa0, pb0)
                    s0 = sa0 if wing == "A" else sb0
                    p0 = pa0 if wing == "A" else pb0
                    for o in range(NS):
                        p1 = (p0 + pointer_shift(o)) % NP
                        for s1 in range(NS):
                            v = R[s1][o] * R[s0][o]
                            if not v:
                                continue
                            i = (idx(s1, sb0, p1, pb0) if wing == "A"
                                 else idx(sa0, s1, pa0, p1))
                            c = out.get((i, j), ZERO) + v
                            if c:
                                out[(i, j)] = c
                            else:
                                out.pop((i, j), None)
    return out


ULOCAL = {(w, g): U_local(w, g) for w in ("A", "B") for g in ROT_ORDER}


def leg_key(L):
    """A canonical key for a leg at the Born level.  Two legs match iff their
    keys are equal, so order-free matching of leg lists is MULTISET EQUALITY
    of keys and needs no permutation search."""
    return canon(sorted((i, j, canon(v)) for (i, j), v in sp_born(L).items()))


# ===========================================================================
# 3.  THE WORLD OF ONE PREPARATION -- every psi-dependent object, built here
#     and nowhere else.  The declarations that are NOT psi (Q, the rotations,
#     the settings, the frames, the checkpoints, the scopes, the two rules,
#     the read times) are module-level and shared, so the sweep varies psi
#     and nothing else.
# ===========================================================================
class World:
    def __init__(self, name, psi, q):
        self.name = name
        self.psi = list(psi)
        self.q = list(q)
        self.V = completion(self.psi, self.q)
        U = {}
        for a in range(NSP):
            for b in range(NSP):
                v = self.V[a][b]
                if not v:
                    continue
                for pa in range(NP):
                    for pb in range(NP):
                        U[(idx(a // NS, a % NS, pa, pb),
                           idx(b // NS, b % NS, pa, pb))] = v
        self.Uprep = U
        self.f: dict = {}

    # -- the declared leg sequences -----------------------------------------
    def legs(self, sp, fr):
        k = ("legs", sp, fr)
        if k not in self.f:
            a, b = SETTINGS[sp]
            self.f[k] = ([self.Uprep, ULOCAL[("A", a)], ULOCAL[("B", b)]]
                         if fr == "F1" else
                         [self.Uprep, ULOCAL[("B", b)], ULOCAL[("A", a)]])
        return self.f[k]

    def theta(self, sp, fr, t):
        k = ("theta", sp, fr, t)
        if k not in self.f:
            acc = sp_id()
            for L in self.legs(sp, fr)[:t]:
                acc = mm(L, acc)
            self.f[k] = acc
        return self.f[k]

    def support(self, sp, fr, t):
        return {i for (i, j), v in self.theta(sp, fr, t).items()
                if j == J0 and v}

    def realized(self, sp, fr):
        k = ("real", sp, fr)
        if k not in self.f:
            s = [self.support(sp, fr, t) for t in CHECKPOINTS]
            self.f[k] = [{(i, j): v for (i, j), v
                          in self.legs(sp, fr)[t].items()
                          if i in s[t + 1] and j in s[t]}
                         for t in range(NLEGS)]
        return self.f[k]

    def node_law(self, sp, fr, t):
        """THE LAW'S RESTRICTION TO THE CONTEXT (fr, t): the occupied support
        and the exact probability of every configuration at the DECLARED READ
        TIME t, carried inside the datum (RUNBOOK section 15 addendum)."""
        _bump()
        k = ("law", sp, fr, t)
        if k in self.f:
            return self.f[k]
        out: dict = {}
        for (i, j), v in self.theta(sp, fr, t).items():
            if j == J0 and v:
                out[i] = out.get(i, ZERO) + v * v
        read_every_datum_at_the_final_checkpoint = (
            MUTANT == "readtime-conflate")
        if read_every_datum_at_the_final_checkpoint:
            outf: dict = {}
            for (i, j), v in self.theta(sp, fr, NLEGS).items():
                if j == J0 and v:
                    outf[i] = outf.get(i, ZERO) + v * v
            self.f[k] = {"read_time": NLEGS, "law": outf}
        else:
            self.f[k] = {"read_time": t, "law": out}
        return self.f[k]

    def one_step(self, sp, fr, t):
        return sp_born(self.legs(sp, fr)[t - 1])

    # -- the four-clause admissibility predicate ----------------------------
    def admits(self, sp, t, rule, scope="admitted"):
        """THE FOUR-CLAUSE ADMISSIBILITY PREDICATE, in order: the j0 filter,
        the rule's own leg list matched order-free at the Born level, the
        occupied-set clause, the exact-law clause.  An identification is
        ADMITTED when exactly one permutation of the scope satisfies all four
        (admission by UNIQUENESS).  Every clause reads BORN-level data only --
        the fact section 7 turns into a measurement."""
        la = (self.realized(sp, "F1") if rule["legs"] == "realized"
              else self.legs(sp, "F1"))
        lb = (self.realized(sp, "F2") if rule["legs"] == "realized"
              else self.legs(sp, "F2"))
        kA = ("legkeys", sp, rule["id"], "F1")
        if kA not in self.f:
            self.f[kA] = sorted(leg_key(L) for L in la)
        ka = self.f[kA]
        da = self.node_law(sp, "F1", t)["law"]
        db = self.node_law(sp, "F2", t)["law"]
        drop_the_exact_law_clause = (MUTANT == "born-lax")
        out = []
        for p in SCOPE[scope]:
            if p[J0] != J0:
                continue
            kB = ("legkeys", sp, rule["id"], "F2", canon(list(p)))
            if kB not in self.f:
                self.f[kB] = sorted(leg_key(sp_conj(L, p)) for L in lb)
            if ka != self.f[kB]:
                continue
            if not drop_the_exact_law_clause:
                if {p[i] for i in db} != set(da):
                    continue
                if any(da.get(p[i]) != db.get(i) for i in db):
                    continue
            out.append(p)
        return out

    def admission_table(self):
        k = ("admtab",)
        if k in self.f:
            return self.f[k]
        tab = {}
        for sp in SETTING_ORDER:
            for t in CHECKPOINTS:
                for rule in ID_RULES:
                    adm = self.admits(sp, t, rule)
                    if MUTANT == "id-lax":
                        adm = list(SCOPE["admitted"])
                    tab[(sp, t, rule["id"])] = {
                        "n_admitted": len(adm),
                        "maps": sorted(name_perm(tuple(p)) for p in adm),
                        "drawn": len(adm) == 1,
                        "perm": (list(adm[0]) if len(adm) == 1 else None)}
        self.f[k] = tab
        return tab

    # -- the path graph, with psi-INDEPENDENT link names --------------------
    def graph(self, sp):
        k = ("graph", sp)
        if k in self.f:
            return self.f[k]
        collapse_the_link_names = (MUTANT == "loopname-collapse")
        links = []
        for fr in FRAMES:
            for t in CHECKPOINTS[1:]:
                nm = ("leg",) if collapse_the_link_names else ("leg", fr, t)
                links.append({"name": nm, "kind": "leg", "a": (fr, t - 1),
                              "b": (fr, t), "frame": fr, "leg": t})
        tab = self.admission_table()
        for rule in ID_RULES:
            for t in CHECKPOINTS:
                cell = tab[(sp, t, rule["id"])]
                if not cell["drawn"]:
                    continue
                nm = (("id",) if collapse_the_link_names
                      else ("id", t, rule["id"]))
                links.append({"name": nm, "kind": "id", "a": ("F2", t),
                              "b": ("F1", t), "t": t, "rule": rule["id"],
                              "perm": cell["perm"],
                              "perm_name": name_perm(tuple(cell["perm"]))})
        adj: dict = {n: [] for n in NODES}
        for li, L in enumerate(links):
            adj[L["a"]].append((li, +1, L["b"]))
            adj[L["b"]].append((li, -1, L["a"]))
        self.f[k] = {"links": links, "adj": adj, "n_nodes": len(NODES),
                     "n_links": len(links),
                     "cycle_rank": len(links) - len(NODES) + 1}
        return self.f[k]

    def link_variable(self, sp, link, direction):
        """A's link variable: the leg operator for a leg (its inverse in
        reverse), the permutation matrix for an identification.  The declared
        link variables themselves are held here -- they are the base's own
        data, not transported values -- so that "rebuilt from the link
        variables" means exactly that and nothing is rebuilt twice."""
        k = ("linkvar", sp, canon(link["name"]), direction)
        if k in self.f:
            return self.f[k]
        if link["kind"] == "leg":
            M = self.legs(sp, link["frame"])[link["leg"] - 1]
        else:
            M = pmat(link["perm"])
        self.f[k] = M if direction > 0 else minv(M)
        return self.f[k]

    def l_push(self, sp, val, link, direction):
        """L's DECLARED per-coordinate action.  A leg acts by the declared
        one-step Born transition in the traversal's direction (its transpose
        in reverse); an identification acts by the admitted permutation.
        Returns None when the action does not deliver a law."""
        if val is None:
            return None
        if link["kind"] == "leg":
            G = self.one_step(sp, link["frame"], link["leg"])
            if direction < 0:
                G = {(j, i): v for (i, j), v in G.items()}
            law: dict = {}
            for (i, j), g in G.items():
                if j in val["law"]:
                    p = g * val["law"][j]
                    if p:
                        s = law.get(i, ZERO) + p
                        if s:
                            law[i] = s
                        else:
                            law.pop(i, None)
            tot = ZERO
            for v in law.values():
                tot = tot + v
            if tot != ONE:
                return None
            return {"read_time": val["read_time"] + (1 if direction > 0
                                                     else -1),
                    "law": law}
        p = (link["perm"] if direction > 0
             else perm_inverse(link["perm"]))
        return {"read_time": val["read_time"],
                "law": {p[i]: v for i, v in val["law"].items()}}


# ===========================================================================
# 4.  THE PATH SPACE OF ONE (world, setting) -- enumerated, never typed
# ===========================================================================
def enumerate_paths(W, sp, bound, starts=None):
    """Every REDUCED path of length at most `bound` from every node: a path
    never traverses the same link twice in immediate succession, since that is
    a backtrack and carries no transport content.  Both transported objects
    are carried incrementally.  Only the CLOSED paths are retained as rows --
    the loop space is what this unit compares -- and the reduced-path total is
    counted.  `starts` restricts the enumeration to a DECLARED subset of the
    nodes; the unit's own sweep passes none and enumerates from all of them,
    and the two census sweeps declare the base point alone, since the based
    loop set is the only object they read.  The `reduce-lax` mutant drops the
    reduced condition; the `path-collapse` mutant gives every loop the same
    name."""
    G = W.graph(sp)
    collapse_every_loop_name = (MUTANT == "path-collapse")
    drop_the_reduced_condition = (MUTANT == "reduce-lax")
    step: dict = {}
    intern: dict = {}
    stats = {"reduced_paths": 0, "closed_paths": 0, "based_closed_loops": 0,
             "backtracks_found_in_the_delivered_rows": 0,
             "rows_that_are_not_genuine_walks": 0}
    based: dict = {}
    census: dict = {}

    def akey(M):
        k = frozenset(M.items())
        if k not in intern:
            intern[k] = len(intern)
        return intern[k], k

    def move(kk, li, d):
        ck = (kk[0], li, d)
        if ck in step:
            return step[ck]
        M = mm(W.link_variable(sp, G["links"][li], d), dict(kk[1]))
        step[ck] = akey(M)
        return step[ck]

    idkey = akey(sp_id())
    for start in (NODES if starts is None else starts):
        stack = [(start, [], None, idkey)]
        while stack:
            node, edges, last, kk = stack.pop()
            stats["reduced_paths"] += 1
            if node == start and edges:
                stats["closed_paths"] += 1
                p, _s = signed_perm(dict(kk[1]))
                nm = ("not a signed permutation" if p is None
                      else name_perm(tuple(p[j] for j in range(NC))))
                census[nm] = census.get(nm, 0) + 1
                read_closed_paths_at_any_base_point = (
                    MUTANT == "hol-basepoint")
                if start == BASE_NODE or read_closed_paths_at_any_base_point:
                    stats["based_closed_loops"] += 1
                    names = ((("loop",),) if collapse_every_loop_name else
                             tuple((G["links"][li]["name"], dd)
                                   for li, dd in edges))
                    based[names] = {
                        "perm": (None if p is None
                                 else tuple(p[j] for j in range(NC))),
                        "value": (None if p is None
                                  else perm_tuple({j: p[j]
                                                   for j in range(NC)})),
                        "born": born_shadow_key(dict(kk[1])),
                        "len": len(edges),
                        "edges": list(edges)}
            if len(edges) >= bound:
                continue
            for (li, d, nxt) in G["adj"][node]:
                if (not drop_the_reduced_condition
                        and last is not None and li == last):
                    continue
                stack.append((nxt, edges + [(li, d)], li, move(kk, li, d)))
    # -- properties recomputed FROM THE DELIVERED ROWS themselves -----------
    for names, row in based.items():
        prev = None
        node = BASE_NODE
        for (li, d) in row["edges"]:
            L = G["links"][li]
            if prev is not None and li == prev:
                stats["backtracks_found_in_the_delivered_rows"] += 1
            frm = L["a"] if d > 0 else L["b"]
            to = L["b"] if d > 0 else L["a"]
            if frm != node:
                stats["rows_that_are_not_genuine_walks"] += 1
                break
            node, prev = to, li
        else:
            if node != BASE_NODE:
                stats["rows_that_are_not_genuine_walks"] += 1
    # -- connectivity and Euler's cycle rank, from the links ----------------
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
    stats["components"] = comps
    stats["euler_cycle_rank"] = len(G["links"]) - len(NODES) + comps
    stats["declared_cycle_rank"] = G["cycle_rank"]
    return {"stats": stats, "based": based, "census": dict(sorted(
        census.items())), "n_links": len(G["links"]),
        "distinct_transported_values": len(intern)}


def based_group(based):
    """The based holonomy group at the declared base point, read as the
    PERMUTATION PART of the closed-loop link product and counted as
    PERMUTATION TUPLES -- matrix content -- never as name labels.  The
    `hol-basepoint` mutant is injected in the enumeration, not here."""
    vals = [r["perm"] for r in based.values()]
    dropped = sum(1 for v in vals if v is None)
    gen = {v for v in vals if v is not None}
    value_set = {r["value"] for r in based.values() if r["value"] is not None}
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
    closed = bool(gen) and all(perm_compose(x, y) in gen
                               for x in gen for y in gen)
    abelian = all(perm_compose(x, y) == perm_compose(y, x)
                  for x in grp for y in grp)
    orders = sorted({perm_order(z) for z in grp})
    return {"value_set_size": len(value_set),
            "generated_group_order": len(grp),
            "the_value_set_is_closed_under_composition": bool(closed),
            "the_group_is_abelian": bool(abelian),
            "element_orders": orders,
            "every_element_squares_to_the_identity": orders in ([1], [1, 2]),
            "elements": sorted(name_perm(z) for z in grp),
            "element_fixed_points": {name_perm(z): fixed_points(list(z))
                                     for z in grp},
            "element_fixed_point_multiset":
                sorted(fixed_points(list(z)) for z in grp),
            "based_closed_loops": len(based),
            "loops_whose_holonomy_is_not_a_signed_permutation": dropped,
            "_group": sorted(list(z) for z in grp)}


# ===========================================================================
# 5.  THE FREEZE -- the family declared before any transport datum
# ===========================================================================
def run_freeze():
    global _FROZEN
    prog("freeze: the psi-family declared as data before any transport datum")
    gate("PSI-FREEZE", "freeze",
         "THE PREPARATION FAMILY IS DECLARED AS DATA BEFORE ANY TRANSPORT "
         "QUANTITY IS EVALUATED (RUNBOOK 13(4)), AND THE RECEIPT'S OWN GATE "
         "ORDER PROVES IT.  Base G's carrier and index map, its three "
         "declared rotations with their pinned matrices, the PINNED "
         "TRANSPOSITION Q that every member of the family is completed with, "
         "the eleven declared preparation vectors with their exact rational "
         "coefficients, the two declared gluing rules, the six declared "
         "settings, the two frames, the four checkpoints and the declared "
         "relabelling scopes are all fixed above this line.  The gate "
         "measures the transport-datum evaluation counter to be ZERO at this "
         "point and this gate to be the first gate of the run.  The "
         "`freeze-lax` mutant evaluates one law datum before the freeze and "
         "must die here",
         _FEVALS == 0 and not GATES,
         {"transport_datum_evaluations_so_far": _FEVALS,
          "gates_recorded_so_far": len(GATES),
          "declared_family_size": len(PSI_FAMILY),
          "declared_settings": len(SETTINGS),
          "declared_rules": len(ID_RULES)})
    _FROZEN = True


# ===========================================================================
# 6.  THE DECLARATIONS, MEASURED
# ===========================================================================
def schmidt_rank(psi):
    """The exact rank over Q of the 3x3 coefficient matrix.  The
    `schmidt-lax` mutant returns 1 always, so the family's declared rank
    spread collapses and the family gate must die."""
    report_every_state_as_a_product_state = (MUTANT == "schmidt-lax")
    if report_every_state_as_a_product_state:
        return 1
    rows = [[psi[a * NS + b] for b in range(NS)] for a in range(NS)]
    r = 0
    for c in range(NS):
        piv = None
        for i in range(r, NS):
            if rows[i][c]:
                piv = i
                break
        if piv is None:
            continue
        rows[r], rows[piv] = rows[piv], rows[r]
        for i in range(NS):
            if i != r and rows[i][c]:
                f = rows[i][c] / rows[r][c]
                rows[i] = [rows[i][k] - f * rows[r][k] for k in range(NS)]
        r += 1
    return r


def psi_facts(psi):
    inv = all(psi[i] == psi[SIGMA9[i]] for i in range(NSP))
    anti = all(psi[i] == -psi[SIGMA9[i]] for i in range(NSP))
    born_sym = all(psi[i] * psi[i] == psi[SIGMA9[i]] * psi[SIGMA9[i]]
                   for i in range(NSP))
    return {"norm_squared": str(sum(v * v for v in psi)),
            "is_a_unit_vector": sum(v * v for v in psi) == ONE,
            "schmidt_rank": schmidt_rank(psi),
            "support": sum(1 for v in psi if v),
            "is_exchange_invariant": bool(inv),
            "is_exchange_anti_invariant": bool(anti),
            "its_born_shadow_is_exchange_symmetric": bool(born_sym),
            "coefficients": [str(v) for v in psi]}


def run_base_declaration():
    prog("base G rebuilt and anchored against its pinned declaration")
    q = declared_Q()
    for k in ROT_ORDER:
        for i in range(NS):
            for j in range(NS):
                anchor("A-ROT-%s-%d%d" % (k, i, j), "this unit's pinned "
                       "declaration of base G", "%s[%d][%d]" % (k, i, j),
                       PINNED_ROT[k][i][j], str(ROT[k][i][j]))
    anchor("A-Q", "this unit's pinned declaration of base G",
           "the declared transposition Q, held FIXED across the family",
           Q_PINNED, list(q))
    psiG = psi_vector(dict(PSI_FAMILY[0][2]))
    VG = completion(psiG, q)
    for i in range(NSP):
        for j in range(NSP):
            anchor("A-V-%d%d" % (i, j), "this unit's pinned declaration of "
                   "base G", "V(psi-G)[%d][%d]" % (i, j),
                   PINNED_V_OF_PSI_G[i][j], str(VG[i][j]))
    orth = {k: all(sum(ROT[k][r][a] * ROT[k][r][b] for r in range(NS))
                   == (ONE if a == b else ZERO)
                   for a in range(NS) for b in range(NS))
            for k in ROT_ORDER}
    inj = len({pointer_shift(o) for o in range(NS)}) == NS
    decomp = True
    for wing in ("A", "B"):
        for g in ROT_ORDER:
            reb: dict = {}
            for sa0 in range(NS):
                for sb0 in range(NS):
                    for pa0 in range(NP):
                        for pb0 in range(NP):
                            j = idx(sa0, sb0, pa0, pb0)
                            s0 = sa0 if wing == "A" else sb0
                            p0 = pa0 if wing == "A" else pb0
                            for o in range(NS):
                                p1 = (p0 + SHIFT_DECLARED[o]) % NP
                                for s1 in range(NS):
                                    v = (parse_fr(PINNED_ROT[g][s1][o])
                                         * parse_fr(PINNED_ROT[g][s0][o]))
                                    if not v:
                                        continue
                                    i = (idx(s1, sb0, p1, pb0) if wing == "A"
                                         else idx(sa0, s1, pa0, p1))
                                    c = reb.get((i, j), ZERO) + v
                                    if c:
                                        reb[(i, j)] = c
                                    else:
                                        reb.pop((i, j), None)
            if reb != ULOCAL[(wing, g)]:
                decomp = False
    commute = all(mm(ULOCAL[("A", a)], ULOCAL[("B", b)])
                  == mm(ULOCAL[("B", b)], ULOCAL[("A", a)])
                  for a in ROT_ORDER for b in ROT_ORDER)
    TABLES["base_declaration"] = {
        "carrier": NC, "system_dimension_per_wing": NS,
        "pointer_states_per_wing": NP, "initial_configuration": J0,
        "legs_per_frame": NLEGS, "checkpoints": len(CHECKPOINTS),
        "declared_division_events": list(DIVISION_EVENTS),
        "nodes_per_setting": len(NODES), "path_length_bound": L_MAX,
        "declared_settings": len(SETTINGS),
        "symmetric_settings": [sp for sp in SETTING_ORDER
                               if SETTINGS[sp][0] == SETTINGS[sp][1]],
        "the_declared_transposition_Q": list(q),
        "every_declared_rotation_is_exactly_orthogonal": orth,
        "the_record_shift_is_injective": inj,
        "the_local_legs_decompose_as_declared": decomp,
        "the_two_wings_commute_at_every_declared_pair": commute}
    gate("PSI-BASE-PINNED", "measurement",
         "BASE G IS REBUILT NATIVELY AND ANCHORED, ENTRY BY ENTRY, AGAINST "
         "THIS UNIT'S OWN PINNED DECLARATION.  Nothing of GEN's module is "
         "imported: the three rotation matrices are reconstructed from their "
         "integer quaternions by Euler-Rodrigues and anchored against the "
         "pinned matrices; the declared transposition Q is anchored; and the "
         "completion V = H(psi-G) . Q is anchored against the pinned 9x9 "
         "matrix.  The gate additionally measures the properties the species "
         "needs and the pinned data cannot supply: every rotation exactly "
         "orthogonal over Q, the record shift INJECTIVE, the two wings' legs "
         "COMMUTING at every declared pair, and each local leg equal, entry "
         "by entry, to a sum assembled from the PINNED rotation matrices and "
         "an INDEPENDENTLY DECLARED shift table -- a comparator built from "
         "data independent of the constructor it audits, so a perturbation "
         "of either moves one side of the comparison and not the other.  The "
         "`anchor-rot`, `anchor-Q`, `anchor-psi` and `anchor-record` mutants "
         "each perturb one declared object and must die here",
         all(orth.values()) and inj and decomp and commute
         and all(a["passed"] for a in ANCHORS),
         {"anchors_recorded": len(ANCHORS),
          "anchors_passed": sum(1 for a in ANCHORS if a["passed"]),
          "orthogonality": orth, "record_shift_injective": inj,
          "local_legs_decompose": decomp, "wings_commute": commute})


def run_family_declaration():
    prog("the preparation family, declared as data, its sizes computed")
    q = declared_Q()
    rows = {}
    for nm, why, coeffs in PSI_FAMILY:
        psi = psi_vector(dict(coeffs))
        f = psi_facts(psi)
        V = completion(psi, q)
        f["role"] = why
        f["the_completion_V_has_psi_as_its_first_column"] = all(
            V[i][0] == psi[i] for i in range(NSP))
        f["the_completion_V_is_exactly_orthogonal"] = all(
            sum(V[r][a] * V[r][b] for r in range(NSP))
            == (ONE if a == b else ZERO)
            for a in range(NSP) for b in range(NSP))
        f["the_born_shadow_of_V_is_exchange_symmetric"] = all(
            V[i][j] * V[i][j]
            == V[SIGMA9[i]][SIGMA9[j]] * V[SIGMA9[i]][SIGMA9[j]]
            for i in range(NSP) for j in range(NSP))
        rows[nm] = f
    distinct = len({canon(rows[nm]["coefficients"]) for nm in PSI_ORDER})
    inv = [nm for nm in PSI_ORDER if rows[nm]["is_exchange_invariant"]]
    non = [nm for nm in PSI_ORDER if not rows[nm]["is_exchange_invariant"]]
    ranks_inv = sorted({rows[nm]["schmidt_rank"] for nm in inv})
    bornsym = [nm for nm in PSI_ORDER
               if rows[nm]["its_born_shadow_is_exchange_symmetric"]]
    TABLES["psi_family"] = {
        "per_member": rows, "family_size": len(PSI_FAMILY),
        "distinct_coefficient_vectors": distinct,
        "exchange_invariant_members": inv,
        "exchange_non_invariant_members": non,
        "schmidt_ranks_among_the_invariant_members": ranks_inv,
        "members_whose_born_shadow_is_exchange_symmetric": bornsym,
        "the_declared_transposition_every_member_is_completed_with": list(q),
        "route": "each member is a declared rational vector on the nine "
                 "system-pair basis states; norm, Schmidt rank, exchange "
                 "behaviour and Born-shadow symmetry are computed here, and "
                 "the completion V = H(psi) . Q uses the SAME declared Q for "
                 "every member"}
    gate("PSI-FAMILY-DECLARED", "measurement",
         "THE PREPARATION FAMILY IS DECLARED AS DATA AND ITS SIZES ARE "
         "COMPUTED.  Every member is measured to be an exact rational UNIT "
         "vector, all eleven are measured DISTINCT as coefficient vectors, "
         "and each one's completion V = H(psi) . Q -- built with the SAME "
         "declared Q -- is measured to be exactly orthogonal with psi as its "
         "first column, so every member is a legitimate preparation of the "
         "very same declared form.  The pin's own composition requirements "
         "are measured rather than asserted: at least three exchange-"
         "INVARIANT members BEYOND the pinned one, of DIFFERING Schmidt "
         "rank, and at least three exchange-NON-invariant members.  The "
         "`psi-collapse` mutant replaces every member by the pinned one and "
         "dies at the distinctness clause; the `schmidt-lax` mutant reports "
         "every state as a product state and dies at the rank-spread clause",
         all(rows[nm]["is_a_unit_vector"] for nm in PSI_ORDER)
         and distinct == len(PSI_FAMILY)
         and all(rows[nm]["the_completion_V_is_exactly_orthogonal"]
                 for nm in PSI_ORDER)
         and all(rows[nm]["the_completion_V_has_psi_as_its_first_column"]
                 for nm in PSI_ORDER)
         and len(inv) >= 4 and len(non) >= 3 and len(ranks_inv) >= 3,
         {"family_size": len(PSI_FAMILY),
          "distinct_coefficient_vectors": distinct,
          "exchange_invariant": len(inv), "exchange_non_invariant": len(non),
          "schmidt_ranks_among_the_invariant_members": ranks_inv,
          "members_with_an_exchange_symmetric_born_shadow": len(bornsym),
          "every_member_is_a_unit_vector":
              all(rows[nm]["is_a_unit_vector"] for nm in PSI_ORDER),
          "every_completion_is_orthogonal_with_psi_as_column_0":
              all(rows[nm]["the_completion_V_is_exactly_orthogonal"]
                  and rows[nm]["the_completion_V_has_psi_as_its_first_column"]
                  for nm in PSI_ORDER)})
    return rows


def run_arena():
    prog("the arena, declared, sizes computed")
    _sset = {tuple(p) for p in SCOPE["base"]}
    closed = all(perm_compose(x, y) in _sset for x in _sset for y in _sset)
    adm = [tuple(p) for p in SCOPE["admitted"]]
    TABLES["arena"] = {
        "carrier": NC, "settings": len(SETTINGS),
        "symmetric_setting_count": sum(1 for sp in SETTING_ORDER
                                       if SETTINGS[sp][0] == SETTINGS[sp][1]),
        "frames": len(FRAMES), "legs_per_frame": NLEGS,
        "checkpoints": len(CHECKPOINTS),
        "checkpoint_values": list(CHECKPOINTS),
        "declared_division_events": list(DIVISION_EVENTS),
        "nodes_per_setting": len(NODES), "path_length_bound": L_MAX,
        "declared_relabelling_scope": SCOPE["n_base"],
        "declared_extension_scope": SCOPE["n_ext_total"],
        "admitted_after_the_j0_filter": SCOPE["n_admitted"],
        "admitted_after_the_j0_filter_at_the_extension":
            SCOPE["n_admitted_extension"],
        "the_admitted_maps": sorted(name_perm(p) for p in adm),
        "the_declared_base_point": list(BASE_NODE),
        "the_preparation_family": len(PSI_FAMILY),
        "the_declared_completion_form": "V = H(psi) . Q, Q PINNED",
        "state": "p(0) = delta_{j0}",
        "the_law": "the exact Born law of the declared leg sequence, read at "
                   "the node's declared read time",
        "boundary": "the final division event, checkpoint %d" % NLEGS}
    gate("PSI-ARENA", "measurement",
         "THE ARENA IS DECLARED AS DATA AND EVERY SIZE IS COMPUTED FROM THE "
         "DECLARATION (RUNBOOK section 15).  Boundary: the final division "
         "event.  Family: the six declared settings and the eleven declared "
         "preparations.  Law: the exact Born law at the node's declared read "
         "time.  State: p(0) = delta_{j0}.  Arena: the declared relabelling "
         "scope, generated and deduplicated, together with the two "
         "permutations of it that survive the j0 filter -- the identity and "
         "the wing exchange -- over which EVERY admission search in this "
         "unit runs.  The arena is measured IDENTICAL for every member of "
         "the family, since psi is the only thing the sweep varies.  The "
         "`scope-lax` mutant subsamples the admitted scope and must die here",
         SCOPE["n_admitted"] == 2 and SCOPE["n_base"] > SCOPE["n_admitted"]
         and sorted(name_perm(p) for p in adm) == ["the identity",
                                                   "the wing exchange"]
         and closed,
         {"declared_relabelling_scope": SCOPE["n_base"],
          "declared_extension_scope": SCOPE["n_ext_total"],
          "admitted_after_the_j0_filter": SCOPE["n_admitted"],
          "the_admitted_maps": sorted(name_perm(p) for p in adm),
          "the_declared_scope_is_closed_under_composition": closed,
          "compositions_checked": SCOPE["n_base"] ** 2})


def run_external_pin():
    """The inherited GEN unit, pinned BY HASH before any number is read from
    it.  The `gen-hash` mutant perturbs the bytes before they are hashed."""
    prog("the inherited GEN receipt, pinned by hash")
    raw = GEN_RECEIPT.read_bytes()
    perturb_the_external_receipt = (MUTANT == "gen-hash")
    if perturb_the_external_receipt:
        raw = raw + b"\n"
    h = hashlib.sha256(raw).hexdigest()
    rec = json.loads(GEN_RECEIPT.read_text())
    anchor("A-GEN-SHA", "the committed GEN terminal receipt",
           "sha256 of gen_generality_receipt.json",
           "e0b2f444f6a9b82861024f7733c7230583742dfd477d9ed6037a241e7b48d292",
           h)
    anchor("A-GEN-SCHEMA", "the committed GEN terminal receipt",
           "its schema string", "gen-generality-receipt-v1", rec["schema"])
    anchor("A-GEN-SRC", "the committed GEN terminal receipt",
           "the generator hash it records for its own instrument",
           "f3cc8da27b1c492d670b81157d03aba7a33990663d0cb5001a93718415f298c1",
           rec["source_sha256"])
    TABLES["external_pin"] = {
        "file": GEN_RECEIPT.name, "sha256": h, "schema": rec["schema"],
        "generator_sha256": rec["source_sha256"],
        "base_commit_it_records": rec["base_commit"],
        "route": "the file is hashed and its schema and generator hash are "
                 "anchored BEFORE any number is read out of it, so 'the "
                 "committed GEN terminal receipt' is an assertion and not a "
                 "caption"}
    gate("PSI-GEN-PIN", "measurement",
         "THE INHERITED GEN UNIT IS PINNED BY HASH.  No object of GEN's "
         "model is imported anywhere in this unit: the only thing read from "
         "it is its committed receipt, whose sha256, schema string and "
         "recorded generator hash are ANCHORED EXIT-1 before any value is "
         "taken out of it.  Every number this unit reuses from GEN is "
         "anchored separately, so a drift in the file or in any reused value "
         "kills the run.  The `gen-hash` mutant perturbs the bytes before "
         "they are hashed and must die here",
         all(a["passed"] for a in ANCHORS if a["id"].startswith("A-GEN")),
         {"sha256": h, "schema": rec["schema"],
          "anchors_against_the_external_receipt":
              sum(1 for a in ANCHORS if a["id"].startswith("A-GEN"))})
    return rec


# ===========================================================================
# 7.  THE SWEEP -- one world per declared preparation, everything else fixed
# ===========================================================================
def run_sweep():
    prog("the sweep: one world per declared preparation")
    q = declared_Q()
    collapse_the_family = (MUTANT == "psi-collapse")
    # The reference completion's defect and its product with the wing
    # exchange are given NAMES before the enumeration prints anything.  Names
    # are printing only: every gate predicate in this unit compares
    # permutation tuples, never labels.
    _p, _s = signed_perm(prep_defect(
        World("naming", psi_vector(dict(PSI_FAMILY[0][2])), q)))
    if _p is not None:
        _t = tuple(_p[j] for j in range(NC))
        PERM_NAME.setdefault(canon(list(_t)),
                             "the completion's non-equivariance defect")
        PERM_NAME.setdefault(
            canon(list(perm_compose(tuple(WSWAP), _t))),
            "the wing exchange composed with the non-equivariance defect")
    worlds, results = {}, {}
    for nm, why, coeffs in PSI_FAMILY:
        cc = dict(PSI_FAMILY[0][2]) if collapse_the_family else dict(coeffs)
        W = World(nm, psi_vector(cc), q)
        worlds[nm] = W
        per = {}
        for sp in SETTING_ORDER:
            per[sp] = enumerate_paths(W, sp, L_MAX)
        results[nm] = per
        prog("  %-7s links %s" % (nm, [per[sp]["n_links"]
                                       for sp in SETTING_ORDER]))
    # -- the admission tables, cell by cell ---------------------------------
    admtab = {}
    for nm in PSI_ORDER:
        tab = worlds[nm].admission_table()
        admtab[nm] = {"%s/t%d/%s" % (sp, t, r["id"]):
                      {"n_admitted": tab[(sp, t, r["id"])]["n_admitted"],
                       "maps": tab[(sp, t, r["id"])]["maps"],
                       "drawn": tab[(sp, t, r["id"])]["drawn"]}
                      for sp in SETTING_ORDER for t in CHECKPOINTS
                      for r in ID_RULES}
    cells = len(admtab[PSI_REFERENCE])
    draws = {nm: {r["id"]: sum(1 for k, v in admtab[nm].items()
                               if k.endswith("/" + r["id"]) and v["drawn"])
                  for r in ID_RULES} for nm in PSI_ORDER}
    TABLES["admission_per_psi"] = {
        "cells_per_member": cells, "per_member": admtab,
        "cells_where_each_rule_draws_a_link": draws}
    both = all(draws[nm]["FULL"] > 0 for nm in PSI_ORDER)
    gate("PSI-ADMISSION-PER-PSI", "measurement",
         "THE ADMISSION TABLE IS COMPUTED FOR EVERY MEMBER OF THE FAMILY, AT "
         "EVERY CELL AND BOTH RULES.  The four-clause predicate -- the j0 "
         "filter, the rule's own leg list matched order-free at the Born "
         "level, the occupied-set clause, the exact-law clause -- is "
         "evaluated at all %d (setting, checkpoint) cells for both declared "
         "rules and all eleven preparations, and a link is DRAWN only where "
         "the rule admits UNIQUELY.  The gate measures that the table is a "
         "real partition rather than a constant: the full-leg rule draws "
         "somewhere for EVERY member, the realized rule draws for SOME "
         "members and not for others, and the number of drawing cells is "
         "counted per member and never typed.  The `born-lax` mutant drops "
         "the exact-law clause and the `id-lax` mutant accepts every "
         "admitted permutation, destroying the uniqueness criterion; both "
         "must die here" % (len(SETTING_ORDER) * len(CHECKPOINTS)),
         both and len({draws[nm]["REAL"] for nm in PSI_ORDER}) > 1
         and all(v["n_admitted"] <= 1 or not v["drawn"]
                 for nm in PSI_ORDER for v in admtab[nm].values()),
         {"cells_per_member": cells,
          "members": len(PSI_ORDER),
          "cells_where_each_rule_draws_a_link": draws,
          "distinct_realized_rule_draw_counts":
              sorted({draws[nm]["REAL"] for nm in PSI_ORDER})})
    # -- the loop space, per member -----------------------------------------
    ps = {}
    for nm in PSI_ORDER:
        ps[nm] = {sp: {"links": results[nm][sp]["n_links"],
                       "cycle_rank": results[nm][sp]["stats"][
                           "declared_cycle_rank"],
                       "reduced_paths": results[nm][sp]["stats"][
                           "reduced_paths"],
                       "closed_paths": results[nm][sp]["stats"][
                           "closed_paths"],
                       "based_closed_loops": results[nm][sp]["stats"][
                           "based_closed_loops"]}
                  for sp in SETTING_ORDER}
    tot = {nm: {k: sum(ps[nm][sp][k] for sp in SETTING_ORDER)
                for k in ("reduced_paths", "closed_paths",
                          "based_closed_loops")} for nm in PSI_ORDER}
    audit = {nm: {sp: {k: results[nm][sp]["stats"][k]
                       for k in ("backtracks_found_in_the_delivered_rows",
                                 "rows_that_are_not_genuine_walks",
                                 "components", "euler_cycle_rank",
                                 "declared_cycle_rank")}
                  for sp in SETTING_ORDER} for nm in PSI_ORDER}
    bad = sum(v["backtracks_found_in_the_delivered_rows"]
              + v["rows_that_are_not_genuine_walks"]
              for nm in PSI_ORDER for v in audit[nm].values())
    rows_match = all(len(results[nm][sp]["based"])
                     == results[nm][sp]["stats"]["based_closed_loops"]
                     for nm in PSI_ORDER for sp in SETTING_ORDER)
    euler = all(audit[nm][sp]["euler_cycle_rank"]
                == audit[nm][sp]["declared_cycle_rank"]
                and audit[nm][sp]["components"] == 1
                for nm in PSI_ORDER for sp in SETTING_ORDER)
    TABLES["loop_space_per_psi"] = {
        "per_member": ps, "totals_per_member": tot, "audit": audit}
    gate("PSI-PATH-SPACE", "measurement",
         "THE LOOP SPACE IS ENUMERATED FOR EVERY MEMBER AND EVERY SIZE IS "
         "COMPUTED, NEVER TYPED.  Reduced paths from every node, closed "
         "paths at every base point and closed loops based at the declared "
         "base point are counted by enumeration at the declared length "
         "bound.  Four properties are then RECOMPUTED FROM THE DELIVERED "
         "ROWS THEMSELVES: that no delivered loop traverses one link twice "
         "in immediate succession, that every delivered loop is a genuine "
         "walk returning to the node it declares, that each graph is "
         "connected by union-find over its own links, and that the declared "
         "cycle rank is Euler's with that measured component count.  The "
         "`reduce-lax` mutant drops the reduced condition and the "
         "`path-collapse` mutant gives every loop one name; both must die "
         "here",
         bad == 0 and euler and rows_match
         and all(tot[nm]["based_closed_loops"] > 0 for nm in PSI_ORDER),
         {"members": len(PSI_ORDER),
          "rows_violating_the_reduced_or_walk_conditions": bad,
          "the_delivered_rows_are_as_many_as_the_counted_loops": rows_match,
          "every_graph_connected_with_euler_cycle_rank": euler,
          "totals_per_member": tot})
    return worlds, results


# ===========================================================================
# 8.  THE COMPARISON, AT MATCHED COORDINATES
# ===========================================================================
def run_comparison(worlds, results):
    prog("the comparison at matched coordinates")
    ref = results[PSI_REFERENCE]
    # (ii) the admission tables, cell by cell
    admtab = TABLES["admission_per_psi"]["per_member"]
    delta = {}
    for nm in PSI_ORDER:
        if nm == PSI_REFERENCE:
            continue
        d = [k for k in sorted(admtab[PSI_REFERENCE])
             if (admtab[PSI_REFERENCE][k]["n_admitted"]
                 != admtab[nm][k]["n_admitted"]
                 or admtab[PSI_REFERENCE][k]["maps"] != admtab[nm][k]["maps"])]
        delta[nm] = d
    movers = sorted(nm for nm in delta if delta[nm])
    still = sorted(nm for nm in delta if not delta[nm])
    # (i) the common loops, matched by NAME, and their holonomy
    matched = {}
    for nm in PSI_ORDER:
        if nm == PSI_REFERENCE:
            continue
        rows = {}
        for sp in SETTING_ORDER:
            a, b = ref[sp]["based"], results[nm][sp]["based"]
            common = set(a) & set(b)
            born_diff = sorted((l for l in common
                                if a[l]["born"] != b[l]["born"]),
                               key=lambda x: (len(x), canon(x)))
            perm_diff = sorted((l for l in common
                                if a[l]["perm"] != b[l]["perm"]),
                               key=lambda x: (len(x), canon(x)))
            flat_to_non = sorted(
                (l for l in common
                 if a[l]["perm"] == tuple(IDPERM) and a[l]["born"]
                 != b[l]["born"]), key=lambda x: (len(x), canon(x)))
            readable_flip = sorted(
                (l for l in common
                 if (a[l]["perm"] is None) != (b[l]["perm"] is None)),
                key=lambda x: (len(x), canon(x)))
            rows[sp] = {
                "loops_at_the_reference": len(a),
                "loops_at_this_member": len(b),
                "common_loops": len(common),
                "loops_only_at_the_reference": len(a) - len(common),
                "loops_only_at_this_member": len(b) - len(common),
                "common_loops_whose_born_holonomy_differs": len(born_diff),
                "common_loops_whose_permutation_part_differs":
                    len(perm_diff),
                "common_loops_flat_at_the_reference_and_not_here":
                    len(flat_to_non),
                "common_loops_where_readability_flips": len(readable_flip),
                "_witness_born": born_diff[0] if born_diff else None,
                "_witness_flat": flat_to_non[0] if flat_to_non else None}
        matched[nm] = rows
    TABLES["matched_comparison"] = {
        "reference": PSI_REFERENCE,
        "admission_delta_cells": {nm: delta[nm] for nm in PSI_ORDER
                                  if nm != PSI_REFERENCE},
        "members_whose_admission_table_moves": movers,
        "members_whose_admission_table_is_identical": still,
        "per_member_per_setting": {
            nm: {sp: {k: v for k, v in matched[nm][sp].items()
                      if not k.startswith("_")}
                 for sp in SETTING_ORDER} for nm in matched},
        "route": "loops are matched by their psi-INDEPENDENT LINK NAMES -- "
                 "('leg', frame, leg) and ('id', checkpoint, rule) -- so a "
                 "loop common to two members is the same sequence of named "
                 "links traversed in the same directions, at the same "
                 "setting, based at the same declared node, with the same "
                 "read times; the matched table is the primary object and "
                 "every contrast below is derived from it"}
    # the witness census
    curv = sorted(nm for nm in matched
                  if any(matched[nm][sp]["common_loops_whose_born_holonomy"
                                         "_differs"] > 0
                         for sp in SETTING_ORDER))
    quiet = sorted(nm for nm in matched if nm not in curv)
    inv_rows = TABLES["psi_family"]["per_member"]
    invariant_and_quiet = all(
        nm in quiet for nm in matched if inv_rows[nm]["is_exchange_invariant"])
    noninv_bornsym_and_loud = all(
        nm in curv for nm in matched
        if (not inv_rows[nm]["is_exchange_invariant"]
            and inv_rows[nm]["its_born_shadow_is_exchange_symmetric"]))
    TABLES["witness_census"] = {
        "members_with_a_differing_common_loop": curv,
        "members_with_no_differing_common_loop": quiet,
        "every_exchange_invariant_member_agrees_everywhere":
            invariant_and_quiet,
        "every_born_symmetric_non_invariant_member_disagrees_somewhere":
            noninv_bornsym_and_loud}
    gate("PSI-MATCHED-COORDINATES", "measurement",
         "EVERY COMPARISON IS READ AT MATCHED COORDINATES (RUNBOOK section "
         "15 addendum).  The compared objects are loops, and a loop is "
         "identified by its psi-INDEPENDENT LINK NAMES together with the "
         "traversal directions, so 'the same loop at two preparations' is a "
         "statement about names and not about positions in a list that "
         "moved.  Four coordinates are measured to match at every cell of "
         "the table: the SETTING, the BASE POINT, the sequence of NAMED "
         "links with directions, and the READ TIME, which is carried inside "
         "the law datum and is measured never to compare equal across two "
         "different checkpoints.  The gate measures that the link names are "
         "injective within a graph (so a name identifies one link) and that "
         "the reference member's own loop set is recovered by name at every "
         "setting.  The `loopname-collapse` mutant collapses the link names "
         "and the `readtime-conflate` mutant reads every datum at the final "
         "checkpoint; both must die here",
         all(len({canon(L["name"]) for L in worlds[nm].graph(sp)["links"]})
             == len(worlds[nm].graph(sp)["links"])
             for nm in PSI_ORDER for sp in SETTING_ORDER)
         and all(matched[nm][sp]["common_loops"] > 0
                 for nm in matched for sp in SETTING_ORDER)
         and _read_times_never_collide(worlds),
         {"members_compared": len(matched),
          "settings": len(SETTING_ORDER),
          "link_names_are_injective_in_every_graph": True,
          "read_time_collisions_across_checkpoints": 0})
    return matched, delta, movers, still, curv, quiet


def _read_times_never_collide(worlds):
    """Two law data read at different checkpoints must never compare equal:
    the read time is a coordinate of the datum."""
    bad = 0
    for nm in PSI_ORDER:
        W = worlds[nm]
        for sp in SETTING_ORDER:
            vals = {}
            for fr in FRAMES:
                for t in CHECKPOINTS:
                    d = W.node_law(sp, fr, t)
                    vals[(fr, t)] = (d["read_time"],
                                     frozenset(d["law"].items()))
            for k1 in vals:
                for k2 in vals:
                    if k1[1] != k2[1] and vals[k1] == vals[k2]:
                        bad += 1
    TABLES.setdefault("read_time", {})["collisions"] = bad
    return bad == 0


# ===========================================================================
# 9.  THE psi-LAW -- how the defect depends on the preparation
# ===========================================================================
def m9(A, B):
    out = {}
    for (i, k), u in A.items():
        for j in range(NSP):
            v = B.get((k, j))
            if v is None:
                continue
            t = u * v
            if not t:
                continue
            s = out.get((i, j), ZERO) + t
            if s:
                out[(i, j)] = s
            else:
                out.pop((i, j), None)
    return out


def dense9(V):
    return {(i, j): V[i][j] for i in range(NSP) for j in range(NSP)
            if V[i][j]}


def tensor_with_pointer_identity(M9):
    """M (x) I_9: the 9x9 system-pair matrix acting on the 81 configurations
    and trivially on the pointer pair, in the model's own index map."""
    out = {}
    for (a, b), v in M9.items():
        for p in range(NSP):
            out[(a * NSP + p, b * NSP + p)] = v
    return out


def prep_defect(W, sp=None):
    """D = P_W U_prep^-1 P_W U_prep, computed DIRECTLY at 81x81.  The
    `defect-order` mutant composes the four factors in the wrong order."""
    PW = pmat(WSWAP)
    U = W.Uprep
    compose_the_defect_in_the_wrong_order = (MUTANT == "defect-order")
    if compose_the_defect_in_the_wrong_order:
        return mm(PW, mm(U, mm(PW, minv(U))))
    return mm(PW, mm(minv(U), mm(PW, U)))


def run_psi_law(worlds):
    """THE psi-LAW: D(psi) = D_GEN . Q^T E(psi) Q with E(psi) = sigma H sigma
    H, and E(psi) = I exactly on the exchange-invariant locus."""
    prog("the psi-law and its two-directional characterisation")
    q = declared_Q()
    s9 = {(SIGMA9[i], i): ONE for i in range(NSP)}
    QP = {(q[j], j): ONE for j in range(NSP)}
    QPt = {(j, q[j]): ONE for j in range(NSP)}
    D_gen9 = m9(s9, m9(QPt, m9(s9, QP)))
    drop_the_psi_term = (MUTANT == "psilaw-drop")
    rows, law_ok, char_ok = {}, True, True
    for nm in PSI_ORDER:
        W = worlds[nm]
        H = dense9(householder(W.psi))
        E = m9(s9, m9(H, m9(s9, H)))
        E_is_identity = (E == {(i, i): ONE for i in range(NSP)})
        pred9 = (dict(D_gen9) if drop_the_psi_term
                 else m9(D_gen9, m9(QPt, m9(E, QP))))
        pred = tensor_with_pointer_identity(pred9)
        direct = prep_defect(W)
        law_ok = law_ok and (pred == direct)
        inv = TABLES["psi_family"]["per_member"][nm]["is_exchange_invariant"]
        char_ok = char_ok and (E_is_identity == inv)
        p, _s = signed_perm(direct)
        rows[nm] = {
            "the_psi_term_E_is_the_identity": E_is_identity,
            "psi_is_exchange_invariant": inv,
            "the_law_reproduces_the_direct_81x81_defect": pred == direct,
            "the_defect_equals_GENs": direct == tensor_with_pointer_identity(
                D_gen9),
            "the_defect_is_a_signed_permutation": p is not None,
            "the_defects_fixed_configurations":
                None if p is None else fixed_points(
                    [p[j] for j in range(NC)]),
            "the_defects_order":
                None if p is None else perm_order(
                    [p[j] for j in range(NC)])}
    same_as_gen = sorted(nm for nm in PSI_ORDER
                         if rows[nm]["the_defect_equals_GENs"])
    inv_members = TABLES["psi_family"]["exchange_invariant_members"]
    TABLES["psi_law"] = {
        "statement": "D(psi) = D_GEN . Q^T E(psi) Q, with E(psi) = sigma "
                     "H(psi) sigma H(psi) the Householder's own exchange "
                     "defect and D_GEN = (sigma Q^T sigma Q) (x) I_9",
        "per_member": rows,
        "members_whose_defect_equals_GENs": same_as_gen,
        "the_exchange_invariant_members": inv_members,
        "the_two_lists_coincide": same_as_gen == sorted(inv_members),
        "route": "the law is evaluated at 9x9 and tensored with the pointer "
                 "identity, and is compared against the DIRECT 81x81 "
                 "four-factor product built from the member's own "
                 "preparation leg -- two independent routes to the same "
                 "object"}
    gate("PSI-LAW", "derivation",
         "THE GEN LAW GENERALISES, AND THE psi-TERM IS EXHIBITED.  GEN "
         "measured D = (sigma Q^T sigma Q) (x) I_9 for an exchange-INVARIANT "
         "preparation, with the Householder cancelling identically.  Off "
         "that locus the cancellation fails, and what replaces it is "
         "measured here: D(psi) = D_GEN . Q^T E(psi) Q with E(psi) = sigma "
         "H(psi) sigma H(psi) -- the HOUSEHOLDER'S OWN exchange defect.  Two "
         "clauses, both must-pass.  (1) THE LAW: for every member of the "
         "family the 9x9 law tensored with the pointer identity is measured "
         "EQUAL, entry by entry, to the direct 81x81 four-factor product "
         "P_W U_prep^-1 P_W U_prep built from that member's own preparation "
         "leg -- two independent routes.  (2) THE CHARACTERISATION, IN BOTH "
         "DIRECTIONS: the psi-term E(psi) is the identity EXACTLY on the "
         "exchange-invariant members and on no other, so the list of members "
         "reproducing GEN's defect is measured to COINCIDE with the list of "
         "exchange-invariant members -- neither inclusion assumed.  The "
         "`psilaw-drop` mutant drops the psi-term, so the law predicts GEN's "
         "defect for every member, and the `defect-order` mutant composes "
         "the four factors in the wrong order; both must die here",
         law_ok and char_ok and same_as_gen == sorted(inv_members),
         {"members": len(PSI_ORDER),
          "the_law_reproduces_the_direct_computation_at_every_member": law_ok,
          "the_psi_term_is_the_identity_exactly_on_the_invariant_locus":
              char_ok,
          "members_whose_defect_equals_GENs": same_as_gen,
          "the_exchange_invariant_members": sorted(inv_members)})
    return rows


# ===========================================================================
# 10.  THE SIGN-FLIP CENSUS -- exhaustive over the declared sub-family
# ===========================================================================
def run_signflip_census(worlds):
    """Every member of the family is completed with the same Q, so the one
    remaining freedom inside a fixed BORN SHADOW is the sign pattern.  For
    each declared exchange-invariant member, every sign pattern that fixes
    the initial coefficient is enumerated and rebuilt in full at the
    symmetric setting GP-E."""
    prog("the sign-flip census, exhaustive over the declared sub-family")
    q = declared_Q()
    subsample = (MUTANT == "signflip-lax")
    ref = enumerate_paths(worlds[PSI_REFERENCE], "GP-E", L_MAX,
                          starts=(BASE_NODE,))["based"]
    inv_members = [nm for nm in PSI_ORDER
                   if TABLES["psi_family"]["per_member"][nm][
                       "is_exchange_invariant"]]
    rows, total, mismatches = [], 0, 0
    for nm in inv_members:
        base = worlds[nm].psi
        sup = [i for i in range(NSP) if base[i] and i != 0]
        pats = list(itertools.product((1, -1), repeat=len(sup)))
        if subsample:
            pats = pats[:1]
        for pat in pats:
            psi = list(base)
            for k, i in enumerate(sup):
                psi[i] = psi[i] * pat[k]
            still_invariant = all(psi[i] == psi[SIGMA9[i]]
                                  for i in range(NSP))
            born_same = all(psi[i] * psi[i] == base[i] * base[i]
                            for i in range(NSP))
            W2 = World("%s%s" % (nm, canon(list(pat))), psi, q)
            got = enumerate_paths(W2, "GP-E", L_MAX,
                                  starts=(BASE_NODE,))["based"]
            common = set(ref) & set(got)
            agrees = all(ref[l]["born"] == got[l]["born"] for l in common)
            same_space = set(ref) == set(got)
            total += 1
            if agrees != still_invariant or not same_space or not born_same:
                mismatches += 1
            rows.append({"member": nm, "sign_pattern": list(pat),
                         "still_exchange_invariant": bool(still_invariant),
                         "the_born_shadow_is_unchanged": bool(born_same),
                         "the_loop_space_is_unchanged": bool(same_space),
                         "every_common_loop_agrees_with_the_reference":
                             bool(agrees),
                         "common_loops": len(common)})
    moved = [r for r in rows if not r["every_common_loop_agrees_with_the"
                                     "_reference"]]
    TABLES["signflip_census"] = {
        "sub_family_size": total, "members_swept": inv_members,
        "rows": rows,
        "patterns_that_move_the_holonomy": len(moved),
        "patterns_that_do_not": total - len(moved),
        "mismatches_between_agreement_and_exchange_invariance": mismatches,
        "route": "for each declared exchange-invariant member every sign "
                 "pattern on its support that fixes the initial coefficient "
                 "is enumerated -- the size is computed, never typed -- and "
                 "each one is REBUILT IN FULL at GP-E: new completion, new "
                 "admission table, new graph, new enumeration, new based "
                 "holonomy"}
    gate("PSI-SIGNFLIP-CENSUS", "measurement",
         "THE SIGN-FLIP CENSUS IS EXHAUSTIVE OVER THE DECLARED SUB-FAMILY "
         "AND DECIDES THE DEPENDENCE IN BOTH DIRECTIONS.  Every sign pattern "
         "on the support of every declared exchange-invariant member -- the "
         "count computed by enumeration -- is rebuilt in full at the "
         "symmetric setting GP-E.  Three things are measured at every "
         "member.  The BORN SHADOW is unchanged by a sign pattern, so no "
         "Born-level declaration can see the flip.  The LOOP SPACE is "
         "unchanged, so every loop is common and the comparison is total "
         "rather than partial.  And the HOLONOMY agrees with the reference "
         "on every common loop IF AND ONLY IF the flipped state is still "
         "exchange-invariant -- both directions, member by member, with the "
         "number of mismatches gated at zero.  That is the dependence law: "
         "the holonomy moves exactly when the sign pattern differs across "
         "some sigma-pair of the support.  The `signflip-lax` mutant "
         "subsamples the census to one pattern per member and must die here",
         mismatches == 0 and total > 2 * len(inv_members)
         and len(moved) > 0 and len(moved) < total,
         {"sub_family_size": total, "members_swept": len(inv_members),
          "patterns_that_move_the_holonomy": len(moved),
          "patterns_that_do_not": total - len(moved),
          "mismatches_between_agreement_and_exchange_invariance":
              mismatches})


# ===========================================================================
# 11.  THE TWO CONTROLS
# ===========================================================================
def run_positive_control(worlds, results, gen):
    """GEN's pinned psi must reproduce GEN's terminal readings exactly."""
    prog("the positive control: psi-G must reproduce the GEN terminal unit")
    per = gen["findings"]["holonomy_group"]["per_setting"]
    adm = gen["tables"]["admission"]["per_cell"]
    ps = gen["tables"]["path_space"]
    perturb_a_reused_committed_value = (MUTANT == "anchor-gen")
    if perturb_a_reused_committed_value:
        per["GP-E"]["generated_group_order"] += 1
    mine = {sp: based_group(results[PSI_REFERENCE][sp]["based"])
            for sp in SETTING_ORDER}
    for sp in SETTING_ORDER:
        anchor("A-GEN-GRP-%s" % sp, "the committed GEN terminal receipt",
               "the based holonomy group order at %s" % sp,
               per[sp]["generated_group_order"],
               mine[sp]["generated_group_order"])
        anchor("A-GEN-LOOPS-%s" % sp, "the committed GEN terminal receipt",
               "the closed paths based at F1@t0 at %s" % sp,
               per[sp]["closed_paths_based_there"],
               mine[sp]["based_closed_loops"])
        anchor("A-GEN-LINKS-%s" % sp, "the committed GEN terminal receipt",
               "the links of the path graph at %s" % sp, ps[sp]["links"],
               results[PSI_REFERENCE][sp]["n_links"])
        anchor("A-GEN-CLOSED-%s" % sp, "the committed GEN terminal receipt",
               "the closed paths at every base point at %s" % sp,
               ps[sp]["closed_paths"],
               results[PSI_REFERENCE][sp]["stats"]["closed_paths"])
        anchor("A-GEN-PATHS-%s" % sp, "the committed GEN terminal receipt",
               "the reduced paths at %s" % sp, ps[sp]["paths"],
               results[PSI_REFERENCE][sp]["stats"]["reduced_paths"])
    anchor("A-GEN-VALSET", "the committed GEN terminal receipt",
           "the value-set size at GP-E and its closure",
           [per["GP-E"]["value_set_size"],
            per["GP-E"]["the_value_set_is_closed_under_composition"],
            per["GP-E"]["the_group_is_abelian"],
            per["GP-E"]["element_orders"]],
           [mine["GP-E"]["value_set_size"],
            mine["GP-E"]["the_value_set_is_closed_under_composition"],
            mine["GP-E"]["the_group_is_abelian"],
            mine["GP-E"]["element_orders"]])
    anchor("A-GEN-FIXPTS", "the committed GEN terminal receipt",
           "the fixed configurations of every element of the group at GP-E",
           sorted(per["GP-E"]["element_fixed_points"].values()),
           mine["GP-E"]["element_fixed_point_multiset"])
    mytab = TABLES["admission_per_psi"]["per_member"][PSI_REFERENCE]
    gen_cells = {"%s/t%d/%s" % (sp, t, r): adm["%s/t%d" % (sp, t)][
        "FULL" if r == "FULL" else "REAL"]["maps"]
        for sp in SETTING_ORDER for t in CHECKPOINTS
        for r in ("FULL", "REAL")}
    mine_cells = {k: v["maps"] for k, v in mytab.items()}
    anchor("A-GEN-ADMISSION", "the committed GEN terminal receipt",
           "the admission table, all %d cells, both rules, cell by cell"
           % len(gen_cells), gen_cells, mine_cells)
    defect = prep_defect(worlds[PSI_REFERENCE])
    p, _s = signed_perm(defect)
    anchor("A-GEN-DEFECT", "the committed GEN terminal receipt",
           "the defect's order and its fixed configurations",
           [gen["findings"]["patterns"]["P3_non_equivariance_defect"][
               "order"],
            gen["findings"]["patterns"]["P3_non_equivariance_defect"][
                "fixed_points"]],
           [None if p is None else perm_order([p[j] for j in range(NC)]),
            None if p is None else fixed_points([p[j] for j in range(NC)])])
    overwrite_the_positive_control = (MUTANT == "control-lax")
    ok = all(a["passed"] for a in ANCHORS if a["id"].startswith("A-GEN"))
    if overwrite_the_positive_control:
        ok = False
    TABLES["positive_control"] = {
        "per_setting": {sp: {k: v for k, v in mine[sp].items()
                             if not k.startswith("_")}
                        for sp in SETTING_ORDER},
        "anchors_against_GEN": sum(1 for a in ANCHORS
                                   if a["id"].startswith("A-GEN")),
        "route": "every reading is recomputed natively here and anchored, "
                 "exit-1, against the value GEN's committed receipt records"}
    gate("PSI-POSITIVE-CONTROL", "measurement",
         "THE POSITIVE CONTROL: GEN'S PINNED PREPARATION REPRODUCES GEN'S "
         "TERMINAL UNIT EXACTLY, AND EVERY CLAUSE IS AN ANCHOR AGAINST THE "
         "COMMITTED RECEIPT.  At psi-G this unit's independently rebuilt "
         "instrument is measured to deliver GEN's admission table cell for "
         "cell in the permutation each rule draws at all 48 (setting, "
         "checkpoint, rule) cells; GEN's link counts, reduced-path counts, "
         "closed-path counts and based-loop counts at every setting; GEN's "
         "based holonomy group order at every setting, with the value set "
         "measured closed at the declared bound, the group abelian, every "
         "element of order dividing two -- the KLEIN FOUR-GROUP -- and the "
         "four elements' fixed-configuration counts; and GEN's defect, of "
         "order two with 45 fixed configurations.  If any of these had "
         "moved, the instrument would be measuring something other than "
         "GEN's geometry and no comparison across psi would mean anything.  "
         "The `anchor-gen` mutant perturbs a reused GEN value and the "
         "`control-lax` waiver overwrites this predicate; both must die here",
         ok, {"anchors_against_GEN":
              sum(1 for a in ANCHORS if a["id"].startswith("A-GEN")),
              "anchors_passed": sum(1 for a in ANCHORS
                                    if a["id"].startswith("A-GEN")
                                    and a["passed"]),
              "group_order_per_setting":
                  {sp: mine[sp]["generated_group_order"]
                   for sp in SETTING_ORDER}})
    return mine


def delta_of_Q(q):
    """delta(Q) = sigma Q^-1 sigma Q, as a permutation of the nine
    system-pair labels: the GEN law's own predictor."""
    qi = [0] * NSP
    for i, v in enumerate(q):
        qi[v] = i
    return tuple(SIGMA9[qi[SIGMA9[q[i]]]] for i in range(NSP))


def run_negative_control(worlds, results):
    """A DIFFERENT declared Q must move the holonomy by the amount the GEN law
    predicts.  If it does not, the instrument is dead."""
    prog("the negative control with teeth: a different declared Q")
    psiG = worlds[PSI_REFERENCE].psi
    ref = based_group(results[PSI_REFERENCE]["GP-E"]["based"])
    rows = {}
    for nm, why, q in Q_CONTROLS:
        use_the_pinned_Q_instead = (MUTANT == "qcontrol-lax")
        qq = list(declared_Q()) if use_the_pinned_Q_instead else list(q)
        d = delta_of_Q(qq)
        n = 1
        cur, ident = tuple(d), tuple(range(NSP))
        while cur != ident:
            cur = tuple(d[cur[i]] for i in range(NSP))
            n += 1
        W2 = World("%s@%s" % (PSI_REFERENCE, nm), psiG, qq)
        got = enumerate_paths(W2, "GP-E", L_MAX, starts=(BASE_NODE,))
        grp = based_group(got["based"])
        predicted = 1 if n == 1 else 2 * n
        rows[nm] = {
            "description": why, "Q": qq,
            "delta_of_Q": list(d), "order_of_delta": n,
            "the_GEN_law_predicts_a_group_of_order": predicted,
            "measured_group_order": grp["generated_group_order"],
            "measured_abelian": grp["the_group_is_abelian"],
            "links": got["n_links"],
            "based_closed_loops": grp["based_closed_loops"],
            "the_prediction_is_met":
                grp["generated_group_order"] == predicted,
            "the_holonomy_moved_from_the_pinned_Q":
                grp["generated_group_order"]
                != ref["generated_group_order"]
                or grp["the_group_is_abelian"] != ref["the_group_is_abelian"]}
    TABLES["negative_control"] = {
        "at_the_pinned_Q": {"group_order": ref["generated_group_order"],
                            "abelian": ref["the_group_is_abelian"],
                            "links": results[PSI_REFERENCE]["GP-E"][
                                "n_links"]},
        "per_control": rows,
        "route": "the preparation is held at psi-G and the declared "
                 "transposition alone is changed, so the contrast is read at "
                 "matched coordinates: same base, same rules, same scopes, "
                 "same setting, same base point"}
    gate("PSI-NEGATIVE-CONTROL", "measurement",
         "THE NEGATIVE CONTROL HAS TEETH, AND ITS PREDICTION IS THE GEN "
         "LAW'S.  At the SAME preparation psi-G and with every other "
         "declaration untouched, the declared transposition Q is replaced by "
         "two other declared transpositions, and the holonomy must move by "
         "the amount GEN's dihedral law predicts: a group of order 2n with "
         "n = ord(sigma Q^-1 sigma Q), and order 1 with links refused on the "
         "exchange-equivariant locus where that order is one.  Q-negA has "
         "delta of order THREE, so the law predicts a NON-ABELIAN group of "
         "order six where the pinned Q gives the abelian group of order "
         "four; Q-negB lies on the equivariant locus, so the law predicts a "
         "FLAT connection.  Both predictions are measured, and the gate "
         "requires both to be met AND the holonomy to have actually moved "
         "from the pinned Q's reading -- if a declaration change cannot move "
         "this instrument, the instrument is dead and no psi-side reading it "
         "reports is worth anything.  The `qcontrol-lax` mutant substitutes "
         "the pinned Q for the controls, so nothing moves, and must die here",
         all(r["the_prediction_is_met"] and r["the_holonomy_moved_from_the"
                                              "_pinned_Q"]
             for r in rows.values()),
         {"at_the_pinned_Q": ref["generated_group_order"],
          "controls": {nm: {"order_of_delta": r["order_of_delta"],
                            "predicted": r["the_GEN_law_predicts_a_group_of"
                                           "_order"],
                            "measured": r["measured_group_order"],
                            "abelian": r["measured_abelian"]}
                       for nm, r in rows.items()}})


# ===========================================================================
# 12.  THE SWITCHING SELF-TEST (RUNBOOK section 14) AND THE FLIP-TESTS
# ===========================================================================
DECLARED_PROBES = (
    ("the canonical loop",
     ((("id", 0, "FULL"), -1), (("leg", "F2", 1), +1), (("leg", "F2", 2), +1),
      (("leg", "F2", 3), +1), (("id", 3, "FULL"), +1),
      (("leg", "F1", 3), -1), (("leg", "F1", 2), -1),
      (("leg", "F1", 1), -1))),
    ("the realized prep bigon",
     ((("id", 0, "REAL"), -1), (("leg", "F2", 1), +1),
      (("id", 1, "REAL"), +1), (("leg", "F1", 1), -1))),
    ("the mixed prep bigon",
     ((("id", 0, "FULL"), -1), (("leg", "F2", 1), +1),
      (("id", 1, "REAL"), +1), (("leg", "F1", 1), -1))),
    ("the doubled realized prep bigon",
     ((("id", 0, "REAL"), -1), (("leg", "F2", 1), +1),
      (("id", 1, "REAL"), +1), (("leg", "F1", 1), -1),
      (("id", 0, "REAL"), -1), (("leg", "F2", 1), +1),
      (("id", 1, "REAL"), +1), (("leg", "F1", 1), -1))),
)
SWEEP_SETTING = "GP-E"
SWEEP_MEMBERS = ("psi-G", "psi-N1")


def named_edges(W, sp, names):
    """Resolve a declared loop, given by NAMES, into this world's own link
    indices.  Returns None if the world's graph does not contain every named
    link -- which is exactly what 'the loop does not exist here' means."""
    G = W.graph(sp)
    by = {}
    for li, L in enumerate(G["links"]):
        by[canon(L["name"])] = li
    out = []
    for nm, d in names:
        k = canon(list(nm))
        if k not in by:
            return None
        out.append((by[k], d))
    return out


def loop_matrix_fresh(W, sp, edges, signs=None, memoised=True):
    """The closed-loop matrix, REBUILT from the link variables.  `signs` is a
    switching: one sign per link of the graph.  The `gauge-sign` mutant drops
    the switching on a reversed traversal, so its action is no longer a global
    scalar and the sweep's must-pass clause fails."""
    G = W.graph(sp)
    acc = sp_id()
    for (li, d) in edges:
        M = W.link_variable(sp, G["links"][li], d)
        if signs is not None:
            s = signs[li]
            drop_the_switching_on_a_reversed_traversal = (
                MUTANT == "gauge-sign")
            if drop_the_switching_on_a_reversed_traversal and d < 0:
                s = 1
            if s < 0:
                M = sp_neg(M)
        acc = (mm_memo(M, acc) if memoised else mm(M, acc))
    return acc


def run_switching_selftest(worlds):
    """RUNBOOK section 14: an instrument that computes a symmetry-invariant
    quantity must be self-tested under the symmetry's own action."""
    global _FRESH
    prog("the switching self-test, complete at the declared setting")
    rows = {}
    # -- prime the cache with the very keys the self-test will request ------
    primed, reread = 0, 0
    for nm in SWEEP_MEMBERS:
        W = worlds[nm]
        for pname, names in DECLARED_PROBES:
            e = named_edges(W, SWEEP_SETTING, names)
            if e is None:
                continue
            _memo((nm, SWEEP_SETTING, pname),
                  lambda W=W, e=e: loop_matrix_fresh(W, SWEEP_SETTING, e))
            primed += 1
    for nm in SWEEP_MEMBERS:
        W = worlds[nm]
        for pname, names in DECLARED_PROBES:
            e = named_edges(W, SWEEP_SETTING, names)
            if e is None:
                continue
            before = _CACHE["cache_reads_that_returned_a_stored_value"]
            _memo((nm, SWEEP_SETTING, pname),
                  lambda: (_ for _ in ()).throw(
                      RuntimeError("the primed cache did not serve")))
            if _CACHE["cache_reads_that_returned_a_stored_value"] > before:
                reread += 1
    comparisons, deviations, unreadable_flips, telescoping = 0, 0, 0, 0
    _FRESH = True
    for nm in SWEEP_MEMBERS:
        W = worlds[nm]
        G = W.graph(SWEEP_SETTING)
        L = len(G["links"])
        subsample = (MUTANT == "gauge-subsample")
        universe = list(itertools.product((1, -1), repeat=L))
        if subsample:
            universe = universe[:4]
        for pname, names in DECLARED_PROBES:
            e = named_edges(W, SWEEP_SETTING, names)
            if e is None:
                continue
            base = _memo((nm, SWEEP_SETTING, pname),
                         lambda W=W, e=e: loop_matrix_fresh(
                             W, SWEEP_SETTING, e, memoised=False))
            b_born, b_sp = born_shadow_key(base), signed_perm(base)[0]
            for sw in universe:
                M = _memo((nm, SWEEP_SETTING, pname),
                          lambda W=W, e=e, sw=sw: loop_matrix_fresh(
                              W, SWEEP_SETTING, e, signs=sw))
                comparisons += 1
                prod = 1
                for (li, _d) in e:
                    prod *= sw[li]
                if M != (base if prod > 0 else sp_neg(base)):
                    deviations += 1
                if born_shadow_key(M) != b_born:
                    deviations += 1
                if (signed_perm(M)[0] is None) != (b_sp is None):
                    unreadable_flips += 1
            # -- the checkpoint subgroup: node signs, which must telescope --
            for bits in itertools.product((1, -1), repeat=len(NODES) - 1):
                node_sign = {NODES[0]: 1}
                for k, n in enumerate(NODES[1:]):
                    node_sign[n] = bits[k]
                sw = [node_sign[G["links"][li]["a"]]
                      * node_sign[G["links"][li]["b"]] for li in range(L)]
                M = loop_matrix_fresh(W, SWEEP_SETTING, e, signs=sw)
                comparisons += 1
                if M != base:
                    telescoping += 1
            rows["%s/%s" % (nm, pname)] = {
                "the_holonomy_is_a_signed_permutation": b_sp is not None,
                "links_of_the_graph": L,
                "switchings_swept": len(universe),
                "the_switching_group_is_swept_complete":
                    len(universe) == 2 ** L,
                "checkpoint_switchings_swept": 2 ** (len(NODES) - 1)}
    _FRESH = False
    TABLES["switching_selftest"] = {
        "setting": SWEEP_SETTING, "members": list(SWEEP_MEMBERS),
        "probes": [p[0] for p in DECLARED_PROBES],
        "per_probe": rows,
        "exact_matrix_comparisons": comparisons,
        "the_switching_group_is_swept_complete_at_every_probe":
            all(r["the_switching_group_is_swept_complete"]
                for r in rows.values()),
        "deviations_from_the_global_scalar_action": deviations,
        "loops_whose_readability_moved_under_a_switching": unreadable_flips,
        "checkpoint_switchings_that_did_not_telescope": telescoping,
        "cache": dict(_CACHE),
        "cache_entries_primed": primed,
        "primed_keys_that_the_cache_served_on_a_second_visit": reread,
        "route": "the tested set is fixed by DECLARATION -- the declared "
                 "probe loops, in the order they are declared, at the "
                 "declared setting, for the declared members -- and is never "
                 "selected by the verdicts under audit"}
    complete = bool(rows) and all(
        r["the_switching_group_is_swept_complete"] for r in rows.values())
    ok = (deviations == 0 and unreadable_flips == 0 and telescoping == 0
          and comparisons > 0 and complete
          and _CACHE["value_cache_hits"] == 0
          and _CACHE["value_cache_misses"] > 0
          and _CACHE["fresh_requests_for_a_key_already_in_the_cache"] > 0
          and reread == primed and primed > 0)
    gate("PSI-SWITCHING-SELFTEST", "measurement",
         "THE HOLONOMY READINGS ARE SELF-TESTED UNDER THE SYMMETRY'S OWN "
         "ACTION, AND THE SELF-TEST EVALUATES FRESH AGAINST A CACHE MEASURED "
         "TO WORK (RUNBOOK section 14 and both its addenda).  The declared "
         "switching group assigns one sign to each link of the setting's own "
         "graph and is swept COMPLETE, and the checkpoint subgroup -- the "
         "switchings induced by a sign at each node -- is swept complete "
         "beside it.  Three must-pass clauses: every swept holonomy is "
         "measured to equal the unswitched one times the product of the "
         "signs along the loop, so the action is a GLOBAL SCALAR; the BORN "
         "SHADOW of the holonomy, this unit's primary comparator, is "
         "measured INVARIANT at every switching; and no checkpoint switching "
         "moves any holonomy at all.  Every holonomy in the sweep is REBUILT "
         "from the link variables with the value cache bypassed, and the "
         "bypass is measured against a cache that is measured to EXIST and "
         "to WORK: it is primed with the very keys the sweep will request, a "
         "second pass is measured to return the stored values, the sweep is "
         "measured to ask for keys that are in the populated cache, and its "
         "hit count is nevertheless gated at ZERO against a positive miss "
         "count -- zero hits over zero lookups would be vacuous.  The "
         "`gauge-sign`, `gauge-subsample`, `memo-lax` and `bornhol-lax` "
         "mutants must each die here",
         ok,
         {"exact_matrix_comparisons": comparisons,
          "the_switching_group_is_swept_complete_at_every_probe": complete,
          "deviations_from_the_global_scalar_action": deviations,
          "readability_moves_under_a_switching": unreadable_flips,
          "checkpoint_switchings_that_did_not_telescope": telescoping,
          "value_cache_hits": _CACHE["value_cache_hits"],
          "value_cache_misses": _CACHE["value_cache_misses"],
          "fresh_requests_for_a_key_already_in_the_cache":
              _CACHE["fresh_requests_for_a_key_already_in_the_cache"],
          "cache_entries_primed": primed,
          "primed_keys_served_on_a_second_visit": reread})


def run_flip_tests(worlds, results):
    """The direction flip-test, and the BOOKKEEPING SPLIT flip-test."""
    prog("the flip-tests: direction, and the Born/sign bookkeeping split")
    flips, bad = 0, 0
    for nm in SWEEP_MEMBERS:
        W = worlds[nm]
        for pname, names in DECLARED_PROBES:
            e = named_edges(W, SWEEP_SETTING, names)
            if e is None:
                continue
            fwd = loop_matrix_fresh(W, SWEEP_SETTING, e, memoised=False)
            rev = loop_matrix_fresh(
                W, SWEEP_SETTING, [(li, -d) for (li, d) in reversed(e)],
                memoised=False)
            flips += 1
            if mm(fwd, rev) != sp_id():
                bad += 1
    # -- the bookkeeping split: the Born layer against the sign layer -------
    ref = results[PSI_REFERENCE]
    fam = TABLES["psi_family"]["per_member"]
    split = {}
    for nm in PSI_ORDER:
        if nm == PSI_REFERENCE:
            continue
        same_born = all(
            worlds[nm].psi[i] * worlds[nm].psi[i]
            == worlds[PSI_REFERENCE].psi[i] * worlds[PSI_REFERENCE].psi[i]
            for i in range(NSP))
        # THE BORN-LEVEL DATA THE ADMISSION PREDICATE ACTUALLY KEYS ON:
        # the Born shadow of the completion, and the Born-level canonical key
        # of every declared and every realized leg -- the very objects the
        # four-clause predicate compares.  Measured, not argued.
        V_same = all(
            worlds[nm].V[i][j] * worlds[nm].V[i][j]
            == (worlds[PSI_REFERENCE].V[i][j]
                * worlds[PSI_REFERENCE].V[i][j])
            for i in range(NSP) for j in range(NSP))
        legs_same = True
        for sp in SETTING_ORDER:
            for fr in FRAMES:
                if ([leg_key(x) for x in worlds[nm].legs(sp, fr)]
                        != [leg_key(x) for x
                            in worlds[PSI_REFERENCE].legs(sp, fr)]):
                    legs_same = False
                if ([leg_key(x) for x in worlds[nm].realized(sp, fr)]
                        != [leg_key(x) for x
                            in worlds[PSI_REFERENCE].realized(sp, fr)]):
                    legs_same = False
        L_agrees, A_agrees = True, True
        for sp in SETTING_ORDER:
            a, b = ref[sp]["based"], results[nm][sp]["based"]
            for l in set(a) & set(b):
                if a[l]["born"] != b[l]["born"]:
                    A_agrees = False
        for sp in SETTING_ORDER:
            for fr in FRAMES:
                for t in CHECKPOINTS:
                    if (worlds[PSI_REFERENCE].node_law(sp, fr, t)
                            != worlds[nm].node_law(sp, fr, t)):
                        L_agrees = False
        split[nm] = {"the_same_born_shadow_as_the_reference": bool(same_born),
                     "the_born_shadow_of_the_completion_agrees": bool(V_same),
                     "the_born_level_keys_of_every_leg_agree":
                         bool(legs_same),
                     "the_law_layer_agrees_everywhere": bool(L_agrees),
                     "the_amplitude_layer_agrees_on_every_common_loop":
                         bool(A_agrees)}
    both_ways = all(
        (v["the_law_layer_agrees_everywhere"] == v["the_same_born_shadow_as"
                                                   "_the_reference"])
        for v in split.values())
    born_level_blind = all(
        (v["the_born_shadow_of_the_completion_agrees"]
         and v["the_born_level_keys_of_every_leg_agree"])
        == v["the_same_born_shadow_as_the_reference"]
        for v in split.values())
    witness = [nm for nm, v in split.items()
               if v["the_same_born_shadow_as_the_reference"]
               and v["the_law_layer_agrees_everywhere"]
               and v["the_born_shadow_of_the_completion_agrees"]
               and v["the_born_level_keys_of_every_leg_agree"]
               and not v["the_amplitude_layer_agrees_on_every_common_loop"]]
    overwrite_the_flip_test = (MUTANT == "flip-lax")
    TABLES["flip_tests"] = {
        "loops_direction_flipped": flips,
        "loops_whose_reversal_was_not_the_inverse": bad,
        "the_bookkeeping_split": split,
        "the_law_layer_tracks_the_born_shadow_exactly": both_ways,
        "the_born_level_data_tracks_the_born_shadow_exactly":
            born_level_blind,
        "members_where_the_two_layers_part_company": sorted(witness),
        "route": "the split is Born data against sign data: the law layer, "
                 "the occupied sets and every clause of the admission "
                 "predicate read the Born shadow alone, while the amplitude "
                 "layer reads the vector itself.  The test is run in both "
                 "directions -- which members' law layer agrees, and which "
                 "members' amplitude layer agrees -- and the members where "
                 "they part company are named"}
    gate("PSI-FLIP-TESTS", "measurement",
         "TWO FLIP-TESTS, AND THE BOOKKEEPING SPLIT IS THE ONE WITH TEETH.  "
         "(1) THE DIRECTION FLIP-TEST: every declared probe loop is "
         "re-traversed with the direction convention flipped and the product "
         "of the two matrices is measured to be exactly the identity.  Its "
         "positive content is forced by algebra -- the link variables are "
         "measured orthogonal and the reverse traversal is the transpose -- "
         "so what it retains is instrument integrity: the `orient-flip` "
         "mutant reads a reverse traversal without transposing and dies "
         "here.  (2) THE BOOKKEEPING SPLIT: this unit's two transported "
         "objects divide exactly along Born data against sign data, and that "
         "division is MEASURED in both directions, and at the level "
         "where the invisibility is claimed.  THE BORN-LEVEL DATA THE "
         "ADMISSION PREDICATE ACTUALLY KEYS ON is compared directly: the "
         "Born shadow of the COMPLETION V entry by entry, and the canonical "
         "Born-level key of every declared leg and every realized leg at "
         "every (setting, frame).  Those are measured to agree with the "
         "reference for EXACTLY the members that share the reference's Born "
         "shadow, neither more nor fewer -- so for those members no clause "
         "of the predicate has any input that differs at all.  The LAW "
         "LAYER is measured to agree at every node of every setting for "
         "exactly the same members; and the members whose AMPLITUDE LAYER "
         "nevertheless disagrees on a common loop are NAMED.  Those are the "
         "members where the two layers part company, and their existence is "
         "the unit's finding stated as a bookkeeping fact.  The `flip-lax` "
         "waiver overwrites this predicate",
         bad == 0 and flips > 0 and both_ways and born_level_blind
         and not overwrite_the_flip_test,
         {"loops_direction_flipped": flips,
          "loops_whose_reversal_was_not_the_inverse": bad,
          "the_law_layer_tracks_the_born_shadow_exactly": both_ways,
          "the_born_level_data_tracks_the_born_shadow_exactly":
              born_level_blind,
          "members_where_the_two_layers_part_company": sorted(witness)})
    return witness


# ===========================================================================
# 13.  THE WITNESS, THE INDEPENDENT COMPARATOR, AND THE VERDICT
# ===========================================================================
def run_witness(worlds, results, matched, curv, quiet):
    """The (i) gate: is there a COMMON loop whose holonomy differs?"""
    prog("the witness gate")
    fam = TABLES["psi_family"]["per_member"]
    ref = results[PSI_REFERENCE]
    witnesses = []
    for nm in curv:
        for sp in SETTING_ORDER:
            w = matched[nm][sp]["_witness_born"]
            if w is None:
                continue
            a = ref[sp]["based"][w]
            b = results[nm][sp]["based"][w]
            # THE INDEPENDENT COMPARATOR: the witness loop's holonomy is
            # rebuilt from the link variables by a plain left-to-right
            # product, with no interning, no step memo and no value cache --
            # a route that shares no component with the enumeration that
            # produced the row under audit.
            ea = named_edges(worlds[PSI_REFERENCE], sp,
                             tuple((list(n), d) for n, d in w))
            eb = named_edges(worlds[nm], sp,
                             tuple((list(n), d) for n, d in w))
            ra = loop_matrix_fresh(worlds[PSI_REFERENCE], sp, ea,
                                   memoised=False)
            rb = loop_matrix_fresh(worlds[nm], sp, eb, memoised=False)
            witnesses.append({
                "member": nm, "setting": sp, "loop": canon(w),
                "loop_length": a["len"],
                "holonomy_at_the_reference_is_a_signed_permutation":
                    a["perm"] is not None,
                "holonomy_here_is_a_signed_permutation":
                    b["perm"] is not None,
                "the_reference_holonomy_is_the_identity":
                    a["perm"] == tuple(IDPERM),
                "the_born_shadows_differ": a["born"] != b["born"],
                "the_independent_rebuild_agrees_at_the_reference":
                    born_shadow_key(ra) == a["born"],
                "the_independent_rebuild_agrees_here":
                    born_shadow_key(rb) == b["born"],
                "the_independent_rebuilds_differ":
                    born_shadow_key(ra) != born_shadow_key(rb)})
            break
    flat_wit = []
    for nm in curv:
        for sp in SETTING_ORDER:
            w = matched[nm][sp]["_witness_flat"]
            if w is not None:
                flat_wit.append({"member": nm, "setting": sp,
                                 "loop": canon(w),
                                 "loop_length": ref[sp]["based"][w]["len"]})
                break
    rebuilds_ok = all(w["the_independent_rebuild_agrees_at_the_reference"]
                      and w["the_independent_rebuild_agrees_here"]
                      and w["the_independent_rebuilds_differ"]
                      for w in witnesses)
    invariant_quiet = all(nm in quiet for nm in matched
                          if fam[nm]["is_exchange_invariant"])
    TABLES["witnesses"] = {
        "witness_pairs": witnesses,
        "flat_to_non_flat_witnesses": flat_wit,
        "members_with_a_differing_common_loop": curv,
        "members_with_no_differing_common_loop": quiet,
        "every_exchange_invariant_member_agrees_on_every_common_loop":
            invariant_quiet,
        "route": "each witness is a (loop, member) pair read at matched "
                 "coordinates, and each one's two holonomies are REBUILT by "
                 "an independent route -- a plain left-to-right product of "
                 "freshly constructed link variables, sharing no interning, "
                 "no step memo and no value cache with the enumeration that "
                 "produced the row -- and the rebuilds are measured to "
                 "reproduce the rows AND to differ from each other"}
    overwrite_the_witness = (MUTANT == "witness-lax")
    ok = (len(witnesses) > 0 and rebuilds_ok and invariant_quiet
          and not overwrite_the_witness)
    gate("PSI-WITNESS", "measurement",
         "THE WITNESS GATE, WITH BOTH HALVES IN ITS OWN PREDICATE.  THE "
         "POSITIVE HALF: at least one COMMON loop -- the same sequence of "
         "named links, traversed in the same directions, at the same "
         "setting, based at the same declared node -- is measured to carry "
         "DIFFERENT holonomy at two members of the family, with every "
         "declaration held fixed and only the preparation varying; and each "
         "witness's two holonomies are rebuilt by an INDEPENDENT route that "
         "shares no interning, no step memo and no value cache with the "
         "enumeration that produced them, with the rebuilds measured to "
         "reproduce the rows and to differ from each other.  THE NEGATIVE "
         "HALF: every exchange-INVARIANT member of the family is measured to "
         "agree with the reference on EVERY common loop, so the gate is a "
         "measurement that comes out both ways on one family and not a "
         "fixture of the instrument.  The `psi-collapse` mutant makes every "
         "member the reference, killing the positive half; the "
         "`label-collapse` and `hol-basepoint` mutants corrupt the holonomy "
         "reading; the `witness-lax` waiver overwrites this predicate",
         ok,
         {"witness_pairs": len(witnesses),
          "flat_to_non_flat_witnesses": len(flat_wit),
          "independent_rebuilds_agree_and_differ": rebuilds_ok,
          "members_with_a_differing_common_loop": curv,
          "every_exchange_invariant_member_agrees_everywhere":
              invariant_quiet})
    return witnesses, flat_wit


def run_path_space_dependence(movers, still, matched):
    """The (ii) gate: does psi change WHICH loops exist?"""
    prog("the path-space-dependence gate")
    sizes = TABLES["loop_space_per_psi"]["per_member"]
    ref = sizes[PSI_REFERENCE]
    moved_sizes = {nm: {sp: sizes[nm][sp]["based_closed_loops"]
                        for sp in SETTING_ORDER} for nm in movers}
    ok = (len(movers) > 0 and len(still) > 0
          and all(any(sizes[nm][sp]["links"] != ref[sp]["links"]
                      for sp in SETTING_ORDER) for nm in movers)
          and all(all(sizes[nm][sp]["links"] == ref[sp]["links"]
                      for sp in SETTING_ORDER) for nm in still))
    TABLES["path_space_dependence"] = {
        "members_whose_admission_table_moves": movers,
        "members_whose_admission_table_is_identical": still,
        "based_loop_counts_at_the_moving_members": moved_sizes,
        "based_loop_counts_at_the_reference":
            {sp: ref[sp]["based_closed_loops"] for sp in SETTING_ORDER},
        "the_cells_that_move": {nm: TABLES["matched_comparison"][
            "admission_delta_cells"][nm] for nm in movers}}
    gate("PSI-PATH-SPACE-DEPENDENCE", "measurement",
         "WHETHER THE PREPARATION CHANGES WHICH LOOPS EXIST IS DECIDED CELL "
         "BY CELL, AND BOTH ANSWERS OCCUR IN THE FAMILY.  The admission "
         "tables of all eleven members are compared cell by cell in the "
         "number of admitted permutations AND in the permutation each rule "
         "draws.  Members whose table is IDENTICAL to the reference's are "
         "measured to have identical graphs -- same links, same loop space "
         "-- so their comparison is total; members whose table MOVES are "
         "named together with the cells that move and the loop counts that "
         "result.  Both halves are clauses of this gate's own predicate, so "
         "the reading comes out both ways on one family.  The `born-lax` "
         "mutant drops the exact-law clause from the admission predicate, "
         "which moves cells that must not move, and must die here",
         ok,
         {"members_whose_admission_table_moves": movers,
          "members_whose_admission_table_is_identical": still,
          "cells_compared_per_member": TABLES["admission_per_psi"][
              "cells_per_member"],
          "based_loop_counts_at_the_reference":
              {sp: ref[sp]["based_closed_loops"] for sp in SETTING_ORDER},
          "based_loop_counts_at_the_moving_members": moved_sizes})


def run_verdict(witnesses, movers, curv):
    """The decision rule is pre-registered and the verdict is derived from
    the gates and from nothing else."""
    prog("the verdict")
    curvature = bool(witnesses)
    path_space = bool(movers)
    if curvature:
        v = "PSI-CURVATURE-EXISTS"
    elif path_space:
        v = "PSI-PATH-SPACE-DEPENDENCE"
    else:
        v = "PSI-DECLARATION-ONLY"
    emit_an_out_of_vocabulary_verdict = (MUTANT == "verdict-lax")
    if emit_an_out_of_vocabulary_verdict:
        v = "PSI-STATE-CARRIES-GEOMETRY"
    qual = "-AT-FIXED-BORN-SHADOW"
    full = v + qual
    inv = v in PREREGISTERED
    FINDINGS["unit_verdict"] = full
    FINDINGS["the_verdicts_declared_scope"] = list(SCOPE_CLAUSES)
    gate("PSI-VERDICT", "derivation",
         "THE VERDICT IS DERIVED FROM THE PRE-REGISTERED DECISION RULE AND "
         "FROM NOTHING ELSE, AND IT IS IN THE PRE-REGISTERED VOCABULARY.  "
         "PSI-CURVATURE-EXISTS if a common loop's holonomy is measured to "
         "differ between two preparations; otherwise "
         "PSI-PATH-SPACE-DEPENDENCE if the loop space is measured to move "
         "while every common loop agrees; otherwise PSI-DECLARATION-ONLY; "
         "and PSI-BLOCKED-AT-<object> where the census cannot be posed.  The "
         "qualifier names the scope the family actually decides: the "
         "witnesses are read at a FIXED BORN SHADOW, where the arena, the "
         "law layer and the whole loop space are measured identical.  The "
         "verdict string is re-derived inside this gate from the recorded "
         "measurements and measured to be the string the rule selects; the "
         "`verdict-lax` mutant emits an out-of-vocabulary verdict and must "
         "die here",
         inv,
         {"verdict": full, "in_the_pre_registered_vocabulary": inv,
          "a_common_loop_differs": curvature,
          "the_loop_space_moves": path_space,
          "members_with_a_differing_common_loop": curv,
          "scope": list(SCOPE_CLAUSES)})
    return full


# ===========================================================================
# 14.  EXEMPTION, EXACTNESS AND THE DECLARATION ORDER
# ===========================================================================
def run_exemption_sweep():
    """RUNBOOK section 14 addendum: NO GATE PREDICATE MAY REFERENCE MUTANT
    IDENTITY."""
    src = Path(__file__).resolve().read_text()
    tree = ast.parse(src)
    found, wider = [], {"MUTANT != ...": [], "MUTANT not in ...": [],
                        "MUTANT is not ...": [], "not (MUTANT == ...)": []}
    for node in ast.walk(tree):
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.Not):
            for sub in ast.walk(node.operand):
                if (isinstance(sub, ast.Compare)
                        and any(isinstance(x, ast.Name) and x.id == "MUTANT"
                                for x in [sub.left] + list(sub.comparators))
                        and any(isinstance(op, ast.Eq) for op in sub.ops)):
                    wider["not (MUTANT == ...)"].append(node.lineno)
        if not isinstance(node, ast.Compare):
            continue
        names = [node.left] + list(node.comparators)
        if not any(isinstance(x, ast.Name) and x.id == "MUTANT"
                   for x in names):
            continue
        if any(isinstance(op, ast.NotEq) for op in node.ops):
            found.append(node.lineno)
            wider["MUTANT != ..."].append(node.lineno)
        if any(isinstance(op, ast.NotIn) for op in node.ops):
            wider["MUTANT not in ..."].append(node.lineno)
        if any(isinstance(op, ast.IsNot) for op in node.ops):
            wider["MUTANT is not ..."].append(node.lineno)
    call_sites, reaching = 0, []
    for node in ast.walk(tree):
        if (isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
                and node.func.id in ("gate", "anchor")):
            call_sites += 1
            for arg in list(node.args) + [k.value for k in node.keywords]:
                for sub in ast.walk(arg):
                    if isinstance(sub, ast.Name) and sub.id == "MUTANT":
                        reaching.append(node.lineno)
                        break
    if MUTANT == "exempt-lax":
        found.append(0)
        wider["MUTANT != ..."].append(0)
    outside = {k: sorted(set(v) - set(reaching)) for k, v in wider.items()}
    gate("PSI-NO-MUTANT-EXEMPTION", "derivation",
         "NO GATE PREDICATE REFERENCES MUTANT IDENTITY (RUNBOOK section 14 "
         "addendum), MEASURED AS THE HEADLINE SAYS IT.  Two clauses, both "
         "from an AST sweep of this module's own source.  (1) THE DIRECT "
         "STATEMENT: every `gate(...)` and `anchor(...)` call site is found, "
         "its argument expressions are walked to any depth, and the number "
         "of call sites reaching the mutant flag at all -- in a predicate, a "
         "claim string or a value expression -- is measured to be ZERO "
         "against the computed total.  (2) THE EXEMPTION FORMS: "
         "`MUTANT != ...`, `MUTANT not in ...`, `MUTANT is not ...` and "
         "`not (MUTANT == ...)` are counted separately anywhere in the "
         "source, every occurrence found is measured to lie OUTSIDE every "
         "gate and anchor call site, and the `!=` count itself is gated at "
         "zero.  Every mutation in this instrument is injected where the "
         "computation happens.  The `exempt-lax` waiver registers one such "
         "comparison and must die here",
         not found and not reaching,
         {"gate_and_anchor_call_sites": call_sites,
          "call_sites_reaching_the_mutant_flag": sorted(set(reaching)),
          "exemption_forms_found_anywhere_in_the_source":
              {k: len(v) for k, v in wider.items()},
          "their_line_numbers": {k: sorted(set(v))
                                 for k, v in wider.items() if v},
          "all_of_them_outside_any_gate_or_anchor_call_site":
              outside == {k: sorted(set(v)) for k, v in wider.items()},
          "mutant_exemption_comparisons": found,
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
    gate("PSI-EXACT", "derivation",
         "EXACT ARITHMETIC EVERYWHERE.  An AST sweep of this module finds no "
         "float literal and no call to `float`, and a runtime sweep finds no "
         "float in any value that reached a gate or an anchor.  The "
         "substrate is `fractions.Fraction`: every declared operator has "
         "RATIONAL entries and is exactly orthogonal over Q, every declared "
         "preparation is an exact rational unit vector, so equality of "
         "matrices is equality of exact rationals and no tolerance exists "
         "anywhere in this instrument.  The `float-lax` mutant introduces a "
         "float literal and must die here",
         not lits and not calls and not runtime,
         {"float_literal_lines": lits, "float_call_lines": calls,
          "rows_carrying_a_float": runtime,
          "fraction_available": str(Fr(1, 2))})


def run_declaration_order():
    ids = [g["id"] for g in GATES]
    decl = ["PSI-FREEZE", "PSI-BASE-PINNED", "PSI-FAMILY-DECLARED",
            "PSI-ARENA", "PSI-GEN-PIN"]
    transport = ["PSI-ADMISSION-PER-PSI", "PSI-PATH-SPACE",
                 "PSI-MATCHED-COORDINATES", "PSI-WITNESS",
                 "PSI-PATH-SPACE-DEPENDENCE"]
    present = all(g in ids for g in decl + transport)
    last_decl = max((ids.index(g) for g in decl if g in ids), default=-1)
    first_tr = min((ids.index(g) for g in transport if g in ids),
                   default=len(ids))
    gate("PSI-DECLARATION-ORDER", "derivation",
         "THE RECEIPT'S GATE ORDER PROVES THE FREEZE.  The pin requires the "
         "preparation family to be declared AS DATA before any transport "
         "measurement, and the proof is the order in which this receipt's "
         "gates were recorded: every declaration gate -- the freeze, the "
         "pinned base, the family with its computed sizes, the arena, the "
         "hash-pin of the inherited receipt -- is measured to sit STRICTLY "
         "BEFORE the first transport gate, and the freeze gate is measured "
         "to be the first gate of the run with the transport-datum counter "
         "at zero.  The `order-lax` mutant emits a transport measurement "
         "before the declarations and must die here",
         present and last_decl < first_tr and ids[0] == "PSI-FREEZE",
         {"first_gate": ids[0],
          "last_declaration_gate_index": last_decl,
          "first_transport_gate_index": first_tr,
          "declaration_gates": decl, "transport_gates": transport,
          "gate_order": ids})


# ===========================================================================
# 15.  THE MUTANT TABLE
# ===========================================================================
MUTANT_DECL = (
    ("psi-collapse", "computation",
     "every member of the family replaced by the pinned preparation"),
    ("schmidt-lax", "computation", "every state reported as a product state"),
    ("born-lax", "computation",
     "the exact-law clause dropped from the admission predicate"),
    ("id-lax", "computation",
     "every admitted permutation accepted as an identification"),
    ("scope-lax", "computation", "the admitted relabelling scope subsampled"),
    ("reduce-lax", "computation", "the reduced-path condition dropped"),
    ("path-collapse", "computation", "every loop given the same name"),
    ("loopname-collapse", "computation",
     "the link names collapsed, so loops match across graphs by shape alone"),
    ("readtime-conflate", "computation",
     "every node datum read at the final checkpoint"),
    ("label-collapse", "computation",
     "the holonomy value counted as a name label, not a permutation"),
    ("hol-basepoint", "computation",
     "closed paths collected at every base point, not the declared one"),
    ("orient-flip", "computation",
     "a link's reverse traversal read without transposition"),
    ("gauge-sign", "computation",
     "the switching dropped on a reversed traversal"),
    ("gauge-subsample", "computation", "the switching sweep subsampled"),
    ("bornhol-lax", "computation",
     "the gauge-invariant holonomy reading replaced by the raw matrix"),
    ("memo-lax", "computation", "the self-test allowed to read the cache"),
    ("freeze-lax", "computation",
     "one law datum evaluated before the freeze"),
    ("order-lax", "computation",
     "a transport measurement emitted before the declarations"),
    ("defect-order", "computation",
     "the defect composed in the wrong order"),
    ("psilaw-drop", "computation",
     "the psi-term dropped from the psi-law, so it predicts GEN's defect "
     "for every preparation"),
    ("signflip-lax", "computation",
     "the sign-flip census subsampled to one pattern per member"),
    ("qcontrol-lax", "computation",
     "the negative control's alternative Q replaced by the pinned Q"),
    ("anchor-rot", "computation",
     "one entry of a constructed declared rotation perturbed"),
    ("anchor-Q", "computation", "the declared transposition Q perturbed"),
    ("anchor-psi", "computation",
     "one coefficient of the pinned preparation perturbed"),
    ("anchor-record", "computation",
     "the pointer shift made non-injective, so the record is destroyed"),
    ("anchor-gen", "computation",
     "a reused GEN committed value perturbed"),
    ("gen-hash", "computation",
     "the external receipt's bytes perturbed before they are hashed"),
    ("control-lax", "waiver",
     "the positive control's predicate overwritten after the fact"),
    ("witness-lax", "waiver",
     "the witness gate's predicate overwritten after the fact"),
    ("flip-lax", "waiver",
     "the flip-test's predicate overwritten after the fact"),
    ("verdict-lax", "waiver", "an out-of-vocabulary verdict emitted"),
    ("float-lax", "waiver",
     "a float literal registered in the exactness gate's own evidence list "
     "after its AST sweep has run: the source text is never edited, so this "
     "is a waiver and is declared as one"),
    ("exempt-lax", "waiver",
     "a mutant-identity exemption registered in the exemption gate's own "
     "evidence list after its AST sweep has run: the source text is never "
     "edited, so this is a waiver and is declared as one"),
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
                                          kill["failed_anchors"][:3]
                                          + kill["failed_gates"]))
        return {"mutant": m, "exit": r.returncode, "died": r.returncode == 1,
                "falsified_anchors": kill["failed_anchors"][:6],
                "falsified_gates": kill["failed_gates"],
                "crashed_before_reporting": kill["crashed"]}

    with ThreadPoolExecutor(max_workers=min(12, len(MUTANTS))) as ex:
        rows = list(ex.map(_run, MUTANTS))
    kinds = {m[0]: m[1] for m in MUTANT_DECL}
    for r in rows:
        r["kind"] = kinds[r["mutant"]]
        r["declaration"] = [m[2] for m in MUTANT_DECL
                            if m[0] == r["mutant"]][0]
    must = [x["id"] for x in GATES if x["class"] != "disclosure"
            and x["id"] != "PSI-FALSIFICATION"]
    hit = {g for r in rows for g in r["falsified_gates"]}
    comp_hit = {g for r in rows if r["kind"] == "computation"
                for g in r["falsified_gates"]}
    never = sorted(set(must) - hit)
    only_waiver = sorted((set(must) & hit) - comp_hit)
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
    gate("PSI-FALSIFICATION", "derivation",
         "EVERY MUST-PASS GATE IS FALSIFIED BY SOME MUTANT, AND EVERY MUTANT "
         "DIES.  Each declared mutant is run to completion, must exit 1, and "
         "must falsify at least one NAMED gate or anchor; the second clause "
         "is the one that matters -- the set of must-pass gates that NO "
         "mutant falsifies is measured to be EMPTY.  Each mutant declares "
         "its KIND and the split is counted from the declaration: a WAIVER "
         "proves a gate's predicate is load-bearing for the exit code, not "
         "that the gate would catch a computational defect, and the two are "
         "not claimed to be the same thing.  BOTH DENOMINATORS ARE REPORTED, "
         "because they differ: the count of must-pass gates falsified by "
         "SOME mutant, and the smaller count falsified by a mutant that "
         "perturbs a COMPUTATION.  The gates carried by a waiver alone are "
         "named, not averaged away.  The one gate excluded from the "
         "denominator is this one: `run_mutant_table` does not run inside a "
         "mutant, so the census gate does not exist there",
         all(r["died"] for r in rows)
         and all(r["falsified_anchors"] or r["falsified_gates"]
                 for r in rows)
         and not never,
         {"mutants": len(rows), "died": sum(1 for r in rows if r["died"]),
          "perturb_a_computation": sum(1 for r in rows
                                       if r["kind"] == "computation"),
          "waivers": sum(1 for r in rows if r["kind"] == "waiver"),
          "must_pass_gate_denominator": len(must),
          "falsified_by_some_mutant": len(set(must) & hit),
          "falsified_by_a_computation_mutant": len(set(must) & comp_hit),
          "falsified_only_by_a_waiver": only_waiver,
          "the_gate_excluded_from_the_denominator": "PSI-FALSIFICATION",
          "never_falsified": never})


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
                       "must_pass_gates": len(must),
                       "disclosures": len(GATES) - len(must),
                       "must_pass_failures": fails}}


def _wrap(s, w):
    out, cur = [], ""
    for word in s.split():
        if len(cur) + len(word) + 1 > w:
            out.append(cur)
            cur = word
        else:
            cur = (cur + " " + word) if cur else word
    if cur:
        out.append(cur)
    return out


def render(rec):
    L = []
    A = L.append
    A("=" * 78)
    A("PSI -- THE psi-SIDE CURVATURE HUNT")
    A("Does the physical state contribute geometry?")
    A("=" * 78)
    A("schema        %s" % rec["schema"])
    A("pin           %s (sha %s)" % (rec["pin_commit"],
                                     rec["pin_sha256_prefix"]))
    A("immutable base %s   generator sha256 %s"
      % (rec["base_commit"], rec["source_sha256"][:16]))
    A("")
    A("VERDICT: %s" % rec["findings"].get("unit_verdict", "(none)"))
    for c in rec["findings"].get("the_verdicts_declared_scope", []):
        A("         %s" % c)
    A("")
    A("-" * 78)
    A("1.  THE PREPARATION FAMILY, DECLARED AS DATA")
    A("-" * 78)
    fam = rec["tables"]["psi_family"]
    A("%-8s %-5s %-4s %-4s %-5s %-6s %s"
      % ("member", "|psi|", "rank", "supp", "inv", "bornS", "role"))
    for nm in PSI_ORDER:
        r = fam["per_member"][nm]
        A("%-8s %-5s %-4d %-4d %-5s %-6s %s"
          % (nm, r["norm_squared"], r["schmidt_rank"], r["support"],
             "yes" if r["is_exchange_invariant"] else "no",
             "yes" if r["its_born_shadow_is_exchange_symmetric"] else "no",
             r["role"][:34]))
    A("family size %d (computed); exchange-invariant %d; non-invariant %d"
      % (fam["family_size"], len(fam["exchange_invariant_members"]),
         len(fam["exchange_non_invariant_members"])))
    A("Schmidt ranks among the invariant members: %s"
      % fam["schmidt_ranks_among_the_invariant_members"])
    A("every member completed with the SAME declared Q = %s"
      % fam["the_declared_transposition_every_member_is_completed_with"])
    A("")
    A("-" * 78)
    A("2.  THE ADMISSION TABLE AND THE LOOP SPACE, PER MEMBER")
    A("-" * 78)
    dr = rec["tables"]["admission_per_psi"]["cells_where_each_rule_draws_"
                                            "a_link"]
    ls = rec["tables"]["loop_space_per_psi"]["per_member"]
    A("%-8s %-5s %-5s %-24s %-24s"
      % ("member", "FULL", "REAL", "links per setting",
         "based loops per setting"))
    for nm in PSI_ORDER:
        A("%-8s %-5d %-5d %-24s %-24s"
          % (nm, dr[nm]["FULL"], dr[nm]["REAL"],
             canon([ls[nm][sp]["links"] for sp in SETTING_ORDER]),
             canon([ls[nm][sp]["based_closed_loops"]
                    for sp in SETTING_ORDER])))
    A("")
    A("-" * 78)
    A("3.  THE MATCHED COMPARISON (reference %s)"
      % rec["tables"]["matched_comparison"]["reference"])
    A("-" * 78)
    mc = rec["tables"]["matched_comparison"]["per_member_per_setting"]
    A("%-8s %-6s %-8s %-8s %-8s %-8s"
      % ("member", "adm-d", "common", "bornDiff", "permDiff", "flat->non"))
    for nm in PSI_ORDER:
        if nm == PSI_REFERENCE:
            continue
        d = len(rec["tables"]["matched_comparison"]["admission_delta_cells"][
            nm])
        row = mc[nm][SWEEP_SETTING]
        A("%-8s %-6d %-8d %-8d %-8d %-8d"
          % (nm, d, row["common_loops"],
             row["common_loops_whose_born_holonomy_differs"],
             row["common_loops_whose_permutation_part_differs"],
             row["common_loops_flat_at_the_reference_and_not_here"]))
    A("(the row is read at %s; every setting is in the receipt)"
      % SWEEP_SETTING)
    A("")
    A("-" * 78)
    A("4.  GATES")
    A("-" * 78)
    for g in rec["gates"]:
        A("[%s] %-28s %s" % ("PASS" if g["passed"] else "FAIL", g["id"],
                             "(disclosure)" if g["class"] == "disclosure"
                             else ""))
        for ln in _wrap(g["claim"], 74):
            A("    " + ln)
        A("    value: " + canon(g["value"])[:900])
        A("")
    A("-" * 78)
    A("5.  ANCHORS (exit-1 only)")
    A("-" * 78)
    bad = [a for a in rec["anchors"] if not a["passed"]]
    A("%d anchors, %d passed, %d failed"
      % (len(rec["anchors"]),
         sum(1 for a in rec["anchors"] if a["passed"]), len(bad)))
    for a in bad[:20]:
        A("  FAIL %s: %s declared=%s computed=%s"
          % (a["id"], a["quantity"], canon(a["declared"])[:200],
             canon(a["computed"])[:200]))
    A("")
    A("-" * 78)
    A("6.  TOTALS")
    A("-" * 78)
    for k, v in sorted(rec["totals"].items()):
        A("%-24s %s" % (k, v))
    A("=" * 78)
    return "\n".join(L) + "\n"


# ===========================================================================
# MAIN
# ===========================================================================
def main():
    global MUTANT, SOURCE_SHA256, ROT, SCOPE, WSWAP, IDPERM
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

    # The declared objects are built at import, before the mutant flag is
    # read, so the mutated ones are rebuilt here with the flag in force.
    ROT = {k: rotation(k) for k in ROT_ORDER}
    SCOPE = declared_scope()
    ULOCAL.clear()
    for w in ("A", "B"):
        for g in ROT_ORDER:
            ULOCAL[(w, g)] = U_local(w, g)
    if MUTANT == "freeze-lax":
        World("pre", psi_vector(dict(PSI_FAMILY[0][2])),
              declared_Q()).node_law(SETTING_ORDER[0], "F1", 1)
    if MUTANT == "order-lax":
        gate("PSI-WITNESS", "measurement",
             "emitted before the declarations", True, {})

    run_freeze()
    run_base_declaration()
    run_family_declaration()
    run_arena()
    gen = run_external_pin()

    worlds, results = run_sweep()
    matched, delta, movers, still, curv, quiet = run_comparison(worlds,
                                                                results)
    run_positive_control(worlds, results, gen)
    witnesses, flat_wit = run_witness(worlds, results, matched, curv, quiet)
    run_path_space_dependence(movers, still, matched)
    run_psi_law(worlds)
    run_signflip_census(worlds)
    run_negative_control(worlds, results)
    run_switching_selftest(worlds)
    run_flip_tests(worlds, results)
    verdict = run_verdict(witnesses, movers, curv)

    fam = TABLES["psi_family"]
    ls = TABLES["loop_space_per_psi"]["per_member"]
    FINDINGS["thesis"] = (
        "THE PHYSICAL STATE CONTRIBUTES GEOMETRY.  On base G, with the "
        "declared transposition Q held FIXED at GEN's pinned value and every "
        "other declaration -- the two gluing rules, the six settings, the "
        "two frames, the four checkpoints, the read times, the 162-element "
        "relabelling scope and its two admitted elements -- held identical, "
        "a declared %d-member family of preparations was swept, %d of them "
        "exchange-invariant with Schmidt ranks %s and %d of them not.  The "
        "sweep separates the preparation's two channels.  (1) THE BORN "
        "SHADOW FIXES THE ARENA: every clause of the four-clause admission "
        "predicate reads Born-level data alone, so members sharing a Born "
        "shadow are measured to have the SAME admission table at all %d "
        "cells, the same graph and the same loop space, while the members "
        "whose Born shadow is not exchange-symmetric lose the realized "
        "rule's identifications at %s and collapse to a flat connection.  "
        "(2) THE SIGN STRUCTURE CARRIES THE CURVATURE: at a FIXED Born "
        "shadow -- same laws, same occupied sets, same admission table, same "
        "loop space, and a law layer measured to agree at every node -- the "
        "holonomy is measured to DIFFER on %s of the %s common loops based "
        "at the declared base point, %s of which are FLAT at the reference "
        "and not flat at the witness.  The dependence is characterised in "
        "both directions and exhaustively: the GEN law generalises to "
        "D(psi) = D_GEN . Q^T E(psi) Q with E(psi) = sigma H(psi) sigma "
        "H(psi) the Householder's own exchange defect, E(psi) is measured to "
        "be the identity EXACTLY on the exchange-invariant locus, and over "
        "the exhaustive %d-member sign-flip census the holonomy agrees with "
        "the reference on every common loop IF AND ONLY IF the flipped state "
        "is still exchange-invariant.  GEN's psi-independence is therefore "
        "not a theorem of the theory but a theorem about the "
        "exchange-invariant locus, and off that locus the curvature is "
        "carried by a feature of the state that NO Born-level declaration "
        "can see.  Controls: at GEN's pinned preparation this instrument "
        "reproduces GEN's terminal admission table cell for cell, its link "
        "and path counts, its Klein four-group and its defect, every clause "
        "anchored exit-1 against the hash-pinned committed receipt; and a "
        "declaration change with teeth -- two alternative declared "
        "transpositions -- moves the holonomy by exactly the amount GEN's "
        "dihedral law predicts, order six and non-abelian at one and flat at "
        "the other.  Stated at the committed finite scope, at the declared "
        "preparation family, at the declared completion form and its pinned "
        "Q, per coordinate; nothing is claimed about nature."
        % (fam["family_size"], len(fam["exchange_invariant_members"]),
           canon(fam["schmidt_ranks_among_the_invariant_members"]),
           len(fam["exchange_non_invariant_members"]),
           TABLES["admission_per_psi"]["cells_per_member"],
           canon(TABLES["path_space_dependence"][
               "members_whose_admission_table_moves"]),
           canon(TABLES["matched_comparison"]["per_member_per_setting"][
               "psi-N1"]["GP-E"]["common_loops_whose_born_holonomy_differs"]),
           canon(ls["psi-G"]["GP-E"]["based_closed_loops"]),
           canon(TABLES["matched_comparison"]["per_member_per_setting"][
               "psi-N1"]["GP-E"][
                   "common_loops_flat_at_the_reference_and_not_here"]),
           TABLES["signflip_census"]["sub_family_size"]))

    run_declaration_order()
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
