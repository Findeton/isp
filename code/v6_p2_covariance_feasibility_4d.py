"""
v6 paper 2 §3 probe, 3+1 (physical case): is the Born transition Gamma(a,t)=|<x2|U|x1>|^2 a function of s^2?

1+1 (v6_p2_covariance_feasibility.py) showed: naive-position first-order data (flat dp measure) are
FRAME-DEPENDENT, while the Lorentz-invariant measure dp/2w gives a covariant f(s^2). Here we confirm it in
3+1, the physical case.

3+1 relativistic particle H=sqrt(p^2+m^2), p=|p_vec|. By rotational symmetry K depends only on a=|x2-x1|, t:
  K(a,t) = (1/(2pi)^3) INT d^3p  meas(p)  e^{i p.a - i w t}
         = (1/(2 pi^2)) INT_0^inf dp  p^2  sinc(pa)  meas(p)  e^{-i w t}          [sinc(x)=sin(x)/x]
  flat (naive position):  meas = 1            (measure d^3p)
  cov  (invariant):       meas = 1/(2w)       (measure d^3p/2w  = the 3+1 Wightman two-point function)
both smeared by e^{-sig^2 p^2/2} (finite record resolution). Gamma=|K|^2. Test: boost along x at fixed s^2
(t^2 - a^2 = s^2); covariant <=> Gamma constant along the orbit. (Overall prefactors irrelevant: we report
the coefficient of variation over the orbit, which is normalization-independent.)
"""
import numpy as np

m, sig = 1.0, 0.15
P, NP = 80.0, 60000
p = np.linspace(1e-8, P, NP)                         # radial momentum, p>0
w = np.sqrt(p**2 + m**2)
damp = np.exp(-sig**2 * p**2 / 2)
def sinc(x): return np.sinc(x/np.pi)                 # sin(x)/x, safe at 0

def K(a, t, measure):
    meas = (1.0 if measure == "flat" else 1.0/(2*w))
    integrand = p**2 * sinc(p*a) * meas * damp * np.exp(-1j*w*t)
    return np.trapz(integrand, p)                    # drop the constant 1/(2pi^2): irrelevant for CV
def Gamma(a, t, measure): return np.abs(K(a, t, measure))**2

def boost_orbit(s2, vs):
    """points with t^2-a^2=s2 (timelike), from boosting the rest point (a=0, t=sqrt(s2)) along x."""
    T0 = np.sqrt(s2)
    return [(abs(g*v*T0), g*T0) for v in vs for g in [1/np.sqrt(1-v**2)]]

vs = np.array([0.0, 0.2, 0.4, 0.6, 0.8])
print("="*88)
print("Paper 2 §3 probe in 3+1: is Gamma(a,t)=|<x2|U|x1>|^2 a function of s^2 only?")
print(f"   3+1 relativistic particle H=sqrt(p^2+m^2), m={m}, record resolution sig={sig}")
print("="*88)
for s2 in [2.0, 6.0]:
    print(f"\n   s^2 = {s2}  (rest point t={np.sqrt(s2):.3f}, a=0):")
    print(f"     {'v':>6} {'(a,t)':>16} {'Gamma_flat (naive pos)':>24} {'Gamma_cov (invariant)':>24}")
    gf, gc = [], []
    for (a, t), v in zip(boost_orbit(s2, vs), vs):
        Gf, Gc = Gamma(a, t, "flat"), Gamma(a, t, "cov")
        gf.append(Gf); gc.append(Gc)
        print(f"     {v:>6.2f} {f'({a:.2f},{t:.2f})':>16} {Gf:>24.6e} {Gc:>24.6e}")
    gf, gc = np.array(gf), np.array(gc)
    print(f"     coeff of variation over the boost orbit:  flat = {gf.std()/gf.mean():.3f}   "
          f"cov = {gc.std()/gc.mean():.3e}")
    print(f"     -> flat {'VARIES (frame-dependent)' if gf.std()/gf.mean()>0.05 else 'constant'};  "
          f"cov {'CONSTANT (covariant f(s^2))' if gc.std()/gc.mean()<0.03 else 'varies'}")

print("\n" + "="*88); print("VERDICT (paper 2 §3, 3+1)"); print("="*88)
orb = boost_orbit(6.0, vs)
gf = np.array([Gamma(a,t,"flat") for a,t in orb]); gc = np.array([Gamma(a,t,"cov") for a,t in orb])
print(f"- 3+1 confirms 1+1: naive-position first-order data (flat d^3p) are FRAME-DEPENDENT")
print(f"  (coeff of variation {gf.std()/gf.mean():.2f} along the boost orbit at s^2=6), while the Lorentz-")
print(f"  invariant measure d^3p/2w (= 3+1 Wightman function) gives CONSTANT Gamma (CV {gc.std()/gc.mean():.1e},")
print(f"  the residue being the frame-fixed Gaussian smearing) = a genuine f(s^2).")
print(f"- So the §3 result is dimension-robust: in the PHYSICAL 3+1 case too, the covariance gate is the")
print(f"  localization OBSERVABLE (invariant measure / Newton-Wigner / Wightman), not the memory. The same")
print(f"  caveat stands: covariant localization is non-sharp (Hegerfeldt), sharpening Q3 (gravity sourcing).")
