"""Machine-precision verification of the new exact identities:
  (G)  X(s) = e^{m(s)} / E_U[e^m],  m(s) = 2 sum_{a in M(s)} h_a
  (Phi) D = Phi(law of m) = E[m e^m]/E[e^m] - log E[e^m]
  (DP)  m(s) + m(s') >= 2 H_{s+s'},  H_t = sum_{chi_a(t) = -1} h_a
  (J)   D + Dbar = sum h_a e^{-h_a}
  (B)   w(s) + m(s) = B = sum h + log N + Dbar, all s
Run on a spread of orientations for n = 3, 4, 5.
Also: delta reference values via mpmath (dps=60) for n=2..8.
"""
import numpy as np
from mpmath import mp, mpf, log as mlog, findroot

def walsh_matrix(n):
    N = 1 << n
    pc = np.zeros((N, N), dtype=np.int64)
    for a in range(N):
        pc[a] = [bin(a & s).count("1") for s in range(N)]
    return np.where(pc % 2 == 0, 1.0, -1.0)

def solve_seal(sigma, W, tol=1e-13, maxit=300):
    N = W.shape[0]
    l = np.zeros(N - 1)
    def Gval(lv):
        f = W[1:].T @ lv
        m = f.max()
        return m + np.log(np.mean(np.exp(f - m))) + np.exp(-sigma * lv).sum()
    for it in range(maxit):
        f = W[1:].T @ l; f -= f.max()
        wgt = np.exp(f); p = wgt / wgt.sum()
        x = W[1:] @ p
        barrier = np.exp(-sigma * l)
        grad = x - sigma * barrier
        if np.abs(grad).max() < tol:
            break
        Wc = W[1:] * np.sqrt(p)[None, :]
        H = Wc @ Wc.T - np.outer(x, x) + np.diag(barrier)
        step = np.linalg.solve(H, grad)
        g0 = Gval(l); t = 1.0
        while t > 1e-9 and Gval(l - t * step) > g0 + 1e-15:
            t /= 2
        l = l - t * step
    f = W[1:].T @ l; f -= f.max()
    wgt = np.exp(f); p = wgt / wgt.sum()
    return l, W[1:] @ p, p

def check(n, idx_list, rng):
    N = 1 << n
    W = walsh_matrix(n)
    worst = {}
    for idx in idx_list:
        if isinstance(idx, int):
            sigma = np.array([1.0 if (idx >> k) & 1 else -1.0 for k in range(N - 1)])
        else:
            sigma = idx
        l, x, p = solve_seal(sigma, W)
        X = N * p
        u = np.abs(x); h = -np.log(u)
        D = float(np.sum(p * np.log(X)))
        Dbar = float(-np.mean(np.log(X)))
        # m(s)
        m = np.array([2 * h[(sigma * W[1:, s]) > 0].sum() for s in range(N)])
        Eem = np.mean(np.exp(m - m.max()))
        Xg = np.exp(m - m.max()) / Eem
        e1 = np.abs(Xg - X).max()                                   # (G)
        Phi = float(np.mean(m * np.exp(m - m.max())) / (np.mean(np.exp(m - m.max()))) - (m.max() + np.log(Eem)))
        e2 = abs(Phi - D)                                            # (Phi)
        e3 = abs(D + Dbar - np.sum(h * np.exp(-h)))                  # (J)
        w = np.log(N) - np.log(X)
        B = h.sum() + np.log(N) + Dbar
        e4 = np.abs(w + m - B).max()                                 # (B)
        # (DP): check the inequality and its derivation basis
        Ht = np.array([h[W[1:, t] < 0].sum() for t in range(1, N)])
        viol = 0
        for s in range(N):
            for t in range(1, N):
                if m[s] + m[s ^ t] < 2 * Ht[t - 1] - 1e-9:
                    viol += 1
        for k, v in [("G", e1), ("Phi", e2), ("J", e3), ("B", e4), ("DPviol", viol)]:
            worst[k] = max(worst.get(k, 0), v)
    print(f"n={n}: worst errors: " + ", ".join(f"{k}={v:.2e}" if k != "DPviol" else f"{k}={v}" for k, v in worst.items()))

def delta_refs():
    mp.dps = 60
    print("\ndelta references (mpmath dps=60):")
    for n in range(2, 9):
        N = 1 << n
        f = lambda u: u**(N + 1) + u**N + (N - 1) * u - 1
        u = findroot(f, mpf(1) / (N - 1))
        A = 1 - (N - 1) * u; Bv = 1 + u
        D = (A * mlog(A) + (N - 1) * Bv * mlog(Bv)) / N
        print(f"  n={n}: u*={mp.nstr(u, 20)}  D_delta={mp.nstr(D, 15)}  1/(N-1)={mp.nstr(mpf(1)/(N-1), 8)}  log(N/(N-1))={mp.nstr(mlog(mpf(N)/(N-1)), 8)}")

if __name__ == "__main__":
    rng = np.random.default_rng(3)
    check(3, [0, 14, 46, 77, 100], rng)
    check(4, [0, 480, 128, 13517, 7174, 31000], rng)
    # n=5: random sigmas
    sig5 = [np.where(rng.random(31) < 0.5, 1.0, -1.0) for _ in range(6)]
    check(5, sig5, rng)
    delta_refs()
