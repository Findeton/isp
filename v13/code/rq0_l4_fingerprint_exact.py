#!/usr/bin/env python3
"""RQ0-L4 branch C -- THE NOMOLOGICAL FINGERPRINT HUNT.

Executes the frozen pin `v13/note-rq0-l4-nomological-fingerprint-pin.md`
(commit b4fc87c) against the immutable stage-5 TERMINAL base (a5cb096).

THE QUESTION.  Does the law itself remember what forgetting erased?  Is
there a statistic on declared data -- evaluated, where the candidate demands
it, at COUNTERFACTUAL arguments the law admits -- that separates the
LEGITIMATE tomographic coarse patch from the FORGED 2+1+1 and 2+2 patches,
robustly?  The terminal cycle proved no statistic separates two declarations
of the SAME quadruple (a collision witnesses it); the committed pairs here
are of DISTINCT quadruple, which the terminal cycle left open.

THE DISCIPLINE THIS FILE ENFORCES (RUNBOOK sec 13(4)).  Every candidate is
DECLARED, its source text SHA-256-registered, and gated for corridor
membership BEFORE any fixture value is computed.  The corridor gates decide
on an OFF-FIXTURE population -- the 48 records of the committed carrier that
are not one of the four committed boundaries.  The freeze is warranted by
TWO checks that work: the definition hashes of L4-00, which bind the receipt
to inspectable source, and the AUTOMATED SOURCE SCAN of L4-SRC, which
verifies that no candidate definition mentions any committed boundary.  What
the gate ORDER cannot certify is disclosed rather than claimed: the
covariance and name-blindness gates are orbit properties, so they evaluate
candidates at relabelled arguments, and some of those images ARE committed
boundaries -- counted exactly by L4-IMG, and harmless because every such
value is equality-tested against its own off-fixture partner and none is
retained, thresholded or used in any selection.

THE NAME-BLINDNESS PRINCIPLE (L4-NB).  A statistic must be a function of
LABEL-FREE invariants: relabelling the carrier throughout the declared datum
-- boundary, law, preparation and state together -- may not move its value.
Covariance (the stabilizer of the declared data) has no content where that
stabilizer is trivial; name-blindness has content everywhere, and it is the
corpus's own co-reference discipline, under which names are never compared.

Orientation is fixed to the corpus's own defect semantics (stage-5
Definition 2.2(b)): a patch is admitted when the statistic is SMALL, so a
candidate separates iff the legitimate patch is STRICTLY BELOW both forged
ones.  A candidate wanting the other direction declares the negated form as
its definition, which C4c does.

Exact arithmetic throughout.  Anchors exit 1 on mismatch and never on a
substantive negative.  `--mutant NAME` breaks exactly one anchor or one
derivation step and must exit 1.  No wall-clock value enters the receipt or
the rendered output, so two runs of the same source produce byte-identical
artifacts.

Scope: finite; ONE committed carrier of five configurations; the committed
law families and the 687-law census at three; "coarse" is algebra-relative
only.  No locality, topology, causality, spacetime, field, QFT or gravity
object is constructed or claimed.
"""

from __future__ import annotations

import argparse
import hashlib
import inspect
import json
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from fractions import Fraction as Fr
from itertools import combinations, permutations, product
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import rq0_l0_fixed_point_exact as CB    # Cycle B TERMINAL machinery
import rq0_l1_composite_exact as CBP     # Cycle B' TERMINAL machinery
import rq0_l2_admissibility_exact as L2  # Cycle B" TERMINAL machinery
import rq0_l3_epsilon_exact as L3        # stage-5 TERMINAL machinery

SCHEMA = "rq0-l4-nomological-fingerprint-receipt-v1"
PIN_COMMIT = "b4fc87c"
BASE_COMMIT = "a5cb096"
OUT_TXT = HERE / "rq0_l4_fingerprint_output.txt"
OUT_JSON = HERE / "rq0_l4_fingerprint_receipt.json"

T0 = time.time()
MUTANT: str | None = None
SOURCE_SHA256 = ""

GATES: list[dict] = []
ANCHORS: list[dict] = []
TABLES: dict = {}
FINDINGS: dict = {}

CARRIER = 5
PREP_FULL = frozenset(range(CARRIER))
RHO = L2.RHO                        # the committed branch-memory state
RHO_AMNESTY = (Fr(1, 2), Fr(0), Fr(1, 2), Fr(0), Fr(0))   # stage-5 sec 5.4
RHO_REL = (Fr(3, 4), Fr(1, 16), Fr(1, 16), Fr(1, 16), Fr(1, 16))  # R1's
                                    # relabelled state: the committed state
                                    # with the marked configuration moved
PI1 = ((0, 1), (2,), (3,), (4,))    # the forged aligned manufactured 2+1+1
P22 = ((0, 1), (2, 3), (4,))        # the forged aligned manufactured 2+2
PTOMO = ((0, 1, 2, 3), (4,))        # the LEGITIMATE corrected tomographic min
DISC5 = CB.discrete(5)
ONEATOM5 = ((0, 1, 2, 3, 4),)       # total erasure, the diagnostic boundary
FIXTURE = (PI1, P22, PTOMO, DISC5)
PROVENANCE = {PI1: "FORGED", P22: "FORGED", PTOMO: "LEGITIMATE",
              DISC5: "LEGITIMATE"}


def prog(msg: str) -> None:
    sys.stdout.write(f"[{time.time() - T0:7.1f}s] {msg}\n")
    sys.stdout.flush()


# --------------------------------------------------------------------------
# 0.  Gates, anchors, and the freeze-barrier provenance flags.
# --------------------------------------------------------------------------

_TOUCHED_FIXTURE = False            # THE FIXTURE-STAGE ANNOTATION.  Set at
                                    # the stage boundary and at L4-COV2.  It
                                    # is an AUTHOR-DECLARED annotation of
                                    # which stage a gate belongs to, NOT an
                                    # instrumented detector of evaluation:
                                    # the orbit gates evaluate candidates at
                                    # relabelled images without setting it,
                                    # which is why L4-IMG counts those
                                    # directly and the barrier does not
                                    # claim they did not happen.


def touch(part) -> None:
    global _TOUCHED_FIXTURE
    if part in FIXTURE:
        _TOUCHED_FIXTURE = True


def gate(gid: str, cls: str, claim: str, ok: bool, value=None,
         must_pass: bool = False) -> bool:
    """A gate records a claim, its verdict, and the author-declared stage it
    fired in.  `must_pass` marks gates whose failure exits 1.  Corridor and
    fixture findings are substantive and exit 0."""
    GATES.append({"id": gid, "class": cls, "claim": claim, "passed": bool(ok),
                  "must_pass": bool(must_pass), "value": value,
                  "fixture_stage_declared_when_fired": _TOUCHED_FIXTURE})
    return bool(ok)


def anchor(aid: str, source: str, quantity: str, committed, computed) -> None:
    """Exit-1-only.  Every terminal value this unit reuses is reproduced by
    this unit's own route and compared here."""
    if MUTANT == f"anchor:{aid}":
        computed = "MUTANT"
    ok = (committed == computed)
    ANCHORS.append({"id": aid, "source": source, "quantity": quantity,
                    "committed": committed, "computed": computed,
                    "passed": bool(ok)})
    if not ok:
        sys.stdout.write(
            f"\nANCHOR FAILURE {aid}: {quantity}\n"
            f"  committed ({source}): {committed!r}\n"
            f"  computed here      : {computed!r}\n")
        sys.stdout.flush()
        raise SystemExit(1)


def S(x) -> str:
    return str(x)


# --------------------------------------------------------------------------
# 1.  PRIMITIVES, on this unit's own routes.
# --------------------------------------------------------------------------


_PRES: dict = {}
_PKEY: dict = {}
_SUCC: dict = {}
_EPS: dict = {}
_STAB: dict = {}


def my_pres(law, part):
    """Pres_L(pi): the admitted operations whose images of distinct declared
    blocks are pairwise disjoint.  Own route; gated equal to B"'s.  Memoized
    on the declared law object and the declared boundary -- the memo is a
    speed device only and changes no value."""
    k = (id(law), part)
    if k in _PRES:
        return _PRES[k]
    if MUTANT == "pres-lax":
        _PRES[k] = list(law)
        return _PRES[k]
    out = []
    for F in law:
        seen: list = []
        ok = True
        for r in part:
            img = frozenset().union(*[F[j] for j in r])
            if any(img & s for s in seen):
                ok = False
                break
            seen.append(img)
        if ok:
            out.append(F)
    _PRES[k] = out
    return out


def pres_key(law, part):
    k = (id(law), part)
    if k not in _PKEY:
        _PKEY[k] = _famkey(my_pres(law, part))
    return _PKEY[k]


def succ_of(law, part, n: int):
    """The declared family's realized successor map: succ(j) is everything
    the realized legs of the declared family can occupy from j.  Reach is its
    closure, so reach at every declared preparation costs one closure."""
    k = (id(law), part)
    if k not in _SUCC:
        fam = my_pres(law, part)
        _SUCC[k] = tuple(frozenset().union(*[F[j] for F in fam])
                         if fam else frozenset() for j in range(n))
    return _SUCC[k]


def eps_at(law, part, rho):
    k = (id(law), part, rho)
    if k not in _EPS:
        _EPS[k] = my_eps(part, my_pres(law, part), rho)
    return _EPS[k]


def stab_of(name, law, rho, prep, n):
    k = (name, rho, tuple(sorted(prep)))
    if k not in _STAB:
        _STAB[k] = stabilizer(law, rho, prep, n)
    return _STAB[k]


def my_ker(fam, n: int):
    """ker(F): configurations merged exactly when NO declared task separates
    them.  The generated coarse structure, i.e. what the law itself makes
    indistinguishable."""
    if MUTANT == "ker-lax":
        return CB.indiscrete(n)
    if not fam:
        return CB.indiscrete(n)
    sig: dict = {}
    for j in range(n):
        sig.setdefault(tuple(tuple(sorted(F[j])) for F in fam), []).append(j)
    return tuple(sorted(tuple(sorted(v)) for v in sig.values()))


def my_reach(fam, prep, n: int):
    """The reachable subprocess: the declared preparation closed under the
    realized legs of the declared family.  An ORDER ON CONFIGURATIONS."""
    if MUTANT == "reach-lax":
        return set(range(n))
    R, growing = set(prep), True
    while growing:
        growing = False
        for F in fam:
            for j in sorted(R):
                for l in F[j]:
                    if l not in R:
                        R.add(l)
                        growing = True
    return R


def my_eps(part, fam, rho):
    """The concordance defect eps = max_F d(F, pi, rho), stage-5 Def 2.1."""
    if MUTANT == "eps-lax":
        return Fr(0)
    worst = Fr(0)
    for F in fam:
        tot = Fr(0)
        for r in part:
            pr = sum((rho[j] for j in r), Fr(0))
            mx = Fr(0)
            for s in range(len(rho)):
                v = sum((rho[j] * Fr(1, len(F[j])) for j in r if s in F[j]),
                        Fr(0))
                if v > mx:
                    mx = v
            tot += pr - mx
        if tot > worst:
            worst = tot
    return worst


def reach_from_succ(succ, prep):
    """The same reachable subprocess by the successor route: one closure per
    declared preparation instead of one saturation pass per admitted task."""
    if MUTANT == "reach-lax":
        return set(range(len(succ)))
    R, stack = set(prep), list(prep)
    while stack:
        j = stack.pop()
        for l in succ[j]:
            if l not in R:
                R.add(l)
                stack.append(l)
    return R


def my_omega(part, fam, prep, rho, n):
    """The occupancy defect: the committed state's probability of a record
    outcome the patch's own realized process never produces.  Reference
    route, over the declared family directly."""
    R = my_reach(fam, prep, n)
    return sum((sum((rho[j] for j in r), Fr(0))
                for r in part if not (set(r) & R)), Fr(0))


def omega_fast(part, law, prep, rho, n):
    """The same defect by the successor route.  Gated equal to the reference
    route and to the terminal one (L4-X6)."""
    R = reach_from_succ(succ_of(law, part, n), prep)
    return sum((sum((rho[j] for j in r), Fr(0))
                for r in part if not (set(r) & R)), Fr(0))


def preps_of(n: int):
    return [frozenset(s) for k in range(1, n + 1)
            for s in combinations(range(n), k)]


def level_partition(rho):
    """The declared state's LEVEL PARTITION: configurations of equal declared
    mass.  This is the state's own symmetry data and nothing else."""
    if MUTANT == "levelset-lax":
        return tuple((j,) for j in range(len(rho)))
    sig: dict = {}
    for j, v in enumerate(rho):
        sig.setdefault(v, []).append(j)
    return tuple(sorted(tuple(sorted(v)) for v in sig.values()))


def saturated_atoms(part, lam):
    """Which declared atoms are unions of lam-classes.  Route 1: per-atom
    membership test."""
    cls = {j: c for c in lam for j in c}
    return tuple(all(set(cls[j]) <= set(r) for j in r) for r in part)


def saturated_atoms_route2(part, lam):
    """Route 2, independent: an atom is lam-saturated iff its lam-closure --
    the union of the classes it meets -- is itself."""
    out = []
    for r in part:
        clo: set = set()
        for c in lam:
            if set(c) & set(r):
                clo |= set(c)
        out.append(clo == set(r))
    return tuple(out)


def reach_classes(law, part, n: int):
    """The law's own reachability classes: j ~ k iff the realized process
    started at j occupies exactly what it occupies started at k."""
    succ = succ_of(law, part, n)
    sig: dict = {}
    for j in range(n):
        sig.setdefault(tuple(sorted(reach_from_succ(succ, frozenset({j})))),
                       []).append(j)
    return tuple(sorted(tuple(sorted(v)) for v in sig.values()))


def shape_invariant(part, rho):
    """THE CANDIDATE COMPLETE COVARIANT INVARIANT of a declared boundary at a
    declared state: the multiset over declared atoms of the atom's profile
    across the state's level classes.  Gated below to be exactly the orbit
    invariant of the admitted-isomorphism action."""
    if MUTANT == "shape-lax":
        return ()
    lam = level_partition(rho)
    return tuple(sorted(tuple(len(set(r) & set(c)) for c in lam)
                        for r in part))


_ACT: dict = {}


def act_part(part, sigma):
    """The admitted relabelling sigma acting on a declared boundary.
    Memoized on (boundary, relabelling); the memo is a speed device only and
    changes no value."""
    k = (part, sigma)
    if k not in _ACT:
        _ACT[k] = tuple(sorted(tuple(sorted(sigma[j] for j in r))
                               for r in part))
    return _ACT[k]


def act_law(law, sigma):
    """sigma . L = { sigma F sigma^-1 }, on sector supports."""
    inv = [0] * len(sigma)
    for j, s in enumerate(sigma):
        inv[s] = j
    return set(tuple(tuple(sorted(sigma[l] for l in law_F[inv[j]]))
                     for j in range(len(sigma))) for law_F in law)


def stabilizer(law, rho, prep, n: int):
    """THE ADMITTED ISOMORPHISMS of the declared data: carrier relabellings
    fixing the declared state, the declared law (setwise) and the declared
    preparation.  Measured, never assumed."""
    if MUTANT == "stab-lax":
        return [tuple(p) for p in permutations(range(n))]
    key0 = set(tuple(tuple(sorted(s)) for s in F) for F in law)
    out = []
    for p in permutations(range(n)):
        if any(rho[p[j]] != rho[j] for j in range(n)):
            continue
        if frozenset(p[j] for j in prep) != frozenset(prep):
            continue
        if act_law(law, p) != key0:
            continue
        out.append(tuple(p))
    return out


def orbits_of(parts, group):
    """Orbits of the declared boundaries under the admitted isomorphisms."""
    if MUTANT == "orbit-lax":
        return [tuple(sorted(parts))]
    seen: set = set()
    out = []
    for p in parts:
        if p in seen:
            continue
        orb = sorted({act_part(p, g) for g in group})
        for q in orb:
            seen.add(q)
        out.append(tuple(orb))
    return out


# --------------------------------------------------------------------------
# 1b.  THE FULL RELABELLING ACTION, on the WHOLE declared datum.  Covariance
#      is invariance under the stabilizer of the declared data; NAME-BLINDNESS
#      is invariance under all 120 relabellings acting on boundary, law,
#      preparation and state TOGETHER.  Where the stabilizer is trivial the
#      first has no content and the second still does.
# --------------------------------------------------------------------------


SYM5 = [tuple(p) for p in permutations(range(5))]
_LAWREG: dict = {}


def law_key_of(law):
    return tuple(sorted(tuple(tuple(sorted(s)) for s in F) for F in law))


def register_law(law):
    """Canonicalise a law object through a registry, so that a relabelling
    which fixes the family returns the ORIGINAL object.  The memos then hit;
    no value depends on the memo."""
    k = law_key_of(law)
    if k not in _LAWREG:
        _LAWREG[k] = law
    return _LAWREG[k]


def act_law_obj(law, sigma):
    """sigma . L as a LAW OBJECT: the same family read in relabelled names,
    (sigma.F)[sigma j] = sigma(F[j])."""
    n = len(sigma)
    inv = [0] * n
    for j, s in enumerate(sigma):
        inv[s] = j
    return register_law([tuple(frozenset(sigma[l] for l in F[inv[j]])
                               for j in range(n)) for F in law])


def act_prep(prep, sigma):
    return frozenset(sigma[j] for j in prep)


def act_rho(rho, sigma):
    inv = [0] * len(sigma)
    for j, s in enumerate(sigma):
        inv[s] = j
    return tuple(rho[inv[j]] for j in range(len(sigma)))


_CVAL: dict = {}


def cval(cid, fn, part, law, prep, rho, n=5):
    """A memoized candidate evaluation, used by the relabelling gates only.
    Keyed on the canonical law object, so the memo is a speed device and
    changes no value."""
    k = (cid, id(law), part, prep, rho)
    if k not in _CVAL:
        _CVAL[k] = fn(part, law, prep, rho, n)
    return _CVAL[k]


def name_blind(cid, fn, law, records, group=None):
    """G-NB, THE NAME-BLINDNESS GATE.  Is the candidate a function of
    LABEL-FREE invariants?  Tested exhaustively: for every declared record in
    `records` and every one of the 120 carrier relabellings, the value at the
    RELABELLED declared datum -- boundary, law, preparation and state moved
    together -- must equal the value at the original.  A statistic that
    compares carrier NAMES fails; one built from declared structure cannot."""
    if MUTANT == "nb-lax":
        group = [tuple(range(5))]
    base = {p: cval(cid, fn, p, law, PREP_FULL, RHO) for p in records}
    hits = 0
    for sig in (group if group is not None else SYM5):
        lw = act_law_obj(law, sig)
        pr = act_prep(PREP_FULL, sig)
        rh = act_rho(RHO, sig)
        for p in records:
            q = act_part(p, sig)
            if q in FIXTURE:
                hits += 1
            if cval(cid, fn, q, lw, pr, rh) != base[p]:
                return False, {"relabelling": list(sig), "record": S(p)}, hits
    return True, None, hits


def fixture_images(records, group):
    """How many (record, relabelling) pairs of an orbit gate land ON a
    committed boundary -- the evaluations the gate ORDER cannot avoid, since
    covariance and name-blindness are orbit properties.  Reported, per
    boundary, by L4-IMG."""
    out: dict = {}
    for p in records:
        for g in group:
            q = act_part(p, g)
            if q in FIXTURE:
                out[S(q)] = out.get(S(q), 0) + 1
    return out


FIXTURE_TOKENS = ["PI1", "P22", "PTOMO", "DISC5", "ONEATOM5", "FIXTURE",
                  "PROVENANCE"]


def source_scan(fns):
    """THE CHECK THAT WORKS.  An automated scan of each declared definition's
    own source text for any reference to a committed boundary.  This, with
    the definition hashes of L4-00, is what the freeze rests on: the hashes
    bind the receipt to inspectable source, and the scan inspects it."""
    out = []
    for label, fn in fns:
        src = inspect.getsource(fn)
        if MUTANT == "srcscan-lax":
            src = ""
        found = sorted({t for t in FIXTURE_TOKENS if t in src})
        out.append({"definition": label, "fixture_references": found,
                    "clean": not found})
    return out


# --------------------------------------------------------------------------
# 2.  ANCHORS.  Every terminal value reused, reproduced by this unit.
# --------------------------------------------------------------------------


def run_anchors():
    prog("anchors: stage-5 TERMINAL, Cycle B/B'/B\" committed values")
    committed_laws5()
    det = LAW5["DET"]

    anchor("A01", "Cycle B sec 4 (Bell triangle)",
           "record-lattice sizes at 1..5 configurations", [1, 2, 5, 15, 52],
           [CB.bell(n) for n in (1, 2, 3, 4, 5)])
    anchor("A02", "Cycle B Thm 4.4 / B\" M32",
           "DET and REV cardinalities at five configurations", [3125, 120],
           [len(det), len(L2.law_rev(5))])
    anchor("A03", "stage-5 Thm 4.1 / B\" sec 6",
           "Pres under DET at the forged 2+1+1, the forged 2+2, the "
           "legitimate tomographic minimum and the carrier's own algebra",
           [240, 420, 1280, 120],
           [len(my_pres(det, p)) for p in (PI1, P22, PTOMO, DISC5)])
    anchor("A04", "stage-5 Thm 4.1",
           "eps at the two forged coarse patches and the legitimate one, at "
           "the committed state", ["1/16", "1/8", "3/16"],
           [S(my_eps(p, my_pres(det, p), RHO)) for p in (PI1, P22, PTOMO)])
    anchor("A05", "stage-5 Cor 4.3",
           "the eps spectrum over all 52 records and its multiplicities, "
           "the Stirling row S(5,k)",
           [["0", "1/16", "1/8", "3/16", "1/4"], [1, 10, 25, 15, 1]],
           _eps_spectrum(det))
    anchor("A06", "stage-5 Thm 5.1 (state map)",
           "the closed-form state map at the committed state and at the "
           "selective-amnesty state (1/2,0,1/2,0,0)",
           [["1/16", "1/8", "3/16"], ["0", "0", "1/2"]],
           [[S(v) for v in L3.state_map(RHO)],
            [S(v) for v in L3.state_map(RHO_AMNESTY)]])
    anchor("A07", "stage-5 sec 9.1",
           "omega vanishes at every record and every declared preparation "
           "under DET: instances, and non-zero among them", [1612, 0],
           _omega_det_census(det))
    anchor("A08", "stage-5 Thm 5.1 (simplex)",
           "the declared state grid at denominator 16, and the forward "
           "separating set for eps over it", [4845, 0], _grid_census())
    c = L2.census_T3()
    anchor("A09", "B\" Thm 3.5 (census)",
           "censused laws; identity-containing; laws admitting a proper "
           "boundary", [687, 259, 428],
           [c["laws"], c["identity_containing"],
            c["admitting_a_proper_boundary"]])
    anchor("A10", "stage-5 Prop 3.2",
           "admissible patches at identity-free censused laws, and those "
           "with eps non-zero", [745, 0], _identity_free_side())
    anchor("A11", "stage-5 sec 9.1 (R2 K2/F5)",
           "(boundary, family) keys over the census, those reachable from "
           "more than one declared law, and the worst fan-in",
           [874, 175, 428], _census_fan_in())
    anchor("A12", "B\" Thm 8.4",
           "the DET cost tower at the committed tower's four levels",
           [120, 360, 1260, 3120],
           [L2.forging_cost(det, p, 5)["cost"]
            for p in (PI1, P22, PTOMO, ONEATOM5)])
    anchor("A13", "stage-5 Thm 5.1 (the refinement chain)",
           "both forgeries are REFINEMENTS of the legitimate coarse chart",
           [True, True, True],
           [CB.refines(PI1, P22), CB.refines(P22, PTOMO),
            CB.refines(PI1, PTOMO)])
    a1111 = CBP.aligned_manufactured_boundary((1, 1, 1, 1))
    addr = CBP.boundary_from_blocks("ADDRESS", (1,) * 5)
    anchor("A14", "stage-5 Thm 5.3 (the collision)",
           "the adversary's manufactured 1+1+1+1 context and the legitimate "
           "address context present IDENTICAL declared data", True,
           a1111.atoms == addr.atoms)
    anchor("A15", "THIS UNIT vs B\" / stage-5",
           "this unit's own Pres, eps and omega routes agree with the "
           "terminal ones over all 52 records under DET", [0, 0, 0],
           _route_agreement(det))
    txt = (HERE.parent / "paper-rq0-epsilon-admissibility.md").read_text()
    anchor("A16", "stage-5 sec 10 (immutable, verbatim)",
           "the terminal cycle's OWN constraint on any successor statistic",
           True,
           ("no refinement-monotone statistic whatever" in txt
            and "Any successor must be\nnon-monotone in the refinement order"
            in txt))
    # A17 and A18 carry the warrant that actually kills an anti-monotone
    # separator.  Both are STRING anchors: they certify the terminal cycle's
    # words, and nothing about how this unit reads them.
    anchor("A17", "stage-5 sec 1 (immutable, verbatim)",
           "the terminal cycle's OWN verdict on an anti-monotone grading",
           True,
           ("a grading of coarseness with the sign flipped rather than a "
            "reading\nof provenance") in txt)
    anchor("A18", "stage-5 sec 9.1 (immutable, verbatim)",
           "the terminal cycle's OWN count of the rows where omega ranks the "
           "legitimate patch best: 15 of 155, 12 at FUNNEL and 3 at the "
           "counter-law, 6 admitting it at tolerance zero",
           True,
           ("That grading exists at 15 of the 155 (law,\npreparation) rows "
            "— 12 at FUNNEL, 3 at the counter-law" in txt
            and "admits the legitimate patch at tolerance\nzero at 6 of them"
            in txt))
    anchor("A19", "stage-5 sec 9.1 (the fifteen rows, recomputed here)",
           "the (law, preparation) rows at which omega ranks the LEGITIMATE "
           "patch strictly best -- total of 155, per committed law, and "
           "those admitting it at tolerance zero",
           [15, [0, 12, 0, 0, 3], 6], _omega_rows_census())


def _eps_spectrum(det):
    spec: dict = {}
    for p in CB.parts_of(5):
        spec.setdefault(my_eps(p, my_pres(det, p), RHO), 0)
        spec[my_eps(p, my_pres(det, p), RHO)] += 1
    ks = sorted(spec)
    return [[S(k) for k in ks], [spec[k] for k in ks]]


def _omega_det_census(det):
    n = z = 0
    for p in CB.parts_of(5):
        for pr in preps_of(5):
            n += 1
            if omega_fast(p, det, pr, RHO, 5) != 0:
                z += 1
    return [n, z]


_GRID: list = []


def grid_states():
    if not _GRID:
        _GRID.extend(L3.grid_states())
    return _GRID


def _omega_rows_census():
    """Stage-5 sec 9.1's FIFTEEN ROWS, recomputed on this unit's own route:
    over the five committed laws and all 31 admitted preparations, the rows
    at which omega ranks the LEGITIMATE patch strictly best, and those that
    admit it at tolerance zero.  These rows are C1's separating content --
    C1 being the sum of omega over the same preparations -- and the terminal
    cycle has already adjudicated them (A17, A18)."""
    per, tol0 = [], 0
    for lname, law in committed_laws5():
        c = 0
        for pr in preps_of(5):
            w1 = omega_fast(PI1, law, pr, RHO, 5)
            w2 = omega_fast(P22, law, pr, RHO, 5)
            wl = omega_fast(PTOMO, law, pr, RHO, 5)
            if wl < w1 and wl < w2:
                c += 1
                if wl == 0:
                    tol0 += 1
        per.append(c)
    return [sum(per), per, tol0]


def _grid_census():
    fwd = 0
    for st in grid_states():
        a, b, cc = L3.state_map(st)
        if cc < a and cc < b:
            fwd += 1
    return [len(grid_states()), fwd]


_IDFREE: list = []


def identity_free_admissible():
    """The dichotomy's identity-free side: the census patches the terminal
    axiom admits at identity-free laws -- where PROPER charts live."""
    if not _IDFREE:
        rho3 = tuple(Fr(1, 3) for _ in range(3))
        for Lf in L2.laws_of_T3():
            law = [L2.sup_of_map(f) for f in sorted(Lf)]
            if L2.has_identity(law, 3):
                continue
            for p in CB.parts_of(3):
                fam = my_pres(law, p)
                if L2.adjudicate(p, fam, law, frozenset(range(3)),
                                 3)["admissible"]:
                    _IDFREE.append((p, tuple(sorted(Lf)), law, rho3))
    return _IDFREE


def _identity_free_side():
    bad = sum(1 for p, _, law, r3 in identity_free_admissible()
              if my_eps(p, my_pres(law, p), r3) != 0)
    return [len(identity_free_admissible()), bad]


_FANIN3: dict = {}


def census_fan_in():
    """The terminal fan-in resource at three configurations: how many
    declared laws reach each (boundary, preservation family) key."""
    if not _FANIN3:
        for Lf in L2.laws_of_T3():
            law = [L2.sup_of_map(f) for f in sorted(Lf)]
            for p in CB.parts_of(3):
                k = (p, tuple(sorted(tuple(tuple(sorted(s)) for s in F)
                                     for F in my_pres(law, p))))
                _FANIN3.setdefault(k, set()).add(tuple(sorted(Lf)))
    return _FANIN3


def _census_fan_in():
    fan = {k: len(v) for k, v in census_fan_in().items()}
    return [len(fan), sum(1 for v in fan.values() if v > 1), max(fan.values())]


def _route_agreement(det):
    dp = de = do = 0
    for p in CB.parts_of(5):
        f1, f2 = my_pres(det, p), L2.pres_of(det, p)
        dp += (sorted(map(L2.key, f1)) != sorted(map(L2.key, f2)))
        de += (my_eps(p, f1, RHO) != L3.epsilon(p, f2, RHO))
        do += (my_omega(p, f1, PREP_FULL, RHO, 5)
               != L3.occupancy_defect(p, f2, PREP_FULL, RHO, 5))
    return [dp, de, do]


# --------------------------------------------------------------------------
# 3.  THE CANDIDATE FAMILY, DECLARED BEFORE ANY FIXTURE VALUE IS COMPUTED.
#     Orientation is fixed: admitted iff the statistic is SMALL.
# --------------------------------------------------------------------------


def c1_counterfactual_occupancy(part, law, prep, rho, n):
    """C1 -- COUNTERFACTUAL OCCUPANCY PROFILE.  The profile of the occupancy
    defect omega over ALL admitted preparations, not only the declared one,
    summarised by its total.  This is the pin's answer to the DET forger who
    attains omega = 0 at all 31 declared preparations: compare profiles."""
    return sum((omega_fast(part, law, pr, rho, n) for pr in preps_of(n)),
               Fr(0))


def c1_profile(part, law, prep, rho, n):
    """C1's underlying profile, kept for the pointwise reading."""
    return tuple(omega_fast(part, law, pr, rho, n) for pr in preps_of(n))


def c2_generation_mismatch(part, law, prep, rho, n):
    """C2 -- GENERATION-PROFILE MISMATCH.  The coarse structure the law
    actually GENERATES on the patch's realized process -- the collision
    classes ker(Pres_L(pi)) of the realized legs -- against the declared
    boundary: the declared mass on which the generated structure resolves
    inside a declared atom."""
    if MUTANT == "mismatch-lax":
        return Fr(0)
    fam = my_pres(law, part)
    R = reach_from_succ(succ_of(law, part, n), prep)
    K = my_ker(fam, n)
    tot = Fr(0)
    for r in part:
        rr = [j for j in r if j in R]
        if not rr:
            continue
        pr = sum((rho[j] for j in rr), Fr(0))
        best = Fr(0)
        for cl in K:
            v = sum((rho[j] for j in cl if j in rr), Fr(0))
            if v > best:
                best = v
        tot += pr - best
    return tot


_POP: dict = {}


def law_population(n: int):
    """THE DECLARED LAW POPULATION for C3's fan-in, per arity.  At three
    configurations it is the committed 687-law census.  At five it is every
    composition-closed law generated by ONE admitted single-valued operation,
    together with the committed laws -- named as a declared population, never
    as an exhaustive census."""
    if n not in _POP:
        if n == 3:
            _POP[n] = [[L2.sup_of_map(f) for f in sorted(Lf)]
                       for Lf in L2.laws_of_T3()]
        else:
            seen = set()
            for f in product(range(n), repeat=n):
                seen.add(frozenset(L2.closure_of_maps((f,), n)))
            pop = [[L2.sup_of_map(f) for f in sorted(Lf)]
                   for Lf in sorted(seen, key=lambda L: (len(L), sorted(L)))]
            if MUTANT != "fanin-lax":
                pop = pop + [law for _, law in L2.committed_laws(n)]
            _POP[n] = pop
    return _POP[n]


def _famkey(fam):
    return tuple(sorted(tuple(tuple(sorted(s)) for s in F) for F in fam))


def c3_law_fan_in(part, law, prep, rho, n):
    """C3 -- LAW-FAN-IN.  How many laws of the declared population present
    the SAME (boundary, preservation family) key as the declared one: the
    terminal factoring result (175 of 874 keys reachable from more than one
    law, one from 428) turned into a statistic on the patch."""
    k = pres_key(law, part)
    m = len(k)
    return Fr(sum(1 for Lp in law_population(n)
                  if len(Lp) >= m and pres_key(Lp, part) == k))


def c4a_state_alignment(part, law, prep, rho, n):
    """C4a -- STATE-SYMMETRY ALIGNMENT DEFECT.  The declared mass carried by
    declared atoms that are NOT unions of the declared state's level classes:
    the mass on which the boundary cuts across the state's own symmetry."""
    if MUTANT == "align-lax":
        return Fr(0)
    lam = level_partition(rho)
    sat = saturated_atoms(part, lam)
    return sum((sum((rho[j] for j in r), Fr(0))
                for r, s in zip(part, sat) if not s), Fr(0))


def c4a_route2(part, law, prep, rho, n):
    sat = saturated_atoms_route2(part, level_partition(rho))
    return sum((sum((rho[j] for j in r), Fr(0))
                for r, s in zip(part, sat) if not s), Fr(0))


def c4b_reach_alignment(part, law, prep, rho, n):
    """C4b -- LAW-REACHABILITY ALIGNMENT DEFECT.  The same construction with
    the LAW's own counterfactual structure in place of the state's: the
    declared mass on atoms that are not unions of the law's reachability
    classes, i.e. the mass the law's own dynamics does not regenerate."""
    cls = reach_classes(law, part, n)
    sat = saturated_atoms(part, cls)
    return sum((sum((rho[j] for j in r), Fr(0))
                for r, s in zip(part, sat) if not s), Fr(0))


def c4c_pair_resolution(part, law, prep, rho, n):
    """C4c -- THE MAXIMAL COVARIANT CANDIDATE.  The negated count of ordered
    configuration pairs the boundary merges.  Declared negated so that the
    COARSEST boundary is the most admitted: this is the strongest reading any
    covariant statistic of the declared boundary can have, and Section 8
    proves every covariant candidate factors through its invariant."""
    return Fr(-sum(len(r) * (len(r) - 1) for r in part))


CANDIDATES = [
    ("C1", "counterfactual occupancy profile", c1_counterfactual_occupancy),
    ("C2", "generation-profile mismatch", c2_generation_mismatch),
    ("C3", "law-fan-in", c3_law_fan_in),
    ("C4a", "state-symmetry alignment defect", c4a_state_alignment),
    ("C4b", "law-reachability alignment defect", c4b_reach_alignment),
    ("C4c", "the maximal covariant candidate (pair-resolution index)",
     c4c_pair_resolution),
]

DECLARED_DEFINITIONS = [
    ("c1_counterfactual_occupancy", c1_counterfactual_occupancy),
    ("c1_profile", c1_profile),
    ("c2_generation_mismatch", c2_generation_mismatch),
    ("c3_law_fan_in", c3_law_fan_in),
    ("c4a_state_alignment", c4a_state_alignment),
    ("c4a_route2", c4a_route2),
    ("c4b_reach_alignment", c4b_reach_alignment),
    ("c4c_pair_resolution", c4c_pair_resolution),
]


# --------------------------------------------------------------------------
# 3b.  THE PANEL CLASS.  Eight further statistics, none of them a hunt
#      candidate: they were constructed AGAINST the delivered unit, with the
#      fixture already known, and they are carried here because a corridor
#      that only ever meets its author's constructions has not been tested.
#      They are declared and hashed in L4-00B, gated by the same battery, and
#      evaluated only AFTER the barrier.  TUNE is the permanent NEGATIVE
#      CONTROL of the freeze audit.
# --------------------------------------------------------------------------


def c5_marked_block_penalty(part, law, prep, rho, n):
    """C5 -- R1's construction (operator lens), completed to name-blindness.
    The pair-resolution index penalised by the excess of the block carrying
    the configuration the declared state marks out: PR(pi) + 1000 s, with s
    the mean over the maximal-mass configurations of |block(j)| - 1.  Built
    to clear the pinned corridor, the inherited G1 AND the erasure column at
    once -- the only construction in this file that refuses total erasure."""
    top = max(rho)
    M = [j for j in range(n) if rho[j] == top]
    blk = {j: r for r in part for j in r}
    s = sum((Fr(len(blk[j]) - 1) for j in M), Fr(0)) / Fr(len(M))
    return c4c_pair_resolution(part, law, prep, rho, n) + 1000 * s


def d1_two_atom_count(part, law, prep, rho, n):
    """D1 -- R2's construction (effectus lens): the number of two-element
    declared atoms.  State-blind, non-monotone, and a function of the atom
    sizes: the first arm of the fused theorem with an inhabitant."""
    return Fr(sum(1 for r in part if len(r) == 2))


def d2_two_atom_mass(part, law, prep, rho, n):
    """D2 -- R2's construction: the declared mass carried by two-element
    atoms.  It READS the declared state and the sweep never inverts it --
    R2's refutation of 'the sweep's power is co-extensive with
    state-reading'."""
    return sum((sum((rho[j] for j in r), Fr(0))
                for r in part if len(r) == 2), Fr(0))


def d3_label_reader(part, law, prep, rho, n):
    """D3 -- R2's sharpest construction: D1 doubled plus the indicator of one
    named atom.  It passes every pinned corridor gate at the counter-law
    under both readings of G1, separates, and survives the sweep -- and it
    COMPARES NAMES.  The corpse the name-blindness gate exists to produce."""
    return Fr(2 * sum(1 for r in part if len(r) == 2)
              + (1 if (0, 1) in part else 0))


def d4_middling_atom_count(part, law, prep, rho, n):
    """D4 -- R2's construction: the number of atoms of size neither 1 nor 4.
    It separates and REFUSES total erasure, which is why 'every separator
    certifies total erasure' is a measured property of three candidates and
    not a law."""
    return Fr(sum(1 for r in part if len(r) not in (1, 4)))


def d5_named_sink_weighted_pairs(part, law, prep, rho, n):
    """D5 -- R2's construction as written: the merged-pair count weighted by
    (1/2 - the mass at configuration 4).  It is measured ANTI-MONOTONE at the
    committed state and the sweep inverts it anyway -- the refutation of the
    'monotone separators are immune by construction' mechanism.  As written
    it reads a configuration by NAME, so the name-blindness gate takes it."""
    return (Fr(1, 2) - rho[4]) * Fr(sum(len(r) * (len(r) - 1) for r in part))


def d5n_marked_mass_weighted_pairs(part, law, prep, rho, n):
    """D5N -- R2's D5 completed to name-blindness: the same statistic with
    the marked configuration's mass in place of configuration 4's.  It
    carries R2's structural point through the gate."""
    return (Fr(1, 2) - max(rho)) * Fr(sum(len(r) * (len(r) - 1)
                                          for r in part))


def d_sum_of_two_declared(part, law, prep, rho, n):
    """D -- R3's construction (instrument lens): C4a + C1/1000, a sum of two
    DECLARED candidates with no fixture reference whatever.  It passes the
    full pinned and inherited corridor at the counter-law, which the declared
    family does not -- the declared family is not closed under sums."""
    return (c4a_state_alignment(part, law, prep, rho, n)
            + c1_counterfactual_occupancy(part, law, prep, rho, n) / 1000)


def tune_negative_control(part, law, prep, rho, n):
    """TUNE -- R3's construction, and the PERMANENT NEGATIVE CONTROL of the
    freeze audit: D with one explicit read of the committed legitimate
    boundary.  It would be registered as a fingerprint by the delivered
    machinery -- it separates, it is not order-entailed, and no state inverts
    it.  It must be caught, and it must be caught by the SOURCE SCAN and by
    the NAME-BLINDNESS gate, never by the barrier, which cannot see it."""
    return (d_sum_of_two_declared(part, law, prep, rho, n)
            - 1000 * (1 if part == PTOMO else 0))


PANEL = [
    ("C5", "R1: pair-resolution penalised by the marked block's excess",
     c5_marked_block_penalty),
    ("D1", "R2: the count of two-element atoms", d1_two_atom_count),
    ("D2", "R2: the mass on two-element atoms", d2_two_atom_mass),
    ("D3", "R2: D1 doubled plus a NAMED-ATOM indicator", d3_label_reader),
    ("D4", "R2: the count of atoms of size neither 1 nor 4",
     d4_middling_atom_count),
    ("D5", "R2: merged pairs weighted by (1/2 - the mass AT CONFIGURATION 4)",
     d5_named_sink_weighted_pairs),
    ("D5N", "R2's D5 completed to name-blindness (the marked mass)",
     d5n_marked_mass_weighted_pairs),
    ("D", "R3: C4a + C1/1000, a sum of two declared candidates",
     d_sum_of_two_declared),
    ("TUNE", "R3: D with one read of the committed legitimate boundary "
     "(THE NEGATIVE CONTROL)", tune_negative_control),
]


def declare_candidates():
    """THE FREEZE.  The family, its definitions and the SHA-256 of their
    source text are registered here, before any fixture value exists."""
    prog("candidate family: declared and frozen (6 candidates); source scan")
    if MUTANT == "freeze-lax":
        touch(PTOMO)               # a fixture value computed BEFORE the
                                   # declaration: the threat L4-00 exists for
    reg = []
    for cid, name, fn in CANDIDATES:
        src = inspect.getsource(fn)
        reg.append({"id": cid, "name": name,
                    "orientation": "admitted iff the statistic is SMALL",
                    "definition_sha256":
                        hashlib.sha256(src.encode()).hexdigest()[:16],
                    "docstring": " ".join(fn.__doc__.split())})
    TABLES["the_declared_candidate_family"] = reg
    gate("L4-00", "freeze",
         "THE CANDIDATE FAMILY IS DECLARED AND FROZEN BEFORE ANY FIXTURE "
         "VALUE IS COMPUTED.  Six candidates, each with its definition, its "
         "orientation and the SHA-256 of its source text; the pin's C1, C2 "
         "and C3 and three worker constructions.  The hashes are what binds "
         "this receipt to inspectable source, and they are half of what "
         "carries the freeze; L4-SRC is the other half.",
         len(reg) == 6 and not _TOUCHED_FIXTURE, len(reg), must_pass=True)
    scan = source_scan(DECLARED_DEFINITIONS
                       + [("tune_negative_control (NEGATIVE CONTROL)",
                           tune_negative_control)])
    TABLES["freeze_source_scan"] = scan
    clean = all(r["clean"] for r in scan if "CONTROL" not in r["definition"])
    caught = [r for r in scan
              if "CONTROL" in r["definition"] and not r["clean"]]
    gate("L4-SRC", "freeze",
         "THE FREEZE'S SUBSTANTIVE CHECK: AN AUTOMATED SOURCE SCAN.  Each of "
         "the eight declared definitions is scanned, in its own source text, "
         "for any reference to a committed boundary (PI1, P22, PTOMO, DISC5, "
         "ONEATOM5, FIXTURE, PROVENANCE): every one is a generic function of "
         "(part, law, prep, rho, n) and NONE of them mentions one.  The gate "
         "is self-testing: it passes only if the eight are clean AND the "
         "permanent negative control -- R3's TUNE, which special-cases the "
         "committed legitimate boundary -- IS caught by the same scan.  This "
         "is the check that works, and it is a property of the source, not "
         "of the gate order.",
         clean and bool(caught),
         {"declared_definitions_scanned": len(DECLARED_DEFINITIONS),
          "declared_definitions_clean": clean,
          "negative_control_caught_by_the_scan":
              [r["definition"] for r in caught],
          "tokens": FIXTURE_TOKENS}, must_pass=True)
    return reg


# --------------------------------------------------------------------------
# 4.  THE CORRIDOR GATES.  Off-fixture population only.
# --------------------------------------------------------------------------


def off_fixture():
    return [p for p in CB.parts_of(5) if p not in FIXTURE]


_LAWS5: list = []
LAW5: dict = {}


def committed_laws5():
    """The five committed law families, held once so that every memo keys on
    a stable object and no value depends on the memo."""
    if not _LAWS5:
        _LAWS5.extend(L2.committed_laws(5))
        LAW5.update({nm: lw for nm, lw in _LAWS5})
    return _LAWS5


_IMG: dict = {}


def corridor_row(cid, fn, lname, law, OFF, pairs, img_key="L4-G5"):
    """The full corridor battery for one (candidate, law), decided on the
    off-fixture population alone: nondegeneracy, monotonicity type in both
    readings, the two factoring gates, covariance, and NAME-BLINDNESS."""
    vals = {p: fn(p, law, PREP_FULL, RHO, 5) for p in OFF}
    # -- G3, first per the pin: content must survive the committed
    #    configuration.
    g3 = len(set(vals.values())) > 1
    # -- G1: monotonicity type in the refinement order.
    mono = anti = True
    for p, q in pairs:
        f, c = (p, q) if CB.refines(p, q) else (q, p)
        if vals[f] > vals[c]:
            mono = False
        if vals[f] < vals[c]:
            anti = False
    g1 = not mono          # THE PIN's gate 1, literally
    mtype = ("monotone" if mono and not anti else
             "anti-monotone" if anti and not mono else
             "constant" if mono and anti else "neither")
    # THE INHERITED gate 1 (stage-5 sec 10, anchor A16): a successor
    # must be NON-monotone in the refinement order -- monotone in
    # EITHER direction is a grading of coarseness.
    g1t = (mtype == "neither")
    # -- G2a: not a function of eps.  G2b: not a function of the
    #    covariant invariant.
    fe: dict = {}
    fs: dict = {}
    g2a = g2b = False
    for p in OFF:
        e = eps_at(law, p, RHO)
        if fe.setdefault(e, vals[p]) != vals[p]:
            g2a = True
        sh = shape_invariant(p, RHO)
        if fs.setdefault(sh, vals[p]) != vals[p]:
            g2b = True
    # -- G5: covariance under the admitted isomorphisms.
    grp = stab_of(lname, law, RHO, PREP_FULL, 5)
    g5 = all(fn(act_part(p, g), law, PREP_FULL, RHO, 5) == vals[p]
             for p in OFF for g in grp)
    _IMG.setdefault(img_key, {})
    for k, v in fixture_images(OFF, grp).items():
        _IMG[img_key][k] = _IMG[img_key].get(k, 0) + v
    # -- G-NB: NAME-BLINDNESS, under all 120 relabellings of the whole
    #    declared datum.  This is the gate with content where the
    #    stabilizer is trivial and covariance therefore has none.
    nb, witness, hits = name_blind(cid, fn, law, OFF)
    if img_key == "L4-G5":
        _IMG.setdefault("L4-NB", {})
        _IMG["L4-NB"]["total"] = _IMG["L4-NB"].get("total", 0) + hits
    return {"candidate": cid, "law": lname,
            "G3_nondegenerate": g3, "monotonicity_type": mtype,
            "G1_not_refinement_monotone": g1,
            "G1t_non_monotone_in_the_refinement_order": g1t,
            "G2a_not_a_function_of_eps": g2a,
            "G2b_not_a_function_of_the_covariant_invariant": g2b,
            "G5_covariant": g5,
            "GNB_name_blind": nb,
            "GNB_label_reading_witness": witness,
            "distinct_values_off_fixture": len(set(vals.values())),
            "stabilizer_order": len(grp),
            "G5_vacuous_no_admitted_isomorphism": len(grp) == 1}


def run_corridor():
    prog("corridor gates: nondegeneracy, monotonicity, factoring, "
         "covariance, NAME-BLINDNESS, identity-free side -- OFF-FIXTURE ONLY")
    OFF = off_fixture()
    pairs = [(p, q) for p, q in combinations(OFF, 2)
             if CB.refines(p, q) or CB.refines(q, p)]
    TABLES["comparable_pair_populations"] = {
        "off_fixture_comparable_ordered_pairs": 2 * len(pairs),
        "off_fixture_comparable_unordered_pairs": len(pairs)}
    TABLES["committed_law_cardinalities"] = {
        nm: len(lw) for nm, lw in committed_laws5()}
    TABLES["committed_laws_invariant_under_relabelling"] = {
        nm: len({law_key_of(act_law_obj(lw, sg)) for sg in SYM5})
        for nm, lw in committed_laws5()}
    rows = []
    for cid, name, fn in CANDIDATES:
        for lname, law in committed_laws5():
            rows.append(corridor_row(cid, fn, lname, law, OFF, pairs))
    TABLES["corridor_gates_off_fixture"] = rows
    fails = [(r["candidate"], r["law"]) for r in rows
             if not r["GNB_name_blind"]]
    gate("L4-NB", "corridor",
         "THE NAME-BLINDNESS GATE.  A statistic on declared data must be a "
         "function of LABEL-FREE invariants: relabelling the carrier "
         "throughout the declared datum -- boundary, law, preparation and "
         "state moved together -- may not move its value.  Tested "
         "exhaustively over the 48 off-fixture records and all 120 "
         "relabellings at every committed law, with a witness recorded for "
         "every failure.  Covariance (gate 5) is invariance under the "
         "STABILIZER of the declared data and has no content where that "
         "stabilizer is trivial; this gate has content everywhere, and it is "
         "the corpus's own co-reference discipline, under which names are "
         "never compared.  Measured on the declared six: one failure, C3 at "
         "the counter-law -- and it is NOT a statistic reading names.  C3 "
         "counts the laws of a DECLARED POPULATION sharing the patch's key, "
         "and that population is not closed under relabelling: it adjoins "
         "the five committed laws, one of which -- the counter-law, "
         "generated by block-minimum idempotents -- is itself a "
         "label-reading construction, so a relabelled counter-law is not in "
         "the population.  The gate is measuring the population's "
         "non-closure, not the statistic; C3 is dead at G3 in any case, its "
         "fan-in being identically 1 at every committed law.",
         not fails, {"failures": fails,
                     "diagnosis": {
                         "C3 @ COUNTER-LAW": "the declared 2847-law "
                         "population is not closed under relabelling (it "
                         "adjoins the committed counter-law, a "
                         "label-reading construction); C3 is dead at G3 "
                         "regardless"}})
    for cid, _, _ in CANDIDATES:
        mine = [r for r in rows if r["candidate"] == cid]
        base = ["G3_nondegenerate", "G2a_not_a_function_of_eps",
                "G2b_not_a_function_of_the_covariant_invariant",
                "G5_covariant"]
        alive = [r["law"] for r in mine
                 if all(r[k] for k in base) and r["G1_not_refinement_monotone"]]
        alive_t = [r["law"] for r in mine
                   if all(r[k] for k in base)
                   and r["G1t_non_monotone_in_the_refinement_order"]]
        gate(f"L4-C{cid}", "corridor",
             f"{cid} corridor membership at the committed laws, decided on "
             f"the 48 off-fixture records alone.  Under the PIN's gate 1 "
             f"(not refinement-monotone): {alive if alive else 'NONE'}.  "
             f"Under the INHERITED gate 1 (stage-5 sec 10, anchor A16: a "
             f"successor must be NON-monotone in the refinement order): "
             f"{alive_t if alive_t else 'NONE'}.",
             bool(alive), {"laws_passing_the_pinned_corridor": alive,
                           "laws_passing_the_inherited_corridor": alive_t})

    # -- G6: the dichotomy's identity-free side must stay intact.
    idf = identity_free_admissible()
    g6rows = []
    for cid, name, fn in CANDIDATES:
        vals = set()
        for p, _, law, r3 in idf:
            vals.add(fn(p, law, frozenset(range(3)), r3, 3))
        g6rows.append({"candidate": cid, "distinct_values_on_the_745": len(vals),
                       "G6_side_intact": len(vals) == 1})
    TABLES["identity_free_side"] = g6rows
    gate("L4-G6", "corridor",
         "THE DICHOTOMY'S IDENTITY-FREE SIDE.  eps is constant (exactly 0) "
         "at all 745 admissible patches at identity-free censused laws, so "
         "one tolerance retains the whole side.  A candidate keeps the side "
         "intact only if it is constant there too; measured per candidate.",
         True, g6rows)
    return rows


def freeze_barrier():
    """THE BARRIER, REBUILT.  What an in-script gate can certify is the
    ORDER of its own stages and the DECISIONS taken in them; it cannot
    certify authoring order, and -- measured -- it cannot certify that no
    candidate was evaluated at a committed boundary, because covariance and
    name-blindness are orbit properties and the orbits of off-fixture records
    meet the fixture.  So the barrier claims what is true and L4-IMG counts
    what it cannot avoid."""
    img = {k: dict(v) for k, v in _IMG.items()}
    for k in list(img):
        img[k]["SUBTOTAL"] = sum(img[k].values())
    tot = sum(d["SUBTOTAL"] for d in img.values())
    det = LAW5["DET"]
    per_law = fixture_images(off_fixture(),
                             stab_of("DET", det, RHO, PREP_FULL, 5))
    img["per_candidate_per_symmetric_law_in_the_covariance_gate"] = {
        **per_law, "SUBTOTAL": sum(per_law.values())}
    gate("L4-IMG", "freeze",
         "THE ORBIT-FORCED EVALUATIONS, DISCLOSED AND COUNTED.  Covariance "
         "and name-blindness are ORBIT properties: they compare a "
         "candidate's value at a record with its value at the record's "
         "relabelled image, and some of those images ARE committed "
         "boundaries -- necessarily, since the forged 2+1+1 and the forged "
         "2+2 lie in the orbits of off-fixture records under the admitted "
         "isomorphisms, and the legitimate tomographic minimum lies in "
         "theirs under the full relabelling group.  Every such value is "
         "equality-tested against its own off-fixture partner; none is "
         "retained, compared to a threshold, or used in any selection, and "
         "no ORDERING of fixture values is ever read.  Counted exactly, per "
         "gate and per committed boundary.",
         True, {"per_gate": img, "total_pre_barrier_evaluations_at_a_"
                "committed_boundary": tot})
    ok = all(g["passed"] for g in GATES if g["id"] in ("L4-00", "L4-SRC"))
    if MUTANT == "freeze-lax":
        ok = False
    gate("L4-FREEZE", "freeze",
         "FREEZE BARRIER, THE HONEST CLAIM.  Two checks carry the freeze and "
         "both are above this line: L4-00, which registers the SHA-256 of "
         "every candidate definition's source text before any fixture value "
         "is computed, binding the receipt to inspectable source; and "
         "L4-SRC, an automated scan of that source establishing that NO "
         "candidate definition mentions any committed boundary -- with a "
         "permanent negative control that the scan catches.  Below this line "
         "the corridor's DECISIONS are already taken, on the 48 off-fixture "
         "records and the 745 census patches alone.  What is NOT claimed: "
         "that the gate order proves the freeze (it cannot establish "
         "authoring order), and that no candidate was evaluated at a "
         "committed boundary (L4-IMG counts those that the orbit gates "
         "force).  RUNBOOK sec 13(4).",
         ok, {"gates_before_the_barrier": len(GATES),
              "carried_by": ["L4-00 definition hashes",
                             "L4-SRC automated source scan"],
              "not_carried_by": ["the gate order",
                                 "the per-gate provenance annotation"]},
         must_pass=True)


# --------------------------------------------------------------------------
# 5.  THE FIXTURE.  Only now are the committed pairs evaluated.
# --------------------------------------------------------------------------


def separates(v_legit, v_f1, v_f2) -> bool:
    """The corpus's defect semantics: a candidate separates iff a tolerance
    admits the LEGITIMATE coarse patch and rejects BOTH forged ones."""
    if MUTANT == "sep-lax":
        return True
    return v_legit < v_f1 and v_legit < v_f2


def run_fixture():
    prog("fixture: the committed distinct-quadruple pairs")
    rows = []
    for cid, name, fn in CANDIDATES:
        for lname, law in committed_laws5():
            for p in FIXTURE:
                touch(p)
            v1 = fn(PI1, law, PREP_FULL, RHO, 5)
            v2 = fn(P22, law, PREP_FULL, RHO, 5)
            vl = fn(PTOMO, law, PREP_FULL, RHO, 5)
            vd = fn(DISC5, law, PREP_FULL, RHO, 5)
            ve = fn(ONEATOM5, law, PREP_FULL, RHO, 5)
            sep = separates(vl, v1, v2)
            rows.append({
                "candidate": cid, "law": lname,
                "forged_2+1+1": S(v1), "forged_2+2": S(v2),
                "legitimate_tomographic": S(vl),
                "carrier_algebra": S(vd), "total_erasure": S(ve),
                "separates": sep,
                "certifies_total_erasure_at_that_tolerance":
                    bool(sep and ve <= vl)})
    TABLES["fixture_values"] = rows
    seps = sorted({r["candidate"] for r in rows if r["separates"]})
    for cid, _, _ in CANDIDATES:
        mine = [r["law"] for r in rows
                if r["candidate"] == cid and r["separates"]]
        gate(f"L4-F{cid}", "fixture",
             f"{cid} on the committed pairs at the committed configuration: "
             f"separating laws {mine if mine else 'NONE'}.",
             bool(mine), {"separating_laws": mine})
    # -- C1's pointwise reading, its strongest form.
    ptrows = []
    for lname, law in committed_laws5():
        pr1 = c1_profile(PI1, law, PREP_FULL, RHO, 5)
        pr2 = c1_profile(P22, law, PREP_FULL, RHO, 5)
        prl = c1_profile(PTOMO, law, PREP_FULL, RHO, 5)
        hits = [i for i in range(len(pr1)) if separates(prl[i], pr1[i], pr2[i])]
        ptrows.append({"law": lname, "preparations_separating": len(hits),
                       "of": len(pr1)})
    TABLES["c1_pointwise_profile"] = ptrows
    gate("L4-C1PT", "fixture",
         "C1 READ POINTWISE, its strongest form: is there ANY admitted "
         "preparation at which the occupancy profile separates the committed "
         "pairs?  Swept over all 31 preparations at every committed law.",
         any(r["preparations_separating"] for r in ptrows), ptrows)
    # -- WHY each separation happens.  Both measurements read only data
    #    already frozen: the monotonicity type measured OFF-FIXTURE, and the
    #    fixture column computed in the same pass as the separation itself.
    ent = []
    for r in rows:
        if not r["separates"]:
            continue
        mt = [x["monotonicity_type"]
              for x in TABLES["corridor_gates_off_fixture"]
              if x["candidate"] == r["candidate"] and x["law"] == r["law"]][0]
        ent.append({"candidate": r["candidate"], "law": r["law"],
                    "monotonicity_type_measured_off_fixture": mt,
                    "separation_entailed_by_the_refinement_order":
                        mt in ("monotone", "anti-monotone"),
                    "certifies_total_erasure_at_the_separating_tolerance":
                        r["certifies_total_erasure_at_that_tolerance"]})
    TABLES["why_each_separation_happens"] = ent
    gate("L4-ENT", "fixture",
         "IS THE SEPARATION ENTAILED BY THE REFINEMENT ORDER?  The committed "
         "triple is a CHAIN whose coarsest member is the legitimate one "
         "(anchor A13), so a candidate measured monotone in EITHER direction "
         "off-fixture separates it automatically, by the order alone and "
         "with no reading of provenance.  Reported per separating row; the "
         "gate passes only if some separation is NOT so entailed.",
         any(not e["separation_entailed_by_the_refinement_order"]
             for e in ent), ent)
    gate("L4-ERASE", "fixture",
         "DOES THE SEPARATING TOLERANCE CERTIFY TOTAL ERASURE?  The one-atom "
         "boundary forgets the whole carrier.  A tolerance that admits the "
         "legitimate coarse patch and rejects both forgeries, yet also "
         "admits total erasure, is grading how much is forgotten and not "
         "who declared it.  The gate passes only if some separator refuses "
         "total erasure at its own separating tolerance.",
         any(not e["certifies_total_erasure_at_the_separating_tolerance"]
             for e in ent), ent)
    FINDINGS["separating_candidates"] = seps
    return rows, seps


# --------------------------------------------------------------------------
# 6.  THE AMNESTY SWEEP.  Every separator, over the whole declared simplex.
# --------------------------------------------------------------------------


def run_amnesty(seps):
    prog(f"amnesty sweep over 4845 declared states: {seps or 'no separator'}")
    rows = []
    for cid in seps:
        fn = dict((c[0], c[2]) for c in CANDIDATES)[cid]
        for lname, law in committed_laws5():
            base = [r for r in TABLES["fixture_values"]
                    if r["candidate"] == cid and r["law"] == lname]
            if not base or not base[0]["separates"]:
                continue
            sep = tie = inv = 0
            for st in grid_states():
                v1 = fn(PI1, law, PREP_FULL, st, 5)
                v2 = fn(P22, law, PREP_FULL, st, 5)
                vl = fn(PTOMO, law, PREP_FULL, st, 5)
                if MUTANT == "amnesty-lax":
                    continue
                if vl > v1 or vl > v2:
                    inv += 1
                elif vl < v1 and vl < v2:
                    sep += 1
                else:
                    tie += 1
            rows.append({"candidate": cid, "law": lname, "states": len(grid_states()),
                         "separating_states": sep, "tied_states": tie,
                         "INVERTING_states": inv,
                         "verdict": ("FINGERPRINT-AMNESTY" if inv else
                                     "survives the sweep")})
    TABLES["amnesty_sweep"] = rows
    gate("L4-AM-SUM", "amnesty",
         "THE SWEEP IS EXHAUSTIVE.  Every one of the 4845 declared states of "
         "denominator 16 is classified exactly once as separating, tied or "
         "inverting, for every separator that reached the sweep.",
         all(r["separating_states"] + r["tied_states"] + r["INVERTING_states"]
             == len(grid_states()) for r in rows) and bool(rows) == bool(seps),
         len(rows), must_pass=True)
    for r in rows:
        gate(f"L4-AM-{r['candidate']}-{r['law']}", "amnesty",
             f"{r['candidate']} at {r['law']} swept over the whole declared "
             f"state simplex at denominator 16: separation holds at "
             f"{r['separating_states']} states, ties at {r['tied_states']}, "
             f"and INVERTS at {r['INVERTING_states']}.  Any inversion is "
             f"FINGERPRINT-AMNESTY and kills the candidate.",
             r["INVERTING_states"] == 0, r)
    return rows


# --------------------------------------------------------------------------
# 7.  ROBUSTNESS FOR ANY SURVIVOR: the law census and the law-blindness test.
# --------------------------------------------------------------------------


def run_robustness(seps):
    prog("robustness: law-blindness of every separator, and the census")
    rows = []
    for cid, name, fn in CANDIDATES:
        vals = {lname: (S(fn(PI1, law, PREP_FULL, RHO, 5)),
                        S(fn(P22, law, PREP_FULL, RHO, 5)),
                        S(fn(PTOMO, law, PREP_FULL, RHO, 5)))
                for lname, law in committed_laws5()}
        rows.append({"candidate": cid,
                     "distinct_value_triples_across_the_five_committed_laws":
                         len(set(vals.values())),
                     "law_blind_on_the_committed_pairs":
                         len(set(vals.values())) == 1,
                     "per_law": vals})
    TABLES["law_blindness"] = rows
    gate("L4-LB", "robustness",
         "LAW-BLINDNESS ON THE COMMITTED PAIRS.  The pin's question is "
         "whether the LAW remembers.  A candidate whose values on the three "
         "committed boundaries do not move across the five committed laws "
         "reads no law at all, whatever else it reads.",
         True, [{"candidate": r["candidate"],
                 "law_blind": r["law_blind_on_the_committed_pairs"]}
                for r in rows])
    fan = {k: len(v) for k, v in census_fan_in().items()}
    TABLES["census_fan_in_resource"] = {
        "boundary_family_keys": len(fan),
        "keys_reachable_from_more_than_one_declared_law":
            sum(1 for v in fan.values() if v > 1),
        "worst_fan_in": max(fan.values()),
        "keys_with_fan_in_one": sum(1 for v in fan.values() if v == 1)}
    return rows


# --------------------------------------------------------------------------
# 8.  THE COVARIANCE ANALYSIS AND THE CLASS THEOREM.
# --------------------------------------------------------------------------


def run_covariance():
    prog("covariance: the admitted isomorphisms, the orbits, the theorem")
    parts5 = CB.parts_of(5)
    rows = []
    for lname, law in committed_laws5():
        grp = stab_of(lname, law, RHO, PREP_FULL, 5)
        orbs = orbits_of(parts5, grp)
        bij = all((shape_invariant(p, RHO) == shape_invariant(q, RHO))
                  == any(p in o and q in o for o in orbs)
                  for p in parts5 for q in parts5)
        rows.append({"law": lname, "admitted_isomorphisms": len(grp),
                     "orbits_of_the_52_records": len(orbs),
                     "orbit_invariant_is_the_shape_profile": bij})
    TABLES["admitted_isomorphism_action"] = rows
    det = LAW5["DET"]
    grp = stab_of("DET", det, RHO, PREP_FULL, 5)
    orbs = orbits_of(parts5, grp)
    sym = [r for r in rows if r["admitted_isomorphisms"] == 24]
    gate("L4-COV0", "covariance",
         "THE COMMITTED LAWS SPLIT BY SYMMETRY.  Four of the five committed "
         "law families -- DET, FUNNEL, REV and the funnel closure -- have "
         "the full 24-element admitted-isomorphism group at the committed "
         "state and preparation; the COUNTER-LAW has the TRIVIAL group, so "
         "corridor gate 5 has no content there and any statistic passes it "
         "vacuously.  This is measured, and it is where the one corridor "
         "survivor survives.",
         len(sym) == 4 and any(r["admitted_isomorphisms"] == 1 for r in rows),
         {r["law"]: r["admitted_isomorphisms"] for r in rows},
         must_pass=True)
    gate("L4-COV1", "covariance",
         "THE ADMITTED ISOMORPHISMS OF THE COMMITTED CONFIGURATION are the "
         "24 relabellings fixing the retained sink and permuting the four "
         "success addresses -- the stabilizer of the declared state, law and "
         "preparation, measured and not assumed.  Under them the 52 records "
         "fall into exactly 12 orbits, and two records share an orbit if and "
         "only if they share the shape profile (the multiset over declared "
         "atoms of the atom's profile across the state's level classes), "
         "checked over all 52 x 52 pairs.",
         len(grp) == 24 and len(orbs) == 12
         and all(r["orbit_invariant_is_the_shape_profile"] for r in sym),
         {"stabilizer_order": len(grp), "orbits": len(orbs)}, must_pass=True)

    orb_of = {}
    for i, o in enumerate(orbs):
        for p in o:
            orb_of[p] = i
    trip = [(PI1, "FORGED"), (P22, "FORGED"), (PTOMO, "LEGITIMATE")]
    for p, _ in trip:
        touch(p)
    distinct = len({orb_of[p] for p, _ in trip}) == 3
    related = any(act_part(p, g) == q
                  for p, _ in trip for q, _ in trip if p != q for g in grp)
    gate("L4-COV2", "covariance",
         "ARE THE COMMITTED PAIRS RELATED BY AN ADMITTED ISOMORPHISM?  No: "
         "the three coarse boundaries lie in three DISTINCT orbits, of sizes "
         f"{[len([o for o in orbs if p in o][0]) for p, _ in trip]}, and no "
         "admitted isomorphism carries one to another.  Covariance therefore "
         "does NOT force them equal, and separation is not blocked by it.",
         distinct and not related,
         {"distinct_orbits": distinct, "related_by_an_isomorphism": related},
         must_pass=True)

    shapes = {p: shape_invariant(p, RHO) for p, _ in trip}
    gate("L4-COV3", "covariance",
         "THE CLASS THEOREM.  Every admitted-isomorphism-covariant statistic "
         "of the declared data at the committed configuration is constant on "
         "orbits, hence factors through the shape profile -- the boundary's "
         "resolution data.  So a covariant candidate that separates the "
         "committed pairs separates them BY SHAPE ALONE, and no covariant "
         "candidate can satisfy corridor gate 2 in its strong reading.  The "
         "corridor is empty at the committed configuration.  Witness of the "
         "cost: the terminal collision -- the adversary's manufactured "
         "1+1+1+1 context and the legitimate address context present "
         "identical declared data (anchor A14), hence identical shape, hence "
         "identical verdict from every covariant statistic.",
         len(set(shapes.values())) == 3,
         {S(k): [list(t) for t in v] for k, v in shapes.items()},
         must_pass=True)

    cov_and_nonres = []
    for cid, name, fn in CANDIDATES:
        r = [x for x in TABLES["corridor_gates_off_fixture"]
             if x["candidate"] == cid and x["law"] == "DET"][0]
        if r["G5_covariant"] and r[
                "G2b_not_a_function_of_the_covariant_invariant"]:
            cov_and_nonres.append(cid)
    gate("L4-COV4", "covariance",
         "THE THEOREM, MEASURED ON THE DECLARED FAMILY.  No declared "
         "candidate is both covariant and a non-function of the covariant "
         "shape invariant at DET: the intersection is empty, exactly as "
         "L4-COV3 proves it must be.",
         not cov_and_nonres, {"covariant_and_non_resolution": cov_and_nonres},
         must_pass=True)
    run_decomposition(parts5, orbs, grp)
    return rows


# --------------------------------------------------------------------------
# 8b.  SHAPE IS NOT RESOLUTION: the 12-vs-7 decomposition, its control, and
#      the scope of the full-group hypothesis.
# --------------------------------------------------------------------------


def resolution_profile(part):
    """THE RESOLUTION PROFILE -- the block-size profile, which is what the
    pin's gate 2 names: 'must not factor through partition-size or resolution
    data'.  It is STRICTLY COARSER than the covariant shape invariant."""
    return tuple(sorted(len(r) for r in part))


def marked_excess(part, rho):
    """THE STATE-DERIVED DATUM the shape invariant carries and the resolution
    profile does not: how many further configurations the boundary merges
    with the one the declared state marks out.  s = |block(marked)| - 1."""
    top = max(rho)
    M = [j for j in range(len(rho)) if rho[j] == top]
    blk = {j: r for r in part for j in r}
    return tuple(sorted(len(blk[j]) - 1 for j in M))


def _pcount(k: int) -> int:
    """p(k), the number of integer partitions of k."""
    tab = [1] + [0] * k
    for part in range(1, k + 1):
        for j in range(part, k + 1):
            tab[j] += tab[j - part]
    return tab[k]


def run_decomposition(parts5, orbs, grp):
    orb_of = {p: i for i, o in enumerate(orbs) for p in o}
    shapes = {shape_invariant(p, RHO) for p in parts5}
    res = {resolution_profile(p) for p in parts5}
    split = sorted({r for r in res
                    if len({orb_of[p] for p in parts5
                            if resolution_profile(p) == r}) > 1})
    pairs_ok = all((orb_of[p] == orb_of[q])
                   == ((resolution_profile(p), marked_excess(p, RHO))
                       == (resolution_profile(q), marked_excess(q, RHO)))
                   for p in parts5 for q in parts5)
    route2 = sum(_pcount(4 - s) for s in range(5))
    census = sorted(len(o) for o in orbs)
    trip_excess = [marked_excess(p, RHO) for p in (PI1, P22, PTOMO)]
    TABLES["shape_is_not_resolution"] = {
        "orbit_classes_the_covariant_shape_invariant": len(shapes),
        "resolution_profile_classes": len(res),
        "resolution_profiles_that_split_into_two_orbits": len(split),
        "the_splitting_profiles": [list(r) for r in split],
        "orbit_size_census": census,
        "orbit_size_census_sums_to": sum(census),
        "second_route_sum_over_s_of_p_4_minus_s": route2,
        "marked_block_excess_at_the_committed_triple":
            [list(t) for t in trip_excess]}
    gate("L4-DEC", "covariance",
         "SHAPE IS NOT RESOLUTION, AND THE GAP IS STATE-DERIVED.  The "
         "covariant orbit invariant separates the 52 records into 12 "
         "classes; the RESOLUTION profile -- the block-size profile the "
         "pin's gate 2 names -- separates them into 7, and exactly 5 "
         "resolution profiles split into two orbits apiece (12 = 7 + 5).  "
         "The datum that splits them is s, how many configurations the "
         "boundary merges with the one the declared state marks out: "
         "measured over all 52 x 52 pairs, two records share an orbit if and "
         "only if they share the PAIR (resolution profile, s).  A second "
         "route with no group action agrees: an orbit is determined by (s, "
         "the multiset of the remaining block sizes), giving sum over s of "
         "p(4-s) = 5+3+2+1+1 = 12.  The orbit-size census sums to 52.  So "
         "every covariant statistic factors through (resolution profile, "
         "state-reading component) -- and NOT through resolution data alone.",
         len(shapes) == 12 and len(res) == 7 and len(split) == 5
         and pairs_ok and route2 == 12 and sum(census) == 52,
         TABLES["shape_is_not_resolution"], must_pass=True)

    rho_u = tuple(Fr(1, 5) for _ in range(5))
    det = LAW5["DET"]
    grp_u = stabilizer(det, rho_u, PREP_FULL, 5)
    orbs_u = orbits_of(parts5, grp_u)
    orbu_of = {p: i for i, o in enumerate(orbs_u) for p in o}
    res_exact = all((orbu_of[p] == orbu_of[q])
                    == (resolution_profile(p) == resolution_profile(q))
                    for p in parts5 for q in parts5)
    gate("L4-UNIF", "covariance",
         "THE CONTROL THAT SETTLES IT.  At the UNIFORM state the declared "
         "data marks no configuration out, the admitted-isomorphism group is "
         "the whole 120, the 52 records fall into exactly 7 orbits, and the "
         "orbit invariant IS the block-size profile exactly -- measured over "
         "all 52 x 52 pairs.  The 12-vs-7 gap is therefore produced entirely "
         "by the committed state's 4+1 level structure, and a sentence "
         "identifying the covariant invariant with resolution data is the "
         "uniform-state theorem carried where it fails.",
         len(grp_u) == 120 and len(orbs_u) == 7 and res_exact,
         {"admitted_isomorphisms": len(grp_u), "orbits": len(orbs_u),
          "orbit_invariant_is_the_resolution_profile": res_exact},
         must_pass=True)

    hist: dict = {}
    bad = 0
    for st in grid_states():
        closed = 1
        mult: dict = {}
        for v in st:
            mult[v] = mult.get(v, 0) + 1
        if MUTANT != "scope-lax":
            for m in mult.values():
                for k in range(2, m + 1):
                    closed *= k
        brute = sum(1 for sg in SYM5
                    if all(st[sg[j]] == st[j] for j in range(5)))
        if closed != brute:
            bad += 1
        hist[closed] = hist.get(closed, 0) + 1
    probe = [len(stabilizer(det, st, PREP_FULL, 5))
             for st in (RHO, grid_states()[0], grid_states()[2422])]
    probe_ok = probe == [sum(1 for sg in SYM5
                             if all(st[sg[j]] == st[j] for j in range(5)))
                         for st in (RHO, grid_states()[0],
                                    grid_states()[2422])]
    TABLES["full_group_scope_over_the_declared_simplex"] = {
        "states": len(grid_states()),
        "admitted_isomorphism_group_size_histogram":
            {S(k): v for k, v in sorted(hist.items())},
        "states_carrying_the_full_24": hist.get(24, 0),
        "states_with_a_trivial_group": hist.get(1, 0),
        "states_carrying_the_whole_120": hist.get(120, 0)}
    gate("L4-SCOPE", "covariance",
         "THE SCOPE OF THE FULL-GROUP HYPOTHESIS, COUNTED.  The class "
         "theorem needs the full 24-element admitted-isomorphism group, "
         "which is the automorphism group of the declared state's level "
         "partition (DET, REV, FUNNEL and the funnel closure being invariant "
         "under every relabelling).  Over the 4845 declared states of "
         "denominator 16 that group is carried by exactly 25 states; 1200 "
         "carry a TRIVIAL group, where the theorem has no content at all; "
         "and none carries the whole 120, the uniform state not being of "
         "denominator 16.  The emptiness the theorem delivers is purchased "
         "by the committed state's degeneracy, and this is its price.",
         bad == 0 and probe_ok and hist.get(24, 0) == 25
         and hist.get(1, 0) == 1200 and sum(hist.values()) == 4845,
         TABLES["full_group_scope_over_the_declared_simplex"], must_pass=True)


# --------------------------------------------------------------------------
# 8c.  THEOREM 6.1's HYPOTHESIS, MEASURED WHERE ITS CONCLUSION LIVES.
# --------------------------------------------------------------------------


def mono_type(vals, pairs):
    mono = anti = True
    for p, q in pairs:
        f, c = (p, q) if CB.refines(p, q) else (q, p)
        if vals[f] > vals[c]:
            mono = False
        if vals[f] < vals[c]:
            anti = False
    return ("monotone" if mono and not anti else
            "anti-monotone" if anti and not mono else
            "constant" if mono and anti else "neither")


def comparable_pairs(records):
    return [(p, q) for p, q in combinations(records, 2)
            if CB.refines(p, q) or CB.refines(q, p)]


def run_extension():
    prog("theorem 6.1's extension: off-fixture type against all-52 type")
    ALL = CB.parts_of(5)
    OFF = off_fixture()
    p_off, p_all = comparable_pairs(OFF), comparable_pairs(ALL)
    fns = dict((c[0], c[2]) for c in CANDIDATES)
    rows = []
    for cid in ("C1", "C4a", "C4c"):
        for lname in ("DET", "FUNNEL", "COUNTER-LAW"):
            law = LAW5[lname]
            vals = {p: fns[cid](p, law, PREP_FULL, RHO, 5) for p in ALL}
            t_off = mono_type({p: vals[p] for p in OFF}, p_off)
            t_all = mono_type(vals, p_all)
            if MUTANT == "ext-lax":
                t_all = "neither"
            rows.append({"candidate": cid, "law": lname,
                         "type_off_fixture": t_off, "type_over_all_52": t_all,
                         "agree": t_off == t_all})
    TABLES["monotonicity_type_extension"] = {
        "off_fixture_comparable_pairs": len(p_off),
        "all_52_comparable_pairs": len(p_all), "rows": rows}
    gate("L4-EXT", "derivation",
         "THEOREM 6.1's HYPOTHESIS IS MEASURED OFF-FIXTURE AND ITS "
         "CONCLUSION IS ABOUT THE FIXTURE CHAIN, which is not in that "
         "population: off-fixture monotonicity does not ENTAIL monotonicity "
         "across the chain.  The extension is therefore measured here and "
         "not asserted: over the 224 comparable off-fixture pairs and the "
         "306 comparable pairs of the whole 52-record lattice, the "
         "monotonicity type is the SAME in all nine (candidate, law) cases "
         "-- C1, C4a and C4c at DET, FUNNEL and the counter-law.  The "
         "theorem is restated with the measured hypothesis.",
         all(r["agree"] for r in rows) and len(p_off) == 224
         and len(p_all) == 306, TABLES["monotonicity_type_extension"],
         must_pass=True)


# --------------------------------------------------------------------------
# 8d.  THE PANEL CLASS, and THE FUSED THEOREM measured over the NAME-BLIND
#      class at every committed configuration.
# --------------------------------------------------------------------------


def sweep(fn, law):
    sep = tie = inv = 0
    for st in grid_states():
        v1 = fn(PI1, law, PREP_FULL, st, 5)
        v2 = fn(P22, law, PREP_FULL, st, 5)
        vl = fn(PTOMO, law, PREP_FULL, st, 5)
        if vl > v1 or vl > v2:
            inv += 1
        elif vl < v1 and vl < v2:
            sep += 1
        else:
            tie += 1
    return sep, tie, inv


def c1_coefficients(part, law, n):
    """C1 IS LINEAR IN THE DECLARED STATE: C1 = sum_j rho_j c_j, where c_j
    counts the admitted preparations at which j's declared atom is unreached.
    Gated equal to the direct evaluation, and it makes C1's monotonicity type
    computable at EVERY declared state rather than at the committed one."""
    c = [0] * n
    if MUTANT == "c1state-lax":
        return c
    succ = succ_of(law, part, n)
    for pr in preps_of(n):
        R = reach_from_succ(succ, pr)
        for r in part:
            if not (set(r) & R):
                for j in r:
                    c[j] += 1
    return c


def run_c1_over_the_simplex():
    """The measurement Section 5 needs and the delivered analysis argued for
    instead: C1 is state-DEPENDENT, so its immunity to the sweep is not
    structural.  It is measured, exhaustively."""
    prog("C1's monotonicity type at every one of the 4845 declared states")
    OFF = off_fixture()
    pairs = comparable_pairs(OFF)
    rows = []
    for lname in ("FUNNEL", "COUNTER-LAW"):
        law = LAW5[lname]
        coef = {p: c1_coefficients(p, law, 5) for p in OFF}
        d = sum(1 for p in OFF
                if sum((RHO[j] * coef[p][j] for j in range(5)), Fr(0))
                != c1_counterfactual_occupancy(p, law, PREP_FULL, RHO, 5))
        anti = 0
        for st in grid_states():
            vals = {p: sum((st[j] * coef[p][j] for j in range(5)), Fr(0))
                    for p in OFF}
            if mono_type(vals, pairs) == "anti-monotone":
                anti += 1
        rows.append({"law": lname, "route_disagreements_at_the_committed_"
                     "state": d, "states": len(grid_states()),
                     "states_at_which_C1_is_anti_monotone": anti})
    TABLES["c1_monotonicity_over_the_simplex"] = rows
    gate("L4-C1STATE", "amnesty",
         "C1's MONOTONICITY TYPE AT EVERY DECLARED STATE.  C4c is state-blind "
         "and its type is state-free by construction; C1 is NOT -- omega "
         "reads rho -- so its immunity to the amnesty sweep is a measurement "
         "and not a structural property, and the measurement is made here "
         "rather than argued.  C1 is linear in the declared state (two "
         "routes, 0 disagreements at the committed state), and over the 224 "
         "comparable off-fixture pairs it is anti-monotone at ALL 4845 "
         "declared states, at FUNNEL and at the counter-law alike.  That is "
         "why no state inverts it -- and the general claim that a monotone "
         "separator is immune by construction is false for state-dependent "
         "statistics (see D5).",
         all(r["route_disagreements_at_the_committed_state"] == 0
             and r["states_at_which_C1_is_anti_monotone"] == 4845
             for r in rows), rows, must_pass=True)


def run_panel():
    prog("the panel class: nine constructions, declared post-fixture, gated")
    OFF = off_fixture()
    pairs = comparable_pairs(OFF)
    reg = []
    for cid, name, fn in PANEL:
        reg.append({"id": cid, "name": name,
                    "declared": "AFTER the fixture was known -- a "
                                "construction against this unit, not a "
                                "candidate of the hunt",
                    "definition_sha256": hashlib.sha256(
                        inspect.getsource(fn).encode()).hexdigest()[:16],
                    "docstring": " ".join(fn.__doc__.split())})
    TABLES["the_panel_class"] = reg
    gate("L4-00B", "panel",
         "THE PANEL CLASS, DECLARED AND HASHED.  Nine further statistics, "
         "none of them a hunt candidate: each was constructed AGAINST the "
         "delivered unit with the fixture already known, and each is carried "
         "here because a corridor that only ever meets its author's "
         "constructions has not been tested.  They are declared as "
         "post-fixture, hashed like the six, gated by the same battery, and "
         "evaluated only after the barrier.  TUNE is the permanent negative "
         "control of the freeze audit.",
         len(reg) == len(PANEL), len(reg), must_pass=True)
    rows = []
    for cid, name, fn in PANEL:
        for lname, law in committed_laws5():
            r = corridor_row(cid, fn, lname, law, OFF, pairs,
                             img_key="post-barrier (panel class)")
            v1 = fn(PI1, law, PREP_FULL, RHO, 5)
            v2 = fn(P22, law, PREP_FULL, RHO, 5)
            vl = fn(PTOMO, law, PREP_FULL, RHO, 5)
            ve = fn(ONEATOM5, law, PREP_FULL, RHO, 5)
            sp = separates(vl, v1, v2)
            r.update({"forged_2+1+1": S(v1), "forged_2+2": S(v2),
                      "legitimate_tomographic": S(vl), "total_erasure": S(ve),
                      "separates": sp,
                      "certifies_total_erasure_at_that_tolerance":
                          bool(sp and ve <= vl)})
            if sp:
                s, t, i = sweep(fn, law)
                r.update({"sweep_separating": s, "sweep_tied": t,
                          "sweep_INVERTING": i})
            rows.append(r)
    TABLES["panel_class_gates"] = rows
    by = {(r["candidate"], r["law"]): r for r in rows}
    d3 = [r for r in rows if r["candidate"] == "D3"]
    tune = [r for r in rows if r["candidate"] == "TUNE"]
    c5 = [r for r in rows if r["candidate"] == "C5"]
    d5 = [r for r in rows if r["candidate"] == "D5"]
    d5n = [r for r in rows if r["candidate"] == "D5N"]
    scan = {r["definition"]: r for r in TABLES["freeze_source_scan"]}
    corpses = {
        "D3 (R2)": {"dies_at": "the name-blindness gate",
                    "name_blind": any(r["GNB_name_blind"] for r in d3),
                    "two_boundaries_of_the_SAME_shape_it_separates":
                        {"{01|2|3|4}": S(d3_label_reader(
                            ((0, 1), (2,), (3,), (4,)), LAW5["DET"],
                            PREP_FULL, RHO, 5)),
                         "{02|1|3|4}": S(d3_label_reader(
                             ((0, 2), (1,), (3,), (4,)), LAW5["DET"],
                             PREP_FULL, RHO, 5)),
                         "same_shape_invariant": shape_invariant(
                             ((0, 1), (2,), (3,), (4,)), RHO)
                         == shape_invariant(((0, 2), (1,), (3,), (4,)), RHO)},
                    "would_otherwise_pass": all(
                        r["separates"] and r["G3_nondegenerate"]
                        and r["G2b_not_a_function_of_the_covariant_invariant"]
                        and r["monotonicity_type"] == "neither" for r in d3),
                    "sweep_INVERTING": [r.get("sweep_INVERTING") for r in d3]},
        "TUNE (R3)": {"dies_at": "the name-blindness gate AND the source scan",
                      "name_blind": any(r["GNB_name_blind"] for r in tune),
                      "caught_by_the_source_scan": not scan[
                          "tune_negative_control (NEGATIVE CONTROL)"]["clean"],
                      "sweep_INVERTING":
                          [r.get("sweep_INVERTING") for r in tune]},
        "C5 (R1)": {"dies_at": "the amnesty sweep (state relabelling)",
                    "name_blind": all(r["GNB_name_blind"] for r in c5),
                    "refuses_total_erasure": all(
                        not r["certifies_total_erasure_at_that_tolerance"]
                        for r in c5 if r["separates"]),
                    "at_the_relabelled_state_(3/4,1/16,1/16,1/16,1/16)":
                        [S(c5_marked_block_penalty(p, LAW5["DET"], PREP_FULL,
                                                   RHO_REL, 5))
                         for p in (PI1, P22, PTOMO)],
                    "sweep_INVERTING": [r.get("sweep_INVERTING") for r in c5]},
        "D5 (R2)": {"dies_at": "the name-blindness gate as written; its "
                               "name-blind completion D5N at the sweep",
                    "name_blind": any(r["GNB_name_blind"] for r in d5),
                    "monotonicity_type_at_the_committed_state":
                        sorted({r["monotonicity_type"] for r in d5}),
                    "sweep_INVERTING_literal":
                        [r.get("sweep_INVERTING") for r in d5],
                    "sweep_INVERTING_name_blind_completion":
                        [r.get("sweep_INVERTING") for r in d5n]}}
    TABLES["the_counterexample_corpses"] = corpses
    gate("L4-CORPSE", "panel",
         "THE FOUR COUNTEREXAMPLE CORPSES, EACH AT ITS NAMED GATE.  D3 and "
         "TUNE compare carrier NAMES and die at the name-blindness gate -- "
         "TUNE twice over, since the source scan catches it as well, which "
         "is the point of a negative control.  C5 is name-blind and refuses "
         "total erasure, and the amnesty sweep inverts it, because the "
         "datum it adds to the pair-resolution index is the declared "
         "state's, and the state moves.  D5 as written reads a "
         "configuration by name; its name-blind completion is measured "
         "ANTI-MONOTONE at the committed state and the sweep inverts it "
         "anyway -- which refutes 'a monotone separator passes the amnesty "
         "gate by construction' for state-dependent statistics.",
         (not any(r["GNB_name_blind"] for r in d3))
         and (not any(r["GNB_name_blind"] for r in tune))
         and (not scan["tune_negative_control (NEGATIVE CONTROL)"]["clean"])
         and all(r["GNB_name_blind"] for r in c5)
         and all(r.get("sweep_INVERTING", 0) > 0 for r in c5
                 if r["separates"])
         and all(r.get("sweep_INVERTING", 0) > 0 for r in d5n
                 if r["separates"]),
         corpses, must_pass=True)
    return rows


def run_fused():
    prog("the fused theorem, measured over the name-blind class")
    fx = {(r["candidate"], r["law"]): r for r in TABLES["fixture_values"]}
    am = {(r["candidate"], r["law"]): r for r in TABLES["amnesty_sweep"]}
    rows = []
    for r in TABLES["corridor_gates_off_fixture"]:
        k = (r["candidate"], r["law"])
        rows.append({**r, "separates": fx[k]["separates"],
                     "sweep_INVERTING": am[k]["INVERTING_states"]
                     if k in am else None,
                     "certifies_total_erasure_at_that_tolerance":
                         fx[k]["certifies_total_erasure_at_that_tolerance"]})
    rows += TABLES["panel_class_gates"]
    meas = []
    for r in rows:
        if not r["separates"]:
            continue
        arms = []
        if not r["G2b_not_a_function_of_the_covariant_invariant"]:
            arms.append("resolution-reading: a function of the covariant "
                        "shape invariant (resolution profile refined by the "
                        "declared state's level classes)")
        if r["monotonicity_type"] in ("monotone", "anti-monotone"):
            arms.append("order-entailed: the verdict is the committed "
                        "chain's own order (Theorem 6.1)")
        if r.get("sweep_INVERTING"):
            arms.append("state-reading: the amnesty sweep inverts it")
        meas.append({"candidate": r["candidate"], "law": r["law"],
                     "name_blind": r["GNB_name_blind"],
                     "arms": arms, "unaccounted": not arms,
                     "sweep_INVERTING": r.get("sweep_INVERTING"),
                     "certifies_total_erasure":
                         r["certifies_total_erasure_at_that_tolerance"]})
    TABLES["the_fused_claim_measured"] = meas
    nb = [m for m in meas if m["name_blind"]]
    nnb = [m for m in meas if not m["name_blind"]]
    robust_nb = [m for m in nb if m["unaccounted"]]
    robust_nnb = [m for m in nnb if m["unaccounted"]]
    if MUTANT == "fused-lax":
        robust_nb = robust_nb + ["MUTANT"]
    FINDINGS["the_fused_claim_over_the_name_blind_class"] = {
        "separating_rows_measured": len(meas),
        "name_blind_separating_rows": len(nb),
        "name_blind_rows_unaccounted_by_any_arm": len(robust_nb),
        "label_reading_rows_unaccounted_by_any_arm": len(robust_nnb),
        "the_label_readers_that_would_otherwise_survive":
            sorted({m["candidate"] for m in robust_nnb})}
    gate("L4-FUSED", "verdict",
         "THE FUSED CLAIM, MEASURED OVER THE NAME-BLIND CLASS AT EVERY "
         "COMMITTED CONFIGURATION.  Every separating (statistic, law) row of "
         "the whole declared-plus-panel class that passes the name-blindness "
         "gate falls to at least one of the three arms: it is a function of "
         "the covariant shape invariant (resolution data relative to the "
         "declared state's level partition), or its verdict is entailed by "
         "the committed chain's order, or the amnesty sweep inverts it.  "
         "None is unaccounted; there is no robust name-blind separator at "
         "any committed law.  The gate is not vacuous: the rows that ARE "
         "unaccounted are exactly the label-reading constructions, which "
         "separate, are not order-entailed and no state inverts -- and which "
         "the name-blindness gate takes.",
         not robust_nb and bool(robust_nnb),
         FINDINGS["the_fused_claim_over_the_name_blind_class"],
         must_pass=True)
    return meas


# --------------------------------------------------------------------------
# 9.  DERIVATION CROSS-CHECKS.  Two routes per candidate where a second
#     route exists; these are the gates the derivation mutants must break.
# --------------------------------------------------------------------------


def run_crosschecks():
    prog("derivation cross-checks: two independent routes per object")
    OFF = off_fixture()
    det = LAW5["DET"]
    d = sum(1 for p in OFF
            if c4a_state_alignment(p, det, PREP_FULL, RHO, 5)
            != c4a_route2(p, det, PREP_FULL, RHO, 5))
    gate("L4-X1", "derivation",
         "C4a computed by two independent routes -- per-atom level-class "
         "membership, and the atom's level-closure -- over the 48 "
         "off-fixture records: zero disagreements.", d == 0, d, must_pass=True)

    bad = 0
    for lname, law in committed_laws5():
        for p in OFF:
            fam = my_pres(law, p)
            if L2.has_identity(law, 5) and my_ker(fam, 5) != DISC5:
                bad += 1
    gate("L4-X2", "derivation",
         "THE GENERATED STRUCTURE AT AN IDENTITY-CONTAINING LAW IS DISCRETE. "
         "Every committed law contains the identity, the identity preserves "
         "every boundary, and its collision partition is discrete, so "
         "ker(Pres_L(pi)) is discrete at every off-fixture record and every "
         "committed law: 0 exceptions.  This is why C2 collapses.",
         bad == 0, bad, must_pass=True)

    diff = 0
    for lname, law in committed_laws5():
        for p in OFF:
            if (c2_generation_mismatch(p, law, PREP_FULL, RHO, 5)
                    != my_eps(p, my_pres(law, p), RHO)):
                diff += 1
    gate("L4-X3", "derivation",
         "C2 IS eps.  The generation-profile mismatch equals the concordance "
         "defect at every off-fixture record under every committed law -- "
         f"240 instances, {diff} disagreements -- a consequence of L4-X2 and "
         "the closed form, measured before it is used.",
         diff == 0, diff, must_pass=True)

    pop = law_population(5)
    ok = all(any(_famkey(Lp) == _famkey(law) for Lp in pop)
             for _, law in committed_laws5())
    gate("L4-X4", "derivation",
         "C3's declared law population at five configurations contains every "
         "committed law and is closed under composition member-wise.",
         ok and all(L2.is_composition_closed(Lp) for Lp in pop[:64]),
         {"population_size": len(pop)}, must_pass=True)

    inv = all(c4c_pair_resolution(act_part(p, g), det, PREP_FULL, RHO, 5)
              == c4c_pair_resolution(p, det, PREP_FULL, RHO, 5)
              for p in OFF for g in stab_of("DET", det, RHO, PREP_FULL, 5))
    gate("L4-X5", "derivation",
         "C4c is invariant under every admitted isomorphism, as the maximal "
         "covariant candidate must be.", inv, None, must_pass=True)

    d2 = 0
    for p in OFF:
        fam = my_pres(det, p)
        for pr in preps_of(5):
            if omega_fast(p, det, pr, RHO, 5) != my_omega(p, fam, pr, RHO, 5):
                d2 += 1
        if (omega_fast(p, det, PREP_FULL, RHO, 5)
                != L3.occupancy_defect(p, L2.pres_of(det, p), PREP_FULL,
                                       RHO, 5)):
            d2 += 1
    cl = LAW5["COUNTER-LAW"]
    nz = 0
    for p in OFF:
        for pr in (frozenset({0}), frozenset({4}), frozenset({0, 4})):
            a1 = omega_fast(p, cl, pr, RHO, 5)
            a2 = L3.occupancy_defect(p, L2.pres_of(cl, p), pr, RHO, 5)
            d2 += (a1 != a2)
            nz += (a2 != 0)
    gate("L4-X6", "derivation",
         "C1's underlying occupancy defect by THREE routes: the successor "
         "closure against the family saturation over all 48 off-fixture "
         "records at all 31 admitted preparations (1488 instances), and "
         "both against the terminal module's own route at the declared "
         f"preparation (48 more), and at the COUNTER-LAW at three declared "
         f"preparations where the defect is genuinely non-zero ({nz} of 144 "
         f"instances carry omega > 0).  {d2} disagreements.",
         d2 == 0 and nz > 0, [d2, nz], must_pass=True)

    ident = tuple(range(5))
    gate("L4-X7", "derivation",
         "THE SEPARATION PREDICATE IS THE CORPUS'S OWN.  A candidate "
         "separates iff a tolerance admits the legitimate patch and rejects "
         "both forged ones, so it is irreflexive (equal values never "
         "separate) and oriented (only the legitimate side may be the low "
         "one).  And the admitted-isomorphism action is an action: the "
         "identity relabelling fixes every one of the 52 records.",
         (not separates(Fr(1), Fr(1), Fr(1)))
         and separates(Fr(0), Fr(1), Fr(1))
         and (not separates(Fr(1), Fr(0), Fr(1)))
         and all(act_part(p, ident) == p for p in CB.parts_of(5)),
         None, must_pass=True)


# --------------------------------------------------------------------------
# 10.  VERDICT.
# --------------------------------------------------------------------------


def verdict():
    rows = TABLES["fixture_values"]
    amn = TABLES.get("amnesty_sweep", [])
    per = []
    order = ["G3_nondegenerate", "G1_not_refinement_monotone",
             "G2a_not_a_function_of_eps",
             "G2b_not_a_function_of_the_covariant_invariant", "G5_covariant"]
    order_t = ["G3_nondegenerate", "G1t_non_monotone_in_the_refinement_order",
               "G2a_not_a_function_of_eps",
               "G2b_not_a_function_of_the_covariant_invariant", "G5_covariant"]
    ent = {(e["candidate"], e["law"]): e
           for e in TABLES["why_each_separation_happens"]}
    g6 = {r["candidate"]: r for r in TABLES["identity_free_side"]}
    for cid, name, fn in CANDIDATES:
        mine = [r for r in TABLES["corridor_gates_off_fixture"]
                if r["candidate"] == cid]
        alive = [r for r in mine if all(r[k] for k in order)]
        seplaws = [r["law"] for r in rows
                   if r["candidate"] == cid and r["separates"]]
        inv = [r for r in amn if r["candidate"] == cid
               and r["INVERTING_states"] > 0]
        if not alive:
            first = None
            for k in order:
                if not any(r[k] for r in mine):
                    first = k
                    break
            killer = f"corridor {first}"
            outcome = "KILLED IN THE CORRIDOR"
        elif not seplaws:
            killer = "G7 separation on the committed pairs"
            outcome = "NO SEPARATION"
        elif inv:
            killer = "G4 the amnesty sweep"
            outcome = "FINGERPRINT-AMNESTY"
        else:
            killer = "none"
            outcome = "SEPARATOR"
        alive_t = [r for r in mine if all(r[k] for k in order_t)]
        if not alive_t:
            outcome_t = "KILLED IN THE INHERITED CORRIDOR"
            killer_t = "inherited gate 1 (non-monotone in the refinement "\
                       "order), stage-5 sec 10" \
                if not any(r["G1t_non_monotone_in_the_refinement_order"]
                           for r in mine) else killer
        elif not seplaws:
            outcome_t, killer_t = "NO SEPARATION", killer
        elif inv:
            outcome_t, killer_t = "FINGERPRINT-AMNESTY", "G4 the amnesty sweep"
        else:
            outcome_t, killer_t = "SEPARATOR", "none"
        per.append({"candidate": cid, "name": name, "outcome": outcome,
                    "killing_gate": killer,
                    "outcome_inherited_corridor": outcome_t,
                    "killing_gate_inherited_corridor": killer_t,
                    "corridor_laws": [r["law"] for r in alive],
                    "separating_laws": seplaws,
                    "order_entailed_separation":
                        [l for l in seplaws
                         if ent[(cid, l)]
                         ["separation_entailed_by_the_refinement_order"]],
                    "identity_free_side_intact": g6[cid]["G6_side_intact"],
                    "amnesty_verdict": ("FINGERPRINT-AMNESTY" if inv else
                                        "survives the sweep" if seplaws
                                        else "not reached"),
                    "inverting_states": (inv[0]["INVERTING_states"]
                                         if inv else 0)})
    TABLES["per_candidate_verdicts"] = per
    survivors = [p["candidate"] for p in per if p["outcome"] == "SEPARATOR"]
    survivors_t = [p["candidate"] for p in per
                   if p["outcome_inherited_corridor"] == "SEPARATOR"]
    amn_ids = sorted({r["candidate"] for r in amn
                      if r["INVERTING_states"] > 0})
    dich = all((e["separation_entailed_by_the_refinement_order"]
                != (e["candidate"] in amn_ids))
               for e in TABLES["why_each_separation_happens"])
    amnesties = sorted({r["candidate"] for r in amn
                        if r["INVERTING_states"] > 0})
    # -- THE C1 DISQUALIFICATION, its grounds in the order of their force.
    ent_c1 = [e for e in TABLES["why_each_separation_happens"]
              if e["candidate"] == "C1"]
    idf = {r["candidate"]: r for r in TABLES["identity_free_side"]}
    rows_c1 = [r for r in TABLES["corridor_gates_off_fixture"]
               if r["candidate"] == "C1"]
    grounds = [
        {"rank": 1, "ground": "ORDER-ENTAILMENT.  C1 is measured "
         "anti-monotone in the refinement order -- off-fixture and, by "
         "L4-EXT, over the whole 52-record lattice -- and the committed "
         "triple is a chain whose coarsest member is the legitimate patch, "
         "so its verdict is the order's and reads no provenance.  The "
         "terminal cycle adjudicated exactly this case on exactly these rows "
         "(A17, A18, A19).",
         "independently_sufficient": True,
         "measured": all(e["separation_entailed_by_the_refinement_order"]
                         for e in ent_c1)},
        {"rank": 2, "ground": "TOTAL ERASURE.  The tolerance that admits the "
         "legitimate chart and rejects both forgeries also admits the "
         "one-atom boundary, which forgets the entire carrier.",
         "independently_sufficient": True,
         "measured": all(
             e["certifies_total_erasure_at_the_separating_tolerance"]
             for e in ent_c1)},
        {"rank": 3, "ground": "THE IDENTITY-FREE SIDE.  C1 takes 3 distinct "
         "values on the 745 admissible patches at identity-free censused "
         "laws, where eps takes one, so it splits the side on which proper "
         "charts live.", "independently_sufficient": False,
         "measured": not idf["C1"]["G6_side_intact"]},
        {"rank": 4, "ground": "THE COVARIANCE GATE IS VACUOUS AT THE "
         "COUNTER-LAW -- and this carries NO INFORMATION.  A vacuous "
         "universal quantification is satisfied, not evaded: nothing about "
         "C1 was tested.  The correct accounting is not that C1 failed a "
         "gate but that C1 was SCREENED BY FOUR GATES, NOT FIVE.  A "
         "symmetry-free configuration is an admissible configuration.",
         "independently_sufficient": False,
         "measured": any(r["G5_vacuous_no_admitted_isomorphism"]
                         for r in rows_c1)}]
    TABLES["the_c1_disqualification"] = grounds
    gate("L4-C1-DQ", "verdict",
         "THE DISQUALIFICATION OF THE ONE CORRIDOR SURVIVOR, ITS GROUNDS IN "
         "THE ORDER OF THEIR FORCE.  Order-entailment and total erasure are "
         "each independently sufficient and each bites at EVERY committed "
         "law, symmetric or not; the identity-free split is collateral; the "
         "vacuous covariance gate is not a ground at all but a statement "
         "that one of five gates did not test C1.  And the separating "
         "content is not new: C1 is the sum of omega over the same 31 "
         "preparations whose rows the terminal cycle already counted and "
         "already dismissed -- 15 of 155, 12 at FUNNEL and 3 at the "
         "counter-law (A19), 'a grading of coarseness with the sign flipped "
         "rather than a reading of provenance' (A17, verbatim).",
         all(g["measured"] for g in grounds), grounds, must_pass=True)
    tags = []
    if amnesties:
        tags.append("RQ0-L4-FINGERPRINT-AMNESTY")
    tags.append("RQ0-L4-CLASS-IMPOSSIBILITY (the fused theorem at "
                "full-group configurations; measured over the name-blind "
                "class at every committed configuration)")
    tags.append("RQ0-L4-BLOCKED-AT-THE-REFINEMENT-ORDER")
    FINDINGS["registered_outcomes"] = tags
    FINDINGS["withdrawn_outcomes"] = [
        "RQ0-L4-NOMOLOGICAL-FINGERPRINT -- WITHDRAWN.  The pin's letter is "
        "met by C1 at the counter-law and the letter is not the finding: "
        "C1's separating content is the immutable base's own already-counted "
        "and already-dismissed omega rows (A17, A18, A19), and the tag is "
        "disqualified on order-entailment and on total erasure, each "
        "independently sufficient (L4-C1-DQ).  Registering it would "
        "re-register an adjudicated negative as a positive."]
    FINDINGS["the_pins_letter_survivor_before_withdrawal"] = survivors
    FINDINGS["survivors_pinned_corridor"] = survivors
    FINDINGS["survivors_inherited_corridor"] = survivors_t
    FINDINGS["amnesty_kills"] = amnesties
    FINDINGS["the_fingerprint_dichotomy"] = dich
    gate("L4-DICH", "verdict",
         "THE XOR TALLY OVER THE DECLARED FAMILY -- AN OBSERVATION, NOT A "
         "THEOREM.  Over the separating rows of the six declared candidates, "
         "each separation is EITHER entailed by the refinement order OR "
         "inverted by the amnesty sweep, and none is both.  This is a "
         "property of the declared family and not of statistics on declared "
         "data, and the panel class shows why: D1 is in NEITHER arm "
         "(state-blind, non-monotone, never inverted) and D5N is in BOTH "
         "(anti-monotone at the committed state and inverted anyway).  The "
         "claim that carries the verdict is not this tally but L4-FUSED.",
         dich, [{"candidate": e["candidate"], "law": e["law"],
                 "order_entailed":
                     e["separation_entailed_by_the_refinement_order"]}
                for e in TABLES["why_each_separation_happens"]])
    return per, tags


# --------------------------------------------------------------------------
# 11.  RECEIPT AND RENDERING.  No wall-clock anywhere.
# --------------------------------------------------------------------------


def build_receipt():
    return {
        "schema": SCHEMA, "unit": "RQ0-L4 branch C -- the nomological "
        "fingerprint hunt", "pin_commit": PIN_COMMIT,
        "base_commit": BASE_COMMIT, "source_sha256": SOURCE_SHA256,
        "arithmetic": "exact rationals throughout; no float in any "
                      "substantive path",
        "the_freeze_is_carried_by": [
            "L4-00: the SHA-256 of every candidate definition's source text, "
            "registered before any fixture value is computed",
            "L4-SRC: an automated scan of that source for any reference to a "
            "committed boundary, self-tested against a negative control"],
        "the_freeze_is_NOT_carried_by": [
            "the gate order, which cannot establish authoring order",
            "the per-gate stage annotation, which records the stage a gate "
            "was written into and not what the run evaluated",
            "any claim that no candidate was evaluated at a committed "
            "boundary: the orbit gates force such evaluations and L4-IMG "
            "counts them"],
        "anchors": ANCHORS, "gates": GATES, "tables": TABLES,
        "findings": FINDINGS,
        "totals": {"anchors": len(ANCHORS),
                   "anchors_passed": sum(1 for a in ANCHORS if a["passed"]),
                   "gates": len(GATES),
                   "gates_passed": sum(1 for g in GATES if g["passed"]),
                   "must_pass_gates": sum(1 for g in GATES if g["must_pass"]),
                   "must_pass_failures":
                       sum(1 for g in GATES
                           if g["must_pass"] and not g["passed"]),
                   "candidates": len(CANDIDATES)},
    }


def render(rec) -> str:
    L = []
    A = L.append
    A("RQ0-L4 BRANCH C -- THE NOMOLOGICAL FINGERPRINT HUNT")
    A("=" * 78)
    A(f"pin {rec['pin_commit']}   base {rec['base_commit']}")
    A(f"source sha256 {rec['source_sha256'][:32]}")
    A("")
    A("THE DECLARED CANDIDATE FAMILY (frozen before any fixture value)")
    A("-" * 78)
    for c in rec["tables"]["the_declared_candidate_family"]:
        A(f"  {c['id']:<4} {c['name']}")
        A(f"       def sha256 {c['definition_sha256']}   "
          f"orientation: {c['orientation']}")
    A("")
    A("CORRIDOR GATES, OFF-FIXTURE POPULATION ONLY (48 records)")
    A("-" * 78)
    A(f"  {'cand':<5}{'law':<16}{'G3':<5}{'type':<14}{'G1':<5}{'G2a':<6}"
      f"{'G2b':<6}{'G5':<5}")
    for r in rec["tables"]["corridor_gates_off_fixture"]:
        A(f"  {r['candidate']:<5}{r['law']:<16}"
          f"{('y' if r['G3_nondegenerate'] else 'n'):<5}"
          f"{r['monotonicity_type']:<14}"
          f"{('y' if r['G1_not_refinement_monotone'] else 'n'):<5}"
          f"{('y' if r['G2a_not_a_function_of_eps'] else 'n'):<6}"
          f"{('y' if r['G2b_not_a_function_of_the_covariant_invariant'] else 'n'):<6}"
          f"{('y' if r['G5_covariant'] else 'n'):<5}")
    A("")
    A("THE IDENTITY-FREE SIDE (745 admissible patches, eps = 0 throughout)")
    A("-" * 78)
    for r in rec["tables"]["identity_free_side"]:
        A(f"  {r['candidate']:<5} distinct values on the 745: "
          f"{r['distinct_values_on_the_745']:<6} "
          f"side intact: {'yes' if r['G6_side_intact'] else 'NO'}")
    A("")
    A("FIXTURE: THE COMMITTED DISTINCT-QUADRUPLE PAIRS")
    A("-" * 78)
    A(f"  {'cand':<5}{'law':<16}{'2+1+1':<10}{'2+2':<10}{'LEGIT':<10}"
      f"{'erasure':<10}sep")
    for r in rec["tables"]["fixture_values"]:
        A(f"  {r['candidate']:<5}{r['law']:<16}{r['forged_2+1+1']:<10}"
          f"{r['forged_2+2']:<10}{r['legitimate_tomographic']:<10}"
          f"{r['total_erasure']:<10}{'YES' if r['separates'] else 'no'}")
    A("")
    A("THE AMNESTY SWEEP (every separator, all 4845 declared states)")
    A("-" * 78)
    if rec["tables"].get("amnesty_sweep"):
        for r in rec["tables"]["amnesty_sweep"]:
            A(f"  {r['candidate']:<5}{r['law']:<16}"
              f"separating {r['separating_states']:<6}"
              f"tied {r['tied_states']:<6}"
              f"INVERTING {r['INVERTING_states']:<6}{r['verdict']}")
    else:
        A("  no separator reached the sweep")
    A("")
    A("WHY EACH SEPARATION HAPPENS")
    A("-" * 78)
    for r in rec["tables"]["why_each_separation_happens"]:
        A(f"  {r['candidate']:<5}{r['law']:<16}"
          f"{r['monotonicity_type_measured_off_fixture']:<15}"
          f"order-entailed: "
          f"{'YES' if r['separation_entailed_by_the_refinement_order'] else 'no ':<5}"
          f"certifies total erasure: "
          f"{'YES' if r['certifies_total_erasure_at_the_separating_tolerance'] else 'no'}")
    A("")
    A("THE ADMITTED-ISOMORPHISM ACTION")
    A("-" * 78)
    for r in rec["tables"]["admitted_isomorphism_action"]:
        A(f"  {r['law']:<16}isomorphisms {r['admitted_isomorphisms']:<5}"
          f"orbits of the 52 records {r['orbits_of_the_52_records']:<5}"
          f"orbit = shape: "
          f"{'yes' if r['orbit_invariant_is_the_shape_profile'] else 'NO'}")
    A("")
    A("SHAPE IS NOT RESOLUTION (the 12-vs-7 decomposition)")
    A("-" * 78)
    d = rec["tables"]["shape_is_not_resolution"]
    A(f"  covariant shape classes {d['orbit_classes_the_covariant_shape_invariant']}"
      f"   resolution-profile classes {d['resolution_profile_classes']}"
      f"   splitting profiles {d['resolution_profiles_that_split_into_two_orbits']}")
    A(f"  second route sum_s p(4-s) = {d['second_route_sum_over_s_of_p_4_minus_s']}"
      f"   orbit-size census {d['orbit_size_census']} = "
      f"{d['orbit_size_census_sums_to']}")
    A(f"  the splitting resolution profiles: {d['the_splitting_profiles']}")
    A(f"  marked-block excess at the committed triple: "
      f"{d['marked_block_excess_at_the_committed_triple']}")
    s = rec["tables"]["full_group_scope_over_the_declared_simplex"]
    A(f"  full-group scope over the {s['states']} declared states: "
      f"{s['states_carrying_the_full_24']} carry the full 24, "
      f"{s['states_with_a_trivial_group']} a trivial group, "
      f"{s['states_carrying_the_whole_120']} the whole 120")
    A(f"  group-size histogram {s['admitted_isomorphism_group_size_histogram']}")
    A("")
    A("THE NAME-BLINDNESS GATE, AND THE PANEL CLASS (declared post-fixture)")
    A("-" * 78)
    A(f"  {'stat':<6}{'law':<16}{'NB':<5}{'type':<14}{'G2b':<6}{'sep':<5}"
      f"{'erasure':<10}sweep INVERTING")
    for r in rec["tables"]["panel_class_gates"]:
        A(f"  {r['candidate']:<6}{r['law']:<16}"
          f"{('y' if r['GNB_name_blind'] else 'NO'):<5}"
          f"{r['monotonicity_type']:<14}"
          f"{('y' if r['G2b_not_a_function_of_the_covariant_invariant'] else 'n'):<6}"
          f"{('YES' if r['separates'] else 'no'):<5}"
          f"{r['total_erasure']:<10}"
          f"{r.get('sweep_INVERTING', '-')}")
    A("")
    A("THE FUSED CLAIM, MEASURED OVER THE NAME-BLIND CLASS")
    A("-" * 78)
    for r in rec["tables"]["the_fused_claim_measured"]:
        tail = ("REMOVED BY THE NAME-BLINDNESS GATE" if not r["name_blind"]
                else "UNACCOUNTED BY ANY ARM" if r["unaccounted"]
                else str(len(r["arms"])) + " arm(s): "
                + "; ".join(a.split(":")[0] for a in r["arms"]))
        A(f"  {r['candidate']:<6}{r['law']:<16}"
          f"{('name-blind' if r['name_blind'] else 'LABEL-READING'):<15}"
          f"{tail}")
    f = rec["findings"]["the_fused_claim_over_the_name_blind_class"]
    A(f"  name-blind separating rows {f['name_blind_separating_rows']}, "
      f"unaccounted by any arm {f['name_blind_rows_unaccounted_by_any_arm']}; "
      f"label-reading rows unaccounted "
      f"{f['label_reading_rows_unaccounted_by_any_arm']} "
      f"({f['the_label_readers_that_would_otherwise_survive']})")
    A("")
    A("THE DISQUALIFICATION OF THE PIN'S-LETTER SURVIVOR, IN ORDER OF FORCE")
    A("-" * 78)
    for g in rec["tables"]["the_c1_disqualification"]:
        A(f"  {g['rank']}. {' '.join(g['ground'].split())[:150]}")
        A(f"     independently sufficient: "
          f"{'YES' if g['independently_sufficient'] else 'no'}   measured: "
          f"{'yes' if g['measured'] else 'NO'}")
    A("")
    A("LAW-BLINDNESS ON THE COMMITTED PAIRS")
    A("-" * 78)
    for r in rec["tables"]["law_blindness"]:
        A(f"  {r['candidate']:<5}distinct value triples across the five "
          f"committed laws: "
          f"{r['distinct_value_triples_across_the_five_committed_laws']}"
          f"   law-blind: "
          f"{'YES' if r['law_blind_on_the_committed_pairs'] else 'no'}")
    A("")
    A("PER-CANDIDATE VERDICTS")
    A("-" * 78)
    for r in rec["tables"]["per_candidate_verdicts"]:
        A(f"  {r['candidate']:<5}pinned corridor  : {r['outcome']:<26}"
          f"killed by: {r['killing_gate']}")
        A(f"       inherited corridor: "
          f"{r['outcome_inherited_corridor']:<26}"
          f"killed by: {r['killing_gate_inherited_corridor']}")
        A(f"       amnesty sweep     : {r['amnesty_verdict']}"
          f"{'' if not r['inverting_states'] else ' at ' + str(r['inverting_states']) + ' of 4845 states'}")
        A(f"       corridor laws {r['corridor_laws']}   separating laws "
          f"{r['separating_laws']}   order-entailed at "
          f"{r['order_entailed_separation']}")
    A("")
    A("GATES")
    A("-" * 78)
    for g in rec["gates"]:
        A(f"  [{'PASS' if g['passed'] else 'fail'}] {g['id']:<16}"
          f"{'(must pass)' if g['must_pass'] else ''}")
        A(f"       {' '.join(g['claim'].split())[:300]}")
    A("")
    A("ANCHORS (exit-1-only)")
    A("-" * 78)
    for a in rec["anchors"]:
        A(f"  [{'PASS' if a['passed'] else 'FAIL'}] {a['id']:<6}"
          f"{a['quantity'][:66]}")
    A("")
    A("THE FREEZE, AS IT IS ACTUALLY CARRIED")
    A("-" * 78)
    for r in rec["tables"]["freeze_source_scan"]:
        A(f"  {r['definition']:<48}"
          f"{'clean' if r['clean'] else 'CAUGHT: ' + ','.join(r['fixture_references'])}")
    img = [g for g in rec["gates"] if g["id"] == "L4-IMG"][0]["value"]
    A(f"  orbit-forced evaluations at a committed boundary, pre-barrier: "
      f"{img['total_pre_barrier_evaluations_at_a_committed_boundary']}")
    A(f"    {img['per_gate']}")
    A("")
    A("REGISTERED OUTCOMES")
    A("-" * 78)
    for t in rec["findings"]["registered_outcomes"]:
        A(f"  {t}")
    A("")
    A("WITHDRAWN")
    A("-" * 78)
    for t in rec["findings"]["withdrawn_outcomes"]:
        A(f"  {' '.join(t.split())}")
    A("")
    t = rec["totals"]
    A(f"TOTALS: {t['anchors']} anchors ({t['anchors_passed']} passed), "
      f"{t['gates']} gates ({t['gates_passed']} passed), "
      f"{t['must_pass_gates']} must-pass "
      f"({t['must_pass_failures']} failures), "
      f"{t['candidates']} declared candidates")
    return "\n".join(L) + "\n"


MUTANTS = ["anchor:A03", "anchor:A04", "anchor:A08", "anchor:A10",
           "anchor:A11", "anchor:A13", "anchor:A15", "anchor:A17",
           "anchor:A18", "anchor:A19",
           "pres-lax", "eps-lax", "ker-lax", "reach-lax", "levelset-lax",
           "shape-lax", "stab-lax", "orbit-lax", "align-lax", "mismatch-lax",
           "fanin-lax", "freeze-lax", "sep-lax", "amnesty-lax",
           "nb-lax", "srcscan-lax", "ext-lax", "fused-lax", "scope-lax",
           "c1state-lax"]


def _run_one_mutant(m: str) -> int:
    r = subprocess.run([sys.executable, str(Path(__file__).resolve()),
                        "--mutant", m, "--quiet"],
                       capture_output=True, text=True)
    return r.returncode


def run_falsification_selftest() -> int:
    """Every mutant must exit 1.  The mutants are run in parallel as
    independent subprocesses and reported in declaration order, so the
    report is deterministic and does not depend on completion order."""
    bad = []
    with ThreadPoolExecutor(max_workers=8) as ex:
        codes = list(ex.map(_run_one_mutant, MUTANTS))
    for m, code in zip(MUTANTS, codes):
        ok = (code == 1)
        sys.stdout.write(f"  mutant {m:<16} exit {code} "
                         f"{'OK' if ok else 'DID NOT DIE'}\n")
        if not ok:
            bad.append(m)
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
    L2.MUTANT = None
    L3.MUTANT = None

    run_anchors()
    declare_candidates()
    run_corridor()
    run_crosschecks()
    freeze_barrier()
    rows, seps = run_fixture()
    run_amnesty(seps)
    run_robustness(seps)
    run_covariance()
    run_extension()
    run_c1_over_the_simplex()
    run_panel()
    run_fused()
    per, tags = verdict()

    rec = build_receipt()
    txt = render(rec)
    if not a.mutant:
        OUT_TXT.write_text(txt)
        OUT_JSON.write_text(json.dumps(rec, indent=1, sort_keys=True) + "\n")
    if not a.quiet:
        sys.stdout.write("\n" + txt)
    fail = rec["totals"]["must_pass_failures"]
    prog(f"done: {rec['totals']['anchors']} anchors, "
         f"{rec['totals']['gates']} gates, {fail} must-pass failures")
    return 1 if fail else 0


if __name__ == "__main__":
    raise SystemExit(main())
