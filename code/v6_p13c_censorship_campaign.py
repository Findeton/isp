#!/usr/bin/env python3
"""
v6_p13c: the record censorship classification (Paper 13, route 3).

The lapse form A_N = -N d(N d.) is EXACTLY -d^2/dy^2 in the record
(tortoise) coordinate y = int dx/N for EVERY lapse profile (p13a).  The
entire classification of a degeneracy locus N = x^beta therefore reduces
to ONE quantity: the record distance to the locus,

    Y = int_0 dx / x^beta :  FINITE  for beta < 1,
                             INFINITE for beta >= 1.

 (i)  beta < 1 (NAKED): the locus sits at FINITE record distance - a
      regular endpoint demanding a boundary condition.  Receipt: the
      clamped and free record towers converge to DIFFERENT continuum
      theories (lam_1 -> (pi/2Y)^2 vs (pi/4Y)^2... two distinct exact
      targets): a boundary record is DEMANDED.
 (ii) beta >= 1 (CENSORED): infinite record distance.  Both towers
      collapse onto the same free record geometry: lam_1 * Y^2 -> pi^2
      (clamped) and pi^2/4 (free) while lam_1 itself -> 0 - the scheme
      label survives only as a tag riding AT INFINITE RECORD DISTANCE,
      invisible to every sealed diamond at finite distance.  THE RECORD
      CENSORSHIP CRITERION: a degeneracy is a horizon iff its extension
      ambiguity is displaced to infinite record distance (beta >= 1);
      below the line it is naked and demands a boundary record.
      beta = 1 (Rindler) is the marginal case: Y diverges only
      logarithmically - the same log-threshold as P12's alpha = 1.
 (iii) EXTREMAL HORIZONS ARE COLD: for N = x(x + a)/(1 + a) the surface
      gravity is kappa_a = N'(0) = a/(1+a); the Euclidean tip is smooth
      (m = 1 mode exponent exactly 1) ONLY at beta = 2pi/kappa_a:
      T = kappa_a/2pi -> 0 as a -> 0.  The extremal limit has a record
      cusp: no period closes it, the horizon is at zero temperature.
"""
import numpy as np
from scipy.linalg import eigvalsh_tridiagonal
import scipy.sparse as sp
import scipy.sparse.linalg as spl

def lapse_lam1(x_min, n, beta, clamped):
    """lam_1 of A_N = -N d(N d.), N = x^beta, on [x_min, 1], grid
    uniform in the record (tortoise) coordinate; Dirichlet at x = 1;
    clamped (Dirichlet) or free (Neumann) at x_min.  Also returns the
    record distance Y(x_min)."""
    if beta == 1.0:
        xs = x_min * (1.0 / x_min) ** (np.arange(n + 1) / n)
    else:
        Yfull = (x_min ** (1 - beta) - 1) / (beta - 1)
        ys = Yfull * (1 - np.arange(n + 1) / n)        # y = 0 at x = 1
        xs = (1 + (beta - 1) * ys) ** (1 / (1 - beta))
    N = lambda x: x ** beta
    xb = np.sqrt(xs[:-1] * xs[1:])
    w = N(xb) / np.diff(xs)
    cell = np.empty(n + 1)
    cell[1:-1] = 0.5 * (xs[2:] - xs[:-2])
    cell[0] = 0.5 * (xs[1] - xs[0]); cell[-1] = 0.5 * (xs[-1] - xs[-2])
    m = cell / N(xs)
    Y = np.sum(np.diff(xs) / N(xb))
    if clamped:
        d = (w[:-1] + w[1:]) / m[1:-1]
        e = -w[1:-1] / np.sqrt(m[1:-2] * m[2:-1])
    else:
        wl = np.concatenate(([0.0], w[:-1]))
        d = (wl + w) / m[:-1]
        e = -w[:-1] / np.sqrt(m[:-2] * m[1:-1])
    return eigvalsh_tridiagonal(d, e, select="i", select_range=(0, 0))[0], Y

# ---------- (i)+(ii) the censorship line at beta = 1 ----------
print("== (i)+(ii) clamped vs free record towers across the lapse family ==")
print("   beta   x_min     lam1_clamped   lam1_free    lam1_c*Y^2"
      "   lam1_f*Y^2      Y")
for beta in (0.5, 0.75, 1.0, 2.0):
    for x_min in (1e-2, 1e-3, 1e-4):
        lc, Y = lapse_lam1(x_min, 8000, beta, True)
        lf, _ = lapse_lam1(x_min, 8000, beta, False)
        print(f"   {beta:4.2f}   {x_min:.0e}    {lc:11.6f}   {lf:11.6f}"
              f"   {lc*Y*Y:9.4f}    {lf*Y*Y:9.4f}   {Y:9.3f}")
print("  exact free-Laplacian targets: clamped (D-D) lam1*Y^2 = pi^2 ="
      f" {np.pi**2:.4f};")
print(f"  free (N-D) lam1*Y^2 = pi^2/4 = {np.pi**2/4:.4f}.")
print("  reading:")
print("   beta < 1 (Y finite): lam_1 converges to TWO DIFFERENT finite")
print("     limits - e.g. beta = 0.5: clamped -> pi^2/4 = 2.4674, free ->")
print("     pi^2/16 = 0.6169 (Y -> 2): the locus is a regular endpoint at")
print("     FINITE record distance; the continuum theory is undetermined")
print("     until a boundary record decides: NAKED.")
print("   beta >= 1 (Y infinite): both towers collapse onto the SAME free")
print("     record geometry (lam1*Y^2 pinned at pi^2 and pi^2/4 while")
print("     lam_1 -> 0): the clamped/free label rides at infinite record")
print("     distance, invisible to every finite sealed diamond: CENSORED.")
print("   beta = 1 is marginal (Y ~ ln(1/x_min), the P12 log threshold);")
print("   beta = 2 censors at power rate (Y ~ 1/x_min): extremal-fast.")

# ---------- (iii) extremal horizons are cold ----------
print("\n== (iii) extremal coldness: the smooth period tracks 1/N'(0) ==")
def tip_exponent(a, beta_period, n=60000, x_min=1e-5):
    """m = 1 Euclidean mode exponent at the tip for the static metric
    ds^2 = dx^2 + N^2 dtau^2, N = x(x+a)/(1+a), tau-period beta_period.
    Smooth tip <=> exponent = 1."""
    xs = x_min * (1.0 / x_min) ** (np.arange(n + 1) / n)
    N = lambda x: x * (x + a) / (1 + a)
    xb = np.sqrt(xs[:-1] * xs[1:])
    w = N(xb) / np.diff(xs)
    cell = np.empty(n + 1)
    cell[1:-1] = 0.5 * (xs[2:] - xs[:-2])
    cell[0] = 0.5 * (xs[1] - xs[0]); cell[-1] = 0.5 * (xs[-1] - xs[-2])
    m = N(xs) * cell
    cent = (2 * np.pi / beta_period) ** 2 / N(xs) ** 2 * m
    # interior unknowns (Dirichlet at x = 1, natural at x_min)
    d = np.concatenate(([w[0]], w[:-1] + w[1:])) + cent[:-1]
    e = -w[:-1]
    A = sp.diags([e, d, e], [-1, 0, 1], format="csc")
    Minv = sp.diags(1.0 / np.sqrt(m[:-1]))
    L = Minv @ A @ Minv
    vals, vecs = spl.eigsh(L, k=1, sigma=0, which="LM")
    v = np.abs(vecs[:, 0] / np.sqrt(m[:-1]))
    i1 = np.searchsorted(xs, 1.5e-3); i2 = np.searchsorted(xs, 8e-3)
    return np.polyfit(np.log(xs[i1:i2]), np.log(v[i1:i2]), 1)[0]

print("    a     kappa_a = a/(1+a)   beta tested        tip exponent")
for a in (0.5, 0.25):
    kap = a / (1 + a)
    for tag, bet in (("2pi/kappa_a", 2 * np.pi / kap), ("2pi (naive)", 2 * np.pi)):
        s = tip_exponent(a, bet)
        print(f"  {a:5.2f}      {kap:7.4f}        {tag:12s}      {s:8.4f}")
print("  -> the tip is smooth (exponent 1) only at beta = 2pi/N'(0):")
print("     T = N'(0)/2pi.  As a -> 0 (extremal limit, N ~ x^2) the")
print("     smooth period diverges: EXTREMAL RECORD HORIZONS ARE COLD")
print("     (T -> 0); the Euclidean tip degenerates to a cusp that no")
print("     finite period closes.")
print("== p13c done ==")
