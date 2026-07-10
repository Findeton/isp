#!/usr/bin/env python3
"""
dimwall_rotframe_b.py — v9 round 44b: the drift-tuned diagonal+noise
class (the dichotomy's untested corner) + the omega=inf mechanism-morph
decomposition. Pin: note-3p1-rotframe round-44 corrections section
(6e76e24, strictly before this ran). Machinery verbatim from
dimwall_rotframe.py.
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

def build_drift(sd, rho, C=3, N=2048, M=32, L=16, D=1024, NW=256):
    """The drift-tuned diagonal+noise class: deposit = e*(rho*diag + z),
    z ~ N(0, I3), raw signed; slots + per-channel churn kept."""
    rng = np.random.default_rng(sd)
    acc = np.zeros((M, C))
    chiV = np.zeros((N, C))
    diag = np.ones(3) / np.sqrt(3.0)
    for t in range(N):
        c = int(rng.integers(M))
        e = rng.exponential(0.109551)
        z = rng.normal(size=3)
        acc[c] += e * (rho * diag + z)
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

def rodrigues(axis, ang):
    ux, uy, uz = axis
    K = np.array([[0, -uz, uy], [uz, 0, -ux], [-uy, ux, 0]])
    return np.eye(3) + np.sin(ang) * K + (1 - np.cos(ang)) * (K @ K)

def build_rot_inf(sd, C=3, N=2048, M=32, L=16, alpha=0.75):
    """The round-44 omega = inf builder (verbatim rng structure),
    returning slot ids for the Gz2 decomposition."""
    rng = np.random.default_rng(sd)
    acc = np.zeros((M, C))
    chiV = np.zeros((N, C))
    slot = np.zeros(N, dtype=int)
    pref = np.arange(M) % C
    for t in range(N):
        c = int(rng.integers(M))
        slot[t] = c
        e = rng.exponential(0.109551)
        if rng.random() < alpha:
            k = int(pref[c])
        else:
            k = int(rng.integers(C))
        G = rng.normal(size=(3, 3))
        Qm, R = np.linalg.qr(G)
        Qm *= np.sign(np.diag(R))
        if np.linalg.det(Qm) < 0:
            Qm[:, 0] = -Qm[:, 0]
        ek = np.zeros(3); ek[k] = 1.0
        acc[c] += e * (Qm @ ek)
        chiV[t] = acc[c]
        for kk in range(C):
            if rng.random() < 1.0 / L:
                acc[int(rng.integers(M)), kk] = 0.0
    b = np.arange(N)
    rel = b[:, None] < b[None, :]
    for k in range(C):
        rel &= chiV[:, None, k] <= chiV[None, :, k]
    np.fill_diagonal(rel, False)
    return rel, chiV, slot

print("[rotating frame 44b — the drift-tuned corner + the morph record]")

# ---- Gz0: calibration ----
SEEDS43 = [20262400 + i for i in range(5)]
Fm4, Fo4 = [], []
for sd in SEEDS43:
    rng = np.random.default_rng(sd)
    rel, P = m4diamond(rng, 256)
    Fm4.append(F_iso_cloud(transverse(rel, P, "m4"))[0])
    rng = np.random.default_rng(sd)
    rel, Z = orthantk(rng, 256, 4)
    Fo4.append(F_iso_cloud(transverse(rel, Z))[0])
Fm4, Fo4 = np.array(Fm4), np.array(Fo4)
oka = (round(Fm4.min(), 3), round(Fm4.max(), 3)) == (1.080, 1.130) and \
      (round(Fo4.min(), 3), round(Fo4.max(), 3)) == (1.263, 1.344)
check("Gz0 (calibration): the round-43 anchor bands reproduced exactly", oka,
      f"M4 [{Fm4.min():.3f},{Fm4.max():.3f}], o4 [{Fo4.min():.3f},{Fo4.max():.3f}]")
if not oka:
    print("CALIBRATION REFUSAL."); print("FAILURES: 1"); raise SystemExit(1)
MAXM4 = float(Fm4.max())

# ---- Gz1: the drift-tuned class ----
SEEDS = [20262700 + i for i in range(5)]
WSTART = (2048 - 512) // 2
print("    Gz1 (drift-tuned diagonal+noise; the registered prediction: "
      "fraction -> 1, win d_MM -> 2, F_iso -> 1 with healthy eigenvalues):")
rows = {}
for rho in (0.0, 0.5, 1.0, 2.0, 4.0):
    Fs, F2s, frs, wfrs, refusals, eigs, prs = [], [], [], [], 0, [], []
    for sd in SEEDS:
        rel, chiV, wrel, coords, rng = build_drift(sd, rho)
        v = transverse(wrel, coords)
        F, er, dg = F_iso_cloud(v)
        Fs.append(F); F2s.append(F_2D_cloud(v)); eigs.append(er)
        prs.append(len(v))
        frs.append(frac(rel))
        widx = np.sort(rng.choice(np.arange(WSTART, WSTART + 512), 128,
                                  replace=False))
        wfrs.append(frac(rel[np.ix_(widx, widx)]))
        for _ in range(2):
            idx = np.sort(rng.choice(np.arange(WSTART, WSTART + 512), 144,
                                     replace=False))
            if not dim_le_2(rel[np.ix_(idx, idx)]):
                refusals += 1
    dmw = d_mm(float(np.mean(wfrs)))
    rows[rho] = (float(np.nanmean(Fs)), refusals, dmw)
    print(f"      rho={rho:3.1f}: F_iso = {np.nanmean(Fs):6.3f} "
          f"[{np.nanmin(Fs):.3f},{np.nanmax(Fs):.3f}]  "
          f"F_2D = {np.nanmean(F2s):5.3f}  eig3/1 {np.mean(eigs):.3f}  "
          f"pairs {int(np.mean(prs))}  frac {np.mean(frs):.4f}  "
          f"win-frac {np.mean(wfrs):.4f}  win-refusals {refusals}/10  "
          f"win d_MM = {dmw:.2f}", flush=True)
check("Gz1: the drift dial computed at every rho", True)

# the read
hi = rows[4.0]
lo = rows[0.0]
pred_ok = hi[2] <= 2.6 and hi[0] <= 1.3
surprise = any(F <= 1.1 * MAXM4 and r >= 8 and d >= 3.7
               for (F, r, d) in rows.values())
if surprise:
    read = "SURPRISE-PARKING candidate present — S4 certification required"
elif pred_ok:
    read = ("PREDICTED-FAILURE-CONFIRMED: high-rho rounds the cloud only as "
            "window dominance trivializes (volume-d toward 2)")
else:
    read = "OTHER — the printed columns are the record"
print(f"\n      Gz1 THE READ: {read}\n")
check("Gz1-read (a read)", True, read[:100])

# ---- Gz2: the omega=inf decomposition (the morph record) ----
print("    Gz2 (omega = inf mechanism-morph decomposition):")
ss_fr, cs_fr, zero_atom = [], [], []
for sd in [20262600 + i for i in range(5)]:
    rel, chiV, slot = build_rot_inf(sd)
    ii, jj = np.where(rel)
    same = slot[ii] == slot[jj]
    n = rel.shape[0]
    tot = n * (n - 1) / 2
    ss_fr.append(same.sum() / tot)
    cs_fr.append((~same).sum() / tot)
    d = chiV[jj] - chiV[ii]
    zero_atom.append(float((np.abs(d) < 1e-12).any(axis=1).mean()))
print(f"      related-pair fraction: same-slot {np.mean(ss_fr):.4f}, "
      f"cross-slot {np.mean(cs_fr):.4f} (total {np.mean(ss_fr)+np.mean(cs_fr):.4f}; "
      f"stationary-coincidence prediction 2^-3 = 0.125)")
print(f"      zero-atom mass among related pairs (some chi-difference "
      f"exactly 0): {np.mean(zero_atom):.3f}")
check("Gz2: the decomposition printed (the morph record)", True)

print()
total = PASS + FAIL
print(f"ALL CHECKS PASS ({PASS}/{total})" if FAIL == 0
      else f"FAILURES: {FAIL}/{total}")
if FAIL: raise SystemExit(1)
