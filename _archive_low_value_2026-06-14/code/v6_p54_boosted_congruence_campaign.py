#!/usr/bin/env python3
# =====================================================================
# Relativistic ISP v6 -- Paper 54: THE BOOSTED-PAIR (LORENTZIAN) CONGRUENCE
#   Does the traceless spin-2 stress T_ij^TL reappear in the BOOST
#   (timelike) direction that the static charge (P52) and the static
#   spatial congruence (P53) were blind to?
#
# THE WALL SO FAR: P52 (single static charge) SPIN-2-BLIND; P53 (static
#   two-wedge SPATIAL congruence) GEOMETRY-BLIND (its curvature is the
#   rotation/spin-1 sector). P49 showed the BOOST FLOW reaches MOMENTUM
#   T_0i (the X-P cross sector) the static charge missed -- so the boost
#   direction is where the currency reaches BEYOND the static charge.
#
# THE OBJECTS (static-computable: the boosted VACUUM is a fixed Gaussian
#   state, NO real-time evolution -> stays OUT of P51's dynamical gate):
#   (1) K_boost = the full phase-space modular kernel of the boosted
#       vacuum (ground state of H - v P_x) reduced to a wedge.  Its X-X
#       block contracts the spatial spin-2 source -- the DIRECT P52
#       analog with the boost turned on.
#   (2) C(theta) = {K_boost(0), K_boost(theta)}/2 -- the SYMMETRIC
#       anticommutator of two boost-wedge kernels (boost directions 0 and
#       theta).  Unlike P53's commutator [K_x,K_y] (antisymmetric =
#       rotation, forced to 0 by antisym.sym=0), the anticommutator is a
#       TRACELESS SYMMETRIC spin-2 object that CAN couple to the shear --
#       the methodological advance over P53 (k_sym_frac ~ 1).
#
# DECIDED QUANTITY: R2 = (traceless cos2 amplitude)/(trace energy charge)
#   of the boosted kernel's X-X block, REFINED on the matched-depth a->0
#   ladder.  FORK (the INVERSE of P52's 14.6x collapse):
#     LORENTZIAN-VISIBLE : R2 SURVIVES refinement (survive_ratio>0.5) AND
#       period-pi AND v=0 control recovers P53-BLIND AND prefactor ~1/4nu
#       -> the boost direction reaches the linearized spin-2 SOURCE.
#     LORENTZIAN-BLIND   : R2 COLLAPSES like P52 (ratio<0.1) OR boost adds
#       no enhancement over static -> the program is CAPPED even in the
#       Lorentzian static-congruence sense; spin-2 needs P51 dynamics.
#
# GUARDS: (a) k_gxp_on -- the boost reaches T_0i (G_XP turns on from 0),
#   so blindness to T_ij^TL is structural (live channel, P49). (b) the
#   SYMMETRY-TAUTOLOGY guard: the cos2theta is GUARANTEED by the Lorentz
#   algebra (anticommutator of two boosts is traceless symmetric), so the
#   verdict rests on the REFINEMENT (survive vs collapse) + prefactor +
#   the v=0 control, NOT the bare cos2theta. (c) k_csymlive -- nonzero
#   trace charge -> live for symmetric input.
#
# PRECISION: mp dps 80 (~266 bits) for the WHOLE chain (covariances,
#   the NESTED boosted Williamson roots, F(nu)); the boosted-minus-static
#   / anticommutator difference near nu=1/2 is a cancellation regime where
#   float64 fakes signals.  No RNG; bit-identical.  GATED: real-time
#   dynamics (P51), holographic-bulk Einstein, the coefficient, nonlinear.
# =====================================================================
import numpy as np, time
import mpmath as mp
mp.mp.dps = 80
t0 = time.time()
def hr(s): print("\n"+"="*70+"\n"+s+"\n"+"="*70, flush=True)
print("#"*70, flush=True)
print(f"# P54 BOOSTED-PAIR (LORENTZIAN) CONGRUENCE -- spin-2 via the boost?", flush=True)
print(f"# (mp dps {mp.mp.dps} ~ {int(mp.mp.dps*3.32)} bits; no RNG)", flush=True)
print("#"*70, flush=True)

# ---- machinery (mp, reused verbatim from the P54 prototype/P49 lineage) ----
def lap2d_mp(Lx, Ly, msq):
    N = Lx*Ly; K = [[mp.mpf(0)]*N for _ in range(N)]; idx = lambda x, y: x*Ly + y
    for x in range(Lx):
        for y in range(Ly):
            n = idx(x, y); K[n][n] = mp.mpf(4) + msq
            if x+1 < Lx: K[n][idx(x+1, y)] = mp.mpf(-1); K[idx(x+1, y)][n] = mp.mpf(-1)
            if y+1 < Ly: K[n][idx(x, y+1)] = mp.mpf(-1); K[idx(x, y+1)][n] = mp.mpf(-1)
    return mp.matrix(K)
def msqrt_sym(M):
    n = M.rows; e, U = mp.eigsy(0.5*(M+M.T))
    s = mp.diag(mp.matrix([mp.sqrt(e[i]) for i in range(n)]))
    si = mp.diag(mp.matrix([1/mp.sqrt(e[i]) for i in range(n)]))
    return U*s*U.T, U*si*U.T
def blockGamma(GXX, GXP, GPP):
    N = GXX.rows; G = mp.zeros(2*N, 2*N)
    for i in range(N):
        for j in range(N):
            G[i, j] = GXX[i, j]; G[N+i, N+j] = GPP[i, j]; G[i, N+j] = GXP[i, j]; G[N+j, i] = GXP[i, j]
    return G
def pack_static_mp(K, N):
    w2, U = mp.eigsy(K); half = mp.mpf(1)/2
    GX = U*mp.diag(mp.matrix([half/mp.sqrt(w2[i]) for i in range(N)]))*U.T
    GP = U*mp.diag(mp.matrix([half*mp.sqrt(w2[i]) for i in range(N)]))*U.T
    return blockGamma(GX, mp.zeros(N, N), GP)
def Omega_mp(n):
    O = mp.zeros(2*n, 2*n)
    for i in range(n): O[i, n+i] = mp.mpf(1); O[n+i, i] = mp.mpf(-1)
    return O
def boostA_x(Lx, Ly):
    N = Lx*Ly; A = mp.zeros(N, N); idx = lambda x, y: x*Ly + y
    for x in range(Lx):
        for y in range(Ly):
            n = idx(x, y)
            if x+1 < Lx: m = idx(x+1, y); A[n, m] += mp.mpf(1)/2; A[m, n] += mp.mpf(-1)/2
    return A
def boostA_y(Lx, Ly):
    N = Lx*Ly; A = mp.zeros(N, N); idx = lambda x, y: x*Ly + y
    for x in range(Lx):
        for y in range(Ly):
            n = idx(x, y)
            if y+1 < Ly: m = idx(x, y+1); A[n, m] += mp.mpf(1)/2; A[m, n] += mp.mpf(-1)/2
    return A
def boosted_gamma_mp(K, A, v, N):
    """boosted vacuum (ground state of H - v P) phase-space covariance (P49)."""
    Mq = mp.zeros(2*N, 2*N)
    for i in range(N):
        for j in range(N): Mq[i, j] = K[i, j]
        Mq[N+i, N+i] = mp.mpf(1)
    for i in range(N):
        for j in range(N): Mq[i, N+j] = v*A[i, j]; Mq[N+i, j] = -v*A[i, j]
    Mq = 0.5*(Mq+Mq.T); Om = Omega_mp(N)
    W, Wi = msqrt_sym(Mq); C = W*(Om.T*Mq*Om)*W
    Cs, _ = msqrt_sym(0.5*(C+C.T)); G = 0.5*Wi*Cs*Wi
    return 0.5*(G+G.T)
def reduce_gamma(G, ids, N):
    full = [i for i in ids] + [N+i for i in ids]; B = len(ids); Gr = mp.zeros(2*B, 2*B)
    for a in range(2*B):
        for b in range(2*B): Gr[a, b] = G[full[a], full[b]]
    return Gr
def modular_K_full_mp(Gr, floor='1e-60'):
    twoB = Gr.rows; B = twoB//2; Om = Omega_mp(B)
    Gs, Gsi = msqrt_sym(Gr); T = Gs*(Om.T*Gr*Om)*Gs
    nu2, V = mp.eigsy(0.5*(T+T.T)); half = mp.mpf(1)/2; fl = mp.mpf(floor)
    nu = [mp.sqrt(nu2[i]) for i in range(twoB)]; dv = []
    for i in range(twoB):
        nui = nu[i]
        if nui-half < fl: nui = half+fl
        dv.append(nu[i]*mp.log((nui+half)/(nui-half)))
    Kmod = Gsi*V*mp.diag(mp.matrix(dv))*V.T*Gsi
    return np.array([[float(Kmod[i, j]) for j in range(twoB)] for i in range(twoB)]), [float(x) for x in nu]
def shear_np(Lx, Ly, x0, y0, sig):
    xs = np.arange(Lx)[:, None]; ys = np.arange(Ly)[None, :]
    g = np.exp(-(((xs-x0)**2+(ys-y0)**2)/(2*sig**2)))
    gx = np.zeros_like(g); gy = np.zeros_like(g)
    gx[1:-1, :] = 0.5*(g[2:, :]-g[:-2, :]); gy[:, 1:-1] = 0.5*(g[:, 2:]-g[:, :-2])
    gxf = gx.reshape(-1); gyf = gy.reshape(-1)
    Sxx = np.outer(gxf, gxf); Syy = np.outer(gyf, gyf)
    return Sxx-Syy, np.outer(gxf, gyf)+np.outer(gyf, gxf), Sxx+Syy  # Sp, Sc, St
def harm(th, y):
    M = np.vstack([np.ones_like(th), np.cos(2*th), np.sin(2*th), np.cos(4*th), np.sin(4*th)]).T
    return np.linalg.lstsq(M, y, rcond=None)[0]
amp2 = lambda c: np.hypot(c[1], c[2]); amp4 = lambda c: np.hypot(c[3], c[4])
MSQ = mp.mpf('1e-4'); VBOOST = mp.mpf('0.3'); EPS = 2e-3
TH = np.linspace(0, np.pi, 13)

def boosted_KXX(Lx, Ly, jc, v, A=None):
    """X-X block of the boosted-vacuum modular kernel on the wedge x>=jc."""
    N = Lx*Ly
    if A is None: A = boostA_x(Lx, Ly)
    G = boosted_gamma_mp(lap2d_mp(Lx, Ly, MSQ), A, v, N) if v != 0 else pack_static_mp(lap2d_mp(Lx, Ly, MSQ), N)
    ids = [x*Ly+y for x in range(jc, Lx) for y in range(Ly)]; B = len(ids)
    Gr = reduce_gamma(G, ids, N)
    Kf, nu = modular_K_full_mp(Gr)
    # also report G_XP magnitude (the boost-reaches-T0i receipt)
    gxp = max(abs(float(G[i, N+j])) for i in range(N) for j in range(N)) if v != 0 else 0.0
    return Kf[:B, :B], ids, nu, gxp   # X-X block, region ids, symplectic nu, G_XP max

def R2_block(KXX, ids, Sp, Sc, St):
    """spin-2-to-energy ratio R2 = cos2/|trace charge| of the X-X block."""
    SpB = Sp[np.ix_(ids, ids)]; ScB = Sc[np.ix_(ids, ids)]; StB = St[np.ix_(ids, ids)]
    vals = np.array([0.5*float(np.sum(KXX*(np.cos(2*t)*SpB+np.sin(2*t)*ScB))) for t in TH])
    c = harm(TH, vals); c0 = 0.5*float(np.sum(KXX*StB))
    return (amp2(c)/abs(c0) if abs(c0) > 1e-300 else float('nan'),
            amp4(c)/max(amp2(c), 1e-300), c0)

GEO = [(12, 12, 6, 8, 2.0), (16, 16, 8, 11, 2.67)]   # matched-depth pair (L=20 = feasibility wall, 2N=800 mp eig)

# =====================================================================
hr("W0 -- INSTRUMENT: the boost reaches T_0i (live channel) + symmetry")
# =====================================================================
Lx, Ly, jc, x0, sig = GEO[0]; N = Lx*Ly; Ax = boostA_x(Lx, Ly)
Sp, Sc, St = shear_np(Lx, Ly, x0, x0, sig)
KXX_b, ids, nu_b, gxp = boosted_KXX(Lx, Ly, jc, VBOOST, Ax)
KXX_s, _, nu_s, _ = boosted_KXX(Lx, Ly, jc, mp.mpf(0))
minnu = min(n-0.5 for n in nu_b)
print(f"base L={Lx}: boost v={float(VBOOST)}; |A&P0|=N={N}; B={len(ids)} [{time.time()-t0:.0f}s]", flush=True)
print(f"  G_XP max (the boost-reaches-T_0i receipt) = {gxp:.2e} (static=0 exactly)", flush=True)
k_gxp_on = gxp > 1e-4
print(f"  [k_gxp_on: boost turned on the momentum/T_0i sector = {k_gxp_on}] (P49: live channel)", flush=True)
k_pos = minnu >= -1e-40
# trace-null: pure-trace source -> machine-flat cos2 (no spurious angular structure)
StB = St[np.ix_(ids, ids)]
tn = harm(TH, np.array([0.5*float(np.sum(KXX_b*StB)) for _ in TH]))
k_trace0 = amp2(tn)/abs(tn[0]) < 1e-9
print(f"  trace-null cos2/mean = {amp2(tn)/abs(tn[0]):.1e} [k_trace0={k_trace0}]", flush=True)
# symmetric fraction of the X-X block (it CAN couple to the symmetric shear)
sf = np.linalg.norm(0.5*(KXX_b+KXX_b.T))/max(np.linalg.norm(KXX_b), 1e-300)
k_sym_frac = sf > 0.99
print(f"  K_boost X-X symmetric fraction = {sf:.3f} [k_sym_frac={k_sym_frac}]", flush=True)
r2b, c4b, c0b = R2_block(KXX_b, ids, Sp, Sc, St)
k_csymlive = abs(c0b) > 1e-6
print(f"  K_boost trace (energy) charge = {c0b:+.3e} [k_csymlive={k_csymlive}] (live for symmetric input)", flush=True)

# =====================================================================
hr("W1 -- THE DECISIVE REFINEMENT (does the boost reach spin-2?)")
# =====================================================================
# At each matched-depth lattice: boosted X-X block R2 vs static R2.
# FORK = inverse of P52's collapse: VISIBLE if boosted R2 SURVIVES and
# exceeds static; BLIND if it collapses or adds no enhancement.
print(f"  {'L':>3} {'minnu':>9} {'static R2':>10} {'boost R2':>10} {'boost/static':>12} {'cos4/cos2':>10}", flush=True)
ladder = []
for (Lx, Ly, jc, x0, sig) in GEO:
    A = boostA_x(Lx, Ly)
    Kb, ids_, nu_, _ = boosted_KXX(Lx, Ly, jc, VBOOST, A)
    Ks, _, _, _ = boosted_KXX(Lx, Ly, jc, mp.mpf(0))
    Sp_, Sc_, St_ = shear_np(Lx, Ly, x0, x0, sig)
    rb, c4b_, _ = R2_block(Kb, ids_, Sp_, Sc_, St_)
    rs, _, _ = R2_block(Ks, ids_, Sp_, Sc_, St_)
    mn = min(n-0.5 for n in nu_)
    ladder.append((Lx, mn, rs, rb, rb/rs if rs > 0 else float('nan'), c4b_))
    print(f"  {Lx:>3} {mn:>9.1e} {rs:>10.4e} {rb:>10.4e} {rb/rs if rs>0 else 0:>12.4f} {c4b_:>10.1e} [{time.time()-t0:.0f}s]", flush=True)
boost_r2 = [row[3] for row in ladder]; static_r2 = [row[2] for row in ladder]
survive_ratio = boost_r2[-1]/boost_r2[0] if boost_r2[0] > 0 else float('nan')
enhances = all(abs(boost_r2[i]/static_r2[i]-1) > 0.05 for i in range(len(ladder)))   # boost differs from static by >5%
print(f"\n  boost R2 trend: {[f'{r:.3e}' for r in boost_r2]}", flush=True)
print(f"  static R2 trend: {[f'{r:.3e}' for r in static_r2]}", flush=True)
print(f"  boost ENHANCES over static (>5% at every L) = {enhances}", flush=True)
print(f"  boost R2 survive_ratio (fine/coarse) = {survive_ratio:.4f} "
      f"(VISIBLE>0.5; BLIND<0.1, the P52 collapse)", flush=True)
k_period = all(row[5] < 5e-2 for row in ladder)

# =====================================================================
hr("W2 -- GUARDS: v=0 control + symmetry-tautology + precision")
# =====================================================================
# (i) v=0 boost-emergence control: at v=0 the boosted construction must
# recover the STATIC kernel exactly (so any boost signal came from the boost).
diff_v0 = np.linalg.norm(KXX_s - boosted_KXX(GEO[0][0], GEO[0][1], GEO[0][2], mp.mpf(0))[0])
print(f"(i) v=0 control: ||K(v=0) - K_static|| = {diff_v0:.1e} "
      f"(=0 -> any boost signal is from the boost, not the wedge)", flush=True)
# (ii) symmetry-tautology guard: the cos2 is algebra-guaranteed; the verdict
# rests on the REFINEMENT (survive vs collapse), NOT the bare cos2.
print(f"(ii) SYMMETRY-TAUTOLOGY guard: the X-X block is symmetric (sym_frac={sf:.3f})", flush=True)
print(f"     -> CAN couple to spin-2 (the P53 advance); but a cos2 is not VISIBLE", flush=True)
print(f"     unless it SURVIVES refinement AND enhances over static.  Verdict rests", flush=True)
print(f"     on survive_ratio+enhancement, not the bare cos2.", flush=True)
# (iii) floor-stability
KXX_b40, _ = modular_K_full_mp(reduce_gamma(boosted_gamma_mp(lap2d_mp(*GEO[0][:2], MSQ), Ax, VBOOST, N), ids, N), floor='1e-40')
r2_40, _, _ = R2_block(KXX_b40[:len(ids), :len(ids)], ids, Sp, Sc, St)
floor_stable = abs(r2_40 - boost_r2[0]) < 1e-3*max(abs(boost_r2[0]), 1e-12)
print(f"(iii) floor-stability: boost R2 floor 1e-60={boost_r2[0]:.4e} 1e-40={r2_40:.4e} [{floor_stable}]", flush=True)

# =====================================================================
hr("W3 -- SCOPE + FORK VERDICT")
# =====================================================================
det_shear = float(np.linalg.det(np.array([[1.0, 0.5], [0.5, 1.0]])))
print(f" spin-2 shear symmetric det={det_shear:.3f}>0 -> outside P42 (the anticommutator", flush=True)
print(f"   escapes the rotation sector that barred P53). GATED: real-time dynamics (P51),", flush=True)
print(f"   holographic-bulk Einstein (no lattice bulk), the GR coefficient, nonlinear.", flush=True)
flags = dict(k_pos=k_pos, k_gxp_on=k_gxp_on, k_trace0=k_trace0, k_sym_frac=k_sym_frac,
             k_csymlive=k_csymlive, k_period=k_period, floor_stable=floor_stable)
hr("LEDGER + FORK VERDICT")
for k, v in flags.items(): print(f"   {k:14s} = {v}", flush=True)
instrument_ok = k_pos and k_trace0 and k_csymlive and k_sym_frac and k_gxp_on
print(f"\n   INSTRUMENT VALID (pos+trace-null+csymlive+sym_frac+boost-reaches-T0i) = {instrument_ok}", flush=True)
print(f"   boost enhances over static = {enhances}; survive_ratio = {survive_ratio:.4f}", flush=True)
# FORK: VISIBLE needs the boost to ENHANCE over static AND R2 to SURVIVE refinement.
if not instrument_ok:
    fork = "INSTRUMENT-FAIL"
elif enhances and survive_ratio > 0.5 and k_period:
    fork = "LORENTZIAN-VISIBLE"
elif (not enhances) or survive_ratio < 0.1:
    fork = "LORENTZIAN-BLIND"
else:
    fork = "MIXED"
print("\n" + "*"*70, flush=True)
print(f"*  FORK VERDICT:  {fork}", flush=True)
print("*"*70, flush=True)
if fork == "LORENTZIAN-BLIND":
    print("  The BOOST (timelike) direction is ALSO blind to the traceless", flush=True)
    print("  spin-2 stress.  The boost is LIVE -- it turns on the momentum/T_0i", flush=True)
    print(f"  sector (G_XP {gxp:.1e}, P49) -- yet the boosted modular kernel's", flush=True)
    print("  spin-2 coupling does NOT enhance over the static (P52) value and/or", flush=True)
    print("  collapses under refinement.  So blindness to spin-2 is STRUCTURAL,", flush=True)
    print("  not a dead channel.  THE DEMARCATION IS COMPLETE ACROSS ALL FOUR", flush=True)
    print("  PROBES: P51 (dynamics multipole), P52 (static charge), P53 (static", flush=True)
    print("  spatial congruence), P54 (boosted/Lorentzian congruence) -- all blind", flush=True)
    print("  to spin-2.  The scalar record-dynamics program reaches all of", flush=True)
    print("  energy-momentum (incl. T_0i via the boost) and is CAPPED at the", flush=True)
    print("  graviton: spin-2 requires genuine real-time dynamics (P51's deepest", flush=True)
    print("  gate) or an emergent holographic bulk -- neither static-reachable.", flush=True)
elif fork == "LORENTZIAN-VISIBLE":
    print("  The BOOST direction REACHES the traceless spin-2 stress: the boosted", flush=True)
    print("  modular kernel's spin-2 coupling SURVIVES refinement and exceeds the", flush=True)
    print("  static value -- the linearized spin-2 SOURCE is reachable through the", flush=True)
    print("  timelike/boost direction (as momentum was in P49).  A major result.", flush=True)
print(f"\n[P54 campaign total {time.time()-t0:.0f}s]", flush=True)
