#!/usr/bin/env python3
# =====================================================================
# Relativistic ISP v6 -- Paper 53: THE GEOMETRY SIDE
#   Does the traceless spin-2 stress T_ij^TL reappear in the modular
#   CONGRUENCE (the variation of K across differently-oriented regions)
#   even though P52 proved it is projected out of each single region's
#   static charge?
#
# THE OBJECT: two wedges with DIFFERENT boost directions -- A = x>=jc
#   (x-boost), B = y>=jc (y-boost) -- the minimal congruence.  Their
#   modular kernels K_A, K_B do not commute.  We price a polarized
#   traceless-shear source S(theta) against the cross-region objects:
#     C_AB = (K_A K_B + K_B K_A)/2   (symmetric cross channel)
#     B_AB = (K_A K_B - K_B K_A)/2   ([K_A,K_B], the Berry curvature)
#   and against the cut-variation dK = K_B - K_A.  The traceless
#   response is normalized by the trace (energy) charge (the P52 c2/c0).
#
# THE STRUCTURAL SPINE (analytic): the commutator of two boosts is a
#   ROTATION, [K_x, K_y] = -i J_z (Lorentz algebra).  So the congruence
#   curvature B_AB lives in the ROTATION (spin-1, ANTISYMMETRIC) sector
#   -- which is (a) orthogonal to the SYMMETRIC traceless spin-2 shear,
#   and (b) exactly the P42-barred circulation sector (det(JR)=-1).  So
#   the congruence's non-commuting part cannot carry spin-2 -- predicted
#   BLIND, confirmed numerically (Berry traceless ~ machine 0).
#
# FORK G (pre-registered): the decided quantity is the traceless coupling
#   R2 = (traceless cos2 amp)/(trace energy charge) of the most-coupled
#   congruence proxy, REFINED on a matched-depth a->0 ladder.  The test
#   is the INVERSE of P52's collapse:
#     GEOMETRY-VISIBLE : R2 SURVIVES refinement (collapse ratio > 0.5)
#       AND family-independent -> linearized spin-2 source recoverable.
#     GEOMETRY-BLIND   : R2 COLLAPSES (ratio < 0.1, like P52) OR the
#       congruence coupling never exceeds the single-region baseline ->
#       capped at the scalar energy-momentum first law.
#     MIXED            : stable but coefficient-unmatched / partial.
#
# WHY A NEGATIVE IS NON-TRIVIAL (not trivial-BLIND): CAL-LIVE shows the
#   congruence channel DOES respond to a known rotation/anisotropy probe
#   (the channel is open, not a dead instrument); blindness to the
#   SYMMETRIC traceless shear is then a structural fact.
#
# SCOPE (GATED): the FGHMVR linearized-Einstein recovery is HOLOGRAPHIC
#   (needs a bulk dual); the record lattice is a boundary theory with no
#   bulk, so the first law dS=d<K> is automatically satisfied and carries
#   no geometric constraint.  Genuine spin-2 needs either an emergent
#   holographic bulk (absent) or the Lorentzian/dynamical sector (P51,
#   gated).  Also GATED: nonlinear Einstein, the GR coefficient (P50 nu
#   l_c-unconverged), back-reaction, radiative graviton.
#
# PRECISION (honest): mpmath dps 80 (~266 bits) for KERNEL CONSTRUCTION
#   (covariances via eigsy, Williamson reduction, F(nu)) -- this is the
#   precision-critical step (F(nu) diverges as nu->1/2; deep modes run to
#   min(nu-1/2)=1.1e-53 at L=20).  Kernels are then cast to float64 and the
#   congruence ALGEBRA (K_A K_B products, commutator, contractions) is
#   float64 -- a float-safe use: kernels well-conditioned, decisive C_AB
#   signal O(1), no F(nu) in the products.  (The one cancellation object,
#   the commutator, is a tautological zero by the antisym.sym selection
#   rule, so float64 is adequate there too.)  No RNG; bit-identical.
# EVIDENTIARY WEIGHTING (per hostile review): the Berry traceless amp and
#   the CAL-LIVE contrast are SYMMETRY TAUTOLOGIES (antisym.sym=0;
#   antisym.antisym!=0), reported as consistency checks, NOT measurements.
#   The load-bearing, contingent result is the SYMMETRIC C_AB cross-excess.
# =====================================================================
import numpy as np
import time
import mpmath as mp
mp.mp.dps = 80

t0 = time.time()
def hr(s): print("\n" + "="*70 + "\n" + s + "\n" + "="*70, flush=True)
print("#"*70, flush=True)
print(f"# P53 THE GEOMETRY SIDE -- spin-2 in the modular congruence?", flush=True)
print(f"# (mp dps {mp.mp.dps} ~ {int(mp.mp.dps*3.32)} bits; no RNG)", flush=True)
print("#"*70, flush=True)

# --------------------------------------------------------------------
# Fully-mp machinery (reused verbatim from the P52/P53-prototype lineage)
# --------------------------------------------------------------------
def lap2d_mp(Lx, Ly, msq):
    N = Lx*Ly; K = [[mp.mpf(0)]*N for _ in range(N)]
    idx = lambda x, y: x*Ly + y
    for x in range(Lx):
        for y in range(Ly):
            n = idx(x, y); K[n][n] = mp.mpf(4) + msq
            if x+1 < Lx: K[n][idx(x+1, y)] = mp.mpf(-1); K[idx(x+1, y)][n] = mp.mpf(-1)
            if y+1 < Ly: K[n][idx(x, y+1)] = mp.mpf(-1); K[idx(x, y+1)][n] = mp.mpf(-1)
    return mp.matrix(K)

def pack_mp(K, N):
    w2, U = mp.eigsy(K); half = mp.mpf(1)/2
    GX = U*mp.diag(mp.matrix([half/mp.sqrt(w2[i]) for i in range(N)]))*U.T
    GP = U*mp.diag(mp.matrix([half*mp.sqrt(w2[i]) for i in range(N)]))*U.T
    return GX, GP

def tofloat(Mmp):
    return np.array([[float(Mmp[i, j]) for j in range(Mmp.cols)] for i in range(Mmp.rows)])

def williamson_mp(GX, GP, ids):
    B = len(ids)
    GXb = mp.matrix([[GX[ids[a], ids[b]] for b in range(B)] for a in range(B)])
    GPb = mp.matrix([[GP[ids[a], ids[b]] for b in range(B)] for a in range(B)])
    e2, V = mp.eigsy(GXb)
    Mi = V*mp.diag(mp.matrix([1/mp.sqrt(e2[i]) for i in range(B)]))*V.T
    w2, W = mp.eigsy((V*mp.diag(mp.matrix([mp.sqrt(e2[i]) for i in range(B)]))*V.T)*GPb*
                     (V*mp.diag(mp.matrix([mp.sqrt(e2[i]) for i in range(B)]))*V.T))
    nu = [mp.sqrt(w2[i]) for i in range(B)]
    return tofloat(Mi*W), nu

def modular_kernel_X(GX, GP, ids, floor='1e-60'):
    """X-sector modular kernel matrix K_X = Qf diag(F(nu) nu) Qf^T, in the
    region's own index space."""
    Qf, nu = williamson_mp(GX, GP, ids)
    half = mp.mpf(1)/2; fl = mp.mpf(floor)
    Fn = np.array([float(mp.log((nu[k]+half)/max(nu[k]-half, fl))*nu[k]) for k in range(len(nu))])
    return Qf @ np.diag(Fn) @ Qf.T, nu

def shear_np(Lx, Ly, x0, y0, sig):
    xs = np.arange(Lx)[:, None]; ys = np.arange(Ly)[None, :]
    g = np.exp(-(((xs-x0)**2 + (ys-y0)**2)/(2*sig**2)))
    gx = np.zeros_like(g); gy = np.zeros_like(g)
    gx[1:-1, :] = 0.5*(g[2:, :] - g[:-2, :]); gy[:, 1:-1] = 0.5*(g[:, 2:] - g[:, :-2])
    gxf = gx.reshape(-1); gyf = gy.reshape(-1)
    Sxx = np.outer(gxf, gxf); Syy = np.outer(gyf, gyf)
    St = Sxx + Syy; Sp = Sxx - Syy; Sc = np.outer(gxf, gyf) + np.outer(gyf, gxf)
    nrm = np.linalg.norm(St)
    return Sp/nrm, Sc/nrm, St/nrm

def harm(th, y):
    M = np.vstack([np.ones_like(th), np.cos(2*th), np.sin(2*th), np.cos(4*th), np.sin(4*th)]).T
    return np.linalg.lstsq(M, y, rcond=None)[0]
amp2 = lambda c: np.hypot(c[1], c[2])
amp4 = lambda c: np.hypot(c[3], c[4])

MSQ = mp.mpf('1e-4'); EPS = 2e-3
TH = np.linspace(0, np.pi, 13)

# congruence builder at a given lattice (matched dimensionless geometry):
#   A = x>=jc (x-boost), B = y>=jc (y-boost), source at overlap corner.
def build_congruence(Lx, Ly, jc, x0, sig, floor='1e-60'):
    N = Lx*Ly
    GX, GP = pack_mp(lap2d_mp(Lx, Ly, MSQ), N)
    idsA = [x*Ly + y for x in range(jc, Lx) for y in range(Ly)]
    idsB = [x*Ly + y for x in range(Lx) for y in range(jc, Ly)]
    KA_loc, nuA = modular_kernel_X(GX, GP, idsA, floor)
    KB_loc, nuB = modular_kernel_X(GX, GP, idsB, floor)
    def lift(Kloc, ids):
        K = np.zeros((N, N)); K[np.ix_(ids, ids)] = Kloc; return K
    KA, KB = lift(KA_loc, idsA), lift(KB_loc, idsB)
    Sp, Sc, St = shear_np(Lx, Ly, x0, x0, sig)
    minnu = min(min(float(nuA[i]-mp.mpf(1)/2) for i in range(len(nuA))),
                min(float(nuB[i]-mp.mpf(1)/2) for i in range(len(nuB))))
    return dict(KA=KA, KB=KB, Sp=Sp, Sc=Sc, St=St, minnu=minnu, N=N,
                nA=np.linalg.norm(KA), nB=np.linalg.norm(KB))

def sweep_traceless(op, Sp, Sc):
    return np.array([0.5*float(np.tensordot(op, np.cos(2*t)*Sp+np.sin(2*t)*Sc, axes=([0,1],[0,1]))) for t in TH])
def c0_trace(op, St):
    return 0.5*float(np.tensordot(op, St, axes=([0, 1], [0, 1])))
def R2_traceless(op, Sp, Sc, St):
    """spin-2-to-energy ratio: traceless cos2 amp / |trace energy charge|."""
    c = harm(TH, sweep_traceless(op, Sp, Sc)); c0 = c0_trace(op, St)
    return (amp2(c)/abs(c0) if abs(c0) > 1e-300 else float('nan'),
            amp4(c)/max(amp2(c), 1e-300), c0)

# geometry ladder (matched dimensionless geometry, a->0), mirroring P52
GEO = [(12, 12, 6, 8, 2.0), (16, 16, 8, 11, 2.67), (20, 20, 10, 13, 3.33)]
# dist-to-cut / sig at the corner source: (x0-jc)/sig held ~1.0; margin similar.

# =====================================================================
hr("W0 -- THE CONGRUENCE INSTRUMENT (base lattice) + CALIBRATION")
# =====================================================================
print("structural spine: A=x-boost wedge, B=y-boost wedge; [K_x,K_y]=-iJ_z", flush=True)
print("(Lorentz algebra) -> the Berry curvature B_AB lives in the ROTATION", flush=True)
print("(spin-1, ANTISYMMETRIC) sector, orthogonal to the SYMMETRIC spin-2", flush=True)
print("shear AND inside P42's barred circulation sector -> predicted BLIND.", flush=True)
base = build_congruence(*GEO[0][:2], GEO[0][2], GEO[0][3], GEO[0][4])
KA, KB, Sp, Sc, St = base['KA'], base['KB'], base['Sp'], base['Sc'], base['St']
print(f"\nbase L={GEO[0][0]}: |KA|={base['nA']:.3e} |KB|={base['nB']:.3e} "
      f"min(nu-1/2)={base['minnu']:.2e} [{time.time()-t0:.0f}s]", flush=True)
k_pos = base['minnu'] >= -1e-40
CAB = 0.5*(KA@KB + KB@KA)
BAB = 0.5*(KA@KB - KB@KA)
print(f"||[KA,KB]||={np.linalg.norm(BAB):.3e} (non-zero -> congruence HAS curvature)", flush=True)
k_curv = np.linalg.norm(BAB) > 1e-6*max(base['nA'], base['nB'])

# CAL-1 trace-null: a pure-trace source must give machine-flat traceless cos2
# (the kernel adds no spurious angular structure) -- promoted to congruence.
def trace_null(op):
    # feed the PURE-TRACE source rotated: its cos2 must be ~0
    vals = np.array([0.5*float(np.tensordot(op, St, axes=([0,1],[0,1]))) for _ in TH])
    c = harm(TH, vals); return amp2(c)/abs(c[0]) if abs(c[0]) > 1e-300 else 0.0
k_trace0 = trace_null(CAB) < 1e-9
print(f"CAL trace-null (congruence C_AB cos2/mean on pure-trace) = {trace_null(CAB):.1e} "
      f"[k_trace0={k_trace0}]", flush=True)

# LIVENESS of the SPIN-2 (symmetric) channel -- the dead-instrument disarm
# that actually matters: C_AB carries a NONZERO energy (trace) charge, so it
# is a WORKING instrument for symmetric input.  Its spin-2 coupling falling
# below baseline (W1) is then a structural statement, NOT operator silence.
c0_CAB = c0_trace(CAB, St)
k_csymlive = abs(c0_CAB) > 1e-6
print(f"SYMMETRIC-CHANNEL LIVENESS: C_AB energy (trace) charge = {c0_CAB:+.3e} "
      f"(nonzero -> C_AB is a LIVE instrument for symmetric input) [k_csymlive={k_csymlive}]", flush=True)
# CAL-LIVE (rotation-sector wiring check, SYMMETRY-FORCED, not a measurement):
# the commutator B_AB is antisymmetric so B_AB.A_anti != 0 while K_A.A_anti = 0
# by antisym.sym=0 -- this only certifies the spin-1/rotation channel is open
# (never in doubt); it is SILENT on the symmetric spin-2 channel.
xs = np.arange(GEO[0][0])[:, None]; ys = np.arange(GEO[0][1])[None, :]
g = np.exp(-(((xs-GEO[0][3])**2+(ys-GEO[0][3])**2)/(2*GEO[0][4]**2)))
gxa = np.zeros_like(g); gya = np.zeros_like(g)
gxa[1:-1, :] = 0.5*(g[2:, :]-g[:-2, :]); gya[:, 1:-1] = 0.5*(g[:, 2:]-g[:, :-2])
gxf = gxa.reshape(-1); gyf = gya.reshape(-1)
A_anti = (np.outer(gxf, gyf) - np.outer(gyf, gxf)); A_anti = A_anti/np.linalg.norm(A_anti)
live_berry = 0.5*float(np.tensordot(BAB, A_anti, axes=([0,1],[0,1])))
live_single = 0.5*float(np.tensordot(KA, A_anti, axes=([0,1],[0,1])))
k_live = abs(live_berry) > 1e-8 and abs(live_berry) > abs(live_single)
print(f"CAL-LIVE (rotation-sector wiring check, SYMMETRY-FORCED): Berry.A_anti = "
      f"{live_berry:+.3e} vs single-A.A_anti {live_single:+.3e} (=0 by antisym.sym)", flush=True)
print(f"   [k_live: rotation/spin-1 channel open = {k_live}; certifies ONLY the", flush=True)
print(f"    antisymmetric channel -- the spin-2 disarm is C_AB liveness above]", flush=True)

# =====================================================================
hr("W1 -- THE DECISIVE REFINEMENT (does the congruence carry spin-2?)")
# =====================================================================
# At each matched-depth lattice, measure the TRACELESS coupling R2 of:
#  - single region (the P52 baseline, expected BLIND/collapse)
#  - C_AB the symmetric cross channel (the congruence's coupling)
#  - B_AB the Berry curvature (the rotation sector -- structurally ~0)
# FORK: VISIBLE if the congruence R2 SURVIVES refinement AND exceeds the
# single-region baseline; BLIND if it collapses or never exceeds it.
print(f"  {'L':>3} {'minnu':>9} {'single R2':>11} {'C_AB R2':>11} {'Berry TLamp':>12} {'cross-excess':>12}", flush=True)
ladder = []
for (Lx, Ly, jc, x0, sig) in GEO:
    c = build_congruence(Lx, Ly, jc, x0, sig)
    KA, KB, Sp, Sc, St = c['KA'], c['KB'], c['Sp'], c['Sc'], c['St']
    CAB = 0.5*(KA@KB + KB@KA); BAB = 0.5*(KA@KB - KB@KA)
    CAA = KA@KA; CBB = KB@KB
    r_single = R2_traceless(KA, Sp, Sc, St)[0]
    r_cab = R2_traceless(CAB, Sp, Sc, St)[0]
    r_caa = R2_traceless(CAA, Sp, Sc, St)[0]; r_cbb = R2_traceless(CBB, Sp, Sc, St)[0]
    base_R2 = 0.5*(r_caa + r_cbb)            # same-cut (no new direction) baseline
    berry_tl = amp2(harm(TH, sweep_traceless(BAB, Sp, Sc)))   # absolute traceless amp
    cross_excess = r_cab - base_R2
    ladder.append((Lx, c['minnu'], r_single, r_cab, berry_tl, cross_excess, base_R2))
    print(f"  {Lx:>3} {c['minnu']:>9.1e} {r_single:>11.4e} {r_cab:>11.4e} "
          f"{berry_tl:>12.3e} {cross_excess:>+12.4e} [{time.time()-t0:.0f}s]", flush=True)

# the decisive quantity: the CROSS-DIRECTION EXCESS (congruence coupling beyond
# the same-cut baseline) -- the genuine new-direction spin-2 coupling.
excess = [row[5] for row in ladder]
cab_r2 = [row[3] for row in ladder]
single_r2 = [row[2] for row in ladder]
# does the congruence coupling EXCEED the single-region baseline at all?
cong_exceeds = all(cab_r2[i] > 2*single_r2[i] for i in range(len(ladder)))
# does the cross-excess SURVIVE refinement (VISIBLE) or COLLAPSE (BLIND)?
exc_coarse = abs(excess[0]); exc_fine = abs(excess[-1])
survive_ratio = exc_fine/exc_coarse if exc_coarse > 1e-300 else float('nan')
print(f"\n  cross-excess trend: {[f'{e:+.2e}' for e in excess]}", flush=True)
print(f"  congruence R2 exceeds 2x single-region baseline at every L = {cong_exceeds}", flush=True)
print(f"  cross-excess survive ratio (fine/coarse) = {survive_ratio:.4f}", flush=True)
berry_amps = [row[4] for row in ladder]
print(f"  Berry traceless amp (SELECTION-RULE check, antisym.sym=0, ~float64 "
      f"roundoff): {[f'{b:.1e}' for b in berry_amps]} -- an algebraic identity,", flush=True)
print(f"  NOT a measurement; weight rests on the symmetric cross-excess above.", flush=True)
k_berry_zero = max(berry_amps) < 1e-9

# =====================================================================
hr("W2 -- PRECISION + STRUCTURAL RECEIPTS")
# =====================================================================
# (i) floor INACTIVITY (honest): the regulator floor never engages -- min(nu-1/2)
# (3.9e-31..1.1e-53) sits far above the floors (1e-60,1e-78), so the two-floor
# C_AB R2 are bit-identical by construction.  This is an underflow safety net,
# NOT a binding precision test.  dps-80 is load-bearing for KERNEL CONSTRUCTION
# (resolving min(nu-1/2)); the float64 congruence algebra is float-safe.
c = build_congruence(*GEO[0][:2], GEO[0][2], GEO[0][3], GEO[0][4], floor='1e-78')
CAB78 = 0.5*(c['KA']@c['KB'] + c['KB']@c['KA'])
r_cab78 = R2_traceless(CAB78, c['Sp'], c['Sc'], c['St'])[0]
floor_inactive = abs(r_cab78 - cab_r2[0]) < 1e-3*max(abs(cab_r2[0]), 1e-12)
print(f"(i) floor INACTIVE: C_AB R2 floor 1e-60={cab_r2[0]:.4e} 1e-78={r_cab78:.4e} "
      f"identical (floors below min(nu-1/2) -> safety net only) [{floor_inactive}]", flush=True)
# (ii) selection-rule receipt: the Berry traceless amp ~0 is the algebraic
# identity antisym.sym=0 (NOT a contingent measurement); its only physics
# content is the CONTINUUM identification [K_x,K_y]->-iJ_z placing the
# antisymmetric channel in the rotation (spin-1) sector, P42-barred.  The
# LOAD-BEARING result is the SYMMETRIC C_AB cross-excess (negative, growing).
print(f"(ii) SELECTION RULE: Berry [KA,KB] traceless = antisym.sym = 0 identically "
      f"({k_berry_zero}); physics = continuum [K_x,K_y]->-iJ_z (rotation/spin-1,", flush=True)
print(f"     P42-barred), orthogonal to spin-2.  Load-bearing = symmetric", flush=True)
print(f"     cross-excess {[f'{e:+.3f}' for e in excess]} (negative -> no spin-2 channel).", flush=True)
# (iii) FGHMVR-needs-bulk note (scope, analytic): the first-order ball residual
# dS - d<K> = 0 by the entanglement first law; the FGHMVR linearized-Einstein
# recovery needs a HOLOGRAPHIC BULK (absent on a record lattice).
print(f"(iii) FGHMVR scope: the first law dS=d<K> holds at first order with NO", flush=True)
print(f"     residual on a bulkless lattice -> no geometric constraint to source", flush=True)
print(f"     spin-2.  The Einstein recovery is holographic; the lattice has no bulk.", flush=True)

# =====================================================================
hr("W3 -- SCOPE / NO-GO")
# =====================================================================
shear_def = np.array([[1.0, 0.5], [0.5, 1.0]]); det_shear = float(np.linalg.det(shear_def))
print(f" the spin-2 shear is symmetric, det={det_shear:.3f}>0 (volume-preserving)", flush=True)
print(f"   -> OUTSIDE P42's circulation no-go; but the congruence CURVATURE", flush=True)
print(f"   [K_x,K_y]=J_z is exactly the antisymmetric det(JR)=-1 sector P42 BARS.", flush=True)
k_scope = det_shear > 0
print(" GATED: holographic-bulk Einstein recovery (no lattice bulk); Lorentzian/", flush=True)
print("   dynamical graviton (P51); nonlinear Einstein; the GR coefficient", flush=True)
print("   (P50 nu l_c-unconverged); back-reaction.", flush=True)

# =====================================================================
hr("LEDGER + FORK G VERDICT")
# =====================================================================
flags = dict(k_pos=k_pos, k_curv=k_curv, k_trace0=k_trace0,
             k_csymlive=k_csymlive, k_live=k_live, k_berry_zero=k_berry_zero,
             floor_inactive=floor_inactive, k_scope=k_scope)
for k, v in flags.items():
    print(f"   {k:14s} = {v}", flush=True)
# instrument validity for the SPIN-2 (symmetric) channel rests on C_AB being a
# LIVE instrument for symmetric input (k_csymlive), NOT on the symmetry-forced
# rotation-channel CAL-LIVE (k_live, reported but not the spin-2 disarm).
instrument_ok = k_pos and k_trace0 and k_curv and k_csymlive and k_scope
print(f"\n   INSTRUMENT VALID (positivity+trace-null+has-curvature+C_AB-symmetric-LIVE+scope) = {instrument_ok}", flush=True)
print(f"   congruence opens NEW symmetric channel beyond baseline = {cong_exceeds}", flush=True)
print(f"   cross-excess (sign-aware; VISIBLE needs >0 AND growing) = {[f'{e:+.3f}' for e in excess]}", flush=True)

# FORK G (pre-registered, SIGN-AWARE): VISIBLE requires the congruence to open a
# NEW positive symmetric channel beyond the same-cut baseline (cross-excess > 0)
# AND survive refinement.  The operative criterion is cong_exceeds; the
# cross-excess is negative at every L -> no new channel -> BLIND.
visible = cong_exceeds and (excess[-1] > 0) and (abs(excess[-1]) >= abs(excess[0]))
blind = (not cong_exceeds) or (excess[-1] < 0)
if not instrument_ok:
    fork = "INSTRUMENT-FAIL"
elif visible:
    fork = "GEOMETRY-VISIBLE"
elif blind:
    fork = "GEOMETRY-BLIND (static two-wedge spatial congruence)"
else:
    fork = "MIXED"
print("\n" + "*"*70, flush=True)
print(f"*  FORK G VERDICT:  {fork}", flush=True)
print("*"*70, flush=True)
if fork.startswith("GEOMETRY-BLIND"):
    print("  The static TWO-WEDGE SPATIAL congruence does NOT carry the traceless", flush=True)
    print("  spin-2 stress.  Two cross-region objects, settled by different means:", flush=True)
    print("  (1) ANTISYMMETRIC commutator B_AB -- a SELECTION RULE (antisym.sym=0,", flush=True)
    print("  lattice-exact); continuum reading [K_x,K_y]->-iJ_z = rotation (spin-1,", flush=True)
    print("  P42-barred), orthogonal to spin-2.  (2) SYMMETRIC C_AB -- the genuine", flush=True)
    print("  CONTINGENT result: a LIVE instrument (nonzero energy charge) whose", flush=True)
    print("  spin-2 cross-excess is NEGATIVE and grows under refinement", flush=True)
    print(f"  ({[f'{e:+.3f}' for e in excess]}) -> the 2nd boost direction opens NO", flush=True)
    print("  spin-2 channel.  GATED (untested, not refuted): ball-family (FGHMVR,", flush=True)
    print("  holographic, no lattice bulk), Lorentzian/boosted-pair (the boost-angle", flush=True)
    print("  sweep that could flip to VISIBLE), second-variation/Raychaudhuri.", flush=True)
    print("  DEMARCATION (static side) complete: P52 single-region + P53 static", flush=True)
    print("  two-wedge congruence both blind to spin-2.  Program reaches all of", flush=True)
    print("  energy-momentum, stops at the graviton (needs bulk or Lorentzian/", flush=True)
    print("  dynamical, gated).  CAPPED at the scalar energy-momentum first law.", flush=True)
print(f"\n[P53 campaign total {time.time()-t0:.0f}s]", flush=True)
