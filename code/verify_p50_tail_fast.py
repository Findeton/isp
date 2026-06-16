#!/usr/bin/env python3
# FAST targeted version: quantify whether float64's high-l entropy error
# contaminates the area-coefficient tail increment (the convergence claim).
# Key idea: the last area increment (l_c 2560->5120) was +2.74e-4 in a.
# We compute the float-vs-mp ABSOLUTE error in the area coefficient
# contributed by the l-window (2561..5120), sampled, to see if it is
# comparable to 2.74e-4 (which would mean the convergence is float-faked)
# or far below it (convergence is real).
import numpy as np, mpmath as mp, time, sys
mp.mp.dps = 80
half = mp.mpf(1)/2
t0=time.time()
def chain_K(N): return np.diag(2.0*np.ones(N))-np.eye(N,k=1)-np.eye(N,k=-1)
def radial_K(N,l):
    r=np.arange(1,N+1,dtype=float); K=chain_K(N); K[np.diag_indices(N)]+=l*(l+1.0)/r**2; return K
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

N=96; Rs=(8,12,16,20,24)
Av=np.vstack([np.array(Rs,float)**2,np.array(Rs,float),np.ones(len(Rs))]).T
# Riemann block-estimate of the area-coeff increment from window (lo,hi]:
# da = a-fit of [ sum_{l in window, stride} stride*(2l+1)*S_l(R) ] over R.
def da_window(lo,hi,stride,fn,tag):
    contrib={R:0.0 for R in Rs}
    ls=list(range(lo,hi+1,stride))
    for l in ls:
        for R in Rs:
            contrib[R]+=stride*(2*l+1)*fn(N,l,R)
        print(f"    [{tag}] l={l} done [{time.time()-t0:.0f}s]", flush=True)
    return np.linalg.lstsq(Av,np.array([contrib[R] for R in Rs]),rcond=None)[0][0]

print("WINDOW (2561,5120) stride 512 : area-coeff increment, float vs mp", flush=True)
af=da_window(2561,5120,512,S_l_f,"float")
print(f"  da_float (window 2561-5120, stride 512) = {af:+.4e}", flush=True)
am=da_window(2561,5120,512,S_l_mp,"mp80")
print(f"  da_mp    (window 2561-5120, stride 512) = {am:+.4e}", flush=True)
print(f"  ABS DIFF in area-coeff tail increment = {abs(af-am):.2e}", flush=True)
print(f"  (compare to the reported last increment 2.74e-4 and the U_G-relevant", flush=True)
print(f"   a-precision; if abs diff << 2.7e-4, the convergence is NOT float-faked)", flush=True)
