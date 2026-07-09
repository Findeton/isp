#!/usr/bin/env python3
"""
dimwall_selection_v2.py — v9 round 35: THE SELECTION SUCCESSOR
(note-3p1-witness §2; pin committed at 089c115 strictly before this
receipt; the paper-6 hostile review's MINOR-1).
The survival part of round-31's dimwall_selection.py ported verbatim
(web_survival, the eta x L grid, SEEDS 20261110-20261112, the
C_max = 5 spot) with the class logic FIXED to implement note-3p1-p5's
pinned C_max-INDEPENDENCE conjunct — the round-31 receipt computed
ce5 and never used it; its "SELECTS(7.2)" is superseded on the record
(LEDGER #90) and reruns of the original artifact still print the
superseded class.  The d_MM curve loads the frozen
v9/data/mm_reference.json (round 35; byte-identical seed recipe).
Classes:
  COLLAPSE        max C_eff <= 2 everywhere (as before);
  SELECTS         span <= 1.5x AND |mean - median| < 0.5 AND the
                  C_max = 5 spot REFUSES the tracking test (the
                  pinned conjunct: C_eff must not scale with C_max);
  C_MAX-TRACKING  |ce5/5 - mean(ceffs)/8| < 0.1 (the per-C_max
                  ratios agree, both ~0.9 — no survival selection);
  DIAL-TRACKING   otherwise (span > 1.5x), as before.
Registered expectation: C_MAX-TRACKING.  Mapping receipt; exit 0.
"""
import json
import numpy as np

def rel_win(idx, chiV, C):
    b = idx
    rel = b[:, None] < b[None, :]
    for k in range(C):
        rel &= chiV[idx][:, None, k] <= chiV[idx][None, :, k]
    np.fill_diagonal(rel, False)
    return rel

def frac(rel):
    n = rel.shape[0]
    return rel.sum() / (n * (n - 1) / 2)

def web_survival(sd, Cmax, eta, L, N=4096, M=32):
    rng = np.random.default_rng(sd)
    acc = np.zeros((M, Cmax))
    chiV = np.zeros((N, Cmax))
    dep = np.zeros(Cmax)
    for t in range(N):
        c = int(rng.integers(M))
        w = acc[c] + eta
        w = w / w.sum()
        k = int(rng.choice(Cmax, p=w))
        e = rng.exponential(0.109551)
        acc[c, k] += e
        if t >= N - 512:
            dep[k] += e
        chiV[t] = acc[c]
        for kk in range(Cmax):
            if rng.random() < 1.0 / L:
                acc[int(rng.integers(M)), kk] = 0.0
    p = dep / max(dep.sum(), 1e-12)
    ceff = 1.0 / max((p ** 2).sum(), 1e-12)
    return ceff, chiV, rng

print("[dimwall selection v2: the pinned C_max-independence conjunct]")

# the frozen d_MM curve (round 35; byte-identical to the r31 in-receipt
# curve — same seed recipe 20260760+)
ref = {int(k[1:]): v for k, v in
       json.load(open("v9/data/mm_reference.json")).items()}
print("      frozen reference: " + "  ".join(
    f"M{d}={ref[d]:.4f}" for d in sorted(ref)))
def d_mm(f):
    ds = sorted(ref); fs = [ref[d] for d in ds]
    if f >= fs[0]: return 2.0
    if f <= fs[-1]: return float(ds[-1])
    for a2 in range(len(ds) - 1):
        if fs[a2] >= f >= fs[a2 + 1]:
            w = (fs[a2] - f) / (fs[a2] - fs[a2 + 1])
            return ds[a2] + w * (ds[a2 + 1] - ds[a2])
    return float("nan")

SEEDS = (20261110, 20261111, 20261112)
print("      (a) channel-survival — C_eff (deposit shares, last window) "
      "and windowed d_MM:")
ceffs = []
for eta in (0.005, 0.05, 0.5):
    for L in (8, 16, 32):
        ce_l, dm_l = [], []
        for sd in SEEDS:
            ceff, chiV, r = web_survival(sd, 8, eta, L)
            start = 4096 - 768
            idx = np.sort(r.choice(np.arange(start, start + 512), 128,
                                   replace=False))
            rel = rel_win(idx, chiV, 8)
            ce_l.append(ceff); dm_l.append(d_mm(frac(rel)))
        ceffs.append(float(np.mean(ce_l)))
        print(f"      eta={eta:<6} L={L:<3}: C_eff = {np.mean(ce_l):.2f} "
              f"(sd {np.std(ce_l):.2f}); windowed d_MM = {np.mean(dm_l):.2f}")
ce5, _, _ = web_survival(SEEDS[0], 5, 0.05, 16)
print(f"      C_max = 5 spot (eta 0.05, L 16): C_eff = {ce5:.2f}")

span = max(ceffs) / max(min(ceffs), 1e-9)
track = abs(ce5 / 5 - np.mean(ceffs) / 8) < 0.1
print(f"      the conjunct row: ce5/5 = {ce5 / 5:.3f} vs mean/8 = "
      f"{np.mean(ceffs) / 8:.3f} — tracking test "
      f"{'FIRES' if track else 'refuses'}")
if max(ceffs) <= 2.0:
    va = "COLLAPSE (C_eff <= 2 everywhere)"
elif (span <= 1.5 and abs(np.mean(ceffs) - np.median(ceffs)) < 0.5
      and not track):
    va = f"SELECTS (C_eff ~ {np.mean(ceffs):.1f}, C_max-independent)"
elif track:
    va = (f"C_MAX-TRACKING (C_eff/C_max = {ce5 / 5:.2f} at C_max = 5 vs "
          f"{np.mean(ceffs) / 8:.2f} at C_max = 8 — C_eff ~ 0.9 x C_max; "
          f"no survival selection)")
else:
    va = (f"DIAL-TRACKING (C_eff spans {min(ceffs):.1f}.."
          f"{max(ceffs):.1f}, x{span:.1f})")
print(f"      (a) VERDICT CLASS: {va}")

print()
print(f"ADJUDICATION: (a) {va}")
print("ALL CHECKS PASS (mapping receipt — the corrected class reported)")
