#!/usr/bin/env python3
# CRITICAL ADVERSARIAL TEST: the float64 entropy is NOT float-safe at high l
# (rel error 5.6e-2 at l=2560).  The l_c-sweep to 5120 is the load-bearing
# convergence claim.  Does the float64 error contaminate:
#   (1) the per-l contribution (2l+1)*S_l that builds S_ball, and
#   (2) the resulting area coefficient a and its 'convergence'?
#
# We compute (2l+1)*S_l at high l in BOTH float64 and mp dps-80 and compare
# the WEIGHTED contribution (what actually enters the area fit), and we
# rebuild the area coefficient's high-l increments with mp to see if the
# 'geometric convergence to 0.295' is real or a float artifact.
import numpy as np, mpmath as mp, time
mp.mp.dps = 80
half = mp.mpf(1)/2
t0=time.time()

def chain_K(N,msq):
    return np.diag((2.0+msq)*np.ones(N)) - np.eye(N,k=1) - np.eye(N,k=-1)
def radial_K(N,l):
    r=np.arange(1,N+1,dtype=float); K=chain_K(N,0.0); K[np.diag_indices(N)]+=l*(l+1.0)/r**2; return K
def pack_K(K):
    w2,U=np.linalg.eigh(K); w=np.sqrt(np.clip(w2,1e-18,None)); return (U*(0.5/w))@U.T,(U*(0.5*w))@U.T
def S_block_f(GX,GP,R,clip=1e-12):
    e2,V=np.linalg.eigh(GX[:R,:R]); M=(V*np.sqrt(np.clip(e2,1e-14,None)))@V.T
    w2_,_=np.linalg.eigh(M@GP[:R,:R]@M); nu=np.sqrt(np.clip(w2_,0.25+clip,None))
    return float(np.sum((nu+0.5)*np.log(nu+0.5)-(nu-0.5)*np.log(nu-0.5)))
def S_l_f(N,l,R):
    GX,GP=pack_K(radial_K(N,l)); return S_block_f(GX,GP,R)

def S_l_mp(N,l,R):
    K=mp.zeros(N,N)
    for i in range(N):
        K[i,i]=mp.mpf(2)+mp.mpf(l*(l+1))/mp.mpf(i+1)**2
        if i+1<N: K[i,i+1]=-1; K[i+1,i]=-1
    w2,U=mp.eigsy(K)
    GX=U*mp.diag(mp.matrix([half/mp.sqrt(w2[i]) for i in range(N)]))*U.T
    GP=U*mp.diag(mp.matrix([half*mp.sqrt(w2[i]) for i in range(N)]))*U.T
    GXb=mp.matrix([[GX[a,b] for b in range(R)] for a in range(R)])
    GPb=mp.matrix([[GP[a,b] for b in range(R)] for a in range(R)])
    e2,V=mp.eigsy(GXb); M=V*mp.diag(mp.matrix([mp.sqrt(e2[i]) for i in range(R)]))*V.T
    w2b,_=mp.eigsy(M*GPb*M); S=mp.mpf(0)
    for i in range(R):
        nu=mp.sqrt(w2b[i]); d=nu-half
        S+=(nu+half)*mp.log(nu+half)-(d*mp.log(d) if d>0 else mp.mpf(0))
    return float(S)

N=96
print("="*72)
print("WEIGHTED CONTRIBUTION (2l+1)*S_l at high l: float64 vs mp dps-80")
print("Rs used in the area fit: 8,12,16,20,24.  Show R=24 (largest weight).")
print("="*72)
R=24
print(f"  {'l':>5} {'(2l+1)Sf':>14} {'(2l+1)Smp':>14} {'rel':>9} {'abs diff':>11}")
tot_f=0.0; tot_mp=0.0
for l in [160,320,640,1280,2560,5120]:
    sf=S_l_f(N,l,R); sm=S_l_mp(N,l,R)
    cf=(2*l+1)*sf; cm=(2*l+1)*sm
    print(f"  {l:>5} {cf:>14.6e} {cm:>14.6e} {abs(cf-cm)/abs(cm):>9.1e} {cf-cm:>+11.2e} [{time.time()-t0:.0f}s]")

print()
print("="*72)
print("CRITICAL: rebuild area-coeff high-l increments with mp (the tail that")
print("the 'geometric convergence to 0.295' rests on).  da_lc = a(2lc)-a(lc).")
print("We compute the INCREMENT to S_ball from l in (lc, 2lc] for each R, mp.")
print("="*72)
Rs=(8,12,16,20,24)
Av=np.vstack([np.array(Rs,float)**2,np.array(Rs,float),np.ones(len(Rs))]).T
# We need cumulative S_ball at l_c = 640,1280,2560 in mp.  That's expensive
# (mp eigsy per l).  Instead compute the BLOCK increments d_lc = sum_{l in window}
# (2l+1) S_l for windows [641,1280],[1281,2560] -- subsample with stride to
# bound cost, then compare float vs mp on the SAME subsample (apples-to-apples).
def block_sum(lo,hi,stride,fn):
    """sum (2l+1)S_l over l in [lo,hi] stride 'stride', scaled by stride
    (Riemann estimate of the true block sum)."""
    s={R:0.0 for R in Rs}
    for l in range(lo,hi+1,stride):
        for R in Rs:
            s[R]+=stride*(2*l+1)*fn(N,l,R)
    return s
# windows that build the last two increments
for (lo,hi,stride) in [(641,1280,64),(1281,2560,128),(2561,5120,256)]:
    sf=block_sum(lo,hi,stride,S_l_f)
    sm=block_sum(lo,hi,stride,S_l_mp)
    af=np.linalg.lstsq(Av,np.array([sf[R] for R in Rs]),rcond=None)[0][0]
    am=np.linalg.lstsq(Av,np.array([sm[R] for R in Rs]),rcond=None)[0][0]
    print(f"  window ({lo:>4},{hi:>4}) stride {stride:>3}: da_float={af:>+.3e} "
          f"da_mp={am:>+.3e} rel={abs(af-am)/abs(am) if am!=0 else 0:.1e} [{time.time()-t0:.0f}s]")
print("\n  -> if da_float and da_mp agree, the convergence is real despite the")
print("     per-mode float error (cancellation in the (2l+1)-weighted block);")
print("     if they DIVERGE, the 0.295 convergence is partly a float artifact.")
