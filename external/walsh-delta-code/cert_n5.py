"""Certified verification of Global Delta Optimality for n = 5 via the
complete orbit partition produced by orbit_bfs (orbits_n5.txt).

Validity: D(sigma) is invariant under the group action (translations act by
l_a -> l_a * chi_a(t) on the convex problem G_sigma; GL(n,2) acts by mask
relabeling; both are bijections of the orientation set preserving G-values),
so certifying one representative per orbit certifies the whole orbit. The
orbit partition is complete by construction (BFS covers all 2^31 states;
checksum verified by orbit_bfs).

Per representative: float64 Newton warm start -> 3 mpmath (dps=40) Newton
steps -> certified residual/Kantorovich/Lipschitz exactly as in cert_scan.
"""
import numpy as np
from mpmath import mp, mpf, exp as mexp, log as mlog, sqrt as msqrt, matrix, lu_solve

def walsh_matrix(n):
    N = 1 << n
    pc = np.zeros((N, N), dtype=np.int64)
    for a in range(N):
        pc[a] = [bin(a & s).count("1") for s in range(N)]
    return np.where(pc % 2 == 0, 1.0, -1.0)

def solve_seal_f64(sigma, W, tol=5e-14, maxit=400):
    N = W.shape[0]
    l = np.zeros(N - 1)
    def Gval(lv):
        f = W[1:].T @ lv; m = f.max()
        return m + np.log(np.mean(np.exp(f - m))) + np.exp(-sigma * lv).sum()
    for _ in range(maxit):
        f = W[1:].T @ l; f -= f.max()
        w = np.exp(f); p = w / w.sum()
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
    return l

def mp_newton_steps(lm, sg, Wmp, N, steps=3):
    for _ in range(steps):
        field = [sum(Wmp[a + 1][s] * lm[a] for a in range(N - 1)) for s in range(N)]
        fmax = max(field)
        ws = [mexp(f - fmax) for f in field]
        Z = sum(ws); p = [w / Z for w in ws]
        x = [sum(Wmp[a + 1][s] * p[s] for s in range(N)) for a in range(N - 1)]
        barrier = [mexp(-sg[a] * lm[a]) for a in range(N - 1)]
        grad = [x[a] - sg[a] * barrier[a] for a in range(N - 1)]
        H = matrix(N - 1, N - 1)
        for a in range(N - 1):
            for b in range(a, N - 1):
                v = sum(Wmp[a + 1][s] * Wmp[b + 1][s] * p[s] for s in range(N)) - x[a] * x[b]
                if a == b: v += barrier[a]
                H[a, b] = v; H[b, a] = v
        step = lu_solve(H, matrix(grad))
        for a in range(N - 1):
            lm[a] -= step[a]
    return lm

def main():
    n = 5; N = 32
    mp.dps = 40
    W = walsh_matrix(n)
    Wmp = [[mpf(int(W[a][s])) for s in range(N)] for a in range(N)]

    # certified delta enclosure (dps 60 bracketing)
    mp.dps = 60
    pol = lambda u: u**(N + 1) + u**N + (N - 1) * u - 1
    lo, hi = mpf(0), mpf(1) / (N - 1)
    assert pol(lo) < 0 and pol(hi) > 0
    for _ in range(300):
        mid = (lo + hi) / 2
        if pol(mid) < 0: lo = mid
        else: hi = mid
    def Dof(u):
        A = 1 - (N - 1) * u; B = 1 + u
        return (A * mlog(A) + (N - 1) * B * mlog(B)) / N
    Dlo_d, Dhi_d = min(Dof(lo), Dof(hi)), max(Dof(lo), Dof(hi))
    mp.dps = 40

    # delta orbit id (rep 0 in target gauge: sigma = all -1 -> bits 0)
    orbits = []
    with open("orbits_n5.txt") as f:
        for line in f:
            r, sz = line.split()
            orbits.append((int(r), int(sz)))
    total = sum(sz for _, sz in orbits)
    assert total == 1 << 31, f"checksum fail {total}"
    print(f"orbit file OK: {len(orbits)} orbits, sizes sum to 2^31")

    worst = None; worst_rep = None; fails = 0
    results = []
    for i, (rep, sz) in enumerate(orbits):
        sigma = np.array([1.0 if (rep >> k) & 1 else -1.0 for k in range(N - 1)])
        l64 = solve_seal_f64(sigma, W)
        lm = [mpf(float(v)) for v in l64]
        sg = [mpf(int(v)) for v in sigma]
        lm = mp_newton_steps(lm, sg, Wmp, N, steps=3)
        # certified evaluation at lm
        field = [sum(Wmp[a + 1][s] * lm[a] for a in range(N - 1)) for s in range(N)]
        fmax = max(field)
        ws = [mexp(f - fmax) for f in field]
        Z = sum(ws); p = [w / Z for w in ws]
        x = [sum(Wmp[a + 1][s] * p[s] for s in range(N)) for a in range(N - 1)]
        barrier = [mexp(-sg[a] * lm[a]) for a in range(N - 1)]
        grad = [x[a] - sg[a] * barrier[a] for a in range(N - 1)]
        rho = msqrt(sum(g * g for g in grad))
        lam = min(barrier)
        r0 = 2 * mexp(1) * rho / lam
        lnorm = msqrt(sum(v * v for v in lm))
        eD = (N - 1) * (lnorm + r0) * r0
        X = [N * pv for pv in p]
        Dtil = sum(p[s] * mlog(X[s]) for s in range(N))
        is_delta = (rep == 0)
        results.append((rep, sz, float(Dtil), float(eD), float(r0)))
        if r0 > 0.5:
            fails += 1
            print(f"  rep {rep}: RADIUS FAIL r0={mp.nstr(r0,5)}")
            continue
        if is_delta:
            ok = (Dtil - eD <= Dhi_d) and (Dtil + eD >= Dlo_d)
            print(f"  delta orbit: size={sz}, D={mp.nstr(Dtil,25)} enclosure-match={ok}")
            if not ok: fails += 1
        else:
            margin = (Dtil - eD) - Dhi_d
            if worst is None or margin < worst:
                worst, worst_rep = margin, rep
            if margin <= 0:
                fails += 1
                print(f"  rep {rep}: MARGIN FAIL {mp.nstr(margin,8)}")
        if i % 20 == 0:
            import sys; print(f"  ... {i}/{len(orbits)}", file=sys.stderr)

    print(f"\nn=5 CERTIFIED SUMMARY: orbits={len(orbits)}, failures={fails}")
    print(f"  D_delta(32) in [{mp.nstr(Dlo_d,25)}, {mp.nstr(Dhi_d,25)}]")
    print(f"  worst certified non-delta margin = {mp.nstr(worst,15)} (orbit rep {worst_rep})")
    res = sorted(results, key=lambda r: r[2])
    print("  five lowest orbits by D: (rep, size, D, errD)")
    for r in res[:5]:
        print(f"    {r[0]:>10} {r[1]:>10} {r[2]:.9f} {r[3]:.2e}")
    np.save("cert_n5_results.npy", np.array([(r[0], r[1], r[2], r[3]) for r in results]))

if __name__ == "__main__":
    main()
