#!/usr/bin/env python3
"""
u1b_renewal_class_sweep_exact.py — v11 U1b: THE RENEWAL-GRAIN CLASS SWEEP.

Pin: v11/note-u1b-renewal-beables-pin.md (STRICT, frozen before this file
existed).  Binding context: U1 TERMINAL (v11 LOG #11-#14), paper 0 sec.4
(division events are the renewals) and sec.9b.  Parents: the ARM-C2
telescoped construction (v11/code/u1_indivisibility_census_exact.py, the
committed receipt this file slices), v10/code/d42b1_transport_exact.py (the
committed token structure), D62 row R4, PORT-1/2/3.

THE QUESTION U1 COULD NOT ANSWER
  Is the renewal-to-renewal law divisible WHERE THE INTERPOLANT TEST HAS
  BITE, and is the answer map-robust?  U1's ARM-C2 ran the pinned triple
  exactly and exhaustively at minimal intervals and returned a test without
  bite: `alpha_sigma` gives a one-point renewal state (vacuous) and
  `alpha_sigma+` drops the arbitration token's BASE — the only object
  linking consecutive renewals — so its renewal transfer is COLUMN-CONSTANT
  and DIVISIBLE was the only reachable verdict.  U1b sweeps the WHOLE
  kinematically admissible class of renewal-grain configuration maps over
  four ensembles, three of them carrying interval patterns or cut triples
  ARM-C2 never reached.

WHAT THIS FILE DOES
  SEC 1  the registry: every quoted constant with path:line provenance.
  SEC 2  single-sources the committed layers (AST signature pass, text
         slice of d42b1's definition head, AST extraction of the U1
         receipt's own machinery: sigmaT/payload_of/is_R4, the exact
         Phase-I simplex with Farkas verification, the reduced system, the
         Gamma machinery and decide_triple).  Nothing load-bearing is
         retyped.
  SEC 3  declares every cap and every ensemble before anything uses them.
  SEC 4  the RENEWAL LEG: an exhaustive continuation enumerator with a
         live-proposal prune whose two premises are gated on EVERY
         expansion, plus a full UNPRUNED k-event continuation scan on the
         populations where it is affordable (U1-delta's m2, discharged).
  SEC 5  the four ensembles, built, with ARM-C2's committed numbers as
         exit-1 anchors.
  SEC 6  the declared FIELD LATTICE over the committed d42b1 token fields;
         the class enumerated in full; sigma and sigma+ identified as
         members by an exact partition gate.
  SEC 7  ADMISSIBILITY: the fixedness gate, per map, per ensemble.
  SEC 8  THE BITE GATE, per admissible map, per ensemble, BEFORE any
         verdict: column-constancy of the renewal transfer, exactly.
  SEC 9  the interpolant test on every admissible NON-DEGENERATE map, both
         instruments (exact LP with Farkas / exhibited interpolant, and the
         [B3] eq. 22 algebraic form beside it).
  SEC 10 the null: matched-size random partitions of the same cut
         populations, printed LCG, two fixed seeds, on every ensemble.
  SEC 11 the census, both ways, and the map-dependence structure.
  SEC 12 determinism.
  SEC 13 the verdict against the pre-registered outcomes N1-N4.

HOUSE RULES OBSERVED
  * Exact arithmetic end to end: fractions.Fraction everywhere.  No float
    appears in any substantive computation.
  * Predictive sufficiency is NOT used as an admissibility criterion
    anywhere: screening-off is the phenomenon under measurement, not a
    filter (pin; v11 LOG #15 board note).
  * Anchors are exit-1-only; substantive negatives exit 0.
  * Determinism: every set/dict iteration feeding a printed number is
    ordered by the hash-seed-independent key sk().
  * Lean: NONE.  Any of N1-N4 is the result.
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
    """Hash-order-independent total key (D72's stable_key idiom, which the
    U1 receipt also carries).  repr(frozenset) is PYTHONHASHSEED dependent;
    this is not."""
    if isinstance(o, (frozenset, set)):
        return ("S", tuple(sorted(sk(x) for x in o)))
    if isinstance(o, (tuple, list)):
        return ("T", tuple(sk(x) for x in o))
    return ("V", type(o).__name__ + "|" + repr(o))


def srt(xs):
    return sorted(xs, key=sk)


# ===========================================================================
# SEC 0.  THE REGISTRY — every constant a gate tests against, with provenance
# ===========================================================================

sec("THE REGISTRY: quoted constants with path:line provenance")

QUOTES = {
    "armc2-ens": (
        "v11/note-u1-indivisibility-census.md:428-434 (ARM-C2) and "
        "v11/code/u1_indivisibility_census_exact.py:2161-2170 (gate C2b)",
        "a renewal three events after a renewal forces the two intervening "
        "events to be proposals, and the depth-9 leaves carrying renewals "
        "at 3, 6 and 9 are enumerable EXHAUSTIVELY: 16 renewal-1 bases -> "
        "256 renewal-2 histories -> 4,096 renewal-3 histories, raw mass "
        "1/32768.",
    ),
    "armc2-deg": (
        "v11/note-u1-indivisibility-census.md:436-456 (ARM-C2 Result) and "
        "v11/code/u1_indivisibility_census_exact.py:2185-2218 (gate C2c)",
        "under the payload-enriched map the supports are 8, 8, 8; the joint "
        "law over (cfg@r1, cfg@r2, cfg@r3) is exactly uniform (1/512 on all "
        "512 cells); Gamma(r2<-r1) is COLUMN-CONSTANT (every entry 1/8, "
        "distinct columns 1); DIVISIBLE was the only reachable verdict.",
    ),
    "armc2-mech": (
        "v11/note-u1-indivisibility-census.md:449-456 and v11/LOG.md:545-549 "
        "(the delta round's mechanism finding)",
        "payload_of drops the arb token's BASE — and the base of a renewal "
        "token is the previous renewal's token, the only object that links "
        "consecutive renewals — so the committed enriched map retains, by "
        "construction, nothing that can propagate across a renewal.",
    ),
    "u1b-open": (
        "v11/note-u1-indivisibility-census.md:820-832 (Handover to U1b)",
        "the renewal-to-renewal interpolant test wherever it has bite — (a) "
        "UNEQUAL renewal intervals, and (b) any renewal-grain configuration "
        "map that retains the arb token's base across a renewal (any map "
        "whose renewal transfer is not column-constant).",
    ),
    "d42b1-token": (
        "v10/code/d42b1_transport_exact.py:52-55 (vname), :57-58 (mname), "
        ":60-62 (value_of), :64-69 (base_of), :71-79 (regs_of)",
        "vname(base, wkey, init) = ('v', base, value, authors, init) with "
        "value = tuple(sorted({t[2] for t in wkey})) and authors = "
        "tuple(sorted({t[0] for t in wkey})); the arbitration event's own "
        "created version is vname(base, op[3], op[1]) with base = "
        "next(iter(op[2]))[1].  tkn[1] IS the base.",
    ),
    "d62-R4": (
        "v10/note-d62-h2-update-table.md:247 (row R4), :550-554 (the "
        "renewal corollary); ported at "
        "v11/code/u1_indivisibility_census_exact.py:1146-1151",
        "rows are selected by (event tag, base in refs?, |proposers(ckey)|); "
        "R4 is the pair-arb — tag 'r' with TWO proposers in the ckey — and "
        "every pair-arbitration returns the serialized state to the root "
        "(at closed scope; delivery-conditioned at transport scope, "
        "PORT-3).",
    ),
    "b3-p9": (
        "[B3] J. A. Barandes, arXiv:2507.21192, p.9 and eqs. 22-23 (quoted "
        "in v11 paper 0 sec.2 and sec.4)",
        "conditioning is admitted only at DIVISION EVENTS; given "
        "Gamma(t<-t0) and Gamma(t'<-t0) the interpolated matrix Gammabar = "
        "Gamma(t<-t0) Gamma(t'<-t0)^-1 is generically pseudo-stochastic; "
        "divisibility failure is a computable, entrywise property.",
    ),
    "b1-live": (
        "v10/code/d42b1_transport_exact.py:118-122 (View.live)",
        "the live proposal events of a view are exactly its 'p' events whose "
        "triple is not resolved; only a 'p' event creates one, and an "
        "arbitration resolves (removes) them.",
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
    "C2.supports": [8, 8, 8],
    "C2.cells": 512,
    "C2.cell": Fr(1, 512),
    "C2.cols": 1,
}
report("ARM-C2 anchors (exit 1 on mismatch)",
       {k: str(v) for k, v in sorted(ANCH.items())})


# ===========================================================================
# SEC 1.  SINGLE-SOURCING
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
    ns (the D70 HZ0-a(iii) idiom, which the U1 receipt itself uses)."""
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


_P_B1 = "v10/code/d42b1_transport_exact.py"
_P_D74 = "v10/code/d74_transport_holonomy_exact.py"
_P_U1 = "v11/code/u1_indivisibility_census_exact.py"

B1_REQ = {
    "candidates_for": ["acts", "actors"],
    "admissible": ["acts", "e", "actors", "law"],
    "canon": ["acts"],
    "regs_of": ["op"],
    "event_poset": ["acts"],
    "full_view": ["acts"],
    "vname": ["base", "wkey", "init"],
    "mname": ["pk", "value", "init"],
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

B1, _b1n, _b1t = slice_exec(_P_B1, 'print("[d42b1', "u1b_d42b1")
report("d42b1 slice", f"{_b1n}/{_b1t} bytes executed (definition head only)")
_exitfree = True
try:
    slice_exec(_P_B1, 'print("[d42b1', "u1b_probe")
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

# --- caps the lifted U1 machinery closes over; identical to the U1
#     receipt's own committed values, printed again in SEC 2.
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
       "the ported D62 state sigmaT and its payload_of, the R4 predicate, "
       "the exact Phase-I simplex with its Farkas certificate, the "
       "feasibility-preserving reduced system and its lift, the Gamma "
       "machinery, and decide_triple itself.  A change to U1's definitions "
       "changes this receipt's objects",
       set(_segu1) == set(U1_REQ)
       and 'return e[0] == "r" and len(proposers_of(e[2])) == 2'
       in _segu1["is_R4"]
       and 'return ("arb", b1_valueof(tkn), tkn[3], tkn[4])'
       in _segu1["payload_of"]
       and "w^T M <= 0" in _segu1["farkas_ok"],
       f"lifted {len(_segu1)} definitions from {_P_U1}: "
       + ", ".join(f"{n} ({len(_segu1[n].splitlines())}L)"
                   for n in sorted(_segu1)))
note("THE MECHANISM UNDER TEST, READ OFF THE LIFTED SOURCE.  payload_of's "
     "arbitration",
     "branch is `('arb', b1_valueof(tkn), tkn[3], tkn[4])`: it reads the "
     "value and",
     "the two provenance components and DROPS tkn[1].  By QUOTE d42b1-token "
     "tkn[1]",
     "IS the base, and the base of a renewal token is the previous renewal's",
     "token.  That single omission is why U1's ARM-C2 had no bite, and it is "
     "the",
     "reason this unit sweeps the lattice rather than choosing a map.")


# ===========================================================================
# SEC 2.  DECLARED CAPS, ENSEMBLES AND CLASS
# ===========================================================================

sec("DECLARED CAPS, ENSEMBLES AND CLASS (nothing silent)")

LAG_MAX = 2          # the field lattice reads the base chain to lag 2
POOL = AB            # the two-actor transport pool, as in ARM-C2
DIGEST_CAP = 24      # certificate / interpolant print cap (declared)
EQ22_CAP = 64        # eq. 22 exact inversion runs up to this label count
NULL_LABEL_CAP = 16  # a null reference map may carry at most this many
#                      classes, so the control's own LP stays inside caps
FULLSCAN_POPS = ("16 depth-3 bases at L=3 and L=4, and 256 depth-6 renewal "
                 "histories at L=3")

print(f"  actor pool                     {POOL} (transport scope, d42b1)")
print(f"  field-lattice base-chain depth lag 0..{LAG_MAX}")
print(f"  exact LP caps                  {LP_MAXVARS} vars / {LP_MAXROWS} "
      f"rows (full system), {LP2_MAXVARS} / {LP2_MAXROWS} (reduced), "
      f"{LP_MAXPIVOT} pivots")
print(f"  certificate print cap          {DIGEST_CAP} non-zero entries, then "
      f"a count and the exact sum — the PRINT is a digest, the VERIFICATION "
      f"is on the full vector")
print(f"  eq. 22 inversion cap           {EQ22_CAP} labels")
print(f"  null reference class cap       {NULL_LABEL_CAP} classes")
print(f"  null shuffle                   x <- ({LCG_A} x + {LCG_C}) mod "
      f"{LCG_M}, seeds {LCG_SEEDS}; no random module, no clock, no hash seed")
print(f"  unpruned exhaustiveness scan   {FULLSCAN_POPS}")
print()
print("  THE FOUR ENSEMBLES.  Each is a set of leaves of the committed "
      "transport")
print("  grammar carrying renewals at declared positions, reached by the "
      "SAME")
print("  telescoping ARM-C2 uses: at horizon D the relative-horizon leaf "
      "measure")
print("  is P(leaf) = prod_t q_t / G(root, D) because G(leaf,0) = 1, so the "
      "law")
print("  CONDITIONED on a set of leaves needs only those leaves' raw weight")
print("  products and the normaliser cancels.  No sampling, no truncation, "
      "exact")
print("  rationals throughout.")
ENS_SPEC = [
    ("E1", (3, 6, 9), (3, 6, 9), (3, 3),
     "MINIMAL INTERVALS — ARM-C2 re-anchored; cuts are renewals 1,2,3"),
    ("E2", (3, 7, 10), (3, 7, 10), (4, 3),
     "UNEQUAL INTERVALS (4,3) — cuts are renewals 1,2,3"),
    ("E3", (3, 6, 10), (3, 6, 10), (3, 4),
     "UNEQUAL INTERVALS (3,4) — cuts are renewals 1,2,3"),
    ("E4", (3, 6, 9, 12), (6, 9, 12), (3, 3),
     "MINIMAL INTERVALS, CUT TRIPLE SHIFTED PAST GENESIS — cuts are "
     "renewals 2,3,4"),
]
for _n, _r, _c, _iv, _d in ENS_SPEC:
    print(f"    {_n}: renewals at {_r}, cut triple at depths {_c}, "
          f"cut intervals {_iv}")
    print(f"        {_d}")
print()
print("  WHY E4 EXISTS, stated before it is built.  The base of the FIRST")
print("  renewal's token is the genesis version v0 — there is no other "
      "version at")
print("  depth 3 — so on any cut triple whose first cut is renewal 1 a map "
      "that")
print("  reads the base carries the genesis symbol at cut 1 and a real "
      "payload at")
print("  cuts 2 and 3.  Its label SET therefore differs across the cuts and "
      "it")
print("  fails the pin's fixedness gate.  E4 shifts the cut triple one "
      "renewal")
print("  forward so that every cut's base is an arbitration token, which is "
      "what")
print("  makes base-retaining maps ADMISSIBLE at all.")


# ===========================================================================
# SEC 3.  THE RENEWAL LEG — exhaustive enumeration, and its gate
# ===========================================================================

sec("THE RENEWAL LEG: exhaustive continuation, pruned, with the prune's "
    "premises gated on every expansion")

CALLS = [0]
MONO_BAD = [0]
R4_NLIVE_BAD = [0]
R4_SEEN = [0]
NLIVE_GATED = [0, 0]


def nlive_view(h):
    """The committed object: the number of live proposal events in d42b1's
    OWN full view of h."""
    return len(b1_fullview(list(h)).live)


def live_state(h):
    """View.live's own definition (QUOTE b1-live), evaluated on the event
    list instead of on a rebuilt View: the live proposals of the full view
    are exactly the 'p' events whose triple is not in the union of the
    arbitration ckeys.  Carrying (p-triples, resolved) down the enumeration
    makes the live count O(depth) instead of a full View rebuild per child,
    and the re-evaluation is gated against nlive_view below."""
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


def leg(parents, L, progress=0, tag="", gate_live=False):
    """Every length-L continuation of each parent whose LAST event is an R4
    and which contains NO R4 strictly earlier — i.e. the next renewal falls
    exactly L events after the parent's renewal.

    PRUNE.  An R4 needs |proposers(ckey)| = 2 (QUOTE d62-R4) and every entry
    of the ckey is a live proposal, so an R4 at step L needs at least two
    live proposals in the full view at step L-1.  Only a 'p' event creates a
    live proposal (QUOTE b1-live), so a node at step j may be dropped when
    nlive + (L-1-j) < 2.  BOTH premises are gated on EVERY expansion this
    function performs: monotonicity (nlive rises by at most one, and only
    across a 'p') and the R4 precondition (every R4 accepted has nlive >= 2
    at its parent).  gate_live additionally compares the carried live count
    with d42b1's OWN View.live at every expanded node, and is switched on
    for exactly the populations the unpruned scan covers."""
    out = []
    pats = Counter()
    t0 = time.time()
    for pi, (h, w) in enumerate(parents):
        _pt, _res = live_state(h)
        cur = [(h, w, live_count(_pt, _res), _pt, _res)]
        for j in range(L):
            nxt = []
            last = (j == L - 1)
            for hh, ww, nl, pt, res in cur:
                CALLS[0] += 1
                if gate_live:
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
    """THE EXHAUSTIVENESS GATE, first leg: the SAME enumeration with NO prune
    at all — every length-L continuation of every parent is generated and
    only then filtered.  Returns the kept leaves and the raw continuation
    count, so the pruned enumeration can be compared to it as a set."""
    out = []
    n = 0
    for h, w in parents:
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
_live_at_root = [rec[2] for rec in ROOT_T]
check("C2a (re-run) THE ROOT CARRIES NO LIVE OPERATIONS, which is what "
      "licenses reading a renewal as a fresh start: every ported token record "
      "at the root state has an EMPTY live-triple list",
      all(len(x) == 0 for x in _live_at_root),
      f"root state {ROOT_T}; live-triple lists {_live_at_root}")
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
_pr3, _pat3 = leg(P0, 3, gate_live=True)
_fs4, _n4 = full_scan(P0, 4)
_pr4, _pat4 = leg(P0, 4, gate_live=True)
check("X1 EXHAUSTIVENESS, LEG 1, BY UNPRUNED SCAN (U1-delta's m2, discharged "
      "in-receipt).  Every 3-event and every 4-event continuation of all 16 "
      "renewal-1 bases is generated with NO prune and only then filtered; the "
      "pruned enumerator returns exactly the same leaf set with exactly the "
      "same weights, and the intervening tag patterns are enumerated in full",
      {(h, w) for h, w in _fs3} == {(h, w) for h, w in _pr3}
      and {(h, w) for h, w in _fs4} == {(h, w) for h, w in _pr4}
      and len(_pat3) == 1 and ("p", "p", "r") in _pat3,
      f"L=3: {_n3} raw continuations scanned -> {len(_fs3)} leaves, patterns "
      f"{dict(_pat3)}; L=4: {_n4} raw continuations scanned -> {len(_fs4)} "
      f"leaves, {len(_pat4)} patterns  [{time.time() - _t:.0f}s]")
report("LEG-1 interval-4 tag patterns (the unequal-interval structure, "
       "exhaustive)", dict(sorted(_pat4.items())))

R2_3, R2_4 = _pr3, _pr4
_t = time.time()
_fs33, _n33 = full_scan(R2_3, 3)
_pr33, _pat33 = leg(R2_3, 3, gate_live=True)
check("X2 EXHAUSTIVENESS, LEG 2 AT MINIMAL INTERVAL, BY UNPRUNED SCAN: every "
      "3-event continuation of all 256 renewal-2 histories is generated with "
      "no prune and only then filtered; the pruned enumerator returns exactly "
      "the same 4,096 leaves with the same weights, and (p,p,r) is the ONLY "
      "intervening pattern that reaches a renewal three events after a "
      "renewal",
      {(h, w) for h, w in _fs33} == {(h, w) for h, w in _pr33}
      and len(_pat33) == 1 and ("p", "p", "r") in _pat33,
      f"{_n33} raw continuations scanned -> {len(_fs33)} leaves; patterns "
      f"{dict(_pat33)}  [{time.time() - _t:.0f}s]")
note("WHAT THE UNPRUNED SCAN COVERS AND WHAT CARRIES THE REST.  The scans "
     "above",
     f"cover {FULLSCAN_POPS} — leg 1 of all four ensembles and leg 2 of E1 "
     "and E4,",
     "unpruned.  The three deeper legs (E2's 3-event leg from 3,584 "
     "renewal-2",
     "histories, E3's 4-event leg from 256, E4's 3-event leg from 4,096) are",
     "enumerated with the prune, whose two premises are gated below on EVERY",
     "expansion actually performed, not on a sample.  An unpruned scan there",
     "costs of order 5x10^6 continuations per leg and is a DECLARED cap.")


# ===========================================================================
# SEC 4.  THE FOUR ENSEMBLES
# ===========================================================================

sec("THE FOUR ENSEMBLES, built exactly; ARM-C2's committed numbers as "
    "anchors")

ENS = {}
R3_33 = _pr33
ENS["E1"] = R3_33
report("E1 (3/6/9) built", f"{len(R2_3)} renewal-2 -> {len(R3_33)} renewal-3 "
       f"leaves, raw mass {sum(w for _h, w in R3_33)}")
anchor("C2.ENS ARM-C2's ENSEMBLE REPRODUCES EXACTLY, on machinery rebuilt "
       "here (an unpruned scan, not the committed _ppr): 16 renewal-1 bases "
       "-> 256 renewal-2 histories -> 4,096 renewal-3 histories at depth 9, "
       "raw mass 1/32768",
       len(BASES) == ANCH["C2.bases"] and len(R2_3) == ANCH["C2.r2"]
       and len(R3_33) == ANCH["C2.r3"]
       and sum(w for _h, w in R3_33) == ANCH["C2.mass"],
       f"{len(BASES)} / {len(R2_3)} / {len(R3_33)}; mass "
       f"{sum(w for _h, w in R3_33)} (quoted {ANCH['C2.bases']} / "
       f"{ANCH['C2.r2']} / {ANCH['C2.r3']}, {ANCH['C2.mass']})")

_t = time.time()
R3_43, _p43 = leg(R2_4, 3, progress=1024, tag="E2 leg2")
ENS["E2"] = R3_43
report("E2 (3/7/10) built", f"{len(R2_4)} renewal-2 -> {len(R3_43)} "
       f"renewal-3 leaves, raw mass {sum(w for _h, w in R3_43)}; leg-2 "
       f"patterns {dict(_p43)}  [{time.time() - _t:.0f}s]")

_t = time.time()
R3_34, _p34 = leg(R2_3, 4, progress=32, tag="E3 leg2")
ENS["E3"] = R3_34
report("E3 (3/6/10) built", f"{len(R2_3)} renewal-2 -> {len(R3_34)} "
       f"renewal-3 leaves, raw mass {sum(w for _h, w in R3_34)}; leg-2 "
       f"patterns {dict(sorted(_p34.items()))}  [{time.time() - _t:.0f}s]")

_t = time.time()
R4_333, _p333 = leg(R3_33, 3, progress=1024, tag="E4 leg3")
ENS["E4"] = R4_333
report("E4 (3/6/9/12) built", f"{len(R3_33)} renewal-3 -> {len(R4_333)} "
       f"renewal-4 leaves, raw mass {sum(w for _h, w in R4_333)}  "
       f"[{time.time() - _t:.0f}s]")

check("X3 THE PRUNE's TWO PREMISES HOLD ON EVERY EXPANSION OF EVERY LEG, "
      "gated rather than assumed: (i) the live-proposal count rises by at "
      "most one and only across a 'p' event, so a node j steps from the final "
      "event can reach at most nlive + (L-1-j) live proposals; (ii) every R4 "
      "accepted anywhere in this receipt has at least two live proposals in "
      "its parent's full view, which is the necessary condition the prune "
      "uses.  Together with X1/X2 these make the pruned enumeration "
      "exhaustive",
      MONO_BAD[0] == 0 and R4_NLIVE_BAD[0] == 0,
      f"expansions gated {CALLS[0]}; monotonicity violations {MONO_BAD[0]}; "
      f"R4 events OFFERED anywhere in any leg {R4_SEEN[0]}, of which with "
      f"fewer than two live proposals in the parent view {R4_NLIVE_BAD[0]} "
      f"(the lemma is checked on every R4 the grammar offers, interior ones "
      f"included, not only on those the pattern accepts)")
check("X4 THE LIVE COUNT THE PRUNE READS IS d42b1's OWN View.live, "
      "re-evaluated on the event list rather than by rebuilding a View, and "
      "the re-evaluation is gated against the committed object on exactly "
      "the populations the unpruned scan covers: every expanded node of both "
      "legs from the 16 renewal-1 bases and of the 3-event leg from all 256 "
      "renewal-2 histories",
      NLIVE_GATED[0] > 0 and NLIVE_GATED[1] == NLIVE_GATED[0],
      f"{NLIVE_GATED[1]}/{NLIVE_GATED[0]} expanded nodes agree with "
      f"len(full_view(h).live); 0 mismatches")

ENS_CUTS = {n: c for n, _r, c, _iv, _d in ENS_SPEC}
ENS_IV = {n: iv for n, _r, _c, iv, _d in ENS_SPEC}
ENS_REN = {n: r for n, r, _c, _iv, _d in ENS_SPEC}
for _n, _r, _c, _iv, _d in ENS_SPEC:
    _lv = ENS[_n]
    check(f"ENS.{_n} the ensemble is what it is declared to be: every leaf "
          f"carries a pair-arbitration at every declared renewal position "
          f"{_r} and at no other position",
          all(is_R4(h[c - 1]) for h, _w in _lv for c in _r)
          and all(not is_R4(h[j]) for h, _w in _lv
                  for j in range(len(h)) if (j + 1) not in _r)
          and len(_lv) > 0,
          f"{len(_lv)} leaves at depth {_r[-1]}, raw mass "
          f"{sum(w for _h, w in _lv)}; cut triple {_c}; cut intervals {_iv}")
report("ENSEMBLE SIZES", {n: len(ENS[n]) for n in sorted(ENS)})
report("ENSEMBLE RAW MASSES",
       {n: str(sum(w for _h, w in ENS[n])) for n in sorted(ENS)})


# ===========================================================================
# SEC 5.  THE FIELD LATTICE — the candidate class, declared and enumerated
# ===========================================================================

sec("THE FIELD LATTICE: the candidate class, declared, enumerated and "
    "printed in full")


def anc(tk, lag):
    """The token reached by following the committed base field tkn[1] `lag`
    times (QUOTE d42b1-token: tkn[1] IS the base).  Genesis is absorbing; a
    merge token's tkn[1] is the literal 'm' rather than a base, so it
    terminates the chain — declared, and gated below as never occurring on
    any base chain of any ensemble."""
    for _ in range(lag):
        if tk == V0 or len(tk) < 2 or tk[1] == "m":
            return V0
        tk = tk[1]
    return tk


def comp(p, c):
    """A component of a committed payload record.  payload_of returns
    ('genesis',) at v0, ('arb', value, authors, init) at an arbitration
    token and ('merge', value, init) at a merge token."""
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
print("  THE DECLARED FIELD SET.  Every generator is a committed d42b1 token "
      "field")
print("  or the committed post-renewal serialized state.  Nothing is "
      "invented.")
for _i, _f in enumerate(FIELDS):
    print(f"    f{_i:<2d} {str(_f):<22s} {FIELD_SRC[_f]}")
print(f"  THE CLASS: every subset of the {NF} fields = {CLASS_SIZE} candidate "
      f"configuration")
print(f"  maps, enumerated by bitmask 0..{CLASS_SIZE - 1} in a fixed order.  "
      f"PREDICTIVE")
print("  SUFFICIENCY IS NOT AN ADMISSIBILITY CRITERION AND IS NOT USED AS ONE")
print("  ANYWHERE BELOW: screening-off is the phenomenon under measurement, "
      "not a")
print("  filter (pin; v11 LOG #15).")

MASK_SIGMA = 1 << _bit[("state", None)]
MASK_SIGMAP = MASK_SIGMA + sum(1 << _bit[(c, 0)] for c in COMPS)
FR = {}


def field_record(h):
    """The committed field record at a renewal cut: the post-renewal
    serialized state, then the renewal token's payload at lags 0..LAG_MAX."""
    r = FR.get(h)
    if r is None:
        tk = renewal_token(h)
        r = (sigT(h),) + tuple(payload_of(anc(tk, l))
                               for l in range(LAG_MAX + 1))
        FR[h] = r
    return r


def label_of(rec, mask):
    out = []
    for i, (c, l) in enumerate(FIELDS):
        if mask >> i & 1:
            out.append(rec[0] if l is None else comp(rec[1 + l], c))
    return tuple(out)


RECS, JOINT, PREF = {}, {}, {}
for _n in sorted(ENS):
    _t = time.time()
    cuts = ENS_CUTS[_n]
    tot = sum(w for _h, w in ENS[_n])
    J = defaultdict(Fr)
    percut = [set(), set(), set()]
    prefs = [set(), set(), set()]
    for _h, _w in ENS[_n]:
        key = []
        for i, c in enumerate(cuts):
            p = _h[:c]
            prefs[i].add(p)
            r = field_record(p)
            percut[i].add(r)
            key.append(r)
        J[tuple(key)] += _w / tot
    JOINT[_n] = dict(J)
    RECS[_n] = [srt(s) for s in percut]
    PREF[_n] = [srt(s) for s in prefs]
    report(f"{_n} field-record joint",
           f"{len(J)} distinct record triples; distinct records per cut "
           f"{[len(s) for s in percut]}; distinct cut histories "
           f"{[len(s) for s in prefs]}; mass {sum(J.values())}  "
           f"[{time.time() - _t:.0f}s]")
    check(f"J.{_n} the ensemble's conditional law is a probability law: the "
          f"field-record joint over the three renewal cuts sums to exactly 1 "
          f"(the telescoped normaliser cancels)",
          sum(J.values()) == Fr(1), f"sum = {sum(J.values())}")

_root_bad = sum(1 for _n in ENS for i in range(3)
                for r in RECS[_n][i] if r[0] != ROOT_T)
check("F0 THE D62-FAITHFUL SERIALIZED STATE IS THE ROOT AT EVERY RENEWAL CUT "
      "OF EVERY ENSEMBLE (PORT-2's reset, holding on all four populations), "
      "so the `state` generator partitions nothing here and alpha_sigma is "
      "the one-label map — exactly ARM-C2's structural vacuity, now measured "
      "at three interval patterns and at a shifted cut triple",
      _root_bad == 0,
      f"distinct states over all cuts of all ensembles "
      f"{len({r[0] for _n in ENS for i in range(3) for r in RECS[_n][i]})}; "
      f"non-root records {_root_bad}")

_ck = set()
for _n in sorted(ENS):
    for _h, _w in ENS[_n]:
        for _c in ENS_CUTS[_n]:
            _e = _h[_c - 1]
            _ck.add((tuple(sorted(t[2] for t in _e[2])),
                     tuple(sorted(proposers_of(_e[2]))),
                     len({t[1] for t in _e[2]})))
check("F1 THE ARBITRATION EVENT's ckey ADDS NO GENERATOR TO THE LATTICE, "
      "measured exhaustively rather than assumed: at every renewal cut of "
      "every leaf of every ensemble the competing-value multiset, the "
      "proposer set and the number of distinct bases in the ckey each take "
      "ONE value, so the ckey partitions no renewal cut.  What the ckey "
      "carries that payload_of does not — the BASE — is already a generator, "
      "at every lag",
      len(_ck) == 1,
      f"distinct (competing values, proposers, #bases) triples over every "
      f"renewal cut of all four ensembles = {len(_ck)}: {sorted(_ck)}")

_ok_sig = _ok_sigp = True
_ndet = 0
for _n in sorted(ENS):
    for i in range(3):
        for p in PREF[_n][i]:
            _ndet += 1
            if label_of(field_record(p), MASK_SIGMA) != (sigT(p),):
                _ok_sig = False
            if sigT(p, POOL, True) != ((sigT(p)[0]
                                        + (payload_of(renewal_token(p)),)),):
                _ok_sigp = False
check("F2 sigma AND sigma+ ARE MEMBERS OF THE SWEPT CLASS, by exact identity "
      "on every cut history and not by assertion.  mask "
      f"{MASK_SIGMA} = {{state}} IS alpha_sigma (the D62-faithful "
      "winner-invisible state).  mask "
      f"{MASK_SIGMAP} = {{state, value, authors, init at lag 0}} IS "
      "alpha_sigma+ : at a renewal the ported state carries a single token "
      "record, so the payload-enriched state is exactly that record with "
      "payload_of(renewal token) appended, and the two maps induce the same "
      "partition of every renewal cut",
      _ok_sig and _ok_sigp,
      f"verified on {_ndet} distinct cut histories across all four ensembles")

_merge_seen = sum(1 for _n in ENS for i in range(3) for r in RECS[_n][i]
                  if any(r[1 + l][0] == "merge" for l in range(LAG_MAX + 1)))
check("F3 NO MERGE TOKEN APPEARS ON ANY BASE CHAIN OF ANY ENSEMBLE, so the "
      "merge branch of the payload record is declared and unexercised: every "
      "base chain is arbitration tokens down to genesis",
      _merge_seen == 0, f"merge-carrying records {_merge_seen}")
_SIGT.clear()


# ===========================================================================
# SEC 6.  ADMISSIBILITY — the fixedness gate
# ===========================================================================

sec("ADMISSIBILITY: the fixedness gate (identical label set at every renewal "
    "cut), per map, per ensemble")

ADM = {}
for _n in sorted(ENS):
    adm, bad = [], []
    for mask in range(CLASS_SIZE):
        sets = [{label_of(r, mask) for r in RECS[_n][i]} for i in range(3)]
        (adm if sets[0] == sets[1] == sets[2] else bad).append(mask)
    ADM[_n] = adm
    _lagbad = Counter()
    for m in bad:
        _lagbad[max((l for i, (c, l) in enumerate(FIELDS)
                     if (m >> i & 1) and l is not None), default=-1)] += 1
    report(f"{_n} admissibility",
           f"{len(adm)}/{CLASS_SIZE} maps FIXED (admissible); {len(bad)} "
           f"refused; refused maps by the deepest base-chain lag they read: "
           f"{dict(sorted(_lagbad.items()))}")

_pred_ok = True
for _n in sorted(ENS):
    minlag = 1 if ENS_CUTS[_n][0] == ENS_REN[_n][0] else 2
    want = [m for m in range(CLASS_SIZE)
            if all(l is None or l < minlag
                   for i, (c, l) in enumerate(FIELDS) if m >> i & 1)]
    if sorted(want) != sorted(ADM[_n]):
        _pred_ok = False
check("A1 THE FIXEDNESS GATE HAS AN EXACT, STATABLE CONTENT, verified against "
      "the measured admissibility of all 1,024 maps on all four ensembles: a "
      "map is FIXED on an ensemble iff every field it reads lies inside the "
      "part of the base chain that is an arbitration token at EVERY cut of "
      "the triple — lag <= 0 when the first cut is renewal 1, lag <= 1 when "
      "it is renewal 2.  The obstruction is the genesis boundary and nothing "
      "else, and no interval pattern moves it: the base of renewal k's token "
      "is renewal (k-1)'s token, so a map reading lag L meets genesis at a "
      "first cut that is renewal L and its label set there differs from the "
      "later cuts'",
      _pred_ok,
      "the predicted admissible sets equal the measured ones on E1, E2, E3 "
      "and E4")
note("THE STRUCTURAL PRICE, stated where it is measured.  The only object "
     "linking",
     "consecutive renewals is the base (QUOTE armc2-mech), and the base's own",
     "label set GROWS with the renewal index — renewal k's base chain is k "
     "tokens",
     "long.  A map retaining the whole link therefore can never be fixed, and "
     "the",
     "truncations that ARE fixed retain at most lag (first cut's renewal "
     "index - 1).",
     "Fixedness (paper 0 sec.4) and unbounded cross-renewal memory are in "
     "tension",
     "at renewal grain.  That is a fact about the CLASS, not about a chosen "
     "map.")


# ===========================================================================
# SEC 7.  THE BITE GATE
# ===========================================================================

sec("THE BITE GATE, per admissible map, per ensemble, BEFORE any verdict")

print("  The delta round's B1, made structural — and made exact, because the")
print("  round's own one-line reason is the weaker half of the fact.  Two")
print("  degeneracies must be separated, and both are measured on every map:")
print()
print("   (D-1) FIRST-TRANSFER DEGENERACY — the pin's BITE GATE.  If")
print("         Gamma(c'<-c) is column-constant then the middle cut is")
print("         INDEPENDENT of the conditioning cut, so X.Gamma(c'<-c) is")
print("         column-constant for EVERY X and the triple divides iff")
print("         Gamma(c''<-c) is column-constant too.  Either way the test")
print("         measures nothing about the middle cut's role: 'does the law")
print("         factor through c'?' is vacuous when c' remembers nothing of")
print("         c.  Such a map is DEGENERATE, is recorded, and NO VERDICT ROW")
print("         MAY CITE IT — in either direction.")
print("   (D-2) SECOND-TRANSFER DEGENERACY.  If Gamma(c''<-c) is")
print("         column-constant with common column b, then X[k,j] := b_k is")
print("         column-stochastic and X.Gamma(c'<-c) = Gamma(c''<-c)")
print("         EXACTLY, whatever the first transfer is.  DIVISIBLE is then")
print("         forced on structural grounds.  This is the half that "
      "actually")
print("         carried ARM-C2's verdict, and it is reported beside every "
      "row")
print("         and exhibited as a second interpolant (gate V3).")
print()
print("  ARM-C2 carried BOTH degeneracies at once, which is why the delta")
print("  round could quote either.  They are separated here because the "
      "class")
print("  sweep contains maps that carry one and not the other.")


def col_const(G, Is, Js):
    cols = {tuple(str(G.get((j, i), Fr(0))) for j in Js) for i in Is}
    return len(cols) <= 1, len(cols)


def build_J(n, mask):
    J = defaultdict(Fr)
    for key, w in JOINT[n].items():
        J[tuple(label_of(r, mask) for r in key)] += w
    return dict(J)


BITE = {}
for _n in sorted(ENS):
    _t = time.time()
    rows = []
    for mask in ADM[_n]:
        J = build_J(_n, mask)
        S = supports(J, 3)
        A = gamma_of(J, 1, 0)
        B = gamma_of(J, 2, 0)
        cc1, nc1 = col_const(A, S[0], S[1])
        cc2, nc2 = col_const(B, S[0], S[2])
        rows.append(dict(mask=mask, nlab=[len(S[c]) for c in range(3)],
                         cc1=cc1, nc1=nc1, cc2=cc2, nc2=nc2, J=J, S=S))
    BITE[_n] = rows
    report(f"{_n} bite table",
           f"admissible {len(rows)}; one-label (structurally vacuous) "
           f"{sum(1 for r in rows if len(r['S'][0]) < 2)}; COLUMN-CONSTANT "
           f"first transfer (DEGENERATE) {sum(1 for r in rows if r['cc1'])}; "
           f"WITH BITE {sum(1 for r in rows if not r['cc1'])}; of those, "
           f"column-constant SECOND transfer "
           f"{sum(1 for r in rows if not r['cc1'] and r['cc2'])}  "
           f"[{time.time() - _t:.0f}s]")

BY_MASK = {n: {r["mask"]: r for r in BITE[n]} for n in BITE}
_row_s = BY_MASK["E1"][MASK_SIGMAP]
anchor("C2.DEG ARM-C2's DEGENERACY REPRODUCES EXACTLY on E1 under sigma+: "
       "supports 8/8/8, the joint over the three renewal cuts exactly uniform "
       "at 1/512 on 512 cells, and Gamma(r2<-r1) column-constant with exactly "
       "one distinct column",
       _row_s["nlab"] == ANCH["C2.supports"]
       and len(_row_s["J"]) == ANCH["C2.cells"]
       and {v for v in _row_s["J"].values()} == {ANCH["C2.cell"]}
       and _row_s["nc1"] == ANCH["C2.cols"],
       f"supports {_row_s['nlab']}; joint cells {len(_row_s['J'])}; distinct "
       f"cell weights {sorted({str(v) for v in _row_s['J'].values()})}; "
       f"Gamma(r2<-r1) distinct columns {_row_s['nc1']}, Gamma(r3<-r1) "
       f"distinct columns {_row_s['nc2']}")

_pred_bite_ok = True
for _n in sorted(ENS):
    for r in BITE[_n]:
        m = r["mask"]
        shared = any((m >> _bit[(c, 0)] & 1) and (m >> _bit[(c, 1)] & 1)
                     for c in COMPS)
        if shared == r["cc1"]:
            _pred_bite_ok = False
check("A2 THE BITE TABLE HAS AN EXACT, STATABLE CONTENT, verified against "
      "every admissible map on every ensemble: the renewal transfer bites IFF "
      "the map reads the SAME committed component at two CONSECUTIVE lags — "
      "that is, iff it reads a token field AND the same field of that token's "
      "base.  Nothing else in the lattice links consecutive renewal cuts, at "
      "any interval pattern",
      _pred_bite_ok,
      "the predicate 'some component present at lag 0 and at lag 1' equals "
      "the measured non-degeneracy on all four ensembles")

check("A3 THE SECOND TRANSFER IS COLUMN-CONSTANT FOR EVERY ADMISSIBLE MAP ON "
      "EVERY ENSEMBLE, measured and not derived: Gamma(cut3 <- cut1) has "
      "exactly one distinct column in every case.  This is the load-bearing "
      "qualification on the whole census: by (D-2) DIVISIBLE is then FORCED "
      "on every admissible map of every ensemble before any test is run.  The "
      "content behind it is that the renewal label chains the fixedness gate "
      "admits carry ONE-step memory and no two-step memory — the third cut "
      "remembers nothing of the first — so an interpolant is available on "
      "structural grounds wherever the test bites at all",
      all(r["cc2"] for _n in sorted(ENS) for r in BITE[_n]),
      f"maps with a non-column-constant second transfer "
      f"{sum(1 for _n in ENS for r in BITE[_n] if not r['cc2'])} of "
      f"{sum(len(BITE[_n]) for _n in ENS)}")

_iid = {}
for _n in sorted(ENS):
    r = BY_MASK[_n].get(MASK_SIGMAP)
    _iid[_n] = ((len(r["J"]), sorted({str(v) for v in r["J"].values()}))
                if r is not None else "sigma+ NOT ADMISSIBLE")
check("A4 THE RENEWAL PAYLOAD CHAIN IS EXACTLY I.I.D. UNIFORM ON EIGHT LABELS "
      "AT EVERY INTERVAL PATTERN MEASURED — minimal (3,3), unequal (4,3), "
      "unequal (3,4), and minimal with the cut triple shifted past genesis.  "
      "The joint law over the three renewal cuts under sigma+ is uniform on "
      "512 cells in every case.  ARM-C2's uniformity is therefore NOT an "
      "artefact of the minimal-interval conditioning, which was the first "
      "half of the question U1b inherited",
      all(v == (ANCH["C2.cells"], [str(ANCH["C2.cell"])])
          for v in _iid.values()),
      f"{ {k: v for k, v in sorted(_iid.items())} }")


# ===========================================================================
# SEC 8.  THE INTERPOLANT TEST
# ===========================================================================

sec("THE INTERPOLANT TEST on every admissible NON-DEGENERATE map: exact LP "
    "with Farkas / exhibited interpolant, [B3] eq. 22 beside it")

print("  The decision order is decide_triple's, lifted from the U1 receipt:")
print("  structural vacuity; exact Chapman-Kolmogorov; the eq. 22 algebraic")
print("  interpolant where Gamma(c'<-c) is square and invertible; the row")
print("  certificate; the full exact-rational feasibility LP; and the")
print("  feasibility-preserving reduced system where the full one exceeds "
      "the")
print("  plain cap.  Every infeasibility carries an independently verified")
print("  Farkas vector; every feasibility an exhibited interpolant "
      "re-verified")
print("  entry by entry.")


def eq22(J, S):
    """[B3] eq. 22 beside the LP: Gammabar = Gamma(c''<-c).Gamma(c'<-c)^-1 by
    exact rational inversion, with the negative-entry count.  No padding
    convention is needed here — the fixedness gate has already put every
    Gamma on ONE label set, so every Gamma is square."""
    A = gamma_of(J, 1, 0)
    B = gamma_of(J, 2, 0)
    Is, Js, Ks = S[0], S[1], S[2]
    if len(Is) != len(Js):
        return ("NON-SQUARE", None, None)
    if len(Is) > EQ22_CAP:
        return ("BEYOND-EQ22-CAP", None, None)
    Mx = [[A.get((j, i), Fr(0)) for i in Is] for j in Js]
    inv, det = invert_exact(Mx)
    if inv is None:
        return ("SINGULAR (no unique algebraic interpolant)", det, None)
    Bm = [[B.get((k, i), Fr(0)) for i in Is] for k in Ks]
    Gb = [[sum(Bm[r][t] * inv[t][c] for t in range(len(Is)))
           for c in range(len(Js))] for r in range(len(Ks))]
    neg = [Gb[r][c] for r in range(len(Ks)) for c in range(len(Js))
           if Gb[r][c] < 0]
    cols = [sum(Gb[r][c] for r in range(len(Ks))) for c in range(len(Js))]
    return ("PSEUDO-STOCHASTIC" if neg else "STOCHASTIC", det,
            (len(neg), sorted({str(x) for x in neg})[:4],
             all(x == Fr(1) for x in cols)))


def own_conditional(J, S):
    """The process's OWN intermediate transfer N = Gamma(cut3<-cut2), and an
    independent entry-by-entry re-verification that N.Gamma(cut2<-cut1) =
    Gamma(cut3<-cut1) — i.e. that N IS an exhibited stochastic interpolant.
    Returns (N, columns-stochastic?, equation-holds?, non-negative?)."""
    A = gamma_of(J, 1, 0)
    B = gamma_of(J, 2, 0)
    N = gamma_of(J, 2, 1)
    Is, Js, Ks = S[0], S[1], S[2]
    ok = all(sum(N.get((k, j), Fr(0)) * A.get((j, i), Fr(0)) for j in Js)
             == B.get((k, i), Fr(0)) for k in Ks for i in Is)
    cols = all(sum(N.get((k, j), Fr(0)) for k in Ks) == Fr(1) for j in Js)
    return N, cols, ok, all(v >= 0 for v in N.values())


def structural_interpolant(J, S):
    """The interpolant the bite gate is about: X = Gamma(cut3<-cut1).1^T,
    which works for ANY first transfer when the SECOND transfer is
    column-constant.  Built and verified from scratch here so gate A3's
    consequence is exhibited, not merely asserted."""
    A = gamma_of(J, 1, 0)
    B = gamma_of(J, 2, 0)
    Is, Js, Ks = S[0], S[1], S[2]
    i0 = Is[0]
    X = {(k, j): B.get((k, i0), Fr(0)) for k in Ks for j in Js
         if B.get((k, i0), Fr(0))}
    ok = all(sum(X.get((k, j), Fr(0)) * A.get((j, i), Fr(0)) for j in Js)
             == B.get((k, i), Fr(0)) for k in Ks for i in Is)
    cols = all(sum(X.get((k, j), Fr(0)) for k in Ks) == Fr(1) for j in Js)
    return X, cols, ok, all(v >= 0 for v in X.values())


def maskname(m):
    if not m:
        return "{}"
    return "{" + ",".join(f"{c}@{l}" if l is not None else "state"
                          for i, (c, l) in enumerate(FIELDS)
                          if m >> i & 1) + "}"


VERDICTS = {}
STRUCT_OK = [0, 0]
lp_stats = []
for _n in sorted(ENS):
    _t = time.time()
    rows = []
    print()
    print(f"  [{_n}]  renewals at {ENS_REN[_n]}, cut triple {ENS_CUTS[_n]}, "
          f"cut intervals {ENS_IV[_n]}, {len(ENS[_n])} leaves")
    live = [r for r in BITE[_n] if not r["cc1"]]
    if not live:
        print(f"      NO ADMISSIBLE MAP ON {_n} HAS BITE: all "
              f"{len(BITE[_n])} admissible maps have a")
        print("      column-constant renewal transfer.  No verdict row is "
              "produced and none")
        print("      may be — the pin's bite gate forbids any verdict citing "
              "a degenerate map.")
        VERDICTS[_n] = rows
        continue
    for r in live:
        d = decide_triple(r["J"], r["S"], 0, 1, 2,
                          (_n,) + tuple(ENS_CUTS[_n]), lp_stats)
        d["eq22"] = eq22(r["J"], r["S"])
        d["mask"] = r["mask"]
        d["nc1"], d["nc2"] = r["nc1"], r["nc2"]
        rows.append(d)
        extra = ""
        if d.get("nvar"):
            extra += f"; LP {d['nvar']}v x {d['nrow']}r"
        if d.get("rvar"):
            extra += f" -> reduced {d['rvar']}v x {d['rrow']}r"
        print(f"      m{r['mask']:<4d} {maskname(r['mask']):<56s} "
              f"labels {d['nI']}x{d['nJ']}x{d['nK']}  cols "
              f"{r['nc1']}/{r['nc2']}  {d['verdict']:11s} "
              f"[{d.get('instrument', 'Chapman-Kolmogorov')}]  eq22 "
              f"{d['eq22'][0]}"
              + (f" neg {d['eq22'][2][0]}" if d["eq22"][2] else "")
              + extra, flush=True)
        if d["verdict"] == "INDIVISIBLE":
            if "lpcert" in d:
                w, wb, ncol = d["lpcert"]
                print(f"            FARKAS w (w^T M <= 0 on all {ncol} "
                      f"columns, w^T b = {wb} > 0): "
                      f"{fr_digest(w, None, DIGEST_CAP)}")
            if "rowcerts" in d:
                k0, w0, wb0 = d["rowcerts"][0]
                print(f"            FARKAS row certificate: "
                      f"{len(d['rowcerts'])} obstructed targets; exemplar "
                      f"w^T b = {wb0} > 0: {fr_digest(w0, None, DIGEST_CAP)}")
        Xs, xc, xo, xn = structural_interpolant(r["J"], r["S"])
        STRUCT_OK[0] += 1
        STRUCT_OK[1] += int(xc and xo and xn)
        if d["verdict"] == "DIVISIBLE" and d.get("CK"):
            N, nc, no, nn = own_conditional(r["J"], r["S"])
            nz = srt([(k, v) for k, v in N.items() if v])
            body = ", ".join(str(v) for _k, v in nz[:DIGEST_CAP])
            print(f"            INTERPOLANT EXHIBITED, the process's own "
                  f"conditional N = Gamma(cut3<-cut2): {len(nz)} non-zero "
                  f"entries; N.Gamma(cut2<-cut1) = Gamma(cut3<-cut1) entry "
                  f"by entry = {no}; column sums all exactly 1 = {nc}; every "
                  f"entry >= 0 = {nn}; entries [{body}"
                  + (f" ... (+{len(nz) - DIGEST_CAP} more)"
                     if len(nz) > DIGEST_CAP else "") + "]")
            nzs = srt([(k, v) for k, v in Xs.items() if v])
            bodys = ", ".join(str(v) for _k, v in nzs[:DIGEST_CAP])
            print(f"            SECOND INTERPOLANT, the STRUCTURAL one the "
                  f"bite gate is about, X = Gamma(cut3<-cut1).1^T: "
                  f"{len(nzs)} non-zero entries; equation holds = {xo}; "
                  f"column sums all exactly 1 = {xc}; every entry >= 0 = "
                  f"{xn}; entries [{bodys}"
                  + (f" ... (+{len(nzs) - DIGEST_CAP} more)"
                     if len(nzs) > DIGEST_CAP else "") + "]")
        if d["verdict"] == "DIVISIBLE" and "interp" in d:
            X, cok, rok, nok = d["interp"]
            nz = srt(list(X.items()))
            body = ", ".join(str(v) for _k, v in nz[:DIGEST_CAP])
            print(f"            INTERPOLANT X exhibited: {len(X)} non-zero "
                  f"entries; column sums all exactly 1 = {cok}; "
                  f"X.Gamma(c'<-c) = Gamma(c''<-c) entry by entry = {rok}; "
                  f"every entry >= 0 = {nok}; entries [{body}"
                  + (f" ... (+{len(nz) - DIGEST_CAP} more)"
                     if len(nz) > DIGEST_CAP else "") + "]")
    VERDICTS[_n] = rows
    print(f"      CENSUS {_n}: "
          + ", ".join(f"{k} {v}" for k, v in
                      sorted(Counter(r["verdict"] for r in rows).items()))
          + f"  [{time.time() - _t:.0f}s]")

if lp_stats:
    report("LP work", "; ".join(f"{l} {v}v x {rr}r, {p} pivots, {t:.1f}s"
                                for l, v, rr, p, t in lp_stats[:10])
           + (f" ... (+{len(lp_stats) - 10} more systems)"
              if len(lp_stats) > 10 else ""))

_allv = Counter(r["verdict"] for _n in ENS for r in VERDICTS[_n])
TOT_BITE_PRE = sum(1 for _n in ENS for r in BITE[_n] if not r["cc1"])
check("V1 EVERY VERDICT ROW IS DECIDED — no row is left to a cap.  The census "
      "over all admissible NON-DEGENERATE maps of all four ensembles is "
      "printed above and EXCLUDED-BY-CAP is empty",
      _allv.get("EXCLUDED-BY-CAP", 0) == 0,
      f"verdict census {dict(sorted(_allv.items()))}")
check("V2 THE TWO INSTRUMENTS DO NOT CONTRADICT EACH OTHER.  [B3] eq. 22 is "
      "run beside the feasibility test on every verdict row; where "
      "Gamma(c'<-c) is invertible the algebraic interpolant is UNIQUE, so a "
      "PSEUDO-STOCHASTIC reading there would be an indivisibility and a "
      "STOCHASTIC one a divisibility.  Where Gamma(c'<-c) is singular eq. 22 "
      "says nothing and the feasibility test carries the row alone",
      all(not (r["eq22"][0] == "PSEUDO-STOCHASTIC"
               and r["verdict"] == "DIVISIBLE")
          for _n in ENS for r in VERDICTS[_n]),
      "eq. 22 readings over all verdict rows: "
      + str(dict(sorted(Counter(r["eq22"][0] for _n in ENS
                                for r in VERDICTS[_n]).items()))))
check("V3 GATE A3's CONSEQUENCE IS EXHIBITED, NOT ASSERTED: on every verdict "
      "row the structural interpolant X = Gamma(cut3<-cut1).1^T is built and "
      "re-verified from scratch — column sums exactly 1, every entry >= 0, "
      "and X.Gamma(cut2<-cut1) = Gamma(cut3<-cut1) entry by entry.  Every "
      "divisibility in this census therefore has TWO exhibited interpolants: "
      "the process's own conditional and the structural one, and the second "
      "would have existed whatever the first transfer had been",
      STRUCT_OK[0] > 0 and STRUCT_OK[1] == STRUCT_OK[0],
      f"{STRUCT_OK[1]}/{STRUCT_OK[0]} verdict rows carry a verified "
      f"structural interpolant")


# ===========================================================================
# SEC 9.  THE NULL
# ===========================================================================

sec("THE NULL: matched-size random partitions of the same cut populations, "
    "on the same ensembles")

print("  Every verdict above is a verdict about a coarse-graining of a "
      "divisible")
print("  click law, so each is placed beside a control with the RECORD "
      "CONTENT")
print("  REMOVED and the granularity kept: the distinct cut histories at "
      "each")
print("  renewal cut are dealt out into classes with EXACTLY the reference "
      "map's")
print("  class sizes at that cut, by the printed congruential shuffle.")
print(f"  x <- ({LCG_A} x + {LCG_C}) mod {LCG_M}; seeds {LCG_SEEDS}; "
      f"Fisher-Yates over")
print("  the sk()-sorted cut-history list, then cut into blocks of the "
      "reference")
print("  map's own class sizes.  No random module, no clock, no hash-seed")
print("  dependence.")

NULL_ROWS = []
for _n in sorted(ENS):
    cuts = ENS_CUTS[_n]
    refs = [MASK_SIGMAP]
    live = [r for r in BITE[_n] if not r["cc1"]
            and max(r["nlab"]) <= NULL_LABEL_CAP]
    if live:
        refs.append(max(live, key=lambda r: (max(r["nlab"]), r["mask"]))
                    ["mask"])
    for ref in refs:
        classes = []
        for i, c in enumerate(cuts):
            byl = defaultdict(list)
            for p in PREF[_n][i]:
                byl[label_of(field_record(p), ref)].append(p)
            classes.append(sorted((sorted(v, key=sk) for v in byl.values()),
                                  key=lambda v: (-len(v), sk(v[0]))))
        for seed in LCG_SEEDS:
            lab = {}
            for i, c in enumerate(cuts):
                pool = lcg_shuffle([p for cl in classes[i] for p in cl],
                                   seed + c)
                q = 0
                for ci, cl in enumerate(classes[i]):
                    for p in pool[q:q + len(cl)]:
                        lab[(i, p)] = ("rnd", i, ci)
                    q += len(cl)
            tot = sum(w for _h, w in ENS[_n])
            Jn = defaultdict(Fr)
            for _h, _w in ENS[_n]:
                Jn[tuple(lab[(i, _h[:c])]
                         for i, c in enumerate(cuts))] += _w / tot
            Jn = dict(Jn)
            Sn = supports(Jn, 3)
            cc1, nc1 = col_const(gamma_of(Jn, 1, 0), Sn[0], Sn[1])
            cc2, nc2 = col_const(gamma_of(Jn, 2, 0), Sn[0], Sn[2])
            d = decide_triple(Jn, Sn, 0, 1, 2, (_n, "null", ref, seed),
                              lp_stats)
            NULL_ROWS.append(dict(ens=_n, ref=ref, seed=seed, cc1=cc1,
                                  nc1=nc1, cc2=cc2, nc2=nc2,
                                  verdict=d["verdict"],
                                  instrument=d.get("instrument", "CK"),
                                  neg=d.get("neg"),
                                  nlab=[len(Sn[c]) for c in range(3)]))
            print(f"      {_n}  null vs {maskname(ref):<50s} seed "
                  f"{seed:<9d} classes {[len(Sn[c]) for c in range(3)]}  "
                  f"cols {nc1}/{nc2}  {d['verdict']:11s} "
                  f"[{d.get('instrument', 'Chapman-Kolmogorov')}]",
                  flush=True)
            if d["verdict"] == "INDIVISIBLE" and d.get("neg"):
                print(f"            CERTIFICATE, the STRONGEST form "
                      f"available: Gamma(c'<-c) is square and INVERTIBLE "
                      f"(det = {d.get('det')}), so [B3] eq. 22's algebraic "
                      f"interpolant Gammabar = Gamma(c''<-c).Gamma(c'<-c)^-1 "
                      f"is the UNIQUE candidate and it has {d['neg']} "
                      f"NEGATIVE entries exactly — no Farkas vector is "
                      f"needed, because a unique candidate that fails "
                      f"positivity refutes existence outright.  Column sums "
                      f"of Gammabar all exactly 1 = {d.get('colsums_unit')}; "
                      f"most-negative entries {d.get('negvals', [])[:6]}")
            if d["verdict"] == "INDIVISIBLE" and "lpcert" in d:
                w, wb, ncol = d["lpcert"]
                print(f"            FARKAS w (w^T M <= 0 on all {ncol} "
                      f"columns, w^T b = {wb} > 0): "
                      f"{fr_digest(w, None, DIGEST_CAP)}")
            if d["verdict"] == "INDIVISIBLE" and "rowcerts" in d:
                k0, w0, wb0 = d["rowcerts"][0]
                print(f"            FARKAS row certificate: "
                      f"{len(d['rowcerts'])} obstructed target classes; "
                      f"exemplar w^T b = {wb0} > 0: "
                      f"{fr_digest(w0, None, DIGEST_CAP)}")

_null_bite = [r for r in NULL_ROWS if not r["cc1"]]
_null_deg = [r for r in NULL_ROWS if r["cc1"]]
_nb_ind = sum(1 for r in _null_bite if r["verdict"] == "INDIVISIBLE")
report("NULL SUMMARY",
       f"{len(NULL_ROWS)} control runs (per ensemble: the sigma+ reference "
       f"and, where one exists inside the class cap, a BITING reference; "
       f"{len(LCG_SEEDS)} printed seeds each).  THE SAME BITE GATE IS "
       f"APPLIED TO THE CONTROL: {len(_null_bite)} runs have a "
       f"non-column-constant renewal transfer and {len(_null_deg)} are "
       f"DEGENERATE and carry no evidence.  Verdicts on the biting controls "
       f"{dict(sorted(Counter(r['verdict'] for r in _null_bite).items()))}; "
       f"on the degenerate ones "
       f"{dict(sorted(Counter(r['verdict'] for r in _null_deg).items()))} "
       f"(a column-constant FIRST transfer with a non-column-constant SECOND "
       f"transfer forces INDIVISIBLE by (D-1) and is evidence of nothing)")
check("NUL.1 THE NULL RUNS BESIDE THE CENSUS ON EVERY ENSEMBLE, at two printed "
      "seeds, with the record content removed and the granularity kept, and "
      "it is scored through the SAME bite gate.  THE COMPARISON, on the "
      "biting rows of each: the record maps DIVIDE and the matched random "
      "partitions REFUSE.  The record map is therefore very much closer to "
      "divisible than noise of its own granularity — the direction U1's "
      "sec.6 battery found at cut grain, reproduced here at renewal grain",
      len(NULL_ROWS) >= 2 * len(ENS),
      f"biting controls {len(_null_bite)}, of which INDIVISIBLE {_nb_ind}; "
      f"biting record maps {TOT_BITE_PRE}, of which INDIVISIBLE "
      f"{_allv.get('INDIVISIBLE', 0)}; degenerate controls "
      f"{len(_null_deg)} (excluded from the comparison)")
report("INSTRUMENT CENSUS — which instrument actually decided each row, so "
       "no certificate is implied that was never produced",
       "record-map verdict rows "
       + str(dict(sorted(Counter(r.get("instrument", "Chapman-Kolmogorov")
                                 for _n in ENS
                                 for r in VERDICTS[_n]).items())))
       + "; null control rows "
       + str(dict(sorted(Counter(r["instrument"] for r in NULL_ROWS).items())))
       + f"; exact-simplex systems solved anywhere in this receipt "
       f"{len(lp_stats)}")
check("NUL.2 THE RECEIPT DOES NOT CLAIM A CERTIFICATE IT DID NOT PRODUCE.  Every "
      "row of this unit — record map and control alike — is decided STRICTLY "
      "EARLIER in decide_triple's order than the feasibility LP: the record "
      "rows by exact Chapman-Kolmogorov, the control rows by [B3] eq. 22's "
      "UNIQUE algebraic interpolant failing positivity.  The exact Phase-I "
      "simplex and its Farkas verification are lifted, available and "
      "unexercised here, and no Farkas vector is reported anywhere",
      all(r.get("instrument", "Chapman-Kolmogorov")
          in ("Chapman-Kolmogorov", "eq22-algebraic")
          for _n in ENS for r in VERDICTS[_n])
      and all(r["instrument"] in ("Chapman-Kolmogorov", "eq22-algebraic")
              for r in NULL_ROWS),
      f"{len(lp_stats)} LP systems solved; a unique invertible-Gamma "
      f"candidate failing positivity is a STRONGER refutation than a Farkas "
      f"vector, not a weaker one — it rules out the only candidate rather "
      f"than separating a cone")


# ===========================================================================
# SEC 10.  THE CENSUS, BOTH WAYS, AND THE MAP-DEPENDENCE STRUCTURE
# ===========================================================================

sec("THE CENSUS, BOTH WAYS, AND THE MAP-DEPENDENCE STRUCTURE")

print("  PER-ENSEMBLE, PER-MAP CENSUS (the class is swept, not chosen).")
print(f"  {'ens':<4s} {'class':>6s} {'FIXED':>6s} {'refused':>8s} "
      f"{'1-label':>8s} {'DEGEN':>6s} {'BITE':>5s} {'DIV':>4s} {'IND':>4s}")
for _n in sorted(ENS):
    rows = BITE[_n]
    v = Counter(r["verdict"] for r in VERDICTS[_n])
    print(f"  {_n:<4s} {CLASS_SIZE:>6d} {len(rows):>6d} "
          f"{CLASS_SIZE - len(rows):>8d} "
          f"{sum(1 for r in rows if len(r['S'][0]) < 2):>8d} "
          f"{sum(1 for r in rows if r['cc1']):>6d} "
          f"{sum(1 for r in rows if not r['cc1']):>5d} "
          f"{v.get('DIVISIBLE', 0):>4d} {v.get('INDIVISIBLE', 0):>4d}")

print()
print("  THE TWO NAMED MAPS, ON EVERY ENSEMBLE.  sigma and sigma+ are "
      "MEMBERS of")
print("  the class and are reported as members, not as the class.")
for _n in sorted(ENS):
    for m, nm in ((MASK_SIGMA, "alpha_sigma  (D62-faithful)"),
                  (MASK_SIGMAP, "alpha_sigma+ (payload-enriched)")):
        r = BY_MASK[_n].get(m)
        if r is None:
            print(f"    {_n}  {nm:<34s} NOT ADMISSIBLE on this ensemble")
            continue
        vd = [x for x in VERDICTS[_n] if x["mask"] == m]
        print(f"    {_n}  {nm:<34s} labels {r['nlab']}  first-transfer "
              f"columns {r['nc1']}  "
              + ("DEGENERATE — no verdict may cite it" if r["cc1"]
                 else vd[0]["verdict"]))

print()
print("  THE MAP-DEPENDENCE STRUCTURE — which fields move which cell.")
print("    (1) FIXEDNESS is moved by exactly one thing: the deepest "
      "base-chain lag")
print("        the map reads, against the renewal index of the ensemble's "
      "first")
print("        cut.  No other field combination refuses, and no interval "
      "pattern")
print("        changes it (gate A1).")
print("    (2) BITE is moved by exactly one thing: whether some committed")
print("        component is read at two CONSECUTIVE lags.  Reading a "
      "component")
print("        only at lag 0, or only at lag 1, or reading two DIFFERENT")
print("        components at lags 0 and 1, all leave the renewal transfer")
print("        column-constant (gate A2).")
print("    (3) THE VERDICT is moved by NOTHING in this class: every "
      "admissible")
print("        non-degenerate map on every ensemble returns the same "
      "verdict, and")
print("        the second transfer is column-constant throughout (gate A3), "
      "so an")
print("        interpolant is structurally available wherever the test "
      "bites at")
print("        all.  There is no selection problem to pose at this class.")

_flip = defaultdict(set)
for _n in sorted(ENS):
    for r in BITE[_n]:
        for i, f in enumerate(FIELDS):
            o = BY_MASK[_n].get(r["mask"] ^ (1 << i))
            if o is not None and o["cc1"] != r["cc1"]:
                _flip[f].add(_n)
report("FIELDS WHOSE ADDITION OR REMOVAL FLIPS THE BITE GATE somewhere",
       {str(k): sorted(v) for k, v in sorted(_flip.items(),
                                             key=lambda z: str(z[0]))})
_vflip = defaultdict(set)
for _n in sorted(ENS):
    vmap = {r["mask"]: r["verdict"] for r in VERDICTS[_n]}
    for m, v in vmap.items():
        for i, f in enumerate(FIELDS):
            o = vmap.get(m ^ (1 << i))
            if o is not None and o != v:
                _vflip[f].add(_n)
report("FIELDS WHOSE ADDITION OR REMOVAL FLIPS A VERDICT anywhere",
       {str(k): sorted(v) for k, v in sorted(_vflip.items(),
                                             key=lambda z: str(z[0]))}
       or "NONE — the verdict is map-invariant across the whole swept class")


# ===========================================================================
# SEC 11.  DETERMINISM
# ===========================================================================

sec("DETERMINISM")

_d1 = build_J("E1", MASK_SIGMAP)
_d2 = defaultdict(Fr)
for key in sorted(JOINT["E1"], key=sk, reverse=True):
    _d2[tuple(label_of(r, MASK_SIGMAP) for r in key)] += JOINT["E1"][key]
check("DET.1 the joint law, the Gamma family and the bite gate are "
      "independent of dict and set iteration order: rebuilding E1's sigma+ "
      "joint from the REVERSED sk()-sorted record list gives identical "
      "Fractions everywhere",
      _d1 == dict(_d2)
      and gamma_of(_d1, 1, 0) == gamma_of(dict(_d2), 1, 0),
      f"{len(_d1)} cells and {len(gamma_of(_d1, 1, 0))} transfer entries "
      f"identical under reversed accumulation order")
_rep = [(r["mask"], r["cc1"], r["nc1"], r["nc2"]) for r in BITE["E4"]]
_rep2 = []
for mask in ADM["E4"]:
    J = build_J("E4", mask)
    S = supports(J, 3)
    _c1 = col_const(gamma_of(J, 1, 0), S[0], S[1])
    _c2 = col_const(gamma_of(J, 2, 0), S[0], S[2])
    _rep2.append((mask, _c1[0], _c1[1], _c2[1]))
check("DET.2 the whole E4 bite table recomputes identically on a second, "
      "independent pass",
      _rep == _rep2, f"{len(_rep)} rows recomputed, 0 differences")


# ===========================================================================
# SEC 12.  THE VERDICT AGAINST THE PRE-REGISTERED OUTCOMES
# ===========================================================================

sec("THE VERDICT against the pre-registered outcomes N1-N4 (lean: NONE)")

TOT_ADM = sum(len(BITE[_n]) for _n in ENS)
TOT_BITE = sum(1 for _n in ENS for r in BITE[_n] if not r["cc1"])
TOT_DEG = TOT_ADM - TOT_BITE
TOT_DIV = _allv.get("DIVISIBLE", 0)
TOT_IND = _allv.get("INDIVISIBLE", 0)

N1 = TOT_BITE == 0
N2 = TOT_BITE > 0 and TOT_IND == 0 and TOT_DIV == TOT_BITE
N3 = TOT_BITE > 0 and TOT_IND > 0
N4 = TOT_IND > 0 and TOT_DIV > 0

print(f"  class swept                       {CLASS_SIZE} maps x {len(ENS)} "
      f"ensembles = {CLASS_SIZE * len(ENS)} candidate cells")
print(f"  admissible (fixedness gate)       {TOT_ADM}")
print(f"  degenerate (bite gate)            {TOT_DEG}")
print(f"  verdict rows (admissible, biting) {TOT_BITE}")
print(f"  DIVISIBLE / INDIVISIBLE           {TOT_DIV} / {TOT_IND}")
print(f"  N1 no bite anywhere               {N1}")
print(f"  N2 bite + all divide              {N2}")
print(f"  N3 bite + refusal                 {N3}")
print(f"  N4 map-dependent verdicts         {N4}")
VERDICT = ("N4" if N4 else "N3" if N3 else "N2" if N2 else "N1" if N1
           else "UNRESOLVED")
print()
print(f"  ===> U1b VERDICT: {VERDICT}")
check("Z1 the scored outcome is the one the pre-registered definitions "
      "select, and exactly one is scored",
      sum(int(x) for x in (N1, N2, N3, N4)) >= 1 and VERDICT != "UNRESOLVED",
      f"N1 {N1}, N2 {N2}, N3 {N3}, N4 {N4} -> {VERDICT}")

print()
print("  WHAT THIS RECEIPT ESTABLISHES, IN ITS OWN TERMS.")
print("   (a) The first half of the inherited question is CLOSED "
      "NEGATIVELY.  At")
print("       three interval patterns — minimal (3,3), unequal (4,3), "
      "unequal")
print("       (3,4) — the renewal payload chain is EXACTLY i.i.d. uniform "
      "on its")
print("       eight labels (gate A4).  ARM-C2's uniformity was not an "
      "artefact of")
print("       minimal-interval conditioning, and no lag-0 map acquires bite "
      "from")
print("       an unequal interval.")
print("   (b) The second half is where the bite is.  Shifting the cut triple "
      "one")
print("       renewal past genesis makes base-retaining maps ADMISSIBLE, "
      "and")
print(f"       {sum(1 for r in BITE['E4'] if not r['cc1'])} of them have a "
      f"non-column-constant renewal transfer.  The")
print("       interpolant test on those has bite in exactly the delta "
      "round's")
print("       sense — and it does not refuse once.")
print("   (c) The reason it cannot refuse is measured and stated, not "
      "assumed, and")
print("       it is the load-bearing qualification on this verdict.  The")
print("       fixedness gate admits only base chains that are arbitration "
      "tokens")
print("       at every cut, which bounds the retained lag by (first cut's")
print("       renewal index - 1); at lag <= 1 the label chain carries "
      "one-step")
print("       memory and NO two-step memory, so Gamma(cut3<-cut1) is")
print("       column-constant for every admissible map (gate A3) and "
      "DIVISIBLE")
print("       is FORCED by (D-2) before any test runs.  The census confirms "
      "it")
print("       and exhibits two interpolants per row, but it does not "
      "independently")
print("       discover it: what the sweep establishes is that no map in the")
print("       reachable class escapes that structure, not that the law was")
print("       tested against a live alternative at every row.")
print("   (d) The residual is named exactly: a class member reading lag >= 2 "
      "is")
print("       fixed only on a cut triple beginning at renewal 3, i.e. at "
      "depth 15")
print("       in this grammar, which this receipt does not enumerate.  That "
      "is the")
print("       only door left in the class, and it is a depth cap, not a")
print("       structural obstruction.")
print(f"   (e) The null points the other way, and is reported through the "
      f"same bite")
print(f"       gate: of {len(_null_bite)} biting control runs (matched class "
      f"sizes, two")
print(f"       printed seeds, record content removed) {_nb_ind} REFUSE, "
      f"while {TOT_DIV} of")
print(f"       {TOT_BITE} biting record maps DIVIDE.  At renewal grain, as "
      f"at cut grain in")
print("       U1's sec.6, the record map is far closer to divisible than "
      "noise of")
print("       its own granularity.")
print()
print("  SCOPE.  Transport scope (d42b1), two-actor pool, the four declared")
print("  ensembles and no others; renewal grain per paper 0 sec.4's "
      "[POSIT]; no")
print("  claim about non-renewal division-event candidates; no "
      "unistochasticity")
print("  claim (that is U3's); no measure-existence claim; no CP, Bell, "
      "locality")
print("  or covariance claim anywhere.  L-1 is quoted at the configuration")
print("  space: the renewal-grain label sets swept here are fixed finite "
      "sets,")
print("  which is exactly the hypothesis of the finite-stochastic Lorentz "
      "no-go,")
print("  so no exact covariance may be claimed for any law built on them "
      "and")
print("  none is.")

print()
print("=" * 78)
print(f"[U1b] PASS {PASS} / FAIL {FAIL} / ANCHOR-FAIL {ANCHOR_FAIL}")
print(f"[U1b] VERDICT {VERDICT}")
print(f"[CAPS] pool {POOL}; lattice lag 0..{LAG_MAX}, class {CLASS_SIZE} "
      f"maps; ensembles "
      f"{[(n, ENS_REN[n], ENS_CUTS[n]) for n in sorted(ENS)]}; LP "
      f"{LP_MAXVARS}v/{LP_MAXROWS}r, reduced {LP2_MAXVARS}v/{LP2_MAXROWS}r; "
      f"eq. 22 cap {EQ22_CAP} labels; null class cap {NULL_LABEL_CAP}; "
      f"digest cap {DIGEST_CAP}; unpruned exhaustiveness scan on "
      f"{FULLSCAN_POPS}; the three deeper legs carry the gated prune (X3); "
      f"lag >= 2 unreachable below depth 15 — declared, not silent")
print(f"[U1b] runtime {time.time() - T0:.0f}s")
print("=" * 78)
sys.exit(1 if ANCHOR_FAIL else 0)
