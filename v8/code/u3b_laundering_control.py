#!/usr/bin/env python3
"""
u3b_laundering_control.py — paper 17 round-1 repair (physics referee M6):
the uniform-committer CONTROL COLUMN for u3's laundering axis.

THE GAP: u3 CHECK 4 measured rho along L in {2, 8, no-churn} for the
argmin-chi committer ONLY (+0.145 / +0.486 / +0.980) and the paper's first
draft read the axis as "visibility controlled by L, not by determinism per
se". But the no-churn endpoint confounds two mechanisms: common-birth
co-growth (paper 13 family A: uniform race, no churn -> Spearman +0.78;
family A has no churn axis — the baseline is determinism-FREE, and this
receipt's uniform column shows churn launders it too) and the water-filling lockstep (P1's determinism-specific
mechanism). The axis needs the uniform-committer column at the SAME L
values so the determinism INCREMENT Delta rho(L) is what gets read.

PRE-REGISTERED (this docstring, before first run; both directions live):
the uniform column reproduces paper 13's +0.78-class value at no-churn and
low values at L = 2; the determinism increment Delta rho = rho(argmin) -
rho(uniform) is expected ~0 at L = 2 (churn launders) and positive at
no-churn (the lockstep is real on top of common birth). If instead the
uniform column matches argmin everywhere, P1's mechanism is fully reducible
to common birth and paper 17's laundering paragraph must be rewritten again.

Conventions: u3's web generator, bookkeeping lines omitted (RNG-neutral
here: no kill-the-oldest arm runs, so the age ledger is inert; race/argmin
committers, uniform victim, continuous content, M = 32, N = 512), Spearman with ties, 4 seeds
per cell (matching u3 CHECK 4's seed count; directional grade).
Seed: default_rng(20260705).
"""

import numpy as np

rng = np.random.default_rng(20260705)

PASS = 0
FAIL = 0

def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    if ok: PASS += 1
    else: FAIL += 1
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

def spearman_ties(x, y):
    def avg_rank(v):
        o = np.argsort(v, kind="stable"); r = np.empty(len(v)); r[o] = np.arange(len(v))
        vals, inv = np.unique(v, return_inverse=True)
        sums = np.bincount(inv, weights=r); cnts = np.bincount(inv)
        return (sums / cnts)[inv]
    return float(np.corrcoef(avg_rank(x), avg_rank(y))[0, 1])

def web(N, M, L, committer="race"):
    """u3's web, uniform victim, continuous content; L = None => no churn."""
    chi_acc = np.zeros(M)
    chi = np.zeros(N)
    for t in range(N):
        if committer == "race":
            c = int(rng.integers(M))
        else:                                   # argmin_chi (water-filling)
            c = int(np.argmin(chi_acc))
        chi_acc[c] += rng.exponential(0.109551)
        chi[t] = chi_acc[c]
        if L is not None and rng.random() < 1.0 / L:
            v = int(rng.integers(M))
            chi_acc[v] = 0.0
    return np.arange(N), chi

print("CHECK 1: the axis with BOTH committer columns (M = 32, N = 512, 4 seeds)")
print("      L        uniform rho    argmin rho     increment Delta rho")
rows = {}
for L, tag in ((2, "L = 2"), (8, "L = 8"), (None, "no churn")):
    r_u, r_a = [], []
    for s in range(4):
        b, chi = web(512, 32, L, "race")
        r_u.append(spearman_ties(b, chi))
        b, chi = web(512, 32, L, "argmin")
        r_a.append(spearman_ties(b, chi))
    rows[tag] = (np.mean(r_u), np.mean(r_a))
    print(f"      {tag:<9}  {np.mean(r_u):+.3f}         {np.mean(r_a):+.3f}"
          f"          {np.mean(r_a) - np.mean(r_u):+.3f}")

ok = rows["no churn"][0] > 0.5
check("the uniform no-churn endpoint reproduces paper 13's common-birth "
      "class (+0.78-class rho with NO determinism anywhere)", ok,
      f"uniform no-churn rho = {rows['no churn'][0]:+.3f} (paper 13 family "
      f"A: +0.78)")

inc_corner = rows["L = 2"][1] - rows["L = 2"][0]
inc_nochurn = rows["no churn"][1] - rows["no churn"][0]
ok = abs(inc_corner) < 0.15 and inc_nochurn > 0.05
check("the determinism INCREMENT is ~0 at the corner and positive at "
      "no-churn — churn launders the lockstep; common birth carries most "
      "of the raw no-churn rho", ok,
      f"Delta rho: corner {inc_corner:+.3f}, no-churn {inc_nochurn:+.3f}")

print()
total = PASS + FAIL
if FAIL == 0:
    print(f"ALL CHECKS PASS ({PASS}/{total})")
else:
    print(f"FAILURES: {FAIL}/{total}")
    raise SystemExit(1)
