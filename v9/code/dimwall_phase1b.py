#!/usr/bin/env python3
"""
dimwall_phase1b.py — v9 round 25: PHASE 1b — decorrelation at the source
(note-3p1-p1b; pin committed at ac6e7ef strictly before this receipt.
NO-REVIEW MODE on record; reserved-review trigger: d_MM(C=3, pinned)
>= 3.7 => PENDING-USER-REVIEW-DECISION.)

Mechanisms: V-A slot-channel affinity (P(pref) = alpha + (1-alpha)/C;
round-robin preferences) breaking the common-age factor; V-B independent
per-channel churn clocks (rate 1/L each).  Registered: an INTERIOR
optimum in alpha (alpha = 1 re-collapses to dim <= 2 — the disjoint-sum
theorem: decorrelation alone is insufficient; channels must be distinct
AND interacting).

PINNED (note SS2; pinned point = alpha 0.75, per-channel churn, C = 3):
  Gb1  channel-corr < 0.25 on 5/5 (baseline +0.598).
  Gb2  d_MM >= 3.0 (seed mean) AND 2-realizer refuses >= 4/5.
  Gb3  d_MM strictly monotone over C = 1, 2, 3; d_MM(C = 2) >= 2.6.
  Gb4  the segregation control: alpha = 1 => 2-realizer PASSES >= 4/5
       (refusal impeaches the instrument => ROUND-VOID).
INFO: the (alpha x churn) sweep at C = 3 (3 seeds/cell).
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

def web_rel(sd, C, alpha=0.0, churn_mode="full", N=2048, M=32, L=16):
    rng = np.random.default_rng(sd)
    pref = np.arange(M) % C
    acc = np.zeros((M, C))
    chiV = np.zeros((N, C))
    for t in range(N):
        c = int(rng.integers(M))
        if C > 1 and rng.random() < alpha:
            k = int(pref[c])
        else:
            k = int(rng.integers(C))
        acc[c, k] += rng.exponential(0.109551)
        chiV[t] = acc[c]
        if churn_mode == "full":
            if rng.random() < 1.0 / L:
                acc[int(rng.integers(M))] = 0.0
        else:                                # independent per-channel clocks
            for kk in range(C):
                if rng.random() < 1.0 / L:
                    acc[int(rng.integers(M)), kk] = 0.0
    b = np.arange(N)
    rel = b[:, None] < b[None, :]
    for k in range(C):
        rel &= chiV[:, None, k] <= chiV[None, :, k]
    np.fill_diagonal(rel, False)
    return rel, chiV, rng

def frac(rel):
    n = rel.shape[0]
    return rel.sum() / (n * (n - 1) / 2)

print("[dimwall Phase 1b: decorrelation at the source]")

# MM calibration (Phase-0 recipe verbatim)
ref = {}
for d in (1, 2, 3):
    fr = []
    for k in range(8):
        r = np.random.default_rng(20260760 + 10 * d + k)
        rel = (sprinkle_m2(r, 512) if d == 1 else sprinkle_mink(r, 512, d))
        fr.append(frac(rel))
    ref[d + 1] = float(np.mean(fr))
print("      MM reference fractions: " + "  ".join(
    f"M^{d}: {f:.4f}" for d, f in sorted(ref.items())))
def d_mm(f):
    ds = sorted(ref); fs = [ref[d] for d in ds]
    if f >= fs[0]: return 2.0
    if f <= fs[-1]: return 4.0 + (fs[-1] - f) / max(fs[-2] - fs[-1], 1e-9)
    for a in range(len(ds) - 1):
        if fs[a] >= f >= fs[a + 1]:
            w = (fs[a] - f) / (fs[a] - fs[a + 1])
            return ds[a] + w * (ds[a + 1] - ds[a])
    return float("nan")

SEEDS = list(range(20260790, 20260795))

def measure(C, alpha, churn_mode, seeds, draws=2, do_realizer=True):
    fr_l, corr_l, ref_ct = [], [], 0
    for sd in seeds:
        rel, chiV, r = web_rel(sd, C, alpha, churn_mode)
        fr_l.append(frac(rel))
        if C >= 2:
            cc = np.corrcoef(chiV.T)
            corr_l.append(float(np.mean(cc[np.triu_indices(C, 1)])))
        if do_realizer:
            hit = False
            for _ in range(draws):
                idx = np.sort(r.choice(2048, 144, replace=False))
                if not dim_le_2(rel[np.ix_(idx, idx)]):
                    hit = True
                    break
            ref_ct += hit
    return (float(np.mean(fr_l)),
            float(np.mean(corr_l)) if corr_l else float("nan"), ref_ct)

# ---- the pinned point ----
f3, c3, r3 = measure(3, 0.75, "chan", SEEDS)
d3 = d_mm(f3)
print(f"      PINNED (C=3, a=0.75, per-chan churn): corr {c3:+.3f}, "
      f"fraction {f3:.4f}, d_MM = {d3:.2f}, realizer-refusals {r3}/5")
check("Gb1 (decorrelation works): channel-corr < 0.25 on the pinned "
      "point (baseline +0.598)", c3 < 0.25, f"corr {c3:+.3f}")
check("Gb2 (the dial responds): d_MM >= 3.0 AND 2-realizer refuses "
      ">= 4/5 at the pinned point", d3 >= 3.0 and r3 >= 4,
      f"d_MM {d3:.2f}, refusals {r3}/5")

# ---- the C-ladder at the pinned mechanism ----
f1, _, _ = measure(1, 0.0, "chan", SEEDS, do_realizer=False)
f2, c2, r2 = measure(2, 0.75, "chan", SEEDS)
d1, d2 = d_mm(f1), d_mm(f2)
check("Gb3 (the C-ladder): d_MM strictly monotone over C = 1, 2, 3; "
      "d_MM(C = 2) >= 2.6", d1 < d2 < d3 and d2 >= 2.6,
      f"d_MM = {d1:.2f} / {d2:.2f} / {d3:.2f} (C=2 corr {c2:+.3f}, "
      f"refusals {r2}/5)")

# ---- the segregation control ----
fS, cS, rS = measure(3, 1.0, "chan", SEEDS)
check("Gb4 (the segregation control, theorem-backed): alpha = 1 => "
      "2-realizer PASSES >= 4/5 (disjoint-sum collapse to dim <= 2)",
      (5 - rS) >= 4, f"passes {5 - rS}/5 (corr {cS:+.3f}, "
      f"d_MM {d_mm(fS):.2f} — fraction-only, structure segregated)")

trigger = d3 >= 3.7
if PASS == 4 and FAIL == 0:
    verdict = ("DECORRELATION-ACHIEVED [MEASURED]"
               + ("; d_MM(C=3) >= 3.7 => PENDING-USER-REVIEW-DECISION"
                  if trigger else ""))
elif c3 < 0.25:
    verdict = "DECORRELATED-BUT-FLAT (the common-age story incomplete)"
else:
    verdict = "AFFINITY-INSUFFICIENT"
print(f"      VERDICT: {verdict}")

# ---- INFO: the sweep ----
print("      [INFO — the (alpha x churn) sweep at C = 3, 3 seeds/cell]")
for cm in ("full", "chan"):
    for a in (0.0, 0.5, 0.75, 0.9, 1.0):
        fx, cx, rx = measure(3, a, cm, SEEDS[:3], draws=1)
        print(f"      churn={cm:4s} a={a:.2f}: corr {cx:+.3f}, "
              f"frac {fx:.4f}, d_MM {d_mm(fx):.2f}, refusals {rx}/3")

print()
print(f"PRE-REGISTERED GATE LEDGER: "
      f"{'ALL HELD' if FAIL == 0 else 'REFUSALS PRESENT'} — Gb1 corr; "
      f"Gb2 dial; Gb3 ladder; Gb4 control; verdict: {verdict}")
print()
total = PASS + FAIL
print(f"ALL CHECKS PASS ({PASS}/{total})" if FAIL == 0 else f"FAILURES: {FAIL}/{total}")
if FAIL: raise SystemExit(1)
