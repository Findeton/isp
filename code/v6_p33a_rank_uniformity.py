#!/usr/bin/env python3
"""
v6_p33a: rank uniformity and the SOT engine (Paper 33, part A).

The corpus' shared boundary is the TAME-SCOPE FRONTIER: theorems
are proved and receipted at finite rank, and 'stated scope' marks
the unproven portability to the full (infinite-rank) record
category.  This campaign structures the frontier instead of
gesturing at it.

 (i)   THE RANK-FREE CATALOG: theorems whose proofs never use the
       rank port verbatim to any rank.  Receipts at d = 8, 16, 32:
       the palindrome factorization stays EXACT, achiral reality
       stays machine-zero, chiral classes stay complex-capable -
       the Achiral Necklace Theorem (and with it the Stieltjes
       structure, the collapse lemma's centrality argument, the
       normal escape) is dimension-blind, as its proof says.
 (ii)  THE SOT ENGINE THEOREM (proved, all ranks including
       infinite): if T is self-adjoint, 0 <= T <= 1, T Omega =
       Omega, then T^n -> P_1 STRONGLY - by the spectral theorem,
       with NO gap and NO rank assumption (t^n -> 1_{t=1} pointwise
       boundedly on [0,1]).  (E-bg)'s clustering engine is
       rank-blind.  Receipts: a near-gapless ledger (second
       eigenvalue 0.9990) clusters slowly but completely; a
       dense-spectrum mock (d = 400, eigenvalues packed against 1)
       clusters despite having no spectral gap to speak of.
 (iii) THE CATALOG, printed: rank-free vs rank-receipted vs
       genuinely limit-bound - the frontier's map.
"""
import numpy as np

rng = np.random.default_rng(330)

# ---------- (i) rank-free receipts ----------
print("== (i) the rank-free catalog: receipts at d = 8, 16, 32 ==")
def word_op(w, A0, A1):
    M = np.eye(A0.shape[0])
    for ch in w:
        M = M @ (A0 if ch == "0" else A1)
    return M
for d in (8, 16, 32):
    G0 = rng.standard_normal((d, d))
    G1 = rng.standard_normal((d, d))
    A0, A1 = G0 @ G0.T, G1 @ G1.T
    # palindrome factorization exact
    B = word_op("00100", A0, A1)
    C = A0 @ A0
    err = np.abs(B - C @ A1 @ C.T).max() / np.abs(B).max()
    # achiral reality
    ev_a = np.linalg.eigvals(word_op("010011", A0, A1))  # achiral?
    # use a known achiral class: 0101 and 001100? verify by canon
    ev_a = np.linalg.eigvals(word_op("0101", A0, A1))
    im_a = np.abs(ev_a.imag).max() / np.abs(ev_a).max()
    # chiral complex-capability (quick climb)
    best = 0.0
    H0, H1 = G0.copy(), G1.copy()
    sz = 0.3
    for k in range(400):
        P0 = H0 + sz * rng.standard_normal((d, d))
        P1 = H1 + sz * rng.standard_normal((d, d))
        ev = np.linalg.eigvals(word_op("00011101",
                                       P0 @ P0.T, P1 @ P1.T))
        v = np.abs(ev.imag).max() / np.abs(ev).max()
        if v > best:
            best, H0, H1 = v, P0, P1
        sz = max(sz * 0.995, 0.05)
    print(f"   d = {d:2d}: palindrome fact. rel-err = {err:.1e};"
          f"  achiral |Im|/rho = {im_a:.1e};"
          f"  chiral capable: {best:.3f}")
print("  -> the ANT chain is dimension-blind, exactly as its proof")
print("     requires: rank-free theorems stay theorems at any rank.")

# ---------- (ii) the SOT engine ----------
print("\n== (ii) the SOT engine: clustering without a gap ==")
# near-gapless ledger: load the slow mode DELIBERATELY
d = 60
lam = np.concatenate([[1.0, 0.9990, 0.9985],
                      rng.uniform(0.1, 0.95, d - 3)])
Q, _ = np.linalg.qr(rng.standard_normal((d, d)))
Om = Q[:, 0]
u = Om + 0.5 * Q[:, 1]          # couples to the 0.9990 mode
w = Om + 0.5 * Q[:, 1]
lim = float((u @ Om) * (Om @ w))
print(f"  near-gapless ledger (2nd eigenvalue 0.9990; probe loads")
print(f"  the slow mode at 0.5):")
for n in (10, 1000, 10000, 100000):
    Tn = Q @ np.diag(lam ** n) @ Q.T
    val = float(u @ Tn @ w)
    print(f"    n = {n:6d}:  <u, T^n w> = {val:.4f}"
          f"   (limit {lim:.4f})")
print("  -> SLOW (the 0.999 mode persists for thousands of steps)")
print("     but COMPLETE: the engine needs no gap, only the")
print("     spectral theorem (t^n -> 1_(t=1) boundedly on [0,1]).")
# dense-spectrum mock
d2 = 400
lam2 = np.concatenate([[1.0], 1 - np.geomspace(1e-5, 0.9, d2 - 1)])
Q2, _ = np.linalg.qr(rng.standard_normal((d2, d2)))
Om2 = Q2[:, 0]
u2 = Q2 @ (rng.standard_normal(d2) * 0.2) + Om2
w2 = Q2 @ (rng.standard_normal(d2) * 0.2) + Om2
num0 = float(u2 @ Q2 @ np.diag(lam2 ** 0) @ Q2.T @ w2)
print(f"  dense-spectrum mock (d = 400, eigenvalues packed against")
print(f"  1 down to 1e-5 gaps):")
for n in (10 ** 3, 10 ** 5, 10 ** 7):
    Tn = Q2 @ np.diag(lam2 ** n) @ Q2.T
    val = float(u2 @ Tn @ w2)
    lim = float((u2 @ Om2) * (Om2 @ w2))
    print(f"    n = 1e{int(np.log10(n))}:  <u, T^n w> ="
          f" {val:.4f}   (limit {lim:.4f})")
print("  -> convergence marches through the packed spectrum: the")
print("     SOT engine theorem in action - T self-adjoint <= 1 with")
print("     T Omega = Omega clusters at ANY rank, including the")
print("     infinite-rank limit this mock imitates.")

# ---------- (iii) the catalog ----------
print("\n== (iii) the frontier map ==")
print("""  RANK-FREE (proofs functorial in rank; port verbatim):
    ANT + reflection-axis lemma; palindrome factorization;
    Stieltjes structure (spectral theorem); the collapse lemma
    (centrality + GNS); the normal escape (G = I algebra); the
    peripheral reduction (per-rank statement + limits); the
    exhaustion of reflection; DR-invisibility.
  RANK-UNIFORM BY THE SOT ENGINE (this paper's theorem):
    (E-bg) clustering; sector convergence T^n -> P_1; the
    background-reaching arguments of P31's (E) chain.
  RANK-RECEIPTED ONLY (searches and walls; no porting claim):
    the validity walls (s ~ 0.2); the NR receipts (d <= 5); the
    band/isolation measurements; the pinch coordinates; tower
    exclusion bounds.
  GENUINELY LIMIT-BOUND (the real frontier, named):
    continuous sector integrals (T-cont, part B); the L3/tame
    reconstruction beyond the tame class; (V); thermodynamic
    limits of the dynamics layer.""")
print("== p33a done ==")
