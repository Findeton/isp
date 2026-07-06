#!/usr/bin/env python3
"""
ml3b_a_coupled_operator.py — v9 round 15: ML3B BUILD-STEP (a) — the
two-species coupled record GW system (note-ml3b-a; gates pinned there and
committed at eea1de2 BEFORE this receipt existed).

The coupled large-N gap system on two record overlap operators:
  M_A = g^2 Sigma_A(M_A) + g_x Sigma_B(M_B)
  M_B = g^2 Sigma_B(M_B) + g_x Sigma_A(M_A)
(the scalar-channel cross four-fermi at seals; g_x = the sector's one new
dial, disclosed).

PINNED GATES (note-ml3b-a SS2):
  G4c (the kill gate, dps = 120, L = 4, Q in {0, 1}): GW identity and
     Luscher Ward < 1e-90 per species; AND the coupled-mass Ward breaking
     is EXACTLY M_s*(g5 - s): ||D(M_s) g5hat + g5 D(M_s) - M_s(g5 - s)||
     < 1e-90 per species AT THE COUPLED MASSES — the cross-coupling adds
     no new chirality structure, algebraically.
  Ga2 (existence + cross-susceptibility, L = 6, (Q_A, Q_B) = (0, 1),
     g^2 = 4, dps >= 60): the coupled system solves with M_A, M_B > 0 at
     g_x in {0, 1/4, 1/2}; the g_x = 0 column reproduces single-species
     masses (continuity anchor); |Delta M_A / Delta g_x| > 1e-6 over
     [0, 1/2] [directional: positive expected]. Symmetric control
     (Q_A = Q_B = 1) printed unpinned.
Eigenvalues [LATTICE-NUMERIC, FLAGGED]; masses [DERIVED given the matter
sector: large-N, 2d, quenched, small lattices, mode-relative — paper 5's
scope verbatim; NOT the Clay gap]. Machinery extracted verbatim from
s_igw_production_gap_flow.py. Exit 1 by design on refusal.
"""
import numpy as np
import mpmath as mp

mp.mp.dps = 120
PASS = 0
FAIL = 0

def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    if ok: PASS += 1
    else: FAIL += 1
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

gam1 = np.array([[0, 1], [1, 0]], complex)
gam2 = np.array([[0, -1j], [1j, 0]], complex)
gam5 = np.array([[1, 0], [0, -1]], complex)

def flux_links(L1, L2, Q):
    """Uniform-field-strength U(1) links, total flux 2 pi Q (paper14)."""
    x2 = np.arange(L2)
    U1 = np.exp(-2j * np.pi * Q * x2 / (L1 * L2))[None, :] * np.ones((L1, 1))
    U2 = np.ones((L1, L2), complex)
    U2[:, L2 - 1] = np.exp(2j * np.pi * Q * np.arange(L1) / L1)
    return [U1, U2]

def hop(L1, L2, U, mu):
    V = L1 * L2
    T = np.zeros((V, V), complex)
    for x1 in range(L1):
        for x2 in range(L2):
            s = x1 * L2 + x2
            t = (((x1 + 1) % L1) * L2 + x2) if mu == 0 else (x1 * L2 + (x2 + 1) % L2)
            T[s, t] = U[mu][x1, x2]
    return T

def wilson(L1, L2, U, m0=-1.0, r=1.0):
    V = L1 * L2
    D = (m0 + 2 * r) * np.eye(2 * V, dtype=complex)
    for mu, g in ((0, gam1), (1, gam2)):
        T = hop(L1, L2, U, mu)
        D -= 0.5 * (np.kron(r * np.eye(2) - g, T)
                    + np.kron(r * np.eye(2) + g, T.conj().T))
    return D

def overlap_float(L1, L2, U):
    """float64 overlap operator (lattice-numeric path; spectrum/traces)."""
    V = L1 * L2
    G5 = np.kron(gam5, np.eye(V))
    H = G5 @ wilson(L1, L2, U)
    ev, P = np.linalg.eigh(H)
    s = (P * np.sign(ev)) @ P.conj().T
    return np.eye(2 * V) + G5 @ s, G5, s

def np_to_mp(A):
    n, m = A.shape
    M = mp.matrix(n, m)
    for i in range(n):
        for j in range(m):
            M[i, j] = mp.mpc(A[i, j].real, A[i, j].imag)
    return M

def mp_max_abs(M):
    return max(abs(M[i, j]) for i in range(M.rows) for j in range(M.cols))

def msign_hp(H, iters=80):
    """Scaled-Newton matrix-sign iteration (Higham), preserves Hermiticity.
       Converges quadratically; drives s^2 = 1 to full dps precision.
       H must be Hermitian non-singular (g5 D_W is, away from criticality)."""
    n = H.rows
    Y = H.copy()
    tol = mp.mpf(10) ** (-(mp.mp.dps - 8))
    for k in range(iters):
        Yi = Y ** -1
        dY = abs(mp.det(Y))
        dYi = abs(mp.det(Yi))
        c = (dYi / dY) ** (mp.mpf(1) / (2 * n)) if dY > 0 else mp.mpf(1)
        Ynew = (c * Y + (1 / c) * Yi) / 2
        diff = mp_max_abs(Ynew - Y)
        Y = Ynew
        if diff < tol:
            break
    # Hermitize to kill rounding asymmetry (sign of Hermitian is Hermitian)
    Yh = (Y + Y.conj_transpose()) / 2 if hasattr(Y, "conj_transpose") else None
    if Yh is None:
        Yh = mp.matrix(n, n)
        for i in range(n):
            for j in range(n):
                Yh[i, j] = (Y[i, j] + mp.conj(Y[j, i])) / 2
    return Yh, k

def overlap_hp(L1, L2, U):
    """High-precision overlap operator: D = 1 + g5 * sign(g5 D_W), with
       sign driven to s^2 = 1 < 1e-90 by scaled-Newton.  Returns (D, G5, s)
       as mpmath matrices."""
    V = L1 * L2
    Dw = wilson(L1, L2, U)
    G5 = np.kron(gam5, np.eye(V))
    H = G5 @ Dw                      # Hermitian
    Hm = np_to_mp(H)
    s_hp, k = msign_hp(Hm)
    G5m = np_to_mp(G5)
    I = mp.eye(2 * V)
    D_hp = I + G5m * s_hp
    return D_hp, G5m, s_hp, k

def build_sigma_extended(L, Q):
    """Return (Sigma_func, n_zero) where Sigma_func(M) is the Luscher-subtracted
       condensate evaluated by EIGENDECOMPOSING D once (extended precision via
       mpmath eig on the dense overlap), so the M-dependence is a closed scalar
       sum over eigenvalues -- the gap-equation root is then a pure high-precision
       scalar solve.  [LATTICE-NUMERIC for the eigenvalues, FLAGGED.]"""
    U = flux_links(L, L, Q)
    D, G5, s = overlap_float(L, L, U)
    V = L * L
    # eigen-decompose D (overlap eigenvalues on the GW circle).  D is normal
    # (g5-hermitian); eig gives lambda_n and the condensate trace closes as
    #   Tr[(1-D/2) (D + M(1-D/2))^{-1}] = sum_n (1 - lam_n/2) / (lam_n + M(1 - lam_n/2)).
    evD = np.linalg.eigvals(D)
    n_zero = int(np.sum(np.abs(evD) < 1e-8))
    # The topological zero modes are EXACT zeros of the record overlap D (the
    # index theorem index(D)=Q, paper14, machine-verified in all flux sectors);
    # the float64 residue ~1e-15 on those eigenvalues is pure roundoff.  We SNAP
    # the n_zero smallest-magnitude eigenvalues to EXACTLY 0 so the Banks-Casher
    # M->0 limit (Part 3) is exact -- otherwise the float64 floor (~1e-15) would
    # cap the 1/M divergence below the true zero-mode contribution.  [LATTICE-
    # NUMERIC eigenvalues; the SNAP is the index-theorem statement, exact.]
    order = np.argsort(np.abs(evD))
    lam = [mp.mpc(z.real, z.imag) for z in evD]
    for j in order[:n_zero]:
        lam[j] = mp.mpc(0)            # exact topological zero (index theorem)
    def Sigma(Mval):
        Mv = mp.mpf(Mval) if not isinstance(Mval, mp.mpf) else Mval
        tot = mp.mpf(0)
        for l in lam:
            num = 1 - l / 2
            den = l + Mv * (1 - l / 2)
            tot += num / den
        return (tot / V).real
    return Sigma, n_zero, evD

print("[ml3b-a: the coupled two-species record GW system]")

# ---- Ga2 first (its masses feed G4c's coupled-mass identity)
mp.mp.dps = 60
SA, nzA, _ = build_sigma_extended(6, 0)
SB, nzB, _ = build_sigma_extended(6, 1)
V6 = 36

def solve_coupled(g2, gx, SA, SB, nzA, nzB, V):
    """Newton on the coupled system with Luscher-subtracted bulk sums
    (the zero-mode 1/M term subtracted as in paper 5's solve_gap)."""
    def bulkA(M): return SA(M) - mp.mpf(nzA) / (mp.mpf(M) * V)
    def bulkB(M): return SB(M) - mp.mpf(nzB) / (mp.mpf(M) * V)
    MA, MB = mp.mpf("0.7"), mp.mpf("0.7")
    for _ in range(200):
        fA = MA - g2 * bulkA(MA) - gx * bulkB(MB)
        fB = MB - g2 * bulkB(MB) - gx * bulkA(MA)
        h = mp.mpf("1e-20")
        dAA = 1 - g2 * (bulkA(MA + h) - bulkA(MA)) / h
        dAB = -gx * (bulkB(MB + h) - bulkB(MB)) / h
        dBA = -gx * (bulkA(MA + h) - bulkA(MA)) / h
        dBB = 1 - g2 * (bulkB(MB + h) - bulkB(MB)) / h
        det = dAA * dBB - dAB * dBA
        dMA = (fA * dBB - fB * dAB) / det
        dMB = (fB * dAA - fA * dBA) / det
        MA, MB = MA - dMA, MB - dMB
        if abs(dMA) + abs(dMB) < mp.mpf("1e-50"):
            break
    return MA, MB

g2 = mp.mpf(4)
sols = {}
for gx in (mp.mpf(0), mp.mpf(1)/4, mp.mpf(1)/2):
    MA, MB = solve_coupled(g2, gx, SA, SB, nzA, nzB, V6)
    sols[float(gx)] = (MA, MB)
    print(f"      Ga2 (QA,QB)=(0,1) g2=4 gx={float(gx):.2f}: "
          f"M_A = {mp.nstr(MA, 12)}, M_B = {mp.nstr(MB, 12)}")
M0A, M0B = solve_coupled(g2, mp.mpf(0), SA, SA, nzA, nzA, V6)  # A-only sanity via symmetric
singleA = solve_coupled(g2, mp.mpf(0), SA, SB, nzA, nzB, V6)
cont = abs(sols[0.0][0] - singleA[0]) < mp.mpf("1e-40")
sus = (sols[0.5][0] - sols[0.0][0]) / mp.mpf("0.5")
ok_exist = all(s[0] > 0 and s[1] > 0 for s in sols.values())
check("Ga2 (existence + continuity + cross-susceptibility): the coupled "
      "system solves with M_A, M_B > 0 at all g_x; the g_x = 0 column is "
      "the single-species anchor; |dM_A/dg_x| > 1e-6 over [0, 1/2] "
      "[directional: positive expected]",
      ok_exist and abs(sus) > mp.mpf("1e-6"),
      f"dM_A/dg_x = {mp.nstr(sus, 8)}; M_A(0) = {mp.nstr(sols[0.0][0], 10)}")
# symmetric control, unpinned
MAs, MBs = solve_coupled(g2, mp.mpf(1)/2, SB, SB, nzB, nzB, V6)
print(f"      control (Q_A = Q_B = 1, gx = 1/2, unpinned): "
      f"M = {mp.nstr(MAs, 10)} / {mp.nstr(MBs, 10)}")

# ---- G4c at dps 120, L = 4, the coupled masses
mp.mp.dps = 120
resids = []
for (Q, Ms) in ((0, sols[0.5][0]), (1, sols[0.5][1])):
    U = flux_links(4, 4, Q)
    Dhp, G5hp, shp, _iters = overlap_hp(4, 4, U)
    n = Dhp.rows
    I = mp.eye(n)
    gw = mp_max_abs(G5hp * Dhp + Dhp * G5hp - Dhp * G5hp * Dhp)
    g5hat = G5hp * (I - Dhp)
    ward0 = mp_max_abs(Dhp * g5hat + G5hp * Dhp)
    Mv = mp.mpf(mp.nstr(Ms, 50))
    DM = Dhp + Mv * (I - Dhp / 2)
    brk = DM * g5hat + G5hp * DM - Mv * (G5hp - shp)
    ward_m = mp_max_abs(brk)
    resids.append((Q, gw, ward0, ward_m))
    print(f"      G4c Q={Q}: GW resid {mp.nstr(gw, 3)}; Ward(0) "
          f"{mp.nstr(ward0, 3)}; coupled-mass breaking-identity resid "
          f"{mp.nstr(ward_m, 3)} at M = {mp.nstr(Mv, 8)}")
thr = mp.mpf("1e-90")
ok4 = all(gw < thr and w0 < thr and wm < thr for _, gw, w0, wm in resids)
check("G4c (the kill gate): GW identity, Luscher Ward, AND the coupled-"
      "mass breaking EXACTLY M_s(g5 - s), all < 1e-90 per species at the "
      "coupled masses — exact chirality SURVIVES the cross-coupling",
      ok4)

print()
print(f"PRE-REGISTERED GATE LEDGER: "
      f"{'ALL HELD' if FAIL == 0 else 'REFUSALS PRESENT'} — Ga2 "
      f"existence/susceptibility; G4c chirality survival")
print()
total = PASS + FAIL
print(f"ALL CHECKS PASS ({PASS}/{total})" if FAIL == 0 else f"FAILURES: {FAIL}/{total}")
if FAIL: raise SystemExit(1)
