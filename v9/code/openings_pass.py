#!/usr/bin/env python3
"""
openings_pass.py — v9 round 35: THE OPENINGS PASS (note-3p1-openings;
pin committed at a1fa12c strictly before this receipt).
A: the MM association-dependence row (MAJOR-2 formalized).
B: S4 witness-density lower bound (searcher validated in-receipt).
C: the frozen MM reference table -> v9/data/mm_reference.json.
O1: the capacity ceiling's scale law [directional: C*(n) grows ~ log n].
O2: comparability percolation vs C and web size [directional: log N].
Measured/mapping receipt; exit 1 only on instrument failure (searcher
validation or reference generation).
"""
import json, os
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

def orthant_rel(rng, N, k):
    Z = rng.random((N, k))
    rel = np.ones((N, N), dtype=bool)
    for j in range(k):
        rel &= Z[:, None, j] < Z[None, :, j]
    np.fill_diagonal(rel, False)
    return rel

def frac(rel):
    n = rel.shape[0]
    return rel.sum() / (n * (n - 1) / 2)

def web_chiv(sd, C, N=2048, M=32, L=16, alpha=0.75):
    rng = np.random.default_rng(sd)
    acc = np.zeros((M, C))
    pref = np.arange(M) % C
    chiV = np.zeros((N, C))
    for t in range(N):
        c = int(rng.integers(M))
        if C > 1 and rng.random() < alpha:
            k = int(pref[c])
        else:
            k = int(rng.integers(C))
        acc[c, k] += rng.exponential(0.109551)
        chiV[t] = acc[c]
        for kk in range(C):
            if rng.random() < 1.0 / L:
                acc[int(rng.integers(M)), kk] = 0.0
    return chiV, rng

def rel_win(idx, chiV, C):
    b = idx
    rel = b[:, None] < b[None, :]
    for k in range(C):
        rel &= chiV[idx][:, None, k] <= chiV[idx][None, :, k]
    np.fill_diagonal(rel, False)
    return rel

def find_s4(rel, rng, tries=200):
    n = rel.shape[0]
    comp = rel | rel.T
    for _ in range(tries):
        perm = rng.permutation(n)
        A = []
        for v in perm:
            if all(not comp[v, a] for a in A):
                A.append(int(v))
                if len(A) == 4:
                    break
        if len(A) < 4:
            continue
        buckets = [[] for _ in range(4)]
        for b in range(n):
            if b in A:
                continue
            above = [bool(rel[a, b]) for a in A]
            if sum(above) == 3:
                i = above.index(False)
                if not comp[A[i], b]:
                    buckets[i].append(b)
        if any(not bk for bk in buckets):
            continue
        for _ in range(60):
            B = [bk[int(rng.integers(len(bk)))] for bk in buckets]
            if len(set(B)) == 4 and all(
                    not comp[B[i], B[j]]
                    for i in range(4) for j in range(i + 1, 4)):
                return A, B
    return None

print("[openings pass]")

# ---- C: the frozen MM reference ----
ref = {}
for d in (1, 2, 3, 4):
    fr = []
    for k in range(8):
        r = np.random.default_rng(20260760 + 10 * d + k)
        rel = (sprinkle_m2(r, 512) if d == 1 else sprinkle_mink(r, 512, d))
        fr.append(frac(rel))
    ref[d + 1] = float(np.mean(fr))
os.makedirs("v9/data", exist_ok=True)
json.dump({"M%d" % d: ref[d] for d in ref},
          open("v9/data/mm_reference.json", "w"), indent=1)
check("C (frozen reference): v9/data/mm_reference.json written",
      os.path.exists("v9/data/mm_reference.json"),
      " ".join(f"M{d}={ref[d]:.4f}" for d in sorted(ref)))
def d_mm(f):
    ds = sorted(ref); fs = [ref[d] for d in ds]
    if f >= fs[0]: return 2.0
    if f <= fs[-1]: return float(ds[-1])
    for a in range(len(ds) - 1):
        if fs[a] >= f >= fs[a + 1]:
            w = (fs[a] - f) / (fs[a] - fs[a + 1])
            return ds[a] + w * (ds[a + 1] - ds[a])
    return float("nan")

# ---- A: the association row ----
dm_web, dm_shuf = [], []
for sd in (20261400, 20261401, 20261402):
    chiV, r = web_chiv(sd, 3)
    start = (2048 - 512) // 2
    idx = np.sort(r.choice(np.arange(start, start + 512), 128, replace=False))
    dm_web.append(d_mm(frac(rel_win(idx, chiV, 3))))
    chiP = chiV.copy()
    for k in range(3):
        chiP[idx, k] = r.permutation(chiP[idx, k])
    dm_shuf.append(d_mm(frac(rel_win(idx, chiP, 3))))
print(f"      A (association row): web d_MM {np.mean(dm_web):.2f} vs "
      f"channel-shuffled {np.mean(dm_shuf):.2f} — the gap "
      f"{np.mean(dm_web)-np.mean(dm_shuf):+.2f} is the dynamics' "
      f"cross-channel association (MAJOR-2, receipt-carried)")

# ---- B: witness density (searcher validated first) ----
r = np.random.default_rng(20261410)
val_pos = sum(1 for j in range(5)
              if find_s4(orthant_rel(np.random.default_rng(700 + j), 128, 4),
                         r) is not None)
val_neg3 = sum(1 for j in range(5)
               if find_s4(orthant_rel(np.random.default_rng(800 + j), 128, 3),
                          r) is not None)
c2neg = 0
for j in range(5):
    chiV, r2 = web_chiv(20261420 + j, 2)
    idx = np.sort(r2.choice(np.arange(768, 1280), 128, replace=False))
    if find_s4(rel_win(idx, chiV, 2), r) is not None:
        c2neg += 1
check("B (searcher validation): finds S4 in iid 4-orthant 5/5; zero "
      "false positives on 3-orthant and C = 2 windows",
      val_pos == 5 and val_neg3 == 0 and c2neg == 0,
      f"pos {val_pos}/5, neg3 {val_neg3}/5, C2 {c2neg}/5")
hits = 0; total = 0
for sd in range(20261430, 20261435):
    chiV, r2 = web_chiv(sd, 3)
    for _ in range(10):
        idx = np.sort(r2.choice(np.arange(768, 1280), 128, replace=False))
        total += 1
        if find_s4(rel_win(idx, chiV, 3), r) is not None:
            hits += 1
print(f"      B (witness density, LOWER bound): S4 hit-rate "
      f"{hits}/{total} window draws (C = 3, 5 seeds x 10 draws)")

# ---- O1: the capacity ceiling's scale law ----
print("      O1 (the ceiling's scale law) — viability at alpha = 0.75:")
ANCH = {}
for n in (96, 144, 216):
    for k in range(5, 10):
        fr = []
        for j in range(5):
            rr = np.random.default_rng(20261500 + 1000 * n + 10 * k + j)
            fr.append(frac(orthant_rel(rr, n, k)))
        ANCH[(n, k)] = float(np.mean(fr))
ceil = {}
for n in (96, 144, 216):
    row = []
    for C in (4, 5, 6, 7, 8):
        ok = 0
        for sd in (20261600 + C, 20261610 + C):
            chiV, r2 = web_chiv(sd, C)
            cc = np.corrcoef(chiV[512:1536].T)
            corr = float(np.mean(cc[np.triu_indices(C, 1)]))
            idx = np.sort(r2.choice(np.arange(768, 1280), n, replace=False))
            rel = rel_win(idx, chiV, C)
            f = frac(rel)
            anch = ANCH[(n, C + 1)]
            vol = f > 0 and anch > 0 and abs(np.log2(f / anch)) <= 1
            if corr < 0.25 and vol and not dim_le_2(rel):
                ok += 1
        row.append("V" if ok == 2 else ".")
    viable = [C for C, s in zip((4, 5, 6, 7, 8), row) if s == "V"]
    ceil[n] = max(viable) if viable else 0
    print(f"      n={n:3d}: C=4..8 [{' '.join(row)}]  ceiling C* = {ceil[n]}")
trend = ceil[96] <= ceil[144] <= ceil[216] and ceil[216] > ceil[96]
print(f"      O1 REGISTERED [directional] ceiling grows with n: "
      f"{'CONFIRMED' if trend else 'NOT CONFIRMED'} "
      f"({ceil[96]}/{ceil[144]}/{ceil[216]})")

# ---- O2: comparability percolation ----
print("      O2 (percolation) — largest-component fraction of the "
      "comparability graph:")
perc = {}
for N in (1024, 2048, 4096):
    row = []
    for C in (2, 3, 4, 5, 6, 7, 8, 9):
        lccs = []
        for sd in (20261700 + C, 20261710 + C):
            chiV, r2 = web_chiv(sd, C, N=N)
            b = np.arange(N)
            rel = b[:, None] < b[None, :]
            for k in range(C):
                rel &= chiV[:, None, k] <= chiV[None, :, k]
            np.fill_diagonal(rel, False)
            adj = rel | rel.T
            seen = np.zeros(N, dtype=bool)
            best = 0
            for s0 in range(N):
                if seen[s0]:
                    continue
                front = np.zeros(N, dtype=bool); front[s0] = True
                compo = front.copy()
                while front.any():
                    front = (adj[front].any(0)) & ~compo
                    compo |= front
                seen |= compo
                best = max(best, int(compo.sum()))
                if best > N // 2:
                    break
            lccs.append(best / N)
        row.append(float(np.mean(lccs)))
    thr = next((C for C, v in zip((2, 3, 4, 5, 6, 7, 8, 9), row) if v < 0.9),
               ">9")
    perc[N] = thr
    print(f"      N={N:4d}: LCC " + " ".join(f"{v:.2f}" for v in row)
          + f"  (first < 0.9 at C = {thr})")
print(f"      O2 REGISTERED [directional] threshold grows with N: "
      f"thresholds {perc}")

print()
print(f"PRE-REGISTERED GATE LEDGER: "
      f"{'ALL HELD' if FAIL == 0 else 'REFUSALS PRESENT'} — C frozen; "
      f"B searcher; A/O1/O2 measured")
print()
total_c = PASS + FAIL
print(f"ALL CHECKS PASS ({PASS}/{total_c})" if FAIL == 0
      else f"FAILURES: {FAIL}/{total_c}")
if FAIL: raise SystemExit(1)
