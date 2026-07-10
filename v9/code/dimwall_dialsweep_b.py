#!/usr/bin/env python3
"""
dimwall_dialsweep_b.py — v9 round 42b: the in-family completion
(pin: note-3p1-dialsweep round-42 corrections section, 0b1eac2,
strictly before this ran). Two dials the round-42 grid did not cover:
per-commit Dirichlet weights (Ge1) and per-slot mixing with FULL-VECTOR
churn (Ge2), plus the memo's degenerate endpoint. Machinery verbatim
from dimwall_dialsweep.py.
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

def build(sd, variant, beta=None, C=3, N=2048, M=32, L=16, D=1024, NW=256):
    """variant: 'perslot-pc' (round-42 per-slot Dirichlet, per-channel
    churn — the wiring row); 'percommit-pc' (fresh W per deposit,
    per-channel churn); 'perslot-full' (per-slot W, full-vector churn);
    'equal-full' (exact split, full-vector churn — the degenerate
    endpoint)."""
    rng = np.random.default_rng(sd)
    acc = np.zeros((M, C))
    chiV = np.zeros((N, C))
    if variant in ("perslot-pc", "perslot-full"):
        Wd = rng.dirichlet(np.full(C, beta), size=M)
    for t in range(N):
        c = int(rng.integers(M))
        e = rng.exponential(0.109551)
        if variant in ("perslot-pc", "perslot-full"):
            acc[c] += e * Wd[c]
        elif variant == "percommit-pc":
            acc[c] += e * rng.dirichlet(np.full(C, beta))
        else:  # equal-full
            acc[c] += e / C
        chiV[t] = acc[c]
        if variant in ("perslot-pc", "percommit-pc"):
            for kk in range(C):
                if rng.random() < 1.0 / L:
                    acc[int(rng.integers(M)), kk] = 0.0
        else:
            if rng.random() < 1.0 / L:
                acc[int(rng.integers(M))] = 0.0
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

frozen = json.load(open("v9/data/mm_reference.json"))
ref = {2: frozen["M2"], 3: frozen["M3"], 4: frozen["M4"], 5: frozen["M5"]}
def d_mm(f):
    ds = sorted(ref); fs = [ref[d] for d in ds]
    if f >= fs[0]: return 2.0
    if f <= fs[-1]: return float(ds[-1])
    for a in range(len(ds) - 1):
        if fs[a] >= f >= fs[a + 1]:
            w = (fs[a] - f) / (fs[a] - fs[a + 1])
            return ds[a] + w * (ds[a + 1] - ds[a])
    return float("nan")

def frac(rel):
    n = rel.shape[0]
    return rel.sum() / (n * (n - 1) / 2)

def row(variant, tag, beta, seeds):
    WSTART = (2048 - 512) // 2
    Fs, wfrs, refusals = [], [], 0
    degen = 0
    for sd in seeds:
        rel, chiV, wrel, coords, rng = build(sd, variant, beta=beta)
        F, npairs = footprint_F(wrel, coords)
        if not np.isfinite(F):
            degen += 1
        Fs.append(F)
        widx = np.sort(rng.choice(np.arange(WSTART, WSTART + 512), 128,
                                  replace=False))
        wfrs.append(frac(rel[np.ix_(widx, widx)]))
        for _ in range(2):
            idx = np.sort(rng.choice(np.arange(WSTART, WSTART + 512), 144,
                                     replace=False))
            if not dim_le_2(rel[np.ix_(idx, idx)]):
                refusals += 1
    dmw = d_mm(float(np.mean(wfrs)))
    Fm = float(np.nanmean(Fs)) if degen < len(seeds) else float("nan")
    lo = float(np.nanmin(Fs)) if degen < len(seeds) else float("nan")
    hi = float(np.nanmax(Fs)) if degen < len(seeds) else float("nan")
    print(f"      {tag:16s}: F = {Fm:6.3f} [{lo:.3f},{hi:.3f}]"
          f"{'  DEGENERATE(' + str(degen) + '/5)' if degen else ''}  "
          f"win-refusals {refusals}/10  win d_MM = {dmw:.2f}")
    return Fm, refusals, dmw, degen

print("[dial sweep 42b — the in-family completion]")
S42 = [20262200 + i for i in range(5)]
SB = [20262300 + i for i in range(5)]

# Ge-w: wiring — round-42 per-slot b=1.0 row
R42_B1 = (1.809, 3.94)  # (mean F, win d_MM) from the round-42 print
Fm, refn, dmw, _ = row("perslot-pc", "wiring b=1.0", 1.0, S42)
check("Ge-w (wiring): round-42 per-slot b = 1.0 row reproduced",
      round(Fm, 3) == R42_B1[0] and round(dmw, 2) == R42_B1[1],
      f"F {Fm:.3f} vs {R42_B1[0]}, win d_MM {dmw:.2f} vs {R42_B1[1]}")

print("    Ge1 (per-commit Dirichlet, per-channel churn):")
res = {}
for b in (0.25, 1.0, 4.0):
    res[f"pc b={b}"] = row("percommit-pc", f"per-commit b={b}", b, SB)
print("    Ge2 (per-slot Dirichlet, FULL-VECTOR churn):")
for b in (1.0, 4.0, 16.0):
    res[f"fv b={b}"] = row("perslot-full", f"full-reset b={b}", b, SB)
res["equal-full"] = row("equal-full", "equal+full-reset", None, SB)
print("      (equal+full-reset = the memo's degenerate endpoint: "
      "co-monotone by proof, dim <= 2 expected)")

check("Ge1/Ge2: all rows computed and printed", True)

FLOOR = 1.307   # the orthant-iid band minimum (round 40/42)
beaten = [t for t, (F, rn, dm, dg) in res.items()
          if t != "equal-full" and np.isfinite(F) and F < FLOOR]
verdict = ("FLOOR-BEATEN at " + str(beaten)) if beaten else \
    "FLOOR-HOLDS (no non-degenerate point below the orthant-iid band minimum)"
print(f"\n      Ge3 THE FLOOR VERDICT: {verdict}\n")
check("Ge3 (the floor verdict; a read)", True, verdict)

print()
total = PASS + FAIL
print(f"ALL CHECKS PASS ({PASS}/{total})" if FAIL == 0
      else f"FAILURES: {FAIL}/{total}")
if FAIL: raise SystemExit(1)
