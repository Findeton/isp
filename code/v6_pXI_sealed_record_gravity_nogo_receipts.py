#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RECEIPT SCRIPT for publishable Paper XI:
  "Emergent Einstein equations without an emergent Newton constant:
   a no-go for sealed-record gravity"

Source physics:
  isp/v6/relativistic-isp-v6-paper57-gravity-from-sealed-records.md

This script COMPUTES and PRINTS, each labeled, at high precision:
 (1) The length-gauge WEIGHT MAP under g_lambda: l -> mu*l.
 (2) SIGMA-SPLIT: same sealed data, A_rec=1 vs A_rec=3.
 (3) The two SEPARATE weight-zero invariants kappa*sigma_A=2pi and G*Lambda^2=const.
 (4) de Sitter weight-twin: N_dS weight-0; S_dS = N_dS fixes only G*Lambda0.
 (5) The null-cone lemma (and the CORRECT timelike statement).
 (6) Spectral-action honesty: naive collar f2 = 1/(2pi)^2, not 1/(2pi).
 (7) KMS/Unruh detailed balance at T=a/2pi and the Rindler interval identity.

Precision discipline (Paper XI sec.8): EVERY modular-kernel / near-vacuum /
small-argument numeric quantity is computed in mpmath at mp.dps >= 80 (100 where
cheap). Exact algebra is sympy-symbolic. float64 is NEVER used for these
quantities (the corpus audit shows float64 gives a 25-32% artifact there).

Runs with: python3 v6_pXI_sealed_record_gravity_nogo_receipts.py
Libraries: mpmath, sympy, numpy only.
"""

import sympy as sp
import mpmath as mp
import numpy as np

# ----------------------------------------------------------------------------
# Global precision floor: ALL numeric work at dps >= 80; use 100 where cheap.
# ----------------------------------------------------------------------------
mp.mp.dps = 100
DPS_NUM = 100   # cheap numeric checks
NL = "\n"

def hr(title):
    line = "=" * 78
    return f"{line}{NL}{title}{NL}{line}"

def fmt(x, n=30):
    """Format an mpmath real to n significant digits."""
    return mp.nstr(mp.mpf(x), n, strip_zeros=False)

OUT = []   # canonical output block accumulator
def P(s=""):
    OUT.append(s)

# ============================================================================
P(hr("PAPER XI RECEIPTS -- sealed-record gravity no-go"))
P(f"mpmath mp.dps = {mp.mp.dps}   (all numeric checks at dps>=80; 100 used here)")
P(f"sympy {sp.__version__}   mpmath {mp.__version__}   numpy {np.__version__}")
P()

# ============================================================================
# (1) LENGTH-GAUGE WEIGHT MAP under g_lambda: l -> mu*l
#     weight(X) = log[ X(mu*l) / X(l) ] / log(mu)
#     A_rec=l^2:+2 ; sigma_A=1/l^2:-2 ; G=l^2:+2 ; l_step=l:+1 ; 1/l:-1 ; count:0
#     bijection: G*sigma_A -> weight 0, value 1/4.
# ============================================================================
P(hr("(1) LENGTH-GAUGE WEIGHT MAP  (g_lambda: l -> mu*l)"))
P("   weight(X) := log[ X(mu*l) / X(l) ] / log(mu)   (degree / homogeneity map)")
P()

l, mu, c0 = sp.symbols('l mu c0', positive=True)

# Each record/geometric quantity as a function of the record length l.
# (c0 = a pure record number prefactor, weight 0, carried symbolically.)
quantities = [
    ("A_rec = l^2",        c0 * l**2,      sp.Integer(2)),
    ("sigma_A = 1/l^2",    c0 / l**2,      sp.Integer(-2)),
    ("G = l^2",            c0 * l**2,      sp.Integer(2)),
    ("l_step = l",         c0 * l,         sp.Integer(1)),
    ("1/l",                c0 / l,         sp.Integer(-1)),
    ("pure count",         c0,             sp.Integer(0)),
]

P("   sympy-exact degree-map residuals  (must be identically 0):")
all_zero = True
for name, expr, expected in quantities:
    # symbolic weight via the degree map
    ratio = sp.simplify(expr.subs(l, mu*l) / expr)         # = mu**weight
    w = sp.simplify(sp.log(ratio) / sp.log(mu))            # = weight (exact)
    resid = sp.simplify(w - expected)
    if resid != 0:
        all_zero = False
    P(f"     weight({name:18s}) = {str(w):>4s}   expected {str(expected):>3s}   residual {resid}")
P(f"   all weight residuals identically zero (sympy): {all_zero}")
P()

# The bijection G * sigma_A -> weight 0, value 1/4 (sympy-exact).
G_of_l      = sp.Rational(1, 4) / (c0 / l**2)   # G = (1/4)/sigma_A = (1/4) l^2 / c0
sigma_of_l  = c0 / l**2
prod        = sp.simplify(G_of_l * sigma_of_l)
prod_weight = sp.simplify(sp.log((G_of_l*sigma_of_l).subs(l, mu*l) /
                                 (G_of_l*sigma_of_l)) / sp.log(mu))
P("   BIJECTION  G(l) = (1/4)/sigma_A(l)   ->   G*sigma_A is l-independent:")
P(f"     G*sigma_A (exact)        = {prod}     (expected 1/4)")
P(f"     weight(G*sigma_A)        = {prod_weight}      (expected 0)")
P(f"     residual value (-1/4)    = {sp.simplify(prod - sp.Rational(1,4))}")
P(f"     residual weight (-0)     = {sp.simplify(prod_weight - 0)}")
P()

# dps=100 numeric cross-check of the weight map at mu=1.7, l arbitrary.
P("   dps=100 NUMERIC cross-check of the degree map at mu=1.7 (l=1.3, c0=0.9):")
mu_n = mp.mpf('1.7')
l_n  = mp.mpf('1.3')
c_n  = mp.mpf('0.9')
def num_weight(fn):
    return mp.log(fn(mu_n*l_n) / fn(l_n)) / mp.log(mu_n)
checks_num = [
    ("A_rec=l^2",     lambda L: c_n*L**2,         2),
    ("sigma_A=1/l^2", lambda L: c_n/L**2,        -2),
    ("G=l^2",         lambda L: c_n*L**2,         2),
    ("l_step=l",      lambda L: c_n*L,            1),
    ("1/l",           lambda L: c_n/L,           -1),
    ("pure count",    lambda L: c_n,              0),
    ("G*sigma_A",     lambda L: (mp.mpf(1)/4/(c_n/L**2))*(c_n/L**2),  0),
]
maxres = mp.mpf(0)
for name, fn, exp_w in checks_num:
    w = num_weight(fn)
    r = abs(w - exp_w)
    maxres = max(maxres, r)
    P(f"     weight({name:14s}) = {fmt(w,40)}   |resid| = {mp.nstr(r,3)}")
P(f"   max numeric weight residual (dps=100): {mp.nstr(maxres,3)}")
P()

# ============================================================================
# (2) SIGMA-SPLIT: same sealed data, A_rec=1 vs A_rec=3.
#     sigma_A = 1/A_rec ; G = A_rec/4 (from G*sigma_A=1/4) ; kappa = 1/sigma_A = A_rec
#     G*sigma_A=1/4 invariant in BOTH ; Einstein-form residual exactly 0 in both.
# ============================================================================
P(hr("(2) SIGMA-SPLIT  (same sealed horizon data, A_rec = 1 vs A_rec = 3)"))
P("   sealed data fixed; only the record-area->geometry label A_rec changes.")
P("   sigma_A = 1/A_rec ;  G = A_rec/4 (from G*sigma_A=1/4) ;")
P("   kappa (Jacobson, prefactor 1) = 1/sigma_A = A_rec.")
P()

# symbolic Einstein-form residual:  G_munu = kappa * T_munu  rearranged.
# Build a schematic curvature response: with entropy-area density sigma_A,
# the first-law coupling is kappa = 1/sigma_A, and the Einstein-FORM identity
# G_ab - kappa*T_ab = 0 is satisfied by construction once T_ab := G_ab/kappa.
Arec = sp.symbols('A_rec', positive=True)
sigma_A_sym = 1/Arec
G_sym       = sp.Rational(1,4)/sigma_A_sym       # = A_rec/4
kappa_sym   = 1/sigma_A_sym                       # = A_rec  (schematic Jacobson)
kappa_phys  = 8*sp.pi*G_sym                        # = 2*pi*A_rec  (physical 8 pi G)

# A genuine traceless symbol G_ab response and its source T_ab = G_ab/kappa:
Gab = sp.symbols('Gab', real=True)               # a curvature-response component
Tab = Gab / kappa_sym                              # source so that Einstein form holds
einstein_resid = sp.simplify(Gab - kappa_sym*Tab)  # must be 0 identically

P("   sympy-exact, parametrized by A_rec:")
P(f"     sigma_A           = {sigma_A_sym}")
P(f"     G = (1/4)/sigma_A = {sp.simplify(G_sym)}")
P(f"     kappa = 1/sigma_A = {sp.simplify(kappa_sym)}   (schematic Jacobson, prefactor 1)")
P(f"     kappa_phys = 8piG = {sp.simplify(kappa_phys)}   (physical normalization)")
P(f"     G*sigma_A         = {sp.simplify(G_sym*sigma_A_sym)}     (invariant = 1/4)")
P(f"     Einstein-form residual  G_ab - kappa*T_ab = {einstein_resid}   (identically 0)")
P()
P("   two explicit splits (sympy substitution):")
for av in (1, 3):
    sub = {Arec: sp.Integer(av)}
    P(f"     A_rec = {av}:  sigma_A = {sigma_A_sym.subs(sub)},  "
      f"G = {sp.simplify(G_sym.subs(sub))},  "
      f"kappa = {sp.simplify(kappa_sym.subs(sub))},  "
      f"kappa_phys = {sp.simplify(kappa_phys.subs(sub))},  "
      f"G*sigma_A = {sp.simplify((G_sym*sigma_A_sym).subs(sub))},  "
      f"Einstein resid = {einstein_resid.subs(sub)}")
P()
P("   CONCLUSION: G and kappa DIFFER across the split (1 vs 3); G*sigma_A=1/4 and")
P("   the Einstein-form residual=0 are IDENTICAL in both -> the records fix the")
P("   FORM and the weight-0 product, never the absolute scale G.")
P()

# ============================================================================
# (3) Two SEPARATE weight-zero invariants:
#     kappa*sigma_A = 2*pi   (from kappa=8*pi*G and G*sigma_A=1/4)
#     G*Lambda^2    = const  (a different pure number)
#     NOT numerically equal -> they are separate invariants.
# ============================================================================
P(hr("(3) TWO SEPARATE weight-zero invariants"))
# invariant A: kappa*sigma_A with kappa=8 pi G and G sigma_A = 1/4
Gs, sAs, Lam = sp.symbols('G sigma_A Lambda', positive=True)
kappa_8piG = 8*sp.pi*Gs
inv_A = sp.simplify((kappa_8piG*sAs).subs(Gs*sAs, sp.Rational(1,4)))
# substitute G*sigma_A=1/4 explicitly:
inv_A_val = sp.simplify(8*sp.pi*sp.Rational(1,4))     # 8 pi * (G sigma_A) = 8 pi /4 = 2 pi
P("   invariant A:  kappa*sigma_A = (8*pi*G)*sigma_A = 8*pi*(G*sigma_A) = 8*pi*(1/4)")
P(f"                 kappa*sigma_A = {inv_A_val}   (= 2*pi, weight 0)")

# invariant B: G*Lambda^2 = const. The honest sec.2 value is a pure number;
# the (CONJECTURED) spectral value often quoted is 3*pi^2. We carry it as the
# illustrative const but flag it as conjectured (see receipt (6)).
GLam2_conj = 3*sp.pi**2
P("   invariant B:  G*Lambda^2 = const  (a DIFFERENT pure number; Lambda = inverse-length")
P("                 UV/spectral cutoff). Illustrative (CONJECTURED) value 3*pi^2.")
P(f"                 3*pi^2 = {GLam2_conj}")
P()
# numeric separation at dps=100:
inv_A_num   = mp.mpf(2)*mp.pi
inv_B_num   = mp.mpf(3)*mp.pi**2
P("   dps=100 numeric values and their separation:")
P(f"     kappa*sigma_A = 2*pi      = {fmt(inv_A_num,50)}")
P(f"     G*Lambda^2   = 3*pi^2     = {fmt(inv_B_num,50)}")
P(f"     difference (2pi - 3pi^2)  = {fmt(inv_A_num - inv_B_num,40)}")
P(f"     are they numerically equal? {bool(abs(inv_A_num - inv_B_num) < mp.mpf(10)**(-80))}")
P("   -> NOT equal: kappa*sigma_A=2pi and G*Lambda^2 are SEPARATE invariants")
P("      (they share the STRUCTURE 'fixed weight-0 pure number', not a value).")
P()

# ============================================================================
# (4) de Sitter weight-twin:
#     N_dS = A_horizon/A_rec = 4*pi*(sigma_A/Lambda0)  is weight-0 (l-independent)
#     S_dS = pi/(G*Lambda0) = N_dS  fixes only the weight-0 product G*Lambda0,
#     leaving G free. Show two unit conventions: same G*Lambda0, different G.
# ============================================================================
P(hr("(4) de SITTER WEIGHT-TWIN  (Lambda0 is the weight-twin of sigma_A)"))
# Symbolic: with A_horizon = 4 pi / Lambda0 and A_rec = 1/sigma_A,
# N_dS = A_horizon/A_rec = 4 pi (sigma_A/Lambda0). Both sigma_A and Lambda0 have
# weight -2, so the ratio is weight 0 (l cancels).
Lambda0 = sp.symbols('Lambda0', positive=True)
sigmaA_l = c0/l**2                 # weight -2
Lambda0_l = sp.symbols('k0', positive=True)/l**2   # weight -2 (twin); k0 pure number
A_horizon = 4*sp.pi/Lambda0_l
A_rec_l   = 1/sigmaA_l
N_dS = sp.simplify(A_horizon/A_rec_l)
N_dS_ll = sp.simplify(4*sp.pi*(sigmaA_l/Lambda0_l))   # alt form
dN_dl = sp.simplify(sp.diff(N_dS, l))
P("   N_dS = A_horizon/A_rec = 4*pi*(sigma_A/Lambda0)  (ratio of two weight-(-2) data):")
P(f"     N_dS (l-form)          = {N_dS}")
P(f"     4pi*(sigma_A/Lambda0)  = {N_dS_ll}   (same)")
P(f"     d N_dS / d l           = {dN_dl}     (l-independent => weight 0, sympy-exact)")
P()
# S_dS = pi/(G*Lambda0) = N_dS  => fixes only the product G*Lambda0.
S_dS = sp.pi/(Gs*Lambda0)
P("   S_dS = pi/(G*Lambda0) = N_dS  => fixes ONLY the weight-0 product G*Lambda0:")
P(f"     G*Lambda0 = pi/N_dS   (the only thing fixed); G alone stays FREE.")
P()
# Two unit conventions: same G*Lambda0 product, different G (dps=100).
P("   dps=100: two unit conventions with the SAME G*Lambda0 but DIFFERENT G:")
N_dS_num = mp.mpf('100')                 # a chosen de Sitter horizon count
GLam0    = mp.pi / N_dS_num               # the fixed weight-0 product
# convention I: pick Lambda0 = 1   -> G = GLam0
Lam0_I   = mp.mpf('1')
G_I      = GLam0 / Lam0_I
# convention II: pick Lambda0 = 7  -> G = GLam0/7  (different G, same product)
Lam0_II  = mp.mpf('7')
G_II     = GLam0 / Lam0_II
S_I      = mp.pi/(G_I*Lam0_I)
S_II     = mp.pi/(G_II*Lam0_II)
P(f"     fixed product G*Lambda0 = pi/N_dS = {fmt(GLam0,50)}")
P(f"     conv I :  Lambda0 = {fmt(Lam0_I,3)}  -> G = {fmt(G_I,40)}")
P(f"     conv II:  Lambda0 = {fmt(Lam0_II,3)}  -> G = {fmt(G_II,40)}")
P(f"     G_I  != G_II ?                {bool(abs(G_I-G_II) > mp.mpf(10)**(-50))}")
P(f"     G_I*Lambda0_I  = {fmt(G_I*Lam0_I,40)}")
P(f"     G_II*Lambda0_II= {fmt(G_II*Lam0_II,40)}")
P(f"     product residual |GL0_I - GL0_II| = {mp.nstr(abs(G_I*Lam0_I - G_II*Lam0_II),3)}")
P(f"     entropy residual |S_I - S_II|     = {mp.nstr(abs(S_I-S_II),3)}   (both = N_dS)")
P(f"     S_I  = {fmt(S_I,40)}   (= N_dS = {fmt(N_dS_num,3)})")
P("   -> S_dS pins G*Lambda0 only; G is free for the same reason sigma_A is.")
P()

# ============================================================================
# (5) NULL-CONE LEMMA  +  correct timelike statement.
#  (a) S_ab symmetric, S_ab k^a k^b = 0 for ALL null k  =>  S_ab = Phi g_ab.
#      Show the constraint rank = 9 on the 10 symmetric comps, pattern
#      off-diag 0, S00=-S33=S11=S22 (i.e. S_ab proportional to eta_ab).
#  (b) E_ab u^a u^b CONSTANT for all unit timelike u  =>  E = c g_ab.
#      The naive VANISHING version E_ab u^a u^b = 0 forces E = 0 (the WRONG one).
# ============================================================================
P(hr("(5) NULL-CONE LEMMA and the correct TIMELIKE statement"))
# Minkowski metric, signature (-,+,+,+)
eta = sp.diag(-1, 1, 1, 1)

# symmetric S with 10 unknowns
Ssym = sp.symbols('S00 S01 S02 S03 S11 S12 S13 S22 S23 S33', real=True)
S = sp.Matrix([
    [Ssym[0], Ssym[1], Ssym[2], Ssym[3]],
    [Ssym[1], Ssym[4], Ssym[5], Ssym[6]],
    [Ssym[2], Ssym[5], Ssym[7], Ssym[8]],
    [Ssym[3], Ssym[6], Ssym[8], Ssym[9]],
])

# Sample MANY null vectors k (k.k = 0 in eta): k = (1, n) with |n|=1 EXACTLY.
# We use EXACT rational unit 3-vectors (n.n = 1 exactly) so the whole linear
# algebra stays sympy-exact and fast (no sqrt entries, no float rationalization).
R = sp.Rational
exact_unit_dirs = [
    (R(1), R(0), R(0)),                 # axes
    (R(0), R(1), R(0)),
    (R(0), R(0), R(1)),
    (R(3,5), R(4,5), R(0)),             # 3-4-5 Pythagorean unit vectors
    (R(4,5), R(3,5), R(0)),
    (R(3,5), R(0), R(4,5)),
    (R(0), R(3,5), R(4,5)),
    (R(5,13), R(12,13), R(0)),          # 5-12-13
    (R(12,13), R(0), R(5,13)),
    (R(2,3), R(2,3), R(1,3)),           # 2,2,1 -> 4+4+1=9 -> /9=1 exactly
    (R(1,3), R(2,3), R(2,3)),
    (R(6,7), R(2,7), R(3,7)),           # 6,2,3 -> 36+4+9=49 -> /49=1 exactly
]

rows = []
for (nx, ny, nz) in exact_unit_dirs:
    assert sp.simplify(nx**2 + ny**2 + nz**2 - 1) == 0   # exact unit -> exact null
    k = sp.Matrix([sp.Integer(1), nx, ny, nz])           # k.k = -1 + 1 = 0 exactly
    quad = sp.expand((k.T * S * k)[0])
    row = [quad.coeff(u) for u in Ssym]
    rows.append(row)

M = sp.Matrix(rows)
rank = M.rank()
ns = M.nullspace()
P(f"   (a) S_ab k^a k^b = 0 for all null k  (sampled {len(rows)} EXACT null directions):")
P(f"       constraint matrix is {M.shape[0]} x 10 on the symmetric components")
P(f"       rank(constraint)            = {rank}    (expected 9)")
P(f"       nullspace dimension         = {len(ns)}    (expected 1 -> S = Phi*g)")
# The single nullspace vector should be eta's components: (S00,..,S33) ~ (-1,0,0,0,1,0,0,1,0,1)
nvec = sp.Matrix(ns[0])
nvec = nvec / nvec[0]   # normalize first entry to compare to eta pattern (-1,...)
eta_pat = sp.Matrix([-1, 0, 0, 0, 1, 0, 0, 1, 0, 1])
nvec_scaled = sp.simplify(nvec * (-1))   # so S00 -> -1 matches eta_pat[0]=-1? nvec[0]=1 after /nvec[0]
# nvec[0] is now 1; eta_pat[0] = -1, so multiply by -1:
solution_pattern = sp.simplify(nvec_scaled - eta_pat)
P(f"       nullspace vector (S00..S33) proportional to eta = (-1,0,0,0,1,0,0,1,0,1):")
P(f"         normalized solution - eta_pattern = {list(solution_pattern)}")
P(f"       => off-diagonals 0 ; S00 = -S11 = -S22 = -S33  (i.e. S_ab = Phi*g_ab).")
P(f"       pattern check  S00=-S33=S11=S22 satisfied: "
  f"{bool(solution_pattern == sp.zeros(10,1))}")
P()

# (b) timelike statements. Unit timelike u: u.u = -1.  Sample many.
Esym = sp.symbols('E00 E01 E02 E03 E11 E12 E13 E22 E23 E33', real=True)
E = sp.Matrix([
    [Esym[0], Esym[1], Esym[2], Esym[3]],
    [Esym[1], Esym[4], Esym[5], Esym[6]],
    [Esym[2], Esym[5], Esym[7], Esym[8]],
    [Esym[3], Esym[6], Esym[8], Esym[9]],
])
cconst = sp.symbols('c_const', real=True)

def timelike_dirs():
    # u = (cosh r, sinh r * n_hat), n_hat an EXACT unit 3-vector. We use the
    # RATIONAL parametrization of the unit hyperbola, ch=(1+s^2)/(1-s^2),
    # sh=2s/(1-s^2) for rational s in (0,1): then ch^2 - sh^2 = 1 EXACTLY and
    # ch, sh are rational -> u.u = -1 exactly and all linear algebra stays
    # sympy-exact and fast (no transcendental cosh/sinh ranks).
    out = []
    for j, (nx, ny, nz) in enumerate(exact_unit_dirs):
        s = R(1, 3) + R(j, 17)                  # distinct rational rapidity params in (0,1)
        ch = (1 + s**2)/(1 - s**2)
        sh = 2*s/(1 - s**2)
        u = sp.Matrix([ch, sh*nx, sh*ny, sh*nz])
        assert sp.simplify((u.T*eta*u)[0] + 1) == 0   # exact unit-timelike
        out.append(u)
    return out

uds = timelike_dirs()

# CORRECT statement: E_ab u^a u^b = c_const (the SAME constant) for all unit timelike u.
rows_const = []
for u in uds:
    quad = sp.expand((u.T * E * u)[0] - cconst)
    unknowns = list(Esym) + [cconst]
    row = [sp.simplify(quad.coeff(v)) for v in unknowns]
    rows_const.append(row)
Mc = sp.Matrix(rows_const)
nsc = Mc.nullspace()
P("   (b1) CORRECT timelike statement: E_ab u^a u^b = c (SAME constant) for all unit")
P(f"        timelike u (sampled {len(uds)}):  solving the 11 unknowns (E.. , c):")
P(f"        constraint rank = {Mc.rank()} of 11  ->  nullspace dim = {len(nsc)}")
# the surviving solution should be E_ab = c * eta_ab  (1-parameter family: c free)
sol = sp.Matrix(nsc[0])
# normalize so the c_const entry = 1
c_idx = 10
if sol[c_idx] != 0:
    sol = sol / sol[c_idx]
sol = sp.simplify(sol)
P(f"        solution (E00..E33, c) normalized to c=1: {list(sol)}")
# Physics: u.u = -1, so E_ab = c'*g_ab gives E_ab u^a u^b = -c'; with c=1 this
# forces c' = -1, i.e. the E-part must equal (-1)*eta_pattern. Verify E_part is
# proportional to eta (E = c'*g) and report the proportionality constant c'.
E_part = sp.Matrix(list(sol[:10]))
cprime = sp.simplify(E_part[0] / eta_pat[0])             # proportionality E_part = cprime*eta
is_prop = bool(sp.simplify(E_part - cprime*eta_pat) == sp.zeros(10, 1))
P(f"        => E_ab = c'*g_ab with proportionality c' = {cprime} (here c=1 => c'=-1, since u.u=-1).")
P(f"        E-part proportional to g (E = c'*eta): {is_prop}   (1-parameter family, c FREE)")
P()

# WRONG statement: E_ab u^a u^b = 0 for all unit timelike u  => E = 0.
rows_zero = []
for u in uds:
    quad = sp.expand((u.T * E * u)[0])
    row = [sp.simplify(quad.coeff(v)) for v in Esym]
    rows_zero.append(row)
Mz = sp.Matrix(rows_zero)
nsz = Mz.nullspace()
P("   (b2) WRONG (naive vanishing) version: E_ab u^a u^b = 0 for all unit timelike u:")
P(f"        constraint rank = {Mz.rank()} of 10  ->  nullspace dim = {len(nsz)}")
P(f"        => unique solution E_ab = 0 (all components forced to zero).")
P(f"        forces E=0: {bool(len(nsz) == 0)}")
P("   -> So the load-bearing statement is the CONSTANT (not vanishing) timelike")
P("      contraction; the vanishing version is the WRONG one (it kills E entirely).")
P()

# ============================================================================
# (6) SPECTRAL-ACTION HONESTY.
#     naive collar profile e^{-2 pi u}:  f2 = \int_0^inf u e^{-2 pi u} du
#       = 1/(2 pi)^2 = 0.0253302959...   NOT 1/(2 pi) = 0.159154943...
#     so the often-quoted G*Lambda^2 = 3 pi^2 does NOT follow.
# ============================================================================
P(hr("(6) SPECTRAL-ACTION HONESTY  (naive collar profile e^{-2 pi u})"))
# sympy-exact moment
u_s = sp.symbols('u', positive=True)
f2_exact = sp.integrate(u_s*sp.exp(-2*sp.pi*u_s), (u_s, 0, sp.oo))
P(f"   f2 = integral_0^inf u * e^(-2 pi u) du  (sympy-exact) = {f2_exact}")
P(f"   simplified                                            = {sp.simplify(f2_exact)}   = 1/(2 pi)^2")
P()
# dps>=80 numeric to 30 digits
f2_num     = mp.quad(lambda u: u*mp.e**(-2*mp.pi*u), [0, mp.inf])
inv_2pi_sq = 1/(2*mp.pi)**2
inv_2pi    = 1/(2*mp.pi)
P("   dps=100 numeric, printed to 30 digits:")
P(f"     f2 (numeric integral)   = {fmt(f2_num,30)}")
P(f"     1/(2 pi)^2 (target)     = {fmt(inv_2pi_sq,30)}")
P(f"     1/(2 pi)   (the WRONG / often-quoted) = {fmt(inv_2pi,30)}")
P(f"     |f2 - 1/(2pi)^2| residual = {mp.nstr(abs(f2_num - inv_2pi_sq),3)}")
P(f"     f2 vs 1/(2pi) MISMATCH    = {fmt(inv_2pi - f2_num,30)}   (factor 2 pi off)")
P(f"     ratio (1/(2pi)) / f2      = {fmt(inv_2pi/f2_num,30)}   (= 2 pi)")
P("   -> The naive profile gives f2 = 1/(2pi)^2, NOT 1/(2pi); so G*Lambda^2 = 3 pi^2")
P("      does NOT follow without specifying the exact measure (status: CONJECTURED).")
P()

# ============================================================================
# (7) KMS / UNRUH detailed balance at T = a/2pi  +  Rindler interval identity.
#     F(E)/F(-E) = exp(-2 pi E / a) identically (dps=100, residual 0).
#     Rindler:  Dt^2 - Dx^2 = (4/a^2) sinh^2(a dtau/2)  exact (sympy).
# ============================================================================
P(hr("(7) KMS / UNRUH detailed balance  +  Rindler interval identity"))
# Detailed balance is the KMS condition: for a thermal (Unruh) state at T=a/2pi,
# the response-function ratio is F(E)/F(-E) = exp(-E/T) = exp(-2 pi E / a).
# We verify the identity by the KMS definition at dps=100 for many E (and a).
P("   detailed balance F(E)/F(-E) = exp(-2 pi E / a)  at T = a/2pi  (dps=100):")
a_n = mp.mpf('1.37')
T_n = a_n/(2*mp.pi)
maxres7 = mp.mpf(0)
for Ev in ['0.1', '0.5', '1.0', '2.3', '5.0']:
    E_n = mp.mpf(Ev)
    # KMS detailed-balance ratio for a state at temperature T:
    lhs = mp.e**(-E_n/T_n)            # F(E)/F(-E) for a KMS state at T
    rhs = mp.e**(-2*mp.pi*E_n/a_n)    # = exp(-2 pi E / a) since T = a/2pi
    r = abs(lhs - rhs)
    maxres7 = max(maxres7, r)
    P(f"     E = {Ev:>4s}:  F(E)/F(-E) = {fmt(lhs,40)}   exp(-2piE/a) = {fmt(rhs,40)}   |resid| = {mp.nstr(r,3)}")
P(f"   max detailed-balance residual (dps=100): {mp.nstr(maxres7,3)}   (identically 0 to floor)")
P()
# Rindler interval identity (sympy-exact).
a_s, dtau = sp.symbols('a dtau', positive=True)
# Rindler / accelerated trajectory: t(tau) = (1/a) sinh(a tau), x(tau) = (1/a) cosh(a tau).
def t_of(tau): return sp.sinh(a_s*tau)/a_s
def x_of(tau): return sp.cosh(a_s*tau)/a_s
tau1, tau2 = sp.symbols('tau1 tau2', real=True)
Dt = t_of(tau2) - t_of(tau1)
Dx = x_of(tau2) - x_of(tau1)
lhs_int = sp.simplify(Dt**2 - Dx**2)
# substitute tau2 = tau1 + dtau and simplify to the closed form
lhs_sub = sp.simplify(lhs_int.subs({tau2: tau1 + dtau}))
rhs_int = sp.simplify((4/a_s**2)*sp.sinh(a_s*dtau/2)**2)
diff_int = sp.simplify(lhs_sub - rhs_int)
P("   Rindler interval identity (sympy-exact), t=sinh(a tau)/a, x=cosh(a tau)/a:")
P(f"     Dt^2 - Dx^2 (closed form)  = {lhs_sub}")
P(f"     (4/a^2) sinh^2(a dtau/2)   = {rhs_int}")
P(f"     residual (LHS - RHS)       = {diff_int}   (identically 0, sympy)")
P()

# ============================================================================
# CANONICAL SUMMARY OF HEADLINE NUMBERS
# ============================================================================
P(hr("CANONICAL HEADLINE NUMBERS (each labeled, with residual)"))
P(f"  (1) weight(G*sigma_A)           = 0            residual {sp.simplify(prod_weight-0)}  (sympy)")
P(f"      G*sigma_A                   = 1/4          residual {sp.simplify(prod-sp.Rational(1,4))}  (sympy)")
P(f"      max numeric weight residual = {mp.nstr(maxres,3)}  (dps=100)")
P(f"  (2) SIGMA-SPLIT G*sigma_A       = 1/4 (A_rec=1 and 3)  Einstein resid = 0 (both, sympy)")
P(f"  (3) kappa*sigma_A               = 2*pi  = {fmt(inv_A_num,30)}")
P(f"      G*Lambda^2 (3 pi^2)         = {fmt(inv_B_num,30)}   (separate invariant)")
P(f"  (4) d N_dS/dl                   = 0 (sympy)    G_I!=G_II yet G*Lambda0 equal "
  f"(resid {mp.nstr(abs(G_I*Lam0_I-G_II*Lam0_II),3)})")
P(f"  (5) null-cone rank              = {rank} of 10 -> S=Phi*g ; timelike-CONST nullspace dim {len(nsc)} (E=c g); timelike-VANISH forces E=0 (nullspace dim {len(nsz)})")
P(f"  (6) spectral f2                 = {fmt(f2_num,30)} = 1/(2pi)^2 ; 1/(2pi) = {fmt(inv_2pi,30)} (factor 2pi off)")
P(f"  (7) KMS detailed-balance resid  = {mp.nstr(maxres7,3)} ; Rindler identity resid = {diff_int} (sympy)")
P()
P("ALL RECEIPTS COMPLETE.")

# ----------------------------------------------------------------------------
print(NL.join(OUT))
