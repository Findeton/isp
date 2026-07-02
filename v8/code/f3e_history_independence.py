"""
v7 Paper 1 — f3e: the two dense-step premises (b1) single channel and (b2) stationarity,
and the product-limit forcing of the exponential.

The dense-regime step S(chi1+chi2)=S(chi1)S(chi2) needs survival S to be a function of
ACCUMULATED CONTENT ALONE. This splits into TWO logically distinct conditions:

  (b1) SINGLE coherence channel: collapses the Chapman-Kolmogorov MATRIX composition to a
       SCALAR (kills inter-channel cross-terms). FORCED by the q=2 one-contrast screen of
       section 3.1 (one off-diagonal => one scalar channel).
  (b2) STATIONARITY / translation-invariance: the per-content contraction is the SAME at
       every location along the commit order. A SEPARATE premise -- even a single channel
       fails multiplicativity if its contraction varies with content-location. Supplied by
       the screen being the SAME q=2 one-contrast object at each seal.

Given (a) dense seals + (b1) + (b2), the exponential is forced WITHOUT assuming the finite
per-step law is already exponential: lim_m (f(chi/m))^m = exp(chi*(log f)'(0)) for ANY
stationary per-step contraction f.

Pre-geometric: all quantities are record-internal probabilities / |amplitude| ratios; no
spacetime, metric, light cone, or s^2. High precision: mpmath dps=120.
"""
import mpmath as mp
mp.mp.dps = 120

print("=" * 74)
print("F3e  dense-step premises (b1) single-channel + (b2) stationarity   [dps=%d]" % mp.mp.dps)
print("=" * 74)

# --- single scalar channel, STATIONARY: multiplicative ---------------------------------
r = mp.mpf('0.8')
n1, n2 = 3, 4
g1 = r ** (n1 + n2) - r ** n1 * r ** n2
print("(0) single stationary channel:  S(n1+n2) - S(n1)S(n2) = %s  (multiplicative)" % mp.nstr(g1, 3))

# --- (b1) MULTI-channel with mixing: scalar survival is history-dependent --------------
M = mp.matrix([[mp.mpf('0.85'), mp.mpf('0.10')],
               [mp.mpf('0.05'), mp.mpf('0.60')]])
w = mp.matrix([[1], [1]])

def Mpow(k):
    R = mp.eye(2)
    for _ in range(k):
        R = M * R
    return R

def surv(v, k):
    Mv = Mpow(k) * v
    return abs((w.T * Mv)[0]) / abs((w.T * v)[0])

vA = mp.matrix([[1], [0]]); vB = mp.matrix([[0], [1]]); k = 4
sA, sB = surv(vA, k), surv(vB, k)
gap_b1 = abs(sA - sB)
print("(b1) multi-channel survival of same %d-step stretch: A=%s  B=%s" % (k, mp.nstr(sA, 6), mp.nstr(sB, 6)))
print("     history-dependence gap = %s  => NOT content-only without a single channel" % mp.nstr(gap_b1, 4))

# --- (b2) single channel but NON-stationary contraction: multiplicativity fails --------
# step-1 contraction r1, step-2 contraction r2 (r1 != r2): same content per step, different rate.
r1, r2 = mp.mpf('0.9'), mp.mpf('0.7')
S_two = r1 * r2                 # survival of two steps
S_one_sq = r1 * r1             # (survival of one step)^2 -- the multiplicative prediction
gap_b2 = abs(S_one_sq - S_two)
print("(b2) single NON-stationary channel: S(1)*S(1)=%s vs S(2)=%s,  gap = %s" %
      (mp.nstr(S_one_sq, 4), mp.nstr(S_two, 4), mp.nstr(gap_b2, 4)))
print("     => even ONE channel breaks multiplicativity if the contraction varies with location")

# --- product limit: (a)+(b1)+(b2) force exp for ANY stationary per-step law f -----------
# f(x) = 1/(1+x)  (NOT exponential).  (log f)'(0) = -1  =>  lim_m f(chi/m)^m = exp(-chi).
chi = mp.mpf('1')
def f(x): return 1 / (1 + x)
vals = [(f(chi / m)) ** m for m in [10, 100, 1000, 100000]]
print("(prod) f=1/(1+x) (non-exponential): (f(chi/m))^m for m=10,100,1000,1e5:")
for m, v in zip([10, 100, 1000, 100000], vals):
    print("        m=%-7d -> %s" % (m, mp.nstr(v, 8)))
print("        target exp(-chi) = %s   |limit - exp| ~ %s" %
      (mp.nstr(mp.e ** (-chi), 8), mp.nstr(abs(vals[-1] - mp.e ** (-chi)), 3)))

assert abs(g1) < mp.mpf(10) ** (-100)
assert gap_b1 > mp.mpf('0.01') and gap_b2 > mp.mpf('0.01')
assert abs(vals[-1] - mp.e ** (-chi)) < mp.mpf('1e-4')

print()
print("CONCLUSION:")
print(" (b1) the SINGLE-channel (matrix->scalar) half IS forced by the q=2 one-contrast")
print("      screen of section 3.1 (gap %s above for a multi-channel screen);" % mp.nstr(gap_b1, 3))
print(" (b2) the STATIONARITY half is a SEPARATE premise (gap %s for a non-stationary" % mp.nstr(gap_b2, 3))
print("      single channel), supplied by the screen being the same q=2 contrast at each seal;")
print(" given (a)+(b1)+(b2), the product limit forces exp for ANY stationary per-step law.")
print("=" * 74)
print("DONE.  (no spacetime / metric / s^2 used)")
print("=" * 74)
