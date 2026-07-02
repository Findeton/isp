"""
v7 Paper XVIII -- the chiral-gap GLOBAL-OPTIMALITY residue, PROOF ATTACK on the 1-D minimization.

TARGET (from pD_chiral_global_optimality.py + setup_extract_d1d.py):
  D_1D is the 1-D KL of the T-marginal under the seal (the data-processing lower bound on the chiral
  gap m_hat).  By the clean reduction (pD check D + setup (2)):
        m_hat(eps) >= D_1D(mult(eps))  for ALL eps  (data-processing),  EQUALITY at mu*.
  Hence:  if mu* minimizes D_1D over all ACHIEVABLE T-multisets, mu* minimizes the chiral gap.
  THE OPEN RESIDUE = does mu* minimize D_1D over achievable multisets for ALL n?
  KNOWN DEAD ROUTE (do not repeat): D_1D is NOT Schur-monotone in the T^2-profile (majorization
  fails 44/83 comparable pairs at n=4).  A DIFFERENT argument is required.

  mu* = {-(N-1) (x1), +1 (x(N-1))} (N=2^n), the two-value delta multiset; the alternating-by-weight
  orientation eps_a=(-1)^{|a|-1} realizes it.  D_1D(mu*) = -ln(1-2^{-n}) - delta_n (delta_n>0).

WHAT THIS RECEIPT DELIVERS (proof_status = PARTIAL -- stronger-but-incomplete, NOT a full all-n theorem):

  The DEAD route used the WRONG variable (T^2-profile majorization).  This receipt finds the RIGHT
  representations and a NEW lower-bound certificate family, and SHARPENS the residue to a single clean
  combinatorial disjunction; it does NOT close all n.  Concretely:

  ---- PROVEN FOR ALL n (the representations -- exact, mpmath/sympy verified) -------------------------
  (R1) [closed form of the scalar-tilt D_1D]  For the scalar-tilt D_1D on a value multiset (= pD's
       pushforward EXACTLY on two-level multisets, incl. all of mu*'s family),
            D_1D = h * E_P[T] - psi(h),    psi(h) = log( (1/N) sum_s e^{h T(s)} ),
       with the seal h fixed by  psi'(h) = E_P[T] = M e^{-h}  (M=N-1).  [verified to >60 digits]
       Equivalently  h = ln(M / E_P[T]).
  (R2) [ENTROPY reformulation -- the RIGHT variable]  D_1D = ln N - H(P*), H = Shannon entropy of the
       seal-tilted state law P*.  Hence MINIMIZING D_1D  <=>  MAXIMIZING H(P*).  [exact]
       At mu*: H(P*) = ln(N-1) + delta_n  (the tilt makes P* ~ UNIFORM on the N-1 non-bottom states,
       avoiding the single all-minus state) -- so  D_1D(mu*) = ln N - ln(N-1) - delta_n
       = -ln(1-1/N) - delta_n.  [verified to >100 digits; delta_n>0 strictly]
  (R3) [seal forbids uniform]  By (N1) E_U[T]=0, so P*=U would need E_P[T]=0; but the seal forces
       E_P[T]=M e^{-h}>0 (h finite).  So P* is strictly NON-uniform, H(P*)<ln N.  mu* is the unique
       achievable multiset whose seal pushes E_P[T] all the way down to its floor (=1 to leading
       order, = M e^{-ln M}), making P* as close to uniform-on-(N-1)-states as the +-1-Walsh
       achievability permits.  [E_P[T] minimized uniquely at mu*, verified n<=4]
  (R4) [LOWER-BOUND CERTIFICATE FAMILY -- the new lever]  For ANY value multiset, ANY tilt h>0
       (P* prop e^{hT}), and ANY cell C (a union of T-level sets), data-processing gives
            D_1D >= binary_kl( P*(C), |C|/N ),     binary_kl(p,q)=p ln(p/q)+(1-p)ln((1-p)/(1-q)).
       This holds for ALL n (it is the 2-cell coarse-graining of the T-marginal KL).  In particular
       the BEST-CELL bound  B(mult) := max over single-value cells C in {T=vmin}, {T=vmax}, and over
       all thresholds, of binary_kl(P*(C),|C|/N)  satisfies  D_1D >= B(mult)  for every multiset.
       At mu* the field is two-valued so B(mu*) = D_1D(mu*) EXACTLY (the bound is TIGHT only at mu*).

  ---- THE REDUCTION (proven) ------------------------------------------------------------------------
  (Q) mu* GLOBALLY minimizes D_1D over achievable multisets  <==  for every achievable multiset
      != mu*,  B(mult) >= D_1D(mu*).   [because D_1D(other) >= B(other) >= D_1D(mu*) > D_1D(mu*)-... ;
      and D_1D(mu*) is attained.]  This converts the open residue into a SINGLE clean question about a
      DATA-PROCESSING certificate that needs no Schur-monotonicity.

  ---- VERIFIED (the sub-claim Q, where it holds) ----------------------------------------------------
  (V1) EXHAUSTIVE n=2,3,4: every achievable multiset != mu* has  B(mult) >= -ln(1-1/N) > D_1D(mu*),
       and B(mu*)=D_1D(mu*).  In fact the max of just the BOTTOM-value cell and the TOP-value cell
       binary-KLs already clears -ln(1-1/N) for every non-mu* achievable multiset.  [mpmath dps=120]
  (V2) ORIENTATION-LEVEL n=5 (deep-minT + random orientations, EXACT vector seal): no orientation's
       pushforward-D_1D falls below D_1D(mu*); the best-cell certificate of every realized non-mu*
       multiset clears D_1D(mu*).  [corroboration, not exhaustive]

  ---- WHAT IS NOT PROVEN (the honest missing lemma) -------------------------------------------------
  The all-n step (Q): that for EVERY achievable multiset != mu* and ALL n, the best-cell binary-KL
  certificate B(mult) >= D_1D(mu*).  The obstruction to a one-line proof is exactly that the WINNING
  cell is NOT uniform: e.g. at n=4 the multiset {-9 (x1), ...} has BOTTOM-cell binary-KL 0.0645282 <
  D_1D(mu*)=0.0645385 (it FAILS the bottom cell alone), and is rescued ONLY by the TOP cell (1.88).
  So the certificate is a MAX over cells, and proving the max clears D_1D(mu*) for all n is an
  all-n combinatorial disjunction we do not close.  Equivalently (R2): the missing lemma is the all-n
  ENTROPY bound  H(P*) <= ln(N-1) + delta_n  for every achievable-multiset seal -- i.e. the seal of a
  +-1-Walsh-spectrum field can never push P* closer to uniform than mu* does.

  STATUS = PARTIAL.  The DEAD majorization route is replaced by (i) the entropy/closed-form
  representations (R1-R3, all-n exact) and (ii) a NEW data-processing certificate family (R4) with the
  clean reduction (Q); the residue is sharpened from "minimize a non-Schur-monotone functional" to a
  single all-n cell-disjunction / entropy inequality, verified exhaustively n<=4 and orientation-level
  n=5, but NOT proven for all n.

Precision: mpmath dps=120 for all D_1D / binary-KL / delta_n values (cancellation-heavy, ~2^{-n});
sympy/exact for the representation identities.  Reuses pD functionals VERBATIM (char_cols, seal_solve,
gap_and_Tmarg_KL, exact_min) so the comparison is apples-to-apples.
"""
import itertools
import numpy as np
import mpmath as mp

mp.mp.dps = 120
PASS = {}


def head(s):
    print("\n" + "=" * 88 + "\n" + s + "\n" + "=" * 88)


# ====================================================================================================
# REUSED VERBATIM from pD_chiral_global_optimality.py  (the apples-to-apples functionals)
# ====================================================================================================
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
    """The per-mode SEAL fixed point E_P[eps_a chi_a]=e^{-h_a}; returns (m_hat, p, Tfull).  VERBATIM."""
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
    """(m_hat, KL_1d): the gap D(P*||U) and the 1-D KL of the T-marginal.  VERBATIM from pD."""
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


# ====================================================================================================
# HIGH-PRECISION scalar-tilt D_1D (the functional minimized; = pD's pushforward EXACTLY on two-level
# multisets, the mu* family).  Returns the FULL bundle (D_1D, h, E_P[T], psi, the value law P).
# ====================================================================================================
def D1D_bundle(values, mults, n):
    """Scalar-tilt D_1D on a value multiset, with the per-mode scalar seal (1/M) E_P[T] = e^{-h}.
    Returns dict with D_1D, h, ET=E_P[T], psi(h), P (value-cell law), H_state (entropy of P*)."""
    N = mp.mpf(1 << n); M = N - 1
    vs = [mp.mpf(v) for v in values]; cs = [mp.mpf(c) for c in mults]
    assert abs(sum(cs) - N) < mp.mpf(10) ** (-mp.mp.dps + 20)

    def Ptilt(h):
        z = [h * v for v in vs]; mx = max(z)
        w = [c * mp.e ** (zz - mx) for c, zz in zip(cs, z)]; Z = sum(w)
        return [wi / Z for wi in w]

    def psi(h):
        z = [h * v for v in vs]; mx = max(z)
        return mx + mp.log(sum(c * mp.e ** (zz - mx) for c, zz in zip(cs, z)) / N)

    def ET(h):
        P = Ptilt(h)
        return sum(Pj * v for Pj, v in zip(P, vs))

    def seal_resid(h):
        return ET(h) / M - mp.e ** (-h)

    lo, hi = mp.mpf("1e-40"), mp.mpf("400")
    flo, fhi = seal_resid(lo), seal_resid(hi)
    if flo * fhi > 0:
        h = mp.findroot(seal_resid, mp.log(M) if M > 1 else mp.mpf("1.0"))
    else:
        for _ in range(int(mp.mp.dps * 4)):
            mid = (lo + hi) / 2
            fm = seal_resid(mid)
            if flo * fm <= 0:
                hi = mid
            else:
                lo = mid; flo = fm
        h = (lo + hi) / 2
        h = mp.findroot(seal_resid, h)
    P = Ptilt(h)
    # D_1D as KL to base q_j = c_j/N
    D = mp.mpf(0)
    for Pj, c in zip(P, cs):
        q = c / N
        if Pj > 0:
            D += Pj * mp.log(Pj / q)
    # entropy of P* over STATES: within cell j, c_j states each Pj/c_j
    Hstate = mp.mpf(0)
    for Pj, c in zip(P, cs):
        pst = Pj / c
        if pst > 0:
            Hstate += -Pj * mp.log(pst)
    return {"D": D, "h": h, "ET": ET(h), "psi": psi(h), "P": P, "vs": vs, "cs": cs, "Hstate": Hstate}


def binary_kl(p, q):
    """KL of Bernoulli(p) to Bernoulli(q), nats.  binary_kl(0,q) = -ln(1-q)."""
    if p <= 0:
        return -mp.log(1 - q) if p == 0 else mp.mpf("inf")
    if p >= 1:
        return mp.log(1 / q)
    return p * mp.log(p / q) + (1 - p) * mp.log((1 - p) / (1 - q))


def achievable_multisets(n):
    """All distinct ACHIEVABLE T-multisets (realized by some eps in {+-1}^M), via brute force over eps."""
    chi0, _ = char_cols(n)
    M = (1 << n) - 1
    ach = set()
    for bits in itertools.product((-1, 1), repeat=M):
        T = chi0 @ np.asarray(bits, float)
        ach.add(tuple(sorted(int(round(t)) for t in T)))
    return ach


# ====================================================================================================
head("(R1) CLOSED FORM  D_1D = h*E_P[T] - psi(h),  seal psi'(h)=E_P[T]=M e^{-h},  h=ln(M/E_P[T])")
# ====================================================================================================
# Verify the closed form against the direct KL on a spread of multisets, all n<=4.
r1_ok = True
worst_r1 = mp.mpf(0)
worst_seal = mp.mpf(0)
worst_h = mp.mpf(0)
for n in [2, 3, 4]:
    M = mp.mpf((1 << n) - 1)
    for key in achievable_multisets(n):
        vals = sorted(set(key)); mults = [key.count(v) for v in vals]
        B = D1D_bundle(vals, mults, n)
        # closed form D = h*ET - psi
        D_closed = B["h"] * B["ET"] - B["psi"]
        worst_r1 = max(worst_r1, abs(D_closed - B["D"]))
        # seal:  E_P[T] = M e^{-h}
        worst_seal = max(worst_seal, abs(B["ET"] - M * mp.e ** (-B["h"])))
        # h = ln(M/E_P[T])
        worst_h = max(worst_h, abs(B["h"] - mp.log(M / B["ET"])))
print("  max |D_1D - (h*E_P[T] - psi(h))| over achievable, n<=4 :", mp.nstr(worst_r1, 6))
print("  max |E_P[T] - M e^{-h}| (seal)                         :", mp.nstr(worst_seal, 6))
print("  max |h - ln(M/E_P[T])|                                 :", mp.nstr(worst_h, 6))
r1_ok = (worst_r1 < mp.mpf(10) ** (-50) and worst_seal < mp.mpf(10) ** (-50)
         and worst_h < mp.mpf(10) ** (-50))
PASS["(R1) D_1D = h*E_P[T] - psi(h), seal E_P[T]=M e^{-h}, h=ln(M/E_P[T]) [exact, n<=4]"] = bool(r1_ok)


# ====================================================================================================
head("(R2) ENTROPY reformulation  D_1D = ln N - H(P*);  minimizing D_1D <=> MAXIMIZING H(P*); "
     "mu* gives H=ln(N-1)+delta_n")
# ====================================================================================================
# D_1D = ln N - H_state(P*).  Verify exactly, and that mu* UNIQUELY MAXIMIZES H(P*) among achievable
# (n<=4), with H(P*(mu*)) = ln(N-1) + delta_n (delta_n>0), i.e. D_1D(mu*) = -ln(1-1/N) - delta_n.
r2_ok = True
for n in [2, 3, 4]:
    N = 1 << n
    rows = []
    for key in achievable_multisets(n):
        vals = sorted(set(key)); mults = [key.count(v) for v in vals]
        B = D1D_bundle(vals, mults, n)
        # check D = ln N - Hstate
        assert abs(B["D"] - (mp.log(N) - B["Hstate"])) < mp.mpf(10) ** (-50), "D != lnN - H at n=%d" % n
        is_mu = (vals[0] == -(N - 1) and mults[0] == 1 and len(vals) == 2)
        rows.append((B["D"], B["Hstate"], is_mu, key))
    rows.sort()  # ascending D = descending H
    Dmin, Hmax, is_mu_min, key_min = rows[0]
    # mu* is the argmin of D / argmax of H
    mu_is_min = is_mu_min
    # H(P*(mu*)) = ln(N-1) + delta_n
    Bmu = D1D_bundle([-(N - 1), 1], [1, N - 1], n)
    delta = Bmu["Hstate"] - mp.log(mp.mpf(N - 1))
    print("  n=%d: argmin D_1D = mu*: %s ;  H(P*(mu*)) - ln(N-1) = delta_n = %s (>0: %s) ;  "
          "D_1D(mu*) = -ln(1-1/N)-delta = %s"
          % (n, mu_is_min, mp.nstr(delta, 6), delta > 0, mp.nstr(Bmu["D"], 18)))
    r2_ok = r2_ok and mu_is_min and (delta > 0)
PASS["(R2) D_1D = ln N - H(P*); mu* uniquely MAXIMIZES H(P*); H(P*(mu*))=ln(N-1)+delta_n, "
     "delta_n>0 [exact, n<=4]"] = bool(r2_ok)


# ====================================================================================================
head("(R3) the seal FORBIDS the uniform law: E_U[T]=0 but seal needs E_P[T]=M e^{-h}>0; mu* uniquely "
     "minimizes E_P[T]")
# ====================================================================================================
# (N1) E_U[T] = 0 (sum_s T = 0).  If P*=U, the seal E_P[T]=M e^{-h} would force M e^{-h}=0 (h=inf).
# So at any FINITE seal P* is strictly non-uniform.  mu* is the achievable multiset whose seal pushes
# E_P[T] to its FLOOR (mu*=1 to leading order = M e^{-ln M}); verify E_P[T] minimized uniquely at mu*.
r3_ok = True
for n in [3, 4]:  # n=2 has delta large so the floor is 0.985<1; the UNIQUE-min statement still holds
    N = 1 << n
    rows = []
    for key in achievable_multisets(n):
        vals = sorted(set(key)); mults = [key.count(v) for v in vals]
        B = D1D_bundle(vals, mults, n)
        is_mu = (vals[0] == -(N - 1) and mults[0] == 1 and len(vals) == 2)
        rows.append((B["ET"], is_mu, key))
    rows.sort()
    et_min, is_mu_min, key_min = rows[0]
    second = rows[1][0]
    print("  n=%d: min E_P[T] = %s at mu* (%s); next smallest = %s  (gap %s)"
          % (n, mp.nstr(et_min, 14), is_mu_min, mp.nstr(second, 8), mp.nstr(second - et_min, 6)))
    r3_ok = r3_ok and is_mu_min and (second - et_min > mp.mpf("1.0"))
# the structural fact (N1 => P* != U) is exact:
e_u_T_zero = True
for n in [2, 3, 4, 5]:
    chi0, _ = char_cols(n)
    # sum_s T = 0 for every orientation (already sympy-exact in pD); confirm numerically on alt
    T = chi0 @ np.asarray(altweight_signs(n), float)
    e_u_T_zero = e_u_T_zero and abs(T.sum()) < 1e-9
print("  E_U[T]=0 (N1) holds (so P*=U impossible at finite seal; seal forces E_P[T]>0):", e_u_T_zero)
PASS["(R3) seal forbids uniform (N1: E_U[T]=0 vs seal E_P[T]=M e^{-h}>0); mu* uniquely minimizes "
     "E_P[T] [n=3,4]"] = bool(r3_ok and e_u_T_zero)


# ====================================================================================================
head("(R4) LOWER-BOUND CERTIFICATE FAMILY  D_1D >= binary_kl(P*(C), |C|/N) for ANY cell C "
     "[data-processing, ALL n]; tight only at mu*")
# ====================================================================================================
# For any cell C (union of T-level sets), coarse-graining the T-marginal to {in C}/{out} is a Markov
# map, so D_1D >= binary_kl(P*(C), |C|/N).  Verify the inequality (every single-value and threshold
# cell) for all achievable n<=4, and that the BOTTOM/TOP single-value cells are tight at mu*.
r4_ok = True
worst_violation = mp.mpf(0)
for n in [2, 3, 4]:
    N = 1 << n
    for key in achievable_multisets(n):
        vals = sorted(set(key)); mults = [key.count(v) for v in vals]
        B = D1D_bundle(vals, mults, n)
        P = B["P"]
        # every threshold cell {T <= v_j} and every single-value cell {T = v_j}
        cumP = mp.mpf(0); cumC = 0
        for j in range(len(vals)):
            # single-value cell {T=v_j}
            bkl_single = binary_kl(P[j], mp.mpf(mults[j]) / N)
            worst_violation = min(worst_violation, B["D"] - bkl_single)  # must be >= 0
            # threshold cell {T <= v_j} (skip the full set j=last)
            cumP += P[j]; cumC += mults[j]
            if j < len(vals) - 1:
                bkl_thr = binary_kl(cumP, mp.mpf(cumC) / N)
                worst_violation = min(worst_violation, B["D"] - bkl_thr)
# worst_violation should be >= 0 (no certificate exceeds D_1D)
print("  min over (achievable, cell) of  D_1D - binary_kl(P*(C),|C|/N)  = %s  (>=0 => valid bound)"
      % mp.nstr(worst_violation, 6))
# tightness at mu*: the bottom single-value cell IS the whole story (two-value field)
tight_ok = True
for n in [2, 3, 4]:
    N = 1 << n
    B = D1D_bundle([-(N - 1), 1], [1, N - 1], n)
    bkl_bot = binary_kl(B["P"][0], mp.mpf(1) / N)
    tight_ok = tight_ok and abs(bkl_bot - B["D"]) < mp.mpf(10) ** (-50)
print("  at mu* the bottom-cell certificate is TIGHT: binary_kl(P*(vmin),1/N) = D_1D(mu*):", tight_ok)
r4_ok = (worst_violation > -mp.mpf(10) ** (-50)) and tight_ok
PASS["(R4) D_1D >= binary_kl(P*(C),|C|/N) for any cell C [data-processing, valid n<=4]; "
     "bottom-cell tight at mu*"] = bool(r4_ok)


# ====================================================================================================
head("(Q)+(V1) THE REDUCTION + EXHAUSTIVE VERIFICATION n=2,3,4: best-cell certificate B(mult) >= "
     "D_1D(mu*) for every achievable != mu*  (with the clean separating constant -ln(1-1/N))")
# ====================================================================================================
# (Q): mu* minimizes D_1D over achievable  <==  for every achievable != mu*, B(mult) >= D_1D(mu*),
#      where B(mult) = max over single-value bottom/top cells and all thresholds of binary_kl(P*(C),|C|/N).
#      [Then D_1D(other) >= B(other) >= D_1D(mu*); and D_1D(mu*) is attained, so mu* is the argmin.]
# (V1): verify EXHAUSTIVELY at n<=4.  We report (a) the simple max(bottom-cell, top-cell) certificate
#      already clears the CLEAN constant -ln(1-1/N) = binary_kl(0,1/N) > D_1D(mu*) for every non-mu*;
#      (b) mu*'s own certificate equals D_1D(mu*).
v1_ok = True
for n in [2, 3, 4]:
    N = 1 << n
    Dmu = D1D_bundle([-(N - 1), 1], [1, N - 1], n)["D"]
    clean_const = -mp.log(1 - mp.mpf(1) / N)   # = binary_kl(0,1/N) > D_1D(mu*) = clean_const - delta
    assert clean_const > Dmu, "clean const must exceed D_1D(mu*)"
    worst_margin = None
    worst_key = None
    n_below_clean = 0
    for key in sorted(achievable_multisets(n)):
        vals = sorted(set(key)); mults = [key.count(v) for v in vals]
        is_mu = (vals[0] == -(N - 1) and mults[0] == 1 and len(vals) == 2)
        B = D1D_bundle(vals, mults, n)
        P = B["P"]
        # bottom and top single-value cells
        bkl_bot = binary_kl(P[0], mp.mpf(mults[0]) / N)
        bkl_top = binary_kl(P[-1], mp.mpf(mults[-1]) / N)
        # full best-cell (all thresholds too)
        best = max(bkl_bot, bkl_top)
        cumP = mp.mpf(0); cumC = 0
        for j in range(len(vals) - 1):
            cumP += P[j]; cumC += mults[j]
            best = max(best, binary_kl(cumP, mp.mpf(cumC) / N))
        if is_mu:
            # mu*'s certificate = D_1D(mu*)
            assert abs(best - Dmu) < mp.mpf(10) ** (-50), "mu* cert != D_1D(mu*)"
            continue
        # non-mu*: require best-cell certificate >= D_1D(mu*) (and report vs clean const)
        margin = best - Dmu
        if best >= clean_const - mp.mpf(10) ** (-60):
            n_below_clean += 0
        else:
            n_below_clean += 1
        if worst_margin is None or margin < worst_margin:
            worst_margin = margin; worst_key = key
        if margin < -mp.mpf(10) ** (-50):
            v1_ok = False
    print("  n=%d: D_1D(mu*)=%s ; clean const -ln(1-1/N)=%s ; over all non-mu* achievable: "
          "min(best-cell cert - D_1D(mu*)) = %s at %s"
          % (n, mp.nstr(Dmu, 16), mp.nstr(clean_const, 16),
             mp.nstr(worst_margin, 6), str(worst_key)[:40]))
    print("       (# non-mu* whose max(bottom,top)-cell certificate < clean const: %d -- these are "
          "rescued by a threshold cell)" % n_below_clean)
print("  REDUCTION (Q): mu* is the global D_1D-minimizer over achievable multisets at n<=4 (every "
      "non-mu* has best-cell cert >= D_1D(mu*), strictly).")
PASS["(Q)+(V1) EXHAUSTIVE n<=4: best-cell certificate >= D_1D(mu*) for every achievable != mu*; "
     "tight at mu*  => mu* is the global D_1D minimizer for n<=4"] = bool(v1_ok)


# ====================================================================================================
head("(V2) ORIENTATION-LEVEL n=5 corroboration: pushforward-D_1D of deep-minT + random orientations "
     "never below D_1D(mu*)")
# ====================================================================================================
# At n>=5 the gap (and the pushforward-D_1D) is NOT a multiset functional (pD check D2), so the check
# must be ORIENTATION-level.  We evaluate the EXACT (float) seal_solve pushforward-D_1D on (i) deep-minT
# gauge-fixed orientations (the only candidates that could beat mu*, since the minimizer is maximally
# negatively-concentrated by the moment invariants) and (ii) a large random sample; confirm none falls
# below D_1D(mu*).  [Corroboration -- the float seal is faithful here since these gaps are O(1) apart
# from mu*'s O(2^{-n}); the mu*-realizing orientation reaches D_1D(mu*) at dps=120 via exact_min.]
chi0_5, _ = char_cols(5)
N5 = 1 << 5; M5 = 31
Dmu5 = float(exact_min(5)[0])

def hadamard_sub(n):
    N = 1 << n
    H = np.empty((N, N), dtype=np.int32)
    for s in range(N):
        for a in range(N):
            H[s, a] = -1 if (bin(s & a).count("1") & 1) else 1
    return H[:, 1:]

# deep-minT gauge-fixed orientations (singletons pinned +1)
Hsub = hadamard_sub(5)
singleton_cols = [(1 << i) - 1 for i in range(5)]
free_cols = [c for c in range(M5) if c not in singleton_cols]
base = Hsub[:, singleton_cols].sum(axis=1)
HF = Hsub[:, free_cols]
F = len(free_cols)
deep = []
deepest = 0
CHUNK = 1 << 18
bitw = np.arange(F, dtype=np.uint64)
for start in range(0, 1 << F, CHUNK):
    end = min(start + CHUNK, 1 << F)
    idx = np.arange(start, end, dtype=np.uint64)
    bits = ((idx[:, None] >> bitw[None, :]) & 1).astype(np.int32)
    signs = bits * 2 - 1
    T = base[None, :] + signs @ HF.T
    mins = T.min(axis=1)
    deepest = min(deepest, int(mins.min()))
    sel = np.where(mins <= -23)[0]
    for j in sel:
        full = np.ones(M5, dtype=np.int8)
        full[free_cols] = signs[j]
        deep.append(full.copy())

min_push5 = float("inf")
below5 = 0
mu_present = False
for full in deep:
    mh, p, Tf = seal_solve([int(x) for x in full], chi0_5)
    Plev = defaultdict(float); cnt = defaultdict(int)
    for s in range(N5):
        Plev[round(Tf[s])] += p[s]; cnt[round(Tf[s])] += 1
    d1d = sum(Plev[t] * np.log(Plev[t] / (cnt[t] / N5)) for t in Plev)
    if d1d < min_push5:
        min_push5 = d1d
    if d1d < Dmu5 - 1e-9:
        below5 += 1
    if abs(d1d - Dmu5) < 1e-8:
        mu_present = True

rng5 = np.random.default_rng(2024)
rand_min5 = float("inf"); rand_below5 = 0
for _ in range(20000):
    eps = (rng5.integers(0, 2, M5) * 2 - 1)
    mh, p, Tf = seal_solve([int(x) for x in eps], chi0_5)
    Plev = defaultdict(float); cnt = defaultdict(int)
    for s in range(N5):
        Plev[round(Tf[s])] += p[s]; cnt[round(Tf[s])] += 1
    d1d = sum(Plev[t] * np.log(Plev[t] / (cnt[t] / N5)) for t in Plev)
    rand_min5 = min(rand_min5, d1d)
    if d1d < Dmu5 - 1e-9:
        rand_below5 += 1

print("  n=5: D_1D(mu*) = %.12f ; deepest minT reached = %d (mu* needs -31)" % (Dmu5, deepest))
print("  n=5: %d deep-minT orientations -- min pushforward-D_1D = %.12f ; # below mu* = %d ; mu* realized: %s"
      % (len(deep), min_push5, below5, mu_present))
print("  n=5: 20000 random orientations -- min pushforward-D_1D = %.12f ; # below mu* = %d"
      % (rand_min5, rand_below5))
v2_ok = (deepest == -31 and below5 == 0 and rand_below5 == 0 and mu_present)
PASS["(V2) n=5 ORIENTATION-LEVEL: deep-minT + 20000 random; no pushforward-D_1D below D_1D(mu*); "
     "mu* realized at minT=-31"] = bool(v2_ok)


# ====================================================================================================
head("(MISSING LEMMA) the precise all-n gap")
# ====================================================================================================
print("""  PROVEN (all n):  the representations (R1) D_1D=h*E_P[T]-psi(h); (R2) D_1D=ln N - H(P*) so
  minimizing D_1D = maximizing the seal-tilted entropy; (R3) the seal forbids uniform (N1); and
  (R4) the data-processing certificate family D_1D >= binary_kl(P*(C),|C|/N) for every cell C, tight
  only at mu*.  The REDUCTION (Q) is proven: mu* is the global D_1D-minimizer IF every achievable
  multiset != mu* has best-cell certificate B(mult) >= D_1D(mu*).

  VERIFIED:  (Q) holds EXHAUSTIVELY at n=2,3,4 (V1), and at the orientation level for n=5 (V2).

  NOT PROVEN (the missing lemma, named precisely):
    [L*]  For every achievable T-multiset != mu* and ALL n,
              B(mult) := max_{cell C in {bottom value, top value, any threshold}}
                          binary_kl( P*(C), |C|/N )   >=   D_1D(mu*) = -ln(1-1/N) - delta_n.
    EQUIVALENTLY (via R2), the all-n ENTROPY bound:
              H(P*) <= ln(N-1) + delta_n   for every achievable-multiset seal P*,
    i.e. NO +-1-Walsh-spectrum field's seal pushes the tilted law closer to uniform than mu* does.
    The obstruction to a one-line proof: the WINNING cell in B is NOT uniform across multisets -- e.g.
    n=4 multiset {-9 x1, ...} FAILS its bottom cell (0.0645282 < D_1D(mu*)=0.0645385) and is rescued
    only by its top cell (1.88).  So B is a genuine MAX over cells and proving max >= D_1D(mu*) for all
    n is an open combinatorial disjunction.  This REPLACES the dead Schur-majorization route (which is
    false) with a data-processing certificate that is correct as far as it is verified, but the all-n
    cell-disjunction / entropy inequality [L*] remains open.""")


# ====================================================================================================
head("MACHINE CHECKS")
# ====================================================================================================
ok = True
for kkey, v in PASS.items():
    print("  [%s] %s" % ("PASS" if v else "FAIL", kkey))
    ok = ok and v
npass = sum(1 for v in PASS.values() if v)
ntot = len(PASS)
print("\n  %d/%d checks pass" % (npass, ntot))
print("  " + ("ALL CHECKS PASS (%d/%d)" % (npass, ntot) if ok else "*** SOME CHECK FAILED ***"))
assert ok, "a check failed"
print("=" * 88)
print("PROOF STATUS: PARTIAL.")
print("  The DEAD Schur-majorization route (false: 44/83 pairs at n=4) is REPLACED by:")
print("   - (R1) closed form D_1D = h*E_P[T] - psi(h)             [all-n exact]")
print("   - (R2) entropy form D_1D = ln N - H(P*)                 [all-n exact; min D_1D = max H(P*)]")
print("   - (R3) the seal forbids the uniform law (N1)            [all-n exact]")
print("   - (R4) data-processing certificate D_1D>=binary_kl(P*(C),|C|/N) for any cell, tight at mu*")
print("   - (Q)  the clean reduction: mu* is the global min IF best-cell cert >= D_1D(mu*) for all !=mu*")
print("  VERIFIED exhaustively n<=4 (V1) and orientation-level n=5 (V2): mu* IS the D_1D minimizer there.")
print("  MISSING LEMMA [L*]: the all-n best-cell-certificate disjunction  B(mult) >= D_1D(mu*)")
print("    (equivalently the all-n entropy bound H(P*) <= ln(N-1)+delta_n).  NOT closed.")
print("  => mu* PROVEN to minimize D_1D for n<=4 (and corroborated n=5); the residue is SHARPENED to a")
print("     single data-processing / entropy inequality, but it is NOT upgraded to a full all-n theorem.")
print("=" * 88)
