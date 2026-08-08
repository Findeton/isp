#!/usr/bin/env python3
"""GEN -- THE GENERALITY CHECK: THE NT GEOMETRY ON A SECOND BASE.

Executes the frozen pin `v13/note-gen-generality-pin.md` (sha 0da6205815a6,
commit 5e8bc58) against the immutable base fceb614 (NT TERMINAL, v13 LOG
#211).

THE QUESTION.  Is the NT geometry a property of THE THEORY or of the one
committed W6 base?  This unit CONSTRUCTS A SECOND BASE -- same structural
species, genuinely different flesh -- and re-measures the five
pre-registered patterns on it.

BASE G, DECLARED AS DATA BEFORE ANY TRANSPORT MEASUREMENT.  Two wings, a
preparation, commuting local legs on the wings, records at the final
division event -- the species.  The flesh is new at every coordinate:

  * the system on each wing is a QUTRIT, not a qubit: the carrier has 81
    configurations (s_A, s_B, p_A, p_B) with s in {0,1,2} and a
    three-state pointer per wing, against the first base's 36;
  * every measurement has THREE outcomes, and the pointer records the
    outcome by a cyclic shift, so the record is the pointer value itself;
  * the arithmetic is the RATIONALS: every declared operator is exactly
    orthogonal over Q, where the first base needed the totally real
    quartic field Q(cos pi/8).  The measurement bases are the columns of
    RATIONAL rotation matrices built from integer quaternions by
    Euler-Rodrigues, in two different coordinate planes;
  * the PREPARATION is different and its ORTHOGONAL COMPLETION IS PINNED
    EXPLICITLY AS DATA (the completion-relativity lesson made structural:
    the full 9x9 matrix is typed in this file as the declaration and the
    constructed one is anchored against it, entry by entry).  It is the
    Householder reflection carrying the initial system state to a declared
    entangled qutrit vector, composed with a declared basis transposition
    -- and the transposition is load-bearing, which this unit MEASURES
    rather than assumes (the declared completion flip-test).

Every count of every declared collection -- the setting family, the
admitted relabelling group, its declared extension, the checkpoint-phase
switching group, the node/link/path counts, the group orders -- is
COMPUTED by enumeration in this file and never typed.

THE FIVE PRE-REGISTERED PATTERNS, EACH GATED SEPARATELY.
  P1  a nontrivial holonomy group exists (some closed loop non-flat).
  P2  the group COMPUTED, whatever it is: permutation-tuple counting,
      never labels; closure measured; order and structure named -- AT
      THE DECLARED COMPLETION, which the census of section 14 measures
      to select the isomorphism type.
  P3  TWO curvature sources -- identification multiplicity (isolated by
      running the single-rule sub-connections separately) and the
      COMPLETION'S NON-EQUIVARIANCE DEFECT D = P_W U_prep^-1 P_W U_prep
      -- each exhibited or its absence measured.
  P4  that defect is an ELEMENT of the holonomy group.
  P5  non-principality: membership of every holonomy element in every
      declared and admitted collection, computed.

THE COMPLETION CENSUS (the unit's central result, section 14).  The
defect obeys an exact law, derived here and gated two ways:

    D = (Sigma V^T Sigma V) (x) I_9      (any orthogonal completion V)
      = (Sigma Q^T Sigma Q) (x) I_9      (V = H . Q, psi exchange-invariant)

-- the Householder CANCELS IDENTICALLY, so D DOES NOT DEPEND ON psi: it
is manufactured by the declared transposition alone.  Both curvature
sources are therefore DECLARATION-side at this base.  The law reduces
the whole completion question to 9x9 and the family V = H . Q with Q a
permutation of the nine system-pair indices fixing the first is swept
EXHAUSTIVELY: all 8! = 40,320 members.  Geometry is GENERIC (the
exceptions are exactly the exchange-equivariant locus), the GROUP is
completion-selected, and the family is dihedral:

    Hol = < W, D | W^2 = D^n = 1, W D W = D^-1 >,  n = ord(D).

The 28-member sub-family of the pinned completion's own declared form
(a single basis transposition) is REBUILT IN FULL, and so is the
lexicographically first member of every measured class -- one class
per (order of the defect, fixed configurations of the defect).

DISCIPLINE.  RUNBOOK section 14 with every addendum: the switching
sweep evaluates FRESH against a POPULATED cache whose read path is
exercised and gated (a zero-hit count over zero lookups is vacuous);
every rebuild/decomposition check builds its comparator INDEPENDENTLY
of the component under audit (the record decomposition is rebuilt from
the PINNED rotations and an independently declared shift table);
analytically-forced clauses are DISCLOSURES and not must-pass gates;
the symmetry instrument is self-tested under its own action and the
mutant table carries sign/orientation perturbations.

CONTROLS.  Positive: a same-order path pair that MUST agree -- frame 1's
leg order against frame 2's, the two legs measured to commute -- and the
closed loop it forms.  Negative, with teeth: a deliberately twisted
comparator, the canonical loop with one identification replaced by the
wing exchange where the base supplies the identity; if it does not show
holonomy the instrument is dead and the run says so.

NO GATE PREDICATE REFERENCES MUTANT IDENTITY: every mutation is
injected where the computation happens; an AST sweep measures that no
`gate(...)` or `anchor(...)` call site reaches the mutant flag at all,
and that the exemption comparison forms are absent from the module.
RUNBOOK section 15 with every addendum: the arena is declared as data
with sizes computed, and the READ TIME is a declared coordinate of
every node and of the law datum, so two data read at different
checkpoints can never compare equal.

Exact arithmetic throughout: `fractions.Fraction` only.  No float enters
any path.  Anchors exit 1 on mismatch.  No wall-clock value enters the
receipt or the rendered output, so two delivery-mode runs are
byte-identical.

Scope: finite; ONE declared carrier of 81 configurations; a declared
six-setting family; two declared frames; four declared checkpoints; a
declared 162-element relabelling scope and its declared 216-element
extension.  No locality, topology, causality, spacetime, field, QFT or
gravity object is constructed or claimed.  Nothing is claimed about
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

SCHEMA = "gen-generality-receipt-v1"
PIN_SHA256 = "0da6205815a6"
PIN_COMMIT = "5e8bc58"
BASE_COMMIT = "fceb614"
NT_RECEIPT = HERE / "nt_transport_receipt.json"
OUT_TXT = HERE / "gen_generality_output.txt"
OUT_JSON = HERE / "gen_generality_receipt.json"

MUTANT: str | None = None
SOURCE_SHA256 = ""

GATES: list[dict] = []
ANCHORS: list[dict] = []
TABLES: dict = {}
FINDINGS: dict = {}

PREREGISTERED = ("GEN-STRUCTURE-REPRODUCES", "GEN-STRUCTURE-VARIES-",
                 "GEN-STRUCTURE-ABSENT", "GEN-BLOCKED-AT-")

# The QUALIFIER slot of the pre-registered UNIT-OUTCOME(-QUALIFIER) form.
# The completion is arena data by the pin's own terms, and the census of
# section 14 measures that a different declared completion of the very same
# preparation vector returns a different pre-registered outcome, so the
# scope the qualifier names is the one parameter that moves the outcome.
QUALIFIER = "-AT-DECLARED-COMPLETION"
SCOPE_CLAUSES = ("at the committed finite scope",
                 "at the declared admission scope",
                 "at the declared completion",
                 "per coordinate")

T0 = time.time()

# The freeze counter (RUNBOOK 13(4)): no transport datum may be evaluated
# before the base declaration is recorded.
_FROZEN = False
_FEVALS = 0

# Fresh-evaluation bookkeeping (RUNBOOK section 14 addendum, both halves:
# the self-test must evaluate fresh, AND the cache path must be measured to
# be EXERCISED -- zero hits over zero lookups is vacuous).
_FRESH = False
_CACHE = {"value_cache_hits": 0, "value_cache_misses": 0,
          "value_cache_lookups": 0, "value_cache_writes": 0,
          "cache_reads_that_returned_a_stored_value": 0,
          "fresh_requests_for_a_key_already_in_the_cache": 0}
_MEMO: dict = {}


def prog(msg: str) -> None:
    """Progress line; stderr only, so no wall-clock reaches any artifact."""
    sys.stderr.write("[gen %6.1fs] %s\n" % (time.time() - T0, msg))
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
    """The instrument's ONLY transported-value cache.  Bypassed entirely in
    fresh mode, where the hit count is gated at zero; the `memo-lax` mutant
    lets the self-test read the cache and must die there.  The mutation is
    injected HERE, in the computation; no gate predicate names it.

    The bookkeeping is what makes the zero-hit reading a MEASUREMENT
    rather than a vacuity: the cache is PRIMED before the self-test with
    the very keys the self-test will request, the priming phase's own
    re-read is counted (so the read path is measured to work), and every
    fresh-mode request for a key that IS in the cache is counted -- so the
    self-test's zero hits are zero hits against a populated cache that was
    asked for its entries and refused to serve them."""
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
# 1.  BASE G -- THE SECOND BASE, DECLARED AS DATA
#
#     Everything in this section is a DECLARATION.  The pinned matrices are
#     typed here as the unit's own committed data and the constructed ones
#     are anchored against them entry by entry (section 3), so a drift in
#     any constructor kills the run loudly.  Every COUNT below is computed
#     by enumeration, never typed.
# ===========================================================================
ZERO, ONE = Fr(0), Fr(1)

NS = 3                          # the system dimension on each wing: a QUTRIT
NP = 3                          # the pointer states per wing: 0 = ready
NC = NS * NS * NP * NP          # the carrier, computed
J0 = 0                          # the initial configuration (0, 0, 0, 0)


def idx(sa, sb, pa, pb):
    return ((sa * NS + sb) * NP + pa) * NP + pb


def unidx(i):
    pb = i % NP
    pa = (i // NP) % NP
    sb = (i // (NP * NP)) % NS
    sa = i // (NP * NP * NS)
    return sa, sb, pa, pb


# -- the declared measurement family: integer quaternions -------------------
#    R0 is the computational-basis measurement; R1 rotates the (1,2)
#    coordinate plane by the 3-4-5 angle; R2 rotates the (0,1) plane by the
#    5-12-13 angle.  Two different planes, so the family is genuinely
#    three-dimensional and not one plane rotation with a spectator.
QUATERNIONS = {"R0": (1, 0, 0, 0), "R1": (2, 1, 0, 0), "R2": (3, 0, 0, 2)}
ROT_ORDER = ["R0", "R1", "R2"]

# THE PINNED ROTATION MATRICES (declared data; constructed and anchored).
PINNED_ROT = {
    "R0": [["1", "0", "0"], ["0", "1", "0"], ["0", "0", "1"]],
    "R1": [["1", "0", "0"], ["0", "3/5", "-4/5"], ["0", "4/5", "3/5"]],
    "R2": [["5/13", "-12/13", "0"], ["12/13", "5/13", "0"], ["0", "0", "1"]],
}

# THE DECLARED OUTCOME-TO-SHIFT TABLE.  Declared data, typed here, and used
# ONLY by the independent comparator of the record decomposition (section 3):
# the constructor reads `pointer_shift`, the comparator reads THIS, so a
# perturbation of the constructor moves one side of the comparison and not
# the other (RUNBOOK section 14 addendum: a rebuild check must construct its
# comparator independently of the component under audit).
SHIFT_DECLARED = (0, 1, 2)

# -- the declared preparation ----------------------------------------------
#    psi is an entangled qutrit-pair vector: invariant under the exchange of
#    the two systems, of Schmidt rank three, with UNEQUAL Schmidt
#    coefficients (2/3, 2/3, 1/3).  The first base's preparation vector is
#    the singlet: ANTI-invariant, of Schmidt rank two, with equal
#    coefficients.  What the two share is the property the species needs --
#    the Born shadow of the preparation column is invariant under the wing
#    exchange -- and nothing else.
PSI_COEFF = {(0, 1): "2/3", (1, 0): "2/3", (2, 2): "1/3"}

# THE DECLARED COMPLETION.  V = H . Q, with H the Householder reflection
# carrying e_{(0,0)} to psi and Q the transposition of the system-pair basis
# states (0,1) and (0,2), which fixes (0,0) so that V e_{(0,0)} = psi still.
# Q is what makes |V| fail to be exchange-symmetric, and that is exactly
# what makes the FULL-leg rule admit the identity UNIQUELY.  It is declared,
# printed in full, and its alternative (Q = the identity, i.e. the bare
# Householder completion) is MEASURED in the declared completion flip-test.
Q_COMPLETION = [0, 2, 1, 3, 4, 5, 6, 7, 8]

# THE PINNED COMPLETION MATRIX V, 9x9, in the system-pair basis ordered
# (0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2).  Column 0
# is psi.  This is the unit's committed declaration of the preparation; the
# constructor is anchored against it entry by entry (A03).
PINNED_V = [
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

# -- the declared setting family -------------------------------------------
SETTINGS = {"GP-A": ("R0", "R1"), "GP-B": ("R0", "R2"),
            "GP-C": ("R1", "R2"), "GP-D": ("R2", "R1"),
            "GP-E": ("R0", "R0"), "GP-F": ("R1", "R1")}
SETTING_ORDER = ["GP-A", "GP-B", "GP-C", "GP-D", "GP-E", "GP-F"]

FRAMES = ("F1", "F2")

# -- the declared transported objects and gluing rules ----------------------
OBJECTS = (
    ("L", "the law's restriction to the context",
     "the occupied support and the exact law at the node's DECLARED READ "
     "TIME, which is carried inside the datum",
     "legs act by the declared one-step Born transition (its transpose in "
     "reverse); identifications act by the admitted permutation"),
    ("A", "the amplitude layer, closed-loop form",
     "the ordered product of link variables around a closed loop",
     "legs contribute the leg operator (its inverse in reverse); "
     "identifications contribute the permutation matrix"),
)

ID_RULES = (
    {"id": "FULL", "name": "FULL-DECLARED-LEGS",
     "definition":
         "the corridor-bound rule matching the FULL declared legs "
         "order-free at the Born level: an identification at checkpoint t "
         "is admitted iff exactly one permutation of the admitted scope "
         "carries j0 to j0, carries frame 2's full declared legs onto "
         "frame 1's, carries frame 2's occupied set at t onto frame 1's, "
         "and carries frame 2's exact law at t onto frame 1's",
     "legs": "declared"},
    {"id": "REAL", "name": "REALIZED-ONLY",
     "definition":
         "the same four-clause predicate with each leg restricted to the "
         "configurations the process actually occupies before and after it",
     "legs": "realized"},
)

PROBES = ("the canonical loop", "the aligned-prefix bigon",
          "the prefix-crossing loop", "the twisted comparator")


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


ROT = {k: rotation(k) for k in ROT_ORDER}

PSI = [ZERO] * (NS * NS)
for (_a, _b), _v in PSI_COEFF.items():
    PSI[_a * NS + _b] = parse_fr(_v)

# the system-pair exchange, as a permutation of the 9 system-pair indices
SIGMA9 = [(b * NS + a) for a in range(NS) for b in range(NS)]


def householder():
    """H = I - 2 w w^T / (w.w) with w = psi - e_{(0,0)}: the reflection that
    carries the initial system state exactly onto the declared preparation
    vector.  Symmetric, orthogonal and involutive."""
    w = list(PSI)
    w[0] = w[0] - ONE
    ww = sum(v * v for v in w)
    return [[(ONE if i == j else ZERO) - 2 * w[i] * w[j] / ww
             for j in range(NS * NS)] for i in range(NS * NS)]


def completion():
    """V = H . Q: the DECLARED orthogonal completion of the preparation.
    Column j of V is column Q(j) of H, so column 0 is psi and the remaining
    eight columns are the declared completion, printed in full."""
    H = householder()
    perturb_the_constructed_completion = (MUTANT == "anchor-completion")
    take_the_bare_householder_completion = (MUTANT == "completion-Q")
    Q = (list(range(NS * NS)) if take_the_bare_householder_completion
         else Q_COMPLETION)
    V = [[H[i][Q[j]] for j in range(NS * NS)] for i in range(NS * NS)]
    if perturb_the_constructed_completion:
        V[0][2] = -V[0][2]
    return V


VCOMP = completion()


# ---- exact sparse linear algebra over Q ----------------------------------
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
    """The same sparse product as `mm`, with the FIELD's own products and
    sums memoised.  Nothing is approximated and nothing is cached at the
    level of a transported value: the memo is of + and x in Q.  The two
    routines are measured against each other on EVERY swept instance -- the
    section 14 gate compares each switched holonomy, built here, against the
    unswitched holonomy built by `mm`, so an all-positive switching is an
    exact equality test of this routine against the plain one."""
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


def sp_restrict(A, rows, cols):
    return {(i, j): v for (i, j), v in A.items() if i in rows and j in cols}


def minv(A):
    """The inverse of a leg.  Every declared leg is measured EXACTLY
    orthogonal, so the inverse is the transpose; the `orient-flip` mutant
    drops the transposition and must die against the orthogonality
    anchors and the controls."""
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
        if v == ONE:
            s = 1
        elif v == -ONE:
            s = -1
        else:
            return None, None
        perm[j], sgn[j] = i, s
    return perm, sgn


# ---- the declared operators ----------------------------------------------
_FIXTURE: dict = {}

# the pointer shift map: outcome o advances the wing's pointer by o.  It is
# INJECTIVE, which is what makes the final pointer value a record of the
# outcome; the `anchor-record` mutant collapses two outcomes onto one shift.
def pointer_shift(o):
    collapse_the_record = (MUTANT == "anchor-record")
    if collapse_the_record and o == 2:
        return 1
    return o


def U_prep():
    key = ("prep",)
    if key in _FIXTURE:
        return _FIXTURE[key]
    out = {}
    for a in range(NS * NS):
        for b in range(NS * NS):
            v = VCOMP[a][b]
            if not v:
                continue
            for pa in range(NP):
                for pb in range(NP):
                    out[(idx(a // NS, a % NS, pa, pb),
                         idx(b // NS, b % NS, pa, pb))] = v
    _FIXTURE[key] = out
    return out


def U_local(wing, g):
    """U_X(g) = sum_o Pi^g_o (x) Sh^{n(o)} on the wing (s_X, p_X), the
    identity on the other wing.  Pi^g_o is the rank-one projector onto
    column o of the declared rotation R_g and n is the pointer shift."""
    key = ("loc", wing, g)
    if key in _FIXTURE:
        return _FIXTURE[key]
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
    _FIXTURE[key] = out
    return out


def legs_of(sp, fr):
    key = ("legs", sp, fr)
    if key in _FIXTURE:
        return _FIXTURE[key]
    a, b = SETTINGS[sp]
    P, UA, UB = U_prep(), U_local("A", a), U_local("B", b)
    _FIXTURE[key] = [P, UA, UB] if fr == "F1" else [P, UB, UA]
    return _FIXTURE[key]


NLEGS = len(legs_of(SETTING_ORDER[0], "F1"))    # computed, never typed
CHECKPOINTS = tuple(range(0, NLEGS + 1))
DIVISION_EVENTS = (CHECKPOINTS[0], CHECKPOINTS[-1])
NODES = tuple((fr, t) for fr in FRAMES for t in CHECKPOINTS)
L_MAX = 2 * NLEGS + 2                           # the canonical loop's length


def theta(sp, fr, t):
    key = ("theta", sp, fr, t)
    if key not in _FIXTURE:
        acc = sp_id()
        for L in legs_of(sp, fr)[:t]:
            acc = mm(L, acc)
        _FIXTURE[key] = acc
    return _FIXTURE[key]


def realized_legs(sp, fr):
    """Each declared leg restricted to the configurations the process
    actually occupies before and after it."""
    key = ("realized", sp, fr)
    if key in _FIXTURE:
        return _FIXTURE[key]
    supp = [{i for (i, j), v in theta(sp, fr, t).items()
             if j == J0 and v} for t in CHECKPOINTS]
    _FIXTURE[key] = [sp_restrict(legs_of(sp, fr)[t], supp[t + 1], supp[t])
                     for t in range(NLEGS)]
    return _FIXTURE[key]


def node_law(sp, fr, t):
    """THE LAW'S RESTRICTION TO THE CONTEXT (fr, t): the occupied support and
    the exact probability of every configuration at the DECLARED READ TIME
    t, carried inside the datum (RUNBOOK section 15 addendum)."""
    _bump()
    key = ("node_law", sp, fr, t)
    if key in _FIXTURE:
        return _FIXTURE[key]
    T = theta(sp, fr, t)
    out: dict = {}
    for (i, j), v in T.items():
        if j == J0 and v:
            out[i] = out.get(i, ZERO) + v * v
    read_every_datum_at_the_final_checkpoint = (MUTANT == "readtime-conflate")
    if read_every_datum_at_the_final_checkpoint:
        TF = theta(sp, fr, NLEGS)
        outf: dict = {}
        for (i, j), v in TF.items():
            if j == J0 and v:
                outf[i] = outf.get(i, ZERO) + v * v
        _FIXTURE[key] = {"read_time": NLEGS, "law": outf}
    else:
        _FIXTURE[key] = {"read_time": t, "law": out}
    return _FIXTURE[key]


def one_step(sp, fr, t):
    """The DECLARED one-step Born transition into checkpoint t."""
    return sp_born(legs_of(sp, fr)[t - 1])


# ---- the declared relabelling scopes --------------------------------------
def build_perm(sw, ra, rb, sa, sb):
    """The declared relabelling scope: the WING EXCHANGE flag, a cyclic
    system relabelling per wing, a cyclic pointer relabelling per wing.  The
    wing flag always moves the system pair AND the pointer pair together --
    that is the structural fact the escape gate reads."""
    p = [0] * NC
    for i in range(NC):
        qa, qb, pa, pb = unidx(i)
        qa2, qb2 = (qa + ra) % NS, (qb + rb) % NS
        pa2, pb2 = (pa + sa) % NP, (pb + sb) % NP
        p[i] = (idx(qb2, qa2, pb2, pa2) if sw else idx(qa2, qb2, pa2, pb2))
    return p


def build_perm_tr(sw, ra, rb, ta, tb):
    """The declared EXTENSION scope: the pointer TRANSPOSITION (1 <-> 2)
    fixes the ready state 0, so it survives the j0 filter where the cyclic
    pointer relabellings do not."""
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
    generate_the_scope_from_a_truncated_generator = (MUTANT == "scope-gen")
    prange = ((0, 1) if generate_the_scope_from_a_truncated_generator
              else tuple(range(NP)))
    base = [build_perm(sw, ra, rb, sa, sb)
            for sw in (0, 1) for ra in range(NS) for rb in range(NS)
            for sa in prange for sb in prange]
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
            "n_base_generated": len(base),
            "n_base": len({tuple(p) for p in base}),
            "n_ext_total": len(base + ext_u),
            "n_admitted": len(admitted),
            "n_admitted_extension": len(admitted_ext)}


SCOPE = declared_scope()
WSWAP = build_perm(1, 0, 0, 0, 0)               # the wing exchange
IDPERM = build_perm(0, 0, 0, 0, 0)


def _cfg_perm(f):
    return [idx(*f(*unidx(j))) for j in range(NC)]


# The two halves of the wing exchange, in the model's own coordinates: the
# SYSTEM-only exchange and the POINTER-only exchange.  The factorisation
# W = XS . XP is MEASURED below, never assumed.
XSSWAP = _cfg_perm(lambda sa, sb, pa, pb: (sb, sa, pa, pb))
XPSWAP = _cfg_perm(lambda sa, sb, pa, pb: (sa, sb, pb, pa))

PERM_NAME = {canon(list(IDPERM)): "the identity",
             canon(list(WSWAP)): "the wing exchange",
             canon(list(XSSWAP)): "the system-only wing exchange",
             canon(list(XPSWAP)): "the pointer-only wing exchange"}

_NAMES_OF_THE_TWO_DECLARED_MAPS = {canon(list(IDPERM)): "the identity",
                                   canon(list(WSWAP)): "the wing exchange"}


def name_perm(t):
    return PERM_NAME.get(canon(list(t)), "another permutation")


def perm_tuple(p):
    """A holonomy's VALUE: the permutation itself, as the tuple of images.
    This is MATRIX CONTENT.  The `label-collapse` mutant returns a NAME
    drawn from the two declared identification maps instead, so that every
    other permutation collapses onto one string and the value set is
    counted as a set of labels -- a count of the wrong object.  The
    mutation is injected here, in the computation; no gate predicate names
    it, and the count gate must catch it blind."""
    t = tuple(p[j] for j in range(NC))
    count_labels_instead_of_permutations = (MUTANT == "label-collapse")
    if count_labels_instead_of_permutations:
        return _NAMES_OF_THE_TWO_DECLARED_MAPS.get(canon(list(t)),
                                                   "another permutation")
    return t


def perm_compose(x, y):
    return tuple(x[y[i]] for i in range(NC))


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


# ===========================================================================
# 2.  THE FREEZE -- the base declared before any transport datum
# ===========================================================================
def run_freeze():
    global _FROZEN
    prog("freeze: BASE G declared as data before any transport measurement")
    gate("GEN-FREEZE", "freeze",
         "THE SECOND BASE IS DECLARED BEFORE ANY TRANSPORT MEASUREMENT "
         "(RUNBOOK 13(4)), AND THE RECEIPT'S GATE ORDER PROVES IT.  The "
         "carrier and its index map, the three declared rotations as "
         "integer quaternions with their PINNED matrices, the declared "
         "preparation vector, the PINNED orthogonal completion in full, the "
         "declared setting family, the two frames, the checkpoints with the "
         "read time as a coordinate of every node, the two gluing rules, "
         "the two transported objects with their per-coordinate actions, "
         "the declared relabelling scope and its extension, and the four "
         "declared probes are ALL recorded above -- and the transport-datum "
         "evaluation counter is measured to be ZERO at this point, with "
         "this the FIRST gate recorded.  The `freeze-lax` mutant evaluates "
         "one node law first and must die here",
         _FEVALS == 0 and len(GATES) == 0,
         {"transport_datum_evaluations_before_the_freeze": _FEVALS,
          "gates_recorded_before_this_one": len(GATES),
          "carrier": NC, "system_dimension_per_wing": NS,
          "pointer_states_per_wing": NP,
          "initial_configuration": J0,
          "declared_rotations": ROT_ORDER,
          "declared_settings": SETTING_ORDER,
          "frames": list(FRAMES),
          "checkpoints": list(CHECKPOINTS),
          "declared_division_events": list(DIVISION_EVENTS),
          "nodes_per_setting": len(NODES),
          "legs_per_frame": NLEGS,
          "path_length_bound": L_MAX,
          "objects": [o[0] for o in OBJECTS],
          "identification_rules": [r["id"] for r in ID_RULES],
          "probes": list(PROBES)})
    TABLES["declarations"] = {
        "carrier": {
            "configurations": NC,
            "coordinates": "(s_A, s_B, p_A, p_B)",
            "system_dimension_per_wing": NS,
            "pointer_states_per_wing": NP,
            "index_map": "i = ((s_A*%d + s_B)*%d + p_A)*%d + p_B"
                         % (NS, NP, NP),
            "initial_configuration": J0,
            "initial_configuration_coordinates": list(unidx(J0))},
        "measurement_family": {
            "quaternions": {k: list(v) for k, v in QUATERNIONS.items()},
            "pinned_rotation_matrices": PINNED_ROT,
            "outcomes_per_measurement": NS,
            "pointer_shift_of_outcome_o": "o (mod %d)" % NP},
        "preparation": {
            "vector_psi_coefficients": {"|%d,%d>" % k: v
                                        for k, v in PSI_COEFF.items()},
            "completion_rule": "V = H . Q with H the Householder reflection "
                               "carrying e_{(0,0)} to psi and Q the declared "
                               "transposition of the system-pair basis "
                               "states (0,1) and (0,2)",
            "Q_as_a_permutation_of_the_9_system_pair_indices":
                list(Q_COMPLETION),
            "pinned_completion_matrix_V": PINNED_V,
            "U_prep": "V (x) I_%d, the identity on the pointer pair"
                      % (NP * NP)},
        "settings": {k: list(v) for k, v in SETTINGS.items()},
        "frames": {"F1": "(prep, A, B)", "F2": "(prep, B, A)"},
        "objects": [{"id": i, "name": n, "datum": d, "action": a}
                    for i, n, d, a in OBJECTS],
        "identification_rules": [dict(r) for r in ID_RULES],
        "nodes": ["%s@t%d" % n for n in NODES],
        "path_length_bound": L_MAX,
        "probes": list(PROBES)}
    _FROZEN = True


# ===========================================================================
# 3.  THE BASE, VERIFIED AS DECLARED -- anchors and gates, before transport
# ===========================================================================
def _nt():
    return json.loads(NT_RECEIPT.read_text())


def run_base_declaration():
    """Every declared object is CONSTRUCTED here and measured against the
    pinned declaration, and every structural property the species requires
    is measured on the constructed objects.  No transport quantity is
    computed in this section: the gate order of the receipt is the proof."""
    prog("the declared base: pinned data vs constructed, and the species")

    # -- A01-A03: the pinned declarations vs their constructors -------------
    anchor("A01", "the pinned declaration of this unit",
           "the three declared rotation matrices, entry by entry",
           PINNED_ROT,
           {k: [[str(v) for v in row] for row in ROT[k]] for k in ROT_ORDER})
    anchor("A02", "the pinned declaration of this unit",
           "the preparation vector psi, as the first column of V",
           [str(parse_fr(PSI_COEFF.get((i // NS, i % NS), "0")))
            for i in range(NS * NS)],
           [str(VCOMP[i][0]) for i in range(NS * NS)])
    anchor("A03", "the pinned declaration of this unit",
           "the PINNED ORTHOGONAL COMPLETION V, all 81 entries",
           PINNED_V,
           [[str(v) for v in row] for row in VCOMP])

    # -- the constructed objects, measured ---------------------------------
    rot_orth = {}
    for k in ROT_ORDER:
        R = ROT[k]
        rot_orth[k] = all(
            sum((R[i][a] * R[i][b] for i in range(NS)), ZERO)
            == (ONE if a == b else ZERO)
            for a in range(NS) for b in range(NS))
    V_orth = all(sum((VCOMP[k][i] * VCOMP[k][j] for k in range(NS * NS)),
                     ZERO) == (ONE if i == j else ZERO)
                 for i in range(NS * NS) for j in range(NS * NS))
    psi_norm = sum((VCOMP[i][0] * VCOMP[i][0] for i in range(NS * NS)), ZERO)

    # Schmidt rank of psi: the exact rank of its 3x3 coefficient matrix.
    Mc = [[VCOMP[a * NS + b][0] for b in range(NS)] for a in range(NS)]
    A = [row[:] for row in Mc]
    rank = 0
    for c in range(NS):
        piv = next((i for i in range(rank, NS) if A[i][c]), None)
        if piv is None:
            continue
        A[rank], A[piv] = A[piv], A[rank]
        inv = ONE / A[rank][c]
        A[rank] = [inv * v for v in A[rank]]
        for i in range(NS):
            if i != rank and A[i][c]:
                f = A[i][c]
                A[i] = [x - f * y for x, y in zip(A[i], A[rank])]
        rank += 1

    # the two symmetry facts the species turns on, MEASURED
    psi_sym = all(VCOMP[i][0] == VCOMP[SIGMA9[i]][0] for i in range(NS * NS))
    psi_born_sym = all(VCOMP[i][0] * VCOMP[i][0]
                       == VCOMP[SIGMA9[i]][0] * VCOMP[SIGMA9[i]][0]
                       for i in range(NS * NS))
    H = householder()
    H_born_sym = all(H[i][j] * H[i][j]
                     == H[SIGMA9[i]][SIGMA9[j]] * H[SIGMA9[i]][SIGMA9[j]]
                     for i in range(NS * NS) for j in range(NS * NS))
    V_born_sym = all(VCOMP[i][j] * VCOMP[i][j]
                     == VCOMP[SIGMA9[i]][SIGMA9[j]]
                     * VCOMP[SIGMA9[i]][SIGMA9[j]]
                     for i in range(NS * NS) for j in range(NS * NS))

    ops_orth = {}
    for fr in FRAMES:
        for sp in SETTING_ORDER:
            for k, L in enumerate(legs_of(sp, fr)):
                ops_orth["%s/%s/leg%d" % (sp, fr, k + 1)] = is_orthogonal(L)

    # the local legs commute, MEASURED at every declared setting pair
    commute = {}
    for a in ROT_ORDER:
        for b in ROT_ORDER:
            UA, UB = U_local("A", a), U_local("B", b)
            commute["A(%s),B(%s)" % (a, b)] = (mm(UA, UB) == mm(UB, UA))

    # the record property, MEASURED: the pointer shift is injective in the
    # outcome, and every declared local leg decomposes as a sum of rank-one
    # projectors tensored with the corresponding shift.  THE COMPARATOR IS
    # INDEPENDENT OF BOTH COMPONENTS IT AUDITS (RUNBOOK section 14 addendum):
    # it is built from the PINNED rotation matrices and the independently
    # declared shift table SHIFT_DECLARED, never from `rotation()` or from
    # `pointer_shift()`, so a perturbation of either constructor moves the
    # constructed leg while leaving the comparator where it was.
    shifts = [pointer_shift(o) for o in range(NS)]
    shift_injective = len(set(shifts)) == NS
    proj_ok, record_ok = True, True
    record_mismatches = []
    for g in ROT_ORDER:
        R = ROT[g]
        for o in range(NS):
            for o2 in range(NS):
                ip = sum((R[i][o] * R[i][o2] for i in range(NS)), ZERO)
                if ip != (ONE if o == o2 else ZERO):
                    proj_ok = False
    for wing in ("A", "B"):
        for g in ROT_ORDER:
            U = U_local(wing, g)
            RP = [[parse_fr(v) for v in row] for row in PINNED_ROT[g]]
            rebuilt: dict = {}
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
                                    v = RP[s1][o] * RP[s0][o]
                                    if not v:
                                        continue
                                    i = (idx(s1, sb0, p1, pb0) if wing == "A"
                                         else idx(sa0, s1, pa0, p1))
                                    c = rebuilt.get((i, j), ZERO) + v
                                    if c:
                                        rebuilt[(i, j)] = c
                                    else:
                                        rebuilt.pop((i, j), None)
            if rebuilt != U:
                record_ok = False
                record_mismatches.append("%s/%s" % (wing, g))

    anchor("A04", "the declared species",
           "every declared operator of every (setting, frame) is exactly "
           "orthogonal", True, all(ops_orth.values()))
    anchor("A05", "the declared species",
           "the two wings' local legs commute at every declared pair of "
           "rotations", True, all(commute.values()))
    anchor("A06", "the declared species",
           "the pointer shift is injective in the outcome, so the final "
           "pointer value records the outcome", True, shift_injective)
    anchor("A07", "the pinned declaration of this unit",
           "V is exactly orthogonal and psi is a unit vector",
           [True, str(ONE)], [V_orth, str(psi_norm)])

    TABLES["base_declaration"] = {
        "rotations_are_orthogonal": rot_orth,
        "completion_is_orthogonal": V_orth,
        "psi_is_a_unit_vector": str(psi_norm) == str(ONE),
        "psi_schmidt_rank": rank,
        "psi_is_invariant_under_the_system_exchange": psi_sym,
        "the_born_shadow_of_psi_is_invariant_under_the_system_exchange":
            psi_born_sym,
        "the_born_shadow_of_the_householder_H_is_exchange_symmetric":
            H_born_sym,
        "the_born_shadow_of_the_declared_completion_V_is_exchange_symmetric":
            V_born_sym,
        "declared_operators_are_orthogonal": ops_orth,
        "the_local_legs_commute": commute,
        "pointer_shifts": shifts,
        "the_independently_declared_shift_table": list(SHIFT_DECLARED),
        "the_projectors_are_orthonormal": proj_ok,
        "every_local_leg_is_a_sum_of_projectors_times_shifts": record_ok,
        "legs_where_the_independent_comparator_disagrees": record_mismatches,
        "legs_per_frame": NLEGS}

    gate("GEN-BASE-PINNED", "measurement",
         "THE SECOND BASE IS PINNED AS DATA AND ITS CONSTRUCTORS AGREE WITH "
         "THE PIN.  The three declared rotation matrices and the full 9x9 "
         "orthogonal COMPLETION of the preparation are typed in this file "
         "as the unit's declaration, and the objects the constructors build "
         "from the integer quaternions and from the Householder rule are "
         "measured against them ENTRY BY ENTRY (A01-A03).  The completion "
         "is not a silent choice: the completion-relativity lesson is made "
         "structural by printing the matrix.  The gate then measures on the "
         "CONSTRUCTED objects that every declared rotation is exactly "
         "orthogonal, that V is exactly orthogonal, that psi is a unit "
         "vector, and that psi's Schmidt rank is the declared one -- so the "
         "preparation is entangled and not a product.  The "
         "`anchor-completion` mutant perturbs one entry of the constructed "
         "completion and the `anchor-rot` mutant one entry of a constructed "
         "rotation; both must die here",
         all(rot_orth.values()) and V_orth
         and str(psi_norm) == str(ONE) and rank == NS
         and all(a["passed"] for a in ANCHORS),
         {"rotations_are_orthogonal": rot_orth,
          "completion_is_orthogonal": V_orth,
          "psi_norm_squared": str(psi_norm),
          "psi_schmidt_rank": rank,
          "system_dimension": NS,
          "pinned_anchors_passed": [a["id"] for a in ANCHORS
                                    if a["passed"]]})

    gate("GEN-SPECIES", "measurement",
         "BASE G IS OF THE DECLARED SPECIES.  Four clauses, each measured "
         "on the constructed operators.  (1) TWO WINGS with LOCAL legs: "
         "every declared local leg acts on one wing's (system, pointer) "
         "pair and trivially on the other, and the two wings' legs are "
         "measured to COMMUTE at every one of the declared pairs of "
         "rotations (A05) -- the fact the positive control rests on.  (2) A "
         "PREPARATION: one declared leg, common to both frames, exactly "
         "orthogonal, carrying the initial configuration to an ENTANGLED "
         "state (Schmidt rank measured above).  (3) RECORDS AT THE FINAL "
         "DIVISION EVENT: every local leg is measured to be exactly the sum "
         "over outcomes of a rank-one projector tensored with the pointer "
         "shift of that outcome, the projectors are measured orthonormal, "
         "and the shift map is measured INJECTIVE -- so the pointer value "
         "at the final division event determines the outcome.  THE "
         "DECOMPOSITION'S COMPARATOR IS BUILT INDEPENDENTLY OF BOTH "
         "COMPONENTS IT AUDITS (RUNBOOK section 14 addendum): the sum is "
         "assembled from the PINNED rotation matrices and the independently "
         "declared shift table, never from the rotation constructor or from "
         "`pointer_shift`, so a perturbation of either moves one side of "
         "the comparison and not the other.  The `anchor-record` mutant "
         "collapses two outcomes onto one shift and dies at the injectivity "
         "clause AND at the decomposition clause; the `anchor-rot` mutant "
         "perturbs a constructed rotation and dies at the decomposition "
         "clause as well.  (4) EVERY DECLARED OPERATOR IS EXACTLY "
         "ORTHOGONAL (A04), so the Born shadow of every leg is a stochastic "
         "matrix and the reverse traversal is the transpose",
         all(commute.values()) and all(ops_orth.values())
         and shift_injective and proj_ok and record_ok and rank >= 2,
         {"the_local_legs_commute_at_every_declared_pair":
              all(commute.values()),
          "declared_operator_orthogonality_cells": len(ops_orth),
          "declared_operators_that_are_not_orthogonal":
              [k for k, v in ops_orth.items() if not v],
          "pointer_shift_is_injective": shift_injective,
          "pointer_shifts_from_the_constructor": shifts,
          "the_independently_declared_shift_table": list(SHIFT_DECLARED),
          "projectors_orthonormal": proj_ok,
          "legs_measured_equal_to_the_independently_built_decomposition":
              record_ok,
          "legs_where_the_independent_comparator_disagrees":
              record_mismatches,
          "the_comparator_reads":
              "PINNED_ROT and SHIFT_DECLARED (declared data), not "
              "rotation() and not pointer_shift()",
          "psi_schmidt_rank": rank})

    gate("GEN-COMPLETION-IS-LOAD-BEARING", "measurement",
         "THE PREPARATION'S TWO SYMMETRY FACTS, WHICH ARE WHAT THE SPECIES "
         "TURNS ON, MEASURED SEPARATELY.  (1) The BORN SHADOW of the "
         "preparation column psi is invariant under the exchange of the two "
         "systems -- so the wing exchange is not excluded at the outset "
         "from being a co-reference of the realized process.  On this base "
         "psi itself is measured INVARIANT under that exchange, where the "
         "first base's preparation vector is ANTI-invariant: the shared "
         "property is the Born-level one, and the vectors differ.  (2) The "
         "Born shadow of the declared COMPLETION V is measured NOT to be "
         "exchange-symmetric, while the Born shadow of the bare Householder "
         "H from which V is built IS -- so the declared basis transposition "
         "Q, and nothing else, is what breaks the symmetry at the level of "
         "the full declared leg.  That single declared choice is what makes "
         "the FULL-leg rule admit ONE permutation rather than two, and its "
         "alternative is measured in the declared completion flip-test.  "
         "The `anchor-completion` mutant perturbs the constructed "
         "completion and must die here or at GEN-BASE-PINNED",
         psi_born_sym and H_born_sym and not V_born_sym,
         {"psi_is_exchange_invariant": psi_sym,
          "born_shadow_of_psi_is_exchange_symmetric": psi_born_sym,
          "born_shadow_of_H_is_exchange_symmetric": H_born_sym,
          "born_shadow_of_V_is_exchange_symmetric": V_born_sym,
          "the_declared_transposition_Q": list(Q_COMPLETION)})
    return {"psi_born_sym": psi_born_sym, "V_born_sym": V_born_sym,
            "schmidt_rank": rank}


def run_external_pin():
    """THE ONE EXTERNAL ARTIFACT THIS UNIT READS IS HASH-PINNED BEFORE IT IS
    READ.  The five reused first-base values are anchored against their own
    fields (A08-A12); this anchors the FILE those fields live in, so that
    'the committed NT terminal receipt' is an assertion and not a caption."""
    raw = NT_RECEIPT.read_bytes()
    perturb_the_external_bytes = (MUTANT == "nt-hash")
    if perturb_the_external_bytes:
        raw = raw + b" "
    nt = json.loads(raw.decode())
    anchor("A13", "the committed NT terminal receipt, as a file",
           "the sha256 of the receipt this unit reads, the generator hash "
           "the receipt itself records, and its schema",
           ["d256891b479a8636fe88df5e9b0f553998140f1553fdfc167662220b44eeb"
            "03e",
            "8cb7607d2ba18c358f12ca22e69d5d398e3e840a998ad8316ef33dc296367"
            "0e7",
            "nt-transport-receipt-v1"],
           [hashlib.sha256(raw).hexdigest(), nt["source_sha256"],
            nt["schema"]])
    gate("GEN-EXTERNAL-SOURCE-PINNED", "measurement",
         "THE EXTERNAL SOURCE IS PINNED BY HASH, NOT BY PATH.  This unit "
         "reads exactly one file it did not write -- the first base's "
         "committed terminal receipt -- and A13 measures the sha256 of that "
         "file, together with the generator hash the receipt records for "
         "its own instrument and its schema string, against the values this "
         "unit declares.  A different receipt at the same path, or an "
         "edited one, kills the run here before any of its numbers is used; "
         "the five value anchors A08-A12 then measure that the numbers "
         "inside it are still what this unit believes",
         all(a["passed"] for a in ANCHORS if a["id"] == "A13"),
         {"receipt_sha256": hashlib.sha256(raw).hexdigest(),
          "the_generator_hash_the_receipt_records": nt["source_sha256"],
          "schema": nt["schema"],
          "the_receipts_own_pin_and_base_commits":
              [nt["pin_commit"], nt["base_commit"]]})


def run_arena():
    """RUNBOOK section 15: the arena declared AS DATA, with every size
    computed by enumeration and none typed."""
    prog("the declared arena (section 15), sizes computed by enumeration")
    sym = [sp for sp in SETTING_ORDER if SETTINGS[sp][0] == SETTINGS[sp][1]]
    wfact = (perm_compose(tuple(XSSWAP), tuple(XPSWAP)) == tuple(WSWAP))
    admitted_names = sorted(name_perm(tuple(p)) for p in SCOPE["admitted"])
    scope_closed = True
    bset = {tuple(p) for p in SCOPE["base"]}
    for x in SCOPE["base"]:
        for y in SCOPE["base"]:
            if perm_compose(tuple(x), tuple(y)) not in bset:
                scope_closed = False
                break
        if not scope_closed:
            break
    # The EXTENSION's closure is measured separately, because it is a
    # different fact: the extension is a UNION and membership in it is a set
    # test, not a group test.
    ext_closed = True
    eset = {tuple(p) for p in SCOPE["extension_all"]}
    for x in SCOPE["extension_all"]:
        for y in SCOPE["extension_all"]:
            if perm_compose(tuple(x), tuple(y)) not in eset:
                ext_closed = False
                break
        if not ext_closed:
            break
    arena = {
        "carrier": NC,
        "initial_configuration": J0,
        "state": "p(0) = delta_{j0}",
        "settings": len(SETTING_ORDER),
        "symmetric_settings": sym,
        "symmetric_setting_count": len(sym),
        "frames": len(FRAMES),
        "legs_per_frame": NLEGS,
        "checkpoints": len(CHECKPOINTS),
        "checkpoint_values": list(CHECKPOINTS),
        "declared_division_events": list(DIVISION_EVENTS),
        "nodes_per_setting": len(NODES),
        "path_length_bound": L_MAX,
        "declared_relabelling_scope": SCOPE["n_base"],
        "declared_relabelling_scope_generated": SCOPE["n_base_generated"],
        "declared_extension_scope": SCOPE["n_ext_total"],
        "admitted_after_the_j0_filter": SCOPE["n_admitted"],
        "admitted_after_the_j0_filter_at_the_extension":
            SCOPE["n_admitted_extension"],
        "the_admitted_maps": admitted_names,
        "the_declared_scope_is_closed_under_composition": scope_closed,
        "the_declared_extension_is_closed_under_composition": ext_closed,
        "the_wing_exchange_factorises_as_XS_XP": wfact,
        "fixed_points_of_the_wing_exchange": fixed_points(WSWAP),
        "fixed_points_of_the_system_only_exchange": fixed_points(XSSWAP),
        "fixed_points_of_the_pointer_only_exchange": fixed_points(XPSWAP)}
    TABLES["arena"] = arena
    gate("GEN-ARENA", "measurement",
         "THE ARENA IS DECLARED AS DATA AND EVERY SIZE IS COMPUTED "
         "(RUNBOOK section 15).  The carrier, the initial configuration and "
         "the state; the setting family and, computed from the declaration "
         "itself, which of its members are SYMMETRIC; the frames, the legs "
         "per frame, the checkpoints with the read time a coordinate of "
         "every node, the declared division events, the node count and the "
         "path length bound; the declared relabelling scope, its declared "
         "extension, and the subsets of each that survive the j0 filter.  "
         "EVERY ONE of these numbers is produced by an enumeration in this "
         "run: the scope is generated from its own generators and "
         "deduplicated, the admitted sets are filtered, the symmetric "
         "settings are read off the family, the checkpoint set is computed "
         "from the leg count.  The gate measures that the DECLARED "
         "RELABELLING SCOPE is CLOSED under composition -- so that scope, "
         "and that scope alone, is a group and not a list; the declared "
         "EXTENSION's closure is measured separately and reported as "
         "measured, since the extension is a union and membership in it is "
         "a set test, on which no result depends.  The gate also measures "
         "that the wing exchange factorises as the system-only exchange "
         "times the pointer-only exchange, and that the j0 filter leaves "
         "exactly the maps the identification rules will search over.  The "
         "`scope-lax` mutant subsamples the admitted scope and must die "
         "here",
         scope_closed and wfact
         and SCOPE["n_base"] == SCOPE["n_base_generated"]
         and SCOPE["n_admitted"] > 0
         and SCOPE["n_admitted_extension"] > SCOPE["n_admitted"]
         and len(sym) > 0 and len(CHECKPOINTS) == NLEGS + 1
         and len(NODES) == len(FRAMES) * len(CHECKPOINTS)
         and L_MAX == 2 * NLEGS + 2,
         arena)
    return arena


# ===========================================================================
# 4.  THE GLUING RULES, THE ALIGNMENT PROFILE AND THE ADMISSION TABLE
# ===========================================================================
def leg_key(L):
    """A canonical key for a declared leg at the Born level.  Two legs match
    iff their keys are equal, so order-free matching of leg lists is
    MULTISET EQUALITY of keys and needs no permutation search."""
    return canon(sorted((i, j, canon(v)) for (i, j), v in sp_born(L).items()))


def prefix_profile():
    """DO THE TWO FRAMES' DECLARED LEG PREFIXES UP TO t MATCH ORDER-FREE?
    The `prefix-lax` mutant reads the WHOLE declared leg list instead of the
    prefix and must die at the profile gate."""
    out = {}
    for t in CHECKPOINTS[1:]:
        for sp in SETTING_ORDER:
            cut = NLEGS if MUTANT == "prefix-lax" else t
            ka = sorted(leg_key(L) for L in legs_of(sp, "F1")[:cut])
            kb = sorted(leg_key(L) for L in legs_of(sp, "F2")[:cut])
            out[(t, sp)] = (ka == kb)
    return out


def admits(sp, t, rule, scope="admitted"):
    """THE FOUR-CLAUSE ADMISSIBILITY PREDICATE, in order: the j0 filter, the
    rule's own leg list matched order-free at the Born level, the
    occupied-set clause, the exact-law clause.  An identification is
    ADMITTED when exactly one permutation of the scope satisfies all four
    (admission by UNIQUENESS)."""
    la = (realized_legs(sp, "F1") if rule["legs"] == "realized"
          else legs_of(sp, "F1"))
    lb = (realized_legs(sp, "F2") if rule["legs"] == "realized"
          else legs_of(sp, "F2"))
    kA = ("legkeys", sp, rule["id"], "F1")
    if kA not in _FIXTURE:
        _FIXTURE[kA] = sorted(leg_key(L) for L in la)
    ka = _FIXTURE[kA]
    da = node_law(sp, "F1", t)["law"]
    db = node_law(sp, "F2", t)["law"]
    out = []
    for p in SCOPE[scope]:
        if p[J0] != J0:
            continue
        kB = ("legkeys", sp, rule["id"], "F2", canon(list(p)))
        if kB not in _FIXTURE:
            _FIXTURE[kB] = sorted(leg_key(sp_conj(L, p)) for L in lb)
        if ka != _FIXTURE[kB]:
            continue
        if {p[i] for i in db} != set(da):
            continue
        if any(da.get(p[i]) != db.get(i) for i in db):
            continue
        out.append(p)
    return out


def run_admission(pref):
    """The admission table and the alignment profile, both computed."""
    prog("the admission table and the leg-prefix alignment profile")
    table, trans = {}, {}
    for sp in SETTING_ORDER:
        for t in CHECKPOINTS:
            row = {}
            for rule in ID_RULES:
                adm = admits(sp, t, rule)
                row[rule["id"]] = {
                    "n_admitted": len(adm),
                    "maps": sorted(name_perm(tuple(p)) for p in adm),
                    "drawn": len(adm) == 1}
            table["%s/t%d" % (sp, t)] = row
        for t in CHECKPOINTS[1:]:
            trans[(t, sp)] = len(admits(sp, t, ID_RULES[0])) > 0
    agree = [k for k in trans if trans[k] == pref[k]]
    TABLES["admission"] = {
        "per_cell": table,
        "alignment_profile": {"t%d/%s" % k: v for k, v in sorted(pref.items())},
        "full_rule_transport_profile": {"t%d/%s" % k: v
                                        for k, v in sorted(trans.items())},
        "cells": len(trans),
        "cells_where_alignment_agrees_with_the_full_rule_profile": len(agree),
        "route": "alignment by multiset equality of canonical Born leg keys; "
                 "admission by this unit's own four-clause predicate over "
                 "the declared admitted scope"}
    drawn_full = sum(1 for k, r in table.items() if r["FULL"]["drawn"])
    drawn_real = sum(1 for k, r in table.items() if r["REAL"]["drawn"])
    gate("GEN-ADMISSION-TABLE", "measurement",
         "THE TWO GLUING RULES ARE MEASURED CELL BY CELL ON BASE G, AND THE "
         "LEG-PREFIX ALIGNMENT PROFILE IS COMPUTED BY AN INDEPENDENT ROUTE.  "
         "Alignment is multiset equality of canonical Born leg keys over the "
         "first t declared legs -- order-free matching without any "
         "permutation search.  Admission is the four-clause predicate over "
         "the declared admitted scope, and a link is DRAWN only where the "
         "rule admits UNIQUELY.  The gate measures that both rules draw "
         "somewhere (so the path graph has identification links at all), "
         "that the alignment profile is not constant in the read time (so "
         "the corridor classification is a real partition and not a "
         "relabelling of everything), and that the alignment profile agrees "
         "with the FULL rule's own transport profile at EVERY cell.  The "
         "`prefix-lax` mutant reads the whole declared leg list instead of "
         "the prefix, which makes the profile constant, and must die here; "
         "the `id-lax` mutant accepts every admitted permutation as an "
         "identification and must die at the uniqueness clause",
         drawn_full > 0 and drawn_real > 0
         and len({v for v in pref.values()}) > 1
         and len(agree) == len(trans),
         {"cells_where_the_full_rule_draws_a_link": drawn_full,
          "cells_where_the_realized_rule_draws_a_link": drawn_real,
          "distinct_alignment_verdicts": sorted({str(v)
                                                 for v in pref.values()}),
          "cells": len(trans),
          "cells_where_alignment_agrees_with_the_full_rule_profile":
              len(agree)})
    return table, trans


# ===========================================================================
# 5.  THE PATH SPACE -- enumerated, never typed
# ===========================================================================
def identification_links(sp):
    out = []
    for rule in ID_RULES:
        for t in CHECKPOINTS:
            adm = admits(sp, t, rule)
            if MUTANT == "id-lax":
                adm = list(SCOPE["admitted"])
            if len(adm) != 1:
                continue
            p = adm[0]
            out.append({"t": t, "rule": rule["id"], "perm": list(p),
                        "perm_name": name_perm(tuple(p))})
    return out


def build_graph(sp, pref):
    """THE PATH GRAPH of one setting.  Nodes are (frame, checkpoint); the
    READ TIME is a coordinate of the node and of every datum read there.
    Edges are the declared moves: leg applications in both directions, and
    the admitted identifications."""
    links = []
    for fr in FRAMES:
        for t in CHECKPOINTS[1:]:
            links.append({"kind": "leg", "a": (fr, t - 1), "b": (fr, t),
                          "frame": fr, "leg": t, "prefix_aligned": None})
    for L in identification_links(sp):
        t = L["t"]
        aligned = pref[(t, sp)] if (t, sp) in pref else True
        links.append({"kind": "id", "a": ("F2", t), "b": ("F1", t),
                      "t": t, "rule": L["rule"], "perm": L["perm"],
                      "perm_name": L["perm_name"],
                      "prefix_aligned": bool(aligned)})
    adj: dict = {n: [] for n in NODES}
    for li, L in enumerate(links):
        adj[L["a"]].append((li, +1, L["b"]))
        adj[L["b"]].append((li, -1, L["a"]))
    return {"links": links, "adj": adj, "n_nodes": len(NODES),
            "n_links": len(links), "cycle_rank": len(links) - len(NODES) + 1}


_INTERN: dict = {}
_INTERN_VALUE: dict = {}
_HOL_CLASS: dict = {}


def structural_key(v):
    """A hashable STRUCTURAL key: the sorted items of the object, whose
    entries are exact rationals.  Key identity IS exact value identity; no
    tolerance and no string rendering enters any comparison."""
    if isinstance(v, dict) and "law" in v:
        return ("L", v["read_time"], frozenset(v["law"].items()))
    return frozenset(v.items())


def intern(key):
    if key not in _INTERN:
        _INTERN[key] = len(_INTERN)
        _INTERN_VALUE[_INTERN[key]] = key
    return _INTERN[key]


def relative_sign_class(sgn):
    """THE INVARIANT SIGN CONTENT of a signed permutation.  A switching
    multiplies a closed loop's matrix by a global +-1, flipping every entry
    of `sgn` together; the RELATIVE signs s_j * s_0 survive that action
    while the raw sign set does not."""
    s0 = sgn[0]
    return tuple(sgn[j] * s0 for j in range(NC))


def holonomy_class_of_interned(akey):
    """The signed-permutation class of an interned amplitude-layer value.
    The interned key IS the exact matrix, so this is a reading of it and
    not a recomputation.  A key that was never interned carries no matrix
    -- the `path-collapse` mutation replaces every path's key with one
    token -- and is reported as unreadable so the gates measure the
    collapse instead of the run dying on it."""
    if akey not in _INTERN_VALUE:
        return (None, None, "not a readable transported value")
    if akey not in _HOL_CLASS:
        A = dict(_INTERN_VALUE[akey])
        p, s = signed_perm(A)
        _HOL_CLASS[akey] = (
            None if p is None else tuple(p[j] for j in range(NC)),
            None if s is None else relative_sign_class(s),
            "not a signed permutation" if p is None
            else name_perm(tuple(p[j] for j in range(NC))))
    return _HOL_CLASS[akey]


def l_value(sp, fr, t):
    d = node_law(sp, fr, t)
    return {"read_time": d["read_time"], "law": dict(d["law"])}


def l_push(sp, val, link, direction):
    """L's DECLARED per-coordinate action.  A leg acts by the declared
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
        return {"read_time": val["read_time"] + (1 if direction > 0 else -1),
                "law": law}
    p = link["perm"] if direction > 0 else perm_inverse(link["perm"])
    return {"read_time": val["read_time"],
            "law": {p[i]: v for i, v in val["law"].items()}}


def link_variable(sp, link, direction):
    """A's link variable: the leg operator for a leg (its inverse in
    reverse), the permutation matrix for an identification."""
    if link["kind"] == "leg":
        L = legs_of(sp, link["frame"])[link["leg"] - 1]
        return L if direction > 0 else minv(L)
    P = pmat(link["perm"])
    return P if direction > 0 else minv(P)


def transport_along(sp, G, path, obj):
    if obj == "A":
        acc = sp_id()
        for (li, d) in path["edges"]:
            acc = mm(link_variable(sp, G["links"][li], d), acc)
        return acc
    fr, t = path["start"]
    val = l_value(sp, fr, t)
    for (li, d) in path["edges"]:
        val = l_push(sp, val, G["links"][li], d)
        if val is None:
            return None
    return val


def enumerate_paths(sp, G, bound):
    """Every REDUCED path of length at most `bound`: a path never traverses
    the same link twice in immediate succession, since that is a backtrack
    and carries no transport content.  Each path is walked ONCE, carrying
    both objects' data incrementally.  The `reduce-lax` mutant drops the
    reduced condition; the `path-collapse` mutant gives every path the same
    key, so that no two paths can ever be measured to disagree."""
    rows = []
    step: dict = {}

    def move(obj, val, key, li, d):
        ck = (obj, key, li, d)
        if ck in step:
            return step[ck]
        L = G["links"][li]
        if obj == "L":
            nv = l_push(sp, val, L, d)
        else:
            nv = mm(link_variable(sp, L, d), val)
        nk = None if nv is None else intern(structural_key(nv))
        step[ck] = (nv, nk)
        return step[ck]

    def walk(start, node, edges, last, v1, v2, crossing, k1, k2):
        rows.append({
            "start": start, "end": node, "len": len(edges),
            "edges": list(edges),
            "corridor": "crossing" if crossing else "aligned",
            "L": "COLLAPSED" if MUTANT == "path-collapse" else
                 ("OBSTRUCTED" if v1 is None else k1),
            "A": "COLLAPSED" if MUTANT == "path-collapse" else k2})
        if len(edges) >= bound:
            return
        drop_the_reduced_condition = (MUTANT == "reduce-lax")
        for (li, d, nxt) in G["adj"][node]:
            if (not drop_the_reduced_condition
                    and last is not None and li == last):
                continue
            L = G["links"][li]
            n1, m1 = move("L", v1, k1, li, d)
            n2, m2 = move("A", v2, k2, li, d)
            walk(start, nxt, edges + [(li, d)], li, n1, n2,
                 crossing or (L["kind"] == "id" and not L["prefix_aligned"]),
                 m1, m2)

    for start in NODES:
        s1 = l_value(sp, start[0], start[1])
        s2 = sp_id()
        walk(start, start, [], None, s1, s2, False,
             intern(structural_key(s1)), intern(structural_key(s2)))
    return rows


def run_paths(pref):
    graphs, values = {}, {}
    for sp in SETTING_ORDER:
        prog("  path space %s" % sp)
        graphs[sp] = build_graph(sp, pref)
        values[sp] = enumerate_paths(sp, graphs[sp], L_MAX)
    return graphs, values


def run_pair_table(graphs, values):
    """THE MATCHED TABLE OF PATH PAIRS: every unordered pair of enumerated
    paths sharing BOTH endpoints, at matched coordinates.  The read time is
    part of the endpoint, and of the L datum, so no cell of this table
    compares data read at different checkpoints."""
    pairs, totals = {}, {"pairs": 0}
    for sp in SETTING_ORDER:
        prog("  matched pair table %s" % sp)
        by_ends: dict = {}
        for r in values[sp]:
            by_ends.setdefault((r["start"], r["end"]), []).append(r)
        rows = {o: {"aligned": [0, 0], "crossing": [0, 0]}
                for o in ("L", "A")}
        n = 0
        for _k, grp in by_ends.items():
            for i in range(len(grp)):
                for j in range(i + 1, len(grp)):
                    a, b = grp[i], grp[j]
                    n += 1
                    corr = ("crossing" if "crossing"
                            in (a["corridor"], b["corridor"]) else "aligned")
                    for o in ("L", "A"):
                        rows[o][corr][0 if a[o] == b[o] else 1] += 1
        pairs[sp] = rows
        totals["pairs"] += n
    agg = {o: {c: [sum(pairs[sp][o][c][k] for sp in SETTING_ORDER)
                   for k in (0, 1)]
               for c in ("aligned", "crossing")} for o in ("L", "A")}
    TABLES["pair_table"] = {
        "per_setting": {sp: {o: {c: {"agree": pairs[sp][o][c][0],
                                     "disagree": pairs[sp][o][c][1]}
                                 for c in ("aligned", "crossing")}
                             for o in ("L", "A")} for sp in SETTING_ORDER},
        "aggregate": {o: {c: {"agree": agg[o][c][0], "disagree": agg[o][c][1]}
                          for c in ("aligned", "crossing")}
                      for o in ("L", "A")},
        "total_pairs_sharing_both_endpoints": totals["pairs"]}
    return pairs, totals, agg


def run_path_space_audit(graphs, values, totals):
    """Every predicate here is recomputed FROM THE DELIVERED ROWS, so each
    is a property of the enumerated path space and not a restatement of a
    constructor argument."""
    ps, audit = {}, {}
    for sp in SETTING_ORDER:
        G, rows = graphs[sp], values[sp]
        ps[sp] = {
            "nodes": G["n_nodes"], "links": G["n_links"],
            "identification_links": sum(1 for L in G["links"]
                                        if L["kind"] == "id"),
            "cycle_rank": G["cycle_rank"], "paths": len(rows),
            "closed_paths": sum(1 for p in rows
                                if p["start"] == p["end"] and p["len"]),
            "link_detail": [{"t": L["t"], "rule": L["rule"],
                             "perm_name": L["perm_name"],
                             "prefix_aligned": L["prefix_aligned"]}
                            for L in G["links"] if L["kind"] == "id"]}
        backtracks = walk_breaks = end_breaks = 0
        for r in rows:
            e = r["edges"]
            for k in range(1, len(e)):
                if e[k][0] == e[k - 1][0]:
                    backtracks += 1
            node = r["start"]
            for (li, d) in e:
                L = G["links"][li]
                tail, head = ((L["a"], L["b"]) if d > 0 else (L["b"], L["a"]))
                if node != tail:
                    walk_breaks += 1
                node = head
            if node != r["end"]:
                end_breaks += 1
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
    ps["_total_paths"] = sum(len(values[sp]) for sp in SETTING_ORDER)
    ps["_total_pairs"] = totals["pairs"]
    TABLES["path_space"] = ps
    TABLES["path_space_audit"] = audit
    gate("GEN-PATH-SPACE-ENUMERATED", "measurement",
         "THE PATH SPACE IS ENUMERATED, NEVER TYPED, AND THE DECLARED "
         "PROPERTY OF ITS PATHS IS MEASURED ON THE ROWS THEMSELVES.  Nodes "
         "are (frame, checkpoint) coordinates with the READ TIME a "
         "coordinate of the node; moves are leg applications in both "
         "directions and the admitted identifications; paths are the "
         "REDUCED sequences of moves up to the declared bound, which is the "
         "canonical loop's own length.  FOUR PREDICATES, EACH RECOMPUTED "
         "HERE FROM THE DELIVERED ROWS: (1) the REDUCED condition, read off "
         "the enumerated edge lists; (2) every enumerated path is a genuine "
         "walk in the graph, step by step, ending at the node it declares; "
         "(3) the graph is CONNECTED, measured by union-find over the "
         "links, and the cycle rank is Euler's with that MEASURED component "
         "count; (4) the enumeration reaches every declared node and "
         "contains closed paths at every setting.  The `reduce-lax` mutant "
         "drops the reduced condition and must die at predicate (1), which "
         "counts its backtracks",
         all(audit[sp]["paths_that_traverse_one_link_twice_in_succession"] == 0
             and audit[sp]["steps_that_do_not_follow_the_graph"] == 0
             and audit[sp]["paths_whose_walk_does_not_reach_the_declared_end"]
             == 0
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
            "total_path_pairs": ps["_total_pairs"], "audit": audit})
    return ps


# ===========================================================================
# 6.  THE DECLARED PROBES AND THE CONTROLS
# ===========================================================================
def find_link(G, kind, **kw):
    for li, L in enumerate(G["links"]):
        if L["kind"] != kind:
            continue
        if all(L.get(k) == v for k, v in kw.items()):
            return li
    return None


def declared_loops(sp, G):
    """THE FOUR DECLARED PROBES, built from the graph rather than typed."""
    out = []
    idl = [li for li, L in enumerate(G["links"]) if L["kind"] == "id"]
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
                    "role": "POSITIVE CONTROL: the two frames' leg orders, "
                            "which MUST agree because the legs commute"})
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
                    "role": "the identification-multiplicity probe"})
    for li in idl:
        L = G["links"][li]
        if L["prefix_aligned"]:
            continue
        t = L["t"]
        for t2 in CHECKPOINTS:
            if t2 == t:
                continue
            other = [x for x in idl if G["links"][x]["t"] == t2
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
                        "role": "the prefix-crossing probe"})
            break
    if top is not None and bot is not None:
        tw = dict(G["links"][top])
        tw["perm"] = list(WSWAP)
        tw["perm_name"] = "the wing exchange (INJECTED)"
        out.append({"name": "the twisted comparator", "base": ("F1", 0),
                    "edges": None, "twist_link": top, "twist": tw,
                    "corridor": "aligned",
                    "role": "NEGATIVE CONTROL: it MUST show holonomy"})
    return out


def loop_holonomy(sp, G, loop, obj):
    links = list(G["links"])
    edges = loop["edges"]
    if edges is None:
        base = [x for x in declared_loops(sp, G)
                if x["name"] == "the canonical loop"][0]
        edges = base["edges"]
        links[loop["twist_link"]] = loop["twist"]
    path = {"start": loop["base"], "end": loop["base"], "edges": edges}
    return transport_along(sp, {"links": links, "adj": G["adj"]}, path, obj)


def run_probes(graphs):
    prog("the declared probes")
    rows = {}
    for sp in SETTING_ORDER:
        G = graphs[sp]
        for loop in declared_loops(sp, G):
            H = loop_holonomy(sp, G, loop, "A")
            perm, sgn = signed_perm(H) if H is not None else (None, None)
            baseL = l_value(sp, loop["base"][0], loop["base"][1])
            hL = loop_holonomy(sp, G, loop, "L")
            rows["%s / %s" % (sp, loop["name"])] = {
                "role": loop["role"], "corridor": loop["corridor"],
                "base_node": "%s@t%d" % loop["base"],
                "length": len(loop["edges"] or []) or None,
                "L_returns": (hL is not None and canon(hL) == canon(baseL)),
                "L_obstructed": hL is None,
                "A_is_signed_permutation": perm is not None,
                "A_permutation_is_the_identity":
                    perm is not None and all(perm[j] == j for j in range(NC)),
                "A_permutation_name":
                    name_perm(tuple(perm[j] for j in range(NC)))
                    if perm is not None else "not a signed permutation",
                "A_permutation_fixed_points":
                    fixed_points([perm[j] for j in range(NC)])
                    if perm is not None else None,
                "A_sign_orbit": sorted(set(sgn.values())) if sgn else None,
                "A_relative_signs_are_mixed":
                    (len(set(relative_sign_class(sgn))) > 1) if sgn else None}
    TABLES["probes"] = rows
    return rows


def run_controls(graphs, values, probes):
    """THE TWO CONTROLS, both measured, both with declared teeth."""
    prog("the positive and negative controls")
    # POSITIVE: the same-order path pair.  Frame 1's three legs forward from
    # F1@t0 to F1@t3, against the path that crosses at t=0, runs frame 2's
    # three legs, and crosses back at t=3.  They share BOTH endpoints and
    # they MUST agree, because the two local legs are measured to commute.
    pos = {}
    for sp in SETTING_ORDER:
        G = graphs[sp]
        top = find_link(G, "id", t=CHECKPOINTS[-1], rule="FULL")
        bot = find_link(G, "id", t=CHECKPOINTS[0], rule="FULL")
        if top is None or bot is None:
            pos[sp] = {"exists": False}
            continue
        p1 = {"start": ("F1", 0), "end": ("F1", NLEGS),
              "edges": [(find_link(G, "leg", frame="F1", leg=t), +1)
                        for t in CHECKPOINTS[1:]]}
        p2 = {"start": ("F1", 0), "end": ("F1", NLEGS),
              "edges": [(bot, -1)]
                       + [(find_link(G, "leg", frame="F2", leg=t), +1)
                          for t in CHECKPOINTS[1:]] + [(top, +1)]}
        a1 = transport_along(sp, G, p1, "A")
        a2 = transport_along(sp, G, p2, "A")
        pos[sp] = {"exists": True, "same_endpoints": p1["end"] == p2["end"],
                   "lengths": [len(p1["edges"]), len(p2["edges"])],
                   "the_two_orders_agree_at_the_amplitude_layer": a1 == a2}
    canon_rows = {k: v for k, v in probes.items()
                  if k.endswith("/ the canonical loop")}
    pos_ok = (all(v["exists"] and v["the_two_orders_agree_at_the_amplitude_"
                                   "layer"] for v in pos.values())
              and all(v["A_permutation_is_the_identity"]
                      for v in canon_rows.values())
              and len(canon_rows) == len(SETTING_ORDER))
    if MUTANT == "control-lax":
        pos_ok = False
    TABLES["positive_control"] = pos
    gate("GEN-POSITIVE-CONTROL", "measurement",
         "THE POSITIVE CONTROL: A SAME-ORDER PATH PAIR THAT MUST AGREE.  "
         "From F1@t0 to F1@t3 the graph carries two paths -- frame 1's three "
         "legs forward, and the path that crosses to frame 2 at the initial "
         "division event, runs frame 2's three legs, and crosses back at the "
         "final one.  They share BOTH endpoints, and the amplitude-layer "
         "transport along them is measured EQUAL at every setting, because "
         "the two frames differ only by the order of two legs measured to "
         "commute (A05).  The closed loop they form -- the pin's canonical "
         "loop -- is measured to have holonomy exactly the identity "
         "permutation at every setting.  Its discriminating power is small "
         "and is stated as such: given the commuting-legs anchor it could "
         "not have come out otherwise.  What it does exclude is a broken "
         "traversal convention, and the `orient-flip` mutant, which reads a "
         "leg's reverse traversal without transposing, dies on it; the "
         "`control-lax` waiver overwrites the predicate and dies too",
         pos_ok,
         {"per_setting": pos,
          "canonical_loop_holonomy":
              {k: v["A_permutation_name"] for k, v in canon_rows.items()},
          "canonical_loops_measured": len(canon_rows)})

    neg = {k: v for k, v in probes.items()
           if k.endswith("/ the twisted comparator")}
    neg_ok = (len(neg) == len(SETTING_ORDER)
              and all(not v["A_permutation_is_the_identity"]
                      for v in neg.values()))
    gate("GEN-NEGATIVE-CONTROL", "measurement",
         "THE NEGATIVE CONTROL, WITH TEETH.  The canonical loop is rebuilt "
         "with ONE identification deliberately replaced by the wing "
         "exchange at a coordinate where the base itself supplies the "
         "identity.  If the instrument cannot see that twist, it cannot see "
         "any twist and every flatness reading above is vacuous.  The gate "
         "measures that the injected loop's holonomy is NOT the identity at "
         "EVERY setting -- including the four where the base admits no "
         "second identification at all and where every genuine loop is "
         "measured flat.  If this gate had failed the run would say the "
         "instrument is dead",
         neg_ok,
         {"per_setting": {k: {"permutation": v["A_permutation_name"],
                              "is_a_signed_permutation":
                                  v["A_is_signed_permutation"],
                              "is_the_identity":
                                  v["A_permutation_is_the_identity"],
                              "fixed_points": v["A_permutation_fixed_points"]}
                          for k, v in neg.items()},
          "comparators_measured": len(neg)})
    return pos, neg


# ===========================================================================
# 7.  THE FIVE PRE-REGISTERED PATTERNS, EACH GATED SEPARATELY
# ===========================================================================
def based_holonomy(sp, values, closure_bound=None):
    """The based holonomy at the declared base point F1@t0, read as the
    PERMUTATION PART of the closed-loop link product and counted as
    PERMUTATIONS -- matrix content -- never as name labels.  The
    `hol-basepoint` mutant reads closed paths based anywhere instead, so the
    set is no longer a based holonomy and the closure clause falls over.

    `closure_bound` is a DECLARED runtime bound used only by the completion
    census's rebuild sweep, which computes tens of holonomy groups: the
    closure stops if it exceeds the bound and says so, and the sweep gates
    that the bound was never reached.  The unit's own measurements pass no
    bound at all."""
    read_closed_paths_at_any_base_point = (MUTANT == "hol-basepoint")
    base = ("F1", CHECKPOINTS[0])
    els, perms_seen, dropped, sgns = set(), [], 0, set()
    mixed: dict = {}
    for path in values[sp]:
        if path["start"] != path["end"] or not path["len"]:
            continue
        if path["start"] != base and not read_closed_paths_at_any_base_point:
            continue
        t, rel, nm = holonomy_class_of_interned(path["A"])
        if t is None:
            dropped += 1
            continue
        els.add(perm_tuple({j: t[j] for j in range(NC)}))
        perms_seen.append(tuple(t))
        sgns.add(rel)
        mixed[nm] = mixed.get(nm, False) or (len(set(rel)) > 1)
    gen = set(perms_seen)
    grp = set(gen) | {tuple(IDPERM)}
    changed, bound_hit = True, False
    while changed and not bound_hit:
        changed = False
        for x in list(grp):
            for y in list(grp):
                z = perm_compose(x, y)
                if z not in grp:
                    grp.add(z)
                    changed = True
                    if closure_bound is not None and len(grp) > closure_bound:
                        bound_hit = True
                        break
            if bound_hit:
                break
    closed = (bool(gen) and not bound_hit
              and all(perm_compose(x, y) in gen for x in gen for y in gen))
    abelian = all(perm_compose(x, y) == perm_compose(y, x)
                  for x in grp for y in grp)
    orders = sorted({perm_order(z) for z in grp})
    return {"value_set_size": len(els),
            "generated_group_order": len(grp),
            "the_declared_closure_bound_was_reached": bound_hit,
            "the_value_set_is_closed_under_composition": bool(closed),
            "the_value_set_is_the_generated_group":
                bool(gen | {tuple(IDPERM)} == grp),
            "the_group_is_abelian": bool(abelian),
            "element_orders": orders,
            "every_element_squares_to_the_identity": orders in ([1], [1, 2]),
            "elements": sorted(name_perm(z) for z in grp),
            "element_fixed_points": {name_perm(z): fixed_points(list(z))
                                     for z in grp},
            "closed_paths_based_there": len(perms_seen) + dropped,
            "closed_paths_whose_holonomy_is_not_a_signed_permutation":
                dropped,
            "distinct_relative_sign_classes": len(sgns),
            "elements_with_mixed_relative_signs":
                sorted(k for k, v in mixed.items() if v),
            "_group": sorted(list(z) for z in grp),
            "_value_set": sorted(list(z) for z in gen)}


def closed_path_census(sp, values):
    out: dict = {}
    for path in values[sp]:
        if path["start"] != path["end"] or not path["len"]:
            continue
        _t, _r, nm = holonomy_class_of_interned(path["A"])
        key = (path["corridor"], nm)
        out[key] = out.get(key, 0) + 1
    return {"%s / %s" % k: v for k, v in sorted(out.items())}


def subconnection(sp, pref, rule_ids):
    """THE SUB-CONNECTION built from a chosen subset of the declared gluing
    rules.  The single-rule sub-connections are the decisive diagnostic for
    P3(i): in each of them EVERY coordinate has identification multiplicity
    at most one, so if one of them is already non-flat then multiplicity is
    measured NOT to be necessary for holonomy."""
    G = build_graph(sp, pref)
    keep = [L for L in G["links"]
            if L["kind"] == "leg" or L["rule"] in rule_ids]
    adj: dict = {n: [] for n in NODES}
    for li, L in enumerate(keep):
        adj[L["a"]].append((li, +1, L["b"]))
        adj[L["b"]].append((li, -1, L["a"]))
    GG = {"links": keep, "adj": adj}
    base = ("F1", CHECKPOINTS[0])
    classes: dict = {}
    vals = []
    stack = [(base, [], None, sp_id())]
    while stack:
        node, edges, last, acc = stack.pop()
        if node == base and edges:
            p, _s = signed_perm(acc)
            nm = ("not a signed permutation" if p is None
                  else name_perm(tuple(p[j] for j in range(NC))))
            classes[nm] = classes.get(nm, 0) + 1
            if p is not None:
                vals.append(tuple(p[j] for j in range(NC)))
        if len(edges) >= L_MAX:
            continue
        for (li, d, nxt) in GG["adj"][node]:
            if last is not None and li == last:
                continue
            stack.append((nxt, edges + [(li, d)], li,
                          mm(link_variable(sp, keep[li], d), acc)))
    grp = {tuple(IDPERM)} | set(vals)
    changed = True
    while changed:
        changed = False
        for x in list(grp):
            for y in list(grp):
                z = perm_compose(x, y)
                if z not in grp:
                    grp.add(z)
                    changed = True
    mx = 0
    for t in {L["t"] for L in keep if L["kind"] == "id"}:
        mx = max(mx, sum(1 for L in keep if L["kind"] == "id"
                         and L["t"] == t))
    return {"rules": sorted(rule_ids), "links": len(keep),
            "identification_links": sum(1 for L in keep
                                        if L["kind"] == "id"),
            "cycle_rank": len(keep) - len(NODES) + 1,
            "closed_paths_at_the_base_point":
                sum(classes.values()),
            "holonomy_classes": dict(sorted(classes.items())),
            "non_identity_closed_paths":
                sum(n for c, n in classes.items() if c != "the identity"),
            "generated_group_order": len(grp),
            "max_identification_multiplicity_at_one_coordinate": mx}


def prep_defect():
    """P3(ii): D = P_W U_prep^-1 P_W U_prep, THE COMPLETION'S
    NON-EQUIVARIANCE DEFECT -- the element produced by the failure of the
    declared preparation LEG (hence of the declared completion V, not of
    the preparation VECTOR psi) to intertwine under the wing exchange.
    Section 14 derives and gates the closed form D = (Sigma V^T Sigma V)
    (x) I_9 and its cancellation to (Sigma Q^T Sigma Q) (x) I_9, in which
    psi does not appear at all.  The `defect-order` mutant composes the
    four factors in the wrong order and must die at the involution and
    membership clauses."""
    PW = pmat(WSWAP)
    U = U_prep()
    compose_the_defect_in_the_wrong_order = (MUTANT == "defect-order")
    if compose_the_defect_in_the_wrong_order:
        X = mm(PW, mm(U, mm(PW, minv(U))))
        X = mm(X, mm(PW, PW))
    else:
        X = mm(PW, mm(minv(U), mm(PW, U)))
    p, s = signed_perm(X)
    t = None if p is None else tuple(p[j] for j in range(NC))
    return {"matrix": X, "perm": t,
            "is_a_signed_permutation": p is not None,
            "is_the_identity": t is not None and t == tuple(range(NC)),
            "name": "not a signed permutation" if t is None else name_perm(t),
            "order": None if t is None else perm_order(t),
            "fixed_points": None if t is None else fixed_points(list(t)),
            "equals_the_wing_exchange": t is not None and t == tuple(WSWAP),
            "equals_the_system_only_exchange":
                t is not None and t == tuple(XSSWAP),
            "equals_the_pointer_only_exchange":
                t is not None and t == tuple(XPSWAP),
            "mixed_relative_signs":
                None if s is None else len(set(relative_sign_class(s))) > 1}


def intertwining_table():
    """Does the wing exchange intertwine the two frames' legs, leg by leg?"""
    rows = {}
    PW = pmat(WSWAP)
    for sp in SETTING_ORDER:
        for leg in range(1, NLEGS + 1):
            L1 = legs_of(sp, "F1")[leg - 1]
            L2 = legs_of(sp, "F2")[leg - 1]
            rows["%s/leg%d" % (sp, leg)] = bool(mm(PW, mm(L2, PW)) == L1)
    return rows


def membership(t):
    tt = tuple(t)
    return {
        "in_the_declared_relabelling_scope":
            any(tuple(q) == tt for q in SCOPE["base"]),
        "in_the_declared_extension_scope":
            any(tuple(q) == tt for q in SCOPE["extension_all"]),
        "in_the_admitted_set":
            any(tuple(q) == tt for q in SCOPE["admitted"]),
        "in_the_admitted_extension":
            any(tuple(q) == tt for q in SCOPE["admitted_extension"])}


def run_patterns(graphs, values, pref, probes):
    """P1 .. P5, each gated separately."""
    prog("P1-P5: the five pre-registered patterns")
    # The completion's non-equivariance defect is computed FIRST, so that
    # the element it names is available to the printer before the group is
    # enumerated (the names are also registered before the probes run, in
    # `main`, so the negative control's holonomy is printed by name).
    # The registration is a printing convenience only: every predicate below
    # compares PERMUTATION TUPLES and no gate reads a name.
    D = prep_defect()
    if D["perm"] is not None:
        PERM_NAME.setdefault(canon(list(D["perm"])),
                             "the completion's non-equivariance defect")
        PERM_NAME.setdefault(
            canon(list(perm_compose(tuple(WSWAP), tuple(D["perm"])))),
            "the wing exchange composed with the non-equivariance defect")
        D["name"] = name_perm(D["perm"])
    hg = {sp: based_holonomy(sp, values) for sp in SETTING_ORDER}
    census = {sp: closed_path_census(sp, values) for sp in SETTING_ORDER}
    TABLES["closed_path_census"] = census
    FINDINGS["holonomy_group"] = {
        "per_setting": {sp: {k: v for k, v in hg[sp].items()
                             if not k.startswith("_")}
                        for sp in SETTING_ORDER},
        "description": "the based closed-loop holonomy at node F1@t0, read "
                       "as the permutation part of the closed-loop link "
                       "product, enumerated over every closed path of the "
                       "committed path space based there, and counted as "
                       "PERMUTATION TUPLES and never as name labels"}

    nontrivial = [sp for sp in SETTING_ORDER
                  if hg[sp]["generated_group_order"] > 1]
    nonflat = {sp: sum(n for k, n in census[sp].items()
                       if not k.endswith("the identity"))
               for sp in SETTING_ORDER}
    # Of the non-flat closed paths, how many carry a holonomy that is not a
    # signed permutation at all?  The two counts are printed against
    # different denominators elsewhere, so their relation is measured here.
    notsp = {sp: sum(n for k, n in census[sp].items()
                     if k.endswith("not a signed permutation"))
             for sp in SETTING_ORDER}
    # ---- P1 --------------------------------------------------------------
    gate("GEN-P1-NONTRIVIAL-HOLONOMY", "measurement",
         "P1 -- DOES A NONTRIVIAL HOLONOMY GROUP EXIST ON THE SECOND BASE?  "
         "The gate is a census over every closed path of the committed path "
         "space: at each setting it counts the closed paths whose "
         "amplitude-layer holonomy is NOT the identity permutation, and the "
         "order of the group generated at the declared base point.  The "
         "pattern HOLDS if some closed loop is non-flat and is ABSENT if "
         "every one of them is flat -- and an absence here would be a real "
         "result, reported plainly, not a failure of the run.  The negative "
         "control (GEN-NEGATIVE-CONTROL) is what makes the reading "
         "non-vacuous: the instrument is measured able to see a twist that "
         "is put there deliberately.  BOTH DIRECTIONS ARE IN THE PREDICATE "
         "AND NOT ONLY IN THE TABLE BESIDE IT: the gate requires some "
         "setting to carry a non-flat closed path AND every setting whose "
         "based group is trivial to carry NONE, so the measurement comes "
         "out both ways on one base by the gate's own predicate.  Of the "
         "non-flat closed paths, the number whose holonomy is not a signed "
         "permutation at all is counted against the same denominator and "
         "printed here rather than left to be inferred.  The "
         "`path-collapse` mutant gives every path one key, which makes the "
         "holonomy unreadable, and must die here",
         len(nontrivial) > 0
         and all(hg[sp]["closed_paths_based_there"] > 0
                 for sp in SETTING_ORDER)
         and all(nonflat[sp] == 0 for sp in SETTING_ORDER
                 if sp not in nontrivial),
         {"settings_with_a_nontrivial_based_holonomy_group": nontrivial,
          "generated_group_order_per_setting":
              {sp: hg[sp]["generated_group_order"] for sp in SETTING_ORDER},
          "non_flat_closed_paths_per_setting": nonflat,
          "of_those_non_flat_paths_the_ones_that_are_not_signed_"
          "permutations": notsp,
          "closed_paths_based_at_F1_t0_per_setting":
              {sp: hg[sp]["closed_paths_based_there"]
               for sp in SETTING_ORDER}})

    # ---- P2 --------------------------------------------------------------
    orders = {sp: hg[sp]["generated_group_order"] for sp in SETTING_ORDER}
    vs = {sp: hg[sp]["value_set_size"] for sp in SETTING_ORDER}
    struct = {}
    for sp in SETTING_ORDER:
        n = orders[sp]
        el = hg[sp]["element_orders"]
        if n == 1:
            nm = "trivial"
        elif n == 2:
            nm = "the cyclic group of order 2"
        elif n == 4 and el == [1, 2]:
            nm = "the Klein four-group"
        elif n == 4:
            nm = "the cyclic group of order 4"
        else:
            nm = ("elementary abelian of order %d" % n
                  if hg[sp]["the_group_is_abelian"] and el in ([1], [1, 2])
                  else "a group of order %d" % n)
        struct[sp] = nm
    FINDINGS["group_structure"] = struct
    gate("GEN-P2-GROUP-COMPUTED", "measurement",
         "P2 -- THE GROUP, COMPUTED, WHATEVER IT IS.  The value set is the "
         "set of PERMUTATION TUPLES realized by closed paths based at "
         "F1@t0; a set of NAMES would count as many elements as the naming "
         "table happens to know, which is a count of the wrong object.  The "
         "gate measures (1) that the value set has the same cardinality as "
         "the group it generates by closure, so the value set is already "
         "CLOSED at the declared length bound -- a measurement, not an "
         "assumption; (2) the group's order, its element orders and whether "
         "it is abelian, from which its isomorphism type is NAMED; (3) the "
         "number of closed paths based there whose holonomy is not a signed "
         "permutation, counted and printed rather than silently dropped.  "
         "Reproducing the first base's Klein four-group is NOT required: a "
         "different group is a discovery and is reported as the group it "
         "is.  THE ISOMORPHISM TYPE IS A READING AT THE DECLARED "
         "COMPLETION: the census of GEN-COMPLETION-CENSUS measures the type "
         "to be selected by the completion, so every statement of the type "
         "carries that scope tag and the existence of a nontrivial group is "
         "the completion-generic content.  The `label-collapse` mutant "
         "counts labels instead of permutations and must die at clause (1)",
         all(vs[sp] == orders[sp] for sp in SETTING_ORDER)
         and all(hg[sp]["the_value_set_is_the_generated_group"]
                 for sp in SETTING_ORDER)
         and all(hg[sp]["the_value_set_is_closed_under_composition"]
                 or orders[sp] == 1 for sp in SETTING_ORDER),
         {"the_scope_of_the_isomorphism_type":
              "at the declared completion V = H . Q (see "
              "GEN-COMPLETION-CENSUS)",
          "value_set_size_per_setting": vs,
          "generated_group_order_per_setting": orders,
          "structure_named_per_setting": struct,
          "element_orders_per_setting":
              {sp: hg[sp]["element_orders"] for sp in SETTING_ORDER},
          "abelian_per_setting":
              {sp: hg[sp]["the_group_is_abelian"] for sp in SETTING_ORDER},
          "elements_per_setting":
              {sp: hg[sp]["elements"] for sp in SETTING_ORDER},
          "element_fixed_points":
              {sp: hg[sp]["element_fixed_points"] for sp in SETTING_ORDER},
          "closed_paths_whose_holonomy_is_not_a_signed_permutation":
              {sp: hg[sp]["closed_paths_whose_holonomy_is_not_a_signed_"
                          "permutation"] for sp in SETTING_ORDER},
          "elements_with_mixed_relative_signs":
              {sp: hg[sp]["elements_with_mixed_relative_signs"]
               for sp in SETTING_ORDER}})

    # ---- P3 --------------------------------------------------------------
    mult = {}
    for sp in SETTING_ORDER:
        for t in CHECKPOINTS:
            maps = set()
            for rule in ID_RULES:
                adm = admits(sp, t, rule)
                if len(adm) == 1:
                    maps.add(tuple(adm[0]))
            mult["%s/t%d" % (sp, t)] = len(maps)
    subs = {}
    for sp in SETTING_ORDER:
        for rules in (("FULL",), ("REAL",), ("FULL", "REAL")):
            subs["%s/%s" % (sp, "+".join(rules))] = subconnection(sp, pref,
                                                                  rules)
    inter = intertwining_table()
    TABLES["mechanism"] = {
        "identification_multiplicity": mult,
        "coordinates_of_multiplicity_at_least_two":
            sorted(k for k, v in mult.items() if v >= 2),
        "single_rule_subconnections": subs,
        "the_wing_exchange_intertwines_the_leg": inter,
        "the_completions_non_equivariance_defect":
            {k: v for k, v in D.items() if k not in ("matrix", "perm")}}
    single_rule_nonflat = sorted(
        k for k, v in subs.items()
        if v["max_identification_multiplicity_at_one_coordinate"] <= 1
        and v["non_identity_closed_paths"] > 0)
    multi = sorted(k for k, v in mult.items() if v >= 2)
    gate("GEN-P3-TWO-CURVATURE-SOURCES", "measurement",
         "P3 -- THE TWO CURVATURE SOURCES, EACH EXHIBITED OR ITS ABSENCE "
         "MEASURED.  SOURCE (i), IDENTIFICATION MULTIPLICITY: the number of "
         "DISTINCT admitted maps drawn at each (setting, checkpoint) is "
         "counted, and the coordinates carrying two are named.  To isolate "
         "it, the SINGLE-RULE sub-connections are built and enumerated "
         "SEPARATELY -- in each of them every coordinate carries at most one "
         "admitted map, so a non-identity closed path there is holonomy "
         "that multiplicity cannot explain.  SOURCE (ii), THE COMPLETION'S "
         "NON-EQUIVARIANCE DEFECT: D = P_W U_prep^-1 P_W U_prep is computed "
         "exactly on this base, tested for being a signed permutation, and "
         "named by what it does -- its order, its fixed-point count and "
         "whether it is the wing exchange or either of its two halves.  The "
         "wing exchange's intertwining of every declared leg is measured "
         "leg by leg, so the defect's cause is exhibited and not asserted; "
         "the closed form that identifies the defect as a function of the "
         "declared COMPLETION alone -- and not of the preparation VECTOR -- "
         "is derived and gated at GEN-DEFECT-LAW.  "
         "The gate requires BOTH sources to be measured and reported: at "
         "least one coordinate of multiplicity two, at least one "
         "single-rule sub-connection measured non-flat, and a defect "
         "element that is not the identity.  The `defect-order` mutant "
         "composes the defect's factors in the wrong order and must die "
         "here",
         len(multi) > 0 and len(single_rule_nonflat) > 0
         and not D["is_the_identity"],
         {"coordinates_of_multiplicity_at_least_two": multi,
          "single_rule_subconnections_measured_non_flat":
              single_rule_nonflat,
          "the_completions_non_equivariance_defect":
              {k: v for k, v in D.items() if k not in ("matrix", "perm")},
          "the_wing_exchange_intertwines_the_preparation_leg":
              {k: v for k, v in inter.items() if k.endswith("leg1")},
          "legs_the_wing_exchange_intertwines":
              sorted(k for k, v in inter.items() if v)})

    # ---- P4 --------------------------------------------------------------
    inpg = {}
    for sp in SETTING_ORDER:
        grp = {tuple(z) for z in hg[sp]["_group"]}
        inpg[sp] = (D["perm"] is not None and tuple(D["perm"]) in grp)
    gate("GEN-P4-DEFECT-IS-A-GROUP-ELEMENT", "measurement",
         "P4 -- IS THE PREPARATION-DEFECT AN ELEMENT OF THE HOLONOMY "
         "GROUP?  The question is decided by permutation-tuple membership: "
         "the defect's own permutation, computed in P3 from the declared "
         "preparation and the wing exchange, is tested against the group "
         "computed in P2 from the enumerated closed paths -- two "
         "independent computations, compared as tuples and never as names.  "
         "The gate measures that the defect IS an element at every setting "
         "whose group is nontrivial, and that it is NOT an element where "
         "the group is trivial (where the only element is the identity and "
         "the defect is measured not to be it).  The second half is what "
         "makes the first a measurement rather than a tautology.  The "
         "`defect-order` mutant perturbs the defect and must die here",
         all(inpg[sp] for sp in nontrivial)
         and all(not inpg[sp] for sp in SETTING_ORDER
                 if sp not in nontrivial)
         and len(nontrivial) > 0,
         {"the_defect_is_an_element_per_setting": inpg,
          "the_defect_name": D["name"],
          "the_defect_order": D["order"],
          "the_defect_fixed_points": D["fixed_points"],
          "settings_with_a_nontrivial_group": nontrivial})

    # ---- P5 --------------------------------------------------------------
    esc = {}
    for sp in SETTING_ORDER:
        rows = {}
        for z in hg[sp]["_group"]:
            m = membership(z)
            m["order"] = perm_order(tuple(z))
            m["fixed_points"] = fixed_points(z)
            m["mixed_relative_signs"] = (
                name_perm(tuple(z))
                in hg[sp]["elements_with_mixed_relative_signs"])
            rows[name_perm(tuple(z))] = m
        esc[sp] = rows
    outside = {sp: sum(1 for r in esc[sp].values()
                       if not r["in_the_declared_relabelling_scope"]
                       and not r["in_the_declared_extension_scope"])
               for sp in SETTING_ORDER}
    # WHAT KIND OF TRANSPORT EACH LINK IS, measured link by link at a
    # setting whose group is nontrivial: the identification links are drawn
    # from the admitted set by construction, but the LEG links are not
    # transports the base admits at all, and that is a measurement.
    link_kinds = {}
    if nontrivial:
        spx = sorted(nontrivial)[0]
        Gx = graphs[spx]
        for li, L in enumerate(Gx["links"]):
            M = link_variable(spx, L, +1)
            p, _s = signed_perm(M)
            if p is None:
                link_kinds["link%02d/%s" % (li, L["kind"])] = {
                    "what_it_is": "not a signed permutation at all",
                    "in_any_declared_collection": False}
            else:
                t = tuple(p[j] for j in range(NC))
                m = membership(t)
                link_kinds["link%02d/%s" % (li, L["kind"])] = {
                    "what_it_is": ("the permutation %s" % name_perm(t)),
                    "in_the_declared_relabelling_scope":
                        m["in_the_declared_relabelling_scope"],
                    "in_the_admitted_set": m["in_the_admitted_set"],
                    "in_any_declared_collection": any(m.values())}
    leg_links_outside = sum(1 for k, v in link_kinds.items()
                            if k.endswith("/leg")
                            and not v["in_any_declared_collection"])
    id_links_inside = sum(1 for k, v in link_kinds.items()
                          if k.endswith("/id")
                          and v.get("in_the_admitted_set"))
    # THE FORCEDNESS OF THE MEMBERSHIP TABLE, measured (RUNBOOK section 14
    # addendum: an analytically forced clause is a disclosure).  Each of the
    # four collections is measured invariant under left multiplication by
    # the wing exchange, and the inclusions between them are measured; those
    # two facts force every cell of the table except one.
    coll = {"the declared relabelling scope": SCOPE["base"],
            "the declared extension scope": SCOPE["extension_all"],
            "the admitted set": SCOPE["admitted"],
            "the admitted extension": SCOPE["admitted_extension"]}
    winv, contains = {}, {}
    for nm, C in coll.items():
        cs = {tuple(p) for p in C}
        winv[nm] = ({perm_compose(tuple(WSWAP), tuple(p)) for p in C} == cs)
        contains[nm] = {"the identity": tuple(IDPERM) in cs,
                        "the wing exchange": tuple(WSWAP) in cs}
    incl = {
        "admitted set inside the declared relabelling scope":
            {tuple(p) for p in SCOPE["admitted"]}
            <= {tuple(p) for p in SCOPE["base"]},
        "declared relabelling scope inside the declared extension":
            {tuple(p) for p in SCOPE["base"]}
            <= {tuple(p) for p in SCOPE["extension_all"]},
        "admitted extension inside the declared extension":
            {tuple(p) for p in SCOPE["admitted_extension"]}
            <= {tuple(p) for p in SCOPE["extension_all"]}}
    TABLES["structure_group"] = {
        "per_setting": esc,
        "elements_outside_every_declared_collection": outside,
        "what_each_link_of_a_nontrivial_setting_is": link_kinds,
        "leg_links_outside_every_declared_collection": leg_links_outside,
        "identification_links_in_the_admitted_set": id_links_inside,
        "each_collection_is_invariant_under_the_wing_exchange": winv,
        "each_collection_contains": contains,
        "inclusions_between_the_collections": incl,
        "the_wing_exchange_factorises_as_XS_XP":
            perm_compose(tuple(XSSWAP), tuple(XPSWAP)) == tuple(WSWAP),
        "membership_of_the_two_halves_of_the_wing_exchange": {
            "the system-only wing exchange": membership(XSSWAP),
            "the pointer-only wing exchange": membership(XPSWAP)},
        "membership_of_the_non_equivariance_defect":
            None if D["perm"] is None else membership(D["perm"])}
    gate("GEN-P5-NON-PRINCIPALITY", "measurement",
         "P5 -- DOES THE GROUP ESCAPE THE BASE'S OWN DECLARED SCOPES?  "
         "Membership of EVERY holonomy element in EVERY declared and "
         "admitted collection is computed, element by element and "
         "collection by collection: the declared relabelling scope, its "
         "declared extension, and the two subsets of those that survive the "
         "j0 filter and over which every admission search in this unit "
         "runs.  Every IDENTIFICATION link of this connection is a "
         "transport the base admits -- by construction, since admission "
         "searches the admitted set -- while the LEG links are measured "
         "NOT to be transports the base admits at all: at a setting whose "
         "group is nontrivial the preparation legs are measured not to be "
         "signed permutations and the local legs, which ARE permutations of "
         "the configurations, are measured outside all four collections.  "
         "The question is whether the GROUP THOSE LINKS GENERATE AROUND "
         "LOOPS is a subgroup of the base's own isomorphisms.  The gate "
         "measures that at least one element of at least one setting's "
         "group lies outside every declared collection -- non-principality "
         "-- and that at the settings whose group is trivial the count is "
         "zero, so the measurement can come out both ways and does.  The "
         "escape's STRENGTH is bounded by how small the declared scope is, "
         "which is a declaration and is stated as one.  The `scope-lax` "
         "mutant subsamples the admitted scope and must die at GEN-ARENA or "
         "here",
         any(outside[sp] > 0 for sp in SETTING_ORDER)
         and all(outside[sp] == 0 for sp in SETTING_ORDER
                 if sp not in nontrivial),
         {"elements_outside_every_declared_collection": outside,
          "per_setting": esc,
          "what_each_link_of_a_nontrivial_setting_is": link_kinds,
          "leg_links_outside_every_declared_collection": leg_links_outside,
          "identification_links_in_the_admitted_set": id_links_inside,
          "membership_of_the_non_equivariance_defect":
              None if D["perm"] is None else membership(D["perm"])})
    gate("GEN-P5-FORCEDNESS", "disclosure",
         "HOW MUCH OF P5'S MEMBERSHIP TABLE IS FREE, MEASURED AND "
         "DISCLOSED (RUNBOOK section 14 addendum).  The table has one row "
         "per holonomy element and one column per declared collection, but "
         "its cells are not independent, and this disclosure measures why.  "
         "Each of the four collections is measured INVARIANT under left "
         "multiplication by the wing exchange, and each is measured to "
         "contain the identity and the wing exchange -- so those two rows "
         "are forced 'yes' everywhere by the scope's own generators, and "
         "the W.D row is forced to repeat the D row.  The inclusions "
         "admitted-set c declared-scope c declared-extension and "
         "admitted-extension c declared-extension are measured -- so a "
         "single 'no' at the widest collection forces the other three.  "
         "What remains free is exactly ONE cell: whether the defect lies "
         "outside the declared EXTENSION.  P5's verdict is that one "
         "measurement, and the table is its consequence",
         True,
         {"each_collection_is_invariant_under_the_wing_exchange": winv,
          "each_collection_contains": contains,
          "inclusions_between_the_collections": incl,
          "the_one_free_cell":
              "the non-equivariance defect is outside the declared "
              "extension scope",
          "the_free_cell_measured":
              (None if D["perm"] is None
               else not membership(D["perm"])
               ["in_the_declared_extension_scope"])})
    FINDINGS["patterns"] = {
        "P1_nontrivial_holonomy_exists": len(nontrivial) > 0,
        "P1_settings": nontrivial,
        "P2_group_order": orders,
        "P2_structure": struct,
        "P3_multiplicity_coordinates": multi,
        "P3_single_rule_subconnections_non_flat": single_rule_nonflat,
        "P3_non_equivariance_defect":
            {k: v for k, v in D.items() if k not in ("matrix", "perm")},
        "P4_defect_is_a_group_element": inpg,
        "P5_elements_outside_every_declared_collection": outside}
    return hg, D, subs, esc, nontrivial, struct


# ===========================================================================
# 8.  THE GAUGE SELF-TEST (RUNBOOK section 14) -- FRESH, and with teeth
# ===========================================================================
def gauge_group(G):
    """THE DECLARED SWITCHING GROUP: one sign per link of the setting's own
    graph, legs and identifications alike.  Its order is computed by
    enumeration, never typed.  The CHECKPOINT subgroup is the part induced
    by a sign at each NODE -- the base's own checkpoint-phase redundancy --
    and is enumerated separately."""
    ix = list(range(len(G["links"])))
    order = 2 ** len(ix)
    full = [dict(zip(ix, eps))
            for eps in itertools.product((1, -1), repeat=len(ix))]
    if MUTANT == "gauge-subsample":
        full = full[:1]
    cp, seen = [], set()
    for s in itertools.product((1, -1), repeat=len(NODES)):
        sn = dict(zip(NODES, s))
        sw = {li: sn[G["links"][li]["a"]] * sn[G["links"][li]["b"]]
              for li in ix}
        key = canon(sorted(sw.items()))
        if key not in seen:
            seen.add(key)
            cp.append(sw)
    return {"links": ix, "full": full, "checkpoint": cp,
            "order": order, "swept": len(full)}


def switched_signs(edges, sw):
    """The sign the switching puts on each traversal.  The `gauge-sign`
    mutant drops the switching on a REVERSED traversal -- the
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
    """Recomputed from the link variables EVERY time (section 14 addendum).
    The call is routed THROUGH the instrument's value cache so that the
    bypass is a MEASURED fact and not an absence: in fresh mode the cache is
    bypassed and every call counts a MISS, while the `memo-lax` mutant
    restores the reviewed defect and the checkpoint subgroup's re-visits of
    switchings already swept register as HITS."""
    def build():
        acc = sp_id()
        for k in range(len(A)):
            acc = mm_memo(A[k] if signs[k] > 0 else negA[k], acc)
        return acc
    return _memo(("loop", sp, key), build)


def prime_the_value_cache(graphs):
    """EXERCISE THE CACHE PATH BEFORE THE SELF-TEST BYPASSES IT (RUNBOOK
    section 14 addendum, second half: a zero-hit gate must also gate that
    the cache path IS exercised -- zero hits of zero lookups is vacuous).

    Every declared loop that carries an edge list has its all-positive
    holonomy computed here in NON-fresh mode, under exactly the key the
    self-test will later request.  So the cache is measured populated, its
    read path is measured to return stored values (the second pass over the
    same keys), and the self-test's zero hits are then zero hits against a
    populated cache that was asked for those very entries."""
    prog("priming the value cache (so the bypass has something to bypass)")
    primed = 0
    for _pass in (1, 2):
        for sp in SETTING_ORDER:
            G = graphs[sp]
            for loop in declared_loops(sp, G):
                if loop["edges"] is None:
                    continue
                A = [link_variable(sp, G["links"][li], d)
                     for (li, d) in loop["edges"]]
                negA = [sp_neg(X) for X in A]
                sg = [1] * len(A)
                loop_matrix_fresh(sp, A, negA, sg,
                                  (loop["name"], tuple(sg)))
                primed += 1
    return primed


def run_gauge_selftest(graphs):
    global _FRESH
    primed = prime_the_value_cache(graphs)
    prog("section 14: the gauge-covariance self-test (fresh evaluation)")
    _FRESH = True
    before = dict(_CACHE)
    rows, sizes = {}, {}
    not_signed = perm_moved = sign_fail = scalar_dev = moved_raw = 0
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
        # EVERY declared loop that carries an edge list, in the order the
        # probes are built, never selected by the verdicts under audit.
        swept = [x for x in declared_loops(sp, G) if x["edges"] is not None]
        for loop in swept:
            A = [link_variable(sp, G["links"][li], d)
                 for (li, d) in loop["edges"]]
            negA = [sp_neg(X) for X in A]
            H0 = sp_id()
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
                    tot = 1
                    for e in sg:
                        tot *= e
                    comparisons += 1
                    if H != (H0 if tot > 0 else sp_neg(H0)):
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
        prog("  swept %s (%d loops)" % (sp, len(swept)))
    after = dict(_CACHE)
    hits = after["value_cache_hits"] - before["value_cache_hits"]
    misses = after["value_cache_misses"] - before["value_cache_misses"]
    cached_keys_requested = (
        after["fresh_requests_for_a_key_already_in_the_cache"]
        - before["fresh_requests_for_a_key_already_in_the_cache"])
    _FRESH = False
    TABLES["gauge_selftest"] = {
        "per_loop": rows, "group_sizes": sizes,
        "loops_swept_per_setting": {sp: sum(1 for k in rows
                                            if k.startswith(sp + " /"))
                                    for sp in SETTING_ORDER},
        "the_declared_probe_excluded_from_the_sweep":
            "the twisted comparator: it carries no edge list of its own, "
            "being the canonical loop with one link overwritten"}
    gate("GEN-GAUGE-COVARIANCE", "measurement",
         "THE MANDATORY SECTION 14 SELF-TEST, STATED AT WHAT IT MEASURES.  "
         "Every declared loop that has an edge list -- ALL of them, not one "
         "per role -- has its holonomy RECOMPUTED FROM THE LINK VARIABLES "
         "under EVERY element of the declared switching group, and the "
         "sweep is measured COMPLETE at every setting.  The gate measures "
         "four things that CAN fail: (1) the declared switching acts on a "
         "closed loop by the GLOBAL SCALAR given by the product of the "
         "signs it puts on the traversals -- every swept holonomy is "
         "compared, exactly, against that scalar times the unswitched "
         "holonomy built by the plain product routine, so the memoising "
         "routine is measured against the plain one on every instance; "
         "(2) every swept holonomy is a SIGNED PERMUTATION at all, which "
         "for the eight-link canonical loop of non-permutation matrices is "
         "a real fact; (3) the loop's SIGN is fixed under the whole "
         "checkpoint subgroup -- the telescoping property a wrong sign "
         "convention breaks; (4) the group orders are the enumerated powers "
         "of two and the checkpoint subgroup has the enumerated order.  The "
         "`gauge-sign` mutant drops the switching on a reversed traversal "
         "and must die at clauses (1) and (3); the `gauge-subsample` mutant "
         "shrinks the sweep and must die at clause (4).  THE INVARIANCE OF "
         "THE PERMUTATION PART IS NOT A CLAUSE OF THIS GATE: it FOLLOWS "
         "from clause (1) and is reported as the disclosure "
         "GEN-GAUGE-PERMUTATION-FORCED",
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
    gate("GEN-GAUGE-PERMUTATION-FORCED", "disclosure",
         "AN ANALYTICALLY FORCED CLAUSE, REPORTED AS A DISCLOSURE AND NOT "
         "AS A MUST-PASS MEASUREMENT.  The declared switching assigns one "
         "sign per link, so it acts on a CLOSED loop's link product by the "
         "product of those signs -- a global +-1 (measured: clause (1) of "
         "GEN-GAUGE-COVARIANCE, %d exact comparisons, %d deviations).  A "
         "signed permutation matrix and its negative have the SAME "
         "permutation part.  Therefore the permutation part of a closed "
         "loop's holonomy is invariant under the whole switching group BY "
         "ALGEBRA, for every loop, every setting and every switching, "
         "whatever else in this instrument were wrong: no switching and no "
         "mutant could make this clause fail, and it is not claimed as a "
         "measurement.  The sweep confirms it -- exactly one permutation "
         "part at every declared loop, over the COMPLETE group -- and that "
         "confirmation is what is reported here.  The same algebra makes "
         "the RELATIVE sign class s_j*s_0 invariant while the raw sign set "
         "is not, which is why the relative class is the sign content this "
         "unit reports" % (comparisons, scalar_dev),
         True,
         {"loops_whose_permutation_part_moved_under_the_full_group":
              perm_moved,
          "loops_swept": len(rows),
          "distinct_relative_sign_classes_per_loop":
              sorted({v["distinct_relative_sign_classes_under_the_full_"
                        "group"] for v in rows.values()})})
    gate("GEN-GAUGE-CONTROL-MOVES", "measurement",
         "THE MIS-CONVENTIONED CONTROL MOVES.  A quantity that reads the "
         "closed loop's RAW SIGN -- the gauge-orbit datum a report of "
         "'the signs' would promote to physics -- is measured to MOVE under "
         "the declared switching group at at least one declared loop.  A "
         "sweep under which nothing moves cannot certify an invariance, so "
         "this gate is the sweep's own tooth; the `gauge-subsample` mutant "
         "collapses the sweep and must die here",
         moved_raw > 0,
         {"loops_at_which_the_raw_sign_moved": moved_raw,
          "loops_swept": len(rows)})
    gate("GEN-FRESH-EVAL", "measurement",
         "THE SELF-TEST EVALUATES FRESH, AGAINST A CACHE MEASURED TO BE "
         "POPULATED AND MEASURED TO WORK (RUNBOOK section 14 addendum, both "
         "halves).  Every holonomy in the sweep is rebuilt from the link "
         "variables with the instrument's value cache bypassed.  A zero hit "
         "count is only worth something if the cache path is EXERCISED, so "
         "before the sweep the cache is PRIMED: every declared loop with an "
         "edge list has its all-positive holonomy stored under exactly the "
         "key the sweep will later request, and a second pass over the same "
         "keys is measured to return the STORED values -- so the read path "
         "is measured to work and the store is measured non-empty.  Four "
         "clauses, each of which can fail: (1) the cache is measured "
         "populated (writes positive); (2) the cache's read path is "
         "measured to serve stored values (reads that returned a stored "
         "value positive); (3) the sweep is measured to REQUEST keys that "
         "are in the populated cache, positively many of them; (4) the "
         "sweep's cache-HIT count is nevertheless ZERO, against a positive "
         "MISS count.  The `memo-lax` mutant lets the phase read the cache "
         "and must die at clause (4), turning every one of those requests "
         "into a hit",
         hits == 0 and misses > 0
         and _CACHE["value_cache_writes"] > 0
         and _CACHE["cache_reads_that_returned_a_stored_value"] > 0
         and cached_keys_requested > 0,
         {"value_cache_hits_during_the_self_test": hits,
          "value_cache_misses_during_the_self_test": misses,
          "entries_written_into_the_cache_before_the_self_test":
              _CACHE["value_cache_writes"],
          "cache_reads_that_returned_a_stored_value":
              _CACHE["cache_reads_that_returned_a_stored_value"],
          "self_test_requests_for_a_key_already_in_the_cache":
              cached_keys_requested,
          "cache_lookups_outside_the_self_test":
              _CACHE["value_cache_lookups"],
          "priming_calls": primed})
    return rows, sizes


# ===========================================================================
# 9.  THE DECLARATION FLIP-TESTS
# ===========================================================================
def run_flip_tests(graphs, probes):
    """Wherever a bookkeeping split exists, the declaration is flipped and
    the verdict is measured to be invariant -- or the dependence is
    reported as the result it is."""
    prog("the declaration flip-tests")
    rows = {}
    bad = 0
    for sp in SETTING_ORDER:
        G = graphs[sp]
        for loop in declared_loops(sp, G):
            if loop["edges"] is None:
                continue
            fwd = {"start": loop["base"], "end": loop["base"],
                   "edges": loop["edges"]}
            rev = {"start": loop["base"], "end": loop["base"],
                   "edges": [(li, -d) for (li, d) in
                             reversed(loop["edges"])]}
            Hf = transport_along(sp, G, fwd, "A")
            Hr = transport_along(sp, G, rev, "A")
            pf, _ = signed_perm(Hf)
            pr, _ = signed_perm(Hr)
            ok = (pf is not None and pr is not None
                  and tuple(pr[j] for j in range(NC))
                  == tuple(perm_inverse([pf[j] for j in range(NC)])))
            if not ok:
                bad += 1
            rows["%s / %s" % (sp, loop["name"])] = {
                "forward": (name_perm(tuple(pf[j] for j in range(NC)))
                            if pf else "not a signed permutation"),
                "reversed_is_the_inverse": ok}
    flip_ok = (bad == 0 and len(rows) > 0)
    if MUTANT == "flip-lax":
        flip_ok = False
    TABLES["flip_tests"] = {"direction": rows,
                            "loops_flipped": len(rows),
                            "loops_where_the_reversal_is_not_the_inverse":
                                bad}
    gate("GEN-FLIP-DIRECTION", "measurement",
         "THE DIRECTION FLIP-TEST (must-pass).  Every declared loop that "
         "carries an edge list is re-traversed with the direction "
         "convention flipped, and the resulting permutation is measured to "
         "be the INVERSE of the forward one, at every loop and every "
         "setting -- so no holonomy verdict in this unit depends on which "
         "way round the bookkeeping runs the loop.  ITS POSITIVE CONTENT IS "
         "FORCED, AND THAT IS STATED HERE RATHER THAN LEFT TO BE "
         "DISCOVERED: every link variable is measured orthogonal and the "
         "reverse traversal is implemented as the transpose, so a reversed "
         "loop's matrix is the inverse of the forward one BY ALGEBRA for "
         "any input, and every element of this base's holonomy group is "
         "measured to be an involution, so the inverse permutation is the "
         "same permutation at every one of these loops.  What the gate "
         "retains is instrument integrity, and that is not forced: the "
         "`orient-flip` mutant reads a leg's reverse traversal WITHOUT "
         "transposing, which breaks the relation, and it is what gives this "
         "gate its teeth; the `flip-lax` waiver overwrites the predicate "
         "and dies here too.  Coverage is stated: the twisted comparator is "
         "the canonical loop with one link overwritten and carries no edge "
         "list of its own, so the NEGATIVE CONTROL IS NOT FLIP-TESTED",
         flip_ok,
         {"loops_flipped": len(rows),
          "loops_where_the_reversal_is_not_the_inverse": bad,
          "the_declared_probe_not_flip_tested": "the twisted comparator"})
    return rows


def species_clauses(V):
    """THE FOUR CLAUSES OF THE DECLARED SPECIES, measured on a base built
    with the completion V.  Called on the ALTERNATIVE completion so that
    the question 'is the alternative of the declared species?' is answered
    by measurement rather than by assertion."""
    ops = {}
    for fr in FRAMES:
        for sp in SETTING_ORDER:
            for k, L in enumerate(legs_of(sp, fr)):
                ops["%s/%s/leg%d" % (sp, fr, k + 1)] = is_orthogonal(L)
    commute = {}
    for a in ROT_ORDER:
        for b in ROT_ORDER:
            commute["A(%s),B(%s)" % (a, b)] = (
                mm(U_local("A", a), U_local("B", b))
                == mm(U_local("B", b), U_local("A", a)))
    Mc = [[V[a * NS + b][0] for b in range(NS)] for a in range(NS)]
    A = [row[:] for row in Mc]
    rank = 0
    for c in range(NS):
        piv = next((i for i in range(rank, NS) if A[i][c]), None)
        if piv is None:
            continue
        A[rank], A[piv] = A[piv], A[rank]
        inv = ONE / A[rank][c]
        A[rank] = [inv * v for v in A[rank]]
        for i in range(NS):
            if i != rank and A[i][c]:
                f = A[i][c]
                A[i] = [x - f * y for x, y in zip(A[i], A[rank])]
        rank += 1
    V_orth = all(sum((V[k][i] * V[k][j] for k in range(NS * NS)), ZERO)
                 == (ONE if i == j else ZERO)
                 for i in range(NS * NS) for j in range(NS * NS))
    shifts = [pointer_shift(o) for o in range(NS)]
    return {"two_wings_with_commuting_local_legs": all(commute.values()),
            "a_preparation_common_to_both_frames_and_entangled":
                V_orth and rank >= 2,
            "the_preparation_schmidt_rank": rank,
            "records_at_the_final_division_event_shift_injective":
                len(set(shifts)) == NS,
            "every_declared_operator_exactly_orthogonal":
                all(ops.values()),
            "all_four_clauses_hold":
                all(commute.values()) and V_orth and rank >= 2
                and len(set(shifts)) == NS and all(ops.values())}


def with_completion(V, settings=None, species=False, bound=None):
    """Rebuild the base on a DIFFERENT declared completion and return its
    admission table, its holonomy group and its non-equivariance defect.
    The fixture store is swapped out and restored, so nothing this measures
    leaks into any verdict above.  `settings` declares WHICH settings are
    rebuilt (all six for the flip-test; the census sweep declares the
    symmetric setting GP-E and GP-A as its flat control, and prints that
    scope)."""
    global VCOMP, _FIXTURE, _INTERN, _INTERN_VALUE, _HOL_CLASS
    keepV, keepF = VCOMP, _FIXTURE
    keepI, keepIV, keepH = _INTERN, _INTERN_VALUE, _HOL_CLASS
    VCOMP, _FIXTURE = V, {}
    _INTERN, _INTERN_VALUE, _HOL_CLASS = {}, {}, {}
    sps = list(SETTING_ORDER) if settings is None else list(settings)
    try:
        born_sym = all(VCOMP[i][j] * VCOMP[i][j]
                       == VCOMP[SIGMA9[i]][SIGMA9[j]]
                       * VCOMP[SIGMA9[i]][SIGMA9[j]]
                       for i in range(NS * NS) for j in range(NS * NS))
        pref = prefix_profile()
        table, per_rule = {}, {r["id"]: 0 for r in ID_RULES}
        for sp in sps:
            for t in CHECKPOINTS:
                cell = {r["id"]: len(admits(sp, t, r)) for r in ID_RULES}
                table["%s/t%d" % (sp, t)] = cell
                for r in ID_RULES:
                    if cell[r["id"]] == 1:
                        per_rule[r["id"]] += 1
        drawn = sum(1 for r in table.values()
                    for v in r.values() if v == 1)
        graphs = {sp: build_graph(sp, pref) for sp in sps}
        groups, canon_loop = {}, {}
        for sp in sps:
            rows = enumerate_paths(sp, graphs[sp], L_MAX)
            groups[sp] = based_holonomy(sp, {sp: rows},
                                        closure_bound=bound)
            canon_loop[sp] = any(x["name"] == "the canonical loop"
                                 for x in declared_loops(sp, graphs[sp]))
        D = prep_defect()
        out = {"born_shadow_of_the_completion_is_exchange_symmetric":
                   born_sym,
               "settings_rebuilt": sps,
               "admission_counts_per_cell": table,
               "cells_where_a_link_is_drawn": drawn,
               "cells_where_each_rule_draws_a_link": per_rule,
               "the_canonical_loop_exists_per_setting": canon_loop,
               "settings_where_the_canonical_loop_exists":
                   sum(1 for v in canon_loop.values() if v),
               "identification_links_per_setting":
                   {sp: sum(1 for L in graphs[sp]["links"]
                            if L["kind"] == "id") for sp in sps},
               "holonomy_group_order_per_setting":
                   {sp: groups[sp]["generated_group_order"] for sp in sps},
               "holonomy_group_is_abelian_per_setting":
                   {sp: groups[sp]["the_group_is_abelian"] for sp in sps},
               "holonomy_element_orders_per_setting":
                   {sp: groups[sp]["element_orders"] for sp in sps},
               "value_set_size_per_setting":
                   {sp: groups[sp]["value_set_size"] for sp in sps},
               "the_value_set_is_closed_at_the_bound_per_setting":
                   {sp: groups[sp]["the_value_set_is_closed_under_"
                                   "composition"] for sp in sps},
               "the_declared_closure_bound_was_reached":
                   any(groups[sp]["the_declared_closure_bound_was_reached"]
                       for sp in sps),
               "the_completions_non_equivariance_defect":
                   {k: v for k, v in D.items()
                    if k not in ("matrix", "perm")}}
        if species:
            out["the_declared_species_measured_on_this_completion"] = \
                species_clauses(V)
        return out
    finally:
        VCOMP, _FIXTURE = keepV, keepF
        _INTERN, _INTERN_VALUE, _HOL_CLASS = keepI, keepIV, keepH


def run_completion_flip(declared_summary):
    """THE DECLARED COMPLETION FLIP-TEST.  The completion is a declaration,
    and this measures what depends on it -- reported, folded into no
    verdict."""
    prog("the declared completion flip-test (the bare Householder)")
    alt = with_completion(householder(), species=True)
    TABLES["completion_flip_test"] = {
        "declared_completion": declared_summary,
        "alternative_completion_V_equals_H":
            "the bare Householder reflection, i.e. the declared completion "
            "with Q taken to be the identity instead of the declared "
            "transposition; its first column is the SAME psi",
        "measured_at_the_alternative": alt}
    gate("GEN-COMPLETION-FLIP", "disclosure",
         "THE COMPLETION IS A DECLARATION, AND WHAT DEPENDS ON IT IS "
         "MEASURED RATHER THAN ASSERTED.  The preparation's orthogonal "
         "completion is pinned as data because a completion is never "
         "forced: the same preparation VECTOR psi admits many orthogonal "
         "completions, and this unit declares one.  The flip-test rebuilds "
         "the entire base on the alternative completion -- the bare "
         "Householder reflection, the declared completion with the "
         "transposition Q removed, whose first column is the SAME psi -- "
         "and re-measures the admission table, the identification links "
         "drawn, the holonomy group order at every setting and the "
         "non-equivariance defect.  WHAT THE ALTERNATIVE STILL HAS IS "
         "MEASURED TOO, and it is not nothing: the four clauses of the "
         "declared species are measured to HOLD on it, the full-leg rule is "
         "measured still to draw links, and the canonical loop is measured "
         "still to exist at the settings named below -- so the five "
         "patterns are POSABLE there and are posed, and the answer is the "
         "pre-registered outcome GEN-STRUCTURE-ABSENT rather than an "
         "unposable question.  What the alternative loses is measured "
         "exactly: the wing exchange intertwines the preparation leg (the "
         "completion is exchange-EQUIVARIANT), so the defect is the "
         "identity, and at the symmetric settings the full-leg rule admits "
         "two permutations where it had admitted one.  The census of "
         "GEN-COMPLETION-CENSUS places this completion in its family.  The "
         "measurement is folded into NO verdict: every result of this unit "
         "stands at the DECLARED completion and at no other, and that "
         "scope statement is what this disclosure exists to license",
         True, alt)
    return alt


# ===========================================================================
# 9b.  THE COMPLETION CENSUS -- the defect law, the exhaustive family sweep,
#      the group family, and the rebuilds.
#
#      The three constructions gated here -- the closed form for the defect,
#      the exhaustive census of the completion family, and the enumeration
#      of Klein connections on the gauge-fixed graph -- were contributed by
#      this unit's review panel and are re-derived and re-measured natively
#      here (v13 LOG #219).
# ===========================================================================
ENUMERATION_CAP = 100000        # declared: the connection space is swept
#                                 exhaustively below this many assignments
CLOSURE_BOUND = 256             # declared: the rebuild sweep's group-closure
#                                 bound; the sweep gates that it is never
#                                 reached (the measured orders are <= 30)

# The declared alternative preparation VECTORS.  Each is rational, of unit
# norm, and (except the last, which is the negative control) invariant under
# the exchange of the two systems.  They exist to measure the psi-
# independence of the defect -- and, at the control, to measure that the
# invariance hypothesis is load-bearing rather than decorative.
PSI_FAMILY = (
    ("the declared psi", {(0, 1): "2/3", (1, 0): "2/3", (2, 2): "1/3"}, True),
    ("psi-2", {(0, 0): "1/3", (1, 2): "2/3", (2, 1): "2/3"}, True),
    ("psi-3", {(0, 0): "4/5", (1, 1): "3/5"}, True),
    ("psi-4", {(0, 1): "1/2", (1, 0): "1/2", (1, 2): "1/2", (2, 1): "1/2"},
     True),
    ("psi-5 (NOT exchange-invariant: the negative control)",
     {(0, 1): "3/5", (1, 0): "4/5"}, False),
)


def perm9_inverse(p):
    o = [0] * len(p)
    for i, v in enumerate(p):
        o[v] = i
    return tuple(o)


def perm9_compose(x, y):
    return tuple(x[y[i]] for i in range(len(y)))


def perm9_order(p):
    q, n, ident = tuple(p), 1, tuple(range(len(p)))
    while q != ident:
        q = perm9_compose(tuple(p), q)
        n += 1
    return n


def defect_permutation_of(q):
    """THE CANCELLATION FORM, as a permutation of the nine system-pair
    indices: delta(Q) = sigma . Q^-1 . sigma . Q.  psi does not appear."""
    s = tuple(SIGMA9)
    return perm9_compose(perm9_compose(s, perm9_inverse(q)),
                         perm9_compose(s, q))


def householder_of(coeffs):
    """The Householder reflection carrying e_{(0,0)} to the declared vector
    with the given rational coefficients."""
    psi = [ZERO] * (NS * NS)
    for (a, b), v in coeffs.items():
        psi[a * NS + b] = parse_fr(v)
    w = list(psi)
    w[0] = w[0] - ONE
    ww = sum(v * v for v in w)
    H = [[(ONE if i == j else ZERO) - 2 * w[i] * w[j] / ww
          for j in range(NS * NS)] for i in range(NS * NS)]
    return psi, H


def completion_from(H, q):
    """V = H . Q, column j of V being column Q(j) of H -- the declared
    construction, applied to any H and any permutation q."""
    return [[H[i][q[j]] for j in range(NS * NS)] for i in range(NS * NS)]


def defect_of_completion(V):
    """D = P_W U_prep^-1 P_W U_prep, computed DIRECTLY at 81x81 from the
    completion V -- the same four-factor product the P3 measurement uses,
    with U_prep rebuilt from V."""
    U = {}
    for a in range(NS * NS):
        for b in range(NS * NS):
            v = V[a][b]
            if not v:
                continue
            for pa in range(NP):
                for pb in range(NP):
                    U[(idx(a // NS, a % NS, pa, pb),
                       idx(b // NS, b % NS, pa, pb))] = v
    PW = pmat(WSWAP)
    return mm(PW, mm(minv(U), mm(PW, U)))


def tensor_with_pointer_identity(M9):
    """M (x) I_9: the 9x9 system-pair matrix acting on the 81 configurations
    and trivially on the pointer pair, in the model's own index map."""
    out = {}
    for (a, b), v in M9.items():
        for p in range(NS * NS):
            out[(a * NS * NS + p, b * NS * NS + p)] = v
    return out


def m9(A, B):
    out = {}
    for (i, k), u in A.items():
        for j in range(NS * NS):
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
    return {(i, j): V[i][j] for i in range(NS * NS)
            for j in range(NS * NS) if V[i][j]}


def run_defect_law():
    """THE DEFECT LAW, derived and gated two ways, with psi-independence
    measured over a declared family of preparation vectors."""
    prog("the defect law and its psi-independence")
    s9 = {(SIGMA9[i], i): ONE for i in range(NS * NS)}
    q = tuple(Q_COMPLETION)
    QP = {(q[j], j): ONE for j in range(NS * NS)}
    QPt = {(j, q[j]): ONE for j in range(NS * NS)}
    cancellation = tensor_with_pointer_identity(
        m9(s9, m9(QPt, m9(s9, QP))))
    rows, law_ok, cancel_ok, same_D, control_differs = {}, True, True, True, 0
    D_declared = None
    for nm, coeffs, invariant in PSI_FAMILY:
        psi, H = householder_of(coeffs)
        norm = sum(v * v for v in psi)
        sym = all(psi[i] == psi[SIGMA9[i]] for i in range(NS * NS))
        V = completion_from(H, q)
        Dd = defect_of_completion(V)
        Vd = dense9(V)
        law = tensor_with_pointer_identity(
            m9(s9, m9({(j, i): v for (i, j), v in Vd.items()},
                      m9(s9, Vd))))
        if D_declared is None:
            D_declared = Dd
        p, _sg = signed_perm(Dd)
        t = None if p is None else tuple(p[j] for j in range(NC))
        rows[nm] = {
            "the_vector_is_of_unit_norm": str(norm) == str(ONE),
            "the_vector_is_exchange_invariant": sym,
            "declared_as_exchange_invariant": invariant,
            "the_law_D_equals_sigma_Vt_sigma_V_tensor_I": Dd == law,
            "the_cancellation_D_equals_sigma_Qt_sigma_Q_tensor_I":
                Dd == cancellation,
            "the_defect_equals_the_declared_completions_defect":
                Dd == D_declared,
            "fixed_configurations": None if t is None else fixed_points(t)}
        if Dd != law:
            law_ok = False
        if sym != invariant:
            law_ok = False
        if invariant:
            if Dd != cancellation:
                cancel_ok = False
            if Dd != D_declared:
                same_D = False
        else:
            if Dd != cancellation and Dd != D_declared:
                control_differs += 1
    delta = defect_permutation_of(q)
    predicted_fixed = 9 * sum(1 for i in range(NS * NS) if delta[i] == i)
    Dp, _s = signed_perm(cancellation)
    measured_fixed = (None if Dp is None
                      else fixed_points([Dp[j] for j in range(NC)]))
    TABLES["defect_law"] = {
        "the_law": "D = (sigma V^T sigma V) (x) I_9, for any completion V",
        "the_cancellation":
            "D = (sigma Q^T sigma Q) (x) I_9 when V = H . Q and psi is "
            "exchange-invariant: the Householder cancels identically and "
            "psi does not appear",
        "per_declared_preparation_vector": rows,
        "the_defect_permutation_at_the_9x9_level": list(delta),
        "its_fixed_points_at_the_9x9_level":
            sum(1 for i in range(NS * NS) if delta[i] == i),
        "fixed_configurations_predicted_by_the_9x9_form": predicted_fixed,
        "fixed_configurations_measured_at_81x81": measured_fixed,
        "the_negative_controls_defect_differs": control_differs}
    gate("GEN-DEFECT-LAW", "measurement",
         "THE DEFECT OBEYS AN EXACT LAW, AND THE LAW SAYS THE DEFECT IS NOT "
         "THE PREPARATION'S.  With U_prep = V (x) I_9 and the wing exchange "
         "P_W = sigma (x) sigma, the four-factor product collapses: D = "
         "(sigma V^T sigma V) (x) I_9, measured exactly against the direct "
         "81x81 computation for every completion of a declared family of "
         "preparation vectors.  When V = H . Q with H the Householder of an "
         "exchange-INVARIANT psi, H is exchange-equivariant and involutive, "
         "so it CANCELS IDENTICALLY and D = (sigma Q^T sigma Q) (x) I_9 -- "
         "in which psi does not appear at all.  Four declared "
         "exchange-invariant preparation vectors, all different, are "
         "measured to give the SAME defect, entry by entry, as the declared "
         "one; a fifth, declared NOT exchange-invariant, is the negative "
         "control and is measured to give a DIFFERENT defect, so the "
         "invariance hypothesis is measured load-bearing rather than "
         "decorative.  The 9x9 form's fixed-point count times the nine "
         "untouched pointer pairs is measured equal to the 81-configuration "
         "count.  The `defect-order` mutant composes the product in the "
         "wrong order, the `anchor-completion` mutant perturbs the "
         "constructed completion, and the `completion-Q` mutant replaces it "
         "by the bare Householder; each moves one side of a comparison and "
         "must die here",
         law_ok and cancel_ok and same_D and control_differs > 0
         and predicted_fixed == measured_fixed
         and defect_of_completion(VCOMP) == cancellation,
         {"per_declared_preparation_vector": rows,
          "the_law_holds_for_every_declared_vector": law_ok,
          "the_cancellation_holds_for_every_invariant_vector": cancel_ok,
          "every_invariant_vector_gives_the_same_defect": same_D,
          "the_negative_controls_defect_differs": control_differs,
          "fixed_configurations_predicted_by_the_9x9_form": predicted_fixed,
          "fixed_configurations_measured_at_81x81": measured_fixed,
          "the_defect_of_the_completion_in_force_is_the_cancellation_form":
              defect_of_completion(VCOMP) == cancellation})
    return cancellation, delta


def run_completion_census():
    """THE EXHAUSTIVE CENSUS of the declared completion family: all 8! =
    40,320 permutations Q of the nine system-pair indices fixing the first,
    every one of which has psi as its first column.  The census runs at the
    9x9 level through the law gated above, so it is exhaustive and cheap."""
    prog("the completion census: the exhaustive 8! family sweep")
    s = tuple(SIGMA9)
    # Which elements of the declared scopes act on the system pair alone,
    # i.e. are of the form delta (x) I_9?  Computed by scanning the scopes,
    # never assumed: those are the only ones a defect could belong to.
    def tensor_part(p):
        d = [None] * (NS * NS)
        for a in range(NS * NS):
            for pp in range(NS * NS):
                j = p[a * NS * NS + pp]
                if j % (NS * NS) != pp:
                    return None
                b = j // (NS * NS)
                if d[a] is None:
                    d[a] = b
                elif d[a] != b:
                    return None
        return tuple(d)
    scope9 = {t for t in (tensor_part(p) for p in SCOPE["base"])
              if t is not None}
    ext9 = {t for t in (tensor_part(p) for p in SCOPE["extension_all"])
            if t is not None}
    by_order, by_fixed, by_class, equivariant = {}, {}, {}, 0
    equivariance_mismatches, dihedral_failures = 0, 0
    escapes, inside = 0, 0
    total = 0
    first_of_order = {}
    declared_seen, declared_entry = False, None
    for tail in itertools.permutations(range(1, NS * NS)):
        qq = (0,) + tail
        d = defect_permutation_of(qq)
        n = perm9_order(d)
        f = sum(1 for i in range(NS * NS) if d[i] == i)
        total += 1
        by_order[n] = by_order.get(n, 0) + 1
        by_fixed[9 * f] = by_fixed.get(9 * f, 0) + 1
        commutes = (perm9_compose(s, qq) == perm9_compose(qq, s))
        if n == 1:
            equivariant += 1
        if (n == 1) != commutes:
            equivariance_mismatches += 1
        if perm9_compose(perm9_compose(s, d), s) != perm9_inverse(d):
            dihedral_failures += 1
        if n > 1:
            if d in scope9 or d in ext9:
                inside += 1
            else:
                escapes += 1
        cls = "ord=%d,fixed=%d" % (n, 9 * f)
        by_class[cls] = by_class.get(cls, 0) + 1
        if cls not in first_of_order:
            first_of_order[cls] = qq
        if qq == tuple(Q_COMPLETION):
            declared_seen = True
            declared_entry = {"order": n, "fixed_configurations": 9 * f,
                              "the_defect_permutation": list(d)}
    spectrum = sorted({(2 * n if n > 1 else 1) for n in by_order})
    census = {
        "the_declared_family":
            "V = H . Q with Q a permutation of the nine system-pair indices "
            "fixing the first, so that V's first column is psi for every "
            "member",
        "family_size": total,
        "swept": "EXHAUSTIVE (every member)",
        "members_by_the_order_of_the_defect":
            {str(k): v for k, v in sorted(by_order.items())},
        "members_by_the_fixed_configurations_of_the_defect":
            {str(k): v for k, v in sorted(by_fixed.items())},
        "geometry_bearing_members": total - equivariant,
        "members_whose_defect_is_the_identity": equivariant,
        "members_where_a_trivial_defect_and_an_equivariant_Q_disagree":
            equivariance_mismatches,
        "the_exceptions_are_exactly_the_exchange_equivariant_locus":
            equivariance_mismatches == 0,
        "members_where_the_dihedral_relation_fails": dihedral_failures,
        "the_dihedral_relation_holds_at_every_member":
            dihedral_failures == 0,
        "the_predicted_holonomy_group_order_spectrum": spectrum,
        "geometry_bearing_members_whose_defect_escapes_every_declared_"
        "collection": escapes,
        "geometry_bearing_members_whose_defect_lies_inside_a_declared_"
        "collection": inside,
        "scope_elements_that_act_on_the_system_pair_alone": len(scope9),
        "extension_elements_that_act_on_the_system_pair_alone": len(ext9),
        "the_declared_completion_is_a_member": declared_seen,
        "the_declared_completions_entry":
            declared_entry if declared_seen else None,
        "the_measured_classes_of_the_family":
            "one per (order of the defect, fixed configurations of the "
            "defect); every class's lexicographically first member is "
            "rebuilt in full below",
        "class_sizes": {k: by_class[k] for k in sorted(by_class)},
        "the_lexicographically_first_member_of_each_class":
            {k: list(v) for k, v in sorted(first_of_order.items())}}
    TABLES["completion_census"] = census
    anchor("A14", "the frozen review panel's contributed census",
           "the number of completions of the declared family whose defect "
           "is the identity, and the number that bear geometry",
           [96, 40224], [equivariant, total - equivariant])
    anchor("A15", "the frozen review panel's contributed census",
           "the distribution of the defect's fixed configurations over the "
           "declared family",
           {"9": 16704, "18": 11520, "27": 5376, "36": 4608, "45": 864,
            "54": 1152, "81": 96},
           {str(k): v for k, v in sorted(by_fixed.items())})
    gate("GEN-COMPLETION-CENSUS", "measurement",
         "THE COMPLETION FAMILY, SWEPT EXHAUSTIVELY.  The declared "
         "completion is one member of a family the law above reduces to "
         "9x9: V = H . Q with Q any permutation of the nine system-pair "
         "indices fixing the first, so that every member has psi as its "
         "first column.  The family's size is COMPUTED by enumeration, and "
         "EVERY member is swept.  The gate measures five things that can "
         "fail.  (1) The defect is the identity on exactly the members "
         "whose Q COMMUTES with the system exchange -- the "
         "exchange-EQUIVARIANT locus -- measured member by member, in both "
         "directions.  (2) Geometry is therefore GENERIC in the family and "
         "the equivariant locus is the exception, with both counts "
         "computed.  (3) The dihedral relation sigma D sigma = D^-1 holds "
         "at EVERY member, which is what makes the family dihedral: <W, D | "
         "W^2 = D^n = 1, W D W = D^-1> with n the defect's order.  (4) The "
         "defect of every geometry-bearing member lies OUTSIDE every "
         "declared collection -- computed against the elements of the "
         "declared scope and its extension that act on the system pair "
         "alone, which are found by scanning the scopes and not assumed.  "
         "(5) The pinned completion is measured to BE a member of the "
         "family and its census entry -- the order of its defect and its "
         "fixed-configuration count -- is measured to agree with the defect "
         "measured on the base itself, so the census is tied to the base in "
         "force and the `defect-order`, `anchor-completion` and "
         "`completion-Q` mutants die here.  The isomorphism type of the "
         "holonomy group is therefore COMPLETION-SELECTED, and every claim "
         "about the type in this unit carries that scope tag",
         census["the_declared_completion_is_a_member"]
         and equivariance_mismatches == 0 and dihedral_failures == 0
         and escapes > 0 and inside == 0
         and equivariant > 0 and total - equivariant > equivariant
         and declared_entry["fixed_configurations"]
         == TABLES["mechanism"]["the_completions_non_equivariance_defect"]
                  ["fixed_points"]
         and declared_entry["order"]
         == TABLES["mechanism"]["the_completions_non_equivariance_defect"]
                  ["order"],
         census)
    return census, first_of_order


def run_completion_rebuilds(first_of_order, hg):
    """FULL REBUILDS on declared sub-families: the 28 members of the pinned
    completion's own declared form (a single basis transposition), and the
    lexicographically first member of every measured class, one class per
    (order of the defect, fixed configurations of the defect).  Each is
    rebuilt at the symmetric setting GP-E and at GP-A as the flat control --
    the declared scope of the rebuild, printed."""
    prog("the completion census: full rebuilds (the declared form, "
         "then one per class)")
    sym = [sp for sp in SETTING_ORDER if SETTINGS[sp][0] == SETTINGS[sp][1]]
    flat = [sp for sp in SETTING_ORDER if SETTINGS[sp][0] != SETTINGS[sp][1]]
    sps = [flat[0], sym[0]]
    H = householder()
    rows, split, mismatches = {}, {}, []
    bound_reached = []
    for i in range(1, NS * NS):
        for j in range(i + 1, NS * NS):
            qq = list(range(NS * NS))
            qq[i], qq[j] = qq[j], qq[i]
            qq = tuple(qq)
            d = defect_permutation_of(qq)
            n = perm9_order(d)
            r = with_completion(completion_from(H, qq),
                                settings=sps,
                                bound=CLOSURE_BOUND)
            got = r["holonomy_group_order_per_setting"][sym[0]]
            want = 2 * n if n > 1 else 1
            ab = r["holonomy_group_is_abelian_per_setting"][sym[0]]
            nm = ("trivial" if got == 1
                  else ("the Klein four-group" if got == 4 and ab
                        else ("a non-abelian group of order %d" % got
                              if not ab else "an abelian group of order %d"
                              % got)))
            split[nm] = split.get(nm, 0) + 1
            rows["Q = (%d %d)" % (i, j)] = {
                "the_order_of_the_defect": n,
                "the_dihedral_prediction_for_the_group_order": want,
                "the_measured_group_order_at_the_symmetric_setting": got,
                "the_measured_group_order_at_the_flat_control":
                    r["holonomy_group_order_per_setting"][flat[0]],
                "abelian": ab,
                "the_structure": nm,
                "identification_links_at_the_symmetric_setting":
                    r["identification_links_per_setting"][sym[0]]}
            if got != want or r["holonomy_group_order_per_setting"][
                    flat[0]] != 1:
                mismatches.append("Q = (%d %d)" % (i, j))
            if r["the_declared_closure_bound_was_reached"]:
                bound_reached.append("Q = (%d %d)" % (i, j))
    spot = {}
    for cls in sorted(first_of_order,
                      key=lambda k: (int(k.split(",")[0].split("=")[1]),
                                     int(k.split(",")[1].split("=")[1]))):
        qq = tuple(first_of_order[cls])
        n = perm9_order(defect_permutation_of(qq))
        r = with_completion(completion_from(H, qq), settings=sps,
                            bound=CLOSURE_BOUND)
        got = r["holonomy_group_order_per_setting"][sym[0]]
        want = 2 * n if n > 1 else 1
        spot[cls] = {
            "Q": list(qq),
            "the_order_of_the_defect": n,
            "the_dihedral_prediction_for_the_group_order": want,
            "the_measured_group_order_at_the_symmetric_setting": got,
            "the_measured_group_order_at_the_flat_control":
                r["holonomy_group_order_per_setting"][flat[0]],
            "abelian": r["holonomy_group_is_abelian_per_setting"][sym[0]],
            "element_orders":
                r["holonomy_element_orders_per_setting"][sym[0]],
            "value_set_size": r["value_set_size_per_setting"][sym[0]],
            "the_value_set_is_closed_at_the_declared_bound":
                r["the_value_set_is_closed_at_the_bound_per_setting"][
                    sym[0]],
            "the_defects_fixed_configurations":
                r["the_completions_non_equivariance_defect"]["fixed_points"]}
        if got != want:
            mismatches.append(cls)
        if r["the_declared_closure_bound_was_reached"]:
            bound_reached.append(cls)
    declared_row = rows.get("Q = (%d %d)"
                            % (min(x for x in range(NS * NS)
                                   if Q_COMPLETION[x] != x),
                               max(x for x in range(NS * NS)
                                   if Q_COMPLETION[x] != x)))
    TABLES["completion_rebuilds"] = {
        "the_rebuild_scope":
            "each member is rebuilt in full at %s (symmetric) and at %s "
            "(the flat control); the other four settings are not rebuilt "
            "in this sweep; each rebuilt group is closed under a declared "
            "bound of %d elements, and the sweep gates that the bound is "
            "never reached" % (sym[0], flat[0], CLOSURE_BOUND),
        "the_declared_closure_bound": CLOSURE_BOUND,
        "members_where_the_declared_closure_bound_was_reached":
            bound_reached,
        "the_declared_form_sub_family":
            "every Q that is a single transposition of the nine "
            "system-pair indices fixing the first -- the pinned "
            "completion's own declared form",
        "sub_family_size": len(rows),
        "per_member": rows,
        "the_split_of_the_declared_form_sub_family": split,
        "one_full_rebuild_per_measured_class": spot,
        "the_class_rule":
            "one class per (order of the defect, fixed configurations of "
            "the defect); the lexicographically first member of each is "
            "rebuilt",
        "members_where_the_measured_group_order_differs_from_the_dihedral_"
        "prediction": mismatches,
        "the_declared_completions_own_row": declared_row}
    anchor("A16", "the frozen review panel's contributed census",
           "the split of the 28-member declared-form sub-family into flat, "
           "Klein-four and non-abelian order-6 members",
           [4, 12, 12],
           [split.get("trivial", 0), split.get("the Klein four-group", 0),
            split.get("a non-abelian group of order 6", 0)])
    gate("GEN-COMPLETION-FAMILY-REBUILT", "measurement",
         "THE FAMILY IS NOT ONLY COUNTED, IT IS REBUILT.  Two declared "
         "sub-families are rebuilt IN FULL -- new completion, new admission "
         "table, new graph, new path enumeration, new based holonomy -- at "
         "the symmetric setting and at an asymmetric one as the flat "
         "control.  (a) EVERY member of the pinned completion's own "
         "declared form, a single transposition of the nine system-pair "
         "indices: the sub-family's size is computed, and it splits into "
         "flat members, members whose group is the Klein four-group, and "
         "members whose group is NON-ABELIAN of order six -- so the "
         "isomorphism type is selected inside the pinned completion's own "
         "form, not only across the wider family.  (b) The "
         "lexicographically first member of EVERY class measured by "
         "the census, so the whole predicted spectrum is exhibited by "
         "rebuild and not by extrapolation.  The gate measures that the "
         "MEASURED based holonomy group order equals the DIHEDRAL "
         "PREDICTION 2n at every rebuilt member with a nontrivial defect, "
         "that it is trivial at the equivariant ones, that the flat control "
         "setting is measured flat at every member, and that the pinned "
         "completion's own rebuilt row reproduces the group order measured "
         "on the base itself by the main enumeration.  A mutant that "
         "perturbs the admission rule, the scopes, the path space or the "
         "holonomy reading moves the rebuilds and must die here",
         not mismatches and not bound_reached
         and len(rows) > 0 and len(spot) > 0
         and declared_row is not None
         and declared_row["the_measured_group_order_at_the_symmetric_"
                          "setting"] == hg[sym[0]]["generated_group_order"],
         {"sub_family_size": len(rows),
          "the_split_of_the_declared_form_sub_family": split,
          "classes_rebuilt": sorted(spot),
          "members_where_the_measured_group_order_differs_from_the_"
          "dihedral_prediction": mismatches,
          "members_where_the_declared_closure_bound_was_reached":
              bound_reached,
          "the_declared_completions_own_row": declared_row,
          "the_group_order_measured_on_the_base_itself":
              hg[sym[0]]["generated_group_order"],
          "the_rebuild_scope": TABLES["completion_rebuilds"][
              "the_rebuild_scope"]})
    return rows, spot


def run_connection_enumeration(graphs, values, hg):
    """HOW MUCH OF THE CROSS-BASE AGREEMENT THE GRAPH AND THE GROUP EXPLAIN.

    The holonomy of a based closed walk is fixed by the images of the
    graph's independent cycles in the group.  This gauge-fixes the
    connection on a spanning tree, measures that the model so obtained
    reproduces the directly computed holonomy walk by walk, and then
    enumerates EVERY assignment of the group's elements to the independent
    cycles -- the complete space of connections on this graph with this
    group -- and counts how many reproduce the measured class counts.

    The setting is fixed BY DECLARATION -- the first symmetric member of
    the declared family -- and never selected by the verdicts under audit
    (RUNBOOK section 14 addendum)."""
    sp = [s for s in SETTING_ORDER if SETTINGS[s][0] == SETTINGS[s][1]][0]
    prog("the connection enumeration on the gauge-fixed graph (%s)" % sp)
    G = graphs[sp]
    base = ("F1", CHECKPOINTS[0])
    # a spanning tree, by breadth-first search from the base node over the
    # links in their own index order: a declared rule, not a choice
    T = {base: sp_id()}
    tree, frontier = set(), [base]
    while frontier:
        nxt = []
        for node in frontier:
            for (li, d, other) in sorted(G["adj"][node], key=lambda x: x[0]):
                if other in T:
                    continue
                tree.add(li)
                T[other] = mm(link_variable(sp, G["links"][li], d), T[node])
                nxt.append(other)
        frontier = nxt
    cotree = [li for li in range(G["n_links"]) if li not in tree]
    grp = {tuple(z) for z in hg[sp]["_group"]}
    labels, outside_group, unreadable = {}, 0, 0
    nodes_reached = len(T)
    for li in range(G["n_links"]):
        L = G["links"][li]
        if L["a"] not in T or L["b"] not in T:
            # the spanning tree did not reach this link's endpoints: the
            # graph is not connected, so there is no gauge-fixing to do and
            # the label is reported unreadable rather than invented
            labels[li] = None
            unreadable += 1
            continue
        g = mm(minv(T[L["b"]]), mm(link_variable(sp, L, +1), T[L["a"]]))
        p, _s = signed_perm(g)
        if p is None:
            labels[li] = None
            unreadable += 1
            continue
        t = tuple(p[j] for j in range(NC))
        labels[li] = t
        if t not in grp:
            outside_group += 1
    # the model, measured walk by walk against the direct computation
    walks = [r for r in values[sp]
             if r["start"] == base and r["end"] == base and r["len"]]
    disagreements, checked, parvec = 0, 0, {}
    measured_counts = {}
    for r in walks:
        acc = tuple(range(NC))
        ok = True
        for (li, d) in r["edges"]:
            t = labels[li]
            if t is None:
                ok = False
                break
            acc = perm_compose(t if d > 0 else tuple(perm_inverse(list(t))),
                               acc)
        direct = holonomy_class_of_interned(r["A"])[0]
        checked += 1
        if not ok or direct is None or acc != direct:
            disagreements += 1
        if direct is not None:
            measured_counts[direct] = measured_counts.get(direct, 0) + 1
        par = tuple(sum(1 for (li, _d) in r["edges"] if li == c) % 2
                    for c in cotree)
        parvec[par] = parvec.get(par, 0) + 1
    measured_profile = tuple(sorted(measured_counts.values()))
    # the complete space of connections on this graph with this group
    els = sorted(grp)
    ident = tuple(range(NC))
    profiles, hits, surjective, surjective_hits = {}, 0, 0, 0
    space = len(els) ** len(cotree)
    swept = space <= ENUMERATION_CAP
    for assign in (itertools.product(range(len(els)), repeat=len(cotree))
                   if swept else ()):
        counts = {}
        for par, n in parvec.items():
            acc = ident
            for k, c in enumerate(assign):
                if par[k]:
                    acc = perm_compose(els[c], acc)
            counts[acc] = counts.get(acc, 0) + n
        prof = tuple(sorted(counts.values()))
        profiles[prof] = profiles.get(prof, 0) + 1
        gen = {ident} | {els[c] for c in assign}
        changed = True
        while changed:
            changed = False
            for x in list(gen):
                for y in list(gen):
                    z = perm_compose(x, y)
                    if z not in gen:
                        gen.add(z)
                        changed = True
        onto = (len(gen) == len(grp))
        surjective += 1 if onto else 0
        if prof == measured_profile:
            hits += 1
            surjective_hits += 1 if onto else 0
    TABLES["connection_enumeration"] = {
        "setting": sp,
        "spanning_tree_links": sorted(tree),
        "nodes_reached_by_the_spanning_tree": nodes_reached,
        "nodes_declared": len(NODES),
        "independent_cycles": len(cotree),
        "links_whose_gauge_fixed_label_is_unreadable": unreadable,
        "links_whose_gauge_fixed_label_lies_outside_the_group":
            outside_group,
        "based_closed_walks_checked": checked,
        "walks_where_the_cycle_model_disagrees_with_the_direct_holonomy":
            disagreements,
        "the_measured_class_counts": list(measured_profile),
        "the_group_the_connection_takes_values_in": len(els),
        "the_size_of_the_connection_space": space,
        "the_connection_space_was_swept_exhaustively": swept,
        "the_declared_enumeration_cap": ENUMERATION_CAP,
        "connections_enumerated": space if swept else 0,
        "distinct_class_count_profiles": len(profiles),
        "connections_reproducing_the_measured_profile": hits,
        "connections_whose_labels_generate_the_whole_group": surjective,
        "of_those_reproducing_the_measured_profile": surjective_hits,
        "the_most_common_profile":
            ([list(max(profiles.items(), key=lambda kv: kv[1])[0]),
              max(profiles.values())] if profiles else None)}
    gate("GEN-CONNECTION-CLASS-COUNTS", "measurement",
         "WHAT THE SHARED GRAPH AND THE SHARED GROUP DO NOT EXPLAIN.  The "
         "class counts of the based closed walks are not a function of the "
         "graph and the group alone, and this gate measures how far from it "
         "they are.  First the connection is GAUGE-FIXED: a spanning tree "
         "is grown from the base node by breadth-first search over the "
         "links in their own index order, every link is relabelled by "
         "conjugation with the tree transports, and the resulting labels "
         "are measured to be signed permutations lying IN the measured "
         "holonomy group -- so the connection really is a group-valued "
         "connection on this graph.  Then the model is measured: the "
         "holonomy of every based closed walk is measured equal, "
         "permutation tuple by permutation tuple, to the ordered product of "
         "those labels along the walk -- at every walk, which is what makes "
         "the model a measurement and not an assumption.  Finally EVERY "
         "assignment of the group's elements to the independent cycles is "
         "enumerated -- the complete connection space, its size computed -- "
         "and the number reproducing the measured class counts is counted.  "
         "It is a small fraction, and it is printed: an isomorphic graph "
         "and an isomorphic group therefore do NOT determine these counts, "
         "so an agreement of class counts across two bases records "
         "something the graph and the group do not, and this unit registers "
         "that as an open question rather than explaining it away.  The "
         "`path-collapse` mutant makes the holonomies unreadable and must "
         "die at the model clause",
         unreadable == 0 and outside_group == 0 and disagreements == 0
         and checked > 0 and swept and hits > 0 and hits < space
         and len(els) > 1 and nodes_reached == len(NODES),
         TABLES["connection_enumeration"])
    return TABLES["connection_enumeration"]


def run_family_probe():
    """THE MEASUREMENT FAMILY, FLIPPED.  The declared six-setting family is
    a free declaration; this measures whether the holonomy at a symmetric
    setting depends on WHICH rotation the two wings share, by adding two
    further symmetric settings -- one on a declared rotation the family
    already contains, one on a FRESH integer quaternion -- and re-measuring.
    Folded into no verdict."""
    global SETTINGS, SETTING_ORDER, ROT, _FIXTURE, _INTERN, _INTERN_VALUE
    global _HOL_CLASS
    prog("the measurement-family probe (two further symmetric settings)")
    keepS, keepO, keepR = dict(SETTINGS), list(SETTING_ORDER), dict(ROT)
    keepF, keepI = _FIXTURE, _INTERN
    keepIV, keepH = _INTERN_VALUE, _HOL_CLASS
    QUATERNIONS["R3"] = (4, 1, 2, 0)
    try:
        ROT = dict(ROT)
        ROT["R3"] = rotation("R3")
        r3_orth = all(sum((ROT["R3"][i][a] * ROT["R3"][i][b]
                           for i in range(NS)), ZERO)
                      == (ONE if a == b else ZERO)
                      for a in range(NS) for b in range(NS))
        SETTINGS = dict(SETTINGS)
        SETTINGS["GP-G"] = ("R2", "R2")
        SETTINGS["GP-H"] = ("R3", "R3")
        SETTING_ORDER = list(SETTING_ORDER) + ["GP-G", "GP-H"]
        _FIXTURE, _INTERN, _INTERN_VALUE, _HOL_CLASS = {}, {}, {}, {}
        pref = prefix_profile()
        rows = {}
        for sp in ("GP-E", "GP-G", "GP-H"):
            G = build_graph(sp, pref)
            vals = enumerate_paths(sp, G, L_MAX)
            h = based_holonomy(sp, {sp: vals})
            base = ("F1", CHECKPOINTS[0])
            counts = {}
            for r in vals:
                if r["start"] == base and r["end"] == base and r["len"]:
                    t = holonomy_class_of_interned(r["A"])[0]
                    if t is not None:
                        counts[t] = counts.get(t, 0) + 1
            rows[sp] = {"wings": list(SETTINGS[sp]),
                        "identification_links":
                            sum(1 for L in G["links"] if L["kind"] == "id"),
                        "generated_group_order": h["generated_group_order"],
                        "abelian": h["the_group_is_abelian"],
                        "element_orders": h["element_orders"],
                        "class_counts_at_the_base_point":
                            sorted(counts.values()),
                        "closed_paths_at_the_base_point":
                            h["closed_paths_based_there"]}
    finally:
        SETTINGS, SETTING_ORDER, ROT = keepS, keepO, keepR
        QUATERNIONS.pop("R3", None)
        _FIXTURE, _INTERN = keepF, keepI
        _INTERN_VALUE, _HOL_CLASS = keepIV, keepH
    same = (len({r["generated_group_order"] for r in rows.values()}) == 1
            and len({tuple(r["class_counts_at_the_base_point"])
                     for r in rows.values()}) == 1)
    TABLES["family_probe"] = {
        "the_added_settings":
            "GP-G shares the declared rotation R2 on both wings; GP-H "
            "shares a rotation built from the FRESH integer quaternion "
            "(4, 1, 2, 0), which is not in the declared family at all",
        "the_fresh_rotation_is_exactly_orthogonal": r3_orth,
        "per_setting": rows,
        "the_group_and_the_class_counts_are_the_same_at_every_symmetric_"
        "setting": same}
    gate("GEN-FAMILY-PROBE", "disclosure",
         "WHAT THE MEASUREMENT FAMILY DECIDES, MEASURED.  The six-setting "
         "family is a free declaration, so this disclosure measures what "
         "depends on it.  Two FURTHER symmetric settings are built and the "
         "base is re-enumerated on them: one sharing a rotation the "
         "declared family already contains, one sharing a rotation built "
         "from a fresh integer quaternion that is not in the declared "
         "family at all and is measured exactly orthogonal.  At all three "
         "symmetric settings the based holonomy group and the class counts "
         "are measured IDENTICAL.  So the measurement family is measured "
         "INERT for the geometry: the holonomy at a symmetric setting does "
         "not depend on which rotation the two wings share.  The "
         "measurement is folded into no verdict; it is what entitles this "
         "unit to say which of its declared coordinates do work",
         True, TABLES["family_probe"])
    return TABLES["family_probe"]


def run_scope_disclosure(pref):
    """The declared extension scope, searched but folded into no verdict."""
    prog("the declared scopes: the narrow one used, the extension searched")
    cells, links_ext, canon_exists, lost = {}, {}, {}, []
    for sp in SETTING_ORDER:
        n_ext = 0
        for rule in ID_RULES:
            for t in CHECKPOINTS:
                a = len(admits(sp, t, rule))
                b = len(admits(sp, t, rule, scope="admitted_extension"))
                if a != b:
                    cells["%s/%s/t%d" % (sp, rule["id"], t)] = {
                        "admitted_at_the_declared_scope": a,
                        "admitted_at_the_declared_extension": b}
                if b == 1:
                    n_ext += 1
        links_ext[sp] = n_ext
        has_top = any(len(admits(sp, CHECKPOINTS[-1], r,
                                 scope="admitted_extension")) == 1
                      for r in ID_RULES if r["id"] == "FULL")
        has_bot = any(len(admits(sp, CHECKPOINTS[0], r,
                                 scope="admitted_extension")) == 1
                      for r in ID_RULES if r["id"] == "FULL")
        canon_exists[sp] = bool(has_top and has_bot)
        if not canon_exists[sp]:
            lost.append(sp)
    TABLES["admission_scope"] = {
        "cells_where_the_scope_changes_admission": cells,
        "identification_links_at_the_declared_extension": links_ext,
        "the_canonical_loop_exists_at_the_declared_extension": canon_exists,
        "settings_where_the_canonical_loop_would_not_exist": lost}
    gate("GEN-ADMISSION-SCOPE", "disclosure",
         "THE ADMISSION SCOPE IS A CHOICE, AND WHAT DEPENDS ON IT IS "
         "MEASURED.  Every admission search that feeds a link, a profile or "
         "a verdict in this unit runs over the elements of the declared "
         "relabelling scope that survive the j0 filter; every negative in "
         "this unit is a negative at THAT scope.  The declared EXTENSION is "
         "searched here with the same four-clause predicate over the wider "
         "set, and the cells where the two disagree are printed.  Because "
         "admission is by UNIQUENESS, a wider scope can REFUSE a link the "
         "narrower one draws, so the settings at which the canonical loop "
         "would cease to exist are named.  The measurement is folded into "
         "no verdict",
         True,
         {"cells_where_the_scope_changes_admission": cells,
          "identification_links_at_the_declared_extension": links_ext,
          "the_canonical_loop_exists_at_the_declared_extension":
              canon_exists,
          "settings_where_the_canonical_loop_would_not_exist": lost})


def run_comparison(hg, D, subs, esc, nontrivial, struct, ps):
    """THE COMPARISON WITH THE FIRST BASE, anchored against its committed
    terminal receipt.  Nothing of the first base's model is imported: only
    numbers from its receipt are read, and they are anchored exit-1."""
    prog("the comparison with the first base (anchored to the NT receipt)")
    nt = _nt()
    ntg = nt["findings"]["holonomy_group"]["per_setting"]["SP-E"]
    nts = nt["tables"]["structure_group"]
    ntp = nt["tables"]["path_space"]
    ntsub = nt["tables"]["mechanism"]["single_rule_subconnections"]
    perturb_a_reused_first_base_value = (MUTANT == "anchor-nt")
    got_order = ntg["generated_group_order"]
    if perturb_a_reused_first_base_value:
        got_order = got_order + 1
    anchor("A08", "the committed NT terminal receipt",
           "the first base's based holonomy group order at its symmetric "
           "setting", 4, got_order)
    anchor("A09", "the committed NT terminal receipt",
           "the first base's holonomy value-set size and its closure",
           [4, True],
           [ntg["value_set_size"],
            ntg["the_value_set_is_closed_under_composition"]])
    anchor("A10", "the committed NT terminal receipt",
           "the first base's elements lying outside every declared scope, "
           "at its two symmetric settings",
           [2, 2],
           [nts["elements_outside_every_declared_scope"]["SP-E"],
            nts["elements_outside_every_declared_scope"]["SP-F"]])
    anchor("A11", "the committed NT terminal receipt",
           "the first base's total reduced paths and path pairs",
           [34024, 4972096],
           [ntp["_total_paths"], ntp["_total_pairs"]])
    anchor("A12", "the committed NT terminal receipt",
           "the first base's realized-rule sub-connection at SP-E: closed "
           "paths at the base point, and its generated group order",
           [18, 2],
           [ntsub["SP-E/REAL"]["closed_paths_at_F1_t0"],
            ntsub["SP-E/REAL"]["generated_group_order"]])

    sym = sorted(nontrivial)
    # The first base's own DECLARED arena, read from its receipt rather than
    # typed here, and anchored (A17).
    nta = nt["tables"]["declarations"]["arena"]
    anchor("A17", "the committed NT terminal receipt",
           "the first base's declared arena: carrier, settings, declared "
           "relabelling scope, admitted set and admitted extension",
           [36, 6, 72, 2, 8],
           [nta["carrier"], nta["settings"], nta["declared_permutation_"
                                                 "scope"],
            nta["admitted_permutation_group"], nta["admitted_extension"]])
    # The first base's group STRUCTURE is not typed either: it is named by
    # THIS unit's own naming rule, applied to the properties its receipt
    # reports (order, abelian, element orders squaring to the identity).
    nt_struct = ("the Klein four-group"
                 if (ntg["generated_group_order"] == 4
                     and ntg["the_group_is_abelian"]
                     and ntg["every_element_squares_to_the_identity"])
                 else "a group of order %d" % ntg["generated_group_order"])
    nt_defect = nt["tables"]["mechanism"]["the_prep_leg_defect_element"][
        "SP-E"]["name"]
    nt_halves = [k for k in nts["factor_fixed_points"]
                 if k != "the wing exchange"]
    rows = {
        "carrier": {"first base": nta["carrier"], "base G": NC,
                    "first base read from": "the NT receipt (A17)"},
        "system dimension per wing":
            {"first base": 2, "base G": NS,
             "first base read from": "DECLARED HERE: the NT receipt carries "
                                     "no such field"},
        "outcomes per measurement":
            {"first base": 2, "base G": NS,
             "first base read from": "DECLARED HERE: the NT receipt carries "
                                     "no such field"},
        "arithmetic": {"first base": "the quartic field Q(cos pi/8)",
                       "base G": "the rationals Q",
                       "first base read from":
                           "DECLARED HERE: the NT receipt carries no such "
                           "field"},
        "preparation vector under the wing exchange":
            {"first base": "ANTI-invariant (the singlet)",
             "base G": "invariant",
             "first base read from": "DECLARED HERE: the NT receipt carries "
                                     "no such field"},
        "preparation Schmidt rank":
            {"first base": 2,
             "base G": TABLES["base_declaration"]["psi_schmidt_rank"],
             "first base read from": "DECLARED HERE: the NT receipt carries "
                                     "no such field"},
        "settings": {"first base": nta["settings"],
                     "base G": len(SETTING_ORDER),
                     "first base read from": "the NT receipt (A17)"},
        "symmetric settings":
            {"first base": 2,
             "base G": len([s for s in SETTING_ORDER
                            if SETTINGS[s][0] == SETTINGS[s][1]]),
             "first base read from": "DECLARED HERE: the NT receipt carries "
                                     "no such field"},
        "declared relabelling scope":
            {"first base": nta["declared_permutation_scope"],
             "base G": SCOPE["n_base"],
             "first base read from": "the NT receipt (A17)"},
        "admitted after the j0 filter":
            {"first base": nta["admitted_permutation_group"],
             "base G": SCOPE["n_admitted"],
             "first base read from": "the NT receipt (A17)"},
        "admitted at the extension":
            {"first base": nta["admitted_extension"],
             "base G": SCOPE["n_admitted_extension"],
             "first base read from": "the NT receipt (A17)"},
        "total reduced paths": {"first base": ntp["_total_paths"],
                                "base G": ps["_total_paths"],
                                "first base read from":
                                    "the NT receipt (A11)"},
        "path pairs sharing both endpoints":
            {"first base": ntp["_total_pairs"], "base G": ps["_total_pairs"],
             "first base read from": "the NT receipt (A11)"},
        "holonomy group order at a symmetric setting":
            {"first base": ntg["generated_group_order"],
             "base G": hg[sym[0]]["generated_group_order"] if sym else 1,
             "first base read from": "the NT receipt (A08)"},
        "holonomy group structure":
            {"first base": nt_struct,
             "base G": struct[sym[0]] if sym else "trivial",
             "first base read from":
                 "the NT receipt, named by this unit's own naming rule "
                 "from the order, the element orders and abelianness it "
                 "reports"},
        "value set closed at the declared bound":
            {"first base": ntg["the_value_set_is_closed_under_composition"],
             "base G": (hg[sym[0]]["the_value_set_is_closed_under_"
                                   "composition"] if sym else None),
             "first base read from": "the NT receipt (A09)"},
        "elements outside every declared collection":
            {"first base": nts["elements_outside_every_declared_scope"]
                              ["SP-E"],
             "base G": (sum(1 for r in esc[sym[0]].values()
                            if not r["in_the_declared_relabelling_scope"]
                            and not r["in_the_declared_extension_scope"])
                        if sym else 0),
             "first base read from": "the NT receipt (A10)"},
        "the second generator of the holonomy group":
            {"first base": nt_defect, "base G": D["name"],
             "first base read from": "the NT receipt"},
        "the second generator is one half of the wing exchange":
            {"first base": nt_defect in nt_halves,
             "base G": bool(D["equals_the_system_only_exchange"]
                            or D["equals_the_pointer_only_exchange"]),
             "first base read from":
                 "the NT receipt: its defect's name against its own two "
                 "wing-exchange factors"},
        "realized-rule sub-connection: closed paths at the base point":
            {"first base": ntsub["SP-E/REAL"]["closed_paths_at_F1_t0"],
             "base G": (subs["%s/REAL" % sym[0]]
                        ["closed_paths_at_the_base_point"] if sym else 0),
             "first base read from": "the NT receipt (A12)"},
        "realized-rule sub-connection: generated group order":
            {"first base": ntsub["SP-E/REAL"]["generated_group_order"],
             "base G": (subs["%s/REAL" % sym[0]]["generated_group_order"]
                        if sym else 1),
             "first base read from": "the NT receipt (A12)"},
    }
    # WHY EACH AGREEMENT AGREES.  Declared per row, so that the twelve
    # agreements are not read as twelve independent confirmations.
    PROVENANCE = {
        "settings": "a copied design choice",
        "symmetric settings": "a copied design choice",
        "admitted after the j0 filter": "a consequence of the scope design",
        "admitted at the extension": "a consequence of the scope design",
        "total reduced paths": "graph combinatorics",
        "path pairs sharing both endpoints": "graph combinatorics",
        "realized-rule sub-connection: closed paths at the base point":
            "graph combinatorics",
        "holonomy group order at a symmetric setting": "geometry",
        "holonomy group structure":
            "geometry, at the declared completion (the type is "
            "completion-selected: GEN-COMPLETION-CENSUS)",
        "value set closed at the declared bound": "geometry",
        "elements outside every declared collection": "geometry",
        "realized-rule sub-connection: generated group order": "geometry",
    }
    for k, v in rows.items():
        if v["first base"] == v["base G"]:
            v["agrees because"] = PROVENANCE.get(k, "unclassified")
    kinds = {}
    for k, v in rows.items():
        if v["first base"] == v["base G"]:
            kinds[v["agrees because"].split(",")[0]] = kinds.get(
                v["agrees because"].split(",")[0], 0) + 1
    # THE CROSS-BASE CONNECTION COMPARISON, registered OPEN: the two bases'
    # admission tables are compared cell for cell in the PERMUTATION each
    # rule draws, which is the datum the class counts turn on.
    ntm = nt["tables"]["mechanism"]["identification_multiplicity"]
    ntorder = sorted({k.split("/")[0] for k in ntm})
    cells, agree_cells = 0, 0
    for i, sp in enumerate(SETTING_ORDER):
        if i >= len(ntorder):
            break
        for t in CHECKPOINTS:
            key_g = "%s/t%d" % (sp, t)
            key_n = "%s/t%d" % (ntorder[i], t)
            if key_n not in ntm or key_g not in TABLES["admission"][
                    "per_cell"]:
                continue
            g_cell = TABLES["admission"]["per_cell"][key_g]
            g_maps = {r["id"]: (g_cell[r["id"]]["maps"][0]
                                if g_cell[r["id"]]["drawn"] else None)
                      for r in ID_RULES}
            n_counts = ntm[key_n]["admitted_count_per_rule"]
            n_maps_list = ntm[key_n]["admitted_maps"]
            n_maps = {}
            for r in ID_RULES:
                if n_counts.get(r["id"]) == 1:
                    n_maps[r["id"]] = (
                        "the identity" if r["id"] == "FULL"
                        and "the identity" in n_maps_list
                        else ("the wing exchange"
                              if "the wing exchange" in n_maps_list
                              else None))
                else:
                    n_maps[r["id"]] = None
            cells += 1
            if g_maps == n_maps:
                agree_cells += 1
    TABLES["cross_base_connection"] = {
        "what_is_compared":
            "the permutation each gluing rule draws, cell for cell, at "
            "matched (setting index, checkpoint) coordinates",
        "cells_compared": cells,
        "cells_where_the_two_bases_draw_the_same_permutation_per_rule":
            agree_cells,
        "status": "OPEN: the agreement of the class counts across the two "
                  "bases is not explained by the shared graph and the "
                  "shared group (GEN-CONNECTION-CLASS-COUNTS); this "
                  "cell-for-cell agreement is the further structure the two "
                  "bases share, and this unit registers it as an open "
                  "question rather than as a mechanism"}
    TABLES["comparison_with_the_first_base"] = rows
    TABLES["comparison_provenance"] = {
        "agreements_by_kind": kinds,
        "differing_coordinates": [k for k, v in rows.items()
                                  if v["first base"] != v["base G"]],
        "the_coordinates_measured_to_carry_the_result": [
            "the preparation's Born-shadow symmetry type (it decides "
            "whether the wing exchange can be a co-reference at all: "
            "GEN-COMPLETION-IS-LOAD-BEARING)",
            "the declared completion (it decides the defect and with it "
            "the group: GEN-DEFECT-LAW, GEN-COMPLETION-CENSUS)"],
        "coordinates_measured_INERT_for_the_geometry": [
            "which rotation the two wings share at a symmetric setting "
            "(GEN-FAMILY-PROBE)",
            "the preparation vector itself, beyond its symmetry type, at "
            "a fixed completion (GEN-DEFECT-LAW)"],
        "the_rest":
            "the remaining differing coordinates -- the carrier size, the "
            "system dimension, the outcome count, the Schmidt rank and the "
            "scope size -- are not separately varied by this unit; they "
            "enter the elements' fixed-point counts, and no inertness is "
            "claimed for them",
        "differing_coordinates_that_are_not_one_of_the_two_carrying_ones":
            len([k for k, v in rows.items()
                 if v["first base"] != v["base G"]]) - 2}
    gate("GEN-COMPARISON", "measurement",
         "THE COMPARISON WITH THE FIRST BASE, COORDINATE BY COORDINATE, "
         "SPLIT INTO WHAT IS READ FROM ITS COMMITTED TERMINAL RECEIPT AND "
         "WHAT IS DECLARED HERE.  Nothing of the first base's MODEL is "
         "imported by this unit -- no fixture, no operator, no permutation "
         "-- and the only thing read from it is its receipt's reported "
         "numbers, which are anchored exit-1 so that a drift in either "
         "kills the run (A08-A12, A17).  Fifteen of the twenty-one rows now "
         "READ the first base's value from that receipt, including its "
         "declared arena, its defect's own name, and its group STRUCTURE, "
         "which is not typed but NAMED by this unit's own naming rule from "
         "the order, element orders and abelianness the receipt reports.  "
         "The remaining six -- the system dimension, the outcome count, the "
         "arithmetic, the preparation vector's behaviour under the wing "
         "exchange, its Schmidt rank and the symmetric-setting count -- are "
         "DECLARED HERE and marked as declared in the table itself, because "
         "the first base's receipt carries no such field; they are "
         "disclosures, not anchors.  EVERY AGREEMENT CARRIES ITS "
         "PROVENANCE: agreements are classified, in the table, as copied "
         "design choices, as consequences of the scope design, as graph "
         "combinatorics, or as geometry, and the counts are computed -- so "
         "the twelve agreements are not read as twelve independent "
         "confirmations.  The gate measures that the two bases genuinely "
         "DIFFER in their flesh, so the comparison is between two bases and "
         "not between a base and itself, and that every agreement is "
         "classified.  The `anchor-nt` mutant perturbs a reused first-base "
         "value and must die here",
         NC != 36 and NS != 2 and SCOPE["n_base"] != 72
         and all(v.get("agrees because", "x") != "unclassified"
                 for v in rows.values())
         and all(a["passed"] for a in ANCHORS if a["id"].startswith("A0")
                 or a["id"].startswith("A1")),
         {"differing_coordinates":
              [k for k, v in rows.items()
               if v["first base"] != v["base G"]],
          "agreeing_coordinates":
              [k for k, v in rows.items()
               if v["first base"] == v["base G"]],
          "agreements_by_kind": kinds,
          "rows_whose_first_base_value_is_read_from_the_NT_receipt":
              sum(1 for v in rows.values()
                  if not v["first base read from"].startswith("DECLARED")),
          "rows_whose_first_base_value_is_declared_here":
              sum(1 for v in rows.values()
                  if v["first base read from"].startswith("DECLARED")),
          "what_carries_the_result": TABLES["comparison_provenance"],
          "the_cross_base_connection_comparison":
              TABLES["cross_base_connection"],
          "table": rows})
    return rows


# ===========================================================================
# 10.  MATCHED COORDINATES, AND THE UNIT VERDICT
# ===========================================================================
def run_read_time(values, agg):
    """RUNBOOK section 15 addendum: the read time is a DECLARED coordinate
    of every node and of the law datum, so a comparison of two law data at
    different checkpoints can never read as an agreement."""
    prog("matched coordinates: the read time as a declared coordinate")
    cross = same = 0
    for sp in SETTING_ORDER:
        seen: dict = {}
        for fr in FRAMES:
            for t in CHECKPOINTS:
                seen[(fr, t)] = intern(structural_key(l_value(sp, fr, t)))
        for a in seen:
            for b in seen:
                if a >= b:
                    continue
                if a[1] != b[1] and seen[a] == seen[b]:
                    cross += 1
                if a[1] == b[1] and seen[a] == seen[b]:
                    same += 1
    # Is the read-time coordinate doing separating work on this base, or is
    # it determined by the endpoint?  MEASURED over every enumerated path:
    # the read time carried inside the L datum against the checkpoint of the
    # node the path ends at.
    carried = agreed = obstructed = 0
    for sp in SETTING_ORDER:
        for r in values[sp]:
            v = r["L"]
            if not isinstance(v, int) or v not in _INTERN_VALUE:
                obstructed += 1
                continue
            key = _INTERN_VALUE[v]
            carried += 1
            if key[0] == "L" and key[1] == r["end"][1]:
                agreed += 1
    TABLES["read_time"] = {
        "law_data_read_at_different_checkpoints_that_compare_equal": cross,
        "law_data_read_at_the_same_checkpoint_that_compare_equal": same,
        "the_matched_table_pairs_only_paths_sharing_both_endpoints": True,
        "paths_whose_carried_read_time_equals_the_endpoint_checkpoint":
            agreed,
        "paths_carrying_a_readable_law_datum": carried,
        "paths_whose_law_datum_is_obstructed_or_collapsed": obstructed}
    gate("GEN-READ-TIME-COORDINATE", "measurement",
         "THE READ TIME IS A DECLARED COORDINATE OF EVERY NODE AND OF THE "
         "LAW DATUM (RUNBOOK section 15 addendum), AND THE MATCHED TABLE "
         "READS EVERY CONTRAST AT MATCHED COORDINATES.  ONE MUST-PASS "
         "CLAUSE, and it can fail: no two law data read at DIFFERENT "
         "checkpoints compare equal -- measured over every pair of the "
         "declared nodes at every setting, the count gated at zero, with "
         "the count of pairs read at the SAME checkpoint that do compare "
         "equal gated positive so the zero is not the zero of an empty "
         "comparison.  It is the checkpoint tag inside the datum that "
         "makes the first count zero.  The former second clause -- that no "
         "pair of the matched table carries different read times at its two "
         "endpoints -- is WITHDRAWN from the predicate: the matched table "
         "is grouped BY endpoint pair, so that count could not be nonzero "
         "for any input, mutated or not, and a clause that cannot fail is a "
         "disclosure and not a gate (GEN-READ-TIME-FORCED).  The "
         "`readtime-conflate` mutant reads every node datum at the final "
         "checkpoint, which makes law data at different checkpoints compare "
         "equal, and must die here",
         cross == 0 and same > 0,
         {"law_data_read_at_different_checkpoints_that_compare_equal": cross,
          "law_data_read_at_the_same_checkpoint_that_compare_equal": same,
          "aggregate_pair_table": {o: {c: {"agree": agg[o][c][0],
                                           "disagree": agg[o][c][1]}
                                       for c in ("aligned", "crossing")}
                                   for o in ("L", "A")}})
    gate("GEN-READ-TIME-FORCED", "disclosure",
         "WHAT THE READ-TIME COORDINATE DOES ON THIS BASE, MEASURED AND "
         "DISCLOSED.  The matched table pairs only paths sharing BOTH "
         "endpoints, so matched coordinates there are STRUCTURAL -- a "
         "consequence of how the table is grouped, not a measurement -- and "
         "the corresponding count is reported here rather than gated.  "
         "Measured over every enumerated path that carries a readable law "
         "datum: the read time carried INSIDE the datum equals the "
         "checkpoint of the node the path ends at, at every one of them.  "
         "So on this base the coordinate is a FUNCTION OF THE ENDPOINT, and "
         "the discipline it enforces is satisfied structurally here; the "
         "must-pass content is the node-level clause of "
         "GEN-READ-TIME-COORDINATE, whose zero is what the tag buys, and "
         "the `readtime-conflate` mutant is what gives that clause its "
         "teeth",
         True,
         {"paths_whose_carried_read_time_equals_the_endpoint_checkpoint":
              agreed,
          "paths_carrying_a_readable_law_datum": carried,
          "paths_whose_law_datum_is_obstructed_or_collapsed": obstructed,
          "the_coordinate_is_a_function_of_the_endpoint_on_this_base":
              carried > 0 and agreed == carried})


def run_verdict(nontrivial, struct, comparison):
    """THE UNIT VERDICT, DERIVED FROM THE GATED PATTERNS AND FROM NOTHING
    ELSE.  The decision rule is pre-registered: ABSENT if P1 fails,
    REPRODUCES if all five pattern gates pass, VARIES otherwise with the
    failing patterns and the computed differences named."""
    prog("the unit verdict, derived from the five gated patterns")
    pg = {x["id"]: x["passed"] for x in GATES
          if x["id"].startswith("GEN-P")}
    order = ["GEN-P1-NONTRIVIAL-HOLONOMY", "GEN-P2-GROUP-COMPUTED",
             "GEN-P3-TWO-CURVATURE-SOURCES",
             "GEN-P4-DEFECT-IS-A-GROUP-ELEMENT",
             "GEN-P5-NON-PRINCIPALITY"]
    failed = [g for g in order if not pg.get(g, False)]
    diffs = [k for k, v in comparison.items()
             if v["first base"] != v["base G"]]
    if not pg.get("GEN-P1-NONTRIVIAL-HOLONOMY", False):
        verdict = "GEN-STRUCTURE-ABSENT"
    elif not failed:
        verdict = "GEN-STRUCTURE-REPRODUCES" + QUALIFIER
    else:
        verdict = "GEN-STRUCTURE-VARIES-<%s>" % ", ".join(failed)
    if MUTANT == "verdict-lax":
        verdict = "GEN-UNDECIDED"
    FINDINGS["unit_verdict"] = verdict
    FINDINGS["the_verdicts_declared_scope"] = SCOPE_CLAUSES
    FINDINGS["pattern_gates"] = {g: pg.get(g, False) for g in order}
    FINDINGS["computed_differences_from_the_first_base"] = diffs
    # THE SECOND CONJUNCT, MADE REAL: the verdict is re-derived here from
    # the recorded gate results -- read out of the receipt's own gate list,
    # not from the caller's arguments -- and compared with the string that
    # was emitted.  A waiver that overwrites the emitted string is caught by
    # this comparison and not only by the vocabulary check.
    recorded = {x["id"]: x["passed"] for x in GATES
                if x["id"].startswith("GEN-P") and x["class"] != "disclosure"
                and x["id"] in order}
    if not recorded.get("GEN-P1-NONTRIVIAL-HOLONOMY", False):
        rederived = "GEN-STRUCTURE-ABSENT"
    elif all(recorded.get(g, False) for g in order):
        rederived = "GEN-STRUCTURE-REPRODUCES" + QUALIFIER
    else:
        rederived = "GEN-STRUCTURE-VARIES-<%s>" % ", ".join(
            [g for g in order if not recorded.get(g, False)])
    gate("GEN-VOCABULARY", "derivation",
         "THE VERDICT IS DRAWN FROM THE PIN'S PRE-REGISTERED VOCABULARY AND "
         "FROM NOTHING ELSE, AND IT IS DERIVED FROM THE FIVE PATTERN GATES "
         "BY A PRE-REGISTERED RULE: ABSENT if P1 fails; REPRODUCES if all "
         "five pattern gates pass; VARIES, with the failing patterns named "
         "in the tag, otherwise; BLOCKED where a census cannot be posed.  "
         "The outcome name is pre-registered and the QUALIFIER states the "
         "scope the pin itself declares to be arena data -- the completion "
         "-- in the UNIT-OUTCOME-QUALIFIER form the vocabulary permits; no "
         "verdict name is invented.  TWO CLAUSES.  (1) The emitted verdict "
         "begins with one of the pre-registered names.  (2) The emitted "
         "verdict is RE-DERIVED inside this gate from the pattern gates as "
         "they were RECORDED in this receipt's own gate list -- not from "
         "the arguments the verdict routine was called with -- and the two "
         "strings are measured equal, so a verdict that did not come from "
         "the rule is caught here.  Reproduction of the PATTERNS is what "
         "the verdict reports; the computed DIFFERENCES between the two "
         "bases are reported beside it and never averaged into it.  The "
         "`verdict-lax` waiver emits an out-of-vocabulary tag and must die "
         "at both clauses",
         any(verdict.startswith(x) for x in PREREGISTERED)
         and verdict == rederived,
         {"unit_verdict": verdict,
          "the_verdict_re_derived_from_the_recorded_gate_results": rederived,
          "the_two_agree": verdict == rederived,
          "the_verdicts_declared_scope": SCOPE_CLAUSES,
          "pattern_gates": {g: pg.get(g, False) for g in order},
          "patterns_that_failed": failed,
          "computed_differences_from_the_first_base": diffs})
    return verdict


# ===========================================================================
# 11.  EXEMPTION, EXACTNESS AND THE DECLARATION ORDER
# ===========================================================================
def run_exemption_sweep():
    """RUNBOOK section 14 addendum: NO GATE PREDICATE MAY REFERENCE MUTANT
    IDENTITY.  This sweep parses THIS module and counts every comparison of
    the global MUTANT against anything with `!=` -- the exemption pattern --
    anywhere in the source, gate or not."""
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
        touches = any(isinstance(x, ast.Name) and x.id == "MUTANT"
                      for x in names)
        if not touches:
            continue
        if any(isinstance(op, ast.NotEq) for op in node.ops):
            found.append(node.lineno)
            wider["MUTANT != ..."].append(node.lineno)
        if any(isinstance(op, ast.NotIn) for op in node.ops):
            wider["MUTANT not in ..."].append(node.lineno)
        if any(isinstance(op, ast.IsNot) for op in node.ops):
            wider["MUTANT is not ..."].append(node.lineno)
    # THE DIRECT STATEMENT OF THE HEADLINE: walk the argument expressions of
    # every gate() and anchor() call site and count any reference to the
    # mutant flag anywhere inside them.
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
    outside_gates = {k: sorted(set(v) - set(reaching))
                     for k, v in wider.items()}
    gate("GEN-NO-MUTANT-EXEMPTION", "derivation",
         "NO GATE PREDICATE REFERENCES MUTANT IDENTITY (RUNBOOK section 14 "
         "addendum), MEASURED AS THE HEADLINE SAYS IT.  Two clauses, both "
         "from an AST sweep of this module's own source.  (1) THE DIRECT "
         "STATEMENT: every `gate(...)` and `anchor(...)` call site is "
         "found, its argument expressions are walked to any depth, and the "
         "number of call sites reaching the mutant flag at all -- in a "
         "predicate, a claim string or a value expression -- is measured to "
         "be ZERO, against the computed total number of call sites.  (2) "
         "THE EXEMPTION FORMS: `MUTANT != ...`, `MUTANT not in ...`, "
         "`MUTANT is not ...` and `not (MUTANT == ...)` are counted "
         "separately anywhere in the source, since a gate that counts only "
         "one of them does not enforce its own headline; every occurrence "
         "found is measured to lie OUTSIDE every gate and anchor call site, "
         "and the `!=` count itself is gated at zero.  Every mutation in "
         "this instrument is injected where the computation happens, and "
         "every declared falsifier dies by a gate's own predicate evaluated "
         "blind.  The `exempt-lax` waiver registers one such comparison and "
         "must die here",
         not found and not reaching,
         {"gate_and_anchor_call_sites": call_sites,
          "call_sites_reaching_the_mutant_flag": sorted(set(reaching)),
          "exemption_forms_found_anywhere_in_the_source":
              {k: len(v) for k, v in wider.items()},
          "their_line_numbers": {k: sorted(set(v))
                                 for k, v in wider.items() if v},
          "all_of_them_outside_any_gate_or_anchor_call_site":
              outside_gates == {k: sorted(set(v)) for k, v in wider.items()},
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
    gate("GEN-EXACT", "derivation",
         "EXACT ARITHMETIC EVERYWHERE.  An AST sweep of this module finds no "
         "float literal and no call to `float`, and a runtime sweep finds no "
         "float in any value that reached a gate or an anchor.  The "
         "substrate is `fractions.Fraction`: every declared operator of base "
         "G has RATIONAL entries and is exactly orthogonal over Q, so "
         "equality of matrices is equality of exact rationals and no "
         "tolerance exists anywhere in this instrument.  The `float-lax` "
         "mutant introduces a float literal and must die here",
         not lits and not calls and not runtime,
         {"float_literal_lines": lits, "float_call_lines": calls,
          "rows_carrying_a_float": runtime,
          "fraction_available": str(Fr(1, 2))})


def run_declaration_order():
    """The receipt's own gate ORDER is the proof that the base was declared
    as data before any transport measurement."""
    ids = [g["id"] for g in GATES]
    decl = ["GEN-FREEZE", "GEN-BASE-PINNED", "GEN-SPECIES",
            "GEN-COMPLETION-IS-LOAD-BEARING", "GEN-ARENA"]
    transport = ["GEN-PATH-SPACE-ENUMERATED", "GEN-P1-NONTRIVIAL-HOLONOMY",
                 "GEN-P2-GROUP-COMPUTED", "GEN-P3-TWO-CURVATURE-SOURCES",
                 "GEN-P4-DEFECT-IS-A-GROUP-ELEMENT",
                 "GEN-P5-NON-PRINCIPALITY"]
    present = all(g in ids for g in decl + transport)
    last_decl = max((ids.index(g) for g in decl if g in ids), default=-1)
    first_tr = min((ids.index(g) for g in transport if g in ids),
                   default=len(ids))
    gate("GEN-DECLARATION-ORDER", "derivation",
         "THE RECEIPT'S GATE ORDER PROVES THE FREEZE.  The pin requires the "
         "second base to be declared AS DATA before any transport "
         "measurement, and the proof is the order in which this receipt's "
         "gates were recorded: every base-declaration gate -- the freeze, "
         "the pinned completion and rotations, the species clauses, the "
         "completion's symmetry facts, the arena with its computed sizes -- "
         "is measured to sit STRICTLY BEFORE the first transport gate, and "
         "the freeze gate is measured to be the first gate of the run with "
         "the transport-datum counter at zero.  The `order-lax` mutant "
         "emits a transport measurement before the declarations and must "
         "die here",
         present and last_decl < first_tr and ids[0] == "GEN-FREEZE",
         {"first_gate": ids[0],
          "last_base_declaration_gate_index": last_decl,
          "first_transport_gate_index": first_tr,
          "base_declaration_gates": decl,
          "transport_gates": transport,
          "gate_order": ids})


# ===========================================================================
# 12.  THE MUTANT TABLE
# ===========================================================================
MUTANT_DECL = (
    ("prefix-lax", "computation",
     "the leg prefix read as the whole declared leg list"),
    ("path-collapse", "computation",
     "every path given the same transported key"),
    ("reduce-lax", "computation", "the reduced-path condition dropped"),
    ("label-collapse", "computation",
     "the holonomy value set counted as name labels, not permutations"),
    ("hol-basepoint", "computation",
     "the based holonomy read at every base point at once"),
    ("gauge-sign", "computation",
     "the switching dropped on a reversed traversal"),
    ("gauge-subsample", "computation", "the switching sweep subsampled"),
    ("memo-lax", "computation", "the self-test allowed to read the cache"),
    ("freeze-lax", "computation",
     "one transport datum evaluated before the freeze"),
    ("order-lax", "computation",
     "a transport measurement emitted before the base declaration"),
    ("float-lax", "waiver",
     "a float literal registered in the exactness gate's own evidence list "
     "after its AST sweep has run: the source text is never edited, so this "
     "is a waiver and is declared as one"),
    ("exempt-lax", "waiver",
     "a mutant-identity exemption registered in the exemption gate's own "
     "evidence list after its AST sweep has run: the source text is never "
     "edited, so this is a waiver and is declared as one"),
    ("orient-flip", "computation",
     "a leg's reverse traversal read without transposition"),
    ("id-lax", "computation",
     "every admitted permutation accepted as an identification"),
    ("scope-lax", "computation", "the admitted relabelling scope subsampled"),
    ("readtime-conflate", "computation",
     "every node datum read at the final checkpoint"),
    ("defect-order", "computation",
     "the completion's non-equivariance defect composed in the wrong order"),
    ("anchor-completion", "computation",
     "one entry of the constructed completion perturbed"),
    ("completion-Q", "computation",
     "the declared completion replaced by the bare Householder"),
    ("scope-gen", "computation",
     "the declared relabelling scope generated from a truncated generator"),
    ("anchor-rot", "computation",
     "one entry of a constructed declared rotation perturbed"),
    ("anchor-record", "computation",
     "the pointer shift made non-injective, so the record is destroyed"),
    ("anchor-nt", "computation",
     "a reused first-base committed value perturbed"),
    ("nt-hash", "computation",
     "the external receipt's bytes perturbed before they are hashed"),
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
        r["declaration"] = [m[2] for m in MUTANT_DECL
                            if m[0] == r["mutant"]][0]
    must = [x["id"] for x in GATES if x["class"] != "disclosure"
            and x["id"] != "GEN-FALSIFICATION"]
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
    gate("GEN-FALSIFICATION", "derivation",
         "EVERY MUST-PASS GATE IS FALSIFIED BY SOME MUTANT, AND EVERY "
         "MUTANT DIES.  Each declared mutant is run to completion, must "
         "exit 1, and must falsify at least one NAMED gate or anchor; the "
         "second clause is the one that matters -- the set of must-pass "
         "gates that NO mutant falsifies is measured to be EMPTY.  Each "
         "mutant declares its KIND and the split is counted from the "
         "declaration: a WAIVER proves a gate's predicate is load-bearing "
         "for the exit code, not that the gate would catch a computational "
         "defect, and the two are not claimed to be the same thing.  BOTH "
         "DENOMINATORS ARE REPORTED, because they differ: the count of "
         "must-pass gates falsified by SOME mutant, and the smaller count "
         "falsified by a mutant that perturbs a COMPUTATION.  The gates "
         "carried by a waiver alone are named, not averaged away.  The one "
         "gate excluded from the denominator is this one: `run_mutant_table` "
         "does not run inside a mutant, so the census gate does not exist "
         "there and cannot be falsified by this mechanism at all",
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
          "the_gate_excluded_from_the_denominator": "GEN-FALSIFICATION",
          "never_falsified": never})


# ===========================================================================
# 13.  RECEIPT AND RENDER
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
            cur = (cur + " " + word).strip()
    if cur:
        out.append(cur)
    return out or [""]


def render(rec):
    L = []
    W = 78

    def hdr(t):
        L.append("")
        L.append("-" * W)
        L.append(t)
        L.append("-" * W)

    def kv(k, v, ind=2):
        L.append(" " * ind + "%-52s %s" % (k, v))

    L.append("=" * W)
    L.append("GEN -- THE GENERALITY CHECK: THE NT GEOMETRY ON A SECOND BASE")
    L.append("=" * W)
    L.append("pin %s (sha %s)   immutable base %s"
             % (PIN_COMMIT, PIN_SHA256, BASE_COMMIT))
    L.append("source sha256 %s" % rec["source_sha256"])

    d = TABLES["declarations"]
    hdr("1.  BASE G, DECLARED AS DATA (before any transport measurement)")
    for k, v in sorted(d["carrier"].items()):
        kv(k, v)
    L.append("")
    L.append("  the declared measurement family (integer quaternions):")
    for r in ROT_ORDER:
        kv("  %s  quaternion %s" % (r, d["measurement_family"]
                                    ["quaternions"][r]),
           d["measurement_family"]["pinned_rotation_matrices"][r])
    kv("outcomes per measurement",
       d["measurement_family"]["outcomes_per_measurement"])
    kv("pointer shift of outcome o",
       d["measurement_family"]["pointer_shift_of_outcome_o"])
    L.append("")
    L.append("  the declared preparation:")
    kv("psi", d["preparation"]["vector_psi_coefficients"])
    for ln in _wrap("completion rule: "
                    + d["preparation"]["completion_rule"], W - 4):
        L.append("    " + ln)
    kv("Q as a permutation of the 9 system-pair indices",
       d["preparation"]["Q_as_a_permutation_of_the_9_system_pair_indices"])
    L.append("")
    L.append("  THE PINNED ORTHOGONAL COMPLETION V (column 0 is psi):")
    hdrs = ["(%d,%d)" % (a, b) for a in range(NS) for b in range(NS)]
    L.append("      " + " ".join("%9s" % h for h in hdrs))
    for i, row in enumerate(d["preparation"]["pinned_completion_matrix_V"]):
        L.append("  %5s " % hdrs[i] + " ".join("%9s" % v for v in row))
    kv("U_prep", d["preparation"]["U_prep"])
    L.append("")
    L.append("  the declared setting family (six):")
    for sp in SETTING_ORDER:
        kv("  " + sp, "wing A = %s, wing B = %s"
           % tuple(d["settings"][sp]))
    L.append("")
    L.append("  the declared transported objects:")
    for o in d["objects"]:
        L.append("    %s -- %s" % (o["id"], o["name"]))
        for ln in _wrap("datum: " + o["datum"], W - 8):
            L.append("        " + ln)
        for ln in _wrap("action: " + o["action"], W - 8):
            L.append("        " + ln)
    L.append("")
    L.append("  the declared gluing rules:")
    for r in d["identification_rules"]:
        L.append("    %s (%s)" % (r["id"], r["name"]))
        for ln in _wrap(r["definition"], W - 8):
            L.append("        " + ln)

    hdr("2.  THE ARENA (RUNBOOK section 15), every size computed")
    for k, v in sorted(TABLES["arena"].items()):
        kv(k, v)

    hdr("3.  THE BASE, VERIFIED AS DECLARED")
    b = TABLES["base_declaration"]
    for k in ("psi_schmidt_rank", "psi_is_invariant_under_the_system_"
              "exchange",
              "the_born_shadow_of_psi_is_invariant_under_the_system_"
              "exchange",
              "the_born_shadow_of_the_householder_H_is_exchange_symmetric",
              "the_born_shadow_of_the_declared_completion_V_is_exchange_"
              "symmetric",
              "completion_is_orthogonal", "psi_is_a_unit_vector",
              "the_projectors_are_orthonormal",
              "every_local_leg_is_a_sum_of_projectors_times_shifts",
              "pointer_shifts"):
        kv(k, b[k])
    kv("declared operators measured orthogonal",
       "%d/%d" % (sum(1 for v in b["declared_operators_are_orthogonal"]
                      .values() if v),
                  len(b["declared_operators_are_orthogonal"])))
    kv("local-leg commutation cells measured",
       "%d/%d" % (sum(1 for v in b["the_local_legs_commute"].values() if v),
                  len(b["the_local_legs_commute"])))

    hdr("4.  THE ADMISSION TABLE AND THE ALIGNMENT PROFILE")
    a = TABLES["admission"]
    L.append("  %-14s %-26s %-26s" % ("cell", "FULL admits", "REAL admits"))
    for sp in SETTING_ORDER:
        for t in CHECKPOINTS:
            r = a["per_cell"]["%s/t%d" % (sp, t)]
            L.append("  %-14s %-26s %-26s"
                     % ("%s/t%d" % (sp, t),
                        "%d %s" % (r["FULL"]["n_admitted"],
                                   r["FULL"]["maps"]),
                        "%d %s" % (r["REAL"]["n_admitted"],
                                   r["REAL"]["maps"])))
    L.append("")
    kv("leg-prefix alignment profile", a["alignment_profile"])
    kv("cells where alignment agrees with the FULL profile",
       "%d/%d" % (a["cells_where_alignment_agrees_with_the_full_rule_"
                    "profile"], a["cells"]))

    hdr("5.  THE PATH SPACE (enumerated)")
    ps = TABLES["path_space"]
    L.append("  %-8s %6s %6s %6s %6s %8s %8s"
             % ("setting", "nodes", "links", "id", "rank", "paths",
                "closed"))
    for sp in SETTING_ORDER:
        r = ps[sp]
        L.append("  %-8s %6d %6d %6d %6d %8d %8d"
                 % (sp, r["nodes"], r["links"], r["identification_links"],
                    r["cycle_rank"], r["paths"], r["closed_paths"]))
    kv("total reduced paths", ps["_total_paths"])
    kv("path pairs sharing both endpoints", ps["_total_pairs"])
    L.append("")
    L.append("  the matched table of path pairs (agree / disagree):")
    ag = TABLES["pair_table"]["aggregate"]
    for o in ("L", "A"):
        for c in ("aligned", "crossing"):
            kv("  %s / %s" % (o, c), "%d / %d" % (ag[o][c]["agree"],
                                                  ag[o][c]["disagree"]))

    hdr("6.  THE DECLARED PROBES")
    L.append("  %-46s %-30s" % ("probe", "holonomy (permutation part)"))
    for k, v in TABLES["probes"].items():
        L.append("  %-46s %-30s" % (k, v["A_permutation_name"]))

    hdr("7.  THE FIVE PRE-REGISTERED PATTERNS")
    f = FINDINGS["patterns"]
    kv("P1  a nontrivial holonomy group exists",
       "%s   at %s" % (f["P1_nontrivial_holonomy_exists"], f["P1_settings"]))
    kv("P2  group order per setting", f["P2_group_order"])
    kv("P2  structure named", f["P2_structure"])
    for sp in SETTING_ORDER:
        g = FINDINGS["holonomy_group"]["per_setting"][sp]
        kv("      %s elements" % sp, g["elements"])
        kv("      %s fixed points" % sp, g["element_fixed_points"])
        kv("      %s value set closed / is the group" % sp,
           "%s / %s" % (g["the_value_set_is_closed_under_composition"],
                        g["the_value_set_is_the_generated_group"]))
        kv("      %s not-a-signed-permutation closed paths" % sp,
           g["closed_paths_whose_holonomy_is_not_a_signed_permutation"])
    kv("P3  coordinates of identification multiplicity >= 2",
       f["P3_multiplicity_coordinates"])
    kv("P3  single-rule sub-connections measured non-flat",
       f["P3_single_rule_subconnections_non_flat"])
    kv("P3  the completion's non-equivariance defect",
       f["P3_non_equivariance_defect"])
    kv("P4  the defect is a group element", f["P4_defect_is_a_group_element"])
    kv("P5  elements outside every declared collection",
       f["P5_elements_outside_every_declared_collection"])
    L.append("")
    L.append("  the membership table, element by element:")
    for sp in SETTING_ORDER:
        for nm, r in TABLES["structure_group"]["per_setting"][sp].items():
            L.append("    %-8s %-46s scope=%-5s ext=%-5s adm=%-5s"
                     % (sp, nm, r["in_the_declared_relabelling_scope"],
                        r["in_the_declared_extension_scope"],
                        r["in_the_admitted_set"]))

    hdr("8.  THE SINGLE-RULE SUB-CONNECTIONS (P3, source (i) isolated)")
    L.append("  %-18s %5s %5s %8s %6s  %s"
             % ("setting / rules", "links", "rank", "closed", "group",
                "classes"))
    for k, v in TABLES["mechanism"]["single_rule_subconnections"].items():
        L.append("  %-18s %5d %5d %8d %6d  %s"
                 % (k, v["links"], v["cycle_rank"],
                    v["closed_paths_at_the_base_point"],
                    v["generated_group_order"], v["holonomy_classes"]))

    hdr("9.  THE GAUGE LAYER (RUNBOOK section 14), swept complete")
    gs = TABLES["gauge_selftest"]
    for sp in SETTING_ORDER:
        kv(sp, gs["group_sizes"][sp])
    gg = [x for x in GATES if x["id"] == "GEN-GAUGE-COVARIANCE"][0]["value"]
    for k, v in gg.items():
        if k != "group_sizes":
            kv(k, v)
    fe = [x for x in GATES if x["id"] == "GEN-FRESH-EVAL"][0]["value"]
    for k, v in fe.items():
        kv(k, v)

    hdr("10.  THE DECLARATION FLIP-TESTS")
    kv("loops flipped", TABLES["flip_tests"]["loops_flipped"])
    kv("loops where the reversal is not the inverse",
       TABLES["flip_tests"]["loops_where_the_reversal_is_not_the_inverse"])
    L.append("")
    L.append("  the completion flip-test (the bare Householder):")
    for k, v in TABLES["completion_flip_test"]["measured_at_the_"
                                               "alternative"].items():
        if k != "admission_counts_per_cell":
            kv("  " + k, v)

    hdr("10b.  THE COMPLETION CENSUS (the declared family, swept whole)")
    dl = TABLES["defect_law"]
    L.append("  the defect law:  " + dl["the_law"])
    for ln in _wrap("the cancellation: " + dl["the_cancellation"], W - 4):
        L.append("    " + ln)
    L.append("")
    L.append("  %-46s %-8s %-8s %-8s"
             % ("declared preparation vector", "invar.", "law", "same D"))
    for k, v in dl["per_declared_preparation_vector"].items():
        L.append("  %-46s %-8s %-8s %-8s"
                 % (k[:46], v["the_vector_is_exchange_invariant"],
                    v["the_law_D_equals_sigma_Vt_sigma_V_tensor_I"],
                    v["the_defect_equals_the_declared_completions_defect"]))
    L.append("")
    c = TABLES["completion_census"]
    for k in ("family_size", "swept", "geometry_bearing_members",
              "members_whose_defect_is_the_identity",
              "the_exceptions_are_exactly_the_exchange_equivariant_locus",
              "the_dihedral_relation_holds_at_every_member",
              "the_predicted_holonomy_group_order_spectrum",
              "geometry_bearing_members_whose_defect_escapes_every_"
              "declared_collection",
              "geometry_bearing_members_whose_defect_lies_inside_a_"
              "declared_collection"):
        kv(k, c[k])
    kv("members by the order of the defect",
       c["members_by_the_order_of_the_defect"])
    kv("members by the defect's fixed configurations",
       c["members_by_the_fixed_configurations_of_the_defect"])
    kv("the declared completion's own entry", c["the_declared_completions_"
                                                "entry"]["order"])
    L.append("")
    rb = TABLES["completion_rebuilds"]
    for ln in _wrap(rb["the_rebuild_scope"], W - 4):
        L.append("    " + ln)
    kv("the declared-form sub-family, size", rb["sub_family_size"])
    kv("its split", rb["the_split_of_the_declared_form_sub_family"])
    kv("members where the measured order differs from 2n",
       rb["members_where_the_measured_group_order_differs_from_the_"
          "dihedral_prediction"])
    L.append("")
    L.append("  one full rebuild per measured class:")
    L.append("    %-14s %-26s %-8s %-8s %-8s %-6s"
             % ("class", "Q", "predict", "measured", "abelian", "vset"))
    for k, v in TABLES["completion_rebuilds"][
            "one_full_rebuild_per_measured_class"].items():
        L.append("    %-14s %-26s %-8s %-8s %-8s %-6s"
                 % (k, v["Q"], v["the_dihedral_prediction_for_the_group_"
                                 "order"],
                    v["the_measured_group_order_at_the_symmetric_setting"],
                    v["abelian"], v["value_set_size"]))
    L.append("")
    ce = TABLES["connection_enumeration"]
    L.append("  the connection enumeration on the gauge-fixed graph (%s):"
             % ce["setting"])
    for k in ("independent_cycles", "based_closed_walks_checked",
              "walks_where_the_cycle_model_disagrees_with_the_direct_"
              "holonomy",
              "the_measured_class_counts", "connections_enumerated",
              "distinct_class_count_profiles",
              "connections_reproducing_the_measured_profile",
              "connections_whose_labels_generate_the_whole_group",
              "of_those_reproducing_the_measured_profile",
              "the_most_common_profile"):
        kv("  " + k, ce[k])
    L.append("")
    fp = TABLES["family_probe"]
    L.append("  the measurement-family probe:")
    for k, v in fp["per_setting"].items():
        kv("  " + k, "%s  group=%s  classes=%s"
           % (v["wings"], v["generated_group_order"],
              v["class_counts_at_the_base_point"]))
    kv("  the group and the class counts are the same at every symmetric "
       "setting",
       fp["the_group_and_the_class_counts_are_the_same_at_every_symmetric_"
          "setting"])

    hdr("11.  THE COMPARISON WITH THE FIRST BASE (anchored exit-1)")
    L.append("  %-46s %-22s %-16s %s"
             % ("coordinate", "first base", "base G", "provenance"))
    for k, v in TABLES["comparison_with_the_first_base"].items():
        L.append("  %-46s %-22s %-16s %s"
                 % (k[:46], str(v["first base"])[:22],
                    str(v["base G"])[:16],
                    v.get("agrees because",
                          "DIFFERENT")[:40]))
    L.append("")
    cp = TABLES["comparison_provenance"]
    kv("agreements by kind", cp["agreements_by_kind"])
    kv("differing coordinates", len(cp["differing_coordinates"]))
    for x in cp["the_coordinates_measured_to_carry_the_result"]:
        for ln in _wrap("carries the result: " + x, W - 6):
            L.append("      " + ln)
    for x in cp["coordinates_measured_INERT_for_the_geometry"]:
        for ln in _wrap("measured inert: " + x, W - 6):
            L.append("      " + ln)
    cb = TABLES["cross_base_connection"]
    kv("cross-base admission cells compared", cb["cells_compared"])
    kv("cells where both bases draw the same permutation per rule",
       cb["cells_where_the_two_bases_draw_the_same_permutation_per_rule"])
    for ln in _wrap(cb["status"], W - 4):
        L.append("    " + ln)

    hdr("12.  ANCHORS")
    for a in rec["anchors"]:
        L.append("  %-6s %-8s %s" % (a["id"], "PASS" if a["passed"]
                                     else "FAIL", a["quantity"]))
        L.append("         source: %s" % a["source"])

    hdr("13.  GATES")
    for g in rec["gates"]:
        L.append("  %-40s %-12s %s"
                 % (g["id"], g["class"], "PASS" if g["passed"] else "FAIL"))
        for ln in _wrap(g["claim"], W - 6):
            L.append("      " + ln)
        L.append("      value: " + canon(g["value"])[:2000])
        L.append("")

    if "mutants" in TABLES:
        hdr("14.  THE MUTANT TABLE")
        L.append("  %-20s %-12s %-5s %s"
                 % ("mutant", "kind", "exit", "falsified"))
        for r in TABLES["mutants"]:
            L.append("  %-20s %-12s %-5d %s"
                     % (r["mutant"], r["kind"], r["exit"],
                        r["falsified_anchors"] + r["falsified_gates"]))
        gf = TABLES["gate_falsification"]
        kv("must-pass gates", len(gf["must_pass_gates"]))
        kv("falsified by some mutant", len(gf["falsified_by_some_mutant"]))
        kv("falsified by a computation mutant",
           len(gf["falsified_by_a_computation_mutant"]))
        kv("falsified only by a waiver", gf["falsified_only_by_a_waiver"])
        kv("NEVER FALSIFIED", gf["never_falsified"])

    hdr("15.  THE UNIT VERDICT")
    kv("pattern gates", FINDINGS["pattern_gates"])
    kv("computed differences from the first base",
       FINDINGS["computed_differences_from_the_first_base"])
    kv("the verdict's declared scope",
       ", ".join(FINDINGS["the_verdicts_declared_scope"]))
    L.append("")
    L.append("  " + FINDINGS["unit_verdict"])
    L.append("")
    for ln in _wrap(FINDINGS["thesis"], W - 2):
        L.append("  " + ln)
    L.append("")
    kv("anchors", rec["totals"]["anchors"])
    kv("gates (must-pass / disclosure)",
       "%d / %d" % (rec["totals"]["must_pass_gates"],
                    rec["totals"]["disclosures"]))
    kv("must-pass failures", rec["totals"]["must_pass_failures"])
    L.append("")
    return "\n".join(L) + "\n"


# ===========================================================================
# MAIN
# ===========================================================================
def main():
    global MUTANT, SOURCE_SHA256, VCOMP, SCOPE, ROT
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
    VCOMP = completion()
    SCOPE = declared_scope()
    _FIXTURE.clear()
    if MUTANT == "freeze-lax":
        node_law(SETTING_ORDER[0], "F1", 1)
    if MUTANT == "order-lax":
        gate("GEN-P1-NONTRIVIAL-HOLONOMY", "measurement",
             "emitted before the base declaration", True, {})
    run_freeze()

    run_base_declaration()
    run_external_pin()
    run_arena()

    pref = prefix_profile()
    run_admission(pref)

    graphs, values = run_paths(pref)
    pairs, totals, agg = run_pair_table(graphs, values)
    ps = run_path_space_audit(graphs, values, totals)
    # The defect's own permutation is named BEFORE the probes are printed,
    # so that the negative control's holonomy is reported by name rather
    # than as "another permutation".  Names are printing only: every gate
    # predicate in this unit compares permutation tuples.
    _D0 = prep_defect()
    if _D0["perm"] is not None:
        PERM_NAME.setdefault(canon(list(_D0["perm"])),
                             "the completion's non-equivariance defect")
        PERM_NAME.setdefault(
            canon(list(perm_compose(tuple(WSWAP), tuple(_D0["perm"])))),
            "the wing exchange composed with the non-equivariance defect")
    probes = run_probes(graphs)
    run_controls(graphs, values, probes)
    hg, D, subs, esc, nontrivial, struct = run_patterns(graphs, values,
                                                        pref, probes)
    run_read_time(values, agg)
    run_gauge_selftest(graphs)
    run_flip_tests(graphs, probes)
    run_scope_disclosure(pref)
    run_completion_flip({
        "V": "H . Q, the pinned matrix of section 1",
        "born_shadow_is_exchange_symmetric":
            TABLES["base_declaration"]["the_born_shadow_of_the_declared_"
                                       "completion_V_is_exchange_symmetric"],
        "identification_links_per_setting":
            {sp: TABLES["path_space"][sp]["identification_links"]
             for sp in SETTING_ORDER},
        "holonomy_group_order_per_setting":
            {sp: hg[sp]["generated_group_order"] for sp in SETTING_ORDER}})
    run_defect_law()
    census, first_of_order = run_completion_census()
    run_completion_rebuilds(first_of_order, hg)
    run_connection_enumeration(graphs, values, hg)
    run_family_probe()
    comparison = run_comparison(hg, D, subs, esc, nontrivial, struct, ps)

    sym = sorted(nontrivial)
    cen = TABLES["completion_census"]
    reb = TABLES["completion_rebuilds"]
    FINDINGS["thesis"] = (
        "A SECOND BASE of the same structural species -- two wings, a "
        "preparation, commuting local legs, records at the final division "
        "event -- was constructed with genuinely different flesh: qutrit "
        "systems instead of qubits, %d configurations instead of 36, three "
        "outcomes per measurement instead of two, exact arithmetic over the "
        "RATIONALS instead of a quartic field, and a different preparation "
        "whose orthogonal completion is PINNED EXPLICITLY as data.  On that "
        "base the five pre-registered patterns were re-measured, each gated "
        "separately.  All five HOLD AT THE DECLARED COMPLETION: a "
        "nontrivial based holonomy group exists at the symmetric settings; "
        "counted as PERMUTATION TUPLES it has order %s, is measured already "
        "CLOSED at the declared length bound, and is %s; both curvature "
        "sources are exhibited -- identification multiplicity at the "
        "coordinates where two rules draw different maps, and, isolated by "
        "running the single-rule sub-connections separately, the "
        "COMPLETION'S NON-EQUIVARIANCE DEFECT, which already makes the "
        "realized-rule sub-connection non-flat at multiplicity one; that "
        "defect is measured to BE an element of the group; and two of the "
        "group's four elements are measured to lie outside the declared "
        "relabelling scope, outside its declared extension and outside both "
        "admitted sets, so the connection is NOT PRINCIPAL for this base's "
        "own isomorphisms either.  THE COMPLETION IS THE PARAMETER THAT "
        "DECIDES, AND IT IS SWEPT EXHAUSTIVELY.  The defect obeys the exact "
        "law D = (sigma V^T sigma V) (x) I_9, which for V = H . Q with an "
        "exchange-invariant psi cancels to (sigma Q^T sigma Q) (x) I_9: the "
        "defect is INDEPENDENT OF THE PREPARATION VECTOR and is "
        "manufactured by the declared transposition alone, so BOTH "
        "curvature sources on this base are declaration-side.  Over the "
        "whole declared completion family -- %d members, every one swept -- "
        "%d bear geometry and the %d that do not are exactly the "
        "exchange-equivariant locus: EXISTENCE IS GENERIC, and the "
        "flip-test's bare Householder is a member of the rare exceptional "
        "class.  The ISOMORPHISM TYPE, by contrast, is completion-selected: "
        "the family is dihedral, <W, D | W^2 = D^n = 1, W D W = D^-1> with "
        "n the defect's order, the predicted group orders %s all exhibited "
        "by full rebuild, and inside the pinned completion's own declared "
        "form -- a single basis transposition, %d members, all rebuilt -- "
        "%d give the Klein four-group, %d give the NON-ABELIAN group of "
        "order six and %d are flat.  What recurs across the two bases is "
        "therefore the PRESENTATION and the existence of a nontrivial group "
        "with two sources and a scope-escaping generator; the isomorphism "
        "type is a function of the declared completion, and the pinned "
        "completion's class -- the defect fixing 45 of the 81 "
        "configurations -- is %s of the family.  Stated at the committed "
        "finite scope, at the declared admission scope, AT THE DECLARED "
        "COMPLETION, per coordinate; nothing is claimed about nature."
        % (NC,
           hg[sym[0]]["generated_group_order"] if sym else 1,
           struct[sym[0]] if sym else "trivial",
           cen["family_size"], cen["geometry_bearing_members"],
           cen["members_whose_defect_is_the_identity"],
           cen["the_predicted_holonomy_group_order_spectrum"],
           reb["sub_family_size"],
           reb["the_split_of_the_declared_form_sub_family"].get(
               "the Klein four-group", 0),
           reb["the_split_of_the_declared_form_sub_family"].get(
               "a non-abelian group of order 6", 0),
           reb["the_split_of_the_declared_form_sub_family"].get(
               "trivial", 0),
           ("%d of %d"
            % (cen["members_by_the_fixed_configurations_of_the_defect"]
               .get("45", 0), cen["family_size"]))))

    run_verdict(nontrivial, struct, comparison)
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
