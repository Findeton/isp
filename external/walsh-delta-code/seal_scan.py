"""Exhaustive sealed-orientation scan for the Walsh Delta Global-Optimality
Problem.

Setup (target-free indexing): G = F_2^n as bitmasks 0..N-1, chi_a(s) =
(-1)^{popcount(a&s)}.  An orientation is sigma in {+-1}^{N-1} (indexed by
nonzero masks a = 1..N-1).  The sealed point is the unique minimizer of the
strictly convex coercive function

    G_sigma(l) = F(l) + sum_a exp(-sigma_a l_a),
    F(l) = log mean_s exp(sum_a l_a chi_a(s)).

At the minimum:  x_a := E_P[chi_a] = sigma_a exp(-sigma_a l_a),
which is exactly the seal  E_P[sigma_a chi_a] = e^{-h_a},  h_a = sigma_a l_a.

Outputs per orientation: D = D(P||U), Dbar = D(U||P), chi2 = sum x_a^2,
sumDL = sum over Walsh lines of 4-point quotient KL, R2 = D - gamma_n*sumDL,
minX = min_s X(s).
"""
import numpy as np
import itertools, sys

def walsh_matrix(n):
    N = 1 << n
    a = np.arange(N)
    # W[a, s] = (-1)^{popcount(a & s)}
    pc = np.zeros((N, N), dtype=np.int64)
    for i, ai in enumerate(a):
        pc[i] = [bin(ai & s).count("1") for s in range(N)]
    return np.where(pc % 2 == 0, 1.0, -1.0)

def lines(N):
    """All Walsh lines {a,b,a^b}, a,b,c nonzero distinct, as sorted triples."""
    out = set()
    for a in range(1, N):
        for b in range(a + 1, N):
            c = a ^ b
            if c > b:
                out.add((a, b, c))
    return sorted(out)

def solve_seal(sigma, W, tol=1e-13, maxit=200):
    """Damped Newton on G_sigma. sigma: (N-1,) array of +-1.
    Returns l (N-1,), x (N-1,), X (N,), ok flag."""
    N = W.shape[0]
    l = np.zeros(N - 1)
    for it in range(maxit):
        field = W[1:].T @ l                       # (N,) sum_a l_a chi_a(s)
        field -= field.max()
        w = np.exp(field)
        Z = w.sum()
        p = w / Z                                  # P(s)
        x = W[1:] @ p                              # x_a = E_P chi_a
        barrier = np.exp(-sigma * l)               # e^{-sigma_a l_a}
        grad = x - sigma * barrier
        # Hessian: Cov_P(chi) + diag(barrier)
        Wc = W[1:] * np.sqrt(p)[None, :]
        H = Wc @ Wc.T - np.outer(x, x) + np.diag(barrier)
        try:
            step = np.linalg.solve(H, grad)
        except np.linalg.LinAlgError:
            step = np.linalg.lstsq(H, grad, rcond=None)[0]
        # damped line search on G value
        def Gval(lv):
            f = W[1:].T @ lv
            m = f.max()
            return m + np.log(np.mean(np.exp(f - m))) + np.exp(-sigma * lv).sum()
        g0 = Gval(l)
        t = 1.0
        while t > 1e-8:
            l_new = l - t * step
            if Gval(l_new) <= g0 + 1e-15:
                break
            t /= 2
        l = l - t * step
        if np.abs(grad).max() < tol:
            break
    field = W[1:].T @ l
    field -= field.max()
    w = np.exp(field)
    p = w / w.sum()
    x = W[1:] @ p
    ok = np.abs(x - sigma * np.exp(-sigma * l)).max() < 1e-9
    return l, x, p, ok

def quantities(l, x, p, W, LINES, gamma):
    N = W.shape[0]
    X = N * p
    D = float(np.sum(p * np.log(np.maximum(X, 1e-300))))
    Dbar = float(-np.mean(np.log(np.maximum(X, 1e-300))))
    chi2 = float(np.sum(x * x))
    sumDL = 0.0
    for (a, b, c) in LINES:
        xa, xb, xc = x[a - 1], x[b - 1], x[c - 1]
        vals = np.array([1 + xa + xb + xc, 1 + xa - xb - xc,
                         1 - xa + xb - xc, 1 - xa - xb + xc])
        vals = np.maximum(vals, 1e-300)
        sumDL += 0.25 * float(np.sum(vals * np.log(vals)))
    R2 = D - gamma * sumDL
    return D, Dbar, chi2, sumDL, R2, float(X.min())

def delta_reference(n):
    """Solve u^{N+1} + u^N + (N-1)u - 1 = 0 for the delta amplitude."""
    N = 1 << n
    from numpy.polynomial import polynomial as P
    coeffs = np.zeros(N + 2)
    coeffs[0] = -1.0; coeffs[1] = N - 1.0; coeffs[N] = 1.0; coeffs[N + 1] = 1.0
    roots = np.roots(coeffs[::-1])
    real = [r.real for r in roots if abs(r.imag) < 1e-12 and 0 < r.real < 1.0 / (N - 1) + 1e-9]
    return min(real)

def main(n):
    N = 1 << n
    W = walsh_matrix(n)
    LINES = lines(N)
    nL = len(LINES)
    gamma = n / (2.0 * nL)
    assert nL == (N - 1) * (N - 2) // 6

    ustar = delta_reference(n)
    DLstar = 0.25 * ((1 - 3 * ustar) * np.log(1 - 3 * ustar)
                     + 3 * (1 + ustar) * np.log(1 + ustar))

    M = N - 1
    total = 1 << M
    print(f"n={n} N={N} orientations={total} lines={nL} u*={ustar:.12f} DL*={DLstar:.12e}")

    recs = []
    for idx in range(total):
        sigma = np.array([1.0 if (idx >> k) & 1 else -1.0 for k in range(M)])
        l, x, p, ok = solve_seal(sigma, W)
        if not ok:
            print(f"  WARN idx={idx} not converged")
        D, Dbar, chi2, sumDL, R2, minX = quantities(l, x, p, W, LINES, gamma)
        recs.append((idx, D, Dbar, chi2, sumDL, R2, minX))
        if total >= 1000 and idx % max(1, total // 20) == 0:
            print(f"  ... {idx}/{total}", file=sys.stderr)

    recs.sort(key=lambda r: r[1])
    arr = np.array([(r[1], r[2], r[3], r[4], r[5], r[6]) for r in recs])
    idxs = [r[0] for r in recs]

    # Delta orientations: sigma_a = -chi_a(s*) for each s*.
    delta_ids = set()
    for sstar in range(N):
        bits = 0
        for a in range(1, N):
            sa = -W[a, sstar]   # sigma_a
            if sa > 0:
                bits |= (1 << (a - 1))
        delta_ids.add(bits)

    print(f"delta orbit size: {len(delta_ids)}")
    D_delta = None
    for r in recs:
        if r[0] in delta_ids:
            D_delta = r[1]; delta_rec = r
            break
    # gather all delta records for consistency
    dvals = [r[1] for r in recs if r[0] in delta_ids]
    print(f"delta D values: min={min(dvals):.12f} max={max(dvals):.12f}")

    # analytic delta D
    A = 1 - (N - 1) * ustar; B = 1 + ustar
    D_delta_analytic = (A * np.log(A) + (N - 1) * B * np.log(B)) / N
    print(f"analytic delta D = {D_delta_analytic:.12f}")

    print("\nlowest 12 orientations by D:")
    print(f"{'idx':>8} {'D':>14} {'Dbar':>12} {'chi2':>12} {'sumDL':>12} {'R2':>12} {'minX':>10} delta?")
    for r in recs[:12]:
        print(f"{r[0]:>8} {r[1]:>14.9f} {r[2]:>12.6f} {r[3]:>12.8f} {r[4]:>12.8f} {r[5]:>12.8f} {r[6]:>10.6f} {r[0] in delta_ids}")

    # SPS checks over ALL orientations
    delta_recs = [r for r in recs if r[0] in delta_ids]
    R2_delta = max(r[5] for r in delta_recs)
    sumDL_delta_num = min(r[4] for r in delta_recs)
    sumDLstar = nL * DLstar
    print(f"\nsum_L DL* (analytic) = {sumDLstar:.10e}, numeric delta sumDL = {sumDL_delta_num:.10e}")
    chi2_delta = max(r[3] for r in delta_recs)

    viol1 = [r for r in recs if r[0] not in delta_ids and r[4] < sumDLstar - 1e-11]
    viol2 = [r for r in recs if r[0] not in delta_ids and r[5] < R2_delta - 1e-11]
    print(f"SPS-1 (sum_L D_L >= sum_L DL*): violations among non-delta: {len(viol1)}")
    print(f"SPS-2 (R2 >= R2_delta={R2_delta:.10f}): violations among non-delta: {len(viol2)}")
    if viol2[:5]:
        for r in viol2[:5]:
            print(f"   SPS-2 viol: idx={r[0]} D={r[1]:.9f} R2={r[5]:.9f}")
    nd = [r for r in recs if r[0] not in delta_ids]
    min_chi2_nd = min(r[3] for r in nd)
    print(f"chi2 floor: chi2_delta={chi2_delta:.10f}, min non-delta chi2={min_chi2_nd:.10f}, ratio={min_chi2_nd/chi2_delta:.6f}")
    min_sumDL_nd = min(r[4] for r in nd)
    print(f"sumDL: delta={sumDL_delta_num:.10e}, min non-delta={min_sumDL_nd:.10e}, ratio={min_sumDL_nd/sumDLstar:.6f}")
    min_R2_nd = min(r[5] for r in nd)
    print(f"R2: delta={R2_delta:.10e}, min non-delta={min_R2_nd:.10e}")
    minD_nd = min(r[1] for r in nd)
    print(f"D: delta={D_delta:.10f}, min non-delta={minD_nd:.10f}, ratio={minD_nd/D_delta:.6f}")
    # Dbar maximality check
    Dbar_delta = min(r[2] for r in delta_recs)
    max_Dbar_nd = max(r[2] for r in nd)
    print(f"Dbar: delta={Dbar_delta:.10f}, max non-delta={max_Dbar_nd:.10f}")
    np.save(f"scan_n{n}.npy", np.array([(r[0],)+r[1:] for r in recs]))

if __name__ == "__main__":
    for n in [int(t) for t in sys.argv[1:]] or [2, 3]:
        main(n)
        print("=" * 90)
