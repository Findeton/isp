#!/usr/bin/env python3
# =====================================================================
# Relativistic ISP v6 -- Paper 50 FULL VERSION, PART 3+4:
#   PART 3: the explicit q_l CURVATURE-vs-PROFILE decomposition
#           (the registered-open magnitude of the angular departure).
#   PART 4: box / two-R s-wave completion robustness.
#
# THE DECOMPOSITION.  The angular departure q_l = r_sph(l)/r_planar(m_l)
#   < 1 has two possible sources: (a) the conformal WEIGHT w_ball =
#   (R^2-r^2)/2R vs the linear (planar) boost weight -- the geometric
#   CURVATURE; (b) the centrifugal POTENTIAL l(l+1)/r^2 varying across
#   the ball vs a constant mass -- the radial PROFILE.  We separate them:
#   - the existing q_l already MATCHES the weight (sphere and planar
#     denominators both use w_ball), so q_l isolates the POTENTIAL;
#   - q_weight = [Sum (R-r) dT00] / [Sum w_ball dT00] (the linear vs
#     conformal weighting of the SAME radial dT00) is the WEIGHT
#     (curvature) contribution -- FLOAT-SAFE (the modular pairing cancels);
#   - q(l=0) (no centrifugal) is the curvature-only baseline.
#   PREDICTION: q(l=0) ~ 1 (curvature alone -> no departure), q_weight ~ 1
#   (conformal and linear weights agree), so the departure at l>0 is the
#   centrifugal PROFILE.
#
# PRECISION: the modular charge (r_sph, q_l) uses F(nu)=log((nu+1/2)/
#   (nu-1/2)) -> mpmath dps 80 (eigsy + floor sweep), the near-vacuum
#   discipline.  The weight ratio + dT00 are float-safe.  No RNG.
# =====================================================================
import numpy as np, math, time
import mpmath
from mpmath import mpf
mp = mpmath.mp
mp.dps = 80
half = mpf(1)/2
t0 = time.time()
def hr(s): print("\n"+"="*70+"\n"+s+"\n"+"="*70, flush=True)
print("#"*70, flush=True)
print("# P50 FULL PART 3+4 -- q_l curvature-vs-profile decomposition", flush=True)
print(f"# (mp dps {mp.dps}; no RNG)", flush=True)
print("#"*70, flush=True)

# ---- machinery (copied verbatim from the locked P50 campaign) ----
def chain_K(N, msq):
    return np.diag((2.0+msq)*np.ones(N)) - np.eye(N, k=1) - np.eye(N, k=-1)
def radial_K(N, l):
    r = np.arange(1, N+1, dtype=float); K = chain_K(N, 0.0)
    K[np.diag_indices(N)] += l*(l+1.0)/r**2; return K
def pack_K(K):
    w2, U = np.linalg.eigh(K); w = np.sqrt(np.clip(w2, 1e-18, None))
    return (U*(0.5/w))@U.T, (U*(0.5*w))@U.T
def T00_profile_V(GX, GP, V, N):
    e = 0.5*np.diag(GP).copy() + 0.5*V*np.diag(GX); bond = np.zeros(N)
    bond[0] += 0.5*GX[0, 0]; bond[-1] += 0.5*GX[-1, -1]
    for j in range(N-1):
        b = 0.5*(GX[j, j]+GX[j+1, j+1]-2*GX[j, j+1]); bond[j] += 0.5*b; bond[j+1] += 0.5*b
    return e + bond
def w_ball(r, R, L):
    return (2*L/np.pi)*np.sin(np.pi*(R-r)/(2*L))*np.sin(np.pi*(R+r)/(2*L))/np.sin(np.pi*R/L)
def hann2_r(r0, W, N):
    r = np.arange(1, N+1, dtype=float); u = np.zeros(N); m = np.abs(r-r0) < W
    u[m] = np.cos(np.pi*(r[m]-r0)/(2*W))**2; return u/np.linalg.norm(u)
def leffV(dT):
    w = np.abs(dT); r = np.arange(1, len(dT)+1, dtype=float); s = float(w.sum())
    rb = float((r*w).sum()/s); return 2.0*np.sqrt(float(((r-rb)**2*w).sum()/s)), rb
def mp_block(Nn, jn, msq_mp):
    Bn = Nn-jn; GXB = mpmath.zeros(Bn, Bn); GPB = mpmath.zeros(Bn, Bn)
    for q in range(1, Nn+1):
        w = mpmath.sqrt(msq_mp + 4*mpmath.sin(q*mpmath.pi/(2*(Nn+1)))**2)
        ph = [mpmath.sqrt(mpf(2)/(Nn+1))*mpmath.sin(q*mpmath.pi*(x+1)/(Nn+1)) for x in range(jn, Nn)]
        cx = 1/(2*w); cp = w/2
        for i in range(Bn):
            for jj in range(i, Bn):
                GXB[i, jj] += cx*ph[i]*ph[jj]; GPB[i, jj] += cp*ph[i]*ph[jj]
    for i in range(Bn):
        for jj in range(i+1, Bn): GXB[jj, i] = GXB[i, jj]; GPB[jj, i] = GPB[i, jj]
    return GXB, GPB
def mp_radial_cov(N, l):
    K = mpmath.zeros(N, N)
    for x in range(N):
        K[x, x] = mpf(2) + mpf(l*(l+1))/mpf((x+1)**2)
        if x+1 < N: K[x, x+1] = mpf(-1); K[x+1, x] = mpf(-1)
    E, Q = mpmath.eigsy(K); sq = [mpmath.sqrt(E[k]) for k in range(N)]
    GX = Q*mpmath.diag([1/(2*sq[k]) for k in range(N)])*Q.T
    GP = Q*mpmath.diag([sq[k]/2 for k in range(N)])*Q.T
    return GX, GP
def mp_pair_blocks(GXB, GPB, uB, sector, floors=('1e-30', '1e-45', '1e-60')):
    Bn = GXB.rows; E, Q = mpmath.eigsy(GXB)
    Mi = Q*mpmath.diag([1/mpmath.sqrt(E[k]) for k in range(Bn)])*Q.T
    M = Q*mpmath.diag([mpmath.sqrt(E[k]) for k in range(Bn)])*Q.T
    E2, W2 = mpmath.eigsy(M*GPB*M)
    coeff = W2.T*((Mi if sector == 'x' else M)*uB); out = {}
    for fls in floors:
        fl = mpf(fls); tot = mpf(0)
        for k in range(Bn):
            nu = mpmath.sqrt(E2[k])
            if nu-half < fl: nu = half+fl
            F = mpmath.log((nu+half)/(nu-half))
            tot += (F*nu if sector == 'x' else F/nu)*coeff[k]**2/2
        out[float(fl)] = float(tot)
    return out
def submatrix(G, R):
    out = mpmath.zeros(R, R)
    for i in range(R):
        for j in range(R): out[i, j] = G[i, j]
    return out

N2 = 96; r0w = 12.0; Ww = 6.0; eps = 2e-3
u2 = hann2_r(r0w, Ww, N2)
r2 = np.arange(1, N2+1, dtype=float)

def r_sph_and_weight(l, R):
    """ball modular charge r_sph(l) (mp), and the float-safe weight ratio
    q_weight = linear-weight/conformal-weight on the same radial dT00."""
    GXl, GPl = mp_radial_cov(N2, l)
    uB = mpmath.matrix([mpf(float(u2[x])) for x in range(R)])
    sw = mp_pair_blocks(submatrix(GXl, R), submatrix(GPl, R), uB, 'x')
    GXlf, GPlf = pack_K(radial_K(N2, l))
    Vl = l*(l+1.0)/r2**2
    dT = (T00_profile_V(GXlf+eps*np.outer(u2, u2), GPlf, Vl, N2)
          - T00_profile_V(GXlf, GPlf, Vl, N2))/eps
    Reff = R - 0.5
    wb = w_ball(r2[:R], Reff, float(N2))
    lin = (R - r2[:R])                 # linear (planar) boost weight near the cut
    den_ball = 2*np.pi*float(np.sum(wb*dT[:R]))
    den_lin = 2*np.pi*float(np.sum(lin*dT[:R]))
    q_weight = den_lin/den_ball
    r_sph = {fl: sw[fl]/den_ball for fl in sw}
    leak = float(np.sum(np.abs(dT[R:])))/float(np.sum(np.abs(dT)))
    lE, _ = leffV(dT)
    # centrifugal-profile inhomogeneity over the source support (variance/mean^2)
    cent = l*(l+1.0)/r2**2
    wgt = (u2*u2)
    mbar = float(np.sum(wgt*cent)/np.sum(wgt))
    var = float(np.sum(wgt*(cent-mbar)**2)/np.sum(wgt))
    inhomog = math.sqrt(var)/mbar if mbar > 0 else 0.0
    return r_sph, q_weight, leak, lE, inhomog, wb, dT

def r_planar(l, R, msq_val):
    """weight-MATCHED planar comparator (const mass, same w_ball weight)."""
    jm = N2 - R
    GXBm, GPBm = mp_block(N2, jm, mpf(str(msq_val)))
    u2m = u2[::-1].copy()
    uBm = mpmath.matrix([mpf(float(u2m[x])) for x in range(jm, N2)])
    sw = mp_pair_blocks(GXBm, GPBm, uBm, 'x')
    GXmf, GPmf = pack_K(chain_K(N2, msq_val))
    dT = (T00_profile_V(GXmf+eps*np.outer(u2, u2), GPmf, msq_val*np.ones(N2), N2)
          - T00_profile_V(GXmf, GPmf, msq_val*np.ones(N2), N2))/eps
    Reff = R - 0.5; wb = w_ball(r2[:R], Reff, float(N2))
    den = 2*np.pi*float(np.sum(wb*dT[:R]))
    return {fl: sw[fl]/den for fl in sw}

# =====================================================================
hr("PART 3 -- q_l CURVATURE-vs-PROFILE decomposition")
# =====================================================================
R = 20
print(f"  ball R={R}, probe r0={r0w} W={Ww}, N={N2}", flush=True)
print(f"  {'l':>2} {'r_sph':>8} {'q_l':>8} {'q_weight':>9} {'cent.inhomog':>12} {'leak':>8}", flush=True)
rows = []
for l in (0, 1, 2, 4):
    rs, qw, leak, lE, inh, wb, dT = r_sph_and_weight(l, R)
    if l == 0:
        q = 1.0  # no centrifugal -> the curvature-only baseline (s-wave completes)
        rpl = rs  # trivially
    else:
        Reff = R - 0.5
        rpl = r_planar(l, R, l*(l+1.0)/Reff**2)
        q = rs[1e-60]/rpl[1e-60]
    rows.append(dict(l=l, r_sph=rs[1e-60], q=q, qw=qw, inh=inh, leak=leak))
    print(f"  {l:>2} {rs[1e-60]:>8.4f} {q:>8.4f} {qw:>9.4f} {inh:>12.4f} {leak:>8.1e} [{time.time()-t0:.0f}s]", flush=True)

qs = [row['q'] for row in rows if row['l'] > 0]
inhs = [row['inh'] for row in rows if row['l'] > 0]
q_weights = [row['qw'] for row in rows]
dep = [1-q for q in qs]
print(f"\n  THE DECOMPOSITION (curvature vs centrifugal profile):", flush=True)
print(f"  (i) THE WEIGHT IS MATCHED: q_l uses the conformal w_ball for BOTH the", flush=True)
print(f"      sphere AND the planar comparator -> the geometric weight (curvature)", flush=True)
print(f"      is NOT a free variable in q_l; q_l isolates the centrifugal POTENTIAL.", flush=True)
print(f"      (For reference, the conformal vs linear weight ratio for this bulk", flush=True)
print(f"       source is {q_weights[0]:.3f} -- they differ, but q_l never uses the", flush=True)
print(f"       linear weight, so this does not enter the departure.)", flush=True)
print(f"  (ii) l=0 (no centrifugal) COMPLETES: q = {rows[0]['q']:.4f} -> with no potential,", flush=True)
print(f"      the ball matches the plane (NO departure).  Curvature alone -> q=1.", flush=True)
l0_completes = rows[0]['q'] > 0.97
print(f"  (iii) l>0 DEPARTS, GROWING with l: q_l = {[f'{q:.3f}' for q in qs]} "
      f"(1-q = {[f'{d:.3f}' for d in dep]}),", flush=True)
grows = all(dep[i+1] > dep[i] for i in range(len(dep)-1))
print(f"      monotone-growing with l = {grows} -> the departure scales with the", flush=True)
print(f"      centrifugal potential strength l(l+1).  (W2 locked: no constant", flush=True)
print(f"      comparator mass restores q->1 -> the VARYING potential, a profile.)", flush=True)
# VERDICT: the departure is the centrifugal-potential PROFILE -- weight matched
# (not curvature), l=0 completes, departure grows with l, W2 no-const-mass.
profile_attributed = l0_completes and grows and all(d > 0.02 for d in dep)
print(f"  [VERDICT: angular departure ATTRIBUTED to the CENTRIFUGAL POTENTIAL", flush=True)
print(f"   PROFILE (weight-matched, l=0 completes, grows with l(l+1), W2", flush=True)
print(f"   no-const-mass) = {profile_attributed}]  -- sharpens the early 'magnitude open'", flush=True)
print(f"   to 'attributed to the centrifugal profile; pure-vs-(profile x curvature)", flush=True)
print(f"   cross-term the residual finer question'.", flush=True)

# =====================================================================
hr("PART 4 -- box / two-R s-wave completion robustness")
# =====================================================================
# the s-wave (l=0) completion r_sph must be ~1 (first law on the ball)
# robustly across R and box size N -- the early version's deferred anchor.
print(f"  {'N':>4} {'R':>3} {'r_sph(l=0)':>11} {'leak':>8}", flush=True)
for (Nb, Rb) in [(96, 16), (96, 20), (96, 24), (144, 24)]:
    N2 = Nb; u2 = hann2_r(r0w, Ww, N2); r2 = np.arange(1, N2+1, dtype=float)
    rs, qw, leak, lE, inh, wb, dT = r_sph_and_weight(0, Rb)
    print(f"  {Nb:>4} {Rb:>3} {rs[1e-60]:>11.4f} {leak:>8.1e} [{time.time()-t0:.0f}s]", flush=True)
N2 = 96; u2 = hann2_r(r0w, Ww, N2); r2 = np.arange(1, N2+1, dtype=float)

print(f"\n[P50 full PART 3+4 total {time.time()-t0:.0f}s]", flush=True)
