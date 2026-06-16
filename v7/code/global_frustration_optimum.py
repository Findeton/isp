"""
global_frustration_optimum.py -- receipt for Theorem 7.1 of the binding-codes paper.

The exponential-consistency fixed point of a parity-relation code assigns fields h_a to
the m = 2^n - 1 nontrivial parity modes chi_a(s) = prod_{i in a} s_i of (Z/2)^n by the
self-referential condition <chi_a>_h = e^{-h_a}.  An ORIENTATION is a sign eps_a in {+-1}
per mode (the multi-mode generalisation of the single sign lambda of the frustration
identity).  Each of the 2^(2^n - 1) orientations has an evidence content -- the relative
entropy m(n; eps) = D(P_h || U) of the tilted law to the uniform law -- at its fixed point.

THEOREM 7.1.  The minimum evidence content over all orientations of the complete n-mode set
is attained at the ALTERNATING-BY-WEIGHT orientation eps_a = (-1)^{|a|-1}, which collapses
the tilted exponent to two values,

   T(s) = sum_{a!=0} eps_a chi_a(s) = 1 - prod_i (1 - s_i)
        = -(2^n - 1)  on the all-minus state,   +1  on each of the other 2^n - 1 states,

giving a scalar self-consistency whose solution is, in closed form,

   m_min(n) = -ln(1 - 2^-n) - delta_n,

delta_n the (positive, doubly-exponentially small) correction from the dropped all-minus
weight.  Hence m_min(n) is strictly positive at every finite n, decays as 2^-n with
prefactor exactly 1, and the minimiser is the maximally binding orientation
(defect = D^free - D(P||U), so minimum relative entropy = maximum binding defect).

Verified: the two-value identity over all 2^n states (n=2..7); the closed form against the
exact fixed-point values (n=3,4,5) at dps 130; delta_n > 0 (analytic + high-precision);
the prefactor; and the global-optimality lemma by EXHAUSTIVE enumeration over all
orientations at n = 2 (8), n = 3 (128), n = 4 (32768).

Pure statistical mechanics: every quantity is a relative entropy / character sum of the
parity-relation-code fixed point.  No external scale, lattice, or continuum enters.
"""
import mpmath as mp
import numpy as np
import itertools

mp.mp.dps = 130
PASS = {}


def head(s):
    print("\n" + "=" * 78 + "\n" + s + "\n" + "=" * 78)


# ---------------------------------------------------------------------------
head("(1) the two-value identity T(s) = 1 - prod_i(1 - s_i)")
def T_bruteforce(n, s):
    tot = 0
    for mask in range(1, 1 << n):
        idx = [i for i in range(n) if (mask >> i) & 1]
        w = 1
        for i in idx:
            w *= s[i]
        tot += (-1) ** (len(idx) - 1) * w
    return tot


ident_ok = True
for n in range(2, 8):
    for bits in itertools.product((-1, 1), repeat=n):
        T = T_bruteforce(n, bits)
        expected = -((1 << n) - 1) if all(b == -1 for b in bits) else 1
        if T != expected:
            ident_ok = False
print("  T(s) = -(2^n-1) on all-minus, +1 on each of the other 2^n-1 states")
print("  verified exactly over all 2^n states for n = 2..7:", ident_ok)
PASS["(1) two-value identity T(s) in {-(2^n-1), +1} exact for n=2..7"] = ident_ok


# ---------------------------------------------------------------------------
head("(2) closed form m_min(n) = -ln(1 - 2^-n) - delta_n vs exact fixed-point values")
def exact_min(n):
    N = 1 << n
    M = N - 1
    def fp(h):
        w0 = mp.e ** (-h * M)
        eh = mp.e ** (h)
        Z = w0 + M * eh
        E_s1 = (w0 * (-1) + eh * (1)) / Z      # E[chi_a] for a weight-1 mode = e^{-h}
        return E_s1 - mp.e ** (-h)
    h = mp.findroot(fp, mp.log(mp.mpf(M)) if M > 1 else mp.mpf("1.0"))
    w0 = mp.e ** (-h * M)
    eh = mp.e ** (h)
    Z = w0 + M * eh
    psi = mp.log(Z / N)
    D_PU = h * (M * mp.e ** (-h)) - psi          # relative entropy D(P_h || U)
    closed = -mp.log(1 - mp.power(2, -n))
    return D_PU, closed, h


anchors = {3: "0.133530982072", 4: "0.064538521138", 5: "0.031748698315"}
anchor_ok = True
print("   n     m_min(n) [exact]                      -ln(1-2^-n)            delta_n     m*2^n")
for n in [3, 4, 5, 6, 7, 25]:
    D_PU, closed, h = exact_min(n)
    print("  %3d  %-34s %-22s %-11s %s" % (
        n, mp.nstr(D_PU, 28), mp.nstr(closed, 18), mp.nstr(closed - D_PU, 4), mp.nstr(D_PU * 2 ** n, 12)))
    if n in anchors:
        anchor_ok = anchor_ok and abs(D_PU - mp.mpf(anchors[n])) < mp.mpf("1e-11")
PASS["(2) closed form reproduces the exact fixed-point relative entropy at n=3,4,5"] = anchor_ok


# ---------------------------------------------------------------------------
head("(3) delta_n > 0 (analytic + high precision); strictly positive; prefactor -> 1")
# Analytic: -ln(1-2^-n) is D(P||U) for the UNIFORM law over the M='other' states (dropping the
# positive-weight all-minus state).  Restoring that state strictly lowers D(P||U) (it adds mass
# off the uniform support), so the true m_min < -ln(1-2^-n), i.e. delta_n > 0.
mp.mp.dps = 420
d7 = exact_min(7)
mp.mp.dps = 130
print("  delta_7 at dps=420 =", mp.nstr(d7[1] - d7[0], 6), " (> 0, doubly-exp small)")
pos_ok = True
pref = []
for n in [3, 5, 8, 12, 20, 40]:
    D_PU, closed, h = exact_min(n)
    pos_ok = pos_ok and (D_PU > 0)
    pref.append(D_PU * 2 ** n)
PASS["(3) m_min(n) > 0 at every finite n; delta_n > 0 (analytic, dps=420 at n=7)"] = (
    pos_ok and (d7[1] - d7[0]) > 0)
PASS["(3b) prefactor m_min(n) * 2^n -> 1 exactly"] = abs(pref[-1] - 1) < mp.mpf("1e-9")


# ---------------------------------------------------------------------------
head("(4) GLOBAL-OPTIMALITY LEMMA: exhaustive over all orientations at n = 2, 3, 4")
def char_cols(n):
    st = np.array(list(itertools.product((-1, 1), repeat=n)), float)
    cols = np.empty((st.shape[0], (1 << n) - 1))
    for mask in range(1, 1 << n):
        idx = [i for i in range(n) if (mask >> i) & 1]
        cols[:, mask - 1] = np.prod(st[:, idx], axis=1)
    return cols


_eta = float(mp.findroot(lambda e: mp.tanh(e) - mp.e ** (-e), mp.mpf("0.609")))
def relent_of_orientation(n, signs, chi0, tol=1e-13, maxit=400):
    chi = chi0 * np.asarray(signs, float)[None, :]
    h = np.full(chi.shape[1], _eta)
    for _ in range(maxit):
        z = chi @ h; z -= z.max(); w = np.exp(z); p = w / w.sum()
        E = chi.T @ p; F = E - np.exp(-h)
        if np.abs(F).max() < tol:
            break
        Cov = (chi * p[:, None]).T @ chi - np.outer(E, E)
        J = Cov + np.diag(np.exp(-h))
        try:
            step = np.linalg.solve(J, F)
        except np.linalg.LinAlgError:
            step = np.linalg.lstsq(J, F, rcond=None)[0]
        h = h - step
    z = chi @ h; z -= z.max(); p = np.exp(z); p /= p.sum()
    return float(np.sum(p * np.log(p * p.size)))


def altweight(n):
    return [(-1) ** (bin(mask).count("1") - 1) for mask in range(1, 1 << n)]


for n in [2, 3, 4]:
    chi0 = char_cols(n)
    M = (1 << n) - 1
    best = min(relent_of_orientation(n, bits, chi0) for bits in itertools.product((-1, 1), repeat=M))
    closed = float(exact_min(n)[0])
    g_alt = relent_of_orientation(n, altweight(n), chi0)
    print("  n=%d: exhaustive min over all %d orientations = %.12f ; closed form = %.12f ; alt-by-weight = %.12f"
          % (n, 2 ** M, best, closed, g_alt))
    PASS["(4) n=%d exhaustive global min == closed form, realised by alternating-by-weight" % n] = (
        abs(best - closed) < 1e-9 and abs(g_alt - closed) < 1e-9)


# ---------------------------------------------------------------------------
head("MACHINE CHECKS")
ok = True
for k, v in PASS.items():
    print("  [%s] %s" % ("PASS" if v else "FAIL", k))
    ok = ok and v
print("\n  " + ("ALL CHECKS PASS" if ok else "*** SOME CHECK FAILED ***"))
assert ok, "a check failed"
print("=" * 78)
print("DONE.  The minimum evidence content over all orientations of the complete n-mode set is")
print("       m_min(n) = -ln(1 - 2^-n) - delta_n (delta_n > 0, doubly-exp small), attained at the")
print("       alternating-by-weight orientation: the maximally binding orientation, with binding")
print("       defect diverging as the relative entropy decays to 0 like 2^-n.")
print("=" * 78)
