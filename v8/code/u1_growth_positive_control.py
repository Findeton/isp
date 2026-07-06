#!/usr/bin/env python3
"""
u1_growth_positive_control.py — design note 8 gate G0: the positive control
for the growth-law program.

WHAT THIS RECEIPT ESTABLISHES (pre-registered, note 8 §4 G0): before any
Gibbs(beta) placement law is measured, (i) the paper-12/13 instrument stack
reproduces on this machine/stream, (ii) the trivial-Phi endpoint of the
beta-family — the j3 churn corner (L = 2, continuous content, reset births,
victim = the committing slot) — reproduces paper 16 §4's cell membership at
N = 2048 (three layers: T1 rho, T2 canonical D* vs same-N band, T3 per-draw
interval-dispersion z on a 40-draw ensemble), and (iii) the u2 GROWTH KERNEL
(churn events at rate 1/L per commit, victim chosen UNIFORMLY over live slots
— the beta = 0 endpoint of the victim-selection family) is itself in/near the
cell, so that any beta > 0 effect measured in u2 is attributable to the law
and not to the kernel change (the j2 beta = 0 lesson, note 8 §5 risk 1).

KERNEL EQUIVALENCE NOTE (stated in advance): strict-j3 (victim = committer,
death prob 1/L at own commit) and uniform-victim (churn event prob 1/L per
global commit, victim uniform over M slots) have the SAME mean lifetime in
own-commit units (L), different lifetime laws (geometric in own commits vs
geometric in global commits thinned by the race). Both are memoryless; the
pre-registered expectation is that both sit in the corner's band-adjacent
range (1.2-1.5x per paper 16 §4). A failure here would void u2's Arm B.

Conventions: paper 13's bands and layers; j1's per-draw dispersion z; j3's
40-draw T3 calibration at N = 2048; float64 measurement landscape;
default_rng(20260703). Gates quoted from note 8 §4 / paper 16 §4.
"""

import numpy as np

rng = np.random.default_rng(20260703)

PASS = 0
FAIL = 0

def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    if ok: PASS += 1
    else: FAIL += 1
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))


# ------------------------------------------------------------- instruments
# (j1/j3 verbatim: star discrepancy, rank embedding, tie-aware Spearman,
#  interval-dispersion Fano statistic)

def star_disc(pts):
    N = len(pts)
    us = np.unique(np.concatenate([pts[:, 0], [1.0]]))
    vs = np.unique(np.concatenate([pts[:, 1], [1.0]]))
    order = np.argsort(pts[:, 0], kind="stable")
    pu = pts[order, 0]; pv = pts[order, 1]
    best = 0.0
    for a in us:
        ko = np.searchsorted(pu, a, "left"); kc = np.searchsorted(pu, a, "right")
        so = np.sort(pv[:ko]); sc = np.sort(pv[:kc])
        co = np.searchsorted(so, vs, "left") / N
        cc = np.searchsorted(sc, vs, "right") / N
        vol = a * vs
        best = max(best, float(np.abs(co - vol).max()), float(np.abs(cc - vol).max()))
    return best

def rank_embed2(b, chi):
    N = len(b)
    r1 = np.argsort(np.argsort(b))
    r2 = np.argsort(np.argsort(chi))
    return np.column_stack([(r1 + 0.5) / N, (r2 + 0.5) / N])

def spearman_ties(x, y):
    def avg_rank(v):
        o = np.argsort(v, kind="stable"); r = np.empty(len(v)); r[o] = np.arange(len(v))
        vals, inv = np.unique(v, return_inverse=True)
        sums = np.bincount(inv, weights=r); cnts = np.bincount(inv)
        return (sums / cnts)[inv]
    rx, ry = avg_rank(x), avg_rank(y)
    return float(np.corrcoef(rx, ry)[0, 1])

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

# --------------------------------------------------------------- generators
def web_j3(N, M, L):
    """j3's churn corner verbatim: continuous increments, reset births,
    victim = the committing slot at prob 1/L per own commit."""
    chi_acc = np.zeros(M)
    chi = np.zeros(N); lineage = np.zeros(N, dtype=np.int64)
    lid = np.arange(M).copy(); next_id = M
    mean_c = 0.109551  # mean of the 3-atom menu (route-B scale; kappa drops out
                       # of the rank pipeline — value immaterial, disclosed)
    for t in range(N):
        c = int(rng.integers(M))
        chi_acc[c] += rng.exponential(mean_c)
        chi[t] = chi_acc[c]; lineage[t] = lid[c]
        if rng.random() < 1.0 / L:
            chi_acc[c] = 0.0
            lid[c] = next_id; next_id += 1
    return np.arange(N), chi, lineage

def web_kernel(N, M, L):
    """u2's beta = 0 growth kernel: churn event at prob 1/L per GLOBAL commit,
    victim UNIFORM over live slots, reset birth. Same mean lifetime L in
    own-commit units (a slot commits every M global commits on average and
    dies at rate 1/(L*M) per global commit)."""
    chi_acc = np.zeros(M)
    chi = np.zeros(N); lineage = np.zeros(N, dtype=np.int64)
    born_at = np.zeros(M, dtype=np.int64)      # own-commit counter at birth
    own = np.zeros(M, dtype=np.int64)
    lifetimes = []
    lid = np.arange(M).copy(); next_id = M
    mean_c = 0.109551
    for t in range(N):
        c = int(rng.integers(M))
        chi_acc[c] += rng.exponential(mean_c)
        own[c] += 1
        chi[t] = chi_acc[c]; lineage[t] = lid[c]
        if rng.random() < 1.0 / L:
            v = int(rng.integers(M))           # uniform victim — the kernel
            lifetimes.append(int(own[v] - born_at[v]))
            chi_acc[v] = 0.0
            born_at[v] = own[v]
            lid[v] = next_id; next_id += 1
    return np.arange(N), chi, lineage, lifetimes

def bands(N, nD=20, nF=None):
    fb = [star_disc(rank_embed2(*(lambda p: (p[:, 0], p[:, 1]))(rng.random((N, 2)))))
          for _ in range(nD)]
    out = [float(np.mean(fb)), float(np.std(fb))]
    if nF:
        ens = [interval_fano(np.argsort(np.argsort(p[:, 0])), p[:, 1])
               for p in (rng.random((N, 2)) for _ in range(nF))]
        out += [float(np.mean(ens)), float(np.std(ens)), ens]
    return out


# ------------------------- CHECK 1: instrument reproduction at N = 512
print("CHECK 1: instrument + positive control at N = 512 (fresh stream)")
N, M, L = 512, 32, 2
Df, Dsd = bands(N)[:2]
print(f"      pooled faithful band D*(rank, N = {N}) = {Df:.4f} +/- {Dsd:.4f}")
pts = rng.random((N, 2))
d_ctrl = star_disc(rank_embed2(np.argsort(np.argsort(pts[:, 0])), pts[:, 1]))
ok = d_ctrl < 1.5 * Df and 0.020 < Df < 0.033
check("sprinkling-as-two-clock control at the band; the band itself inside "
      "the corpus range (paper 13's pooled 0.0263 +/- 0.0047)", ok,
      f"D*_ctrl = {d_ctrl:.4f}; band {Df:.4f}")

# ------------------------- CHECK 2: strict-j3 corner reproduces at N = 512
print("CHECK 2: the trivial-Phi endpoint (strict j3 corner, L = 2) at N = 512")
ds, rs = [], []
for _ in range(6):
    b, c, _ = web_j3(N, M, L)
    ds.append(star_disc(rank_embed2(b, c)))
    rs.append(spearman_ties(b, c))
D2c, rho2c = float(np.mean(ds)), float(np.mean(np.abs(rs)))
ok = D2c < 1.7 * Df and rho2c < 0.12
check("corner band-adjacent (paper 16 §4's 1.2-1.5x range, tolerance 1.7x "
      "fresh-stream) and decorrelated (T1)", ok,
      f"D* = {D2c:.4f} ({D2c/Df:.2f}x), |rho| = {rho2c:.3f}")

# ------------------------- CHECK 3: uniform-victim kernel at N = 512
print("CHECK 3: the u2 growth kernel (uniform victim, beta = 0) at N = 512")
ds, rs, all_lt = [], [], []
for _ in range(6):
    b, c, _, lts = web_kernel(N, M, L)
    ds.append(star_disc(rank_embed2(b, c)))
    rs.append(spearman_ties(b, c))
    all_lt += lts
Dk, rhok = float(np.mean(ds)), float(np.mean(np.abs(rs)))
L_eff = float(np.mean(all_lt)) if all_lt else float("nan")
ok = Dk < 1.7 * Df and rhok < 0.12
check("uniform-victim kernel is itself in the corner's range — u2's beta = 0 "
      "baseline is clean (any beta > 0 effect is the law's, not the kernel's)",
      ok, f"D* = {Dk:.4f} ({Dk/Df:.2f}x), |rho| = {rhok:.3f}")
ok = abs(L_eff - L) < 0.7
check("kernel-equivalence: realized mean lifetime (own commits) matches L "
      "(the two churn parameterizations agree in the mean, as derived in "
      "the docstring)", ok, f"L_eff = {L_eff:.2f} vs L = {L}")

# ------------------------- CHECK 4: the three-layer cell test at N = 2048
print("CHECK 4: the full three-layer cell test at N = 2048 (both kernels)")
N2 = 2048
Df2, Dsd2, mu_f, sd_ens, ens = bands(N2, nD=12, nF=40)
print(f"      faithful band D*(N = {N2}) = {Df2:.4f} +/- {Dsd2:.4f}; "
      f"fano ensemble {mu_f:.3f} +/- {sd_ens:.3f} (40 draws)")
rows = {}
for name, gen in (("strict-j3", web_j3), ("uniform-victim", web_kernel)):
    ds, rs, fs = [], [], []
    for _ in range(4):
        out = gen(N2, M, L)
        b, c = out[0], out[1]
        ds.append(star_disc(rank_embed2(b, c)))
        rs.append(spearman_ties(b, c))
        fs.append(interval_fano(b, c))
    D_, rho_, f_ = float(np.mean(ds)), float(np.mean(np.abs(rs))), float(np.mean(fs))
    z_ = abs(f_ - mu_f) / max(sd_ens, 1e-12)
    rows[name] = (D_, rho_, f_, z_)
    print(f"      {name:<16} D* {D_:.4f} ({D_/Df2:.2f}x)  |rho| {rho_:.3f}  "
          f"fano {f_:.3f}  z {z_:.1f}")
ok = all(r[0] < Df2 + 2.5 * Dsd2 + 0.004 and r[1] < 0.1 and r[3] < 3.5
         for r in rows.values())
check("BOTH kernels pass all three layers at N = 2048 (T1 |rho| < 0.1; "
      "T2 D* band-adjacent; T3 per-draw z < 3.5 vs the 40-draw ensemble) — "
      "G0 holds and u2's Arm B is licensed", ok,
      "; ".join(f"{k}: {v[0]/Df2:.2f}x, z={v[3]:.1f}" for k, v in rows.items()))

# ------------------------- verdict
print()
total = PASS + FAIL
if FAIL == 0:
    print(f"ALL CHECKS PASS ({PASS}/{total})")
else:
    print(f"FAILURES: {FAIL}/{total}")
    raise SystemExit(1)
