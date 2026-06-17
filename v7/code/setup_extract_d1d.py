"""
SETUP extraction for the SHARD chiral-gap global-optimality residue (v7 Paper XVIII).

Reuses the EXACT functionals from pD_chiral_global_optimality.py (and p9a) so the
comparison is apples-to-apples:
  - seal_solve / gap_vector_seal   -> the per-mode seal fixed point grad G = 0
  - gap_and_Tmarg_KL               -> (m_hat, KL_1d) the 1-D KL of the T-marginal
  - exact_min                      -> the scalar two-value seal on mu* (closed form)

It then:
  (1) STATES the exact D_1D functional, with a HIGH-PRECISION mpmath reimplementation
      of the 1-D KL on a value-multiset (the seal self-consistency / tilt-fixing).
  (2) CONFIRMS m_hat(eps) >= D_1D(mult(eps)) for all eps, equality on mu* (n<=4 exhaustive,
      n=5 sample) -- reproduces pD check (D).
  (3) CONFIRMS the Walsh framing by explicit n=2,3 checks:
        * T_eps = W' @ eps, W' the Walsh-Hadamard matrix with the constant column dropped;
        * the Walsh-Hadamard coefficients of T_eps are (0, eps_1, ..., eps_M) = zero mean,
          every nonzero-frequency coeff = +-1;
        * mu* corresponds to eps_a = -chi_a(s*), s*=all-minus -> eps_a=(-1)^{|a|-1};
        * T = 1 - N*delta_{s*}; multiset mu* = {-(N-1) once, +1 (N-1) times}.
  (4) COMPUTES D_1D(mu*) for n=2..8 at dps>=120 (the closed form -ln(1-2^-n)-delta_n).
  (5) Lists the known NECESSARY conditions for achievability and derives the higher-moment /
      spectral constraints from the +-1-Walsh-coefficient structure (sympy-exact where possible).
"""
import itertools
import numpy as np
import sympy as sp
import mpmath as mp

mp.mp.dps = 140  # >= 120 as required


# ============================================================================
# REUSED VERBATIM from pD_chiral_global_optimality.py (shared machinery)
# ============================================================================
def char_cols(n):
    """Character matrix: rows = states s in {+-1}^n, cols = masks a = 1..2^n-1, entry chi_a(s)."""
    st = np.array(list(itertools.product((-1, 1), repeat=n)), float)
    cols = np.empty((st.shape[0], (1 << n) - 1))
    for mask in range(1, 1 << n):
        idx = [i for i in range(n) if (mask >> i) & 1]
        cols[:, mask - 1] = np.prod(st[:, idx], axis=1)
    return cols, st


def altweight_signs(n):
    return [(-1) ** (bin(mask).count("1") - 1) for mask in range(1, 1 << n)]


def seal_solve(signs, chi0, tol=1e-13, maxit=200):
    """The per-mode SEAL fixed point E_P[eps_a chi_a]=e^{-h_a}; returns (m_hat, p, Tfull).
    VERBATIM from pD (the gap_of_orientation seal fixed point)."""
    chi = chi0 * np.asarray(signs, float)[None, :]
    m = chi.shape[1]
    N = chi.shape[0]
    h = np.zeros(m)

    def Gpot(hh):
        z = chi @ hh
        mx = z.max()
        return mx + np.log(np.mean(np.exp(z - mx))) + np.sum(np.exp(-hh))

    G0 = Gpot(h)
    for _ in range(maxit):
        z = chi @ h
        z -= z.max()
        w = np.exp(z)
        p = w / w.sum()
        E = chi.T @ p
        grad = E - np.exp(-h)
        if np.abs(grad).max() < tol:
            break
        Cov = (chi * p[:, None]).T @ chi - np.outer(E, E)
        J = Cov + np.diag(np.exp(-h))
        try:
            step = np.linalg.solve(J, grad)
        except np.linalg.LinAlgError:
            step = np.linalg.lstsq(J, grad, rcond=None)[0]
        t = 1.0
        Gn = Gpot(h - step)
        if not (Gn <= G0 + 1e-12):
            t = 0.5
            while t > 1e-8 and Gpot(h - t * step) > G0:
                t *= 0.5
            Gn = Gpot(h - t * step)
        h = np.minimum(h - t * step, 40.0)
        G0 = Gpot(h)
    z = chi @ h
    z -= z.max()
    p = np.exp(z)
    p /= p.sum()
    mhat = float(np.sum(p * np.log(p * N)))
    return mhat, p, chi.sum(1)


def gap_vector_seal(signs, chi0, tol=1e-13, maxit=200):
    return seal_solve(signs, chi0, tol=tol, maxit=maxit)[0]


from collections import defaultdict


def gap_and_Tmarg_KL(signs, chi0):
    """(m_hat, KL_1d): the gap D(P*||U) and the 1-D KL of the T-marginal.  VERBATIM from pD.
    By data-processing m_hat >= KL_1d ALWAYS; equality iff seal P* constant on level sets of T."""
    mhat, p, Tfull = seal_solve(signs, chi0)
    N = len(p)
    Plev = defaultdict(float); cnt = defaultdict(int)
    for s in range(N):
        Plev[round(Tfull[s])] += p[s]; cnt[round(Tfull[s])] += 1
    kl1d = sum(Plev[t] * np.log(Plev[t] / (cnt[t] / N)) for t in Plev)
    return mhat, kl1d


def exact_min(n):
    """Scalar seal on mu* = {-(N-1) (x1), +1 (x(N-1))}; VERBATIM from pD/p9a."""
    N = 1 << n
    M = N - 1
    def fp(h):
        w0 = mp.e ** (-h * M)
        eh = mp.e ** (h)
        Z = w0 + M * eh
        E_s1 = (w0 * (-1) + eh * (1)) / Z
        return E_s1 - mp.e ** (-h)
    h = mp.findroot(fp, mp.log(mp.mpf(M)) if M > 1 else mp.mpf("1.0"))
    w0 = mp.e ** (-h * M)
    eh = mp.e ** (h)
    Z = w0 + M * eh
    psi = mp.log(Z / N)
    Ecommon = mp.e ** (-h)
    D = h * (M * Ecommon) - psi
    closed = -mp.log(1 - mp.power(2, -n))
    return D, closed, h


# ============================================================================
# (1) THE EXACT D_1D FUNCTIONAL -- high-precision mpmath, on a value-multiset.
# ============================================================================
# D_1D is the 1-D KL of the T-marginal under the SEAL tilt restricted to the scalar
# field T.  For a multiset with distinct values v_1..v_r and multiplicities c_1..c_r
# (sum c = N), the uniform marginal puts mass q_j = c_j/N on value v_j.  The seal tilts
# the value-histogram by a SINGLE scalar tilt h (the "tilt parameter"): the tilted law is
#      P_j(h) = c_j * exp(h * v_j) / Z(h),   Z(h) = sum_j c_j exp(h * v_j).
# The TILT IS FIXED by the same per-mode seal self-consistency that defines m_hat, projected
# onto the scalar field.  On the scalar field T = sum_a phi_a, the modes are coupled only
# through their common scalar; the seal condition E_P[eps_a chi_a] = e^{-h_a} averaged/equalized
# to the SCALAR mode gives the 1-D stationarity:  the scalar seal sets
#      h such that  (1/M) * E_P[T] = e^{-h}        ... (scalar seal, the tilt self-consistency)
# Equivalently the 1-D reduction is the relative entropy
#      D_1D(mult) = sum_j P_j(h*) * log( P_j(h*) / q_j ),  q_j = c_j/N,
# evaluated at the tilt h* that makes the tilted law the seal fixed point's T-pushforward.
#
# CRITICAL CONSISTENCY ANCHOR: on mu* the field is genuinely two-valued, the M modes equalize
# to one scalar, and the scalar seal self-consistency E[s_1] = e^{-h} (one mode, since all equal)
# coincides with exact_min.  We therefore VERIFY our D_1D matches exact_min on mu* and matches
# pD's float gap_and_Tmarg_KL on every n<=4 orbit (where m_hat = KL_1d exactly).
#
# We implement D_1D in TWO self-consistency conventions and KEEP the one that reproduces both
# (a) exact_min(n) on mu* AND (b) pD's KL_1d on n<=4 -- so it is the SAME functional pD uses,
# at high precision.  Convention M (the per-mode scalar seal) is the one pD's two-value exact_min
# uses; we confirm it equals pD's pushforward-KL on n<=4.

def D1D_perMode(values, mults, n, h0=None):
    """1-D KL with the PER-MODE scalar seal self-consistency  (1/M) E_P[T] = e^{-h}.
    values: list of distinct T-values (mp or int); mults: their multiplicities (sum = N=2^n).
    Returns (D_1D, h*).  All-mpmath, dps as set globally."""
    N = mp.mpf(1 << n)
    M = N - 1
    vs = [mp.mpf(v) for v in values]
    cs = [mp.mpf(c) for c in mults]
    assert abs(sum(cs) - N) < mp.mpf(10) ** (-mp.mp.dps + 20)

    def Ptilt(h):
        z = [h * v for v in vs]
        mx = max(z)
        w = [c * mp.e ** (zz - mx) for c, zz in zip(cs, z)]
        Z = sum(w)
        return [wi / Z for wi in w]

    def seal_resid(h):
        P = Ptilt(h)
        ET = sum(Pj * v for Pj, v in zip(P, vs))   # E_P[T]
        return ET / M - mp.e ** (-h)               # (1/M) E_P[T] = e^{-h}

    # root: monotone in h on (0, inf); bracket and bisect at full precision
    if h0 is None:
        h0 = mp.log(M) if M > 1 else mp.mpf("1.0")
    lo, hi = mp.mpf("1e-30"), mp.mpf("400")
    flo, fhi = seal_resid(lo), seal_resid(hi)
    if flo * fhi > 0:
        # fall back to findroot from h0
        h = mp.findroot(seal_resid, h0)
    else:
        for _ in range(int(mp.mp.dps * 4)):
            mid = (lo + hi) / 2
            fm = seal_resid(mid)
            if flo * fm <= 0:
                hi = mid
            else:
                lo = mid; flo = fm
        h = (lo + hi) / 2
        h = mp.findroot(seal_resid, h)   # polish
    P = Ptilt(h)
    D = mp.mpf(0)
    for Pj, c in zip(P, cs):
        q = c / N
        if Pj > 0:
            D += Pj * mp.log(Pj / q)
    return D, h


# ----------------------------------------------------------------------------
# pD's ACTUAL D_1D = the PUSHFORWARD of the full vector seal P* through T (mpmath).
# This is the functional gap_and_Tmarg_KL computes (the DPI lower bound).  It depends on eps
# through P* (the per-mode vector seal), NOT through the multiset alone -- equality with the
# scalar-tilt form holds only on two-level multisets.  We give the mpmath version so the values
# (and the n<=4 equality m_hat = D_1D) are reproducible at dps>=120.
def vector_seal_and_pushforward_mp(signs, n, dps=140, maxit=4000):
    """Full vector seal grad G=0 (mpmath) + pushforward KL of P* through T.
    Returns (m_hat, D_1D_pushforward, gradnorm).  D_1D = D(law_{P*}(T)||law_U(T))."""
    old = mp.mp.dps; mp.mp.dps = dps
    try:
        st = list(itertools.product((-1, 1), repeat=n))
        N = 1 << n; M = N - 1
        C = []
        for s in st:
            row = []
            for mask in range(1, N):
                p = 1
                for i in range(n):
                    if (mask >> i) & 1:
                        p *= s[i]
                row.append(p)
            C.append(row)
        phi = [[mp.mpf(signs[a] * C[s][a]) for a in range(M)] for s in range(N)]
        Tint = [sum(signs[a] * C[s][a] for a in range(M)) for s in range(N)]
        h = [mp.mpf(0)] * M
        for _ in range(maxit):
            z = [sum(phi[s][a] * h[a] for a in range(M)) for s in range(N)]
            mx = max(z); w = [mp.e ** (z[s] - mx) for s in range(N)]; Zt = sum(w)
            p = [w[s] / Zt for s in range(N)]
            E = [sum(p[s] * phi[s][a] for s in range(N)) for a in range(M)]
            emh = [mp.e ** (-h[a]) for a in range(M)]
            grad = [E[a] - emh[a] for a in range(M)]
            gn = max(abs(g) for g in grad)
            if gn < mp.mpf(10) ** (-(dps - 8)):
                break
            Hk = [[mp.mpf(0)] * M for _ in range(M)]
            for a in range(M):
                for b in range(a, M):
                    cov = sum(p[s] * phi[s][a] * phi[s][b] for s in range(N)) - E[a] * E[b]
                    Hk[a][b] = cov + (emh[a] if a == b else mp.mpf(0)); Hk[b][a] = Hk[a][b]
            step = mp.lu_solve(mp.matrix(Hk), mp.matrix(grad))
            h = [h[a] - step[a] for a in range(M)]
        z = [sum(phi[s][a] * h[a] for a in range(M)) for s in range(N)]
        mx = max(z); w = [mp.e ** (z[s] - mx) for s in range(N)]; Zt = sum(w)
        p = [w[s] / Zt for s in range(N)]
        mhat = sum(p[s] * mp.log(p[s] * N) for s in range(N))
        # pushforward through T
        Plev = {}; cnt = {}
        for s in range(N):
            t = Tint[s]
            Plev[t] = Plev.get(t, mp.mpf(0)) + p[s]; cnt[t] = cnt.get(t, 0) + 1
        D1d = mp.mpf(0)
        for t in Plev:
            q = mp.mpf(cnt[t]) / N
            D1d += Plev[t] * mp.log(Plev[t] / q)
        return mhat, D1d, gn
    finally:
        mp.mp.dps = old


print("=" * 88)
print("(1) THE EXACT D_1D FUNCTIONAL -- consistency anchors")
print("=" * 88)
# Anchor (a): D1D_perMode on mu* must equal exact_min(n) (the closed form).
for n in [2, 3, 4, 5, 6]:
    N = 1 << n
    D_mu_star, h_mu = D1D_perMode([-(N - 1), 1], [1, N - 1], n)
    D_exact, closed, h_exact = exact_min(n)
    print("  n=%d : D1D_perMode(mu*) = %s" % (n, mp.nstr(D_mu_star, 30)))
    print("        exact_min(n)      = %s   | diff = %s | tilt diff = %s"
          % (mp.nstr(D_exact, 30), mp.nstr(abs(D_mu_star - D_exact), 3),
             mp.nstr(abs(h_mu - h_exact), 3)))
    assert abs(D_mu_star - D_exact) < mp.mpf(10) ** (-60), "D1D != exact_min on mu* at n=%d" % n
print("  ANCHOR (a) PASS: D1D_perMode == exact_min on mu* (n=2..6) to >60 digits.")

# Anchor (b) -- THE LOAD-BEARING SUBTLETY.  pD's actual D_1D is gap_and_Tmarg_KL's
# PUSHFORWARD of the FULL vector seal P* through T:  D_1D(eps) := D(law_{P*}(T)||law_U(T)),
# the masses being the T-LEVEL-SET masses of the vector seal P*.  This is NOT a standalone
# scalar-tilt functional of the multiset alone: at MULTI-LEVEL multisets the level masses are
# NOT a single-tilt exponential family in v (the per-mode tilt vector h is not constant).
# The scalar-tilt D1D_perMode reproduces pD's pushforward ONLY on TWO-LEVEL multisets
# (where the M modes equalize to one scalar -- e.g. mu* and its mirror).  We verify exactly that.
worst_2lvl = 0.0
worst_multi = 0.0
n_2lvl = 0; n_multi = 0
for n in [2, 3, 4]:
    chi0, _ = char_cols(n)
    M = (1 << n) - 1
    seen = {}
    for bits in itertools.product((-1, 1), repeat=M):
        T = (chi0 * np.asarray(bits, float)[None, :]).sum(1)
        key = tuple(sorted(int(round(t)) for t in T))
        if key in seen:
            continue
        seen[key] = True
        mh, kl = gap_and_Tmarg_KL(bits, chi0)
        vals = sorted(set(key))
        mults = [key.count(v) for v in vals]
        D1d, _h = D1D_perMode(vals, mults, n)
        d = abs(float(D1d) - kl)
        if len(vals) == 2:
            worst_2lvl = max(worst_2lvl, d); n_2lvl += 1
        else:
            worst_multi = max(worst_multi, d); n_multi += 1
print("  ANCHOR (b): TWO-LEVEL multisets (%d of them, n<=4): max |D1D_perMode - pD.KL_1d| = %.3e" % (n_2lvl, worst_2lvl))
print("              MULTI-LEVEL multisets (%d of them, n<=4): max |D1D_perMode - pD.KL_1d| = %.3e" % (n_multi, worst_multi))
assert worst_2lvl < 1e-9, "D1D_perMode must match pD KL_1d on TWO-LEVEL multisets"
assert worst_multi > 1e-2, "expected scalar-tilt to DIFFER from pushforward on multi-level"
print("  ANCHOR (b) RESULT: the scalar-tilt D1D_perMode == pD's pushforward-KL EXACTLY on two-level")
print("    multisets (incl. mu*), but DIFFERS on multi-level ones -> pD's D_1D is the PUSHFORWARD of")
print("    the FULL vector seal, NOT a standalone scalar-tilt-of-the-histogram functional.")
print("    [The scalar-tilt 'tilt the value-histogram by the seal' picture is EXACT only on two-level")
print("     multisets; for the two-point family (F) it is exactly the functional that is minimized.]")

# Anchor (c): mpmath pushforward D_1D == m_hat at n<=4 (gap IS a multiset functional there),
# and == D1D_perMode on mu*.  High-precision confirmation of pD's data-processing equality.
print("  ANCHOR (c) [mpmath dps=140, pushforward of full vector seal]:")
for (n, label, signs) in [
        (3, "mu*", altweight_signs(3)),
        (3, "all+1", [1] * 7),
        (3, "multi-level {-5,-1,3}",
         None)]:
    if signs is None:
        chi0, _ = char_cols(3)
        for bits in itertools.product((-1, 1), repeat=7):
            T = chi0 @ np.asarray(bits, float)
            if tuple(sorted(int(round(t)) for t in T)) == (-5, -1, -1, -1, -1, 3, 3, 3):
                signs = list(bits); break
    mhat_mp, D1d_mp, gn = vector_seal_and_pushforward_mp(signs, 3, dps=140)
    print("    n=3 %-22s : m_hat = %s  D_1D(pushfwd) = %s  |m_hat-D_1D| = %s"
          % (label, mp.nstr(mhat_mp, 22), mp.nstr(D1d_mp, 22), mp.nstr(abs(mhat_mp - D1d_mp), 3)))
    assert abs(mhat_mp - D1d_mp) < mp.mpf(10) ** (-100), "pushforward != m_hat at n<=4 (gap IS multiset fn there)"
print("    => at n<=4, D_1D(pushforward) = m_hat to >100 digits (gap a pure multiset functional).")


# ============================================================================
# (2) CONFIRM the data-processing reduction  m_hat(eps) >= D_1D(mult(eps)),
#     equality at mu* -> target is the 1-D minimization over achievable multisets.
# ============================================================================
print()
print("=" * 88)
print("(2) DATA-PROCESSING REDUCTION  m_hat(eps) >= D_1D(mult(eps)), equality on mu*")
print("=" * 88)
# (i) equality on mu* (already shown in (1) anchor a): m_hat(mu*) = D_1D(mu*).
# (ii) the inequality m_hat >= D_1D for ALL eps: reproduce pD check (D) -- equality n<=4,
#      strict inequality + no DPI violation at n=5.
print("  (i) equality on mu*: m_hat(mu*) = D_1D(mu*) -- confirmed in (1), to >60 digits.")
# (ii) exhaustive n<=4 equality (m_hat == KL_1d), and n=5 DPI direction + strict failure of equality.
worst_eq = 0.0
for n in [2, 3, 4]:
    chi0, _ = char_cols(n)
    M = (1 << n) - 1
    for bits in itertools.product((-1, 1), repeat=M):
        mh, kl = gap_and_Tmarg_KL(bits, chi0)
        worst_eq = max(worst_eq, abs(mh - kl))
print("  (ii) n<=4 exhaustive: max |m_hat - D_1D| = %.3e (equality => gap is a multiset functional)" % worst_eq)
rng = np.random.default_rng(12345)
chi0_5, _ = char_cols(5); M5 = 31
min_excess = 1e9; max_excess = 0.0
for _ in range(3000):
    eps = (rng.integers(0, 2, M5) * 2 - 1)
    mh, kl = gap_and_Tmarg_KL(eps, chi0_5)
    min_excess = min(min_excess, mh - kl)
    max_excess = max(max_excess, abs(mh - kl))
print("  (ii) n=5 sample (3000): min(m_hat - D_1D) = %.3e (>=0 => DPI holds, m_hat >= D_1D)" % min_excess)
print("       n=5 sample: max|m_hat - D_1D| = %.3e (>0 => equality FAILS for n>=5: gap NOT a multiset fn)"
      % max_excess)
assert worst_eq < 1e-9 and min_excess > -1e-9 and max_excess > 1e-3
print("  REDUCTION CONFIRMED: m_hat(eps) >= D_1D(mult(eps)) all eps (DPI); equality at mu*.")
print("  => TARGET = minimize D_1D over ACHIEVABLE multisets; counterexample iff achievable mult")
print("     with D_1D < D_1D(mu*); proof iff none exists.")


# ============================================================================
# (3) CONFIRM the WALSH framing by explicit small-n checks (n=2,3).
# ============================================================================
print()
print("=" * 88)
print("(3) WALSH FRAMING -- explicit n=2,3 checks")
print("=" * 88)
def walsh_full(n):
    """Full 2^n x 2^n Walsh-Hadamard matrix W[s,a] = chi_a(s) = prod_{i in a} s_i,
    rows s in {+-1}^n (natural order from itertools), cols a = 0..2^n-1 (a=0 the constant)."""
    st = list(itertools.product((-1, 1), repeat=n))
    N = 1 << n
    W = np.empty((N, N), float)
    for si, s in enumerate(st):
        for a in range(N):
            p = 1.0
            for i in range(n):
                if (a >> i) & 1:
                    p *= s[i]
            W[si, a] = p
    return W, st

for n in [2, 3]:
    N = 1 << n; M = N - 1
    W, st = walsh_full(n)
    Wconst = W[:, 0]              # constant column (all ones)
    Wprime = W[:, 1:]            # drop the constant column: N x M, the Walsh matrix W'
    # check it matches char_cols ordering (chi_a, a=1..M)
    chi0, _ = char_cols(n)
    assert np.allclose(Wprime, chi0), "Wprime != char_cols at n=%d" % n
    # (3a) T_eps = W' @ eps for a RANDOM eps
    rng3 = np.random.default_rng(100 + n)
    eps = rng3.integers(0, 2, M) * 2 - 1
    T_direct = chi0 @ eps                    # sum_a eps_a chi_a(s)
    T_walsh = Wprime @ eps
    assert np.allclose(T_direct, T_walsh)
    # (3b) Walsh-Hadamard coefficients of T_eps are (0, eps_1,...,eps_M):
    #      coeff_a = (1/N) sum_s T(s) chi_a(s).  For a=0 -> 0 (zero mean); for a!=0 -> eps_a (+-1).
    coeffs = (W.T @ T_walsh) / N            # length N: coeff for a=0..M
    assert abs(coeffs[0]) < 1e-12, "nonzero mean (a=0 coeff) at n=%d" % n
    assert np.allclose(coeffs[1:], eps), "nonzero-freq coeffs != eps at n=%d" % n
    assert np.allclose(np.abs(coeffs[1:]), 1.0), "coeffs not +-1 at n=%d" % n
    # (3c) mu* via eps_a = -chi_a(s*), s* = all-minus state.
    s_star = tuple([-1] * n)
    eps_mu = np.array([-(np.prod([s_star[i] for i in range(n) if (a >> i) & 1]))
                       for a in range(1, N)], float)
    # eps_a = -chi_a(all-minus) = -(-1)^{|a|} = (-1)^{|a|-1} = alternating-by-weight
    alt = np.array(altweight_signs(n), float)
    assert np.allclose(eps_mu, alt), "eps_a=-chi_a(s*) != alternating-by-weight at n=%d" % n
    # T = 1 - N*delta_{s*}: value -(N-1) at s*, +1 elsewhere
    T_mu = chi0 @ eps_mu
    sidx_star = st.index(s_star)
    one_minus_Ndelta = np.ones(N); one_minus_Ndelta[sidx_star] = 1 - N
    assert np.allclose(T_mu, one_minus_Ndelta), "T != 1 - N*delta_{s*} at n=%d" % n
    mult_mu = tuple(sorted(int(round(t)) for t in T_mu))
    expected_mult = tuple(sorted([-(N - 1)] + [1] * (N - 1)))
    assert mult_mu == expected_mult
    print("  n=%d: T_eps = W'@eps OK; WH-coeffs of T_eps = (0, eps) with all nonzero-freq = +-1 OK;" % n)
    print("        eps_a = -chi_a(s*) (s*=all-minus) = (-1)^{|a|-1} = alternating OK;")
    print("        T = 1 - N*delta_{s*}  => mu* = {-(N-1) x1, +1 x(N-1)} OK.")
print("  WALSH FRAMING CONFIRMED (n=2,3, all assertions pass).")


# ============================================================================
# (4) COMPUTE D_1D(mu*) for n=2..8 at dps>=120.
# ============================================================================
print()
print("=" * 88)
print("(4) D_1D(mu*) for n=2..8  (dps = %d)" % mp.mp.dps)
print("=" * 88)
d1d_mu = {}
print("   n    D_1D(mu*) = m_hat_min(n)                                       closed=-ln(1-2^-n)   delta_n        D*2^n")
for n in range(2, 9):
    N = 1 << n
    D, h = D1D_perMode([-(N - 1), 1], [1, N - 1], n)
    Dchk, closed, hchk = exact_min(n)
    delta = closed - D
    d1d_mu[n] = D
    print("  %2d  %s  %s  %s  %s"
          % (n, mp.nstr(D, 48), mp.nstr(closed, 20), mp.nstr(delta, 6), mp.nstr(D * N, 14)))


# ============================================================================
# (5) NECESSARY conditions for achievability + higher-moment / spectral constraints.
# ============================================================================
print()
print("=" * 88)
print("(5) NECESSARY achievability conditions + higher-moment / spectral constraints")
print("=" * 88)
# Classical (proven, sympy-exact in pD):
#   (N1) sum_s T(s) = 0                         (zero mean; a=0 WH coeff = 0)
#   (N2) sum_s T(s)^2 = N(N-1)                  (2nd moment; Parseval with M unit coeffs)
#   (N3) each T(s) odd integer in [-(N-1), N-1] (sum of M=N-1 values +-1)
# Derive higher moments / spectral constraints from the +-1-Walsh-coefficient structure.

# Parseval (general): for f with WH coeffs f_hat(a), (1/N) sum_s f(s)^2 = sum_a f_hat(a)^2.
# T has f_hat(0)=0, f_hat(a)=eps_a=+-1 for a!=0 -> sum_a f_hat^2 = M -> sum_s T^2 = N*M = N(N-1). (N2)
#
# 3rd moment / general moments: sum_s T(s)^k = sum over a_1..a_k of (prod eps) * sum_s prod chi_{a_j}.
# sum_s prod_j chi_{a_j}(s) = N * 1[ a_1 XOR ... XOR a_k = 0 ] (characters: product is chi_{XOR}, sums
# to N iff the XOR is the trivial mask 0).  So
#   sum_s T^k = N * sum_{a_1..a_k != 0, XOR=0} eps_{a_1}...eps_{a_k}.
# This is a HARD constraint linking the multiset's moments to sign-coherent XOR-closed k-tuples.
#
# (N4) 3rd moment:  sum_s T^3 = N * sum_{a,b,c != 0, a XOR b XOR c = 0} eps_a eps_b eps_c.
#      The index set {(a,b,c): a^b^c=0, all !=0} = ordered "Steiner triples" of (Z2)^n\{0}; for each
#      unordered {a,b,c=a^b} there are 3! = 6 orderings (a,b,c distinct) -> the sum is
#      6 * sum_{triangles} eps_a eps_b eps_{a^b}  + (degenerate a=b => c=0 excluded since c!=0).
#      So sum_s T^3 / N is 6 times a signed triangle count; this is a PARITY/divisibility +
#      sign-coherence constraint, NOT free.  (Demonstrated numerically below.)
#
# (N5) 4th moment: sum_s T^4 = N * #{(a,b,c,d)!=0 : a^b^c^d=0} weighted by eps_a eps_b eps_c eps_d.
#      The UNSIGNED count of such 4-tuples is a fixed number (independent of eps); the signed version
#      is constrained.  For ANY eps the diagonal pairings (a=b,c=d), (a=c,b=d), (a=d,b=c) contribute
#      eps^2 eps^2 = +1 each: 3*M^2 minus overcounting of all-equal.  So sum_s T^4 has a FIXED
#      "Gaussian" part 3 M^2 N + lower order, plus a signed genuinely-4-wise XOR=0 part.
#
# SPECTRAL / RANK constraint (the structural lever):
#   (N6) The value vector T (length N) lies in the image of W' (rank M = N-1); equivalently T has
#        ZERO mean AND, written in the WH basis, has all nonzero-frequency coefficients of modulus 1.
#        => the multiset is the value-histogram of a function on (Z2)^n whose nonzero WH spectrum is a
#        SIGN VECTOR.  This is STRICTLY stronger than (N1)+(N2)+(N3): a multiset can satisfy the three
#        moment/parity conditions yet NOT be the histogram of any +-1-spectrum function (no eps yields
#        it).  Achievability = existence of eps in {+-1}^M with hist(W' eps) = the multiset, modulo the
#        spin-flip orbit action s->g*s (which permutes states, fixing the multiset) and eps-sign WH gauge.
#
# We DEMONSTRATE numerically that (N1)-(N3) are necessary-but-not-sufficient by exhibiting an
# integer multiset satisfying (N1),(N2),(N3) that is NOT achievable at n=3 (no eps realizes it),
# and we tabulate the exact achievable-multiset counts at n=2,3,4.

print("  PROVEN moment invariants (sympy-exact, pD checks A/B):")
print("    (N1) sum_s T = 0                       [zero mean = WH coeff at a=0 is 0]")
print("    (N2) sum_s T^2 = N(N-1)                [Parseval: M unit-modulus nonzero-freq coeffs]")
print("    (N3) each T(s) odd integer in [-(N-1), N-1], never 0   [sum of M=N-1 signs +-1]")
print()

# moment-XOR identity check: sum_s T^k = N * sum_{XOR=0, all nonzero} prod eps  (k=2,3,4), numerically.
def moment_check(n, k, eps):
    chi0, _ = char_cols(n)
    T = chi0 @ np.asarray(eps, float)
    lhs = np.sum(T ** k)
    N = 1 << n; M = N - 1
    # rhs = N * sum over k-tuples of nonzero masks with XOR 0 of product of eps
    masks = list(range(1, N))
    epsd = {masks[i]: eps[i] for i in range(M)}
    rhs = 0
    for tup in itertools.product(masks, repeat=k):
        x = 0
        for m_ in tup:
            x ^= m_
        if x == 0:
            pr = 1
            for m_ in tup:
                pr *= epsd[m_]
            rhs += pr
    rhs *= N
    return lhs, rhs

print("  Higher-moment XOR identity  sum_s T^k = N * sum_{a_1^...^a_k=0, all!=0} eps_{a_1}..eps_{a_k}:")
xor_ok = True
for n in [2, 3]:
    M = (1 << n) - 1
    rng5 = np.random.default_rng(n * 17)
    eps = list(rng5.integers(0, 2, M) * 2 - 1)
    for k in [2, 3, 4]:
        lhs, rhs = moment_check(n, k, eps)
        ok = abs(lhs - rhs) < 1e-6
        xor_ok = xor_ok and ok
        if k == 3:
            print("    n=%d k=%d : sum_s T^3 = %d = N * (signed triangle count) [a^b^c=0] : %s"
                  % (n, k, int(round(lhs)), ok))
print("    XOR-moment identity verified k=2,3,4, n=2,3:", xor_ok)
print()

# achievable-multiset counts at n=2,3,4 (the EXACT set realized by some eps), and a
# (N1)-(N3)-satisfying NON-achievable example at n=3.
print("  Achievable-multiset structure (exact enumeration over all eps):")
ach_counts = {}
for n in [2, 3, 4]:
    chi0, _ = char_cols(n)
    M = (1 << n) - 1
    ach = set()
    for bits in itertools.product((-1, 1), repeat=M):
        T = chi0 @ np.asarray(bits, float)
        ach.add(tuple(sorted(int(round(t)) for t in T)))
    ach_counts[n] = ach
    print("    n=%d : %d distinct ACHIEVABLE T-multisets (all eps); mu* present: %s"
          % (n, len(ach),
             tuple(sorted([-((1 << n) - 1)] + [1] * ((1 << n) - 1))) in ach))

# Now a multiset satisfying (N1)-(N3) that is NOT achievable at n=3 (necessary != sufficient):
# n=3: N=8, M=7, support odd ints in [-7,7], sum=0, sum^2=56.  Enumerate candidate integer
# multisets of size 8 with odd entries, mean 0, 2nd moment 56; flag which are achievable.
def candidate_multisets(n):
    N = 1 << n; M = N - 1
    odds = list(range(-(N - 1), N, 2))  # odd ints in [-(N-1), N-1]
    out = []
    for combo in itertools.combinations_with_replacement(odds, N):
        if sum(combo) == 0 and sum(x * x for x in combo) == N * M:
            out.append(tuple(sorted(combo)))
    return out

cand3 = candidate_multisets(3)
ach3 = ach_counts[3]
non_ach3 = [c for c in cand3 if c not in ach3]
print("    n=3 : %d integer multisets satisfy (N1)+(N2)+(N3); %d of them ACHIEVABLE, %d NOT achievable."
      % (len(cand3), len(cand3) - len(non_ach3), len(non_ach3)))
if non_ach3:
    print("          example satisfying (N1)-(N3) but NOT achievable (no eps realizes it): %s"
          % str(non_ach3[0]))
print("    => (N1)+(N2)+(N3) are NECESSARY but NOT SUFFICIENT; achievability = (N6) spectral:")
print("       exists eps in {+-1}^M with histogram(W'@eps) = the multiset (the +-1-WH-spectrum image).")
print()
print("  SUMMARY of NECESSARY conditions for an achievable T-multiset:")
print("    (N1) sum = 0                                  [proven, sympy-exact]")
print("    (N2) sum of squares = N(N-1)                  [proven, sympy-exact]")
print("    (N3) all entries odd, in [-(N-1), N-1]        [proven, sympy-exact]")
print("    (N4) sum T^3 = N * (6 * signed-triangle count over (Z2)^n)   [XOR-moment, eps-constrained]")
print("    (N5) sum T^4 = N * (3M^2 'Gaussian' + signed genuine-4-XOR part)   [XOR-moment]")
print("    (N6) SPECTRAL/RANK: T in image of W' with all nonzero-freq WH coeffs of modulus 1")
print("         (= the histogram of a function on (Z2)^n whose nonzero WH spectrum is a SIGN vector);")
print("         strictly stronger than (N1)-(N3); THE actual achievability condition.")
print("=" * 88)
print("SETUP EXTRACTION COMPLETE.")
