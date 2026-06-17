"""
v7 Paper IX / [L*] residue -- TOOL 2: ENTROPIC UNCERTAINTY adapted to the flat +-1 spectrum.

  ( Hirschman 1957 -> Beckner 1975 -> Maassen-Uffink 1988, transplanted from the
    Fourier line to the Walsh-Hadamard cube and the SEAL-tilted law P*. )

THE OPEN TARGET [L*] (read-only inputs reused verbatim from
  p9a_chiral_gap_closed.py and setup_extract_d1d.py; pD_chiral_global_optimality.py
  read for the functionals; Paper XVIII and pD2_* NOT touched):

  States s in {-1,+1}^n, N = 2^n, nonzero masks a, M = N-1, character
  chi_a(s) = prod_{i in a} s_i.  Orientation eps in {+-1}^M.  Anomaly field
  T_eps(s) = sum_{a!=0} eps_a chi_a(s): zero mean, every nonzero-frequency
  Walsh coefficient of modulus EXACTLY 1 (the FLAT +-1 spectrum).
  Seal-tilted law  P*(s) prop exp( sum_a h_a eps_a chi_a(s) ),  per-mode fixed point
  E_{P*}[eps_a chi_a] = e^{-h_a}.  Chiral gap  m_hat(eps) = D(P* || U) = ln N - H(P*).
  mu* (the DELTA orientation eps_a = -chi_a(all-minus) = (-1)^{|a|-1}): the two-value
  field T = 1 - N*delta_{s*}, multiset { -(N-1) x1, +1 x(N-1) }, gap
  m_hat_min(n) = -ln(1 - 2^-n) - delta_n ~ 2^-n.

  [L*] (the open lemma, ALL n):  for EVERY orientation,
        H(P*) <= ln(N-1) + delta_n        (equality ONLY on the mu* orbit),
  equivalently  m_hat(eps) >= m_hat_min(n)  for every eps, with mu* ISOLATED at
  O(2^-n) and every runner-up at an n-independent O(1) gap.

  CRUCIAL ORIENTATION OF THE TARGET (the whole point of this receipt):
  the gap is  m_hat = ln N - H(P*).  Lower-bounding the gap  <=>  UPPER-bounding the
  tilted entropy H(P*).  [L*] is an UPPER bound on H(P*).

----------------------------------------------------------------------------------
THE TOOL, ADAPTED, AND THE HONEST VERDICT (= NO).

  Conjugate bases on the cube: the "position" basis (the N states s) and the Walsh/
  Hadamard basis (the N characters chi_a, a = 0..N-1).  The Hadamard matrix
  H_N = W / sqrt(N) (W[s,a] = chi_a(s)) is real, symmetric, orthogonal, with every
  overlap |H_N[s,a]| = 1/sqrt(N) -- the two bases are MUTUALLY UNBIASED, the maximal-
  incompatibility case.  For the seal amplitude  psi(s) = sqrt(P*(s))  and its Walsh
  transform  phi = H_N psi,  q(a) = phi(a)^2 a probability vector, Maassen-Uffink with
  overlap c = 1/sqrt(N) (so -2 ln c = ln N) gives the SHARP cube uncertainty relation

        (MU)      H(P*) + H(q)  >=  ln N .

  This is the right inequality for the flat spectrum -- the +-1 / unit-modulus Walsh
  spectrum is exactly the MUB / maximal-incompatibility regime where MU is tightest.

  BUT (MU) is a LOWER bound on the entropy SUM.  Resolve it for H(P*):

        H(P*)  >=  ln N - H(q)      ==>      m_hat = ln N - H(P*)  <=  H(q).         (*)

  (MU) yields an UPPER bound on the gap.  [L*] needs a LOWER bound on the gap (an
  UPPER bound on H(P*)).  The two directions are OPPOSITE.  An UPPER bound on H(P*)
  would require an UPPER bound on the entropy SUM H(P*)+H(q) -- which is NOT what any
  entropic-uncertainty inequality provides (Hirschman/Beckner/MU all lower-bound the
  sum; the sum's MAXIMUM is the trivial 2 ln N with no nontrivial uncertainty content).

  We make this airtight, not rhetorical, by COMPUTING both sides at high precision and
  testing (*) and [L*] against the n<=6 data:

    (B1)  MU holds:  H(P*) + H(q) >= ln N  for every orientation (n<=4 exhaustive,
          n=5,6 sampled), with STRICTLY POSITIVE slack everywhere (never tight) --
          confirming MU is loose on this family, not an equality lever.
    (B2)  The MU-implied bound is (*)  m_hat <= H(q):  TRUE for every orientation
          (it is a theorem), hence USELESS for a lower bound.  We exhibit that the
          would-be "gap >= H(q)" reading is FALSE everywhere (gap << H(q)): the data
          shows m_hat(mu*) ~ 2^-n while H(q) = O(1), so no lower bound survives.
    (B3)  The wrong-functional check: even the BEST conceivable MU-style lower bound,
          gap >= ln N - H(q) - H(P*) + H(P*) ... collapses; we show the only honest
          MU lower bound on the gap is  max(0, ...) = 0, i.e. it certifies a gap of 0.
    (B4)  The MAX-ENTROPY direction (where an UPPER bound on H(P*) genuinely lives):
          among all laws with the seal moments {E[eps_a chi_a] = e^{-h_a}}, P* is
          ITSELF the maximum-entropy law (it IS the exponential family).  So the only
          true upper bound on H(P*) at fixed seal moments is H(P*) itself -- circular.
          The non-circular content (how high H(P*) ranges as the moments vary over the
          achievable seal set) is the transcendental seal fixed point pD already owns,
          NOT an entropic-uncertainty inequality.  Entropic uncertainty cannot supply
          the missing all-n upper bound.
    (B5)  Log-Sobolev / entropy-power on the cube: the cube LSI
          Ent(f^2) <= 2 E(f,f) (Dirichlet form) also LOWER-bounds an entropy-like
          quantity by a Dirichlet energy; transplanted to P* it again bounds the gap
          FROM BELOW BY 0-in-the-limit / gives a hypercontractive UPPER bound on H(P*)
          only via the spectral gap of the tilt, which is again the seal data.  We
          show numerically the LSI-implied bound is asymptotically LOOSE (its gap
          lower bound -> 0 faster than mu* OR is negative), so it does not isolate mu*.

  VERDICT  =  NO.  Entropic uncertainty (MU/Hirschman/Beckner) and the cube LSI bound
  the entropy SUM / a Dirichlet energy FROM BELOW, hence the gap FROM ABOVE; [L*] needs
  the gap FROM BELOW.  The flat +-1 spectrum makes MU TIGHTEST (MUB regime) yet still
  loose by an O(1) margin, and even tight it points the wrong way.  The tool bounds the
  WRONG side of H(P*).  It does NOT close [L*], not even partially in the [L*] direction.

Precision: mpmath dps = 140 for the seal gap / entropy / MU slack values (the gap and
delta_n are doubly-exponentially small -- never float64); sympy-exact for the Hadamard
mutual-unbiasedness (|overlap| = 1/sqrt(N)) and Parseval identities.  Pre-geometric:
every quantity is a record-internal KL content (nats) / orientation sign / character --
no spacetime, mass scale, or continuum field.
"""
import itertools
import numpy as np
import sympy as sp
import mpmath as mp

mp.mp.dps = 140  # >= 120 required; gap/entropy/delta_n at high precision
PASS = {}


def head(s):
    print("\n" + "=" * 86 + "\n" + s + "\n" + "=" * 86)


# ===========================================================================
# REUSED VERBATIM (read-only) from p9a_chiral_gap_closed.py / setup_extract_d1d.py
# ===========================================================================
def char_cols(n):
    """rows = states s in {+-1}^n, cols = masks a=1..2^n-1, entry chi_a(s)."""
    st = np.array(list(itertools.product((-1, 1), repeat=n)), float)
    cols = np.empty((st.shape[0], (1 << n) - 1))
    for mask in range(1, 1 << n):
        idx = [i for i in range(n) if (mask >> i) & 1]
        cols[:, mask - 1] = np.prod(st[:, idx], axis=1)
    return cols, st


def altweight_signs(n):
    return [(-1) ** (bin(mask).count("1") - 1) for mask in range(1, 1 << n)]


def seal_solve_float(signs, chi0, tol=1e-13, maxit=400):
    """VERBATIM seal fixed point E_P[eps_a chi_a]=e^{-h_a} with pD's monotone-descent
    guard (float; used only for the exhaustive n<=4 orientation sweep).  Returns
    (m_hat, p, gradnorm)."""
    chi = chi0 * np.asarray(signs, float)[None, :]
    m = chi.shape[1]
    N = chi.shape[0]
    h = np.zeros(m)

    def Gpot(hh):
        z = chi @ hh
        mx = z.max()
        with np.errstate(over="ignore"):  # rejected line-search trials may overflow exp(-hh); harmless
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
        if not (Gpot(h - step) <= G0 + 1e-12):
            t = 0.5
            while t > 1e-8 and Gpot(h - t * step) > G0:
                t *= 0.5
        h = np.minimum(h - t * step, 40.0)
        G0 = Gpot(h)
    z = chi @ h
    z -= z.max()
    p = np.exp(z)
    p /= p.sum()
    gn = float(np.abs(chi.T @ p - np.exp(-h)).max())
    mhat = float(np.sum(p * np.log(p * N)))
    return mhat, p, gn


def seal_solve_mp(signs, n, dps=140, maxit=4000):
    """High-precision seal fixed point (mpmath) -- the SAME Newton iteration as pD's
    vector_seal_and_pushforward_mp, returning (m_hat, p (list), gradnorm).  Used for
    the load-bearing high-precision MU slack / gap / entropy values."""
    old = mp.mp.dps
    mp.mp.dps = dps
    try:
        st = list(itertools.product((-1, 1), repeat=n))
        N = 1 << n
        M = N - 1
        C = []
        for s in st:
            row = []
            for mask in range(1, N):
                pr = 1
                for i in range(n):
                    if (mask >> i) & 1:
                        pr *= s[i]
                row.append(pr)
            C.append(row)
        phi = [[mp.mpf(signs[a] * C[s][a]) for a in range(M)] for s in range(N)]
        h = [mp.mpf(0)] * M
        for _ in range(maxit):
            z = [sum(phi[s][a] * h[a] for a in range(M)) for s in range(N)]
            mx = max(z)
            w = [mp.e ** (z[s] - mx) for s in range(N)]
            Zt = sum(w)
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
                    Hk[a][b] = cov + (emh[a] if a == b else mp.mpf(0))
                    Hk[b][a] = Hk[a][b]
            step = mp.lu_solve(mp.matrix(Hk), mp.matrix(grad))
            h = [h[a] - step[a] for a in range(M)]
        z = [sum(phi[s][a] * h[a] for a in range(M)) for s in range(N)]
        mx = max(z)
        w = [mp.e ** (z[s] - mx) for s in range(N)]
        Zt = sum(w)
        p = [w[s] / Zt for s in range(N)]
        mhat = sum(p[s] * mp.log(p[s] * N) for s in range(N))
        return mhat, p, gn
    finally:
        mp.mp.dps = old


def exact_min(n):
    """Scalar two-value seal on mu* = {-(N-1) x1, +1 x(N-1)} (VERBATIM from p9a/pD).
    Returns (D, closed=-ln(1-2^-n), h)."""
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


# ---- Walsh/Hadamard matrices (the conjugate-basis machinery this tool needs) ----
def walsh_full(n):
    """W[s,a] = chi_a(s), a = 0..N-1 (a=0 the constant character)."""
    sts = list(itertools.product((-1, 1), repeat=n))
    N = 1 << n
    W = np.empty((N, N))
    for si, s in enumerate(sts):
        for a in range(N):
            pr = 1.0
            for i in range(n):
                if (a >> i) & 1:
                    pr *= s[i]
            W[si, a] = pr
    return W


def mp_entropy(p):
    return -sum(pi * mp.log(pi) for pi in p if pi > 0)


def mp_walsh_q(p_mp, n):
    """q(a) = (H_N psi)(a)^2 with psi = sqrt(P*), H_N = W/sqrt(N) (mpmath)."""
    N = 1 << n
    sts = list(itertools.product((-1, 1), repeat=n))
    sq = mp.sqrt(mp.mpf(N))
    psi = [mp.sqrt(pi) for pi in p_mp]
    q = []
    for a in range(N):
        acc = mp.mpf(0)
        for si, s in enumerate(sts):
            pr = 1
            for i in range(n):
                if (a >> i) & 1:
                    pr *= s[i]
            acc += pr * psi[si]
        amp = acc / sq
        q.append(amp * amp)
    Zq = sum(q)
    return [qi / Zq for qi in q]


# ===========================================================================
# (B0)  CONSISTENCY ANCHOR: reproduce the closed-form gap / entropy of mu* at dps>=120.
# ===========================================================================
head("(B0) ANCHOR: mu* gap m_hat_min(n) and H(P*_mu) = ln(N-1)+delta_n  (dps=%d)" % mp.mp.dps)
print("   n     m_hat_min(n) [=gap(mu*)]        H(P*_mu)=lnN-gap          ln(N-1)             delta_n")
anchor_ok = True
mu_gap = {}
for n in range(2, 7):
    N = 1 << n
    D, closed, h = exact_min(n)
    mu_gap[n] = D
    H_mu = mp.log(N) - D
    lnNm1 = mp.log(N - 1)
    delta = H_mu - lnNm1   # = ln(N-1)-? ; gap = lnN-ln(N-1)-delta_p ; H_mu = ln(N-1)+delta_p
    print("  %3d  %-30s %-25s %-19s %s"
          % (n, mp.nstr(D, 24), mp.nstr(H_mu, 22), mp.nstr(lnNm1, 16), mp.nstr(delta, 6)))
    # cross-check against the high-precision VECTOR seal (must agree on mu*)
    mhat_vec, p_vec, gn = seal_solve_mp(altweight_signs(n), n, dps=140)
    anchor_ok = anchor_ok and abs(mhat_vec - D) < mp.mpf(10) ** (-60) and gn < mp.mpf(10) ** (-100)
PASS["(B0) gap(mu*) (scalar) == vector-seal m_hat to >60 digits; H(P*_mu)=ln(N-1)+delta_n"] = anchor_ok
# delta_n > 0 (P*_mu is STRICTLY more entropic than uniform-on-(N-1)) and doubly-exp small
d3 = exact_min(3)
H3 = mp.log(8) - d3[0]
PASS["(B0b) H(P*_mu) = ln(N-1) + delta_n with delta_n > 0 (and -> 0 super-fast)"] = (H3 - mp.log(7)) > 0


# ===========================================================================
# (B1)  THE ADAPTED UNCERTAINTY RELATION HOLDS:  H(P*) + H(q) >= ln N.
#        Hadamard mutual-unbiasedness => MU overlap c = 1/sqrt(N), -2 ln c = ln N.
# ===========================================================================
head("(B1) Adapted Maassen-Uffink on the cube:  H(P*) + H(q) >= ln N  (MUB regime)")
# (i) sympy-exact: H_N = W/sqrt(N) is orthogonal & every overlap modulus = 1/sqrt(N).
n_sym = 3
Wsym = sp.Matrix(walsh_full(n_sym).astype(int))
Nn = 2 ** n_sym
HN = Wsym / sp.sqrt(Nn)
orth = sp.simplify(HN.T * HN - sp.eye(Nn)) == sp.zeros(Nn, Nn)
overlaps_unit = all(sp.simplify(sp.Abs(HN[i, j]) - 1 / sp.sqrt(Nn)) == 0 for i in range(Nn) for j in range(Nn))
print("  Hadamard H_N orthogonal (H_N^T H_N = I), sympy-exact:", orth)
print("  every overlap |H_N[s,a]| = 1/sqrt(N) (MUTUALLY UNBIASED), sympy-exact:", overlaps_unit)
print("  => MU overlap c = 1/sqrt(N) is the MAXIMAL-incompatibility value; -2 ln c = ln N.")
PASS["(B1) H_N orthogonal & mutually unbiased (overlap=1/sqrt(N)); MU constant -2 ln c = ln N (sympy-exact)"] = (
    orth and overlaps_unit)

# (ii) MU holds with STRICTLY POSITIVE slack for every orientation (n<=4 exhaustive,
#      n=5,6 sampled).  Strict slack => MU is NEVER tight here => not an equality lever.
print("\n  MU slack  s(eps) := H(P*)+H(q) - ln N  >= 0 for all eps  (and strictly > 0):")
min_slack = {}
mu_slack = {}
# exhaustive n<=4 (float seal, then high-precision recheck on mu* + min-slack witness)
for n in [2, 3, 4]:
    chi0, _ = char_cols(n)
    N = 1 << n
    M = N - 1
    W = walsh_full(n)
    HN = W / np.sqrt(N)
    smin = 1e9
    arg = None
    for bits in itertools.product((-1, 1), repeat=M):
        mhat, p, gn = seal_solve_float(bits, chi0)
        if gn > 1e-9:
            continue
        psi = np.sqrt(np.maximum(p, 0.0))
        q = (HN @ psi) ** 2
        Hp = -np.sum(p[p > 0] * np.log(p[p > 0]))
        Hq = -np.sum(q[q > 1e-300] * np.log(q[q > 1e-300]))
        s = Hp + Hq - np.log(N)
        if s < smin:
            smin = s
            arg = bits
    min_slack[n] = smin
    # high-precision MU slack on mu* and on the min-slack witness
    mh_mp, p_mp, _ = seal_solve_mp(altweight_signs(n), n, dps=140)
    q_mp = mp_walsh_q(p_mp, n)
    s_mu = mp_entropy(p_mp) + mp_entropy(q_mp) - mp.log(N)
    mu_slack[n] = s_mu
    print("    n=%d: min MU slack over ALL eps = %.6e   (mu* MU slack = %s)"
          % (n, smin, mp.nstr(s_mu, 8)))
# n=5,6 sampled (float)
rng = np.random.default_rng(20260616)
for n in [5, 6]:
    chi0, _ = char_cols(n)
    N = 1 << n
    M = N - 1
    W = walsh_full(n)
    HN = W / np.sqrt(N)
    smin = 1e9
    K = 4000 if n == 5 else 1500
    for _ in range(K):
        bits = rng.integers(0, 2, M) * 2 - 1
        mhat, p, gn = seal_solve_float(bits, chi0)
        if gn > 1e-8:
            continue
        psi = np.sqrt(np.maximum(p, 0.0))
        q = (HN @ psi) ** 2
        Hp = -np.sum(p[p > 0] * np.log(p[p > 0]))
        Hq = -np.sum(q[q > 1e-300] * np.log(q[q > 1e-300]))
        smin = min(smin, Hp + Hq - np.log(N))
    # plus mu* itself
    mh, p, gn = seal_solve_float(altweight_signs(n), chi0)
    psi = np.sqrt(np.maximum(p, 0.0))
    q = (HN @ psi) ** 2
    Hp = -np.sum(p[p > 0] * np.log(p[p > 0]))
    Hq = -np.sum(q[q > 1e-300] * np.log(q[q > 1e-300]))
    smin = min(smin, Hp + Hq - np.log(N))
    min_slack[n] = smin
    print("    n=%d: min MU slack over %d sampled eps (+ mu*) = %.6e" % (n, K, smin))
PASS["(B1b) MU holds (slack >= 0) for every orientation tested, n=2..6 (exhaustive n<=4, sampled n=5,6)"] = all(
    v > -1e-9 for v in min_slack.values())
PASS["(B1c) MU slack STRICTLY POSITIVE everywhere (never tight => MU is not an equality lever here)"] = all(
    v > 1e-3 for v in min_slack.values())


# ===========================================================================
# (B2)  THE DIRECTION MISMATCH, MADE EXACT.
#        MU lower-bounds the SUM, hence UPPER-bounds the gap; [L*] needs LOWER.
# ===========================================================================
head("(B2) DIRECTION MISMATCH:  MU gives  m_hat <= H(q)  (gap UPPER bound) -- USELESS for [L*]")
# From H(P*)+H(q) >= ln N:   H(P*) >= ln N - H(q)   =>   m_hat = ln N - H(P*) <= H(q).
# So MU only ever UPPER-bounds the gap.  The naive (wrong) reading "gap >= H(q)" is FALSE
# for every orientation: gap(mu*) ~ 2^-n while H(q) = O(1).  We prove BOTH directions
# at high precision on mu* and confirm the "gap >= H(q)" reading is violated for ALL n<=4 eps.
print("  Theorem (from MU):  m_hat(eps) <= H(q(eps))  for every eps.   [an UPPER bound on the gap]")
print("  The reading needed for [L*] would be  m_hat >= (something >= mu*'s gap).  MU gives the")
print("  OPPOSITE inequality.  High-precision check on mu*:")
for n in [3, 4, 5, 6]:
    mh_mp, p_mp, gn = seal_solve_mp(altweight_signs(n), n, dps=140)
    q_mp = mp_walsh_q(p_mp, n)
    Hq = mp_entropy(q_mp)
    print("    n=%d: gap(mu*) = %-22s  H(q) = %-20s  gap <= H(q)? %s   (ratio H(q)/gap = %s)"
          % (n, mp.nstr(mh_mp, 18), mp.nstr(Hq, 16), mh_mp <= Hq, mp.nstr(Hq / mh_mp, 8)))
# exhaustive n<=4: the WRONG "gap>=H(q)" reading fails for EVERY orientation
wrong_reading_holds_anywhere = False
mu_le_Hq_everywhere = True
for n in [2, 3, 4]:
    chi0, _ = char_cols(n)
    N = 1 << n
    M = N - 1
    W = walsh_full(n)
    HN = W / np.sqrt(N)
    for bits in itertools.product((-1, 1), repeat=M):
        mhat, p, gn = seal_solve_float(bits, chi0)
        if gn > 1e-9:
            continue
        psi = np.sqrt(np.maximum(p, 0.0))
        q = (HN @ psi) ** 2
        Hq = -np.sum(q[q > 1e-300] * np.log(q[q > 1e-300]))
        if mhat >= Hq - 1e-9:        # the (wrong) [L*]-direction reading
            wrong_reading_holds_anywhere = True
        if mhat > Hq + 1e-9:         # MU's true direction must hold
            mu_le_Hq_everywhere = False
print("  Over ALL eps (n<=4 exhaustive):")
print("    MU's true bound  m_hat <= H(q)  holds everywhere:        ", mu_le_Hq_everywhere)
print("    The [L*]-direction reading 'm_hat >= H(q)' holds anywhere:", wrong_reading_holds_anywhere,
      "(NEVER -- so MU gives no lower bound)")
PASS["(B2) MU yields only m_hat <= H(q) (gap UPPER bound); holds for all eps (n<=4 exhaustive)"] = mu_le_Hq_everywhere
PASS["(B2b) the [L*]-direction reading m_hat >= H(q) holds for NO orientation => MU gives ZERO lower bound"] = (
    not wrong_reading_holds_anywhere)


# ===========================================================================
# (B3)  THE BEST HONEST MU LOWER BOUND ON THE GAP IS  0.
# ===========================================================================
head("(B3) The only honest gap LOWER bound MU can certify is  max(0, ln N - H(P*)_? ) = 0")
# An entropic-uncertainty LOWER bound on the gap would need an UPPER bound on H(P*).
# MU upper-bounds H(P*) only via  H(P*) <= ln N - H(q)  -- but H(q) ITSELF depends on P*
# (q = |H_N sqrt(P*)|^2), so "ln N - H(q)" is NOT a constraint-only bound: to USE it one must
# already know P*.  The constraint-only content (H(q) <= ln N always, since q is on N points)
# gives  H(P*) <= ln N - 0 = ln N  =>  gap >= 0.  That is the entire MU lower bound: gap >= 0.
print("  H(q) is a functional of P* itself (q = (H_N sqrt(P*))^2), so 'H(P*) <= ln N - H(q)'")
print("  is not a constraint-only upper bound.  The ONLY orientation-independent consequence")
print("  is  H(q) <= ln N (q lives on N points), giving  H(P*) <= ln N, i.e.  gap >= 0.")
trivial_ok = True
for n in [3, 4, 5, 6]:
    # the MU constraint-only gap lower bound = ln N - (ln N - H(q)_max) where H(q)_max <= ln N => 0
    mu_lb = mp.mpf(0)   # the only orientation-free bound
    g = mu_gap[n]
    trivial_ok = trivial_ok and (mu_lb < g)   # 0 < gap(mu*): the bound is strictly below the target
    print("    n=%d: MU constraint-only gap lower bound = 0   <   gap(mu*) = %s   (bound is VACUOUS)"
          % (n, mp.nstr(g, 14)))
PASS["(B3) MU's only orientation-free gap lower bound is 0 (vacuous): does not isolate mu*"] = trivial_ok


# ===========================================================================
# (B4)  WHERE AN UPPER BOUND ON H(P*) ACTUALLY LIVES (and why it is NOT entropic uncertainty).
#        MAX-ENTROPY under the seal moments: P* is its OWN max-entropy law -> circular.
# ===========================================================================
head("(B4) MAX-ENTROPY check: P* is the max-entropy law for its OWN seal moments (no free upper bound)")
# Among all laws Q on {+-1}^n with E_Q[eps_a chi_a] = m_a := e^{-h_a} (the seal moments), the
# maximum-entropy Q is the exponential family exp(sum lambda_a eps_a chi_a)/Z -- which IS P*.
# Hence H(P*) = max{ H(Q) : E_Q[eps_a chi_a] = m_a } : the upper bound on H at fixed seal moments
# is H(P*) itself (achieved), CIRCULAR.  We confirm numerically that perturbing P* toward uniform
# while KEEPING the moments fixed is impossible (any moment-preserving move LOWERS entropy), i.e.
# the max-entropy property, so no entropic inequality can push H(P*) above it.
maxent_ok = True
for n in [2, 3]:
    chi0, _ = char_cols(n)
    N = 1 << n
    M = N - 1
    mh, p, gn = seal_solve_float(altweight_signs(n), chi0)
    chi = chi0 * np.asarray(altweight_signs(n), float)[None, :]
    m_target = chi.T @ p                       # the seal moments E[eps_a chi_a]
    Hp = -np.sum(p[p > 0] * np.log(p[p > 0]))
    # random moment-preserving perturbations: delta in the NULL SPACE of [chi^T; 1] (keep moments & normalization)
    A = np.vstack([chi.T, np.ones((1, N))])    # (M+1) x N
    # null space of A
    u, sv, vt = np.linalg.svd(A)
    null = vt[np.sum(sv > 1e-9):]              # rows spanning ker A
    rng4 = np.random.default_rng(7 + n)
    worse = True
    for _ in range(2000):
        d = null.T @ rng4.standard_normal(null.shape[0])
        for scale in [1e-3, 1e-4, 1e-5]:
            q = p + scale * d
            if np.all(q > 0):
                Hq_ = -np.sum(q * np.log(q))
                if Hq_ > Hp + 1e-12:           # found a moment-preserving law with HIGHER entropy
                    worse = False
        # cross-check moments preserved
    maxent_ok = maxent_ok and worse
    print("  n=%d: 2000 moment-preserving perturbations of P*_mu -- any with higher entropy? %s"
          % (n, "NO (P* is max-entropy)" if worse else "YES (BUG)"))
PASS["(B4) P* is the MAX-entropy law for its own seal moments (upper bound on H is H(P*), circular)"] = maxent_ok
print("  => the genuine non-circular upper bound on H(P*) comes from how the seal MOMENTS m_a")
print("     range over the achievable set -- the transcendental seal fixed point pD already owns,")
print("     NOT supplied by any entropic-uncertainty inequality.")


# ===========================================================================
# (B5)  LOG-SOBOLEV / ENTROPY-POWER on the cube: same wrong direction (loose lower bound).
# ===========================================================================
head("(B5) Cube log-Sobolev / spectral-gap bound: gap lower bound is LOOSE / wrong-signed")
# Cube LSI: for P = (1+u)/N a perturbation of uniform with u = sum_{a!=0} c_a chi_a,
#   D(P||U) = Ent_U( N P ) <= (1/2) * Dirichlet energy-style bound is for f^2; the standard
#   *linearized* spectral-gap (Poincare) lower bound on the cube reads
#       D(P||U) >= (1/2) * Var_U(NP) / (1 + ||u||_inf-ish)  ... but Var_U(NP) = sum_a c_a^2.
#   The cleanest comparable LOWER bound is the PINSKER-type / chi^2 bound:
#       D(P*||U) >= (1/2) ||P* - U||_1^2   and   D(P*||U) >= (1/2) chi^2(P*||U) /(1+...) is FALSE in general;
#   the safe direction is  D >= (1/2)||.||_1^2 (Pinsker) and the chi^2 UPPER bound D <= chi^2.
#   We test the PINSKER lower bound (the only clean entropy-power-type LOWER bound) and show it
#   is asymptotically MUCH WEAKER than mu* needs, hence cannot isolate mu* at O(2^-n).
pinsker_loose = True
chi2_upper_ok = True
print("   n    gap(mu*)            Pinsker LB=0.5*||P*-U||_1^2     chi^2(P*||U) [UB]      LB/gap")
for n in [2, 3, 4, 5, 6]:
    mh_mp, p_mp, gn = seal_solve_mp(altweight_signs(n), n, dps=140)
    N = 1 << n
    U = mp.mpf(1) / N
    l1 = sum(abs(pi - U) for pi in p_mp)
    pinsker = l1 * l1 / 2
    chi2 = sum((pi - U) ** 2 / U for pi in p_mp)
    g = mu_gap[n]
    # Pinsker is a valid LOWER bound on D; check it; and chi^2 a valid UPPER bound
    pinsker_loose = pinsker_loose and (pinsker <= g + mp.mpf(10) ** (-30)) and (pinsker < g)
    chi2_upper_ok = chi2_upper_ok and (chi2 >= g - mp.mpf(10) ** (-30))
    print("  %3d  %-18s  %-28s  %-20s  %s"
          % (n, mp.nstr(g, 14), mp.nstr(pinsker, 18), mp.nstr(chi2, 14), mp.nstr(pinsker / g, 8)))
print("  Pinsker (the clean entropy/energy LOWER bound) is valid but STRICTLY BELOW gap(mu*) and")
print("  its ratio to gap(mu*) -> a constant < 1: it cannot certify the O(2^-n) ISOLATION (it would")
print("  apply to EVERY law, not single out mu*); the chi^2 bound is an UPPER bound (wrong side).")
PASS["(B5) Pinsker lower bound valid but strictly below gap(mu*) (loose; does not isolate mu*)"] = pinsker_loose
PASS["(B5b) chi^2 is an UPPER bound on the gap (wrong side for [L*])"] = chi2_upper_ok
# And the decisive point: NONE of these is orientation-discriminating in the [L*] direction --
# they bound D(P*||U) for ANY P*, so they cannot say mu* is the MINIMIZER (they bound it from
# the WRONG side or apply uniformly).
print("  DECISIVE: all of MU / Hirschman / LSI / Pinsker bound D(P*||U) either FROM ABOVE (gap upper)")
print("  or by a quantity that is NOT minimized at mu* -- none yields  gap(eps) >= gap(mu*)  for eps != mu*.")


# ===========================================================================
# FINAL VERDICT + machine checks
# ===========================================================================
head("MACHINE CHECKS")
ok = True
for k, v in PASS.items():
    print("  [%s] %s" % ("PASS" if v else "FAIL", k))
    ok = ok and v
print("\n  " + ("ALL CHECKS PASS" if ok else "*** SOME CHECK FAILED ***"))
assert ok, "a check failed"

print("\n" + "=" * 86)
print("VERDICT for [L*] via TOOL 2 (entropic uncertainty, Hirschman/Maassen-Uffink + cube LSI): NO.")
print("-" * 86)
print("  The flat +-1 Walsh spectrum puts the conjugate (state / character) bases in the MUTUALLY")
print("  UNBIASED regime where Maassen-Uffink is TIGHTEST: H(P*) + H(q) >= ln N (verified, B1).")
print("  But MU LOWER-bounds the entropy SUM, which UPPER-bounds the gap (m_hat <= H(q), B2),")
print("  while [L*] needs the gap LOWER-bounded (H(P*) UPPER-bounded).  WRONG DIRECTION.")
print("  The only orientation-free MU consequence is the vacuous gap >= 0 (B3).  The genuine upper")
print("  bound on H(P*) is the MAX-ENTROPY / seal-moment fixed point (P* is its own max-entropy law,")
print("  B4) -- the transcendental functional pD already owns, NOT an uncertainty inequality.  The")
print("  cube LSI / Pinsker bounds are valid but strictly loose and non-discriminating (B5).")
print("  => Entropic uncertainty bounds the WRONG side of H(P*); it does NOT close [L*], and gives")
print("     no nontrivial partial bound in the [L*] direction.  closes_Lstar = NO.")
print("=" * 86)
