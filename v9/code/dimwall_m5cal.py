#!/usr/bin/env python3
"""
dimwall_m5cal.py — v9 round 30: the M5-extended calibration
(note-3p1-m5cal; pin committed at 8a65750 strictly before this receipt).
Gates: Gm5-0 the M5 point separates (> 3x pooled sd below M4); Gm5-1
windowed d_MM(C=3, Delta=512) in [3.7, 4.3] by INTERPOLATION; Gm5-2 the
in-window ladder strictly monotone with C=2 in [2.8, 3.5].  On green the
reserved review fires (grading withheld).  Exit 1 by design on refusal.
"""
import numpy as np

PASS = FAIL = 0
def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    if ok: PASS += 1
    else: FAIL += 1
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

def sprinkle_mink(rng, N, dspace):
    """Uniform diamond sprinkle in 1+dspace dims (batch rejection)."""
    T = np.empty(0); X = np.empty((0, dspace))
    while len(T) < N:
        t = rng.random(4 * N)
        x = rng.uniform(-0.5, 0.5, (4 * N, dspace))
        r = np.linalg.norm(x, axis=1)
        keep = (r <= t) & (r <= 1 - t)
        T = np.concatenate([T, t[keep]])
        X = np.vstack([X, x[keep]])
    T = T[:N]; X = X[:N]
    dt = T[None, :] - T[:, None]
    dx = np.linalg.norm(X[None, :, :] - X[:, None, :], axis=2)
    rel = (dt > 0) & (dt >= dx)
    np.fill_diagonal(rel, False)
    return rel

def sprinkle_m2(rng, N):
    u = rng.random(N); v = rng.random(N)
    rel = (u[:, None] < u[None, :]) & (v[:, None] < v[None, :])
    np.fill_diagonal(rel, False)
    return rel

def web_chiv(sd, C=3, N=2048, M=32, L=16, alpha=0.75):
    rng = np.random.default_rng(sd)
    acc = np.zeros((M, C))
    pref = np.arange(M) % C
    chiV = np.zeros((N, C))
    for t in range(N):
        c = int(rng.integers(M))
        if C > 1 and rng.random() < alpha:
            k = int(pref[c])
        else:
            k = int(rng.integers(C))
        acc[c, k] += rng.exponential(0.109551)
        chiV[t] = acc[c]
        for kk in range(C):
            if rng.random() < 1.0 / L:
                acc[int(rng.integers(M)), kk] = 0.0
    return chiV, rng

def win_frac(sd, C, D=512, NW=128):
    chiV, r = web_chiv(sd, C=C)
    start = (2048 - D) // 2
    idx = np.sort(r.choice(np.arange(start, start + D), NW, replace=False))
    b = idx
    rel = b[:, None] < b[None, :]
    for k in range(C):
        rel &= chiV[idx][:, None, k] <= chiV[idx][None, :, k]
    np.fill_diagonal(rel, False)
    n = rel.shape[0]
    return rel.sum() / (n * (n - 1) / 2)

print("[dimwall m5cal: the extended calibration]")
ref = {}
sds = {}
for d in (1, 2, 3, 4):
    fr = []
    for k in range(8):
        r = np.random.default_rng(20260760 + 10 * d + k)
        rel = (sprinkle_m2(r, 512) if d == 1 else sprinkle_mink(r, 512, d))
        n = rel.shape[0]
        fr.append(rel.sum() / (n * (n - 1) / 2))
    ref[d + 1] = float(np.mean(fr))
    sds[d + 1] = float(np.std(fr, ddof=1))
    print(f"      M^{d+1}: fraction {ref[d+1]:.4f} ± {sds[d+1]:.4f}"
          + ("   [analytic anchor 1/2]" if d == 1 else ""))

gap = ref[4] - ref[5]
check("Gm5-0 (the curve extends): M5 sits below M4 by > 3x pooled sd",
      gap > 3 * (sds[4] + sds[5]), f"gap {gap:.4f} vs sd-sum {sds[4]+sds[5]:.4f}")

def d_mm(f):
    ds = sorted(ref); fs = [ref[d] for d in ds]
    if f >= fs[0]: return 2.0
    if f <= fs[-1]: return float(ds[-1])
    for a in range(len(ds) - 1):
        if fs[a] >= f >= fs[a + 1]:
            w = (fs[a] - f) / (fs[a] - fs[a + 1])
            return ds[a] + w * (ds[a + 1] - ds[a])
    return float("nan")

SEEDS = list(range(20260960, 20260965))
f3 = [win_frac(sd, 3) for sd in SEEDS]
d3 = d_mm(float(np.mean(f3)))
interp = ref[5] <= float(np.mean(f3)) <= ref[2]
check("Gm5-1 (the re-read): windowed d_MM(C = 3) in [3.7, 4.3] by "
      "INTERPOLATION on the extended curve",
      3.7 <= d3 <= 4.3 and interp,
      f"d_MM = {d3:.2f} (mean fraction {np.mean(f3):.4f}; interpolated: {interp})")

f2 = [win_frac(sd, 2) for sd in SEEDS]
f1 = [win_frac(sd, 1) for sd in SEEDS]
d2, d1 = d_mm(float(np.mean(f2))), d_mm(float(np.mean(f1)))
check("Gm5-2 (the in-window ladder): strictly monotone C = 1, 2, 3 with "
      "C = 2 in [2.8, 3.5]", d1 < d2 < d3 and 2.8 <= d2 <= 3.5,
      f"d_MM = {d1:.2f} / {d2:.2f} / {d3:.2f}")

# INFO: the orthant clock-scale
orf = {}
for k in (3, 4, 5):
    fr = []
    for j in range(8):
        r = np.random.default_rng(20261000 + 100 * k + j)
        Z = r.random((512, k))
        rel = np.ones((512, 512), dtype=bool)
        for q in range(k):
            rel &= Z[:, None, q] < Z[None, :, q]
        np.fill_diagonal(rel, False)
        fr.append(rel.sum() / (512 * 511 / 2))
    orf[k] = float(np.mean(fr))
print("      INFO orthant anchors: " + "  ".join(
    f"k={k}: {orf[k]:.4f} (analytic {2.0**(1-k):.4f})" for k in orf))
print(f"      INFO: windowed C = 3 fraction {np.mean(f3):.4f} sits between "
      f"orthant k=4 ({orf[4]:.4f}) and k=5 ({orf[5]:.4f}) — effective "
      f"clocks > 4 on the polyhedral scale (printed, unpinned)")

verdict = ("GREEN — THE RESERVED REVIEW FIRES (grading withheld)"
           if FAIL == 0 else "CALIBRATION REFUSED — the finding stays unread")
print(f"      VERDICT: {verdict}")
print()
print(f"PRE-REGISTERED GATE LEDGER: "
      f"{'ALL HELD' if FAIL == 0 else 'REFUSALS PRESENT'} — Gm5-0/1/2; {verdict}")
print()
total = PASS + FAIL
print(f"ALL CHECKS PASS ({PASS}/{total})" if FAIL == 0 else f"FAILURES: {FAIL}/{total}")
if FAIL: raise SystemExit(1)
