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
