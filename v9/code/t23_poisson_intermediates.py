#!/usr/bin/env python3
"""
t23_poisson_intermediates.py — v9 round 13: THEOREM P'S MEASURABLE JOINTS
(note-t23 SS4; gates pinned there and committed at d9189b3 BEFORE this
receipt existed — the freeze discipline's first full cycle).

Theorem P: churn-class supplies with sub-geometric lifetime tails and
atomless content have interval-count statistics -> Poisson at rate
O(L/N) (Chen-Stein over the life-partition dependency graph). Joints:
  V1 the rate: pooled |fano - 1| gap at (32, 2) decreasing in N across
     {512..4096}, total decrease >= 4x (O(1/N) predicts 8x) [directional].
  V2 the density mechanism: gap at N = 2048 monotone non-decreasing in
     L across {2, 4, 8} [directional].
  V3 the tail boundary (Lemma P3, load-bearing): matched mean-lifetime 4 —
     geometric vs deterministic-4 (both qualify) within 2x of each other;
     heavy-tail (1 + Pareto(1.5), infinite variance, VIOLATES the
     hypothesis) exceeds geometric by >= 3x [directional].
  V4 the density ledger: same-life pair density = 2(L-1)/(N-1) within
     25% at (32, 2), N in {1024, 4096} (exact count from life ids).
Instrument: u1's interval_fano VERBATIM (the cell's own z-layer object).
Seed 20260720; float64 landscapes; 12 reps/cell. Exit 1 by design on
refusal; first-run ledger preserved in-note if any amendment occurs.
"""
import numpy as np

rng = np.random.default_rng(20260720)
PASS = 0
FAIL = 0

def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    if ok: PASS += 1
    else: FAIL += 1
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

def dominance_order(pts):
    return (pts[None, :, 0] > pts[:, None, 0]) & (pts[None, :, 1] > pts[:, None, 1])

def interval_fano(b_, c_, kmin=10):
    pts_ = np.column_stack([np.asarray(b_, dtype=float), c_])
    Np = len(pts_)
    C = dominance_order(pts_)
    r1 = np.argsort(np.argsort(pts_[:, 0]))
    r2 = np.argsort(np.argsort(pts_[:, 1]))
    Cf = C.astype(np.float32)
    btw = np.rint(Cf @ Cf).astype(np.int32)
    ii, jj = np.nonzero(C)
    dr1 = (r1[jj] - r1[ii]).astype(float)
    dr2 = (r2[jj] - r2[ii]).astype(float)
    exp_k = (dr1 - 1) * (dr2 - 1) / Np
    sel = exp_k >= kmin
    resid = btw[ii, jj][sel] - exp_k[sel]
    return float(np.mean(resid ** 2 / exp_k[sel]))


def web_churn(Nn, M, life="geom", L=2):
    """j3-class churn with pluggable lifetime law. life in {geom, det,
    heavy}: geom = reset w.p. 1/L per own commit (mean L); det = reset
    after exactly L own commits; heavy = per-life budget 1 + Pareto(1.5)
    own commits (mean 4, infinite variance — violates sub-geometric)."""
    chi_acc = np.zeros(M)
    own = np.zeros(M, dtype=np.int64)
    budget = np.zeros(M)
    life_id = np.arange(M).copy(); next_id = M
    if life == "heavy":
        budget = 1.0 + (rng.random(M) ** (-1.0 / 1.5))
    chi = np.zeros(Nn); lid = np.zeros(Nn, dtype=np.int64)
    for t in range(Nn):
        c = int(rng.integers(M))
        chi_acc[c] += rng.exponential(1.0)
        own[c] += 1
        chi[t] = chi_acc[c]; lid[t] = life_id[c]
        reset = False
        if life == "geom":
            reset = rng.random() < 1.0 / L
        elif life == "det":
            reset = own[c] >= L
        elif life == "heavy":
            reset = own[c] >= budget[c]
        if reset:
            chi_acc[c] = 0.0; own[c] = 0
            life_id[c] = next_id; next_id += 1
            if life == "heavy":
                budget[c] = 1.0 + (rng.random() ** (-1.0 / 1.5))
    return chi, lid

M = 32
print("[t23 Theorem P joints — Poissonization of the churn class]")

def fano_gap(Nn, life, L, reps=12):
    gaps = []
    for _ in range(reps):
        chi, _ = web_churn(Nn, M, life, L)
        gaps.append(abs(interval_fano(np.arange(Nn), chi) - 1.0))
    return float(np.mean(gaps)), float(np.std(gaps, ddof=1) / np.sqrt(reps))

# V1: the rate in N
g = {}
for Nn in (512, 1024, 2048, 4096):
    g[Nn] = fano_gap(Nn, "geom", 2)
print("      V1 |fano-1| gap: " + "  ".join(
    f"N={n}: {v[0]:.4f}+-{v[1]:.4f}" for n, v in g.items()))
mono = all(g[a][0] >= g[b][0] for a, b in ((512, 1024), (1024, 2048), (2048, 4096)))
ratio = g[512][0] / max(g[4096][0], 1e-12)
check("V1 (the rate, Lemma P2) [directional, 12 reps]: the gap decreases "
      "monotonically in N AND falls >= 4x from 512 to 4096 (O(1/N) "
      "predicts 8x)", mono and ratio >= 4,
      f"monotone: {mono}; 512->4096 ratio {ratio:.1f}x")

# V2: the L-dependence at N = 2048
gl = {}
for L in (2, 4, 8):
    gl[L] = fano_gap(2048, "geom", L)
print("      V2 gap vs L @2048: " + "  ".join(
    f"L={l}: {v[0]:.4f}+-{v[1]:.4f}" for l, v in gl.items()))
monoL = gl[2][0] <= gl[4][0] <= gl[8][0]
check("V2 (the density mechanism) [directional, 12 reps]: the gap is "
      "monotone non-decreasing in L (same-lineage pair density ~ L/N)",
      monoL, f"{gl[2][0]:.4f} <= {gl[4][0]:.4f} <= {gl[8][0]:.4f}")

# V3: the tail boundary at matched mean lifetime 4
gg = fano_gap(2048, "geom", 4)
gd = fano_gap(2048, "det", 4)
gh = fano_gap(2048, "heavy", 4)
print(f"      V3 @2048, mean-lifetime 4: geom {gg[0]:.4f}+-{gg[1]:.4f}, "
      f"det {gd[0]:.4f}+-{gd[1]:.4f}, heavy {gh[0]:.4f}+-{gh[1]:.4f}")
qual2 = max(gg[0], gd[0]) / max(min(gg[0], gd[0]), 1e-12) <= 2.0
heavy3 = gh[0] >= 3.0 * gg[0]
check("V3 (Lemma P3, the load-bearing tail hypothesis) [directional, "
      "12 reps]: the two QUALIFYING laws within 2x of each other; the "
      "heavy-tail (infinite-variance) law exceeds geometric >= 3x — the "
      "plateau signature", qual2 and heavy3,
      f"qualifying ratio {max(gg[0],gd[0])/max(min(gg[0],gd[0]),1e-12):.2f}; "
      f"heavy/geom {gh[0]/max(gg[0],1e-12):.1f}x")

# V4: the density ledger (exact count from life ids)
ok4 = True
for Nn in (1024, 4096):
    dens = []
    for _ in range(12):
        chi, lid = web_churn(Nn, M, "geom", 2)
        _, counts = np.unique(lid, return_counts=True)
        pairs = float(np.sum(counts * (counts - 1) // 2))
        dens.append(pairs / (Nn * (Nn - 1) / 2.0))
    d = float(np.mean(dens))
    pred = 2.0 * (2 - 1) / (Nn - 1)
    ok = abs(d - pred) / pred <= 0.25
    ok4 &= ok
    print(f"      V4 same-life pair density N={Nn}: {d:.6f} vs 2(L-1)/(N-1) "
          f"= {pred:.6f} ({(d/pred-1)*100:+.1f}%)")
check("V4 (the density ledger = paper 16's object): measured within 25% "
      "of 2(L-1)/(N-1) at both N (exact life-id counts)", ok4)

print()
print(f"PRE-REGISTERED GATE LEDGER: {'ALL HELD' if FAIL == 0 else 'REFUSALS PRESENT'} "
      f"— V1 rate; V2 L-density; V3 tail boundary; V4 ledger")
print()
total = PASS + FAIL
print(f"ALL CHECKS PASS ({PASS}/{total})" if FAIL == 0 else f"FAILURES: {FAIL}/{total}")
if FAIL: raise SystemExit(1)
