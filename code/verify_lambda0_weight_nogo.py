"""
ADVERSARIAL no-go leak test: can any record self-consistency / dynamical
condition intrinsically FIX the weight-(-2) VALUE of the unimodular Lambda0,
rather than only the weight-0 product G*Lambda0 ?

Gauge group (paper6 Theorem G, paper57 sec 2): the unit action g_lambda sends
the discreteness/record length  l = A_rec^{1/2}  ->  mu * l   (length weight +1),
holding ALL sealed/record data fixed.  Induced area weights:
    A_rec   : +2      (it is l^2)
    sigma_A : -2      (entropy per geometric area)
    kappa   : +2
    G       : +2      (G*sigma_A = 1/4 weight-0)
    Lambda0 : -2      (a cosmological constant is an inverse length^2)
An INTRINSIC record functional factors through the record sector R, on which
g_lambda is the identity => it is weight-0 (Theorem G).  So NO intrinsic record
number can carry weight -2.  A mechanism "fixes Lambda0's value intrinsically"
ONLY IF it equates Lambda0 (weight -2) to a record-intrinsic quantity (weight 0)
WITHOUT introducing a free weight-(-2) modulus (the length l, or any other
gauge-charged unit).

We track weights symbolically with sympy and check the numerics at dps>=80
where a near-vacuum / spectral quantity appears.
"""

import sympy as sp
import mpmath as mp

mp.mp.dps = 100

# symbolic gauge parameter mu (length rescaling l -> mu*l) and weight bookkeeping
mu = sp.symbols('mu', positive=True)

def w(expr_weight):
    """return the mu-power that a quantity of length-weight `expr_weight` carries"""
    return mu**sp.Rational(expr_weight)

# canonical weights
W = {
    'l':       1,   # record/discreteness length  l = A_rec^{1/2}
    'A_rec':   2,
    'sigma_A':-2,
    'kappa':   2,
    'G':       2,
    'Lambda0':-2,   # cosmological constant ~ 1/length^2
    'Lambda':  -1,  # an inverse-length UV/spectral cutoff (mass dim +1 => length -1)
    'rho':    -4,   # an energy density ~ 1/length^4 in natural units
    'N':       0,   # a pure record COUNT is weight-0 (it is intrinsic)
    'number':  0,
}

print("="*72)
print("WEIGHT TABLE (length-rescaling l -> mu*l):")
for k,v in W.items():
    print(f"   {k:9s} weight {v:+d}   -> mu**{v}")
print("="*72)

report = {}

# ----------------------------------------------------------------------
# CANDIDATE (a): SAKHAROV-INDUCED vacuum energy / cosmological constant.
#   Induced  Lambda0_induced ~ (record cutoff)^4 * G   [the standard
#   one-loop vacuum-energy estimate, rho_vac ~ Lambda_UV^4, fed into
#   Lambda0 = 8 pi G rho_vac]. The corpus also quotes the induced-gravity
#   relation  G*Lambda^2 = (pure number)/N  (here written 192 pi^2 / N).
# Question: does this give a record-intrinsic VALUE for Lambda0 (weight -2),
#   or does it merely re-express it via the free length modulus l ?
# ----------------------------------------------------------------------
print("\n[CANDIDATE a]  SAKHAROV-INDUCED Lambda0\n")

# The record UV cutoff is an inverse length.  Sealed records carry no absolute
# length, so the ONLY inverse length the records can build is 1/l (paper57 2.2:
# 'the reference scale is forced to be 1/l').  Hence:
Lambda_UV = sp.Symbol('Lambda_UV', positive=True)   # = c_num / l, c_num weight-0
c_num = sp.Symbol('c_num', positive=True)            # pure record number, weight 0
l = sp.Symbol('l', positive=True)

# weight of Lambda_UV (an inverse length built from records):
wt_Lambda_UV = sp.Rational(-1)   # = c_num * l**(-1)

# induced vacuum energy density rho_vac ~ Lambda_UV^4  (weight -4)
wt_rho_vac = 4*wt_Lambda_UV
# induced cosmological constant Lambda0 = 8 pi G rho_vac  (G weight +2)
wt_Lambda0_induced = W['G'] + wt_rho_vac
print(f"   Lambda_UV  weight = {wt_Lambda_UV}  (records' only inverse length is 1/l)")
print(f"   rho_vac ~ Lambda_UV^4   weight = {wt_rho_vac}")
print(f"   Lambda0 = 8piG rho_vac  weight = {wt_Lambda0_induced}  "
      f"(must be -2 for a CC)")

# Check 1: is the INDUCED Lambda0 dimensionally a genuine weight -2 object?
induced_is_weight_minus2 = (wt_Lambda0_induced == -2)
# Sakharov induced gravity gives 1/G ~ N * Lambda_UV^2, i.e. G*Lambda_UV^2 = const/N
# (the corpus writes G*Lambda^2 = 192 pi^2 / N).  Symbolically:
N = sp.Symbol('N', positive=True)
G = sp.Symbol('G', positive=True)
# induced relation: G * Lambda_UV^2 = K / N  with K a pure number
K = sp.Symbol('K', positive=True)
induced_rel = sp.Eq(G*Lambda_UV**2, K/N)
# weight of LHS:
wt_GLambda2 = W['G'] + 2*wt_Lambda_UV
print(f"   G*Lambda_UV^2 weight = {wt_GLambda2}  (RHS K/N is weight 0)")

# Now the leak test: does the induced relation SOLVE for Lambda0's value
# without a residual free weight-(-2) quantity?  Substitute Lambda_UV = c_num/l:
Lambda0_induced_expr = 8*sp.pi*G*(c_num/l)**4      # = 8 pi G c_num^4 / l^4
# and G is itself only known via G = (K/N)/Lambda_UV^2 = (K/N) l^2 / c_num^2:
G_from_induced = (K/N) * l**2 / c_num**2
Lambda0_final = Lambda0_induced_expr.subs(G, G_from_induced)
Lambda0_final = sp.simplify(Lambda0_final)
print(f"   substitute G(induced) and Lambda_UV=c_num/l:")
print(f"     Lambda0 = {Lambda0_final}")
# extract residual l-power
poly_l = sp.Poly(sp.together(Lambda0_final).as_numer_denom()[0], l)
# simpler: get the exponent of l in Lambda0_final
l_exp = sp.degree(sp.numer(Lambda0_final), l) - sp.degree(sp.denom(Lambda0_final), l)
print(f"     residual power of l = {l_exp}   "
      f"(0 would mean Lambda0 became a pure record number = LEAK)")
report['a'] = {
    'induced_weight_of_Lambda0': int(wt_Lambda0_induced),
    'Lambda0_after_substitution': str(Lambda0_final),
    'residual_l_power': int(l_exp),
    'leaks': bool(l_exp == 0),
}

# numeric sanity at high precision: pick record numbers, vary the gauge modulus l
mp.mp.dps = 90
c_num_v = mp.mpf('1.0')
K_v = 192*mp.pi**2
N_v = mp.mpf('1e122')        # de Sitter record count order (S_dS ~ 1e122)
def Lambda0_of_l(lval):
    Gv = (K_v/N_v) * lval**2 / c_num_v**2
    return 8*mp.pi*Gv*(c_num_v/lval)**4
v1 = Lambda0_of_l(mp.mpf('1.0'))
v2 = Lambda0_of_l(mp.mpf('1.7'))    # gauge rescale mu=1.7
ratio = v2/v1
print(f"   NUMERIC (dps90): Lambda0(l=1)   = {mp.nstr(v1,12)}")
print(f"                    Lambda0(l=1.7) = {mp.nstr(v2,12)}")
print(f"                    ratio          = {mp.nstr(ratio,12)}  "
      f"(expected mu^{l_exp} = {mp.nstr(mp.mpf('1.7')**int(l_exp),12)})")
report['a']['gauge_ratio'] = mp.nstr(ratio, 16)
report['a']['expected_mu_power'] = mp.nstr(mp.mpf('1.7')**int(l_exp), 16)

# ----------------------------------------------------------------------
# CANDIDATE (b): SEALING-RATE / BACK-REACTION EQUILIBRIUM fixed point.
#   Unimodular law:  d Lambda/dt = 8 pi G * eta,  eta = w*u  (w = sealing/
#   commitment heating power density, weight -4 since [energy]/[volume]).
#   A 'fixed point' would balance commitment heating against expansion:
#       w  ==  (expansion drain of vacuum energy)  ~  H * rho_Lambda
#   with H the Hubble rate (weight -1, an inverse length/time) and
#   rho_Lambda = Lambda0/(8 pi G) (weight -2 - 2 = -4).  Test whether this
#   self-consistency yields a VALUE for Lambda0 or only a weight-0 condition.
# ----------------------------------------------------------------------
print("\n[CANDIDATE b]  SEALING-RATE / BACK-REACTION EQUILIBRIUM\n")

# weights
wt_w   = -4          # heating power per volume (energy/volume/... ); take -4 (per length^4)
wt_H   = -1          # Hubble ~ 1/length
wt_rhoLambda = W['Lambda0'] - W['G']    # rho_L = Lambda0/(8 pi G)
print(f"   rho_Lambda = Lambda0/(8 pi G) weight = {wt_rhoLambda}")
# Equilibrium condition  w == H * rho_Lambda  :
wt_LHS = wt_w
wt_RHS = wt_H + wt_rhoLambda
print(f"   equilibrium  w == H*rho_Lambda : LHS weight {wt_LHS}, RHS weight {wt_RHS}")
balanced = (wt_LHS == wt_RHS)
print(f"   weights match? {balanced}  "
      f"(if they match the condition is a weight-0 RATIO equation)")
# The condition, made dimensionless, is  w/(H*rho_Lambda) = 1 : weight  (-4)-(-1)-(-4)= +1??
wt_dimensionless = wt_w - wt_H - wt_rhoLambda
print(f"   the ratio w/(H rho_L) has weight {wt_dimensionless} "
      f"(0 => it is a pure-number CONDITION, fixes no scale)")

# Crucial adversarial point: does the fixed point SOLVE for Lambda0, or does it
# just relate Lambda0 to H (another weight-charged cosmological datum) and to w
# (a record RATE)?  A record commitment RATE is events per (record 4-volume),
# i.e. (count)/l^4  -> weight -4, with the count weight-0.  So:
n_rate = sp.Symbol('n_rate', positive=True)   # record number, weight 0
w_seal = n_rate / l**4                          # heating density from sealing
H = sp.Symbol('H', positive=True)               # weight -1 cosmological datum
Lambda0 = sp.Symbol('Lambda0', positive=True)
rho_L = Lambda0/(8*sp.pi*G)
eqb = sp.Eq(w_seal, H*rho_L)
Lambda0_solved = sp.solve(eqb, Lambda0)[0]
print(f"   solve equilibrium for Lambda0:")
print(f"     Lambda0 = {Lambda0_solved}")
# This still contains G, H, l : substitute G = (K/N) l^2 / c_num^2 (induced) to
# see if Lambda0 becomes record-intrinsic; H is a FREE cosmological datum.
Lambda0_solved_sub = Lambda0_solved.subs(G, (K/N)*l**2/c_num**2)
Lambda0_solved_sub = sp.simplify(Lambda0_solved_sub)
print(f"     with G(induced): Lambda0 = {Lambda0_solved_sub}")
free_syms = Lambda0_solved_sub.free_symbols
print(f"     free symbols remaining = {sorted([str(s) for s in free_syms])}")
# does H (a weight-(-1) external datum) survive?  if so the value is set by the
# external expansion rate, not by the records.
H_survives = (H in free_syms)
l_survives = (l in free_syms)
report['b'] = {
    'weights_balance': bool(balanced),
    'dimensionless_condition_weight': int(wt_dimensionless),
    'Lambda0_solved': str(Lambda0_solved_sub),
    'external_H_survives': bool(H_survives),
    'gauge_length_l_survives': bool(l_survives),
    'leaks': bool((not H_survives) and (not l_survives)),
}

# ----------------------------------------------------------------------
# CANDIDATE (c): DYNAMICAL-LAMBDA SELF-TUNING / SEQUESTERING.
#   Sequestering (Kaloper-Padilla): the global constraint
#       <rho_vac> = (1/4) <T>   (trace average over spacetime 4-volume)
#   makes the net Lambda depend on the 4-VOLUME of the universe, removing the
#   radiative-correction sensitivity.  Test: does the sequester constraint
#   pin Lambda0's VALUE intrinsically, or does it fix only the (weight-0) ratio
#   Lambda0 * V4^{1/2}-type combination and import the 4-volume (a weight +4
#   external datum)?
# ----------------------------------------------------------------------
print("\n[CANDIDATE c]  SEQUESTERING / SELF-TUNING dynamical Lambda\n")

V4 = sp.Symbol('V4', positive=True)     # spacetime 4-volume, weight +4 (length^4)
Tbar = sp.Symbol('Tbar')                # spacetime-averaged trace of T, weight -4
# Kaloper-Padilla:  Lambda_eff = (1/4)<T> = (1/V4) integral(T) /4 .  The residual
# (historic) Lambda is  Lambda_eff ~ <T> which is a 4-volume-AVERAGE.
# weight of <T> = -4 ; weight of Lambda_eff (as a CC, ~1/length^2) requires *G:
Lambda_eff = 2*sp.pi*G*Tbar     # schematic: Lambda ~ G * <T>
wt_Lambda_eff = W['G'] + (-4)
print(f"   sequester Lambda_eff ~ G<T>, weight = {wt_Lambda_eff}  (a CC needs -2)")
# This is weight -2 ONLY accidentally?  G<T> = (+2)+(-4) = -2. GOOD - it IS a CC.
# But the VALUE is <T>, the running average of the matter trace over the cosmic
# 4-volume -> set by the matter content and the 4-volume, i.e. by an external
# cosmological history, NOT by an intrinsic record number.
seq_weight_ok = (wt_Lambda_eff == -2)
# Does it become record-intrinsic? <T> is weight -4: the records' only weight-(-4)
# object is (number)/l^4.  So Lambda_eff = G * number / l^4 = [(K/N) l^2] * number / l^4
Lambda_eff_records = ((K/N)*l**2/c_num**2) * (sp.Symbol('m_num',positive=True)/l**4)
Lambda_eff_records = sp.simplify(Lambda_eff_records)
l_exp_c = sp.degree(sp.numer(Lambda_eff_records), l) - sp.degree(sp.denom(Lambda_eff_records), l)
print(f"   if <T> is record-built (number/l^4): Lambda_eff = {Lambda_eff_records}")
print(f"     residual power of l = {l_exp_c}  (0 => LEAK)")
report['c'] = {
    'sequester_weight_is_minus2': bool(seq_weight_ok),
    'Lambda_eff_records': str(Lambda_eff_records),
    'residual_l_power': int(l_exp_c),
    'leaks': bool(l_exp_c == 0),
    'note': 'value = spacetime average <T>, an external cosmological-history datum',
}

# ----------------------------------------------------------------------
# THE de SITTER RELATION (the named "leak" route):
#   S_dS = pi/(G*Lambda0) = N_dS  (de Sitter horizon entropy = record count).
#   N_dS is weight-0 (a count).  Does this fix G or Lambda0 separately?
# ----------------------------------------------------------------------
print("\n[de SITTER relation]  S_dS = pi/(G*Lambda0) = N_dS\n")
N_dS = sp.Symbol('N_dS', positive=True)   # record count, weight 0
relation = sp.Eq(sp.pi/(G*Lambda0), N_dS)
# weight of pi/(G*Lambda0):
wt_product = -(W['G'] + W['Lambda0'])   # = -((+2)+(-2)) = 0
print(f"   weight of 1/(G*Lambda0) = {wt_product}  (RHS N_dS weight 0 => consistent)")
# The relation fixes the PRODUCT G*Lambda0 = pi/N_dS (weight 0). Solve:
GLambda0 = sp.solve(relation, G*Lambda0)
print(f"   => G*Lambda0 = pi/N_dS  (weight 0, a pure number). 1 eqn, 2 unknowns.")
# To fix Lambda0 alone you need a SECOND, weight-(-2) equation. The only way the
# records supply one is via l (the gauge modulus).  Demonstrate the residual
# gauge freedom: G*Lambda0 fixed, but (G,Lambda0) slides along the orbit
# G->mu^2 G, Lambda0->mu^-2 Lambda0 leaving the product invariant.
print("   gauge orbit: G->mu^2 G, Lambda0->mu^-2 Lambda0 keeps G*Lambda0 fixed.")
# numeric: product fixed, value free
mp.mp.dps = 100
N_dS_v = mp.mpf('1e122')
prod = mp.pi/N_dS_v
for muval in ['1.0','1.7','1e10']:
    m = mp.mpf(muval)
    Gv = m**2 * mp.mpf('1.0')
    Lv = prod/Gv
    print(f"     mu={muval:6s}: G={mp.nstr(Gv,6)}  Lambda0={mp.nstr(Lv,6)}  "
          f"product={mp.nstr(Gv*Lv,8)} (invariant)")
report['de_Sitter'] = {
    'product_weight': int(wt_product),
    'fixes': 'G*Lambda0 = pi/N_dS only (weight-0 product)',
    'second_equation_needed_weight': -2,
    'only_record_source_of_weight_-2': 'l (the gauge modulus) -> circular',
    'leaks': False,
}

# ----------------------------------------------------------------------
print("\n" + "="*72)
print("VERDICT PER CANDIDATE:")
for k in ['a','b','c','de_Sitter']:
    print(f"  ({k}) leaks = {report[k]['leaks']}")
any_leak = any(report[k]['leaks'] for k in report)
print(f"\n  ANY MECHANISM FIXES Lambda0's VALUE INTRINSICALLY ? -> {any_leak}")
print("="*72)
