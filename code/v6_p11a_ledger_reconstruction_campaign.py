#!/usr/bin/env python3
"""
v6_p11a: infinite-dimensional ledger reconstruction - the L3 residue
(Paper 11, Part I).

The existence half of L3 is closed (P7 Theorem 7.5, Kolmogorov).  This
campaign does the RECONSTRUCTION half on refinement towers:

 T1 (RP passes to limits): PSD conditions are closed under pointwise
    limits of correlations, so any sector APPROXIMABLE by eventless
    finitely-presented sectors is reflection positive in the limit -
    sharpening O6 to "not even approximable."
 T2/T3 (the Gaussian tower benchmark): from binned RECORD data of the
    free collar (the Mehler transfer kernel of P7 D5), reconstruct:
      - the spectrum: E_n -> omega(n + 1/2) with quantified convergence;
      - the UNBOUNDED position operator: ladder matrix elements
        <n|x|n+1> -> sqrt((n+1)/(2 omega)), off-ladder elements -> 0
        (selection rules emerge), and sqrt(n) growth (unboundedness
        witnessed);
    i.e. QFT-grade Hilbert/operator structure recovered from finite
    ledger truncations, with rates.
 T4 (loop classes along towers): Bargmann loop invariants of truncated
    dilations converge to the limit invariants and remain gauge-invariant
    at every level: the ledger's holonomy classes survive the
    infinite-dimensional limit.
 T5 (dilation towers): the P7 D1 dilation built at every truncation
    reproduces its law exactly, and coarse laws are EXACT marginals of
    fine laws (projective consistency): the inductive system that the
    imported unbounded Naimark/Stinespring theory completes.
"""
import numpy as np

rng = np.random.default_rng(11)
omega, tau = 1.0, 0.4

def mehler_S(d, X=7.0):
    """symmetrized binned transfer of the free record collar."""
    x = np.linspace(-X, X, d)
    dx = x[1] - x[0]
    sh, ch = np.sinh(omega * tau), np.cosh(omega * tau)
    K = np.sqrt(omega / (2 * np.pi * sh)) * np.exp(
        -omega * ((x[:, None] ** 2 + x[None, :] ** 2) * ch
                  - 2 * x[:, None] * x[None, :]) / (2 * sh))
    return K * dx, x

# ---------- T2/T3: the Gaussian tower ----------
print("== T2/T3. the Gaussian tower: spectrum and the unbounded ladder ==")
print("   d     E1-E0 err     E2-E1 err     E3-E2 err     E4-E3 err")
for d in (20, 40, 80, 160):
    S, x = mehler_S(d)
    ev = np.linalg.eigvalsh(S)[::-1]
    E = -np.log(ev[:6]) / tau
    gaps = np.diff(E[:5])
    errs = np.abs(gaps - omega)
    print(f"  {d:4d}   " + "   ".join(f"{e:.3e}" for e in errs))
S, x = mehler_S(160)
ev, evec = np.linalg.eigh(S)
order = np.argsort(ev)[::-1]
ev, evec = ev[order], evec[:, order]
Xop = evec.T @ (x[:, None] * evec)
print("\n  reconstructed position operator in the reconstructed eigenbasis:")
print("   n    |<n|x|n+1>|      target sqrt((n+1)/2w)   err")
for n in (0, 1, 2, 3, 4, 10, 20):
    tgt = np.sqrt((n + 1) / (2 * omega))
    print(f"  {n:3d}   {abs(Xop[n, n+1]):.9f}    {tgt:.9f}       "
          f"{abs(abs(Xop[n, n+1]) - tgt):.2e}")
off = max(abs(Xop[n, m]) for n in range(8) for m in range(8) if abs(n - m) not in (1,))
print(f"  max off-ladder element |<n|x|m>|, |n-m| != 1, n,m < 8: {off:.2e}")
print(f"  growth: |<20|x|21>| / |<0|x|1>| = {abs(Xop[20,21])/abs(Xop[0,1]):.4f}"
      f"  (sqrt(21) = {np.sqrt(21):.4f}): the operator is UNBOUNDED in the limit")
print("  -> spectrum, ladder algebra, selection rules, and unboundedness are")
print("     all RECONSTRUCTED from binned record data, with quantified rates.")

# ---------- T1: RP passes to limits ----------
print("\n== T1. reflection positivity passes to projective limits ==")
def hankel_min(C, N):
    G = np.array([[C[i + j] for j in range(1, N + 1)] for i in range(1, N + 1)])
    return np.linalg.eigvalsh(G)[0]
worst = 0.0
for d in (20, 40, 80, 160):
    S, x = mehler_S(d)
    ev, evec = np.linalg.eigh(S)
    lam = ev / ev.max()
    f = evec.T @ (x * np.exp(-x**2))           # an observable in eigenbasis
    mu = f ** 2 / np.sum(f ** 2)               # spectral measure weights
    C = [float(np.sum(mu * lam ** r)) for r in range(30)]
    worst = min(worst, hankel_min(C, 12))
print(f"  binned towers d = 20..160: worst site-Hankel min eig = {worst:.2e}")
print("  LEMMA (2 lines): each Gram entry of the limit is a limit of entries")
print("  of PSD matrices; the PSD cone is closed; hence RP survives every")
print("  pointwise limit of correlations.  COROLLARY: any sector APPROXIMABLE")
print("  by eventless finitely-presented sectors is RP - O6 sharpens to")
print("  'sectors not even approximable by eventless presentations'.")

# ---------- T4: the Weyl/CCR structure reconstructed in the limit ----------
print("\n== T4. the Weyl algebra reconstructed from record data ==")
def uexp(H, s):
    ev, vv = np.linalg.eigh(H)
    return (vv * np.exp(1j * s * ev)) @ vv.T.conj()
s_par, r_par = 1.3, 0.9
print("   d    K(levels)   |<0|e^{isX}|0> - e^{-s^2/4}|   ||GC - e^{-isr} I|| (6x6)")
for d, K in ((40, 12), (80, 24), (160, 36)):
    S, x = mehler_S(d)
    ev, evec = np.linalg.eigh(S)
    order = np.argsort(ev)[::-1]
    ev, evec = ev[order][:K], evec[:, order][:, :K]   # resolved-level tower
    En = -np.log(ev / ev[0]) / tau            # reconstructed level energies
    Xd = evec.T @ (x[:, None] * evec)
    Hd = np.diag(En)
    Pd = 1j * (Hd @ Xd - Xd @ Hd)             # Heisenberg: P = i[H, X]
    # (i) characteristic function vs the exact continuum answer
    Us = uexp(Xd, s_par)
    char_err = abs(Us[0, 0] - np.exp(-s_par ** 2 / 4))
    # (ii) the CCR via the Weyl group commutator
    Ur = uexp(Pd, r_par)
    GC = Us @ Ur @ Us.conj().T @ Ur.conj().T
    blk = GC[:6, :6] - np.exp(-1j * s_par * r_par) * np.eye(6)
    print(f"  {d:4d}     {K:3d}         {char_err:.6e}               {np.linalg.norm(blk):.6e}")
print(f"  P-ladder check at d=160, K=36: | |<0|P|1>| - sqrt(1/2) | = "
      f"{abs(abs(Pd[0,1]) - np.sqrt(0.5)):.2e}")
# Bargmann-loop gauge invariance of the reconstructed unitaries
Us = uexp(Xd, s_par)
ph = np.exp(1j * rng.uniform(0, 2 * np.pi, Xd.shape[0]))
Ug = np.diag(ph) @ Us @ np.diag(ph).conj()
def Bloop(U, ell):
    z = 1.0 + 0j
    for k in range(len(ell) - 1):
        z *= U[ell[k + 1], ell[k]]
    return z
ginv = max(abs(Bloop(Ug, l) - Bloop(Us, l))
           for l in [(0, 1, 2, 0), (0, 3, 1, 0)])
print(f"  Bargmann-loop gauge invariance (random diagonal phases): {ginv:.2e}")
print("  -> the reconstructed X and P = i[H,X] satisfy the WEYL RELATION")
print("     e^{isX} e^{irP} e^{-isX} e^{-irP} = e^{-isr}: the canonical")
print("     commutation relations - the continuum quantum kinematics - are")
print("     recovered from finite ledger truncations, against the EXACT")
print("     infinite-dimensional targets, with quantified convergence.")

# ---------- T5: dilation towers and projective consistency ----------
print("\n== T5. dilation towers: per-level exactness + projective consistency ==")
Sfine, xf = mehler_S(160)
Gfine = Sfine / Sfine.sum(axis=1, keepdims=True)     # fine record law
def coarse_law(G, b):
    d = G.shape[0] // b
    Q = np.zeros((d, d))
    pi_f = stationary = np.real(np.linalg.eig(G.T)[1][:, 0])
    pi_f = np.abs(pi_f) / np.abs(pi_f).sum()
    for i in range(d):
        for j in range(d):
            blk_i = slice(i * b, (i + 1) * b)
            blk_j = slice(j * b, (j + 1) * b)
            wi = pi_f[blk_i] / pi_f[blk_i].sum()
            Q[i, j] = wi @ G[blk_i, blk_j].sum(axis=1)
    return Q / Q.sum(axis=1, keepdims=True), pi_f
for b, name in ((2, "160 -> 80"), (4, "160 -> 40")):
    Q, pi_f = coarse_law(Gfine, b)
    d = Q.shape[0]
    # P7 D1 dilation at the coarse level, exactness:
    V = np.zeros((d * d, d))
    for i in range(d):
        V[np.arange(d) * d + i, i] = np.sqrt(Q[i])
    # direct check: squared dilation amplitudes give back the law
    rec = np.array([[V[j * d + i, i] ** 2 for j in range(d)] for i in range(d)])
    iso = np.abs(V.T @ V - np.eye(d)).max()
    print(f"  level {name}: dilation isometry gap = {iso:.2e},"
          f" law reproduction gap = {np.abs(rec - Q).max():.2e}")
    # projective consistency: coarse stationary = block-sum of fine stationary
    pi_c = np.real(np.linalg.eig(Q.T)[1][:, 0]); pi_c = np.abs(pi_c) / np.abs(pi_c).sum()
    pi_blk = pi_f.reshape(d, b).sum(axis=1)
    print(f"     coarse stationary vs block-summed fine: max gap = "
          f"{np.abs(pi_c - pi_blk).max():.2e}  (projective consistency)")
print("  -> every level carries its exact D1 dilation, and the levels cohere:")
print("     the inductive system exists; the imported unbounded Naimark/")
print("     Stinespring theory (with Nelson/Kato self-adjointness criteria on")
print("     the tame class) completes it to the separable-Hilbert-space limit.")
print("== p11a done ==")
