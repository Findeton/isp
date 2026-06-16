#!/usr/bin/env python3
# Independent adversarial reproduction of Paper 50 W2: the angular departure
# q_l = r_sph(l) / r_planar(m_l) < 1, and the 4-comparator-mass test.
#
# The modular charge (numerator/denominator pairing with F(nu)) is done at
# mpmath dps-80 with a floor sweep (1e-30/45/60) -- the near-vacuum-correct
# path.  We reproduce q_1 and stress it:
#   - floor-sweep stability (is q_1 floor-LIMITED or floor-CONVERGED?)
#   - the 4 comparator masses (screen/probe/dT00-avg/u2-avg)
#   - ADVERSARIAL: a 5th comparator -- the SMALLEST centrifugal value over
#     the ball (the most generous flat-screen mass) -- does even THAT restore q->1?
import numpy as np, math, mpmath
from mpmath import mp, mpf
mp.dps = 80
half = mpf(1)/2

def chain_K(N,msq): return np.diag((2.0+msq)*np.ones(N))-np.eye(N,k=1)-np.eye(N,k=-1)
def radial_K(N,l):
    r=np.arange(1,N+1,dtype=float); K=chain_K(N,0.0); K[np.diag_indices(N)]+=l*(l+1.0)/r**2; return K
def pack_K(K):
    w2,U=np.linalg.eigh(K); w=np.sqrt(np.clip(w2,1e-18,None)); return (U*(0.5/w))@U.T,(U*(0.5*w))@U.T
def T00_profile_V(GX,GP,V,N):
    e=0.5*np.diag(GP).copy()+0.5*V*np.diag(GX); bond=np.zeros(N)
    bond[0]+=0.5*GX[0,0]; bond[-1]+=0.5*GX[-1,-1]
    for j in range(N-1):
        b=0.5*(GX[j,j]+GX[j+1,j+1]-2*GX[j,j+1]); bond[j]+=0.5*b; bond[j+1]+=0.5*b
    return e+bond
def w_ball(r,R,L): return (2*L/np.pi)*np.sin(np.pi*(R-r)/(2*L))*np.sin(np.pi*(R+r)/(2*L))/np.sin(np.pi*R/L)
def hann2_r(r0,W,N):
    r=np.arange(1,N+1,dtype=float); u=np.zeros(N); m=np.abs(r-r0)<W
    u[m]=np.cos(np.pi*(r[m]-r0)/(2*W))**2; return u/np.linalg.norm(u)
def leffV(dT):
    w=np.abs(dT); r=np.arange(1,len(dT)+1,dtype=float); s=float(w.sum())
    rb=float((r*w).sum()/s); return 2.0*np.sqrt(float(((r-rb)**2*w).sum()/s)),rb
def mp_block(Nn,jn,msq_mp):
    Bn=Nn-jn; GXB=mpmath.zeros(Bn,Bn); GPB=mpmath.zeros(Bn,Bn)
    for q in range(1,Nn+1):
        w=mpmath.sqrt(msq_mp+4*mpmath.sin(q*mpmath.pi/(2*(Nn+1)))**2)
        ph=[mpmath.sqrt(mpf(2)/(Nn+1))*mpmath.sin(q*mpmath.pi*(x+1)/(Nn+1)) for x in range(jn,Nn)]
        cx=1/(2*w); cp=w/2
        for i in range(Bn):
            for jj in range(i,Bn): GXB[i,jj]+=cx*ph[i]*ph[jj]; GPB[i,jj]+=cp*ph[i]*ph[jj]
    for i in range(Bn):
        for jj in range(i+1,Bn): GXB[jj,i]=GXB[i,jj]; GPB[jj,i]=GPB[i,jj]
    return GXB,GPB
def mp_radial_cov(N,l):
    K=mpmath.zeros(N,N)
    for x in range(N):
        K[x,x]=mpf(2)+mpf(l*(l+1))/mpf((x+1)**2)
        if x+1<N: K[x,x+1]=mpf(-1); K[x+1,x]=mpf(-1)
    E,Q=mpmath.eigsy(K); sq=[mpmath.sqrt(E[k]) for k in range(N)]
    GX=Q*mpmath.diag([1/(2*sq[k]) for k in range(N)])*Q.T
    GP=Q*mpmath.diag([sq[k]/2 for k in range(N)])*Q.T; return GX,GP
def mp_pair_blocks(GXB,GPB,uB,sector,floors=('1e-30','1e-45','1e-60')):
    Bn=GXB.rows; E,Q=mpmath.eigsy(GXB)
    Mi=Q*mpmath.diag([1/mpmath.sqrt(E[k]) for k in range(Bn)])*Q.T
    M=Q*mpmath.diag([mpmath.sqrt(E[k]) for k in range(Bn)])*Q.T
    E2,W2=mpmath.eigsy(M*GPB*M); coeff=W2.T*((Mi if sector=='x' else M)*uB); out={}
    for fls in floors:
        fl=mpf(fls); tot=mpf(0)
        for k in range(Bn):
            nu=mpmath.sqrt(E2[k])
            if nu-half<fl: nu=half+fl
            F=mpmath.log((nu+half)/(nu-half)); tot+=(F*nu if sector=='x' else F/nu)*coeff[k]**2/2
        out[float(fl)]=float(tot)
    return out
def submatrix(G,R):
    out=mpmath.zeros(R,R)
    for i in range(R):
        for j in range(R): out[i,j]=G[i,j]
    return out

N2,R2,r0w,Ww=96,24,12.0,6
Reff2=R2+0.5
r2=np.arange(1,N2+1,dtype=float)
u2=hann2_r(r0w,Ww,N2)
uB2=mpmath.matrix([mpf(float(u2[x])) for x in range(R2)])
jm2=N2-R2; u2m=u2[::-1].copy()
uB2m=mpmath.matrix([mpf(float(u2m[x])) for x in range(jm2,N2)])
wbv2=w_ball(r2[:R2],Reff2,float(N2))

print("="*72)
print("INDEPENDENT q_l: ball R=24, probe r0=12 W=6, N=96, R_eff=24.5, mp dps-80")
print("="*72)
for l in (1,2,4):
    GXl,GPl=mp_radial_cov(N2,l)
    sw_l=mp_pair_blocks(submatrix(GXl,R2),submatrix(GPl,R2),uB2,'x')
    GXlf,GPlf=pack_K(radial_K(N2,l)); Vl=l*(l+1.0)/r2**2
    dTl=(T00_profile_V(GXlf+2e-3*np.outer(u2,u2),GPlf,Vl,N2)-T00_profile_V(GXlf,GPlf,Vl,N2))/2e-3
    den_l=2*np.pi*float(np.sum(wbv2*dTl[:R2])); r_sph_l={fl:sw_l[fl]/den_l for fl in sw_l}
    lE_l,_=leffV(dTl); ml=math.sqrt(l*(l+1.0))/Reff2
    def planar_q(msq_val,fl=1e-60):
        msq=mpf(str(msq_val)); GXBm,GPBm=mp_block(N2,jm2,msq)
        sw_m=mp_pair_blocks(GXBm,GPBm,uB2m,'x')
        GXmf,GPmf=pack_K(chain_K(N2,msq_val)); Vm=msq_val*np.ones(N2)
        dTm=(T00_profile_V(GXmf+2e-3*np.outer(u2,u2),GPmf,Vm,N2)-T00_profile_V(GXmf,GPmf,Vm,N2))/2e-3
        den_m=2*np.pi*float(np.sum(wbv2*dTm[:R2])); return r_sph_l[fl]/(sw_m[fl]/den_m)
    cent=l*(l+1.0)/r2**2
    m2_dT=float(np.sum(np.abs(dTl)*cent)/np.sum(np.abs(dTl)))
    m2_u=float(np.sum((u2*u2)*cent)/np.sum(u2*u2))
    q_screen=planar_q(l*(l+1.0)/Reff2**2); q_probe=planar_q(l*(l+1.0)/r0w**2)
    q_dT=planar_q(m2_dT); q_u=planar_q(m2_u)
    # ADVERSARIAL 5th mass: smallest centrifugal value over the BALL interior
    # (most generous flat-screen, smallest mass -> largest planar response -> smallest q
    # actually; smallest mass gives the MOST generous q toward 1? test both extremes)
    m2_min=float(l*(l+1.0)/R2**2)   # smallest l(l+1)/r^2 over r in [1,R] is at r=R
    m2_max=float(l*(l+1.0)/1.0**2)  # largest at r=1
    q_minmass=planar_q(m2_min); q_maxmass=planar_q(m2_max)
    # floor sweep on q(screen)
    qs={fl:r_sph_l[fl]/(planar_q_full:=None or 0) for fl in []}  # placeholder
    # explicit floor sweep
    def planar_q_fl(msq_val):
        msq=mpf(str(msq_val)); GXBm,GPBm=mp_block(N2,jm2,msq)
        sw_m=mp_pair_blocks(GXBm,GPBm,uB2m,'x')
        GXmf,GPmf=pack_K(chain_K(N2,msq_val)); Vm=msq_val*np.ones(N2)
        dTm=(T00_profile_V(GXmf+2e-3*np.outer(u2,u2),GPmf,Vm,N2)-T00_profile_V(GXmf,GPmf,Vm,N2))/2e-3
        den_m=2*np.pi*float(np.sum(wbv2*dTm[:R2]))
        return {fl:r_sph_l[fl]/(sw_m[fl]/den_m) for fl in sw_m}
    qfl=planar_q_fl(l*(l+1.0)/Reff2**2)
    print(f"\n  l={l} (m_l*l_E={ml*lE_l:.2f}{' IN-WINDOW' if ml*lE_l<0.5 else ' out-of-window'}): "
          f"r_sph={r_sph_l[1e-60]:.4f}")
    print(f"    q(screen/probe/dT00-avg/u2-avg) = {q_screen:.4f}/{q_probe:.4f}/{q_dT:.4f}/{q_u:.4f}")
    print(f"    range over those 4 = [{min(q_screen,q_probe,q_dT,q_u):.4f}, {max(q_screen,q_probe,q_dT,q_u):.4f}]")
    print(f"    ADVERSARIAL extra masses: q(min-cent @r=R)={q_minmass:.4f}  q(max-cent @r=1)={q_maxmass:.4f}")
    print(f"    q(screen) floor sweep 1e-30/45/60 = {qfl[1e-30]:.4f}/{qfl[1e-45]:.4f}/{qfl[1e-60]:.4f} "
          f"(converged={abs(qfl[1e-60]/qfl[1e-45]-1)<1e-4})")
    allq=[q_screen,q_probe,q_dT,q_u,q_minmass,q_maxmass]
    print(f"    => MAX q over ALL 6 masses = {max(allq):.4f} (restores universality if >0.97: {max(allq)>0.97})")
