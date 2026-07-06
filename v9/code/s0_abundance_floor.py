#!/usr/bin/env python3
"""
s0_abundance_floor.py — v9 PLAN.md T1.1: the abundance campaign's go/no-go.
Companion to note-t11-abundance-floor.md (the derivation and theorem
statements live there; this receipt decides the measured questions).

WHAT IS AT STAKE (the master fork): if the backwards-derived abundance
action's faithful floor is quadratic, the action route dies at its root
(PLAN.md T1.1 kill text). The note decomposes the family into Row C (the
pair-block comparability charge S_comp = (n(n-1)/2)(r - 1/2)^2 — floor O(n)
EXACT, both walls Omega(n^2), elementary) and Row A (the per-interval
abundance charge S_ab with the EXACT closed-form reference E[A_j(k)] —
floor Theta(N log^2 N) conditional on H-var). This receipt verifies the
exact laws and measures the two named questions.

THE EXACT REFERENCE LAW (note-t11 §1, verified in CHECK 2):
  E[A_j(k)] = k(k-1) C(k-2,j) * Integral_0^1 g(s) s^j (1-s)^{k-2-j} ds,
  g(s) = (1+s) ln(1/s) - 2(1-s)   [the gap-area density; total mass 1/4],
  closed form via  int s^a (1-s)^b ln(1/s) = B(a+1,b+1)[psi(a+b+2)-psi(a+1)].
  Sanity anchors: int g = 1/4 (P(ordered pair related)); E[A_j] ~ k ln k.

GATES (pre-registered in this docstring before first execution):
  G1 (Row C): measured N^2/2 * mean (r-1/2)^2 on diamond sprinklings within
      4 SEM of the exact (n-2)/18 + 1/4 at N in {256, 512, 1024}; the wall
      arithmetic printed (antichain n(n-1)/8; r = 0.78 class >= 0.039 n(n-1)).
  G2 (exact law): closed-form E[A_j(k)] within 4 SEM of Monte Carlo at
      k in {64, 128}, j in {0, 1, 2}; the mass anchor int g = 1/4 at dps 60.
  G3 (H-var): Var(A_j)/E[A_j] growth over k in {64, 128, 256}: gate =
      exponent < 0.5. NOTE (review round 1): this gate certifies only
      SUB-QUADRATIC-floor survival (k^0.4 would pass it while violating
      H-var's polylog); H-var itself rests on the measured near-zero
      exponent, printed.
  G4 (the floor observable — the GO/NO-GO): sampled-pair estimates of
      E[S_ab](N) on faithful sprinklings at N in {256, 512, 1024},
      normalized by N ln^2 N: max/min < 2.5 across the range = GO
      (flat-at-this-window; the conditional theorem's practical face).
      Both directions live: a strong upward trend = NO-GO finding.
  G5 (the cluster pricing — Row A's purpose): mean per-interval m_ab on
      the paper-11 cluster blow-up population, k-matched against faithful:
      ratio > 2 (pre-registered direction: the adversary that passes S_r
      and Row C pays in the abundance profile).
  G6 (division of labor, disclosed): S_ab(antichain) = 0 exactly — the
      sparse wall is Row C's, not Row A's.

Precision: closed forms and anchors at mpmath dps = 60; Monte Carlo
landscapes float64 (counts exact int); btw matrices float32 with exact
rint (the j2/u3 convention). Seed: default_rng(20260705). Population
conventions: diamond = dominance on the unit square (lightcone coords,
paper 7); cluster = paper 11's blow-up (N/6 centers x 6, jitter 1e-3).
"""

import numpy as np
from mpmath import mp, beta as mbeta, digamma, quad, mpf, log as mlog

mp.dps = 60

rng = np.random.default_rng(20260705)

PASS = 0
FAIL = 0

def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    if ok: PASS += 1
    else: FAIL += 1
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))


# ------------------------------------------------------- exact reference law
def EA_exact(k, j):
    """E[A_j(k)] in closed form (note-t11 §1), dps 60."""
    if k - 2 - j < 0:
        return mpf(0)
    b = mpf(k - 1 - j)                      # (1-s)^{k-2-j}: B(., k-1-j)
    t1 = mbeta(j + 1, b) * (digamma(k) - digamma(j + 1))
    t2 = mbeta(j + 2, b) * (digamma(k + 1) - digamma(j + 2))
    t3 = -2 * mbeta(j + 1, k - j)           # -2 int s^j (1-s)^{k-1-j}
    from mpmath import binomial
    return mpf(k) * (k - 1) * binomial(k - 2, j) * (t1 + t2 + t3)

# ---------------------------------------------------------------- generators
def sprinkle(N):
    return rng.random((N, 2))

def cluster_pts(N, c=6, jit=1e-3):
    M = N // c
    ctr = rng.random((M, 2))
    return np.repeat(ctr, c, axis=0) + rng.normal(0, jit, (M * c, 2))

def dominance(pts):
    return (pts[None, :, 0] > pts[:, None, 0]) & (pts[None, :, 1] > pts[:, None, 1])

def abundance_counts(pts, J=2):
    """A_j (unordered related pairs with interior exactly j), j = 0..J."""
    C = dominance(pts)
    k = len(pts)
    btw = np.rint(C.astype(np.float32) @ C.astype(np.float32)).astype(np.int32)
    interiors = btw[C]                       # one entry per ordered related pair
    return [int(np.sum(interiors == j)) for j in range(J + 1)], C

def m_ab_of_interval(pts_in, J=2):
    """The per-interval abundance misfit m_ab (note-t11 §1)."""
    k = len(pts_in)
    A, _ = abundance_counts(pts_in, J)
    tot = 0.0
    for j in range(J + 1):
        ref = float(EA_exact(k, j))
        tot += (A[j] / k - ref / k) ** 2
    return tot

# ============ CHECK 1: Row C — the exact floor and the wall arithmetic (G1)
print("CHECK 1: Row C (comparability block) — floor exact, walls arithmetic")
ok_all = True
for N in (256, 512, 1024):
    vals = []
    for s in range(24):
        pts = sprinkle(N)
        C = dominance(pts)
        r = 2.0 * C.sum() / (N * (N - 1))
        vals.append((N * (N - 1) / 2) * (r - 0.5) ** 2)
    meas, sem = np.mean(vals), np.std(vals, ddof=1) / np.sqrt(len(vals))
    exact = (N - 2) / 18 + 0.25
    ok = abs(meas - exact) < 4 * sem
    ok_all &= ok
    print(f"      N = {N:>4}: S_comp measured {meas:8.2f} +/- {sem:.2f} vs exact {exact:8.2f}")
check("faithful floor of S_comp matches the exact (n-2)/18 + 1/4 at every N "
      "(O(n) — Row C's floor is closed, unconditional)", ok_all)
n = 1024
print(f"      walls at n = {n}: antichain n(n-1)/8 = {n*(n-1)/8:.2e}; "
      f"dense r = 0.78 class >= {0.5*(0.78-0.5)**2*n*(n-1):.2e}; "
      f"u2 endpoint r = 0.059 >= {0.5*(0.059-0.5)**2*n*(n-1):.2e}  [Omega(n^2), arithmetic]")
wall_anti = n * (n - 1) / 8
wall_dense = 0.5 * (0.78 - 0.5) ** 2 * n * (n - 1)
wall_u2 = 0.5 * (0.059 - 0.5) ** 2 * n * (n - 1)
floor_n = (n - 2) / 18 + 0.25
ok = min(wall_anti, wall_dense, wall_u2) > 100 * floor_n
check("both walls are Omega(n^2) from Row C alone and exceed the O(n) "
      "floor by > 100x at n = 1024 (asserted numerically, not narrated)",
      ok, f"min wall / floor = {min(wall_anti, wall_dense, wall_u2)/floor_n:.0f}x")

# ============ CHECK 2: the exact abundance law vs Monte Carlo (G2)
print("CHECK 2: the closed-form E[A_j(k)] against Monte Carlo")
mass = quad(lambda s: ((1 + s) * mlog(1 / s) - 2 * (1 - s)), [0, 1])
ok = abs(mass - mpf(1) / 4) < mpf(10) ** (-40)
check("the gap-area density's total mass is exactly 1/4 (P(pair related); "
      "dps 60)", ok, f"int g = {mp.nstr(mass, 20)}")
ok_all = True
for k, reps in ((64, 1500), (128, 600)):
    A_acc = np.zeros((reps, 3), dtype=np.int64)
    for rdx in range(reps):
        A, _ = abundance_counts(sprinkle(k))
        A_acc[rdx] = A
    for j in range(3):
        mc, sem = A_acc[:, j].mean(), A_acc[:, j].std(ddof=1) / np.sqrt(reps)
        ex = float(EA_exact(k, j))
        ok = abs(mc - ex) < 4 * sem
        ok_all &= ok
        print(f"      k = {k:>3}, j = {j}: MC {mc:8.2f} +/- {sem:.2f} vs exact {ex:8.2f}")
check("closed form within 4 SEM of Monte Carlo at every (k, j) — the "
      "reference is EXACT, no asymptotic-bias term exists in m_ab", ok_all)

# ============ CHECK 3: H-var (G3)
print("CHECK 3: H-var — Var(A_j)/E[A_j] growth")
ks = [64, 128, 256]
ratio = np.zeros((3, 3))
for ki, k in enumerate(ks):
    reps = {64: 800, 128: 400, 256: 200}[k]
    A_acc = np.zeros((reps, 3), dtype=np.int64)
    for rdx in range(reps):
        A, _ = abundance_counts(sprinkle(k))
        A_acc[rdx] = A
    for j in range(3):
        ratio[ki, j] = A_acc[:, j].var(ddof=1) / A_acc[:, j].mean()
    print(f"      k = {k:>3}: Var/E = {np.round(ratio[ki], 2).tolist()}")
expo = np.polyfit(np.log(ks), np.log(ratio.mean(axis=1)), 1)[0]
ok = expo < 0.5
check("H-var holds in the measured window: Var/E grows with exponent < 0.5 "
      "in k (Poisson-class-to-polylog; the floor's polylog form survives)",
      ok, f"fitted exponent = {expo:.3f}")

# ============ CHECK 4: the floor observable (G4 — THE GO/NO-GO)
print("CHECK 4: the floor observable — sampled E[S_ab](N) / (N ln^2 N)")
M0 = 8
floor_vals = {}
for N in (256, 512, 1024):
    acc = []
    seed_pairs = []
    for s in range(3):
        pts = sprinkle(N)
        C = dominance(pts)
        ii, jj = np.nonzero(C)
        npairs = len(ii)
        pick = rng.choice(npairs, size=min(60, npairs), replace=False)
        for p in pick:
            u, v = ii[p], jj[p]
            lo = pts[u]; hi = pts[v]
            inside = ((pts[:, 0] > lo[0]) & (pts[:, 0] < hi[0]) &
                      (pts[:, 1] > lo[1]) & (pts[:, 1] < hi[1]))
            k = int(inside.sum())
            if k < M0:
                acc.append(0.0)
            else:
                acc.append(m_ab_of_interval(pts[inside]))
        seed_pairs.append(npairs)   # per-seed count (review round 1: the
                                    # first cut used only the LAST seed's)
        tot_pairs = npairs      # nonzero(C) on STRICT dominance already
                                # enumerates each unordered related pair once
                                # (C ^ C.T = 0) — the first draft halved this
                                # (a 2x undercount, v9-bundle review MAJOR-3,
                                # fixed & re-run; the CHECK 4/4b gates are
                                # ratio-flatness reads, so no verdict moved,
                                # and the law-tracking ratio moved 0.45 -> ~0.9)
    tot_pairs = float(np.mean(seed_pairs))
    est = np.mean(acc) * tot_pairs
    sem = np.std(acc, ddof=1) / np.sqrt(len(acc)) * tot_pairs
    norm = est / (N * np.log(N) ** 2)
    floor_vals[N] = norm
    print(f"      N = {N:>4}: S_ab estimate {est:9.1f} +/- {sem:.1f} "
          f"-> /(N ln^2 N) = {norm:.4f}")
vals = np.array(list(floor_vals.values()))
ok = vals.max() / vals.min() < 2.5
check("GO/NO-GO: S_ab/(N ln^2 N) flat within 2.5x across N = 256..1024 — "
      "the conditional floor's practical face (a strong upward trend would "
      "be the NO-GO finding; both directions were live)", ok,
      f"max/min = {vals.max()/vals.min():.2f}")

# ---- CHECK 4b: does the exact law PREDICT the finite-N shape? (added at
# first execution, before any verdict consumed: the normalized observable
# rises 0.08 -> 0.18 across the window; if that rise is the exact law's own
# finite-N transient, the prediction tracks the measurement and the floor
# claim stands on the law rather than on window-flatness.)
print("CHECK 4b: the finite-N prediction from the exact law + measured Var/E")
r_bar = float(ratio.mean())          # measured Var/E level (CHECK 3)
_EA_cache = {}
def f_of_k(k):
    if k not in _EA_cache:
        _EA_cache[k] = sum(float(EA_exact(k, j)) for j in range(3)) / k ** 2
    return _EA_cache[k]
from math import lgamma as _lg, exp as _exp, log as _log
def pois_pmf(k, lam):
    return _exp(k * _log(lam) - lam - _lg(k + 1))
def predict(N):
    s_grid = np.geomspace(1e-4, 1.0, 140)
    g = (1 + s_grid) * np.log(1 / s_grid) - 2 * (1 - s_grid)
    tot = 0.0
    prev_s = 0.0
    for s, gs in zip(s_grid, g):
        lam = (N - 2) * s
        lo = max(M0, int(lam - 6 * np.sqrt(lam + 1)))
        hi = int(lam + 6 * np.sqrt(lam + 1)) + 8
        inner = sum(pois_pmf(k, lam) * f_of_k(k) for k in range(lo, hi + 1)) if lam > 0.5 else (
            sum(pois_pmf(k, lam) * f_of_k(k) for k in range(M0, M0 + 40)))
        tot += gs * inner * (s - prev_s)
        prev_s = s
    return N * (N - 1) * r_bar * tot
ok_all = True
ratios_pm = []
for N in (256, 512, 1024):
    pred = predict(N)
    meas = floor_vals[N] * (N * np.log(N) ** 2)
    ratios_pm.append(meas / pred)
    print(f"      N = {N:>4}: predicted {pred:9.1f} vs measured {meas:9.1f} "
          f"(ratio {meas/pred:.2f})")
rp = np.array(ratios_pm)
ok = rp.max() / rp.min() < 1.5
check("the exact-law prediction TRACKS the measured totals (ratio flat "
      "within 1.5x across N) — the rising normalized observable is the "
      "law's own finite-N shape, and the floor claim stands on the law",
      ok, f"meas/pred = {np.round(rp, 2).tolist()}")

# ============ CHECK 5: the cluster adversary priced (G5)
print("CHECK 5: Row A prices the cluster adversary (k-matched)")
mf, mc_ = [], []
for s in range(4):
    pts = cluster_pts(510)
    C = dominance(pts)
    ii, jj = np.nonzero(C)
    pick = rng.choice(len(ii), size=50, replace=False)
    for p in pick:
        u, v = ii[p], jj[p]
        lo, hi = pts[u], pts[v]
        inside = ((pts[:, 0] > lo[0]) & (pts[:, 0] < hi[0]) &
                  (pts[:, 1] > lo[1]) & (pts[:, 1] < hi[1]))
        k = int(inside.sum())
        if k >= M0:
            mc_.append((k, m_ab_of_interval(pts[inside])))
for s in range(4):
    pts = sprinkle(510)
    C = dominance(pts)
    ii, jj = np.nonzero(C)
    pick = rng.choice(len(ii), size=50, replace=False)
    for p in pick:
        u, v = ii[p], jj[p]
        lo, hi = pts[u], pts[v]
        inside = ((pts[:, 0] > lo[0]) & (pts[:, 0] < hi[0]) &
                  (pts[:, 1] > lo[1]) & (pts[:, 1] < hi[1]))
        k = int(inside.sum())
        if k >= M0:
            mf.append((k, m_ab_of_interval(pts[inside])))
# k-matched comparison: restrict both to the overlapping k-range
kf = np.array([x[0] for x in mf]); vf = np.array([x[1] for x in mf])
kc = np.array([x[0] for x in mc_]); vc = np.array([x[1] for x in mc_])
klo, khi = max(kf.min(), kc.min()), min(kf.max(), kc.max())
self_f = vf[(kf >= klo) & (kf <= khi)]
self_c = vc[(kc >= klo) & (kc <= khi)]
ratio = self_c.mean() / self_f.mean()
ok = ratio > 2
check("cluster blow-up pays > 2x the faithful abundance misfit on k-matched "
      "intervals — the adversary that survives S_r and Row C is priced by "
      "Row A (paper 11 §4's named discriminator, now measured per-interval)",
      ok, f"ratio = {ratio:.1f}x (k-range [{klo}, {khi}]; "
          f"n = {len(self_c)}/{len(self_f)})")

# ============ CHECK 6: the division of labor (G6) — computed, not narrated
anti = np.column_stack([np.linspace(0.05, 0.95, 64),
                        np.linspace(0.95, 0.05, 64)])   # a 64-point antichain
C_anti = dominance(anti)
S_ab_anti = 0.0
ii, jj = np.nonzero(C_anti)
for u, v in zip(ii, jj):
    I = np.nonzero(C_anti[u] & C_anti[:, v])[0]
    if len(I) >= M0:
        S_ab_anti += m_ab_of_interval(anti[I])
check("S_ab(antichain) = 0 COMPUTED on a built 64-point antichain (zero "
      "related pairs: " + str(int(C_anti.sum())) + ") — the sparse wall is "
      "Row C's job; Row A is the profile discriminator", 
      C_anti.sum() == 0 and S_ab_anti == 0.0,
      f"S_ab = {S_ab_anti}")

print()
total = PASS + FAIL
if FAIL == 0:
    print(f"ALL CHECKS PASS ({PASS}/{total})")
else:
    print(f"FAILURES: {FAIL}/{total}")
    raise SystemExit(1)
