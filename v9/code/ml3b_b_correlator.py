#!/usr/bin/env python3
"""
ml3b_b_correlator.py — v9 round 16: ML3B STEP (b) — the connected
cross-species correlator (note-ml3b-b; pins committed at 4206520 BEFORE
this receipt existed).

C_AB(x,y) = g_x * sum_z Pi_A(x,z) Pi_B(z,y);
Pi_s(u,v) = -Tr_spinor[S_s(u,v) S_s(v,u)];  S_s = (D + M_s(1 - D/2))^-1
at the step-(a) coupled masses (L = 6, sectors (0,1), g^2 = 4;
zero-mode-subtracted-both-channels convention). Leading connected order;
float64 (decay-shape measurement); the operator-level chirality kill is
NOT live at this order (disclosed — no survival rhetoric).

PINNED (note-ml3b-b SS2): Gb1 the LIVE kill — binned |C| strictly
decreasing over d in {0,1},{2,3},{4-6} AND far < 0.5x near AND near >
1e-12, at g_x = 1/2. Gb2 [directional]: fitted decay rate within 3x of
2*min(M_A, M_B). Gb3: chi-hat (seal window w = 1) nonzero and finite
(sign+magnitude printed; NO physical-chi_AB claim). Gb4 [directional,
printed]: the g_x = 1/4 vs 1/2 ratio in (1, 2).
Exit 1 by design on refusal.
"""
import numpy as np
import mpmath as mp

mp.mp.dps = 60
PASS = FAIL = 0
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

print("[ml3b-b: the connected cross-species correlator]")
Lx = 6; V = Lx * Lx
SAf, nzA, _ = build_sigma_extended(Lx, 0)
SBf, nzB, _ = build_sigma_extended(Lx, 1)

def corr_at(gx):
    MA, MB = solve_coupled(mp.mpf(4), mp.mpf(gx), SAf, SBf, nzA, nzB, V)
    out = {}
    for tag, Q, Ms in (("A", 0, MA), ("B", 1, MB)):
        U = flux_links(Lx, Lx, Q)
        D, G5, s = overlap_float(Lx, Lx, U)
        Mf = float(Ms)
        S = np.linalg.inv(D + Mf * (np.eye(2 * V) - D / 2))
        # spinor blocks: index = a*V + u
        Pi = np.zeros((V, V))
        for a in (0, 1):
            for bb in (0, 1):
                Pi -= (S[a*V:(a+1)*V, bb*V:(bb+1)*V]
                       * S[bb*V:(bb+1)*V, a*V:(a+1)*V].T).real
        out[tag] = Pi
    C = float(gx) * (out["A"] @ out["B"])
    return C, float(MA), float(MB)

def dists(Lx):
    xs = np.arange(Lx)
    dx = np.minimum(np.abs(xs[:, None] - xs[None, :]),
                    Lx - np.abs(xs[:, None] - xs[None, :]))
    sites = [(x, y) for x in range(Lx) for y in range(Lx)]
    Dm = np.zeros((len(sites), len(sites)), dtype=int)
    for i, (x1, y1) in enumerate(sites):
        for j, (x2, y2) in enumerate(sites):
            Dm[i, j] = dx[x1, x2] + dx[y1, y2]
    return Dm

Dm = dists(Lx)
C5, MA, MB = corr_at(0.5)
absC = np.abs(C5)
bins = [(0, 1), (2, 3), (4, 6)]
means = []
for lo, hi in bins:
    sel = (Dm >= lo) & (Dm <= hi)
    means.append(float(absC[sel].mean()))
print(f"      masses at g_x = 1/2: M_A = {MA:.6f}, M_B = {MB:.6f}")
print("      binned |C_AB|: " + "  ".join(
    f"d={lo}-{hi}: {m:.3e}" for (lo, hi), m in zip(bins, means)))
gb1 = (means[0] > means[1] > means[2] and means[2] < 0.5 * means[0]
       and means[0] > 1e-12)
check("Gb1 (existence + decay — THE LIVE KILL): binned |C_AB| strictly "
      "decreasing, far < 0.5x near, near > 1e-12 at g_x = 1/2",
      gb1, f"{means[0]:.3e} > {means[1]:.3e} > {means[2]:.3e}")

# Gb2: fitted rate vs 2*min(M)
ds = np.array([0.5, 2.5, 5.0])
lm = np.log(np.maximum(means, 1e-300))
rate = -(lm[2] - lm[0]) / (ds[2] - ds[0])
target = 2 * min(MA, MB)
check("Gb2 (mass-scale consistency) [directional]: the fitted decay rate "
      "within 3x of 2*min(M_A, M_B)",
      target / 3 <= rate <= target * 3,
      f"rate {rate:.3f} vs 2*minM {target:.3f}")

# Gb3: the derived chi-hat (seal window w = 1)
sel1 = Dm <= 1
chi_hat = float(C5[sel1].mean())
check("Gb3 (the derived chi readout): chi-hat (w = 1 window mean) nonzero "
      "and finite — the campaign's first DERIVED two-party coupling "
      "number; magnitude interpretation withheld (SS4 conventions)",
      np.isfinite(chi_hat) and abs(chi_hat) > 1e-15,
      f"chi_hat = {chi_hat:+.6e}")

# Gb4: g_x scaling [directional, printed]
C25, _, _ = corr_at(0.25)
r = float(np.abs(C5)[sel1].mean() / max(np.abs(C25)[sel1].mean(), 1e-300))
print(f"      Gb4 [directional, printed]: near-window |C| ratio "
      f"(g_x 1/2 vs 1/4) = {r:.3f} (expected in (1, 2))")

print()
print(f"PRE-REGISTERED GATE LEDGER: "
      f"{'ALL HELD' if FAIL == 0 else 'REFUSALS PRESENT'} — Gb1 kill; "
      f"Gb2 rate; Gb3 chi-hat; Gb4 printed")
print()
total = PASS + FAIL
print(f"ALL CHECKS PASS ({PASS}/{total})" if FAIL == 0 else f"FAILURES: {FAIL}/{total}")
if FAIL: raise SystemExit(1)
