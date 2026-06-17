"""
R2-counterexample INDEPENDENT hunt for Paper XVIII (chiral-gap global-optimality lemma).

Independently implemented from the paper's STATED definitions (not copied from pD):
  - states s in {+-1}^n, characters chi_a(s) = prod_{i in a} s_i
  - orientation eps_a in {+-1} on each nonzero mask a (M = 2^n - 1 of them)
  - seal: tilted law P(s) ∝ exp(sum_a h_a eps_a chi_a(s)); fixed point E_P[eps_a chi_a]=e^{-h_a}
  - chiral gap m_hat(eps) = D(P*||U) (nats)
  - claim: global min over orientations attained at alternating-by-weight eps_a=(-1)^{|a|-1},
    value m_hat_min(n) = -ln(1-2^-n) - delta_n.

This re-derives everything and hunts adversarially for an orientation beating alternating.
"""
import itertools
import numpy as np
import mpmath as mp

mp.mp.dps = 60


# --------------------------------------------------------------------------- #
# independent character matrix
# --------------------------------------------------------------------------- #
def char_matrix(n):
    """rows = states s, cols = nonzero masks a (1..2^n-1), entry = chi_a(s) = prod_{i in a} s_i."""
    states = np.array(list(itertools.product((-1, 1), repeat=n)), dtype=float)
    N = states.shape[0]
    M = (1 << n) - 1
    C = np.empty((N, M), dtype=float)
    for mask in range(1, 1 << n):
        idx = [i for i in range(n) if (mask >> i) & 1]
        C[:, mask - 1] = np.prod(states[:, idx], axis=1)
    return C, states


def altweight(n):
    return np.array([(-1) ** (bin(mask).count("1") - 1) for mask in range(1, 1 << n)], dtype=float)


# --------------------------------------------------------------------------- #
# Independent seal solver (float64). Minimize the strictly-convex potential
#   G(h) = log( (1/N) sum_s exp( sum_a h_a phi_a(s) ) ) + sum_a e^{-h_a},
# phi_a(s) = eps_a chi_a(s). grad G = E_P[phi] - e^{-h} = 0 is exactly the seal.
# I use damped Newton with backtracking line search on G (convex => global min).
# Then m_hat = D(P*||U).
# --------------------------------------------------------------------------- #
def seal_gap(eps, C, tol=1e-14, maxit=500, hcap=60.0):
    phi = C * np.asarray(eps, float)[None, :]
    N, M = phi.shape
    h = np.zeros(M)

    def Gpot(hh):
        z = phi @ hh
        mx = z.max()
        return mx + np.log(np.mean(np.exp(z - mx))) + np.sum(np.exp(-hh))

    for _ in range(maxit):
        z = phi @ h
        z -= z.max()
        w = np.exp(z)
        p = w / w.sum()
        E = phi.T @ p
        grad = E - np.exp(-h)
        if np.max(np.abs(grad)) < tol:
            break
        Cov = (phi * p[:, None]).T @ phi - np.outer(E, E)
        J = Cov + np.diag(np.exp(-h))
        try:
            step = np.linalg.solve(J, grad)
        except np.linalg.LinAlgError:
            step = np.linalg.lstsq(J, grad, rcond=None)[0]
        # backtracking line search on convex G
        G0 = Gpot(h)
        t = 1.0
        while t > 1e-10:
            hn = np.minimum(h - t * step, hcap)
            if Gpot(hn) <= G0 + 1e-13:
                break
            t *= 0.5
        h = np.minimum(h - t * step, hcap)
    z = phi @ h
    z -= z.max()
    p = np.exp(z)
    p /= p.sum()
    return float(np.sum(p * np.log(p * N))), p, phi.sum(1)


# --------------------------------------------------------------------------- #
# Independent mpmath seal (high precision) for tie-breaking / verification
# --------------------------------------------------------------------------- #
def seal_gap_mp(eps, n, dps=50, maxit=3000):
    old = mp.mp.dps
    mp.mp.dps = dps
    try:
        states = list(itertools.product((-1, 1), repeat=n))
        N = len(states)
        M = (1 << n) - 1
        phi = []
        for s in states:
            row = []
            for mask in range(1, 1 << n):
                pr = 1
                for i in range(n):
                    if (mask >> i) & 1:
                        pr *= s[i]
                row.append(mp.mpf(int(eps[mask - 1]) * pr))
            phi.append(row)
        h = [mp.mpf(0)] * M
        for _ in range(maxit):
            z = [sum(phi[s][a] * h[a] for a in range(M)) for s in range(N)]
            mx = max(z)
            w = [mp.e ** (z[s] - mx) for s in range(N)]
            Z = sum(w)
            p = [w[s] / Z for s in range(N)]
            E = [sum(p[s] * phi[s][a] for s in range(N)) for a in range(M)]
            emh = [mp.e ** (-h[a]) for a in range(M)]
            grad = [E[a] - emh[a] for a in range(M)]
            if max(abs(g) for g in grad) < mp.mpf(10) ** (-(dps - 8)):
                break
            Hk = [[mp.mpf(0)] * M for _ in range(M)]
            for a in range(M):
                for b in range(a, M):
                    cov = sum(p[s] * phi[s][a] * phi[s][b] for s in range(N)) - E[a] * E[b]
                    Hk[a][b] = cov + (emh[a] if a == b else mp.mpf(0))
                    Hk[b][a] = Hk[a][b]
            step = mp.lu_solve(mp.matrix(Hk), mp.matrix(grad))
            h = [h[a] - step[a] for a in range(M)]
        z = [sum(phi[s][a] * h[a] for a in range(M)) for s in range(N)]
        mx = max(z)
        w = [mp.e ** (z[s] - mx) for s in range(N)]
        Z = sum(w)
        p = [w[s] / Z for s in range(N)]
        D = sum(p[s] * mp.log(p[s] * N) for s in range(N))
        gn = max(abs(g) for g in grad)
        return D, gn
    finally:
        mp.mp.dps = old


def closed_form(n):
    N = 1 << n
    M = N - 1

    def fp(h):
        w0 = mp.e ** (-h * M)
        eh = mp.e ** h
        Z = w0 + M * eh
        return (w0 * (-1) + eh) / Z - mp.e ** (-h)
    h = mp.findroot(fp, mp.log(mp.mpf(M)))
    w0 = mp.e ** (-h * M)
    eh = mp.e ** h
    Z = w0 + M * eh
    psi = mp.log(Z / N)
    return h * (M * mp.e ** (-h)) - psi


# =========================================================================== #
print("=" * 80)
print("PART 1: independent exhaustive base n=2,3,4 (confirm global min = alt-by-weight = p9a)")
print("=" * 80)
for n in [2, 3, 4]:
    C, _ = char_matrix(n)
    M = (1 << n) - 1
    cf = float(closed_form(n))
    g_alt = seal_gap(altweight(n), C)[0]
    best = np.inf
    best_eps = None
    for bits in itertools.product((-1, 1), repeat=M):
        g = seal_gap(np.array(bits, float), C)[0]
        if g < best:
            best = g
            best_eps = bits
    print(f"  n={n}: classes=2^{M}={2**M:>6d}  global_min={best:.12f}  closed={cf:.12f}  "
          f"alt_gap={g_alt:.12f}")
    print(f"        min==closed? {abs(best-cf)<1e-9}   alt==min? {abs(g_alt-best)<1e-9}   "
          f"alt==closed? {abs(g_alt-cf)<1e-9}")
    # is the minimizer the alternating orbit? check T-multiset matches mu*
    Tbest = (C * np.array(best_eps, float)[None, :]).sum(1)
    mu_star = sorted([-(2**n - 1)] + [1] * (2**n - 1))
    print(f"        minimizer T-multiset == mu*? {sorted(int(round(t)) for t in Tbest)==mu_star}")


# =========================================================================== #
print()
print("=" * 80)
print("PART 2: n=5 adversarial hunt for an orientation beating alt-by-weight")
print("=" * 80)
# The minimizer must be maximally negatively-concentrated (moment invariant B):
# minT must be as deep as possible. mu* has minT = -(2^n-1). So the deep-minT band
# is where any beating class lives. Enumerate ALL gauge-fixed orientations with deep
# minT via the Walsh transform, plus random + greedy + structured families.

def hadamard_sub(n):
    N = 1 << n
    H = np.empty((N, N), dtype=np.int32)
    for s in range(N):
        for a in range(N):
            H[s, a] = -1 if (bin(s & a).count("1") & 1) else 1
    return H[:, 1:]  # N x (N-1)

n = 5
C5, _ = char_matrix(n)
cf5 = float(closed_form(n))
g_alt5 = seal_gap(altweight(n), C5)[0]
print(f"  closed mu* = {cf5:.12f} ; alt gap = {g_alt5:.12f} ; |diff|={abs(cf5-g_alt5):.2e}")

# gauge-fix: pin singleton signs to +1 (sound by spin-flip orbit invariance C).
N = 1 << n; M = N - 1
Hsub = hadamard_sub(n)
singleton_cols = [(1 << i) - 1 for i in range(n)]
free_cols = [c for c in range(M) if c not in singleton_cols]
base = Hsub[:, singleton_cols].sum(axis=1)
HF = Hsub[:, free_cols]
F = len(free_cols)
print(f"  gauge-fixed free dims = {F} (space 2^{F} = {2**F})")

# Enumerate ALL 2^26 gauge-fixed orientations, keep ones with deep minT.
# We sweep thresholds to be sure we capture every candidate near the deep end.
DEEP_THRESH = -23   # keep minT <= -23 (mu* has minT=-31). Captures a wide deep band.
bitw = np.arange(F, dtype=np.uint64)
CHUNK = 1 << 22
total = 1 << F
deep_orients = []
best_minT = 0
minT_hist = {}
for start in range(0, total, CHUNK):
    end = min(start + CHUNK, total)
    idx = np.arange(start, end, dtype=np.uint64)
    bits = ((idx[:, None] >> bitw[None, :]) & 1).astype(np.int32)
    signs = bits * 2 - 1
    T = base[None, :] + signs @ HF.T
    mins = T.min(axis=1)
    best_minT = min(best_minT, int(mins.min()))
    for mt in np.unique(mins):
        minT_hist[int(mt)] = minT_hist.get(int(mt), 0) + int((mins == mt).sum())
    sel = np.where(mins <= DEEP_THRESH)[0]
    for j in sel:
        full = np.ones(M, dtype=np.int32)
        full[free_cols] = signs[j]
        deep_orients.append(full)

print(f"  deepest minT reached = {best_minT} (mu* minT = -{N-1})")
print(f"  deep orientations (minT<=-23) collected = {len(deep_orients)}")
print(f"  minT histogram (deep tail): " +
      ", ".join(f"{k}:{minT_hist[k]}" for k in sorted(minT_hist)[:8]))

# Evaluate EXACT vector-seal gap at the ORIENTATION level on every deep orientation.
min_gap5 = np.inf
below = []
mu_star_present = False
for full in deep_orients:
    g = seal_gap(full.astype(float), C5)[0]
    if g < min_gap5:
        min_gap5 = g
    if g < cf5 - 1e-8:
        below.append((g, full.copy()))
    if abs(g - cf5) < 1e-8:
        mu_star_present = True
print(f"  min gap over {len(deep_orients)} deep orientations = {min_gap5:.12f}")
print(f"  mu* realized (gap==closed) among deep? {mu_star_present}")
print(f"  orientations BELOW mu*: {len(below)}")
