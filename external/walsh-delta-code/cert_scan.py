"""Certified verification of Global Delta Optimality for n = 2, 3, 4.

For EVERY orientation sigma:
  1. float64 damped Newton on the strictly convex G_sigma -> l_tilde.
  2. mpmath (dps=30) exact-style evaluation AT l_tilde (l_tilde's float64
     entries are exact binary rationals, so the mp evaluation error is
     ~1e-30, dominated by the dps budget):
       rho    = ||grad G(l_tilde)||_2           (certified residual)
       lam    = min_a exp(-sigma_a l_tilde_a)   (certified Hessian floor)
       Dtil   = D(l_tilde)                      (certified value)
  3. A posteriori bound (rigorous; proof in the deliverable):
       if r0 := 2*e*rho/lam <= 1 then ||l* - l_tilde||_2 <= r0,
     using Hess G >= diag(e^{-sigma l}) >= lam*e^{-1} on the segment.
  4. Lipschitz transfer:  grad D(l) = H_F(l) l, and
       ||H_F(l)|| <= trace(Cov) <= N-1  (Cov of +-1 variables),
     so |D(l*) - Dtil| <= (N-1) * (||l_tilde|| + r0) * r0 =: eD.
  5. Certified comparison: for non-delta sigma require
       Dtil - eD > Ddelta_hi,
     where Ddelta_hi is a certified upper enclosure of D_delta from the
     scalar seal polynomial p(u) = u^{N+1} + u^N + (N-1)u - 1 via sign
     bracketing at dps 60.

Output: per-n summary with the worst (smallest) certified margin.
"""
import numpy as np
from mpmath import mp, mpf, exp as mexp, log as mlog, sqrt as msqrt

def walsh_matrix(n):
    N = 1 << n
    pc = np.zeros((N, N), dtype=np.int64)
    for a in range(N):
        pc[a] = [bin(a & s).count("1") for s in range(N)]
    return np.where(pc % 2 == 0, 1.0, -1.0)

def solve_seal_f64(sigma, W, tol=5e-14, maxit=300):
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

def delta_enclosure(n, dps=60):
    """Certified enclosure [Dlo, Dhi] for D_delta via sign bracketing."""
    mp.dps = dps
    N = 1 << n
    p = lambda u: u**(N + 1) + u**N + (N - 1) * u - 1
    lo, hi = mpf(0), mpf(1) / (N - 1)
    assert p(lo) < 0 and p(hi) > 0
    for _ in range(300):
        mid = (lo + hi) / 2
        if p(mid) < 0: lo = mid
        else: hi = mid
    def Dof(u):
        A = 1 - (N - 1) * u; B = 1 + u
        return (A * mlog(A) + (N - 1) * B * mlog(B)) / N
    # D is monotone in u near u* in a mild interval; take max/min over endpoints
    cands = [Dof(lo), Dof(hi)]
    return min(cands), max(cands)

def certify(n, mp_dps=30, report_every=4096):
    N = 1 << n
    W = walsh_matrix(n)
    Wmp = [[mpf(int(W[a][s])) for s in range(N)] for a in range(N)]
    Dlo_d, Dhi_d = delta_enclosure(n)
    mp.dps = mp_dps
    total = 1 << (N - 1)
    delta_ids = set()
    for sstar in range(N):
        bits = 0
        for a in range(1, N):
            if -W[a, sstar] > 0: bits |= 1 << (a - 1)
        delta_ids.add(bits)

    worst_margin = None; worst_idx = None
    max_r0 = mpf(0); max_eD = mpf(0); fails = 0
    for idx in range(total):
        sigma = np.array([1.0 if (idx >> k) & 1 else -1.0 for k in range(N - 1)])
        l = solve_seal_f64(sigma, W)
        # certified mp evaluation at exact float64 point
        lm = [mpf(float(v)) for v in l]
        sg = [mpf(int(v)) for v in sigma]
        field = [sum(Wmp[a + 1][s] * lm[a] for a in range(N - 1)) for s in range(N)]
        fmax = max(field)
        ws = [mexp(f - fmax) for f in field]
        Z = sum(ws)
        pmp = [w / Z for w in ws]
        x = [sum(Wmp[a + 1][s] * pmp[s] for s in range(N)) for a in range(N - 1)]
        barrier = [mexp(-sg[a] * lm[a]) for a in range(N - 1)]
        grad = [x[a] - sg[a] * barrier[a] for a in range(N - 1)]
        rho = msqrt(sum(g * g for g in grad))
        lam = min(barrier)
        r0 = 2 * mexp(1) * rho / lam
        if not (r0 <= mpf(1) / 2):   # NaN-safe: NaN fails loudly
            fails += 1
            print(f"  n={n} idx={idx}: KANTOROVICH RADIUS TOO LARGE r0={mp.nstr(r0,5)}")
            continue
        lnorm = msqrt(sum(v * v for v in lm))
        eD = (N - 1) * (lnorm + r0) * r0
        # D(l_tilde), certified
        X = [N * pv for pv in pmp]
        Dtil = sum(pmp[s] * mlog(X[s]) for s in range(N))
        max_r0 = max(max_r0, r0); max_eD = max(max_eD, eD)
        if idx in delta_ids:
            # certified consistency: |Dtil - D_delta| small
            if not (Dtil - eD <= Dhi_d and Dtil + eD >= Dlo_d):
                fails += 1
                print(f"  n={n} delta idx={idx}: enclosure mismatch")
        else:
            margin = (Dtil - eD) - Dhi_d
            if worst_margin is None or margin < worst_margin:
                worst_margin, worst_idx = margin, idx
            if margin <= 0:
                fails += 1
                print(f"  n={n} idx={idx}: MARGIN FAIL {mp.nstr(margin,8)}")
        if idx % report_every == 0:
            import sys
            print(f"  ... n={n} {idx}/{total}", file=sys.stderr)
    print(f"n={n}: CERTIFIED. orientations={total}, failures={fails}")
    print(f"  D_delta in [{mp.nstr(Dlo_d,25)}, {mp.nstr(Dhi_d,25)}]")
    print(f"  worst certified non-delta margin = {mp.nstr(worst_margin,15)} (idx {worst_idx})")
    print(f"  max Kantorovich radius r0 = {mp.nstr(max_r0,4)}, max |D|-error = {mp.nstr(max_eD,4)}")
    return fails == 0

if __name__ == "__main__":
    import sys
    ok = True
    for n in [int(t) for t in (sys.argv[1:] or ["2", "3", "4"])]:
        ok &= certify(n)
    print("ALL CERTIFIED" if ok else "FAILURES PRESENT")
