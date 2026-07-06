#!/usr/bin/env python3
"""
t23_poisson_intermediates.py — v9 round 13: THEOREM P'S MEASURABLE JOINTS
(note-t23 SS4; gates pinned there and committed at d9189b3 BEFORE this
receipt existed — the freeze discipline's first full cycle).

Theorem P: churn-class supplies with sub-geometric lifetime tails and
atomless content have interval-count statistics -> Poisson at rate
O(L/N) (Chen-Stein over the life-partition dependency graph). Joints:
  P-DOUBLEPRIME BAND PINS (note-t23 SS7, pinned at 080fd89; run-1 and
     run-2 histories frozen at f959aeb / d0f9d87): V1'' both ensembles'
     band gaps decay in N AND churn <= box everywhere; V2'' P3 as the
     N-trend (geom decay >= 1.3x; heavy STRICTLY flatter); V3'' the
     cv2-correct qualifying prediction (det/geom in [0.1, 1.0]); V4
     unchanged. Band = exp_k in [10, 40], the Poisson-target regime.
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
print("[t23 Theorem P-doubleprime joints — the BAND form (note-t23 SS7)]")

def ifano_band(b_, c_, lo=10, hi=40):
    """u1 interval_fano restricted to small intervals (exp_k in [lo, hi])
    — the regime where the absolute Poisson target applies (SS5 diagnostic
    column, unpinned)."""
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
    sel = (exp_k >= lo) & (exp_k <= hi)
    if not np.any(sel): return float("nan")
    resid = btw[ii, jj][sel] - exp_k[sel]
    return float(np.mean(resid ** 2 / exp_k[sel]))

REPS = 24
def cellstats(Nn, life, L):
    full, band = [], []
    for _ in range(REPS):
        chi, _ = web_churn(Nn, M, life, L)
        full.append(abs(interval_fano(np.arange(Nn), chi) - 1.0))
        band.append(abs(ifano_band(np.arange(Nn), chi) - 1.0))
    return (float(np.mean(full)), float(np.std(full, ddof=1)/np.sqrt(REPS)),
            float(np.mean(band)))
def boxstats(Nn):
    full, band = [], []
    for _ in range(REPS):
        v = rng.random(Nn)
        full.append(abs(interval_fano(np.arange(Nn), v) - 1.0))
        band.append(abs(ifano_band(np.arange(Nn), v) - 1.0))
    return (float(np.mean(full)), float(np.std(full, ddof=1)/np.sqrt(REPS)),
            float(np.mean(band)))

def band_cell(Nn, life, L):
    vals = []
    for _ in range(REPS):
        chi, _ = web_churn(Nn, M, life, L)
        vals.append(abs(ifano_band(np.arange(Nn), chi) - 1.0))
    return float(np.mean(vals)), float(np.std(vals, ddof=1)/np.sqrt(REPS))
def band_box(Nn):
    vals = []
    for _ in range(REPS):
        vals.append(abs(ifano_band(np.arange(Nn), rng.random(Nn)) - 1.0))
    return float(np.mean(vals)), float(np.std(vals, ddof=1)/np.sqrt(REPS))

NS = (512, 2048, 4096)
ch = {Nn: band_cell(Nn, "geom", 2) for Nn in NS}
bx = {Nn: band_box(Nn) for Nn in NS}
for Nn in NS:
    print(f"      V1'' N={Nn}: churn {ch[Nn][0]:.4f}+-{ch[Nn][1]:.4f}   "
          f"box {bx[Nn][0]:.4f}+-{bx[Nn][1]:.4f}")
mono_c = ch[512][0] >= ch[2048][0] >= ch[4096][0]
mono_b = bx[512][0] >= bx[2048][0] >= bx[4096][0]
order = all(ch[Nn][0] <= bx[Nn][0] for Nn in NS)
check("V1'' (the band decay + ordering, 24 reps) [directional]: both "
      "ensembles' band gaps decrease monotonically in N AND churn <= box "
      "at every N", mono_c and mono_b and order,
      f"churn mono {mono_c}, box mono {mono_b}, churn<=box {order}")

gg = {Nn: band_cell(Nn, "geom", 4) for Nn in NS}
hh = {Nn: band_cell(Nn, "heavy", 4) for Nn in NS}
rg = gg[512][0] / max(gg[4096][0], 1e-12)
rh = hh[512][0] / max(hh[4096][0], 1e-12)
print(f"      V2'' geom band: " + "  ".join(f"N={n}: {gg[n][0]:.4f}" for n in NS)
      + f"  decay {rg:.2f}x")
print(f"      V2'' heavy band: " + "  ".join(f"N={n}: {hh[n][0]:.4f}" for n in NS)
      + f"  decay {rh:.2f}x")
check("V2'' (Lemma P3 as the N-trend, 24 reps) [directional]: geometric "
      "band-gap decay >= 1.3x from 512 to 4096 AND the heavy-tail decay "
      "ratio STRICTLY below the geometric's (the plateau signature)",
      rg >= 1.3 and rh < rg, f"geom {rg:.2f}x vs heavy {rh:.2f}x")

dd = band_cell(2048, "det", 4)
ratio = dd[0] / max(gg[2048][0], 1e-12)
print(f"      V3'' @2048 mean-4: det {dd[0]:.4f}+-{dd[1]:.4f} vs geom "
      f"{gg[2048][0]:.4f} -> det/geom = {ratio:.2f}")
check("V3'' (the cv2-correct qualifying prediction, 24 reps) "
      "[directional]: det <= geom with det/geom in [0.1, 1.0] (T2.1's "
      "cv2 law's direction; the anti-corpus symmetric pin retired)",
      0.1 <= ratio <= 1.0, f"det/geom = {ratio:.2f}")

ok4 = True
for Nn in (1024, 4096):
    dens = []
    for _ in range(12):
        chi, lid = web_churn(Nn, M, "geom", 2)
        _, counts = np.unique(lid, return_counts=True)
        pairs = float(np.sum(counts * (counts - 1) // 2))
        dens.append(pairs / (Nn * (Nn - 1) / 2.0))
    d = float(np.mean(dens)); pred = 2.0 / (Nn - 1)
    ok4 &= abs(d - pred) / pred <= 0.25
    print(f"      V4 same-life pair density N={Nn}: {d:.6f} vs {pred:.6f} "
          f"({(d/pred-1)*100:+.1f}%)")
check("V4 (the density ledger = paper 16 object): within 25% of "
      "2(L-1)/(N-1) at both N (exact life-id counts)", ok4)

print()
print(f"PRE-REGISTERED GATE LEDGER (P'' band pins, note SS7): "
      f"{'ALL HELD' if FAIL == 0 else 'REFUSALS PRESENT'} — V1'' decay+order; "
      f"V2'' P3 N-trend; V3'' cv2 prediction; V4 ledger")
print()
total = PASS + FAIL
print(f"ALL CHECKS PASS ({PASS}/{total})" if FAIL == 0 else f"FAILURES: {FAIL}/{total}")
if FAIL: raise SystemExit(1)
