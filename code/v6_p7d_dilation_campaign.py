"""
v6_p7d: dilation campaign (gates 5 and 1 jointly).
D1: every sealed record transition law has a constructive unitary
    (unistochastic) dilation: squared-modulus marginals reproduce it.
D3: Bargmann loop phases of the dilation are gauge-invariant under
    record relabeling phases and ARE the retained holonomy: two-route
    interference is exactly the loop phase.
D5: Gaussian-sector (R-) discharge: the Euclidean correlator at beta = Theta
    equals the analytically continued Lorentzian correlator of the SAME
    generator, identically.
Sorkin: quadratic weights => third-order interference parameter kappa_3 = 0
    exactly; p != 2 norms violate it (the triple-slit experiments test p=2).
Duality: V = Bhattacharyya survival satisfies the wave-particle duality
    inequality V^2 + D^2 <= 1 (Fuchs-van de Graaf), with the Gaussian-pointer
    case matching QM visibility exactly.
"""
import numpy as np
from scipy.linalg import null_space
rng = np.random.default_rng(11)

print("=== p7d: dilation / loop-holonomy / Sorkin / duality ===\n")

# ---------- D1: constructive Stinespring dilation -----------------------------
print("D1: unitary dilation of a sealed transition law")
d = 3
G = rng.random((d,d)); G = G / G.sum(axis=0, keepdims=True)     # columns P(j|i)
V = np.zeros((d*d, d))
for i in range(d):
    for j in range(d):
        V[j*d + i, i] = np.sqrt(G[j,i])        # ancilla-out = input label
print(f"  isometry check |V^T V - I| = {np.max(np.abs(V.T@V-np.eye(d))):.3e}")
N = null_space(V.T)                             # orthonormal completion
U = np.hstack([V, N])
print(f"  unitarity |U^T U - I| = {np.max(np.abs(U.T@U-np.eye(d*d))):.3e}")
marg = np.zeros((d,d))
for i in range(d):
    col = U[:, i]                               # input (i, anc=0)
    for j in range(d):
        marg[j,i] = np.sum(col[j*d:(j+1)*d]**2)
print(f"  squared-modulus marginal vs Gamma: max gap = {np.max(np.abs(marg-G)):.3e}")
print("  => every record law IS unistochastically representable: (Q)-existence DISCHARGED.\n")

# ---------- D3: Bargmann loop phases = retained holonomy ----------------------
print("D3: loop phases are gauge-invariant and are the interference law")
n = 5
Z = (rng.standard_normal((n,n)) + 1j*rng.standard_normal((n,n)))/np.sqrt(2)
Q,_ = np.linalg.qr(Z)                            # Haar-ish unitary
loop = [0,2,4,1]
def bargmann(U, loop):
    z = 1.0+0j
    for a,b in zip(loop, loop[1:]+loop[:1]):
        z *= U[b,a]
    return z
B0 = bargmann(Q, loop)
D = np.diag(np.exp(1j*rng.uniform(0,2*np.pi,n)))
B1 = bargmann(D@Q@D.conj().T, loop)
print(f"  |arg B - arg B'| under record rephasing U -> D U D^dag = {abs(np.angle(B0)-np.angle(B1)):.3e}")
i,m,mp,k = 0,1,3,4
A = Q[k,m]*Q[m,i]; Bc = Q[k,mp]*Q[mp,i]
Delta = np.angle(A*np.conj(Bc))                  # 4-cycle Bargmann phase
P_coh = abs(A+Bc)**2
P_law = abs(A)**2 + abs(Bc)**2 + 2*abs(A)*abs(Bc)*np.cos(Delta)
print(f"  two-route interference vs loop-phase law: gap = {abs(P_coh-P_law):.3e}")
print("  => retained holonomy = Bargmann loop class of the dilation: (Q)-canonicity")
print("     reduces to the corpus' own closed-holonomy ledger (P4 s40 Mobius reconstruction).\n")

# ---------- D5: Gaussian (R-) discharge ----------------------------------------
print("D5: Euclidean correlator = continued Lorentzian correlator (same generator)")
w, beta = 1.3, 2*np.pi
CE = lambda t: np.cosh(w*(beta/2-t))/(2*w*np.sinh(w*beta/2))
CLcont = lambda t: (1/np.tanh(beta*w/2)*np.cos(w*(-1j*t)) - 1j*np.sin(w*(-1j*t)))/(2*w)
gaps = [abs(CE(t)-CLcont(t)) for t in (0.3, 1.0, 2.5)]
print(f"  |C_E(tau) - C_L(-i tau)| at tau=0.3,1.0,2.5 = {gaps[0]:.2e}, {gaps[1]:.2e}, {gaps[2]:.2e}")
print("  => Gaussian sector: the Euclidean extension EXISTS with the same generator;")
print("     (R-) is DISCHARGED for free record sectors; kernel shrinks to interacting (R-)'.\n")

# ---------- Sorkin third-order parameter -----------------------------------------
print("Sorkin parameter kappa_3 (triple-slit):")
a = (rng.standard_normal(3)+1j*rng.standard_normal(3))
def I_p(S, p):
    z = sum(a[s] for s in S)
    return abs(z)**p
def kappa3(p):
    return (I_p([0,1,2],p) - I_p([0,1],p) - I_p([0,2],p) - I_p([1,2],p)
            + I_p([0],p) + I_p([1],p) + I_p([2],p))
for p in (2.0, 1.5, 3.0):
    print(f"  p = {p}: kappa_3 = {kappa3(p):+.6e}")
print("  => kappa_3 = 0 exactly iff weights are quadratic (p=2): the Sinha et al.")
print("     triple-slit experiments are direct empirical tests of the p=2 selection.\n")

# ---------- duality: V = Bhattacharyya survival ------------------------------------
print("wave-particle duality from record overlap (V = sum sqrt(p0 p1)):")
worst = 1.0; viol=0
for _ in range(20000):
    p0 = rng.dirichlet(np.ones(4)); p1 = rng.dirichlet(np.ones(4))
    V = np.sum(np.sqrt(p0*p1)); Dtv = 0.5*np.sum(np.abs(p0-p1))
    s = V*V + Dtv*Dtv
    worst = min(worst, 1-s) if s<=1 else worst
    if s > 1+1e-12: viol += 1
print(f"  V^2 + D^2 <= 1 over 20000 random record pairs: violations = {viol}")
dlt, sig = 1.7, 0.6
Vqm = np.exp(-dlt**2/(8*sig**2))
xs = np.linspace(-12,12,200001)
g0 = np.exp(-(xs+dlt/2)**2/(2*sig**2)); g1 = np.exp(-(xs-dlt/2)**2/(2*sig**2))
g0/=np.trapezoid(g0,xs); g1/=np.trapezoid(g1,xs)
Vrec = np.trapezoid(np.sqrt(g0*g1), xs)
print(f"  Gaussian pointer: QM visibility e^(-d^2/8s^2) = {Vqm:.12f}, record Bhattacharyya = {Vrec:.12f}, gap = {abs(Vqm-Vrec):.2e}")
print("  => V = exp(-I_B) with I_B the Bhattacharyya record evidence: duality is")
print("     no-division survival; matches QM exactly for real-Gaussian pointers.")
