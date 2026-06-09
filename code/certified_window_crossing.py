#!/usr/bin/env python3
"""Certified finite-window crossing for hierarchical (Migdal-Kadanoff) 4D SU(2).

Companion to Paper 45.  Executable demonstration of the E/T/X architecture
(Entry compactness / certified Traversal / open eXit basin) on the nearest
exactly-renormalizable cousin of 4D SU(2) that still exhibits genuine
dimensional transmutation: SU(2) lattice gauge theory on the Berker-Ostlund
hierarchical lattice, whose exact RG step is the Migdal-Kadanoff recursion
(b=2, d=4):

    bond moving:   g = f^4                    (pointwise product = fusion)
    decimation:    c'_n = n * (g_n / (n g_1))^4   (2x2 plaquette tiling)

State = SU(2) class function f = sum_n c_n chi_n with n = 2j+1 (dimension
label), c_n >= 0.  Positivity of coefficients is exactly preserved by both
operations, which makes a fully certified (interval, two-sided,
tail-controlled) implementation possible with NO quadrature:

  * kept coefficients n <= N are mpmath intervals (outward rounded);
  * the tail  T >= sum_{n>N} n c_n  is an interval, controlled by
    - mass balance (fg)(1) = f(1) g(1)  (exact for pointwise products),
    - c_n <= T/n for n > N  (undercount inflation of kept coefficients),
    - decimation tail  sum_{m>N} g_m^4/m^2 <= T^4/(5 N^5).

Exit-basin lemma (Lemma 45.X in Paper 45; explicit constants): with
    eps = (sum_{n>=2} n c_n + tail) / c_1     (normalized nontrivial mass),
one MK step gives
    eps' <= (zeta(6)-1) (4 eps)^4 (1+eps)^12,
so for eps <= 1/5:  eps' <= 39.6 eps^4 <= 0.317 eps, and L_k = -log eps_k
obeys L_{k+1} >= 4 L_k - log 39.6.  Hence the hierarchical-model string
tension in bare units satisfies

    sigma_phys >= 4^{-K} ( -log eps_K - log(39.6)/3 ) > 0

whenever eps_K <= 1/5 is CERTIFIED at some level K.  (The Wilson loop at
level k is r_2^(area in level-k plaquettes), r_2 = c_2/(2 c_1) <= eps/2.)

Cost structure (the point of the demonstration): the number of certified
steps to the basin is K ~ 8/t0 ~ 4 beta0 (LINEAR in beta0, while the
transmuted scale is e^{-c beta0}), and the working precision must grow
linearly in K because the step map is expansive (arithmetic sensitivity
~16 per step; measured width consumption ~2.4 digits/step including
tail-inflation effects, hence the 2.9/step provisioning below).  Total
cost is therefore polynomial in beta0 - the log-refinement (Kondo)
principle made literal, versus the exponential cost of any uniform-
resolution method (Paper 44 SS10-11).

This file demonstrates the architecture; it is NOT a claim about the
hypercubic lattice (see Paper 45 for honest scope).

Usage:
    python3 certified_window_crossing.py                # certified table
    python3 certified_window_crossing.py --float        # float diagnostic
    python3 certified_window_crossing.py --t0 0.125     # single point
"""

from __future__ import annotations

import argparse
import math
import time

from mpmath import iv, mp

LOG_C0 = math.log((math.pi**6 / 945.0 - 1.0) * 256.0 * (1.2) ** 12)  # log 39.6
BASIN_EPS = 0.2


# ----------------------------------------------------------------------------
# certified state: kept interval coefficients + interval tail
# ----------------------------------------------------------------------------

class State:
    """f = sum_{n<=N} c[n-1] chi_n (+ tail), c interval >= 0, T >= sum_{n>N} n c_n."""

    __slots__ = ("c", "tail")

    def __init__(self, c, tail):
        self.c = c
        self.tail = tail

    @property
    def N(self):
        return len(self.c)

    def mass(self):
        s = iv.mpf(0)
        for i, ci in enumerate(self.c):
            s += (i + 1) * ci
        return s + self.tail

    def eps(self):
        s = iv.mpf(0)
        for i in range(1, self.N):
            s += (i + 1) * self.c[i]
        return (s + self.tail) / self.c[0]

    def prune(self, rel_floor):
        """Fold negligible high coefficients into the tail (rigorous)."""
        scale = self.c[0].b  # upper bound of c_1 (post-normalization ~ 1)
        cut = self.N
        extra = iv.mpf(0)
        while cut > 8:
            n = cut
            ci = self.c[n - 1]
            if ci.b * n < rel_floor * scale:
                extra += iv.mpf([0, ci.b]) * n
                cut -= 1
            else:
                break
        if cut < self.N:
            self.c = self.c[:cut]
            self.tail = self.tail + extra


def fuse(f: State, g: State) -> State:
    """Pointwise product f*g in the character basis, certified two-sided.

    (fg)_m = sum_{a,b admissible} f_a g_b, admissible (n-labels, n=2j+1):
        |a-b|+1 <= m <= a+b-1,  m = a+b-1 (mod 2).
    """
    N = min(f.N, g.N)
    fc, gc = f.c[:N], g.c[:N]
    # parity prefix sums of g: P[p][k] = sum_{b<=k, b%2==p} g_b   (k=0..N)
    P = [[iv.mpf(0)] * (N + 1), [iv.mpf(0)] * (N + 1)]
    for b in range(1, N + 1):
        p = b % 2
        q = 1 - p
        P[p][b] = P[p][b - 1] + gc[b - 1]
        P[q][b] = P[q][b - 1]
    Tf, Tg = f.tail, g.tail
    tfd = Tf.b / (N + 1)
    tgd = Tg.b / (N + 1)

    out = []
    for m in range(1, N + 1):
        s = iv.mpf(0)
        for a in range(1, N + 1):
            blo = abs(a - m) + 1
            if blo > N:
                continue
            bhi = min(a + m - 1, N)
            p = (a + m - 1) % 2
            win = P[p][bhi] - P[p][blo - 1]
            # win encloses a sum of nonnegatives; clip lower at 0
            if win.a < 0:
                win = iv.mpf([0, win.b])
            s += fc[a - 1] * win
        # undercount inflation: terms with a>N or b>N
        gw = max([gc[b - 1].b for b in range(max(1, N - m + 1), N + 1)] + [tgd])
        fw = max([fc[a - 1].b for a in range(max(1, N - m + 1), N + 1)] + [tfd])
        delta = m * (tfd * gw + tgd * fw + tfd * tgd)
        out.append(s + iv.mpf([0, delta]))

    # tail by mass balance: (fg)(1) = f(1) g(1)
    M = f.mass() * g.mass()
    km = iv.mpf(0)
    for i, ci in enumerate(out):
        km += (i + 1) * ci
    t = M - km
    t_lo = max(0, t.a)
    t_hi = t.b if t.b > 0 else mp.mpf(0)
    return State(out, iv.mpf([t_lo, t_hi]))


def mk_step(f: State, rel_floor) -> State:
    """One MK step, b=2, d=4: bond-move f^4 then decimate ratios^4; renormalize."""
    g2 = fuse(f, f)
    g2.prune(rel_floor)
    g4 = fuse(g2, g2)
    g4.prune(rel_floor)
    N = g4.N
    c1 = g4.c[0] ** 4
    out = [iv.mpf(1)]
    for n in range(2, N + 1):
        out.append((g4.c[n - 1] ** 4 / (mp.mpf(n) ** 3)) / c1)
    t_hi = (g4.tail.b ** 4) / (5 * mp.mpf(N) ** 5)
    tail = iv.mpf([0, t_hi]) / c1
    st = State(out, tail)
    st.prune(rel_floor)
    return st


def heat_kernel_state(t0: float, N: int) -> State:
    """c_n = n exp(-t0 (n^2-1)/4), rigorous tail bound for sum_{n>N} n c_n."""
    t = iv.mpf(str(t0))
    c = [n * iv.exp(-t * (n * n - 1) / 4) for n in range(1, N + 1)]
    # tail: sum_{n>N} n^2 e^{-t(n^2-1)/4}
    #   n^2 e^{-t n^2/8} <= 8/(t e)  and  sum_{n>N} e^{-t n^2/8} <= geometric
    tb = mp.mpf(str(t0))
    sup = 8.0 / (tb * mp.e)
    ratio = mp.exp(-tb * (2 * N + 3) / 8)
    geo = mp.exp(-tb * (N + 1) ** 2 / 8) / (1 - ratio)
    t_hi = mp.exp(tb / 4) * sup * geo
    return State(c, iv.mpf([0, t_hi]))


# ----------------------------------------------------------------------------
# drivers
# ----------------------------------------------------------------------------

def run_certified(t0: float, N: int, kmax: int = 400, verbose: bool = False):
    rel_floor = mp.mpf(2) ** int(-0.92 * mp.prec)  # prune threshold << width floor
    st = heat_kernel_state(t0, N)
    for k in range(kmax + 1):
        e = st.eps()
        if verbose:
            print(f"  k={k:4d} N={st.N:4d} eps=[{mp.nstr(e.a, 6)},{mp.nstr(e.b, 6)}] "
                  f"tail_hi={mp.nstr(st.tail.b, 3)}")
        if e.b <= BASIN_EPS:
            lower = -mp.log(e.b) - LOG_C0 / 3
            log_sigma = float(mp.log(lower)) - k * math.log(4.0)
            width = float(e.b - e.a)
            return k, float(e.b), log_sigma, width
        if not mp.isfinite(e.b) or e.a < 0:
            print(f"  [diag] k={k} NONFINITE/NEG eps=[{mp.nstr(e.a,8)},{mp.nstr(e.b,8)}]"
                  f" tail=[{mp.nstr(st.tail.a,4)},{mp.nstr(st.tail.b,4)}] N={st.N}")
            return None
        st = mk_step(st, rel_floor)
    e = st.eps()
    print(f"  [diag] kmax exhausted: eps=[{mp.nstr(e.a,8)},{mp.nstr(e.b,8)}]"
          f" tail.b={mp.nstr(st.tail.b,4)} N={st.N}")
    return None


def run_float(t0: float, N: int, kmax: int = 400):
    import numpy as np
    n = np.arange(1, N + 1, dtype=np.float64)
    c = n * np.exp(-t0 * (n**2 - 1.0) / 4.0)
    th = (np.arange(4096) + 0.5) * (math.pi / 4096)
    chars = np.array([np.sin(m * th) / np.sin(th) for m in range(1, N + 1)])
    w = (2.0 / math.pi) * np.sin(th) ** 2 * (math.pi / 4096)
    for k in range(kmax + 1):
        eps = float(np.sum(n[1:] * c[1:]) / c[0])
        if eps <= BASIN_EPS:
            return k, eps, float(c[1] / (2 * c[0]))
        fval = c @ chars
        g = chars @ (fval**4 * w)
        c = n * (g / (n * g[0])) ** 4
        c = c / c[0]
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--float", action="store_true", dest="floatmode")
    ap.add_argument("--t0", type=float, default=None)
    ap.add_argument("--N", type=int, default=0)
    ap.add_argument("--digits", type=int, default=0)
    ap.add_argument("--verbose", action="store_true")
    args = ap.parse_args()

    t0_list = [args.t0] if args.t0 else [1.0, 0.5, 0.25, 0.125, 0.0833, 0.0625, 0.05]
    print("hierarchical (MK) 4D SU(2): certified window crossing  [Paper 45]")
    print("t0 ~ 2/beta0 (heat-kernel line); exit basin eps <= 1/5 (Lemma 45.X)")
    print()
    if args.floatmode:
        print(" t0       beta0~2/t0  K(basin)  eps_K       r2_K")
        for t0 in t0_list:
            N = args.N or max(48, int(math.sqrt(1280.0 / t0)) + 16)
            res = run_float(t0, N)
            if res:
                k, e, r2 = res
                print(f" {t0:<8.4g} {2/t0:<11.4g} {k:<9d} {e:<11.4e} {r2:<11.4e}")
        return

    print(" t0      beta0   N    digits  K(cert)  eps_K(hi)   width(eps)  "
          "log4 sigma_phys >=   secs")
    rows = []
    for t0 in t0_list:
        # N sizing: the truncation edge injects a structural width seed
        # ~10^{-0.078 t0 N^2} (edge coefficients have O(1) relative width by
        # construction); it must be below the ~2-digits/step growth budget
        # over K ~ 7.9/t0 steps, so N grows ~1/t0 for deep windows.
        n_phys = int(math.sqrt(1280.0 / t0)) + 16
        n_seed = int(1.15 * math.sqrt(200.0 / t0**2 + 255.0 / t0)) + 1
        N = args.N or max(48, n_phys, n_seed)
        fl = run_float(t0, N)
        k_est = fl[0] if fl else 200
        # measured width consumption is ~2.4 digits/step (pow4 twice, fusion,
        # undercount inflation); provision 2.9/step + margin
        digits = args.digits or int(2.9 * (k_est + 4)) + 60
        mp.prec = int(digits * 3.3322) + 8
        iv.prec = mp.prec  # mpmath interval context has its own precision!
        tic = time.time()
        res = run_certified(t0, N, kmax=k_est + 40, verbose=args.verbose)
        secs = time.time() - tic
        if res is None:
            print(f" {t0:<7.4g} {2/t0:<7.4g} {N:<4d} {digits:<7d} "
                  f"FAILED (no certified basin entry)   {secs:6.1f}")
            continue
        k, eps_hi, log_sigma, width = res
        rows.append((t0, k, log_sigma))
        print(f" {t0:<7.4g} {2/t0:<7.4g} {N:<4d} {digits:<7d} {k:<8d} "
              f"{eps_hi:<11.4e} {width:<11.2e} {log_sigma/math.log(4.0):<19.3f}  {secs:6.1f}")
    if len(rows) >= 3:
        xs = [1.0 / r[0] for r in rows]
        ys = [r[2] for r in rows]
        n = len(xs)
        sx, sy = sum(xs), sum(ys)
        sxx = sum(x * x for x in xs)
        sxy = sum(x * y for x, y in zip(xs, ys))
        slope = (n * sxy - sx * sy) / (n * sxx - sx * sx)
        icpt = (sy - slope * sx) / n
        print()
        print(f"transmutation: certified log sigma_phys ~= {slope:.3f}/t0 + {icpt:.2f}")
        print(f"  1/t0 ~ beta0/2  =>  d log sigma / d beta0 ~= {slope/2:.3f}")
        print("  essential singularity e^{-c beta0} certified through the window;")
        print("  cost (steps, digits) LINEAR in beta0 - the log-refinement principle.")


if __name__ == "__main__":
    main()
