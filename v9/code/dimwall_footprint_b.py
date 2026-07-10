#!/usr/bin/env python3
"""
dimwall_footprint_b.py — v9 round 40, the ablation receipt (pin: the
Round-40-corrections section of note-3p1-lorentz2-footprint, commit
b1dc125, strictly before this file ran).

Adjudicates the attribution of the corner-web F concentration among:
m1 deposit sparsity (Ga1: the one-hot line), m2 alpha-preference (Ga2:
alpha = 0 webs), m3 slot-chain temporal correlation (Ga3: shuffled
snapshots). Plus the review's INFO set: tie/cap-mass prints, the q x
s_min robustness grid, the tie-immune angular functional.

Machinery copied verbatim from dimwall_footprint.py (round 40; itself
verbatim from dimwall_lorentz1.py round 36 with sprinkle_m4 renamed
m4diamond — the disclosed rename).
"""
import numpy as np

PASS = FAIL = 0
def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    if ok: PASS += 1
    else: FAIL += 1
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

def orthant4(rng, N):
    Z = rng.random((N, 4))
    rel = np.ones((N, N), dtype=bool)
    for j in range(4):
        rel &= Z[:, None, j] < Z[None, :, j]
    np.fill_diagonal(rel, False)
    return rel, Z

def web_window(sd, mode, C=3, N=2048, M=32, L=16, alpha=0.75, D=1024, NW=256,
               shuffle=False):
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
    chi = chiV[idx]
    if shuffle:
        chi = chi[rng.permutation(NW)]   # Ga3: destroy temporal coupling
    coords = np.column_stack([idx.astype(float), chi])
    b = idx
    rel = b[:, None] < b[None, :]
    for k in range(C):
        rel &= chi[:, None, k] <= chi[None, :, k]
    np.fill_diagonal(rel, False)
    return rel, coords

def onehot_line(sd, C=3, N=2048, D=1024, NW=256):
    """Ga1: a single accumulator, no slots / churn / preference."""
    rng = np.random.default_rng(sd)
    chiV = np.zeros((N, C))
    acc = np.zeros(C)
    for t in range(N):
        acc[int(rng.integers(C))] += rng.exponential(0.109551)
        chiV[t] = acc
    start = (N - D) // 2
    idx = np.sort(rng.choice(np.arange(start, start + D), NW, replace=False))
    coords = np.column_stack([idx.astype(float), chiV[idx]])
    rel = idx[:, None] < idx[None, :]
    for k in range(C):
        rel &= chiV[idx][:, None, k] <= chiV[idx][None, :, k]
    np.fill_diagonal(rel, False)
    return rel, coords

def footprint(rel, coords, q=0.9, s_min=0.3, angular=False, tiestats=False):
    X = (coords - coords.mean(0)) / np.maximum(coords.std(0), 1e-9)
    k = X.shape[1]
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
    keep = s >= s_min
    d = d[keep]; s = s[keep]
    w = d - s[:, None] * dhat[None, :]
    v = w / s[:, None]
    if angular:
        v = v / np.maximum(np.linalg.norm(v, axis=1, keepdims=True), 1e-12)
    hs_c, hs_f = [], []
    capmass = []
    cap = 1.0 / np.sqrt(3.0)
    for u in dirs:
        p = v @ u
        pp = p[p > 0]
        hs_c.append(np.quantile(pp, q) if len(pp) >= 30 else np.nan)
        m = v @ (-u)
        mm = m[m > 0]
        hs_f.append(np.quantile(mm, q) if len(mm) >= 30 else np.nan)
        if tiestats and not angular:
            capmass.append(float((np.abs(mm - cap) < 1e-9).mean()) if len(mm) else 0.0)
    F = float(np.mean(hs_c) / np.mean(hs_f))
    extra = None
    if tiestats:
        # tie fraction: kept pairs with an exact zero in some non-axial
        # component (raw ties survive the affine standardization)
        tie = float((np.abs(d[:, 1:]) < 1e-12).any(axis=1).mean()) if k > 1 else 0.0
        extra = (tie, capmass)
    return F, len(s), extra

def band(build, seeds, label, **kw):
    Fs = []
    for sd in seeds:
        rel, coords = build(sd)
        F, npairs, extra = footprint(rel, coords, **kw)
        Fs.append(F)
        ex = (f", tie-frac {extra[0]:.3f}, face cap-mass "
              f"{np.round(extra[1], 3).tolist()}") if kw.get("tiestats") else ""
        print(f"      {label} seed {sd}: F = {F:6.3f} (pairs {npairs}{ex})")
    return np.array(Fs)

print("[footprint ablation receipt — round 40 corrections]")
S40 = [20262000 + i for i in range(5)]
SAB = [20262100 + i for i in range(5)]

# Gb-w: wiring — reproduce the round-40 corner and orthant prints
R40_CORNER = [2.218, 1.949, 2.179, 2.316, 2.180]
R40_ORTH = [1.363, 1.307, 1.345, 1.392, 1.334]
print("    wiring rerun (round-40 seeds):")
Fc = band(lambda sd: web_window(sd, "corner"), S40, "corner  ", tiestats=True)
Fo = band(lambda sd: orthant4(np.random.default_rng(sd), 256), S40,
          "orthant ", tiestats=True)
okw = (np.round(Fc, 3) == np.array(R40_CORNER)).all() and \
      (np.round(Fo, 3) == np.array(R40_ORTH)).all()
check("Gb-w (wiring): round-40 corner and orthant F reproduced exactly",
      okw, f"corner {np.round(Fc,3).tolist()}, orthant {np.round(Fo,3).tolist()}")

# the ablations
print("    Ga1 (m1 alone — the one-hot line, no slots/churn/preference):")
F1 = band(onehot_line, SAB, "onehot  ", tiestats=True)
print("    Ga2 (m2 removed — corner webs, alpha = 0):")
F2 = band(lambda sd: web_window(sd, "corner", alpha=0.0), SAB, "alpha0  ",
          tiestats=True)
print("    Ga3 (m3 removed — corner webs, snapshots shuffled):")
F3 = band(lambda sd: web_window(sd, "corner", shuffle=True), SAB, "shuffle ",
          tiestats=True)

print(f"      BANDS: corner [{Fc.min():.3f},{Fc.max():.3f}] | "
      f"orthant [{Fo.min():.3f},{Fo.max():.3f}] | M4 (round 40) [0.983,0.999]")
print(f"      Ga1 one-hot  mean {F1.mean():.3f} band [{F1.min():.3f},{F1.max():.3f}]")
print(f"      Ga2 alpha=0  mean {F2.mean():.3f} band [{F2.min():.3f},{F2.max():.3f}]")
print(f"      Ga3 shuffled mean {F3.mean():.3f} band [{F3.min():.3f},{F3.max():.3f}]")
check("Ga1-3 (attribution probe): all three ablation bands computed and "
      "printed with the reference bands", np.isfinite(np.concatenate([F1, F2, F3])).all())

# INFO: tie-immune angular functional
print("    INFO: tie-immune angular functional (corner + orthant, round-40 seeds):")
Fang_c = [footprint(*web_window(sd, "corner"), angular=True)[0] for sd in S40]
Fang_o = []
for sd in S40:
    rng = np.random.default_rng(sd)
    Fang_o.append(footprint(*orthant4(rng, 256), angular=True)[0])
print(f"      F_ang corner {np.round(Fang_c,3).tolist()} | "
      f"orthant {np.round(Fang_o,3).tolist()}")

# INFO: robustness grid
print("    INFO: robustness grid (seed-mean F, corner | orthant):")
for q in (0.8, 0.9, 0.95):
    row = []
    for sm in (0.2, 0.3, 0.5):
        fc = np.mean([footprint(*web_window(sd, "corner"), q=q, s_min=sm)[0]
                      for sd in S40])
        fo = np.mean([footprint(*orthant4(np.random.default_rng(sd), 256),
                                q=q, s_min=sm)[0] for sd in S40])
        row.append(f"q{q}/s{sm}: {fc:.2f}|{fo:.2f}")
    print("      " + "  ".join(row))

print()
total = PASS + FAIL
print(f"ALL CHECKS PASS ({PASS}/{total})" if FAIL == 0
      else f"FAILURES: {FAIL}/{total}")
if FAIL: raise SystemExit(1)
