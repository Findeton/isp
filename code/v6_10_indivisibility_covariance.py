"""
v6 §10: does INDIVISIBILITY (the one ISP-specific lever, §1.1) clear the interacting-QFT covariance residue?

§10 is the covariance residue: does the relativistic ISP reconstruction stay Lorentz-invariant for INTERACTING
fields? The free case exists (Tumulka rGRWf 2006); the interacting case is the long-standing open problem in
relativistic collapse models. Its single most concrete obstruction is the ENERGY-PRODUCTION DIVERGENCE:
white (Markovian) collapse noise coupled to a quantum field injects energy at ALL frequencies, giving a
UV-divergent heating rate (Pearle's relativistic CSL; "fixed" only by Bedingham 2011 mediating-field smearing
or Adler-Bassi colored noise). This is exactly the §1.1 "energy non-conservation killer."

The ISP lever: indivisibility = NON-MARKOVIANITY = a FINITE noise correlation time tau_c (the same tau_c that
turns paper1/v5p2 gravitational decoherence into a Gaussian onset). A finite-memory noise has a noise power
spectrum S(omega) that DECAYS at high frequency, so it cannot excite arbitrarily high field modes. Question:
does the indivisible correlation make the interacting heating rate FINITE and CUTOFF-INDEPENDENT (genuinely
regulated, not just milder)?

Heating rate of a 3D relativistic (massless) scalar field coupled to collapse noise:
   dE/dt  ~  integral d^3k  omega_k  S(omega_k)  =  integral_0^Lambda  omega^2 * omega * S(omega) d omega
          =  integral_0^Lambda  omega^3 S(omega) d omega          [d^3k = 4pi omega^2 d omega, energy ~ omega]
White noise S=1 => ~ Lambda^4 (quartic UV divergence). The regulator is the spectral shape S(omega).
"""
import numpy as np

tau = 1.0                                              # noise correlation time (indivisibility memory scale)
def H(S, Lam, ngrid=200000):
    w = np.linspace(1e-6, Lam, ngrid)
    return np.trapezoid(w**3 * S(w), w)                # heating rate up to cutoff Lambda

spectra = {
    "white  (Markovian, S=1)":                  lambda w: np.ones_like(w),
    "OU/exp-correlation (Lorentzian S)":        lambda w: 1.0/(1.0 + (w*tau)**2),
    "indivisible/smooth (Gaussian S)":          lambda w: np.exp(-(w*tau)**2),
}
expected = {  # analytic large-Lambda behaviour of  ∫ w^3 S dw
    "white  (Markovian, S=1)":           "~ Lambda^4   (quartic divergence)",
    "OU/exp-correlation (Lorentzian S)": "~ Lambda^2   (quadratic divergence -- milder, still divergent)",
    "indivisible/smooth (Gaussian S)":   "-> 1/(2 tau^4)  (FINITE, cutoff-independent)",
}

print("="*90)
print("§10 probe: interacting heating rate  dE/dt ~ INT_0^Lambda omega^3 S(omega) d omega")
print(f"            does indivisibility (finite tau_c={tau}) regulate the relativistic-collapse divergence?")
print("="*90)
Lams = [10, 20, 40, 80]
print(f"   {'noise spectrum':<38} " + "".join(f"{'H(L='+str(L)+')':>12}" for L in Lams) + f"{'H(2L)/H(L)':>12}")
for name, S in spectra.items():
    vals = [H(S, L) for L in Lams]
    ratio = vals[-1]/vals[-2]                          # doubling Lambda: ->16 quartic, ->4 quadratic, ->1 finite
    print(f"   {name:<38} " + "".join(f"{v:>12.3g}" for v in vals) + f"{ratio:>12.2f}")
print("\n   doubling-ratio H(2L)/H(L):  16 = quartic (white), 4 = quadratic (OU), ~1 = CONVERGED (indivisible).")

# cutoff-independence (the real test) + the finite Gaussian value vs analytic 1/(2 tau^4)
Hg = H(spectra["indivisible/smooth (Gaussian S)"], 200.0)
print(f"\n   Gaussian (indivisible) heating at huge Lambda=200:  H = {Hg:.5f}   analytic 1/(2 tau^4) = {1/(2*tau**4):.5f}")
print(f"   => Lambda-INDEPENDENT (genuinely finite), set by the correlation time tau_c, not the cutoff.")

# how the finite value scales with the memory time tau (the indivisibility scale)
print("\n   finite heating vs correlation time tau (Gaussian/indivisible):")
for t in [0.5, 1.0, 2.0]:
    Sg = (lambda tt: (lambda w: np.exp(-(w*tt)**2)))(t)
    print(f"     tau={t}:  H = {H(Sg, 200.0):.4f}   (analytic 1/(2 tau^4) = {1/(2*t**4):.4f})  => slower noise = less heating")

print("\n" + "="*90); print("VERDICT (§10)"); print("="*90)
print("- White (Markovian) noise: H ~ Lambda^4, DIVERGES -- the relativistic-CSL energy catastrophe (KILL).")
print("- OU / exponential-correlation (Lorentzian spectrum): H ~ Lambda^2, still DIVERGES in 3D -- 'colored'")
print("  alone is NOT enough; the regulator must be SMOOTH (faster-than-power-law spectral decay).")
print("- Indivisible / smooth (Gaussian spectrum): H -> 1/(2 tau^4), FINITE and CUTOFF-INDEPENDENT. The")
print("  finite-memory, smooth correlation -- exactly the tau_c the ISP indivisibility lever supplies (and the")
print("  same Gaussian structure as paper1/v5p2's decoherence onset) -- removes the energy divergence.")
print("- SCOPE (honest): this clears the ENERGY/heating facet of §10 (one §1.1 killer) and shows indivisibility")
print("  supplies the precise regulator, with a sharp condition (smooth, not merely colored, correlation). It")
print("  does NOT construct the full interacting Lorentz-covariant process: the residual open core is")
print("  Tomonaga-Schwinger INTEGRABILITY (frame-independent evolution between arbitrary spacelike slices) of")
print("  the indivisible interacting reconstruction -- the genuinely analytic problem, not closed numerically.")
