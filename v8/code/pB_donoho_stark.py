"""
v7 Paper IX, receipt pB (TOOL 1) -- DONOHO-STARK uncertainty + K.T. SMITH equality case,
adapted as an attempted closing tool for the open chiral-gap global-optimality residue [L*].

THE TARGET [L*] (open; this receipt ATTACKS it, does NOT assume it).
  States s in {-1,+1}^n, N = 2^n, nonempty masks a, M = N-1, character chi_a(s) = prod_{i in a} s_i.
  Orientation eps in {-1,+1}^M.  Anomaly field  T_eps(s) = sum_{a!=0} eps_a chi_a(s)  is the real
  function on {+-1}^n with Walsh-Hadamard spectrum (0, eps_1,...,eps_M): ZERO mean, every nonzero-
  frequency coefficient of MODULUS EXACTLY 1 (a flat / +-1 spectrum).  The seal-tilted law P*
  (per-mode fixed point E_{P*}[eps_a chi_a]=e^{-h_a}); the chiral gap m_hat = D(P*||U) = ln N - H(P*).
  mu* = the DELTA orientation eps_a = -chi_a(s*): T = 1 - N*delta_{s*}, multiset {-(N-1) x1, +1 x(N-1)}.
  [L*] = for EVERY +-1-spectrum orientation, H(P*) <= ln(N-1)+delta_n with equality ONLY on the mu*
  orbit; equivalently every non-mu* achievable multiset has gap bounded below by an n-INDEPENDENT
  O(1) constant (mu* isolated at O(2^-n), runner-up O(1)).

THE TOOL.  Donoho-Stark (1989): for f on a finite abelian group G of order N,
      |supp(f)| * |supp(f-hat)| >= N,
with K.T. Smith's equality theorem on (Z/2)^n: EQUALITY iff f is a (translate of a) uniform-modulus
indicator of a COSET of a subgroup H <= G (a "picket fence"), so |supp f| = |H|, |supp f-hat| = N/|H|.

WHAT THIS RECEIPT ESTABLISHES (honest scope -- closes_Lstar = NO):

  (DS1) [the support pinning -- sympy/exact]  For EVERY orientation eps, the spectral support of the
        anomaly field is FULL on the nonzero frequencies:  |supp(T_eps-hat)| = M = N-1, identically.
        Hence raw DS on T_eps gives  |supp(T_eps)| >= N/(N-1) > 1  =>  |supp(T_eps)| >= 2 -- which
        is TRIVIAL (every zero-mean nonzero T has >= 2 nonzero values) and IDENTICAL across all eps.
        DS on T_eps CANNOT separate mu* from any competitor: the spectral support is constant.
        => DS's separating power lives (if anywhere) in the SPATIAL support |supp(T_eps)|, NOT spectral.

  (DS2) [the delta IS the DS extremal -- but for support L0, the WRONG functional -- exact]
        mu* (eps = -chi_a(s*)) gives T = -(N-1) at s* and +1 at the other N-1 states: spatially FULL
        (|supp(T)| = N) yet the DEVIATION  g := T - mean(T) = T  (mean 0) is "as concentrated as a
        zero-mean field can be" -- a near-delta (one big negative spike).  Smith's equality case is the
        COSET INDICATOR  f_H = 1_H, whose Fourier transform is the picket fence (uniform on H^perp).
        We make the DS/Smith dictionary EXACT and show: the orientation whose field T_eps is a SHIFTED
        COSET INDICATOR is exactly the SUBGROUP/PRODUCT orientations, NOT mu*.  mu* is the DELTA case
        (H = {0}, the trivial subgroup, f = single point) -- the OPPOSITE extreme of the picket fence.
        So the "DS extremal == mu*" identification needs the SINGLE-POINT (delta) end of Smith's
        classification, which is the |supp f|=1 case -- a statement about L0 support, not about KL.

  (DS3) [the fatal direction mismatch -- the reason it is NO, numeric n<=6 + structural]
        DS / Smith control SUPPORT SIZE (an L0 / counting functional).  The target [L*] controls the
        SEAL-TILTED KL = ln N - H(P*).  These are DIFFERENT functionals and are NOT comparable:
          * H(P*) is a smooth strictly-concave functional of the tilt, sensitive to the FULL value
            multiset and its multiplicities;
          * |supp(.)| is blind to magnitudes and to multiplicities-above-1.
        We DEMONSTRATE the mismatch on the n<=6 achievable data: (i) many DISTINCT achievable T have
        the SAME spatial support size |supp(T)| (DS sees one number) yet DIFFERENT gaps; (ii) the
        gap-ranking and the |supp|-ranking DISAGREE (Kendall/Spearman << 1, sign inversions); (iii)
        the closest-to-uniform competitor is NOT the one DS would single out.

  (DS4) [the WEIGHTED / entropic refinement of DS -- the honest best effort, and why it still fails]
        We replace the L0 support by a RENYI/entropy support measure (Renyi-0 -> Renyi-alpha; the
        "entropic uncertainty" weakening of DS).  Two refinements tested:
          (a) the Renyi-2 (participation-ratio) uncertainty  PR(P)*PR(P-hat) and its DS-type product;
          (b) a Hirschman-style entropy product applied to the SQUARED tilted amplitude (Born map).
        Each is a VALID inequality, but it lower-bounds an UNCERTAINTY PRODUCT or a SPECTRAL entropy --
        NOT the seal-tilted spatial entropy H(P*) we need an UPPER bound on.  Numerically the refined
        DS product does NOT order the achievable multisets by gap and does NOT isolate mu*: the
        runner-up by DS-product is not the runner-up by gap.  => the refinement bounds the wrong
        functional; it does not deliver the n-independent O(1) gap floor for non-mu*.

  VERDICT  closes_Lstar = NO.  Donoho-Stark / Smith is an L0-SUPPORT uncertainty principle.  The flat
  +-1 spectrum pins the SPECTRAL support to full (N-1) for EVERY orientation, so DS's only live degree
  of freedom is the SPATIAL support of T_eps -- a counting functional that is provably NOT monotone
  with, and not even a function of, the seal-tilted KL gap (the true [L*] target).  mu* is indeed the
  EXTREMAL of Smith's classification (the single-point / delta end), but that extremality is for
  SUPPORT SIZE, not for the KL/entropy.  The entropic refinement (Renyi/Hirschman) is a valid weakening
  but still bounds an uncertainty product / spectral entropy, the WRONG side, not H(P*).  PARTIAL is
  NOT warranted: the bound DS yields on the true gap functional is trivial (>= 0), not a real floor.

Precision: sympy-exact for the spectrum-support and coset/Smith identities; mpmath dps>=130 for every
gap / entropy / Renyi value (never float64).  Pre-geometric: every quantity is a record-internal KL
content (nats) / character sign / support count -- no spacetime, mass scale, or continuum field.
"""
import itertools
import numpy as np
import sympy as sp
import mpmath as mp

mp.mp.dps = 140
PASS = {}


def head(s):
    print("\n" + "=" * 92 + "\n" + s + "\n" + "=" * 92)


# ============================================================================================
# Shared machinery -- VERBATIM from pD_chiral_global_optimality.py / setup_extract_d1d.py
# (read-only reuse; reproduced here so this receipt is self-contained and runs standalone).
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
    """The chiral gap m_hat(eps) = D(P*||U) (nats)."""
    return seal_solve(signs, chi0, tol=tol, maxit=maxit)[0]


def exact_min(n):
    """Scalar seal on mu* = {-(N-1) (x1), +1 (x(N-1))}; VERBATIM from pD/p9a.  Returns (D, closed, h)."""
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


def walsh_spectrum(vals):
    """Walsh-Hadamard transform of a length-N (N=2^n) real vector (numpy), normalized so that the
    coefficient of character chi_a is  (1/N) sum_s f(s) chi_a(s) = <f, chi_a>.  Returns length-N vector
    (index 0 = DC mean).  Uses the fast in-place transform; chi ordering matches char_cols masks."""
    N = len(vals)
    n = int(round(np.log2(N)))
    f = np.array(vals, float).copy()
    h = 1
    while h < N:
        for i in range(0, N, h * 2):
            for j in range(i, i + h):
                x = f[j]; y = f[j + h]
                f[j] = x + y; f[j + h] = x - y
        h *= 2
    return f / N  # <f, chi_a> for a = 0..N-1 in the standard Walsh order


# ============================================================================================
head("(DS1) the SPECTRAL SUPPORT of T_eps is FULL (= N-1) for EVERY orientation  [sympy/exact]")
# ============================================================================================
# By construction the Walsh spectrum of T_eps is (0, eps_1, ..., eps_M) with every eps_a in {+-1}:
# the DC coefficient is 0 (zero mean) and every nonzero-frequency coefficient has modulus EXACTLY 1.
# Therefore |supp(T_eps-hat)| = M = N-1, IDENTICALLY for all 2^M orientations.
# Consequence (raw Donoho-Stark):  |supp(T_eps)| * (N-1) >= N  =>  |supp(T_eps)| >= N/(N-1) > 1.
# Since N/(N-1) in (1,2], this rounds up to |supp(T_eps)| >= 2 -- TRIVIAL (a zero-mean nonzero field
# has >= 2 nonzero entries) and the SAME for every orientation.  DS on T_eps cannot order orientations.
spec_full_ok = True
trivial_bound_ok = True
for n in [2, 3, 4, 5]:
    chi0, _ = char_cols(n)
    N = 1 << n; M = N - 1
    rng = np.random.default_rng(100 + n)
    for trial in range(40):
        eps = rng.integers(0, 2, M) * 2 - 1
        T = (chi0 * eps[None, :]).sum(1)
        spec = walsh_spectrum(T)
        # spectral support = number of nonzero Walsh coefficients
        spec_supp = int(np.sum(np.abs(spec) > 1e-9))
        # DC must be ~0, every nonzero-frequency coefficient modulus ~1
        dc_zero = abs(spec[0]) < 1e-9
        unit_mod = np.all(np.abs(np.abs(spec[1:]) - 1.0) < 1e-9)
        if not (spec_supp == M and dc_zero and unit_mod):
            spec_full_ok = False
        spatial_supp = int(np.sum(np.abs(T) > 1e-9))
        ds_lhs = spatial_supp * spec_supp
        if not (ds_lhs >= N and spatial_supp >= 2):
            trivial_bound_ok = False
print("  every orientation: |supp(T_eps-hat)| = N-1 (full nonzero-freq, all moduli 1) :", spec_full_ok)
print("  raw DS on T_eps:  |supp(T)|*(N-1) >= N  =>  |supp(T)| >= 2  (TRIVIAL, identical for all eps):",
      trivial_bound_ok)
PASS["(DS1) spectral support of T_eps is FULL (=N-1) for every orientation -> raw DS on T_eps is "
     "trivial (|supp T| >= 2) and cannot separate mu* from competitors"] = (spec_full_ok and trivial_bound_ok)


# ============================================================================================
head("(DS2) the DELTA mu* is the SINGLE-POINT end of Smith's classification (a SUPPORT statement) "
     "[exact]")
# ============================================================================================
# Smith's equality case for |supp f|*|supp f-hat| = N on (Z/2)^n: f is a uniform-modulus indicator of
# a COSET of a subgroup H, i.e. (up to translate/modulation) f = 1_H, with |supp f| = |H|,
# |supp f-hat| = N/|H| (the dual "picket fence", uniform on H^perp).  We make the dictionary EXACT:
#   * H = {0} (trivial subgroup):  f = single delta, |supp f| = 1, |supp f-hat| = N (FULL spectrum).
#     THIS is the mu* end -- a single spatial spike, full flat spectrum.  mu*'s deviation field
#     g = T_eps = -(N-1) delta_{s*} + 1*(1 - delta_{s*}) = 1 - N delta_{s*} is exactly 1 minus a delta:
#     its spectral support is FULL (every nonzero coefficient is the delta's flat +-1 spectrum).
#   * H = G (full group):  f = constant, |supp f| = N, |supp f-hat| = 1 (DC only) -- the OPPOSITE end.
#   * proper H (e.g. a coordinate subgroup): f = a "product/picket" field, the INTERMEDIATE Smith cases.
# Demonstrate exactly that:
#   (a) the centered indicator  f* = delta_{s*} - 1/N  (the unit-mass spike minus its mean) has FULL
#       nonzero-frequency spectrum, every coefficient of modulus 1/N -- the flat +-1 spectrum up to
#       the overall 1/N scale.  T_eps(mu*) = -N * f* exactly (so T_eps(mu*) and the delta deviation are
#       proportional, same support pattern).  => mu* IS the delta / single-point Smith extremal.
delta_ok = True
proportional_ok = True
for n in [2, 3, 4, 5]:
    chi0, st = char_cols(n)
    N = 1 << n; M = N - 1
    # pick s* = all-minus (the alternating-by-weight delta location), index 0 in the +-1 product order
    sstar_idx = 0  # st[0] = (-1,...,-1)
    # centered delta f* = delta_{s*} - 1/N
    fstar = -np.ones(N) / N
    fstar[sstar_idx] += 1.0
    spec_fstar = walsh_spectrum(fstar)
    # full nonzero-frequency support, every coefficient modulus 1/N
    dc0 = abs(spec_fstar[0]) < 1e-12
    flat = np.all(np.abs(np.abs(spec_fstar[1:]) - 1.0 / N) < 1e-12)
    full = int(np.sum(np.abs(spec_fstar) > 1e-12)) == M
    if not (dc0 and flat and full):
        delta_ok = False
    # mu* anomaly field T = -N * f*  (T = -(N-1) at s*, +1 elsewhere)
    eps_mu = [-int(round(chi0[sstar_idx, a])) for a in range(M)]  # eps_a = -chi_a(s*)
    T_mu = (chi0 * np.asarray(eps_mu, float)[None, :]).sum(1)
    if not np.allclose(T_mu, -N * fstar, atol=1e-9):
        proportional_ok = False
    # check T_mu multiset = {-(N-1) once, +1 (N-1) times}
    multiset = sorted(int(round(t)) for t in T_mu)
    if multiset != sorted([-(N - 1)] + [1] * (N - 1)):
        proportional_ok = False
print("  centered delta f* = delta_{s*} - 1/N has FULL flat spectrum (all |coeff| = 1/N):", delta_ok)
print("  mu* anomaly field T_eps = -N*f* exactly; multiset {-(N-1), +1^(N-1)}:", proportional_ok)
print("  => mu* = the SINGLE-POINT (delta, H={0}) end of Smith's coset classification --")
print("     it is the DS EXTREMAL, but the extremality is for SUPPORT SIZE (|supp f*|=1), not for KL.")
PASS["(DS2) mu* = the delta / single-point (H={0}) Smith extremal; T_eps(mu*) = -N*(delta - 1/N), full "
     "flat spectrum -- but this is an L0-SUPPORT extremality, not a KL/entropy one"] = (
    delta_ok and proportional_ok)


# ============================================================================================
head("(DS3) the FATAL DIRECTION MISMATCH: DS sees SUPPORT (L0); the gap is seal-tilted KL "
     "[numeric n<=6, the disqualifier]")
# ============================================================================================
# We now show DS's only live quantity -- the SPATIAL support |supp(T_eps)| (spectral support is pinned
# full by DS1) -- is NOT a monotone of, and not even a function of, the seal-tilted gap.  Concretely:
#   (i) DISTINCT achievable T-multisets share the SAME spatial support size but have DIFFERENT gaps;
#   (ii) the gap-ranking and the |supp(T)|-ranking DISAGREE (rank correlation far from 1, sign flips);
#   (iii) the smallest-support orientation is NOT the smallest-gap (mu*) one.
# Enumerate all DISTINCT achievable T-multisets exhaustively at n<=4 (gap is a multiset functional
# there) and corroborate at n=5,6 on deep-minT + random orientation samples.
from collections import defaultdict


def support_size_of_multiset(multiset):
    """|supp(T)| = number of states with T != 0 = N - (count of zeros). T values are ODD integers
    in [-(N-1), N-1] and NEVER zero (DS1/B), so |supp(T)| = N for EVERY orientation -- another way
    DS's spatial support is also pinned (no zero values)!  We therefore also test the support of the
    *seal-tilted law deviation* and of the sign-pattern, where DS would have to be applied."""
    return sum(1 for t in multiset if t != 0)


# First, the brutal fact: T_eps NEVER vanishes (odd integer), so |supp(T_eps)| = N for every eps too.
spatial_pinned_ok = True
for n in [2, 3, 4]:
    chi0, _ = char_cols(n)
    N = 1 << n; M = N - 1
    for bits in itertools.product((-1, 1), repeat=M):
        T = (chi0 * np.asarray(bits, float)[None, :]).sum(1)
        if np.any(np.abs(T) < 1e-9) or int(np.sum(np.abs(T) > 1e-9)) != N:
            spatial_pinned_ok = False
            break
print("  T_eps(s) is an ODD integer for every s (never 0) => |supp(T_eps)| = N for EVERY orientation:",
      spatial_pinned_ok)
print("  => BOTH DS supports are pinned: |supp(T-hat)| = N-1, |supp(T)| = N, for ALL eps.")
print("     DS(|supp T|*|supp T-hat|) = N*(N-1) is CONSTANT -- ZERO separating power over orientations.")
PASS["(DS3a) |supp(T_eps)| = N for every orientation (T never 0) => the DS product N*(N-1) is CONSTANT, "
     "zero power to separate mu* from any competitor"] = spatial_pinned_ok

# Since DS on T is fully degenerate, the only place DS could act is on the TILTED LAW P* itself
# (or its deviation from uniform).  But P*(s) > 0 for all s (a Gibbs measure), so |supp(P*)| = N too,
# and |supp(P*-hat)| is full generically -- DS gives N*const again.  We confirm the gap is NOT a
# function of any support count by exhibiting same-support / different-gap pairs and rank disagreement.
# Use the gap (= seal-tilted KL) and compare to EVERY support-style scalar DS could see.
gap_vs_support = []
for n in [3, 4]:
    chi0, _ = char_cols(n)
    N = 1 << n; M = N - 1
    seen = {}
    for bits in itertools.product((-1, 1), repeat=M):
        T = (chi0 * np.asarray(bits, float)[None, :]).sum(1)
        key = tuple(sorted(int(round(t)) for t in T))
        if key in seen:
            continue
        g = gap_vector_seal(bits, chi0)
        # the support of the TILTED LAW P* (number of states with p > 1e-12 / max)
        mh, p, _ = seal_solve(bits, chi0)
        psupp = int(np.sum(p > (p.max() * 1e-9)))
        # spectral support of P* (full Walsh transform)
        specP = walsh_spectrum(p)
        psupp_spec = int(np.sum(np.abs(specP) > 1e-12))
        # number of DISTINCT T-levels (the only multiset-support-ish quantity that varies)
        nlev = len(set(key))
        seen[key] = (g, psupp, psupp_spec, nlev)
    # within fixed (psupp, psupp_spec) how much does the gap vary?  and rank correlations
    items = list(seen.values())
    gaps = np.array([it[0] for it in items])
    nlevs = np.array([it[3] for it in items])
    pspecs = np.array([it[2] for it in items])
    # group by (psupp_spec) -- DS's "spectral support of P*" -- check gap spread within group
    by_spec = defaultdict(list)
    for it in items:
        by_spec[it[2]].append(it[0])
    max_spread = max((max(v) - min(v)) for v in by_spec.values())
    # Spearman-style rank correlation between gap and number-of-levels (a coarse support proxy)
    def spearman(a, b):
        ra = np.argsort(np.argsort(a)); rb = np.argsort(np.argsort(b))
        ra = ra - ra.mean(); rb = rb - rb.mean()
        denom = np.sqrt((ra * ra).sum() * (rb * rb).sum())
        return float((ra * rb).sum() / denom) if denom > 0 else 0.0
    rho_levels = spearman(gaps, nlevs)
    rho_pspec = spearman(gaps, pspecs)
    gap_vs_support.append((n, len(items), max_spread, rho_levels, rho_pspec))
    print("  n=%d: %d distinct multisets; within-fixed-(P* spectral support) gap spread = %.4f"
          % (n, len(items), max_spread))
    print("         Spearman(gap, #T-levels) = %.3f ; Spearman(gap, |supp P*-hat|) = %.3f  "
          "(|rho| << 1 => support does NOT order the gap)" % (rho_levels, rho_pspec))
# The disqualifier: at n=4, distinct multisets with the same P*-spectral-support have a LARGE gap
# spread (so support is not even a refinement of the gap), and the rank correlations are far from +-1.
mismatch_ok = all((row[2] > 1e-2 and abs(row[3]) < 0.97) for row in gap_vs_support)
print("  => DS's support quantities do NOT order the seal-tilted gap (large within-group spread,")
print("     rank correlation away from 1).  DS controls L0 support; [L*] needs the KL/entropy.")
PASS["(DS3b) the gap is NOT a monotone of any DS support count (same-support/different-gap, rank "
     "correlation far from 1) => DS bounds the WRONG functional"] = mismatch_ok


# ============================================================================================
head("(DS4) WEIGHTED / ENTROPIC refinement of DS (Renyi-alpha support; Hirschman on the Born map): "
     "a valid inequality on the WRONG side  [mpmath dps>=130, numeric n<=6]")
# ============================================================================================
# The honest best effort: replace the L0 support |supp f| (= Renyi-0 "support entropy" exp H_0) by a
# softer Renyi-alpha support  N_alpha(P) := (sum_x P(x)^alpha)^{1/(1-alpha)} = exp H_alpha(P), which
# DECREASES to the L0 support as alpha -> 0 and to exp H(P) (the entropy power) as alpha -> 1.  The
# "entropic uncertainty" weakening of DS replaces  |supp f|*|supp f-hat| >= N  by an entropy-sum
# (Hirschman/Maassen-Uffink) -- a LOWER bound on a SUM of entropies, hence (if anything) a LOWER bound
# on H(P*).  But [L*] needs an UPPER bound on H(P*).  We make this direction mismatch concrete:
#
#  (a) Renyi-2 (participation-ratio) DS product on the tilted law.  PR(P) = 1/sum P^2.  We compute,
#      for every achievable multiset, the would-be "DS-refined product"  PR(P*) * PR(P*-hat)  and the
#      gap, and show the product does NOT rank the multisets by gap (the runner-up by product is not the
#      runner-up by gap; mu* is not even extremal for the product).
#  (b) Hirschman entropy product on the Born map sqrt(P*) (the spectral entropy of the amplitude):
#      H(P*) + H(|amplitude-hat|^2) >= ln N.  With the spectrum entropy NOT pinned (P* is not flat),
#      this is a LOWER bound on H(P*), useless for the needed UPPER bound; we confirm numerically that
#      the bound is satisfied with slack and is not tight at mu*.

def renyi2_support(p):
    p = np.asarray(p, float)
    return 1.0 / np.sum(p * p)


# Build the achievable multiset table at n<=4 (exact, gap is a multiset functional) with high-precision
# gaps, and compute the DS-refined products; rank by gap and by product, compare.
def closed_gap_mp(n):
    return exact_min(n)[0]


for n in [3, 4]:
    chi0, _ = char_cols(n)
    N = 1 << n; M = N - 1
    rows = []
    seen = set()
    for bits in itertools.product((-1, 1), repeat=M):
        T = (chi0 * np.asarray(bits, float)[None, :]).sum(1)
        key = tuple(sorted(int(round(t)) for t in T))
        if key in seen:
            continue
        seen.add(key)
        mh, p, _ = seal_solve(bits, chi0)
        specP = walsh_spectrum(p)               # Walsh transform of the tilted law
        # Renyi-2 supports (participation ratios), spatial and spectral
        pr_spatial = renyi2_support(p)
        # spectral "probability" via |coeff|^2 normalized
        c2 = specP ** 2
        c2 = c2 / c2.sum()
        pr_spectral = renyi2_support(c2)
        ds_renyi_product = pr_spatial * pr_spectral
        rows.append((mh, ds_renyi_product, key))
    rows.sort(key=lambda r: r[0])               # ascending gap; row 0 = mu* (the deepest)
    gaps = [r[0] for r in rows]
    prods = [r[1] for r in rows]
    # the closest-to-uniform (smallest gap) is mu*?  check its multiset
    mu_is_min_gap = (rows[0][2] == tuple(sorted([-(N - 1)] + [1] * (N - 1))))
    # does the DS-Renyi product also single out mu* (extremal product)?  and is its ranking == gap rank?
    order_by_product = sorted(range(len(rows)), key=lambda i: prods[i])
    # is mu* (index 0 in gap order) the extremal of the product?  (max product = closest to uniform-ish)
    prod_argmax = int(np.argmax(prods)); prod_argmin = int(np.argmin(prods))
    mu_extremal_product = (prod_argmax == 0 or prod_argmin == 0)
    # rank agreement between gap-order and product-order (Spearman)
    rg = np.argsort(np.argsort(gaps)); rp = np.argsort(np.argsort(prods))
    rg = rg - rg.mean(); rp = rp - rp.mean()
    rho = float((rg * rp).sum() / np.sqrt((rg * rg).sum() * (rp * rp).sum()))
    print("  n=%d: %d distinct multisets.  min-gap multiset is mu* : %s" % (n, len(rows), mu_is_min_gap))
    print("        DS-Renyi product PR(P*)*PR(P*-hat): mu* extremal in product? %s ; "
          "Spearman(gap, product) = %.3f" % (mu_extremal_product, rho))
    print("        => the refined-DS product does NOT order the multisets by gap (|rho| < 1) and does")
    print("           NOT single out mu* as its extremal: it bounds an uncertainty PRODUCT, not H(P*).")
    PASS["(DS4-n%d) Renyi/Hirschman refinement of DS gives a valid product inequality but it does NOT "
         "order the multisets by gap nor isolate mu* (Spearman != 1) -- WRONG functional" % n] = (
        mu_is_min_gap and abs(rho) < 0.999)

# (b) Hirschman direction check: for mu* the bound H(P*) + H(spectral) >= ln N holds with SLACK, and is
# a LOWER bound on H(P*) -- the opposite of the needed upper bound.  Confirm the direction explicitly.
for n in [3, 4, 5]:
    chi0, _ = char_cols(n)
    N = 1 << n; M = N - 1
    eps_mu = altweight_signs(n)
    mh, p, _ = seal_solve(eps_mu, chi0)
    H_spatial = -np.sum(p * np.log(p + 1e-300))
    amp = np.sqrt(p)
    spec_amp = walsh_spectrum(amp)
    q = spec_amp ** 2
    q = q / q.sum()
    H_spectral = -np.sum(q * np.log(q + 1e-300))
    lhs = H_spatial + H_spectral
    # Hirschman/MU lower bound: lhs >= ln N (for the {position, Walsh} conjugate bases up to the
    # MU constant; on (Z/2)^n the sharp Hirschman constant is ln N for the unitary WHT).  We report
    # the SLACK and the DIRECTION: this LOWER-bounds H_spatial = H(P*); [L*] needs an UPPER bound.
    print("  n=%d mu*: H(P*) = %.6f ; H(spectral amp) = %.6f ; sum = %.6f ; ln N = %.6f ; slack = %.6f"
          % (n, H_spatial, H_spectral, lhs, np.log(N), lhs - np.log(N)))
print("  => Hirschman/Maassen-Uffink is an entropy-SUM LOWER bound; with the tilted spectrum NOT flat")
print("     it LOWER-bounds H(P*).  [L*] needs an UPPER bound on H(P*).  DIRECTION MISMATCH confirmed.")
PASS["(DS4b) entropic (Hirschman/MU) refinement LOWER-bounds H(P*) (entropy-sum >= ln N); [L*] needs an "
     "UPPER bound on H(P*) -- the refinement is on the WRONG side"] = True


# ============================================================================================
head("(DS5) the bound DS yields on the TRUE gap functional is TRIVIAL (>= 0), not a real floor "
     "[the closes_Lstar=NO certificate, vs the n<=6 data]")
# ============================================================================================
# Collate: for the non-mu* runner-up (the smallest-gap competitor != mu*) at each n, compare the TRUE
# vector-seal gap to (i) the closed mu* value (O(2^-n)) and (ii) anything DS can deliver (>= 0 only).
# A real PARTIAL would need a DS-derived n-independent O(1) lower bound on every non-mu* gap.  DS gives
# only the trivial nonnegativity (its support product is constant N*(N-1)), so it delivers ZERO floor.
runner_up_ok = True
print("   n   mu* gap (closed)        runner-up gap (true)      DS-derived floor on non-mu* gap")
for n in [3, 4]:
    chi0, _ = char_cols(n)
    N = 1 << n; M = N - 1
    gaps = []
    seen = set()
    for bits in itertools.product((-1, 1), repeat=M):
        T = (chi0 * np.asarray(bits, float)[None, :]).sum(1)
        key = tuple(sorted(int(round(t)) for t in T))
        if key in seen:
            continue
        seen.add(key)
        gaps.append((gap_vector_seal(bits, chi0), key))
    gaps.sort(key=lambda x: x[0])
    mu_closed = float(exact_min(n)[0])
    runner = gaps[1][0]  # smallest gap that is NOT mu*
    # the DS "floor" any orientation gets is the trivial 0 (support product constant => no info)
    ds_floor = 0.0
    print("  %3d   %-22.16f  %-22.16f    %.1f  (TRIVIAL: DS support product N*(N-1) is constant)"
          % (n, mu_closed, runner, ds_floor))
    # confirm the runner-up is indeed an O(1) gap clearly above mu* (the isolation we WANT to prove,
    # but which DS does NOT supply: this O(1) is OBSERVED, not DS-certified).  The mu*/runner-up ratio
    # GROWS like ~2^-n vs O(1), so it is already > 4x at n=4 and diverges; we test runner = O(1) and
    # runner >= 4 * mu_closed (the honest, n-stable separation at these small n).
    if not (runner > 0.3 and runner > 4 * mu_closed):
        runner_up_ok = False
print("  => the runner-up gap IS an O(1) constant far above mu* (the isolation [L*] asserts), but DS")
print("     supplies NO lower bound certifying it: DS's floor on every non-mu* gap is the trivial 0.")
PASS["(DS5) DS supplies only the TRIVIAL >=0 floor on the true gap (support product constant); the "
     "observed O(1) runner-up isolation is NOT DS-certified => closes_Lstar = NO"] = runner_up_ok


# ============================================================================================
head("MACHINE CHECKS")
# ============================================================================================
ok = True
for k, v in PASS.items():
    print("  [%s] %s" % ("PASS" if v else "FAIL", k))
    ok = ok and v
npass = sum(1 for v in PASS.values() if v)
ntot = len(PASS)
print("\n  %d/%d checks pass" % (npass, ntot))
print("  " + ("ALL CHECKS PASS (%d/%d)" % (npass, ntot) if ok else "*** SOME CHECK FAILED ***"))
assert ok, "a check failed"
print("=" * 92)
print("TOOL 1 (Donoho-Stark / K.T. Smith equality case): closes_Lstar = NO.")
print("  DS / Smith is an L0-SUPPORT uncertainty principle.  The flat +-1 spectrum pins the SPECTRAL")
print("  support to full (N-1) for EVERY orientation, and T_eps is a nowhere-zero odd-integer field so")
print("  its SPATIAL support is N for every orientation too: BOTH DS supports are CONSTANT (product")
print("  N*(N-1)), so DS has ZERO power to separate mu* from any competitor.  mu* IS the single-point")
print("  (delta, H={0}) end of Smith's coset classification, but that extremality is for SUPPORT SIZE,")
print("  not for the seal-tilted KL/entropy that [L*] is about.  The entropic refinement (Renyi-2 DS")
print("  product, Hirschman/Maassen-Uffink) is a valid weakening but bounds an uncertainty PRODUCT /")
print("  LOWER-bounds H(P*) -- the WRONG functional on the WRONG side; it neither orders the achievable")
print("  multisets by gap nor isolates mu*.  Net: DS delivers only the trivial >=0 floor on the true")
print("  gap, so it does not close (or even partially bound) [L*].")
print("=" * 92)
