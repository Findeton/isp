"""High-precision (mpmath, dps=50) re-verification of the critical scan
values: delta D and runner-up D for n=3,4, and the SPS-2 margin at n=3
(the thinnest margin found in the float64 scans).

Solves the seal by Newton on the convex G_sigma entirely in mpmath.
"""
from mpmath import mp, mpf, exp, log, matrix, lu_solve, norm
mp.dps = 50

def walsh(n):
    N = 1 << n
    return [[mpf(-1) ** bin(a & s).count("1") for s in range(N)] for a in range(N)]

def solve_seal(sigma, W, N, maxit=200):
    l = [mpf(0)] * (N - 1)
    for it in range(maxit):
        field = [sum(W[a + 1][s] * l[a] for a in range(N - 1)) for s in range(N)]
        mx = max(field)
        ws = [exp(f - mx) for f in field]
        Z = sum(ws)
        p = [w / Z for w in ws]
        x = [sum(W[a + 1][s] * p[s] for s in range(N)) for a in range(N - 1)]
        barrier = [exp(-sigma[a] * l[a]) for a in range(N - 1)]
        grad = [x[a] - sigma[a] * barrier[a] for a in range(N - 1)]
        gmax = max(abs(g) for g in grad)
        if gmax < mpf(10) ** (-40):
            break
        H = matrix(N - 1, N - 1)
        for a in range(N - 1):
            for b in range(a, N - 1):
                v = sum(W[a + 1][s] * W[b + 1][s] * p[s] for s in range(N)) - x[a] * x[b]
                if a == b:
                    v += barrier[a]
                H[a, b] = v; H[b, a] = v
        step = lu_solve(H, matrix(grad))
        for a in range(N - 1):
            l[a] -= step[a]
    return l, x, p, gmax

def quantities(sigma, W, N, label):
    l, x, p, res = solve_seal(sigma, W, N)
    X = [N * pi for pi in p]
    D = sum(p[s] * log(X[s]) for s in range(N))
    print(f"  {label}: D = {mp.nstr(D, 25)}   (Newton residual {mp.nstr(res, 3)})")
    return D, x

def lines(N):
    out = set()
    for a in range(1, N):
        for b in range(a + 1, N):
            c = a ^ b
            if c > b:
                out.add((a, b, c))
    return sorted(out)

def R2(x, D, N, n):
    LL = lines(N)
    gamma = mpf(n) / (2 * len(LL))
    sDL = mpf(0)
    for (a, b, c) in LL:
        xa, xb, xc = x[a - 1], x[b - 1], x[c - 1]
        for ea in (1, -1):
            for eb in (1, -1):
                v = 1 + xa * ea + xb * eb + xc * ea * eb
                sDL += v * log(v) / 4
    return D - gamma * sDL

for n, delta_idx, runner_idx in [(3, 0, 46), (4, 0, 480)]:
    N = 1 << n
    W = walsh(n)
    print(f"n={n}:")
    sig_d = [-W[a][0] for a in range(1, N)]          # delta at s*=0
    Dd, xd = quantities(sig_d, W, N, "delta   ")
    sig_r = [mpf(1) if (runner_idx >> k) & 1 else mpf(-1) for k in range(N - 1)]
    Dr, xr = quantities(sig_r, W, N, "runner-up")
    print(f"  gap D_runner - D_delta = {mp.nstr(Dr - Dd, 20)}  (must be > 0)")
    if n == 3:
        R2d = R2(xd, Dd, N, n)
        R2r = R2(xr, Dr, N, n)
        print(f"  R2(delta) = {mp.nstr(R2d, 20)}")
        print(f"  R2(runner)= {mp.nstr(R2r, 20)}  margin = {mp.nstr(R2r - R2d, 12)}")
        # also the min-R2 non-delta found in float64 scan: idx 46 family was min; check idx 14 (|M|=1)
        sig1 = [mpf(1) if (14 >> k) & 1 else mpf(-1) for k in range(N - 1)]
        D1, x1 = quantities(sig1, W, N, "|M|=1   ")
        print(f"  R2(|M|=1) = {mp.nstr(R2(x1, D1, N, n), 20)}")
