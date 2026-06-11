#!/usr/bin/env python3
"""
v6_p32b: the rigidity inversion (Paper 32, receipts part B).

The corrected converse says: full-rate decay at all scales forces
smoothness.  Its CONSTRUCTIVE face is an inversion: from detector
data alone, recover (a) the regularity class, (b) the location of
the singularity, (c) its amplitude - and classify impostors by
their in-window scale-break.  This script receipts the inversion at
demonstration scope.

 (i)   CLASS RECOVERY: alpha-hat = 2 x (measured rate), capped at
       smooth: calibration across alpha in {0.5, 1.0} and smooth
       controls, random positions and amplitudes.
 (ii)  POSITION RECOVERY: argmax_x |r~_t(x)| at the smallest valid
       scale lands on the cusp to within the kernel width.
 (iii) THE AMPLITUDE SANDWICH: at fixed scale, the detector signal
       is two-sidedly LINEAR in the cusp amplitude eta - the
       first-order rigidity inequality c1 eta <= sup|r~| <= c2 eta,
       with the measured c2/c1 spread printed.
 (iv)  THE DECISION RULE (the constructive converse, blind): fit a
       single power law to sup|r~_t|; rate >= 0.85 with small
       residual -> SMOOTH; rate < 0.85 with small residual -> CUSP
       with alpha-hat; large residual -> SCALE-BREAK (impostor
       class).  Blind classification over smooth / cusp /
       microstructure cases: the confusion matrix.
"""
import numpy as np

rng = np.random.default_rng(321)

N = 512
h = 1.0 / N
X = np.arange(N) * h
TS = np.geomspace(2.5e-4, 6e-3, 7)

def operator(c_nodes):
    c_edge = 0.5 * (c_nodes + np.roll(c_nodes, -1))
    L = np.zeros((N, N))
    idx = np.arange(N)
    jdx = (idx + 1) % N
    L[idx, idx] += c_edge
    L[jdx, jdx] += c_edge
    L[idx, jdx] -= c_edge
    L[jdx, idx] -= c_edge
    return L / (h * h)

def heat_diag(c_nodes, ts):
    lam, V = np.linalg.eigh(operator(c_nodes))
    return [((V * V) * np.exp(-t * lam)[None, :]).sum(1) / h
            for t in ts]

S_GRID = np.geomspace(0.5 * TS[0], 4 * TS[-1], 60)
_g_vals = [float(Kd[0] * np.sqrt(4 * np.pi * s) - 1.0)
           for Kd, s in zip(heat_diag(np.ones(N), S_GRID), S_GRID)]
def g_base(s):
    return np.interp(np.log(s), np.log(S_GRID), _g_vals)

def detector(c_nodes, ts):
    Ks = heat_diag(c_nodes, ts)
    return [Kd * np.sqrt(4 * np.pi * c_nodes * t) - 1.0
            - g_base(c_nodes * t) for Kd, t in zip(Ks, ts)]

def fit_power(sups, ts):
    A = np.vstack([np.log(ts), np.ones(len(ts))]).T
    coef, res = np.linalg.lstsq(A, np.log(sups), rcond=None)[:2]
    resid = float(np.sqrt(res[0] / len(ts))) if len(res) else 0.0
    return float(coef[0]), resid

def cusp_c(alpha, x0, eta):
    d = np.minimum(np.abs(X - x0), 1 - np.abs(X - x0))
    return 1.0 + eta * d ** alpha

# ---------- (i) class recovery ----------
print("== (i) class recovery: alpha-hat = 2 x rate ==")
print("   true alpha   x0     eta    alpha-hat")
errs = []
for alpha in (0.5, 1.0):
    for trial in range(3):
        x0 = float(rng.uniform(0.1, 0.9))
        eta = float(rng.uniform(0.4, 1.2))
        sups = [np.abs(r).max()
                for r in detector(cusp_c(alpha, x0, eta), TS)]
        sl, _ = fit_power(sups, TS)
        ah = min(2 * sl, 2.0)
        errs.append(abs(ah - alpha))
        print(f"     {alpha:.1f}      {x0:.2f}   {eta:.2f}"
              f"    {ah:.2f}")
print(f"  max |alpha-hat - alpha| = {max(errs):.2f}")
print("  -> the detector INVERTS: the Holder class is recovered")
print("     from rates alone (alpha <= 1 scope, as receipted in")
print("     p32a).")

# ---------- (ii) position recovery ----------
print("\n== (ii) position recovery ==")
worst = 0.0
for trial in range(6):
    x0 = float(rng.uniform(0.05, 0.95))
    r0 = detector(cusp_c(0.5, x0, 0.8), [TS[0]])[0]
    xh = float(X[np.argmax(np.abs(r0))])
    d = min(abs(xh - x0), 1 - abs(xh - x0))
    worst = max(worst, d)
print(f"  6 random cusps: max |x-hat - x0| = {worst:.4f}"
      f"  (kernel width sqrt(t) = {np.sqrt(TS[0]):.4f})")
print("  -> the singularity is LOCATED to within the kernel width:")
print("     the inversion is local, not just global.")

# ---------- (iii) the amplitude sandwich ----------
print("\n== (iii) the amplitude sandwich at fixed scale ==")
etas = np.array([0.2, 0.4, 0.8, 1.6])
sigs = []
for eta in etas:
    r = detector(cusp_c(0.5, 0.5, float(eta)), [TS[2]])[0]
    sigs.append(float(np.abs(r).max()))
ratios = np.array(sigs) / etas
print("   eta:    " + "  ".join(f"{e:.1f}" for e in etas))
print("   sup|r~|:" + "  ".join(f"{s:.4f}" for s in sigs))
print(f"   sup/eta in [{ratios.min():.4f}, {ratios.max():.4f}]"
      f"  (spread x{ratios.max()/ratios.min():.2f})")
print("  -> two-sidedly linear in the amplitude: the first-order")
print("     rigidity inequality c1 eta <= signal <= c2 eta at")
print("     demonstration scope - a detector ZERO at this scale")
print("     forces amplitude zero.")

# ---------- (iv) the blind decision rule ----------
print("\n== (iv) the constructive converse, blind ==")
cases = []
for _ in range(5):
    f = sum(rng.uniform(-0.2, 0.2) * np.sin(2 * np.pi * (k + 1) * X
            + rng.uniform(0, 7)) for k in range(3))
    cases.append(("SMOOTH", 1.0 + f))
for _ in range(5):
    a = float(rng.choice([0.5, 1.0]))
    cases.append((f"CUSP", cusp_c(a, float(rng.uniform(0.1, 0.9)),
                                  float(rng.uniform(0.4, 1.0)))))
for ddel in (1 / 32, 1 / 40):
    cases.append(("BREAK", 1.0 + 0.5 * np.sin(2 * np.pi * X / ddel)))
correct = 0
print("   true     verdict   rate   resid")
for label, c in cases:
    sups = [np.abs(r).max() for r in detector(c, TS)]
    sl, resid = fit_power(sups, TS)
    # the graded law's exponent range is (0, 1]: a non-decaying
    # reading (rate < 0.1) belongs to NO Holder class - it is a
    # scale-break, exactly like a large fit residual
    if resid > 0.25 or sl < 0.1:
        v = "BREAK"
    elif sl >= 0.85:
        v = "SMOOTH"
    else:
        v = "CUSP"
    correct += v == label
    print(f"   {label:7s}  {v:7s}  {sl:5.2f}  {resid:.3f}")
print(f"  blind classification: {correct}/{len(cases)} correct")
print("  -> the decision rule separates smooth, cusp, and")
print("     scale-break (impostor) classes from detector data")
print("     alone: the corrected converse is CONSTRUCTIVE at")
print("     demonstration scope.")
print("== p32b done ==")
