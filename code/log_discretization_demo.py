#!/usr/bin/env python3
"""
Why logarithmic discretization (Wilson's trick) is the right tool when physics lives at an
exponentially small scale -- illustrated on DEAD-SIMPLE problems where you don't "need" it,
so the principle is naked.

The transmutation structure in one line: the physics gets EQUAL weight per DECADE of scale, down
to an exponentially small scale (Lambda, or the gap, or eps below). A UNIFORM grid spends its
resolution evenly in the LINEAR variable -> wastes it at large scales, starves the small ones,
needs ~1/eps points to reach the bottom. A LOGARITHMIC grid spends one unit per decade -> matches
the equal-per-decade structure -> reaches the bottom in ~log(1/eps) points. That is Wilson's NRG,
and it is exactly the resolution the moment/positivity bootstrap (which truncates UNIFORMLY) lacks.
"""
import numpy as np


# ===== Problem A (trivial): integral of 1/x, the canonical "equal weight per decade" object =====
# exact:  int_eps^1 dx/x = log(1/eps).
def uniform_midpoint(eps, N):
    x = eps + (1 - eps) * (np.arange(N) + 0.5) / N        # N uniform midpoints on [eps,1]
    return np.sum((1 - eps) / N / x)


def geometric_trapz(eps, N):
    # N+1 points log-spaced from eps to 1; trapezoid. (1/x dx = d log x, so this is ~exact for any N.)
    lx = np.linspace(np.log(eps), 0.0, N + 1)
    x = np.exp(lx)
    f = 1.0 / x
    return float(np.sum(0.5 * (f[1:] + f[:-1]) * np.diff(x)))   # manual trapezoid (numpy-2 safe)


def problemA():
    print("Problem A:  int_eps^1 dx/x = log(1/eps).  Uniform grid vs LOG (geometric) grid.")
    print("  eps      exact     | uniform N=20   N=2000   N=200000 | geometric N=8   N=20")
    for eps in (1e-2, 1e-4, 1e-6):
        ex = np.log(1 / eps)
        u20, u2k, u2e5 = uniform_midpoint(eps, 20), uniform_midpoint(eps, 2000), uniform_midpoint(eps, 200000)
        g8, g20 = geometric_trapz(eps, 8), geometric_trapz(eps, 20)
        print(f"  {eps:.0e}  {ex:7.3f}  | {u20:8.3f} {u2k:8.3f} {u2e5:9.3f} | {g8:9.3f} {g20:8.3f}")
    print("  => UNIFORM needs N ~ 1/eps to get the log right (resolution wasted up high, starved")
    print("     down low). GEOMETRIC (one point per decade) is ~exact with N ~ log(1/eps) points.\n")


# ===== Problem B (the connection): to 'find' a scale at r=xi you must PROBE at r~xi =====
def problemB():
    print("Problem B:  a gap m lives at scale r ~ xi = 1/m. To detect it you must probe out to r~xi.")
    print("  Probes needed to REACH scale xi:   uniform set {1,2,...,R}: R = xi ;   log set {1,2,4,...,2^K}: K = log2(xi)")
    print("  m (gap)     xi=1/m     uniform probes ~xi     log probes ~log2(xi)")
    for m in (0.1, 0.01, 1e-3, 1e-4, 1e-6):
        xi = 1 / m
        print(f"  {m:.0e}    {xi:10.0f}     {xi:12.0f}          {np.log2(xi):6.1f}")
    print("  => the moment bootstrap used UNIFORM moments G(0..R) -> needed R ~ xi (exponential in beta).")
    print("     LOG-spaced probes reach the same scale in ~log(xi) -- linearly many DECADES. That is the")
    print("     Wilson/NRG resolution, and why an RG crosses the transmutation gap where the bootstrap can't.\n")


# ===== Problem C (one notch of 'RG'): doubling/decimation reaches scale 2^K in K steps =====
def problemC():
    print("Problem C (the RG flavor): a decimation step that DOUBLES the length scale each iteration")
    print("  reaches correlation length xi in K = log2(xi) steps (vs xi single-site steps).")
    print("  This is the iterative content of log discretization: each step = one decade of scale.")
    for xi in (8, 64, 1024, 2**20):
        print(f"   xi={xi:>8}:  single-site steps = {xi:>8}   |   doubling (RG) steps = {int(np.log2(xi)):>3}")
    print()


if __name__ == "__main__":
    print("=" * 86)
    print("Logarithmic discretization, illustrated on trivial problems (you don't need it -> you SEE it)")
    print("=" * 86 + "\n")
    problemA()
    problemB()
    problemC()
    print("THE POINT: dimensional transmutation puts the physics 'equal per decade' down to an")
    print("exponentially small scale. Match the discretization to that structure (logarithmic / RG)")
    print("and you reach it in linearly-many decades; use a uniform grid (or a uniform bootstrap")
    print("truncation) and you need exponentially many points. Same problem, opposite cost.")
