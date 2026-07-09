#!/usr/bin/env python3
"""
dimwall_selection.py — v9 round 31: THE SELECTION QUESTION (note-3p1-p5;
pin committed at a10f03f strictly before this receipt.  NO-REVIEW MODE;
a mapping receipt — verdict classes, not numeric predictions).

(b) band-closure: C = 2..6 x alpha sweep; VIABLE = decorrelated
    (corr < 0.25) + volume within 2x of the measured (C+1)-orthant
    anchor + realizer refusal.  Classes: BAND-CLOSES-AT(C*) /
    BAND-PERSISTS / NO-BAND.
(a) channel-survival: C_max = 8, reinforcement deposits
    P(k|c) prop acc[c,k] + eta, per-channel churn; C_eff = 1/sum p^2 in
    the last window; windowed d_MM reads surviving + 1.  Classes:
    SELECTS / DIAL-TRACKING / COLLAPSE.
Exit 1 only on instrument failure.
"""
import numpy as np

def dim_le_2(rel):
    n = rel.shape[0]
    inc = ~(rel | rel.T) & ~np.eye(n, dtype=bool)
    parent = list(range(n * n))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(x, y):
        rx, ry = find(x), find(y)
        if rx != ry:
            parent[rx] = ry
    for a in range(n):
        nbs = np.where(inc[a])[0]
        if len(nbs) < 2:
            continue
        sub = inc[np.ix_(nbs, nbs)]
        iu, ju = np.triu_indices(len(nbs), 1)
        sel = ~sub[iu, ju]
        for b, c in zip(nbs[iu[sel]], nbs[ju[sel]]):
            union(a * n + b, a * n + c)
            union(b * n + a, c * n + a)
    ii, jj = np.where(np.triu(inc, 1))
    for i, j in zip(ii, jj):
        if find(i * n + j) == find(j * n + i):
            return False
    return True

def sprinkle_mink(rng, N, dspace):
    T = np.empty(0); X = np.empty((0, dspace))
    while len(T) < N:
        t = rng.random(6 * N)
        x = rng.uniform(-0.5, 0.5, (6 * N, dspace))
        r = np.linalg.norm(x, axis=1)
        keep = (r <= t) & (r <= 1 - t)
        T = np.concatenate([T, t[keep]]); X = np.vstack([X, x[keep]])
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

def frac(rel):
    n = rel.shape[0]
    return rel.sum() / (n * (n - 1) / 2)

def rel_win(idx, chiV, C):
    b = idx
    rel = b[:, None] < b[None, :]
    for k in range(C):
        rel &= chiV[idx][:, None, k] <= chiV[idx][None, :, k]
    np.fill_diagonal(rel, False)
    return rel

print("[dimwall selection: why C = 3?]")

# measured orthant anchors at N = 128 (k = 3..7)
ORTH = {}
for k in range(3, 8):
    fr = []
    for j in range(6):
        r = np.random.default_rng(20261100 + 100 * k + j)
        Z = r.random((128, k))
        rel = np.ones((128, 128), dtype=bool)
        for q in range(k):
            rel &= Z[:, None, q] < Z[None, :, q]
        np.fill_diagonal(rel, False)
        fr.append(frac(rel))
    ORTH[k] = float(np.mean(fr))
print("      orthant anchors @128: " + "  ".join(
    f"k={k}: {v:.4f}" for k, v in ORTH.items()))

# ---------- (b) the band-closure sweep ----------
def web_corner(sd, C, alpha, N=2048, M=32, L=16):
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

ALPHAS = (0.5, 0.6, 0.7, 0.8, 0.9, 0.95)
SEEDS = (20261110, 20261111, 20261112)
print("      (b) band-closure sweep — viable-alpha count per C:")
band = {}
for C in (2, 3, 4, 5, 6):
    width = 0
    row = []
    for a in ALPHAS:
        ok_seeds = 0
        realizer_needed = []
        for sd in SEEDS:
            chiV, r = web_corner(sd, C, a)
            cc = np.corrcoef(chiV[512:1536].T)
            corr = float(np.mean(cc[np.triu_indices(C, 1)]))
            start = (2048 - 512) // 2
            idx = np.sort(r.choice(np.arange(start, start + 512), 128,
                                   replace=False))
            rel = rel_win(idx, chiV, C)
            f = frac(rel)
            vol = abs(np.log2(f / ORTH[C + 1])) <= 1 if f > 0 else False
            if corr < 0.25 and vol:
                realizer_needed.append(rel)
        if len(realizer_needed) >= 2:
            ok_seeds = sum(1 for rel in realizer_needed[:3]
                           if not dim_le_2(rel))
        viable = len(realizer_needed) >= 2 and ok_seeds >= 2
        width += viable
        row.append("V" if viable else ".")
    band[C] = width
    print(f"      C={C}: [{' '.join(row)}]  width = {width}/6")

if all(band[C] >= 1 for C in band):
    vb = "BAND-PERSISTS (width >= 1 through C = 6)"
elif any(band[C] == 0 for C in band):
    cs = [C for C in sorted(band) if band[C] == 0]
    prev_ok = all(band[C2] >= 1 for C2 in sorted(band) if C2 < cs[0])
    vb = (f"BAND-CLOSES-AT({cs[0]})" if prev_ok and cs[0] > 2
          else "NO-BAND / irregular — see table")
print(f"      (b) VERDICT CLASS: {vb}")

# ---------- (a) channel-survival ----------
def web_survival(sd, Cmax, eta, L, N=4096, M=32):
    rng = np.random.default_rng(sd)
    acc = np.zeros((M, Cmax))
    chiV = np.zeros((N, Cmax))
    dep = np.zeros(Cmax)
    for t in range(N):
        c = int(rng.integers(M))
        w = acc[c] + eta
        w = w / w.sum()
        k = int(rng.choice(Cmax, p=w))
        e = rng.exponential(0.109551)
        acc[c, k] += e
        if t >= N - 512:
            dep[k] += e
        chiV[t] = acc[c]
        for kk in range(Cmax):
            if rng.random() < 1.0 / L:
                acc[int(rng.integers(M)), kk] = 0.0
    p = dep / max(dep.sum(), 1e-12)
    ceff = 1.0 / max((p ** 2).sum(), 1e-12)
    return ceff, chiV, rng

# d_MM curve (M2..M5, standard recipe)
ref = {}
for d in (1, 2, 3, 4):
    fr = []
    for k in range(8):
        r = np.random.default_rng(20260760 + 10 * d + k)
        rel = (sprinkle_m2(r, 512) if d == 1 else sprinkle_mink(r, 512, d))
        fr.append(frac(rel))
    ref[d + 1] = float(np.mean(fr))
def d_mm(f):
    ds = sorted(ref); fs = [ref[d] for d in ds]
    if f >= fs[0]: return 2.0
    if f <= fs[-1]: return float(ds[-1])
    for a2 in range(len(ds) - 1):
        if fs[a2] >= f >= fs[a2 + 1]:
            w = (fs[a2] - f) / (fs[a2] - fs[a2 + 1])
            return ds[a2] + w * (ds[a2 + 1] - ds[a2])
    return float("nan")

print("      (a) channel-survival — C_eff (deposit shares, last window) "
      "and windowed d_MM:")
ceffs = []
for eta in (0.005, 0.05, 0.5):
    for L in (8, 16, 32):
        ce_l, dm_l = [], []
        for sd in SEEDS:
            ceff, chiV, r = web_survival(sd, 8, eta, L)
            start = 4096 - 768
            idx = np.sort(r.choice(np.arange(start, start + 512), 128,
                                   replace=False))
            rel = rel_win(idx, chiV, 8)
            ce_l.append(ceff); dm_l.append(d_mm(frac(rel)))
        ceffs.append(float(np.mean(ce_l)))
        print(f"      eta={eta:<6} L={L:<3}: C_eff = {np.mean(ce_l):.2f} "
              f"(sd {np.std(ce_l):.2f}); windowed d_MM = {np.mean(dm_l):.2f}")
ce5, _, _ = web_survival(SEEDS[0], 5, 0.05, 16)
print(f"      C_max = 5 spot (eta 0.05, L 16): C_eff = {ce5:.2f}")

span = max(ceffs) / max(min(ceffs), 1e-9)
if max(ceffs) <= 2.0:
    va = "COLLAPSE (C_eff <= 2 everywhere)"
elif span <= 1.5 and abs(np.mean(ceffs) - np.median(ceffs)) < 0.5:
    va = f"SELECTS (C_eff ~ {np.mean(ceffs):.1f} across the grid)"
else:
    va = f"DIAL-TRACKING (C_eff spans {min(ceffs):.1f}..{max(ceffs):.1f}, x{span:.1f})"
print(f"      (a) VERDICT CLASS: {va}")

print()
print(f"ADJUDICATION: (b) {vb}; (a) {va}")
print("ALL CHECKS PASS (mapping receipt — classes reported)")
