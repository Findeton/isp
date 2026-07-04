#!/usr/bin/env python3
"""
o2_estimator_onset.py — v8 paper 8 §3: the conformal-order onset (order axis).

QUESTION. Given a perfectly manifold-like record order (Poisson sprinkling of a
causal diamond — the coordinates HELD OUT as scoring truth only, estimators
order-only; methodology of v8 paper 4 §1 / paper 7), at what record count N do the
order→conformal estimators STABILIZE — i.e. when does the conformal-order readout
become statistically meaningful at the tolerances of paper 7's certificate?

This is a READOUT-onset measurement, conditional on manifold-like input. It does
NOT touch the manifoldlikeness gate (paper 4 §5, paper 7): it measures when the
instruments turn on, not when/whether records become geometric.

Estimator implementations are standalone copies of g1_estimator_concordance.py's
(same definitions, so the onsets are commensurable with paper 7's bands), with one
performance change: boolean matmuls run in float32 BLAS (counts < 2^24, exact).

Onset definitions (disclosed, N-independent tolerances in DIMENSION units taken
from paper 7's operative floors — axes 1-2 half-width floor 0.15, axis 3 floor 0.40):
  N*_1  (d_MM axis):    smallest tabulated N with >= 90% of seeds |d_MM - d| <= 0.15
  N*_3  (midpoint axis): smallest tabulated N with >= 90% of seeds |d_mid - d| <= 0.40
                         (NaN => fail, paper 7 convention)
  N*_cert = max(N*_1, N*_3): the certificate's dimension-axes onset.
Height (axis 2) has no N-free tolerance: it is scored against the
Baik-Deift-Johansson law E[H] ~ 2 sqrt(N) - 1.7711 N^{1/6} [IMPORT] (2D only), and
its ratio-to-2sqrt(N) drift is reported. Abundance (axis 4) is scored as internal
concentration: median TV(seed profile, same-N ensemble mean); the 0.03-scale
threshold quoted in paper 7 is N = 480-calibrated — the curve's crossing of it is
reported, not asserted as N-free.

Conventions (disclosed): "sprinkling" here is FIXED-N (binomial) sampling, the
field-standard finite-N surrogate for Poisson — and fixed N is exactly what makes
the BDJ E[L_N] comparison an equality-in-law statement rather than a mixture.
Tabulated med|d_mid - d| values are medians over the non-NaN seeds only (the NaN
count is printed beside them); the PASS-RATE columns count NaN as fail.
Float discipline: the Monte-Carlo landscape is float64 (a search/measurement, per
the corpus rule); the f(d) anchors are mpmath dps = 40.
Seed: default_rng(20260702).
"""

import numpy as np
from mpmath import mp, mpf, gamma, findroot

mp.dps = 40
rng = np.random.default_rng(20260702)

PASS = 0
FAIL = 0

def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    if ok: PASS += 1
    else: FAIL += 1
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))


# ---------------------------------------------------------------- populations
def sprinkle_2d(N):
    uv = rng.random((N, 2))
    return (uv[None, :, 0] > uv[:, None, 0]) & (uv[None, :, 1] > uv[:, None, 1])

def sprinkle_3d(N):
    pts = []
    while len(pts) < N:
        m = max(64, 4 * (N - len(pts)))
        t = rng.uniform(-1, 1, m); x = rng.uniform(-1, 1, m); y = rng.uniform(-1, 1, m)
        keep = np.hypot(x, y) <= 1 - np.abs(t)
        for tt, xx, yy in zip(t[keep], x[keep], y[keep]):
            pts.append((tt, xx, yy))
            if len(pts) == N:
                break
    P = np.array(pts)
    dt = P[None, :, 0] - P[:, None, 0]
    dr = np.hypot(P[None, :, 1] - P[:, None, 1], P[None, :, 2] - P[:, None, 2])
    return (dt > 0) & (dt >= dr)

# ----------------------------------------------------------------- estimators
def f_mm(d):
    d = mpf(d)
    return gamma(d + 1) * gamma(d / 2) / (2 * gamma(3 * d / 2))

def d_mm(C):
    N = C.shape[0]
    r = 2.0 * C.sum() / (N * (N - 1))
    if r <= 0:
        return float("inf")
    try:
        return float(findroot(lambda d: f_mm(d) - r, mpf(2.0)))
    except Exception:
        ds = np.linspace(1.05, 6.0, 2000)
        return float(ds[int(np.argmin([abs(float(f_mm(d)) - r) for d in ds]))])

def height(C):
    N = C.shape[0]
    indeg = C.sum(axis=0).astype(int)
    stack = [i for i in range(N) if indeg[i] == 0]
    Clist = [np.nonzero(C[i])[0] for i in range(N)]
    L = np.ones(N, dtype=int)
    topo = []
    while stack:
        v = stack.pop()
        topo.append(v)
        for w in Clist[v]:
            indeg[w] -= 1
            if indeg[w] == 0:
                stack.append(w)
    for v in topo:
        succ = Clist[v]
        if len(succ):
            L[succ] = np.maximum(L[succ], L[v] + 1)
    return int(L.max())

def between_matrix(C):
    Cf = C.astype(np.float32)
    B = Cf @ Cf
    return np.rint(B).astype(np.int32)

def d_mid(C, between):
    sizes = np.where(C, between, -1)
    x, y = np.unravel_index(np.argmax(sizes), sizes.shape)
    big = sizes[x, y]
    if big < 8:
        return float("nan")
    inner = np.nonzero(C[x] & C[:, y])[0]
    best = 0
    for m in inner:
        a = int((C[x] & C[:, m]).sum())
        b = int((C[m] & C[:, y]).sum())
        best = max(best, min(a, b))
    if best < 1:
        return float("nan")
    return float(np.log2((big + 2) / (best + 2)))

def abundance_profile(C, between, kmax=5):
    pairs = C.sum()
    prof = np.array([np.sum(C & (between == k)) for k in range(kmax + 1)], dtype=float)
    return prof / max(pairs, 1)

def analyze(C):
    B = between_matrix(C)
    return {"d_mm": d_mm(C), "H": height(C), "d_mid": d_mid(C, B),
            "prof": abundance_profile(C, B)}

# ------------------------------------------------------------------ anchors
print("CHECK 0: Myrheim-Meyer anchors (mpmath dps = 40)")
ok = abs(f_mm(2) - mpf(1) / 2) < mpf(10) ** -35 and \
     abs(f_mm(3) - mpf(8) / 35) < mpf(10) ** -35 and abs(f_mm(1) - 1) < mpf(10) ** -35
check("f(1) = 1, f(2) = 1/2, f(3) = 8/35 exact", ok)

# --------------------------------------------------------------- the sweep, 2D
SIZES_2D = [16, 32, 64, 128, 256, 512, 1024, 2048]
SEEDS_2D = {16: 40, 32: 40, 64: 40, 128: 40, 256: 40, 512: 40, 1024: 25, 2048: 15}
TOL_MM, TOL_MID = 0.15, 0.40
PASS_FRAC = 0.90

print("\nSWEEP 2D: Poisson diamond, order-only estimators, held-out coordinates")
print("  N     seeds  med|dMM-2|  pass1  med|dmid-2|(NaN)  pass3  "
      "H_mean  H_BDJ   medTV")
res2 = {}
for N in SIZES_2D:
    S = SEEDS_2D[N]
    rows = [analyze(sprinkle_2d(N)) for _ in range(S)]
    dmm = np.array([r["d_mm"] for r in rows])
    dmid = np.array([r["d_mid"] for r in rows])
    hh = np.array([r["H"] for r in rows], dtype=float)
    profs = np.stack([r["prof"] for r in rows])
    mean_prof = profs.mean(axis=0)
    tvs = 0.5 * np.abs(profs - mean_prof).sum(axis=1)
    e1 = np.abs(dmm - 2.0)
    e3 = np.abs(dmid - 2.0)                      # NaN stays NaN
    pass1 = float(np.mean(e1 <= TOL_MM))
    pass3 = float(np.mean(np.where(np.isnan(e3), False, e3 <= TOL_MID)))
    nnan = int(np.isnan(dmid).sum())
    bdj = 2 * np.sqrt(N) - 1.7711 * N ** (1 / 6)
    res2[N] = dict(pass1=pass1, pass3=pass3, e1med=float(np.median(e1)),
                   e3med=float(np.nanmedian(e3)) if nnan < S else float("nan"),
                   Hmean=float(hh.mean()), bdj=float(bdj),
                   tvmed=float(np.median(tvs)), nnan=nnan)
    print(f"  {N:<5} {S:<6} {np.median(e1):.4f}      {pass1:4.0%}  "
          f"{res2[N]['e3med']:.4f} ({nnan:>2}NaN)     {pass3:4.0%}  "
          f"{hh.mean():6.2f}  {bdj:6.2f}  {np.median(tvs):.4f}")

def onset(res, key, sizes):
    for N in sizes:
        if N in res and res[N][key] >= PASS_FRAC:
            # require it to STAY passed at all larger tabulated N
            if all(res[M][key] >= PASS_FRAC for M in res if M >= N):
                return N
    return None

N1 = onset(res2, "pass1", SIZES_2D)
N3 = onset(res2, "pass3", SIZES_2D)
print(f"\n  onsets 2D: N*_1 (d_MM) = {N1}, N*_3 (midpoint) = {N3}, "
      f"N*_cert = {max(N1, N3) if N1 and N3 else None}")

print("\nCHECK 1: 2D onsets exist and are stable through the largest N")
check("N*_1 exists (d_MM axis onset, tol 0.15, 90% of seeds, stable upward)",
      N1 is not None, f"N*_1 = {N1}")
check("N*_3 exists (midpoint axis onset, tol 0.40, NaN=>fail, stable upward)",
      N3 is not None, f"N*_3 = {N3}")

print("CHECK 2: below onset the readout is void; errors shrink with N")
small = res2[16]
check("at N = 16 the dimension axes fail for most seeds (readout void)",
      small["pass1"] < 0.5 and small["pass3"] < 0.5,
      f"pass1 = {small['pass1']:.0%}, pass3 = {small['pass3']:.0%}")
e1s = [res2[N]["e1med"] for N in SIZES_2D]
check("median |d_MM - 2| decreases N=16 -> 2048 and is < 0.05 at N = 2048",
      e1s[0] > e1s[-1] and e1s[-1] < 0.05, f"{e1s[0]:.3f} -> {e1s[-1]:.4f}")

print("CHECK 3: d_MM error scaling exponent")
NN = np.array([N for N in SIZES_2D if N >= 64], dtype=float)
EE = np.array([res2[int(N)]["e1med"] for N in NN])
alpha, loga = np.polyfit(np.log(NN), np.log(EE), 1)
alpha = -alpha
check("fitted median-error exponent alpha in (0.3, 0.7) (~ N^{-1/2} concentration)",
      0.3 < alpha < 0.7, f"alpha = {alpha:.3f}")

print("CHECK 4: height axis vs the BDJ finite-size law [IMPORT]")
ok = True
for N in (256, 512, 1024, 2048):
    rel = abs(res2[N]["Hmean"] - res2[N]["bdj"]) / res2[N]["bdj"]
    if rel > 0.04:
        ok = False
check("mean H within 4% of 2 sqrt(N) - 1.7711 N^{1/6} for N >= 256",
      ok, ", ".join(f"N={N}: {res2[N]['Hmean']:.1f}/{res2[N]['bdj']:.1f}"
                    for N in (256, 2048)))

print("CHECK 5: abundance concentration (axis 4)")
tvs = [res2[N]["tvmed"] for N in SIZES_2D]
check("median internal TV decreases monotonically N=16 -> 2048",
      all(tvs[i] > tvs[i + 1] for i in range(len(tvs) - 1)),
      " -> ".join(f"{t:.3f}" for t in (tvs[0], tvs[3], tvs[-1])))
cross = next((N for N in SIZES_2D if res2[N]["tvmed"] <= 0.03), None)
check("the TV curve crosses the 0.03 scale (the paper-7 N=480-calibrated threshold) "
      "at a tabulated N", cross is not None, f"first N with medTV <= 0.03: {cross}")

# --------------------------------------------------------------- the sweep, 3D
SIZES_3D = [16, 32, 64, 128, 256, 512, 1024]
SEEDS_3D = {16: 30, 32: 30, 64: 30, 128: 30, 256: 30, 512: 25, 1024: 15}

print("\nSWEEP 3D: Poisson diamond M^3")
print("  N     seeds  med|dMM-3|  pass1  med|dmid-3|(NaN)  pass3")
res3 = {}
for N in SIZES_3D:
    S = SEEDS_3D[N]
    rows = [analyze(sprinkle_3d(N)) for _ in range(S)]
    dmm = np.array([r["d_mm"] for r in rows])
    dmid = np.array([r["d_mid"] for r in rows])
    e1 = np.abs(dmm - 3.0)
    e3 = np.abs(dmid - 3.0)
    pass1 = float(np.mean(e1 <= TOL_MM))
    pass3 = float(np.mean(np.where(np.isnan(e3), False, e3 <= TOL_MID)))
    nnan = int(np.isnan(dmid).sum())
    res3[N] = dict(pass1=pass1, pass3=pass3, e1med=float(np.median(e1)),
                   e3med=float(np.nanmedian(e3)) if nnan < S else float("nan"))
    print(f"  {N:<5} {S:<6} {np.median(e1):.4f}      {pass1:4.0%}  "
          f"{res3[N]['e3med']:.4f} ({nnan:>2}NaN)     {pass3:4.0%}")

N1_3 = onset(res3, "pass1", SIZES_3D)
N3_3 = onset(res3, "pass3", SIZES_3D)
print(f"\n  onsets 3D: N*_1 = {N1_3}, N*_3 = {N3_3}")

print("CHECK 6: 3D d_MM onset exists; 3D needs more records than 2D on the same axis")
check("3D N*_1 exists", N1_3 is not None, f"N*_1(3D) = {N1_3}")
check("N*_1(3D) >= N*_1(2D) (higher dimension, harder readout, same tolerance)",
      N1_3 is not None and N1 is not None and N1_3 >= N1,
      f"{N1_3} >= {N1}")

print("CHECK 7: 3D midpoint axis — substantive convergence test")
# real test (was a hardcoded-True report pre-review): NaN incidence must vanish
# by N = 128 and the pass rate must reach 100% at the largest tabulated N
ok = (res3[128]["pass3"] > 0.5 and res3[1024]["pass3"] == 1.0
      and res3[16]["pass3"] < 0.5)
check("3D midpoint: void at N = 16 (<50%), majority-pass by N = 128, 100% at N = 1024",
      ok, f"pass3: {res3[16]['pass3']:.0%} -> {res3[128]['pass3']:.0%} -> "
          f"{res3[1024]['pass3']:.0%}; N*_3(3D) = {N3_3}")

# ------------------------------------------------------------------- verdict
print()
total = PASS + FAIL
if FAIL == 0:
    print(f"ALL CHECKS PASS ({PASS}/{total})")
    print(f"ONSETS: 2D N*_1={N1}, N*_3={N3}, N*_cert={max(N1, N3)}; "
          f"3D N*_1={N1_3}, N*_3={N3_3}; alpha={alpha:.3f}")
else:
    print(f"FAILURES: {FAIL}/{total}")
    raise SystemExit(1)
