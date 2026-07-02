"""Analyze scan results: group orientations by defect distance |M| to the
delta family (= Hamming distance of tau to nearest character, first-order RM
decoding via FWHT), and check the exact depth/defect identity

    2 sum_{a in M(s)} h_a = Dbar + sum_a h_a - log(1/X(s))   for every s.
"""
import numpy as np

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
        f = W[1:].T @ l
        f -= f.max()
        w = np.exp(f); p = w / w.sum()
        x = W[1:] @ p
        barrier = np.exp(-sigma * l)
        grad = x - sigma * barrier
        Wc = W[1:] * np.sqrt(p)[None, :]
        H = Wc @ Wc.T - np.outer(x, x) + np.diag(barrier)
        step = np.linalg.solve(H, grad)
        g0 = Gval(l); t = 1.0
        while t > 1e-8 and Gval(l - t * step) > g0 + 1e-15:
            t /= 2
        l = l - t * step
        if np.abs(grad).max() < tol:
            break
    f = W[1:].T @ l; f -= f.max()
    w = np.exp(f); p = w / w.sum()
    return l, W[1:] @ p, p

def defect_dist(idx, n, W):
    """min over s* of |{a: sigma_a != -chi_a(s*)}| and the argmin s*."""
    N = 1 << n
    sigma = np.array([1.0 if (idx >> k) & 1 else -1.0 for k in range(N - 1)])
    best, bs = N, -1
    for s in range(N):
        d = int(np.sum(sigma != -W[1:, s]))
        if d < best:
            best, bs = d, s
    return best, bs

def main(n):
    N = 1 << n
    W = walsh_matrix(n)
    dat = np.load(f"scan_n{n}.npy")   # rows sorted by D: idx, D, Dbar, chi2, sumDL, R2, minX
    print(f"n={n}: {len(dat)} orientations")
    # defect distance for every orientation
    dists = np.zeros(len(dat), dtype=int)
    for i, row in enumerate(dat):
        dists[i], _ = defect_dist(int(row[0]), n, W)
    Dvals = dat[:, 1]
    print("per-defect-class stats (|M| : count, min D, argmin idx, max D):")
    for m in range(0, dists.max() + 1):
        sel = dists == m
        if not sel.any():
            continue
        Dm = Dvals[sel]
        am = dat[sel][np.argmin(Dm), 0]
        print(f"  |M|={m:2d}: count={sel.sum():6d}  minD={Dm.min():.9f} (idx {int(am)})  maxD={Dm.max():.9f}")
    # global runner-up
    nd = dat[dists > 0]
    ndist = dists[dists > 0]
    j = np.argmin(nd[:, 1])
    print(f"\nrunner-up: idx={int(nd[j,0])}, D={nd[j,1]:.9f}, |M|={ndist[j]}, chi2={nd[j,3]:.6f}, minX={nd[j,6]:.6f}")
    # min-chi2 non-delta
    j2 = np.argmin(nd[:, 3])
    print(f"min-chi2 non-delta: idx={int(nd[j2,0])}, chi2={nd[j2,3]:.9f}, D={nd[j2,1]:.9f}, |M|={ndist[j2]}")

    # detailed look at runner-up and the |M|=1 representative
    for label, idx in [("runner-up", int(nd[j, 0]))]:
        sigma = np.array([1.0 if (idx >> k) & 1 else -1.0 for k in range(N - 1)])
        l, x, p = solve_seal(sigma, W)
        X = N * p
        u = np.abs(x); h = -np.log(u)
        Dbar = float(-np.mean(np.log(X)))
        print(f"\n[{label}] idx={idx}")
        print(f"  u values (sorted): {np.sort(u)}")
        print(f"  h values (sorted): {np.sort(h)}")
        print(f"  X values (sorted): {np.sort(X)}")
        # identity check at min point
        s0 = int(np.argmin(X))
        t = sigma * W[1:, s0]
        M = t > 0
        lhs = 2 * h[M].sum()
        rhs = Dbar + h.sum() - np.log(1.0 / X[s0])
        print(f"  identity at argmin X: 2*sum_M h = {lhs:.9f} vs Dbar+sum h-log(1/minX) = {rhs:.9f}")
    # |M|=1 class representative if exists
    sel1 = np.where(dists == 1)[0]
    if len(sel1):
        idx = int(dat[sel1[np.argmin(dat[sel1, 1])], 0])
        sigma = np.array([1.0 if (idx >> k) & 1 else -1.0 for k in range(N - 1)])
        l, x, p = solve_seal(sigma, W)
        X = N * p
        u = np.abs(x); h = -np.log(u)
        print(f"\n[|M|=1 best] idx={idx}, D={dat[sel1[np.argmin(dat[sel1,1])],1]:.9f}")
        print(f"  u levels: {sorted(set(np.round(u,9)))}")
        print(f"  X levels: {sorted(set(np.round(X,9)))}")

if __name__ == "__main__":
    import sys
    for n in [int(t) for t in (sys.argv[1:] or ["3", "4"])]:
        main(n)
        print("=" * 80)
