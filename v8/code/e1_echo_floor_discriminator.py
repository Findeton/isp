#!/usr/bin/env python3
"""
e1_echo_floor_discriminator.py — v8 paper 10 §2: the active-protocol (echo/CPMG)
discriminator at the blindness boundary.

Paper 6 §3 proved the passive blindness of the seal's no-revival channel and named
its boundary: a matched REFOCUSABLE dephasing with the same free-induction decay
IS echo/CPMG-distinguishable from the seal — but the distinctions live on the
reversibility axis, so nothing crosses the CP-divisibility line. This receipt
turns that boundary exhibit into a designed protocol with numbers.

MODEL (disclosed): total qubit coherence under an n-pulse CPMG sequence of total
time T:
    -ln W(T, n) = chi_noise(T, n) + Lambda_s * T
  * chi_noise: Gaussian dephasing from stationary classical noise with
    autocorrelation Cn(t) = sig^2 exp(-|t|/tau_c) (Ornstein-Uhlenbeck), computed
    from the toggling function y(t) = +/-1 of the sequence:
        chi = (1/2) Int_0^T Int_0^T y(t) y(t') Cn(t - t') dt dt'
  * Lambda_s * T: the seal survival term, PULSE-INVARIANT BY MODEL — this encodes
    the corpus claim (a committed seal is not a unitary rotation; no pulse undoes
    a commit: paper 1 §3.5's definitional no-revival + paper 6's boundary), it is
    NOT derived here. The protocol's logic only needs the dichotomy
    refocusable-vs-not.

THE PROTOCOL: sweep n at fixed T; refocusable noise is suppressed (OU: ~ n^-2 for
pulse spacing << tau_c) while the floor stays; the plateau of -ln W over the
n-ladder estimates Lambda_s T. What the protocol CAN do: exclude the entire
refocusable-noise explanation class and measure the floor. What it CANNOT do
(honest boundary, verified in CHECK 5): distinguish the seal from EXACTLY
MARKOVIAN (white) dephasing, which is equally pulse-blind — the residual mimic
class is precisely paper 6's CP-divisibility line.

Numerics: chi integrals on a fine grid validated against closed forms (mpmath
dps = 40 anchors); shot-noise Monte Carlo float64, default_rng(20260702).
"""

import numpy as np
from mpmath import mp, mpf, exp as mpexp

mp.dps = 40
rng = np.random.default_rng(20260702)

PASS = 0
FAIL = 0

def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    if ok: PASS += 1
    else: FAIL += 1
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))


# --------------------------------------------------------------- chi integrals
def toggling(T, n, grid):
    """CPMG toggling function on the grid: pulses at (k - 1/2) T/n, k = 1..n."""
    y = np.ones_like(grid)
    if n == 0:
        return y
    pulses = (np.arange(1, n + 1) - 0.5) * T / n
    for p in pulses:
        y[grid >= p] *= -1
    # cumulative flips: recompute cleanly
    y = np.ones_like(grid)
    flips = np.searchsorted(pulses, grid, side="right")
    return (-1.0) ** flips

def chi_noise(T, n, sig2, tau_c, ngrid=1600):
    t = (np.arange(ngrid) + 0.5) * T / ngrid
    dt = T / ngrid
    y = toggling(T, n, t)
    Cmat = sig2 * np.exp(-np.abs(t[:, None] - t[None, :]) / tau_c)
    return 0.5 * float(y @ Cmat @ y) * dt * dt

# closed forms (OU, free induction and Hahn echo)
def chi_fid_exact(T, sig2, tau_c):
    x = mpf(T) / tau_c
    return float(sig2 * tau_c ** 2 * (x - 1 + mpexp(-x)))

def chi_hahn_exact(T, sig2, tau_c):
    x = mpf(T) / tau_c
    return float(sig2 * tau_c ** 2 * (x - 3 - mpexp(-x) + 4 * mpexp(-x / 2)))

# ------------------------------------------------ CHECK 1: integrator anchors
print("CHECK 1: grid integrator vs closed forms (OU noise)")
T, sig2, tau_c = 1.0, 4.0, 0.6
c_fid = chi_noise(T, 0, sig2, tau_c)
c_hahn = chi_noise(T, 1, sig2, tau_c)
e_fid = chi_fid_exact(T, sig2, tau_c)
e_hahn = chi_hahn_exact(T, sig2, tau_c)
ok = abs(c_fid - e_fid) / e_fid < 2e-3 and abs(c_hahn - e_hahn) / e_hahn < 2e-3
check("free-induction and Hahn-echo chi match the OU closed forms to < 0.2%",
      ok, f"FID {c_fid:.5f}/{e_fid:.5f}, Hahn {c_hahn:.5f}/{e_hahn:.5f}")

# --------------------------------------- CHECK 2: CPMG suppression + scaling
print("CHECK 2: the refocusable branch — CPMG suppression and its n^-2 scaling")
ns = [1, 2, 4, 8, 16, 32, 64]
chis = {n: chi_noise(T, n, sig2, tau_c) for n in ns}
ok = all(chis[ns[i + 1]] < chis[ns[i]] for i in range(len(ns) - 1))
check("chi_n strictly decreasing along the CPMG ladder n = 1..64", ok,
      " -> ".join(f"{chis[n]:.4f}" for n in (1, 8, 64)))
# scaling exponent in the pulse-spacing << tau_c regime (n >= 8)
nn = np.array([8, 16, 32, 64], dtype=float)
cc = np.array([chis[int(n)] for n in nn])
p_fit = -np.polyfit(np.log(nn), np.log(cc), 1)[0]
ok = 1.7 < p_fit < 2.3
check("suppression exponent ~ n^-2 for pulse spacing << tau_c (fitted p in "
      "(1.7, 2.3))", ok, f"p = {p_fit:.3f}")

# ------------------------------------------------ CHECK 3: the seal floor
print("CHECK 3: the floor — pulse-invariant seal term saturates the ladder")
Lam_s = 0.05                      # seal rate x T = the floor (injected truth)
def neg_lnW(T, n):
    return chi_noise(T, n, sig2, tau_c) + Lam_s * T
floor64 = neg_lnW(T, 64)
ok = abs(floor64 - Lam_s * T) < 0.15 * Lam_s * T and \
     all(neg_lnW(T, n) > neg_lnW(T, 2 * n) for n in (1, 2, 4, 8, 16, 32))
check("-ln W(T, n) decreases monotonically to the injected floor Lambda_s T "
      "(within 15% at n = 64)", ok,
      f"-lnW(64) = {floor64:.4f} vs floor {Lam_s * T:.4f}")

# --------------------------------------- CHECK 4: shot-noise floor estimator
print("CHECK 4: the floor estimator under shot noise")
M_SHOTS = 20000
REPS = 400
n_est = 64
# the protocol estimator is the RAW plateau value -ln W_hat at large n; its bias
# IS the residual refocusable chi at n_est (disclosed; shrinks as n^-2)
est_raw = []
for _ in range(REPS):
    W = np.exp(-neg_lnW(T, n_est))
    p = 0.5 * (1 + W)
    k = rng.binomial(M_SHOTS, p)
    W_hat = np.clip(2 * k / M_SHOTS - 1, 1e-6, 1 - 1e-9)
    est_raw.append(-np.log(W_hat))
m_raw, s_raw = float(np.mean(est_raw)), float(np.std(est_raw))
bias = m_raw - Lam_s * T
ok = abs(bias - chis[n_est]) < 3 * s_raw / np.sqrt(REPS) + 5e-4 and \
     s_raw < 0.01
check(f"raw plateau estimator: mean bias = the residual noise chi_64 (disclosed, "
      f"shrinks as n^-2), shot std < 0.01 at M = {M_SHOTS}",
      ok, f"mean = {m_raw:.4f} (floor {Lam_s * T:.4f} + chi64 {chis[64]:.4f}), "
      f"std = {s_raw:.4f}")

# discrimination: shots to distinguish floor = 0.05 from floor = 0 at 5 sigma
W1, W0 = np.exp(-(chis[64] + 0.05)), np.exp(-chis[64])
# fringe p = (1+W)/2; sigma_W per shot pair = sqrt(1 - W^2) approx
sigW = np.sqrt(1 - W1 ** 2)
M_need = int(np.ceil((5 * sigW / (W0 - W1)) ** 2))
ok = M_need < 20000
check("5-sigma discrimination of floor 0.05 vs 0 needs < 20k shots at n = 64",
      ok, f"M_5sigma = {M_need}")

# --------------------------------------- CHECK 5: the honest boundary (Markov)
print("CHECK 5: the residual mimic class — white (Markovian) dephasing is pulse-blind")
# white noise: Cn = 2 gamma delta(t) => chi = (1/2) Int y^2 * 2 gamma dt = gamma T.
# The identity is ANALYTIC (y^2 = 1); what the grid CAN verify (post-review, was a
# tautology): the toggling function is genuinely +/-1-valued for every n, so
# Int y^2 dt = T exactly on the grid — the mechanism of the pulse-blindness.
gamma = 0.08
ok = True
ngrid = 1600
tg = (np.arange(ngrid) + 0.5) * T / ngrid
for n in (0, 1, 4, 16, 64):
    y = toggling(T, n, tg)
    if not (np.all(np.abs(y) == 1.0)
            and abs(float((y * y).sum()) * T / ngrid - T) < 1e-12):
        ok = False
check("white-noise chi_n = gamma T for EVERY n [ANALYTIC: y^2 = 1; grid-verified: "
      "toggling +/-1-valued, Int y^2 dt = T at n = 0..64] — the surviving mimic "
      "class is memoryless (delta-correlated) dephasing: paper 6's CP-divisibility "
      "line in the multi-time/interventional sense",
      ok, f"gamma T = {gamma * T:.4f} at n = 0, 1, 4, 16, 64")

# ------------------------------------------------ CHECK 6: protocol summary table
print("CHECK 6: the designed ladder (printed) and the two-hypothesis split")
print("      n      chi_noise    -lnW(seal+noise)   -lnW(noise only)")
for n in (0, 1, 4, 16, 64):
    cn = chis.get(n, chi_noise(T, n, sig2, tau_c))
    print(f"      {n:<6} {cn:9.4f}    {cn + Lam_s * T:9.4f}          {cn:9.4f}")
split = (chis[64] + Lam_s * T) / max(chis[64], 1e-12)
ok = split > 3.0
check("at n = 64 the seal+noise curve sits > 3x above the pure-noise curve "
      "(the floor dominates the plateau)", ok, f"ratio = {split:.1f}")

# ------------------------------------------------------------------- verdict
print()
total = PASS + FAIL
if FAIL == 0:
    print(f"ALL CHECKS PASS ({PASS}/{total})")
else:
    print(f"FAILURES: {FAIL}/{total}")
    raise SystemExit(1)
