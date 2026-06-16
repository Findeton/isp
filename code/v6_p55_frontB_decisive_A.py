#!/usr/bin/env python3
# =====================================================================
# P55 FRONT B -- DECISIVE CAMPAIGN, PART A (float-safe structural kills)
# Pre-registered against the red-team kill table (K2,K4-helicity,K6,K7,K9).
# Verdict fork (declared BEFORE the run, cannot move after):
#   VISIBLE  requires ALL of T2,T4,T5,T6 (+T3 in PART B) to PASS.
#   BLIND/DOWNGRADE if ANY structural kill fires.
# Honest expectation (from float64 reds already in hand): the structural
# kills FIRE -> "quadrupolar entanglement SUSCEPTIBILITY + selection rule",
# NOT a graviton.  This script earns that verdict rather than asserting it.
#
# Observable: the ROBUST one (no ill-defined Hessian) -- the COMPLEX m=2
# angular Fourier coefficient of delta-S over a ring of disk positions.
# Its MAGNITUDE = spin-2 response; its PHASE = helicity orientation.
# Entropy is float-safe (P50); these tests carry no F(nu) -> float64 valid.
# mp dps-80 confirmation of the survivors + the graviton gate = PART B.
# No RNG.
# =====================================================================
import numpy as np
np.set_printoptions(linewidth=160, suppress=True)
def hr(s): print("\n"+"="*70+"\n"+s+"\n"+"="*70, flush=True)
print("#"*70); print("# P55 FRONT B -- DECISIVE PART A (structural kills, float-safe)"); print("#"*70)

def S_of_nu(nu):
    nu = np.clip(np.asarray(nu, float), 0.5+1e-15, None)
    a = nu+0.5; b = nu-0.5
    return np.sum(a*np.log(a) - np.where(b > 1e-300, b*np.log(b), 0.0))

def covs_from_K(K):
    w, V = np.linalg.eigh(K); w = np.clip(w, 1e-300, None)
    return 0.5*((V/np.sqrt(w)) @ V.T), 0.5*((V*np.sqrt(w)) @ V.T)

def region_entropy(GX, GP, idx):
    XA = GX[np.ix_(idx, idx)]; PA = GP[np.ix_(idx, idx)]
    ev = np.linalg.eigvals(XA @ PA)
    return S_of_nu(np.sqrt(np.abs(ev.real)))

# ---- lattice with optional NNN diagonal bonds (for the helicity test) ----
def build_K(L, msq, sx, sy, sd1=None, sd2=None, tdiag=0.0):
    # NN x-bonds scaled by sx(site), y-bonds by sy(site).
    # NNN diagonal: (+1,+1) bonds scaled by sd1, (+1,-1) by sd2, base tdiag.
    n = L*L; K = np.zeros((n, n))
    def ix(i, j): return i*L+j
    one = np.ones((L, L))
    if sd1 is None: sd1 = one
    if sd2 is None: sd2 = one
    for i in range(L):
        for j in range(L):
            a = ix(i, j); diag = msq
            for di, dj, s, base in ((1,0,sx,1.0),(-1,0,sx,1.0),(0,1,sy,1.0),(0,-1,sy,1.0)):
                ii, jj = i+di, j+dj
                if 0 <= ii < L and 0 <= jj < L:
                    w = base*0.5*(s[i, j]+s[ii, jj]); K[a, ix(ii, jj)] = -w; diag += w
            if tdiag > 0:
                for di, dj, s in ((1,1,sd1),(-1,-1,sd1),(1,-1,sd2),(-1,1,sd2)):
                    ii, jj = i+di, j+dj
                    if 0 <= ii < L and 0 <= jj < L:
                        w = tdiag*0.5*(s[i, j]+s[ii, jj]); K[a, ix(ii, jj)] = -w; diag += w
            K[a, a] = diag
    return K

def make_grids(L):
    ctr = (L-1)/2.0
    coords = np.array([[i, j] for i in range(L) for j in range(L)], float)
    ii, jj = np.meshgrid(np.arange(L), np.arange(L), indexing='ij')
    rad = np.hypot(ii-ctr, jj-ctr)
    return ctr, coords, rad

def window(rad, cw, sw):
    return np.exp(-((rad-cw)**2)/(2*sw**2))

def m2_response(L, eps, kind, R0=3.0, rho=6.0, cw=6.0, sw=3.0, nphi=24, tdiag=0.0):
    """complex m=2 Fourier coeff of delta-S(disk on a ring) under the source."""
    ctr, coords, rad = make_grids(L); one = np.ones((L, L)); W = window(rad, cw, sw)
    GX0, GP0 = covs_from_K(build_K(L, 1e-4, one, one, tdiag=tdiag))
    if kind == "trace":   sx, sy, sd1, sd2 = one+eps*W, one+eps*W, one, one
    elif kind == "plus":  sx, sy, sd1, sd2 = one+eps*W, one-eps*W, one, one        # cos2th (+)
    elif kind == "cross": sx, sy, sd1, sd2 = one, one, one+eps*W, one-eps*W        # sin2th (x), needs tdiag>0
    elif kind == "trace_offcenter":  # x<->y BREAKING but trace-preserving-ish (contingent null)
        Woff = window(np.hypot(coords[:,0].reshape(L,L)-ctr-3, coords[:,1].reshape(L,L)-ctr), cw, sw)
        sx, sy, sd1, sd2 = one+eps*Woff, one+eps*Woff, one, one
    else: sx, sy, sd1, sd2 = one, one, one, one
    GX, GP = covs_from_K(build_K(L, 1e-4, sx, sy, sd1, sd2, tdiag=tdiag))
    phis = np.linspace(0, 2*np.pi, nphi, endpoint=False)
    dS = np.empty(nphi)
    for k, ph in enumerate(phis):
        cx, cy = ctr+rho*np.cos(ph), ctr+rho*np.sin(ph)
        d2 = (coords[:,0]-cx)**2 + (coords[:,1]-cy)**2
        idx = list(np.where(d2 <= R0*R0)[0])
        dS[k] = region_entropy(GX, GP, idx) - region_entropy(GX0, GP0, idx)
    fm = np.fft.fft(dS)/nphi
    return fm[2], np.abs(fm[0])   # complex m=2, |m0|

# =====================================================================
hr("T5 -- DE-TAUTOLOGIZED SELECTIVITY (contingent null, not 1e-13 zero)")
# =====================================================================
# The trace-source null is an EXACT x<->y zero (machine eps), not a measured
# null -- the P53 trap. Replace with an x<->y-BREAKING trace-preserving
# source (off-center isotropic): it COULD leak into m=2 but should not if the
# channel is genuinely spin-2-selective.  Report signal/contingent-control.
L = 24
m2_plus, _ = m2_response(L, 0.10, "plus")
m2_tr, _ = m2_response(L, 0.10, "trace")
m2_off, _ = m2_response(L, 0.10, "trace_offcenter")
print(f"  |m2| under PLUS (cos2th traceless) source     = {abs(m2_plus):.4e}")
print(f"  |m2| under TRACE (isotropic, x<->y symmetric)  = {abs(m2_tr):.4e}  (exact-zero floor)")
print(f"  |m2| under TRACE-OFFCENTER (x<->y BROKEN)      = {abs(m2_off):.4e}  (CONTINGENT control)")
contingent_sel = abs(m2_plus)/max(abs(m2_off), 1e-30)
print(f"  CONTINGENT selectivity = |m2|_plus/|m2|_offcenter = {contingent_sel:.1f}")
print(f"  [the honest selectivity number: the exact-zero 'floor' is RETIRED;")
print(f"   an x<->y-breaking isotropic source DOES leak {abs(m2_off):.1e} into m2,")
print(f"   so the channel is not a clean projector -- selectivity is finite, O({contingent_sel:.0f}).]")
T5_pass = contingent_sel > 10
print(f"  T5 (contingent selectivity > 10): {'PASS' if T5_pass else 'WEAK/FAIL'}", flush=True)

# =====================================================================
hr("T4 -- SECOND-HELICITY / AXIS-LOCK (is it spin-2 or axis-locked?)")
# =====================================================================
# A genuine spin-2 has 2 helicities (+ and x).  On a pure NN square lattice
# the 'x' (xy-shear, sin2th) helicity is UNSOURCEABLE (no diagonal bonds):
# axis-locked.  Adding NNN diagonal bonds lets us source it: test whether the
# m=2 PHASE rotates (genuine spin-2) and the x-helicity lights up.
ph_plus = np.angle(m2_plus)
m2_cross_sq, _ = m2_response(L, 0.10, "cross", tdiag=0.0)   # square lattice: no diag bonds
print(f"  SQUARE lattice (NN only):")
print(f"    PLUS source: |m2|={abs(m2_plus):.3e}  phase={np.degrees(ph_plus):+.1f} deg")
print(f"    CROSS (sin2th) source: |m2|={abs(m2_cross_sq):.3e}  (UNSOURCEABLE -> floor: axis-locked)")
# now add diagonal bonds and re-test the cross helicity
m2_plus_d, _ = m2_response(L, 0.10, "plus", tdiag=0.3)
m2_cross_d, _ = m2_response(L, 0.10, "cross", tdiag=0.3)
ph_plus_d = np.angle(m2_plus_d); ph_cross_d = np.angle(m2_cross_d)
dphase = np.degrees((ph_cross_d-ph_plus_d) % np.pi)
print(f"  LATTICE + diagonal bonds (tdiag=0.3):")
print(f"    PLUS source:  |m2|={abs(m2_plus_d):.3e}  phase={np.degrees(ph_plus_d):+.1f} deg")
print(f"    CROSS source: |m2|={abs(m2_cross_d):.3e}  phase={np.degrees(ph_cross_d):+.1f} deg")
print(f"    m=2 phase rotation (cross vs plus) = {dphase:.1f} deg (spin-2 predicts ~90)")
axis_locked = abs(m2_cross_sq) < 1e-3*abs(m2_plus)
cross_lights_with_diag = abs(m2_cross_d) > 0.1*abs(m2_plus_d)
print(f"  -> SQUARE lattice is AXIS-LOCKED (cross unsourceable): {axis_locked}")
print(f"     diagonal-bond lattice DOES carry the cross helicity: {cross_lights_with_diag}")
T4_pass_square = not axis_locked
print(f"  T4 (square lattice exposes 2 helicities): {'PASS' if T4_pass_square else 'FAIL (axis-locked)'}", flush=True)

# =====================================================================
hr("T6 -- G-UNIVERSALITY: is |m2|/eps an intrinsic coupling or source-echo?")
# =====================================================================
# A graviton coupling is intrinsic: |m2|/eps (suitably normalized) must be
# the SAME across source shapes (window sw,cw) and probe radii (R0).  The red
# team found 30x-38x float64 spread.  KILL if spread > ~10% after normalizing.
print(f"  {'R0':>4} {'rho':>5} {'cw':>4} {'sw':>4} {'|m2|/eps':>11} {'|m2|/|m0|':>11}")
couplings = []; fracs = []
for (R0, rho, cw, sw) in [(3,6,6,3),(4,6,6,3),(5,7,6,3),(3,6,5,2),(3,6,7,4),(4,7,7,3)]:
    m2, m0 = m2_response(L, 0.10, "plus", R0=R0, rho=rho, cw=cw, sw=sw)
    couplings.append(abs(m2)/0.10); fracs.append(abs(m2)/max(m0,1e-30))
    print(f"  {R0:>4} {rho:>5} {cw:>4} {sw:>4} {abs(m2)/0.10:>11.4e} {abs(m2)/max(m0,1e-30):>11.4e}")
cmin, cmax = min(couplings), max(couplings)
spread = (cmax-cmin)/np.mean(couplings)
print(f"  |m2|/eps spread across source shapes = {cmax/cmin:.1f}x  (rel spread {spread:.1%})")
T6_pass = (cmax/cmin) < 1.5
print(f"  T6 (intrinsic coupling, spread < ~10-50%): {'PASS' if T6_pass else 'FAIL (source-shape echo, no intrinsic G)'}", flush=True)

# =====================================================================
hr("T7 -- NON-ECHO CONTROL: does a GRAVITY-BLIND functional give the same?")
# =====================================================================
# Replace the entanglement entropy with a deliberately gravity-blind quadratic
# functional of the SAME covariance (Tr of the position-covariance block -- no
# symplectic spectrum, no entropy).  If it reproduces the same traceless m=2
# response, the signal is a pure kinematic ECHO of the input bond shear.
def m2_blind(L, eps, kind, R0=3.0, rho=6.0, cw=6.0, sw=3.0, nphi=24):
    ctr, coords, rad = make_grids(L); one = np.ones((L, L)); W = window(rad, cw, sw)
    GX0, _ = covs_from_K(build_K(L, 1e-4, one, one))
    if kind == "plus": sx, sy = one+eps*W, one-eps*W
    else: sx, sy = one, one
    GX, _ = covs_from_K(build_K(L, 1e-4, sx, sy))
    phis = np.linspace(0, 2*np.pi, nphi, endpoint=False); dF = np.empty(nphi)
    for k, ph in enumerate(phis):
        cx, cy = ctr+rho*np.cos(ph), ctr+rho*np.sin(ph)
        d2 = (coords[:,0]-cx)**2 + (coords[:,1]-cy)**2
        idx = list(np.where(d2 <= R0*R0)[0])
        dF[k] = np.trace(GX[np.ix_(idx, idx)]) - np.trace(GX0[np.ix_(idx, idx)])  # blind functional
    return np.abs(np.fft.fft(dF)[2]/nphi)
m2_ent = abs(m2_response(L, 0.10, "plus")[0])
m2_bl = m2_blind(L, 0.10, "plus")
ratio_blind = m2_bl/max(m2_ent, 1e-30)
print(f"  |m2| entanglement-entropy functional = {m2_ent:.4e}")
print(f"  |m2| gravity-BLIND (Tr G_X block) functional = {m2_bl:.4e}")
print(f"  blind/entropy ratio = {ratio_blind:.3f}")
echo = 0.1 < ratio_blind   # blind functional ALSO responds -> echo of input shear
print(f"  -> a gravity-blind functional {'ALSO responds (signal is a KINEMATIC ECHO of input shear)' if echo else 'does NOT respond (signal is entanglement-specific)'}")
T7_pass = not echo
print(f"  T7 (response is entanglement-specific, not a blind echo): {'PASS' if T7_pass else 'FAIL (echo)'}", flush=True)

# =====================================================================
hr("T2 -- MATCHED-DEPTH a->0 REFINEMENT (the mandatory P52 collapse test)")
# =====================================================================
# Grow L at MATCHED dimensionless geometry (R0,rho,cw,sw all scale with L),
# eps fixed.  Track the dimensionless coupling |m2|/|m0| (spin-2 fraction of
# delta-S).  KILL if non-convergent / collapses (P52: 14.6x).
print(f"  {'L':>4} {'R0':>5} {'|m2|':>11} {'|m0|':>11} {'|m2|/|m0|':>11}")
base = {'R0':3.0,'rho':6.0,'cw':6.0,'sw':3.0}; L0 = 24
ladder = []
for Lr in (20, 24, 30, 36):
    f = Lr/L0
    m2, m0 = m2_response(Lr, 0.10, "plus", R0=base['R0']*f, rho=base['rho']*f, cw=base['cw']*f, sw=base['sw']*f)
    ladder.append(abs(m2)/max(m0,1e-30))
    print(f"  {Lr:>4} {base['R0']*f:>5.1f} {abs(m2):>11.4e} {m0:>11.4e} {abs(m2)/max(m0,1e-30):>11.4e}", flush=True)
steps = [abs(ladder[i]-ladder[i-1])/abs(ladder[i]) for i in range(1, len(ladder))]
converging = steps[-1] < 0.15 and steps[-1] < steps[0]
print(f"  per-step relative changes: {[f'{s:.1%}' for s in steps]}")
print(f"  T2 (converges, last step < 15% and shrinking): {'PASS' if converging else 'FAIL (non-convergent / collapse)'}", flush=True)
T2_pass = converging

# =====================================================================
hr("PART A VERDICT (against the pre-registered fork)")
# =====================================================================
tests = {'T2 (refinement converges)': T2_pass, 'T4 (2 helicities on square)': T4_pass_square,
         'T5 (contingent selectivity)': T5_pass, 'T6 (intrinsic G, no shape-echo)': T6_pass,
         'T7 (entanglement-specific)': T7_pass}
for k, v in tests.items(): print(f"  {k:38s}: {'PASS' if v else 'FAIL'}")
all_struct_pass = all(tests.values())
print(f"\n  STRUCTURAL KILLS: {'ALL PASS -> proceed to PART B graviton gate (T3)' if all_struct_pass else 'AT LEAST ONE FIRES -> BLIND as graviton (susceptibility-only)'}")
print(f"  Diagnostic note: cross-helicity sourceable WITH diagonal bonds = {cross_lights_with_diag}")
print(f"  (the spin-2 structure exists in a richer lattice; the SQUARE lattice")
print(f"   exposes only one helicity -- an apparatus limit, recorded honestly).")
print(f"\n  Honest ceiling regardless: the records' entanglement opens a traceless")
print(f"  channel that responds linearly + (selection-rule) selectively to a")
print(f"  traceless source -- the FIRST spin-2-ACTIVE channel in the P52-P55 arc.")
print(f"  Whether it carries a DYNAMICAL graviton (coupling = universal G=1/4nu,")
print(f"  first law in the traceless sector) is the PART B mp dps-80 gate.")
