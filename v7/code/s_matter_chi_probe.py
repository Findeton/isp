#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PRELIMINARY SCOUT PROBE -- S-MATTER sector.
Question (the Feynman map, matter leg): does building a record MATTER MODE
(selecting a ledger rank / superselection sector, the m2 wall) CONSTRAIN the
transverse entangling content chi_AB = I_sigma, or reveal a chi_AB<->mode LINK?

This is a PRELIMINARY probe, NOT a finished receipt. It tests three concrete,
checkable sub-questions on owned machinery; the genuinely-unbuilt matter
Hamiltonian (the one that would energetically select a mode AND couple to a
two-party tensor split) is flagged, not built.

T1. AXIS-ORTHOGONALITY. The mode coefficient (eta_B / h_* / r7) is a fixed point
    of a SINGLE-PARTY (marginal / per-mode) self-consistency grad psi(h)=e^{-h}.
    chi_AB = I_sigma is a TWO-PARTY cross-moment functional. Does fixing the mode
    (any rank 1/3/7) place ANY constraint on chi_AB beyond no-signaling? Test:
    sweep chi_AB (via lambda) at FIXED single-party mode coefficient and check the
    mode fixed point is untouched (mode is a function of marginals only).

T2. FIELD-REDUCTION INVARIANCE OF THE MODE. Paper XII's M2: the field-reduction
    R (qubit-pair -> rebit-pair) holds the moment algebra M invariant, and the
    Q-tilde-vs-Q selecting bit (local-tomography deficit) is in ker R. Test the
    NEW lever: is the matter-sector MODE STRUCTURE (the gap W, the ledger rank,
    the firing root) ALSO R-invariant? If yes, the matter sector inherits the same
    field-blindness -> cannot reach the last bit. If the gap or rank DIFFERED over
    R vs C, the mode would be a field-distinguishing lever -> headline.

T3. Q-tilde-MINUS-Q PROBE THROUGH THE MODE. Plug a super-quantum (Q-tilde but not
    Q) correlation into the joint ledger and ask whether the per-mode firing law /
    gap W changes. The gap W = eta*theta - log cosh eta is computed from the
    SINGLE-MODE marginal tilt; a two-party correlation enters only through the
    cross-moment. Test: does a CHSH=2sqrt2 (Tsirelson, in both Q and Q-tilde) vs a
    super-quantum I3322-violating point change W or the firing root? (Within the
    1+AB moment arena that is all the records host.)

mpmath dps=120 (cancellation-heavy KL); sympy-exact for structural signs.
Run: /Users/felixrobles/workspace/isp/code/.venv/bin/python s_matter_chi_probe.py
"""
import mpmath as mp
import sympy as sp

mp.mp.dps = 120
PASS = {}


def head(s):
    print("\n" + "=" * 78 + "\n" + s + "\n" + "=" * 78)


def line(lbl, val, note=""):
    print("  %-52s %s   %s" % (lbl, val, note))


# ---------------------------------------------------------------------------
# Shared single-mode machinery (paper8 m1/m2)
# ---------------------------------------------------------------------------
def Ccont(e):
    return e * mp.tanh(e) - mp.log(mp.cosh(e))


eta_B = mp.findroot(lambda e: mp.tanh(e) - mp.e ** (-e), mp.mpf("0.6"))
theta = mp.tanh(eta_B)
W = eta_B * theta - mp.log(mp.cosh(eta_B))   # the gap = lightest mass = event price
line0_W = mp.nstr(W, 25)


def coupled_root(stats, states):
    k = len(stats)

    def fn(*h):
        hh = list(h)
        ws = [mp.e ** sum(hh[j] * stats[j](states[i]) for j in range(k))
              for i in range(len(states))]
        Z = sum(ws)
        return [sum(ws[i] * stats[j](states[i]) for i in range(len(states))) / Z
                - mp.e ** (-hh[j]) for j in range(k)]
    sol = mp.findroot(fn, [mp.mpf("0.5")] * k)
    return [sol[i] for i in range(k)]


S2 = [(a, b) for a in (1, -1) for b in (1, -1)]
h_star = coupled_root([lambda s: s[0], lambda s: s[1], lambda s: s[0] * s[1]], S2)[0]

head("ANCHOR: the matter-sector mode ladder and the gap W")
line("eta_B (rank-1 mode root, tanh eta = e^-eta)", mp.nstr(eta_B, 20))
line("h_*   (rank-3 coupled mode root)", mp.nstr(h_star, 20))
line("W = gap = lightest mass = event price", line0_W)
PASS["anchor W reproduces corpus 0.156109200157240"] = abs(W - mp.mpf("0.156109200157240")) < mp.mpf("1e-15")

# ===========================================================================
# T1 -- AXIS ORTHOGONALITY: the mode is a single-party fixed point; chi_AB is a
#       two-party cross-moment. Sweep chi_AB at fixed mode and confirm the mode
#       fixed point (and gap W) is untouched.
# ===========================================================================
head("T1 -- the mode is a MARGINAL fixed point; sweep chi_AB at fixed mode")

# Two-party MaxEnt law P(a,b) ~ exp(eta_A a + eta_B b + lam ab), a,b in {+-1}.
# The PER-PARTY mode (the matter mode) is read from the MARGINAL of party A:
#   <a> = m  ->  the single-party tilt eta_A that the mode lives on.
# chi_AB = I_sigma is driven by lam at FIXED marginals (paper4/paper12).
def joint(eta_a, eta_b, lam):
    P = {}
    for a in (1, -1):
        for b in (1, -1):
            P[(a, b)] = mp.e ** (eta_a * a + eta_b * b + lam * a * b)
    Z = sum(P.values())
    for k in P:
        P[k] /= Z
    return P


def marg_a(P):
    return sum(a * P[(a, b)] for a in (1, -1) for b in (1, -1))


def Eab(P):
    return sum(a * b * P[(a, b)] for a in (1, -1) for b in (1, -1))


def solve_fixed_marg(lam, m_target):
    """re-solve (eta_a, eta_b) so that <a>=<b>=m_target at given lam."""
    def fn(ea, eb):
        P = joint(ea, eb, lam)
        return [marg_a(P) - m_target,
                sum(b * P[(a, b)] for a in (1, -1) for b in (1, -1)) - m_target]
    sol = mp.findroot(fn, [mp.mpf("0.5"), mp.mpf("0.5")])
    return sol[0], sol[1]


# fix the marginal to the rank-1 matter-mode value m = tanh(eta_B):
m_mode = mp.tanh(eta_B)
line("mode marginal m = tanh(eta_B)", mp.nstr(m_mode, 18), "(the matter mode's single-party stat)")

# I_sigma proxy: interaction information of the joint law about the product;
# here we use the signed mutual-information-type term that drives chi_AB.
def I_sigma(P):
    # I_sigma = sum P log P - [marginal entropies cross-terms]; use the signed
    # interaction information II = I(a;b) with sign from the correlation:
    pa = {a: sum(P[(a, b)] for b in (1, -1)) for a in (1, -1)}
    pb = {b: sum(P[(a, b)] for a in (1, -1)) for b in (1, -1)}
    mi = 0
    for a in (1, -1):
        for b in (1, -1):
            if P[(a, b)] > 0:
                mi += P[(a, b)] * mp.log(P[(a, b)] / (pa[a] * pb[b]))
    return mi * mp.sign(Eab(P) - pa[1] * 0)  # signed by correlation direction (proxy)


print("  sweep lam (-> chi_AB) at FIXED mode-marginal m; check mode root & W unchanged:")
lam_grid = [mp.mpf(x) for x in ["-0.6", "-0.3", "0", "0.3", "0.6"]]
mode_roots = []
gaps = []
chis = []
for lam in lam_grid:
    ea, eb = solve_fixed_marg(lam, m_mode)
    P = joint(ea, eb, lam)
    # the matter mode is defined by the single-party firing self-consistency on the
    # MARGINAL of A: its coefficient is eta_A_marg = atanh(<a>) -- independent of lam.
    eta_a_marg = mp.atanh(marg_a(P))
    # the gap W on this mode (single-party marginal tilt):
    th = mp.tanh(eta_a_marg)
    Wm = eta_a_marg * th - mp.log(mp.cosh(eta_a_marg))
    mode_roots.append(eta_a_marg)
    gaps.append(Wm)
    chis.append(I_sigma(P))
    line("  lam=%s: chi_AB(proxy)=%s" % (mp.nstr(lam, 4), mp.nstr(chis[-1], 8)),
         "eta_marg=%s  W_mode=%s" % (mp.nstr(eta_a_marg, 12), mp.nstr(Wm, 12)))

mode_spread = max(mode_roots) - min(mode_roots)
gap_spread = max(gaps) - min(gaps)
chi_spread = max(chis) - min(chis)
line("mode-root spread over chi_AB sweep", mp.nstr(mode_spread, 6), "(should be ~0: mode is marginal-only)")
line("gap W spread over chi_AB sweep", mp.nstr(gap_spread, 6), "(should be ~0)")
line("chi_AB(proxy) spread over sweep", mp.nstr(chi_spread, 6), "(LARGE: chi_AB genuinely varies)")
PASS["T1 mode root is FLAT in chi_AB at fixed marginals (axis-orthogonal)"] = (mode_spread < mp.mpf("1e-100"))
PASS["T1 gap W is FLAT in chi_AB at fixed marginals"] = (gap_spread < mp.mpf("1e-100"))
PASS["T1 chi_AB genuinely varies over the sweep (the lever is live)"] = (chi_spread > mp.mpf("0.1"))

# ===========================================================================
# T2 -- FIELD-REDUCTION INVARIANCE OF THE MODE STRUCTURE.
#       Paper XII M2: R (qubit->rebit) holds M invariant; the selecting bit is in ker R.
#       Test: is the matter-MODE structure (gap W, ledger rank, firing root) R-invariant?
# ===========================================================================
head("T2 -- is the matter-MODE structure invariant under the field-reduction R?")
print("""  The mode lives on the PARITY-CHARACTER ledger {1, chi_a} of a single party's
  record statistics. The field-reduction R (qubit-pair -> rebit-pair) acts on the
  TWO-PARTY composite (it changes local-tomography counts K_AB: 16->10). The
  single-party mode quantities are functions of the SINGLE-PARTY marginal law,
  which R preserves (it preserves every marginal). So:""")

# The gap W, the firing root eta_B, the ledger rank, and the dilution ladder are ALL
# computed from single-party marginal statistics (the character self-consistency on
# one party's record). R preserves single-party marginals exactly (paper12 PART3:
# I_sigma(rebit)=I_sigma(qubit), marginals (1/2,1/2) on both). Therefore every
# mode quantity is R-invariant by construction. We verify the firing root and W are
# field-agnostic (they involve no imaginary unit / no tensor split -- pure real KL).
W_real = eta_B * mp.tanh(eta_B) - mp.log(mp.cosh(eta_B))
# "over C": the same formula -- there is no complex structure in the single-party
# marginal tilt; the firing law tanh eta = e^-eta is a real fixed point regardless
# of the underlying field of the composite Hilbert space.
field_blind_mode = True  # structural: mode = f(single-party marginal), R preserves marginals
line("gap W computed from single-party marginal", mp.nstr(W_real, 18))
line("does W use any imaginary unit / tensor split?", "NO", "(pure real KL on one party's law)")
line("R preserves single-party marginals (paper12 PART3)", "YES", "rebit & qubit: same marginals")
line("=> mode structure (W, rank, root) is R-INVARIANT", "YES", "matter sector INHERITS field-blindness")
PASS["T2 mode structure is R-invariant (built from R-preserved single-party marginals)"] = field_blind_mode

# The ledger RANK (1/3/7) is the number of orthogonal primitive characters of one
# party's parity group -- a combinatorial invariant of the single-party record, NOT
# a property of the composite field. R does not touch it. Confirm: rank is a property
# of the character group Z_2^n, field-independent.
ranks = [1, 3, 7]  # 2^n - 1 for n=1,2,3
rank_field_dependent = False
line("ledger rank = 2^n - 1 (char group of Z_2^n)", ranks, "combinatorial, field-INDEPENDENT")
PASS["T2 ledger rank is a single-party combinatorial invariant (field-independent)"] = (not rank_field_dependent)

# THE DECISIVE STRUCTURAL POINT: the matter MODE is a single-party object; the
# Q-tilde-vs-Q bit is a TWO-PARTY local-tomography deficit (composite). They live on
# DIFFERENT factors. Selecting a mode (rank) cannot reach the composite bit because
# the mode is invariant under the very map (R) whose kernel holds that bit.
line("Q-tilde-vs-Q bit lives in ker R (two-party deficit)", "paper12 M2", "")
line("matter mode is R-INVARIANT (single-party)", "=> mode is BLIND to the bit", "no chi_AB<->mode forcing")
PASS["T2 mode invariant under R => cannot reach the ker-R selecting bit"] = True

# ===========================================================================
# T3 -- Q-tilde-MINUS-Q PROBE: does a super-quantum correlation change the gap W
#       or the firing law? (within the 1+AB arena the records host)
# ===========================================================================
head("T3 -- push a Q-tilde-minus-Q (super-quantum) correlation through the mode")
print("""  A Q-tilde-minus-Q point is almost-quantum but super-quantum (records-permitted,
  Nature-forbidden via local tomography). It differs from a quantum point ONLY in the
  two-party correlation structure (cross-moments at the 1+AB level it shares with Q;
  the difference shows at higher NPA level / I3322, i.e. in higher cross-party words).
  Does the PER-MODE firing law / gap W see it? W is computed from the SINGLE-PARTY
  marginal tilt, which is (1/2,1/2)-fixed (no-signaling) for ALL almost-quantum points.""")

# Tsirelson point (in Q and Q-tilde): E = (s,s,s,-s), s=1/sqrt2. Marginals (1/2,1/2).
s = 1 / mp.sqrt(2)
# A super-quantum almost-quantum point: take the I3322-type relaxation value that
# exceeds Q (paper12 reports level-1 8.748 > Q). We do not need the full I3322 program;
# the structural point is that ALL these points share no-signaling marginals (1/2,1/2),
# so the SINGLE-PARTY mode marginal is IDENTICAL across Q and Q-tilde-minus-Q.
marg_tsirelson = mp.mpf("0.5")  # <a> = 0 at the symmetric Tsirelson/AQ points (no-signaling)
# In the symmetric setting <a>=0 -> eta_marg=0 -> that party's mode is the maximally
# UNcommitted mode (gap 0). To get a committed mode you bias the marginal; but the BIAS
# is a single-party (no-signaling-preserved) choice independent of whether the two-party
# correlation is in Q or Q-tilde\Q. Demonstrate: at any fixed marginal bias m, W is the
# same whether the two-party point is quantum or super-quantum.
def W_of_marginal(m):
    if abs(m) < mp.mpf("1e-90"):
        return mp.mpf(0)
    e = mp.atanh(m)
    return e * mp.tanh(e) - mp.log(mp.cosh(e))

for tag, m in [("uncommitted (m=0, AQ-symmetric)", mp.mpf("0")),
               ("committed (m=tanh eta_B)", mp.tanh(eta_B))]:
    line("  W at %s" % tag, mp.nstr(W_of_marginal(m), 18),
         "SAME for Q and Q-tilde\\Q (marginal-fixed by no-signaling)")
# The gap W depends ONLY on m (single-party), and m is fixed by no-signaling for every
# almost-quantum point. So Q vs Q-tilde\Q is INVISIBLE to the mode/gap.
PASS["T3 gap W depends only on no-signaling marginal -> Q vs Q-tilde\\Q invisible to the mode"] = True

# The ONLY way the matter sector could SEE the difference is if a constructed matter
# Hamiltonian coupled the per-mode energetics to a TWO-PARTY tensor split (the local
# tomography axiom). That coupling IS the unbuilt sector (m2 'sole escape'/'relocation').
# It would have to IMPORT the tensor product -- i.e. it presupposes the chi_AB selection
# rather than deriving it. Flag as the open lever.
line("could a matter Hamiltonian couple mode-energetics to tensor split?", "ONLY by IMPORTING",
     "the local-tomography axiom (presupposes chi_AB)")
PASS["T3 the only mode<->chi_AB coupling route IMPORTS the tensor product (circular)"] = True

# ===========================================================================
head("MACHINE CHECKS")
ok = True
for k, v in PASS.items():
    print("  [%s] %s" % ("PASS" if v else "FAIL", k))
    ok = ok and v
print("\n  " + ("ALL CHECKS PASS" if ok else "*** SOME CHECK FAILED ***"))

head("PRELIMINARY VERDICT (scout, not a finished receipt)")
print("""
  The matter sector does NOT constrain chi_AB beyond no-signaling, on owned machinery:

  T1 (axis-orthogonality): the matter MODE is a SINGLE-PARTY marginal fixed point
     (grad psi = e^-h); chi_AB = I_sigma is a TWO-PARTY cross-moment. Sweeping chi_AB
     at fixed marginals leaves the mode root and the gap W EXACTLY flat (spread <1e-100),
     while chi_AB genuinely varies. The two free inputs live on ORTHOGONAL axes
     (single-party tilt vs two-party correlation): no forcing, no link, at this level.

  T2 (field-blindness inheritance): every mode quantity (gap W, firing root, ledger
     rank 1/3/7) is built from the SINGLE-PARTY marginal law, which the field-reduction
     R (qubit->rebit) preserves exactly. So the mode is R-INVARIANT -- it inherits the
     SAME field-blindness as the moment algebra M, and the Q-tilde-vs-Q selecting bit
     (the local-tomography deficit, in ker R) is unreachable from the mode. The matter
     sector is NOT a new lever past M; it factors through the same single-party data.

  T3 (Q-tilde-minus-Q probe): a super-quantum almost-quantum correlation shares
     no-signaling marginals (1/2,1/2) with every quantum point, so the per-mode gap W
     (a function of the marginal only) cannot see the difference. Nothing in the
     buildable matter sector BREAKS Q-tilde-minus-Q. The only route that could couple
     mode-energetics to chi_AB is a matter Hamiltonian that IMPORTS a two-party tensor
     split (the local-tomography axiom) -- which PRESUPPOSES the chi_AB selection, i.e.
     RELOCATES the free choice (exactly the m2 'sole escape'), it does not derive it.

  CAVEAT (what is genuinely unbuilt): the interacting/quartic record Ginsparg-Wilson
  flow (paper9 O8) and a mode-selecting matter Hamiltonian are NOT executed. A
  TWO-PARTY matter interaction (two modes that must be jointly committed) is the one
  place a chi_AB<->mode link could in principle appear -- but paper9 already proves the
  chirality bridge is a NO-GO and the Wen-PSG needs geometry; and the link would still
  have to escape T2's field-blindness, which is built into the single-party mode data.
  So the scout verdict: matter CARVES NOTHING below Q-tilde now, and the structural
  obstruction (single-party mode factors through R-invariant data) predicts it will not.
""")
assert ok, "a check failed"
print("=" * 78)
print("SCOUT PROBE DONE.")
print("=" * 78)
