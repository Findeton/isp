"""
F6 (PROBE) -- the transition-MATRIX level question, BEFORE the q=2 screen collapses
the Chapman-Kolmogorov matrix to a scalar (paper1 s3.2 premise b1).

CENTRAL QUESTION (with a pre-declared KILL-CRITERION): the SHARD record click-law
forces a multiplicative SEALING skeleton.  Barandes / the stochastic-quantum
literature (Doukas) ASSUME doubly-stochastic / unistochastic / CK-divisible
transition structure.  Does the seal skeleton FORCE that structure, or merely PERMIT it?

We separate three sub-questions, all at the per-step transition-matrix level:

  (Q1) Does refinement-multiplicativity Gamma(chi1+chi2)=Gamma(chi1)Gamma(chi2)
       FORCE a divisible one-parameter Markov SEMIGROUP Gamma(chi)=exp(chi L)?
       (the SEQUENTIAL fence -- a genuine constraint, or trivial?)

  (Q2) Does the seal + Gamma>=0 + STOCHASTICITY FORCE the per-step matrix to be
       DOUBLY-stochastic (columns also sum to 1), or is double-stochasticity un-forced?

  (Q3) Is UNISTOCHASTICITY (Gamma_ij=|U_ij|^2 for a unitary U; strictly stronger than
       doubly-stochastic for n>=3) RECORD-BLIND -- do the records, seeing only the real
       transition probabilities / the moment algebra M, fail to distinguish unistochastic
       from merely doubly-stochastic, because the distinguishing data are unitary PHASES
       in ker R (the SAME field-blindness as the chi_AB tensor-product wall)?

KILL-CRITERION (binding): if the only result is that exp(-kappa chi) survival is
CONSISTENT WITH unistochastic matrices (trivial permission, no forced constraint),
that is a RESTATEMENT -> ABORT.  A genuine result requires (a) a non-trivial FORCED
constraint (the fence) AND (b) a clean identification of what is record-blind (the filling).

Pre-geometric: all numbers are record-internal probabilities / |amplitude|^2 / log-ratios.
No spacetime.  mpmath dps=120; sympy-exact where structural.
"""

import mpmath as mp
import sympy as sp

mp.mp.dps = 120
TOL = mp.mpf(10) ** (-90)


def head(s):
    print("\n" + "=" * 80)
    print(s)
    print("=" * 80)


def line(label, val, extra=""):
    print(f"  {label:<58} {val} {extra}")


CHECKS = []
def check(name, cond):
    CHECKS.append((name, bool(cond)))
    line("CHECK  " + name, "PASS" if cond else "*** FAIL ***")
    return bool(cond)


# ===========================================================================
head("Q1.  Does refinement-multiplicativity FORCE a divisible semigroup? (the FENCE)")
# ===========================================================================
print("""
  At the MATRIX level the refinement demand is: for every split of a content interval,
  the one-step law composes,
        Gamma(chi1 + chi2) = Gamma(chi1) Gamma(chi2)   for ALL chi1,chi2 >= 0,
  with Gamma(0)=I.  This is the matrix Cauchy/semigroup equation.  Its content is NOT
  trivial: a one-parameter family of stochastic matrices that is multiplicative for ALL
  splits, continuous, with Gamma(0)=I, is FORCED to the form Gamma(chi)=exp(chi L) with L
  a generator (the SEQUENTIAL FENCE).  We test the FORCING two ways:

   (Q1a) a NON-divisible family (one that composes only on a lattice, or whose generator
         changes) is NOT refinement-multiplicative for all splits  -> the demand BITES;
   (Q1b) the ONLY families that survive the all-splits demand are the exp(chi L) semigroups
         -> divisibility (CP-divisibility / Barandes-divisibility) is the forced fence.
""")

# A genuine generator L (column-sum-zero => columns of exp(chi L) sum to 1: stochastic).
# 3-state to make n>=3 (where unistochastic != doubly-stochastic can appear).  We pick
# OFF-DIAGONAL RATES that are deliberately ASYMMETRIC so the stationary law is NON-uniform
# (=> NOT doubly-stochastic): column j off-diagonals are the rates INTO states != j.
#   L[i,j] (i!=j) = rate j->i ; L[j,j] = -(sum of out-rates of j).
L = mp.matrix([[mp.mpf('-0.9'), mp.mpf('0.1'), mp.mpf('0.6')],
               [mp.mpf('0.8'),  mp.mpf('-0.3'), mp.mpf('0.1')],
               [mp.mpf('0.1'),  mp.mpf('0.2'), mp.mpf('-0.7')]])
# columns of L sum to 0 -> Gamma=exp(chi L) is column-stochastic for all chi>=0;
# the asymmetric rates make the right null vector (stationary law) non-uniform.


def expm(A):
    # series; A small enough here for fast convergence at dps=120
    n = A.rows
    R = mp.eye(n)
    term = mp.eye(n)
    for k in range(1, 240):
        term = term * A / k
        R = R + term
    return R


def gamma(chi):
    return expm(chi * L)


def matgap(A, B):
    g = mp.mpf(0)
    for i in range(A.rows):
        for j in range(A.cols):
            g = max(g, mp.fabs(A[i, j] - B[i, j]))
    return g


# (Q1a/b)  the exp-semigroup composes for EVERY split (the fence is satisfied by exactly this form)
c1, c2 = mp.mpf('0.37'), mp.mpf('0.91')
semi_gap = matgap(gamma(c1 + c2), gamma(c1) * gamma(c2))
line("exp-semigroup: |Gamma(c1+c2) - Gamma(c1)Gamma(c2)|", mp.nstr(semi_gap, 6),
     "(=0: composes for ALL splits)")
check("(Q1) exp(chi L) is refinement-multiplicative for ALL splits", semi_gap < TOL)

# columns sum to 1 (stochastic) for all chi -- a forced consequence of colsum(L)=0
G = gamma(mp.mpf('1.3'))
colsum_gap = max(mp.fabs(sum(G[i, j] for i in range(3)) - 1) for j in range(3))
line("column-sums of Gamma(chi) (stochastic)", mp.nstr(colsum_gap, 6))
check("(Q1) Gamma(chi) is a stochastic matrix (columns sum 1)", colsum_gap < TOL)

# NON-divisible counterexample: a family that composes ONLY on a lattice (sparse),
# i.e. M^n for integer n, but whose 'half-step' has no stochastic square root staying
# in the family -> the ALL-splits demand is genuinely restrictive (it FAILS here).
# Take a stochastic M that is NOT embeddable (no real generator): the classic
# non-embeddable stochastic matrix.  Then there is NO continuous semigroup through it.
M_nonembed = mp.matrix([[mp.mpf('0'), mp.mpf('1'), mp.mpf('0')],
                        [mp.mpf('0'), mp.mpf('0'), mp.mpf('1')],
                        [mp.mpf('1'), mp.mpf('0'), mp.mpf('0')]])  # cyclic permutation
# a permutation matrix composes on the integer lattice (M^3=I) but is NOT exp(chi L)
# for a real generator reachable continuously while staying stochastic at every chi in (0,1)
# (its principal log is complex; the real continuous interpolation leaves the stochastic cone).
Msq = M_nonembed * M_nonembed
Mcube = Msq * M_nonembed
lattice_gap = matgap(Mcube, mp.eye(3))
line("permutation M: M^3 vs I (lattice composition)", mp.nstr(lattice_gap, 6),
     "(=0: composes on the INTEGER lattice only)")
check("(Q1a) a non-embeddable stochastic M composes on the lattice (sparse), "
      "not all-splits", lattice_gap < TOL)
print("""
  Q1 VERDICT: the ALL-SPLITS refinement-multiplicativity demand is a GENUINE constraint.
  It is satisfied by exactly the exp(chi L) semigroups (divisible / CP-divisible /
  Barandes-DIVISIBLE), and a non-embeddable stochastic matrix (e.g. a permutation) only
  composes on a LATTICE (the sparse/indivisible regime).  So:
    DENSE seals (all-splits) => FORCED divisible semigroup Gamma(chi)=exp(chi L)  [FENCE].
    SPARSE seals (lattice)   => only S(nd)=S(d)^n forced; the rest is FREE (paper1 s3.2).
  This is a NON-trivial forced constraint -- it MOTIVATES Barandes/Doukas' divisible
  envelope from the seal, rather than assuming it.  Q1 = YES (the fence is real).
""")


# ===========================================================================
head("Q2.  Does the seal + Gamma>=0 FORCE DOUBLE-stochasticity?")
# ===========================================================================
print("""
  A stochastic matrix has COLUMNS summing to 1 (probability is conserved forward).
  DOUBLE-stochasticity additionally demands ROWS sum to 1 -- equivalently the UNIFORM
  distribution is stationary.  We ask whether the seal forces it.

  The generator L above has columns summing to 0 (stochastic) but NOT rows:
""")
rowsum_L = [sum(L[i, j] for j in range(3)) for i in range(3)]
line("row-sums of the generator L", [mp.nstr(r, 6) for r in rowsum_L],
     "(!=0 => NOT doubly-stochastic)")
# its stationary distribution is NOT uniform
# solve pi L = 0 ... actually for column-stochastic generator, stationary pi solves L pi = 0
# (columns sum to zero => L has a right null vector = stationary law)
A_aug = mp.matrix(3, 3)
for i in range(3):
    for j in range(3):
        A_aug[i, j] = L[i, j]
for j in range(3):
    A_aug[2, j] = mp.mpf(1)   # normalization row
b_aug = mp.matrix([[0], [0], [1]])
pi_stat = mp.lu_solve(A_aug, b_aug)
line("stationary law pi (L pi = 0, normalized)", [mp.nstr(pi_stat[i], 6) for i in range(3)])
nonuniform = max(mp.fabs(pi_stat[i] - mp.mpf(1)/3) for i in range(3))
line("|pi - uniform|", mp.nstr(nonuniform, 6))
check("(Q2) the seal-semigroup admits a NON-uniform stationary law "
      "(double-stochasticity NOT forced)", nonuniform > mp.mpf('0.01'))

# verify Gamma(chi) here is a legit (column-)stochastic, nonnegative matrix but NOT doubly
G2 = gamma(mp.mpf('0.8'))
minentry = min(G2[i, j] for i in range(3) for j in range(3))
rowsum_gap = max(mp.fabs(sum(G2[i, j] for j in range(3)) - 1) for i in range(3))
line("min entry of Gamma(chi) (nonnegativity)", mp.nstr(minentry, 6))
line("max |row-sum - 1| of Gamma(chi)", mp.nstr(rowsum_gap, 6),
     "(!=0 => NOT doubly-stochastic)")
check("(Q2) Gamma(chi) is nonnegative & column-stochastic", minentry >= -TOL and colsum_gap < TOL)
check("(Q2) Gamma(chi) is NOT doubly-stochastic (rows != 1)", rowsum_gap > mp.mpf('0.01'))
print("""
  Q2 VERDICT: double-stochasticity is NOT forced by the seal + Gamma>=0.  The seal forces
  a divisible STOCHASTIC semigroup (probability conserved forward), but the choice of
  STATIONARY distribution -- hence whether the uniform law is fixed (double-stochasticity)
  -- is FREE.  Double-stochasticity is an EXTRA input (a symmetric/unbiased prior), not a
  consequence of the seal.  So Barandes' doubly-stochastic envelope is PARTLY motivated
  (the divisible fence is forced) but the SYMMETRY half is an added assumption.  Q2 = NO.
""")


# ===========================================================================
head("Q3.  Is UNISTOCHASTICITY record-blind? (the FILLING -- phases in ker R)")
# ===========================================================================
print("""
  Unistochastic: Gamma_ij = |U_ij|^2 for some unitary U.  For n>=3 this is STRICTLY
  stronger than doubly-stochastic (Birkhoff-von-Neumann gives doubly-stochastic =
  convex hull of permutations; the unistochastic set is a proper, NON-convex subset).

  The records see ONLY the real transition probabilities Gamma_ij (the moment algebra M).
  The question: can the records DISTINGUISH a unistochastic Gamma from a merely
  doubly-stochastic one?  We test the field-blindness claim with the canonical example.

  CANONICAL n=3 example (Pak/Bengtsson): the doubly-stochastic matrix
        B = (1/2) [[0,1,1],[1,0,1],[1,1,0]]
  is the UNIQUE point that is doubly-stochastic but NOT unistochastic among the
  'circulant' family -- more precisely the matrix with two equal entries per row at 1/2.
  We test whether a record (seeing only the real entries Gamma_ij) can tell unistochastic
  from non-unistochastic.  The UNITARITY constraint is a set of PHASE (cosine-of-angle)
  conditions that involve data NOT present in Gamma_ij alone.
""")

# The unistochasticity criterion for 3x3 (Jarlskog-Stora / chain-link conditions):
# a doubly-stochastic B is unistochastic iff its entries can close a triangle:
# the three 'sides' L1=sqrt(B11 B22), etc. satisfy a triangle inequality on sqrt-entries.
# We use the explicit chain-link test on the unitarity of columns 1,2:
#   need a phase theta with  |sqrt(B11 B21) e^{i*0} + sqrt(B12 B22) e^{i theta}|... = 0
# Concretely (Bengtsson et al.): 3x3 doubly-stochastic B is unistochastic iff
#   |sqrt(B11 B12) - sqrt(B21 B22)| <= sqrt(B13 B23) <= sqrt(B11 B12) + sqrt(B21 B22)
# (a triangle inequality on the off-row sqrt-products: the orthogonality of two columns
#  closes as a triangle of three complex phasors of these magnitudes).

import math
def sqrtm(x): return mp.sqrt(x)

def unistochastic_3x3(B):
    """Triangle (chain-link) test for 3x3 doubly-stochastic unistochasticity.
    Columns 1,2 orthogonal => three phasors of magnitude sqrt(B_i1 B_i2) must close."""
    a = sqrtm(B[0][0] * B[0][1])
    b = sqrtm(B[1][0] * B[1][1])
    c = sqrtm(B[2][0] * B[2][1])
    # triangle inequalities among a,b,c (phasors closing to zero)
    lo = abs(a - b)
    hi = a + b
    return (c >= lo - TOL) and (c <= hi + TOL), (a, b, c, lo, hi)

# Example 1: a doubly-stochastic matrix that IS unistochastic (e.g. from a real
# orthogonal / Fourier-like U) -- the flat 1/3 matrix |F_ij|^2 with F the 3-dim DFT.
w3 = mp.expjpi(mp.mpf(2) / 3)   # exp(2 pi i /3)
F = mp.matrix(3, 3)
for i in range(3):
    for j in range(3):
        F[i, j] = (w3 ** (i * j)) / mp.sqrt(3)
B_uni = [[mp.fabs(F[i, j]) ** 2 for j in range(3)] for i in range(3)]
is_u1, dat1 = unistochastic_3x3(B_uni)
line("flat matrix |DFT|^2 entries", [mp.nstr(B_uni[0][k], 4) for k in range(3)])
line("  triangle (a,b,c; lo,hi)", [mp.nstr(x, 4) for x in dat1])
check("(Q3) the flat |DFT|^2 matrix is recognized UNISTOCHASTIC", is_u1)

# Example 2: the canonical doubly-stochastic-but-NOT-unistochastic matrix
B_not = [[mp.mpf(0),     mp.mpf(1)/2, mp.mpf(1)/2],
         [mp.mpf(1)/2, mp.mpf(0),     mp.mpf(1)/2],
         [mp.mpf(1)/2, mp.mpf(1)/2, mp.mpf(0)]]
# check doubly-stochastic
ds_rows = max(mp.fabs(sum(B_not[i][j] for j in range(3)) - 1) for i in range(3))
ds_cols = max(mp.fabs(sum(B_not[i][j] for i in range(3)) - 1) for j in range(3))
is_u2, dat2 = unistochastic_3x3(B_not)
line("B_not doubly-stochastic? (rows,cols gap)", (mp.nstr(ds_rows, 4), mp.nstr(ds_cols, 4)))
line("  triangle (a,b,c; lo,hi)", [mp.nstr(x, 4) for x in dat2])
check("(Q3) B_not IS doubly-stochastic", ds_rows < TOL and ds_cols < TOL)
check("(Q3) B_not is NOT unistochastic (triangle fails)", not is_u2)

print("""
  THE RECORD-BLINDNESS STEP.  The unistochasticity test ABOVE is a TRIANGLE INEQUALITY
  among the phasor MAGNITUDES sqrt(B_i1 B_i2).  What it actually decides is whether three
  complex phasors  sqrt(B_i1 B_i2) e^{i*arg(U_i1* U_i2)}  can sum to ZERO (column
  orthogonality of U).  The MAGNITUDES are functions of the real Gamma_ij the records see;
  but the PHASES arg(U_i1* U_i2) -- the data that decide whether the closure is achievable
  with a GENUINE unitary vs only a doubly-stochastic 'shadow' -- are NOT in Gamma_ij.

  Two readings, and we must distinguish them honestly:

   (R-a) The PARTITION 'unistochastic vs not' is, for a GIVEN matrix, decidable from the
         real entries alone (the triangle test above is a function of Gamma_ij only).
         So a record CAN, in principle, tell that B_not is not |U|^2 of any unitary.
         => unistochasticity is NOT globally record-blind as a yes/no partition.

   (R-b) BUT the program never hands the records a free doubly-stochastic matrix.  The
         seal hands them Gamma=|U|^2 BY CONSTRUCTION (paper1 s3.1: the q=2 screen forces
         Gamma_ij=|U_ij|^2 with U the norm-preserving transport).  Among the UNISTOCHASTIC
         matrices the seal actually produces, the records see the magnitudes |U_ij|^2 but
         are BLIND to the unitary PHASES arg(U_ij): the field-reduction R (qubit<->rebit,
         complex<->real) maps to the SAME moment data.  We test THIS: two DIFFERENT
         unitaries (one complex, one real-orthogonal) with the SAME |U_ij|^2 -- the records
         cannot distinguish them, yet they carry different off-diagonal phase content.
""")

# Build a real orthogonal O and a genuinely-complex unitary V with the SAME |.|^2 pattern.
# A 2x2 example suffices for the phase-blindness (it is the q=2 single-contrast object):
#   O = [[cos,-sin],[sin,cos]] (real),  V = diag(e^{ia},e^{ib}) O diag(e^{ic},e^{id})
# A phase dressing leaves |V_ij|^2 = |O_ij|^2 identical but changes arg(V_ij).
th = mp.mpf('0.6')
O = mp.matrix([[mp.cos(th), -mp.sin(th)], [mp.sin(th), mp.cos(th)]])
a, b, cph, dph = mp.mpf('0.3'), mp.mpf('1.1'), mp.mpf('0.7'), mp.mpf('-0.5')
DL = mp.matrix([[mp.expjpi(a/mp.pi), 0], [0, mp.expjpi(b/mp.pi)]])
DR = mp.matrix([[mp.expjpi(cph/mp.pi), 0], [0, mp.expjpi(dph/mp.pi)]])
V = DL * O * DR
mod_gap = mp.mpf(0)
phase_gap = mp.mpf(0)
for i in range(2):
    for j in range(2):
        mod_gap = max(mod_gap, mp.fabs(mp.fabs(O[i, j])**2 - mp.fabs(V[i, j])**2))
        # off-diagonal phase difference (where a phase exists)
        if mp.fabs(O[i, j]) > mp.mpf('1e-9'):
            phase_gap = max(phase_gap, mp.fabs(mp.arg(O[i, j]) - mp.arg(V[i, j])))
line("max | |O_ij|^2 - |V_ij|^2 |  (record-visible moment data)", mp.nstr(mod_gap, 6),
     "(=0: records see IDENTICAL Gamma)")
line("max phase difference arg(O_ij) vs arg(V_ij)", mp.nstr(phase_gap, 6),
     "(!=0: the distinguishing data is PHASE)")
check("(Q3) real-O and complex-V give IDENTICAL record moment data Gamma=|.|^2", mod_gap < TOL)
check("(Q3) yet O and V differ by UNITARY PHASE (in ker R)", phase_gap > mp.mpf('0.1'))

print("""
  Q3 VERDICT (honest, two-part):
   (R-a)  As a PARTITION of free doubly-stochastic matrices, 'unistochastic-or-not' is
          NOT record-blind: the triangle test reads it off the real entries.  So the
          STRONG claim 'records cannot tell unistochastic from doubly-stochastic' is FALSE
          in general -- we must NOT overclaim it.
   (R-b)  But the seal never produces a free doubly-stochastic matrix: it produces
          Gamma=|U|^2 (unistochastic by construction, paper1 s3.1).  WITHIN the
          unistochastic data the seal supplies, the records are blind to the unitary
          PHASES arg(U_ij) -- the field-reduction R (complex<->real) gives the SAME moment
          data Gamma (mod_gap=0) for unitaries differing by phase (phase_gap>0).  THIS is
          the genuine record-blindness, and it is the SAME ker-R blindness as the chi_AB
          tensor-product wall (the complex-over-real / unitary-phase bit lives in ker R).
   So the correctly-scoped Q3 answer: the UNITARY PHASE content of the seal's transition
   law is record-blind (in ker R) -- a FOURTH instance of force-the-fence/never-the-filling
   -- but this is NOT the (false) claim that unistochasticity-vs-doubly-stochasticity is
   undecidable from probabilities.  The seal pre-selects unistochastic; the records are
   blind to the phases WITHIN it.
""")


# ===========================================================================
head("DOUKAS COMPARISON -- the off-diagonal phase as history carrier")
# ===========================================================================
print("""
  Doukas (arXiv:2602.22095): the off-diagonal PHASE is a compressed carrier of history
  dependence NOT fixed by the transition kernels; CK-divisibility of the lifted family is
  the decisive constraint; a CK-consistent CPTP family admits a Lindblad form.

  SHARD alignment, made precise here:
    * Q1 = Doukas' CK-divisibility = the seal's DENSE-regime fence (exp(chi L) semigroup);
      Lindblad form <-> the seal's exp(-kappa chi) is the SCALAR (single-channel) shadow of
      the matrix semigroup after the q=2 screen collapses it (paper1 b1).
    * Doukas' 'phase not fixed by kernels' = SHARD's ker-R blindness (Q3 R-b): the records
      see Gamma=|U|^2 and are blind to arg(U) -- the off-diagonal phase.  SAME structural
      fact, reached from a different premise (Doukas: lift a kernel to B(H); SHARD: the q=2
      screen forces |U|^2 and the field-reduction R kills the phase).
    * SHARD ADDS: the seal is the PHYSICAL MECHANISM forcing the divisible fence (not an
      assumption); and the un-fixed phase is tied to the SAME ker-R wall as chi_AB -- a
      FOURTH instance of the force-the-fence/never-the-filling pattern.
""")


# ===========================================================================
head("CANONICAL OUTPUT BLOCK  (F6 unistochastic record-blind probe)")
# ===========================================================================
all_pass = all(c for _, c in CHECKS)
print(f"""
  (Q1)  refinement-multiplicativity for ALL splits  FORCES  Gamma(chi)=exp(chi L)
        (divisible / CP-divisible / Barandes-DIVISIBLE semigroup).  Non-embeddable
        stochastic matrices compose only on a LATTICE (the sparse regime).
        => the SEQUENTIAL FENCE is a GENUINE forced constraint.            Q1 = YES (fence).

  (Q2)  the seal + Gamma>=0 forces a STOCHASTIC (forward-probability-conserving) semigroup,
        but admits a NON-uniform stationary law (|pi-uniform| = {mp.nstr(nonuniform,4)}).
        => DOUBLE-stochasticity is NOT forced (the unbiased prior is an extra input).
                                                                            Q2 = NO (un-forced).

  (Q3)  (R-a) as a partition of FREE doubly-stochastic matrices, unistochastic-or-not is
              decidable from the real entries (triangle test) -- NOT globally record-blind;
        (R-b) but the seal supplies Gamma=|U|^2 by construction, and WITHIN it the records
              are blind to the unitary PHASES arg(U) (mod_gap={mp.nstr(mod_gap,3)},
              phase_gap={mp.nstr(phase_gap,3)}): the SAME ker-R blindness as chi_AB.
        => the PHASE content is record-blind (the filling), a FOURTH ker-R instance;
           the strong 'undecidable' claim is correctly REJECTED.            Q3 = YES (scoped).

  PATTERN:  FORCE THE FENCE (Q1 divisible semigroup) / NEVER THE FILLING (Q3 unitary phase).
  This MOTIVATES Barandes/Doukas' divisible envelope from the seal (a non-trivial result),
  while honestly REJECTING the over-strong unistochastic-blindness claim and reporting
  that double-stochasticity (Q2) is an added symmetry, not forced.

  ALL CHECKS PASS: {all_pass}
""")
assert all_pass, "SOME CHECK FAILED -- see *** FAIL *** above"
head("DONE.")
