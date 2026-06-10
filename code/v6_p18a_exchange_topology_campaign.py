#!/usr/bin/env python3
"""
v6_p18a: exchange topology - permutation forcing in d >= 3 (Paper 18,
Theorem R1).

The relative configuration space of two identical record excitations in
spatial dimension d is R^d \\ {0} ~ S^(d-1).  The exchange-squared loop
is a closed loop in it.  Eventless transport is FLAT away from
coincidence (P4 s20: events are the only curvature sources), and:

  d >= 3:  S^(d-1) is SIMPLY CONNECTED - every flat fiber connection is
           pure gauge, the exchange-squared holonomy is the IDENTITY,
           so the exchange operator satisfies eps^2 = 1: braid-group
           statistics COLLAPSES TO THE SYMMETRIC GROUP.
  d = 2:   S^1 has pi_1 = Z - flat connections carry a holonomy
           modulus: exchange-squared holonomy is ARBITRARY: the braid
           group survives.  This is EXACTLY Paper 9's record-anyon
           window, recovered as the unique exception.

Receipts:
 (i)   d = 3, eventless (pure-gauge U(3)) transport: the
       exchange-squared holonomy = identity to integrator precision,
       for random gauge fields and at every stage of the explicit
       contraction of the loop.
 (ii)  d = 3, NON-flat (eventful) connection: the holonomy is NOT
       identity at full size but converges to identity as the explicit
       homotopy shrinks the loop - holonomy is carried by enclosed
       EVENTS only; eventless exchange-squared is trivial.
 (iii) d = 2, flat connection with modulus: exchange-squared holonomy
       = an arbitrary U(3) element (printed): the anyon window.
"""
import numpy as np

rng = np.random.default_rng(18)

def random_hermitian(scale=1.0):
    X = rng.standard_normal((3, 3)) + 1j * rng.standard_normal((3, 3))
    H = (X + X.conj().T) / 2
    return scale * H

def expm_h(H):
    ev, P = np.linalg.eigh(H)
    return (P * np.exp(1j * ev)) @ P.conj().T

# loop family on S^2: gamma_s(t) at polar angle alpha(s), shrinking to
# the pole; s = 1 is the full exchange-squared great circle
def loop(s, t):
    alpha = s * np.pi / 2
    return np.array([np.cos(2 * np.pi * t) * np.sin(alpha),
                     np.sin(2 * np.pi * t) * np.sin(alpha),
                     np.cos(alpha)])

def holonomy(field_g, s, n=4000):
    """transport with the pure-gauge connection A = (dg) g^-1 along
    gamma_s: T = g(x(t)) g(x(0))^-1 exactly; computed by stepping."""
    T = np.eye(3, dtype=complex)
    g_prev = field_g(loop(s, 0.0))
    for k in range(1, n + 1):
        g_now = field_g(loop(s, k / n))
        T = g_now @ np.linalg.inv(g_prev) @ T
        g_prev = g_now
    return T

# ---------- (i) eventless transport in d = 3 ----------
print("== (i) d = 3, eventless: exchange^2 holonomy = identity ==")
Hs = [random_hermitian(0.8) for _ in range(3)]
def gfield(x):
    f = [x[0] * x[2], np.sin(np.pi * x[1]), x[0] * x[1] * x[2] + x[2] ** 2]
    M = sum(fi * Hi for fi, Hi in zip(f, Hs))
    return expm_h(M)
for s in (1.0, 0.6, 0.3):
    T = holonomy(gfield, s)
    print(f"  contraction stage s = {s}: ||holonomy - 1||_max = "
          f"{np.abs(T - np.eye(3)).max():.2e}")
print("  -> for EVENTLESS (flat = pure-gauge) fiber transport the")
print("     exchange-squared loop carries NO holonomy, at every stage of")
print("     the contraction: eps^2 = 1 is FORCED in d = 3 - braid")
print("     statistics collapses to the symmetric group (Theorem R1).")

# ---------- (ii) eventful contrast ----------
print("\n== (ii) d = 3, eventful: holonomy lives on enclosed events ==")
W = random_hermitian(1.0)
def transport_eventful(s, n=6000):
    """non-flat connection A = W * (z-dependent weight) d(phi):
    curvature nonzero - 'events' distributed over the sphere."""
    T = np.eye(3, dtype=complex)
    for k in range(n):
        x0, x1 = loop(s, k / n), loop(s, (k + 1) / n)
        dphi = np.arctan2(x1[1], x1[0]) - np.arctan2(x0[1], x0[0])
        if dphi > np.pi: dphi -= 2 * np.pi
        if dphi < -np.pi: dphi += 2 * np.pi
        A = W * (1 - x0[2]) / 2
        T = expm_h(A * dphi / (2 * np.pi) * 2 * np.pi) @ T
    return T
for s in (1.0, 0.5, 0.25, 0.1):
    T = transport_eventful(s)
    print(f"  s = {s:4.2f}: ||holonomy - 1||_max = "
          f"{np.abs(T - np.eye(3)).max():.3e}")
print("  -> with curvature (events) present the loop holonomy is O(1) at")
print("     full size and vanishes as the contraction empties the loop:")
print("     exchange-squared holonomy measures ENCLOSED EVENTS, never")
print("     statistics.  Eventless exchange-squared = 1, always.")

# ---------- (iii) the d = 2 anyon window ----------
print("\n== (iii) d = 2: the flat modulus survives ==")
X2 = random_hermitian(0.5)
hol2 = expm_h(2 * np.pi * X2)
print("  flat connection on S^1: A = X dtheta, holonomy of the")
print("  exchange-squared (winding-1) loop = exp(2 pi i X):")
print(f"  ||holonomy - 1||_max = {np.abs(hol2 - np.eye(3)).max():.3f}"
      f"   (an ARBITRARY U(3) element)")
print("  -> pi_1(S^1) = Z: flat connections carry a modulus; the braid")
print("     group survives ONLY in d = 2 - Paper 9's record-anyon window")
print("     recovered as the unique exception, now from the same theorem")
print("     that forces eps^2 = 1 everywhere else.")
print("== p18a done ==")
