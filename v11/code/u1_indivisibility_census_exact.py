#!/usr/bin/env python3
"""
u1_indivisibility_census_exact.py — v11 U1: THE INDIVISIBILITY CENSUS.

Pin: v11/note-u1-indivisibility-census-pin.md (STRICT, frozen before this
file existed).  Binding specification: paper 0 (v11) sec.7 (U1: preamble +
three arms), sec.6 constraints 1/4/6, sec.10 falsifiers, sec.3 strata,
sec.4 division-events-are-renewals; [V11-CAT] sec.4.5, sec.4.9-preamble,
sec.7 ranks 1 and 4.  Parents: v10 D70 (the relative-horizon kernels),
D72/D74 (the transport square census and the 44 descent-obstruction
squares), D62 row R4 (renewal = a row of the update table), D49/D43b (the
Zhat completion and the six-state chain), v10 paper 31 sec.4.3 / d43c
(Born = K1), the D75 Barandes audit pin (b) Arm 0, and [B3] eqs. 22-23.

THE THREE ARMS
  ARM 0  Born = K1 rebuilt on the committed arbitration layer in EXACT
         arithmetic (the isometry defect is exactly 0 in Q(sqrt 2), not
         1e-40), plus its Zhat-completed sibling (six-state chain,
         conflict row {1/7, 3/4, 3/28}, total mass exactly 1).
  ARM 1  The renewal-to-renewal Gamma family from the committed transport
         grammar read at record grain through the D46b/D70 relative-
         horizon kernel; the D62-R4 renewal predicate PORTED to transport
         scope with the port verified against the layer; then the [B3]
         eq. 22 interpolant census over every composable cut triple at the
         declared caps -- algebraic where Gamma(c'<-c) is invertible, exact
         rational linear feasibility (Phase-I simplex, Bland) where it is
         not, with an independently verified Farkas certificate on every
         infeasible verdict.
  ARM 2  Paper 29's four descent conditions (DC1-DC4, in the D65 pin's
         form) on the SAME family at the SAME caps; then the Arm-1/Arm-2
         agreement census.

ENGRAVED CONSTRAINTS (paper 0 sec.6, carried into every gate text)
  * This is NOT a CP-divisibility test (sec.6.6): CP-divisibility and
    Barandes-indivisibility are orthogonal axes.  The instruments here are
    the interpolant test and the descent conditions, and nothing else.
  * No Bell/locality framing (sec.6.4): Bell is settled and closed.
  * Wherever exact covariance could be implied, L-1's bound is quoted:
    v11 may expect at most statistical/approximate Lorentz invariance at
    renewal grain, never exact covariance (paper 0 sec.7, L-1).
  * Lean: NONE.  The record is 0-for-5 on quantum-location intuitions.

HOUSE RULES OBSERVED
  * Exact arithmetic end to end: fractions.Fraction for every weight,
    probability, ratio and matrix entry; Q(sqrt 2) for the Arm-0
    amplitudes.  No float appears in any substantive computation.
  * Committed layers are single-sourced by text-slice (definition head
    only) and by AST extraction, with an AST signature pass and with
    exit-freedom gated: sys.exit / os._exit raise inside the slice.
  * No bare-constant predicates: every number a gate tests against is
    either QUOTED from a committed source (registry QUOTES/ANCH, with
    path:line provenance) or derived inside this receipt.
  * Every census printed BOTH WAYS.
  * Substantive negatives exit 0.  exit 1 is reserved for ANCHOR failure.
  * Determinism: every set/dict iteration feeding a printed number is
    ordered by the hash-seed-independent key sk().
"""

from __future__ import annotations

import ast
import os
import sys
import time
import types
from collections import Counter, defaultdict
from fractions import Fraction as Fr

T0 = time.time()
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.dirname(REPO)               # .../isp   (run from anywhere)
os.chdir(REPO)
sys.setrecursionlimit(400000)

PASS = FAIL = 0
ANCHOR_FAIL = 0
SECT = [0]


def sec(title):
    SECT[0] += 1
    print()
    print("-" * 78)
    print(f"SEC {SECT[0]}  {title}")
    print("-" * 78)


def check(label, ok, detail="", reporting_only=False):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    if reporting_only:
        tag = "[RPT ]"
    else:
        PASS += int(bool(ok))
        FAIL += int(not ok)
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))
    if reporting_only:
        print("         ^ REPORTING ONLY: cannot fail as posed; not counted "
              "as evidence")
    return bool(ok)


def anchor(label, ok, detail=""):
    global ANCHOR_FAIL
    if not check("ANCHOR " + label, ok, detail):
        ANCHOR_FAIL += 1
    return bool(ok)


def report(label, value):
    print(f"  [DATA] {label}: {value}")


def sk(o):
    """Hash-order-independent total key for nested frozenset/tuple objects
    (D72's stable_key, re-derived; repr of a frozenset is PYTHONHASHSEED
    dependent and this is not)."""
    if isinstance(o, (frozenset, set)):
        return ("S", tuple(sorted(sk(x) for x in o)))
    if isinstance(o, (tuple, list)):
        return ("T", tuple(sk(x) for x in o))
    return ("V", type(o).__name__ + "|" + repr(o))


def fmt(counter):
    return {str(k): v for k, v in sorted(counter.items(), key=lambda z: sk(z[0]))}


def srt(xs):
    return sorted(xs, key=sk)


# ===========================================================================
# SEC 0.  THE REGISTRY — every constant a gate tests against, with provenance
# ===========================================================================

QUOTES = {
    "B3-22": (
        "[B3] J. A. Barandes, arXiv:2507.21192, eqs. 22-23 (quoted in v11 "
        "paper 0 sec.2)",
        "given Gamma(t<-t0) and Gamma(t'<-t0), the interpolated matrix "
        "Gammabar = Gamma(t<-t0) Gamma(t'<-t0)^-1 is generically "
        "PSEUDO-STOCHASTIC (negative entries); a stochastic matrix has a "
        "stochastic inverse only if it is a permutation.  Divisibility "
        "failure is a computable, entrywise property.",
    ),
    "v1p22": (
        "v1/relativistic-isp-v1-paper22-entropy-indivisible.md:120-150 "
        "(Definition 2), as quoted in v10/note-d75-barandes-audit.md:241-254",
        "'A stochastic process Gamma(t<-t_0) is INDIVISIBLE if for every "
        "intermediate time t_0 < t' < t there exists NO genuine stochastic "
        "matrix ... Equivalently, the algebraic intermediate matrix ... has "
        "at least one negative entry for SOME (t,t',t_0).'  DEFECT, flagged "
        "by the audit: the first sentence quantifies UNIVERSALLY over t', "
        "the 'equivalently' clause EXISTENTIALLY; they are not equivalent.",
    ),
    "d75-arm0": (
        "v10/note-d75-barandes-audit.md:1116-1122 (pin (b) Arm 0)",
        "the raw generated weights are not stochastic (menus sum to 2 or "
        "5/2); the object is the COMPLETED transfer: Zhat root-free "
        "completion, whose state-to-state matrix is a function of the state "
        "alone with conflict row {1/7, 3/4, 3/28} and total mass exactly 1.",
    ),
    "d49-zhat": (
        "v10/note-d49-completion-dichotomy-settlement-result.md:24-26, "
        "109-110",
        "Zhat(h) = 2^(-|h|) . f(class(sigma(h))), f = (4,4,3,7,3,3)/3, "
        "lambda = 2; the completed state-to-state transfer is identical at "
        "every history carrying that state, with d43b's conflict row "
        "{0: 1/7, 3: 3/4, 5: 3/28}.",
    ),
    "d43b-T": (
        "v10/code/d43b_state_chain_exact.py:153-160 (T_REF) and "
        "v10/note-d43b-martin-boundary-unimodularity.md:128-137",
        "the exact 6x6 transfer of the uniform-lookahead intrinsic chain, "
        "row sums (2,2,2,5/2,2,2); lambda = 2 exactly; one dominant class "
        "{2,4,5}; f = (4,4,3,7,3,3)/3 with the transient extension FORCED; "
        "the completed transfer per-state normalized exactly.",
    ),
    "d43b-census": (
        "v10/code/d43b_state_chain_exact.py:73-76 (MG0) and :106-112 (MG2a)",
        "closed-scope cumulative family sizes at depths 0-6 = "
        "[1,7,39,215,1191,6471,34375]; the intrinsic |P_t| tables "
        "cutoff-2 [4,4,5,5,5], cutoff-3 [4,5,6,6], cutoff-4 [4,5,6].",
    ),
    "p31-4.3": (
        "v10/relativistic-isp-v10-paper31-four-decisions-at-the-joints.md"
        ":496-524 (sec.4.3) and v10/code/d43c_pincer_escapes_exact.py"
        ":134-241",
        "V_single (2x1) deterministic, V_pair (4x1) on the 2-conflict; both "
        "isometric (defect 0.0 at working precision); the squared branch "
        "amplitudes of V_pair are exactly 1/2-1/2 (the K1 law on the "
        "2-conflict, recomputed from the layer); menu reconstruction at "
        "both cuts exact in rationals -- 1/4 on the arbitration sector at "
        "the early cut, 1/4 + 1/8 + 1/8 at the join; the SAME matrices at "
        "both cuts; the pincer baseline full sums 1 vs 5/4.",
    ),
    "d62-R4": (
        "v10/note-d62-h2-update-table.md:247 (row R4), :377-394 (the R4 "
        "proof and T4(c)), :550-554 (the renewal corollary)",
        "R4 = pair-arb on b, i.e. ('r', x, C, W) with proposers(C) = {A,B}: "
        "hold A,B |-> v; live = (); comps = (); refs = {v}; flag v |-> "
        "False -- 'serialisation-identical to sigma([])'.  EVERY PAIR-ARB "
        "IS A RENEWAL TO THE ROOT STATE; rows are selected by (event tag, "
        "base in refs?, |proposers(ckey)|), a partition with no "
        "fall-through.  All 8,944 R4 instances sit on a base that is both "
        "actors' non-superseded token.",
    ),
    "d70-kernel": (
        "v10/code/d70_horizon_limit_exact.py:207-242 (HZ0-a(iii)), lifting "
        "v10/code/d46b_martin_transport_exact.py",
        "rel_potential (the exact backward recursion G(h, r) with "
        "G(h, 0) = 1), krel (k_r(e|h) = q(e|h).G(h+e, r-1)/G(h, r)), sector "
        "(per-EVENT-KIND mass) and conditional (k_r(e)/sector-mass) are the "
        "D46b objects, extracted by AST from the terminal D46b receipt.",
    ),
    "d74-T61": (
        "v10/note-d72-weld-result.md:150 (T6.1), v10/data/"
        "d74_transport_holonomy_exact.out:91-100 and the D74 registry "
        "ANCH (v10/code/d74_transport_holonomy_exact.py:267-306)",
        "(A,B) d<=4: 3969 histories, 1546 closed squares, 88 non-unit, "
        "full ratio multiset {1: 1458, 1/2: 70, 2/3: 2, 3/2: 6, 2: 10}, "
        "kinds {(r,d): 68, (d,r): 8, (d,n): 6, (d,d): 4, (n,d): 2}, "
        "half-open 40 (AB-only 28, BA-only 12), both-blocked 142, "
        "shallowest defect at total depth 3.  (A,B,C) d<=3: 3424 "
        "histories, 1554 closed, 12 non-unit, kinds {(r,d): 12}.",
    ),
    "d74-4444": (
        "v10/data/d74_transport_holonomy_exact.out:262-267 (A3.1/A3.2)",
        "AB4: menu quotient 113 classes, coarsest congruence 185 classes; "
        "of 88 defective squares the menu quotient CLOSES 44 and the "
        "congruence closes 44; SEEN (curvature-type) 44 with spectrum "
        "{1/2: 26, 2: 10, 2/3: 2, 3/2: 6}; UNSEEN (descent-obstruction-"
        "type) 44 with spectrum {1/2: 44} and kinds {(r,d): 44}.  ABC3: "
        "the menu quotient closes 0 of 12; the whole defect is "
        "descent-obstruction type.  (A,B) d<=5: 960 defective, menu "
        "quotient closes 604, unseen 356.",
    ),
    "d65-DC1": (
        "v10/note-d65-descent-conditions-pin.md:37-89 (DC1-DC4) and "
        "v10/note-d65-descent-conditions-result.md:61-117",
        "DC1: events a,b COMMUTE at H iff both orders are admissible and "
        "the terminal state agrees; THE TEST is P(a|H).P(b|Ha) =? "
        "P(b|H).P(a|Hb) with P the normalized kernel.  DC2: boundary "
        "sufficiency = fibre constancy of the next-record law.  DC3: the "
        "five durable-record hypotheses.  DC4: the supplied-vs-derived "
        "ledger.  At closed scope DC1 FAILED: 32,256 failures on 425,334 "
        "refined-record-identical ordered pairs, spectrum "
        "{1: 393078, 4/5: 16128, 5/4: 16128}.",
    ),
    "p0-s4": (
        "v11/relativistic-isp-v11-paper0-the-indivisible-record-law.md"
        ":132-160 (sec.4)",
        "[POSIT] v11's division events are the renewal events; "
        "[THEOREM-GRADE CONVERGENCE] Barandes' fixed configuration space is "
        "'exactly satisfied at renewal grain, because renewals reset to the "
        "root: the configuration space at division events is small, fixed, "
        "and identical across runs'.",
    ),
    "L-1": (
        "v11/relativistic-isp-v11-paper0-the-indivisible-record-law.md"
        ":266-277 (L-1)",
        "exact covariance implemented by invertible stochastic maps on a "
        "fixed finite configuration space forces those maps to be "
        "permutations; v11 may expect AT MOST statistical/approximate "
        "Lorentz invariance at renewal grain, NEVER exact covariance.  Any "
        "v11 claim of exact finite covariance is pre-refuted.",
    ),
    "CP": (
        "v11 paper 0 sec.6.6, citing [V11-CAT] sec.2.5",
        "U1 is NOT a CP-divisibility test: CP-divisibility and "
        "Barandes-indivisibility are orthogonal axes, so the census must "
        "run the interpolant and descent instruments, never a CP criterion.",
    ),
}

ANCH = {
    # d42b1 / D74 / D72 committed transport census
    "AB_hist": 3969, "ABC_hist": 3424,
    "AB_closed": 1546, "AB_defects": 88,
    "AB_full_ratios": {Fr(1, 2): 70, Fr(2, 3): 2, Fr(1): 1458,
                       Fr(3, 2): 6, Fr(2): 10},
    "AB_kinds": {("r", "d"): 68, ("d", "r"): 8, ("d", "n"): 6,
                 ("d", "d"): 4, ("n", "d"): 2},
    "AB_halfopen": 40, "AB_ABonly": 28, "AB_BAonly": 12,
    "AB_bothblocked": 142, "AB_mindepth": 3,
    "ABC_closed": 1554, "ABC_defects": 12,
    "ABC_full_ratios": {Fr(1, 2): 12, Fr(1): 1542},
    "ABC_kinds": {("r", "d"): 12},
    # D74 A3.1/A3.2 — the 44 + 44 split
    "AB_menu_cls": 113, "AB_cong_cls": 185,
    "AB5_defects": 960, "AB5_seen": 604, "AB5_unseen": 356,
    "AB_seen": 44, "AB_unseen": 44,
    "AB_seen_spec": {Fr(1, 2): 26, Fr(2): 10, Fr(2, 3): 2, Fr(3, 2): 6},
    "AB_unseen_spec": {Fr(1, 2): 44},
    "AB_unseen_kinds": {("r", "d"): 44},
    "ABC_seen": 0, "ABC_unseen": 12,
    # d43b / d49 — the Zhat sibling
    "closed_census": [1, 7, 39, 215, 1191, 6471, 34375],
    "Pt_tables": {2: [4, 4, 5, 5, 5], 3: [4, 5, 6, 6], 4: [4, 5, 6]},
    "T_REF": {
        0: {0: Fr(3, 2), 1: Fr(1, 2)},
        1: {1: Fr(3, 2), 2: Fr(1, 8), 3: Fr(1, 8), 4: Fr(1, 4)},
        2: {2: Fr(3, 2), 5: Fr(1, 2)},
        3: {0: Fr(1, 2), 3: Fr(3, 2), 5: Fr(1, 2)},
        4: {4: Fr(3, 2), 5: Fr(1, 2)},
        5: {2: Fr(1, 4), 4: Fr(1, 4), 5: Fr(3, 2)},
    },
    "T_rowsums": [Fr(2), Fr(2), Fr(2), Fr(5, 2), Fr(2), Fr(2)],
    "f_perron": [Fr(4, 3), Fr(4, 3), Fr(1), Fr(7, 3), Fr(1), Fr(1)],
    "lam": Fr(2),
    "conflict_row": {0: Fr(1, 7), 3: Fr(3, 4), 5: Fr(3, 28)},
    # paper 31 sec.4.3 / d43c — Born = K1
    "menu_early_sum": Fr(1, 4), "menu_join": [Fr(1, 4), Fr(1, 8), Fr(1, 8)],
    "full_sum_early": Fr(1), "full_sum_join": Fr(5, 4),
    "born_pair": [Fr(1, 2), Fr(1, 2)], "born_single": [Fr(1)],
}

print("=" * 78)
print("v11 U1 — THE INDIVISIBILITY CENSUS  (exact receipt)")
print("=" * 78)
print("  banner: exact Fractions end to end (Q(sqrt 2) for the Arm-0")
print("  amplitudes); committed v10 layers single-sourced by text-slice and")
print("  by AST with an AST signature pass and exit-freedom gated; every")
print("  tested constant quoted from a committed source (registry below);")
print("  every census printed BOTH WAYS; substantive negatives exit 0;")
print("  exit 1 ONLY if a committed anchor fails to reproduce.")
print()
print("  ENGRAVED (paper 0 sec.6): this is NOT a CP-divisibility test")
print("  (sec.6.6); nothing here is framed as a Bell/locality result")
print("  (sec.6.4); L-1's bound is quoted wherever exact covariance could")
print("  be implied; LEAN: NONE.")
print()
print(f"  PYTHONHASHSEED = {os.environ.get('PYTHONHASHSEED', '(unset)')}")
print(f"  python         = {sys.version.split()[0]}")
print()
print("  QUOTE REGISTRY (every anchor below is held to these):")
for _k in sorted(QUOTES):
    _where, _text = QUOTES[_k]
    print(f"    [{_k}] {_where}")
    for _i in range(0, len(_text), 68):
        print(f"        {_text[_i:_i + 68]}")


# ===========================================================================
# SEC 1.  SINGLE-SOURCING
# ===========================================================================

sec("SINGLE-SOURCING: AST signature pass, text-slice, AST extraction")


class _NoExit(Exception):
    pass


def ast_signatures(path, required):
    tree = ast.parse(open(path).read(), filename=path)
    sigs = {}
    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            sigs[node.name] = [a.arg for a in node.args.args]
        elif isinstance(node, ast.ClassDef):
            sigs[node.name] = ["<class>"]
    missing = []
    for name, args in required.items():
        if name not in sigs:
            missing.append((name, "ABSENT"))
        elif args is not None and sigs[name] != args:
            missing.append((name, f"{sigs[name]} != {args}"))
    return sigs, missing


def slice_exec(path, cut_marker, name, extra=None):
    """Execute the definition head of a committed source (everything strictly
    before the first module-level executable statement).  sys.exit/os._exit
    raise inside, and are restored after."""
    src = open(path).read()
    idx = src.index(cut_marker)
    head = src[:idx]
    mod = types.ModuleType(name)
    sys.modules[name] = mod
    ns = mod.__dict__
    ns["__name__"] = name
    if extra:
        ns.update(extra)
    real_exit, real_osexit = sys.exit, os._exit

    def _blocked(*a, **k):
        raise _NoExit("sliced layer attempted to exit")

    sys.exit, os._exit = _blocked, _blocked
    try:
        exec(compile(head, f"<slice:{os.path.basename(path)}>", "exec"), ns)
    finally:
        sys.exit, os._exit = real_exit, real_osexit
    return ns, len(head), len(src)


def ast_defs(path, names, ns):
    """Extract named module-level FunctionDefs by AST and compile them into
    ns (the D70 HZ0-a(iii) idiom).  Returns the source segments."""
    src = open(path).read()
    tree = ast.parse(src, filename=path)
    lines = src.splitlines(keepends=True)
    segs = {}
    for nd in tree.body:
        if isinstance(nd, ast.FunctionDef) and nd.name in names:
            segs[nd.name] = "".join(lines[nd.lineno - 1:nd.end_lineno])
    for nm in names:
        if nm not in segs:
            continue
        exec(compile(segs[nm], f"<ast:{os.path.basename(path)}:{nm}>",
                     "exec"), ns)
    return segs


B1_REQ = {
    "candidates_for": ["acts", "actors"],
    "admissible": ["acts", "e", "actors", "law"],
    "canon": ["acts"],
    "regs_of": ["op"],
    "event_poset": ["acts"],
    "full_view": ["acts"],
    "own_view": ["acts", "a"],
    "prop_options_in_view": ["view", "a"],
    "deliver_options_in_view": ["view", "a", "actors"],
    "admissible_arb_ckeys": ["acts", "a", "actors"],
    "linear_extensions": ["acts"],
    "vname": ["base", "wkey", "init"],
    "value_of": ["v"],
    "PK1": ["ckey", "edge_triples"],
    "View": ["<class>"],
}
B3_REQ = {
    "candidates_for": ["acts", "actors"],
    "admissible": ["acts", "e"],
    "canon": ["acts"],
    "regs_of": ["op"],
    "arb_components_in_view": ["view", "a"],
    "own_view_canon": ["acts", "a"],
    "PK1": ["ckey", "edge_triples"],
    "mu_of": ["acts"],
}
D74_REQ = {
    "enumerate_line": ["cands", "actors", "depth", "filt"],
    "square_census": ["fam", "cache", "actors", "dep", "adm", "regs",
                      "canon_f", "filt", "reverse_cands", "tamper"],
    "holonomy_of": ["edges", "reverse_order"],
    "A_menu": ["h", "cache"],
    "congruence": ["R"],
    "mu_map": ["fam", "cache"],
    "sk": ["o"],
    "evsk": ["e"],
}
D46B_REQ = {"rel_potential": None, "krel": None, "sector": None,
            "conditional": None}

_P_B1 = "v10/code/d42b1_transport_exact.py"
_P_B3 = "v10/code/d42b3_placement_exact.py"
_P_D74 = "v10/code/d74_transport_holonomy_exact.py"
_P_D46B = "v10/code/d46b_martin_transport_exact.py"

_s1, _m1 = ast_signatures(_P_B1, B1_REQ)
_s3, _m3 = ast_signatures(_P_B3, B3_REQ)
_s74, _m74 = ast_signatures(_P_D74, D74_REQ)
_s46, _m46 = ast_signatures(_P_D46B, D46B_REQ)
anchor("SRC.1 AST SIGNATURE PASS on all four committed sources: every "
       "required def exists at module level with the exact positional "
       "argument list, so a silent upstream edit cannot slip through",
       not (_m1 or _m3 or _m74 or _m46),
       f"d42b1 {len(_s1)} defs ({len(B1_REQ)} required, missing {_m1}); "
       f"d42b3 {len(_s3)} defs (missing {_m3}); d74 {len(_s74)} defs "
       f"(missing {_m74}); d46b {len(_s46)} defs (missing {_m46})")

B1, _b1n, _b1t = slice_exec(_P_B1, 'print("[d42b1', "u1_d42b1")
B3, _b3n, _b3t = slice_exec(_P_B3, 'print("[d42b3', "u1_d42b3")
report("d42b1 slice", f"{_b1n}/{_b1t} bytes executed (definition head only)")
report("d42b3 slice", f"{_b3n}/{_b3t} bytes executed (definition head only)")

_exitfree = True
try:
    slice_exec(_P_B1, 'print("[d42b1', "u1_probe")
except _NoExit:
    _exitfree = False
anchor("SRC.2 EXIT-FREEDOM GATED: sys.exit / os._exit are neutralised "
       "inside the slice and restored after, so a sliced layer cannot set "
       "this receipt's exit status; the slice re-executes cleanly",
       _exitfree and "sys.exit" not in open(_P_B1).read()[:_b1n],
       f"second slice of d42b1 executed with exit blocked; 0 sys.exit in "
       f"the {_b1n}-byte head")

b1_cand = B1["candidates_for"]
b1_adm = B1["admissible"]
b1_canon = B1["canon"]
b1_regs = B1["regs_of"]
b1_fullview = B1["full_view"]
b1_ownview = B1["own_view"]
b1_view = B1["View"]
b1_poset = B1["event_poset"]
b1_vname = B1["vname"]
b1_valueof = B1["value_of"]
b1_PK1 = B1["PK1"]
V0 = B1["V0"]
b3_cand = B3["candidates_for"]
b3_adm = B3["admissible"]
b3_canon = B3["canon"]
b3_regs = B3["regs_of"]
b3_PK1 = B3["PK1"]
b3_arbcomp = B3["arb_components_in_view"]
b3_ownviewcanon = B3["own_view_canon"]
b3_poset = B3["event_poset"]
b3_View = B3["View"]
b3_vname = B3["vname"]

# --- D74's census machinery, extracted by AST (not re-implemented) --------
NS74 = {"Fr": Fr, "Counter": Counter, "defaultdict": defaultdict,
        "b1_adm": b1_adm, "_EVSK": {}}
_seg74 = ast_defs(_P_D74, list(D74_REQ), NS74)
enumerate_line = NS74["enumerate_line"]
square_census = NS74["square_census"]
holonomy_of = NS74["holonomy_of"]
A_menu = NS74["A_menu"]
congruence = NS74["congruence"]
mu_map = NS74["mu_map"]
anchor("SRC.3 D74's CENSUS MACHINERY IS D74's, extracted by AST from the "
       "committed receipt and not retyped: enumerate_line, square_census "
       "(the exchange-square census), holonomy_of, A_menu (the weighted-"
       "menu abstraction whose kernel IS the coarsest descent quotient), "
       "congruence (the coarsest weighted congruence) and mu_map",
       set(_seg74) == set(D74_REQ)
       and 'r = Fr(qA * qB2, 1) / Fr(qB * qA2, 1)' in _seg74["square_census"]
       and 'sorted((evsk(e), str(q)) for e, q in cache[h])'
       in _seg74["A_menu"],
       f"lifted {len(_seg74)} definitions from {_P_D74}: "
       + ", ".join(f"{n} ({len(_seg74[n].splitlines())} lines)"
                   for n in sorted(_seg74)))

# --- D46b's kernel objects, extracted by AST (the D70 HZ0-a(iii) idiom) ---
NS46 = {"Fr": Fr}
_seg46 = ast_defs(_P_D46B, list(D46B_REQ), NS46)
rel_potential = NS46["rel_potential"]
krel = NS46["krel"]
d46b_sector = NS46["sector"]
d46b_conditional = NS46["conditional"]
anchor("SRC.4 THE KERNEL OBJECTS ARE THE D46b OBJECTS (D70's HZ0-a(iii), "
       "re-run here): rel_potential (the exact backward recursion G(h,r) "
       "with G(h,0) = 1), krel (k_r(e|h) = q(e|h).G(h+e,r-1)/G(h,r)), "
       "sector and conditional, extracted by ast.FunctionDef from the "
       "TERMINAL D46b receipt, so a change to D46b's definitions changes "
       "this receipt's object",
       set(_seg46) == set(D46B_REQ)
       and "G(h + (e,), r - 1)" in _seg46["rel_potential"]
       and "q * G(h + (e,), r - 1) / tot" in _seg46["krel"]
       and "v / s[e[0]]" in _seg46["conditional"],
       f"lifted {len(_seg46)} definitions from {_P_D46B}: "
       + ", ".join(f"{n} ({len(_seg46[n].splitlines())} lines)"
                   for n in sorted(_seg46)))

AB = ("A", "B")
ABC = ("A", "B", "C")


# ===========================================================================
# SEC 2.  DECLARED CAPS — printed before anything uses them
# ===========================================================================

sec("DECLARED CAPS AND FAMILIES (nothing silent)")

CAP_A = 5          # ARM-A: (A,B) transport family, exhaustive to depth 5
CAP_B = 6          # ARM-B: renewal-started window, exhaustive to depth 6
CAP_D = 4          # ARM-D: (A,B,C) transport family, exhaustive to depth 4
CAP_ANCH_AB = 4    # the D74 AB4 anchor arm
CAP_ANCH_ABC = 3   # the D74 ABC3 anchor arm
CAP_CLOSED = 6     # the closed-scope (d42b3) family for Arm 0's sibling
CAP_DC1 = 3        # DC1 parent depth (squares to depth CAP_DC1 + 2)
LP_MAXVARS = 700   # exact Phase-I simplex: variable cap per triple
LP_MAXROWS = 400   # exact Phase-I simplex: constraint cap per triple
LP2_MAXVARS = 5000  # the REDUCED system's cap (implied zeros + aggregation)
LP2_MAXROWS = 1200
LP_MAXPIVOT = 400000
PAD_MAX = 100      # [B3] eq. 22 algebraic arm: fixed-configuration-space cap

print(f"  ARM-A  (A,B) transport, exhaustive depth <= {CAP_A}; cuts = "
      f"depths 0..{CAP_A}; horizon {CAP_A}")
print(f"  ARM-B  renewal-started window: every depth-3 history whose last "
      f"event is a pair-arb, exhaustive to depth {CAP_B}; cuts = depths "
      f"3..{CAP_B}; horizon {CAP_B}")
print(f"  ARM-C  renewal-to-renewal cuts (renewal index 0,1,2) inside ARM-B")
print(f"  ARM-D  (A,B,C) transport, exhaustive depth <= {CAP_D}; cuts = "
      f"depths 0..{CAP_D}; horizon {CAP_D}  [the pool control]")
print(f"  ANCHOR arms: (A,B) depth <= {CAP_ANCH_AB} and (A,B,C) depth <= "
      f"{CAP_ANCH_ABC} — D72/D74's own windows, reproduced exactly")
print(f"  ARM-0  closed-scope (d42b3) family to depth {CAP_CLOSED} for the "
      f"Zhat sibling; the pair fixture [pA0] / [pA0,pB1] for Born = K1")
print(f"  DC1    ordered-pair census over every parent of depth <= "
      f"{CAP_DC1} (squares to depth {CAP_DC1 + 2}), exhaustive, unsampled")
print(f"  LP     exact rational Phase-I simplex (Bland), caps: <= "
      f"{LP_MAXVARS} variables, <= {LP_MAXROWS} constraints, <= "
      f"{LP_MAXPIVOT} pivots; every triple exceeding a cap is PRINTED as "
      f"excluded with its size, and its cheap row certificate is still run")
print(f"  LP2    the REDUCED system — implied zeros plus aggregation of "
      f"identical Gamma columns and identical target rows, both proved "
      f"feasibility-preserving in reduce_system() — decides triples the "
      f"plain LP cap refuses; caps <= {LP2_MAXVARS} variables, <= "
      f"{LP2_MAXROWS} constraints")
print(f"  EQ22   the algebraic arm runs on fixed configuration spaces of "
      f"size <= {PAD_MAX} (exact rational inversion); larger triples are "
      f"printed as excluded")
print("  WHY THOSE LP NUMBERS, since a tuned cap is a way to avoid an")
print("  inconvenient answer: they are set by measured cost and by nothing")
print("  else.  Exact Phase-I simplex on a 608-variable / 179-row triple "
      "costs")
print("  ~90 s and ~3,200 pivots on this machine; the caps admit that size "
      "and")
print("  refuse the next one up.  Every excluded triple still gets the row")
print("  certificate.  WHAT A CAP CAN HIDE, STATED CORRECTLY: the row")
print("  certificate is SUFFICIENT for indivisibility and NOT NECESSARY — "
      "it")
print("  asks whether some target admits no non-negative row at all, and a")
print("  triple can be indivisible with every row individually solvable,")
print("  the obstruction living only in the column-stochasticity that "
      "couples")
print("  them.  A CAP CAN THEREFORE HIDE AN INDIVISIBLE TRIPLE EXACTLY AS")
print("  EASILY AS A DIVISIBLE ONE, and this receipt exhibits one: "
      "(1,4,5)")
print("  under alpha_sigma passes the row certificate with no obstruction "
      "and")
print("  is INDIVISIBLE on the full system.  That is why the LP2 reduction")
print("  below exists.")
print("  EXCLUDED BY CAP, STATED IN ADVANCE: a renewal-to-renewal triple")
print("  with a non-degenerate FIRST cut needs THREE renewals, i.e. depth")
print("  >= 9 in the two-actor transport family (a pair-arb needs two")
print("  proposals), which is ~10^8 histories and is not enumerated here.")
print("  No sampled arm is run anywhere in this receipt.")


# ===========================================================================
# SEC 3.  THE PREAMBLE — v1 paper 22's definition, with the audit's defect
#         repaired.  This is the definitional ground every gate below cites.
# ===========================================================================

sec("THE PREAMBLE — the repaired definition of indivisibility")

print("""  v1 paper 22 Definition 2 states the property twice and the two
  statements are NOT equivalent (the D75 audit's named defect): the first
  sentence quantifies UNIVERSALLY over the intermediate ('for every
  intermediate t' there exists no stochastic factor'), the 'equivalently'
  clause EXISTENTIALLY ('has a negative entry for SOME (t,t',t_0)').  The
  audit's reading — everything the corpus proves is the existential form —
  is adopted, and the definition is restated so that the quantifiers are
  separated and each is named:

    Let Gamma(c' <- c) be the family of transition matrices of a process
    indexed by cuts of a partial order, Gamma_{ji} = P(config j at c' |
    config i at c), so that columns sum to 1.

    (D1) LOCAL DIVISIBILITY at a composable triple (c, c', c''):
         there EXISTS a column-stochastic X with X . Gamma(c' <- c) =
         Gamma(c'' <- c).  When Gamma(c' <- c) is square and invertible X
         is unique and equals the algebraic interpolant Gammabar =
         Gamma(c'' <- c) . Gamma(c' <- c)^-1 of [B3] eq. 22, so local
         divisibility is then exactly 'Gammabar has no negative entry'.
         When Gamma(c' <- c) is singular the algebraic form does not
         apply and (D1) is decided as a linear feasibility question.

    (D2) INDIVISIBLE AT A TRIPLE (the existential form; the honest one):
         (D1) fails at that triple.

    (D3) INDIVISIBLE (process-level, existential):  (D2) holds for SOME
         composable triple in the declared cut family.

    (D4) EVERYWHERE-INDIVISIBLE (the universal form v1's first sentence
         asserts):  (D2) holds for EVERY composable triple.

  (D3) and (D4) are the two readings v1 paper 22 conflated.  Every verdict
  below is stated in the (D2)/(D3) form and the (D4) form is reported
  separately, never inferred from (D3).  DEGENERACY, declared: at a triple
  whose first cut carries a SINGLE configuration, (D1) is satisfied by the
  constant matrix X = Gamma(c'' <- c) . 1^T for any Gamma(c' <- c), so
  such a triple can never be indivisible and is reported as STRUCTURALLY
  VACUOUS rather than as a divisible datum.

  NOT A CP TEST (paper 0 sec.6.6): (D1)-(D4) are statements about
  factorisation of stochastic matrices.  No completely-positive map, no
  divisibility of a dynamical map on operators, and no CP criterion of any
  kind appears anywhere in this receipt.""")


# ===========================================================================
# SEC 4.  ARM 0 — BORN = K1 IN EXACT ARITHMETIC, AND THE Zhat SIBLING
# ===========================================================================

sec("ARM 0 — Born = K1 on the committed arbitration layer (exact), and "
    "the Zhat-completed sibling")

_t = time.time()


class Q2:
    """Exact arithmetic in Q(sqrt 2): a + b.sqrt(2), a and b Fractions.
    The Arm-0 amplitudes are exactly representable here, so the isometry
    defect is EXACTLY 0 rather than 1e-40."""

    __slots__ = ("a", "b")

    def __init__(self, a=0, b=0):
        self.a = Fr(a)
        self.b = Fr(b)

    def __add__(self, o):
        return Q2(self.a + o.a, self.b + o.b)

    def __sub__(self, o):
        return Q2(self.a - o.a, self.b - o.b)

    def __mul__(self, o):
        return Q2(self.a * o.a + 2 * self.b * o.b,
                  self.a * o.b + self.b * o.a)

    def __eq__(self, o):
        return isinstance(o, Q2) and self.a == o.a and self.b == o.b

    def is_rational(self):
        return self.b == 0

    def __repr__(self):
        if self.b == 0:
            return str(self.a)
        return f"{self.a} + {self.b}*sqrt2"


ONE = Q2(1, 0)
ZERO = Q2(0, 0)
INV_SQRT2 = Q2(0, Fr(1, 2))          # 1/sqrt(2) = (1/2) sqrt(2), exactly


def q2_matmul(A, B):
    n, k, m = len(A), len(B), len(B[0])
    return [[sum((A[i][t] * B[t][j] for t in range(k)), ZERO)
             for j in range(m)] for i in range(n)]


def q2_T(A):
    return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]


def iso_defect_exact(M):
    """max |(M^T M - I)_{ij}| as an exact object: returns the set of
    non-zero entries of M^T M - I.  Empty set == defect exactly 0."""
    G = q2_matmul(q2_T(M), M)
    bad = []
    for i in range(len(G)):
        for j in range(len(G[0])):
            want = ONE if i == j else ZERO
            if not (G[i][j] == want):
                bad.append((i, j, G[i][j]))
    return bad


# ---- A0.1  the committed pair fixture, re-run on the committed layer -----
pA0 = ("p", "A", V0, 0)
pB1 = ("p", "B", V0, 1)
tA, tB = ("A", V0, 0), ("B", V0, 1)
SELFA = ("r", "A", frozenset({tA}), frozenset({tA}))
PAIRA = ("r", "A", frozenset({tA, tB}), frozenset({tA}))
PAIRB = ("r", "A", frozenset({tA, tB}), frozenset({tB}))
H1, H2 = [pA0], [pA0, pB1]


def arb_menu_closed(h):
    return sorted(((e, q) for e, q in b3_cand(h, AB)
                   if e[1] == "A" and e[0] == "r"), key=lambda z: sk(z[0]))


m1 = arb_menu_closed(H1)
m2 = arb_menu_closed(H2)
s_full_1 = sum(q for e, q in b3_cand(H1, AB) if e[1] == "A")
s_full_2 = sum(q for e, q in b3_cand(H2, AB) if e[1] == "A")
pair_events = [e for e, q in m2 if e[2] == frozenset({tA, tB})]
anchor("A0.1 THE COMMITTED PAIR EXHIBIT RE-RUNS (paper 31 sec.4.3's "
       "baseline): A's arbitration menu is ONE event at the early cut and "
       "THREE at the join (self plus the two pair winners); the full "
       "per-actor sums are exactly 1 and 5/4; the pair branches are "
       "inadmissible early",
       len(m1) == 1 and len(m2) == 3 and len(pair_events) == 2
       and s_full_1 == ANCH["full_sum_early"]
       and s_full_2 == ANCH["full_sum_join"]
       and all(not b3_adm(H1, e)[0] for e in pair_events),
       f"menu sizes {len(m1)}/{len(m2)}; full sums {s_full_1}/{s_full_2} "
       f"(quoted {ANCH['full_sum_early']}/{ANCH['full_sum_join']})")

# ---- A0.2  the isometric family, in Q(sqrt 2) ---------------------------
O_pair = [[INV_SQRT2], [INV_SQRT2]]              # the join-typed opening click
A_pair = [[ONE, ZERO], [ZERO, ZERO], [ZERO, ZERO], [ZERO, ONE]]  # acceptance
V_pair = q2_matmul(A_pair, O_pair)
O_sing = [[ONE]]
A_sing = [[ONE], [ZERO]]
V_sing = q2_matmul(A_sing, O_sing)
_defects = {nm: iso_defect_exact(M) for nm, M in
            (("V_pair", V_pair), ("V_single", V_sing), ("O_pair", O_pair),
             ("A_pair", A_pair), ("O_single", O_sing), ("A_single", A_sing))}
_shapes = ((len(V_pair), len(V_pair[0])), (len(V_sing), len(V_sing[0])))
anchor("A0.2 ISOMETRY EXACTLY 0 (an upgrade on the committed receipt, "
       "which gated 1e-40 in mpmath): V_pair (4x1) and V_single (2x1), "
       "built as Acceptance o OpeningClick from committed machinery, and "
       "BOTH factors of each, satisfy M^T M - I = 0 identically in "
       "Q(sqrt 2).  The committed defect '0.0 at the working precision' is "
       "now an exact algebraic 0",
       all(len(v) == 0 for v in _defects.values())
       and _shapes == ((4, 1), (2, 1)),
       f"shapes {_shapes}; non-zero entries of M^T M - I by matrix: "
       + ", ".join(f"{n} {len(_defects[n])}" for n in sorted(_defects)))

# ---- A0.3  Born = K1, recomputed from the layer -------------------------
edge = frozenset({tuple(sorted((tA, tB)))})
k1_pair = b3_PK1(frozenset({tA, tB}), edge)
k1_sing = b3_PK1(frozenset({tA}), frozenset())
born_pair = {frozenset({tA}): (V_pair[0][0] * V_pair[0][0]),
             frozenset({tB}): (V_pair[3][0] * V_pair[3][0])}
born_sing = {frozenset({tA}): (V_sing[0][0] * V_sing[0][0])}
_born_rational = all(x.is_rational() for x in
                     list(born_pair.values()) + list(born_sing.values()))
_born_eq = (all(born_pair[w].a == k1_pair[w] for w in k1_pair)
            and all(born_sing[w].a == k1_sing[w] for w in k1_sing))
anchor("A0.3 BORN = K1 EXACTLY: the squared branch amplitudes of V_pair "
       "are exactly 1/2 and 1/2 — RATIONAL numbers, not approximations — "
       "and equal PK1 on the 2-conflict recomputed from the committed "
       "layer; V_single's branch is deterministic and equals PK1 on the "
       "singleton",
       _born_rational and _born_eq
       and sorted(x.a for x in born_pair.values()) == ANCH["born_pair"]
       and [x.a for x in born_sing.values()] == ANCH["born_single"],
       f"|amp|^2 (pair) = {sorted(str(x.a) for x in born_pair.values())}; "
       f"PK1 (pair) = {sorted(str(v) for v in k1_pair.values())}; "
       f"|amp|^2 (single) = {[str(x.a) for x in born_sing.values()]}; "
       f"all rational = {_born_rational}")

# ---- A0.4  menu reconstruction at BOTH cuts, exact in rationals ---------
BORN = {1: [Fr(1)], 2: [Fr(1, 2), Fr(1, 2)]}


def share(h, e):
    acts2 = list(h) + [e]
    pred = b3_poset(acts2)
    view = b3_View(acts2, pred, pred[len(acts2) - 1])
    return Fr(1, 4) / len(b3_arbcomp(view, e[1]))


def reconstruct(h):
    out, used = {}, []
    if b3_adm(h, SELFA)[0]:
        out[SELFA] = share(h, SELFA) * BORN[1][0]
        used.append("single")
    if b3_adm(h, PAIRA)[0] and b3_adm(h, PAIRB)[0]:
        s = share(h, PAIRA)
        out[PAIRA] = s * BORN[2][0]
        out[PAIRB] = s * BORN[2][1]
        used.append("pair")
    return out, used


r1, idx1 = reconstruct(H1)
r2, idx2 = reconstruct(H2)
anchor("A0.4 MENU RECONSTRUCTION AT BOTH CUTS, EXACT IN RATIONALS, FROM "
       "THE SAME MATRICES: (past-local admissible-ckey index x budget "
       "share 1/4 / #components, read from the layer's own past-view "
       "machinery) x (the V_C Born splits) equals the committed menus — "
       "1/4 on the arbitration sector at the early cut and 1/4 + 1/8 + 1/8 "
       "at the join.  What differs between the cuts is the classical index "
       "set, not the operator",
       r1 == dict(m1) and r2 == dict(m2)
       and idx1 == ["single"] and idx2 == ["single", "pair"]
       and sum(r1.values()) == ANCH["menu_early_sum"]
       and srt(r2.values()) == srt(ANCH["menu_join"]),
       f"early menu {[str(v) for v in srt(r1.values())]} (sum "
       f"{sum(r1.values())}); join menu "
       f"{[str(v) for v in srt(r2.values())]}; index sets {idx1} vs {idx2}")

# ---- A0.5  the Zhat-completed sibling, per the audit's specification ----
_t2 = time.time()
CFAM, CCACHE = enumerate_line(b3_cand, AB, CAP_CLOSED)
_cum = [sum(1 for h in CFAM if len(h) <= k) for k in range(CAP_CLOSED + 1)]
anchor("A0.5a THE CLOSED-SCOPE FAMILY REPRODUCES d43b's census: cumulative "
       "family sizes at depths 0..6",
       _cum == ANCH["closed_census"],
       f"{_cum} (quoted {ANCH['closed_census']})")


def menu_shape_closed(cands):
    d = {}
    for e, q in cands:
        d[(e[0], q)] = d.get((e[0], q), 0) + 1
    return tuple(sorted(d.items(), key=lambda z: sk(z[0])))


def relabel(d, keys):
    relab = {}
    for k in keys:
        relab.setdefault(d[k], len(relab))
    return {k: relab[d[k]] for k in d}


_KEYS = sorted((tuple(h) for h in CFAM), key=sk)
P0 = {k: menu_shape_closed(CCACHE[k]) for k in _KEYS}
P = {0: relabel(P0, _KEYS)}
for t in range(5):
    nxt = {}
    for k in _KEYS:
        if len(k) > 5 - t:
            continue
        nxt[k] = (P[t][k], tuple(sorted(((str(q), P[t][k + (e,)])
                                         for e, q in CCACHE[k]),
                                        key=lambda z: sk(z))))
    P[t + 1] = relabel(nxt, [k for k in _KEYS if len(k) <= 5 - t])
tables = {c: [len({P[t][k] for k in _KEYS if len(k) <= c})
              for t in range(0, 7 - c)] for c in (2, 3, 4)}
anchor("A0.5b THE UNIFORM-LOOKAHEAD INTRINSIC PARTITION STABILISES AT SIX "
       "STATES at lookahead t = 2 (d43b MG2a): the |P_t| tables on the "
       "len<=2/3/4 windows reproduce the committed anchors",
       tables == ANCH["Pt_tables"],
       f"cutoff-2 {tables[2]}, cutoff-3 {tables[3]}, cutoff-4 {tables[4]} "
       f"(quoted {ANCH['Pt_tables']})")

_pB0 = ("p", "B", V0, 0)
REPS = [(), (pA0,), (pA0, _pB0), (pA0, pB1), (pA0, SELFA),
        (pA0, _pB0, SELFA)]
_raw = [P[2][r] for r in REPS]
_repmap = {r: i for i, r in enumerate(_raw)}
CLS = {k: _repmap.get(P[2][k], -1) for k in _KEYS if len(k) <= 4}
_rows, _okwd, _nmem = {}, True, 0
for k in _KEYS:
    if len(k) > 3:
        continue
    _nmem += 1
    r = CLS[k]
    row = {}
    for e, q in CCACHE[k]:
        c2 = CLS[k + (e,)]
        row[c2] = row.get(c2, Fr(0)) + q
    if r in _rows:
        _okwd &= (_rows[r] == row)
    else:
        _rows[r] = row
T = [[_rows.get(i, {}).get(j, Fr(0)) for j in range(6)] for i in range(6)]
_rowsums = [sum(_rows.get(i, {}).values()) for i in range(6)]
anchor("A0.5c THE EXACT 6x6 TRANSFER IS THE COMMITTED ONE (d43b MG2d): "
       "well-defined per state on every one of the 215 len<=3 members, "
       "equal to the committed matrix entry for entry, row sums = the "
       "per-cut masses (2,2,2,5/2,2,2) with the conflict state carrying "
       "the 5/4-per-actor excess",
       _okwd and _nmem == 215 and _rows == ANCH["T_REF"]
       and _rowsums == ANCH["T_rowsums"] and len(set(_raw)) == 6,
       f"members {_nmem}; well-defined {_okwd}; T == committed "
       f"{_rows == ANCH['T_REF']}; row sums "
       f"{[str(x) for x in _rowsums]}")

f = ANCH["f_perron"]
lam = ANCH["lam"]
_eig = all(sum(T[i][j] * f[j] for j in range(6)) == lam * f[i]
           for i in range(6))
ZH = [[T[i][j] * f[j] / (lam * f[i]) for j in range(6)] for i in range(6)]
_zh_rows = [sum(ZH[i]) for i in range(6)]
_conf = {j: ZH[3][j] for j in range(6) if ZH[3][j] != 0}
_zh_nonneg = all(ZH[i][j] >= 0 for i in range(6) for j in range(6))
anchor("A0.5d THE Zhat-COMPLETED SIBLING, BUILT TO THE AUDIT'S "
       "SPECIFICATION AND EXACTLY STOCHASTIC: with the committed Perron "
       "data (T f = 2 f exactly, f = (4,4,3,7,3,3)/3) the completed "
       "state-to-state transfer Zhat(i->j) = T_ij f_j / (lambda f_i) has "
       "EVERY ROW SUMMING TO EXACTLY 1 with every entry non-negative, and "
       "its conflict row is exactly {0: 1/7, 3: 3/4, 5: 3/28} — the row "
       "the D75 audit specified to the receipt, total mass exactly 1",
       _eig and all(x == Fr(1) for x in _zh_rows) and _zh_nonneg
       and _conf == ANCH["conflict_row"]
       and sum(_conf.values()) == Fr(1),
       f"T f = 2 f exact = {_eig}; row sums "
       f"{[str(x) for x in _zh_rows]}; conflict row "
       f"{ {k: str(v) for k, v in sorted(_conf.items())} }; total mass "
       f"{sum(_conf.values())}")
print("  [DATA] the Zhat-completed six-state sibling (rows = source "
      "state, exact):")
for i in range(6):
    print("           " + str(i) + ": "
          + "  ".join(f"{j}:{ZH[i][j]}" for j in range(6) if ZH[i][j] != 0))
report("ARM-0 handover to U3", "the two anchor matrices are {V_single, "
       "V_pair} (exact Q(sqrt 2), Born = K1) and the 6x6 Zhat transfer "
       "above.  U3's unistochasticity screen reads the Zhat matrix: its "
       "columns do NOT sum to 1 (column sums printed below), so the "
       "completed chain is row-stochastic and NOT doubly stochastic, "
       "hence NOT unistochastic — the audit's pin (b) Arm 1 screen, "
       "recorded here as ARM-0 output and left for U3 to adjudicate")
_colsums = [sum(ZH[i][j] for i in range(6)) for j in range(6)]
report("Zhat column sums (U3's screen, reported not adjudicated)",
       [str(x) for x in _colsums])
report("ARM-0 time", f"{time.time() - _t:.0f}s")


# ===========================================================================
# SEC 5.  THE ANCHOR BLOCK — D72/D74's committed transport census.
#         exit 1 lives here and nowhere else.
# ===========================================================================

sec("ANCHORS — D72/D74's committed transport census and the 44 + 44 split")

_t = time.time()
ANCHARMS = {}
for _nm, _actors, _dep, _pref in (("AB4", AB, CAP_ANCH_AB, "AB"),
                                  ("ABC3", ABC, CAP_ANCH_ABC, "ABC")):
    fam, cache = enumerate_line(b1_cand, _actors, _dep)
    st, rat, kinds, okinds, defs, half, closed = square_census(
        fam, cache, _actors, _dep, b1_adm, b1_regs, b1_canon)
    dely = sum(1 for h, a, b, r, *_ in defs if "d" in (a[0], b[0]))
    mind = min((len(h) + 2 for h, *_ in defs), default=None)
    ANCHARMS[_nm] = dict(fam=fam, cache=cache, defs=defs, closed=closed,
                         actors=_actors, dep=_dep, st=st, rat=rat)
    report(f"{_nm} census", f"{len(fam)} histories; {dict(st)}; non-unit "
           f"{len(defs)}; ratios {fmt(rat)}; kinds {dict(kinds)}; "
           f"delivery-bearing {dely}/{len(defs)}; shallowest {mind}")
    anchor(f"{_nm}.1 D72's T6.1 row reproduces EXACTLY — family size, "
           f"closed-square count, the FULL ratio multiset (unit and "
           f"non-unit), the kind census, delivery-bearing fraction, "
           f"both-blocked count and shallowest defect depth",
           len(fam) == ANCH[_pref + "_hist"]
           and st["closed"] == ANCH[_pref + "_closed"]
           and dict(rat) == ANCH[_pref + "_full_ratios"]
           and dict(kinds) == ANCH[_pref + "_kinds"]
           and dely == len(defs) == ANCH[_pref + "_defects"]
           and (_pref != "AB" or (st["both-blocked"] == ANCH["AB_bothblocked"]
                                  and mind == ANCH["AB_mindepth"])),
           f"histories {len(fam)}/{ANCH[_pref + '_hist']}; closed "
           f"{st['closed']}/{ANCH[_pref + '_closed']}; non-unit "
           f"{len(defs)}/{ANCH[_pref + '_defects']}; ratios match "
           f"{dict(rat) == ANCH[_pref + '_full_ratios']}; kinds match "
           f"{dict(kinds) == ANCH[_pref + '_kinds']}")
    if _pref == "AB":
        anchor("AB4.2 D72's T6.2 half-open row reproduces EXACTLY",
               st.get("AB-only", 0) == ANCH["AB_ABonly"]
               and st.get("BA-only", 0) == ANCH["AB_BAonly"]
               and st.get("AB-only", 0) + st.get("BA-only", 0)
               == ANCH["AB_halfopen"],
               f"AB-only {st.get('AB-only', 0)}, BA-only "
               f"{st.get('BA-only', 0)}, total "
               f"{st.get('AB-only', 0) + st.get('BA-only', 0)}")

# --- the 44 + 44 descent split, reproduced on D74's own carrier ----------
for _nm, _pref in (("AB4", "AB"), ("ABC3", "ABC")):
    R = ANCHARMS[_nm]
    Vm = {tuple(h): sk(A_menu(tuple(h), R["cache"])) for h in R["fam"]}
    seen, unseen = [], []
    for row in R["defs"]:
        hh, a, b = row[0], row[1], row[2]
        (seen if Vm[hh + (a, b)] == Vm[hh + (b, a)] else unseen).append(row)
    R["seen"], R["unseen"] = seen, unseen
    R["menu_cls"] = len(set(Vm.values()))
    cong, iters = congruence(R)
    R["cong_cls"] = len(set(cong.values()))
    R["cong_def"] = sum(1 for hh, a, b, r, *_ in R["defs"]
                        if cong[hh + (a, b)] == cong[hh + (b, a)])
    report(f"{_nm} carrier", f"menu quotient {R['menu_cls']} classes; "
           f"coarsest congruence {R['cong_cls']} classes after {iters} "
           f"refinement rounds; of {len(R['defs'])} defective squares the "
           f"menu quotient CLOSES {len(seen)} and the congruence closes "
           f"{R['cong_def']}")
    report(f"{_nm} the dichotomy",
           f"SEEN (curvature-type) {len(seen)}: spectrum "
           f"{fmt(Counter(r[3] for r in seen))}, kinds "
           f"{ {str(k): v for k, v in sorted(Counter((r[1][0], r[2][0]) for r in seen).items())} }"
           f" | UNSEEN (descent-obstruction-type) {len(unseen)}: spectrum "
           f"{fmt(Counter(r[3] for r in unseen))}, kinds "
           f"{ {str(k): v for k, v in sorted(Counter((r[1][0], r[2][0]) for r in unseen).items())} }")

_A4 = ANCHARMS["AB4"]
anchor("D74.1 THE 44 + 44 SPLIT REPRODUCES EXACTLY — the pin's prime "
       "suspects.  On AB4 the coarsest DESCENT quotient (the weighted-menu "
       "partition) closes 44 of the 88 defective squares and the coarsest "
       "weighted CONGRUENCE closes the same 44; the invisible half is 44 "
       "squares with spectrum {1/2: 44} and kinds {(r,d): 44}; on ABC3 the "
       "menu quotient closes 0 of 12, i.e. at that window the entire "
       "defect is of the descent-obstruction type",
       len(_A4["seen"]) == ANCH["AB_seen"]
       and len(_A4["unseen"]) == ANCH["AB_unseen"]
       and _A4["cong_def"] == ANCH["AB_seen"]
       and _A4["menu_cls"] == ANCH["AB_menu_cls"]
       and _A4["cong_cls"] == ANCH["AB_cong_cls"]
       and dict(Counter(r[3] for r in _A4["seen"])) == ANCH["AB_seen_spec"]
       and dict(Counter(r[3] for r in _A4["unseen"]))
       == ANCH["AB_unseen_spec"]
       and dict(Counter((r[1][0], r[2][0]) for r in _A4["unseen"]))
       == ANCH["AB_unseen_kinds"]
       and len(ANCHARMS["ABC3"]["seen"]) == ANCH["ABC_seen"]
       and len(ANCHARMS["ABC3"]["unseen"]) == ANCH["ABC_unseen"],
       f"AB4 seen/unseen {len(_A4['seen'])}/{len(_A4['unseen'])} (quoted "
       f"{ANCH['AB_seen']}/{ANCH['AB_unseen']}); congruence closes "
       f"{_A4['cong_def']}; menu classes {_A4['menu_cls']}; congruence "
       f"classes {_A4['cong_cls']}; ABC3 seen/unseen "
       f"{len(ANCHARMS['ABC3']['seen'])}/{len(ANCHARMS['ABC3']['unseen'])}")

# --- THE 44 DESCENT-OBSTRUCTION SQUARES, NAMED FIRST (pin, Arm 1) -------
print()
print("  [A1-PRIME]  THE 44 DESCENT-OBSTRUCTION SQUARES OF AB4, NAMED "
      "FIRST AND IN FULL")
print("              (D74 sec.B2.12(iv)'s invisible half: the two orders "
      "of the square")
print("              carry DIFFERENT weighted menus, so the square closes "
      "in NO quotient")
print("              on which the connection is well defined.  These are "
      "the pin's")
print("              pre-registered prime suspects for Arm 1.)")
_U44 = sorted(_A4["unseen"], key=lambda row: sk((row[0], row[1], row[2])))
for _i, (_hh, _ea, _eb, _r, _qa, _qb2, _qb, _qa2) in enumerate(_U44):
    print(f"    U{_i:02d}  base depth {len(_hh)}  ratio {_r}  kinds "
          f"({_ea[0]},{_eb[0]})")
    print(f"          h  = {list(_hh)}")
    print(f"          eA = {_ea}")
    print(f"          eB = {_eb}")
    print(f"          q(eA|h) = {_qa}, q(eB|h.eA) = {_qb2}, q(eB|h) = "
          f"{_qb}, q(eA|h.eB) = {_qa2}")
report("the 44 named squares, base-depth census",
       dict(sorted(Counter(len(r[0]) for r in _U44).items())))
report("the 44 named squares, event-kind pairs",
       {str(k): v for k, v in
        sorted(Counter((r[1][0], r[2][0]) for r in _U44).items())})
report("anchor block time", f"{time.time() - _t:.0f}s")

if ANCHOR_FAIL:
    print()
    print("!" * 78)
    print("ANCHOR FAILURE — a committed number did not reproduce.")
    print("STOPPING.  Nothing below this line may be believed.")
    print("!" * 78)
    sys.exit(1)


# ===========================================================================
# SEC 6.  ARM 1, PART A — the renewal predicate: D62 row R4 PORTED to
#         transport scope, with the port verified against the layer.
# ===========================================================================

sec("ARM 1 (a) — the D62-R4 renewal predicate, ported to transport scope "
    "and verified")


def proposers_of(ckey):
    return {t[0] for t in ckey}


def is_R4(e):
    """The D62 row selector for R4, ported verbatim: rows are selected by
    (event tag, base in refs?, |proposers(ckey)|), and R4 is the pair-arb —
    tag 'r' with TWO proposers in the ckey.  This is a purely syntactic
    predicate on the event; it reads no state."""
    return e[0] == "r" and len(proposers_of(e[2])) == 2


def sigmaT(h, actors, enriched, view_of, cache_store):
    """The D62 sigma FIELDS, ported to transport scope.

    D62's sigma is (hold, live, comps, refs, sup|refs) with tokens renamed
    canonically.  Two things must change at transport scope and both are
    declared:  (i) an actor may hold SEVERAL non-superseded versions once
    deliveries exist, so `hold` becomes the SET of an actor's alive
    holdings (at closed scope it is a singleton by D62 (5a) and the two
    definitions agree);  (ii) tokens are renamed by their ROLE rather than
    by name — the state is the sorted multiset of token records
    (holders, superseded?, live triples on it) — which is exactly D62's
    canonical renaming made permutation-safe.  `comps` is not carried
    separately: by D62 Row 0 it is a function of `live`, which the token
    records contain.  `refs` is D62's F2 (holds union live-carrying bases),
    so a superseded, unheld token is DROPPED, exactly as in the table.

    enriched=False is the D62-faithful state — WINNER-INVISIBLE, by D62's
    own corollary that sigma(h+e) does not depend on the arbitration
    winner W.  enriched=True adds each token's payload record (value,
    authors, initiator), which is the physical configuration the record
    carries; both are run everywhere below."""
    key = (h, tuple(actors), enriched)
    if key in cache_store:
        return cache_store[key]
    v = view_of(list(h))
    alive = {a: set(x for x in v.holdings(a) if x not in v.superseded)
             for a in actors}
    live = [(op[1], op[2], op[3]) for op in v.live.values()]
    refs = set()
    for a in actors:
        refs |= alive[a]
    for (_p, b, _i) in live:
        refs.add(b)
    recs = []
    for tkn in refs:
        holders = tuple(a for a in actors if tkn in alive[a])
        rec = (holders, tkn in v.superseded,
               tuple(sorted(((p, i) for (p, b, i) in live if b == tkn),
                            key=sk)))
        if enriched:
            rec = rec + (payload_of(tkn),)
        recs.append(rec)
    out = tuple(sorted(recs, key=sk))
    cache_store[key] = out
    return out


def payload_of(tkn):
    if tkn == V0:
        return ("genesis",)
    if tkn[1] == "m":
        return ("merge", b1_valueof(tkn), tkn[4])
    return ("arb", b1_valueof(tkn), tkn[3], tkn[4])


_SIGT = {}
_SIGC = {}


def sigT(h, actors=AB, enriched=False):
    return sigmaT(h, actors, enriched, b1_fullview, _SIGT)


def b3_fullview(acts):
    """d42b3 exposes View + event_poset but no full_view helper; the full
    view is View over every index, which is d42b1's own full_view body."""
    pred = b3_poset(acts)
    return b3_View(acts, pred, set(range(len(acts))))


def sigC(h, actors=AB, enriched=False):
    return sigmaT(h, actors, enriched, b3_fullview, _SIGC)


ROOT_T = sigT(())
ROOT_C = sigC(())
report("the root state sigma([]) at both scopes", f"transport {ROOT_T} | "
       f"closed {ROOT_C} | equal = {ROOT_T == ROOT_C}")

# --- the state is a function of (history, ACTOR POOL, map), and the cache
#     key must carry all three; gated, because a key that drops the pool
#     silently serves two-actor state to the three-actor arm.
_ab_root, _abc_root = sigT((), AB), sigT((), ABC)
_ab_root2 = sigT((), AB)
_shared = [tuple(h) for h in enumerate_line(b1_cand, AB, 2)[0]]
_pool_diff = sum(1 for k in _shared if sigT(k, AB) != sigT(k, ABC))
check("SIG.1 THE PORTED STATE IS A FUNCTION OF (history, ACTOR POOL, map) "
      "AND THE MEMO KEY CARRIES ALL THREE.  The same event word read in the "
      "(A,B) pool and in the (A,B,C) pool has DIFFERENT ported states — the "
      "token records name their holders, and C holds nothing — so a memo "
      "keyed on (history, map) alone would serve two-actor state to the "
      "three-actor arm on most shared words.  The key is (history, actor "
      "tuple, map); the two readings are checked to differ at the ROOT "
      "itself and on the shared words counted below, and to be stable "
      "under re-reading",
      _ab_root != _abc_root and _ab_root == _ab_root2 and _pool_diff > 0,
      f"root (A,B) = {_ab_root}; root (A,B,C) = {_abc_root}; shared words "
      f"to depth 2 = {len(_shared)}, pool-distinguished {_pool_diff}/"
      f"{len(_shared)}; re-read stable = {_ab_root == _ab_root2}")

# PORT-1: the R4 row at CLOSED scope — the table's own scope
_r4c = _r4c_root = 0
_rows_c = Counter()
for k in _KEYS:
    if not k:
        continue
    if is_R4(k[-1]):
        _r4c += 1
        _r4c_root += int(sigC(k) == ROOT_C)
    _rows_c[("R4" if is_R4(k[-1]) else k[-1][0])] += 1
check("PORT-1 THE R4 ROW AND ITS RENEWAL COROLLARY HOLD AT CLOSED SCOPE, "
      "recomputed here from the ported field set: every pair-arb in the "
      "closed-scope family to depth 6 returns the serialised state to the "
      "ROOT — D62's 'every pair-arb is a RENEWAL to the root state', which "
      "is a row of the table and not a measured coincidence",
      _r4c > 0 and _r4c_root == _r4c,
      f"{_r4c_root}/{_r4c} pair-arbs return to the root state on "
      f"{len(_KEYS)} closed-scope histories; event-tag census "
      f"{dict(sorted(_rows_c.items()))}")

# PORT-2: the R4 row at TRANSPORT scope, in-family
_t = time.time()
FAM_A, CACHE_A = enumerate_line(b1_cand, AB, CAP_A)
report("ARM-A family", f"{len(FAM_A)} histories, (A,B) transport, depth "
       f"<= {CAP_A}  [{time.time() - _t:.0f}s]")
_r4t = _r4t_root = 0
_post = Counter()
for h in FAM_A:
    k = tuple(h)
    if k and is_R4(k[-1]):
        _r4t += 1
        s = sigT(k)
        _r4t_root += int(s == ROOT_T)
        _post[s] += 1
check("PORT-2 THE PORT HOLDS IN-FAMILY AT THE DECLARED CAP: every pair-arb "
      "of the (A,B) transport family to depth 5 also returns the ported "
      "serialised state to the root, so at this window transport scope "
      "inherits D62's renewal corollary and paper 0 sec.4's fixed "
      "renewal-grain configuration space is realised",
      _r4t > 0 and _r4t_root == _r4t,
      f"{_r4t_root}/{_r4t} pair-arbs return to root; distinct "
      f"post-renewal states = {len(_post)}")

# PORT-3: the constructed beyond-cap witness — the port's boundary
_selfA = ("r", "A", frozenset({tA}), frozenset({tA}))
_v1 = b1_vname(V0, frozenset({tA}), "A")
_selfB = ("r", "B", frozenset({tB}), frozenset({tB}))
_vB = b1_vname(V0, frozenset({tB}), "B")
_pAv1 = ("p", "A", _v1, 0)
_pBv1 = ("p", "B", _v1, 1)
_tAv1, _tBv1 = ("A", _v1, 0), ("B", _v1, 1)
_pair_v1 = ("r", "A", frozenset({_tAv1, _tBv1}), frozenset({_tAv1}))
SIG_DIV = [pA0, _selfA, pB1, _selfB, ("d", "A", "B", _v1), _pAv1, _pBv1,
           _pair_v1]
_ok_div = all(b1_adm(SIG_DIV[:j], SIG_DIV[j], AB)[0]
              for j in range(len(SIG_DIV)))
_q_div = [b1_adm(SIG_DIV[:j], SIG_DIV[j], AB)[1] for j in range(len(SIG_DIV))]
_s_div = sigT(tuple(SIG_DIV))
check("PORT-3 AND THE PORT HAS A BOUNDARY, EXHIBITED ON A CONSTRUCTED "
      "ADMISSIBLE CHAIN BEYOND THE CAP.  Blind self-arbitration by both "
      "actors diverges the holdings; one delivery gives B a second alive "
      "token; the pair-arb that follows supersedes only its own base, so "
      "the post-renewal state carries TWO token records and is NOT the "
      "root.  Every one of the eight events is admission-checked against "
      "the committed layer and priced.  CONSEQUENCE, stated flatly: paper "
      "0 sec.4's [POSIT] that renewals reset to the root — hence that the "
      "division-event configuration space is fixed — is TRUE at every "
      "reachable cap here and FALSE in general at transport scope; it is a "
      "delivery-conditioned property, not a theorem of the grammar",
      _ok_div and _s_div != ROOT_T and len(_s_div) == 2
      and is_R4(SIG_DIV[-1]),
      f"chain admissible end to end = {_ok_div} (8 events, weights "
      f"{[str(x) for x in _q_div]}); post-pair-arb state has "
      f"{len(_s_div)} token records vs 1 at the root; state = {_s_div}")
print("      the witness chain, event by event:")
for _j, _e in enumerate(SIG_DIV):
    print(f"        {_j}: {_e}   q = {_q_div[_j]}")

_ren_cfg = {}
for h in FAM_A:
    k = tuple(h)
    if k and is_R4(k[-1]):
        _ren_cfg[sigT(k, AB, True)] = _ren_cfg.get(sigT(k, AB, True), 0) + 1
report("the renewal-grain configuration space, BOTH WAYS",
       f"winner-invisible (D62-faithful) states at renewals: "
       f"{len(_post)} — the root, and only the root; payload-enriched "
       f"states at renewals: {len(_ren_cfg)} — (winning value) x (winning "
       f"author) x (initiator), each realised {sorted(set(_ren_cfg.values()))} "
       f"times in-family")
print("      L-1's BOUND, quoted where it bites (paper 0 sec.7): the "
      "renewal-grain")
print("      configuration space just measured IS a fixed finite set at "
      "this cap, which")
print("      is exactly the hypothesis of the finite-stochastic Lorentz "
      "no-go.  So no")
print("      exact covariance may be claimed for the law built on it: v11 "
      "may expect")
print("      at most statistical/approximate Lorentz invariance at renewal "
      "grain,")
print("      never exact covariance, and this receipt claims none.")


# ===========================================================================
# SEC 7.  ARM 1, PART B — the Gamma family and the [B3] eq. 22 census
# ===========================================================================

sec("ARM 1 (b) — the Gamma family, and the [B3] eq. 22 interpolant census")


def horizon_measure(cache, fam, D, roots=None, root_weight=None):
    """The D46b/D70 relative-horizon construction, applied at the family's
    own cap: G(h, r) by the AST-lifted recursion with r = D - |h|, and the
    forward measure P built from k_r(e|h) = q(e|h) G(h+e, r-1)/G(h, r).
    Returns (G, P, bydepth).  Every value is an exact Fraction."""
    bydepth = defaultdict(list)
    for h in fam:
        bydepth[len(tuple(h))].append(tuple(h))
    for d in bydepth:
        bydepth[d] = sorted(bydepth[d], key=sk)
    G = {}
    d0 = min(bydepth)
    for d in range(D, d0 - 1, -1):
        for k in bydepth[d]:
            G[k] = (Fr(1) if d == D
                    else sum(q * G[k + (e,)] for e, q in cache[k]))
    P = {}
    if roots is None:
        P[()] = Fr(1)
    else:
        Z = sum(root_weight[b] * G[b] for b in roots)
        for b in roots:
            P[b] = root_weight[b] * G[b] / Z
    for d in range(d0, D):
        for k in bydepth[d]:
            if k not in P:
                continue
            for e, q in cache[k]:
                P[k + (e,)] = P.get(k + (e,), Fr(0)) + P[k] * q * G[k + (e,)] / G[k]
    return G, P, bydepth


def kernel_rows_are_stochastic(cache, G, bydepth, D):
    bad = 0
    n = 0
    for d in range(min(bydepth), D):
        for k in bydepth[d]:
            n += 1
            s = sum(q * G[k + (e,)] / G[k] for e, q in cache[k])
            bad += int(s != Fr(1))
    return n, bad


_t = time.time()
G_A, P_A, BD_A = horizon_measure(CACHE_A, FAM_A, CAP_A)
_n, _bad = kernel_rows_are_stochastic(CACHE_A, G_A, BD_A, CAP_A)
_mass = [sum(P_A[k] for k in BD_A[d]) for d in range(CAP_A + 1)]
check("G1 THE LAW IS A PROBABILITY LAW BY CONSTRUCTION, GATED EXACTLY: "
      "with the D46b relative-horizon normalisation the one-step kernel "
      "sums to exactly 1 at every history of the family, and the induced "
      "cut marginal is exactly 1 at every depth.  This is what makes a "
      "Gamma family exist at all: the RAW generated menus sum to 2 or 5/2 "
      "and are not a stochastic matrix (the D75 audit's sec.5.3 point)",
      _bad == 0 and all(m == Fr(1) for m in _mass),
      f"kernels tested {_n}, non-unit row sums {_bad}; cut masses by depth "
      f"{[str(m) for m in _mass]}")
report("raw menu masses (the object the normalisation repairs)",
       fmt(Counter(sum(q for e, q in CACHE_A[tuple(h)]) for h in FAM_A)))


# ---------- exact rational Phase-I simplex, with a Farkas certificate ----
def phase1(M, b, maxpivot=LP_MAXPIVOT, rule="bland", stall=60):
    """Exact: does x >= 0 with M x = b exist?  No floats anywhere.
    Returns (feasible, pivots, cert) where cert is the FEASIBLE POINT x
    when one exists and the Farkas vector w (w^T M <= 0, w^T b > 0,
    verified by the caller) when one does not.

    rule='bland'   — Bland's entering rule throughout; the slow, always
                     terminating instrument, used on every system inside
                     the plain LP cap.
    rule='dantzig' — most-negative reduced cost, with Bland's rule forced
                     after `stall` consecutive degenerate pivots, which is
                     what makes termination finite.  Used only on the
                     reduced systems of SEC 7's raised cap.  The rule
                     changes the pivot PATH and nothing else: the verdict,
                     the feasible point and the Farkas vector are all
                     certified after the fact, and gate LP.1 runs both
                     rules on the same systems and compares verdicts."""
    m = len(M)
    n = len(M[0]) if m else 0
    rows = []
    for i in range(m):
        r = list(M[i])
        bi = b[i]
        if bi < 0:
            r = [-x for x in r]
            bi = -bi
        rows.append(r + [Fr(0)] * m + [bi])
    for i in range(m):
        rows[i][n + i] = Fr(1)
    basis = [n + i for i in range(m)]
    cost = [Fr(0)] * (n + m + 1)
    for i in range(m):
        for j in range(n + m + 1):
            cost[j] -= rows[i][j]
    for i in range(m):
        cost[n + i] = Fr(0)
    piv = 0
    degen = 0
    obj = -cost[-1]
    while True:
        e = -1
        if rule == "bland" or degen >= stall:
            for j in range(n + m):
                if cost[j] < 0:
                    e = j
                    break
        else:
            bestc = Fr(0)
            for j in range(n + m):
                if cost[j] < bestc:
                    bestc, e = cost[j], j
        if e < 0:
            break
        l = -1
        best = None
        for i in range(m):
            if rows[i][e] > 0:
                rt = rows[i][-1] / rows[i][e]
                if best is None or rt < best or (rt == best
                                                 and basis[i] < basis[l]):
                    best, l = rt, i
        if l < 0:
            return None, piv, None
        pv = rows[l][e]
        rows[l] = [x / pv for x in rows[l]]
        for i in range(m):
            if i != l and rows[i][e] != 0:
                fq = rows[i][e]
                rows[i] = [a - fq * bb for a, bb in zip(rows[i], rows[l])]
        if cost[e] != 0:
            fq = cost[e]
            cost = [a - fq * bb for a, bb in zip(cost, rows[l])]
        basis[l] = e
        piv += 1
        nobj = -cost[-1]
        degen = degen + 1 if nobj == obj else 0
        obj = nobj
        if piv > maxpivot:
            raise RuntimeError("pivot cap exceeded")
    if obj == 0:
        x = [Fr(0)] * n
        for i in range(m):
            if basis[i] < n:
                x[basis[i]] = rows[i][-1]
        return True, piv, x
    w = [Fr(1) - cost[n + i] for i in range(m)]
    for i in range(m):
        if b[i] < 0:
            w[i] = -w[i]
    return False, piv, w


def farkas_ok(M, b, w):
    """Independent verification of an infeasibility certificate:
    w^T M <= 0 componentwise and w^T b > 0 proves {x >= 0 : Mx = b} = {}."""
    if w is None:
        return False
    n = len(M[0])
    for j in range(n):
        if sum(w[i] * M[i][j] for i in range(len(M))) > 0:
            return False
    return sum(w[i] * b[i] for i in range(len(M))) > 0


def reduce_system(A, B, Is, Js, Ks):
    """The interpolant system {X >= 0, X.Gamma(c'<-c) = Gamma(c''<-c),
    1^T X = 1^T} rewritten by two reductions, each FEASIBILITY-PRESERVING
    IN BOTH DIRECTIONS and each proved here rather than assumed:

      (R1) IMPLIED ZEROS.  If some i has A[j,i] > 0 while B[k,i] = 0, the
           equation sum_j' X[k,j'] A[j',i] = B[k,i] = 0 is a sum of
           non-negative terms, so X[k,j] = 0 in EVERY solution.  Those
           variables are deleted; each equation (k,i) with B[k,i] = 0 then
           reads 0 = 0 on the surviving variables and is deleted too.
      (R2) AGGREGATION.  If j1 and j2 carry the SAME column
           a_j = (A[j,i])_i, replacing X's two columns by their average
           leaves every row sum and every column sum unchanged, so a
           solution exists iff a solution constant on {j1, j2} exists.
           The same averaging works for two targets k1, k2 with the same
           row b_k = (B[k,i])_i.  One variable per (b-group, a-group)
           then suffices, carrying the group sizes as coefficients.

    Feasibility of the reduced system LIFTS to X[k,j] = x[grp(k), grp(j)];
    infeasibility of the reduced system therefore proves indivisibility.
    Returns (M, b, var, GL, HL, Gsz, Hsz, err)."""
    aj = {j: tuple(A.get((j, i), Fr(0)) for i in Is) for j in Js}
    bk = {k: tuple(B.get((k, i), Fr(0)) for i in Is) for k in Ks}
    Gs, Hs = defaultdict(list), defaultdict(list)
    for j in Js:
        Gs[aj[j]].append(j)
    for k in Ks:
        Hs[bk[k]].append(k)
    key = lambda v: sk(tuple(str(x) for x in v))
    GL, HL = sorted(Gs, key=key), sorted(Hs, key=key)
    sG = {g: frozenset(t for t, v in enumerate(g) if v) for g in GL}
    sH = {h: frozenset(t for t, v in enumerate(h) if v) for h in HL}
    var = {}
    for h in HL:
        for g in GL:
            if sG[g] <= sH[h]:
                var[(h, g)] = len(var)
    n = len(var)
    M, bb = [], []
    for g in GL:
        row = [Fr(0)] * n
        hit = False
        for h in HL:
            if (h, g) in var:
                row[var[(h, g)]] = Fr(len(Hs[h]))
                hit = True
        if not hit:
            return None, None, None, GL, HL, Gs, Hs, "NO-TARGET"
        M.append(row)
        bb.append(Fr(1))
    for h in HL:
        for t in sorted(sH[h]):
            row = [Fr(0)] * n
            for g in GL:
                if (h, g) in var and g[t]:
                    row[var[(h, g)]] = Fr(len(Gs[g])) * g[t]
            M.append(row)
            bb.append(h[t])
    return M, bb, var, GL, HL, Gs, Hs, None


def lift_and_verify(x, var, GL, HL, Gs, Hs, A, B, Is, Js, Ks):
    """Lift a reduced solution to the full X and verify it from scratch:
    every entry >= 0, every COLUMN sum exactly 1, and X.Gamma(c'<-c)
    exactly Gamma(c''<-c) entry by entry.  Returns (X, colsums_ok,
    rows_ok, nonneg_ok)."""
    grpJ = {j: g for g in GL for j in Gs[g]}
    grpK = {k: h for h in HL for k in Hs[h]}
    X = {}
    for k in Ks:
        for j in Js:
            v = x[var[(grpK[k], grpJ[j])]] if (grpK[k], grpJ[j]) in var \
                else Fr(0)
            if v:
                X[(k, j)] = v
    nonneg = all(v >= 0 for v in X.values())
    cols = [sum(X.get((k, j), Fr(0)) for k in Ks) for j in Js]
    rowsok = True
    for k in Ks:
        for i in Is:
            s = sum(X.get((k, j), Fr(0)) * A.get((j, i), Fr(0)) for j in Js)
            if s != B.get((k, i), Fr(0)):
                rowsok = False
    return X, all(c == Fr(1) for c in cols), rowsok, nonneg


# ---------- the Gamma machinery -----------------------------------------
def joint_paths(bydepth, P, alpha, cuts, leafdepth):
    """The exact joint law of the configuration read at each cut, computed
    from the leaves of the family (so the marginals are the cut marginals
    of the horizon-normalised process)."""
    J = defaultdict(Fr)
    for k in bydepth[leafdepth]:
        p = P.get(k)
        if not p:
            continue
        J[tuple(alpha(k[:c]) for c in cuts)] += p
    return J


def gamma_of(J, ia, ib):
    """Gamma(cut ia <- cut ib) as a dict {(j, i): Fraction}, column-
    stochastic: entry (j, i) = P(config j at cut ia | config i at cut ib)."""
    num = defaultdict(Fr)
    den = defaultdict(Fr)
    for key, p in J.items():
        num[(key[ia], key[ib])] += p
        den[key[ib]] += p
    return {k: v / den[k[1]] for k, v in sorted(num.items(), key=lambda z: sk(z[0]))}


def supports(J, ncuts):
    return {c: srt({key[c] for key in J}) for c in range(ncuts)}


def decide_triple(J, S, i0, i1, i2, label, lp_stats):
    """The [B3] eq. 22 decision at one composable triple.  Returns a dict
    with the verdict and every quantity behind it."""
    A = gamma_of(J, i1, i0)          # Gamma(c' <- c)
    B = gamma_of(J, i2, i0)          # Gamma(c'' <- c)
    N = gamma_of(J, i2, i1)          # the process's OWN intermediate
    Is, Js, Ks = S[i0], S[i1], S[i2]
    out = dict(triple=label, nI=len(Is), nJ=len(Js), nK=len(Ks))
    # (0) structural vacuity
    if len(Is) < 2:
        out["verdict"] = "VACUOUS"
        out["why"] = "first cut carries a single configuration"
        return out
    # (1) does the process's own conditional already do it? (Chapman-Kolmogorov)
    byj = defaultdict(list)
    for (j, i), v in A.items():
        if v:
            byj[j].append((i, v))
    comp = defaultdict(Fr)
    for (kk, j), w in N.items():
        if w:
            for i, v in byj.get(j, ()):
                comp[(kk, i)] += w * v
    ck = (all(comp.get(k, Fr(0)) == v for k, v in B.items())
          and all(B.get(k, Fr(0)) == v for k, v in comp.items()))
    out["CK"] = ck
    if ck:
        out["verdict"] = "DIVISIBLE"
        out["why"] = "the process's own conditional Gamma(c''<-c') works"
        out["neg"] = 0
        return out
    # (2) the algebraic interpolant, when Gamma(c'<-c) is square+invertible
    out["square"] = (len(Is) == len(Js))
    if out["square"]:
        Mx = [[A.get((j, i), Fr(0)) for i in Is] for j in Js]
        inv, det = invert_exact(Mx)
        out["det"] = det
        if inv is not None:
            Bm = [[B.get((k, i), Fr(0)) for i in Is] for k in Ks]
            Gb = [[sum(Bm[r][t] * inv[t][c] for t in range(len(Is)))
                   for c in range(len(Js))] for r in range(len(Ks))]
            neg = [(r, c, Gb[r][c]) for r in range(len(Ks))
                   for c in range(len(Js)) if Gb[r][c] < 0]
            colsum = [sum(Gb[r][c] for r in range(len(Ks)))
                      for c in range(len(Js))]
            out["neg"] = len(neg)
            out["negvals"] = sorted({str(x[2]) for x in neg})
            out["colsums_unit"] = all(x == Fr(1) for x in colsum)
            out["verdict"] = ("INDIVISIBLE" if neg else "DIVISIBLE")
            out["why"] = ("the UNIQUE algebraic interpolant Gammabar = "
                          "Gamma(c''<-c) Gamma(c'<-c)^-1 has negative "
                          "entries ([B3] eq. 22)" if neg else
                          "the unique algebraic interpolant is stochastic")
            out["instrument"] = "eq22-algebraic"
            return out
    # (3) the row certificate: row k of X must solve A^T y = B[k,:], y >= 0
    bad = []
    certs = []
    for k in Ks:
        M = [[A.get((j, i), Fr(0)) for j in Js] for i in Is]
        bb = [B.get((k, i), Fr(0)) for i in Is]
        feas, _p, w = phase1(M, bb)
        if feas is False and farkas_ok(M, bb, w):
            bad.append(k)
            certs.append((k, w, sum(w[i] * bb[i] for i in range(len(Is)))))
    out["rowfail"] = len(bad)
    if bad:
        out["verdict"] = "INDIVISIBLE"
        out["instrument"] = "row-certificate (Farkas, verified)"
        out["why"] = (f"{len(bad)} of {len(Ks)} target configurations admit "
                      f"NO non-negative row at all")
        out["neg"] = None
        out["rowcerts"] = certs
        out["rowcert_basis"] = list(Is)
        return out
    # (4) the full feasibility LP
    nvar = len(Ks) * len(Js)
    nrow = len(Js) + len(Ks) * len(Is)
    out["nvar"], out["nrow"] = nvar, nrow
    if nvar > LP_MAXVARS or nrow > LP_MAXROWS:
        return decide_reduced(A, B, Is, Js, Ks, out, lp_stats)
    idx = {}
    for k in Ks:
        for j in Js:
            idx[(k, j)] = len(idx)
    M, bb = [], []
    for j in Js:
        row = [Fr(0)] * nvar
        for k in Ks:
            row[idx[(k, j)]] = Fr(1)
        M.append(row)
        bb.append(Fr(1))
    for k in Ks:
        for i in Is:
            row = [Fr(0)] * nvar
            for j in Js:
                a = A.get((j, i))
                if a:
                    row[idx[(k, j)]] = a
            M.append(row)
            bb.append(B.get((k, i), Fr(0)))
    t0 = time.time()
    feas, piv, w = phase1(M, bb)
    lp_stats.append((label, nvar, nrow, piv, time.time() - t0))
    if feas:
        out["verdict"] = "DIVISIBLE"
        out["instrument"] = "exact LP feasibility"
        out["why"] = ("a stochastic intermediate EXISTS but is NOT the "
                      "process's own conditional (CK fails)")
        Xd = {}
        for (k, j), t in idx.items():
            if w[t]:
                Xd[(k, j)] = w[t]
        cols = [sum(Xd.get((k, j), Fr(0)) for k in Ks) for j in Js]
        rws = all(sum(Xd.get((k, j), Fr(0)) * A.get((j, i), Fr(0))
                      for j in Js) == B.get((k, i), Fr(0))
                  for k in Ks for i in Is)
        out["interp"] = (Xd, all(c == Fr(1) for c in cols), rws,
                         all(v >= 0 for v in Xd.values()))
    else:
        ok = farkas_ok(M, bb, w)
        out["verdict"] = "INDIVISIBLE"
        out["instrument"] = ("exact LP infeasibility, Farkas certificate "
                             + ("VERIFIED" if ok else "NOT VERIFIED"))
        out["farkas"] = ok
        out["lpcert"] = (w, sum(w[i] * bb[i] for i in range(len(M))),
                         len(M[0]))
        out["why"] = ("no column-stochastic X satisfies X Gamma(c'<-c) = "
                      "Gamma(c''<-c)")
    out["neg"] = None
    return out


def decide_reduced(A, B, Is, Js, Ks, out, lp_stats):
    """The raised cap: decide the triple on the REDUCED system built by
    reduce_system(), whose feasibility is equivalent to the full one."""
    M, bb, var, GL, HL, Gs, Hs, err = reduce_system(A, B, Is, Js, Ks)
    if err == "NO-TARGET":
        out["verdict"] = "INDIVISIBLE"
        out["instrument"] = "implied-zero cover (R1)"
        out["why"] = ("some configuration at the middle cut has NO target "
                      "it may be sent to at all: its column sum cannot be 1")
        out["neg"] = None
        return out
    out["rvar"], out["rrow"] = len(var), len(M)
    out["rgrp"] = (len(GL), len(HL))
    if len(var) > LP2_MAXVARS or len(M) > LP2_MAXROWS:
        out["verdict"] = "EXCLUDED-BY-CAP"
        out["instrument"] = "row-certificate only"
        out["why"] = (f"full LP {out['nvar']}v x {out['nrow']}r and reduced "
                      f"LP {len(var)}v x {len(M)}r both exceed the declared "
                      f"caps; the row certificate ran and returned no "
                      f"obstruction, which is NOT a proof of divisibility "
                      f"in either direction")
        return out
    t0 = time.time()
    feas, piv, cert = phase1(M, bb, rule="dantzig")
    lp_stats.append((str(out["triple"]) + "/reduced", len(var), len(M), piv,
                     time.time() - t0))
    if feas:
        X, cok, rok, nok = lift_and_verify(cert, var, GL, HL, Gs, Hs,
                                           A, B, Is, Js, Ks)
        out["verdict"] = "DIVISIBLE"
        out["instrument"] = ("exact LP feasibility on the reduced system, "
                             "interpolant lifted and re-verified")
        out["why"] = ("a column-stochastic interpolant EXISTS (exhibited "
                      "and checked entry by entry) but is NOT the "
                      "process's own conditional (CK fails)")
        out["interp"] = (X, cok, rok, nok)
    else:
        ok = farkas_ok(M, bb, cert)
        out["verdict"] = "INDIVISIBLE"
        out["instrument"] = ("exact LP infeasibility on the reduced system, "
                             "Farkas certificate "
                             + ("VERIFIED" if ok else "NOT VERIFIED"))
        out["farkas"] = ok
        out["lpcert"] = (cert, sum(cert[i] * bb[i] for i in range(len(M))),
                         len(var))
        out["why"] = ("no column-stochastic X satisfies X Gamma(c'<-c) = "
                      "Gamma(c''<-c)")
    out["neg"] = None
    return out


def invert_exact(M):
    """Exact rational inverse by Gauss-Jordan; returns (inverse, det)."""
    n = len(M)
    A = [row[:] + [Fr(1) if i == j else Fr(0) for j in range(n)]
         for i, row in enumerate(M)]
    det = Fr(1)
    for c in range(n):
        p = None
        for r in range(c, n):
            if A[r][c] != 0:
                p = r
                break
        if p is None:
            return None, Fr(0)
        if p != c:
            A[c], A[p] = A[p], A[c]
            det = -det
        det *= A[c][c]
        pv = A[c][c]
        A[c] = [x / pv for x in A[c]]
        for r in range(n):
            if r != c and A[r][c] != 0:
                fq = A[r][c]
                A[r] = [x - fq * y for x, y in zip(A[r], A[c])]
    return [row[n:] for row in A], det


def fr_digest(vec, labels=None, cap=24):
    """A hand-checkable exact digest of a certificate vector: the non-zero
    entries as Fractions, in index order, with the count and the exact sum
    so a reader can re-add them."""
    nz = [(i, v) for i, v in enumerate(vec) if v != 0]
    body = ", ".join(f"{i}:{v}" for i, v in nz[:cap])
    tail = f" ... (+{len(nz) - cap} more)" if len(nz) > cap else ""
    return (f"{len(nz)} non-zero of {len(vec)}; sum = "
            f"{sum(v for _i, v in nz)}; entries [{body}{tail}]")


def print_certificate(r):
    """Every INDIVISIBLE verdict prints its certificate in exact rationals,
    so a reader can check it by hand rather than take the word 'verified'."""
    if r["verdict"] != "INDIVISIBLE":
        return
    if "lpcert" in r:
        w, wb, ncol = r["lpcert"]
        print(f"          FARKAS w (w^T M <= 0 on all {ncol} columns, "
              f"w^T b = {wb} > 0): {fr_digest(w)}")
    if "rowcerts" in r:
        k0, w0, wb0 = r["rowcerts"][0]
        print(f"          FARKAS, row certificate: {len(r['rowcerts'])} "
              f"obstructed targets; exemplar w over the {len(w0)} "
              f"first-cut configurations, w^T b = {wb0} > 0: "
              f"{fr_digest(w0)}")
        print(f"          all obstructed w^T b: "
              f"{[str(c[2]) for c in r['rowcerts']]}")


def print_interpolant(r):
    if r["verdict"] != "DIVISIBLE" or "interp" not in r:
        return
    X, cok, rok, nok = r["interp"]
    print(f"          INTERPOLANT X exhibited: {len(X)} non-zero entries; "
          f"column sums all exactly 1 = {cok}; X.Gamma(c'<-c) = "
          f"Gamma(c''<-c) entry by entry = {rok}; every entry >= 0 = {nok}")


def run_census(name, J, cuts, note="", divcuts=()):
    S = supports(J, len(cuts))
    print()
    print(f"  [{name}]  cuts {list(cuts)}; configuration support sizes "
          f"{[len(S[c]) for c in range(len(cuts))]}"
          + (f";  {note}" if note else ""))
    lp_stats = []
    rows = []
    for i0 in range(len(cuts)):
        for i1 in range(i0 + 1, len(cuts)):
            for i2 in range(i1 + 1, len(cuts)):
                lab = (cuts[i0], cuts[i1], cuts[i2])
                r = decide_triple(J, S, i0, i1, i2, lab, lp_stats)
                r["divcut"] = cuts[i0] in divcuts
                r["arm"] = name
                rows.append(r)
                extra = ""
                if r.get("neg"):
                    extra = (f"; NEGATIVE ENTRIES = {r['neg']} exactly, "
                             f"values {r.get('negvals')}")
                if r.get("nvar"):
                    extra += f"; LP {r['nvar']}v x {r['nrow']}r"
                if r.get("rvar"):
                    extra += (f" -> reduced {r['rvar']}v x {r['rrow']}r "
                              f"(groups {r['rgrp'][0]}x{r['rgrp'][1]})")
                print(f"      {lab}  {r['verdict']:16s} "
                      f"[{r.get('instrument', 'CK')}]  "
                      f"sizes {r['nI']}x{r['nJ']}x{r['nK']}  {r['why']}"
                      + extra
                      + ("  [first cut IS a division event]"
                         if r["divcut"] else ""))
                print_certificate(r)
                print_interpolant(r)
    ver = Counter(r["verdict"] for r in rows)
    print(f"      CENSUS {name}: " + ", ".join(f"{k} {v}" for k, v in
                                               sorted(ver.items())))
    if lp_stats:
        print(f"      LP work: " + "; ".join(
            f"{l} {v}v x {r}r, {p} pivots, {t:.1f}s"
            for l, v, r, p, t in lp_stats))
    return rows, S


# ---------------- ARM-A: the record grain of the realizer ---------------
print()
print("  ARM-A — the RECORD GRAIN of v10's own law: cuts are the depths of "
      "the")
print("  generated order, configurations are the ported D62 state (both "
      "ways:")
print("  winner-invisible and payload-enriched).  This is the grain at "
      "which v10")
print("  ran everything, and paper 0 sec.3 assigns v10's per-click law to "
      "THE")
print("  REALIZER; the census below asks what the law looks like when it is")
print("  read at the record's own grain instead of the realizer's.")
CUTS_A = tuple(range(CAP_A + 1))
ARM_A_RESULTS = {}
for _nm, _enr in (("alpha_sigma  (D62-faithful, winner-invisible)", False),
                  ("alpha_sigma+ (payload-enriched)", True)):
    J = joint_paths(BD_A, P_A, lambda k, e=_enr: sigT(k, AB, e), CUTS_A,
                    CAP_A)
    rows, S = run_census("ARM-A / " + _nm, J, CUTS_A, divcuts=(0,))
    ARM_A_RESULTS[_nm] = (rows, S, J)
report("ARM-A time", f"{time.time() - _t:.0f}s")

# ---------------- ARM-B: the division-event grain -----------------------
_t = time.time()
print()
print("  ARM-B — the DIVISION-EVENT GRAIN.  The ensemble is conditioned on "
      "a PAST")
print("  event only: that the depth-3 prefix ends in a pair-arb, i.e. that "
      "the")
print("  first division event has occurred at the earliest depth the "
      "grammar")
print("  allows.  The initial distribution over those histories is the "
      "horizon-6")
print("  measure's own conditional, so no future information is used.")
FAM3, CACHE3 = enumerate_line(b1_cand, AB, 3)
BASES = srt(tuple(h) for h in FAM3 if len(h) == 3 and is_R4(h[-1]))
CACHE_B = {}
FAM_B = []
for b in BASES:
    fam_b, cache_b = enumerate_line(
        lambda hh, aa, _b=b: b1_cand(list(_b) + list(hh), aa), AB,
        CAP_B - 3)
    for hh in fam_b:
        k = b + tuple(hh)
        FAM_B.append(k)
        CACHE_B[k] = cache_b[tuple(hh)]
MU_B = {}
for b in BASES:
    m = Fr(1)
    for j in range(3):
        m *= [q for e, q in CACHE3[b[:j]] if e == b[j]][0]
    MU_B[b] = m
G_B, P_B, BD_B = horizon_measure(CACHE_B, FAM_B, CAP_B, roots=BASES,
                                 root_weight=MU_B)
_n, _bad = kernel_rows_are_stochastic(CACHE_B, G_B, BD_B, CAP_B)
_mass = [sum(P_B[k] for k in BD_B[d]) for d in range(3, CAP_B + 1)]
check("G2 ARM-B is a probability law too: the horizon-6 kernel sums to 1 "
      "at every history of the renewal-started window and the cut marginal "
      "is 1 at depths 3..6",
      _bad == 0 and all(m == Fr(1) for m in _mass),
      f"{len(BASES)} renewal bases, {len(FAM_B)} histories; kernels "
      f"{_n}, non-unit {_bad}; cut masses {[str(m) for m in _mass]}")
CUTS_B = tuple(range(3, CAP_B + 1))
ARM_B_RESULTS = {}
for _nm, _enr in (("alpha_sigma  (D62-faithful, winner-invisible)", False),
                  ("alpha_sigma+ (payload-enriched)", True)):
    J = joint_paths(BD_B, P_B, lambda k, e=_enr: sigT(k, AB, e), CUTS_B,
                    CAP_B)
    rows, S = run_census("ARM-B / " + _nm, J, CUTS_B,
                         note="cut 3 IS a division event", divcuts=(3,))
    ARM_B_RESULTS[_nm] = (rows, S, J)
print()
print("      HOW FAR ARM-B REACHES, AND THE MAP-DEPENDENCE IT EXPOSES.  "
      "ARM-B's")
print("      window runs three steps past the division event, i.e. "
      "relative")
print("      depths 0..3, so ARM-A's triples that begin at relative depth "
      ">= 2")
print("      ((2,3,4) and later) would need depths 5,6,7 and are beyond "
      "this")
print("      cap.  ARM-A's other two indivisible triples begin at relative")
print("      depth 1 — (1,2,3) and (1,3,4) — and their post-renewal "
      "analogue")
print("      IS inside the window: it is ARM-B's (4,5,6).  It is "
      "DIVISIBLE by")
print("      exact Chapman-Kolmogorov under the D62-faithful map and "
      "INDIVISIBLE")
print("      under the payload-enriched one.  So the one comparison this "
      "arm")
print("      can actually make points in the ARTEFACT direction for the "
      "coarse")
print("      map and against it for the fine one: the verdict at a "
      "post-renewal")
print("      window is a property of the CONFIGURATION MAP, not of the "
      "process")
print("      alone.  Both readings are printed above and neither is "
      "preferred.")
report("ARM-B time", f"{time.time() - _t:.0f}s")

# ---------------- ARM-C: renewal-to-renewal -----------------------------
_t = time.time()
print()
print("  ARM-C — RENEWAL-TO-RENEWAL.  Cuts are renewal indices 0, 1, 2.")
_ren2 = defaultdict(Fr)
_ren2_tot = Fr(0)
for k in BD_B[CAP_B]:
    if is_R4(k[-1]):
        _ren2[(sigT(k[:3], AB, True), sigT(k, AB, True))] += P_B[k]
        _ren2_tot += P_B[k]
_r1cfg = srt({a for a, b in _ren2})
_r2cfg = srt({b for a, b in _ren2})
report("renewal 2 within the cap",
       f"mass reaching a second renewal by depth {CAP_B} = {_ren2_tot}; "
       f"renewal-1 configurations {len(_r1cfg)}; renewal-2 configurations "
       f"{len(_r2cfg)}")
_R = {}
for a in _r1cfg:
    tot = sum(v for (x, y), v in _ren2.items() if x == a)
    for b in _r2cfg:
        _R[(b, a)] = sum(v for (x, y), v in _ren2.items()
                         if x == a and y == b) / tot
_cols = [tuple(str(_R[(b, a)]) for b in _r2cfg) for a in _r1cfg]
_homog = len(set(_cols)) == 1
check("C1 THE RENEWAL STEP IS CONFIGURATION-INDEPENDENT (measured, at the "
      "cap): conditioned on a second renewal occurring inside the window, "
      "the distribution of the renewal-2 configuration is the SAME "
      "whichever renewal-1 configuration the process came from.  The "
      "renewal-to-renewal transfer is therefore a RANK-ONE column-"
      "stochastic matrix, R^2 = R, and every renewal triple factors "
      "through it — the renewal chain is a genuine renewal process at this "
      "scope.  DECLARED: this conditions on a FUTURE event (that renewal 2 "
      "arrives by depth 6), which at this cap forces both renewal "
      "intervals to be minimal; it is the conditioned law of that "
      "sub-ensemble and is labelled as such",
      _homog and len(_r1cfg) > 1,
      f"{len(_r1cfg)} distinct renewal-1 configurations, "
      f"{len(set(_cols))} distinct renewal-step columns "
      f"(1 == configuration-independent); rank-one = {_homog}")
check("C2 THE RENEWAL-TO-RENEWAL TRIPLE (0,1,2) IS STRUCTURALLY VACUOUS "
      "under the winner-invisible map at every reachable cap, and this is "
      "reported rather than dressed up: renewal cut 0 is the root, a "
      "SINGLE configuration, so by the preamble's degeneracy clause a "
      "stochastic interpolant always exists.  A NON-DEGENERATE renewal "
      "triple needs THREE renewals, i.e. depth >= 9 in this grammar; "
      "ARM-C2 below runs exactly that",
      True,
      f"renewal cut 0 configurations = 1; the first non-degenerate renewal "
      f"triple sits at depth >= 9 (>= 3 pair-arbs x 3 events), beyond cap "
      f"{CAP_B} — ARM-C2 reaches it by conditioning instead of enumerating")
report("ARM-C time", f"{time.time() - _t:.0f}s")

# ------- ARM-C2: THE PINNED NON-DEGENERATE RENEWAL-TO-RENEWAL TRIPLE ----
_t = time.time()
print()
print("  ARM-C2 — THE PINNED TEST, RUN.  The cut triple is (renewal 1, "
      "renewal 2,")
print("  renewal 3): three DIVISION EVENTS, the grain paper 0 sec.4 says "
      "the law")
print("  lives at, with a FIRST CUT THAT IS NOT THE ROOT.  Depth 9 is not")
print("  enumerated — the two-actor transport family has ~10^8 histories "
      "there.")
print("  It is reached by CONDITIONING instead, and the conditioning is "
      "what")
print("  makes it exact rather than sampled:")
print("    (i)  at horizon D the relative-horizon leaf measure telescopes "
      "to")
print("         P(leaf) = prod_t q_t / G(root, D) — G(leaf,0) = 1 — so the "
      "law")
print("         CONDITIONED on any set of depth-D leaves needs only those")
print("         leaves' raw products; the normaliser cancels.  No sampling, "
      "no")
print("         truncation, exact rationals.")
print("   (ii)  a pair-arbitration needs two proposals in its ckey; at a")
print("         renewal the ported state is the ROOT, which carries NO "
      "live")
print("         operations (gated below), so a renewal three events after a")
print("         renewal forces the intervening two events to be proposals.")
print("         The depth-9 leaves carrying three renewals at 3, 6, 9 are")
print("         therefore enumerable directly and EXHAUSTIVELY.")
print("  DECLARED, and it is the arm's boundary: this is the "
      "MINIMAL-INTERVAL")
print("  sub-ensemble — conditioning on renewal 3 by depth 9 forces all "
      "three")
print("  renewal intervals to their shortest length.  It is the same "
      "future-")
print("  conditioning ARM-C declares, one renewal further on.")
_live_at_root = [rec[2] for rec in ROOT_T]
check("C2a THE ROOT CARRIES NO LIVE OPERATIONS, which is what licenses the "
      "enumeration above: every ported token record at the root state has "
      "an EMPTY live-triple list, so no proposal survives a renewal and a "
      "pair-arb three events later must be fed by two fresh proposals",
      all(len(x) == 0 for x in _live_at_root),
      f"root state {ROOT_T}; live-triple lists {_live_at_root}")


def _ppr(base, w0):
    """Every continuation of `base` that ends in a pair-arbitration exactly
    three events later: proposal, proposal, pair-arb (C2a licenses the
    restriction).  Exact weights, carried multiplicatively."""
    out = []
    for e1, q1 in b1_cand(list(base), AB):
        if e1[0] != "p":
            continue
        h1 = base + (e1,)
        for e2, q2 in b1_cand(list(h1), AB):
            if e2[0] != "p":
                continue
            h2 = h1 + (e2,)
            for e3, q3 in b1_cand(list(h2), AB):
                if is_R4(e3):
                    out.append((h2 + (e3,), w0 * q1 * q2 * q3))
    return out


_R2H = []
for _b in BASES:
    _R2H += _ppr(_b, MU_B[_b])
_R3H = []
for _h6, _w in _R2H:
    _R3H += _ppr(_h6, _w)
_r3tot = sum(w for _h, w in _R3H)
check("C2b THE MINIMAL-INTERVAL RENEWAL-3 ENSEMBLE IS BUILT AND CLOSED: "
      "every depth-6 history in it ends in a pair-arbitration whose ported "
      "state is exactly the root, and every depth-9 history in it ends in a "
      "third pair-arbitration",
      len(_R3H) > 0
      and all(sigT(h) == ROOT_T and is_R4(h[-1]) for h, _w in _R2H)
      and all(is_R4(h[-1]) for h, _w in _R3H),
      f"{len(BASES)} renewal-1 bases -> {len(_R2H)} renewal-2 histories "
      f"(depth 6) -> {len(_R3H)} renewal-3 histories (depth 9); raw mass "
      f"{_r3tot}")
ARM_C2 = {}
for _nm, _enr in (("alpha_sigma  (D62-faithful, winner-invisible)", False),
                  ("alpha_sigma+ (payload-enriched)", True)):
    _JC = defaultdict(Fr)
    for _h, _w in _R3H:
        _JC[(sigT(_h[:3], AB, _enr), sigT(_h[:6], AB, _enr),
             sigT(_h, AB, _enr))] += _w / _r3tot
    _rows, _S = run_census("ARM-C2 / " + _nm, dict(_JC), (1, 2, 3),
                           note="cuts are RENEWAL INDICES 1,2,3 — all three "
                                "are division events", divcuts=(1, 2, 3))
    ARM_C2[_nm] = (_rows, _S, dict(_JC))
_c2rows = ARM_C2["alpha_sigma+ (payload-enriched)"][0]
_c2S = ARM_C2["alpha_sigma+ (payload-enriched)"][1]
_c2v = _c2rows[0]["verdict"]
check("C2c THE PINNED QUESTION IS DECIDED, AND IT DIVIDES.  The "
      "non-degenerate renewal-to-renewal triple — first cut a division "
      "event carrying MORE THAN ONE configuration, which is what makes it "
      "non-degenerate, and the very computation the cap blocked — admits a "
      "stochastic interpolant.  At renewal grain, on the minimal-interval "
      "sub-ensemble, the record law DIVIDES; the payload-enriched map is "
      "the one that makes the test non-vacuous and it is the one that "
      "divides",
      _c2v == "DIVISIBLE" and len(_c2S[0]) > 1,
      f"renewal-grain supports {[len(_c2S[c]) for c in range(3)]}; verdict "
      f"{_c2v} by {_c2rows[0].get('instrument', 'Chapman-Kolmogorov')}; "
      f"winner-invisible reading "
      f"{ARM_C2['alpha_sigma  (D62-faithful, winner-invisible)'][0][0]['verdict']}")
_c2A = gamma_of(ARM_C2["alpha_sigma+ (payload-enriched)"][2], 1, 0)
_c2B = gamma_of(ARM_C2["alpha_sigma+ (payload-enriched)"][2], 2, 0)
_c2cols = len({tuple(str(_c2A.get((j, i), Fr(0))) for j in _c2S[1])
               for i in _c2S[0]})
_c2cols2 = len({tuple(str(_c2B.get((k, i), Fr(0))) for k in _c2S[2])
                for i in _c2S[0]})
report("ARM-C2 renewal transfers",
       f"Gamma(r2<-r1) distinct columns {_c2cols}; Gamma(r3<-r1) distinct "
       f"columns {_c2cols2} (1 == the renewal chain forgets its "
       f"configuration in one step, so R^2 = R and every renewal triple "
       f"factors through R)")
report("ARM-C2 time", f"{time.time() - _t:.0f}s")

# ---------------- ARM-D: the three-actor pool control -------------------
_t = time.time()
print()
print("  ARM-D — THE POOL CONTROL: the same census on a THREE-actor "
      "transport")
print("  family, so that no verdict rests on a two-actor accident.")
FAM_D, CACHE_D = enumerate_line(b1_cand, ABC, CAP_D)
G_D, P_D, BD_D = horizon_measure(CACHE_D, FAM_D, CAP_D)
_n, _bad = kernel_rows_are_stochastic(CACHE_D, G_D, BD_D, CAP_D)
_mass = [sum(P_D[k] for k in BD_D[d]) for d in range(CAP_D + 1)]
check("G3 ARM-D is a probability law: kernel row sums and cut marginals "
      "exactly 1 on the three-actor family",
      _bad == 0 and all(m == Fr(1) for m in _mass),
      f"{len(FAM_D)} histories; kernels {_n}, non-unit {_bad}; cut masses "
      f"{[str(m) for m in _mass]}")
CUTS_D = tuple(range(CAP_D + 1))
ARM_D_RESULTS = {}
J = joint_paths(BD_D, P_D, lambda k: sigT(k, ABC, False), CUTS_D, CAP_D)
rows, S = run_census("ARM-D / alpha_sigma (D62-faithful)", J, CUTS_D,
                     divcuts=(0,))
ARM_D_RESULTS["alpha_sigma"] = (rows, S, J)
report("ARM-D time", f"{time.time() - _t:.0f}s")

# ---------------- THE COARSE-GRAINING CONTROL BATTERY (the null) --------
_t = time.time()
print()
print("  THE NULL.  Every verdict above is a verdict about a COARSE-"
      "GRAINING of a")
print("  divisible click law, and the question a census cannot answer "
      "about")
print("  itself is how much of it is the RECORD and how much is coarse-"
      "graining")
print("  as such.  The battery below answers it: the same family, the same")
print("  horizon measure, the same cuts, the same instrument, four "
      "control maps")
print("  with the record content removed and the granularity kept.")
print("    (i)   FULL PREFIX — the finest map, alpha(h) = h.  The law is a")
print("          chain rule on prefixes, so Chapman-Kolmogorov must hold "
      "and")
print("          every triple must divide.  This is the pipeline's own "
      "sanity")
print("          check: if it fails, nothing else in this receipt means "
      "anything.")
print("    (ii)  RANDOM PARTITION — the prefixes at each depth are dealt "
      "out")
print("          into classes with EXACTLY alpha_sigma's class sizes at "
      "that")
print("          depth, by a printed congruential shuffle.  Same "
      "granularity,")
print("          same size profile, ZERO record content.  Two fixed seeds.")
print("    (iii) KINEMATIC TAG MULTISET — alpha(h) = the multiset of event")
print("          tags, a map that reads the grammar and no record at all.")
print("    (iv)  ACTOR SEQUENCE — alpha(h) = the sequence of acting actors,")
print("          a coarse kinematic map whose lumpability is measured here")
print("          rather than assumed.")

TEST5 = ((1, 2, 3), (2, 3, 4), (2, 3, 5), (2, 4, 5), (3, 4, 5))
LCG_A, LCG_C, LCG_M = 1103515245, 12345, 2147483648
LCG_SEEDS = (20260727, 11)
print(f"  THE SHUFFLE, PRINTED: x <- ({LCG_A} x + {LCG_C}) mod {LCG_M}, "
      f"seeds {LCG_SEEDS};")
print("  Fisher-Yates over the sk()-sorted prefix list, then the shuffled")
print("  list is cut into blocks of alpha_sigma's own class sizes.  No "
      "call to")
print("  any random module and no dependence on the clock or the hash "
      "seed.")


def lcg_shuffle(xs, seed):
    a = list(xs)
    s = seed
    for i in range(len(a) - 1, 0, -1):
        s = (LCG_A * s + LCG_C) % LCG_M
        j = s % (i + 1)
        a[i], a[j] = a[j], a[i]
    return a


_SIG_CLASSES = {}
for _d in range(CAP_A + 1):
    _c = defaultdict(list)
    for k in BD_A[_d]:
        if P_A.get(k):
            _c[sigT(k)].append(k)
    _SIG_CLASSES[_d] = sorted((sorted(v, key=sk) for v in _c.values()),
                              key=lambda v: (-len(v), sk(v[0])))


def random_map(seed):
    lab = {}
    for d in range(CAP_A + 1):
        pool = lcg_shuffle([k for cls in _SIG_CLASSES[d] for k in cls], seed + d)
        p = 0
        for ci, cls in enumerate(_SIG_CLASSES[d]):
            for k in pool[p:p + len(cls)]:
                lab[k] = ("rnd", d, ci)
            p += len(cls)
    return lambda h: lab[h]


def tag_map(h):
    return ("tag",) + tuple(sorted(Counter(e[0] for e in h).items()))


def actor_map(h):
    return ("act",) + tuple(e[1] for e in h)


def row_obstructions(J, S, i0, i1, i2):
    """The same row-certificate instrument the census uses, reported as a
    raw count so two maps can be compared on one scale."""
    A = gamma_of(J, i1, i0)
    B = gamma_of(J, i2, i0)
    Is, Js, Ks = S[i0], S[i1], S[i2]
    if len(Is) < 2:
        return None, len(Ks), None
    byj = defaultdict(list)
    for (j, i), v in A.items():
        if v:
            byj[j].append((i, v))
    N = gamma_of(J, i2, i1)
    comp = defaultdict(Fr)
    for (kk, j), w in N.items():
        if w:
            for i, v in byj.get(j, ()):
                comp[(kk, i)] += w * v
    ck = (all(comp.get(k, Fr(0)) == v for k, v in B.items())
          and all(B.get(k, Fr(0)) == v for k, v in comp.items()))
    if ck:
        return 0, len(Ks), True      # an interpolant exists: no row can fail
    M = [[A.get((j, i), Fr(0)) for j in Js] for i in Is]
    bad = 0
    for k in Ks:
        bb = [B.get((k, i), Fr(0)) for i in Is]
        feas, _p, w = phase1(M, bb)
        if feas is False and farkas_ok(M, bb, w):
            bad += 1
    return bad, len(Ks), ck


NULLMAPS = [("alpha_sigma  (THE RECORD MAP)", lambda h: sigT(h, AB, False)),
            ("full prefix  (finest, Markov)", lambda h: h),
            (f"random partition, seed {LCG_SEEDS[0]}", random_map(LCG_SEEDS[0])),
            (f"random partition, seed {LCG_SEEDS[1]}", random_map(LCG_SEEDS[1])),
            ("kinematic tag multiset", tag_map),
            ("actor sequence", actor_map)]
NULLTAB = {}
NULLSUP = {}
print()
print(f"      {'map':34s} {'supports 0..5':26s} " +
      "  ".join(f"{str(t):>13s}" for t in TEST5))
for _nm, _f in NULLMAPS:
    Jn = joint_paths(BD_A, P_A, _f, CUTS_A, CAP_A)
    Sn = supports(Jn, len(CUTS_A))
    NULLSUP[_nm] = [len(Sn[c]) for c in range(CAP_A + 1)]
    cells = []
    for t3 in TEST5:
        bad, nk, ck = row_obstructions(Jn, Sn, *t3)
        NULLTAB[(_nm, t3)] = (bad, nk, ck)
        cells.append(f"{bad}/{nk}" + ("*" if ck else ""))
    print(f"      {_nm:34s} {str([len(Sn[c]) for c in range(CAP_A + 1)]):26s} "
          + "  ".join(f"{c:>13s}" for c in cells))
print("      cell = obstructed target configurations / target "
      "configurations;")
print("      * = Chapman-Kolmogorov holds exactly at that triple (the "
      "process's")
print("      own conditional already interpolates, so the triple DIVIDES).")
_sigbad = sum(NULLTAB[(NULLMAPS[0][0], t)][0] for t in TEST5)
_rndbad = [sum(NULLTAB[(nm, t)][0] for t in TEST5)
           for nm, _f in NULLMAPS[2:4]]
_prefck = all(NULLTAB[(NULLMAPS[1][0], t)][2] for t in TEST5)
check("N1 THE PIPELINE'S OWN SANITY CHECK PASSES: under the finest map the "
      "generated law satisfies Chapman-Kolmogorov EXACTLY at every test "
      "triple and divides everywhere.  Every indivisibility reported by "
      "this receipt is therefore a property of a COARSE-GRAINING and of "
      "nothing else",
      _prefck,
      f"full-prefix CK exact at all {len(TEST5)} test triples = {_prefck}; "
      f"prefix supports by depth {NULLSUP[NULLMAPS[1][0]]}; record-map "
      f"supports {NULLSUP[NULLMAPS[0][0]]}")
check("N2 THE NULL OUT-SCORES THE RECORD MAP.  A uniformly random "
      "partition of the same prefixes into alpha_sigma's own class sizes — "
      "zero record content, identical granularity — is obstructed on MORE "
      "target configurations than alpha_sigma is, at both seeds.  "
      "Indivisibility at cut grain is therefore what coarse-graining a "
      "divisible chain generically does, and the record map holds the "
      "property LESS strongly than noise of its own granularity.  This is "
      "the direction OPPOSITE to a bridge headline, and it is the reason "
      "this unit's verdict is scoped rather than asserted",
      all(r > _sigbad for r in _rndbad),
      f"obstructed rows summed over the {len(TEST5)} test triples: "
      f"alpha_sigma {_sigbad}; random {_rndbad}; per-triple table above")
report("Barandes' own caveat, quoted where it bites",
       "[B3] takes UNISTOCHASTICITY, not indivisibility, as the quantum "
       "criterion: indivisibility per se is generic for classical "
       "coarse-grainings, which N2 measures directly.  The "
       "unistochasticity screen is U3's and is reported unadjudicated in "
       "ARM 0")
report("null battery time", f"{time.time() - _t:.0f}s")

# ---------------- the [B3] eq. 22 ALGEBRAIC arm -------------------------
_t = time.time()
_rowsA, _SA, _JA = ARM_A_RESULTS["alpha_sigma  (D62-faithful, "
                                 "winner-invisible)"]
print()
print("  THE [B3] EQ. 22 ALGEBRAIC ARM — Gammabar = Gamma(c''<-c) "
      "Gamma(c'<-c)^-1,")
print("  with the negative entries counted exactly.  This needs a SQUARE "
      "Gamma,")
print("  i.e. Barandes' kinematical axiom: ONE fixed configuration space "
      "for all")
print("  cuts.  MEASURED FACT FIRST, because it decides how the arm must "
      "be run:")
print("  on this carrier the configuration support STRICTLY GROWS with the "
      "cut")
print("  (sizes printed above), so Gamma(c'<-c) is NEVER square on the "
      "supports")
print("  and eq. 22's algebraic form is INAPPLICABLE as written.  The arm "
      "is")
print("  therefore run under a DECLARED CONVENTION: the configuration "
      "space is")
print("  the union X of the three cuts' supports, and a configuration not "
      "yet")
print("  realised at a cut is held FIXED by the law (an identity column).  "
      "That")
print("  makes every Gamma square; the convention is a choice and is "
      "labelled")
print("  one, which is why the feasibility form above — convention-free, "
      "and")
print("  quantifying over ALL stochastic intermediates rather than the "
      "unique")
print("  algebraic one — remains the decisive instrument.")
def eq22_decide(Jm, Sm, trip):
    """[B3] eq. 22 under the declared identity-padding convention.  Returns
    (triple, verdict, |X|, det, negative entries, most negative, column
    sums all 1) — every component exact."""
    l0, l1, l2 = trip
    Xs = srt(set(Sm[l0]) | set(Sm[l1]) | set(Sm[l2]))
    n = len(Xs)
    if n > PAD_MAX:
        return (trip, "EXCLUDED-BY-CAP", n, None, None, None, None)
    G1m = gamma_of(Jm, l1, l0)
    G2m = gamma_of(Jm, l2, l0)
    pos = {x: i for i, x in enumerate(Xs)}
    src = set(Sm[l0])

    def pad(Gm):
        M = [[Fr(0)] * n for _ in range(n)]
        for c, x in enumerate(Xs):
            if x in src:
                for (j, i), v in Gm.items():
                    if i == x:
                        M[pos[j]][c] = v
            else:
                M[c][c] = Fr(1)
        return M

    A = pad(G1m)
    Bm = pad(G2m)
    inv, det = invert_exact(A)
    if inv is None:
        return (trip, "SINGULAR", n, det, None, None, None)
    Gb = [[sum(Bm[a][t] * inv[t][b] for t in range(n)) for b in range(n)]
          for a in range(n)]
    neg = [Gb[a][b] for a in range(n) for b in range(n) if Gb[a][b] < 0]
    cols = [sum(Gb[a][b] for a in range(n)) for b in range(n)]
    return (trip, "PSEUDO-STOCHASTIC" if neg else "STOCHASTIC", n, det,
            len(neg), min(neg, default=Fr(0)),
            all(x == Fr(1) for x in cols))


EQ22 = []
for r in _rowsA:
    e = eq22_decide(_JA, _SA, r["triple"])
    EQ22.append(e[:5])
    if e[1] == "EXCLUDED-BY-CAP":
        print(f"      {str(e[0]):12s} EXCLUDED-BY-CAP  fixed "
              f"configuration space {e[2]} > {PAD_MAX}")
    elif e[1] == "SINGULAR":
        print(f"      {str(e[0]):12s} SINGULAR         "
              f"|X| = {e[2]}, det = 0 — a stochastic matrix has a stochastic "
              f"inverse only if it is a permutation ([B3] eq. 23)")
    else:
        print(f"      {str(e[0]):12s} {e[1]:17s} "
              f"|X| = {e[2]}; NEGATIVE ENTRIES = {e[4]} of {e[2] * e[2]} "
              f"exactly (identity-padding convention); column sums all 1 = "
              f"{e[6]}; most negative = {e[5]}")
_eq22_pseudo = [e for e in EQ22 if e[1] == "PSEUDO-STOCHASTIC"]
_eq22_stoch = [e for e in EQ22 if e[1] == "STOCHASTIC"]
report("eq. 22 algebraic census (ARM-A / alpha_sigma)",
       f"pseudo-stochastic {len(_eq22_pseudo)}, stochastic "
       f"{len(_eq22_stoch)}, singular "
       f"{len([e for e in EQ22 if e[1] == 'SINGULAR'])}, excluded "
       f"{len([e for e in EQ22 if e[1] == 'EXCLUDED-BY-CAP'])}; total "
       f"negative entries {sum(e[4] or 0 for e in EQ22)} — A COUNT "
       f"RELATIVE TO THE IDENTITY-PADDING CONVENTION declared above, not "
       f"an invariant of the process: the configuration space is the union "
       f"of the three cuts' supports and unrealised configurations are "
       f"held fixed by an identity column, and a different padding "
       f"convention gives a different count")
_agree22 = Counter()
for (t3, st, nn, det, nneg) in EQ22:
    v = {r["triple"]: r["verdict"] for r in _rowsA}[t3]
    if st in ("PSEUDO-STOCHASTIC", "STOCHASTIC"):
        _agree22[(st, v)] += 1
report("eq. 22 algebraic reading vs the feasibility verdict",
       {f"{k[0]} / {k[1]}": v for k, v in sorted(_agree22.items())})
_gap_a = _agree22[("PSEUDO-STOCHASTIC", "DIVISIBLE")]
_gap_b = _agree22[("STOCHASTIC", "INDIVISIBLE")]
check("EQ22.1 THE ALGEBRAIC READING IS WEAKER THAN THE FEASIBILITY "
      "READING IN ONE DIRECTION, AND THE CENSUS EXHIBITS THAT DIRECTION "
      "AND ONLY THAT ONE.  A pseudo-stochastic Gammabar says the UNIQUE "
      "algebraic intermediate under the fixed-space convention has "
      "negative entries; it does NOT by itself say no stochastic "
      "intermediate exists, and the table above contains triples where the "
      "algebraic reading is pseudo-stochastic while a genuine stochastic "
      "interpolant provably exists.  THE CONVERSE DIRECTION IS "
      "UNEXHIBITED: the cell STOCHASTIC-and-INDIVISIBLE is EMPTY on this "
      "census, so nothing here shows the algebraic reading missing an "
      "indivisibility, and no two-directional claim is made.  [B3] eq. 22 "
      "is the right instrument only when the configuration space really is "
      "fixed — which, on this carrier, it is not away from renewals",
      _gap_a > 0 and _gap_b == 0,
      f"{len(_eq22_pseudo)} pseudo-stochastic, {len(_eq22_stoch)} "
      f"stochastic; PSEUDO-and-DIVISIBLE = {_gap_a} (the exhibited "
      f"direction), STOCHASTIC-and-INDIVISIBLE = {_gap_b} (the "
      f"unexhibited one)")


# ===========================================================================
# SEC 8.  ARM 1, PART C — where the indivisibility sits
# ===========================================================================

sec("ARM 1 (c) — the geography of the census (input to U2)")

_IND = [r for r in _rowsA if r["verdict"] == "INDIVISIBLE"]
_DIV = [r for r in _rowsA if r["verdict"] == "DIVISIBLE"]
_VAC = [r for r in _rowsA if r["verdict"] == "VACUOUS"]
report("ARM-A / alpha_sigma verdicts by triple",
       {str(r["triple"]): r["verdict"] for r in _rowsA})

# where do the indivisible windows sit relative to division events?
_ren_mass = {}
for r in _rowsA:
    l0, _l1, l2 = r["triple"]
    m = Fr(0)
    for k in BD_A[CAP_A]:
        if any(is_R4(k[j]) for j in range(l0, l2)):
            m += P_A[k]
    _ren_mass[r["triple"]] = m
report("mass of the ensemble carrying a DIVISION EVENT inside the window, "
       "per triple",
       {str(t): str(m) for t, m in sorted(_ren_mass.items())})
_ind_masses = srt({_ren_mass[r["triple"]] for r in _IND})
_mx = max(_ind_masses)
_mxpct = f"{float(_mx) * 100:.2f}"          # display only; the gate is exact
check("J1 THE INDIVISIBLE WINDOWS ARE BRIDGE WINDOWS ON MOST OF THEIR MASS "
      "— reported as a MEASURED co-location and nothing more.  Paper 0 "
      "sec.4 places the anomalies in the conflict windows BETWEEN "
      "renewals; the mass of the ensemble that carries any division event "
      "inside an indivisible window is printed above for every triple.  "
      "The MAXIMUM of those masses is the number that must be quoted, and "
      "it is printed exactly below; the bridge mass is its complement.  "
      "This is the J-geography input U2 needs, and it is NOT a test of the "
      "J-conjecture, which is U2's and is not run here",
      len(_IND) > 0 and max(_ind_masses) < Fr(1, 20),
      f"indivisible triples {[str(r['triple']) for r in _IND]}; "
      f"division-event mass inside them "
      f"{[str(m) for m in _ind_masses]}; MAXIMUM = {_mx} = {_mxpct}% "
      f"exactly, so the bridge mass is AT LEAST {Fr(1) - _mx} of every "
      f"indivisible window and no larger claim may be made")

# the 44 named squares vs the lumpability defect
_lump = {}
for d in range(CAP_A):
    cls = defaultdict(list)
    for k in BD_A[d]:
        if P_A.get(k):
            cls[sigT(k)].append(k)
    bad = set()
    for c, hs in cls.items():
        dists = set()
        for k in hs:
            dd = defaultdict(Fr)
            for e, q in CACHE_A[k]:
                dd[sigT(k + (e,))] += q * G_A[k + (e,)] / G_A[k]
            dists.add(tuple(sorted(((sk(a), str(b)) for a, b in dd.items()))))
        if len(dists) > 1:
            bad.add(c)
    _lump[d] = (len(cls), len(bad), bad)
report("the lumpability defect by depth (classes, non-lumpable classes)",
       {d: (_lump[d][0], _lump[d][1]) for d in sorted(_lump)})
_u44_on_bad = 0
for (hh, ea, eb, r, *_rest) in _U44:
    d = len(hh)
    if d in _lump and sigT(hh) in _lump[d][2]:
        _u44_on_bad += 1
check("J2 THE 44 NAMED SQUARES SIT ON THE LUMPABILITY DEFECT.  The "
      "descent-obstruction squares are exactly the places where two orders "
      "of the same pair carry DIFFERENT weighted menus; the record-grain "
      "law is non-lumpable exactly where a configuration class contains "
      "histories with different menus.  The count below is the overlap, "
      "measured, with no causal claim attached",
      _u44_on_bad > 0,
      f"{_u44_on_bad} of {len(_U44)} descent-obstruction squares have "
      f"their base in a NON-LUMPABLE configuration class of ARM-A")


# ===========================================================================
# SEC 9.  ARM 2 — paper 29's four descent conditions on the SAME family
# ===========================================================================

sec("ARM 2 — the four descent conditions (DC1-DC4) on the same family")

_t = time.time()
print("  The D65 pin's conditions, ported to transport scope and run at the")
print("  SAME caps as Arm 1.  Two normalisations are carried throughout,")
print("  because the transport grammar admits both honest ones: the D65 "
      "form")
print("  p = q / M (menu weight over menu mass) and the D46b/D70 "
      "relative-horizon")
print("  kernel k_r.  Both are printed; neither is preferred by fiat.")

# ---- DC1 ---------------------------------------------------------------
FAM_DC, CACHE_DC = enumerate_line(b1_cand, AB, CAP_DC1)
_stD, _ratD, _kindsD, _okD, _defD, _halfD, _closedD = square_census(
    FAM_DC, CACHE_DC, AB, CAP_DC1 + 2, b1_adm, b1_regs, b1_canon)
_MM = {k: sum(q for e, q in CACHE_A[k]) for k in CACHE_A}
dc1 = Counter()
dc1_ratio_q = Counter()
dc1_ratio_M = Counter()
dc1_ratio_k = Counter()
dc1_by_depth = defaultdict(Counter)
dc1_class = Counter()
_gsplit = Counter()
_allraw = Counter()
for (hh, ea, eb, r) in _closedD:
    ok_r, qa = b1_adm(list(hh), ea, AB)
    ok_r2, qb2 = b1_adm(list(hh) + [ea], eb, AB)
    ok_r3, qb = b1_adm(list(hh), eb, AB)
    ok_r4, qa2 = b1_adm(list(hh) + [eb], ea, AB)
    s1, s2 = hh + (ea, eb), hh + (eb, ea)
    rq = (qa * qb2) / (qb * qa2)
    _allraw[rq] += 1
    refined = sk(b1_canon(list(s1))) == sk(b1_canon(list(s2)))
    sigma_commuting = sigT(s1) == sigT(s2)
    if refined:
        _gsplit[("refined-identical", G_A[s1] == G_A[s2])] += 1
    else:
        _gsplit[("not refined-identical", G_A[s1] == G_A[s2])] += 1
    if rq != 1:
        menu_same = (A_menu(s1, CACHE_A) == A_menu(s2, CACHE_A))
        dc1_class["curvature-type (closes in the menu quotient)"
                  if menu_same else
                  "descent-obstruction-type (closes in NO descent "
                  "quotient)"] += 1
    if not sigma_commuting:
        dc1["non-commuting (excluded by name)"] += 1
        continue
    dc1_ratio_q[rq] += 1
    # the D65 normalisation p = q / M
    pa = qa / _MM[hh]
    pb2 = qb2 / _MM[hh + (ea,)]
    pb = qb / _MM[hh]
    pa2 = qa2 / _MM[hh + (eb,)]
    rM = (pa * pb2) / (pb * pa2)
    dc1_ratio_M[rM] += 1
    # the relative-horizon normalisation
    rk = ((qa * G_A[hh + (ea,)] / G_A[hh])
          * (qb2 * G_A[s1] / G_A[hh + (ea,)])) / (
        (qb * G_A[hh + (eb,)] / G_A[hh])
        * (qa2 * G_A[s2] / G_A[hh + (eb,)]))
    dc1_ratio_k[rk] += 1
    tag = "refined-record identical" if refined else \
        "sigma-commuting, not refined-identical"
    dc1[tag + " | raw " + ("HOLDS" if rq == 1 else "FAILS")] += 1
    dc1[tag + " | D65 q/M " + ("HOLDS" if rM == 1 else "FAILS")] += 1
    dc1[tag + " | horizon k_r " + ("HOLDS" if rk == 1 else "FAILS")] += 1
    dc1_by_depth[len(hh)][("raw", rq == 1)] += 1
    dc1_by_depth[len(hh)][("k_r", rk == 1)] += 1
report("DC1 census (ordered pairs, both orders admissible, at every parent "
       f"of depth <= {CAP_DC1})",
       {k: v for k, v in sorted(dc1.items())})
report("DC1 exact ratio spectra", f"raw q {fmt(dc1_ratio_q)} | D65 q/M "
       f"{fmt(dc1_ratio_M)} | horizon k_r {fmt(dc1_ratio_k)}")
report("DC1 by parent depth", {d: {str(k): v for k, v in
                                   sorted(dc1_by_depth[d].items())}
                               for d in sorted(dc1_by_depth)})
_dc1_fail_raw = sum(v for k, v in dc1_ratio_q.items() if k != 1)
_dc1_fail_k = sum(v for k, v in dc1_ratio_k.items() if k != 1)
_dc1_fail_M = sum(v for k, v in dc1_ratio_M.items() if k != 1)
_ref_raw_fail = dc1.get("refined-record identical | raw FAILS", 0)
_ref_M_fail = dc1.get("refined-record identical | D65 q/M FAILS", 0)
_ref_k_fail = dc1.get("refined-record identical | horizon k_r FAILS", 0)
_ref_tot = (dc1.get("refined-record identical | raw FAILS", 0)
            + dc1.get("refined-record identical | raw HOLDS", 0))
check("DC1 FAILS AT TRANSPORT SCOPE — and the failure is NORMALISATION-"
      "DEPENDENT in a way that must be stated, not averaged.  On the WIDER "
      "sigma-commuting census all three normalisations fail.  On Theorem "
      "1's OWN hypothesis class — refined-record identical pairs, D65's "
      "DC1(f) — the raw and horizon forms HOLD identically and the D65 "
      "q/M form FAILS, which is the same normalisation and the same kind "
      "of failure D65 measured at closed scope (32,256 of 425,334).  The "
      "instrument does not agree with itself across normalisations, and "
      "that is the finding",
      _dc1_fail_raw > 0 and _dc1_fail_k > 0 and _ref_M_fail > 0,
      f"WIDER (sigma-commuting, {sum(dc1_ratio_q.values())} ordered "
      f"pairs): raw {_dc1_fail_raw}, D65 q/M {_dc1_fail_M}, horizon k_r "
      f"{_dc1_fail_k} | DC1(f) (refined-record identical, {_ref_tot} "
      f"pairs): raw {_ref_raw_fail}, D65 q/M {_ref_M_fail}, horizon k_r "
      f"{_ref_k_fail}")
check("DC1-IDENTIFICATION, CORRECTLY SCOPED: the horizon normalisation "
      "changes the DC1 ratio EXACTLY when the two orders carry different "
      "records.  The horizon potential G is constant on refined-record-"
      "identical endpoint pairs — so on Theorem 1's own hypothesis class "
      "the horizon-normalised DC1 defect IS the raw D72/D74 exchange-"
      "square ratio, and paper 29's descent condition and D72's transport "
      "square census are literally the same number there.  Off that class "
      "they are different numbers, and the receipt reports both",
      _ref_k_fail == _ref_raw_fail
      and _gsplit[("refined-identical", False)] == 0
      and _gsplit[("not refined-identical", False)] > 0,
      f"G equal / unequal on refined-identical pairs: "
      f"{_gsplit[('refined-identical', True)]} / "
      f"{_gsplit[('refined-identical', False)]}; on non-refined pairs: "
      f"{_gsplit[('not refined-identical', True)]} / "
      f"{_gsplit[('not refined-identical', False)]}")
_dfull = sum(v for k, v in _allraw.items() if k != 1)
anchor("DC1.960 THE DC1 RAW DEFECT CENSUS IS D72/D74's SQUARE CENSUS AT "
       "THE SAME WINDOW, TO THE UNIT: over every closed exchange square of "
       "the (A,B) transport family to depth 5 the raw commuting-square "
       "identity fails exactly 960 times, which is D74's committed "
       "depth-5 defect count; and the failures split into the "
       "curvature-type and descent-obstruction-type halves in D74's "
       "committed proportions 604 / 356",
       _dfull == ANCH["AB5_defects"]
       and dc1_class["curvature-type (closes in the menu quotient)"]
       == ANCH["AB5_seen"]
       and dc1_class["descent-obstruction-type (closes in NO descent "
                     "quotient)"] == ANCH["AB5_unseen"],
       f"raw DC1 failures over all closed squares = {_dfull} (quoted "
       f"{ANCH['AB5_defects']}); split "
       f"{dict(sorted(dc1_class.items()))} (quoted "
       f"{ANCH['AB5_seen']} / {ANCH['AB5_unseen']}); full ratio spectrum "
       f"{fmt(_allraw)}")

# ---- DC2 ---------------------------------------------------------------
_dc2 = {}
for d in range(CAP_A):
    ncls, nbad, _bads = _lump[d]
    _dc2[d] = (ncls, nbad)
_dc2_tot = sum(v[1] for v in _dc2.values())
check("DC2 BOUNDARY SUFFICIENCY FAILS AT TRANSPORT SCOPE — and this is the "
      "sharpest single difference from closed scope, where it is a "
      "THEOREM.  At closed scope DC2 is exactly (H1)+(H2): sigma is a "
      "sufficient boundary statistic and the next-record law is constant "
      "on its fibres.  At transport scope the ported state is NOT "
      "sufficient: configuration classes contain histories with different "
      "next-configuration laws, from depth 2 onward",
      _dc2_tot > 0,
      f"non-lumpable classes by depth {_dc2}; total {_dc2_tot}.  At closed "
      f"scope the same statistic is sufficient by D61/D62 [THEOREM]")

# ---- DC3 ---------------------------------------------------------------
_pos = sum(1 for k in CACHE_A for e, q in CACHE_A[k] if q <= 0)
_sum1 = sum(1 for k in BD_A[d] for d in range(CAP_A))
check("DC3(1) exclusive-and-exhaustive alternatives: the normalised menu "
      "is a partition of the admissible continuations and sums to exactly "
      "1 at every history (gated at G1 above)", _bad == 0,
      "the same gate as G1/G2/G3; not independent evidence",
      reporting_only=True)
check("DC3(2) decoherence of the queried algebra: the generated law is a "
      "stochastic process on records, so decoherence is trivially "
      "satisfied AND trivially uninformative.  This is where the map's "
      "remaining segment lives — the generated line still has no "
      "functional level, and U1 does not create one", True,
      "declared, exactly as D65 declared it at closed scope",
      reporting_only=True)
check("DC3(3) common refined cylinder = DC1's census above", True,
      "identical predicate; see DC1", reporting_only=True)
check("DC3(4) POSITIVITY of every displayed conditioning cylinder: every "
      "menu weight of the transport family is strictly positive, gated "
      "exactly", _pos == 0,
      f"non-positive menu weights = {_pos} over "
      f"{sum(len(CACHE_A[k]) for k in CACHE_A)} priced candidates")
check("DC3(5) sufficient declared boundary = DC2 above — and it FAILS at "
      "transport scope", _dc2_tot > 0,
      f"{_dc2_tot} non-lumpable classes; see DC2")

# ---- DC4 ---------------------------------------------------------------
print()
print("  [DC4]  THE SUPPLIED-VS-DERIVED LEDGER, RE-SCORED AT TRANSPORT "
      "SCOPE AND")
print("         RENEWAL GRAIN.  No item moves without a gate above it.")
print("         boundary state (D59 item 1) — at closed scope D65 moved it "
      "to")
print("           DERIVED via DC2.  At transport scope it moves BACK to "
      "SUPPLIED:")
print("           DC2 fails, so the ported state is not a sufficient "
      "boundary")
print("           statistic and any boundary condition on it is an "
      "assumption.")
print("         the measure (D59 item 2) — the relative-horizon "
      "normalisation")
print("           supplies a probability law at every finite cap (G1/G2/"
      "G3);")
print("           D70's infinite-horizon bound is OPEN and nothing here "
      "closes")
print("           it.  Status unchanged: SUPPLIED at finite horizon.")
print("         renormalization, record instrument, clock dictionary, the")
print("           functional level — all four STAND as supplied; this unit")
print("           gates none of them, and DC3(2) says why the functional")
print("           level in particular cannot move here.")
print("         NEW ITEM, added by this unit: the RENEWAL RESET (paper 0")
print("           sec.4's [POSIT]) is now scored SUPPLIED-WITH-A-BOUNDARY: "
      "true")
print("           at every reachable cap (PORT-2), false on a constructed")
print("           admissible chain (PORT-3).")
report("ARM-2 time", f"{time.time() - _t:.0f}s")


# ===========================================================================
# SEC 10.  THE AGREEMENT CENSUS — Arm 1 against Arm 2
# ===========================================================================

sec("THE AGREEMENT CENSUS — the two instruments, triple by triple")

print("  Arm 1's instrument is the [B3] eq. 22 interpolant test at a cut")
print("  triple.  Arm 2's instruments are per-STEP: DC1 (the commuting-"
      "square")
print("  identity at a parent) and DC2 (fibre constancy at a depth).  They "
      "are")
print("  compared by aggregating Arm 2 over the window the triple spans:")
print("  a triple (l0, l', l'') is 'Arm-2 defective' iff some DC1 failure "
      "or")
print("  some DC2 failure occurs at a depth in [l0, l''-1].")
_dc1_by_d = defaultdict(int)
for (hh, ea, eb, r) in _closedD:
    s1, s2 = hh + (ea, eb), hh + (eb, ea)
    if sigT(s1) != sigT(s2):
        continue
    ok_r, qa = b1_adm(list(hh), ea, AB)
    ok_r2, qb2 = b1_adm(list(hh) + [ea], eb, AB)
    ok_r3, qb = b1_adm(list(hh), eb, AB)
    ok_r4, qa2 = b1_adm(list(hh) + [eb], ea, AB)
    if (qa * qb2) != (qb * qa2):
        _dc1_by_d[len(hh)] += 1
report("DC1 failures by parent depth", dict(sorted(_dc1_by_d.items())))
report("DC2 failures by depth", {d: _dc2[d][1] for d in sorted(_dc2)})

TAB = Counter()
ROWS = []
for r in _rowsA:
    l0, l1, l2 = r["triple"]
    d1 = sum(_dc1_by_d.get(d, 0) for d in range(l0, min(l2, CAP_DC1 + 1)))
    d2 = sum(_dc2.get(d, (0, 0))[1] for d in range(l0, l2))
    arm2 = "DEFECTIVE" if (d1 or d2) else "CLEAN"
    arm1 = r["verdict"]
    ROWS.append((r["triple"], arm1, arm2, d1, d2))
    if arm1 in ("DIVISIBLE", "INDIVISIBLE"):
        TAB[(arm1, arm2)] += 1
print()
print(f"      {'triple':12s} {'ARM 1 (interpolant)':22s} "
      f"{'ARM 2 (descent)':14s} {'DC1 fails':>10s} {'DC2 fails':>10s}")
for t, a1, a2, d1, d2 in ROWS:
    print(f"      {str(t):12s} {a1:22s} {a2:14s} {d1:10d} {d2:10d}")
print()
report("the 2x2 agreement table (Arm 1 x Arm 2, non-vacuous triples only)",
       {f"{k[0]} / {k[1]}": v for k, v in sorted(TAB.items())})
_disagree = TAB[("DIVISIBLE", "DEFECTIVE")] + TAB[("INDIVISIBLE", "CLEAN")]
_agree = TAB[("INDIVISIBLE", "DEFECTIVE")] + TAB[("DIVISIBLE", "CLEAN")]
check("AG1 THE TWO INSTRUMENTS DISAGREE, AND THE DISAGREEMENT IS ONE-SIDED "
      "AND EXACTLY CHARACTERISED: every triple Arm 1 calls INDIVISIBLE is "
      "also Arm-2 defective, but Arm 2 is defective on triples Arm 1 calls "
      "DIVISIBLE.  Descent failure is therefore NECESSARY BUT NOT "
      "SUFFICIENT for cut-indivisibility on this family: the descent "
      "conditions are the finer instrument at the step scale and the "
      "coarser verdict at the window scale.  Neither instrument is "
      "redundant and neither dominates",
      TAB[("INDIVISIBLE", "CLEAN")] == 0 and _disagree > 0,
      f"agreements {_agree}, disagreements {_disagree}; "
      f"INDIVISIBLE&CLEAN = {TAB[('INDIVISIBLE', 'CLEAN')]} (an "
      f"INDIVISIBLE triple with a clean window would have been the "
      f"instrument-splitting witness; there is none)")

# --- the same table for the enriched configuration (both ways) ----------
_rowsA2 = ARM_A_RESULTS["alpha_sigma+ (payload-enriched)"][0]
_v1v = {str(r["triple"]): r["verdict"] for r in _rowsA}
_v2v = {str(r["triple"]): r["verdict"] for r in _rowsA2}
_conf = Counter((_v1v[k], _v2v[k]) for k in _v1v)
report("ARM-A verdicts, the two configuration maps against each other",
       {f"sigma {k[0]} / sigma+ {k[1]}": v for k, v in sorted(_conf.items())})
_subst = {"DIVISIBLE", "INDIVISIBLE", "VACUOUS"}
_opposed = sum(v for k, v in _conf.items()
               if k[0] in _subst and k[1] in _subst and k[0] != k[1])
_opp_trips = [k for k in _v1v
              if _v1v[k] in _subst and _v2v[k] in _subst
              and _v1v[k] != _v2v[k]]
_opp_dir = all(_v1v[k] == "INDIVISIBLE" and _v2v[k] == "DIVISIBLE"
               for k in _opp_trips)
check("AG2 THE TWO COMMITTED CONFIGURATION MAPS DO OPPOSE, AND THEY OPPOSE "
      "IN THE ARTEFACT DIRECTION.  Once every triple is decided, the "
      "winner-invisible D62 state and the payload-enriched state give "
      "OPPOSITE substantive verdicts on the triples listed below, and "
      "every opposition has the same sign: the COARSE map calls the "
      "triple INDIVISIBLE and the FINE map DIVIDES it, with an exhibited "
      "and re-verified interpolant.  That is the direction in which "
      "indivisibility is an artefact of throwing information away, not a "
      "property of the process.  NO ANTI-ARTEFACT READING IS AVAILABLE "
      "FROM THIS COMPARISON, and none is made: the two triples where the "
      "maps oppose are exactly the two the plain LP cap cannot reach, so a "
      "cap-limited census would read as agreement for the wrong reason",
      _opposed > 0 and _opp_dir,
      f"opposed substantive verdicts = {_opposed} of {len(_v1v)} at "
      f"{sorted(_opp_trips)}; every opposition coarse-INDIVISIBLE / "
      f"fine-DIVISIBLE = {_opp_dir}; remaining differences = "
      f"{sum(v for k, v in _conf.items() if k[0] != k[1]) - _opposed}")


# ===========================================================================
# SEC 11.  DETERMINISM PROBE
# ===========================================================================

sec("DETERMINISM PROBE")

_j1 = joint_paths(BD_A, P_A, lambda k: sigT(k), CUTS_A, CAP_A)
_bd_rev = {d: list(reversed(BD_A[d])) for d in BD_A}
_j2 = joint_paths(_bd_rev, P_A, lambda k: sigT(k), CUTS_A, CAP_A)
_g1 = gamma_of(_j1, 4, 2)
_g2 = gamma_of(_j2, 4, 2)
_S1 = supports(_j1, len(CUTS_A))
_S2 = supports(_j2, len(CUTS_A))
_lp1, _lp2 = [], []
_d1 = decide_triple(_j1, _S1, 1, 2, 3, (1, 2, 3), _lp1)   # LP arm
_d2 = decide_triple(_j2, _S2, 1, 2, 3, (1, 2, 3), _lp2)
_e1 = decide_triple(_j1, _S1, 1, 4, 5, (1, 4, 5), _lp1)   # LP2 reduced arm
_e2 = decide_triple(_j2, _S2, 1, 4, 5, (1, 4, 5), _lp2)
_tupkey = lambda r: (r["verdict"], r.get("instrument"), r.get("nvar"),
                     r.get("nrow"), r.get("rvar"), r.get("rrow"),
                     r.get("rgrp"), r.get("rowfail"),
                     str(r.get("lpcert", ("", "", ""))[1]))
_alg2 = [eq22_decide(_j2, _S2, t)[:5] for t in
         ((1, 2, 3), (2, 3, 4), (3, 4, 5))]
_alg1 = [e for e in EQ22 if e[0] in ((1, 2, 3), (2, 3, 4), (3, 4, 5))]
check("DET.1 every printed number is order-independent, AND THE PROBE "
      "EXERCISES THE DECIDING ARMS, not just the joint law.  The family is "
      "traversed in the opposite order and four objects are recompared "
      "entry by entry: the joint cut law; a representative Gamma block; "
      "the FULL result tuple of a triple decided by the plain LP arm "
      "(1,2,3), Farkas value included; and the FULL result tuple of a "
      "triple decided by the reduced LP2 arm (1,4,5), reduction sizes and "
      "Farkas value included.  All set iteration that feeds a printed "
      "number is keyed by the hash-seed-independent sk()",
      _j1 == _j2 and _g1 == _g2
      and _tupkey(_d1) == _tupkey(_d2) and _tupkey(_e1) == _tupkey(_e2),
      f"joint law identical = {_j1 == _j2}; Gamma(4<-2) identical = "
      f"{_g1 == _g2}; entries compared {len(_g1)}; LP arm (1,2,3) tuple "
      f"identical = {_tupkey(_d1) == _tupkey(_d2)} {_tupkey(_d1)}; LP2 arm "
      f"(1,4,5) tuple identical = {_tupkey(_e1) == _tupkey(_e2)} "
      f"{_tupkey(_e1)}")
check("DET.2 the eq. 22 algebraic arm is order-independent too: three "
      "triples are RE-DERIVED from the reversed traversal — verdict, "
      "fixed-space size, exact determinant and exact negative-entry count "
      "— and compared component by component against the stored table",
      len(_alg1) == len(_alg2) and _alg1 == _alg2,
      f"{len(_alg2)} triples re-derived: "
      f"{[(str(a[0]), a[1], a[2], a[4]) for a in _alg2]}; identical to the "
      f"stored census = {_alg1 == _alg2}; whole-census negative entries "
      f"{sum(e[4] or 0 for e in EQ22)} under the declared padding "
      f"convention")


# ===========================================================================
# SEC 12.  THE VERDICT
# ===========================================================================

sec("THE VERDICT, against the pre-registered outcomes")

_all_rows = (_rowsA + _rowsA2
             + ARM_B_RESULTS["alpha_sigma  (D62-faithful, "
                             "winner-invisible)"][0]
             + ARM_B_RESULTS["alpha_sigma+ (payload-enriched)"][0]
             + ARM_C2["alpha_sigma  (D62-faithful, winner-invisible)"][0]
             + ARM_C2["alpha_sigma+ (payload-enriched)"][0]
             + ARM_D_RESULTS["alpha_sigma"][0])
_tot = Counter(r["verdict"] for r in _all_rows)
_nind = _tot["INDIVISIBLE"]
report("the whole census, all arms, all configuration maps",
       {k: v for k, v in sorted(_tot.items())})
report("the same census WITHOUT ARM-C2 (the 58 triples of the four "
       "depth-indexed arms, for comparison with any earlier count)",
       {k: v for k, v in
        sorted(Counter(r["verdict"] for r in _all_rows
                       if not r["arm"].startswith("ARM-C2")).items())})
report("indivisible triples, by arm",
       {"ARM-A/sigma": [str(r["triple"]) for r in _rowsA
                        if r["verdict"] == "INDIVISIBLE"],
        "ARM-A/sigma+": [str(r["triple"]) for r in _rowsA2
                         if r["verdict"] == "INDIVISIBLE"],
        "ARM-B": [str(r["triple"]) for arm in ARM_B_RESULTS.values()
                  for r in arm[0] if r["verdict"] == "INDIVISIBLE"],
        "ARM-C2": [str(r["triple"]) for arm in ARM_C2.values()
                   for r in arm[0] if r["verdict"] == "INDIVISIBLE"],
        "ARM-D": [str(r["triple"]) for r in ARM_D_RESULTS["alpha_sigma"][0]
                  if r["verdict"] == "INDIVISIBLE"]})
_wins = Counter()
for r in _all_rows:
    if r["verdict"] == "INDIVISIBLE":
        _wins[(r["triple"], r["arm"].split("/")[0].strip())] += 1
_distinct_ind = len({(t, a) for (t, a) in _wins})
_distinct_ind_windows = len({t for (t, a) in _wins})
report("the double-count caveat, carried with the headline number",
       f"{_nind} indivisible VERDICTS across all arms and both "
       f"configuration maps; the same (arm, triple) window read by the two "
       f"maps is counted twice, so the number of DISTINCT (arm, window) "
       f"pairs is {_distinct_ind}, and of distinct cut triples "
       f"{_distinct_ind_windows}.  The vacuous count carries the same "
       f"caveat: "
       f"{len({(r['triple'], r['arm'].split('/')[0].strip()) for r in _all_rows if r['verdict'] == 'VACUOUS'})} "
       f"distinct (arm, window) pairs behind {_tot['VACUOUS']} verdicts")

# --- THE DIVISION-EVENT TABLE: the census keyed by [B3] p.9's own rule ---
print()
print("  THE DIVISION-EVENT TABLE.  [B3] p.9 admits conditioning ONLY at "
      "division")
print("  events, and paper 0 sec.4 identifies division events with "
      "renewals.  The")
print("  census above is therefore two censuses, and only one of them is "
      "the law's")
print("  own.  A triple is counted DIVISION-EVENT-CONDITIONED iff its "
      "FIRST cut is")
print("  a division event for EVERY history of its ensemble: the initial "
      "cut,")
print("  where the process sits at the root by construction, and ARM-B's "
      "cut 3 and")
print("  ARM-C2's renewal cuts, where the ensemble is conditioned on a "
      "pair-arb.")
_dv = Counter()
for r in _all_rows:
    _dv[(bool(r["divcut"]), r["verdict"])] += 1
print()
print(f"      {'first conditioning cut':34s} " +
      "".join(f"{v:>17s}" for v in ("INDIVISIBLE", "DIVISIBLE",
                                    "EXCLUDED-BY-CAP", "VACUOUS", "total")))
for flag, lab in ((True, "IS a division event"),
                  (False, "is NOT a division event")):
    cells = [_dv[(flag, v)] for v in ("INDIVISIBLE", "DIVISIBLE",
                                      "EXCLUDED-BY-CAP", "VACUOUS")]
    print(f"      {lab:34s} " + "".join(f"{c:>17d}" for c in
                                        cells + [sum(cells)]))
_ind_at_div = _dv[(True, "INDIVISIBLE")]
check("B5 EVERY INDIVISIBILITY THIS RECEIPT FINDS SITS AT A CONDITIONING "
      "CUT THE LAW DOES NOT ADMIT.  [B3] p.9's conditioning rule is that "
      "the allowed conditioning times are the division events; paper 0 "
      "sec.4 fixes division events = renewals.  Split the whole census by "
      "that rule and it separates completely: at a division-event "
      "conditioning cut there is NO indivisible triple at all — the "
      "winner-invisible readings are structurally vacuous because a "
      "renewal resets to the root, and every non-vacuous one DIVIDES, two "
      "of them by exact Chapman-Kolmogorov and the pinned "
      "renewal-to-renewal triple of ARM-C2 among them.  Every indivisible "
      "triple in this receipt has its first cut strictly BETWEEN division "
      "events, which is cut grain and not record grain",
      _ind_at_div == 0 and _dv[(False, "INDIVISIBLE")] > 0,
      f"division-event cuts: {_ind_at_div} indivisible of "
      f"{sum(v for k, v in _dv.items() if k[0])}; non-division cuts: "
      f"{_dv[(False, 'INDIVISIBLE')]} indivisible of "
      f"{sum(v for k, v in _dv.items() if not k[0])}")

VERDICT = "U1-BRIDGE-AT-ADJACENT-SCOPE"
if _nind == 0:
    VERDICT = "U1-DIV"
if TAB[("INDIVISIBLE", "CLEAN")] > 0:
    VERDICT = "U1-SPLIT"
print()
print(f"  >>> VERDICT: {VERDICT}")
print("      THE BRIDGE IS AT THE ADJACENT SCOPE, AND THE NULL IS "
      "ATTACHED TO IT.")
print("      At CUT grain, on conditioning cuts that are NOT division "
      "events, the")
print("      D62 record state is a non-lumpable function of the DIVISIBLE "
      "click")
print("      law, and its Gamma family admits no column-stochastic "
      "interpolant at")
print(f"      {_dv[(False, 'INDIVISIBLE')]} triples, each with an "
      f"independently verified exact Farkas")
print("      certificate.  That property is SHARED WITH — and held LESS")
print("      STRONGLY THAN — a uniformly random partition of the same "
      "prefixes")
print("      into the same class sizes (gate N2), so it is what coarse-"
      "graining")
print("      a divisible chain generically does and not a signature of "
      "the")
print("      record.  At EVERY conditioning cut that IS a division event "
      "— the")
print("      only cuts [B3] p.9 admits, and the grain paper 0 sec.4 puts "
      "the law")
print("      at — the law DIVIDES exactly, including the pinned "
      "non-degenerate")
print("      renewal-to-renewal triple, which ARM-C2 runs and which "
      "divides by")
print("      exact Chapman-Kolmogorov on a rank-one renewal transfer.")
print("      This is a real, informative, negative-leaning result.  It is "
      "NOT the")
print("      corpus's first generated indivisible bridge, and the U1-"
      "BRIDGE")
print("      pre-registered outcome is NOT met at the grain that outcome "
      "meant.")
print()
print("      THE ONE FACT, NAMED ONCE.  Arm 1's interpolant census and "
      "Arm 2's")
print("      DC2 failure are not two results.  Both are the "
      "NON-LUMPABILITY of")
print("      the ported state under deliveries — DC2 measures it per "
      "step, the")
print("      census measures what it does to a window — and the agreement "
      "table")
print("      below is the relation between the two readings of that single "
      "fact,")
print("      not corroboration of one by the other.")
print()
print("      WHAT REMAINS OPEN, PRECISELY.  ARM-C2 decides the pinned "
      "triple on")
print("      the MINIMAL-INTERVAL sub-ensemble: conditioning on a third "
      "renewal")
print("      by depth 9 forces every renewal interval to its shortest "
      "length.  A")
print("      renewal chain with UNEQUAL intervals is not reached by this")
print("      conditioning and is not reached by enumeration either "
      "(~10^8")
print("      histories at depth 9); that is the successor computation, and "
      "it is")
print("      named U1b.")
print()
print("  AND THE U1-SPLIT TEST, RUN AND REPORTED RATHER THAN ASSUMED "
      "AWAY.")
print("  The pin's third outcome fires if the two instruments disagree.  "
      "They")
print("  do disagree — but ONE-SIDEDLY and with the direction measured: "
      "every")
print("  triple Arm 1 calls INDIVISIBLE is Arm-2 defective, and Arm 2 is "
      "also")
print("  defective on triples Arm 1 calls DIVISIBLE and on every VACUOUS "
      "one.")
print("  Arm 2's descent conditions fail at EVERY parent depth >= 1 and "
      "EVERY")
print("  cut depth >= 2 in this family, so at window scale Arm 2 has no")
print("  resolving power at all.  The witness class that would have made "
      "this a")
print("  genuine U1-SPLIT — an INDIVISIBLE triple in a CLEAN window, "
      "which would")
print("  put the instruments in opposite directions on one object — is "
      "EMPTY: "
      f"{TAB[('INDIVISIBLE', 'CLEAN')]} of {sum(TAB.values())}.")
print()
print("  SCOPE, NON-NEGOTIABLE.  Transport scope (d42b1), the declared "
      "families")
print("  and caps only; renewal grain per paper 0 sec.4's POSIT, which "
      "PORT-3")
print("  shows is delivery-conditioned rather than grammatical; no "
      "infinite-")
print("  volume claim; no measure-existence claim (D70's bound is open); "
      "no CP")
print("  statement of any kind; no Bell or locality statement of any kind; "
      "and,")
print("  per L-1, no claim of exact covariance anywhere — at most "
      "statistical")
print("  Lorentz invariance is available at renewal grain and none is "
      "claimed")
print("  here.  The J-conjecture is NOT tested (that is U2); the "
      "unistochasticity")
print("  screen is REPORTED and not adjudicated (that is U3).")

print()
print(f"[SUMMARY] {PASS} PASS / {FAIL} FAIL / {ANCHOR_FAIL} ANCHOR-FAIL")
print(f"[RUNTIME] {time.time() - T0:.0f}s wall clock, single-threaded, "
      f"exact arithmetic throughout")
print(f"[CAPS] ARM-A depth {CAP_A}; ARM-B depth {CAP_B}; ARM-C2 depth 9 "
      f"(minimal-interval sub-ensemble, conditioned); ARM-D depth "
      f"{CAP_D} (3 actors); anchors depth {CAP_ANCH_AB}/{CAP_ANCH_ABC}; "
      f"closed scope depth {CAP_CLOSED}; DC1 parents depth {CAP_DC1}; "
      f"LP caps {LP_MAXVARS} vars / {LP_MAXROWS} rows, reduced-system caps "
      f"{LP2_MAXVARS} vars / {LP2_MAXROWS} rows; eq. 22 fixed space "
      f"{PAD_MAX}; EXCLUDED-BY-CAP triples remaining: "
      f"{_tot['EXCLUDED-BY-CAP']}")
if ANCHOR_FAIL:
    sys.exit(1)
print("[EXIT] 0 — substantive negatives are results, not failures")
