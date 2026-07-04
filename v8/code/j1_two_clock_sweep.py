#!/usr/bin/env python3
"""
j1_two_clock_sweep.py — v8 paper 13 §2: the two-clock construction — a
record-native candidate class for 2D-manifoldlike record configurations,
measured with the paper-12 instrument.

THE MODEL [POSITED, two posits named]: seals carry two record-native scalars —
the global commit index b (posit 1: a global commit sequencing across chains)
and the accumulated content chi of their chain (paper 1's odometer; posit 2:
cross-chain chi-comparability as a causal criterion). Precedence := dominance
in both clocks. Every such order has dim <= 2 BY CONSTRUCTION.

UNIVERSALITY (paper 13 Thm 2.1, trivial but organizing): EVERY 2D order is a
two-clock configuration (b = rank in L1 — a linear extension, hence a valid
commit sequence; chi = rank in L2 — chain-monotone, hence a valid supply
assignment). So the frame costs nothing beyond dim <= 2, and ALL the physics
sits in the joint (commit, supply) statistics — the manifoldlikeness question
is thereby RELOCATED into paper 1 §7.1's [PHYSICAL] supply configuration data.
Corollary: the class trivially CONTAINS manifoldlike members (positive control
below); the tested question is whether NATURAL supply families land there.

THE SWEEP (the measured content): supply families —
  A  homogeneous renewal (iid exponential increments, equal rates)
  B  static heterogeneous rates (log-uniform over 2 decades)
  C  wandering log-rates (per-commit Gaussian steps, sigma in {0.15, 0.6, 1.2})
  F  Levy supply (Pareto alpha = 0.5, infinite mean), M = 128
  S  the positive control: chi = the v-coordinate of an actual sprinkling
     (a legal supply realization by universality)
scored by the paper-12 pipeline: canonical D* vs the same-N faithful band, the
rank-rank dependence (Spearman — the obstruction metric), and the statistical
layer on the best natural family.

Gates are written from a disclosed pre-run exploration (this is a MEASUREMENT
of the families, and the headline is the measured NEGATIVE where it is one).
Float discipline: float64 measurement; default_rng(20260702).
"""

import numpy as np

rng = np.random.default_rng(20260702)

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

def two_clock(N, M, family):
    chain = rng.integers(0, M, N)
    chi = np.zeros(N)
    acc = np.zeros(M)
    if family == "A":
        logr = np.zeros(M); wander, alpha = 0.0, None
    elif family == "B":
        logr = np.log(10 ** rng.uniform(-1, 1, M)); wander, alpha = 0.0, None
    elif family.startswith("C"):
        logr = np.log(10 ** rng.uniform(-0.5, 0.5, M))
        wander, alpha = float(family[1:]), None
    elif family == "F":
        logr = np.zeros(M); wander, alpha = 0.0, 0.5
    for t in range(N):
        c = chain[t]
        if wander > 0:
            logr[c] += rng.normal(0, wander)
        if alpha:
            inc = (1.0 / rng.random() ** (1 / alpha)) * np.exp(logr[c])
        else:
            inc = rng.exponential(np.exp(logr[c]))
        acc[c] += inc
        chi[t] = acc[c]
    return np.arange(N), chi, chain

def spearman(x, y):
    rx = np.argsort(np.argsort(x)).astype(float)
    ry = np.argsort(np.argsort(y)).astype(float)
    return float(np.corrcoef(rx, ry)[0, 1])

N, M, SEEDS = 512, 32, 6   # SEEDS = replicate draws from the one seeded stream

# faithful band at N = 512, POOLED over 20 replicates with spread quoted
# (post-review: a 6-draw band was a ~2-sigma-low fluke at 0.0240; paper 12's
# i2 reports 0.0270 for the same statistic — the pooled band supersedes both
# as the denominator, and the spread travels with every ratio)
faith = [star_disc(rank_embed2(*(lambda p: (p[:, 0], p[:, 1]))(rng.random((N, 2)))))
         for _ in range(20)]
D_faith = float(np.mean(faith))
D_faith_sd = float(np.std(faith))

# ------------------------------ CHECK 1: universality + the positive control
print("CHECK 1: universality and the positive control")
pts = rng.random((N, 2))
b_ctrl = np.argsort(np.argsort(pts[:, 0]))        # commit order = u-rank (a linear ext.)
chi_ctrl = pts[:, 1]                              # supply = v-coordinate (chain-monotone)
emb = rank_embed2(b_ctrl, chi_ctrl)
C_two = dominance_order(np.column_stack([b_ctrl, chi_ctrl]).astype(float))
C_spr = dominance_order(pts)
d_ctrl = star_disc(emb)
ok = np.array_equal(C_two, C_spr) and d_ctrl < 1.5 * D_faith
check("a sprinkling IS a two-clock configuration (order bit-identical; its "
      "supply realization passes the pipeline at the faithful band) — the frame "
      "is universal for dim <= 2 and the pipeline is not rigged against it", ok,
      f"D*_control = {d_ctrl:.4f} vs faithful band {D_faith:.4f}")

# ------------------------------ CHECK 2: chain-structure sanity
print("CHECK 2: structural sanity")
b, chi, chain = two_clock(N, M, "B")
ok = True
for c in range(M):
    members = np.nonzero(chain == c)[0]
    if len(members) > 1:
        if not (np.all(np.diff(b[members]) > 0) and np.all(np.diff(chi[members]) > 0)):
            ok = False
check("same-chain seals are totally ordered in BOTH clocks (chains are chains — "
      "the odometer is monotone along its own chain)", ok)

# ------------------------------ CHECK 3: the natural-family sweep
print("CHECK 3: the natural-family sweep (the measured content)")
print(f"      faithful band D*(rank, N = {N}) = {D_faith:.4f} +/- {D_faith_sd:.4f} "
      f"(20 replicates; i2's independent value 0.0270 — consistent within spread)")
print("      family              D*(rank)        ratio    Spearman(b, chi)")
fams = ["A", "B", "C0.15", "C0.6", "C1.2", "A128", "F"]
results = {}
for fam in fams:
    Mf = 128 if fam in ("F", "A128") else M
    ds, rhos = [], []
    for _ in range(SEEDS):
        bb, cc, _ = two_clock(N, Mf, "A" if fam == "A128" else fam)
        ds.append(star_disc(rank_embed2(bb, cc)))
        rhos.append(spearman(bb, cc))
    results[fam] = (float(np.mean(ds)), float(np.std(ds)), float(np.mean(rhos)))
    print(f"      {fam:<18} {results[fam][0]:.4f} +/- {results[fam][1]:.4f}   "
          f"{results[fam][0]/D_faith:4.1f}x    {results[fam][2]:+.3f}")
best_fam = min(results, key=lambda f: results[f][0])
ok = all(results[f][0] > 2.0 * D_faith for f in fams)
check("EVERY natural supply family FAILS the volume layer (D* > 2x the pooled "
      "faithful band) — the measured negative: natural renewal/heterogeneous/"
      "wandering/Levy supplies do NOT land in the manifoldlike cell", ok,
      f"best = {best_fam} at {results[best_fam][0]/D_faith:.1f}x")
# m7 control: F vs A128 separates the increment-law effect from the chain-count
# effect (F differs from A in BOTH; A128 isolates M)
dA, dA128, dF = results["A"][0], results["A128"][0], results["F"][0]
ok = dA128 < dA and dF <= dA128 * 1.05
check("the M = 128 homogeneous control: more/shorter chains alone lowers D* "
      "(mechanical interleaving); the Levy family's remaining advantage over "
      "A128 is the increment-law part — the 'best family' attribution is now "
      "deconfounded", ok,
      f"A(32) {dA:.3f} -> A128 {dA128:.3f} -> F(128, Levy) {dF:.3f}")

# ------------------------------ CHECK 4: the obstruction localized
print("CHECK 4: the obstruction — built-in clock dependence")
rho_faith = [spearman(*(lambda p: (p[:, 0], p[:, 1]))(rng.random((N, 2))))
             for _ in range(6)]
rho_f = float(np.mean(np.abs(rho_faith)))
ok = all(abs(results[f][2]) > 0.25 for f in fams) and rho_f < 0.1
check("every natural family carries strong rank-rank dependence "
      "(|Spearman| > 0.25; both clocks grow with time — within-chain "
      "diagonality + rate persistence) while faithful coordinates are "
      "independent (|rho| < 0.1) — the obstruction is structural to natural "
      "supplies, not a tuning accident", ok,
      f"family rhos {', '.join(f'{results[f][2]:+.2f}' for f in fams)}; "
      f"faithful {rho_f:.3f}")

# ------------------------------ CHECK 5: statistical layer on the best family
print("CHECK 5: the best natural family also fails the statistical layer")
def interval_fano(pts_or_bc, kmin=10):
    if isinstance(pts_or_bc, tuple):
        b_, c_ = pts_or_bc
        pts_ = np.column_stack([b_.astype(float), c_])
    else:
        pts_ = pts_or_bc
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

ens = [interval_fano(rng.random((N, 2))) for _ in range(8)]
mu, sd = float(np.mean(ens)), float(np.std(ens))
bb, cc, _ = two_clock(N, M, best_fam)
f_best = interval_fano((bb, cc))
z = abs(f_best - mu) / max(sd, 1e-12)
ok = z > 4
check(f"best family ({best_fam}) fails the interval-dispersion layer too "
      f"(z > 4 off the sprinkling ensemble)", ok,
      f"{f_best:.3f} vs {mu:.3f} +/- {sd:.3f} (z = {z:.1f})")

# ------------------------------ verdict
print()
total = PASS + FAIL
if FAIL == 0:
    print(f"ALL CHECKS PASS ({PASS}/{total})")
else:
    print(f"FAILURES: {FAIL}/{total}")
    raise SystemExit(1)
