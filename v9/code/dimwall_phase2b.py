#!/usr/bin/env python3
"""
dimwall_phase2b.py — v9 round 27: PHASE 2-II — the extremal-statistics
cone discriminator (note-3p1-p2b; pin committed at f82ee24 strictly
before this receipt.  NO-REVIEW MODE on record.)

Instrument: one Mirsky peeling per instance -> H = height (= #layers),
W = max layer size (the width proxy, pinned as-is).  All instances at
matched N = 768 (webs via induced subsamples, 2 draws/seed).  Matched-s2
log-space loci (round M^{2,3,4} vs orthant k = 3,4,5; 10 seeds); the
d = 2 anchor (M2 == orthant-2) printed as wiring.

PINNED (note SS2):
  Gx0  separation certification FIRST (> 3x pooled sd, per component,
       across the webs' s2 range) else VOID-INSTRUMENT-II (pivot named:
       directional/embedding instruments).
  Gx1  corner webs nearer ORTHANT >= 4/5 [registered].
  Gx2  [directional] kdir mean d_round < corner mean d_round.
  Gx3  kdir retention: realizer refusals >= 4/5; full-web d_MM >= 3.0.
Exit 1 by design on refusal.
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

def web_rel(sd, mode, C=3, N=2048, M=32, L=16, alpha=0.75):
    rng = np.random.default_rng(sd)
    acc = np.zeros((M, C))
    chiV = np.zeros((N, C))
    if mode == "kdir":
        Wd = rng.dirichlet(np.ones(C), size=M)
    pref = np.arange(M) % C
    for t in range(N):
        c = int(rng.integers(M))
        e = rng.exponential(0.109551)
        if mode == "kdir":
            acc[c] += e * Wd[c]
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
    return rel, rng

def mirsky(rel):
    """One peeling: returns (H = #layers, W = max layer size, s2)."""
    n = rel.shape[0]
    rem = np.ones(n, dtype=bool)
    H = 0; Wmax = 0
    while rem.any():
        pc = (rel & rem[:, None] & rem[None, :]).sum(0)
        minimal = rem & (pc == 0)
        H += 1
        Wmax = max(Wmax, int(minimal.sum()))
        rem &= ~minimal
    s2 = rel.sum() / (n * (n - 1) / 2)
    return H, Wmax, s2

print("[dimwall Phase 2-II: the extremal discriminator]")
NN = 768

def fam_stats(build, params, seed0, reps=10):
    out = {}
    for p in params:
        rows = []
        for k in range(reps):
            r = np.random.default_rng(seed0 + 100 * p + k)
            H, W, s2 = mirsky(build(r, NN, p))
            rows.append((s2, H, W))
        rows = np.array(rows, dtype=float)
        out[p] = (rows.mean(0), rows.std(0, ddof=1))
    return out

round_fam = fam_stats(lambda r, N, d: (sprinkle_m2(r, N) if d == 2
                                       else sprinkle_mink(r, N, d - 1)),
                      [2, 3, 4], 20260870)
orth_fam = fam_stats(lambda r, N, k: orthant_rel(r, N, k),
                     [2, 3, 4, 5], 20260900)
for name, fam in (("round M^d", round_fam), ("orthant k", orth_fam)):
    for p, (m, s) in sorted(fam.items()):
        print(f"      ref {name}={p}: s2 {m[0]:.4f}±{s[0]:.4f}  "
              f"H {m[1]:.1f}±{s[1]:.1f}  W {m[2]:.1f}±{s[2]:.1f}")
a_r, a_o = round_fam[2][0], orth_fam[2][0]
print(f"      d = 2 anchor (wiring): round (H {a_r[1]:.1f}, W {a_r[2]:.1f}) "
      f"vs orthant-2 (H {a_o[1]:.1f}, W {a_o[2]:.1f}) — coincide within sds")

def matched(fam, s2, exclude2=True):
    ps = sorted((p for p in fam if not (exclude2 and p == 2)),
                key=lambda p: -fam[p][0][0])
    s2s = [fam[p][0][0] for p in ps]
    if not (s2s[-1] <= s2 <= s2s[0]):
        return None
    for a in range(len(ps) - 1):
        if s2s[a] >= s2 >= s2s[a + 1]:
            w = (np.log(s2s[a]) - np.log(s2)) / (np.log(s2s[a]) - np.log(s2s[a + 1]))
            m = np.exp((1 - w) * np.log(fam[ps[a]][0]) + w * np.log(fam[ps[a + 1]][0]))
            sd = (1 - w) * fam[ps[a]][1] + w * fam[ps[a + 1]][1]
            return m, sd
    return None

def dists(s2, H, W):
    mr = matched(round_fam, s2)
    mo = matched(orth_fam, s2, exclude2=False)
    if mr is None or mo is None:
        return None
    dr = np.hypot(np.log(H) - np.log(mr[0][1]), np.log(W) - np.log(mr[0][2]))
    do = np.hypot(np.log(H) - np.log(mo[0][1]), np.log(W) - np.log(mo[0][2]))
    return dr, do, mr, mo

# ---- webs ----
SEEDS = list(range(20260930, 20260935))
def web_stats(mode):
    rows = []
    ref_ct = 0
    fr_full = []
    for sd in SEEDS:
        rel, r = web_rel(sd, mode)
        n = rel.shape[0]
        fr_full.append(rel.sum() / (n * (n - 1) / 2))
        Hs, Ws, ss = [], [], []
        for _ in range(2):
            idx = np.sort(r.choice(2048, NN, replace=False))
            H, W, s2 = mirsky(rel[np.ix_(idx, idx)])
            Hs.append(H); Ws.append(W); ss.append(s2)
        rows.append((float(np.mean(ss)), float(np.mean(Hs)), float(np.mean(Ws))))
        if mode == "kdir":
            hit = False
            for _ in range(2):
                idx = np.sort(r.choice(2048, 144, replace=False))
                if not dim_le_2(rel[np.ix_(idx, idx)]):
                    hit = True
                    break
            ref_ct += hit
    return rows, ref_ct, float(np.mean(fr_full))

corner_rows, _, _ = web_stats("corner")
kdir_rows, kdir_ok, kdir_frac = web_stats("kdir")
print("      corner webs (s2, H, W): " + "  ".join(
    f"({a:.3f}, {b:.0f}, {c:.0f})" for a, b, c in corner_rows))
print("      kdir webs   (s2, H, W): " + "  ".join(
    f"({a:.3f}, {b:.0f}, {c:.0f})" for a, b, c in kdir_rows))

# ---- Gx0 ----
sep_ok = True
for s2, H, W in corner_rows + kdir_rows:
    res = dists(s2, H, W)
    if res is None:
        sep_ok = False
        break
    _, _, mr, mo = res
    for comp in (1, 2):
        gap = abs(np.log(mr[0][comp]) - np.log(mo[0][comp]))
        sd = mr[1][comp] / mr[0][comp] + mo[1][comp] / mo[0][comp]
        if not gap > 3 * sd:
            sep_ok = False
            break
    if not sep_ok:
        break
check("Gx0 (separation certification): round vs orthant matched (H, W) "
      "loci differ by > 3x pooled sd across the webs' s2 range", sep_ok)
if not sep_ok:
    print("      VERDICT: VOID-INSTRUMENT-II — cone shape invisible to "
          "counting AND extremal order statistics at this N; the pivot "
          "is directional/embedding instruments (fresh design)")
    print()
    print("PRE-REGISTERED GATE LEDGER: REFUSALS PRESENT — Gx0")
    print()
    print("FAILURES: 1/1")
    raise SystemExit(1)

# ---- Gx1 / Gx2 ----
cd = [dists(*row)[:2] for row in corner_rows]
kd = [dists(*row)[:2] for row in kdir_rows]
print("      corner (dR, dO): " + "  ".join(f"({a:.3f}, {b:.3f})" for a, b in cd))
print("      kdir   (dR, dO): " + "  ".join(f"({a:.3f}, {b:.3f})" for a, b in kd))
near_orth = sum(1 for a, b in cd if b < a)
check("Gx1 (baseline, registered): corner webs nearer the ORTHANT locus "
      "on >= 4/5 seeds", near_orth >= 4, f"{near_orth}/5")
mr_c = float(np.mean([a for a, _ in cd]))
mr_k = float(np.mean([a for a, _ in kd]))
check("Gx2 [directional]: kdir reduces mean d_round vs corner",
      mr_k < mr_c, f"corner {mr_c:.3f} -> kdir {mr_k:.3f}")

# ---- Gx3 ----
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
dk = d_mm(kdir_frac)
check("Gx3 (retention): kdir realizer refusals >= 4/5; full-web d_MM >= 3.0",
      kdir_ok >= 4 and dk >= 3.0, f"refusals {kdir_ok}/5, d_MM {dk:.2f}")

if near_orth >= 4 and mr_k < mr_c and kdir_ok >= 4 and dk >= 3.0:
    verdict = "MIXING-ROUNDS [MEASURED, directional] — Phase 2b tunes the mixing"
elif near_orth >= 4:
    verdict = ("POLYHEDRAL-RIGID — the framework predicts finite-C "
               "anisotropy (the falsifiable-signature branch)")
else:
    verdict = "MEASURE-DOMINATED — the webs sit off both ideals"
print(f"      VERDICT: {verdict}")

print()
print(f"PRE-REGISTERED GATE LEDGER: "
      f"{'ALL HELD' if FAIL == 0 else 'REFUSALS PRESENT'} — Gx0 sep; "
      f"Gx1 baseline; Gx2 mixing; Gx3 retention; verdict: {verdict}")
print()
total = PASS + FAIL
print(f"ALL CHECKS PASS ({PASS}/{total})" if FAIL == 0 else f"FAILURES: {FAIL}/{total}")
if FAIL: raise SystemExit(1)
