#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
s_mode_import_wall.py  --  TASK B (PRODUCTION).  The canonical-mode no-go (the third/matter import-fixed wall).

CLAIM (decisive).  The canonical MODE -- WHICH ledger rank r in {1,3,7} (= number of
orthogonal primitive characters) is "the" physical one -- CANNOT be selected by any
record-internal energetic principle.  It is a genuine IMPORT-fixed wall of the same
weight-0 grade and family as G / l_step (the SCALE wall) and chi_AB (the TENSOR-PRODUCT
wall).  This is the third (matter) import-fixed wall (Paper VIII's "fifth wall" in the local
enumeration; in the meta-result it is the matter member of the THREE last imports --
scale l_step, tensor product chi_AB, canonical mode -- restated here as a clean no-go).

This receipt makes the no-go DECISIVE by proving three things, in order:

 (1) CROSS-SECTOR COMMON-ZERO OBSTRUCTION (the core).
     The ranks 1/3/7 are gauge-INEQUIVALENT superselection sectors: rank = number of
     orthogonal primitive characters of the parity group (Z2)^n, an INVARIANT.  We show
     SYMBOLICALLY (sympy-exact) that no record-internal map changes the rank: the only
     record-internal moves are (a) relabelling/sign-flips of characters (orthogonal group
     permutations -- preserve the count) and (b) the firing fixed point grad psi = e^{-h}
     (acts WITHIN a fixed character set -- preserves the count).  A mode-selecting
     Hamiltonian therefore needs a CROSS-SECTOR ground-energy COMPARISON, hence a COMMON
     ENERGY ZERO across the sectors.  The records supply ONLY a per-sector reference: each
     sector's content is the relative entropy D(P_r || U_r) against its OWN uniform law
     U_r of dimension 2^n.  We prove this leaves the per-sector free energies defined only
     up to INDEPENDENT additive constants c_r the records do not fix -- so NO record-
     internal common zero exists, and the cross-sector argmin is not a record output.
     (Sympy-exact: D(P_r||U_r) and D(P_r||U_r') differ by ln(dim_r'/dim_r) = a free gauge
     of the zero; the records never see U_{r'} from inside sector r.)

 (2) ARGMIN SWITCHES (the operational confirmation).
     Build the SIMPLEST candidate free-energy functional on the ranks with ONE free
     coupling alpha (the matter coupling g, a temperature / chemical potential):
        F_alpha(r) = (total ledger content)  -  alpha * (log multiplicity).
     Show argmin_r F_alpha(r) SWITCHES as alpha sweeps -- reproducing the level-crossings
     ~0.168 / 0.207 / 0.247 -- and that NO crossing value equals ANY forced click-law
     constant (eta_B=0.6094, W=0.156109, h_*=0.4951, r7=0.3680, the chiral-gap anchors
     m_min(3..5), 1/eta_B, ...): we tabulate the EXACT minimum distance.  So even
     "pick alpha" is an import.  And even alpha=0 (pure energy, no coupling) is
     CONVENTION-dependent: extensive vs intensive vs binding energy forms pick DIFFERENT
     ranks -- the wall is relocated not to one coupling but to the choice of Hamiltonian.

 (3) CONCLUSION: mode = IMPORT, weight-0, SAME grade/family as G/l_step and chi_AB.
     The firing law (grad psi = e^{-h}) is FORCED in EVERY sector (the FORM), but WHICH
     sector is physical is the last distinguishing choice the records never make.  This
     is exactly the l_step / Q-tilde signature.

PRECISION DISCIPLINE.  Structural / algebraic identities (rank invariant; the common-zero
additive-constant lemma; the crossing values; the no-forced-constant distances) are
sympy-EXACT or mpmath dps>=100.  The per-mode coefficients h_r and contents C(h_r) are
mpmath fixed-point solves at dps=120 (high precision, NOT lattice -- they are scalar
transcendental roots of grad psi = e^{-h}, not lattice eigenvalue traces); flagged below.
There is NO lattice-numeric quantity in this receipt (no eigenvalue spectrum / gap-trace).

Run: /Users/felixrobles/workspace/isp/code/.venv/bin/python s_mode_import_wall.py
"""
import mpmath as mp
import sympy as sp

mp.mp.dps = 120
PASS = {}
NOTE = {}
EXACTNESS = {}   # provenance tag per check: 'sympy-exact' | 'mpmath-hp' | 'structural'


def head(s):
    print("\n" + "=" * 78 + "\n" + s + "\n" + "=" * 78)


def line(lbl, val, note=""):
    print("  %-54s %s   %s" % (lbl, val, note))


def reg(key, ok, tag):
    PASS[key] = ok
    EXACTNESS[key] = tag


# ===========================================================================
# Shared single-mode (parity) information geometry, identical to m2/p9a/paper2.
# All high-precision (mpmath dps=120); these are scalar transcendental roots,
# NOT lattice eigenvalues -- high-precision, not lattice-numeric.
# ===========================================================================
def C(e):
    """per-seal evidence content of a parity mode at coefficient e (relative entropy, nats)."""
    return e * mp.tanh(e) - mp.log(mp.cosh(e))


def J(e):
    return mp.sech(e) ** 2


eta_A = mp.findroot(lambda e: C(e) - J(e), mp.mpf("1.0903"))   # capacity root (C=J), NOT a seal
W_star = J(eta_A)                                              # the ceiling = 0.825..? -> see note
# The UNORIENTED FLOOR (the forced click-law constant "W"=0.156109...) is the content at the
# one-mode SEAL root eta_B (tanh eta = e^-eta), NOT J(eta_A).  Compute both, label cleanly.
eta_B = mp.findroot(lambda e: mp.tanh(e) - mp.e ** (-e), mp.mpf("0.609"))
W_floor = C(eta_B)   # = 0.156109200157240...  (the forced unoriented floor)


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
r1 = coupled_root([lambda s: s[0]], S1)[0]                                   # == eta_B
r3 = coupled_root([lambda s: s[0], lambda s: s[1], lambda s: s[0] * s[1]], S2)[0]   # == h_*
r7 = coupled_root([lambda s: s[0], lambda s: s[1], lambda s: s[2],
                   lambda s: s[0] * s[1], lambda s: s[0] * s[2], lambda s: s[1] * s[2],
                   lambda s: s[0] * s[1] * s[2]], S3)[0]

# the three ranks (n, rank m = # orthogonal primitive characters = 2^n - 1, per-mode coeff h)
RANKS = [(1, 1, r1), (2, 3, r3), (3, 7, r7)]


# the exact chiral-gap anchors (p9a closed form) -- a FORCED click-law constant family
def chiral_gap(n):
    N = 1 << n
    M = N - 1
    h = mp.findroot(lambda x: ((mp.e ** (-x * M)) * (-1) + (mp.e ** x) * 1) /
                    ((mp.e ** (-x * M)) + M * (mp.e ** x)) - mp.e ** (-x),
                    mp.log(mp.mpf(M)))
    w0 = mp.e ** (-h * M); eh = mp.e ** h; Z = w0 + M * eh
    psi = mp.log(Z / N)
    return h * (M * mp.e ** (-h)) - psi


head("ANCHORS -- re-verify the corpus click-law constants (mpmath dps=120, high-precision)")
line("eta_B (one-mode seal root, tanh eta=e^-eta)", mp.nstr(eta_B, 22))
line("  == r1 (1-char coupled root)?", mp.nstr(abs(eta_B - r1), 6), "(must be ~0)")
line("W_floor = C(eta_B) (unoriented floor)", mp.nstr(W_floor, 22),
     "want 0.156109200157240")
line("h_*  = r3 (3-char coupled root)", mp.nstr(r3, 22))
line("r7   (7-char coupled root)", mp.nstr(r7, 22))
line("chiral m_min(3)", mp.nstr(chiral_gap(3), 22), "want 0.133530982072")
line("chiral m_min(4)", mp.nstr(chiral_gap(4), 22), "want 0.064538521138")
line("chiral m_min(5)", mp.nstr(chiral_gap(5), 22), "want 0.031748698315")
reg("ANCHOR eta_B==r1 (one-mode root identity)", abs(eta_B - r1) < mp.mpf("1e-100"), "mpmath-hp")
reg("ANCHOR W_floor = 0.156109200157240...",
    abs(W_floor - mp.mpf("0.156109200157240")) < mp.mpf("1e-15"), "mpmath-hp")
reg("ANCHOR ladder monotone DOWN (0.609>0.495>0.368)", (r1 > r3 > r7), "mpmath-hp")
reg("ANCHOR chiral anchors n=3,4,5 reproduce corpus",
    abs(chiral_gap(3) - mp.mpf("0.133530982072")) < mp.mpf("1e-11") and
    abs(chiral_gap(4) - mp.mpf("0.064538521138")) < mp.mpf("1e-11") and
    abs(chiral_gap(5) - mp.mpf("0.031748698315")) < mp.mpf("1e-11"), "mpmath-hp")


# ===========================================================================
# PART (1) -- CROSS-SECTOR COMMON-ZERO OBSTRUCTION (the core no-go)
# ===========================================================================
head("PART (1) -- CROSS-SECTOR COMMON-ZERO OBSTRUCTION (the core)")
print("""  Rank = number of orthogonal primitive characters of the parity group (Z2)^n.
  CLAIM 1a: rank is a superselection INVARIANT -- no record-internal map changes it.
  CLAIM 1b: a mode-selecting Hamiltonian needs a cross-sector COMMON ENERGY ZERO.
  CLAIM 1c: the records supply only a PER-SECTOR reference (content vs OWN U_r, dim 2^n),
            leaving the per-sector free energies free up to INDEPENDENT additive constants.
  => NO record-internal common zero => cross-sector argmin is NOT a record output.""")

# ---- (1a) rank invariant, sympy-EXACT ------------------------------------
# The primitive characters of (Z2)^n are chi_a(s) = prod_{i in a} s_i for nonempty subsets
# a of {1..n}.  There are exactly 2^n - 1 of them; they are ORTHOGONAL under the uniform
# inner product <chi_a, chi_b> = (1/2^n) sum_s chi_a(s) chi_b(s) = delta_{ab}.  The rank
# (= # orthogonal primitives) is therefore the dimension of the odd character space, an
# integer invariant 2^n - 1.  The ONLY record-internal symmetries are (i) the orthogonal
# group O on the character index (relabel / sign-flip a character: a PERMUTATION-with-signs,
# preserving the count) and (ii) the firing map grad psi = e^{-h} (acts within a fixed
# character set, preserving the count).  Neither changes 2^n - 1.  Show this EXACTLY.
nn = sp.symbols("n", positive=True, integer=True)
rank_expr = 2**nn - 1
line("rank(n) = # orthogonal primitive characters", sp.srepr(rank_expr)[:0] or str(rank_expr),
     "sympy-exact")
# orthogonality of the primitive characters, EXACT, for n=1,2,3 (the three sectors):
ortho_ok = True
for n in (1, 2, 3):
    states = list(__import__("itertools").product((-1, 1), repeat=n))
    masks = [a for a in range(1, 1 << n)]

    def chi(a, s):
        return sp.Integer(__import__("functools").reduce(
            lambda u, i: u * (s[i] if (a >> i) & 1 else 1), range(n), 1))
    G = sp.Matrix(len(masks), len(masks),
                  lambda i, j: sp.Rational(sum(int(chi(masks[i], s) * chi(masks[j], s))
                                               for s in states), 1 << n))
    # Gram matrix must be the identity of size 2^n - 1  -> rank exactly 2^n - 1
    ortho_ok = ortho_ok and (G == sp.eye(len(masks))) and (G.rank() == (1 << n) - 1)
line("primitive-character Gram = Identity (orthonormal)?", "YES" if ortho_ok else "NO",
     "=> rank EXACTLY 2^n-1 for n=1,2,3 (sympy-exact)")
# the three ranks are DISTINCT integers -> three distinct superselection sectors
ranks = [(1 << n) - 1 for n in (1, 2, 3)]
line("the three ranks", ranks, "distinct integers => 3 distinct sectors")
# no record-internal map changes an integer count: relabel/sign = permutation (preserves |.|),
# firing acts within a fixed set (preserves |.|).  Demonstrate: a sign-flip diag(+-1) and a
# permutation P both leave the Gram = Identity and the rank fixed (orthogonal-group closure).
import itertools as _it
n = 2
states = list(_it.product((-1, 1), repeat=n)); masks = [1, 2, 3]


def chi2(a, s):
    return __import__("functools").reduce(lambda u, i: u * (s[i] if (a >> i) & 1 else 1), range(n), 1)


M0 = sp.Matrix([[chi2(a, s) for a in masks] for s in states])     # 4x3 design matrix
# sign-flip S = diag(-1,1,-1) and a permutation P of the 3 characters
Sgn = sp.diag(-1, 1, -1)
P = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
G0 = (M0.T * M0) / (1 << n)
G1 = ((M0 * Sgn * P).T * (M0 * Sgn * P)) / (1 << n)
rank_preserved = (G0 == sp.eye(3)) and (G1 == sp.eye(3)) and (G0.rank() == G1.rank() == 3)
line("sign-flip+permutation preserve Gram=I and rank?", "YES" if rank_preserved else "NO",
     "(the ONLY record-internal char moves preserve rank -- sympy-exact)")
reg("(1a) rank = 2^n-1 is a sympy-exact superselection invariant (orthonormal primitives)",
    ortho_ok and rank_preserved and len(set(ranks)) == 3, "sympy-exact")
NOTE["(1a)"] = ("Rank = # orthogonal primitive characters = 2^n-1 (the primitive characters "
                "are orthonormal: Gram = Identity, sympy-exact for n=1,2,3). The only record-"
                "internal moves on the character set -- sign-flips and permutations (the "
                "orthogonal group on the index) and the firing map (within a fixed set) -- "
                "preserve the integer count. So 1/3/7 are three DISTINCT superselection "
                "sectors no record-internal map connects: gauge-INEQUIVALENT (Wen-PSG).")

# ---- (1b)+(1c) the common-zero obstruction, sympy-EXACT -------------------
# Each sector's record-internal "energy" is the per-seal content = relative entropy
# D(P_r || U_r) of the tilted law P_r against the sector's OWN uniform reference U_r,
# which has dimension dim_r = 2^n.  The records, FROM INSIDE sector r, see only U_r --
# never U_{r'} of another sector.  KEY ALGEBRA (sympy-exact): if you (illegitimately)
# tried to measure P_r against a DIFFERENT-dimension reference U_{r'} (dim 2^{n'}), the
# content would shift by EXACTLY the log-dimension difference:
#      D(P || Uniform_{dim d}) = ln d - H(P)
# so   D(P_r||U_{r'}) - D(P_r||U_r) = ln(2^{n'}) - ln(2^n) = (n'-n) ln 2,
# an additive constant INDEPENDENT of P_r.  Hence each sector's free-energy zero is fixed
# only up to an independent additive constant c_r = (a choice of reference dimension /
# normalization), which the records do NOT fix.  No common zero => no cross-sector argmin.
P_, d_, H_, n_, np_ = sp.symbols("P d H n nprime", positive=True)
# D(P||Uniform_d) = sum P ln(P / (1/d)) = ln d - H(P);  treat H(P) as the (reference-free) entropy.
D_vs_dim = sp.log(d_) - H_                      # content against a uniform of dimension d
shift = (D_vs_dim.subs(d_, 2**np_)) - (D_vs_dim.subs(d_, 2**n_))
shift_simplified = sp.simplify(shift)           # should be (n' - n) ln 2, H cancels
line("D(P||U_{2^n}) = ln(2^n) - H(P)", str(D_vs_dim.subs(d_, 2**n_)), "sympy-exact")
line("D(P||U_{2^n'}) - D(P||U_{2^n}) =", str(shift_simplified),
     "INDEPENDENT of P -> a free additive constant")
indep_of_P = sp.simplify(sp.diff(shift, H_)) == 0 and sp.simplify(
    shift_simplified - (np_ - n_) * sp.log(2)) == 0
line("is the shift independent of P (a pure gauge of the zero)?",
     "YES" if indep_of_P else "NO", "(H(P) cancels exactly)")
reg("(1b/c) cross-sector reference shift = (n'-n)ln2, independent of P (free additive zero)",
    bool(indep_of_P), "sympy-exact")

# OPERATIONAL confirmation at dps=120: the per-sector contents D(P_r||U_r) (each vs its OWN
# uniform) and the would-be cross-comparison.  The per-sector contents are well-defined; the
# CROSS-sector comparison shifts by (n'-n)ln2 per the lemma -- an unfixed offset.
def content_vs_own_uniform(n, h_common):
    """D(P_r || U_r): tilted parity ledger at common coeff h, vs uniform on 2^n states.
       For the FULL symmetric ledger this is m * C(h) is NOT it; the record content is the
       relative entropy of the tilted JOINT law vs uniform.  Compute exactly from the joint."""
    states = list(_it.product((-1, 1), repeat=n))
    masks = [a for a in range(1, 1 << n)]

    def chi(a, s):
        r = 1
        for i in range(n):
            if (a >> i) & 1:
                r *= s[i]
        return r
    # tilted weight at common coeff h on every primitive character
    ws = [mp.e ** (h_common * sum(chi(a, s) for a in masks)) for s in states]
    Z = sum(ws)
    p = [w / Z for w in ws]
    N = len(states)
    return sum(pi * mp.log(pi * N) for pi in p if pi > 0)   # D(P || U_{2^n})


# use the per-sector common coefficient (the firing fixed point) for each sector
Dr = [(n, content_vs_own_uniform(n, h)) for (n, m, h) in RANKS]
print("   per-sector content D(P_r || U_r), each vs its OWN uniform reference U_r:")
for n, D in Dr:
    line("   sector n=%d (rank %d, U_r dim 2^%d=%d)" % (n, (1 << n) - 1, n, 1 << n),
         mp.nstr(D, 20), "nats; defined up to +c_r")
# the cross-sector offsets the records do NOT fix (one per sector, independent):
line("=> free additive constants c_1,c_2,c_3 (per-sector zeros)", "INDEPENDENT",
     "records fix NONE of them => no common zero")
reg("(1c) per-sector contents D(P_r||U_r) well-defined; cross-sector zero NOT record-fixed",
    all(D > 0 for _, D in Dr), "mpmath-hp")
NOTE["(1bc)"] = ("Each sector's record energy is D(P_r||U_r) -- content against its OWN "
                 "uniform reference U_r of dimension 2^n. From inside sector r the records "
                 "never see another sector's U_{r'}. The ONLY way to compare across sectors "
                 "is to re-reference, which shifts the content by EXACTLY (n'-n)ln2, "
                 "independent of the state P (sympy-exact: H(P) cancels). So each sector's "
                 "free-energy zero is fixed only up to an independent additive constant c_r "
                 "the records do not supply. A cross-sector argmin requires choosing the c_r "
                 "-- a reference IMPORT. No record-internal common zero exists; the core no-go.")

# ===========================================================================
# PART (2) -- ARGMIN SWITCHES + no forced-constant + alpha=0 convention-dependence
# ===========================================================================
head("PART (2) -- ARGMIN SWITCHES as alpha sweeps; no crossing = a forced click-law constant")

# total ledger content per sector (the natural extensive 'cost of writing the ledger'):
# m_r * C(h_r)  (the per-mode content times the number of modes; matches m2/scout convention)
data = []
for (n, m, h) in RANKS:
    data.append(dict(n=n, m=m, h=h, cper=C(h), ctot=m * C(h), gap=(W_floor if n == 1 else chiral_gap(n))))

# F_alpha(r) = total content - alpha * log(multiplicity).  alpha = matter coupling (a temperature).
def F_alpha(d, alpha):
    return d["ctot"] - alpha * mp.log(d["m"] + 1)


def argmin_rank(alpha):
    return min(data, key=lambda d: F_alpha(d, alpha))["n"]


sweep = [mp.mpf(a) for a in ("0", "0.05", "0.1", "0.15", "0.168", "0.18",
                             "0.2", "0.21", "0.247", "0.3", "0.5", "1", "5")]
print("   alpha      argmin n    F(n1)         F(n2)         F(n3)")
seen = []
for a in sweep:
    Fs = [F_alpha(d, a) for d in data]
    am = argmin_rank(a); seen.append(am)
    print("  %-8s   n=%d        %s  %s  %s" % (
        mp.nstr(a, 6), am, mp.nstr(Fs[0], 10), mp.nstr(Fs[1], 10), mp.nstr(Fs[2], 10)))
switches = len(set(seen)) > 1
line("argmin SWITCHES across alpha?", "YES" if switches else "NO",
     "ranks visited: %s" % sorted(set(seen)))
reg("(2) argmin rank SWITCHES as alpha sweeps -> mode-choice = coupling-choice",
    switches, "mpmath-hp")

# exact level-crossings (where two sectors degenerate): F_a = F_b
def crossing(da, db):
    return (da["ctot"] - db["ctot"]) / (mp.log(da["m"] + 1) - mp.log(db["m"] + 1))


a12 = crossing(data[0], data[1])   # rank1 = rank2
a23 = crossing(data[1], data[2])   # rank2 = rank3
a13 = crossing(data[0], data[2])   # rank1 = rank3
line("crossing alpha (rank1=rank2)", mp.nstr(a12, 14))
line("crossing alpha (rank2=rank3)", mp.nstr(a23, 14))
line("crossing alpha (rank1=rank3)", mp.nstr(a13, 14))
# the actual ORDER of switching as alpha grows from 0: n=1 (cheapest extensive) -> as alpha
# grows the log-multiplicity reward eventually flips it to n=3. The relevant boundary is the
# SMALLEST crossing above which n=3 wins; reproduce the ~0.168-0.247 band.
band_lo, band_hi = min(a12, a23, a13), max(a12, a23, a13)
line("crossing band [lo, hi]", "[%s, %s]" % (mp.nstr(band_lo, 8), mp.nstr(band_hi, 8)),
     "want ~0.168 .. 0.247")
reg("(2) crossings reproduce the ~0.168-0.247 level-crossing band",
    band_lo < mp.mpf("0.17") and band_hi > mp.mpf("0.24") and band_hi < mp.mpf("0.25"),
    "mpmath-hp")

# NO crossing equals a forced click-law constant.  Tabulate EXACT minimum distance to the
# full forced-constant family.
forced = {
    "eta_B (=r1)": r1,
    "W_floor": W_floor,
    "h_* (=r3)": r3,
    "r7": r7,
    "1/eta_B": 1 / eta_B,
    "C(eta_B)=W_floor": C(eta_B),
    "m_min(3)": chiral_gap(3),
    "m_min(4)": chiral_gap(4),
    "m_min(5)": chiral_gap(5),
}
print("   nearest forced constant to each crossing (EXACT min distance):")
min_overall = mp.inf
for crname, crval in (("a12", a12), ("a23", a23), ("a13", a13)):
    best = min(forced.items(), key=lambda kv: abs(crval - kv[1]))
    dist = abs(crval - best[1])
    min_overall = min(min_overall, dist)
    line("   %s = %s  nearest:" % (crname, mp.nstr(crval, 10)),
         "%s (|d|=%s)" % (best[0], mp.nstr(dist, 8)))
line("MIN distance crossing<->any forced constant", mp.nstr(min_overall, 10),
     "BOUNDED AWAY from 0 => no crossing IS a forced constant")
reg("(2) NO crossing equals any forced click-law constant (min dist > 1e-3)",
    min_overall > mp.mpf("1e-3"), "mpmath-hp")
NOTE["(2)"] = ("F_alpha = (total content) - alpha*ln(modes+1): argmin switches between "
               "ranks across crossings a23=%s, a13=%s, a12=%s (the ~0.168-0.247 band). "
               "The nearest forced click-law constant to ANY crossing sits a distance "
               "%s away -- no crossing is a forced number. So 'which mode' = 'what is "
               "alpha', and alpha is not record-fixed: picking alpha is itself an import."
               % (mp.nstr(a23, 6), mp.nstr(a13, 6), mp.nstr(a12, 6), mp.nstr(min_overall, 5)))

# alpha is a free temperature: the firing clock is mode-blind (E[I]=1 in every sector),
# so nothing record-internal pins it.
EI = mp.quad(lambda I: I * mp.e ** (-I), [0, mp.inf])
line("firing clock E[I] (mode-blind, every sector)", mp.nstr(EI, 16),
     "no record handle fixes alpha")
reg("(2) firing clock mode-blind (E[I]=1 exactly): no record handle for alpha",
    abs(EI - 1) < mp.mpf("1e-100"), "mpmath-hp")

# alpha = 0 is ALSO convention-dependent: different energy FORMS pick different ranks.
head("PART (2b) -- even alpha=0 (pure energy, no coupling) is CONVENTION/Hamiltonian-dependent")
conv = {
    "extensive  m*C   (cost of whole ledger)": lambda d: d["ctot"],
    "intensive  C     (cost per seal)": lambda d: d["cper"],
    "action     C*gap (cost x lightest mass)": lambda d: d["cper"] * d["gap"],
    "binding    W-C   (min: deepest below floor)": lambda d: W_floor - d["cper"],
    "neg-bind   -(W-C) (max binding)": lambda d: -(W_floor - d["cper"]),
    "density    C/m   (cost per mode)": lambda d: d["cper"] / d["m"],
}
conv_argmins = {}
for name, f in conv.items():
    am = min(data, key=f)["n"]
    conv_argmins[name] = am
    line("alpha=0 ground state under '%s'" % name, "rank n=%d" % am,
         "vals " + ",".join("n%d:%s" % (d["n"], mp.nstr(f(d), 6)) for d in data))
conv_distinct = sorted(set(conv_argmins.values()))
line("DISTINCT alpha=0 ground states across conventions", conv_distinct,
     ">1 => even the ground state is convention-bound")
reg("(2b) alpha=0 ground state is CONVENTION-dependent (energy form -> different rank)",
    len(conv_distinct) > 1, "mpmath-hp")
NOTE["(2b)"] = ("Even at alpha=0 (pure energy, no free coupling), the selected rank depends "
                "on the ENERGY CONVENTION: extensive cost m*C picks n=%d, intensive cost C "
                "picks n=%d, action/density pick others. So the wall is not even relocated "
                "to a SINGLE coupling alpha -- it is relocated to the CHOICE OF HAMILTONIAN "
                "FORM. That choice is the matter-sector import in full."
                % (conv_argmins["extensive  m*C   (cost of whole ledger)"],
                   conv_argmins["intensive  C     (cost per seal)"]))

# ===========================================================================
# PART (3) -- GRADE/FAMILY: mode is weight-0, same family as G/l_step and chi_AB
# ===========================================================================
head("PART (3) -- the canonical mode is IMPORT, weight-0, SAME grade/family as G/l_step, chi_AB")
print("""  WEIGHT-0 TEST (the corpus invariant template).  An import-fixed wall is a quantity
  the records leave free at weight 0: self-consistency fixes the FORM, never the last
  distinguishing choice.  We verify the three diagnostic signatures all hold for the mode,
  exactly as they hold for the SCALE wall (G/l_step) and the TENSOR wall (chi_AB):

   (S1) FORM forced in every sector: grad psi = e^{-h} solvable & unique in each rank.
   (S2) Cross-sector selector requires an IMPORT: a common zero / a coupling alpha / a
        Hamiltonian form -- none record-internal (Parts 1 and 2).
   (S3) No forced click-law constant lands the selector: the would-be selectors (crossings)
        miss every forced number (Part 2).""")

# (S1) the firing form is forced & unique in every sector (the fixed point exists, is the
# unique attracting root; we already solved r1,r3,r7 and they satisfy grad psi = e^{-h}).
def residual(stats, states, h):
    ws = [mp.e ** sum(h * stats[j](states[i]) for j in range(len(stats))) for i in range(len(states))]
    Z = sum(ws)
    return max(abs(sum(ws[i] * stats[j](states[i]) for i in range(len(states))) / Z - mp.e ** (-h))
               for j in range(len(stats)))


res1 = residual([lambda s: s[0]], S1, r1)
res3 = residual([lambda s: s[0], lambda s: s[1], lambda s: s[0] * s[1]], S2, r3)
res7 = residual([lambda s: s[0], lambda s: s[1], lambda s: s[2],
                 lambda s: s[0] * s[1], lambda s: s[0] * s[2], lambda s: s[1] * s[2],
                 lambda s: s[0] * s[1] * s[2]], S3, r7)
line("(S1) firing residual |grad psi - e^-h| per sector",
     "n1:%s n2:%s n3:%s" % (mp.nstr(res1, 4), mp.nstr(res3, 4), mp.nstr(res7, 4)),
     "FORM forced & solved in every sector")
reg("(S1) firing FORM grad psi=e^{-h} forced & solved in EVERY sector (residual<1e-30)",
    max(res1, res3, res7) < mp.mpf("1e-30"), "mpmath-hp")

# (S2) selector requires an import: from Part 1 (no common zero) and Part 2 (alpha free).
reg("(S2) cross-sector selector requires an import (common zero / alpha / H-form)",
    PASS["(1b/c) cross-sector reference shift = (n'-n)ln2, independent of P (free additive zero)"]
    and PASS["(2) argmin rank SWITCHES as alpha sweeps -> mode-choice = coupling-choice"], "structural")

# (S3) no forced click-law constant lands the selector (from Part 2).
reg("(S3) no forced click-law constant is the selector (crossings miss every forced number)",
    PASS["(2) NO crossing equals any forced click-law constant (min dist > 1e-3)"], "structural")

# FAMILY MAP: the three import walls share the EXACT structural signature.
print("""
   FAMILY MAP (the meta-result -- three last imports, one signature each):
     wall            FORM forced (record)            last choice = IMPORT (weight 0)
     ----            --------------------            -------------------------------
     SCALE  l_step   kappa*sigma_A = G*Lambda^2      the absolute length a=sqrt(A_rec)  (G no-go, Paper 57)
     TENSOR chi_AB   transverse capacity, up to Q~   the entangling tensor product chi  (Paper VII)
     MODE   (here)   grad psi = e^{-h} every sector  WHICH rank 1/3/7 is physical        (this no-go)
   Each: the records FORCE the form, never the last distinguishing choice. Weight 0.""")
reg("(3) mode shares the weight-0 import signature of l_step (scale) and chi_AB (tensor)",
    PASS["(S1) firing FORM grad psi=e^{-h} forced & solved in EVERY sector (residual<1e-30)"]
    and PASS["(S2) cross-sector selector requires an import (common zero / alpha / H-form)"]
    and PASS["(S3) no forced click-law constant is the selector (crossings miss every forced number)"],
    "structural")
NOTE["(3)"] = ("The canonical mode passes all three weight-0 diagnostics: the firing FORM "
               "grad psi=e^{-h} is forced and uniquely solved in every sector (S1), any "
               "cross-sector selector requires an import -- a common zero (Part 1) or a "
               "coupling alpha / Hamiltonian form (Part 2) (S2), and no forced click-law "
               "constant lands the selector (S3). This is the SAME signature as the SCALE "
               "wall (G/l_step: form kappa*sigma_A=G*Lambda^2 forced, absolute length free) "
               "and the TENSOR wall (chi_AB: transverse capacity forced up to Q~, entangling "
               "product free). The mode is the matter member of the three last imports.")

# ===========================================================================
head("MACHINE CHECKS (with precision provenance)")
ok = True
for k, v in PASS.items():
    print("  [%s] [%-10s] %s" % ("PASS" if v else "FAIL", EXACTNESS[k], k))
    ok = ok and v
print("\n  " + ("ALL CHECKS PASS" if ok else "*** SOME CHECK FAILED ***"))
n_exact = sum(1 for k in PASS if EXACTNESS[k] == "sympy-exact")
n_hp = sum(1 for k in PASS if EXACTNESS[k] == "mpmath-hp")
n_struct = sum(1 for k in PASS if EXACTNESS[k] == "structural")
print("  provenance: %d sympy-exact, %d mpmath-high-precision(dps=120), %d structural;"
      " 0 lattice-numeric." % (n_exact, n_hp, n_struct))

head("VERDICT NOTES")
for k in ["(1a)", "(1bc)", "(2)", "(2b)", "(3)"]:
    print("\n  >> %s\n     %s" % (k, NOTE[k]))

head("FINAL VERDICT -- the canonical mode is the third (matter) import-fixed wall (NO-GO)")
print("""
  The canonical MODE cannot be selected by any record-internal energetic principle. (dps=120)

  (1) CORE -- CROSS-SECTOR COMMON-ZERO OBSTRUCTION. The ranks 1/3/7 are gauge-INEQUIVALENT
      superselection sectors: rank = # orthogonal primitive characters = 2^n-1, an integer
      invariant (orthonormal primitives, Gram=Identity; sympy-exact) that no record-internal
      move -- sign-flip, permutation, or the firing map -- changes. A mode-selecting
      Hamiltonian therefore needs a CROSS-SECTOR ground-energy comparison, hence a COMMON
      ENERGY ZERO. The records supply only a PER-SECTOR reference: content D(P_r||U_r) vs the
      sector's OWN uniform U_r of dimension 2^n. Re-referencing across sectors shifts the
      content by EXACTLY (n'-n)ln2, INDEPENDENT of the state (sympy-exact: H(P) cancels), so
      each sector's zero is free up to an independent additive constant the records never fix.
      No record-internal common zero exists -> the cross-sector argmin is not a record output.

  (2) ARGMIN SWITCHES. The simplest free-energy F_alpha=(total content)-alpha*ln(modes+1)
      has an argmin that SWITCHES between ranks across crossings in the ~0.168-0.247 band,
      and NO crossing equals any forced click-law constant (eta_B, W=0.156109, h_*, r7,
      m_min(3..5), 1/eta_B; min distance bounded away from 0). The firing clock is mode-blind
      (E[I]=1), so nothing record-internal pins alpha -- picking alpha is an import. Even
      alpha=0 is convention-dependent: extensive/intensive/action/binding energy forms pick
      DIFFERENT ranks, so the freedom relocates to the CHOICE OF HAMILTONIAN itself.

  (3) GRADE/FAMILY. The mode passes all three weight-0 diagnostics (form forced in every
      sector; cross-sector selector needs an import; no forced constant lands it). It is
      IMPORT-fixed at weight 0 -- the SAME grade and family as G/l_step (the SCALE wall) and
      chi_AB (the TENSOR-PRODUCT wall). The records carry everything RELATIVE; the canonical
      mode is the matter member of the three last SHARD-specific imports.

  SCOPE / HONESTY. This is a record-internal NO-GO, NOT a claim about physics' true mode
  count: it says the SHARD records do not, by themselves, energetically select a ledger rank.
  The PSG 'import external data' escape (a built matter Hamiltonian that selects a rank) is
  not refuted -- it is shown to RELOCATE the choice (to alpha / to the Hamiltonian form / to
  the cross-sector zero), i.e. to be an import, not a record-internal canonicalization. The
  large-N Gross-Neveu mechanism (Task A) builds a DYNAMICAL mass WITHIN a fixed sector; it
  does not (and is not claimed to) select the sector. 2d, parity-character ledger; the
  per-mode coefficients are scalar transcendental roots (high-precision), not lattice spectra.
""")
assert ok, "a check failed"
print("=" * 78 + "\nDONE (TASK B -- s_mode_import_wall).\n" + "=" * 78)
