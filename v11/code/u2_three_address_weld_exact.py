#!/usr/bin/env python3
# Requires Python >= 3.12 (PEP 701 f-strings); run with /opt/homebrew/bin/python3.13.
"""
u2_three_address_weld_exact.py — v11 U2, THE THREE-ADDRESS WELD:
curvature, irreversibility, non-lumpability.

Pin: v11/note-u2-three-address-weld-pin.md (STRICT, binding, frozen
before any code was written).  Binding specification: paper 0 sec.9b,
the catalog [V11-CAT] sec.4.7.  Parents: v10 D74 TERMINAL (transport
curvature: the 88 + 40 + 12 census, the 44 + 44 descent split, group
<2,3>), v11 LD TERMINAL (the irreversibility wall: a closed square's
reversed record is priced IFF its record carries no arbitration,
17,277/17,277; the wall strictly contains the curvature), v11 U1
TERMINAL (non-lumpability: DC2's ladder, the 44 descent-obstruction
squares, 32/44 on non-lumpable classes), v11 U3 TERMINAL.

THE QUESTION.  Are curvature (J != 1), irreversibility (the reversed
record refused) and non-lumpability (DC2 failing) THE SAME ADDRESS seen
by three instruments, three loci in exact containment, or crossing
structures — and what is the exact boundary census of each containment?

THE UNIT (pin sec."The unit"):
  W-A  the 2x2x2 census.  Over EVERY closed square of the committed
       populations (AB4, ABC3, ASYM1, ASYM2 — re-anchored) all three
       statuses exactly, per population and pooled, BOTH WAYS.
  W-B  the containment structure: every candidate implication tested
       exactly, and for every strict containment / crossing the exact
       boundary census by population, kind pair, base depth and value.
  W-C  the weld candidate: does ONE grammar quantity predict all three
       statuses on every square?  Exact prediction table per candidate;
       if none succeeds, the failure pattern is the deliverable.
  W-D  the record-grain hook (U2b) NAMED, NOT RUN.

SINGLE-SOURCING.  All three instruments are the committed ones, lifted
rather than retyped: D74's census machinery (enumerate_line,
square_census, A_menu, congruence, sk, evsk) by ast.FunctionDef from
v10/code/d74_transport_holonomy_exact.py; LD's reversal functor (rho,
rev, rev_with, mu_of_sequence, first_blocker, classify,
reversal_census) by ast.FunctionDef from
v11/code/ld_reversal_probe_exact.py; U1's sigma port and horizon
measure (sigmaT, payload_of, horizon_measure) by ast.FunctionDef from
v11/code/u1_indivisibility_census_exact.py.  The committed d42b1
transport layer is text-sliced with an AST signature pass and
exit-freedom gated.

DECLARED CAPS (printed at the end).  Populations: AB4 (A,B) d<=4;
ABC3 (A,B,C) d<=3; ASYM1 (A,B) d<=5 one-way A->B; ASYM2 (A,B,C) d<=4
directed ring A->B->C->A.  The lumpability instrument runs at each
population's OWN window, with U1's committed ARM-A window ((A,B) d<=5,
unfiltered) carried as the port-verification instrument and as the
horizon control for AB4.  Transport scope, cut grain, committed
families only.

SCOPE.  Cut grain / transport scope.  Record-grain claims are U2b's and
are not made here.  No claim that any weld quantity is "the quantum
layer".  The reversal is FORMAL (category-level) throughout, exactly as
LD declares it: no dynamical or thermodynamic language appears in this
receipt.  Weight-system level only; no measure claim.  No CP, Bell,
locality or covariance framing.

HOUSE RULES OBSERVED
  * Exact arithmetic (fractions.Fraction) end to end.  No floats
    anywhere except wall-clock timings.
  * Every number a gate tests against is either a QUOTED committed value
    (registry QUOTES/ANCH, with path provenance) or a quantity derived
    inside this receipt.
  * Every census printed BOTH WAYS.
  * Substantive negatives exit 0.  exit 1 is reserved for ANCHOR
    failure — a committed D72/D74/LD/U1 number that does not reproduce.
  * Determinism: all iteration that feeds a printed number is ordered by
    sk() (hash-seed independent); a determinism probe is run.
  * Section progress and block times printed; total runtime printed.
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
REPO = os.path.dirname(REPO)          # .../isp  (run from anywhere)
os.chdir(REPO)

PASS = FAIL = 0
ANCHOR_FAIL = 0
COROLLARY = []


def sec(title):
    print()
    print("-" * 78)
    print(title)
    print("-" * 78)
    sys.stdout.flush()


def check(label, ok, detail="", corollary_of=None):
    """corollary_of: the gate is entailed by another gate or is true of
    every object of its type.  Run and printed but NOT counted as
    independent evidence (the D72 MODERATE-4 discipline, carried)."""
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    PASS += int(bool(ok))
    FAIL += int(not ok)
    if corollary_of is not None:
        COROLLARY.append((label.split(":")[0].split("  ")[0], corollary_of))
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))
    if corollary_of is not None:
        print(f"         ^ NO INDEPENDENT INFORMATION: {corollary_of}")
    sys.stdout.flush()
    return bool(ok)


def anchor(label, ok, detail=""):
    global ANCHOR_FAIL
    if not check("ANCHOR " + label, ok, detail):
        ANCHOR_FAIL += 1
    return bool(ok)


def report(label, value):
    print(f"  [DATA] {label}: {value}")
    sys.stdout.flush()


def fmtk(counter):
    return {str(k): v for k, v in sorted(counter.items(),
                                         key=lambda z: str(z[0]))}


# ===========================================================================
# SEC 0.  THE REGISTRY — every constant a gate tests against, with provenance
# ===========================================================================

QUOTES = {
    "T6.1": (
        "v10/note-d72-weld-result.md:150 (sec.1 T6.1), quoted verbatim by "
        "v10/code/d74_transport_holonomy_exact.py and by "
        "v11/code/ld_reversal_probe_exact.py",
        "(A,B) d <= 4: 88 of 1,546 closed squares non-unit, spectrum "
        "{1/2: 70, 2/3: 2, 3/2: 6, 2: 10}, kinds {(r,d): 68, (d,r): 8, "
        "(d,n): 6, (d,d): 4, (n,d): 2}, both-blocked 142, "
        "delivery-bearing 88/88, shallowest defect at total depth 3.  "
        "(A,B,C) d <= 3: 12 of 1,554, spectrum {1/2: 12}, kinds "
        "{(r,d): 12}, both-blocked 42.",
    ),
    "T6.2": (
        "v10/note-d72-weld-result.md:151 (sec.1 T6.2)",
        "(A,B) d <= 4: 40 half-open (AB-only 28, BA-only 12), kinds "
        "{(r,d): 12, (d,r): 4, (p,d): 16, (d,p): 8}.",
    ),
    "d74_group": (
        "v10/note-d74-transport-holonomy-result.md:1, :97-98, :227",
        "the transport holonomy value set is {1/2, 2/3, 3/2, 2} at every "
        "scope run; the group it generates is <2,3>.",
    ),
    "d74_4444": (
        "v10/note-d74-transport-holonomy-result.md (A3.1/A3.2), quoted by "
        "v11/code/u1_indivisibility_census_exact.py as QUOTES['d74-4444']",
        "AB4: of 88 defective squares the weighted-menu quotient CLOSES 44 "
        "and the coarsest weighted congruence closes the same 44; SEEN "
        "(curvature-type) 44 with spectrum {1/2: 26, 2: 10, 2/3: 2, "
        "3/2: 6}; UNSEEN (descent-obstruction-type) 44 with spectrum "
        "{1/2: 44} and kinds {(r,d): 44}.  ABC3: the menu quotient closes "
        "0 of 12.",
    ),
    "d74_asym": (
        "v10/code/d74_transport_holonomy_exact.py:1406-1420 (oneway, ring), "
        "censused in v11/note-ld-last-door.md sec.4",
        "ASYM-1, the link A->B only: 5,504 closed, 334 non-unit, spectrum "
        "{1/2: 184, 2/3: 10, 3/2: 68, 2: 72}.  ASYM-2, the defected "
        "directed ring A->B->C->A: 8,673 closed, 228 non-unit, spectrum "
        "{1/2: 190, 2/3: 2, 3/2: 10, 2: 26}.  Declared SUB-GRAMMARS: the "
        "support is restricted, the committed weights are untouched.",
    ),
    "LD_C3a": (
        "v11/note-ld-last-door.md sec.3 C.3a / sec.4 D.3, adjudicated v11 "
        "LOG #10",
        "a closed square's reversed counterpart is priced by the committed "
        "law IF AND ONLY IF its endpoint record carries no arbitration "
        "event: over all four arms (17,277 closed squares) the cross-tab "
        "is {(arb, priced): 0, (arb, refused): 5,768, (no arb, priced): "
        "11,509, (no arb, refused): 0}; on the two anchor arms alone "
        "(3,100 squares) it is {0, 526, 2,574, 0}.",
    ),
    "LD_C3b": (
        "v11/note-ld-last-door.md sec.3 C.3b / sec.4 D.1, D.3",
        "every holonomy-carrying loop's record carries an arbitration: "
        "662/662 over the four arms (88 + 12 + 334 + 228), and 662/662 "
        "holonomy-carrying loops have NO priced reversed counterpart "
        "(0 INVERSION, 0 INVARIANT, 0 OTHER, 662 UNDEFINED).",
    ),
    "U1_DC2": (
        "v11/code/u1_output.txt:772, :789 (gates J2 and DC2), "
        "v11/note-u1-indivisibility-census.md",
        "the lumpability defect of ARM-A ((A,B) transport, exhaustive to "
        "depth 5, relative-horizon measure at horizon 5), by depth "
        "(classes, non-lumpable classes): {0: (1,0), 1: (5,0), 2: (11,4), "
        "3: (19,8), 4: (32,12)}, total 24 non-lumpable classes; and 32 of "
        "the 44 descent-obstruction squares of AB4 have their base in a "
        "NON-LUMPABLE configuration class of ARM-A.",
    ),
    "U1_44": (
        "v11/code/u1_output.txt:464-465",
        "the 44 named descent-obstruction squares of AB4: base-depth "
        "census {1: 4, 2: 40}; event-kind pairs {('r','d'): 44}.",
    ),
}

ANCH = {
    "AB_hist": 3969, "AB_closed": 1546, "AB_defects": 88,
    "AB_full_ratios": {Fr(1, 2): 70, Fr(2, 3): 2, Fr(1): 1458,
                       Fr(3, 2): 6, Fr(2): 10},
    "AB_kinds": {("r", "d"): 68, ("d", "r"): 8, ("d", "n"): 6,
                 ("d", "d"): 4, ("n", "d"): 2},
    "AB_bothblocked": 142, "AB_ABonly": 28, "AB_BAonly": 12,
    "AB_halfopen": 40,
    "AB_openkinds": {("r", "d"): 12, ("d", "r"): 4, ("p", "d"): 16,
                     ("d", "p"): 8},
    "AB_mindepth": 3,
    "ABC_hist": 3424, "ABC_closed": 1554, "ABC_defects": 12,
    "ABC_full_ratios": {Fr(1, 2): 12, Fr(1): 1542},
    "ABC_kinds": {("r", "d"): 12}, "ABC_bothblocked": 42,
    "ASYM1_closed": 5504, "ASYM1_defects": 334,
    "ASYM1_spec": {Fr(1, 2): 184, Fr(2, 3): 10, Fr(3, 2): 68, Fr(2): 72},
    "ASYM2_closed": 8673, "ASYM2_defects": 228,
    "ASYM2_spec": {Fr(1, 2): 190, Fr(2, 3): 2, Fr(3, 2): 10, Fr(2): 26},
    "group_valueset": {Fr(1, 2), Fr(2, 3), Fr(3, 2), Fr(2)},
    "AB_seen": 44, "AB_unseen": 44,
    "AB_seen_spec": {Fr(1, 2): 26, Fr(2): 10, Fr(2, 3): 2, Fr(3, 2): 6},
    "AB_unseen_spec": {Fr(1, 2): 44},
    "AB_unseen_kinds": {("r", "d"): 44},
    "AB_unseen_depths": {1: 4, 2: 40},
    "ABC_seen": 0, "ABC_unseen": 12,
    "LD_total_closed": 17277,
    "LD_curved": 662,
    "LD_xtab4": {(True, True): 0, (True, False): 5768,
                 (False, True): 11509, (False, False): 0},
    "LD_xtab2": {(True, True): 0, (True, False): 526,
                 (False, True): 2574, (False, False): 0},
    "U1_ladder": {0: (1, 0), 1: (5, 0), 2: (11, 4), 3: (19, 8),
                  4: (32, 12)},
    "U1_44_nonlump": 32,
}

print("=" * 78)
print("U2 — THE THREE-ADDRESS WELD: curvature, irreversibility, "
      "non-lumpability")
print("=" * 78)
print("  banner: exact Fractions throughout; the committed d42b1 layer")
print("  single-sourced by text-slice + an AST signature pass with")
print("  exit-freedom gated; all three instruments lifted by AST from")
print("  their own committed receipts (D74, LD, U1) and not retyped;")
print("  every tested constant quoted from a committed source (registry")
print("  below); every census printed BOTH WAYS; substantive negatives")
print("  exit 0; exit 1 ONLY if a committed number fails to reproduce.")
print()
print("  SCOPE: cut grain / transport scope, committed populations only.")
print("  Record-grain claims are U2b's and are not made here.  The")
print("  reversal is FORMAL (category-level), exactly as LD declares it:")
print("  no dynamical or thermodynamic language appears in this receipt.")
print("  Weight-system level only; no measure claim; no CP/Bell/locality/")
print("  covariance framing.  No claim that any weld quantity is 'the")
print("  quantum layer'.")
print()
print(f"  PYTHONHASHSEED = {os.environ.get('PYTHONHASHSEED', '(unset)')}")
print()
print("  QUOTE REGISTRY (the anchors below are held to these):")
for k, (where, text) in QUOTES.items():
    print(f"    [{k}] {where}")
    for i in range(0, len(text), 68):
        print(f"        {text[i:i + 68]}")
sys.stdout.flush()


# ===========================================================================
# SEC 0.1  SINGLE-SOURCING
# ===========================================================================

sec("SEC 0.1  SINGLE-SOURCING: AST signature pass, text-slice, AST lift")


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


def slice_exec(path, cut_marker, name):
    src = open(path).read()
    idx = src.index(cut_marker)
    head = src[:idx]
    mod = types.ModuleType(name)
    sys.modules[name] = mod
    ns = mod.__dict__
    ns["__name__"] = name
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
    ns, in the order given (the D70 HZ0-a(iii) idiom, as U1 carries it)."""
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


_P_B1 = "v10/code/d42b1_transport_exact.py"
_P_D74 = "v10/code/d74_transport_holonomy_exact.py"
_P_LD = "v11/code/ld_reversal_probe_exact.py"
_P_U1 = "v11/code/u1_indivisibility_census_exact.py"

B1_REQ = {
    "candidates_for": ["acts", "actors"],
    "admissible": ["acts", "e", "actors", "law"],
    "canon": ["acts"],
    "regs_of": ["op"],
    "event_poset": ["acts"],
    "full_view": ["acts"],
    "value_of": ["v"],
    "vname": ["base", "wkey", "init"],
    "View": ["<class>"],
}
D74_REQ = {
    "sk": ["o"],
    "evsk": ["e"],
    "enumerate_line": ["cands", "actors", "depth", "filt"],
    "square_census": ["fam", "cache", "actors", "dep", "adm", "regs",
                      "canon_f", "filt", "reverse_cands", "tamper"],
    "A_menu": ["h", "cache"],
    "congruence": ["R"],
}
LD_REQ = {
    "rho": ["e"],
    "rev": ["seq"],
    "rev_with": ["seq", "r_"],
    "mu_of_sequence": ["seq", "actors", "filt"],
    "first_blocker": ["seq", "actors", "filt"],
    "classify": ["v", "v_rev"],
    "reversal_census": ["arm", "relab", "opp_filt"],
    "oneway": ["e"],
    "ring": ["e"],
}
U1_REQ = {
    "payload_of": ["tkn"],
    "sigmaT": ["h", "actors", "enriched", "view_of", "cache_store"],
    "horizon_measure": ["cache", "fam", "D", "roots", "root_weight"],
}

_s1, _m1 = ast_signatures(_P_B1, B1_REQ)
_s74, _m74 = ast_signatures(_P_D74, D74_REQ)
_sld, _mld = ast_signatures(_P_LD, LD_REQ)
_su1, _mu1 = ast_signatures(_P_U1, U1_REQ)
anchor("SRC.1 AST SIGNATURE PASS on all four committed sources: every "
       "required def exists at module level with the exact positional "
       "argument list, so a silent upstream edit to the transport layer, "
       "to D74's census machinery, to LD's reversal functor or to U1's "
       "sigma port cannot slip through unnoticed",
       not (_m1 or _m74 or _mld or _mu1),
       f"d42b1 {len(_s1)} defs ({len(B1_REQ)} required, missing {_m1}); "
       f"d74 {len(_s74)} defs (missing {_m74}); ld {len(_sld)} defs "
       f"(missing {_mld}); u1 {len(_su1)} defs (missing {_mu1})")

B1, _b1n, _b1t = slice_exec(_P_B1, 'print("[d42b1', "u2_d42b1")
report("d42b1 slice", f"{_b1n}/{_b1t} bytes executed (definition head "
       "only)")

_exitfree = True
try:
    slice_exec(_P_B1, 'print("[d42b1', "u2_probe")
except _NoExit:
    _exitfree = False
check("SRC.2 EXIT-FREEDOM GATED: sys.exit / os._exit are neutralised "
      "inside the slice and restored after, so a sliced layer cannot set "
      "this receipt's exit status; the slice re-executes cleanly",
      _exitfree and "sys.exit" not in open(_P_B1).read()[:_b1n],
      f"second slice of d42b1 executed with exit blocked; 0 sys.exit in "
      f"the {_b1n}-byte head",
      corollary_of="a property of the loader, not of the substrate; it "
      "tests our plumbing")

b1_cand = B1["candidates_for"]
b1_adm = B1["admissible"]
b1_canon = B1["canon"]
b1_regs = B1["regs_of"]
b1_fullview = B1["full_view"]
b1_poset = B1["event_poset"]
b1_valueof = B1["value_of"]
V0 = B1["V0"]

# --- D74's census machinery, lifted -----------------------------------------
NS74 = {"Fr": Fr, "Counter": Counter, "defaultdict": defaultdict,
        "b1_adm": b1_adm, "_EVSK": {}}
_seg74 = ast_defs(_P_D74, list(D74_REQ), NS74)
sk = NS74["sk"]
evsk = NS74["evsk"]
enumerate_line = NS74["enumerate_line"]
square_census = NS74["square_census"]
A_menu = NS74["A_menu"]
congruence = NS74["congruence"]
anchor("SRC.3 D74's CENSUS MACHINERY IS D74's, lifted by AST from the "
       "committed receipt and not retyped: sk, evsk, enumerate_line, "
       "square_census (the exchange-square census whose ratio line is the "
       "holonomy), A_menu (the weighted-menu abstraction whose kernel IS "
       "the coarsest descent quotient) and congruence",
       set(_seg74) == set(D74_REQ)
       and "r = Fr(qA * qB2, 1) / Fr(qB * qA2, 1)" in _seg74["square_census"]
       and "sorted((evsk(e), str(q)) for e, q in cache[h])"
       in _seg74["A_menu"],
       f"lifted {len(_seg74)} definitions from {_P_D74}: "
       + ", ".join(f"{n} ({len(_seg74[n].splitlines())} lines)"
                   for n in sorted(_seg74)))

# --- LD's reversal functor, lifted ------------------------------------------
NSLD = {"Fr": Fr, "b1_adm": b1_adm}
_segld = ast_defs(_P_LD, ["rho", "rev", "rev_with", "mu_of_sequence",
                          "first_blocker", "classify", "reversal_census",
                          "oneway", "ring"], NSLD)
rho = NSLD["rho"]
rev = NSLD["rev"]
rev_with = NSLD["rev_with"]
mu_of_sequence = NSLD["mu_of_sequence"]
first_blocker = NSLD["first_blocker"]
classify = NSLD["classify"]
reversal_census = NSLD["reversal_census"]
oneway = NSLD["oneway"]
ring = NSLD["ring"]
anchor("SRC.4 LD's REVERSAL FUNCTOR IS LD's, lifted by AST from the "
       "TERMINAL LD receipt and not retyped: rho (the forced event-kind "
       "relabelling — delivery transposes, every other kind is self-dual), "
       "rev, rev_with, mu_of_sequence (the committed measure of a bare "
       "event sequence read from the empty record), first_blocker, "
       "classify and reversal_census, together with the two committed "
       "sub-grammar filters oneway and ring",
       set(_segld) == set(LD_REQ)
       and "return ('d', e[2], e[1], e[3])" in _segld["rho"]
       and "mu_of_sequence(RA, actors, of)" in _segld["reversal_census"],
       f"lifted {len(_segld)} definitions from {_P_LD}: "
       + ", ".join(f"{n} ({len(_segld[n].splitlines())} lines)"
                   for n in sorted(_segld)))

# --- U1's sigma port and horizon measure, lifted -----------------------------
NSU1 = {"Fr": Fr, "defaultdict": defaultdict, "sk": sk, "V0": V0,
        "b1_valueof": b1_valueof}
_segu1 = ast_defs(_P_U1, ["payload_of", "sigmaT", "horizon_measure"], NSU1)
payload_of = NSU1["payload_of"]
sigmaT = NSU1["sigmaT"]
horizon_measure = NSU1["horizon_measure"]
anchor("SRC.5 U1's DC2 INSTRUMENT IS U1's, lifted by AST from the TERMINAL "
       "U1 receipt and not retyped: sigmaT (the D62 sigma fields ported to "
       "transport scope — the WINNER-INVISIBLE reading, enriched=False, "
       "which is the reading U1's DC2 census uses), payload_of, and "
       "horizon_measure (the D46b/D70 relative-horizon construction "
       "G(h,r) and the forward measure built from "
       "k_r(e|h) = q(e|h) G(h+e,r-1)/G(h,r))",
       set(_segu1) == set(U1_REQ)
       and "alive = {a: set(x for x in v.holdings(a)" in _segu1["sigmaT"]
       and "sum(q * G[k + (e,)] for e, q in cache[k])"
       in _segu1["horizon_measure"],
       f"lifted {len(_segu1)} definitions from {_P_U1}: "
       + ", ".join(f"{n} ({len(_segu1[n].splitlines())} lines)"
                   for n in sorted(_segu1)))


def fmt(counter):
    return {str(k): v for k, v in sorted(counter.items(),
                                         key=lambda z: sk(z[0]))}


AB = ("A", "B")
ABC = ("A", "B", "C")


# ===========================================================================
# SEC 1.  DECLARED CAPS AND POPULATIONS — printed before anything uses them
# ===========================================================================

sec("SEC 1  DECLARED CAPS AND POPULATIONS (nothing silent)")

POPS = (
    ("AB4", AB, 4, None, "(A,B) depth<=4 — D72/D74's anchor window"),
    ("ABC3", ABC, 3, None, "(A,B,C) depth<=3 — D72/D74's anchor window"),
    ("ASYM1", AB, 5, oneway, "(A,B) depth<=5, one-way A->B — D74's "
     "declared sub-grammar"),
    ("ASYM2", ABC, 4, ring, "(A,B,C) depth<=4, directed ring A->B->C->A "
     "— D74's declared sub-grammar"),
)
POPNAMES = tuple(p[0] for p in POPS)

for nm, actors, dep, filt, desc in POPS:
    print(f"  POPULATION {nm:<6} {desc}")
print("  the lumpability instrument runs at EACH POPULATION'S OWN WINDOW")
print("    (its actor pool, its cap, its declared sub-grammar filter,")
print("     horizon = the cap), and U1's committed ARM-A window")
print("    ((A,B) depth<=5, unfiltered, horizon 5) is carried BOTH as the")
print("     port-verification instrument and as AB4's horizon control.")
print("  the reversal instrument is LD's committed reading: the anchor")
print("    populations reverse into the unrestricted grammar, the two")
print("    sub-grammar populations into their MIRROR sub-grammar (LD's")
print("    honest opposite of a directed schedule), with the arm's own")
print("    sub-grammar carried as the second reading.")
print("  transport scope, cut grain, committed families only; weight-")
print("    system level; no measure claim.")
sys.stdout.flush()


# ===========================================================================
# SEC 2.  ANCHORS — the committed censuses must reproduce EXACTLY.
#         exit 1 lives here and nowhere else.
# ===========================================================================

sec("SEC 2  ANCHORS — D72/D74's census on all four populations "
    "(exit 1 on failure)")

_t = time.time()
ARMS = {}
for nm, actors, dep, filt, desc in POPS:
    fam, cache = enumerate_line(b1_cand, actors, dep, filt)
    st, rat, kinds, okinds, defs, half, closed = square_census(
        fam, cache, actors, dep, b1_adm, b1_regs, b1_canon, filt)
    ARMS[nm] = dict(label=f"{nm} {desc}", actors=actors, dep=dep, filt=filt,
                    fam=fam, cache=cache, st=st, rat=rat, kinds=kinds,
                    okinds=okinds, defs=defs, half=half, closed=closed,
                    nonunit=Counter({k: v for k, v in rat.items()
                                     if k != 1}))
    report(f"{nm} census", f"{len(fam)} histories; {dict(st)}; non-unit "
           f"{len(defs)}; ratios {fmt(rat)}; kinds {fmtk(kinds)}")
    print(f"         [{time.time() - _t:.0f}s elapsed in SEC 2]")
    sys.stdout.flush()

_A, _C = ARMS["AB4"], ARMS["ABC3"]
_dely = sum(1 for h, a, b, r, *_ in _A["defs"] if "d" in (a[0], b[0]))
_mind = min(len(h) + 2 for h, *_ in _A["defs"])
anchor("AB4.1 D72's T6.1 row reproduces EXACTLY — history count, "
       "closed-square count, the FULL ratio multiset (unit AND non-unit), "
       "the kind census, the both-blocked count, the delivery-bearing "
       "fraction and the shallowest defect depth",
       len(_A["fam"]) == ANCH["AB_hist"]
       and _A["st"]["closed"] == ANCH["AB_closed"]
       and dict(_A["rat"]) == ANCH["AB_full_ratios"]
       and dict(_A["kinds"]) == ANCH["AB_kinds"]
       and _dely == len(_A["defs"]) == ANCH["AB_defects"]
       and _A["st"]["both-blocked"] == ANCH["AB_bothblocked"]
       and _mind == ANCH["AB_mindepth"],
       f"histories {len(_A['fam'])}/{ANCH['AB_hist']}; closed "
       f"{_A['st']['closed']}/{ANCH['AB_closed']}; non-unit "
       f"{len(_A['defs'])}/{ANCH['AB_defects']}; ratios match "
       f"{dict(_A['rat']) == ANCH['AB_full_ratios']}; kinds match "
       f"{dict(_A['kinds']) == ANCH['AB_kinds']}; delivery-bearing "
       f"{_dely}/{len(_A['defs'])}; shallowest {_mind}")
anchor("AB4.2 D72's T6.2 half-open row reproduces EXACTLY — 40 half-open "
       "squares, AB-only 28, BA-only 12, with the committed kind census",
       _A["st"].get("AB-only", 0) == ANCH["AB_ABonly"]
       and _A["st"].get("BA-only", 0) == ANCH["AB_BAonly"]
       and dict(_A["okinds"]) == ANCH["AB_openkinds"],
       f"AB-only {_A['st'].get('AB-only', 0)}, BA-only "
       f"{_A['st'].get('BA-only', 0)}, kinds {fmtk(_A['okinds'])}")
anchor("ABC3.1 D72's T6.1 row at the three-actor anchor window reproduces "
       "EXACTLY",
       len(_C["fam"]) == ANCH["ABC_hist"]
       and _C["st"]["closed"] == ANCH["ABC_closed"]
       and dict(_C["rat"]) == ANCH["ABC_full_ratios"]
       and dict(_C["kinds"]) == ANCH["ABC_kinds"]
       and len(_C["defs"]) == ANCH["ABC_defects"]
       and _C["st"]["both-blocked"] == ANCH["ABC_bothblocked"],
       f"histories {len(_C['fam'])}/{ANCH['ABC_hist']}; closed "
       f"{_C['st']['closed']}/{ANCH['ABC_closed']}; non-unit "
       f"{len(_C['defs'])}/{ANCH['ABC_defects']}; both-blocked "
       f"{_C['st']['both-blocked']}")
for nm, key in (("ASYM1", "ASYM1"), ("ASYM2", "ASYM2")):
    R = ARMS[nm]
    anchor(f"{nm}.1 D74's declared sub-grammar census reproduces EXACTLY "
           f"(the count LD's sec.4 table carries): closed-square count, "
           f"non-unit count and the full non-unit spectrum",
           R["st"]["closed"] == ANCH[key + "_closed"]
           and len(R["defs"]) == ANCH[key + "_defects"]
           and dict(R["nonunit"]) == ANCH[key + "_spec"],
           f"closed {R['st']['closed']}/{ANCH[key + '_closed']}; non-unit "
           f"{len(R['defs'])}/{ANCH[key + '_defects']}; spectrum "
           f"{fmt(R['nonunit'])}")

_valset = set()
for nm in POPNAMES:
    _valset |= set(ARMS[nm]["nonunit"])
anchor("G.1 D74's holonomy value set reproduces EXACTLY over all four "
       "populations: {1/2, 2/3, 3/2, 2}, the value set of the group <2,3> "
       "(the group row itself is D74's and is not re-derived here — this "
       "receipt uses J only as a status and a candidate)",
       _valset == ANCH["group_valueset"],
       f"value set {sorted(str(x) for x in _valset)} (quoted "
       f"{sorted(str(x) for x in ANCH['group_valueset'])})")

_tot_closed = sum(ARMS[nm]["st"]["closed"] for nm in POPNAMES)
_tot_curved = sum(len(ARMS[nm]["defs"]) for nm in POPNAMES)
anchor("LD.0 THE POOLED POPULATION IS LD's POPULATION, TO THE UNIT: "
       "17,277 closed squares over the four arms, of which 662 are "
       "holonomy-carrying",
       _tot_closed == ANCH["LD_total_closed"]
       and _tot_curved == ANCH["LD_curved"],
       f"closed squares {_tot_closed} (quoted {ANCH['LD_total_closed']}); "
       f"holonomy-carrying {_tot_curved} (quoted {ANCH['LD_curved']})")

# --- D74's 44 + 44 descent split, on D74's own carrier ---------------------
for nm in ("AB4", "ABC3"):
    R = ARMS[nm]
    Vm = {tuple(h): sk(A_menu(tuple(h), R["cache"])) for h in R["fam"]}
    seen, unseen = [], []
    for row in R["defs"]:
        hh, a, b = row[0], row[1], row[2]
        (seen if Vm[hh + (a, b)] == Vm[hh + (b, a)] else unseen).append(row)
    cong, iters = congruence(R)
    R["seen"], R["unseen"] = seen, unseen
    R["cong_def"] = sum(1 for hh, a, b, r, *_ in R["defs"]
                        if cong[hh + (a, b)] == cong[hh + (b, a)])
    report(f"{nm} descent split", f"of {len(R['defs'])} defective squares "
           f"the weighted-menu quotient CLOSES {len(seen)} and the "
           f"coarsest weighted congruence closes {R['cong_def']} "
           f"({iters} refinement rounds); UNSEEN "
           f"(descent-obstruction-type) {len(unseen)}: spectrum "
           f"{fmt(Counter(r[3] for r in unseen))}, kinds "
           f"{fmtk(Counter((r[1][0], r[2][0]) for r in unseen))}")

U44 = sorted(_A["unseen"], key=lambda row: sk((row[0], row[1], row[2])))
anchor("D74.1 THE 44 + 44 SPLIT REPRODUCES EXACTLY on AB4 — the coarsest "
       "descent quotient closes 44 of the 88 defective squares, the "
       "coarsest weighted congruence closes the same 44, and the invisible "
       "half is 44 squares with spectrum {1/2: 44}, kinds {(r,d): 44} and "
       "base depths {1: 4, 2: 40}; on ABC3 the menu quotient closes 0 of "
       "12.  These 44 are U1's named descent-obstruction squares",
       len(_A["seen"]) == ANCH["AB_seen"]
       and len(_A["unseen"]) == ANCH["AB_unseen"]
       and _A["cong_def"] == ANCH["AB_seen"]
       and dict(Counter(r[3] for r in _A["seen"])) == ANCH["AB_seen_spec"]
       and dict(Counter(r[3] for r in U44)) == ANCH["AB_unseen_spec"]
       and dict(Counter((r[1][0], r[2][0]) for r in U44))
       == ANCH["AB_unseen_kinds"]
       and dict(Counter(len(r[0]) for r in U44)) == ANCH["AB_unseen_depths"]
       and len(_C["seen"]) == ANCH["ABC_seen"]
       and len(_C["unseen"]) == ANCH["ABC_unseen"],
       f"AB4 seen/unseen {len(_A['seen'])}/{len(_A['unseen'])} (quoted "
       f"{ANCH['AB_seen']}/{ANCH['AB_unseen']}); congruence closes "
       f"{_A['cong_def']}; 44-square base depths "
       f"{dict(sorted(Counter(len(r[0]) for r in U44).items()))}; kinds "
       f"{fmtk(Counter((r[1][0], r[2][0]) for r in U44))}; ABC3 "
       f"seen/unseen {len(_C['seen'])}/{len(_C['unseen'])}")

report("SEC 2 block time", f"{time.time() - _t:.0f}s")


# ===========================================================================
# SEC 3.  INSTRUMENT II — LD's REVERSAL FUNCTOR, RE-GATED PER POPULATION
# ===========================================================================

sec("SEC 3  INSTRUMENT II — the reversal status, and LD's biconditional "
    "re-gated")

print("""  LD's committed reading, carried verbatim.  A closed square is the loop
  h -> h.eA -> h.eA.eB = h.eB.eA -> h.eB -> h; its two endpoint records
  sigma_AB = h.eA.eB and sigma_BA = h.eB.eA go under R to R(sigma_AB) and
  R(sigma_BA), and the square is PRICED iff the committed law prices both
  images and REFUSED otherwise.  The anchor populations are read in the
  unrestricted grammar; the two sub-grammar populations are read in their
  MIRROR sub-grammar (LD's honest opposite of a directed schedule, of =
  f o rho), with the arm's own sub-grammar carried as a second reading.

  LD's C.3a is the biconditional this unit needs before it may use
  arbitration-carrying as a proxy for refusal, so it is RE-GATED here,
  per population and pooled, in BOTH directions.""")

_t = time.time()
ROWS = {}
for nm in POPNAMES:
    rows, _of = reversal_census(ARMS[nm])
    ROWS[nm] = rows
    cls = Counter(classify(v, vr) for _h, _a, _b, v, vr, *_ in rows)
    carry = Counter(classify(v, vr) for _h, _a, _b, v, vr, *_ in rows
                    if v != 1)
    report(f"{nm} reversal classification (all closed squares)", fmtk(cls))
    report(f"{nm} reversal classification (holonomy-carrying only, "
           f"{sum(carry.values())} squares)", fmtk(carry))
    print(f"         [{time.time() - _t:.0f}s elapsed in SEC 3]")
    sys.stdout.flush()


def arb_of(h, eA, eB):
    return any(e[0] == "r" for e in tuple(h) + (eA, eB))


_xtab = {nm: Counter() for nm in POPNAMES}
for nm in POPNAMES:
    for h, eA, eB, v, vr, oA, oB, RA, RB in ROWS[nm]:
        _xtab[nm][(arb_of(h, eA, eB), vr is not None)] += 1
_xt4 = Counter()
for nm in POPNAMES:
    _xt4 += _xtab[nm]
_xt2 = _xtab["AB4"] + _xtab["ABC3"]
_CELLS = ((True, True), (True, False), (False, True), (False, False))


def full4(counter):
    return {k: counter.get(k, 0) for k in _CELLS}


for nm in POPNAMES:
    report(f"{nm} cross-tab (record carries an arbitration) x (its image "
           f"is priced)",
           {f"arb={k[0]}, priced={k[1]}": v
            for k, v in sorted(_xtab[nm].items(), key=str)})
report("POOLED cross-tab over all four populations",
       {f"arb={k[0]}, priced={k[1]}": v
        for k, v in sorted(_xt4.items(), key=str)})

anchor("LD.1 LD's ONE-KIND ADDRESS REPRODUCES EXACTLY, PER POPULATION AND "
       "POOLED, IN BOTH DIRECTIONS: a closed square's reversed counterpart "
       "is priced IF AND ONLY IF its endpoint record carries no "
       "arbitration event.  The pooled cross-tab is "
       "{(arb, priced): 0, (arb, refused): 5,768, (no arb, priced): "
       "11,509, (no arb, refused): 0}; the two anchor populations alone "
       "give {0, 526, 2,574, 0}.  This is the licence — and the only "
       "licence — for using arbitration-carrying as the exact proxy for "
       "refusal anywhere below",
       full4(_xt4) == ANCH["LD_xtab4"] and full4(_xt2) == ANCH["LD_xtab2"]
       and all(_xtab[nm][(True, True)] == 0
               and _xtab[nm][(False, False)] == 0 for nm in POPNAMES),
       f"pooled {dict(sorted(full4(_xt4).items(), key=str))} (quoted "
       f"{dict(sorted(ANCH['LD_xtab4'].items(), key=str))}); anchor pair "
       f"{dict(sorted(full4(_xt2).items(), key=str))}; per-population "
       f"off-diagonal zeros "
       f"{[(nm, _xtab[nm][(True, True)], _xtab[nm][(False, False)]) for nm in POPNAMES]}")

_carry_arb = Counter()
_carry_priced = Counter()
for nm in POPNAMES:
    for h, eA, eB, v, vr, *_ in ROWS[nm]:
        if v != 1:
            _carry_arb[arb_of(h, eA, eB)] += 1
            _carry_priced[vr is not None] += 1
anchor("LD.2 LD's C.3b REPRODUCES EXACTLY: every holonomy-carrying loop's "
       "record carries an arbitration (662/662) and not one of them has a "
       "priced reversed counterpart (662 UNDEFINED, 0 INVERSION, 0 "
       "INVARIANT, 0 OTHER)",
       _carry_arb[False] == 0 and _carry_arb[True] == ANCH["LD_curved"]
       and _carry_priced[True] == 0,
       f"holonomy-carrying loops carrying an arbitration "
       f"{_carry_arb[True]}/{sum(_carry_arb.values())}; with a priced "
       f"reversed counterpart {_carry_priced[True]}")

# --- the two sub-grammar readings, BOTH WAYS -------------------------------
_vac_tot = _vac_ok = 0
for nm in ("ASYM1", "ASYM2"):
    f = ARMS[nm]["filt"]
    for h, eA, eB, v, vr, oA, oB, RA, RB in ROWS[nm]:
        for R_ in (RA, RB):
            _vac_tot += 1
            _vac_ok += int(all(f(rho(e)) for e in R_))
check("REV.1a THE MIRROR FILTER IS VACUOUS ON IMAGES, MEASURED RATHER "
      "THAN ARGUED.  LD's D.2 argues that of(e) = f(rho(e)) passes "
      "identically on a reversed record, because every reversed event is "
      "rho(e_fwd) with f(e_fwd) true and rho is an involution.  Here it is "
      "measured event by event over every reversed endpoint record of both "
      "declared sub-grammar populations: the mirror filter refuses "
      "nothing.  The mirror column is therefore a reading of the "
      "UNRESTRICTED grammar, and the refusals it reports are the "
      "committed law's, not the filter's",
      _vac_ok == _vac_tot and _vac_tot > 0,
      f"{_vac_ok}/{_vac_tot} reversed endpoint records of ASYM1 and ASYM2 "
      f"pass the mirror filter at every event")

_own = {}
_own_rows = {}
for nm in ("ASYM1", "ASYM2"):
    rows_s, _ = reversal_census(ARMS[nm], opp_filt="same")
    _own_rows[nm] = rows_s
    t = Counter()
    for h, eA, eB, v, vr, *_ in rows_s:
        t[(arb_of(h, eA, eB), vr is not None)] += 1
    _own[nm] = t
    report(f"{nm} SECOND READING — reversed into the arm's OWN "
           f"(unmirrored) sub-grammar (LD's rigged control: the "
           f"rho-image of 'A may send to B' is 'B may send to A', so this "
           f"reading refuses on the link direction alone)",
           {f"arb={k[0]}, priced={k[1]}": v
            for k, v in sorted(t.items(), key=str)})
_moved = {}
for nm in ("ASYM1", "ASYM2"):
    mv = [(a, b, c) for (h, eA, eB, v, vr, *_), (h2, e2, e3, v2, vr2, *_)
          in zip(ROWS[nm], _own_rows[nm])
          for (a, b, c) in [(h, eA, eB)]
          if (vr is None) != (vr2 is None)]
    _moved[nm] = (len(mv), sum(1 for a, b, c in mv if arb_of(a, b, c)),
                  sum(1 for (h, eA, eB, v, vr, *_) in ROWS[nm]
                      if vr is None),
                  sum(1 for (h, eA, eB, v, vr, *_) in _own_rows[nm]
                      if vr is None))
report("the own-sub-grammar reading against the mirror reading (squares "
       "moved, of which arbitration-carrying; refused under mirror; "
       "refused under own)", _moved)
check("REV.1b THE OWN-SUB-GRAMMAR READING IS STRICTLY STRICTER AND MOVES "
      "ONLY ARBITRATION-FREE SQUARES, so the address this unit uses is "
      "untouched by the choice.  Read in its own unmirrored sub-grammar "
      "every square the mirror reading refuses is refused again, and the "
      "extra refusals are refusals of the LINK DIRECTION — every one of "
      "them arbitration-free.  Not one arbitration-carrying square "
      "changes status, so 'refused iff arbitration-carrying' is the "
      "mirror reading's statement and the own reading's failure of it is "
      "exactly the rigging LD names",
      all(_moved[nm][1] == 0 and _moved[nm][3] >= _moved[nm][2]
          for nm in ("ASYM1", "ASYM2"))
      and all(_own[nm][(True, True)] == 0 for nm in ("ASYM1", "ASYM2")),
      "; ".join(f"{nm}: {_moved[nm][0]} squares move, of which "
                f"{_moved[nm][1]} carry an arbitration; refused "
                f"{_moved[nm][2]} -> {_moved[nm][3]}"
                for nm in ("ASYM1", "ASYM2")))

report("SEC 3 block time", f"{time.time() - _t:.0f}s")


# ===========================================================================
# SEC 4.  INSTRUMENT III — U1's DC2 INSTRUMENT, PORTED TO PER-SQUARE SCOPE
# ===========================================================================

sec("SEC 4  INSTRUMENT III — U1's DC2 lumpability instrument, ported and "
    "VERIFIED")

print("""  U1's DC2 test, verbatim in its body and parameterised in its window.
  At a depth d the ported configuration map sigma (D62's fields, the
  WINNER-INVISIBLE reading) partitions the family's depth-d histories
  into classes; a class is NON-LUMPABLE iff two of its members carry
  DIFFERENT next-configuration laws under the relative-horizon kernel
  k_r(e|h) = q(e|h) G(h+e, r-1)/G(h, r).  U1 runs this at ARM-A ((A,B)
  transport, exhaustive to depth 5, horizon 5) and reports the ladder
  {0: (1,0), 1: (5,0), 2: (11,4), 3: (19,8), 4: (32,12)}.

  THE PORT TO PER-SQUARE SCOPE.  A closed square (h, eA, eB) sits at
  base depth d = |h|; its LUMPABILITY STATUS is the status of its base's
  configuration class at that depth in the instrument run at the square's
  own window.  Two further readings are carried as controls: LUMP-W, the
  square's whole window (the base class at depth d, or either shoulder
  class at depth d+1); and LUMP-B, DC1's sigma-commuting predicate at the
  square itself (sigma(h.eA.eB) != sigma(h.eB.eA)).

  THE PORT IS VERIFIED BEFORE IT IS USED, at U1's own window, against
  U1's own two committed numbers: the ladder, and 32 of the 44 named
  descent-obstruction squares on non-lumpable classes.""")

_t = time.time()


def lump_instrument(actors, cap, filt, label, fam=None, cache=None):
    """U1's DC2 instrument, parameterised in (actor pool, cap, declared
    sub-grammar).  The body is U1's, line for line.  `fam`/`cache` may be
    supplied when the identical enumerate_line call has already been made
    for the census; they are never anything else."""
    if fam is None:
        fam, cache = enumerate_line(b1_cand, actors, cap, filt)
    G, P, BD = horizon_measure(cache, fam, cap, None, None)
    store = {}

    def sig(k):
        return sigmaT(k, actors, False, b1_fullview, store)

    lump = {}
    for d in range(cap):
        cls = defaultdict(list)
        for k in BD[d]:
            if P.get(k):
                cls[sig(k)].append(k)
        bad = set()
        for c, hs in cls.items():
            dists = set()
            for k in hs:
                dd = defaultdict(Fr)
                for e, q in cache[k]:
                    dd[sig(k + (e,))] += q * G[k + (e,)] / G[k]
                dists.add(tuple(sorted(((sk(a), str(b))
                                        for a, b in dd.items()))))
            if len(dists) > 1:
                bad.add(c)
        lump[d] = (len(cls), len(bad), bad)
    return dict(label=label, actors=actors, cap=cap, filt=filt, fam=fam,
                cache=cache, G=G, P=P, BD=BD, lump=lump, sig=sig)


# --- PORT-VERIFY: U1's own window -------------------------------------------
ARMA = lump_instrument(AB, 5, None, "ARM-A (A,B) d<=5, unfiltered "
                       "[U1's committed window]")
_ladder = {d: (ARMA["lump"][d][0], ARMA["lump"][d][1])
           for d in sorted(ARMA["lump"])}
report("ARM-A lumpability defect by depth (classes, non-lumpable classes)",
       _ladder)
report("ARM-A family", f"{len(ARMA['fam'])} histories  "
       f"[{time.time() - _t:.0f}s]")
anchor("PORT.1 THE PORTED DC2 INSTRUMENT REPRODUCES U1's COMMITTED LADDER "
       "EXACTLY at U1's own window: (classes, non-lumpable classes) by "
       "depth = {0: (1,0), 1: (5,0), 2: (11,4), 3: (19,8), 4: (32,12)}, "
       "24 non-lumpable classes in total, the defect appearing from depth "
       "2 onward",
       _ladder == ANCH["U1_ladder"],
       f"measured {_ladder}; quoted {ANCH['U1_ladder']}; total "
       f"{sum(v[1] for v in _ladder.values())}")

_u44_bad = sum(1 for (hh, ea, eb, r, *_rest) in U44
               if ARMA["sig"](hh) in ARMA["lump"][len(hh)][2])
anchor("PORT.2 THE PER-SQUARE PORT REPRODUCES U1's COMMITTED GEOGRAPHY "
       "EXACTLY: read square by square through its base's configuration "
       "class, 32 of the 44 named descent-obstruction squares of AB4 sit "
       "on a NON-LUMPABLE class of ARM-A — U1's gate J2, to the unit.  "
       "The per-square reading is therefore U1's instrument and not a new "
       "one, and may be applied to the other three populations",
       _u44_bad == ANCH["U1_44_nonlump"],
       f"{_u44_bad} of {len(U44)} descent-obstruction squares on "
       f"non-lumpable classes (quoted {ANCH['U1_44_nonlump']} of 44)")
report("the 44 named squares, non-lumpable split by base depth",
       {d: (sum(1 for r in U44 if len(r[0]) == d
                and ARMA["sig"](r[0]) in ARMA["lump"][d][2]),
            sum(1 for r in U44 if len(r[0]) == d))
        for d in sorted({len(r[0]) for r in U44})})

# --- the per-population instruments -----------------------------------------
LUMP = {}
for nm, actors, dep, filt, desc in POPS:
    LUMP[nm] = lump_instrument(actors, dep, filt,
                               f"{nm} own window {desc}",
                               ARMS[nm]["fam"], ARMS[nm]["cache"])
    L = LUMP[nm]
    report(f"{nm} lumpability instrument",
           f"{len(L['fam'])} histories at its own window; defect by depth "
           f"(classes, non-lumpable) "
           f"{ {d: (L['lump'][d][0], L['lump'][d][1]) for d in sorted(L['lump'])} }")
    print(f"         [{time.time() - _t:.0f}s elapsed in SEC 4]")
    sys.stdout.flush()

_first = {nm: min((d for d in LUMP[nm]["lump"]
                   if LUMP[nm]["lump"][d][1] > 0), default=None)
          for nm in POPNAMES}
_first["ARM-A"] = min(d for d in ARMA["lump"] if ARMA["lump"][d][1] > 0)
report("the shallowest depth carrying a non-lumpable class, by window",
       {k: v for k, v in sorted(_first.items())})
check("PORT.3 THE DC2 DEFECT NEVER APPEARS BELOW DEPTH 2, IN ANY WINDOW "
      "RUN HERE.  U1's ARM-A, and each of the four populations' own "
      "windows, agree: depths 0 and 1 are lumpable everywhere, and the "
      "first non-lumpable class sits at depth 2 wherever the window "
      "reaches depth 2 at all.  This is the fact that fixes what the "
      "lumpability axis can see on each population, and it is stated "
      "before the census reads it",
      all(v in (None, 2) for v in _first.values())
      and _first["ARM-A"] == 2,
      f"shallowest non-lumpable depth by window "
      f"{ {k: str(v) for k, v in sorted(_first.items())} }")

_shallow = {nm: max(len(r[0]) for r in ARMS[nm]["closed"])
            for nm in POPNAMES}
report("the DEEPEST base depth a closed square of each population has",
       _shallow)
check("PORT.4 THE ABC3 ANCHOR WINDOW IS TOO SHALLOW FOR THE LUMPABILITY "
      "AXIS TO CARRY ANY INFORMATION, and this is declared here rather "
      "than discovered in the census.  A closed square needs |h| + 2 <= "
      "cap, so at cap 3 every ABC3 square has base depth <= 1 — and by "
      "PORT.3 no window has a non-lumpable class below depth 2.  Every "
      "ABC3 square is therefore LUMPABLE by the depth of its own window "
      "and not by anything about three-actor pools: ASYM2, a three-actor "
      "population reaching depth 4, carries non-lumpable classes at "
      "depths 2 and 3",
      _shallow["ABC3"] <= 1
      and sum(LUMP["ABC3"]["lump"][d][1] for d in LUMP["ABC3"]["lump"]) == 0
      and sum(LUMP["ASYM2"]["lump"][d][1]
              for d in LUMP["ASYM2"]["lump"]) > 0,
      f"ABC3 deepest square base depth {_shallow['ABC3']}; ABC3 "
      f"non-lumpable classes "
      f"{sum(LUMP['ABC3']['lump'][d][1] for d in LUMP['ABC3']['lump'])}; "
      f"ASYM2 (three actors, depth 4) non-lumpable classes "
      f"{sum(LUMP['ASYM2']['lump'][d][1] for d in LUMP['ASYM2']['lump'])} "
      f"at depths "
      f"{[d for d in sorted(LUMP['ASYM2']['lump']) if LUMP['ASYM2']['lump'][d][1] > 0]}")

# --- the deep-window control instrument for each population ----------------
print()
print("  [PORT.5]  THE DEEP-WINDOW CONTROL.  Each population is also read")
print("            through the DEEPEST committed window available for its")
print("            own grammar, so that no lumpability status below rests")
print("            on the population's own cap: AB4 through U1's ARM-A")
print("            ((A,B) d<=5, unfiltered), ABC3 through ARM-D ((A,B,C)")
print("            d<=4, unfiltered — U1's own pool control window), and")
print("            the two declared sub-grammars through their own")
print("            windows, which are already the deepest D74 declares for")
print("            them.")
sys.stdout.flush()
ARMD = lump_instrument(ABC, 4, None, "ARM-D (A,B,C) d<=4, unfiltered")
report("ARM-D lumpability defect by depth (classes, non-lumpable classes)",
       {d: (ARMD["lump"][d][0], ARMD["lump"][d][1])
        for d in sorted(ARMD["lump"])})
report("ARM-D family", f"{len(ARMD['fam'])} histories  "
       f"[{time.time() - _t:.0f}s]")
CTL = {"AB4": ARMA, "ABC3": ARMD, "ASYM1": LUMP["ASYM1"],
       "ASYM2": LUMP["ASYM2"]}
check("PORT.5 THE DEEP-WINDOW CONTROL AGREES WITH PORT.3: the deeper "
      "unfiltered three-actor window carries the defect at depths 2 and 3 "
      "and still carries none at depths 0 and 1, so ABC3's empty "
      "lumpability axis survives a window one level deeper than its own",
      ARMD["lump"][0][1] == 0 and ARMD["lump"][1][1] == 0
      and sum(ARMD["lump"][d][1] for d in ARMD["lump"]) > 0,
      f"ARM-D by depth "
      f"{ {d: (ARMD['lump'][d][0], ARMD['lump'][d][1]) for d in sorted(ARMD['lump'])} }")

report("SEC 4 block time", f"{time.time() - _t:.0f}s")


# ===========================================================================
# SEC 5.  W-A — THE 2x2x2 CENSUS
# ===========================================================================

sec("SEC 5  W-A — THE THREE-WAY CENSUS: every closed square, all three "
    "statuses")

_t = time.time()

SQ = []          # one row per closed square of the pooled population
for nm in POPNAMES:
    L = LUMP[nm]
    K = CTL[nm]
    for h, eA, eB, v, vr, oA, oB, RA, RB in ROWS[nm]:
        d = len(h)
        base_bad = L["sig"](h) in L["lump"][d][2]
        sh_bad = (L["sig"](h + (eA,)) in L["lump"][d + 1][2]
                  or L["sig"](h + (eB,)) in L["lump"][d + 1][2])
        noncomm = (L["sig"](h + (eA, eB)) != L["sig"](h + (eB, eA)))
        deep_bad = K["sig"](h) in K["lump"][d][2]
        SQ.append(dict(pop=nm, h=h, eA=eA, eB=eB, v=v, d=d,
                       kinds=(eA[0], eB[0]),
                       curved=(v != 1),
                       refused=(vr is None),
                       arb=arb_of(h, eA, eB),
                       lumpA=base_bad,
                       lumpW=(base_bad or sh_bad),
                       lumpB=noncomm,
                       lumpC=deep_bad))
SQ.sort(key=lambda r: (r["pop"], sk((r["h"], r["eA"], r["eB"]))))
report("the pooled square population", f"{len(SQ)} closed squares over "
       f"{len(POPNAMES)} populations "
       f"{ {nm: sum(1 for r in SQ if r['pop'] == nm) for nm in POPNAMES} }")


def tri(r, lump="lumpA"):
    return (r["curved"], r["refused"], r[lump])


def print_222(label, rows, lump="lumpA"):
    """The 2x2x2 contingency table, printed BOTH WAYS: as the eight cells
    in (J, reversal, lumpability) order and again in (lumpability,
    reversal, J) order, so the two readings must agree cell for cell."""
    T = Counter(tri(r, lump) for r in rows)
    print(f"  [DATA] {label} — 2x2x2, WAY 1 "
          f"(J-status x reversal-status x {lump}):")
    print(f"           {'curved':>8} {'refused':>8} {'non-lump':>9} "
          f"{'count':>7}")
    for c in (True, False):
        for rr in (True, False):
            for ll in (True, False):
                print(f"           {str(c):>8} {str(rr):>8} {str(ll):>9} "
                      f"{T[(c, rr, ll)]:>7}")
    print(f"  [DATA] {label} — 2x2x2, WAY 2 (the same eight cells "
          f"re-indexed {lump} x reversal x J; the two readings must agree "
          f"cell for cell):")
    T2 = Counter()
    for r in rows:
        T2[(r[lump], r["refused"], r["curved"])] += 1
    agree = all(T[(c, rr, ll)] == T2[(ll, rr, c)]
                for c in (True, False) for rr in (True, False)
                for ll in (True, False))
    print(f"           {'non-lump':>9} {'refused':>8} {'curved':>8} "
          f"{'count':>7}")
    for ll in (True, False):
        for rr in (True, False):
            for c in (True, False):
                print(f"           {str(ll):>9} {str(rr):>8} {str(c):>8} "
                      f"{T2[(ll, rr, c)]:>7}")
    print(f"           WAY 1 == WAY 2 cell for cell: {agree}")
    m = {"curved": sum(1 for r in rows if r["curved"]),
         "refused": sum(1 for r in rows if r["refused"]),
         "arb-carrying": sum(1 for r in rows if r["arb"]),
         lump: sum(1 for r in rows if r[lump]),
         "total": len(rows)}
    print(f"  [DATA] {label} — marginals: {m}")
    sys.stdout.flush()
    return T, agree


_agrees = []
for nm in POPNAMES:
    _T, _ag = print_222(ARMS[nm]["label"], [r for r in SQ if r["pop"] == nm])
    _agrees.append(_ag)
POOL_T, _ag = print_222("POOLED (all four populations)", SQ)
_agrees.append(_ag)
check("A.1 THE 2x2x2 CENSUS IS PRINTED BOTH WAYS AND THE TWO READINGS "
      "AGREE CELL FOR CELL, per population and pooled.  The table is "
      "re-indexed from (J, reversal, lumpability) to (lumpability, "
      "reversal, J) by an independent pass over the squares",
      all(_agrees), f"{sum(_agrees)}/{len(_agrees)} tables agree",
      corollary_of="a re-indexing of the same counter; it gates the "
      "printing, not the census")

# --- both ways: by holonomy value and by kind pair ------------------------
print()
print("  [A.2]  THE CENSUS BY HOLONOMY VALUE (WAY 1 of the loop axis).")
byval = defaultdict(Counter)
for r in SQ:
    byval[r["v"]][(r["refused"], r["lumpA"])] += 1
print(f"           {'v':>8} {'squares':>8}  (refused, non-lumpable) census")
for v in sorted(byval, key=lambda z: (z != 1, z)):
    print(f"           {str(v):>8} {sum(byval[v].values()):>8}  "
          f"{ {f'ref={k[0]},nl={k[1]}': n for k, n in sorted(byval[v].items(), key=str)} }")

print()
print("  [A.3]  THE CENSUS BY LOOP CLASS (WAY 2 of the loop axis: the "
      "ordered kind pair,")
print("         which is D72's and D74's own defect-kind axis).")
bykind = defaultdict(Counter)
for r in SQ:
    bykind[r["kinds"]][tri(r)] += 1
print(f"           {'kinds':>8} {'squares':>8}  (curved, refused, "
      f"non-lumpable) census")
for k in sorted(bykind, key=str):
    print(f"           {str(k):>8} {sum(bykind[k].values()):>8}  "
          f"{ {f'{int(a)}{int(b)}{int(c)}': n for (a, b, c), n in sorted(bykind[k].items(), key=str)} }")

print()
print("  [A.4]  THE CENSUS BY BASE DEPTH.")
bydep = defaultdict(Counter)
for r in SQ:
    bydep[(r["pop"], r["d"])][tri(r)] += 1
for k in sorted(bydep, key=str):
    print(f"           {str(k):>14}  "
          f"{ {f'{int(a)}{int(b)}{int(c)}': n for (a, b, c), n in sorted(bydep[k].items(), key=str)} }")

# --- the two control readings of lumpability -------------------------------
print()
print("  [A.5]  THE THREE CONTROL READINGS OF LUMPABILITY, POOLED.")
POOL_C, _agC = print_222("POOLED, LUMP-C (the deep-window control: each "
                         "population read through the deepest committed "
                         "window available for its own grammar)",
                         SQ, "lumpC")
POOL_W, _agW = print_222("POOLED, LUMP-W (the square's whole window: base "
                         "class at depth d, or either shoulder class at "
                         "depth d+1)", SQ, "lumpW")
POOL_B, _agB = print_222("POOLED, LUMP-B (DC1's sigma-commuting predicate "
                         "at the square itself)", SQ, "lumpB")

# --- the horizon dependence, measured --------------------------------------
_hdiff = {nm: sum(1 for r in SQ
                  if r["pop"] == nm and r["lumpA"] != r["lumpC"])
          for nm in POPNAMES}
report("horizon control — squares whose lumpability status differs "
       "between the population's own window and the deep-window control",
       {nm: f"{_hdiff[nm]} of "
        f"{sum(1 for r in SQ if r['pop'] == nm)}" for nm in POPNAMES})
report("non-lumpable square counts, own window vs deep window",
       {nm: (sum(1 for r in SQ if r["pop"] == nm and r["lumpA"]),
             sum(1 for r in SQ if r["pop"] == nm and r["lumpC"]))
        for nm in POPNAMES})
check("A.6 THE LUMPABILITY STATUS OF A SQUARE IS HORIZON-DEPENDENT IN "
      "PRINCIPLE, AND THE DEPENDENCE IS MEASURED RATHER THAN ASSUMED "
      "AWAY.  The relative-horizon kernel k_r depends on the remaining "
      "horizon, so the same square read at its population's own window "
      "and at the deepest available window for its grammar need not "
      "agree.  The exact number of squares on which the two readings "
      "differ is printed above, per population; every verdict below is "
      "stated at the population's own window with the deep-window reading "
      "carried beside it",
      True,
      f"differing squares by population {_hdiff}; pooled "
      f"{sum(_hdiff.values())} of {len(SQ)}",
      corollary_of="a reported measurement with no failing branch; it "
      "records a scope fact, it does not test one")

report("SEC 5 block time", f"{time.time() - _t:.0f}s")


# ===========================================================================
# SEC 6.  W-B — THE CONTAINMENT STRUCTURE AND ITS BOUNDARY CENSUSES
# ===========================================================================

sec("SEC 6  W-B — THE CONTAINMENT STRUCTURE: every implication, every "
    "boundary")

_t = time.time()


def bcensus(label, rows):
    """The exact boundary census of a difference set: by population, by
    kind pair, by base depth, and by holonomy value."""
    if not rows:
        print(f"           {label}: EMPTY")
        return
    print(f"           {label}: {len(rows)} squares")
    print(f"             by population "
          f"{dict(sorted(Counter(r['pop'] for r in rows).items()))}")
    print(f"             by kind pair "
          f"{fmtk(Counter(r['kinds'] for r in rows))}")
    print(f"             by base depth "
          f"{dict(sorted(Counter(r['d'] for r in rows).items()))}")
    print(f"             by holonomy value "
          f"{fmt(Counter(r['v'] for r in rows))}")
    sys.stdout.flush()


def implication(name, lhs, rhs, rows, lump="lumpA"):
    """Test lhs => rhs exactly and census the two difference sets."""
    L = [r for r in rows if lhs(r)]
    Rr = [r for r in rows if rhs(r)]
    LnotR = [r for r in L if not rhs(r)]
    RnotL = [r for r in Rr if not lhs(r)]
    holds = not LnotR
    conv = not RnotL
    if holds and conv:
        kind = "EQUAL (the same set of squares)"
    elif holds:
        kind = "STRICT CONTAINMENT lhs subset rhs"
    elif conv:
        kind = "STRICT CONTAINMENT rhs subset lhs"
    else:
        kind = "CROSSING (neither contains the other)"
    print()
    print(f"  [IMPL] {name}")
    print(f"           |lhs| = {len(L)}, |rhs| = {len(Rr)}, "
          f"|lhs and rhs| = {len(L) - len(LnotR)}   ->  {kind}")
    bcensus("BOUNDARY  lhs \\ rhs (counterexamples to lhs => rhs)", LnotR)
    bcensus("BOUNDARY  rhs \\ lhs (counterexamples to rhs => lhs)", RnotL)
    return dict(name=name, kind=kind, nL=len(L), nR=len(Rr),
                LnotR=LnotR, RnotL=RnotL, holds=holds, conv=conv)


IMPL = {}
IMPL["C=>A"] = implication(
    "CURVED (J != 1)  =>  ARBITRATION-CARRYING   [D74 x LD, C.3b]",
    lambda r: r["curved"], lambda r: r["arb"], SQ)
IMPL["R<=>A"] = implication(
    "REFUSED (no priced reversed record)  <=>  ARBITRATION-CARRYING   "
    "[LD C.3a, re-gated]",
    lambda r: r["refused"], lambda r: r["arb"], SQ)
IMPL["C=>R"] = implication(
    "CURVED  =>  REFUSED   [the curvature inside the wall]",
    lambda r: r["curved"], lambda r: r["refused"], SQ)
IMPL["C=>L"] = implication(
    "CURVED  =>  NON-LUMPABLE   [the open question]",
    lambda r: r["curved"], lambda r: r["lumpA"], SQ)
IMPL["L=>R"] = implication(
    "NON-LUMPABLE  =>  REFUSED   [the open question]",
    lambda r: r["lumpA"], lambda r: r["refused"], SQ)
IMPL["L=>A"] = implication(
    "NON-LUMPABLE  =>  ARBITRATION-CARRYING   [the open question]",
    lambda r: r["lumpA"], lambda r: r["arb"], SQ)

check("B.1 THE REVERSAL STATUS AND THE ARBITRATION STATUS ARE THE SAME "
      "SET OF SQUARES, EXACTLY.  Both difference sets are empty on all "
      "17,277 squares, in both directions.  LD's biconditional is "
      "therefore not merely reproduced as a count: the two statuses are "
      "the same subset of the pooled population, square for square, so "
      "the middle axis of the 2x2x2 may be read as either without "
      "ambiguity",
      IMPL["R<=>A"]["holds"] and IMPL["R<=>A"]["conv"],
      f"refused \\ arb {len(IMPL['R<=>A']['LnotR'])}; arb \\ refused "
      f"{len(IMPL['R<=>A']['RnotL'])}; |refused| = "
      f"{IMPL['R<=>A']['nL']}")

check("B.2 CURVATURE IS STRICTLY CONTAINED IN IRREVERSIBILITY, and the "
      "boundary is exhibited: every curved square is refused, and the "
      "difference set — the flat squares the law also refuses — is "
      "censused above by population, kind pair, depth and value.  This is "
      "LD's containment, re-measured square by square rather than as two "
      "counts",
      IMPL["C=>R"]["holds"] and not IMPL["C=>R"]["conv"],
      f"curved {IMPL['C=>R']['nL']}, refused {IMPL['C=>R']['nR']}, "
      f"boundary (flat and refused) {len(IMPL['C=>R']['RnotL'])}")

_CL = IMPL["C=>L"]
check("B.3 CURVATURE AND NON-LUMPABILITY CROSS: neither contains the "
      "other.  There are curved squares on lumpable classes and "
      "non-lumpable classes carrying flat squares, and both difference "
      "sets are non-empty and censused above.  A weld theorem cannot "
      "route through 'curved therefore non-lumpable' or its converse at "
      "this scope",
      (not _CL["holds"]) and (not _CL["conv"]),
      f"curved and lumpable {len(_CL['LnotR'])}; non-lumpable and flat "
      f"{len(_CL['RnotL'])}; curved {_CL['nL']}; non-lumpable "
      f"{_CL['nR']}")

_LA = IMPL["L=>A"]
check("B.4 NON-LUMPABILITY AND IRREVERSIBILITY CROSS TOO — measured, "
      "with both difference sets censused above (gate repaired per the "
      "hostile round: the predicate now fails if either implication "
      "holds)",
      (not _LA["holds"]) and (not _LA["conv"]),
      f"non-lumpable \\ refused {len(_LA['LnotR'])}; refused \\ "
      f"non-lumpable {len(_LA['RnotL'])}; verdict "
      f"{_LA['kind']}")

# --- the same lattice under the two control readings ----------------------
print()
print("  [B.5]  THE SAME LATTICE UNDER THE THREE CONTROL READINGS OF")
print("         LUMPABILITY, so that no containment verdict rests on the")
print("         choice of per-square port or on the population's own cap.")
_ctl = {}
for lump in ("lumpC", "lumpW", "lumpB"):
    a = implication(f"CURVED  =>  NON-LUMPABLE [{lump}]",
                    lambda r: r["curved"], lambda r, l=lump: r[l], SQ)
    b = implication(f"NON-LUMPABLE [{lump}]  =>  ARBITRATION-CARRYING",
                    lambda r, l=lump: r[l], lambda r: r["arb"], SQ)
    _ctl[lump] = (a, b)
check("B.5 THE VERDICT ON CURVATURE-VERSUS-NON-LUMPABILITY SURVIVES ALL "
      "THREE CONTROL READINGS OF THE PER-SQUARE PORT.  Under LUMP-C (the "
      "deep-window control), under LUMP-W (the square's whole window) and "
      "under LUMP-B (DC1's sigma-commuting predicate at the square "
      "itself), curvature still fails to imply non-lumpability, with the "
      "counterexample count printed for each.  Under LUMP-C and LUMP-W "
      "the two loci cross as they do under the primary reading; under "
      "LUMP-B the containment is the degenerate one, because LUMP-B is "
      "the EMPTY SET (gate B.5a).  No reading makes curvature imply "
      "non-lumpability, so the finding is a property of the two loci and "
      "not of the porting convention or of the population's own cap",
      all((not _ctl[l][0]["holds"]) for l in ("lumpC", "lumpW", "lumpB")),
      "; ".join(f"{l}: curved-and-lumpable {len(_ctl[l][0]['LnotR'])}, "
                f"non-lumpable-and-flat {len(_ctl[l][0]['RnotL'])}, "
                f"verdict {_ctl[l][0]['kind']}"
                for l in ("lumpC", "lumpW", "lumpB")))

_nb = sum(1 for r in SQ if r["lumpB"])
check("B.5a THE PORTED CONFIGURATION MAP IS ORDER-BLIND AT EVERY CLOSED "
      "EXCHANGE SQUARE, EXHAUSTIVELY: sigma(h.eA.eB) = sigma(h.eB.eA) on "
      "all 17,277 squares of all four populations, curved and flat "
      "alike.  U1's DC1 census excludes the sigma-non-commuting pairs "
      "'by name'; at closed squares there are none to exclude.  ROUND "
      "CORRECTION (LOG #24): this endpoint fact does NOT locate the DC2 "
      "signal — order-blindness at the endpoint says nothing about the "
      "two SHOULDERS, and the round exhibited a square-local DC2 "
      "predicate (equal shoulder classes, unequal shoulder kernels) "
      "that is NON-EMPTY: 464/17,277 pooled, 48/1,546 on AB4, 88 "
      "curved, with a printed witness.  What this gate measures is "
      "endpoint order-blindness, exhaustively — no more",
      _nb == 0 and len(SQ) > 0,
      f"sigma-non-commuting closed squares: {_nb} of {len(SQ)}; "
      f"holonomy-carrying squares among them: "
      f"{sum(1 for r in SQ if r['lumpB'] and r['curved'])} of "
      f"{sum(1 for r in SQ if r['curved'])}")

# --- the pairwise verdict matrix ------------------------------------------
print()
print("  [B.6]  THE PAIRWISE VERDICT MATRIX (the three loci, both ways).")
_SETS = {"CURVED": lambda r: r["curved"],
         "REFUSED": lambda r: r["refused"],
         "NON-LUMPABLE": lambda r: r["lumpA"]}
_pairverdict = {}
_names = sorted(_SETS)
print(f"           {'pair':<32} {'|X|':>6} {'|Y|':>6} {'|X&Y|':>7} "
      f"{'X\\Y':>6} {'Y\\X':>6}  verdict")
for i in range(len(_names)):
    for j in range(i + 1, len(_names)):
        X, Y = _names[i], _names[j]
        fx, fy = _SETS[X], _SETS[Y]
        nx = sum(1 for r in SQ if fx(r))
        ny = sum(1 for r in SQ if fy(r))
        nb = sum(1 for r in SQ if fx(r) and fy(r))
        xy = nx - nb
        yx = ny - nb
        vd = ("EQUAL" if xy == 0 and yx == 0 else
              f"{X} SUBSET {Y}" if xy == 0 else
              f"{Y} SUBSET {X}" if yx == 0 else "CROSSING")
        _pairverdict[(X, Y)] = vd
        print(f"           {X + ' vs ' + Y:<32} {nx:>6} {ny:>6} {nb:>7} "
              f"{xy:>6} {yx:>6}  {vd}")
sys.stdout.flush()

report("SEC 6 block time", f"{time.time() - _t:.0f}s")


# ===========================================================================
# SEC 7.  W-C — THE WELD CANDIDATE
# ===========================================================================

sec("SEC 7  W-C — THE WELD CANDIDATE: does one grammar quantity predict "
    "all three?")

print("""  A candidate quantity q is a WELD iff the status triple (curved,
  refused, non-lumpable) is a FUNCTION of q on the pooled population:
  no two squares with the same q-value carry different status triples.
  Each candidate is also scored against each status separately, so a
  candidate that predicts one address and not the others is visible as
  such rather than merely failing.

  The candidates are read on the endpoint record sigma_AB = h.eA.eB.
  Every candidate is first tested for ORDER-BLINDNESS — the same value on
  sigma_BA — since a square-level quantity that depends on the traversal
  order is not a property of the square.""")

_t = time.time()


def view_stats(seq):
    v = b1_fullview(list(seq))
    comps = v.components()
    sizes = sorted(len(g) for base, g in comps)
    return dict(ncreated=len(v.created), nlive=len(v.live),
                ncomp=len(comps), maxcomp=(max(sizes) if sizes else 0),
                joinsig=tuple(sizes))


_VS = {}


def vs(seq):
    key = tuple(seq)
    out = _VS.get(key)
    if out is None:
        out = view_stats(key)
        _VS[key] = out
    return out


CANDIDATES = [
    ("narb", "the arbitration count in the endpoint record",
     lambda r, s: sum(1 for e in s if e[0] == "r")),
    ("narb>=1", "arbitration-carrying (LD's one-kind address, as a "
     "binary quantity)",
     lambda r, s: sum(1 for e in s if e[0] == "r") >= 1),
    ("ncreated", "the created-version count of the endpoint view "
     "(LD's mechanism: the arbitration is the only realised kind that "
     "creates a version)",
     lambda r, s: vs(s)["ncreated"]),
    ("ncreated>=1", "the endpoint record holds a created (non-V0) version",
     lambda r, s: vs(s)["ncreated"] >= 1),
    ("nlive", "the live-proposal count of the endpoint view",
     lambda r, s: vs(s)["nlive"]),
    ("ncomp", "the number of live-proposal (join) components",
     lambda r, s: vs(s)["ncomp"]),
    ("maxcomp", "the largest live-proposal component — the join width",
     lambda r, s: vs(s)["maxcomp"]),
    ("joinsig", "the full join structure: the sorted multiset of "
     "live-proposal component sizes",
     lambda r, s: vs(s)["joinsig"]),
    ("J", "the holonomy value itself",
     lambda r, s: r["v"]),
    ("kindpair", "the exchanged kind pair (D72's own defect axis)",
     lambda r, s: r["kinds"]),
    ("kindmultiset", "the multiset of event kinds in the endpoint record",
     lambda r, s: tuple(sorted(Counter(e[0] for e in s).items()))),
    ("basedepth", "the square's base depth",
     lambda r, s: r["d"]),
    ("narb_base", "the arbitration count of the square's BASE record h",
     lambda r, s: sum(1 for e in r["h"] if e[0] == "r")),
    ("joinsig_base", "the join structure at the square's BASE record",
     lambda r, s: vs(r["h"])["joinsig"]),
    ("sigma_base", "the DC2 instrument's OWN state at the square's base — "
     "the ported configuration sigma(h) with its depth, read in the "
     "population's own window (window-relative, and a quantity that "
     "predicts lumpability BY CONSTRUCTION: it is included precisely to "
     "see whether it predicts anything else)",
     lambda r, s: (r["pop"], r["d"], LUMP[r["pop"]]["sig"](r["h"]))),
    ("sigma_end", "the ported configuration of the ENDPOINT record, read "
     "in the population's own window (window-relative)",
     lambda r, s: (r["pop"], LUMP[r["pop"]]["sig"](s))),
]

CAND_VAL = {}
_orderblind = {}
for name, desc, f in CANDIDATES:
    vals_ab, vals_ba = [], []
    for r in SQ:
        sAB = tuple(r["h"]) + (r["eA"], r["eB"])
        sBA = tuple(r["h"]) + (r["eB"], r["eA"])
        vals_ab.append(f(r, sAB))
        vals_ba.append(f(r, sBA))
    CAND_VAL[name] = vals_ab
    nd = sum(1 for a, b in zip(vals_ab, vals_ba) if a != b)
    _orderblind[name] = nd
    print(f"  [DATA] candidate {name:<14} order-blind on "
          f"{len(SQ) - nd}/{len(SQ)} squares"
          + ("" if nd == 0 else f"  (ORDER-DEPENDENT on {nd}; the "
             f"sigma_AB reading is used and the dependence is declared)"))
sys.stdout.flush()

check("C.0 LD's MECHANISM SENTENCE IS AN IDENTITY ON THIS POPULATION — "
      "ENTAILED by the encoding given D.1, not discovered (the round's "
      "relabel, LOG #24): View.created gains exactly one entry per "
      "arbitration and one per merge, and D.1 shows 0 merges, so "
      "ncreated = narb is forced up to vname injectivity; the measured "
      "residue is the 248 squares at narb = 2.  The check: "
      "the created-version count of a square's endpoint record "
      "equals its arbitration count on every one of the 17,277 squares.  "
      "The arbitration is the only realised kind that creates a version "
      "(the merge, the other creating kind, is not reached — gate D.1), "
      "and no two arbitrations of one record create the same version.  "
      "The two candidates 'narb' and 'ncreated' are therefore the SAME "
      "quantity here and are scored separately only so that the table "
      "shows it",
      CAND_VAL["narb"] == CAND_VAL["ncreated"],
      f"squares where the created-version count differs from the "
      f"arbitration count: "
      f"{sum(1 for a, b in zip(CAND_VAL['narb'], CAND_VAL['ncreated']) if a != b)}"
      f" of {len(SQ)}")

print()
print("  [C.1]  THE PREDICTION TABLE.  For each candidate: the number of")
print("         distinct values it takes, whether it predicts each status")
print("         separately, whether it predicts the full triple, and the")
print("         exact failure count (squares sitting in a value-class that")
print("         carries more than one status triple).")
print()
print(f"      {'candidate':<14} {'values':>6}  {'J':>5} {'REV':>5} "
      f"{'LUMP':>5}  {'TRIPLE':>7}  {'failing squares':>15}")

WELD = []
CAND_ROWS = []
for name, desc, f in CANDIDATES:
    vals = CAND_VAL[name]
    by = defaultdict(set)
    byC, byR, byL = defaultdict(set), defaultdict(set), defaultdict(set)
    cnt = Counter()
    for q, r in zip(vals, SQ):
        by[q].add(tri(r))
        byC[q].add(r["curved"])
        byR[q].add(r["refused"])
        byL[q].add(r["lumpA"])
        cnt[q] += 1
    okC = all(len(s) == 1 for s in byC.values())
    okR = all(len(s) == 1 for s in byR.values())
    okL = all(len(s) == 1 for s in byL.values())
    okT = all(len(s) == 1 for s in by.values())
    failsq = sum(cnt[q] for q in by if len(by[q]) > 1)
    CAND_ROWS.append((name, len(by), okC, okR, okL, okT, failsq,
                      {q: sorted(by[q]) for q in by if len(by[q]) > 1},
                      cnt))
    if okT:
        WELD.append(name)
    print(f"      {name:<14} {len(by):>6}  {str(okC):>5} {str(okR):>5} "
          f"{str(okL):>5}  {str(okT):>7}  {failsq:>15}")
sys.stdout.flush()

print()
print("  [C.2]  THE FAILURE PATTERN, CANDIDATE BY CANDIDATE.  For every")
print("         candidate that is not a weld, the value-classes that carry")
print("         more than one status triple, with the exact split.")
for (name, nv, okC, okR, okL, okT, failsq, bad, cnt) in CAND_ROWS:
    if okT:
        print(f"      {name}: NO FAILURE — this candidate predicts the "
              f"full triple")
        continue
    print(f"      {name}: {len(bad)} of {nv} value-classes carry more than "
          f"one status triple ({failsq} squares)")
    for q in sorted(bad, key=str)[:12]:
        sub = Counter(tri(r) for q2, r in zip(CAND_VAL[name], SQ)
                      if q2 == q)
        print(f"        value {str(q):<28} n={cnt[q]:<6} triples "
              f"{ {f'{int(a)}{int(b)}{int(c)}': n for (a, b, c), n in sorted(sub.items(), key=str)} }")
    if len(bad) > 12:
        print(f"        ... {len(bad) - 12} further value-classes (the "
              f"count above is complete)")
sys.stdout.flush()

check("C.1 THE ARBITRATION IS AN EXACT PREDICTOR OF THE IRREVERSIBILITY "
      "ADDRESS AND OF NOTHING ELSE.  The binary quantity narb >= 1 "
      "predicts the reversal status on every one of the 17,277 squares — "
      "that is LD's biconditional restated as a prediction — and it "
      "predicts neither curvature nor lumpability: its two value-classes "
      "both carry both curvature statuses and both lumpability statuses",
      [r for r in CAND_ROWS if r[0] == "narb>=1"][0][3]
      and not [r for r in CAND_ROWS if r[0] == "narb>=1"][0][2]
      and not [r for r in CAND_ROWS if r[0] == "narb>=1"][0][4],
      f"narb>=1: predicts J = {[r for r in CAND_ROWS if r[0] == 'narb>=1'][0][2]}, "
      f"predicts reversal = {[r for r in CAND_ROWS if r[0] == 'narb>=1'][0][3]}, "
      f"predicts lumpability = {[r for r in CAND_ROWS if r[0] == 'narb>=1'][0][4]}")

check("C.2 THE HOLONOMY VALUE ITSELF IS NOT A WELD EITHER.  J predicts "
      "its own status by definition and predicts the reversal status "
      "one-sidedly only — every non-unit value class is wholly refused, "
      "but the unit class carries both statuses — and it predicts "
      "lumpability nowhere",
      not [r for r in CAND_ROWS if r[0] == "J"][0][5],
      f"J: predicts reversal = {[r for r in CAND_ROWS if r[0] == 'J'][0][3]}, "
      f"predicts lumpability = {[r for r in CAND_ROWS if r[0] == 'J'][0][4]}, "
      f"predicts the triple = {[r for r in CAND_ROWS if r[0] == 'J'][0][5]}")

_sb = [r for r in CAND_ROWS if r[0] == "sigma_base"][0]
check("C.3 THE CONFIGURATION MAP DOES NOT SEE THE CURVATURE.  sigma_base "
      "— the DC2 instrument's own state at the square's base, which "
      "predicts the lumpability status BY CONSTRUCTION — is scored "
      "against the other two addresses and predicts neither.  The "
      "instrument that defines one address is blind to the other two, "
      "which is the sharp form of the crossing measured at B.3 and B.4",
      _sb[4] and not _sb[2] and not _sb[3],
      f"sigma_base: {_sb[1]} distinct values; predicts J = {_sb[2]}, "
      f"predicts reversal = {_sb[3]}, predicts lumpability = {_sb[4]}, "
      f"predicts the triple = {_sb[5]}")

check("C.4 NO SINGLE CANDIDATE GRAMMAR QUANTITY IS A WELD.  The pin's own "
      "candidates — the arbitration count, LD's created-version count, "
      "the join / live-proposal structure, and J itself — are each tested "
      "against the full status triple on every square, together with the "
      "base-read and configuration-map candidates, and the failure "
      "pattern of each is the deliverable printed above",
      len(WELD) == 0,
      f"welds found: {WELD if WELD else 'none'} of "
      f"{len(CANDIDATES)} candidates tested")

# --- the joint scan, labelled as secondary --------------------------------
print()
print("  [C-SCAN]  THE MINIMAL-SET SCAN, reported as a SECONDARY reading "
      "and")
print("         not as an answer to the pin's question, which asks for ONE")
print("         quantity.  How many of these quantities does it take to")
print("         predict all three statuses, and does any combination")
print("         predict JOINTLY — that is, without simply carrying one")
print("         exact single-status predictor per address?")
_cn = [c[0] for c in CANDIDATES]
_CODE = [(int(r["curved"]) * 4 + int(r["refused"]) * 2 + int(r["lumpA"]))
         for r in SQ]
_COL = {n: CAND_VAL[n] for n in _cn}


def subset_predicts(names):
    seen = {}
    cols = [_COL[n] for n in names]
    for i, code in enumerate(_CODE):
        key = tuple(c[i] for c in cols)
        prev = seen.get(key)
        if prev is None:
            seen[key] = code
        elif prev != code:
            return False, len(seen)
    return True, len(seen)


_exactJ = {r[0] for r in CAND_ROWS if r[2]}
_exactR = {r[0] for r in CAND_ROWS if r[3]}
_exactL = {r[0] for r in CAND_ROWS if r[4]}
report("exact single-status predictors, by address",
       {"J": sorted(_exactJ), "reversal": sorted(_exactR),
        "lumpability": sorted(_exactL)})

_pairs_ok = []
for i in range(len(_cn)):
    for j in range(i + 1, len(_cn)):
        ok, nv = subset_predicts((_cn[i], _cn[j]))
        if ok:
            _pairs_ok.append((_cn[i], _cn[j], nv))
report("PAIRS of candidates that jointly predict the full status triple",
       _pairs_ok if _pairs_ok else f"none of "
       f"{len(_cn) * (len(_cn) - 1) // 2}")

_trip_ok = []
_trip_joint = []
for i in range(len(_cn)):
    for j in range(i + 1, len(_cn)):
        for k in range(j + 1, len(_cn)):
            t = (_cn[i], _cn[j], _cn[k])
            ok, nv = subset_predicts(t)
            if ok:
                _trip_ok.append((t, nv))
                if not (set(t) & _exactJ and set(t) & _exactR
                        and set(t) & _exactL):
                    _trip_joint.append((t, nv))
report("TRIPLES of candidates that jointly predict the full status "
       "triple", f"{len(_trip_ok)} of "
       f"{len(_cn) * (len(_cn) - 1) * (len(_cn) - 2) // 6}")
report("of those, triples that predict JOINTLY — without carrying an "
       "exact single-status predictor for each of the three addresses",
       _trip_joint if _trip_joint else "none")
for t, nv in _trip_ok[:8]:
    print(f"           {t}  ({nv} value-classes)")
if len(_trip_ok) > 8:
    print(f"           ... {len(_trip_ok) - 8} further predicting triples")
check("C.5 IT TAKES EXACTLY THREE OF THESE QUANTITIES, ONE PER ADDRESS, "
      "AND THERE IS NO JOINT PREDICTION.  No single candidate and no "
      "pair predicts the status triple; triples do, and every triple "
      "that does carries an exact predictor of curvature, an exact "
      "predictor of the reversal status and an exact predictor of "
      "lumpability.  Nothing is welded by combining: the three addresses "
      "are separately predictable and remain three",
      len(WELD) == 0 and len(_pairs_ok) == 0 and len(_trip_ok) > 0
      and len(_trip_joint) == 0,
      f"welds {len(WELD)}; predicting pairs {len(_pairs_ok)} of "
      f"{len(_cn) * (len(_cn) - 1) // 2}; predicting triples "
      f"{len(_trip_ok)} of "
      f"{len(_cn) * (len(_cn) - 1) * (len(_cn) - 2) // 6}; of those, "
      f"jointly-predicting (no per-address predictor inside) "
      f"{len(_trip_joint)}")

report("SEC 7 block time", f"{time.time() - _t:.0f}s")


# ===========================================================================
# SEC 8.  W-D — THE RECORD-GRAIN HOOK, NAMED AND NOT RUN
# ===========================================================================

sec("SEC 8  W-D — THE RECORD-GRAIN HOOK (U2b): NAMED, NOT RUN")

print("""  Everything in this receipt is measured at CUT GRAIN on the committed
  transport populations: a square's three statuses are read from its
  base, its exchanged pair and its endpoint record at the declared caps.
  The record-grain question — whether the same address separates the
  refusing from the dividing masks of the two-sided test at depth 15 — is
  U2b's, is conditional on U1c returning N4, and is NOT run here.  No
  number in this receipt bears on it, and no claim is made about it: the
  populations here do not reach depth 15, do not carry the lag >= 2 masks
  the U1b round named as the only door left in that class, and do not
  contain a single realised merge event (LD's D.4 scope limit, which this
  receipt inherits unchanged along with LD's functor).  If U1c returns
  N4, U2b asks of the refusing masks exactly the three questions W-A asks
  of a square; if it does not, U2b does not open.""")

_merges = sum(1 for r in SQ
              for e in tuple(r["h"]) + (r["eA"], r["eB"]) if e[0] == "m")
check("D.1 THE MERGE SECTOR IS NOT REACHED, and this receipt inherits "
      "LD's D.4 scope limit unchanged: no merge event is realised in any "
      "of the four populations, so nothing here — no status, no "
      "containment, no candidate — says anything about how the three "
      "instruments behave on a merge",
      _merges == 0,
      f"merge events realised across all {len(SQ)} censused squares: "
      f"{_merges}; kinds realised "
      f"{sorted({e[0] for r in SQ for e in tuple(r['h']) + (r['eA'], r['eB'])})}")


# ===========================================================================
# SEC 9.  DETERMINISM
# ===========================================================================

sec("SEC 9  DETERMINISM PROBE")

_t = time.time()
_SQ2 = sorted(SQ, key=lambda r: (sk((r["h"], r["eA"], r["eB"])), r["pop"]),
              reverse=True)
_T2 = Counter(tri(r) for r in _SQ2)
_impl2 = {}
for k, (lhs, rhs) in (("C=>A", (lambda r: r["curved"], lambda r: r["arb"])),
                      ("C=>L", (lambda r: r["curved"],
                                lambda r: r["lumpA"])),
                      ("L=>A", (lambda r: r["lumpA"], lambda r: r["arb"]))):
    _impl2[k] = (sum(1 for r in _SQ2 if lhs(r) and not rhs(r)),
                 sum(1 for r in _SQ2 if rhs(r) and not lhs(r)))
_impl1 = {k: (len(IMPL[k]["LnotR"]), len(IMPL[k]["RnotL"]))
          for k in ("C=>A", "C=>L", "L=>A")}
_cand2 = {}
for name, desc, f in CANDIDATES:
    by = defaultdict(set)
    for r in _SQ2:
        sAB = tuple(r["h"]) + (r["eA"], r["eB"])
        by[f(r, sAB)].add(tri(r))
    _cand2[name] = (len(by), all(len(s) == 1 for s in by.values()))
_cand1 = {r[0]: (r[1], r[5]) for r in CAND_ROWS}
check("DET.1 THE CENSUS IS DETERMINISTIC AND ORDER-INDEPENDENT, AND THE "
      "PROBE EXERCISES THE DECIDING OBJECTS.  Traversed in the reverse "
      "stable-key order, three objects are recompared: the full pooled "
      "2x2x2 table cell for cell; the boundary sizes of the three "
      "deciding implications; and every candidate's value count and weld "
      "verdict.  All set iteration that feeds a printed number is keyed by "
      "the hash-seed-independent sk()",
      _T2 == POOL_T and _impl2 == _impl1 and _cand2 == _cand1,
      f"2x2x2 identical = {_T2 == POOL_T}; implication boundaries "
      f"identical = {_impl2 == _impl1} {_impl1}; candidate table "
      f"identical = {_cand2 == _cand1} ({len(_cand1)} candidates)")
report("SEC 9 block time", f"{time.time() - _t:.0f}s")


# ===========================================================================
# SEC 10.  THE VERDICT
# ===========================================================================

print()
print("=" * 78)
print("SEC 10  THE VERDICT, AGAINST THE PIN'S PRE-REGISTERED OUTCOMES")
print("=" * 78)

_setC = {(r["pop"], sk((r["h"], r["eA"], r["eB"]))) for r in SQ
         if r["curved"]}
_setR = {(r["pop"], sk((r["h"], r["eA"], r["eB"]))) for r in SQ
         if r["refused"]}
_setL = {(r["pop"], sk((r["h"], r["eA"], r["eB"]))) for r in SQ
         if r["lumpA"]}
_pairs = (("CURVED", _setC, "REFUSED", _setR),
          ("CURVED", _setC, "NON-LUMPABLE", _setL),
          ("REFUSED", _setR, "NON-LUMPABLE", _setL))
_nested = []
_crossing = []
for X, SX, Y, SY in _pairs:
    if SX <= SY or SY <= SX:
        _nested.append((X, Y))
    else:
        _crossing.append((X, Y, len(SX - SY), len(SY - SX)))

print()
print("  THE THREE LOCI, AS SETS OF SQUARES OF THE POOLED POPULATION.")
print(f"    closed squares censused          {len(SQ)}")
print(f"    CURVED        (J != 1)           {len(_setC)}")
print(f"    REFUSED       (no priced image)  {len(_setR)}   "
      f"[= ARBITRATION-CARRYING, gate B.1]")
print(f"    NON-LUMPABLE  (DC2 failing)      {len(_setL)}")
print(f"    all three                        "
      f"{len(_setC & _setR & _setL)}")
print(f"    none of the three                "
      f"{len(SQ) - len(_setC | _setR | _setL)}")
print()
print("  THE PAIRWISE STRUCTURE.")
for X, SX, Y, SY in _pairs:
    if SX == SY:
        vd = "EQUAL"
    elif SX <= SY:
        vd = f"{X} STRICTLY INSIDE {Y}  (boundary {len(SY - SX)})"
    elif SY <= SX:
        vd = f"{Y} STRICTLY INSIDE {X}  (boundary {len(SX - SY)})"
    else:
        vd = (f"CROSSING  ({X}\\{Y} = {len(SX - SY)}, {Y}\\{X} = "
              f"{len(SY - SX)})")
    print(f"    {X} vs {Y}: {vd}")

_setLC = {(r["pop"], sk((r["h"], r["eA"], r["eB"]))) for r in SQ
          if r["lumpC"]}
print()
print("  THE SAME PAIRWISE STRUCTURE UNDER THE DEEP-WINDOW CONTROL "
      "(LUMP-C).")
print(f"    NON-LUMPABLE (deep window)       {len(_setLC)}")
for X, SX, Y in (("CURVED", _setC, "NON-LUMPABLE"),
                 ("REFUSED", _setR, "NON-LUMPABLE")):
    SY = _setLC
    if SX == SY:
        vd = "EQUAL"
    elif SX <= SY:
        vd = f"{X} STRICTLY INSIDE {Y}  (boundary {len(SY - SX)})"
    elif SY <= SX:
        vd = f"{Y} STRICTLY INSIDE {X}  (boundary {len(SX - SY)})"
    else:
        vd = (f"CROSSING  ({X}\\{Y} = {len(SX - SY)}, {Y}\\{X} = "
              f"{len(SY - SX)})")
    print(f"    {X} vs {Y} [LUMP-C]: {vd}")

VERDICT = ("W-ONE-ADDRESS" if (_setC == _setR == _setL)
           else ("W-CROSS" if _crossing else "W-CHAIN"))
VERDICT_CTL = ("W-ONE-ADDRESS" if (_setC == _setR == _setLC)
               else ("W-CROSS"
                     if any(not (SX <= SY or SY <= SX)
                            for SX, SY in ((_setC, _setR),
                                           (_setC, _setLC),
                                           (_setR, _setLC)))
                     else "W-CHAIN"))

print()
print("  AGAINST THE THREE PRE-REGISTERED OUTCOMES.")
print(f"    W-ONE-ADDRESS  requires: all three statuses coincide, or an "
      f"exact chain with")
print(f"                   empty boundaries.  Coincide = "
      f"{_setC == _setR == _setL}; empty boundaries = "
      f"{len(_setR - _setC) == 0 and len(_setL - _setC) == 0}.  "
      f"{'MET' if VERDICT == 'W-ONE-ADDRESS' else 'NOT MET'}.")
print(f"    W-CHAIN        requires: exact strict containments, every "
      f"pair nested, with")
print(f"                   non-empty boundaries.  Pairs nested = "
      f"{len(_nested)} of 3.  "
      f"{'MET' if VERDICT == 'W-CHAIN' else 'NOT MET'}.")
print(f"    W-CROSS        requires: at least one pair of statuses "
      f"crosses.  Crossing pairs")
print(f"                   = {len(_crossing)} of 3: "
      f"{[(a, b) for a, b, x, y in _crossing]}.  "
      f"{'MET' if VERDICT == 'W-CROSS' else 'NOT MET'}.")
print()
print(f"  VERDICT: {VERDICT}")
print(f"  VERDICT under the deep-window control (LUMP-C): {VERDICT_CTL}"
      + ("  — UNCHANGED" if VERDICT_CTL == VERDICT else "  — CHANGED"))
print()
print("  WHAT IT SAYS, WITH ITS SCOPE — every clause a printed number.")
print(f"    CURVED \\ REFUSED       = {len(_setC - _setR):>6}   "
      f"REFUSED \\ CURVED       = {len(_setR - _setC):>6}")
print(f"    CURVED \\ NON-LUMPABLE  = {len(_setC - _setL):>6}   "
      f"NON-LUMPABLE \\ CURVED  = {len(_setL - _setC):>6}")
print(f"    REFUSED \\ NON-LUMPABLE = {len(_setR - _setL):>6}   "
      f"NON-LUMPABLE \\ REFUSED = {len(_setL - _setR):>6}")
print(f"    the arbitration is an exact predictor of REFUSED "
      f"(gate B.1, {len(SQ)}/{len(SQ)}) and of no other status "
      f"(gate C.1).")
print(f"    single-quantity welds found: "
      f"{WELD if WELD else 'NONE of the ' + str(len(CANDIDATES)) + ' candidates tested'}.")
print("""
  WHAT IT DOES NOT SAY.  It does not say non-lumpability is unrelated to
  the record law; it says exactly which squares the three instruments
  disagree on, at these populations and these caps.  It does not say a
  weld quantity cannot exist; it says none of the pin's named candidates
  is one, and prints each one's failure pattern.  Nothing here is a
  record-grain claim (W-D), nothing here touches the merge sector (D.1),
  and no quantity measured here is offered as 'the quantum layer'.""")

print()
print("-" * 78)
print("DECLARED CAPS")
print("-" * 78)
for nm, actors, dep, filt, desc in POPS:
    print(f"  {nm:<6} {desc}; closed squares "
          f"{ARMS[nm]['st']['closed']}, holonomy-carrying "
          f"{len(ARMS[nm]['defs'])}")
print(f"  pooled closed squares censused: {len(SQ)}")
print(f"  lumpability instrument: each population's OWN window (horizon = "
      f"its cap);")
print(f"    U1's ARM-A window ((A,B) d<=5, unfiltered, horizon 5) carried "
      f"as the")
print(f"    port-verification instrument and as AB4's horizon control")
print(f"  lumpability readings carried: LUMP-A (base class at the "
      f"population's own")
print(f"    window, primary — the reading gate PORT.2 verifies against "
      f"U1), LUMP-C")
print(f"    (the deep-window control: AB4 through ARM-A, ABC3 through "
      f"ARM-D, the two")
print(f"    sub-grammars through their own deepest declared window), "
      f"LUMP-W (the")
print(f"    square's window), LUMP-B (DC1's sigma-commuting predicate)")
print(f"  reversal instrument: LD's committed functor; the two sub-grammar")
print(f"    populations read in their MIRROR sub-grammar, with the own "
      f"reading")
print(f"    carried as a control (gate REV.1)")
print(f"  weld candidates tested: {len(CANDIDATES)} singles, "
      f"{len(_cn) * (len(_cn) - 1) // 2} pairs, "
      f"{len(_cn) * (len(_cn) - 1) * (len(_cn) - 2) // 6} triples "
      f"(exhaustive to size 3)")
print("  transport scope, cut grain; committed populations only; "
      "weight-system")
print("    level; no measure claim; the merge sector is not reached")
print("  exact Fractions end to end; no float enters any gate or any "
      "printed")
print("    quantity except wall-clock timings")

print()
print("-" * 78)
print(f"GATES: {PASS} pass, {FAIL} fail  "
      f"(of which {len(COROLLARY)} carry no independent information)")
for a, b in COROLLARY:
    print(f"    corollary: {a} <- {b}")
print(f"ANCHOR FAILURES: {ANCHOR_FAIL}")
print(f"VERDICT: {VERDICT}")
print(f"RUNTIME: {time.time() - T0:.0f}s")
print("-" * 78)

sys.exit(1 if ANCHOR_FAIL else 0)
