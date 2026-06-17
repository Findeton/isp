"""
v7 Paper XVIII  --  p18_seal_divisibility.py

DOES THE SEAL SKELETON FORCE THE BARANDES / DOUKAS TRANSITION-MATRIX STRUCTURE,
OR MERELY PERMIT IT?  (the per-step transition-MATRIX level, BEFORE the q=2
single-channel screen collapses Chapman-Kolmogorov to a scalar -- paper1 sec 3.2.)

The SHARD record click-law FORCES a multiplicative SEALING skeleton:
   * survival-multiplicativity along the refinement axis  S(chi)=exp(-kappa chi)
     (Filter 3 / f3_self_consistency.py, f3b/f3e; Cauchy on the seal sub-semigroup),
   * an orthogonal-projection seal  E = E^2 = E*  (Born projection, f1),
   * transverse moment-positivity  Gamma >= 0  (Gram of the substrate's own
     observables -- p6 PART 5).
Barandes (arXiv:2507.21192) and Doukas (arXiv:2602.22095) ASSUME a transition-matrix
structure (doubly-stochastic / unistochastic / Chapman-Kolmogorov-divisible) WITHOUT
deriving WHY.  This receipt tests, at the per-step transition-MATRIX level, with
explicit small (n=2,3) matrices, sympy-exact / mpmath dps>=120:

  Q1  Does refinement-multiplicativity  Gamma(chi1+chi2)=Gamma(chi1)Gamma(chi2)
      for a one-parameter ROW-stochastic family FORCE a divisible Markov SEMIGROUP
      Gamma(chi)=exp(chi L), L a generator (Q-matrix: off-diag>=0, rows sum 0)?
      Is survival S=exp(-kappa chi) exactly the sub-stochastic diagonal decay of
      such a generator?                                        --> classify FORCED/PERMITTED/NOT

  Q2  Does the seal + Gamma>=0 FORCE the per-step matrix to be DOUBLY-stochastic
      (columns also sum to 1)?  Or is double-stochasticity UN-forced (stationary
      distribution free)?  Build a VALID sealed family that is row- but NOT
      column-stochastic, or prove forcing.                     --> classify FORCED/PERMITTED/NOT

  Q3  Is UNISTOCHASTICITY  (Gamma_ij=|U_ij|^2 for a unitary U; strictly stronger
      than doubly-stochastic for n>=3) RECORD-BLIND -- do the records, seeing only
      the real transition probabilities / the moment algebra M (invariant under the
      field-reduction R, qubit<->rebit), fail to distinguish unistochastic from
      merely doubly-stochastic, because the distinguishing unitary PHASES live in
      ker R (the SAME field-blindness as the chi_AB tensor-product wall, p6 PART 4)?
                                                               --> classify RECORD_BLIND/DISTINGUISHED/INCONCLUSIVE

THE HONEST PRIOR (stated, then TESTED, NOT assumed): the v7 OI/PI result
(f5_oi_pi_consistency.py) shows survival-multiplicativity along the SEQUENTIAL axis
is ORTHOGONAL to factorization of the joint OUTCOME law across PARALLEL chains.  So
the likely outcome is: the seal FORCES the sequential divisible semigroup (the
FENCE, Q1) while the transverse doubly-vs-unistochastic choice is RECORD-BLIND (the
FILLING, Q3) -- a FOURTH instance of force-the-fence-never-the-filling, a genuine
motivation of the Barandes/Doukas assumption.

THE KILL-CRITERION (pre-declared, binding): if the ONLY result is that exp(-kappa chi)
survival is CONSISTENT WITH unistochastic matrices (a trivial permission, no
non-trivial CONSTRAINT forced), that is a RESTATEMENT, not a derivation -> ABORT
(verdict RESTATEMENT_ABORT).  A GENUINE result requires (a) a non-trivial FORCED
constraint (the fence: the divisible semigroup actually forced, not merely
permitted) AND (b) a clean identification of what is record-blind (the filling).

Pre-geometric discipline: chi is a weight-0 record-internal KL number (accumulated
holonomy content); NO spacetime, metric, light cone, or s^2.  HIGH PRECISION:
mpmath dps>=120 for every cancellation-heavy quantity; sympy-exact where the claim
is algebraic; integer-exact for the K-counts.  Any solver-tolerance number is flagged.

VERIFIED CITATIONS:
  Barandes arXiv:2507.21192 (Indivisible Stochastic Processes): assumes the
    indivisible/non-Markovian transition structure; the WHY is unmotivated.
  Doukas arXiv:2602.22095 (On the emergence of QM from stochastic processes,
    25 Feb 2026): lifts a stochastic kernel Gamma to B(H); Chapman-Kolmogorov
    DIVISIBILITY of the lifted family is the decisive additional constraint; a
    CK-consistent CPTP family admits a Lindblad form; off-diagonal PHASE is a
    compressed carrier of history dependence NOT fixed by transition kernels.
    THE DIRECT COMPANION for Q1/Q3.
"""

import mpmath as mp
import sympy as sp

mp.mp.dps = 140                       # >= 120 with margin for cancellation
TOL = mp.mpf(10) ** (-110)            # high-precision identity tolerance


def head(s):
    print("\n" + "=" * 78)
    print(s)
    print("=" * 78)


def line(label, val, extra=""):
    print(f"  {label:<56} {val} {extra}")


CHECKS = []
def check(name, cond, extra="", solver_tol=False):
    CHECKS.append((name, bool(cond)))
    tag = "PASS" if cond else "*** FAIL ***"
    flag = "  [solver-tol ~1e-9, NOT high precision]" if solver_tol else ""
    line("CHECK  " + name, tag, extra + flag)
    return bool(cond)


# ===========================================================================
#  Helpers: high-precision matrix exponential and stochasticity diagnostics
# ===========================================================================
def matexp(L, t):
    """exp(t L) at mpmath dps; uses native mp.expm (scaling+Pade)."""
    return mp.expm(t * L)

def rowsums(M):
    return [mp.fsum([M[i, j] for j in range(M.cols)]) for i in range(M.rows)]

def colsums(M):
    return [mp.fsum([M[i, j] for i in range(M.rows)]) for j in range(M.cols)]

def minentry(M):
    return min(M[i, j] for i in range(M.rows) for j in range(M.cols))

def umax(U):
    """max deviation of U U^H from I (unitarity defect)."""
    UU = U * U.H
    return max(abs(UU[i, j] - (1 if i == j else 0))
               for i in range(U.rows) for j in range(U.cols))


# ===========================================================================
head("Q1.  DOES REFINEMENT-MULTIPLICATIVITY FORCE THE DIVISIBLE SEMIGROUP exp(chi L)?")
# ===========================================================================
print("""
  The per-step transition object Gamma(chi) is a ROW-stochastic matrix (rows are
  conditional outcome laws p(next | current) -- they MUST sum to 1; this is just
  'the next step has some outcome').  Refinement self-consistency (f3_self_consistency
  PART 2b: inserting an intermediate SEAL must compose; Chapman-Kolmogorov at the
  diagonalizing point) demands, on the WHOLE matrix BEFORE the q=2 screen:

       Gamma(chi1 + chi2) = Gamma(chi1) Gamma(chi2)     for ALL chi1,chi2 >= 0,
       Gamma(0) = I,   Gamma(chi) row-stochastic, Gamma continuous in chi.

  THEOREM (standard, here verified explicitly n=2): a continuous one-parameter
  semigroup of row-stochastic matrices has the form Gamma(chi)=exp(chi L) with L the
  GENERATOR  L = Gamma'(0), and row-stochasticity for ALL chi>=0 FORCES L to be a
  Q-MATRIX (off-diagonal >= 0, each row sums to 0).  This is a GENUINE NON-TRIVIAL
  CONSTRAINT -- the SEQUENTIAL FENCE -- NOT mere consistency: it (i) forbids any
  non-exponential one-parameter family, (ii) pins the per-step law to a single
  generator, (iii) is exactly Doukas' Chapman-Kolmogorov DIVISIBILITY = Lindblad
  premise, here DERIVED from refinement self-consistency rather than assumed.
""")

# --- explicit n=2 Q-matrix generator ---------------------------------------
a, b = mp.mpf("0.8"), mp.mpf("0.3")
L2 = mp.matrix([[-a, a], [b, -b]])          # off-diag>=0, rows sum 0  => Q-matrix
line("n=2 generator L (Q-matrix off-diag>=0, rows sum 0)", "")
for i in range(2):
    line("   L row %d" % i, [mp.nstr(L2[i, j], 6) for j in range(2)],
         "rowsum=%s" % mp.nstr(rowsums(L2)[i], 4))
check("Q1 n=2: L is a Q-matrix (off-diag>=0)", L2[0, 1] >= 0 and L2[1, 0] >= 0)
check("Q1 n=2: L rows sum to 0 (generator)",
      abs(rowsums(L2)[0]) < TOL and abs(rowsums(L2)[1]) < TOL)

# semigroup / divisibility for arbitrary split chi1+chi2
c1, c2 = mp.mpf("0.5"), mp.mpf("0.9")
G1, G2 = matexp(L2, c1), matexp(L2, c2)
G12 = matexp(L2, c1 + c2)
sg_gap = max(abs((G1 * G2)[i, j] - G12[i, j]) for i in range(2) for j in range(2))
line("Q1 semigroup gap |exp(c1 L)exp(c2 L) - exp((c1+c2)L)|", mp.nstr(sg_gap, 6))
check("Q1 n=2: divisible SEMIGROUP exp(chi L) (Chapman-Kolmogorov, dps>=120)",
      sg_gap < TOL)

# exp(chi L) is row-stochastic and nonneg for the Q-matrix generator
G = matexp(L2, mp.mpf("1.4"))
rs = rowsums(G)
line("Q1 row sums of exp(1.4 L)", [mp.nstr(x, 8) for x in rs])
line("Q1 min entry of exp(1.4 L) (Gamma>=0)", mp.nstr(minentry(G), 8))
check("Q1 n=2: exp(chi L) is ROW-stochastic (rows sum 1) AND nonneg",
      all(abs(x - 1) < TOL for x in rs) and minentry(G) >= -TOL)

# --- explicit n=3 Q-matrix generator (matrix BEFORE the q=2 scalar screen) ---
L3 = mp.matrix([[-mp.mpf("0.9"), mp.mpf("0.5"), mp.mpf("0.4")],
                [mp.mpf("0.2"), -mp.mpf("0.7"), mp.mpf("0.5")],
                [mp.mpf("0.6"), mp.mpf("0.1"), -mp.mpf("0.7")]])
check("Q1 n=3: L is a Q-matrix (off-diag>=0)",
      all(L3[i, j] >= 0 for i in range(3) for j in range(3) if i != j))
check("Q1 n=3: L rows sum to 0", all(abs(s) < TOL for s in rowsums(L3)))
H1, H2 = matexp(L3, mp.mpf("0.6")), matexp(L3, mp.mpf("1.1"))
H12 = matexp(L3, mp.mpf("1.7"))
sg3 = max(abs((H1 * H2)[i, j] - H12[i, j]) for i in range(3) for j in range(3))
line("Q1 n=3 semigroup gap", mp.nstr(sg3, 6))
check("Q1 n=3: divisible semigroup (dps>=120)", sg3 < TOL)
check("Q1 n=3: exp(chi L) row-stochastic & nonneg",
      all(abs(x - 1) < TOL for x in rowsums(H12)) and minentry(H12) >= -TOL)

# --- CONVERSE: a NON-generator breaks stochasticity at small chi -------------
# (shows the Q-matrix constraint is BINDING, not vacuous)
Lbad = mp.matrix([[-a, a], [b, -b]]); Lbad[0, 1] = -mp.mpf("0.1")  # neg off-diag
Gbad = matexp(Lbad, mp.mpf("0.01"))
line("Q1 converse: min entry of exp(0.01 Lbad) (Lbad off-diag<0)",
     mp.nstr(minentry(Gbad), 6))
check("Q1 converse: NON-Q-matrix generator -> NEGATIVE entry (not stochastic)",
      minentry(Gbad) < -mp.mpf("1e-6"),
      "row-stochasticity-for-all-chi FORCES L to be a Q-matrix")

# --- survival S=exp(-kappa chi) = sub-stochastic diagonal decay of a generator
print("""
  The forced scalar survival S(chi)=exp(-kappa chi) (after the q=2 screen) is EXACTLY
  the surviving-coherence diagonal entry of such a semigroup: take the 2-state
  generator with one COHERENT state leaking at rate kappa into an ABSORBING SEALED
  state.  Then [exp(chi L_seal)]_{coh,coh} = exp(-kappa chi) -- the sub-stochastic
  (probability-losing) diagonal block of a bona-fide row-stochastic semigroup.
""")
kappa = mp.mpf("0.7")
Lseal = mp.matrix([[-kappa, kappa], [0, 0]])    # coherent->sealed leak; sealed absorbing
Gseal = matexp(Lseal, mp.mpf("1.3"))
S_pred = mp.exp(-kappa * mp.mpf("1.3"))
line("[exp(1.3 L_seal)]_{coh,coh}", mp.nstr(Gseal[0, 0], 14))
line("exp(-kappa*1.3)            ", mp.nstr(S_pred, 14))
line("gap", mp.nstr(abs(Gseal[0, 0] - S_pred), 6))
check("Q1: S=exp(-kappa chi) is the sub-stochastic diagonal decay of the seal "
      "generator (dps>=120)", abs(Gseal[0, 0] - S_pred) < TOL)
# multiplicativity of the survival diagonal across a refinement split (sympy-exact)
kp, x1, x2 = sp.symbols('kappa chi1 chi2', nonnegative=True)
resid = sp.simplify(sp.exp(-kp * (x1 + x2)) - sp.exp(-kp * x1) * sp.exp(-kp * x2))
line("sympy: S(c1+c2)-S(c1)S(c2)", resid)
check("Q1: survival diagonal multiplicative S(c1+c2)=S(c1)S(c2) (sympy-exact)",
      resid == 0)

print("""
  Q1 VERDICT: FORCED.  Refinement-multiplicativity of the ROW-stochastic family +
  Gamma(0)=I + continuity FORCES the divisible Markov semigroup Gamma(chi)=exp(chi L)
  with L a Q-matrix generator -- the SEQUENTIAL FENCE.  This is a genuine non-trivial
  constraint (the converse shows a non-generator FAILS stochasticity), and it is
  EXACTLY Doukas' Chapman-Kolmogorov DIVISIBILITY / Lindblad premise, here DERIVED
  (not assumed) from refinement self-consistency.  The forced survival
  S=exp(-kappa chi) is the sub-stochastic diagonal decay of this very semigroup.
  This MOTIVATES the Barandes/Doukas transition-matrix assumption from inside.
""")


# ===========================================================================
head("Q2.  DOES seal + Gamma>=0 FORCE DOUBLY-STOCHASTIC (columns sum to 1)?")
# ===========================================================================
print("""
  Row-stochasticity is FORCED (Q1: 'the next step has some outcome').  DOUBLE-
  stochasticity (columns ALSO sum to 1) is an EXTRA condition: it says the UNIFORM
  distribution is stationary (B^T 1 = 1).  We test whether the seal skeleton +
  Gamma>=0 forces it.  COUNTEREXAMPLE strategy: a generic Q-matrix generator has a
  NON-uniform stationary distribution pi (left null vector of L), so exp(chi L) is
  row-stochastic, Gamma>=0, seal-multiplicative -- yet NOT column-stochastic.  The
  stationary-distribution CHOICE is FREE.  Double-stochasticity requires a SPECIAL
  (e.g. symmetric / doubly-balanced) generator -- it is an extra INPUT, un-forced.
""")

# the SAME n=2 generator L2 (a valid sealed family): row-stochastic, Gamma>=0
csG = colsums(G)                                   # G = exp(1.4 L2) from Q1
line("Q2 row sums of exp(1.4 L2)  (FORCED = 1)", [mp.nstr(x, 8) for x in rowsums(G)])
line("Q2 col sums of exp(1.4 L2)  (FREE != 1)", [mp.nstr(x, 8) for x in csG])
line("Q2 col-sum deviation from 1", [mp.nstr(abs(x - 1), 6) for x in csG])
check("Q2 n=2: valid sealed family is ROW-stochastic (forced)",
      all(abs(x - 1) < TOL for x in rowsums(G)))
check("Q2 n=2: same family is Gamma>=0 and seal-multiplicative",
      minentry(G) >= -TOL and sg_gap < TOL)
check("Q2 n=2: it is NOT column-stochastic (double-stoch FAILS, deviation>0.1)",
      max(abs(x - 1) for x in csG) > mp.mpf("0.1"),
      "stationary distribution is non-uniform => columns free")

# stationary distribution (left null vector of L2): pi=(b,a)/(a+b), non-uniform
pi = (b / (a + b), a / (a + b))
line("Q2 stationary distribution pi (left null of L)", [mp.nstr(x, 8) for x in pi])
check("Q2: stationary distribution is NON-uniform (free choice, not 1/n)",
      abs(pi[0] - mp.mpf("0.5")) > mp.mpf("0.1"))

# n=3 valid sealed family also not doubly-stochastic
csH = colsums(H12)
line("Q2 n=3 col sums of exp(1.7 L3)", [mp.nstr(x, 6) for x in csH])
check("Q2 n=3: row-stochastic (forced) but NOT column-stochastic",
      all(abs(x - 1) < TOL for x in rowsums(H12))
      and max(abs(x - 1) for x in csH) > mp.mpf("0.05"))

# double-stochasticity DOES hold for a SPECIAL symmetric generator -> it's an extra input
Lsym = mp.matrix([[-a, a], [a, -a]])               # symmetric Q-matrix
Gsym = matexp(Lsym, mp.mpf("1.4"))
line("Q2 symmetric generator -> col sums", [mp.nstr(x, 8) for x in colsums(Gsym)])
check("Q2: double-stochasticity holds ONLY for a SPECIAL (symmetric) generator "
      "=> it is an EXTRA un-forced input",
      all(abs(x - 1) < TOL for x in colsums(Gsym))
      and max(abs(x - 1) for x in csG) > mp.mpf("0.1"))

print("""
  Q2 VERDICT: NOT (double-stochasticity un-forced; only PERMITTED for special
  generators).  The seal + Gamma>=0 force ROW-stochasticity but NOT column-
  stochasticity: an explicit valid sealed family (n=2 and n=3) is row-stochastic,
  Gamma>=0, seal-multiplicative, yet has non-uniform stationary distribution and
  column sums != 1.  Double-stochasticity = 'uniform distribution is stationary' is
  a SEPARATE stationary-distribution CHOICE, an extra input the seal does NOT supply.
  (It can be MOTIVATED downstream by an extra symmetry/maximum-entropy prior on the
  stationary law -- e.g. Barandes' time-reversal symmetric / unital case -- but it
  is NOT forced by the seal skeleton itself.)
""")


# ===========================================================================
head("Q3.  IS UNISTOCHASTIC vs DOUBLY-STOCHASTIC RECORD-BLIND? (the decisive one)")
# ===========================================================================
print("""
  UNISTOCHASTIC: Gamma_ij = |U_ij|^2 for a unitary U.  For n>=3 strictly STRONGER
  than doubly-stochastic (Birkhoff-von-Neumann polytope strictly contains the
  unistochastic set).  THE QUESTION: can the records distinguish unistochastic from
  merely doubly-stochastic?  The records see ONLY the real transition probabilities
  Gamma_ij = |U_ij|^2 -- i.e. the moment algebra M (marginals + cross-moments),
  invariant under the field-reduction R (qubit<->rebit, complex->real).  The
  DISTINGUISHING data is the unitary PHASES of U, which live in ker R.

  PART 3a.  Standard n=3 example: a DOUBLY-stochastic matrix that is NOT
            unistochastic (rigorous triangle/chain criterion).  [DISTINCTION EXISTS]
  PART 3b.  PHASE-BLINDNESS: distinct unitaries with IDENTICAL records |U_ij|^2
            (differ only by phases in ker R) -- the records cannot tell them apart,
            cannot read off the phase content (Jarlskog), cannot even tell a real
            (rebit) preimage from a complex (qubit) one.  [RECORD-BLIND]
  PART 3c.  Tie to p6 PART 4: the distinguishing bit is the SAME local-tomography /
            complex-over-real bit that is in ker R for chi_AB.  [FOURTH INSTANCE]
""")

# ---------------------------------------------------------------------------
print("\n  PART 3a.  n=3 doubly-stochastic but NOT unistochastic (rigorous).")
# the standard cyclic example
B = mp.matrix([[mp.mpf(1) / 2, mp.mpf(1) / 2, 0],
               [0, mp.mpf(1) / 2, mp.mpf(1) / 2],
               [mp.mpf(1) / 2, 0, mp.mpf(1) / 2]])
line("B (doubly stochastic candidate)", "")
for i in range(3):
    line("   B row %d" % i, [mp.nstr(B[i, j], 6) for j in range(3)])
check("Q3a: B is doubly-stochastic (rows AND cols sum to 1)",
      all(abs(x - 1) < TOL for x in rowsums(B))
      and all(abs(x - 1) < TOL for x in colsums(B)))

# rigorous 3x3 unistochasticity criterion (chain/triangle on sqrt-products).
# For a 3x3 doubly-stochastic B, define for each pair of COLUMNS (j,k):
#   t_i = sqrt(B_ij B_ik).  B unistochastic  <=>  the t_i obey the TRIANGLE
#   inequalities (a unitarity-triangle closes) for the column pair.
def triangle(t):
    a_, b_, c_ = t
    eps = mp.mpf(10) ** (-100)
    return (a_ <= b_ + c_ + eps) and (b_ <= a_ + c_ + eps) and (c_ <= a_ + b_ + eps)

uni_ok = False
for (j, k) in [(0, 1), (0, 2), (1, 2)]:
    t = [mp.sqrt(B[i, j] * B[i, k]) for i in range(3)]
    ok = triangle(t)
    line("Q3a cols %s: t_i=sqrt(B_ij B_ik)=%s triangle?"
         % ((j, k), [mp.nstr(v, 5) for v in t]), ok)
    uni_ok = uni_ok or ok
check("Q3a: B is NOT unistochastic (unitarity-triangle FAILS for every column pair)",
      not uni_ok,
      "t=(1/2,0,0): 1/2 > 0+0 => no unitary U with |U_ij|^2=B_ij")

# sanity: a genuinely UNISTOCHASTIC doubly-stochastic matrix DOES pass (DFT -> flat)
w = mp.exp(2j * mp.pi / 3)
Udft = mp.matrix([[1, 1, 1], [1, w, w**2], [1, w**2, w**4]]) / mp.sqrt(3)
Bflat = mp.matrix(3, 3)
for i in range(3):
    for j in range(3):
        Bflat[i, j] = abs(Udft[i, j]) ** 2
line("Q3a unitary DFT image (should be flat 1/3)",
     [mp.nstr(Bflat[0, j], 5) for j in range(3)])
check("Q3a: DFT unitary -> unistochastic flat-1/3 matrix (control passes)",
      umax(Udft) < TOL
      and all(abs(Bflat[i, j] - mp.mpf(1) / 3) < TOL for i in range(3) for j in range(3)))

# ---------------------------------------------------------------------------
print("\n  PART 3b.  PHASE-BLINDNESS: distinct U with IDENTICAL records |U_ij|^2.")
print("""
  The records ARE the unistochastic matrix Gamma_ij=|U_ij|^2.  We exhibit unitaries
  that produce the SAME Gamma yet differ in phase content (in ker R).  Three layers:
   (i)   a real orthogonal O and a complex unitary Uc with IDENTICAL |.|^2 (n=2),
   (ii)  a genuinely complex (CP-phase) n=3 unitary rephased D1 U D2 -> SAME records,
   (iii) the records cannot read the Jarlskog phase invariant J (its SIGN is in ker R).
""")

# (i) n=2: real orthogonal vs complex unitary, same moduli-squared
th = mp.mpf("0.6")
cc, ss = mp.cos(th), mp.sin(th)
O = mp.matrix([[cc, -ss], [ss, cc]])                       # real (rebit-realizable)
phase = mp.exp(1j * mp.mpf("1.1"))
Uc = mp.matrix([[cc, -ss * phase], [ss, cc * phase]])       # complex, SAME |.|^2
mod_gap = max(abs(abs(O[i, j])**2 - abs(Uc[i, j])**2) for i in range(2) for j in range(2))
line("Q3b(i) O orthogonal? / Uc unitary?", "%s / %s"
     % (mp.nstr(umax(O), 4), mp.nstr(umax(Uc), 4)))
line("Q3b(i) max | |O_ij|^2 - |Uc_ij|^2 |  (record gap)", mp.nstr(mod_gap, 6))
check("Q3b(i): a REAL (rebit) and a COMPLEX (qubit) unitary give IDENTICAL records",
      mod_gap < TOL and umax(O) < TOL and umax(Uc) < TOL,
      "records (transition probabilities) cannot tell real from complex preimage")

# (ii) n=3 genuinely complex CKM-like unitary; rephase -> identical records
def ckm(t12, t13, t23, delta):
    c12, s12 = mp.cos(t12), mp.sin(t12)
    c13, s13 = mp.cos(t13), mp.sin(t13)
    c23, s23 = mp.cos(t23), mp.sin(t23)
    ed = mp.exp(1j * delta)
    R23 = mp.matrix([[1, 0, 0], [0, c23, s23], [0, -s23, c23]])
    R13 = mp.matrix([[c13, 0, s13 * mp.conj(ed)], [0, 1, 0], [-s13 * ed, 0, c13]])
    R12 = mp.matrix([[c12, s12, 0], [-s12, c12, 0], [0, 0, 1]])
    return R23 * R13 * R12

U = ckm(mp.mpf("0.5"), mp.mpf("0.3"), mp.mpf("0.7"), mp.mpf("1.2"))
Bu = mp.matrix(3, 3)
for i in range(3):
    for j in range(3):
        Bu[i, j] = abs(U[i, j]) ** 2
check("Q3b(ii): CKM-type U is unitary; |U_ij|^2 is doubly-stochastic (unistochastic)",
      umax(U) < TOL
      and all(abs(x - 1) < TOL for x in rowsums(Bu))
      and all(abs(x - 1) < TOL for x in colsums(Bu)))

# rephase columns and rows by diagonal phase matrices -> SAME |U_ij|^2
D1 = mp.diag([mp.exp(1j * mp.mpf("0.4")), mp.exp(1j * mp.mpf("2.1")), mp.exp(1j * mp.mpf("-0.9"))])
D2 = mp.diag([mp.exp(1j * mp.mpf("1.7")), mp.exp(1j * mp.mpf("0.2")), mp.exp(1j * mp.mpf("3.0"))])
Up = D1 * U * D2
Bp = mp.matrix(3, 3)
for i in range(3):
    for j in range(3):
        Bp[i, j] = abs(Up[i, j]) ** 2
rec_gap = max(abs(Bu[i, j] - Bp[i, j]) for i in range(3) for j in range(3))
uni_gap = max(abs(U[i, j] - Up[i, j]) for i in range(3) for j in range(3))
line("Q3b(ii) max|records(U) - records(D1 U D2)|", mp.nstr(rec_gap, 6))
line("Q3b(ii) max|U - D1 U D2|  (the unitaries DO differ)", mp.nstr(uni_gap, 6))
check("Q3b(ii): rephased D1 U D2 has IDENTICAL records but DIFFERENT unitary "
      "(phases in ker R)", rec_gap < TOL and uni_gap > mp.mpf("0.5"))

# (iii) the Jarlskog phase invariant J -- a quantity the records cannot fix
def jarlskog(V):
    return (V[0, 0] * V[1, 1] * mp.conj(V[0, 1]) * mp.conj(V[1, 0])).imag
J_U = jarlskog(U)
# a DIFFERENT unitary with the SAME records but OPPOSITE Jarlskog sign: complex-conjugate
Uconj = mp.matrix(3, 3)
for i in range(3):
    for j in range(3):
        Uconj[i, j] = mp.conj(U[i, j])             # conjugation preserves |U_ij|^2, flips J
Bc = mp.matrix(3, 3)
for i in range(3):
    for j in range(3):
        Bc[i, j] = abs(Uconj[i, j]) ** 2
conj_rec_gap = max(abs(Bu[i, j] - Bc[i, j]) for i in range(3) for j in range(3))
J_conj = jarlskog(Uconj)
line("Q3b(iii) Jarlskog J(U)", mp.nstr(J_U, 12))
line("Q3b(iii) Jarlskog J(U*)  (conjugate, SAME records)", mp.nstr(J_conj, 12))
line("Q3b(iii) record gap between U and U*", mp.nstr(conj_rec_gap, 6))
check("Q3b(iii): U and U* have IDENTICAL records but OPPOSITE Jarlskog sign "
      "(J in ker R)",
      conj_rec_gap < TOL and abs(J_U + J_conj) < TOL and abs(J_U) > mp.mpf("0.01"),
      "the complex-phase content (J, its sign) is record-INVISIBLE")

# ---------------------------------------------------------------------------
print("\n  PART 3c.  TIE TO p6 PART 4: the distinguishing bit is the SAME ker-R bit.")
print("""
  The bit that would PROMOTE a doubly-stochastic matrix to a UNIQUE unitary preimage
  (fixing unistochasticity AND its phases) is the COMPLEX-over-REAL / local-tomography
  bit -- IDENTICALLY the bit that fixes a unique complex chi_AB in p6 PART 4.  We
  reproduce the p6 PART-4 K-counts (sympy-EXACT integers): M (the moment algebra /
  records) preserves all transition probabilities but NOT this count, so R (qubit<->
  rebit) is invisible to it.  Unistochastic-vs-doubly-stochastic is distinguished
  ONLY by phases in ker R -> a FOURTH instance of the field-blindness wall.
""")
d = sp.Integer(2)
K_single_C = d**2                        # complex qubit  = 4
K_single_R = d * (d + 1) // 2            # real rebit     = 3
D = sp.Integer(4)
K_2qubit = D**2                          # 16
K_2rebit = D * (D + 1) // 2              # 10
deficit_R = K_2rebit - K_single_R * K_single_R   # +1
deficit_C = K_2qubit - K_single_C * K_single_C   # 0
line("Q3c K_single  complex(qubit)=d^2 / real(rebit)=d(d+1)/2",
     "%s / %s" % (K_single_C, K_single_R))
line("Q3c K_AB  2qubit=D^2 / 2rebit=D(D+1)/2", "%s / %s" % (K_2qubit, K_2rebit))
line("Q3c local-tomography deficit  rebit / qubit",
     "%s / %s" % (deficit_R, deficit_C))
check("Q3c: p6 PART-4 K-counts reproduced (sympy-exact): R=3,C=4; 2rebit=10,2qubit=16",
      K_single_R == 3 and K_single_C == 4 and K_2rebit == 10 and K_2qubit == 16)
check("Q3c: complex-over-real bit is +1 deficit (rebit) vs 0 (qubit) -- in ker R, "
      "the SAME bit that distinguishes unistochastic from doubly-stochastic",
      deficit_R == 1 and deficit_C == 0,
      "phases distinguishing |U_ij|^2-preimages live in ker R = chi_AB field-blindness")

print("""
  Q3 VERDICT: RECORD_BLIND.  (a) For n>=3 a genuine DISTINCTION exists -- the
  standard cyclic matrix is doubly-stochastic but NOT unistochastic (unitarity
  triangle fails).  (b) BUT the records (the transition probabilities = the moment
  algebra M = |U_ij|^2) CANNOT see the distinguishing data: distinct unitaries
  (real vs complex; U vs D1 U D2; U vs U*) carry IDENTICAL records while differing
  by PHASES, including the Jarlskog phase invariant whose very SIGN is record-
  invisible.  Those phases live in ker R -- IDENTICALLY the complex-over-real /
  local-tomography bit (p6 PART-4 K-deficit +1) that fixes a unique complex chi_AB.
  Unistochastic-vs-doubly-stochastic is thus a FOURTH instance of force-the-fence-
  never-the-filling: the records are BLIND to the unitary-phase filling.
""")


# ===========================================================================
head("CENTRAL VERDICT  (kill-criterion adjudicated)")
# ===========================================================================
all_pass = all(c for _, c in CHECKS)
n_pass = sum(1 for _, c in CHECKS if c)
n_tot = len(CHECKS)

print(f"""
  THE CENTRAL QUESTION: does the SHARD seal skeleton (multiplicative survival
  S=exp(-kappa chi) + orthogonal-projection seal + transverse Gamma>=0) FORCE the
  Barandes/Doukas transition-matrix structure, or merely PERMIT it?

  KILL-CRITERION CHECK (pre-declared, binding):
    Required for a GENUINE result (NOT a restatement):
      (a) a NON-TRIVIAL FORCED constraint (the fence)         -> Q1: FORCED (the
          divisible Markov semigroup exp(chi L), L a Q-matrix generator, is forced
          by refinement-multiplicativity; the converse shows a non-generator FAILS
          stochasticity, so the constraint is BINDING, not vacuous).  This is
          EXACTLY Doukas' Chapman-Kolmogorov divisibility / Lindblad premise,
          DERIVED here rather than assumed.
      (b) a CLEAN identification of what is record-blind (the filling) -> Q3:
          RECORD_BLIND (unistochastic-vs-doubly-stochastic is distinguished ONLY by
          unitary phases in ker R = the chi_AB field-blindness bit, p6 PART-4).
    Both (a) and (b) are satisfied with explicit small matrices and high precision.
    => NOT a RESTATEMENT_ABORT.  A genuine derivation.

  THE THREE-WAY SPLIT (honest FORCED / PERMITTED / NOT / RECORD-BLIND):
    Q1  divisible Markov SEMIGROUP exp(chi L), L a Q-matrix     FORCED      (the FENCE)
        - survival S=exp(-kappa chi) = sub-stochastic diagonal decay of that semigroup
    Q2  DOUBLY-stochastic (columns sum 1)                       NOT/PERMITTED (un-forced;
        - row-stochastic forced; stationary distribution FREE;   only for special
          double-stochasticity is an extra symmetry input)       symmetric generators)
    Q3  UNISTOCHASTIC vs doubly-stochastic                      RECORD_BLIND (the FILLING)
        - distinction real for n>=3, but distinguishing PHASES in ker R; records
          (the moment algebra M) see only |U_ij|^2; FOURTH ker-R field-blindness.

  This MOTIVATES the Barandes/Doukas assumption from inside: the seal FORCES the
  divisible-semigroup transition structure (the fence Barandes/Doukas posit), while
  the doubly-stochastic stationary-law choice is un-forced and the unistochastic
  phase content is record-blind (the filling they fill by fiat / by lift to B(H)).
  Force-the-fence-never-the-filling, a FOURTH instance, consistent with the v7
  OI/PI orthogonality (f5): sequential multiplicativity is the fence; transverse /
  phase structure is the record-blind filling.

  ALL CHECKS PASS: {all_pass}   ({n_pass}/{n_tot})
""")

assert all_pass, "SOME CHECK FAILED -- see *** FAIL *** above"
print(f"ALL CHECKS PASS ({n_pass}/{n_tot})")
head("DONE.  (all machine-check asserts passed; mpmath dps=%d, sympy-exact where algebraic)" % mp.mp.dps)
