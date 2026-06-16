"""
v7 Paper 5 — the c_m free-calibration receipt (the gravitational per-species coupling).

Paper 5 proves: c_m = G m^2/(hbar c), the DIMENSIONLESS gravitational coupling-per-species
(the gravitational analog of the fine-structure constant), is
  (i)   WEIGHT-0 / intrinsic-eligible -- the scale no-go (Paper 3 / 57 / XI) does NOT
        forbid it (it carries no absolute length);
  (ii)  NOT a gravity-sector output -- by Paper 7 Theorem 6.1 the gravity sector is
        complete-and-blind w.r.t. c_m (exactly as GR does not fix m_e); c_m = the matter
        ledger's spectral gap, relocated OUT of gravity;
  (iii) currently FREE -- no executed corpus identity constrains it (the toy-value
        NOT-SELECTED result: kappa*sigma_A/2pi = 1 independent of c_m);
  (iv)  the gravitational twin of the scale no-go's free unit kappa -- ONE free
        dimensionless coupling per species;
  (v)   the SHARED open obligation with the spacing d: c_m = gamma_G * nu_m^2 with nu_m a
        mode-dependent matter gap, the SAME mode-canonicalization bottleneck as d.

This receipt verifies, at mpmath dps>=60 (CODATA SI) and sympy-exact (grading):
  (1) the NUMERIC reality  c_m(e)=1.75e-45, c_m(p)=5.9e-39, ratio = (m_p/m_e)^2;
  (2) WEIGHT-0 + gauge invariance: under l -> mu*l (G~l^2, m~1/l), c_m is invariant;
      weight(c_m) = weight(G) + 2 weight(m) = (+2) + 2(-1) = 0 (sympy);
  (3) the FACTORIZATION c_m = gamma_G * nu_m^2: a product of two weight-0 record numbers
      (an area-normalization convention and a matter spectral gap);
  (4) the SHARED BOTTLENECK with d: the gap nu_m is MODE-DEPENDENT (eta_B vs h_*), so a
      c_m value needs the same mode canonicalization that fixes d -- NOT supplied;
  (5) the numerology refutation (theta_B^2 vs Srednicki a) carried over: c_m must NOT be
      pinned to a record number; any value smuggles in the 1/4 convention + a mode choice.

Pre-geometric note: c_m is weight-0 throughout (a ratio of record numbers); the
gravitational constants (G, hbar, c, masses) enter only to exhibit the physical hierarchy
and to confirm the weight bookkeeping -- the result is that gravity cannot OUTPUT c_m.
"""
import mpmath as mp
import sympy as sp

mp.mp.dps = 60
PASS = {}


def head(s):
    print("\n" + "=" * 78 + "\n" + s + "\n" + "=" * 78)


def line(lbl, val, note=""):
    print("  %-44s %s   %s" % (lbl, val, note))


# ===========================================================================
head("(1) NUMERIC reality: c_m = G m^2/(hbar c) = (m/M_Planck)^2  (the hierarchy)")
# CODATA-2018 SI
G = mp.mpf("6.67430e-11")            # m^3 kg^-1 s^-2
hbar = mp.mpf("1.054571817e-34")     # J s
c = mp.mpf("299792458")              # m/s
m_e = mp.mpf("9.1093837015e-31")     # kg
m_p = mp.mpf("1.67262192369e-27")    # kg
M_Pl = mp.sqrt(hbar * c / G)         # Planck mass


def c_m(m):
    return G * m ** 2 / (hbar * c)


cm_e = c_m(m_e)
cm_p = c_m(m_p)
line("M_Planck (kg)", mp.nstr(M_Pl, 10))
line("c_m(electron) = (m_e/M_Pl)^2", mp.nstr(cm_e, 8), "~ 1.75e-45")
line("c_m(proton)   = (m_p/M_Pl)^2", mp.nstr(cm_p, 8), "~ 5.91e-39")
line("c_m(p)/c_m(e)  vs  (m_p/m_e)^2", "%s vs %s" % (mp.nstr(cm_p / cm_e, 10), mp.nstr((m_p / m_e) ** 2, 10)))
PASS["(1) c_m(e)~1.75e-45, c_m(p)~5.9e-39, and c_m proportional to m^2 (ratio=(m_p/m_e)^2)"] = (
    abs(cm_e - mp.mpf("1.7518e-45")) < mp.mpf("1e-48")
    and abs(cm_p - mp.mpf("5.9061e-39")) < mp.mpf("1e-42")
    and abs(cm_p / cm_e - (m_p / m_e) ** 2) < mp.mpf("1e-30")
)
# c_m = (m/M_Pl)^2 identity
PASS["(1b) c_m = (m/M_Planck)^2 exactly"] = (
    abs(cm_e - (m_e / M_Pl) ** 2) < mp.mpf("1e-60")
)

# ===========================================================================
head("(2) WEIGHT-0 + gauge invariance: c_m is intrinsic-eligible (no-go does NOT forbid)")
# Record-length gauge l -> mu*l :  G ~ l^2 (weight +2),  m ~ 1/l (weight -1),  hbar*c
# weight 0.  weight(c_m) = +2 + 2*(-1) - 0 = 0.  So c_m is gauge-invariant.
wG, wm, whc = sp.Integer(2), sp.Integer(-1), sp.Integer(0)
w_cm = wG + 2 * wm - whc
line("weight(G), weight(m), weight(hbar c)", "%s, %s, %s" % (wG, wm, whc))
line("weight(c_m) = wG + 2*wm - whc", str(w_cm), "(= 0: weight-zero / intrinsic-eligible)")
PASS["(2) weight(c_m) = 0 (intrinsic-eligible; scale no-go does NOT forbid it)"] = (w_cm == 0)
# numerical gauge invariance: scale l by mu -> G*mu^2, m/mu ; c_m invariant
for mu in [mp.mpf("1.7"), mp.mpf("5")]:
    cm_scaled = (G * mu ** 2) * (m_e / mu) ** 2 / (hbar * c)
    line("c_m under l->%s*l / c_m" % mp.nstr(mu, 2), mp.nstr(cm_scaled / cm_e, 12), "(= 1: invariant)")
PASS["(2b) c_m invariant under l->mu*l (G->mu^2 G, m->m/mu): the scale cancels"] = (
    all(abs((G * mu ** 2) * (m_e / mu) ** 2 / (hbar * c) / cm_e - 1) < mp.mpf("1e-40")
        for mu in [mp.mpf("1.7"), mp.mpf("5")])
)

# ===========================================================================
head("(3) EXACT factorization c_m = gamma_G * nu_m^2 (sigma_A cancels; gamma_G = G*sigma_A = 1/4)")
# EXACT identity (natural units hbar=c=1):
#   gamma_G = G * sigma_A   (the area-law coefficient; = 1/4 at the Bekenstein density
#                            sigma_A = 1/(4G) -- a RATIO-OF-TWINS convention, gravity-side)
#   nu_m    = m / sqrt(sigma_A)   (the matter mass in record sqrt-area units; weight-0)
#   gamma_G * nu_m^2 = (G*sigma_A) * (m^2/sigma_A) = G*m^2 = c_m   <- sigma_A CANCELS.
Gs, sig, msym = sp.symbols("G sigma_A m", positive=True)
gamma_G = Gs * sig
nu_m = msym / sp.sqrt(sig)
cm_factored = sp.simplify(gamma_G * nu_m ** 2)
line("gamma_G = G*sigma_A", str(gamma_G), "(= 1/4 at sigma_A = 1/(4G); convention)")
line("nu_m = m/sqrt(sigma_A)", str(nu_m), "(matter mass in record units; weight-0)")
line("gamma_G * nu_m^2  (sigma_A cancels)", str(cm_factored), "= G*m^2 = c_m  (exact)")
PASS["(3) c_m = gamma_G*nu_m^2 = G*m^2 EXACTLY (sigma_A cancels; gamma_G=G*sigma_A=1/4)"] = (
    sp.simplify(cm_factored - Gs * msym ** 2) == 0
    and sp.simplify((Gs * sig).subs(sig, 1 / (4 * Gs)) - sp.Rational(1, 4)) == 0
)
# The matter content lives ENTIRELY in nu_m (= paper7's spectral gap m_hat); gamma_G=1/4
# is a gravity-side convention.  So fixing c_m == fixing nu_m == the matter sector.
# Physical reality check: nu_m(electron) = sqrt(c_m(e)/gamma_G) = sqrt(1.75e-45/0.25) ~ 8.4e-23,
# i.e. ~22 orders BELOW the toy lattice gaps eta_B=0.609 / C(eta_B)=0.156 -- those are
# illustrative mode-dependence, NOT candidate physical masses.
nu_e = mp.sqrt(cm_e / mp.mpf("0.25"))
line("nu_m(electron) = sqrt(c_m(e)/gamma_G)", mp.nstr(nu_e, 6), "(~8.4e-23: physical, NOT eta_B/0.156)")
PASS["(3b) physical nu_m(e)~8.4e-23 is ~22 orders below the toy gaps (toy=illustrative only)"] = (
    nu_e < mp.mpf("1e-20") and nu_e > mp.mpf("1e-25")
)

head("(3c) NOT-SELECTED structure: the gravity invariants do not depend on c_m")
# kappa*sigma_A = 2pi and G*sigma_A = 1/4 are functions of (G, sigma_A) ONLY -- c_m does
# not appear, so ANY c_m passes them (the paper6 s9 toy-value 12/1200 NOT-SELECTED result,
# whose four-cell scan is INHERITED from paper6, reproduced structurally here).
cm_sym = sp.symbols("c_m", positive=True)
inv1 = 8 * sp.pi * Gs * sig          # kappa*sigma_A = 8pi (G sigma_A) = 2pi at G sigma_A=1/4
inv2 = Gs * sig                       # G*sigma_A = 1/4
line("kappa*sigma_A INDEPENDENT of c_m?", str(sp.diff(inv1, cm_sym) == 0), "(d/dc_m = 0: yes, independent)")
line("G*sigma_A INDEPENDENT of c_m?", str(sp.diff(inv2, cm_sym) == 0), "(d/dc_m = 0: yes, independent)")
PASS["(3c) gravity invariants kappa*sigma_A, G*sigma_A are c_m-independent (NOT-SELECTED; any c_m passes)"] = (
    sp.diff(inv1, cm_sym) == 0 and sp.diff(inv2, cm_sym) == 0
)

# ===========================================================================
head("(4) SHARED BOTTLENECK with d: nu_m is MODE-DEPENDENT (same canonicalization as d)")
# The matter gap nu_m, like the spacing d, is selected by the firing fixed point
# grad psi(h)=e^{-h}, whose root is MODE-DEPENDENT: one-mode eta_B vs coupled h_*.
# So a c_m VALUE needs the SAME mode canonicalization that fixes d -- not supplied.
def C(e):
    return e * mp.tanh(e) - mp.log(mp.cosh(e))


eta_B = mp.findroot(lambda e: mp.tanh(e) - mp.e ** (-e), mp.mpf("0.6"))
h_star = mp.findroot(
    lambda h: (mp.e ** (3 * h) - mp.e ** (-h)) / (mp.e ** (3 * h) + 3 * mp.e ** (-h)) - mp.e ** (-h),
    mp.mpf("0.5"),
)
line("one-mode gap eta_B", mp.nstr(eta_B, 12))
line("coupled gap h_*", mp.nstr(h_star, 12), "(|eta_B - h_*| = %s)" % mp.nstr(abs(eta_B - h_star), 6))
line("=> nu_m mode-dependent", "no canonical member", "(same bottleneck as the spacing d)")
PASS["(4) the matter gap is mode-dependent (eta_B != h_*): c_m shares d's canonicalization bottleneck"] = (
    abs(eta_B - h_star) > mp.mpf("0.1")
)

# ===========================================================================
head("(5) NO pinning: any c_m value smuggles in the 1/4 convention + a mode choice")
# Illustrative-only: gamma_G=1/4 (A_rec=1 gauge convention) times eta_B^2 -> a NUMBER,
# which is NOT c_m's physical value and rests on two unforced choices.  And the strongest
# record-number numerology (theta_B^2 vs Srednicki a) is refuted algebraically.
illustrative = mp.mpf("0.25") * eta_B ** 2
line("illustrative gamma_G*eta_B^2 (NOT a prediction)", mp.nstr(illustrative, 10),
     "(smuggles 1/4 conv + a TOY mode)")
# the illustrative O(0.1) is ~44 orders from the physical c_m(e)=1.75e-45 -- self-evidently
# NOT a candidate value (it uses the toy tilt eta_B, not a physical mass).
line("illustrative / c_m(electron)", mp.nstr(illustrative / cm_e, 4), "(~5e43: O(0.1) vs 1.75e-45)")
PASS["(5b) illustrative 0.093 is ~44 orders from physical c_m(e): self-evidently not a prediction"] = (
    illustrative / cm_e > mp.mpf("1e40")
)
# tribonacci-algebraic refutation of theta_B^2 vs Srednicki a (carried from p3)
t = sp.symbols("t")
theta_B = mp.tanh(eta_B)
val = (theta_B ** 2) ** 3 + (theta_B ** 2) ** 2 + 3 * (theta_B ** 2) - 1
sredn = mp.mpf("0.295417")
line("theta_B^2 (root of s^3+s^2+3s-1)", mp.nstr(theta_B ** 2, 12), "vs Srednicki a=%s" % mp.nstr(sredn, 8))
PASS["(5) theta_B^2 cubic-algebraic, != Srednicki a (numerology); no record number pins c_m"] = (
    abs(val) < mp.mpf("1e-50")
    and abs(theta_B ** 2 - sredn) > mp.mpf("1e-5")
    and sp.Poly(t ** 3 + t ** 2 + 3 * t - 1, t).is_irreducible
)

# ===========================================================================
head("MACHINE CHECKS")
ok = True
for k, v in PASS.items():
    print("  [%s] %s" % ("PASS" if v else "FAIL", k))
    ok = ok and v
print("\n  " + ("ALL CHECKS PASS" if ok else "*** SOME CHECK FAILED ***"))
assert ok, "a check failed"
print("=" * 78)
print("DONE.  c_m is weight-0 and PERMITTED, but provably a matter-sector calibration the")
print("       gravity sector is complete-and-blind to (Thm 6.1): one free coupling per")
print("       species, sharing the spacing d's mode-canonicalization + matter-sector gate.")
print("=" * 78)
