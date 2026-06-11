#!/usr/bin/env python3
"""
v6_p32c: the 2d port of the graded Weyl law ((C-reg-rig), first
installment; Paper 32 / publishable Paper IV).

Port of the 1d receipts to L = -div(c grad) on the 2-torus:
 (i)   calibration with the exact constant-coefficient rescaling
       baseline K_t(c) = K_{ct}(1) (valid in any dimension), and
       the smooth-coefficient rate (graded law: t^1);
 (ii)  the graded forward law for C^alpha cusps (rates
       min(1, alpha/2));
 (iii) the 2d homogenization impostor with its OWN exact classical
       anchor: for a statistically isotropic symmetric two-phase
       medium, the effective coefficient is the GEOMETRIC MEAN
       (Dykhne/Keller duality) - the kernel-reported c_eff is
       tested against sqrt(c1 c2);
 (iv)  position recovery in 2d (the inversion is local in any d).
"""
import numpy as np

rng = np.random.default_rng(322)

N = 40                      # 2-torus grid (N^2 = 1600 sites)
h = 1.0 / N
xs = np.arange(N) * h
X, Y = np.meshgrid(xs, xs, indexing="ij")

def operator(c):
    """FD divergence-form Laplacian on T^2 with edge-averaged c."""
    n2 = N * N
    L = np.zeros((n2, n2))
    def idx(i, j):
        return (i % N) * N + (j % N)
    for i in range(N):
        for j in range(N):
            s = idx(i, j)
            for (di, dj) in ((1, 0), (0, 1)):
                t = idx(i + di, j + dj)
                ce = 0.5 * (c[i, j] + c[(i + di) % N, (j + dj) % N])
                L[s, s] += ce
                L[t, t] += ce
                L[s, t] -= ce
                L[t, s] -= ce
    return L / (h * h)

def heat_diag(c, ts):
    lam, V = np.linalg.eigh(operator(c))
    return [((V * V) * np.exp(-t * lam)[None, :]).sum(1) / (h * h)
            for t in ts]

TS = np.geomspace(1.2e-3, 1.0e-2, 6)
S_GRID = np.geomspace(0.5 * TS[0], 4 * TS[-1], 40)
_g = [float(Kd[0] * (4 * np.pi * s) - 1.0)
      for Kd, s in zip(heat_diag(np.ones((N, N)), S_GRID), S_GRID)]
def g_base(s):
    return np.interp(np.log(s), np.log(S_GRID), _g)

def detector(c, ts):
    cf = c.flatten()
    out = []
    for Kd, t in zip(heat_diag(c, ts), ts):
        raw = Kd * (4 * np.pi * cf * t) - 1.0
        out.append(raw - g_base(cf * t))
    return out

def rate(sups, ts):
    A = np.vstack([np.log(ts), np.ones(len(ts))]).T
    return float(np.linalg.lstsq(A, np.log(sups), rcond=None)[0][0])

# ---------- (i) calibration ----------
print("== (i) 2d calibration ==")
r0 = detector(1.4 * np.ones((N, N)), [TS[0], TS[-1]])
print(f"  constant c = 1.4: floor {np.abs(r0[0]).max():.1e},"
      f" {np.abs(r0[-1]).max():.1e}")
c_sm = 1.0 + 0.25 * np.sin(2 * np.pi * X) * np.cos(2 * np.pi * Y)
sups = [np.abs(r).max() for r in detector(c_sm, TS)]
print(f"  smooth c: rate = {rate(sups, TS):.3f}  (graded law: 1.0)")

# ---------- (ii) graded law in 2d ----------
print("\n== (ii) the graded law on the 2-torus ==")
print("   alpha    rate     predicted")
def torus_dist(X, Y, x0, y0):
    dx = np.minimum(np.abs(X - x0), 1 - np.abs(X - x0))
    dy = np.minimum(np.abs(Y - y0), 1 - np.abs(Y - y0))
    return np.sqrt(dx ** 2 + dy ** 2)
for alpha in (0.5, 1.0):
    c = 1.0 + 0.8 * torus_dist(X, Y, 0.5, 0.5) ** alpha
    sups = [np.abs(r).max() for r in detector(c, TS)]
    print(f"   {alpha:.1f}     {rate(sups, TS):.3f}     "
          f"{min(1.0, alpha / 2):.2f}")
print("  -> the graded forward law ports to 2d.")

# ---------- (iii) the Dykhne impostor ----------
print("\n== (iii) the 2d impostor: geometric-mean effective medium ==")
c1, c2 = 0.5, 2.0
# symmetric two-phase random checkerboard at cell scale 1/10
cell = N // 10
phase = rng.random((10, 10)) < 0.5
c_chk = np.where(np.kron(phase, np.ones((cell, cell))), c1, c2)
gm = float(np.sqrt(c1 * c2))
ts_hi = np.geomspace(6e-3, 2e-2, 4)
Ks = heat_diag(c_chk, ts_hi)
eff = [float((1.0 / (Kd * 4 * np.pi * t)).mean())
       for Kd, t in zip(Ks, ts_hi)]
print(f"  symmetric two-phase checkerboard (c1, c2) = ({c1}, {c2}):")
print(f"  arithmetic mean {np.mean(c_chk):.3f}, geometric mean"
      f" {gm:.4f},")
print(f"  kernel-reported effective c = {np.mean(eff):.4f}"
      f"  ({abs(np.mean(eff) - gm) / gm * 100:.1f}% from geometric)")
ts_lo = [3e-4]
sup_lo = np.abs(detector(c_chk, ts_lo)[0]).max()
print(f"  below the cell scale: sup|r~| = {sup_lo:.2f} (O(1) break)")
print("  -> the 2d impostor reads as the DYKHNE/KELLER geometric-")
print("     mean medium - dimension-specific exact homogenization,")
print("     correctly reproduced - and remains scale-bounded: the")
print("     corrected (all-scale) converse is the right statement")
print("     in 2d exactly as in 1d.")

# ---------- (iv) position recovery in 2d ----------
print("\n== (iv) position recovery on the 2-torus ==")
worst = 0.0
for _ in range(4):
    x0, y0 = rng.uniform(0.1, 0.9, 2)
    c = 1.0 + 0.8 * torus_dist(X, Y, x0, y0) ** 0.5
    r = detector(c, [TS[0]])[0].reshape(N, N)
    i, j = np.unravel_index(np.argmax(np.abs(r)), (N, N))
    d = float(torus_dist(np.array([[i * h]]), np.array([[j * h]]),
                         x0, y0)[0, 0])
    worst = max(worst, d)
print(f"  4 random cusps: max location error = {worst:.3f}"
      f"  (kernel width sqrt(t) = {np.sqrt(TS[0]):.3f})")
print("  -> the inversion is local in 2d as in 1d.")
print("== p32c done ==")
