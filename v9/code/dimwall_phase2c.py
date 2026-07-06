#!/usr/bin/env python3
"""
dimwall_phase2c.py — v9 round 28: DE-FLEETED STATISTICS (note-3p1-p2c;
pin committed at 2883fb2 strictly before this receipt.  NO-REVIEW MODE.)

Decimation: ONE random commit per slot-LIFE (life ends at any channel
reset of the slot); kept sets subsampled to N_dec = 320.  Gates: Gf1
decimated d_MM(C=3) >= 3.75 (>= 3.8 flags PENDING-USER-REVIEW-DECISION);
Gf2 decimated (H, W) within 3x pooled sd of the orthant matched locus
on >= 4/5 seeds; Gf3 realizer refusals >= 4/5 on 144-subposets.
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

def web_decimated(sd, C=3, N=2048, M=32, L=16, alpha=0.75):
    """The pinned-class web with life tracking; returns the kept-set
    (b, chiV) decimated to one commit per (slot, life)."""
    rng = np.random.default_rng(sd)
    acc = np.zeros((M, C))
    life = np.zeros(M, dtype=int)
    pref = np.arange(M) % C
    slot_of = np.zeros(N, dtype=int); life_of = np.zeros(N, dtype=int)
    chiV = np.zeros((N, C))
    for t in range(N):
        c = int(rng.integers(M))
        if rng.random() < alpha:
            k = int(pref[c])
        else:
            k = int(rng.integers(C))
        acc[c, k] += rng.exponential(0.109551)
        chiV[t] = acc[c]
        slot_of[t] = c; life_of[t] = life[c]
        for kk in range(C):
            if rng.random() < 1.0 / L:
                v = int(rng.integers(M))
                acc[v, kk] = 0.0
                life[v] += 1
    keep = {}
    for t in range(N):
        key = (slot_of[t], life_of[t])
        if key not in keep:
            keep[key] = [t]
        else:
            keep[key].append(t)
    kept = np.array(sorted(int(rng.choice(v)) if len(v) > 1 else v[0]
                           for v in keep.values()), dtype=int)
    return kept, chiV, rng

def rel_of(kept, chiV, C=3):
    b = kept
    rel = b[:, None] < b[None, :]
    for k in range(C):
        rel &= chiV[kept][:, None, k] <= chiV[kept][None, :, k]
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

print("[dimwall Phase 2c: de-fleeted statistics — one record per thread-life]")
ND = 320

# d_MM curve (N-independent fractions; Phase-0 recipe)
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

# extremal orthant references at N = 320
orth = {}
for k in (3, 4, 5):
    rows = []
    for j in range(8):
        r = np.random.default_rng(20260950 + 100 * k + j)
        rows.append(mirsky(orthant_rel(r, ND, k)))
    rows = np.array([(s, h, w) for h, w, s in rows], dtype=float)
    orth[k] = (rows.mean(0), rows.std(0, ddof=1))
    m, s = orth[k]
    print(f"      orthant k={k} @N={ND}: s2 {m[0]:.4f}±{s[0]:.4f}  "
          f"H {m[1]:.1f}±{s[1]:.1f}  W {m[2]:.1f}±{s[2]:.1f}")

def matched_orth(s2):
    ps = sorted(orth, key=lambda p: -orth[p][0][0])
    s2s = [orth[p][0][0] for p in ps]
    if not (s2s[-1] <= s2 <= s2s[0]):
        return None
    for a in range(len(ps) - 1):
        if s2s[a] >= s2 >= s2s[a + 1]:
            w = (np.log(s2s[a]) - np.log(s2)) / (np.log(s2s[a]) - np.log(s2s[a + 1]))
            m = np.exp((1 - w) * np.log(orth[ps[a]][0]) + w * np.log(orth[ps[a + 1]][0]))
            sd = (1 - w) * orth[ps[a]][1] + w * orth[ps[a + 1]][1]
            return m, sd
    return None

SEEDS = list(range(20260940, 20260945))
fr3, hw_ok, ref_ct, sizes = [], 0, 0, []
for sd in SEEDS:
    kept, chiV, r = web_decimated(sd, C=3)
    sizes.append(len(kept))
    sub = kept if len(kept) <= ND else np.sort(r.choice(kept, ND, replace=False))
    rel = rel_of(sub, chiV)
    H, W, s2 = mirsky(rel)
    fr3.append(s2)
    mo = matched_orth(s2)
    ok = False
    if mo is not None:
        ok = all(abs(np.log([H, W][i - 1]) - np.log(mo[0][i]))
                 <= 3 * (mo[1][i] / mo[0][i]) for i in (1, 2))
    hw_ok += ok
    idx = (np.arange(len(sub)) if len(sub) <= 144
           else np.sort(r.choice(len(sub), 144, replace=False)))
    ref_ct += not dim_le_2(rel[np.ix_(idx, idx)])
    print(f"      seed {sd}: kept {len(kept)}, s2 {s2:.4f}, H {H}, W {W}, "
          f"orthant-locus {'OK' if ok else 'OFF'}"
          + (f" (matched H {mo[0][1]:.1f}±{mo[1][1]:.1f}, W {mo[0][2]:.1f}"
             f"±{mo[1][2]:.1f})" if mo else " (s2 out of family range)"))

d3 = d_mm(float(np.mean(fr3)))
trigger = d3 >= 3.8
check("Gf1 (the dimension question): decimated d_MM(C = 3) >= 3.75",
      d3 >= 3.75, f"d_MM = {d3:.2f}"
      + ("; >= 3.8 => PENDING-USER-REVIEW-DECISION" if trigger else ""))
check("Gf2 (the anomaly resolves): decimated (H, W) within 3x sd of the "
      "orthant matched locus on >= 4/5 seeds", hw_ok >= 4, f"{hw_ok}/5")
check("Gf3 (retention): realizer refusals >= 4/5", ref_ct >= 4,
      f"{ref_ct}/5")

# INFO: C = 2 decimated
fr2 = []
for sd in SEEDS[:3]:
    kept, chiV, r = web_decimated(sd, C=2)
    sub = kept if len(kept) <= ND else np.sort(r.choice(kept, ND, replace=False))
    rel = rel_of(sub, chiV, C=2)
    n = rel.shape[0]
    fr2.append(rel.sum() / (n * (n - 1) / 2))
print(f"      INFO: decimated C = 2 d_MM = {d_mm(float(np.mean(fr2))):.2f}; "
      f"kept sizes {sizes}")

if d3 >= 3.75 and hw_ok >= 4 and ref_ct >= 4:
    verdict = ("DE-FLEETED-CLEAN — the fleet structure was the residual "
               "anomaly; Phase 3 runs on DECIMATED webs"
               + ("; PENDING-USER-REVIEW-DECISION" if trigger else ""))
elif d3 >= 3.75:
    verdict = "DIMENSION-CLOSES-ANOMALY-REMAINS"
elif hw_ok >= 4:
    verdict = "ANOMALY-WAS-CHAINS-DIMENSION-DIDN'T-FOLLOW"
else:
    verdict = "THE-FLEET-WAS-NOT-THE-CAUSE (diagnosis reopens)"
print(f"      VERDICT: {verdict}")

print()
print(f"PRE-REGISTERED GATE LEDGER: "
      f"{'ALL HELD' if FAIL == 0 else 'REFUSALS PRESENT'} — Gf1 dial; "
      f"Gf2 locus; Gf3 retention; verdict: {verdict}")
print()
total = PASS + FAIL
print(f"ALL CHECKS PASS ({PASS}/{total})" if FAIL == 0 else f"FAILURES: {FAIL}/{total}")
if FAIL: raise SystemExit(1)
