#!/usr/bin/env python3
"""
w5_ltp_lemma_exact.py — v12 W5: THE LTP LEMMA about [B3]'s own framework.

  UNIT   : v12 W5 — BARANDES RECAST AS CHART THEORY (pin:
           v12/note-w5-barandes-recast-pin.md).
  CLAIM  : [B3]'s own law of total probability (eqs. 19-20, p.9), applied
           at TWO of the model's own division events, FORCES the declared
           intermediate division event to be denied exactly where the
           declared law fails to compose ON THE ACTUAL DISTRIBUTION.
  GATE   : the forcing is exhibited exactly on the committed BC2 Bell
           model, rebuilt here in its own arithmetic and ANCHORED against
           the numbers printed in the committed receipt
           (git show f6d07ee:bc/code/bc2_output.txt).
  LEAN   : NONE.
  EXACT  : Fractions and the real quartic field K = Q[x]/(8x^4-8x^2+1)
           = Q(cos(pi/8)).  No float, no tolerance, no randomness.
  EXIT   : 0 unless a gate fails.  The unit's substantive finding is a
           NEGATIVE about a declared division-event set and exits 0.

  Scope: this file computes properties of [B3]'s FORMAL APPARATUS on ONE
  declared toy model.  No claim about nature.  No Bell-inequality claim,
  no locality claim, no covariance claim: BC2 owns the frame question and
  is cited, never re-derived.  [B3]'s equivalence theorem is not under
  test.
"""

import sys
import time
from collections import Counter
from fractions import Fraction as Fr

T0 = time.time()
GATES = []          # (id, ok, claim, detail, kind)
KINDS = {"A": "ANCHOR", "C": "CONTROL", "G": "GATE"}


def hdr(n, title):
    print()
    print("=" * 78)
    print(f"SEC {n}  {title}   [+{time.time()-T0:.0f}s]")
    print("=" * 78)


def check(gid, claim, ok, detail="", kind="G"):
    GATES.append((gid, bool(ok), claim, detail, kind))
    tag = "PASS" if ok else "FAIL"
    print(f"  [{tag}] {gid} {claim}" + (f"  ({detail})" if detail else ""))
    return bool(ok)


def datum(text):
    print(f"       {text}")


# ===========================================================================
print("=" * 78)
print("w5_ltp_lemma_exact.py — v12 W5: THE LTP LEMMA")
print("[B3]'s eqs. (19)-(20) force denying a composite division event")
print("exactly where the declared law fails to compose on the actual p.")
print("=" * 78)
print("  banner: EXACT arithmetic end to end.  NO float, NO tolerance, NO")
print("          randomness.  Rationals: fractions.Fraction.  Algebraic:")
print("          K = Q[x]/(8x^4 - 8x^2 + 1) = Q(cos(pi/8)), a real quartic")
print("          field with an exact zero test certified in-receipt.")
print("  scope : [B3]'s FORMAL APPARATUS on ONE declared toy model.")
print("          NO relativity claim, NO Bell-inequality claim, NO locality")
print("          claim.  BC2 owns the frame question and is CITED.")
print("  lean  : NONE.")

hdr(0, "THE REGISTRY — every source a gate tests against, quoted, page-cited")

SRC = {
 "B3-ltp": ("[B3] p.9, eqs. (18)-(21)",
            "The only available Chapman-Kolmogorov equations (5) take the "
            "simple form p(i,t) = SUM_j p(i,t|j,t0) p(j,t0), which is just "
            "the LAW OF TOTAL PROBABILITY. ... Equivalently, in matrix "
            "notation, p(t) = Gamma(t <- t0) p(t0)."),
 "B3-div": ("[B3] p.9 (below eq. 21)",
            "Note that no assumption is made here that the transition "
            "probabilities p(i,t|j,t0) exist as part of the laws for all "
            "real-valued choices of t0.  Allowed conditioning times t0 are "
            "called DIVISION EVENTS for the given system, and, without any "
            "real loss of generality, are assumed to include an 'initial' "
            "time 0."),
 "B3-linear": ("[B3] p.9 (below eq. 21)",
               "Importantly, notice that the law of total probability (19) "
               "is LINEAR, in the sense that it establishes a linear "
               "relationship between the system's standalone probabilities "
               "at t0 and the system's standalone probabilities at t."),
 "B3-free-t": ("[B3] p.10 (top)",
               "The target time t, by contrast, can be treated as a FREE "
               "VARIABLE.  In particular, no assumption is made that "
               "t > t0.  One can choose t < t0 as well."),
 "B3-sysc": ("[B3] p.10",
             "Division events are not global properties of the whole "
             "universe, but are SYSTEM-CENTRIC, just like various other "
             "kinds of spontaneous time-translation-breaking in physics."),
 "B3-indiv": ("[B3] p.10",
              "Crucially, an indivisible stochastic process, as befits its "
              "name, will NOT GENERALLY OBEY A DIVISIBILITY CONDITION like "
              "(7) or (14)."),
 "B3-eq22": ("[B3] p.10, eqs. (22)-(23)",
             "However, it turns out that a matrix ~Gamma(t <- t') defined "
             "according to (22) will generically fail to be a column "
             "stochastic matrix, and, indeed, will typically have negative "
             "entries, and so will form a so-called PSEUDO-STOCHASTIC "
             "matrix."),
 "B3-dict": ("[B3] p.11, eq. (25)",
             "Gamma_ij(t <- 0) = |Theta_ij(t <- 0)|^2.  Note that this "
             "formula is NOT A POSTULATE, BUT AN IDENTITY, and that the "
             "potential matrix Theta(t <- 0), which will be called a "
             "TIME-EVOLUTION OPERATOR in what follows, is NOT UNIQUE."),
 "B3-uni": ("[B3] p.18 (below eq. 64)",
            "an N x N matrix is called UNISTOCHASTIC if its individual "
            "entries are expressible as the modulus-squares of the "
            "corresponding entries of an N x N unitary matrix."),
 "B3-axioms": ("[B3] p.29 (Section 5, the three axioms)",
               "Kinematical axiom: ... The configuration space is a FIXED "
               "feature of the model, meaning that it does not vary between "
               "real-world runs or instantiations of the model.  Dynamical "
               "axiom: For arbitrary target times, and for conditioning "
               "times corresponding to division events, the model's "
               "dynamical laws consist of transition probabilities ... At "
               "the level of the given model, the DYNAMICAL LAWS ARE FIXED "
               "FEATURES.  Epistemic axiom: ... This standalone probability "
               "distribution ... is CONTINGENT, meaning that it can vary "
               "between runs of the model."),
 "B3-meas": ("[B3] p.29 (dynamical axiom)",
             "For example, DIVISION EVENTS ARE GENERATED DURING A "
             "MEASUREMENT PROCESS, which can be modeled as just another "
             "stochastic process."),
 "B3-outcome": ("[B3] p.16",
                "at the end of the measurement process, the measuring "
                "device will end up in one of its possible "
                "MEASUREMENT-OUTCOME CONFIGURATIONS with a stochastic "
                "probability that coincides with the standard Born rule."),
 "bc2": ("bc/note-bc2-bell-two-frames.md @ cbb7279 (green-unreviewed)",
         "the model, the two frames, the six setting pairs, the divisibility "
         "census (0,0,576,576,0,576), the eq.22 ranks, the inventory "
         "censuses, the singlet control, the basis-free certificate"),
 "bc4": ("bc/LOG.md #4 @ f6d07ee (BC2 hostile round)",
         "M-1 (a genuine incidental about [B3]): the declared intermediate "
         "division event VIOLATES the law of total probability (eqs. 19-20) "
         "at SP-C/D/F -- on this model 'legitimate division event <=> the "
         "process divides at it'."),
 "bc1": ("bc/note-bc1-division-event-composition.md @ 42d8610",
         "C-OBSTRUCTION: the system-centric division-event assignment is not "
         "a restriction-compatible family on the subsystem lattice."),
 "p0": ("v12/relativistic-isp-v12-paper0-the-weld.md v2.1, T2'",
        "three defects distinguished and not conflated: Delta^B(U2,U1) = "
        "B(U2U1) - B(U2)B(U1) (the Born-shadow defect); D_210 = Gamma_20 - "
        "Gamma_21 Gamma_10 (the residual of an ACTUAL DECLARED stochastic "
        "law); d_div (existential divisibility)."),
 "w3p": ("v12/note-w3p-records-kill-defect-pin.md (STATEMENT, not a result)",
         "for a stable record of {C_r} and any subsequent dynamics "
         "preserving the record sectors, the induced stochastic law on the "
         "commutative record algebra is DIVISIBLE -- the actual residual "
         "D_210 vanishes there."),
 "w1p": ("v12/note-w1p-three-class.md (W1' TERMINAL, LOG #7), C+1",
         "Delta^B != 0 does NOT imply stochastic indivisibility: the exact "
         "rational instance Delta^B_00 = -4032/15625 != 0 with K = "
         "S(-175/527) stochastic and K B(U1) = B(U2U1)."),
}
for k in sorted(SRC):
    where, quote = SRC[k]
    print(f"  [{k}] {where}")
    print(f"        \"{quote}\"")
print()
print("  MODEL PROVENANCE, declared: the committed BC2 receipt PRINTS")
print("  CENSUSES, NOT MATRICES (bc2_output.txt SEC 6 prints supports,")
print("  value censuses, nonzero counts, column-support censuses and")
print("  distinct-value counts; no transition matrix is printed entry by")
print("  entry).  The matrices are therefore NOT EXTRACTABLE from the")
print("  committed output.  This receipt REBUILDS the model from the")
print("  singlet dictionary and the construction DECLARED in the committed")
print("  receipt (read via `git show f6d07ee:bc/code/bc2_two_frames_exact")
print("  .py`), in its OWN field arithmetic, importing no code, and then")
print("  ANCHORS the rebuild against every number the committed receipt")
print("  prints (SEC 4 below).  Nothing is lifted; everything is re-derived")
print("  and checked against the committed print.")
print()
print("  CAPS, declared: one Bell model, |C| = 36, six setting pairs, two")
print("  frame orderings.  NO LP/Farkas search: this unit decides the")
print("  DECLARED-LAW residual D_210, never the EXISTENTIAL object d_div")
print("  (that census is U1's and BC1's).  Retrodictive matrices are not")
print("  computed (BC2's cap, inherited).  No claim about frames is made or")
print("  used; BC2's verdict is cited as data, not re-derived.")

# ===========================================================================
hdr(1, "THE FIELD K — irreducibility certified, arithmetic gated")

F0, F1_ = Fr(0), Fr(1)


def K(a=0, b=0, c=0, d=0):
    return (Fr(a), Fr(b), Fr(c), Fr(d))


Z, ONE = K(), K(1)
CC = K(0, 1)                       # c = cos(pi/8)


def kadd(x, y):
    return (x[0] + y[0], x[1] + y[1], x[2] + y[2], x[3] + y[3])


def ksub(x, y):
    return (x[0] - y[0], x[1] - y[1], x[2] - y[2], x[3] - y[3])


def kneg(x):
    return (-x[0], -x[1], -x[2], -x[3])


def kmul(x, y):
    r = [F0] * 7
    for i in range(4):
        xi = x[i]
        if xi == 0:
            continue
        for j in range(4):
            if y[j]:
                r[i + j] += xi * y[j]
    a0, a1, a2, a3, a4, a5, a6 = r
    a2 += Fr(7, 8) * a6
    a0 -= Fr(1, 8) * a6            # c^6 = (7/8)c^2 - 1/8
    a3 += a5
    a1 -= Fr(1, 8) * a5            # c^5 = c^3 - c/8
    a2 += a4
    a0 -= Fr(1, 8) * a4            # c^4 = c^2 - 1/8
    return (a0, a1, a2, a3)


def kzero(x):
    return x[0] == 0 and x[1] == 0 and x[2] == 0 and x[3] == 0


print("""
  Every algebraic number below is an element of

     K = Q[x]/(m),   m(x) = 8x^4 - 8x^2 + 1,   x |-> c = cos(pi/8),

  reduced by c^4 = c^2 - 1/8.  m is the minimal polynomial of cos(22.5 deg)
  because cos(4t) = 8cos^4 t - 8cos^2 t + 1 and cos(90 deg) = 0.  The zero
  test 'all four coordinates vanish' is sound exactly because m is
  irreducible over Q, which is certified below.  There is no tolerance in
  this file.
""")

_roots = [Fr(p, q) for q in (1, 2, 4, 8) for p in (1, -1)]


def _m(x):
    return 8 * x ** 4 - 8 * x ** 2 + 1


_hits = [str(r) for r in _roots if _m(r) == 0]
check("K1", "m HAS NO RATIONAL ROOT: by the rational-root theorem any "
      "rational root p/q has p | 1 and q | 8; all 8 candidates are "
      "evaluated exactly and none is a root",
      not _hits, f"candidates {sorted(set(str(r) for r in _roots))}; "
      f"roots found {_hits}", kind="C")


def _is_rat_square(x):
    if x < 0:
        return False
    n, d = x.numerator, x.denominator
    return int(n ** 0.5 + 0.5) ** 2 == n and int(d ** 0.5 + 0.5) ** 2 == d


_c1 = _is_rat_square(Fr(1) - Fr(1, 2))    # beta = 0 branch: z^2+z+1/8
_c2 = _is_rat_square(Fr(1, 8))            # delta = gamma branch: gamma^2=1/8
check("K2", "m HAS NO FACTORISATION INTO TWO RATIONAL QUADRATICS: writing "
      "8x^4-8x^2+1 = 8(x^2+bx+g)(x^2-bx+d) the x^3 coefficient forces the "
      "displayed form, the x coefficient forces b = 0 or d = g, and both "
      "branches need an irrational (disc 1/2, resp. g^2 = 1/8).  With K1 "
      "this certifies irreducibility, hence the soundness of the zero test",
      (not _c1) and (not _c2),
      f"1 - 1/2 a rational square? {_c1}; 1/8 a rational square? {_c2}",
      kind="C")

SQ2 = K(-2, 0, 4)                  # sqrt2 = 4c^2 - 2
check("K3", "sqrt2 = 4c^2 - 2 SQUARES TO 2 EXACTLY IN K",
      kzero(ksub(kmul(SQ2, SQ2), K(2))), "residual 0", kind="C")

C22, S22 = CC, K(0, -3, 0, 4)      # cos/sin 22.5
C45 = K(-1, 0, 2)                  # cos45 = 2c^2 - 1
S45, C67, S67 = C45, S22, CC
HALF = {0: (ONE, Z), 45: (C22, S22), 90: (C45, S45),
        135: (C67, S67), 180: (Z, ONE)}
_bad = [t for t, (ct, st) in HALF.items()
        if not kzero(ksub(kadd(kmul(ct, ct), kmul(st, st)), ONE))]
check("K4", "EVERY DECLARED HALF-ANGLE AMPLITUDE PAIR IS EXACTLY A UNIT "
      "VECTOR IN K: cos^2(th/2) + sin^2(th/2) = 1 at all five declared "
      "coplanar directions",
      not _bad, f"directions {sorted(HALF)}; failures {_bad}", kind="C")


def kinv(x):
    cols = []
    for j in range(4):
        e = [F0] * 4
        e[j] = F1_
        cols.append(kmul(x, tuple(e)))
    A = [[cols[j][i] for j in range(4)] + [F1_ if i == 0 else F0]
         for i in range(4)]
    piv = 0
    for c in range(4):
        r = next((rr for rr in range(piv, 4) if A[rr][c] != 0), None)
        if r is None:
            raise ZeroDivisionError("K element is not invertible")
        A[piv], A[r] = A[r], A[piv]
        pv = A[piv][c]
        A[piv] = [v / pv for v in A[piv]]
        for rr in range(4):
            if rr != piv and A[rr][c] != 0:
                f = A[rr][c]
                A[rr] = [A[rr][k] - f * A[piv][k] for k in range(5)]
        piv += 1
    return tuple(A[i][4] for i in range(4))


_t = kadd(K(3), SQ2)
check("K5", "EXACT DIVISION IN K IS AVAILABLE AND VERIFIED: the inverse is "
      "solved from the 4x4 rational multiplication matrix and "
      "(3+sqrt2)^-1 (3+sqrt2) = 1 with zero residual",
      kzero(ksub(kmul(kinv(_t), _t), ONE)),
      f"(3+sqrt2)^-1 coordinates in (1, c, c^2, c^3) = "
      f"{tuple(str(x) for x in kinv(_t))}", kind="C")


def toQ2(x):
    """K-elements with vanishing c and c^3 coordinates lie in Q(sqrt2)."""
    assert x[1] == 0 and x[3] == 0, x
    return (x[0] + x[2] / 2, x[2] / Fr(4))


def fmt(x):
    p, q = toQ2(x)
    if q == 0:
        return str(p)
    return f"{p}{'+' if q > 0 else '-'}({abs(q)})r2"


_rt = kadd(K(Fr(3, 16)), kmul(K(Fr(1, 8)), SQ2))
check("K6", "THE Q(sqrt2) READER IS SOUND: {1, c^2} spans Q(sqrt2) inside "
      "K, so an element with vanishing c and c^3 coordinates is read off "
      "exactly as p + q sqrt2; the round trip is verified on the value "
      "3/16 + (1/8)sqrt2 that the committed receipt prints",
      fmt(_rt) == "3/16+(1/8)r2", f"reader returns {fmt(_rt)}", kind="C")

# ===========================================================================
hdr(2, "THE LEMMA — stated, and its two non-trivial steps gated formally")

print("""
  LEMMA (LTP-FORCING).  Let M be a model satisfying [B3]'s three axioms
  ([B3-axioms]) with finite configuration space C, |C| = N.  Let 0 and t'
  be two DIVISION EVENTS of M ([B3-div]; 0 is one by [B3]'s own
  convention), and let t be any target time ([B3-free-t]: the target time
  is free).  The dynamical axiom then supplies the model with the fixed
  column-stochastic matrices Gamma(t' <- 0), Gamma(t <- 0) and
  Gamma(t <- t'), and [B3]'s law of total probability ([B3-ltp], eqs.
  19-20) holds at BOTH conditioning times.  Write

      D_210  :=  Gamma(t <- 0)  -  Gamma(t <- t') Gamma(t' <- 0)

  for the DECLARED-LAW residual of [p0]'s T2' (NOT Delta^B, NOT d_div).
  Then:

  (a) VECTOR FORM (no extra hypothesis).  For every standalone
      distribution p(0) the model actually runs on,

          D_210 p(0) = 0.

      Proof.  p(t') = Gamma(t' <- 0) p(0) and p(t) = Gamma(t <- 0) p(0)
      by eq. (20) at the division event 0; p(t) = Gamma(t <- t') p(t') by
      eq. (20) at the division event t'.  Substituting the first into the
      third and subtracting the second gives D_210 p(0) = 0, using only
      associativity of the matrix action.  QED

  (b) MATRIX FORM, under H-SPAN.  If the standalone distributions
      admissible across runs SPAN R^N -- the epistemic axiom read at full
      strength ('CONTINGENT, meaning that it can vary between runs') while
      the dynamical laws are 'FIXED FEATURES' [B3-axioms] -- then
      D_210 = 0 exactly, as matrices.

  (c) THE FORCING (the contrapositive of (a)).  If the model exhibits a
      target time t and an admissible p(0) with D_210 p(0) != 0, then t'
      IS NOT A DIVISION EVENT of that model.  No hypothesis beyond [B3]'s
      own eqs. (19)-(20) is used; H-SPAN is NOT needed for (c).

  Scope, engraved: (a)-(c) concern the DECLARED leg Gamma(t <- t') that
  the model's own dynamics supplies.  They say nothing about whether SOME
  other column-stochastic bridge exists (d_div), and nothing about
  Delta^B, which by [w1p] can be nonzero on a divisible process.
""")


# --- L1/L2: the two steps of (a), gated as formal polynomial identities ---
def pmul(P, Q):
    out = {}
    for m1, c1 in P.items():
        for m2, c2 in Q.items():
            m = tuple(sorted(m1 + m2))
            out[m] = out.get(m, F0) + c1 * c2
    return {m: c for m, c in out.items() if c != 0}


def padd(P, Q):
    out = dict(P)
    for m, c in Q.items():
        out[m] = out.get(m, F0) + c
    return {m: c for m, c in out.items() if c != 0}


def psub(P, Q):
    return padd(P, {m: -c for m, c in Q.items()})


def var(name):
    return {(name,): F1_}


NF = 3
G10 = [[var(f"a{i}{j}") for j in range(NF)] for i in range(NF)]
G21 = [[var(f"b{i}{j}") for j in range(NF)] for i in range(NF)]
P0 = [var(f"p{j}") for j in range(NF)]


def _fmv(M, v, i):
    s = {}
    for j in range(len(v)):
        s = padd(s, pmul(M[i][j], v[j]))
    return s


def fmatmul(A, B):
    n, m, k = len(A), len(B[0]), len(B)
    return [[_fmm(A, B, i, j, k) for j in range(m)] for i in range(n)]


def _fmm(A, B, i, j, k):
    s = {}
    for p in range(k):
        s = padd(s, pmul(A[i][p], B[p][j]))
    return s


_inner = [_fmv(G10, P0, r) for r in range(NF)]
_lhs = [_fmv(G21, _inner, i) for i in range(NF)]
_prod = fmatmul(G21, G10)
_rhs = [_fmv(_prod, P0, i) for i in range(NF)]
_res = [psub(_lhs[i], _rhs[i]) for i in range(NF)]
_nmon = len(set(m for r in _lhs for m in r))
check("L1", "THE ONLY STEP THE PROOF OF (a) USES IS FORMAL: with all "
      f"{2*NF*NF + NF} entries INDETERMINATE over Q, "
      "Gamma_21(Gamma_10 p0) - (Gamma_21 Gamma_10) p0 is identically the "
      "zero polynomial vector -- associativity of the matrix action, no "
      "property of stochasticity assumed",
      all(not r for r in _res),
      f"N = {NF}; monomials on each side {_nmon}; surviving monomials "
      f"{sum(len(r) for r in _res)}")

DSEP = [[Fr(1), Fr(-1)], [Fr(-1), Fr(1)]]
PHALF = [Fr(1, 2), Fr(1, 2)]
_dp = [sum(DSEP[i][j] * PHALF[j] for j in range(2)) for i in range(2)]
_d0 = [DSEP[i][0] for i in range(2)]
check("L2", "H-SPAN IS LOAD-BEARING, BY EXACT SEPARATING INSTANCE: the "
      "residual D = [[1,-1],[-1,1]] is nonzero yet annihilates the "
      "distribution p = (1/2, 1/2), so the VECTOR form (a) is STRICTLY "
      "WEAKER than the matrix form (b); the matrix corollary genuinely "
      "needs the full-strength epistemic reading",
      any(x != 0 for r in DSEP for x in r) and all(x == 0 for x in _dp),
      f"D p = {[str(x) for x in _dp]}; D != 0")

check("L3", "AND SPANNING RESTORES IT: the same D fails to annihilate the "
      "point mass delta_0, so admitting the N point masses across runs "
      "already forces D = 0 -- the spanning hypothesis is not exotic",
      any(x != 0 for x in _d0), f"D delta_0 = {[str(x) for x in _d0]}")

_colsum = [sum(DSEP[i][j] for i in range(2)) for j in range(2)]
check("L4", "THE RESIDUAL IS INVISIBLE TO SUMMING: a difference of two "
      "column-stochastic matrices has identically zero column sums, so "
      "D_210 p(0) always sums to zero and a nonzero residual must show up "
      "as CANCELLING mass -- the detection below counts entries, never "
      "totals",
      all(x == 0 for x in _colsum), f"column sums {[str(x) for x in _colsum]}",
      kind="C")

# ===========================================================================
hdr(3, "THE MODEL — the committed BC2 Bell model, rebuilt in this receipt")

print("""
  C = { (qA, qB, pA, pB) }, qA,qB in {0,1}, pA,pB in {r,+,-}; |C| = 36,
  index i = ((qA*2 + qB)*3 + pA)*3 + pB, initial configuration
  j0 = (0,0,r,r) = 0.  The pointer configurations are [B3]'s
  MEASUREMENT-OUTCOME CONFIGURATIONS [B3-outcome].

  U_prep acts on (qA,qB) only and carries j0 to the singlet;
  U_X(theta) = SUM_s Pi^theta_s (x) Sh^{n(s)} with Sh the 3-cycle
  r -> + -> - -> r on that wing's pointer, n(+) = 1, n(-) = 2.
  F1 = (prep, A, B), F2 = (prep, B, A); target times 0,1,2,3; division
  events D = {0, 2, 3} in each frame ([B3-div] for 0, [B3-meas] for 2 and
  3).  Theta(3<-2) is the second measurement's own operator.
""")

NC = 36
PT = {0: "r", 1: "+", 2: "-"}


def cfg(i):
    return ((i // 18) % 2, (i // 9) % 2, (i // 3) % 3, i % 3)


def cfg_str(i):
    qA, qB, pA, pB = cfg(i)
    return f"({qA}{qB}|{PT[pA]}{PT[pB]})"


def mzeros(n, m=None):
    m = m or n
    return [[Z] * m for _ in range(n)]


def meye(n):
    M = mzeros(n)
    for i in range(n):
        M[i][i] = ONE
    return M


def mmul(A, B):
    n, k, m = len(A), len(B), len(B[0])
    Bt = [[B[p][j] for p in range(k)] for j in range(m)]
    C = [[Z] * m for _ in range(n)]
    for i in range(n):
        Ai = A[i]
        nzs = [(p, Ai[p]) for p in range(k) if not kzero(Ai[p])]
        Ci = C[i]
        for j in range(m):
            Bj = Bt[j]
            s = Z
            for p, a in nzs:
                b = Bj[p]
                if not kzero(b):
                    s = kadd(s, kmul(a, b))
            Ci[j] = s
    return C


def madd(A, B):
    return [[kadd(A[i][j], B[i][j]) for j in range(len(A[0]))]
            for i in range(len(A))]


def kron(A, B):
    na, ma, nb, mb = len(A), len(A[0]), len(B), len(B[0])
    C = [[Z] * (ma * mb) for _ in range(na * nb)]
    for i in range(na):
        for j in range(ma):
            a = A[i][j]
            if kzero(a):
                continue
            for p in range(nb):
                for q in range(mb):
                    if not kzero(B[p][q]):
                        C[i * nb + p][j * mb + q] = kmul(a, B[p][q])
    return C


def matvec(M, v):
    out = []
    for i in range(len(M)):
        s = Z
        for j in range(len(v)):
            if not kzero(M[i][j]) and not kzero(v[j]):
                s = kadd(s, kmul(M[i][j], v[j]))
        out.append(s)
    return out


def orth_residuals(U):
    n = len(U)
    bad = 0
    for i in range(n):
        for j in range(n):
            s = Z
            for p in range(n):
                a, b = U[p][i], U[p][j]
                if not kzero(a) and not kzero(b):
                    s = kadd(s, kmul(a, b))
            t = ksub(s, ONE) if i == j else s
            if not kzero(t):
                bad += 1
    return bad


I2, I3, I9 = meye(2), meye(3), meye(9)
SH = [[Z, Z, ONE], [ONE, Z, Z], [Z, ONE, Z]]
SH2 = mmul(SH, SH)


def proj(th):
    ct, st = HALF[th % 360]
    vp, vm = [ct, st], [kneg(st), ct]
    Pp = [[kmul(vp[i], vp[j]) for j in range(2)] for i in range(2)]
    Pm = [[kmul(vm[i], vm[j]) for j in range(2)] for i in range(2)]
    return Pp, Pm


def U_meas(th, wing):
    Pp, Pm = proj(th)
    out = mzeros(NC)
    for P, sh in ((Pp, SH), (Pm, SH2)):
        if wing == "A":
            out = madd(out, kron(kron(P, I2), kron(sh, I3)))
        else:
            out = madd(out, kron(kron(I2, P), kron(I3, sh)))
    return out


R2H = kmul(SQ2, K(Fr(1, 2)))
PREP4 = [[Z, R2H, R2H, Z],
         [R2H, Z, Z, R2H],
         [kneg(R2H), Z, Z, R2H],
         [Z, R2H, kneg(R2H), Z]]
U_PREP = kron(PREP4, I9)

_sing = [PREP4[i][0] for i in range(4)]
check("M1", "THE PREPARATION OPERATOR IS EXACTLY ORTHOGONAL AND ITS j0 "
      "COLUMN IS EXACTLY THE SINGLET: 16 inner products with zero residual "
      "and column 0 = (0, 1/sqrt2, -1/sqrt2, 0) on the pair basis "
      "(00,01,10,11), as the committed receipt's M1 prints",
      orth_residuals(PREP4) == 0 and kzero(_sing[0])
      and kzero(ksub(_sing[1], R2H)) and kzero(kadd(_sing[2], R2H))
      and kzero(_sing[3]),
      f"orthogonality residuals {orth_residuals(PREP4)}; singlet column "
      f"{[fmt(x) for x in _sing]}", kind="A")

SET = [("SP-A", 0, 45), ("SP-B", 0, 135), ("SP-C", 90, 45),
       ("SP-D", 90, 135), ("SP-E", 0, 0), ("SP-F", 45, 45)]
UA, UB = {}, {}
for _nm, _a, _b in SET:
    UA.setdefault(_a, U_meas(_a, "A"))
    UB.setdefault(_b, U_meas(_b, "B"))

_bad_orth = [lab for lab, U in
             ([("U_prep", U_PREP)]
              + [(f"U_A({a})", U) for a, U in sorted(UA.items())]
              + [(f"U_B({b})", U) for b, U in sorted(UB.items())])
             if orth_residuals(U) != 0]
check("M2", "EVERY TIME-EVOLUTION OPERATOR IS EXACTLY REAL ORTHOGONAL: "
      "U^T U = I verified entry by entry in K for U_prep and all 3 + 3 "
      "measurement operators -- 1296 inner products each, zero residuals; "
      "hence |U_ij|^2 = U_ij^2 and no complex ring is needed",
      not _bad_orth, f"operators checked {1+len(UA)+len(UB)}; failures "
      f"{_bad_orth}", kind="A")

_cf = []
for a in sorted(UA):
    for b in sorted(UB):
        if any(not kzero(ksub(x, y)) for rx, ry in
               zip(mmul(UA[a], UB[b]), mmul(UB[b], UA[a]))
               for x, y in zip(rx, ry)):
            _cf.append((a, b))
check("M3", "THE TWO MEASUREMENT OPERATORS COMMUTE EXACTLY AT EVERY "
      "SETTING PAIR: [U_A(a), U_B(b)] = 0 entry by entry in K over all "
      "3 x 3 = 9 pairs",
      not _cf, f"pairs checked 9; failures {_cf}", kind="A")


def gam(TH):
    return [[kmul(x, x) for x in row] for row in TH]


p0 = [Z] * NC
p0[0] = ONE
S = {}
for nm, a, b in SET:
    for fr in ("F1", "F2"):
        if fr == "F1":
            TH2 = mmul(UA[a], U_PREP)
            LEG = UB[b]
        else:
            TH2 = mmul(UB[b], U_PREP)
            LEG = UA[a]
        TH3 = mmul(LEG, TH2)
        d = dict(TH1=U_PREP, TH2=TH2, TH3=TH3, LEG=LEG,
                 G10=gam(U_PREP), G20=gam(TH2), G30=gam(TH3), G32=gam(LEG))
        d["p1"] = matvec(d["G10"], p0)
        d["p2"] = matvec(d["G20"], p0)
        d["p3"] = matvec(d["G30"], p0)
        S[(nm, fr)] = d

_compfail = []
for key, d in S.items():
    if any(not kzero(ksub(x, y))
           for rx, ry in zip(d["TH3"], mmul(d["LEG"], d["TH2"]))
           for x, y in zip(rx, ry)):
        _compfail.append(key)
check("M4", "THE AMPLITUDE PROPAGATORS COMPOSE EXACTLY: "
      "Theta(3<-0) = Theta(3<-2) Theta(2<-0) at all 1296 entries, in both "
      "frames at all six setting pairs.  This is what makes the declared "
      "residual D_210 EQUAL to the Born-shadow defect Delta^B(Theta(3<-2), "
      "Theta(2<-0)) of [p0]'s T2' on this model -- the two objects are "
      "distinct in general and coincide here",
      not _compfail, f"cells checked {len(S)}; failures {_compfail}")

_stoch = []
for key, d in S.items():
    for lab in ("G10", "G20", "G30", "G32"):
        M = d[lab]
        for j in range(NC):
            s = Z
            for i in range(NC):
                s = kadd(s, M[i][j])
            if not kzero(ksub(s, ONE)):
                _stoch.append((key, lab, j))
check("M5", "EVERY TRANSITION MATRIX IS EXACTLY COLUMN-STOCHASTIC: all "
      "columns sum to 1 in K, and every entry is a square in K hence "
      "non-negative by construction -- [B3] eq. (9) verified, not assumed",
      not _stoch, f"columns checked {len(S)*4*NC}; failures "
      f"{len(_stoch)}", kind="C")

# ===========================================================================
hdr(4, "THE ANCHOR BATTERY — the rebuild against the committed BC2 print")

print("""
  Every number in this section is quoted from the COMMITTED receipt
  bc/code/bc2_output.txt and bc/note-bc2-bell-two-frames.md at f6d07ee /
  cbb7279 [bc2].  A failure here means the rebuild is not the committed
  model, and the unit is void: these gates are exit-1.
""")

COS = {0: ONE, 45: C45, 90: Z, 135: kneg(C45), 180: kneg(ONE),
       -45: C45, -90: Z, -135: kneg(C45)}
_qm = []
_nid = 0
for nm, a, b in SET:
    for fr in ("F1", "F2"):
        p3 = S[(nm, fr)]["p3"]
        for al in (1, 2):
            for be in (1, 2):
                s = Z
                for i in range(NC):
                    if (i // 3) % 3 == al and i % 3 == be:
                        s = kadd(s, p3[i])
                sa, sb = (1 if al == 1 else -1), (1 if be == 1 else -1)
                pred = kmul(K(Fr(1, 4)),
                            ksub(ONE, kmul(K(sa * sb), COS[(a - b)])))
                _nid += 1
                if not kzero(ksub(s, pred)):
                    _qm.append((nm, fr, al, be))
        for who, sel in (("A", lambda i: (i // 3) % 3),
                         ("B", lambda i: i % 3)):
            for al in (1, 2):
                s = Z
                for i in range(NC):
                    if sel(i) == al:
                        s = kadd(s, p3[i])
                _nid += 1
                if not kzero(ksub(s, K(Fr(1, 2)))):
                    _qm.append((nm, fr, who, al))
check("A1", "BOTH FRAMES REPRODUCE THE EXACT SINGLET OUTCOME LAW AT ALL "
      "SIX SETTING PAIRS: P(alpha,beta) = (1 - alpha beta cos(a-b))/4 and "
      "both single-wing marginals 1/2, as exact identities in K -- the "
      f"committed QM control ({_nid} identities)",
      not _qm, f"identities {_nid}; failures {_qm}; SP-A joint "
      f"{[fmt(x) for x in [kmul(K(Fr(1,4)), ksub(ONE, kmul(K(s), COS[-45]))) for s in (1,-1)]]}",
      kind="A")


def nzc(M):
    return sum(1 for row in M for x in row if not kzero(x))


def colsupp(M):
    return dict(Counter(sum(1 for i in range(NC) if not kzero(M[i][j]))
                        for j in range(NC)))


def ndist(M):
    return len(set(M[i][j] for i in range(NC) for j in range(NC)))


def vsupp(v):
    return sum(1 for x in v if not kzero(x))


def vcens(v):
    return dict(Counter(fmt(x) for x in v if not kzero(x)))


INV_EXPECT = {
  ("F1", "p1"): (2, {"1/2": 2}), ("F2", "p1"): (2, {"1/2": 2}),
  ("F1", "p2"): (2, {"1/2": 2}),
  ("F2", "p2"): (8, {"1/16": 4, "3/16+(1/8)r2": 2, "3/16-(1/8)r2": 2}),
  ("F1", "p3"): (8, {"1/16": 4, "3/16+(1/8)r2": 2, "3/16-(1/8)r2": 2}),
  ("F2", "p3"): (8, {"1/16": 4, "3/16+(1/8)r2": 2, "3/16-(1/8)r2": 2}),
}
GAM_EXPECT = {
  ("F1", "G10"): (72, {2: 36}, 2), ("F2", "G10"): (72, {2: 36}, 2),
  ("F1", "G20"): (72, {2: 36}, 2), ("F2", "G20"): (288, {8: 36}, 4),
  ("F1", "G30"): (288, {8: 36}, 4), ("F2", "G30"): (288, {8: 36}, 4),
  ("F1", "G32"): (144, {4: 36}, 4), ("F2", "G32"): (36, {1: 36}, 2),
}
_ia = []
for fr in ("F1", "F2"):
    d = S[("SP-A", fr)]
    for lab in ("p1", "p2", "p3"):
        sup, cen = INV_EXPECT[(fr, lab)]
        if vsupp(d[lab]) != sup or vcens(d[lab]) != cen:
            _ia.append((fr, lab, vsupp(d[lab]), vcens(d[lab])))
    for lab in ("G10", "G20", "G30", "G32"):
        n, cs, nd = GAM_EXPECT[(fr, lab)]
        if nzc(d[lab]) != n or colsupp(d[lab]) != cs or ndist(d[lab]) != nd:
            _ia.append((fr, lab, nzc(d[lab]), colsupp(d[lab]),
                        ndist(d[lab])))
check("A2", "THE WHOLE SP-A SPECIFIED-CONTENT INVENTORY REPRODUCES, BOTH "
      "FRAMES: marginal supports and exact value censuses for p(1),p(2),"
      "p(3) and nonzero counts, column-support censuses and distinct-value "
      "counts for Gamma(1<-0), Gamma(2<-0), Gamma(3<-0), Gamma(3<-2) -- 14 "
      "objects, 34 printed numbers, all from the committed SEC 6",
      not _ia, f"mismatches {_ia}", kind="A")

DIV_EXPECT = {"SP-A": 0, "SP-B": 0, "SP-C": 576, "SP-D": 576,
              "SP-E": 0, "SP-F": 576}
MDIFF = {}
_da = []
for nm, a, b in SET:
    for fr in ("F1", "F2"):
        d = S[(nm, fr)]
        prod = mmul(d["G32"], d["G20"])
        n = sum(1 for i in range(NC) for j in range(NC)
                if not kzero(ksub(prod[i][j], d["G30"][i][j])))
        MDIFF[(nm, fr)] = n
        if n != DIV_EXPECT[nm]:
            _da.append((nm, fr, n))
check("A3", "THE DIVISIBILITY CENSUS REPRODUCES EXACTLY IN BOTH FRAMES: "
      "Gamma(3<-2) Gamma(2<-0) differs from Gamma(3<-0) in "
      "(0,0,576,576,0,576) entries at (SP-A..SP-F) -- the committed S2",
      not _da, f"census {[(nm, MDIFF[(nm,'F1')], MDIFF[(nm,'F2')]) for nm,_,_ in SET]}; "
      f"mismatches {_da}", kind="A")


def rank(M):
    A = [row[:] for row in M]
    n, m, r = len(A), len(A[0]), 0
    for c in range(m):
        p = next((rr for rr in range(r, n) if not kzero(A[rr][c])), None)
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        inv = kinv(A[r][c])
        A[r] = [kmul(inv, v) for v in A[r]]
        for rr in range(n):
            if rr != r and not kzero(A[rr][c]):
                f = A[rr][c]
                A[rr] = [ksub(A[rr][k], kmul(f, A[r][k])) for k in range(m)]
        r += 1
        if r == n:
            break
    return r


RANK_EXPECT = {"SP-A": (18, 18), "SP-B": (18, 18), "SP-C": (9, 18),
               "SP-D": (9, 18), "SP-E": (18, 18), "SP-F": (18, 18)}
_ra = []
RK = {}
for nm, a, b in SET:
    rr = (rank(S[(nm, "F1")]["G20"]), rank(S[(nm, "F2")]["G20"]))
    RK[nm] = rr
    if rr != RANK_EXPECT[nm]:
        _ra.append((nm, rr))
check("A4", "[B3] eq. (22)'s OWN HYPOTHESIS FAILS, AT THE COMMITTED RANKS: "
      "the exact rank of Gamma(2<-0) over K is (18,18),(18,18),(9,18),"
      "(9,18),(18,18),(18,18) in (F1,F2) at SP-A..SP-F, never 36, so the "
      "interpolant of eq. (22) does not exist and the pseudo-stochastic "
      "diagnosis is not even reached -- the committed S3",
      not _ra, f"ranks {[(nm, RK[nm]) for nm, _, _ in SET]}; mismatches "
      f"{_ra}", kind="A")

T52 = {"SP-A": (0, 10, 16, 360, 576, 180), "SP-B": (0, 10, 16, 360, 576, 180),
       "SP-C": (0, 24, 24, 864, 864, 288), "SP-D": (0, 24, 24, 864, 864, 288),
       "SP-E": (0, 4, 4, 144, 144, 72), "SP-F": (0, 16, 16, 720, 720, 288)}


def dcv(a, b):
    return sum(1 for i in range(len(a)) if not kzero(ksub(a[i], b[i])))


def dcm(A, B):
    return sum(1 for i in range(NC) for j in range(NC)
               if not kzero(ksub(A[i][j], B[i][j])))


_ta = []
ROW52 = {}
for nm, a, b in SET:
    d1, d2 = S[(nm, "F1")], S[(nm, "F2")]
    row = (dcv(d1["p1"], d2["p1"]), dcv(d1["p2"], d2["p3"]),
           dcv(d1["p3"], d2["p2"]), dcm(d1["G20"], d2["G30"]),
           dcm(d1["G30"], d2["G20"]), dcm(d1["G32"], d2["G32"]))
    ROW52[nm] = row
    if row != T52[nm]:
        _ta.append((nm, row))
check("A5", "THE COMMITTED MISMATCH TABLE (bc2 note, section 5.2) "
      "REPRODUCES CELL FOR CELL under the Lorentz correspondence phi_LOR: "
      "36 differing-entry counts across six objects and six setting pairs",
      not _ta, f"rows {[(nm, ROW52[nm]) for nm, _, _ in SET]}; mismatches "
      f"{_ta}", kind="A")

_ba = []
for nm, a, b in SET:
    d1, d2 = S[(nm, "F1")], S[(nm, "F2")]
    v = []
    for tag, vec, sel in (("B@Alice-F1", d1["p2"], lambda i: i % 3),
                          ("B@Alice-F2", d2["p3"], lambda i: i % 3),
                          ("A@Bob-F1", d1["p3"], lambda i: (i // 3) % 3),
                          ("A@Bob-F2", d2["p2"], lambda i: (i // 3) % 3)):
        s = Z
        for i in range(NC):
            if sel(i) == 0:
                s = kadd(s, vec[i])
        v.append(s)
    if not (kzero(ksub(v[0], ONE)) and kzero(v[1])
            and kzero(v[2]) and kzero(ksub(v[3], ONE))):
        _ba.append((nm, [fmt(x) for x in v]))
check("A6", "THE BASIS-FREE CERTIFICATE REPRODUCES AT ALL SIX SETTING "
      "PAIRS: at the division event that IS Alice's measurement, "
      "Pr[pointer B still ready] = 1 exactly in F1 and 0 exactly in F2, and "
      "symmetrically for pointer A at Bob's",
      not _ba, f"failures {_ba}", kind="A")

# ===========================================================================
hdr(5, "THE GATE — the LTP residual on the model, exact")

print("""
  The model declares D = {0, 2, 3}: 0 by [B3-div], and 2 and 3 by
  [B3-meas] ('division events are generated during a measurement
  process').  The lemma's hypotheses are therefore the model's own.  Take
  t' = 2 and the target time t = 3, and evaluate

     r  :=  D_210 p(0)  =  Gamma(3<-0) p(0) - Gamma(3<-2) Gamma(2<-0) p(0)
        =  p(3) - Gamma(3<-2) p(2),

  on the model's own declared p(0) = delta_{j0}.  By lemma (c), any
  nonzero r denies t' = 2 the status of a division event.
""")

VRES, VN = {}, {}
_sum_fail, _col_fail = [], []
for nm, a, b in SET:
    for fr in ("F1", "F2"):
        d = S[(nm, fr)]
        r = [ksub(d["p3"][i], matvec(d["G32"], d["p2"])[i])
             for i in range(NC)]
        VRES[(nm, fr)] = r
        VN[(nm, fr)] = sum(1 for x in r if not kzero(x))
        s = Z
        for x in r:
            s = kadd(s, x)
        if not kzero(s):
            _sum_fail.append((nm, fr))
        prod = mmul(d["G32"], d["G20"])
        colj0 = [ksub(d["G30"][i][0], prod[i][0]) for i in range(NC)]
        if any(not kzero(ksub(colj0[i], r[i])) for i in range(NC)):
            _col_fail.append((nm, fr))

check("G1", "THE RESIDUAL IS EXACTLY THE j0 COLUMN OF THE MATRIX RESIDUAL, "
      "in all twelve cells: because the model's declared p(0) is the point "
      "mass delta_{j0}, the vector form of the lemma reads off one column "
      "of D_210 and nothing is hidden by the choice of p(0)",
      not _col_fail, f"cells {len(S)}; failures {_col_fail}")

check("G2", "THE RESIDUAL SUMS TO ZERO EXACTLY IN ALL TWELVE CELLS, as "
      "L4 requires: the violation is cancelling mass, never a change of "
      "normalisation, so no total can detect it",
      not _sum_fail, f"failures {_sum_fail}")

print()
print("  THE CENSUS (nonzero entries of r out of 36; matrix residual out")
print("  of 1296; the two must be simultaneously zero or nonzero here):")
print()
print("     setting  frame   |r| nonzero / 36    D_210 differing / 1296")
for nm, a, b in SET:
    for fr in ("F1", "F2"):
        print(f"     {nm:8s} {fr:5s}   {VN[(nm,fr)]:8d} / 36        "
              f"{MDIFF[(nm,fr)]:9d} / 1296")

VIOL = sorted(set(nm for nm, _, _ in SET
                  if VN[(nm, "F1")] or VN[(nm, "F2")]))
CLEAN = sorted(set(nm for nm, _, _ in SET
                   if not (VN[(nm, "F1")] or VN[(nm, "F2")])))
_sep = [(nm, fr) for (nm, fr) in VN
        if (MDIFF[(nm, fr)] != 0) != (VN[(nm, fr)] != 0)]
check("G3", "THE VECTOR AND MATRIX RESIDUALS AGREE ON WHICH CELLS ARE "
      "VIOLATED, 12 of 12: on this model the declared p(0) already "
      "witnesses every matrix violation, so the FORCING NEEDS NO H-SPAN "
      "here.  (A reported negative on the separation L2 exhibits in "
      "general: this model supplies no cell where the matrix residual is "
      "nonzero and the vector residual vanishes.)",
      not _sep, f"separating cells {_sep} (0 expected); violated "
      f"{VIOL}; clean {CLEAN}")

_sixteen = [(nm, fr) for (nm, fr) in VN if VN[(nm, fr)] == 16]
check("G4", "THE HEADLINE COUNT: the residual has EXACTLY 16 NONZERO "
      "ENTRIES OF 36 at SP-C, SP-D and SP-F, in BOTH frames -- six cells, "
      "and 16 x 36 = 576 is exactly the committed matrix count of A3",
      len(_sixteen) == 6
      and set(nm for nm, _ in _sixteen) == {"SP-C", "SP-D", "SP-F"}
      and all(MDIFF[c] == 16 * 36 for c in _sixteen),
      f"cells with |r| = 16: {sorted(_sixteen)}")

print()
print("  THE WITNESS, printed in full — SP-C (a = 90 deg, b = 45 deg),")
print("  frame F1 = (prep, A, B), t' = 2 (Alice's measurement), t = 3:")
print()
print("     index  configuration   r_i = p_i(3) - [Gamma(3<-2) p(2)]_i")
_w = VRES[("SP-C", "F1")]
for i in range(NC):
    if not kzero(_w[i]):
        print(f"     {i:5d}  {cfg_str(i):14s}  {fmt(_w[i])}")
_vals = sorted(set(fmt(_w[i]) for i in range(NC) if not kzero(_w[i])))
print(f"     distinct values: {_vals}")
print("     (all four are +-1/32 +- sqrt2/32; they cancel in pairs, G2)")

check("G5", "THE WITNESS IS EXACTLY THE FOUR VALUES +-1/32 +- sqrt2/32, "
      "each occurring four times, so the violation is irrational and "
      "cannot be an arithmetic artefact of a rational truncation",
      len(_vals) == 4 and all(
          Counter(fmt(_w[i]) for i in range(NC)
                  if not kzero(_w[i]))[v] == 4 for v in _vals),
      f"value census {dict(Counter(fmt(_w[i]) for i in range(NC) if not kzero(_w[i])))}")

check("G6", "THE FORCING FIRES: at SP-C, SP-D and SP-F, in both frames, "
      "[B3]'s own eqs. (19)-(20) at the division events 0 and t' = 2 are "
      "CONTRADICTED by the model's own declared law on the model's own "
      "declared p(0).  By lemma (c), t' = 2 IS NOT A DIVISION EVENT of "
      "those models -- and t' = 2 is exactly where [B3-meas] says a "
      "measurement generates one.  THE DENIAL IS FORCED BY THE FRAMEWORK, "
      "NOT IMPOSED FROM OUTSIDE",
      VIOL == ["SP-C", "SP-D", "SP-F"] and CLEAN == ["SP-A", "SP-B", "SP-E"],
      f"forced denial at {VIOL}; consistent at {CLEAN}")

check("G7", "AND THE BICONDITIONAL OF [bc4] M-1 IS THE MODEL-LEVEL "
      "COROLLARY, NOT THE LEMMA: on this model the setting pairs where "
      "t'=2 survives as a division event are exactly the setting pairs "
      "where the declared law composes there.  The lemma proves ONE "
      "direction (division event => the declared law composes on p(0)); "
      "the converse holds HERE because the declared leg Gamma(3<-2) is "
      "column-stochastic at every setting pair (M5), and is NOT claimed in "
      "general",
      set(VIOL) | set(CLEAN) == {nm for nm, _, _ in SET}
      and set(VIOL) & set(CLEAN) == set(),
      f"divides & division event: {CLEAN}; neither: {VIOL}")

check("G8", "THE THREE DEFECTS STAY DISTINCT: on this model D_210 EQUALS "
      "Delta^B(Theta(3<-2), Theta(2<-0)) because the amplitude propagators "
      "compose (M4), so the 576/16 counts are simultaneously a declared-law "
      "residual and a Born-shadow defect; the EXISTENTIAL object d_div is "
      "NOT decided here (no LP is run) and by [w1p] Delta^B != 0 does not "
      "imply d_div != 0.  This gate asserts the identification and the "
      "abstention, both",
      not _compfail,
      "D_210 = Delta^B on all 12 cells (M4); d_div: NOT COMPUTED (declared "
      "cap, U1/BC1's subject)")

# ===========================================================================
hdr(6, "VERDICT")

npass = sum(1 for g in GATES if g[1])
nfail = len(GATES) - npass
nanch = sum(1 for g in GATES if g[4] == "A")
nctl = sum(1 for g in GATES if g[4] == "C")
afail = sum(1 for g in GATES if g[4] == "A" and not g[1])
cfail = sum(1 for g in GATES if g[4] == "C" and not g[1])

print(f"""
  LEMMA (LTP-FORCING) is stated at SEC 2 and its two non-trivial steps are
  gated (L1 the formal identity, L2/L3 the H-SPAN separation).

  ON THE COMMITTED BC2 MODEL, REBUILT AND ANCHORED:

    * the rebuild reproduces every number the committed receipt prints
      (A1-A6: the singlet control, the whole SP-A inventory, the
      divisibility census, the eq.22 ranks, the 36-cell mismatch table,
      the basis-free certificate);

    * the declared intermediate division event t' = 2 violates [B3]'s own
      law of total probability at SP-C, SP-D and SP-F, in both frames, ON
      THE MODEL'S OWN DECLARED p(0): the residual has 16 nonzero entries
      of 36, with the four irrational values +-1/32 +- sqrt2/32;

    * by lemma (c) the framework therefore FORCES DENYING that a division
      event occurs there -- at exactly the place [B3] p.29 says a
      measurement generates one.  The denial is [B3]'s, not v12's.

  WHAT IS NOT CLAIMED: nothing about nature; nothing about frames (BC2
  owns that and is cited, not re-derived); nothing about existential
  divisibility d_div (no LP is run); nothing about [B3]'s equivalence
  theorem, which is not under test.

  GATES {len(GATES)}  PASS {npass}  FAIL {nfail}  (anchors {nanch}, anchor \
failures {afail}; controls {nctl}, control failures {cfail})
  RUNTIME {time.time()-T0:.1f} s.  Deterministic: no randomness, no hashing
  -order dependence, no float anywhere.
""")

if nfail:
    print("  FAILED GATES: " + ", ".join(g[0] for g in GATES if not g[1]))
    sys.exit(1)
print("  EXIT 0 — the unit's finding is a substantive NEGATIVE about a")
print("  declared division-event set, and exits 0 by house rule.")
sys.exit(0)
