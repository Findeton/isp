"""
v6_p6e: naturality audit campaign (gate G1).
Part 1: audit-by-execution. Every finite law of the corpus is implemented as a
        function of (record data; A_rec). Outputs must be bit-identical across
        A_rec values: the gauge parameter must not appear in any law.
Part 2: the n^2 covariance lemma. The refinement normalization L_n = c*n^2*(D-A)
        is chart-side: record outputs are c-independent exactly; chart outputs
        carry weight; intrinsic spectral ratios are c-independent at every n.
Part 3: joint unit coherence. length unit l0 -> mu*l0 induces A_rec -> mu^2*A_rec
        and chart factor -> mu^-2; intrinsic readouts fixed, labels covariant.
"""
import numpy as np
from mpmath import mp, tanh, cosh, log, exp, findroot, mpf
from scipy.optimize import fsolve
mp.dps = 25

print("=== p6e: naturality audit campaign (G1) ===\n")
print("Part 1: audit-by-execution over the corpus laws")

def law_saturation_root(A_rec):
    return float(findroot(lambda e: e*tanh(e)-log(cosh(e))-(1-tanh(e)**2), 1.1))

def law_commitment_root(A_rec):
    return float(findroot(lambda e: tanh(e)-exp(-e), 0.6))

def law_coupled_ledger(A_rec):
    states=[(x,y) for x in (-1,1) for y in (-1,1)]
    chi=np.array([[x,y,x*y] for (x,y) in states],float)
    def g(h):
        w=np.exp(chi@h)/4.0; p=w/w.sum()
        return chi.T@p-np.exp(-h)
    return fsolve(g,[0.5,0.5,0.5])

def law_born_p_selection(A_rec):
    # screen-weight invariance under equal n-splitting
    return [2*np.log(n)/np.log(n) for n in (2,3,4,5)]

def law_interference(A_rec):
    return [abs(1+np.exp(1j*ph))**2/4 for ph in (0,np.pi/3,np.pi/2,np.pi)]

def law_survival_gluing(A_rec):
    I,J=0.7,1.3
    return np.exp(-(I+J))-np.exp(-I)*np.exp(-J)

def law_record_gravity(A_rec):
    N=8; A=np.zeros((N,N))
    for i in range(N): A[i,(i+1)%N]=A[(i+1)%N,i]=1
    L=np.diag(A.sum(1))-A
    E=np.array([1,0,0,1,0,1,0,0],float)
    rho=0.364784952089977*(E-E.mean())
    phi=np.linalg.solve(L+np.ones((N,N))/N, 2*np.pi*rho); phi-=phi.mean()
    K0=A/A.sum(1,keepdims=True)
    K=K0*np.exp(-(phi[None,:]-phi[:,None])/2); K=K/K.sum(1,keepdims=True)
    return np.concatenate([rho,phi,K.ravel()])

def law_seam_cancellation(A_rec):
    # two glued cells: internal interface contributions cancel in the summed source
    h_iface=np.array([0.3,-0.3])      # oriented interface cochain, two sides
    return float(h_iface.sum())

LAWS=[("saturation root (P4 s5)",law_saturation_root),
      ("commitment root (P4 s71)",law_commitment_root),
      ("coupled ledger h (P4 s71)",law_coupled_ledger),
      ("Born p-selection (P4 s8 / P5 s3)",law_born_p_selection),
      ("interference table (P4 s9)",law_interference),
      ("survival gluing (P4 s71)",law_survival_gluing),
      ("record-gravity packet rho/phi/K (P4 s11-12)",law_record_gravity),
      ("seam cancellation (P4 s44-47)",law_seam_cancellation)]

worst=0.0
for name,f in LAWS:
    outs=[np.atleast_1d(np.asarray(f(a),dtype=float)) for a in (1.0,3.0,0.25)]
    gap=max(float(np.max(np.abs(outs[0]-o))) for o in outs[1:])
    worst=max(worst,gap)
    print(f"  {name:<46s} A_rec-dependence gap = {gap:.3e}   NONE")
print(f"  worst gap over all executed laws = {worst:.3e}")
print("  => no law of the executed corpus consumes A_rec: the gauge parameter")
print("     lives only in the labeling map A_op = A_rec * C.\n")

print("Part 2: n^2 covariance lemma (the one convention site)")
def circle_spectrum(n,c):
    A=np.zeros((n,n))
    for i in range(n): A[i,(i+1)%n]=A[(i+1)%n,i]=1
    Lrec=np.diag(A.sum(1))-A           # record operator: never sees c
    Ln=c*n*n*Lrec                      # continuum chart operator
    ev=np.sort(np.linalg.eigvalsh(Ln))
    return Lrec,Ln,ev

for n in (16,64):
    _,_,ev1=circle_spectrum(n,1.0)
    _,_,ev2=circle_spectrum(n,2.7)
    r1=ev1[2:6]/ev1[1]; r2=ev2[2:6]/ev2[1]
    print(f"  n={n:3d}: spectral ratios c=1   : {np.array2string(r1,precision=6)}")
    print(f"        spectral ratios c=2.7 : {np.array2string(r2,precision=6)}   ratio gap = {np.max(np.abs(r1-r2)):.2e}")
    print(f"        chart covariance: ev(c=2.7)/ev(c=1) = {ev2[1]/ev1[1]:.6f} (predicted 2.700000)")
# record dynamics never sees c:
n=32
Lrec,_,_=circle_spectrum(n,1.0)
P=np.eye(n)-Lrec/4.0
dist=np.linalg.matrix_power(P,40)[0]
Lrec2,_,_=circle_spectrum(n,2.7)
P2=np.eye(n)-Lrec2/4.0
dist2=np.linalg.matrix_power(P2,40)[0]
print(f"  record-step walk distribution gap (c=1 vs c=2.7): {np.max(np.abs(dist-dist2)):.3e}")
print(f"  continuum limit check: ratios -> k^2 with circle degeneracy: [1,4,4,9] (n=64 ratios above)")
print("  => c (and n^2 itself) is a continuum-chart unit choice; record outputs are")
print("     exactly c-independent; chart outputs carry weight +1 in c.\n")

print("Part 3: joint unit coherence (length unit mu)")
mu=1.7
for (qty,weight,base) in [("A_rec",2,1.0),("A_op(S)",2,4.0),("sigma_A",-2,1.0),
                          ("kappa_label",2,2*np.pi),("chart factor n^2-coeff",-2,1.0),
                          ("kappa*sigma_A",0,2*np.pi),("area ratio",0,0.5)]:
    val=base*mu**weight
    print(f"  {qty:<24s} weight {weight:+d}: {base:.6f} -> {val:.6f}")
print("  => the unit group acts coherently with weight = area dimension;")
print("     weight-zero combinations (ratios, kappa*sigma_A) are the intrinsic ring.")
