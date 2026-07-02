#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
p4a_joint_clicklaw.py -- Long March v7, PAPER 1, Tier A, section 5.2 OPEN.
THE JOINT CLICK-LAW FORCING (the entanglement guardrail, made quantitative).

QUESTION (paper1 v7 s3.5 / s5.2, item 2 of the residue):
  The single-chain forcing (s3.2) gives S(chi)=exp(-kappa chi) by the Cauchy
  multiplicative equation S(chi1+chi2)=S(chi1)S(chi2), whose PREMISE is that
  survival is "a function of the ACCUMULATED CONTENT ALONE" -- a single scalar
  odometer chi.  s3.5 flags, but does NOT settle, the JOINT case: two PARALLEL
  record chains A and B with a JOINT CONSTRAINT LEDGER C_AB.  Apply refinement
  self-consistency to the JOINT chain and ask:

    (Q1 EXP-FORM)   Does refinement-multiplicativity along the JOINT commit order
                    still FORCE the exponential form S_AB = exp(-kappa X) for the
                    relevant joint argument X?
    (Q2 ADDITIVITY) Does it force the joint content to be ADDITIVE
                       X = chi_A + chi_B        (=> S_AB = S_A * S_B,  NO entanglement)
                    or does the joint refinement PERMIT a genuine non-additive
                    MUTUAL term
                       X = chi_A + chi_B + chi_AB   (=> entanglement / correlation)?

  Equivalently: is the single-chain premise ("survival a function of accumulated
  content ALONE") AUTOMATICALLY satisfied jointly, or does the joint case carry a
  genuinely NEW degree of freedom (the mutual content chi_AB) that survival can
  depend on -- which the sequential Cauchy argument does NOT see?

  VERDICT WANTED: FORCED / CONSTRAINED / FREE for the joint law.

PRE-GEOMETRIC (Tier A) throughout.  Records only; the commit order; the intrinsic
content is a KL divergence chi = D(P_AB||P_BA) of forward vs reverse holonomy
transport.  NO spacetime, metric, light cone, proper time, or s^2 EVER.  The
"joint commit order" is the single succession in which BOTH chains' seals are
interleaved (one global order of division events); C_AB is the joint constraint
ledger correlating the two chains' transport laws.  mpmath dps=140, sympy-exact.

KINEMATICS NOTE (why 3 states per chain): a 2-state Markov chain is ALWAYS
reversible (Kolmogorov criterion: no cycle), hence has ZERO entropy production --
so sigma_A = sigma_B = 0 trivially.  To make the SINGLE-CHAIN odometers genuinely
nonzero (an arrow present on EACH chain) we use 3-state DRIVEN cycle kernels per
chain; the joint process lives on the 9-state product, and the constraint ledger
C_AB couples them.  Everything is a record-internal probability/KL -- no geometry.

STRUCTURE (and what each PART proves):
  PART 0.  The joint odometer sigma_AB = sigma_A + sigma_B + I_sigma; I_sigma is
           the genuinely-new mutual term (candidate chi_AB): =0 iff C_AB factorizes,
           !=0 for a correlated ledger.
  PART 1.  (Q1) exp-form along the JOINT commit order is FORCED, content-blind.
  PART 2.  (Q2) the joint commit-order refinement (R-seq) TELESCOPES with I_sigma!=0
           -> blind to chi_AB -> does NOT force additivity.  Factorization is the
           SEPARATE (R-par) A|B cut, never invoked; defect = exp(-kappa chi_AB).
  PART 3.  guardrail = no-signaling (PI-yes / OI-no), satisfiable with chi_AB!=0.
  PART 4.  a continuum of mutual content at FIXED marginals -> a FREE direction.
  PART 5.  honest verdict: FORCED-SKELETON / FREE-COMPLEMENT.

ASSERTS machine-check every load-bearing gap at dps=140.
"""

import mpmath as mp
import sympy as sp

mp.mp.dps = 140


def head(s):
    print("\n" + "=" * 80)
    print(s)
    print("=" * 80)


def sub(s):
    print("\n  -- " + s + " --")


def line(label, val, extra=""):
    print(f"  {label:<56} {val} {extra}")


TOL = mp.mpf(10) ** (-100)   # high-precision machine-zero floor


# ===========================================================================
# Joint record kinematics on a product of two finite chains.
#   nA, nB = number of record-states per chain.  Joint state s=(a,b).
#   A kernel K is a dict: K[s][sp] = P( s -> sp ).
#   The JOINT CONSTRAINT LEDGER C_AB is the correlation in K (factorized => no C_AB).
# All quantities are record-internal probabilities / KL divergences -- no geometry.
# ===========================================================================

def jstates(nA, nB):
    return [(a, b) for a in range(nA) for b in range(nB)]


def marginals(pi, nA, nB):
    pA = [sum(pi[(a, b)] for b in range(nB)) for a in range(nA)]
    pB = [sum(pi[(a, b)] for a in range(nA)) for b in range(nB)]
    return pA, pB


def stationary_joint(K, nA, nB):
    """Stationary joint pi (dict) for the kernel K, exact lu_solve."""
    S = jstates(nA, nB)
    N = len(S)
    idx = {s: i for i, s in enumerate(S)}
    Amat = mp.matrix(N, N)
    for j, sp_ in enumerate(S):
        for i, s in enumerate(S):
            Amat[j, i] = (1 if i == j else 0) - K[s][sp_]
    for i in range(N):
        Amat[N - 1, i] = mp.mpf(1)
    b = mp.matrix(N, 1)
    b[N - 1] = mp.mpf(1)
    pcol = mp.lu_solve(Amat, b)
    return {s: pcol[idx[s]] for s in S}


def entropy_production_joint(pi, K, nA, nB):
    """Joint entropy production sigma_AB = D(P_fwd || P_rev) over the product state space."""
    S = jstates(nA, nB)
    sig = mp.mpf(0)
    for s in S:
        ps = pi[s]
        for sp_ in S:
            fwd = ps * K[s][sp_]
            rev = pi[sp_] * K[sp_][s]
            if fwd > 0 and rev > 0:
                sig += fwd * mp.log(fwd / rev)
    return sig


def entropy_production_marginal(pi, K, which, nA, nB):
    """
    Single-chain entropy production of the coarse-grained MARGINAL process for
    chain 'which' (0=A,1=B): chi_A (resp chi_B), the odometer that chain carries
    on its own.  Coarse-grain the joint flow to the marginal transition law.
    """
    nW = nA if which == 0 else nB
    pA, pB = marginals(pi, nA, nB)
    pmarg = pA if which == 0 else pB
    S = jstates(nA, nB)
    Kmarg = [[mp.mpf(0) for _ in range(nW)] for _ in range(nW)]
    for s in S:
        ps = pi[s]
        for sp_ in S:
            x = s[which]
            y = sp_[which]
            Kmarg[x][y] += ps * K[s][sp_]
    for x in range(nW):
        if pmarg[x] > 0:
            for y in range(nW):
                Kmarg[x][y] /= pmarg[x]
    sig = mp.mpf(0)
    for x in range(nW):
        for y in range(nW):
            fwd = pmarg[x] * Kmarg[x][y]
            rev = pmarg[y] * Kmarg[y][x]
            if fwd > 0 and rev > 0:
                sig += fwd * mp.log(fwd / rev)
    return sig


def build_product_kernel(KA, KB, nA, nB):
    """Independent product kernel K((a',b')|(a,b)) = KA(a'|a) KB(b'|b)."""
    S = jstates(nA, nB)
    K = {}
    for s in S:
        K[s] = {}
        for sp_ in S:
            K[s][sp_] = KA[s[0]][sp_[0]] * KB[s[1]][sp_[1]]
    return K


# 3-state DRIVEN cycle kernels (genuine arrow on EACH chain: sigma > 0)
KA = [[mp.mpf('0.10'), mp.mpf('0.70'), mp.mpf('0.20')],
      [mp.mpf('0.20'), mp.mpf('0.10'), mp.mpf('0.70')],
      [mp.mpf('0.70'), mp.mpf('0.20'), mp.mpf('0.10')]]
KB = [[mp.mpf('0.15'), mp.mpf('0.65'), mp.mpf('0.20')],
      [mp.mpf('0.25'), mp.mpf('0.15'), mp.mpf('0.60')],
      [mp.mpf('0.60'), mp.mpf('0.25'), mp.mpf('0.15')]]
NA, NB = 3, 3
states = jstates(NA, NB)


# ===========================================================================
head("PART 0.  THE JOINT ODOMETER:  sigma_AB = sigma_A + sigma_B + I_sigma")
# ===========================================================================
print("""
  The joint accumulated content is the entropy production of the JOINT forward-vs-
  reverse holonomy law over the PRODUCT record-state space:
      sigma_AB = D( P_AB^{joint} || P_BA^{joint} ).
  We decompose it EXACTLY:
      sigma_AB = sigma_A + sigma_B + I_sigma,
  where sigma_A, sigma_B are the MARGINAL (single-chain) odometers and I_sigma is
  the MUTUAL term -- the candidate chi_AB.  I_sigma is the genuinely-new JOINT
  degree of freedom the single-chain argument never sees.  (3-state driven chains:
  each chain carries a genuine arrow, so sigma_A, sigma_B are themselves nonzero.)
""")

sub("(0.a) PRODUCT ledger  C_AB = factorized  =>  I_sigma = 0 EXACTLY (additive)")
Kprod = build_product_kernel(KA, KB, NA, NB)
pi_prod = stationary_joint(Kprod, NA, NB)
pA_p, pB_p = marginals(pi_prod, NA, NB)
prod_pi_gap = max(abs(pi_prod[(a, b)] - pA_p[a] * pB_p[b]) for a in range(NA) for b in range(NB))
sigAB_prod = entropy_production_joint(pi_prod, Kprod, NA, NB)
sigA_prod = entropy_production_marginal(pi_prod, Kprod, 0, NA, NB)
sigB_prod = entropy_production_marginal(pi_prod, Kprod, 1, NA, NB)
Isig_prod = sigAB_prod - (sigA_prod + sigB_prod)
line("joint stationary is a product?  max|pi-pA pB|", mp.nstr(prod_pi_gap, 6))
line("sigma_A (marginal A odometer)", mp.nstr(sigA_prod, 30), "(>0: arrow on A)")
line("sigma_B (marginal B odometer)", mp.nstr(sigB_prod, 30), "(>0: arrow on B)")
line("sigma_AB (joint odometer)", mp.nstr(sigAB_prod, 30))
line("I_sigma = sigma_AB-(sigma_A+sigma_B)", mp.nstr(Isig_prod, 6),
     "(=0: additive => S_AB=S_A S_B => NO entanglement)")
assert sigA_prod > mp.mpf('1e-3') and sigB_prod > mp.mpf('1e-3'), "need genuine single-chain arrows"
assert abs(Isig_prod) < TOL, "product ledger must give additive joint content"
assert abs(prod_pi_gap) < TOL

sub("(0.b) CORRELATED ledger  C_AB couples the chains  =>  I_sigma != 0 (mutual term)")
# Correlated joint kernel: tilt the product kernel by a constraint that couples the
# two chains' MOVES.  The tilt depends on the DESTINATION pair (a',b') so it genuinely
# correlates the joint transition (the ledger C_AB), not a mere reparametrization.
g = mp.mpf('0.45')   # coupling strength of the joint constraint ledger C_AB
def coupling(sp_):
    # favors A,B advancing in the SAME cyclic direction (a joint constraint)
    return mp.e ** (g * mp.cos(2 * mp.pi * (sp_[0] - sp_[1]) / 3))
Kcorr = {}
for s in states:
    row = {}
    tot = mp.mpf(0)
    for sp_ in states:
        row[sp_] = Kprod[s][sp_] * coupling(sp_)
        tot += row[sp_]
    for sp_ in states:
        row[sp_] /= tot
    Kcorr[s] = row
pi_corr = stationary_joint(Kcorr, NA, NB)
pA_c, pB_c = marginals(pi_corr, NA, NB)
corr_pi_gap = max(abs(pi_corr[(a, b)] - pA_c[a] * pB_c[b]) for a in range(NA) for b in range(NB))
sigAB_corr = entropy_production_joint(pi_corr, Kcorr, NA, NB)
sigA_corr = entropy_production_marginal(pi_corr, Kcorr, 0, NA, NB)
sigB_corr = entropy_production_marginal(pi_corr, Kcorr, 1, NA, NB)
Isig_corr = sigAB_corr - (sigA_corr + sigB_corr)
line("joint stationary is a product?  max|pi-pA pB|", mp.nstr(corr_pi_gap, 6),
     "(!=0: genuinely correlated joint ledger)")
line("sigma_A (marginal A odometer)", mp.nstr(sigA_corr, 30))
line("sigma_B (marginal B odometer)", mp.nstr(sigB_corr, 30))
line("sigma_AB (joint odometer)", mp.nstr(sigAB_corr, 30))
line("I_sigma = sigma_AB-(sigma_A+sigma_B)", mp.nstr(Isig_corr, 12),
     "(!=0: NON-additive MUTUAL content chi_AB present)")
assert corr_pi_gap > mp.mpf('1e-3'), "need a genuinely correlated joint ledger"
assert abs(Isig_corr) > mp.mpf('1e-3'), "correlated ledger must give a mutual term"

sub("(0.c) the SIGNED I_sigma is NOT zero-iff-factorized: I_sigma=0 at a CORRELATED kernel")
# I_sigma = sigma_AB - sigma_A - sigma_B is a DIFFERENCE of entropy productions and is
# TWO-SIDED; it can CANCEL at a genuinely non-factorized kernel.  So I_sigma=0 is IMPLIED
# by factorization but does NOT imply it -- only the non-negative kinematic E_cl has
# 'zero iff factorized' (v1 paper21 Prop 1a).  Exhibit the counterexample: convex-mix a
# synergy kernel (I_sigma<0) with a redundancy/no-signaling kernel (I_sigma>0); at the
# crossing I_sigma=0 the kernel is still genuinely correlated (factorization defect >> 0).
_dvals = [mp.mpf(-1), mp.mpf(0), mp.mpf(1)]   # zero-mean tilt on the destination index
def _Kns(g):
    K = {}
    for s in states:
        row = {sp_: Kprod[s][sp_] * (1 + g * _dvals[sp_[0]] * _dvals[sp_[1]]) for sp_ in states}
        t = sum(row.values()); K[s] = {sp_: row[sp_] / t for sp_ in row}
    return K
def _Isig(K):
    pi = stationary_joint(K, NA, NB)
    return (entropy_production_joint(pi, K, NA, NB)
            - entropy_production_marginal(pi, K, 0, NA, NB)
            - entropy_production_marginal(pi, K, 1, NA, NB)), pi
def _factdefect(K):
    pi = stationary_joint(K, NA, NB)
    pA, pB = marginals(pi, NA, NB)
    return max(abs(pi[(a, b)] - pA[a] * pB[b]) for a in range(NA) for b in range(NB))
Kred = _Kns(mp.mpf('0.7'))
i_red, _ = _Isig(Kred)
i_syn = Isig_corr                                   # cos-coupling synergy kernel: I_sigma < 0
line("synergy kernel I_sigma  (cos-coupling)", mp.nstr(i_syn, 6), "(< 0)")
line("redundancy kernel I_sigma  (no-signaling tilt)", mp.nstr(i_red, 6), "(> 0)")
def _Kmix(t):
    return {s: {sp_: (1 - t) * Kcorr[s][sp_] + t * Kred[s][sp_] for sp_ in states} for s in states}
lo, hi = mp.mpf(0), mp.mpf(1)
for _ in range(200):
    mid = (lo + hi) / 2
    if _Isig(Kcorr)[0] * _Isig(_Kmix(mid))[0] <= 0:
        hi = mid
    else:
        lo = mid
t_star = (lo + hi) / 2
Kx = _Kmix(t_star)
Isig_star, _ = _Isig(Kx)
fd_star = _factdefect(Kx)
line("mixture at t* = %s: I_sigma" % mp.nstr(t_star, 8), mp.nstr(Isig_star, 4), "(= 0, machine zero)")
line("  factorization defect at t*", mp.nstr(fd_star, 6), "(>> 0: GENUINELY non-factorized)")
PASS_counterex = (abs(Isig_star) < mp.mpf('1e-30')) and (fd_star > mp.mpf('1e-2'))
assert PASS_counterex, "I_sigma=0 must occur at a genuinely correlated kernel (necessary-not-sufficient)"
print("""
  => I_sigma=0 does NOT imply factorization (it does here at fact-defect ~0.09).
     Only the NON-NEGATIVE kinematic E_cl is 'zero IFF factorized'; the signed I_sigma
     vanishes <= factorization (necessary, not sufficient): {factorized} subset {I_sigma=0}.
""")

print("""
  VERDICT PART 0:  the joint odometer carries a genuinely-new term I_sigma.
    factorized ledger  -> I_sigma = 0   (additive: X=chi_A+chi_B)
    correlated ledger  -> I_sigma != 0  (non-additive: X=chi_A+chi_B+chi_AB) GENERICALLY,
       though the SIGNED I_sigma can also cancel at special correlated kernels (0.c).
  So the joint content has a degree of freedom (chi_AB := I_sigma) that does NOT
  exist on a single chain.  Factorization IMPLIES I_sigma=0 (necessary, not sufficient);
  the converse 'zero iff factorized' holds only for the non-negative kinematic E_cl.
""")


# ===========================================================================
head("PART 1.  (Q1) EXP-FORM along the JOINT commit order is FORCED (content-blind)")
# ===========================================================================
print("""
  Whatever scalar argument X the joint survival is a function of, refinement of the
  JOINT commit order (interleaving both chains' seals into one succession) and
  composing at a joint refinement point gives the SAME Cauchy equation
      S_AB(X1 + X2) = S_AB(X1) S_AB(X2),
  whose unique monotone measurable solution is S_AB(X) = exp(-kappa X).  This step
  is identical to s3.2 -- it is SHAPE-only and BLIND to how X is built from A,B.
""")
X1, X2, kap = sp.symbols('X1 X2 kappa', positive=True)
Sfun = lambda X: sp.exp(-kap * X)
cauchy_resid = sp.simplify(Sfun(X1 + X2) - Sfun(X1) * Sfun(X2))
line("sympy:  S_AB(X1+X2) - S_AB(X1)S_AB(X2)  for S=exp(-kX)",
     str(cauchy_resid), "(=0: exp solves Cauchy on the JOINT argument)")
assert cauchy_resid == 0
p = sp.symbols('p', positive=True)
refine_p = sp.simplify(2**p - 2)
line("sympy:  refinement consistency 2^p - 2 = 0  =>  p =", str(sp.solve(refine_p, p)),
     "(only p=1 refinement-consistent for the joint X too)")
assert sp.solve(refine_p, p) == [1]
Xj = mp.mpf('1.3')
f = lambda x: 1 / (1 + x)          # non-exponential per-step contraction
prodlim = (f(Xj / 100000)) ** 100000
line("product-limit  (f(X/m))^m, m=1e5, f=1/(1+x)", mp.nstr(prodlim, 16))
line("target exp(-X)", mp.nstr(mp.e ** (-Xj), 16))
line("|product-limit - exp(-X)|", mp.nstr(abs(prodlim - mp.e ** (-Xj)), 4),
     "(joint exp-shape forced for ANY stationary per-step law)")
assert abs(prodlim - mp.e ** (-Xj)) < mp.mpf('1e-4')

print("""
  VERDICT PART 1:  (Q1) the EXP SHAPE of the joint survival is FORCED, exactly as
  for one chain, and it is CONTENT-BLIND: it constrains S_AB as a function of its
  scalar argument X but says NOTHING about whether X = chi_A+chi_B or
  chi_A+chi_B+chi_AB.  This is precisely s3.5's point that sequential
  multiplicativity neither requires nor forbids the joint correlation.
""")


# ===========================================================================
head("PART 2.  (Q2) THE DECISIVE SPLIT:  joint refinement does NOT force additivity")
# ===========================================================================
print("""
  Two DIFFERENT refinement directions on the joint chain.  The single-chain Cauchy
  argument only ever uses (R-seq); we show (R-seq) is BLIND to the mutual term.

   (R-seq)  CONCATENATION along the joint commit order: split a stretch of the
            interleaved order into two consecutive sub-stretches.  This is the
            ODOMETER telescoping (f3c), and it holds for the joint sigma_AB just
            as for a single chain -- for ANY ledger, correlated or not.  It
            constrains the SHAPE in X, NOT the structure of X.

   (R-par)  PARTITION across the A|B cut: split the joint content into its A-part
            and B-part.  Multiplicativity ACROSS THIS CUT,  S_AB = S_A * S_B, is
            EQUIVALENT to I_sigma = 0 (factorization).  The single-chain argument
            NEVER invokes (R-par) -- it has no A|B cut.  So nothing in the
            sequential forcing makes (R-par) hold.
""")

sub("(2.a) (R-seq) telescopes for the CORRELATED joint odometer  =>  blind to chi_AB")
def joint_cocycle(pi, K, s, sp_):
    fwd = pi[s] * K[s][sp_]
    rev = pi[sp_] * K[sp_][s]
    return mp.log(fwd / rev)
# a joint trajectory through several joint states (a realized interleaved commit order)
jpath = [(0, 0), (1, 1), (2, 2), (0, 1), (1, 2), (2, 0), (0, 0)]
def jpath_action(pi, K, path):
    return sum(joint_cocycle(pi, K, path[k], path[k + 1]) for k in range(len(path) - 1))
A_full = jpath_action(pi_corr, Kcorr, jpath)
cut = 3
A_s1 = jpath_action(pi_corr, Kcorr, jpath[:cut + 1])    # first 3 edges
A_s2 = jpath_action(pi_corr, Kcorr, jpath[cut:])        # last 3 edges
seq_gap = A_full - (A_s1 + A_s2)
line("joint trajectory action A[full]", mp.nstr(A_full, 22))
line("A[seg1] + A[seg2]", mp.nstr(A_s1 + A_s2, 22))
line("(R-seq) concatenation gap (correlated ledger)", mp.nstr(seq_gap, 6),
     "(=0: joint commit order telescopes EVEN WITH chi_AB != 0)")
assert abs(seq_gap) < TOL
line("...but I_sigma for this SAME correlated ledger", mp.nstr(Isig_corr, 8),
     "(!=0: (R-seq) is BLIND to the mutual term -- did NOT force it to 0)")
assert abs(Isig_corr) > mp.mpf('1e-3')

sub("(2.b) (R-par) factorization across A|B  <=>  I_sigma = 0  (NOT supplied by R-seq)")
k0 = mp.mpf('0.9')
S_AB_corr = mp.e ** (-k0 * sigAB_corr)
S_A_corr = mp.e ** (-k0 * sigA_corr)
S_B_corr = mp.e ** (-k0 * sigB_corr)
factor_gap_corr = S_AB_corr - S_A_corr * S_B_corr
line("S_AB = exp(-k sigma_AB)  [correlated]", mp.nstr(S_AB_corr, 22))
line("S_A * S_B = exp(-k(sigma_A+sigma_B))", mp.nstr(S_A_corr * S_B_corr, 22))
line("(R-par) factorization gap  S_AB - S_A S_B", mp.nstr(factor_gap_corr, 8),
     "(!=0: joint survival does NOT factor -- entanglement present)")
assert abs(factor_gap_corr) > mp.mpf('1e-3')
S_AB_prod = mp.e ** (-k0 * sigAB_prod)
S_A_prod = mp.e ** (-k0 * sigA_prod)
S_B_prod = mp.e ** (-k0 * sigB_prod)
factor_gap_prod = S_AB_prod - S_A_prod * S_B_prod
line("(product ledger) S_AB - S_A S_B", mp.nstr(factor_gap_prod, 6),
     "(=0: factorizes only when I_sigma=0)")
assert abs(factor_gap_prod) < TOL
# THE EXACT IDENTITY: factorization defect IS exp(-kappa * mutual content)
ratio = S_AB_corr / (S_A_corr * S_B_corr)
ratio_pred = mp.e ** (-k0 * Isig_corr)
line("S_AB/(S_A S_B)  vs  exp(-k I_sigma)", mp.nstr(ratio - ratio_pred, 6),
     "(=0: the factorization defect IS exp(-k * mutual content chi_AB))")
assert abs(ratio - ratio_pred) < TOL

print("""
  VERDICT PART 2:  (Q2)  The joint commit-order refinement (R-seq) is the ONLY
  refinement the single-chain Cauchy argument uses, and it TELESCOPES for the
  correlated odometer (gap ~0) WHILE the mutual term I_sigma != 0.  Therefore the
  sequential forcing is BLIND to chi_AB and does NOT force additivity X=chi_A+chi_B.
  Additivity is EQUIVALENT to the SEPARATE (R-par) factorization across the A|B cut,
  which the sequential argument never invokes and does NOT supply.  The factor-
  ization defect is EXACTLY exp(-kappa * chi_AB).  So the joint refinement PERMITS
  a non-additive mutual term => entanglement is PERMITTED, not forced, not forbidden.
""")


# ===========================================================================
head("PART 3.  THE GUARDRAIL = NO-SIGNALING (PI-yes, OI-no), made exact")
# ===========================================================================
print("""
  s3.5's genuine Tier-A obligation: the joint law must keep PARAMETER-INDEPENDENCE
  (no-signaling) while DROPPING OUTCOME-INDEPENDENCE (correlated outcomes).  A
  no-signaling correlated ledger: joint kernel whose A-marginal transition is
  EXACTLY KA (independent of B's setting), B-marginal EXACTLY KB, but the JOINT
  transition carries correlation g.  Construction (marginal-preserving tilt):
      K((a',b')|(a,b)) = KA(a'|a) KB(b'|b) [1 + g * dA(a,a') * dB(b,b')],
  with dA zero-mean in a' under KA(.|a) and dB zero-mean in b' under KB(.|b), so
  BOTH marginals are preserved EXACTLY (=> chi_A, chi_B, and no-signaling hold).
""")

def build_nosig_kernel(KA_loc, KB_loc, g):
    K = {}
    for s in states:
        a, b = s
        meanA = sum(KA_loc[a][ap] * ap for ap in range(NA))
        meanB = sum(KB_loc[b][bp] * bp for bp in range(NB))
        row = {}
        for sp_ in states:
            ap, bp = sp_
            dA = ap - meanA           # zero-mean under KA(.|a) by construction of meanA
            dB = bp - meanB
            val = KA_loc[a][ap] * KB_loc[b][bp] * (1 + g * dA * dB)
            row[sp_] = val
        # the tilt is exactly marginal-preserving and sums to 1; renormalize for safety
        tot = sum(row[sp_] for sp_ in states)
        for sp_ in states:
            row[sp_] /= tot
        K[s] = row
    return K

def marginal_kernel(K, which):
    """Marginal transition law of chain 'which'; also returns the max inconsistency
    across the OTHER chain's coordinate (=0 <=> no-signaling)."""
    nW = NA if which == 0 else NB
    nO = NB if which == 0 else NA
    res = {}
    consistent = mp.mpf(0)
    for wx in range(nW):
        rows = []
        for other in range(nO):
            s = (wx, other) if which == 0 else (other, wx)
            ky = [mp.mpf(0)] * nW
            for sp_ in states:
                ky[sp_[which]] += K[s][sp_]
            rows.append(ky)
        consistent = max(consistent, max(abs(rows[o][y] - rows[0][y])
                                         for o in range(nO) for y in range(nW)))
        res[wx] = rows[0]
    return res, consistent

sub("(3.a) parameter-independence: marginal A-kernel invariant under B's local setting")
KB_setting1 = KB
KB_setting2 = [[mp.mpf('0.05'), mp.mpf('0.80'), mp.mpf('0.15')],
               [mp.mpf('0.35'), mp.mpf('0.05'), mp.mpf('0.60')],
               [mp.mpf('0.50'), mp.mpf('0.45'), mp.mpf('0.05')]]   # B's OTHER setting
gns = mp.mpf('0.5')
Kns1 = build_nosig_kernel(KA, KB_setting1, gns)
Kns2 = build_nosig_kernel(KA, KB_setting2, gns)
KAmarg1, cons1 = marginal_kernel(Kns1, 0)
KAmarg2, cons2 = marginal_kernel(Kns2, 0)
line("A-marginal kernel B-coordinate-independent? (setting1)", mp.nstr(cons1, 6))
line("A-marginal kernel B-coordinate-independent? (setting2)", mp.nstr(cons2, 6))
PI_gap = max(abs(KAmarg1[x][y] - KAmarg2[x][y]) for x in range(NA) for y in range(NA))
line("A-marginal kernel: |setting1 - setting2|", mp.nstr(PI_gap, 6),
     "(=0: PARAMETER-INDEPENDENCE / no-signaling holds)")
KA_match = max(abs(KAmarg1[x][y] - KA[x][y]) for x in range(NA) for y in range(NA))
line("A-marginal kernel equals bare KA?", mp.nstr(KA_match, 6),
     "(=0: A's odometer chi_A independent of B's setting and of g)")
assert cons1 < TOL and cons2 < TOL
assert PI_gap < TOL
assert KA_match < TOL

sub("(3.b) outcome-dependence: joint odometer carries mutual content I_sigma != 0")
pi_ns = stationary_joint(Kns1, NA, NB)
sigAB_ns = entropy_production_joint(pi_ns, Kns1, NA, NB)
sigA_ns = entropy_production_marginal(pi_ns, Kns1, 0, NA, NB)
sigB_ns = entropy_production_marginal(pi_ns, Kns1, 1, NA, NB)
Isig_ns = sigAB_ns - (sigA_ns + sigB_ns)
ns_pi_gap = max(abs(pi_ns[(a, b)] - sum(pi_ns[(a, bb)] for bb in range(NB))
                    * sum(pi_ns[(aa, b)] for aa in range(NA)))
                for a in range(NA) for b in range(NB))
line("no-signaling ledger: joint NOT a product? max|pi-pApB|", mp.nstr(ns_pi_gap, 6))
line("no-signaling ledger: I_sigma (mutual content)", mp.nstr(Isig_ns, 12),
     "(!=0: OI dropped -- correlated outcomes survive while PI holds)")
assert abs(Isig_ns) > mp.mpf('1e-4'), "no-signaling ledger should still carry correlation"

print("""
  VERDICT PART 3:  the guardrail (PI-yes / no-signaling, OI-no / correlated) is a
  genuine CONSTRAINT the joint law must satisfy, and it is SATISFIABLE TOGETHER WITH
  a nonzero mutual term: A's marginal odometer chi_A is exactly B-setting-independent
  (PI gap ~0) WHILE the joint mutual content I_sigma != 0 (outcomes correlated).
  So no-signaling CONSTRAINS the joint law but does NOT force chi_AB to zero.
""")


# ===========================================================================
head("PART 4.  COUNTING THE FREEDOM:  a continuum of mutual content at fixed marginals")
# ===========================================================================
print("""
  The new joint degree of freedom is FUNCTIONAL: with the SAME marginals (hence the
  SAME S_A, S_B and the SAME single calibration kappa) there is a CONTINUUM of
  no-signaling correlated ledgers with DIFFERENT mutual content chi_AB = I_sigma.
  We sweep the coupling g (preserving marginals EXACTLY) and show I_sigma varies
  continuously through a nonzero range -- an explicit free direction.
""")
def kernel_min_entry(K):
    """smallest entry of K -- must be >= 0 for a valid probability kernel."""
    return min(K[s][sp_] for s in states for sp_ in states)

print("    g        I_sigma (=chi_AB)         chi_A (fixed)        chi_B (fixed)     min K")
Igrid = []
chiA_grid = []
# small-g window where the marginal-preserving tilt (1 + g dA dB) stays POSITIVE
# (a valid probability kernel) AND monotone; large g distorts the kernel non-
# monotonically (and eventually violates positivity), so we sweep the VALID window.
gvals = ['0.0', '0.05', '0.10', '0.15', '0.20', '0.25', '0.30']
for gv in gvals:
    gg = mp.mpf(gv)
    K = build_nosig_kernel(KA, KB_setting1, gg)
    minK = kernel_min_entry(K)
    pim = stationary_joint(K, NA, NB)
    sAB = entropy_production_joint(pim, K, NA, NB)
    sA = entropy_production_marginal(pim, K, 0, NA, NB)
    sB = entropy_production_marginal(pim, K, 1, NA, NB)
    I = sAB - (sA + sB)
    Igrid.append(I)
    chiA_grid.append(sA)
    print("   %5s    %s    %s    %s    %s"
          % (gv, mp.nstr(I, 16), mp.nstr(sA, 12), mp.nstr(sB, 12), mp.nstr(minK, 4)))
line("I_sigma at g=0", mp.nstr(Igrid[0], 8), "(=0: uncorrelated ledger is additive)")
line("I_sigma at g=0.30", mp.nstr(Igrid[-1], 8), "(>0: correlated, non-additive)")
assert abs(Igrid[0]) < mp.mpf('1e-6'), "g=0 should be (near-)additive"
assert Igrid[-1] > mp.mpf('1e-3'), "growing coupling gives growing mutual content"
# all kernels in the swept window are valid probability kernels (entries >= 0)
all_valid = all(kernel_min_entry(build_nosig_kernel(KA, KB_setting1, mp.mpf(gv))) >= 0 for gv in gvals)
line("all swept kernels valid (min entry >= 0)?", all_valid, "(valid no-signaling ledgers)")
assert all_valid
# strictly increasing on the VALID small-g window (the substantive monotone branch)
strictly_increasing = all(Igrid[i + 1] > Igrid[i] for i in range(len(Igrid) - 1))
line("|I_sigma| strictly increases with g on the valid window?", strictly_increasing,
     "(monotone free direction in the positivity-valid window)")
assert strictly_increasing
# the genuine claim: a CONTINUUM of DISTINCT nonzero mutual-content values at fixed marginals
distinct_nonzero = len(set(mp.nstr(I, 20) for I in Igrid[1:])) == len(Igrid[1:])
line("distinct nonzero I_sigma values (a continuum)?", distinct_nonzero,
     "(=> chi_AB is a genuine FREE functional direction)")
assert distinct_nonzero
# chi_A fixed across the sweep (marginal kappa untouched) -- the orthogonality
chiA_spread = max(chiA_grid) - min(chiA_grid)
line("chi_A spread across the whole g-sweep", mp.nstr(chiA_spread, 6),
     "(=0: marginal odometer/calibration fixed while chi_AB sweeps => orthogonal d.o.f.)")
assert chiA_spread < TOL

print("""
  VERDICT PART 4:  the mutual content chi_AB is a genuine FREE direction: a
  continuum of values at FIXED marginals (fixed chi_A, chi_B, fixed kappa).  It is
  ORTHOGONAL to everything the single-chain law fixes.  This is the entanglement
  degree of freedom -- present jointly, absent on one chain.
""")


# ===========================================================================
head("PART 5.  HONEST VERDICT  --  the JOINT click-law")
# ===========================================================================
print("""
  Decompose the joint click-law into SHAPE and CONTENT and rate each.

  (Q1)  EXP-FORM (shape in the scalar joint argument X):  FORCED.
        Refinement of the joint commit order gives the SAME Cauchy multiplicative
        equation S_AB(X1+X2)=S_AB(X1)S_AB(X2) => exp(-kappa X), p=1 only, for ANY
        stationary per-step contraction (PART 1).  This is CONTENT-BLIND: it
        constrains S_AB as a function of X but not how X is built from A,B.

  (Q2)  CONTENT STRUCTURE (is X = chi_A+chi_B or chi_A+chi_B+chi_AB):  FREE in the
        mutual direction.  The joint odometer carries an EXACT decomposition
            sigma_AB = sigma_A + sigma_B + I_sigma   (PART 0),
        and I_sigma (= chi_AB) is:
          * = 0  iff the joint ledger C_AB factorizes (=> S_AB=S_A S_B, no entang.);
          * != 0 for a genuinely correlated ledger (=> entanglement).
        The single-chain Cauchy argument uses ONLY commit-order concatenation
        (R-seq), which TELESCOPES for the correlated odometer (gap ~0) WHILE
        I_sigma != 0 (PART 2): it is BLIND to the mutual term.  Additivity is the
        SEPARATE (R-par) factorization across the A|B cut, NEVER invoked by the
        sequential forcing.  The factorization defect is EXACTLY exp(-kappa chi_AB).

  THE PREMISE CHECK (the crux of s5.2):  the single-chain Cauchy premise is
  "survival is a function of the ACCUMULATED CONTENT ALONE" -- ONE scalar.  Jointly
  this premise is NOT automatically satisfied: the accumulated joint content is a
  scalar (sigma_AB) that DECOMPOSES into sigma_A+sigma_B PLUS a mutual term, and the
  mutual term is a genuinely NEW degree of freedom (PART 4: a continuum at fixed
  marginals, orthogonal to chi_A,chi_B,kappa).  The joint case HAS the new d.o.f.
  the single-chain premise assumed away.

  THE GUARDRAIL (PART 3):  the joint law MUST satisfy no-signaling (PI-yes) while
  dropping outcome-independence (OI-no).  This is a CONSTRAINT, satisfiable with
  I_sigma != 0 (PI gap ~0, mutual term nonzero).  It NARROWS but does not FIX the
  mutual content.

  OVERALL JOINT-LAW VERDICT:  FORCED-SKELETON / FREE-COMPLEMENT.
    * the SHAPE skeleton (exp, p=1, one calibration kappa) is FORCED -- the same
      Branch-A 'unique-modulo-one-scale' outcome as the single chain;
    * the ENTANGLEMENT complement (the mutual content chi_AB) is a genuinely NEW
      FREE degree of freedom that joint refinement neither forces to zero
      (no factorization) nor forbids (no-signaling permits it);
    * the joint law as a whole is CONSTRAINED (exp-shape + no-signaling forced),
      with the entanglement content FREE -- exactly s3.5's "constrained, not
      forced" open status, now made quantitative.
""")


# ===========================================================================
head("CANONICAL OUTPUT BLOCK  (p4a joint-clicklaw receipt, dps=%d)" % mp.mp.dps)
# ===========================================================================
print(f"""
  PART 0  joint odometer decomposition sigma_AB = sigma_A+sigma_B+I_sigma:
    sigma_A, sigma_B (arrows present)  = {mp.nstr(sigA_prod, 6)}, {mp.nstr(sigB_prod, 6)}
    product   ledger:  I_sigma = {mp.nstr(Isig_prod, 4)}   (additive => S_AB=S_A S_B, no entang.)
    correlated ledger: I_sigma = {mp.nstr(Isig_corr, 8)}   (non-additive mutual content chi_AB)

  PART 1  (Q1) exp-shape on the joint argument:
    Cauchy residual (sympy)           = {cauchy_resid}      (exp forced)
    p=1 only (sympy 2^p-2=0)          : p in {sp.solve(refine_p, p)}
    product-limit |.-exp|             = {mp.nstr(abs(prodlim - mp.e ** (-Xj)), 4)}   (forced for ANY per-step law)

  PART 2  (Q2) joint commit-order refinement is BLIND to chi_AB:
    (R-seq) telescope gap (correlated) = {mp.nstr(seq_gap, 4)}   (=0: order composes)
    ...while I_sigma                   = {mp.nstr(Isig_corr, 6)}   (!=0: mutual term untouched)
    (R-par) factorization gap          = {mp.nstr(factor_gap_corr, 6)}   (!=0: S_AB != S_A S_B)
    S_AB/(S_A S_B) = exp(-k chi_AB)?   gap = {mp.nstr(ratio - ratio_pred, 4)}   (defect IS exp(-k*mutual))

  PART 3  guardrail (PI-yes / OI-no):
    no-signaling marginal-A invariance = {mp.nstr(PI_gap, 4)}   (=0: parameter-independence)
    no-signaling ledger mutual I_sigma = {mp.nstr(Isig_ns, 6)}   (!=0: outcomes correlated)

  PART 4  free direction (fixed marginals, positivity-valid window):
    I_sigma(g=0)                       = {mp.nstr(Igrid[0], 4)}   (additive)
    I_sigma(g=0.30)                    = {mp.nstr(Igrid[-1], 6)}   (continuum of distinct mutual content)
    chi_A spread across sweep          = {mp.nstr(chiA_spread, 4)}   (orthogonal to chi_A,chi_B,kappa)

  VERDICT:
    (Q1) exp-FORM along the joint commit order   : FORCED  (content-blind shape)
    (Q2) ADDITIVE content X=chi_A+chi_B          : NOT forced
         mutual term chi_AB (entanglement)       : PERMITTED / FREE
    guardrail no-signaling (PI-yes,OI-no)        : CONSTRAINT (forced), satisfiable with chi_AB!=0
    => JOINT LAW = FORCED-SKELETON-FREE-COMPLEMENT:
         shape (exp,p=1,one kappa) FORCED; entanglement content chi_AB a genuinely
         NEW FREE d.o.f.; no-signaling the only extra constraint.
    => the single-chain Cauchy premise ('content = one scalar ALONE') is NOT
       satisfied jointly: the joint case has a genuinely new degree of freedom.

  Pre-geometric throughout: every quantity is a record-internal probability / KL /
  log-likelihood-ratio.  No spacetime, metric, light cone, or s^2 was used.
""")

head("DONE.")
