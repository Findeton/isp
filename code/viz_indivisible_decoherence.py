#!/usr/bin/env python3
"""
The falsifiable discriminator for V5-Paper-2 section 16:
Markovian (Penrose-Diosi) gravitational decoherence is EXPONENTIAL (finite initial slope);
indivisible (non-Markovian / ISP) decoherence is GAUSSIAN at short times (zero initial slope).
Same threshold scale tau_G = hbar/E_G; different onset shape. Saves indivisible_decoherence.png.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

tauG = 1.0  # work in units of the Penrose-Diosi time tau_G = hbar/E_G


def Gamma_markov(T):      # DP: linear exponent  -> exp(-T/tauG)
    return T / tauG


def Gamma_gauss(T):       # maximally indivisible: quadratic -> exp(-1/2 (T/tauG)^2)
    return 0.5 * (T / tauG) ** 2


def Gamma_memory(T, tc):  # exponential memory K(s)=sigma^2 exp(-|s|/tc), sigma^2/hbar^2 = 1
    return tc * tc * (T / tc - 1.0 + np.exp(-T / tc))


fig, ax = plt.subplots(1, 2, figsize=(13, 5.2))
fig.suptitle("Gravitational coherence decay: Markovian (DP) exponential vs indivisible (ISP) Gaussian",
             fontsize=13, fontweight="bold")

# ---- (A) the fit-free discriminator: residual gravitational exponent near T=0 ----
a = ax[0]
T = np.linspace(0, 1.2, 400)
a.plot(T, 0 * T, "k-", lw=2, label="ordinary QM:  L = 0")
a.plot(T, -Gamma_markov(T), "r-", lw=2, label=r"DP / Markov:  $L=-T/\tau_G$  (finite slope)")
a.plot(T, -Gamma_gauss(T), "b-", lw=2, label=r"ISP / indivisible:  $L=-\frac{1}{2}(T/\tau_G)^2$  (zero slope)")
# tangents at origin to make the onset explicit
a.plot(T, -Gamma_markov(T), "r-")
a.plot([0, 0.45], [0, -0.45], "r:", lw=1)   # DP tangent: slope -1
a.plot([0, 0.45], [0, 0.0], "b:", lw=1)     # ISP tangent: slope 0
a.scatter([0], [0], c="k", zorder=5)
a.annotate("finite initial slope\n(= Markovian DP/CSL)", xy=(0.32, -0.32), xytext=(0.45, -0.62),
           color="red", fontsize=9, arrowprops=dict(arrowstyle="->", color="red"))
a.annotate("zero initial slope: Zeno plateau\n(= indivisible ISP)", xy=(0.22, -0.024), xytext=(0.30, 0.10),
           color="blue", fontsize=9, arrowprops=dict(arrowstyle="->", color="blue"))
a.set_xlabel(r"hold time  $T/\tau_G$  (at fixed $E_G$, environment subtracted)")
a.set_ylabel(r"residual gravitational log-coherence  $L(T)=\ln[V/V_{env}]$")
a.set_title("(A) The shape-based onset discriminator\nrate-robust: no absolute-rate fit")
a.legend(loc="lower left", fontsize=8.5); a.grid(alpha=0.3); a.set_ylim(-0.9, 0.25)

# ---- (B) the crossover family: ISP interpolates, DP is the tau_c -> 0 edge ----
b = ax[1]
T2 = np.linspace(0, 3, 400)
b.plot(T2, Gamma_gauss(T2), "b-", lw=2, label=r"pure Gaussian ($\tau_c\!\to\!\infty$, max. indivisible)")
for tc, st in [(0.6, "b--"), (0.2, "b-.")]:
    b.plot(T2, Gamma_memory(T2, tc), st, lw=1.6, label=rf"exp-memory $\tau_c={tc}$ (Gaussian onset $\to$ linear tail)")
b.plot(T2, Gamma_markov(T2), "r-", lw=2, label=r"Markov / DP ($\tau_c\!\to\!0$)")
b.set_xlabel(r"hold time  $T/\tau_G$")
b.set_ylabel(r"decoherence exponent  $\chi(T)=-\ln[C(T)/C(0)]$")
b.set_title("(B) The indivisible family\nquadratic onset, linear tail beyond the record-memory time")
b.legend(loc="upper left", fontsize=8.5); b.grid(alpha=0.3); b.set_ylim(0, 3)

plt.tight_layout(rect=[0, 0, 1, 0.94])
out = "indivisible_decoherence.png"
plt.savefig(out, dpi=130)
print("saved", out)
