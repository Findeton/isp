#!/usr/bin/env python3
"""
v6_p30f: the isolation scaling (CPE campaign, final probe).

p30e showed: the p30c depth-5 witness dies at depth 8, but a band
around G = I still carries clock strength through depth 12.  The
decisive structural question for the reduced system:

   Is all-depth feasibility ISOLATED at the normal point G = I
   (every G != I with coupling dies at some finite alternation
   depth, with a death depth scaling like 1/eps), or does an open
   band survive all depths?

 (i)   BAND WINNERS: at fixed off-diagonal distance eps from G = I,
       maximize clock strength r under adversary positivity at
       depths <= 12 (as p30e), KEEPING the winning parameters.
 (ii)  DEATH DEPTHS: take each winner to depths 16-64 with the exact
       coordinate-descent adversary: first negative depth k*(eps).
       Scaling receipt: k* vs 1/eps.
 (iii) THE DEEPENING TREND at eps = 0.05: re-optimize r with the
       constraint set deepened to K = 12, 24, 48: the sequence
       r_max(K).  Decay toward 0 = isolation-to-zero (the CPE
       mechanism at reduced level); a positive plateau = a genuine
       all-depth band (CPE would then rest entirely on the letter-
       level exclusion).
"""
import numpy as np

rng = np.random.default_rng(306)
sig = np.array([0.0, 1.0, -1.0])

def build(p):
    g, dr, di, b0, br, bi = p
    delta = dr + 1j * di
    G = np.array([[1.0, g, g],
                  [g, 1.0, delta],
                  [g, np.conj(delta), 1.0]])
    beta = np.array([b0, br + 1j * bi, br - 1j * bi])
    return G, beta

def reduced(p):
    G, beta = build(p)
    if np.linalg.eigvalsh(G)[0] < 1e-8:
        return None
    H = np.linalg.inv(G)
    alpha = H @ beta
    c = np.conj(alpha) * beta
    c0 = c[0].real
    if c0 <= 1e-12:
        return None
    return G, H, alpha, beta, c0, 2 * abs(c[1]) / c0

def chain_value(phis, G, H, alpha, beta):
    row = np.exp(1j * phis[0] * sig) * np.conj(alpha)
    k = len(phis)
    for j in range(2, k + 1):
        row = row @ (G if j % 2 == 0 else H)
        sgn = -1.0 if j % 2 == 0 else 1.0
        row = row * np.exp(1j * sgn * phis[j - 1] * sig)
    end = alpha if k % 2 == 0 else beta
    return float((row @ end).real)

def adversary(depth, G, H, alpha, beta, arng, starts=6):
    best = np.inf
    for _ in range(starts):
        ph = arng.uniform(0, 2 * np.pi, depth)
        cur = chain_value(ph, G, H, alpha, beta)
        for sweep in range(80):
            improved = False
            for j in range(depth):
                keep = ph[j]
                vals = []
                for t in (0.0, np.pi, np.pi / 2):
                    ph[j] = t
                    vals.append(chain_value(ph, G, H, alpha, beta))
                a = (vals[0] + vals[1]) / 2
                w = (vals[0] - vals[1]) / 2 + 1j * (a - vals[2])
                if abs(w) < 1e-15:
                    ph[j] = keep
                    continue
                ph[j] = np.pi - np.angle(w)
                newv = a - abs(w)
                if newv < cur - 1e-13:
                    cur = newv
                    improved = True
            if not improved:
                break
        best = min(best, cur)
    return best

def worst_margin(p, depths, arng, starts=4):
    red = reduced(p)
    if red is None:
        return None
    G, H, alpha, beta, c0, r = red
    wm = (c0 - 2 * abs((np.conj(alpha) * beta)[1])) / c0
    for d in depths:
        wm = min(wm, adversary(d, G, H, alpha, beta, arng, starts) / c0)
        if wm < -1e-9:
            break
    return wm, r

def band_optimize(eps, depths, arng, restarts=3, steps=400, warm=None):
    best_r, best_p = -1.0, None
    sz0 = max(eps / 3, 0.02)
    for rs in range(restarts):
        if warm is not None and rs == 0:
            p = warm.copy()
        else:
            p = np.array([eps, eps / 2, 0.0, np.sqrt(2.0), 1.0, 0.0]) \
                + sz0 * arng.standard_normal(6)
        cur, sz = -1e18, sz0
        for k in range(steps):
            q = p + sz * arng.standard_normal(6)
            dist = max(abs(q[0]), abs(q[1] + 1j * q[2]))
            sz = max(sz * 0.997, 0.015)
            if not (0.7 * eps <= dist <= 1.3 * eps):
                continue
            out = worst_margin(q, depths, arng)
            if out is None:
                continue
            wm, r = out
            sc = r - 80 * max(0.0, -wm)
            if sc > cur:
                cur, p = sc, q
                if wm >= -1e-9 and r > best_r:
                    best_r, best_p = r, q.copy()
    return best_r, best_p

# ---------- (i) + (ii): band winners and their death depths ----------
print("== (i/ii) band winners and their death depths ==")
D12 = (2, 3, 4, 5, 8, 12)
DEEP = (16, 20, 24, 32, 40, 48, 64)
print("   eps    dist     r(<=12)   death depth k*")
death = {}
winners = {}
for eps in (0.05, 0.15, 0.30):
    r, p = band_optimize(eps, D12, rng)
    if p is None:
        print(f"   {eps:.2f}   -        none feasible at depth 12")
        continue
    winners[eps] = p
    dist = max(abs(p[0]), abs(p[1] + 1j * p[2]))
    red = reduced(p)
    G, H, alpha, beta, c0, _ = red
    kstar = None
    for k in DEEP:
        m = adversary(k, G, H, alpha, beta, rng, starts=8) / c0
        if m < -1e-9:
            kstar = k
            break
    death[eps] = (r, kstar)
    ks = str(kstar) if kstar else ">64"
    print(f"   {eps:.2f}   {dist:.3f}    {r:.4f}    {ks:>6s}")
if death and all(v[1] is not None for v in death.values()):
    print("  -> every depth-12 band winner found here dies at finite")
    print("     depth (the shape of ISOLATION at this budget).")
elif death:
    print("  -> MIXED: some winners die at finite depth, at least")
    print("     one survives the deepest adversary probe (64 phases,")
    print("     8 restarts).  Either the local adversary misses the")
    print("     killing phase pattern at this budget, or the")
    print("     all-depth feasible set is genuinely a band off the")
    print("     normal point: (ISO) is OPEN, evidence mixed -")
    print("     reported exactly as measured.")

# ---------- (iii) the deepening trend ----------
print("\n== (iii) the deepening trend at eps = 0.05"
      " (warm-started at the band winner) ==")
print("   constraint depth K     max feasible r")
warm = winners.get(0.05)
trend = {}
for K, depths in [(12, (3, 5, 8, 12)),
                  (32, (3, 5, 8, 16, 32)),
                  (56, (3, 5, 8, 16, 32, 56))]:
    r, p = band_optimize(0.05, depths, rng, restarts=3,
                         steps=300 if K > 12 else 400, warm=warm)
    trend[K] = r
    print(f"     {K:2d}                    {r:.4f}")
rs = [trend[k] for k in (12, 32, 56)]
kstar05 = death.get(0.05, (None, None))[1]
print(f"  (the specific eps = 0.05 winner above died at k* ="
      f" {kstar05};")
print("   the trend re-optimizes within the shell at each K, so it")
print("   measures the SHELL's best survivor, not that one point)")
print(f"  trend: {rs[0]:.3f} -> {rs[1]:.3f} -> {rs[2]:.3f}")
if rs[-1] < 0.0:
    print("  -> the shell is EXTINGUISHED at depth K = 56: isolation")
    print("     at this distance, live.")
elif rs[-1] < 0.6 * rs[0]:
    print("  -> r_max decays strongly with constraint depth;")
    print("     consistent with isolation at finite depth per shell.")
else:
    print("  -> r_max declines only mildly through K = 56: the shell")
    print("     retains strong feasible coupling at every depth this")
    print("     search reaches.  Combined with the mixed death-depth")
    print("     table: the reduced-level evidence does NOT settle")
    print("     (ISO).  If the band is real, the spectral half of")
    print("     (CPE) rests entirely on the letter-level exclusion")
    print("     (NR + the trade-off wall), which is independently")
    print("     receipted; if the adversary is the bottleneck, a")
    print("     global phase-optimization (SOS over the torus) is")
    print("     the named next tool.  Reported exactly as measured.")
print("== p30f done ==")
