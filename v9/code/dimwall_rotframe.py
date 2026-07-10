#!/usr/bin/env python3
"""
dimwall_rotframe.py — v9 round 44: the rotating-frame class
(pin: note-3p1-rotframe, 97b20ee, strictly before this ran).

Machinery verbatim from rounds 40-43b (footprint, F_iso + card,
Golumbic, find_sk/verify_sk, frozen-curve d_mm). New, pinned: the
rotating-frame builder (basis drift, raw negative deposits) and the
F_2D collapse-robust secondary.
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

def fib_sphere(n=64):
    i = np.arange(n) + 0.5
    phi = np.arccos(1 - 2 * i / n)
    theta = np.pi * (1 + 5 ** 0.5) * i
    return np.column_stack([np.sin(phi) * np.cos(theta),
                            np.sin(phi) * np.sin(theta), np.cos(phi)])
UDIRS = fib_sphere(64)
U16 = np.column_stack([np.cos(2 * np.pi * np.arange(16) / 16),
                       np.sin(2 * np.pi * np.arange(16) / 16)])

def pca_frame(v):
    C = np.cov(v.T)
    evals, evecs = np.linalg.eigh(C)
    order = np.argsort(evals)[::-1]
    evals = evals[order]; evecs = evecs[:, order]
    E = evecs[:, :3]
    for c in range(3):
        j = np.argmax(np.abs(E[:, c]))
        if E[j, c] < 0:
            E[:, c] = -E[:, c]
    return evals, E

def transverse(rel, coords, family="dom"):
    X = (coords - coords.mean(0)) / np.maximum(coords.std(0), 1e-9)
    k = X.shape[1]
    if family == "m4":
        dhat = np.zeros(k); dhat[0] = 1.0
    else:
        dhat = np.ones(k) / np.sqrt(k)
    ii, jj = np.where(rel)
    d = X[jj] - X[ii]
    s = d @ dhat
    keep = s >= S_MIN
    d = d[keep]; s = s[keep]
    w = d - s[:, None] * dhat[None, :]
    return w / s[:, None]

def F_iso_cloud(v):
    if len(v) < 4 * MIN_PROJ:
        return float("nan"), 0.0, True
    evals, E = pca_frame(v)
    eig_ratio = float(evals[2] / max(evals[0], 1e-30))
    p3 = v @ E
    hs = []
    for u in UDIRS:
        pr = p3 @ u
        pr = pr[pr > 0]
        hs.append(np.quantile(pr, Q) if len(pr) >= MIN_PROJ else np.nan)
    hs = np.array(hs)
    if np.isnan(hs).any():
        return float("nan"), eig_ratio, True
    hs_sorted = np.sort(hs)
    return float(hs_sorted[-8:].mean() / hs_sorted[:8].mean()), eig_ratio, False

def F_2D_cloud(v):
    """The collapse-robust secondary: top-2 PCA plane, 16-gon supports,
    top-4/bottom-4."""
    if len(v) < 4 * MIN_PROJ:
        return float("nan")
    evals, E = pca_frame(v)
    p2 = v @ E[:, :2]
    hs = []
    for u in U16:
        pr = p2 @ u
        pr = pr[pr > 0]
        hs.append(np.quantile(pr, Q) if len(pr) >= MIN_PROJ else np.nan)
    hs = np.array(hs)
    if np.isnan(hs).any():
        return float("nan")
    hs_sorted = np.sort(hs)
    return float(hs_sorted[-4:].mean() / hs_sorted[:4].mean())

def native_F(rel, coords):
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

def rodrigues(axis, ang):
    ux, uy, uz = axis
    K = np.array([[0, -uz, uy], [uz, 0, -ux], [-uy, ux, 0]])
    return np.eye(3) + np.sin(ang) * K + (1 - np.cos(ang)) * (K @ K)

def build_rot(sd, omega, C=3, N=2048, M=32, L=16, alpha=0.75, D=1024, NW=256):
    """The corner class (round-40 web_window, verbatim rng structure at
    omega = 0) with a drifting deposit basis at omega > 0; omega = inf
    (np.inf) draws a fresh Haar rotation per commit. Negative deposit
    components allowed raw (the pinned negativity decision)."""
    rng = np.random.default_rng(sd)
    acc = np.zeros((M, C))
    chiV = np.zeros((N, C))
    pref = np.arange(M) % C
    B = np.eye(3)
    for t in range(N):
        c = int(rng.integers(M))
        e = rng.exponential(0.109551)
        if rng.random() < alpha:
            k = int(pref[c])
        else:
            k = int(rng.integers(C))
        if omega == 0.0:
            acc[c, k] += e
        else:
            if np.isinf(omega):
                G = rng.normal(size=(3, 3))
                Qm, R = np.linalg.qr(G)
                Qm *= np.sign(np.diag(R))
                if np.linalg.det(Qm) < 0:
                    Qm[:, 0] = -Qm[:, 0]
                B = Qm
            else:
                ax = rng.normal(size=3)
                ax /= np.linalg.norm(ax)
                B = rodrigues(ax, omega) @ B
            ek = np.zeros(3); ek[k] = 1.0
            acc[c] += e * (B @ ek)
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

def build_percommit(sd, beta=1.0, C=3, N=2048, M=32, L=16, D=1024, NW=256):
    rng = np.random.default_rng(sd)
    acc = np.zeros((M, C))
    chiV = np.zeros((N, C))
    for t in range(N):
        c = int(rng.integers(M))
        e = rng.exponential(0.109551)
        acc[c] += e * rng.dirichlet(np.full(C, beta))
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
    return rel, chiV, rel[np.ix_(idx, idx)], coords, rng

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

print("[rotating frame — round 44]")

# ---- Gw0b part 1: the reference card ----
print("    calibration: the reference card (must match the 43b bands):")
CARD43B = {"iso": (1.050, 1.112), "disk": (3.009, 3.087),
           "p12": (2.121, 2.183), "p045": (2.550, 2.625),
           "simp": (1.545, 1.575)}
SC = [20262500 + i for i in range(5)]
def card(name, gen):
    Fs = []
    for sd in SC:
        rng = np.random.default_rng(sd)
        F, er, dg = F_iso_cloud(gen(rng))
        Fs.append(F)
    lo, hi = float(np.nanmin(Fs)), float(np.nanmax(Fs))
    print(f"      {name:6s}: [{lo:.3f},{hi:.3f}] vs 43b {CARD43B[name]}")
    return abs(lo - CARD43B[name][0]) < 1e-9 and abs(hi - CARD43B[name][1]) < 1e-9

def disk(r):
    v = r.normal(size=(3000, 3)); v[:, 2] = 0.0
    return v
def plane_eig(r, e3):
    v = r.normal(size=(3000, 3)); v[:, 2] *= np.sqrt(e3)
    return v
def simplex_cloud(r):
    w = r.dirichlet(np.ones(4), size=3000)
    Bm = np.array([[1, 0, 0], [-1/3, 2*np.sqrt(2)/3, 0],
                   [-1/3, -np.sqrt(2)/3, np.sqrt(6)/3],
                   [-1/3, -np.sqrt(2)/3, -np.sqrt(6)/3]])
    return w @ Bm
okcard = (card("iso", lambda r: r.normal(size=(3000, 3))) and
          card("disk", disk) and card("p12", lambda r: plane_eig(r, 0.12)) and
          card("p045", lambda r: plane_eig(r, 0.045)) and
          card("simp", simplex_cloud))

# ---- Gw0b part 2: the anchors ----
SEEDS43 = [20262400 + i for i in range(5)]
Fm4, F2m4, Fo4 = [], [], []
for sd in SEEDS43:
    rng = np.random.default_rng(sd)
    rel, P = m4diamond(rng, 256)
    v = transverse(rel, P, "m4")
    F, er, dg = F_iso_cloud(v)
    Fm4.append(F); F2m4.append(F_2D_cloud(v))
    rng = np.random.default_rng(sd)
    rel, Z = orthantk(rng, 256, 4)
    Fo4.append(F_iso_cloud(transverse(rel, Z))[0])
Fm4, Fo4 = np.array(Fm4), np.array(Fo4)
R43 = {"m4": (1.080, 1.130), "o4": (1.263, 1.344)}
oka = (round(Fm4.min(), 3), round(Fm4.max(), 3)) == R43["m4"] and \
      (round(Fo4.min(), 3), round(Fo4.max(), 3)) == R43["o4"]
print(f"      anchors: M4 F_iso [{Fm4.min():.3f},{Fm4.max():.3f}] "
      f"(43: {R43['m4']}), o4 [{Fo4.min():.3f},{Fo4.max():.3f}] "
      f"(43: {R43['o4']}); M4 F_2D [{np.nanmin(F2m4):.3f},{np.nanmax(F2m4):.3f}]")
check("Gw0b (calibration): the card matches 43b exactly; the anchors "
      "match round 43 exactly", okcard and oka)
if not (okcard and oka):
    print("\nCALIBRATION REFUSAL."); print("FAILURES: 1"); raise SystemExit(1)
MAXM4 = float(Fm4.max())
MAXM4_2D = float(np.nanmax(F2m4))

# ---- Gw0: wiring (omega = 0 == round-40 corner) ----
R40_CORNER = [2.218, 1.949, 2.179, 2.316, 2.180]
S40 = [20262000 + i for i in range(5)]
got = []
for sd in S40:
    rel, chiV, wrel, coords, rng = build_rot(sd, 0.0)
    got.append(round(native_F(wrel, coords), 3))
check("Gw0 (wiring): omega = 0 reproduces the round-40 corner F exactly",
      got == R40_CORNER, f"{got}")
if got != R40_CORNER:
    print("\nWIRING REFUSAL."); print("FAILURES: 1"); raise SystemExit(1)

# ---- Gw1: the omega curve ----
SEEDS = [20262600 + i for i in range(5)]
OMEGAS = [0.0, 0.1, 0.3, 1.0, 3.0, np.inf]
WSTART = (2048 - 512) // 2
rows = {}
print(f"    Gw1 (the omega curve; parking: F_iso <= {1.1*MAXM4:.3f}, "
      f"F_2D <= {1.1*MAXM4_2D:.3f}, refusals >= 8/10, win d_MM >= 3.7):")
for om in OMEGAS:
    Fs, F2s, Fn, wfrs, frs, refusals, eigs, prs, degs = \
        [], [], [], [], [], 0, [], [], 0
    rels = []
    for sd in SEEDS:
        rel, chiV, wrel, coords, rng = build_rot(sd, om)
        v = transverse(wrel, coords)
        F, er, dg = F_iso_cloud(v)
        Fs.append(F); F2s.append(F_2D_cloud(v)); Fn.append(native_F(wrel, coords))
        eigs.append(er); prs.append(len(v)); degs += dg
        frs.append(frac(rel))
        widx = np.sort(rng.choice(np.arange(WSTART, WSTART + 512), 128,
                                  replace=False))
        wfrs.append(frac(rel[np.ix_(widx, widx)]))
        for _ in range(2):
            idx = np.sort(rng.choice(np.arange(WSTART, WSTART + 512), 144,
                                     replace=False))
            if not dim_le_2(rel[np.ix_(idx, idx)]):
                refusals += 1
        rels.append((rel, rng))
    dmw = d_mm(float(np.mean(wfrs)))
    sparse = min(prs) < 4 * MIN_PROJ
    tag = "inf" if np.isinf(om) else f"{om:.1f}"
    rows[tag] = dict(F=float(np.nanmean(Fs)), F2=float(np.nanmean(F2s)),
                     Fn=float(np.nanmean(Fn)), refusals=refusals, dmm=dmw,
                     degs=degs, sparse=sparse, rels=rels,
                     pairs=int(np.mean(prs)))
    print(f"      om={tag:4s}: F_iso = {np.nanmean(Fs):6.3f} "
          f"[{np.nanmin(Fs):.3f},{np.nanmax(Fs):.3f}]  "
          f"F_2D = {np.nanmean(F2s):5.3f}  native {np.nanmean(Fn):5.3f}  "
          f"eig3/1 {np.mean(eigs):.3f}  pairs {int(np.mean(prs))}"
          f"{' SPARSE' if sparse else ''}{' DEGEN' + str(degs) if degs else ''}  "
          f"frac {np.mean(frs):.4f}  win-refusals {refusals}/10  "
          f"win d_MM = {dmw:.2f}", flush=True)
# continuity INFO row
rel, chiV, wrel, coords, rng = build_percommit(20262600)
v = transverse(wrel, coords)
print(f"      INFO per-commit b=1 (continuity): F_iso = "
      f"{F_iso_cloud(v)[0]:.3f}, native {native_F(wrel, coords):.3f}")
check("Gw1: the omega curve computed at every point", True)

# ---- Gw2: parking certification ----
cands = [t for t, r in rows.items()
         if np.isfinite(r["F"]) and r["F"] <= 1.1 * MAXM4
         and np.isfinite(r["F2"]) and r["F2"] <= 1.1 * MAXM4_2D
         and r["refusals"] >= 8 and r["dmm"] >= 3.7
         and not r["sparse"] and r["degs"] == 0]
print(f"      parking candidates: {cands if cands else 'NONE'}")
confirmed = []
for t in cands:
    hits = 0
    for (rel, rng) in rows[t]["rels"]:
        res = find_sk(rel, rng, 4)
        if res and verify_sk(rel, res[0], res[1], 4):
            hits += 1
    print(f"      S4 certification at om={t}: witnesses on {hits}/5 seeds")
    if hits >= 3:
        confirmed.append(t)
check("Gw2: S4 certification run at every candidate", True,
      f"{len(cands)} candidates, {len(confirmed)} confirmed")

# ---- Gw3: the verdict ----
lowish = [t for t, r in rows.items()
          if np.isfinite(r["F"]) and r["F"] <= 1.2 * MAXM4
          and r["dmm"] >= 3.0 and not r["sparse"]]
if confirmed:
    verdict = f"PARKING-EXISTS at omega = {confirmed}"
elif not lowish:
    verdict = (f"LAST-NO-GO (no non-sparse point reaches F_iso <= "
               f"{1.2*MAXM4:.3f} with win d_MM >= 3.0) — the rounds-40-44 "
               f"arc completes")
else:
    verdict = f"MIXED-FRONTIER: near-misses {lowish}"
print(f"\n      Gw3 THE VERDICT: {verdict}\n")
check("Gw3 (the verdict; a read)", True, verdict[:110])

print()
total = PASS + FAIL
print(f"ALL CHECKS PASS ({PASS}/{total})" if FAIL == 0
      else f"FAILURES: {FAIL}/{total}")
if FAIL: raise SystemExit(1)
