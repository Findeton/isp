#!/usr/bin/env python3
"""
wb2_contemporaries.py — v9 round 19: THE CONTEMPORARIES TEST (note-wb2;
pin committed at 3ce7fc3 strictly before this receipt).

wb1 construction verbatim; NEW: the strong-overlap restriction (lifespan
intersection > 50% of the shorter lifespan — the referee definition,
pinned) and the 2-regressor rank-partial (levels-outer + birth-affinity
as separate regressors).  FRESH seeds 20260737-39 (the referee scouting
ran on wb1's seeds; those numbers have no vote here).

PINNED (note-wb2 SS2):
  Gv1 [directional] strong-overlap partial rho_r > 0 on 3/3.
  Gv2 Stouffer-combined null-z >= 3 (24 chain-relabel perms/seed).
  Gv3 rho_r(strong) > rho_r(complement) on 3/3 (the mechanism's signature).
  Gv4 placebo (supply-fit + permuted residuals) |z| < 2 on primary.
All => BRIDGE-SUPPORTED-RESTRICTED [DEMONSTRATED given the Hasse-GFF
import; contemporaneous regime]; >= 2/3 negative on Gv1 =>
REFUTED-AT-GRADE; else UNDETERMINED.  Exit 1 by design on refusal.
"""
import numpy as np

PASS = FAIL = 0
def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    if ok: PASS += 1
    else: FAIL += 1
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

def ranks(x):
    return np.argsort(np.argsort(x)).astype(float)

def partial2(w, x, f1, f2):
    """2-regressor rank-partial: residualize ranks of w and x on
    [ranks(f1), ranks(f2), 1]; Pearson of residuals."""
    F = np.column_stack([ranks(f1), ranks(f2), np.ones(len(w))])
    rw, rx = ranks(w), ranks(x)
    bw, *_ = np.linalg.lstsq(F, rw, rcond=None)
    bx, *_ = np.linalg.lstsq(F, rx, rcond=None)
    ew, ex = rw - F @ bw, rx - F @ bx
    return float(np.corrcoef(ew, ex)[0, 1])

def run_seed(sd):
    rng = np.random.default_rng(sd)
    N, M, L = 2048, 32, 16
    chi_acc = np.zeros(M)
    segs = {}; gen = np.zeros(M, dtype=int); birth = {}
    for m in range(M): segs[(m, 0)] = []; birth[(m, 0)] = 0
    chi = np.zeros(N)
    for t in range(N):
        c = int(rng.integers(M))
        chi_acc[c] += rng.exponential(0.109551)
        chi[t] = chi_acc[c]
        segs[(c, gen[c])].append(t)
        if rng.random() < 1.0 / L:
            v = int(rng.integers(M))
            chi_acc[v] = 0.0; gen[v] += 1
            segs[(v, gen[v])] = []; birth[(v, gen[v])] = t
    keys = [k for k, v in segs.items() if len(v) >= 8]
    chains = [segs[k] for k in keys]
    Mc = len(chains)
    b = np.arange(N)
    C = (b[None, :] > b[:, None]) & (chi[None, :] > chi[:, None])
    K = (C | C.T).astype(np.float64)
    Cf = C.astype(np.float32)
    btw = np.rint(Cf @ Cf).astype(np.int32)
    Hasse = C & (btw == 0)
    A_g = (Hasse | Hasse.T).astype(np.float64)
    Lg = np.diag(A_g.sum(1)) - A_g
    Cov = np.linalg.inv(Lg + 0.1 * np.eye(N))
    W = np.zeros((Mc, Mc)); chi_AB = np.zeros((Mc, Mc))
    for i in range(Mc):
        for j in range(Mc):
            if i != j:
                W[i, j] = K[np.ix_(chains[i], chains[j])].mean()
                chi_AB[i, j] = Cov[np.ix_(chains[i], chains[j])].mean()
    levels = np.array([chi[v].mean() for v in chains])
    births = np.array([birth[k] for k in keys], dtype=float)
    lo = np.array([min(v) for v in chains], dtype=float)
    hi = np.array([max(v) for v in chains], dtype=float)
    # the strong-overlap pair mask (pinned: > 50% of the shorter lifespan)
    ov = np.minimum(hi[:, None], hi[None, :]) - np.maximum(lo[:, None], lo[None, :])
    shorter = np.minimum(hi[:, None] - lo[:, None], hi[None, :] - lo[None, :])
    strong = ov > 0.5 * shorter
    iu = np.triu_indices(Mc, 1)
    sel = strong[iu]
    lev_f = np.outer(levels, levels)[iu]
    bir_f = np.exp(-np.abs(births[:, None] - births[None, :]) / (2048 / 4))[iu]
    w, x = W[iu], chi_AB[iu]

    def restricted_partial(xvec, mask):
        return partial2(w[mask], xvec[mask], lev_f[mask], bir_f[mask])

    rho_s = restricted_partial(x, sel)
    rho_c = restricted_partial(x, ~sel)
    # null: chain-relabeled chi^ through the SAME restricted pipeline
    nulls = []
    for _ in range(24):
        pr = rng.permutation(Mc)
        xp = chi_AB[np.ix_(pr, pr)][iu]
        nulls.append(restricted_partial(xp, sel))
    z = (rho_s - np.mean(nulls)) / max(np.std(nulls, ddof=1), 1e-12)
    # placebo: supply-fit + permuted residuals as the fake field
    F = np.column_stack([lev_f, bir_f, np.ones(len(w))])
    cf, *_ = np.linalg.lstsq(F, x, rcond=None)
    resid = x - F @ cf
    fake = F @ cf + rng.permutation(resid)
    rho_p = restricted_partial(fake, sel)
    nullp = []
    for _ in range(24):
        pr = rng.permutation(Mc)
        Fk = np.zeros((Mc, Mc)); Fk[iu] = fake; Fk = Fk + Fk.T
        fp = Fk[np.ix_(pr, pr)][iu]
        nullp.append(restricted_partial(fp, sel))
    zp = (rho_p - np.mean(nullp)) / max(np.std(nullp, ddof=1), 1e-12)
    return dict(Mc=Mc, npair=int(sel.sum()), frac=float(sel.mean()),
                rho_s=rho_s, rho_c=rho_c, z=float(z), zp=float(zp))

SEEDS = [20260737, 20260738, 20260739]
print("[wb2: the contemporaries test — the bridge in the instrument-native regime]")
rows = [run_seed(sd) for sd in SEEDS]
for sd, r in zip(SEEDS, rows):
    print(f"      seed {sd}: Mc = {r['Mc']}, strong-overlap pairs {r['npair']} "
          f"({100*r['frac']:.0f}%); partial rho_s = {r['rho_s']:+.3f} (z {r['z']:.1f}); "
          f"complement rho_c = {r['rho_c']:+.3f}; placebo z {r['zp']:+.1f}")

gv1 = all(r['rho_s'] > 0 for r in rows)
check("Gv1 [directional]: strong-overlap 2-reg partial > 0 on 3/3 fresh seeds",
      gv1, " / ".join(f"{r['rho_s']:+.3f}" for r in rows))
zc = sum(r['z'] for r in rows) / np.sqrt(3)
check("Gv2 (evidence): Stouffer-combined null-z >= 3", zc >= 3, f"z_comb = {zc:.1f}")
gv3 = all(r['rho_s'] > r['rho_c'] for r in rows)
check("Gv3 (the mechanism's signature): restricted > complement on 3/3", gv3,
      " / ".join(f"{r['rho_s']:+.3f}>{r['rho_c']:+.3f}" for r in rows))
gv4 = abs(rows[0]['zp']) < 2
check("Gv4 (placebo): supply-fit + permuted-residual fake reads |z| < 2 "
      "on the primary", gv4, f"zp = {rows[0]['zp']:+.1f}")

neg = sum(1 for r in rows if r['rho_s'] <= 0)
if gv1 and zc >= 3 and gv3 and gv4:
    verdict = ("BRIDGE-SUPPORTED-RESTRICTED [DEMONSTRATED given the "
               "Hasse-GFF import; contemporaneous regime] — the W-port's "
               "first supported form")
elif neg >= 2:
    verdict = "REFUTED-AT-GRADE (the rung falls in its native regime)"
else:
    verdict = "UNDETERMINED (named power fix: more seeds / larger fleets)"
print(f"      VERDICT: {verdict}")

print()
print(f"PRE-REGISTERED GATE LEDGER: "
      f"{'ALL HELD' if FAIL == 0 else 'REFUSALS PRESENT'} — Gv1–Gv4; "
      f"verdict: {verdict}")
print()
total = PASS + FAIL
print(f"ALL CHECKS PASS ({PASS}/{total})" if FAIL == 0 else f"FAILURES: {FAIL}/{total}")
if FAIL: raise SystemExit(1)
