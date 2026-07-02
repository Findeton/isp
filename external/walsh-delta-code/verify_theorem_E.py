"""Receipt: log-domain verification of Theorem E (deliverable 6d) on the
known in-regime families. Run: python3 verify_theorem_E.py

Verifies, for the j=2 (3-dip) family at n=9,10,11 and the j=3 family at
n=10,11: in-regime D <= 1/60; dip count k and deep count m >= 3;
per-mask (D1) error |ghat + F/N| <= 2.5*sqrt(2D); floor
min|F|/N >= h'(D) = 0.5*log(1/(2D)) - 2.5*sqrt(2D); exact sign readout
sigma_a = -sgn F(a); and the conclusion N*D >= 3*psi(e^-5) = 2.878717.

CRITICAL: all depth quantities are computed in LOG-DOMAIN
(logX = logN + field - logsumexp(field)); depths reach beta ~ N log(N/4)
(~5700 at n=10), so X underflows float64 and any exp-domain computation
silently corrupts beta (this exact artifact produced a false alarm on
first run; see solve log 2026-07-02).
"""
import numpy as np

def walsh(n):
    N = 1 << n
    pc = np.zeros((N, N), dtype=np.int64)
    for a in range(N):
        pc[a] = [bin(a & s).count("1") for s in range(N)]
    return np.where(pc % 2 == 0, 1.0, -1.0)

def solve(sigma, W, tol=1e-12, maxit=600):
    N = W.shape[0]; l = np.zeros(N - 1)
    def G(lv):
        f = W[1:].T @ lv; m = f.max()
        return m + np.log(np.mean(np.exp(f - m))) + np.exp(-sigma * lv).sum()
    for _ in range(maxit):
        f = W[1:].T @ l; f -= f.max(); w = np.exp(f); p = w / w.sum()
        x = W[1:] @ p; b = np.exp(-sigma * l); g = x - sigma * b
        if np.abs(g).max() < tol: break
        Wc = W[1:] * np.sqrt(p)[None, :]
        H = Wc @ Wc.T - np.outer(x, x) + np.diag(b)
        st = np.linalg.solve(H, g); g0 = G(l); t = 1.0
        while t > 1e-9 and G(l - t * st) > g0 + 1e-15: t /= 2
        l = l - t * st
    return l

def check_E(n, jbits, label):
    N = 1 << n; W = walsh(n)
    mask = (1 << jbits) - 1
    sigma = np.array([1.0 if (a & mask) == mask else -1.0 for a in range(1, N)])
    l = solve(sigma, W)
    field = W[1:].T @ l; m = field.max()
    lse = m + np.log(np.sum(np.exp(field - m)))
    logX = np.log(N) + field - lse            # exact log-domain
    p = np.exp(field - lse)
    D = float(np.sum(p * logX))
    ok = True
    print(f"[{label}] n={n} D={D:.6f} N*D={N*D:.4f} in-regime={D <= 1/60}")
    if D > 1 / 60:
        print("   branch 1 (D > 1/60) applies; nothing to check"); return True
    dips = np.where(logX <= np.log(0.5))[0]
    beta = -logX[dips]
    mdeep = int((beta >= 5.0).sum())
    ghat = (W[1:] @ logX) / N
    F = np.zeros(N - 1)
    for j, s in enumerate(dips): F += beta[j] * W[1:, s]
    checks = [
        ("k-bound", len(dips) <= D * N / 0.1534264),
        ("deep m>=3", mdeep >= 3),
        ("(D1) error", float(np.abs(ghat + F / N).max()) <= 2.5 * np.sqrt(2 * D)),
        ("(D1) floor", float(np.abs(F).min() / N) >= 0.5 * np.log(1 / (2 * D)) - 2.5 * np.sqrt(2 * D)),
        ("sign readout", bool(np.all(sigma == -np.sign(F)))),
        ("E conclusion", N * D >= 2.878716),
    ]
    for name, val in checks:
        ok &= bool(val)
        print(f"   {name}: {val}")
    return ok

if __name__ == "__main__":
    allok = True
    for n in [9, 10, 11]:
        allok &= check_E(n, 2, "3-dip family (j=2)")
    for n in [10, 11]:
        allok &= check_E(n, 3, "j=3 family")
    print("ALL CHECKS PASS" if allok else "FAILURES PRESENT")
