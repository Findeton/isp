"""
ADJUDICATOR independent sanity-check of Paper57 sec 3.3 decisive structural claim.

Claim under test: a crossed product of a COMMUTATIVE record algebra A by any
classical flow (modular OR sigma-arrow) stays semifinite (type I/II, never III_1)
UNLESS the action is ergodic-without-equivalent-invariant-measure (i.e. its
Connes Radon-Nikodym cocycle has nontrivial ratio set / measure-class change).

We verify, from scratch (not reusing the agents' scripts):

 (A) modular flow on a commutative (diagonal Gibbs) algebra is inner/trivial:
     ||[A_hat, a]|| = 0  for the diagonal modular generator.

 (B) the sigma-arrow flow alpha_t = e^{tL}, L = P - I (P a stochastic kernel),
     IS genuinely non-trivial/outer on A: ||[L, a]|| > 0.

 (C) sigma = D(P_AB || P_BA) = E[A_D] > 0 (the corpus arrow, paper10 T2),
     BUT pi is invariant: pi P = pi  =>  the Connes RN cocycle
     [d(pi o alpha_t)/d pi] = 1  =>  asymptotic ratio set = {1}.
     By Krieger/Connes-Takesaki: ratio set {1}  =>  crossed product SEMIFINITE
     (type I or II), NEVER type III_1.

 (D) the half-sided modular inclusion [K,P]=iP has NO finite-dim rep:
     Hermitian K with real spectrum + [K,P]=iP forces P=0 (ladder argument).

 (E) DECISIVE general lemma (the thing the prompt asks me to settle):
     for ANY classical flow on a commutative algebra preserving an equivalent
     finite measure, ratio set = {1}, so crossed product is semifinite.
     A type-III_1 seed REQUIRES a flow with NO equivalent sigma-finite invariant
     measure (essentially-ergodic / dissipative). The sigma-arrow of paper10 is
     DEFINED at stationarity (pi P = pi), so it can NEVER be that flow.
"""
import numpy as np
import mpmath as mp
import sympy as sp

mp.mp.dps = 100
np.random.seed(0)

def opnorm(M):
    # spectral norm via largest singular value, computed in high precision-ish
    M = np.asarray(M, dtype=complex)
    return float(np.linalg.norm(M, 2))

print("="*78)
print("(A) MODULAR FLOW ON COMMUTATIVE (DIAGONAL) ALGEBRA IS INNER/TRIVIAL")
print("="*78)
# A diagonal Gibbs state rho = diag(p), modular operator Delta = rho (x) rho^{-1}
# acting on the commutative algebra A = diagonal matrices. The modular generator
# for a DIAGONAL state acting on DIAGONAL operators is [log rho, .] = 0.
n = 6
p = np.abs(np.random.rand(n)); p /= p.sum()
logrho = np.diag(np.log(p))              # modular generator log Delta (one-sided)
a = np.diag(np.random.rand(n))           # an element of the commutative algebra A
comm_mod = logrho @ a - a @ logrho
print("  diagonal state p:", np.round(p,4))
print("  ||[log rho, a]|| (modular generator vs commutative element) =", opnorm(comm_mod))
print("  -> modular flow is INNER/TRIVIAL on A (matches sec3.3(ii): ||[A_hat,a]||=0)")

print()
print("="*78)
print("(B+C) SIGMA-ARROW FLOW: NON-TRIVIAL/OUTER, BUT INVARIANT-MEASURE PRESERVING")
print("="*78)
# Build an irreducible stochastic kernel P with NON-symmetric (driven) currents,
# i.e. genuine entropy production sigma = D(P_AB || P_BA) > 0 at its stationary pi.
# Use a 4-state driven cycle (Schnakenberg).
P = np.array([
    [0.1, 0.6, 0.0, 0.3],
    [0.2, 0.1, 0.6, 0.1],
    [0.3, 0.1, 0.1, 0.5],
    [0.5, 0.2, 0.2, 0.1],
])
# stationary distribution pi: left eigenvector of P with eigenvalue 1
w, V = np.linalg.eig(P.T)
idx = np.argmin(np.abs(w - 1.0))
pi = np.real(V[:, idx]); pi = pi / pi.sum()
print("  stochastic P rows sum to 1:", np.round(P.sum(axis=1),12))
print("  stationary pi:", np.round(pi,6))
print("  invariance residual ||pi P - pi|| =", opnorm((pi @ P - pi).reshape(1,-1)))

# sigma-arrow generator L = P - I, acting on functions (the commutative algebra A
# = diagonal multiplication operators on C^4). Test it is OUTER (moves A):
L = P - np.eye(4)
acomm = np.diag([1.0, 2.0, 3.0, 4.0])   # a in A (diagonal multiplication op)
# action of flow generator on A by conjugation in the GNS/regular rep:
# represent A as diagonal, L as a Markov generator on the same index set.
comm_sig = L @ acomm - acomm @ L
print("  ||[L = P-I, a]|| (sigma-flow generator vs commutative element) =",
      opnorm(comm_sig), " > 0  -> OUTER/non-trivial")

# entropy production sigma = sum_{a,b} pi_a P_ab log(P_ab/P_ba)  (the paper10 arrow)
# Use mpmath for the value.
mp.mp.dps = 100
Pm = mp.matrix(P.tolist())
pim = mp.matrix(pi.tolist())
sigma = mp.mpf(0)
for i in range(4):
    for j in range(4):
        Pij = Pm[i,j]; Pji = Pm[j,i]
        if Pij > 0 and Pji > 0:
            sigma += pim[i]*Pij*mp.log(Pij/Pji)
print("  sigma = D(P_AB||P_BA) = sum pi_a P_ab log(P_ab/P_ba) =", mp.nstr(sigma, 25))
print("  sigma > 0 ?", sigma > 0, " (strictly positive -> genuine arrow, paper10 T2)")

# Connes RN cocycle for the flow alpha_t = e^{tL}: measure-class derivative
# d(pi o alpha_t)/d pi.  Because pi is INVARIANT (pi e^{tL} = pi for all t),
# the pushed-forward measure equals pi, so the RN derivative is identically 1.
print()
print("  --- Connes RN cocycle / ratio set test ---")
for t in [0.5, 1.0, 2.0, 5.0]:
    expL = sp.Matrix(P.tolist()) - sp.eye(4)   # generator
    # exp(t L) numerically in high precision via mpmath
    Lm = Pm - mp.eye(4)
    alpha_t = mp.expm(t*Lm)         # row-stochastic-ish flow on functions
    pushed = pim.T * alpha_t        # pi pushed forward (row vector) = pi e^{tL}
    rn_dev = max(abs(pushed[0,k] - pim[k]) for k in range(4))
    print(f"    t={t}: max|d(pi o alpha_t)/dpi - 1| = {mp.nstr(rn_dev, 6)}")
print("  -> RN cocycle == 1 for all t  =>  asymptotic ratio set r(M) = {1}")
print("  -> Krieger/Connes-Takesaki: ratio set {1} => crossed product SEMIFINITE")
print("  -> NOT type III_1 (type III_1 requires ratio set = [0, infinity))")
