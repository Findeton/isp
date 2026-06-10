#!/usr/bin/env python3
"""
v6_p13a: the near-horizon record operator (Paper 13, route 1).

A horizon is a lapse-degeneracy locus N -> 0.  The lapse-resolved record
operator (Paper 12) is A_N = -N d(N d.), symmetric in L^2(dx/N), and the
identity N d/dx = d/dy with the tortoise (record) coordinate
y = int dx/N makes it EXACTLY the free Laplacian -d^2/dy^2 in record
coordinates - for every lapse profile.  Receipts, for N = kappa x:

 (i)  RECORD DISTANCE: the distance from any interior point to the
      locus diverges logarithmically: Y(x_min) = (1/kappa) ln(1/x_min);
      the lattice record distance tracks it.
 (ii) EXACT FREE STRUCTURE: the lapse operator's spectrum on
      [x_min, 1] (Dirichlet) equals the free spectrum (k pi / Y)^2 at
      O(h^2) - the tortoise unitary equivalence, machine-verified.
 (iii) MODE PILEUP: the counting function N(Lambda) grows by
      (sqrt(Lambda)/pi) (ln 10 / kappa) per decade of approach - the
      spectral signature of the horizon at infinite record distance.
 (iv) EXPONENTIAL APPROACH: a record wave packet falling toward the
      locus obeys x_peak(t) = x_0 e^{-kappa t}: measured slope of
      ln x_c(t) equals -kappa (run at kappa = 1 and kappa = 0.5).
"""
import numpy as np
from scipy.linalg import eigvalsh_tridiagonal

def lapse_tridiag(x_min, n, kappa, beta=1.0, neumann_left=False):
    """Symmetrized tridiagonal for A_N = -N d(N d.), N = kappa x^beta,
    on a geometric grid over [x_min, 1].  Dirichlet at x = 1; Dirichlet
    (default) or Neumann at x_min.  Returns (diag, off, Y_lattice)."""
    xs = x_min * (1.0 / x_min) ** (np.arange(n + 1) / n)   # nodes
    N = lambda x: kappa * x ** beta
    xb = np.sqrt(xs[:-1] * xs[1:])                          # bond midpoints
    w = N(xb) / np.diff(xs)                                 # bond weights
    cell = np.empty(n + 1)
    cell[1:-1] = 0.5 * (xs[2:] - xs[:-2])
    cell[0] = 0.5 * (xs[1] - xs[0])
    cell[-1] = 0.5 * (xs[-1] - xs[-2])
    m = cell / N(xs)                                        # measure dx/N
    if neumann_left:
        # unknowns at nodes 0..n-1 (node n is the Dirichlet wall at x=1)
        d = np.empty(n); e = np.empty(n - 1)
        wl = np.concatenate(([0.0], w[:-1]))                # no bond left of node 0
        d = (wl + w) / m[:-1]
        e = -w[:-1] / np.sqrt(m[:-2] * m[1:-1])
    else:
        # unknowns at interior nodes 1..n-1
        d = (w[:-1] + w[1:]) / m[1:-1]
        e = -w[1:-1] / np.sqrt(m[1:-2] * m[2:-1])
    Y = np.sum(np.diff(xs) / N(xb))
    return d, e, Y

# ---------- (i) + (ii): record distance and exact free structure ----------
print("== (i)+(ii) the lapse operator IS the free record Laplacian ==")
kappa = 1.0
for x_min in (1e-2, 1e-4):
    _, _, Y = lapse_tridiag(x_min, 4000, kappa)
    Yex = np.log(1.0 / x_min) / kappa
    print(f"  x_min = {x_min:.0e}: lattice record distance Y = {Y:.6f}"
          f"   exact (1/kappa) ln(1/x_min) = {Yex:.6f}"
          f"   rel err = {abs(Y - Yex)/Yex:.2e}")
x_min = 1e-3
Yex = np.log(1.0 / x_min)
errs = {}
for n in (2000, 4000):
    d, e, Y = lapse_tridiag(x_min, n, kappa)
    lam = eigvalsh_tridiagonal(d, e)[:4]
    tgt = (np.arange(1, 5) * np.pi / Y) ** 2
    errs[n] = np.abs(lam - tgt) / tgt
    print(f"  n = {n}: max rel err of lam_1..4 vs (k pi / Y)^2 = "
          f"{errs[n].max():.3e}")
print(f"  ratio = {errs[2000].max()/errs[4000].max():.2f}   [O(h^2): 4.00]")
print("  -> A_N = -N d(N d) is EXACTLY -d^2/dy^2 in the record (tortoise)")
print("     coordinate, for the lattice as for the continuum: the horizon")
print("     sits at infinite record distance behind a free geometry.")

# ---------- (iii) mode pileup ----------
print("\n== (iii) mode pileup: the spectral signature of infinite distance ==")
Lam = 400.0
print("   x_min     modes below Lambda = 400    predicted (sqrt(L)/pi) Y")
counts = []
for x_min in (1e-2, 1e-3, 1e-4, 1e-5):
    d, e, Y = lapse_tridiag(x_min, 8000, kappa)
    lam = eigvalsh_tridiagonal(d, e)
    cnt = int(np.sum(lam < Lam))
    counts.append(cnt)
    print(f"   {x_min:.0e}        {cnt:4d}                       "
          f"{np.sqrt(Lam)/np.pi*Y:8.2f}")
incs = np.diff(counts)
print(f"  increments per decade: {list(incs)}   predicted "
      f"{np.sqrt(Lam)/np.pi*np.log(10)/kappa:.2f}")
print("  -> the counting function grows WITHOUT BOUND as the lattice")
print("     approaches the locus - log-many modes per decade: the record")
print("     spectrum piles up at the horizon (infinite record volume).")

# ---------- (iv) exponential approach ----------
print("\n== (iv) infall: x_peak(t) = x_0 exp(-kappa t) ==")
for kap in (1.0, 0.5):
    x_min, n = 1e-6, 6000
    xs = x_min * (1.0 / x_min) ** (np.arange(n + 1) / n)
    N = lambda x: kap * x
    xb = np.sqrt(xs[:-1] * xs[1:])
    w = N(xb) / np.diff(xs)
    cell = np.empty(n + 1)
    cell[1:-1] = 0.5 * (xs[2:] - xs[:-2])
    cell[0] = 0.5 * (xs[1] - xs[0]); cell[-1] = 0.5 * (xs[-1] - xs[-2])
    m = cell / N(xs)
    sq = np.sqrt(m)
    y = np.concatenate(([0.0], np.cumsum(np.diff(xs) / N(xb))))
    y -= y[-1]                                  # y = 0 at x = 1, negative inward
    def Lv(v):
        u = v / sq
        flux = w * (u[1:] - u[:-1])
        r = np.zeros_like(u)
        r[:-1] += flux
        r[1:] -= flux
        return -r / sq                          # sq * (A_N u): symmetrized
    # packet at y0 = -3 moving toward the horizon (decreasing y)
    y0, sig = -3.0, 0.5
    u0 = np.exp(-0.5 * ((y - y0) / sig) ** 2)
    du0 = -(y - y0) / sig ** 2 * u0             # u_t = +u_y: infalling mover
    v_prev = sq * u0
    dt = 0.2 * np.min(np.diff(y))
    v = sq * (u0 + dt * du0) - 0.5 * dt * dt * Lv(sq * u0)
    t_marks, x_cs = [], []
    steps = int(6.0 / dt)
    for s in range(steps):
        v_next = 2 * v - v_prev - dt * dt * Lv(v)
        v_prev, v = v, v_next
        t = (s + 2) * dt
        if abs(t - round(t / 0.75) * 0.75) < dt / 2 and 0.5 <= t <= 5.5:
            e_dens = v * v
            yc = float((y * e_dens).sum() / e_dens.sum())
            t_marks.append(t); x_cs.append(np.exp(kap * yc))
    t_marks = np.array(t_marks); x_cs = np.array(x_cs)
    slope = np.polyfit(t_marks, np.log(x_cs), 1)[0]
    print(f"  kappa = {kap}: fitted d ln x_c / dt = {slope:.4f}"
          f"   target -kappa = {-kap}   err = {abs(slope + kap):.1e}")
print("  -> infalling record packets approach the locus exponentially in")
print("     coordinate time at exactly the surface-gravity rate: the locus")
print("     is never reached at finite record time - a horizon.")
print("== p13a done ==")
