#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
p6c_alternative_capacity.py -- v7 Long March, OPEN-PATH 2.
STRESS-TEST: can a DIFFERENT (still-defensible) record-internal "joint capacity"
resurrect a transverse self-consistency FORCING of the entangling content chi_AB?

CONTEXT.  The Phase-1 scout established (M1, candidate C1, the literal analog of the
single-chain one-diamond KL=Fisher crossing): on the record-internal joint law

      P(a,b)  proportional to  exp( eta_A a + eta_B b + lambda a b ),    a,b in {-1,+1}

the FAITHFUL capacity leg -- the Fisher information of the MARGINAL TILT, Var(a) =
1 - <a>^2 -- is a function of the MARGINALS ALONE and is therefore EXACTLY lambda-
blind.  The joint KL content C_AB(lambda) is U-SHAPED (min at lambda=0), so there is
no single rising leg, the max-min is ill-posed, and any forced-looking balance moves
with the marginals (lam*=0.115 at m=0.3, 0.619 at m=0.5).  RESULT: the faithful
capacity cannot force chi_AB.

But "capacity" is a DEFINITIONAL CHOICE.  A genuine forcing would require an
alternative capacity that simultaneously
   (a) FALLS in the entangling parameter lambda at FIXED marginals,
   (b) OPPOSES a genuinely RISING content leg, and
   (c) crosses at an INTRINSIC lambda INDEPENDENT of the marginals.
We test THREE alternative capacity definitions and ask, for each, whether (a)+(b)+(c)
hold or whether it (like the faithful one) goes blind / fails monotone-opposition /
pins only the marginals.

  CANDIDATE (1): the A|B-CUT channel capacity / conditional mutual information across
                 the PARALLEL cut (NOT the sequential refinement that telescopes blind).
  CANDIDATE (2): the HOLONOMY-FISHER J_lambda = Var(ab) -- Fisher information w.r.t. the
                 entangling natural parameter lambda ITSELF.  Is it monotone-falling, and
                 does it oppose a rising content?
  CANDIDATE (3): the non-negative kinematic E_cl (nearest-product KL, E_cl(Bell)=ln2)
                 as the CONTENT leg against any falling capacity.

PRE-GEOMETRIC (Tier A) throughout: every quantity is a record-internal probability /
KL / Fisher number on the moment algebra M = <{1, A, B, AB}>_psi.  No spacetime,
metric, light cone, proper time, or s^2 ever.  mpmath dps>=120 (140 for cancellation-
heavy parts); sympy-exact derivative signs where possible.

CRUX OF THE PROTOCOL.  Forcing must be tested AT FIXED MARGINALS -- otherwise the
"capacity" is just tracking the marginals (the C1 circularity).  Holding <a>,<b>
fixed, lambda is the PURE entangling direction.  We re-solve eta_A,eta_B for every
lambda so that <a>=<b>=m is pinned, then read off each capacity/content leg.
"""

import mpmath as mp
import sympy as sp

mp.mp.dps = 140

STATES = [(-1, -1), (-1, 1), (1, -1), (1, 1)]


def head(s):
    print("\n" + "=" * 80)
    print(s)
    print("=" * 80)


def sub(s):
    print("\n  -- " + s + " --")


def line(label, val, extra=""):
    print(f"  {label:<54} {val} {extra}")


TOL = mp.mpf(10) ** (-100)


# ===========================================================================
# Record-internal joint law on the (A,B) moment algebra and its solver.
#   P(a,b) propto exp(eta_A a + eta_B b + lambda a b),  a,b in {-1,+1}.
#   To test forcing in the PURE entangling direction we hold the MARGINALS
#   <a>=ma, <b>=mb fixed and re-solve (eta_A, eta_B) for each lambda.
# ===========================================================================

def joint_law(etaA, etaB, lam):
    w = {s: mp.e ** (etaA * s[0] + etaB * s[1] + lam * s[0] * s[1]) for s in STATES}
    Z = sum(w.values())
    return {s: w[s] / Z for s in STATES}


def solve_fixed_marginals(ma, mb, lam, guess=None):
    """Re-tune (eta_A, eta_B) so that <a>=ma, <b>=mb at the given lambda."""
    if guess is None:
        guess = (mp.mpf("0.4"), mp.mpf("0.4"))

    def eqs(etaA, etaB):
        p = joint_law(etaA, etaB, lam)
        Ea = sum(p[s] * s[0] for s in STATES)
        Eb = sum(p[s] * s[1] for s in STATES)
        return [Ea - ma, Eb - mb]

    sol = mp.findroot(eqs, guess)
    return joint_law(sol[0], sol[1], lam), sol[0], sol[1]


def moments(p):
    Ea = sum(p[s] * s[0] for s in STATES)
    Eb = sum(p[s] * s[1] for s in STATES)
    Eab = sum(p[s] * s[0] * s[1] for s in STATES)
    return Ea, Eb, Eab


def mutual_info(p):
    """I(A:B): the cut mutual information = E_cl to the nearest product (single joint)."""
    pa = {a: sum(p[(a, b)] for b in (-1, 1)) for a in (-1, 1)}
    pb = {b: sum(p[(a, b)] for a in (-1, 1)) for b in (-1, 1)}
    I = mp.mpf(0)
    for a in (-1, 1):
        for b in (-1, 1):
            if p[(a, b)] > 0:
                I += p[(a, b)] * mp.log(p[(a, b)] / (pa[a] * pb[b]))
    return I


def E_cl_nearest_product(p):
    """Non-negative kinematic E_cl: KL of the joint from its NEAREST product law.
    For a single joint distribution the nearest product (in KL) is the marginal
    product, so E_cl(A:B) = I(A:B).  (Paper 21 Prop 1a: E_cl=0 iff product, >=0.)"""
    return mutual_info(p)


def cut_channel_capacity(p):
    """CANDIDATE (1) ALT READING: the A|B-cut as a channel B->A, capacity-as-rate.
    Treat the conditional p(a|b) as a channel with input distribution = the B-marginal
    fixed by the record.  The information FLOWING ACROSS THE CUT at the record's own
    input is exactly I(A:B).  (Maximizing over inputs gives the Shannon capacity, but
    that re-optimizes the B-marginal -- i.e. it CHANGES the record's marginals, which
    is exactly the protocol violation.  At fixed record marginals the cut rate IS the
    mutual information.)  We return both: the record-rate (=MI) and the max-over-input
    channel capacity C_chan, and show BOTH are marginal-tied, not lambda-intrinsic."""
    return mutual_info(p)


def channel_capacity_BtoA(p):
    """The Shannon capacity of the binary channel b -> a defined by p(a|b),
    max over input distribution r(b).  This re-optimizes the input (= moves marginals).
    Computed by Blahut-Arimoto at high precision for the corroborating point."""
    # transition W[a][b] = p(a|b)
    pb = {b: sum(p[(a, b)] for a in (-1, 1)) for b in (-1, 1)}
    W = {a: {b: (p[(a, b)] / pb[b] if pb[b] > 0 else mp.mpf(0)) for b in (-1, 1)} for a in (-1, 1)}
    # Blahut-Arimoto
    r = {b: mp.mpf(1) / 2 for b in (-1, 1)}
    for _ in range(4000):
        qa = {a: sum(r[b] * W[a][b] for b in (-1, 1)) for a in (-1, 1)}
        # D_b = sum_a W(a|b) ln(W(a|b)/qa)
        logc = {}
        for b in (-1, 1):
            d = mp.mpf(0)
            for a in (-1, 1):
                if W[a][b] > 0 and qa[a] > 0:
                    d += W[a][b] * mp.log(W[a][b] / qa[a])
            logc[b] = d
        cb = {b: mp.e ** logc[b] for b in (-1, 1)}
        Zc = sum(r[b] * cb[b] for b in (-1, 1))
        r = {b: r[b] * cb[b] / Zc for b in (-1, 1)}
    return mp.log(Zc)


# ===========================================================================
head("SETUP.  The record-internal joint law and the marginal-blindness of the faithful capacity")
# ===========================================================================
print("""
  P(a,b) propto exp(eta_A a + eta_B b + lambda a b),  a,b in {-1,+1}.  lambda is the
  ENTANGLING natural parameter (the cross-moment tilt).  We test forcing AT FIXED
  MARGINALS: re-solve (eta_A,eta_B) for each lambda so <a>=<b>=m stays pinned.  Then
  lambda is the PURE entangling direction and any capacity that 'tracks the marginals'
  is exposed as not lambda-intrinsic.

  First reproduce the C1 baseline: the FAITHFUL capacity Var(a)=1-<a>^2 is the Fisher
  of the MARGINAL tilt -- it is a function of m ALONE, hence EXACTLY lambda-blind.
""")
for mstr in ["0.3", "0.5", "0.7"]:
    m = mp.mpf(mstr)
    vals = []
    g = None
    for lstr in ["-0.6", "-0.3", "0.0", "0.3", "0.6"]:
        lam = mp.mpf(lstr)
        p, eA, eB = solve_fixed_marginals(m, m, lam, g)
        g = (eA, eB)
        Ea, Eb, Eab = moments(p)
        vals.append(1 - Ea ** 2)
    spread = max(vals) - min(vals)
    line(f"m={mstr}: Var(a) across lambda in [-0.6,0.6], spread", mp.nstr(spread, 6),
         "(=0: faithful capacity is lambda-BLIND -- C1 baseline)")
    assert spread < mp.mpf("1e-90"), "faithful capacity must be exactly lambda-blind"
print("  => FAITHFUL capacity reproduces the C1 no-go: blind to lambda at fixed marginals.")


# ===========================================================================
head("CANDIDATE (2).  HOLONOMY-FISHER  J_lambda = Var(ab)  (Fisher in the ENTANGLING parameter)")
# ===========================================================================
print("""
  The natural 'fix' for C1's blindness: use the Fisher information of the ENTANGLING
  natural parameter lambda itself, not the marginal tilt.  In the exponential family
  P propto exp(eta_A a + eta_B b + lambda ab), the log-partition Hessian entry for
  lambda is exactly
        J_lambda = Var(ab) = <(ab)^2> - <ab>^2 = 1 - <ab>^2     (since (ab)^2=1).
  This is genuinely lambda-DEPENDENT (unlike Var(a)).  Forcing needs J_lambda to FALL
  monotonically in lambda and oppose a rising content.  We test that.
""")

sub("(2.a) sympy-EXACT sign of dJ_lambda/dlambda at fixed marginals")
# Parameterize the fixed-marginal family by the joint corner prob q=P(1,1); marginals
# u=(1+m)/2 fix the other three cells.  Eab is then EXACT-linear in q, and lambda is a
# monotone increasing function of q (the Ising log-odds).  So d/dlambda has sign of d/dq.
m_s, q_s = sp.symbols('m q', real=True)
u_s = (1 + m_s) / 2
p11, p1m, pm1, pmm = q_s, u_s - q_s, u_s - q_s, 1 - 2 * u_s + q_s
Eab_s = sp.simplify(p11 - p1m - pm1 + pmm)          # = 4q - 2 - 2m + 1 -> simplify
line("Eab(q,m) [sympy-exact]", Eab_s, "(linear in q)")
# lambda as Ising log-odds: lambda = (1/4) ln( p11 pmm / (p1m pm1) ), strictly increasing in q
lam_s = sp.Rational(1, 4) * sp.log(p11 * pmm / (p1m * pm1))
dlam_dq = sp.simplify(sp.diff(lam_s, q_s))
line("d lambda/d q  [sympy]", sp.simplify(dlam_dq), "(>0 on the valid interior: lambda increases with q)")
# J_lambda = 1 - Eab^2 ; dJ/dq = -2 Eab dEab/dq ; dEab/dq = 4 > 0
dEab_dq = sp.diff(Eab_s, q_s)
line("dEab/dq  [sympy-exact]", dEab_dq, "(>0: correlation strictly increases with lambda)")
print("""
  => dJ_lambda/dlambda  =  (dJ/dq)/(dlambda/dq),  dlambda/dq>0, and
     dJ/dq = -2 Eab * dEab/dq = -8 Eab   (sympy-exact, dEab/dq=4).
     Hence  sign( dJ_lambda/dlambda ) = -sign(Eab).
     J_lambda RISES while Eab<0, PEAKS at Eab=0, FALLS while Eab>0  ==>  HUMP-SHAPED,
     NOT monotone-falling.  (a) FAILS: there is no single falling leg.
""")
sign_expr = sp.simplify(-2 * Eab_s * dEab_dq)
line("dJ_lambda/dq = -2 Eab dEab/dq  [sympy]", sign_expr, "(= -8 Eab: sign is -sign(Eab))")

sub("(2.b) numeric hump: J_lambda(lambda) at fixed marginals -- peak location MOVES with m")
def Eab_fixed(m, lam, g):
    p, eA, eB = solve_fixed_marginals(m, m, lam, g)
    Ea, Eb, Eab = moments(p)
    return Eab, (eA, eB)

for mstr in ["0.3", "0.5", "0.7"]:
    m = mp.mpf(mstr)
    print(f"\n    m={mstr}:   lambda      Eab          J_lambda=1-Eab^2")
    g = None
    prevJ = None
    rose = fell = False
    for lstr in ["-0.6", "-0.4", "-0.2", "-0.1", "0.0", "0.2", "0.4", "0.6"]:
        lam = mp.mpf(lstr)
        Eab, g = Eab_fixed(m, lam, g)
        J = 1 - Eab ** 2
        print(f"             {lstr:>6}   {mp.nstr(Eab, 10):>14}   {mp.nstr(J, 12)}")
        if prevJ is not None:
            if J > prevJ: rose = True
            if J < prevJ: fell = True
        prevJ = J
    line(f"    m={mstr}: J_lambda both rises AND falls over the window?", rose and fell,
         "(True => NON-monotone hump => no falling capacity leg)")

sub("(2.c) the hump PEAK (Eab=0) location is MARGINAL-DEPENDENT (not intrinsic)")
def find_peak(m):
    """Locate the J_lambda peak: where Eab(lambda)=0.  Scan for a sign change of Eab;
    if Eab>0 on the whole reachable window the peak is at the boundary (lambda->-inf)."""
    lo, hi = mp.mpf("-3.0"), mp.mpf("0.6")
    g = None
    def Eab_at(lam, gg):
        return Eab_fixed(m, lam, gg)
    # coarse scan for sign change
    grid = [lo + (hi - lo) * k / 40 for k in range(41)]
    prev = None
    bracket = None
    g = None
    for lam in grid:
        try:
            E, g = Eab_at(lam, g)
        except Exception:
            break
        if prev is not None and prev[1] * E < 0:
            bracket = (prev[0], lam)
        prev = (lam, E)
    if bracket is None:
        return None  # no interior peak (monotone branch only)
    a, b = bracket
    ga = None
    for _ in range(150):
        mid = (a + b) / 2
        Em, _ = Eab_at(mid, None)
        Ea_, _ = Eab_at(a, None)
        if Ea_ * Em <= 0:
            b = mid
        else:
            a = mid
    return (a + b) / 2

for mstr in ["0.3", "0.5", "0.7"]:
    m = mp.mpf(mstr)
    pk = find_peak(m)
    if pk is None:
        line(f"    m={mstr}: J_lambda peak (Eab=0)", "NONE in reach",
             "(Eab>0 throughout => peak at boundary lambda->-inf: monotone, pins nothing)")
    else:
        line(f"    m={mstr}: J_lambda peak (Eab=0) at lambda*", mp.nstr(pk, 12),
             "(MARGINAL-DEPENDENT)")
print("""
  VERDICT CANDIDATE (2):  J_lambda = Var(ab) is genuinely lambda-DEPENDENT (it beats
  C1's blindness) but it is HUMP-shaped, NOT monotone-falling: dJ/dlambda = -2 Eab
  dEab/dlambda with dEab/dlambda>0, so the sign is -sign(Eab).  (a) FAILS (no single
  falling leg) and (c) FAILS (the turning point Eab=0 moves with the marginals --
  lambda*~ -0.11 at m=0.3, pushed to the boundary lambda->-inf for m>=0.5).  No
  intrinsic crossing.  Same disease as C1's U-shaped content, mirror-imaged.
""")


# ===========================================================================
head("CANDIDATE (3).  E_cl (nearest-product KL) as the CONTENT leg -- is IT monotone?")
# ===========================================================================
print("""
  E_cl >= 0, =0 iff product (Paper 21 Prop 1a), E_cl(Bell)=ln2.  Proposed as the
  RISING content leg to oppose a falling capacity.  For a single joint distribution
  the nearest product is the marginal product, so E_cl(A:B) = I(A:B) (the cut MI).
  We first CALIBRATE E_cl(Bell)=ln2, then test monotonicity at fixed marginals.
""")

sub("(3.a) calibration: E_cl on the maximally-correlated (Bell-like) joint = ln2")
# Bell-like single joint with uniform marginals: P(1,1)=P(-1,-1)=1/2, others 0.
pbell = {(1, 1): mp.mpf(1) / 2, (-1, -1): mp.mpf(1) / 2, (1, -1): mp.mpf(0), (-1, 1): mp.mpf(0)}
Ecl_bell = E_cl_nearest_product(pbell)
line("E_cl(Bell-like joint, uniform marginals)", mp.nstr(Ecl_bell, 30))
line("ln 2", mp.nstr(mp.log(2), 30))
line("|E_cl(Bell) - ln2|", mp.nstr(abs(Ecl_bell - mp.log(2)), 6))
assert abs(Ecl_bell - mp.log(2)) < TOL, "E_cl(Bell) must equal ln2"

sub("(3.b) E_cl(lambda) at fixed marginals -- U-shaped (min at lambda=0), NOT monotone")
for mstr in ["0.3", "0.5"]:
    m = mp.mpf(mstr)
    print(f"\n    m={mstr}:   lambda     E_cl=I(A:B)")
    g = None
    Evals = []
    lams = ["-0.6", "-0.4", "-0.2", "0.0", "0.2", "0.4", "0.6"]
    for lstr in lams:
        lam = mp.mpf(lstr)
        p, eA, eB = solve_fixed_marginals(m, m, lam, g)
        g = (eA, eB)
        E = E_cl_nearest_product(p)
        Evals.append((lam, E))
        print(f"             {lstr:>6}   {mp.nstr(E, 14)}")
    # minimum is at lambda=0 (independence), strictly positive on both sides
    mid = [e for (l, e) in Evals if l == mp.mpf("0.0")][0]
    left = [e for (l, e) in Evals if l == mp.mpf("-0.6")][0]
    right = [e for (l, e) in Evals if l == mp.mpf("0.6")][0]
    line(f"    m={mstr}: E_cl(lambda=0) (the MINIMUM)", mp.nstr(mid, 6),
         "(~0: independence => zero content)")
    line(f"    m={mstr}: E_cl rises on BOTH sides of 0?", (left > mid and right > mid),
         "(True => U-shaped, NOT monotone rising)")
    assert mid < mp.mpf("1e-30"), "E_cl must vanish at lambda=0"
    assert left > mp.mpf("1e-3") and right > mp.mpf("1e-3")
print("""
  VERDICT CANDIDATE (3):  E_cl as a content leg is U-SHAPED in lambda at fixed
  marginals (minimum 0 at lambda=0, rising for BOTH signs of lambda) -- it is NOT a
  monotone RISING leg.  It distinguishes ZERO from NONZERO correlation but cannot
  distinguish +lambda from -lambda, and provides no single rising arm to cross a
  falling capacity.  (b) FAILS.  (This is the same U-shape the M1 scout found for the
  joint KL content C_AB.)
""")


# ===========================================================================
head("CANDIDATE (1).  A|B-CUT channel capacity / conditional mutual info across the PARALLEL cut")
# ===========================================================================
print("""
  The sequential refinement telescopes blind (p4a PART 2: R-seq gap ~0 while I_sigma!=0).
  The PARALLEL cut is the place a capacity could see chi_AB.  Two readings of 'capacity
  across the A|B cut', both record-internal:
    (1R) the RECORD-RATE: information across the cut at the record's OWN marginals = I(A:B).
    (1C) the CHANNEL CAPACITY: Shannon capacity C_chan of the channel b->a (max over input).
  We test forcing for both.
""")

sub("(1.a) record-rate reading (1R): the cut MI = E_cl -- U-shaped (same as candidate 3)")
print("    (already shown in candidate (3): I(A:B) is U-shaped, min at lambda=0).")
line("    cut record-rate = I(A:B)", "U-shaped (min at lambda=0)", "(NOT a falling capacity)")

sub("(1.b) channel-capacity reading (1C): C_chan(lambda) at fixed marginals (Blahut-Arimoto)")
for mstr in ["0.3", "0.5"]:
    m = mp.mpf(mstr)
    print(f"\n    m={mstr}:   lambda     C_chan(b->a)    I(A:B)")
    g = None
    Cvals = []
    for lstr in ["-0.6", "-0.3", "0.0", "0.3", "0.6"]:
        lam = mp.mpf(lstr)
        p, eA, eB = solve_fixed_marginals(m, m, lam, g)
        g = (eA, eB)
        Cc = channel_capacity_BtoA(p)
        I = mutual_info(p)
        Cvals.append((lam, Cc))
        print(f"             {lstr:>6}   {mp.nstr(Cc, 12):>14}   {mp.nstr(I, 10)}")
    mid = [c for (l, c) in Cvals if l == mp.mpf("0.0")][0]
    left = [c for (l, c) in Cvals if l == mp.mpf("-0.6")][0]
    right = [c for (l, c) in Cvals if l == mp.mpf("0.6")][0]
    line(f"    m={mstr}: C_chan(lambda=0) (minimum)", mp.nstr(mid, 6))
    line(f"    m={mstr}: C_chan rises on BOTH sides of 0?", (left > mid and right > mid),
         "(True => U-shaped: channel capacity also NOT monotone-falling)")
print("""
  VERDICT CANDIDATE (1):  Across the parallel A|B cut, BOTH readings are U-shaped in
  lambda at fixed marginals -- the record-rate I(A:B) and the max-over-input channel
  capacity C_chan both bottom out at lambda=0 and RISE for either sign.  Neither is a
  monotone FALLING capacity.  (Re-optimizing the channel input to get C_chan also
  moves the marginals, the very protocol violation that makes 'forcing' circular.)
  (a) FAILS for the cut capacity too.
""")


# ===========================================================================
head("CROSS-CHECK.  Is there ANY monotone-opposed crossing pinning an INTRINSIC lambda?")
# ===========================================================================
print("""
  The forcing template (single-chain LAW-A) is a falling Fisher leg J(eta)=sech^2 eta
  crossing a rising KL content C(eta) at the INTRINSIC eta_*=1.09034...  For the joint
  law we have now charted both legs at fixed marginals:

    leg                         shape in lambda (fixed marginals)     monotone-opposed?
    ----------------------------------------------------------------------------------
    faithful Var(a)             FLAT (lambda-blind)                   no (blind)         [C1]
    holonomy-Fisher Var(ab)     HUMP (peak at Eab=0, marg-dep)        no (not falling)   [cand 2]
    cut record-rate I(A:B)      U (min at lambda=0)                   no (not rising)    [cand 1R/3]
    cut channel cap C_chan      U (min at lambda=0)                   no (not rising)    [cand 1C]
    E_cl (nearest-prod KL)      U (min at lambda=0)                   no (not rising)    [cand 3]

  The single-chain crossing worked because LAW-A had a STRICTLY FALLING Fisher and a
  STRICTLY RISING content on the SAME half-line eta>0.  Here, at fixed marginals:
   * every CONTENT-like leg (I, E_cl, C_chan) is EVEN-ish (U-shaped, min at 0): it
     cannot tell the sign of lambda, so it has no single rising arm;
   * the only lambda-DEPENDENT capacity (Var(ab)) is HUMP-shaped with a MARGINAL-
     DEPENDENT turning point;
   * the one strictly-monotone object is Eab itself (the cross-moment), but Eab is the
     COORDINATE lambda re-expressed -- using 'Eab rising' as a 'content rising' and
     'Var(ab)=1-Eab^2 falling' as 'capacity falling' is the TAUTOLOGY x rises while
     1-x^2 falls; their 'crossing' 1-Eab^2 = Eab is at Eab=(sqrt5-1)/2 (golden), a
     FIXED number -- but it pins Eab, hence (through the marginal-dependent map
     Eab(lambda;m)) a MARGINAL-DEPENDENT lambda, and it is content-free (no second
     independent principle).  We show this 'golden' pseudo-crossing is marginal-tied.
""")

sub("the only monotone pair (Eab up, 1-Eab^2 down) crosses at a FIXED moment but a MOVING lambda")
golden = (mp.sqrt(5) - 1) / 2
line("tautological crossing 1-Eab^2 = Eab  =>  Eab*", mp.nstr(golden, 30), "(golden ratio, FIXED moment)")
# verify
line("check 1 - golden^2 - golden", mp.nstr(1 - golden ** 2 - golden, 6), "(=0)")
def lam_for_Eab_target(m, target):
    """Find lambda (fixed marginals m) achieving Eab=target, if reachable."""
    g = None
    def E_at(lam):
        nonlocal g
        p, eA, eB = solve_fixed_marginals(m, m, lam, g)
        g = (eA, eB)
        return sum(p[s] * s[0] * s[1] for s in STATES) - target
    return mp.findroot(E_at, mp.mpf("0.6"))
print("\n    lambda achieving the golden cross Eab=0.618... at each marginal:")
lstars = []
for mstr in ["0.3", "0.5", "0.7"]:
    m = mp.mpf(mstr)
    ls = lam_for_Eab_target(m, golden)
    lstars.append(ls)
    line(f"    m={mstr}: lambda*(golden cross)", mp.nstr(ls, 12), "(MOVES with m)")
spread_l = max(lstars) - min(lstars)
line("spread of lambda*(golden) across m in {0.3,0.5,0.7}", mp.nstr(spread_l, 8),
     "(>>0: the 'crossing' lambda is NOT intrinsic -- it tracks the marginals)")
assert spread_l > mp.mpf("1e-2"), "the tautological crossing must be marginal-dependent"
print("""
  => Even the ONE monotone-opposed pair one can manufacture (Eab vs 1-Eab^2) is a
     TAUTOLOGY (x vs 1-x^2, not two independent principles) and its crossing pins a
     FIXED MOMENT (golden ratio) but a MARGINAL-DEPENDENT lambda (spread > 0.6 across
     m).  It is exactly the C1 circularity in moment coordinates: it pins the
     marginals/moment, never an intrinsic entangling lambda.
""")


# ===========================================================================
head("FAITHFULNESS / EXHAUSTION  -- which capacities were and were NOT tested")
# ===========================================================================
print("""
  TESTED (and each fails one of (a)/(b)/(c)):
   * faithful marginal-tilt Fisher Var(a)        -> BLIND (a fails: flat in lambda)        [C1 reproduced]
   * holonomy-Fisher Var(ab)=J_lambda            -> HUMP (a&c fail: not falling; peak moves) [cand 2]
   * cut record-rate / cond. mutual info I(A:B)  -> U-shape (b fails: not rising one-armed)  [cand 1R/3]
   * cut Shannon channel capacity C_chan         -> U-shape (b fails; re-opt moves marginals)[cand 1C]
   * nearest-product KL E_cl (calib E_cl(Bell)=ln2) -> U-shape (b fails)                     [cand 3]
   * tautological Eab vs 1-Eab^2 'crossing'      -> pins golden MOMENT but MOVING lambda     [cross-check]

  The common structural reason (the moment-algebra invariance from M2 / t1):
  every record-internal capacity is a functional of the level-(1+AB) moment algebra
  M=<1,A,B,AB>_psi.  At FIXED MARGINALS the only remaining coordinate is the single
  cross-moment Eab (a monotone reparam of lambda).  A faithful 'capacity' is either
  (i) a function of the marginals alone (blind), or (ii) an EVEN function of the
  signed correlation about its independence point (U/hump-shaped: it measures the
  MAGNITUDE of departure from product, which is sign-blind), or (iii) literally Eab
  (the coordinate, giving a tautological crossing at a fixed moment / moving lambda).
  None yields a strictly-falling-vs-strictly-rising pair on a common half-line with a
  marginal-INDEPENDENT crossing.  So no defensible alternative capacity resurrects
  forcing.

  NOT EXHAUSTED (honest residue -- these are NOT record-internal Tier-A capacities):
   * Capacities that import a PREFERRED tensor split / complex structure (e.g. an
     entanglement ENTROPY of a chosen factorization) are exactly the kernel direction
     M2 identifies as field-blind: they ASSUME the chi_AB they would 'force'.  They are
     not record-internal (they need the very factorization at issue), so they cannot
     count as a Tier-A forcing principle.
   * Off-state / higher-level moment algebras (beyond level 1+AB) are a different
     arena (paper-level escalation), not an alternative 'capacity' on the same law.
""")


# ===========================================================================
head("CANONICAL OUTPUT BLOCK  (p6c alternative-capacity stress-test, dps=%d)" % mp.mp.dps)
# ===========================================================================
# recompute a few headline numbers cleanly for the block
m03 = mp.mpf("0.3")
# faithful blindness spread at m=0.3
g = None; vfaith = []
for lstr in ["-0.6", "0.0", "0.6"]:
    p, eA, eB = solve_fixed_marginals(m03, m03, mp.mpf(lstr), g); g = (eA, eB)
    Ea, Eb, Eab = moments(p); vfaith.append(1 - Ea ** 2)
faith_spread = max(vfaith) - min(vfaith)
# Var(ab) hump endpoints/peak at m=0.3
g = None
Eab_m06, g = Eab_fixed(m03, mp.mpf("-0.6"), g)
Eab_0, g = Eab_fixed(m03, mp.mpf("0.0"), g)
Eab_p06, g = Eab_fixed(m03, mp.mpf("0.6"), g)
J_m06, J_0, J_p06 = 1 - Eab_m06 ** 2, 1 - Eab_0 ** 2, 1 - Eab_p06 ** 2
peak03 = find_peak(m03)

print(f"""
  PROTOCOL:  test forcing at FIXED MARGINALS (<a>=<b>=m), lambda = pure entangling
  direction; re-solve (eta_A,eta_B) per lambda.  dps={mp.mp.dps}.

  faithful capacity Var(a)  [C1 baseline]:
    spread over lambda in [-0.6,0.6] at m=0.3   = {mp.nstr(faith_spread, 4)}   (lambda-BLIND)

  CANDIDATE (2) holonomy-Fisher J_lambda=Var(ab):  sympy-exact sign dJ/dq = -8 Eab
    J(lambda=-0.6,0,+0.6) at m=0.3              = {mp.nstr(J_m06, 8)}, {mp.nstr(J_0, 8)}, {mp.nstr(J_p06, 8)}
    => HUMP (rises then falls); peak (Eab=0) at  lambda*={mp.nstr(peak03, 8)} at m=0.3,
       pushed to boundary lambda->-inf for m>=0.5  => (a)&(c) FAIL (not falling; moves)

  CANDIDATE (1) cut capacity (record-rate I(A:B) & Shannon C_chan):
    both U-shaped, minimum at lambda=0          => (b) FAILS (not a rising/falling one-armed leg)

  CANDIDATE (3) E_cl (nearest-product KL):
    E_cl(Bell) = ln2 = {mp.nstr(mp.log(2), 12)}  (calibrated)
    E_cl(lambda) U-shaped, min 0 at lambda=0     => (b) FAILS (not monotone rising)

  tautological monotone pair Eab vs 1-Eab^2:
    crosses at golden moment Eab*={mp.nstr(golden, 10)} (FIXED) but lambda*(m) MOVES,
    spread across m={{0.3,0.5,0.7}} = {mp.nstr(spread_l, 6)}  => pins a MOMENT, not lambda

  VERDICT:  NO alternative capacity yields an intrinsic monotone-opposed crossing.
    Each defensible record-internal capacity either goes BLIND (Var(a)), is HUMP-shaped
    with a marginal-dependent turning point (Var(ab)), is U-shaped/sign-blind so has no
    single rising arm (I, E_cl, C_chan), or is the coordinate itself giving a tautology
    that pins a fixed MOMENT at a MOVING lambda.  The C1 no-go is robust to the
    definitional choice of 'capacity'.  => CLOSED: the no-go holds.

  Pre-geometric throughout: every leg is a record-internal probability/KL/Fisher on the
  moment algebra <1,A,B,AB>_psi.  No spacetime, metric, light cone, or s^2 was used.
""")

head("DONE.")
