#!/usr/bin/env python3
"""
dimwall_phase0.py — v9 round 23: THE DIMENSION WALL, Phase 0
(note-3p1-dimension-ledger; pin committed at 062a56e strictly before this
receipt).  NO-REVIEW MODE (user 2026-07-06) — the wiring gate Gw is the
compensating discipline and is deliberately over-built.

The two-clock Lemma: (b, chi)-dominance orders have dim <= 2 by
definition (intersection of two linear orders); M^2 IS two-clock
causality; M^3's round cone is not.  This receipt certifies the
instruments Phase 1 will trust:
  dim<=2 tester  = Golumbic implication classes on the incomparability
                   graph (comparability iff no class holds an edge both
                   ways);
  independent brute = enumerate linear extensions L1; dim <= 2 iff some
                   conjugate P + reverse(L1 on incomparables) is an
                   acyclic tournament (out-degree test).

PINNED (note SS3):
  Gw   tester == brute on 300 random posets (n <= 7) AND canned cases
       (S3 refuses; chain/antichain/2D-dominance pass).  Any mismatch
       kills the receipt.
  Gd1  M3 diamond sprinklings (N = 128) REFUSE dim <= 2, 5/5 seeds.
  Gd2  M2 diamond sprinklings (N = 128) PASS, 5/5 seeds.
  Gd3  induced 128-subposets of grown corpus webs PASS, 5/5 seeds
       (consistency; the whole-web dim <= 2 is by the Lemma).
  Gd4  [printed] the MM estimator calibrated FORMULA-FREE from measured
       M^d reference sprinklings (d = 2, 3, 4; N = 512; 8 seeds);
       readings: M3 in the 3-band, the corpus web in the 2-band.
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

# ---------------- the tester: Golumbic implication classes ----------------
def dim_le_2(rel):
    """rel: NxN bool strict partial order (transitive).  True iff the
    incomparability graph is a comparability graph (dim(P) <= 2)."""
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
        sel = ~sub[iu, ju]              # heads/tails NON-adjacent => forced
        for b, c in zip(nbs[iu[sel]], nbs[ju[sel]]):
            union(a * n + b, a * n + c)     # same tail
            union(b * n + a, c * n + a)     # same head
    ii, jj = np.where(np.triu(inc, 1))
    for i, j in zip(ii, jj):
        if find(i * n + j) == find(j * n + i):
            return False
    return True

# ---------------- the independent brute (n <= 7) ----------------
def linear_extensions(rel):
    n = rel.shape[0]
    preds = [set(np.where(rel[:, j])[0]) for j in range(n)]
    out, cur, used = [], [], set()
    def rec():
        if len(cur) == n:
            out.append(list(cur)); return
        for v in range(n):
            if v not in used and preds[v] <= used:
                used.add(v); cur.append(v)
                rec()
                cur.pop(); used.remove(v)
    rec()
    return out

def dim_le_2_brute(rel):
    """dim <= 2 iff for some linear extension L1 the conjugate tournament
    (P as-is; incomparables reversed vs L1) is acyclic — tested by the
    out-degree criterion (acyclic tournament <=> out-degrees are a
    permutation of 0..n-1)."""
    n = rel.shape[0]
    inc = ~(rel | rel.T) & ~np.eye(n, dtype=bool)
    for L1 in linear_extensions(rel):
        pos = np.empty(n, dtype=int)
        pos[L1] = np.arange(n)
        before = pos[:, None] < pos[None, :]
        Q = rel | (inc & before.T)          # incomparables reversed
        degs = sorted(Q.sum(1))
        if degs == list(range(n)):
            return True
    return False

def tclose(rel):
    n = rel.shape[0]
    R = rel.copy()
    for _ in range(n):
        R2 = R | (R @ R)
        if (R2 == R).all():
            break
        R = R2
    np.fill_diagonal(R, False)
    return R

# ---------------- sprinklings ----------------
def sprinkle_mink(rng, N, dspace):
    """Uniform points in the causal diamond of M^(1+dspace); returns rel."""
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

# ---------------- the corpus web (wb-line builder, order only) ----------------
def web_rel(sd, N=2048, M=32, L=16):
    rng = np.random.default_rng(sd)
    chi_acc = np.zeros(M); chi = np.zeros(N)
    for t in range(N):
        c = int(rng.integers(M))
        chi_acc[c] += rng.exponential(0.109551)
        chi[t] = chi_acc[c]
        if rng.random() < 1.0 / L:
            v = int(rng.integers(M))
            chi_acc[v] = 0.0
    b = np.arange(N)
    rel = (b[:, None] < b[None, :]) & (chi[:, None] < chi[None, :])
    np.fill_diagonal(rel, False)
    return rel, rng

print("[dimwall Phase 0: the two-clock wall, measured]")

# ---- Gw: the wiring gate ----
rng = np.random.default_rng(20260740)
agree = True; ntest = 0
for _ in range(300):
    n = int(rng.integers(4, 8))
    p = rng.choice([0.15, 0.3, 0.5])
    base = np.triu(rng.random((n, n)) < p, 1)
    rel = tclose(base)
    if dim_le_2(rel) != dim_le_2_brute(rel):
        agree = False
        break
    ntest += 1
# canned: S3 (a_i < b_j iff i != j) — dim 3
s3 = np.zeros((6, 6), dtype=bool)
for i in range(3):
    for j in range(3):
        if i != j:
            s3[i, 3 + j] = True
canned_ok = (not dim_le_2(s3)) and (not dim_le_2_brute(s3))
chain = np.triu(np.ones((7, 7), dtype=bool), 1)
anti = np.zeros((6, 6), dtype=bool)
canned_ok &= dim_le_2(chain) and dim_le_2(anti)
for _ in range(20):
    x = rng.random(7); y = rng.random(7)
    dom = (x[:, None] < x[None, :]) & (y[:, None] < y[None, :])
    np.fill_diagonal(dom, False)
    canned_ok &= dim_le_2(dom)
check("Gw (wiring — load-bearing in no-review mode): tester == brute on "
      "300 random posets; S3 refuses both; chain/antichain/2D-dominance "
      "pass", agree and ntest == 300 and canned_ok,
      f"{ntest}/300 agreements; canned {'ok' if canned_ok else 'MISMATCH'}")
if not (agree and canned_ok):
    print("FAILURES: wiring dead — nothing downstream is read")
    raise SystemExit(1)

# ---- Gd1 / Gd2: M3 refuses, M2 passes ----
m3_refuse = 0; m2_pass = 0
for sd in range(20260741, 20260746):
    r = np.random.default_rng(sd)
    if not dim_le_2(sprinkle_mink(r, 128, 2)):
        m3_refuse += 1
    if dim_le_2(sprinkle_m2(np.random.default_rng(sd + 100), 128)):
        m2_pass += 1
check("Gd1 (the tester sees genuine 3D): M3 diamond sprinklings (N = 128) "
      "REFUSE dim <= 2 on 5/5 seeds", m3_refuse == 5, f"{m3_refuse}/5")
check("Gd2 (large-instance positive control): M2 sprinklings (N = 128) "
      "PASS on 5/5 seeds", m2_pass == 5, f"{m2_pass}/5")

# ---- Gd3: corpus webs (induced subposets) ----
web_ok = 0
web_fracs = []
for sd in range(20260746, 20260751):
    rel, r = web_rel(sd)
    web_fracs.append(rel.sum() / (2048 * 2047 / 2))
    idx = np.sort(r.choice(2048, 128, replace=False))
    sub = rel[np.ix_(idx, idx)]
    if dim_le_2(sub):
        web_ok += 1
check("Gd3 (instrument consistency): induced 128-subposets of grown "
      "corpus webs PASS on 5/5 (whole-web dim <= 2 is the Lemma's)",
      web_ok == 5, f"{web_ok}/5")

# ---- Gd4: the measured MM calibration (printed) ----
print("      [Gd4 — the formula-free MM calibration]")
ref = {}
for d, name in ((1, "M2"), (2, "M3"), (3, "M4")):
    fr = []
    for k in range(8):
        r = np.random.default_rng(20260760 + 10 * d + k)
        rel = (sprinkle_m2(r, 512) if d == 1
               else sprinkle_mink(r, 512, d))
        fr.append(rel.sum() / (512 * 511 / 2))
    ref[d + 1] = (float(np.mean(fr)), float(np.std(fr, ddof=1)))
    print(f"      reference M^{d+1}: ordering fraction "
          f"{ref[d+1][0]:.4f} +- {ref[d+1][1]:.4f}")
def d_mm(frac):
    ds = sorted(ref)                     # [2, 3, 4]
    fs = [ref[d][0] for d in ds]         # decreasing with d
    if frac >= fs[0]: return 2.0
    if frac <= fs[-1]: return 4.0 + (fs[-1] - frac) / max(fs[-2] - fs[-1], 1e-9)
    for a in range(len(ds) - 1):
        if fs[a] >= frac >= fs[a + 1]:
            w = (fs[a] - frac) / (fs[a] - fs[a + 1])
            return ds[a] + w * (ds[a + 1] - ds[a])
    return float("nan")
m3f = []
for sd in range(20260741, 20260746):
    r = np.random.default_rng(sd)
    rel = sprinkle_mink(r, 128, 2)
    m3f.append(rel.sum() / (128 * 127 / 2))
print(f"      M3 test sprinkles: fraction {np.mean(m3f):.4f} => "
      f"d_MM = {d_mm(float(np.mean(m3f))):.2f}   [3-band expected]")
wf = float(np.mean(web_fracs))
print(f"      corpus webs (N = 2048): fraction {wf:.4f} => "
      f"d_MM = {d_mm(wf):.2f}   [2-band expected]")

print()
print(f"PRE-REGISTERED GATE LEDGER: "
      f"{'ALL HELD' if FAIL == 0 else 'REFUSALS PRESENT'} — Gw wiring; "
      f"Gd1 M3 refuses; Gd2 M2 passes; Gd3 corpus consistent; Gd4 printed")
print()
total = PASS + FAIL
print(f"ALL CHECKS PASS ({PASS}/{total})" if FAIL == 0 else f"FAILURES: {FAIL}/{total}")
if FAIL: raise SystemExit(1)
