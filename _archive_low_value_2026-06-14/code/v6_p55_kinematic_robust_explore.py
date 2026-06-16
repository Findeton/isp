#!/usr/bin/env python3
# =====================================================================
# P55 FRONT B -- ROBUST observable (float64): the l=2 angular Fourier
# component of delta-S over a RING of disk positions.
#
# WHY: the Hessian-of-S over the disk CENTER is ill-defined on a lattice
# (S(center) is a STEP function -- shifting a discrete disk's membership
# jumps), so its second difference is h-dependent garbage (verified: the
# trace channel flips sign with h).  A WELL-DEFINED spin-2 observable:
#   delta S(phi) = S_perturbed(disk at angle phi) - S_vacuum(disk at phi),
# for fixed-size disks centered on a RING of radius rho around the source.
# Each disk's entropy is well-defined; delta S(phi) is smooth in phi.
# Its m=2 (cos2phi) Fourier component = the SPIN-2 response; m=0 = the
# monopole/trace.  A traceless (cos2theta) source -> m=2 lights up; a
# trace (isotropic) source -> only m=0.
#
# HONEST CAVEAT (the tautology the verdict must clear): a quadrupolar
# source trivially gives a quadrupolar delta-S.  The LOAD-BEARING content
# is NOT "m=2 exists" but (i) refinement stability of the dimensionless
# coupling, (ii) the coupling matching the universal G=1/(4 nu), (iii) the
# first-law structure delta S = delta <K>.  This script establishes the
# robust SIGNAL; the coupling/refinement/first-law tests follow.
# float64 (entropy float-safe); mp confirm at an anchor next.  No RNG.
# =====================================================================
import numpy as np
np.set_printoptions(linewidth=160, suppress=True)
def hr(s): print("\n"+"="*70+"\n"+s+"\n"+"="*70, flush=True)
print("#"*70); print("# P55 FRONT B -- ROBUST spin-2 observable (angular Fourier of dS)"); print("#"*70)

def S_of_nu(nu):
    nu = np.clip(np.asarray(nu, float), 0.5+1e-15, None)
    a = nu+0.5; b = nu-0.5
    return np.sum(a*np.log(a) - np.where(b > 1e-300, b*np.log(b), 0.0))

def lap2d(L, msq, sx=None, sy=None):
    n = L*L; K = np.zeros((n, n))
    def ix(i, j): return i*L+j
    if sx is None: sx = np.ones((L, L))
    if sy is None: sy = np.ones((L, L))
    for i in range(L):
        for j in range(L):
            a = ix(i, j); diag = msq
            for di, dj, s in ((1,0,sx),(-1,0,sx),(0,1,sy),(0,-1,sy)):
                ii, jj = i+di, j+dj
                if 0 <= ii < L and 0 <= jj < L:
                    w = 0.5*(s[i, j]+s[ii, jj]); K[a, ix(ii, jj)] = -w; diag += w
            K[a, a] = diag
    return K

def covs_from_K(K):
    w, V = np.linalg.eigh(K); w = np.clip(w, 1e-300, None)
    return 0.5*((V/np.sqrt(w)) @ V.T), 0.5*((V*np.sqrt(w)) @ V.T)

def region_entropy(GX, GP, idx):
    XA = GX[np.ix_(idx, idx)]; PA = GP[np.ix_(idx, idx)]
    ev = np.linalg.eigvals(XA @ PA)
    return S_of_nu(np.sqrt(np.abs(ev.real)))

L = 26; ctr = (L-1)/2.0
coords = np.array([[i, j] for i in range(L) for j in range(L)], float)
ii_grid, jj_grid = np.meshgrid(np.arange(L), np.arange(L), indexing='ij')
RAD = np.hypot(ii_grid-ctr, jj_grid-ctr)
WIN = np.exp(-((RAD-6.0)**2)/(2*3.0**2))

def perturbed_K(eps, kind):
    if kind == "trace": sx = 1.0+eps*WIN; sy = 1.0+eps*WIN
    elif kind == "quad": sx = 1.0+eps*WIN; sy = 1.0-eps*WIN
    else: sx = np.ones((L, L)); sy = np.ones((L, L))
    return lap2d(L, 1e-4, sx, sy)

def disk_idx(cx, cy, R):
    d2 = (coords[:, 0]-cx)**2 + (coords[:, 1]-cy)**2
    return list(np.where(d2 <= R*R)[0])

GX0, GP0 = covs_from_K(perturbed_K(0.0, "vac"))

def dS_ring(eps, kind, rho=6.0, R0=3.0, nphi=24):
    GX, GP = covs_from_K(perturbed_K(eps, kind))
    phis = np.linspace(0, 2*np.pi, nphi, endpoint=False)
    dS = np.zeros(nphi)
    for k, ph in enumerate(phis):
        cx = ctr+rho*np.cos(ph); cy = ctr+rho*np.sin(ph)
        idx = disk_idx(cx, cy, R0)
        dS[k] = region_entropy(GX, GP, idx) - region_entropy(GX0, GP0, idx)
    fm = np.fft.fft(dS)/nphi
    return dS, np.abs(fm)

# =====================================================================
hr("delta-S(phi) angular Fourier content: trace vs traceless source")
# =====================================================================
print(f"  {'eps':>6} {'src':>7} {'m=0 (mono)':>12} {'m=2 (spin2)':>12} {'m=4':>11} {'m2/m0':>8}")
rows = []
for eps in (0.05, 0.10, 0.20):
    for kind in ("trace", "quad"):
        dS, mags = dS_ring(eps, kind)
        rows.append((eps, kind, mags[0], mags[2], mags[4]))
        print(f"  {eps:6.2f} {kind:>7} {mags[0]:12.4e} {mags[2]:12.4e} {mags[4]:11.3e} {mags[2]/max(mags[0],1e-30):8.2f}")

# =====================================================================
hr("SELECTIVITY + LINEARITY of the robust m=2 channel")
# =====================================================================
q2 = {e: m2 for (e, k, m0, m2, m4) in rows if k == "quad"}
t2 = {e: m2 for (e, k, m0, m2, m4) in rows if k == "trace"}
print(f"  m=2 (spin-2) amplitude of delta-S:")
for e in (0.05, 0.10, 0.20):
    print(f"    eps={e}: QUAD src m=2 = {q2[e]:.4e}   TRACE src m=2 = {t2[e]:.4e}   quad/trace = {q2[e]/max(t2[e],1e-30):.1f}")
epss = np.array([0.05, 0.10, 0.20]); qv = np.array([q2[e] for e in epss])
slope = np.polyfit(np.log(epss), np.log(qv), 1)[0]
sel = np.mean([q2[e]/max(t2[e], 1e-30) for e in epss])
print(f"\n  linearity exponent d log(m2)/d log(eps) = {slope:.2f}  (~1 => linear FGHMVR)")
print(f"  selectivity (quad-driven / trace-driven m=2) = {sel:.1f}")
print(f"  -> the spin-2 signal SURVIVES the well-defined (no-Hessian) observable: {slope>0.7 and sel>3}")
print(f"  NOTE: m=2-from-quad is partly EXPECTED (quad source -> quad response).")
print(f"        The verdict rests on coupling=G=1/(4nu) + refinement + first-law,")
print(f"        NOT on the mere existence of m=2.  Those are the next tests.")
