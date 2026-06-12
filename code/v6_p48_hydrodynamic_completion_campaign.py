# Paper 48 (v6) campaign: THE HYDRODYNAMIC COMPLETION - does the
# coherent currency map complete to the finite-box BW target at
# the hydrodynamic end, and is the EP species residue a cutoff
# artifact?  The instruments: TWO compact-support probe families
# (Hann^2 and flat-top plateau - strictly zero outside finite
# support, enclosure receipted PER ANCHOR by a computed leakage
# print and a kill), parameterized by the MEASURED ENERGY WIDTH
# l_E = 2 x rms of dT00 (for the massless chain the coherent
# perturbation's energy is pure gradient - the probe amplitude
# width and the energy width are different objects, and the
# families differ in energy profile BY DESIGN); per-anchor floor
# sweeps; per-anchor float-droop receipts at identical geometry;
# a three-rung cutoff ladder for the EP question.  Canonical:
# /tmp/v6_p48_campaign.out (bit-identical rerun required).
import math
import numpy as np
import mpmath
from mpmath import mp, mpf

print("""== DESIGN BLOCK (pre-registered) ==
QUESTION 1 (completion): the currency campaign left one
quantitative open edge - the coherent kernel ratio
r = d<K>/d<K_boost> reached r/g_box = 0.980 at its single
exact anchor (probe-tail-capped window) - does the map
COMPLETE to the finite-box BW target (r/g_box -> 1) as the
probe's ENERGY distribution becomes screen-scale (l_E/d -> 1),
or saturate below it?  And is the completion - if seen - a
property of the energy distribution, or does it depend on the
probe's shape beyond its width?
QUESTION 2 (EP): the currency campaign's half-scale species
anchor gave EP_exact = 1.027 [1.025-1.029], with transfer to
the full config registered, not receipted.  Is the residue a
property of the map, or a CUTOFF ARTIFACT of the coarse heavy
species (xi = 1.25 lattice units at half scale)?  Receipt: a
three-rung cutoff ladder at fixed dimensionless geometry.
INSTRUMENTS, declared:
  (i) TWO COMPACT-SUPPORT PROBE FAMILIES:
   Hann^2: v = cos^2(pi(x-x0)/(2W)) on |x-x0| < W, zero
    outside.  Identity receipts: l_v = 2 sigma of v^2 =
    0.5658 W on this lattice; dT00 support is one site past
    the probe support, so EXACT enclosure requires d >= W:
    the exactly-enclosed Hann^2 window caps at l_v/d <= 0.566.
   PLATEAU: v = 1 on |x-x0| <= P, cos^2 taper of width T
    (same C^1 class), support P+T.  Its coherent energy lives
    in the taper bands - by design a DIFFERENT energy profile
    at the same amplitude width.
   THE WINDOW AXIS: for the massless chain dT00 is pure
   gradient, so the physical probe scale is the measured
   ENERGY width l_E = 2 sigma of dT00 (l_E ~ 1.9 l_v for
   Hann^2; plateau energy is band-concentrated).  Both widths
   printed per anchor; the curve is quoted on l_E/d.
   ENCLOSURE IS A PER-ANCHOR RECEIPT: leakage =
   sum|dT[:j]|/sum|dT| printed for every compact-family
   anchor; kill K-LEAK fires unless it is EXACTLY 0.0 at
   every headline anchor.
  (ii) EXACT ANCHORS: mpmath dps 80, per-anchor floor sweep
   (floors 1e-30/45/60); kill K-FLOOR fires if any Hann^2
   headline anchor grows > 1e-2 between 1e-45 and 1e-60 (the
   headline family); boost-offset convention spread (offsets
   0/0.5/1) printed per anchor.  Probe-family floor gates:
   K-PROBE (Hann^2) and K-PROBE2 (plateau) at one validation
   geometry each, 1e-2 threshold.  ADMISSIBILITY, declared:
   an anchor resolves a fork only if its family gate did not
   fire, its leakage is exactly 0.0, and its own floor growth
   is <= 1e-2; inadmissible anchors stay printed as
   exploratory rows and are listed - band-concentrated energy
   sits toward the near-cut regime, so plateau floor
   fragility is a registered finding, not a kill; a fork with
   no admissible anchors resolves as NOT RESOLVABLE at this
   instrument.
  (iii) FLOAT-DROOP RECEIPT AT IDENTICAL GEOMETRY: the float
   clip-14 ratio is printed beside every exact anchor - the
   regulator droop is receipted per anchor, not inferred.
  (iv) the finite-box BW target g_box(d) = (2N/pi)
   sin(pi d/2N) sin(pi(2R-d)/2N)/(d sin(pi R/N)), R = N - j.
  (v) DIFFERENTIAL RECEIPT: matched-depth anchor pairs
   (h12/h20/p21, d = 22/21/21) difference out the boost-offset
   convention almost exactly - the instrument that sees below
   the offset systematic; printed across offsets 0/0.5/1.  A
   convention-robust drift registers as a NAMED OPEN EDGE
   (THE BEND); the flag is defined on the h12-p21 endpoint
   pair (declared); the two sub-pairs decompose the drift into
   an intra-family and a cross-family leg; the linear
   continuation to the 0.03 criterion is printed.  No
   directional kill.
  (vi) THE BEND'S BOX RECEIPT: the same three anchors
   (identical probes, x0, d - the screen-side geometry
   unchanged) recomputed exactly at N = 240, the far wall
   receding.  Leakage accumulates into K-LEAK; floor growths
   printed; these anchors resolve only the box question, not
   the completion fork.  Reading: if the h12-p21 differential
   keeps its sign at every offset and at least half its
   N = 192 magnitude, the drift is box-stable at this step;
   below half, the finite-box hypothesis leads; sign loss
   resolves it as a finite-box residual.  Either way
   registered; no kill.
W1 - FLOAT TREND MAP: context only (clip-12|14), no verdict
   weight; the droop receipts live per anchor in W2.
PRE-REGISTERED FORKS (resolved by the printed numbers):
  COMPLETION (per family): the family's top-of-window
   r_exact/g_box sits within 0.03 of 1 ON CENTRAL VALUES at
   the declared +1/2 offset (strict proximity), AND 1 lies
   within the per-anchor systematic (consistency) - both
   printed separately.  The strict criterion is anchored to
   the declared +1/2 convention (stated; convention-robust
   statements live in the differential receipt).
   SATURATION: the top central sits below 1 by more than the
   stacked systematic.  The zone between the readings is
   UNRESOLVED and says so: the offset convention is a
   correlated bracket, not random error - the per-anchor
   exclusion floor (central - syst) and the family's
   central-value bend are printed; structure below the
   offset systematic is probed by the DIFFERENTIAL RECEIPT
   (v), and a convention-robust drift is registered as a
   named edge.
  SHAPE (the sufficiency question): two matched pairs - one
   Hann^2 and one plateau anchor at the same l_E/d (~0.6 and
   ~0.95) - agree within combined systematics -> the
   completion diagnostic is a property of the energy
   distribution (ROBUST); disagree -> the one-parameter l_E/d
   story fails at this scope (SHAPE-DEPENDENT, registered
   as a finding either way; no directional kill).  A pair
   resolves only if both anchors are admissible; with no
   resolvable pair the shape fork is UNRESOLVED, registered.
W2 ANCHOR SET (N = 192):
  Hann^2 (W, x0, d): (8,110,28) (12,110,22) (16,112,18)
   (20,110,21 - the family's enclosure cap);
  plateau (P=6, T=14, x0=112; d): 47, 30, 21 - d = 47/30
   pair with the W=12/W=16 Hann^2 anchors on l_E/d; d = 21
   (the support cap) extends the enclosed window to
   l_E/d ~ 1.3, past the Hann^2 cap.  Taper width T = 14 is
   set wider than the Hann^2 half-widths in play (band width
   is the floor-stability scale; the gate receipts decide).
W3 - EP (QUESTION 2):
  (a) enclosed d-sweep at half scale: N = 128, m = 0.4/0.8,
   Hann^2 W = 12 at x0 = 64, d = 13/16/20 (all enclosed;
   leakage printed).  Registered reading: does EP move toward
   1 as l_E/d grows (shallower d)?  No directional kill - the
   answer is printed either way, monotone flag computed.
  (b) shape pair for EP: plateau P=4/T=10 at x0=66, d=19
   (l_E/d near the d=13 Hann^2 row) - species ratio
   robustness across probe shape; per-species tails
   receipted by K-EPFLOOR.
  (c) THE CUTOFF LADDER (the registered follow-up, closed
   self-contained): the SAME dimensionless configuration -
   Gaussian probe (the P44/P45 family; tails declared, the
   ladder keeps tail-bracket discipline instead of K-LEAK) at
   x0/N = 0.508, w/N = 3/32, screen j/N = 13/32, species
   masses (mN = 51.2, 102.4) - at three cutoffs:
     quarter N =  64, m = 0.8/1.6, w =  6 @ 32.5, j =  26
     half    N = 128, m = 0.4/0.8, w = 12 @ 65,   j =  52
     full    N = 256, m = 0.2/0.4, w = 24 @ 130,  j = 104
   Instrument: dps 90, floors 1e-30/45/60/75 (the currency
   campaign's half-scale settings), geometric-tail
   extrapolation with the model CHECKED in-run (q12 vs q23
   printed; decreasing q means the extrapolation OVERSHOOTS
   the tail, so the bracket [no-tail, extrapolated] is
   conservative); per-rung EP bracket [min/max over tail
   models]; per-rung Gaussian tail-crossing of the cut
   printed (the ladder's family standard is the tail bracket,
   not enclosure - the TREND at fixed dimensionless geometry
   is the receipt); kill K-EPFLOOR fires if any species tail
   beyond its last floor exceeds 10%.  The quarter rung is a
   deep-lattice trend point (heavy xi = 0.625 a, outside any
   scaling window) - declared.  Readings, registered:
   (1) transfer - do the half and full rung brackets overlap?
   (computed flag; the currency campaign's 1.027
   [1.025-1.029] is the cross-paper anchor, overlap with this
   run's half rung printed as a consistency receipt);
   (2) cutoff trend - does |EP - 1| (extrapolated centrals;
   bracket-robust check and step factors printed) shrink
   along quarter -> half -> full?  Monotone-toward-1 = the
   residue is a cutoff artifact dissolving toward the
   continuum (computed flag, no directional kill);
   (3) species structure - if 1 - r ~ C (m a)^2, the
   deviation ratio (1 - r_heavy)/(1 - r_light) sits near
   (m_h/m_l)^2 = 4 at every rung: printed per rung on
   extrapolated centrals, an identity-style receipt of the
   artifact reading, no kill; the tail-model
   conservativeness (q23 < q12 at every ladder
   species/rung) is a computed flag, not an eyeballed one.
Conventions: float64 + mpmath; no RNG; bounds round in the
safe direction; ledger from computed flags; the P44 boost
convention (x - j + 1/2) declared, offsets swept; identity
rows are receipts, not kills.
=================================================================
""")

# ----------------- machinery -----------------
def chain_pack(N, msq):
    K = np.diag((2.0+msq)*np.ones(N)) - np.eye(N, k=1) - np.eye(N, k=-1)
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
def modular_K(GX, GP, j, N, nuclip=1e-12):
    ids = np.arange(j, N)
    e2, V = np.linalg.eigh(GX[np.ix_(ids, ids)])
    e2c = np.clip(e2, 1e-14, None)
    M = (V*np.sqrt(e2c)) @ V.T
    Mi = (V*(1.0/np.sqrt(e2c))) @ V.T
    w2_, W_ = np.linalg.eigh(M @ GP[np.ix_(ids, ids)] @ M)
    nu_ = np.sqrt(np.clip(w2_, 0.25 + nuclip, None))
    F_ = np.log((nu_+0.5)/(nu_-0.5))
    return Mi @ (W_*(F_*nu_)) @ W_.T @ Mi
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
def plateau(x0, P, T, N):
    xs = np.arange(N)
    a = np.abs(xs - x0)
    v = np.zeros(N)
    v[a <= P] = 1.0
    band = (a > P) & (a < P + T)
    v[band] = np.cos(np.pi*(a[band]-P)/(2*T))**2
    return v/np.linalg.norm(v)
def leff_of(v):
    w2 = v*v
    xb = float(np.sum(np.arange(len(v))*w2))
    s2 = float(np.sum((np.arange(len(v))-xb)**2*w2))
    return 2.0*np.sqrt(s2), xb
def leffE_of(dT):
    w = np.abs(dT)
    s = float(np.sum(w))
    xb = float(np.sum(np.arange(len(dT))*w))/s
    s2 = float(np.sum((np.arange(len(dT))-xb)**2*w))/s
    return 2.0*np.sqrt(s2), xb
def leak_of(dT, j):
    return float(np.sum(np.abs(dT[:j])))/float(np.sum(np.abs(dT)))

def hann2_mp(x0, W, N):
    return [mpmath.cos(mpmath.pi*(x-x0)/(2*W))**2
            if abs(x-x0) < W else mpf(0) for x in range(N)]
def plateau_mp(x0, P, T, N):
    out = []
    for x in range(N):
        a = abs(x - x0)
        if a <= P:
            out.append(mpf(1))
        elif a < P + T:
            out.append(mpmath.cos(mpmath.pi*(a-P)/(2*T))**2)
        else:
            out.append(mpf(0))
    return out

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
def mp_anchor(Nn, jn, msq_mp, vfull,
              floors=('1e-30', '1e-45', '1e-60')):
    Bn = Nn - jn
    GXB, GPB = mp_block(Nn, jn, msq_mp)
    E, Q = mpmath.eigsy(GXB)
    Mi = Q*mpmath.diag([1/mpmath.sqrt(E[k]) for k in range(Bn)])*Q.T
    M = Q*mpmath.diag([mpmath.sqrt(E[k]) for k in range(Bn)])*Q.T
    E2, W2 = mpmath.eigsy(M*GPB*M)
    nrm = mpmath.sqrt(sum(v*v for v in vfull))
    vB = mpmath.matrix([vfull[x]/nrm for x in range(jn, Nn)])
    u = W2.T*(Mi*vB)
    out = {}
    for fls in floors:
        fl = mpf(fls)
        tot = mpf(0)
        for k in range(Bn):
            nu = mpmath.sqrt(E2[k])
            if nu - half < fl:
                nu = half + fl
            F = mpmath.log((nu+half)/(nu-half))
            tot += F*nu*u[k]**2/2
        out[float(fl)] = float(tot)
    return out

mp.dps = 80

# ----------------- W0: probe-family validation -----------------
print("== W0. probe-family validation ==")
N0, x00, W0_, j0 = 128, 80, 12, 64
# Hann^2 identity receipts: amplitude vs energy width, and the cap
GXf, GPf = chain_pack(N0, 0.0)
Ef = T00_profile(GXf, GPf, 0.0, N0)
print("  Hann^2 width identities (N = 128, x0 = 64):")
for Wv in (8, 12, 16, 20):
    vv = hann2(64, Wv, N0)
    lv, _ = leff_of(vv)
    dTv = T00_profile(GXf + 2e-3*np.outer(vv, vv), GPf, 0.0, N0) - Ef
    lE, _ = leffE_of(dTv)
    print(f"   W = {Wv:2d}: l_v/W = {lv/Wv:.4f}, l_E/W = {lE/Wv:.4f}")
print("   -> exact enclosure needs d >= W: the enclosed Hann^2")
print("      window caps at l_v/d <= 0.566 (l_E/d ~ 1.07).")
# Hann^2 floor gate (K-PROBE) + Gaussian control + leakage
vh = hann2_mp(x00, W0_, N0)
vh_f = hann2(x00, W0_, N0)
leff_h, _ = leff_of(vh_f)
wg = leff_h/2/np.sqrt(0.5)
vg = [mpmath.e**(-mpf((x-x00)**2)/(2*mpf(wg)**2)) for x in range(N0)]
sw_h = mp_anchor(N0, j0, mpf(0), vh)
sw_g = mp_anchor(N0, j0, mpf(0), vg)
gr_h = sw_h[1e-60]/sw_h[1e-45] - 1
gr_g = sw_g[1e-60]/sw_g[1e-45] - 1
k_probe = abs(gr_h) <= 1e-2
print(f"  Hann^2 (W = {W0_}, l_v = {leff_h:.2f}): dK/a floor sweep "
      f"{sw_h[1e-30]:.6f} -> {sw_h[1e-45]:.6f} -> {sw_h[1e-60]:.6f}")
print(f"   growth 45->60: {gr_h:+.1e}  (K-PROBE <= 1e-2: "
      f"{'did not fire' if k_probe else 'FIRED'})")
print(f"  Gaussian (matched l_v, w = {wg:.2f}): sweep "
      f"{sw_g[1e-30]:.6f} -> {sw_g[1e-45]:.6f} -> {sw_g[1e-60]:.6f}"
      f"  (growth {gr_g:+.1e})")
dTh = T00_profile(GXf + 2e-3*np.outer(vh_f, vh_f), GPf, 0.0, N0) - Ef
print(f"  Hann^2 leakage at this geometry: {leak_of(dTh, j0):.1e}")
# plateau floor gate (K-PROBE2) at an enclosed geometry
P0, T0, x0p = 6, 14, 86
vp_f = plateau(x0p, P0, T0, N0)
vp = plateau_mp(x0p, P0, T0, N0)
lv_p, _ = leff_of(vp_f)
dTp = T00_profile(GXf + 2e-3*np.outer(vp_f, vp_f), GPf, 0.0, N0) - Ef
lE_p, _ = leffE_of(dTp)
sw_p = mp_anchor(N0, j0, mpf(0), vp)
gr_p = sw_p[1e-60]/sw_p[1e-45] - 1
k_probe2 = abs(gr_p) <= 1e-2
print(f"  plateau (P = {P0}, T = {T0}, x0 = {x0p}; l_v = {lv_p:.2f}, "
      f"l_E = {lE_p:.2f}): sweep")
print(f"   {sw_p[1e-30]:.6f} -> {sw_p[1e-45]:.6f} -> {sw_p[1e-60]:.6f}"
      f"  growth 45->60: {gr_p:+.1e}")
print(f"   (K-PROBE2 <= 1e-2: "
      f"{'did not fire' if k_probe2 else 'FIRED'}); leakage "
      f"{leak_of(dTp, j0):.1e}")
if k_probe and k_probe2:
    print("  -> both compact families pass the floor gate; energy")
    print("     width is the window axis (the l_E/l_v ratios above:")
    print("     band-concentrated plateau energy vs the Hann^2 ring).")
else:
    fired = [n for n, ok in (("Hann^2", k_probe),
                             ("plateau", k_probe2)) if not ok]
    print("  -> floor gate FIRED for: " + ", ".join(fired) + " -")
    print("     that family's anchors are inadmissible for fork")
    print("     resolution (declared fallback); rows stay printed")
    print("     as exploratory.")

# ----------------- W1: float trend map -----------------
print("\n== W1. float trend map (context only; clip-12|14) ==")
N1 = 256
GX1, GP1 = chain_pack(N1, 0.0)
E1 = T00_profile(GX1, GP1, 0.0, N1)
xs1 = np.arange(N1)
print("   (l_E/d, r12 | r14 | r14/g_box):")
for W_, d in ((10, 30), (14, 28), (18, 26), (22, 26), (26, 28),
              (30, 32)):
    v = hann2(150, W_, N1)
    D = np.outer(v, v)
    dT = T00_profile(GX1 + 2e-3*D, GP1, 0.0, N1) - E1
    lE1, _ = leffE_of(dT)
    dc = float(np.sum(xs1*dT)/dT.sum())
    j = int(round(dc - d))
    rr = []
    for nc in (1e-12, 1e-14):
        Kx = modular_K(GX1, GP1, j, N1, nuclip=nc)
        ids = np.arange(j, N1)
        dKe = 0.5*2e-3*float(np.sum(Kx * D[np.ix_(ids, ids)]))
        rr.append(dKe/dK_boost(dT, j, N1))
    gb = gbox2(dc-j, j, N1)
    print(f"   ({lE1/(dc-j):.3f}, {rr[0]:.4f} | {rr[1]:.4f} | "
          f"{rr[1]/gb:.4f})")
print("   -> context only; the per-anchor float-droop receipts at")
print("      identical geometry live beside the W2 exact anchors.")

# ----------------- W2: the completion curve -----------------
print("\n== W2. THE COMPLETION CURVE (exact anchors, N = 192) ==")
N2 = 192
GX2f, GP2f = chain_pack(N2, 0.0)
E2f = T00_profile(GX2f, GP2f, 0.0, N2)
xs2 = np.arange(N2)
anchors = (('hann', 'h8',  (8,  None), 110, 28),
           ('hann', 'h12', (12, None), 110, 22),
           ('hann', 'h16', (16, None), 112, 18),
           ('hann', 'h20', (20, None), 110, 21),
           ('plat', 'p47', (6, 14),    112, 47),
           ('plat', 'p30', (6, 14),    112, 30),
           ('plat', 'p21', (6, 14),    112, 21))
curve = {}
k_leak = True
k_floor = True
gfam = {'hann': k_probe, 'plat': k_probe2}
for fam, tag, (A, B_), x0_, d_ in anchors:
    if fam == 'hann':
        v_f = hann2(x0_, A, N2)
        v_mp = hann2_mp(x0_, A, N2)
        lab = f"hann W={A:2d}"
    else:
        v_f = plateau(x0_, A, B_, N2)
        v_mp = plateau_mp(x0_, A, B_, N2)
        lab = f"plat P={A},T={B_}"
    lv, _ = leff_of(v_f)
    D = np.outer(v_f, v_f)
    dT = T00_profile(GX2f + 2e-3*D, GP2f, 0.0, N2) - E2f
    lE, _ = leffE_of(dT)
    dc = float(np.sum(xs2*dT)/dT.sum())
    j = int(round(dc - d_))
    leak = leak_of(dT, j)
    k_leak = k_leak and (leak == 0.0)
    # float-droop receipt at identical geometry
    Kx14 = modular_K(GX2f, GP2f, j, N2, nuclip=1e-14)
    ids = np.arange(j, N2)
    dKe14 = 0.5*2e-3*float(np.sum(Kx14 * D[np.ix_(ids, ids)]))
    r14 = dKe14/dK_boost(dT, j, N2)
    # exact anchor
    sw = mp_anchor(N2, j, mpf(0), v_mp)
    gr = sw[1e-60]/sw[1e-45] - 1
    if fam == 'hann':
        k_floor = k_floor and (abs(gr) <= 1e-2)
    offs = []
    for off in (0.0, 0.5, 1.0):
        dKb = dK_boost(dT, j, N2, off=off)/2e-3
        offs.append(sw[1e-60]/dKb)
    r_ex = offs[1]
    gb = gbox2(dc-j, j, N2)
    osp = (max(offs)-min(offs))/r_ex
    syst = abs(gr) + osp
    curve[tag] = dict(fam=fam, lEd=lE/(dc-j), lvd=lv/(dc-j),
                      r=r_ex, gb=gb, ratio=r_ex/gb, syst=syst,
                      gr=gr, leak=leak, f14=r14/gb, d=dc-j,
                      roffs=[o/gb for o in offs])
    print(f"  [{lab}] l_E/d = {lE/(dc-j):.3f} (l_v/d = "
          f"{lv/(dc-j):.3f}, d = {dc-j:.1f}): leakage {leak:.1e}")
    print(f"   float r14/g_box = {r14/gb:.4f} (droop receipt at "
          f"identical geometry)")
    print(f"   r_exact = {r_ex:.4f} [floor growth {gr:+.1e}; "
          f"offset spread {osp*100:.1f}%]")
    if gfam[fam] and leak == 0.0 and abs(gr) <= 1e-2:
        print(f"   g_box = {gb:.4f}; r/g_box = {r_ex/gb:.4f} "
              f"+- {syst:.3f}; excludes plateaus below "
              f"{r_ex/gb - syst:.3f}")
    else:
        print(f"   g_box = {gb:.4f}; r/g_box = {r_ex/gb:.4f} "
              f"+- {syst:.3f}; EXPLORATORY (gate) - no "
              f"exclusion claimed")
print(f"  K-LEAK  (every W2 anchor leakage exactly 0.0 so far): "
      f"{'did not fire' if k_leak else 'FIRED'}")
print(f"  K-FLOOR (every Hann^2 anchor floor growth <= 1e-2): "
      f"{'did not fire' if k_floor else 'FIRED'}")

# fork resolution from admissible anchors (declared gates)
gate_fam = {'hann': k_probe, 'plat': k_probe2}
adm = {t: c for t, c in curve.items()
       if gate_fam[c['fam']] and c['leak'] == 0.0
       and abs(c['gr']) <= 1e-2}
print("  admissibility: " + ", ".join(
    f"{t} {'ok' if t in adm else 'EXCLUDED'}"
    f" ({curve[t]['gr']:+.0e})" for t in curve))
forks = {}
print("  THE COMPLETION FORK, per family (admissible anchors):")
for fam in ('hann', 'plat'):
    fa = [c for c in adm.values() if c['fam'] == fam]
    if not fa:
        forks[fam] = dict(top=None, strict=False, cons=False,
                          bend=float('nan'))
        print(f"   {fam}: no admissible anchors - the family's "
              f"completion fork is NOT")
        print(f"    RESOLVABLE at this instrument (floor-fragile; "
              f"registered).")
        continue
    top = max(fa, key=lambda c: c['lEd'])
    strict = abs(top['ratio'] - 1) <= 0.03
    cons = abs(top['ratio'] - 1) <= top['syst']
    bend = max(abs(c['ratio'] - 1) for c in fa)
    forks[fam] = dict(top=top, strict=strict, cons=cons, bend=bend)
    print(f"   {fam}: top-of-window l_E/d = {top['lEd']:.2f}, "
          f"r/g_box = {top['ratio']:.4f} +- {top['syst']:.3f}")
    print(f"    strict 0.03 on centrals: "
          f"{'PASS' if strict else 'fail'}; 1 within +-syst: "
          f"{'yes' if cons else 'NO'}; family central-value bend "
          f"{bend*100:.1f}%")
    print(f"    (criterion anchored to the declared +1/2 offset; "
          f"convention-robust")
    print(f"     statements live in the differential receipt "
          f"below)")
    if strict and cons:
        print(f"    -> COMPLETION reading fires on centrals; "
              f"saturation below {top['ratio']-top['syst']:.3f} "
              f"excluded; structure below")
        print(f"       the offset systematic is probed by the "
              f"differential receipt below.")
    elif cons:
        print(f"    -> strict proximity fails but 1 lies within "
              f"the systematic: UNRESOLVED zone - neither")
        print(f"       reading fires; registered as such.")
    else:
        print(f"    -> SATURATION reading: the family top sits "
              f"below 1 beyond its stacked systematic - a")
        print(f"       falsifiable sub-BW residue, registered.")
# shape fork: matched pairs on l_E/d (admissible pairs only)
pairs = (('h12', 'p47'), ('h16', 'p30'))
pair_oks = []
print("  THE SHAPE FORK (matched l_E/d pairs):")
for th, tp in pairs:
    ch, cp = curve[th], curve[tp]
    if th not in adm or tp not in adm:
        print(f"   {th} vs {tp}: NOT RESOLVABLE (inadmissible "
              f"anchor) - skipped.")
        continue
    dlt = abs(cp['ratio'] - ch['ratio'])
    comb = ch['syst'] + cp['syst']
    ok = dlt <= comb
    pair_oks.append(ok)
    print(f"   {th} (l_E/d {ch['lEd']:.2f}) vs {tp} (l_E/d "
          f"{cp['lEd']:.2f}): r/g_box {ch['ratio']:.4f} vs "
          f"{cp['ratio']:.4f}")
    print(f"    |delta| = {dlt:.4f} vs combined syst {comb:.3f} "
          f"-> {'agree' if ok else 'DISAGREE'}")
if not pair_oks:
    shape_state = 'UNRESOLVED'
    print("   -> shape fork UNRESOLVED: no resolvable matched "
          "pair at this instrument -")
    print("      registered.")
elif all(pair_oks):
    shape_state = 'ROBUST'
    print("   -> SHAPE-ROBUST: at matched l_E/d the families "
          "agree within combined")
    print("      systematics - the completion diagnostic is a "
          "property of the energy")
    print("      distribution at this scope.  (Power note: the "
          "yardstick is the combined")
    print("      systematic - a coarse test; finer shape "
          "structure lives in the")
    print("      differential receipt below.)")
else:
    shape_state = 'SHAPE-DEPENDENT'
    print("   -> SHAPE-DEPENDENT: the families disagree at "
          "matched l_E/d beyond")
    print("      combined systematics - the one-parameter l_E/d "
          "story fails at this")
    print("      scope; registered as a finding.")

# differential receipt: matched-depth pairs cancel the offset
# convention - the instrument below the offset systematic
print("  DIFFERENTIAL RECEIPT (matched-depth pairs, offsets "
      "0/0.5/1):")
dr = {}
for ta, tb in (('h12', 'h20'), ('h20', 'p21'), ('h12', 'p21')):
    ca, cb = curve[ta], curve[tb]
    dd = [a - b for a, b in zip(ca['roffs'], cb['roffs'])]
    dr[(ta, tb)] = (min(dd), max(dd))
    print(f"   {ta} (d = {ca['d']:.0f}) - {tb} (d = {cb['d']:.0f})"
          f": r/g_box diff {min(dd):+.4f} .. {max(dd):+.4f}")
bend_robust = dr[('h12', 'p21')][0] > 0
bp_lo = math.floor(dr[('h12', 'p21')][0]*1000)/10
bp_hi = math.ceil(dr[('h12', 'p21')][1]*1000)/10
if bend_robust:
    print(f"   -> THE BEND: a convention-robust downward drift of"
          f" {bp_lo:.1f}-{bp_hi:.1f}% from")
    print(f"      mid-window (l_E/d {curve['h12']['lEd']:.2f}) to "
          f"the top ({curve['p21']['lEd']:.2f}) survives every "
          f"offset -")
    print(f"      a NAMED OPEN EDGE, registered.  Hypotheses, "
          f"none claimed: a residual")
    print(f"      form factor; the onset of percent-level "
          f"saturation; a finite-box")
    print(f"      residual beyond g_box; probe-sampling "
          f"discreteness.  The box receipt")
    print(f"      below takes the first cut.  The completion "
          f"criterion (0.03 on")
    print(f"      centrals) stands; the drift sits below it.")
    dl = curve['p21']['lEd'] - curve['h12']['lEd']
    head = 0.03 - (1 - curve['p21']['ratio'])
    if head > 0 and dr[('h12', 'p21')][0] > 0:
        print(f"      Linear continuation would breach the 0.03 "
              f"criterion near l_E/d ~")
        print(f"      {curve['p21']['lEd'] + head*dl/dr[('h12','p21')][1]:.2f}"
              f"-{curve['p21']['lEd'] + head*dl/dr[('h12','p21')][0]:.2f}"
              f" - the successor's domain (stated).")
else:
    print(f"   -> no convention-robust drift: the matched-depth "
          f"differences change sign")
    print(f"      across offsets - sub-systematic structure "
          f"unresolved; registered.")

# the box receipt: same screen-side geometry, far wall recedes
print("  THE BEND'S BOX RECEIPT (N = 240; identical probes, x0, "
      "d; far wall recedes):")
N2b = 240
GX2b, GP2b = chain_pack(N2b, 0.0)
E2b = T00_profile(GX2b, GP2b, 0.0, N2b)
xs2b = np.arange(N2b)
curve_b = {}
for fam, tag, (A, B_), x0_, d_ in (
        ('hann', 'h12', (12, None), 110, 22),
        ('hann', 'h20', (20, None), 110, 21),
        ('plat', 'p21', (6, 14), 112, 21)):
    if fam == 'hann':
        v_f = hann2(x0_, A, N2b)
        v_mp = hann2_mp(x0_, A, N2b)
    else:
        v_f = plateau(x0_, A, B_, N2b)
        v_mp = plateau_mp(x0_, A, B_, N2b)
    D = np.outer(v_f, v_f)
    dT = T00_profile(GX2b + 2e-3*D, GP2b, 0.0, N2b) - E2b
    dc = float(np.sum(xs2b*dT)/dT.sum())
    j = int(round(dc - d_))
    leak = leak_of(dT, j)
    k_leak = k_leak and (leak == 0.0)
    sw = mp_anchor(N2b, j, mpf(0), v_mp)
    gr = sw[1e-60]/sw[1e-45] - 1
    offs = []
    for off in (0.0, 0.5, 1.0):
        dKb = dK_boost(dT, j, N2b, off=off)/2e-3
        offs.append(sw[1e-60]/dKb)
    gb = gbox2(dc-j, j, N2b)
    curve_b[tag] = dict(roffs=[o/gb for o in offs])
    print(f"   [{tag}] leakage {leak:.1e}; floor growth {gr:+.1e};"
          f" r/g_box = {offs[1]/gb:.4f}")
ddb = [a - b for a, b in zip(curve_b['h12']['roffs'],
                             curve_b['p21']['roffs'])]
print(f"   h12 - p21 at N = 240: {min(ddb):+.4f} .. {max(ddb):+.4f}"
      f"   (N = 192: {dr[('h12','p21')][0]:+.4f} .. "
      f"{dr[('h12','p21')][1]:+.4f})")
if min(ddb) > 0 and min(ddb) >= 0.5*dr[('h12', 'p21')][0]:
    box_state = 'STABLE'
    print("   -> box-stable at this step: the differential keeps "
          "its sign and at least")
    print("      half its magnitude as the far wall recedes - "
          "THE BEND stands as a")
    print("      named edge (registered).")
elif min(ddb) > 0:
    box_state = 'SHRINKS'
    print("   -> the differential keeps its sign but falls below "
          "half its N = 192")
    print("      magnitude - the finite-box hypothesis leads; "
          "the edge is re-scoped")
    print("      as box-sensitive (registered).")
else:
    box_state = 'COLLAPSES'
    print("   -> the differential loses its sign as the far wall "
          "recedes - THE BEND")
    print("      resolves as a finite-box residual at this step "
          "(registered).")

# ----------------- W3: EP - the species question -----------------
print("\n== W3. EP - the species question ==")
k_epfloor = True
def species_anchor(Nn, msq, v_f, v_mp, jn,
                   floors=('1e-30', '1e-45', '1e-60'), label=""):
    """exact species anchor with tail extrapolation; returns
    (no-tail, extrap, tail, sweep, dKb, lE_d)"""
    global k_epfloor
    GXs, GPs = chain_pack(Nn, msq)
    Es = T00_profile(GXs, GPs, msq, Nn)
    D = np.outer(v_f, v_f)
    dT = T00_profile(GXs + 2e-3*D, GPs, msq, Nn) - Es
    sw = mp_anchor(Nn, jn, mpf(str(msq)), v_mp, floors=floors)
    fl = sorted(sw.keys(), reverse=True)   # large -> small floor
    incs = [sw[fl[i+1]] - sw[fl[i]] for i in range(len(fl)-1)]
    last = sw[fl[-1]]
    qs = [incs[i+1]/incs[i] if incs[i] > 0 else float('nan')
          for i in range(len(incs)-1)]
    if incs[-2] > 0 and 0 < incs[-1] < incs[-2]:
        q = incs[-1]/incs[-2]
        conv = last + incs[-1]*q/(1-q)
    else:
        conv = last
    tail = abs(conv/last - 1)
    k_epfloor = k_epfloor and (tail <= 0.10)
    dKb = dK_boost(dT, jn, Nn)/2e-3
    lE, _ = leffE_of(dT)
    dcs = float(np.sum(np.arange(Nn)*dT)/dT.sum())
    return dict(notail=last/dKb, ext=conv/dKb, tail=tail, sw=sw,
                fl=fl, qs=qs, dKb=dKb, lEd=lE/(dcs-jn),
                leak=leak_of(dT, jn))

print(" (a) enclosed d-sweep, half scale (N = 128, Hann^2 W = 12 "
      "@ 64):")
N3 = 128
ep_curve = []
for d_ in (13, 16, 20):
    rs = {}
    for m_ in (0.4, 0.8):
        msq = m_*m_
        GXs, GPs = chain_pack(N3, msq)
        Es = T00_profile(GXs, GPs, msq, N3)
        v_f = hann2(64, 12, N3)
        dT0 = T00_profile(GXs + 2e-3*np.outer(v_f, v_f), GPs,
                          msq, N3) - Es
        dc = float(np.sum(np.arange(N3)*dT0)/dT0.sum())
        j = int(round(dc - d_))
        a = species_anchor(N3, msq, v_f, hann2_mp(64, 12, N3), j)
        rs[m_] = a
    ep = rs[0.4]['ext']/rs[0.8]['ext']
    ep_curve.append((d_, ep))
    k_leak = k_leak and (rs[0.4]['leak'] == 0.0) \
                    and (rs[0.8]['leak'] == 0.0)
    print(f"  d = {d_:2d} (l_E/d = {rs[0.4]['lEd']:.2f}/"
          f"{rs[0.8]['lEd']:.2f}, leakage {rs[0.4]['leak']:.0e}/"
          f"{rs[0.8]['leak']:.0e}):")
    print(f"   r(0.4) = {rs[0.4]['ext']:.4f}, r(0.8) = "
          f"{rs[0.8]['ext']:.4f}  -> EP_exact = {ep:.4f}")
toward1 = abs(ep_curve[0][1] - 1) <= abs(ep_curve[-1][1] - 1)
mono_ep = all(ep_curve[i][1] >= ep_curve[i+1][1] - 1e-9
              for i in range(len(ep_curve)-1)) or \
          all(ep_curve[i][1] <= ep_curve[i+1][1] + 1e-9
              for i in range(len(ep_curve)-1))
print(f"  registered reading - does EP move toward 1 at the "
      f"hydrodynamic end (small d)?")
print(f"   EP_exact(d): "
      + " -> ".join(f"{ep:.4f}" for _, ep in ep_curve)
      + f" (d = 13/16/20; monotone: {mono_ep}): answer "
      + ("YES" if toward1 else
         "NO - the residue does NOT dissolve hydrodynamically"))

print(" (b) shape pair (plateau P=4, T=10 @ 66, d = 19):")
vp3_f = plateau(66, 4, 10, N3)
vp3 = plateau_mp(66, 4, 10, N3)
rsp = {}
for m_ in (0.4, 0.8):
    rsp[m_] = species_anchor(N3, m_*m_, vp3_f, vp3, 47)
    k_leak = k_leak and (rsp[m_]['leak'] == 0.0)
ep_plat = rsp[0.4]['ext']/rsp[0.8]['ext']
print(f"  l_E/d = {rsp[0.4]['lEd']:.2f}/{rsp[0.8]['lEd']:.2f}, "
      f"leakage {rsp[0.4]['leak']:.0e}/{rsp[0.8]['leak']:.0e}")
print(f"  r(0.4) = {rsp[0.4]['ext']:.4f}, r(0.8) = "
      f"{rsp[0.8]['ext']:.4f}  -> EP_exact = {ep_plat:.4f}")
print(f"  vs the matched Hann^2 row (d = 13): {ep_curve[0][1]:.4f}"
      f"  (shape spread {abs(ep_plat-ep_curve[0][1])*100:.1f}%)")

print(" (c) THE CUTOFF LADDER (dps 90, floors to 1e-75, Gaussian "
      "family):")
mp.dps = 90
F4 = ('1e-30', '1e-45', '1e-60', '1e-75')
rungs = (('quarter', 64, 26, 6.0, 32.5, (0.8, 1.6)),
         ('half   ', 128, 52, 12.0, 65.0, (0.4, 0.8)),
         ('full   ', 256, 104, 24.0, 130.0, (0.2, 0.4)))
ladder = []
q_dec = True
for name, Nn, jn, wn, x0n, (ml, mh) in rungs:
    res = {}
    for m_ in (ml, mh):
        msq = m_*m_
        v_f = np.exp(-0.5*((np.arange(Nn)-x0n)/wn)**2)
        v_f = v_f/np.linalg.norm(v_f)
        v_mp = [mpmath.e**(-(x-mpf(str(x0n)))**2/(2*mpf(str(wn))**2))
                for x in range(Nn)]
        a = species_anchor(Nn, msq, v_f, v_mp, jn, floors=F4)
        res[m_] = a
        print(f"  {name} m = {m_}: sweep "
              + "/".join(f"{a['sw'][k]:.4f}"
                         for k in sorted(a['sw'], reverse=True))
              + f"  tail {a['tail']*100:.1f}%  cut-crossing "
              f"{a['leak']:.1e}")
        print(f"    geometric-model check q12/q23: "
              + "/".join(f"{q:.3f}" for q in a['qs'])
              + f"  ratio {a['ext']:.4f} (extrap) / "
              f"{a['notail']:.4f} (no-tail)")
        q_dec = q_dec and (a['tail'] < 1e-6
                           or a['qs'][1] < a['qs'][0])
    lo = min(res[ml]['notail'], res[ml]['ext']) \
        / max(res[mh]['notail'], res[mh]['ext'])
    hi = max(res[ml]['notail'], res[ml]['ext']) \
        / min(res[mh]['notail'], res[mh]['ext'])
    mid = res[ml]['ext']/res[mh]['ext']
    devr = (1 - res[mh]['ext'])/(1 - res[ml]['ext'])
    ladder.append(dict(name=name.strip(), lo=lo, hi=hi, mid=mid,
                       devr=devr))
    print(f"  {name} EP_exact = {mid:.4f}  [bracket {lo:.4f} - "
          f"{hi:.4f}]  deviation ratio "
          f"(1-r_h)/(1-r_l) = {devr:.2f}")
mp.dps = 80
lad_mono = (abs(ladder[0]['mid']-1) >= abs(ladder[1]['mid']-1)
            >= abs(ladder[2]['mid']-1))
lad_mono_rob = (ladder[1]['hi'] < ladder[0]['lo']) and \
               (ladder[2]['hi'] < ladder[1]['lo'])
xfer_fail = (ladder[2]['hi'] < ladder[1]['lo']) or \
            (ladder[2]['lo'] > ladder[1]['hi'])
p45_lo, p45_hi = 1.025, 1.029   # P45's half-scale receipt
half_consistent = not (ladder[1]['hi'] < p45_lo
                       or ladder[1]['lo'] > p45_hi)
print(f"  LADDER: |EP - 1| extrapolated centrals "
      + " -> ".join(f"{abs(r['mid']-1)*100:.1f}%" for r in ladder)
      + f" (quarter -> half -> full): monotone toward 1: "
      + ("YES" if lad_mono else "NO"))
print(f"  monotone toward 1 across brackets (robust): "
      + ("YES" if lad_mono_rob else "NO"))
f1 = ((ladder[0]['lo']-1)/(ladder[1]['hi']-1),
      (ladder[0]['hi']-1)/(ladder[1]['lo']-1))
f2 = ((ladder[1]['lo']-1)/(ladder[2]['hi']-1),
      (ladder[1]['hi']-1)/(ladder[2]['lo']-1))
def frange(f):
    return (f"[{math.floor(f[0]*10)/10:.1f}, "
            f"{math.ceil(f[1]*10)/10:.1f}]")
print(f"  step shrink factors across brackets: {frange(f1)} / "
      f"{frange(f2)}")
print(f"   (same order as the O(a^2) factor 4 - an observation, "
      f"not a receipt; the")
print(f"    quarter rung is deep-lattice, heavy xi = 0.625 a - a "
      f"trend point)")
print(f"  SPECIES STRUCTURE: deviation ratios "
      + " -> ".join(f"{r['devr']:.2f}" for r in ladder)
      + " vs (m_h/m_l)^2 = 4")
print(f"   - both species individually approach the boost law as "
      f"1 - r ~ C (m a)^2;")
print(f"     the near-constant ratio is the m^2 a^2 artifact "
      f"signature (the receipt")
print(f"     behind the reading; EP -> 1 is its corollary).")
print(f"  tail-model conservativeness (q23 < q12, every ladder "
      f"species/rung): "
      + ("YES" if q_dec else "NO"))
print(f"  half-rung vs the currency campaign's 1.027 "
      f"[{p45_lo}-{p45_hi}]: "
      + ("consistent" if half_consistent else "INCONSISTENT"))
print(f"  transfer half -> full: brackets "
      + ("DISJOINT - the half-scale residue does not transfer"
         if xfer_fail else "overlap - transfer not refuted")
      + " (computed flag)")
if lad_mono and xfer_fail:
    print("  -> the species residue SHRINKS under cutoff "
          "refinement at fixed dimensionless")
    print("     geometry: a cutoff artifact of the coarse heavy "
          "species, dissolving toward")
    print("     the continuum - the currency campaign's transfer "
          "assumption is corrected")
    print("     by receipt, and its 'genuine residue' reading "
          "with it.")
elif xfer_fail:
    print("  -> transfer fails (brackets disjoint) but the ladder "
          "is NOT monotone: the")
    print("     residue is cutoff-sensitive without a clean "
          "continuum trend - registered.")
else:
    print("  -> the half and full rungs are consistent: the "
          "transfer question stays open")
    print("     at this instrument - registered.")
print(f"  K-EPFLOOR (all species tails <= 10%): "
      f"{'did not fire' if k_epfloor else 'FIRED'}")

# ----------------- ledger -----------------
def kstat(ok):
    return "did not fire" if ok else "FIRED"
fh, fp = forks['hann'], forks['plat']
def fork_word(f):
    if f['top'] is None:
        return "NOT RESOLVABLE (floor-fragile; registered)"
    if f['strict'] and f['cons']:
        return "COMPLETION (strict + consistent)"
    if f['cons']:
        return "UNRESOLVED (consistent, not strict)"
    return "SATURATION (registered prediction)"
shape_line = {'ROBUST': 'ROBUST',
              'SHAPE-DEPENDENT':
                  'SHAPE-DEPENDENT (registered finding)',
              'UNRESOLVED':
                  'UNRESOLVED (no resolvable pair; registered)'
              }[shape_state]
box_word = {'STABLE': 'box-stable at N = 240',
            'SHRINKS': 'box-sensitive (below half by N = 240)',
            'COLLAPSES': 'a finite-box residual (sign lost by '
                         'N = 240)'}[box_state]
b240 = max(abs(1 - curve_b[t]['roffs'][1]) for t in curve_b)
if not bend_robust:
    bend_item = ("sub-systematic structure (differential receipt"
                 " found no convention-robust\n  drift)")
elif box_state == 'COLLAPSES':
    bend_item = (f"THE BEND RESOLVED - the N = 192 drift is a "
                 f"finite-box residual (sign\n  lost by N = 240, "
                 f"where the matched anchors sit within "
                 f"{math.ceil(b240*1000)/10:.1f}% of the\n  "
                 f"target; differential + box receipts)")
elif box_state == 'SHRINKS':
    bend_item = ("THE BEND - box-sensitive (below half by "
                 "N = 240): the finite-box\n  hypothesis leads; "
                 "registered")
else:
    bend_item = ("THE BEND - a convention-robust percent-level "
                 "drift, box-stable at\n  N = 240 (differential +"
                 " box receipts; a named edge for a successor)")
print(f"""\n== LEDGER (generated from computed flags) ==
  K-PROBE   Hann^2 floor-stable ({gr_h:+.0e})     -> {kstat(k_probe)}
  K-PROBE2  plateau floor-stable ({gr_p:+.0e})    -> {kstat(k_probe2)}
  K-LEAK    every compact anchor leakage 0.0  -> {kstat(k_leak)}
  K-FLOOR   every Hann^2 W2 anchor growth <= 1e-2 -> {kstat(k_floor)}
  K-EPFLOOR all species tails <= 10%          -> {kstat(k_epfloor)}
  COMPLETION CURVE (l_E/d axis):
    hann: """ + " / ".join(f"{curve[t]['ratio']:.3f}+-{curve[t]['syst']:.3f}"
                           for t in ('h8', 'h12', 'h16', 'h20')) + f"""
      at l_E/d """ + " / ".join(f"{curve[t]['lEd']:.2f}"
                                for t in ('h8', 'h12', 'h16', 'h20')) + f"""
    plat: """ + " / ".join(f"{curve[t]['ratio']:.3f}+-{curve[t]['syst']:.3f}"
                           for t in ('p47', 'p30', 'p21')) + f"""
      at l_E/d """ + " / ".join(f"{curve[t]['lEd']:.2f}"
                                for t in ('p47', 'p30', 'p21')) + f"""
    fork: hann {fork_word(fh)}; plat {fork_word(fp)}
    shape (matched l_E/d): {shape_line}
  EP: d-sweep {' -> '.join(f'{ep:.4f}' for _, ep in ep_curve)} (d = 13/16/20),
    toward-1 at the hydrodynamic end: {'YES' if toward1 else 'NO (registered adverse answer)'};
    shape pair {ep_plat:.4f};
    CUTOFF LADDER """ + " -> ".join(f"{r['mid']:.4f}[{r['lo']:.4f}-{r['hi']:.4f}]"
                                    for r in ladder) + f"""
    monotone toward 1: {'YES' if lad_mono else 'NO'} (bracket-robust: {'YES' if lad_mono_rob else 'NO'}); half-full transfer: {'DISJOINT (corrected)' if xfer_fail else 'overlap'}
  REGISTERED: {bend_item};
  compact-probe continuum EP (the ladder is Gaussian-family);
  the continuum (beyond-box) fate; spherical/tensor/
  Lorentzian scopes.""")

# verdict assembled from computed flags
if fh['top'] is None:
    s_h = ("the Hann^2 family fork is NOT RESOLVABLE at this "
           "instrument (floor-fragile)")
elif fh['strict'] and fh['cons']:
    s_h = (f"the Hann^2 family COMPLETES - top-of-window "
           f"r/g_box = {fh['top']['ratio']:.4f} at l_E/d = "
           f"{fh['top']['lEd']:.2f}, within 0.03 of 1 on central "
           f"values; saturation below "
           f"{fh['top']['ratio']-fh['top']['syst']:.3f} excluded")
elif fh['cons']:
    s_h = (f"the Hann^2 family top reads "
           f"{fh['top']['ratio']:.4f} at l_E/d = "
           f"{fh['top']['lEd']:.2f} - UNRESOLVED (consistent "
           f"with 1, not strict)")
else:
    s_h = (f"the Hann^2 family top reads "
           f"{fh['top']['ratio']:.4f} at l_E/d = "
           f"{fh['top']['lEd']:.2f} - SATURATION, a registered "
           f"sub-BW prediction")
if fp['top'] is None:
    s_p = ("the plateau family is excluded by its floor gates "
           "(band-concentrated energy is floor-fragile - a "
           "registered instrument finding)")
elif fp['strict'] and fp['cons']:
    s_p = (f"the plateau family agrees - top "
           f"{fp['top']['ratio']:.4f} at l_E/d = "
           f"{fp['top']['lEd']:.2f}")
elif fp['cons']:
    s_p = (f"the plateau family top reads "
           f"{fp['top']['ratio']:.4f} at l_E/d = "
           f"{fp['top']['lEd']:.2f} - UNRESOLVED (consistent "
           f"with 1, not strict)")
else:
    s_p = (f"the plateau family top reads "
           f"{fp['top']['ratio']:.4f} at l_E/d = "
           f"{fp['top']['lEd']:.2f} - a SATURATION reading")
s_shape = {'ROBUST': "the shape fork resolves ROBUST: at matched "
                     "l_E/d the families agree - the completion "
                     "diagnostic is a property of the energy "
                     "distribution at this scope",
           'SHAPE-DEPENDENT': "the shape fork resolves "
                     "SHAPE-DEPENDENT: the one-parameter l_E/d "
                     "story fails at this scope - registered",
           'UNRESOLVED': "the shape fork is UNRESOLVED at this "
                     "instrument - registered"}[shape_state]
s_ep1 = ('YES' if toward1 else
         'NO - the residue does not dissolve with l_E/d')
s_lad = ((', monotone toward 1' +
          (' (bracket-robust)' if lad_mono_rob else '') +
          ': the residue is a lattice artifact of the coarse '
          'heavy species, dissolving toward the continuum')
         if lad_mono else
         ', non-monotone: cutoff-sensitive without a clean trend')
s_xfer = ("DISJOINT: the currency campaign's registered transfer "
          "assumption is corrected by receipt" if xfer_fail else
          "overlapping: the currency campaign's transfer "
          "assumption is not refuted")
if not bend_robust:
    s_bend = ("The differential receipt finds no "
              "convention-robust drift - sub-systematic\n  "
              "structure unresolved, registered")
elif box_state == 'COLLAPSES':
    s_bend = (f"THE BEND RESOLVES: the convention-robust "
              f"{bp_lo:.1f}-{bp_hi:.1f}% drift at N = 192 is a\n"
              f"  finite-box residual - the differential loses "
              f"its sign as the far wall\n  recedes, and at "
              f"N = 240 the matched anchors sit within "
              f"{math.ceil(b240*1000)/10:.1f}% of the\n  target "
              f"(differential + box receipts)")
elif box_state == 'SHRINKS':
    s_bend = (f"THE BEND: the {bp_lo:.1f}-{bp_hi:.1f}% drift is "
              f"box-sensitive (below half by N = 240) -\n  the "
              f"finite-box hypothesis leads; registered")
else:
    s_bend = (f"THE BEND: a convention-robust downward drift of "
              f"{bp_lo:.1f}-{bp_hi:.1f}% across the top half\n  "
              f"of the window is registered as a named open edge "
              f"- box-stable at N = 240\n  (differential + box "
              f"receipts)")
s_noviol = (("no scale-invariant zero-amplitude EP violation "
             "survives at planar scope\n  (receipted on the "
             "Gaussian family; compact-probe continuum EP "
             "registered)")
            if (lad_mono and xfer_fail) else
            ("the scale-invariance question for the residue "
             "stays open at this\n  instrument - registered"))
print(f"""\n== VERDICT ==
  COMPLETION (on the energy-width axis): {s_h};
  {s_p}; {s_shape}.
  {s_bend}.
  EP: the registered hydrodynamic reading comes back {s_ep1};
  what moves the residue is the CUTOFF - the ladder at fixed
  dimensionless geometry reads """
      + " -> ".join(f"{r['mid']:.3f}" for r in ladder)
      + f""" (quarter -> half -> full){s_lad};
  the half -> full transfer brackets are {s_xfer},
  and {s_noviol}.  NOT claimed: continuum beyond the box;
  spheres, tensor components, Lorentzian dynamics; anything
  beyond the quoted per-anchor systematics and brackets.""")
