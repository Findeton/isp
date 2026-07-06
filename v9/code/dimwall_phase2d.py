#!/usr/bin/env python3
"""
dimwall_phase2d.py — v9 round 29: THE TIME-WINDOW DIAGNOSIS
(note-3p1-p2d; pin committed at 36ffb48 strictly before this receipt.
NO-REVIEW MODE.)  Central b-windows Delta in {128,256,512,1024,2048},
matched N = 128; Delta* = 512 (tau ~ L*M).  Gates: Gt1 z(2048) >
z(512) on >= 4/5; Gt2 z(512) <= 3 on >= 4/5; Gt3 windowed d_MM >= 3.2
and realizer refusals >= 4/5 at Delta*.  Exit 1 by design on refusal.
"""
import numpy as np

PASS = FAIL = 0
def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    if ok: PASS += 1
    else: FAIL += 1
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

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
    pts = []
    while len(pts) < N:
        t = rng.random()
        x = rng.uniform(-0.5, 0.5, dspace)
        r = np.linalg.norm(x)
        if r <= t and r <= 1 - t:
            pts.append((t, x))
    T = np.array([p[0] for p in pts])
    X = np.array([p[1] for p in pts])
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

def orthant_rel(rng, N, k):
    Z = rng.random((N, k))
    rel = np.ones((N, N), dtype=bool)
    for j in range(k):
        rel &= Z[:, None, j] < Z[None, :, j]
    np.fill_diagonal(rel, False)
    return rel

def web_chiv(sd, C=3, N=2048, M=32, L=16, alpha=0.75):
    rng = np.random.default_rng(sd)
    acc = np.zeros((M, C))
    pref = np.arange(M) % C
    chiV = np.zeros((N, C))
    for t in range(N):
        c = int(rng.integers(M))
        if rng.random() < alpha:
            k = int(pref[c])
        else:
            k = int(rng.integers(C))
        acc[c, k] += rng.exponential(0.109551)
        chiV[t] = acc[c]
        for kk in range(C):
            if rng.random() < 1.0 / L:
                acc[int(rng.integers(M)), kk] = 0.0
    return chiV, rng

def rel_of(idx, chiV, C):
    b = idx
    rel = b[:, None] < b[None, :]
    for k in range(C):
        rel &= chiV[idx][:, None, k] <= chiV[idx][None, :, k]
    np.fill_diagonal(rel, False)
    return rel

def mirsky(rel):
    n = rel.shape[0]
    rem = np.ones(n, dtype=bool)
    H = 0; Wm = 0
    while rem.any():
        pc = (rel & rem[:, None] & rem[None, :]).sum(0)
        minimal = rem & (pc == 0)
        H += 1
        Wm = max(Wm, int(minimal.sum()))
        rem &= ~minimal
    s2 = rel.sum() / (n * (n - 1) / 2)
    return H, Wm, s2

print("[dimwall Phase 2d: the time-window diagnosis]")
NW = 128

# orthant references at N = 128
orth = {}
for k in (3, 4, 5):
    rows = []
    for j in range(8):
        r = np.random.default_rng(20260970 + 100 * k + j)
        H, W, s2 = mirsky(orthant_rel(r, NW, k))
        rows.append((s2, H, W))
    rows = np.array(rows, dtype=float)
    orth[k] = (rows.mean(0), rows.std(0, ddof=1))
    m, s = orth[k]
    print(f"      orthant k={k} @N={NW}: s2 {m[0]:.4f}±{s[0]:.4f}  "
          f"H {m[1]:.1f}±{s[1]:.1f}  W {m[2]:.1f}±{s[2]:.1f}")

def zdist(s2, H, W):
    ps = sorted(orth, key=lambda p: -orth[p][0][0])
    s2s = [orth[p][0][0] for p in ps]
    if not (s2s[-1] <= s2 <= s2s[0]):
        return None
    for a in range(len(ps) - 1):
        if s2s[a] >= s2 >= s2s[a + 1]:
            w = (np.log(s2s[a]) - np.log(s2)) / (np.log(s2s[a]) - np.log(s2s[a + 1]))
            m = np.exp((1 - w) * np.log(orth[ps[a]][0]) + w * np.log(orth[ps[a + 1]][0]))
            sd = (1 - w) * orth[ps[a]][1] + w * orth[ps[a + 1]][1]
            zH = abs(np.log(H) - np.log(m[1])) / (sd[1] / m[1])
            zW = abs(np.log(W) - np.log(m[2])) / (sd[2] / m[2])
            return max(zH, zW)
    return None

# d_MM curve (N-independent)
ref = {}
for d in (1, 2, 3):
    fr = []
    for k in range(8):
        r = np.random.default_rng(20260760 + 10 * d + k)
        rel = (sprinkle_m2(r, 512) if d == 1 else sprinkle_mink(r, 512, d))
        n = rel.shape[0]
        fr.append(rel.sum() / (n * (n - 1) / 2))
    ref[d + 1] = float(np.mean(fr))
def d_mm(f):
    ds = sorted(ref); fs = [ref[d] for d in ds]
    if f >= fs[0]: return 2.0
    if f <= fs[-1]: return 4.0 + (fs[-1] - f) / max(fs[-2] - fs[-1], 1e-9)
    for a in range(len(ds) - 1):
        if fs[a] >= f >= fs[a + 1]:
            w = (fs[a] - f) / (fs[a] - fs[a + 1])
            return ds[a] + w * (ds[a + 1] - ds[a])
    return float("nan")

SEEDS = list(range(20260960, 20260965))
DELTAS = (128, 256, 512, 1024, 2048)
Z = {d: [] for d in DELTAS}
FR = {d: [] for d in DELTAS}
ref_ct = 0
for sd in SEEDS:
    chiV, r = web_chiv(sd)
    for D in DELTAS:
        start = (2048 - D) // 2
        win = np.arange(start, start + D)
        idx = win if D <= NW else np.sort(r.choice(win, NW, replace=False))
        rel = rel_of(idx, chiV, 3)
        H, W, s2 = mirsky(rel)
        Z[D].append(zdist(s2, H, W))
        FR[D].append(s2)
        if D == 512:
            ref_ct += not dim_le_2(rel)

print("      Delta sweep (seed-mean z to orthant locus | mean s2 | d_MM):")
for D in DELTAS:
    zs = [z for z in Z[D] if z is not None]
    zm = float(np.mean(zs)) if zs else float("nan")
    fm = float(np.mean(FR[D]))
    miss = 5 - len(zs)
    print(f"      Delta={D:5d}: z {zm:6.2f} ({len(zs)}/5 in-range"
          + (f", {miss} outside family s2" if miss else "")
          + f") | s2 {fm:.4f} | d_MM {d_mm(fm):.2f}")

z512 = Z[512]; z2048 = Z[2048]
gt1 = sum(1 for a, b in zip(z2048, z512)
          if a is not None and b is not None and a > b)
check("Gt1 (the cylinder signature): z(2048) > z(512) on >= 4/5 seeds",
      gt1 >= 4, f"{gt1}/5")
gt2 = sum(1 for z in z512 if z is not None and z <= 3)
check("Gt2 (the joining): z(Delta* = 512) <= 3 on >= 4/5 seeds",
      gt2 >= 4, f"{gt2}/5 (z values: "
      + ", ".join(f"{z:.2f}" if z is not None else "out" for z in z512) + ")")
dmm512 = d_mm(float(np.mean(FR[512])))
check("Gt3 (in-window dimension): windowed d_MM(512) >= 3.2 AND realizer "
      "refusals >= 4/5", dmm512 >= 3.2 and ref_ct >= 4,
      f"d_MM {dmm512:.2f}, refusals {ref_ct}/5")

# INFO: C = 2 spot at Delta*
fr2 = []
for sd in SEEDS[:3]:
    chiV, r = web_chiv(sd, C=2)
    start = (2048 - 512) // 2
    idx = np.sort(r.choice(np.arange(start, start + 512), NW, replace=False))
    rel = rel_of(idx, chiV, 2)
    n = rel.shape[0]
    fr2.append(rel.sum() / (n * (n - 1) / 2))
print(f"      INFO: C = 2 windowed (512) d_MM = {d_mm(float(np.mean(fr2))):.2f}")

if gt1 >= 4 and gt2 >= 4 and dmm512 >= 3.2 and ref_ct >= 4:
    verdict = "CYLINDER-CONFIRMED — Phase 3 reconstructs on Delta* = 512 windows"
elif gt1 >= 4:
    verdict = "BAND-SHIFTED (the phenomenon real; the scale argument off — see sweep)"
else:
    verdict = "CYLINDER-REFUTED (the anomaly is deeper than the measure's shape)"
print(f"      VERDICT: {verdict}")

print()
print(f"PRE-REGISTERED GATE LEDGER: "
      f"{'ALL HELD' if FAIL == 0 else 'REFUSALS PRESENT'} — Gt1 signature; "
      f"Gt2 joining; Gt3 dimension; verdict: {verdict}")
print()
total = PASS + FAIL
print(f"ALL CHECKS PASS ({PASS}/{total})" if FAIL == 0 else f"FAILURES: {FAIL}/{total}")
if FAIL: raise SystemExit(1)
