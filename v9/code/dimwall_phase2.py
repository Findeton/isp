#!/usr/bin/env python3
"""
dimwall_phase2.py — v9 round 26: PHASE 2, Lorentzization I — the
cone-shape discriminator (note-3p1-p2; pin committed at 55ab773 strictly
before this receipt.  NO-REVIEW MODE on record.)

Instrument: the chain-abundance triple s_k = (#k-chains)/C(N,k), k=2,3,4
(transitive orders: C3 = sum_y in*out; C4 = sum_{y<z} in(y)*out(z)).
Reference families MEASURED (no formulas): round M^{2,3,4} diamonds;
iid k-orthant dominance (k = 3,4,5).  Matched-s2 comparison: interpolate
each family's (s3, s4) at the web's s2 (log-space in the family
parameter); d_round / d_orthant = log-space distances.

PINNED (note SS4; webs = the Phase-1b class, C = 3, per-chan churn):
  Gc0  instrument separation (> 3x pooled seed-sd at matched s2 across
       the web range) else VOID-INSTRUMENT.
  Gc1  corner webs (one-hot a=0.75) nearer ORTHANT on >= 4/5 seeds.
  Gc2  [directional] K-direction webs (Dirichlet slot directions,
       vector deposits) reduce mean d_round vs the corner webs.
  Gc3  K-direction retention: realizer refusals >= 4/5, d_MM >= 3.0.
Verdicts: MIXING-ROUNDS / POLYHEDRAL-RIGID / MEASURE-DOMINATED.
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
    """mode 'corner' = Phase-1b one-hot affinity; 'kdir' = Dirichlet slot
    directions with vector deposits."""
    rng = np.random.default_rng(sd)
    acc = np.zeros((M, C))
    chiV = np.zeros((N, C))
    if mode == "kdir":
        W = rng.dirichlet(np.ones(C), size=M)
    pref = np.arange(M) % C
    for t in range(N):
        c = int(rng.integers(M))
        e = rng.exponential(0.109551)
        if mode == "kdir":
            acc[c] += e * W[c]
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

def triple(rel):
    n = rel.shape[0]
    R = rel.astype(np.float64)
    ind = R.sum(0); outd = R.sum(1)
    c2 = R.sum()
    c3 = float((ind * outd).sum())
    c4 = float((R * np.outer(ind, outd)).sum())
    from math import comb
    return (c2 / comb(n, 2), c3 / comb(n, 3), c4 / comb(n, 4))

print("[dimwall Phase 2: the cone-shape discriminator]")

# ---- the measured reference families ----
def family(build, params, seeds0, N=512, reps=8):
    out = {}
    for p in params:
        tr = []
        for k in range(reps):
            r = np.random.default_rng(seeds0 + 100 * p + k)
            tr.append(triple(build(r, N, p)))
        out[p] = (np.mean(tr, axis=0), np.std(tr, axis=0, ddof=1))
    return out

round_fam = family(lambda r, N, d: (sprinkle_m2(r, N) if d == 2
                                    else sprinkle_mink(r, N, d - 1)),
                   [2, 3, 4], 20260800)
orth_fam = family(lambda r, N, k: orthant_rel(r, N, k), [3, 4, 5], 20260830)
for name, fam in (("round M^d", round_fam), ("orthant k", orth_fam)):
    for p, (m, s) in sorted(fam.items()):
        print(f"      ref {name}={p}: s2 {m[0]:.4f}±{s[0]:.4f}  "
              f"s3 {m[1]:.5f}±{s[1]:.5f}  s4 {m[2]:.6f}±{s[2]:.6f}")

def matched(fam, s2):
    """Interpolate (s3, s4) and their sds at ordering fraction s2 (log
    space along the family parameter)."""
    ps = sorted(fam, key=lambda p: -fam[p][0][0])
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

def dists(tr):
    mr = matched(round_fam, tr[0])
    mo = matched(orth_fam, tr[0])
    if mr is None or mo is None:
        return None
    dr = np.hypot(np.log(tr[1]) - np.log(mr[0][1]), np.log(tr[2]) - np.log(mr[0][2]))
    do = np.hypot(np.log(tr[1]) - np.log(mo[0][1]), np.log(tr[2]) - np.log(mo[0][2]))
    return dr, do, mr, mo

# ---- Gc0: separation over the webs' s2 range ----
SEEDS = list(range(20260860, 20260865))
corner_tr = []
for sd in SEEDS:
    rel, _ = web_rel(sd, "corner")
    corner_tr.append(triple(rel))
kdir_tr = []
kdir_ok = 0
frs = []
for sd in SEEDS:
    rel, r = web_rel(sd, "kdir")
    kdir_tr.append(triple(rel))
    frs.append(triple(rel)[0])
    hit = False
    for _ in range(2):
        idx = np.sort(r.choice(2048, 144, replace=False))
        if not dim_le_2(rel[np.ix_(idx, idx)]):
            hit = True
            break
    kdir_ok += hit

sep_ok = True
for tr in corner_tr + kdir_tr:
    res = dists(tr)
    if res is None:
        sep_ok = False
        break
    _, _, mr, mo = res
    gap3 = abs(np.log(mr[0][1]) - np.log(mo[0][1]))
    gap4 = abs(np.log(mr[0][2]) - np.log(mo[0][2]))
    sd3 = (mr[1][1] / mr[0][1] + mo[1][1] / mo[0][1])
    sd4 = (mr[1][2] / mr[0][2] + mo[1][2] / mo[0][2])
    if not (gap3 > 3 * sd3 and gap4 > 3 * sd4):
        sep_ok = False
        break
check("Gc0 (instrument separation): round vs orthant matched loci differ "
      "by > 3x pooled seed-sd (log space) across the webs' s2 range",
      sep_ok)
if not sep_ok:
    print("VERDICT: VOID-INSTRUMENT")
    print(f"FAILURES: 1/1")
    raise SystemExit(1)

# ---- Gc1: the baseline signature ----
near_orth = 0
cd = []
for tr in corner_tr:
    dr, do, _, _ = dists(tr)
    cd.append((dr, do))
    near_orth += do < dr
print("      corner webs: " + "  ".join(
    f"(dR {a:.3f}, dO {b:.3f})" for a, b in cd))
check("Gc1 (baseline, registered): the corner webs sit nearer the "
      "ORTHANT locus on >= 4/5 seeds", near_orth >= 4, f"{near_orth}/5")

# ---- Gc2: the mixing probe ----
kd = []
for tr in kdir_tr:
    dr, do, _, _ = dists(tr)
    kd.append((dr, do))
print("      K-direction webs: " + "  ".join(
    f"(dR {a:.3f}, dO {b:.3f})" for a, b in kd))
mr_c = float(np.mean([a for a, _ in cd]))
mr_k = float(np.mean([a for a, _ in kd]))
check("Gc2 [directional]: the K-direction variant reduces mean d_round "
      "vs the corner webs", mr_k < mr_c,
      f"corner {mr_c:.3f} -> kdir {mr_k:.3f}")

# ---- Gc3: retention ----
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
dk = d_mm(float(np.mean(frs)))
check("Gc3 (retention): K-direction webs keep realizer refusals >= 4/5 "
      "and d_MM >= 3.0", kdir_ok >= 4 and dk >= 3.0,
      f"refusals {kdir_ok}/5, d_MM {dk:.2f}")

if near_orth >= 4 and mr_k < mr_c and kdir_ok >= 4 and dk >= 3.0:
    verdict = "MIXING-ROUNDS [MEASURED, directional] — Phase 2b tunes the mixing"
elif near_orth >= 4:
    verdict = ("POLYHEDRAL-RIGID — the framework predicts finite-C "
               "anisotropy (the falsifiable-signature branch)")
else:
    verdict = "MEASURE-DOMINATED — the webs sit off both ideals (the table is the finding)"
print(f"      VERDICT: {verdict}")
print(f"      INFO: corner d_MM = "
      f"{d_mm(float(np.mean([t[0] for t in corner_tr]))):.2f}; "
      f"kdir d_MM = {dk:.2f}; mean dR/dO: corner "
      f"{mr_c / np.mean([b for _, b in cd]):.2f}, kdir "
      f"{mr_k / np.mean([b for _, b in kd]):.2f}")

print()
print(f"PRE-REGISTERED GATE LEDGER: "
      f"{'ALL HELD' if FAIL == 0 else 'REFUSALS PRESENT'} — Gc0 sep; "
      f"Gc1 baseline; Gc2 mixing; Gc3 retention; verdict: {verdict}")
print()
total = PASS + FAIL
print(f"ALL CHECKS PASS ({PASS}/{total})" if FAIL == 0 else f"FAILURES: {FAIL}/{total}")
if FAIL: raise SystemExit(1)
