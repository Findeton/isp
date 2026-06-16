#!/usr/bin/env python3
# Independent adversarial reproduction of Paper 50 Result 3:
#  - the l_c-converged ball area coefficient a -> Srednicki 0.295
#  - nu_sph = a/(4pi), nu_planar via k-integral, U_G = nu_sph/nu_planar
#
# ADVERSARIAL EXTRAS the corpus did not print:
#  (A) does 'a' depend on the R-grid / box N?  (universality of the constant)
#  (B) the geometric-Richardson tail: is the ratio really converging?
#  (C) does U_G ~ 1 survive a DIFFERENT nu_planar definition (the real test
#      of "ratio fixed" -- both legs must be the same regulator)?
import numpy as np

def chain_K(N, msq):
    return np.diag((2.0+msq)*np.ones(N)) - np.eye(N,k=1) - np.eye(N,k=-1)
def radial_K(N, l):
    r = np.arange(1,N+1,dtype=float); K = chain_K(N,0.0)
    K[np.diag_indices(N)] += l*(l+1.0)/r**2; return K
def pack_K(K):
    w2,U = np.linalg.eigh(K); w = np.sqrt(np.clip(w2,1e-18,None))
    return (U*(0.5/w))@U.T, (U*(0.5*w))@U.T
def S_block(GX,GP,R,clip=1e-12):
    e2,V = np.linalg.eigh(GX[:R,:R])
    M = (V*np.sqrt(np.clip(e2,1e-14,None)))@V.T
    w2_,_ = np.linalg.eigh(M@GP[:R,:R]@M)
    nu = np.sqrt(np.clip(w2_,0.25+clip,None))
    return float(np.sum((nu+0.5)*np.log(nu+0.5)-(nu-0.5)*np.log(nu-0.5)))
def S_l(N,l,R):
    GX,GP = pack_K(radial_K(N,l)); return S_block(GX,GP,R)

def area_coeff(N, Rs, l_max):
    Av = np.vstack([np.array(Rs,float)**2, np.array(Rs,float), np.ones(len(Rs))]).T
    cum = {R: np.zeros(l_max+1) for R in Rs}
    for R in Rs:
        run = 0.0
        for l in range(l_max+1):
            run += (2*l+1)*S_l(N,l,R); cum[R][l]=run
    def a_at(lc):
        Sb = np.array([cum[R][lc] for R in Rs])
        return np.linalg.lstsq(Av, Sb, rcond=None)[0]
    return a_at, cum

print("="*72)
print("INDEPENDENT REPRO: ball area coefficient a (l_c sweep), N=96, Rs=(8..24)")
print("="*72)
N=96; Rs=(8,12,16,20,24); l_max=5120
a_at, cum = area_coeff(N, Rs, l_max)
lcs=[40,80,160,320,640,1280,2560,5120]
avals=[a_at(lc)[0] for lc in lcs]
incs=[avals[i]-avals[i-1] for i in range(1,len(avals))]
print(f"  {'l_c':>5} {'a':>10} {'da':>12} {'ratio':>7}")
for i,lc in enumerate(lcs):
    da = incs[i-1] if i>0 else float('nan')
    rat = incs[i-1]/incs[i-2] if i>1 else float('nan')
    print(f"  {lc:>5} {avals[i]:>10.6f} {da:>+12.2e} {rat:>7.3f}")
r_geo = incs[-1]/incs[-2]
a_inf = avals[-1] + incs[-1]*r_geo/(1-r_geo)
print(f"  a(5120)={avals[-1]:.6f}  last inc={abs(incs[-1]):.2e}  geo ratio={r_geo:.3f}")
print(f"  a_inf (Richardson) = {a_inf:.6f}   (Srednicki 0.295)")
nu_sph_expl = avals[-1]/(4*np.pi); nu_sph_rich = a_inf/(4*np.pi)
print(f"  nu_sph: explicit={nu_sph_expl:.6f}  Richardson={nu_sph_rich:.6f}")

print()
print("="*72)
print("ADVERSARIAL (A): does 'a' depend on the R-grid?  (universality of a)")
print("="*72)
# reuse cached cum at l_max for several R-subsets/grids
def a_from_grid(Rs_sub, lc):
    Av = np.vstack([np.array(Rs_sub,float)**2, np.array(Rs_sub,float), np.ones(len(Rs_sub))]).T
    Sb = np.array([cum[R][lc] for R in Rs_sub])
    return np.linalg.lstsq(Av, Sb, rcond=None)[0][0]
for grid in [(8,12,16,20,24),(12,16,20,24),(8,16,24),(16,20,24),(8,12,16)]:
    print(f"  Rs={grid}: a(5120)={a_from_grid(grid,5120):.6f}")

print()
print("="*72)
print("ADVERSARIAL (B): box-size dependence of a (N=96 vs larger N)")
print("="*72)
for Nb in [96,128]:
    a_at_b, _ = area_coeff(Nb, (8,12,16,20,24), 2560)
    ab = a_at_b(2560)[0]
    print(f"  N={Nb}: a(l_c=2560)={ab:.6f}  nu_sph={ab/(4*np.pi):.6f}")

print()
print("="*72)
print("nu_planar (k-integral on the SAME chain) + U_G + kmax systematic")
print("="*72)
w2p,Up = np.linalg.eigh(chain_K(N,0.0))
def S_pl_k2(k2,R):
    w = np.sqrt(np.clip(w2p+k2,1e-18,None))
    return S_block((Up*(0.5/w))@Up.T,(Up*(0.5*w))@Up.T,R)
def nu_planar_kmax(R,kmax):
    ks = np.arange(0.0025,kmax,0.005)
    Sk = np.array([S_pl_k2(k*k,R) for k in ks]); I = float(np.trapz(ks*Sk,ks))
    m = ks>kmax/2.0
    A2 = np.vstack([1/ks[m]**4, np.log(ks[m])/ks[m]**4]).T
    cf,*_ = np.linalg.lstsq(A2,Sk[m],rcond=None)
    kt = np.arange(kmax,4000.0,0.05); I += float(np.trapz(kt*(cf[0]+cf[1]*np.log(kt))/kt**4,kt))
    return I/(2*np.pi)
print(f"  {'kmax':>5} {'nu_planar':>10} {'U_G(rich)':>10} {'U_G(expl)':>10}")
ugs=[]
for kmax in (10,12,16,20,40):
    npl = nu_planar_kmax(24,float(kmax)); ugs.append(nu_sph_rich/npl)
    print(f"  {kmax:>5} {npl:>10.6f} {nu_sph_rich/npl:>10.5f} {nu_sph_expl/npl:>10.5f}")
print(f"  U_G band (kmax) = {max(ugs)-min(ugs):.1e}; straddles 1 = {min(ugs)<1<max(ugs)}")
