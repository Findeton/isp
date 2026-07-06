#!/usr/bin/env python3
"""
dimwall_phase1.py — v9 round 24: PHASE 1 — does dimension track the
number of evidence channels?  (note-3p1-p1; pin committed at 6640aff
strictly before this receipt.  NO-REVIEW MODE on record; instruments =
the Phase-0-certified tester + the measured MM curve, re-derived here.)

Builder: wb-line churn web, C independent evidence channels (each click
deposits Exp evidence in ONE uniform channel of the committing slot;
commits snapshot the slot vector; churn resets the victim's WHOLE
vector).  Dominance: b strict AND all channels weak-<= (slot worldlines
stay chains; dim <= C+1 by the Lemma; C = 1 = the corpus class).

PINNED (note SS3):
  Gm1  2-realizer REFUSES 144-subposets of C = 2 and C = 3 webs on
       >= 4/5 seeds each (2 draws/seed; refusal on an induced subposet
       witnesses whole-web dim >= 3).
  Gm2  C = 1 webs PASS 5/5 (the control).
  Gm3  d_MM (Phase-0 calibrated curve, full webs) strictly monotone in
       C and >= 2.5 at C = 2, >= 3.0 at C = 3 (seed means).
  Gm4  INFO: analytic 2^-C polyhedral refs + measured iid dominance;
       channel-correlation diagnostic; per-channel-reset variant;
       no-churn variant.
Verdicts: DIMENSION-TRACKS-CHANNELS [MEASURED; C = 3 flagged
PENDING-USER-REVIEW-DECISION] / CLOCK-COLLAPSE / DIM-WITHOUT-VOLUME.
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

# ---------- Phase-0 tester (certified Gw 300/300), verbatim ----------
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

# ---------- the multi-channel builder ----------
def web_rel_C(sd, C, N=2048, M=32, L=16, reset="full", churn=True):
    rng = np.random.default_rng(sd)
    acc = np.zeros((M, C))
    chiV = np.zeros((N, C))
    for t in range(N):
        c = int(rng.integers(M))
        k = int(rng.integers(C))
        acc[c, k] += rng.exponential(0.109551)
        chiV[t] = acc[c]
        if churn and rng.random() < 1.0 / L:
            v = int(rng.integers(M))
            if reset == "full":
                acc[v] = 0.0
            else:                       # per-channel reset (INFO probe)
                acc[v, int(rng.integers(C))] = 0.0
    b = np.arange(N)
    rel = b[:, None] < b[None, :]
    for k in range(C):
        rel &= chiV[:, None, k] <= chiV[None, :, k]
    np.fill_diagonal(rel, False)
    return rel, chiV, rng

def frac(rel):
    n = rel.shape[0]
    return rel.sum() / (n * (n - 1) / 2)

print("[dimwall Phase 1: the multi-channel builder]")

# ---------- the MM calibration (Phase-0 recipe, re-derived) ----------
ref = {}
for d, tag in ((1, "M2"), (2, "M3"), (3, "M4")):
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

# ---------- the grid ----------
SEEDS = list(range(20260770, 20260775))
dmm = {}
refuse = {}
corr_diag = {}
for C in (1, 2, 3):
    fr_list, ref_ct, cd = [], 0, []
    for sd in SEEDS:
        rel, chiV, r = web_rel_C(sd, C)
        fr_list.append(frac(rel))
        if C >= 2:
            hit = False
            for _ in range(2):
                idx = np.sort(r.choice(2048, 144, replace=False))
                if not dim_le_2(rel[np.ix_(idx, idx)]):
                    hit = True
                    break
            ref_ct += hit
        else:
            idx = np.sort(r.choice(2048, 144, replace=False))
            ref_ct += dim_le_2(rel[np.ix_(idx, idx)])
        if C >= 2:
            cc = np.corrcoef(chiV.T)
            cd.append(float(np.mean(cc[np.triu_indices(C, 1)])))
    dmm[C] = d_mm(float(np.mean(fr_list)))
    refuse[C] = ref_ct
    corr_diag[C] = float(np.mean(cd)) if cd else float("nan")
    print(f"      C = {C}: fraction {np.mean(fr_list):.4f} "
          f"(iid polyhedral ref {2.0**(-C):.4f}) => d_MM = {dmm[C]:.2f}; "
          f"{'2-realizer REFUSALS' if C >= 2 else '2-realizer PASSES'} "
          f"{ref_ct}/5; channel-corr {corr_diag[C]:+.3f}" if C >= 2 else
          f"      C = {C}: fraction {np.mean(fr_list):.4f} "
          f"(iid ref {2.0**(-C):.4f}) => d_MM = {dmm[C]:.2f}; "
          f"2-realizer PASSES {ref_ct}/5")

check("Gm1 (THE WALL COMES DOWN): 2-realizer REFUSES C = 2 and C = 3 "
      "web subposets on >= 4/5 seeds each",
      refuse[2] >= 4 and refuse[3] >= 4,
      f"C=2: {refuse[2]}/5, C=3: {refuse[3]}/5")
check("Gm2 (the control): C = 1 webs PASS on 5/5", refuse[1] == 5,
      f"{refuse[1]}/5")
gm3 = (dmm[1] < dmm[2] < dmm[3]) and dmm[2] >= 2.5 and dmm[3] >= 3.0
check("Gm3 (the dimension dial): d_MM strictly monotone in C; >= 2.5 at "
      "C = 2; >= 3.0 at C = 3",
      gm3, f"d_MM = {dmm[1]:.2f} / {dmm[2]:.2f} / {dmm[3]:.2f}")

if refuse[2] >= 4 and refuse[3] >= 4 and refuse[1] == 5 and gm3:
    verdict = ("DIMENSION-TRACKS-CHANNELS [MEASURED; the C = 3 leg "
               "flagged PENDING-USER-REVIEW-DECISION per PLAN]")
elif not (refuse[2] >= 4 and refuse[3] >= 4):
    verdict = "CLOCK-COLLAPSE (see the correlation diagnostic + variants)"
else:
    verdict = "DIM-WITHOUT-VOLUME (order dimension rises; the estimator lags)"
print(f"      VERDICT: {verdict}")

# ---------- Gm4 INFO: iid dominance + variants ----------
print("      [Gm4 — INFO, unpinned]")
for C in (2, 3):
    r = np.random.default_rng(20260780 + C)
    Z = r.random((512, C + 1))
    rel = np.ones((512, 512), dtype=bool)
    for k in range(C + 1):
        rel &= Z[:, None, k] < Z[None, :, k]
    np.fill_diagonal(rel, False)
    print(f"      iid (C+1)-dominance measured (C = {C}): {frac(rel):.4f} "
          f"(analytic {2.0**(-C):.4f}) => d_MM = {d_mm(frac(rel)):.2f}")
for C in (2, 3):
    fr_v = [frac(web_rel_C(sd, C, reset="chan")[0]) for sd in SEEDS[:3]]
    fr_n = [frac(web_rel_C(sd, C, churn=False)[0]) for sd in SEEDS[:3]]
    print(f"      C = {C} variants: per-channel-reset d_MM = "
          f"{d_mm(float(np.mean(fr_v))):.2f}; no-churn d_MM = "
          f"{d_mm(float(np.mean(fr_n))):.2f}")

print()
print(f"PRE-REGISTERED GATE LEDGER: "
      f"{'ALL HELD' if FAIL == 0 else 'REFUSALS PRESENT'} — Gm1 wall; "
      f"Gm2 control; Gm3 dial; verdict: {verdict}")
print()
total = PASS + FAIL
print(f"ALL CHECKS PASS ({PASS}/{total})" if FAIL == 0 else f"FAILURES: {FAIL}/{total}")
if FAIL: raise SystemExit(1)
