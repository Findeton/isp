#!/usr/bin/env python3
"""
dimwall_dialsweep.py — v9 round 42: Phase 2b, the specialization/mixing
dial vs (cone shape F, order dimension). Pin: note-3p1-dialsweep
(51ebc8a, strictly before this ran).

Machinery provenance (copied verbatim): footprint + web_window from
dimwall_footprint.py (round 40; per-channel churn — the Lorentz-line
convention); dim_le_2 (Golumbic), sprinkle_mink/sprinkle_m2, the MM
recipe, and the paper-6-class builder conventions from
dimwall_phase0/phase1.py.
"""
import json
import numpy as np

PASS = FAIL = 0
def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    if ok: PASS += 1
    else: FAIL += 1
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

# ---- footprint machinery (verbatim, round 40) ----
S_MIN = 0.3
Q = 0.9
MIN_PROJ = 30

def footprint_F(rel, coords, q=Q, s_min=S_MIN):
    X = (coords - coords.mean(0)) / np.maximum(coords.std(0), 1e-9)
    k = X.shape[1]
    dhat = np.ones(k) / np.sqrt(k)
    dirs = []
    for a in range(k):
        e = np.zeros(k); e[a] = 1.0
        w = e - (e @ dhat) * dhat
        dirs.append(w / np.linalg.norm(w))
    dirs = np.array(dirs)
    ii, jj = np.where(rel)
    d = X[jj] - X[ii]
    s = d @ dhat
    keep = s >= s_min
    d = d[keep]; s = s[keep]
    w = d - s[:, None] * dhat[None, :]
    v = w / s[:, None]
    hs_c, hs_f = [], []
    for u in dirs:
        p = v @ u; p = p[p > 0]
        hs_c.append(np.quantile(p, q) if len(p) >= MIN_PROJ else np.nan)
        m = v @ (-u); m = m[m > 0]
        hs_f.append(np.quantile(m, q) if len(m) >= MIN_PROJ else np.nan)
    return float(np.mean(hs_c) / np.mean(hs_f)), len(s)

def build_lorentzline(sd, mode, alpha=0.75, beta=None, C=3, N=2048, M=32,
                      L=16, D=1024, NW=256):
    """The rounds-36/40 builder, verbatim rng structure, generalized:
    mode 'alpha' = one-hot with preference alpha; mode 'beta' = per-slot
    Dirichlet(beta) weights; mode 'equal' = exact 1/C split.
    Per-channel churn. Returns (full rel, chiV, windowed rel, coords)."""
    rng = np.random.default_rng(sd)
    acc = np.zeros((M, C))
    chiV = np.zeros((N, C))
    if mode == "beta":
        Wd = rng.dirichlet(np.full(C, beta), size=M)
    pref = np.arange(M) % C
    for t in range(N):
        c = int(rng.integers(M))
        e = rng.exponential(0.109551)
        if mode == "beta":
            acc[c] += e * Wd[c]
        elif mode == "equal":
            acc[c] += e / C
        else:
            if rng.random() < alpha:
                k = int(pref[c])
            else:
                k = int(rng.integers(C))
            acc[c, k] += e
        chiV[t] = acc[c]
        for kk in range(C):
            if rng.random() < 1.0 / L:
                acc[int(rng.integers(M)), kk] = 0.0
    b = np.arange(N)
    rel = b[:, None] < b[None, :]
    for k in range(C):
        rel &= chiV[:, None, k] <= chiV[None, :, k]
    np.fill_diagonal(rel, False)
    start = (N - D) // 2
    idx = np.sort(rng.choice(np.arange(start, start + D), NW, replace=False))
    coords = np.column_stack([idx.astype(float), chiV[idx]])
    wrel = rel[np.ix_(idx, idx)]
    return rel, chiV, wrel, coords, rng

def build_p6class(sd, C=3, N=2048, M=32, L=16):
    """The paper-6 certified class (dimwall_phase1 web_rel_C, verbatim
    rng structure): uniform choice, full-vector churn."""
    rng = np.random.default_rng(sd)
    acc = np.zeros((M, C))
    chiV = np.zeros((N, C))
    for t in range(N):
        c = int(rng.integers(M))
        k = int(rng.integers(C))
        acc[c, k] += rng.exponential(0.109551)
        chiV[t] = acc[c]
        if rng.random() < 1.0 / L:
            acc[int(rng.integers(M))] = 0.0
    b = np.arange(N)
    rel = b[:, None] < b[None, :]
    for k in range(C):
        rel &= chiV[:, None, k] <= chiV[None, :, k]
    np.fill_diagonal(rel, False)
    return rel, chiV, rng

# ---- Golumbic dim<=2 tester (verbatim, phase 0) ----
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

# ---- MM machinery — byte-verbatim from openings_pass.py, which WROTE
# the frozen v9/data/mm_reference.json (round 35). Amendment trail,
# disclosed: attempt 1 was a from-memory transcription (8*N batch),
# attempt 2 copied dimwall_phase0.py (one-at-a-time rejection) — both
# caught by Gd0b, which requires the json's own byte-recipe. The corpus
# carries THREE sprinkle_mink variants (phase0; m5cal 4*N; openings
# 6*N) — flagged for the round review. ----
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

print("[dial sweep — round 42]")
ref = {}
for d in (1, 2, 3):
    fr = []
    for k in range(8):
        r = np.random.default_rng(20260760 + 10 * d + k)
        rel = (sprinkle_m2(r, 512) if d == 1 else sprinkle_mink(r, 512, d))
        fr.append(frac(rel))
    ref[d + 1] = float(np.mean(fr))
frozen = json.load(open("v9/data/mm_reference.json"))
ok0b = all(abs(ref[d] - frozen[f"M{d}"]) < 1e-9 for d in (2, 3, 4))
check("Gd0b (wiring, MM side): re-derived reference == frozen json (1e-9)",
      ok0b, "  ".join(f"M{d}:{ref[d]:.4f}" for d in (2, 3, 4)))
ref[5] = frozen["M5"]   # the m5cal extension (frozen; interpolate to M5)

def d_mm(f):
    # m5cal mapping: interpolate on the frozen M2..M5 curve; clamp at 5
    ds = sorted(ref); fs = [ref[d] for d in ds]
    if f >= fs[0]: return 2.0
    if f <= fs[-1]: return float(ds[-1])
    for a in range(len(ds) - 1):
        if fs[a] >= f >= fs[a + 1]:
            w = (fs[a] - f) / (fs[a] - fs[a + 1])
            return ds[a] + w * (ds[a + 1] - ds[a])
    return float("nan")

def win_frac_m5cal(sd, C, D=512, NW=128):
    # m5cal verbatim: web_chiv (alpha=0.75, per-channel churn) + window
    rng = np.random.default_rng(sd)
    M, L, N = 32, 16, 2048
    acc = np.zeros((M, C))
    pref = np.arange(M) % C
    chiV = np.zeros((N, C))
    for t in range(N):
        c = int(rng.integers(M))
        if C > 1 and rng.random() < 0.75:
            k = int(pref[c])
        else:
            k = int(rng.integers(C))
        acc[c, k] += rng.exponential(0.109551)
        chiV[t] = acc[c]
        for kk in range(C):
            if rng.random() < 1.0 / L:
                acc[int(rng.integers(M)), kk] = 0.0
    start = (2048 - D) // 2
    idx = np.sort(rng.choice(np.arange(start, start + D), NW, replace=False))
    b = idx
    rel = b[:, None] < b[None, :]
    for k in range(C):
        rel &= chiV[idx][:, None, k] <= chiV[idx][None, :, k]
    np.fill_diagonal(rel, False)
    n = rel.shape[0]
    return rel.sum() / (n * (n - 1) / 2)

wfr = [win_frac_m5cal(sd, 3) for sd in range(20260960, 20260965)]
wmean = float(np.mean(wfr))
check("Gd0c-prime (the crown anchor): m5cal windowed fraction and d_MM "
      "reproduced (0.1008 -> 4.04)",
      round(wmean, 4) == 0.1008 and round(d_mm(wmean), 2) == 4.04,
      f"fraction {wmean:.4f} -> d_MM {d_mm(wmean):.2f}")

# Gd0a: wiring, F side (round-40 seeds and values)
R40 = {"corner": [2.218, 1.949, 2.179, 2.316, 2.180],
       "kdir": [1.725, 1.831, 1.811, 1.664, 1.865]}
S40 = [20262000 + i for i in range(5)]
okA = True
for mode, key, kw in (("alpha", "corner", dict(alpha=0.75)),
                      ("beta", "kdir", dict(beta=1.0))):
    got = []
    for sd in S40:
        _, _, wrel, coords, _ = build_lorentzline(sd, mode, **kw)
        F, _ = footprint_F(wrel, coords)
        got.append(round(F, 3))
    okA &= got == R40[key]
    print(f"      wiring {key}: {got}")
check("Gd0a (wiring, F side): round-40 corner and kdir F reproduced exactly",
      okA)

# ---- the sweep ----
SEEDS = [20262200 + i for i in range(5)]
POINTS = ([("alpha", f"a={a}", dict(alpha=a)) for a in (0.0, 0.25, 0.5, 0.75, 1.0)]
          + [("beta", f"b={b}", dict(beta=b)) for b in (0.25, 1.0, 4.0, 16.0)]
          + [("equal", "b=EQ", {})])
rows = {}
WSTART = (2048 - 512) // 2
for mode, tag, kw in POINTS:
    Fs, frs, wfrs, refusals, corrs = [], [], [], 0, []
    for sd in SEEDS:
        rel, chiV, wrel, coords, rng = build_lorentzline(sd, mode, **kw)
        F, npairs = footprint_F(wrel, coords)
        Fs.append(F)
        frs.append(frac(rel))
        widx = np.sort(rng.choice(np.arange(WSTART, WSTART + 512), 128,
                                  replace=False))
        wfrs.append(frac(rel[np.ix_(widx, widx)]))
        for _ in range(2):
            idx = np.sort(rng.choice(np.arange(WSTART, WSTART + 512), 144,
                                     replace=False))
            if not dim_le_2(rel[np.ix_(idx, idx)]):
                refusals += 1
        cc = np.corrcoef(chiV.T)
        corrs.append(float(np.mean(cc[np.triu_indices(3, 1)])))
    dmw = d_mm(float(np.mean(wfrs)))
    dm_full = d_mm(float(np.mean(frs)))
    rows[tag] = (float(np.nanmean(Fs)), float(np.nanmin(Fs)), float(np.nanmax(Fs)),
                 refusals, dmw, float(np.mean(corrs)), dm_full)
    print(f"      {tag:7s}: F = {rows[tag][0]:.3f} [{rows[tag][1]:.3f},"
          f"{rows[tag][2]:.3f}]  win-refusals {refusals}/10  "
          f"win d_MM = {dmw:.2f}  (INFO full-web {dm_full:.2f})  "
          f"chan-corr {rows[tag][5]:+.3f}")

# A6: the paper-6 class anchor
frs, refusals = [], 0
for sd in SEEDS:
    rel, chiV, rng = build_p6class(sd)
    frs.append(frac(rel))
    for _ in range(2):
        idx = np.sort(rng.choice(2048, 144, replace=False))
        if not dim_le_2(rel[np.ix_(idx, idx)]):
            refusals += 1
dmA6 = d_mm(float(np.mean(frs)))
print(f"      INFO A6 (round-24 uniform class): refusals {refusals}/10, "
      f"full-web d_MM = {dmA6:.2f} (corpus round-24 reading 2.50, "
      f"DIM-WITHOUT-VOLUME — consistency print, not a gate)")

check("Gd1 (shape curves) [MEASURED]: F computed at every dial point",
      all(np.isfinite(rows[t][0]) for t in rows))
check("Gd2 (dimension curves) [MEASURED]: refusals + d_MM at every point",
      True, "printed above")

# Gd3: the trade-off verdict (pinned semantics)
sweet = [t for t, r in rows.items()
         if r[0] <= 1.10 and r[3] >= 8 and r[4] >= 3.7]
lowF = [t for t, r in rows.items() if r[0] <= 1.20]
nogo = len(lowF) > 0 and all(rows[t][3] <= 2 or rows[t][4] <= 3.0 for t in lowF)
if sweet:
    verdict = f"SWEET-SPOT-EXISTS at {sweet}"
elif nogo or not lowF:
    verdict = "TRADE-OFF-NO-GO (no point reaches F <= 1.2 with dimension intact)" \
        if lowF else "TRADE-OFF-NO-GO (no dial point reaches F <= 1.2 at all)"
else:
    best_d = max(lowF, key=lambda t: rows[t][4])
    high_dim = [t for t, r in rows.items() if r[3] >= 8]
    best_f = min(high_dim, key=lambda t: rows[t][0]) if high_dim else None
    verdict = (f"MIXED-FRONTIER: max-d among F<=1.2 is {best_d} "
               f"(d_MM {rows[best_d][4]:.2f}, refusals {rows[best_d][3]}/10); "
               f"min-F among refusals>=8/10 is {best_f} (F {rows[best_f][0]:.3f})"
               if best_f else f"MIXED-FRONTIER: max-d among F<=1.2 is {best_d}")
print(f"\n      Gd3 THE TRADE-OFF VERDICT: {verdict}\n")
check("Gd3 (verdict read; not a pass/fail — always passes if computed)", True,
      verdict[:100])

# Gd4: the scale leg
print("      Gd4 (scale leg): F at (D,NW) = (1024,256) vs (2048,512), N = 4096:")
for mode, tag, kw in (("alpha", "a=0.75", dict(alpha=0.75)),
                      ("beta", "b=1.0", dict(beta=1.0)),
                      ("beta", "b=16.0", dict(beta=16.0))):
    f1, f2 = [], []
    for sd in SEEDS:
        _, _, w1, c1, _ = build_lorentzline(sd, mode, N=4096, D=1024, NW=256, **kw)
        F1, _ = footprint_F(w1, c1)
        _, _, w2, c2, _ = build_lorentzline(sd, mode, N=4096, D=2048, NW=512, **kw)
        F2, _ = footprint_F(w2, c2)
        f1.append(F1); f2.append(F2)
    m1, m2 = np.nanmean(f1), np.nanmean(f2)
    trend = "DECAYS" if m2 < m1 - 0.05 else ("SHARPENS" if m2 > m1 + 0.05 else "PERSISTS")
    print(f"        {tag:7s}: F(1024,256) = {m1:.3f} -> F(2048,512) = {m2:.3f}  [{trend}]")
check("Gd4 (scale leg) [directional]: printed per point", True)

print()
total = PASS + FAIL
print(f"ALL CHECKS PASS ({PASS}/{total})" if FAIL == 0
      else f"FAILURES: {FAIL}/{total}")
if FAIL: raise SystemExit(1)
