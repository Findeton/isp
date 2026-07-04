#!/usr/bin/env python3
"""
e2_quarter_law_analog.py — v8 paper 10 §3: the quarter-law analog-validation
protocol (-ln BC = sigma/4) in an engineered open system.

Paper 6 §1: the quarter law is a THEOREM about the which-path pair's own two
divergences (-ln BC = D_B, sigma = D_KL, ratio -> 1/4 in the weak/dense limit,
exact running kappa(eps) on the symmetric binary recorder, exact 1/4 at all
strengths on the Gaussian recorder); its application to physical seals rides the
[POSITED] seal-is-record bridge. An ENGINEERED system can instantiate the bridge
BY CONSTRUCTION: build a recorder whose forward/reverse (arrow) pair IS its
which-path pair. Then both sides are independently measurable — visibility
interferometrically, sigma by forward/reverse sampling — and the ratio is a
near-term falsifiable test of the seal-decoherence structure.

This receipt: (1) re-derives the closed forms and the running series sympy-exact
against paper 6's anchors; (2) simulates the finite-shot protocol and its
estimator distribution; (3) prices the 1/4-vs-1 discrimination (the old equality
conjecture / the JSD complementarity value) in shots; (4) budgets the leading
systematic (extraneous dephasing inflates -ln V); (5) shows the protocol DETECTS
a broken bridge (mismatched arrow/which-path pairs pull kappa off the curve).

Falsification logic (paper 10 §3 text, arithmetic here): in the engineered
system a measured kappa off the running curve indicts the engineering match (the
theorem is unconditional given the match); in a NATURAL seal system it would
falsify the [POSITED] bridge — that asymmetry is the point of the analog test.

Precision: closed forms/series sympy-exact + mpmath dps = 60; the shot-noise
Monte Carlo is float64 (a measurement). Seed: default_rng(20260702).
"""

import numpy as np
import sympy as sp
from mpmath import mp, mpf, log as mplog, atanh, sqrt as mpsqrt

mp.dps = 60
rng = np.random.default_rng(20260702)

PASS = 0
FAIL = 0

def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    if ok: PASS += 1
    else: FAIL += 1
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))


# ------------------------------------------- CHECK 1: closed forms + series
print("CHECK 1: closed forms and the running series (sympy-exact, paper 6 anchors)")
e = sp.symbols("epsilon", positive=True)
P0 = [sp.Rational(1, 2) + e, sp.Rational(1, 2) - e]
P1 = [sp.Rational(1, 2) - e, sp.Rational(1, 2) + e]
BC = sum(sp.sqrt(p * q) for p, q in zip(P0, P1))
DB = -sp.log(BC)
DKL = sum(p * sp.log(p / q) for p, q in zip(P0, P1))
ok = sp.simplify(BC - sp.sqrt(1 - 4 * e ** 2)) == 0
check("BC = sqrt(1 - 4 eps^2)", ok)
ok = sp.simplify(DB + sp.Rational(1, 2) * sp.log(1 - 4 * e ** 2)) == 0
check("D_B = -(1/2) log(1 - 4 eps^2)", ok)
diff = sp.expand_log(DKL - (4 * e * sp.atanh(2 * e)).rewrite(sp.log), force=True)
# put all logs on the common basis {log(1/2 - eps), log(1/2 + eps), log 2}:
half = sp.Rational(1, 2)
diff = diff.subs({sp.log(1 - 2 * e): sp.log(2) + sp.log(half - e),
                  sp.log(2 * e + 1): sp.log(2) + sp.log(half + e)})
ok = sp.simplify(sp.expand(diff)) == 0
check("D_KL = 4 eps atanh(2 eps) (log basis {log(1/2 -+ eps), log 2}; "
      "domain 0 < eps < 1/2)", ok)
kappa = sp.simplify(DB / DKL)
ser = sp.series(kappa, e, 0, 7).removeO()
target = sp.Rational(1, 4) + e ** 2 / 6 + sp.Rational(14, 45) * e ** 4 \
         + sp.Rational(724, 945) * e ** 6
ok = sp.simplify(ser - target) == 0
check("kappa(eps) = 1/4 + eps^2/6 + 14 eps^4/45 + 724 eps^6/945 + O(eps^8) "
      "(paper 6's series, re-derived exactly)", ok)

mu = sp.symbols("mu", positive=True)
DB_g = mu ** 2 / 8
DKL_g = mu ** 2 / 2
ok = sp.simplify(DB_g / DKL_g - sp.Rational(1, 4)) == 0
check("Gaussian recorder: kappa = 1/4 at every strength (exact)", ok)

# ------------------------------------------- CHECK 2: the finite-shot protocol
print("CHECK 2: the engineered protocol under shot noise (eps = 0.1)")
EPS = 0.1
p0 = np.array([0.5 + EPS, 0.5 - EPS])
p1 = np.array([0.5 - EPS, 0.5 + EPS])
V_true = float(mpsqrt(1 - 4 * mpf("0.1") ** 2))
DB_true = float(-mplog(mpf(V_true)))
DKL_true = float(4 * mpf("0.1") * atanh(2 * mpf("0.1")))
kappa_true = DB_true / DKL_true
print(f"      truth: V = {V_true:.6f}, D_B = {DB_true:.6f}, sigma = {DKL_true:.6f}, "
      f"kappa(0.1) = {kappa_true:.6f}")

M = 100000
REPS = 800
k_hats = []
for _ in range(REPS):
    # visibility: fringe measurement at the optimal phase, p_+ = (1 + V)/2
    kk = rng.binomial(M, 0.5 * (1 + V_true))
    V_hat = np.clip(2 * kk / M - 1, 1e-9, 1 - 1e-12)
    # sigma: forward/reverse sampling, plug-in KL over the binary outcome
    f_cnt = rng.multinomial(M, p0) / M
    r_cnt = rng.multinomial(M, p1) / M
    f_cnt = np.clip(f_cnt, 1e-12, 1)
    r_cnt = np.clip(r_cnt, 1e-12, 1)
    sig_hat = float(np.sum(f_cnt * np.log(f_cnt / r_cnt)))
    k_hats.append(-np.log(V_hat) / sig_hat)
k_hats = np.array(k_hats)
mean_k, std_k = float(k_hats.mean()), float(k_hats.std())
ok = abs(mean_k - kappa_true) < 3 * std_k / np.sqrt(REPS) + 2e-3 and std_k < 0.05
check(f"kappa estimator (M = {M} shots per leg, {REPS} replicas) recovers the "
      f"running value within CI", ok,
      f"kappa_hat = {mean_k:.4f} +/- {std_k:.4f} vs {kappa_true:.4f}")

# ------------------------------------------- CHECK 3: 1/4-vs-1 discrimination
print("CHECK 3: pricing the 1/4-vs-1 discrimination (the dissolved equality)")
# under kappa = 1 the predicted visibility is exp(-sigma); under the quarter law
# it is exp(-kappa(eps) sigma). Shots for 5-sigma separation on the fringe:
V_quarter = float(np.exp(-kappa_true * DKL_true))
V_equal = float(np.exp(-DKL_true))
# variance convention DISCLOSED (post-review): two conventions, both quoted —
# (a) data-generating hypothesis (quarter law true): sigma_V = sqrt(1 - V(1/4)^2)
# (b) strict null rejection (kappa = 1 as null):     sigma_V = sqrt(1 - V(1)^2)
sig_a = np.sqrt(1 - V_quarter ** 2)
sig_b = np.sqrt(1 - V_equal ** 2)
M_a = int(np.ceil((5 * sig_a / (V_quarter - V_equal)) ** 2))
M_b = int(np.ceil((5 * sig_b / (V_quarter - V_equal)) ** 2))
ok = V_quarter > V_equal and M_a < 500 and M_b < 2000
check("5-sigma separation of kappa = 1/4 from kappa = 1 at eps = 0.1: both "
      "variance conventions quoted — detection-resolution (quarter-law variance) "
      "and strict kappa=1-null rejection", ok,
      f"V(1/4) = {V_quarter:.4f} vs V(1) = {V_equal:.4f}; "
      f"M_5sigma = {M_a} (a) / {M_b} (b)")

# ------------------------------------------- CHECK 4: the systematics budget
print("CHECK 4: extraneous-dephasing systematic")
# any extra visibility loss eta adds to -ln V: kappa_hat = 1/4 + eta/sigma.
# requirement for a <= 10% bias: eta <= 0.025 sigma. verified numerically:
eta = 0.025 * DKL_true
k_biased = (DB_true + eta) / DKL_true
ok = abs(k_biased - kappa_true - 0.025) < 1e-12
check("kappa bias = eta/sigma exactly; 10%-bias design requirement "
      "eta <= 0.025 sigma", ok,
      f"eta = {eta:.5f} -> kappa_hat = {k_biased:.4f} (+0.025)")

# ------------------------------------------- CHECK 5: broken-bridge detection
print("CHECK 5: the protocol detects a broken bridge")
# mismatch: the arrow pair is a DIFFERENT distribution pair (eps' = 2 eps) than
# the which-path pair (eps) — the bridge's shared-J premise fails, and kappa_hat
# leaves the running curve by construction:
DKL_mis = float(4 * mpf("0.2") * atanh(2 * mpf("0.2")))
k_mis = DB_true / DKL_mis
ok = abs(k_mis - kappa_true) > 0.15
check("mismatched arrow/which-path pairs (eps' = 2 eps) pull kappa_hat far off "
      "the running curve — a measurable bridge-failure signature", ok,
      f"kappa_mis = {k_mis:.4f} vs curve {kappa_true:.4f}")

# ------------------------------------------------------------------- verdict
print()
total = PASS + FAIL
if FAIL == 0:
    print(f"ALL CHECKS PASS ({PASS}/{total})")
else:
    print(f"FAILURES: {FAIL}/{total}")
    raise SystemExit(1)
