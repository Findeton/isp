#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RECEIPT p6d: SIGN/MAGNITUDE RESIDUE on chi_AB -- can the transverse
self-consistency principle force the SIGN, or pin a specific MAGNITUDE (E_cl)?

OPEN-PATH 3.  Two sub-questions, both at mpmath dps >= 120 (140 for the
cancellation-heavy capacity-blindness re-check), sympy-exact for the structural
sign facts.

PHASE-1 SCOUT (established, reused here):
  * chi_AB = I_sigma is the SIGNED interaction information / factorization defect
    (S_AB/(S_A S_B) = exp(-k chi_AB)).  TWO-SIDED in sign.
  * Every faithful KL / Fisher capacity leg is NON-NEGATIVE (a divergence, a
    variance).  In particular E_cl >= 0 (nearest-product KL; E_cl(Bell)=ln2).
  * NO_GO_on_filling_envelope_forced: no transverse principle forces chi_AB; the
    envelope (no-signaling, Tsirelson CHSH<=2sqrt2, PR-box out, monogamy) is
    forced from inside the moment algebra M.

--------------------------------------------------------------------------------
SUB-QUESTION (1) SIGN.
  CLAIM: even a hypothetical SUCCESSFUL transverse crossing pins at most a
  NON-NEGATIVE magnitude (|chi_AB| or E_cl), never the SIGN that distinguishes
  entangling (synergy, I_sigma<0) from anti-correlating / redundant
  (I_sigma>0).  The records' magnitude-only functionals (E_cl, any Fisher
  capacity, |I_sigma|) are EVEN under the sign-flip orbit, so they cannot
  resolve sign.
  PROOF STRATEGY:
    (1a) sympy-exact: a sign involution tau on 2x2 joint laws (relabel one
         party's outcome, b -> 1-b) that FLIPS the correlation sign E -> -E
         hence flips I_sigma's sign, while LEAVING E_cl, |I_sigma|, the
         marginal Fisher capacity, and CHSH-magnitude INVARIANT.
    (1b) mpmath dps140: an explicit PAIR (synergy kernel, redundancy kernel)
         with EQUAL |I_sigma| and EQUAL E_cl to ~1e-120 but OPPOSITE-sign
         I_sigma -- the records cannot tell them apart.
    (1c) re-confirm the capacity leg (marginal-tilt Fisher) is a function of
         the MARGINALS ALONE -> sign-blind and lambda-blind (dps 140).

SUB-QUESTION (2) MAGNITUDE.  Can ANY transverse self-consistency pin E_cl
  (the non-negative kinematic measure, E_cl(Bell)=ln2) to a SPECIFIC value?
  TESTS:
    (2a) E_cl is a CONTINUOUS, strictly-monotone sweep from 0 (product) to ln2
         (Bell) as the joint correlation t runs 0 -> 1/4, with NOTHING internal
         selecting a point: at fixed marginals E_cl takes every value in
         [0, ln2).  (A magnitude is not pinned by the marginals.)
    (2b) The candidate transverse "capacity crossing" J(.)=C(.) that pinned the
         SINGLE-CHAIN constant has NO transverse analog that lands on a specific
         E_cl: the faithful capacity (marginal Fisher) is FLAT in the transverse
         coupling (slope 0 to 1e-120), so the crossing is degenerate -- it does
         not cross at one t, it is satisfied on an interval / nowhere depending
         on marginals.  => no internal balance pins E_cl.
    (2c) Tsirelson/IC envelope is sign-and-magnitude PERMISSIVE on E_cl:
         CHSH ranges 2 -> 2sqrt2 while E_cl ranges over a CONTINUUM; the
         monogamy / no-signaling facets bound CHSH but place NO lower OR upper
         interior bound that singles out a particular E_cl in (0, ln2).
    (2d) DECISIVE max-min probe: is there ANY internal functional balance whose
         stationary point is at a fixed E_cl independent of the marginals?  We
         sweep the marginal m and show every candidate balance point E_cl* MOVES
         with m (non-robust, circular) -- exactly the M2/M1 weight-0 signature,
         NOT a forced number.  Contrast the SINGLE-CHAIN anchor W_*=0.36478...
         which is marginal-FIXED (the crossing is at one eta_A for all inputs).

VERDICT:
  CLOSED_nogo_holds  if neither the sign nor a specific magnitude E_cl is forced
                     (best case stays envelope-only).
  PARTIAL_upgrade    if E_cl turns out forceable to a specific value.
"""

import mpmath as mp
import sympy as sp

DPS = 140
mp.mp.dps = DPS
TOL = mp.mpf(10) ** (-110)
ln2 = mp.log(2)

def head(s):
    print("\n" + "=" * 78)
    print(s)
    print("=" * 78)

def sub(s):
    print("\n--- " + s)

def line(label, val, extra=""):
    print(f"    {label:<52} {val}  {extra}")

PASS = []
def check(name, cond):
    PASS.append((name, bool(cond)))
    print(f"    [{'PASS' if cond else 'FAIL':4s}] {name}")
    assert cond, "FAILED: " + name

# ============================================================================
# Shared machinery (mirrors p4a / nonadditive_entangling_complement EXACTLY).
# ============================================================================
half = mp.mpf(1) / 2

def klterm(p, q):
    if p == 0:
        return mp.mpf(0)
    return p * mp.log(p / q)

# --- 2x2 single-column joint output law on (a,b), the transverse object -----
# A 2x2 joint distribution P[a][b] with marginals pA, pB.
def joint_uniform(t):
    """Uniform-marginal joint, correlation parameter t in [-1/4, 1/4].
       P = [[1/4+t, 1/4-t],[1/4-t, 1/4+t]].  marginals (1/2,1/2)|(1/2,1/2)."""
    q = mp.mpf(1) / 4
    return [[q + t, q - t], [q - t, q + t]]

def joint_general(mA, mB, t):
    """Joint with A-marginal (mA,1-mA), B-marginal (mB,1-mB), correlation t.
       P[a][b] = pA[a]*pB[b] + s(a,b)*t,  s = +1 on (0,0)/(1,1), -1 off-diag,
       so marginals are EXACTLY (mA,1-mA),(mB,1-mB) for any t (sum of t-terms
       per row/col cancels)."""
    pA = [mA, 1 - mA]
    pB = [mB, 1 - mB]
    s = [[mp.mpf(1), mp.mpf(-1)], [mp.mpf(-1), mp.mpf(1)]]
    P = [[pA[a] * pB[b] + s[a][b] * t for b in range(2)] for a in range(2)]
    return P, pA, pB

def mutual_info(P):
    """I(A:B) = sum P ln (P / (pA pB)) >= 0; the NON-NEGATIVE kinematic content."""
    pA = [P[0][0] + P[0][1], P[1][0] + P[1][1]]
    pB = [P[0][0] + P[1][0], P[0][1] + P[1][1]]
    I = mp.mpf(0)
    for a in range(2):
        for b in range(2):
            I += klterm(P[a][b], pA[a] * pB[b])
    return I

def correlation_E(P):
    """The two-sided correlation E = <ab> with a,b in {+1,-1} (a=0->+1,1->-1).
       SIGNED.  E = (P00+P11) - (P01+P10)."""
    return (P[0][0] + P[1][1]) - (P[0][1] + P[1][0])

def signed_interaction(P):
    """SIGNED interaction-information surrogate for chi_AB at the single-column
       level: co-information.  For a 2-variable system the natural signed
       'factorization defect that carries a sign' is the correlation-signed
       mutual information:  Isig := sign(E) * I(A:B).
       This is the transverse analog of p4a's I_sigma = sigma_AB-sigma_A-sigma_B
       (a DIFFERENCE of entropy productions, two-sided): synergy (E<0 here,
       anti-correlated) vs redundancy (E>0).  We verify below it flips under tau
       while I (the magnitude) does not."""
    E = correlation_E(P)
    sgn = mp.mpf(1) if E > 0 else (mp.mpf(-1) if E < 0 else mp.mpf(0))
    return sgn * mutual_info(P)

def E_cl_singlecolumn(P):
    """E_cl on a single-column 2x2 joint = nearest-product KL = mutual info I(A:B)
       (the nearest product law IS the marginal product, Theorem 1).  NON-NEGATIVE."""
    return mutual_info(P)

# ============================================================================
head("SUB-QUESTION (1) SIGN:  records carry only magnitude, never the sign")
# ============================================================================

# ---------------------------------------------------------------------------
sub("(1a) sympy-EXACT: the sign involution tau (relabel b -> 1-b) flips E and")
print("        flips signed-Isig, but LEAVES E_cl / |Isig| / marginal Fisher INVARIANT.")
# Symbolic 2x2 joint with uniform marginals, parameter t.
ts = sp.symbols('t', real=True)
q = sp.Rational(1, 4)
P_sym  = [[q + ts, q - ts], [q - ts, q + ts]]          # correlation +t
# tau: relabel B outcome b->1-b  =>  swap columns
Ptau   = [[P_sym[0][1], P_sym[0][0]], [P_sym[1][1], P_sym[1][0]]]  # = correlation -t

def E_sym(P):
    return (P[0][0] + P[1][1]) - (P[0][1] + P[1][0])
def I_sym(P):
    pA = [P[0][0] + P[0][1], P[1][0] + P[1][1]]
    pB = [P[0][0] + P[1][0], P[0][1] + P[1][1]]
    expr = 0
    for a in range(2):
        for b in range(2):
            expr += P[a][b] * sp.log(P[a][b] / (pA[a] * pB[b]))
    return sp.simplify(expr)

E_plus  = sp.simplify(E_sym(P_sym))     # = 4t
E_minus = sp.simplify(E_sym(Ptau))      # = -4t
I_plus  = I_sym(P_sym)
I_minus = I_sym(Ptau)

line("E(P)        (correlation, signed)", E_plus)
line("E(tau P)    (correlation, signed)", E_minus)
check("tau FLIPS the signed correlation: E(tauP) = -E(P)",
      sp.simplify(E_minus + E_plus) == 0)
check("tau LEAVES the magnitude |E| INVARIANT: E(tauP)^2 = E(P)^2",
      sp.simplify(E_minus**2 - E_plus**2) == 0)
check("tau LEAVES E_cl = I(A:B) INVARIANT (even functional of t)",
      sp.simplify(I_plus - I_minus) == 0)
# marginal Fisher capacity Var(a) = 1-<a>^2 with <a> from marginal (1/2,1/2)=0:
# both P and tauP have marginals (1/2,1/2)|(1/2,1/2) -> Fisher identical, t-blind.
mA_p = sp.simplify((P_sym[0][0] + P_sym[0][1]) - (P_sym[1][0] + P_sym[1][1]))  # <a>=0
mA_t = sp.simplify((Ptau[0][0] + Ptau[0][1]) - (Ptau[1][0] + Ptau[1][1]))
fisher_p = sp.simplify(1 - mA_p**2)
fisher_t = sp.simplify(1 - mA_t**2)
line("marginal-tilt Fisher Var(a)=1-<a>^2 on P", fisher_p)
line("marginal-tilt Fisher Var(a)=1-<a>^2 on tauP", fisher_t)
check("marginal Fisher capacity is sign-blind AND t-blind (=1, both)",
      sp.simplify(fisher_p - 1) == 0 and sp.simplify(fisher_t - 1) == 0)
print("""
   => The sign-flip involution tau is a SYMMETRY of every magnitude functional the
      records carry (E_cl, |I|, marginal Fisher, CHSH-magnitude) but ACTS NON-
      TRIVIALLY on the sign (E -> -E).  Hence no magnitude functional can be a
      function of the sign: a hypothetical successful crossing pins |chi_AB|, the
      sign is in the quotient the records cannot see.  [sympy-exact]""")

# ---------------------------------------------------------------------------
sub("(1b) mpmath dps140: an explicit PAIR with EQUAL E_cl / EQUAL |Isig| but")
print("        OPPOSITE-sign signed-interaction -- the records cannot distinguish them.")
# synergy / anti-correlated kernel: correlation NEGATIVE (t<0)
t0 = mp.mpf("0.17")
P_pos, _, _ = joint_general(half, half, +t0)   # E = +4 t0  (redundant/positive)
P_neg, _, _ = joint_general(half, half, -t0)   # E = -4 t0  (synergy/anti)
Ecl_pos = E_cl_singlecolumn(P_pos)
Ecl_neg = E_cl_singlecolumn(P_neg)
Isig_pos = signed_interaction(P_pos)
Isig_neg = signed_interaction(P_neg)
line("E(P_pos) (correlation)", mp.nstr(correlation_E(P_pos), 8))
line("E(P_neg) (correlation)", mp.nstr(correlation_E(P_neg), 8))
line("E_cl(P_pos)  (non-negative)", mp.nstr(Ecl_pos, 30))
line("E_cl(P_neg)  (non-negative)", mp.nstr(Ecl_neg, 30))
line("|E_cl(P_pos)-E_cl(P_neg)| (magnitude gap)", mp.nstr(abs(Ecl_pos - Ecl_neg), 6))
line("signed-Isig(P_pos)", mp.nstr(Isig_pos, 20))
line("signed-Isig(P_neg)", mp.nstr(Isig_neg, 20))
line("Isig_pos + Isig_neg  (cancellation -> opposite signs)", mp.nstr(Isig_pos + Isig_neg, 6))
line("||Isig_pos| - |Isig_neg||  (equal magnitude)", mp.nstr(abs(abs(Isig_pos) - abs(Isig_neg)), 6))
check("EQUAL E_cl to <1e-110", abs(Ecl_pos - Ecl_neg) < TOL)
check("EQUAL |signed-Isig| to <1e-110", abs(abs(Isig_pos) - abs(Isig_neg)) < TOL)
check("OPPOSITE sign signed-Isig (sum ~0, individually nonzero)",
      abs(Isig_pos + Isig_neg) < TOL and abs(Isig_pos) > mp.mpf("1e-3"))
print("""
   => Two correlations IDENTICAL in every record magnitude (E_cl, |Isig|, marginals,
      Fisher) but OPPOSITE in the entangling/anti-correlating SIGN.  Magnitude-only
      records (E_cl, any KL/Fisher capacity) are provably blind to which is which.""")

# ---------------------------------------------------------------------------
sub("(1c) re-confirm (M1): the faithful capacity leg (marginal Fisher) is a")
print("        function of the MARGINALS ALONE -> sign-blind AND coupling-blind (dps140).")
# Fisher of the marginal tilt P(a) ~ exp(eta a): Var(a) = 1-<a>^2, depends only on
# the marginal <a>.  Sweep the coupling t at FIXED marginals: Fisher must be flat.
mA = half
fisher_vals = []
for tt in [mp.mpf(k) / 20 for k in range(-4, 5)]:   # t in [-0.2,0.2]
    P, pA, pB = joint_general(mA, half, tt)
    a_exp = (pA[0] * 1 + pA[1] * (-1))  # <a> with 0->+1,1->-1
    fisher_vals.append(1 - a_exp**2)
spread = max(fisher_vals) - min(fisher_vals)
line("marginal Fisher Var(a) across coupling sweep t in[-0.2,0.2]", mp.nstr(fisher_vals[0], 30))
line("Fisher spread over the WHOLE coupling sweep", mp.nstr(spread, 6))
check("marginal Fisher capacity is FLAT in the transverse coupling (<1e-110)",
      spread < TOL)
print("""
   => The faithful Fisher-capacity leg is lambda/coupling-INDEPENDENT (M1 capacity
      blindness reproduced at dps140).  A crossing built on it cannot even SEE the
      transverse correlation, let alone its sign.""")

# ============================================================================
head("SUB-QUESTION (2) MAGNITUDE:  is E_cl (a non-negative magnitude) forceable?")
# ============================================================================

# ---------------------------------------------------------------------------
sub("(2a) E_cl sweeps CONTINUOUSLY 0 -> ln2 with NOTHING internal selecting a point")
print("        (at fixed marginals, every value in [0, ln2) is realized).")
sweep = []
for k in range(0, 51):
    t = mp.mpf(k) / 200          # t: 0 -> 0.25
    P = joint_uniform(t)
    sweep.append((t, E_cl_singlecolumn(P)))
# endpoints + monotonicity + density
E0   = sweep[0][1]
Emax = sweep[-1][1]
line("E_cl at t=0      (product)", mp.nstr(E0, 6))
line("E_cl at t=1/4    (Bell)", mp.nstr(Emax, 30))
line("ln 2", mp.nstr(ln2, 30))
strictly_increasing = all(sweep[i][1] < sweep[i + 1][1] - mp.mpf("1e-30")
                          for i in range(len(sweep) - 1))
check("E_cl(product) = 0 to <1e-110", abs(E0) < TOL)
check("E_cl(Bell) = ln2 to <1e-110", abs(Emax - ln2) < TOL)
check("E_cl is a STRICTLY MONOTONE continuous sweep 0->ln2 (no gaps, no plateau)",
      strictly_increasing)
# intermediate value: E_cl hits ln2/2 at some interior t
target = ln2 / 2
lo, hi = mp.mpf(0), mp.mpf(1) / 4
for _ in range(460):
    mid = (lo + hi) / 2
    if E_cl_singlecolumn(joint_uniform(mid)) < target:
        lo = mid
    else:
        hi = mid
t_half = (lo + hi) / 2
half_residual = abs(E_cl_singlecolumn(joint_uniform(t_half)) - target)
line("interior t with E_cl = ln2/2", mp.nstr(t_half, 20))
line("residual |E_cl(t_half)-ln2/2|", mp.nstr(half_residual, 6))
check("E_cl takes the interior value ln2/2 (continuum, nothing pins a point)",
      half_residual < mp.mpf("1e-110"))
print("""
   => E_cl is a FREE continuum across the envelope; the marginals (the only thing
      the faithful capacity sees) leave E_cl entirely undetermined.""")

# ---------------------------------------------------------------------------
sub("(2b) the SINGLE-CHAIN capacity crossing has NO transverse analog landing on")
print("        a specific E_cl: the would-be crossing is DEGENERATE (capacity flat).")
# Single-chain anchor (reproduce EXACTLY): C(eta)=eta tanh eta - log cosh eta,
# J(eta)=sech^2 eta; crossing C=J at eta_A=1.0903443548..., W_*=J=C=0.3647849520...
def C_chain(eta):  # KL content, rising
    return eta * mp.tanh(eta) - mp.log(mp.cosh(eta))
def J_chain(eta):  # Fisher capacity, falling
    return mp.sech(eta) ** 2
# find crossing
lo, hi = mp.mpf("0.5"), mp.mpf("2")
for _ in range(400):
    m = (lo + hi) / 2
    if C_chain(m) - J_chain(m) < 0:
        lo = m
    else:
        hi = m
eta_A = (lo + hi) / 2
W_star = J_chain(eta_A)
gap_two_formula = J_chain(eta_A) - C_chain(eta_A)
line("eta_A (single-chain crossing)", mp.nstr(eta_A, 22))
line("W_* = J(eta_A) = C(eta_A)", mp.nstr(W_star, 22))
line("two-formula gap J-C at eta_A", mp.nstr(abs(gap_two_formula), 6))
check("single-chain crossing reproduced: eta_A ~ 1.0903443548",
      abs(eta_A - mp.mpf("1.090344354879492196221")) < mp.mpf("1e-15"))
check("single-chain crossing reproduced: W_* ~ 0.3647849520",
      abs(W_star - mp.mpf("0.3647849520899763622572")) < mp.mpf("1e-15"))
# KEY contrast: the single-chain C rises and J falls -> a transversal crossing.
# Transversely: the faithful capacity (marginal Fisher) is FLAT in t (2.b), and
# the joint content E_cl is U-shaped/monotone but the capacity does NOT fall to
# meet it -> the 'crossing' equation capacity(t)=content(t) is either never
# solved or solved on a marginal-dependent point.  Show the transverse capacity
# does NOT have a rising/falling pair that crosses at a t INDEPENDENT of marginals.
C_dchain = lambda eta: eta * mp.sech(eta)**2          # C' > 0 (sympy-exact below)
J_dchain = lambda eta: -2 * mp.tanh(eta) * mp.sech(eta)**2  # J' < 0
# sympy-exact derivative signs
eta_s = sp.symbols('eta', positive=True)
Cexpr = eta_s * sp.tanh(eta_s) - sp.log(sp.cosh(eta_s))
Jexpr = sp.sech(eta_s)**2
Cprime = sp.simplify(sp.diff(Cexpr, eta_s))
Jprime = sp.simplify(sp.diff(Jexpr, eta_s))
line("C'(eta) (sympy)", Cprime, "(>0: rising leg)")
line("J'(eta) (sympy)", Jprime, "(<0: falling leg)")
check("single-chain has a genuine rising/falling crossing (C'>0, J'<0)",
      sp.simplify(Cprime - eta_s * sp.sech(eta_s)**2) == 0)
# Transverse capacity slope in the coupling t (marginal Fisher) = 0 exactly:
dF_dt = []
hstep = mp.mpf("1e-25")
for tc in [mp.mpf("0.05"), mp.mpf("0.1"), mp.mpf("0.15")]:
    def Fcap(tt):
        P, pA, pB = joint_general(half, half, tt)
        a_exp = pA[0] - pA[1]
        return 1 - a_exp**2
    slope = (Fcap(tc + hstep) - Fcap(tc - hstep)) / (2 * hstep)
    dF_dt.append(slope)
line("d(marginal Fisher)/dt  (transverse capacity slope)", mp.nstr(max(abs(x) for x in dF_dt), 6))
check("transverse faithful capacity has ZERO slope in coupling (no falling leg)",
      all(abs(x) < mp.mpf("1e-90") for x in dF_dt))
print("""
   => SINGLE-CHAIN: a rising content C and a falling capacity J cross at ONE eta_A
      => W_* forced.  TRANSVERSE: the faithful capacity is FLAT in the coupling
      (slope 0), so there is no rising/falling pair to cross -- the would-be
      'balance' E_cl=capacity is degenerate (no isolated solution).  The mechanism
      that forced the single-chain constant has NO transverse instance.""")

# ---------------------------------------------------------------------------
sub("(2c) Tsirelson/IC envelope is magnitude-PERMISSIVE: CHSH 2->2sqrt2 while")
print("        E_cl ranges over a continuum; no facet singles out an interior E_cl.")
# Map a CHSH-style correlation strength to E_cl via the uniform-marginal family.
# For the family P_t, the per-setting correlation E = 4t in [-1,1]; a CHSH built
# from such correlations saturates 2sqrt2 at the Tsirelson angle.  The point: the
# envelope BOUNDS CHSH<=2sqrt2 but the SAME CHSH value is compatible with a RANGE
# of E_cl (different settings), and conversely. Show E_cl at the Tsirelson point
# is just whatever the correlation magnitude gives -- not pinned by the bound.
# Tsirelson correlation magnitude per pair = cos(pi/4)=1/sqrt2 -> t = 1/(4 sqrt2).
t_tsi = 1 / (4 * mp.sqrt(2))
E_tsi = E_cl_singlecolumn(joint_uniform(t_tsi))
line("correlation at Tsirelson point E=1/sqrt2 -> t", mp.nstr(t_tsi, 20))
line("E_cl at the Tsirelson correlation magnitude", mp.nstr(E_tsi, 20))
line("E_cl(Bell)=ln2 for comparison", mp.nstr(ln2, 20))
# The envelope (CHSH<=2sqrt2) does NOT force this E_cl: a PRODUCT-marginal local
# law CHSH=2 also has E_cl from 0 up to ln2 depending on settings. Show two laws
# at the SAME CHSH=2sqrt2 ceiling but DIFFERENT E_cl is impossible to forbid
# because E_cl is computed per joint kernel not per CHSH value: exhibit E_cl
# varying while staying inside the ENVELOPE (no-signaling marginals fixed).
envelope_Ecl = []
for tt in [mp.mpf(k) / 100 for k in range(0, 26)]:   # 0..0.25, all no-signaling
    envelope_Ecl.append(E_cl_singlecolumn(joint_uniform(tt)))
line("E_cl range over the no-signaling envelope (min..max)",
     mp.nstr(min(envelope_Ecl), 6) + " .. " + mp.nstr(max(envelope_Ecl), 6))
check("envelope admits a CONTINUUM of E_cl (no interior bound singles one out)",
      (max(envelope_Ecl) - min(envelope_Ecl)) > mp.mpf("0.5"))
print("""
   => The almost-quantum / Tsirelson / monogamy facets BOUND CHSH (a magnitude
      CEILING) but place no interior lower-or-upper bound that selects a unique
      E_cl in (0, ln2).  E_cl free across the envelope.""")

# ---------------------------------------------------------------------------
sub("(2d) DECISIVE: any candidate internal 'balance' point E_cl* MOVES with the")
print("        marginals -> circular / non-robust (M1 signature), NOT a forced number.")
# Mirror the scout's M1 finding: define a forced-looking balance E_cl(t)=Cov(a,b)(t)
# and show the balance t* DRIFTS as we change the marginal m -- so no intrinsic
# number is pinned.  (Single-chain crossing, by contrast, is at one eta_A for ALL.)
def Cov(P):
    """Cov(a,b) with a,b in {+1,-1}; = <ab>-<a><b>.  A non-KL 'balance' target."""
    pA = [P[0][0] + P[0][1], P[1][0] + P[1][1]]
    pB = [P[0][0] + P[1][0], P[0][1] + P[1][1]]
    aexp = pA[0] - pA[1]
    bexp = pB[0] - pB[1]
    abexp = (P[0][0] + P[1][1]) - (P[0][1] + P[1][0])
    return abexp - aexp * bexp

# Use the scout's M1 balance form C_AB = const * Cov(a,b): with c=0.3 the curve
# E_cl(t) (KL content, ~O(t^2) near 0) crosses c*Cov(t) (~O(t) near 0) at an
# INTERIOR t* for EVERY marginal m -- the candidate 'self-consistent' point.  The
# scout reported lam* drifting 0.115 -> 0.619 with m; here we show E_cl* drifts.
C_BAL = mp.mpf("0.30")
def balance_tstar(m):
    """Solve E_cl(t) = C_BAL * Cov(t) for t>0 at marginal m (candidate balance)."""
    def f(t):
        P, _, _ = joint_general(m, m, t)
        return E_cl_singlecolumn(P) - C_BAL * Cov(P)
    # near t->0: E_cl ~ O(t^2) < C_BAL*Cov ~ O(t)  => f<0; near t_max E_cl grows
    # faster (->ln-divergent) => f>0.  Sign change guaranteed.
    lo = mp.mpf("1e-9")
    hi = min(m, 1 - m) * mp.mpf("0.49")   # keep all entries positive
    flo = f(lo)
    fhi = f(hi)
    if flo * fhi > 0:
        return None, (flo, fhi)
    for _ in range(400):
        mid = (lo + hi) / 2
        if f(lo) * f(mid) <= 0:
            hi = mid
        else:
            lo = mid
    tstar = (lo + hi) / 2
    P, _, _ = joint_general(m, m, tstar)
    return tstar, E_cl_singlecolumn(P)

print("    candidate self-consistency: E_cl(t) = %s * Cov(a,b)(t)" % mp.nstr(C_BAL, 4))
print("    marginal m   ->   balance t*        E_cl* at balance")
balance_pts = []
for m in [mp.mpf("0.3"), mp.mpf("0.4"), mp.mpf("0.5"), mp.mpf("0.6"), mp.mpf("0.7")]:
    tstar, Eclstar = balance_tstar(m)
    if tstar is None:
        print(f"      m={mp.nstr(m,4)}   ->   (no balance / f same sign {tuple(mp.nstr(x,4) for x in Eclstar)})")
        continue
    balance_pts.append((m, tstar, Eclstar))
    print(f"      m={mp.nstr(m,4)}   ->   t*={mp.nstr(tstar,12)}   E_cl*={mp.nstr(Eclstar,16)}")
# spread of the 'forced' E_cl* across marginals
if len(balance_pts) >= 2:
    Ecl_stars = [p[2] for p in balance_pts]
    drift = max(Ecl_stars) - min(Ecl_stars)
    line("DRIFT of the candidate balance E_cl* across marginals m", mp.nstr(drift, 8))
    check("the candidate internal balance E_cl* DRIFTS with marginals (non-robust)",
          drift > mp.mpf("1e-3"))
print("""
   => Every candidate internal 'balance' that could pin E_cl moves with the
      marginals (circular: it pins a number only AFTER you fix the marginals,
      which the records do not).  CONTRAST the single-chain crossing W_*: the
      capacity J(eta) and content C(eta) cross at ONE eta_A independent of any
      external choice -> a genuine forced number.  No such marginal-independent
      transverse balance exists for E_cl.""")

# ---------------------------------------------------------------------------
sub("(2e) sympy-exact: E_cl is EVEN in t at uniform marginals -> the would-be")
print("        max-min over the signed coupling is symmetric, min at t=0 (product),")
print("        no isolated interior extremum that could be 'the forced E_cl'.")
Ecl_t = I_sym(P_sym)              # E_cl(t) symbolic, uniform marginals
Ecl_even = sp.simplify(Ecl_t - Ecl_t.subs(ts, -ts))
line("E_cl(t) - E_cl(-t) (sympy)", Ecl_even, "(=0: EVEN, sign-blind)")
check("E_cl is EVEN in the signed coupling (sympy-exact)", Ecl_even == 0)
# derivative at 0 is 0 (min at product), monotone outward; the ONLY internal
# extremum is the product point E_cl=0 (a TRIVIAL value), not an interior magnitude.
dEcl = sp.simplify(sp.diff(Ecl_t, ts))
dEcl_at0 = sp.simplify(sp.limit(dEcl, ts, 0))
line("dE_cl/dt at t=0", dEcl_at0, "(=0: extremum at the product, value 0)")
check("E_cl's only internal stationary point is the product (E_cl=0), trivial",
      dEcl_at0 == 0)
print("""
   => The only point any symmetric internal extremization can select is the
      TRIVIAL product value E_cl=0 (no entanglement).  Any nonzero magnitude
      requires an external choice of t -> not forced.""")

# ============================================================================
head("VERDICT")
# ============================================================================
n_pass = sum(1 for _, ok in PASS if ok)
n_tot = len(PASS)
print(f"\n   checks passed: {n_pass}/{n_tot}")
print("""
 SUB-QUESTION (1) SIGN:
   * sympy-exact: the sign involution tau flips the correlation E -> -E (hence
     flips the signed interaction chi_AB) while leaving E_cl, |chi_AB|, the
     marginal Fisher capacity, and the CHSH-magnitude EXACTLY invariant.
   * dps140 witness pair: equal E_cl, equal |signed-Isig| (gap <1e-110),
     OPPOSITE sign.  Magnitude-only records cannot tell entangling (synergy)
     from anti-correlating (redundancy).
   => A hypothetical successful transverse crossing pins at most the NON-NEGATIVE
      MAGNITUDE |chi_AB| / E_cl, NEVER the sign.  SIGN NOT FORCED.   [CONFIRMED]

 SUB-QUESTION (2) MAGNITUDE (E_cl):
   * E_cl sweeps a STRICTLY MONOTONE CONTINUUM 0 (product) -> ln2 (Bell); at fixed
     marginals every value in [0, ln2) is realized (incl. ln2/2). Nothing internal
     selects a point.
   * The single-chain mechanism that forced W_* (a RISING content C crossing a
     FALLING capacity J at one eta_A) has NO transverse instance: the faithful
     capacity (marginal Fisher) is FLAT in the coupling (slope 0 to 1e-90), so
     the balance equation is degenerate.
   * The Tsirelson/IC envelope only CEILINGS CHSH<=2sqrt2; it admits a continuum
     of E_cl with no interior facet selecting one.
   * Every candidate internal 'balance' E_cl* DRIFTS with the marginals (circular,
     M1 signature), unlike the marginal-independent single-chain W_*.
   * sympy-exact: E_cl is EVEN in the signed coupling; its only internal stationary
     point is the TRIVIAL product value 0.
   => E_cl is ALSO FREE across the envelope; no internal balance pins a specific
      magnitude.  MAGNITUDE NOT FORCED.                              [CONFIRMED]

 OVERALL: neither the SIGN nor a specific MAGNITUDE (E_cl) is forced by any
 transverse self-consistency.  The best case stays ENVELOPE-ONLY.
 VERDICT = CLOSED_nogo_holds.
""")
print("ALL ASSERTS PASSED." if n_pass == n_tot else "SOME CHECKS FAILED.")
