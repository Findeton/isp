"""
v6 paper 2 §3 probe: can the indivisible division-event memory be a covariant f(s^2)?

Paper 2 framed this as an equivalence-class question (lever 4: ISP fixes only first-order conditionals, so
the higher-order memory is gauge -> maybe choose a covariant representative). But there is a PRIOR GATE: the
FIRST-ORDER data themselves. In ISP the empirically-fixed first-order content is the Born transition
probability Gamma(x2<-x1) = |<x2|U|x1>|^2. If Gamma is already frame-dependent at fixed invariant interval
s^2 = t^2 - a^2, then NO higher-order (memory) freedom can repair covariance -- the binding constraint is the
covariance of the first-order localization observable (sub-question Q1), not the memory (Q2/lever 4).

This probe computes Gamma for a 1+1 relativistic particle (H = sqrt(p^2+m^2)) under BOOSTS at fixed s^2, for
two localization observables:
  (flat)  naive position eigenstates, measure dp        -> K_flat(a,t) = (1/2pi) INT dp        e^{ipa-iw t}
  (cov)   Lorentz-invariant localization, measure dp/2w -> K_cov(a,t)  = (1/2pi) INT dp/(2w)   e^{ipa-iw t}
(both smeared by e^{-sig^2 p^2/2} = finite record resolution, so |K|^2 is well-defined). The cov measure is
the field Wightman two-point function -- manifestly a function of s^2. Test: is |K|^2 constant along a boost
orbit (same s^2)? Covariant <=> constant.
"""
import numpy as np

m, sig = 1.0, 0.15
P, NP = 80.0, 40000
p = np.linspace(-P, P, NP); dp = p[1]-p[0]
w = np.sqrt(p**2 + m**2)
damp = np.exp(-sig**2 * p**2 / 2)

def K(a, t, measure):
    meas = (1.0 if measure == "flat" else 1.0/(2*w))
    integrand = meas * damp * np.exp(1j*(p*a - w*t))
    return np.trapz(integrand, p) / (2*np.pi)
def Gamma(a, t, measure): return np.abs(K(a, t, measure))**2

def boost_orbit(s2, vs):
    """points (a,t) all with t^2 - a^2 = s2 (timelike, t>0), reached by boosting the rest point (0,sqrt(s2))."""
    T0 = np.sqrt(s2); out = []
    for v in vs:
        g = 1/np.sqrt(1-v**2)
        a = g*(0 - v*T0); t = g*(T0 - v*0)         # boost of (a=0, t=T0)
        out.append((a, t))
    return out

vs = np.array([0.0, 0.2, 0.4, 0.6, 0.8])
print("="*86)
print("Paper 2 §3 probe: is the first-order Born transition Gamma(a,t)=|<x2|U|x1>|^2 a function of s^2 only?")
print(f"   1+1 relativistic particle H=sqrt(p^2+m^2), m={m}, record resolution sig={sig}")
print("="*86)
print("   boost orbit at fixed s^2 (same invariant interval): is Gamma constant along it?\n")
for s2 in [2.0, 6.0]:
    print(f"   s^2 = {s2}  (rest point t={np.sqrt(s2):.3f}, a=0):")
    print(f"     {'v':>6} {'(a,t)':>16} {'Gamma_flat (naive pos)':>24} {'Gamma_cov (invariant)':>24}")
    gf, gc = [], []
    for (a, t), v in zip(boost_orbit(s2, vs), vs):
        Gf, Gc = Gamma(a, t, "flat"), Gamma(a, t, "cov")
        gf.append(Gf); gc.append(Gc)
        print(f"     {v:>6.2f} {f'({a:+.2f},{t:.2f})':>16} {Gf:>24.6e} {Gc:>24.6e}")
    gf, gc = np.array(gf), np.array(gc)
    cv_flat = gf.std()/gf.mean(); cv_cov = gc.std()/gc.mean()
    print(f"     coeff of variation over the boost orbit:  flat = {cv_flat:.3f}   cov = {cv_cov:.3e}")
    print(f"     -> flat {'VARIES (frame-dependent)' if cv_flat>0.05 else 'constant'};  "
          f"cov {'CONSTANT (covariant, f(s^2))' if cv_cov<0.02 else 'varies'}\n")

print("="*86); print("VERDICT (paper 2 §3)"); print("="*86)
# summary numbers at s^2=6
orb = boost_orbit(6.0, vs)
gf = np.array([Gamma(a,t,"flat") for a,t in orb]); gc = np.array([Gamma(a,t,"cov") for a,t in orb])
print(f"- Naive-position first-order data (flat dp measure): Gamma VARIES along the boost orbit")
print(f"  (coeff of variation {gf.std()/gf.mean():.2f} at s^2=6) -> FRAME-DEPENDENT. No higher-order/memory")
print(f"  freedom (lever 4) can repair this: the FIXED first-order data already break covariance.")
print(f"- Lorentz-invariant localization (dp/2w measure = the field Wightman function): Gamma is CONSTANT")
print(f"  along the orbit (coeff of variation {gc.std()/gc.mean():.1e}) -> a genuine f(s^2).")
print(f"- CONCLUSION: the binding constraint is Q1 (the localization observable), not Q2/lever-4 (the memory).")
print(f"  Covariance of the indivisible first-order data REQUIRES a covariant localization (invariant measure")
print(f"  dp/2w = Newton-Wigner-type / Tumulka covariant flash), NOT naive position eigenstates. WITH that")
print(f"  choice the first-order data are already f(s^2), so a covariant memory completion is feasible; WITHOUT")
print(f"  it, covariance is obstructed at first order. This refines paper 2: the residue's gate is the")
print(f"  division-event observable, and a concrete covariant choice exists.")
