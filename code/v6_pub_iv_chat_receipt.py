# v6 publishable Paper IV receipt: de-circularized (ratio) detector + N-refinement.
#
# Referee point IV.5: the windowed detector s(x,t) = K(x,t) sqrt(4 pi c(x) t) - 1 - g(c(x) t)
# uses the TRUE c(x) in its own normalization -- circular if c is what you are probing.
# Naive fix (estimate c_hat from K at the smallest window time) FAILS by construction:
# the detector then vanishes at that time and the decay fit measures the vanishing, not
# the roughness (recorded 2026-06-11: alpha_hat pinned at the cap).
#
# Honest fix: the RATIO detector
#   s_lam(x,t) = K(x, lam t) sqrt(lam) (1+g(c_hat(x) t)) / ( K(x,t) (1+g(c_hat(x) lam t)) ) - 1
# In the continuum flat model K = 1/sqrt(4 pi c t), so the c-dependence cancels exactly;
# c_hat enters only inside the lattice correction g (|g| small, smooth), where its
# O(t^{alpha/2}) estimation error is harmless. Same windowed exponent: sup_x |s_lam| ~ t^{alpha/2}
# at a c-roughness exponent alpha; smooth c gives rate ~ 1 (the t^1 windowed regime).
#
# Canonical: /tmp/v6_pub_iv_chat.out  (bit-identical rerun required)

import numpy as np

rng = np.random.default_rng(323)
LAM = 4.0
T_BASE = np.geomspace(2.5e-4, 1.5e-3, 5)


def make(N):
    h = 1.0 / N
    X = np.arange(N) * h

    def operator(c):
        ce = 0.5 * (c + np.roll(c, -1))
        L = np.zeros((N, N))
        idx = np.arange(N)
        jdx = (idx + 1) % N
        L[idx, idx] += ce
        L[jdx, jdx] += ce
        L[idx, jdx] -= ce
        L[jdx, idx] -= ce
        return L / (h * h)

    def heat(c, ts):
        lam, V = np.linalg.eigh(operator(c))
        return [((V * V) * np.exp(-t * lam)[None, :]).sum(1) / h for t in ts]

    return X, heat


def rate(sups, ts):
    A = np.vstack([np.log(ts), np.ones(len(ts))]).T
    return float(np.linalg.lstsq(A, np.log(sups), rcond=None)[0][0])


def run(N):
    X, heat = make(N)
    # flat-lattice correction g(s): K_flat(s) sqrt(4 pi s) = 1 + g(s)  (c=1 baseline; for
    # constant c the discrete kernel at time t equals the flat kernel at time ct exactly)
    SG = np.geomspace(0.1 * T_BASE[0], 8 * LAM * T_BASE[-1], 80)
    g_vals = np.array([float(K[0] * np.sqrt(4 * np.pi * s) - 1.0)
                       for K, s in zip(heat(np.ones(N), SG), SG)])

    def gb(s):
        return np.interp(np.log(s), np.log(SG), g_vals)

    def ratio_detector(c):
        ts = list(T_BASE) + list(LAM * T_BASE)
        Ks = heat(c, ts)
        Kb, Kl = Ks[:len(T_BASE)], Ks[len(T_BASE):]
        # crude c_hat from the smallest time -- used ONLY inside g
        t0 = T_BASE[0]
        c_hat = 1.0 / (4 * np.pi * t0 * Kb[0] ** 2)
        c_hat = c_hat * (1 + gb(c_hat * t0)) ** 2
        sups = []
        for K1, K2, t in zip(Kb, Kl, T_BASE):
            s = K2 * np.sqrt(LAM) * (1 + gb(c_hat * t)) / (K1 * (1 + gb(c_hat * LAM * t))) - 1.0
            sups.append(float(np.abs(s).max()))
        return sups

    print(f"N={N}: ratio detector (lam={LAM:g}), c_hat used only in lattice correction")
    for alpha in (0.5, 1.0):
        rates = []
        for _ in range(3):
            x0 = float(rng.uniform(0.1, 0.9))
            eta = float(rng.uniform(0.4, 1.0))
            d = np.minimum(np.abs(X - x0), 1 - np.abs(X - x0))
            rates.append(rate(ratio_detector(1.0 + eta * d ** alpha), T_BASE))
        print(f"  alpha={alpha}: rates={['%.3f' % r for r in rates]}  (target {alpha/2:.2f})")
    c = 1.0 + 0.3 * np.sin(2 * np.pi * X) + 0.15 * np.cos(4 * np.pi * X)
    print(f"  smooth control: rate={rate(ratio_detector(c), T_BASE):.3f}  (target ~1)")

    # N-refinement of the ORIGINAL (true-c) detector rates, fixed profiles
    TS = np.geomspace(2.5e-4, 6e-3, 7)

    def det(c, ts):
        Ks = heat(c, ts)
        return [(K * np.sqrt(4 * np.pi * c * t) - 1.0 - gb(c * t)) for K, t in zip(Ks, ts)]

    out = []
    for alpha in (0.5, 1.0):
        d = np.minimum(np.abs(X - 0.5), 1 - np.abs(X - 0.5))
        c = 1.0 + 0.8 * d ** alpha
        out.append(rate([np.abs(r).max() for r in det(c, TS)], TS))
    c = 1.0 + 0.3 * np.sin(2 * np.pi * X) + 0.15 * np.cos(4 * np.pi * X)
    out.append(rate([np.abs(r).max() for r in det(c, TS)], TS))
    print(f"  N-refinement (true-c detector): alpha=0.5/1.0/smooth rates = "
          f"{out[0]:.3f}/{out[1]:.3f}/{out[2]:.3f}")


for N in (512, 768):
    run(N)
