#!/usr/bin/env python3
# Independent adversarial verification of Paper 50's float-safety claim
# and the basic partial-wave entropy machinery.
#
# Claim under test: the entanglement entropy
#   S = sum[(nu+1/2)log(nu+1/2) - (nu-1/2)log(nu-1/2)]
# is FLOAT-SAFE (no near-vacuum divergence as nu->1/2), so the l_c-sweep
# can run in float64 even though the modular kernel F(nu) is NOT float-safe.
#
# We compute S_l(N,l,R) in BOTH float64 and mpmath dps=80 and compare.
import numpy as np
import mpmath as mp
mp.mp.dps = 80

# ---------- float64 ----------
def chain_K(N):
    return np.diag(2.0*np.ones(N)) - np.eye(N, k=1) - np.eye(N, k=-1)
def radial_K(N, l):
    r = np.arange(1, N+1, dtype=float)
    K = chain_K(N); K[np.diag_indices(N)] += l*(l+1.0)/r**2
    return K
def pack_K(K):
    w2, U = np.linalg.eigh(K); w = np.sqrt(np.clip(w2, 1e-18, None))
    return (U*(0.5/w))@U.T, (U*(0.5*w))@U.T
def S_block_f(GX, GP, R, clip):
    e2, V = np.linalg.eigh(GX[:R,:R])
    M = (V*np.sqrt(np.clip(e2,1e-14,None)))@V.T
    w2_,_ = np.linalg.eigh(M@GP[:R,:R]@M)
    nu = np.sqrt(np.clip(w2_, 0.25+clip, None))
    return float(np.sum((nu+0.5)*np.log(nu+0.5)-(nu-0.5)*np.log(nu-0.5))), nu
def S_l_f(N, l, R, clip=1e-12):
    GX,GP = pack_K(radial_K(N,l)); return S_block_f(GX,GP,R,clip)

# ---------- mp dps-80 ----------
def S_l_mp(N, l, R, floor=mp.mpf(10)**-70):
    half = mp.mpf(1)/2
    K = mp.zeros(N,N)
    for i in range(N):
        K[i,i] = mp.mpf(2) + mp.mpf(l*(l+1))/mp.mpf(i+1)**2
        if i+1<N: K[i,i+1]=-1; K[i+1,i]=-1
    w2,U = mp.eigsy(K)
    GX = U*mp.diag(mp.matrix([half/mp.sqrt(w2[i]) for i in range(N)]))*U.T
    GP = U*mp.diag(mp.matrix([half*mp.sqrt(w2[i]) for i in range(N)]))*U.T
    GXb = mp.matrix([[GX[a,b] for b in range(R)] for a in range(R)])
    GPb = mp.matrix([[GP[a,b] for b in range(R)] for a in range(R)])
    e2,V = mp.eigsy(GXb)
    M = V*mp.diag(mp.matrix([mp.sqrt(e2[i]) for i in range(R)]))*V.T
    w2b,_ = mp.eigsy(M*GPb*M)
    S = mp.mpf(0); nus=[]
    for i in range(R):
        nu = mp.sqrt(w2b[i]); nus.append(nu)
        # no clip in mp -- the (nu-1/2)log(nu-1/2) term should vanish if nu->1/2
        d = nu-half
        term_minus = d*mp.log(d) if d>0 else mp.mpf(0)
        S += (nu+half)*mp.log(nu+half) - term_minus
    return S, nus

print("="*72)
print("ADVERSARIAL FLOAT-SAFETY TEST: S_l float64 vs mp dps-80")
print("="*72)
N=96
for (l,R) in [(0,24),(0,8),(10,24),(40,16),(80,8),(160,8)]:
    sf,nuf = S_l_f(N,l,R)
    sm,num = S_l_mp(N,l,R)
    smf = float(sm)
    # smallest symplectic eigenvalue: how close to the 1/2 vacuum floor?
    nmin = float(min(num))
    rel = abs(sf-smf)/abs(smf) if smf!=0 else 0.0
    print(f"  l={l:3d} R={R:2d}: float={sf:.12f} mp80={smf:.12f} rel={rel:.2e}  nu_min={nmin:.6f} (nu-1/2={nmin-0.5:.2e})")

print()
print("="*72)
print("ADVERSARIAL: does the float64 CLIP (nu>=1/2+1e-12) bias S vs unclipped mp?")
print("="*72)
# The float code clips nu to >= 0.5+1e-12. The mp code does NOT clip.
# If near-vacuum modes (nu very near 1/2) carry weight, clip biases S.
# Test at high l where the radial barrier pushes modes toward vacuum.
for (l,R) in [(0,24),(160,24),(640,24),(1280,24),(2560,24)]:
    sf,nuf = S_l_f(N,l,R)
    sm,num = S_l_mp(N,l,R)
    nmin = float(min(num))
    rel = abs(sf-float(sm))/abs(float(sm)) if float(sm)!=0 else 0.0
    # how many modes within 1e-10 of the floor?
    nclose = int(np.sum(np.array([float(x)-0.5 for x in num])<1e-10))
    print(f"  l={l:4d} R={R}: S_float={sf:.3e} S_mp={float(sm):.3e} rel={rel:.2e} nu_min-1/2={nmin-0.5:.2e} modes<1e-10:{nclose}")
