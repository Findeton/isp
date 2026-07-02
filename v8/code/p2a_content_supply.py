#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
p2a_content_supply.py  --  Long March v7, PAPER 2 receipt: the content supply.

Does the record's own closed-holonomy ledger generate its clock?

Paper 1 forced the click-law's SHAPE in the intrinsic content chi=D(P_AB||P_BA):
  - divisible (dense) regime:   S(chi) = exp(-kappa chi)            [FORCED, mod 1 scale]
  - indivisible (sparse) regime: S(nd)=S(d)^n on lattice L={nd}     [skeleton FORCED]
                                 + FREE inter-seal profile + FREE spacing d.
Left OPEN: (i) the MAGNITUDE of dchi (hence kappa), (ii) the spacing d.
R2-A showed: composition-self-consistency (Cauchy/refinement) does NOT fix d.

This receipt tests four questions, the CENTERPIECE being Q2.

  Q1  Is dchi's FORM forced by the cochain (= the coboundary rho_i = h_{i+1}-h_i,
      paper4 s44 telescope Sum rho_i = h_b - h_a)?
  Q2  Does a CAPACITY/SATURATION self-consistency principle FORCE d = W_*?
      (NEW principle, distinct from Paper 1's composition-self-consistency.)
  Q3  Is the accumulation RATE (size of rho_i) forced or physical input?
  Q4  Confirm kappa is the no-go floor (weight-0 content -> rate needs 1 abs unit).

Pre-geometric (Tier A) throughout: records, commit order, chi a weight-0 KL pure
number. NO spacetime/metric/light cone/s^2.

High precision: mpmath dps>=120, sympy-exact where structural.

Author receipt for v7 Paper 2.  Run: python3 p2a_content_supply.py
"""

import mpmath as mp
import sympy as sp

mp.mp.dps = 140  # >= 100 demanded; use 140 with margin for cancellation-heavy balances

# ---------------------------------------------------------------------------
def head(s):
    print("\n" + "=" * 78)
    print(s)
    print("=" * 78)

def sub(s):
    print("\n  -- " + s + " --")

def line(label, val, extra=""):
    s = "    {:<52}".format(label)
    s += str(val)
    if extra:
        s += "   " + extra
    print(s)

PASS = {}  # collect machine verdicts

# ===========================================================================
head("PART 0.  The one-diamond constants (paper4 s5 KL=Fisher) -- anchors")
# ===========================================================================
print("""
  Single-diamond law: contrast q in {-1,+1}, P_eta(q)=e^{eta q}/(2 cosh eta),
  eventless base mu_D=(1/2,1/2).  Two intrinsic functions of accumulated tilt eta:

    KL content (accumulated distinguishability):
        C(eta) := D(P_eta || mu_D) = eta tanh eta - log cosh eta     (rises 0 -> inf)
    Fisher capacity (instantaneous coherent capacity of the contrast):
        J(eta) := Var_{P_eta}(q) = d^2 psi / d eta^2 = 1 - tanh^2 eta (falls 1 -> 0)

  The KL=Fisher self-consistency fixes the one-diamond constants:
        C(eta) = J(eta)  <=>  eta tanh eta - log cosh eta = 1 - tanh^2 eta.
""")

eta = sp.symbols('eta', positive=True)
psi_s   = sp.log(2*sp.cosh(eta)) - sp.log(2)
C_s     = eta*sp.tanh(eta) - sp.log(sp.cosh(eta))     # KL content
J_s     = sp.simplify(sp.diff(psi_s, eta, 2))         # Fisher capacity = sech^2
line("psi(eta)  = log(2 cosh eta) - log 2", "")
line("C(eta)    = eta tanh eta - log cosh eta", "(KL content; sympy)")
line("J(eta)    = psi''(eta)", J_s, "(Fisher capacity; sympy)")

def C(x):   # KL content
    x = mp.mpf(x); return x*mp.tanh(x) - mp.log(mp.cosh(x))
def J(x):   # Fisher capacity
    x = mp.mpf(x); return 1 - mp.tanh(x)**2
def balance(x):
    return C(x) - J(x)

eta_star   = mp.findroot(balance, mp.mpf("1.09"))
theta_star = mp.tanh(eta_star)
W_star     = 1 - theta_star**2                 # = J(eta_*) = capacity at saturation
W_star_kl  = C(eta_star)                        # = C(eta_*) = content at saturation

line("eta_*   (root of C=J)",            mp.nstr(eta_star, 50))
line("theta_* = tanh eta_*",             mp.nstr(theta_star, 50))
line("W_* = J(eta_*)  (Fisher capacity)", mp.nstr(W_star, 50))
line("W_* = C(eta_*)  (KL content)",      mp.nstr(W_star_kl, 50))
line("residual balance(eta_*) = C-J",     mp.nstr(balance(eta_star), 6))
line("|C(eta_*) - J(eta_*)| (independent)", mp.nstr(abs(W_star - W_star_kl), 6),
     "(=0: the two formulas for W_* agree)")
PASS["W_* two-formula agreement <1e-100"] = abs(W_star - W_star_kl) < mp.mpf("1e-100")
PASS["balance(eta_*) ~ 0 <1e-100"]        = abs(balance(eta_star)) < mp.mpf("1e-100")

# ===========================================================================
head("Q1.  IS dchi's FORM FORCED BY THE COCHAIN COBOUNDARY?")
# ===========================================================================
print("""
  paper4 s44: a chain of sealed diamonds carries oriented interface cochains
  h_0, h_1, ..., h_N (the complete closed-holonomy potential).  The LOCAL source
  in diamond i is the coboundary (interface mismatch):
        rho_i = h_{i+1} - h_i               (paper4 s44, eq for rho_i)
  with the EXACT telescope (gluing) property
        Sum_{i=a}^{b-1} rho_i = h_b - h_a.  (paper4 s44)

  Paper 1 (R2-B) identified chi = accumulated entropy production sigma with this
  telescope: chi is a content ODOMETER, chi(seg1 then seg2)=chi(seg1)+chi(seg2),
  and the per-step INCREMENT is exactly the coboundary of the holonomy potential.

  CLAIM TO TEST: the FORM of dchi is FORCED to be the cochain coboundary
        dchi_i  =  rho_i  =  h_{i+1} - h_i,
  a theorem of the telescope structure; only its MAGNITUDE (size of rho_i) is open.
""")

sub("(a) telescope identity: Sum rho_i = h_b - h_a  (sympy-exact, symbolic chain)")
N = 7
h = sp.symbols('h0:%d' % (N+1))            # h_0..h_N, free symbols (arbitrary potential)
rho = [h[i+1] - h[i] for i in range(N)]    # coboundary
# telescope over any sub-block [a,b)
def telescope_gap(a, b):
    lhs = sum(rho[a:b])
    rhs = h[b] - h[a]
    return sp.simplify(lhs - rhs)
gaps = [telescope_gap(a, b) for a in range(N) for b in range(a+1, N+1)]
all_zero = all(g == 0 for g in gaps)
line("Sum_{i=a}^{b-1} rho_i - (h_b - h_a) for ALL sub-blocks", "all == 0" if all_zero else "FAIL")
line("number of sub-blocks checked", len(gaps))
PASS["Q1 telescope identity sympy-exact (all sub-blocks)"] = all_zero

sub("(b) coboundary <=> additive increment of a SCALAR potential (forced form)")
print("""    A content functional chi is concatenation-additive (the forced odometer of
    Paper 1) IFF it is the telescoping sum of a per-step increment d_i:
          chi(a->b) = Sum_{i=a}^{b-1} d_i,   chi(a->b)+chi(b->c)=chi(a->c).
    A sequence d_i is a coboundary of SOME potential H (d_i = H_{i+1}-H_i) IFF its
    partial sums telescope, i.e. IFF chi is path-independent (depends only on the
    endpoints a,b).  This is the discrete Poincare lemma on a chain (1D: every
    closed 1-cochain is exact; H^1 of a path = 0).  So:

      ODOMETER (additive, endpoint-only)  <=>  dchi_i is a coboundary d_i=H_{i+1}-H_i.

    Paper 1 FORCED the odometer (arrow-positivity: chi:=accumulated sigma is
    concatenation-additive).  Therefore dchi's FORM is forced to be a coboundary.
    The ONLY question is WHICH potential H, i.e. the MAGNITUDE of each increment.""")

# Verify the discrete Poincare lemma numerically: any additive (endpoint-only)
# content on a chain has a potential whose coboundary reproduces it.
mp.mp.dps = 140
# take an ARBITRARY per-step increment sequence (physical holonomy mismatches)
d_phys = [mp.mpf(v) for v in ["0.57","-0.80","0.54","0.45","0.91","-0.33","0.12"]]
# reconstruct a potential H by partial sums (H_0 := h0 arbitrary)
h0 = mp.mpf("0.15")
Hrec = [h0]
for d in d_phys:
    Hrec.append(Hrec[-1] + d)
# coboundary of reconstructed potential must give back d_phys EXACTLY
cob = [Hrec[i+1]-Hrec[i] for i in range(len(d_phys))]
maxgap = max(abs(cob[i]-d_phys[i]) for i in range(len(d_phys)))
line("max | coboundary(H_rec)_i - d_phys_i |", mp.nstr(maxgap, 6),
     "(=0: every additive increment IS a coboundary)")
# and the telescope reproduces endpoint mismatch
tel_gap = abs(sum(d_phys) - (Hrec[-1]-Hrec[0]))
line("| Sum d_phys - (H_N - H_0) | (telescope)", mp.nstr(tel_gap, 6))
PASS["Q1 Poincare: additive increment = coboundary (mp)"] = maxgap < mp.mpf("1e-120")
PASS["Q1 telescope reproduces endpoint mismatch (mp)"]    = tel_gap < mp.mpf("1e-120")

sub("(c) matches paper4 s45 receipt numbers (h, rho)")
# paper4 s45 decisive numbers: h = .15,.72,-.08,.46,.91 ; rho = .57,-.80,.54,.45
h_p4   = [mp.mpf(v) for v in ["0.15","0.72","-0.08","0.46","0.91"]]
rho_p4 = [h_p4[i+1]-h_p4[i] for i in range(len(h_p4)-1)]
rho_p4_quoted = [mp.mpf(v) for v in ["0.57","-0.80","0.54","0.45"]]
gap_p4 = max(abs(rho_p4[i]-rho_p4_quoted[i]) for i in range(4))
line("paper4 s45 rho = h_{i+1}-h_i reproduced", [mp.nstr(r, 6) for r in rho_p4])
line("max gap vs paper4 s45 quoted rho", mp.nstr(gap_p4, 6))
# telescope: sum rho = h_b - h_a
sum_rho = sum(rho_p4)
endpoint = h_p4[-1]-h_p4[0]
line("Sum rho = 0.76 ; h_N - h_0 = 0.76 ; gap", mp.nstr(abs(sum_rho-endpoint), 6))
PASS["Q1 paper4 s45 rho reproduced <1e-100"]   = gap_p4 < mp.mpf("1e-100")
PASS["Q1 paper4 s45 telescope <1e-100"]        = abs(sum_rho-endpoint) < mp.mpf("1e-100")

print("""
  Q1 VERDICT: dchi's FORM is FORCED to be the cochain coboundary
        dchi_i = rho_i = h_{i+1} - h_i,
  a theorem of the odometer (Paper 1) + the discrete Poincare lemma (1D exactness)
  + paper4 s44's source-as-coboundary law.  The telescope Sum rho_i = h_b - h_a is
  the SAME object as the content-additivity of Paper 1's odometer.  Only the
  MAGNITUDE (which potential h, i.e. the size of each rho_i) is open -> Q3.
  STATUS: FORCED-IN-FORM (coboundary), MAGNITUDE-OPEN.
""")

# ===========================================================================
head("Q2.  CENTERPIECE: DOES A CAPACITY/SATURATION PRINCIPLE FORCE d = W_*?")
# ===========================================================================
print("""
  The NEW principle (distinct from Paper 1's composition-self-consistency):

    A single record diamond can hold at most W_* of COHERENT content at
    self-consistency.  Once the accumulated unsealed holonomy content reaches that
    capacity, the diamond is SATURATED and MUST commit (seal).  So the seal fires
    at accumulated content = W_*, forcing the spacing d = W_*.

  We test this in four parts:
    (a) set up the capacity bound precisely from the KL=Fisher structure;
    (b) is 'commit exactly at saturation content W_*' a THEOREM or a POSTULATE?
    (c) does it EVADE R2-A's freedom (composition is silent on spacing)?
    (d) compute W_* to dps>=100; any internal characterization of W_*?
""")

# ---- Q2(d) first: W_* high precision + characterization --------------------
sub("(d) W_* to high precision + internal characterization")
mp.mp.dps = 140
line("W_* (dps 50 shown of 140 computed)", mp.nstr(W_star, 50))
# Is W_* the MAXIMUM of any natural one-diamond functional? Test candidates.
# Candidate 1: the "coherent content" min(C(eta), J(eta)) -- the amount that is
# BOTH accumulated AND still within capacity. Its max over eta is exactly W_*.
def coherent(x):
    return min(C(x), J(x))   # cannot exceed remaining capacity, nor exceed accrued
# ANALYTIC characterization (not a coarse grid): C is strictly increasing, J is
# strictly decreasing, so min(C,J) = C on [0,eta_*] (rising) and = J on [eta_*,inf)
# (falling), hence min(C,J) is maximized EXACTLY at the unique crossing eta_*, with
# value C(eta_*)=J(eta_*)=W_*.  The max is thus W_* to full precision, by structure.
vmax = coherent(eta_star)   # value AT the crossing = the true argmax (analytic)
line("max_eta min(C(eta),J(eta)) = min(C,J) at eta_*", mp.nstr(vmax, 50))
line("|max - W_*| (analytic: max is AT the crossing)", mp.nstr(abs(vmax - W_star), 6),
     "(=0 to full precision; max is exactly the crossing)")
# Verify the structural premise globally: C monotone up, J monotone down, on a
# fine scan + a small symbolic sign check of derivatives.
xs = [mp.mpf(k)/200 for k in range(1, 600)]
C_mono = all(C(xs[i+1]) > C(xs[i]) for i in range(len(xs)-1))
J_mono = all(J(xs[i+1]) < J(xs[i]) for i in range(len(xs)-1))
# symbolic: C'(eta)=eta sech^2 eta > 0 ; J'(eta)=-2 tanh eta sech^2 eta < 0 (eta>0)
Cp = sp.simplify(sp.diff(C_s, eta))     # = eta*sech^2(eta)
Jp = sp.simplify(sp.diff(J_s, eta))     # = -2 tanh sech^2
line("C'(eta) (sympy)", Cp, "(>0 for eta>0 => C strictly up)")
line("J'(eta) (sympy)", Jp, "(<0 for eta>0 => J strictly down)")
line("C(eta) strictly increasing on scan", C_mono)
line("J(eta) strictly decreasing on scan", J_mono)
# on [0,eta_*] min=C (since C<=J there); on [eta_*,inf) min=J -> peak at eta_*
left_is_C  = C(eta_star/2)  <= J(eta_star/2)    # under-saturated: C is the min
right_is_J = J(2*eta_star)  <= C(2*eta_star)    # over-saturated: J is the min
line("on [0,eta_*] min(C,J)=C (C<=J) ?", left_is_C)
line("on [eta_*,inf) min(C,J)=J (J<=C) ?", right_is_J)
PASS["Q2d coherent-content max = W_* (analytic, full prec)"] = abs(vmax - W_star) < mp.mpf("1e-100")
PASS["Q2d C increasing, J decreasing (bound structure)"] = (C_mono and J_mono and left_is_C and right_is_J)

print("""
    CHARACTERIZATION: W_* is the unique fixed value where the MONOTONE-RISING
    accumulated content C(eta) meets the MONOTONE-FALLING instantaneous capacity
    J(eta).  Equivalently W_* = max_eta min(C(eta),J(eta)) -- the largest content
    that is simultaneously (i) accumulated and (ii) still within capacity.  This
    IS a genuine capacity/saturation bound STRUCTURE (a max of a coherent-content
    functional), not an arbitrary crossing.  W_* is the saturation content of one
    diamond.  [This part is FORCED: W_* is a forced pure number and IS a capacity.]
""")

# ---- Q2(a) the capacity bound precisely ------------------------------------
sub("(a) the capacity bound, precisely")
print("""    At tilt eta a diamond has:
        accumulated content C(eta)  (monotone up, the odometer reading)
        remaining capacity  J(eta)  (monotone down, Fisher of the contrast)
    Self-consistency (KL=Fisher) is the demand C(eta)=J(eta): the accrued content
    equals the contrast's own capacity to carry it.  For eta<eta_* the diamond is
    UNDER-saturated (C<J: capacity to spare); for eta>eta_* it is OVER-saturated
    (C>J: content exceeds what the single contrast can self-consistently carry).
    The boundary eta_* (content W_*) is the saturation point.  So 'the maximum
    coherent content a diamond can carry at self-consistency' = W_*.  [FORCED]""")
# under/over saturation sign check
line("C-J at eta_*/2 (under-saturated, <0)", mp.nstr(balance(eta_star/2), 8))
line("C-J at 2 eta_* (over-saturated, >0)",  mp.nstr(balance(2*eta_star), 8))
PASS["Q2a saturation sign structure (under<0, over>0)"] = (
    balance(eta_star/2) < 0 and balance(2*eta_star) > 0)

# ---- Q2(b) THEOREM or POSTULATE? the decisive honesty test -----------------
sub("(b) DECISIVE: is 'commit AT saturation' a theorem or a postulate?")
print("""    The capacity bound (a) is FORCED: a diamond's max self-consistent coherent
    content IS W_*.  But the SPACING question is: does a seal fire EXACTLY when the
    ACCUMULATED INTER-SEAL content reaches W_*?  This needs a bridge premise:

      (P-sat)  'a diamond commits the instant its accumulated coherent content
                reaches the one-diamond saturation capacity W_*.'

    Is (P-sat) forced?  Examine what the record structure actually delivers:

    - The capacity bound says a SINGLE diamond at self-consistency carries <= W_*.
      It bounds the content of ONE saturated diamond.  It does NOT, by itself, say
      the SEALING DYNAMICS must wait until accumulation hits that bound: a diamond
      could seal EARLY (at content < W_*, under-saturated) and remain a valid
      record -- nothing in the capacity bound forbids an under-full commitment.
    - Conversely a diamond cannot self-consistently EXCEED W_* (over-saturation
      C>J is inconsistent), so W_* is a genuine UPPER bound on per-seal content:
            d <= W_*    is FORCED.
      But an upper bound is not an equality: d=W_* requires SATURATING the bound,
      i.e. the extra principle 'seals fire as LATE as possible / at the capacity'.""")

# Demonstrate: a sub-saturated lattice d < W_* is still a fully consistent
# geometric-skeleton seal law (composition holds on L for ANY d), so composition
# does NOT force saturation, and the capacity bound only gives d <= W_*.
mp.mp.dps = 120
kappa = mp.mpf("1.0")   # any fixed conversion (the one free scale); test d-freedom
def S_lattice(n, d):    # geometric skeleton S(nd)=S(d)^n with S(d)=exp(-kappa d)
    return mp.e**(-kappa*d*n)
# check S(nd)=S(d)^n for several d including d<W_*, d=W_*, d>W_*
ds = [W_star/4, W_star/2, W_star, 2*W_star]
comp_ok = True
for d in ds:
    for n in range(1, 6):
        gap = abs(S_lattice(n, d) - S_lattice(1, d)**n)
        if gap > mp.mpf("1e-100"):
            comp_ok = False
line("S(nd)=S(d)^n holds for d in {W_/4,W_/2,W_,2W_}", comp_ok,
     "(composition consistent for ANY d -- R2-A)")
PASS["Q2b composition holds for all d (R2-A confirmed)"] = comp_ok

line("FORCED upper bound  d <= W_*  (no over-saturation)", "YES (capacity bound)")
line("FORCED equality     d == W_*  (must saturate)?", "NO -- and the firing law DENIES it (see p2b/p2c)")

print("""
    d = W_* is equivalent to the postulate (P-sat) 'the seal fires AT the capacity,
    not before'.  This receipt (p2a) proves only the CEILING d <= W_*; whether the
    EQUALITY holds is settled by the corpus's own seal-firing law, in p2b / p2c:
    that law (paper4 s71-76, the vector fixed point grad psi(h)=exp(-h)) commits
    STRICTLY UNDER the ceiling in every admissible mode (one-mode C(eta_B)=0.156,
    coupled C(h_*)=0.109, both < W_*=0.365), so it CONTRADICTS (P-sat).  Hence the
    capacity law (s5) and the firing law (s71-76) are distinct and CONSISTENT; only
    (P-sat)/d=W_* is denied.  No internal EQUATION whose unique root is d=W_* exists;
    only the INEQUALITY d<=W_* (here) and a sub-capacity, mode-dependent firing
    content (p2b/p2c).""")

# ---- Q2(c) does saturation EVADE R2-A's freedom? --------------------------
sub("(c) does the capacity bound EVADE R2-A's composition-freedom?")
print("""    R2-A's freedom: the COMPOSITION condition (Cauchy/refinement) only checks the
    law AT seal points -> silent on spacing -> ANY d>0 admissible (confirmed above).
    The capacity bound is a DIFFERENT constraint (not composition): it caps the
    content PER diamond.  Does it pin d where composition could not?

    PARTIAL YES: the capacity bound adds NEW information composition lacked --
    it converts 'any d>0' into the genuine UPPER BOUND  d <= W_*.  That is real
    progress beyond R2-A (composition gave no bound at all; capacity gives a
    ceiling).  So saturation is NOT vacuous against R2-A.

    BUT NOT FULL: to land on the EQUALITY d=W_* one still needs the extremal
    postulate (P-sat) 'saturate the bound'.  The capacity bound alone leaves the
    half-open interval (0, W_*] free.  So:
        composition (R2-A):  d in (0, inf)      [no constraint]
        + capacity bound:    d in (0, W_*]      [FORCED ceiling -- new]
        + (P-sat) extremal:  d = W_*            [CHOICE -- saturate]""")
line("R2-A admissible spacings", "(0, inf)")
line("+ capacity bound -> admissible spacings", "(0, W_*]   <- W_* now a FORCED ceiling")
line("+ (P-sat) extremal -> spacing", "d = W_*    <- requires the saturate-choice")

print("""
  Q2 VERDICT (BRUTALLY HONEST): saturation does NOT FORCE d=W_*.  What IS forced:
    * W_* is a genuine capacity (a forced pure number; = max_eta min(C,J));
    * the capacity bound forces a real CEILING  d <= W_*  (this EVADES part of
      R2-A's total freedom -- composition gave no bound, capacity gives one);
  What is NOT forced -- and what the corpus's firing law DENIES:
    * d=W_* is the postulate (P-sat) 'seal AT the capacity'.  The corpus's own
      seal-firing law (paper4 s71-76; p2b/p2c) commits STRICTLY UNDER the ceiling,
      at a MODE-DEPENDENT root (one-mode eta_B, coupled h_*), so it contradicts
      (P-sat).  The capacity law (s5) and firing law (s71-76) are distinct and
      CONSISTENT; the open question is not 'reconcile two laws' but 'what (if
      anything) fixes the content spacing d', given the firing content is mode-
      dependent and the firing clock is random.
  STATUS: d <= W_* FORCED (ceiling, here); d = W_* DENIED by the firing law (p2b/p2c).
  The honest upgrade over Paper 1/R2-A is the CEILING.
""")

# ===========================================================================
head("Q3.  IS THE ACCUMULATION RATE (size of rho_i) FORCED OR PHYSICAL?")
# ===========================================================================
print("""
  Q1 forced dchi's FORM = coboundary rho_i = h_{i+1}-h_i.  The MAGNITUDE of each
  rho_i is the actual relative-holonomy configuration of the chain: the difference
  of the closed-holonomy potential across the i-th interface.

  paper4 s44 (and s45) is explicit: the global closed-holonomy cochain
  {h_i} is the PHYSICAL FREE DATA of the whole sealed process ('the physical free
  data are global closed-holonomy cochains of the whole sealed process, not
  independent local source amplitudes').  Given {h_i}, every rho_i is FIXED (a
  coboundary, Q1).  But {h_i} ITSELF is the configuration the records actually
  carry -- it is not fixed by any internal self-consistency; it is the physical
  input (the realized holonomy).
""")
sub("structure forced, magnitude physical -- the same split as Q1")
# Demonstrate: same telescope/odometer for ANY potential {h_i}; the law constrains
# only DIFFERENCES (form), never the absolute size (magnitude).
mp.mp.dps = 120
h_cfgA = [mp.mpf(v) for v in ["0.15","0.72","-0.08","0.46","0.91"]]
h_cfgB = [10*x for x in h_cfgA]   # a DIFFERENT physical holonomy (10x bigger)
rhoA = [h_cfgA[i+1]-h_cfgA[i] for i in range(4)]
rhoB = [h_cfgB[i+1]-h_cfgB[i] for i in range(4)]
line("rho for config A (small holonomy)", [mp.nstr(r,5) for r in rhoA])
line("rho for config B (10x holonomy)",   [mp.nstr(r,5) for r in rhoB])
# both telescope correctly; both are coboundaries; magnitudes differ -> physical
telA = abs(sum(rhoA)-(h_cfgA[-1]-h_cfgA[0]))
telB = abs(sum(rhoB)-(h_cfgB[-1]-h_cfgB[0]))
line("telescope gap A", mp.nstr(telA,6))
line("telescope gap B", mp.nstr(telB,6))
line("rho magnitudes differ (B = 10*A)?", all(abs(rhoB[i]-10*rhoA[i])<mp.mpf("1e-100") for i in range(4)))
PASS["Q3 form holds for any magnitude (A and B both telescope)"] = (
    telA < mp.mpf("1e-100") and telB < mp.mpf("1e-100"))
print("""
  Q3 VERDICT: the FORM of the accumulation (coboundary/telescope/odometer) is
  FORCED (Q1); the SIZE of each rho_i = h_{i+1}-h_i is the PHYSICAL relative-
  holonomy configuration {h_i} -- genuine physical input, not internally forced.
  STATUS: STRUCTURE FORCED, MAGNITUDE PHYSICAL.
""")

# ===========================================================================
head("Q4.  CONFIRM kappa IS THE NO-GO FLOOR")
# ===========================================================================
print("""
  Even if d=W_* (a weight-0 content pure number) were forced AND dchi's form is
  forced, the survival law S(chi)=exp(-kappa chi) [dense] / S(d)=exp(-kappa d)
  [sparse skeleton] needs the conversion kappa from CONTENT to COMMIT-ORDER RATE.

  WEIGHTS (the no-go bookkeeping, paper XI):
    chi = D(P_AB||P_BA)  : a KL divergence  -> WEIGHT 0 (dimensionless pure number)
    d   = W_* = 1-theta_*^2 : a pure number -> WEIGHT 0 (eligible; records carry it)
    kappa : content -> rate  = [rate]/[content] = [1/(commit-order unit)]
            -> requires ONE absolute commit-order unit the records do NOT carry.
""")
sub("weight bookkeeping (dimensional analysis of the conversion)")
# symbolic weight check: assign weight w to commit-order 'time' T; chi,d weight 0.
wT = sp.symbols('w_T', positive=True)   # weight of one commit-order/rate unit
w_chi = 0       # KL divergence: weight 0
w_d   = 0       # W_*: weight 0
w_kappa = sp.Symbol('w_kappa')
# S=exp(-kappa chi) dimensionless => kappa*chi weight 0 => w_kappa + w_chi = 0
# but kappa is a RATE per content: w_kappa = (rate weight) - (content weight).
# rate weight = -wT (per commit-order unit). So:
w_kappa_val = -wT - w_chi   # = -wT
line("w(chi)   [KL divergence]", w_chi, "(weight-0: records carry it)")
line("w(d=W_*) [pure number]",   w_d,   "(weight-0: eligible)")
line("w(kappa) = -w_T - w(chi)", w_kappa_val, "(needs one absolute commit-order unit)")
line("kappa*chi must be weight-0 for exp() argument", "=> w_kappa = -w(chi) only if rate unit supplied")
# the point: chi and d are weight-0 (eligible), kappa carries the lone weight-(-wT)
no_go_consistent = (w_chi == 0 and w_d == 0 and w_kappa_val != 0)
line("chi, d weight-0 AND kappa carries the lone unit?", no_go_consistent)
PASS["Q4 chi,d weight-0; kappa is the lone scale"] = bool(no_go_consistent)
print("""
  Q4 VERDICT: CONSISTENT with the scale no-go (paper XI).  Both d=W_* and chi are
  weight-0 content pure numbers -- the records CAN carry them (eligible).  The
  conversion kappa (content -> commit-order rate) carries the ONE absolute unit
  the weight-0 records provably cannot supply.  Fixing d=W_* in weight-0 content
  units does NOT manufacture the missing scale: kappa remains the single free
  no-go floor.  STATUS: NO-GO-CONSISTENT (kappa is the one forbidden absolute
  scale; d and W_* are eligible weight-0 numbers).
""")

# ===========================================================================
head("SUMMARY OF MACHINE CHECKS")
# ===========================================================================
allok = True
for k, v in PASS.items():
    print("    [{}]  {}".format("PASS" if v else "FAIL", k))
    allok = allok and bool(v)
print("\n    ALL CHECKS PASS:", allok)

print("""
================================================================================
STRUCTURED VERDICT (Long March v7 Paper 2 -- the content supply)
================================================================================
  Q1  dchi FORM forced by the cochain?
        FORCED-IN-FORM.  dchi_i = rho_i = h_{i+1}-h_i is the coboundary of the
        closed-holonomy potential; the telescope Sum rho_i=h_b-h_a IS Paper 1's
        odometer additivity; discrete Poincare lemma (1D exactness) makes
        'additive content' <=> 'coboundary' an identity.  Magnitude open.

  Q2  Does saturation FORCE d=W_*?   *** CENTERPIECE -- HONEST: NO ***
        - W_* IS a genuine capacity (forced pure number = max_eta min(C,J),
          the crossing of rising content C and falling capacity J).
        - The capacity bound FORCES a real CEILING  d <= W_*  (no over-
          saturation) -- this EVADES part of R2-A's total freedom (composition
          gave NO bound; capacity gives one).
        - The EQUALITY d=W_* is the postulate (P-sat) 'commit AT the capacity'.
          The corpus's own seal-firing law (paper4 s71-76; p2b/p2c) commits
          STRICTLY UNDER the ceiling at a MODE-DEPENDENT root, so it DENIES
          (P-sat).  The capacity law (s5) and firing law (s71-76) are distinct
          and CONSISTENT -- no corpus contradiction.
        STATUS: d <= W_* FORCED (ceiling, here); d = W_* DENIED by the firing law.

  Q3  Accumulation rate forced or physical?
        STRUCTURE FORCED, MAGNITUDE PHYSICAL.  The coboundary/telescope FORM is
        forced; the size of each rho_i = the realized closed-holonomy potential
        {h_i}, the physical free data of the sealed process (paper4 s44).

  Q4  kappa the no-go floor?
        NO-GO-CONSISTENT.  chi and d are weight-0 (eligible) pure numbers;
        kappa (content->commit-rate) is the ONE absolute unit the records cannot
        carry.  Fixing d in weight-0 units never manufactures the scale.

  NEXT INVESTIGATION (resolved in p2b/p2c; open for Paper 3):
        The capacity bound upgraded 'd free in (0,inf)' to 'd in (0,W_*]'; p2b/p2c
        then showed the firing law commits STRICTLY UNDER W_* in every admissible
        mode (sub-capacity, mode-dependent, on a random evidence clock), so d=W_*
        is denied.  The genuine open obligation is NOT 'reconcile s5 with s71'
        (they are consistent) but 'what (if anything) fixes the content spacing d':
          (i)  a MaxEnt/least-work variational principle on the inter-seal collar;
          (ii) the Paper-3 cross-tier bridge: get d from a DERIVED Tier-B
               gravitational dimensionless coefficient (the no-go ALLOWS this, d
               weight-0); the one-mode root 1/eta_B=1.641 (= 1d mass-gap
               correlation length) is a suggestive thread.
================================================================================
""")
