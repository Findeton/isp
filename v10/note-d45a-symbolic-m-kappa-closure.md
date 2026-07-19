# D45a — the symbolic-m closure of kappa: from verified-on-hull to derived-for-all-m

**Status:** CAMPAIGN PIN (strict), 2026-07-19; user-authorized ("go
ahead" on the two-unit proposal).  Parents: D44d TERMINAL #353 (the
quartic kappa(m) = (9m^4 - 15m^2 + 4)/144 verified with zero
tolerance on the 28-point hull [1/16, 2]; the hull caveat = this
unit's target); the d43a/d44d series machinery.  Receipt:
`v10/code/d45a_symbolic_kappa_exact.py`.

## 1. The target

**[TARGET] Derive kappa(m) as an exact identity valid for ALL m** by
running the committed identification pipeline with the mass as a
FORMAL VARIABLE — matrix entries become polynomials in m over exact
rationals — upgrading the terminal statement from [EXACT on the
hull] to [THEOREM at fixture scale, all m], and deliver the
STRUCTURAL ORIGIN of the factorization (3m^2 - 1)(3m^2 - 4): which
tau channels carry which polynomial factors, and how the
delta-weighted combination produces the quartic.

## 2. Feasibility facts (checked pre-pin, 2026-07-19)

- Mass enters the Hamiltonian ONLY linearly on the diagonal (the
  committed d44d receipt's addH(..., m * wm) lines); hopping is
  m-free.  At ORD 4 every series coefficient entry is a polynomial
  in m of degree <= 4.
- The Neumann inversion of Gamma(U_free) is a Delta-series whose
  Delta^0 term is the identity — no division by m-dependent
  quantities anywhere; entries stay POLYNOMIAL in m with rational
  coefficients (divisions are by integer constants only).
- kappa itself is the delta-weighted tau combination — a polynomial
  in m over Q (the identified quartic/144 IS a polynomial).  The
  d44d "rational function" scan found it in the polynomial family.

## 3. Gates (pre-registered)

- **YG0 (regression):** the symbolic pipeline EVALUATED at m = 1/2
  and m = 1 reproduces 13/2304 and -1/72 exactly, and at >= 3 more
  committed grid masses reproduces the committed KTAB values.
- **YG1 (THE DERIVATION):** the symbolic tau tables (each channel
  entry a polynomial in m) and the symbolic collapse: EXC D =
  1 . (I - sigma_x) IDENTICALLY in m; LT D = kappa(m) . (I -
  sigma_x) with kappa(m) - (9m^4 - 15m^2 + 4)/144 == 0 AS A
  POLYNOMIAL (every coefficient zero) — the all-m identity.
- **YG2 (the ray identity in m):** all off-ray components of both
  rules' identified operators vanish as POLYNOMIALS in m (not
  per-mass) — the collapse is an all-m theorem.
- **YG3 (structural origin):** print each tau channel's exact
  polynomial in m; the delta-weighted combination; its
  factorization — the "why (3m^2 - 1)(3m^2 - 4)" content delivered
  as the exhibited polynomial algebra [EXACT].
- **YG4 (purity + determinism):** NO floats anywhere — pure
  Fraction-coefficient polynomial arithmetic; the banner is
  tolerance-free; rerun byte-identical.

Failure modes (pre-registered, deliverable): if any pipeline stage
is provably non-polynomial in m, exhibit the stage — that is a
finding about the identification, not a receipt failure; if the
polynomial identity FAILS, the hull-verified quartic and the
symbolic pipeline disagree — deliver both objects exactly (a
reversal-class result; the committed 28-point verification bounds
where the truth can lie).

## 4. Scope

The singleton identification at ORD 4, L = 12 (sufficient for the
identity; the slab arms are m-pointwise-verified at #353 and
inherit by A5's weight-independence note — re-running them
symbolically is optional and declared either way).  No claim beyond
the fixture; the smeared interacting successor (with its g = 0
column) is untouched by this unit.

## 5. First-run amendments (2026-07-19, pre-round)

**A1 (declared inert deviations).** Exact-zero dropping replaces the
committed pipeline's numeric dust drops (inert: exact arithmetic);
the slab arms are NOT re-run symbolically (pin §4's optional clause
taken — they inherit pointwise per #353 + its A5
weight-independence note). The division audit confirmed while
porting: only integer-constant divisions anywhere; the pin's
non-polynomial failure mode was structurally excluded.

**A2 (one gate beyond the pin: YG3-C).** Channel-factorization
identities by exact expansion — the sharpened "which channels carry
which factors" deliverable: in the FLIP sector (3m^2 - 1) is a
common factor of EVERY channel (tau(+-1,f) = -+(3m^2-1)(24m^2-5)/2304;
tau(+-3,f) = +-(3m^2-1)/256), so m^2 = 1/3 kills every flip channel
IDENTICALLY, while (3m^2 - 4) emerges only in the combination
2 tau(1) + 6 tau(3) = -kappa(m); in the SAME sector no single
channel factorizes (tau(+-2,s) = +-(36m^4-60m^2+7)/2304 irreducible
over Q, disc 2592) — the constant tau(+-4,s) = +-1/512 shifts the
bracket 7 -> 16, creating 4(3m^2-1)(3m^2-4). The two zero crossings
have DIFFERENT channel origins: m^2 = 1/3 is a per-channel kill;
m^2 = 4/3 exists only in the weighted sums.

## 6. Round-1 amendments (2026-07-19; round frozen at
## reviews/d45a-round1-hostile-review.md: PASS-AS-RESCOPED,
## 0B/1M/2m/4n; all headlines survived a from-scratch sympy rebuild
## + 8 out-of-hull masses on two engines + 10/10 mutants)

**B1 (MAJOR-1 — a check(True) violation, OWNED).** YG4-B as
committed at #357 was check(..., True) — unfalsifiable by
construction, in direct violation of the no-check(True) law this
program convicted at d43b F-B3, and it passed MY pre-commit
verification (the PASS-count check does not catch gate vacuity —
noted for the verification protocol). Every content claim behind it
was true (referee-verified externally), but the gate was not a
gate. REPAIRED: YG4-B is now a token-level source self-scan
(tokenizer excludes strings/comments so the probe cannot
self-trip): no banned name {TOL, mpmath, random, datetime, getenv,
environ}, no float/complex NUMBER literal (421 integer tokens
scanned); byte-identity remains an external protocol line, no
longer inside any gate's claim. #357's "GREEN 20/20" reading is
forward-corrected at #360: as-committed it was 19 computed + 1
declared; as-repaired it is 22 computed.

**B2 (minor-1 — the irreducibility inference scoped).** The disc
route decides irreducibility only AS A QUADRATIC IN x = m^2; the
print now says so, and a biquadratic m-split check (m^2 +- cm + d
over Q, c != 0: d^2 = a0/a2, 2d - c^2 = a1/a2) runs and returns
NONE — tau(2,same)'s numerator is irreducible over Q in m as well,
now by receipt computation (the round had proved it externally).

**B3 (minor-2 — the Neumann preconditions gated).** PIPE-3 gates
Delta^1-freeness of Gamma(U_free); PIPE-4 gates
Gfi . Gamma(U_free) == I as a truncated series — closing the
single-gate margin the round exhibited with its M5 mutant.

**B4 (nits).** YG4-A's walk now includes U_free and Gamma_free;
YG2-B now covers LT site 5; YG3-A's label says "recombined from
the retained channel objects" (the independent rebuild is the
frozen round's). Receipt now 22 PASS / 0 FAIL.
