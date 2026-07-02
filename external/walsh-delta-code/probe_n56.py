"""Probe the D-landscape minimum over non-delta orientations for n=5,6.

Can't enumerate 2^31 / 2^63 orientations. Strategy:
 - seeds: all 1- and 2-defect flips of the target delta; subspace-structured
   defect sets (M = W\{0} or a coset for subgroups W); the n=4 runner-up
   pattern lifted; random sign patterns.
 - steepest-descent local search in Hamming space: flip the single sigma_a
   that lowers D most, until local minimum; reject delta orbit members.
"""
import numpy as np
import itertools, sys

def walsh_matrix(n):
    N = 1 << n
    pc = np.zeros((N, N), dtype=np.int64)
    for a in range(N):
        pc[a] = [bin(a & s).count("1") for s in range(N)]
    return np.where(pc % 2 == 0, 1.0, -1.0)

def solve_seal(sigma, W, l0=None, tol=1e-12, maxit=200):
    N = W.shape[0]
    l = np.zeros(N - 1) if l0 is None else l0.copy()
    def Gval(lv):
        f = W[1:].T @ lv
        m = f.max()
        return m + np.log(np.mean(np.exp(f - m))) + np.exp(-sigma * lv).sum()
    for it in range(maxit):
        f = W[1:].T @ l
        f -= f.max()
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

def D_of(sigma, W, l0=None):
    l, x, p = solve_seal(sigma, W, l0)
    N = W.shape[0]
    X = N * p
    D = float(np.sum(p * np.log(np.maximum(X, 1e-300))))
    return D, l, x, p

def is_delta(sigma, W):
    N = W.shape[0]
    for s in range(N):
        if np.all(sigma == -W[1:, s]):
            return True
    return False

def local_search(sigma0, W, max_steps=60):
    sigma = sigma0.copy()
    D, l, _, _ = D_of(sigma, W)
    for step in range(max_steps):
        best = (D, -1)
        for a in range(len(sigma)):
            sig2 = sigma.copy(); sig2[a] *= -1
            if is_delta(sig2, W):
                continue
            D2, _, _, _ = D_of(sig2, W, l)
            if D2 < best[0] - 1e-12:
                best = (D2, a)
        if best[1] < 0:
            break
        sigma[best[1]] *= -1
        D, l, _, _ = D_of(sigma, W, l)
    return sigma, D

def main(n, n_random=200, seed=7):
    rng = np.random.default_rng(seed)
    N = 1 << n
    W = walsh_matrix(n)
    Mn = N - 1
    delta = -W[1:, 0]   # target-gauge delta: sigma_a = -1
    seeds = []
    # 1- and 2-defect flips
    for a in range(Mn):
        s = delta.copy(); s[a] *= -1; seeds.append(("def1", s))
    for a, b in itertools.combinations(range(min(Mn, 31)), 2):
        s = delta.copy(); s[a] *= -1; s[b] *= -1; seeds.append(("def2", s))
    # subspace defect sets: M = W0 \ {0} for subgroups spanned by k basis masks
    base_masks = [1 << i for i in range(n)]
    for k in range(1, n + 1):
        for combo in itertools.combinations(base_masks, k):
            span = {0}
            for m in combo:
                span |= {x ^ m for x in span}
            s = delta.copy()
            for a in span - {0}:
                s[a - 1] *= -1
            seeds.append((f"span{k}", s))
    # affine hyperplane defect sets: M = {a: chi_a(t)=-1}
    for t in range(1, N):
        s = delta.copy()
        for a in range(1, N):
            if W[a, t] < 0:
                s[a - 1] *= -1
        seeds.append(("hyp", s))   # note: this IS the translated delta (skip via is_delta)
    # random
    for _ in range(n_random):
        s = np.where(rng.random(Mn) < 0.5, 1.0, -1.0)
        seeds.append(("rand", s))

    best = (1e9, None, None)
    results = []
    for tag, s in seeds:
        if is_delta(s, W):
            continue
        D0, _, _, _ = D_of(s, W)
        s2, D2 = local_search(s, W)
        results.append((tag, D0, D2))
        if D2 < best[0]:
            best = (D2, s2.copy(), tag)
            print(f"  new best: D={D2:.9f} from seed {tag} (seed D={D0:.6f})")
    # delta reference
    coeffs = np.zeros(N + 2)
    coeffs[0] = -1.0; coeffs[1] = N - 1.0; coeffs[N] = 1.0; coeffs[N + 1] = 1.0
    roots = np.roots(coeffs[::-1])
    ustar = min(r.real for r in roots if abs(r.imag) < 1e-12 and 0 < r.real < 1.0/(N-1)+1e-9)
    A = 1 - (N - 1) * ustar; Bv = 1 + ustar
    Dd = (A * np.log(A) + (N - 1) * Bv * np.log(Bv)) / N
    print(f"n={n}: D_delta={Dd:.9f}, best non-delta found D={best[0]:.9f}, ratio={best[0]/Dd:.3f}")
    # structure of best
    sigma = best[1]
    D, l, x, p = D_of(sigma, W)
    X = N * p
    u = np.abs(x); h = -np.log(u)
    # defect distance
    dd = min(int(np.sum(sigma != -W[1:, s])) for s in range(N))
    print(f"  |M|(best)={dd}, minX={X.min():.3e}, u-levels={sorted(set(np.round(u,6)))[:6]}")
    print(f"  X-levels={sorted(set(np.round(X,6)))[:8]}")
    return best

if __name__ == "__main__":
    for n in [int(t) for t in (sys.argv[1:] or ["5"])]:
        main(n)
        print("=" * 90)
