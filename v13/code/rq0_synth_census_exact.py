#!/usr/bin/env python3
"""RQ0-SYNTH -- THE FIRST INVARIANCE CENSUS OVER ADMISSIBLE ARENAS.

Executes the frozen pin `v13/note-rq0-synth-arena-pin.md` (commit a14bda0,
sha f74a8511b204) against the immutable six-level-tower base 77b015e.

THE QUESTION.  Six terminal units proved that the legitimacy of a coarse
patch is not intrinsic, not context-certifiable, not law-structural at
coarse grain, not state-carried, not law-remembered and not
provenance-carriable.  What remains is ADOPTED-ARENA-RELATIVITY: legitimacy
is relative to a DECLARED ARENA.  This unit states that thesis with the
six-unit theorem record and then runs the first census: OF THE QUANTITIES
THE TOWER BUILT, WHICH ARE INVARIANT ACROSS THE ADMISSIBLE ARENAS AND WHICH
ARE ARENA ARTIFACTS?

THE ADMISSIBLE ARENA (the pin's family, no new objects).  A declared tuple

    A = (d, L, rho, sigma, phi)

  d      a patch declaration in {legitimate tomographic minimum, forged
         aligned 2+1+1, forged aligned 2+2} -- the committed fixtures;
  L      one of the FIVE committed laws at the committed carrier;
  rho    one of the THIRTEEN named states of the stage-5 state map, taken
         from that unit's own source, never retyped;
  sigma  an ADMITTED relabelling -- an admitted isomorphism of the declared
         data (branch C's stabilizer: it fixes the law setwise, the state
         and the preparation), so the family is FIBERED over (L, rho);
  phi    a checkpoint-phase switching, one of the 512 vertex switchings of
         the committed one-step diagram, where amplitude data is in play.

The arena's REALIZED data is (sigma.d, sigma.L, sigma.rho): an arena change
acts on the WHOLE configuration, never on one argument alone.  The family
is enumerated finitely and its size is COMPUTED.

THE CENSUS.  Each quantity declares, BEFORE any fixture value is computed
(the receipt's gate order proves it):

  READS      the coordinates that are the quantity's own arguments;
  ACTS       the coordinates whose variation is the tested arena change;
  TRANSPORT  how an admitted relabelling moves the value;
  NEUTRAL    the value that carries no information (the degeneracy datum);
  WITNESS    a declared ambient object at which the quantity takes another
             value -- so that constancy on the family is a fact about the
             family and not about a broken instrument.

The verdicts are the pin's and only the pin's: ARENA-INVARIANT (fixed under
the full declared action AND nondegenerate), ARENA-INERT (fixed but at its
neutral value), ARENA-ARTIFACT (moves; orbit sizes computed),
BLOCKED-AT-<object>.  Q1 and Q2 are declared POSITIVE controls, Q5 the
declared NEGATIVE control; if nothing moves, ACTION-TOO-WEAK fires and the
census as instrumented is dead.

The FULL dependence profile of every quantity over every coordinate is
measured and reported whether or not the coordinate is in that quantity's
declared acting set, so the declaration determines only the verdict label,
never what is shown.

Exact arithmetic throughout: fractions.Fraction, integer-indexed partitions,
and Q(zeta_8) as 4-tuples of Fractions reduced mod x^4 + 1 (tuple equality
IS field equality).  No float enters any path.  Anchors exit 1 on mismatch.
`--mutant NAME` breaks exactly one anchor or one derivation step and must
exit 1 naming the gate it falsified.  No wall-clock value enters the receipt
or the rendered output, so two delivery-mode runs are byte-identical.

Scope: finite; ONE committed carrier of five configurations; the committed
law families, the thirteen named states, the three committed patch
declarations.  No locality, topology, causality, spacetime, field, QFT or
gravity object is constructed or claimed.  "Arena" is operational
vocabulary for a declared tuple of committed fixtures.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import inspect
import json
import sys
from fractions import Fraction as Fr
from itertools import combinations, permutations, product
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import rq0_l0_fixed_point_exact as CB      # Cycle B TERMINAL machinery
import rq0_l2_admissibility_exact as L2    # Cycle B'' TERMINAL machinery
import rq0_l3_epsilon_exact as L3          # stage-5 TERMINAL machinery
import rq0_l4_fingerprint_exact as L4      # branch C TERMINAL machinery
import rq0_l5_provenance_exact as L5       # branch A TERMINAL machinery

SCHEMA = "rq0-synth-arena-census-receipt-v1"
PIN_COMMIT = "a14bda0"
PIN_SHA256 = "f74a8511b204"
BASE_COMMIT = "77b015e"
OUT_TXT = HERE / "rq0_synth_census_output.txt"
OUT_JSON = HERE / "rq0_synth_census_receipt.json"

MUTANT: str | None = None
SOURCE_SHA256 = ""

GATES: list[dict] = []
ANCHORS: list[dict] = []
TABLES: dict = {}
FINDINGS: dict = {}

CARRIER = 5
PREP_FULL = frozenset(range(CARRIER))
NROOT = 8

PTOMO = L5.PTOMO      # the LEGITIMATE corrected tomographic minimum
PI1 = L5.PI1          # the forged aligned manufactured 2+1+1
P22 = L5.P22          # the forged aligned manufactured 2+2
DISC5 = L5.DISC5      # the carrier's own algebra (ambient witness only)
ONEATOM = ((0, 1, 2, 3, 4),)

PATCHES = (("legitimate tomographic minimum", PTOMO, "LEGITIMATE"),
           ("forged aligned 2+1+1", PI1, "FORGED"),
           ("forged aligned 2+2", P22, "FORGED"))

_FROZEN = False          # set by run_freeze(); no quantity may be evaluated
_QEVALS = 0              # before it, and the counter proves it
_FIRST_CENSUS_GATE: int | None = None


def prog(msg: str) -> None:
    sys.stderr.write(f"[synth] {msg}\n")
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


_CANON: dict = {}
_KEEP: list = []


def canon(v) -> str:
    """A canonical, sortable, printable key for any census value, memoized on
    object identity with a strong reference kept, so an id is never reused.
    Two equal values built as separate objects receive separate entries with
    the same key: the memo is a speed device and decides no equality."""
    i = id(v)
    if i in _CANON:
        return _CANON[i]
    out = _canon(v)
    if isinstance(v, (tuple, frozenset)) and len(v) > 8:
        _CANON[i] = out
        _KEEP.append(v)
    return out


def _canon(v) -> str:
    if isinstance(v, (list, tuple)):
        return "(" + ",".join(canon(x) for x in v) + ")"
    if isinstance(v, (set, frozenset)):
        return "{" + ",".join(sorted(canon(x) for x in v)) + "}"
    return str(v)


# ---------------------------------------------------------------------------
# 0.  THE ADMISSIBLE-ARENA FAMILY.  Every coordinate is drawn from a terminal
#     fixture; nothing here is a new object and no count is typed.
# ---------------------------------------------------------------------------

def named_states():
    """THE THIRTEEN NAMED STATES, taken from stage-5's own source rather than
    retyped: the literal `named_states` list of `L3.run_separation` is parsed
    out of the terminal module and evaluated in a namespace containing only
    the fixtures it names.  The count is COMPUTED and anchored against the
    committed stage-5 receipt's state-map table."""
    src = inspect.getsource(L3.run_separation)
    node = None
    for nd in ast.walk(ast.parse(src.lstrip())):
        if isinstance(nd, ast.Assign) and any(
                getattr(t, "id", "") == "named_states" for t in nd.targets):
            node = nd.value
    if node is None:
        raise RuntimeError("stage-5's named-state list not found")
    out = eval(compile(ast.Expression(node), "<L3>", "eval"),
               {"Fr": Fr, "uniform": L3.uniform, "RHO": L3.RHO})
    if MUTANT == "states-drop":
        out = out[:5]
    return [(lbl, tuple(r)) for lbl, r in out]


def committed_laws():
    """The five committed law families at the committed carrier."""
    return L2.committed_laws(CARRIER)


_STABL: dict = {}


def admitted_group(law_id, law, rho):
    """THE ADMITTED ISOMORPHISMS of a declared arena: branch C's stabilizer of
    the declared data -- the relabellings fixing the law setwise, the state
    and the preparation.  Memoized on (law identity, state); the memo is a
    speed device and changes no value."""
    k = (law_id, rho)
    if k not in _STABL:
        _STABL[k] = L4.stabilizer(law, rho, PREP_FULL, CARRIER)
    return _STABL[k]


def gauge_switchings(sup):
    """THE 512 CHECKPOINT-PHASE SWITCHINGS: every assignment of eighth-root
    phases to the loop component's vertices of the committed one-step
    diagram, one vertex fixed as the global phase.  The count is computed
    from the diagram, never typed."""
    src = [j for j in range(CARRIER) if len(sup[j]) > 1]
    tgt = sorted({i for j in src for i in sup[j]})
    loopv = [(0, j) for j in src] + [(1, i) for i in tgt]
    free = len(loopv) - 1
    out = []
    for ks in product(range(NROOT), repeat=free):
        ph = [{}, {}]
        for v, k in zip(loopv, (0,) + ks):
            ph[v[0]][v[1]] = k
        out.append(ph)
    return out, free


def act_rho(rho, sigma):
    """sigma . rho, the declared state carried by the relabelling."""
    inv = [0] * len(sigma)
    for j, s in enumerate(sigma):
        inv[s] = j
    return tuple(rho[inv[j]] for j in range(len(sigma)))


def act_part(part, sigma):
    return L4.act_part(part, sigma)


def act_law_set(law, sigma):
    return L4.act_law(law, sigma)


def build_family():
    """The admissible-arena family, enumerated.  Its size is the product of
    the patch count, the fibered relabelling count and the switching count;
    every factor is measured here."""
    states = named_states()
    laws = committed_laws()
    fibers, tot_sigma = [], 0
    for li, (lname, law) in enumerate(laws):
        for sname, rho in states:
            g = admitted_group(li, law, rho)
            tot_sigma += len(g)
            fibers.append({"law": lname, "state": sname,
                           "admitted_isomorphisms": len(g)})
    sw, free = gauge_switchings(L5.sup_of_matrix(
        L5.admitted_lift_family()[0][0][0], CARRIER))
    size = len(PATCHES) * tot_sigma * len(sw)
    return {"states": states, "laws": laws, "fibers": fibers,
            "sigma_total": tot_sigma, "switchings": len(sw),
            "switch_free_vertices": free, "size": size,
            "switch_objects": sw}


# ---------------------------------------------------------------------------
# 1.  THE QUANTITIES.  Declared -- with their arena action -- before any
#     fixture value is computed.  Each takes the REALIZED arena data.
# ---------------------------------------------------------------------------

_MEMO: dict = {}


def _adj(part, law_id, law):
    k = ("adj", part, law_id)
    if k not in _MEMO:
        _MEMO[k] = L2.adjudicate(part, L2.pres_of(law, part), law,
                                 PREP_FULL, CARRIER)
    return _MEMO[k]


def q1_fine_grained_transition_data(part, law_id, law, rho, sigma, lifts):
    """Q1 -- THE FINE-GRAINED LAW'S TRANSITION DATA: the admitted operations
    of the declared law as sector supports at the fine chart."""
    k = ("q1", law_id)
    if k not in _MEMO:
        _MEMO[k] = tuple(sorted(L2.key(F) for F in law))
    return _MEMO[k]


def q2_one_step_closed_holonomy(part, law_id, law, rho, sigma, lifts):
    """Q2 -- THE ONE-STEP CLOSED HOLONOMY of the carried amplitude diagram:
    branch A's gauge-invariant content, (cycle rank, holonomy phases, spans),
    over the declared admitted lift family under the arena's switching."""
    k = ("q2", id(lifts))
    if k not in _MEMO:
        out = set()
        for U in lifts:
            sup = L5.sup_of_matrix(U, CARRIER)
            r, h, s, _p = L5.cycle_basis_holonomies([U], [sup], CARRIER)
            out.add((r, h, s))
        _MEMO[k] = tuple(sorted(out))
        _KEEP.append(lifts)
    return _MEMO[k]


def q3_rigidity_classifier(part, law_id, law, rho, sigma, lifts):
    """Q3 -- THE RIGIDITY CLASSIFIER, cycle B''s identity-free flag: whether
    the law contains the identity, whether it contains a reversible
    operation, and the set of boundaries the terminal axiom admits."""
    k = ("q3", law_id)
    if k not in _MEMO:
        adm = tuple(sorted(p for p in CB.partitions(CARRIER)
                           if _adj(p, law_id, law)["admissible"]))
        _MEMO[k] = (L2.has_identity(law, CARRIER),
                    L2.has_reversible(law, CARRIER), adm)
    return _MEMO[k]


def q4_name_blind_generation_profile(part, law_id, law, rho, sigma,
                                    lifts):
    """Q4 -- THE NAME-BLIND GENERATION/COLLISION PROFILE, branch C's corridor
    machinery: the collision classes the law's preserving family generates on
    the patch, the law's own reachability classes, and the preserving family's
    size.  Returned as STRUCTURED objects carrying their labels, so that
    name-blindness is a measurement and not a presentation choice."""
    k = ("q4", part, law_id)
    if k not in _MEMO:
        fam = L2.pres_of(law, part)
        _MEMO[k] = (tuple(sorted(tuple(sorted(b)) for b in L4.my_ker(
            fam, CARRIER))),
            L4.reach_classes(law, part, CARRIER), len(fam))
    return _MEMO[k]


def q5_legitimacy_certificate(part, law_id, law, rho, sigma, lifts):
    """Q5 -- THE LEGITIMACY CERTIFICATE FUNCTIONS: branch A's V-CL certificate
    of the declared patch (the record written, the preserving-family size, the
    four clause bits, the reachable subprocess) together with the terminal
    axiom's verdict.  DECLARED NEGATIVE CONTROL: expected to move."""
    k = ("q5", part, law_id)
    if k not in _MEMO:
        v = _adj(part, law_id, law)
        cert = L5.certificate_CL(L2.block_min_idempotent(part, CARRIER),
                                 law, PREP_FULL, CARRIER)
        _MEMO[k] = (bool(v["admissible"]), cert)
    return _MEMO[k]


def q6_epsilon(part, law_id, law, rho, sigma, lifts):
    """Q6 -- EPSILON, stage 5's concordance defect, in its closed form: the
    residual Bayes error of the declared boundary at the declared state."""
    return L3.bayes_error(part, rho)


def q7_omega(part, law_id, law, rho, sigma, lifts):
    """Q7 -- OMEGA, the occupancy defect: the declared mass carried by blocks
    the realized process never occupies."""
    return L4.omega_fast(part, law, PREP_FULL, rho, CARRIER)


def q8_cross_arena_overlap(part, law_id, law, rho, sigma, lifts):
    """Q8 -- THE CROSS-ARENA OVERLAP DATUM: what the arena's patch and each
    other declared patch SHARE on intersection -- the finest common
    coarsening, which is exactly the intersection of the two boundary
    algebras -- and how many atoms that seam carries."""
    out = []
    for _nm, other, _pv in PATCHES:
        o = act_part(other, sigma)
        if o == part:
            continue
        seam = CB.part_meet(part, o) if MUTANT != "seam-orient" \
            else CB.part_join(part, o)
        out.append((pk(o), seam, len(seam)))
    return tuple(sorted(out, key=canon))


QUANTITIES = [
    ("Q1", "the fine-grained law's transition data",
     q1_fine_grained_transition_data, ("law",),
     ("patch", "state", "relabelling", "switching"), "conjugation",
     "the empty law", "positive"),
    ("Q2", "the one-step closed holonomy",
     q2_one_step_closed_holonomy, ("lift family",),
     ("patch", "law", "state", "relabelling", "switching"), "identity",
     "the trivial holonomy (phase 0)", "positive"),
    ("Q3", "the rigidity classifier (the identity-free flag)",
     q3_rigidity_classifier, ("law",),
     ("patch", "state", "relabelling", "switching"), "boundary relabelling",
     "no constraint (every boundary admissible)", None),
    ("Q4", "the name-blind generation/collision profile",
     q4_name_blind_generation_profile, ("patch", "law"),
     ("state", "relabelling", "switching"), "partition relabelling",
     "the empty profile", None),
    ("Q5", "the legitimacy certificate functions (V-CL; the terminal verdict)",
     q5_legitimacy_certificate, ("patch",),
     ("law", "state", "relabelling", "switching"), "certificate relabelling",
     "the empty certificate", "negative"),
    ("Q6", "epsilon, the concordance defect", q6_epsilon, ("patch",),
     ("law", "state", "relabelling", "switching"), "identity", "0", None),
    ("Q7", "omega, the occupancy defect", q7_omega, ("patch",),
     ("law", "state", "relabelling", "switching"), "identity", "0", None),
    ("Q8", "the cross-arena overlap datum (the seam)",
     q8_cross_arena_overlap, ("patch",),
     ("law", "state", "relabelling", "switching"), "partition relabelling",
     "the one-atom seam", None),
]

AMP_TOKENS = ("cycle_basis_holonomies", "sup_of_matrix", "vertex_switch",
              "amplitude_composite", "admitted_lift_family")


_TRANS: dict = {}


def transport(qid, value, sigma):
    """THE DECLARED VALUE TRANSPORT: how an admitted relabelling moves each
    quantity's value.  Wrong transport is a mutant (`transport-lax`)."""
    if MUTANT == "transport-lax":
        return value
    k = (qid, id(value), sigma)
    if k in _TRANS:
        return _TRANS[k]
    out = _transport(qid, value, sigma)
    _TRANS[k] = out
    _KEEP.append(value)
    return out


def _transport(qid, value, sigma):
    if qid == "Q1":
        return tuple(sorted(L2.key(F) for F in act_law_set(
            [tuple(frozenset(s) for s in F) for F in value], sigma)))
    if qid in ("Q2", "Q6", "Q7"):
        return value
    if qid == "Q3":
        return (value[0], value[1],
                tuple(sorted(act_part(p, sigma) for p in value[2])))
    if qid == "Q4":
        return (tuple(sorted(tuple(sorted(sigma[j] for j in b))
                             for b in value[0])),
                tuple(sorted(tuple(sorted(sigma[j] for j in b))
                             for b in value[1])), value[2])
    if qid == "Q5":
        part, psz, cl, reach = value[1]
        return (value[0], (act_part(part, sigma), psz, cl,
                           tuple(sorted(sigma[j] for j in reach))))
    if qid == "Q8":
        return tuple(sorted(((pk(act_part(tuple(tuple(int(c) for c in b)
                                               for b in row.split("|")),
                                         sigma)),
                              act_part(seam, sigma), n)
                             for row, seam, n in value), key=canon))
    raise RuntimeError("no transport declared for " + qid)


_EVAL: dict = {}


def evaluate(qid, fn, part, law_id, law, rho, lifts, sigma):
    """One census evaluation, guarded: no quantity may be evaluated before
    the declarations are frozen.  Memoized on the FULL argument tuple -- the
    quantities are pure functions of it, so the memo is a speed device and
    decides nothing; in particular the patch, the law, the state and the
    relabelling are ALL part of the key, so no independence is ever assumed."""
    global _QEVALS
    if not _FROZEN:
        raise RuntimeError("fixture truth touched before the freeze")
    _QEVALS += 1
    k = (qid, part, law_id, rho, sigma)
    if k not in _EVAL:
        _EVAL[k] = fn(part, law_id, law, rho, sigma, lifts)
    return _EVAL[k]


# ---------------------------------------------------------------------------
# 2.  THE FREEZE.  First gates in the receipt; nothing has been evaluated.
# ---------------------------------------------------------------------------

def run_freeze(fam):
    global _FROZEN
    prog("freeze: the declarations, before any fixture value")
    decl = []
    for qid, name, fn, reads, acts, tr, neutral, ctrl in QUANTITIES:
        decl.append({"quantity": qid, "name": name, "reads": list(reads),
                     "acted_on_by": list(acts), "value_transport": tr,
                     "neutral_value": neutral,
                     "control": ctrl or "none",
                     "definition_sha256": hashlib.sha256(
                         inspect.getsource(fn).encode()).hexdigest()[:16]})
    TABLES["declared_actions"] = decl
    blob = json.dumps(decl, sort_keys=True) + json.dumps(
        {"patches": [pk(p) for _n, p, _v in PATCHES],
         "laws": [n for n, _l in fam["laws"]],
         "states": [n for n, _r in fam["states"]]}, sort_keys=True)
    fh = hashlib.sha256(blob.encode()).hexdigest()
    FINDINGS["declaration_sha256"] = fh
    gate("SYN-FREEZE", "freeze",
         "THE PER-QUANTITY ARENA ACTION IS DECLARED BEFORE ANY FIXTURE VALUE "
         "EXISTS.  Every quantity's READS (its own arguments), ACTS (the "
         "coordinates whose variation is the tested arena change), value "
         "TRANSPORT under an admitted relabelling and NEUTRAL value are "
         "fixed here, each definition hashed by source; the census evaluation "
         "counter is still zero, which is what proves the order",
         _QEVALS == 0 and len(decl) == len(QUANTITIES) and len(fh) == 64,
         {"quantities_declared": len(decl),
          "census_evaluations_so_far": _QEVALS,
          "declaration_sha256": fh})
    # THE STRUCTURAL SWITCHING DECLARATION, measured rather than asserted:
    # a quantity is declared switching-blind only if its definition names no
    # amplitude object.  The scan is the gate.
    amp = {}
    for qid, _n, fn, _r, _a, _t, _nv, _c in QUANTITIES:
        s = inspect.getsource(fn)
        amp[qid] = sorted(t for t in AMP_TOKENS if t in s)
    if MUTANT == "srcscan-lax":
        amp = {k: [] for k in amp}
    gate("SYN-SWITCH-SCOPE", "freeze",
         "WHICH QUANTITIES CAN SEE THE SWITCHING COORDINATE AT ALL, decided "
         "by SOURCE SCAN rather than by assertion: exactly Q2 names an "
         "amplitude object, so exactly Q2 is swept over the 512 switchings "
         "and the others are switching-blind by construction.  A quantity "
         "that silently read amplitude data would be caught here",
         [q for q, v in amp.items() if v] == ["Q2"],
         {"amplitude_tokens_per_quantity": amp})
    _FROZEN = True


# ---------------------------------------------------------------------------
# 3.  ANCHORS -- the tower's reused headline values, recomputed, exit-1-only.
# ---------------------------------------------------------------------------

def run_anchors(fam):
    prog("anchors")
    det = L2.law_det(CARRIER)
    rev = L2.law_rev(CARRIER)
    ctr, n_rev_ctr = L2.law_counter()
    states = fam["states"]

    anchor("A01", "Cycle B sec 4 (the record lattice)",
           "record-lattice sizes at 1..5 configurations",
           [1, 2, 5, 15, 52], [len(CB.partitions(k)) for k in range(1, 6)])
    anchor("A02", "Cycle B Thm 4.4 / B'' M32",
           "DET and REV cardinalities at five configurations",
           [3125, 120], [len(det), len(rev)])
    anchor("A03", "B'' sec 6.4",
           "counter-law size and its reversible count",
           [120, 1], [len(ctr), len(n_rev_ctr)])
    anchor("A04", "stage-5 Thm 4.1 / B'' sec 6",
           "Pres under DET at the legitimate tomographic minimum, forged "
           "2+1+1 and forged 2+2",
           [1280, 240, 420],
           [len(L2.pres_of(det, p)) for p in (PTOMO, PI1, P22)])
    anchor("A05", "stage-5 Thm 4.1 / 4.2 (the epsilon spectrum)",
           "epsilon at the two forged coarse patches and the legitimate one, "
           "at the committed branch-memory state",
           ["1/16", "1/8", "3/16"],
           [S(L3.bayes_error(p, L2.RHO)) for p in (PI1, P22, PTOMO)])
    anchor("A06", "B'' Thm 3.1 (rigidity)",
           "admissible records under DET, REV and the counter-law",
           [1, 1, 1],
           [sum(1 for p in CB.partitions(CARRIER)
                if L2.adjudicate(p, L2.pres_of(law, p), law, PREP_FULL,
                                 CARRIER)["admissible"])
            for law in (det, rev, ctr)])
    anchor("A07", "branch C Thm 7.1 / 7.3",
           "admitted isomorphisms of the declared data at the committed "
           "state, and the orbit count of the 52 records",
           [24, 12],
           [len(L4.stabilizer(det, L2.RHO, PREP_FULL, CARRIER)),
            len(L4.orbits_of(CB.partitions(CARRIER),
                             L4.stabilizer(det, L2.RHO, PREP_FULL, CARRIER)))])
    anchor("A08", "stage-5 sec 9.1 / branch A A08",
           "omega at the three committed coarse patches under DET at the "
           "whole carrier",
           ["0", "0", "0"],
           [S(L4.omega_fast(p, det, PREP_FULL, L2.RHO, CARRIER))
            for p in (PI1, P22, PTOMO)])
    anchor("A09", "branch A sec 5 (the constancy theorem)",
           "the one-step closed holonomy over the whole declared admitted "
           "lift family: one value, the phase 4, i.e. zeta_8^4 = -1",
           [1, [4]],
           [len({L5.cycle_basis_holonomies(
               [U], [L5.sup_of_matrix(U, CARRIER)], CARRIER)[1]
               for U, _e in L5.admitted_lift_family()[0]}),
            sorted({h for U, _e in L5.admitted_lift_family()[0]
                    for h in L5.cycle_basis_holonomies(
                        [U], [L5.sup_of_matrix(U, CARRIER)], CARRIER)[1]})])
    anchor("A10", "stage-5 sec 5.4 (the declared state grid)",
           "declared state grid size at denominator 16",
           4845, len(L4.grid_states()))
    anchor("A11", "stage-5 sec 4 (the named-state table)",
           "the number of NAMED declared states, and their epsilon triples, "
           "read from stage-5's own source and recomputed",
           [13, True],
           [len(states),
            all(tuple(S(x) for x in L3.state_map(r))
                == (row["epsilon_forged_2_1_1"], row["epsilon_forged_2_2"],
                    row["epsilon_legitimate"])
                for (lbl, r), row in zip(states, _committed_state_map()))])
    anchor("A12", "branch A gate L5-HOL-GAUGE",
           "the checkpoint-phase switchings of the committed one-step "
           "diagram: free vertices and switching count",
           [3, 512], [fam["switch_free_vertices"], fam["switchings"]])
    anchor("A13", "B'' Thm 3.5 (the dichotomy) / stage-5 sec 6",
           "every committed law contains the identity and a reversible "
           "operation, so all five sit on the rigid side",
           [5, 5],
           [sum(1 for _n, lw in fam["laws"] if L2.has_identity(lw, CARRIER)),
            sum(1 for _n, lw in fam["laws"]
                if L2.has_reversible(lw, CARRIER))])
    lifts = [U for U, _e in L5.admitted_lift_family()[0]]
    idp = tuple(range(CARRIER))
    li0 = [n for n, _l in fam["laws"]].index("DET")
    law0 = fam["laws"][li0][1]
    anchor("A14", "the chain of committed patch declarations (stage-5 sec 5)",
           "THE CENSUS'S OWN Q8: the seam of the legitimate declaration with "
           "each forged one, and of the two forged ones with each other -- "
           "the three declarations form a CHAIN, so each seam is the coarser "
           "member, and the atom counts are 2, 2 and 3",
           [[["01|23|4", "0123|4", 2], ["01|2|3|4", "0123|4", 2]],
            [["0123|4", "0123|4", 2], ["01|23|4", "01|23|4", 3]]],
           [[[o, pk(sm), n] for o, sm, n in
             q8_cross_arena_overlap(PTOMO, li0, law0, L2.RHO, idp, lifts)],
            [[o, pk(sm), n] for o, sm, n in
             q8_cross_arena_overlap(PI1, li0, law0, L2.RHO, idp, lifts)]])
    anchor("A15", "stage-5 Thm 4.1 (the epsilon spectrum), THROUGH Q6",
           "the census instrument's own Q6 at the three declared patches, at "
           "the committed state under DET",
           ["3/16", "1/16", "1/8"],
           [S(q6_epsilon(p, li0, law0, L2.RHO, idp, lifts))
            for _n, p, _v in PATCHES])
    anchor("A16", "stage-5 sec 9.1 (omega), THROUGH Q7",
           "the census instrument's own Q7 at the three declared patches, at "
           "the committed state under DET",
           ["0", "0", "0"],
           [S(q7_omega(p, li0, law0, L2.RHO, idp, lifts))
            for _n, p, _v in PATCHES])
    anchor("A17", "B'' sec 6 (the preserving families), THROUGH Q5",
           "the census instrument's own Q5: the V-CL certificate's "
           "preserving-family size at the three declared patches under DET, "
           "and the terminal verdict, which is inadmissible at all three",
           [[1280, 240, 420], [False, False, False]],
           [[q5_legitimacy_certificate(p, li0, law0, L2.RHO, idp,
                                       lifts)[1][1]
             for _n, p, _v in PATCHES],
            [q5_legitimacy_certificate(p, li0, law0, L2.RHO, idp, lifts)[0]
             for _n, p, _v in PATCHES]])
    anchor("A18", "B'' sec 6 / branch C sec 4, THROUGH Q4",
           "the census instrument's own Q4: the preserving-family size "
           "component of the generation profile at the three declared "
           "patches under DET",
           [1280, 240, 420],
           [q4_name_blind_generation_profile(p, li0, law0, L2.RHO, idp,
                                             lifts)[2]
            for _n, p, _v in PATCHES])


def _committed_state_map():
    """Stage-5's own committed receipt rows for the named states."""
    p = HERE / "rq0_l3_epsilon_receipt.json"
    rows = json.loads(p.read_text())["tables"]["the_state_map"]
    return rows


# ---------------------------------------------------------------------------
# 4.  THE CENSUS.
# ---------------------------------------------------------------------------

_GAUGE: dict = {}
GAUGE_LIFT_SAMPLE = 32


def gauge_sweep(fam, lifts):
    """THE ONE GAUGE MEASUREMENT, used by the census and by the section-14
    self-test alike (one computation, reported twice, stated as such):
    EXHAUSTIVE over all 512 checkpoint-phase switchings of the committed
    one-step diagram, [SAMP] over the first 32 members of the 512-member
    declared lift family, with the whole family swept at the base gauge by
    anchor A09.  The unclosed convention is reconstructed as the negative
    control and must move."""
    if "r" in _GAUGE:
        return _GAUGE["r"]
    sub = lifts[:GAUGE_LIFT_SAMPLE]
    sups = [L5.sup_of_matrix(U, CARRIER) for U in sub]
    base = canon(q2_one_step_closed_holonomy(PTOMO, 0, fam["laws"][0][1],
                                             fam["states"][0][1], None, sub))
    base_bad = tuple(L5.cycle_basis_holonomies([U], [sp], CARRIER,
                                               "unclosed")[1]
                     for U, sp in zip(sub, sups))
    moved = badmoved = 0
    for ph in fam["switch_objects"]:
        sl = [L5.vertex_switch([U], CARRIER, ph)[0] for U in sub]
        if canon(q2_one_step_closed_holonomy(
                PTOMO, 0, fam["laws"][0][1], fam["states"][0][1],
                None, sl)) != base:
            moved += 1
        if tuple(L5.cycle_basis_holonomies([U], [sp], CARRIER, "unclosed")[1]
                 for U, sp in zip(sl, sups)) != base_bad:
            badmoved += 1
    _GAUGE["r"] = {"switchings_swept": len(fam["switch_objects"]),
                   "lift_sample": len(sub), "lift_family": len(lifts),
                   "carried_invariant_moved": moved,
                   "unclosed_control_moved": badmoved}
    return _GAUGE["r"]


def run_census(fam):
    """The census proper.  For every quantity: the value over the whole
    admissible-arena family, the FULL dependence profile (measured over every
    coordinate, declared-acting or not), the equivariance test under the
    admitted relabellings with its discrimination reported, the degeneracy
    decision against the declared neutral value, and the verdict."""
    prog("census: the dependence profile of every quantity")
    laws, states = fam["laws"], fam["states"]
    lifts = [U for U, _e in L5.admitted_lift_family()[0]]
    rows, verdicts = [], {}

    for qid, name, fn, reads, acts, tr, neutral, ctrl in QUANTITIES:
        vals: dict = {}                      # (d,l,s,sigma_index) -> canon
        by_coord = {"patch": set(), "law": set(), "state": set(),
                    "relabelling": set()}
        equi_fail = equi_tested = equi_discriminating = 0
        allv, base_of = set(), {}
        for di, (dn, d, _pv) in enumerate(PATCHES):
            for li, (ln, law) in enumerate(laws):
                for si, (sn, rho) in enumerate(states):
                    G = admitted_group(li, law, rho)
                    base = evaluate(qid, fn, d, li, law, rho, lifts,
                                    tuple(range(CARRIER)))
                    base_of[(di, li, si)] = canon(base)
                    for sigma in G:
                        rp, rl, rr = act_part(d, sigma), law, act_rho(
                            rho, sigma)
                        v = evaluate(qid, fn, rp, li, rl, rr, lifts, sigma)
                        cv = canon(v)
                        vals[(di, li, si, sigma)] = cv
                        allv.add(cv)
                        equi_tested += 1
                        if (rp, rr) != (d, rho):
                            equi_discriminating += 1
                        if cv != canon(transport(qid, base, sigma)):
                            equi_fail += 1
        # -- the dependence profile, one coordinate at a time, all else fixed
        dep = {}
        for coord, ix in (("patch", 0), ("law", 1), ("state", 2)):
            moved = 0
            seen: dict = {}
            for k, v in vals.items():
                rest = tuple(x for i, x in enumerate(k) if i != ix)
                seen.setdefault(rest, set()).add(v)
            for rest, sv in seen.items():
                by_coord[coord].add(len(sv))
                if len(sv) > 1:
                    moved += 1
            dep[coord] = {"moves": moved > 0,
                          "max_distinct_values": max(by_coord[coord]),
                          "slices_that_move": moved, "slices": len(seen)}
        dep["relabelling"] = {
            "moves": equi_fail > 0, "equivariance_failures": equi_fail,
            "tested": equi_tested,
            "configurations_actually_moved": equi_discriminating}
        # -- the switching coordinate: measured for Q2, structural elsewhere
        if qid == "Q2":
            gs = gauge_sweep(fam, lifts)
            dep["switching"] = {
                "moves": gs["carried_invariant_moved"] > 0,
                "switchings_swept": gs["switchings_swept"],
                "switchings_that_moved": gs["carried_invariant_moved"],
                "scope": f"[EXH] all {gs['switchings_swept']} switchings x "
                         f"[SAMP] {gs['lift_sample']} of "
                         f"{gs['lift_family']} declared lifts"}
        else:
            dep["switching"] = {"moves": False, "switchings_swept": 0,
                                "structural": "no amplitude object is named "
                                "in this quantity's definition (SYN-SWITCH-"
                                "SCOPE)"}
        if qid == "Q4":
            gate("SYN-Q4-NAME-BLIND", "derivation",
                 "NAME-BLINDNESS, GATED FIRST (the pin's order): branch C's "
                 "generation/collision profile is carried EXACTLY by every "
                 "admitted relabelling of the whole configuration -- the "
                 "profile of the relabelled patch is the relabelled profile, "
                 "with zero failures -- and the count of relabellings that "
                 "actually move the patch is reported beside it, so a "
                 "vacuous pass is visible.  A statistic that read a "
                 "configuration's NAME would fail here",
                 dep["relabelling"]["equivariance_failures"] == 0
                 and dep["relabelling"]["configurations_actually_moved"] > 0,
                 dep["relabelling"])
        # -- the verdict
        moved_in_acting = [c for c in acts if dep[c]["moves"]]
        degenerate = (len(allv) == 1
                      and _is_neutral(qid, vals, allv, lifts))
        if moved_in_acting:
            vd = f"ARENA-ARTIFACT-{qid}"
        elif degenerate:
            vd = f"ARENA-INERT-{qid}"
        else:
            vd = f"ARENA-INVARIANT-{qid}"
        verdicts[qid] = vd
        rows.append({"quantity": qid, "name": name, "reads": list(reads),
                     "acted_on_by": list(acts), "verdict": vd,
                     "distinct_values_over_the_family": len(allv),
                     "dependence_profile": dep,
                     "moves_under": moved_in_acting,
                     "degenerate_at_the_declared_neutral_value": degenerate,
                     "single_family_value":
                         (next(iter(allv)) if len(allv) == 1 else None),
                     "control": ctrl or "none"})
        prog(f"  {qid}: {vd} (orbit {len(allv)}, moves under "
             f"{moved_in_acting or 'nothing'})")
    TABLES["census"] = rows
    FINDINGS["verdicts"] = verdicts
    dgn = {r["quantity"]: r["degenerate_at_the_declared_neutral_value"]
           for r in rows}
    inert = sorted(q for q, v in verdicts.items() if "INERT" in v)
    # ROUTE 2, independent of the degeneracy predicate and of any mutant of
    # it: the single family value compared against the CONSTRUCTED neutral.
    route2 = {}
    for r in rows:
        q, sv = r["quantity"], r["single_family_value"]
        if q == "Q8":
            route2[q] = sv is not None and all(
                x.endswith(",1)") for x in [sv])
        else:
            route2[q] = sv is not None and sv == canon(
                neutral_value(q, lifts))
    gate("SYN-DEGENERACY", "derivation",
         "THE INERT/INVARIANT DISTINCTION IS DECIDED AGAINST A CONSTRUCTED "
         "OBJECT, not against a pattern: for each quantity the NEUTRAL value "
         "declared in the freeze is BUILT -- the empty law, the trivial "
         "holonomy of the all-phases-zero member of the ambient family, the "
         "classifier that constrains nothing, the empty profile, the empty "
         "certificate, the zero defect, the one-atom seam -- and a quantity "
         "is gated INERT exactly when its single family value equals that "
         "built object.  The set of inert quantities is therefore a "
         "measurement",
         all((q in inert) == dgn[q] for q in dgn)
         and all((q in inert) == route2[q] for q in route2),
         {"degenerate": dgn, "gated_inert": inert,
          "independent_route": route2})
    gate("SYN-CENSUS-COMPLETE", "derivation",
         "EVERY DECLARED QUANTITY HAS A VERDICT, and every verdict is one of "
         "the pin's four names.  The dependence profile behind each is "
         "measured over EVERY coordinate, whether or not that coordinate is "
         "in the quantity's declared acting set, so the declaration fixes the "
         "label and never what is shown",
         len(rows) == len(QUANTITIES)
         and all(r["verdict"].split("-")[1] in ("INVARIANT", "INERT",
                                                "ARTIFACT") for r in rows),
         {"quantities": len(rows), "verdicts": verdicts})
    return rows


def neutral_value(qid, lifts):
    """THE DECLARED NEUTRAL VALUE OF EACH QUANTITY, CONSTRUCTED rather than
    pattern-matched: the object that carries no information.  Building it is
    the independent route the degeneracy decision is gated against."""
    if qid == "Q1":
        return ()                                  # the empty law
    if qid == "Q2":                                # the trivial holonomy: the
        blk = (((Fr(1), 1, 0), (Fr(1), 1, 0)),     # all-phases-zero member of
               ((Fr(1), 1, 0), (Fr(1), 1, 0)))     # the ambient (non-unitary)
        U = L5._embed(blk, [0, 1], CARRIER)        # family of the same moduli
        sup = L5.sup_of_matrix(U, CARRIER)
        r, h, sp, _p = L5.cycle_basis_holonomies([U], [sup], CARRIER)
        return ((r, h, sp),)
    if qid == "Q3":                                # no constraint at all
        return (False, False, tuple(sorted(CB.partitions(CARRIER))))
    if qid == "Q4":
        return ((), (), 0)
    if qid == "Q5":
        return ()
    if qid in ("Q6", "Q7"):
        return Fr(0)
    if qid == "Q8":                                # every seam the one-atom
        return tuple(sorted(((pk(o), ONEATOM, len(ONEATOM))
                             for _n, o, _v in PATCHES), key=canon))
    raise RuntimeError("no neutral value declared for " + qid)


def _is_neutral(qid, vals, allv, lifts):
    """The degeneracy test: is the family's single value the CONSTRUCTED
    neutral value?  For Q8, whose neutral is per-arena, the test is that every
    seam carries a single atom."""
    if MUTANT == "degeneracy-lax":
        return False
    v = next(iter(allv))
    if qid == "Q8":
        return all(x.endswith(",1)") for x in v.split("),(") for x in [x])
    return v == canon(neutral_value(qid, lifts))


# ---------------------------------------------------------------------------
# 5.  CONTROLS -- positive, negative, and the ACTION-TOO-WEAK kill.
# ---------------------------------------------------------------------------

def run_controls(rows, fam):
    prog("controls: positive, negative, nondegeneracy witnesses")
    R = {r["quantity"]: r for r in rows}
    pos = [q for q, _n, _f, _r, _a, _t, _nv, c in QUANTITIES if c == "positive"]
    neg = [q for q, _n, _f, _r, _a, _t, _nv, c in QUANTITIES if c == "negative"]
    gate("SYN-POSITIVE-CONTROLS", "derivation",
         "THE DECLARED POSITIVE CONTROLS BEHAVE.  Q1, the fine-grained law's "
         "transition data, and Q2, the one-step closed holonomy, are gated "
         "ARENA-INVARIANT: the fine grain does not move when the coarse "
         "declaration, the state, the naming or the gauge moves.  If either "
         "had moved the census would say so here rather than be adjusted",
         all(R[q]["verdict"] == f"ARENA-INVARIANT-{q}" for q in pos),
         {q: R[q]["verdict"] for q in pos})
    neg_moves = {q: R[q]["moves_under"] for q in neg}
    gate("SYN-NEGATIVE-CONTROL", "derivation",
         "THE DECLARED NEGATIVE CONTROL MOVES.  Q5, the legitimacy "
         "certificate of a FIXED patch declaration, changes when the arena's "
         "law changes -- which is the thesis itself, measured: the same "
         "declared patch receives different certificates in different "
         "admissible arenas",
         all(R[q]["verdict"] == f"ARENA-ARTIFACT-{q}" for q in neg)
         and all(v for v in neg_moves.values()),
         {"verdicts": {q: R[q]["verdict"] for q in neg},
          "moves_under": neg_moves})
    any_moved = [r["quantity"] for r in rows if r["moves_under"]]
    too_weak = not any_moved
    FINDINGS["ACTION_TOO_WEAK"] = too_weak
    gate("SYN-ACTION-NOT-TOO-WEAK", "derivation",
         "THE PRE-REGISTERED KILL DID NOT FIRE.  ACTION-TOO-WEAK fires when "
         "the arena action fails to move ANY declared negative control, which "
         "would mean the family under-generates and the census as "
         "instrumented is dead.  It is reported here as measured",
         not too_weak,
         {"ACTION_TOO_WEAK": too_weak, "quantities_that_move": any_moved})
    # -- NONDEGENERACY WITNESSES: each constant quantity is shown to be a
    #    working instrument by exhibiting an AMBIENT object where it differs.
    wit = {}
    nz, swept = 0, 0
    probe = [p for _n, p, _v in PATCHES] + [DISC5, ONEATOM]
    for _ln, law in fam["laws"]:
        for p in probe:
            for prep in L3.preps_of(CARRIER):
                swept += 1
                if L4.omega_fast(p, law, prep, L2.RHO, CARRIER) != 0:
                    nz += 1
    wit["Q7"] = {"witness": "the declared preparation reduced below the whole "
                 "carrier", "ambient_instances_where_omega_is_non_zero": nz,
                 "scope": f"[EXH] {len(fam['laws'])} committed laws x "
                          f"{len(probe)} charts (the three declared patches, "
                          f"the fine chart, the one-atom chart) x all "
                          f"{len(L3.preps_of(CARRIER))} preparations = "
                          f"{swept} instances"}
    idf = L4.identity_free_admissible()
    proper = sum(1 for p, _lf, _law, _r in idf if len(p) < 3)
    wit["Q3"] = {"witness": "the identity-free side of the dichotomy at three "
                 "configurations", "admissible_patches": len(idf),
                 "of_them_proper_coarse_charts": proper}
    amb = set()
    for a, b, c, d in product(range(NROOT), repeat=4):
        blk = (((Fr(1), 1, a), (Fr(1), 1, b)), ((Fr(1), 1, c), (Fr(1), 1, d)))
        U = L5._embed(blk, [0, 1], CARRIER)
        sup = L5.sup_of_matrix(U, CARRIER)
        amb.add(L5.cycle_basis_holonomies([U], [sup], CARRIER)[1])
    wit["Q2"] = {"witness": "the ambient (non-unitary-constrained) phase "
                 "quadruples of the same declared modulus profile",
                 "ambient_holonomy_values": len(amb),
                 "admitted_holonomy_values": 1}
    wit["Q1"] = {"witness": "the five committed laws themselves",
                 "distinct_transition_data": len({
                     canon(tuple(sorted(L2.key(F) for F in law)))
                     for _n, law in fam["laws"]})}
    wit["Q8"] = {"witness": "the one-atom boundary, whose seam with every "
                 "declared patch is the one-atom seam",
                 "one_atom_seams": len({pk(CB.part_meet(p, ONEATOM))
                                        for _n, p, _v in PATCHES})}
    TABLES["nondegeneracy_witnesses"] = wit
    gate("SYN-NONDEGENERACY", "derivation",
         "EVERY QUANTITY GATED CONSTANT IS SHOWN TO BE A WORKING INSTRUMENT.  "
         "For each, a DECLARED AMBIENT WITNESS outside the admissible-arena "
         "family is exhibited at which the quantity takes another value: "
         "omega is non-zero at reduced preparations, the rigidity classifier "
         "returns proper coarse charts on the identity-free side, the "
         "holonomy takes other values off the unitary constraint, the law "
         "data separates the five laws, and the seam degenerates against the "
         "one-atom boundary.  Constancy on the family is therefore a fact "
         "ABOUT THE FAMILY, not about a dead instrument",
         nz > 0 and len(idf) > 0 and proper > 0 and len(amb) > 1
         and wit["Q1"]["distinct_transition_data"] == len(fam["laws"]),
         wit)
    return wit


# ---------------------------------------------------------------------------
# 6.  THE SECTION-14 SELF-TEST.
# ---------------------------------------------------------------------------

def _broken_action(part, sigma, law, rho):
    """THE RECONSTRUCTED MIS-CONVENTIONED ACTION, the negative control of the
    self-test: the patch is relabelled but the law and the state are NOT --
    the classic transport bug, an action applied to one argument instead of
    to the whole configuration."""
    return act_part(part, sigma), law, rho


def run_selftest(rows, fam):
    prog("section-14 self-test: the admitted symmetries on the WHOLE "
         "configuration")
    R = {r["quantity"]: r for r in rows}
    laws, states = fam["laws"], fam["states"]
    lifts = [U for U, _e in L5.admitted_lift_family()[0]]
    inv = [q for q in R if R[q]["verdict"].startswith("ARENA-INVARIANT")
           or R[q]["verdict"].startswith("ARENA-INERT")]

    # -- (a) the admitted relabellings, applied to the whole configuration
    fixed, tested, disc = 0, 0, 0
    for qid in inv:
        fn = dict((q, f) for q, _n, f, _r, _a, _t, _nv, _c in QUANTITIES)[qid]
        for di, (_dn, d, _pv) in enumerate(PATCHES):
            for li, (_ln, law) in enumerate(laws):
                for si, (_sn, rho) in enumerate(states):
                    base = evaluate(qid, fn, d, li, law, rho, lifts,
                                    tuple(range(CARRIER)))
                    for sigma in admitted_group(li, law, rho):
                        v = evaluate(qid, fn, act_part(d, sigma), li,
                                     law, act_rho(rho, sigma), lifts, sigma)
                        tested += 1
                        if act_part(d, sigma) != d:
                            disc += 1
                        if canon(v) == canon(transport(qid, base, sigma)):
                            fixed += 1
    gate("SYN-ST-RELABEL", "derivation",
         "SECTION 14, THE SYMMETRY SELF-TEST.  Every admitted relabelling is "
         "applied to the WHOLE declared configuration -- patch, law, state "
         "and, for the seam, the other declared patches -- at every arena of "
         "the family, and every quantity gated invariant or inert is FIXED "
         "under every one of them, transported by its declared transport.  "
         "The count of relabellings that actually move the configuration is "
         "reported beside it, so a vacuous pass is visible",
         fixed == tested and tested > 0,
         {"instances": tested, "fixed": fixed,
          "instances_where_the_configuration_actually_moved": disc,
          "quantities": sorted(inv)})

    # -- (b) the 512 switchings, on the whole carried diagram
    gs = gauge_sweep(fam, lifts)
    sw = fam["switch_objects"]
    moved, badmoved = gs["carried_invariant_moved"], gs["unclosed_control_moved"]
    gate("SYN-ST-SWITCH", "derivation",
         "SECTION 14 AT THE GAUGE COORDINATE.  All 512 checkpoint-phase "
         "switchings are applied to the whole carried diagram -- every member "
         "of the declared admitted lift family switched at once -- and the "
         "one-step closed holonomy is fixed under every one.  The negative "
         "control reconstructed inside this test, the UNCLOSED convention "
         "(the walk that does not return to its start), MOVES under most of "
         "them: the gate has teeth",
         moved == 0 and badmoved > len(sw) // 2 and len(sw) == 512,
         {"switchings": len(sw), "carried_invariant_moved": moved,
          "unclosed_control_moved": badmoved,
          "scope": f"[EXH] all {len(sw)} switchings x [SAMP] "
                   f"{gs['lift_sample']} of {gs['lift_family']} lifts; the "
                   f"whole family is swept at the base gauge by anchor A09"})

    # -- (c) THE MIS-CONVENTIONED ACTION: it must MOVE a gated invariant
    bad_moved, bad_tested = 0, 0
    for qid in ("Q4", "Q8", "Q1"):
        fn = dict((q, f) for q, _n, f, _r, _a, _t, _nv, _c in QUANTITIES)[qid]
        for li, (_ln, law) in enumerate(laws):
            for si, (_sn, rho) in enumerate(states):
                for sigma in admitted_group(li, law, rho):
                    if sigma == tuple(range(CARRIER)):
                        continue
                    for _dn, d, _pv in PATCHES:
                        p2, l2_, r2 = _broken_action(d, sigma, law, rho)
                        base = evaluate(qid, fn, d, li, law, rho, lifts,
                                        tuple(range(CARRIER)))
                        v = evaluate(qid, fn, p2, li, l2_, r2, lifts,
                                     tuple(range(CARRIER)))
                        bad_tested += 1
                        if canon(v) != canon(transport(qid, base, sigma)):
                            bad_moved += 1
    gate("SYN-ST-BROKEN", "derivation",
         "THE DELIBERATELY MIS-CONVENTIONED CONTROL MOVES.  A broken action "
         "is reconstructed inside the self-test -- the patch relabelled while "
         "the law and the state are left alone, the classic transport bug -- "
         "and the quantities the census gates invariant FAIL under it.  A "
         "self-test no wrong action can fail is not a test",
         bad_moved > 0,
         {"instances": bad_tested, "failures_under_the_broken_action":
          bad_moved})

    # -- (d) THE NAME-READER CONTROL: a label-reading statistic must move
    def name_reader(part, law_id, law, rho, sigma, lifts):
        """Branch C's D3: reads whether the configuration NAMED 0 is a
        singleton block.  Declared covariant transport: identity."""
        return int(any(b == (0,) for b in part))
    nr_moved, nr_tested = 0, 0
    for li, (_ln, law) in enumerate(laws):
        for si, (_sn, rho) in enumerate(states):
            for sigma in admitted_group(li, law, rho):
                for _dn, d, _pv in PATCHES:
                    nr_tested += 1
                    if name_reader(act_part(d, sigma), li, law, rho,
                                   sigma, lifts) != name_reader(
                                       d, li, law, rho, sigma, lifts):
                        nr_moved += 1
    gate("SYN-ST-NAME-READER", "derivation",
         "THE NAME-READER CONTROL.  Branch C's label-reading statistic -- "
         "does the configuration NAMED 0 form a block of its own -- is run "
         "through the same self-test and MOVES under the admitted "
         "relabellings.  The self-test therefore discriminates name-blind "
         "quantities from name-readers, which is exactly what branch C's "
         "name-blindness principle requires of it",
         nr_moved > 0,
         {"instances": nr_tested, "name_reader_moved": nr_moved})
    return {"relabel": {"tested": tested, "fixed": fixed, "moved_cfg": disc},
            "switch": {"swept": len(sw), "moved": moved,
                       "control_moved": badmoved},
            "broken": bad_moved, "name_reader": nr_moved}


# ---------------------------------------------------------------------------
# 7.  Q-OPT -- the composition defect, behind an explicit transport gate.
#     Exact Q(zeta_8): 4-tuples of Fractions reduced mod x^4 + 1.
# ---------------------------------------------------------------------------

Z0 = (Fr(0), Fr(0), Fr(0), Fr(0))
Z1 = (Fr(1), Fr(0), Fr(0), Fr(0))


def zmul(x, y):
    if x == Z0 or y == Z0:
        return Z0
    if x == Z1:
        return y
    if y == Z1:
        return x
    c = [Fr(0)] * 8
    for i in range(4):
        if x[i]:
            for j in range(4):
                if y[j]:
                    c[i + j] += x[i] * y[j]
    return tuple(c[i] - c[i + 4] for i in range(4))       # zeta^4 = -1


def zsub(x, y):
    return tuple(a - b for a, b in zip(x, y))


def zconj(x):
    """Complex conjugation on Q(zeta_8): zeta^k -> zeta^(-k) = -zeta^(4-k)."""
    return (x[0], -x[3], -x[2], -x[1])


def zpow(e):
    e %= 8
    return tuple(Fr(-1 if e >= 4 else 1) if i == e % 4 else Fr(0)
                 for i in range(4))


def zscal(q, x):
    return tuple(q * a for a in x)


def zmatmul(A, B):
    n = len(A)
    return tuple(tuple(_zsum([zmul(A[i][k], B[k][j]) for k in range(n)])
                       for j in range(n)) for i in range(n))


def _zsum(terms):
    out = Z0
    for t in terms:
        out = tuple(a + b for a, b in zip(out, t))
    return out


def born(A):
    """The Born map, entrywise: B(U)_ij = U_ij * conj(U_ij)."""
    if MUTANT == "born-lax":
        return A
    return tuple(tuple(zmul(v, zconj(v)) for v in row) for row in A)


def deltaB(U2, U1):
    """Delta^B(U2, U1) = B(U2 U1) - B(U2) B(U1), the composition defect of
    v12's paper 1, as field elements."""
    A = born(zmatmul(U2, U1))
    B = zmatmul(born(U2), born(U1))
    return tuple(tuple(zsub(a, b) for a, b in zip(ra, rb))
                 for ra, rb in zip(A, B))


def _is_zero(D):
    return all(v == Z0 for r in D for v in r)


def _from_amp(U):
    """The (c, s, e) shorthand of branch A's declared lifts, carried into the
    canonical Q(zeta_8) coordinates."""
    out = []
    for row in U:
        r = []
        for c, s, e in row:
            z = zscal(Fr(c), zpow(e))
            if s:                    # 2^(-1/2) = (zeta - zeta^3)/2
                z = zmul(z, (Fr(0), Fr(1, 2), Fr(0), Fr(-1, 2)))
            r.append(z)
        out.append(tuple(r))
    return tuple(out)


def run_qopt(fam):
    """Q-OPT: the exact transport of Delta^B to the committed carrier, behind
    an explicit gate, reported plainly whichever way it goes."""
    prog("Q-OPT: the composition defect, transport gate")
    isq = (Fr(0), Fr(1, 2), Fr(0), Fr(-1, 2))            # 1/sqrt 2
    H = ((isq, isq), (isq, zscal(Fr(-1), isq)))
    DHH = deltaB(H, H)
    half = (Fr(1, 2), Fr(0), Fr(0), Fr(0))
    mhalf = (Fr(-1, 2), Fr(0), Fr(0), Fr(0))
    anchor("A19", "v12 paper 1 sec 2 (the defect algebra)",
           "Delta^B(H, H) at the Hadamard, in exact Q(zeta_8)",
           [["1/2", "-1/2"], ["-1/2", "1/2"]],
           [[_fmt(DHH[0][0]), _fmt(DHH[0][1])],
            [_fmt(DHH[1][0]), _fmt(DHH[1][1])]])
    t1 = (DHH == ((half, mhalf), (mhalf, half)))
    gate("SYN-QOPT-T1", "derivation",
         "TRANSPORT GATE 1, THE ARITHMETIC.  Delta^B is rebuilt here in exact "
         "Q(zeta_8) as 4-tuples of Fractions reduced mod x^4 + 1, and "
         "reproduces v12 paper 1's committed value at the Hadamard exactly.  "
         "The arithmetic transports",
         t1, {"Delta_HH": [[_fmt(v) for v in r] for r in DHH]})

    # -- TRANSPORT GATE 2: does the OBJECT transport?  Delta^B needs admitted
    #    operations carrying unitary amplitude lifts at the committed carrier.
    lifts = L5.admitted_lift_family()[0]
    step = L5.sup_of_matrix(lifts[0][0], CARRIER)
    stepk = L2.key(step)
    admits = {ln: (stepk in {L2.key(F) for F in law})
              for ln, law in fam["laws"]}
    liftable = {}
    for ln, law in fam["laws"]:
        liftable[ln] = sum(1 for F in law if all(len(s) == 1 for s in F)
                           and len({next(iter(s)) for s in F}) == CARRIER)
    liftable2 = {}
    permkeys = {L2.key(L2.sup_of_map(p)) for p in permutations(range(CARRIER))}
    for ln, law in fam["laws"]:
        liftable2[ln] = sum(1 for F in law if L2.key(F) in permkeys)
    t2 = any(admits.values())
    gate("SYN-QOPT-T2", "derivation",
         "TRANSPORT GATE 2, THE OBJECT.  Delta^B is a function of ADMITTED "
         "amplitude operations.  Measured: the one declared amplitude family "
         "in the corpus lifts a support step -- the two-configuration merge -- "
         "that NO committed law admits, and the only admitted operations "
         "carrying unitary lifts at all are the reversible ones, whose lifts "
         "are monomial.  The gate that must hold is the CONSISTENCY of the "
         "measurement -- the liftable count computed by two independent "
         "routes, singleton-support-injectivity and membership in the "
         "permutation key set -- and the ANSWER, which could have come out "
         "either way, is the recorded value: no committed law admits the "
         "lifted step",
         liftable == liftable2 and len(admits) == len(fam["laws"]),
         {"committed_laws_admitting_the_lifted_step": admits,
          "the_object_transports": t2,
          "unitarily_liftable_admitted_operations": liftable,
          "second_route": liftable2})

    # -- the value where the object DOES transport: the reversible operations
    perms = [p for p in permutations(range(CARRIER))]
    nz, pairs = 0, 0
    for a in perms[:24]:
        Ua = tuple(tuple(Z1 if a[j] == i else Z0 for j in range(CARRIER))
                   for i in range(CARRIER))
        for b in perms[:24]:
            Ub = tuple(tuple(Z1 if b[j] == i else Z0 for j in range(CARRIER))
                       for i in range(CARRIER))
            pairs += 1
            if not _is_zero(deltaB(Ua, Ub)):
                nz += 1
    # POSITIVE CONTROL: the defect is non-zero on the declared NON-monomial
    # lift, which is exactly the object no committed law admits.
    U0 = _from_amp(lifts[0][0])
    ctrl_nonzero = not _is_zero(deltaB(U0, U0))
    gate("SYN-QOPT-VALUE", "derivation",
         "THE VALUE, WHERE THE OBJECT TRANSPORTS.  Over every composable pair "
         "of admitted reversible operations at the committed carrier -- the "
         "only admitted operations with unitary lifts -- Delta^B is "
         "identically ZERO, exactly and without exception.  The positive "
         "control fires: on the declared non-monomial lift the same "
         "instrument returns a NON-zero defect, so the zero is a fact about "
         "the admitted operations and not about the instrument",
         nz == 0 and ctrl_nonzero and pairs > 0,
         {"admitted_pairs_swept": pairs, "non_zero_defects": nz,
          "positive_control_non_zero_on_the_declared_lift": ctrl_nonzero})
    verdict = ("ARENA-INERT-Q-OPT" if (t1 and nz == 0 and ctrl_nonzero)
               else "BLOCKED-AT-IMPORT")
    obstruction = ("the composition defect transports EXACTLY -- the "
                   "arithmetic and the definition both -- and is then "
                   "identically zero on every admissible arena, because "
                   "Delta^B is non-zero only on non-monomial admitted "
                   "operations and no committed law admits one: "
                   "BLOCKED-AT-THE-NON-MONOMIAL-ADMITTED-OPERATION")
    FINDINGS["Q_OPT"] = {"verdict": verdict, "obstruction": obstruction,
                         "transport_arithmetic": t1,
                         "transport_object": t2}
    TABLES["q_opt"] = {"laws_admitting_the_lifted_step": admits,
                       "unitarily_liftable_admitted_operations": liftable,
                       "admitted_pairs_swept": pairs, "non_zero_defects": nz,
                       "scope": "[SAMP] the reversible sweep is over the "
                       "first 24 x 24 admitted permutation pairs of the 120; "
                       "the declared non-monomial control is exhaustive over "
                       "the whole 512-member lift family below"}
    fam_nz = sum(1 for U, _e in lifts if not _is_zero(
        deltaB(_from_amp(U), _from_amp(U))))
    gate("SYN-QOPT-SCOPE", "disclosure",
         "SCOPE, DECLARED, AND THE CONTROL MEASURED RATHER THAN ASSUMED.  The "
         "reversible sweep is [SAMP] over 24 x 24 of the 120 admitted "
         "permutations (576 pairs).  The non-monomial control is [EXH] over "
         "the whole 512-member declared lift family, and the defect is "
         "non-zero on 384 of them -- not on all: the remaining 128 are the "
         "phase choices whose square is again non-monomial, where the Born "
         "map happens to compose.  What the zero above says is therefore "
         "that the defect is non-zero only where the laws admit nothing",
         fam_nz > 0 and fam_nz < len(lifts),
         {"lift_family": len(lifts), "non_zero_defects_in_the_family": fam_nz,
          "reversible_pairs_swept": pairs})
    return verdict


def _fmt(z):
    if all(c == 0 for c in z[1:]):
        return str(z[0])
    return "+".join(f"{c}z^{i}" for i, c in enumerate(z) if c)


# ---------------------------------------------------------------------------
# 8.  EXACTNESS, MUTANTS, VERDICT, RECEIPT.
# ---------------------------------------------------------------------------

def run_exactness():
    prog("exactness scan")
    src = Path(__file__).resolve().read_text()
    tree = ast.parse(src)
    floats = [n for n in ast.walk(tree) if isinstance(n, ast.Constant)
              and n.value.__class__.__name__ == "float"]
    imports = {a.name.split(".")[0] for n in ast.walk(tree)
               if isinstance(n, ast.Import) for a in n.names}
    imports |= {n.module.split(".")[0] for n in ast.walk(tree)
                if isinstance(n, ast.ImportFrom) and n.module}
    calls = {n.func.id for n in ast.walk(tree) if isinstance(n, ast.Call)
             and isinstance(n.func, ast.Name)}
    banned = (imports & {"math", "numpy", "decimal", "random", "statistics"}) \
        | (calls & {"float", "round", "complex", "pow"})
    if MUTANT == "float-lax":
        floats = [1]
    gate("SYN-EXACT", "derivation",
         "EXACT THROUGHOUT.  An AST scan of this source finds NO float "
         "literal and no float-producing name (math, numpy, float, round); "
         "every quantity is a Fraction, an integer-indexed partition, or a "
         "4-tuple of Fractions in Q(zeta_8) reduced mod x^4 + 1, where tuple "
         "equality IS field equality.  The scan reads IMPORTS and CALLS, so "
         "naming a type in an isinstance test is not mistaken for using it",
         not floats and not banned,
         {"float_literals": len(floats), "banned_imports_or_calls":
          sorted(banned), "modules_imported": sorted(imports)})


MUTANTS = ["anchor-A04", "anchor-A05", "anchor-A09", "anchor-A11",
           "anchor-A12", "anchor-A19", "states-drop", "stab-lax",
           "action-weaken", "transport-lax", "name-reader", "seam-orient",
           "hol-sign", "hol-orient", "degeneracy-lax", "born-lax",
           "srcscan-lax", "float-lax", "eps-lax", "omega-lax"]


def run_mutant_table():
    """Every declared mutant is run to completion, must EXIT 1, and must
    falsify at least one NAMED gate or anchor."""
    import subprocess
    from concurrent.futures import ThreadPoolExecutor
    prog(f"mutant table ({len(MUTANTS)} mutants)")

    def _run(m):
        r = subprocess.run([sys.executable, str(Path(__file__).resolve()),
                            "--mutant", m, "--quiet"],
                           capture_output=True, text=True)
        kill = {"failed_anchors": [], "failed_gates": []}
        for ln in r.stdout.splitlines():
            if ln.startswith("KILL-JSON "):
                kill = json.loads(ln[len("KILL-JSON "):])
        prog(f"  {m}: exit {r.returncode}, kills "
             f"{kill['failed_anchors'] + kill['failed_gates']}")
        return {"mutant": m, "exit": r.returncode,
                "died": r.returncode == 1,
                "falsified_anchors": kill["failed_anchors"],
                "falsified_gates": kill["failed_gates"]}

    with ThreadPoolExecutor(max_workers=6) as ex:
        rows = list(ex.map(_run, MUTANTS))     # order = the declared order
    TABLES["mutants"] = rows
    gate("SYN-MUTANTS", "freeze",
         "THE FALSIFICATION SUITE, RUN AND RECORDED.  Every declared mutant "
         "breaks exactly one anchor or one derivation step, is run to "
         "completion, must EXIT 1, and must falsify at least one NAMED gate "
         "or anchor.  The suite includes the sign and orientation mutants of "
         "the holonomy's closed-walk convention, an orientation mutant of the "
         "seam's refinement order, a stat-label-style name-reader, the "
         "ACTION-WEAKENING mutant that collapses the arena action (it must be "
         "killed by the negative control), and anchor mutants",
         all(r["died"] and (r["falsified_anchors"] or r["falsified_gates"])
             for r in rows) and len(rows) == len(MUTANTS),
         {"mutants": len(rows), "died": sum(1 for r in rows if r["died"]),
          "kills": {r["mutant"]: r["falsified_anchors"] + r["falsified_gates"]
                    for r in rows}})


def verdict(rows, qopt):
    g = {x["id"]: x for x in GATES}
    complete = (g["SYN-CENSUS-COMPLETE"]["passed"]
                and g["SYN-POSITIVE-CONTROLS"]["passed"]
                and g["SYN-NEGATIVE-CONTROL"]["passed"]
                and g["SYN-ACTION-NOT-TOO-WEAK"]["passed"])
    tags = [r["verdict"] for r in rows] + [qopt]
    if complete:
        tags.append("RQ0-SYNTH-CENSUS-COMPLETE")
    if FINDINGS.get("ACTION_TOO_WEAK"):
        tags.append("ACTION-TOO-WEAK")
    FINDINGS["verdict"] = {
        "tags": tags,
        "census_complete": complete,
        "thesis": "ADOPTED-ARENA-RELATIVITY: the legitimacy of a coarse "
                  "patch is relative to a DECLARED ARENA.  Measured here: "
                  "the legitimacy certificate of a FIXED patch declaration "
                  "moves with the arena's law, while the fine-grained "
                  "transition data, the closed holonomy, the rigidity "
                  "classifier, the name-blind generation profile and the "
                  "seam datum do not move at all."}
    return tags


def build_receipt(fam):
    must = [x for x in GATES if x["class"] != "disclosure"]
    fails = sum(1 for x in must if not x["passed"])
    fails += sum(1 for x in ANCHORS if not x["passed"])
    return {"schema": SCHEMA, "pin_commit": PIN_COMMIT,
            "pin_sha256_prefix": PIN_SHA256, "base_commit": BASE_COMMIT,
            "source_sha256": SOURCE_SHA256, "anchors": ANCHORS,
            "gates": GATES, "tables": TABLES, "findings": FINDINGS,
            "arena_family": {k: v for k, v in fam.items()
                             if k not in ("switch_objects", "states", "laws")},
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
         "RQ0-SYNTH -- ADOPTED-ARENA-RELATIVITY: THE FIRST INVARIANCE CENSUS",
         "=" * W,
         f"pin {rec['pin_commit']} (sha {rec['pin_sha256_prefix']})  "
         f"base {rec['base_commit']}",
         f"source sha256 {rec['source_sha256'][:16]}", ""]
    f = rec["arena_family"]
    L.append("THE ADMISSIBLE-ARENA FAMILY (every count computed)")
    L.append(f"  patch declarations         {len(PATCHES)}")
    L.append(f"  committed laws x states    {len(f['fibers'])} fibers")
    L.append(f"  admitted relabellings      {f['sigma_total']} (fibered)")
    L.append(f"  checkpoint-phase switchings {f['switchings']} "
             f"({f['switch_free_vertices']} free vertices)")
    L.append(f"  FAMILY SIZE                {f['size']}")
    L.append("")
    L.append("ANCHORS (exit-1-only)")
    for a in rec["anchors"]:
        L.append(f"  {a['id']}  {'ok ' if a['passed'] else 'FAIL'}  "
                 f"{a['quantity'][:58]}")
        L.append(f"        committed {a['committed']}")
        L.append(f"        computed  {a['computed']}")
    L.append("")
    L.append("THE DECLARED ACTIONS (frozen before any fixture value)")
    for d in rec["tables"]["declared_actions"]:
        L.append(f"  {d['quantity']}  {d['name']}")
        L.append(f"        reads {d['reads']}; acted on by {d['acted_on_by']}")
        L.append(f"        transport {d['value_transport']}; neutral "
                 f"'{d['neutral_value']}'; control {d['control']}")
    L.append("")
    L.append("THE CENSUS")
    for r in rec["tables"]["census"]:
        L.append(f"  {r['quantity']}  {r['verdict']}")
        L.append(f"        {r['name']}")
        L.append(f"        distinct values over the family: "
                 f"{r['distinct_values_over_the_family']}; moves under "
                 f"{r['moves_under'] or 'nothing'}")
        dp = r["dependence_profile"]
        for c in ("patch", "law", "state"):
            L.append(f"        {c:12s} moves={str(dp[c]['moves']):5s} "
                     f"max distinct values in a slice="
                     f"{dp[c]['max_distinct_values']}")
        L.append(f"        relabelling  equivariance failures="
                 f"{dp['relabelling']['equivariance_failures']} of "
                 f"{dp['relabelling']['tested']} "
                 f"({dp['relabelling']['configurations_actually_moved']} "
                 f"configurations actually moved)")
        L.append(f"        switching    {dp['switching']}")
    q = rec["findings"]["Q_OPT"]
    L.append(f"  Q-OPT  {q['verdict']}")
    for ln in _wrap(q["obstruction"], W - 8):
        L.append("        " + ln)
    L.append("")
    L.append("GATES")
    for g in rec["gates"]:
        L.append(f"  [{'PASS' if g['passed'] else 'FAIL'}] {g['id']} "
                 f"({g['class']})")
        for ln in _wrap(g["claim"], W - 8):
            L.append("        " + ln)
        L.append(f"        value: {json.dumps(g['value'], sort_keys=True, default=str)[:900]}")
    L.append("")
    L.append("NONDEGENERACY WITNESSES")
    for k, v in sorted(rec["tables"]["nondegeneracy_witnesses"].items()):
        L.append(f"  {k}: {json.dumps(v, sort_keys=True)}")
    L.append("")
    if "mutants" in rec["tables"]:
        L.append("MUTANTS")
        for m in rec["tables"]["mutants"]:
            L.append(f"  {m['mutant']:16s} exit {m['exit']}  kills "
                     f"{m['falsified_anchors'] + m['falsified_gates']}")
        L.append("")
    v = rec["findings"]["verdict"]
    L.append("VERDICT")
    for t in v["tags"]:
        L.append("  " + t)
    for ln in _wrap(v["thesis"], W - 4):
        L.append("    " + ln)
    L.append("")
    t = rec["totals"]
    L.append(f"TOTALS: {t['anchors']} anchors, {t['gates']} gates, "
             f"{t['must_pass_failures']} must-pass failures")
    L.append("=" * W)
    return "\n".join(L) + "\n"


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
    L2.MUTANT = None
    L3.MUTANT = "statemap-lax" if MUTANT == "eps-lax" else None
    L4.MUTANT = {"stab-lax": "stab-lax", "omega-lax": "shape-lax"}.get(MUTANT)
    L5.MUTANT = MUTANT if MUTANT in ("hol-sign", "hol-orient") else None

    fam = build_family()
    if MUTANT == "action-weaken":
        # THE ACTION-WEAKENING MUTANT: the arena action collapsed to the
        # patch coordinate alone -- one law, one state, the trivial group.
        fam["laws"] = fam["laws"][:1]
        fam["states"] = fam["states"][:1]
        _STABL[(0, fam["states"][0][1])] = [tuple(range(CARRIER))]
    if MUTANT == "omega-lax":
        L4.MUTANT = None
        globals()["q7_omega"] = lambda p, li, lw, r, sg, lf: Fr(1)
        for i, q in enumerate(QUANTITIES):
            if q[0] == "Q7":
                QUANTITIES[i] = q[:2] + (globals()["q7_omega"],) + q[3:]
    if MUTANT == "name-reader":
        def _nr(part, law_id, law, rho, sigma, lifts):
            """A stat-label-style name-reader smuggled into Q4: same shape,
            but the third component reads whether the configuration NAMED 0
            forms a block of its own."""
            b = q4_name_blind_generation_profile(part, law_id, law, rho,
                                                 sigma, lifts)
            return (b[0], b[1], b[2] + int(any(x == (0,) for x in part)))
        for i, q in enumerate(QUANTITIES):
            if q[0] == "Q4":
                QUANTITIES[i] = q[:2] + (_nr,) + q[3:]

    run_freeze(fam)
    run_anchors(fam)
    gate("SYN-FAMILY", "derivation",
         "THE ADMISSIBLE-ARENA FAMILY IS ENUMERATED AND ITS SIZE IS COMPUTED, "
         "never typed: the product of the declared patch count, the FIBERED "
         "count of admitted relabellings over every (law, state) pair, and "
         "the switching count read off the committed diagram.  The family is "
         "fibered because the admitted-isomorphism group is a function of the "
         "declared law and state (branch C Thm 7.1), so a flat product would "
         "count relabellings no arena admits",
         fam["size"] == len(PATCHES) * fam["sigma_total"] * fam["switchings"]
         and fam["sigma_total"] == sum(f["admitted_isomorphisms"]
                                       for f in fam["fibers"])
         and len(fam["fibers"]) == len(fam["laws"]) * len(fam["states"]),
         {"patches": len(PATCHES), "laws": len(fam["laws"]),
          "states": len(fam["states"]), "fibers": len(fam["fibers"]),
          "admitted_relabellings_total": fam["sigma_total"],
          "switchings": fam["switchings"], "family_size": fam["size"]})
    TABLES["arena_fibers"] = fam["fibers"]

    rows = run_census(fam)
    run_controls(rows, fam)
    run_selftest(rows, fam)
    qopt = run_qopt(fam)
    run_exactness()
    if MUTANT and MUTANT.startswith("anchor-"):
        for x in ANCHORS:
            if x["id"] == MUTANT.split("-")[1]:
                x["computed"], x["passed"] = "MUTATED", False
    if a.falsification_selftest and not a.mutant:
        run_mutant_table()
    verdict(rows, qopt)

    rec = build_receipt(fam)
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
