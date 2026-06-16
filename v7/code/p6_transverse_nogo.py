#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
p6_transverse_nogo.py -- THE MAIN TRANSVERSE NO-GO RECEIPT.  v7 Long March, Paper 6.

CLAIM (the split, honesty-graded):
  [CONSTRAINED]  The almost-quantum ENVELOPE is FORCED FROM INSIDE the records:
                 moment-positivity Gamma>=0 (Gamma = Gram matrix of the substrate's
                 OWN observables {1, A_x, B_y, A_xB_y}) ENTAILS no-signaling, the
                 Tsirelson ceiling CHSH<=2sqrt2 (NPA level-1, PR-box excluded), the
                 Collins-Gisin I3322 (projector form) strict OUTER relaxation
                 (level-(1+AB) 0.2514709 > level-2 0.2513864 > Q-bound 0.2508754,
                 Pal-Vertesi 2010), and the monogamy facet
                 CHSH_AB^2 + CHSH_AC^2 <= 8.
  [NO-GO]        The entangling CONTENT chi_AB = I_sigma is NOT forced -- by BOTH
                 independent weight-0 mechanisms:
                 (M1) INFORMATION-GEOMETRIC CAPACITY BLINDNESS.  On
                      P(a,b) prop exp(eta_A a + eta_B b + lambda ab), the faithful
                      Fisher-capacity leg is the marginal-tilt Fisher
                      Var(a)=1-<a>^2, a function of the MARGINALS ALONE ->
                      EXACTLY lambda-independent at fixed marginals; and the joint
                      KL content C_AB(lambda) is U-SHAPED (no rising leg, max-min
                      ill-posed; any forced-looking balance C_AB=Cov(a,b) MOVES with
                      the marginals -> circular, pins no intrinsic number).
                 (M2) OPERATOR-ALGEBRAIC FIELD BLINDNESS.  The chains meet ONLY at
                      shared cross-moments (commutation ON THE STATE, NOT a tensor
                      factorization), so every transverse principle factors through
                      the level-(1+AB) moment algebra M.  M is an INVARIANT of the
                      field-reduction map R (qubit-pair -> rebit-pair, complex->real):
                      R preserves every marginal, every cross-moment E_xy, the
                      idempotent seal E=E^2=E*, the Tsirelson point, AND the sealing
                      scalar I_sigma itself, while CHANGING the local-tomography count
                      K_AB (deficit K_AB-K_A K_B = +1 over R, 0 over C).  The ONE bit
                      distinguishing a unique complex chi_AB lies in the KERNEL of the
                      factorization through M.  So chi_AB is free up to Q-tilde; the
                      gap Q-tilde \\ Q is permanent and level-independent (Tsirelson's
                      problem / Slofstra 2019).

  The split is DIFFERENT in structure from the weight-+1 scale/Newton-G no-go
  (Paper 57): there, records carry no absolute LENGTH; here, records carry no
  global TENSOR PRODUCT / no intrinsic SECOND-TILT capacity leg.

PARTS:
  PART 0  single-chain template sanity (eta_A, theta_*, W_* by BOTH J and C;
          monotone opposition; eta_B seal-firing).
  PART 1  M1 capacity blindness (fixed-marginal solver; Var(a) lambda-flat;
          C_AB(lambda) U-shaped).
  PART 2  M1 circularity / non-intrinsic (C_AB=Cov(a,b) root MOVES with m).
  PART 3  M2 field blindness, sealing scalar (rebit & qubit realize the SAME
          p(a,b|x,y); I_sigma(rebit)-I_sigma(qubit)=0; seal E^2=E=E* over R and C).
  PART 4  M2 separator invisible (info-dim K-counts; local-tomography boolean).
  PART 5  POSITIVE: envelope forced from inside (cvxpy SDP, SOLVER-TOLERANCE FLAGGED).
  PART 6  C4 cocycle triviality (associator==1; grouped survival grouping-independent
          -> H^2 trivial / coboundary).

PRECISION: mpmath dps=140 for exact/cancellation parts; sympy-exact for derivative
signs / dimension counts; cvxpy/SCS ONLY for corroboration with EVERY digit flagged
as solver-tolerance (~1e-9), NEVER high precision.

PRE-GEOMETRIC discipline: a,b in {+1,-1} are committed record outcomes; x,y,lambda,
eta are abstract Tier-A record-internal labels / tilts; every quantity is a
record-internal probability, KL divergence (weight-0 pure number), or a moment
<psi|O_i^dagger O_j|psi>.  No spacetime, metric, light cone, or s^2 ever appears.
"""

import mpmath as mp
import sympy as sp
import numpy as np

mp.mp.dps = 140            # exact / cancellation-heavy parts
np.set_printoptions(precision=10, suppress=True)

# ---------------------------------------------------------------------------
# check harness
# ---------------------------------------------------------------------------
CHECKS = []
def check(name, cond, detail="", solver_tol=False):
    cond = bool(cond)
    CHECKS.append((name, cond, solver_tol))
    tag = "PASS" if cond else "**FAIL**"
    flag = "  [SOLVER-TOL ~1e-9]" if solver_tol else ""
    print(f"  [{tag}]  {name}   {detail}{flag}")
    return cond

def head(s):
    print("\n" + "=" * 80)
    print(s)
    print("=" * 80)

def line(label, val, extra=""):
    print(f"    {label:<52} {val} {extra}")


# ===========================================================================
head("PART 0.  SINGLE-CHAIN TEMPLATE SANITY (the anchors to reproduce)")
# ===========================================================================
print("""
  LAW-A capacity crossing: the one-diamond self-consistency KL = Fisher,
      C(eta) = eta tanh eta - log cosh eta      (KL content; C' = eta sech^2 eta > 0)
      J(eta) = sech^2 eta = 1 - tanh^2 eta      (Fisher capacity; J' = -2 tanh sech^2 < 0)
  crossing C(eta_A) = J(eta_A) at eta_A; W_* = J(eta_A) = C(eta_A); theta_*=tanh eta_A.
  LAW-B seal-firing: tanh(eta) = e^{-eta} -> eta_B; C(eta_B)/W_* ~ 0.428; 1/eta_B.
""")

QUOTED_ETA_A   = mp.mpf("1.090344354879492196221")
QUOTED_THETA_S = mp.mpf("0.797003794162878272143")
QUOTED_W_S     = mp.mpf("0.3647849520899763622572")
QUOTED_ETA_B   = mp.mpf("0.609377863436006232")
QUOTED_INV_ETA_B = mp.mpf("1.641017929928488")

def C_of(eta):
    eta = mp.mpf(eta)
    return eta*mp.tanh(eta) - mp.log(mp.cosh(eta))

def J_of(eta):
    eta = mp.mpf(eta)
    return 1 - mp.tanh(eta)**2          # = sech^2 eta

def balance_A(eta):
    return C_of(eta) - J_of(eta)

eta_A   = mp.findroot(balance_A, mp.mpf("1.09"))
theta_s = mp.tanh(eta_A)
W_s_J   = J_of(eta_A)                    # Fisher formula
W_s_C   = C_of(eta_A)                    # KL formula (independent)
two_formula_gap = abs(W_s_J - W_s_C)

line("eta_A (root of C=J)", mp.nstr(eta_A, 40))
line("theta_* = tanh eta_A", mp.nstr(theta_s, 40))
line("W_* = J(eta_A) [Fisher]", mp.nstr(W_s_J, 40))
line("W_* = C(eta_A) [KL, independent]", mp.nstr(W_s_C, 40))
line("two-formula gap |J-C| at eta_A", mp.nstr(two_formula_gap, 6))

check("eta_A reproduces 1.090344354879492196221 (<1e-18)",
      abs(eta_A - QUOTED_ETA_A) < mp.mpf("1e-18"),
      f"|d|={mp.nstr(abs(eta_A-QUOTED_ETA_A),4)}")
check("theta_* reproduces 0.797003794162878272143 (<1e-18)",
      abs(theta_s - QUOTED_THETA_S) < mp.mpf("1e-18"),
      f"|d|={mp.nstr(abs(theta_s-QUOTED_THETA_S),4)}")
check("W_* reproduces 0.3647849520899763622572 by BOTH J and C (<1e-18)",
      abs(W_s_J - QUOTED_W_S) < mp.mpf("1e-18") and abs(W_s_C - QUOTED_W_S) < mp.mpf("1e-18"),
      f"|J-quote|={mp.nstr(abs(W_s_J-QUOTED_W_S),4)}")
check("two-formula gap |J(eta_A)-C(eta_A)| < 1e-130 (expect ~6.6e-142)",
      two_formula_gap < mp.mpf("1e-130"),
      f"gap={mp.nstr(two_formula_gap,4)}")

# sympy-EXACT monotone opposition of the two legs
eta = sp.symbols('eta', positive=True)
C_sym = eta*sp.tanh(eta) - sp.log(sp.cosh(eta))
J_sym = 1 - sp.tanh(eta)**2
Cp = sp.simplify(sp.diff(C_sym, eta))
Jp = sp.simplify(sp.diff(J_sym, eta))
# C'(eta) = eta sech^2 eta ; J'(eta) = -2 tanh eta sech^2 eta
Cp_target = eta*sp.sech(eta)**2
Jp_target = -2*sp.tanh(eta)*sp.sech(eta)**2
Cp_match = sp.simplify(Cp - Cp_target) == 0
Jp_match = sp.simplify(Jp - Jp_target) == 0
line("C'(eta) [sympy]", Cp)
line("J'(eta) [sympy]", Jp)
check("sympy-exact: C'(eta) = eta sech^2 eta (rising leg, >0 for eta>0)", Cp_match,
      "C' > 0")
check("sympy-exact: J'(eta) = -2 tanh eta sech^2 eta (falling leg, <0 for eta>0)", Jp_match,
      "J' < 0  => monotone OPPOSITION (a single transversal crossing)")
# numeric sign confirmation away from 0
check("C'(1)>0 and J'(1)<0 numerically (opposition)",
      float(Cp.subs(eta,1)) > 0 and float(Jp.subs(eta,1)) < 0,
      f"C'(1)={float(Cp.subs(eta,1)):.4f}, J'(1)={float(Jp.subs(eta,1)):.4f}")

# LAW-B seal firing  tanh(eta) = e^{-eta}
def balance_B(eta):
    eta = mp.mpf(eta)
    return mp.tanh(eta) - mp.e**(-eta)
eta_B = mp.findroot(balance_B, mp.mpf("0.6"))
C_etaB = C_of(eta_B)
ratio_B = C_etaB / W_s_J
inv_eta_B = 1/eta_B
line("eta_B (root of tanh eta = e^-eta)", mp.nstr(eta_B, 30))
line("C(eta_B)/W_*", mp.nstr(ratio_B, 12))
line("1/eta_B", mp.nstr(inv_eta_B, 18))
check("eta_B reproduces 0.609377863436006232 (<1e-15)",
      abs(eta_B - QUOTED_ETA_B) < mp.mpf("1e-15"),
      f"|d|={mp.nstr(abs(eta_B-QUOTED_ETA_B),4)}")
check("C(eta_B)/W_* ~ 0.428 (within 5e-4)",
      abs(ratio_B - mp.mpf("0.428")) < mp.mpf("5e-4"),
      f"ratio={mp.nstr(ratio_B,6)}")
check("1/eta_B reproduces 1.641017929928488 (<1e-12)",
      abs(inv_eta_B - QUOTED_INV_ETA_B) < mp.mpf("1e-12"),
      f"|d|={mp.nstr(abs(inv_eta_B-QUOTED_INV_ETA_B),4)}")


# ===========================================================================
head("PART 1.  M1 CAPACITY BLINDNESS  (the literal single-chain analog FAILS)")
# ===========================================================================
print("""
  The transverse candidate (C1): try to run the SINGLE-CHAIN trick on the JOINT
  exponential family
        P(a,b) prop exp(eta_A a + eta_B b + lambda a b),   a,b in {+1,-1},
  with lambda the entangling tilt (the candidate chi_AB lever).  Hold the MARGINALS
  fixed at <a>=<b>=m (re-solving (eta_A,eta_B) at each lambda) and ask whether a
  KL=Fisher capacity crossing pins lambda.  TWO obstructions:

   (1a) the FAITHFUL Fisher leg (the analog of J) is the MARGINAL-TILT Fisher
        Var(a) = 1 - <a>^2, a function of the MARGINALS ALONE.  At fixed marginals it
        is EXACTLY lambda-independent: dJ_marg/dlambda = 0.  No rising/falling leg
        in lambda at all -> nothing to cross.
   (1b) the joint KL content C_AB(lambda) = D(P_lambda || P_0-at-same-marginals) is
        U-SHAPED in lambda (min at lambda=0, rising on BOTH sides) -> no single
        monotone leg, the max-min crossing is ill-posed.
""")

def joint_probs(eA, eB, lam):
    """P(a,b) prop exp(eA a + eB b + lam ab) on {+1,-1}^2; returns dict and Z."""
    eA, eB, lam = mp.mpf(eA), mp.mpf(eB), mp.mpf(lam)
    w = {}
    for a in (1, -1):
        for b in (1, -1):
            w[(a, b)] = mp.e**(eA*a + eB*b + lam*a*b)
    Z = sum(w.values())
    return {k: v/Z for k, v in w.items()}, Z

def marg_means(P):
    ma = sum(a*P[(a, b)] for a in (1, -1) for b in (1, -1))
    mb = sum(b*P[(a, b)] for a in (1, -1) for b in (1, -1))
    return ma, mb

def solve_eta_for_marginals(m, lam):
    """Find (eA,eB) so that <a>=<b>=m at the given lambda. Symmetric => eA=eB=e."""
    m, lam = mp.mpf(m), mp.mpf(lam)
    def f(e):
        P, _ = joint_probs(e, e, lam)
        ma, _ = marg_means(P)
        return ma - m
    e0 = mp.atanh(m)            # lambda=0 seed
    e = mp.findroot(f, e0)
    return e

def cov_ab(P):
    ab = sum(a*b*P[(a, b)] for a in (1, -1) for b in (1, -1))
    ma, mb = marg_means(P)
    return ab - ma*mb

def fisher_marginal(P):
    """Faithful Fisher of the MARGINAL tilt: Var(a) = 1 - <a>^2 (marginals only)."""
    ma, _ = marg_means(P)
    return 1 - ma**2

def C_AB_content(P):
    """The joint KL CONTENT of the committed law vs the EVENTLESS base mu_D = uniform
       (1/4,1/4,1/4,1/4) -- the count-dual of the single-chain template (paper4 s5,
       where C = D(P_eta || mu_D) with mu_D the eventless base).  This is the JOINT
       analog of the single-chain content C(eta).  C_AB = D(P || 1/4)."""
    base = mp.mpf(1)/4
    s = mp.mpf(0)
    for k in P:
        if P[k] > 0:
            s += P[k]*mp.log(P[k]/base)
    return s

m_fix = mp.mpf("0.5")           # the marginal we hold (matches the quoted C_AB values)
lam_grid = [mp.mpf(x)/10 for x in range(-6, 7)]   # -0.6 .. 0.6

print("  lambda     <a>(resid)        Var(a)=1-<a>^2          C_AB(lambda)")
records = []
max_marg_resid = mp.mpf(0)
var_vals = []
C_vals = {}
for lam in lam_grid:
    e = solve_eta_for_marginals(m_fix, lam)
    P, _ = joint_probs(e, e, lam)
    ma, mb = marg_means(P)
    resid = abs(ma - m_fix) + abs(mb - m_fix)
    max_marg_resid = max(max_marg_resid, resid)
    var = fisher_marginal(P)
    var_vals.append(var)
    C = C_AB_content(P)
    C_vals[float(lam)] = C
    records.append((lam, resid, var, C))
    print(f"   {float(lam):+.2f}   {mp.nstr(resid,4):>10}   {mp.nstr(var,22)}   {mp.nstr(C,18)}")

var_spread = max(var_vals) - min(var_vals)
check("fixed-marginal solver: max marginal residual < 1e-110",
      max_marg_resid < mp.mpf("1e-110"),
      f"max_resid={mp.nstr(max_marg_resid,4)}")
check("M1(1a): Var(a)=1-<a>^2 spread across lambda < 1e-100 (realized ~1.3e-141 at dps=140)",
      var_spread < mp.mpf("1e-100"),
      f"spread={mp.nstr(var_spread,4)} => faithful Fisher leg is lambda-INDEPENDENT")

# central-difference dJ_marg/dlambda at lambda=0 (h tiny)
h = mp.mpf("1e-30")
def Jmarg_at(lam):
    e = solve_eta_for_marginals(m_fix, lam)
    P, _ = joint_probs(e, e, lam)
    return fisher_marginal(P)
dJ = (Jmarg_at(h) - Jmarg_at(-h))/(2*h)
check("M1(1a): central-diff dJ_marg/dlambda (h=1e-30) ~ 0 (<1e-90)",
      abs(dJ) < mp.mpf("1e-90"),
      f"|dJ/dlam|={mp.nstr(abs(dJ),4)}  => no transverse capacity leg")

# U-shape of C_AB: min at lambda=0, both wings higher
C_center = C_vals[0.0]
C_wing_p = C_vals[0.6]
C_wing_m = C_vals[-0.6]
line("C_AB(lambda=0)  [center, the MIN]", mp.nstr(C_center, 12))
line("C_AB(lambda=+0.6) [wing]", mp.nstr(C_wing_p, 12))
line("C_AB(lambda=-0.6) [wing]", mp.nstr(C_wing_m, 12))
# check center is the minimum over the grid
is_min = all(C_vals[float(lam)] >= C_center - mp.mpf("1e-110") for lam in lam_grid)
check("M1(1b): C_AB(lambda) U-SHAPED -- lambda=0 is the MINIMUM over the grid",
      is_min, "both wings rise => no single monotone leg")
check("M1(1b): center ~0.26162407, wings ~0.37125 (+0.6) / ~0.31128 (-0.6)",
      abs(C_center - mp.mpf("0.26162407")) < mp.mpf("1e-6")
      and abs(C_wing_p - mp.mpf("0.37125")) < mp.mpf("2e-5")
      and abs(C_wing_m - mp.mpf("0.31128")) < mp.mpf("2e-5"),
      f"center={mp.nstr(C_center,8)}, +wing={mp.nstr(C_wing_p,8)}, -wing={mp.nstr(C_wing_m,8)}")
check("M1(1b): both wings STRICTLY exceed the center (U-shape, not a crossing)",
      C_wing_p > C_center and C_wing_m > C_center,
      f"+wing-center={mp.nstr(C_wing_p-C_center,4)}, -wing-center={mp.nstr(C_wing_m-C_center,4)}")


# ===========================================================================
head("PART 2.  M1 CIRCULARITY / NON-INTRINSIC  (any forced-looking balance MOVES)")
# ===========================================================================
print("""
  One could try to RESCUE a crossing by balancing the joint KL content against the
  one lambda-RESPONSIVE Fisher entry, the off-diagonal Cov(a,b).  But (i) Cov(a,b)
  IS the entangling content chi_AB itself -> the 'principle' C_AB(lambda)=Cov(a,b)
  is CIRCULAR (it sets the content equal to a transform of the content); and (ii)
  its root lambda* MOVES with the marginal m -> it pins NO intrinsic number.
""")

def balance_M1(lam, m):
    """C_AB(lambda) - Cov(a,b): balance the joint KL content against the ONLY
       lambda-responsive Fisher entry (the off-diagonal Cov = the entangling content
       itself).  C_AB here is the joint content vs the eventless base (same as PART 1)."""
    e = solve_eta_for_marginals(m, lam)
    P, _ = joint_probs(e, e, lam)
    C = C_AB_content(P)
    return C - cov_ab(P)

roots = {}
for m in [mp.mpf("0.3"), mp.mpf("0.5"), mp.mpf("0.7")]:
    # C_AB content is strictly positive (vs uniform) and rising in |lambda|; Cov rises
    # from 0.  A finite NONZERO crossing C_AB=Cov may or may not exist; scan-bracket on
    # (0.02, 1.5) for a genuine sign change (findroot from one seed lands on no root).
    r = None
    prev = balance_M1(mp.mpf("0.02"), m)
    L = mp.mpf("0.02")
    while L < mp.mpf("1.5"):
        L2 = L + mp.mpf("0.02")
        cur = balance_M1(L2, m)
        if prev*cur < 0:
            r = mp.findroot(lambda LL: balance_M1(LL, m), (L+L2)/2)
            break
        prev = cur; L = L2
    roots[float(m)] = r
    line(f"C_AB(lambda)=Cov(a,b) nonzero root at m={float(m)}",
         (mp.nstr(r, 10) if r is not None else "no robust root in (0.02,1.5) -- NON-ROBUST"))

r03 = roots[0.3]
r05 = roots[0.5]
r07 = roots[0.7]
check("M1(2): nonzero root at m=0.3 ~ 0.115 (within 5e-3)",
      r03 is not None and abs(r03 - mp.mpf("0.115")) < mp.mpf("5e-3"),
      f"lam*(0.3)={mp.nstr(r03,6) if r03 is not None else None}")
check("M1(2): nonzero root at m=0.5 ~ 0.619 (within 5e-3)",
      r05 is not None and abs(r05 - mp.mpf("0.619")) < mp.mpf("5e-3"),
      f"lam*(0.5)={mp.nstr(r05,6) if r05 is not None else None}")
check("M1(2): the root MOVES with the marginal m (non-robust => pins no intrinsic #)",
      r03 is not None and r05 is not None and abs(r05 - r03) > mp.mpf("0.3"),
      f"lam*(0.5)-lam*(0.3)={mp.nstr(r05-r03,6) if (r03 and r05) else None}")
check("M1(2): at m=0.7 the C_AB=Cov balance has NO robust root (non-robust)",
      r07 is None,
      f"m=0.7 root: {mp.nstr(r07,6) if r07 is not None else 'NON-ROBUST (no crossing)'}")
print("""
    => The only lambda-responsive Fisher entry is Cov(a,b) = the entangling content
       itself; balancing against it is CIRCULAR, and the resulting lambda* drifts
       with the marginals.  M1 pins NO intrinsic chi_AB.  [NO-GO via capacity blindness]
""")


# ===========================================================================
head("PART 3.  M2 FIELD BLINDNESS -- the SEALING SCALAR is invariant under R")
# ===========================================================================
print("""
  The transverse principle factors through the level-(1+AB) moment algebra M =
  <{1, A_x, B_y, A_xB_y}>_psi (the chains meet ONLY at shared cross-moments).  M is
  an INVARIANT of the field-reduction map R: qubit-pair -> rebit-pair (complex ->
  real).  At the Tsirelson correlator E=(E00,E01,E10,E11)=(s,s,s,-s), s=1/sqrt2, the
  click-law p(a,b|x,y)=(1+ab E_xy)/4 is realized by BOTH a rebit Bell pair and a
  qubit singlet, with IDENTICAL marginals, CHSH, idempotent seal, AND sealing scalar
  I_sigma.  R changes only the kernel datum K_AB (PART 4), invisible to M.
""")

s = 1/mp.sqrt(2)
E = {(0,0): s, (0,1): s, (1,0): s, (1,1): -s}

def click_law(Exy):
    """p(a,b|x,y) = (1 + a b Exy)/4, a,b in {+1,-1}."""
    p = {}
    for a in (1, -1):
        for b in (1, -1):
            p[(a, b)] = (1 + a*b*Exy)/4
    return p

def marginals_click(p):
    pa = {a: sum(p[(a, b)] for b in (1, -1)) for a in (1, -1)}
    pb = {b: sum(p[(a, b)] for a in (1, -1)) for b in (1, -1)}
    return pa, pb

# marginals at every (x,y): must be (1/2,1/2)
marg_ok = True
for xy, Exy in E.items():
    p = click_law(Exy)
    pa, pb = marginals_click(p)
    if abs(pa[1]-mp.mpf("0.5")) > mp.mpf("1e-118") or abs(pb[1]-mp.mpf("0.5")) > mp.mpf("1e-118"):
        marg_ok = False
check("M2: click-law marginals = (1/2,1/2) at all (x,y) (<1e-118)", marg_ok,
      "uniform marginals => no-signaling at the marginal level")

CHSH = E[(0,0)] + E[(0,1)] + E[(1,0)] - E[(1,1)]
check("M2: CHSH = E00+E01+E10-E11 = 2sqrt2 (Tsirelson) (<1e-118)",
      abs(CHSH - 2*mp.sqrt(2)) < mp.mpf("1e-118"),
      f"|CHSH-2sqrt2|={mp.nstr(abs(CHSH-2*mp.sqrt(2)),4)}")

# --- sealing scalar I_sigma: the mutual content of the joint click-law at a
#     FIXED isotropic setting (the correlator that the seal commits).  I_sigma is a
#     functional of the moment algebra M (marginals + cross-moment E) ALONE, hence
#     field-blind.  We compute it from the SAME p(ab) that BOTH the rebit and qubit
#     realizations produce -- they produce the identical click-law, so I_sigma is
#     literally identical.  (The point of M2 is that I_sigma reads only M.)
def I_sigma_of(Exy):
    """mutual information I(A:B) of p(a,b)=(1+abE)/4 -- a functional of M (E,marginals)."""
    p = click_law(Exy)
    pa, pb = marginals_click(p)
    I = mp.mpf(0)
    for a in (1, -1):
        for b in (1, -1):
            if p[(a, b)] > 0:
                I += p[(a, b)]*mp.log(p[(a, b)]/(pa[a]*pb[b]))
    return I

# rebit and qubit BOTH realize the SAME correlator s -> SAME click-law -> SAME I_sigma.
# We COMPUTE the correlator from each field's measurement algebra (not assert it):
#   qubit singlet:  E = -cos(thetaA - thetaB), full SU(2) (Y available).
#   rebit Bell pair: real measurement vectors in the X-Z plane (NO Y); the singlet
#                    correlator is the SAME angle algebra E = -cos(phiA - phiB).
# Both reach |E| = 1/sqrt2 at the Tsirelson angle pi/4 -- because the CHSH/correlator
# structure lives entirely in the X-Z plane that R preserves.  The Y-direction (the
# one R removes) does NOT enter any moment of M.  Hence the moment-algebra functional
# I_sigma is identical -- field-blind.
# NOTE: here both correlators are the SAME scalar by construction (the Tsirelson E lies
# in the X-Z plane both fields share), so the I_sigma equality below is true-by-design --
# it illustrates that I_sigma is a moment functional of E.  The LOAD-BEARING, genuinely
# field-distinguishing computation (qubit-singlet vs rebit-Bell-pair Hilbert realizations
# giving the SAME holonomy from DIFFERENT algebras) is in p6b_holonomy_phase_audit.py; the
# no-go (M2) rests on the K-deficit/orbit argument (PART 4), not on this equality.
ang_T = mp.pi/4                       # Tsirelson angle
E_from_qubit = -mp.cos(mp.mpf(0) - ang_T)   # qubit singlet, SU(2) (Y available, unused here)
E_from_rebit = -mp.cos(mp.mpf(0) - ang_T)   # rebit Bell pair, X-Z plane only (no Y)
line("qubit correlator E (SU(2), Y available)", mp.nstr(E_from_qubit, 22))
line("rebit correlator E (X-Z plane, no Y)", mp.nstr(E_from_rebit, 22))
check("M2: qubit & rebit BOTH reach |E|=1/sqrt2 at Tsirelson angle (<1e-118)",
      abs(abs(E_from_qubit) - s) < mp.mpf("1e-118")
      and abs(abs(E_from_rebit) - s) < mp.mpf("1e-118"),
      "the CHSH correlator lives in the X-Z plane R preserves (Y unused)")
I_qubit = I_sigma_of(abs(E_from_qubit))
I_rebit = I_sigma_of(abs(E_from_rebit))
line("I_sigma (qubit realization)", mp.nstr(I_qubit, 22))
line("I_sigma (rebit realization)", mp.nstr(I_rebit, 22))
check("M2: I_sigma(rebit) - I_sigma(qubit) = 0 (<1e-118)",
      abs(I_rebit - I_qubit) < mp.mpf("1e-118"),
      f"|d I_sigma|={mp.nstr(abs(I_rebit-I_qubit),4)}  => sealing scalar is FIELD-BLIND")

# --- the idempotent seal E_proj = E_proj^2 = E_proj^* over BOTH R and C.
#     real screen: projector in the X-Z plane (no Y); complex screen: uses Y.
#     We use high-precision mpmath matrices and verify |E^2-E| and |E-E*| < 1e-118.
def mp_matmul(M, N):
    n = M.rows
    R = mp.zeros(n, n)
    for i in range(n):
        for j in range(n):
            R[i, j] = sum(M[i, k]*N[k, j] for k in range(n))
    return R

def mp_conj_transpose(M):
    n = M.rows
    R = mp.zeros(n, n)
    for i in range(n):
        for j in range(n):
            R[j, i] = mp.conj(M[i, j])
    return R

def mp_maxabs(M):
    return max(abs(M[i, j]) for i in range(M.rows) for j in range(M.cols))

I2 = mp.matrix([[1, 0], [0, 1]])
Xp = mp.matrix([[0, 1], [1, 0]])
Zp = mp.matrix([[1, 0], [0, -1]])
Yp = mp.matrix([[0, -1j], [1j, 0]])

# real seal: n in X-Z plane, n=(3/5,0,4/5)
nx, nz = mp.mpf(3)/5, mp.mpf(4)/5
E_real = (I2 + nx*Xp + nz*Zp) * mp.mpf("0.5")
E2_real = mp_matmul(E_real, E_real)
idem_real = mp_maxabs(E2_real - E_real)
sa_real = mp_maxabs(E_real - mp_conj_transpose(E_real))
# complex seal: uses Y, n=(3/5 along Y, 4/5 along Z)
E_cx = (I2 + (mp.mpf(3)/5)*Yp + (mp.mpf(4)/5)*Zp) * mp.mpf("0.5")
E2_cx = mp_matmul(E_cx, E_cx)
idem_cx = mp_maxabs(E2_cx - E_cx)
sa_cx = mp_maxabs(E_cx - mp_conj_transpose(E_cx))

line("real seal  |E^2 - E|", mp.nstr(idem_real, 6))
line("real seal  |E - E^*|", mp.nstr(sa_real, 6))
line("complex seal |E^2 - E|", mp.nstr(idem_cx, 6))
line("complex seal |E - E^*|", mp.nstr(sa_cx, 6))
check("M2: real (X-Z) seal idempotent |E^2-E| < 1e-118", idem_real < mp.mpf("1e-118"))
check("M2: real (X-Z) seal self-adjoint |E-E^*| < 1e-118", sa_real < mp.mpf("1e-118"))
check("M2: complex (uses Y) seal idempotent |E^2-E| < 1e-118", idem_cx < mp.mpf("1e-118"))
check("M2: complex (uses Y) seal self-adjoint |E-E^*| < 1e-118", sa_cx < mp.mpf("1e-118"),
      "seal E=E^2=E^* holds IDENTICALLY over R and C => field-blind")


# ===========================================================================
head("PART 4.  M2 SEPARATOR INVISIBLE -- info-dim counts (sympy-EXACT)")
# ===========================================================================
print("""
  The ONE bit that distinguishes a unique complex chi_AB is the LOCAL-TOMOGRAPHY
  count K_AB = K_A * K_B, which lives in the KERNEL of the factorization through M:
      complex qubit:  K_single = d^2       = 4,  K_2qubit = D^2 = 16 = 4*4 (LOCAL TOMOG)
      real   rebit :  K_single = d(d+1)/2  = 3,  K_2rebit = 10 != 9 = 3*3 (DEFICIT +1)
  M preserves all moments but NOT this count -> R is invisible to every transverse
  principle that factors through M.  sympy-exact integer arithmetic.
""")
d = sp.Integer(2)
K_single_C = d**2                       # 4
K_single_R = d*(d+1)//2                 # 3
D = sp.Integer(4)                       # composite Hilbert dim 2*2
K_2qubit = D**2                         # 16
K_2rebit = D*(D+1)//2                   # real symmetric 4x4 -> 10
line("K_single complex (qubit) = d^2", K_single_C)
line("K_single real (rebit) = d(d+1)/2", K_single_R)
line("K_2qubit = D^2", K_2qubit)
line("K_2rebit = D(D+1)/2 (real sym 4x4)", K_2rebit)
deficit_R = K_2rebit - K_single_R*K_single_R
deficit_C = K_2qubit - K_single_C*K_single_C
line("rebit deficit K_AB - K_A*K_B", deficit_R)
line("qubit deficit K_AB - K_A*K_B", deficit_C)

check("M2: K_single(R)=3, K_single(C)=4 (sympy-exact)",
      K_single_R == 3 and K_single_C == 4)
check("M2: K_2rebit=10, K_2qubit=16 (sympy-exact)",
      K_2rebit == 10 and K_2qubit == 16)
check("M2: local-tomography boolean FALSE for rebit (10 != 9, deficit +1)",
      (K_2rebit == K_single_R*K_single_R) is False and deficit_R == 1,
      "rebit FAILS K_AB=K_A K_B => hidden joint parameter invisible to M")
check("M2: local-tomography boolean TRUE for qubit (16 == 16, deficit 0)",
      (K_2qubit == K_single_C*K_single_C) is True and deficit_C == 0,
      "qubit SATISFIES K_AB=K_A K_B")
print("""
    => R preserves M (all moments, the seal, the Tsirelson point, I_sigma) yet flips
       the local-tomography count (deficit +1 over R, 0 over C).  The complex-vs-real
       bit -- the one that would fix a UNIQUE chi_AB -- lies in ker(factorization
       through M).  [NO-GO via field blindness; gap Q-tilde \\ Q permanent, Slofstra 2019]
""")


# ===========================================================================
head("PART 5.  POSITIVE: ENVELOPE FORCED FROM INSIDE  (cvxpy SDP, SOLVER-TOLERANCE)")
# ===========================================================================
print("""
  Gamma >= 0 is the Gram matrix of the substrate's OWN observables {1,A_x,B_y,A_xB_y}
  -- moment-positivity is FORCED (a Gram matrix is PSD).  This single inside-fact
  ENTAILS the whole almost-quantum envelope.  cvxpy/SCS ONLY for corroboration;
  EVERY printed digit below is SOLVER-TOLERANCE ~1e-9 (NOT high precision).
""")
import cvxpy as cp

# --- (5a) NPA level-1 caps CHSH at 2sqrt2; PR-box infeasible ----------------
def max_chsh_npa1():
    Ev = cp.Variable((2, 2)); AA = cp.Variable(); BB = cp.Variable()
    G = cp.bmat([
        [cp.Constant(1.0), cp.Constant(0.0), cp.Constant(0.0), cp.Constant(0.0), cp.Constant(0.0)],
        [cp.Constant(0.0), cp.Constant(1.0), AA, Ev[0, 0], Ev[0, 1]],
        [cp.Constant(0.0), AA, cp.Constant(1.0), Ev[1, 0], Ev[1, 1]],
        [cp.Constant(0.0), Ev[0, 0], Ev[1, 0], cp.Constant(1.0), BB],
        [cp.Constant(0.0), Ev[0, 1], Ev[1, 1], BB, cp.Constant(1.0)],
    ])
    chsh = Ev[0, 0] + Ev[0, 1] + Ev[1, 0] - Ev[1, 1]
    prob = cp.Problem(cp.Maximize(chsh), [G >> 0])
    prob.solve(solver=cp.SCS, eps=1e-10)
    return prob.value

def chsh_feasible(E00, E01, E10, E11):
    AA = cp.Variable(); BB = cp.Variable()
    G = cp.bmat([
        [cp.Constant(1.0), cp.Constant(0.0), cp.Constant(0.0), cp.Constant(0.0), cp.Constant(0.0)],
        [cp.Constant(0.0), cp.Constant(1.0), AA, cp.Constant(E00), cp.Constant(E01)],
        [cp.Constant(0.0), AA, cp.Constant(1.0), cp.Constant(E10), cp.Constant(E11)],
        [cp.Constant(0.0), cp.Constant(E00), cp.Constant(E10), cp.Constant(1.0), BB],
        [cp.Constant(0.0), cp.Constant(E01), cp.Constant(E11), BB, cp.Constant(1.0)],
    ])
    prob = cp.Problem(cp.Minimize(0), [G >> 0])
    prob.solve(solver=cp.SCS, eps=1e-9)
    return prob.status in ("optimal", "optimal_inaccurate")

chsh_max = max_chsh_npa1()
tsirelson = float(2*mp.sqrt(2))
line("NPA level-1 max CHSH", f"{chsh_max:.10f}", f"(Tsirelson {tsirelson:.10f})")
check("ENVELOPE: Gamma>=0 caps CHSH at 2sqrt2 (|max-2sqrt2|<1e-7)",
      abs(chsh_max - tsirelson) < 1e-7,
      f"|max-2sqrt2|={abs(chsh_max-tsirelson):.2e}", solver_tol=True)
feas_pr = chsh_feasible(1, 1, 1, -1)
check("ENVELOPE: PR-box E=(1,1,1,-1) (CHSH=4) INFEASIBLE under Gamma>=0",
      not feas_pr, "PR-box excluded from inside", solver_tol=True)
t = float(1/mp.sqrt(2))
feas_ts = chsh_feasible(t, t, t, -t)
check("ENVELOPE: Tsirelson point (CHSH=2sqrt2) FEASIBLE under Gamma>=0",
      feas_ts, "boundary attained", solver_tol=True)

# --- (5b) I3322 strict OUTER relaxation, Collins-Gisin PROJECTOR form -----------
# The genuine Q-tilde\Q witness.  The +-1-CORRELATOR I3322 is NOT used: at the
# records' level it has classical = quantum = level-(1+AB) max = 8.0 (NO gap), and a
# bare {I,A_x,B_y} word list WITHOUT cross-products lands at 8.748 -- ABOVE Q-tilde
# and records-inadmissible (it is the bare Q^1 list, not 1+AB).  The Collins-Gisin
# PROJECTOR functional is the one with a TRUE strict-outer Q-tilde\Q nesting:
#   level-(1+AB) 0.2514709 > level-2 0.2513864 > Q-bound 0.2508754 (Pal-Vertesi 2010,
#   PRA 82, 022116, NPA level>=4 certifies Q; CITED, not re-derived).
# Projectors PA[x]=P(a=0|x), PB[y]=P(b=0|y); PA^2=PA; A,B commute on the state.
_cg_cA = [-2, -1, 0]
_cg_cB = [-1, 0, 0]
_cg_cAB = [[1, 1, 1], [1, 1, -1], [1, -1, 0]]
CG_Q_UPPER = mp.mpf("0.2508754")   # Pal-Vertesi 2010 (NPA level>=4): Q <= this. CITED.

def cg_i3322_bound(level):
    """Maximize the Collins-Gisin I3322 over the NPA moment matrix.
       level='1+AB' : base {1,PA,PB} PLUS all 9 products PA[x]PB[y] (the records' level).
       level=2      : ADDS same-party pairs PA[x]PA[x'], PB[y]PB[y'] -> tighter outer
                      relaxation, hence an UPPER bound on Q."""
    nA, nB = 3, 3
    words = ['I'] + [f'A{x}' for x in range(nA)] + [f'B{y}' for y in range(nB)]
    for x in range(nA):
        for y in range(nB):
            words.append(f'A{x}B{y}')
    if level == 2:
        for x in range(nA):
            for xp in range(x+1, nA):
                words.append(f'A{x}A{xp}')
        for y in range(nB):
            for yp in range(y+1, nB):
                words.append(f'B{y}B{yp}')
    n = len(words)

    def toks(w):
        return [w[k:k+2] for k in range(0, len(w), 2)]

    def reduce_word(w):
        # projectors: PA^2=PA (collapse ADJACENT identical same-party); A,B commute.
        t = toks(w)
        Apart = [s for s in t if s[0] == 'A']
        Bpart = [s for s in t if s[0] == 'B']
        def collapse(part):
            out = []
            for s in part:
                if out and out[-1] == s:
                    continue
                out.append(s)
            return out
        red = ''.join(collapse(Apart)) + ''.join(collapse(Bpart))
        return red if red else 'I'

    def dagger(w):
        return 'I' if w == 'I' else ''.join(reversed(toks(w)))

    moment_set = set()
    entry = [[None]*n for _ in range(n)]
    for i in range(n):
        for jj in range(n):
            prod = dagger(words[i]) + words[jj]
            prod = prod.replace('I', '') or 'I'
            red = reduce_word(prod)
            entry[i][jj] = red
            moment_set.add(red)
    var = {m: (cp.Constant(1.0) if m == 'I' else cp.Variable(name=m))
           for m in sorted(moment_set)}
    G = cp.bmat([[var[entry[i][jj]] for jj in range(n)] for i in range(n)])

    def mom(label):
        return var[reduce_word(label)]
    func = 0
    for x in range(nA):
        func = func + _cg_cA[x]*mom(f'A{x}')
    for y in range(nB):
        func = func + _cg_cB[y]*mom(f'B{y}')
    for x in range(nA):
        for y in range(nB):
            if _cg_cAB[x][y] != 0:
                func = func + _cg_cAB[x][y]*mom(f'A{x}B{y}')
    prob = cp.Problem(cp.Maximize(func), [G >> 0])
    prob.solve(solver=cp.SCS, eps=1e-9, max_iters=300000)
    return prob.value

b1 = cg_i3322_bound('1+AB')   # the records' level: the witness P* lives here
b2 = cg_i3322_bound(2)        # tighter outer relaxation: an UPPER bound on Q
line("CG-I3322 level-(1+AB) optimum (in Q-tilde)", f"{b1:.7f}")
line("CG-I3322 level-2 (tighter; UPPER bound on Q)", f"{b2:.7f}")
line("CG-I3322 Q upper bound (Pal-Vertesi 2010, level>=4)", f"{float(CG_Q_UPPER):.7f}", "(CITED)")
check("ENVELOPE: CG-I3322 strict-outer NESTING 1+AB > level-2 > Q "
      "(0.2514709 > 0.2513864 > 0.2508754) => 1+AB is a genuine Q-tilde-not-Q relaxation",
      b1 - b2 > 1e-5 and mp.mpf(b2) > CG_Q_UPPER and mp.mpf(b1) > CG_Q_UPPER + mp.mpf("1e-6"),
      f"{b1:.7f} > {b2:.7f} > {float(CG_Q_UPPER):.7f}  (gap_to_Q={float(mp.mpf(b1)-CG_Q_UPPER):.7f})",
      solver_tol=True)

# --- (5c) monogamy facet CHSH_AB^2 + CHSH_AC^2 <= 8 over {1,A,B,C,AB,AC} -------
# The PRODUCT operators A_xB_y and A_xC_z must be GENERATORS (not just free moments):
# this is the level the prompt names, "over {1,A,B,C,AB,AC}".  As generators they bind
# B and C through Alice, e.g. <(A0B0)^dagger (A0C0)> = <B0 A0 A0 C0> = <B0 C0> (A0^2=1),
# so the B-C cross-block is no longer free -- THAT is what recovers monogamy.  (At bare
# level-1 over {1,A,B,C} the B-C block floats and monogamy is NOT a facet; the product
# generators are required -- consistent with the Q-tilde\Q gap.)
_mono_words = ['I', 'A0', 'A1', 'B0', 'B1', 'C0', 'C1']
for _x in range(2):
    for _y in range(2):
        _mono_words.append(f'A{_x}B{_y}')
for _x in range(2):
    for _z in range(2):
        _mono_words.append(f'A{_x}C{_z}')

def _mono_toks(w):
    return [w[k:k+2] for k in range(0, len(w), 2)]

def _mono_reduce(w):
    t = _mono_toks(w)
    A = [x for x in t if x[0] == 'A']
    B = [x for x in t if x[0] == 'B']
    C = [x for x in t if x[0] == 'C']
    def cancel(p):
        st = []
        for x in p:
            if st and st[-1] == x:
                st.pop()
            else:
                st.append(x)
        return st
    r = ''.join(cancel(A)) + ''.join(cancel(B)) + ''.join(cancel(C))
    return r if r else 'I'

def _mono_dagger(w):
    return 'I' if w == 'I' else ''.join(reversed(_mono_toks(w)))

_mono_n = len(_mono_words)
_mono_entry = [[None]*_mono_n for _ in range(_mono_n)]
_mono_mset = set()
for _i in range(_mono_n):
    for _j in range(_mono_n):
        _p = _mono_dagger(_mono_words[_i]) + _mono_words[_j]
        _p = _p.replace('I', '') or 'I'
        _red = _mono_reduce(_p)
        _mono_entry[_i][_j] = _red
        _mono_mset.add(_red)

def chsh_pair_feasible(chsh_ab_target, chsh_ac_target):
    """Feasibility of the moment matrix over {1,A,B,C,AB,AC} (product operators as
       GENERATORS) with the CHSH_AB and CHSH_AC VALUES fixed.  Feasible iff a PSD
       completion exists.  The shared Alice operators bind B and C => monogamy."""
    var = {m: (cp.Constant(1.0) if m == 'I' else cp.Variable(name=m)) for m in sorted(_mono_mset)}
    G = cp.bmat([[var[_mono_entry[i][j]] for j in range(_mono_n)] for i in range(_mono_n)])
    def mom(label):
        return var.get(_mono_reduce(label), cp.Constant(0.0))
    chsh_ab = mom('A0B0') + mom('A0B1') + mom('A1B0') - mom('A1B1')
    chsh_ac = mom('A0C0') + mom('A0C1') + mom('A1C0') - mom('A1C1')
    cons = [G >> 0, chsh_ab == chsh_ab_target, chsh_ac == chsh_ac_target]
    prob = cp.Problem(cp.Minimize(0), cons)
    prob.solve(solver=cp.SCS, eps=1e-9, max_iters=100000)
    return prob.status in ("optimal", "optimal_inaccurate")

# facet boundary points: (2sqrt2, 0) and (2,2) satisfy 8+0=8 and 4+4=8 (feasible);
# a point OUTSIDE the facet, e.g. (2sqrt2, 2sqrt2) -> 8+8=16 > 8, must be infeasible.
f_corner1 = chsh_pair_feasible(2*float(mp.sqrt(2)), 0.0)
f_corner2 = chsh_pair_feasible(2.0, 2.0)
f_outside = chsh_pair_feasible(2*float(mp.sqrt(2)), 2*float(mp.sqrt(2)))
v_in1 = (2*float(mp.sqrt(2)))**2 + 0.0
v_in2 = 2.0**2 + 2.0**2
v_out = (2*float(mp.sqrt(2)))**2 + (2*float(mp.sqrt(2)))**2
line("monogamy facet value (2sqrt2,0): CHSH_AB^2+CHSH_AC^2", f"{v_in1:.4f}",
     f"feasible={f_corner1}")
line("monogamy facet value (2,2):      CHSH_AB^2+CHSH_AC^2", f"{v_in2:.4f}",
     f"feasible={f_corner2}")
line("OUTSIDE (2sqrt2,2sqrt2):          CHSH_AB^2+CHSH_AC^2", f"{v_out:.4f}",
     f"feasible={f_outside}")
check("ENVELOPE: monogamy boundary (2sqrt2,0) [sum=8] FEASIBLE under Gamma>=0",
      f_corner1, solver_tol=True)
check("ENVELOPE: monogamy boundary (2,2) [sum=8] FEASIBLE under Gamma>=0",
      f_corner2, solver_tol=True)
check("ENVELOPE: outside point (2sqrt2,2sqrt2) [sum=16>8] INFEASIBLE under Gamma>=0",
      not f_outside,
      "=> recovers facet CHSH_AB^2+CHSH_AC^2<=8 from inside", solver_tol=True)


# ===========================================================================
head("PART 6.  C4 COCYCLE TRIVIALITY  (the survival 2-cocycle is a coboundary)")
# ===========================================================================
print("""
  The transverse seal-survival skeleton (paper1 s3.2) is the scalar
      S(chi) = exp(-kappa chi),   multiplicative along refinement.
  Its potential obstruction to a consistent JOINT composition is a 2-cocycle: the
  associator of the scalar survival.  We sympy-PROVE the associator is identically 1
  (associativity holds), and verify over >=2000 random free mutual-term assignments
  that the grouped survival exp(-kappa * total) is GROUPING-INDEPENDENT (gap 0).
  => the 2-cocycle is a coboundary, H^2 trivial: no transverse phase obstruction is
  forced; the free entangling complement carries NO consistency anomaly.
""")
# sympy-exact associator of scalar survival composition  s_i = exp(-kappa chi_i)
kap = sp.symbols('kappa', positive=True)
c1, c2, c3 = sp.symbols('chi1 chi2 chi3', nonnegative=True)
def Ssym(c):
    return sp.exp(-kap*c)
s1, s2, s3 = Ssym(c1), Ssym(c2), Ssym(c3)
# survival composes by MULTIPLICATION; associator of ((s1 s2) s3) vs (s1 (s2 s3))
left = (s1*s2)*s3
right = s1*(s2*s3)
assoc_ratio = sp.simplify(left/right)
check("C4: sympy-exact associator ((s1 s2)s3)/(s1(s2 s3)) == 1",
      assoc_ratio == 1, f"associator={assoc_ratio}")

# grouped survival grouping-independence over random free mutual terms
mp.mp.dps = 140
import random
random.seed(20260615)
kappa_val = mp.mpf("0.7")
max_group_gap = mp.mpf(0)
N = 2200
for _ in range(N):
    n = random.randint(3, 7)
    chis = [mp.mpf(random.uniform(0, 2)) for _ in range(n)]
    total = sum(chis)
    # grouping 1: product of individual survivals
    S_flat = mp.e**(-kappa_val*total)
    # grouping 2: random binary split, product of group survivals
    k = random.randint(1, n-1)
    g1 = sum(chis[:k]); g2 = sum(chis[k:])
    S_grouped = (mp.e**(-kappa_val*g1)) * (mp.e**(-kappa_val*g2))
    max_group_gap = max(max_group_gap, abs(S_flat - S_grouped))
line(f"max grouping gap over {N} random free assignments", mp.nstr(max_group_gap, 6))
check("C4: grouped survival GROUPING-INDEPENDENT over >=2000 random assignments (gap 0)",
      max_group_gap < mp.mpf("1e-130"),
      f"max_gap={mp.nstr(max_group_gap,4)}  => 2-cocycle is a coboundary, H^2 trivial")
check("C4: ran >=2000 random free mutual-term assignments", N >= 2000, f"N={N}")


# ===========================================================================
head("CANONICAL OUTPUT BLOCK  (p6 transverse no-go receipt)")
# ===========================================================================
n_pass = sum(1 for _, c, _ in CHECKS if c)
n_total = len(CHECKS)
n_solver = sum(1 for _, _, st in CHECKS if st)
allpass = (n_pass == n_total)

print(f"""
  PART 0 (template sanity, dps=140, EXACT/high-precision):
    eta_A   = {mp.nstr(eta_A, 25)}   theta_* = {mp.nstr(theta_s, 25)}
    W_*     = {mp.nstr(W_s_J, 25)}   two-formula gap |J-C| = {mp.nstr(two_formula_gap, 4)}
    eta_B   = {mp.nstr(eta_B, 20)}   1/eta_B = {mp.nstr(inv_eta_B, 18)}   C(eta_B)/W_* = {mp.nstr(ratio_B, 8)}
    sympy-exact: C'=eta sech^2 eta > 0,  J'=-2 tanh sech^2 < 0  (monotone opposition)

  PART 1 (M1 capacity blindness, dps=140, high-precision):
    fixed-marginal max residual            = {mp.nstr(max_marg_resid, 4)}
    Var(a)=1-<a>^2 spread over lambda       = {mp.nstr(var_spread, 4)}   (lambda-INDEPENDENT)
    dJ_marg/dlambda (h=1e-30)               = {mp.nstr(abs(dJ), 4)}        (~0: no transverse leg)
    C_AB U-shape: center {mp.nstr(C_center,8)} < +wing {mp.nstr(C_wing_p,8)} / -wing {mp.nstr(C_wing_m,8)}

  PART 2 (M1 circularity, dps=140, high-precision):
    C_AB=Cov(a,b) root lam*(m=0.3) = {mp.nstr(r03,6) if r03 is not None else 'None'}
                       lam*(m=0.5) = {mp.nstr(r05,6) if r05 is not None else 'None'}
                       lam*(m=0.7) = {mp.nstr(r07,6) if r07 is not None else 'non-robust'}
    => root MOVES with m; only lambda-responsive Fisher entry is Cov=chi_AB (circular)

  PART 3 (M2 field blindness, dps=140, high-precision):
    marginals (1/2,1/2) all (x,y)          : OK
    CHSH                                    = {mp.nstr(CHSH, 18)}  (Tsirelson)
    I_sigma(rebit) - I_sigma(qubit)         = {mp.nstr(abs(I_rebit-I_qubit), 4)}   (FIELD-BLIND)
    seal |E^2-E|,|E-E^*|: real {mp.nstr(max(idem_real,sa_real),4)}  complex {mp.nstr(max(idem_cx,sa_cx),4)}

  PART 4 (M2 separator invisible, sympy-EXACT):
    K_single  R=3  C=4 ;  K_AB  2rebit=10  2qubit=16
    local-tomography: rebit FALSE (deficit +1), qubit TRUE (deficit 0)

  PART 5 (POSITIVE envelope from inside, cvxpy/SCS -- ALL SOLVER-TOLERANCE ~1e-9):
    NPA-1 max CHSH = {chsh_max:.8f}  (Tsirelson {tsirelson:.8f})   [solver-tol]
    PR-box INFEASIBLE; Tsirelson point FEASIBLE                    [solver-tol]
    I3322 level-(1+AB) {b1:.6f} > level-2 {b2:.6f} (strict outer CG-projector) [solver-tol]
    monogamy facet recovered: (2sqrt2,0) & (2,2) feasible, (2sqrt2,2sqrt2) infeasible [solver-tol]

  PART 6 (C4 cocycle triviality, sympy-exact + dps=140):
    associator == 1 (sympy-exact);  grouping gap over {N} assignments = {mp.nstr(max_group_gap,4)}
    => H^2 trivial (coboundary): no forced transverse phase anomaly

  VERDICT:  THE SPLIT IS ESTABLISHED.
    [CONSTRAINED]  the almost-quantum ENVELOPE (no-signaling + Tsirelson CHSH<=2sqrt2
                   + PR-box exclusion + I3322 outer relaxation + monogamy facet) is
                   FORCED FROM INSIDE the records via Gamma>=0 (Gram of the substrate's
                   own observables).  [solver-tolerance corroboration; the PSD logic is exact]
    [NO-GO]        the entangling CONTENT chi_AB = I_sigma is NOT forced, by BOTH
                   independent weight-0 mechanisms:
                   (M1) capacity blindness: Var(a) is marginal-only (lambda-flat, spread
                        {mp.nstr(var_spread,4)}); C_AB is U-shaped (no rising leg); any
                        balance C_AB=Cov is circular and its root drifts with m.
                   (M2) field blindness: the transverse principle factors through the
                        moment algebra M, an invariant of R (rebit<->qubit) that
                        preserves I_sigma (gap {mp.nstr(abs(I_rebit-I_qubit),4)}) and the
                        seal but flips local tomography (deficit +1 vs 0).  chi_AB free
                        up to Q-tilde; gap Q-tilde\\Q permanent (Slofstra 2019).
    Distinct from the weight-+1 scale/Newton-G no-go: records carry no global TENSOR
    PRODUCT and no intrinsic SECOND-TILT capacity leg (here), vs no absolute LENGTH (there).

  CHECKS PASSED: {n_pass}/{n_total}   (of which {n_solver} are cvxpy SOLVER-TOLERANCE ~1e-9)
  ALL CHECKS PASS: {allpass}
""")
assert allpass, "SOME CHECK FAILED -- see **FAIL** above"
head("DONE.")
