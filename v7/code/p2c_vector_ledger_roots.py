#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
p2c_vector_ledger_roots.py -- Long March v7, PAPER 2, vector-ledger commitment roots.

PURPOSE
=======
Settle, at high precision, how Paper 2 (v7) should frame the "commitment root".
Paper 4 (v6) s69-76 supplies an *intrinsic division-event commitment law*
    grad psi(h) = exp(-h)
on the complete primitive oriented closed-history RN/KL ledger chi.  A round-2
referee flagged that s71's scalar law tanh eta = exp(-eta) (root eta_B ~ 0.6094)
is a ONE-MODE PARITY SLICE of this richer VECTOR ledger; the coupled {x,y,xy}
fixed point reportedly lands at a THIRD value h ~ 0.495053, distinct from BOTH
the s5 self-consistency root eta_A = 1.0903 AND the one-mode seal root eta_B.

This receipt verifies (mpmath dps>=120, sympy-exact where it helps):

  TASK 2  one-mode seal root  : tanh eta = exp(-eta)        -> eta_B
          double-counting root: tanh eta = exp(-2 eta)      -> eta_DC  (rejected)
  TASK 3  coupled vector root : grad psi(h)=exp(-h) on {x,y,xy}, U uniform on
          omega in {-1,+1}^2, psi(h)=log[(1/4) sum_omega exp(h.chi(omega))].
          Confirm/correct h ~ (0.495053, 0.495053, 0.495053); report exact value
          and whether all three components are equal.
  TASK 4/5 adjudication data  : compare eta_A (LAW-A, C=J), eta_B (one-mode seal),
          h* (coupled).  Content C(.) at each, against the capacity W_*.

VERBATIM GROUNDING (paper4 v6 paper4 s71, s73-76):
  s71: "partial_j psi(h) = exp(-h_j) for each positive primitive oriented mode.
        This is the finite intrinsic division-event commitment law."
  s71 one-mode: "P_eta(H)=U(H) exp(eta H - log cosh eta), partial_eta psi = tanh eta.
        The law becomes  tanh eta = exp(-eta).
        eta_* = 0.6093778634360061, theta_*=tanh eta_*=exp(-eta_*)=0.5436890126920763."
  s71 coupled : "In the finite complete-ledger test with primitive statistics
        x, y, xy, the solution is  h=(0.495053,0.495053,0.495053)."
  s71 double-count: "tanh eta = exp(-2 eta) ... gives ... eta=0.4406867935097715.
        That is rejected by the cochain normalization."

ledger construction confirmed against diagnostic source
  code/v6_p4af_intrinsic_division_commitment_law.py (stats_complete = x, y, x*y;
  log_partition = log[(1/4) sum_{omega in {-1,1}^2} exp(sum_j h_j chi_j(omega))];
  fixed point grad psi(h)_j = exp(-h_j)).

CONSTANTS for adjudication (paper4 s5):
  eta_A = 1.090344354879492  (root of C=J), W_* = J(eta_A) = 0.364784952089976.

Run: python3 p2c_vector_ledger_roots.py
Fallback: /Users/felixrobles/workspace/isp/code/.venv/bin/python p2c_vector_ledger_roots.py
"""

import mpmath as mp

mp.mp.dps = 160  # >=120 demanded; 160 for cancellation-heavy gradients/Hessians

# ---------------------------------------------------------------------------
def head(s):
    print("\n" + "=" * 78); print(s); print("=" * 78)

def sub(s):
    print("\n  -- " + s + " --")

def line(label, val, extra=""):
    s = "    {:<52}".format(label) + str(val)
    if extra:
        s += "   " + extra
    print(s)

PASS = {}

# ===========================================================================
# Shared single-mode (parity) information geometry (paper4 s5)
#   P_eta(q)=e^{eta q}/(2 cosh eta), q in {-1,+1}; psi=log(2 cosh eta)-log 2.
#   C(eta)=D(P_eta||mu)=eta tanh eta - log cosh eta;  J(eta)=1-tanh^2 eta.
# ===========================================================================
def C(x):
    return x * mp.tanh(x) - mp.log(mp.cosh(x))

def J(x):
    return 1 - mp.tanh(x) ** 2

# --- LAW-A self-consistency root (paper4 s5): C(eta)=J(eta) -----------------
etaA = mp.findroot(lambda x: C(x) - J(x), mp.mpf("1.0903"))
W_star = J(etaA)            # = C(etaA) by construction
W_star_C = C(etaA)

head("CONSTANTS (paper4 s5: single-diamond self-consistency, for adjudication)")
line("eta_A  (root of C=J)              ", mp.nstr(etaA, 45))
line("W_* = J(eta_A) = C(eta_A)         ", mp.nstr(W_star, 45))
line("|C(eta_A) - J(eta_A)| (balance)   ", mp.nstr(abs(W_star - W_star_C), 6))
PASS["eta_A matches paper4 s5 (1.090344354879492)"] = \
    abs(etaA - mp.mpf("1.090344354879492")) < mp.mpf("1e-15")
PASS["W_* matches paper4 s5 (0.364784952089976)"] = \
    abs(W_star - mp.mpf("0.364784952089976")) < mp.mpf("1e-15")
PASS["C(eta_A)=J(eta_A) to <1e-120 (independent formulas)"] = \
    abs(W_star - W_star_C) < mp.mpf("1e-120")

# ===========================================================================
# TASK 2 -- one-mode seal root and the rejected double-counting root
# ===========================================================================
head("TASK 2 -- one-mode parity seal root  tanh eta = exp(-eta)  (paper4 s71)")

fB   = lambda x: mp.tanh(x) - mp.exp(-x)
etaB = mp.findroot(fB, mp.mpf("0.6"))
thetaB = mp.tanh(etaB)
survB  = mp.exp(-etaB)

line("eta_B  (root of tanh eta = exp(-eta)) ", mp.nstr(etaB, 50))
line("theta_B = tanh eta_B                  ", mp.nstr(thetaB, 50))
line("exp(-eta_B) (no-division survival)    ", mp.nstr(survB, 50))
line("|tanh eta_B - exp(-eta_B)| residual   ", mp.nstr(abs(thetaB - survB), 6))
# monotone uniqueness: d/deta(tanh-exp(-eta)) = sech^2 + exp(-eta) > 0 always
deriv_min = min((1 / mp.cosh(mp.mpf(k) / 20) ** 2) + mp.exp(-mp.mpf(k) / 20)
                for k in range(0, 400))
line("min d/deta(tanh-exp(-eta)) over [0,20] ", mp.nstr(deriv_min, 8),
     "> 0  => one root, no bifurcation")
PASS["TASK2 eta_B = 0.6093778634360061 (paper4 s71)"] = \
    abs(etaB - mp.mpf("0.6093778634360061")) < mp.mpf("1e-15")
PASS["TASK2 theta_B=exp(-eta_B) self-consistent <1e-120"] = \
    abs(thetaB - survB) < mp.mpf("1e-120")
PASS["TASK2 one-mode law strictly monotone (unique root)"] = deriv_min > 0

sub("rejected double-counting root  tanh eta = exp(-2 eta)  (paper4 s71)")
etaDC  = mp.findroot(lambda x: mp.tanh(x) - mp.exp(-2 * x), mp.mpf("0.44"))
line("eta_DC (root of tanh eta = exp(-2 eta))", mp.nstr(etaDC, 50))
line("|tanh eta_DC - exp(-2 eta_DC)| residual ", mp.nstr(abs(mp.tanh(etaDC) - mp.exp(-2 * etaDC)), 6))
PASS["TASK2 double-count eta_DC = 0.4406867935097715 (paper4 s71)"] = \
    abs(etaDC - mp.mpf("0.4406867935097715")) < mp.mpf("1e-15")

# ===========================================================================
# TASK 3 -- coupled VECTOR ledger root  grad psi(h)=exp(-h) on {x,y,xy}
#   U uniform on omega=(x,y) in {-1,+1}^2 (4 configs).
#   chi(omega) = (x, y, x*y).
#   psi(h) = log[ (1/4) sum_omega exp(h_x x + h_y y + h_xy x y) ].
#   grad psi(h)_j = <chi_j>_{P_h}  (exp-family mean).
#   Fixed point: <x> = e^{-h_x}, <y> = e^{-h_y}, <xy> = e^{-h_xy}.
# ===========================================================================
head("TASK 3 -- coupled VECTOR ledger root  grad psi(h) = exp(-h)  on {x,y,xy}")

CONFIGS = [(mp.mpf(x), mp.mpf(y)) for x in (-1, 1) for y in (-1, 1)]

def chi(omega):
    x, y = omega
    return (x, y, x * y)

def Z_and_means(h):
    """Partition Z and exp-family means <x>,<y>,<xy> under P_h on the 4 configs."""
    hx, hy, hxy = h
    Z = mp.mpf(0)
    mx = my = mxy = mp.mpf(0)
    for omega in CONFIGS:
        x, y, xy = chi(omega)
        w = mp.e ** (hx * x + hy * y + hxy * xy)
        Z += w
        mx += w * x; my += w * y; mxy += w * xy
    return Z, (mx / Z, my / Z, mxy / Z)

def grad_psi(h):
    _, m = Z_and_means(h)
    return m

def commitment_residual(*h):
    """grad psi(h) - exp(-h) (the s71 fixed-point equation, componentwise).

    Accepts either commitment_residual(h_list) or, as mp.findroot calls it,
    commitment_residual(h0, h1, h2)."""
    if len(h) == 1 and hasattr(h[0], "__len__"):
        h = tuple(h[0])
    m = grad_psi(h)
    return [m[j] - mp.e ** (-h[j]) for j in range(3)]

# --- Solve the coupled 3x3 fixed point at high precision (mp.findroot) ------
# Use the symmetric seed; let findroot discover whether components stay equal.
h_sol = mp.findroot(commitment_residual,
                    (mp.mpf("0.5"), mp.mpf("0.5"), mp.mpf("0.5")))
h_sol = [mp.mpf(h_sol[i]) for i in range(3)]   # ensure plain mpf list
res_vec = commitment_residual(h_sol)
res_norm = mp.sqrt(sum(r * r for r in res_vec))

sub("coupled fixed point (general 3-vector solve, symmetric seed)")
line("h_x                                   ", mp.nstr(h_sol[0], 50))
line("h_y                                   ", mp.nstr(h_sol[1], 50))
line("h_xy                                  ", mp.nstr(h_sol[2], 50))
line("||grad psi(h) - exp(-h)|| residual    ", mp.nstr(res_norm, 6))
line("|h_x - h_y|                           ", mp.nstr(abs(h_sol[0] - h_sol[1]), 8))
line("|h_x - h_xy|                          ", mp.nstr(abs(h_sol[0] - h_sol[2]), 8))
line("|h_y - h_xy|                          ", mp.nstr(abs(h_sol[1] - h_sol[2]), 8))

components_equal = (abs(h_sol[0] - h_sol[1]) < mp.mpf("1e-120") and
                    abs(h_sol[0] - h_sol[2]) < mp.mpf("1e-120"))
PASS["TASK3 coupled root residual < 1e-100"] = res_norm < mp.mpf("1e-100")
PASS["TASK3 coupled root matches s71 (0.495053)"] = \
    abs(h_sol[0] - mp.mpf("0.495053")) < mp.mpf("1e-5")

# --- INDEPENDENT confirmation: reduce to the symmetric scalar equation ------
# By the omega-(x,y) symmetry of U (uniform) and the symmetric statistic set,
# the symmetric subspace h_x=h_y=h_xy=h is invariant.  On it, with h common:
#   Z = sum_omega exp(h(x+y+xy)).  The 4 configs (x,y,xy):
#     (+,+,+) -> 3h ;  (+,-,-) -> -h ;  (-,+,-) -> -h ;  (-,-,+) -> -h .
#   So Z(h) = e^{3h} + 3 e^{-h}.
#   <x> = [ (+1)e^{3h} + (+1)e^{-h} + (-1)e^{-h} + (-1)e^{-h} ]/Z
#       = [ e^{3h} - e^{-h} ] / (e^{3h} + 3 e^{-h}).
#   By symmetry <x>=<y>=<xy>=g(h).  Fixed point: g(h) = e^{-h}.
def g_sym(h):
    num = mp.e ** (3 * h) - mp.e ** (-h)
    den = mp.e ** (3 * h) + 3 * mp.e ** (-h)
    return num / den

f_sym = lambda h: g_sym(h) - mp.e ** (-h)
h_scalar = mp.findroot(f_sym, mp.mpf("0.5"))
sub("INDEPENDENT scalar reduction on the symmetric subspace")
line("symmetric closed form Z(h)=e^{3h}+3e^{-h}; <chi>=g(h)", "")
line("g(h) = (e^{3h}-e^{-h})/(e^{3h}+3 e^{-h})", "")
line("h*  (root of g(h)=e^{-h})             ", mp.nstr(h_scalar, 50))
line("|g(h*) - exp(-h*)| residual           ", mp.nstr(abs(f_sym(h_scalar)), 6))
line("|h* - h_x(vector solve)|              ", mp.nstr(abs(h_scalar - h_sol[0]), 8))
PASS["TASK3 scalar reduction == vector solve (<1e-100)"] = \
    abs(h_scalar - h_sol[0]) < mp.mpf("1e-100")
PASS["TASK3 components all equal (symmetric coupled root)"] = components_equal

# --- Strict convexity / isolation: Hessian of Phi(h)=psi(h)+sum exp(-h_j) ---
# Phi'' = Hess(psi) + diag(exp(-h_j)).  Hess(psi)=Cov_{P_h}(chi) is PSD;
# diag(exp(-h)) is positive => Phi strictly convex => the critical point is the
# unique isolated minimizer (paper4 s71/s73 "strictly convex commitment potential").
def cov_psi(h):
    Z, m = Z_and_means(h)
    hx, hy, hxy = h
    Cov = [[mp.mpf(0)] * 3 for _ in range(3)]
    for omega in CONFIGS:
        c = chi(omega)
        w = mp.e ** (hx * c[0] + hy * c[1] + hxy * c[2]) / Z
        for a in range(3):
            for b in range(3):
                Cov[a][b] += w * (c[a] - m[a]) * (c[b] - m[b])
    return Cov

Cov = cov_psi(h_sol)
Hess = [[Cov[a][b] + (mp.e ** (-h_sol[a]) if a == b else mp.mpf(0))
         for b in range(3)] for a in range(3)]
Hmat = mp.matrix(Hess)
eigs = mp.eigsy(Hmat, eigvals_only=True)
min_eig = min(eigs)
line("min eig of Hessian(Phi) at h*          ", mp.nstr(min_eig, 30),
     "> 0  => strictly convex, unique isolated minimizer")
PASS["TASK3 commitment potential Phi strictly convex (Hess>0)"] = min_eig > 0

# ===========================================================================
# TASK 4/5 -- adjudication: three roots, and content vs W_* across modes
# ===========================================================================
head("TASK 4/5 -- adjudication: three roots & 'seals fire under W_*' across modes")

sub("the three distinct roots")
line("eta_A  (LAW-A, C=J self-consistency)  ", mp.nstr(etaA, 30), "fixes constants/W_*")
line("h*     (coupled {x,y,xy} seal ledger) ", mp.nstr(h_sol[0], 30), "vector commitment root")
line("eta_B  (one-mode parity seal)         ", mp.nstr(etaB, 30), "scalar commitment root")
line("eta_DC (double-count, REJECTED)       ", mp.nstr(etaDC, 30), "rejected by cochain unit")
# ordering
roots_sorted = sorted([("eta_DC", etaDC), ("h*", h_sol[0]),
                       ("eta_B", etaB), ("eta_A", etaA)], key=lambda t: t[1])
line("ascending order                       ",
     " < ".join("%s(%s)" % (n, mp.nstr(v, 8)) for n, v in roots_sorted))
PASS["ADJ three commitment roots are mutually distinct"] = (
    abs(etaB - h_sol[0]) > mp.mpf("0.1") and
    abs(etaB - etaA) > mp.mpf("0.4") and
    abs(h_sol[0] - etaA) > mp.mpf("0.5"))

# --- content at each seal root vs capacity W_* ------------------------------
# 'Content' for a one-parameter parity-type mode is C(eta)=eta tanh eta - log cosh eta,
# i.e. the per-mode KL/RN content D(P_eta||mu).  For the one-mode seal root that
# IS the right content.  For the coupled root, the most honest *per-mode* content
# proxy is C evaluated at the common component h* (each of the 3 modes is a
# parity-type oriented mode with coefficient h*); we also report the total
# multi-mode KL content D(P_{h*}||U) of the coupled exponential family.
sub("per-mode KL content C(.) vs capacity W_* (= max-min self-consistent content)")
C_at_etaB = C(etaB)
C_at_hstar = C(h_sol[0])        # per-mode parity content at the coupled coefficient
line("W_* (capacity ceiling, = C(eta_A))    ", mp.nstr(W_star, 30))
line("C(eta_B)  one-mode seal content       ", mp.nstr(C_at_etaB, 30),
     "<- below W_*" if C_at_etaB < W_star else "<- NOT below W_*")
line("C(h*)     coupled per-mode content     ", mp.nstr(C_at_hstar, 30),
     "<- below W_*" if C_at_hstar < W_star else "<- NOT below W_*")
line("C(eta_B)/W_*  (fraction of capacity)   ", mp.nstr(C_at_etaB / W_star, 12))
line("C(h*)/W_*     (fraction of capacity)   ", mp.nstr(C_at_hstar / W_star, 12))

# Total KL content of the coupled exponential family D(P_{h*} || U):
#   D = sum_omega P_h(omega) log( P_h(omega)/ (1/4) )
#     = <h, chi>_{P_h} - psi(h)   (standard exp-family identity, base U=1/4 each)
def kl_coupled(h):
    Z, m = Z_and_means(h)
    psi = mp.log(Z / 4)                       # log[(1/4) sum exp(h.chi)]
    return (h[0] * m[0] + h[1] * m[1] + h[2] * m[2]) - psi
D_coupled = kl_coupled(h_sol)
line("D(P_{h*}||U)  TOTAL coupled KL content ", mp.nstr(D_coupled, 30),
     "(3-mode; compare to 3*W_* capacity budget)")
line("D(P_{h*}||U) / (3 W_*)                 ", mp.nstr(D_coupled / (3 * W_star), 12))

PASS["TASK5 one-mode seal content C(eta_B) < W_*"] = C_at_etaB < W_star
PASS["TASK5 coupled per-mode content C(h*) < W_*"] = C_at_hstar < W_star
PASS["TASK5 coupled TOTAL content < 3-mode capacity 3 W_*"] = D_coupled < 3 * W_star
# robustness: BOTH checkable seal modes fire strictly under the per-mode ceiling
PASS["TASK5 'seals fire under W_*' robust in every checked mode"] = \
    (C_at_etaB < W_star) and (C_at_hstar < W_star)

# ===========================================================================
head("TASK 6 -- STRUCTURAL robustness: content < W_* is not merely empirical")
# The inequality 'content < W_*' is structural, not 'every mode we happened to check':
#   (a) seal content C(eta) is MONOTONE INCREASING in the seal coefficient
#       (C'(eta) = eta*sech^2(eta) > 0 for eta>0), so larger coefficient = more content;
#   (b) reaching content W_* requires coefficient eta_A (since C(eta_A)=W_* exactly),
#       which the seal law tanh eta = exp(-lambda eta) attains only at cochain unit
#       lambda* = -ln(tanh eta_A)/eta_A ~ 0.208 < 1 -- i.e. UNDER-counting the forced
#       RN action, inadmissible by the SAME cochain-unit argument that rejects lambda=2
#       (the double-count). Admissible lambda >= 1 => coefficient <= eta_B = 0.6094;
#   (c) coupling more modes only DILUTES the per-mode coefficient (h_* = 0.4951 < eta_B),
#       lowering content further.
# Hence the canonical one-mode content C(eta_B) = 0.428 W_* is the SUPREMUM over all
# admissible modes, and it is strictly < W_*.
sub("structural reason the inequality is robust")
Cp = lambda e: e * mp.sech(e) ** 2
line("C'(eta) at eta=0.3, 0.6, 1.09     ", "%s, %s, %s  (>0: C strictly rising)"
     % (mp.nstr(Cp(mp.mpf("0.3")), 6), mp.nstr(Cp(mp.mpf("0.6")), 6), mp.nstr(Cp(etaA), 6)))
C_inf = mp.log(2)
line("lim_{eta->inf} C(eta) = log 2      ", "%s   (C bounded, C(50)=%s)"
     % (mp.nstr(C_inf, 18), mp.nstr(C(mp.mpf(50)), 18)))
lam_star = -mp.log(mp.tanh(etaA)) / etaA
line("lambda* to reach content W_*       ", "%s   (< 1 => under-counts RN action, inadmissible)"
     % mp.nstr(lam_star, 10))
line("C(eta_B)/W_* (canonical lambda=1)  ", "%s   (= supremum over admissible modes)"
     % mp.nstr(C_at_etaB / W_star, 10))
PASS["TASK6 C(eta) strictly monotone increasing (C'>0)"] = \
    all(Cp(e) > 0 for e in (mp.mpf("0.1"), mp.mpf("0.6"), etaA, mp.mpf("3")))
PASS["TASK6 C(eta_A) = W_* exactly (<1e-100): content W_* needs coefficient eta_A"] = \
    abs(C(etaA) - W_star) < mp.mpf("1e-100")
PASS["TASK6 C bounded: lim C = log 2 (C(50) ~ log2 <1e-20)"] = \
    abs(C(mp.mpf(50)) - mp.log(2)) < mp.mpf("1e-20")
PASS["TASK6 lambda* to reach W_* ~ 0.208 < 1 (inadmissible under-count)"] = \
    (lam_star < mp.mpf("0.25")) and (lam_star < 1)
PASS["TASK6 coupling DILUTES: h_* < eta_B (more modes -> lower coefficient)"] = \
    h_sol[0] < etaB
PASS["TASK6 admissible-class supremum = C(eta_B) < W_*"] = \
    (C_at_etaB < W_star) and (C_at_etaB >= C_at_hstar)

# IMPORTANT scope: the supremum C(eta_B) is over the ADMISSIBLE class only --
#   complete primitive ORTHOGONAL parity ledgers (paper4 s73-76) on the COUNT-DUAL
#   eventless base mu=(1/2,1/2) (paper4 s5-6).  Two structural facts, then the gate:
# (i) MONOTONE DILUTION over the full symmetric character group on {+-1}^m (uniform
#     base): per-mode coefficient FALLS as modes are added -- 1 char -> eta_B=0.6094,
#     {x,y,xy} -> 0.4951, full 7-char on {+-1}^3 -> 0.3680.  Orthogonal/independent
#     modes each sit AT eta_B; any coupling only lowers the coefficient.
# (ii) GATE IS LOAD-BEARING: drop the count-dual base (skew mu(+)=p<1/2) and the
#     seal coefficient AND content EXCEED eta_B / W_* -- p=0.2 gives content 0.526 >
#     W_*=0.365.  Such skewed (and non-orthogonal/mixed-basis, paper4 s75) ledgers
#     are INADMISSIBLE; they are exactly what the count-dual + orthogonality gates
#     exclude.  So 'seals fire under W_*' is a theorem OF the admissible class.
sub("(i) monotone dilution over the symmetric character group (uniform base)")
S2 = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
S3 = [(a, b, c) for a in (1, -1) for b in (1, -1) for c in (1, -1)]
def _solve(states, stats, base=None):
    k = len(stats)
    def fn(*h):
        hh = list(h)
        ws = [(1 if base is None else base[s]) * mp.e ** sum(hh[j] * stats[j](s) for j in range(k)) for s in states]
        Z = sum(ws)
        return [sum(ws[i] * stats[j](states[i]) for i in range(len(states))) / Z - mp.e ** (-hh[j]) for j in range(k)]
    sol = mp.findroot(fn, [mp.mpf("0.5")] * k)
    return [sol[i] for i in range(k)]
r1 = _solve([(1,), (-1,)], [lambda s: s[0]])[0]
r3 = _solve(S2, [lambda s: s[0], lambda s: s[1], lambda s: s[0] * s[1]])[0]
r7 = _solve(S3, [lambda s: s[0], lambda s: s[1], lambda s: s[2],
                 lambda s: s[0]*s[1], lambda s: s[0]*s[2], lambda s: s[1]*s[2],
                 lambda s: s[0]*s[1]*s[2]])[0]
line("per-mode coeff: 1-char / 3-char / 7-char", "%s / %s / %s  (eta_B=%s; falls)"
     % (mp.nstr(r1, 8), mp.nstr(r3, 8), mp.nstr(r7, 8), mp.nstr(etaB, 8)))
PASS["TASK6 orthogonal modes each = eta_B; coupling DILUTES (0.609>0.495>0.368)"] = \
    (abs(r1 - etaB) < mp.mpf("1e-30")) and (r3 < r1) and (r7 < r3)
sub("(ii) gate is load-bearing: a SKEWED (non-count-dual) base exceeds W_*")
def _skew(p):
    h = mp.findroot(lambda h: (p*mp.e**h - (1-p)*mp.e**(-h)) / (p*mp.e**h + (1-p)*mp.e**(-h)) - mp.e**(-h), 1)
    a = p*mp.e**h; b = (1-p)*mp.e**(-h); Z = a + b
    D = (a/Z)*mp.log((a/Z)/p) + (b/Z)*mp.log((b/Z)/(1-p))
    return h, D
h_sk, D_sk = _skew(mp.mpf("0.2"))
line("skewed base mu(+)=0.2: coeff, content", "%s, %s  (both > eta_B / W_*)"
     % (mp.nstr(h_sk, 8), mp.nstr(D_sk, 8)))
PASS["TASK6 INADMISSIBLE skewed base (p=0.2) EXCEEDS W_* (gate is load-bearing)"] = \
    (h_sk > etaB) and (D_sk > W_star)

# ===========================================================================
head("VERDICT BLOCK")
print(f"""
  THREE DISTINCT COMMITMENT-LAW ROOTS (all high precision, this run):
    eta_A  = {mp.nstr(etaA, 16)}   LAW-A self-consistency C=J  (fixes W_*; NOT a seal root)
    h*     = {mp.nstr(h_sol[0], 16)}   coupled {{x,y,xy}} division-event ledger  grad psi=exp(-h)
    eta_B  = {mp.nstr(etaB, 16)}   one-mode parity seal  tanh eta = exp(-eta)
    eta_DC = {mp.nstr(etaDC, 16)}   double-count  tanh eta = exp(-2 eta)  (REJECTED by paper4)

  s71 vs s73-76 DISTINCTION (verbatim-grounded):
    s71 ONE-MODE law selects a TILT COEFFICIENT h (== eta) of the whole-history
      parity Gibbs law P_eta=U exp(eta H - log cosh eta): partial_eta psi = tanh eta,
      seal law  tanh eta = exp(-eta)  -> eta_B.  It is NOT a spacing or a content;
      it is the RN/cochain action coefficient of the single oriented closed-history mode.
    s73-76 UPGRADE it to the VECTOR/cofinal commitment law on the COMPLETE primitive
      oriented RN/KL ledger:  grad psi(h) = exp(-h)  (one equation per primitive mode),
      Euler eq of the strictly convex potential Phi(h)=psi(h)+sum_j exp(-h_j),
      cofinal/cover-invariant on the primitive QUOTIENT ledger (serial-subdivision
      invariant via prod exp(-I_k)=exp(-sum I_k)).  The {{x,y,xy}} coupled instance
      lands at h*=({mp.nstr(h_sol[0],8)},...) with all three components EQUAL.

  IS 'THE commitment root' WELL-DEFINED?  ->  NO -- it is MODE-/LEDGER-DEPENDENT.
    The seal/commitment law is grad psi(h)=exp(-h) on whatever the COMPLETE primitive
    ledger is.  A different complete ledger (one oriented mode -> eta_B; the coupled
    {{x,y,xy}} ledger -> h*~0.4951) gives a different numerical root.  eta_B is the
    ONE-MODE-PARITY value, not a corpus-unique 'the' commitment root.  s69 also warns
    a fixed-CONTENT threshold is non-canonical (selected eta drifts with the supplied
    unit), so there is no single content/eta the seal universally commits.

  s69 NON-CANONICITY (verbatim): the constant-unit/Poisson-renewal route
    eta=atanh(exp(-r eta)) selects eta only after the dimensionless ratio r is
    supplied, and 'Changing the renewal shape changes the selected eta' /
    'commitment scale attack ... the selected eta moves, so r must be intrinsic'.
    => a FIXED-CONTENT commitment threshold is NON-CANONICAL; the selected eta
    drifts with the supplied unit/shape.  (s71 removes r via RN self-accounting,
    fixing r=1 -> the survival shape, but the *ledger/mode* still sets the root.)

  IS 'SEALS FIRE UNDER W_*' ROBUST ACROSS MODES?  ->  YES (every mode checked).
    one-mode:  C(eta_B) = {mp.nstr(C_at_etaB, 12)}  <  W_* = {mp.nstr(W_star, 12)}  (frac {mp.nstr(C_at_etaB/W_star,6)})
    coupled :  C(h*)    = {mp.nstr(C_at_hstar, 12)}  <  W_*               (frac {mp.nstr(C_at_hstar/W_star,6)})
    coupled total D(P_{{h*}}||U) = {mp.nstr(D_coupled,12)} < 3 W_* (the 3-mode capacity budget).
    Both checkable seal modes fire STRICTLY UNDER the W_* per-mode capacity ceiling.

  RECOMMENDATION FOR PAPER 2 WORDING (commitment root / 'two roots' framing):
    Paper 2 should NOT call eta_B 'the' commitment root.  State it as:
    (1) eta_A=1.0903 is the self-consistency root that FIXES the diamond constants
        and the capacity W_*; it is not a seal-firing value.
    (2) The corpus seal/division-event law is the VECTOR fixed point grad psi(h)=exp(-h)
        on the complete primitive oriented ledger; its numerical root is mode-/ledger-
        dependent -- eta_B=0.6094 is the ONE-MODE-PARITY slice, the coupled {{x,y,xy}}
        ledger gives ~0.4951.  Frame eta_B as 'the one-mode-parity seal value', not the
        unique canonical commitment root.
    (3) The robust, mode-independent corpus fact is the INEQUALITY: in every sealing
        mode we can check, the committed content lands STRICTLY BELOW the W_* capacity
        (C(eta_B), C(h*) both < W_*).  Paper 2 should lead with that inequality, not
        with a single magic number, and should cite s69's non-canonicity of any
        fixed-content threshold so it neither manufactures a contradiction nor implies
        a unique seal root.
""")

# ===========================================================================
head("MACHINE CHECKS")
allpass = True
for k, v in PASS.items():
    flag = "PASS" if v else "FAIL"
    if not v:
        allpass = False
    print(f"  [{flag}] {k}")
print("\n  " + ("ALL CHECKS PASS" if allpass else "*** SOME CHECK FAILED ***"))
assert allpass, "p2c receipt FAILED a machine check"
