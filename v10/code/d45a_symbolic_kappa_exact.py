#!/usr/bin/env python3
"""
d45a_symbolic_kappa_exact.py — v10 D45a: the symbolic-m closure of
kappa. Pin: note-d45a-symbolic-m-kappa-closure.md (strict). Parents:
D44d TERMINAL #353 (the quartic kappa(m) = (9m^4 - 15m^2 + 4)/144
verified with zero tolerance on the 28-point hull [1/16, 2]; the hull
caveat is this unit's target); the d43a/d44d exact-series machinery
(v10/code/d44d_slab_kappa_exact.py, ported STRUCTURALLY below with the
mass as a FORMAL VARIABLE).

What this receipt does: re-runs the committed SINGLETON identification
(ORD 4, L = 12, both rules EXC and LT) with m symbolic — every matrix
entry is a PAIR of polynomials in m (real, imaginary) with exact
Fraction coefficients; the Delta-series is a list of such pairs. The
tau/D first-moment identification then yields D as a matrix of
polynomials in m, and the LT collapse constant kappa(m) is DERIVED as
an exact polynomial identity valid for ALL m — upgrading D44d's
[EXACT on the hull] to [THEOREM at fixture scale, all m] — together
with the structural origin of the factorization (3m^2 - 1)(3m^2 - 4).

Gates (pre-registered in the pin): YG0 regression — the derived
polynomials evaluated at committed grid masses reproduce the committed
KTAB rationals exactly (polynomial evaluation is a ring homomorphism
Q[m] -> Q, so evaluating the derived symbolic objects at m IS running
the pipeline at that mass); YG1 the derivation — the symbolic tau
tables and the collapse EXC D = 1*(I - sigma_x) and LT D = kappa(m)*
(I - sigma_x) with kappa(m) - (9m^4 - 15m^2 + 4)/144 == the ZERO
polynomial; YG2 the ray identity in m — off-ray components, imaginary
parts, sub-onset orders, delta-odd defects, and completeness-slot
commutators all vanish AS POLYNOMIALS; YG3 structural origin — each
tau channel polynomial, the delta-weighted combination, and the exact
factorization over Q; YG4 purity — ZERO floats (no mpmath anywhere;
pure Fraction polynomial arithmetic; a runtime type walk over every
retained coefficient) and byte-identical determinism.

DIVISION AUDIT (the pin's failure-mode check, verified in the port):
the only divisions in the entire pipeline are by INTEGER constants —
the 1/2 hopping normalization and the 1/k! exponential factorials
enter as exact Fraction constants; the Neumann inversion of
Gamma(U_free) starts at the identity and divides by nothing. The
polynomial layer below defines NO division of polynomials at all, so
any m-dependent division attempted by a pipeline stage would raise
TypeError; none does. Every stage is division-free in m and every
entry stays a polynomial in m over Q.

Port deviations (declared; all mathematically inert): (1) mpc entries
become (real, imag) polynomial pairs — i^2 = -1 bookkeeping in the
pair multiply; (2) exact-zero entries/series are dropped where the
committed numeric code kept dust below 1e-45/1e-30 — here zero means
IDENTICALLY zero, so dropping cannot change any coefficient; (3)
scope is the committed SINGLETON path (tau over separations r = 1..4,
the tau_D_sg0/kappa_pipeline convention) at the single phase ORD 4 /
L 12 — the slab arms are m-pointwise-verified at #353 and inherit by
the A5 weight-independence note (pin section 4: re-running them
symbolically is OPTIONAL and here declared NOT re-run); (4) there is
no tolerance anywhere — every gate is exact equality of polynomials.

Committed regression sources (read-only): KTAB grid values from
v10/data/d44d_slab_kappa_exact.out (KG2 table); the LT signed channel
values REF_LT from v10/code/d44d_slab_kappa_exact.py (T5 anchors).

Deterministic: no RNG, no wall clock, no environment reads; all
printed iterations sorted; rerun byte-identical under any
PYTHONHASHSEED. Exit 1 on any gate failure.
"""
import sys
import math
from fractions import Fraction as Fr

ORD = 4
L = 12
DIM = 2 * L
SX = [[0, 1], [1, 0]]

PASS = FAIL = 0
def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    PASS, FAIL = PASS + int(bool(ok)), FAIL + int(not ok)
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

def idx(n, s): return 2 * (n % L) + s

# ---- exact polynomial layer: dense tuples of Fraction in m -----------------
# canonical form: trimmed tuple (no trailing zeros); the zero polynomial is
# the empty tuple. NO polynomial division is defined anywhere in this layer.
def p_trim(t):
    n = len(t)
    while n and t[n - 1] == 0:
        n -= 1
    return tuple(t[:n])

def p_add(a, b):
    if not a: return b
    if not b: return a
    n = max(len(a), len(b))
    out = [Fr(0)] * n
    for i, x in enumerate(a): out[i] += x
    for i, x in enumerate(b): out[i] += x
    return p_trim(out)

def p_neg(a): return tuple(-x for x in a)
def p_sub(a, b): return p_add(a, p_neg(b))

def p_mul(a, b):
    if not a or not b: return ()
    out = [Fr(0)] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        if ai == 0: continue
        for j, bj in enumerate(b):
            if bj != 0: out[i + j] += ai * bj
    return p_trim(out)

def p_scale(a, c):
    if not a or c == 0: return ()
    return tuple(x * c for x in a)

def p_eval(a, mv):
    acc = Fr(0)
    for c in reversed(a): acc = acc * mv + c
    return acc

def p_str(a):
    if not a: return "0"
    return " + ".join(f"({c})*m^{k}" for k, c in enumerate(a) if c != 0)

# ---- poly-complex layer: entries are PAIRS (re, im) of m-polynomials -------
PCZ = ((), ())
PC_ONE = ((Fr(1),), ())
def pc_is0(z): return not z[0] and not z[1]
def pc_add(z, w): return (p_add(z[0], w[0]), p_add(z[1], w[1]))
def pc_neg(z): return (p_neg(z[0]), p_neg(z[1]))
def pc_sub(z, w): return (p_sub(z[0], w[0]), p_sub(z[1], w[1]))
def pc_mul(z, w):
    a, b = z
    c, d = w
    return (p_sub(p_mul(a, c), p_mul(b, d)),
            p_add(p_mul(a, d), p_mul(b, c)))
def pc_conj(z): return (z[0], p_neg(z[1]))
def pc_cscale(z, cre, cim):
    a, b = z
    return (p_sub(p_scale(a, cre), p_scale(b, cim)),
            p_add(p_scale(b, cre), p_scale(a, cim)))
def pc_iscale(z, k):
    kf = Fr(k)
    return (p_scale(z[0], kf), p_scale(z[1], kf))
def pc_str(z):
    if pc_is0(z): return "0"
    if not z[1]: return p_str(z[0])
    if not z[0]: return "i*[" + p_str(z[1]) + "]"
    return p_str(z[0]) + " + i*[" + p_str(z[1]) + "]"

# ---- series scalars: lists of ORD+1 poly-complex coefficients --------------
# (the d44d s_zero/s_const/s_add/s_mul/s_conj, entries now symbolic in m)
def s_zero(): return [PCZ] * (ORD + 1)
def s_one():
    v = s_zero(); v[0] = PC_ONE; return v
def s_is0(s): return all(pc_is0(x) for x in s)
def s_add(a, b): return [pc_add(a[k], b[k]) for k in range(ORD + 1)]
def s_mul(a, b):
    out = s_zero()
    for i in range(ORD + 1):
        ai = a[i]
        if pc_is0(ai): continue
        for j in range(ORD + 1 - i):
            bj = b[j]
            if pc_is0(bj): continue
            out[i + j] = pc_add(out[i + j], pc_mul(ai, bj))
    return out
def s_conj(a): return [pc_conj(x) for x in a]

# ---- series matrices (the d44d m_mul/m_add/m_identity/m_neumann_inv) -------
def m_mul_sym(A, B):
    cols = {}
    for (i, j), s in B.items():
        cols.setdefault(i, []).append((j, s))
    out = {}
    for (i, k), a in A.items():
        for (j, s) in cols.get(k, []):
            prod = s_mul(a, s)
            if s_is0(prod): continue
            key = (i, j)
            if key in out: out[key] = s_add(out[key], prod)
            else: out[key] = prod
    return {k: v for k, v in out.items() if not s_is0(v)}

def m_add_sym(A, B):
    out = dict(A)
    for k, s in B.items():
        out[k] = s_add(out[k], s) if k in out else s
    return out

def m_identity_sym():
    return {(i, i): s_one() for i in range(DIM)}

def m_neumann_inv_sym(M):
    """Inverse of M = I + N with N constant-free: sum (-N)^j. Division-free:
    starts at the identity; only pc products and sums below."""
    N = {}
    for (i, j), s in M.items():
        t = list(s)
        if i == j:
            t[0] = pc_sub(t[0], PC_ONE)
        if any(not pc_is0(x) for x in t):
            N[(i, j)] = t
    # port-verification (the pin's division-free check): N must be
    # constant-free in Delta, or the Neumann series would not invert M
    assert all(pc_is0(t[0]) for t in N.values()), \
        "Neumann precondition violated: N has a Delta^0 term"
    out = m_identity_sym()
    term = m_identity_sym()
    minusN = {k: [pc_neg(x) for x in v] for k, v in N.items()}
    for _ in range(ORD // 2 + 1):
        term = m_mul_sym(term, minusN)
        if not term: break
        out = m_add_sym(out, term)
    return out

# ---- symbolic Hamiltonian builders (the d44d build_H / build_H_R) ----------
# The mass enters ONLY as m * wm on the diagonal (the committed addH lines);
# hopping is m-free at -i/2 / +i/2. Symbolically: diagonal entries are the
# degree-1 real polynomials +-wm*m; hopping entries are pure-imaginary
# constants -+wb/2.
def _pc_mass(w):        # the pair for w*m  (real poly 0 + w*m, imag 0)
    return (p_trim([Fr(0), Fr(w)]), ())
def _pc_hop(w):         # the pair for -i*w/2
    return ((), p_trim([Fr(-1, 2) * Fr(w)]))
def _pc_hop_c(w):       # the pair for +i*w/2
    return ((), p_trim([Fr(1, 2) * Fr(w)]))

def build_H_sym(lam=None, n0=None):
    """Symbolic port of the d44d build_H: collar of {n0} scaled by (1-lam)."""
    H = {}
    def addH(i, j, z):
        H[(i, j)] = pc_add(H.get((i, j), PCZ), z)
    for n in range(L):
        wm = (Fr(1) - lam) if (lam is not None and n == n0) else Fr(1)
        addH(idx(n, 0), idx(n, 0), _pc_mass(wm))
        addH(idx(n, 1), idx(n, 1), _pc_mass(-wm))
    for n in range(L):
        wb = ((Fr(1) - lam) if (lam is not None and
                                (n == n0 or (n + 1) % L == n0)) else Fr(1))
        for s in range(2):
            for sp in range(2):
                if SX[sp][s] == 0: continue
                addH(idx(n + 1, sp), idx(n, s), _pc_hop(wb))
                addH(idx(n, s), idx(n + 1, sp), _pc_hop_c(wb))
    return {k: v for k, v in H.items() if not pc_is0(v)}

def build_H_R_sym(Rset, lam):
    """Symbolic port of the d44d build_H_R: sites in Rset and bonds meeting
    Rset carry weight (1-lam)."""
    H = {}
    def addH(i, j, z):
        H[(i, j)] = pc_add(H.get((i, j), PCZ), z)
    for n in range(L):
        wm = (Fr(1) - lam) if (n % L) in Rset else Fr(1)
        addH(idx(n, 0), idx(n, 0), _pc_mass(wm))
        addH(idx(n, 1), idx(n, 1), _pc_mass(-wm))
    for n in range(L):
        wb = ((Fr(1) - lam) if ((n % L) in Rset or ((n + 1) % L) in Rset)
              else Fr(1))
        for s in range(2):
            for sp in range(2):
                if SX[sp][s] == 0: continue
                addH(idx(n + 1, sp), idx(n, s), _pc_hop(wb))
                addH(idx(n, s), idx(n + 1, sp), _pc_hop_c(wb))
    return {k: v for k, v in H.items() if not pc_is0(v)}

def num_mul_sym(A, B):
    """Product of poly-complex matrices (the d44d num_mul, entries symbolic)."""
    cols = {}
    for (i, j), v in B.items():
        cols.setdefault(i, []).append((j, v))
    out = {}
    for (i, k), a in A.items():
        for (j, v) in cols.get(k, []):
            out[(i, j)] = pc_add(out.get((i, j), PCZ), pc_mul(a, v))
    return {k: v for k, v in out.items() if not pc_is0(v)}

MINUS_I_POW = {0: (Fr(1), Fr(0)), 1: (Fr(0), Fr(-1)),
               2: (Fr(-1), Fr(0)), 3: (Fr(0), Fr(1))}

def exp_series_sym(H):
    """U(Delta) = sum_k (-i Delta)^k H^k / k! — the d44d exp_series; the
    only divisions are the integer factorials (as exact Fractions)."""
    out = {(i, i): s_one() for i in range(DIM)}
    P = {(i, i): PC_ONE for i in range(DIM)}
    fact = 1
    for k in range(1, ORD + 1):
        P = num_mul_sym(P, H)
        fact *= k
        cre, cim = MINUS_I_POW[k % 4]
        cre, cim = cre / fact, cim / fact
        for key, v in P.items():
            pc = pc_cscale(v, cre, cim)
            if pc_is0(pc): continue
            s = list(out.get(key, s_zero()))
            s[k] = pc_add(s[k], pc)
            out[key] = s
    return out

def gamma_series_sym(U):
    """Gamma(U) = |U|^2 entrywise: s_mul(v, conj(v)) — conjugation negates
    the imaginary polynomial of each pair (m and Delta are real)."""
    out = {}
    for k, v in U.items():
        g = s_mul(v, s_conj(v))
        if not s_is0(g): out[k] = g
    return out

def coeff_matrix_sym(M, p):
    return {k: v[p] for k, v in M.items() if not pc_is0(v[p])}

def comm_sym(X, Y):
    """[X, Y] on poly-complex coefficient matrices (the d44d comm_num; the
    numeric dust drop becomes an exact-zero drop)."""
    XY = {}
    for (i, k), a in X.items():
        for (kk, j), b in Y.items():
            if k != kk: continue
            XY[(i, j)] = pc_add(XY.get((i, j), PCZ), pc_mul(a, b))
    for (i, k), a in Y.items():
        for (kk, j), b in X.items():
            if k != kk: continue
            XY[(i, j)] = pc_sub(XY.get((i, j), PCZ), pc_mul(a, b))
    return {k: v for k, v in XY.items() if not pc_is0(v)}

def tau_D_pairs_sym(A_at, rs):
    """The d43a/d44d tau/D first-moment identification, symbolic:
    tau(delta,s,s') = sum_{r in rs} r * sum_i [A(0), A(r)]_{(i,s),(i+delta,s')}
    D(s,s') = sum_delta delta * tau(delta,s,s') — all weights integers."""
    A0 = A_at(0)
    tau = {}
    for r in rs:
        Ar = A_at(r)
        XY = comm_sym(A0, Ar)
        for (i, j) in sorted(XY):
            v = XY[(i, j)]
            si, sj = i // 2, j // 2
            delta_ = (sj - si) % L
            if delta_ > L // 2: delta_ -= L
            key = (delta_, i % 2, j % 2)
            tau[key] = pc_add(tau.get(key, PCZ), pc_iscale(v, r))
    D = {}
    for (delta_, a_, b_) in sorted(tau):
        D[(a_, b_)] = pc_add(D.get((a_, b_), PCZ),
                             pc_iscale(tau[(delta_, a_, b_)], delta_))
    tau = {k: v for k, v in tau.items() if not pc_is0(v)}
    return tau, D

# ---- committed regression targets (read-only sources, cited) ---------------
# KTAB grid values: v10/data/d44d_slab_kappa_exact.out, KG2 table (28-point
# hull; the 7 masses below are the pin's m = 1/2, 1 anchors plus 5 more).
KREF = [(Fr(1, 16), Fr(258313, 9437184)),
        (Fr(1, 4), Fr(793, 36864)),
        (Fr(1, 2), Fr(13, 2304)),
        (Fr(5, 8), Fr(-1991, 589824)),
        (Fr(1), Fr(-1, 72)),
        (Fr(3, 2), Fr(253, 2304)),
        (Fr(2), Fr(11, 18))]
# LT signed channel values: v10/code/d44d_slab_kappa_exact.py, REF_LT (T5).
REF_LT = {Fr(1, 2): {(1, 'flip'): Fr(1, 9216), (-1, 'flip'): Fr(-1, 9216),
                     (2, 'same'): Fr(-23, 9216), (-2, 'same'): Fr(23, 9216),
                     (3, 'flip'): Fr(-1, 1024), (-3, 'flip'): Fr(1, 1024),
                     (4, 'same'): Fr(1, 512), (-4, 'same'): Fr(-1, 512)},
          Fr(1): {(1, 'flip'): Fr(-19, 1152), (-1, 'flip'): Fr(19, 1152),
                  (2, 'same'): Fr(-17, 2304), (-2, 'same'): Fr(17, 2304),
                  (3, 'flip'): Fr(1, 128), (-3, 'flip'): Fr(-1, 128),
                  (4, 'same'): Fr(1, 512), (-4, 'same'): Fr(-1, 512)}}
# The D44d-identified quartic (the YG1 target): (9m^4 - 15m^2 + 4)/144.
KAPPA_TARGET = p_trim([Fr(1, 36), Fr(0), Fr(-5, 48), Fr(0), Fr(1, 16)])

# ============================================================================
print("[d45a — the symbolic-m closure of kappa: the identification pipeline")
print("  run with the mass as a FORMAL VARIABLE]")
print("  banner: EXACT symbolic arithmetic — every matrix entry is a pair of")
print("  polynomials in m (real, imaginary) with Fraction coefficients; the")
print("  Delta-series is a list of such pairs; ZERO floats (no mpmath import,")
print("  no float literal, no tolerance — every gate is polynomial equality).")
print("  Scope: the committed d44d SINGLETON identification, ORD = 4, L = 12,")
print("  both rules (EXC read at Delta^2, LT at Delta^4), tau over r = 1..4 —")
print("  the tau_D_sg0/kappa_pipeline code path ported structurally; the slab")
print("  arms are m-pointwise-verified at #353 and inherit by the A5 weight-")
print("  independence note (declared NOT re-run symbolically; pin section 4).")
print("  DIVISION AUDIT (the pin's failure mode, verified in the port): the")
print("  only divisions anywhere are by integer constants — the 1/2 hopping")
print("  normalization and the 1/k! factorials, entering as exact Fractions;")
print("  the Neumann inversion starts at the identity (gated constant-free")
print("  below by assertion); the polynomial layer defines NO division of")
print("  polynomials, so an m-dependent division would raise TypeError.")
print("  Exact-zero dropping replaces the committed numeric dust drops (an")
print("  identically-zero entry carries no information; mathematically inert).")
print("  Regression sources (read-only): the KTAB rationals from")
print("  v10/data/d44d_slab_kappa_exact.out (KG2) and the REF_LT signed")
print("  channel table from v10/code/d44d_slab_kappa_exact.py (T5).")
print("  Ring-homomorphism note (YG0): evaluation m -> m0 is a homomorphism")
print("  Q[m] -> Q, so the derived polynomials evaluated at m0 ARE the")
print("  pipeline outputs at mass m0; agreement with the committed grid is")
print("  the regression content.")
print("  Deterministic: no RNG, no wall clock, no environment reads; sorted")
print("  iteration at every print; rerun byte-identical (YG4).")

# ============================================================================
print("\n[Y-PORT — port fidelity of the symbolic builders]")
n0 = 3
pf_ok = True
for lamv in (Fr(1), Fr(1, 2)):
    Ha = build_H_sym(lam=lamv, n0=n0)
    Hb = build_H_R_sym({n0}, lamv)
    pf_ok &= set(Ha) == set(Hb) and all(Ha[k] == Hb[k] for k in Ha)
Hfree_a = build_H_sym()
Hfree_b = build_H_R_sym(set(), Fr(0))
pf_ok &= set(Hfree_a) == set(Hfree_b) and all(
    Hfree_a[k] == Hfree_b[k] for k in Hfree_a)
check("PF1 the generalized region collar builder == the singleton builder "
      "entrywise as POLYNOMIAL PAIRS (lam = 1 and 1/2), and both give the "
      "free H on the empty region", pf_ok)

H_full = build_H_sym()
herm_ok = set(H_full) == {(j, i) for (i, j) in H_full} and all(
    H_full[(i, j)] == pc_conj(H_full[(j, i)]) for (i, j) in H_full)
mass_lin_ok = True
for (i, j), (re, im) in sorted(H_full.items()):
    if i == j:
        mass_lin_ok &= im == () and len(re) == 2 and re[0] == 0
    else:
        mass_lin_ok &= re == () and len(im) == 1
check("PF2 the symbolic H is Hermitian as a polynomial-pair matrix; the "
      "mass enters ONLY linearly on the diagonal (deg-1 real polynomials "
      "with zero constant term); every hopping entry is a pure-imaginary "
      "m-free constant", herm_ok and mass_lin_ok,
      f"{len(H_full)} nonzero entries")

# ============================================================================
print("\n[Y-PIPE — the symbolic pipeline: U_free, Gamma, Neumann inverse, "
      "per-site J, tau/D]")
U_free = exp_series_sym(H_full)
Gam_free = gamma_series_sym(U_free)
d0_ok = all(Gam_free.get((i, i), s_zero())[0] == PC_ONE for i in range(DIM)) \
    and all(pc_is0(v[0]) for (i, j), v in Gam_free.items() if i != j)
check("PIPE-1 Gamma(U_free) has Delta^0 == identity exactly (the Neumann "
      "precondition; N = Gamma - I is constant-free by assertion inside "
      "the inversion)", d0_ok)
Gfi = m_neumann_inv_sym(Gam_free)
gam_real_ok = all(not v[k][1] for v in Gam_free.values()
                  for k in range(ORD + 1))
gfi_real_ok = all(not v[k][1] for v in Gfi.values() for k in range(ORD + 1))
check("PIPE-2 Gamma(U_free) and its Neumann inverse are REAL polynomial "
      "matrices (every imaginary polynomial identically zero) — |U|^2 "
      "realness holds symbolically", gam_real_ok and gfi_real_ok,
      f"Gfi: {len(Gfi)} nonzero series entries")
d1_free_ok = all(pc_is0(v[1]) for v in Gam_free.values())
check("PIPE-3 (round-1 minor-2a) Gamma(U_free) is Delta^1-FREE as a "
      "polynomial statement (the Neumann remainder N = Gamma - I starts "
      "at Delta^2 — gated, no longer asserted)", d1_free_ok)
_prod = m_mul_sym(Gfi, Gam_free)
prod_id_ok = (all(_prod.get((i, i), s_zero())[0] == PC_ONE
                  and all(pc_is0(_prod[(i, i)][k]) for k in range(1, ORD + 1))
                  for i in range(DIM))
              and all(all(pc_is0(v[k]) for k in range(ORD + 1))
                      for (i, j), v in _prod.items() if i != j))
check("PIPE-4 (round-1 minor-2b) Gfi . Gamma(U_free) == I as a truncated "
      "series of polynomial matrices (the inverse verified by product, "
      "closing the single-gate margin the round exhibited via its M5 "
      "mutant)", prod_id_ok)

JCACHE = {}
def J_region_sym(site, rule):
    """The d44d A_region/J path, symbolic: B = collar-deleted H (lam = 1);
    EXC: J = Gamma(exp(B)) Gfi; LT: J = Gamma(exp(B) exp(C)) Gfi, C = H - B."""
    key = (rule, site)
    if key in JCACHE: return JCACHE[key]
    B = build_H_R_sym({site % L}, Fr(1))
    if rule == 'EXC':
        J = m_mul_sym(gamma_series_sym(exp_series_sym(B)), Gfi)
    else:
        C = {}
        for k in sorted(set(H_full) | set(B)):
            v = pc_sub(H_full.get(k, PCZ), B.get(k, PCZ))
            if not pc_is0(v): C[k] = v
        U = m_mul_sym(exp_series_sym(B), exp_series_sym(C))
        J = m_mul_sym(gamma_series_sym(U), Gfi)
    JCACHE[key] = J
    return J

EXTRACT_ORD = {'EXC': 2, 'LT': 4}
def A_sym(site, rule):
    return coeff_matrix_sym(J_region_sym(site, rule), EXTRACT_ORD[rule])

tauE, DE = tau_D_pairs_sym(lambda r: A_sym(r, 'EXC'), (1, 2, 3, 4))
print("  EXC identification done (tau over r = 1..4, read at Delta^2)")
tauL, DL = tau_D_pairs_sym(lambda r: A_sym(r, 'LT'), (1, 2, 3, 4))
print("  LT identification done (tau over r = 1..4, read at Delta^4)")
KAPPA_SYM = DL.get((0, 0), PCZ)[0]

# ============================================================================
print("\n[YG0 — regression: the derived polynomials evaluated on the "
      "committed grid]")
print("  m       committed KTAB      symbolic kappa(m) eval   EXC eval")
yg0_lt_ok = True
yg0_exc_ok = True
DE00 = DE.get((0, 0), PCZ)
for mfr, kref in KREF:
    kv = p_eval(KAPPA_SYM, mfr)
    ev = p_eval(DE00[0], mfr)
    okL = (kv == kref) and p_eval(DL.get((0, 0), PCZ)[1], mfr) == 0
    okE = (ev == Fr(1)) and p_eval(DE00[1], mfr) == 0
    yg0_lt_ok &= okL
    yg0_exc_ok &= okE
    print(f"  {str(mfr):6s}  {str(kref):>18s}  {str(kv):>18s} "
          f"[{'==' if okL else '!='}]  {str(ev):>4s} "
          f"[{'==' if okE else '!='}]")
check("YG0-A the symbolic LT D(0,0) evaluated at m = 1/2 and m = 1 gives "
      "13/2304 and -1/72 EXACTLY, and at 5 more committed grid masses "
      "reproduces the committed KTAB rationals exactly", yg0_lt_ok,
      "7 masses, exact Fraction equality, zero tolerance")
check("YG0-B the symbolic EXC D(0,0) evaluated at every one of the 7 grid "
      "masses equals 1 exactly (the committed KG2-B mass-blindness)",
      yg0_exc_ok)

# ============================================================================
print("\n[YG1 — THE DERIVATION: symbolic tau tables and the collapse]")

def print_tau_table(tau, rule):
    print(f"  {rule} tau channels (delta, s, s') -> polynomial in m "
          f"[exact Fraction coefficients]:")
    for key in sorted(tau):
        d_, a_, b_ = key
        ch = 'flip' if a_ != b_ else 'same'
        print(f"    delta={d_:+d} (s,s')=({a_},{b_}) [{ch}]: "
              f"{pc_str(tau[key])}")

print_tau_table(tauE, 'EXC')
print("  EXC D entries (polynomials in m):")
for key in sorted(DE):
    print(f"    D{key} = {pc_str(DE[key])}")
PC_MONE = ((Fr(-1),), ())
exc_id_ok = (DE.get((0, 0), PCZ) == PC_ONE and DE.get((1, 1), PCZ) == PC_ONE
             and DE.get((0, 1), PCZ) == PC_MONE
             and DE.get((1, 0), PCZ) == PC_MONE)
check("YG1-A EXC collapse: D == 1*(I - sigma_x) IDENTICALLY IN m — all "
      "four entries are the CONSTANT polynomials (1, -1, -1, 1); the EXC "
      "side is mass-blind as a theorem, not per-mass", exc_id_ok)

print_tau_table(tauL, 'LT')
print("  LT D entries (polynomials in m):")
for key in sorted(DL):
    print(f"    D{key} = {pc_str(DL[key])}")
print(f"  DERIVED: kappa(m) = D_LT(0,0) = {p_str(KAPPA_SYM)}")
lt_ray_ok = (DL.get((1, 1), PCZ) == DL.get((0, 0), PCZ)
             and DL.get((0, 1), PCZ) == DL.get((1, 0), PCZ)
             and DL.get((0, 1), PCZ) == pc_neg(DL.get((0, 0), PCZ)))
check("YG1-B LT collapse: D == kappa(m)*(I - sigma_x) with ONE polynomial "
      "kappa(m) — D(1,1) == D(0,0), D(0,1) == D(1,0) == -D(0,0) as "
      "polynomial-pair identities", lt_ray_ok)
kdiff = p_sub(KAPPA_SYM, KAPPA_TARGET)
check("YG1-C THE ALL-m IDENTITY: kappa(m) - (9m^4 - 15m^2 + 4)/144 == the "
      "ZERO polynomial (every coefficient zero) — the D44d hull-verified "
      "quartic is now DERIVED for all m", kdiff == (),
      f"difference polynomial = {p_str(kdiff)}")

yg1_tab_ok = True
for mv in (Fr(1, 2), Fr(1)):
    got = {}
    for (d_, a_, b_), v in sorted(tauL.items()):
        if (a_, b_) in ((0, 1), (0, 0)):
            val = p_eval(v[0], mv)
            imv = p_eval(v[1], mv)
            yg1_tab_ok &= imv == 0
            if val != 0:
                got[(d_, 'flip' if a_ != b_ else 'same')] = val
    yg1_tab_ok &= got == REF_LT[mv]
check("YG1-D the symbolic LT tau table evaluated at m = 1/2 and m = 1 "
      "reproduces the committed REF_LT signed channel values exactly "
      "(set equality of nonzero channels AND exact values)", yg1_tab_ok,
      "the d44d T5 table is the m-evaluation of these polynomials")

# ============================================================================
print("\n[YG2 — the ray identity in m: every off-ray component vanishes "
      "as a POLYNOMIAL]")
yg2_off_ok = True
yg2_detail = []
for rule, D in (('EXC', DE), ('LT', DL)):
    d00 = D.get((0, 0), PCZ)
    d11 = D.get((1, 1), PCZ)
    d01 = D.get((0, 1), PCZ)
    d10 = D.get((1, 0), PCZ)
    # sigma-basis components: ray = c*(I - sigma_x) means cz, cy, cI + cx
    # all vanish; symbolically each is a polynomial pair that must be ().
    cz = pc_sub(d00, d11)                 # 2*cz
    cy = pc_sub(d01, d10)                 # 2i*cy
    ci_plus_cx = pc_add(d00, d01)         # cI + cx (the ray closure)
    ok = pc_is0(cz) and pc_is0(cy) and pc_is0(ci_plus_cx)
    yg2_off_ok &= ok
    yg2_detail.append(f"{rule}: D00-D11 == {pc_str(cz)}, D01-D10 == "
                      f"{pc_str(cy)}, D00+D01 == {pc_str(ci_plus_cx)}")
check("YG2-A off-ray components of BOTH rules' identified operators are "
      "the ZERO polynomial: D00 - D11 == 0 (sigma_z), D01 - D10 == 0 "
      "(sigma_y), D00 + D01 == 0 (the I/sigma_x ray closure) — the "
      "collapse is an all-m theorem, not pointwise", yg2_off_ok,
      "; ".join(yg2_detail))

yg2_real_ok = True
for tau in (tauE, tauL):
    for v in tau.values():
        yg2_real_ok &= v[1] == ()
for D in (DE, DL):
    for v in D.values():
        yg2_real_ok &= v[1] == ()
for rule in ('EXC', 'LT'):
    sites_b = range(6) if rule == 'LT' else range(5)
    for r in sites_b:
        for v in A_sym(r, rule).values():
            yg2_real_ok &= v[1] == ()
check("YG2-B REALITY as polynomials: every A-coefficient entry (all "
      "retained sites of both rules — round-1 nit: LT site 5 now "
      "included), every tau channel, and every D entry has "
      "identically-zero imaginary polynomial", yg2_real_ok)

yg2_odd_ok = True
for tau in (tauE, tauL):
    for (d_, a_, b_), v in sorted(tau.items()):
        yg2_odd_ok &= pc_is0(pc_add(v, tau.get((-d_, a_, b_), PCZ)))
check("YG2-C delta-odd IN m: tau(-delta,s,s') == -tau(delta,s,s') as a "
      "polynomial identity in every channel of both rules (the committed "
      "B6 anchor upgraded to all m)", yg2_odd_ok)

sub_ok = True
sub_det = []
for rule, orders in (('EXC', (1,)), ('LT', (1, 2, 3))):
    sites = range(6) if rule == 'LT' else range(5)
    for site in sites:
        J = J_region_sym(site, rule)
        id0 = all(J.get((i, i), s_zero())[0] == PC_ONE for i in range(DIM)) \
            and all(pc_is0(v[0]) for (i, j), v in J.items() if i != j)
        zs = all(coeff_matrix_sym(J, p) == {} for p in orders)
        sub_ok &= id0 and zs
    sub_det.append(f"{rule}: orders {orders} zero at sites "
                   f"{list(sites)}, Delta^0 == I")
check("YG2-D sub-onset validity as polynomials: J^EXC order 1 and J^LT "
      "orders 1-3 are ZERO polynomial matrices at every site used; "
      "Delta^0 == identity exactly", sub_ok, "; ".join(sub_det))

slotE3 = comm_sym(A_sym(0, 'EXC'), A_sym(3, 'EXC'))
slotE4 = comm_sym(A_sym(0, 'EXC'), A_sym(4, 'EXC'))
slotL5 = comm_sym(A_sym(0, 'LT'), A_sym(5, 'LT'))
check("YG2-E completeness as polynomials: the EXC commutators at r = 3, 4 "
      "vanish identically (the r = 1..4 sum is EXACTLY the r = 1..2 "
      "kernel sum) and the LT completeness slot [A(0), A(5)] == 0 — the "
      "r = 1..4 identification is complete for both rules at all m",
      slotE3 == {} and slotE4 == {} and slotL5 == {},
      f"entry counts: EXC r=3: {len(slotE3)}, EXC r=4: {len(slotE4)}, "
      f"LT r=5: {len(slotL5)}")

# ============================================================================
print("\n[YG3 — structural origin: which channels carry which factors]")

def poly_x_from_even(p):
    """p(m) with only even powers -> q(x), x = m^2; else None."""
    if any(c != 0 for k, c in enumerate(p) if k % 2 == 1):
        return None
    return p_trim([p[k] for k in range(0, len(p), 2)])

def int_clear(px):
    """q(x) over Q -> (den, [int coeffs ascending]) with q = ints/den."""
    den = 1
    for c in px:
        den = den * c.denominator // math.gcd(den, c.denominator)
    return den, [int(c * den) for c in px]

def divisors(n):
    n = abs(n)
    if n == 0: return []
    f = {}
    t, d = n, 2
    while d * d <= t:
        while t % d == 0:
            f[d] = f.get(d, 0) + 1
            t //= d
        d += 1
    if t > 1: f[t] = f.get(t, 0) + 1
    ds = {1}
    for pr, e in f.items():
        ds = {x * pr ** i for x in ds for i in range(e + 1)}
    return sorted(ds)

def strip_rational_roots(ic):
    """Integer poly (ascending) -> (roots list of Fr, residual int poly).
    Exact synthetic division; rational-root theorem candidates."""
    roots = []
    ic = list(ic)
    while len(ic) > 1 and ic[0] == 0:          # x = 0 roots
        roots.append(Fr(0))
        ic = ic[1:]
    changed = True
    while changed and len(ic) > 2:
        changed = False
        cands = [Fr(sg * p, q) for p in divisors(ic[0])
                 for q in divisors(ic[-1]) for sg in (1, -1)]
        for r in sorted(set(cands)):
            if sum(Fr(c) * r ** k for k, c in enumerate(ic)) == 0:
                q = []                          # exact synthetic division
                acc = Fr(0)
                for c in reversed(ic):
                    acc = acc * r + c
                    q.append(acc)
                q = q[:-1][::-1]                # quotient, ascending
                roots.append(r)
                _, ic = int_clear(p_trim([Fr(x) for x in q]))
                ic = list(ic)
                changed = True
                break
    if len(ic) == 2:                            # linear residual: exact root
        roots.append(Fr(-ic[0], ic[1]))
        ic = [ic[1]]
    return roots, ic

def quad_roots(ic):
    """Integer quadratic [a0, a1, a2] -> (disc, sqrt or None, roots or None)."""
    a0, a1, a2 = ic
    disc = a1 * a1 - 4 * a2 * a0
    s = math.isqrt(disc) if disc >= 0 else None
    if s is not None and s * s == disc:
        return disc, s, sorted((Fr(-a1 - s, 2 * a2), Fr(-a1 + s, 2 * a2)))
    return disc, None, None

def factor_report(label, p):
    """Print the exact factorization content of an even polynomial in m;
    returns the rational x-roots found (delivered; only kappa is gated)."""
    if not p:
        print(f"    {label}: the zero polynomial")
        return []
    px = poly_x_from_even(p)
    if px is None:
        print(f"    {label}: not even in m (odd coefficients present)")
        return []
    if len(px) == 1:
        print(f"    {label}: CONSTANT in m = {px[0]}")
        return []
    den, ic = int_clear(px)
    print(f"    {label}: in x = m^2: ({' + '.join(f'({c})*x^{k}' for k, c in enumerate(ic) if c != 0)})/{den}")
    roots = []
    if len(ic) == 2:
        roots = [Fr(-ic[0], ic[1])]
        print(f"      linear in x: exact rational root x = {roots[0]}")
    elif len(ic) == 3:
        disc, s, rr = quad_roots(ic)
        if rr is not None:
            roots = list(rr)
            print(f"      quadratic-in-m^2 route: disc = {disc} = {s}^2 "
                  f"(perfect square) -> exact rational roots x = {rr[0]}, "
                  f"{rr[1]}")
        else:
            print(f"      quadratic-in-m^2 route: disc = {disc} (not a "
                  f"perfect square) — irreducible over Q AS A QUADRATIC "
                  f"IN x = m^2 (round-1 minor-1 scope; the disc "
                  f"inference decides x-factorization only; the "
                  f"m-quartic could a priori still split into "
                  f"quadratics in m — checked next)")
            a0, a1, a2 = ic
            # biquadratic split a2*m^4 + a1*m^2 + a0 =
            # a2*(m^2 + c*m + d)(m^2 - c*m + d) needs d^2 = a0/a2 and
            # 2d - c^2 = a1/a2 with rational c, d; c = 0 is the disc
            # route already refuted, so require c != 0 rational:
            bi_split = False
            r0 = Fr(a0, a2)
            if r0 >= 0:
                dn, dd = r0.numerator, r0.denominator
                sn, sd = math.isqrt(dn), math.isqrt(dd)
                if sn * sn == dn and sd * sd == dd:
                    for d_ in (Fr(sn, sd), Fr(-sn, sd)):
                        c2 = 2 * d_ - Fr(a1, a2)
                        if c2 > 0:
                            cn, cd = c2.numerator, c2.denominator
                            qn, qd = math.isqrt(cn), math.isqrt(cd)
                            if qn * qn == cn and qd * qd == cd:
                                bi_split = True
            print(f"      biquadratic m-split (m^2 +- c m + d over Q, "
                  f"c != 0): {'EXISTS' if bi_split else 'NONE'} -> "
                  f"{'REDUCIBLE in m' if bi_split else 'irreducible over Q in m as well'}")
    else:
        roots, resid = strip_rational_roots(ic)
        if roots:
            print(f"      rational roots stripped: "
                  f"{', '.join(str(r) for r in roots)}")
        if len(resid) == 3:
            disc, s, rr = quad_roots(resid)
            if rr is not None:
                roots += rr
                print(f"      residual quadratic: disc = {disc} = {s}^2 "
                      f"(perfect square) -> rational roots {rr[0]}, {rr[1]}")
            else:
                print(f"      residual quadratic irreducible over Q: disc = "
                      f"{disc} (not a perfect square)")
        elif len(resid) > 3:
            print(f"      residual degree {len(resid) - 1} with no rational "
                  f"roots (delivered as-is)")
    if roots:
        fstr = " * ".join(f"({r.denominator}*m^2 - {r.numerator})"
                          for r in sorted(roots))
        print(f"      rational x-roots as m^2-factors: {fstr}")
    return sorted(roots)

print("  the D(0,0) combination is D00 = sum_delta delta*tau(delta,0,0); "
      "channel content:")
same_terms = [(d_, tauL[(d_, 0, 0)]) for (d_, a_, b_) in sorted(tauL)
              if (a_, b_) == (0, 0)]
comb = PCZ
for d_, v in same_terms:
    print(f"    delta={d_:+d}: tau = {pc_str(v)}")
    print(f"              delta*tau = {pc_str(pc_iscale(v, d_))}")
    comb = pc_add(comb, pc_iscale(v, d_))
print(f"  the delta-weighted combination (same channels): {pc_str(comb)}")
flip_comb = PCZ
for (d_, a_, b_) in sorted(tauL):
    if (a_, b_) == (0, 1):
        flip_comb = pc_add(flip_comb, pc_iscale(tauL[(d_, a_, b_)], d_))
print(f"  the flip-channel combination (D(0,1)): {pc_str(flip_comb)}")
check("YG3-A the delta-weighted same-channel combination == kappa(m) and "
      "the flip-channel combination == -kappa(m), recombined from the "
      "retained channel objects (round-1 nit: same in-memory objects, "
      "not an independent rebuild — the independent rebuild is the "
      "frozen round's)",
      comb == DL.get((0, 0), PCZ) and comb[0] == KAPPA_SYM
      and flip_comb == DL.get((0, 1), PCZ)
      and flip_comb[0] == p_neg(KAPPA_SYM))

print("  exact factorization over Q of each channel polynomial and of "
      "kappa (x = m^2):")
for d_, v in same_terms:
    factor_report(f"tau(delta={d_:+d}, same)", v[0])
for (d_, a_, b_) in sorted(tauL):
    if (a_, b_) == (0, 1):
        factor_report(f"tau(delta={d_:+d}, flip)", tauL[(d_, a_, b_)][0])
kroots = factor_report("kappa(m)", KAPPA_SYM)
f1 = p_trim([Fr(-1), Fr(0), Fr(3)])          # 3m^2 - 1
f2 = p_trim([Fr(-4), Fr(0), Fr(3)])          # 3m^2 - 4
fac_ok = (p_scale(p_mul(f1, f2), Fr(1, 144)) == KAPPA_SYM
          and kroots == [Fr(1, 3), Fr(4, 3)])
print("  kappa factorization statement: 144*kappa(m) = "
      "(3*m^2 - 1)*(3*m^2 - 4)"
      f"  [exact expansion check: {p_scale(p_mul(f1, f2), Fr(1, 144)) == KAPPA_SYM}]")
check("YG3-B the exact factorization: kappa(m) == (3m^2 - 1)(3m^2 - 4)/144 "
      "by exact polynomial expansion, with the rational x-roots 1/3 and "
      "4/3 found by the integer-discriminant route (81 = 9^2)", fac_ok,
      "zero crossings at m^2 = 1/3 and m^2 = 4/3 for ALL m — no hull")

# which channels carry which factors — the exhibited algebra, exact:
X24 = p_trim([Fr(-5), Fr(0), Fr(24)])        # 24m^2 - 5
Q7 = p_trim([Fr(7), Fr(0), Fr(-60), Fr(0), Fr(36)])   # 36m^4 - 60m^2 + 7
t2 = tauL.get((2, 0, 0), PCZ)[0]
t4 = tauL.get((4, 0, 0), PCZ)[0]
t1 = tauL.get((1, 0, 1), PCZ)[0]
t3 = tauL.get((3, 0, 1), PCZ)[0]
chan_ok = (t4 == (Fr(1, 512),)
           and t2 == p_scale(Q7, Fr(1, 2304))
           and t3 == p_scale(f1, Fr(1, 256))
           and t1 == p_scale(p_mul(f1, X24), Fr(-1, 2304)))
same_recomb = p_add(p_scale(t2, Fr(4)), p_scale(t4, Fr(8)))
flip_recomb = p_add(p_scale(t1, Fr(2)), p_scale(t3, Fr(6)))
recomb_ok = (same_recomb == KAPPA_SYM and flip_recomb == p_neg(KAPPA_SYM))
print("  STRUCTURAL ORIGIN (the exhibited polynomial algebra, exact):")
print("    same sector -> D(0,0): tau(+-2) = +-(36m^4 - 60m^2 + 7)/2304 "
      "[irreducible over Q, disc 2592] and tau(+-4) = +-1/512 [constant];")
print("    by delta-oddness D(0,0) = 4*tau(2) + 8*tau(4) = [4*(36m^4 - "
      "60m^2 + 7) + 36]/2304 — the constant channel shifts the bracket "
      "7 -> 16, and 36m^4 - 60m^2 + 16 = 4*(3m^2 - 1)*(3m^2 - 4): the "
      "factorization EXISTS IN NO SINGLE same channel; it is CREATED by "
      "the delta-weighted addition of the constant tau(4) channel.")
print("    flip sector -> D(0,1): tau(+-1) = -+(3m^2 - 1)*(24m^2 - 5)/2304 "
      "and tau(+-3) = +-(3m^2 - 1)/256 — the factor (3m^2 - 1) is a COMMON "
      "FACTOR of every flip channel; D(0,1) = 2*tau(1) + 6*tau(3) = "
      "(3m^2 - 1)*(64 - 48m^2)/2304 = -(3m^2 - 1)*(3m^2 - 4)/144: the "
      "second factor (3m^2 - 4) emerges from the weighted sum.")
check("YG3-C which channels carry which factors, gated by exact expansion: "
      "tau(4,same) == 1/512; tau(2,same) == (36m^4 - 60m^2 + 7)/2304; "
      "tau(3,flip) == (3m^2 - 1)/256; tau(1,flip) == -(3m^2 - 1)(24m^2 - "
      "5)/2304; and the sector recombinations 4*tau(2) + 8*tau(4) == "
      "kappa(m), 2*tau(1) + 6*tau(3) == -kappa(m)", chan_ok and recomb_ok,
      "(3m^2 - 1) sits in every flip channel; (3m^2 - 4) only in the sums")

# ============================================================================
print("\n[YG4 — purity and determinism]")
no_mp = 'mpmath' not in sys.modules
FLOATS = [0]
FRACS = [0]
def type_walk(obj):
    if isinstance(obj, float):
        FLOATS[0] += 1
    elif isinstance(obj, Fr):
        FRACS[0] += 1
    elif isinstance(obj, (tuple, list)):
        for x in obj: type_walk(x)
    elif isinstance(obj, dict):
        for k in sorted(obj):
            type_walk(k)
            type_walk(obj[k])
for structure in (H_full, tauE, tauL, DE, DL, KAPPA_SYM, KAPPA_TARGET):
    type_walk(structure)
for key in sorted(JCACHE):
    type_walk(JCACHE[key])
for v in Gfi.values():
    type_walk(v)
for m_obj in (U_free, Gam_free):
    for v in m_obj.values():
        type_walk(v)
check("YG4-A ZERO floats: mpmath never imported; a recursive type walk "
      "over every retained object (H, U_free, Gamma_free, Gfi, every "
      "cached J series, both tau tables, both D matrices, kappa) finds "
      "0 float objects and Fraction coefficients only (round-1 nit: "
      "U_free/Gamma_free now walked)", no_mp and FLOATS[0] == 0
      and FRACS[0] > 0,
      f"floats = {FLOATS[0]}, Fraction coefficients walked = {FRACS[0]}")
import tokenize
import io
_src = open(__file__).read()
_toks = list(tokenize.generate_tokens(io.StringIO(_src).readline))
_names = {t.string for t in _toks if t.type == tokenize.NAME}
_numbers = [t.string for t in _toks if t.type == tokenize.NUMBER
            and not t.string.lower().startswith(("0x", "0o", "0b"))]
_banned = {"TOL", "mpmath", "random", "datetime", "getenv", "environ"}
_clean_names = not (_names & _banned)
_no_float_lit = all(all(ch not in s for ch in ".eEjJ")
                    for s in _numbers)
check("YG4-B tolerance-free banner, NOW SELF-VERIFYING (round-1 MAJOR-1 "
      "repaired — the previous form was check(True)): a token-level "
      "self-scan of this source (strings and comments excluded by the "
      "tokenizer, so the probe cannot self-trip) finds NO name in "
      "{TOL, mpmath, random, datetime, getenv, environ} and NO float "
      "or complex NUMBER literal (math is imported for exact integer "
      "gcd/isqrt only); every gate above is exact equality of "
      "polynomial pairs (rerun byte-identity stays an externally "
      "verified protocol line, seeds 0/7 — not this gate's claim)",
      _clean_names and _no_float_lit and len(_numbers) > 0,
      f"banned names absent = {_clean_names}; integer-only NUMBER "
      f"tokens = {_no_float_lit} ({len(_numbers)} scanned)")

# ============================================================================
print(f"\n[SUMMARY] {PASS} PASS / {FAIL} FAIL")
if FAIL:
    print("[VERDICT] FAIL — a symbolic gate broke; per the pin's "
          "pre-registered failure modes, the objects above are the "
          "deliverable; exit 1")
    sys.exit(1)
print("[YG1 VERDICT] the singleton identification at ORD 4, L 12 is now a "
      "THEOREM for ALL m at fixture scale: EXC D = 1*(I - sigma_x) "
      "identically; LT D = kappa(m)*(I - sigma_x) with kappa(m) = "
      "(9*m^4 - 15*m^2 + 4)/144 = (3*m^2 - 1)*(3*m^2 - 4)/144 as an exact "
      "polynomial identity — the D44d hull caveat is CLOSED (the 28-point "
      "verification was the shadow of this identity).")
print("[YG3 VERDICT] structural origin (gated at YG3-C): D(0,0) is fed "
      "ONLY by the same-spin channels — 4*tau(2,same) + 8*tau(4,same) with "
      "tau(2) = (36m^4 - 60m^2 + 7)/2304 IRREDUCIBLE over Q and tau(4) = "
      "1/512 constant; the factorization lives in NO single same channel — "
      "the constant channel's +9 shift of the bracket (7 -> 16) CREATES "
      "36m^4 - 60m^2 + 16 = 4*(3m^2 - 1)*(3m^2 - 4). In the flip sector "
      "(3m^2 - 1) is a COMMON FACTOR of every channel (tau(+-3) = "
      "+-(3m^2 - 1)/256; tau(+-1) = -+(3m^2 - 1)*(24m^2 - 5)/2304) and "
      "(3m^2 - 4) emerges from the weighted sum 2*tau(1) + 6*tau(3) = "
      "-kappa(m), closing the (I - sigma_x) ray. The two zero crossings "
      "have DIFFERENT channel origins: m^2 = 1/3 kills every flip channel "
      "identically; m^2 = 4/3 kills only the combinations.")
print("[VERDICT] d45a delivered: the symbolic-m closure holds — YG0 "
      "regression exact on 7 committed grid masses; YG1 the all-m collapse "
      "identities; YG2 off-ray/reality/sub-onset/delta-odd/completeness "
      "all vanish as polynomials; YG3 the factorization exhibited exactly; "
      "YG4 zero floats. kappa(m) = (3*m^2 - 1)*(3*m^2 - 4)/144 for ALL m "
      "at fixture scale (ORD 4, L 12, singleton; slab arms inherit "
      "pointwise per #353 + A5, declared not re-run).")
