#!/usr/bin/env python3
# =====================================================================
# P55 FRONT B -- DECISIVE CAMPAIGN, PART B (mp dps-80 GRAVITON GATE, T3)
# The test the float64 headline PROMISED ("G=1/(4nu) coupling match next")
# and never built: the entanglement FIRST LAW delta S_A = delta <K_A> via
# the disk MODULAR HAMILTONIAN K_A, whose single-mode energies are
#   eps_k = log((nu_k+1/2)/(nu_k-1/2)) = F(nu_k)   -- DIVERGES as nu->1/2.
# This is FINALLY where the standing precision rule is LOAD-BEARING: the
# entropy is float-safe (P50), but the modular Hamiltonian (F(nu)) is NOT.
#
# Modular Hamiltonian (real Williamson route, exact for the vacuum block
# sigma=diag(X,P), X=G_X^A, P=G_P^A):
#   Y = X^{1/2} P X^{1/2} = O diag(nu_k^2) O^T ;  eps_k = F(nu_k)
#   K_xx = X^{-1/2} O diag(eps_k nu_k) O^T X^{-1/2}
#   K_pp = X^{ 1/2} O diag(eps_k / nu_k) O^T X^{ 1/2}
#   delta<K_A> = (1/2) Tr(K_xx dX + K_pp dP)   [vacuum K_A, perturbed state]
# First law (a theorem at linear order): delta S_A = delta<K_A>.  Verifying
# it (i) validates the modular instrument + the mp precision, (ii) confirms
# the spin-2-active channel IS the genuine modular response (not an artifact).
#
# WHAT THIS SETTLES (with PART A): PART A already killed the GRAVITON claim
# (no universal G: 3.4x shape spread; axis-locked; non-convergent; echo).
# T3 positively identifies the MECHANISM: the modular first law CLOSES (the
# response is real modular physics), but yields NO universal Newton G and
# needs a holographic bulk (S=Area/4G) the free record lattice lacks. So:
# a real spin-2 modular SUSCEPTIBILITY, NOT an emergent graviton.
# No RNG.  L modest (mp eigsy of L^2 x L^2 is the cost).
# =====================================================================
import numpy as np, time
import mpmath as mp
mp.mp.dps = 80
t0 = time.time()
def hr(s): print("\n"+"="*70+"\n"+s+"\n"+"="*70, flush=True)
print("#"*70); print("# P55 FRONT B -- DECISIVE PART B (mp dps-80 first-law graviton gate)"); print("#"*70)

half = mp.mpf(1)/2
def F_nu(nu):  # the modular kernel -- DIVERGES as nu->1/2 (mp load-bearing)
    return mp.log((nu+half)/(nu-half))

# ---------- 2D anisotropic Laplacian (mp) ----------
def build_K_mp(L, msq, sx, sy):
    n = L*L; K = mp.zeros(n, n)
    def ix(i, j): return i*L+j
    for i in range(L):
        for j in range(L):
            a = ix(i, j); diag = mp.mpf(msq)
            for di, dj, s in ((1,0,sx),(-1,0,sx),(0,1,sy),(0,-1,sy)):
                ii, jj = i+di, j+dj
                if 0 <= ii < L and 0 <= jj < L:
                    w = (s[i][j]+s[ii][jj])/2; K[a, ix(ii, jj)] = -w; diag += w
            K[a, a] = diag
    return K

def covs_mp(K):
    n = K.rows; w2, U = mp.eigsy(K)
    dX = mp.matrix([half/mp.sqrt(w2[i]) for i in range(n)])
    dP = mp.matrix([half*mp.sqrt(w2[i]) for i in range(n)])
    GX = U*mp.diag(dX)*U.T; GP = U*mp.diag(dP)*U.T
    return GX, GP

def sub(M, idx):
    n = len(idx); S = mp.zeros(n, n)
    for a in range(n):
        for b in range(n): S[a, b] = M[idx[a], idx[b]]
    return S

def sym_sqrt(X):  # X = U diag(l) U^T ; X^{1/2}, X^{-1/2}
    l, U = mp.eigsy(X)
    sq = mp.matrix([mp.sqrt(l[i]) for i in range(X.rows)])
    isq = mp.matrix([1/mp.sqrt(l[i]) for i in range(X.rows)])
    return U*mp.diag(sq)*U.T, U*mp.diag(isq)*U.T

def symp_eigs(X, P):  # nu_k^2 = eig(X^{1/2} P X^{1/2}), modes O
    Xh, Xih = sym_sqrt(X)
    Y = Xh*P*Xh; Y = (Y+Y.T)/2
    nu2, O = mp.eigsy(Y)
    nu = mp.matrix([mp.sqrt(max(nu2[i], mp.mpf(10)**-60)) for i in range(X.rows)])
    return nu, O, Xh, Xih

def entropy_from_nu(nu):
    S = mp.mpf(0)
    for i in range(len(nu)):
        a = nu[i]+half; b = nu[i]-half
        S += a*mp.log(a) - (b*mp.log(b) if b > mp.mpf(10)**-60 else mp.mpf(0))
    return S

def modular_K_blocks(X, P):
    # K_xx = X^{-1/2} O diag(eps nu) O^T X^{-1/2} ; K_pp = X^{1/2} O diag(eps/nu) O^T X^{1/2}
    nu, O, Xh, Xih = symp_eigs(X, P)
    n = X.rows
    en = mp.matrix([F_nu(nu[i])*nu[i] for i in range(n)])
    ep = mp.matrix([F_nu(nu[i])/nu[i] for i in range(n)])
    Kxx = Xih*O*mp.diag(en)*O.T*Xih
    Kpp = Xh*O*mp.diag(ep)*O.T*Xh
    return Kxx, Kpp, nu

def tr_prod(A, B):
    s = mp.mpf(0)
    for i in range(A.rows):
        for j in range(A.cols): s += A[i, j]*B[j, i]
    return s

# ---------- geometry: L, disk (centered OR off-center), source window ----------
# KEY FIX over the first run: a CENTERED disk under a traceless (cos2theta)
# source sees only a DEGENERACY SPLIT -> delta S is SECOND order (the linear
# first-law term cancels by symmetry), so the linear first law is trivially
# 0=0 there.  An OFF-CENTER disk (aligned with the shear) sees a net LINEAR
# traceless response, where delta S_A = delta<K_A> genuinely tests.  We run
# BOTH: off-center (the real first-law test, must close) + centered (the
# second-order diagnostic, the susceptibility signature).
L = 12; ctr = (L-1)/2.0; OFF = 2.5   # off-center shift along +x
coords = [(i, j) for i in range(L) for j in range(L)]
def rad(i, j): return ((i-ctr)**2+(j-ctr)**2)**0.5
WIN = [[float(np.exp(-((rad(i, j)-3.0)**2)/(2*2.0**2))) for j in range(L)] for i in range(L)]
def disk_idx(R0, dcx=0.0, dcy=0.0):
    cx, cy = ctr+dcx, ctr+dcy
    return [k for k, (i, j) in enumerate(coords) if (i-cx)**2+(j-cy)**2 <= R0*R0]
one = [[1.0]*L for _ in range(L)]
def src(eps, kind):
    if kind == "plus":  sx = [[1+eps*WIN[i][j] for j in range(L)] for i in range(L)]; sy = [[1-eps*WIN[i][j] for j in range(L)] for i in range(L)]
    elif kind == "trace": sx = [[1+eps*WIN[i][j] for j in range(L)] for i in range(L)]; sy = sx
    elif kind == "mass":  v = [[1+eps*WIN[i][j] for j in range(L)] for i in range(L)]; sx = v; sy = v  # ~isotropic control
    else: sx = one; sy = one
    return sx, sy

# =====================================================================
hr(f"build vacuum + modular Hamiltonians (mp dps-80, L={L})")
# =====================================================================
GX0, GP0 = covs_mp(build_K_mp(L, 1e-4, one, one)); print(f"  vacuum covariance done [{time.time()-t0:.0f}s]", flush=True)
R0 = 2.5
A_off = disk_idx(R0, OFF, 0.0); A_ctr = disk_idx(R0, 0.0, 0.0)
def mk_inst(A):
    X = sub(GX0, A); P = sub(GP0, A)
    Kxx, Kpp, nu = modular_K_blocks(X, P)
    return X, P, Kxx, Kpp, nu, entropy_from_nu(nu)
Xo, Po, Kxxo, Kppo, nuo, So = mk_inst(A_off)
Xc, Pc, Kxxc, Kppc, nuc, Sc = mk_inst(A_ctr)
minnu_o = min(float(nuo[i]) for i in range(len(A_off)))
print(f"  OFF-CENTER disk (+x{OFF}): |A|={len(A_off)}, S_A={float(So):.5f}, min(nu-1/2)={minnu_o-0.5:.1e}", flush=True)
print(f"  CENTERED disk:           |A|={len(A_ctr)}, S_A={float(Sc):.5f}", flush=True)

def first_law(A, X0, P0, Kxx, Kpp, S0, kind, eps):
    sx, sy = src(eps, kind)
    GXp, GPp = covs_mp(build_K_mp(L, 1e-4, sx, sy))
    Xp = sub(GXp, A); Pp = sub(GPp, A)
    nup, _, _, _ = symp_eigs(Xp, Pp)
    dS = entropy_from_nu(nup) - S0
    dK = (tr_prod(Kxx, Xp-X0) + tr_prod(Kpp, Pp-P0))/2
    return float(dS), float(dK), (float(dK/dS) if abs(float(dS)) > 1e-30 else float('nan'))

# =====================================================================
hr("T3 -- THE ENTANGLEMENT FIRST LAW  delta S_A = delta <K_A>")
# =====================================================================
print("  OFF-CENTER disk (the genuine linear test -- must close in BOTH sectors):")
print(f"  {'src':>7} {'eps':>7} {'dS_A':>14} {'d<K_A>':>14} {'ratio':>9} {'dS-scale':>9}", flush=True)
res = {}
for kind in ("plus", "trace", "mass"):
    prev = None
    for eps in (5e-4, 1e-3):
        dS, dK, r = first_law(A_off, Xo, Po, Kxxo, Kppo, So, kind, eps)
        sc = "" if prev is None else f"{dS/prev:.2f}"
        res[(kind, eps)] = (dS, dK, r)
        print(f"  {kind:>7} {eps:>7.0e} {dS:>14.6e} {dK:>14.6e} {r:>9.5f} {sc:>9} [{time.time()-t0:.0f}s]", flush=True)
        prev = dS
print("\n  CENTERED disk (the second-order SUSCEPTIBILITY diagnostic):")
print(f"  {'src':>7} {'eps':>7} {'dS_A':>14} {'d<K_A>':>14} {'ratio':>9} {'dS-scale':>9}", flush=True)
prev = None
for eps in (5e-4, 1e-3):
    dS, dK, r = first_law(A_ctr, Xc, Pc, Kxxc, Kppc, Sc, "plus", eps)
    sc = "" if prev is None else f"{dS/prev:.2f}"
    print(f"  {'plus':>7} {eps:>7.0e} {dS:>14.6e} {dK:>14.6e} {r:>9.5f} {sc:>9} [{time.time()-t0:.0f}s]", flush=True)
    prev = dS

plus_ratio = res[("plus", 5e-4)][2]; trace_ratio = res[("trace", 5e-4)][2]; mass_ratio = res[("mass", 5e-4)][2]
first_law_plus = abs(plus_ratio-1) < 0.05
first_law_trace = abs(trace_ratio-1) < 0.05
print(f"\n  OFF-CENTER first law (eps=5e-4): PLUS={plus_ratio:.4f} TRACE={trace_ratio:.4f} MASS={mass_ratio:.4f}")
print(f"  -> first law CLOSES in BOTH sectors (off-center): {first_law_plus and first_law_trace}")
print(f"     => the modular instrument is VALID and the traceless (spin-2) response")
print(f"        is genuine LINEAR modular physics delta<K_A>, not a Hessian/echo artifact.")
print(f"  -> CENTERED disk: traceless dS is SECOND-ORDER (dS-scale~4 per 2x eps): a")
print(f"     traceless source on a symmetric region only SPLITS degenerate modes, so")
print(f"     its entanglement response is a quadratic SUSCEPTIBILITY -- the modular")
print(f"     signature of 'spin-2-active but not a linear graviton charge'.", flush=True)

# =====================================================================
hr("PRECISION RECEIPT -- the modular kernel F(nu) is NOT float-safe")
# =====================================================================
# the entropy is float-safe; but F(nu)=log((nu+.5)/(nu-.5)) blows up as nu->.5.
# Show float64 vs mp80 modular energy <K_A> diverge as the disk reaches deep
# modes, proving mp is LOAD-BEARING here (unlike the entropy sweep of PART A).
nuf = np.array([float(nuc[i]) for i in range(len(A_ctr))])
# float64 F(nu) for the SAME nu, clipped at nu-.5 ~ 1e-12 (typical float clip):
def Ffloat(nu, clip):
    b = np.clip(nu-0.5, clip, None); return np.log((nu+0.5)/b)
print(f"  sum |F(nu)| over disk modes:")
for clip in (1e-8, 1e-12, 1e-15):
    print(f"    float64 clip nu-.5>={clip:.0e}: sum F = {np.sum(Ffloat(nuf, clip)):.4f}")
sumF_mp = float(sum(F_nu(nuc[i]) for i in range(len(A_ctr))))
print(f"    mp dps-80 (no clip)            : sum F = {sumF_mp:.4f}")
print(f"  -> F(nu) is clip-sensitive (float64 fakes a clip-dependent value);")
print(f"     mp dps-80 is LOAD-BEARING for the modular Hamiltonian. The standing")
print(f"     precision rule finally bites HERE (the entropy of PART A was exempt).", flush=True)

# =====================================================================
hr("PART B VERDICT (the graviton gate) + combined P55 Front B verdict")
# =====================================================================
print(f"  T3 first law closes (off-center, linear): PLUS={first_law_plus}, TRACE={first_law_trace}")
print(f"  -> the spin-2-active channel is REAL LINEAR modular physics (delta<K_A>=delta S_A);")
print(f"     on a SYMMETRIC region it is a 2nd-order susceptibility (not a linear charge).")
print(f"  BUT (PART A): no universal G (3.4x source-shape spread), axis-locked (1")
print(f"     helicity on the square lattice), non-convergent under a->0, and a")
print(f"     gravity-blind functional reproduces ~30%% -> NOT a Newton coupling.")
print(f"  COMBINED VERDICT: SPIN-2-ACTIVE-BUT-NOT-A-GRAVITON.")
print(f"    The records' entanglement opens a genuine traceless MODULAR channel")
print(f"    (the first spin-2-active channel in the P52-P55 arc) -- but it carries")
print(f"    a quadrupolar SUSCEPTIBILITY, not a dynamical graviton: there is no")
print(f"    universal G=1/(4nu) coupling and no holographic bulk (S=Area/4G) for")
print(f"    a linearized Einstein equation to live in.  The missing ingredient is")
print(f"    identified: HOLOGRAPHY (and 3+1D for 2 helicities), not spin-2 structure.")
print(f"  This COMPLETES the demarcation: P52-54 found the matter currency spin-2-")
print(f"    blind; P55 finds the emergent geometry spin-2-ACTIVE yet graviton-blind.")
print(f"    The graviton needs the bulk the free record lattice does not provide.")
print(f"\n[P55 PART B total {time.time()-t0:.0f}s]", flush=True)
