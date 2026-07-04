#!/usr/bin/env python3
"""
pB2_walsh_delta_theorem.py — v8 paper 5 §2: the global-optimality THEOREM (all n),
assembly arithmetic + independent small-n base, v8-resident.

What this receipt DOES verify (self-contained, mpmath dps >= 60 / sympy-exact):
  1. The Theorem E standing constants at c0 = 1/60 (safe-rounding direction checked).
  2. The trichotomy constant 3*psi(e^-5) = 2.87871... and psi decreasing on (0,1) (sympy).
  3. The elementary delta bound D_delta < 1/(N-1), analytic + numeric n = 2..14.
  4. The Theorem F assembly arithmetic: both branches strict, all N >= 2.
  5. An INDEPENDENT exhaustive re-solve of the base: every orientation at n = 2 (8)
     and n = 3 (128), fresh Newton solver, delta orbit uniquely minimal with margin.
  6. The equality case at n = 3: all 8 delta orientations share one gap (translation
     covariance), equal to the exhaustive minimum and to the closed form.
  7. Closed-form anchors: direct mu* solve vs -ln(1-2^-n) - delta_n, n = 2..6,
     against the corpus anchors of paper 5 §1.2.
  8. n = 4 cross-check: mu* solve = corpus global minimum 0.0645385211... (the full
     32768-class exhaustion is receipt pD + companion w1; NOT re-run here).

What it does NOT verify (imported, with provenance): the n <= 4 per-orientation
Newton-Kantorovich certificates, the n = 5 complete 176-orbit transversal, the
orbit-partition BFS/Burnside completeness, and Theorems 1/D(D1-D2) themselves —
these live in the companion math paper (shard/papers/paper-XII-walsh-delta.md,
receipts w1-w5) and the route note (isp/external/walsh-delta-gibbs-route.md §6d),
audited by seven independent hostile verifiers, zero falsifications.
"""

import itertools
from mpmath import mp, mpf, exp, log, sqrt, matrix, lu_solve, ln

mp.dps = 60

PASS = 0
FAIL = 0

def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    if ok: PASS += 1
    else: FAIL += 1
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))


# ---------------------------------------------------------------- seal solver
def masks(n):
    return list(range(1, 2 ** n))

def chi_table(n):
    """chi[a][s] = parity character, s and a as bitmasks."""
    N = 2 ** n
    tab = [[0] * N for _ in range(N)]
    for a in range(N):
        for s in range(N):
            tab[a][s] = -1 if bin(a & s).count("1") % 2 else 1
    return tab

def solve_seal(n, eps, chi, dps=60, tol=None):
    """Newton on grad G = E_P[eps_a chi_a] - e^{-h_a} = 0; returns (h, gap)."""
    if tol is None:
        tol = mpf(10) ** (-dps + 12)
    N = 2 ** n
    A = masks(n)
    M = len(A)
    h = [mpf("0.1")] * M
    for _ in range(200):
        # P propto exp(sum_a h_a eps_a chi_a(s))
        expo = [sum(h[i] * eps[i] * chi[A[i]][s] for i in range(M)) for s in range(N)]
        mx = max(expo)
        w = [exp(e - mx) for e in expo]
        Z = sum(w)
        P = [wi / Z for wi in w]
        m = [sum(P[s] * eps[i] * chi[A[i]][s] for s in range(N)) for i in range(M)]
        g = [m[i] - exp(-h[i]) for i in range(M)]
        gn = max(abs(x) for x in g)
        if gn < tol:
            break
        # Hessian: Cov_P(eps_a chi_a, eps_b chi_b) + diag(e^{-h})
        H = matrix(M, M)
        for i in range(M):
            for j in range(i, M):
                ee = sum(P[s] * eps[i] * chi[A[i]][s] * eps[j] * chi[A[j]][s]
                         for s in range(N))
                c = ee - m[i] * m[j]
                H[i, j] = c
                H[j, i] = c
        for i in range(M):
            H[i, i] += exp(-h[i])
        d = lu_solve(H, matrix([-x for x in g]))
        for i in range(M):
            h[i] += d[i]
    # gap = D(P||U) = sum h_a m_a - log( (1/N) sum exp(...) )
    expo = [sum(h[i] * eps[i] * chi[A[i]][s] for i in range(M)) for s in range(N)]
    mx = max(expo)
    lZ = mx + log(sum(exp(e - mx) for e in expo)) - log(N)
    m = None
    w = [exp(e - mx) for e in expo]
    Z = sum(w)
    P = [wi / Z for wi in w]
    gap = sum(P[s] * expo[s] for s in range(N)) - (mx + log(Z / N))
    # equivalently E_P[T_h] - psi; compute as D(P||U) directly for robustness:
    gap = sum(P[s] * log(P[s] * N) for s in range(N))
    return h, gap


# ------------------------------------------------- 1. standing constants (E)
print("CHECK 1: Theorem E standing constants at c0 = 1/60 (safe rounding)")
c0 = mpf(1) / 60
hmin = log(1 / (2 * c0)) / 2          # (1/2) log 30
epsG = mpf("2.5") * sqrt(2 * c0)
hpr = hmin - epsG
psi_half = mpf("0.5") * log(mpf("0.5")) - mpf("0.5") + 1
ok = (hmin > mpf("1.70059") and epsG < mpf("0.45644") and hpr > mpf("1.24416")
      and hmin > 2 * epsG
      and 1 / (60 * psi_half) < mpf("0.108630")
      and 5 / (60 * psi_half) < mpf("0.543149")
      and hpr - 5 / (60 * psi_half) > mpf("0.701014")
      and hpr - 2 * (5 / (60 * psi_half)) > mpf("0.157865"))
check("h_min>1.70059, eps_G<0.45644, h'>1.24416, h_min>2eps_G, dip/shallow/domination bounds",
      ok, f"h_min={float(hmin):.6f} eps_G={float(epsG):.6f} h'={float(hpr):.6f}")

# ------------------------------------------- 2. trichotomy constant + psi mono
print("CHECK 2: trichotomy constant and psi monotone on (0,1)")
psi_e5 = exp(mpf(-5)) * (-5) - exp(mpf(-5)) + 1     # psi(e^-5) = 1 - 6e^-5
K3 = 3 * psi_e5
ok = abs(K3 - 3 * (1 - 6 * exp(mpf(-5)))) < mpf(10) ** -55 and \
     mpf("2.87871") < K3 < mpf("2.87872") and K3 > mpf(64) / 63
check("3*psi(e^-5) = 3(1-6e^-5) = 2.87871... > 64/63", ok, f"K3={float(K3):.6f}")

import sympy as sp
x = sp.symbols("x", positive=True)
psi_sym = x * sp.log(x) - x + 1
dpsi = sp.diff(psi_sym, x)
ok = sp.simplify(dpsi - sp.log(x)) == 0
check("psi'(x) = log x < 0 on (0,1)  [sympy-exact]", ok, "psi decreasing on (0,1)")

# --------------------------------------------------------- 3. the delta bound
print("CHECK 3: delta bound D_delta < 1/(N-1)")
# analytic: -ln(1-x) < x/(1-x) for x in (0,1); x = 1/N gives -ln(1-1/N) < 1/(N-1);
# D_delta = -ln(1-2^-n) - delta_n with delta_n > 0 only strengthens it.
t = sp.symbols("t", positive=True)
f = t / (1 - t) + sp.log(1 - t)          # want f > 0 on (0,1)
ok = sp.simplify(sp.diff(f, t) - t / (1 - t) ** 2) == 0 and f.subs(t, sp.Rational(1, 10 ** 9)) > 0
check("analytic: -ln(1-x) < x/(1-x) on (0,1) (f(0)=0, f'=t/(1-t)^2>0)", ok)
allok = True
for n in range(2, 15):
    N = mpf(2) ** n
    ub = -log(1 - 1 / N)                 # >= D_delta
    if not ub < 1 / (N - 1):
        allok = False
check("numeric n = 2..14: -ln(1-2^-n) < 1/(N-1) at dps 60", allok)

# ------------------------------------------------------- 4. assembly arithmetic
print("CHECK 4: Theorem F assembly arithmetic")
# K3*(N-1) > N <=> N > K3/(K3-1) = 1.53..; monotone trivially in N, so the n <= 20
# grid plus the algebraic threshold check covers all N >= 2
ok = all(K3 * (mpf(2) ** n - 1) > mpf(2) ** n for n in range(1, 21)) and \
     K3 / (K3 - 1) < 2
check("branch m>=3: 2.87871*(N-1) > N — grid n <= 20 + threshold K3/(K3-1) < 2 "
      "(monotone tail algebraic)", ok)
ok = (mpf(1) / 63 < mpf(1) / 60) and all(1 / (mpf(2) ** n - 1) <= mpf(1) / 63 for n in range(6, 15))
check("branch D>1/60: D_delta < 1/(N-1) <= 1/63 < 1/60 — grid n = 6..14 "
      "(1/(N-1) decreasing, tail trivial)", ok)

# --------------------------------- 5. independent exhaustive base, n = 2 and 3
print("CHECK 5: independent exhaustive re-solve, n = 2 (8) and n = 3 (128)")
for n, expect_classes in ((2, 8), (3, 128)):
    N = 2 ** n
    chi = chi_table(n)
    A = masks(n)
    M = len(A)
    gaps = []
    deltas = set()
    for sstar in range(N):
        deltas.add(tuple(-chi[a][sstar] for a in A))
    delta_gaps, other_gaps = [], []
    cnt = 0
    for signs in itertools.product((1, -1), repeat=M):
        cnt += 1
        _, gap = solve_seal(n, list(signs), chi, dps=40)
        (delta_gaps if signs in deltas else other_gaps).append(gap)
    span_delta = max(delta_gaps) - min(delta_gaps)
    margin = min(other_gaps) - max(delta_gaps)
    # gate the margin VALUE against the companion's certified worst margins
    cert = {2: mpf("0.193236"), 3: mpf("0.462239")}[n]
    ok = (cnt == expect_classes and len(delta_gaps) == N
          and span_delta < mpf(10) ** -35 and margin > 0
          and abs(margin - cert) < mpf(10) ** -5)
    check(f"n={n}: {cnt} orientations; {N} deltas tie (span<1e-35); delta strictly "
          f"minimal; margin = companion's certified {float(cert)} to 1e-5",
          ok, f"margin={float(margin):.6f}")

# --------------------------------------------- 6. equality case = closed form
print("CHECK 6: equality case and closed-form anchors")
anchors = {2: "0.266653365179738098", 3: "0.133530982072471973",
           4: "0.064538521137571171", 5: "0.031748698314580301",
           6: "0.015748356968139"}
allok = True
for n in range(2, 7):
    N = 2 ** n
    chi = chi_table(n)
    A = masks(n)
    eps = [-chi[a][N - 1] for a in A]     # delta at the all-ones bitmask state
    _, gap = solve_seal(n, eps, chi, dps=60)
    ref = mpf(anchors[n])
    if abs(gap - ref) > mpf(10) ** (-len(anchors[n].split(".")[1]) + 2):
        allok = False
    # closed form: gap = -ln(1-2^-n) - delta_n with delta_n > 0 (n = 2..6 all in range)
    dn = -log(1 - mpf(2) ** -n) - gap
    if not dn > 0:
        allok = False
check("mu* direct solve = corpus anchors (n=2..6) and delta_n > 0", allok)

n4_min = mpf("0.064538521137571171")
chi = chi_table(4)
A = masks(4)
eps = [-chi[a][15] for a in A]
_, gap4 = solve_seal(4, eps, chi, dps=60)
ok = abs(gap4 - n4_min) < mpf(10) ** -17
check("n=4: mu* solve equals the exhaustive global minimum of receipt pD/w1", ok,
      f"|diff|={float(abs(gap4 - n4_min)):.1e}")

# ------------------------------------------------------------------- verdict
print()
total = PASS + FAIL
if FAIL == 0:
    print(f"ALL CHECKS PASS ({PASS}/{total})")
else:
    print(f"FAILURES: {FAIL}/{total}")
    raise SystemExit(1)
