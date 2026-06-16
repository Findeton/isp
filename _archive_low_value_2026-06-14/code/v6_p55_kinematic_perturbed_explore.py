#!/usr/bin/env python3
# =====================================================================
# P55 FRONT B -- THE DECISIVE TEST (float64 explore): does the EMERGENT
# kinematic geometry carry the GRAVITON when SOURCED?
#
# The vacuum kinematic geometry is maximally symmetric (spin-2 channel at
# the floor) -- expected, not the test.  The genuine, non-tautological
# test is the FGHMVR LINEAR RESPONSE: perturb the record state by a
# localized stress and ask whether the kinematic curvature's TRACELESS
# (spin-2) channel responds.  The discriminating contrast:
#   - a PURE-TRACE (isotropic) source should move the TRACE channel
#     (scale / central charge) and leave the traceless channel at floor;
#   - a TRACELESS (cos2theta quadrupolar) source -- IF the emergent
#     geometry carries spin-2 -- should light up the TRACELESS channel,
#     linearly in the source amplitude, and NOT under the trace source.
# That selectivity (traceless-out iff traceless-in, linear, above floor)
# is the graviton signature.  Its ABSENCE (traceless channel stays at
# floor even under a traceless source) is KINEMATIC-BLIND.
#
# This is NOT a P53-style tautology: a cos2theta state perturbation has
# a generic (sym . sym != 0) overlap with the traceless curvature channel
# -- a null is contingent and load-bearing.
#
# Source = a localized SYMPLECTIC SQUEEZING of the Gaussian covariance:
#   x_i -> e^{r_i} x_i, p_i -> e^{-r_i} p_i   (a valid pure-state Bogoliubov),
#   r_i = eps * window(radius) * profile(angle),
#   profile = 1 (trace source)  OR  cos(2 theta_i) (traceless source).
# float64 (entropy float-safe); mp dps-80 confirm of the verdict ratios next.
# =====================================================================
import numpy as np
np.set_printoptions(linewidth=160, suppress=True)
def hr(s): print("\n"+"="*70+"\n"+s+"\n"+"="*70, flush=True)
print("#"*70); print("# P55 FRONT B -- DECISIVE perturbed-response spin-2 test (float64)"); print("#"*70)

def S_of_nu(nu):
    nu = np.clip(np.asarray(nu, float), 0.5+1e-15, None)
    a = nu+0.5; b = nu-0.5
    return np.sum(a*np.log(a) - np.where(b > 1e-300, b*np.log(b), 0.0))

def lap2d(L, msq, sx=None, sy=None):
    # anisotropic Laplacian: x-bonds scaled by sx(site), y-bonds by sy(site).
    # sx=sy=1 -> isotropic vacuum.  sx=1+s, sy=1-s (window) -> TRACELESS shear.
    # sx=sy=1+s -> TRACE (isotropic/conformal) perturbation.
    n = L*L; K = np.zeros((n, n))
    def ix(i, j): return i*L+j
    if sx is None: sx = np.ones((L, L))
    if sy is None: sy = np.ones((L, L))
    for i in range(L):
        for j in range(L):
            a = ix(i, j)
            diag = msq
            for di, dj, s in ((1,0,sx),(-1,0,sx),(0,1,sy),(0,-1,sy)):
                ii, jj = i+di, j+dj
                if 0 <= ii < L and 0 <= jj < L:
                    # symmetric bond weight = average of the two endpoints' scale
                    w = 0.5*(s[i, j]+s[ii, jj])
                    K[a, ix(ii, jj)] = -w; diag += w
            K[a, a] = diag
    return K

def covs_from_K(K):
    w, V = np.linalg.eigh(K); w = np.clip(w, 1e-300, None)
    Khalf = (V*np.sqrt(w)) @ V.T; Kmhalf = (V/np.sqrt(w)) @ V.T
    return 0.5*Kmhalf, 0.5*Khalf

def region_entropy(GX, GP, idx):
    XA = GX[np.ix_(idx, idx)]; PA = GP[np.ix_(idx, idx)]
    ev = np.linalg.eigvals(XA @ PA)
    return S_of_nu(np.sqrt(np.abs(ev.real)))

# ---- lattice + vacuum covariances ----
L = 22; K2 = lap2d(L, 1e-4); GX0, GP0 = covs_from_K(K2)
ctr = (L-1)/2.0
coords = np.array([[i, j] for i in range(L) for j in range(L)], float)
ii_grid, jj_grid = np.meshgrid(np.arange(L), np.arange(L), indexing='ij')
RAD = np.hypot(ii_grid-ctr, jj_grid-ctr)
WIN = np.exp(-((RAD-5.0)**2)/(2*3.0**2))   # localized window, mid-lattice

def disk_idx(cx, cy, R):
    d2 = (coords[:, 0]-cx)**2 + (coords[:, 1]-cy)**2
    return list(np.where(d2 <= R*R)[0])

def perturbed_covs(eps, kind):
    # GENUINE state perturbation: ground state of an anisotropically-modulated
    # Laplacian (NOT a local unitary -> entanglement actually changes).
    if kind == "trace":      # isotropic conformal-factor (pure-trace) shear
        sx = 1.0+eps*WIN; sy = 1.0+eps*WIN
    elif kind == "quad":     # TRACELESS shear: strengthen x-bonds, weaken y-bonds
        sx = 1.0+eps*WIN; sy = 1.0-eps*WIN
    else:                    # vacuum
        sx = np.ones((L, L)); sy = np.ones((L, L))
    K = lap2d(L, 1e-4, sx, sy)
    return covs_from_K(K)

def spin2_of_state(GX, GP, R0=5.0, hh=1.0):
    # kinematic metric = Hessian of S over (cx,cy) at fixed R0; extract
    # (cx,cy)-plane trace and traceless (spin-2) parts.
    def S(cx, cy): return region_entropy(GX, GP, disk_idx(cx, cy, R0))
    c = ctr
    Sxx = (S(c+hh, c)-2*S(c, c)+S(c-hh, c))/hh**2
    Syy = (S(c, c+hh)-2*S(c, c)+S(c, c-hh))/hh**2
    Sxy = (S(c+hh, c+hh)-S(c+hh, c-hh)-S(c-hh, c+hh)+S(c-hh, c-hh))/(4*hh**2)
    tr = Sxx+Syy
    tl = np.array([Sxx-Syy, 2*Sxy])
    return tr, tl, np.linalg.norm(tl)

# =====================================================================
hr("baseline + the two sources (eps sweep): trace vs traceless response")
# =====================================================================
tr0, tl0, n0 = spin2_of_state(GX0, GP0)
print(f"  VACUUM: trace={tr0:.4e}  |traceless|={n0:.3e}  spin2_frac={n0/abs(tr0):.3e}")
print()
print(f"  {'eps':>6} {'src':>9} {'trace':>12} {'|traceless|':>12} {'spin2_frac':>11} {'d|tl|/floor':>11}")
rows = []
for eps in (0.05, 0.10, 0.20):
    for name in ("trace", "quad"):
        GX, GP = perturbed_covs(eps, name)
        tr, tl, ntl = spin2_of_state(GX, GP)
        rows.append((eps, name, tr, ntl, ntl/abs(tr), ntl/max(n0, 1e-30)))
        print(f"  {eps:6.2f} {name:>9} {tr:12.4e} {ntl:12.4e} {ntl/abs(tr):11.3e} {ntl/max(n0,1e-30):11.2f}")

# =====================================================================
hr("SELECTIVITY + LINEARITY: the graviton signature")
# =====================================================================
# does the TRACELESS channel respond to the QUAD source and NOT the trace source?
q = {eps: ntl for (eps, name, tr, ntl, fr, rr) in rows if name == "quad"}
t = {eps: ntl for (eps, name, tr, ntl, fr, rr) in rows if name == "trace"}
print(f"  traceless-channel output |traceless|:")
for eps in (0.05, 0.10, 0.20):
    print(f"    eps={eps}: under QUAD src = {q[eps]:.4e}   under TRACE src = {t[eps]:.4e}   ratio quad/trace = {q[eps]/max(t[eps],1e-30):.2f}")
# selectivity: quad should drive traceless much more than trace does
sel = np.mean([q[e]/max(t[e], 1e-30) for e in (0.05, 0.10, 0.20)])
# linearity of the quad response in eps (slope on log-log ~ 1 if linear)
epss = np.array([0.05, 0.10, 0.20]); qv = np.array([q[e]-n0 for e in epss])
qv = np.clip(qv, 1e-30, None)
slope = np.polyfit(np.log(epss), np.log(qv), 1)[0]
print(f"\n  selectivity (quad-driven / trace-driven traceless) = {sel:.2f}  (>>1 => spin-2 channel selective)")
print(f"  linearity exponent d log|tl|/d log eps = {slope:.2f}  (~1 => linear FGHMVR response)")
above_floor = q[0.20] > 5*n0
print(f"  traceless response above vacuum floor (eps=0.2) = {above_floor}  (q={q[0.20]:.2e} vs floor {n0:.2e})")

# =====================================================================
hr("VERDICT (decisive Front B exploration)")
# =====================================================================
visible = above_floor and sel > 3
print(f"  spin-2 channel responds above floor under traceless source = {above_floor}")
print(f"  response is SELECTIVE to the traceless source (not the trace) = {sel > 3}")
print(f"  -> {'KINEMATIC-VISIBLE (emergent geometry carries the graviton!)' if visible else 'KINEMATIC-BLIND (emergent geometry prices only the trace/central charge)'}")
print(f"\n  Whichever way: this is the genuine non-tautological test the whole arc")
print(f"  was driving toward -- the traceless curvature channel of an emergent")
print(f"  geometry made of records, sourced by a traceless stress.  mp dps-80")
print(f"  confirm of the selectivity ratio + the G=1/(4nu) coupling match next.")
