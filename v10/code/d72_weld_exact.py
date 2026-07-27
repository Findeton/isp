#!/usr/bin/env python3
"""
d72_weld_exact.py — v10 D72 THE WELD: the reversal-holonomy identity.

Pin: v10/note-d72-weld-pin.md (FROZEN).  Parents: D71b
(note-d71b-holonomy-phase-identity.md), D71
(note-d71-phase-archaeology.md).

P1 under test (pin, verbatim):
  "v7 paper 30's odd channel is the reversal-odd channel of a
   probability-transport holonomy, and its phase e^{i Phi(O)} is that
   holonomy: concretely, the order-dual * on a five-record type
   (paper30:2511) coincides, on the generated line's own objects, with
   the transport-order reversal AB -> BA that defines
   A_D = log dP_AB/dP_BA (v6 p4 sec.34), and the amplitude
   A(R) ~ e^{-K(E)} e^{i Phi(O)} is the U(1) holonomy of sqrt(q)-transport
   around delete-then-insert round trips of the record deletion graph,
   with A_D as its real part (log-modulus) and Phi(O) as its argument."

HOUSE RULES OBSERVED
  * Exact arithmetic (fractions.Fraction) wherever the objects are
    rational.  Every v10 step weight q is rational; every A_D is the
    logarithm of an EXACT Fraction and the gates are stated on the
    Fraction, never on its float image.
  * Committed layers are consumed by TEXT-SLICE of their own sources,
    with (a) verbatim fidelity markers asserted present before the
    slice is executed and (b) EXIT-FREEDOM GATED: sys.exit / os._exit
    are neutralised inside the sliced exec so an imported layer can
    never decide this receipt's exit status.
  * No bare-constant predicates.  Every threshold is either a QUOTED
    committed value (registry QUOTES, each with path:line provenance)
    or a quantity derived inside this receipt.
  * Substantive negatives exit 0.  exit 1 is reserved for anchor
    failure (a committed object that fails to reproduce).

RUNTIME.  ~7-10 min, dominated by ANCHOR A2 (the v7 N=9 record
universe).  Set D72_SKIP_A2=1 to skip that anchor (it then reports
SKIPPED and the receipt still exits on its own gates); the default is
to run it.

ROUND 1 (reviews/d72-round1-hostile-review.md, REVISE: 5 MAJOR /
5 MODERATE / 6 MINOR).  Every arithmetic claim of the first delivery
reproduced under the referee's independent rebuild; the round broke the
SCOPE, the INSTRUMENT and the WEIGHT CHOICE.  What this version adds,
all of it recomputed here from the committed layers and none of it
copied from the review:
  T6  the TRANSPORT-SCOPE square census on grammar 2 (d42b1), which the
      first delivery asserted and never ran: A_D is NOT zero there.
  T6.3 the instrument's blind spot: none of those defects closes at
      record level, so the record-deletion-graph census cannot see them.
  T4  the NORMALISED kernel (p = q / menu mass): the connection still
      descends, and its holonomy is NOT trivial — it is <5/4> in R+,
      which is D65's committed mass-ratio coboundary and is falsifier
      F4's shape.  F4 FIRES; it is no longer "vacuous".
  T5  the referee's APPENDIX theorem (grammar-1 raw flatness, depth-free)
      adopted as the round's contribution, with L1/L3/L4/L5/L6 gated.
  T2.0 the potential identity mu(C2)/mu(C1): T2.1-T2.5 are corollaries
      of T1.8, not independent measurements.
  k=5  the T3 cell the first delivery said "does not exist here".
  The licensed window is widened from bases |h|<=3 to bases |h|<=5
  (depth <= 7) at no new enumeration cost, plus 3- and 4-actor arms.
"""

from __future__ import annotations

import math
import os
import sys
import time
from collections import Counter, defaultdict
from fractions import Fraction as Fr
from itertools import combinations, permutations

T0 = time.time()
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.dirname(REPO)  # .../isp
os.chdir(REPO)

PASS = FAIL = 0
ANCHOR_FAIL = 0
COROLLARY = []      # MODERATE 4: gates that carry no INDEPENDENT information


def check(label, ok, detail="", corollary_of=None):
    """corollary_of: this gate is entailed by another gate (or is a theorem
    true of every object of its type).  It is still run and still printed,
    but it is NOT counted as independent evidence in the summary — the
    round's MODERATE 4."""
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    PASS += int(bool(ok))
    FAIL += int(not ok)
    if corollary_of is not None:
        COROLLARY.append((label.split(":")[0].split("  ")[0], corollary_of))
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))
    if corollary_of is not None:
        print(f"         ^ NO INDEPENDENT INFORMATION: {corollary_of}")
    return bool(ok)


def anchor(label, ok, detail=""):
    global ANCHOR_FAIL
    if not check("ANCHOR " + label, ok, detail):
        ANCHOR_FAIL += 1
    return bool(ok)


def report(label, value):
    print(f"  [DATA] {label}: {value}")


# ===========================================================================
# SEC 0.  THE QUOTE REGISTRY — every constant this receipt tests against is
#         a verbatim committed string or number, with provenance.
# ===========================================================================

QUOTES = {
    "star": (
        "v7/relativistic-isp-v7-paper30-rooted-boundary-law.md:2506-2511",
        "Let `\\ast` denote the order-dual operation on a five-record "
        "sector: F^\\ast = the same five-record type with every order "
        "relation reversed.",
    ),
    "EO": (
        "v7/relativistic-isp-v7-paper30-rooted-boundary-law.md:2724-2735",
        "For a dual pair (F,F*), define E_F(R)=F(R)+F^\\ast(R), the even "
        "count, and O_F(R)=F(R)-F^\\ast(R), the dual-odd imbalance.",
    ),
    "Ldual": (
        "v7/relativistic-isp-v7-paper30-rooted-boundary-law.md:2843-2849",
        "L_dual = e^{-kE}e^{i theta O}; E is dual-even data such as F+F*; "
        "O is dual-odd data such as F-F*; dual reversal sends O to -O; "
        "therefore dual reversal sends L to its complex conjugate.",
    ),
    "AD": (
        "v6/relativistic-isp-v6-paper4.md:2607-2645 (sec.34)",
        "A_D = log dP_AB / dP_BA, the exchange cocycle.",
    ),
    "AD_row": (
        "v6/relativistic-isp-v6-paper4.md:2636",
        "| antisymmetry | reverse ordering has action -A_D | orientation "
        "reversal is fixed | gap=2.2e-16 | PASS |",
    ),
    "loop_row": (
        "v6/relativistic-isp-v6-paper4.md:2637",
        "commuting/eventless loop has zero action (rms 0.0e+00)",
    ),
    "drift": (
        "v7/relativistic-isp-v7-paper30-rooted-boundary-law.md:1999",
        "the receipt measures deletion drift from N=9 to N=8 and insertion "
        "drift from N=8 to N=9",
    ),
    "sqrtq": (
        "v10/note-d42b4-quantum-lift.md:15-18",
        "The lift assigns each complete depth-D history the amplitude "
        "prod sqrt(q) (the #152 budget amplitudes) on record ancillas.",
    ),
    "H1zero": (
        "v8/relativistic-isp-v8-paper1-foundations-click-law.md:77",
        "On a one-dimensional commit path H^1 = 0.",
    ),
    "d65": (
        "v10/note-d65-descent-conditions-result.md:173-182",
        "The defect is exactly the intermediate-mass ratio.  For every "
        "commuting pair, d = M(sigma(Hb)) / M(sigma(Ha)), with M the "
        "per-state menu mass ... 34 states of mass 2 and 2 states of mass "
        "5/2 ... Spectrum: {1: 576654, 4/5: 44316, 5/4: 44316} — exactly "
        "the ratio set of the two masses.",
    ),
}

# committed NUMERIC anchors (quoted values, never re-derived here)
NAIVE_DUALCONJ_ERROR_V7 = "1.8210207227600682556870097725525"   # paper30:2838
DUAL_DUALCONJ_ERROR_V7 = "0"                                     # paper30:2851
V6_ANTISYM_GAP_QUOTED = 2.2e-16                                  # v6 p4:2636
D42B4_ZSEQ = Fr(4)      # note-d42b4 / d42b4 receipt: Z_seq  = 4
D42B4_ZCLASS = Fr(3)    # note-d42b4 / d42b4 receipt: Z_class = 3
D42B4_NSEQ = 32         # note-d42b4 / d42b4 receipt: 32 depth-2 sequences
D65_MASSES = {Fr(2), Fr(5, 2)}                    # QUOTES['d65'], note:176-177
D65_DEFECT_RATIOS = {Fr(4, 5), Fr(1), Fr(5, 4)}   # QUOTES['d65'], note:181
FLOAT_EPS = sys.float_info.epsilon   # every float tolerance below is a
FLOAT_TOL = 64 * FLOAT_EPS           # derived multiple of this, not a
                                     # typed-in power of ten (MINOR 1)

print("=" * 78)
print("D72 — THE WELD: the reversal-holonomy identity (exact receipt)")
print("=" * 78)
print("  banner: exact Fractions on every v10 weight; committed layers by")
print("  text-slice with fidelity markers + gated exit-freedom; quoted")
print("  constants only (registry below); substantive negatives exit 0.")
print()
print("  FIDELITY QUOTES (the operationalisations below are held to these):")
for k, (where, text) in QUOTES.items():
    print(f"    [{k}] {where}")
    for i in range(0, len(text), 68):
        print(f"        {text[i:i+68]}")


# ===========================================================================
# SEC 0.1  TEXT-SLICE LOADER, with gated exit-freedom
# ===========================================================================

class _NoExit(Exception):
    pass


def slice_exec(path, cut_marker, fidelity_markers, name):
    """Execute the definition head of a committed source.

    cut_marker       : the first module-level *executable* statement; the
                       slice is everything strictly before it.
    fidelity_markers : verbatim substrings that MUST be present in the
                       source, so that a silent upstream edit cannot let an
                       unfaithful operationalisation through unnoticed.
    Exit-freedom is gated: sys.exit / os._exit raise inside the slice and
    are restored afterwards, so the imported layer cannot set our status.
    """
    src = open(path).read()
    missing = [m for m in fidelity_markers if m not in src]
    if missing:
        raise SystemExit(f"FIDELITY MARKER MISSING in {path}: {missing[:2]}")
    idx = src.index(cut_marker)
    head = src[:idx]
    import types as _types
    mod = _types.ModuleType(name)
    sys.modules[name] = mod          # so dataclasses can resolve __module__
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


print()
print("-" * 78)
print("SEC 0.1  committed sources, sliced")
print("-" * 78)

# --- the generated line, grammar 1 (placement layer) ------------------------
B3, b3n, b3tot = slice_exec(
    "v10/code/d42b3_placement_exact.py",
    'print("[d42b3',
    ["def candidates_for(acts, actors):",
     "def admissible(acts, e):",
     "def event_poset(acts):",
     "def canon(acts):",
     "def mu_of(acts):",
     "def regs_of(op):",
     "def prop_options_in_view(view, a):",
     "def arb_components_in_view(view, a):"],
    "d72_d42b3",
)
report("d42b3 slice", f"{b3n}/{b3tot} bytes; "
       f"exports = candidates_for/admissible/event_poset/canon/mu_of/"
       f"regs_of/prop_options_in_view/arb_components_in_view")

# --- the generated line, grammar 2 (transport/reconciliation layer) ---------
B1, b1n, b1tot = slice_exec(
    "v10/code/d42b1_transport_exact.py",
    'print("[d42b1',
    ["def candidates_for(acts, actors):",
     "def admissible(acts, e, actors, law=PK1):",
     "def linear_extensions(acts):",
     "def canon(acts):",
     "def regs_of(op):"],
    "d72_d42b1",
)
report("d42b1 slice", f"{b1n}/{b1tot} bytes; second grammar (A7 ladder)")

# --- v7 paper 30's own order-dual and complex-Laplace machinery -------------
sys.path.insert(0, os.path.join(REPO, "v7", "code"))
P30, p30n, p30tot = slice_exec(
    "v7/code/p30_complex_amplitude_campaign.py",
    'print("=" * 80)',
    ["def opposite_bits(bits, n):",
     "def dual_key(key, n):",
     "def complex_laplace_by_mode(mode, pairs, kappa, root, n=9):",
     "def laplace_dual_conjugation_error(pairs, kappa, root, mode):",
     '        elif mode == "dual_complex":',
     "def fast_flag_counts(bits, n, k):"],
    "d72_p30",
)
report("p30 slice", f"{p30n}/{p30tot} bytes; the * (opposite_bits/dual_key) "
       "and L_dual (complex_laplace_by_mode) machinery")

# --- v6 paper 4 sec.34's own exchange-cocycle machinery ---------------------
P4N, p4nn, p4ntot = slice_exec(
    "code/v6_p4n_exchange_cocycle_law.py",
    "def main() -> None:",
    ["def rn_action(p: list[float], q: list[float]) -> list[float]:",
     "    return [math.log(pi / qi) for pi, qi in zip(p, q)]",
     "def exchange_laws(k_a: list[list[float]], k_b: list[list[float]])",
     "def flatten_law(matrix: list[list[float]]) -> list[float]:"],
    "d72_p4n",
)
report("v6 p4n slice", f"{p4nn}/{p4ntot} bytes; exchange_laws + rn_action "
       "(the A_D machinery)")


# ===========================================================================
# SEC 1.  ANCHORS — committed objects must reproduce, else exit 1
# ===========================================================================

print()
print("-" * 78)
print("SEC 1  ANCHORS (exit 1 on failure)")
print("-" * 78)

# --- A1: the v6 exchange-cocycle receipt, rerun in its own machinery -------
_n = 18
_ka = P4N["stochastic_transport"](_n, phase=0.15, eps=0.62, sigma=2.15,
                                  handedness=1.0)
_kb = P4N["stochastic_transport"](_n, phase=0.90, eps=0.58, sigma=2.35,
                                  handedness=-1.0)
_pab, _pba = P4N["exchange_laws"](_ka, _kb)
_AD = P4N["rn_action"](_pab, _pba)
_rev = P4N["rn_action"](_pba, _pab)
_antisym_gap = P4N["max_gap"](_rev, [-v for v in _AD])
_pe, _qe = P4N["exchange_laws"](_ka, _ka)
_eventless_rms = P4N["rms"](P4N["rn_action"](_pe, _qe))
anchor("A1 v6 p4 sec.34 antisymmetry row reproduces "
       f"(quoted {QUOTES['AD_row'][0]}: gap=2.2e-16)",
       _antisym_gap <= 10.0 * V6_ANTISYM_GAP_QUOTED and _eventless_rms == 0.0,
       f"antisymmetry gap = {_antisym_gap:.3e} (quoted 2.2e-16); "
       f"eventless loop rms = {_eventless_rms:.1e} (quoted 0.0e+00)")

# --- A2: v7 paper 30's dual-conjugation numbers, in v7's own machinery -----
SKIP_A2 = os.environ.get("D72_SKIP_A2") == "1"
if SKIP_A2:
    print("  [SKIP] ANCHOR A2 (D72_SKIP_A2=1) — the v7 N=9 dual-conjugation "
          "numbers are NOT re-derived in this run")
    a2_naive = a2_dual = None
else:
    _t = time.time()
    reps_by_n = {}
    for _k in range(1, 10):
        _c, _r, _d = P30["build_record_universe"](_k)
        reps_by_n[_k] = _r
    P30["reps_by_n"] = reps_by_n
    feature_cache = {9: {"flags5": {k: P30["fast_flag_counts"](b, 9, 5)
                                    for k, b in reps_by_n[9].items()}}}
    P30["feature_cache"] = feature_cache
    D = P30["D"]
    PAIRS = ((24576, 540672), (25488, 525208), (24606, 549648))   # p30:2700
    KAPPA = D("0.03125")                                           # p30 campaign
    ROOT = P30["ROOTS"]["pi/6"]                                    # p30 campaign
    a2_naive = P30["laplace_dual_conjugation_error"](
        PAIRS, KAPPA, ROOT, "naive_complex")
    a2_dual = P30["laplace_dual_conjugation_error"](
        PAIRS, KAPPA, ROOT, "dual_complex")
    # v7 prints this with fmt_dec(., 32) at p30_complex_amplitude_campaign.py
    # line 732; the published string carries 32 significant digits.
    _naive_str = P30["fmt_dec"](a2_naive, 32)
    anchor("A2 v7 paper30 dual-conjugation: naive = "
           f"{NAIVE_DUALCONJ_ERROR_V7} (p30:2838), L_dual = "
           f"{DUAL_DUALCONJ_ERROR_V7} (p30:2851)",
           _naive_str == NAIVE_DUALCONJ_ERROR_V7 and a2_dual == 0,
           f"recomputed naive = {_naive_str}; recomputed L_dual = "
           f"{a2_dual}; N=9 records = {len(reps_by_n[9])}; "
           f"{time.time()-_t:.0f}s")
    # A2b: v7's own * is an involution on its own universe
    _inv_ok = all(P30["dual_key"](P30["dual_key"](k, 7), 7) == k
                  for k in reps_by_n[7])
    anchor("A2b the committed * (opposite_bits/dual_key) is an involution "
           "on v7's own record universe (N=7)",
           _inv_ok, f"{len(reps_by_n[7])} records at N=7")

# --- A2c: the SAME anchor, reached independently of the N=9 run -----------
# The dual-conjugation error of v7's own two modes has an exact closed form
# (derivation in SEC 5): with * : E -> E, O -> -O and rho = e^{i theta},
#     |L_dual(R*)  - conj L_dual(R)|  = 0
#     |L_naive(R*) - conj L_naive(R)| = 2 e^{-kappa E} |sin(theta E)|
# At v7's own kappa = 1/32 and theta = pi/6 the second is maximised over
# integer E at E = 3 (where |sin| = 1), giving 2 e^{-3/32}.  If that equals
# paper30:2838's published constant to all of its published digits, then
# this receipt's port of L_naive/L_dual is the SAME function v7 evaluated —
# an operationalisation-fidelity anchor that costs nothing.
from decimal import Decimal as _Dec, getcontext as _gc
_gc().prec = 140
_closed_at_3 = 2 * (_Dec(-3) / 32).exp()
_closed_str = str(_closed_at_3)[:len(NAIVE_DUALCONJ_ERROR_V7)]
_ARGMAX_RANGE = 4000     # MINOR 1: the round checked 0..3999; so do we
_argmax_ok = all(
    2 * math.exp(-3 / 32.0) >= 2 * math.exp(-e / 32.0)
    * abs(math.sin(math.pi * e / 6)) - FLOAT_TOL
    for e in range(0, _ARGMAX_RANGE))
anchor("A2c the exact closed form of v7's dual-conjugation error, "
       "maximised over integer E, REPRODUCES paper30:2838's published "
       f"constant {NAIVE_DUALCONJ_ERROR_V7} — with no re-run of the N=9 "
       "universe",
       _closed_str == NAIVE_DUALCONJ_ERROR_V7 and _argmax_ok,
       f"2*exp(-3/32) = {_closed_str}; argmax over E in "
       f"0..{_ARGMAX_RANGE-1} is E = 3 "
       f"({_argmax_ok}).  COROLLARY, and it is a finding: v7's headline "
       "'1.82' is a closed-form constant of the ANSATZ, not a measurement "
       "of the N=9 record universe — it says only that some record has "
       "E = 3.")

# --- A3: the generated line's own committed anchors ------------------------
AB = ("A", "B")
V0 = B3["V0"]
b3_candidates = B3["candidates_for"]
b3_admissible = B3["admissible"]
b3_canon = B3["canon"]
b3_poset = B3["event_poset"]
b3_mu = B3["mu_of"]
b3_regs = B3["regs_of"]          # L2/L4: comparability = register overlap
b3_View = B3["View"]
b3_propopts = B3["prop_options_in_view"]
b3_arbcomps = B3["arb_components_in_view"]

_seqs = []
for _e1, _q1 in b3_candidates([], AB):
    for _e2, _q2 in b3_candidates([_e1], AB):
        _seqs.append(((_e1, _e2), _q1 * _q2))
_Zseq = sum(m for _, m in _seqs)
_cls = {}
for _s, _m in _seqs:
    _cls.setdefault(b3_canon(list(_s)), set()).add(_m)
_gauge_single = all(len(v) == 1 for v in _cls.values())
_Zclass = sum(next(iter(v)) for v in _cls.values())
anchor("A3 the F-PAIR fixture reproduces d42b4's anchors "
       "(32 depth-2 sequences, Z_seq = 4, Z_class = 3, one mu per class)",
       len(_seqs) == D42B4_NSEQ and _Zseq == D42B4_ZSEQ
       and _Zclass == D42B4_ZCLASS and _gauge_single,
       f"sequences = {len(_seqs)}, Z_seq = {_Zseq}, classes = {len(_cls)}, "
       f"Z_class = {_Zclass}, one-mu-per-class = {_gauge_single}")

if ANCHOR_FAIL:
    print()
    print("!" * 78)
    print("ANCHOR FAILURE — a committed object did not reproduce.  STOPPING.")
    print("!" * 78)
    sys.exit(1)


# ===========================================================================
# SEC 2.  THE GENERATED LINE, enumerated (grammar 1, depth <= 5)
# ===========================================================================

print()
print("-" * 78)
print("SEC 2  the generated line, enumerated")
print("-" * 78)

DEPTH = int(os.environ.get("D72_DEPTH", "5"))


def enumerate_line(cands, actors, depth):
    fam = [[]]
    frontier = [[]]
    cache = {}
    while frontier:
        h = frontier.pop()
        c = cands(h, actors)
        cache[tuple(h)] = c
        if len(h) >= depth:
            continue
        for e, q in c:
            fam.append(h + [e])
            frontier.append(h + [e])
    return fam, cache


FAM, CAND = enumerate_line(b3_candidates, AB, DEPTH)
CLASS = {tuple(h): b3_canon(h) for h in FAM}
BYCLASS = {}
for h in FAM:
    BYCLASS.setdefault(CLASS[tuple(h)], []).append(h)
report("grammar 1 (d42b3 placement) depth<=%d" % DEPTH,
       f"{len(FAM)} histories, {len(BYCLASS)} record classes, "
       f"per-depth histories = "
       f"{dict(sorted(Counter(len(h) for h in FAM).items()))}")
report("record classes per depth",
       dict(sorted(Counter(len(v[0]) for v in BYCLASS.values()).items())))


# ===========================================================================
# SEC 3.  T1 — THE REVERSAL TEST
#
#  The two reversals, and the carrier problem, stated before anything is
#  computed:
#
#   R1  (v6 p4 sec.34)  AB -> BA : swap the ORDER OF APPLICATION of two
#       co-admissible transports at a common base.  Domain: triples
#       (h; e_A, e_B).  A_D(h;A,B) = log [ q(e_A|h)q(e_B|h e_A) ]
#                                       / [ q(e_B|h)q(e_A|h e_B) ].
#       This is EXACTLY v6's flatten_law(K_A K_B)/flatten_law(K_B K_A)
#       read at the single (start,end) atom the generated line offers:
#       start = h, end = the two-step extension.  Verified against v6's
#       own rn_action/exchange_laws in SEC 3.0.
#
#   R2  (v7 p30:2511)   *      : reverse EVERY ORDER RELATION of a record
#       type.  Domain: records (labelled posets), here canon(h) with the
#       causal order event_poset(h).
#
#  These have different domains.  Constructing a common carrier IS the
#  unit's hard part.  Three carriers are constructed and all three are run.
# ===========================================================================

print()
print("-" * 78)
print("SEC 3  T1 — THE REVERSAL TEST")
print("-" * 78)


def dual_pred(pred):
    n = len(pred)
    out = [set() for _ in range(n)]
    for j in range(n):
        for i in pred[j]:
            out[i].add(j)
    return out


def linexts(pred):
    n = len(pred)
    out = []
    for perm in permutations(range(n)):
        inv = {e: i for i, e in enumerate(perm)}
        if all(inv[i] < inv[j] for j in range(n) for i in pred[j]):
            out.append(perm)
    return out


# --- 3.0  the A_D operationalisation, held against v6's own code -----------
# v6 forms A_D as rn_action(flatten_law(K_A K_B), flatten_law(K_B K_A)).
# On the generated line the analogue at base h is the two-step path law.
# GATE: build a 2x2 toy from v10-shaped rational step weights, push it
# through v6's OWN exchange_laws/rn_action, and require our Fraction ratio
# to agree with v6's float A_D on the corresponding atom.
def AD_ratio(h, eA, eB):
    """EXACT Fraction dP_AB/dP_BA, or None if the square does not close."""
    okA, qA = b3_admissible(h, eA)
    okB, qB = b3_admissible(h, eB)
    if not (okA and okB):
        return None, None
    okB2, qB2 = b3_admissible(h + [eA], eB)
    okA2, qA2 = b3_admissible(h + [eB], eA)
    if okB2 and okA2:
        return Fr(qA * qB2, 1) / Fr(qB * qA2, 1), "closed"
    if okB2 and not okA2:
        return None, "AB-only"
    if okA2 and not okB2:
        return None, "BA-only"
    return None, "both-blocked"


_KA = [[Fr(1, 4), Fr(3, 4)], [Fr(2, 3), Fr(1, 3)]]
_KB = [[Fr(1, 2), Fr(1, 2)], [Fr(1, 5), Fr(4, 5)]]


def _mm(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2)]
            for i in range(2)]


_ab = _mm(_KA, _KB)
_ba = _mm(_KB, _KA)
_exact_AD = [_ab[i][j] / _ba[i][j] for i in range(2) for j in range(2)]
_v6_AD = P4N["rn_action"](
    P4N["flatten_law"]([[float(x) for x in r] for r in _ab]),
    P4N["flatten_law"]([[float(x) for x in r] for r in _ba]))
_agree = max(abs(math.log(float(r)) - a) for r, a in zip(_exact_AD, _v6_AD))
check("T1.0 OPERATIONALISATION FIDELITY: our exact Fraction "
      "dP_AB/dP_BA agrees with v6's own rn_action(exchange_laws(.)) on a "
      "rational 2x2 control, atom by atom",
      _agree < 1e-14,
      f"max |log(exact ratio) - v6 float A_D| = {_agree:.3e} over 4 atoms; "
      "the 1/n uniform-start factor of flatten_law cancels in the ratio "
      "(verified: it is the same constant on both laws)")

# --- 3.1  the census of exchange squares on the generated line -------------
sq = Counter()
ratios = Counter()
nonunit = []
open_pairs = 0
for h in FAM:
    if len(h) + 2 > DEPTH:
        continue
    cands = [e for e, q in CAND[tuple(h)]]
    for i in range(len(cands)):
        for j in range(i + 1, len(cands)):
            eA, eB = cands[i], cands[j]
            r, status = AD_ratio(h, eA, eB)
            sq[status] += 1
            if status == "closed":
                open_pairs += 1
                ratios[r] += 1
                if r != 1:
                    nonunit.append((h, eA, eB, r))
report("exchange-square census (grammar 1, bases |h|<=%d, depth<=%d)"
       % (DEPTH - 2, DEPTH), dict(sq))
report("distinct exact ratios dP_AB/dP_BA (bases |h|<=%d)" % (DEPTH - 2),
       dict(ratios))

# --- 3.1b  THE WIDER WINDOW (round MODERATE 3) and the L2/L4 SPLIT ---------
# AD_ratio calls only admissible(), which needs no enumeration: squares at
# bases |h| = 4, 5 are computable from the SAME depth-5 family and reach
# depth 6 and 7.  The same pass also splits every closed square by the L2
# criterion (comparability = register overlap, regs_of) and records whether
# a comparable square contains an idle event — the two facts the round's
# APPENDIX theorem needs (SEC 4C).
_t = time.time()
wide_status = defaultdict(Counter)
wide_ratios = Counter()
wide_nonunit = 0
L3_by_base = Counter()
L4_by_base = Counter()
L3_viol = 0
L4_noidle = 0
for h in FAM:
    cands = [e for e, q in CAND[tuple(h)]]
    for i in range(len(cands)):
        for j in range(i + 1, len(cands)):
            eA, eB = cands[i], cands[j]
            okA, qA = b3_admissible(h, eA)
            okB, qB = b3_admissible(h, eB)
            if not (okA and okB):
                continue
            okB2, qB2 = b3_admissible(h + [eA], eB)
            okA2, qA2 = b3_admissible(h + [eB], eA)
            if okB2 and okA2:
                st = "closed"
                r = Fr(qA * qB2, 1) / Fr(qB * qA2, 1)
                wide_ratios[r] += 1
                wide_nonunit += int(r != 1)
                if b3_regs(eA) & b3_regs(eB):
                    L4_by_base[len(h)] += 1
                    L4_noidle += int(eA[0] != 'n' and eB[0] != 'n')
                else:
                    L3_by_base[len(h)] += 1
                    # L3's content, gated: the OTHER event's weight is
                    # unchanged by the interposed disjoint event
                    L3_viol += int(qB2 != qB or qA2 != qA)
            elif okB2:
                st = "AB-only"
            elif okA2:
                st = "BA-only"
            else:
                st = "both-blocked"
            wide_status[len(h)][st] += 1
report("WIDE exchange-square census, grammar 1 (A,B), bases |h| = 0..%d "
       "(reaching depth %d)" % (DEPTH, DEPTH + 2),
       {b: dict(c) for b, c in sorted(wide_status.items())})
report("WIDE ratio multiset dP_AB/dP_BA over every base",
       f"{ {str(k): v for k, v in sorted(wide_ratios.items())} }  "
       f"[{time.time()-_t:.0f}s]")
L3_disjoint = sum(L3_by_base.values())
L4_comparable = sum(L4_by_base.values())
report("closed squares split by the L2 criterion (comparability = register "
       "overlap): register-DISJOINT (the locality argument's domain) vs "
       "register-OVERLAPPING (not covered by it), per base |h|",
       {b: (L3_by_base[b], L4_by_base[b])
        for b in sorted(set(L3_by_base) | set(L4_by_base))})
report("the first delivery's own licensed window (bases |h| <= %d)"
       % (DEPTH - 2),
       f"disjoint {sum(L3_by_base[b] for b in range(DEPTH - 1))} / "
       f"comparable {sum(L4_by_base[b] for b in range(DEPTH - 1))} "
       f"of {open_pairs} closed squares — the locality sketch covers the "
       f"first number only")

check("T1.1 A_D CONTENT (grammar 1, WIDENED): every closed exchange square "
      "of the d42b3 placement line has dP_AB/dP_BA EXACTLY 1 — at every "
      f"base |h| = 0..{DEPTH}, i.e. up to total depth {DEPTH+2}, not only "
      "on the bases the first delivery licensed.  On THIS grammar the "
      "transport reversal AB->BA has no content",
      wide_nonunit == 0 and sum(wide_ratios.values()) > 0
      and set(wide_ratios) == {Fr(1)},
      f"{sum(wide_ratios.values())} closed squares over all bases "
      f"(vs {open_pairs} in the first delivery's window), "
      f"{wide_nonunit} with ratio != 1; "
      f"ratio multiset = {{1: {wide_ratios[Fr(1)]}}}.  SCOPE: this is a "
      "GRAMMAR-1 statement — see T6.1, where it is FALSE")

check("T1.2 NO HALF-OPEN SQUARE IN GRAMMAR 1: there is no pair whose AB "
      "order is admissible while BA is not (a half-open square would make "
      "A_D +/-infinity — a support-level, non-U(1) and non-R+ defect).  "
      "GRAMMAR-1 ONLY: T6.2 exhibits 40 of them in grammar 2",
      all(c["AB-only"] == 0 and c["BA-only"] == 0
          for c in wide_status.values()),
      f"over all bases: AB-only = {sum(c['AB-only'] for c in wide_status.values())}, "
      f"BA-only = {sum(c['BA-only'] for c in wide_status.values())}, "
      f"both-blocked = {sum(c['both-blocked'] for c in wide_status.values())}")

# --- 3.2  CARRIER A: the linear-extension carrier --------------------------
# The order-dual * of a record induces on its linear extensions the map
# "reverse the sequence".  This is the only canonical lift of * from
# records to the sequences A_D is defined on.  GATE it, do not assume it.
_bij_ok = True
_bij_n = 0
for h in FAM:
    if len(h) < 2:
        continue
    pred = b3_poset(h)
    L = set(linexts(pred))
    Dl = set(linexts(dual_pred(pred)))
    _bij_n += 1
    if {tuple(reversed(p)) for p in L} != Dl:
        _bij_ok = False
        break
check("T1.3 CARRIER A is well-founded: sequence reversal is exactly the "
      "action induced by the order-dual * on linear extensions "
      "(rev : LinExt(P) -> LinExt(P*) is a bijection, checked on every "
      "history of the generated line)",
      _bij_ok, f"{_bij_n} histories, all depths 2..{DEPTH}",
      corollary_of="a one-line theorem true of EVERY finite poset — sigma "
      "is a linear extension of P iff reversed(sigma) is one of P* — so "
      "this sweep tests this receipt's implementation of dual_pred/linexts, "
      "not the generated family")

# On CARRIER A, at base h = [] with a two-event history, *_seq IS AB->BA.
_two = [h for h in FAM if len(h) == 2]
_coincide = all(list(reversed(h)) == [h[1], h[0]] for h in _two)
_rev_adm_2 = sum(1 for h in _two if b3_mu(list(reversed(h))) is not None)
check("T1.4 THE COINCIDENCE, and its exact extent: on 2-event histories "
      "(the F-PAIR fixture, base h = []) the induced order-dual *_seq and "
      "the transport reversal AB->BA are the SAME partial map — "
      "literally, term by term",
      _coincide and len(_two) == D42B4_NSEQ,
      f"{len(_two)} two-event histories = d42b4's 32; "
      f"{_rev_adm_2} have an admissible reverse")

# and where they diverge: count the (h; e_A, e_B) triples with |h| >= 1 on
# which *_seq (whole-sequence reversal) and AB->BA (top transposition) give
# literally different sequences.
_div = 0
_div_adm = 0
_div_same = 0
for h in FAM:
    if len(h) < 1 or len(h) + 2 > DEPTH:
        continue
    cands = [e for e, q in CAND[tuple(h)]]
    for i in range(len(cands)):
        for j in range(i + 1, len(cands)):
            eA, eB = cands[i], cands[j]
            r, st = AD_ratio(h, eA, eB)
            if st != "closed":
                continue
            full = h + [eA, eB]
            star_seq = list(reversed(full))
            swap = h + [eB, eA]
            _div += 1
            if star_seq == swap:
                _div_same += 1
            if b3_mu(star_seq) is not None:
                _div_adm += 1
check("T1.5 THE DIVERGENCE: on every closed square with a non-empty base "
      "(|h| >= 1 under the pair), *_seq reverses the WHOLE sequence while "
      "AB->BA transposes only the top two — the two maps give different "
      "sequences wherever there is anything below the pair",
      _div > 0 and _div_same == 0,
      f"{_div} closed squares with |h| >= 1; {_div_same} on which the two "
      f"maps agree; {_div_adm} whose *_seq image is itself admissible "
      "(so *_seq has a domain there, but it is not AB->BA)")

# --- 3.3  the oddness gate, on CARRIER A -----------------------------------
_odd_ok = True
_odd_n = 0
for h in FAM:
    if len(h) + 2 > DEPTH:
        continue
    cands = [e for e, q in CAND[tuple(h)]]
    for i in range(len(cands)):
        for j in range(i + 1, len(cands)):
            r, st = AD_ratio(h, cands[i], cands[j])
            if st != "closed":
                continue
            rp, stp = AD_ratio(h, cands[j], cands[i])
            _odd_n += 1
            if stp != "closed" or rp != 1 / r:
                _odd_ok = False
check("T1.6 ODDNESS UNDER AB->BA (v6's antisymmetry row, exact): "
      "dP_BA/dP_AB = (dP_AB/dP_BA)^-1 as Fractions, hence A_D -> -A_D, "
      "on every closed square — v6:2636's gap=2.2e-16 reproduced at gap "
      "EXACTLY 0 in exact arithmetic",
      _odd_ok and _odd_n > 0, f"{_odd_n} squares, exact inverse in all")

check("T1.7 ODDNESS UNDER * (the pin's actual question): A_D is odd under "
      "the order-dual on CARRIER A — but ONLY because A_D == 0, so the "
      "test reads 0 = -0.  The identity is CONFIRMED VACUOUSLY: it holds "
      "with zero content, on the one fixture (2-event, base []) where the "
      "two reversals are the same map",
      set(ratios) == {Fr(1)},
      "A_D == 0 on all %d closed squares; oddness is the identity 0 = -0"
      % open_pairs,
      corollary_of="T1.1 — the predicate set(ratios) == {1} is literally "
      "T1.1's own predicate")

# --- 3.4  CARRIER B: the record carrier ------------------------------------
# Does A_D descend to records?  It does — as the zero function, because
# gauge-equivalent sequences carry equal mu.  Then * acts on records, but
# A_D is identically 0 there, so * has nothing to act on.
_mu_gauge_ok = True
_mu_n = 0
for C, hs in BYCLASS.items():
    vals = {b3_mu(h) for h in hs}
    _mu_n += 1
    if len(vals) != 1:
        _mu_gauge_ok = False
check("T1.8 CARRIER B (record-level): mu is constant on every record "
      "class of the generated line, so A_D descends to records — as the "
      "ZERO function.  * acts on records; A_D-on-records is 0; the "
      "carrier exists and carries nothing",
      _mu_gauge_ok, f"{_mu_n} record classes, one mu each")

# --- 3.5  CARRIER C: is the family *-closed at all? ------------------------
_DR_CACHE = {}


def dual_realised(h):
    """Is the LABELLED order-dual of this record itself a generated record?
    (Round MODERATE 2: this is the labelled question — the same multiset of
    events, re-ordered.  The order-TYPE question is T3's, and its answer is
    k-dependent and partly opposite.)"""
    _ck = b3_canon(h)
    if _ck in _DR_CACHE:
        return _DR_CACHE[_ck]
    _DR_CACHE[_ck] = _dual_realised_uncached(h)
    return _DR_CACHE[_ck]


def _dual_realised_uncached(h):
    n = len(h)
    pred = b3_poset(h)
    dp = dual_pred(pred)
    target = {(a, b) for b in range(n) for a in dp[b]}
    for perm in linexts(dp):
        cand = [h[perm[i]] for i in range(n)]
        if b3_mu(cand) is None:
            continue
        p2 = b3_poset(cand)
        got = {(perm[a], perm[b]) for b in range(n) for a in p2[b]}
        if got == target:
            return True
    return False


dual_cens = Counter()
for C, hs in BYCLASS.items():
    h = hs[0]
    if len(h) < 2:
        continue
    dual_cens[(len(h), dual_realised(h))] += 1
report("record order-dual realised inside the generated line",
       dict(sorted(dual_cens.items())))
_dr_yes = sum(v for k, v in dual_cens.items() if k[1])
_dr_no = sum(v for k, v in dual_cens.items() if not k[1])
check("T1.9 CARRIER C: the generated line is NOT closed under the LABELLED "
      "order-dual — a majority of its records have no dual inside the "
      "family, so * is a PARTIAL map on v10's objects, not an operation on "
      "them.  LABELLED is load-bearing (round MODERATE 2): this asks "
      "whether the SAME MULTISET OF EVENTS, re-ordered, realises the dual "
      "order.  The ORDER-TYPE question is different and k-dependent, and "
      "T3 answers it separately (k=3: 0/1 odd orbits with an absent dual "
      "member; k=4: 1/2; k=5: 4/4)",
      _dr_no > 0,
      f"{_dr_yes} records have their labelled order-dual in-family; "
      f"{_dr_no} do not")

print()
print("  T1 VERDICT — see SEC 6 falsifier board.  In one line: the two "
      "reversals do")
print("  admit a common carrier (CARRIER A, gated at T1.3), they coincide "
      "exactly")
print("  on the F-PAIR fixture (T1.4) and diverge everywhere else (T1.5), "
      "and on")
print("  the carrier A_D is identically zero (T1.1), so 'is A_D odd under "
      "*' is")
print("  answered YES with zero content (T1.7).")


# ===========================================================================
# SEC 4.  T2 — THE CLOSURE TEST
#
#  The pin: prod sqrt(q) transported around delete-then-insert round trips
#  of the record deletion graph.  Built from the generated layer's OWN
#  operations: an UP move is "insert an admissible event e at a history h"
#  and carries the layer's own step weight q(e|h); the DOWN move is its
#  reverse.  Nodes are RECORDS (canonical classes), because it is only the
#  record identification that creates any cycle at all — the sequence
#  extension graph is a tree (each history has a unique prefix parent), so
#  H^1 of the sequence layer is zero for trivial reasons, exactly as
#  v8 p1:77 says of a commit path.  The transverse loops are therefore
#  precisely the incomparable-pair exchanges and their concatenations.
# ===========================================================================

print()
print("-" * 78)
print("SEC 4  T2 — THE CLOSURE TEST")
print("-" * 78)


def stable_key(o):
    """A hash-order-independent total key for the nested frozenset/tuple
    record classes.  `repr` of a frozenset depends on insertion order and
    therefore on PYTHONHASHSEED; this does not."""
    if isinstance(o, (frozenset, set)):
        return ("S", tuple(sorted(stable_key(x) for x in o)))
    if isinstance(o, (tuple, list)):
        return ("T", tuple(stable_key(x) for x in o))
    return ("V", type(o).__name__ + "|" + repr(o))


def build_edges(fam, cache, canon_f, depth):
    """Up-edges of the record deletion graph, with the layer's own step
    weights.  A key with more than one weight means the connection does not
    descend from sequences to records."""
    edgew = defaultdict(set)
    for h in fam:
        if len(h) >= depth:
            continue
        C = canon_f(h)
        for e, q in cache[tuple(h)]:
            edgew[(C, canon_f(h + [e]))].add(Fr(q))
    return edgew


def holonomy_of(edgew, reverse_order=False, tamper=None):
    """Exact holonomy census by spanning-forest potentials.  Every
    independent cycle (rank = E - V + C) is tested; the holonomy of a cycle
    is a product of step weights and their inverses, hence an exact
    Fraction.  `tamper` multiplies the weight of one named edge — the
    negative control."""
    nodes = set()
    for a, b in edgew:
        nodes.add(a)
        nodes.add(b)
    parent = {x: x for x in nodes}
    pot = {x: Fr(1) for x in nodes}

    def find(x):
        f = Fr(1)
        y = x
        while parent[y] != y:
            f *= pot[y]
            y = parent[y]
        return y, f

    rank = 0
    defects = []
    hol_values = set()
    keys = sorted(edgew, key=stable_key, reverse=reverse_order)
    for k in keys:
        for w in sorted(edgew[k], reverse=reverse_order):
            if tamper is not None and k == tamper[0] and w == tamper[1]:
                w = w * tamper[2]
            C, C2 = k
            rC, fC = find(C)
            rC2, fC2 = find(C2)
            if rC == rC2:
                rank += 1
                hol = (fC * w) / fC2
                hol_values.add(hol)
                if hol != 1:
                    defects.append((k, w, hol))
            else:
                parent[rC2] = rC
                pot[rC2] = (fC * w) / fC2
    return len(nodes), rank, defects, hol_values


def deletion_graph_holonomy(fam, cache, canon_f, depth, label):
    edgew = build_edges(fam, cache, canon_f, depth)
    multi = [k for k, v in edgew.items() if len(v) > 1]
    nn, rank, defects, hols = holonomy_of(edgew)
    worst = max((abs(math.log(float(d[2]))) for d in defects), default=0.0)
    report(f"{label}: deletion graph",
           f"nodes = {nn}, up-edges = {len(edgew)}, "
           f"multi-valued edges = {len(multi)}, independent cycles = "
           f"{rank}, non-trivial holonomies = {len(defects)}, "
           f"holonomy value set = {sorted(hols) if len(hols) < 6 else '...'}")
    return nn, len(edgew), len(multi), rank, defects, worst, edgew


n1, e1, m1, r1, d1, w1, EW1 = deletion_graph_holonomy(
    FAM, CAND, b3_canon, DEPTH, "grammar 1 (d42b3), depth<=%d" % DEPTH)

# --- T2.0  THE POTENTIAL IDENTITY (round MAJOR 3) --------------------------
# mu(h.e) = mu(h) q(e|h) BY DEFINITION (mu_of, d42b3:251).  So if mu is
# constant on record classes (T1.8) then phi(C) := mu(C) is a well-defined
# NODE POTENTIAL and every up-edge weight is phi(C2)/phi(C1).  That single
# identity forces T2.1 (parallel edges agree), T2.2 (ratios telescope
# around any cycle), T2.3, T2.5 and T2.NC with no census at all.  Gate the
# identity here, and label those five as corollaries rather than as five
# independent measurements.
_phi = {C: b3_mu(hs[0]) for C, hs in BYCLASS.items()}
_pot_ok = 0
_pot_bad = 0
for (C1, C2), ws in EW1.items():
    for w in ws:
        if _phi[C1] is not None and _phi[C2] is not None \
                and w == Fr(_phi[C2]) / Fr(_phi[C1]):
            _pot_ok += 1
        else:
            _pot_bad += 1
check("T2.0 THE CONNECTION IS AN EXACT GRADIENT: every up-edge weight is "
      "phi(C2)/phi(C1) with phi = mu, the record-class weight of T1.8.  "
      "This is the whole of T2: single-valuedness, cycle-triviality and "
      "the three arms are ALGEBRAICALLY FORCED by T1.8, and the negative "
      "control CANNOT fail.  The instrument's blind spot follows too — a "
      "gradient-flat record graph says nothing about squares whose two "
      "orders land in DIFFERENT classes (see T6.3)",
      _pot_bad == 0 and _pot_ok > 0,
      f"{_pot_ok}/{_pot_ok + _pot_bad} up-edge weights equal the mu-ratio "
      f"exactly; {_pot_bad} exceptions")

check("T2.1 THE CONNECTION DESCENDS: every up-edge of the record deletion "
      "graph carries a SINGLE step weight — the sqrt(q) connection is "
      "well defined on records, not merely on sequences",
      m1 == 0, f"{e1} up-edges, {m1} multi-valued",
      corollary_of="T2.0 (hence T1.8): parallel up-edges C1->C2 both equal "
      "phi(C2)/phi(C1)")

check("T2.2 THE ROUND TRIP CLOSES AT 1, EXACTLY, ON EVERY INDEPENDENT "
      "CYCLE: the modulus returns to its start and the accumulated log is "
      "0 = A_D on every loop (T1.1).  This is the pin's F2 condition, and "
      "the cycle rank shows the test is NOT vacuous",
      len(d1) == 0 and r1 > 0,
      f"{r1} independent cycles (E - V + C), {len(d1)} with holonomy != 1, "
      f"worst |log holonomy| = {w1}",
      corollary_of="T2.0 (hence T1.8): a product of phi-ratios telescopes "
      "around any cycle.  The 758 cycles are not 758 independent facts")

# explicit delete-then-insert round trips (the transverse loops named in
# the pin's parent: incomparable-pair exchanges ARE the transverse loops)
sq_loops = 0
sq_hol_nonunit = 0
sq_seen_disjoint = sq_seen_comparable = 0
sq_all_disjoint = sq_all_comparable = 0
for h in FAM:
    if len(h) + 2 > DEPTH:
        continue
    cands = [e for e, q in CAND[tuple(h)]]
    for i in range(len(cands)):
        for j in range(i + 1, len(cands)):
            eA, eB = cands[i], cands[j]
            r, st = AD_ratio(h, eA, eB)
            if st != "closed":
                continue
            _ovl = bool(b3_regs(eA) & b3_regs(eB))
            sq_all_comparable += int(_ovl)
            sq_all_disjoint += int(not _ovl)
            if b3_canon(h + [eA, eB]) != b3_canon(h + [eB, eA]):
                continue      # not a closed loop in the record graph
            sq_loops += 1
            sq_seen_comparable += int(_ovl)
            sq_seen_disjoint += int(not _ovl)
            if r != 1:
                sq_hol_nonunit += 1
check("T2.3 THE EXPLICIT DELETE-THEN-INSERT ROUND TRIPS (the transverse "
      "loops: h.eA.eB -> h.eB -> h.eB.eA -> h.eA -> h.eA.eB).  sqrt(q)-"
      "transport around each gives sqrt(dP_AB/dP_BA) = 1 exactly, and "
      "2*log of it equals A_D = 0",
      sq_hol_nonunit == 0 and sq_loops > 0,
      f"{sq_loops} record-closing exchange loops, {sq_hol_nonunit} with "
      "holonomy != 1",
      corollary_of="T1.1 and T2.0.  Note what it counts: only the "
      f"{sq_loops} squares that CLOSE at record level, out of "
      f"{open_pairs} closed squares in the same window — the other "
      f"{open_pairs - sq_loops} are invisible to any record-graph loop "
      "test (T6.3)")

check("T2.3b WHAT THE RECORD-GRAPH INSTRUMENT CAN SEE AT ALL: a square "
      "closes at record level EXACTLY WHEN its two events are register-"
      "disjoint.  So the loop census and the locality argument have the "
      "SAME domain, and the register-overlapping squares — the ones the "
      "locality argument does not cover — are invisible to it.  Two "
      "arguments with one blind spot; only the raw square census (T1.1) "
      "decides them, and in grammar 2 that is exactly where the defect "
      "lives (T6.3)",
      sq_seen_comparable == 0 and sq_seen_disjoint == sq_all_disjoint
      and sq_all_comparable > 0,
      f"of {open_pairs} closed squares in the licensed window, "
      f"{sq_all_disjoint} are register-disjoint and {sq_all_comparable} "
      f"are overlapping; the record graph closes on {sq_seen_disjoint} of "
      f"the first and {sq_seen_comparable} of the second")

# NEGATIVE CONTROL — the instrument must be able to see a defect.
_stable_edges = sorted(EW1, key=stable_key)
_tamper_rows = []
for k in _stable_edges[:20]:
    _nn, _rk, _df, _hl = holonomy_of(
        EW1, tamper=(k, sorted(EW1[k])[0], Fr(3, 2)))
    _tamper_rows.append((len(_df), sorted({h for h in _hl if h != 1})))
_tamper_hits = [r for r in _tamper_rows if r[0] > 0]
check("T2.NC NEGATIVE CONTROL: multiplying ONE up-edge weight by 3/2 makes "
      "the same detector report a non-trivial holonomy — so the zero above "
      "is a measurement, not a blind instrument.  Twenty edges are tampered "
      "one at a time, in a HASH-ORDER-INDEPENDENT order (stable_key), and "
      "the census is reported rather than the first hit",
      len(_tamper_hits) > 0,
      f"{len(_tamper_hits)}/20 tampered edges produce a non-trivial "
      f"holonomy; defect counts = {[r[0] for r in _tamper_rows]}; "
      f"first non-trivial value set = "
      f"{_tamper_hits[0][1][:3] if _tamper_hits else None}",
      corollary_of="T2.0: multiplying one edge of an EXACT GRADIENT by 3/2 "
      "must produce a defect, so this control cannot fail and its passing "
      "is not evidence of sensitivity.  A control that CAN fail is T6 — "
      "grammar 2 now supplies a substrate with a genuine defect, and the "
      "record-graph instrument does NOT see it (T6.3)")

check("T2.4 U(1) CONTENT OF THE RAW CONNECTION: the round-trip defect of "
      "the UN-NORMALISED budget weight is not merely real-positive rather "
      "than unimodular (falsifier F4's shape) — there is no defect at all. "
      "The holonomy group of sqrt(q)-transport on the generated line's "
      "record deletion graph is the TRIVIAL group FOR THE RAW WEIGHT.  "
      "WEIGHT CHOICE IS LOAD-BEARING (round MAJOR 2): for the process's "
      "own conditional kernel q/M the same graph has NON-TRIVIAL holonomy "
      "(T4.3), and that is where F4 fires",
      len(d1) == 0,
      "raw holonomy group = {1}; neither R+ nor U(1) is realised by the "
      "raw weight, because nothing but 1 is realised",
      corollary_of="T2.2, whose predicate len(d1) == 0 this repeats")

# ===========================================================================
# SEC 4B.  T6 — THE TRANSPORT SCOPE (the round's MAJOR 1)
#
#  The first delivery ran ONLY deletion_graph_holonomy on grammar 2 and
#  then asserted, as [MEASURED], that every closed exchange square there
#  has ratio 1.  It never computed one.  Here the square census is run on
#  the same layer, the same actor pools and the same depths — and A_D is
#  NOT zero.  The two facts are reported side by side deliberately: the
#  record-graph census (T2.5) is flat and the square census (T6.1) is not,
#  because they are not the same test (T6.3).
# ===========================================================================
b1_cand = B1["candidates_for"]
b1_canon = B1["canon"]
b1_adm = B1["admissible"]
b1_regs = B1["regs_of"]


def mu_map(fam, cache):
    """mu(h) = product of the layer's own step weights along h, built
    incrementally from the parent's cached candidate weight."""
    mu = {(): Fr(1)}
    for h in sorted(fam, key=len):
        if not h:
            continue
        par = tuple(h[:-1])
        qs = [q for ee, q in cache[par] if ee == h[-1]]
        mu[tuple(h)] = mu[par] * Fr(qs[0])
    return mu


def transport_square_census(fam, cache, actors, dep, canon_f):
    """The exchange-square census in grammar 2, with its kinds, its
    record-level closure and its minimal witness."""
    st = Counter()
    rat = Counter()
    kinds = Counter()
    open_kinds = Counter()
    defects = []
    half = []
    for h in fam:
        if len(h) + 2 > dep:
            continue
        cands = [e for e, q in cache[tuple(h)]]
        for i in range(len(cands)):
            for j in range(i + 1, len(cands)):
                eA, eB = cands[i], cands[j]
                okA, qA = b1_adm(h, eA, actors)
                okB, qB = b1_adm(h, eB, actors)
                if not (okA and okB):
                    continue
                okB2, qB2 = b1_adm(h + [eA], eB, actors)
                okA2, qA2 = b1_adm(h + [eB], eA, actors)
                if okB2 and okA2:
                    st["closed"] += 1
                    r = Fr(qA * qB2, 1) / Fr(qB * qA2, 1)
                    rat[r] += 1
                    if r != 1:
                        kinds[(eA[0], eB[0])] += 1
                        defects.append((h, eA, eB, r, qA, qB2, qB, qA2))
                elif okB2:
                    st["AB-only"] += 1
                    open_kinds[(eA[0], eB[0])] += 1
                    half.append((h, eA, eB, "AB-only"))
                elif okA2:
                    st["BA-only"] += 1
                    open_kinds[(eA[0], eB[0])] += 1
                    half.append((h, eA, eB, "BA-only"))
                else:
                    st["both-blocked"] += 1
    return st, rat, kinds, open_kinds, defects, half


TRANSPORT_DEFECTS = 0        # non-unit closed squares, grammar 2, all arms
TRANSPORT_CLOSED = 0
TRANSPORT_HALFOPEN = 0
TRANSPORT_RECORD_CLOSES = 0  # of the defects, how many the record graph sees
TRANSPORT_SPECTRUM = Counter()

for _actors, _dep in ((("A", "B"), 4), (("A", "B", "C"), 3)):
    _t = time.time()
    _fam, _cache = enumerate_line(b1_cand, _actors, _dep)
    _n, _e, _m, _r, _d, _w, _ew = deletion_graph_holonomy(
        _fam, _cache, b1_canon, _dep,
        f"grammar 2 (d42b1) {_actors} depth<={_dep}")
    _mu = mu_map(_fam, _cache)
    _mucls = defaultdict(set)
    for _h in _fam:
        _mucls[b1_canon(_h)].add(_mu[tuple(_h)])
    _mu_const = sum(1 for v in _mucls.values() if len(v) == 1)
    check(f"T2.5 SECOND GRAMMAR {_actors} depth<={_dep}, RECORD-GRAPH ARM: "
          "connection descends, every independent cycle has holonomy "
          "exactly 1 — AND THIS ARM IS BLIND (see T6.3).  mu is class-"
          "constant here too, so the grammar-2 record graph is an exact "
          "gradient for the same reason grammar 1's is",
          _m == 0 and len(_d) == 0 and _r > 0,
          f"{_r} independent cycles, {len(_d)} defects, {len(_fam)} "
          f"histories; mu class-constant on {_mu_const}/{len(_mucls)} "
          "classes",
          corollary_of="the same potential identity as T2.0, now verified "
          "in grammar 2: a gradient record graph is flat by algebra and "
          "cannot report a square defect whose two orders land in "
          "different classes")

    _st, _rat, _kinds, _okinds, _defs, _half = transport_square_census(
        _fam, _cache, _actors, _dep, b1_canon)
    report(f"grammar 2 (d42b1) {_actors} depth<={_dep}: exchange-square "
           "census", dict(_st))
    report(f"grammar 2 {_actors}: exact ratios dP_AB/dP_BA",
           {str(k): v for k, v in sorted(_rat.items())})
    _closes = sum(1 for h, eA, eB, r, *_ in _defs
                  if b1_canon(h + [eA, eB]) == b1_canon(h + [eB, eA]))
    _dely = sum(1 for h, eA, eB, r, *_ in _defs if 'd' in (eA[0], eB[0]))
    _dely_h = sum(1 for h, eA, eB, k in _half if 'd' in (eA[0], eB[0]))
    _mindepth = min((len(h) + 2 for h, *_ in _defs), default=None)
    TRANSPORT_DEFECTS += len(_defs)
    TRANSPORT_CLOSED += _st["closed"]
    TRANSPORT_HALFOPEN += _st["AB-only"] + _st["BA-only"]
    TRANSPORT_RECORD_CLOSES += _closes
    for _k_, _v_ in _rat.items():
        if _k_ != 1:
            TRANSPORT_SPECTRUM[_k_] += _v_

    check(f"T6.1 A_D IS NOT ZERO AT TRANSPORT SCOPE {_actors} depth<="
          f"{_dep}: the d42b1 grammar — deliveries and multi-proposer "
          "arbitrations — has closed exchange squares with dP_AB/dP_BA "
          "!= 1.  The first delivery asserted the opposite on exactly "
          "this window as [MEASURED] and never computed it.  EVERY defect "
          "carries a DELIVERY event, and the defect appears at the "
          "shallowest depth the census can reach",
          len(_defs) > 0 and _dely == len(_defs),
          f"{len(_defs)} of {_st['closed']} closed squares have ratio != 1; "
          f"spectrum {{ {', '.join(f'{k}: {v}' for k, v in sorted(_rat.items()) if k != 1)} }}; "
          f"kinds {dict(_kinds)}; delivery-bearing {_dely}/{len(_defs)}; "
          f"shallowest defect at total depth {_mindepth}")

    check(f"T6.2 HALF-OPEN SQUARES AT TRANSPORT SCOPE {_actors} depth<="
          f"{_dep}: pairs admissible in one order only, i.e. A_D = "
          "+/-infinity — the support-level, non-U(1) and non-R+ defect "
          "T1.2 rules out in grammar 1 and the first delivery carried "
          "across both grammars",
          True,
          f"AB-only = {_st['AB-only']}, BA-only = {_st['BA-only']} "
          f"(total {_st['AB-only'] + _st['BA-only']}); kinds "
          f"{dict(_okinds)}; delivery-bearing {_dely_h}/"
          f"{len(_half)} — REPORTED, not gated as a pass/fail")

    check(f"T6.3 THE RECORD-GRAPH INSTRUMENT IS BLIND TO THEM BY "
          f"CONSTRUCTION {_actors}: none of the defective squares closes "
          "at record level, so T2.5's deletion-graph holonomy census — "
          "the only test the first delivery ran on this grammar — cannot "
          "see a single one of them.  T2.NC's negative control cannot "
          "detect this class of blindness either, because it perturbs an "
          "edge the graph does contain",
          len(_defs) > 0 and _closes == 0,
          f"{_closes}/{len(_defs)} defective squares close at record "
          f"level; the record graph carries {_r} independent cycles and "
          f"reports {len(_d)} defects")

    if _defs:
        _wit = min(_defs, key=lambda z: (len(z[0]), stable_key(
            (tuple(z[0]), z[1], z[2]))))
        _h, _eA, _eB, _r_, _qA, _qB2, _qB, _qA2 = _wit
        _muAB = _mu[tuple(_h)] * _qA * _qB2
        _muBA = _mu[tuple(_h)] * _qB * _qA2
        print(f"  [DATA] T6 WITNESS ({_actors}, minimal depth), in full:")
        print(f"           h   = {list(_h)}")
        print(f"           eA  = {_eA}")
        print(f"           eB  = {_eB}")
        print(f"           q(eA|h) = {_qA} , q(eB|h.eA) = {_qB2}  ->  "
              f"dP_AB = {Fr(_qA * _qB2)}")
        print(f"           q(eB|h) = {_qB} , q(eA|h.eB) = {_qA2}  ->  "
              f"dP_BA = {Fr(_qB * _qA2)}")
        print(f"           dP_AB/dP_BA = {_r_} ,  A_D = log({_r_}) != 0")
        print(f"           second route (whole-history weights): "
              f"mu(h.eA.eB) = {_muAB} vs mu(h.eB.eA) = {_muBA}, "
              f"ratio {Fr(_muAB) / Fr(_muBA)}")
        check(f"T6.4 WITNESS CROSS-ROUTE {_actors}: the minimal witness's "
              "ratio recomputed from whole-history weights (products along "
              "the two orders) agrees with the step-product route",
              Fr(_muAB) / Fr(_muBA) == _r_,
              f"route 1 = {_r_}, route 2 = {Fr(_muAB) / Fr(_muBA)}")
    report(f"grammar 2 {_actors} arm time", f"{time.time()-_t:.0f}s")

# --- the transport-scope idle budget: WHY grammar 2 is not flat ------------
_t = time.time()
_fam1, _cache1 = enumerate_line(b1_cand, ("A", "B"), 4)
_b1_idle = Counter()
for _h in _fam1:
    for _a in ("A", "B"):
        _ok, _q = b1_adm(_h, ('n', _a), ("A", "B"))
        if _ok:
            _b1_idle[_q] += 1
_b1_comp = _b1_noidle = 0
for _h in _fam1:
    if len(_h) + 2 > 4:
        continue
    _cs = [e for e, q in _cache1[tuple(_h)]]
    for _i in range(len(_cs)):
        for _j in range(_i + 1, len(_cs)):
            _eA, _eB = _cs[_i], _cs[_j]
            _o1, _ = b1_adm(_h, _eA, ("A", "B"))
            _o2, _ = b1_adm(_h, _eB, ("A", "B"))
            if not (_o1 and _o2):
                continue
            _o3, _ = b1_adm(_h + [_eA], _eB, ("A", "B"))
            _o4, _ = b1_adm(_h + [_eB], _eA, ("A", "B"))
            if not (_o3 and _o4):
                continue
            if b1_regs(_eA) & b1_regs(_eB):
                _b1_comp += 1
                _b1_noidle += int(_eA[0] != 'n' and _eB[0] != 'n')
check("T6.5 WHY GRAMMAR 2 IS NOT FLAT — the theorem's grammar-1 hypotheses "
      "FAIL here, exactly as the round's scope clause says.  (i) The idle "
      "weight is NOT the constant 3/4: the budget is a three-way split and "
      "the propose/arbitrate exclusivity is gone.  (ii) L4 fails outright: "
      "there are comparable closed squares with NO idle member — the (r,d) "
      "pairs by one actor that carry the defect",
      len(set(_b1_idle)) > 1 and _b1_noidle > 0,
      f"d42b1 (A,B) depth<=4 idle-weight spectrum = "
      f"{ {str(k): v for k, v in sorted(_b1_idle.items())} } "
      f"(grammar 1's is the single value 3/4, T5.L6); comparable closed "
      f"squares = {_b1_comp}, of which {_b1_noidle} contain no idle event "
      f"(grammar 1's count is 0, T5.L4)  [{time.time()-_t:.0f}s]")


# ===========================================================================
# SEC 4C.  T4 — THE NORMALISED KERNEL (the round's MAJOR 2)
#
#  Everything above transports the RAW step weight q(e|h).  The v10 step
#  weights are not conditional probabilities: the menu mass
#  M(h) = sum_e q(e|h) is not constant.  v6 p4 sec.34's A_D is defined for a
#  STOCHASTIC transport (v6's stochastic_transport builds row-stochastic
#  kernels), and this receipt's own fidelity control T1.0 uses row-stochastic
#  matrices — so normalisation is exactly the property the fidelity gate
#  cannot see.  The choice is therefore run BOTH WAYS here.
#
#  For the D42b4 lift specifically the raw weight remains the right object
#  (QUOTES['sqrtq'] says "the amplitude prod sqrt(q)"), so finding (b)'s
#  phase-slot corollary survives for that lift.  But "the generated line is
#  flat" is false for the process's own conditional kernel, and the defect
#  is D65's committed mass-ratio coboundary, quoted in QUOTES['d65'].
# ===========================================================================

print()
print("-" * 78)
print("SEC 4C  T4 — THE NORMALISED KERNEL (raw vs conditional)")
print("-" * 78)

_t = time.time()
MENU = {tuple(h): sum(q for e, q in CAND[tuple(h)]) for h in FAM}
_menu_spec = Counter(MENU.values())
_menu_cls = defaultdict(set)
for h in FAM:
    _menu_cls[CLASS[tuple(h)]].add(MENU[tuple(h)])
_menu_const = sum(1 for v in _menu_cls.values() if len(v) == 1)
report("menu mass M(h) = sum_e q(e|h), spectrum over the family",
       {str(k): v for k, v in sorted(_menu_spec.items())})
check("T4.1 THE MENU MASS IS NOT CONSTANT BUT IS CLASS-CONSTANT: the raw "
      "weights are not conditional probabilities (M != 1 and M is not even "
      "constant), so 'raw' and 'normalised' are different connections; and "
      "M is a function of the RECORD, so the normalised connection descends "
      "to records exactly as the raw one does.  ANCHOR: the two values are "
      "D65's own committed menu masses (QUOTES['d65']: 34 states of mass 2 "
      "and 2 states of mass 5/2)",
      len(_menu_spec) > 1 and _menu_const == len(_menu_cls)
      and set(_menu_spec) == D65_MASSES,
      f"M spectrum = { {str(k): v for k, v in sorted(_menu_spec.items())} }; "
      f"class-constant on {_menu_const}/{len(_menu_cls)} classes; value set "
      f"{sorted(str(x) for x in _menu_spec)} == D65's committed "
      f"{sorted(str(x) for x in D65_MASSES)}")

# normalised square ratios, by base.  p(e|h) = q(e|h)/M(h), so the
# normalised square ratio is (raw ratio) * M(h.eB)/M(h.eA).
_nrat = defaultdict(Counter)
_nident = _nident_bad = 0
for h in FAM:
    if len(h) + 1 > DEPTH:
        continue            # need h.eA and h.eB inside the enumerated family
    cands = [e for e, q in CAND[tuple(h)]]
    for i in range(len(cands)):
        for j in range(i + 1, len(cands)):
            eA, eB = cands[i], cands[j]
            r, st = AD_ratio(h, eA, eB)
            if st != "closed":
                continue
            nr = r * Fr(MENU[tuple(h + [eB])]) / Fr(MENU[tuple(h + [eA])])
            _nrat[len(h)][nr] += 1
            _nident += 1
            if nr != Fr(MENU[tuple(h + [eB])]) / Fr(MENU[tuple(h + [eA])]):
                _nident_bad += 1
_nrat_all = Counter()
for b, c in _nrat.items():
    _nrat_all += c
report("normalised square ratios by base |h|",
       {b: {str(k): v for k, v in sorted(c.items())}
        for b, c in sorted(_nrat.items())})
check("T4.2 THE NORMALISED SQUARE IS NOT FLAT: with p = q/M the exchange "
      "square ratio is exactly M(h.e_B)/M(h.e_A) — the raw ratio being 1 — "
      "and that is not 1.  ANCHOR: the value set is D65's committed defect "
      "spectrum {1, 4/5, 5/4} (QUOTES['d65']), i.e. this is the SAME object "
      "D65 already decided, not a new one",
      set(_nrat_all) == D65_DEFECT_RATIOS
      and sum(v for k, v in _nrat_all.items() if k != 1) > 0
      and _nident_bad == 0,
      f"{sum(_nrat_all.values())} squares, "
      f"{sum(v for k, v in _nrat_all.items() if k != 1)} non-unit; "
      f"multiset { {str(k): v for k, v in sorted(_nrat_all.items())} }; "
      f"on the first delivery's own licensed window (bases |h| <= "
      f"{DEPTH-2}) it is "
      f"{ {str(k): sum(_nrat[b][k] for b in range(DEPTH - 1)) for k in sorted(_nrat_all)} } "
      f"— i.e. the SAME {open_pairs} squares the receipt called flat; "
      f"identity ratio == M(h.eB)/M(h.eA) failed on {_nident_bad}")

_ewN = defaultdict(set)
for h in FAM:
    if len(h) >= DEPTH:
        continue
    C = CLASS[tuple(h)]
    for e, q in CAND[tuple(h)]:
        _ewN[(C, b3_canon(h + [e]))].add(Fr(q) / Fr(MENU[tuple(h)]))
_multiN = [k for k, v in _ewN.items() if len(v) > 1]
_nnN, _rkN, _dfN, _holN = holonomy_of(_ewN)
_nnN2, _rkN2, _dfN2, _holN2 = holonomy_of(_ewN, reverse_order=True)


def _pow_of(v, gen):
    """exponent of v as a power of gen, or None."""
    n, x = 0, Fr(v)
    while x > 1:
        x /= gen
        n += 1
    while x < 1:
        x *= gen
        n -= 1
    return n if x == 1 else None


_gen = Fr(5, 4)
_allhol = ({h for h in _holN if h != 1} | {h for h in _holN2 if h != 1})
_exps = [_pow_of(v, _gen) for v in _allhol]
_pow_ok = all(e is not None for e in _exps)
_gcd = 0
for e in _exps:
    if e is not None:
        _gcd = math.gcd(_gcd, abs(e))
_unimodular = [v for v in _allhol if abs(v) == 1]
report("normalised holonomy (spanning-forest census on the SAME graph)",
       f"nodes = {_nnN}, up-edges = {len(_ewN)}, multi-valued = "
       f"{len(_multiN)}, independent cycles = {_rkN}, non-trivial = "
       f"{len(_dfN)} (forward build) / {len(_dfN2)} (reversed build), "
       f"forward value set = {sorted(str(x) for x in _holN)}, reversed "
       f"value set = {sorted(str(x) for x in _holN2)}")
check("T4.3 THE NORMALISED CONNECTION DESCENDS TO RECORDS AND ITS HOLONOMY "
      "IS NON-TRIVIAL, AND IT IS R+-VALUED WITH NO U(1) PART.  This is "
      "falsifier F4's exact shape — a real holonomy of probability "
      "transport with no argument — which the first delivery recorded as "
      "'not reached, vacuously'.  The image of the holonomy homomorphism "
      "is the infinite cyclic group <5/4> (basis-independent); the COUNT "
      "of non-trivial basis cycles is spanning-forest-dependent and is "
      "reported for two different builds rather than quoted as a fact",
      len(_multiN) == 0 and len(_dfN) > 0 and len(_dfN2) > 0
      and _pow_ok and _gcd == 1 and not _unimodular,
      f"every up-edge single-valued ({len(_multiN)} multi-valued); "
      f"{len(_dfN)}/{_rkN} non-trivial basis cycles forward, "
      f"{len(_dfN2)}/{_rkN2} reversed; every realised value is a power of "
      f"5/4 (exponents {sorted(e for e in _exps if e is not None)}, "
      f"gcd {_gcd}), so the image group is <5/4> subset R+; no value has "
      f"modulus 1 with a non-zero argument — the defect is pure modulus")

print()
print("  T4 VERDICT: the flatness of SEC 4 is a property of the "
      "UN-NORMALISED")
print("  budget weight.  For the D42b4 lift (QUOTES['sqrtq'] — 'the "
      "amplitude")
print("  prod sqrt(q)') the raw weight is the right object and the +1 phase "
      "slot")
print("  stands FOR THAT LIFT.  For the process's own conditional kernel the "
      "same")
print("  record graph carries a non-trivial R+ holonomy, which is D65's "
      "committed")
print("  mass-ratio coboundary (QUOTES['d65']) and is F4's shape.  F4 "
      "FIRES.")


# ===========================================================================
# SEC 4D.  T5 — THE DEPTH-FREE THEOREM'S VERIFICATION LEMMAS
#          (the round's MAJOR 4 and its APPENDIX)
#
#  The first delivery's residue 1 sketched a locality argument for why the
#  generated line is flat.  The round proved it — and showed that locality
#  covers only the register-DISJOINT squares (1,355 of 2,227 in the first
#  delivery's window).  The other, register-overlapping half is carried by
#  L4+L5+L6, which are MENU facts, not locality facts: they turn on the
#  propose- and arbitrate-budgets being EQUAL (1/4 each) and mutually
#  exclusive in an actor's own view, so the idle weight is the constant 3/4.
#  That is a grammar-1 coincidence.  It fails in d42b1 (T6.5) and so does
#  the conclusion (T6.1).  The lemma statements are gated here; the proof
#  text lives in the note.
# ===========================================================================

print()
print("-" * 78)
print("SEC 4D  T5 — THE THEOREM'S LEMMAS, GATED")
print("-" * 78)

# L1: q(e|h) is a function of (e, canon(down-set of e)) — past-locality.
_t = time.time()
_l1keys = {}
_l1clash = 0
for h in FAM:
    for e, q in CAND[tuple(h)]:
        acts2 = h + [e]
        pred = b3_poset(acts2)
        sub = [acts2[i] for i in sorted(pred[len(acts2) - 1])]
        k = (e, b3_canon(sub))
        if k in _l1keys and _l1keys[k] != q:
            _l1clash += 1
        _l1keys[k] = q
check("T5.L1 PAST-LOCALITY: the step weight is a function of (e, canon of "
      "e's own down-set) — every field admissible() reads is computed from "
      "the downward-closed view pred[j], so q(e|h) = Q(e, D(e)).  Keys "
      "collide only when the weights agree",
      _l1clash == 0 and len(_l1keys) > 0,
      f"{len(_l1keys)} distinct (e, canon(down-set)) keys over histories of "
      f"depth <= {DEPTH+1}, {_l1clash} weight clashes")

check("T5.L3 DISJOINT => COMMUTING (the locality half): on every closed "
      "square whose two events have DISJOINT register sets, each event's "
      "weight is unchanged by interposing the other — q(e_B|h.e_A) = "
      "q(e_B|h) and symmetrically.  This is the half the first delivery's "
      "sketch covers, and it is a THEOREM (L1+L2)",
      L3_viol == 0 and L3_disjoint > 0,
      f"{L3_disjoint} register-disjoint closed squares over all bases "
      f"0..{DEPTH} at two actors, {L3_viol} weight violations")

check("T5.L4 AN OVERLAPPING CLOSED SQUARE ALWAYS CONTAINS AN IDLE EVENT: "
      "register overlap between two non-idle events forces a shared actor, "
      "and (p,p), (p,r), (r,r) same-actor pairs are all blocked in one "
      "order or the other — so one member has kind 'n'.  THIS IS THE HALF "
      "THE LOCALITY ARGUMENT DOES NOT COVER, and it is grammar-specific",
      L4_noidle == 0 and L4_comparable > 0,
      f"{L4_comparable} register-overlapping (causally comparable) closed "
      f"squares over all bases 0..{DEPTH} at two actors — "
      f"{L4_noidle} without an idle member.  COVERAGE of the first "
      f"delivery's locality sketch, in its own licensed window: "
      f"{sum(L3_by_base[b] for b in range(DEPTH - 1))} of {open_pairs} "
      f"squares (the disjoint ones); the other "
      f"{sum(L4_by_base[b] for b in range(DEPTH - 1))} are carried by "
      f"L4-L6, which are MENU facts, not locality facts")

# L5: idle inertness — a kind-'n' act contributes to no View field.
_l5n = _l5v = 0
for h in FAM:
    if len(h) + 1 > DEPTH:
        continue
    for a in AB:
        h2 = h + [('n', a)]
        for e, q in CAND[tuple(h)]:
            ok2, q2 = b3_admissible(h2, e)
            _l5n += 1
            if not ok2 or q2 != q:
                _l5v += 1
check("T5.L5 IDLE INERTNESS: View.props filters on kind 'p' and View.arbs "
      "on kind 'r', so a kind-'n' act contributes to no field of any view "
      "— adding it changes no weight, q(e|h.n_a) = q(e|h)",
      _l5v == 0 and _l5n > 0,
      f"{_l5n} (history, actor, event) evaluations at two actors, "
      f"{_l5v} violations")


def idle_state(acts, a):
    """(has_p, has_r, #available bases) in a's own past-local view — the
    two indicators admissible() reads to price an idle event."""
    acts2 = acts + [('n', a)]
    pred = b3_poset(acts2)
    view = b3_View(acts2, pred, pred[len(acts2) - 1])
    po = b3_propopts(view, a)
    return bool(po), bool(b3_arbcomps(view, a)), len({b for b, x in po})


_idlew = Counter()
_hphr = Counter()
_nbases = Counter()
_d6 = 0
for h in FAM:
    for a in AB:
        ok, q = b3_admissible(h, ('n', a))
        _idlew[q] += 1
        hp, hr, nb = idle_state(h, a)
        _hphr[(hp, hr)] += 1
        _nbases[nb] += 1
for h in FAM:                      # one level deeper, free: depth <= 6
    if len(h) != DEPTH:
        continue
    for e, q in CAND[tuple(h)]:
        h6 = h + [e]
        _d6 += 1
        for a in AB:
            ok, qq = b3_admissible(h6, ('n', a))
            _idlew[qq] += 1
            hp, hr, nb = idle_state(h6, a)
            _hphr[(hp, hr)] += 1
            _nbases[nb] += 1
check("T5.L6 THE IDLE WEIGHT IS THE CONSTANT 3/4, AND THAT IS THE BUDGET "
      "COINCIDENCE THE THEOREM RESTS ON: q(n_a|h) = 1 - 1/4[has_p] - "
      "1/4[has_r] evaluated in a's own view, and EXACTLY ONE of has_p, "
      "has_r holds — an actor holds at most one live proposal at a time "
      "(L6a) and the two states alternate (L6b).  The propose-budget and "
      "the arbitrate-budget are EQUAL, so both branches price the idle at "
      "3/4.  Change either constant and the overlapping squares stop being "
      "flat: this is a TUNING of d42b3, not a structural fact (T6.5)",
      set(_idlew) == {Fr(3, 4)}
      and set(_hphr) <= {(True, False), (False, True)}
      and set(_nbases) <= {0, 1},
      f"{sum(_idlew.values())} (history, actor) pairs over depth <= "
      f"{DEPTH+1} ({_d6} depth-{DEPTH+1} histories included), weight "
      f"spectrum { {str(k): v for k, v in _idlew.items()} }; "
      f"(has_p, has_r) census {dict(_hphr)} — never (T,T), never (F,F); "
      f"#available bases {dict(_nbases)} — never >= 2  "
      f"[{time.time()-_t:.0f}s]")

# The theorem's other arms: 3 and 4 actors, grammar 1.
for _acts, _dep in ((("A", "B", "C"), 4), (("A", "B", "C", "D"), 3)):
    _t = time.time()
    _f, _c = enumerate_line(b3_candidates, _acts, _dep)
    _cl = _dj = _cm = _cm_ni = _dj_v = 0
    _rr = Counter()
    for h in _f:
        if len(h) + 2 > _dep:
            continue
        cs = [e for e, q in _c[tuple(h)]]
        for i in range(len(cs)):
            for j in range(i + 1, len(cs)):
                eA, eB = cs[i], cs[j]
                oA, qA = b3_admissible(h, eA)
                oB, qB = b3_admissible(h, eB)
                if not (oA and oB):
                    continue
                o1, qB2 = b3_admissible(h + [eA], eB)
                o2, qA2 = b3_admissible(h + [eB], eA)
                if not (o1 and o2):
                    continue
                _cl += 1
                _rr[Fr(qA * qB2, 1) / Fr(qB * qA2, 1)] += 1
                if b3_regs(eA) & b3_regs(eB):
                    _cm += 1
                    _cm_ni += int(eA[0] != 'n' and eB[0] != 'n')
                else:
                    _dj += 1
                    _dj_v += int(qB2 != qB or qA2 != qA)
    _iw = Counter()
    for h in _f:
        for a in _acts:
            ok, q = b3_admissible(h, ('n', a))
            _iw[q] += 1
    _l5n2 = _l5v2 = 0
    for h in _f:
        if len(h) + 1 > _dep:
            continue
        for a in _acts:
            h2 = h + [('n', a)]
            for e, q in _c[tuple(h)]:
                ok2, q2 = b3_admissible(h2, e)
                _l5n2 += 1
                _l5v2 += int(not ok2 or q2 != q)
    check(f"T5.ARM grammar 1, actors {_acts}, depth<={_dep}: raw flatness "
          "and all four lemmas hold on a wider actor pool — the theorem is "
          "not a two-actor accident",
          set(_rr) == {Fr(1)} and _dj_v == 0 and _cm_ni == 0
          and set(_iw) == {Fr(3, 4)} and _l5v2 == 0,
          f"{len(_f)} histories; {_cl} closed squares, ratio multiset "
          f"{ {str(k): v for k, v in _rr.items()} }; disjoint {_dj} "
          f"(violations {_dj_v}), comparable {_cm} (without idle "
          f"{_cm_ni}); idle weights { {str(k): v for k, v in _iw.items()} } "
          f"on {sum(_iw.values())} pairs; L5 {_l5n2} evaluations, {_l5v2} "
          f"violations  [{time.time()-_t:.0f}s]")


# ===========================================================================
# SEC 5.  T3 — THE L_dual RE-RUN ON v10's OWN CHANNELS
#
#  The port, stated before it is run (this is the operationalisation the
#  D68 review standard makes load-bearing):
#
#   v7  : a record is a 2-dimensional poset on N=9 points; F ranges over
#         FIVE-record types = isomorphism types of induced 5-element
#         sub-posets; F* is the same type with every order relation
#         reversed (QUOTES['star']); E = F + F*, O = F - F* (QUOTES['EO']).
#   v10 : a record is canon(h) with the causal order event_poset(h); the
#         faithful analogue of a "k-record type" is the isomorphism type of
#         an induced k-element sub-poset of that causal order; F* is that
#         type with every order relation reversed — the SAME operation,
#         opposite_bits, transcribed to k points.
#
#  v10 records have at most DEPTH events, so k = 5 does not exist here;
#  k in {2,3,4} are all run and printed.  Two orbit conventions are run,
#  because the choice is contestable:
#     (i)  ODD-ORBIT ONLY  : E,O summed over the non-self-dual orbits only
#                            (the literal "for a dual pair (F,F*)" reading).
#     (ii) ALL ORBITS      : E summed over every dual orbit, self-dual ones
#                            contributing F + F* = 2F (also literally
#                            dual-even data), O over the non-self-dual ones.
#  Two domains are run, because the choice is contestable:
#     (A) v10-CLOSED : records whose labelled order-dual is itself a
#                      generated record (the only domain on which the v7
#                      gate can be asked of v10's own objects).
#     (B) DUAL-CLOSED: the family adjoined with the abstract order-duals of
#                      its records (posets, not necessarily admissible) —
#                      v7's own situation, since its universe IS dual-closed.
# ===========================================================================

print()
print("-" * 78)
print("SEC 5  T3 — THE L_dual RE-RUN")
print("-" * 78)


def ktype(pred, idx):
    """Canonical bit-code of the induced order type on the points idx.
    Same encoding as v7's bit_index(n,i,j) = i*n + j, bit set iff i < j."""
    k = len(idx)
    best = None
    for perm in permutations(range(k)):
        bits = 0
        for a in range(k):
            for b in range(k):
                if a != b and idx[perm[a]] in pred[idx[perm[b]]]:
                    bits |= 1 << (a * k + b)
        if best is None or bits < best:
            best = bits
    return best


def dual_ktype(t, k):
    """v7's opposite_bits, transcribed to k points, then canonicalised.
    (v7: 'out |= 1 << bit_index(n, j, i)' for every relation i<j.)"""
    d = 0
    for a in range(k):
        for b in range(k):
            if a != b and ((t >> (a * k + b)) & 1):
                d |= 1 << (b * k + a)
    best = None
    for perm in permutations(range(k)):
        bits = 0
        for a in range(k):
            for b in range(k):
                if a != b and ((d >> (perm[a] * k + perm[b])) & 1):
                    bits |= 1 << (a * k + b)
        if best is None or bits < best:
            best = bits
    return best


def flags_k(pred, n, k):
    c = Counter()
    for idx in combinations(range(n), k):
        c[ktype(pred, list(idx))] += 1
    return c


# --- MODERATE 1: the closed form, evaluated in high precision --------------
# The first delivery gated a float64 port against a float64 evaluation of the
# closed form and called the second one "exact".  Both sides were float64.
# The DERIVATION is exact; so are the |sin| values, because theta = pi/6 and
# E is an integer, whence |sin(theta E)| in {0, 1/2, sqrt(3)/2, 1} by
# E mod 6.  Only exp(-E/32) is transcendental, and Decimal evaluates it to
# as many digits as asked.  So the closed form below is exact to _HP_DIGITS
# and the gate says what it can honestly say: the port agrees with it at
# float64 resolution.
_HP_DIGITS = 50
_SIN_ABS = [_Dec(0), _Dec(1) / 2, _Dec(3).sqrt() / 2,
            _Dec(1), _Dec(3).sqrt() / 2, _Dec(1) / 2]


def closed_form_hp(E):
    """2 e^{-E/32} |sin(pi E / 6)| at _HP_DIGITS digits, |sin| exact."""
    return 2 * (_Dec(-E) / 32).exp() * _SIN_ABS[E % 6]


TYPENAME = {(3, 0): "3-antichain", (3, 2): "one relation + isolated point",
            (3, 6): "V (one below two: FORK)",
            (3, 36): "Lambda (two below one: MERGE)",
            (3, 38): "3-chain",
            (2, 0): "2-antichain", (2, 2): "2-chain"}


def typedesc(t, k):
    """Human descriptor of an order type, derived (not tabulated)."""
    if (k, t) in TYPENAME:
        return TYPENAME[(k, t)]
    rel = [(a, b) for a in range(k) for b in range(k)
           if a != b and ((t >> (a * k + b)) & 1)]
    updeg = Counter(a for a, b in rel)
    dndeg = Counter(b for a, b in rel)
    return (f"{len(rel)} relations, max up-degree {max(updeg.values(), default=0)}, "
            f"max down-degree {max(dndeg.values(), default=0)}")

# per-record flag counts, and the dual poset's flag counts
REC = []   # (class, representative, pred, dual_pred)
for C, hs in BYCLASS.items():
    h = hs[0]
    REC.append((C, h, b3_poset(h), dual_pred(b3_poset(h))))

ABSENT_ORBITS = {}   # k -> (absent, odd) — the k-dependence of MODERATE 2
F3_DUAL_ERR = 0.0    # max L_dual dual-conjugation error over every cell
for K in (2, 3, 4, 5):
    print()
    print(f"  --- k = {K} ---")
    seen = Counter()
    for C, h, pred, dp in REC:
        if len(h) < K:
            continue
        for t, c in flags_k(pred, len(h), K).items():
            seen[t] += c
    if not seen:
        print("    (no records of size >= k)")
        continue
    orbits = {}
    for t in seen:
        d = dual_ktype(t, K)
        orbits[tuple(sorted((t, d)))] = None
    for t in sorted(seen):
        d = dual_ktype(t, K)
        nm = typedesc(t, K)
        dnm = typedesc(d, K)
        print(f"    type {t:>6} [{nm}] x{seen[t]:<6} dual -> {d} [{dnm}] "
              f"{'SELF-DUAL' if d == t else ''}"
              f"{'  <-- DUAL TYPE ABSENT FROM FAMILY' if d != t and d not in seen else ''}")
    odd_orbits = [o for o in orbits if o[0] != o[1]]
    all_orbits = list(orbits)
    _abs_k = [o for o in odd_orbits
              if (o[0] not in seen) or (o[1] not in seen)]
    ABSENT_ORBITS[K] = (len(_abs_k), len(odd_orbits))
    report(f"k={K} dual orbits", f"{len(all_orbits)} total, "
           f"{len(odd_orbits)} with a non-trivial odd channel; odd orbits "
           f"whose dual member is ABSENT from the family: "
           f"{len(_abs_k)}/{len(odd_orbits)}")

    for reading, orbs in (("odd-orbit-only", odd_orbits),
                          ("all-orbits", all_orbits)):
        EO = {}
        for C, h, pred, dp in REC:
            if len(h) < K:
                continue
            f = flags_k(pred, len(h), K)
            fd = flags_k(dp, len(h), K)
            E = sum(f.get(a, 0) + f.get(b, 0) for a, b in orbs)
            O = sum(f.get(a, 0) - f.get(b, 0) for a, b in orbs if a != b)
            Ed = sum(fd.get(a, 0) + fd.get(b, 0) for a, b in orbs)
            Od = sum(fd.get(a, 0) - fd.get(b, 0) for a, b in orbs if a != b)
            EO[C] = (E, O, Ed, Od, h)
        if not EO:
            continue
        # (0) the definitional gate: * must send E -> E and O -> -O
        gEO = all(v[0] == v[2] and v[1] == -v[3] for v in EO.values())
        check(f"T3.{K}.{reading}.a  the E/O port satisfies its own "
              "definition (QUOTES['EO']): the order-dual fixes E and "
              "negates O on every record",
              gEO, f"{len(EO)} records")
        Odist = Counter(v[1] for v in EO.values())
        Edist = Counter(v[0] for v in EO.values())
        report(f"k={K} [{reading}] O distribution over records", dict(Odist))
        report(f"k={K} [{reading}] E distribution over records",
               dict(sorted(Edist.items())))

        # ---- domain A: v10-closed ----------------------------------------
        domA = [C for C, h, pred, dp in REC
                if len(h) >= K and dual_realised(h)]
        # ---- the dual-conjugation error, EXACT ---------------------------
        # v7's own forms (complex_laplace_by_mode):
        #   dual_complex : L = e^{-kappa E} rho^{O}
        #   naive_complex: L = e^{-kappa E} rho^{O - E}
        # with rho = e^{i theta}.  Then, using * : E -> E, O -> -O,
        #   |L_dual(R*) - conj(L_dual(R))| = 0                        EXACT
        #   |L_naive(R*) - conj(L_naive(R))| = 2 e^{-kappa E} |sin(theta E)|
        # (derivation: L_naive(R*) - conj L_naive(R)
        #             = e^{-kappa E} rho^{-O} ( rho^{-E} - rho^{E} ).)
        # Both the closed form and the numeric port are computed and gated
        # against each other.
        KAPPA_F = Fr(1, 32)             # v7's own kappa, D("0.03125")
        THETA = math.pi / 6             # v7's own root, ROOTS["pi/6"]

        def L(E, O, mode):
            ex = math.exp(-float(KAPPA_F) * E)
            ang = THETA * (O - E if mode == "naive" else O)
            return (ex * math.cos(ang), ex * math.sin(ang))

        for dname, dom in (("A: v10-closed", domA),
                           ("B: dual-closed", list(EO))):
            if not dom:
                report(f"k={K} [{reading}] domain {dname}", "EMPTY")
                continue
            worst = {}
            worst_hp = {}
            for mode in ("dual", "naive"):
                w = 0.0
                for C in dom:
                    E, O, Ed, Od, h = EO[C]
                    lr = L(Ed, Od, mode)
                    lc = L(E, O, mode)
                    w = max(w, math.hypot(lr[0] - lc[0], lr[1] + lc[1]))
                worst[mode] = w
                if mode == "dual":
                    worst_hp[mode] = _Dec(0)
                else:
                    worst_hp[mode] = max(closed_form_hp(EO[C][0])
                                         for C in dom)
            F3_DUAL_ERR = max(F3_DUAL_ERR, worst["dual"])
            _gap = abs(_Dec(repr(worst["naive"])) - worst_hp["naive"])
            report(f"k={K} [{reading}] domain {dname} ({len(dom)} records)",
                   f"L_dual dual-conjugation error = {worst['dual']:.3e} "
                   f"(closed form: identically 0); L_naive = "
                   f"{worst['naive']:.6f} (closed form at {_HP_DIGITS} "
                   f"digits: {str(worst_hp['naive'])[:20]})")
            check(f"T3.{K}.{reading}.{dname[0]}  the FLOAT64 port agrees "
                  "with a HIGH-PRECISION evaluation of the closed form "
                  "2 e^{-kappa E}|sin(theta E)|, and L_dual is 0.  LABEL "
                  "(round MODERATE 1): the DERIVATION is exact and the "
                  "|sin| values are exact algebraic numbers, but the port "
                  "L() is float64 — so this gate certifies agreement at "
                  "float64 resolution, not exactness of the evaluation",
                  _gap < _Dec(FLOAT_TOL) * max(_Dec(1), worst_hp["naive"])
                  and worst["dual"] < FLOAT_TOL,
                  f"|float64 port - {_HP_DIGITS}-digit closed form| = "
                  f"{float(_gap):.3e} (tolerance {FLOAT_TOL:.3e} x scale); "
                  f"L_dual = {worst['dual']:.3e}")

# the headline T3 readings, recomputed once for the verdict board
K = 3
seen3 = Counter()
for C, h, pred, dp in REC:
    if len(h) >= 3:
        for t, c in flags_k(pred, len(h), 3).items():
            seen3[t] += c
orb3 = {}
for t in seen3:
    orb3[tuple(sorted((t, dual_ktype(t, 3))))] = None
odd3 = [o for o in orb3 if o[0] != o[1]]
absent = [o for o in odd3 if (o[0] not in seen3) or (o[1] not in seen3)]
check("T3.A THE ODD CHANNEL EXISTS ON v10's OBJECTS: at k=3 the generated "
      "line realises a non-self-dual order type, so O is not identically "
      "zero",
      len(odd3) > 0,
      f"non-self-dual orbits realised = {[list(o) for o in odd3]}")
# --- T3.B: how one-sided is the odd channel?  Measured, per depth, because
#     the answer MOVES with the window and the first reading of it was wrong.
#     At depth <= 4 the fork type V does not occur at all and the type-level
#     asymmetry is total; at depth 5 V appears (216 occurrences) and the
#     type-level claim FAILS.  What survives the widening is the weaker and
#     durable statement: the odd channel never changes SIGN on a record.
per_depth_types = {}
for d in range(3, DEPTH + 1):
    c = Counter()
    for C, h, pred, dp in REC:
        if len(h) == d:
            for t, n in flags_k(pred, d, 3).items():
                c[t] += n
    per_depth_types[d] = dict(c)
report("k=3 order-type census per record depth (type 6 = V/FORK, "
       "36 = Lambda/MERGE)", per_depth_types)
_V_absent_upto = [d for d in per_depth_types if 6 not in per_depth_types[d]]
_frac = {k: v for k, v in sorted(ABSENT_ORBITS.items())}
_k5 = ABSENT_ORBITS.get(5)
check("T3.B1 THE TYPE-LEVEL ONE-SIDEDNESS IS k-DEPENDENT, AND AT v7's OWN "
      "k = 5 IT IS TOTAL.  The first delivery's self-correction — 'the "
      "type-level one-sidedness is a WINDOW ARTIFACT, because the fork "
      "type V appears at depth 5' — is a k = 3 statement, and the round's "
      "MAJOR 5 is right that the k = 5 cell reverses it: at k = 5, the "
      "only k that reproduces v7's own five-record type "
      "(QUOTES['star']), EVERY non-self-dual orbit has its dual member "
      "absent from the family.  The depth census below is reported "
      "unchanged; what changes is what it was said to mean",
      len(_V_absent_upto) > 0 and (DEPTH < 5 or 6 in per_depth_types[5])
      and _k5 is not None and _k5[1] > 0 and _k5[0] == _k5[1]
      and len({a / b for a, b in ABSENT_ORBITS.values() if b}) > 1,
      f"absent-dual odd orbits by k (absent/odd): {_frac} — NOT constant "
      f"in k; k=3 says 0, k=5 says all.  Depths with NO fork type = "
      f"{sorted(_V_absent_upto)}; fork:merge counts at the deepest "
      f"measured layer = {per_depth_types[DEPTH].get(6, 0)}:"
      f"{per_depth_types[DEPTH].get(36, 0)}")

Osign = Counter()
for C, h, pred, dp in REC:
    if len(h) < 3:
        continue
    f = flags_k(pred, len(h), 3)
    Osign[sum(f.get(a, 0) - f.get(b, 0) for a, b in odd3)] += 1
_maxO, _minO = max(Osign), min(Osign)
check("T3.B2 WHAT DOES SURVIVE THE WIDENING: the odd channel is SIGN-"
      "DEFINITE on every record at every depth measured — merges always "
      "outnumber forks inside a single record, so O never changes sign.  "
      "A reversal-odd coordinate that cannot change sign cannot separate "
      "a record from its dual within the family",
      _maxO <= 0 and _minO < 0,
      f"O spectrum over {sum(Osign.values())} records = "
      f"{dict(sorted(Osign.items()))} (orbit ordered (V, Lambda), so "
      f"O = #V - #Lambda); max = {_maxO}, min = {_minO}")

report("odd orbits whose dual member is absent from the family, BY k "
       "(round MODERATE 2 / MAJOR 5: this is the ORDER-TYPE answer, and it "
       "is k-dependent; T1.9's 294/1264 is the LABELLED answer)",
       {k: f"{a}/{b}" for k, (a, b) in sorted(ABSENT_ORBITS.items())})

domA3 = [C for C, h, pred, dp in REC if len(h) >= 3 and dual_realised(h)]
E_on_domA_oddonly = set()
for C in domA3:
    h = BYCLASS[C][0]
    f = flags_k(b3_poset(h), len(h), 3)
    E_on_domA_oddonly.add(sum(f.get(a, 0) + f.get(b, 0) for a, b in odd3))
# --- the honesty control on T3: is the 0 evidence about v10 at all? -------
# If L_dual's dual-conjugation error is 0 for ARBITRARY integer (E, O) —
# numbers not drawn from v10 or from anywhere — then the error 0 is an
# algebraic identity of the ansatz and carries no information about the
# substrate.  This is the positive control the D68 review standard demands.
_adv = [(E, O) for E in (0, 1, 2, 3, 5, 7, 11, 97, 1000)
        for O in (-97, -3, -1, 0, 1, 2, 41, 555)]


def _L(E, O, mode):
    ex = math.exp(-(1 / 32.0) * E)
    ang = (math.pi / 6) * (O - E if mode == "naive" else O)
    return (ex * math.cos(ang), ex * math.sin(ang))


_adv_dual = max(math.hypot(_L(E, -O, "dual")[0] - _L(E, O, "dual")[0],
                           _L(E, -O, "dual")[1] + _L(E, O, "dual")[1])
                for E, O in _adv)
_adv_naive = max(math.hypot(_L(E, -O, "naive")[0] - _L(E, O, "naive")[0],
                            _L(E, -O, "naive")[1] + _L(E, O, "naive")[1])
                 for E, O in _adv)
check("T3.CTRL THE '0' IS AN IDENTITY OF THE ANSATZ, NOT A FACT ABOUT v10: "
      "feeding ADVERSARIAL integer (E,O) pairs drawn from nowhere gives "
      "L_dual error 0 all the same, while the naive form still fails.  So "
      "reproducing v7's 0 on v10's channels is evidence only that E was "
      "made even and O odd — which the port did by construction",
      _adv_dual < 1e-12 and _adv_naive > 1,
      f"{len(_adv)} adversarial (E,O) pairs: L_dual max error = "
      f"{_adv_dual:.2e}; L_naive max error = {_adv_naive:.6f}")

check("T3.C THE TRANSFER IS EMPTY ON THE ODD-ORBIT READING: on the only "
      "domain where the v7 gate can be asked of v10's own records "
      "(those whose dual is in-family), the odd-orbit even channel E is "
      "identically 0, so L_dual and L_naive are the SAME function there "
      "and v7's 0-vs-1.82 discrimination has nothing to discriminate",
      E_on_domA_oddonly == {0},
      f"E values on the v10-closed domain (odd-orbit reading) = "
      f"{sorted(E_on_domA_oddonly)}; |domain| = {len(domA3)}")

# the contestable alternative, run: under the ALL-ORBITS reading E counts
# self-dual types too, is non-zero on the v10-closed domain, and the v7
# discrimination DOES reappear there.
all3 = list(orb3)
E_all = []
for C in domA3:
    h = BYCLASS[C][0]
    f = flags_k(b3_poset(h), len(h), 3)
    E_all.append(sum(f.get(a, 0) + f.get(b, 0) for a, b in all3))
_naive_all = max(2 * math.exp(-(1 / 32.0) * E) * abs(math.sin(math.pi * E / 6))
                 for E in E_all)
check("T3.D THE CONTESTABLE CHOICE, RUN BOTH WAYS: under the ALL-ORBITS "
      "reading (self-dual types also contribute F + F* = 2F to the even "
      "channel — equally literal against QUOTES['EO']) the even channel "
      "is non-zero on the v10-closed domain and v7's discrimination DOES "
      "reappear: L_dual 0, L_naive > 0.  The reading is therefore what "
      "decides whether the transfer looks empty or successful, and the "
      "receipt reports both rather than choosing",
      _naive_all > 0 and min(E_all) > 0,
      f"E spectrum on the v10-closed domain (all-orbits) = "
      f"{sorted(set(E_all))}; L_naive max = {_naive_all:.6f} vs v7's own "
      f"{NAIVE_DUALCONJ_ERROR_V7[:8]} (both are the same closed form at "
      "different E)")


# ===========================================================================
# SEC 6.  THE FALSIFIER BOARD
# ===========================================================================

print()
print("-" * 78)
print("SEC 6  THE PIN'S FOUR FALSIFIERS, each with its verdict")
print("-" * 78)

# MODERATE 5: every verdict below is a COMPUTED predicate over gate
# variables.  The first delivery hand-set F3_fired and F4_fired to False
# with the justification in a comment; F4 was wrong.
F1_fired = _dr_no > 0            # * is not an operation on v10's objects
F1_narrow = not (set(ratios) == {Fr(1)})   # A_D not odd under * — false
F2_fired = (len(d1) == 0 and r1 > 0 and wide_nonunit == 0)
F3_fired = F3_DUAL_ERR > FLOAT_TOL         # computed over every T3 cell
# F4: "the round-trip defect exists but is not U(1)-valued."  It fires on
# TWO independent objects now — the normalised connection of grammar 1
# (T4.3) and the raw transport-scope squares of grammar 2 (T6.1) — and in
# both cases the realised values are positive rationals, i.e. R+ with no
# argument.
F4_normalised = len(_dfN) > 0 and _pow_ok and not _unimodular
F4_transport = TRANSPORT_DEFECTS > 0
F4_fired = F4_normalised or F4_transport
F2_scope_ok = TRANSPORT_DEFECTS == 0       # would F2 hold at transport scope?

print()
print("  F1  'A_D is not odd under the order-dual * at the fixture.'")
print("      VERDICT: DOES NOT FIRE AS WRITTEN, FIRES IN ITS SPIRIT.")
print("      As written: A_D IS odd under * on the common carrier — but")
print("      only as 0 = -0 (T1.7), because A_D == 0 identically (T1.1).")
print("      In its spirit: the two reversals are the same map ONLY on")
print("      2-event histories (T1.4) and are different maps everywhere")
print("      else (T1.5); and * is not even an operation on v10's records")
print("      (T1.9: %d of %d records have no in-family dual)."
      % (_dr_no, _dr_yes + _dr_no))
print("      => Clause 3's bridge is NOT established.  The corpus does")
print("         not gain two unrelated reversal-odd channels; it gains")
print("         one channel with no content and one operation with no")
print("         domain.")

print()
print("  F2  'The sqrt(q) round-trip transport is identically 1 on every")
print("      delete-then-insert cycle of the generated line.'")
print(f"      VERDICT: {'FIRED' if F2_fired else 'did not fire'} — AT "
      "CLOSED SCOPE, ON GRAMMAR 1, FOR THE RAW WEIGHT.")
print(f"      {r1} independent cycles at grammar 1 depth<={DEPTH} and "
      f"{sum(wide_ratios.values())} closed")
print("      exchange squares over every base (depth <= 7), all exactly 1;")
print("      every up-edge single-valued.  The round supplies the reason: "
      "it")
print("      is a THEOREM for this grammar (T5.L1/L3/L4/L5/L6), and the")
print("      T2 half of it is forced by T1.8 alone (T2.0).")
print("      THREE SCOPE CLAUSES, all measured here, all narrowing it:")
print("        (i)  GRAMMAR.  At transport scope (d42b1) A_D is NOT zero: "
      f"{TRANSPORT_DEFECTS} of")
print(f"             {TRANSPORT_CLOSED} closed squares are non-unit "
      f"(spectrum "
      f"{ {str(k): v for k, v in sorted(TRANSPORT_SPECTRUM.items())} }),")
print(f"             plus {TRANSPORT_HALFOPEN} half-open squares "
      "(A_D = +/- infinity).  T6.1/T6.2.")
print("        (ii) INSTRUMENT.  The record-deletion-graph census cannot "
      "see them:")
print(f"             {TRANSPORT_RECORD_CLOSES} of {TRANSPORT_DEFECTS} "
      "defective squares close at record level.  T6.3.")
print("        (iii) WEIGHT.  For the process's own conditional kernel "
      "q/M the same")
print("             grammar-1 record graph has non-trivial holonomy, "
      "<5/4> in R+.  T4.3.")
print("      => THE GENERATED LINE IS FLAT AT CLOSED SCOPE, IN GRAMMAR 1, "
      "FOR THE RAW")
print("         BUDGET WEIGHT — and that is exactly the object D42b4's "
      "prod sqrt(q)")
print("         lift transports, so D71 Clause 3's '+1' is forced FOR "
      "THAT LIFT.")
print("         It is not a statement about the generated line as such.")

print()
print("  F3  'L_dual's dual-conjugation error on the generated line's")
print("      channels is non-zero.'")
print(f"      VERDICT: {'FIRES' if F3_fired else 'DOES NOT FIRE'} "
      f"(computed: worst L_dual error over every cell = "
      f"{F3_DUAL_ERR:.3e})")
print("      — and the reason is worse than a")
print("      failure would have been.  The error is 0 on v10's")
print("      channels, at k = 2, 3, 4 AND 5, on both domains and both orbit")
print("      readings.  But T3.CTRL shows the 0 is an ALGEBRAIC IDENTITY")
print("      of the ansatz: adversarial (E,O) integers from nowhere score")
print("      0 too.  Reproducing it is evidence only that the port made E")
print("      even and O odd, which it did by construction.  A2c shows the")
print("      same of v7's own control number: 1.8210207... is exactly")
print("      2*exp(-3/32), the closed form at E = 3 — a constant of the")
print("      ansatz, not a measurement of the N=9 universe.")
print("      Scope, both readings run: on the odd-orbit reading the even")
print("      channel is identically 0 on the v10-closed domain (T3.C), so")
print("      even the naive control scores 0 and there is nothing to")
print("      discriminate; on the all-orbits reading the discrimination")
print("      does reappear (T3.D).  => the surviving v7 form TRANSFERS,")
print("      FORMALLY, and the transfer is empty of substrate content.")

print()
print("  F4  'The round-trip defect exists but is not U(1)-valued.'")
print(f"      VERDICT: {'FIRES' if F4_fired else 'does not fire'} — and "
      "the first delivery's 'not reached,")
print("      vacuously' was WRONG (round MAJOR 1 + MAJOR 2).  A defect "
      "exists,")
print("      on two independent objects, and it is R+-valued with no "
      "argument:")
print(f"        (a) normalised connection, grammar 1: {F4_normalised} — "
      "image group")
print("            <5/4> subset R+ on the same 758-cycle record graph "
      "(T4.3), which")
print("            is D65's committed mass-ratio coboundary "
      "(QUOTES['d65']).")
print(f"        (b) raw transport scope, grammar 2: {F4_transport} — "
      f"{TRANSPORT_DEFECTS} closed squares")
print("            with ratios in "
      f"{sorted(str(k) for k in TRANSPORT_SPECTRUM)} plus "
      f"{TRANSPORT_HALFOPEN} half-open")
print("            squares at A_D = +/- infinity (T6.1, T6.2).")
print("      => The founding slogan is refuted IN F4's OWN DIRECTION, not "
      "one step")
print("         earlier: there IS a real holonomy of probability "
      "transport on this")
print("         substrate, and it has NO PHASE.  What is NOT exhibited "
      "anywhere in")
print("         this unit is a U(1) part — that is what remains open, and "
      "it is now")
print("         a characterisation question, not an existence question.")


# ===========================================================================
# SEC 7.  DETERMINISM PROBE
# ===========================================================================

print()
print("-" * 78)
print("SEC 7  DETERMINISM PROBE")
print("-" * 78)

# (a) independent recomputation of the exchange census by a different route:
#     mu_of on the two full sequences, rather than the product of two
#     admissible() step weights.
alt_nonunit = 0
alt_n = 0
for h in FAM:
    if len(h) + 2 > DEPTH:
        continue
    cands = [e for e, q in CAND[tuple(h)]]
    for i in range(len(cands)):
        for j in range(i + 1, len(cands)):
            eA, eB = cands[i], cands[j]
            m1_ = b3_mu(h + [eA, eB])
            m2_ = b3_mu(h + [eB, eA])
            if m1_ is None or m2_ is None:
                continue
            alt_n += 1
            if m1_ != m2_:
                alt_nonunit += 1
check("D1 SECOND ROUTE: recomputing every square as mu_of(h.eA.eB) vs "
      "mu_of(h.eB.eA) (whole-history weights, not step products) gives "
      "the same census",
      alt_nonunit == 0 and alt_n == open_pairs,
      f"{alt_n} squares by route 2 vs {open_pairs} by route 1; "
      f"{alt_nonunit} unequal")

# (b) order-independence of the spanning-forest construction: rerun the
#     holonomy with edges (and weights) visited in reverse order.
_n2, rank2, def2, _h2 = holonomy_of(EW1, reverse_order=True)
check("D2 SPANNING-FOREST ORDER INDEPENDENCE: reversing the edge visit "
      "order gives the same cycle rank and the same (zero) defect count",
      rank2 == r1 and len(def2) == len(d1),
      f"rank {rank2} vs {r1}; defects {len(def2)} vs {len(d1)}")

# (c) iteration-order independence of the exchange census
_rev_ratios = Counter()
for h in FAM:
    if len(h) + 2 > DEPTH:
        continue
    cands = [e for e, q in reversed(CAND[tuple(h)])]
    for i in range(len(cands)):
        for j in range(i + 1, len(cands)):
            r, st = AD_ratio(h, cands[i], cands[j])
            if st == "closed":
                _rev_ratios[r] += 1
# (d) the one place hash order could have leaked into a reported number was
#     the negative control's choice of edge; it is keyed on stable_key, and
#     re-deriving the same census under the reversed stable order must give
#     the same multiset of defect counts.
_tamper_rev = []
for k in sorted(EW1, key=stable_key)[:20]:
    _nn, _rk, _df, _hl = holonomy_of(
        EW1, reverse_order=True, tamper=(k, sorted(EW1[k])[0], Fr(3, 2)))
    _tamper_rev.append(len(_df) > 0)
check("D4 NEGATIVE-CONTROL STABILITY: the same twenty stable-ordered edges "
      "give the same hit/miss pattern when the spanning forest is built in "
      "the reverse order",
      sum(_tamper_rev) == len(_tamper_hits),
      f"{sum(_tamper_rev)} hits reversed vs {len(_tamper_hits)} forward")

check("D3 ITERATION-ORDER INDEPENDENCE: rebuilding the exchange census "
      "with the candidate lists traversed in the opposite order gives the "
      "identical ratio multiset",
      _rev_ratios == ratios,
      f"reverse-order multiset = {dict(_rev_ratios)} vs "
      f"{dict(ratios)}; PYTHONHASHSEED = "
      f"{os.environ.get('PYTHONHASHSEED', 'default')}")


# ===========================================================================
# SEC 8.  SUMMARY
# ===========================================================================

print()
print("=" * 78)
print(f"[SUMMARY] {PASS} PASS / {FAIL} FAIL   "
      f"(anchor failures: {ANCHOR_FAIL})   "
      f"elapsed {time.time()-T0:.0f}s")
print(f"[SUMMARY] of the {PASS} passes, {len(COROLLARY)} carry NO "
      "INDEPENDENT INFORMATION and are")
print("          not evidence (round MODERATE 4) — each is entailed by "
      "another gate")
print("          or is a theorem true of every object of its type:")
for _lab, _why in COROLLARY:
    print(f"            {_lab:<10} <= {_why[:58]}")
print(f"[SUMMARY] independent-evidence passes: {PASS - len(COROLLARY)}")
print("=" * 78)
print(f"""
[VERDICT] P1 IS REFUTED ON THE GENERATED LINE — at the holonomy leg, not
at the identification leg — and the ROUND-1 repairs move three of the four
things the first delivery said about that refutation.

  T1  the reversal test .... unchanged, and widened.  The two reversals DO
      admit a common carrier (linear extensions), coincide EXACTLY on the
      F-PAIR fixture and nowhere else, and on that carrier A_D is
      identically zero — now on {sum(wide_ratios.values())} closed squares at every base up
      to depth {DEPTH+2}, plus 3- and 4-actor arms.
  T5  WHY (new, the round's theorem) ... grammar-1 raw flatness is a
      THEOREM, not a measurement: past-locality (L1-L3) carries the
      register-disjoint squares, and idle inertness plus the constant
      idle weight 3/4 (L4-L6) carry the overlapping ones.  The second
      half is a BUDGET COINCIDENCE of d42b3 — equal propose/arbitrate
      budgets, mutually exclusive in an actor's own view.
  T6  TRANSPORT SCOPE (new, the round's MAJOR 1) ... and that coincidence
      FAILS one grammar over.  In d42b1, {TRANSPORT_DEFECTS} of {TRANSPORT_CLOSED} closed squares
      have A_D != 0 and {TRANSPORT_HALFOPEN} more are half-open (A_D = +/- infinity).
      Every one of them carries a DELIVERY event.  The first delivery
      asserted the opposite on exactly this window as [MEASURED].
      {TRANSPORT_RECORD_CLOSES} of {TRANSPORT_DEFECTS} close at record level, so the record-deletion-
      graph census — the only test that was run there — is BLIND to them
      by construction, and so is its negative control.
  T4  THE NORMALISED KERNEL (new, the round's MAJOR 2) ... the flatness is
      a property of the RAW budget weight.  For the process's own
      conditional kernel q/M the same record graph carries a non-trivial
      holonomy with image <5/4> in R+ — D65's committed mass-ratio
      coboundary, which this unit had failed to cite.  For D42b4's
      prod sqrt(q) lift the raw weight IS the right object, so the phase
      slot's '+1' survives FOR THAT LIFT.
  T2  the closure test ..... F2 fires at closed scope, on grammar 1, for
      the raw weight — and T2.0 shows the whole T2 census is algebraically
      forced by T1.8 (mu is an exact potential), so the 758 + 424 + 645
      cycles are one fact counted six times, not six measurements.
  T3  the L_dual re-run .... F3 does NOT fire; the 0 is an identity of the
      ansatz (T3.CTRL) and v7's 1.82 is the same closed form at E = 3
      (A2c).  The k = 5 cell — v7's own five-record type, which the first
      delivery said 'does not exist here' — runs in seconds and REVERSES
      T3.B1: at k = 5 all non-self-dual orbits have their dual member
      absent.  Absent/odd by k: {dict(sorted(ABSENT_ORBITS.items()))}.

  F1 fires in its spirit; F2 fires at closed scope only; F3 does not fire
  and means nothing; F4 FIRES — a real holonomy of probability transport
  exists on this substrate and it has NO PHASE.  The exhibited defect is
  R+-valued throughout, on both objects.  The U(1) part is not exhibited
  anywhere here, and that — not existence — is what is left open.
""")
sys.exit(0)
