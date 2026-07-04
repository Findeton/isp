#!/usr/bin/env python3
"""
o1_clicklaw_crossover.py — v8 paper 8 §2: the exact sparse→dense crossover for the
click-law (content axis).

Setting (v8 paper 1 §3.3–3.4): dense seals force S(χ) = exp(−κχ) (Cauchy/Aczél);
sparse seals at lattice L = {kd} force only the geometric skeleton S(kd) = s^k,
s := S(d) = e^{−κd}, with the inter-seal profile FREE. Committed survival is
monotone nonincreasing BY DEFINITION (paper 1 §3.5); the coherence witness between
seals is a different object and is NOT covered here (it may rise transiently —
that freedom is the genuinely-quantum content, paper 1 §3.4 / v6 paper 56).

An ADMISSIBLE profile: S : [0, ∞) → (0, 1], monotone nonincreasing, S(0) = 1,
S(kd) = s^k for all k ≥ 0.

THEOREM 2.1 (uniform crossover bound). For every admissible profile and every χ ≥ 0:
    |log S(χ) + κχ| < κd,     equivalently  e^{−κd} < S(χ)·e^{κχ} < e^{κd}
    (equality approached, never attained off the lattice; ON the lattice the
     deviation is exactly 0).
Proof: χ ∈ [kd, (k+1)d] ⇒ monotonicity + skeleton give S(χ) ∈ [s^{k+1}, s^k],
and e^{−κχ} ∈ [s^{k+1}, s^k]; both lie in an interval of log-width κd. ∎

THEOREM 2.2 (tightness — the freedom's exact diameter). The hold-high profile
S⁺(χ) = s^{⌊χ/d⌋} and hold-low profile S⁻(χ) = s^{⌈χ/d⌉} are admissible and
    sup_χ [log S⁺(χ) + κχ] = κd,   inf_χ [log S⁻(χ) + κχ] = −κd  (suprema, approached).
So the sup-norm radius of the admissible class around the exponential is EXACTLY κd:
the crossover is linear in d with constant exactly 1, two-sided.

COROLLARY 2.3 (per-cell band = paper 1's squeeze). On cell k the allowed S-band has
width s^k(1−s) = B(d)·s^{k}/(s^0)… i.e. exactly the B(d)-squeeze of paper 1 §3.4;
globally |S(χ) − e^{−κχ}| < 1 − s ≤ κd.

COROLLARY 2.4 (detectability / onset density). A measurement resolving log-survival
to ±ε cannot distinguish ANY admissible sparse profile from the dense exponential
iff κd ≤ ε: the forced-shape onset spacing is d* = ε/κ (onset density ρ* = κ/ε).
One-directional care: κd ≤ ε ⇒ indistinguishable (Thm 2.1); κd > ε ⇒ SOME profile
is distinguishable (Thm 2.2), not every profile.

IDENTITY (paper 1 §3.4, re-verified): on the lattice S(d)^{χ/d} = e^{−κχ} for every
d with κ = −log S(d)/d — the dense law is the d → 0 face of the skeleton.

Numerics: mpmath dps = 60 for all asserted values; random profiles are mpmath-built.
Seed: fixed integer (no wall-clock).
"""

import random
from mpmath import mp, mpf, exp, log

mp.dps = 60
random.seed(20260702)

PASS = 0
FAIL = 0

def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    if ok: PASS += 1
    else: FAIL += 1
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))


# ---------------------------------------------------------------- profile kit
def random_admissible_profile(kappa, d, ncells, pts_per_cell):
    """Random monotone profile through the skeleton: within each cell k, a sorted
    batch of uniform-random survival values in [s^{k+1}, s^k].  Returns (chis, Ss)."""
    s = exp(-kappa * d)
    chis, Ss = [mpf(0)], [mpf(1)]
    for k in range(ncells):
        lo, hi = s ** (k + 1), s ** k
        us = sorted(random.random() for _ in range(pts_per_cell))
        for i, u in enumerate(us):
            chi = d * (k + (i + mpf("0.5")) / pts_per_cell)
            S = hi - (hi - lo) * mpf(u)          # decreasing within the cell
            chis.append(chi); Ss.append(S)
        chis.append(d * (k + 1)); Ss.append(lo)  # the lattice point, exact
    return chis, Ss


# ------------------------------------------- 1. skeleton forcing + the identity
print("CHECK 1: the induction step behind the skeleton, and the one-law identity")
import sympy as sp
Ssym = sp.symbols("S", positive=True)
# The forcing argument is paper 1 s3.4's (composition at seals + finite induction);
# what is checkable here is its induction step closing: with S(kd) defined
# recursively by composition, S((k+1)d) = S(kd)*S(d), the closed form is S(d)^k.
ok = True
Sk = sp.Integer(1)
for k in range(1, 61):
    Sk = Sk * Ssym                      # the composition recursion
    if sp.simplify(Sk - Ssym ** k) != 0:
        ok = False
check("composition recursion S((k+1)d) = S(kd)*S(d) closes to S(d)^k, k = 1..60 "
      "[sympy; the forcing premise itself is paper 1 s3.4's]", ok)
chi_s, d_s, kap = sp.symbols("chi d kappa", positive=True)
lhs = sp.exp(-kap * d_s) ** (chi_s / d_s)
ok = sp.simplify(lhs - sp.exp(-kap * chi_s)) == 0
check("S(d)^{chi/d} = e^{-kappa chi} identically (kappa = -log S(d)/d) [sympy]", ok)

# --------------------------------------------------- 2. Theorem 2.1 on profiles
print("CHECK 2: Theorem 2.1 uniform bound on random admissible profiles")
worst_overall = mpf(0)
ok = True
for kappa, d in ((mpf(1), mpf("0.5")), (mpf(1), mpf("0.1")), (mpf(3), mpf("0.25")),
                 (mpf("0.2"), mpf(2)), (mpf(1), mpf("0.01"))):
    for _ in range(40):
        chis, Ss = random_admissible_profile(kappa, d, ncells=30, pts_per_cell=25)
        dev = max(abs(log(S) + kappa * c) for c, S in zip(chis, Ss))
        worst_overall = max(worst_overall, dev / (kappa * d))
        if not dev < kappa * d:
            ok = False
check("sup |log S + kappa chi| < kappa d on 40 random profiles per regime x 5 "
      "(kappa,d) regimes (200 total)",
      ok, f"worst dev/(kappa d) = {float(worst_overall):.6f}")

ok = True
for kappa, d in ((mpf(1), mpf("0.5")), (mpf(3), mpf("0.25"))):
    chis, Ss = random_admissible_profile(kappa, d, 20, 20)
    for c, S in zip(chis, Ss):
        if not abs(log(S * exp(kappa * c))) < kappa * d:
            ok = False
check("two-sided STRICT form: e^{-kd} < S e^{k chi} < e^{kd} pointwise "
      "(lattice points sit at deviation 0)", ok)

# ------------------------------------------------------ 3. Theorem 2.2 tightness
print("CHECK 3: Theorem 2.2 — hold profiles approach +/- kappa d exactly")
kappa, d = mpf(1), mpf("0.4")
s = exp(-kappa * d)
sup_hi = mpf(0); inf_lo = mpf(0)
for k in range(25):
    for j in range(1, 400):
        chi = d * (k + mpf(j) / 400)
        Sp = s ** k          # hold-high on [kd,(k+1)d)
        Sm = s ** (k + 1)    # hold-low on (kd,(k+1)d]
        sup_hi = max(sup_hi, log(Sp) + kappa * chi)
        inf_lo = min(inf_lo, log(Sm) + kappa * chi)
ok = abs(sup_hi - kappa * d * mpf(399) / 400) < mpf(10) ** -50 and \
     abs(inf_lo + kappa * d * mpf(399) / 400) < mpf(10) ** -50
check("hold-high/low deviations reach +/- (399/400) kappa d on the 400-grid "
      "(-> kappa d as the grid refines; sup approached, not attained)", ok,
      f"sup={float(sup_hi):.6f}, kappa d={float(kappa*d):.6f}")
# admissibility of the hold profiles as FUNCTIONS: evaluate S+/- on a fine grid,
# verify monotone nonincreasing pointwise, S(0) = 1, and skeleton hit at every kd.
# Grid points chi_j = j*d/97 are indexed exactly: floor(chi_j/d) = j // 97 and
# ceil(chi_j/d) = (j + 96) // 97 (integer arithmetic — no float floor/ceil artifact)
Q = 97
def S_plus_j(j):
    return s ** (j // Q)

def S_minus_j(j):
    return s ** ((j + Q - 1) // Q)

ok = True
for Sf in (S_plus_j, S_minus_j):
    vals = [Sf(j) for j in range(0, Q * 12 + 1)]
    if vals[0] != 1:
        ok = False
    if any(vals[i] < vals[i + 1] for i in range(len(vals) - 1)):
        ok = False
    for k in range(12):
        if abs(Sf(k * Q) - s ** k) > mpf(10) ** -55:   # the lattice indices j = k*97
            ok = False
check("hold profiles admissible AS FUNCTIONS: S(0)=1, monotone nonincreasing on a "
      "1165-point grid, exact skeleton hit at kd, k = 0..11", ok)

# ------------------------------------------------- 4. Corollary 2.3 per-cell band
print("CHECK 4: Corollary 2.3 — per-cell band width = s^k(1-s), global cap kappa d")
ok = True
for k in range(30):
    width = s ** k - s ** (k + 1)
    if abs(width - s ** k * (1 - s)) > mpf(10) ** -55:
        ok = False
gcap = (1 - s) <= kappa * d
check("band width s^k(1-s) exact for k = 0..29; global |S - exp| < 1-s <= kappa d",
      ok and gcap, f"1-s={float(1-s):.6f} <= kappa d={float(kappa*d):.6f}")

# ------------------------------------------------ 5. Corollary 2.4 onset density
print("CHECK 5: Corollary 2.4 — both directions exercised at the onset spacing")
# Direction 1 (Thm 2.1): at d = 0.9 eps/kappa, EVERY sampled admissible profile
# stays within eps of the exponential. Direction 2 (Thm 2.2): at d = 1.5 eps/kappa,
# the hold-high profile EXCEEDS eps (a distinguishable profile exists).
kap5 = mpf(1)
ok = True
print("      eps        d* = eps/kappa   rho* = 1/d*")
for e10 in (1, 2):
    eps = mpf(10) ** -e10
    dstar = eps / kap5
    print(f"      1e-{e10}      {float(dstar):.4g}          {float(1/dstar):.4g}")
    d_lo = mpf("0.9") * dstar
    for _ in range(20):
        chis, Ss = random_admissible_profile(kap5, d_lo, 12, 12)
        if max(abs(log(S) + kap5 * c) for c, S in zip(chis, Ss)) > eps:
            ok = False                   # would falsify Thm 2.1's direction
    d_hi = mpf("1.5") * dstar
    s_hi = exp(-kap5 * d_hi)
    dev_hold = max(kap5 * (d_hi * (k + mpf(j) / 200) - k * d_hi)
                   for k in range(5) for j in range(1, 200))
    if not dev_hold > eps:
        ok = False                       # would falsify Thm 2.2's direction
check("d = 0.9 d*: all 40 sampled profiles within eps; d = 1.5 d*: the hold "
      "profile exceeds eps — both directions of Cor 2.4 exercised", ok)

# ------------------------------------------------------- 6. dense-limit scaling
print("CHECK 6: dense-limit convergence is linear in d (measured on hold profiles)")
sups = []
for j in range(1, 9):
    dj = mpf(2) ** -j
    sj = exp(-dj)                        # kappa = 1
    # measured sup deviation of the hold-high profile on a 400-per-cell grid
    sup_j = max(log(sj ** k) + (dj * (k + mpf(i) / 400))
                for k in range(8) for i in range(1, 400))
    sups.append(sup_j)
ratios = [sups[i] / sups[i + 1] for i in range(len(sups) - 1)]
ok = all(abs(r - 2) < mpf(10) ** -40 for r in ratios)   # grid factor (399/400) cancels
check("halving d halves the MEASURED hold-profile sup deviation exactly "
      "(slope 1; the common 399/400 grid factor cancels in the ratio)", ok)
# and the mean deviation of RANDOM profiles also scales ~ d (demonstrated, not asserted-exact)
means = []
for j in (2, 4, 6):
    dj = mpf(2) ** -j
    devs = []
    for _ in range(30):
        chis, Ss = random_admissible_profile(mpf(1), dj, 10, 10)
        devs.append(max(abs(log(S) + c) for c, S in zip(chis, Ss)))
    means.append(sum(devs) / len(devs))
r1, r2 = means[0] / means[1], means[1] / means[2]
ok = 3 < r1 < 5 and 3 < r2 < 5          # factor-4 per two octaves = linear
check("random-profile mean deviation scales linearly in d (factor ~4 per 2 octaves)",
      ok, f"ratios {float(r1):.2f}, {float(r2):.2f}")

# --------------------------------------------- 7. per-cell average hazard = kappa
print("CHECK 7: per-cell average hazard is kappa exactly, for EVERY admissible profile")
# cumulative hazard Lambda = -log S; Lambda((k+1)d) - Lambda(kd) = -log s = kappa d
ok = True
for k in range(20):
    if abs((-log(s ** (k + 1))) - (-log(s ** k)) - kappa * d) > mpf(10) ** -55:
        ok = False
check("Lambda((k+1)d) - Lambda(kd) = kappa d identically (profile-independent)", ok)

# ------------------------------------------------------------------- verdict
print()
total = PASS + FAIL
if FAIL == 0:
    print(f"ALL CHECKS PASS ({PASS}/{total})")
else:
    print(f"FAILURES: {FAIL}/{total}")
    raise SystemExit(1)
