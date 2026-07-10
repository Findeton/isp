#!/usr/bin/env python3
"""
dimwall_footprint.py — v9 round 40: Lorentz II, the footprint instrument
(note-3p1-lorentz2-footprint; pin committed strictly before this ran).
Builders copied verbatim from dimwall_lorentz1.py (round 36) per the pin.

The statistic: for related pairs, v = w/s (transverse over axial in the
standardized frame); directional support h(u) = q90 of positive
projections v.u; F = mean corner support / mean face support.
Round cone: F ~ 1. Orthant cone: F >> 1. Gates per the pin; exit 1 by
design on refusal.
"""
import numpy as np

PASS = FAIL = 0
def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    if ok: PASS += 1
    else: FAIL += 1
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

# ---- builders (verbatim from dimwall_lorentz1.py, round 36) ----
def m4diamond(rng, N):
    P = np.empty((0, 4))
    while len(P) < N:
        t = rng.random(6 * N)
        x = rng.uniform(-0.5, 0.5, (6 * N, 3))
        r = np.linalg.norm(x, axis=1)
        keep = (r <= t) & (r <= 1 - t)
        P = np.vstack([P, np.column_stack([t[keep], x[keep]])])
    P = P[:N]
    dt = P[None, :, 0] - P[:, None, 0]
    dx = np.linalg.norm(P[None, :, 1:] - P[:, None, 1:], axis=2)
    rel = (dt > 0) & (dt >= dx)
    np.fill_diagonal(rel, False)
    return rel, P

def orthant4(rng, N):
    Z = rng.random((N, 4))
    rel = np.ones((N, N), dtype=bool)
    for j in range(4):
        rel &= Z[:, None, j] < Z[None, :, j]
    np.fill_diagonal(rel, False)
    return rel, Z

def web_window(sd, mode, C=3, N=2048, M=32, L=16, alpha=0.75, D=1024, NW=256):
    rng = np.random.default_rng(sd)
    acc = np.zeros((M, C))
    chiV = np.zeros((N, C))
    if mode == "kdir":
        Wd = rng.dirichlet(np.ones(C), size=M)
    pref = np.arange(M) % C
    for t in range(N):
        c = int(rng.integers(M))
        e = rng.exponential(0.109551)
        if mode == "kdir":
            acc[c] += e * Wd[c]
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
    start = (N - D) // 2
    idx = np.sort(rng.choice(np.arange(start, start + D), NW, replace=False))
    coords = np.column_stack([idx.astype(float), chiV[idx]])
    b = idx
    rel = b[:, None] < b[None, :]
    for k in range(C):
        rel &= chiV[idx][:, None, k] <= chiV[idx][None, :, k]
    np.fill_diagonal(rel, False)
    return rel, coords

# ---- the footprint statistic ----
S_MIN = 0.3
Q = 0.9
MIN_PROJ = 30

# pinned M4 tetrad in the (x,y,z) transverse space (embedded, t = 0)
TETRAD_M4 = np.array([[0, 1, 1, 1], [0, 1, -1, -1],
                      [0, -1, 1, -1], [0, -1, -1, 1]], float)
TETRAD_M4 /= np.linalg.norm(TETRAD_M4, axis=1, keepdims=True)
# rotated probe tetrad (fixed rotation about the x-axis by 0.5 rad,
# then z by 0.3 rad; pinned)
def _rot(axis_pair, ang, V):
    a, b = axis_pair
    W = V.copy()
    W[:, a] = np.cos(ang) * V[:, a] - np.sin(ang) * V[:, b]
    W[:, b] = np.sin(ang) * V[:, a] + np.cos(ang) * V[:, b]
    return W
TETRAD_M4_ALT = _rot((2, 3), 0.3, _rot((1, 2), 0.5, TETRAD_M4))

def footprint(rel, coords, family, tetrad=None):
    X = (coords - coords.mean(0)) / np.maximum(coords.std(0), 1e-9)
    k = X.shape[1]
    if family == "m4":
        dhat = np.array([1.0, 0, 0, 0])
        dirs = TETRAD_M4 if tetrad is None else tetrad
    else:
        dhat = np.ones(k) / np.sqrt(k)
        dirs = []
        for a in range(k):
            e = np.zeros(k); e[a] = 1.0
            w = e - (e @ dhat) * dhat
            dirs.append(w / np.linalg.norm(w))
        dirs = np.array(dirs)
    ii, jj = np.where(rel)
    d = X[jj] - X[ii]
    s = d @ dhat
    keep = s >= S_MIN
    d = d[keep]; s = s[keep]
    w = d - s[:, None] * dhat[None, :]
    v = w / s[:, None]
    hs_c, hs_f, counts = [], [], []
    for u in dirs:
        for sign, bucket in ((1.0, hs_c), (-1.0, hs_f)):
            p = v @ (sign * u)
            p = p[p > 0]
            counts.append(len(p))
            bucket.append(np.quantile(p, Q) if len(p) >= MIN_PROJ else np.nan)
    F = float(np.mean(hs_c) / np.mean(hs_f))
    return F, len(s), min(counts), hs_c, hs_f

def family_F(build, family, label, seeds, tetrad=None):
    out = []
    for t, sd in enumerate(seeds):
        rng = np.random.default_rng(sd)
        if family == "web":
            rel, coords = build(sd)
            fam = "dom"
        else:
            rel, coords = build(rng, 256)
            fam = family
        F, npairs, minproj, hc, hf = footprint(rel, coords, fam, tetrad)
        out.append(F)
        print(f"      {label} seed {sd}: F = {F:6.3f}  (pairs {npairs}, "
              f"min dir-count {minproj}, corner supports "
              f"{np.round(hc,3).tolist()}, face {np.round(hf,3).tolist()})")
    return np.array(out)

print("[footprint receipt — Lorentz II]")
SEEDS = [20262000 + i for i in range(5)]

print("    M4 diamond (own coordinates, round anchor):")
F_m4 = family_F(m4diamond, "m4", "m4      ", SEEDS)
print("    orthant-iid k = 4 (polyhedral anchor):")
F_or = family_F(orthant4, "dom", "orthant ", SEEDS)

ok0 = np.isfinite(F_m4).all() and np.isfinite(F_or).all() and \
      F_or.min() > F_m4.max()
check("Gf0 (certification): min orthant F > max M4 F, strict separation "
      "5/5 vs 5/5", ok0,
      f"orthant [{F_or.min():.3f}, {F_or.max():.3f}] vs "
      f"M4 [{F_m4.min():.3f}, {F_m4.max():.3f}]")
if not ok0:
    print("\nVOID-INSTRUMENT-V: certification refused; no web is read.")
    print(f"FAILURES: 1")
    raise SystemExit(1)

print("    corner C = 3 webs (windowed):")
F_co = family_F(lambda sd: web_window(sd, "corner"), "web", "corner  ", SEEDS)
print("    kdir C = 3 webs (Dirichlet channel mixing):")
F_kd = family_F(lambda sd: web_window(sd, "kdir"), "web", "kdir    ", SEEDS)

side = "polyhedral" if F_co.min() > F_m4.max() else \
       ("round" if F_co.max() < F_or.min() else "between")
check("Gf1 (baseline, registered [directional]: polyhedral): corner-web F "
      "band printed and classified", np.isfinite(F_co).all(),
      f"corner [{F_co.min():.3f}, {F_co.max():.3f}] -> {side.upper()} "
      f"(M4 max {F_m4.max():.3f}, orthant min {F_or.min():.3f})")

mk, mc = F_kd.mean(), F_co.mean()
check("Gf2 (THE MIXING QUESTION) [directional]: mean F(kdir) < mean "
      "F(corner) — mixing rounds the cone", mk < mc,
      f"kdir {mk:.3f} vs corner {mc:.3f} (shift {mk-mc:+.3f})")

print("    INFO: M4 rotated-tetrad probe (fairness):")
F_m4alt = family_F(m4diamond, "m4", "m4-alt  ", SEEDS, tetrad=TETRAD_M4_ALT)
print(f"      INFO: M4 alt-tetrad band [{F_m4alt.min():.3f}, "
      f"{F_m4alt.max():.3f}] vs pinned [{F_m4.min():.3f}, {F_m4.max():.3f}]"
      f" — frame-choice sensitivity "
      f"{'WITHIN' if (F_m4alt.min() <= F_m4.max() and F_m4.min() <= F_m4alt.max()) else 'OUTSIDE'} band overlap")

print()
total = PASS + FAIL
print(f"ALL CHECKS PASS ({PASS}/{total})" if FAIL == 0
      else f"FAILURES: {FAIL}/{total}")
if FAIL: raise SystemExit(1)
