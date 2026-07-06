#!/usr/bin/env python3
"""
t31_irreducibility_exhibits.py — v9 round 2, T3.1's boundary exhibits
(note-t31; gates pinned here pre-run). Three stacks, two gates:

  MARGINAL gate: KS distance of the empirical gap law from Exp(1).
  TWO-TIME gate: serial structure of successive gaps (Spearman rank
  correlation of (g_t, g_{t+1}) plus a 4x4 binned chi-square vs the
  product law) — the conditional-law discriminator of note-t31 §4.

EXHIBITS & PRE-REGISTERED GATES:
  E1 (Weyl stack, zero randomness): g_t = F^{-1}(frac(t*phi)).
      marginal KS -> SMALL (< 0.02 at T = 20000: equidistribution) BUT
      two-time gate fails at huge significance (|rho| > 0.2 or chi2 z > 10)
      — the marginal reading cannot close leg (i); the conditional can.
  E2 (atomic stack, m = 3): gaps drawn deterministically-cyclically from a
      3-value menu shaped to mimic Exp(1) moments. marginal KS >= 1/(2m) =
      0.167 (the leg-(ii) floor; gate: measured KS within [floor, 1] and
      >= floor - 0.01).
  E3 (relocation stack, w > 0): g_t = F^{-1}(U_t) with U_t fresh uniform
      (the leg-(iii) construction realizing the law exactly): BOTH gates
      pass (marginal KS < 0.02 at T = 20000; |rho| < 0.03; chi2 z < 3).

  E4 (quadratic Weyl, the REVIEW's counterexample, adopted): g_t =
      F^{-1}(frac(t^2 * phi)) — deterministic, zero randomness — passes BOTH
      gates (Weyl: t^2*phi equidistributes jointly with its successor), so
      the two-time gate does NOT close leg (i) either: it extends the
      marginal boundary one order, and degree-k Weyl stacks defeat k-time
      batteries — the undecidability persists for every fixed finite test
      battery (note-t31 §3's thesis, strengthened). Gate: E4 passes the E3
      criteria (that is the exhibit).

Precision: pure float64 throughout (phi = (1+sqrt 5)/2 in double; adequate
for equidistribution reads at T = 2e4 — the earlier docstring's dps-40
claim was wrong and is corrected); default_rng(20260706).
"""

import numpy as np
from math import sqrt, log

rng = np.random.default_rng(20260706)

PASS = 0
FAIL = 0

def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    if ok: PASS += 1
    else: FAIL += 1
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

def ks_exp(g):
    g = np.sort(g)
    n = len(g)
    F = 1.0 - np.exp(-g)
    lo = np.max(np.abs(F - np.arange(1, n + 1) / n))
    hi = np.max(np.abs(F - np.arange(0, n) / n))
    return float(max(lo, hi))

def two_time(g):
    a, b = g[:-1], g[1:]
    ra = np.argsort(np.argsort(a)); rb = np.argsort(np.argsort(b))
    rho = float(np.corrcoef(ra, rb)[0, 1])
    qa = np.quantile(a, [0.25, 0.5, 0.75]); qb = np.quantile(b, [0.25, 0.5, 0.75])
    ia = np.digitize(a, qa); ib = np.digitize(b, qb)
    obs = np.zeros((4, 4))
    for x, y in zip(ia, ib):
        obs[x, y] += 1
    exp = obs.sum() / 16.0
    chi2 = float(((obs - exp) ** 2 / exp).sum())
    z = (chi2 - 9) / sqrt(18.0)          # chi2_9 ref: mean 9, var 18
    return rho, z

T = 20000

print("E1: the Weyl stack (deterministic, infinite state)")
phi = (1 + sqrt(5)) / 2
u = np.mod(np.arange(1, T + 1) * phi, 1.0)
g1 = -np.log(1.0 - u)
ks1 = ks_exp(g1)
rho1, z1 = two_time(g1)
check("marginal KS < 0.02 — the empirical gap law equidistributes to "
      "Exp(1): a ZERO-RANDOMNESS stack passes any marginal gate "
      "asymptotically (leg (i) is unfalsifiable by marginals)", ks1 < 0.02,
      f"KS = {ks1:.4f} at T = {T}")
check("two-time gate FAILS at huge significance for THIS (gap-autonomous) "
      "stack — successive gaps sit on a curve; the gate decides the "
      "linear-Weyl/fixed-menu candidate class, NOT the zero-randomness "
      "class (see E4)",
      abs(rho1) > 0.2 or z1 > 10, f"serial rho = {rho1:+.3f}, chi2 z = {z1:.1f}")

print("E2: the atomic stack (m = 3 menu, deterministic cycling)")
menu = np.array([0.2231, 0.6931, 2.3026])       # ~Exp(1)-ish quantile trio
g2 = np.tile(menu, T // 3 + 1)[:T]
ks2 = ks_exp(g2)
floor = 1.0 / 6.0
check("marginal KS sits at-or-above the leg-(ii) floor 1/(2m) = 0.167 — "
      "finite alphabets cannot make a continuum (the quantitative no-go)",
      ks2 >= floor - 0.01, f"KS = {ks2:.4f} vs floor {floor:.3f}")

print("E3: the relocation stack (w > 0 continuous channel, inverse-CDF)")
g3 = -np.log(1.0 - rng.random(T))
ks3 = ks_exp(g3)
rho3, z3 = two_time(g3)
check("both gates PASS — a deterministic-given-contents stack consuming "
      "one continuous channel realizes the law exactly (leg (iii): "
      "relocation, not removal; the randomness is conserved)",
      ks3 < 0.02 and abs(rho3) < 0.03 and z3 < 3,
      f"KS = {ks3:.4f}, serial rho = {rho3:+.3f}, chi2 z = {z3:.1f}")

print("E4: the quadratic Weyl stack (the review's counterexample, adopted)")
u4 = np.mod(np.arange(1, T + 1).astype(float) ** 2 * phi, 1.0)
g4 = -np.log(1.0 - np.clip(u4, 1e-15, 1 - 1e-15))
ks4 = ks_exp(g4)
rho4, z4 = two_time(g4)
check("the quadratic Weyl stack passes BOTH gates — zero randomness, "
      "marginal-clean AND two-time-clean: no fixed finite battery closes "
      "leg (i); the two-time gate extends the boundary exactly one order "
      "(degree-k defeats k-time) — u5 decides the named corpus candidate "
      "stacks, not the class question",
      ks4 < 0.02 and abs(rho4) < 0.03 and z4 < 3,
      f"KS = {ks4:.4f}, serial rho = {rho4:+.3f}, chi2 z = {z4:.1f}")

print()
total = PASS + FAIL
if FAIL == 0:
    print(f"ALL CHECKS PASS ({PASS}/{total})")
else:
    print(f"FAILURES: {FAIL}/{total}")
    raise SystemExit(1)
