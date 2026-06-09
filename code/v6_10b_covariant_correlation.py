"""
v6 §10 refinement: are "smoothness (energy-finiteness)" and "Tomonaga-Schwinger integrability (covariance)"
two independent conditions, or two faces of ONE requirement -- a Lorentz-invariant noise correlation?

The §6 probe (v6_10_indivisibility_covariance.py) regulated the heating with a FRAME-FIXED tau_c (a Gaussian
in one frame's time). That is a PREFERRED-FRAME smoothing: it makes the energy finite but is NOT covariant.
The covariant requirement (= the integrability/microcausality demand) is that the correlation depend only on
the invariant interval s^2 = dt^2 - dx^2. Claim: demanding covariance AUTOMATICALLY gives the frame-
independent finite heating -- so smoothness is downstream of integrability, not a separate conditional.

Test: the noise correlation sampled along an inertial worldline of velocity v (proper time tau_p; events
(t,x) = (gamma*tau_p, v*gamma*tau_p)), and its temporal power spectrum S(omega) = FT of C_along(d tau_p).
  (a) frame-fixed Gaussian (NON-covariant): C(dt,dx) = exp(-dt^2/2T^2 - dx^2/2L^2)
  (b) Lorentz-invariant     (covariant):     C(dt,dx) = f(s^2),  s^2 = dt^2 - dx^2
Along an inertial worldline s^2 = tau_p^2 EXACTLY (since gamma^2(1-v^2)=1), so any f(s^2) gives a worldline
correlation INDEPENDENT of v. Compare S(omega) and a heating proxy H = INT omega^3 S(omega) d omega in the
rest frame vs a boosted frame.
"""
import numpy as np

T, L = 1.0, 1.0                         # frame-fixed correlation scales (time, space)
def along(dtau, v, kind):
    g = 1/np.sqrt(1-v**2); dt = g*dtau; dx = v*g*dtau
    if kind == "fixed": return np.exp(-dt**2/(2*T**2) - dx**2/(2*L**2))
    if kind == "inv":   return np.exp(-(dt**2 - dx**2)/(2*T**2))     # f(s^2), s^2 = dt^2 - dx^2

def psd(v, kind, wmax=40, nw=400):
    dtau = np.linspace(-12, 12, 24000)
    C = along(dtau, v, kind)
    w = np.linspace(0.0, wmax, nw)
    S = np.array([np.trapezoid(np.cos(wi*dtau)*C, dtau) for wi in w])
    return w, np.clip(S, 0, None)

def heating(v, kind):
    w, S = psd(v, kind); return np.trapezoid(w**3 * S, w)

print("="*88)
print("§10 refinement: does demanding COVARIANCE (correlation = f(s^2)) make the heating frame-independent?")
print("="*88)
print(f"   {'noise correlation':<34} {'H(rest)':>12} {'H(boost v=0.6)':>15} {'ratio':>8}  covariant?")
for label, kind in [("(a) frame-fixed Gaussian  C(dt,dx)", "fixed"),
                    ("(b) Lorentz-invariant     C(s^2) ", "inv")]:
    Hr, Hb = heating(0.0, kind), heating(0.6, kind)
    ratio = Hb/Hr
    cov = "YES (frame-independent)" if abs(ratio-1) < 0.02 else "NO  (preferred frame)"
    print(f"   {label:<34} {Hr:>12.4f} {Hb:>15.4f} {ratio:>8.3f}  {cov}")

# also show the worldline correlation time vs boost: fixed shrinks (time dilation), invariant is constant
print("\n   effective correlation time along the worldline vs boost v (FWHM-ish of C_along):")
print(f"   {'v':>6} {'fixed':>10} {'invariant':>12}")
for v in [0.0, 0.3, 0.6, 0.85]:
    dtau = np.linspace(-8, 8, 16000)
    def width(kind):
        C = along(dtau, v, kind); C = C/C.max()
        return np.trapezoid(C, dtau)                # integral width (area) ~ correlation time
    print(f"   {v:>6.2f} {width('fixed'):>10.3f} {width('inv'):>12.3f}")

print("\n" + "="*88); print("VERDICT (§10 refinement)"); print("="*88)
print("- The frame-fixed Gaussian regulates the energy but is FRAME-DEPENDENT (ratio != 1): its correlation")
print("  time along a worldline shrinks with boost (time dilation of a preferred-frame clock) -> preferred frame.")
print("- A Lorentz-invariant correlation f(s^2) gives the SAME finite heating in every frame (ratio = 1.000):")
print("  along any inertial worldline s^2 = proper-time^2, so f(s^2) is automatically frame-independent.")
print("- CONCLUSION: smoothness (finiteness) and integrability (covariance) are NOT independent. Demanding the")
print("  correlation be Lorentz-invariant/microcausal (= the integrability requirement) makes it a function of")
print("  s^2 with a single proper-time scale, which delivers the finite, frame-independent heating AS A")
print("  COROLLARY. So establishing interacting Tomonaga-Schwinger integrability would DERIVE the smoothness,")
print("  not add it as a separate conditional. The open problem collapses to ONE object: does the indivisible")
print("  interacting correlation, made covariant (f(s^2)), fall off fast enough -- one question, not two.")
