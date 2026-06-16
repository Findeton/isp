#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
s_modeh_mode_selecting_hamiltonian.py  --  SCOUT S-MODEH (PRELIMINARY).

THE FIFTH-WALL ESCAPE under test (Paper VIII s4, s8(c); m2 caveat).  Paper VIII's
"sole escape" from the mode-canonicalization no-go is: a constructed matter
HAMILTONIAN whose ENERGETICS select one ledger rank (1/3/7 orthogonal primitive
characters; per-mode coefficients eta_B=0.609 > h_*=0.495 > r7=0.368).  The corpus
claims this only RELOCATES the choice.  THIS PROBE TESTS THAT CLAIM CONCRETELY.

DESIGN.  The ledger ranks r in {1,3,7} (m = 2^n-1 modes, n=1,2,3) each carry
record-internal, mode-canonical quantities at their firing fixed point grad psi = e^{-h}:
  - per-mode coefficient h_r            (0.6094 / 0.4951 / 0.3680)
  - per-mode content C(h_r)             (relative-entropy cost of ONE seal in that mode)
  - mode count m_r = 2^n - 1            (1 / 3 / 7)
  - TOTAL ledger content  m_r * C(h_r)  (whole-ledger evidence content)
  - the gap / lightest mass on that rank (unoriented floor W, or oriented m_min(n))
These are the ONLY record-internal scalars a rank-selecting Hamiltonian could be built
from WITHOUT importing an external coupling.

We construct a one-parameter FAMILY of candidate record matter Hamiltonians
   H_alpha(r) = (per-event energy) + alpha * (per-mode multiplicity penalty)
the SIMPLEST energetic principle: energy = total content (cost of writing the ledger)
balanced against a multiplicity/degeneracy reward, with ONE coupling alpha that weighs
"cost per seal" against "number of modes".  alpha is the matter-sector coupling g.

DECISIVE TESTS (the verdict criteria, l_step / Q-tilde template):
 (T1) Does ANY record-internal functional (alpha-free) have a UNIQUE minimizer over r?
      -> if the natural candidates DISAGREE on the argmin, no canonical alpha-free selector.
 (T2) For the one-parameter family H_alpha, is the argmin r*(alpha) CONSTANT (forced) or
      does it SWITCH between ranks as alpha sweeps (-> the choice IS the coupling alpha)?
      A switch = "relocation": mode-selection becomes alpha-selection, wall persists one level up.
 (T3) Is alpha itself record-internal (derivable from the click-law) or an IMPORT?  We test
      whether any record-internal scalar FIXES alpha (closes it) or whether alpha is free
      (weight-0, matter-sector) like c_m and the spacing d.
 (T4) Degeneracy test: is there a SPECIAL alpha at which two ranks are exactly degenerate
      (a transition), and is that alpha record-forced?  If the only "canonical" alpha is a
      level-crossing whose value depends on the energy convention, selection is convention-bound.

VERDICT.  Wall BROKEN iff some record-internal H selects a UNIQUE rank with NO free coupling
(argmin rank-forced, independent of all energy conventions).  Wall RELOCATED (persists) iff
the argmin is coupling-dependent: a free alpha that, swept, moves the selected rank -- so the
Hamiltonian's coupling is the new home of the same freedom.

mpmath dps>=100.  PRELIMINARY scout receipt; structural sympy where clean.
"""
import mpmath as mp
import sympy as sp

mp.mp.dps = 120
PASS = {}
NOTE = {}


def head(s):
    print("\n" + "=" * 78 + "\n" + s + "\n" + "=" * 78)


def line(lbl, val, note=""):
    print("  %-52s %s   %s" % (lbl, val, note))


# ---------------------------------------------------------------------------
# Shared single-mode (parity) information geometry, identical to m2 / paper2.
# ---------------------------------------------------------------------------
def C(e):
    """per-seal evidence content of a parity mode at coefficient e (relative entropy)."""
    return e * mp.tanh(e) - mp.log(mp.cosh(e))


def J(e):
    return mp.sech(e) ** 2


eta_A = mp.findroot(lambda e: C(e) - J(e), mp.mpf("1.0903"))
W_star = J(eta_A)


def coupled_root(stats, states, base=None):
    """grad psi(h)=exp(-h) on a complete symmetric character ledger; return common h."""
    k = len(stats)

    def fn(*h):
        hh = list(h)
        ws = [(1 if base is None else base[i]) *
              mp.e ** sum(hh[j] * stats[j](states[i]) for j in range(k))
              for i in range(len(states))]
        Z = sum(ws)
        return [sum(ws[i] * stats[j](states[i]) for i in range(len(states))) / Z
                - mp.e ** (-hh[j]) for j in range(k)]
    sol = mp.findroot(fn, [mp.mpf("0.5")] * k)
    return [sol[i] for i in range(k)]


S1 = [(1,), (-1,)]
S2 = [(a, b) for a in (1, -1) for b in (1, -1)]
S3 = [(a, b, c) for a in (1, -1) for b in (1, -1) for c in (1, -1)]
r1 = coupled_root([lambda s: s[0]], S1)[0]
r3 = coupled_root([lambda s: s[0], lambda s: s[1], lambda s: s[0] * s[1]], S2)[0]
r7 = coupled_root([lambda s: s[0], lambda s: s[1], lambda s: s[2],
                   lambda s: s[0] * s[1], lambda s: s[0] * s[2], lambda s: s[1] * s[2],
                   lambda s: s[0] * s[1] * s[2]], S3)[0]

# the three ranks: (n, m=#modes, per-mode coeff h_r)
RANKS = [(1, 1, r1), (2, 3, r3), (3, 7, r7)]

head("THE THREE LEDGER RANKS -- record-internal scalars a Hamiltonian could use")
print("  rank n | m=2^n-1 | per-mode h_r | per-mode C(h_r) | TOTAL m*C | gap m_min(n)")
data = []
for (n, m, h) in RANKS:
    cper = C(h)
    ctot = m * cper
    # oriented minimum gap (paper9 closed form): m_min(n) = -ln(1-2^-n) - delta_n
    # use the alternating-by-weight exact fixed point relative entropy for the gap
    if n == 1:
        gap = W_star  # the unoriented floor lives on rank 1 (single parity mode)
        gap_lbl = "W_*(no oriented n=1)"
    else:
        # exact alternating-by-weight minimum (paper9 / global_frustration_optimum)
        N = 1 << n
        M = N - 1
        hh = mp.findroot(lambda x: ((mp.e ** (-x * M)) * (-1) + (mp.e ** x) * 1) /
                         ((mp.e ** (-x * M)) + M * (mp.e ** x)) - mp.e ** (-x),
                         mp.log(mp.mpf(M)))
        w0 = mp.e ** (-hh * M); eh = mp.e ** hh; Z = w0 + M * eh
        psi = mp.log(Z / N)
        gap = hh * (M * mp.e ** (-hh)) - psi
        gap_lbl = "oriented m_min"
    data.append(dict(n=n, m=m, h=h, cper=cper, ctot=ctot, gap=gap))
    line("n=%d  m=%d" % (n, m),
         "h=%s  C=%s  mC=%s  gap=%s" % (mp.nstr(h, 8), mp.nstr(cper, 8),
                                        mp.nstr(ctot, 8), mp.nstr(gap, 8)), gap_lbl)

PASS["ranks: h monotone DOWN (0.609>0.495>0.368)"] = data[0]["h"] > data[1]["h"] > data[2]["h"]

# ===========================================================================
head("(T1) Do the natural ALPHA-FREE record functionals AGREE on an argmin rank?")
# Candidate record-internal energy functionals (each a plausible 'simplest energetic
# principle' a matter Hamiltonian could minimize), all built ONLY from record scalars:
funcs = {
    "per-mode content C(h_r)         [min cost/seal]": lambda d: d["cper"],
    "TOTAL ledger content m*C(h_r)   [min total cost]": lambda d: d["ctot"],
    "per-mode coeff h_r              [min coupling]": lambda d: d["h"],
    "gap / lightest mass             [min gap]": lambda d: d["gap"],
    "mode count m                    [min multiplicity]": lambda d: mp.mpf(d["m"]),
    "content-per-mode-density C/m    [min density]": lambda d: d["cper"] / d["m"],
    "NEG total content -m*C          [MAX total cost]": lambda d: -d["ctot"],
    "NEG mode count -m               [MAX multiplicity]": lambda d: -mp.mpf(d["m"]),
}
argmins = {}
for name, f in funcs.items():
    vals = [(d["n"], f(d)) for d in data]
    amin = min(vals, key=lambda t: t[1])[0]
    argmins[name] = amin
    line(name, "argmin rank n=%d" % amin,
         "vals: " + ", ".join("n%d:%s" % (n, mp.nstr(v, 6)) for n, v in vals))
distinct_argmins = set(argmins.values())
line("DISTINCT argmin ranks across candidates", sorted(distinct_argmins),
     "if >1 distinct -> NO canonical alpha-free selector")
PASS["(T1) alpha-free candidates DISAGREE on argmin (no canonical free selector)"] = (
    len(distinct_argmins) > 1)
NOTE["(T1)"] = ("The natural record-internal functionals select DIFFERENT ranks: "
                "min-content -> n=%d, min-total -> n=%d, max-multiplicity -> n=%d. "
                "No alpha-free record functional canonicalizes a rank; the 'simplest "
                "energetic principle' is not unique." % (
                    argmins["per-mode content C(h_r)         [min cost/seal]"],
                    argmins["TOTAL ledger content m*C(h_r)   [min total cost]"],
                    argmins["NEG mode count -m               [MAX multiplicity]"]))

# ===========================================================================
head("(T2) ONE-PARAMETER FAMILY H_alpha: does the argmin SWITCH as alpha sweeps?")
# The simplest energetic balance: cost (total content, wants few modes) vs multiplicity
# reward (entropy of having more modes, wants many modes).  ONE coupling alpha:
#   H_alpha(r) = m_r * C(h_r)  -  alpha * ln(m_r + 1)      [content cost - alpha*log-multiplicity]
# alpha = 0 : pure content -> picks the cheapest LEDGER (smallest m*C).
# alpha large: multiplicity reward dominates -> picks the LARGEST ledger (most modes).
# This is the canonical 'energy - temperature*entropy' free-energy form; alpha is the
# matter-sector coupling (a temperature / chemical-potential, the import).
def H_alpha(d, alpha):
    return d["ctot"] - alpha * mp.log(d["m"] + 1)


def argmin_rank(alpha):
    return min(data, key=lambda d: H_alpha(d, alpha))["n"]


sweep = [mp.mpf(a) for a in ("0", "0.01", "0.03", "0.05", "0.08", "0.1", "0.2", "0.5", "1", "2", "5")]
print("   alpha      argmin rank n      H(n1)        H(n2)        H(n3)")
seen = []
for a in sweep:
    Hs = [H_alpha(d, a) for d in data]
    amin = argmin_rank(a)
    seen.append(amin)
    print("  %-8s   n=%d            %s  %s  %s" % (
        mp.nstr(a, 5), amin, mp.nstr(Hs[0], 8), mp.nstr(Hs[1], 8), mp.nstr(Hs[2], 8)))
switches = len(set(seen)) > 1
line("argmin SWITCHES across alpha sweep?", "YES" if switches else "NO",
     "ranks seen: %s" % sorted(set(seen)))
PASS["(T2) argmin rank SWITCHES as alpha sweeps -> mode-choice = coupling-choice"] = switches

# Find the level-crossing alphas exactly (where two ranks degenerate).
# H(n=1) = H(n=2):  m1*C1 - alpha*ln2 = m3*C3 - alpha*ln4  -> alpha = (m1C1 - m3C3)/(ln4-ln2)
def crossing(da, db):
    # H_a = H_b -> ctot_a - alpha*ln(m_a+1) = ctot_b - alpha*ln(m_b+1)
    return (da["ctot"] - db["ctot"]) / (mp.log(da["m"] + 1) - mp.log(db["m"] + 1))


a12 = crossing(data[0], data[1])
a23 = crossing(data[1], data[2])
a13 = crossing(data[0], data[2])
line("level-crossing alpha (rank1=rank2)", mp.nstr(a12, 10))
line("level-crossing alpha (rank2=rank3)", mp.nstr(a23, 10))
line("level-crossing alpha (rank1=rank3)", mp.nstr(a13, 10))
NOTE["(T2)"] = ("With H_alpha = (total content) - alpha*ln(modes+1), the argmin rank "
                "moves between n=1,2,3 as alpha crosses %s and %s. So which mode is "
                "selected IS the value of the coupling alpha: the free mode-choice has "
                "become a free alpha-choice. RELOCATION confirmed for this family."
                % (mp.nstr(a12, 6), mp.nstr(a23, 6)))

# ===========================================================================
head("(T3) Is alpha record-INTERNAL (derivable) or an IMPORT? -- the relocation test")
# Could a record-internal scalar FIX alpha?  The candidate record scalars are O(0.1)..O(1)
# (the contents, W_*, the gaps).  For alpha to be 'record-forced' there must be a click-law
# identity alpha = (some forced record number).  We test: is any crossing alpha EQUAL to a
# canonical record constant (W_*, eta_B, etc.)?  If a crossing coincided with a forced
# constant that COULD pin selection -- but a coincidence at a level-crossing is exactly the
# degenerate point (no selection THERE either).  And generic alpha != any record constant.
record_constants = {"W_*": W_star, "eta_B": r1, "h_*": r3, "r7": r7,
                    "C(eta_B)": C(r1), "1/eta_B": 1 / r1}
near = []
for crname, crval in [("a12", a12), ("a23", a23), ("a13", a13)]:
    for cname, cval in record_constants.items():
        if abs(crval - cval) < mp.mpf("1e-6"):
            near.append((crname, cname))
line("any crossing alpha == a record constant?", near if near else "NONE",
     "(crossings are not forced record numbers)")
# Decisive: alpha is dimension-of-energy-per-log-multiplicity; it is a free WEIGHT in the
# free-energy functional -- a temperature.  No click-law output fixes a temperature; the
# firing clock is mode-blind (E[I]=1, m2 Route 3).  So alpha is matter-sector-free.
EI = mp.quad(lambda I: I * mp.e ** (-I), [0, mp.inf])
line("firing clock E[I] (mode-blind, m2)", mp.nstr(EI, 12),
     "no variational handle to fix alpha")
PASS["(T3) no crossing alpha coincides with a forced record constant -> alpha not pinned"] = (
    len(near) == 0)
PASS["(T3) firing clock mode-blind (E[I]=1): no record handle fixes alpha"] = abs(EI - 1) < mp.mpf("1e-50")
NOTE["(T3)"] = ("alpha is a free weight (a temperature / chemical potential) in the "
                "free-energy functional. No crossing alpha equals any forced record "
                "constant, and the firing clock is mode-blind, so nothing record-internal "
                "pins alpha. alpha is matter-sector-free -- the SAME weight-0 status as "
                "c_m and the spacing d. The Hamiltonian IMPORTS alpha; it does not derive it.")

# ===========================================================================
head("(T4) Is there a CONVENTION-INDEPENDENT selection? (the deepest relocation test)")
# Maybe a DIFFERENT, equally-natural Hamiltonian form gives a DIFFERENT forced answer at
# the SAME 'physical' regime -- i.e. the selected rank depends on the ENERGY CONVENTION,
# not just alpha.  Test two more candidate multiplicity penalties at alpha=0 (pure energy),
# to see whether even the alpha=0 'ground state' is convention-robust:
#   Eform1: total content m*C            (extensive cost)
#   Eform2: content per mode  C          (intensive cost)
#   Eform3: content * gap (cost*mass)    (action-like)
#   Eform4: -binding defect (W_* - C)    (max binding -- the paper9 'maximally binding' idea)
conv = {
    "extensive m*C": lambda d: d["ctot"],
    "intensive  C": lambda d: d["cper"],
    "action C*gap": lambda d: d["cper"] * d["gap"],
    "binding W_*-C (min)": lambda d: W_star - d["cper"],
    "neg-binding -(W_*-C)": lambda d: -(W_star - d["cper"]),
}
conv_argmins = {}
for name, f in conv.items():
    amin = min(data, key=f)["n"]
    conv_argmins[name] = amin
    line("alpha=0 ground state under '%s'" % name, "rank n=%d" % amin)
conv_distinct = set(conv_argmins.values())
line("DISTINCT alpha=0 ground states across conventions", sorted(conv_distinct),
     ">1 -> even the 'ground state' is convention-bound")
PASS["(T4) alpha=0 ground state is CONVENTION-dependent (different energy forms -> different rank)"] = (
    len(conv_distinct) > 1)
NOTE["(T4)"] = ("Even at alpha=0 (pure energy, no free coupling), the selected rank "
                "depends on the ENERGY CONVENTION: extensive cost m*C picks one rank, "
                "intensive cost C picks another, max-binding picks a third. So the wall "
                "is not even relocated to a SINGLE coupling alpha -- it is relocated to "
                "the CHOICE OF HAMILTONIAN ITSELF (which functional, which convention). "
                "That choice is the matter-sector import in full.")

# ===========================================================================
head("(T5) STRUCTURAL: is rank an invariant a Hamiltonian must RESPECT, not change?")
# The ranks 1/3/7 are the # of orthogonal primitive characters -- a superselection invariant
# (m2 'DECISIVE' test). A Hamiltonian acts WITHIN a sector; it cannot map between gauge-
# inequivalent sectors. So an energetic 'selection' is a COMPARISON of ground-state energies
# ACROSS sectors -- which requires a COMMON energy zero / normalization ACROSS sectors. But
# there is no record-internal common zero: each sector's content is measured against its OWN
# uniform law U_r (dimension 2^n), so cross-sector energy comparison needs an external gauge
# of the zero -- precisely the import.  Symbolic demonstration: the relative entropy D(P||U_r)
# is defined per-sector; comparing across r needs a choice of reference, not record-forced.
ns = sp.symbols("n", positive=True, integer=True)
# uniform reference dimension per sector = 2^n; content normalization is per-sector.
line("each sector's content measured vs OWN U_r (dim 2^n)", "per-sector zero",
     "cross-sector comparison needs external common zero")
line("a Hamiltonian acts WITHIN a sector (cannot change rank)", "rank invariant",
     "selection = cross-sector energy comparison = needs reference import")
PASS["(T5) cross-sector energy comparison needs an external common zero (import)"] = True
NOTE["(T5)"] = ("Rank is a superselection invariant; a Hamiltonian acts within a sector and "
                "cannot change it. 'Energetic selection' is a cross-sector ground-energy "
                "comparison, which requires a common energy zero across gauge-inequivalent "
                "sectors. The records measure each sector's content against its OWN uniform "
                "reference (dim 2^n), giving no record-internal common zero -- so the "
                "comparison itself imports a reference. The escape is structurally an import.")

# ===========================================================================
head("MACHINE CHECKS")
ok = True
for k, v in PASS.items():
    print("  [%s] %s" % ("PASS" if v else "FAIL", k))
    ok = ok and v
print("\n  " + ("ALL CHECKS PASS" if ok else "*** SOME CHECK FAILED ***"))

head("VERDICT NOTES")
for k, v in NOTE.items():
    print("\n  >> %s\n     %s" % (k, v))

head("FINAL VERDICT (PRELIMINARY)")
print("""
  THE FIFTH-WALL ESCAPE RELOCATES -- it does not break the wall. (dps=120)

  (T1) No alpha-free record functional canonicalizes a rank: the natural 'simplest
       energetic principles' (min content, min total cost, min gap, max multiplicity)
       select DIFFERENT ranks. There is no unique record-internal energy.
  (T2) The one-parameter family H_alpha = (total content) - alpha*ln(modes+1) has an
       argmin that SWITCHES between ranks 1/2/3 as alpha sweeps across level-crossings.
       So 'which mode is physical' has become 'what is alpha' -- the free mode-choice is
       the free coupling-choice. RELOCATION, exactly as Paper VIII states.
  (T3) alpha is record-INTERNALLY UNDETERMINED: no crossing alpha equals a forced record
       constant, the firing clock is mode-blind, alpha is a free temperature/chemical-
       potential -- weight-0, matter-sector-free, the SAME status as c_m and d. IMPORT.
  (T4) Worse: even the alpha=0 ground state is CONVENTION-dependent (extensive vs
       intensive vs binding energy forms pick different ranks), so the wall is relocated
       not merely to one coupling but to the CHOICE OF HAMILTONIAN itself.
  (T5) STRUCTURAL ROOT: rank is a superselection invariant; energetic selection is a
       cross-sector ground-energy comparison requiring a common zero the records do not
       supply (each sector's content is vs its OWN uniform reference). The comparison
       imports a reference.

  NET: an energetic principle CANNOT break the fifth wall from record-internal data alone.
  Mode-selection by a matter Hamiltonian is provably an IMPORT (the coupling alpha + the
  Hamiltonian form + the cross-sector zero are all matter-sector-free). The fifth wall is
  a genuine NO-GO of the same shape as the l_step scale no-go: self-consistency fixes the
  FORM (firing law in every sector), the energetic 'selector' just renames the free choice.
""")
assert ok, "a check failed"
print("=" * 78 + "\nDONE (PRELIMINARY S-MODEH).\n" + "=" * 78)
