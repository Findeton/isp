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

RUNTIME.  ~6-9 min, dominated by ANCHOR A2 (the v7 N=9 record
universe).  Set D72_SKIP_A2=1 to skip that anchor (it then reports
SKIPPED and the receipt still exits on its own gates); the default is
to run it.
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


def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    PASS += int(bool(ok))
    FAIL += int(not ok)
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))
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
}

# committed NUMERIC anchors (quoted values, never re-derived here)
NAIVE_DUALCONJ_ERROR_V7 = "1.8210207227600682556870097725525"   # paper30:2838
DUAL_DUALCONJ_ERROR_V7 = "0"                                     # paper30:2851
V6_ANTISYM_GAP_QUOTED = 2.2e-16                                  # v6 p4:2636
D42B4_ZSEQ = Fr(4)      # note-d42b4 / d42b4 receipt: Z_seq  = 4
D42B4_ZCLASS = Fr(3)    # note-d42b4 / d42b4 receipt: Z_class = 3
D42B4_NSEQ = 32         # note-d42b4 / d42b4 receipt: 32 depth-2 sequences

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
     "def mu_of(acts):"],
    "d72_d42b3",
)
report("d42b3 slice", f"{b3n}/{b3tot} bytes; "
       f"exports = candidates_for/admissible/event_poset/canon/mu_of")

# --- the generated line, grammar 2 (transport/reconciliation layer) ---------
B1, b1n, b1tot = slice_exec(
    "v10/code/d42b1_transport_exact.py",
    'print("[d42b1',
    ["def candidates_for(acts, actors):",
     "def admissible(acts, e, actors, law=PK1):",
     "def linear_extensions(acts):",
     "def canon(acts):"],
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
_argmax_ok = all(
    2 * math.exp(-3 / 32.0) >= 2 * math.exp(-e / 32.0)
    * abs(math.sin(math.pi * e / 6)) - 1e-15 for e in range(0, 400))
anchor("A2c the exact closed form of v7's dual-conjugation error, "
       "maximised over integer E, REPRODUCES paper30:2838's published "
       f"constant {NAIVE_DUALCONJ_ERROR_V7} — with no re-run of the N=9 "
       "universe",
       _closed_str == NAIVE_DUALCONJ_ERROR_V7 and _argmax_ok,
       f"2*exp(-3/32) = {_closed_str}; argmax over E in 0..399 is E = 3 "
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
report("exchange-square census (grammar 1, depth<=%d)" % DEPTH, dict(sq))
report("distinct exact ratios dP_AB/dP_BA", dict(ratios))

check("T1.1 A_D CONTENT: every closed exchange square of the generated "
      "line has dP_AB/dP_BA EXACTLY 1, so A_D == 0 identically — the "
      "transport reversal AB->BA has no content on this substrate",
      len(nonunit) == 0 and open_pairs > 0 and set(ratios) == {Fr(1)},
      f"{open_pairs} closed squares, {len(nonunit)} with ratio != 1, "
      f"ratio multiset = {{1: {ratios[Fr(1)]}}}")

check("T1.2 NO HALF-OPEN SQUARE: there is no pair whose AB order is "
      "admissible while BA is not (a half-open square would make A_D "
      "+/-infinity — a support-level, non-U(1) and non-R+ defect)",
      sq["AB-only"] == 0 and sq["BA-only"] == 0,
      f"AB-only = {sq['AB-only']}, BA-only = {sq['BA-only']}, "
      f"both-blocked = {sq['both-blocked']}")

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
      _bij_ok, f"{_bij_n} histories, all depths 2..{DEPTH}")

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
      % open_pairs)

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
def dual_realised(h):
    """Is the labelled order-dual of this record itself a generated record?"""
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
check("T1.9 CARRIER C: the generated line is NOT closed under the order-"
      "dual — a majority of its records have no dual inside the family, "
      "so * is a PARTIAL map on v10's objects, not an operation on them",
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

check("T2.1 THE CONNECTION DESCENDS: every up-edge of the record deletion "
      "graph carries a SINGLE step weight — the sqrt(q) connection is "
      "well defined on records, not merely on sequences",
      m1 == 0, f"{e1} up-edges, {m1} multi-valued")

check("T2.2 THE ROUND TRIP CLOSES AT 1, EXACTLY, ON EVERY INDEPENDENT "
      "CYCLE: the modulus returns to its start and the accumulated log is "
      "0 = A_D on every loop (T1.1).  This is the pin's F2 condition, and "
      "the cycle rank shows the test is NOT vacuous",
      len(d1) == 0 and r1 > 0,
      f"{r1} independent cycles (E - V + C), {len(d1)} with holonomy != 1, "
      f"worst |log holonomy| = {w1}")

# explicit delete-then-insert round trips (the transverse loops named in
# the pin's parent: incomparable-pair exchanges ARE the transverse loops)
sq_loops = 0
sq_hol_nonunit = 0
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
            if b3_canon(h + [eA, eB]) != b3_canon(h + [eB, eA]):
                continue      # not a closed loop in the record graph
            sq_loops += 1
            if r != 1:
                sq_hol_nonunit += 1
check("T2.3 THE EXPLICIT DELETE-THEN-INSERT ROUND TRIPS (the transverse "
      "loops: h.eA.eB -> h.eB -> h.eB.eA -> h.eA -> h.eA.eB).  sqrt(q)-"
      "transport around each gives sqrt(dP_AB/dP_BA) = 1 exactly, and "
      "2*log of it equals A_D = 0",
      sq_hol_nonunit == 0 and sq_loops > 0,
      f"{sq_loops} record-closing exchange loops, {sq_hol_nonunit} with "
      "holonomy != 1")

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
      f"{_tamper_hits[0][1][:3] if _tamper_hits else None}")

check("T2.4 U(1) CONTENT: the round-trip defect is not merely real-"
      "positive rather than unimodular (falsifier F4's shape) — there is "
      "NO defect at all.  The holonomy group of sqrt(q)-transport on the "
      "generated line's record deletion graph is the TRIVIAL group",
      len(d1) == 0,
      "holonomy group = {1}; neither R+ nor U(1) is realised, because "
      "nothing but 1 is realised")

# --- second grammar and a second arm: is the flatness a grammar artifact? --
b1_cand = B1["candidates_for"]
b1_canon = B1["canon"]
for _actors, _dep in ((("A", "B"), 4), (("A", "B", "C"), 3)):
    _fam, _cache = enumerate_line(b1_cand, _actors, _dep)
    _n, _e, _m, _r, _d, _w, _ew = deletion_graph_holonomy(
        _fam, _cache, b1_canon, _dep,
        f"grammar 2 (d42b1) {_actors} depth<={_dep}")
    check(f"T2.5 SECOND GRAMMAR {_actors} depth<={_dep}: same verdict — "
          "connection descends, every independent cycle has holonomy "
          "exactly 1",
          _m == 0 and len(_d) == 0 and _r > 0,
          f"{_r} independent cycles, {len(_d)} defects, {len(_fam)} "
          "histories")


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

for K in (2, 3, 4):
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
    report(f"k={K} dual orbits", f"{len(all_orbits)} total, "
           f"{len(odd_orbits)} with a non-trivial odd channel")

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
            worst_exact = {}
            for mode in ("dual", "naive"):
                w = 0.0
                for C in dom:
                    E, O, Ed, Od, h = EO[C]
                    lr = L(Ed, Od, mode)
                    lc = L(E, O, mode)
                    w = max(w, math.hypot(lr[0] - lc[0], lr[1] + lc[1]))
                worst[mode] = w
                if mode == "dual":
                    worst_exact[mode] = 0.0
                else:
                    worst_exact[mode] = max(
                        2 * math.exp(-float(KAPPA_F) * EO[C][0])
                        * abs(math.sin(THETA * EO[C][0])) for C in dom)
            report(f"k={K} [{reading}] domain {dname} ({len(dom)} records)",
                   f"L_dual dual-conjugation error = {worst['dual']:.3e} "
                   f"(exact 0); L_naive = {worst['naive']:.6f} "
                   f"(exact closed form {worst_exact['naive']:.6f})")
            check(f"T3.{K}.{reading}.{dname[0]}  float port agrees with "
                  "the exact closed form 2 e^{-kappa E}|sin(theta E)| for "
                  "the naive mode, and L_dual is 0",
                  abs(worst["naive"] - worst_exact["naive"]) < 1e-12
                  and worst["dual"] < 1e-12,
                  f"|float - exact| = "
                  f"{abs(worst['naive']-worst_exact['naive']):.3e}")

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
check("T3.B1 THE TYPE-LEVEL ONE-SIDEDNESS IS A WINDOW ARTIFACT, and this "
      "gate is what caught it: at record depth <= 4 the FORK type V does "
      "not occur at all, so the order-dual is total-out-of-family there; "
      "at depth 5 it does occur.  The receipt reports the census per "
      "depth rather than the depth-4 headline",
      len(_V_absent_upto) > 0 and (DEPTH < 5 or 6 in per_depth_types[5]),
      f"depths with NO fork type = {sorted(_V_absent_upto)}; "
      f"fork:merge counts at the deepest measured layer = "
      f"{per_depth_types[DEPTH].get(6, 0)}:{per_depth_types[DEPTH].get(36, 0)}")

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

report("odd orbits whose dual member is absent from the family (k=3)",
       f"{len(absent)}/{len(odd3)}")

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

F1_fired = _dr_no > 0            # * is not an operation on v10's objects
F1_narrow = not (set(ratios) == {Fr(1)})   # A_D not odd under * — false
F2_fired = (len(d1) == 0 and r1 > 0 and len(nonunit) == 0)
F3_fired = False                 # measured below: the error is 0, not != 0
F4_fired = False                 # no defect exists, so none can be non-U(1)

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
print(f"      VERDICT: {'FIRED' if F2_fired else 'did not fire'}.")
print(f"      {r1} independent cycles at grammar 1 depth<={DEPTH}, plus")
print("      two arms of grammar 2; every up-edge single-valued; every")
print("      holonomy exactly 1; every exchange square exactly 1.")
print("      => THE GENERATED LINE IS FLAT.  P1 dies on this substrate,")
print("         and D71 Clause 3's '+1' in the phase slot is a THEOREM")
print("         at the measured window, not an unargued choice.")

print()
print("  F3  'L_dual's dual-conjugation error on the generated line's")
print("      channels is non-zero.'")
print("      VERDICT: DOES NOT FIRE — and the reason is worse than a")
print("      failure would have been.  The error is EXACTLY 0 on v10's")
print("      channels, at k = 2, 3 and 4, on both domains and both orbit")
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
print("      VERDICT: NOT REACHED (vacuously false).  F2 removes its")
print("      premise: there is no defect at all (T2.4).  The holonomy")
print("      group is trivial, so the question 'R+ or U(1)?' has no")
print("      subject.  The founding slogan is refuted on this substrate")
print("      one step EARLIER than F4 anticipated.")


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
print("=" * 78)
print("""
[VERDICT] P1 IS REFUTED ON THE GENERATED LINE, and it is refuted at the
holonomy leg, not at the identification leg.

  T1  the reversal test .... the two reversals DO admit a common carrier
      (linear extensions; gated), they coincide EXACTLY on the F-PAIR
      fixture and nowhere else, and on that carrier A_D is identically
      zero: 'is A_D odd under *' answers YES with zero content.
  T2  the closure test ..... F2 FIRES.  sqrt(q)-transport around every
      delete-then-insert round trip of the record deletion graph returns
      exactly 1, on every independent cycle of two grammars and three
      arms.  There is no holonomy to be the phase of.
  T3  the L_dual re-run .... F3 does NOT fire: the dual-conjugation error
      is exactly 0 on v10's own channels — but T3.CTRL shows that 0 is an
      identity of the ansatz, not a fact about v10, and A2c shows v7's own
      1.82 control is the same closed form at E = 3.  The odd channel is
      SIGN-DEFINITE on every record (T3.B2), the family is not *-closed
      (T1.9), and on the v10-closed domain the odd-orbit even channel
      vanishes (T3.C).  The transfer is formal and empty of content.

  The weld is NOT made.  The honest residue: v7's odd channel and v6's
  A_D are not two halves of one object on this substrate — one of them is
  identically zero here and the other has no domain here.  What the unit
  buys is the no-go the pin pre-registered as F2: THE GENERATED LINE IS
  FLAT, so D71 Clause 3's '+1' is forced, not chosen, at the measured
  window.
""")
sys.exit(0)
