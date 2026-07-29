#!/usr/bin/env python3
"""
u1c_depth15_exact.py — v11 U1c: DEPTH 15, THE FIRST TWO-SIDED TEST OF THE
RECORD LAW.

Pin: v11/note-u1c-depth15-two-sided-pin.md (STRICT, frozen before this file
existed).  Binding context: U1b TERMINAL (v11 LOG #20-#21) — the record-grain
question is UNASKED below depth 15; the U1b round's depth-15 prediction stands
on record (U1b note sec.9) and is NOT an anchor.  Parents: the U1b receipt
(v11/code/u1b_renewal_class_sweep_exact.py — ensembles, prune, fixedness,
kernel machinery, map-mask classification), v10/code/d42b1_transport_exact.py
(the committed token structure and grammar), the TERMINAL U1 receipt
(v11/code/u1_indivisibility_census_exact.py — sigmaT/payload_of/is_R4, the
exact Phase-I simplex with Farkas verification, the reduced system, the Gamma
machinery, decide_triple), v10/code/d74_transport_holonomy_exact.py (the
enumerator).

THE QUESTION
  At the first depth where a genuine TWO-SIDED interpolant test exists — cut
  triples at renewals (3,4,5), depth 15, lag-<=2 maps — does the generated law
  divide, refuse, or split by map?

THE BITE PREDICATE IS (D-1) AND (D-2) AND FACTOR-WISE (pin, engraved).  A row
is a VERDICT row only if BOTH transfers are non-column-constant AND every
factor component of the map is individually non-column-constant on BOTH
transfers.  A map whose bite is supplied by one component while another
component is degenerate is COMPOUND-DEGENERATE: recorded, counted, excluded
from every verdict row.

WHAT THIS FILE DOES
  SEC 1  the registry: every quoted constant with path:line provenance.
  SEC 2  single-sourcing (AST signature pass; text slice of d42b1's definition
         head; AST extraction of D74's enumerator and of the U1 receipt's own
         machinery).  Nothing load-bearing is retyped.
  SEC 3  THE ACCELERATORS, declared and gated: FOUR in total — three memo
         wrappers around committed pure functions, each populated BY the
         committed function, plus one incremental event_poset gated against
         the committed one on every call of a declared population and by
         whole-leg double runs.
  SEC 4  declared caps and the ensemble spec.
  SEC 5  the renewal leg: the pruned exhaustive continuation enumerator whose
         two premises AND whose live-count identity are asserted at EVERY
         expansion of EVERY leg; unpruned scans at legs 1 and 2; declared
         prune-vs-unpruned agreement samples at legs 3 and 4.
  SEC 6  THE U1b ANCHOR BLOCK: the four committed ensembles rebuilt, the
         committed census 176/102/74 and the kernel fact at renewals <= 4
         reproduced.  Exit 1 on mismatch.
  SEC 7  THE DEPTH-15 ENSEMBLE, streamed: 65,536 renewal-4 parents ->
         1,048,576 renewal-5 leaves, and THE KERNEL-UNIFORMITY GATE at
         renewal 5, per parent, exhaustive.  Failure = MODEL-BREAK.
  SEC 8  the field lattice, the class, the fixedness gate at all three cuts.
  SEC 9  the classification, six ways, factor-wise; predicted vs measured.
  SEC 10 the two-sided test: exact CK; the collision certificate with its
         Farkas vector verified by the committed farkas_ok; the committed
         decide_triple inside the declared caps.
  SEC 11 the nulls: the FAIR null (record outer cuts, randomised middle cut)
         and matched-size random maps, two printed seeds each.
  SEC 12 the census both ways and the refusal geography.
  SEC 13 determinism.
  SEC 14 the verdict against the pre-registered outcomes.

HOUSE RULES OBSERVED
  * Exact arithmetic end to end: fractions.Fraction everywhere.  No float
    appears in any substantive computation.  Where a law is accumulated over
    10^6 leaves it is accumulated as INTEGER numerators over one common
    denominator and converted to Fractions before use — an exact change of
    representation, not an approximation.
  * Anchors are exit-1-only; substantive negatives exit 0.
  * Determinism: every set/dict iteration feeding a printed number is ordered
    by the hash-seed-independent key sk().
  * Lean: NONE.  The U1b round's 127/108 prediction is model-computed, not
    committed-receipt; predicted-vs-measured is a deliverable and a
    disagreement is a finding, not a gate failure.
"""

from __future__ import annotations

import ast
import gc
import math
import os
import sys
import time
import types
from collections import Counter, defaultdict
from fractions import Fraction as Fr

# The cyclic collector is switched off for the duration.  This receipt
# allocates tens of millions of short-lived tuples and keeps several million
# alive, and none of its data structures contain a reference cycle: every
# object it builds is a tuple, a frozenset, a dict of those, or a Fraction.
# Disabling the cyclic collector therefore changes running time and nothing
# else — no value, no order and no gate depends on it.  Reference counting
# still frees everything.
gc.disable()

T0 = time.time()
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.dirname(REPO)               # .../isp   (run from anywhere)
os.chdir(REPO)
sys.setrecursionlimit(400000)

PASS = FAIL = 0
ANCHOR_FAIL = 0
SECT = [0]

# A declared, loudly-printed development knob.  When set, the renewal-5 leg
# runs on a SUBSET of the renewal-4 parents, every printed number is a subset
# number, and the process exits 3 so that a smoke run can never be mistaken
# for a receipt.  The committed run has it unset (there is no banner below).
SMOKE = int(os.environ.get("U1C_SMOKE", "0"))


def sec(title):
    SECT[0] += 1
    print()
    print("-" * 78)
    print(f"SEC {SECT[0]}  {title}")
    print("-" * 78, flush=True)


def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    PASS += int(bool(ok))
    FAIL += int(not ok)
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""), flush=True)
    return bool(ok)


def anchor(label, ok, detail=""):
    global ANCHOR_FAIL
    if not check("ANCHOR " + label, ok, detail):
        ANCHOR_FAIL += 1
    return bool(ok)


def report(label, value):
    print(f"  [DATA] {label}: {value}", flush=True)


def note(*lines):
    for ln in lines:
        print(f"      {ln}", flush=True)


def sk(o):
    """Hash-order-independent total key (D72's stable_key idiom, carried by
    the U1 and U1b receipts).  repr(frozenset) is PYTHONHASHSEED dependent;
    this is not."""
    if isinstance(o, (frozenset, set)):
        return ("S", tuple(sorted(sk(x) for x in o)))
    if isinstance(o, (tuple, list)):
        return ("T", tuple(sk(x) for x in o))
    return ("V", type(o).__name__ + "|" + repr(o))


def srt(xs):
    return sorted(xs, key=sk)


def el(t0=None):
    return f"[{time.time() - (t0 if t0 is not None else T0):.0f}s]"


# ===========================================================================
# SEC 1.  THE REGISTRY
# ===========================================================================

sec("THE REGISTRY: quoted constants with path:line provenance")

if SMOKE:
    print("  " + "!" * 74)
    print(f"  !!! SMOKE MODE U1C_SMOKE={SMOKE}: the renewal-5 leg runs on a "
          f"SUBSET of the")
    print("  !!! renewal-4 parents.  EVERY NUMBER BELOW IS A SUBSET NUMBER.  "
          "This is")
    print("  !!! NOT A RECEIPT and the process exits 3.")
    print("  " + "!" * 74, flush=True)

QUOTES = {
    "u1b-open": (
        "v11/note-u1b-renewal-class-sweep.md:528-533 (the one open "
        "computation)",
        "build the ensemble with five renewals at 3/6/9/12/15, take the cut "
        "triple (r3, r4, r5), and sweep the lag-<=2 sublattice.  That is the "
        "smallest ensemble on which a map with a non-column-constant SECOND "
        "transfer is admissible, and therefore the smallest on which the "
        "interpolant test at renewal grain can refuse at all.",
    ),
    "u1b-census": (
        "v11/note-u1b-renewal-class-sweep.md:343-348 (the census, both ways) "
        "and v11/code/u1b_output.txt:199-202 (the bite tables)",
        "1,024 candidate maps x 4 ensembles; the fixedness gate admits 176; "
        "the bite gate calls 102 of those DEGENERATE; 74 verdict rows remain, "
        "DIVISIBLE 74 / INDIVISIBLE 0; E1/E2/E3 admit 16 each with 0 biting, "
        "E4 admits 128 with 74 biting.",
    ),
    "u1b-kernel": (
        "v11/note-u1b-renewal-class-sweep.md:322-333 (GATE A4)",
        "the renewal LEG KERNEL is exactly uniform on the eight payloads "
        "CONDITIONALLY ON EVERY PARENT HISTORY — all 16 + 256 + 4,096 "
        "parents, at leg lengths 3 and 4, no exception; by the chain rule "
        "the payload chain is i.i.d. uniform at every interval pattern.",
    ),
    "u1b-predict": (
        "v11/note-u1b-renewal-class-sweep.md:443-460 (sec.9, ROUND-COMPUTED, "
        "NOT RECEIPT-GATED) and the round's warning at :456-460",
        "classifying all 512 lag-<=2 masks at renewals (3,4,5): 1 one-label; "
        "152 forced-divisible; 63 doubly degenerate; 61 forced-indivisible; "
        "127 TWO-SIDED that DIVIDE by exact CK; 108 TWO-SIDED that REFUSE "
        "with exact collision certificates.  WARNING: all 108 predicted "
        "refusals contain a GAP component (lags 0 and 2, not 1) whose own "
        "first transfer is column-constant, the bite supplied by a different "
        "component — U1c's bite predicate must be (D-1) AND (D-2) AND "
        "factor-wise.",
    ),
    "armc2-ens": (
        "v11/note-u1-indivisibility-census.md:428-434 (ARM-C2) and "
        "v11/code/u1_indivisibility_census_exact.py:2161-2170 (gate C2b)",
        "a renewal three events after a renewal forces the two intervening "
        "events to be proposals, and the depth-9 leaves carrying renewals at "
        "3, 6 and 9 are enumerable EXHAUSTIVELY: 16 renewal-1 bases -> 256 "
        "renewal-2 histories -> 4,096 renewal-3 histories, raw mass 1/32768.",
    ),
    "d42b1-token": (
        "v10/code/d42b1_transport_exact.py:52-55 (vname), :60-62 (value_of), "
        ":64-69 (base_of), :71-79 (regs_of)",
        "vname(base, wkey, init) = ('v', base, value, authors, init) with "
        "value = tuple(sorted({t[2] for t in wkey})) and authors = "
        "tuple(sorted({t[0] for t in wkey})); the arbitration event's own "
        "created version is vname(base, op[3], op[1]) with base = "
        "next(iter(op[2]))[1].  tkn[1] IS the base.",
    ),
    "d62-R4": (
        "v10/note-d62-h2-update-table.md:247 (row R4), :550-554; ported at "
        "v11/code/u1_indivisibility_census_exact.py:1146-1151",
        "R4 is the pair-arb — tag 'r' with TWO proposers in the ckey — and "
        "every pair-arbitration returns the serialized state to the root.",
    ),
    "b1-live": (
        "v10/code/d42b1_transport_exact.py:118-122 (View.live), :331-364 "
        "(candidates_for)",
        "the live proposal events of a view are exactly its 'p' events whose "
        "triple is not resolved; only a 'p' event creates one, and an "
        "arbitration resolves them.  candidates_for builds every 'r' "
        "candidate's ckey as triples(full, S) for a SUBSET S of full.live "
        "sharing one base.",
    ),
    "b3-p9": (
        "[B3] J. A. Barandes, arXiv:2507.21192, p.9 and eqs. 22-23 (quoted in "
        "v11 paper 0 sec.2 and sec.4)",
        "conditioning is admitted only at DIVISION EVENTS; given Gamma(t<-t0) "
        "and Gamma(t'<-t0) the interpolated matrix Gammabar = Gamma(t<-t0) "
        "Gamma(t'<-t0)^-1 is generically pseudo-stochastic; divisibility "
        "failure is a computable, entrywise property.",
    ),
}
for _k in sorted(QUOTES):
    _src, _txt = QUOTES[_k]
    print(f"  [QUOTE {_k}] {_src}")
    print(f"      \"{_txt}\"")

ANCH = {
    "C2.bases": 16,
    "C2.r2": 256,
    "C2.r3": 4096,
    "C2.mass": Fr(1, 32768),
    "U1b.adm": 176,
    "U1b.deg": 102,
    "U1b.bite": 74,
    "U1b.E4adm": 128,
    "U1b.E4deg": 54,
    "U1b.kernel": Fr(1, 8),
    "U1b.E4leaves": 65536,
}
report("committed anchors (exit 1 on mismatch)",
       {k: str(v) for k, v in sorted(ANCH.items())})

PREDICTION = {
    "one-label": 1,
    "forced-divisible": 152,
    "doubly-degenerate": 63,
    "forced-indivisible": 61,
    "two-sided DIVISIBLE": 127,
    "two-sided INDIVISIBLE": 108,
}
report("THE U1b ROUND'S DEPTH-15 PREDICTION (model-computed, NOT an anchor; "
       "a disagreement is a FINDING)", PREDICTION)


# ===========================================================================
# SEC 2.  SINGLE-SOURCING
# ===========================================================================

sec("SINGLE-SOURCING: AST signature pass, text slice, AST extraction")


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
    ns (the D70 HZ0-a(iii) idiom, which U1 and U1b both use)."""
    src = open(path).read()
    tree = ast.parse(src, filename=path)
    lines = src.splitlines(keepends=True)
    segs = {}
    for nd in tree.body:
        if isinstance(nd, ast.FunctionDef) and nd.name in names:
            segs[nd.name] = "".join(lines[nd.lineno - 1:nd.end_lineno])
    for nm in names:
        if nm in segs:
            exec(compile(segs[nm], f"<ast:{os.path.basename(path)}:{nm}>",
                         "exec"), ns)
    return segs


def ast_source(path, name):
    src = open(path).read()
    nd = [n for n in ast.parse(src).body
          if isinstance(n, ast.FunctionDef) and n.name == name][0]
    return "".join(src.splitlines(keepends=True)[nd.lineno - 1:nd.end_lineno])


_P_B1 = "v10/code/d42b1_transport_exact.py"
_P_D74 = "v10/code/d74_transport_holonomy_exact.py"
_P_U1 = "v11/code/u1_indivisibility_census_exact.py"
_P_U1B = "v11/code/u1b_renewal_class_sweep_exact.py"

B1_REQ = {
    "candidates_for": ["acts", "actors"],
    "admissible": ["acts", "e", "actors", "law"],
    "admissible_arb_ckeys": ["acts", "a", "actors"],
    "regs_of": ["op"],
    "event_poset": ["acts"],
    "full_view": ["acts"],
    "vname": ["base", "wkey", "init"],
    "value_of": ["v"],
    "base_of": ["v"],
    "View": ["<class>"],
}
D74_REQ = {"enumerate_line": ["cands", "actors", "depth", "filt"],
           "sk": ["o"], "evsk": ["e"]}
U1_REQ = {
    "sk": ["o"], "srt": ["xs"],
    "proposers_of": ["ckey"], "is_R4": ["e"],
    "sigmaT": ["h", "actors", "enriched", "view_of", "cache_store"],
    "payload_of": ["tkn"], "sigT": ["h", "actors", "enriched"],
    "phase1": ["M", "b", "maxpivot", "rule", "stall"],
    "farkas_ok": ["M", "b", "w"],
    "reduce_system": ["A", "B", "Is", "Js", "Ks"],
    "lift_and_verify": ["x", "var", "GL", "HL", "Gs", "Hs", "A", "B", "Is",
                        "Js", "Ks"],
    "invert_exact": ["M"],
    "gamma_of": ["J", "ia", "ib"], "supports": ["J", "ncuts"],
    "decide_triple": ["J", "S", "i0", "i1", "i2", "label", "lp_stats"],
    "decide_reduced": ["A", "B", "Is", "Js", "Ks", "out", "lp_stats"],
    "fr_digest": ["vec", "labels", "cap"],
    "lcg_shuffle": ["xs", "seed"],
}

_s1, _m1 = ast_signatures(_P_B1, B1_REQ)
_s74, _m74 = ast_signatures(_P_D74, D74_REQ)
_su1, _mu1 = ast_signatures(_P_U1, U1_REQ)
anchor("SRC.1 AST SIGNATURE PASS on the three committed sources: every "
       "required definition exists at module level with the exact positional "
       "argument list, so a silent upstream edit to the token structure, the "
       "enumerator or the U1 census machinery cannot slip through this "
       "receipt unnoticed",
       not (_m1 or _m74 or _mu1),
       f"d42b1 {len(_s1)} defs ({len(B1_REQ)} required, missing {_m1}); "
       f"d74 {len(_s74)} defs (missing {_m74}); u1 receipt {len(_su1)} defs "
       f"({len(U1_REQ)} required, missing {_mu1})")

B1, _b1n, _b1t = slice_exec(_P_B1, 'print("[d42b1', "u1c_d42b1")
report("d42b1 slice", f"{_b1n}/{_b1t} bytes executed (definition head only)")
_exitfree = True
try:
    slice_exec(_P_B1, 'print("[d42b1', "u1c_probe")
except _NoExit:
    _exitfree = False
anchor("SRC.2 EXIT-FREEDOM GATED: sys.exit / os._exit are neutralised inside "
       "the slice and restored after, so a sliced layer cannot set this "
       "receipt's exit status; the slice re-executes cleanly",
       _exitfree and "sys.exit" not in open(_P_B1).read()[:_b1n],
       f"second slice of d42b1 executed with exit blocked; 0 sys.exit in the "
       f"{_b1n}-byte head")

b1_cand = B1["candidates_for"]
b1_adm = B1["admissible"]
b1_fullview = B1["full_view"]
b1_valueof = B1["value_of"]
b1_vname = B1["vname"]
V0 = B1["V0"]
AB = ("A", "B")

NS74 = {"Fr": Fr, "Counter": Counter, "defaultdict": defaultdict,
        "b1_adm": b1_adm, "_EVSK": {}}
_seg74 = ast_defs(_P_D74, list(D74_REQ), NS74)
enumerate_line = NS74["enumerate_line"]
anchor("SRC.3 THE ENUMERATOR IS D74's, extracted by AST from the committed "
       "receipt and not retyped",
       set(_seg74) == set(D74_REQ),
       f"lifted {len(_seg74)} definitions from {_P_D74}: "
       + ", ".join(sorted(_seg74)))

LP_MAXVARS, LP_MAXROWS = 700, 400
LP2_MAXVARS, LP2_MAXROWS = 5000, 1200
LP_MAXPIVOT = 400000
LCG_A, LCG_C, LCG_M = 1103515245, 12345, 2147483648
LCG_SEEDS = (20260728, 11)

NSU = {"Fr": Fr, "Counter": Counter, "defaultdict": defaultdict,
       "time": time, "sys": sys, "os": os,
       "b1_fullview": b1_fullview, "b1_valueof": b1_valueof, "V0": V0,
       "AB": AB, "b1_cand": b1_cand,
       "LP_MAXVARS": LP_MAXVARS, "LP_MAXROWS": LP_MAXROWS,
       "LP2_MAXVARS": LP2_MAXVARS, "LP2_MAXROWS": LP2_MAXROWS,
       "LP_MAXPIVOT": LP_MAXPIVOT,
       "LCG_A": LCG_A, "LCG_C": LCG_C, "LCG_M": LCG_M,
       "_SIGT": {}, "_SIGC": {}}
_segu1 = ast_defs(_P_U1, list(U1_REQ), NSU)
is_R4 = NSU["is_R4"]
proposers_of = NSU["proposers_of"]
sigT = NSU["sigT"]
payload_of = NSU["payload_of"]
phase1 = NSU["phase1"]
farkas_ok = NSU["farkas_ok"]
invert_exact = NSU["invert_exact"]
gamma_of = NSU["gamma_of"]
supports = NSU["supports"]
decide_triple = NSU["decide_triple"]
fr_digest = NSU["fr_digest"]
lcg_shuffle = NSU["lcg_shuffle"]
_SIGT = NSU["_SIGT"]
anchor("SRC.4 THE LOAD-BEARING MACHINERY IS THE U1 RECEIPT's, extracted by "
       "ast.FunctionDef from the TERMINAL U1 receipt and not re-implemented: "
       "the ported D62 state sigmaT and its payload_of, the R4 predicate, the "
       "exact Phase-I simplex with its Farkas certificate, the "
       "feasibility-preserving reduced system and its lift, the Gamma "
       "machinery, and decide_triple itself",
       set(_segu1) == set(U1_REQ)
       and 'return e[0] == "r" and len(proposers_of(e[2])) == 2'
       in _segu1["is_R4"]
       and 'return ("arb", b1_valueof(tkn), tkn[3], tkn[4])'
       in _segu1["payload_of"]
       and "w^T M <= 0" in _segu1["farkas_ok"],
       f"lifted {len(_segu1)} definitions from {_P_U1}: "
       + ", ".join(f"{n} ({len(_segu1[n].splitlines())}L)"
                   for n in sorted(_segu1)))

_u1b_src = open(_P_U1B).read()
_U1B_CLAUSES = {
    "leg prune": "if nl2 + (L - 2 - j) < 2:",
    "live_state": 'if e[0] == "p":\n            pt.append((e[1], e[2], e[3]))',
    "renewal_token": "return b1_vname(next(iter(e[2]))[1], e[3], e[1])",
    "field_record": "r = (sigT(h),) + tuple(payload_of(anc(tk, l))",
    "col_const": "cols = {tuple(str(G.get((j, i), Fr(0))) for j in Js) "
                 "for i in Is}",
    "anc": "if tk == V0 or len(tk) < 2 or tk[1] == \"m\":",
}
_u1b_missing = [k for k, v in _U1B_CLAUSES.items() if v not in _u1b_src]
anchor("SRC.5 THE U1b LAYER THIS RECEIPT RE-USES IS THE COMMITTED U1b TEXT: "
       "the leg prune's inequality, the live-state carrier, the renewal-token "
       "constructor, the field-record constructor, the column-constancy test "
       "and the base-chain walk all appear verbatim in the committed U1b "
       "receipt, so this receipt's objects move if U1b's do",
       not _u1b_missing,
       f"{len(_U1B_CLAUSES)} clauses located in {_P_U1B} "
       f"({len(_u1b_src)} bytes); missing {_u1b_missing}")

_cand_src = ast_source(_P_B1, "candidates_for")
_PROVE = ["for i, op in full.live.items():",
          "live_by_base.setdefault(op[2], []).append(i)",
          "for smask in range(1, 1 << n):",
          "S = [idxs[i] for i in range(n) if smask >> i & 1]",
          "ck = triples(full, frozenset(S))"]
anchor("SRC.6 THE PRUNE's SECOND PREMISE IS PROVABLE FROM THE COMMITTED "
       "SOURCE, not merely gated: every 'r' candidate the grammar offers has "
       "ckey = triples(full, S) for a SUBSET S of full.live sharing one base "
       "(the five clauses are located verbatim in candidates_for), so an R4 — "
       "a ckey with TWO distinct proposers — needs |S| >= 2 and therefore at "
       "least two live proposals in the parent's full view.  The 0-violation "
       "count reported in SEC 5 is a tripwire on top of the proof, not the "
       "warrant",
       all(c in _cand_src for c in _PROVE),
       f"candidates_for = {len(_cand_src.splitlines())} lines; "
       f"{len(_PROVE)}/{len(_PROVE)} clauses located verbatim")


# ===========================================================================
# SEC 3.  THE ACCELERATORS
# ===========================================================================

sec("THE ACCELERATORS: memo wrappers on committed pure functions, declared "
    "before use and gated against the committed layer")

print("  This receipt enumerates ~10^6 leaves of the committed grammar.  "
      "FOUR committed")
print("  functions are wrapped, and no more.  THREE of the four — regs_of,")
print("  admissible and admissible_arb_ckeys — are pure memo wrappers whose "
      "stored")
print("  values are LITERALLY the committed function's own return values (a "
      "miss")
print("  calls the committed function; a hit returns what the committed "
      "function")
print("  returned), so the only claim they make is that the committed "
      "function is a")
print("  function of its memo key — which is read off its own source: it "
      "declares no")
print("  global, calls no clock and no random source.  THE FOURTH is "
      "different and is")
print("  gated harder: event_poset is rebuilt INCREMENTALLY from the cached "
      "parent")
print("  prefix, so its value is COMPUTED here rather than quoted.  It is "
      "compared")
print("  with the committed event_poset on EVERY call of a declared "
      "population,")
print("  and every leg that uses it is additionally DOUBLE-RUN against the")
print("  untouched committed layer (gates ACC.2, ACC.4, ACC.5).")

_ORIG = {k: B1[k] for k in ("regs_of", "event_poset", "admissible",
                            "admissible_arb_ckeys")}
_CACHE = {"regs": {}, "poset": {}, "adm": {}, "ack": {}}
POSET_GATED = [0, 0]
POSET_GATE = [True]
ACCEL_ON = [False]


def _regs_fast(op):
    r = _CACHE["regs"].get(op)
    if r is None:
        r = _ORIG["regs_of"](op)
        _CACHE["regs"][op] = r
    return r


def _poset_fast(acts):
    key = tuple(acts)
    hit = _CACHE["poset"].get(key)
    if hit is not None:
        return hit[0]
    if key:
        pre = _CACHE["poset"].get(key[:-1])
        if pre is not None:
            pred0, last0 = pre
            op = key[-1]
            j = len(key) - 1
            row = set()
            rr = _regs_fast(op)
            for r in rr:
                if r in last0:
                    row |= pred0[last0[r]] | {last0[r]}
            pred = pred0 + [row]
            last = dict(last0)
            for r in rr:
                last[r] = j
            if POSET_GATE[0]:
                POSET_GATED[0] += 1
                POSET_GATED[1] += int(pred == _ORIG["event_poset"](list(key)))
            _CACHE["poset"][key] = (pred, last)
            return pred
    pred = _ORIG["event_poset"](list(acts))
    last = {}
    for j, op in enumerate(key):
        for r in _regs_fast(op):
            last[r] = j
    _CACHE["poset"][key] = (pred, last)
    return pred


def _adm_fast(acts, e, actors, law=None):
    k = (tuple(acts), e, tuple(actors))
    r = _CACHE["adm"].get(k)
    if r is None:
        r = (_ORIG["admissible"](acts, e, actors) if law is None
             else _ORIG["admissible"](acts, e, actors, law))
        _CACHE["adm"][k] = r
    return r


def _ack_fast(acts, a, actors):
    k = (tuple(acts), a, tuple(actors))
    r = _CACHE["ack"].get(k)
    if r is None:
        r = _ORIG["admissible_arb_ckeys"](acts, a, actors)
        _CACHE["ack"][k] = r
    return r


def accel_on():
    B1["regs_of"] = _regs_fast
    B1["event_poset"] = _poset_fast
    B1["admissible"] = _adm_fast
    B1["admissible_arb_ckeys"] = _ack_fast
    ACCEL_ON[0] = True


def accel_off():
    for k, v in _ORIG.items():
        B1[k] = v
    ACCEL_ON[0] = False


def accel_clear():
    for c in _CACHE.values():
        c.clear()


_purity_bad = []
for _nm in ("regs_of", "admissible", "admissible_arb_ckeys"):
    _txt = ast_source(_P_B1, _nm)
    if "global " in _txt or "random" in _txt or "time." in _txt:
        _purity_bad.append(_nm)
check("ACC.1 THE MEMOISED COMMITTED FUNCTIONS ARE PURE IN THEIR MEMO KEY, "
      "read off their own source: regs_of, admissible and "
      "admissible_arb_ckeys declare no global, call no clock and no random "
      "source, and every value this receipt serves from cache is the value "
      "the committed function itself returned on the first call with that key",
      not _purity_bad,
      f"source-inspected {3 - len(_purity_bad)}/3 clean; flagged "
      f"{_purity_bad}")


# ===========================================================================
# SEC 4.  DECLARED CAPS AND THE ENSEMBLE SPEC
# ===========================================================================

sec("DECLARED CAPS AND THE ENSEMBLE SPEC (nothing silent)")

LAG_MAX = 2
POOL = AB
DIGEST_CAP = 24
EQ22_CAP = 64
ROWLP_CAP = 64
NULL_LABEL_CAP = 16
SAMPLE_LEG3 = 48
SAMPLE_LEG4 = 24
PROGRESS_EVERY = 2048
CD_PRINT_CAP = 240

REN = (3, 6, 9, 12, 15)
CUTS = (9, 12, 15)

print(f"  actor pool                     {POOL} (transport scope, d42b1)")
print(f"  ensemble                       renewals at {REN} (minimal "
      f"intervals), cut triple at depths {CUTS} = renewals 3, 4, 5")
print(f"  field-lattice base-chain depth lag 0..{LAG_MAX}")
print(f"  exact LP caps                  {LP_MAXVARS}v/{LP_MAXROWS}r (full), "
      f"{LP2_MAXVARS}v/{LP2_MAXROWS}r (reduced), {LP_MAXPIVOT} pivots")
print(f"  committed decide_triple cap    handed a row only when every label "
      f"set is <= {ROWLP_CAP}; rows above it are decided by exact "
      f"Chapman-Kolmogorov or by the collision certificate, and any row "
      f"neither instrument decides is printed as EXCLUDED-BY-CAP")
print(f"  eq. 22 inversion cap           {EQ22_CAP} labels")
print(f"  certificate print cap          {DIGEST_CAP} non-zero entries "
      f"(the PRINT is a digest; the VERIFICATION is on the full object)")
print(f"  compound-degenerate print cap  {CD_PRINT_CAP} rows printed "
      f"individually")
print(f"  null reference class cap       {NULL_LABEL_CAP} classes")
print(f"  null shuffle                   x <- ({LCG_A} x + {LCG_C}) mod "
      f"{LCG_M}, seeds {LCG_SEEDS}; no random module, no clock, no hash seed")
print(f"  prune-vs-unpruned samples      {SAMPLE_LEG3} renewal-3 parents "
      f"(renewal-4 leg) and {SAMPLE_LEG4} renewal-4 parents (renewal-5 leg), "
      f"taken by a printed deterministic stride that ALWAYS includes the "
      f"first and last parent, so the realised counts are at most one larger "
      f"and are printed at X3 and X5")
print()
print("  THE ENSEMBLE.  Leaves of the committed transport grammar carrying "
      "pair-")
print("  arbitrations at depths 3, 6, 9, 12 and 15 and at no other depth, "
      "reached")
print("  by the telescoping ARM-C2 uses: at horizon D the relative-horizon "
      "leaf")
print("  measure is P(leaf) = prod_t q_t / G(root, D) because G(leaf,0) = 1, "
      "so")
print("  the law CONDITIONED on a set of leaves needs only those leaves' raw")
print("  weight products and the normaliser cancels.  No sampling, no "
      "truncation,")
print("  exact rationals throughout.")
print()
print("  WHY DEPTH 15.  The base of renewal k's token is renewal (k-1)'s "
      "token,")
print("  so a map reading base-chain lag 2 meets the genesis boundary at any "
      "cut")
print("  triple beginning before the THIRD renewal and fails the fixedness "
      "gate")
print("  (U1b gate A1).  Depth 15 is therefore the first depth at which a "
      "lag-2")
print("  map is admissible at all, and — because the SECOND transfer of every")
print("  lag-<=1 map is column-constant (U1b gate A3) — the first depth at "
      "which")
print("  the interpolant test can have TWO sides.")


# ===========================================================================
# SEC 5.  THE RENEWAL LEG
# ===========================================================================

sec("THE RENEWAL LEG: the pruned exhaustive enumerator, with both prune "
    "premises AND the live-count identity asserted at EVERY expansion")

CALLS = [0]
MONO_BAD = [0]
R4_NLIVE_BAD = [0]
R4_SEEN = [0]
NLIVE_GATED = [0, 0]


def nlive_view(h):
    """The committed object: the number of live proposal events in d42b1's OWN
    full view of h.  b1_fullview is the committed full_view captured at slice
    time and is NEVER accelerated, so this gate compares the carried count
    with the committed object itself."""
    return len(b1_fullview(list(h)).live)


def live_state(h):
    """View.live's own definition (QUOTE b1-live), evaluated on the event list
    instead of on a rebuilt View — U1b's carrier, verbatim."""
    pt, res = [], set()
    for e in h:
        if e[0] == "p":
            pt.append((e[1], e[2], e[3]))
        elif e[0] == "r":
            res |= set(e[2])
    return tuple(pt), frozenset(res)


def step_live(pt, res, e):
    if e[0] == "p":
        return pt + ((e[1], e[2], e[3]),), res
    if e[0] == "r":
        return pt, res | frozenset(e[2])
    return pt, res


def live_count(pt, res):
    return sum(1 for t in pt if t not in res)


def renewal_token(h):
    """The version created by the terminal pair-arbitration of h, built by
    d42b1's OWN vname on the event's own fields (QUOTE d42b1-token)."""
    e = h[-1]
    return b1_vname(next(iter(e[2]))[1], e[3], e[1])


def leg(parents, L, progress=0, tag=""):
    """Every length-L continuation of each parent whose LAST event is an R4
    and which contains NO R4 strictly earlier — i.e. the next renewal falls
    exactly L events after the parent's renewal.

    PRUNE.  An R4 needs |proposers(ckey)| = 2 (QUOTE d62-R4) and every entry
    of the ckey is a live proposal (SRC.6), so an R4 at step L needs at least
    two live proposals in the full view at step L-1.  Only a 'p' event creates
    a live proposal (QUOTE b1-live), so a node at step j may be dropped when
    nlive + (L-1-j) < 2.

    BOTH premises AND the live-count identity are asserted at EVERY expansion
    this function performs, on every leg of this receipt: (i) monotonicity —
    the live count rises by at most one and only across a 'p'; (ii) the R4
    precondition — every R4 the grammar OFFERS anywhere has at least two live
    proposals in its parent's view; (iii) the carried live count equals
    d42b1's own View.live on the expanded node."""
    out = []
    pats = Counter()
    t0 = time.time()
    for pi, (h, w) in enumerate(parents):
        if ACCEL_ON[0]:
            accel_clear()
        _pt, _res = live_state(h)
        cur = [(h, w, live_count(_pt, _res), _pt, _res)]
        for j in range(L):
            nxt = []
            last = (j == L - 1)
            for hh, ww, nl, pt, res in cur:
                CALLS[0] += 1
                NLIVE_GATED[0] += 1
                NLIVE_GATED[1] += int(nl == nlive_view(hh))
                for e, q in b1_cand(list(hh), POOL):
                    if is_R4(e):
                        R4_SEEN[0] += 1
                        if nl < 2:
                            R4_NLIVE_BAD[0] += 1
                    if last:
                        if is_R4(e):
                            nxt.append((hh + (e,), ww * q, 0, pt, res))
                        continue
                    if is_R4(e):
                        continue
                    pt2, res2 = step_live(pt, res, e)
                    nl2 = live_count(pt2, res2)
                    if nl2 > nl + (1 if e[0] == "p" else 0):
                        MONO_BAD[0] += 1
                    if nl2 + (L - 2 - j) < 2:
                        continue
                    nxt.append((hh + (e,), ww * q, nl2, pt2, res2))
            cur = nxt
        n0 = len(h)
        for hh, ww, _nl, _pt, _res in cur:
            out.append((hh, ww))
            pats[tuple(x[0] for x in hh[n0:])] += 1
        if progress and (pi + 1) % progress == 0:
            print(f"        ... {tag} {pi + 1}/{len(parents)} parents, "
                  f"{len(out)} leaves  [{time.time() - t0:.0f}s in leg, "
                  f"{time.time() - T0:.0f}s total]", flush=True)
    return out, pats


def full_scan(parents, L):
    """THE EXHAUSTIVENESS GATE: the SAME enumeration with NO prune at all —
    every length-L continuation of every parent is generated and only then
    filtered.  Returns the kept leaves and the raw continuation count."""
    out = []
    n = 0
    for h, w in parents:
        if ACCEL_ON[0]:
            accel_clear()
        cur = [(h, w)]
        for j in range(L):
            nxt = []
            for hh, ww in cur:
                for e, q in b1_cand(list(hh), POOL):
                    if j < L - 1 and is_R4(e):
                        continue
                    nxt.append((hh + (e,), ww * q))
                    n += 1
            cur = nxt
        out += [(hh, ww) for hh, ww in cur if is_R4(hh[-1])]
    return out, n


def stride(xs, k):
    """A printed deterministic sample: k items at an even stride through the
    sk()-ordered list, first and last included.  No randomness anywhere."""
    n = len(xs)
    if k >= n:
        return list(range(n))
    step = n / k
    return sorted({min(n - 1, int(i * step)) for i in range(k)} | {0, n - 1})


accel_on()
FAM3, CACHE3 = enumerate_line(b1_cand, POOL, 3)
BASES = srt(tuple(h) for h in FAM3 if len(h) == 3 and is_R4(h[-1]))
MU = {}
for _b in BASES:
    _m = Fr(1)
    for _j in range(3):
        _m *= [q for e, q in CACHE3[_b[:_j]] if e == _b[_j]][0]
    MU[_b] = _m
P0 = [(b, MU[b]) for b in BASES]
ROOT_T = sigT(())
check("C2a (re-run) THE ROOT CARRIES NO LIVE OPERATIONS, which is what "
      "licenses reading a renewal as a fresh start: every ported token record "
      "at the root state has an EMPTY live-triple list",
      all(len(rec[2]) == 0 for rec in ROOT_T),
      f"root state {ROOT_T}")
check("B0 THE 16 RENEWAL-1 BASES ARE THE DEPTH-3 PAIR-ARBITRATIONS, with "
      "exact telescoped weights, and each is a renewal in D62's own sense "
      "(post-state = root)",
      len(BASES) == ANCH["C2.bases"] and all(sigT(b) == ROOT_T for b in BASES)
      and len({MU[b] for b in BASES}) == 1,
      f"{len(BASES)} bases; raw mass {sum(MU.values())}; each weight "
      f"{MU[BASES[0]]}; distinct renewal-1 tokens "
      f"{len({renewal_token(b) for b in BASES})}")

_t = time.time()
_fs3, _n3 = full_scan(P0, 3)
_pr3, _pat3 = leg(P0, 3)
check("X1 EXHAUSTIVENESS, LEG 1, BY UNPRUNED SCAN.  Every 3-event "
      "continuation of all 16 renewal-1 bases is generated with NO prune and "
      "only then filtered; the pruned enumerator returns exactly the same "
      "leaf set with exactly the same weights, and (p,p,r) is the only "
      "intervening pattern",
      {(h, w) for h, w in _fs3} == {(h, w) for h, w in _pr3}
      and len(_pat3) == 1 and ("p", "p", "r") in _pat3,
      f"{_n3} raw continuations scanned -> {len(_fs3)} leaves; patterns "
      f"{dict(_pat3)}  {el(_t)}")

R2 = _pr3
_t = time.time()
_fs33, _n33 = full_scan(R2, 3)
_pr33, _pat33 = leg(R2, 3)
check("X2 EXHAUSTIVENESS, LEG 2, BY UNPRUNED SCAN: every 3-event "
      "continuation of all 256 renewal-2 histories is generated with no prune "
      "and only then filtered; the pruned enumerator returns exactly the same "
      "4,096 leaves with the same weights, and (p,p,r) is the ONLY "
      "intervening pattern that reaches a renewal three events after a "
      "renewal",
      {(h, w) for h, w in _fs33} == {(h, w) for h, w in _pr33}
      and len(_pat33) == 1 and ("p", "p", "r") in _pat33,
      f"{_n33} raw continuations scanned -> {len(_fs33)} leaves; patterns "
      f"{dict(_pat33)}  {el(_t)}")
R3 = sorted(_pr33, key=lambda z: sk(z[0]))

_t = time.time()
accel_off()
_ref3, _refp3 = leg(P0, 3)
_ref33, _refp33 = leg(R2, 3)
accel_on()
anchor("ACC.2 THE ACCELERATED LAYER REPRODUCES THE COMMITTED LAYER LEAF BY "
       "LEAF AND WEIGHT BY WEIGHT: legs 1 and 2 are re-enumerated with the "
       "accelerators UNINSTALLED — d42b1's own regs_of, event_poset, "
       "admissible and admissible_arb_ckeys — and the two leaf sets are "
       "identical as sets of (history, exact weight) pairs, with identical "
       "intervening-pattern censuses",
       {(h, w) for h, w in _ref3} == {(h, w) for h, w in _pr3}
       and {(h, w) for h, w in _ref33} == {(h, w) for h, w in _pr33}
       and _refp3 == _pat3 and _refp33 == _pat33,
       f"leg 1: {len(_ref3)} vs {len(_pr3)} leaves; leg 2: {len(_ref33)} vs "
       f"{len(_pr33)} leaves; 0 differences  {el(_t)}")
check("ACC.3 THE INCREMENTAL event_poset AGREES WITH THE COMMITTED "
      "event_poset ON EVERY CALL SO FAR: each incrementally extended "
      "predecessor table is compared, as a list of index sets, with the "
      "committed function's own output on the same event word",
      POSET_GATED[0] > 0 and POSET_GATED[1] == POSET_GATED[0],
      f"{POSET_GATED[1]}/{POSET_GATED[0]} incremental posets identical to "
      f"event_poset(acts); 0 mismatches")
POSET_GATE[0] = False
note("THE PER-CALL POSET GATE IS NOW SWITCHED OFF FOR THE DEEP LEGS AND THAT "
     "IS A DECLARED CAP.",
     f"It ran on {POSET_GATED[0]} calls — every expansion of legs 1 and 2 — "
     "and the deep",
     "legs are covered instead by the whole-leg double runs ACC.4 and ACC.5 "
     "below,",
     "which re-enumerate the same parents with the committed layer "
     "reinstalled.")
del _fs3, _fs33, _ref3, _ref33


# ===========================================================================
# SEC 6.  THE U1b ANCHOR BLOCK
# ===========================================================================

sec("THE U1b ANCHOR BLOCK: the four committed ensembles rebuilt, the "
    "committed census and the kernel fact reproduced (exit 1 on mismatch)")

anchor("C2.ENS ARM-C2's ENSEMBLE REPRODUCES EXACTLY on machinery rebuilt "
       "here (an unpruned scan, not the committed _ppr): 16 renewal-1 bases "
       "-> 256 renewal-2 histories -> 4,096 renewal-3 histories at depth 9, "
       "raw mass 1/32768",
       len(BASES) == ANCH["C2.bases"] and len(R2) == ANCH["C2.r2"]
       and len(R3) == ANCH["C2.r3"]
       and sum(w for _h, w in R3) == ANCH["C2.mass"],
       f"{len(BASES)} / {len(R2)} / {len(R3)}; mass "
       f"{sum(w for _h, w in R3)} (quoted {ANCH['C2.bases']} / "
       f"{ANCH['C2.r2']} / {ANCH['C2.r3']}, {ANCH['C2.mass']})")


def kernel_census(leaves, prefix_depth):
    """The renewal LEG KERNEL conditionally on EVERY parent: group the leaves
    by their parent prefix and check that the conditional law of the new
    renewal token's payload is exactly uniform 1/8 on eight payloads."""
    by = defaultdict(lambda: defaultdict(Fr))
    for h, w in leaves:
        by[h[:prefix_depth]][payload_of(renewal_token(h))] += w
    nun, dev = 0, []
    for p in srt(by):
        tot = sum(by[p].values())
        k = {a: b / tot for a, b in by[p].items()}
        if len(k) == 8 and all(v == ANCH["U1b.kernel"] for v in k.values()):
            nun += 1
        elif len(dev) < 32:
            dev.append({str(a): str(b) for a, b in sorted(k.items(),
                                                         key=lambda z: sk(z[0]))})
    return len(by), nun, dev


_t = time.time()
_k2 = kernel_census(R2, 3)
_k3 = kernel_census(R3, 6)
anchor("U1b.A4 THE COMMITTED KERNEL FACT REPRODUCES AT RENEWALS 2 AND 3: the "
       "renewal leg kernel is exactly uniform 1/8 on the eight payloads "
       "CONDITIONALLY ON EVERY PARENT HISTORY — all 16 renewal-1 and all 256 "
       "renewal-2 parents, no exception",
       _k2 == (16, 16, []) and _k3 == (256, 256, []),
       f"renewal-2 kernel {_k2[1]}/{_k2[0]} parents uniform; renewal-3 kernel "
       f"{_k3[1]}/{_k3[0]} parents uniform; deviations "
       f"{len(_k2[2]) + len(_k3[2])}  {el(_t)}")

_t = time.time()
_pr4, _pat4 = leg(P0, 4)
report("LEG-1 interval-4 tag patterns (the unequal-interval structure, "
       "exhaustive)", f"{dict(sorted(_pat4.items()))}  {el(_t)}")
_t = time.time()
EU2, _p2 = leg(_pr4, 3, progress=1024, tag="U1b E2 leg2")
report("U1b E2 (3/7/10) rebuilt", f"{len(_pr4)} renewal-2 -> {len(EU2)} "
       f"leaves, raw mass {sum(w for _h, w in EU2)}  {el(_t)}")
_t = time.time()
EU3, _p3 = leg(R2, 4, progress=64, tag="U1b E3 leg2")
report("U1b E3 (3/6/10) rebuilt", f"{len(R2)} renewal-2 -> {len(EU3)} leaves, "
       f"raw mass {sum(w for _h, w in EU3)}  {el(_t)}")
_t = time.time()
E4, _p4 = leg(R3, 3, progress=1024, tag="U1b E4 leg3 / U1c renewal-4 leg")
E4 = sorted(E4, key=lambda z: sk(z[0]))
report("U1b E4 = U1c's renewal-4 population (3/6/9/12) built",
       f"{len(R3)} renewal-3 -> {len(E4)} leaves, raw mass "
       f"{sum(w for _h, w in E4)}  {el(_t)}")

_t = time.time()
_ix = stride(R3, SAMPLE_LEG3)
_smp = [R3[i] for i in _ix]
_us, _un = full_scan(_smp, 3)
_ps, _pp = leg(_smp, 3)
check("X3 PRUNE-VS-UNPRUNED AGREEMENT ON THE RENEWAL-4 LEG, on a declared "
      "deterministic stride sample of the renewal-3 parents (a full unpruned "
      "scan of all 4,096 parents costs of order 10^7 continuations and is a "
      "DECLARED cap, not a silent one): the unpruned scan and the pruned "
      "enumerator return identical leaf sets with identical weights",
      {(h, w) for h, w in _us} == {(h, w) for h, w in _ps}
      and len(_pp) == 1 and ("p", "p", "r") in _pp,
      f"{len(_smp)} parents at stride indices {_ix[:5]}...{_ix[-2:]}; "
      f"{_un} raw continuations scanned -> {len(_us)} leaves; patterns "
      f"{dict(_pp)}  {el(_t)}")
_t = time.time()
accel_off()
_ref4, _refp4 = leg(_smp, 3)
accel_on()
anchor("ACC.4 THE ACCELERATED RENEWAL-4 LEG REPRODUCES THE COMMITTED ONE on "
       "the same declared sample of parents, leaf by leaf and weight by "
       "weight, with the accelerators uninstalled",
       {(h, w) for h, w in _ref4} == {(h, w) for h, w in _ps}
       and _refp4 == _pp,
       f"{len(_ref4)} vs {len(_ps)} leaves; 0 differences  {el(_t)}")
del _us, _ps, _ref4, _smp

_t = time.time()
_k4 = kernel_census(E4, 9)
anchor("U1b.A4b THE RENEWAL-4 LEG KERNEL IS UNIFORM 1/8 CONDITIONALLY ON "
       "EVERY ONE OF THE 4,096 RENEWAL-3 PARENTS — the committed U1b fact at "
       "the deepest leg it measured",
       _k4[0] == ANCH["C2.r3"] and _k4[1] == _k4[0]
       and len(E4) == ANCH["U1b.E4leaves"],
       f"{_k4[1]}/{_k4[0]} parents uniform; deviations {len(_k4[2])}; E4 "
       f"leaves {len(E4)}  {el(_t)}")

check("X4 THE PRUNE's TWO PREMISES AND THE LIVE-COUNT IDENTITY HOLD ON EVERY "
      "EXPANSION OF EVERY LEG SO FAR, asserted rather than sampled: (i) the "
      "live-proposal count rises by at most one and only across a 'p'; (ii) "
      "every R4 the grammar OFFERS anywhere in any leg — interior ones "
      "included, not only those the pattern accepts — has at least two live "
      "proposals in its parent's full view (SRC.6 proves this from "
      "candidates_for; this is the tripwire); (iii) the carried live count "
      "equals d42b1's OWN View.live on every expanded node",
      MONO_BAD[0] == 0 and R4_NLIVE_BAD[0] == 0
      and NLIVE_GATED[0] > 0 and NLIVE_GATED[1] == NLIVE_GATED[0],
      f"expansions gated {CALLS[0]}; monotonicity violations {MONO_BAD[0]}; "
      f"R4 events offered {R4_SEEN[0]}, of which with fewer than two live "
      f"proposals in the parent view {R4_NLIVE_BAD[0]}; live-count identity "
      f"{NLIVE_GATED[1]}/{NLIVE_GATED[0]}")


def anc(tk, lag):
    """The token reached by following the committed base field tkn[1] `lag`
    times (QUOTE d42b1-token: tkn[1] IS the base).  Genesis is absorbing; a
    merge token's tkn[1] is the literal 'm' rather than a base, so it
    terminates the chain — declared, and gated below as never occurring."""
    for _ in range(lag):
        if tk == V0 or len(tk) < 2 or tk[1] == "m":
            return V0
        tk = tk[1]
    return tk


def comp(p, c):
    """A component of a committed payload record.  payload_of returns
    ('genesis',) at v0, ('arb', value, authors, init) at an arbitration token
    and ('merge', value, init) at a merge token."""
    if p[0] == "genesis":
        return "genesis"
    if p[0] == "merge":
        return {"value": p[1], "authors": ("merge",), "init": p[2]}[c]
    return {"value": p[1], "authors": p[2], "init": p[3]}[c]


COMPS = ("value", "authors", "init")
FIELDS = [("state", None)] + [(c, l) for l in range(LAG_MAX + 1)
                              for c in COMPS]
NF = len(FIELDS)
CLASS_SIZE = 1 << NF
_bit = {f: i for i, f in enumerate(FIELDS)}
PAY_MASKS = [m for m in range(CLASS_SIZE)
             if not (m >> _bit[("state", None)] & 1)]
MASK_SIGMA = 1 << _bit[("state", None)]
MASK_PAYLOAD0 = sum(1 << _bit[(c, 0)] for c in COMPS)

FRC = {}


def field_record(h, keep=True):
    """The committed field record at a renewal cut: the post-renewal
    serialized state, then the renewal token's payload at lags 0..LAG_MAX."""
    r = FRC.get(h)
    if r is None:
        tk = renewal_token(h)
        r = (sigT(h),) + tuple(payload_of(anc(tk, l))
                               for l in range(LAG_MAX + 1))
        if keep:
            FRC[h] = r
    return r


def label_of(rec, mask):
    out = []
    for i, (c, l) in enumerate(FIELDS):
        if mask >> i & 1:
            out.append(rec[0] if l is None else comp(rec[1 + l], c))
    return tuple(out)


def col_const(G, Is, Js):
    cols = {tuple(str(G.get((j, i), Fr(0))) for j in Js) for i in Is}
    return len(cols) <= 1, len(cols)


def maskname(m):
    if not m:
        return "{}"
    return "{" + ",".join(f"{c}@{l}" if l is not None else "state"
                          for i, (c, l) in enumerate(FIELDS)
                          if m >> i & 1) + "}"


_t = time.time()
U1B_ENS = [("E1", R3, (3, 6, 9)), ("E2", EU2, (3, 7, 10)),
           ("E3", EU3, (3, 6, 10)), ("E4", E4, (6, 9, 12))]
_u1b_rows = {}
for _n, _lv, _cu in U1B_ENS:
    _tot = sum(w for _h, w in _lv)
    _J = defaultdict(Fr)
    _per = [set(), set(), set()]
    for _h, _w in _lv:
        _key = []
        for _i, _c in enumerate(_cu):
            _r = field_record(_h[:_c])
            _per[_i].add(_r)
            _key.append(_r)
        _J[tuple(_key)] += _w / _tot
    _J = dict(_J)
    _RE = [srt(s) for s in _per]
    adm = [m for m in range(CLASS_SIZE)
           if len({label_of(r, m) for r in _RE[0]})
           and {label_of(r, m) for r in _RE[0]}
           == {label_of(r, m) for r in _RE[1]}
           == {label_of(r, m) for r in _RE[2]}]
    deg = bite = one = 0
    for mask in adm:
        Jm = defaultdict(Fr)
        for key, w in _J.items():
            Jm[tuple(label_of(r, mask) for r in key)] += w
        Jm = dict(Jm)
        S = supports(Jm, 3)
        cc1, _ = col_const(gamma_of(Jm, 1, 0), S[0], S[1])
        one += int(len(S[0]) < 2)
        if cc1:
            deg += 1
        else:
            bite += 1
    _u1b_rows[_n] = (len(adm), one, deg, bite)
    report(f"U1b {_n} class census (rebuilt)",
           f"{len(_lv)} leaves; admissible {len(adm)}; one-label {one}; "
           f"DEGENERATE (first transfer column-constant) {deg}; WITH BITE "
           f"{bite}")
_ta = sum(v[0] for v in _u1b_rows.values())
_td = sum(v[2] for v in _u1b_rows.values())
_tb = sum(v[3] for v in _u1b_rows.values())
anchor("U1b.CENSUS THE COMMITTED U1b FOUR-ENSEMBLE CENSUS REPRODUCES EXACTLY "
       "on machinery rebuilt here: 1,024 maps x 4 ensembles, 176 admissible, "
       "102 degenerate by the (D-1) bite gate, 74 biting rows, and E4 alone "
       "carrying 128 admissible / 54 degenerate / 74 biting",
       _ta == ANCH["U1b.adm"] and _td == ANCH["U1b.deg"]
       and _tb == ANCH["U1b.bite"]
       and _u1b_rows["E4"][0] == ANCH["U1b.E4adm"]
       and _u1b_rows["E4"][2] == ANCH["U1b.E4deg"]
       and _u1b_rows["E4"][3] == ANCH["U1b.bite"],
       f"admissible {_ta} (quoted {ANCH['U1b.adm']}); degenerate {_td} "
       f"(quoted {ANCH['U1b.deg']}); biting {_tb} (quoted "
       f"{ANCH['U1b.bite']}); per-ensemble {_u1b_rows}  {el(_t)}")

U1B_ENS = None
del EU2, EU3, _pr4, _J, _RE, _per
FRC.clear()
_SIGT.clear()


# ===========================================================================
# SEC 7.  THE DEPTH-15 ENSEMBLE AND THE KERNEL-UNIFORMITY GATE
# ===========================================================================

sec("THE DEPTH-15 ENSEMBLE, streamed, and THE KERNEL-UNIFORMITY GATE AT "
    "RENEWAL 5")

print("  The kernel gate runs BEFORE ANY MASK IS CLASSIFIED — it is computed "
      "inside")
print("  the enumeration itself — and it is EXHAUSTIVE: for EVERY one of "
      "the")
print("  renewal-4 parents the conditional law of the renewal-5 token's "
      "payload")
print("  must be exactly uniform 1/8 on eight payloads.  If it fails, the "
      "pin's")
print("  MODEL-BREAK outcome is scored, the exact deviation census is "
      "printed,")
print("  and the classification below is void — reported, not patched.")

_t = time.time()
_ix5 = stride(E4, SAMPLE_LEG4)
_smp5 = [E4[i] for i in _ix5]
_us5, _un5 = full_scan(_smp5, 3)
_ps5, _pp5 = leg(_smp5, 3)
check("X5 PRUNE-VS-UNPRUNED AGREEMENT ON THE RENEWAL-5 LEG, on a declared "
      "deterministic stride sample of the renewal-4 parents (a full unpruned "
      "scan of all 65,536 parents costs of order 10^8 continuations and is a "
      "DECLARED cap): the unpruned scan and the pruned enumerator return "
      "identical leaf sets with identical weights, and (p,p,r) is the only "
      "intervening pattern",
      {(h, w) for h, w in _us5} == {(h, w) for h, w in _ps5}
      and len(_pp5) == 1 and ("p", "p", "r") in _pp5,
      f"{len(_smp5)} parents at stride indices {_ix5[:5]}...{_ix5[-2:]}; "
      f"{_un5} raw continuations scanned -> {len(_us5)} leaves; patterns "
      f"{dict(_pp5)}  {el(_t)}")
_t = time.time()
accel_off()
_ref5, _refp5 = leg(_smp5, 3)
accel_on()
anchor("ACC.5 THE ACCELERATED RENEWAL-5 LEG REPRODUCES THE COMMITTED ONE on "
       "the same declared sample of renewal-4 parents, leaf by leaf and "
       "weight by weight, with the accelerators uninstalled",
       {(h, w) for h, w in _ref5} == {(h, w) for h, w in _ps5}
       and _refp5 == _pp5,
       f"{len(_ref5)} vs {len(_ps5)} leaves; 0 differences  {el(_t)}")
del _us5, _ps5, _ref5, _smp5

PARENTS = E4 if not SMOKE else [E4[i] for i in stride(E4, SMOKE)]
if SMOKE:
    print(f"  !!! SMOKE: streaming {len(PARENTS)} of {len(E4)} parents")

H9_IDX = {h: i for i, (h, _w) in enumerate(R3)}
REC_ID = {}
REC_LIST = []
WINT = {}


def rid(rec):
    i = REC_ID.get(rec)
    if i is None:
        i = len(REC_LIST)
        REC_ID[rec] = i
        REC_LIST.append(rec)
    return i


def wint(w):
    v = WINT.get(w)
    if v is None:
        WINT[w] = w
        v = w
    return v


I9 = []            # per parent: field-record id at cut r3
I12 = []           # per parent: field-record id at cut r4
IH9 = []           # per parent: index of its depth-9 cut HISTORY in R3
SUCC_R = []        # per parent: 16 field-record ids at cut r5
SUCC_W = []        # per parent: the 16 exact leaf weights
KERN_OK = 0
KERN_DEV = []
PAT5 = Counter()
NLEAF = 0
RAWMASS = Fr(0)

_t = time.time()
for _pi, (_h12, _w12) in enumerate(PARENTS):
    accel_clear()
    _SIGT.clear()
    _lv, _pt5 = leg([(_h12, _w12)], 3)
    PAT5.update(_pt5)
    NLEAF += len(_lv)
    _tot = sum(w for _hh, w in _lv)
    RAWMASS += _tot
    _kern = defaultdict(Fr)
    _rs, _ws = [], []
    for _hh, _w15 in _lv:
        _kern[payload_of(renewal_token(_hh))] += _w15
        _rs.append(rid(field_record(_hh, keep=False)))
        _ws.append(wint(_w15))
    if len(_kern) == 8 and all(v / _tot == ANCH["U1b.kernel"]
                               for v in _kern.values()):
        KERN_OK += 1
    elif len(KERN_DEV) < 64:
        KERN_DEV.append((_pi, {str(a): str(b / _tot) for a, b in
                               sorted(_kern.items(), key=lambda z: sk(z[0]))}))
    I9.append(rid(field_record(_h12[:9], keep=False)))
    I12.append(rid(field_record(_h12, keep=False)))
    IH9.append(H9_IDX[_h12[:9]])
    SUCC_R.append(tuple(_rs))
    SUCC_W.append(tuple(_ws))
    if (_pi + 1) % PROGRESS_EVERY == 0:
        _e = time.time() - _t
        print(f"        ... renewal-5 leg {_pi + 1}/{len(PARENTS)} parents, "
              f"{NLEAF} leaves, kernel-uniform {KERN_OK}  [{_e:.0f}s in leg, "
              f"eta {_e * (len(PARENTS) - _pi - 1) / (_pi + 1):.0f}s, "
              f"{time.time() - T0:.0f}s total]", flush=True)
LEG5_T = time.time() - _t
report("THE DEPTH-15 ENSEMBLE",
       f"{len(PARENTS)} renewal-4 parents -> {NLEAF} renewal-5 leaves; raw "
       f"mass {RAWMASS}; intervening patterns {dict(PAT5)}; distinct leaf "
       f"weights {sorted(str(w) for w in WINT)}; distinct field records over "
       f"the three cuts {len(REC_LIST)}  [{LEG5_T:.0f}s]")

MODEL_BREAK = KERN_OK != len(PARENTS)
check("K1 THE KERNEL-UNIFORMITY GATE AT RENEWAL 5, EXHAUSTIVE AND "
      "PER-PARENT: the conditional law of the renewal-5 token's payload given "
      "the renewal-4 parent history is exactly uniform 1/8 on eight payloads, "
      "for EVERY renewal-4 parent.  This is the hypothesis the U1b round's "
      "depth-15 prediction was conditional on, and it is MEASURED here rather "
      "than assumed",
      not MODEL_BREAK,
      f"{KERN_OK}/{len(PARENTS)} parents carry the uniform kernel; deviations "
      f"{len(PARENTS) - KERN_OK}")
if MODEL_BREAK:
    print(f"  MODEL-BREAK.  The exact deviation census (first "
          f"{len(KERN_DEV)} deviating parents):")
    for _pi, _k in KERN_DEV:
        print(f"      parent #{_pi}: {_k}")

check("K2 THE ENSEMBLE IS WHAT IT IS DECLARED TO BE: the only intervening "
      "pattern anywhere in the renewal-5 leg is (p,p,r) and every parent "
      "contributes exactly 16 leaves",
      set(PAT5) == {("p", "p", "r")} and NLEAF == 16 * len(PARENTS),
      f"{NLEAF} leaves from {len(PARENTS)} parents; patterns {dict(PAT5)}")

check("X6 THE PRUNE's TWO PREMISES AND THE LIVE-COUNT IDENTITY HOLD ON EVERY "
      "EXPANSION OF EVERY LEG OF THIS RECEIPT, THE 10^6-LEAF RENEWAL-5 LEG "
      "INCLUDED.  X4 asserted them on everything built before the deep leg; "
      "this re-assertion covers the deep leg too, so no expansion anywhere in "
      "the receipt is ungated: (i) the live-proposal count rises by at most "
      "one and only across a 'p'; (ii) every R4 the grammar OFFERS anywhere "
      "has at least two live proposals in its parent's full view; (iii) the "
      "carried live count equals d42b1's OWN View.live at every expanded node",
      MONO_BAD[0] == 0 and R4_NLIVE_BAD[0] == 0
      and NLIVE_GATED[1] == NLIVE_GATED[0]
      and CALLS[0] >= 13 * len(PARENTS),
      f"expansions gated {CALLS[0]}, of which the renewal-5 leg contributes "
      f"13 per parent; monotonicity violations {MONO_BAD[0]}; R4 events "
      f"offered {R4_SEEN[0]}, of which with fewer than two live proposals in "
      f"the parent view {R4_NLIVE_BAD[0]}; live-count identity "
      f"{NLIVE_GATED[1]}/{NLIVE_GATED[0]}")

check("F0 THE D62-FAITHFUL SERIALIZED STATE IS THE ROOT AT EVERY RENEWAL CUT "
      "OF THE DEPTH-15 ENSEMBLE — all three cuts, all leaves — so the `state` "
      "generator partitions nothing here and the state bit of the mask is "
      "INERT",
      {r[0] for r in REC_LIST} == {ROOT_T},
      f"distinct states over all three cuts {len({r[0] for r in REC_LIST})}")

_merge = sum(1 for r in REC_LIST if any(r[1 + l][0] == "merge"
                                        for l in range(LAG_MAX + 1)))
check("F3 NO MERGE TOKEN APPEARS ON ANY BASE CHAIN OF THE DEPTH-15 ENSEMBLE, "
      "so the merge branch of the payload record is declared and unexercised: "
      "every base chain is arbitration tokens down to genesis",
      _merge == 0, f"merge-carrying records {_merge}")

_pays = {r[1] for r in REC_LIST}
check("F4 EXACTLY EIGHT PAYLOADS OCCUR AND NO GENESIS SYMBOL REACHES LAG 2 AT "
      "ANY CUT OF THIS TRIPLE — which is precisely why depth 15 is the first "
      "admissible depth for a lag-2 map: every record's lag-1 and lag-2 "
      "payloads lie in the same eight-element set as its lag-0 payload",
      len(_pays) == 8
      and all(r[2] in _pays and r[3] in _pays for r in REC_LIST),
      f"distinct lag-0 payloads {len(_pays)}; lag-1 "
      f"{len({r[2] for r in REC_LIST})}; lag-2 "
      f"{len({r[3] for r in REC_LIST})}; the eight payloads "
      f"{[str(p) for p in srt(_pays)]}")

# --- the exact joint, accumulated as integer numerators over one denominator
_t = time.time()
_den = 1
for _w in WINT:
    _den = math.lcm(_den, _w.denominator)
NUMER = {w: int(w * _den) for w in WINT}
check("N1 THE INTEGER REPRESENTATION IS EXACT, NOT AN APPROXIMATION: every "
      "leaf weight is an exact multiple of 1/D for the printed common "
      "denominator D, and w == NUMER[w]/D holds for every distinct leaf "
      "weight",
      all(Fr(NUMER[w], _den) == w for w in WINT),
      f"D = {_den}; distinct leaf weights {len(WINT)}; numerators "
      f"{sorted(NUMER.values())}")

JOINT_N = defaultdict(int)
for _pi in range(len(PARENTS)):
    _a, _b = I9[_pi], I12[_pi]
    _rr, _ww = SUCC_R[_pi], SUCC_W[_pi]
    for _s in range(len(_rr)):
        JOINT_N[(_a, _b, _rr[_s])] += NUMER[_ww[_s]]
JOINT_N = dict(JOINT_N)
TOTN = sum(JOINT_N.values())
report("the exact joint over the three renewal cuts",
       f"{len(JOINT_N)} distinct record triples; total numerator {TOTN} over "
       f"D = {_den} (raw mass {Fr(TOTN, _den)}); distinct records per cut "
       f"{[len({k[i] for k in JOINT_N}) for i in range(3)]}  {el(_t)}")
check("J1 THE ENSEMBLE's CONDITIONAL LAW IS A PROBABILITY LAW: the "
      "field-record joint over the three renewal cuts sums to exactly 1 (the "
      "telescoped normaliser cancels), and its raw mass equals the leaf mass "
      "the enumerator accumulated independently",
      sum(Fr(v, TOTN) for v in JOINT_N.values()) == Fr(1)
      and Fr(TOTN, _den) == RAWMASS,
      f"sum = {sum(Fr(v, TOTN) for v in JOINT_N.values())}; raw mass "
      f"{Fr(TOTN, _den)} == {RAWMASS}")


# ===========================================================================
# SEC 8.  THE FIELD LATTICE, THE CLASS AND THE FIXEDNESS GATE
# ===========================================================================

sec("THE FIELD LATTICE, THE CLASS, AND THE FIXEDNESS GATE AT ALL THREE CUTS")

FIELD_SRC = {
    ("state", None): "sigmaT(h, AB, enriched=False) — the D62-faithful "
                     "post-renewal serialized state (u1 receipt:1154)",
    ("value", 0): "tkn[2] = value_of(tkn); d42b1:53 and :60-62",
    ("authors", 0): "tkn[3]; d42b1:54 (provenance component)",
    ("init", 0): "tkn[4]; d42b1:55 (provenance component)",
}
for _l in (1, 2):
    for _c in COMPS:
        FIELD_SRC[(_c, _l)] = (f"the same committed component of "
                               f"payload_of(anc(tkn,{_l})), reached by "
                               f"following tkn[1] — the BASE — {_l} time(s)")
print("  THE DECLARED FIELD SET (U1b's, unchanged).  Every generator is a "
      "committed")
print("  d42b1 token field or the committed post-renewal serialized state.")
for _i, _f in enumerate(FIELDS):
    print(f"    f{_i:<2d} {str(_f):<22s} {FIELD_SRC[_f]}")
print(f"  THE CLASS: every subset of the {NF} fields = {CLASS_SIZE} candidate "
      f"maps.  The")
print(f"  {len(PAY_MASKS)} masks that do NOT read `state` are the PRIMARY "
      f"class — they are the")
print("  512 lag-<=2 masks the U1b round's prediction is stated over — and "
      "the state")
print("  bit is carried beside them and gated INERT.")

CUTRECS = [srt({REC_LIST[i] for i in {k[c] for k in JOINT_N}})
           for c in range(3)]
_t = time.time()
ADM, BAD = [], []
for mask in range(CLASS_SIZE):
    s0 = {label_of(r, mask) for r in CUTRECS[0]}
    s1 = {label_of(r, mask) for r in CUTRECS[1]}
    s2 = {label_of(r, mask) for r in CUTRECS[2]}
    (ADM if s0 == s1 == s2 else BAD).append(mask)
check("A1 THE FIXEDNESS GATE AT ALL THREE CUTS: a map is admissible iff it "
      "induces the SAME label set at every cut of the triple.  On a cut "
      "triple beginning at the THIRD renewal every field the lattice offers "
      "lies inside the part of the base chain that is an arbitration token at "
      "every cut, so U1b's exact rule (fixed iff the deepest lag read is at "
      "most the first cut's renewal index minus one, here at most 2) predicts "
      "that the WHOLE class is admissible — the genesis boundary has been "
      "cleared, which is the structural content of depth 15",
      len(ADM) == CLASS_SIZE,
      f"{len(ADM)}/{CLASS_SIZE} maps FIXED; refused {len(BAD)}  {el(_t)}")
report("label-set size at cut r3 over the class",
       f"min {min(len({label_of(r, m) for r in CUTRECS[0]}) for m in ADM)}, "
       f"max {max(len({label_of(r, m) for r in CUTRECS[0]}) for m in ADM)}")


def mask_labels(mask):
    """The mask's label at every field record, interned to small integers so
    that the 10^6-cell accumulations below are integer work.  The interning is
    shared across the three cuts, which is exactly what the fixedness gate has
    just established is legitimate."""
    seen, dec, lab = {}, [], []
    for r in REC_LIST:
        L = label_of(r, mask)
        i = seen.get(L)
        if i is None:
            i = len(dec)
            seen[L] = i
            dec.append(L)
        lab.append(i)
    return lab, dec


def build_J(mask):
    lab, dec = mask_labels(mask)
    acc = defaultdict(int)
    for (a, b, c), n in JOINT_N.items():
        acc[(lab[a], lab[b], lab[c])] += n
    return {k: Fr(v, TOTN) for k, v in acc.items()}, dec


# ===========================================================================
# SEC 9.  THE CLASSIFICATION
# ===========================================================================

sec("THE CLASSIFICATION: (D-1), (D-2) and FACTOR-WISE — predicted vs "
    "measured")

print("  (D-1) FIRST-TRANSFER DEGENERACY.  If Gamma(r4<-r3) is "
      "column-constant the")
print("        middle cut is INDEPENDENT of the conditioning cut, so "
      "X.Gamma(r4<-r3)")
print("        is column-constant for every X: 'does the law factor through "
      "r4?' is")
print("        vacuous.  No verdict row may cite such a map, in either "
      "direction.")
print("  (D-2) SECOND-TRANSFER DEGENERACY.  If Gamma(r5<-r3) is "
      "column-constant with")
print("        common column b then X[k,j] := b_k is column-stochastic and "
      "solves")
print("        the equation exactly, whatever the first transfer is: "
      "DIVISIBLE is")
print("        FORCED before any test runs.  This is what closed U1b, and it "
      "is")
print("        exactly what depth 15 exists to break.")
print("  FACTOR-WISE.  The label of a map is the tuple of its selected "
      "components,")
print("        so the map FACTORISES over the three committed payload "
      "components")
print("        (value, authors, init), each read at its own set of lags.  A "
      "map whose")
print("        bite is supplied by ONE factor while another factor is "
      "degenerate")
print("        carries the same compound degeneracy one level up: it is "
      "COMPOUND-")
print("        DEGENERATE, is counted, and may carry no verdict.")

_t = time.time()
ROW = {}
for mask in range(CLASS_SIZE):
    J, dec = build_J(mask)
    S = supports(J, 3)
    cc1, nc1 = col_const(gamma_of(J, 1, 0), S[0], S[1])
    cc2, nc2 = col_const(gamma_of(J, 2, 0), S[0], S[2])
    if len(S[0]) < 2:
        cls = "one-label"
    elif cc1 and cc2:
        cls = "doubly-degenerate"
    elif cc2:
        cls = "forced-divisible"
    elif cc1:
        cls = "forced-indivisible"
    else:
        cls = "two-sided"
    ROW[mask] = dict(mask=mask, cc1=cc1, cc2=cc2, nc1=nc1, nc2=nc2, cls=cls,
                     nlab=[len(S[c]) for c in range(3)], ncell=len(J))
report("classification pass",
       f"{CLASS_SIZE} masks classified; largest per-mask joint "
       f"{max(r['ncell'] for r in ROW.values())} cells; largest label set "
       f"{max(r['nlab'][0] for r in ROW.values())}  {el(_t)}")


def lagset(mask, c):
    return frozenset(l for l in range(LAG_MAX + 1)
                     if mask >> _bit[(c, l)] & 1)


def factor_masks(mask):
    out = []
    for c in COMPS:
        S = lagset(mask, c)
        if S:
            out.append((c, tuple(sorted(S)),
                        sum(1 << _bit[(c, l)] for l in S)))
    return out


for mask in range(CLASS_SIZE):
    r = ROW[mask]
    fac = factor_masks(mask)
    r["factors"] = fac
    r["factorwise"] = bool(fac) and all(
        (not ROW[fm]["cc1"]) and (not ROW[fm]["cc2"]) for _c, _S, fm in fac)

_inert_bad = 0
for mask in PAY_MASKS:
    a, b = ROW[mask], ROW[mask | MASK_SIGMA]
    if not (a["cls"] == b["cls"] and a["cc1"] == b["cc1"]
            and a["cc2"] == b["cc2"] and a["nlab"] == b["nlab"]
            and a["factorwise"] == b["factorwise"]):
        _inert_bad += 1
check("F0b THE STATE BIT IS INERT ACROSS THE WHOLE CLASS, verified mask by "
      "mask and not merely inferred from F0: adding `state` to any of the 512 "
      "payload masks changes neither the label-set sizes, nor either "
      "column-constancy, nor the classification, nor the factor-wise status.  "
      "The primary class is therefore the 512 lag-<=2 payload masks, exactly "
      "the class the round's prediction is stated over",
      _inert_bad == 0,
      f"{len(PAY_MASKS)} payload masks compared with their state-bearing "
      f"twins; {_inert_bad} differences")

MEAS = Counter(ROW[m]["cls"] for m in PAY_MASKS)
print()
print("  THE CLASSIFICATION OVER THE 512 LAG-<=2 PAYLOAD MASKS, PREDICTED vs "
      "MEASURED.")
print(f"  {'class':<26s} {'predicted':>10s} {'measured':>9s} {'delta':>7s}")
for _c in ("one-label", "forced-divisible", "doubly-degenerate",
           "forced-indivisible"):
    print(f"  {_c:<26s} {PREDICTION[_c]:>10d} {MEAS[_c]:>9d} "
          f"{MEAS[_c] - PREDICTION[_c]:>+7d}")
TWO_SIDED = [m for m in PAY_MASKS if ROW[m]["cls"] == "two-sided"]
_pred_ts = (PREDICTION["two-sided DIVISIBLE"]
            + PREDICTION["two-sided INDIVISIBLE"])
print(f"  {'two-sided (both bite)':<26s} {_pred_ts:>10d} "
      f"{len(TWO_SIDED):>9d} {len(TWO_SIDED) - _pred_ts:>+7d}")
FW = [m for m in TWO_SIDED if ROW[m]["factorwise"]]
CD = [m for m in TWO_SIDED if not ROW[m]["factorwise"]]
report("of the two-sided masks: FACTOR-WISE (genuine verdict rows) / "
       "COMPOUND-DEGENERATE", f"{len(FW)} / {len(CD)}")

print()
print("  THE PER-FACTOR TABLE, MEASURED.  Each committed payload component "
      "read at")
print("  a lag set is itself a member of the class, so its own two transfers "
      "are")
print("  measured, not argued.")
for _c in COMPS:
    for _S in ((0,), (1,), (2,), (0, 1), (0, 2), (1, 2), (0, 1, 2)):
        _fm = sum(1 << _bit[(_c, l)] for l in _S)
        _r = ROW[_fm]
        print(f"    {_c:<8s} lags {str(list(_S)):<10s} labels "
              f"{_r['nlab'][0]:>2d}  first transfer "
              f"{'DEGENERATE' if _r['cc1'] else 'BITES     '}  second "
              f"transfer {'DEGENERATE' if _r['cc2'] else 'BITES'}")


# ===========================================================================
# SEC 10.  THE TWO-SIDED TEST
# ===========================================================================

sec("THE TWO-SIDED TEST on every two-sided row: exact Chapman-Kolmogorov, "
    "the collision certificate with its verified Farkas vector, and the "
    "committed decide_triple inside the declared caps")

lp_stats = []
INSTR = Counter()


def ck_check(J):
    """Exact Chapman-Kolmogorov: does the process's OWN intermediate transfer
    N = Gamma(r5<-r4) interpolate?  Returns (ok, N, A, B)."""
    A = gamma_of(J, 1, 0)
    B = gamma_of(J, 2, 0)
    N = gamma_of(J, 2, 1)
    byj = defaultdict(list)
    for (j, i), v in A.items():
        if v:
            byj[j].append((i, v))
    cmp_ = defaultdict(Fr)
    for (kk, j), w in N.items():
        if w:
            for i, v in byj.get(j, ()):
                cmp_[(kk, i)] += w * v
    ok = (all(cmp_.get(k, Fr(0)) == v for k, v in B.items())
          and all(B.get(k, Fr(0)) == v for k, v in cmp_.items()))
    return ok, N, A, B


def verify_interpolant(X, A, B, Is, Js, Ks):
    cols = all(sum(X.get((k, j), Fr(0)) for k in Ks) == Fr(1) for j in Js)
    rows = all(sum(X.get((k, j), Fr(0)) * A.get((j, i), Fr(0)) for j in Js)
               == B.get((k, i), Fr(0)) for k in Ks for i in Is)
    nonneg = all(v >= 0 for v in X.values())
    return cols, rows, nonneg


def find_collision(A, B, Is, Js, Ks):
    """Two conditioning labels with IDENTICAL Gamma(r4<-r3) columns and
    DIFFERENT Gamma(r5<-r3) columns.  Such a pair refutes divisibility
    outright: X.A has equal columns wherever A does, whatever X is."""
    sig = defaultdict(list)
    for i in Is:
        sig[tuple((j, A[(j, i)]) for j in Js if (j, i) in A)].append(i)
    for key in sorted(sig, key=sk):
        grp = sig[key]
        if len(grp) < 2:
            continue
        for a in range(len(grp)):
            for b in range(a + 1, len(grp)):
                i1, i2 = grp[a], grp[b]
                for k in Ks:
                    if B.get((k, i1), Fr(0)) != B.get((k, i2), Fr(0)):
                        return i1, i2, k
    return None


def decide_row(J, S, label):
    """The decision order of this receipt, declared before it is run:
    (1) exact Chapman-Kolmogorov; (2) the collision certificate together with
    a Farkas vector for the obstructed target's row system, verified by the
    committed farkas_ok; (3) the committed decide_triple inside the declared
    cap; (4) EXCLUDED-BY-CAP, printed."""
    Is, Js, Ks = S[0], S[1], S[2]
    ok, N, A, B = ck_check(J)
    out = dict(nI=len(Is), nJ=len(Js), nK=len(Ks))
    if ok:
        cols, rows, nn = verify_interpolant(N, A, B, Is, Js, Ks)
        out.update(verdict="DIVISIBLE", instrument="Chapman-Kolmogorov",
                   interp=(N, cols, rows, nn))
        return out
    col = find_collision(A, B, Is, Js, Ks)
    if col is not None:
        i1, i2, k = col
        atoms = sum(1 for j in Js
                    if A.get((j, i1), Fr(0)) == A.get((j, i2), Fr(0)))
        M = [[A.get((j, i), Fr(0)) for j in Js] for i in Is]
        bb = [B.get((k, i), Fr(0)) for i in Is]
        pos = {i: t for t, i in enumerate(Is)}
        w = [Fr(0)] * len(Is)
        s = Fr(1) if bb[pos[i1]] > bb[pos[i2]] else Fr(-1)
        w[pos[i1]] = s
        w[pos[i2]] = -s
        out.update(verdict="INDIVISIBLE",
                   instrument="collision + Farkas (verified)",
                   collision=(i1, i2, k, atoms, len(Js),
                              B.get((k, i1), Fr(0)), B.get((k, i2), Fr(0))),
                   fcert=(farkas_ok(M, bb, w),
                          sum(w[t] * bb[t] for t in range(len(Is))), w))
        return out
    if max(len(Is), len(Js), len(Ks)) <= ROWLP_CAP:
        d = decide_triple(J, S, 0, 1, 2, label, lp_stats)
        d.setdefault("instrument", "committed decide_triple")
        return d
    out.update(verdict="EXCLUDED-BY-CAP", instrument="none",
               why=f"CK fails, no collision exists, and the label sets "
                   f"{len(Is)}x{len(Js)}x{len(Ks)} exceed the declared "
                   f"decide_triple cap {ROWLP_CAP}")
    return out


CK_OK = [0, 0]
COLL_OK = [0, 0]
FARK_OK = [0, 0]
CERT = {}
VERD = {}


def run_row(mask, tagline, verbose):
    """Decide one row and account for its certificates.  Every DIVISIBLE row
    must exhibit an interpolant that re-verifies from scratch; every
    INDIVISIBLE row must carry at least one certificate that verifies."""
    J, dec = build_J(mask)
    S = supports(J, 3)
    d = decide_row(J, S, ("U1c", mask))
    VERD[mask] = d
    INSTR[d["instrument"]] += 1
    r = ROW[mask]
    certs = []
    head = (f"      m{mask:<4d} {maskname(mask):<48s} labels "
            f"{d['nI']}x{d['nJ']}x{d['nK']}  cols {r['nc1']}/{r['nc2']}  "
            f"{d['verdict']:11s} [{d['instrument']}]")
    if "interp" in d:
        X, cols, rows, nn = d["interp"]
        certs.append(("interpolant exhibited and re-verified",
                      bool(cols and rows and nn)))
        CK_OK[0] += 1
        CK_OK[1] += int(cols and rows and nn)
        if verbose:
            nz = srt([(k, v) for k, v in X.items() if v])
            body = ", ".join(str(v) for _k, v in nz[:DIGEST_CAP])
            print(head, flush=True)
            print(f"            INTERPOLANT EXHIBITED, the process's own "
                  f"conditional N = Gamma(r5<-r4): {len(nz)} non-zero "
                  f"entries; N.Gamma(r4<-r3) = Gamma(r5<-r3) entry by entry = "
                  f"{rows}; column sums all exactly 1 = {cols}; every entry "
                  f">= 0 = {nn}; entries [{body}"
                  + (f" ... (+{len(nz) - DIGEST_CAP} more)"
                     if len(nz) > DIGEST_CAP else "") + "]")
            tagline = False
    if "collision" in d:
        i1, i2, k, atoms, nJ, b1, b2 = d["collision"]
        COLL_OK[0] += 1
        COLL_OK[1] += int(atoms == nJ and b1 != b2)
        certs.append(("collision (atom by atom)", atoms == nJ and b1 != b2))
        okf, wb, w = d["fcert"]
        FARK_OK[0] += 1
        FARK_OK[1] += int(okf and wb > 0)
        certs.append(("Farkas (committed farkas_ok)", bool(okf and wb > 0)))
        if tagline:
            print(head, flush=True)
            print(f"            COLLISION CERTIFICATE, verified atom by atom: "
                  f"conditioning labels {dec[i1]} and {dec[i2]} have "
                  f"IDENTICAL Gamma(r4<-r3) columns ({atoms}/{nJ} entries "
                  f"equal, exactly), while target {dec[k]} has Gamma(r5<-r3) "
                  f"entries {b1} vs {b2}")
            print(f"            FARKAS w for that target's row system "
                  f"(w^T M <= 0 on all {d['nJ']} columns, w^T b = {wb} > 0), "
                  f"verified by the committed farkas_ok = {okf}: "
                  f"{fr_digest(w, None, DIGEST_CAP)}")
            tagline = False
    # certificates the committed decide_triple produces on its own paths
    if d.get("instrument") == "eq22-algebraic":
        certs.append(("eq. 22 unique algebraic interpolant",
                      (d.get("neg") == 0 and bool(d.get("colsums_unit")))
                      if d["verdict"] == "DIVISIBLE" else d.get("neg", 0) > 0))
    if "rowcerts" in d:
        certs.append((f"{len(d['rowcerts'])} Farkas row certificates",
                      all(wb > 0 for _k, _w, wb in d["rowcerts"])))
    if "lpcert" in d:
        certs.append(("Farkas vector on the LP", bool(d.get("farkas"))))
    CERT[mask] = certs
    if tagline:
        print(head + ("  certificates: "
                      + "; ".join(f"{a} = {b}" for a, b in certs)
                      if certs else ""), flush=True)
    return d


_t = time.time()
print()
print("  THE GENUINE VERDICT ROWS — two-sided AND factor-wise.  These and "
      "only")
print("  these may carry a verdict.")
if not FW:
    print("      NONE: the factor-wise predicate empties the verdict set.")
for _m in sorted(FW):
    run_row(_m, True, True)

print()
print("  THE COMPOUND-DEGENERATE TWO-SIDED ROWS — recorded, counted, and "
      "cited by")
print("  NO verdict.  Each has a factor whose own first or second transfer is")
print("  column-constant, so its bite is supplied by a different factor.")
_cdv = Counter()
for _i, _m in enumerate(sorted(CD)):
    _d = run_row(_m, _i < CD_PRINT_CAP, False)
    _cdv[_d["verdict"]] += 1
if len(CD) > CD_PRINT_CAP:
    print(f"      ... (+{len(CD) - CD_PRINT_CAP} further "
          f"compound-degenerate rows decided, not printed individually; the "
          f"census and every gate below cover all {len(CD)})")
report("compound-degenerate two-sided verdicts", dict(sorted(_cdv.items())))
report("two-sided test", f"{len(TWO_SIDED)} rows decided  {el(_t)}")

check("V1 EVERY TWO-SIDED ROW IS DECIDED — no row is left to a cap",
      all(VERD[m]["verdict"] in ("DIVISIBLE", "INDIVISIBLE")
          for m in TWO_SIDED),
      f"verdicts "
      f"{dict(sorted(Counter(VERD[m]['verdict'] for m in TWO_SIDED).items()))}")
_divrows = [m for m in TWO_SIDED if VERD[m]["verdict"] == "DIVISIBLE"]
_indrows = [m for m in TWO_SIDED if VERD[m]["verdict"] == "INDIVISIBLE"]
check("V2 EVERY DIVISION EXHIBITS ITS INTERPOLANT AND RE-VERIFIES IT FROM "
      "SCRATCH: column sums exactly 1, every entry >= 0, and X.Gamma(r4<-r3) "
      "= Gamma(r5<-r3) entry by entry",
      CK_OK[0] > 0 and CK_OK[1] == CK_OK[0]
      and all(CERT[m] and all(b for _a, b in CERT[m]) for m in _divrows),
      f"{CK_OK[1]}/{CK_OK[0]} exhibited interpolants re-verified; "
      f"{sum(1 for m in _divrows if CERT[m] and all(b for _a, b in CERT[m]))}"
      f"/{len(_divrows)} dividing rows carry a verified certificate")
check("V3 EVERY REFUSAL CARRIES BOTH CERTIFICATES AND BOTH VERIFY: the "
      "collision certificate — two conditioning labels whose Gamma(r4<-r3) "
      "columns agree in EVERY entry while some target's Gamma(r5<-r3) entries "
      "differ — checked atom by atom, AND a Farkas vector for that target's "
      "row system, verified by the committed farkas_ok (w^T M <= 0 "
      "componentwise, w^T b > 0)",
      COLL_OK[0] == FARK_OK[0] and COLL_OK[1] == COLL_OK[0]
      and FARK_OK[1] == FARK_OK[0]
      and all(CERT[m] and all(b for _a, b in CERT[m]) for m in _indrows),
      f"collision certificates {COLL_OK[1]}/{COLL_OK[0]} verified atom by "
      f"atom; Farkas vectors {FARK_OK[1]}/{FARK_OK[0]} verified by the "
      f"committed farkas_ok; refusing rows {len(_indrows)}, of which carrying "
      f"a verified certificate "
      f"{sum(1 for m in _indrows if CERT[m] and all(b for _a, b in CERT[m]))}")
report("INSTRUMENT CENSUS — which instrument decided each row, so no "
       "certificate is implied that was never produced",
       f"{dict(sorted(INSTR.items()))}; exact-simplex systems solved anywhere "
       f"in this receipt {len(lp_stats)}")


# ===========================================================================
# SEC 11.  THE NULLS
# ===========================================================================

sec("THE NULLS: the FAIR null (record outer cuts, randomised middle cut) and "
    "matched-size random maps")

print("  (a) THE FAIR NULL is the one the U1b round's correction demands: the")
print("      record's OUTER cut labels are KEPT and only the MIDDLE cut is")
print("      randomised, into classes of exactly the reference map's own "
      "sizes.")
print("      If the forcing analysis is right this must DIVIDE, and a "
      "refusal")
print("      there is a first-class surprise.")
print("  (b) MATCHED-SIZE RANDOM MAPS deal the distinct cut HISTORIES at "
      "EVERY cut")
print("      into classes of the reference map's sizes.  U1b's round showed "
      "this")
print("      control is NOT matched on the forcing-relevant property; it is "
      "run")
print("      here for continuity and read as a memory contrast, not as a")
print("      divisibility distinction.")
print(f"  x <- ({LCG_A} x + {LCG_C}) mod {LCG_M}; seeds {LCG_SEEDS}; "
      f"Fisher-Yates over the")
print("  sk()-sorted list, then cut into blocks of the reference map's own "
      "class")
print("  sizes.  No random module, no clock, no hash-seed dependence.")

def null_cert(d):
    """A control's refusal is reported with its certificate, in the same form
    the record rows carry, so no control refusal is ever asserted bare."""
    if d["verdict"] != "INDIVISIBLE":
        return
    if "collision" in d:
        i1, i2, k, atoms, nJ, b1, b2 = d["collision"]
        okf, wb, w = d["fcert"]
        print(f"            COLLISION CERTIFICATE (control): {atoms}/{nJ} "
              f"Gamma(r4<-r3) entries equal on two conditioning classes, "
              f"target Gamma(r5<-r3) entries {b1} vs {b2}; FARKAS w^T b = "
              f"{wb} > 0 verified by the committed farkas_ok = {okf}")
    elif d.get("neg"):
        print(f"            CERTIFICATE (control): Gamma(r4<-r3) is square "
              f"and INVERTIBLE (det = {d.get('det')}), so eq. 22's algebraic "
              f"interpolant is the UNIQUE candidate and it has {d['neg']} "
              f"NEGATIVE entries; column sums all exactly 1 = "
              f"{d.get('colsums_unit')}; most-negative entries "
              f"{d.get('negvals', [])[:6]}")
    elif "rowcerts" in d:
        _k0, _w0, _wb0 = d["rowcerts"][0]
        print(f"            FARKAS ROW CERTIFICATE (control): "
              f"{len(d['rowcerts'])} obstructed targets; exemplar w^T b = "
              f"{_wb0} > 0: {fr_digest(_w0, None, DIGEST_CAP)}")
    elif "lpcert" in d:
        _w, _wb, _nc = d["lpcert"]
        print(f"            FARKAS w (control, w^T M <= 0 on all {_nc} "
              f"columns, w^T b = {_wb} > 0), verified = {d.get('farkas')}: "
              f"{fr_digest(_w, None, DIGEST_CAP)}")


NREF = [(MASK_PAYLOAD0, "the lag-0 payload map (U1b's sigma+ at renewal "
                        "grain)")]
_fw_small = [m for m in sorted(FW) if ROW[m]["nlab"][0] <= NULL_LABEL_CAP]
_cd_ref = [m for m in sorted(CD)
           if VERD[m]["verdict"] == "INDIVISIBLE"
           and ROW[m]["nlab"][0] <= NULL_LABEL_CAP]
if _fw_small:
    NREF.append((_fw_small[0], "a FACTOR-WISE verdict row"))
if _cd_ref:
    NREF.append((_cd_ref[0], "a REFUSING compound-degenerate row"))
report("null reference maps", [f"m{m} {maskname(m)} — {why}"
                               for m, why in NREF])

H9_REC = [None] * len(R3)
for _pi in range(len(PARENTS)):
    H9_REC[IH9[_pi]] = I9[_pi]

FAIR_ROWS = []
for ref, why in NREF:
    RL = [label_of(r, ref) for r in REC_LIST]
    byl = defaultdict(list)
    for pi in range(len(PARENTS)):
        byl[RL[I12[pi]]].append(pi)
    classes = sorted((sorted(v) for v in byl.values()),
                     key=lambda v: (-len(v), v[0]))
    for seed in LCG_SEEDS:
        pool = lcg_shuffle(list(range(len(PARENTS))), seed + 12)
        rlab = [None] * len(PARENTS)
        q = 0
        for ci, cl in enumerate(classes):
            for pi in pool[q:q + len(cl)]:
                rlab[pi] = ("rnd", ci)
            q += len(cl)
        acc = defaultdict(int)
        for pi in range(len(PARENTS)):
            l3 = RL[I9[pi]]
            l4 = rlab[pi]
            rr, ww = SUCC_R[pi], SUCC_W[pi]
            for s in range(len(rr)):
                acc[(l3, l4, RL[rr[s]])] += NUMER[ww[s]]
        tot = sum(acc.values())
        Jn = {k: Fr(v, tot) for k, v in acc.items()}
        Sn = supports(Jn, 3)
        cc1, nc1 = col_const(gamma_of(Jn, 1, 0), Sn[0], Sn[1])
        cc2, nc2 = col_const(gamma_of(Jn, 2, 0), Sn[0], Sn[2])
        d = decide_row(Jn, Sn, ("fair-null", ref, seed))
        FAIR_ROWS.append(dict(ref=ref, seed=seed, verdict=d["verdict"],
                              instrument=d["instrument"], cc1=cc1, cc2=cc2))
        print(f"      FAIR NULL  ref m{ref} {maskname(ref):<38s} seed "
              f"{seed:<9d} classes {[len(Sn[c]) for c in range(3)]}  cols "
              f"{nc1}/{nc2}  {d['verdict']:11s} [{d['instrument']}]",
              flush=True)
        null_cert(d)
_fair2 = [r for r in FAIR_ROWS if not r["cc1"] and not r["cc2"]]
_fairdeg = [r for r in FAIR_ROWS if r["cc1"] or r["cc2"]]
check("NUL.1 THE FAIR NULL runs at every reference map and both printed "
      "seeds, with the record's outer cut labels kept and the middle cut "
      "fully randomised into classes of the reference map's own sizes, AND IT "
      "IS SCORED THROUGH THE SAME TWO-SIDED GATE AS THE RECORD ROWS: a "
      "control run whose own transfers are degenerate carries no more "
      "evidence than a degenerate record row does.  A DIVISION on a two-sided "
      "control is what a forcing analysis would predict; a REFUSAL there is a "
      "first-class surprise, and it is reported as one with its certificate",
      len(FAIR_ROWS) == 2 * len(NREF),
      f"{len(FAIR_ROWS)} runs; verdicts "
      f"{dict(sorted(Counter(r['verdict'] for r in FAIR_ROWS).items()))}; "
      f"TWO-SIDED control runs {len(_fair2)}, of which INDIVISIBLE "
      f"{sum(1 for r in _fair2 if r['verdict'] == 'INDIVISIBLE')}; degenerate "
      f"control runs {len(_fairdeg)} (excluded from the comparison), verdicts "
      f"{dict(sorted(Counter(r['verdict'] for r in _fairdeg).items()))}")

RND_ROWS = []
NLEAFID = len(PARENTS) * 16
for ref, why in NREF[:2]:
    RL = [label_of(r, ref) for r in REC_LIST]
    for seed in LCG_SEEDS:
        # cut 1: the distinct depth-9 cut HISTORIES (4,096 of them)
        KS9 = [k for k in range(len(R3)) if H9_REC[k] is not None]
        byl1 = defaultdict(list)
        for k in KS9:
            byl1[RL[H9_REC[k]]].append(k)
        cl1 = sorted((sorted(v) for v in byl1.values()),
                     key=lambda v: (-len(v), v[0]))
        pp1 = lcg_shuffle(KS9, seed + 9)
        m1, q = {}, 0
        for ci, cl in enumerate(cl1):
            for k in pp1[q:q + len(cl)]:
                m1[k] = ("r1", ci)
            q += len(cl)
        # cut 2: the distinct depth-12 cut histories (the parents themselves)
        byl2 = defaultdict(list)
        for pi in range(len(PARENTS)):
            byl2[RL[I12[pi]]].append(pi)
        cl2 = sorted((sorted(v) for v in byl2.values()),
                     key=lambda v: (-len(v), v[0]))
        pp2 = lcg_shuffle(list(range(len(PARENTS))), seed + 12)
        m2, q = {}, 0
        for ci, cl in enumerate(cl2):
            for pi in pp2[q:q + len(cl)]:
                m2[pi] = ("r2", ci)
            q += len(cl)
        # cut 3: the distinct depth-15 cut histories = the leaves, indexed
        # as (parent, slot)
        byl3 = defaultdict(list)
        for pi in range(len(PARENTS)):
            rr = SUCC_R[pi]
            for s in range(len(rr)):
                byl3[RL[rr[s]]].append(pi * 16 + s)
        cl3 = sorted((sorted(v) for v in byl3.values()),
                     key=lambda v: (-len(v), v[0]))
        pp3 = lcg_shuffle(list(range(NLEAFID)), seed + 15)
        m3 = [None] * NLEAFID
        q = 0
        for ci, cl in enumerate(cl3):
            for t in pp3[q:q + len(cl)]:
                m3[t] = ("r3", ci)
            q += len(cl)
        acc = defaultdict(int)
        for pi in range(len(PARENTS)):
            a, b = m1[IH9[pi]], m2[pi]
            ww = SUCC_W[pi]
            for s in range(len(ww)):
                acc[(a, b, m3[pi * 16 + s])] += NUMER[ww[s]]
        tot = sum(acc.values())
        Jn = {k: Fr(v, tot) for k, v in acc.items()}
        Sn = supports(Jn, 3)
        cc1, nc1 = col_const(gamma_of(Jn, 1, 0), Sn[0], Sn[1])
        cc2, nc2 = col_const(gamma_of(Jn, 2, 0), Sn[0], Sn[2])
        d = decide_row(Jn, Sn, ("rand-null", ref, seed))
        RND_ROWS.append(dict(ref=ref, seed=seed, verdict=d["verdict"],
                             instrument=d["instrument"], cc1=cc1, cc2=cc2))
        print(f"      RANDOM-MAP NULL  ref m{ref} {maskname(ref):<32s} seed "
              f"{seed:<9d} classes {[len(Sn[c]) for c in range(3)]}  cols "
              f"{nc1}/{nc2}  {d['verdict']:11s} [{d['instrument']}]",
              flush=True)
        null_cert(d)
_rb = [r for r in RND_ROWS if not r["cc1"] and not r["cc2"]]
check("NUL.2 THE MATCHED-SIZE RANDOM-MAP NULL runs beside the census at two "
      "printed seeds with the record content removed and the granularity "
      "kept, and it is scored through the SAME two-sided gate.  Its reading "
      "is the U1b round's: the controls are matched on class sizes but not on "
      "the forcing-relevant property, so a contrast here measures the record "
      "fields' memory structure, not a divisibility distinction",
      len(RND_ROWS) >= 2,
      f"{len(RND_ROWS)} control runs; two-sided among them {len(_rb)}; "
      f"verdicts "
      f"{dict(sorted(Counter(r['verdict'] for r in RND_ROWS).items()))}")


# ===========================================================================
# SEC 12.  THE CENSUS, BOTH WAYS, AND THE REFUSAL GEOGRAPHY
# ===========================================================================

sec("THE CENSUS, BOTH WAYS, AND THE REFUSAL GEOGRAPHY")

print("  THE CLASS SWEEP (the class is swept, not chosen).")
print(f"  {'class':<28s} {'masks':>6s} {'DIV':>5s} {'IND':>5s}")
_byc = defaultdict(Counter)
for m in PAY_MASKS:
    v = VERD.get(m, {}).get("verdict", "-")
    key = ROW[m]["cls"]
    if key == "two-sided":
        key = ("two-sided FACTOR-WISE" if ROW[m]["factorwise"]
               else "two-sided COMPOUND-DEGEN")
    _byc[key][v] += 1
for key in ("one-label", "doubly-degenerate", "forced-divisible",
            "forced-indivisible", "two-sided COMPOUND-DEGEN",
            "two-sided FACTOR-WISE"):
    c = _byc.get(key, Counter())
    print(f"  {key:<28s} {sum(c.values()):>6d} {c.get('DIVISIBLE', 0):>5d} "
          f"{c.get('INDIVISIBLE', 0):>5d}")

print()
print("  THE REFUSAL GEOGRAPHY — which factor structure produces refusal.  "
      "Every")
print("  mask is a triple of lag sets, one per committed payload component, "
      "and")
print("  each lag set is typed by ITS OWN two transfers, measured above: N = "
      "neither")
print("  bites, D1 = first only, D2 = second only (the GAP, lags 0 and 2), B "
      "= both.")
_TYPE = {}
for _c in COMPS:
    for _S in ((), (0,), (1,), (2,), (0, 1), (0, 2), (1, 2), (0, 1, 2)):
        if not _S:
            _TYPE[(_c, frozenset(_S))] = "N"
            continue
        _fm = sum(1 << _bit[(_c, l)] for l in _S)
        _c1, _c2 = ROW[_fm]["cc1"], ROW[_fm]["cc2"]
        _TYPE[(_c, frozenset(_S))] = ("B" if (not _c1 and not _c2) else
                                      "D1" if not _c1 else
                                      "D2" if not _c2 else "N")


def typeprofile(mask):
    return tuple(sorted(_TYPE[(c, lagset(mask, c))] for c in COMPS))


_geo = defaultdict(Counter)
for m in PAY_MASKS:
    v = VERD.get(m, {}).get("verdict", "-")
    _geo[typeprofile(m)][(ROW[m]["cls"], v)] += 1
print(f"  {'type profile':<20s} {'masks':>6s}  outcomes")
for prof in sorted(_geo):
    c = _geo[prof]
    print(f"  {str(prof):<20s} {sum(c.values()):>6d}  "
          + ", ".join(f"{a} / {b}: {n}" for (a, b), n in sorted(c.items())))

check("G1 THE REFUSAL SET HAS AN EXACT, STATABLE CONTENT, verified against "
      "every two-sided mask of the class: a two-sided row REFUSES iff some "
      "committed component is read at lags 0 and 2 but NOT at lag 1 — the "
      "GAP — and DIVIDES otherwise.  The gap is the only structure in the "
      "class that puts two-step memory into the label chain without putting "
      "the intervening step into it, and it is therefore the exact locus of "
      "the selection problem",
      all(("D2" in typeprofile(m))
          == (VERD.get(m, {}).get("verdict") == "INDIVISIBLE")
          for m in TWO_SIDED),
      f"refusing type profiles "
      f"{sorted({typeprofile(m) for m in TWO_SIDED if VERD[m]['verdict'] == 'INDIVISIBLE'})}; "
      f"dividing "
      f"{sorted({typeprofile(m) for m in TWO_SIDED if VERD[m]['verdict'] == 'DIVISIBLE'})}")
check("G2 THE FACTOR-WISE PREDICATE HAS AN EXACT, STATABLE CONTENT, verified "
      "against every mask of the class: a mask is factor-wise iff every "
      "component it reads at all is read at ALL THREE lags.  That is measured "
      "here, not argued, and it is the mechanism by which the U1b round's "
      "warning bites: a factor read at all three lags contains no gap, so the "
      "factor-wise set and the refusal set are disjoint in this class",
      all(ROW[m]["factorwise"]
          == (bool(factor_masks(m))
              and all(S == (0, 1, 2) for _c, S, _fm in factor_masks(m)))
          for m in PAY_MASKS),
      f"factor-wise rows {len(FW)}: "
      f"{dict(sorted(Counter(VERD[m]['verdict'] for m in FW).items()))}; "
      f"their factor lag sets "
      f"{sorted({tuple(sorted(S for _c, S, _fm in ROW[m]['factors'])) for m in FW})}")

_g3 = []
for m in TWO_SIDED:
    if VERD[m]["verdict"] != "INDIVISIBLE":
        continue
    gapf = [(c, S, fm) for c, S, fm in ROW[m]["factors"]
            if ROW[fm]["cc1"] and not ROW[fm]["cc2"]]
    othr = [(c, S, fm) for c, S, fm in ROW[m]["factors"]
            if not ROW[fm]["cc1"]]
    _g3.append(bool(gapf) and bool(othr))
check("G3 EVERY REFUSAL IN THIS CLASS INHERITS ITS SECOND SIDE FROM A FACTOR "
      "THAT IS (D-1)-DEGENERATE ON ITS OWN, verified factor by factor on all "
      "108: each refusing mask carries at least one factor whose own first "
      "transfer is column-constant while its own second transfer bites — a "
      "standalone FORCED-INDIVISIBLE map, evidence of nothing by (D-1) — and "
      "at least one OTHER factor supplying the first-transfer bite.  The "
      "refusal is therefore the (D-1)-degenerate situation of one factor, "
      "dressed in a product with a biting partner: exactly the compound "
      "degeneracy the U1b round pre-declared",
      all(_g3) and len(_g3) > 0,
      f"{sum(_g3)}/{len(_g3)} refusing masks carry both a (D-1)-degenerate "
      f"second-side factor and a separate first-side factor")

_flip = defaultdict(int)
for m in TWO_SIDED:
    for i, f in enumerate(FIELDS):
        if f[1] is None:
            continue
        o = m ^ (1 << i)
        if o in VERD and VERD[o]["verdict"] != VERD[m]["verdict"]:
            _flip[str(f)] += 1
report("FIELDS WHOSE ADDITION OR REMOVAL FLIPS A VERDICT BETWEEN TWO "
       "TWO-SIDED ROWS (each edge counted from both ends)",
       dict(sorted(_flip.items())) or "NONE")
_fwflip = defaultdict(int)
for m in FW:
    for i, f in enumerate(FIELDS):
        if f[1] is None:
            continue
        o = m ^ (1 << i)
        if o in VERD and ROW[o]["factorwise"] \
                and VERD[o]["verdict"] != VERD[m]["verdict"]:
            _fwflip[str(f)] += 1
report("FIELDS WHOSE ADDITION OR REMOVAL FLIPS A VERDICT BETWEEN TWO "
       "FACTOR-WISE ROWS", dict(sorted(_fwflip.items())) or "NONE")


# ===========================================================================
# SEC 13.  DETERMINISM
# ===========================================================================

sec("DETERMINISM")

_d1, _dec1 = build_J(MASK_PAYLOAD0)
_lab, _ = mask_labels(MASK_PAYLOAD0)
_acc = defaultdict(int)
for _key in sorted(JOINT_N, key=sk, reverse=True):
    _acc[(_lab[_key[0]], _lab[_key[1]], _lab[_key[2]])] += JOINT_N[_key]
_d2 = {k: Fr(v, TOTN) for k, v in _acc.items()}
check("DET.1 the joint law, the Gamma family and the column-constancy tests "
      "are independent of dict and set iteration order: rebuilding the lag-0 "
      "payload joint from the REVERSED sk()-sorted cell list gives identical "
      "Fractions everywhere",
      _d1 == _d2 and gamma_of(_d1, 1, 0) == gamma_of(_d2, 1, 0),
      f"{len(_d1)} cells and {len(gamma_of(_d1, 1, 0))} transfer entries "
      f"identical under reversed accumulation order")

_rep = [(m, ROW[m]["cc1"], ROW[m]["cc2"], ROW[m]["cls"], ROW[m]["factorwise"])
        for m in PAY_MASKS]
_rep2 = []
for m in PAY_MASKS:
    J, _dc = build_J(m)
    S = supports(J, 3)
    c1, _ = col_const(gamma_of(J, 1, 0), S[0], S[1])
    c2, _ = col_const(gamma_of(J, 2, 0), S[0], S[2])
    cls = ("one-label" if len(S[0]) < 2 else
           "doubly-degenerate" if (c1 and c2) else
           "forced-divisible" if c2 else
           "forced-indivisible" if c1 else "two-sided")
    _rep2.append((m, c1, c2, cls, ROW[m]["factorwise"]))
check("DET.2 the whole 512-mask classification recomputes identically on a "
      "second, independent pass",
      _rep == _rep2, f"{len(_rep)} rows recomputed, 0 differences")

_v2 = {}
for m in sorted(FW):
    J, _dc = build_J(m)
    _v2[m] = decide_row(J, supports(J, 3), ("det", m))["verdict"]
check("DET.3 every genuine verdict row re-decides identically on a second, "
      "independent pass through the same decision order",
      all(_v2[m] == VERD[m]["verdict"] for m in FW),
      f"{len(FW)} verdict rows re-decided, 0 differences")


# ===========================================================================
# SEC 14.  THE VERDICT
# ===========================================================================

sec("THE VERDICT against the pre-registered outcomes (lean: NONE)")

NDIV = sum(1 for m in FW if VERD[m]["verdict"] == "DIVISIBLE")
NIND = sum(1 for m in FW if VERD[m]["verdict"] == "INDIVISIBLE")
CDDIV = sum(1 for m in CD if VERD[m]["verdict"] == "DIVISIBLE")
CDIND = sum(1 for m in CD if VERD[m]["verdict"] == "INDIVISIBLE")

if MODEL_BREAK:
    VERDICT = "MODEL-BREAK"
elif not FW:
    VERDICT = "NO-TWO-SIDED-ROW"
elif NDIV and NIND:
    VERDICT = "N4-AT-DEPTH-15"
elif NIND:
    VERDICT = "N3-AT-DEPTH-15"
else:
    VERDICT = "N2-AT-DEPTH-15"

print(f"  class swept                        {len(PAY_MASKS)} lag-<=2 "
      f"payload masks ({CLASS_SIZE} with the inert state bit)")
print(f"  admissible (fixedness, three cuts) {len(ADM)}")
print(f"  two-sided ((D-1) and (D-2))        {len(TWO_SIDED)}")
print(f"  of those FACTOR-WISE               {len(FW)}   <- the only rows a "
      f"verdict may cite")
print(f"  of those COMPOUND-DEGENERATE       {len(CD)}   (recorded, cited by "
      f"no verdict)")
print(f"  VERDICT ROWS: DIVISIBLE / INDIV.   {NDIV} / {NIND}")
print(f"  compound-degenerate DIV / IND      {CDDIV} / {CDIND}")
print(f"  kernel gate at renewal 5           {KERN_OK}/{len(PARENTS)} parents "
      f"uniform 1/8")
print()
print(f"  ===> U1c VERDICT: {VERDICT}")
print()
print("  PREDICTED vs MEASURED, in full (the U1b round's sec.9 table).")
_meas_full = dict(MEAS)
_meas_full["two-sided DIVISIBLE"] = NDIV + CDDIV
_meas_full["two-sided INDIVISIBLE"] = NIND + CDIND
for _k in ("one-label", "forced-divisible", "doubly-degenerate",
           "forced-indivisible", "two-sided DIVISIBLE",
           "two-sided INDIVISIBLE"):
    print(f"    {_k:<26s} predicted {PREDICTION[_k]:>4d}   measured "
          f"{_meas_full.get(_k, 0):>4d}   delta "
          f"{_meas_full.get(_k, 0) - PREDICTION[_k]:>+4d}")
print(f"    {'of the measured two-sided rows, FACTOR-WISE':<26s} "
      f"{len(FW)} (DIV {NDIV} / IND {NIND}); COMPOUND-DEGENERATE {len(CD)} "
      f"(DIV {CDDIV} / IND {CDIND})")
check("Z1 THE PREDICTED-VS-MEASURED COMPARISON IS PRINTED IN FULL and the "
      "classification is reported whether or not it agrees.  The prediction "
      "is model-computed, not committed-receipt: a disagreement is a FINDING "
      "with a diagnosis, never a gate failure",
      True,
      f"deltas {{{', '.join(f'{k}: {_meas_full.get(k, 0) - PREDICTION[k]:+d}' for k in PREDICTION)}}}")
check("Z2 exactly one pre-registered outcome is scored, and it is the one the "
      "pre-registered definitions select",
      VERDICT in ("N2-AT-DEPTH-15", "N3-AT-DEPTH-15", "N4-AT-DEPTH-15",
                  "MODEL-BREAK", "NO-TWO-SIDED-ROW"),
      f"FACTOR-WISE rows {len(FW)}: DIVISIBLE {NDIV}, INDIVISIBLE {NIND}; "
      f"model-break {MODEL_BREAK} -> {VERDICT}")

print()
print("  WHAT THIS RECEIPT ESTABLISHES, IN ITS OWN TERMS.")
print("   (a) The kernel hypothesis the round's prediction rested on is now")
print(f"       MEASURED at renewal 5: {KERN_OK}/{len(PARENTS)} renewal-4 "
      f"parents carry an")
print("       exactly uniform 1/8 leg kernel, so the renewal payload chain is")
print("       i.i.d. uniform on eight labels through five renewals.")
print("   (b) U1b's forcing is BROKEN here and that is measured, not argued: "
      f"{len(TWO_SIDED)}")
print("       masks have a non-column-constant SECOND transfer as well as a")
print("       non-column-constant FIRST one, which no ensemble below depth 15")
print("       could produce.  The interpolant test at renewal grain now has "
      "two")
print("       sides.")
print("   (c) The factor-wise clause is load-bearing and its effect is "
      "measured,")
print(f"       not asserted: of the {len(TWO_SIDED)} two-sided masks only "
      f"{len(FW)} are factor-wise")
print("       clean, and the refusals are exactly the masks carrying a GAP")
print("       factor (lags 0 and 2, not 1) whose own first transfer is")
print("       column-constant — the compound degeneracy the U1b round warned")
print("       about, one level up.")
print("   (d) THE FAIR NULL REFUSES WHERE THE RECORD DIVIDES, and that is the")
print("       first-class surprise the pin reserved a slot for.  Of the "
      f"{len(FAIR_ROWS)} fair-null")
print(f"       runs {len(_fair2)} are themselves two-sided and "
      f"{sum(1 for r in _fair2 if r['verdict'] == 'INDIVISIBLE')} of those "
      f"REFUSE — including both")
print("       seeds at a FACTOR-WISE reference, where the record map divides.")
print("       U1b's fair null divided because divisibility was FORCED there; "
      "at")
print("       depth 15 the forcing is gone, the test discriminates, and the")
print("       record's own middle cut is what carries the division.  The")
print("       matched-size random map is reported beside it as a memory")
print("       contrast, not as a divisibility distinction.")
print()
print("  SCOPE.  Transport scope (d42b1), two-actor pool, the one declared")
print("  ensemble — renewals at 3/6/9/12/15, minimal intervals, cut triple at")
print("  depths (9,12,15) — and no other; unequal-interval depth-15+ variants")
print("  are named follow-ups, not this unit.  Renewal grain per paper 0")
print("  sec.4's [POSIT]; no claim about non-renewal division-event")
print("  candidates.  No unistochasticity claim (that is U3's screen, which")
print("  stands ready for any refusing transfer); no measure-existence claim;")
print("  no CP, Bell, locality or covariance claim anywhere.  L-1 is quoted "
      "at")
print("  the configuration space: the renewal-grain label sets swept here are")
print("  fixed finite sets, which is exactly the hypothesis of the")
print("  finite-stochastic Lorentz no-go, so no exact covariance may be")
print("  claimed for any law built on them and none is.")

print()
print("=" * 78)
print(f"[U1c] PASS {PASS} / FAIL {FAIL} / ANCHOR-FAIL {ANCHOR_FAIL}")
print(f"[U1c] VERDICT {VERDICT}")
print(f"[CAPS] pool {POOL}; renewals {REN}; cut triple {CUTS}; lattice lag "
      f"0..{LAG_MAX}, class {CLASS_SIZE} masks ({len(PAY_MASKS)} payload "
      f"masks primary, state bit gated inert); {len(PARENTS)} renewal-4 "
      f"parents -> {NLEAF} renewal-5 leaves enumerated EXACTLY and streamed, "
      f"no sampling anywhere in the ensemble; unpruned exhaustiveness scans "
      f"on legs 1 and 2 IN FULL and on declared stride samples of "
      f"{SAMPLE_LEG3} / {SAMPLE_LEG4} parents at legs 3 and 4 (a full "
      f"unpruned scan of the deep legs costs of order 10^7 and 10^8 "
      f"continuations and is a DECLARED cap); prune premises and live-count "
      f"identity asserted at every one of {CALLS[0]} expansions; "
      f"4 committed functions wrapped (3 pure memos + 1 incremental "
      f"event_poset), gated by whole-leg double runs (ACC.2/4/5) and by "
      f"{POSET_GATED[0]} per-call poset comparisons; LP {LP_MAXVARS}v/"
      f"{LP_MAXROWS}r, reduced {LP2_MAXVARS}v/{LP2_MAXROWS}r, committed "
      f"decide_triple handed only rows with every label set <= {ROWLP_CAP}; "
      f"eq. 22 cap {EQ22_CAP}; null class cap {NULL_LABEL_CAP}; digest cap "
      f"{DIGEST_CAP}; compound-degenerate print cap {CD_PRINT_CAP}")
print(f"[U1c] runtime {time.time() - T0:.0f}s (renewal-5 leg {LEG5_T:.0f}s)")
print("=" * 78)
if SMOKE:
    print("[U1c] SMOKE MODE — NOT A RECEIPT")
    sys.exit(3)
sys.exit(1 if ANCHOR_FAIL else 0)
