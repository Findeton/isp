"""
F3c -- THE SEQUENTIAL CONTENT-ODOMETER.  v7 Long March, Paper 1, Tier A.

R2-B of the Long March: the section-5.1 content-supply question the hostile
review sharpened.  Paper 1 v7 s3.2 derives S(chi)=exp(-kappa chi) from the
Cauchy multiplicative equation S(chi1+chi2)=S(chi1)S(chi2), which requires the
intrinsic content chi to be SEQUENTIALLY (concatenation) additive along the
commit order:

    chi(seg1 then seg2) = chi(seg1) + chi(seg2)          (the ODOMETER)

accumulating a non-negative increment d_chi >= 0.  The review correctly flagged
that this is NOT the parallel/tensor cocycle A_{D1 x D2} = A_{D1} + A_{D2}
(paper4 s34), a DIFFERENT composition, and is currently ASSUMED (s5.1 open).

THE LEAD (the task): paper10's arrow sigma = D(P_AB || P_BA) = E[A_D] is
ENTROPY PRODUCTION.  If chi is the ACCUMULATED entropy production along the
commit order -- chi = sum/integral of d_sigma, d_sigma>=0 by Arrow-Positivity --
then (a) sequential/concatenation additivity is AUTOMATIC (sums concatenate) and
(b) d_chi = d_sigma >= 0 by arrow-positivity.  Does this CLOSE the odometer?

PRE-GEOMETRIC (Tier A): records only, the commit order, chi = D(P_AB||P_BA).
NO spacetime, metric, light cone, or s^2 anywhere.  The only "time" is the
commit order (the succession of seals).

We establish, with high-precision / exact receipts:

  PART 1.  The classical fact (Crooks 1999, Maes 1999, Schnakenberg 1976,
           paper10 ref map): for an ordered (Markov) transport, the TRAJECTORY
           entropy production is the path log-likelihood ratio
               A[omega] = log( dP_fwd / dP_rev )[omega]
           and along a path omega = x_0 -> x_1 -> ... -> x_n it is the SUM of
           per-step exchange-cocycle increments:
               A[omega] = sum_{k=0}^{n-1} a(x_k, x_{k+1}),
               a(x,y) = log[ pi(x) P(y|x) / ( pi(y) P(x|y) ) ]   (paper4 s34 / paper10 T1).
           This is a SEQUENTIAL (concatenation-along-the-path) sum.  We verify
           it on an explicit driven (sigma>0) Markov chain at dps>=100.

  PART 2.  Hence the EXPECTED arrow sigma = E[A] = D(P_fwd||P_rev) accumulates
           ADDITIVELY over CONSECUTIVE segments of the commit order:
               sigma(seg1 then seg2) = sigma(seg1) + sigma(seg2).
           For a stationary order this is sigma_total = n * sigma_step (linear in
           the number of committed steps).  We verify segment-additivity directly
           on the chain (sigma of an n-step window = sum of per-step sigmas), and
           that it does NOT depend on detailed balance (holds for driven sigma>0).

  PART 3.  THE DISTINCTION, made sharp and quantitative.
             PARALLEL / TENSOR cocycle (paper4 s34):  A_{D1 x D2} = A_{D1}+A_{D2}
               -- INDEPENDENT product of two diamonds (joint law = product law);
               additive because log of a product is a sum of logs.  Composition =
               the tensor/independent product (two diamonds SIDE BY SIDE).
             SEQUENTIAL / ODOMETER:  chi(seg1 -> seg2) = chi(seg1)+chi(seg2)
               -- CONCATENATION along the commit order (one chain, end-to-end);
               additive because trajectory entropy production telescopes over the
               Markov factorization of the path measure.  Composition = the
               CHAIN/CONCATENATION (two diamonds NOSE TO TAIL).
           Both are additive, for STRUCTURALLY DIFFERENT reasons.  We compute both
           gaps on the SAME numbers to show they are distinct compositions that
           happen to share the additive conclusion.

  PART 4.  Is the SEQUENTIAL odometer a THEOREM (of arrow-positivity / the holonomy
           cochain h_C of paper4 s40-44) or a separate input?
             (a) Arrow-positivity (paper10 T2) forces d_chi = d_sigma >= 0 (the
                 non-negative increment).  THEOREM: chi is non-decreasing.
             (b) Concatenation-additivity of chi = accumulated sigma is the
                 telescoping of the path-functional sum (PART 1).  THEOREM,
                 GIVEN that chi is *defined* as accumulated entropy production
                 and that the commit order is a genuine ordered (Markov-
                 presentable at the collar) transport.
             (c) The holonomy-cochain gluing law (paper4 s44):  sum_i rho_i =
                 h_b - h_a, rho_i = h_{i+1}-h_i -- a TELESCOPING identity over a
                 chain of sealed diamonds: the chain accumulation of the cochain
                 increments is exactly concatenation-additive.  We verify the
                 telescope at dps>=100.

  PART 5.  HONEST VERDICT.  We separate the two clauses (additivity vs d_chi>=0)
           and state, for each, whether it is FORCED or ASSUMED, and exactly what
           residual assumption remains -- the identification chi := accumulated
           sigma, and whether the commit order is genuinely ordered/Markov-
           presentable.  This is what s5.1 reduces to.

ALL pre-geometric: every quantity is a record-internal pure number (a KL
divergence, a log-likelihood ratio, a probability).  No length, proper time, or
s^2 ever appears.  mpmath dps = 120, sympy-exact where exact.
"""

import mpmath as mp
import sympy as sp

mp.mp.dps = 120


def head(s):
    print("\n" + "=" * 80)
    print(s)
    print("=" * 80)


def line(label, val, extra=""):
    print(f"  {label:<54} {val} {extra}")


# ===========================================================================
# A reusable ordered (Markov) transport on a finite record-state space, with a
# nonzero stationary current (DRIVEN: sigma>0) so the arrow is genuinely present.
# Everything is exact rationals lifted to mpmath; no geometry, just a kernel.
# ===========================================================================
def build_chain():
    """
    Driven 3-state cycle (0->1->2->0 favored).  Pure record kinematics:
    P(y|x) is a transition law on three record labels.  Returns (P, pi) at
    full mpmath precision.  Stationary pi solved exactly.
    """
    # transition matrix rows sum to 1; a biased cycle => nonzero current
    P = [[mp.mpf('0.10'), mp.mpf('0.70'), mp.mpf('0.20')],
         [mp.mpf('0.20'), mp.mpf('0.10'), mp.mpf('0.70')],
         [mp.mpf('0.70'), mp.mpf('0.20'), mp.mpf('0.10')]]
    n = 3
    # stationary distribution: left eigenvector of P with eigenvalue 1
    # solve pi (I - P) = 0 with sum pi = 1  ->  linear system
    A = mp.matrix(n, n)
    for j in range(n):
        for i in range(n):
            A[j, i] = (1 if i == j else 0) - P[i][j]   # (I - P^T) acting on pi column
    # replace last row with normalization
    for i in range(n):
        A[n - 1, i] = mp.mpf(1)
    b = mp.matrix(n, 1)
    b[n - 1] = mp.mpf(1)
    pi_col = mp.lu_solve(A, b)
    pi = [pi_col[i] for i in range(n)]
    return P, pi, n


def per_step_cocycle(P, pi, x, y):
    """a(x,y) = log[ pi(x) P(y|x) / ( pi(y) P(x|y) ) ]  -- paper4 s34 joint cocycle."""
    return mp.log((pi[x] * P[x][y]) / (pi[y] * P[y][x]))


def per_step_sigma(P, pi, n):
    """
    Stationary per-step entropy production
        sigma_step = sum_{x,y} pi(x) P(y|x) * a(x,y)
                   = E_fwd[a]  (= D(P_AB || P_BA) at the one-step joint level).
    """
    s = mp.mpf(0)
    for x in range(n):
        for y in range(n):
            joint = pi[x] * P[x][y]
            s += joint * per_step_cocycle(P, pi, x, y)
    return s


def path_entropy_production(P, pi, path):
    """A[omega] = sum_k a(x_k, x_{k+1}) -- the TRAJECTORY entropy production."""
    return sum(per_step_cocycle(P, pi, path[k], path[k + 1])
               for k in range(len(path) - 1))


# ===========================================================================
head("PART 1.  TRAJECTORY entropy production = SUM of per-step cocycle increments")
# ===========================================================================
print("""
  Classical fact (Crooks PRE 60 2721 (1999); Maes JSP 95 367 (1999);
  Schnakenberg RMP 48 571 (1976); instantiated in paper10 T1/T2, paper4 s34):
  for an ordered transport P(y|x) with stationary pi, the entropy production of
  a TRAJECTORY omega = x_0 -> x_1 -> ... -> x_n is the path log-likelihood ratio

      A[omega] = log( dP_fwd[omega] / dP_rev[omega] ),

  and because the path measure FACTORIZES over the steps (the order is a genuine
  ordered/Markov transport), the log telescopes into a SUM of per-step exchange-
  cocycle increments

      A[omega] = sum_{k=0}^{n-1} a(x_k, x_{k+1}),
      a(x,y) = log[ pi(x) P(y|x) / ( pi(y) P(x|y) ) ].

  This sum is the SEQUENTIAL (concatenation-along-the-path) structure: each step
  contributes its own increment, and consecutive steps' increments ADD.  This is
  the odometer at the trajectory level, before any expectation is taken.
""")

P, pi, n = build_chain()
line("stationary pi (record-label law)",
     "[" + ", ".join(mp.nstr(p, 18) for p in pi) + "]")
# check pi P = pi
piP = [sum(pi[x] * P[x][y] for x in range(n)) for y in range(n)]
stat_resid = max(abs(piP[y] - pi[y]) for y in range(n))
line("stationarity residual max|pi P - pi|", mp.nstr(stat_resid, 6))

# per-step sigma and detailed-balance check
sigma_step = per_step_sigma(P, pi, n)
line("per-step sigma_step = E_fwd[a] = D(P_AB||P_BA)", mp.nstr(sigma_step, 30),
     "(>0: DRIVEN, arrow present)")

# verify trajectory A telescopes: take a concrete 6-step path and split it
path = [0, 1, 2, 0, 1, 2, 0]            # a 6-edge commit-order trajectory
A_full = path_entropy_production(P, pi, path)
# split the SAME path into seg1 (first 3 edges) and seg2 (last 3 edges)
cut = 3
seg1 = path[:cut + 1]                    # edges 0..2  (x0..x3)
seg2 = path[cut:]                        # edges 3..5  (x3..x6)
A_seg1 = path_entropy_production(P, pi, seg1)
A_seg2 = path_entropy_production(P, pi, seg2)
telescope_gap = A_full - (A_seg1 + A_seg2)
print()
line("A[full 6-edge path]", mp.nstr(A_full, 30))
line("A[seg1 (edges 0-2)]", mp.nstr(A_seg1, 30))
line("A[seg2 (edges 3-5)]", mp.nstr(A_seg2, 30))
line("CONCATENATION GAP  A_full - (A_seg1+A_seg2)", mp.nstr(telescope_gap, 6),
     "(=0: trajectory entropy production CONCATENATES additively)")
assert abs(telescope_gap) < mp.mpf("1e-100")


# ===========================================================================
head("PART 2.  EXPECTED arrow sigma accumulates ADDITIVELY over the commit order")
# ===========================================================================
print("""
  Taking expectations of PART 1's path-sum: along a STATIONARY commit order, the
  expected trajectory entropy production over n consecutive steps is

      Sigma(n) = E[ A[omega over n steps] ] = sum_{k} E[a_k] = n * sigma_step,

  because expectation is linear and every step is stationary.  Hence over the
  commit order

      Sigma(n1 + n2) = Sigma(n1) + Sigma(n2)          (SEQUENTIAL additivity),

  i.e. chi := accumulated sigma is a CONCATENATION-additive ODOMETER.  We verify
  the segment additivity directly (and note it needs NO detailed balance -- it
  holds for the driven sigma>0 chain, so it is NOT a reversibility artifact).
""")

# Sigma(n) by direct expectation over the stationary n-step chain.
def Sigma_expected(P, pi, n_states, nsteps):
    """E[A over nsteps] summed over all stationary trajectories of length nsteps."""
    # enumerate all length-nsteps paths weighted by pi(x0) prod P
    total = mp.mpf(0)
    # iterative: maintain distribution over current state of being at x with
    # accumulated weight; but we need E[A] = sum over paths weight*A.
    # Use linearity: E[A] = sum over edges-position of E[a at that edge] = nsteps*sigma_step
    # for stationary start.  We ALSO brute-force enumerate to confirm independence
    # of the start distribution choice (here stationary).
    import itertools
    for path in itertools.product(range(n_states), repeat=nsteps + 1):
        w = pi[path[0]]
        for k in range(nsteps):
            w *= P[path[k]][path[k + 1]]
        if w == 0:
            continue
        total += w * sum(per_step_cocycle(P, pi, path[k], path[k + 1])
                         for k in range(nsteps))
    return total

S1 = Sigma_expected(P, pi, n, 1)
S2 = Sigma_expected(P, pi, n, 2)
S3 = Sigma_expected(P, pi, n, 3)
S5 = Sigma_expected(P, pi, n, 5)
line("Sigma(1) (brute-force expectation)", mp.nstr(S1, 30))
line("Sigma(2)", mp.nstr(S2, 30))
line("Sigma(3)", mp.nstr(S3, 30))
line("Sigma(5)", mp.nstr(S5, 30))
print()
line("Sigma(1) = sigma_step ?  gap", mp.nstr(S1 - sigma_step, 6))
line("Sigma(2) = 2 sigma_step ?  gap", mp.nstr(S2 - 2 * sigma_step, 6))
line("Sigma(2+3)=Sigma(2)+Sigma(3) ?  gap", mp.nstr(S5 - (S2 + S3), 6),
     "(SEQUENTIAL additivity of accumulated arrow)")
line("linear-in-n:  Sigma(5) - 5 sigma_step", mp.nstr(S5 - 5 * sigma_step, 6))
assert abs(S5 - (S2 + S3)) < mp.mpf("1e-100")
assert abs(S5 - 5 * sigma_step) < mp.mpf("1e-100")

# Arrow-positivity: each increment d_chi = sigma_step >= 0 (paper10 T2).
line("d_chi = sigma_step >= 0  (Arrow-Positivity, paper10 T2)",
     sigma_step > 0, "(non-negative odometer increment)")

print("""
  HONESTY refinement (the two levels of additivity, kept distinct):
   * TRAJECTORY (sample-path) level:  A[seg1->seg2] = A[seg1] + A[seg2] is
     UNCONDITIONAL -- it is just log(product of step ratios) = sum of logs; it
     holds for ANY start, stationary or not (PART 1's gap 1e-120 is start-free).
     This is the odometer s3.2 actually invokes (chi is the accumulated content
     ALONG a realized commit order, a sample-path quantity).
   * EXPECTED-per-step UNIFORMITY  Sigma(n) = n*sigma_step needs STATIONARITY
     (else the per-step expectation drifts as the chain relaxes).  s3.2 does NOT
     need this stronger clause -- it needs concatenation additivity, which is the
     trajectory-level statement.  We flag the distinction so the 'FORCED' claim is
     not overstated: additivity = forced unconditionally; the constant per-step
     RATE is a stationary-regime refinement, not required for the odometer.
""")
# verify sigma_step IS the joint one-step KL D(P_AB||P_BA), not merely E[A_D]
DAB_joint = mp.mpf(0)
for x in range(n):
    for y in range(n):
        pab = pi[x] * P[x][y]
        pba = pi[y] * P[y][x]
        DAB_joint += pab * mp.log(pab / pba)
line("sigma_step == D(P_AB||P_BA) joint KL ?  gap",
     mp.nstr(DAB_joint - sigma_step, 6), "(paper10 T2 identity, exact)")
assert abs(DAB_joint - sigma_step) < mp.mpf("1e-100")


# ===========================================================================
head("PART 3.  PARALLEL/TENSOR  vs  SEQUENTIAL/ODOMETER  -- distinct compositions")
# ===========================================================================
print("""
  Two DIFFERENT additive composition laws live on the same cocycle.  We compute
  both gaps on explicit numbers to show they are structurally distinct (different
  ways of putting two diamonds together) that happen to share 'additive'.

  (P) PARALLEL / TENSOR  (paper4 s34):  two INDEPENDENT diamonds D1, D2; the joint
      law is the PRODUCT law P_{D1xD2} = P_{D1} (x) P_{D2}; the cocycle of the
      product is the SUM because log of a product is a sum of logs:
          A_{D1 x D2}(x1,x2 ; y1,y2) = a1(x1,y1) + a2(x2,y2).
      Composition = SIDE BY SIDE (tensor product of two separate records).

  (S) SEQUENTIAL / ODOMETER:  ONE chain, two CONSECUTIVE stretches seg1, seg2 of
      the SAME commit order; the accumulated arrow over the concatenation is the
      sum because the trajectory entropy production telescopes (PART 1):
          chi(seg1 -> seg2) = chi(seg1) + chi(seg2).
      Composition = NOSE TO TAIL (concatenation along the order).
""")

# (P) PARALLEL: build a second independent chain D2 and form the product cocycle.
def build_chain2():
    P2 = [[mp.mpf('0.25'), mp.mpf('0.65'), mp.mpf('0.10')],
          [mp.mpf('0.55'), mp.mpf('0.15'), mp.mpf('0.30')],
          [mp.mpf('0.20'), mp.mpf('0.50'), mp.mpf('0.30')]]
    nn = 3
    A = mp.matrix(nn, nn)
    for j in range(nn):
        for i in range(nn):
            A[j, i] = (1 if i == j else 0) - P2[i][j]
    for i in range(nn):
        A[nn - 1, i] = mp.mpf(1)
    b = mp.matrix(nn, 1); b[nn - 1] = mp.mpf(1)
    pic = mp.lu_solve(A, b)
    return P2, [pic[i] for i in range(nn)], nn

P2, pi2, n2 = build_chain2()
# product-diamond one-step entropy production = sigma_step(D1) + sigma_step(D2)
sigma2_step = per_step_sigma(P2, pi2, n2)
# joint product chain: states (x1,x2), transition P((y1,y2)|(x1,x2)) = P1*P2,
# stationary pi1 (x) pi2.  Its per-step sigma:
sigma_prod = mp.mpf(0)
for x1 in range(n):
    for x2 in range(n2):
        for y1 in range(n):
            for y2 in range(n2):
                joint = (pi[x1] * pi2[x2]) * (P[x1][y1] * P2[x2][y2])
                a_prod = per_step_cocycle(P, pi, x1, y1) + per_step_cocycle(P2, pi2, x2, y2)
                sigma_prod += joint * a_prod
parallel_gap = sigma_prod - (sigma_step + sigma2_step)
line("(P) sigma(D1)", mp.nstr(sigma_step, 24))
line("(P) sigma(D2)", mp.nstr(sigma2_step, 24))
line("(P) sigma(D1 x D2)  [product/tensor]", mp.nstr(sigma_prod, 24))
line("(P) PARALLEL GAP  sigma_prod-(s1+s2)", mp.nstr(parallel_gap, 6),
     "(=0: tensor cocycle additive, paper4 s34)")
assert abs(parallel_gap) < mp.mpf("1e-100")

print()
# (S) SEQUENTIAL was PART 1/2; restate the gap here side by side.
line("(S) chi(seg1)", mp.nstr(A_seg1, 24))
line("(S) chi(seg2)", mp.nstr(A_seg2, 24))
line("(S) chi(seg1 -> seg2)  [concatenation]", mp.nstr(A_full, 24))
line("(S) SEQUENTIAL GAP  chi_concat-(c1+c2)", mp.nstr(telescope_gap, 6),
     "(=0: trajectory entropy production telescopes)")

print("""
  BOTH gaps are 0, but the COMPOSITIONS differ:
    (P) acts on a PRODUCT state space  (x1,x2)   -- two records side by side;
    (S) acts on a CONCATENATED order   x0..xn    -- one record, end to end.
  The parallel law is 'independence => logs add'; the sequential law is
  'Markov path factorizes => the trajectory cocycle telescopes'.  The hostile
  review was RIGHT that they are different; the point of this receipt is that the
  SEQUENTIAL one is the one s3.2's Cauchy equation needs, and it is supplied --
  not by the tensor cocycle -- but by the path-additivity of entropy production.
""")


# ===========================================================================
head("PART 4.  Is the SEQUENTIAL odometer a THEOREM?  (arrow-positivity + cochain)")
# ===========================================================================
print("""
  Two clauses must hold for the s3.2 odometer:
    (i)  CONCATENATION additivity:  chi(seg1->seg2) = chi(seg1)+chi(seg2);
    (ii) NON-NEGATIVE increment:    d_chi >= 0.

  (i) is PART 1's telescoping of the trajectory entropy production -- a theorem
      GIVEN chi := accumulated sigma and an ordered (Markov-presentable) commit
      transport.  (ii) is exactly Arrow-Positivity (paper10 T2): each increment
      d_chi = d_sigma = D(P_AB||P_BA)_step >= 0, with equality iff detailed
      balance (an eventless, arrow-less step -- which by paper10 T3 is NOT a seal).
""")

# (ii) arrow-positivity floor: scan a 1-parameter family from reversible (eps=0)
# to driven (eps>0); sigma_step and the increment go from 0 up, never negative.
print("  -- arrow-positivity floor: sigma_step >= 0 along reversible->driven family --")
def driven_family(eps):
    # symmetric base (detailed balance) tilted by eps toward a cycle current
    base = mp.mpf('1') / 3
    P = [[base, base + eps, base - eps],
         [base - eps, base, base + eps],
         [base + eps, base - eps, base]]
    A = mp.matrix(3, 3)
    for j in range(3):
        for i in range(3):
            A[j, i] = (1 if i == j else 0) - P[i][j]
    for i in range(3):
        A[2, i] = mp.mpf(1)
    b = mp.matrix(3, 1); b[2] = mp.mpf(1)
    pic = mp.lu_solve(A, b)
    return P, [pic[i] for i in range(3)], 3

for eps in [mp.mpf('0'), mp.mpf('0.05'), mp.mpf('0.10'), mp.mpf('0.20'), mp.mpf('0.30')]:
    Pe, pie, ne = driven_family(eps)
    se = per_step_sigma(Pe, pie, ne)
    tag = " <- detailed balance (eventless: NOT a seal, paper10 T3)" if eps == 0 else ""
    line(f"   eps={float(eps):.2f}:  sigma_step = d_chi", mp.nstr(se, 18),
         (">=0" if se >= -mp.mpf('1e-100') else "NEGATIVE!") + tag)
    assert se >= -mp.mpf("1e-100")

print("""
  (iii) THE HOLONOMY-COCHAIN TELESCOPE (paper4 s44).  For a chain of sealed
  diamonds with oriented interface cochains h_0,...,h_N, the local source is
  rho_i = h_{i+1} - h_i, and the chain accumulation telescopes EXACTLY:
      sum_{i=a}^{b-1} rho_i = h_b - h_a.
  This is the SAME concatenation-additive structure: the cochain increments
  accumulate end-to-end along the chain of diamonds.  We verify the telescope.
""")
# paper4 s45 decisive numbers
h = [mp.mpf('0.15'), mp.mpf('0.72'), mp.mpf('-0.08'), mp.mpf('0.46'), mp.mpf('0.91')]
rho = [h[i + 1] - h[i] for i in range(len(h) - 1)]
# telescope over an arbitrary sub-block [a,b)
a_idx, b_idx = 1, 4
telescope = sum(rho[i] for i in range(a_idx, b_idx))
exact = h[b_idx] - h[a_idx]
line("h (interface cochain, paper4 s45)",
     "[" + ", ".join(mp.nstr(x, 4) for x in h) + "]")
line("rho_i = h_{i+1}-h_i",
     "[" + ", ".join(mp.nstr(x, 4) for x in rho) + "]")
line(f"sum_{{i={a_idx}}}^{{{b_idx-1}}} rho_i", mp.nstr(telescope, 18))
line(f"h_{b_idx} - h_{a_idx}", mp.nstr(exact, 18))
line("TELESCOPE GAP", mp.nstr(telescope - exact, 6),
     "(=0: cochain accumulation is concatenation-additive)")
assert abs(telescope - exact) < mp.mpf("1e-100")

print("""
  So the cochain ledger ALREADY carries a concatenation-additive accumulation
  (s44's telescope).  The arrow chi = accumulated D(P_AB||P_BA) is the SAME kind
  of object: a chain sum of per-diamond increments along the commit order.
""")


# ===========================================================================
head("PART 5.  HONEST VERDICT  --  is the sequential odometer FORCED or ASSUMED?")
# ===========================================================================
print("""
  Decompose s3.2's named premise 'sequential content-additivity' into its two
  clauses and rate each HONESTLY.

  CLAUSE (i)  CONCATENATION ADDITIVITY  chi(seg1->seg2)=chi(seg1)+chi(seg2).
    STATUS: FORCED (UNCONDITIONALLY at the trajectory level), once chi :=
            accumulated entropy production.
    WHY:  trajectory entropy production is the path log-likelihood ratio
          A[omega]=log dP_fwd/dP_rev, and for an ordered transport the path
          measure factorizes, so A telescopes into a SUM of per-step cocycle
          increments (PART 1, gap 1e-120).  Sums concatenate additively by
          construction, for ANY start (stationary or not): the sample-path
          odometer is start-free.  Taking expectations preserves additivity
          (PART 2): Sigma(n1+n2)=Sigma(n1)+Sigma(n2) (gaps 1e-120), with NO
          detailed-balance assumption (holds for driven sigma>0).  [The STRONGER
          clause Sigma(n)=n*sigma_step -- a CONSTANT per-step rate -- needs
          stationarity, but s3.2 does NOT need it; it needs concatenation
          additivity, the trajectory statement, which is unconditional.]  This is
          NOT the parallel/tensor cocycle (PART 3): it is the path-telescoping of
          entropy production, the SEQUENTIAL composition s3.2 actually needs.
          The cochain ledger carries the identical telescope (PART 4(iii)).

  CLAUSE (ii)  NON-NEGATIVE INCREMENT  d_chi >= 0.
    STATUS: FORCED, by Arrow-Positivity (paper10 T2).
    WHY:  d_chi = d_sigma = D(P_AB||P_BA)_step >= 0 exactly, with equality iff
          detailed balance -- and a detailed-balance (eventless, arrow-less) step
          is by paper10 T3 NOT a seal.  So every genuine seal step contributes a
          strictly-positive increment, and chi is a monotone non-decreasing
          ODOMETER.  (PART 4 family: sigma_step>=0 on reversible->driven, =0 only
          at the eventless point.)

  THE ONE REMAINING ASSUMPTION (where the honesty lives):
    The identification  chi := accumulated entropy production sigma = D(P_AB||P_BA).
    Paper 1 v7 s2 ALREADY ADOPTS THIS ('the only state variable available pre-
    geometrically is chi = D(P_AB||P_BA)', and 'the arrow/entropy-production
    functional').  GIVEN that identification (which is a DEFINITION the corpus
    has already made, not a new premise), BOTH clauses of the odometer follow as
    theorems.  The only further structural requirement is that the commit order
    be a genuine ORDERED transport (Markov-presentable at the collar) so the path
    measure factorizes -- which is precisely paper10's standing arena (the
    eventless collar is a finite primitive Markov presentation, T4) and the
    Barandes link (events break Markovianity, BETWEEN events the collar is
    ordered/Markov: paper10 s2.6).

  CONSEQUENCE for s5.1 and s3.2:
    The 'sequential content-additivity (an odometer)' that s3.2 lists as a
    SEPARATE, ASSUMED premise -- distinct from the parallel/tensor cocycle -- is
    NOT an independent assumption.  It is FORCED by:
      * the corpus definition chi := accumulated sigma (paper10 T2; s2 of Paper 1),
      * the path-additivity (telescoping) of trajectory entropy production,
      * Arrow-Positivity for the d_chi>=0 clause (paper10 T2),
      * the same telescope the holonomy cochain already obeys (paper4 s44).
    This CLOSES the ADDITIVITY half of s5.1: the odometer is a theorem of the
    record/arrow structure, not a named premise.  Paper 1 s3.2 had TWO named
    premises (sequential additivity; dense-vs-sparse/divisible).  The first is
    DISCHARGED.  What remains genuinely open in s5.1 is ONLY the dense-vs-sparse
    (divisible-vs-indivisible) question -- the density of seals (s5.3) -- which is
    untouched by this result.

  CAVEAT (kept explicit, single-threaded honesty):
    'FORCED' here is conditional on chi being accumulated entropy production and
    on the commit order being an ordered (Markov-presentable) transport.  These
    are the corpus' OWN standing commitments (paper10's arena, Paper 1 s2's
    definition), so within Paper 1's framework the odometer is a theorem; it is
    NOT forced from outside those commitments.  The residual s5.1 obligation 'does
    the closed-holonomy ledger intrinsically SUPPLY the increment d_chi' (i.e.
    GENERATE its magnitude per diamond) is a DIFFERENT question -- the SIZE of the
    increment and its conversion kappa -- and is NOT what this receipt closes.
    This receipt closes the STRUCTURE (additivity + sign), not the MAGNITUDE.
""")


# ===========================================================================
head("CANONICAL OUTPUT BLOCK  (F3c sequential-odometer receipt)")
# ===========================================================================
print(f"""
  driven record chain (pre-geometric kinematics, dps=120):
    stationarity residual              = {mp.nstr(stat_resid, 4)}
    per-step sigma_step (= d_chi)      = {mp.nstr(sigma_step, 25)}  (>0: arrow present)

  PART 1  trajectory entropy production telescopes (SEQUENTIAL):
    A_full - (A_seg1 + A_seg2)         = {mp.nstr(telescope_gap, 4)}   (concatenation-additive)

  PART 2  accumulated arrow is additive over the commit order:
    Sigma(2+3) - (Sigma(2)+Sigma(3))   = {mp.nstr(S5 - (S2 + S3), 4)}
    Sigma(5)  - 5*sigma_step           = {mp.nstr(S5 - 5 * sigma_step, 4)}   (linear in commit steps)

  PART 3  PARALLEL vs SEQUENTIAL are DISTINCT additive laws (both gap 0):
    parallel/tensor   sigma_prod-(s1+s2)= {mp.nstr(parallel_gap, 4)}   (side-by-side, paper4 s34)
    sequential/odom   chi_concat-(c1+c2)= {mp.nstr(telescope_gap, 4)}   (nose-to-tail, this work)

  PART 4  arrow-positivity + cochain telescope:
    sigma_step >= 0 on reversible->driven family   : TRUE (=0 only at eventless/non-seal)
    cochain telescope sum rho_i - (h_b - h_a)       = {mp.nstr(telescope - exact, 4)}

  VERDICT:
    (i)  concatenation additivity  : FORCED (path entropy production telescopes)
    (ii) non-negative increment    : FORCED (Arrow-Positivity, paper10 T2)
    one remaining identification   : chi := accumulated sigma (corpus DEFINITION,
                                     already adopted in Paper 1 s2)
    => the SEQUENTIAL content-ODOMETER is a THEOREM of the record/arrow structure,
       NOT a separate assumption.  This DISCHARGES the additivity half of s5.1 and
       removes one of Paper 1 s3.2's two named premises.  The remaining open s5.1
       item is the MAGNITUDE/SUPPLY of d_chi and the dense-vs-sparse question -- not
       the additivity, which is now closed.

  Pre-geometric throughout: every number is a record-internal probability / KL /
  log-likelihood-ratio.  No spacetime, metric, light cone, or s^2 was used.
""")

head("DONE.")
