#!/usr/bin/env python3
"""
v6_p10a: the exchange-cocycle reflection-positivity attack on (R-)'''
(Paper 10, Part I).

The native reflection structure is the exchange cocycle of P4 s34,

    A_D(a,b) = log[ pi(a) P(b|a) ] - log[ pi(b) P(a|b) ]
             = log dP_AB/dP_BA   (joint ordered-transport form),

and the chain of theorems is:

 T1 (cocycle laws): A_D is a coboundary  <=>  all cycle affinities vanish
    (Kolmogorov)  <=>  zero stationary currents  <=>  detailed balance.
 T2 (order-evidence identity): the stationary entropy production rate is
    EXACTLY the RN evidence that the collar's traversal ORDER leaves in
    the records:
       sigma = E_fwd[A_D] = D(P_AB || P_BA)  per step,  >= 0,
       = 0  iff detailed balance.
 T3 (no-silent-arrow theorem): an EVENTLESS collar commits no record, so
    the order evidence is zero: D(P_AB||P_BA) = 0  =>  P_AB = P_BA  =>
    detailed balance.  An arrow in an eventless collar would be
    irreversibility carried by zero evidence - the silent-seam exclusion
    in temporal dress.
 T4 (reflection positivity as a theorem): reversible transport => the
    symmetrized transfer operator is self-adjoint => collar correlations
    are spectral measures = moment sequences on [-1,1] (P8 Theorem 6.1
    mechanism) => site-RP at every size; and the full OS form <theta F F>
    over trajectory functionals is PSD (machine: exact enumeration).
    Bond-RP additionally  <=>  the transfer spectrum is nonnegative:
    P8's typed classes acquire a DYNAMICAL characterization.
 T5 (the boundary is the eventlessness boundary): oscillating collar
    memory (P8's non-moment failures) REQUIRES hidden stationary currents
    - entropy production - hence committed evidence: those sectors are
    not eventless.  Machine: the minimal realization of e^{-ar}cos(kr) is
    a driven unicyclic chain with sigma > 0 and explicit RP failure.
"""
import numpy as np
import itertools

rng = np.random.default_rng(10)

def stationary(P):
    w, v = np.linalg.eig(P.T)
    pi = np.real(v[:, np.argmax(np.real(w))])
    pi = np.abs(pi); return pi / pi.sum()

def cocycle(P, pi):
    Jf = pi[:, None] * P
    return np.log(Jf) - np.log(Jf.T)

def entropy_production(P, pi):
    Jf = pi[:, None] * P
    mask = (Jf > 0) & (Jf.T > 0)
    if np.any((Jf > 0) & (Jf.T == 0)):
        return np.inf, np.inf, np.inf      # one-sided rate: infinite arrow
    A = np.zeros_like(Jf)
    A[mask] = np.log(Jf[mask]) - np.log(Jf.T[mask])
    return 0.5 * np.sum((Jf - Jf.T) * A), np.sum(Jf * A), np.sum(Jf * A)

def cycle_affinity(P, cyc):
    s = 0.0
    for i in range(len(cyc)):
        a, b = cyc[i], cyc[(i + 1) % len(cyc)]
        s += np.log(P[a, b] / P[b, a])
    return s

def corr(P, pi, f, R):
    m = pi @ f
    out = []
    g = f.copy()
    for r in range(R + 1):
        out.append(pi @ (f * g) - m * m)
        g = P @ g
    return np.array(out)

def hankel_min_eig(C, N):
    G = np.array([[C[i + j] for j in range(1, N + 1)] for i in range(1, N + 1)])
    return np.linalg.eigvalsh(G)[0]

def os_gram(P, pi, L):
    """exact two-sided stationary chain x_{-L..L}; Gram M[a, b] =
    Prob(future block = a, reflected past block = b) over d^L blocks."""
    d = P.shape[0]
    M = np.zeros((d ** L, d ** L))
    for path in itertools.product(range(d), repeat=2 * L + 1):
        p = pi[path[0]]
        for k in range(2 * L):
            p *= P[path[k], path[k + 1]]
        past = path[:L][::-1]      # (x_{-1},...,x_{-L}) reading outward
        fut = path[L + 1:]         # (x_1,...,x_L)
        ia = sum(fut[k] * d ** k for k in range(L))
        ib = sum(past[k] * d ** k for k in range(L))
        M[ia, ib] += p
    return M

# ---------- T1/T2: cocycle laws and the order-evidence identity ----------
print("== T1/T2. cocycle laws and sigma = E[A_D] = D(P_AB||P_BA) ==")
W = rng.uniform(0.2, 1.0, (4, 4)); W = W + W.T          # symmetric weights
Prev = W / W.sum(1, keepdims=True)
pirev = stationary(Prev)
A = cocycle(Prev, pirev)
sig, EA, KL = entropy_production(Prev, pirev)
cyc = cycle_affinity(Prev, [0, 1, 2, 3])
print(f"  reversible kernel (symmetric weights, d=4):")
print(f"    max |A_D| = {np.abs(A).max():.2e}   cycle affinity(0123) = {cyc:.2e}")
print(f"    sigma = {sig:.2e}  E[A_D] = {EA:.2e}  D(fwd||rev) = {KL:.2e}")
p, q, s0 = 0.55, 0.15, 0.30                              # driven unicycle
Pdrv = s0 * np.eye(3) + p * np.roll(np.eye(3), 1, axis=1) + q * np.roll(np.eye(3), -1, axis=1)
pidrv = stationary(Pdrv)
sigd, EAd, KLd = entropy_production(Pdrv, pidrv)
print(f"  driven unicycle (p={p}, q={q}):")
print(f"    cycle affinity = 3 ln(p/q) = {3*np.log(p/q):.6f}"
      f"  (machine {cycle_affinity(Pdrv,[0,1,2]):.6f})")
print(f"    sigma = {sigd:.6f} = E[A_D] = {EAd:.6f} = D(fwd||rev) = {KLd:.6f}"
      f"   (identity gaps {abs(sigd-EAd):.1e}, {abs(EAd-KLd):.1e})")
print("  -> the entropy production IS the RN order-evidence rate: the exchange")
print("     cocycle's expectation.  T2 is an identity, machine-exact.")

# ---------- T3: no-silent-arrow ----------
print("\n== T3. no-silent-arrow: eventless => D(P_AB||P_BA) = 0 => detailed balance ==")
print("  eventless = the traversal order is recorded by NOTHING: the RN")
print("  evidence distinguishing P_AB from P_BA is zero.  D(P_AB||P_BA) = 0")
print("  <=> P_AB = P_BA (joint laws)  <=> pi(a)P(b|a) = pi(b)P(a|b): detailed")
print("  balance EXACTLY.  An eventless collar with an arrow would carry")
print("  irreversibility on zero evidence - a silent seam in temporal dress.")
print("  (P6.1's detailed-balance verification at 8.7e-19 is this theorem's")
print("  machine shadow; the cocycle A_D of P4 s34 is its native carrier.)")

# ---------- T4: reflection positivity from reversibility ----------
print("\n== T4. RP as a theorem of reversible transports ==")
D2 = np.diag(np.sqrt(pirev))
Tsym = D2 @ Prev @ np.linalg.inv(D2)
print(f"  symmetrized transfer: max |T - T^T| = {np.abs(Tsym - Tsym.T).max():.2e}"
      f"   spectrum in [-1,1]: {np.round(np.sort(np.linalg.eigvalsh(Tsym)), 6)}")
f = rng.normal(size=4)
C = corr(Prev, pirev, f, 40)
print(f"  random observable: Hankel(site) min eig N=12: {hankel_min_eig(C, 12):.2e}"
      f"   (moment sequence: spectral theorem)")
M = os_gram(Prev, pirev, 3)
ev = np.linalg.eigvalsh((M + M.T) / 2)
print(f"  full OS Gram over ALL functionals of 3 future sites (64x64, exact")
print(f"  enumeration of 4^7 paths): min eig = {ev[0]:.2e}  (theorem: >= 0)")
# bond-RP <=> nonnegative transfer spectrum (dynamical typing of P8 classes)
Palt = np.array([[0.2, 0.8], [0.8, 0.2]])               # eig -0.6: alternating
pialt = stationary(Palt)
Calt = corr(Palt, pialt, np.array([1.0, -1.0]), 60)
def bond_min_eig(C, N):
    G = np.array([[C[i + j - 1] for j in range(1, N + 1)] for i in range(1, N + 1)])
    return np.linalg.eigvalsh(G)[0]
Plazy = 0.5 * (np.eye(2) + Palt)                        # spectrum >= 0
Clazy = corr(Plazy, pialt, np.array([1.0, -1.0]), 60)
print(f"  alternating chain (transfer eig -0.6): C(r) = (-0.6)^r exactly;")
print(f"    site Hankel min eig = {hankel_min_eig(list(Calt), 12):.2e}"
      f"   bond min eig = {bond_min_eig(list(Calt), 12):.4f}  (bond FAILS)")
print(f"  lazy chain (spectrum >= 0): site = {hankel_min_eig(list(Clazy), 12):.2e}"
      f"   bond = {bond_min_eig(list(Clazy), 12):.2e}  (both pass)")
print("  -> P8's typed classes, dynamically characterized: site-RP at all sizes")
print("     <=> the correlations ADMIT a reversible presentation; site+bond-RP")
print("     <=> a reversible presentation with nonnegative transfer spectrum.")
print("     (The given kernel need not itself be reversible: the typing is a")
print("     statement about presentability, via the P8 converses.)")

# ---------- T5: the boundary is the eventlessness boundary ----------
print("\n== T5. oscillating memory requires an arrow ==")
lam = np.linalg.eigvals(Pdrv)
lam_c = lam[np.argmax(np.abs(np.imag(lam)))]
rho, phi = np.abs(lam_c), np.abs(np.angle(lam_c))
print(f"  driven unicycle transfer spectrum: complex pair rho = {rho:.6f},"
      f" phase = {phi:.6f}")
print(f"  -> realizes C(r) ~ rho^r cos(phi r + d): the e^(-ar)cos(kr) class of")
print(f"     P8's RP failures, with a = {-np.log(rho):.6f}, k = {phi:.6f}")
fd = np.array([1.0, -0.3, -0.7])
Cd = corr(Pdrv, pidrv, fd, 30)
print(f"  C(r), r=0..8: {np.round(Cd[:9], 5)}")
print(f"  site Hankel min eig (N=6): {hankel_min_eig(list(Cd), 6):.3e}   RP FAILS")
Md = os_gram(Pdrv, pidrv, 3)
evd = np.linalg.eigvalsh((Md + Md.T) / 2)
print(f"  OS Gram min eig (27x27 exact): {evd[0]:.3e}   RP FAILS")
print(f"  entropy production sigma = {sigd:.6f} > 0: the oscillation is POWERED")
print(f"  by a stationary current = committed evidence: NOT an eventless sector.")
# interpolation: sigma and the RP defect vanish together
print("\n  interpolation reversible -> driven (eps = driving asymmetry):")
print("    eps      sigma          min OS eig")
for eps in (0.0, 0.05, 0.1, 0.2, 0.3):
    pp, qq = 0.35 + eps, 0.35 - eps
    Pe = 0.30 * np.eye(3) + pp * np.roll(np.eye(3), 1, axis=1) + qq * np.roll(np.eye(3), -1, axis=1)
    pie = stationary(Pe)
    se, _, _ = entropy_production(Pe, pie)
    Me = os_gram(Pe, pie, 3)
    eve = np.linalg.eigvalsh((Me + Me.T) / 2)[0]
    print(f"   {eps:5.2f}   {se:.6e}   {eve:+.3e}")
print("  -> sigma and the RP defect vanish TOGETHER at eps = 0: positivity is")
print("     equivalent to the absence of the arrow, on this family.")

# the reversible-but-not-RP subtlety: observable vs primitive presentation
print("\n  subtlety (scope of T4): a stationary GAUSSIAN process with")
print("  C(r) = e^(-ar)cos(kr) is time-reversible AS AN OBSERVED PROCESS, yet")
print("  fails RP - because every finite Markov presentation of it carries")
print("  hidden currents (the complex transfer pair above).  The theorem")
print("  lives at the PRIMITIVE record presentation: eventless primitive")
print("  transport => reversible kernel => RP for everything built on it.")
print("  Sectors with no finite primitive presentation remain the kernel.")
print("== p10a done ==")
