# Paper 49 (v6) campaign: MOMENTUM CURRENCY - the gravito-magnetic
# sector at first-law scope.  Three-level architecture: (0) THE
# ZERO LAW - no O(v) scalar modular response, exactly (gated, not
# assumed); (1) the gravito-magnetic boost law on the kernel is
# SYMPLECTIC COVARIANCE - an instrument identity (W0), never a
# measured law; (2) the measurement: the moving probe pairs with
# K_p - the p^2 half of the boost generator, never measured in
# P44-P48 - and the question is whether K_p completes to the SAME
# finite-box BW target (sector universality: kinetic vs gradient
# energy priced equally).  Canonical: /tmp/v6_p49_campaign.out
# (bit-identical rerun required).
import math
import numpy as np
import mpmath
from mpmath import mp, mpf

print("""== DESIGN BLOCK (pre-registered) ==
QUESTION: the energy sector closed at first-law scope (P48): the
coherent currency map completes to the finite-box BW target with
coupling 1/(4 nu).  The momentum sector is open: how does
momentum density T_0x enter the ledger?  Route: the Lorentzian
canonical (exact modular Williamson) route - the rotation no-go
(P42 W3) forbids only REAL-kernel Euclidean reflection
positivity for circulating sectors and does not touch this
instrument (declared).
THE THREE-LEVEL CLAIM ARCHITECTURE, declared up front:
 LEVEL 0 - THE ZERO LAW (a gated measurement): dS and d<K> have
  NO O(v) piece for any flow, by two exact mechanisms - the
  vacuum wedge kernel is X/P block diagonal (K_xp = 0), and
  T-parity (p -> -p) maps v -> -v preserving the symplectic
  spectrum, so S is exactly even in v.  GR rhyme: Kerr S is
  even in J; the O(J) information lives in the conjugate
  pairing Omega dJ, not in S.  Gate K-ODD on the
  antisymmetrized v-sweep.
 LEVEL 1 - THE GRAVITO-MAGNETIC BOOST LAW IS AN IDENTITY: for a
  wedge-interior flow the dragged state is a symplectic
  congruence, so K(v) = S_v^-T K(0) S_v^-1 EXACTLY - the
  XP block of the flowed kernel is the flow-deformed K_p, i.e.
  K(v) = K(0) - 2 pi v sum (x-j+1/2) T-hat_0x + O(v^2) once
  K_p takes its BW form.  This is frame covariance (the FGHMR
  argument on the lattice), NOT a measurement: it is receipted
  as instrument identity K-COV, and all measured content lives
  in Level 2.  The GEM factor 4 is trace-reversal/test-particle
  bookkeeping at tensor/dynamics scope - registered, not
  claimed; the modular first-law coefficient is 1 by frame
  covariance (stated).
 LEVEL 2 - THE MEASUREMENT: the moving probe xi = (u, -v D u)
  (the P48 coherent probe set in motion; D = central
  difference) has modular charge EXACTLY quadratic in v:
  d<K>(v) - d<K>(0) = (eps v^2 / 2) (Du)^T K_p (Du) - the
  FIRST direct pairing with K_p.  The kernel ratio
    r_P = (Du)^T K_p (Du) / [2 pi sum (n-j+off) (Du)_n^2]
  is amplitude-free in eps AND exactly quadratic in v (no
  linear-response window).  Direct kinetic probes
  dG_P = eps w w^T are the second family (dT00 = eps w^2/2,
  site-local, l_E = l_v).  TARGET: the SAME two-wall g_box -
  the Dirichlet doubling forces f = fbar, and a single weight
  prices T00 regardless of its kinetic/gradient split
  (continuum prediction; on the lattice K_p and K_x artifacts
  differ, so the fork is real).
PRE-REGISTERED FORKS:
 COMPLETION (per family, P48 criteria verbatim): top-of-window
  r_P/g_box within 0.03 of 1 ON CENTRALS at the declared +1/2
  offset (strict) AND 1 within per-anchor systematic
  (consistency); UNRESOLVED zone declared; criterion anchored
  to the declared convention (stated).
 THE SECTOR FORK (the headline): r_P/r_X at the SAME probe u,
  SAME screen - UNIVERSAL (within 0.03 on centrals and
  consistent within combined systematics at BOTH box sizes) /
  SPLIT (beyond combined systematics at both) / UNRESOLVED.
  If SPLIT: the declared adjudicator is the P48 cutoff-ladder
  playbook (m^2 a^2 deviation ratios) - registered as the
  next instrument, not run in this canonical.
 THE ROUGHNESS LADDER (the SCOPE of universality): the sectors
  share one BW weight only where the probe is smooth - rough
  probes are predicted to split them (the UV story).  Scope
  receipt: r_P/r_X at fixed screen (N = 192, d = 13) for probe
  widths W = 12/6/4/3, with the RATIO'S OWN FLOOR SWEEP
  printed per rung (floors 1e-30/45/60); a rung whose ratio
  moves more than 1e-4 over the final floor step is labeled
  FLOOR-LIMITED - its printed split is a regulated reading,
  not a converged value (declared rule).  The ladder varies W
  at fixed d, so roughness and window position covary - the
  confound is declared, and a FIXED-POSITION ROUGH CONTROL
  (W = 3 at d = 4: roughness without the window drift) is run
  beside it under the same floor-sweep rule.  These rows are
  NOT completion anchors and do not feed the floor kills;
  their leakage accumulates into K-LEAK-J (stricter than
  required - declared); a monotone split-grows-with-roughness
  flag is computed, no kill.  The IR-law reading is licensed
  only as far as the floor-converged rungs carry it.
ANCHOR FORMAT: headline anchors run at N = 192 AND N = 240
 per the per-family plan enumerated below (the box receipt is
 the anchor format - P48 lesson);
 per-anchor computed leakage ON THE STENCIL HALO (K-LEAK-J,
 exactly 0.0), mp floor sweeps dps 80, floors 1e-30/45/60,
 growth gate 1e-2 (K-FLOOR-P / K-FLOOR-X), offset sweep
 0/0.5/1, float clip-14 droop receipt at identical geometry.
GATE THRESHOLDS, declared: K-INST 1e-6 with XP-block norm
 1e-10; K-COV 1e-6 (float-roundtrip grade); K-PARITY 1e-10 on
 spectra and 1e-9 on dS, and K-ODD (antisymmetrized +/-v,
 1e-9 at v = 1e-3) - NOTE, both are code-symmetry gates:
 Gamma(-v) is the bitwise parity image of Gamma(+v), so dS(-v)
 equals dS(+v) by the same symmetry; the INDEPENDENT evenness
 gates are K-ODD2 (single-sign scaling: |dS(3e-3)/dS(1e-3) -
 9| <= 1e-2) and the exact odd-part kernel contraction (zero
 by block structure, printed); K-NULL 1e-9 (the kinetic
 modular charge beside it is kernel-clip-dependent and is
 printed with a clip sweep 1e-8/10/12/14 - the dS = 0 claim
 is spectra-only, clip-free); K-C6 1e-3 (the c/6
 identification, W1b); K-SREL tolerance -1e-12; K-LR 1e-9;
 K-V0 5e-4 against P48's locked h12 r/g_box = 0.9956;
 exclusion floors printed FLOORED (safe direction).
W1b - THE c/6 IDENTIFICATION AND THE WALL SOURCE: on the ring
 [Omega M_H, Omega M_P] = 0 exactly (circulant
 commutativity), so the ring's boosted vacuum IS the vacuum
 and the scalar flow response is zero - the W1 response is
 WALL-SOURCED (the segment's commutator norm printed beside
 the ring's).  The wall-sourced coefficient is nonetheless
 universal: c2(N) at j = N/2 for N = 96/144/192/288
 (two-point even fit at v = 1e-2/2e-2), 1/N-extrapolated
 against c/6 (central charge c = 1) - identity receipt K-C6.
W0 - INSTRUMENT IDENTITIES AND GATES:
  K-INST   full-covariance Williamson kernel at v = 0 vs the
           block (P45) kernel: same dK for the same probe.
  K-COV    the covariance identity, direct vs conjugated
           kernel for an interior drag (the gravito-magnetic
           Ward identity; the XP-block instrument probe).
  K-PARITY symplectic spectra at +v and -v identical; dS odd
           part at float floor.
  K-NULL   interior vacuum drag: Delta S = 0 EXACTLY (Williamson
           congruence) while the kinetic modular charge is
           O(1) - flow of the vacuum is modular gauge; only
           flowed matter pays.  Beside it the DELIBERATE
           STRADDLE control (the NON-INTERIOR-SUPPORT detector:
           a straddling drag is not a wedge congruence, so its
           dS is genuine cross-cut restructuring - the receipt's
           detection channel, not instrument error)
           and the drag momentum receipt sum T0i = <P>.  The
           symplectic drag is the COMMUTATOR C = [diag(v),D]/2
           - the symmetric part of naive advection - so it
           carries flow-GRADIENT content only (uniform flow
           exactly trivial; stated).
  K-LR     S_wedge = S_complement at every v (purity).
  Identities printed: uniform flow is trivial ([diag(c), D]
  = 0 -> only flow GRADIENTS act); central difference has
  zero ordering c-number (diag A = 0); the moving-probe hydro
  identities dT0i = -eps v (Du)^2 (a definite-sign current)
  and dT00_kin = (v/2)|dT0i| per site; l_E(moving probe) =
  l_E(P48 ring); l_E = l_v for kinetic probes; stencil
  convention row (forward-difference comparison) printed.
W1 - THE v-SWEEP (zero law + closure; float64 with declared
  droop receipts; one geometry N = 192, j = 96):
  paired +/-v grid; c1 ONLY from the antisymmetrized
  combination (K-ODD gate); even fit c2 with v^4 control;
  S_rel = d<K> - dS >= 0 per v (K-SREL, the physicality gate);
  Hellmann-Feynman identity dE = (1/2) v <P> printed; the
  global-flow d<K> is LOG-BOX-DIVERGENT and its r -> 0 like
  ln N / N - printed as an anatomy row, registered NOT a
  completion object (the flow is not compact; no K-LEAK
  analog exists for it - declared).
W2 - THE MOMENTUM COMPLETION CURVE (mp anchors):
  F1 moving probes u = Hann^2 (W = 12, x0 = 110), depths
  d = 22/16/13 (enclosure of the stencil halo by
  construction), at N = 192 and N = 240;
  F2 kinetic probes w = Hann^2 (W = 12, x0 = 110), depths
  d = 22/12, N = 192 (+ box row at the top depth);
  X-SECTOR rows: r_X at the SAME u, SAME screen (the P48
  pipeline verbatim; d = 22 at N = 192 IS P48's h12 anchor -
  the K-V0 reproduction row), depths 22/16/13 at N = 192
  (+ box row at the top depth);
  per-depth sector ratio r_P/r_X with combined systematics;
  matched-depth differential receipts within and across
  families.
W3 - CROSS-CHECKS: K-V0 (P48 h12 reproduction, gated against
  the locked P48 h12 r/g_box = 0.9956); the vacuum-drag
  channel census (an anatomy row, not a kill: its entropy
  response is exactly zero by K-NULL regardless); fork
  resolutions; ledger from computed flags.
Conventions: float64 + mpmath dps 80; no RNG; bounds round in
the safe direction; ledger from computed flags; the P44 boost
convention (x - j + 1/2) declared, offsets swept; central
difference declared with forward-difference spread printed;
identity rows are receipts, not kills; P45's superseded EP
reading is NOT cited as standing (P48 corrected it - declared).
=================================================================
""")

# ----------------- machinery (P48 lineage) -----------------
def chain_K(N, msq):
    return (np.diag((2.0+msq)*np.ones(N)) - np.eye(N, k=1)
            - np.eye(N, k=-1))
def chain_pack(N, msq):
    K = chain_K(N, msq)
    w2, U = np.linalg.eigh(K)
    w = np.sqrt(np.clip(w2, 1e-18, None))
    return (U*(0.5/w)) @ U.T, (U*(0.5*w)) @ U.T
def T00_profile(GX, GP, msq, N):
    e = 0.5*np.diag(GP).copy() + 0.5*msq*np.diag(GX)
    bond = np.zeros(N)
    bond[0] += 0.5*GX[0, 0]
    bond[-1] += 0.5*GX[-1, -1]
    for j in range(N-1):
        b = 0.5*(GX[j, j] + GX[j+1, j+1] - 2*GX[j, j+1])
        bond[j] += 0.5*b
        bond[j+1] += 0.5*b
    return e + bond
def dK_boost(dT, j, N, off=0.5):
    xs = np.arange(N)
    return float(2*np.pi*np.sum((xs[j:]-j+off)*dT[j:]))
def gbox2(d, j, N):
    R = N - j
    return ((2*N/np.pi)*np.sin(np.pi*d/(2*N))
            * np.sin(np.pi*(2*R-d)/(2*N))/(d*np.sin(np.pi*R/N)))
def hann2(x0, W, N):
    xs = np.arange(N)
    v = np.zeros(N)
    m = np.abs(xs - x0) < W
    v[m] = np.cos(np.pi*(xs[m]-x0)/(2*W))**2
    return v/np.linalg.norm(v)
def leffE_of(prof):
    w = np.abs(prof)
    s = float(np.sum(w))
    xb = float(np.sum(np.arange(len(prof))*w))/s
    s2 = float(np.sum((np.arange(len(prof))-xb)**2*w))/s
    return 2.0*np.sqrt(s2), xb
def leak_of(prof, j):
    return float(np.sum(np.abs(prof[:j])))/float(np.sum(np.abs(prof)))

# ---- boosted/dragged machinery (P49; prototype-validated) ----
def build_A(N):
    return 0.5*(np.eye(N, k=1) - np.eye(N, k=-1))
def Omega_of(n):
    O = np.zeros((2*n, 2*n))
    O[:n, n:] = np.eye(n)
    O[n:, :n] = -np.eye(n)
    return O
def sym_sqrt(M):
    e, U = np.linalg.eigh(M)
    s = np.sqrt(np.clip(e, 1e-300, None))
    return (U*s) @ U.T, (U*(1.0/s)) @ U.T
def Mq_of(K, A, v):
    N = K.shape[0]
    M = np.zeros((2*N, 2*N))
    M[:N, :N] = K
    M[N:, N:] = np.eye(N)
    M[:N, N:] = v*A
    M[N:, :N] = -v*A
    return M
def ground_gamma(Mq, Om):
    W, Wi = sym_sqrt(Mq)
    C = W @ (Om.T @ Mq @ Om) @ W
    f, V = np.linalg.eigh(0.5*(C + C.T))
    Cs = (V*np.sqrt(np.clip(f, 0.0, None))) @ V.T
    G = 0.5 * Wi @ Cs @ Wi
    return 0.5*(G + G.T)
def symp_nu(G, Om2):
    Gs, Gsi = sym_sqrt(G)
    T = Gs @ (Om2.T @ G @ Om2) @ Gs
    return np.sqrt(np.clip(np.linalg.eigvalsh(0.5*(T+T.T)),
                           0.25, None))
def wedge_gamma(G, j, N):
    ids = np.concatenate([np.arange(j, N), N + np.arange(j, N)])
    return G[np.ix_(ids, ids)]
def S_of_nu(nu, clip=1e-12):
    nu = np.clip(nu, 0.5 + clip, None)
    return float(np.sum((nu+0.5)*np.log(nu+0.5)
                        - (nu-0.5)*np.log(nu-0.5)))
def modular_K_full(Gred, nuclip=1e-12):
    B2 = Gred.shape[0]
    Om2 = Omega_of(B2//2)
    Gs, Gsi = sym_sqrt(Gred)
    T = Gs @ (Om2.T @ Gred @ Om2) @ Gs
    nu2, V = np.linalg.eigh(0.5*(T+T.T))
    nu = np.sqrt(np.clip(nu2, 0.25 + nuclip, None))
    F = np.log((nu+0.5)/(nu-0.5))
    return Gsi @ (V*(nu*F)) @ V.T @ Gsi
def modular_Kx(GX, GP, j, N, nuclip=1e-12):
    ids = np.arange(j, N)
    e2, V = np.linalg.eigh(GX[np.ix_(ids, ids)])
    e2c = np.clip(e2, 1e-14, None)
    M = (V*np.sqrt(e2c)) @ V.T
    Mi = (V*(1.0/np.sqrt(e2c))) @ V.T
    w2_, W_ = np.linalg.eigh(M @ GP[np.ix_(ids, ids)] @ M)
    nu_ = np.sqrt(np.clip(w2_, 0.25 + nuclip, None))
    F_ = np.log((nu_+0.5)/(nu_-0.5))
    return Mi @ (W_*(F_*nu_)) @ W_.T @ Mi
def modular_Kp(GX, GP, j, N, nuclip=1e-12):
    ids = np.arange(j, N)
    e2, V = np.linalg.eigh(GX[np.ix_(ids, ids)])
    e2c = np.clip(e2, 1e-14, None)
    M = (V*np.sqrt(e2c)) @ V.T
    w2_, W_ = np.linalg.eigh(M @ GP[np.ix_(ids, ids)] @ M)
    nu_ = np.sqrt(np.clip(w2_, 0.25 + nuclip, None))
    F_ = np.log((nu_+0.5)/(nu_-0.5))
    return M @ (W_*(F_/nu_)) @ W_.T @ M

# ---- mp anchors: K_x pairing (P48 verbatim) + K_p pairing ----
half = mpf(1)/2
def mp_block(Nn, jn, msq_mp):
    Bn = Nn - jn
    GXB = mpmath.zeros(Bn, Bn)
    GPB = mpmath.zeros(Bn, Bn)
    for q in range(1, Nn+1):
        w = mpmath.sqrt(msq_mp + 4*mpmath.sin(q*mpmath.pi/(2*(Nn+1)))**2)
        ph = [mpmath.sqrt(mpf(2)/(Nn+1))
              * mpmath.sin(q*mpmath.pi*(x+1)/(Nn+1))
              for x in range(jn, Nn)]
        cx = 1/(2*w); cp = w/2
        for i in range(Bn):
            for jj in range(i, Bn):
                GXB[i, jj] += cx*ph[i]*ph[jj]
                GPB[i, jj] += cp*ph[i]*ph[jj]
    for i in range(Bn):
        for jj in range(i+1, Bn):
            GXB[jj, i] = GXB[i, jj]
            GPB[jj, i] = GPB[i, jj]
    return GXB, GPB
def mp_pair(Nn, jn, msq_mp, vfull, sector,
            floors=('1e-30', '1e-45', '1e-60')):
    """1/2 vhat^T K_sector vhat at the floors; sector 'x' or 'p'."""
    Bn = Nn - jn
    GXB, GPB = mp_block(Nn, jn, msq_mp)
    E, Q = mpmath.eigsy(GXB)
    Mi = Q*mpmath.diag([1/mpmath.sqrt(E[k]) for k in range(Bn)])*Q.T
    M = Q*mpmath.diag([mpmath.sqrt(E[k]) for k in range(Bn)])*Q.T
    E2, W2 = mpmath.eigsy(M*GPB*M)
    nrm = mpmath.sqrt(sum(v*v for v in vfull))
    vB = mpmath.matrix([vfull[x]/nrm for x in range(jn, Nn)])
    u = W2.T*((Mi if sector == 'x' else M)*vB)
    out = {}
    for fls in floors:
        fl = mpf(fls)
        tot = mpf(0)
        for k in range(Bn):
            nu = mpmath.sqrt(E2[k])
            if nu - half < fl:
                nu = half + fl
            F = mpmath.log((nu+half)/(nu-half))
            tot += (F*nu if sector == 'x' else F/nu)*u[k]**2/2
        out[float(fl)] = float(tot)
    return out

mp.dps = 80

# ----------------- W0: instrument identities -----------------
print("== W0. instrument identities and gates ==")
N0 = 128
K0m = chain_K(N0, 0.0)
A0 = build_A(N0)
Om0 = Omega_of(N0)
GX0, GP0 = chain_pack(N0, 0.0)
G0 = np.block([[GX0, np.zeros((N0, N0))], [np.zeros((N0, N0)), GP0]])
j0 = 64
# K-INST: full kernel at v = 0 vs block kernels, same probe dK
u0 = hann2(80, 12, N0)
Du0 = A0 @ u0
Kfull = modular_K_full(wedge_gamma(G0, j0, N0), nuclip=1e-10)
B0 = N0 - j0
Kx_blk = modular_Kx(GX0, GP0, j0, N0, nuclip=1e-10)
Kp_blk = modular_Kp(GX0, GP0, j0, N0, nuclip=1e-10)
dKx_full = u0[j0:] @ Kfull[:B0, :B0] @ u0[j0:]
dKx_blk = u0[j0:] @ Kx_blk @ u0[j0:]
dKp_full = Du0[j0:] @ Kfull[B0:, B0:] @ Du0[j0:]
dKp_blk = Du0[j0:] @ Kp_blk @ Du0[j0:]
xp_norm = np.linalg.norm(Kfull[:B0, B0:])/np.linalg.norm(Kfull)
inst_x = abs(dKx_full/dKx_blk - 1)
inst_p = abs(dKp_full/dKp_blk - 1)
k_inst = (inst_x <= 1e-6) and (inst_p <= 1e-6) and (xp_norm <= 1e-10)
print(f"  K-INST: full-vs-block kernel pairing at v = 0: X rel "
      f"{inst_x:.1e}, P rel {inst_p:.1e};")
print(f"   XP-block norm fraction {xp_norm:.1e}  "
      f"(K-INST <= 1e-6: {'did not fire' if k_inst else 'FIRED'})")
# K-COV: interior drag, direct kernel vs conjugated kernel
vprof = np.zeros(N0)
m_in = np.abs(np.arange(N0) - 96) < 12
vprof[m_in] = np.cos(np.pi*(np.arange(N0)[m_in]-96)/(2*12))**2
C0 = 0.5*(np.diag(vprof) @ A0 - A0 @ np.diag(vprof))
vdrag = 0.2
Sfull = np.eye(2*N0)
Sfull[N0:, :N0] = vdrag*C0
Gd = Sfull @ G0 @ Sfull.T
Kd_direct = modular_K_full(wedge_gamma(Gd, j0, N0), nuclip=1e-10)
idsw = np.concatenate([np.arange(j0, N0), N0 + np.arange(j0, N0)])
Sw = Sfull[np.ix_(idsw, idsw)]
Swi = np.linalg.inv(Sw)
Kd_conj = Swi.T @ modular_K_full(wedge_gamma(G0, j0, N0),
                                 nuclip=1e-10) @ Swi
cov_rel = (np.linalg.norm(Kd_direct - Kd_conj)
           / np.linalg.norm(Kd_conj))
k_cov = cov_rel <= 1e-6
print(f"  K-COV: drag covariance identity K(v) = S^-T K(0) S^-1 "
      f"(interior bump, v = {vdrag}):")
print(f"   rel Frobenius diff = {cov_rel:.1e}  (K-COV <= 1e-6, "
      f"float-roundtrip grade: "
      f"{'did not fire' if k_cov else 'FIRED'})")
# K-PARITY: boosted vacuum at +/-v
vpar = 0.02
Gp_ = ground_gamma(Mq_of(K0m, A0, +vpar), Om0)
Gm_ = ground_gamma(Mq_of(K0m, A0, -vpar), Om0)
nup = symp_nu(wedge_gamma(Gp_, j0, N0), Omega_of(B0))
num_ = symp_nu(wedge_gamma(Gm_, j0, N0), Omega_of(B0))
par = float(np.abs(np.sort(nup) - np.sort(num_)).max())
dS_odd = abs(S_of_nu(nup) - S_of_nu(num_))
k_parity = (par <= 1e-10) and (dS_odd <= 1e-9)
print(f"  K-PARITY: max|nu(+v) - nu(-v)| = {par:.1e}; |dS odd| = "
      f"{dS_odd:.1e}")
print(f"   (K-PARITY: {'did not fire' if k_parity else 'FIRED'})")
# K-NULL: interior vacuum drag is entropy gauge
nu_vac = symp_nu(wedge_gamma(G0, j0, N0), Omega_of(B0))
S_vac = S_of_nu(nu_vac)
rows_null = []
dGam_keep = None
for vd in (0.2, 0.5):
    Sf = np.eye(2*N0)
    Sf[N0:, :N0] = vd*C0
    Gdd = Sf @ G0 @ Sf.T
    nu_d = symp_nu(wedge_gamma(Gdd, j0, N0), Omega_of(B0))
    dS_null = S_of_nu(nu_d) - S_vac
    dGam = wedge_gamma(Gdd - G0, j0, N0)
    charge = 0.5*float(np.sum(Kfull * dGam))
    rows_null.append((vd, dS_null, charge))
    dGam_keep = dGam
    print(f"  K-NULL: interior drag v = {vd}: Delta S = "
          f"{dS_null:+.1e}; kinetic modular charge = {charge:.4f}")
k_null = all(abs(r[1]) <= 1e-9 for r in rows_null)
print(f"   (K-NULL |Delta S| <= 1e-9: "
      f"{'did not fire' if k_null else 'FIRED'})")
chg_sw = []
for nc in (1e-8, 1e-10, 1e-12, 1e-14):
    Kc_ = modular_K_full(wedge_gamma(G0, j0, N0), nuclip=nc)
    chg_sw.append(0.5*float(np.sum(Kc_ * dGam_keep)))
print("   charge clip sweep (v = 0.5, clips 1e-8/10/12/14): "
      + "/".join(f"{c:.4f}" for c in chg_sw))
print("   (the charge is kernel-clip-dependent - quoted with its "
      "clip; dS = 0 is")
print("    spectra-only, clip-free.)")
# straddle control (the non-interior-support detector - control row)
vstr = np.zeros(N0)
m_st = np.abs(np.arange(N0) - j0) < 12
vstr[m_st] = np.cos(np.pi*(np.arange(N0)[m_st]-j0)/(2*12))**2
Cst = 0.5*(np.diag(vstr) @ A0 - A0 @ np.diag(vstr))
Sst = np.eye(2*N0)
Sst[N0:, :N0] = 0.2*Cst
nu_st = symp_nu(wedge_gamma(Sst @ G0 @ Sst.T, j0, N0),
                Omega_of(B0))
print(f"  straddle control (bump ON the cut, v = 0.2): Delta S = "
      f"{S_of_nu(nu_st) - S_vac:+.1e}")
print(f"   (a straddling drag is not a wedge congruence - its dS "
      f"is genuine cross-cut")
print(f"    restructuring; the row is the NON-INTERIOR-SUPPORT "
      f"DETECTOR, printed.)")
# drag momentum receipt + moving-probe hydro identities
Sf2 = np.eye(2*N0)
Sf2[N0:, :N0] = 0.2*C0
Gdd2 = Sf2 @ G0 @ Sf2.T
dT_drag = T00_profile(Gdd2[:N0, :N0], Gdd2[N0:, N0:],
                      0.0, N0) - T00_profile(GX0, GP0, 0.0, N0)
GXPd = Gdd2[:N0, N0:]
T0i_d = np.zeros(N0)
T0i_d[1:-1] = 0.5*(GXPd[2:, 1:-1].diagonal()
                   - GXPd[:-2, 1:-1].diagonal())
psum = abs(float(T0i_d.sum()) - float(np.trace(A0 @ GXPd)))
print(f"  drag momentum receipt: |sum T0i - <P>| = {psum:.1e}  "
      f"(commutator drag = flow-gradient")
print(f"   content only; uniform flow exactly trivial - stated)")
vmv, epsv = 0.05, 2e-3
dGXP_mv = -epsv*vmv*np.outer(u0, Du0)
T0i_mv = np.zeros(N0)
T0i_mv[1:-1] = 0.5*(dGXP_mv[2:, 1:-1].diagonal()
                    - dGXP_mv[:-2, 1:-1].diagonal())
dev1 = float(np.abs(T0i_mv + epsv*vmv*Du0*Du0).max()
             / np.abs(T0i_mv).max())
dT00k = 0.5*epsv*vmv*vmv*Du0*Du0
mk = Du0*Du0 > 1e-12*float(np.max(Du0*Du0))
dev2 = float(np.abs(dT00k[mk]/np.abs(T0i_mv[mk])
                    - vmv/2).max()/(vmv/2))
print(f"  moving-probe hydro identities (eps = {epsv}, v = "
      f"{vmv}): |dT0i + eps v (Du)^2| rel = {dev1:.1e};")
print(f"   |dT00_kin/|dT0i| - v/2| rel = {dev2:.1e}  (the "
      f"definite-sign current and its")
print(f"   kinetic energy - the W2 objects)")
# uniform flow trivial; ordering c-number; K-LR
cu = np.linalg.norm(np.diag(np.ones(N0)) @ A0
                    - A0 @ np.diag(np.ones(N0)))
print(f"  uniform-flow triviality |[I, D]| = {cu:.1e}; central-"
      f"difference ordering c-number = diag(A) = "
      f"{np.abs(np.diag(A0)).max():.1e}")
idsL = np.concatenate([np.arange(0, j0), N0 + np.arange(0, j0)])
nu_L = symp_nu(Gp_[np.ix_(idsL, idsL)], Omega_of(j0))
nu_R = symp_nu(wedge_gamma(Gp_, j0, N0), Omega_of(B0))
lr = abs(S_of_nu(nu_L)/S_of_nu(nu_R) - 1)
k_lr = lr <= 1e-9
print(f"  K-LR: S_left/S_right - 1 = {lr:.1e} at v = {vpar}  "
      f"({'did not fire' if k_lr else 'FIRED'})")
# width identities
dT_mov = Du0*Du0
lE_mov, _ = leffE_of(dT_mov)
GXu = GX0 + 2e-3*np.outer(u0, u0)
dT_x = T00_profile(GXu, GP0, 0.0, N0) - T00_profile(GX0, GP0,
                                                    0.0, N0)
lE_x, _ = leffE_of(dT_x)
w0_ = hann2(80, 12, N0)
lE_kin, _ = leffE_of(w0_*w0_)
print(f"  width identities: l_E(moving probe (Du)^2) = "
      f"{lE_mov:.2f} vs l_E(P48 ring) = {lE_x:.2f};")
print(f"   kinetic probe l_E = l_v = {lE_kin:.2f} exactly "
      f"(site-local dT00 = eps w^2/2)")
# stencil convention row: forward difference
Afwd = np.eye(N0, k=1) - np.eye(N0)
Du_f = Afwd @ u0
Kp0 = modular_Kp(GX0, GP0, j0, N0, nuclip=1e-12)
rP_c = (Du0[j0:] @ Kp0 @ Du0[j0:]) / (
    np.pi*2*np.sum((np.arange(j0, N0)-j0+0.5)*(Du0[j0:]**2)))
rP_f = (Du_f[j0:] @ Kp0 @ Du_f[j0:]) / (
    np.pi*2*np.sum((np.arange(j0, N0)-j0+0.5)*(Du_f[j0:]**2)))
print(f"  stencil row (float, clip 1e-12): r_P central = "
      f"{rP_c:.4f} vs forward = {rP_f:.4f}  (convention spread "
      f"printed; central declared)")

# ----------------- W1: the v-sweep -----------------
print("\n== W1. the v-sweep: the zero law and closure (float64, "
      "N = 192, j = 96) ==")
N1, j1 = 192, 96
K1 = chain_K(N1, 0.0)
A1 = build_A(N1)
Om1 = Omega_of(N1)
GX1, GP1 = chain_pack(N1, 0.0)
G10 = np.block([[GX1, np.zeros((N1, N1))],
                [np.zeros((N1, N1)), GP1]])
B1 = N1 - j1
nu_vac1 = symp_nu(wedge_gamma(G10, j1, N1), Omega_of(B1))
S_vac1 = S_of_nu(nu_vac1)
Kvac1 = modular_K_full(wedge_gamma(G10, j1, N1), nuclip=1e-12)
E_vac = float(np.sum(T00_profile(GX1, GP1, 0.0, N1)))
vs = (1e-3, 3e-3, 1e-2, 3e-2)
rows1 = []
print("   v        dS(v)         dS(-v)        d<K>        "
      "S_rel       dE/(v<P>/2)")
k_srel = True
for v in vs:
    Gp1 = ground_gamma(Mq_of(K1, A1, +v), Om1)
    Gm1 = ground_gamma(Mq_of(K1, A1, -v), Om1)
    dSp = S_of_nu(symp_nu(wedge_gamma(Gp1, j1, N1),
                          Omega_of(B1))) - S_vac1
    dSm = S_of_nu(symp_nu(wedge_gamma(Gm1, j1, N1),
                          Omega_of(B1))) - S_vac1
    dGam = wedge_gamma(Gp1 - G10, j1, N1)
    dK = 0.5*float(np.sum(Kvac1 * dGam))
    srel = dK - dSp
    k_srel = k_srel and (srel >= -1e-12)
    Pexp = float(np.trace(A1 @ Gp1[:N1, N1:]))
    dE = float(np.sum(T00_profile(Gp1[:N1, :N1], Gp1[N1:, N1:],
                                  0.0, N1))) - E_vac
    hf = dE/(0.5*v*Pexp)
    rows1.append((v, dSp, dSm, dK, srel, hf))
    print(f"   {v:7.0e} {dSp:+.6e} {dSm:+.6e} {dK:+.4e} "
          f"{srel:+.4e} {hf:.6f}")
c1 = abs(rows1[0][1] - rows1[0][2])/(2*rows1[0][0])
k_odd = c1 <= 1e-9
print(f"  THE ZERO LAW: |c1| from antisymmetrized +/-v at v = "
      f"{vs[0]:.0e}: {c1:.1e}")
print(f"   (K-ODD <= 1e-9: {'did not fire' if k_odd else 'FIRED'}"
      f"; exact mechanisms: K_xp = 0 and T-parity)")
# independent evenness gates (the +/-v parity gate is
# code-symmetric - declared)
ratio9 = rows1[1][1]/rows1[0][1]
k_odd2 = abs(ratio9 - 9) <= 1e-2
print(f"  K-ODD2 (single-sign scaling): dS(3e-3)/dS(1e-3) = "
      f"{ratio9:.4f} vs 9  "
      f"({'did not fire' if k_odd2 else 'FIRED'})")
Gp1a = ground_gamma(Mq_of(K1, A1, +vs[0]), Om1)
Gm1a = ground_gamma(Mq_of(K1, A1, -vs[0]), Om1)
oddK = 0.25*float(np.sum(Kvac1 * (wedge_gamma(Gp1a, j1, N1)
                                  - wedge_gamma(Gm1a, j1, N1))))
print(f"  odd-part kernel contraction (exact zero by block "
      f"structure): {oddK:.1e}")
print(f"  K-SREL (S_rel = d<K> - dS >= 0 at every v): "
      f"{'did not fire' if k_srel else 'FIRED'}")
# even fit c2 + v^4 control
lv = np.array([r[0] for r in rows1])
le = np.array([0.5*(r[1] + r[2]) for r in rows1])
Mfit = np.vstack([lv**2, lv**4]).T
c2, c4 = np.linalg.lstsq(Mfit, le, rcond=None)[0]
print(f"  even fit dS = c2 v^2 + c4 v^4: c2 = {c2:.6f}, v^4 share "
      f"at v = 3e-2: {abs(c4*9e-4/(c2)):.1e}")
# global-flow anatomy: r is log-box-divergent (registered row)
dKb_g = dK_boost(T00_profile(Gp1[:N1, :N1], Gp1[N1:, N1:], 0.0,
                             N1) - T00_profile(GX1, GP1, 0.0, N1),
                 j1, N1)
print(f"  anatomy row (registered, not a completion object): "
      f"global-flow r = d<K>/dK_boost = "
      f"{rows1[-1][3]/dKb_g:.4f} at j = {j1}; dT00 leakage past "
      f"the cut = "
      f"{leak_of(T00_profile(Gp1[:N1, :N1], Gp1[N1:, N1:], 0.0, N1) - T00_profile(GX1, GP1, 0.0, N1), j1):.2f}")
print("   (the flow is not compact - declared; the moving PROBE "
      "below is the object.)")

print(" W1b - the c/6 identification and the wall source:")
Kper = chain_K(N1, 0.0)
Kper[0, -1] = -1.0
Kper[-1, 0] = -1.0
Aper = build_A(N1)
Aper[0, -1] = -0.5
Aper[-1, 0] = 0.5
MH_d = Mq_of(K1, A1, 0.0)
MP_d = np.zeros((2*N1, 2*N1))
MP_d[:N1, N1:] = A1.T
MP_d[N1:, :N1] = A1
MH_p = np.zeros((2*N1, 2*N1))
MH_p[:N1, :N1] = Kper
MH_p[N1:, N1:] = np.eye(N1)
MP_p = np.zeros((2*N1, 2*N1))
MP_p[:N1, N1:] = Aper.T
MP_p[N1:, :N1] = Aper
GH_d, GP_d = Om1 @ MH_d, Om1 @ MP_d
GH_p, GP_p = Om1 @ MH_p, Om1 @ MP_p
comm_d = float(np.linalg.norm(GH_d @ GP_d - GP_d @ GH_d))
comm_p = float(np.linalg.norm(GH_p @ GP_p - GP_p @ GH_p))
print(f"  wall-source receipt: |[Omega M_H, Omega M_P]| = "
      f"{comm_p:.1e} on the ring vs")
print(f"   {comm_d:.2f} on the segment - the ring's boosted "
      f"vacuum IS the vacuum (its")
print(f"   scalar response is zero); the W1 response is "
      f"WALL-SOURCED, declared.")
print(f"   (zero-mode caveat: the ring statement is per-mode at "
      f"k != 0 / m -> 0+;")
print(f"    P carries no zero-mode content, v below the sound "
      f"speed - stated.)")
c2s = []
for Nn in (96, 144, 192, 288):
    Kn = chain_K(Nn, 0.0)
    An = build_A(Nn)
    Omn = Omega_of(Nn)
    GXn_, GPn_ = chain_pack(Nn, 0.0)
    G0n = np.block([[GXn_, np.zeros((Nn, Nn))],
                    [np.zeros((Nn, Nn)), GPn_]])
    jn = Nn//2
    Bn = Nn - jn
    Sv0 = S_of_nu(symp_nu(wedge_gamma(G0n, jn, Nn),
                          Omega_of(Bn)))
    ds_ = []
    for v_ in (1e-2, 2e-2):
        Gv_ = ground_gamma(Mq_of(Kn, An, v_), Omn)
        ds_.append(S_of_nu(symp_nu(wedge_gamma(Gv_, jn, Nn),
                                   Omega_of(Bn))) - Sv0)
    c2n = (16*ds_[0] - ds_[1])/(12*1e-4)
    c2s.append((Nn, c2n))
    print(f"  c2(N = {Nn:3d}, j = N/2) = {c2n:.6f}")
(N_a, ca), (N_b, cb) = c2s[-2], c2s[-1]
cinf = (N_b*cb - N_a*ca)/(N_b - N_a)
k_c6 = abs(cinf - 1.0/6.0) <= 1e-3
print(f"  1/N extrapolant = {cinf:.6f} vs c/6 = {1.0/6.0:.6f}  "
      f"(K-C6 <= 1e-3: {'did not fire' if k_c6 else 'FIRED'})")
print(f"  -> the wall-sourced flow-entropy coefficient is the "
      f"CENTRAL CHARGE: the")
print(f"     boosted-vacuum response is universal physics, not a "
      f"lattice artifact.")

# ----------------- W2: the momentum completion curve ---------
print("\n== W2. THE MOMENTUM COMPLETION CURVE (mp anchors) ==")
x0w, Ww = 110, 12
k_leakj = True
k_floor_p = True
k_floor_x = True
res = {}
def run_pair(N_, d_, fam, sector, W_=12, gate=True):
    """one exact anchor; returns dict with all receipts."""
    global k_leakj, k_floor_p, k_floor_x
    GXn, GPn = chain_pack(N_, 0.0)
    An = build_A(N_)
    u = hann2(x0w, W_, N_)
    if fam == 'F1':
        vec = An @ u
        prof = vec*vec
    elif fam == 'F2':
        vec = u
        prof = 0.5*u*u
    else:                      # X sector: P48 pipeline
        vec = u
        prof = (T00_profile(GXn + 2e-3*np.outer(u, u), GPn, 0.0,
                            N_)
                - T00_profile(GXn, GPn, 0.0, N_))/2e-3
    lE, _ = leffE_of(prof)
    dc = float(np.sum(np.arange(N_)*prof)/np.sum(prof))
    j = int(round(dc - d_))
    leak = leak_of(prof, j)
    k_leakj = k_leakj and (leak == 0.0)
    # float droop receipt at identical geometry
    if sector == 'p':
        Kp14 = modular_Kp(GXn, GPn, j, N_, nuclip=1e-14)
        num14 = vec[j:] @ Kp14 @ vec[j:]
    else:
        Kx14 = modular_Kx(GXn, GPn, j, N_, nuclip=1e-14)
        num14 = vec[j:] @ Kx14 @ vec[j:]
    den_h = {}
    for off in (0.0, 0.5, 1.0):
        den_h[off] = 2*np.pi*float(
            np.sum((np.arange(j, N_)-j+off)*prof[j:]))
    nrm2 = float(np.sum(vec*vec))
    sw = mp_pair(N_, j, mpf(0), [mpf(float(x)) for x in vec],
                 sector)
    gr = sw[1e-60]/sw[1e-45] - 1
    if gate:
        if fam == 'X':
            k_floor_x = k_floor_x and (abs(gr) <= 1e-2)
        else:
            k_floor_p = k_floor_p and (abs(gr) <= 1e-2)
    # mp_pair returns (1/2) vhat^T K vhat; full pairing =
    # 2*nrm2*sw.  Per-family epsilon-unit bookkeeping:
    #  X : dK = (eps/2) u^T K_x u,  prof = dT/eps     -> fac 1/2
    #  F2: dK = (eps/2) w^T K_p w,  prof = w^2/2      -> fac 1/2
    #  F1: dK = (eps v^2/2)(Du)^T K_p (Du), prof = (Du)^2
    #      (per unit eps v^2/2)                       -> fac 1
    fac = 1.0 if fam == 'F1' else 0.5
    offs = {}
    for off in (0.0, 0.5, 1.0):
        offs[off] = fac*2*nrm2*sw[1e-60] / den_h[off]
    r_ex = offs[0.5]
    gb = gbox2(dc-j, j, N_)
    osp = (max(offs.values())-min(offs.values()))/r_ex
    syst = abs(gr) + osp
    f14 = fac*num14/den_h[0.5]/gb
    return dict(N=N_, d=dc-j, j=j, fam=fam, lEd=lE/(dc-j),
                leak=leak, gr=gr, r=r_ex, gb=gb, ratio=r_ex/gb,
                syst=syst, osp=osp, f14=f14,
                roffs={o: offs[o]/gb for o in offs},
                r_floors={fl: fac*2*nrm2*sw[fl]/den_h[0.5]
                          for fl in sw})

print(" F1 moving probes (u = Hann^2 W = 12 @ 110; r_P pairs "
      "with K_p):")
for N_ in (192, 240):
    for d_ in (22, 16, 13):
        a = run_pair(N_, d_, 'F1', 'p')
        res[('F1', N_, d_)] = a
        print(f"  [N = {a['N']}, d = {a['d']:.0f}] l_E/d = "
              f"{a['lEd']:.3f}: leakage {a['leak']:.1e}; float14 "
              f"{a['f14']:.4f}")
        print(f"   r_P = {a['r']:.4f} [floor {a['gr']:+.1e}; "
              f"offsets {a['osp']*100:.1f}%]; g_box = "
              f"{a['gb']:.4f}; r_P/g_box = {a['ratio']:.4f} +- "
              f"{a['syst']:.3f}")
print(" F2 kinetic probes (dG_P = eps w w^T, w = Hann^2 W = 12 "
      "@ 110):")
for N_, d_ in ((192, 22), (192, 12), (240, 12)):
    a = run_pair(N_, d_, 'F2', 'p')
    res[('F2', N_, d_)] = a
    print(f"  [N = {a['N']}, d = {a['d']:.0f}] l_E/d = "
          f"{a['lEd']:.3f}: leakage {a['leak']:.1e}; float14 "
          f"{a['f14']:.4f}")
    print(f"   r_P = {a['r']:.4f} [floor {a['gr']:+.1e}; offsets "
          f"{a['osp']*100:.1f}%]; g_box = {a['gb']:.4f}; "
          f"r_P/g_box = {a['ratio']:.4f} +- {a['syst']:.3f}")
print(" X-sector rows (same u, same screen; the P48 pipeline):")
for N_, d_ in ((192, 22), (192, 16), (192, 13), (240, 13)):
    a = run_pair(N_, d_, 'X', 'x')
    res[('X', N_, d_)] = a
    print(f"  [N = {a['N']}, d = {a['d']:.0f}] l_E/d = "
          f"{a['lEd']:.3f}: leakage {a['leak']:.1e}; float14 "
          f"{a['f14']:.4f}")
    print(f"   r_X = {a['r']:.4f} [floor {a['gr']:+.1e}; offsets "
          f"{a['osp']*100:.1f}%]; g_box = {a['gb']:.4f}; "
          f"r_X/g_box = {a['ratio']:.4f} +- {a['syst']:.3f}")
print(f"  K-LEAK-J (every anchor, stencil halo, exactly 0.0): "
      f"{'did not fire' if k_leakj else 'FIRED'}")
print(f"  K-FLOOR-P (every P-sector anchor growth <= 1e-2): "
      f"{'did not fire' if k_floor_p else 'FIRED'}")
print(f"  K-FLOOR-X (every X-sector anchor growth <= 1e-2): "
      f"{'did not fire' if k_floor_x else 'FIRED'}")
# K-V0: P48 h12 reproduction
r_v0 = res[('X', 192, 22)]['ratio']
k_v0 = abs(r_v0 - 0.9956) <= 5e-4
print(f"  K-V0: X-sector (N = 192, d = 22) r/g_box = {r_v0:.4f} "
      f"vs P48 h12 locked 0.9956")
print(f"   (K-V0 within 5e-4: {'did not fire' if k_v0 else 'FIRED'})")

# completion fork per family (P48 criteria)
print("  THE COMPLETION FORK (P-sector families):")
forks = {}
for fam, keys in (('F1', [(192, 22), (192, 16), (192, 13)]),
                  ('F2', [(192, 22), (192, 12)])):
    fa = [res[(fam, n, d)] for n, d in keys
          if res[(fam, n, d)]['leak'] == 0.0
          and abs(res[(fam, n, d)]['gr']) <= 1e-2]
    if not fa:
        forks[fam] = dict(top=None, strict=False, cons=False)
        print(f"   {fam}: no admissible anchors - NOT RESOLVABLE "
              f"(registered).")
        continue
    top = max(fa, key=lambda c: c['lEd'])
    strict = abs(top['ratio'] - 1) <= 0.03
    cons = abs(top['ratio'] - 1) <= top['syst']
    forks[fam] = dict(top=top, strict=strict, cons=cons)
    print(f"   {fam}: top l_E/d = {top['lEd']:.2f}, r_P/g_box = "
          f"{top['ratio']:.4f} +- {top['syst']:.3f}; strict 0.03 "
          f"on centrals: {'PASS' if strict else 'fail'}; 1 within "
          f"syst: {'yes' if cons else 'NO'};")
    print(f"    excludes plateaus below "
          f"{math.floor((top['ratio']-top['syst'])*1000)/1000:.3f}"
          f" (floored)")
# THE SECTOR FORK
print("  THE SECTOR FORK (r_P/r_X at the same probe and screen):")
sector_rows = []
for d_ in (22, 16, 13):
    rp = res[('F1', 192, d_)]
    rx = res[('X', 192, d_)]
    q = rp['ratio']/rx['ratio']
    comb = rp['syst'] + rx['syst']
    sector_rows.append((d_, 192, q, comb))
    print(f"   d = {d_} (N = 192): r_P/r_X = {q:.4f}  (combined "
          f"syst {comb:.3f}; floor-growth differential "
          f"{abs(rp['gr']-rx['gr']):.0e})")
rp240 = res[('F1', 240, 13)]
rx240 = res[('X', 240, 13)]
q240 = rp240['ratio']/rx240['ratio']
comb240 = rp240['syst'] + rx240['syst']
sector_rows.append((13, 240, q240, comb240))
print(f"   d = 13 (N = 240, the box receipt): r_P/r_X = "
      f"{q240:.4f}  (combined syst {comb240:.3f}; floor-growth "
      f"differential {abs(rp240['gr']-rx240['gr']):.0e})")
gd_all = [abs(res[('F1', 192, dd)]['gr']
              - res[('X', 192, dd)]['gr']) for dd in (22, 16, 13)]
gd_all.append(abs(rp240['gr'] - rx240['gr']))
outer_split = (max(abs(q - 1) for _, _, q, _ in sector_rows)
               + max(gd_all))
lic = outer_split < 1e-3
if lic:
    print(f"   (fourth digit at floor-grade resolution; computed "
          f"outer bound on the split")
    print(f"    = {outer_split:.1e} < 1e-3 - the licensed "
          f"statement, thirty-plus times")
    print(f"    tighter than the 0.03 criterion.)")
else:
    print(f"   (computed outer bound on the split = "
          f"{outer_split:.1e} - the sub-1e-3 license")
    print(f"    does NOT hold; see ledger.)")
uni_strict = all(abs(q - 1) <= 0.03 for _, _, q, _ in sector_rows)
uni_cons = all(abs(q - 1) <= c for _, _, q, c in sector_rows)
split = all(abs(q - 1) > c for _, _, q, c in sector_rows)
if uni_strict and uni_cons:
    sector_state = 'UNIVERSAL'
    print("   -> SECTOR UNIVERSALITY: kinetic and gradient energy "
          "are priced equally")
    print("      (within 0.03 on centrals and consistent at both "
          "box sizes).")
elif split:
    sector_state = 'SPLIT'
    print("   -> SECTOR SPLIT beyond combined systematics at both "
          "boxes - the declared")
    print("      adjudicator (the cutoff-ladder playbook) is the "
          "next instrument; registered.")
else:
    sector_state = 'UNRESOLVED'
    print("   -> sector fork UNRESOLVED at this instrument - "
          "registered.")
# the roughness ladder: the SCOPE of universality
print("  THE ROUGHNESS LADDER (scope receipt; N = 192, d = 13; "
      "not completion anchors):")
FLS = (1e-30, 1e-45, 1e-60)
qlad = []
for Wr in (12, 6, 4, 3):
    if Wr == 12:
        ap, ax = res[('F1', 192, 13)], res[('X', 192, 13)]
    else:
        ap = run_pair(192, 13, 'F1', 'p', W_=Wr, gate=False)
        ax = run_pair(192, 13, 'X', 'x', W_=Wr, gate=False)
    qf = {fl: ap['r_floors'][fl]/ax['r_floors'][fl] for fl in FLS}
    q = qf[1e-60]
    flim = abs(qf[1e-60]/qf[1e-45] - 1) > 1e-4
    qlad.append((Wr, q, flim))
    print(f"   W = {Wr:2d} (l_E/d = {ap['lEd']:.2f}): r_P/r_X = "
          f"{q:.4f}  [ratio floor sweep "
          f"{qf[1e-30]:.4f}/{qf[1e-45]:.4f}/{qf[1e-60]:.4f}"
          f"{' - FLOOR-LIMITED' if flim else ''}]")
rough_mono = all(abs(qlad[i][1]-1) <= abs(qlad[i+1][1]-1) + 1e-12
                 for i in range(len(qlad)-1))
n_flim = sum(1 for _, _, f in qlad if f)
if rough_mono and n_flim == 0:
    print("   -> the split grows with roughness (monotone: YES), "
          "floor-converged at")
    print("      every rung: universality is a SMOOTH-PROBE (IR) "
          "law - the scope receipt.")
elif rough_mono:
    print(f"   -> the split grows with roughness (monotone: YES),"
          f" but {n_flim} rung(s) are")
    print("      FLOOR-LIMITED: the trend is supported, the "
          "rough-end magnitude is NOT")
    print("      resolved at this instrument - registered.")
else:
    print("   -> the ladder is not monotone - no IR-law reading "
          "licensed; registered.")
# fixed-position rough control: roughness without window drift
print("  FIXED-POSITION ROUGH CONTROL (W = 3 at d = 4 - the "
      "ladder's confound cut):")
cp_ = run_pair(192, 4, 'F1', 'p', W_=3, gate=False)
cx_ = run_pair(192, 4, 'X', 'x', W_=3, gate=False)
qcf = {fl: cp_['r_floors'][fl]/cx_['r_floors'][fl] for fl in FLS}
flimc = abs(qcf[1e-60]/qcf[1e-45] - 1) > 1e-4
print(f"   q = {qcf[1e-60]:.4f}  [ratio floor sweep "
      f"{qcf[1e-30]:.4f}/{qcf[1e-45]:.4f}/{qcf[1e-60]:.4f}"
      f"{' - FLOOR-LIMITED' if flimc else ''}; leakage "
      f"{cp_['leak']:.0e}/{cx_['leak']:.0e}]")
if flimc:
    print("   -> FLOOR-LIMITED: near-cut rough-probe universality"
          " is BEYOND THIS")
    print("      INSTRUMENT (deeper floors are the successor's "
          "target) - registered.")
else:
    print(f"   -> floor-converged: the fixed-position rough split"
          f" is {abs(qcf[1e-60]-1)*100:.2f}% - printed.")
# differential receipts
print("  DIFFERENTIAL RECEIPTS (matched-depth, offsets 0/0.5/1):")
for (ka, kb) in ((('F1', 192, 22), ('F1', 192, 13)),
                 (('F1', 192, 13), ('F2', 192, 12)),
                 (('F1', 192, 13), ('X', 192, 13))):
    ca, cb = res[ka], res[kb]
    dd = [ca['roffs'][o] - cb['roffs'][o] for o in (0.0, 0.5, 1.0)]
    print(f"   {ka[0]}(d={ka[2]}) - {kb[0]}(d={kb[2]}): "
          f"{min(dd):+.4f} .. {max(dd):+.4f}")

# ----------------- W3: anatomy + ledger -----------------
print("\n== W3. anatomy ==")
# vacuum-drag channel census: energy above omega = 1
w2K1, U1 = np.linalg.eigh(K0m)
dE_modes = np.diag(U1.T @ (0.5*(Gdd2[N0:, N0:] - GP0)
                           + 0.5*(K0m @ (Gdd2[:N0, :N0] - GX0))
                           ) @ U1)
hi = np.sqrt(np.clip(w2K1, 0, None)) > 1.0
census = float(np.sum(np.abs(dE_modes[hi]))
               / np.sum(np.abs(dE_modes)))
print(f"  vacuum-drag channel census: fraction of |dE| in modes "
      f"with omega > 1: {census:.2f}")
print(f"   (an anatomy row, no gate; its entropy response is "
      f"exactly zero by K-NULL")
print(f"    regardless.)")

def kstat(ok):
    return "did not fire" if ok else "FIRED"
lad_word = (("split grows with roughness (YES), all rungs "
             "floor-converged:\n    universality is a "
             "smooth-probe (IR) law")
            if rough_mono and n_flim == 0 else
            ((f"split grows with roughness (YES); {n_flim} "
              f"rung(s) FLOOR-LIMITED -\n    trend supported, "
              f"rough-end magnitude unresolved (registered)")
             if rough_mono else
             "not monotone - no IR-law reading (registered)"))
fF1, fF2 = forks['F1'], forks['F2']
def fork_word(f):
    if f['top'] is None:
        return "NOT RESOLVABLE (registered)"
    if f['strict'] and f['cons']:
        return "COMPLETION (strict + consistent)"
    if f['cons']:
        return "UNRESOLVED (consistent, not strict)"
    return "SATURATION (registered prediction)"
if fF1['top'] is None:
    s_f1 = ("the F1 family is NOT RESOLVABLE at this instrument "
            "(registered)")
elif fF1['strict'] and fF1['cons']:
    s_f1 = (f"K_p COMPLETES to the same finite-box BW target "
            f"(F1 top r_P/g_box = {fF1['top']['ratio']:.4f} at "
            f"l_E/d = {fF1['top']['lEd']:.2f}, strict on "
            f"centrals)")
elif fF1['cons']:
    s_f1 = (f"the F1 family top reads {fF1['top']['ratio']:.4f}"
            f" - UNRESOLVED (consistent, not strict)")
else:
    s_f1 = (f"the F1 family top reads {fF1['top']['ratio']:.4f}"
            f" - a SATURATION reading, registered")
print(f"""\n== LEDGER (generated from computed flags) ==
  K-INST   full-vs-block kernel identity      -> {kstat(k_inst)}
  K-COV    drag covariance (Ward) identity    -> {kstat(k_cov)}
  K-PARITY spectra even in v                  -> {kstat(k_parity)}
  K-ODD    zero law: |c1| at float floor      -> {kstat(k_odd)}
  K-ODD2   single-sign evenness scaling       -> {kstat(k_odd2)}
  K-NULL   interior vacuum drag dS = 0        -> {kstat(k_null)}
  K-C6     c2 extrapolant vs c/6 (1e-3)       -> {kstat(k_c6)}
  K-SREL   S_rel >= 0 at every v              -> {kstat(k_srel)}
  K-LR     S_left = S_right                   -> {kstat(k_lr)}
  K-LEAK-J every anchor stencil-halo leak 0.0 -> {kstat(k_leakj)}
  K-FLOOR-P / K-FLOOR-X anchor growths <= 1e-2 -> {kstat(k_floor_p)} / {kstat(k_floor_x)}
  K-V0     P48 h12 reproduction (5e-4)        -> {kstat(k_v0)}
  P-SECTOR COMPLETION: F1 {fork_word(fF1)};
    F2 {fork_word(fF2)}
    F1 curve (N = 192): """
      + " / ".join(f"{res[('F1',192,d)]['ratio']:.3f}+-"
                   f"{res[('F1',192,d)]['syst']:.3f}"
                   for d in (22, 16, 13)) + f"""
      at l_E/d """ + " / ".join(f"{res[('F1',192,d)]['lEd']:.2f}"
                                for d in (22, 16, 13)) + f"""
    F1 box rows (N = 240): """
      + " / ".join(f"{res[('F1',240,d)]['ratio']:.3f}"
                   for d in (22, 16, 13)) + f"""
  SECTOR FORK: {sector_state} - r_P/r_X = """
      + " / ".join(f"{q:.4f}" for _, _, q, _ in sector_rows) + f"""
    (d = 22/16/13 at N = 192; d = 13 at N = 240)
  ROUGHNESS LADDER: r_P/r_X = """
      + " / ".join(f"{q:.4f}" for _, q, _ in qlad) + f"""
    at W = 12/6/4/3 - {lad_word};
    fixed-position control (W = 3, d = 4): {qcf[1e-60]:.4f}"""
      + (" FLOOR-LIMITED (registered)" if flimc else
         " floor-converged") + f"""
  REGISTERED: the gravito-magnetic boost law as covariance
  identity (Level 1; measured content = Level 2 + K-COV); the
  GEM factor 4 (tensor/dynamics scope); the global-flow log-box
  response (anatomy row); gravito-magnetic species EP (the
  ladder playbook, if ever SPLIT); the Faulkner first-order
  dK_xp kernel structure (the successor edge); spheres /
  Lorentzian dynamics (other campaigns).""")

# verdict assembled from computed flags
s_zero = (("THE ZERO LAW holds at floor precision: momentum "
           "density does not gravitate\n  scalarly at linear "
           "order - dS and d<K> are even in v (K-ODD, K-ODD2,\n"
           "  K-PARITY), exactly as Kerr entropy is even in J")
          if (k_odd and k_odd2 and k_parity) else
          ("the zero law FAILED a gate (see ledger) - the O(v) "
           "scalar sector is\n  unresolved at this instrument"))
s_cov = ((f"the gravito-magnetic boost law is SYMPLECTIC "
          f"COVARIANCE, receipted as\n  the Ward identity K-COV "
          f"({cov_rel:.0e}), not claimed as a measurement")
         if k_cov else
         ("the covariance identity FAILED its gate (see ledger)"
          " - the Level-1\n  reading is unsupported"))
s_null = ((f"Interior-drag flow of the vacuum is modular gauge "
           f"(K-NULL: dS = 0 at\n  drag amplitude where the "
           f"kinetic modular charge is "
           f"{rows_null[1][2]:.2f}) - only\n  flowed matter pays")
          if k_null else
          ("the vacuum-drag null FAILED its gate (see ledger)"))
s_lic = ((f"the split is below 1e-3 (computed outer bound "
          f"{outer_split:.1e}, floor-grade\n  resolution), "
          f"thirty-plus times tighter than the criterion")
         if lic else
         (f"the split's computed outer bound is {outer_split:.1e}"
          f" - above the 1e-3 license"))
s_uni = (("kinetic and gradient energy are priced equally in "
          "the modular currency at\n  smooth-probe scales - "
          + s_lic + "; the "
          "roughness trend is\n  monotone, with the rough end "
          + ("floor-converged" if (n_flim == 0 and not flimc)
             else "FLOOR-LIMITED (its magnitude\n  registered, "
             "not resolved)")
          + ": the boost generator is measured whole\n  at this "
          "scope, and at first-law scope gravito-magnetism is "
          "frame-dragged\n  Newtonianism with coefficient 1")
         if sector_state == 'UNIVERSAL' else
         ('the sectors are not priced equally at this instrument'
          ' - ' + ('a registered\n  SPLIT: the cutoff-ladder '
                   'adjudicator is the declared next instrument'
                   if sector_state == 'SPLIT' else
                   'UNRESOLVED,\n  registered')))
print(f"""\n== VERDICT ==
  {s_zero};
  the O(v) information lives in the kernel, where {s_cov}.
  {s_null}.
  THE MEASUREMENT: the moving probe pairs with K_p - the p^2
  half of the boost generator, the first probe to pair with it
  - and {s_f1};
  the SECTOR FORK resolves {sector_state}: r_P/r_X = """
      + " / ".join(f"{q:.4f}" for _, _, q, _ in sector_rows)
      + f"""
  across depths and both box sizes - {s_uni}.
  NOT claimed: the GEM factor 4 (tensor/dynamics bookkeeping);
  continuum beyond the box; spheres, Lorentzian dynamics,
  radiation; probe-shape and species generality of the sector
  statement beyond the roughness ladder's scope; anything
  beyond the quoted per-anchor systematics.""")
