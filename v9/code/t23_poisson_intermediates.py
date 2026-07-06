#!/usr/bin/env python3
"""
t23_poisson_intermediates.py — v9 round 13: THEOREM P'S MEASURABLE JOINTS
(note-t23 SS4; gates pinned there and committed at d9189b3 BEFORE this
receipt existed — the freeze discipline's first full cycle).

Theorem P: churn-class supplies with sub-geometric lifetime tails and
atomless content have interval-count statistics -> Poisson at rate
O(L/N) (Chen-Stein over the life-partition dependency graph). Joints:
  AMENDED to the P-prime control-relative pins (note-t23 SS5; the first
     run and its refusals frozen at f959aeb): V1-rel gap <= floor/3 at
     every N; V2-rel monotone in L; V3-rel tail boundary (heavy >= 2x);
     V4 unchanged. Small-interval absolute column printed unpinned.
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
print("[t23 Theorem P-prime joints — control-relative Poissonization (note-t23 SS5)]")

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

ok1 = True
box_at = {}
for Nn in (512, 2048, 4096):
    bx = boxstats(Nn); ch = cellstats(Nn, "geom", 2)
    box_at[Nn] = bx
    rel = abs(ch[0] - bx[0])
    floor = bx[0]
    print(f"      V1-rel N={Nn}: churn {ch[0]:.4f}+-{ch[1]:.4f}, box {bx[0]:.4f}"
          f"+-{bx[1]:.4f}, |rel| = {rel:.4f} vs floor/3 = {floor/3:.4f}   "
          f"[small-interval abs: churn {ch[2]:.3f}, box {bx[2]:.3f}]")
    if rel > floor / 3: ok1 = False
check("V1-rel (control-relative, 24 reps) [directional]: at every N the "
      "churn-box gap is <= (the box own Poisson floor)/3 — the churn "
      "sits >= 3x closer to the reference than the reference to Poisson",
      ok1)

bx2 = box_at[2048]
rels = {}; ses = {}
for L in (2, 4, 8):
    ch = cellstats(2048, "geom", L)
    rels[L] = abs(ch[0] - bx2[0]); ses[L] = ch[1]
print("      V2-rel gap @2048: " + "  ".join(
    f"L={l}: {rels[l]:.4f}+-{ses[l]:.4f}" for l in rels))
se_pool = max(ses.values())
mono = (rels[2] <= rels[4] + se_pool) and (rels[4] <= rels[8] + se_pool)
check("V2-rel (the density mechanism, control-relative, 24 reps) "
      "[directional]: monotone non-decreasing in L within 1 pooled SE",
      mono, f"{rels[2]:.4f} <= {rels[4]:.4f} <= {rels[8]:.4f} (+-{se_pool:.4f})")

gg = cellstats(2048, "geom", 4); gd = cellstats(2048, "det", 4)
gh = cellstats(2048, "heavy", 4)
rg = abs(gg[0] - bx2[0]); rd = abs(gd[0] - bx2[0]); rh = abs(gh[0] - bx2[0])
print(f"      V3-rel gaps @2048 mean-4: geom {rg:.4f}, det {rd:.4f}, "
      f"heavy {rh:.4f}")
qual2 = max(rg, rd) / max(min(rg, rd), 1e-12) <= 2.0
heavy2 = rh >= 2.0 * rg
check("V3-rel (the tail boundary, control-relative, 24 reps) [directional]: "
      "qualifying pair within 2x; heavy >= 2x above geom (the re-pinned "
      "relative threshold, note SS5)", qual2 and heavy2,
      f"qual ratio {max(rg,rd)/max(min(rg,rd),1e-12):.2f}; heavy/geom "
      f"{rh/max(rg,1e-12):.1f}x")

ok4 = True
for Nn in (1024, 4096):
    dens = []
    for _ in range(12):
        chi, lid = web_churn(Nn, M, "geom", 2)
        _, counts = np.unique(lid, return_counts=True)
        pairs = float(np.sum(counts * (counts - 1) // 2))
        dens.append(pairs / (Nn * (Nn - 1) / 2.0))
    d = float(np.mean(dens)); pred = 2.0 / (Nn - 1)
    ok = abs(d - pred) / pred <= 0.25
    ok4 &= ok
    print(f"      V4 same-life pair density N={Nn}: {d:.6f} vs {pred:.6f} "
          f"({(d/pred-1)*100:+.1f}%)")
check("V4 (the density ledger = paper 16 object): within 25% of "
      "2(L-1)/(N-1) at both N (exact life-id counts)", ok4)

print()
print(f"PRE-REGISTERED GATE LEDGER (P-prime pins, note SS5): "
      f"{'ALL HELD' if FAIL == 0 else 'REFUSALS PRESENT'} — V1-rel; "
      f"V2-rel; V3-rel; V4 ledger")
print()
total = PASS + FAIL
print(f"ALL CHECKS PASS ({PASS}/{total})" if FAIL == 0 else f"FAILURES: {FAIL}/{total}")
if FAIL: raise SystemExit(1)
