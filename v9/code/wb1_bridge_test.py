#!/usr/bin/env python3
"""
wb1_bridge_test.py — v9 round 18: the w <-> chi_AB BRIDGE TEST at the
constructible grade (note-wb1; pins committed BEFORE this receipt).

One grown web (ml2 construction verbatim, (N, M, L) = (2048, 32, 16),
dominance order on (b, chi)); over the SAME chain fleet:
  W_ij     = cross-comparability fraction (the k3/l2/m1 W-port formula)
  chi^_ij  = Hasse-GFF exact cross-chain covariance (ml2 verbatim)
The posited identification (v8 papers 14/15, [POSITED] unbuilt) predicts
positive monotone association.  Grade: chi^ is ml2-class (Hasse-GFF
import), NOT the GW field — disclosed.

PINNED (note-wb1 SS2; seeds 20260734-36, primary first; Spearman over
off-diagonal upper triangle; nulls = 24 chain-relabeling perms):
  Gw1  primary: rho > 0, z >= 3.  REFUSED => BRIDGE-REFUTED (this grade).
  Gw2  3/3 seeds: rho > 0, z >= 2.
  Gw3  CONFOUND CONTROL: rank-partial Spearman given the supply
       surrogate (n3-derived verbatim) > 0 with partial-z >= 2 on >= 2/3
       seeds incl. primary.  Gw1 holds + Gw3 refuses => CONFOUNDED.
All hold => BRIDGE-SUPPORTED [DEMONSTRATED given the Hasse-GFF import].
INFO: supply-alone associations; Mc per seed.  Exit 1 by design.
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

def spearman(x, y):
    rx, ry = ranks(x), ranks(y)
    return float(np.corrcoef(rx, ry)[0, 1])

def partial_spearman(x, y, z):
    """Rank-partial: residualize ranks of x and y on [ranks(z), 1]."""
    rx, ry, rz = ranks(x), ranks(y), ranks(z)
    F = np.column_stack([rz, np.ones(len(rz))])
    bx, *_ = np.linalg.lstsq(F, rx, rcond=None)
    by, *_ = np.linalg.lstsq(F, ry, rcond=None)
    ex, ey = rx - F @ bx, ry - F @ by
    return float(np.corrcoef(ex, ey)[0, 1])

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
    # the dominance order and the two matrices over the SAME fleet
    C = (b[None, :] > b[:, None]) & (chi[None, :] > chi[:, None])
    K = (C | C.T).astype(np.float64)          # comparability
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
    # supply surrogate (n3-derived verbatim)
    levels = np.array([chi[v].mean() for v in chains])
    births = np.array([birth[k] for k in keys], dtype=float)
    def norm01(Mx):
        lo, hi = Mx.min(), Mx.max()
        return (Mx - lo) / (hi - lo + 1e-30)
    sur = (norm01(np.outer(levels, levels))
           + norm01(np.exp(-np.abs(births[:, None] - births[None, :]) / (2048 / 4))))
    iu = np.triu_indices(Mc, 1)
    w, x, s = W[iu], chi_AB[iu], sur[iu]
    rho = spearman(w, x)
    prho = partial_spearman(w, x, s)
    # chain-relabeling nulls (chi^ relabeled against fixed W)
    nr, npr = [], []
    for _ in range(24):
        pr = rng.permutation(Mc)
        xp = chi_AB[np.ix_(pr, pr)][iu]
        nr.append(spearman(w, xp))
        npr.append(partial_spearman(w, xp, s))
    z = (rho - np.mean(nr)) / max(np.std(nr, ddof=1), 1e-12)
    pz = (prho - np.mean(npr)) / max(np.std(npr, ddof=1), 1e-12)
    return dict(Mc=Mc, rho=rho, z=float(z), prho=prho, pz=float(pz),
                sw=spearman(s, w), sx=spearman(s, x))

SEEDS = [20260734, 20260735, 20260736]
print("[wb1: the w <-> chi_AB bridge test — order-derived W vs Hasse-GFF chi^]")
rows = [run_seed(sd) for sd in SEEDS]
for sd, r in zip(SEEDS, rows):
    print(f"      seed {sd}: Mc = {r['Mc']}, rho = {r['rho']:+.3f} (z {r['z']:.1f}), "
          f"partial rho = {r['prho']:+.3f} (z {r['pz']:.1f});  "
          f"INFO supply: rho(sur, W) = {r['sw']:+.3f}, rho(sur, chi^) = {r['sx']:+.3f}")

r0 = rows[0]
gw1 = r0['rho'] > 0 and r0['z'] >= 3
check("Gw1 (association, primary seed): Spearman(W, chi^) > 0 with "
      "null-z >= 3 [directional: positive]", gw1,
      f"rho {r0['rho']:+.3f}, z {r0['z']:.1f}")
gw2 = all(r['rho'] > 0 and r['z'] >= 2 for r in rows)
check("Gw2 (robustness): rho > 0 and z >= 2 on 3/3 seeds", gw2)
n3 = sum(1 for r in rows if r['prho'] > 0 and r['pz'] >= 2)
gw3 = n3 >= 2 and rows[0]['prho'] > 0 and rows[0]['pz'] >= 2
check("Gw3 (the confound control): rank-partial Spearman given the "
      "supply surrogate > 0 with partial-z >= 2 on >= 2/3 seeds "
      "including the primary", gw3, f"{n3}/3 (primary pz {r0['pz']:.1f})")

if gw1 and gw2 and gw3:
    verdict = ("BRIDGE-SUPPORTED [DEMONSTRATED given the Hasse-GFF import] "
               "— the W-port is licensed for ml2-class fields")
elif not gw1:
    verdict = "BRIDGE-REFUTED at this grade (the posited rung falls)"
elif gw1 and not gw3:
    verdict = "CONFOUNDED (supply owns both — the n3-derived diagnosis extends)"
else:
    verdict = "PARTIAL (primary holds, robustness refused)"
print(f"      VERDICT: {verdict}")

print()
print(f"PRE-REGISTERED GATE LEDGER: "
      f"{'ALL HELD' if FAIL == 0 else 'REFUSALS PRESENT'} — Gw1 primary; "
      f"Gw2 seeds; Gw3 confound; verdict: {verdict}")
print()
total = PASS + FAIL
print(f"ALL CHECKS PASS ({PASS}/{total})" if FAIL == 0 else f"FAILURES: {FAIL}/{total}")
if FAIL: raise SystemExit(1)
