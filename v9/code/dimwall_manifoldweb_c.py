#!/usr/bin/env python3
"""
dimwall_manifoldweb_c.py — v9 round 45c: the pure-dipole kernel
(pin: the Round-45b/45c section of note-3p1-manifoldweb, f115d08,
strictly before this ran). Deposits e*(1 + u.v)/2 — monopole+dipole
ONLY, so acc = (A, D) exactly and K=inf dominance = the Minkowski cone
DA >= |DD| in latent coordinates (the pin's theorem). Wiring reproduces
two 45b rows under the half-cosine flag.

Machinery verbatim from rounds 40-44b (F_iso + card, F_2D, Golumbic,
find_sk/verify_sk, frozen d_mm). New, pinned: the direction-valued
deposit builder (half-cosine clock overlaps) and the Gv1 SVD-embedded
covariance check.
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

def fib_sphere(n):
    i = np.arange(n) + 0.5
    phi = np.arccos(1 - 2 * i / n)
    th = np.pi * (1 + 5 ** 0.5) * i
    return np.column_stack([np.sin(phi) * np.cos(th),
                            np.sin(phi) * np.sin(th), np.cos(phi)])
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

def find_sk(rel, rng, k, tries=8000):
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

# ---- the confetti reference (investigation note, seeds 77000+) ----
def kclock_confetti(rng, N, K):
    t = rng.random(N); x = rng.uniform(-0.5, 0.5, (N, 3))
    dt = t[None, :] - t[:, None]
    if K == "inf":
        dx = np.linalg.norm(x[None, :, :] - x[:, None, :], axis=2)
        rel = (dt > 0) & (dt >= dx)
    else:
        U = fib_sphere(K)
        rel = dt > 0
        proj = x @ U.T
        for k in range(K):
            rel &= (dt - (proj[None, :, k] - proj[:, None, k])) >= 0
    np.fill_diagonal(rel, False)
    return rel, np.column_stack([t, x])

# ---- the grown builder ----
def build_manifold(sd, K, alpha, churn="perclock", kernel="halfcos",
                   N=2048, M=32, L=16, D=1024, NW=256):
    """Direction-valued deposits; kernel='halfcos' (45/45b: max(0,u.v))
    or 'dipole' (45c: (1+u.v)/2 — monopole+dipole only)."""
    rng = np.random.default_rng(sd)
    V = fib_sphere(K)
    P = rng.normal(size=(M, 3))
    P /= np.linalg.norm(P, axis=1, keepdims=True)
    acc = np.zeros((M, K))
    chiV = np.zeros((N, K))
    for t in range(N):
        c = int(rng.integers(M))
        e = rng.exponential(0.109551)
        if rng.random() < alpha:
            u = P[c]
        else:
            u = rng.normal(size=3)
            u /= np.linalg.norm(u)
        if kernel == "halfcos":
            acc[c] += e * np.maximum(0.0, V @ u)
        else:
            acc[c] += e * 0.5 * (1.0 + V @ u)
        chiV[t] = acc[c]
        if churn == "perclock":
            for kk in range(K):
                if rng.random() < 1.0 / L:
                    acc[int(rng.integers(M)), kk] = 0.0
        else:
            if rng.random() < 1.0 / L:
                acc[int(rng.integers(M))] = 0.0
    b = np.arange(N)
    rel = b[:, None] < b[None, :]
    for k in range(K):
        rel &= chiV[:, None, k] <= chiV[None, :, k]
    np.fill_diagonal(rel, False)
    start = (N - D) // 2
    idx = np.sort(rng.choice(np.arange(start, start + D), NW, replace=False))
    coords = np.column_stack([idx.astype(float), chiV[idx]])
    wrel = rel[np.ix_(idx, idx)]
    return rel, chiV, wrel, coords, rng

def svd_embed(rel, dims=4):
    """Order-only coordinates: top singular vectors of the centered
    relation matrix (Johnston-style; paper-14-cited)."""
    A = rel.astype(float)
    A = A - A.mean(0)[None, :] - A.mean(1)[:, None] + A.mean()
    U, S, Vt = np.linalg.svd(A, full_matrices=False)
    return U[:, :dims] * S[:dims]

print("[manifold web — round 45]")

# ---- Gm0: calibration ----
CARD43B = {"iso": (1.050, 1.112), "disk": (3.009, 3.087),
           "p12": (2.121, 2.183), "p045": (2.550, 2.625),
           "simp": (1.545, 1.575)}
SC = [20262500 + i for i in range(5)]
def card(name, gen):
    Fs = []
    for sd in SC:
        rng = np.random.default_rng(sd)
        Fs.append(F_iso_cloud(gen(rng))[0])
    return (round(float(np.nanmin(Fs)), 3), round(float(np.nanmax(Fs)), 3)) \
        == CARD43B[name]
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
          card("disk", disk) and card("p12", lambda r: plane_eig(r, 0.12))
          and card("p045", lambda r: plane_eig(r, 0.045))
          and card("simp", simplex_cloud))
Fm4 = []
for sd in [20262400 + i for i in range(5)]:
    rng = np.random.default_rng(sd)
    rel, P = m4diamond(rng, 256)
    Fm4.append(F_iso_cloud(transverse(rel, P, "m4"))[0])
Fm4 = np.array(Fm4)
oka = (round(Fm4.min(), 3), round(Fm4.max(), 3)) == (1.080, 1.130)
# the confetti continuity anchor (investigation-note numbers, same seeds)
# K=4 corrected to the canonical instrument (note-round-cone-
# mechanisms, round-45 correction: the probe variant lacked the PCA
# sign convention; 0.003 shift at K=4 only)
CONF = {4: 1.454, 8: 1.132, 16: 1.055, "inf": 1.046}
okc = True
for K, expect in CONF.items():
    Fs = []
    for sd in range(5):
        rng = np.random.default_rng(77000 + sd)
        rel, P = kclock_confetti(rng, 512, K)
        Fs.append(F_iso_cloud(transverse(rel, P, "m4"))[0])
    got = round(float(np.nanmean(Fs)), 3)
    okc &= got == expect
    print(f"      confetti K={str(K):4s}: F_iso {got} vs note {expect}")
check("Gm0 (calibration): card + M4 anchor + the confetti reference "
      "trajectory all reproduce exactly", okcard and oka and okc)
if not (okcard and oka and okc):
    print("CALIBRATION REFUSAL."); print("FAILURES: 1"); raise SystemExit(1)
MAXM4 = float(Fm4.max())

# ---- Gw (wiring): two round-45b rows under the half-cosine flag ----
R45B = {(4, 0.0): 1.774, (4, 0.75): 1.876}
okw = True
for (K, alpha), expect in R45B.items():
    Fs = []
    for sd in [20262800 + i for i in range(5)]:
        rel, chiV, wrel, coords, rng = build_manifold(sd, K, alpha,
                                                      churn="full",
                                                      kernel="halfcos")
        Fs.append(F_iso_cloud(transverse(wrel, coords))[0])
    got = round(float(np.nanmean(Fs)), 3)
    okw &= got == expect
    print(f"      wiring K={K} a={alpha}: F_iso {got} vs 45b's {expect}")
check("Gw (wiring): 45b rows reproduced under the half-cosine flag", okw)
if not okw:
    print("WIRING REFUSAL."); print("FAILURES: 1"); raise SystemExit(1)

# ---- Gm1/Gm2: the grid (full churn, PURE-DIPOLE kernel) ----
SEEDS = [20262800 + i for i in range(5)]
WSTART = (2048 - 512) // 2
rows = {}
print(f"    the grid (parking: F_iso <= {1.1*MAXM4:.3f}, refusals >= 8/10, "
      f"win d_MM >= 3.7, S4 >= 3/5):")
for K in (4, 8, 12, 16, 24):
    for alpha in (0.0, 0.75):
        Fs, F2s, eigs, prs, frs, wfrs, refusals = [], [], [], [], [], [], 0
        Fembs = []
        rels = []
        for sd in SEEDS:
            rel, chiV, wrel, coords, rng = build_manifold(sd, K, alpha,
                                                          churn="full",
                                                          kernel="dipole")
            v = transverse(wrel, coords)
            F, er, dg = F_iso_cloud(v)
            Fs.append(F); F2s.append(F_2D_cloud(v)); eigs.append(er)
            prs.append(len(v))
            frs.append(frac(rel))
            widx = np.sort(rng.choice(np.arange(WSTART, WSTART + 512), 128,
                                      replace=False))
            wfrs.append(frac(rel[np.ix_(widx, widx)]))
            for _ in range(2):
                idx = np.sort(rng.choice(np.arange(WSTART, WSTART + 512),
                                         144, replace=False))
                if not dim_le_2(rel[np.ix_(idx, idx)]):
                    refusals += 1
            # Gv1: order-only embedded F on the windowed subposet
            emb = svd_embed(wrel, dims=4)
            vE = transverse(wrel, emb)
            Fembs.append(F_iso_cloud(vE)[0])
            rels.append((rel, rng))
        dmw = d_mm(float(np.mean(wfrs)))
        rows[(K, alpha)] = dict(F=float(np.nanmean(Fs)),
                                F2=float(np.nanmean(F2s)),
                                Femb=float(np.nanmean(Fembs)),
                                refusals=refusals, dmm=dmw,
                                pairs=int(np.mean(prs)), rels=rels)
        print(f"      K={K:2d} a={alpha:4.2f}: F_iso = {np.nanmean(Fs):6.3f} "
              f"[{np.nanmin(Fs):.3f},{np.nanmax(Fs):.3f}]  "
              f"F_2D {np.nanmean(F2s):5.3f}  F_emb {np.nanmean(Fembs):5.3f}  "
              f"eig3/1 {np.mean(eigs):.3f}  pairs {int(np.mean(prs))}  "
              f"frac {np.mean(frs):.4f}  win-refusals {refusals}/10  "
              f"win d_MM = {dmw:.2f}", flush=True)
check("Gm1: the grid computed at every (K, alpha) point", True)

# Gm2: witness ladder
print("    Gm2 (witness ladder; tries = 8000 disclosed reduced; absence "
      "is never evidence of absence):")
witness = {}
for (K, alpha) in [(4, 0.0), (4, 0.75), (12, 0.0), (12, 0.75),
                   (16, 0.0), (16, 0.75), (24, 0.0), (24, 0.75)]:
    h4 = 0
    h5 = 0
    for (rel, rng) in rows[(K, alpha)]["rels"]:
        r4 = find_sk(rel, rng, 4)
        if r4 and verify_sk(rel, r4[0], r4[1], 4):
            h4 += 1
        if K >= 12:
            r5 = find_sk(rel, rng, 5)
            if r5 and verify_sk(rel, r5[0], r5[1], 5):
                h5 += 1
    witness[(K, alpha)] = (h4, h5)
    print(f"      K={K:2d} a={alpha:4.2f}: S4 {h4}/5"
          + (f", S5 {h5}/5" if K >= 12 else ""), flush=True)
# S6 INFO at K=24
h6 = 0
for (rel, rng) in rows[(24, 0.0)]["rels"]:
    r6 = find_sk(rel, rng, 6, tries=4000)
    if r6 and verify_sk(rel, r6[0], r6[1], 6):
        h6 += 1
print(f"      INFO K=24 a=0: S6 {h6}/5 (tries 4000)")
check("Gm2: the ladder searched per pin", True)

# Gm3: the verdict
cands = [(K, a) for (K, a), r in rows.items()
         if np.isfinite(r["F"]) and r["F"] <= 1.1 * MAXM4
         and r["refusals"] >= 8 and r["dmm"] >= 3.7
         and witness.get((K, a), (0, 0))[0] >= 3]
lowish = [(K, a) for (K, a), r in rows.items()
          if np.isfinite(r["F"]) and r["F"] <= 1.2 * MAXM4
          and r["dmm"] >= 3.0]
if cands:
    verdict = f"GROWTH-REACHES-ROUND at {cands}"
elif not lowish:
    verdict = (f"GROWTH-SPOILS (no point reaches F_iso <= {1.2*MAXM4:.3f} "
               f"with win d_MM >= 3.0)")
else:
    verdict = f"MIXED-FRONTIER: near-misses {lowish}"
print(f"\n      Gm3 THE VERDICT: {verdict}\n")
check("Gm3 (the verdict; a read)", True, verdict[:110])

# Gv1: covariance
natF = [rows[k]["F"] for k in sorted(rows)]
embF = [rows[k]["Femb"] for k in sorted(rows)]
def spearman(a, b):
    ra = np.argsort(np.argsort(a)).astype(float)
    rb = np.argsort(np.argsort(b)).astype(float)
    return float(np.corrcoef(ra, rb)[0, 1])
rho = spearman(natF, embF)
# a directional read, not an exit-1 gate (pin: exit 1 only on Gm0)
check("Gv1 (F-covariance) [directional read]: Spearman(F_native, "
      "F_embedded) across the grid", True,
      f"rho = {rho:.3f} -> "
      + ("ORDER-READABLE (covariant)" if rho >= 0.8
         else "THE PAPER-XIV BOOKKEEPING CAVEAT FIRES (recorded)"))

print()
total = PASS + FAIL
print(f"ALL CHECKS PASS ({PASS}/{total})" if FAIL == 0
      else f"FAILURES: {FAIL}/{total}")
if FAIL: raise SystemExit(1)
