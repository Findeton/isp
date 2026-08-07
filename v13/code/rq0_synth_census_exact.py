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
_ADJ: dict = {}

# -- FRESH EVALUATION (RUNBOOK section 14 addendum, v13 #185).  A self-test
#    that reaches its quantity through the instrument's own memo tests the
#    CACHE, not the quantity.  Three value-level memos here key on a PROPER
#    SUBSET of the coordinates the census varies -- `_MEMO` (the per-quantity
#    memo), `_EVAL` (the census evaluation memo) and `_TRANS` (the transport
#    memo) -- and are therefore the exact mechanism by which an equivariance
#    test degenerates to `x == x` on one object.  In FRESH mode all three are
#    bypassed entirely and the phase's hit count is GATED at zero.
#    `_ADJ`, the adjudication sub-expression cache, is keyed on the FULL pair
#    (record, law) that determines its value -- it drops no varied coordinate
#    -- and is CLEARED at the start of the fresh phase rather than bypassed,
#    with its miss count gated positive; this is Deviation 10.
_FRESH = False
_CACHE = {"value_cache_hits": 0, "value_cache_misses": 0,
          "adjudication_cache_hits": 0, "adjudication_cache_misses": 0}


def _memo(key, build):
    """The per-quantity value memo.  Bypassed in fresh mode; the `memo-lax`
    mutant restores the reviewed defect (the self-test reading the cache) and
    must die at SYN-ST-FRESH."""
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


def _adj(part, law_id, law):
    k = (part, law_id)
    if k in _ADJ:
        if _FRESH:
            _CACHE["adjudication_cache_hits"] += 1
        return _ADJ[k]
    if _FRESH:
        _CACHE["adjudication_cache_misses"] += 1
    _ADJ[k] = L2.adjudicate(part, L2.pres_of(law, part), law,
                            PREP_FULL, CARRIER)
    return _ADJ[k]


def q1_fine_grained_transition_data(part, law_id, law, rho, sigma, lifts):
    """Q1 -- THE FINE-GRAINED LAW'S TRANSITION DATA: the admitted operations
    of the declared law as sector supports at the fine chart."""
    return _memo(("q1", law_id),
                 lambda: tuple(sorted(L2.key(F) for F in law)))


def q2_one_step_closed_holonomy(part, law_id, law, rho, sigma, lifts):
    """Q2 -- THE ONE-STEP CLOSED HOLONOMY of the carried amplitude diagram:
    branch A's gauge-invariant content, (cycle rank, holonomy phases, spans),
    over the declared admitted lift family under the arena's switching."""
    def build():
        out = set()
        for U in lifts:
            sup = L5.sup_of_matrix(U, CARRIER)
            r, h, s, _p = L5.cycle_basis_holonomies([U], [sup], CARRIER)
            out.add((r, h, s))
        _KEEP.append(lifts)
        return tuple(sorted(out))
    return _memo(("q2", id(lifts)), build)


def q3_rigidity_classifier(part, law_id, law, rho, sigma, lifts):
    """Q3 -- THE RIGIDITY CLASSIFIER, cycle B''s identity-free flag: whether
    the law contains the identity, whether it contains a reversible
    operation, and the set of boundaries the terminal axiom admits."""
    def build():
        adm = tuple(sorted(p for p in CB.partitions(CARRIER)
                           if _adj(p, law_id, law)["admissible"]))
        return (L2.has_identity(law, CARRIER),
                L2.has_reversible(law, CARRIER), adm)
    return _memo(("q3", law_id), build)


def _shadow_amp(lifts):
    """The `hidden-read` mutant's helper: amplitude data consumed through a
    CALLEE, so that a ONE-LEVEL source scan would report the calling quantity
    switching-blind while its value demonstrably depends on the gauge.  The
    repaired scan follows module-local calls and must catch it."""
    U = lifts[0]
    return L5.cycle_basis_holonomies([U], [L5.sup_of_matrix(U, CARRIER)],
                                     CARRIER)[1]


def q4_name_blind_generation_profile(part, law_id, law, rho, sigma,
                                    lifts):
    """Q4 -- THE NAME-BLIND GENERATION/COLLISION PROFILE, branch C's corridor
    machinery: the collision classes the law's preserving family generates on
    the patch, the law's own reachability classes, and the preserving family's
    size.  Returned as STRUCTURED objects carrying their labels, so that
    name-blindness is a measurement and not a presentation choice."""
    def build():
        fam = L2.pres_of(law, part)
        return (tuple(sorted(tuple(sorted(b)) for b in L4.my_ker(
            fam, CARRIER))),
            L4.reach_classes(law, part, CARRIER), len(fam))
    return _memo(("q4", part, law_id), build)


def q5_legitimacy_certificate(part, law_id, law, rho, sigma, lifts):
    """Q5 -- THE LEGITIMACY CERTIFICATE FUNCTIONS: branch A's V-CL certificate
    of the declared patch (the record written, the preserving-family size, the
    four clause bits, the reachable subprocess) together with the terminal
    axiom's verdict.  DECLARED NEGATIVE CONTROL: expected to move."""
    def build():
        v = _adj(part, law_id, law)
        cert = L5.certificate_CL(L2.block_min_idempotent(part, CARRIER),
                                 law, PREP_FULL, CARRIER)
        return (bool(v["admissible"]), cert)
    return _memo(("q5", part, law_id), build)


def q6_epsilon(part, law_id, law, rho, sigma, lifts):
    """Q6 -- EPSILON, stage 5's concordance defect, in its closed form: the
    residual Bayes error of the declared boundary at the declared state."""
    return L3.bayes_error(part, rho)


def q7_omega(part, law_id, law, rho, sigma, lifts):
    """Q7 -- OMEGA, the occupancy defect: the declared mass carried by blocks
    the realized process never occupies."""
    return L4.omega_fast(part, law, PREP_FULL, rho, CARRIER)


def q8_cross_arena_overlap(part, law_id, law, rho, sigma, lifts,
                           others=PATCHES):
    """Q8 -- THE CROSS-ARENA OVERLAP DATUM: what the arena's patch and each
    other declared patch SHARE on intersection -- the finest common
    coarsening, which is exactly the intersection of the two boundary
    algebras -- and how many atoms that seam carries.  `others` is the set of
    declared patches the arena carries; it is the committed three except in
    the AMBIENT nondegeneracy witness, which runs this same function over a
    NON-CHAIN triple outside the family."""
    out = []
    for _nm, other, _pv in others:
        o = other if MUTANT == "seam-blind" else act_part(other, sigma)
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

# THE ARENA COORDINATES, and the parameter through which each reaches a
# quantity.  The signature scan below decides, by reading the source, which
# coordinates a quantity's definition consumes AT ALL -- so that a fixity in
# a coordinate the definition never names is reported as DEFINITIONAL and
# never as a measurement (R2's repair; the model is SYN-SWITCH-SCOPE's).
ARENA_COORDS = (("patch", ("part",)), ("law", ("law", "law_id")),
                ("state", ("rho",)), ("relabelling", ("sigma",)),
                ("switching", ("lifts",)))

# THE SELF-TEST'S TESTED SET, FIXED BY DECLARATION and never by the verdicts
# under audit (RUNBOOK section 14 addendum).  It is gated equal to the full
# declared quantity list.
SELFTEST_QUANTITIES = ("Q1", "Q2", "Q3", "Q4", "Q5", "Q6", "Q7", "Q8")

_SRC_CACHE: dict = {}


def _module_defs():
    """Every TOP-LEVEL function of this module, by name, for the transitive
    source scan.  Nested definitions are not indexed: they belong to the
    source of the function that encloses them."""
    if "defs" not in _SRC_CACHE:
        tree = ast.parse(Path(__file__).resolve().read_text())
        _SRC_CACHE["defs"] = {n.name: n for n in tree.body
                              if isinstance(n, ast.FunctionDef)}
    return _SRC_CACHE["defs"]


def _called_names(node):
    return [nd.func.id for nd in ast.walk(node)
            if isinstance(nd, ast.Call) and isinstance(nd.func, ast.Name)]


def _scan_quantity(fn, deep=True):
    """THE TWO SOURCE SCANS of one quantity, over the TRANSITIVE CLOSURE of
    its module-local callees: which AMPLITUDE objects its definition names,
    and which ARENA COORDINATES it consumes at all.  R3's finding is that a
    ONE-LEVEL scan reports a quantity switching-blind while a helper one call
    down consumes amplitude data; `deep=False` reproduces that blind spot and
    is what the `hidden-read` mutant exploits.  The coordinate scan is an
    OVER-approximation -- a coordinate name occurring anywhere in the closure
    counts -- so it can only ever weaken a blindness claim, never manufacture
    one."""
    import textwrap
    defs = _module_defs()
    src0 = textwrap.dedent(inspect.getsource(fn))
    srcs, seen = [src0], set()
    stack = _called_names(ast.parse(src0))
    while deep and stack:
        nm = stack.pop()
        if nm in seen or nm not in defs:
            continue
        seen.add(nm)
        srcs.append(ast.unparse(defs[nm]))
        stack += _called_names(defs[nm])
    src = "\n".join(srcs)
    ids = {n.id for n in ast.walk(ast.parse(src)) if isinstance(n, ast.Name)}
    return (sorted(t for t in AMP_TOKENS if t in src),
            sorted(c for c, ps in ARENA_COORDS if ids & set(ps)),
            sorted(seen))


_TRANS: dict = {}


def transport(qid, value, sigma):
    """THE DECLARED VALUE TRANSPORT: how an admitted relabelling moves each
    quantity's value.  Wrong transport is a mutant (`transport-lax`)."""
    if MUTANT == "transport-lax":
        return value
    if _FRESH and MUTANT != "memo-lax":
        _CACHE["value_cache_misses"] += 1
        return _transport(qid, value, sigma)
    k = (qid, id(value), sigma)
    if k in _TRANS:
        if _FRESH:
            _CACHE["value_cache_hits"] += 1
        return _TRANS[k]
    if _FRESH:
        _CACHE["value_cache_misses"] += 1
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
    if _FRESH and MUTANT != "memo-lax":
        _CACHE["value_cache_misses"] += 1
        return fn(part, law_id, law, rho, sigma, lifts)
    k = (qid, part, law_id, rho, sigma)
    if k in _EVAL:
        if _FRESH:
            _CACHE["value_cache_hits"] += 1
        return _EVAL[k]
    if _FRESH:
        _CACHE["value_cache_misses"] += 1
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
    # THE SOURCE SCANS, measured rather than asserted, over the TRANSITIVE
    # closure of each quantity's module-local callees.
    amp, coords, closure, amp1 = {}, {}, {}, {}
    for qid, _n, fn, _r, _a, _t, _nv, _c in QUANTITIES:
        amp[qid], coords[qid], closure[qid] = _scan_quantity(fn, True)
        amp1[qid] = _scan_quantity(fn, False)[0]
    TABLES["signature_scan"] = {
        "arena_coordinates_the_definition_consumes": coords,
        "amplitude_objects_named": amp,
        "amplitude_objects_named_by_a_one_level_scan": amp1,
        "module_local_callees_followed": closure}
    FINDINGS["signature_scan"] = coords
    gate("SYN-SWITCH-SCOPE", "freeze",
         "WHICH QUANTITIES CAN SEE THE SWITCHING COORDINATE AT ALL, decided "
         "by SOURCE SCAN rather than by assertion, and over the TRANSITIVE "
         "CLOSURE of each quantity's module-local callees rather than one "
         "level deep: exactly Q2 names an amplitude object, so exactly Q2 is "
         "swept over the 512 switchings and the others are switching-blind "
         "by construction.  A quantity that read amplitude data THROUGH A "
         "HELPER would be caught here -- that is what the `hidden-read` "
         "mutant does, and it dies at this gate",
         [q for q, v in amp.items() if v] == ["Q2"],
         {"amplitude_tokens_per_quantity": amp,
          "the_same_scan_one_level_deep": amp1,
          "callees_followed_per_quantity":
              {q: len(c) for q, c in closure.items()}})
    gate("SYN-SELFTEST-SET", "disclosure",
         "THE SELF-TEST'S TESTED SET IS FIXED BY DECLARATION, never by the "
         "verdicts under audit (RUNBOOK section 14 addendum).  It is the "
         "full declared quantity list, frozen here with the declarations "
         "themselves and gated equal to it; the delivered instrument's "
         "defect was that the set was recomputed from the census's own "
         "verdicts, so a quantity a broken transport made move was DELETED "
         "from the test instead of failing it.  DISCLOSURE CLASS: this gate "
         "records the declaration; the ENFORCEMENT -- that the set actually "
         "tested is this one -- is a conjunct of SYN-ST-RELABEL, which the "
         "`selftest-scope` mutant falsifies by reinstating the reviewed "
         "self-scoping",
         SELFTEST_QUANTITIES == tuple(q[0] for q in QUANTITIES)
         and len(SELFTEST_QUANTITIES) == len(QUANTITIES),
         {"declared_tested_set": list(SELFTEST_QUANTITIES),
          "declared_quantities": [q[0] for q in QUANTITIES]})
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
    anchor("A20", "B'' sec 6 (the preserving families at the legitimate "
           "declaration), THROUGH Q5",
           "the census instrument's own Q5: the preserving-family size of "
           "the legitimate tomographic minimum under EACH of the five "
           "committed laws, and the four clause bits of its certificate "
           "under each -- the fourth bit, (ii-b), the OCCUPANCY clause, is "
           "the one that fails under REV and under no other committed law",
           [[1280, 13, 120, 1161, 60],
            [[False, True, False, True], [False, True, False, True],
             [False, True, False, False], [False, True, False, True],
             [False, True, False, True]]],
           [[q5_legitimacy_certificate(PTOMO, li, lw, L2.RHO, idp,
                                       lifts)[1][1]
             for li, (_ln, lw) in enumerate(fam["laws"])],
            [[bool(b) for b in q5_legitimacy_certificate(
                PTOMO, li, lw, L2.RHO, idp, lifts)[1][2]]
             for li, (_ln, lw) in enumerate(fam["laws"])]])
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
    one-step diagram AND over all 512 members of the declared admitted lift
    family -- the full 262,144-instance cross product, which the reviewed
    instrument sampled at 32 lifts and claimed at 512.  The unclosed
    convention is reconstructed as the negative control and must move."""
    if "r" in _GAUGE:
        return _GAUGE["r"]
    sub = lifts[:GAUGE_LIFT_SAMPLE] if MUTANT == "gauge-subsample" else lifts
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
                   "lifts_swept": len(sub), "lift_family": len(lifts),
                   "instances": len(fam["switch_objects"]) * len(sub),
                   "carried_invariant_moved": moved,
                   "unclosed_control_moved": badmoved}
    return _GAUGE["r"]


def census_domain(fam):
    """The arena domain the census actually sweeps.  `arena-collapse` reduces
    it to a single arena so that NOTHING can move and the pre-registered
    ACTION-TOO-WEAK kill fires."""
    if MUTANT == "arena-collapse":
        return list(PATCHES)[:1], fam["laws"], fam["states"]
    return list(PATCHES), fam["laws"], fam["states"]


ARENA_COORD_NAMES = tuple(c for c, _p in ARENA_COORDS)


def derive_verdict(qid, dep, n_values, degenerate, acts=None):
    """THE VERDICT, DERIVED FROM MEASUREMENT.  A quantity is an ARENA
    ARTIFACT when its value is MEASURED to move as an arena coordinate is
    varied; it is ARENA-INERT when it does not move and its single family
    value is the constructed neutral object; ARENA-INVARIANT when it does not
    move and is nondegenerate.  The READS/ACTS declaration is NOT consulted:
    it survives as bookkeeping annotation only, and the flip-test gate below
    proves that the derivation is independent of it.  `acts` is accepted so
    that the flip-test can pass a declaration in; only the `declaration-lax`
    mutant lets it reach the result."""
    coords = ARENA_COORD_NAMES
    if MUTANT == "declaration-lax" and acts is not None:
        coords = tuple(c for c in coords if c in acts)
    moved = [c for c in coords if dep[c]["moves"]]
    if MUTANT == "verdict-lax":
        return f"ARENA-UNDECIDED-{qid}", moved
    if moved:
        return f"ARENA-ARTIFACT-{qid}", moved
    if degenerate:
        return f"ARENA-INERT-{qid}", moved
    return f"ARENA-INVARIANT-{qid}", moved


def run_census(fam):
    """The census proper.  For every quantity: the value over the whole
    admissible-arena family, the FULL dependence profile (measured over every
    coordinate), the equivariance test under the admitted relabellings with
    its PER-QUANTITY discrimination reported, the degeneracy decision against
    the declared neutral value, and the verdict, derived from the measured
    profile alone."""
    prog("census: the dependence profile of every quantity")
    patches, laws, states = census_domain(fam)
    lifts = [U for U, _e in L5.admitted_lift_family()[0]]
    rows, verdicts, moved_by = [], {}, {}

    for qid, name, fn, reads, acts, tr, neutral, ctrl in QUANTITIES:
        vals: dict = {}                      # (d,l,s,sigma_index) -> canon
        by_coord = {"patch": set(), "law": set(), "state": set(),
                    "relabelling": set()}
        equi_fail = equi_tested = equi_discriminating = 0
        teeth = 0                            # instances where EITHER side of
        allv, base_of, one_obj = set(), {}, {}    # the test differs from base
        denamed = {}                         # per declaration, sigma = id
        for di, (dn, d, _pv) in enumerate(patches):
            for li, (ln, law) in enumerate(laws):
                for si, (sn, rho) in enumerate(states):
                    G = admitted_group(li, law, rho)
                    base = evaluate(qid, fn, d, li, law, rho, lifts,
                                    tuple(range(CARRIER)))
                    cb = canon(base)
                    base_of[(di, li, si)] = cb
                    denamed.setdefault(di, set()).add(cb)
                    for sigma in G:
                        rp, rl, rr = act_part(d, sigma), law, act_rho(
                            rho, sigma)
                        v = evaluate(qid, fn, rp, li, rl, rr, lifts, sigma)
                        cv = canon(v)
                        vals[(di, li, si, sigma)] = cv
                        allv.add(cv)
                        one_obj[cv] = v
                        equi_tested += 1
                        if (rp, rr) != (d, rho):
                            equi_discriminating += 1
                        ct = canon(transport(qid, base, sigma))
                        if cv != ct:
                            equi_fail += 1
                        if cv != cb or ct != cb:
                            teeth += 1
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
            "configurations_actually_moved": equi_discriminating,
            "instances_where_either_side_differs_from_the_base": teeth,
            "discrimination": ("measured" if teeth else
                               "structurally fixed: neither the recomputed "
                               "value nor the transported base ever differs "
                               "from the base, so this row carries no "
                               "information about the transport")}
        # -- the switching coordinate: measured for Q2, structural elsewhere
        if qid == "Q2":
            gs = gauge_sweep(fam, lifts)
            dep["switching"] = {
                "moves": gs["carried_invariant_moved"] > 0,
                "switchings_swept": gs["switchings_swept"],
                "switchings_that_moved": gs["carried_invariant_moved"],
                "scope": f"[EXH] all {gs['switchings_swept']} switchings x "
                         f"[EXH] all {gs['lifts_swept']} declared lifts = "
                         f"{gs['instances']} instances"}
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
        # -- the verdict, DERIVED FROM THE MEASURED PROFILE
        sole = next(iter(allv)) if len(allv) == 1 else None
        degenerate = (sole is not None
                      and _is_neutral(qid, one_obj[sole], lifts))
        vd, moved = derive_verdict(qid, dep, len(allv), degenerate, acts)
        verdicts[qid] = vd
        moved_by[qid] = moved
        # -- the naming quotient, applied to EVERY quantity alike: the count
        #    of distinct values at a FIXED declaration with the naming held
        #    (sigma = identity), and over the three declarations together.
        per_decl = sorted(len(s) for s in denamed.values())
        rows.append({"quantity": qid, "name": name, "reads": list(reads),
                     "acted_on_by": list(acts), "verdict": vd,
                     "distinct_values_over_the_family": len(allv),
                     "distinct_values_per_declaration_de_named": per_decl,
                     "distinct_values_over_all_declarations_de_named":
                         len(set().union(*denamed.values())),
                     "dependence_profile": dep,
                     "moves_under": moved,
                     "declared_acting_coordinates_that_move":
                         [c for c in acts if dep[c]["moves"]],
                     "coordinates_the_definition_consumes":
                         FINDINGS["signature_scan"][qid],
                     "degenerate_at_the_declared_neutral_value": degenerate,
                     "single_family_value": sole,
                     "control": ctrl or "none"})
        prog(f"  {qid}: {vd} (orbit {len(allv)}, moves under "
             f"{moved or 'nothing'})")
    TABLES["census"] = rows
    FINDINGS["verdicts"] = verdicts
    # -- WHAT THE FIBRATION DOES TO A REPORTED NUMBER, disclosed.  The fibered
    #    family constrains which (realized patch, state) pairs co-occur, so
    #    epsilon's range over the family is SMALLER than over a flat product
    #    of the realized patches with the thirteen states.
    realized = {act_part(d, sg) for _dn, d, _pv in patches
                for li, (_ln, law) in enumerate(laws)
                for _sn, rho in states
                for sg in admitted_group(li, law, rho)}
    flat_eps = {L3.bayes_error(p, rho) for p in realized
                for _sn, rho in states}
    patterns = {}
    for li, (ln, law) in enumerate(laws):
        patterns.setdefault(tuple(len(admitted_group(li, law, rho))
                                  for _sn, rho in states), []).append(ln)
    TABLES["fibration_disclosure"] = {
        "distinct_fiber_size_patterns_across_the_laws": len(patterns),
        "fiber_size_patterns": {str(k): v for k, v in patterns.items()},
        "realized_patches": len(realized),
        "epsilon_values_over_the_flat_product_of_realized_patches_x_states":
            len(flat_eps),
        "epsilon_values_over_the_fibered_family":
            [r["distinct_values_over_the_family"] for r in rows
             if r["quantity"] == "Q6"][0]}
    dgn = {r["quantity"]: r["degenerate_at_the_declared_neutral_value"]
           for r in rows}
    inert = sorted(q for q, v in verdicts.items() if "INERT" in v)

    # -- THE DECLARATION FLIP-TEST, now a PERMANENT GATE.  The verdicts are
    #    re-derived under a SECOND declaration -- every arena coordinate acts
    #    on every quantity, the reading a reader who rejects the split would
    #    take -- and the two derivations must agree exactly.
    alt = {}
    for r in rows:
        q = r["quantity"]
        alt[q] = derive_verdict(q, r["dependence_profile"],
                                r["distinct_values_over_the_family"],
                                dgn[q], ARENA_COORD_NAMES)[0]
    gate("SYN-DECLARATION-INDEPENDENT", "derivation",
         "THE VERDICTS DO NOT DEPEND ON THE READS/ACTS DECLARATION.  Every "
         "verdict is derived from the MEASURED dependence profile alone; the "
         "declaration survives as bookkeeping annotation.  The proof is run "
         "here rather than argued: the whole verdict table is re-derived "
         "under a second declaration -- every arena coordinate acting on "
         "every quantity, which is the reading a reader who rejects the "
         "split would take -- and the two tables must be IDENTICAL.  In the "
         "reviewed instrument this flip moved three of eight verdicts, "
         "including a declared positive control",
         all(alt[r["quantity"]] == r["verdict"] for r in rows),
         {"declared": {r["quantity"]: r["verdict"] for r in rows},
          "under_the_alternative_declaration": alt,
          "verdicts_that_differ": [q for q in alt
                                   if alt[q] != verdicts[q]]})

    # -- THE CONSISTENCY LAW BEHIND "DEFINITIONAL": no quantity may move in
    #    a coordinate its definition never names.
    viol = [(r["quantity"], c) for r in rows for c in ARENA_COORD_NAMES
            if r["dependence_profile"][c]["moves"]
            and c not in FINDINGS["signature_scan"][r["quantity"]]]
    gate("SYN-SIGNATURE-SCOPE", "derivation",
         "MEASURED FIXITY VERSUS DEFINITIONAL FIXITY.  The source scan "
         "records which arena coordinates each quantity's definition "
         "consumes at all; a quantity whose definition never names the law "
         "CANNOT move with the law, so reporting that fixity as an "
         "invariance would be reporting a signature as a result.  Q8, the "
         "seam, names neither the law nor the state.  The gate's own law is "
         "the consistency of scan and measurement: NO QUANTITY MOVES IN A "
         "COORDINATE ITS DEFINITION NEVER NAMES.  A wrong relabelling group "
         "or a wrong value transport breaks it, because the quantity then "
         "moves in a coordinate it never reads",
         not viol,
         {"arena_coordinates_consumed": FINDINGS["signature_scan"],
          "violations": [list(v) for v in viol]})

    # ROUTE 2, independent of the degeneracy predicate and of any mutant of
    # it: the single family value compared against the CONSTRUCTED neutral.
    route2 = {r["quantity"]: _route2_neutral(
        r["quantity"], r["single_family_value"], lifts) for r in rows}

    # -- THE WORKING NEGATIVE CONTROL OF THE INERT/INVARIANT BOUNDARY: each
    #    quantity's CONSTRUCTED neutral is fed through the whole decision
    #    path, and must come back ARENA-INERT.  The reviewed instrument's
    #    Q8 branch returned False on Q8's own neutral, so ARENA-INERT-Q8 was
    #    unreachable by construction.
    flat = {c: {"moves": False} for c in ARENA_COORD_NAMES}
    reach, both = {}, {}
    for qid, _n, _f, _r, _a, _t, _nv, _c in QUANTITIES:
        objs = _neutral_objects(qid, lifts)
        both[qid] = all(_is_neutral(qid, o, lifts)
                        and _route2_neutral(qid, canon(o), lifts)
                        for o in objs)
        reach[qid] = all(derive_verdict(qid, flat, 1, _is_neutral(
            qid, o, lifts))[0] == f"ARENA-INERT-{qid}" for o in objs)
    gate("SYN-NEUTRAL-RECOGNITION", "derivation",
         "EVERY QUANTITY'S ARENA-INERT VERDICT IS REACHABLE, demonstrated "
         "rather than assumed: each declared NEUTRAL value is CONSTRUCTED "
         "and fed through the whole decision path -- the degeneracy "
         "predicate and the verdict derivation -- and must come back "
         "ARENA-INERT.  This is the working negative control of the "
         "inert/invariant boundary.  The reviewed instrument decided Q8's "
         "degeneracy by a string suffix and returned False on Q8's own "
         "constructed neutral, so ARENA-INERT-Q8 was unreachable by "
         "construction at the one place the pin says it must not be",
         all(reach.values()) and all(both.values()),
         {"inert_is_reachable_for": reach,
          "both_routes_recognise_the_constructed_neutral": both})
    gate("SYN-DEGENERACY", "derivation",
         "THE INERT/INVARIANT DISTINCTION IS DECIDED AGAINST A CONSTRUCTED "
         "OBJECT, not against a pattern: for each quantity the NEUTRAL value "
         "declared in the freeze is BUILT -- the empty law, the trivial "
         "holonomy of the all-phases-zero member of the ambient family, the "
         "classifier that constrains nothing, the empty profile, the empty "
         "certificate, the zero defect, the one-atom seam of the arena's own "
         "patch with each other declared patch -- and a quantity is gated "
         "INERT exactly when its single family value IS that object, by two "
         "routes: structurally on the value object (for the seam: every seam "
         "it carries is the one-atom partition) and by canonical string "
         "against the construction.  The set of inert quantities is "
         "therefore a measurement",
         all((q in inert) == dgn[q] for q in dgn)
         and all((q in inert) == route2[q] for q in route2),
         {"degenerate": dgn, "gated_inert": inert,
          "independent_route": route2})
    gate("SYN-CENSUS-COMPLETE", "derivation",
         "EVERY DECLARED QUANTITY HAS A VERDICT, every verdict is one of the "
         "pin's four names, and every verdict is DERIVED FROM THE MEASURED "
         "dependence profile over every arena coordinate rather than from a "
         "declaration about which coordinates count as the arena change",
         len(rows) == len(QUANTITIES)
         and all(r["verdict"] in (f"ARENA-INVARIANT-{r['quantity']}",
                                  f"ARENA-INERT-{r['quantity']}",
                                  f"ARENA-ARTIFACT-{r['quantity']}")
                 for r in rows),
         {"quantities": len(rows), "verdicts": verdicts})
    return rows


def neutral_value(qid, lifts, part=None):
    """THE DECLARED NEUTRAL VALUE OF EACH QUANTITY, CONSTRUCTED rather than
    pattern-matched: the object that carries no information.  Building it is
    the independent route the degeneracy decision is gated against.  Q8's
    neutral is per declared patch, because Q8's value is the seam of THIS
    arena's patch with each OTHER declared patch: the neutral must be built
    with the same skip rule or it is not a value the quantity could take --
    which is why the reviewed instrument could not recognise it."""
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
        base = part if part is not None else PATCHES[0][1]
        return tuple(sorted(((pk(o), ONEATOM, len(ONEATOM))
                             for _n, o, _v in PATCHES if o != base),
                            key=canon))
    raise RuntimeError("no neutral value declared for " + qid)


def _neutral_objects(qid, lifts):
    """Every neutral object a quantity could take: one, except for Q8, whose
    neutral is relative to the arena's own declared patch."""
    if qid == "Q8":
        return [neutral_value(qid, lifts, p) for _n, p, _v in PATCHES]
    return [neutral_value(qid, lifts)]


def _is_neutral(qid, value, lifts):
    """ROUTE 1 of the degeneracy test, on the VALUE OBJECT: is the family's
    single value the neutral one?  For Q8 the test is STRUCTURAL and
    independent of the construction -- every seam in the value is the
    one-atom partition -- which is exactly the property `the one-atom seam`
    names."""
    if MUTANT == "degeneracy-lax":
        return False
    if qid == "Q8":
        return bool(value) and all(seam == ONEATOM for _o, seam, _n in value)
    return value == neutral_value(qid, lifts)


def _route2_neutral(qid, sv_canon, lifts):
    """ROUTE 2, independent of route 1: the canonical string of the single
    family value compared against the CONSTRUCTED neutral object."""
    if sv_canon is None:
        return False
    if qid == "Q8":
        return any(sv_canon == canon(neutral_value(qid, lifts, p))
                   for _n, p, _v in PATCHES)
    return sv_canon == canon(neutral_value(qid, lifts))


# ---------------------------------------------------------------------------
# 5.  CONTROLS -- positive, negative, and the ACTION-TOO-WEAK kill.
# ---------------------------------------------------------------------------

def run_controls(rows, fam):
    prog("controls: positive, negative, nondegeneracy witnesses")
    R = {r["quantity"]: r for r in rows}
    pos = [q for q, _n, _f, _r, _a, _t, _nv, c in QUANTITIES if c == "positive"]
    neg = [q for q, _n, _f, _r, _a, _t, _nv, c in QUANTITIES if c == "negative"]
    # THE POSITIVE CONTROLS, RE-ANCHORED ON MEASUREMENT.  Under the re-founded
    # derivation a quantity is an artifact if it moves in ANY arena coordinate,
    # and Q1 -- the declared law's own transition data -- of course moves with
    # the law: that is its argument, not an arena effect.  What the positive
    # control asserts, and what is measured, is PER COORDINATE: the fine grain
    # does not move when the coarse declaration, the state or the naming moves.
    pos_claim = {"Q1": ("patch", "state", "relabelling"),
                 "Q2": ARENA_COORD_NAMES}
    pos_measured = {q: {c: R[q]["dependence_profile"][c]["moves"]
                        for c in pos_claim[q]} for q in pos}
    gate("SYN-POSITIVE-CONTROLS", "derivation",
         "THE DECLARED POSITIVE CONTROLS BEHAVE, PER COORDINATE.  Q1, the "
         "fine-grained law's transition data, is FIXED under the patch "
         "declaration, under the state and under an admitted relabelling of "
         "the whole configuration -- it moves only with the law, which is its "
         "own argument.  Q2, the one-step closed holonomy, is fixed under "
         "EVERY arena coordinate including the gauge.  The control is stated "
         "coordinate by coordinate because that is what is measured; the "
         "reviewed instrument stated it as a single label, and the label was "
         "an artifact of the READS declaration",
         all(not m for q in pos for m in pos_measured[q].values()),
         {"claim": {q: list(pos_claim[q]) for q in pos},
          "measured_to_move": pos_measured,
          "verdicts": {q: R[q]["verdict"] for q in pos}})
    neg_moves = {q: R[q]["moves_under"] for q in neg}
    gate("SYN-NEGATIVE-CONTROL", "derivation",
         "THE DECLARED NEGATIVE CONTROL MOVES, AND MOVES WITH THE LAW.  Q5, "
         "the legitimacy certificate of a FIXED patch declaration, changes "
         "when the arena's law changes -- which is the thesis itself, "
         "measured: the same declared patch receives different certificates "
         "in different admissible arenas.  The gate names the coordinate, so "
         "that a family which merely renamed things could not satisfy it",
         all(R[q]["verdict"] == f"ARENA-ARTIFACT-{q}" for q in neg)
         and all("law" in v for v in neg_moves.values()),
         {"verdicts": {q: R[q]["verdict"] for q in neg},
          "moves_under": neg_moves,
          "certificates_per_declaration_de_named":
              {q: R[q]["distinct_values_per_declaration_de_named"]
               for q in neg}})
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
                 "configurations",
                 "admissible_law_patch_instances": len(idf),
                 "distinct_admissible_patches":
                     len({p for p, _lf, _law, _r in idf}),
                 "distinct_identity_free_laws":
                     len({lf for _p, lf, _law, _r in idf}),
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
    wit["Q1"] = {"witness": "the five committed laws themselves -- NOT an "
                 "ambient object: they are the family's own law coordinate, "
                 "so this is a measurement of separation and not a "
                 "nondegeneracy witness, and it is not gated as one",
                 "distinct_transition_data": len({
                     canon(tuple(sorted(L2.key(F) for F in law)))
                     for _n, law in fam["laws"]}),
                 "ambient": False}
    # -- Q8's witness, THROUGH Q8's OWN FUNCTION and on a NON-CHAIN triple.
    #    The reviewed witness was `meet(p, one-atom) == one-atom`, a lattice
    #    identity true of any input whatsoever and computed outside Q8.
    li0 = [n for n, _l in fam["laws"]].index("DET")
    law0, idp = fam["laws"][li0][1], tuple(range(CARRIER))
    lifts0 = [U for U, _e in L5.admitted_lift_family()[0]]
    NONCHAIN = (("ambient 2+3", ((0, 1), (2, 3, 4)), "AMBIENT"),
                ("ambient 3+2", ((0, 1, 2), (3, 4)), "AMBIENT"),
                ("ambient fine", tuple((j,) for j in range(CARRIER)),
                 "AMBIENT"))
    amb_seams = {nm: [[o, pk(s), n] for o, s, n in
                      q8_cross_arena_overlap(p, li0, law0, L2.RHO, idp,
                                             lifts0, NONCHAIN)]
                 for nm, p, _v in NONCHAIN}
    amb_atoms = sorted({n for r in amb_seams.values() for _o, _s, n in r})
    fam_atoms = sorted({n for _nm, p, _v in PATCHES for _o, _s, n in
                        q8_cross_arena_overlap(p, li0, law0, L2.RHO, idp,
                                               lifts0)})
    strictly_coarser = sum(
        1 for nm, p, _v in NONCHAIN for _o, s, _n in
        q8_cross_arena_overlap(p, li0, law0, L2.RHO, idp, lifts0, NONCHAIN)
        if len(s) < len(p))
    wit["Q8"] = {"witness": "an AMBIENT NON-CHAIN triple of boundaries "
                 "outside the declared family, run through Q8's own "
                 "function: two of its members are incomparable, so their "
                 "seam is strictly coarser than both rather than the coarser "
                 "member, and it collapses to the ONE-ATOM seam -- the "
                 "declared neutral value, which the family's own seams never "
                 "are",
                 "ambient": True, "ambient_seams": amb_seams,
                 "ambient_seam_atom_counts": amb_atoms,
                 "family_seam_atom_counts": fam_atoms,
                 "ambient_seams_strictly_coarser_than_both": strictly_coarser}
    TABLES["nondegeneracy_witnesses"] = wit
    # -- THE SEAM'S ORIENTATION, GATED and not merely anchored.  The seam of
    #    two boundaries is the finest COMMON COARSENING: it must be coarser
    #    than -- or equal to -- both of the patches it joins.  The lattice
    #    opposite (the join, the finest common refinement) fails this at the
    #    first pair, so `seam-orient` now dies at a GATE and not only at the
    #    typed atom counts of anchor A14.
    ord_ok, ord_tested = 0, 0
    for _nm, p, _v in PATCHES:
        for o, s, _n in q8_cross_arena_overlap(p, li0, law0, L2.RHO, idp,
                                               lifts0):
            q = tuple(tuple(int(c) for c in b) for b in o.split("|"))
            ord_tested += 1
            if (CB.part_meet(p, s) == s and CB.part_meet(q, s) == s):
                ord_ok += 1
    gate("SYN-SEAM-ORDER", "derivation",
         "THE SEAM IS A COMMON COARSENING, GATED.  What Q8 returns for a "
         "pair of declared boundaries must be COARSER THAN OR EQUAL TO both "
         "of them -- that is what `the finest common coarsening, which is "
         "the intersection of the two boundary algebras` means, and it is "
         "the property that makes the seam a seam rather than its lattice "
         "opposite.  It is checked here at every declared pair by "
         "recomputing the meet of the seam with each member.  In the "
         "reviewed instrument replacing the meet by the join left the Q8 "
         "verdict standing and killed only a typed atom count",
         ord_tested > 0 and ord_ok == ord_tested,
         {"declared_pairs_tested": ord_tested,
          "seams_coarser_than_or_equal_to_both_members": ord_ok})
    gate("SYN-NONDEGENERACY", "derivation",
         "EVERY QUANTITY GATED CONSTANT IS SHOWN TO BE A WORKING INSTRUMENT, "
         "AND THE SEAM IS SHOWN TO HAVE CONTENT.  For each, a DECLARED "
         "AMBIENT WITNESS outside the admissible-arena family is exhibited "
         "at which the quantity takes another value: omega is non-zero at "
         "reduced preparations; the rigidity classifier returns proper "
         "coarse charts on the identity-free side; the holonomy takes other "
         "values off the unitary constraint; and -- run THROUGH Q8's own "
         "function on an ambient NON-CHAIN triple -- the seam collapses to "
         "the one-atom neutral, which no seam of the declared family is.  "
         "Q1's `witness` is the family's own law coordinate and is therefore "
         "NOT ambient; it is reported as a separation measurement and "
         "deliberately not gated as a nondegeneracy witness",
         nz > 0 and len(idf) > 0 and proper > 0 and len(amb) > 1
         and min(amb_atoms) == 1 and min(fam_atoms) > 1
         and strictly_coarser > 0,
         wit)
    return wit


# ---------------------------------------------------------------------------
# 6.  THE SECTION-14 SELF-TEST.
# ---------------------------------------------------------------------------

def _broken_action(part, sigma, law, rho):
    """MIS-CONVENTION 1, the SEAM control: the arena's own patch is relabelled
    while the OTHER declared patches, the law and the state are left alone.
    Measured, this differs from the census's own action in exactly one thing
    -- the `sigma` handed to the quantity -- because an admitted sigma fixes
    the law setwise and the state POINTWISE anyway (0 of 1073 move either).
    So it bites exactly the quantities whose definition names `sigma`."""
    return act_part(part, sigma), law, rho


def _fn_of(qid):
    return dict((q, f) for q, _n, f, _r, _a, _t, _nv, _c in QUANTITIES)[qid]


def run_selftest(rows, fam):
    """THE SECTION-14 SELF-TEST, EVALUATED FRESH.  Three properties the
    reviewed instrument did not have: (i) the tested set is the DECLARED
    quantity list, never the set of quantities the census has just gated
    fixed -- a self-test whose scope shrinks to its own survivors cannot
    fail; (ii) every evaluation in this phase BYPASSES the value-level memos,
    so the two sides of an equivariance test are separately computed objects
    and not one memoized object compared with itself, and the phase's
    cache-hit count is gated at zero; (iii) the anti-vacuity counters are IN
    the gate predicates rather than beside them, measured per quantity as the
    instances in which either side of the test actually differs from the
    base."""
    global _FRESH
    prog("section-14 self-test: FRESH evaluation, every memo bypassed")
    laws, states = fam["laws"], fam["states"]
    patches = census_domain(fam)[0]
    lifts = [U for U, _e in L5.admitted_lift_family()[0]]
    idp = tuple(range(CARRIER))
    for k in _CACHE:
        _CACHE[k] = 0
    _ADJ.clear()
    _FRESH = True

    # -- the measured mechanism of the admitted action, first: how much does
    #    an admitted relabelling actually move?
    sig_moves_law = sig_moves_state = sig_total = 0
    for li, (_ln, law) in enumerate(laws):
        for _sn, rho in states:
            for sigma in admitted_group(li, law, rho):
                sig_total += 1
                if act_law_set(law, sigma) != {L2.key(F) for F in law}:
                    sig_moves_law += 1
                if act_rho(rho, sigma) != rho:
                    sig_moves_state += 1

    # -- (a) the admitted relabellings, applied to the whole configuration,
    #        over the DECLARED tested set, freshly evaluated, per quantity
    tested_set = SELFTEST_QUANTITIES
    if MUTANT == "selftest-scope":
        # THE REVIEWED DEFECT, REINSTATED: the tested set recomputed from the
        # census's own verdicts, so that a quantity a broken transport makes
        # move is deleted from the test rather than failing it.
        tested_set = tuple(r["quantity"] for r in rows
                           if not r["verdict"].startswith("ARENA-ARTIFACT"))
    per, bad1 = {}, {}
    for qid in tested_set:
        fn = _fn_of(qid)
        fixed = tested = disc = teeth = 0
        bm = bt = 0
        for _dn, d, _pv in patches:
            for li, (_ln, law) in enumerate(laws):
                for _sn, rho in states:
                    base = evaluate(qid, fn, d, li, law, rho, lifts, idp)
                    for sigma in admitted_group(li, law, rho):
                        rp, rr = act_part(d, sigma), act_rho(rho, sigma)
                        v = evaluate(qid, fn, rp, li, law, rr, lifts, sigma)
                        t = transport(qid, base, sigma)
                        tested += 1
                        if (rp, rr) != (d, rho):
                            disc += 1
                        if v != base or t != base:
                            teeth += 1
                        if v == t:
                            fixed += 1
                        # -- MIS-CONVENTION 1, in the same fresh pass and
                        #    against the same freshly transported base: the
                        #    arena's own patch relabelled, the OTHER declared
                        #    patches left alone.
                        if sigma != idp:
                            p2, l2_, r2 = _broken_action(d, sigma, law, rho)
                            vb = evaluate(qid, fn, p2, li, l2_, r2, lifts,
                                          idp)
                            bt += 1
                            if vb != t:
                                bm += 1
        per[qid] = {"tested": tested, "fixed": fixed,
                    "configurations_actually_moved": disc,
                    "instances_where_either_side_differs_from_the_base": teeth}
        bad1[qid] = {"instances": bt, "failures": bm}
        prog(f"  relabel {qid}: {fixed}/{tested} fixed, {teeth} with teeth; "
             f"broken control 1: {bm}/{bt}")
    tested = sum(p["tested"] for p in per.values())
    fixed = sum(p["fixed"] for p in per.values())
    disc = sum(p["configurations_actually_moved"] for p in per.values())
    teeth = sum(p["instances_where_either_side_differs_from_the_base"]
                for p in per.values())
    teeth_q = sorted(q for q in per
                     if per[q]["instances_where_either_side_"
                               "differs_from_the_base"] > 0)
    gate("SYN-ST-RELABEL", "derivation",
         "SECTION 14, THE SYMMETRY SELF-TEST.  Every admitted relabelling is "
         "applied to the WHOLE declared configuration -- patch, law, state "
         "and, for the seam, the other declared patches -- at every arena of "
         "the family, and EVERY DECLARED QUANTITY, not merely the ones the "
         "census has just gated fixed, is FIXED under every one of them, "
         "transported by its declared transport.  The ANTI-VACUITY counter "
         "is in this predicate, not beside it: the number of instances in "
         "which either side of the equality actually differs from the base "
         "is measured PER QUANTITY, and at least two quantities must have "
         "teeth.  A wrong value transport, a wrong relabelling group, a "
         "name-reading quantity, an un-corelabelled seam or a collapsed "
         "action all fail here",
         (tuple(per) == SELFTEST_QUANTITIES
          and all(per[q]["fixed"] == per[q]["tested"] and per[q]["tested"] > 0
                  for q in SELFTEST_QUANTITIES)
          and teeth > 0 and len(teeth_q) > 1),
         {"instances": tested, "fixed": fixed,
          "the_set_actually_tested": list(per),
          "instances_where_the_configuration_actually_moved": disc,
          "quantities": list(SELFTEST_QUANTITIES),
          "quantities_whose_test_has_teeth": teeth_q,
          "per_quantity": per,
          "the_admitted_action_measured": {
              "relabellings": sig_total,
              "that_move_the_law": sig_moves_law,
              "that_move_the_state": sig_moves_state}})
    gate("SYN-ST-FRESH", "derivation",
         "THE SELF-TEST EVALUATES FRESH (RUNBOOK section 14 addendum).  A "
         "self-test that reaches its quantity through the instrument's own "
         "memoization tests the CACHE, not the quantity: in the reviewed "
         "instrument three of the equivariance rows were literally `x == x` "
         "on one memoized object.  Every evaluation and every transport in "
         "this phase bypasses the three value-level memos -- the ones whose "
         "keys omit coordinates the census varies -- and the phase's "
         "value-cache HIT count is gated at ZERO with its miss count gated "
         "positive.  The adjudication sub-expression cache, whose key is the "
         "full (record, law) pair that determines it, is CLEARED here rather "
         "than bypassed and its misses are gated positive too (Deviation 10)",
         (_CACHE["value_cache_hits"] == 0
          and _CACHE["value_cache_misses"] > 0
          and _CACHE["adjudication_cache_misses"] > 0),
         dict(_CACHE))

    # -- (b) the 512 switchings x the 512 lifts, on the whole carried diagram
    gs = gauge_sweep(fam, lifts)
    sw = fam["switch_objects"]
    moved, badmoved = gs["carried_invariant_moved"], gs["unclosed_control_moved"]
    gate("SYN-ST-SWITCH", "derivation",
         "SECTION 14 AT THE GAUGE COORDINATE, EXHAUSTIVELY.  Every one of the "
         "512 checkpoint-phase switchings is applied to the whole carried "
         "diagram and EVERY ONE of the 512 members of the declared admitted "
         "lift family is switched -- the full cross product, which the "
         "reviewed instrument sampled at 32 lifts while claiming the family "
         "-- and the one-step closed holonomy is fixed at every instance.  "
         "The negative control reconstructed inside this test, the UNCLOSED "
         "convention (the walk that does not return to its start), MOVES "
         "under most of them.  Exhaustiveness is in the predicate",
         (moved == 0 and badmoved > len(sw) // 2 and len(sw) == 512
          and gs["lifts_swept"] == gs["lift_family"]),
         {"switchings": len(sw), "carried_invariant_moved": moved,
          "unclosed_control_moved": badmoved,
          "lifts_swept": gs["lifts_swept"], "lift_family": gs["lift_family"],
          "instances": gs["instances"],
          "scope": f"[EXH] all {len(sw)} switchings x [EXH] all "
                   f"{gs['lifts_swept']} declared lifts = {gs['instances']} "
                   f"instances"})

    # -- (c) THE MIS-CONVENTIONED ACTIONS.  Two of them, and what each one
    #        can bite is measured rather than asserted.  Control 1 was run in
    #        the same fresh pass as (a), against the same freshly transported
    #        base, so that the two comparisons are the same measurement seen
    #        two ways rather than two measurements of the same cache.
    # MIS-CONVENTION 2, CONSTRUCTED OUTSIDE THE ADMITTED GROUP.  No admitted
    # relabelling moves the law or the state -- measured, 0 of 1073 for each
    # -- so no control built from an admitted relabelling can give a
    # law-reading quantity any teeth: relabelling the patch `while the law is
    # left alone` is not a deviation from the census's action, it IS the
    # census's action.  This control is therefore built from the relabellings
    # the arena does NOT admit, where leaving the law unrelabelled is a real
    # mis-convention, and it is labelled as constructed outside the group.
    bad2, d0 = {}, patches[0][1]
    for qid in SELFTEST_QUANTITIES:
        fn = _fn_of(qid)
        bm = bt = 0
        for li, (_ln, law) in enumerate(laws):
            rho = states[0][1]
            G = set(admitted_group(li, law, rho))
            base = evaluate(qid, fn, d0, li, law, rho, lifts, idp)
            for sigma in permutations(range(CARRIER)):
                if sigma in G:
                    continue
                v = evaluate(qid, fn, act_part(d0, sigma), li, law, rho,
                             lifts, idp)
                bt += 1
                if v != transport(qid, base, sigma):
                    bm += 1
        bad2[qid] = {"instances": bt, "failures": bm}
    b1 = sum(v["failures"] for v in bad1.values())
    b2 = sum(v["failures"] for v in bad2.values())
    reads_sigma = [q for q in SELFTEST_QUANTITIES
                   if "relabelling" in FINDINGS["signature_scan"][q]]
    gate("SYN-ST-BROKEN", "derivation",
         "THE DELIBERATELY MIS-CONVENTIONED CONTROLS MOVE, AND WHAT EACH CAN "
         "BITE IS MEASURED.  Control 1 relabels the arena's own patch and "
         "leaves the OTHER declared patches unrelabelled.  It does NOT leave "
         "the law and the state alone in any operative sense -- the census's "
         "own action leaves them alone too, because an admitted relabelling "
         "fixes the law setwise and the state POINTWISE, measured 0 of 1073 "
         "for each -- so control 1 differs from the true action in exactly "
         "one thing, the sigma handed to the quantity, and it therefore "
         "bites exactly the quantities whose definition names sigma.  "
         "Control 2 is CONSTRUCTED OUTSIDE THE ADMITTED GROUP, from "
         "relabellings the arena does not admit and transporting by the "
         "INVERSE, so that the law and the state really do move: it bites "
         "the nomological quantities, which control 1 cannot.  Both must "
         "fail somewhere and the per-quantity split is reported",
         b1 > 0 and b2 > 0 and len(reads_sigma) > 0
         and all(bad1[q]["failures"] > 0 for q in reads_sigma if q in bad1)
         and all(q in bad1 for q in reads_sigma),
         {"control_1_the_seam_left_unrelabelled": bad1,
          "control_1_total_failures": b1,
          "quantities_whose_definition_names_the_relabelling": reads_sigma,
          "control_2_outside_the_admitted_group": bad2,
          "control_2_total_failures": b2,
          "control_2_scope": f"[EXH] the legitimate declaration x "
                             f"{len(laws)} committed laws x the committed "
                             f"named state x every relabelling the arena "
                             f"does NOT admit"})

    # -- (d) THE NAME-READER CONTROL: a label-reading statistic must move
    def name_reader(part, law_id, law, rho, sigma, lifts):
        """Branch C's D3: reads whether the configuration NAMED 0 is a
        singleton block.  Declared covariant transport: identity."""
        return int(any(b == (0,) for b in part))
    nr_moved, nr_tested = 0, 0
    for li, (_ln, law) in enumerate(laws):
        for si, (_sn, rho) in enumerate(states):
            for sigma in admitted_group(li, law, rho):
                for _dn, d, _pv in patches:
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
    _FRESH = False
    TABLES["self_test"] = {
        "relabel_per_quantity": per, "cache": dict(_CACHE),
        "the_admitted_action_measured": {
            "relabellings": sig_total, "that_move_the_law": sig_moves_law,
            "that_move_the_state": sig_moves_state},
        "broken_control_1_per_quantity": bad1,
        "broken_control_2_per_quantity": bad2,
        "switch": {"switchings": len(sw), "lifts": gs["lifts_swept"],
                   "instances": gs["instances"], "moved": moved,
                   "unclosed_control_moved": badmoved},
        "name_reader": {"instances": nr_tested, "moved": nr_moved}}
    return {"relabel": {"tested": tested, "fixed": fixed, "moved_cfg": disc},
            "switch": {"swept": len(sw), "moved": moved,
                       "control_moved": badmoved},
            "broken": b1 + b2, "name_reader": nr_moved}


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


AMP_BLOCK = (0, 1)      # the two configurations the declared lift acts on


def _block(M):
    return tuple(tuple(M[i][j] for j in AMP_BLOCK) for i in AMP_BLOCK)


def _mod2(z):
    """|z|^2 = z * conj(z), a REAL element of Q(zeta_8) -- which need not be
    rational (sqrt 2 = zeta - zeta^3 is real), so the whole 4-tuple is
    carried and compared, never its first coordinate alone."""
    return zmul(z, zconj(z))


HALF = (Fr(1, 2), Fr(0), Fr(0), Fr(0))


def _is_fully_unbiased(M):
    """Every entry of the carried block has modulus exactly 2^(-1/2) -- the
    property that actually separates the zero-defect members of the lift
    family, two-sidedly."""
    return all(_mod2(v) == HALF for r in _block(M) for v in r)


def _is_monomial(M):
    """Exactly one non-zero entry in each row and each column of the block."""
    b = _block(M)
    return (all(sum(1 for v in r if v != Z0) == 1 for r in b)
            and all(sum(1 for r in b if r[j] != Z0) == 1
                    for j in range(len(b))))


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


QOPT_NAMES = ("BLOCKED-AT-IMPORT",
              "BLOCKED-AT-THE-NON-MONOMIAL-ADMITTED-OPERATION",
              "ARENA-ARTIFACT-Q-OPT", "ARENA-INERT-Q-OPT",
              "ARENA-INVARIANT-Q-OPT")

# The declared condition tuples the selector is exercised on, one per name:
# (the arithmetic transports, the question is posable, non-zero defects, the
# non-monomial control fires).
QOPT_CONDITIONS = ((False, False, 0, True), (True, False, 0, True),
                   (True, True, 1, True), (True, True, 0, True),
                   (True, True, 0, False))


def _qopt_name(t1, posable, nz, ctrl_nonzero):
    """THE VERDICT SELECTOR, factored out so that the reachability of every
    pre-registered name is a COMPUTATION and not a claim."""
    if MUTANT == "qopt-blind":       # the reviewed two-name form, restored
        return ("ARENA-INERT-Q-OPT" if (t1 and nz == 0 and ctrl_nonzero)
                else "BLOCKED-AT-IMPORT")
    if not t1:
        return "BLOCKED-AT-IMPORT"
    if not posable:
        return "BLOCKED-AT-THE-NON-MONOMIAL-ADMITTED-OPERATION"
    if nz > 0:
        return "ARENA-ARTIFACT-Q-OPT"
    if ctrl_nonzero:
        return "ARENA-INERT-Q-OPT"
    return "ARENA-INVARIANT-Q-OPT"


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
    gate("SYN-QOPT-T2", "disclosure",
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
         "lifted step.  DISCLOSURE CLASS, and why: the two routes compute "
         "the same predicate by different means, so no mutant short of a "
         "stub can separate them; the gate records a measurement rather "
         "than enforcing a claim",
         liftable == liftable2 and len(admits) == len(fam["laws"]),
         {"committed_laws_admitting_the_lifted_step": admits,
          "some_committed_law_admits_the_lifted_step": t2,
          "unitarily_liftable_admitted_operations": liftable,
          "second_route": liftable2})

    # -- THE MONOMIAL THEOREM, exhaustively.  B of a monomial unitary is its
    #    underlying permutation matrix and B is multiplicative on monomials,
    #    so Delta^B vanishes on every monomial pair.  This is a THEOREM, not
    #    a census: it is confirmed here over ALL admitted permutation pairs
    #    and over PHASED monomial pairs, which the reviewed sweep -- built
    #    from Z1/Z0 entries alone -- never touched.
    perms = [p for p in permutations(range(CARRIER))]
    sub = perms[:24] if MUTANT == "qopt-subsample" else perms

    def _perm_matrix(a, ph=None):
        return tuple(tuple((Z1 if ph is None else zpow(ph[j])) if a[j] == i
                           else Z0 for j in range(CARRIER))
                     for i in range(CARRIER))
    nz, pairs = 0, 0
    for a in sub:
        Ua = _perm_matrix(a)
        for b in sub:
            pairs += 1
            if not _is_zero(deltaB(Ua, _perm_matrix(b))):
                nz += 1
    phased_nz, phased = 0, 0
    for i, a in enumerate(perms):                 # a DECLARED phased sweep:
        for k in range(NROOT):                    # every permutation, eight
            pa = [(i + j * k) % NROOT for j in range(CARRIER)]
            pb = [(k + j * i) % NROOT for j in range(CARRIER)]
            phased += 1
            if not _is_zero(deltaB(_perm_matrix(a, pa),
                                   _perm_matrix(perms[(i * 7 + k) % 120],
                                                pb))):
                phased_nz += 1
    # POSITIVE CONTROL: the defect is non-zero on the declared NON-monomial
    # lift, which is exactly the object no committed law admits.
    U0 = _from_amp(lifts[0][0])
    ctrl_nonzero = not _is_zero(deltaB(U0, U0))
    if MUTANT == "qopt-force":       # a non-monomial operation FORCED into
        nz += 1 if not _is_zero(deltaB(U0, U0)) else 0    # the swept set
    gate("SYN-QOPT-VALUE", "derivation",
         "THE VALUE, WHERE THE OBJECT TRANSPORTS, OVER EVERY PAIR.  The "
         "sweep is EXHAUSTIVE over all 14,400 composable pairs of admitted "
         "reversible operations at the committed carrier -- the reviewed "
         "instrument swept 576, which was not a sample but the square of the "
         "point stabilizer of one configuration -- and over a declared "
         "PHASED monomial sweep as well, since the reversible lifts are "
         "monomial and not merely permutation matrices.  Delta^B is "
         "identically ZERO on all of them, which is the monomial theorem, "
         "not a measurement that could have gone otherwise.  The positive "
         "control fires: on the declared non-monomial lift the same "
         "instrument returns a NON-zero defect, so the zero is a fact about "
         "the admitted operations and not about the instrument.  "
         "Exhaustiveness is in the predicate",
         (nz == 0 and phased_nz == 0 and ctrl_nonzero
          and pairs == len(perms) ** 2),
         {"admitted_pairs_swept": pairs, "non_zero_defects": nz,
          "phased_monomial_pairs_swept": phased,
          "non_zero_defects_phased": phased_nz,
          "positive_control_non_zero_on_the_declared_lift": ctrl_nonzero})

    # -- THE VERDICT.  All four of the pin's names are reachable from here.
    #    `posable` is the question the census would have to answer: does any
    #    committed law admit an operation on which Delta^B could be non-zero?
    posable = any(admits.values()) or (MUTANT == "qopt-force")
    verdict = _qopt_name(t1, posable, nz, ctrl_nonzero)
    corridor = {str(c): _qopt_name(*c) for c in QOPT_CONDITIONS}
    obstruction = ("the composition defect transports EXACTLY -- the "
                   "arithmetic and the object both -- but the arena-variation "
                   "question cannot be POSED at the committed laws: Delta^B "
                   "is identically zero on monomials by a theorem, no "
                   "committed law admits a non-monomial operation, and there "
                   "is therefore no admissible arena at which the quantity "
                   "could take a second value.  That is BLOCKED, not INERT")
    gate("SYN-QOPT-NAMES", "derivation",
         "THE VERDICT CORRIDOR IS OPEN, AND THAT IS COMPUTED HERE.  Q-OPT's "
         "verdict is selected from ALL of the pin's names by measured "
         "conditions -- BLOCKED-AT-IMPORT if the arithmetic does not "
         "transport, BLOCKED-AT-THE-NON-MONOMIAL-ADMITTED-OPERATION if no "
         "committed law admits an operation at which the defect could be "
         "non-zero, ARENA-ARTIFACT if it is non-zero somewhere admitted, "
         "ARENA-INERT if it is everywhere the neutral with the control "
         "firing, ARENA-INVARIANT otherwise.  The reviewed instrument could "
         "emit only TWO of the four, so its verdict was fixed before any "
         "fixture was consulted.  The predicate is that the selector, run "
         "over the declared condition tuples, actually REACHES every name; "
         "and the `qopt-force` mutant, which admits a non-monomial "
         "operation, makes the live selection come out differently",
         len(set(corridor.values())) == len(QOPT_NAMES)
         and set(corridor.values()) == set(QOPT_NAMES)
         and verdict in QOPT_NAMES,
         {"verdict": verdict, "arithmetic_transports": t1,
          "the_question_is_posable": posable,
          "non_zero_defects_over_the_admitted_pairs": nz,
          "names_reached_by_the_selector": corridor})
    FINDINGS["Q_OPT"] = {"verdict": verdict, "obstruction": obstruction,
                         "transport_arithmetic": t1,
                         "some_committed_law_admits_the_lifted_step": t2}
    # -- the non-monomial control, and WHAT the 128 zero-defect members are.
    fam_nz, sq_mono, sq_flat = 0, {True: 0, False: 0}, {True: 0, False: 0}
    for U, _e in lifts:
        M = _from_amp(U)
        z = _is_zero(deltaB(M, M))
        fam_nz += 0 if z else 1
        sq = zmatmul(M, M)
        sq_mono[z] += 1 if _is_monomial(sq) else 0
        sq_flat[z] += 1 if _is_fully_unbiased(sq) else 0
    TABLES["q_opt"] = {"laws_admitting_the_lifted_step": admits,
                       "unitarily_liftable_admitted_operations": liftable,
                       "admitted_pairs_swept": pairs, "non_zero_defects": nz,
                       "phased_monomial_pairs_swept": phased,
                       "non_zero_defects_phased": phased_nz,
                       "lift_family": len(lifts),
                       "non_zero_defects_in_the_family": fam_nz,
                       "zero_defect_members": len(lifts) - fam_nz,
                       "of_the_zero_defect_members_the_square_is_monomial":
                           sq_mono[True],
                       "of_the_zero_defect_members_the_square_is_fully_"
                       "unbiased": sq_flat[True],
                       "of_the_non_zero_members_the_square_is_monomial":
                           sq_mono[False],
                       "of_the_non_zero_members_the_square_is_fully_"
                       "unbiased": sq_flat[False],
                       "scope": "[EXH] all admitted permutation pairs; [EXH] "
                       "the whole 512-member declared non-monomial lift "
                       "family; a declared phased monomial sweep"}
    gate("SYN-QOPT-SCOPE", "derivation",
         "THE NON-MONOMIAL CONTROL, AND WHAT SEPARATES ITS TWO HALVES, "
         "MEASURED.  The control is [EXH] over the whole 512-member declared "
         "lift family and the defect is non-zero on 384 of them, not on all. "
         " The reviewed characterisation of the remaining 128 -- `the phase "
         "choices whose square is again non-monomial` -- is FALSE, and "
         "measurably so: 128 of the 384 non-zero members also have "
         "non-monomial squares.  The true criterion is two-sided and is "
         "gated here: Delta^B(U,U) = 0 exactly when U^2 is again FULLY "
         "UNBIASED, every entry of modulus 2^(-1/2) -- 128 of 128 on one "
         "side and 0 of 384 on the other",
         (fam_nz > 0 and fam_nz < len(lifts)
          and sq_flat[True] == len(lifts) - fam_nz and sq_flat[False] == 0),
         {"lift_family": len(lifts), "non_zero_defects_in_the_family": fam_nz,
          "zero_defect_members": len(lifts) - fam_nz,
          "square_fully_unbiased_among_the_zero_defect_members":
              sq_flat[True],
          "square_fully_unbiased_among_the_non_zero_members": sq_flat[False],
          "square_non_monomial_among_the_non_zero_members":
              fam_nz - sq_mono[False],
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


# THE FALSIFICATION SUITE.  Every mutant perturbs a COMPUTATION -- the six
# `anchor-*` mutants of the reviewed suite, which overwrote a computed field
# after every value had been computed and therefore tested only the reporting
# plumbing, are gone, replaced by mutants that break the thing each anchor or
# gate is supposed to be watching.  Three remain gate-input stubs and are
# named as such in the receipt.
MUTANTS = ["states-drop", "stab-lax", "action-weaken", "arena-collapse",
           "transport-lax", "memo-lax", "selftest-scope", "name-reader",
           "seam-orient", "seam-blind", "hidden-read", "hol-sign",
           "hol-orient", "gauge-subsample", "degeneracy-lax", "born-lax",
           "qopt-force", "qopt-subsample", "qopt-blind", "float-lax",
           "eps-lax", "omega-lax", "canon-lax", "declaration-lax",
           "verdict-lax", "freeze-lax", "pres-lax"]

INPUT_STUB_MUTANTS = ("float-lax", "degeneracy-lax")


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

    with ThreadPoolExecutor(max_workers=8) as ex:
        rows = list(ex.map(_run, MUTANTS))     # order = the declared order
    TABLES["mutants"] = rows
    killed = {k for r in rows
              for k in r["falsified_anchors"] + r["falsified_gates"]}
    must = [x["id"] for x in GATES if x["class"] != "disclosure"
            and x["id"] != "SYN-MUTANTS"]
    unfalsified = sorted(set(must) - killed)
    TABLES["gate_falsification"] = {
        "must_pass_gates": len(must), "falsified_by_some_mutant":
            len([g for g in must if g in killed]),
        "not_falsified_by_any_mutant": unfalsified,
        "gate_input_stub_mutants": list(INPUT_STUB_MUTANTS)}
    gate("SYN-MUTANTS", "freeze",
         "THE FALSIFICATION SUITE, RUN AND RECORDED, AND EVERY MUST-PASS "
         "GATE FALSIFIED BY AT LEAST ONE MUTANT.  Every declared mutant "
         "perturbs a COMPUTATION -- not one of them overwrites a computed "
         "field after the fact, which is what six of the reviewed suite's "
         "twenty did -- is run to completion, must EXIT 1, and must falsify "
         "at least one NAMED gate or anchor.  The second half of the "
         "predicate is the one the reviews asked for: the set of must-pass "
         "gates that NO mutant falsifies must be EMPTY, so that no gate can "
         "sit in the table incapable of failing.  SYN-MUTANTS itself is "
         "excluded from that count and its own falsification route is a "
         "mutant that fails to die.  The suite carries the holonomy's sign "
         "and orientation mutants, an orientation mutant of the seam's "
         "refinement order, a stat-label-style name-reader, a wrong value "
         "transport, a cache-reading self-test, an un-corelabelled seam, a "
         "hidden amplitude read one call level down, a subsampled gauge "
         "sweep, a subsampled defect sweep, a forced non-monomial admitted "
         "operation, a declaration-consulting verdict rule, an out-of-"
         "vocabulary verdict, a pre-freeze evaluation, a collapsed arena and "
         "a collapsed action",
         all(r["died"] and (r["falsified_anchors"] or r["falsified_gates"])
             for r in rows) and len(rows) == len(MUTANTS)
         and not unfalsified,
         {"mutants": len(rows), "died": sum(1 for r in rows if r["died"]),
          "must_pass_gates_never_falsified": unfalsified,
          "kills": {r["mutant"]: r["falsified_anchors"] + r["falsified_gates"]
                    for r in rows}})


def verdict(rows, qopt):
    """The completion tag is NOT reachable while any must-pass gate or anchor
    has failed: if the instrument's own mutants can flip a quantity's verdict
    while the unit still reports RQ0-SYNTH-CENSUS-COMPLETE, the tag means
    nothing.  The thesis sentence is DERIVED from the computed rows -- the
    reviewed instrument typed it, and under a mutant it contradicted the very
    tags printed above it."""
    g = {x["id"]: x for x in GATES}
    clean = (all(x["passed"] for x in GATES if x["class"] != "disclosure")
             and all(x["passed"] for x in ANCHORS))
    complete = (clean
                and g["SYN-CENSUS-COMPLETE"]["passed"]
                and g["SYN-POSITIVE-CONTROLS"]["passed"]
                and g["SYN-NEGATIVE-CONTROL"]["passed"]
                and g["SYN-ACTION-NOT-TOO-WEAK"]["passed"]
                and g["SYN-DECLARATION-INDEPENDENT"]["passed"]
                and g["SYN-ST-RELABEL"]["passed"]
                and g["SYN-ST-FRESH"]["passed"])
    tags = [r["verdict"] for r in rows] + [qopt]
    if complete:
        tags.append("RQ0-SYNTH-CENSUS-COMPLETE")
    if FINDINGS.get("ACTION_TOO_WEAK"):
        tags.append("ACTION-TOO-WEAK")
    R = {r["quantity"]: r for r in rows}
    moving = [r["quantity"] for r in rows if r["moves_under"]]
    still = [r["quantity"] for r in rows if not r["moves_under"]]
    law_movers = [r["quantity"] for r in rows
                  if "law" in r["dependence_profile"]
                  and r["dependence_profile"]["law"]["moves"]]
    law_blind = [r["quantity"] for r in rows
                 if "law" not in r["coordinates_the_definition_consumes"]]
    FINDINGS["verdict"] = {
        "tags": tags,
        "census_complete": complete,
        "thesis": (
            "ADOPTED-ARENA-RELATIVITY: the legitimacy of a coarse patch is "
            "relative to a DECLARED ARENA.  Measured here, and stated from "
            "the computed table rather than typed: " + ", ".join(moving) +
            " move under some arena coordinate and " + ", ".join(still) +
            " move under none; the quantities that move WITH THE LAW at a "
            "fixed patch declaration are " + ", ".join(law_movers) +
            "; the quantities whose definition never names the law, so that "
            "their law-fixity is definitional and not measured, are " +
            ", ".join(law_blind) + ".  The asymmetry the unit carries is "
            "between " + " and ".join(
                q for q in ("Q5", "Q8") if q in R) + ", which face the same "
            "declared action, the same fibration and the same sweep: the "
            "certificate of a fixed declaration takes " +
            str(R["Q5"]["distinct_values_per_declaration_de_named"][0]
                if "Q5" in R else 0) + " values per declaration as the law "
            "varies, the seam takes " +
            str(R["Q8"]["distinct_values_per_declaration_de_named"][0]
                if "Q8" in R else 0) + ".")}
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
    L.append("THE SIGNATURE SCAN (which arena coordinates each definition "
             "consumes at all)")
    sg = rec["tables"]["signature_scan"]
    for q, v in sorted(sg["arena_coordinates_the_definition_consumes"].items()):
        L.append(f"  {q}: consumes {v}; amplitude objects "
                 f"{sg['amplitude_objects_named'][q]}")
    L.append("")
    L.append("THE CENSUS")
    for r in rec["tables"]["census"]:
        L.append(f"  {r['quantity']}  {r['verdict']}")
        L.append(f"        {r['name']}")
        L.append(f"        distinct values over the family: "
                 f"{r['distinct_values_over_the_family']}; de-named, per "
                 f"declaration: "
                 f"{r['distinct_values_per_declaration_de_named']}; over all "
                 f"declarations: "
                 f"{r['distinct_values_over_all_declarations_de_named']}")
        L.append(f"        MEASURED to move under "
                 f"{r['moves_under'] or 'nothing'}; definition consumes "
                 f"{r['coordinates_the_definition_consumes']}")
        dp = r["dependence_profile"]
        for c in ("patch", "law", "state"):
            st = ("MOVES" if dp[c]["moves"] else
                  ("fixed [measured]"
                   if c in r["coordinates_the_definition_consumes"]
                   else "fixed [DEFINITIONAL: the definition never names it]"))
            L.append(f"        {c:12s} {st:52s} max distinct in a slice="
                     f"{dp[c]['max_distinct_values']}")
        L.append(f"        relabelling  equivariance failures="
                 f"{dp['relabelling']['equivariance_failures']} of "
                 f"{dp['relabelling']['tested']} "
                 f"({dp['relabelling']['configurations_actually_moved']} "
                 f"configurations actually moved; "
                 f"{dp['relabelling']['instances_where_either_side_differs_from_the_base']}"
                 f" with teeth)")
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
    L.append("MEASURED DISCLOSURES")
    for k, v in sorted(rec["tables"]["fibration_disclosure"].items()):
        L.append(f"  {k}: {v}")
    st = rec["tables"]["self_test"]
    L.append(f"  the admitted action: "
             f"{json.dumps(st['the_admitted_action_measured'], sort_keys=True)}")
    L.append(f"  self-test cache: {json.dumps(st['cache'], sort_keys=True)}")
    for k in ("broken_control_1_per_quantity", "broken_control_2_per_quantity"):
        L.append(f"  {k}: " + ", ".join(
            f"{q} {v['failures']}/{v['instances']}"
            for q, v in sorted(st[k].items())))
    if "gate_falsification" in rec["tables"]:
        L.append(f"  gate falsification: "
                 f"{json.dumps(rec['tables']['gate_falsification'], sort_keys=True)}")
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
    global MUTANT, SOURCE_SHA256, _FROZEN
    ap = argparse.ArgumentParser()
    ap.add_argument("--mutant", default=None)
    ap.add_argument("--quiet", action="store_true")
    ap.add_argument("--falsification-selftest", action="store_true")
    a = ap.parse_args()
    MUTANT = a.mutant
    SOURCE_SHA256 = hashlib.sha256(
        Path(__file__).resolve().read_bytes()).hexdigest()
    L2.MUTANT = "pres-lax" if MUTANT == "pres-lax" else None
    L3.MUTANT = None
    L4.MUTANT = {"stab-lax": "stab-lax", "omega-lax": "shape-lax"}.get(MUTANT)
    L5.MUTANT = MUTANT if MUTANT in ("hol-sign", "hol-orient") else None

    fam = build_family()
    if MUTANT in ("action-weaken", "arena-collapse"):
        # THE ACTION-WEAKENING MUTANT: the arena action collapsed to the
        # patch coordinate alone -- one law, one state, the trivial group.
        # ARENA-COLLAPSE goes one further and takes the patch too, so that
        # NOTHING moves and the pre-registered ACTION-TOO-WEAK kill fires.
        fam["laws"] = fam["laws"][:1]
        fam["states"] = fam["states"][:1]
        _STABL[(0, fam["states"][0][1])] = [tuple(range(CARRIER))]
    if MUTANT == "eps-lax":
        # EPSILON PERTURBED AS Q6 ACTUALLY USES IT: the reviewed `eps-lax`
        # stubbed a stage-5 routine the census never calls, so the ARTIFACT
        # verdict for Q6 and its orbit count had no mutant coverage at all.
        def _q6_lax(part, law_id, law, rho, sigma, lifts):
            """Epsilon read at the WRONG boundary: the one-atom chart instead
            of the arena's declared patch."""
            return L3.bayes_error(ONEATOM, rho)
        globals()["q6_epsilon"] = _q6_lax
        for i, q in enumerate(QUANTITIES):
            if q[0] == "Q6":
                QUANTITIES[i] = q[:2] + (_q6_lax,) + q[3:]
    if MUTANT == "canon-lax":
        # THE CANONICALISER COLLAPSED: every value receives the same key, so
        # every orbit count becomes 1 and nothing can be seen to move.  This
        # is the mutant that covers the orbit counts themselves.
        globals()["_canon"] = lambda v: "COLLAPSED"
    if MUTANT == "hidden-read":
        def _q3_hidden(part, law_id, law, rho, sigma, lifts):
            """Q3 with an AMPLITUDE read one call level down: a one-level
            source scan reports it switching-blind, the transitive scan of
            the repaired instrument catches it."""
            return q3_rigidity_classifier(part, law_id, law, rho, sigma,
                                          lifts) + (_shadow_amp(lifts),)
        for i, q in enumerate(QUANTITIES):
            if q[0] == "Q3":
                QUANTITIES[i] = q[:2] + (_q3_hidden,) + q[3:]
    if MUTANT == "omega-lax":
        L4.MUTANT = None

        def _q7_lax(part, law_id, law, rho, sigma, lifts):
            """Omega forced off its neutral value, so that the INERT verdict
            becomes INVARIANT."""
            return Fr(1)
        globals()["q7_omega"] = _q7_lax
        for i, q in enumerate(QUANTITIES):
            if q[0] == "Q7":
                QUANTITIES[i] = q[:2] + (_q7_lax,) + q[3:]
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

    if MUTANT == "freeze-lax":
        # FIXTURE TRUTH TOUCHED BEFORE THE FREEZE: the evaluation counter is
        # no longer zero when the declarations are recorded, which is the one
        # thing SYN-FREEZE exists to witness.
        _FROZEN = True
        evaluate("Q5", q5_legitimacy_certificate, PTOMO, 0,
                 fam["laws"][0][1], fam["states"][0][1],
                 [U for U, _e in L5.admitted_lift_family()[0]],
                 tuple(range(CARRIER)))
        _FROZEN = False

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
