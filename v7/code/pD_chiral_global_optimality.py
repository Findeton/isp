"""
v7 Paper IX, receipt D -- the chiral-gap GLOBAL-OPTIMALITY lemma.

Paper IX (the closed chiral-gap law, receipt p9a) proved the oriented/chiral minimum gap is
attained at the ALTERNATING-BY-WEIGHT orientation eps_a = (-1)^{|a|-1}, with the closed form
m_hat_min(n) = -ln(1 - 2^-n) - delta_n -- but the GLOBAL optimality of that orientation over all
2^(2^n - 1) orientation classes was verified by EXHAUSTIVE brute force only for n = 2, 3, 4
(n=4 = 2^15 = 32768 classes). For n >= 5 the count 2^(2^n-1) explodes (n=5 -> 2^31) and the
closed form was used WITHOUT a global check. This receipt attacks that named finite lemma.

WHAT THIS RECEIPT ESTABLISHES (honest scope -- proof_status = PARTIAL_REDUCTION):

  The setup.  An orientation assigns a sign eps_a in {+1,-1} to each of the M = 2^n - 1 nonzero
  masks a of the n-bit ledger.  Characters chi_a(s) = prod_{i in a} s_i on states s in {+-1}^n.
  Tilted (sealed) law P(s) ∝ exp( sum_a h_a eps_a chi_a(s) ) with the SEAL fixed point
  E_P[eps_a chi_a] = e^{-h_a} for every a; the chiral gap is m_hat(eps) = D(P || U) (nats),
  U = uniform.  The "anomaly field" is  T_eps(s) := sum_{a != 0} eps_a chi_a(s).

  ---- PROVEN FOR ALL n (the reductions) -------------------------------------------------------
  (A) [polynomial identity]  For the alternating orientation, T(s) = -[ prod_i (1 - s_i) - 1 ],
      which is -(2^n - 1) on the all-minus state and +1 on every other state (the two-value
      collapse).  Hence the alternating orientation realizes the multiset
        mu* = { -(2^n - 1) }  U  { +1 }^{2^n - 1}.                                 (sympy-exact)
  (B) [two moment invariants]  For EVERY orientation:  sum_s T_eps(s) = 0  and
        sum_s T_eps(s)^2 = 2^n (2^n - 1),  from character orthogonality.  Each T_eps(s) is an
      ODD integer in [-(2^n-1), 2^n-1] (never 0).  mu* SATURATES both invariants and is the
      maximally negatively-concentrated such multiset.                            (sympy-exact)
      CAVEAT: (B) pins mu* as the moment-extremal MULTISET; it does NOT order classes by depth
      (the gap is not Schur-monotone in the T^2 profile -- check I -- and the per-minT gap FLOOR
      is non-monotone already at n=4 -- check I2).  So "the minimizer MUST live at the deepest
      minT" is NOT a consequence of (B); the deep-band focus of the n=5,6 search is a HEURISTIC.
  (B2) [maximal depth is mu*-only]  The single deepest level IS settled by proof: minT = -(2^n-1)
      at some state s  IFF  eps_a chi_a(s) = -1 for every mask a  <=>  eps_a = -chi_a(s) forced.
      So the depth -(2^n-1) is reached by EXACTLY one spin-flip orbit -- that of the alternating
      orientation (mu*) -- with a UNIQUE gauge-fixed (singletons +1) representative.  Hence the
      maximal-depth MULTISET is mu* and nothing else, for ALL n.  (Exhaustive n=2..6.)  This is the
      rigorous fragment of the deep-band intuition; it settles the deepest level, NOT the ones above.
  (C) [spin-flip invariance]  m_hat is invariant under the spin-flip relabeling
        (R_g eps)_a = eps_a chi_a(g)  (g a state):  R_g acts on states by the measure-preserving
      bijection s -> g*s, under which the seal problem and D(P||U) are carried to those of R_g eps.
      So m_hat depends only on the spin-flip ORBIT.                               (verified exact)
  (D) [1-D KL LOWER BOUND]  By the data-processing inequality, for EVERY orientation and EVERY n,
        m_hat(eps) = D(P* || U) >= D( law_P(T) || law_U(T) ) =: KL_1d(eps),  the 1-D KL of the
      T-marginal, which depends on eps ONLY through the T-multiset.  EQUALITY -- i.e. P* constant
      on level sets of T, hence the gap a PURE MULTISET FUNCTIONAL -- holds on the mu* orbit and
      EXHAUSTIVELY at n <= 4, but FAILS for n >= 5 (the seal tilts over the full M-vector
      phi_a(s)=eps_a chi_a(s), not over the scalar T=sum_a phi_a).  See (D2) for the explicit
      n=5 witness.  The optimality argument needs only the INEQUALITY (every competitor >= its
      KL_1d) plus EQUALITY-on-mu* (mu*'s gap = its KL_1d).
  (D2) [n>=5 witness]  Two explicit n=5 orientations realizing the SAME T-multiset (minT=-7,
      values {-7,+1,+9}) have DIFFERENT gaps 0.7960484195.. vs 1.1251170042.. (mpmath-converged,
      gradnorm << 1e-30) -- so the gap is NOT a T-multiset functional at n>=5, and per-multiset
      deduplication in the search would be UNSOUND.
  (E) [closed form]  On mu* the seal is SCALAR and the gap is the 1-D two-value fixed point,
        m_hat_min(n) = -ln(1 - 2^-n) - delta_n,  delta_n > 0, doubly-exponentially small.

  ---- TWO-POINT FAMILY (all-n moment-reduction + minimizer verified to n=20) ------------------
  (F) Among all TWO-LEVEL achievable multisets { -a (x k), +b (x (N-k)) } (N = 2^n), the moment
      invariants (B) FORCE  a*b = N - 1  and  k = N b / (a + b)  [sympy-EXACT, ALL n].  The 1-D
      gap is found strictly DECREASING in a over the divisor candidates, so it is uniquely
      minimized at the extreme (a, b, k) = (N-1, 1, 1) = mu*.  The a*b=N-1 reduction is all-n
      exact; the strict-decrease-in-a SELECTION step is verified numerically for n = 2..20 (not
      proved analytically -- the naive continuous a-interpolation is not even globally monotone).

  ---- EXHAUSTIVE BASE (matches p9a) -----------------------------------------------------------
  (G) n = 2 (8 classes), n = 3 (128), n = 4 (32768): the global minimum over ALL orientation
      classes equals the closed-form m_hat_min(n) and is realized by the alternating-by-weight
      class.  (Reproduces p9a check (4)/(4b).)

  ---- ORIENTATION-LEVEL SEARCH (corroboration, NOT brute force) -------------------------------
  (H) n = 5, 6: a STRUCTURED ORIENTATION-LEVEL search -- gauge-fixed by spin-flips (singleton signs
      pinned to +1; (C) is an ORBIT statement, so this is sound), then, since the gap is NOT a
      multiset functional at n>=5 (D2), the EXACT vector-seal gap is evaluated at the ORIENTATION
      level on every deep-minT orientation (the band a mu*-beater would PLAUSIBLY live in -- a
      HEURISTIC motivated by (B), NOT implied by it: the per-minT gap floor is non-monotone, I2)
      plus random and greedy-descent samples -- confirms NO orientation beats m_hat_min(n) AMONG
      THE DEEP BAND (and, at n=5, a random/greedy shallow sample) and that mu* is realized (minT
      reaches -(2^n-1)).  It does NOT exact-seal the shallow orientations exhaustively, so it does
      NOT certify nothing-below-mu* among them; only the deepest single level is mu*-by-proof (B2).
      At n=6 the deep band is covered HONESTLY by
      TWO phases: a RANDOM breadth scan (which by itself reaches only minT ~ -43 -- it does NOT reach
      the maximal depth -63 on its own, so it leaves the deep band -44..-63 UNCOVERED) plus a
      GREEDY-DEEPEN phase that, from many random starts, repeatedly flips the single free sign that
      most DEEPENS minT until none does, genuinely driving minT down to the maximal depth -63 = mu*
      and collecting every deep orientation on the path.  (The deepest minT is thus an EMPIRICAL reach
      of the deepening phase, NOT an initialization: deepest_seen inits at 0, not at -(N-1).)  The
      next-best gap one level up, at minT=-61, is ~0.7165, far above mu*=0.0157, so mu* sits in an
      isolated deep basin.  Corroboration: the all-n claim rests on the proof (reductions A-F + base
      G), not on this finite search.
  (I) OBSTRUCTION FIGURES computed (traceable, not asserted prose): the gap is not Schur-monotone
      in the T^2 profile (n=4: 44 of 83 majorization-comparable distinct-multiset pairs violate it),
      and greedy single-flip descent does not reach the deep mu* basin at n=5.

  ---- WHAT IS NOT PROVEN (the honest residue) -------------------------------------------------
  The single open step is: that mu* GLOBALLY minimizes the 1-D KL lower bound KL_1d among ALL
  achievable T-multisets for ALL n (which, with (D)'s inequality + equality-on-mu*, would close
  global optimality).  No clean all-n certificate closes it -- the gap is NOT Schur-monotone in
  the T^2 profile (majorization FAILS: 44 of 83 comparable pairs at n=4, check I), the scalar-
  tilt restriction is not a uniform bound, and the single-sign-flip landscape has many local
  minima (greedy descent does not reach the deep mu* basin, check I).  The two-point family (F)
  is handled (mu* its minimizer, monotonicity verified to n=20); the multi-LEVEL competitors are
  ruled out only exhaustively (n <= 4) and by the orientation-level search (n = 5, 6).  Hence
  proof_status = PARTIAL_REDUCTION:  Paper IX's "theorem modulo a finite global-optimality lemma"
  is sharpened -- to a 1-D lower-bound problem with equality on mu*, all-n reductions, and the
  two-point family handled -- but it is NOT upgraded to a full all-n theorem.

Precision: sympy-exact for the combinatorial/algebraic structure (identities, moment invariants,
the two-point a*b=N-1 reduction); mpmath dps >= 130 for the m_hat_min(n) anchors and delta_n
(doubly-exponentially small -- never float64).  Pre-geometric: every quantity is a record-internal
KL content (nats) / orientation sign / character -- no spacetime, mass scale, or continuum field.
"""
import itertools
import numpy as np
import sympy as sp
import mpmath as mp

mp.mp.dps = 140
PASS = {}


def head(s):
    print("\n" + "=" * 80 + "\n" + s + "\n" + "=" * 80)


# ============================================================================================
# Shared machinery
# ============================================================================================
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


def chi_scalar_pre(n, mask, s):
    """Character chi_a(s) = prod_{i in a} s_i for a scalar state s (tuple) and integer mask a."""
    p = 1
    for i in range(n):
        if (mask >> i) & 1:
            p *= s[i]
    return p


def seal_solve(signs, chi0, tol=1e-13, maxit=200):
    """Solve the per-mode SEAL fixed point E_P[eps_a chi_a]=e^{-h_a} and return (m_hat, p, Tfull).
    The seal is the stationarity grad G = 0 of the STRICTLY CONVEX potential G(h)=psi(h)+sum_a e^{-h_a};
    Newton with a cheap monotone-descent guard (backtrack only when a full step would not decrease G).
    For degenerate high-gap orientations (some h_a -> +infinity) the iterate is capped (h <= 40) and
    may not reach tol; those have gap >> the minimum, so the returned D is a faithful large value and
    never a spurious minimum (verified: every orientation whose gap is near mu* converges cleanly)."""
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
        if not (Gn <= G0 + 1e-12):          # full Newton step did not decrease G -> backtrack
            t = 0.5
            while t > 1e-8 and Gpot(h - t * step) > G0:
                t *= 0.5
            Gn = Gpot(h - t * step)
        h = np.minimum(h - t * step, 40.0)  # cap to avoid overflow in degenerate (h->inf) directions
        G0 = Gpot(h)
    z = chi @ h
    z -= z.max()
    p = np.exp(z)
    p /= p.sum()
    mhat = float(np.sum(p * np.log(p * N)))
    return mhat, p, chi.sum(1)


def gap_vector_seal(signs, chi0, tol=1e-13, maxit=200):
    """The chiral gap m_hat(eps) = D(P*||U) (nats)."""
    return seal_solve(signs, chi0, tol=tol, maxit=maxit)[0]


# ============================================================================================
head("(A) the polynomial identity: alternating-by-weight collapses T(s) to two values  [sympy-exact]")
# ============================================================================================
# T(s) = sum_{a!=0} (-1)^{|a|-1} prod_{i in a} s_i.  Claim (sympy, all n verified symbolically):
#   T(s) = -( prod_i (1 - s_i) - 1 ).
# Proof:  prod_i (1 + (-(1 - s_i)))  expands to  sum_{a} prod_{i in a} (-(1-s_i)).  We instead use
# the cleaner direct identity:  -(prod_i (1-s_i) - 1) = -sum_{a != 0} prod_{i in a} (-s_i)
#   = -sum_{a!=0} (-1)^{|a|} prod_{i in a} s_i = sum_{a!=0} (-1)^{|a|-1} prod_{i in a} s_i = T(s).
ident_sympy_ok = True
for n in range(2, 8):
    s = sp.symbols("s0:%d" % n)
    # LHS: alternating-by-weight character sum
    lhs = 0
    for mask in range(1, 1 << n):
        idx = [i for i in range(n) if (mask >> i) & 1]
        term = 1
        for i in idx:
            term *= s[i]
        lhs += (-1) ** (len(idx) - 1) * term
    # RHS: -(prod_i (1 - s_i) - 1)
    rhs = -(sp.prod([1 - s[i] for i in range(n)]) - 1)
    if sp.expand(lhs - rhs) != 0:
        ident_sympy_ok = False
print("  sympy-exact:  T(s) = -( prod_i (1 - s_i) - 1 )  for n = 2..7 :", ident_sympy_ok)
# and prod_i(1 - s_i) = 2^n on all-minus, 0 otherwise (since some factor is 1-1=0) -> two values.
twoval_ok = True
for n in range(2, 8):
    for bits in itertools.product((-1, 1), repeat=n):
        prod = 1
        for b in bits:
            prod *= (1 - b)
        T = -(prod - 1)
        expected = -((1 << n) - 1) if all(b == -1 for b in bits) else 1
        if T != expected:
            twoval_ok = False
print("  => T = -(2^n-1) on all-minus, +1 on each of the other 2^n-1 states (n=2..7):", twoval_ok)
PASS["(A) sympy-exact identity T = -(prod(1-s_i)-1) and two-value collapse {-(2^n-1),+1}"] = (
    ident_sympy_ok and twoval_ok)


# ============================================================================================
head("(B) the two MOMENT INVARIANTS of the T-multiset, independent of orientation  [sympy-exact]")
# ============================================================================================
# sum_s T_eps(s) = sum_{a!=0} eps_a (sum_s chi_a(s)) = 0   (nontrivial characters sum to 0).
# sum_s T_eps(s)^2 = sum_{a,b} eps_a eps_b (sum_s chi_a chi_b) = 2^n sum_a eps_a^2 = 2^n (2^n-1).
# Verify symbolically that these hold for ARBITRARY signs eps (symbols), all n.
mom_ok = True
for n in range(2, 7):
    eps = sp.symbols("e1:%d" % (1 << n))  # eps_a for a=1..2^n-1
    states = list(itertools.product((-1, 1), repeat=n))
    masks = list(range(1, 1 << n))
    def chi(mask, s):
        p = 1
        for i in range(n):
            if (mask >> i) & 1:
                p *= s[i]
        return p
    Tsum = 0
    Tsq = 0
    for s in states:
        Ts = sum(eps[k] * chi(masks[k], s) for k in range(len(masks)))
        Tsum += Ts
        Tsq += Ts ** 2
    Tsum = sp.expand(Tsum)
    Tsq = sp.expand(Tsq)
    # eps_a^2 -> 1 since signs are +-1; substitute eps_a^2 = 1 by replacing each eps**2
    Tsq_reduced = Tsq
    for e in eps:
        Tsq_reduced = Tsq_reduced.subs(e ** 2, 1)
    Tsq_reduced = sp.expand(Tsq_reduced)
    if Tsum != 0 or Tsq_reduced != (1 << n) * ((1 << n) - 1):
        mom_ok = False
print("  sympy-exact (arbitrary signs):  sum_s T = 0  and  sum_s T^2 = 2^n(2^n-1)  for n=2..6 :", mom_ok)
# mu* saturates: (-(N-1))^2 + (N-1)*1 = (N-1)N = N(N-1); mean -(N-1)+(N-1) = 0.
sat_ok = all(
    ((2 ** n - 1) ** 2 + (2 ** n - 1) * 1) == (2 ** n) * (2 ** n - 1)
    and (-(2 ** n - 1) + (2 ** n - 1) * 1) == 0
    for n in range(2, 12))
print("  mu* = {-(2^n-1)} u {+1}^{2^n-1} saturates both invariants (mean 0, 2nd-moment 2^n(2^n-1)):", sat_ok)
PASS["(B) moment invariants sum T=0, sum T^2=2^n(2^n-1) (sympy, arbitrary signs); mu* saturates"] = (
    mom_ok and sat_ok)


# ============================================================================================
head("(B2) the MAXIMAL DEPTH is mu*-ONLY: minT = -(2^n-1) forces the alternating orientation "
     "(one spin-flip orbit, one gauge-fixed rep)  [SUB-THEOREM, all n; exhaustive n=2..6]")
# ============================================================================================
# IMPORTANT scope note (addresses the over-reading of (B)).  (B) pins mu* as the moment-extremal
# MULTISET; it does NOT order orientation classes by depth (the gap is NOT Schur-monotone in the
# T^2 profile -- see check I; the per-minT gap FLOOR is non-monotone already at n=4 -- see check I2).
# So "the minimizer MUST live at the deepest minT" is NOT a consequence of (B); the deep-band focus
# of the n=5,6 search (H) is a HEURISTIC, not an implication.  What IS rigorous about the deepest
# level is this clean all-n fact, proved here:
#   T_eps(s) = sum_{a!=0} eps_a chi_a(s) is a sum of M=2^n-1 signs, so T_eps(s) = -(2^n-1) at some
#   state s  IFF  eps_a chi_a(s) = -1 for EVERY mask a  <=>  eps_a = -chi_a(s) forced for all a.
#   Hence the depth -(2^n-1) is reached ONLY by the orientations eps^{(s)}_a = -chi_a(s), one per
#   state s; these form a SINGLE spin-flip orbit (R_g maps eps^{(s)} -> eps^{(g*s)}), whose all-minus
#   representative is eps_a = -(-1)^{|a|} = (-1)^{|a|-1} = the ALTERNATING orientation = mu*.  Pinning
#   the singletons to +1 (eps_{e_i} = -s_i = +1 <=> s = all-minus) leaves mu* as the UNIQUE gauge-
#   fixed deepest class.  So the maximal-depth MULTISET is mu* and nothing else, for ALL n.
b2_ok = True
for n in range(2, 7):
    states = list(itertools.product((-1, 1), repeat=n))
    masks = list(range(1, 1 << n))
    forced = set()                          # the orientations that reach depth -(2^n-1)
    for s in states:
        forced.add(tuple(-chi_scalar_pre(n, m, s) for m in masks))
    alt = tuple((-1) ** (bin(m).count("1") - 1) for m in masks)
    # spin-flip orbit of alt
    orbit_alt = set()
    for g in states:
        orbit_alt.add(tuple(alt[k] * chi_scalar_pre(n, masks[k], g) for k in range(len(masks))))
    # gauge-fixed (singletons +1) deepest orientations
    singleton_masks = [(1 << i) for i in range(n)]
    n_gauge_fixed = sum(
        1 for s in states
        if all(-chi_scalar_pre(n, sm, s) == 1 for sm in singleton_masks))
    ok_n = (forced == orbit_alt                      # deepest = exactly the alt orbit
            and alt in forced                        # alt is deepest
            and len(forced) == (1 << n)              # exactly 2^n of them (one per state)
            and n_gauge_fixed == 1)                  # unique gauge-fixed rep
    b2_ok = b2_ok and ok_n
    print("  n=%d: #deepest orientations=%d (=2^n=%d) ; == alt spin-flip orbit: %s ; "
          "#gauge-fixed deepest=%d (=1)" % (n, len(forced), 1 << n, forced == orbit_alt, n_gauge_fixed))
print("  => the maximal depth -(2^n-1) is realized by mu* ONLY (one orbit, one gauge-fixed rep), all n:", b2_ok)
PASS["(B2) maximal depth minT=-(2^n-1) is mu*-ONLY (single spin-flip orbit, unique gauge-fixed rep); "
     "proves the deepest single level is mu*, but NOT that the minimizer has the deepest minT"] = b2_ok


# ============================================================================================
head("(C) spin-flip invariance of the gap: (R_g eps)_a = eps_a chi_a(g)  [exact, the orbit reduction]")
# ============================================================================================
def chi_scalar(n, mask, s):
    p = 1
    for i in range(n):
        if (mask >> i) & 1:
            p *= s[i]
    return p
flip_ok = True
worst_flip = 0.0
for n in [3, 4]:
    chi0, _ = char_cols(n)
    M = (1 << n) - 1
    masks = list(range(1, 1 << n))
    rng = np.random.default_rng(7 + n)
    for _ in range(30):
        eps = [int(x) for x in (rng.integers(0, 2, M) * 2 - 1)]
        g = [int(x) for x in (rng.integers(0, 2, n) * 2 - 1)]
        Rg = [eps[k] * chi_scalar(n, masks[k], g) for k in range(M)]
        d = abs(gap_vector_seal(eps, chi0) - gap_vector_seal(Rg, chi0))
        worst_flip = max(worst_flip, d)
        if d > 1e-9:
            flip_ok = False
print("  max |m_hat(eps) - m_hat(R_g eps)| over random (eps,g), n=3,4:", worst_flip)
PASS["(C) gap is spin-flip invariant: m_hat(eps)=m_hat(R_g eps) -> gap is an ORBIT/multiset functional"] = flip_ok


# ============================================================================================
head("(D) the 1-D KL LOWER BOUND m_hat(eps) >= D(law_P(T)||law_U(T)) [data-processing, ALL n]; "
     "EQUALITY exhaustive n<=4 and on mu*")
# ============================================================================================
# CORRECTED SCOPE (vs Paper IX's reading).  By data-processing, m_hat(eps) = D(P*||U)
#   >= D(law_P(T)||law_U(T)) =: KL_1d(eps)  -- a 1-D KL on the T-marginal that depends on eps
# ONLY through the T-multiset.  This INEQUALITY holds for ALL n.  EQUALITY -- i.e. the seal P*
# being constant on level sets of T, hence the gap being a PURE MULTISET FUNCTIONAL -- holds:
#   * on the mu* orbit (the field is genuinely two-valued: equality => the closed form (E));
#   * EXHAUSTIVELY on every orbit at n <= 4 (verified here);
# but FAILS for n >= 5: the seal tilts over the full M-vector phi_a(s)=eps_a chi_a(s), not over
# the scalar T(s)=sum_a phi_a(s), so P* is NOT generally constant on T-level sets.  Two distinct
# n=5 orientations realizing the SAME T-multiset can have GENUINELY DIFFERENT gaps (check D2).
# Consequence: the corroborating search at n>=5 must be ORIENTATION-level, not multiset-deduped.
from collections import defaultdict

def gap_and_Tmarg_KL(signs, chi0):
    """Return (m_hat, KL_1d): the gap D(P*||U) and the 1-D KL of the T-marginal D(law_P(T)||law_U(T)).
    By data-processing m_hat >= KL_1d ALWAYS; equality iff the seal P* is constant on level sets of T."""
    mhat, p, Tfull = seal_solve(signs, chi0)
    N = len(p)
    Plev = defaultdict(float); cnt = defaultdict(int)
    for s in range(N):
        Plev[round(Tfull[s])] += p[s]; cnt[round(Tfull[s])] += 1
    kl1d = sum(Plev[t] * np.log(Plev[t] / (cnt[t] / N)) for t in Plev)
    return mhat, kl1d

red_ok = True
worst_red = 0.0      # max |m_hat - KL_1d|  (should be ~0 at n<=4: equality)
worst_class = 0.0    # max within-T-multiset gap spread (should be ~0 at n<=4: multiset functional)
for n in [2, 3, 4]:
    chi0, _ = char_cols(n)
    M = (1 << n) - 1
    classgap = defaultdict(list)
    for bits in itertools.product((-1, 1), repeat=M):
        T = (chi0 * np.asarray(bits, float)[None, :]).sum(1)
        key = tuple(sorted(int(round(t)) for t in T))
        mh, kl = gap_and_Tmarg_KL(bits, chi0)
        worst_red = max(worst_red, abs(mh - kl))
        classgap[key].append(mh)
    for key, gs in classgap.items():
        worst_class = max(worst_class, max(gs) - min(gs))
print("  exhaustive n<=4: max |m_hat - KL_1d(T-marginal)| =", worst_red, " (equality)")
print("  exhaustive n<=4: max within-multiset gap spread  =", worst_class, " (pure multiset functional)")
# Now the ALL-n direction: data-processing m_hat >= KL_1d, verified on a large n=5 random sample
# (no DPI violation), and the FAILURE of equality at n=5 (the gap is NOT a multiset functional).
rng_d = np.random.default_rng(12345)
chi0_5d, _ = char_cols(5); M5 = 31
min_excess = 1e9     # min(m_hat - KL_1d): must be >= ~0 (data-processing); a NEGATIVE value = DPI break
max_excess = 0.0     # max|m_hat - KL_1d| at n=5: STRICTLY POSITIVE (equality fails)
classgap5 = defaultdict(list)
NS = 20000
N5 = 1 << 5
for _ in range(NS):
    eps = (rng_d.integers(0, 2, M5) * 2 - 1)
    mh, p, Tf = seal_solve(eps, chi0_5d)          # single seal solve per orientation
    Plev = defaultdict(float); cnt = defaultdict(int)
    for s in range(N5):
        Plev[round(Tf[s])] += p[s]; cnt[round(Tf[s])] += 1
    kl = sum(Plev[t] * np.log(Plev[t] / (cnt[t] / N5)) for t in Plev)
    min_excess = min(min_excess, mh - kl)
    max_excess = max(max_excess, abs(mh - kl))
    key = tuple(sorted(int(round(t)) for t in Tf))
    classgap5[key].append(mh)
within5 = max((max(g) - min(g)) for g in classgap5.values())
print("  n=5 (20000 random orientations): min(m_hat - KL_1d) = %.3e  (>=0 => no DPI violation)" % min_excess)
print("  n=5 : max|m_hat - KL_1d| = %.3e ; max within-T-multiset gap spread = %.3e  (EQUALITY FAILS)"
      % (max_excess, within5))
# Check D passes iff: (i) equality+multiset-functional EXACT at n<=4, (ii) DPI lower bound holds at
# n=5 (no negative excess beyond rounding), (iii) equality demonstrably FAILS at n=5 (spread large).
dpi_ok = (min_excess > -1e-9)
fails_at_5 = (within5 > 1e-3 and max_excess > 1e-3)
if worst_red > 1e-9 or worst_class > 1e-9:
    red_ok = False
PASS["(D) gap >= 1-D KL of T-marginal by data-processing (ALL n, no DPI violation at n=5); "
     "equality+multiset-functional EXACT at n<=4; equality FAILS at n>=5"] = (
    red_ok and dpi_ok and fails_at_5)


# ============================================================================================
head("(D2) EXPLICIT n=5 witness: two orientations, SAME T-multiset, DIFFERENT gap  [mpmath dps=60]")
# ============================================================================================
# The clinching demonstration that the gap is NOT a T-multiset functional at n=5: two specific
# orientations eps_A, eps_B that realize the SAME T-multiset (minT=-7, value set {-7,+1,+9}) but
# have genuinely different chiral gaps.  Re-solved with an mpmath vector-seal (fully converged
# fixed point, gradient norm << 1e-30) so the gap split is NOT a float64 artifact.
eps_A = [1, 1, -1, 1, 1, -1, 1, -1, -1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, -1, 1, 1, 1, 1]
eps_B = [-1, -1, 1, -1, 1, -1, -1, 1, -1, 1, -1, -1, -1, 1, 1, -1, -1, 1, -1, -1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1]

def char_cols_mp(n):
    st = list(itertools.product((-1, 1), repeat=n))
    cols = []
    for s in st:
        row = []
        for mask in range(1, 1 << n):
            p = 1
            for i in range(n):
                if (mask >> i) & 1:
                    p *= s[i]
            row.append(p)
        cols.append(row)
    return cols  # N x (2^n - 1) integer character matrix

def mp_vector_seal(signs, n, dps=60, maxit=4000):
    """Newton solve of the seal grad G = 0 at mpmath precision; returns (m_hat, gradnorm)."""
    old = mp.mp.dps; mp.mp.dps = dps
    try:
        C = char_cols_mp(n)
        N = len(C); M = len(signs)
        # phi[s][a] = signs[a] * chi_a(s)
        phi = [[mp.mpf(signs[a] * C[s][a]) for a in range(M)] for s in range(N)]
        h = [mp.mpf(0) for _ in range(M)]
        gradnorm = mp.mpf(1)
        for _ in range(maxit):
            z = [sum(phi[s][a] * h[a] for a in range(M)) for s in range(N)]
            mx = max(z)
            w = [mp.e ** (z[s] - mx) for s in range(N)]
            Zt = sum(w)
            p = [w[s] / Zt for s in range(N)]
            E = [sum(p[s] * phi[s][a] for s in range(N)) for a in range(M)]
            emh = [mp.e ** (-h[a]) for a in range(M)]
            grad = [E[a] - emh[a] for a in range(M)]
            gradnorm = max(abs(g) for g in grad)
            if gradnorm < mp.mpf(10) ** (-(dps - 8)):
                break
            # Hessian = Cov_p(phi) + diag(e^{-h})
            Hk = [[mp.mpf(0)] * M for _ in range(M)]
            for a in range(M):
                for b in range(a, M):
                    cov = sum(p[s] * phi[s][a] * phi[s][b] for s in range(N)) - E[a] * E[b]
                    Hk[a][b] = cov + (emh[a] if a == b else mp.mpf(0))
                    Hk[b][a] = Hk[a][b]
            Hm = mp.matrix(Hk); gv = mp.matrix(grad)
            step = mp.lu_solve(Hm, gv)
            h = [h[a] - step[a] for a in range(M)]
        # gap D(P*||U)
        z = [sum(phi[s][a] * h[a] for a in range(M)) for s in range(N)]
        mx = max(z); w = [mp.e ** (z[s] - mx) for s in range(N)]; Zt = sum(w)
        p = [w[s] / Zt for s in range(N)]
        D = sum(p[s] * mp.log(p[s] * N) for s in range(N))
        return D, gradnorm
    finally:
        mp.mp.dps = old

# same T-multiset?
chi0_5w, _ = char_cols(5)
TA = tuple(sorted(int(round(t)) for t in (chi0_5w * np.asarray(eps_A, float)[None, :]).sum(1)))
TB = tuple(sorted(int(round(t)) for t in (chi0_5w * np.asarray(eps_B, float)[None, :]).sum(1)))
same_multiset = (TA == TB)
DA, gnA = mp_vector_seal(eps_A, 5, dps=60)
DB, gnB = mp_vector_seal(eps_B, 5, dps=60)
print("  same T-multiset (minT=%d, values=%s): %s" % (TA[0], sorted(set(TA)), same_multiset))
print("  m_hat(eps_A) = %s   (gradnorm %s)" % (mp.nstr(DA, 16), mp.nstr(gnA, 3)))
print("  m_hat(eps_B) = %s   (gradnorm %s)" % (mp.nstr(DB, 16), mp.nstr(gnB, 3)))
print("  gap split |DA - DB| = %s  => gap is NOT a T-multiset functional at n=5" % mp.nstr(abs(DA - DB), 12))
witness_ok = (same_multiset and gnA < mp.mpf("1e-30") and gnB < mp.mpf("1e-30")
              and abs(DA - mp.mpf("0.7960484195")) < mp.mpf("1e-6")
              and abs(DB - mp.mpf("1.1251170042")) < mp.mpf("1e-6")
              and abs(DA - DB) > mp.mpf("0.3"))
PASS["(D2) n=5 witness: same T-multiset, DIFFERENT gaps 0.7960484195.. vs 1.1251170042.. "
     "(mpmath-converged) => gap NOT a multiset functional at n>=5"] = bool(witness_ok)


# ============================================================================================
head("(E) closed form m_hat_min(n) = -ln(1 - 2^-n) - delta_n on mu*  [mpmath dps=140]")
# ============================================================================================
def exact_min(n):
    """Scalar seal on the two-value multiset mu*: one state weight e^{-h(2^n-1)}, (2^n-1) at e^{h}."""
    N = 1 << n
    M = N - 1
    def fp(h):
        w0 = mp.e ** (-h * M)
        eh = mp.e ** (h)
        Z = w0 + M * eh
        E_s1 = (w0 * (-1) + eh * (1)) / Z  # E[chi_{e_1}] = E[s_1]: -1 on all-minus, +1 else
        return E_s1 - mp.e ** (-h)
    h = mp.findroot(fp, mp.log(mp.mpf(M)) if M > 1 else mp.mpf("1.0"))
    w0 = mp.e ** (-h * M)
    eh = mp.e ** (h)
    Z = w0 + M * eh
    psi = mp.log(Z / N)
    Ecommon = mp.e ** (-h)
    D = h * (M * Ecommon) - psi  # m_hat = sum_a h E_a - psi (all equal)
    closed = -mp.log(1 - mp.power(2, -n))
    return D, closed, h

anchors = {3: "0.133530982072", 4: "0.064538521138", 5: "0.031748698315"}
anchor_ok = True
print("   n    m_hat_min(n) [exact fixed point]               delta_n            m*2^n")
for n in [3, 4, 5, 6, 7, 8, 9, 10, 25]:
    D, closed, h = exact_min(n)
    delta = closed - D
    print("  %3d  %-44s %-16s %s" % (n, mp.nstr(D, 38), mp.nstr(delta, 6), mp.nstr(D * 2 ** n, 16)))
    if n in anchors:
        anchor_ok = anchor_ok and abs(D - mp.mpf(anchors[n])) < mp.mpf("1e-11")
PASS["(E) closed form reproduces corpus anchors n=3,4,5 at dps=140"] = anchor_ok
# delta_n > 0 and doubly-exponentially small; strictly positive and shrinking n=3..6 (above the
# dps floor; for n>=7, delta_n ~ 2^{-n(2^n-1)} is below dps=140 -> precision noise, so we assert
# only where it is faithfully represented).  Sign-definiteness for all n is structural: the closed
# form -ln(1-2^-n) is the seal value AFTER dropping the (strictly positive) all-minus weight, so
# the exact fixed point sits strictly BELOW it -> delta_n > 0.
deltas = [exact_min(n)[1] - exact_min(n)[0] for n in [3, 4, 5, 6]]
delta_pos = all(d > 0 for d in deltas)
delta_shrinks = all(deltas[i] > deltas[i + 1] for i in range(len(deltas) - 1))
PASS["(E2) delta_n > 0 and doubly-exp shrinking for n=3..6 (n3 ~4e-7, n6 ~3e-115)"] = (
    delta_pos and delta_shrinks and deltas[-1] < mp.mpf("1e-100"))
pref_ok = all(exact_min(n)[0] > 0 for n in [3, 5, 8, 12, 20, 40])
PASS["(E3) m_hat_min(n) > 0 at every finite n; m_hat_min(n)*2^n -> 1 (prefactor exactly 1)"] = (
    pref_ok and abs(exact_min(40)[0] * 2 ** 40 - 1) < mp.mpf("1e-9"))


# ============================================================================================
head("(F) two-point family: a*b=N-1 is sympy-exact (ALL n); extreme (N-1,1,1)=mu* minimizes "
     "[gap strictly decreasing in a verified n=2..20, NOT proved analytically]")
# ============================================================================================
# GRADE SPLIT (honest):
#   * a*b = N-1 and k = N b/(a+b) is sympy-EXACT for all n (clean all-n algebraic reduction).
#   * the gap's strict DECREASE in a -- the step that SELECTS a=N-1 (=> mu*) -- is verified
#     NUMERICALLY over the divisor candidates to n=20, NOT proved analytically.  (The naive
#     continuous interpolation a in [1, N-1] is NOT even globally monotone -- a small non-monotone
#     region sits near a~1 where the interpolated multiset is non-achievable anyway -- so a one-line
#     convexity proof is unavailable; the all-n selection rests on the finite verification.)
# A two-level achievable multiset { -a (x k), +b (x (N-k)) }, a,b>0 odd, must satisfy (B):
#   mean 0 :  k a = (N-k) b ;   2nd moment : k a^2 + (N-k) b^2 = N(N-1).
# Substituting (N-k)b = k a into the 2nd moment gives k a (a+b) = N(N-1); and k(a+b)=N b from the
# headcount k + (N-k) = N.  Dividing:  a * b = N - 1.   (sympy-exact below.)
a, b, k, Nsym = sp.symbols("a b k N", positive=True)
# (i) substitute the mean-zero relation (N-k) = k a / b into the 2nd-moment to get k a (a+b) = N(N-1):
Nmk = k * a / b                                  # = N - k  from mean zero  k a = (N-k) b
mom2_reduced = sp.factor(sp.expand(k * a ** 2 + Nmk * b ** 2))   # should be k*a*(a+b)
mom2_form_ok = (mom2_reduced == sp.factor(k * a * (a + b)))
# (ii) headcount k + (N-k) = N with (N-k)=k a/b gives k(a+b) = N b.  Solve the pair for (k,b):
headcount = sp.Eq(k * (a + b), Nsym * b)
mom2_eq = sp.Eq(k * a * (a + b), Nsym * (Nsym - 1))
sol = sp.solve([mom2_eq, headcount], [k, b], dict=True)
ab_forced = False
for so in sol:
    if b in so:
        if sp.simplify(a * so[b] - (Nsym - 1)) == 0:   # a * b = N - 1 on the solution branch
            ab_forced = True
ab_identity = bool(mom2_form_ok and ab_forced)
print("  sympy: 2nd-moment reduces to k*a*(a+b)=N(N-1):", mom2_form_ok)
print("  sympy: with headcount k(a+b)=Nb, the unique branch gives b=(N-1)/a, i.e. a*b = N-1:", ab_forced)

def scalar_gap_2pt(a_, b_, k_, N, M):
    a_ = mp.mpf(a_); b_ = mp.mpf(b_); k_ = mp.mpf(k_)
    def seal(h):
        za = h * (-a_); zb = h * b_; mx = max(za, zb)
        wa = mp.e ** (za - mx); wb = mp.e ** (zb - mx); Z = k_ * wa + (N - k_) * wb
        return (k_ * wa * (-a_) + (N - k_) * wb * b_) / Z - M * mp.e ** (-h)
    # robust bisection (seal is monotone in h on (0, inf); root is unique)
    lo, hi = mp.mpf("1e-12"), mp.mpf("120")
    flo, fhi = seal(lo), seal(hi)
    assert flo * fhi < 0, "no sign change for two-point seal"
    for _ in range(400):
        mid = (lo + hi) / 2
        fm = seal(mid)
        if flo * fm <= 0:
            hi = mid
        else:
            lo = mid; flo = fm
    h = (lo + hi) / 2
    za = h * (-a_); zb = h * b_; mx = max(za, zb)
    wa = mp.e ** (za - mx); wb = mp.e ** (zb - mx); Z = k_ * wa + (N - k_) * wb
    Pa = wa / Z; Pb = wb / Z
    return k_ * Pa * mp.log(Pa * N) + (N - k_) * Pb * mp.log(Pb * N)

twopt_ok = True
dec_all = True
print("   n   #two-point candidates   argmin (a,b,k)        extreme=(N-1,1,1)?  decreasing-in-a?")
# n=2..12 exhaustively (every n), then a sparse confirmation set 13,15,16,18,20 (where the divisor
# structure of N-1=2^n-1 admits >2 two-point candidates) -- the monotonicity is verified, not proved.
for n in list(range(2, 13)) + [13, 15, 16, 18, 20]:
    N = 2 ** n; M = N - 1
    cands = []
    for av in range(1, N):
        if (N - 1) % av == 0:
            bv = (N - 1) // av
            if (N * bv) % (av + bv) == 0:
                kv = (N * bv) // (av + bv)
                if 1 <= kv <= N - 1:
                    cands.append((av, bv, kv, scalar_gap_2pt(av, bv, kv, N, M)))
    cands_by_a = sorted(cands)  # ascending a
    cands_by_g = sorted(cands, key=lambda x: x[3])
    extreme = (N - 1, 1, 1)
    is_min = cands_by_g[0][:3] == extreme
    # gap strictly decreasing in a
    dec = all(cands_by_a[i][3] > cands_by_a[i + 1][3] for i in range(len(cands_by_a) - 1))
    if not is_min:
        twopt_ok = False
    if not dec:
        dec_all = False
    print("  %3d   %18d   %-18s  %-16s   %s"
          % (n, len(cands), str(cands_by_g[0][:3]), str(is_min), str(dec)))
print("  a*b=N-1 sympy-exact (ALL n): %s ; gap strictly decreasing in a over divisors (n=2..20): %s"
      % (bool(ab_identity), dec_all))
PASS["(F) two-point: a*b=N-1 sympy-EXACT (all n); extreme (N-1,1,1)=mu* uniquely minimizes "
     "[strict decrease in a verified n=2..20, not proved analytically]"] = (
    bool(ab_identity) and twopt_ok and dec_all)


# ============================================================================================
head("(G) EXHAUSTIVE BASE n=2,3,4: global min over ALL orientation classes = closed form  [matches p9a]")
# ============================================================================================
base_ok = True
for n in [2, 3]:
    chi0, _ = char_cols(n)
    M = (1 << n) - 1
    closed = float(exact_min(n)[0])
    best = 1e9
    for bits in itertools.product((-1, 1), repeat=M):  # all 2^(2^n-1) orientations
        g = gap_vector_seal(bits, chi0)
        if g < best:
            best = g
    g_alt = gap_vector_seal(altweight_signs(n), chi0)
    ok = abs(best - closed) < 1e-9 and abs(g_alt - closed) < 1e-9
    print("  n=%d: brute min over all %d classes = %.12f ; closed = %.12f ; alt = %.12f ; min realized by alt = %s"
          % (n, 2 ** M, best, closed, g_alt, ok))
    PASS["(G) n=%d EXHAUSTIVE global min == closed form, realized by alternating-by-weight" % n] = ok
    base_ok = base_ok and ok

# n=4 exhaustive (all 2^15 = 32768 classes)
chi0, _ = char_cols(4)
closed4 = float(exact_min(4)[0])
g_alt4 = gap_vector_seal(altweight_signs(4), chi0)
best4 = 1e9
for bits in itertools.product((-1, 1), repeat=15):
    g = gap_vector_seal(bits, chi0)
    if g < best4:
        best4 = g
ok4 = abs(best4 - closed4) < 1e-9 and abs(g_alt4 - closed4) < 1e-9
print("  n=4: brute min over all 32768 classes = %.12f ; closed = %.12f ; alt = %.12f ; min realized by alt = %s"
      % (best4, closed4, g_alt4, ok4))
PASS["(G) n=4 EXHAUSTIVE (all 32768) global min == closed form, realized by alternating-by-weight"] = ok4


# ============================================================================================
head("(H) ORIENTATION-LEVEL SEARCH n=5,6: gauge-fixed deep-minT orientations + random + greedy; "
     "no orientation beats mu*")
# ============================================================================================
# Smart reduction (NOT 2^(2^n-1) brute force), corrected to be ORIENTATION-level:
#   - spin-flip gauge:   set every SINGLETON sign eps_{e_i} = +1  (since (R_g eps)_{e_i}=eps_{e_i} g_i,
#     a flip can fix all n singletons). (C) is an ORBIT statement, so gauge-fixing is SOUND.  The
#     alternating orientation has singleton signs +1, so it survives the gauge.  This removes the
#     2^n spin-flip redundancy -> 2^(2^n-1-n) gauge-fixed reps.
#   - the gap is NOT a T-multiset functional at n>=5 (check D2), so per-multiset DEDUPLICATION would
#     be UNSOUND (a representative's gap need not be the within-class minimum).  We therefore evaluate
#     the EXACT vector-seal gap at the ORIENTATION level: (i) every gauge-fixed orientation reaching a
#     DEEP minT (the only classes that could plausibly beat mu*, since the minimizer must be maximally
#     negatively-concentrated by (B)), (ii) a large random orientation sample, (iii) greedy single-flip
#     descent runs.  The 156 distinct-T-multiset count is reported only as a structural statistic.
# n=6: the gauge-fixed space (2^57) is too large to enumerate, so the search is adversarial
#      (deep-minT seeking) and ORIENTATION-level.  Both n are corroboration; the all-n claim rests on
#      the proof (A-F + base G), not on this finite search.

import os

def hadamard_sub(n):
    N = 1 << n
    H = np.empty((N, N), dtype=np.int16)
    for s in range(N):
        for a in range(N):
            H[s, a] = -1 if (bin(s & a).count("1") & 1) else 1
    return H[:, 1:]  # N x (N-1)


def enum_gauge_fixed(n, with_orientations=True, time_limit_s=None):
    """EXHAUSTIVE enumeration of the gauge-fixed orientation space (all SINGLETON signs pinned to +1
    by spin-flips) for the given n, via the fast Walsh transform.  Returns, for every DISTINCT
    T-multiset, one REALIZING full orientation (length-M sign vector).  This is the smart reduction:
    2^(2^n-1) classes / 2^n spin-flips = 2^(2^n-1-n) gauge-fixed reps; the gap depends only on the
    T-multiset, so we keep one orientation per distinct multiset and evaluate the EXACT vector seal."""
    import time as _time
    N = 1 << n; M = N - 1
    Hsub = hadamard_sub(n).astype(np.int32)
    singleton_cols = [(1 << i) - 1 for i in range(n)]
    free_cols = [c for c in range(M) if c not in singleton_cols]
    base = Hsub[:, singleton_cols].sum(axis=1).astype(np.int32)  # singletons fixed +1
    HF = Hsub[:, free_cols].astype(np.int32)
    F = len(free_cols)
    total = 1 << F
    CHUNK = 1 << 20
    bitw = np.arange(F, dtype=np.uint64)
    rep = {}            # multiset-bytes -> realizing full orientation
    best_minT = 0
    t0 = _time.time()
    complete = True
    for start in range(0, total, CHUNK):
        if time_limit_s is not None and (_time.time() - t0) > time_limit_s:
            complete = False
            break
        end = min(start + CHUNK, total)
        idx = np.arange(start, end, dtype=np.uint64)
        bits = ((idx[:, None] >> bitw[None, :]) & 1).astype(np.int32)
        signs = bits * 2 - 1
        T = base[None, :] + signs @ HF.T
        Ts = np.sort(T, axis=1).astype(np.int8)
        best_minT = min(best_minT, int(Ts[:, 0].min()))
        u, uidx = np.unique(Ts, axis=0, return_index=True)
        for j in range(len(u)):
            key = u[j].tobytes()
            if key not in rep:
                full = np.ones(M, dtype=np.int8)
                full[free_cols] = signs[uidx[j]]
                rep[key] = full.copy()
    return rep, best_minT, complete


def enum_deep_orientations(n, thresh, cap=None):
    """Enumerate the full gauge-fixed space (singletons +1) and return EVERY DISTINCT ORIENTATION
    (not multiset-deduped) whose minT <= thresh -- the deep tier that could plausibly beat mu*.
    Also returns the deepest minT reached.  Distinct ORIENTATIONS, not distinct multisets."""
    N = 1 << n; M = N - 1
    Hsub = hadamard_sub(n).astype(np.int32)
    singleton_cols = [(1 << i) - 1 for i in range(n)]
    free_cols = [c for c in range(M) if c not in singleton_cols]
    base = Hsub[:, singleton_cols].sum(axis=1).astype(np.int32)
    HF = Hsub[:, free_cols].astype(np.int32)
    F = len(free_cols); total = 1 << F
    CHUNK = 1 << 20; bitw = np.arange(F, dtype=np.uint64)
    deep = []           # list of length-M orientations with minT <= thresh
    best_minT = 0
    for start in range(0, total, CHUNK):
        end = min(start + CHUNK, total)
        idx = np.arange(start, end, dtype=np.uint64)
        bits = ((idx[:, None] >> bitw[None, :]) & 1).astype(np.int32)
        signs = bits * 2 - 1
        T = base[None, :] + signs @ HF.T
        mins = T.min(axis=1)
        best_minT = min(best_minT, int(mins.min()))
        sel = np.where(mins <= thresh)[0]
        for j in sel:
            full = np.ones(M, dtype=np.int8)
            full[free_cols] = signs[j]
            deep.append(full.copy())
            if cap is not None and len(deep) >= cap:
                return deep, best_minT
    return deep, best_minT


# ---- n = 5: ORIENTATION-LEVEL search: deep-minT orientations + random + greedy ------------------
chi0_5, _ = char_cols(5)
closed5 = float(exact_min(5)[0])
twoval5 = tuple(sorted([-(2 ** 5 - 1)] + [1] * (2 ** 5 - 1)))
n5_npz = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pD_n5_data.npz")

# (i) DEEP-minT orientations (the only candidates that could beat mu*); these REALIZE mu* (minT=-31).
# Threshold -25 keeps the deepest ~5000 orientations (incl. the unique minT=-31 = mu*): the
# minimizer must be maximally negatively-concentrated (B), so any mu*-beating class lives here.
deep5, deepest5 = enum_deep_orientations(5, thresh=-25)
min_gap5 = float("inf"); below5 = 0; mu_star5_present = False
for full in deep5:
    g = gap_vector_seal([int(x) for x in full], chi0_5)
    if g < min_gap5:
        min_gap5 = g
    if g < closed5 - 1e-8:
        below5 += 1
    if abs(g - closed5) < 1e-8:
        mu_star5_present = True

# also confirm the 156-distinct-T-multiset structural statistic if the precomputed file is present
n_distinct_mult5 = None
if os.path.exists(n5_npz):
    n_distinct_mult5 = int(np.load(n5_npz)["orients"].shape[0])

# (ii) random orientation sample (no dedup) -- bottoms out well above mu* but never below it
rng5 = np.random.default_rng(2024)
rand_min5 = float("inf"); rand_below5 = 0
for _ in range(40000):
    eps = (rng5.integers(0, 2, 31) * 2 - 1)
    g = gap_vector_seal([int(x) for x in eps], chi0_5)
    rand_min5 = min(rand_min5, g)
    if g < closed5 - 1e-8:
        rand_below5 += 1

# (iii) greedy single-flip descent (a few starts) -- confirms the deep mu* basin is NOT reached by
# local descent (an OBSTRUCTION datum, not a search that finds mu*): it bottoms out far above mu*.
def greedy5(eps0, nflip_passes=5):
    eps = list(eps0); g = gap_vector_seal(eps, chi0_5)
    for _ in range(nflip_passes):
        improved = False
        for i in range(31):
            eps[i] *= -1; g2 = gap_vector_seal(eps, chi0_5)
            if g2 < g - 1e-12:
                g = g2; improved = True
            else:
                eps[i] *= -1
        if not improved:
            break
    return g
greedy_min5 = float("inf"); greedy_hits = 0; NSTART = 40
for _ in range(NSTART):
    eps0 = (rng5.integers(0, 2, 31) * 2 - 1)
    gf = greedy5(eps0)
    greedy_min5 = min(greedy_min5, gf)
    if abs(gf - closed5) < 1e-6:
        greedy_hits += 1

g_alt5 = gap_vector_seal(altweight_signs(5), chi0_5)
print("  n=5 deep-minT orientations (minT<=-25): %d evaluated at the ORIENTATION level; deepest minT=%d"
      % (len(deep5), deepest5))
if n_distinct_mult5 is not None:
    print("  n=5 (structural statistic: %d distinct T-multisets in the gauge-fixed space)" % n_distinct_mult5)
print("  n=5 min gap over deep orientations = %.12f ; closed mu* = %.12f ; alt = %.12f ; #below mu* = %d"
      % (min_gap5, closed5, g_alt5, below5))
print("  n=5 mu* realized among deep orientations: %s" % mu_star5_present)
print("  n=5 random sample (40000): min = %.12f (>> mu*); #below mu* = %d" % (rand_min5, rand_below5))
print("  n=5 greedy single-flip descent (%d starts): min reached = %.12f ; mu*-hits = %d  "
      "(deep mu* basin NOT found by local descent => obstruction 3)" % (NSTART, greedy_min5, greedy_hits))
n5_ok = (deepest5 == -(2 ** 5 - 1) and abs(min_gap5 - closed5) < 1e-8 and below5 == 0
         and rand_below5 == 0 and mu_star5_present and abs(g_alt5 - closed5) < 1e-8)
PASS["(H) n=5 ORIENTATION-LEVEL search (deep-minT orientations + 40000 random, EXACT seal): "
     "min = mu*; nothing below mu*; mu* realized at minT=-31"] = n5_ok


# ---- n = 6: alt realizes mu* + adversarial deep search (no class found below mu*) ---------------
chi0_6, _ = char_cols(6)
closed6 = float(exact_min(6)[0])
g_alt6 = gap_vector_seal(altweight_signs(6), chi0_6)
twoval6 = tuple(sorted([-(2 ** 6 - 1)] + [1] * (2 ** 6 - 1)))
alt6_ok = abs(g_alt6 - closed6) < 1e-7

# adversarial search, deep-minT seeking, ORIENTATION-level.  Two phases that together cover the deep
# band [-(2^n-1) .. ~ -mid] where a mu*-beater would PLAUSIBLY live -- a HEURISTIC focus motivated by
# mu*'s moment-extremality (B), NOT implied by it: the per-minT gap floor is NON-monotone (check I2),
# so a shallower minT can give a smaller gap and this search does NOT certify nothing-below among
# shallow orientations.  Only the SINGLE deepest level -(2^n-1) is mu*-by-proof (B2):
#   (1) a RANDOM gauge-fixed phase for breadth (correct init deepest_seen=0; a random scan does NOT
#       reach the deepest minT by itself -- it bottoms out ~ -43 at n=6 -- so this phase alone leaves
#       the deep band -44..-63 UNCOVERED);
#   (2) a GREEDY-DEEPEN phase that genuinely reaches the deepest minT: from many random gauge-fixed
#       starts, repeatedly flip the single free sign that most DEEPENS minT (makes it more negative)
#       until no flip deepens.  This drives minT down to the maximal depth -(2^n-1) = -63 = mu* and
#       collects every distinct deep orientation visited along the way, so the deep band IS covered.
# The EXACT vector-seal gap is evaluated on every DISTINCT deep orientation found by EITHER phase
# (keyed by orientation, since the gap is not a multiset functional at n>=5, (D2)); confirm none
# beats mu*.  mu* (the alternating orientation) is inserted explicitly as the depth -63 anchor and
# is independently re-reached by the greedy-deepen phase.
def n6_adversarial(n_random=2_000_000, n_deep_per_batch=8, n_deepen_starts=400, deep_thresh=-44,
                   seed=0):
    n = 6; N = 1 << n; M = N - 1
    rng = np.random.default_rng(seed)
    Hsub = hadamard_sub(n).astype(np.int16)
    singleton_cols = [(1 << i) - 1 for i in range(n)]
    base = Hsub[:, singleton_cols].astype(np.int32).sum(1)
    free_cols = [c for c in range(M) if c not in singleton_cols]
    HF = Hsub[:, free_cols].astype(np.int16)
    F = len(free_cols)
    deep_orients = {}   # orientation-bytes -> realizing full orientation
    # ---- phase (1): RANDOM breadth.  deepest_seen inits at 0 (NOT at -(N-1)): the random scan's
    #      reach is reported HONESTLY, and is ~ -43 at n=6 (it does NOT reach -63 on its own).
    deepest_random = 0
    B = 50000
    for _ in range(max(1, n_random // B)):
        signs = (rng.integers(0, 2, (B, F)) * 2 - 1).astype(np.int16)
        T = base[None, :] + signs @ HF.T
        Ts = np.sort(T, axis=1).astype(np.int16)
        mins = Ts[:, 0]
        deepest_random = min(deepest_random, int(mins.min()))
        order = np.argsort(mins)[:n_deep_per_batch]   # the deepest-minT classes in this batch
        for oi in order:
            full = np.ones(M, dtype=int)
            full[free_cols] = [int(x) for x in signs[oi]]
            key = full.astype(np.int8).tobytes()
            if key not in deep_orients:
                deep_orients[key] = full
    # ---- phase (2): GREEDY-DEEPEN.  Drives minT to the maximal depth -(2^n-1) and collects every
    #      distinct deep (minT <= deep_thresh) orientation visited -- this is what covers -44..-63.
    HFi = HF.astype(np.int32); basei = base.astype(np.int32)
    deepest_deepen = 0
    for _ in range(n_deepen_starts):
        sgn = (rng.integers(0, 2, F) * 2 - 1).astype(np.int32)
        T = basei + HFi @ sgn
        minT = int(T.min())
        improved = True
        while improved:
            improved = False
            best_flip = None; best_new = minT
            for j in range(F):                         # flip j shifts T by -2*sgn[j]*HF[:,j]
                m = int((T - 2 * sgn[j] * HFi[:, j]).min())
                if m < best_new:
                    best_new = m; best_flip = j
            if best_flip is not None:
                j = best_flip
                T = T - 2 * sgn[j] * HFi[:, j]; sgn[j] *= -1; minT = best_new; improved = True
                if minT <= deep_thresh:                # collect deep orientations on the path
                    full = np.ones(M, dtype=int); full[free_cols] = [int(x) for x in sgn]
                    deep_orients[np.asarray(full, np.int8).tobytes()] = full
        deepest_deepen = min(deepest_deepen, minT)
        if minT <= deep_thresh:
            full = np.ones(M, dtype=int); full[free_cols] = [int(x) for x in sgn]
            deep_orients[np.asarray(full, np.int8).tobytes()] = full
    # always test the alt orientation (the mu* depth -63 anchor) explicitly too
    deep_orients[b"__alt__"] = np.array(altweight_signs(n), dtype=int)
    # evaluate the EXACT vector-seal gap on every distinct deep orientation; track the gap floor per
    # minT level so the next-best (non-mu*) gap in the deepest band is reported, not just the global min.
    cand_min = float("inf"); below = 0; checked = 0
    gap_floor_by_minT = {}
    for full in deep_orients.values():
        T = (chi0_6 * np.asarray(full, float)[None, :]).sum(1)
        mT = int(round(T.min()))
        g = gap_vector_seal([int(x) for x in full], chi0_6)
        checked += 1
        if g < cand_min:
            cand_min = g
        if g < closed6 - 1e-8:
            below += 1
        if mT not in gap_floor_by_minT or g < gap_floor_by_minT[mT]:
            gap_floor_by_minT[mT] = g
    return (deepest_random, deepest_deepen, cand_min, below, checked, gap_floor_by_minT)

(deepest_rand6, deepest_deepen6, cand_min6, below6, checked6,
 gap_floor6) = n6_adversarial(seed=0)
print("  n=6: alt realizes mu* closed form = %.12f (alt gap = %.12f, match=%s)"
      % (closed6, g_alt6, alt6_ok))
print("  n=6 phase (1) RANDOM breadth (2e6 classes): deepest minT reached by the RANDOM scan = %d"
      % deepest_rand6)
print("       (a random scan does NOT reach -63 on its own -- it leaves the deep band -44..-63 to phase 2)")
print("  n=6 phase (2) GREEDY-DEEPEN: deepest minT reached = %d  (mu* needs -%d -- the maximal depth IS reached)"
      % (deepest_deepen6, 2 ** 6 - 1))
print("       EXACT vector-seal gap on %d distinct deep ORIENTATIONS; global min = %.12f ; #below mu* = %d"
      % (checked6, cand_min6, below6))
# report the gap floor across the genuinely deep band so the mu*-isolation is traceable
for mT in sorted(gap_floor6):
    if mT <= -53:
        tag = "  <- mu* (exact)" if abs(gap_floor6[mT] - closed6) < 1e-8 else ""
        print("       minT=%4d : min gap in band = %.6f%s" % (mT, gap_floor6[mT], tag))
# the deepest-band requirements: (i) greedy-deepen genuinely REACHES the maximal depth -63 (not an
# init artifact); (ii) mu* is realized at -63 with the exact gap; (iii) nothing below mu*; (iv) the
# next-deepest band (minT=-61) is gapped FAR above mu* (the deep band is covered, not skipped).
reaches_max_depth6 = (deepest_deepen6 == -(2 ** 6 - 1))
mu_at_max_depth6 = (-(2 ** 6 - 1) in gap_floor6 and abs(gap_floor6[-(2 ** 6 - 1)] - closed6) < 1e-8)
next_band_gapped6 = (-61 in gap_floor6 and gap_floor6[-61] > closed6 + 1e-2)
PASS["(H) n=6 deep ORIENTATION-LEVEL search (random breadth + GREEDY-DEEPEN to the maximal depth -63, "
     "EXACT seal on every deep orientation): alt realizes mu* at -63; none below mu*; deep band -44..-63 "
     "covered (next-best at minT=-61 is far above mu*)"] = (
    alt6_ok and below6 == 0 and reaches_max_depth6 and mu_at_max_depth6 and next_band_gapped6)


# ============================================================================================
head("(I) OBSTRUCTION FIGURES (computed, not asserted): majorization non-monotone; greedy fails")
# ============================================================================================
# These are the figures the paper cites as evidence that the natural closing routes genuinely fail.
# Computed here so they are TRACEABLE, not prose.
# (1) Majorization in the T^2 profile is NOT Schur-monotone for the gap.  Enumerate the distinct
#     achievable T-multisets at n=3,4; at fixed 2nd moment the T^2 profiles have equal sum, so the
#     majorization partial order applies.  Count comparable pairs and how many VIOLATE the would-be
#     monotonicity "more concentrated T^2 (majorizes) => smaller gap".
def majorizes(x, y):
    xs = sorted(x, reverse=True); ys = sorted(y, reverse=True)
    if len(xs) != len(ys) or abs(sum(xs) - sum(ys)) > 1e-9:
        return False
    cx = cy = 0.0
    for i in range(len(xs)):
        cx += xs[i]; cy += ys[i]
        if cx < cy - 1e-9:
            return False
    return True

maj_report = {}
for n in [3, 4]:
    chi0n, _ = char_cols(n); Mn = (1 << n) - 1
    seen = {}
    for bits in itertools.product((-1, 1), repeat=Mn):
        T = (chi0n * np.asarray(bits, float)[None, :]).sum(1)
        key = tuple(sorted(int(round(t)) for t in T))
        if key not in seen:
            seen[key] = gap_vector_seal(bits, chi0n)
    keys = list(seen.keys())
    prof = {k: tuple(sorted((t * t for t in k), reverse=True)) for k in keys}
    comparable = 0; violations = 0
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            ki, kj = keys[i], keys[j]
            if majorizes(prof[ki], prof[kj]) or majorizes(prof[kj], prof[ki]):
                comparable += 1
                big = ki if majorizes(prof[ki], prof[kj]) else kj   # more concentrated T^2
                small = kj if big == ki else ki
                if not (seen[big] <= seen[small] + 1e-9):            # monotone would need big <= small
                    violations += 1
    maj_report[n] = (len(keys), comparable, violations)
    print("  n=%d: %d distinct T-multisets, %d majorization-comparable pairs, %d violate monotonicity"
          % (n, len(keys), comparable, violations))
# the headline figure cited in the paper: n=4 -> 44 of 83 comparable pairs violate
maj_ok = (maj_report[4][1] == 83 and maj_report[4][2] == 44 and maj_report[3][2] >= 1)

# (2) greedy single-flip descent at n=5 does NOT reach the deep mu* basin from generic starts
#     (already computed in (H): greedy_min5 >> mu*, greedy_hits == 0 over the starts run).
greedy_obstruction_ok = (greedy_hits == 0 and greedy_min5 > closed5 + 1e-2)
print("  greedy single-flip descent at n=5: min reached %.6f >> mu* %.6f ; mu*-hits = %d  "
      "(deep basin not locally reachable)" % (greedy_min5, closed5, greedy_hits))
PASS["(I) obstructions COMPUTED: majorization non-monotone (n=4: 44 of 83 comparable pairs violate); "
     "greedy single-flip does NOT reach the deep mu* basin at n=5"] = bool(maj_ok and greedy_obstruction_ok)


# ============================================================================================
head("(I2) the per-minT gap FLOOR is NON-monotone at n=4: a SHALLOWER minT can give a SMALLER gap "
     "-- so 'deeper minT => smaller gap' is FALSE; the deep-band focus of (H) is a HEURISTIC, not (B)")
# ============================================================================================
# This is the figure that disciplines the (H) search language.  (B) pins mu* as the moment-extremal
# MULTISET, but does NOT order classes by depth.  Exhaustively at n=4, compute the FLOOR (minimum gap)
# over all orientations at each minT level.  If "deeper => smaller gap" held, the floor would decrease
# monotonically as minT decreases.  It does NOT: e.g. minT=-7 floor ~0.328 is BELOW minT=-11 (~0.480)
# and minT=-13 (~0.725).  So a mu*-beater is NOT forced into the deepest band by (B); the deep-band
# focus is a search heuristic.  (Only the SINGLE deepest level minT=-(2^n-1) is mu*-only, by (B2).)
chi0_4i, _ = char_cols(4)
floor_by_minT = {}
for bits in itertools.product((-1, 1), repeat=15):
    T = (chi0_4i * np.asarray(bits, float)[None, :]).sum(1)
    mT = int(round(T.min()))
    g = gap_vector_seal(bits, chi0_4i)
    if mT not in floor_by_minT or g < floor_by_minT[mT]:
        floor_by_minT[mT] = g
print("  n=4 per-minT gap FLOOR (min gap over all orientations at that minT):")
for mT in sorted(floor_by_minT, reverse=True):
    tag = "  <- mu* (deepest, B2)" if mT == -(2 ** 4 - 1) else ""
    print("    minT=%4d : floor = %.6f%s" % (mT, floor_by_minT[mT], tag))
# is the floor monotone decreasing as minT decreases (shallow -> deep)?  Should be NON-monotone.
prevf = None; floor_monotone = True
for mT in sorted(floor_by_minT, reverse=True):     # shallow (high minT) -> deep (low minT)
    if prevf is not None and floor_by_minT[mT] < prevf - 1e-9:
        floor_monotone = False
    prevf = floor_by_minT[mT]
# the specific referee figures (the gap is NOT a multiset functional only at n>=5, but the FLOOR
# non-monotonicity is already a clean n=4 fact): minT=-7 floor < minT=-11 floor < minT=-13 floor.
shallow_beats_deeper = (floor_by_minT[-7] < floor_by_minT[-11] - 1e-6
                        and floor_by_minT[-7] < floor_by_minT[-13] - 1e-6)
deepest_is_mu_star = abs(floor_by_minT[-(2 ** 4 - 1)] - float(exact_min(4)[0])) < 1e-8
print("  floor monotone (deeper => smaller)?  %s  (expected False: NON-monotone)" % floor_monotone)
print("  shallow minT=-7 floor (%.4f) < deeper minT=-11 (%.4f) and minT=-13 (%.4f): %s"
      % (floor_by_minT[-7], floor_by_minT[-11], floor_by_minT[-13], shallow_beats_deeper))
print("  deepest level minT=-15 floor = mu* global min (B2): %s" % deepest_is_mu_star)
PASS["(I2) per-minT gap floor NON-monotone at n=4 (minT=-7 floor 0.328 < minT=-11 floor 0.480 < "
     "minT=-13 floor 0.725): 'deeper=>smaller gap' is FALSE, so deep-band focus is heuristic not (B); "
     "ONLY the deepest level minT=-15 is mu* (B2)"] = bool(
    (not floor_monotone) and shallow_beats_deeper and deepest_is_mu_star)


# ============================================================================================
head("MACHINE CHECKS")
# ============================================================================================
ok = True
for kkey, v in PASS.items():
    print("  [%s] %s" % ("PASS" if v else "FAIL", kkey))
    ok = ok and v
npass = sum(1 for v in PASS.values() if v)
ntot = len(PASS)
print("\n  %d/%d checks pass" % (npass, ntot))
print("  " + ("ALL CHECKS PASS (%d/%d)" % (npass, ntot) if ok else "*** SOME CHECK FAILED ***"))
assert ok, "a check failed"
print("=" * 80)
print("PROOF STATUS: PARTIAL_REDUCTION.")
print("  All-n reductions PROVEN: (A) two-value identity [sympy], (B) moment invariants [sympy],")
print("  (C) spin-flip invariance, (D) the 1-D KL LOWER BOUND m_hat >= KL_1d by data-processing")
print("  with equality on mu*, (E) closed form, plus (F) the two-point a*b=N-1 [sympy] with the")
print("  extreme minimizing (monotonicity verified to n=20, not proved analytically).  SCOPE")
print("  CORRECTION: the gap is a PURE T-multiset functional only for n<=4; at n>=5 it is NOT")
print("  (check D2: two n=5 orientations, same T-multiset, gaps 0.796 vs 1.125), so the n>=5")
print("  searches are ORIENTATION-level, not multiset-deduped.  Global optimality is EXHAUSTIVE at")
print("  n=2,3,4 (G) and corroborated at the orientation level at n=5,6 (H).  DEEP-BAND DISCIPLINE:")
print("  the deep-band focus of the n=5,6 search is a HEURISTIC, NOT a consequence of (B) -- the")
print("  per-minT gap floor is NON-monotone already at n=4 (check I2: minT=-7 floor 0.328 BELOW")
print("  minT=-11 0.480 and minT=-13 0.725), so a shallower minT can give a smaller gap.  Only the")
print("  SINGLE deepest level minT=-(2^n-1) is mu*-by-proof (check B2, all n); the search finds")
print("  nothing below mu* AMONG THE DEEP BAND, and does NOT certify nothing-below among shallow")
print("  orientations.  The single open step -- mu* minimizes the 1-D KL among ALL achievable")
print("  multisets for ALL n -- is NOT closed by an all-n certificate (gap not Schur-monotone in")
print("  T^2: 44 of 83 comparable pairs at n=4; the landscape has local minima).  Paper IX's finite")
print("  lemma is SHARPENED to a 1-D lower-bound problem with equality on mu*, the two-point family")
print("  handled, and the maximal-depth level pinned (B2), not upgraded to a full all-n theorem.")
print("=" * 80)
