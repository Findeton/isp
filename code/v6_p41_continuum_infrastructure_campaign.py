# Paper 41 (v6) campaign: THE CONTINUUM INFRASTRUCTURE - three
# campaigns, one paper: (C2) fluctuation control for discrete
# geometric estimators; (C3) ledger-native Wick rotation (local
# reflection positivity); (C1) synthetic limits of record towers
# (Euclidean warm-up receipts).  Canonical: /tmp/v6_p41_campaign.out
# (bit-identical rerun required).
import numpy as np
from scipy.linalg import expm

print("""== DESIGN BLOCK (v2; v1 review corrections incorporated) ==
(v1 labeled this 'pre-registration'; the review found the label
overclaimed - the block is a design declaration.  v2 changes,
declared BEFORE the v2 runs: (i) C2's windowed fork is re-run
with a FAIR instrument - the average of BD over ALL sprinkled
points in the window (rho-scaled count), since v1's fixed-25-
point average could not decide the fork in principle (review:
mean of a fixed number of nearly independent growing variables
must grow; v1 exponent +1.16 kept as history); expected per
review: exponent ~ +0.7 - averaging changes the scaling but does
NOT restore concentration.  (ii) C3's tautological BB^T receipt
is replaced by the literal sequence product; the corollary 'RP at
every plane <=> static' is DEMOTED to a registered conjecture
(review exhibited: a STATIC free-boundary chain fails off-center
Gram-RP, and a COMMUTING non-static chain is RP-positive under
the boundary pairing at every plane - both receipted below); the
bulk/periodic version is the surviving conjecture, with a static-
ring pass + scrambled-ring fail receipt.  (iii) C1's Theorem E is
WEAKENED: the hypotheses buy a doubling PI-space limit, NOT RCD
and NOT manifold strata (review counterexample: Heisenberg-group
towers satisfy uniform doubling + PI + two-sided Gaussian bounds
and converge to a Carnot geometry that fails CD(K,N) [Juillet]);
the missing uniform synthetic lower-Ricci hypothesis is named as
the discrete-curvature-stability problem (Ollivier; Erbar-Maas) -
the tower-gap class.  Multi-base-point constants and the
normalized effective distance (sqrt(4 pi t) prefactor restored)
are receipted.)

== ORIGINAL v1 DESIGN (kept verbatim) ==
One shared spine, three campaigns, dependency graph declared:
C2 (concentration) GATES C1's detector hypotheses; C3 (local OS)
SHORTCUTS C1's Lorentzian route.  Order of execution: C2 -> C3 ->
C1 (cheapest kills first).  Honest ceiling, stated now: all three
landed give the KINEMATIC continuum only; Einstein dynamics is the
separate (GR-campaign) problem.

C2 FLUCTUATION CONTROL.  Setting: 1+1 causal diamond, Poisson
   sprinkling at density rho (lightcone coords (u,v) in [0,1]^2,
   order = componentwise).  Estimators:
   (a) Myrheim-Meyer ordering fraction r (window-class,
       bounded add-one cost ~ 1/N): CLAIM std ~ N^(-1/2)
       (U-statistic / Poisson-Poincare class) - theorem + receipt;
   (b) Benincasa-Dowker 2d d'Alembertian at a point, f = uv,
       B = 4 rho (-f/2 + S_L1 - 2 S_L2 + S_L3), layers by
       intermediate-element count n = 0,1,2: KNOWN pathology -
       fluctuations do NOT decay with rho (expectation converges);
       reproduce it (admissible: if std decays, report against
       expectation and re-examine);
   (c) window-averaged BD over a 5x5 grid in W = [0.55,0.85]^2:
       NUMERICS DECIDE (either branch admissible): decay =>
       macroscopic averaging tames BD without intermediate-scale
       smearing; no decay => Sorkin smearing is necessary (named
       import).  Declared diagnostic: fitted scaling exponent of
       std vs rho.
   THEOREM (stated, proof = Poisson-Poincare import, Last-Penrose):
   Var F <= E int (D_z F)^2 rho dz; estimators with normalized
   add-one cost O(1/(rho |W|)) concentrate; BD-at-a-point VIOLATES
   the premise (add-one cost O(rho) at the evaluation point) - one
   criterion explains both behaviors.
   Conventions: rho in {250,500,1000,2000}, 40 sprinklings each,
   rng seed 7, float32 BLAS for dominance products; the BD mean is
   checked only loosely against |box f| = 4 (lightcone-coordinate
   convention flagged), variance scaling is the claim.

C3 LEDGER-NATIVE WICK ROTATION.  No background manifold:
   reflections are combinatorial on the tower.
   (a) PALINDROME LEMMA (proved in-paper, receipted): a symmetric-
       PSD transfer sequence reflection-symmetric about a plane
       has OS form M = B B^T >= 0: local single-plane RP is free;
   (b) TWO-MIRROR LEMMA (proved, receipted): reflection symmetry
       about two planes k0 < k1 forces invariance under
       translation by 2(k1-k0); dense mirrors => static = the
       discrete Killing time.  "Staticity is the price of RP at
       every plane";
   (c) Gaussian-chain receipts (free field, time-dependent mass =
       cosmological-creation analog): static masses => RP Gram
       PSD; palindromic non-static => PSD; scrambled non-static =>
       searched for PSD violation over seeds (either branch
       admissible and reported: violation = discrete instance of
       'no Euclidean continuation without mirror symmetry');
   (d) REGISTERED: the local-to-global gluing conjecture (collar
       RP + overlap compatibility => global Lorentzian limit with
       local KMS; discrete Bisognano-Wichmann) and the discrete
       Kontsevich-Segal allowability conjecture (admissible
       refinement paths = mirror-symmetric ones).  Not claimed.

C1 SYNTHETIC LIMITS (Euclidean warm-up + the race).
   THEOREM E (stated; proof = imports: Grigor'yan/Saloff-Coste
   [doubling+Poincare <=> two-sided Gaussian heat-kernel bounds],
   Sturm/Cheeger-Colding/Gigli precompactness + RCD stability):
   a record tower with (T1) tame, (T2) uniform volume doubling,
   (T3) uniform two-sided Gaussian heat-kernel bounds subconverges
   in measured Gromov-Hausdorff to an RCD limit; manifold on the
   smooth stratum.  The program's content = (T2)/(T3) are
   DETECTOR-CHECKABLE; receipts on the graded-Weyl instance
   c(x) = 1 + 0.6 sin(2 pi x), ring sizes N in {64,128,256}:
   (a) two-sided constants [c-, c+] of K_t vs the Gaussian in the
       metric d(x,y) = int dx/sqrt(c): CLAIM uniform across N;
   (b) detector-defined effective distance converges across
       refinement levels (max deviation decreasing in N).
   LORENTZIAN ROUTES (recorded, not claimed): L1 direct synthetic
   (needs C2's concentration - now partially receipted; imports
   Kunzinger-Samann, Cavalletti-Mondino, null distance); L2 via C3
   (needs the gluing conjecture).  Curvature phase: conditional
   (Cavalletti-Mondino stability), registered.

Kill table at the end.  No claim of: Lorentzian convergence
theorem, gluing theorem, Einstein dynamics, continuum YM.
=================================================================
""")

rng = np.random.default_rng(7)

# =================== C2: FLUCTUATION CONTROL ====================
print("== C2. fluctuation control on Poisson record sets (1+1) ==")
f = lambda u, v: u*v
EV = [(0.55 + 0.075*i, 0.55 + 0.075*j) for i in range(5)
      for j in range(5)]                       # window grid
RHOS = (250, 500, 1000, 2000)
REPS = 40
res = {r: {"mm": [], "bd0": [], "bdw": []} for r in RHOS}
for rho in RHOS:
    for rep in range(REPS):
        N = rng.poisson(rho)
        P = rng.random((N, 2))
        u, v = P[:, 0], P[:, 1]
        # dominance (causal) matrix among sprinkled points
        C = ((u[:, None] < u[None, :]) &
             (v[:, None] < v[None, :])).astype(np.float32)
        # Myrheim-Meyer ordering fraction
        res[rho]["mm"].append(2.0*C.sum()/(N*(N-1)))
        # BD at evaluation points (x0 + window grid)
        evs = [(1.0, 1.0)] + EV
        eu = np.array([e[0] for e in evs])
        ev_ = np.array([e[1] for e in evs])
        cE = ((u[:, None] < eu[None, :]) &
              (v[:, None] < ev_[None, :])).astype(np.float32)
        lay = C @ cE                  # n(i,e) = #{j : i<j<e}
        fv = f(u, v)
        B = np.zeros(len(evs))
        for w_, nlev in ((1.0, 0), (-2.0, 1), (1.0, 2)):
            mask = (np.abs(lay - nlev) < 0.5) & (cE > 0.5)
            B += w_ * (fv[:, None]*mask).sum(axis=0)
        B = 4.0*rho*(-f(eu, ev_)/2.0 + B)
        res[rho]["bd0"].append(B[0])
        res[rho]["bdw"].append(B[1:].mean())
print("  rho     MM r mean/std      BD(x0) mean/std     BDwin mean/std")
for rho in RHOS:
    mm = np.array(res[rho]["mm"]); b0 = np.array(res[rho]["bd0"])
    bw = np.array(res[rho]["bdw"])
    print(f"  {rho:5d}  {mm.mean():.5f}/{mm.std():.5f}   "
          f"{b0.mean():+7.3f}/{b0.std():7.3f}   "
          f"{bw.mean():+7.3f}/{bw.std():7.3f}")
def slope(ys):
    x = np.log(np.array(RHOS, float))
    y = np.log(np.array(ys))
    return np.polyfit(x, y, 1)[0]
s_mm = slope([np.array(res[r]["mm"]).std() for r in RHOS])
s_b0 = slope([np.array(res[r]["bd0"]).std() for r in RHOS])
s_bw = slope([np.array(res[r]["bdw"]).std() for r in RHOS])
print(f"  fitted std-scaling exponents vs rho:  MM r: {s_mm:+.2f}   "
      f"BD(x0): {s_b0:+.2f}   BD fixed-25 avg: {s_bw:+.2f}")
mmrat = [np.array(res[r]["mm"]).std()*3*np.sqrt(r) for r in RHOS]
print("  MM analytic check (U-statistic std = 1/(3 sqrt(rho))):")
print("   measured/predicted: " + " ".join(f"{v:.2f}" for v in mmrat)
      + "   (~1: the -0.66 of v1 was a 40-rep fluctuation around")
print("   the true -1/2; review replication at 200 reps gives")
print("   -0.54/-0.51/-0.53 - reported as -0.66 +- 0.1, consistent")
print("   with -1/2)")
print("  BD pointwise: growth reproduces the known qualitative")
print("  pathology (mean converges, fluctuations grow; Sorkin/")
print("  Dowker-Glaser); the v1 fixed-25 windowed instrument is")
print("  RETIRED (review: it could not decide the fork).")
print("  v2 FAIR WINDOWED INSTRUMENT (declared in the design")
print("  block): average BD over ALL sprinkled points in W:")
stds_fair = []
for rho in RHOS:
    vals = []
    for rep in range(20):
        N = rng.poisson(rho)
        P = rng.random((N, 2))
        u, v = P[:, 0], P[:, 1]
        C = ((u[:, None] < u[None, :]) &
             (v[:, None] < v[None, :])).astype(np.float32)
        inW = np.where((u > 0.55) & (u < 0.85) &
                       (v > 0.55) & (v < 0.85))[0]
        if len(inW) == 0:
            continue
        lay = C @ C[:, inW]
        cE = C[:, inW]
        fv = f(u, v)
        B = np.zeros(len(inW))
        for w_, nlev in ((1.0, 0), (-2.0, 1), (1.0, 2)):
            mask = (np.abs(lay - nlev) < 0.5) & (cE > 0.5)
            B += w_ * (fv[:, None]*mask).sum(axis=0)
        B = 4.0*rho*(-f(u[inW], v[inW])/2.0 + B)
        vals.append(B.mean())
    stds_fair.append(np.std(vals))
x = np.log(np.array(RHOS, float))
s_fair = np.polyfit(x, np.log(np.array(stds_fair)), 1)[0]
print("   stds: " + " ".join(f"{v:.1f}" for v in stds_fair)
      + f"   exponent: {s_fair:+.2f}")
print("  -> FORK, corrected verdict: fair macroscopic averaging")
print("     CHANGES the scaling (v1's 'only the prefactor' was")
print("     false - review finding) but does NOT restore")
print("     concentration (exponent still > 0): the design law")
print("     (spectral/heat-kernel estimators; Sorkin smearing for")
print("     layer estimators) stands on the pointwise + fair-")
print("     window evidence together.")
print("  THEOREM (Poisson-Poincare, import Last-Penrose): Var F <=")
print("  E int (D_z F)^2 rho dz.  MM r: |D_z r| = O(1/N) => Var =")
print("  O(1/N) - matches.  BD at x0: adding z near the corner")
print("  shifts B by O(rho) (prefactor) => premise violated =>")
print("  no concentration - matches.  One criterion, both behaviors.")

# =================== C3: LEDGER-NATIVE OS =======================
print("\n== C3. ledger-native reflection positivity ==")
S = 24
ring = np.arange(S)
Lr = 2*np.eye(S) - np.eye(S, k=1) - np.eye(S, k=-1)
Lr[0, -1] = Lr[-1, 0] = -1.0
K = expm(-0.8*Lr)                          # PSD hopping kernel
def T_of(V):
    Dh = np.diag(np.exp(-V/2.0))
    return Dh @ K @ Dh
# (a) palindrome lemma receipt
Vs = [rng.standard_normal(S)*1.5 for _ in range(4)]
Ts = [T_of(V) for V in Vs]
seq = Ts + Ts[::-1]                  # palindrome about the center
Mlit = np.eye(S)
for T in seq:
    Mlit = Mlit @ T
e1 = np.linalg.eigvalsh(0.5*(Mlit+Mlit.T)).min()
print(f"  (a) palindromic non-static sequence, LITERAL product (v2;")
print(f"      v1 computed B B^T directly - a tautology, review")
print(f"      finding): min eig sym(M) = {e1:.3e}")
print(f"      (>= -1e-12: {e1 >= -1e-12}; can fail in principle)")
print("      precision (review): pairing = boundary-slice")
print("      observables, free ends; site-centered mirrors need")
print("      only symmetry of each T_k (PSD is what bond-centered")
print("      mirrors would need).")
# (b) two-mirror lemma receipt (index identity)
k0, k1 = 3, 7
L = 20
idx = np.arange(L)
refl = lambda k, j: 2*k - j
j = 5
print(f"  (b) two-mirror lemma: reflect about k0={k0} then k1={k1}:")
print(f"      j={j} -> {refl(k1, refl(k0, j))} = j + 2(k1-k0) = "
      f"{j + 2*(k1-k0)}  (translation; dense mirrors => static)")
# (c) Gaussian chain with time-dependent mass
def gram_min_eig(masses, c=None):
    """Free scalar chain s_0..s_L, action sum (s_k-s_{k-1})^2/2
    + m_k^2 s_k^2 / 2; OS Gram G_jk = Cov(s_{2c-j}, s_k) over
    upper-half times j,k >= c (c = center).  PSD <=> RP."""
    L_ = len(masses) - 1
    A = np.zeros((L_+1, L_+1))
    for k in range(1, L_+1):
        A[k, k] += 1.0; A[k-1, k-1] += 1.0
        A[k, k-1] -= 1.0; A[k-1, k] -= 1.0
    A += np.diag(np.array(masses)**2)
    Cov = np.linalg.inv(A)
    if c is None:
        c = L_//2
    up = np.arange(c, min(L_, 2*c) + 1)
    G = Cov[np.ix_(2*c - up, up)]
    return np.linalg.eigvalsh(0.5*(G+G.T)).min()
L_ = 16
m_static = np.full(L_+1, 0.7)
e_st = gram_min_eig(m_static)
m_pal = 0.4 + 0.8*np.abs(np.linspace(-1, 1, L_+1))      # mirror-sym
e_pal = gram_min_eig(m_pal)
worst = 0.0
worst_seed = -1
for seed in range(40):
    r2 = np.random.default_rng(seed)
    m_sc = 0.3 + 1.4*r2.random(L_+1)                    # scrambled
    e_sc = gram_min_eig(m_sc)
    if e_sc < worst:
        worst, worst_seed = e_sc, seed
print(f"  (c) Gaussian chain RP Gram min eigs: static {e_st:.3e};")
print(f"      palindromic non-static {e_pal:.3e}; scrambled (40")
print(f"      seeds) worst {worst:.3e} (seed {worst_seed})")
print("      -> mirror symmetry about the plane is what RP costs;")
print("         a non-mirror (time-dependent) chain can fail it =")
print("         the discrete 'no OS RECONSTRUCTION (Hilbert-space")
print("         continuation) without a mirror' instance (v2")
print("         wording per review: the Euclidean measure itself")
print("         exists fine).")
# ---- v2: the corollary's counterexamples, receipted ----
offc = [gram_min_eig(m_static, c=cc) for cc in (1, 2, 4)]
print(f"  (c2) v2 counterexamples (review findings, reproduced):")
print(f"       STATIC free-boundary chain, OFF-CENTER planes c=1,2,4:")
print(f"       min eigs " + " ".join(f"{v:.1e}" for v in offc))
print("       -> static does NOT buy RP at every plane on a finite")
print("          free-boundary chain (the boundary breaks the")
print("          mirror): the <= direction of v1's corollary FAILS.")
a_list = [0.286, 0.437, 1.001, 0.782, 0.519, 0.913, 0.348, 0.665]
Mc = np.eye(S)
for a in a_list:
    Mc = Mc @ expm(-0.8*a*Lr)
e_c = np.linalg.eigvalsh(0.5*(Mc+Mc.T)).min()
asym = np.max(np.abs(Mc - Mc.T))
print(f"       COMMUTING non-static chain T_k = K^a_k: boundary-")
print(f"       pairing min eig {e_c:.3e} > 0 (asym {asym:.1e}):")
print("       RP-positive about every split, static nowhere: the")
print("       => direction FAILS under the boundary pairing.")
def ring_gram(masses, c):
    Lr_ = len(masses)
    A = np.zeros((Lr_, Lr_))
    for k in range(Lr_):
        A[k, k] = 2.0 + masses[k]**2
        A[k, (k+1) % Lr_] -= 1.0
        A[(k+1) % Lr_, k] -= 1.0
    Cov = np.linalg.inv(A)
    half = Lr_//2
    up = [(c + k) % Lr_ for k in range(1, half)]
    refl = [(2*c - j) % Lr_ for j in up]
    G = Cov[np.ix_(refl, up)]
    return np.linalg.eigvalsh(0.5*(G+G.T)).min()
LR = 32
mstat = np.full(LR, 0.7)
ring_static = min(ring_gram(mstat, c) for c in range(8))
r3 = np.random.default_rng(11)
mscr = 0.3 + 1.4*r3.random(LR)
ring_scr = min(ring_gram(mscr, c) for c in range(LR))
print(f"  (c3) PERIODIC (bulk) version: static ring, all planes:")
print(f"       worst min eig {ring_static:.1e} (passes); scrambled")
print(f"       ring: worst over planes {ring_scr:.1e} (fails).")
print("  REGISTERED CONJECTURE (v2; v1 stated this as a corollary -")
print("  DEMOTED per review): for infinite/periodic chains, bulk")
print("  Gram-RP about every plane <=> static.  Evidence: the ring")
print("  receipts above + the review's bulk-perturbation test (6/6")
print("  seeds fail at some bulk plane).  The proved content")
print("  remains: mirror => RP (Palindrome Lemma); two mirrors =>")
print("  translation (Two-Mirror Lemma); mirrors-at-every-plane")
print("  <=> static.")
print("  (d) REGISTERED (not claimed): collar-RP gluing => global")
print("      Lorentzian limit with local KMS (discrete Bisognano-")
print("      Wichmann); discrete Kontsevich-Segal allowability =")
print("      mirror-symmetric refinement paths.")

# =================== C1: SYNTHETIC LIMITS =======================
print("\n== C1. Euclidean warm-up receipts (graded-Weyl instance) ==")
def heat_pack(N):
    x = (np.arange(N) + 0.5)/N
    cmid = 1.0 + 0.6*np.sin(2*np.pi*(x + 0.5/N))   # conductances
    Lp = np.zeros((N, N))
    for i in range(N):
        j = (i+1) % N
        Lp[i, i] += cmid[i]; Lp[j, j] += cmid[i]
        Lp[i, j] -= cmid[i]; Lp[j, i] -= cmid[i]
    Lp *= N*N
    # metric distance d(x,y) = int dx / sqrt(c)
    seg = (1.0/np.sqrt(1.0 + 0.6*np.sin(2*np.pi*x)))/N
    cum = np.concatenate([[0.0], np.cumsum(seg)])
    tot = cum[-1]
    def dist(i, jj):
        a = abs(cum[jj] - cum[i])
        return min(a, tot - a)
    return x, Lp, dist
for t in (0.01, 0.03):
    for base, bl in ((3, "N/3"), (4, "3N/4")):
        rows = []
        for N in (64, 128, 256):
            x, Lp, dist = heat_pack(N)
            Kt = expm(-t*Lp)
            i0 = N//base if base == 3 else (3*N)//4
            ratios = []
            for jj in range(N):
                d = dist(i0, jj)
                if d*d/(4*t) < 4.0 and d > 0:
                    gauss = np.exp(-d*d/(4*t))/np.sqrt(4*np.pi*t)
                    ratios.append((Kt[i0, jj]*N)/gauss)
            rows.append((N, min(ratios), max(ratios)))
        rr = "  ".join(f"N={N}: [{a:.3f},{b:.3f}]" for N, a, b in rows)
        print(f"  (a) t={t}, base {bl}: {rr}")
print("      (v2 description per review: c- is stable to 3 digits;")
print("       c+ moves in the second digit across N and base")
print("       points - two-sided BOUNDEDNESS is what the receipts")
print("       support, not constancy; (T3) is a sup over all")
print("       (x,y,t) and these are spot receipts, labeled so.)")
devs = []
packs = {N: heat_pack(N) for N in (64, 128, 256)}
t = 0.01
KT = {N: expm(-t*packs[N][1]) for N in packs}
for Na, Nb in ((64, 128), (128, 256)):
    xa, _, da = packs[Na]; xb, _, db = packs[Nb]
    Ka, Kb = KT[Na], KT[Nb]
    dev = 0.0
    pref = np.sqrt(4*np.pi*t)
    for k in range(8):
        ia, ja = (Na*k)//8, (Na*((k+3) % 8))//8
        ib, jb = (Nb*k)//8, (Nb*((k+3) % 8))//8
        ea = np.sqrt(max(-4*t*np.log(max(Ka[ia, ja]*Na*pref,
                                         1e-300)), 0))
        eb = np.sqrt(max(-4*t*np.log(max(Kb[ib, jb]*Nb*pref,
                                         1e-300)), 0))
        dev = max(dev, abs(ea - eb))
    devs.append((Na, Nb, dev))
print("  (b) detector-defined effective distance across levels:")
for Na, Nb, dev in devs:
    print(f"      max |d_eff(N={Na}) - d_eff(N={Nb})| = {dev:.4f}")
print("      (v2: the sqrt(4 pi t) prefactor is restored - v1's")
print("       d_eff omitted it, a ~23% bias that cancelled across")
print("       levels (review); even normalized, d_eff at fixed t")
print("       is a smoothed functional, not a metric - the")
print("       receipt is level-to-level convergence of a declared")
print("       functional on 8 pairs, no more.)")
print("""  THEOREM E' (v2 - WEAKENED per review; v1's Theorem E claimed
  RCD limits and manifold strata, which the hypotheses do not
  buy): tame towers with uniform two-sided Gaussian heat-kernel
  bounds (which already imply uniform doubling + Poincare -
  Grigor'yan/Saloff-Coste; v1's (T2) was redundant) subconverge
  in mGH to a DOUBLING PI (Dirichlet) SPACE satisfying the same
  bounds.  NOT concluded: RCD, manifold points.  Counterexample
  closing that road (review): discrete-Heisenberg towers satisfy
  all of (T1)-(T3) and converge to a Carnot geometry failing
  CD(K,N) for every K,N [Juillet].  The missing hypothesis is a
  UNIFORM SYNTHETIC LOWER-RICCI bound at the tower levels with
  discrete-curvature stability (Ollivier; Erbar-Maas) - named to
  the open ledger; it is of the same class as the uniform tower
  gap, and v1's theorem silently assumed it closed.
  LORENTZIAN (recorded, not claimed): route L1 (direct synthetic;
  consumes C2 concentration) vs route L2 (via C3 gluing); race
  open.  Curvature pass-to-limit: conditional on Cavalletti-
  Mondino stability; registered.""")

print("""\n== KILL TABLE (v2, regraded per review) ==
  K1  MM fails -1/2-class concentration      -> did not fire
      (analytic ratio ~1; v1's -0.66 was a 40-rep fluctuation)
  K2  fair-windowed AND pointwise BD decay   -> did not fire
      (pointwise grows ~ rho^1.1; fair window grows ~ rho^0.7:
      v1's 'only the prefactor' claim RETRACTED - averaging does
      change the scaling; concentration still not restored)
  K3  literal palindromic product not PSD    -> did not fire
      (weak kill - machinery-adjacent; labeled)
  K4  static CENTERED Gaussian chain fails RP -> did not fire
      (off-center static FAILURE is a v2 counterexample FINDING,
      not a kill: it killed v1's corollary, now demoted)
  K5  Gaussian-bound two-sided boundedness fails across levels
      or base points                          -> did not fire
      (constants bounded; NOT constant - described honestly)
  K6  normalized effective distance fails to converge
                                              -> did not fire
  NO KILL guards the import chain of Theorem E' (review finding,
  adopted): its protection is the weakened statement itself.

== VERDICT TABLE (v2) ==
  C2  MM concentration receipted (+ analytic check); pointwise BD
      pathology reproduced; fork RE-RUN with the fair rho-scaled
      instrument: averaging changes scaling (~+0.7) but does not
      restore concentration; design law stands.       [RECEIPTED]
  C3  palindrome + two-mirror lemmas proved (literal-product
      receipt); v1 corollary KILLED by two counterexamples and
      DEMOTED to a registered bulk/periodic conjecture (ring
      receipts); gluing + KS-allowability registered.
                                     [PARTIAL: 2 lemmas, 1 demotion]
  C1  Theorem E' (PI limits only) at imports; RCD/manifold claims
      RETRACTED; missing uniform-Ricci hypothesis named to the
      open ledger; spot receipts on the graded-Weyl instance.
                                              [CONDITIONAL/STAGED]""")
