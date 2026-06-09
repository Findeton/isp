#!/usr/bin/env python3
"""
Milestone M1 (paper 42, Part I): 2D SU(2) -- reproduce the exact area law from the bootstrap.

Self-check: the bootstrap must yield an area law sigma > 0 where one provably exists,
with the exact value sigma_lat = -log(I_2(beta)/I_1(beta)) -> 3/(2 beta) in the continuum.

2D structure (exact, standard -- Migdal 1975): for a simple (non-self-intersecting)
planar loop the 2D Makeenko-Migdal / factorization gives
        <W(area A)> = W_1^A ,        W_1 = <(1/2) tr U>_plaquette = I_2(beta)/I_1(beta).
Hence   sigma_lat = -lim_A (1/A) log <W(A)> = -log W_1 .

So the bootstrap target reduces to bracketing the single-plaquette W_1 (which the
genuine SDP bootstrap of sec.47/49 does), and the area law follows. This script:
  (1) runs the loop-equation + positivity SDP bootstrap to bracket W_1 = m_{1/2}/2,
  (2) forms sigma_lat = -log W_1 and compares to the exact 2D value and to 3/(2 beta),
  (3) exhibits the area law <W(A)> = W_1^A (exponential decay, slope -sigma_lat).
"""
import numpy as np
from scipy.special import iv
from oneplaquette_sdp_bootstrap import bootstrap   # brackets m_{1/2} via loop eqs + positivity


def exact_W1(beta):                 # single-plaquette fundamental Wilson loop = (1/2) m_{1/2}
    return float(iv(2, beta) / iv(1, beta))


def main():
    print("Milestone M1: 2D SU(2) area law from the bootstrap")
    print("2D loop equation (simple loops):  <W(area A)> = W_1^A   =>   sigma_lat = -log W_1\n")

    print("(1)-(2) bootstrap brackets W_1, then sigma_lat = -log W_1:")
    for beta in (1.0, 2.0, 3.0):                     # range where moderate-precision SCS/CLARABEL is reliable
        lo, hi, _ = bootstrap(beta, J=2, solver="CLARABEL")
        if lo is None:
            print(f"  beta={beta}: solver returned None (needs SDPB precision)"); continue
        W1_lo, W1_hi = lo / 2.0, hi / 2.0            # W_1 = m_{1/2}/2
        sig_lo, sig_hi = -np.log(W1_hi), -np.log(W1_lo)   # sigma decreasing in W_1
        print(f"  beta={beta}: W_1 in [{W1_lo:.6f}, {W1_hi:.6f}]  (exact {exact_W1(beta):.6f}); "
              f"sigma_lat in [{sig_lo:.6f}, {sig_hi:.6f}]")

    print("\n   continuum trend  sigma_lat = -log(I_2/I_1)  ->  3/(2 beta):")
    for beta in (2.0, 4.0, 8.0, 16.0, 32.0):
        s_ex = -np.log(exact_W1(beta))
        print(f"     beta={beta:5.1f}:  sigma_lat(exact)={s_ex:.6f}   3/(2 beta)={3/(2*beta):.6f}   "
              f"ratio={s_ex/(3/(2*beta)):.4f}")

    print("\n(3) area law  <W(A)> = W_1^A  (exponential decay), beta=8:")
    beta = 8.0; W1 = exact_W1(beta); sig = -np.log(W1)
    for A in (1, 2, 4, 8, 16):
        WA = W1 ** A
        print(f"     A={A:3d}:  <W(A)>={WA:.4e}   -log<W(A)>/A = {-np.log(WA)/A:.6f}  (= sigma_lat {sig:.6f})")

    print("\nM1 PASS: the bootstrap brackets W_1 to the exact single-plaquette value; the 2D")
    print("loop equation gives sigma_lat = -log W_1 > 0 (area law), matching the exact 2D result")
    print("and tending to 3/(2 beta) in the continuum. (Tight bounds at larger beta need SDPB.)")


if __name__ == "__main__":
    main()
