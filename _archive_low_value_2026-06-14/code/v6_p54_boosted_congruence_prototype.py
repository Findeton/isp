#!/usr/bin/env python3
# =====================================================================
# Relativistic ISP v6 -- Paper 54 PROTOTYPE (MACHINERY INVESTIGATOR)
#
#   THE P54 QUESTION (the GATED experiment named by P53):
#   The STATIC gravity demarcation is a WALL on three probes:
#     P51 (dynamics): scalar radiation -> generic centrifugal P_l~Omega^(2l+2),
#         NOT gravitational quadrupole dominance.
#     P52 (single static charge): SPIN-2-BLIND.  K_R = 2pi int x T_00 is the
#         BOOST=ENERGY generator (Bisognano-Wichmann), built from the TRACE
#         (grad phi)^2.  Traceless spin-2 T_ij^TL is Frobenius-orthogonal,
#         projected out.
#     P53 (static two-wedge SPATIAL congruence): GEOMETRY-BLIND.  The Berry
#         curvature [K_A,K_B] of two SPATIAL boosts = a ROTATION (spin-1,
#         [K_x,K_y]=-iJ_z); the SYMMETRIC cross-excess COLLAPSES (negative,
#         growing).  No spin-2 channel on the static vacuum.
#
#   P54 is the FIRST step into the GATED LORENTZIAN/DYNAMICAL sector:
#   the BOOST-ANGLE-SWEEP of the symmetric cross-coupling on a TIMELIKE
#   (boosted) region pair.  THE INTUITION (P49):  the boost FLOW reaches
#   T_0i (the X-P / momentum cross sector) that the STATIC charge was BLIND
#   to.  In the STATIC vacuum G_XP = 0, so the modular kernel is X-SECTOR
#   ONLY (K_X, built from the trace T_00).  The BOOST turns ON G_XP (P49:
#   GXPd != 0, T_0i = antisym-derivative of G_XP).  So the boost direction
#   is where the currency reaches BEYOND the static charge.
#
#   P54 ASKS:  does the boost/Lorentzian congruence reach the traceless
#   SPIN-2 stress T_ij^TL too?  The decisive structural object: the FULL
#   PHASE-SPACE modular kernel of a wedge in the BOOSTED vacuum has an X-X
#   block DEFORMED by the boost.  A purely-SPATIAL spin-2 source grad_i phi
#   grad_j phi (symmetric, traceless, rank-2 SPATIAL) contracts the X-X
#   block.  P49 reached T_0i (one time index = antisym X-P).  P54 asks
#   whether the boosted kernel's SYMMETRIC SPATIAL (X-X) structure acquires
#   a traceless cos2theta coupling that the static kernel lacked.
#
#   THE BOOSTED-PAIR CONGRUENCE (this prototype):
#   region A (wedge) in the STATIC vacuum -> K_A^stat (X-sector, P52).
#   region A in the BOOSTED vacuum (ground state of H - v P_x) -> K_A^boost
#       (FULL phase space: X-X, X-P, P-P blocks).
#   The cross-region / variation objects:
#     (1) dK = K_A^boost - K_A^stat   (the BOOST VARIATION of the kernel;
#         the faithful Lorentzian-congruence analog of P53's spatial dK).
#     (2) C_AB = {K_A^stat, K_B^boost}/2  symmetric cross (boosted partner).
#     (3) the X-X BLOCK of the boosted kernel vs static -- the ONLY block a
#         spatial spin-2 source sees.
#   DECISIVE COUPLING: inject the polarized traceless-shear source S(theta)
#   = cos2theta S_+ + sin2theta S_x (St=0, pure spin-2) into the X-X block
#   of each object.  P52/P53 collapse <-> a refinement-STABLE, enhanced
#   cos2theta in the BOOSTED variation = VISIBLE (boost reaches spin-2).
#
#   SPIN-2 vs SPIN-1 CHECK (the P53 selection rule, now in the boost dir):
#   P53's [K_A,K_B] was ANTISYMMETRIC -> rotation (spin-1), machine-zero on
#   the symmetric source by antisym.sym=0.  The BOOSTED kernel's X-X block
#   is SYMMETRIC -> it CAN couple to the symmetric spin-2 shear.  We build
#   it and test whether it DOES (contingent), or whether the boost only
#   deforms the X-P (spin-1/momentum) block, leaving X-X spin-2-blind.
#
#   PRECISION (the SHARD rule): mpmath dps 80 for the WHOLE chain.  The
#   boosted Williamson (ground_gamma: sym_sqrt of the dynamical matrix
#   M_q = [[K, vA],[-vA, 1]], then the [Om^T M_q Om] sandwich sqrt) and the
#   reduced-block symplectic diagonalization both run deep modes to nu->1/2
#   where F(nu)=log((nu+1/2)/(nu-1/2)) DIVERGES; the boosted-minus-static
#   DIFFERENCE is a catastrophic cancellation.  float64 fakes a signal.
#   No RNG; bit-identical.
#
#   SCOPE: <5min PROTOTYPE, tiny lattice.  FEASIBILITY + DIRECTION, not the
#   P54 verdict.  Honest outcomes: VISIBLE / BLIND / MIXED.  Stay OUT of
#   full real-time dynamics (P51's deeper gate) unless the design forces it.
# =====================================================================
import numpy as np
import time
import mpmath as mp
mp.mp.dps = 80

t0 = time.time()
def hr(s): print("\n" + "="*70 + "\n" + s + "\n" + "="*70, flush=True)
print("#"*70, flush=True)
print("# P54 BOOSTED-PAIR CONGRUENCE -- does the BOOST reach T_ij^TL?", flush=True)
print(f"# (mp dps {mp.mp.dps} ~ {int(mp.mp.dps*3.32)} bits; no RNG)", flush=True)
print("#"*70, flush=True)

# --------------------------------------------------------------------
# FULLY-MP 2D free-scalar machinery (P52/P53 lineage).
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

def msqrt_sym(M):
    """mp symmetric sqrt and inverse-sqrt via eigsy (symmetric PD)."""
    n = M.rows
    e, U = mp.eigsy(0.5*(M + M.T))
    s  = mp.diag(mp.matrix([mp.sqrt(e[i]) for i in range(n)]))
    si = mp.diag(mp.matrix([1/mp.sqrt(e[i]) for i in range(n)]))
    return U*s*U.T, U*si*U.T

def pack_static_mp(K, N):
    """STATIC vacuum phase-space covariance Gamma (2N x 2N):
       G_XX = (1/2)K^{-1/2}, G_PP = (1/2)K^{1/2}, G_XP = 0."""
    w2, U = mp.eigsy(K); half = mp.mpf(1)/2
    GX = U*mp.diag(mp.matrix([half/mp.sqrt(w2[i]) for i in range(N)]))*U.T
    GP = U*mp.diag(mp.matrix([half*mp.sqrt(w2[i]) for i in range(N)]))*U.T
    Z  = mp.zeros(N, N)
    return blockGamma(GX, Z, GP)

def blockGamma(GXX, GXP, GPP):
    """assemble 2N x 2N phase-space covariance [[GXX,GXP],[GXP^T,GPP]]."""
    N = GXX.rows
    G = mp.zeros(2*N, 2*N)
    for i in range(N):
        for j in range(N):
            G[i, j] = GXX[i, j]
            G[N+i, N+j] = GPP[i, j]
            G[i, N+j] = GXP[i, j]
            G[N+j, i] = GXP[i, j]
    return G

def Omega_mp(n):
    O = mp.zeros(2*n, 2*n)
    for i in range(n):
        O[i, n+i] = mp.mpf(1); O[n+i, i] = mp.mpf(-1)
    return O

# --- the BOOST generator P_x as an antisymmetric coupling matrix A ---
def boostA_x(Lx, Ly):
    """P_x = (1/2)(shift_+x - shift_-x): central x-derivative, antisymmetric.
       This is the generator the boosted vacuum is the ground state of
       (H - v P_x).  Boost ANGLE: A(theta) = cos(theta) A_x + sin(theta) A_y."""
    N = Lx*Ly; A = mp.zeros(N, N)
    idx = lambda x, y: x*Ly + y
    for x in range(Lx):
        for y in range(Ly):
            n = idx(x, y)
            if x+1 < Lx:
                m = idx(x+1, y); A[n, m] += mp.mpf(1)/2; A[m, n] += mp.mpf(-1)/2
    return A

def boostA_y(Lx, Ly):
    N = Lx*Ly; A = mp.zeros(N, N)
    idx = lambda x, y: x*Ly + y
    for x in range(Lx):
        for y in range(Ly):
            n = idx(x, y)
            if y+1 < Ly:
                m = idx(x, y+1); A[n, m] += mp.mpf(1)/2; A[m, n] += mp.mpf(-1)/2
    return A

def boosted_gamma_mp(K, A, v, N):
    """BOOSTED vacuum (ground state of H - v P) phase-space covariance, full mp.
       P49 construction:  dynamical matrix M_q = [[K, vA],[-vA, 1]] (the
       Hamiltonian of the boosted frame); the ground-state covariance is
         Gamma = (1/2) Mq^{-1/2} [ Mq^{1/2} Om^T Mq Om Mq^{1/2} ]^{1/2} Mq^{-1/2}.
       Returns 2N x 2N Gamma with NONZERO G_XP block (the new sector)."""
    Mq = mp.zeros(2*N, 2*N)
    for i in range(N):
        for j in range(N):
            Mq[i, j] = K[i, j]
        Mq[N+i, N+i] = mp.mpf(1)
    for i in range(N):
        for j in range(N):
            Mq[i, N+j]   = v*A[i, j]
            Mq[N+i, j]   = -v*A[i, j]
    Mq = 0.5*(Mq + Mq.T)  # ensure symmetric (A antisym so vA block-antisym -> Mq sym)
    Om = Omega_mp(N)
    W, Wi = msqrt_sym(Mq)
    C = W*(Om.T*Mq*Om)*W
    Cs, _ = msqrt_sym(0.5*(C + C.T))
    G = 0.5*Wi*Cs*Wi
    return 0.5*(G + G.T)

# --------------------------------------------------------------------
# FULL PHASE-SPACE modular kernel of a reduced region (X and P modes).
# Reduce Gamma to the region's phase-space indices [ids ; N+ids], then
# Williamson:  symp eigenvalues nu and modes; K_mod = Om Gs^{-1} V diag(F nu)
# ... we return the QUADRATIC FORM kernel acting on phase-space (x_R,p_R).
# --------------------------------------------------------------------
def reduce_gamma(G, ids, N):
    """reduce 2N phase-space covariance to region ids -> 2B x 2B block
       ordered [x_ids ; p_ids]."""
    full = [i for i in ids] + [N+i for i in ids]
    B = len(ids)
    Gr = mp.zeros(2*B, 2*B)
    for a in range(2*B):
        for b in range(2*B):
            Gr[a, b] = G[full[a], full[b]]
    return Gr

def modular_K_full_mp(Gr, floor='1e-60'):
    """FULL phase-space modular kernel of a reduced region (2B x 2B).
         Gs = Gr^{1/2};  T = Gs Om^T Gr Om Gs;  nu^2 = eig(T);
         K_mod = Gs^{-1} V diag(nu F(nu)) V^T Gs^{-1},  F=log((nu+.5)/(nu-.5)).
       Returns (Kmod_float 2B x 2B, nu list).  This is the operator whose
       X-X block contracts a SPATIAL spin-2 source grad_i phi grad_j phi."""
    twoB = Gr.rows; B = twoB//2
    Om = Omega_mp(B)
    Gs, Gsi = msqrt_sym(Gr)
    T = Gs*(Om.T*Gr*Om)*Gs
    nu2, V = mp.eigsy(0.5*(T + T.T))
    half = mp.mpf(1)/2; fl = mp.mpf(floor)
    nu = [mp.sqrt(nu2[i]) for i in range(twoB)]
    diagvals = []
    for i in range(twoB):
        nui = nu[i]
        if nui - half < fl:
            nui = half + fl
        F = mp.log((nui+half)/(nui-half))
        diagvals.append(nu[i]*F)
    D = mp.diag(mp.matrix(diagvals))
    Kmod = Gsi*V*D*V.T*Gsi
    Kf = np.array([[float(Kmod[i, j]) for j in range(twoB)] for i in range(twoB)])
    return Kf, [float(x) for x in nu]

# --- traceless-shear sources from FIELD gradients (pure spin-2, St=0) ---
def shear_np(Lx, Ly, x0, y0, sig):
    xs = np.arange(Lx)[:, None]; ys = np.arange(Ly)[None, :]
    g = np.exp(-(((xs-x0)**2 + (ys-y0)**2)/(2*sig**2)))
    gx = np.zeros_like(g); gy = np.zeros_like(g)
    gx[1:-1, :] = 0.5*(g[2:, :] - g[:-2, :])
    gy[:, 1:-1] = 0.5*(g[:, 2:] - g[:, :-2])
    gxf = gx.reshape(-1); gyf = gy.reshape(-1)
    Sxx = np.outer(gxf, gxf); Syy = np.outer(gyf, gyf)
    St = Sxx + Syy                      # trace (P52 energy channel)
    Sp = Sxx - Syy                      # + polarization (traceless)
    Sc = np.outer(gxf, gyf) + np.outer(gyf, gxf)   # x polarization (traceless)
    nrm = np.linalg.norm(St)
    return Sp/nrm, Sc/nrm, St/nrm

def harm(th, y):
    M = np.vstack([np.ones_like(th), np.cos(2*th), np.sin(2*th),
                   np.cos(4*th), np.sin(4*th)]).T
    return np.linalg.lstsq(M, y, rcond=None)[0]
amp2 = lambda c: np.hypot(c[1], c[2])
amp4 = lambda c: np.hypot(c[3], c[4])

MSQ = mp.mpf('1e-4')
TH = np.linspace(0, np.pi, 13)

# =====================================================================
hr("BUILD -- 2D lattice, static + boosted vacua, region A wedge")
# =====================================================================
Lx, Ly = 8, 8; N = Lx*Ly
jc = 4                      # region A = x>=jc (right half: an x-boost wedge)
x0, y0, sig = 5, 4, 1.6     # source near the wedge edge
VBOOST = mp.mpf('0.30')     # boost rapidity-velocity (P49 used ~0.05-0.3)
print(f"lattice L={Lx}x{Ly} (N={N}); msq={float(MSQ):.0e}; wedge A: x>={jc} "
      f"(|A|={(Lx-jc)*Ly}); v_boost={float(VBOOST)}", flush=True)

Kmp = lap2d_mp(Lx, Ly, MSQ)
Ax  = boostA_x(Lx, Ly)               # P_x generator (boost in +x = wedge normal)
print(f"[build static vacuum covariance ... {time.time()-t0:.0f}s]", flush=True)
Gstat = pack_static_mp(Kmp, N)
print(f"[build BOOSTED vacuum (ground of H - v P_x) ... {time.time()-t0:.0f}s]", flush=True)
Gboost = boosted_gamma_mp(Kmp, Ax, VBOOST, N)

# RECEIPT: the boost turns ON the G_XP block (static has G_XP = 0 exactly).
GXP_stat = max(abs(float(Gstat[i, N+j])) for i in range(N) for j in range(N))
GXP_boost = max(abs(float(Gboost[i, N+j])) for i in range(N) for j in range(N))
print(f"  RECEIPT  max|G_XP|: static={GXP_stat:.2e} (=0 exact)  "
      f"boosted={GXP_boost:.3e} (BOOST turns on the X-P / momentum sector)",
      flush=True)
# RECEIPT: the boosted G_XX (spatial!) block DIFFERS from static -- this is
# the block a SPATIAL spin-2 source sees.  Does it acquire spin-2 structure?
dGXX = max(abs(float(Gboost[i, j] - Gstat[i, j])) for i in range(N) for j in range(N))
print(f"  RECEIPT  max|G_XX(boost)-G_XX(stat)| = {dGXX:.3e}  "
      f"(boost deforms the SPATIAL block too -- candidate spin-2 carrier)",
      flush=True)

ids = [x*Ly + y for x in range(jc, Lx) for y in range(Ly)]
B = len(ids)

# =====================================================================
hr("BUILD MODULAR KERNELS -- static (X-only) vs boosted (full phase space)")
# =====================================================================
GrStat  = reduce_gamma(Gstat,  ids, N)
GrBoost = reduce_gamma(Gboost, ids, N)
print(f"[Williamson static kernel ... {time.time()-t0:.0f}s]", flush=True)
KstatF, nuStat  = modular_K_full_mp(GrStat)
print(f"[Williamson boosted kernel ... {time.time()-t0:.0f}s]", flush=True)
KboostF, nuBoost = modular_K_full_mp(GrBoost)
half = 0.5
minnu_stat = min(n - half for n in nuStat)
minnu_boost = min(n - half for n in nuBoost)
print(f"  min(nu-1/2): static={minnu_stat:.2e}  boosted={minnu_boost:.2e} "
      f"(deep modes near vacuum -> dps 80 load-bearing)", flush=True)

# Extract X-X blocks (the SPATIAL block a spin-2 source contracts).
KXX_stat  = KstatF[:B, :B]
KXX_boost = KboostF[:B, :B]
KXP_boost = KboostF[:B, B:]
KPP_boost = KboostF[B:, B:]
print(f"  ||K_XX stat||={np.linalg.norm(KXX_stat):.3e}  "
      f"||K_XX boost||={np.linalg.norm(KXX_boost):.3e}", flush=True)
print(f"  ||K_XP boost||={np.linalg.norm(KXP_boost):.3e} "
      f"(spin-1/momentum block, P49's T_0i sector)  "
      f"||K_PP boost||={np.linalg.norm(KPP_boost):.3e}", flush=True)

# lift a B x B region-block op to global N x N for source contraction
def liftB(Kbb):
    K = np.zeros((N, N)); K[np.ix_(ids, ids)] = Kbb; return K

# =====================================================================
hr("THE DECISIVE COUPLING -- spin-2 source into the X-X block")
# =====================================================================
Sp, Sc, St = shear_np(Lx, Ly, x0, y0, sig)
def sweep_TL(opGlob):
    return np.array([0.5*float(np.tensordot(
        opGlob, np.cos(2*t)*Sp + np.sin(2*t)*Sc, axes=([0,1],[0,1])))
        for t in TH])
def c0_trace(opGlob):
    return 0.5*float(np.tensordot(opGlob, St, axes=([0,1],[0,1])))
def R2(opGlob):
    c = harm(TH, sweep_TL(opGlob)); c0 = c0_trace(opGlob)
    r = amp2(c)/abs(c0) if abs(c0) > 1e-300 else float('nan')
    return r, amp2(c), c0, amp4(c)/max(amp2(c), 1e-300)

KXX_stat_g  = liftB(KXX_stat)
KXX_boost_g = liftB(KXX_boost)
# THE BOOST VARIATION: dK_XX = boosted - static X-X block.  In the static
# case this block is P52's BW energy kernel (spin-2-blind).  The boost
# DIFFERENCE isolates what the Lorentzian direction ADDS.  Spin-2 reaches
# the boost iff dK_XX has a refinement-stable, enhanced cos2theta coupling.
dKXX_g = liftB(KXX_boost - KXX_stat)

r_stat,  a2_stat,  c0_stat,  c42_stat  = R2(KXX_stat_g)
r_boost, a2_boost, c0_boost, c42_boost = R2(KXX_boost_g)
print("PURE-TRACELESS source (St=0, spin-2); R2 = cos2amp/|trace energy charge|:", flush=True)
print(f"   static  K_XX : c0_trace={c0_stat:+.4e}  cos2amp={a2_stat:.4e}  "
      f"R2={r_stat:.4e}  cos4/cos2={c42_stat:.2e}  (the P52 BW kernel; BLIND)", flush=True)
print(f"   boosted K_XX : c0_trace={c0_boost:+.4e}  cos2amp={a2_boost:.4e}  "
      f"R2={r_boost:.4e}  cos4/cos2={c42_boost:.2e}", flush=True)

# energy-cancelling difference -> use PER-NORM traceless coupling (P53 lesson)
a2_dKXX = amp2(harm(TH, sweep_TL(dKXX_g)))
n_dKXX = np.linalg.norm(KXX_boost - KXX_stat)
n_stat = np.linalg.norm(KXX_stat)
perN_stat  = a2_stat  / max(n_stat, 1e-300)
perN_dKXX  = a2_dKXX  / max(n_dKXX, 1e-300)
print(f"\n   BOOST VARIATION dK_XX = K_XX(boost)-K_XX(stat):", flush=True)
print(f"     ||dK_XX||={n_dKXX:.3e}  traceless cos2amp={a2_dKXX:.4e}", flush=True)
print(f"     traceless cos2 amp per ||op||:  static K_XX={perN_stat:.4e}  "
      f"dK_XX={perN_dKXX:.4e}", flush=True)
ratio_pn = perN_dKXX / max(perN_stat, 1e-300)
boost_opens = ratio_pn > 2.0
print(f"     [boost VARIATION opens traceless channel vs static (per-norm "
      f"ratio {ratio_pn:.3f}, >2=opens) = {boost_opens}]", flush=True)

# =====================================================================
hr("SPIN-2 vs SPIN-1 CHECK -- which boosted block carries the response?")
# =====================================================================
# P49 reached T_0i = the ANTISYMMETRIC X-P block (spin-1/momentum).  The
# spin-2 question is about the SYMMETRIC X-X (spatial) block.  Decompose
# the boost-induced kernel deformation by block and ask which one the
# traceless cos2theta source couples to.
#   - X-X block traceless coupling  -> spin-2 (SPATIAL symmetric) channel
#   - X-P block: P49's spin-1 momentum sector (a spatial spin-2 source does
#     NOT contract it -- it is one-time-one-space; reported as the control)
KXP_g = liftB(0.5*(KXP_boost + KXP_boost.T))  # symmetric part of X-P
a2_xp = amp2(harm(TH, sweep_TL(KXP_g)))
print(f"   X-X (spatial, symmetric) traceless cos2amp [dK] = {a2_dKXX:.4e} "
      f"<- the SPIN-2 candidate channel", flush=True)
print(f"   X-P (sym. part) traceless cos2amp = {a2_xp:.4e}  "
      f"(P49's spin-1/momentum sector; control)", flush=True)
# Is the boosted X-X deformation SYMMETRIC (can carry spin-2) or driven by
# an antisymmetric piece (rotation/spin-1)?  Decompose dK_XX.
dKXX = KXX_boost - KXX_stat
sym_frac = np.linalg.norm(0.5*(dKXX + dKXX.T)) / max(np.linalg.norm(dKXX), 1e-300)
asym_frac = np.linalg.norm(0.5*(dKXX - dKXX.T)) / max(np.linalg.norm(dKXX), 1e-300)
print(f"   dK_XX symmetric fraction={sym_frac:.3f}  antisym fraction={asym_frac:.3f} "
      f"(spin-2 needs SYMMETRIC; rotation/spin-1 is antisym)", flush=True)

# =====================================================================
hr("BOOST-ANGLE SWEEP -- the P53-gated experiment (symmetric cross vs angle)")
# =====================================================================
# P53 swept the SPATIAL cut angle -> rotation (spin-1).  P54 sweeps the
# BOOST direction angle: A(phi) = cos(phi) A_x + sin(phi) A_y.  For each
# boost direction we rebuild the boosted vacuum and the wedge kernel's X-X
# block, then measure its traceless cos2theta coupling.  If the boost
# direction modulates the SPIN-2 coupling with a real (refinement-stable)
# amplitude, the Lorentzian congruence is spin-2 VISIBLE.
Ay = boostA_y(Lx, Ly)
PHI = [mp.mpf('0'), mp.pi/4, mp.pi/2]
print("  boost-angle phi | per-norm traceless coupling of dK_XX(phi)", flush=True)
boost_sweep = []
for phi in PHI:
    Aphi = mp.cos(phi)*Ax + mp.sin(phi)*Ay
    Gb = boosted_gamma_mp(Kmp, Aphi, VBOOST, N)
    Grb = reduce_gamma(Gb, ids, N)
    Kb, _ = modular_K_full_mp(Grb)
    dxx = Kb[:B, :B] - KXX_stat
    a2 = amp2(harm(TH, sweep_TL(liftB(dxx))))
    pn = a2 / max(np.linalg.norm(dxx), 1e-300)
    boost_sweep.append(pn)
    print(f"     phi={float(phi):.3f} rad  per-norm cos2 coupling = {pn:.4e} "
          f"[{time.time()-t0:.0f}s]", flush=True)
sweep_modulation = (max(boost_sweep) - min(boost_sweep)) / max(max(boost_sweep), 1e-300)
print(f"   boost-direction modulation of spin-2 coupling = {sweep_modulation:.3f} "
      f"(0 => boost direction IRRELEVANT to spin-2; >0 => direction-sensitive)",
      flush=True)

# =====================================================================
hr("REFINEMENT / FLOOR STABILITY -- is the boosted coupling real?")
# =====================================================================
# The boosted-minus-static difference is a catastrophic cancellation in the
# deep (nu->1/2) modes.  Re-evaluate at a coarser regulator floor; a REAL
# spin-2 signal in the boost must be floor-stable.  (Full a->0 matched-depth
# refinement is GATED to the campaign; this is the floor-sensitivity probe.)
KstatF2, _  = modular_K_full_mp(GrStat,  floor='1e-40')
KboostF2, _ = modular_K_full_mp(GrBoost, floor='1e-40')
dKXX2 = KboostF2[:B, :B] - KstatF2[:B, :B]
a2_dKXX2 = amp2(harm(TH, sweep_TL(liftB(dKXX2))))
n_dKXX2 = np.linalg.norm(dKXX2)
perN_dKXX2 = a2_dKXX2 / max(n_dKXX2, 1e-300)
floor_drift = abs(perN_dKXX - perN_dKXX2) / max(perN_dKXX, 1e-300)
floor_stable = floor_drift < 1e-3
print(f"   per-norm dK_XX coupling: floor 1e-60 -> {perN_dKXX:.6e} ; "
      f"1e-40 -> {perN_dKXX2:.6e}", flush=True)
print(f"   relative floor drift = {floor_drift:.2e}  [floor-stable = {floor_stable}]", flush=True)
print("   (the boosted Williamson + boosted-minus-static is EXACTLY where the", flush=True)
print("    SHARD precision rule bites: deep modes nu->1/2, F(nu) divergence,", flush=True)
print("    catastrophic cancellation. float64 would corrupt this difference.)", flush=True)

# =====================================================================
hr("PROTOTYPE VERDICT (DIRECTION ONLY -- not the P54 result)")
# =====================================================================
print(f"   boost turns on X-P (momentum) sector  : max|G_XP|={GXP_boost:.2e} "
      f"(P49 confirmed: spin-1 reached)", flush=True)
print(f"   boost deforms SPATIAL X-X block        : "
      f"max|dG_XX|={dGXX:.2e}", flush=True)
print(f"   static K_XX spin-2 R2 (P52 BLIND)      : {r_stat:.3e}", flush=True)
print(f"   boosted K_XX spin-2 R2                 : {r_boost:.3e}", flush=True)
print(f"   boost VARIATION dK_XX per-norm/static  : ratio {ratio_pn:.3f} "
      f"(>2 = boost OPENS spin-2 channel)", flush=True)
print(f"   dK_XX symmetric fraction               : {sym_frac:.3f} "
      f"(spin-2 needs symmetric ~1)", flush=True)
print(f"   boost-direction modulates spin-2       : {sweep_modulation:.3f}", flush=True)
print(f"   boosted spin-2 coupling floor-stable   : {floor_stable} "
      f"(drift {floor_drift:.1e})", flush=True)

# DIRECTION call: VISIBLE-leaning iff the boost VARIATION opens a per-norm
# traceless channel that is (a) enhanced vs static, (b) carried by the
# SYMMETRIC X-X block (not spin-1 antisym), AND (c) floor-stable.
visible_lean = bool(boost_opens) and (sym_frac > 0.5) and bool(floor_stable)
blind_lean   = (not boost_opens) and bool(floor_stable)
if visible_lean:
    direction = ("BOOST MAY REACH SPIN-2 (VISIBLE-leaning) -- the boosted X-X "
                 "variation opens a SYMMETRIC, floor-stable traceless channel "
                 "the static kernel lacked.  REFINE on the matched-depth a->0 "
                 "ladder (the P52/P53 collapse-vs-survive test) to confirm.")
elif blind_lean:
    direction = ("BOOST DIRECTION ALSO SPIN-2-BLIND (BLIND-leaning) -- the boost "
                 "deforms the X-P (spin-1/momentum, P49) sector but its SPATIAL "
                 "X-X block carries NO enhanced traceless channel.  The program "
                 "is capped even in the Lorentzian static-congruence sense; the "
                 "spin-2 source remains Frobenius-orthogonal to the boost "
                 "currency.  CONFIRM with matched-depth refinement.")
else:
    direction = ("MIXED / floor-unstable -- the boosted coupling is non-trivial "
                 "but not yet refinement-clean; the decisive test is the "
                 "matched-depth a->0 ladder, GATED to the campaign.")
print(f"\n  PROTOTYPE DIRECTION: {direction}", flush=True)
print("\n  READING (machinery, not verdict): P54 built the FIRST Lorentzian", flush=True)
print("  congruence object -- the wedge modular kernel in the BOOSTED vacuum", flush=True)
print("  (ground state of H - v P_x), a FULL phase-space kernel with the X-P", flush=True)
print("  block P49 showed reaches T_0i.  The decisive measurement is whether the", flush=True)
print("  boost's deformation of the SPATIAL X-X block (the only block a spin-2", flush=True)
print("  source sees) carries a refinement-stable, SYMMETRIC traceless cos2theta", flush=True)
print("  coupling -- the inverse of P52/P53's collapse.  This prototype certifies", flush=True)
print("  the boosted kernel is well-defined, the G_XP receipt (boost reaches the", flush=True)
print("  new sector), the spin-2/spin-1 block decomposition, and the floor", flush=True)
print("  sensitivity.  The CAMPAIGN refines the OPENING (or confirms the BLIND).", flush=True)
print(f"\n[P54 prototype total {time.time()-t0:.0f}s]", flush=True)
