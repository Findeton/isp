# Paper 23d review — Seat P (probability/instrument)

Date: 2026-08-22

Disposition: **ACCEPT-WITH-FIXES** (one MAJOR, one MODERATE, one MINOR)

Blind delta review of the #333 construction
(`699fe5b72037f47a6ef93b51af548a7b476a400a94230eb3d3c606bdf95a52e8`,
182 LF) against pin #332 (`112684d6…`) and 13D `3b91766f…`. Lens:
measure-theoretic soundness of the pinned spaces and the joint law.

## Findings

**F-P1 (MAJOR). Lemma B conflates two different constancy claims.** As
written it says Π "is constant on fibers" — but Π is a measure on
$\mathsf{Cpx}$, so it is trivially fiber-constant; what the proof
needs (and Q3(ii) uses) is that the *joint law* assigns identical mass
to every point of $\mathcal F_{[\chi]}$'s realizations, which follows
because the conditional Γ_D is field-blind across decorations. The
printed statement is true but nearly vacuous; the argument that does
the work lives implicitly in Q3(ii). Required repair: restate Lemma B
as "**joint-law decoration blindness**: for all Π∈P and any two
realizations in one fiber, $\Gamma_{\rm struct}$ assigns equal mass to
every jointly measurable event containing them" — citing Lemma C's
field-blindness as the engine.

**F-P2 (MODERATE). §4's projective-consistency clause is invoked but
never used.** Theorem C nowhere needs deletion-consistency of the
Π_N family; carrying it as if load-bearing invites the charge that the
no-go depends on a restriction a cleverer weight might evade. Either
mark projective consistency as used only to define admissibility (and
note the theorem holds for ALL probability measures on
$(\mathsf{Cpx},\Sigma_\chi)$, an extension by monotonicity), or delete
the invocation. Prefer the former — the stronger ∀-statement should be
printed.

**F-P3 (MINOR). Lemma A's formula fragment is garbled.**
"$\frac12((n!)^2+\text{self-swap count})$ restricted to transport-orbit
classes" mixes two counting levels; the exact numbers 2/5/17 are right
(verified independently with `fractions`/`itertools`) but the displayed
expression is not what was computed. Replace by the verified statement:
counts obtained by exhaustive transport+swap saturation at n=2,3,4;
general closed form not needed for the theorem.

## What survived

The #308 disintegration constraint is respected verbatim; the
conditional-mutation control (#5) is correctly aimed via the Paper 17
exogeneity remark. The Q2 analysis (marks forgotten in Cpx; asymmetric-
program complexes still rank-blind) closes the strongest reopening
route this seat could construct independently. Quantifier ledger rows
check against the proofs. Control rows 1–10 PASS (control 2 conditional
on F-P2's repair). Primary outcome `P23D-ORIENTATION-FIBER-INERT`
earned modulo repairs; none structural.
