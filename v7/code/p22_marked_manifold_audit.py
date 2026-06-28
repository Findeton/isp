#!/usr/bin/env python3
"""
Receipt for v7 Paper XXII: marked compensators and finite-order
manifoldlikeness stress tests.

The goal is deliberately modest.  We do not prove manifoldlikeness.  We test
whether the scalar martingale is blind to finite order pathologies and whether
minimal order-sensitive diagnostics can separate a deterministic 2D
lightcone-coordinate grid benchmark from chain, antichain, and KR-layered
counterfamilies.  We also run a fixed 1+1 binomial-sprinkling stress sample,
which shows that the naive interval-damped pair density normalization is not a
manifoldlikeness criterion.

Checks:
  1. Scalar compensator is order-blind at fixed N.
  2. Myrheim-Meyer dimensions are exact/inverted at high precision.
  3. Height-scaling and interval-damped pair densities distinguish selected
     finite benchmark families.
  4. A retuned KR-layered expected family can spoof the 2D Myrheim-Meyer
     ordering fraction at every tested scale.
  5. Single diagnostics are insufficient; a toy combined audit rejects the
     selected non-manifold families while accepting the deterministic 2D grid
     benchmark.
  6. The same toy audit is not a manifoldlikeness gate: a fixed 1+1
     binomial-sprinkling stress sample has the right MM and height behavior but
     fails the naive tightness threshold for the interval-damped pair density.
  7. The correct 1+1 binomial-sprinkling calibration for the pair density is its
     finite-N expectation.  Normalizing by this expectation stabilizes the
     sprinkled sample and rejects an adversarial bilayer-plus-chain family that
     matches MM dimension and height scaling asymptotically.
  8. A stronger thin-middle layered adversary can spoof MM, height, and a
     single-alpha calibrated pair density.  A small multi-alpha profile exposes
     it, so single-alpha rho is not a manifoldlikeness criterion either.
  9. A wider calibrated generating-function profile exposes the tested actual
     transitive adversaries more cleanly than the three-alpha probe.
 10. Even that wider finite profile is underdetermined at the interval-histogram
     level: a positive real-weight interval measure can match the tested Laplace
     samples while hiding most relation mass at interval sizes beyond the probes.
 11. A naive complete-sandwich poset realization of that hidden mass pays a large
     transitivity tax in low-interval pairs, so the histogram witness is not
     automatically a poset construction.
 12. Splitting the same hidden mass into independent complete-sandwich reservoirs
     cannot lower that tax bound; only genuinely overlapping/staggered transitive
     constructions remain as the next adversarial path.

All nontrivial arithmetic uses integer counts and mpmath at dps=140.
No float64 is used for asserted quantities.
"""

import bisect
import random

import mpmath as mp

mp.mp.dps = 140


def fmt(x, n=32):
    return mp.nstr(x, n)


checks = []


def check(name, ok, detail=""):
    checks.append((name, bool(ok), detail))
    status = "PASS" if ok else "FAIL"
    print(f"[{status}] {name} {detail}")


def linreg_slope(xs, ys):
    xs = [mp.mpf(x) for x in xs]
    ys = [mp.mpf(y) for y in ys]
    mx = sum(xs) / len(xs)
    my = sum(ys) / len(ys)
    num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    den = sum((x - mx) ** 2 for x in xs)
    return num / den


def mm_f(d):
    d = mp.mpf(d)
    return mp.gamma(d + 1) * mp.gamma(d / 2) / (2 * mp.gamma(3 * d / 2))


def mm_inv(r):
    r = mp.mpf(r)
    if r <= 0:
        return mp.inf
    if r >= 1:
        return mp.mpf(1)
    lo = mp.mpf(1)
    hi = mp.mpf(64)
    for _ in range(600):
        mid = (lo + hi) / 2
        if mm_f(mid) > r:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def grid2_metrics(n, alpha):
    """Deterministic [n]x[n] lightcone-coordinate grid benchmark."""
    n = int(n)
    N = n * n
    rel = 0
    eff = mp.mpf(0)
    links = 0
    for di in range(0, n):
        for dj in range(0, n):
            if di == 0 and dj == 0:
                continue
            count = (n - di) * (n - dj)
            rel += count
            interior = (di + 1) * (dj + 1) - 2
            if interior == 0:
                links += count
            eff += mp.mpf(count) * mp.e ** (-alpha * interior)
    total = N * (N - 1) // 2
    return {
        "N": mp.mpf(N),
        "relations": mp.mpf(rel),
        "r": mp.mpf(rel) / total,
        "height": mp.mpf(2 * n - 1),
        "links": mp.mpf(links),
        "P": eff / N,
    }


def chain_metrics(N, alpha):
    N = int(N)
    rel = N * (N - 1) // 2
    eff = mp.mpf(0)
    for gap in range(1, N):
        count = N - gap
        interior = gap - 1
        eff += mp.mpf(count) * mp.e ** (-alpha * interior)
    return {
        "N": mp.mpf(N),
        "relations": mp.mpf(rel),
        "r": mp.mpf(1),
        "height": mp.mpf(N),
        "links": mp.mpf(N - 1),
        "P": eff / N,
    }


def antichain_metrics(N, alpha):
    return {
        "N": mp.mpf(N),
        "relations": mp.mpf(0),
        "r": mp.mpf(0),
        "height": mp.mpf(1),
        "links": mp.mpf(0),
        "P": mp.mpf(0),
    }


def kr_expected_metrics(t, p, alpha):
    """Expected metrics for a KR 3-layer family with sizes (t,2t,t).

    Adjacent layer relations occur with probability p.  Bottom-top relations are
    induced by at least one middle bridge.
    """
    t = int(t)
    p = mp.mpf(p)
    a = mp.mpf(t)
    b = mp.mpf(2 * t)
    c = mp.mpf(t)
    N = a + b + c
    adj_pairs = a * b + b * c
    bottom_top_pairs = a * c
    bt_prob = 1 - (1 - p * p) ** b
    rel = p * adj_pairs + bt_prob * bottom_top_pairs
    # Cover relations are adjacent-layer relations.  A bottom-top relation always
    # has a middle bridge by construction, so it is not a cover.
    links = p * adj_pairs
    # Interval-damped pair density: adjacent covers have empty intervals.  For bottom-top
    # intervals, K~Binomial(b,p^2) bridges; relation exists iff K>=1, weight
    # exp(-alpha*K).  E[exp(-alpha K) 1_{K>=1}] is below.
    bt_eff = (1 - p * p + p * p * mp.e ** (-alpha)) ** b - (1 - p * p) ** b
    eff = links + bottom_top_pairs * bt_eff
    total = N * (N - 1) / 2
    return {
        "N": N,
        "relations": rel,
        "r": rel / total,
        "height": mp.mpf(3),
        "links": links,
        "P": eff / N,
    }


class Fenwick:
    def __init__(self, n):
        self.n = int(n)
        self.tree = [0] * (self.n + 1)

    def add(self, i, value):
        i += 1
        while i <= self.n:
            self.tree[i] += value
            i += i & -i

    def prefix_sum(self, i):
        if i < 0:
            return 0
        if i >= self.n:
            i = self.n - 1
        total = 0
        i += 1
        while i > 0:
            total += self.tree[i]
            i -= i & -i
        return total


def lis_length(values):
    piles = []
    for value in values:
        pos = bisect.bisect_left(piles, value)
        if pos == len(piles):
            piles.append(value)
        else:
            piles[pos] = value
    return len(piles)


def sprinkled2_metrics(N, alpha, seed):
    """A fixed 1+1 binomial-sprinkling stress sample.

    Sorting by one lightcone coordinate leaves the other coordinate as a random
    permutation.  This avoids float sampling entirely while representing the
    order type of a continuous iid sprinkling with probability one.
    """
    N = int(N)
    rng = random.Random(seed)
    perm = list(range(N))
    rng.shuffle(perm)
    weights = [mp.e ** (-alpha * k) for k in range(N)]
    rel = 0
    pair_sum = mp.mpf(0)
    for i in range(N):
        bit = Fenwick(N)
        vi = perm[i]
        for j in range(i + 1, N):
            vj = perm[j]
            if vi < vj:
                rel += 1
                interior = bit.prefix_sum(vj - 1) - bit.prefix_sum(vi)
                pair_sum += weights[interior]
            bit.add(vj, 1)
    total = N * (N - 1) // 2
    return {
        "N": mp.mpf(N),
        "relations": mp.mpf(rel),
        "r": mp.mpf(rel) / total,
        "height": mp.mpf(lis_length(perm)),
        "links": mp.nan,
        "P": pair_sum / N,
    }


def sprinkled2_interval_histogram(N, seed):
    """Interval-size histogram for one fixed 1+1 sprinkling order type."""
    N = int(N)
    rng = random.Random(seed)
    perm = list(range(N))
    rng.shuffle(perm)
    hist = [0] * N
    rel = 0
    for i in range(N):
        bit = Fenwick(N)
        vi = perm[i]
        for j in range(i + 1, N):
            vj = perm[j]
            if vi < vj:
                rel += 1
                interior = bit.prefix_sum(vj - 1) - bit.prefix_sum(vi)
                hist[interior] += 1
            bit.add(vj, 1)
    return {
        "N": mp.mpf(N),
        "relations": mp.mpf(rel),
        "r": mp.mpf(rel) / (N * (N - 1) // 2),
        "height": mp.mpf(lis_length(perm)),
        "hist": hist,
    }


def P_from_histogram(N, hist, alpha):
    total = mp.mpf(0)
    q = mp.e ** (-mp.mpf(alpha))
    power = mp.mpf(1)
    for count in hist:
        total += mp.mpf(count) * power
        power *= q
    return total / int(N)


def sprinkle_pair_density_expectation(N, alpha):
    """Exact finite-N expectation of P_alpha for fixed-N 1+1 sprinklings.

    With points iid in the lightcone-coordinate square, for a pair with coordinate
    gaps U,V the interval area is UV and the number of interior points is
    Binomial(N-2, UV).  If q=exp(-alpha) and c=1-q,

      E[P_alpha] = (N-1) * sum_{k=0}^{N-2} binom(N-2,k)(-c)^k
                         / ((k+1)^2 (k+2)^2).

    The alternating sum is cancellation-heavy, so use guard precision that scales
    with N.  Downstream arithmetic and printing consume the value at the ambient
    mpmath precision.  This guard is calibrated for the alpha values used in this
    receipt, not as a general-purpose arbitrary-alpha quadrature replacement.
    """
    N = int(N)
    guard_dps = max(mp.mp.dps + 40, int(mp.ceil(mp.mpf("0.25") * N)) + 80)
    with mp.workdps(guard_dps):
        q = mp.e ** (-mp.mpf(alpha))
        c = 1 - q
        m = N - 2
        s = mp.mpf(0)
        term = mp.mpf(1)
        for k in range(0, m + 1):
            if k > 0:
                term *= mp.mpf(m - k + 1) / mp.mpf(k) * (-c)
            denom = mp.mpf(k + 1) ** 2 * mp.mpf(k + 2) ** 2
            s += term / denom
        return +(mp.mpf(N - 1) * s)


_SPRINKLE_EXPECTATION_CACHE = {}


def cached_sprinkle_pair_density_expectation(N, alpha):
    key = (int(N), mp.nstr(mp.mpf(alpha), 100), mp.mp.dps)
    if key not in _SPRINKLE_EXPECTATION_CACHE:
        _SPRINKLE_EXPECTATION_CACHE[key] = sprinkle_pair_density_expectation(N, alpha)
    return _SPRINKLE_EXPECTATION_CACHE[key]


def bilayer_chain_spoof_metrics(n, alpha):
    """Non-manifold adversary matching MM and height asymptotically.

    N=n^2 records.  Use a complete bilayer on N-n records plus an isolated chain
    of length n.  The bilayer drives r -> 1/2 (so d_MM -> 2); the isolated chain
    gives H=n=sqrt(N).  The interval-damped pair density is enormous because the
    bilayer has O(N^2) empty intervals.
    """
    n = int(n)
    h = n
    N = n * n
    M = N - h
    a = M // 2
    b = M - a
    rel = a * b + h * (h - 1) // 2
    chain_eff = mp.mpf(0)
    for gap in range(1, h):
        chain_eff += mp.mpf(h - gap) * mp.e ** (-alpha * (gap - 1))
    pair_density = (mp.mpf(a * b) + chain_eff) / N
    total = N * (N - 1) // 2
    return {
        "N": mp.mpf(N),
        "relations": mp.mpf(rel),
        "r": mp.mpf(rel) / total,
        "height": mp.mpf(h),
        "links": mp.nan,
        "P": pair_density,
    }


def thin_middle_chain_spoof_metrics(n, middle, alpha):
    """Stronger non-manifold adversary.

    N=n^2.  Use a complete three-layer order A<M<B with a thin middle layer
    |M|=middle, plus an isolated chain of length n.  The bilayer-like A<B
    relation keeps r -> 1/2; the isolated chain keeps H=sqrt(N); tuning the
    middle layer can match a single-alpha calibrated P density.
    """
    n = int(n)
    middle = int(middle)
    h = n
    N = n * n
    remainder = N - h - middle
    a = remainder // 2
    b = remainder - a
    q = mp.e ** (-alpha)
    rel = a * middle + middle * b + a * b + h * (h - 1) // 2
    chain_eff = mp.mpf(0)
    for gap in range(1, h):
        chain_eff += mp.mpf(h - gap) * q ** (gap - 1)
    pair_density = (mp.mpf(middle * (a + b)) + mp.mpf(a * b) * q ** middle + chain_eff) / N
    total = N * (N - 1) // 2
    return {
        "N": mp.mpf(N),
        "relations": mp.mpf(rel),
        "r": mp.mpf(rel) / total,
        "height": mp.mpf(h),
        "links": mp.nan,
        "P": pair_density,
    }


def tune_thin_middle(n, alpha, expected):
    N = int(n) * int(n)
    upper = min(N - int(n) - 2, max(8, int(mp.ceil(8 * mp.log(N)))))
    best = None
    for middle in range(1, upper + 1):
        m = thin_middle_chain_spoof_metrics(n, middle, alpha)
        rho = m["P"] / expected
        score = abs(rho - 1)
        if best is None or score < best[0]:
            best = (score, middle, m, rho)
    return best


def solve_histogram_moment_match(N, alpha_profile, free_m=None, hidden_m=1000):
    """Positive real-weight interval-measure moment match for a finite alpha list.

    This is not a finite-poset construction.  It is a moment-problem adversary:
    P_alpha is a Laplace sample of the interval-size histogram, so finitely many
    alpha values cannot determine the histogram.  The solve includes the hidden
    large-interval column and the target relation-count constraint.
    """
    N = int(N)
    alpha_profile = [mp.mpf(a) for a in alpha_profile]
    n_alpha = len(alpha_profile)
    if free_m is None:
        free_m = n_alpha
    target_relations = mp.mpf(N * (N - 1)) / 4
    guard_dps = max(mp.mp.dps + 80, 220)
    with mp.workdps(guard_dps):
        alpha_work = [mp.mpf(a) for a in alpha_profile]
        targets = mp.matrix(
            [mp.mpf(N) * cached_sprinkle_pair_density_expectation(N, a) for a in alpha_work]
            + [target_relations]
        )
        solved_ms = list(range(n_alpha)) + [int(free_m)]
        hidden = int(hidden_m)
        A = mp.matrix(
            [[mp.e ** (-a * m) for m in solved_ms] for a in alpha_work]
            + [[mp.mpf(1) for _ in solved_ms]]
        )
        hidden_col = mp.matrix([mp.e ** (-a * hidden) for a in alpha_work] + [mp.mpf(1)])
        base = mp.lu_solve(A, targets)
        direction = mp.lu_solve(A, hidden_col)
        lo = mp.mpf(0)
        hi = mp.inf
        for b, d in zip(base, direction):
            if d > 0:
                hi = min(hi, b / d)
            elif d < 0:
                lo = max(lo, b / d)
            elif b <= 0:
                raise ValueError("no positive histogram interval")
        if not (lo < hi and hi > 0):
            raise ValueError("no positive histogram interval")
        hidden_weight = (max(lo, 0) + hi) / 2
        weights = [base[i] - hidden_weight * direction[i] for i in range(n_alpha + 1)]
        weights.append(hidden_weight)
        ms = solved_ms + [hidden]
        targets_out = mp.matrix([+targets[i] for i in range(n_alpha)])
    return ms, [+w for w in weights], targets_out


def calibrated_rho_profile(N, labeled_alphas, P_builder):
    rows = []
    for label, a in labeled_alphas:
        expected = cached_sprinkle_pair_density_expectation(N, a)
        rho = P_builder(a) / expected
        rows.append((label, a, rho))
    return rows


def profile_max_log_gap(profile):
    return max(abs(mp.log(rho)) for _, _, rho in profile)


def profile_max_abs_gap(profile):
    return max(abs(rho - 1) for _, _, rho in profile)


def profile_text(profile):
    return " ".join(f"rho({label})={fmt(rho, 12)}" for label, _, rho in profile)


def histogram_moment_profile(N, ms, weights, labeled_alphas):
    rows = []
    for label, alpha in labeled_alphas:
        moment_density = sum(w * mp.e ** (-alpha * m) for m, w in zip(ms, weights)) / N
        expected = cached_sprinkle_pair_density_expectation(N, alpha)
        rows.append((label, alpha, moment_density / expected))
    return rows


def fit_height_exponent(metric_fn, sizes, alpha, p=None):
    Ns = []
    Hs = []
    for s in sizes:
        if p is None:
            m = metric_fn(s, alpha)
        else:
            m = metric_fn(s, p, alpha)
        Ns.append(mp.log(m["N"]))
        Hs.append(mp.log(m["height"]))
    return linreg_slope(Ns, Hs)


def fit_P_exponent(metric_fn, sizes, alpha, p=None):
    Ns = []
    Ps = []
    for s in sizes:
        if p is None:
            m = metric_fn(s, alpha)
        else:
            m = metric_fn(s, p, alpha)
        if m["P"] <= 0:
            continue
        Ns.append(mp.log(m["N"]))
        Ps.append(mp.log(m["P"]))
    if len(Ns) < 2:
        return mp.nan
    return linreg_slope(Ns, Ps)


def fit_sprinkled_exponents(sizes, alpha, seed0=8675309):
    metrics = [sprinkled2_metrics(s, alpha, seed0 + int(s)) for s in sizes]
    beta_h = linreg_slope([mp.log(m["N"]) for m in metrics], [mp.log(m["height"]) for m in metrics])
    beta_p = linreg_slope([mp.log(m["N"]) for m in metrics], [mp.log(m["P"]) for m in metrics])
    return metrics, beta_h, beta_p


def fit_kr_retuned_P_exponent(sizes, target_r, alpha):
    Ns = []
    Ps = []
    ps = []
    for s in sizes:
        p = solve_kr_p_for_r(s, target_r)
        m = kr_expected_metrics(s, p, alpha)
        Ns.append(mp.log(m["N"]))
        Ps.append(mp.log(m["P"]))
        ps.append(p)
    return linreg_slope(Ns, Ps), ps


def solve_kr_p_for_r(t, target_r):
    lo = mp.mpf("0")
    hi = mp.mpf("1")
    for _ in range(500):
        mid = (lo + hi) / 2
        rmid = kr_expected_metrics(t, mid, mp.mpf("1"))["r"]
        if rmid < target_r:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def toy_audit_pass(m, beta_h, beta_P, target_d=2):
    """A deliberately finite 2D benchmark audit, not a theorem.

    Conditions:
      - MM dimension close to target 2.
      - height exponent close to 1/2.
      - interval-damped pair density P is nonzero, finite, and approximately tight
        across scales (beta_P near 0).

    The later sprinkled stress sample proves this toy audit is not a general
    manifoldlikeness criterion.
    """
    d_mm = mm_inv(m["r"])
    return (
        abs(d_mm - target_d) < mp.mpf("0.20")
        and abs(beta_h - mp.mpf("0.5")) < mp.mpf("0.12")
        and m["P"] > mp.mpf("0.1")
        and abs(beta_P) < mp.mpf("0.20")
    )


print("=" * 80)
print("P22 marked compensator / manifoldlikeness finite stress tests")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

alpha = mp.log(2)
print("alpha for interval-damped pair density P_alpha =", fmt(alpha, 40))

print("\n(1) Scalar compensator is blind to order at fixed N")
kappa = mp.mpf("0.73")
N_fixed = mp.mpf(256)
scalar_A = {
    "grid": kappa * N_fixed,
    "chain": kappa * N_fixed,
    "antichain": kappa * N_fixed,
    "KR": kappa * N_fixed,
}
for name, val in scalar_A.items():
    print(f"{name:10s} A_N = {fmt(val, 30)}")
check(
    "Scalar compensator cannot distinguish orders at fixed N",
    len(set(str(v) for v in scalar_A.values())) == 1,
    f"A_N={fmt(kappa*N_fixed, 30)}",
)

print("\n(2) Myrheim-Meyer reference values")
refs = {1: mm_f(1), 2: mm_f(2), 3: mm_f(3), 4: mm_f(4)}
for d, val in refs.items():
    print(f"f({d}) = {fmt(val, 50)}")
check("MM f(1)=1", abs(refs[1] - 1) < mp.mpf("1e-120"), f"gap={fmt(abs(refs[1]-1), 8)}")
check("MM f(2)=1/2", abs(refs[2] - mp.mpf(1) / 2) < mp.mpf("1e-120"), f"gap={fmt(abs(refs[2]-mp.mpf(1)/2), 8)}")
check("MM f(3)=8/35", abs(refs[3] - mp.mpf(8) / 35) < mp.mpf("1e-120"), f"gap={fmt(abs(refs[3]-mp.mpf(8)/35), 8)}")
check("MM f(4)=1/10", abs(refs[4] - mp.mpf(1) / 10) < mp.mpf("1e-120"), f"gap={fmt(abs(refs[4]-mp.mpf(1)/10), 8)}")
check("MM inverse returns d=2", abs(mm_inv(refs[2]) - 2) < mp.mpf("1e-40"), f"gap={fmt(abs(mm_inv(refs[2])-2), 8)}")

print("\n(3) Family diagnostics")
grid_sizes = [16, 32, 64, 128]
chain_sizes = [256, 1024, 4096, 16384]
kr_t_sizes = [64, 128, 256, 512]

grid = grid2_metrics(64, alpha)
chain = chain_metrics(4096, alpha)
anti = antichain_metrics(4096, alpha)
kr = kr_expected_metrics(256, mp.mpf("0.5"), alpha)

beta_grid_h = fit_height_exponent(grid2_metrics, grid_sizes, alpha)
beta_chain_h = fit_height_exponent(chain_metrics, chain_sizes, alpha)
beta_anti_h = fit_height_exponent(antichain_metrics, chain_sizes, alpha)
beta_kr_h = fit_height_exponent(kr_expected_metrics, kr_t_sizes, alpha, p=mp.mpf("0.5"))

beta_grid_P = fit_P_exponent(grid2_metrics, grid_sizes, alpha)
beta_chain_P = fit_P_exponent(chain_metrics, chain_sizes, alpha)
beta_kr_P = fit_P_exponent(kr_expected_metrics, kr_t_sizes, alpha, p=mp.mpf("0.5"))

families = [
    ("grid2", grid, beta_grid_h, beta_grid_P),
    ("chain", chain, beta_chain_h, beta_chain_P),
    ("antichain", anti, beta_anti_h, mp.nan),
    ("KR p=1/2", kr, beta_kr_h, beta_kr_P),
]
for name, m, bh, bP in families:
    dmm = mm_inv(m["r"])
    print(
        f"{name:10s} N={fmt(m['N'], 8):>8s} r={fmt(m['r'], 18):>22s} "
        f"dMM={fmt(dmm, 14):>16s} H={fmt(m['height'], 8):>8s} "
        f"beta_H={fmt(bh, 14):>16s} P={fmt(m['P'], 18):>22s} "
        f"beta_P={fmt(bP, 14):>16s}"
    )

check("Deterministic 2D grid benchmark has height exponent near 1/2", abs(beta_grid_h - mp.mpf("0.5")) < mp.mpf("0.08"), f"beta={fmt(beta_grid_h, 20)}")
check("Chain has height exponent near 1", abs(beta_chain_h - 1) < mp.mpf("1e-40"), f"beta={fmt(beta_chain_h, 20)}")
check("KR has height exponent near 0", abs(beta_kr_h) < mp.mpf("0.02"), f"beta={fmt(beta_kr_h, 20)}")
check("Antichain has height exponent 0", abs(beta_anti_h) < mp.mpf("1e-40"), f"beta={fmt(beta_anti_h, 20)}")
check("Deterministic 2D grid interval-damped pair density is tight", abs(beta_grid_P) < mp.mpf("0.08"), f"beta_P={fmt(beta_grid_P, 20)}")
check("KR interval-damped pair density diverges with N", beta_kr_P > mp.mpf("0.85"), f"beta_P={fmt(beta_kr_P, 20)}")
check("Antichain has zero interval-damped pair density", anti["P"] == 0, f"P={fmt(anti['P'], 8)}")

print("\n(4) KR can spoof a single MM dimension estimator in expected family")
t_spoof = 256
p_star = solve_kr_p_for_r(t_spoof, refs[2])
kr_spoof = kr_expected_metrics(t_spoof, p_star, alpha)
kr_spoof_beta_h = fit_height_exponent(kr_expected_metrics, kr_t_sizes, alpha, p=p_star)
kr_spoof_beta_P_fixed = fit_P_exponent(kr_expected_metrics, kr_t_sizes, alpha, p=p_star)
kr_spoof_beta_P_retuned, kr_retuned_ps = fit_kr_retuned_P_exponent(kr_t_sizes, refs[2], alpha)
bridge_defect = (1 - p_star * p_star) ** (2 * t_spoof)
print("t =", t_spoof, "N =", int(4 * t_spoof))
print("p_star solving E[r_KR]=f(2) to receipt precision =", fmt(p_star, 60))
print("bridge unsaturation defect at displayed p_star =", fmt(bridge_defect, 60))
print("r_KR(p_star) to receipt precision =", fmt(kr_spoof["r"], 60))
print("dMM_KR(p_star) =", fmt(mm_inv(kr_spoof["r"]), 40))
print("height exponent =", fmt(kr_spoof_beta_h, 40))
print("fixed-p interval-damped pair exponent =", fmt(kr_spoof_beta_P_fixed, 40))
print("retuned-p interval-damped pair exponent =", fmt(kr_spoof_beta_P_retuned, 40))
for t, p in zip(kr_t_sizes, kr_retuned_ps):
    print(f"  retuned p(t={t}) = {fmt(p, 40)}")
check("KR spoof has p_star in (0,1)", 0 < p_star < 1, f"p={fmt(p_star, 30)}")
check("KR spoof matches 2D ordering fraction to receipt precision", abs(kr_spoof["r"] - refs[2]) < mp.mpf("1e-80"), f"gap={fmt(abs(kr_spoof['r']-refs[2]), 8)}")
check("KR spoof has dMM=2 to receipt precision but height exponent near 0", abs(mm_inv(kr_spoof["r"]) - 2) < mp.mpf("1e-30") and abs(kr_spoof_beta_h) < mp.mpf("0.02"), f"dMM={fmt(mm_inv(kr_spoof['r']), 20)}, beta_H={fmt(kr_spoof_beta_h, 20)}")
check("Retuned KR spoof still has divergent interval-damped pair density", kr_spoof_beta_P_retuned > mp.mpf("0.85"), f"beta_P={fmt(kr_spoof_beta_P_retuned, 20)}")

print("\n(5) Single diagnostics vs toy combined benchmark audit")
grid_pass = toy_audit_pass(grid, beta_grid_h, beta_grid_P)
chain_pass = toy_audit_pass(chain, beta_chain_h, beta_chain_P)
anti_pass = toy_audit_pass(anti, beta_anti_h, mp.nan)
kr_pass = toy_audit_pass(kr, beta_kr_h, beta_kr_P)
kr_spoof_pass = toy_audit_pass(kr_spoof, kr_spoof_beta_h, kr_spoof_beta_P_retuned)

mm_only_grid = abs(mm_inv(grid["r"]) - 2) < mp.mpf("0.20")
mm_only_spoof = abs(mm_inv(kr_spoof["r"]) - 2) < mp.mpf("0.20")
pair_only_grid = grid["P"] > mp.mpf("0.1") and abs(beta_grid_P) < mp.mpf("0.20")
pair_only_chain = chain["P"] > mp.mpf("0.1") and abs(beta_chain_P) < mp.mpf("0.20")

print("MM-only accepts grid?", mm_only_grid, "MM-only accepts spoofed KR?", mm_only_spoof)
print("Pair-density-only accepts grid?", pair_only_grid, "Pair-density-only accepts chain?", pair_only_chain)
print("Toy audit grid/chain/antichain/KR/spoofedKR =", grid_pass, chain_pass, anti_pass, kr_pass, kr_spoof_pass)
check("MM-only diagnostic is insufficient because spoofed KR passes", mm_only_grid and mm_only_spoof, "")
check("Pair-density-only diagnostic is insufficient because chain passes", pair_only_grid and pair_only_chain, "")
check("Toy combined audit accepts deterministic 2D grid benchmark", grid_pass, "")
check("Toy combined audit rejects chain, antichain, KR, and spoofed KR", (not chain_pass) and (not anti_pass) and (not kr_pass) and (not kr_spoof_pass), "")

print("\n(6) Fixed 1+1 binomial-sprinkling stress sample")
spr_sizes = [128, 256, 512, 1024]
spr_metrics, spr_beta_h, spr_beta_P = fit_sprinkled_exponents(spr_sizes, alpha)
spr_expected = [sprinkle_pair_density_expectation(int(m["N"]), alpha) for m in spr_metrics]
for m in spr_metrics:
    expected = spr_expected[spr_metrics.index(m)]
    rho = m["P"] / expected
    print(
        f"sprinkle2  N={fmt(m['N'], 8):>8s} r={fmt(m['r'], 18):>22s} "
        f"dMM={fmt(mm_inv(m['r']), 14):>16s} H={fmt(m['height'], 8):>8s} "
        f"P={fmt(m['P'], 18):>22s} E[P]={fmt(expected, 18):>22s} "
        f"rho={fmt(rho, 12):>14s}"
    )
spr_last = spr_metrics[-1]
spr_toy_pass = toy_audit_pass(spr_last, spr_beta_h, spr_beta_P)
spr_rhos = [m["P"] / e for m, e in zip(spr_metrics, spr_expected)]
print("sprinkle beta_H =", fmt(spr_beta_h, 40))
print("sprinkle beta_P =", fmt(spr_beta_P, 40))
print("toy audit accepts fixed sprinkled stress sample?", spr_toy_pass)
check("Fixed sprinkled stress sample has MM dimension near 2 at largest N", abs(mm_inv(spr_last["r"]) - 2) < mp.mpf("0.20"), f"dMM={fmt(mm_inv(spr_last['r']), 20)}")
check("Fixed sprinkled stress sample has height exponent near 1/2", abs(spr_beta_h - mp.mpf("0.5")) < mp.mpf("0.18"), f"beta_H={fmt(spr_beta_h, 20)}")
check("Naive tight pair-density threshold fails on fixed sprinkled stress sample", spr_beta_P > mp.mpf("0.20"), f"beta_P={fmt(spr_beta_P, 20)}")
check("Toy audit is not a manifoldlikeness gate because it rejects the sprinkled stress sample", not spr_toy_pass, "")
check("Calibrated sprinkled pair density P/E[P] stays near 1", max(abs(r - 1) for r in spr_rhos) < mp.mpf("0.08"), f"max_gap={fmt(max(abs(r - 1) for r in spr_rhos), 20)}")

print("\n(6b) Small sprinkling ensemble bands for calibrated rho")
ensemble_sizes = [128, 256, 512]
ensemble_reps = 8
ensemble_max_gap = mp.mpf(0)
for N in ensemble_sizes:
    expected = sprinkle_pair_density_expectation(N, alpha)
    rhos = []
    for rep in range(ensemble_reps):
        m = sprinkled2_metrics(N, alpha, 24681357 + 1000 * N + rep)
        rhos.append(m["P"] / expected)
    mean_rho = sum(rhos) / len(rhos)
    min_rho = min(rhos)
    max_rho = max(rhos)
    sd_rho = mp.sqrt(sum((r - mean_rho) ** 2 for r in rhos) / len(rhos))
    ensemble_max_gap = max(ensemble_max_gap, max(abs(min_rho - 1), abs(max_rho - 1)))
    print(
        f"N={N:4d} reps={ensemble_reps} rho_mean={fmt(mean_rho, 18)} "
        f"rho_sd={fmt(sd_rho, 12)} rho_min={fmt(min_rho, 12)} rho_max={fmt(max_rho, 12)}"
    )
check("Small sprinkling ensemble rho band stays near 1", ensemble_max_gap < mp.mpf("0.12"), f"max_gap={fmt(ensemble_max_gap, 20)}")

print("\n(7) Adversarial non-manifold MM+height spoof")
adv_ns = [32, 64, 128]
adv_metrics = [bilayer_chain_spoof_metrics(n, alpha) for n in adv_ns]
adv_beta_h = linreg_slope([mp.log(m["N"]) for m in adv_metrics], [mp.log(m["height"]) for m in adv_metrics])
for m in adv_metrics:
    expected = sprinkle_pair_density_expectation(int(m["N"]), alpha)
    rho = m["P"] / expected
    print(
        f"bilayer+chain N={fmt(m['N'], 8):>8s} r={fmt(m['r'], 18):>22s} "
        f"dMM={fmt(mm_inv(m['r']), 14):>16s} H={fmt(m['height'], 8):>8s} "
        f"beta_H={fmt(adv_beta_h, 14):>16s} P={fmt(m['P'], 18):>22s} "
        f"E[P]={fmt(expected, 18):>22s} rho={fmt(rho, 14):>16s}"
    )
adv_last = adv_metrics[-2]  # N=4096: strong but keeps expectation guard modest.
adv_expected = sprinkle_pair_density_expectation(int(adv_last["N"]), alpha)
adv_rho = adv_last["P"] / adv_expected
check("Adversary has MM dimension near 2 at N=4096", abs(mm_inv(adv_last["r"]) - 2) < mp.mpf("0.08"), f"dMM={fmt(mm_inv(adv_last['r']), 20)}")
check("Adversary has height exponent exactly near 1/2", abs(adv_beta_h - mp.mpf("0.5")) < mp.mpf("1e-40"), f"beta_H={fmt(adv_beta_h, 20)}")
check("Calibrated pair density rejects MM+height adversary", adv_rho > mp.mpf("50"), f"rho={fmt(adv_rho, 20)}")

print("\n(8) Thin-middle adversary spoofs single-alpha rho")
alpha_profile = [mp.log(mp.mpf("1.5")), mp.log(2), mp.log(3)]
thin_ns = [32, 64, 128]
thin_rows = []
for n in thin_ns:
    N = n * n
    expected_mid = sprinkle_pair_density_expectation(N, alpha)
    _, middle, m_mid, rho_mid = tune_thin_middle(n, alpha, expected_mid)
    profile = []
    for a_prof in alpha_profile:
        m_prof = thin_middle_chain_spoof_metrics(n, middle, a_prof)
        e_prof = sprinkle_pair_density_expectation(N, a_prof)
        profile.append((a_prof, m_prof["P"] / e_prof))
    thin_rows.append((n, middle, m_mid, rho_mid, profile))
    thin_profile_text = " ".join(f"rho(alpha={fmt(a, 8)})={fmt(r, 12)}" for a, r in profile)
    print(
        f"thin-middle N={N:6d} middle={middle:3d} r={fmt(m_mid['r'], 18)} "
        f"dMM={fmt(mm_inv(m_mid['r']), 14)} H={fmt(m_mid['height'], 8)} "
        f"rho_mid={fmt(rho_mid, 14)} {thin_profile_text}"
    )
thin_mid_row = thin_rows[1]  # N=4096
thin_profile_gaps = [abs(r - 1) for _, r in thin_mid_row[4]]
check("Thin-middle adversary has MM dimension near 2 at N=4096", abs(mm_inv(thin_mid_row[2]["r"]) - 2) < mp.mpf("0.08"), f"dMM={fmt(mm_inv(thin_mid_row[2]['r']), 20)}")
check("Thin-middle adversary has height exponent 1/2 by construction", thin_mid_row[2]["height"] == mp.sqrt(thin_mid_row[2]["N"]), f"H={fmt(thin_mid_row[2]['height'], 20)}")
check("Thin-middle adversary spoofs single-alpha calibrated rho", abs(thin_mid_row[3] - 1) < mp.mpf("0.05"), f"rho_mid={fmt(thin_mid_row[3], 20)}")
check("Multi-alpha rho profile exposes thin-middle adversary", max(thin_profile_gaps) > mp.mpf("0.10"), f"max_gap={fmt(max(thin_profile_gaps), 20)}")

print("\n(9) Wider calibrated interval generating-function profile")
wide_alpha_profile = [
    ("log1.25", mp.log(mp.mpf("1.25"))),
    ("log1.5", mp.log(mp.mpf("1.5"))),
    ("log2", mp.log(2)),
    ("log3", mp.log(3)),
    ("log4", mp.log(4)),
]
wide_N = 1024
wide_n = 32
wide_spr_hist = sprinkled2_interval_histogram(wide_N, 8675309 + wide_N)
wide_spr_profile = calibrated_rho_profile(
    wide_N,
    wide_alpha_profile,
    lambda a: P_from_histogram(wide_N, wide_spr_hist["hist"], a),
)
wide_chain_profile = calibrated_rho_profile(
    wide_N,
    wide_alpha_profile,
    lambda a: chain_metrics(wide_N, a)["P"],
)
wide_bilayer_profile = calibrated_rho_profile(
    wide_N,
    wide_alpha_profile,
    lambda a: bilayer_chain_spoof_metrics(wide_n, a)["P"],
)
wide_thin_middle = thin_rows[0][1]
wide_thin_profile = calibrated_rho_profile(
    wide_N,
    wide_alpha_profile,
    lambda a: thin_middle_chain_spoof_metrics(wide_n, wide_thin_middle, a)["P"],
)
for label, profile in [
    ("sprinkled", wide_spr_profile),
    ("chain", wide_chain_profile),
    ("bilayer+chain", wide_bilayer_profile),
    ("thin-middle", wide_thin_profile),
]:
    print(
        f"{label:14s} max_log_gap={fmt(profile_max_log_gap(profile), 14)} "
        f"{profile_text(profile)}"
    )
check("Fixed sprinkled wide generating profile stays near 1", profile_max_log_gap(wide_spr_profile) < mp.mpf("0.05"), f"max_log_gap={fmt(profile_max_log_gap(wide_spr_profile), 20)}")
check("Wide generating profile rejects chain", profile_max_log_gap(wide_chain_profile) > mp.mpf("1.0"), f"max_log_gap={fmt(profile_max_log_gap(wide_chain_profile), 20)}")
check("Wide generating profile rejects bilayer-plus-chain adversary", profile_max_log_gap(wide_bilayer_profile) > mp.mpf("2.0"), f"max_log_gap={fmt(profile_max_log_gap(wide_bilayer_profile), 20)}")
check("Wide generating profile rejects thin-middle single-alpha spoof", profile_max_log_gap(wide_thin_profile) > mp.mpf("1.0"), f"max_log_gap={fmt(profile_max_log_gap(wide_thin_profile), 20)}")

print("\n(10) Finite generating-function profiles are interval-histogram underdetermined")
hist_N = 4096
hist_alpha_profile = wide_alpha_profile
hist_ms, hist_weights, hist_targets = solve_histogram_moment_match(
    hist_N,
    [a for _, a in hist_alpha_profile],
    free_m=8,
    hidden_m=1000,
)
hist_target_rel = mp.mpf(hist_N * (hist_N - 1)) / 4
hist_moment_gaps = []
for (label, a_prof), target in zip(hist_alpha_profile, hist_targets):
    moment = sum(w * mp.e ** (-a_prof * m) for m, w in zip(hist_ms, hist_weights))
    hist_moment_gaps.append(abs(moment - target))
    print(
        f"{label:7s} alpha={fmt(a_prof, 12)} target_count={fmt(target, 18)} "
        f"matched_count={fmt(moment, 18)} gap={fmt(abs(moment-target), 8)}"
    )
hist_profile = histogram_moment_profile(hist_N, hist_ms, hist_weights, hist_alpha_profile)
print("histogram thicknesses =", hist_ms)
print("histogram weights =", [fmt(w, 18) for w in hist_weights])
print("target relation count for r=1/2 =", fmt(hist_target_rel, 18))
print("histogram total relation weight =", fmt(sum(hist_weights), 18))
print("hidden large-interval fraction =", fmt(hist_weights[-1] / sum(hist_weights), 18))
print("histogram calibrated profile =", profile_text(hist_profile))
check("Histogram moment adversary has positive weights", all(w > 0 for w in hist_weights), "")
check("Histogram moment adversary matches all tested alpha moments", max(hist_moment_gaps) < mp.mpf("1e-80"), f"max_gap={fmt(max(hist_moment_gaps), 20)}")
check("Histogram moment adversary preserves target related-pair count", abs(sum(hist_weights) - hist_target_rel) < mp.mpf("1e-40"), f"gap={fmt(abs(sum(hist_weights)-hist_target_rel), 20)}")
check("Most histogram relation mass is hidden beyond tested interval scales", hist_weights[-1] / sum(hist_weights) > mp.mpf("0.90"), f"hidden_fraction={fmt(hist_weights[-1]/sum(hist_weights), 20)}")
check("Finite five-alpha profile can be moment-spoofed to receipt precision", profile_max_log_gap(hist_profile) < mp.mpf("1e-80"), f"max_log_gap={fmt(profile_max_log_gap(hist_profile), 20)}")

print("\n(11) Complete-sandwich realization pays a transitivity tax")
hidden_mass = hist_weights[-1]
hidden_interval = mp.mpf(hist_ms[-1])
min_cover_tax = 2 * hidden_interval * mp.sqrt(hidden_mass)
min_vertices = hidden_interval + 2 * mp.sqrt(hidden_mass)
tax_density = min_cover_tax / hist_N
mid_expected_density = sprinkle_pair_density_expectation(hist_N, alpha)
print("hidden large-interval mass =", fmt(hidden_mass, 24))
print("hidden interval size =", fmt(hidden_interval, 12))
print("same-N sandwich minimum vertices m + 2*sqrt(hidden_mass) =", fmt(min_vertices, 24))
print("continuous lower bound 2*m*sqrt(hidden_mass) =", fmt(min_cover_tax, 24))
print("tax density lower bound =", fmt(tax_density, 24))
print("sprinkling E[P_alpha] at alpha=log2 =", fmt(mid_expected_density, 24))
print("tax / E[P_alpha] =", fmt(tax_density / mid_expected_density, 24))
check("Complete-sandwich realization cannot fit the same N vertex budget", min_vertices > hist_N, f"min_vertices={fmt(min_vertices, 20)}")
check("Complete-sandwich realization would create huge low-interval tax", tax_density / mid_expected_density > mp.mpf("50"), f"ratio={fmt(tax_density / mid_expected_density, 20)}")

print("\n(12) Split complete-sandwich reservoirs do not lower the tax bound")
split_tax_ratios = []
for split_count in [2, 4, 16]:
    equal_split_tax = mp.mpf(split_count) * 2 * hidden_interval * mp.sqrt(hidden_mass / split_count)
    ratio_to_single = equal_split_tax / min_cover_tax
    split_tax_ratios.append(ratio_to_single)
    print(
        f"equal split count={split_count:2d} tax/single_tax={fmt(ratio_to_single, 24)} "
        f"tax/E[P]={fmt((equal_split_tax / hist_N) / mid_expected_density, 24)}"
    )
check("Independent split-sandwich reservoirs cannot lower the complete-sandwich tax bound", min(split_tax_ratios) > 1, f"min_ratio={fmt(min(split_tax_ratios), 20)}")

print("\n" + "=" * 80)
passed = sum(1 for _, ok, _ in checks if ok)
total = len(checks)
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")
print(f"\nCHECKS PASSED: {passed}/{total}")
if passed != total:
    raise SystemExit(1)
print("DONE.")
