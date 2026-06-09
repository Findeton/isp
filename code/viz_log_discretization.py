#!/usr/bin/env python3
"""
Visualization of WHY logarithmic discretization beats uniform when the physics lives at an
exponentially small scale (dimensional transmutation). Saves log_discretization.png.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def uniform_midpoint(eps, N):
    x = eps + (1 - eps) * (np.arange(N) + 0.5) / N
    return np.sum((1 - eps) / N / x)


def geometric_trapz(eps, N):
    x = np.exp(np.linspace(np.log(eps), 0.0, N + 1))
    f = 1.0 / x
    return float(np.sum(0.5 * (f[1:] + f[:-1]) * np.diff(x)))


fig, ax = plt.subplots(2, 2, figsize=(13, 10))
fig.suptitle("Logarithmic vs uniform discretization: reaching an exponentially small scale",
             fontsize=14, fontweight="bold")

# ---- (A) the integrand 1/x and where each grid puts its points ----
a = ax[0, 0]
eps = 1e-4
xs = np.logspace(np.log10(eps), 0, 600)
a.loglog(xs, 1 / xs, "k-", lw=1.5, label="integrand 1/x")
xu = eps + (1 - eps) * (np.arange(20) + 0.5) / 20          # 20 uniform points
a.loglog(xu, 1 / xu, "rv", ms=7, label="20 UNIFORM points")
xg = np.exp(np.linspace(np.log(eps), 0, 9))                # 9 log points
a.loglog(xg, 1 / xg, "bo", ms=7, label="9 LOG points")
a.axvspan(eps, 1 / 20, color="red", alpha=0.08)
a.text(np.sqrt(eps / 20), 3, "uniform grid BLIND here\n(below its spacing 1/20)",
       color="red", ha="center", fontsize=9)
a.set_xlabel("x  (scale)"); a.set_ylabel("1/x")
a.set_title("(A) Equal weight per DECADE: 1/x.\nUniform points all sit at large x; log points cover every decade")
a.legend(loc="upper right", fontsize=8); a.grid(alpha=0.3, which="both")

# ---- (B) convergence: error of the integral vs number of points ----
b = ax[0, 1]
eps = 1e-6
exact = np.log(1 / eps)
Ns = np.unique(np.logspace(0.5, 6.3, 40).astype(int))
eu = [abs(uniform_midpoint(eps, n) - exact) / exact for n in Ns]
eg = [abs(geometric_trapz(eps, n) - exact) / exact for n in Ns]
b.loglog(Ns, eu, "rv-", ms=4, label="uniform")
b.loglog(Ns, eg, "bo-", ms=4, label="logarithmic")
b.axvline(np.log(1 / eps), color="b", ls=":", lw=1); b.text(np.log(1/eps)*1.1, 1e-3, "N~log(1/ε)", color="b", fontsize=8, rotation=90)
b.axvline(1 / eps, color="r", ls=":", lw=1); b.text(1/eps*0.4, 1e-3, "N~1/ε", color="r", fontsize=8, rotation=90)
b.set_xlabel("N  (number of points)"); b.set_ylabel("relative error of ∫dx/x")
b.set_title("(B) Cost to compute log(1/ε), ε=1e-6.\nuniform needs N~1/ε=10⁶;  log needs N~log(1/ε)~14")
b.legend(fontsize=9); b.grid(alpha=0.3, which="both")

# ---- (C) blindness: fixed N=20, shrink the true scale eps ----
c = ax[1, 0]
epss = np.logspace(-1, -8, 30)
inv = 1 / epss
exact_c = np.log(inv)
unif_c = [uniform_midpoint(e, 20) for e in epss]
geom_c = [geometric_trapz(e, 20) for e in epss]
c.semilogx(inv, exact_c, "k-", lw=1.5, label="exact = log(1/ε)")
c.semilogx(inv, unif_c, "rv-", ms=4, label="uniform N=20 (saturates → BLIND)")
c.semilogx(inv, geom_c, "bo-", ms=4, label="logarithmic N=20 (tracks)")
c.set_xlabel("1/ε   (scale separation)"); c.set_ylabel("estimate of log(1/ε)")
c.set_title("(C) Fixed budget N=20: shrink the true scale.\nUniform flatlines (can't see below its grid); log keeps up")
c.legend(fontsize=9); c.grid(alpha=0.3)

# ---- (D) cost to reach correlation length xi (the gap / Step-E / bootstrap point) ----
d = ax[1, 1]
xis = np.logspace(1, 8, 200)
d.loglog(xis, xis, "r-", lw=2, label="uniform (bootstrap reach): ~ ξ")
d.loglog(xis, np.log2(xis), "b-", lw=2, label="logarithmic / RG (Wilson): ~ log₂ξ")
d.set_xlabel("ξ = 1/gap   (correlation length; ξ~e^{2πβ/N} at the crossover)")
d.set_ylabel("resolution units needed to reach ξ")
d.set_title("(D) Resolving the mass gap through the transmutation crossover.\n"
            "bootstrap (uniform) cost explodes; RG (log) cost is linear in decades")
d.legend(fontsize=9); d.grid(alpha=0.3, which="both")

plt.tight_layout(rect=[0, 0, 1, 0.96])
out = "log_discretization.png"
plt.savefig(out, dpi=130)
print("saved", out)
