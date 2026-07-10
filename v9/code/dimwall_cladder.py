#!/usr/bin/env python3
"""
dimwall_cladder.py — v9 round 43: the large-C parking hypothesis
(pin: note-3p1-cladder, 16ea808, strictly before this ran).

Machinery provenance (verbatim): builders + native footprint + Golumbic
+ windowed metric from dimwall_dialsweep{,_b}.py; find_sk/verify_sk
from dimwall_witness.py. New, pinned here: the F_iso effective-3-frame
isotropy statistic (PCA top-3 + 64-direction Fibonacci sphere).
"""
import json
import numpy as np

PASS = FAIL = 0
def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    if ok: PASS += 1
    else: FAIL += 1
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""), flush=True)

S_MIN = 0.3
Q = 0.9
MIN_PROJ = 30

# ---- pinned Fibonacci sphere (64 directions) ----
def fib_sphere(n=64):
    i = np.arange(n) + 0.5
    phi = np.arccos(1 - 2 * i / n)
    theta = np.pi * (1 + 5 ** 0.5) * i
    return np.column_stack([np.sin(phi) * np.cos(theta),
                            np.sin(phi) * np.sin(theta), np.cos(phi)])
UDIRS = fib_sphere(64)

def transverse_cloud(rel, coords):
    X = (coords - coords.mean(0)) / np.maximum(coords.std(0), 1e-9)
    k = X.shape[1]
    dhat = np.ones(k) / np.sqrt(k)
    ii, jj = np.where(rel)
    d = X[jj] - X[ii]
    s = d @ dhat
    keep = s >= S_MIN
    d = d[keep]; s = s[keep]
    w = d - s[:, None] * dhat[None, :]
    return w / s[:, None]

def F_iso(rel, coords):
    """Effective-3-frame isotropy: PCA top-3 of the v-cloud, directional
    q90 supports on the pinned sphere; top-8/bottom-8 support ratio.
    Returns (F, npairs, eig_ratio3, degenerate_flag)."""
    v = transverse_cloud(rel, coords)
    if len(v) < 4 * MIN_PROJ:
        return float("nan"), len(v), 0.0, True
    C = np.cov(v.T)
    evals, evecs = np.linalg.eigh(C)
    order = np.argsort(evals)[::-1]
    evals = evals[order]; evecs = evecs[:, order]
    E = evecs[:, :3]
    for c in range(3):                       # sign convention
        j = np.argmax(np.abs(E[:, c]))
        if E[j, c] < 0:
            E[:, c] = -E[:, c]
    eig_ratio = float(evals[2] / max(evals[0], 1e-30))
    degen = eig_ratio < 1e-6
    p3 = v @ E
    hs = []
    for u in UDIRS:
        pr = p3 @ u
        pr = pr[pr > 0]
        hs.append(np.quantile(pr, Q) if len(pr) >= MIN_PROJ else np.nan)
    hs = np.array(hs)
    if np.isnan(hs).any():
        return float("nan"), len(v), eig_ratio, True
    hs_sorted = np.sort(hs)
    F = float(hs_sorted[-8:].mean() / hs_sorted[:8].mean())
    return F, len(v), eig_ratio, degen

# ---- native footprint (verbatim, rounds 40/42) — for wiring + C=3 INFO ----
def footprint_native(rel, coords):
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
    keep = s >= S_MIN
    d = d[keep]; s = s[keep]
    w = d - s[:, None] * dhat[None, :]
    v = w / s[:, None]
    hs_c, hs_f = [], []
    for u in dirs:
        p = v @ u; p = p[p > 0]
        hs_c.append(np.quantile(p, Q) if len(p) >= MIN_PROJ else np.nan)
        m = v @ (-u); m = m[m > 0]
        hs_f.append(np.quantile(m, Q) if len(m) >= MIN_PROJ else np.nan)
    return float(np.mean(hs_c) / np.mean(hs_f))

# ---- builders (verbatim conventions from dialsweep_b) ----
def build(sd, variant, beta=None, C=3, N=2048, M=32, L=16, D=1024, NW=256):
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
        elif variant == "equal-pc":
            acc[c] += e / C
        else:
            raise ValueError(variant)
        chiV[t] = acc[c]
        if variant in ("perslot-pc", "equal-pc"):
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

# ---- anchors ----
def m4diamond(rng, N):
    P = np.empty((0, 4))
    while len(P) < N:
        t = rng.random(6 * N)
        x = rng.uniform(-0.5, 0.5, (6 * N, 3))
        r = np.linalg.norm(x, axis=1)
        keep = (r <= t) & (r <= 1 - t)
        P = np.vstack([P, np.column_stack([t[keep], x[keep]])])
    P = P[:N]
    dt = P[None, :, 0] - P[:, None, 0]
    dx = np.linalg.norm(P[None, :, 1:] - P[:, None, 1:], axis=2)
    rel = (dt > 0) & (dt >= dx)
    np.fill_diagonal(rel, False)
    return rel, P

def orthantk(rng, N, k):
    Z = rng.random((N, k))
    rel = np.ones((N, N), dtype=bool)
    for j in range(k):
        rel &= Z[:, None, j] < Z[None, :, j]
    np.fill_diagonal(rel, False)
    return rel, Z

# ---- dimension machinery (verbatim) ----
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

def find_sk(rel, rng, k, tries=20000):
    n = rel.shape[0]
    comp = rel | rel.T
    nodes = np.arange(n)
    for _ in range(tries):
        perm = rng.permutation(n)
        A = []
        for v in perm:
            if not A or not comp[v, A].any():
                A.append(int(v))
                if len(A) == k:
                    break
        if len(A) < k:
            continue
        Aa = np.array(A)
        mask = np.ones(n, dtype=bool)
        mask[Aa] = False
        others = nodes[mask]
        above = rel[np.ix_(Aa, others)]
        cand = above.sum(0) == k - 1
        if not cand.any():
            continue
        cnodes = others[cand]
        miss = np.argmin(above[:, cand], axis=0)
        keep = ~comp[Aa[miss], cnodes]
        buckets = [cnodes[keep & (miss == i)] for i in range(k)]
        if any(len(bk) == 0 for bk in buckets):
            continue
        for _ in range(60):
            B = [int(bk[int(rng.integers(len(bk)))]) for bk in buckets]
            if len(set(B)) == k and not any(
                    comp[B[i], B[j]]
                    for i in range(k) for j in range(i + 1, k)):
                return A, B
    return None

def verify_sk(rel, A, B, k):
    for i in range(k):
        for j in range(k):
            if i != j and (rel[A[i], A[j]] or rel[B[i], B[j]]):
                return False
            if bool(rel[A[i], B[j]]) != (i != j):
                return False
            if rel[B[j], A[i]]:
                return False
        if rel[A[i], B[i]] or rel[B[i], A[i]]:
            return False
    return True

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

print("[c-ladder — round 43]", flush=True)
SEEDS = [20262400 + i for i in range(5)]
SB42 = [20262300 + i for i in range(5)]

# ---- Gc0: certification of F_iso ----
print("    Gc0 anchors (F_iso through the same pipeline):", flush=True)
Fm4, Fo4, Fo9 = [], [], []
for sd in SEEDS:
    rng = np.random.default_rng(sd)
    rel, P = m4diamond(rng, 256)
    F, npairs, er, dg = F_iso(rel, P)
    Fm4.append(F)
    print(f"      m4       seed {sd}: F_iso = {F:6.3f} (pairs {npairs}, "
          f"eig3/eig1 {er:.3f}{', DEGEN' if dg else ''})")
for name, k, sink in (("orthant4", 4, Fo4), ("orthant9", 9, Fo9)):
    for sd in SEEDS:
        rng = np.random.default_rng(sd)
        rel, Z = orthantk(rng, 256, k)
        F, npairs, er, dg = F_iso(rel, Z)
        sink.append(F)
        print(f"      {name} seed {sd}: F_iso = {F:6.3f} (pairs {npairs}, "
              f"eig3/eig1 {er:.3f}{', DEGEN' if dg else ''})")
Fm4, Fo4, Fo9 = map(np.array, (Fm4, Fo4, Fo9))
ok0 = np.isfinite(np.concatenate([Fm4, Fo4, Fo9])).all() and \
      min(Fo4.min(), Fo9.min()) > Fm4.max()
check("Gc0 (certification): min orthant-4/9 F_iso > max M4 F_iso, 5/5 each",
      ok0, f"M4 [{Fm4.min():.3f},{Fm4.max():.3f}] vs o4 "
      f"[{Fo4.min():.3f},{Fo4.max():.3f}] o9 [{Fo9.min():.3f},{Fo9.max():.3f}]")
if not ok0:
    print("\nVOID-INSTRUMENT: F_iso certification refused; no web is read.")
    print("FAILURES: 1")
    raise SystemExit(1)

# ---- Gc-w: wiring (native F, 42b fv rows at C = 3) ----
R42B = {1.0: (1.617, 1.481, 1.731), 4.0: (1.484, 1.417, 1.620),
        16.0: (1.270, 1.227, 1.331)}
okw = True
for b, (m, lo, hi) in R42B.items():
    Fs = []
    for sd in SB42:
        rel, chiV, wrel, coords, rng = build(sd, "perslot-full", beta=b, C=3)
        Fs.append(footprint_native(wrel, coords))
    got = (round(float(np.mean(Fs)), 3), round(float(np.min(Fs)), 3),
           round(float(np.max(Fs)), 3))
    okw &= got == (m, lo, hi)
    print(f"      wiring fv b={b}: {got} vs {(m, lo, hi)}")
check("Gc-w (wiring): 42b fv rows reproduced at 3 d.p.", okw)

# ---- Gc1: the ladder ----
MAXM4 = float(Fm4.max())
WSTART = (2048 - 512) // 2
rows = {}
print(f"    Gc1 (the ladder; parking thresholds: F_iso <= "
      f"{1.1 * MAXM4:.3f}, refusals >= 8/10, win d_MM >= 3.7):", flush=True)
for C in (3, 4, 6, 8):
    for b in (1.0, 4.0, 16.0, 64.0):
        Fs, wfrs, refusals, degs, eig3 = [], [], 0, 0, []
        rels = []
        for sd in SEEDS:
            rel, chiV, wrel, coords, rng = build(sd, "perslot-full",
                                                 beta=b, C=C)
            F, npairs, er, dg = F_iso(wrel, coords)
            Fs.append(F); degs += dg; eig3.append(er)
            widx = np.sort(rng.choice(np.arange(WSTART, WSTART + 512), 128,
                                      replace=False))
            wfrs.append(frac(rel[np.ix_(widx, widx)]))
            for _ in range(2):
                idx = np.sort(rng.choice(np.arange(WSTART, WSTART + 512),
                                         144, replace=False))
                if not dim_le_2(rel[np.ix_(idx, idx)]):
                    refusals += 1
            rels.append((rel, rng))
        dmw = d_mm(float(np.mean(wfrs)))
        Fm = float(np.nanmean(Fs))
        rows[(C, b)] = dict(F=Fm, refusals=refusals, dmm=dmw, degs=degs,
                            rels=rels)
        print(f"      C={C} b={b:5.1f}: F_iso = {Fm:6.3f} "
              f"[{np.nanmin(Fs):.3f},{np.nanmax(Fs):.3f}]"
              f"{'  DEGEN(' + str(degs) + '/5)' if degs else ''}  "
              f"win-refusals {refusals}/10  win d_MM = {dmw:.2f}  "
              f"eig3/1 {np.mean(eig3):.3f}", flush=True)
    # INFO: the dimension-preserving baseline at this C
    Fs, wfrs, refusals = [], [], 0
    for sd in SEEDS:
        rel, chiV, wrel, coords, rng = build(sd, "equal-pc", C=C)
        F, npairs, er, dg = F_iso(wrel, coords)
        Fs.append(F)
        widx = np.sort(rng.choice(np.arange(WSTART, WSTART + 512), 128,
                                  replace=False))
        wfrs.append(frac(rel[np.ix_(widx, widx)]))
        for _ in range(2):
            idx = np.sort(rng.choice(np.arange(WSTART, WSTART + 512), 144,
                                     replace=False))
            if not dim_le_2(rel[np.ix_(idx, idx)]):
                refusals += 1
    print(f"      INFO C={C} equal-split/per-channel-churn: F_iso = "
          f"{np.nanmean(Fs):6.3f}  refusals {refusals}/10  "
          f"win d_MM = {d_mm(float(np.mean(wfrs))):.2f}", flush=True)
check("Gc1: the ladder computed at every (C, beta) point", True)

# ---- Gc2: parking candidates + S4 certification ----
cands = [(C, b) for (C, b), r in rows.items()
         if r["F"] <= 1.1 * MAXM4 and r["refusals"] >= 8
         and r["dmm"] >= 3.7 and r["degs"] == 0]
print(f"      parking candidates: {cands if cands else 'NONE'}")
confirmed = []
for (C, b) in cands:
    hits = 0
    for (rel, rng) in rows[(C, b)]["rels"]:
        res = find_sk(rel, rng, 4)
        if res and verify_sk(rel, res[0], res[1], 4):
            hits += 1
    print(f"      S4 certification at C={C} b={b}: witnesses on {hits}/5 seeds")
    if hits >= 3:
        confirmed.append((C, b))
check("Gc2: S4 certification run at every candidate", True,
      f"{len(cands)} candidates, {len(confirmed)} confirmed")

# ---- Gc3: the verdict ----
lowish = [(C, b) for (C, b), r in rows.items()
          if np.isfinite(r["F"]) and r["F"] <= 1.2 * MAXM4 and r["dmm"] >= 3.0]
if confirmed:
    verdict = f"PARKING-EXISTS at {confirmed}"
elif not lowish:
    verdict = ("UNIVERSAL-FRONTIER (no point reaches F_iso <= "
               f"{1.2 * MAXM4:.3f} with win d_MM >= 3.0)")
else:
    verdict = f"MIXED-FRONTIER: near-misses {lowish}"
print(f"\n      Gc3 THE VERDICT: {verdict}\n")
check("Gc3 (the verdict; a read)", True, verdict[:110])

print()
total = PASS + FAIL
print(f"ALL CHECKS PASS ({PASS}/{total})" if FAIL == 0
      else f"FAILURES: {FAIL}/{total}")
if FAIL: raise SystemExit(1)
