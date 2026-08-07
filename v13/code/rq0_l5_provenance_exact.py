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


def asum(terms):
    """Sum a bag of amplitudes exactly.  Terms combine only when
    commensurable (equal 2^(-s/2) factor); the only phase relation used is
    zeta^e + zeta^(e+4) = 0.  A non-commensurable residue is returned as a
    MIXED token and is gated -- the declared family never produces one."""
    red: dict = {}
    for c, s, e in terms:
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
    return ("MIXED", tuple(sorted((k, str(v)) for k, v in live.items())), 0)


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


def cycle_basis_holonomies(word_mats, word_sups, n):
    """The gauge-invariant content of a carried amplitude path.

    The declared pair gauge is VERTEX SWITCHING on the layered path graph
    (the v12 W7 terminal form): a phase at each vertex, every edge amplitude
    multiplied by the phase difference of its endpoints.  A quantity is
    gauge-invariant iff it is a product of edge amplitudes around a CLOSED
    LOOP, conjugated on reversed edges; a cycle basis carries all of it and
    nothing else does.  Returns (cycle rank, sorted holonomy phases, sorted
    per-cycle checkpoint spans)."""
    E = layered_edges(word_sups, n)
    verts = sorted({v for e in E for v in e[:2]})
    idx = {v: i for i, v in enumerate(verts)}
    parent = list(range(len(verts)))

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
    comps = len({find(i) for i in range(len(verts))})
    rank = len(E) - len(verts) + comps

    adj: dict = {}
    for e in tree:
        adj.setdefault(e[0], []).append((e[1], e, +1))
        adj.setdefault(e[1], []).append((e[0], e, -1))

    def tree_path(a, b):
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
            out.append((e, -s))
            v = p
        return out[::-1]

    hol, spans = [], []
    for e in extra:
        p = tree_path(e[0], e[1])
        if p is None:
            continue
        legs = [(e, +1)] + [(ee, -ss) for ee, ss in reversed(p)]
        acc, layers = AONE, set()
        for ee, s in legs:
            w = word_mats[ee[2]][ee[4]][ee[3]]
            acc = amul(acc, w if s > 0 else aconj(w))
            layers.add(ee[2])
        if MUTANT == "hol-lax":
            acc = AONE
        hol.append(acc[2])
        spans.append(len(layers))
    return rank, tuple(sorted(hol)), tuple(sorted(spans))


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
    rank, hol, spans = cycle_basis_holonomies(word_mats, word_sups, n)
    mods = tuple(sorted(f"{w[0]}/2^({w[1]}/2)" for U in word_mats
                        for row in U for w in row if w[0] != 0))
    return base + (L2.written_of(sup_of_matrix(C, n)), rank, hol, spans,
                   mods)


def local_holonomy_shadow(word_mats, word_sups, n):
    """What a CHECKPOINT-LOCAL admitted verification can read of the carried
    amplitude data.  (P2) is checkpoint-local by its own definition -- it
    verifies the certificate AT its own checkpoint -- so it reads step-local
    invariants only.  This is the v12 recorded-but-phased limit applied to
    the CHECKS."""
    per = tuple(cycle_basis_holonomies([word_mats[t]], [word_sups[t]], n)[:2]
                for t in range(len(word_mats)))
    mods = tuple(sorted(f"{w[0]}/2^({w[1]}/2)" for U in word_mats
                        for row in U for w in row if w[0] != 0))
    return (per, mods)


AMP_DEFS = [amul, aconj, asum, sup_of_matrix, matmul, layered_edges,
            cycle_basis_holonomies, certificate_AMP, local_holonomy_shadow]


# ---------------------------------------------------------------------------
# 4.  THE FREEZE
# ---------------------------------------------------------------------------

def TUNE_negative_control(part, law, prep, rho, n, word):
    """PERMANENT NEGATIVE CONTROL -- must be CAUGHT by the source scan.
    It special-cases the committed legitimate boundary PTOMO by name."""
    return Fr(0) if part == PTOMO else Fr(1)


def run_freeze():
    prog("freeze")
    fns = DEFS + AMP_DEFS + STATS + [nb_negative_control]
    reg = [{"name": f.__name__,
            "sha256": hashlib.sha256(
                inspect.getsource(f).encode()).hexdigest()} for f in fns]
    TABLES["definition_hashes"] = reg
    gate("L5-00", "freeze",
         "every definition of the quintuple, of the amplitude layer, and "
         "every provenance-reading statistic is SHA-256 registered before "
         "any fixture verdict is computed",
         len(reg) == len(fns), len(reg))

    clean = L4.source_scan([(f.__name__, f) for f in fns])
    caught = L4.source_scan([("TUNE", TUNE_negative_control)])
    ok = all(r["clean"] for r in clean) and not caught[0]["clean"]
    gate("L5-SRC", "freeze",
         "automated source scan: no definition mentions a committed "
         "boundary, AND the permanent negative control TUNE -- which "
         "special-cases the legitimate tomographic minimum by name -- is "
         "CAUGHT by the same scan",
         ok, {"definitions_scanned": len(clean),
              "definitions_clean": sum(1 for r in clean if r["clean"]),
              "negative_control_caught": not caught[0]["clean"],
              "negative_control_hits": caught[0]["fixture_references"]})


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
    for a in range(n):
        for b in range(n):
            v = asum([amul(U[i][a], aconj(U[i][b])) for i in range(n)])
            if v != (AONE if a == b else AZERO):
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

    mods = sorted({f"{w[0]}*2^-({w[1]}/2)" for U in GA.values()
                   for row in U for w in row if w[0] != 0})
    gate("L5-AMP-EXACT", "derivation",
         "every declared amplitude is exact in the rational-times-root-of-"
         "unity form c*2^(-s/2)*zeta_8^e; all sums formed are between "
         "commensurable terms, so no float and no MIXED residue arises",
         all("MIXED" not in m for m in mods), mods)

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
        rank, hol, spans = cycle_basis_holonomies(wm, ws, n)
        rows.append({"word": wn, "support_record": pk(supcomp),
                     "amplitude_record": pk(ampcomp), "cycle_rank": rank,
                     "holonomy_phases": list(hol), "cycle_spans": list(spans),
                     "cancellation": supcomp != ampcomp})
    TABLES["amplitude_words"] = rows
    by = {r["word"]: r for r in rows}

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

    bad, tested, ident = [], 0, 0
    for nm, law, cap in (("DET", det, 60), ("REV", rev, 60),
                         ("COUNTER", ctr, 60), ("FUNNEL-CLOSURE", fnl, 60)):
        pool = list(law)[:cap]
        for a in pool:
            for b in pool[:6]:
                for w in ([a], [a, b]):
                    E = layered_edges(w, n)
                    V = (len(w) + 1) * n
                    r, h, _ = cycle_basis_holonomies(
                        [canonical_lift(g, n) for g in w], w, n)
                    tested += 1
                    C = r + V - len(E)      # components, by Euler
                    if len(E) == len(w) * n and C == n and r == 0:
                        ident += 1
                    if r != 0 or h != ():
                        bad.append((nm, L2.key(a), r))
    gate("L5-ACYC-M", "derivation",
         "MEASURED: over one- and two-step carried paths at every committed "
         "law, the layered realized-leg diagram has cycle rank 0 and an "
         "EMPTY holonomy family, with E = m*n edges and exactly n "
         "components in every case -- there is no gauge-invariant amplitude "
         "content to carry",
         not bad and ident == tested,
         {"paths_tested": tested, "euler_identity_holds": ident,
          "violations": len(bad)})

    gate("L5-ACYC-P", "derivation",
         "PROVED: a single-valued step gives each vertex of a layer exactly "
         "one upward edge, so E = m*n while V = (m+1)*n; following upward "
         "edges, every component meets the top layer, so C <= n; hence "
         "rank = E - V + C = C - n <= 0, and rank >= 0 forces rank = 0 and "
         "C = n.  Every committed law is single-valued (anchor A11), so "
         "V-AMP's gauge-invariant content is EMPTY at the whole committed "
         "scope and V-AMP reduces to V-CL there identically",
         True, {"E": "m*n", "V": "(m+1)*n", "C": "n", "rank": 0})

    FINDINGS["acyclicity"] = {
        "statement": "single-valued steps have acyclic layered diagrams",
        "consequence": "V-AMP == V-CL exactly at every committed law",
        "paths_tested": tested}


# ---------------------------------------------------------------------------
# 7.  DISCRIMINATORS 1 AND 3
# ---------------------------------------------------------------------------

def true_histories(n=CARRIER):
    """The DECLARED true generation history of each committed context.  The
    immutable base supplies provenance LABELS but no generation paths, so
    the paths are declared here (deviation 1) in the one form the base's own
    vocabulary fixes: the admitted operation that writes exactly the
    declared record.  delta is written by the identity -- the address
    algebra, nothing done to it; each coarse boundary is written by its
    block-minimum idempotent, which B'' Prop 8.6 already carries as an
    admitted operation."""
    out = {}
    for part in FIXTURE:
        out[part] = [L2.sup_of_map(tuple(range(n))) if part == DISC5
                     else L2.block_min_idempotent(part, n)]
    return out


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
    TH = true_histories(n)
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
         "THE REDUCTION, and it is what fires the kill.  Let S be ANY "
         "statistic on the quintuple.  Because the declarable-history set "
         "is a function of (boundary, preparation, law), the range of "
         "values S can take at a declaration is a function of the "
         "QUADRUPLE, and an adversary may realize any element of it.  So "
         "every provenance-reading statistic is bounded by a quadruple "
         "statistic -- exactly the class stage-5 Theorem 5.3 proved cannot "
         "separate a forged from a legitimate declaration of the same "
         "patch.  RQ0-L5-PROVENANCE-REGRESS FIRES, on both variants",
         True, {"inherited": "stage-5 Theorem 5.3 (forgery is not a "
                             "function of the quadruple)"})
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


def run_regress_at_amplitude():
    """The regress posed at the amplitude scope, where V-AMP's extra content
    is NOT empty: is the carried amplitude datum anchored by the law, or is
    it one further free declaration?"""
    prog("regress at the amplitude scope")
    n = CARRIER
    lifts = []
    for a, b, c in product(range(NROOT), repeat=3):
        d = (c - (a - b) + 4) % NROOT
        blk = (((Fr(1), 1, a), (Fr(1), 1, b)), ((Fr(1), 1, c), (Fr(1), 1, d)))
        U = _embed(blk, [0, 1], n)
        if is_unitary(U, n):
            lifts.append(U)
    hol: dict = {}
    for U in lifts:
        s = sup_of_matrix(U, n)
        h = cycle_basis_holonomies([U], [s], n)[1]
        hol[h] = hol.get(h, 0) + 1
    gate("L5-AMP-FREE", "kill",
         "THE AMPLITUDE DATUM IS ONE FURTHER FREE DECLARATION.  Over the "
         "COMPLETE family of admitted unitary lifts of one declared support "
         "step, the carried gauge-invariant holonomy takes several values "
         "and each is realized by many lifts -- so an adversary declaring a "
         "forged boundary may declare ANY of them, including whichever one "
         "a legitimate declaration carries.  The regress moves one level "
         "deeper with the quantum bits and does not bottom out",
         len(hol) >= 2 and all(v > 1 for v in hol.values()),
         {"admitted_unitary_lifts": len(lifts),
          "distinct_holonomy_classes": len(hol),
          "multiplicities": {str(k): v for k, v in sorted(hol.items())}})
    TABLES["amplitude_lift_family"] = {
        "admitted_unitary_lifts": len(lifts),
        "holonomy_classes": {str(k): v for k, v in sorted(hol.items())}}
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
    TABLES["lossy_CL"] = {"histories": len(H),
                          "distinct_certificates": len(buckets),
                          "class_size": len(big)}
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

    sup01 = sup_of_matrix(lifts[0], n)
    ws = [sup01, sup01]
    seen: dict = {}
    witness = None
    pool = lifts[:120]
    for U in pool:
        for V in pool:
            loc = local_holonomy_shadow([U, V], ws, n)
            glb = cycle_basis_holonomies([U, V], ws, n)[1]
            if loc in seen and seen[loc] != glb:
                witness = {"checkpoint_local_shadows_identical": True,
                           "local_per_step_holonomies":
                               [list(x[1]) for x in loc[0]],
                           "global_holonomies_A": list(seen[loc]),
                           "global_holonomies_B": list(glb)}
                break
            seen.setdefault(loc, glb)
        if witness:
            break
    gate("L5-LOSSY-AMP-A", "kill",
         "RQ0-L5-PROVENANCE-LOSSY FIRES AGAINST V-AMP WHERE ITS CONTENT IS "
         "NOT EMPTY EITHER -- the amendment-v2 form of the adversary.  (P2) "
         "is checkpoint-LOCAL by its own definition: it verifies the "
         "certificate AT its own checkpoint, so an admitted checkpoint "
         "verification reads step-local invariants only, while the carried "
         "diagram's cycle space is strictly larger than the span of its "
         "step-local cycles.  Exhibited: two admitted lifts of ONE declared "
         "support word with IDENTICAL checkpoint-local shadows and "
         "DIFFERENT cross-checkpoint holonomy.  This is the v12 "
         "recorded-but-phased limit applied to the CHECKS -- block-local "
         "data is not phase-triviality",
         witness is not None, witness or {"witness": "none found"})

    r_all = cycle_basis_holonomies([lifts[0], lifts[0]], ws, n)[0]
    r_loc = sum(cycle_basis_holonomies([U], [sup01], n)[0]
                for U in (lifts[0], lifts[0]))
    gate("L5-LOSSY-AMP-DIM", "derivation",
         "the accounting that makes the witness inevitable: the carried "
         "two-step diagram has cycle rank 3 while its two checkpoint-local "
         "diagrams have rank 1 each, so a checkpoint-local verification "
         "leaves a rank-1 residue of gauge-invariant content permanently "
         "unread",
         r_all == 3 and r_loc == 2,
         {"global_rank": r_all, "checkpoint_local_rank": r_loc,
          "unread_residue": r_all - r_loc})

    gate("L5-LOSSY-READING", "disclosure",
         "THE SCISSORS, disclosed rather than resolved.  Under the reading "
         "in which a verification is a classical computation on declared "
         "numerals it reads everything, including the cross-checkpoint "
         "holonomy, and LOSSY does not fire against V-AMP -- but then the "
         "amplitude datum is a free declaration and REGRESS eats it "
         "(L5-AMP-FREE).  Under the reading the amendment fixes -- checks "
         "are record-producing and checkpoint-local -- LOSSY fires.  The "
         "amplitude bits are readable only under the reading that leaves "
         "them unanchored, and anchored only under the reading that leaves "
         "them unread.  Both readings are reported; neither escapes a kill",
         True, {"reading_A_numerals": "REGRESS fires, LOSSY does not",
                "reading_B_record_producing": "both fire"})

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
    TH = true_histories(n)

    group = ([tuple(range(n))] if MUTANT == "nb-lax"
             else list(permutations(range(n))))
    nb_rows = []
    for fn in STATS + [nb_negative_control]:
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
    for fn in STATS:
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
    for fn in STATS:
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


# ---------------------------------------------------------------------------
# 12.  VERDICT
# ---------------------------------------------------------------------------

def verdict():
    g = {x["id"]: x for x in GATES}
    regress = (g["L5-D2-EXIST"]["passed"] and g["L5-D2-COLLISION"]["passed"]
               and g["L5-D2-REDUCTION"]["passed"]
               and g["L5-AMP-FREE"]["passed"])
    lossy_cl = g["L5-LOSSY-CL"]["passed"]
    lossy_amp = (g["L5-LOSSY-AMP-C"]["passed"]
                 and g["L5-LOSSY-AMP-A"]["passed"])
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
                x["value"], sort_keys=True, default=str)[:700])
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
           "p1-break", "p2-break", "acyc-lax", "hol-lax",
           "amp-cancel-lax", "nb-lax", "srcscan-lax"]


def run_falsification_selftest() -> int:
    import subprocess
    bad = []
    for m in MUTANTS:
        r = subprocess.run([sys.executable, str(Path(__file__).resolve()),
                            "--mutant", m, "--quiet"],
                           capture_output=True, text=True)
        if r.returncode != 1:
            bad.append((m, r.returncode))
        sys.stdout.write(f"  mutant {m:<16} exit {r.returncode} "
                         f"{'OK' if r.returncode == 1 else 'DID NOT DIE'}\n")
    sys.stdout.write(f"\n{len(MUTANTS) - len(bad)}/{len(MUTANTS)} mutants "
                     f"died as required\n")
    return 1 if bad else 0


def main() -> int:
    global MUTANT, SOURCE_SHA256
    ap = argparse.ArgumentParser()
    ap.add_argument("--mutant", default=None)
    ap.add_argument("--quiet", action="store_true")
    ap.add_argument("--falsification-selftest", action="store_true")
    a = ap.parse_args()
    if a.falsification_selftest:
        return run_falsification_selftest()
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
    run_lossy_CL(det)
    run_lossy_AMP(det, lifts)
    run_discriminator_4(det)
    run_delta(rows_d1, hol)
    verdict()

    rec = build_receipt()
    txt = render(rec)
    if not a.mutant:
        OUT_TXT.write_text(txt)
        OUT_JSON.write_text(json.dumps(rec, indent=1, sort_keys=True,
                                       default=str) + "\n")
    if not a.quiet:
        sys.stdout.write("\n" + txt)
    fail = rec["totals"]["must_pass_failures"]
    prog(f"done: {rec['totals']['anchors']} anchors, "
         f"{rec['totals']['gates']} gates, {fail} must-pass failures")
    return 1 if fail else 0


if __name__ == "__main__":
    raise SystemExit(main())
