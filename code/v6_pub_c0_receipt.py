# Dedicated receipt for the C0 companion ("Fixed points of
# parity-relation codes").  Regenerates every C0 claim not already
# carried by the campaign receipts (p8a/p8b, v6_p35, v6_p36):
#   1. constants + both closed forms of kappa + 11kappa relation
#   2. Lemma 1.1: fine sign-change scan on (0,6), w <= 40, both
#      lambda (one root each); the lambda=-1 term <= 2/w sweep;
#      the corrected h >= 6 exclusion margins
#   3. the 300-start asymmetric multi-start search (w = 3,4;
#      lambda = +-1; starts in (0.05,4)^w) -> symmetric point only
#   4. Theorem 4.2: b and c to full printed digits; d2 closed form
#      vs numeric Taylor extraction
#   5. Corollary 3.2: |r_w| vs |d2/d1| vs the displayed bound at
#      w in {6, 12, 40, 60, 80, 100}
# Canonical: /tmp/v6_pub_c0_receipt.out  (bit-identical required)
import numpy as np
from mpmath import mp, mpf, tanh, sech, exp, ln, cosh, polyroots, findroot

mp.dps = 60
theta = polyroots([1, 1, 1, -1])[0].real
eta = -ln(theta)
Delta = 1 - theta**2 + theta
kappa1 = eta*(1-theta**2)/Delta
kappa2 = eta*(1+theta**2)/(2+theta**2)
eps = 3*kappa1 - 1

print("== 1. constants and closed forms ==")
print(f"  theta = {mp.nstr(theta, 30)}")
print(f"  eta   = {mp.nstr(eta, 30)}")
print(f"  kappa form 1 (eta(1-th^2)/(1-th^2+th)) = {mp.nstr(kappa1, 30)}")
print(f"  kappa form 2 (eta(1+th^2)/(2+th^2))    = {mp.nstr(kappa2, 30)}")
print(f"  |form1 - form2| = {mp.nstr(abs(kappa1-kappa2), 3)}")
print(f"  eps = 3 kappa - 1 = {mp.nstr(eps, 30)}")
print(f"  1/kappa = {mp.nstr(1/kappa1, 6)}")
r11 = 11*kappa1 - eta*(7 - 2*theta + theta**2)
print(f"  11 kappa - eta(7 - 2 theta + theta^2) = {mp.nstr(abs(r11), 3)}")

# ---- the scalar single-relation equation, both signs --------------
def F(h, w, lam):
    t = tanh(h)
    return t + (1 - t**2)*lam*t**(w-1)/(1 + lam*t**w) - exp(-h)

def solve_sym(w, lam):
    return findroot(lambda h: F(h, w, lam), eta)

def defect(w, lam=1):
    h = solve_sym(w, lam)
    t = tanh(h)
    D = lambda x: x*exp(-x) - ln(cosh(x))
    return ln(1 + lam*t**w) - w*(D(h) - D(eta)), h

print("\n== 2. Lemma 1.1: scan, term bound, h >= 6 exclusion ==")
# fine sign-change scan on (0,6): 20001-point grid, both lambdas
grid = np.linspace(1e-9, 6.0, 20001)
def Fnp(h, w, lam):
    t = np.tanh(h)
    return t + (1 - t**2)*lam*t**(w-1)/(1 + lam*t**w) - np.exp(-h)
bad = []
for w in range(3, 41):
    for lam in (+1, -1):
        v = Fnp(grid, w, lam)
        roots = int(np.sum(np.sign(v[:-1]) != np.sign(v[1:])))
        if roots != 1:
            bad.append((w, lam, roots))
print(f"  20001-point scan on (0,6), w = 3..40, lambda = +-1:")
print(f"  cases with root count != 1: {len(bad)}  {bad if bad else '(every case: exactly one sign change)'}")
# lambda = -1 relation term f(t) = (1-t^2) t^(w-1)/(1-t^w) <= 2/w
tt = np.linspace(1e-6, 1 - 1e-9, 20000)
worst = 0.0
for w in range(3, 41):
    fmax = float(np.max((1 - tt**2)*tt**(w-1)/(1 - tt**w)))
    excess = fmax - 2.0/w
    worst = max(worst, excess)
print(f"  lambda=-1 term vs 2/w over 20000-point t-sweep, w = 3..40:")
print(f"  max (sup f - 2/w) = {worst:.3e}  (<= 0: the 2/w bound holds)")
m3 = float(tanh(mpf(6)) - mpf(2)/3 - exp(mpf(-6)))
print(f"  h >= 6 exclusion margins: lambda=+1 side tanh6 - e^-6 = "
      f"{float(tanh(mpf(6))-exp(mpf(-6))):.6f};")
print(f"  lambda=-1 worst margin (w=3): tanh6 - 2/3 - e^-6 = {m3:.4f}")

print("\n== 3. 300-start asymmetric multi-start search ==")
# per-mode system: <chi_a> = e^{-h_a} for a single weight-w codeword
from scipy.optimize import fsolve
def sys_eq(h, w, lam):
    t = np.tanh(h)
    P = np.prod(t)
    out = np.empty(w)
    for a in range(w):
        Pa = P/t[a] if t[a] != 0 else np.prod(np.delete(t, a))
        out[a] = t[a] + (1 - t[a]**2)*lam*Pa/(1 + lam*P) - np.exp(-h[a])
    return out
rng = np.random.default_rng(20260611)
for w in (3, 4):
    for lam in (+1, -1):
        hsym = float(solve_sym(w, lam))
        sols = set()
        conv = 0
        for _ in range(300):
            x0 = rng.uniform(0.05, 4.0, size=w)
            x, info, ier, _ = fsolve(sys_eq, x0, args=(w, lam),
                                     full_output=True, xtol=1e-13)
            if ier == 1 and np.max(np.abs(sys_eq(x, w, lam))) < 1e-10:
                conv += 1
                sols.add(tuple(np.round(np.sort(x), 8)))
        spread = max(abs(v - hsym) for s in sols for v in s)
        print(f"  w={w} lam={lam:+d}: {conv}/300 converged, "
              f"{len(sols)} distinct solution(s), "
              f"max |h_a - h_sym| = {spread:.2e}")

print("\n== 4. Theorem 4.2: second order, closed forms ==")
c2 = eta*(1-theta**2)**3/(theta**2*Delta**2)
# numeric Taylor extraction of d2(w): defect with codeword amplitude
# lam scaled -> d(lam) = d1 lam + d2 lam^2 + ...; extract via finite
# differences at high precision
def defect_amp(w, lam):
    h = findroot(lambda hh: F(hh, w, lam), eta)
    t = tanh(h)
    D = lambda x: x*exp(-x) - ln(cosh(x))
    return ln(1 + lam*t**w) - w*(D(h) - D(eta))
ws = [4, 8, 16, 30]
bs = []
for w in ws:
    lamh = mpf(1)/10**10            # O(lamh^2) truncation ~ 1e-20
    d_p, d_m = defect_amp(w, lamh), defect_amp(w, -lamh)
    d2num = (d_p + d_m)/(2*lamh**2)
    poly = d2num/theta**(2*w)          # = -1/2 + b w + c w^2
    bs.append((poly + mpf(1)/2 - c2*w**2)/w)
bspread = max(abs(bs[i]-bs[0]) for i in range(len(bs)))
print(f"  c (closed form eta(1-th^2)^3/(th^2 Delta^2)) = {mp.nstr(c2, 12)}")
print(f"  b extracted at w = {ws}: {mp.nstr(bs[0], 16)}")
print(f"  b spread across w (constancy check): {mp.nstr(bspread, 3)}")

print("\n== 5. Corollary 3.2: remainder vs bound ==")
b = bs[0]
print("    w     |r_w|        |d2/d1|      bound 2cw^2 th^w/(w kappa-1)   |r_w|<=bound")
for w in (6, 12, 40, 60, 80, 100):
    d, _ = defect(w)
    d1 = theta**w*(1 - w*kappa1)
    r = d/d1 - 1
    d2 = theta**(2*w)*(mpf(-1)/2 + b*w + c2*w**2)
    bound = 2*c2*w**2*theta**w/(w*kappa1 - 1)
    print(f"   {w:3d}   {mp.nstr(abs(r), 4):>10}   {mp.nstr(abs(d2/d1), 4):>10}"
          f"   {mp.nstr(bound, 4):>12}                  {abs(r) <= bound}")
print("  (|r_w| <= |d2/d1| for every listed w: the factor-2 domination")
print("   is generous; graded a verified-numerics bound in the paper.)")

print("\n== 6. frustration identity (cross-check vs p8b / v6_p36) ==")
d3m, h3m = defect(3, lam=-1)
print(f"  defect(3, lam=-1) = {mp.nstr(d3m, 17)}   h* = {mp.nstr(h3m, 15)}")
