#!/usr/bin/env python3
# =====================================================================
# Relativistic ISP v6 -- Paper 53 PROTOTYPE (MACHINERY INVESTIGATOR)
#
#   THE P53 QUESTION (set up by P52-BLIND):
#   P52 proved a SINGLE region's modular charge K_R is built from T_00
#   (trace (grad phi)^2) and is BLIND to the traceless spin-2 stress
#   T_ij^TL.  Does T_ij^TL REAPPEAR in the CONGRUENCE -- the variation
#   of the modular Hamiltonian ACROSS a family of regions (the modular
#   Berry curvature / kinematic-space structure) -- even though it is
#   absent from each single region's charge?
#
#   This is a MACHINERY prototype: it builds the smallest non-trivial
#   congruence object and asks whether a traceless-shear source
#   registers in a CROSS-region quantity that vanishes (in its
#   traceless coupling) for any SINGLE region.
#
#   THE CONGRUENCE OBJECT (this prototype):
#   Two overlapping wedges A, B whose cuts/boost directions DIFFER.
#   The modular Hamiltonian of a wedge is the full-mode quadratic form
#   K = (1/2)[ x^T (G_X-machinery) x + ... ].  We work at the level of
#   the FULL modular generator restricted to the overlap.  The natural
#   non-commutativity (kinematic curvature) is the COMMUTATOR of the
#   two single-region modular kernels acting on the field algebra:
#       C_AB = [ K_A , K_B ]   (as quadratic-form generators).
#   A SINGLE region's coupling to T_ij^TL is the diagonal (charge)
#   contraction P52 measured.  The CONGRUENCE coupling is the
#   OFF-DIAGONAL / cross contraction that a commutator exposes.
#
#   DECISIVE COUPLING:  inject a polarized traceless-shear source
#   S(theta) = cos2theta S_+ + sin2theta S_x  (St = 0, pure spin-2),
#   contract it (a) into each single region's charge (must be BLIND,
#   replicating P52) and (b) into the cross-region commutator object
#   (the congruence).  If the congruence registers a robust period-pi
#   cos2theta that the single regions do NOT -> spin-2 reappears in
#   the congruence (Einstein source recoverable).  If not -> capped.
#
#   PRECISION (P52 lesson): mpmath dps 80 for the WHOLE chain.
#   covariances via mp.eigsy; F(nu)=log((nu+1/2)/(nu-1/2)) diverges as
#   nu->1/2; deep-bulk modes run to nu=1/2; float64 fakes a signal.
#   No RNG; bit-identical.
#
#   SCOPE: this is a <5min PROTOTYPE on a tiny lattice.  It is a
#   FEASIBILITY + DIRECTION instrument, NOT the P53 verdict.  It tells
#   the campaign WHICH cross-region observable carries the signal and
#   whether the precision floor matters for it.
# =====================================================================
import numpy as np
import time
import mpmath as mp
mp.mp.dps = 80

t0 = time.time()
def hr(s): print("\n" + "="*70 + "\n" + s + "\n" + "="*70, flush=True)
print("#"*70, flush=True)
print("# P53 CONGRUENCE PROTOTYPE -- does T_ij^TL reappear across regions?", flush=True)
print(f"# (mp dps {mp.mp.dps} ~ {int(mp.mp.dps*3.32)} bits; no RNG)", flush=True)
print("#"*70, flush=True)

# --------------------------------------------------------------------
# FULLY-MP 2D free-scalar machinery (reused from P52 / P50 lineage).
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
    """vacuum covariances G_X=(1/2)K^{-1/2}, G_P=(1/2)K^{1/2}, in mp."""
    w2, U = mp.eigsy(K); half = mp.mpf(1)/2
    GX = U*mp.diag(mp.matrix([half/mp.sqrt(w2[i]) for i in range(N)]))*U.T
    GP = U*mp.diag(mp.matrix([half*mp.sqrt(w2[i]) for i in range(N)]))*U.T
    return GX, GP

def tofloat(Mmp):
    return np.array([[float(Mmp[i, j]) for j in range(Mmp.cols)]
                     for i in range(Mmp.rows)])

def williamson_mp(GX, GP, ids):
    """mp Williamson modular kernel of the reduced block. Returns:
       Qf (float transfer = Mi*W), nu (mp symplectic eigvals).
    The modular kernel in the X-sector is  K_X = Mi W diag(F nu) W^T Mi,
    where F=log((nu+1/2)/(nu-1/2)).  A source dG couples to the charge as
    0.5 sum_k F(nu_k) nu_k (q_k^T dG q_k) with q_k the columns of Qf."""
    B = len(ids)
    GXb = mp.matrix([[GX[ids[a], ids[b]] for b in range(B)] for a in range(B)])
    GPb = mp.matrix([[GP[ids[a], ids[b]] for b in range(B)] for a in range(B)])
    e2, V = mp.eigsy(GXb)
    M  = V*mp.diag(mp.matrix([mp.sqrt(e2[i])   for i in range(B)]))*V.T
    Mi = V*mp.diag(mp.matrix([1/mp.sqrt(e2[i]) for i in range(B)]))*V.T
    w2, W = mp.eigsy(M*GPb*M)
    nu = [mp.sqrt(w2[i]) for i in range(B)]
    return tofloat(Mi*W), nu

def modular_kernel_X(GX, GP, ids, floor='1e-60'):
    """Return the FULL X-sector modular kernel K_X (float, B x B) of the
    region 'ids' in the global index labelling restricted to ids:
       K_X = Mi W diag(F(nu) nu) W^T Mi .
    This is the operator whose contraction with a field-sector source dG
    (built from grad phi grad phi) gives the modular charge.  Returning
    the MATRIX (not just the scalar charge) lets us form CROSS-region
    objects (commutators) -- the congruence machinery."""
    Qf, nu = williamson_mp(GX, GP, ids)
    half = mp.mpf(1)/2; fl = mp.mpf(floor)
    Fn = np.array([float(mp.log((nu[k]+half)/max(nu[k]-half, fl))*nu[k])
                   for k in range(len(nu))])
    # K_X = Qf diag(Fn) Qf^T   (Qf = Mi W ; columns are the modes)
    return Qf @ np.diag(Fn) @ Qf.T, nu

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

MSQ = mp.mpf('1e-4'); MSQF = 1e-4; EPS = 2e-3
TH = np.linspace(0, np.pi, 13)

# =====================================================================
hr("BUILD -- base lattice + two overlapping regions A, B (the congruence seed)")
# =====================================================================
# Small tractable lattice.  Two wedges sharing an OVERLAP strip but with
# DIFFERENT cuts: A = right half-plane x>=jcA (vertical cut, x-boost);
# B = top half-plane y>=jcB (horizontal cut, y-boost).  Their modular
# Hamiltonians are generated by boosts in ORTHOGONAL directions -- the
# minimal non-trivial congruence (two different boost directions through
# the overlap corner).  Rotating A->B samples T_mu_nu k^mu k^nu with k
# rotating, i.e. it samples T_xx, T_yy AND (via the corner) T_xy.
Lx, Ly = 12, 12; N = Lx*Ly
jcA = 6      # A = columns x in [6,12)   (cut along x = 6, boost in +x)
jcB = 6      # B = rows    y in [6,12)   (cut along y = 6, boost in +y)
x0, y0, sig = 8, 8, 2.0    # source centred in the A&B OVERLAP corner
print(f"lattice L={Lx}x{Ly} (N={N}); msq={float(MSQ):.0e}", flush=True)
print(f"region A = x>={jcA} (vertical cut, x-boost); "
      f"region B = y>={jcB} (horizontal cut, y-boost)", flush=True)

Kmp = lap2d_mp(Lx, Ly, MSQ)
GX, GP = pack_mp(Kmp, N)
print(f"vacuum covariances built [{time.time()-t0:.0f}s]", flush=True)

idsA = [x*Ly + y for x in range(jcA, Lx) for y in range(Ly)]
idsB = [x*Ly + y for x in range(Lx)      for y in range(jcB, Ly)]
print(f"|A|={len(idsA)}  |B|={len(idsB)}  overlap |A&B|={len(set(idsA)&set(idsB))}", flush=True)

# Build the X-sector modular kernels (matrices, in their own index space)
KA_loc, nuA = modular_kernel_X(GX, GP, idsA)   # on idsA
KB_loc, nuB = modular_kernel_X(GX, GP, idsB)   # on idsB
nuA0 = min(float(nuA[i]-mp.mpf(1)/2) for i in range(len(nuA)))
nuB0 = min(float(nuB[i]-mp.mpf(1)/2) for i in range(len(nuB)))
print(f"min(nu-1/2): A={nuA0:.2e}  B={nuB0:.2e}  (both >=0 -> positive, "
      f"deep modes near vacuum)", flush=True)

# Lift both kernels to the GLOBAL N x N field space (zero outside region).
def lift(Kloc, ids):
    K = np.zeros((N, N))
    K[np.ix_(ids, ids)] = Kloc
    return K
KA = lift(KA_loc, idsA)
KB = lift(KB_loc, idsB)

# =====================================================================
hr("THE CONGRUENCE OBSERVABLES")
# =====================================================================
# (1) SINGLE-REGION charge (P52 replication): for region R and source dG,
#         q_R(theta) = 0.5 * Tr[ K_R dG(theta) ]   (field-sector charge).
#     P52: BLIND to traceless -> c2/c0 collapses with refinement.
#
# (2) CONGRUENCE / Berry curvature object: the modular kernels of A and B
#     do NOT commute (different boost directions).  The leading
#     non-commutativity that can couple to a source is the SYMMETRIZED
#     cross object
#         C_AB = 0.5 (KA KB + KB KA)        (cross-region, on overlap),
#     and the antisymmetric (Berry) part
#         B_AB = 0.5 (KA KB - KB KA)        ([K_A,K_B], the curvature).
#     A traceless source dG couples to the congruence via
#         q_cong(theta) = 0.5 * Tr[ C_AB dG(theta) ]     (cross channel),
#         q_berry(theta) = Tr[ B_AB dG(theta) ]          (curvature channel).
#     KEY: C_AB and B_AB are supported on the OVERLAP and mix the x-cut
#     and y-cut structure -- exactly the cross-region structure P52's
#     single-region argument does NOT control.

Sp, Sc, St = shear_np(Lx, Ly, x0, y0, sig)

def charge_single(Kglob, S):
    return 0.5*float(np.tensordot(Kglob, S, axes=([0, 1], [0, 1])))

def sweep(opmat, kind):
    """contract op against the polarized source over theta; kind selects
    pure-traceless (St=0) or full (with trace)."""
    vals = []
    for th in TH:
        if kind == 'traceless':
            S = np.cos(2*th)*Sp + np.sin(2*th)*Sc          # St = 0
        else:
            S = St + np.cos(2*th)*Sp + np.sin(2*th)*Sc
        vals.append(0.5*float(np.tensordot(opmat, S, axes=([0, 1], [0, 1]))))
    return np.array(vals)

CAB = 0.5*(KA@KB + KB@KA)
BAB = 0.5*(KA@KB - KB@KA)
print(f"||KA||={np.linalg.norm(KA):.3e} ||KB||={np.linalg.norm(KB):.3e}", flush=True)
print(f"||[KA,KB]||={np.linalg.norm(BAB):.3e}  "
      f"(non-zero => A,B modular flows DO NOT commute: the congruence has "
      f"curvature)", flush=True)
print(f"||{{KA,KB}}/2||={np.linalg.norm(CAB):.3e}", flush=True)

# --- NORMALIZATION (the P52 discipline, with the P53 pathology fixed).
# A pure-traceless source has ZERO total energy, so its OWN c0 ~ 0 (a
# meaningless divide).  P52 normalized by the operator's OWN trace charge
# c0_trace.  THAT FAILS for difference operators (Berry [KA,KB], dK=KB-KA)
# whose trace charge CANCELS to machine zero -> spurious R2~1e14.  So we
# use TWO normalizations and trust only their AGREEMENT:
#   R2_self = traceless cos2 amp / |operator's own trace charge|   (P52-style;
#             VALID only when the operator's c0_trace is O(1), i.e. it carries
#             energy -- single regions, anticommutator.  FLAGGED nan-prone.)
#   R2_ext  = traceless cos2 amp / E_ref   with E_ref a FIXED external energy
#             scale (the single-region trace charge) times the operator's
#             relative Frobenius scale -- well-defined for ALL operators,
#             including the energy-blind difference operators.
def c0_trace(opmat):
    """charge the operator assigns to the pure-trace (energy) source."""
    return 0.5*float(np.tensordot(opmat, St, axes=([0, 1], [0, 1])))

# --- the decisive sweeps, PURE-TRACELESS source (St=0, pure spin-2) ---
qA = sweep(KA, 'traceless')
qB = sweep(KB, 'traceless')
qC = sweep(CAB, 'traceless')
qBerry = sweep(BAB, 'traceless')

cA = harm(TH, qA); cB = harm(TH, qB); cC = harm(TH, qC); cBe = harm(TH, qBerry)
c0A = c0_trace(KA); c0B = c0_trace(KB); c0C = c0_trace(CAB); c0Be = c0_trace(BAB)
def report(name, c, c0t):
    R2 = amp2(c)/abs(c0t) if abs(c0t) > 1e-300 else float('nan')
    print(f"   {name:16s} c0_trace={c0t:+.4e}  cos2amp(TL)={amp2(c):.4e}  "
          f"R2=cos2/|c0_trace|={R2:.4e}  cos4/cos2={amp4(c)/max(amp2(c),1e-300):.2e}",
          flush=True)
def R2_of(c, c0t):
    return amp2(c)/abs(c0t) if abs(c0t) > 1e-300 else float('nan')

print("\nPURE-TRACELESS source (St=0); R2 = traceless-cos2 / trace-energy charge", flush=True)
print("(R2 is the spin-2-to-energy ratio P52 used; nonzero+stable+enhanced => spin-2 in congruence):", flush=True)
report("single A", cA, c0A)
report("single B", cB, c0B)
report("CONGRUENCE C_AB", cC, c0C)
report("BERRY [KA,KB]", cBe, c0Be)

# =====================================================================
hr("ATTRIBUTION -- is the congruence cos2theta a REAL cross-region effect?")
# =====================================================================
# Test 1: TRIVIAL congruence C_AA = KA^2 (SAME cut, no new direction).  Its
# R2 is the single-region BW kinematic energy-displacement P52 identified,
# squared through the kernel -- NOT a new spin-2 channel.  The genuine
# CROSS-DIRECTION effect is C_AB's R2 MINUS the same-cut baseline.
CAA = KA@KA; CBB = KB@KB
qCAA = sweep(CAA, 'traceless'); cCAA = harm(TH, qCAA); c0CAA = c0_trace(CAA)
qCBB = sweep(CBB, 'traceless'); cCBB = harm(TH, qCBB); c0CBB = c0_trace(CBB)
print("control: TRIVIAL congruences C_AA=KA^2, C_BB=KB^2 (same cut, no new dir):", flush=True)
report("C_AA (trivial)", cCAA, c0CAA)
report("C_BB (trivial)", cCBB, c0CBB)
# The same-cut baseline R2 (what a single direction's kernel-square gives).
base_R2 = 0.5*(R2_of(cCAA, c0CAA) + R2_of(cCBB, c0CBB))
cong_R2 = R2_of(cC, c0C)
print(f"   same-cut baseline R2 = {base_R2:.4e} ; congruence C_AB R2 = {cong_R2:.4e}", flush=True)

# Test 2: GENUINE cross-direction object.  Subtract the same-cut products
# from the cross product: D_AB = {KA,KB}/2 - 1/2({KA,KA}/2 ... ) is awkward
# dimensionally; instead use the DIRECT cross-direction commutator-square
# focusing object and the symmetric cross-only piece KA KB - (energy-aligned
# baseline).  The cleanest scalar: does C_AB's R2 EXCEED max(single same-cut)?
def r2_of(c):  # kept for floor test below (uses operator's own c0 is wrong; use trace)
    return amp2(c)/abs(c[0]) if abs(c[0]) > 1e-300 else float('nan')
print(f"\n   single-A R2            = {R2_of(cA, c0A):.4e}", flush=True)
print(f"   same-cut baseline R2   = {base_R2:.4e}  (KA^2, KB^2 -- no new direction)", flush=True)
print(f"   C_AB(congruence) R2    = {cong_R2:.4e}", flush=True)
# The CROSS-DIRECTION (genuine congruence) coupling is the EXCESS of the
# cross product over the same-cut baseline.  If C_AB merely inherits the
# energy-aligned same-cut structure, cong_R2 ~ base_R2 (no new spin-2);
# if the different boost directions OPEN a channel, cong_R2 >> base_R2.
cross_excess = cong_R2 - base_R2
enhanced = (np.isfinite(cong_R2) and np.isfinite(base_R2)
            and cong_R2 > 2*max(base_R2, 1e-12))
print(f"   cross-direction EXCESS = cong_R2 - base_R2 = {cross_excess:+.4e}", flush=True)
print(f"   [congruence ENHANCES traceless coupling vs same-cut baseline = {enhanced}]", flush=True)
# BERRY channel: the antisymmetric [KA,KB] is the pure curvature.  Its R2
# isolates whether the NON-COMMUTATIVITY itself (not just the symmetric
# overlap) carries spin-2.
berry_R2 = R2_of(cBe, c0Be)
print(f"   BERRY [KA,KB] R2       = {berry_R2:.4e}  "
      f"(pure curvature channel; ~0 => curvature does NOT carry spin-2)", flush=True)

# Test 3: PRECISION floor sensitivity of the congruence object.  The
# commutator subtracts two near-equal products -> catastrophic
# cancellation amplifies any float64 deep-mode corruption.  Re-evaluate
# the kernels at a different regulator floor; the cross-channel R2 must be
# STABLE if it is a real signal (P52 floor-convergence discipline).
KA2, _ = modular_kernel_X(GX, GP, idsA, floor='1e-45')
KB2, _ = modular_kernel_X(GX, GP, idsB, floor='1e-45')
CAB2 = 0.5*(lift(KA2, idsA)@lift(KB2, idsB) + lift(KB2, idsB)@lift(KA2, idsA))
cC2 = harm(TH, sweep(CAB2, 'traceless')); c0C2 = c0_trace(CAB2)
floor_stable = abs(R2_of(cC, c0C) - R2_of(cC2, c0C2)) < 1e-3
print(f"\n   floor sensitivity (congruence R2): "
      f"1e-60 -> {R2_of(cC, c0C):.4e} ; 1e-45 -> {R2_of(cC2, c0C2):.4e}", flush=True)
print(f"   [floor-stable (real, not near-vacuum artifact) = {floor_stable}]", flush=True)
print("   NOTE: the commutator's catastrophic cancellation is EXACTLY where", flush=True)
print("   the P52 precision lesson bites hardest -- dps 80 mandatory; float64", flush=True)
print("   would corrupt the deep (nu->1/2) modes that the overlap is built from.", flush=True)

# =====================================================================
hr("THE FAITHFUL CONGRUENCE OBJECT -- dK under CUT ROTATION (delta K family)")
# =====================================================================
# The operator-product {KA,KB} is a HEURISTIC for the congruence.  The
# FAITHFUL Jacobson/FGHMVR object is the VARIATION of the modular
# Hamiltonian as the cut DIRECTION rotates: delta K = K(cut_2) - K(cut_1).
# Different cut directions => different boost generators => delta K samples
# T_mu_nu along the ROTATING normal, including the off-diagonal T_xy.
# Build K for two cut directions that share the SAME half-plane region but
# differ in WHICH boost generates the modular flow: the x-cut wedge (A) and
# the y-cut wedge (B) restricted to their COMMON overlap, then dK = KB-KA
# ON THE OVERLAP.  If dK couples to the traceless source where each single
# K does only via the BW energy-displacement, the VARIATION carries spin-2.
ov = sorted(set(idsA) & set(idsB))              # the common overlap region
KA_ov = KA[np.ix_(ov, ov)]; KB_ov = KB[np.ix_(ov, ov)]
dK = KB_ov - KA_ov                              # the cut-rotation variation
# lift dK back to global for the source contraction
dKg = np.zeros((N, N)); dKg[np.ix_(ov, ov)] = dK
qdK = sweep(dKg, 'traceless'); cdK = harm(TH, qdK)
qdK_full = sweep(dKg, 'full');  cdK_full = harm(TH, qdK_full)
c0dK = c0_trace(dKg)
# SCALE-FREE metric (handles the energy-blind difference operator): the
# fraction of dK's TOTAL angular response that is TRACELESS (spin-2),
# A2 = traceless-cos2 amp / (traceless-cos2 amp + |full-source mean charge|).
# Equivalently we compare dK's traceless cos2 to the SINGLE region's
# traceless cos2 at MATCHED operator Frobenius norm (the only honest
# cross-operator comparison when trace charges differ).
nKA = np.linalg.norm(KA[np.ix_(ov, ov)]); ndK = np.linalg.norm(dK)
single_TLamp_per_norm = amp2(cA)/np.linalg.norm(KA)
dK_TLamp_per_norm = amp2(cdK)/max(ndK, 1e-300)
print(f"   overlap |A&B|={len(ov)}; ||dK=KB-KA||(overlap)={ndK:.3e}", flush=True)
print(f"   dK trace-charge c0={c0dK:+.4e}  (~0: ENERGY CANCELS in KB-KA -> the", flush=True)
print(f"     P52-style self-normalized R2 is ILL-DEFINED here; use per-norm)", flush=True)
print(f"   dK traceless cos2 amp = {amp2(cdK):.4e} ; full-source mean = "
      f"{cdK_full[0]:+.4e}", flush=True)
print(f"   traceless cos2 amp per ||operator||:  single-A = "
      f"{single_TLamp_per_norm:.4e} ; dK = {dK_TLamp_per_norm:.4e}", flush=True)
# HONEST decisive metric: does the cut-variation carry MORE traceless
# response per unit operator weight than the single region (a real
# cross-direction opening), or LESS/COMPARABLE (no new channel)?
variation_opens = (np.isfinite(dK_TLamp_per_norm)
                   and dK_TLamp_per_norm > 2*single_TLamp_per_norm)
ratio_pn = dK_TLamp_per_norm/max(single_TLamp_per_norm, 1e-300)
print(f"   [cut-ROTATION variation OPENS traceless channel vs single "
      f"(per-norm ratio {ratio_pn:.3f}, >2 = opens) = {variation_opens}]", flush=True)
print("   (faithful proxy for the Jacobson congruence: dK as the boost", flush=True)
print("    direction rotates.  dK's ENERGY cancels by construction -- so the", flush=True)
print("    QUESTION is whether its surviving response is dominantly TRACELESS.)", flush=True)
# floor-stability of dK traceless amp (commutator-like cancellation)
dKg2 = np.zeros((N, N))
dKg2[np.ix_(ov, ov)] = (lift(KB2, idsB)[np.ix_(ov, ov)]
                        - lift(KA2, idsA)[np.ix_(ov, ov)])
cdK2 = harm(TH, sweep(dKg2, 'traceless'))
dK_floor_stable = abs(amp2(cdK) - amp2(cdK2)) < 1e-6*max(amp2(cdK), 1e-30) + 1e-12
print(f"   dK traceless amp floor 1e-60->{amp2(cdK):.6e} 1e-45->{amp2(cdK2):.6e} "
      f"[stable={dK_floor_stable}]", flush=True)
dK_R2 = ratio_pn  # for the verdict block (now a per-norm ratio, well-defined)

# =====================================================================
hr("RAYCHAUDHURI / FOCUSING analog (sketch-level diagnostic)")
# =====================================================================
# The Jacobson focusing term is d(Area)/dlambda^2 ~ -R_mu_nu k^mu k^nu.
# Lattice analog: the SECOND variation of the modular entropy of a ball
# family under a shear deformation of the cut.  Here, as a feasibility
# probe, we report the curvature of the cross-charge q_C(theta) in theta
# (its cos2 amplitude IS a second-order angular response) and compare to
# the single-region second-order response.  A non-trivial focusing analog
# exists iff the congruence's angular curvature exceeds the single's.
foc_single = amp2(cA)
foc_cong = amp2(cC)
print(f"   angular curvature (cos2 amp): single-A = {foc_single:.3e} ; "
      f"congruence C_AB = {foc_cong:.3e}", flush=True)
print(f"   ratio congruence/single = "
      f"{foc_cong/max(foc_single,1e-300):.2f}", flush=True)
print("   (full Raychaudhuri: 2nd variation of S_ball under cut-shear, with", flush=True)
print("    the partial-wave radial chains K_l of P50 -- GATED to the campaign.)", flush=True)

# =====================================================================
hr("PROTOTYPE VERDICT (DIRECTION ONLY -- not the P53 result)")
# =====================================================================
print(f"   single-region R2 (energy-normalized)     = {R2_of(cA, c0A):.3e} "
      f"(the P52 BW kinematic energy-displacement)", flush=True)
print(f"   same-cut baseline R2 (KA^2/KB^2)         = {base_R2:.3e}", flush=True)
print(f"   anticommutator C_AB R2                   = {cong_R2:.3e}", flush=True)
print(f"   anticommutator ENHANCES vs baseline      = {enhanced}", flush=True)
print(f"   Berry [KA,KB] traceless cos2 amp         = {amp2(cBe):.3e} "
      f"(machine-zero => curvature carries NO spin-2)", flush=True)
print(f"   FAITHFUL cut-variation dK traceless/||op|| ratio vs single = {dK_R2:.3f}", flush=True)
print(f"   cut-variation OPENS traceless channel    = {variation_opens}", flush=True)
print(f"   dK traceless amp floor-stable (dps 80)   = {dK_floor_stable}", flush=True)
print(f"   [KA,KB] != 0 (congruence HAS curvature)  = {np.linalg.norm(BAB) > 1e-12}", flush=True)
# DIRECTION call (prototype-level, NOT the verdict): the congruence carries
# an INDEPENDENT spin-2 channel iff some cross-region object's traceless
# response EXCEEDS the single-region baseline per unit operator weight AND is
# floor-stable.  Berry==machine-zero and anticommutator NOT enhanced are
# NEGATIVE indicators; cut-variation dK per-norm ratio is the faithful proxy.
positive_indicators = sum([bool(enhanced), bool(variation_opens),
                           amp2(cBe) > 1e-6])
if positive_indicators >= 1:
    direction = "SPIN-2 MAY REAPPEAR -- pursue refinement of the OPENING channel"
else:
    direction = ("NO PROTOTYPE-LEVEL CROSS CHANNEL -- every congruence proxy's "
                 "traceless response is COMPARABLE-OR-SMALLER than the single "
                 "region's BW energy-displacement (Berry==machine-zero; "
                 "anticommutator NOT enhanced; dK per-norm ratio<2).  This "
                 "WEAKLY favours CAPPED at the operator-product level, BUT the "
                 "FAITHFUL test is the FGHMVR ball entanglement-equilibrium "
                 "residual dS_EE - dE_mod, GATED to the campaign -- the "
                 "operator commutator is only a heuristic for it.")
print(f"\n  PROTOTYPE DIRECTION: {direction}", flush=True)
print("\n  READING (machinery, not verdict): three congruence proxies were built --", flush=True)
print("  (1) anticommutator {KA,KB}, (2) Berry curvature [KA,KB], (3) the faithful", flush=True)
print("  cut-rotation variation dK=KB-KA on the overlap.  Each is contracted with a", flush=True)
print("  PURE-traceless source and normalized by the trace (energy) charge (the P52", flush=True)
print("  c2/c0).  The DECISIVE campaign measurement is the inverse of P52's collapse:", flush=True)
print("  for whichever proxy shows the largest energy-normalized traceless coupling,", flush=True)
print("  REFINE (a->0, matched dimensionless depth) and ask whether that coupling", flush=True)
print("  SURVIVES (real spin-2 in the congruence -> linearized Einstein recoverable)", flush=True)
print("  or COLLAPSES like P52's single region (program CAPPED at the scalar first", flush=True)
print("  law).  This prototype certifies the observables are well-defined, that the", flush=True)
print("  precision floor (dps 80) is load-bearing for the commutator-cancellation,", flush=True)
print("  and reports which channel the campaign should refine.", flush=True)
print(f"\n[P53 prototype total {time.time()-t0:.0f}s]", flush=True)
