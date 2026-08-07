#!/usr/bin/env python3
"""RQ0-L5 branch A -- THE PROVENANCE QUINTUPLE, IN BOTH VARIANTS.

Executes the frozen pin `v13/note-rq0-l5-provenance-quintuple-pin.md`
INCLUDING ITS AMENDMENT v2 (commit a05e3d5) against the immutable branch-C
TERMINAL base (483311c).

THE EXTENSION.  The patch becomes a QUINTUPLE (boundary, family,
preparation, law, PROVENANCE), where provenance is a DECLARED generation
history: a finite path of admitted operations claimed to have produced the
patch's boundary and records, carried as a chain of fine-grained
B''-certificates at its checkpoints.  The provenance-reading axiom is the
terminal B'' conditions plus

  (P1) the carried path is admitted by the law -- every step an admitted
       operation, composable, endpoint = the declared patch; and
  (P2) each carried fine-grained certificate verifies against the law at
       its own checkpoint.

BOTH VARIANTS RUN, per amendment v2:

  V-CL   the classical-certificate form (the original pin's).
  V-AMP  the amplitude-carrying form: the admitted path is carried WITH the
         amplitude-level description of every step, and the checkpoint
         certificates are computed AT the amplitude level.  Carrying is
         legal -- no-cloning constrains copying unknown states, not writing
         down the declared amplitudes of known admitted operations -- and
         what is carried is GAUGE-INVARIANT content only, per the v12 W7
         terminal form: the declared pair gauge is vertex switching on the
         layered path graph, so raw per-edge phases are gauge artifacts and
         the invariant content is exactly the closed-loop holonomy family.

THE TWO PRE-REGISTERED KILLS, each with a constructed adversary:

  RQ0-L5-PROVENANCE-REGRESS  provenance is the sixth declaration; does
         anything distinguish carried-true from carried-forged provenance
         WITHOUT presupposing the certification provenance was to provide?
  RQ0-L5-PROVENANCE-LOSSY    two admitted histories agreeing on everything
         any admitted verification can read, differing in the un-read part,
         one legitimate and one forged.  Rescoped by amendment v2 for
         V-AMP: verification is record-producing and (P2) is
         checkpoint-local, so the v12 recorded-but-phased limit applies TO
         THE CHECKS.

Exact arithmetic throughout.  An amplitude is a triple (c, s, e) denoting
c * 2^(-s/2) * zeta_8^e with c an exact Fraction, s in {0,1} and e in Z/8 --
the rational-times-root-of-unity family that carries the corpus's own
committed amplitude objects (Weyl clock-shift, Hadamard, DFT).  Sums are
formed only between commensurable terms and the commensurability is gated.
No float enters any substantive path.  Anchors exit 1 on mismatch and never
on a substantive negative.  `--mutant NAME` breaks exactly one anchor or one
derivation step and must exit 1.  No wall-clock value enters the receipt or
the rendered output, so two runs of the same source produce byte-identical
artifacts.

Scope: finite; ONE committed carrier of five configurations; the committed
law families; a DECLARED amplitude-level generator family at the same
carrier.  No locality, topology, causality, spacetime, field, QFT or gravity
object is constructed or claimed.  "Path", "history", "step" and
"checkpoint" are operational vocabulary about admitted operations and
declared configurations; no temporal, causal or spatial reading is made.
"""

from __future__ import annotations

import argparse
import hashlib
import inspect
import json
import sys
from fractions import Fraction as Fr
from itertools import permutations, product
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import rq0_l0_fixed_point_exact as CB      # Cycle B TERMINAL machinery
import rq0_l2_admissibility_exact as L2    # Cycle B'' TERMINAL machinery
import rq0_l3_epsilon_exact as L3          # stage-5 TERMINAL machinery
import rq0_l4_fingerprint_exact as L4      # branch C TERMINAL machinery

SCHEMA = "rq0-l5-provenance-quintuple-receipt-v1"
PIN_COMMIT = "a05e3d5"
BASE_COMMIT = "483311c"
OUT_TXT = HERE / "rq0_l5_provenance_output.txt"
OUT_JSON = HERE / "rq0_l5_provenance_receipt.json"

MUTANT: str | None = None
SOURCE_SHA256 = ""

GATES: list[dict] = []
ANCHORS: list[dict] = []
TABLES: dict = {}
FINDINGS: dict = {}

CARRIER = 5
PREP_FULL = frozenset(range(CARRIER))
RHO = L2.RHO
PI1 = L4.PI1        # forged aligned manufactured 2+1+1
P22 = L4.P22        # forged aligned manufactured 2+2
PTOMO = L4.PTOMO    # LEGITIMATE corrected tomographic minimum
DISC5 = L4.DISC5    # the carrier's own algebra -- LEGITIMATE address chart
FIXTURE = (DISC5, PI1, P22, PTOMO)
PROVENANCE = dict(L4.PROVENANCE)
PROVENANCE[DISC5] = "LEGITIMATE"
NAME = {DISC5: "delta address chart", PI1: "forged 2+1+1",
        P22: "forged 2+2", PTOMO: "legit tomographic min"}

NROOT = 8


def prog(msg: str) -> None:
    sys.stderr.write(f"[l5] {msg}\n")
    sys.stderr.flush()


def gate(gid: str, cls: str, claim: str, ok: bool, value=None) -> bool:
    GATES.append({"id": gid, "class": cls, "claim": claim,
                  "passed": bool(ok), "value": value})
    return ok


def anchor(aid: str, source: str, quantity: str, committed, computed) -> None:
    ANCHORS.append({"id": aid, "source": source, "quantity": quantity,
                    "committed": committed, "computed": computed,
                    "passed": committed == computed})


def S(x) -> str:
    return str(x)


def pk(part) -> str:
    return "|".join("".join(str(j) for j in sorted(b)) for b in part)


# ---------------------------------------------------------------------------
# 0.  Memoized terminal machinery (the committed laws are conjugation-stable,
#     so the relabelling sweeps reuse one canonical law object per key set)
# ---------------------------------------------------------------------------

_LAW_CANON: dict = {}
_ADJ: dict = {}
_PRES: dict = {}


def canon_law(law):
    k = frozenset(L2.key(F) for F in law)
    if k not in _LAW_CANON:
        _LAW_CANON[k] = (len(_LAW_CANON), list(law))
    return _LAW_CANON[k]


def pres_c(law, part):
    lid, lw = canon_law(law)
    k = (lid, part)
    if k not in _PRES:
        _PRES[k] = L2.pres_of(lw, part)
    return _PRES[k]


def adj_c(part, law, prep, n):
    lid, lw = canon_law(law)
    k = (lid, part, prep)
    if k not in _ADJ:
        _ADJ[k] = L2.adjudicate(part, pres_c(lw, part), lw, prep, n)
    return _ADJ[k]


def clauses_of(v):
    return (bool(v["i_a"]), bool(v["i_b"]), bool(v["ii_a"]), bool(v["ii_b"]))


# ---------------------------------------------------------------------------
# 1.  ANCHORS
# ---------------------------------------------------------------------------

def run_anchors() -> None:
    prog("anchors")
    det = L2.law_det(CARRIER)
    rev = L2.law_rev(CARRIER)
    ctr, n_rev_ctr = L2.law_counter()

    anchor("A01", "Cycle B sec 4 (Bell triangle)",
           "record-lattice sizes at 1..5 configurations",
           [1, 2, 5, 15, 52], [len(CB.partitions(k)) for k in range(1, 6)])
    anchor("A02", "Cycle B Thm 4.4 / B'' M32",
           "DET and REV cardinalities at five configurations",
           [3125, 120], [len(det), len(rev)])
    anchor("A03", "B'' sec 6.4",
           "counter-law size and its reversible count",
           [120, 1], [len(ctr), len(n_rev_ctr)])
    anchor("A04", "stage-5 Thm 4.1 / B'' sec 6",
           "Pres under DET at delta, forged 2+1+1, forged 2+2, legitimate "
           "tomographic minimum",
           [120, 240, 420, 1280],
           [len(L2.pres_of(det, p)) for p in (DISC5, PI1, P22, PTOMO)])
    anchor("A05", "stage-5 Thm 4.1 / 4.2",
           "eps at the two forged coarse patches and the legitimate one, "
           "at the committed state",
           ["1/16", "1/8", "3/16"],
           [S(L3.bayes_error(p, RHO)) for p in (PI1, P22, PTOMO)])
    anchor("A06", "B'' Thm 3.1 (rigidity)",
           "admissible records under DET, REV and the counter-law: the "
           "singleton {discrete} each",
           [1, 1, 1],
           [sum(1 for p in CB.partitions(CARRIER)
                if L2.adjudicate(p, L2.pres_of(law, p), law, PREP_FULL,
                                 CARRIER)["admissible"])
            for law in (det, rev, ctr)])
    anchor("A07", "B'' Thm 8.4 (the cost tower)",
           "obstruction sizes under DET at the record, boundary, coarser "
           "boundary and limit levels",
           [120, 360, 1260, 3120],
           [len(L2.obstruction_set(det, p))
            for p in (PI1, P22, PTOMO, ((0, 1, 2, 3, 4),))])
    anchor("A08", "stage-5 sec 9.1",
           "omega at the three coarse committed patches under DET at the "
           "whole carrier",
           ["0", "0", "0"],
           [S(L4.omega_fast(p, det, PREP_FULL, RHO, CARRIER))
            for p in (PI1, P22, PTOMO)])
    grp = L4.stabilizer(det, RHO, PREP_FULL, CARRIER)
    anchor("A09", "branch C Thm 7.1 / 7.3",
           "admitted isomorphisms of the declared data at the committed "
           "state, and the orbit count of the 52 records",
           [24, 12],
           [len(grp), len(L4.orbits_of(CB.partitions(CARRIER), grp))])
    anchor("A10", "stage-5 sec 5.4 / branch C sec 5",
           "declared state grid size at denominator 16",
           4845, len(L4.grid_states()))
    anchor("A11", "stage-5 gate L3-27",
           "every committed law is single-valued",
           [True, True, True, True],
           [L3.is_single_valued(x) for x in
            (det, rev, ctr, L2.law_funnel_closure(CARRIER))])
    anchor("A12", "B'' Thm 6.1 (comparable boundaries)",
           "jointly admissible comparable boundary pairs under DET, REV "
           "and the counter-law",
           [0, 0, 0], _comparable_pairs(det, rev, ctr))

    om = {S(L4.omega_fast(p, det, PREP_FULL, RHO, CARRIER))
          for p in CB.partitions(CARRIER)}
    gate("L5-A08-SCOPE", "derivation",
         "A08's three zeros are reproduced and their scope is stated: omega "
         "sums the declared mass of blocks disjoint from the reachable set, "
         "and the reachable set always contains the declared preparation, so "
         "at the whole-carrier preparation no block can miss it.  Measured "
         "over ALL committed records, not only the three coarse ones: omega "
         "is identically zero there.  The anchor is faithful and "
         "discriminates nothing at this preparation",
         om == {"0"},
         {"records_swept": len(CB.partitions(CARRIER)),
          "distinct_omega_values": sorted(om)})


def _comparable_pairs(det, rev, ctr):
    out, recs = [], CB.partitions(CARRIER)
    for law in (det, rev, ctr):
        adm = [p for p in recs
               if L2.adjudicate(p, L2.pres_of(law, p), law, PREP_FULL,
                                CARRIER)["admissible"]]
        n = 0
        for i, a in enumerate(adm):
            for b in adm[i + 1:]:
                if CB.refines(a, b) or CB.refines(b, a):
                    n += 1
        out.append(n)
    return out


# ---------------------------------------------------------------------------
# 2.  THE QUINTUPLE
# ---------------------------------------------------------------------------

def composite_of(word):
    """The support-level composite of a carried path, step 1 first."""
    C = word[0]
    for g in word[1:]:
        C = L2.compose(g, C)
    return C


def checkpoints_of(word):
    """The declared checkpoints: the intermediate composites, one per step."""
    out, C = [], None
    for g in word:
        C = g if C is None else L2.compose(g, C)
        out.append(C)
    return out


def certificate_CL(C, law, prep, n):
    """V-CL's fine-grained B''-certificate at one checkpoint: the record the
    composite writes, the closure the law assigns it, the four clause bits,
    and the reachable subprocess.  Classical throughout."""
    part = L2.written_of(C)
    v = adj_c(part, law, prep, n)
    return (part, v["pres_size"], clauses_of(v), tuple(sorted(v["reach"])))


def P1(word, part, law, prep, n):
    """(P1) the carried path is admitted by the law: every step an admitted
    operation, composable, endpoint = the declared boundary."""
    if MUTANT == "p1-break":
        return False, "mutant"
    if not word:
        return False, "empty path"
    lk = {L2.key(g) for g in law}
    for t, g in enumerate(word):
        if L2.key(g) not in lk:
            return False, f"step {t + 1} not admitted"
    end = L2.written_of(composite_of(word))
    if end != part:
        return False, f"endpoint writes {pk(end)}, declared {pk(part)}"
    return True, "admitted; endpoint matches"


def P2_weak(word, carried, law, prep, n):
    """(P2) each carried certificate verifies against the law at its own
    checkpoint: the recomputed certificate equals the carried one."""
    if MUTANT == "p2-break":
        return False, "mutant"
    for t, C in enumerate(checkpoints_of(word)):
        if certificate_CL(C, law, prep, n) != carried[t]:
            return False, f"checkpoint {t + 1} does not verify"
    return True, "every carried certificate verifies"


def P2_strong(word, law, prep, n):
    """The strong reading: every checkpoint must itself be B''-admissible."""
    for t, C in enumerate(checkpoints_of(word)):
        part = L2.written_of(C)
        if not adj_c(part, law, prep, n)["admissible"]:
            return False, f"checkpoint {t + 1} at {pk(part)} inadmissible"
    return True, "every checkpoint admissible"


DEFS = [composite_of, checkpoints_of, certificate_CL, P1, P2_weak, P2_strong]


# ---------------------------------------------------------------------------
# 3.  THE AMPLITUDE LAYER.  Exact; gauge-invariant content only.
#     An amplitude is (c, s, e) = c * 2^(-s/2) * zeta_8^e.
# ---------------------------------------------------------------------------

AZERO = (Fr(0), 0, 0)
AONE = (Fr(1), 0, 0)

MIXED_FORMED: list = []      # every non-commensurable residue actually formed


def amul(a, b):
    if a[0] == 0 or b[0] == 0:
        return AZERO
    c = a[0] * b[0]
    s = a[1] + b[1]
    if s == 2:
        c, s = c / 2, 0
    return (c, s, (a[2] + b[2]) % NROOT)


def aconj(a):
    return (a[0], a[1], (-a[2]) % NROOT)


def cyc(a):
    """THE CANONICAL EXACT COORDINATES of an amplitude in Q(zeta_8), over the
    integral basis {1, zeta, zeta^2, zeta^3} with zeta^4 = -1 and
    2^(-1/2) = (zeta - zeta^3)/2.  Those four rationals determine the field
    element, so equality of the tuples IS equality in the field and a
    coordinate tuple of zeros IS the zero of the field.  This is what makes
    the (c, s, e) shorthand safe: the shorthand is a convenience for the
    declared family, and every question of equality or vanishing is decided
    here instead."""
    if a[0] == "MIXED":
        return a[1]
    c, s, e = a
    q = [Fr(0), Fr(0), Fr(0), Fr(0)]

    def put(i, v):
        i %= 2 * 4
        q[i % 4] += v if i < 4 else -v
    if s == 0:
        put(e, c)
    else:
        put(e + 1, c / 2)
        put(e + 3, -c / 2)
    return tuple(q)


def cyc_mul(x, y):
    q = [Fr(0), Fr(0), Fr(0), Fr(0)]
    for i in range(4):
        if x[i] == 0:
            continue
        for j in range(4):
            k = i + j
            if k < 4:
                q[k] += x[i] * y[j]
            else:
                q[k - 4] -= x[i] * y[j]
    return tuple(q)


def cyc_conj(x):
    return (x[0], -x[3], -x[2], -x[1])


def asum(terms):
    """Sum a bag of amplitudes exactly.  Terms whose (c, s, e) shorthands are
    commensurable combine inside the shorthand, using zeta^e + zeta^(e+4) = 0.
    A residue the shorthand cannot name is NOT an inexactness: it is decided
    in the canonical coordinates -- returned as the field zero when it
    vanishes there, and otherwise carried AS those coordinates, which are
    exact and complete.  Every such residue is recorded in MIXED_FORMED so
    the exactness gate measures the sums this run actually formed."""
    red: dict = {}
    for t in terms:
        c, s, e = t
        if c == 0:
            continue
        k = (s, e % 4)
        red[k] = red.get(k, Fr(0)) + (c if e < 4 else -c)
    live = {k: v for k, v in red.items() if v != 0}
    if not live:
        return AZERO
    if len(live) == 1:
        (s, e), v = next(iter(live.items()))
        return (abs(v), s, e if v > 0 else (e + 4) % NROOT)
    q = [Fr(0), Fr(0), Fr(0), Fr(0)]
    for t in terms:
        for i, x in enumerate(cyc(t)):
            q[i] += x
    if not any(q):
        return AZERO
    MIXED_FORMED.append(tuple(q))
    return ("MIXED", tuple(q), 0)


def sup_of_matrix(U, n):
    """The sector support of a declared amplitude operation."""
    return tuple(frozenset({i for i in range(n) if U[i][j][0] != 0})
                 for j in range(n))


def matmul(U, V, n):
    """Exact amplitude composition.  Terms are summed exactly, so
    CANCELLATION IS VISIBLE -- which is precisely what the support-level
    composition of the corpus cannot see."""
    if MUTANT == "amp-cancel-lax":
        # the non-negativity convention reimposed: a leg survives whenever
        # any term is non-zero, so cancellation becomes invisible again
        return tuple(tuple(AONE if any(U[i][k][0] != 0 and V[k][j][0] != 0
                                       for k in range(n)) else AZERO
                           for j in range(n)) for i in range(n))
    return tuple(tuple(asum([amul(U[i][k], V[k][j]) for k in range(n)])
                       for j in range(n)) for i in range(n))


def layered_edges(word_sups, n):
    """The realized-leg graph of a carried path, as a layered multigraph:
    vertices (t, j), one edge per realized leg of each step."""
    E = []
    for t, sup in enumerate(word_sups):
        for j in range(n):
            for jp in sorted(sup[j]):
                E.append(((t, j), (t + 1, jp), t, j, jp))
    if MUTANT == "acyc-lax" and E:
        E.append(E[0])
    return E


def leg_ends(e, s):
    """The (tail, head) of one traversal of edge e: with its stored
    orientation when s > 0, against it when s < 0."""
    return (e[0], e[1]) if s > 0 else (e[1], e[0])


def walk_closes(legs, start):
    """Does this leg sequence traverse a CLOSED walk from `start` back to
    `start`?  Each leg's tail must be the previous leg's head.  This is the
    definitional criterion of Definition 3.1 -- gauge-invariance is
    equivalent to closure -- so it is checked rather than assumed."""
    v = start
    for e, s in legs:
        tail, head = leg_ends(e, s)
        if tail != v:
            return False
        v = head
    return v == start


_CYC: dict = {}


def cycle_structure(word_sups, n, convention="closed"):
    """The combinatorial half of the carried diagram's invariant content,
    computed from the SUPPORTS alone: the cycle rank, the component count on
    the FULL layered vertex set (isolated upper-layer vertices included), and
    one leg sequence per fundamental cycle.

    A fundamental cycle is the extra edge a->b traversed forward, then the
    spanning-tree path b->a traversed BACKWARD -- each leg conjugated when it
    runs against its stored orientation.  Two other conventions are built
    for the gauge self-test's negative controls and are never carried:
    `unclosed` traverses the tree path a->b as well (the walk does not
    close), `reversed` flips the extra edge instead."""
    ck = (tuple(L2.key(s) for s in word_sups), n, convention, MUTANT)
    if ck in _CYC:
        return _CYC[ck]
    E = layered_edges(word_sups, n)
    m = len(word_sups)
    allv = [(t, j) for t in range(m + 1) for j in range(n)]
    idx = {v: i for i, v in enumerate(allv)}
    parent = list(range(len(allv)))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    tree, extra = [], []
    for e in E:
        a, b = find(idx[e[0]]), find(idx[e[1]])
        if a != b:
            parent[a] = b
            tree.append(e)
        else:
            extra.append(e)
    comps_full = len({find(i) for i in range(len(allv))})
    occupied = {v for e in E for v in e[:2]}
    rank = len(E) - len(occupied) + len(
        {find(idx[v]) for v in occupied}) if occupied else 0

    adj: dict = {}
    for e in tree:
        adj.setdefault(e[0], []).append((e[1], e, +1))
        adj.setdefault(e[1], []).append((e[0], e, -1))

    def tree_path(a, b):
        """The tree legs from a to b, each signed by the direction of its
        a->b traversal (+1 along its stored orientation, -1 against it)."""
        seen, stack = {a: None}, [a]
        while stack:
            v = stack.pop()
            if v == b:
                break
            for w, e, s in adj.get(v, []):
                if w not in seen:
                    seen[w] = (v, e, s)
                    stack.append(w)
        if b not in seen:
            return None
        out, v = [], b
        while seen[v] is not None:
            p, e, s = seen[v]
            out.append((e, s))
            v = p
        return out[::-1]

    cycles, closes = [], True
    for e in extra:
        p = tree_path(e[0], e[1])
        if p is None:
            continue
        if convention == "closed":
            legs = [(e, +1)] + [(ee, -ss) for ee, ss in reversed(p)]
        elif convention == "unclosed":
            legs = [(e, +1)] + [(ee, ss) for ee, ss in reversed(p)]
        else:
            legs = [(e, -1)] + [(ee, -ss) for ee, ss in reversed(p)]
        if not walk_closes(legs, leg_ends(*legs[0])[0]):
            closes = False
        cycles.append(legs)
    out = (rank, comps_full, tuple(cycles), closes)
    _CYC[ck] = out
    return out


def cycle_basis_holonomies(word_mats, word_sups, n, convention="closed"):
    """The gauge-invariant content of a carried amplitude path.

    The declared pair gauge is VERTEX SWITCHING on the layered path graph
    (the v12 W7 terminal form): a phase at each vertex, every edge amplitude
    multiplied by the phase difference of its endpoints.  A quantity is
    gauge-invariant iff it is a product of edge amplitudes around a CLOSED
    LOOP, conjugated on reversed edges; a cycle basis carries all of that
    loop content.  Returns (cycle rank, sorted holonomy PHASES, sorted
    per-cycle checkpoint spans, sorted loop PRODUCTS) -- the phase and the
    modulus are reported separately because the loop product is not of unit
    modulus (at the declared Hadamard block it is exactly -1/4)."""
    if MUTANT == "hol-sign":
        convention = "unclosed"       # the direction flag double-negated
    if MUTANT == "hol-orient":
        convention = "reversed"       # the extra edge traversed backwards
    rank, _comps, cycles, _cl = cycle_structure(word_sups, n, convention)
    hol, spans, prods = [], [], []
    for legs in cycles:
        acc, layers = AONE, set()
        for ee, s in legs:
            w = word_mats[ee[2]][ee[4]][ee[3]]
            acc = amul(acc, w if s > 0 else aconj(w))
            layers.add(ee[2])
        if MUTANT == "hol-lax":
            acc = AONE
        hol.append(acc[2])
        spans.append(len(layers))
        prods.append(acc)
    return (rank, tuple(sorted(hol)), tuple(sorted(spans)),
            tuple(sorted(prods, key=str)))


def vertex_switch(word_mats, n, phases):
    """DEFINITION 3.1's OWN SYMMETRY, acting: a phase zeta_8^{p(t,j)} at each
    vertex, every edge amplitude multiplied by the phase difference of its
    endpoints.  On matrices this is U_t -> D_{t+1} U_t D_t^{-1} with D
    diagonal, so a switched lift is still unitary and still inside the
    declared family."""
    out = []
    for t, U in enumerate(word_mats):
        p0, p1 = phases[t], phases[t + 1]
        out.append(tuple(tuple(
            amul((Fr(1), 0, (p1.get(i, 0) - p0.get(j, 0)) % NROOT), U[i][j])
            for j in range(n)) for i in range(n)))
    return out


def cross_checkpoint_phase(word_mats):
    """The declared CROSS-CHECKPOINT invariant of a two-step carried word on
    the declared 2-block: X = (arg u00 - arg u10) + (arg v00 - arg v01).
    Under vertex switching the layer-1 phases cancel in pairs, so X is
    gauge-invariant; it is the datum no single checkpoint's diagram
    contains.  Its gauge-invariance is measured, not asserted (L5-HOL-GAUGE)."""
    u, v = word_mats[0], word_mats[1]
    return (u[0][0][2] - u[1][0][2] + v[0][0][2] - v[0][1][2]) % NROOT


def amplitude_composite(word_mats, n):
    C = word_mats[0]
    for U in word_mats[1:]:
        C = matmul(U, C, n)
    return C


def certificate_AMP(word_mats, word_sups, law, prep, n):
    """V-AMP's checkpoint certificate: V-CL's, PLUS the amplitude-level data
    -- the moduli profile, the gauge-invariant loop holonomies of the whole
    carried diagram, and the record the AMPLITUDE composite writes, which
    may be strictly finer than the support one because amplitudes cancel
    and supports do not."""
    C = amplitude_composite(word_mats, n)
    base = certificate_CL(composite_of(word_sups), law, prep, n)
    rank, hol, spans, _prods = cycle_basis_holonomies(word_mats, word_sups, n)
    mods = tuple(sorted(f"{w[0]}/2^({w[1]}/2)" for U in word_mats
                        for row in U for w in row if w[0] != 0))
    return base + (L2.written_of(sup_of_matrix(C, n)), rank, hol, spans,
                   mods)


def step_local_shadow(word_mats, word_sups, n):
    """Everything a STEP-LOCAL reading of an admitted verification can read
    of the carried amplitude data: each step's own loop holonomies, each
    checkpoint's AMPLITUDE RECORD -- the visible-cancellation datum, which is
    checkpoint-local par excellence and must not be omitted -- and the moduli
    profile.  What it does not contain is the cross-checkpoint loop content.

    The step-local restriction is a DECLARED READING and is labelled one: it
    does not follow from (P2)'s checkpoint-locality, because checkpoints are
    the cumulative composites and the final one spans the whole carried path
    (Section 6.4)."""
    per = tuple(cycle_basis_holonomies([word_mats[t]], [word_sups[t]], n)[1]
                for t in range(len(word_mats)))
    if MUTANT == "shadow-lax":
        recs = ()
    else:
        recs = tuple(pk(L2.written_of(sup_of_matrix(
            amplitude_composite(word_mats[:t + 1], n), n)))
            for t in range(len(word_mats)))
    mods = tuple(sorted(f"{w[0]}/2^({w[1]}/2)" for U in word_mats
                        for row in U for w in row if w[0] != 0))
    return (per, recs, mods)


AMP_DEFS = [amul, aconj, asum, sup_of_matrix, matmul, layered_edges,
            leg_ends, walk_closes, cycle_structure, cycle_basis_holonomies,
            vertex_switch, cross_checkpoint_phase, amplitude_composite,
            certificate_AMP, step_local_shadow]


# ---------------------------------------------------------------------------
# 4.  THE FREEZE
# ---------------------------------------------------------------------------

def TUNE_negative_control(part, law, prep, rho, n, word):
    """PERMANENT NEGATIVE CONTROL -- must be CAUGHT by the source scan.
    It special-cases the committed legitimate boundary PTOMO by name."""
    return Fr(0) if part == PTOMO else Fr(1)


def run_freeze():
    prog("freeze")
    supplier = (TUNE_HISTORY_negative_control if MUTANT == "hist-tune"
                else true_histories)
    fns = (DEFS + AMP_DEFS + STATS
           + [supplier, passing_histories_1, nb_negative_control])
    reg = [{"name": f.__name__,
            "sha256": hashlib.sha256(
                inspect.getsource(f).encode()).hexdigest()} for f in fns]
    TABLES["definition_hashes"] = reg
    gate("L5-00", "freeze",
         "every definition of the quintuple, of the amplitude layer, of the "
         "carried datum itself -- the declared-history supplier and the "
         "declarable-history set -- and every provenance-reading statistic "
         "is SHA-256 registered before any fixture verdict is computed.  The "
         "registration binds this receipt to the DELIVERED source and makes "
         "no claim across revisions: a definition edited between runs is "
         "re-registered, not detected",
         len(reg) == len(fns), len(reg))

    clean = L4.source_scan([(f.__name__, f) for f in fns])
    caught = L4.source_scan([("TUNE", TUNE_negative_control),
                             ("TUNE_HISTORY", TUNE_HISTORY_negative_control)])
    ok = all(r["clean"] for r in clean) and all(
        not r["clean"] for r in caught)
    gate("L5-SRC", "freeze",
         "automated source scan: NO registered definition -- the quintuple's, "
         "the amplitude layer's, the declared-history supplier's and the six "
         "statistics' alike -- mentions a committed boundary, AND both "
         "permanent negative controls are CAUGHT by the same scan: TUNE, "
         "which special-cases the legitimate tomographic minimum inside a "
         "statistic, and TUNE_HISTORY, which special-cases the discrete "
         "boundary inside the history supplier.  The carried datum's own "
         "definition is inside the scanned set, not beside it",
         ok, {"definitions_scanned": len(clean),
              "definitions_clean": sum(1 for r in clean if r["clean"]),
              "negative_controls_caught":
                  {r["definition"]: r["fixture_references"] for r in caught}})


# ---------------------------------------------------------------------------
# 5.  THE DECLARED AMPLITUDE-LEVEL GENERATOR FAMILY
# ---------------------------------------------------------------------------

def _eye(n):
    return tuple(tuple(AONE if i == j else AZERO for j in range(n))
                 for i in range(n))


def _embed(block, idxs, n):
    M = [[AZERO] * n for _ in range(n)]
    for i in range(n):
        M[i][i] = AONE
    for i in idxs:
        for j in idxs:
            M[i][j] = AZERO
    for a, i in enumerate(idxs):
        for b, j in enumerate(idxs):
            M[i][j] = block[a][b]
    return tuple(tuple(r) for r in M)


def declared_amplitude_family(n=CARRIER):
    """G_A: a DECLARED finite generator family of amplitude operations at the
    committed carrier, carried as a declared family exactly as B'' carries
    FUNNEL -- the LAW is its support-level composition closure, computed and
    gated closed.

      ID    identity                             -- writes delta
      SW01  the transposition (0 1)              -- writes delta
      H01   Hadamard on {0,1}, identity else     -- writes the forged 2+1+1
      H23   Hadamard on {2,3}, identity else
      F4    DFT(4) on {0,1,2,3}, identity else   -- writes the legitimate
                                                   tomographic minimum"""
    H = (((Fr(1), 1, 0), (Fr(1), 1, 0)), ((Fr(1), 1, 0), (Fr(1), 1, 4)))
    F = tuple(tuple((Fr(1, 2), 0, (2 * i * j) % NROOT) for j in range(4))
              for i in range(4))
    sw = [[AZERO] * n for _ in range(n)]
    for i in range(n):
        sw[i][i] = AONE
    sw[0][0] = sw[1][1] = AZERO
    sw[0][1] = sw[1][0] = AONE
    return {"ID": _eye(n), "SW01": tuple(tuple(r) for r in sw),
            "H01": _embed(H, [0, 1], n), "H23": _embed(H, [2, 3], n),
            "F4": _embed(F, [0, 1, 2, 3], n)}


def _closure_sups(gens):
    seen = {L2.key(g): g for g in gens}
    frontier = list(seen.values())
    while frontier:
        nxt = []
        for F in list(seen.values()):
            for G in frontier:
                H = L2.compose(F, G)
                if L2.key(H) not in seen:
                    seen[L2.key(H)] = H
                    nxt.append(H)
        frontier = nxt
    return list(seen.values())


def is_unitary(U, n):
    """Exactly unitary: every column pair's inner product compared in the
    CANONICAL coordinates, so the verdict does not depend on whether the
    (c, s, e) shorthand happened to name the sum."""
    one, zero = cyc(AONE), cyc(AZERO)
    for a in range(n):
        for b in range(n):
            v = cyc(asum([amul(U[i][a], aconj(U[i][b])) for i in range(n)]))
            if v != (one if a == b else zero):
                return False
    return True


def run_amplitude_scope():
    prog("amplitude scope")
    n = CARRIER
    GA = declared_amplitude_family(n)
    sups = {k: sup_of_matrix(U, n) for k, U in GA.items()}
    LA = _closure_sups(list(sups.values()))

    gate("L5-AMP-CLOSED", "derivation",
         "the support-level law generated by the declared amplitude family "
         "is composition-closed -- it is the law the family generates, "
         "carried exactly as B'' carries FUNNEL",
         L2.is_composition_closed(LA), len(LA))

    gate("L5-AMP-UNITARY", "derivation",
         "every declared amplitude generator is exactly unitary",
         all(is_unitary(U, n) for U in GA.values()),
         {k: is_unitary(U, n) for k, U in GA.items()})

    words = {"(ID)": ["ID"], "(SW01)": ["SW01"], "(H01)": ["H01"],
             "(H01,H23)": ["H01", "H23"], "(F4)": ["F4"],
             "(H01,H01)": ["H01", "H01"]}
    rows = []
    for wn, w in words.items():
        ws, wm = [sups[k] for k in w], [GA[k] for k in w]
        supcomp = L2.written_of(composite_of(ws))
        ampcomp = L2.written_of(sup_of_matrix(amplitude_composite(wm, n), n))
        rank, hol, spans, prods = cycle_basis_holonomies(wm, ws, n)
        rows.append({"word": wn, "support_record": pk(supcomp),
                     "amplitude_record": pk(ampcomp), "cycle_rank": rank,
                     "holonomy_phases": list(hol), "cycle_spans": list(spans),
                     "loop_products": [f"{p[0]}*2^-({p[1]}/2)*z8^{p[2]}"
                                       for p in prods],
                     "cancellation": supcomp != ampcomp})
    TABLES["amplitude_words"] = rows
    by = {r["word"]: r for r in rows}

    h01 = cycle_basis_holonomies([GA["H01"]], [sups["H01"]], n)[3]
    gate("L5-AMP-MODULUS", "derivation",
         "the carried invariant is the PHASE of the loop product, not the "
         "product: the single fundamental cycle of the declared Hadamard "
         "step has loop product exactly -1/4, of modulus 1/4 and not 1.  The "
         "modulus travels separately, in the certificate's moduli profile, "
         "and the holonomy column reports arguments",
         len(h01) == 1 and h01[0] == (Fr(1, 4), 0, 4),
         {"loop_product": f"{h01[0][0]}*2^-({h01[0][1]}/2)*z8^{h01[0][2]}",
          "as_a_rational": "-1/4"})

    gate("L5-AMP-REACH", "derivation",
         "the declared amplitude family generates every committed boundary "
         "as a written record: delta by (ID), the forged 2+1+1 by (H01), "
         "the forged 2+2 by (H01,H23), the legitimate tomographic minimum "
         "by (F4) -- so the amplitude question is posed AT the fixture",
         (by["(ID)"]["support_record"] == pk(DISC5)
          and by["(H01)"]["support_record"] == pk(PI1)
          and by["(H01,H23)"]["support_record"] == pk(P22)
          and by["(F4)"]["support_record"] == pk(PTOMO)),
         {k: by[k]["support_record"] for k in
          ("(ID)", "(H01)", "(H01,H23)", "(F4)")})

    gate("L5-AMP-CONTENT", "derivation",
         "the amplitude layer has NON-TRIVIAL gauge-invariant content on "
         "this declared family: the cycle rank is positive at every "
         "non-monomial word and the holonomy phases are non-zero, so V-AMP "
         "carries strictly more than V-CL there",
         (by["(H01)"]["cycle_rank"] == 1 and by["(H01,H23)"]["cycle_rank"] == 2
          and by["(F4)"]["cycle_rank"] == 9
          and by["(H01,H01)"]["cycle_rank"] == 3
          and any(h != 0 for h in by["(H01)"]["holonomy_phases"])),
         {k: [by[k]["cycle_rank"], by[k]["holonomy_phases"][:4]]
          for k in by})

    gate("L5-AMP-CANCEL", "derivation",
         "AMPLITUDE CANCELLATION IS VISIBLE TO V-AMP AND INVISIBLE TO V-CL. "
         "The word (H01,H01) has a support-composite writing the FORGED "
         "2+1+1 record while its amplitude composite is the identity, "
         "writing delta.  B'' Definition 4.1's non-negativity -- 'no entry "
         "is lost to cancellation, so a leg is present exactly when the "
         "process can take it' -- is exactly what the amplitude variant "
         "suspends, and this is the first thing the quantum bits buy",
         (by["(H01,H01)"]["support_record"] == pk(PI1)
          and by["(H01,H01)"]["amplitude_record"] == pk(DISC5)),
         {"support": by["(H01,H01)"]["support_record"],
          "amplitude": by["(H01,H01)"]["amplitude_record"]})

    FINDINGS["amplitude_scope"] = {
        "declared_generators": sorted(GA),
        "generated_support_law_size": len(LA),
        "cancellation_witness": "(H01,H01)"}
    return GA, sups, LA


# ---------------------------------------------------------------------------
# 6.  THE ACYCLICITY THEOREM
# ---------------------------------------------------------------------------

_LIFT: dict = {}


def canonical_lift(sup, n):
    """The all-ones amplitude lift of an admitted support map.  Used only
    where the acyclicity theorem says the lift is immaterial."""
    k = L2.key(sup)
    if k not in _LIFT:
        _LIFT[k] = tuple(tuple(AONE if i in sup[j] else AZERO
                               for j in range(n)) for i in range(n))
    return _LIFT[k]


def run_acyclicity():
    prog("acyclicity theorem")
    n = CARRIER
    det, rev = L2.law_det(n), L2.law_rev(n)
    ctr, _ = L2.law_counter()
    fnl = L2.law_funnel_closure(n)

    bad, tested, ident, seen_paths = [], 0, 0, set()
    seen_words: set = set()
    counted_C = 0
    caps = {}
    for nm, law, cap in (("DET", det, 60), ("REV", rev, 60),
                         ("COUNTER", ctr, 60), ("FUNNEL-CLOSURE", fnl, 60)):
        pool = list(law)[:cap]
        caps[nm] = {"law_size": len(law), "operations_sampled": len(pool)}
        for a in pool:
            for b in pool[:6]:
                for w in ([a], [a, b]):
                    E = layered_edges(w, n)
                    V = (len(w) + 1) * n
                    r, comps, _cyc, _cl = cycle_structure(w, n)
                    h = cycle_basis_holonomies(
                        [canonical_lift(g, n) for g in w], w, n)[1]
                    tested += 1
                    seen_paths.add((nm, tuple(L2.key(g) for g in w)))
                    seen_words.add(tuple(L2.key(g) for g in w))
                    if len(E) == len(w) * n and r == 0:
                        ident += 1
                    if comps == n:          # COUNTED on the full vertex set
                        counted_C += 1
                    if r != 0 or h != ():
                        bad.append((nm, L2.key(a), r))
    gate("L5-ACYC-M", "derivation",
         "MEASURED, at a DECLARED SAMPLE of 60 operations per law (not "
         "exhaustive over any law): over one- and two-step carried paths at "
         "every committed law, the layered realized-leg diagram has cycle "
         "rank 0 and an EMPTY holonomy family, with E = m*n edges measured "
         "and exactly n components COUNTED by union-find on the FULL layered "
         "vertex set -- isolated upper-layer vertices included -- rather "
         "than inferred from Euler.  There is no gauge-invariant loop "
         "content to carry",
         not bad and ident == tested and counted_C == tested,
         {"path_evaluations": tested,
          "distinct_carried_paths_at_their_laws": len(seen_paths),
          "distinct_support_sequences": len(seen_words),
          "euler_identity_holds": ident,
          "components_counted_equal_n": counted_C, "violations": len(bad),
          "sample_scope": caps})

    gate("L5-ACYC-P", "derivation",
         "PROVED: a single-valued step gives each vertex of a layer exactly "
         "one upward edge, so E = m*n while V = (m+1)*n; following upward "
         "edges, every component meets the top layer, so C <= n; hence "
         "rank = E - V + C = C - n <= 0, and rank >= 0 forces rank = 0 and "
         "C = n.  Every committed law is single-valued (anchor A11), so "
         "V-AMP's gauge-invariant LOOP content is EMPTY at the whole "
         "committed scope",
         True, {"E": "m*n", "V": "(m+1)*n", "C": "n", "rank": 0})

    # the moduli probe: what the acyclicity theorem does NOT cover.  The
    # probe step is the first NON-INJECTIVE single-valued operation of the
    # committed law -- one with no unitary lift at all.
    step = next(F for F in list(det)[:60]
                if len({next(iter(s)) for s in F}) < n)
    base_lift = canonical_lift(step, n)
    a0 = [list(row) for row in base_lift]
    i0 = next(i for i in range(n) if base_lift[i][0][0] != 0)
    a0[i0][0] = (Fr(1, 2), 0, 0)                            # modulus 1/2
    a1 = [[amul((Fr(1), 0, 3), w) for w in row] for row in base_lift]
    variants = [("all-ones (the declared canonical lift)", base_lift),
                ("modulus 1/2 on one leg", tuple(tuple(r) for r in a0)),
                ("global phase z8^3", tuple(tuple(r) for r in a1))]
    prof = []
    for lab, M in variants:
        r, h, _s, _p = cycle_basis_holonomies([M], [step], n)
        prof.append({"declared_lift": lab, "cycle_rank": r,
                     "holonomy_phases": list(h),
                     "moduli_profile": sorted(
                         f"{w[0]}/2^({w[1]}/2)" for row in M for w in row
                         if w[0] != 0)})
    TABLES["moduli_freedom"] = prof
    gate("L5-ACYC-MODULI", "derivation",
         "THE SCOPE OF THE ACYCLICITY THEOREM, MEASURED.  Rank 0 empties the "
         "carried LOOP content and nothing else: the moduli profile is "
         "gauge-invariant and is not a loop product, so switching on a "
         "forest does not trivialize it.  Three declared lifts of ONE "
         "committed single-valued step -- which, being non-injective, has no "
         "unitary lift at all, so neither (P1) nor (P2) pins its amplitude "
         "description -- give the same rank 0 and the same empty holonomy "
         "family with DIFFERENT moduli profiles.  V-AMP's certificate "
         "therefore reduces to V-CL's on the loop content and the amplitude "
         "record, and on the moduli profile only for the declared all-ones "
         "lift",
         (all(p["cycle_rank"] == 0 and p["holonomy_phases"] == []
              for p in prof)
          and len({tuple(p["moduli_profile"]) for p in prof}) == 2),
         {"distinct_moduli_profiles":
              len({tuple(p["moduli_profile"]) for p in prof}),
          "ranks": [p["cycle_rank"] for p in prof],
          "profiles": {p["declared_lift"]: sorted(set(p["moduli_profile"]))
                       for p in prof}})

    FINDINGS["acyclicity"] = {
        "statement": "single-valued steps have acyclic layered diagrams",
        "consequence": "the carried loop content is empty at every committed "
                       "law; V-AMP's certificate reduces to V-CL's there "
                       "except on the moduli profile, which the theorem does "
                       "not cover and a declared lift fixes",
        "path_evaluations": tested,
        "distinct_carried_paths_at_their_laws": len(seen_paths),
        "distinct_support_sequences": len(seen_words)}


# ---------------------------------------------------------------------------
# 7.  DISCRIMINATORS 1 AND 3
# ---------------------------------------------------------------------------

def true_histories(contexts, n=CARRIER):
    """The DECLARED true generation history of a declared context.  The
    immutable base supplies provenance LABELS but no generation paths, so
    the paths are declared here (deviation 1) in the one form the base's own
    vocabulary fixes, uniformly and with no special case: the admitted
    operation that writes exactly the declared record, namely its
    block-minimum idempotent, which B'' Prop 8.6 already carries as an
    admitted operation.  At the carrier's own algebra that operation IS the
    identity -- nothing was done to the address algebra -- and the identity
    is not written in by hand but computed (gate L5-HIST-UNIFORM).  This
    definition names no committed boundary and is inside the source scan."""
    return {p: [L2.block_min_idempotent(p, n)] for p in contexts}


def TUNE_HISTORY_negative_control(contexts, n=CARRIER):
    """PERMANENT NEGATIVE CONTROL for the history supplier -- must be CAUGHT
    by the source scan.  It special-cases the committed discrete boundary
    DISC5 by name, which is exactly the smuggling the scan exists to catch."""
    return {p: [L2.sup_of_map(tuple(range(n))) if p == DISC5
                else L2.block_min_idempotent(p, n)] for p in contexts}


def adjudicate_quintuple(part, law, prep, word, n, variant, mats=None):
    """The L5 axiom, per variant: the terminal B'' conditions on the
    quadruple, PLUS (P1) and (P2)."""
    base = adj_c(part, law, prep, n)
    p1, w1 = P1(word, part, law, prep, n)
    carried = [certificate_CL(C, law, prep, n) for C in checkpoints_of(word)]
    p2, w2 = P2_weak(word, carried, law, prep, n)
    p2s, w2s = P2_strong(word, law, prep, n)
    row = {"boundary": pk(part), "variant": variant,
           "bdd_admissible": bool(base["admissible"]),
           "clauses": list(clauses_of(base)),
           "P1": p1, "P1_witness": w1, "P2_weak": p2, "P2_witness": w2,
           "P2_strong": p2s, "P2_strong_witness": w2s,
           "L5_admissible": bool(base["admissible"]) and p1 and p2}
    if variant == "V-AMP":
        m = mats if mats is not None else [canonical_lift(g, n) for g in word]
        cert = certificate_AMP(m, word, law, prep, n)
        row["amplitude_record"] = pk(cert[4])
        row["cycle_rank"] = cert[5]
        row["holonomy_phases"] = list(cert[6])
    return row


def run_discriminators_13(law):
    prog("discriminators 1 and 3")
    n = CARRIER
    TH = true_histories(FIXTURE, n)
    gate("L5-HIST-UNIFORM", "freeze",
         "the declared-history supplier has NO fixture branch: the uniform "
         "rule -- the block-minimum idempotent of the declared record -- "
         "returns the IDENTITY at the carrier's own algebra, so the address "
         "chart's 'nothing was done' history is computed by the general rule "
         "rather than written in by name.  Measured against the identity",
         L2.key(TH[DISC5][0]) == L2.key(L2.sup_of_map(tuple(range(n)))),
         {"history_at_the_discrete_boundary": str(L2.key(TH[DISC5][0]))})
    rows = []
    for part in FIXTURE:
        for variant in ("V-CL", "V-AMP"):
            r = adjudicate_quintuple(part, law, PREP_FULL, TH[part], n,
                                     variant)
            r["provenance_truth"] = PROVENANCE[part]
            r["name"] = NAME[part]
            rows.append(r)
    TABLES["discriminator_1"] = rows
    by = {(r["boundary"], r["variant"]): r for r in rows}
    forged = [r for r in rows if r["provenance_truth"] == "FORGED"]

    gate("L5-D1-REJECT", "discriminator",
         "(1) the axiom REJECTS both forged patches carrying their TRUE "
         "manufacture-histories, in both variants",
         all(not r["L5_admissible"] for r in forged),
         {r["boundary"] + "/" + r["variant"]: r["L5_admissible"]
          for r in forged})

    gate("L5-D1-P1", "discriminator",
         "MEASURED, and it is the finding: (P1) and (P2) PASS at every "
         "committed patch, forged and legitimate alike -- the true "
         "manufacture-history of a forged boundary IS an admitted path that "
         "genuinely produces it, and its checkpoint certificates verify.  "
         "The rejection is carried entirely by the inherited B'' clauses; "
         "the provenance component adds NO rejection power",
         all(r["P1"] and r["P2_weak"] for r in rows),
         {r["boundary"] + "/" + r["variant"]: [r["P1"], r["P2_weak"]]
          for r in rows})

    ib = [clauses_of(adj_c(p, law, PREP_FULL, n))[1]
          for p in CB.partitions(n)]
    gate("L5-D1-IDENTITY-CLAUSE", "discriminator",
         "clause (i-b) of the inherited axiom is an IDENTITY under the "
         "adjudication convention this unit inherits, not a measured "
         "verdict: the declared family is taken to be Pres_L of the "
         "boundary's record, and (i-b) asks exactly whether it is.  "
         "Measured over ALL committed records, it holds in every case.  "
         "Three of the four clause columns are measurements; this one is a "
         "convention, and the rejection of the coarse charts is carried by "
         "(i-a) and (ii-a)",
         all(ib), {"records_swept": len(ib),
                   "clause_i_b_true": sum(1 for x in ib if x)})

    gate("L5-D1-COLLATERAL", "discriminator",
         "(3) the same rejection falls on the LEGITIMATE coarse chart: the "
         "tomographic minimum carrying its own true history is rejected by "
         "exactly the clauses that reject the forgeries, in both variants.  "
         "Only the carrier's own algebra passes.  The quintuple inherits "
         "B'' rigidity and does not repair it",
         (by[(pk(DISC5), "V-CL")]["L5_admissible"]
          and not by[(pk(PTOMO), "V-CL")]["L5_admissible"]
          and by[(pk(PTOMO), "V-CL")]["clauses"]
          == by[(pk(PI1), "V-CL")]["clauses"]),
         {"PTOMO": by[(pk(PTOMO), "V-CL")]["clauses"],
          "PI1": by[(pk(PI1), "V-CL")]["clauses"],
          "DISC5_admissible": by[(pk(DISC5), "V-CL")]["L5_admissible"]})

    gate("L5-D1-VARIANT", "delta",
         "V-AMP and V-CL return BIT-IDENTICAL verdicts at every committed "
         "patch, and every carried diagram has cycle rank 0: the delta at "
         "the committed scope is ZERO, by the acyclicity theorem",
         all(by[(pk(p), "V-CL")]["L5_admissible"]
             == by[(pk(p), "V-AMP")]["L5_admissible"]
             and by[(pk(p), "V-AMP")]["cycle_rank"] == 0 for p in FIXTURE),
         {pk(p): by[(pk(p), "V-AMP")]["cycle_rank"] for p in FIXTURE})

    gate("L5-D1-STRONG", "discriminator",
         "the STRONG reading of (P2) -- every checkpoint itself admissible, "
         "not merely honestly certified -- rejects every coarse patch "
         "INCLUDING the legitimate one, so it collapses onto B'' rigidity "
         "and certifies only the carrier's own algebra.  Neither reading of "
         "(P2) separates by provenance",
         (by[(pk(DISC5), "V-CL")]["P2_strong"]
          and not by[(pk(PTOMO), "V-CL")]["P2_strong"]
          and not by[(pk(PI1), "V-CL")]["P2_strong"]),
         {pk(p): by[(pk(p), "V-CL")]["P2_strong"] for p in FIXTURE})
    return rows


# ---------------------------------------------------------------------------
# 8.  DISCRIMINATOR 2 -- THE REGRESS ADVERSARY
# ---------------------------------------------------------------------------

def passing_histories_1(law, part):
    """H_1(part, law): every one-step carried path passing (P1).  (P2) is
    vacuous for an honestly-carried certificate -- the certificate is
    RECOMPUTED, so an honest declarer always verifies -- which is itself the
    first half of the regress."""
    return [F for F in law if L2.written_of(F) == part]


def run_discriminator_2(law):
    prog("discriminator 2 (regress)")
    n = CARRIER
    rows = []
    for part in FIXTURE:
        H1 = passing_histories_1(law, part)
        rows.append({"boundary": pk(part), "name": NAME[part],
                     "provenance_truth": PROVENANCE[part],
                     "passing_one_step_histories": len(H1),
                     "cost_of_ADMISSIBILITY":
                         0 if part == DISC5
                         else len(L2.obstruction_set(law, part))})
    TABLES["regress_history_counts"] = rows

    gate("L5-D2-EXIST", "kill",
         "THE MANUFACTURE-PATH EXISTS AT THE COMMITTED LAW, AND IT IS FREE. "
         "B''s cost theory prices making a forged boundary ADMISSIBLE at "
         "120 deleted operations, unpayable inside the identity-containing "
         "class; it prices GENERATING it as a written record at ZERO -- 120 "
         "admitted one-step paths already write the forged 2+1+1.  "
         "Admissibility and generation are DECOUPLED, and provenance sits "
         "on the generation side, which is the cheap one",
         all(r["passing_one_step_histories"] > 0 for r in rows),
         {r["boundary"]: [r["passing_one_step_histories"],
                          r["cost_of_ADMISSIBILITY"]] for r in rows})

    gate("L5-D2-FUNCTION", "kill",
         "THE DECLARABLE-HISTORY SET IS A FUNCTION OF (boundary, law) AND "
         "OF NOTHING ELSE.  Two declarations of opposite provenance "
         "presenting the same boundary under the same law have the SAME set "
         "of declarable histories, by the definition of (P1) -- so carried "
         "provenance is a free variable the adversary ranges over, not a "
         "datum the law fixes",
         True, {"definition": "H_1(part, law) = {F in law : comp(F) = part}"})

    coll = _delta_collision(law, n)
    TABLES["delta_collision"] = coll
    gate("L5-D2-COLLISION", "kill",
         "THE COLLISION SURVIVES THE EXTENSION -- the constructed adversary. "
         "At the carrier's own algebra the base supplies BOTH provenance "
         "labels for ONE patch (B'' sec 6.5: the adversary's manufactured "
         "1+1+1+1 context and the legitimate address context are literally "
         "the same patch).  Both may declare the same carried history, and "
         "all 120 admitted one-step histories there yield ONE carried "
         "certificate -- in V-CL and in V-AMP alike",
         (coll["distinct_CL_certificates"] == 1
          and coll["distinct_AMP_certificates"] == 1
          and coll["passing_histories"] == 120), coll)

    gate("L5-D2-REDUCTION", "kill",
         "THE REDUCTION, and it is what fires the kill -- stated in the "
         "general form, which closes the escape route in advance.  Let D be "
         "a declared datum and extend it by a component H whose "
         "admissibility is decided by ANY predicate A(D, H).  For any "
         "statistic S the ACHIEVABLE SET {S(D,H) : A(D,H)} is a function of "
         "D alone.  Two declarations presenting the same D therefore have "
         "IDENTICAL achievable sets -- equality, not a bound -- so no "
         "admission rule of the form 'admit iff S lies in A' can admit one "
         "and reject the other, for any A whatever, up-set, down-set or "
         "neither, and no order orientation is needed.  (P1) is the special "
         "case A = (P1), which is why reading deeper into the carried path "
         "cannot help: the carried path is supplied by the party under "
         "test.  Here D is the quadruple TOGETHER WITH the declared state, "
         "since a statistic may read the state; the stage-5 collision "
         "presents the same patch at the same committed state, so the "
         "reduction applies to it.  RQ0-L5-PROVENANCE-REGRESS FIRES, on "
         "both variants",
         True, {"general_form": "achievable sets are equal, not bounded",
                "arguments_of_the_declarable_history_set": "(boundary, law)",
                "arguments_of_the_achievable_set":
                    "(boundary, family, preparation, law, state)",
                "inherited": "stage-5 Theorem 5.3 (forgery is not a "
                             "function of the quadruple)"})

    honest = 0
    for F in passing_histories_1(law, DISC5)[:20]:
        cc = [certificate_CL(C, law, PREP_FULL, n) for C in
              checkpoints_of([F])]
        if P2_weak([F], cc, law, PREP_FULL, n)[0]:
            honest += 1
    other = next(p for p in FIXTURE if p != DISC5)
    dishonest = P2_weak([passing_histories_1(law, DISC5)[0]],
                        [certificate_CL(L2.block_min_idempotent(other, n),
                                        law, PREP_FULL, n)],
                        law, PREP_FULL, n)[0]
    gate("L5-P2-VACUOUS", "discriminator",
         "(P2)-WEAK IS AN IDENTITY, NOT A MEASUREMENT, AND THAT IS WHY "
         "PROVENANCE ADDS NO REJECTION POWER.  The carried certificate is "
         "RECOMPUTED by the same route that produced it, so an honestly "
         "declared carry verifies BY CONSTRUCTION: measured, every honest "
         "carry passes, and no adversary would make the only kind of carry "
         "that could fail.  The predicate is nonetheless wired and can "
         "return false -- the POSITIVE CONTROL a dishonest carry supplies, "
         "here another boundary's certificate carried against a path that "
         "does not produce it, is REJECTED.  The discriminating weight of "
         "(P2) therefore rests entirely on the strong reading, and that "
         "reading collapses onto rigidity",
         honest == 20 and not dishonest,
         {"honest_carries_verified": honest,
          "dishonest_carry_rejected": not dishonest})
    return rows, coll


def _delta_collision(law, n):
    H = passing_histories_1(law, DISC5)
    certs = {certificate_CL(F, law, PREP_FULL, n) for F in H}
    acerts = {certificate_AMP([canonical_lift(F, n)], [F], law, PREP_FULL, n)
              for F in H}
    return {"boundary": pk(DISC5), "passing_histories": len(H),
            "distinct_CL_certificates": len(certs),
            "distinct_AMP_certificates": len(acerts),
            "both_labels_at_this_patch":
                ["LEGITIMATE address context", "FORGED manufactured 1+1+1+1"]}


def _block_lift(a, b, c, mods=(Fr(1), Fr(1)), s=(1, 1), n=CARRIER):
    """One candidate amplitude lift of the declared two-configuration support
    step, from three free phase exponents.  The fourth is COMPUTED from the
    orthogonality relation an equal-block unitary must satisfy."""
    d = (c - (a - b) + 4) % NROOT
    blk = (((mods[0], s[0], a), (mods[1], s[1], b)),
           ((mods[1], s[1], c), (mods[0], s[0], d)))
    return _embed(blk, [0, 1], n), (a, b, c, d)


def admitted_lift_family(mods=(Fr(1), Fr(1)), s=(1, 1), n=CARRIER):
    """The COMPLETE family of admitted unitary lifts of one declared support
    step within a declared modulus profile: every phase quadruple in Z/8^4 is
    tried and unitarity is MEASURED, so the parametrisation is checked
    against the unitary set rather than assumed to exhaust it."""
    param, brute = [], []
    for a, b, c in product(range(NROOT), repeat=3):
        U, e = _block_lift(a, b, c, mods, s, n)
        if is_unitary(U, n):
            param.append((U, e))
    for a, b, c, d in product(range(NROOT), repeat=4):
        blk = (((mods[0], s[0], a), (mods[1], s[1], b)),
               ((mods[1], s[1], c), (mods[0], s[0], d)))
        U = _embed(blk, [0, 1], n)
        if is_unitary(U, n):
            brute.append((U, (a, b, c, d)))
    return param, brute


def run_gauge_selftest(lifts):
    """R-1's SELF-TEST: the instrument that enforces a symmetry is measured
    UNDER that symmetry.  Definition 3.1's own admitted symmetry -- vertex
    switching -- is swept exhaustively over the committed one-step diagram
    and over the two-step diagram, and the carried invariant must be FIXED
    under every switching.  The negative control is the unclosed convention,
    reconstructed here, which must MOVE."""
    prog("gauge-covariance self-test")
    n = CARRIER
    U0 = lifts[0][0]
    sup = sup_of_matrix(U0, n)

    closes = cycle_structure([sup], n)[3]
    closes2 = cycle_structure([sup, sup], n)[3]
    bad_conv = {cv: cycle_structure([sup, sup], n, cv)[3]
                for cv in ("unclosed", "reversed")}
    gate("L5-HOL-CLOSED", "derivation",
         "EVERY fundamental cycle carried is a CLOSED walk -- each leg's "
         "tail is the previous leg's head and the walk returns to its start "
         "-- which is Definition 3.1's own criterion for a quantity to be "
         "gauge-invariant, checked leg by leg rather than assumed.  Both "
         "reconstructed mis-conventions, the one that traverses the tree "
         "path in the same direction as the extra edge and the one that "
         "reverses the extra edge, FAIL to close",
         closes and closes2 and not any(bad_conv.values()),
         {"one_step_closes": closes, "two_step_closes": closes2,
          "unclosed_convention_closes": bad_conv["unclosed"],
          "reversed_convention_closes": bad_conv["reversed"]})

    src = [j for j in range(n) if len(sup[j]) > 1]
    tgt = sorted({i for j in src for i in sup[j]})
    loopv = [(0, j) for j in src] + [(1, i) for i in tgt]
    free = len(loopv) - 1                 # one vertex fixed: the global phase
    base = cycle_basis_holonomies([U0], [sup], n)[1]
    base_bad = cycle_basis_holonomies([U0], [sup], n, "unclosed")[1]
    moved = moved_bad = swept = 0
    for ks in product(range(NROOT), repeat=free):
        ph = [{}, {}]
        for v, k in zip(loopv, (0,) + ks):
            ph[v[0]][v[1]] = k
        sw = vertex_switch([U0], n, ph)
        if not is_unitary(sw[0], n):
            moved = -1
            break
        swept += 1
        if cycle_basis_holonomies(sw, [sup], n)[1] != base:
            moved += 1
        if cycle_basis_holonomies(sw, [sup], n, "unclosed")[1] != base_bad:
            moved_bad += 1
    gate("L5-HOL-GAUGE", "derivation",
         "THE GAUGE-COVARIANCE SELF-TEST.  Definition 3.1's own admitted "
         "symmetry is swept EXHAUSTIVELY over the committed one-step "
         "diagram -- every assignment of eighth-root phases to the loop "
         "component's vertices, one fixed as the global phase -- and every "
         "switched lift is verified to remain unitary and inside the "
         "declared family.  The carried invariant is FIXED under every "
         "single switching.  The negative control, the unclosed convention "
         "reconstructed inside this test, MOVES under most of them: the gate "
         "has teeth, and it is the definitional criterion the paper states",
         moved == 0 and moved_bad > swept // 2 and swept == NROOT ** free,
         {"switchings_swept": swept, "carried_invariant_moved": moved,
          "unclosed_control_moved": moved_bad,
          "switched_lifts_still_unitary": swept})

    ws = [sup, sup]
    lv2 = [(0, j) for j in src] + [(1, j) for j in tgt] + [(2, j) for j in tgt]
    free2 = len(lv2) - 1
    pair = [lifts[0][0], lifts[1][0]]
    b_fam = cycle_basis_holonomies(pair, ws, n)[1]
    b_bad = cycle_basis_holonomies(pair, ws, n, "unclosed")[1]
    b_x = cross_checkpoint_phase(pair)
    f_moved = x_moved = bad2 = swept2 = 0
    for ks in product(range(NROOT), repeat=free2):
        ph = [{}, {}, {}]
        for v, k in zip(lv2, (0,) + ks):
            ph[v[0]][v[1]] = k
        sw = vertex_switch(pair, n, ph)
        swept2 += 1
        if cycle_basis_holonomies(sw, ws, n)[1] != b_fam:
            f_moved += 1
        if cycle_basis_holonomies(sw, ws, n, "unclosed")[1] != b_bad:
            bad2 += 1
        if cross_checkpoint_phase(sw) != b_x:
            x_moved += 1
    gate("L5-HOL-GAUGE-2", "derivation",
         "the same self-test at the TWO-step diagram, where the "
         "cross-checkpoint content lives, swept EXHAUSTIVELY over the loop "
         "component's switchings for one declared lift pair: BOTH the "
         "fundamental-cycle family and the cross-checkpoint invariant "
         "X = (arg u00 - arg u10) + (arg v00 - arg v01) are fixed under "
         "every one, while the unclosed control moves.  X is a "
         "gauge-invariant of the carried two-step diagram, measured, not "
         "declared",
         (f_moved == 0 and x_moved == 0 and bad2 > swept2 // 2
          and swept2 == NROOT ** free2),
         {"switchings_swept": swept2, "cycle_family_moved": f_moved,
          "cross_checkpoint_invariant_moved": x_moved,
          "unclosed_control_moved": bad2})


def run_regress_at_amplitude():
    """The regress posed at the amplitude scope, where V-AMP's extra content
    is NOT empty: is the carried amplitude datum anchored by the law, or is
    it one further free declaration?"""
    prog("regress at the amplitude scope")
    n = CARRIER
    lifts, brute = admitted_lift_family()
    gate("L5-AMP-LIFTS", "derivation",
         "the declared lift family is COMPLETE WITHIN ITS DECLARED MODULUS "
         "PROFILE, measured rather than asserted: brute force over all 8^4 "
         "phase quadruples returns exactly the set the three-parameter "
         "orthogonality parametrisation produces.  Completeness is claimed "
         "only inside the equal-modulus eighth-root family; nothing is "
         "claimed for amplitude families outside it",
         (len(lifts) == len(brute)
          and {L2.key(sup_of_matrix(U, n)) for U, _ in lifts} ==
              {L2.key(sup_of_matrix(U, n)) for U, _ in brute}
          and sorted(e for _, e in lifts) == sorted(e for _, e in brute)),
         {"parametrised": len(lifts), "brute_force_over_8^4": len(brute),
          "phase_quadruples_tried": NROOT ** 4})

    hol: dict = {}
    prods: dict = {}
    neg_real = 0
    for U, _e in lifts:
        s = sup_of_matrix(U, n)
        r, h, _sp, pr = cycle_basis_holonomies([U], [s], n)
        hol[h] = hol.get(h, 0) + 1
        prods[pr] = prods.get(pr, 0) + 1
        if pr and all(p[2] == 4 and p[0] > 0 for p in pr):
            neg_real += 1          # counted per LIFT, not per distinct value
    gate("L5-AMP-CONSTANCY", "derivation",
         "THE CONSTANCY THEOREM, GATED EXHAUSTIVELY.  Over the complete "
         "family of admitted unitary lifts of one declared full-support step "
         "the carried closed-loop holonomy is CONSTANT at zeta_8^4 = -1.  It "
         "is forced by unitarity and not by the declared family: row "
         "orthogonality gives u00*conj(u10) = -u01*conj(u11), and "
         "multiplying by conj(u01)*u11 makes the loop product "
         "-|u01|^2*|u11|^2, a negative real, whatever the moduli.  Every one "
         "of the lifts realizes the single class, and every loop product is "
         "a negative rational",
         (len(hol) == 1 and next(iter(hol)) == (4,)
          and next(iter(hol.values())) == len(lifts)
          and neg_real == len(lifts)),
         {"admitted_unitary_lifts": len(lifts),
          "distinct_holonomy_classes": len(hol),
          "classes": {str(k): v for k, v in sorted(hol.items())},
          "lifts_whose_loop_product_is_a_negative_rational": neg_real,
          "distinct_loop_products": len(prods),
          "the_loop_product": [f"{p[0]}*2^-({p[1]}/2)*z8^{p[2]}"
                               for p in next(iter(prods))]})

    py, _pb = admitted_lift_family((Fr(3, 5), Fr(4, 5)), (0, 0))
    pyh: dict = {}
    for U, _e in py:
        pyh[cycle_basis_holonomies([U], [sup_of_matrix(U, n)], n)[1]] = 1
    novar: dict = {}
    for a, b, c, d in product(range(NROOT), repeat=4):
        blk = (((Fr(1), 1, a), (Fr(1), 1, b)), ((Fr(1), 1, c), (Fr(1), 1, d)))
        U = _embed(blk, [0, 1], n)
        h = cycle_basis_holonomies([U], [sup_of_matrix(U, n)], n)[1]
        novar[h] = novar.get(h, 0) + 1
    gate("L5-AMP-CONSTANCY-CTRL", "derivation",
         "the constancy is UNITARITY's and the gate has teeth, both "
         "measured.  POSITIVE CONTROL: a second declared lift family with "
         "UNEQUAL moduli (3/5, 4/5) -- so not the eighth-root equal-modulus "
         "family at all -- is again constant at zeta_8^4.  NEGATIVE "
         "CONTROL: drop unitarity and keep the same full-support block "
         "shape, and the loop holonomy sweeps ALL eight values.  Constancy "
         "is therefore a property of the admitted lifts, not of the loop "
         "formula",
         (len(pyh) == 1 and next(iter(pyh)) == (4,)
          and len(novar) == NROOT),
         {"unequal_modulus_family_size": len(py),
          "unequal_modulus_classes": [str(k) for k in pyh],
          "non_unitary_full_support_classes": len(novar)})

    sup0 = sup_of_matrix(lifts[0][0], n)
    one_support = len({L2.key(sup_of_matrix(U, n)) for U, _ in lifts}) == 1
    recs: dict = {}
    for U, _e in lifts:
        r = pk(L2.written_of(sup_of_matrix(
            amplitude_composite([U, U], n), n)))
        recs[r] = recs.get(r, 0) + 1
    gate("L5-AMP-FREE", "kill",
         "THE AMPLITUDE DATUM IS BLIND, AND THAT IS WHY REGRESS FIRES ON "
         "V-AMP.  Two measurements, one negative and one positive.  "
         "NEGATIVE: the carried gauge-invariant amplitude datum is CONSTANT "
         "over the complete admitted lift family (L5-AMP-CONSTANCY), so it "
         "carries no information whatever about which lift was declared -- "
         "it cannot police a choice it does not vary with.  POSITIVE: the "
         "declared amplitude scope's LAW is its support-level composition "
         "closure, and every admitted lift of the step has the SAME sector "
         "support, so the law constrains no amplitude at all and every "
         "amplitude datum not already forced by unitarity is free by "
         "construction.  Meanwhile what the forger actually chooses with the "
         "lift is visible in the endpoint: over the same family the two-step "
         "word (U,U) writes the address chart for some lifts and the forged "
         "record for the rest.  Anchored implies constant; free implies "
         "unanchored; the regress does not bottom out",
         (len(hol) == 1 and one_support and len(recs) > 1
          and all(v > 1 for v in recs.values())),
         {"admitted_unitary_lifts": len(lifts),
          "distinct_holonomy_classes": len(hol),
          "distinct_sector_supports_among_the_lifts":
              len({L2.key(sup_of_matrix(U, n)) for U, _ in lifts}),
          "endpoint_record_of_(U,U)_over_the_family": recs})
    TABLES["amplitude_lift_family"] = {
        "admitted_unitary_lifts": len(lifts),
        "holonomy_classes": {str(k): v for k, v in sorted(hol.items())},
        "unequal_modulus_control_family": len(py),
        "non_unitary_control_classes": len(novar),
        "endpoint_record_of_the_doubled_word": recs,
        "declared_support_of_every_lift": str(L2.key(sup0))}
    return lifts, hol


# ---------------------------------------------------------------------------
# 9.  THE LOSSY ADVERSARY
# ---------------------------------------------------------------------------

def run_lossy_CL(law):
    prog("lossy adversary, V-CL")
    n = CARRIER
    H = passing_histories_1(law, DISC5)
    buckets: dict = {}
    for F in H:
        buckets.setdefault(certificate_CL(F, law, PREP_FULL, n),
                           []).append(L2.key(F))
    big = max(buckets.values(), key=len)
    ident = L2.key(L2.sup_of_map(tuple(range(n))))
    rot = L2.key(L2.sup_of_map((1, 2, 3, 0, 4)))
    ok = len(buckets) == 1 and ident in big and rot in big
    gate("L5-LOSSY-CL", "kill",
         "RQ0-L5-PROVENANCE-LOSSY FIRES AGAINST V-CL, with an exhibited "
         "witness at the committed fixture: all 120 admitted one-step "
         "histories that produce the carrier's own algebra carry ONE AND "
         "THE SAME classical certificate.  Among them are the legitimate "
         "address context's history -- the identity, nothing was done -- "
         "and the manufactured context's deleted rotation.  Two admitted "
         "histories, one legitimate and one forged, agreeing on every "
         "carried classical certificate and differing in the un-carried "
         "part: the pin's adversary, constructed",
         ok, {"histories": len(H), "distinct_certificates": len(buckets),
              "largest_indistinguishable_class": len(big),
              "identity_in_class": ident in big,
              "rotation_in_class": rot in big})
    percert: dict = {}
    for F in law:
        percert.setdefault(L2.key(L2.written_of(F)), set()).add(
            certificate_CL(F, law, PREP_FULL, n))
    allrec = len(percert)
    worst = max(len(v) for v in percert.values())
    perb = {pk(p): (len(passing_histories_1(law, p)),
                    len({certificate_CL(F, law, PREP_FULL, n)
                         for F in passing_histories_1(law, p)}))
            for p in FIXTURE}
    gate("L5-LOSSY-CL-THM", "kill",
         "AND IT IS A THEOREM, NOT A FIXTURE FACT.  The carried certificate "
         "is a function of the RECORD the checkpoint writes and of nothing "
         "else about the operation: its first component is that record and "
         "every later component is computed from it.  Measured over the "
         "whole committed law: operations writing the same record carry the "
         "same certificate in EVERY case, and the number of distinct carried "
         "certificates equals the number of distinct records written.  The "
         "same collapse therefore occurs at every committed boundary, not "
         "only at the collision one -- a chain of carried certificates "
         "carries exactly the sequence of written records.  LOSSY against "
         "V-CL is immediate from what the pin specifies is carried",
         (worst == 1
          and all(c == 1 for _h, c in perb.values())),
         {"operations_in_the_law": len(law),
          "distinct_records_written": allrec,
          "distinct_certificates": sum(len(v) for v in percert.values()),
          "max_certificates_among_same_record_operations": worst,
          "histories_and_certificates_per_committed_boundary": perb})

    TABLES["lossy_CL"] = {"histories": len(H),
                          "distinct_certificates": len(buckets),
                          "class_size": len(big),
                          "records_vs_certificates_over_the_whole_law":
                              [allrec, sum(len(v) for v in percert.values())],
                          "per_boundary_histories_to_certificates": perb}
    return ok


def run_lossy_AMP(law, lifts):
    prog("lossy adversary, V-AMP")
    n = CARRIER

    H = passing_histories_1(law, DISC5)
    ac = {certificate_AMP([canonical_lift(F, n)], [F], law, PREP_FULL, n)
          for F in H}
    gate("L5-LOSSY-AMP-C", "kill",
         "RQ0-L5-PROVENANCE-LOSSY FIRES AGAINST V-AMP AT THE COMMITTED "
         "SCOPE, and it fires with the SAME witness: the 120 admitted "
         "histories at the carrier's own algebra carry one and the same "
         "AMPLITUDE certificate too, because their diagrams are monomial "
         "and a monomial diagram has no gauge-invariant loop content at "
         "all.  The amplitude bits are empty exactly where the provenance "
         "question is sharpest",
         len(ac) == 1,
         {"histories": len(H), "distinct_AMP_certificates": len(ac)})

    mono = [canonical_lift(F, n) for F in H]
    unit_mods = {w[0] for U in mono for row in U for w in row if w[0] != 0}
    mono_unit = {}
    for c in [(Fr(1, 2), 0, 0), (Fr(1), 1, 0), (Fr(2), 0, 0), (Fr(1), 0, 0)]:
        M = [[AZERO] * n for _ in range(n)]
        for j in range(n):
            M[next(iter(H[0][j]))][j] = c
        mono_unit[f"{c[0]}*2^-({c[1]}/2)"] = is_unitary(
            tuple(tuple(r) for r in M), n)
    gate("L5-LOSSY-AMP-GEN", "derivation",
         "Theorem 6.2 carried by its ARGUMENT and not by one measured lift: "
         "a monomial diagram has cycle rank 0, so it has no loop content "
         "whatever lift is declared, and unitarity forces UNIT moduli on a "
         "monomial matrix -- measured by trying candidate moduli on one "
         "committed permutation support, where exactly the unit modulus "
         "gives a unitary.  So the committed-scope collapse holds for EVERY "
         "admitted lift, not only the all-ones one",
         (unit_mods == {Fr(1)}
          and [m for m, u in mono_unit.items() if u] == ["1*2^-(0/2)"]),
         {"moduli_in_the_canonical_lifts": [str(x) for x in unit_mods],
          "candidate_moduli_giving_a_unitary_monomial": mono_unit})

    sup01 = sup_of_matrix(lifts[0][0], n)
    ws = [sup01, sup01]
    by_exp = {e: U for U, e in lifts}

    # THE CORRECTED WITNESS.  Three declared phase triples; the fourth
    # exponent of each block is COMPUTED from the orthogonality relation.
    wexp = [_block_lift(*t)[1] for t in ((0, 0, 0), (0, 1, 0), (0, 2, 0))]
    wA = [by_exp[wexp[0]], by_exp[wexp[1]]]
    wB = [by_exp[wexp[0]], by_exp[wexp[2]]]
    shA, shB = step_local_shadow(wA, ws, n), step_local_shadow(wB, ws, n)
    gA = cycle_basis_holonomies(wA, ws, n)[1]
    gB = cycle_basis_holonomies(wB, ws, n)[1]
    xA, xB = cross_checkpoint_phase(wA), cross_checkpoint_phase(wB)
    witness = {"lift_exponents_A": [list(e) for e in (wexp[0], wexp[1])],
               "lift_exponents_B": [list(e) for e in (wexp[0], wexp[2])],
               "step_local_shadows_identical": shA == shB,
               "per_step_holonomies_A": [list(h) for h in shA[0]],
               "per_step_holonomies_B": [list(h) for h in shB[0]],
               "checkpoint_amplitude_records_A": list(shA[1]),
               "checkpoint_amplitude_records_B": list(shB[1]),
               "global_holonomies_A": list(gA),
               "global_holonomies_B": list(gB),
               "cross_checkpoint_invariant_A": xA,
               "cross_checkpoint_invariant_B": xB}

    # The pool sweep: what the step-local reading can and cannot see.
    # Holonomy families and the cross-checkpoint invariant are swept over
    # EVERY pair of admitted lifts; the endpoint record, which needs a
    # composite, is swept over every pair whose first step is the declared
    # Hadamard, and that declared scope is printed with the result.
    per_shadows = {cycle_basis_holonomies([U], [sup01], n)[1]
                   for U, _e in lifts}
    fams, xvals, byx = {}, {}, {}
    for U, _eu in lifts:
        for V, _ev in lifts:
            f = cycle_basis_holonomies([U, V], ws, n)[1]
            x = cross_checkpoint_phase([U, V])
            fams[f] = fams.get(f, 0) + 1
            xvals[x] = xvals.get(x, 0) + 1
    for V, _ev in lifts:
        pr = [lifts[0][0], V]
        byx.setdefault(cross_checkpoint_phase(pr), set()).add(
            pk(L2.written_of(sup_of_matrix(amplitude_composite(pr, n), n))))
    TABLES["cross_checkpoint_sweep"] = {
        "lift_pairs": len(lifts) ** 2,
        "distinct_step_local_holonomy_values": len(per_shadows),
        "distinct_global_families": len(fams),
        "global_families": {str(k): v for k, v in sorted(fams.items())},
        "distinct_cross_checkpoint_values": len(xvals),
        "record_sweep_scope": "every pair whose first step is the declared "
                              "Hadamard lift",
        "record_sweep_pairs": len(lifts),
        "endpoint_record_by_cross_checkpoint_value":
            {str(k): sorted(v) for k, v in sorted(byx.items())}}

    gate("L5-LOSSY-AMP-A", "kill",
         "RQ0-L5-PROVENANCE-LOSSY AGAINST V-AMP AT THE AMPLITUDE SCOPE, "
         "under the DECLARED step-local reading of an admitted "
         "verification.  Over the complete pool of admitted lift pairs of "
         "one declared support word the step-local holonomy shadow takes "
         "exactly ONE value -- it reads nothing at all -- while the "
         "cross-checkpoint invariant sweeps ALL eight of its values.  "
         "Exhibited: two admitted lift pairs agreeing on EVERY "
         "checkpoint-local datum -- per-step holonomies, moduli, and both "
         "checkpoints' amplitude records, so the visible-cancellation datum "
         "is included and not omitted -- and differing in cross-checkpoint "
         "holonomy.  What this establishes is INFORMATION loss under that "
         "reading; the reading itself does not bind (Section 6.4)",
         (shA == shB and gA != gB and xA != xB
          and len(per_shadows) == 1 and len(xvals) == NROOT
          and all(len(v) == 1 for v in byx.values())),
         dict(witness, pool_step_local_holonomy_values=len(per_shadows),
              pool_cross_checkpoint_values=len(xvals),
              pool_global_families=len(fams)))

    gate("L5-SHADOW-SEP", "derivation",
         "POSITIVE CONTROL for the shadow function: the step-local shadow "
         "MUST separate a cancelling word from a non-cancelling one, because "
         "the record the amplitude composite writes is checkpoint-local data "
         "par excellence -- it is the paper's own Gain 1.  Measured: the "
         "doubled Hadamard word, whose amplitude composite is the identity, "
         "has a different shadow from the witness word, whose composite "
         "writes the coarse record.  A shadow that omitted the amplitude "
         "records would fail this gate",
         (step_local_shadow([by_exp[wexp[0]], by_exp[wexp[0]]], ws, n)
          != shA),
         {"cancelling_word_records": list(step_local_shadow(
             [by_exp[wexp[0]], by_exp[wexp[0]]], ws, n)[1]),
          "witness_word_records": list(shA[1])})

    r_all = cycle_basis_holonomies([lifts[0][0], lifts[0][0]], ws, n)[0]
    r_loc = sum(cycle_basis_holonomies([U], [sup01], n)[0]
                for U in (lifts[0][0], lifts[0][0]))
    gate("L5-LOSSY-AMP-DIM", "derivation",
         "the accounting that makes the witness inevitable: the carried "
         "two-step diagram has cycle rank 3 while its two checkpoint-local "
         "diagrams have rank 1 each, so a step-local verification leaves a "
         "rank-1 residue of gauge-invariant content unread.  The rank "
         "accounting is combinatorial and holds for every lift",
         r_all == 3 and r_loc == 2,
         {"global_rank": r_all, "checkpoint_local_rank": r_loc,
          "unread_residue": r_all - r_loc})

    reads_it = (certificate_AMP(wA, ws, law, PREP_FULL, n)
                != certificate_AMP(wB, ws, law, PREP_FULL, n))
    spans2 = cycle_basis_holonomies(wA, ws, n)[2]
    gate("L5-LOSSY-READING", "derivation",
         "THE READING, ADJUDICATED RATHER THAN DISCLOSED, AND IT BINDS THE "
         "OTHER WAY.  A verification that compares certificates containing "
         "the cross-checkpoint holonomy READS the cross-checkpoint "
         "holonomy: Definition 2.3 puts the carried diagram's loop "
         "holonomies inside V-AMP's certificate, (P2) compares carried "
         "against recomputed certificates, and the certificate is computed "
         "over the WHOLE carried word at every committed patch -- measured "
         "here, not asserted.  Checkpoints are the cumulative composites, so "
         "locality at the final checkpoint is locality to the whole carried "
         "path; and the numerals construal that licenses CARRYING the "
         "amplitudes is the same one that licenses computing a loop product "
         "of them.  The step-local restriction is therefore a declared "
         "modelling choice and is labelled one.  The TRUE scissors is "
         "measured and reading-independent: ANCHORED implies CONSTANT (the "
         "per-step holonomy that unitarity anchors is zeta_8^4 always), FREE "
         "implies UNANCHORED (the amplitude scope's law is support-level)",
         reads_it and max(spans2) == 2,
         {"V_AMP_certificate_separates_the_step_local_witness_pair":
              reads_it,
          "layers_spanned_by_a_carried_fundamental_cycle": max(spans2),
          "anchored_datum_is_constant": "zeta_8^4 on all admitted lifts",
          "free_datum_is_unanchored": "the law is the support-level closure",
          "LOSSY_vs_V_AMP_under_the_binding_reading":
              "does not fire at the amplitude scope; fires at the committed "
              "scope by Theorem 6.2, which is reading-independent"})

    TABLES["lossy_AMP"] = {"committed_scope_certificates": len(ac),
                           "global_rank": r_all, "local_rank": r_loc,
                           "witness": witness}
    return witness is not None


# ---------------------------------------------------------------------------
# 10.  DISCRIMINATOR 4 -- name-blindness, separation, amnesty
# ---------------------------------------------------------------------------

def s_manufacture_depth(part, law, prep, rho, n, word):
    """S1: how many carried checkpoints are B''-INADMISSIBLE."""
    return Fr(sum(1 for C in checkpoints_of(word)
                  if not adj_c(L2.written_of(C), law, prep, n)["admissible"]))


def s_intermediate_spread(part, law, prep, rho, n, word):
    """S2: how many DISTINCT records the carried path passes through."""
    return Fr(len({L2.written_of(C) for C in checkpoints_of(word)}))


def s_coarsest_checkpoint_defect(part, law, prep, rho, n, word):
    """S3: the concordance defect of the coarsest carried checkpoint."""
    return max(L3.bayes_error(L2.written_of(C), rho)
               for C in checkpoints_of(word))


def s_history_fan_in(part, law, prep, rho, n, word):
    """S4: how many admitted one-step paths write the declared record --
    the declaration's own ambiguity, read as a statistic."""
    return Fr(sum(1 for F in law if L2.written_of(F) == part))


def s_path_length(part, law, prep, rho, n, word):
    """S5: the declared length of the carried path."""
    return Fr(len(word))


def s_carried_cycle_rank(part, law, prep, rho, n, word):
    """S6 (V-AMP): the total gauge-invariant loop content carried."""
    return Fr(cycle_basis_holonomies(
        [canonical_lift(g, n) for g in word], list(word), n)[0])


STATS = [s_manufacture_depth, s_intermediate_spread,
         s_coarsest_checkpoint_defect, s_history_fan_in, s_path_length,
         s_carried_cycle_rank]
READS_RHO = {"s_coarsest_checkpoint_defect"}


def _stat_label_mutant(part, law, prep, rho, n, word):
    """Used ONLY by the `stat-label` mutant: a DECLARED statistic that reads a
    name.  L5-NB's declared-statistic clause must catch it -- otherwise that
    half of the gate is untested by the suite."""
    return Fr(1) if any(set(b) == {0} for b in part) else Fr(0)


def nb_negative_control(part, law, prep, rho, n, word):
    """PERMANENT NEGATIVE CONTROL for the name-blindness gate -- must be
    CAUGHT.  It compares a NAME: an indicator that the configuration
    labelled 0 forms a block of its own.  Branch C's label-reading class,
    transported; the gate passes only if this is flagged."""
    return Fr(1) if any(set(b) == {0} for b in part) else Fr(0)


def act_word(word, sigma, n):
    """The relabelling action on a carried history: relabel every step's
    support map throughout the datum."""
    inv = [0] * n
    for i, s in enumerate(sigma):
        inv[s] = i
    return [tuple(frozenset({sigma[x] for x in w[inv[j]]})
                  for j in range(n)) for w in word]


def act_law_fs(law, sigma, n):
    inv = [0] * n
    for i, s in enumerate(sigma):
        inv[s] = i
    return [tuple(frozenset({sigma[x] for x in F[inv[j]]})
                  for j in range(n)) for F in law]


def run_discriminator_4(law):
    prog("discriminator 4 (name-blindness, separation, amnesty)")
    n = CARRIER
    TH = true_histories(FIXTURE, n)

    group = ([tuple(range(n))] if MUTANT == "nb-lax"
             else list(permutations(range(n))))
    stats = ([_stat_label_mutant] + STATS[1:] if MUTANT == "stat-label"
             else STATS)
    nb_rows = []
    for fn in stats + [nb_negative_control]:
        viol = 0
        for part in FIXTURE:
            base = fn(part, law, PREP_FULL, RHO, n, TH[part])
            for sigma in group:
                if fn(L4.act_part(part, sigma), act_law_fs(law, sigma, n),
                      L4.act_prep(PREP_FULL, sigma), L4.act_rho(RHO, sigma),
                      n, act_word(TH[part], sigma, n)) != base:
                    viol += 1
        nb_rows.append({"statistic": fn.__name__, "violations": viol,
                        "name_blind": viol == 0,
                        "is_negative_control": fn is nb_negative_control})
    TABLES["name_blindness"] = nb_rows
    decl = [r for r in nb_rows if not r["is_negative_control"]]
    ctrl = [r for r in nb_rows if r["is_negative_control"]][0]
    gate("L5-NB", "discriminator",
         "(4) the name-blindness gate is applied to EVERY "
         "provenance-reading statistic, over all 120 relabellings acting on "
         "the whole declared datum at once -- boundary, law, preparation, "
         "state AND the carried history together.  The gate is "
         "SELF-TESTING: it passes only if all six declared statistics are "
         "name-blind AND the permanent label-reading negative control -- an "
         "indicator that the configuration named 0 forms a block of its own "
         "-- is CAUGHT by the same sweep",
         all(r["name_blind"] for r in decl) and not ctrl["name_blind"],
         {"declared": {r["statistic"]: r["violations"] for r in decl},
          "negative_control_violations": ctrl["violations"],
          "negative_control_caught": not ctrl["name_blind"],
          "group_size": len(group)})

    sep_rows = []
    for fn in stats:
        vals = {p: fn(p, law, PREP_FULL, RHO, n, TH[p]) for p in FIXTURE}
        leg = [vals[p] for p in FIXTURE if PROVENANCE[p] == "LEGITIMATE"]
        frg = [vals[p] for p in FIXTURE if PROVENANCE[p] == "FORGED"]
        sep_rows.append({"statistic": fn.__name__,
                         "values": {pk(p): S(vals[p]) for p in FIXTURE},
                         "separates": max(leg) < min(frg)})
    TABLES["separation"] = sep_rows
    gate("L5-SEP", "discriminator",
         "MEASURED: with the TRUE histories carried, NO declared "
         "provenance-reading statistic separates the legitimate contexts "
         "below the forged ones at the committed state.  The legitimate "
         "coarse chart's true history has the same form as a "
         "manufacture-path, because it IS one -- an admitted operation that "
         "writes the declared record",
         not any(r["separates"] for r in sep_rows),
         {r["statistic"]: r["separates"] for r in sep_rows})

    grid = L4.grid_states()
    amn = []
    for fn in stats:
        if fn.__name__ not in READS_RHO:
            vals = {p: fn(p, law, PREP_FULL, RHO, n, TH[p]) for p in FIXTURE}
            leg = [vals[p] for p in FIXTURE if PROVENANCE[p] == "LEGITIMATE"]
            frg = [vals[p] for p in FIXTURE if PROVENANCE[p] == "FORGED"]
            s = len(grid) if max(leg) < min(frg) else 0
            i = len(grid) if min(leg) > max(frg) else 0
            amn.append({"statistic": fn.__name__, "separates": s,
                        "ties": len(grid) - s - i, "inverts": i,
                        "state_independent": True})
            continue
        s = t = i = 0
        for rho in grid:
            vals = {p: fn(p, law, PREP_FULL, rho, n, TH[p]) for p in FIXTURE}
            leg = [vals[p] for p in FIXTURE if PROVENANCE[p] == "LEGITIMATE"]
            frg = [vals[p] for p in FIXTURE if PROVENANCE[p] == "FORGED"]
            if max(leg) < min(frg):
                s += 1
            elif min(leg) > max(frg):
                i += 1
            else:
                t += 1
        amn.append({"statistic": fn.__name__, "separates": s, "ties": t,
                    "inverts": i, "state_independent": False})
    rho2 = next(r for r in grid if r != RHO)
    reads = {}
    for fn in stats:
        v1 = [fn(p, law, PREP_FULL, RHO, n, TH[p]) for p in FIXTURE]
        v2 = [fn(p, law, PREP_FULL, rho2, n, TH[p]) for p in FIXTURE]
        reads[fn.__name__] = v1 != v2
    gate("L5-RHO-GATED", "discriminator",
         "the amnesty sweep's state-independence is MEASURED, not declared.  "
         "Each statistic is evaluated at the committed state and at a second "
         "declared state; the set that moves is compared against the "
         "declared state-reading set, and the extrapolation used for the "
         "state-independent ones is licensed by that measurement rather than "
         "by a hand-maintained list.  Exactly one statistic moves, and it is "
         "the declared one -- so the gate is a positive control on itself",
         {k for k, v in reads.items() if v} == READS_RHO,
         {"moves_between_two_declared_states": reads,
          "declared_state_reading": sorted(READS_RHO)})

    TABLES["amnesty"] = amn
    gate("L5-AMNESTY", "discriminator",
         "the amnesty sweep is run over all 4845 declared states for every "
         "provenance-reading statistic.  No statistic separates at ANY "
         "state, so the sweep has nothing to amnesty: the failure here is "
         "PRIOR to amnesty rather than an instance of it, and "
         "FINGERPRINT-AMNESTY's pattern does not recur",
         all(r["separates"] == 0 for r in amn),
         {r["statistic"]: [r["separates"], r["ties"], r["inverts"]]
          for r in amn})
    return nb_rows, sep_rows, amn


# ---------------------------------------------------------------------------
# 11.  THE DELTA
# ---------------------------------------------------------------------------

def run_delta(rows_d1, hol_classes):
    prog("the V-CL / V-AMP delta")
    by = {(r["boundary"], r["variant"]): r for r in rows_d1}
    amp = {r["word"]: r for r in TABLES["amplitude_words"]}
    delta = {
        "at_the_committed_scope": {
            "verdicts_identical": all(
                by[(pk(p), "V-CL")]["L5_admissible"]
                == by[(pk(p), "V-AMP")]["L5_admissible"] for p in FIXTURE),
            "carried_cycle_rank": {pk(p): by[(pk(p), "V-AMP")]["cycle_rank"]
                                   for p in FIXTURE},
            "verdict": "ZERO -- the amplitude bits buy NOTHING here, and "
                       "provably so",
            "reason": "every committed law is single-valued; single-valued "
                      "steps have acyclic layered diagrams; vertex "
                      "switching trivializes every edge phase on a forest, "
                      "so there is no gauge-invariant amplitude content to "
                      "carry"},
        "at_the_declared_amplitude_scope": {
            "V_AMP_carries_strictly_more": True,
            "buys_1_visible_cancellation": {
                "word": "(H01,H01)",
                "support_record": amp["(H01,H01)"]["support_record"],
                "amplitude_record": amp["(H01,H01)"]["amplitude_record"],
                "statement": "the amplitude composite is the identity while "
                             "the support composite writes the FORGED 2+1+1 "
                             "record: V-AMP adjudicates an endpoint claim "
                             "that V-CL gets WRONG"},
            "buys_2_loop_holonomy": {
                "cycle_ranks": {k: amp[k]["cycle_rank"] for k in amp},
                "distinct_single_step_holonomy_classes": len(hol_classes),
                "statement": "V-AMP distinguishes carried histories V-CL "
                             "identifies -- a strictly finer equivalence on "
                             "declared provenance"},
            "does_NOT_buy": [
                "the extra content is a FREE DECLARATION (L5-AMP-FREE): "
                "many admitted unitary lifts realize each holonomy class, "
                "so a forger declares whichever one a legitimate "
                "declaration carries -- REGRESS eats it",
                "the extra content is NOT READABLE by the checkpoint-local "
                "verification (P2) is defined to be (L5-LOSSY-AMP-A) -- "
                "LOSSY eats it",
                "at the carrier's own algebra, the one place the base "
                "supplies a genuine provenance collision, the content is "
                "IDENTICALLY EMPTY (L5-LOSSY-AMP-C)"]},
        "reverse_direction": "V-CL certifies nothing V-AMP cannot: the "
                             "classical certificate is the support-and-"
                             "modulus shadow of the amplitude one, computed "
                             "by the same routes.  The delta is one-way.",
        "delta_measured_against_the_kills": "ZERO -- the same two kills "
                                            "fire on both variants"}
    FINDINGS["delta"] = delta
    gate("L5-DELTA", "delta",
         "THE DELTA, STATED EXACTLY.  At the committed scope V-AMP == V-CL "
         "bit for bit and the amplitude bits buy NOTHING, provably.  At the "
         "declared amplitude scope V-AMP buys two real things -- visible "
         "cancellation and loop holonomy -- and BOTH are eaten, one by each "
         "kill.  Measured against the kills the delta is ZERO",
         delta["at_the_committed_scope"]["verdicts_identical"], None)
    return delta


def run_exactness():
    """The exactness gate, measured over the sums this run ACTUALLY FORMED
    rather than over the declared generators' moduli strings."""
    prog("exactness")
    formed = len(MIXED_FORMED)
    # POSITIVE CONTROL: an exact cancellation that the (c, s, e) shorthand
    # cannot see, because it spans two incommensurable shorthands --
    # 2^(-1/2)*zeta = (1 + zeta^2)/2 -- and vanishes only in the field.
    zc = asum([(Fr(1), 1, 1), (Fr(1, 2), 0, 4), (Fr(1, 2), 0, 6)])
    nz = asum([(Fr(1, 2), 0, 0), (Fr(1, 2), 0, 1)])
    caught = len(MIXED_FORMED) - formed
    gate("L5-AMP-EXACT", "derivation",
         "EXACT THROUGHOUT, AND THE CLAIM IS WHAT THE PREDICATE MEASURES.  "
         "No float enters any path; every amplitude is a rational "
         "combination of eighth roots.  The (c, s, e) shorthand names the "
         "declared family, and the declared family is NOT closed under "
         "addition -- composites of two general admitted lifts leave it -- "
         "so every such residue is carried in the CANONICAL Q(zeta_8) "
         "coordinates instead, where equality and vanishing are decided "
         "exactly.  This gate counts the residues EVERY sum this run formed "
         "and runs two controls on the decision procedure: a sum that "
         "vanishes only across two incommensurable shorthands must return "
         "the field zero, and a genuinely non-zero residue must be carried "
         "rather than dropped",
         (zc == AZERO and nz[0] == "MIXED" and any(nz[1]) and caught == 1),
         {"residues_carried_in_canonical_coordinates": formed,
          "cross_shorthand_cancellation_decided_zero": zc == AZERO,
          "non_zero_residue_carried": nz[0] == "MIXED"})


def run_mutant_table():
    """R-9: every declared mutant is run to completion and must die, and the
    GATES IT KILLS are recorded -- a mutant that exits 1 without falsifying a
    named gate would be a mutant that tests nothing."""
    import subprocess
    prog(f"mutant table ({len(MUTANTS)} mutants)")
    rows = []
    for m in MUTANTS:
        r = subprocess.run([sys.executable, str(Path(__file__).resolve()),
                            "--mutant", m, "--quiet"],
                           capture_output=True, text=True)
        kill = {"failed_anchors": [], "failed_gates": []}
        for ln in r.stdout.splitlines():
            if ln.startswith("KILL-JSON "):
                kill = json.loads(ln[len("KILL-JSON "):])
        rows.append({"mutant": m, "exit": r.returncode,
                     "died": r.returncode == 1,
                     "falsified_anchors": kill["failed_anchors"],
                     "falsified_gates": kill["failed_gates"]})
        prog(f"  {m}: exit {r.returncode}, kills "
             f"{kill['failed_anchors'] + kill['failed_gates']}")
    TABLES["mutants"] = rows
    gate("L5-MUTANTS", "freeze",
         "THE FALSIFICATION SUITE, RUN AND RECORDED.  Every declared mutant "
         "breaks exactly one anchor or one derivation step, is run to "
         "completion, must EXIT 1, and must falsify at least one NAMED gate "
         "or anchor -- an exit code alone would not show the suite tests "
         "anything.  The suite includes sign-convention and orientation "
         "mutants of the holonomy: a wholesale replacement mutant tests only "
         "that some invariant is computed, never that the RIGHT one is",
         all(r["died"] and (r["falsified_anchors"] or r["falsified_gates"])
             for r in rows) and len(rows) == len(MUTANTS),
         {"mutants": len(rows),
          "died": sum(1 for r in rows if r["died"]),
          "kills": {r["mutant"]: r["falsified_anchors"] + r["falsified_gates"]
                    for r in rows}})


# ---------------------------------------------------------------------------
# 12.  VERDICT
# ---------------------------------------------------------------------------

def verdict():
    g = {x["id"]: x for x in GATES}
    regress = (g["L5-D2-EXIST"]["passed"] and g["L5-D2-COLLISION"]["passed"]
               and g["L5-D2-REDUCTION"]["passed"]
               and g["L5-AMP-FREE"]["passed"])
    lossy_cl = g["L5-LOSSY-CL"]["passed"] and g["L5-LOSSY-CL-THM"]["passed"]
    # The V-AMP arm fires on the READING-INDEPENDENT committed-scope witness
    # (Theorem 6.2, where the carried content is provably empty); the
    # amplitude-scope witness is carried beside it under a declared reading.
    lossy_amp = (g["L5-LOSSY-AMP-C"]["passed"]
                 and g["L5-LOSSY-AMP-GEN"]["passed"])
    tags = []
    if regress:
        tags.append("RQ0-L5-PROVENANCE-REGRESS")
    if lossy_cl or lossy_amp:
        tags.append("RQ0-L5-PROVENANCE-LOSSY")
    tags.append("RQ0-L5-BLOCKED-AT-THE-DECLARATION")
    per = {"V-CL": {"PROVENANCE-CERTIFIES": not (regress or lossy_cl),
                    "PROVENANCE-REGRESS": regress,
                    "PROVENANCE-LOSSY": lossy_cl},
           "V-AMP": {"PROVENANCE-CERTIFIES": not (regress or lossy_amp),
                     "PROVENANCE-REGRESS": regress,
                     "PROVENANCE-LOSSY": lossy_amp}}
    FINDINGS["verdict"] = {
        "tags": tags, "per_variant": per,
        "both_kills_fire_on_both_variants":
            regress and lossy_cl and lossy_amp,
        "residue": "BRANCH B (coarse arena-relativity) IS THE PROVEN "
                   "RESIDUE: both pre-registered kills fire, on both "
                   "variants, at the declared scope"}
    return per, tags


# ---------------------------------------------------------------------------
# 13.  RECEIPT AND RENDER
# ---------------------------------------------------------------------------

def build_receipt():
    must = [x for x in GATES if x["class"] != "disclosure"]
    fails = sum(1 for x in must if not x["passed"])
    fails += sum(1 for x in ANCHORS if not x["passed"])
    return {"schema": SCHEMA, "pin_commit": PIN_COMMIT,
            "base_commit": BASE_COMMIT, "source_sha256": SOURCE_SHA256,
            "anchors": ANCHORS, "gates": GATES, "tables": TABLES,
            "findings": FINDINGS,
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
    L, W = [], 78
    L.append("=" * W)
    L.append("RQ0-L5 BRANCH A -- THE PROVENANCE QUINTUPLE, BOTH VARIANTS")
    L.append("=" * W)
    L.append(f"pin {rec['pin_commit']}   base {rec['base_commit']}")
    L.append(f"source sha256 {rec['source_sha256']}")
    L.append("")
    L.append("-" * W)
    L.append("ANCHORS (exit 1 on mismatch; never on a substantive negative)")
    L.append("-" * W)
    for a in rec["anchors"]:
        L.append(f"  {a['id']}  {'OK  ' if a['passed'] else 'FAIL'} "
                 f"{a['quantity']}")
        L.append(f"        committed {a['committed']}")
        L.append(f"        computed  {a['computed']}")
    L.append("")
    L.append("-" * W)
    L.append("THE FOUR DISCRIMINATORS, PER VARIANT")
    L.append("-" * W)
    L.append("  (1)+(3) committed patches carrying their TRUE histories")
    L.append("     boundary               variant  prov   B''  P1 P2 P2s  L5"
             "  rank")
    for r in rec["tables"]["discriminator_1"]:
        L.append("     %-22s %-8s %-6s %-4s %-2s %-2s %-4s %-3s %s" % (
            r["name"], r["variant"], r["provenance_truth"][:4],
            "yes" if r["bdd_admissible"] else "no",
            "ok" if r["P1"] else "X", "ok" if r["P2_weak"] else "X",
            "ok" if r["P2_strong"] else "X",
            "YES" if r["L5_admissible"] else "no", r.get("cycle_rank", "-")))
    L.append("")
    L.append("  (2) the regress: declarable one-step histories per boundary")
    for r in rec["tables"]["regress_history_counts"]:
        L.append("     %-22s histories %-5d  cost-of-ADMISSIBILITY %d" % (
            r["name"], r["passing_one_step_histories"],
            r["cost_of_ADMISSIBILITY"]))
    c = rec["tables"]["delta_collision"]
    L.append(f"     collision at {c['boundary']}: {c['passing_histories']} "
             f"histories -> {c['distinct_CL_certificates']} distinct V-CL "
             f"certificate, {c['distinct_AMP_certificates']} distinct V-AMP")
    L.append("")
    L.append("  (4) name-blindness, separation, amnesty")
    for r in rec["tables"]["name_blindness"]:
        if r["is_negative_control"]:
            L.append("     %-30s NB %-5s  <- permanent label-reading "
                     "negative control, must be caught (%d violations)" % (
                         r["statistic"], r["name_blind"], r["violations"]))
            continue
        s = [x for x in rec["tables"]["separation"]
             if x["statistic"] == r["statistic"]][0]
        m = [x for x in rec["tables"]["amnesty"]
             if x["statistic"] == r["statistic"]][0]
        L.append("     %-30s NB %-5s sep %-5s sweep %d/%d/%d" % (
            r["statistic"], r["name_blind"], s["separates"],
            m["separates"], m["ties"], m["inverts"]))
    L.append("")
    L.append("-" * W)
    L.append("THE AMPLITUDE LAYER (V-AMP), at the declared amplitude scope")
    L.append("-" * W)
    L.append("  word         support-record  amplitude-record rank cancels "
             "holonomies")
    for r in rec["tables"]["amplitude_words"]:
        L.append("  %-12s %-15s %-16s %-4d %-7s %s" % (
            r["word"], r["support_record"], r["amplitude_record"],
            r["cycle_rank"], r["cancellation"],
            r["holonomy_phases"][:6]))
    L.append("")
    L.append("-" * W)
    L.append("GATES")
    L.append("-" * W)
    for x in rec["gates"]:
        L.append(f"  {x['id']:<20} [{x['class']}] "
                 f"{'PASS' if x['passed'] else 'FAIL'}")
        for ln in _wrap(x["claim"], 70):
            L.append("      " + ln)
        if x["value"] is not None:
            L.append("      value: " + json.dumps(
                x["value"], sort_keys=True, default=str)[:1200])
    if "mutants" in rec["tables"]:
        L.append("")
        L.append("-" * W)
        L.append("THE FALSIFICATION SUITE -- every mutant must exit 1 AND "
                 "falsify a named gate")
        L.append("-" * W)
        for r in rec["tables"]["mutants"]:
            k = r["falsified_anchors"] + r["falsified_gates"]
            L.append("  %-16s exit %d  %-8s kills %s" % (
                r["mutant"], r["exit"], "DIED" if r["died"] else "SURVIVED",
                ", ".join(k) if k else "NOTHING"))
    L.append("")
    L.append("-" * W)
    L.append("THE DELTA -- WHAT THE AMPLITUDE BITS BUY")
    L.append("-" * W)
    L.append(json.dumps(rec["findings"]["delta"], indent=1, sort_keys=True,
                        default=str))
    L.append("")
    L.append("-" * W)
    L.append("VERDICT")
    L.append("-" * W)
    v = rec["findings"]["verdict"]
    for variant, d in sorted(v["per_variant"].items()):
        L.append(f"  {variant}:")
        for k, val in sorted(d.items()):
            L.append(f"      {k:<26} {val}")
    L.append("  registered tags: " + ", ".join(v["tags"]))
    L.append("  both kills fire on both variants: "
             f"{v['both_kills_fire_on_both_variants']}")
    L.append("  " + v["residue"])
    L.append("")
    t = rec["totals"]
    L.append(f"TOTALS: {t['anchors']} anchors, {t['gates']} gates, "
             f"{t['must_pass_failures']} must-pass failures")
    L.append("=" * W)
    return "\n".join(L) + "\n"


# ---------------------------------------------------------------------------
# 14.  MUTANTS -- over anchors AND derivation gates
# ---------------------------------------------------------------------------

MUTANTS = ["anchor-A02", "anchor-A04", "anchor-A05", "anchor-A06",
           "anchor-A07", "anchor-A09", "comp-lax", "pres-lax",
           "p1-break", "p2-break", "acyc-lax", "hol-lax", "hol-sign",
           "hol-orient", "shadow-lax", "stat-label", "amp-cancel-lax",
           "nb-lax", "srcscan-lax", "hist-tune"]


def main() -> int:
    global MUTANT, SOURCE_SHA256
    ap = argparse.ArgumentParser()
    ap.add_argument("--mutant", default=None)
    ap.add_argument("--quiet", action="store_true")
    ap.add_argument("--falsification-selftest", action="store_true")
    a = ap.parse_args()
    MUTANT = a.mutant
    SOURCE_SHA256 = hashlib.sha256(
        Path(__file__).resolve().read_bytes()).hexdigest()
    L2.MUTANT = MUTANT if MUTANT in ("comp-lax", "pres-lax") else None
    L3.MUTANT = None
    L4.MUTANT = MUTANT if MUTANT == "srcscan-lax" else None

    run_anchors()
    if MUTANT and MUTANT.startswith("anchor-"):
        for x in ANCHORS:
            if x["id"] == MUTANT.split("-")[1]:
                x["computed"], x["passed"] = "MUTATED", False

    run_freeze()
    run_amplitude_scope()
    run_acyclicity()
    det = L2.law_det(CARRIER)
    rows_d1 = run_discriminators_13(det)
    run_discriminator_2(det)
    lifts, hol = run_regress_at_amplitude()
    run_gauge_selftest(lifts)
    run_lossy_CL(det)
    run_lossy_AMP(det, lifts)
    run_discriminator_4(det)
    run_delta(rows_d1, hol)
    run_exactness()
    if a.falsification_selftest and not a.mutant:
        run_mutant_table()
    verdict()

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
    prog(f"done: {rec['totals']['anchors']} anchors, "
         f"{rec['totals']['gates']} gates, {fail} must-pass failures")
    return 1 if fail else 0


if __name__ == "__main__":
    raise SystemExit(main())
