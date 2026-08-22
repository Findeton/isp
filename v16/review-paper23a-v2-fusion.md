# Paper 23a v2 blind review — Seat F (algebra)

Date: 2026-08-22

Reviewer seat: algebraic structure of the class product. Repo
read-only; produced solely from the v2 pin (#315), the candidate
(#316, SHA-256
`c4503bd309bcc54f0c20de2d8f1a28b4b4742c02c5f9eb7d7b2918deb5889209`),
the construction note
(`26d2134a839f79905a0374690df6592412fc1c30352a7cac81bd3103c3ce2085`),
terminal Paper 13D, and the #314 adjudication. No other v2 seat's
report seen.

Verdict: **ACCEPT-WITH-FIXES**

The honest classification is a real result: the certified fixtures
carry a commutative unital carrier-graded nonassociative magma, and
the FP bootstrap route closes for the present law. Two repairs, one
of which touches a proof's completeness.

## F-F2.1 (MAJOR) — Proposition G's proof has a gap at the last step

Defect. Proposition G (commutativity) argues that the braiding
transports the diagonal comparison object of the two fused complexes
"identically componentwise, so both sides satisfy the same
comparisons against every third complex; being congruent to each
other, they are equal classes." Two gaps: (i) the argument as printed
shows each side compares equally against every third complex — that
gives equality of their comparison profiles, and the inference to
$\chi\sim\chi'$ needs the (true but unstated) fact that the diagonal
comparison separates any two incongruent complexes, i.e. that some
third complex or reader cell distinguishes them; (ii) "being
congruent to each other" is the conclusion, not a premise — the
sentence is circular as printed.

Replacement sentences for the end of Proposition G's proof, verbatim:

> The braiding map transports the diagonal comparison object of
> $(\Phi(\chi\boxtimes\chi'),\,\Phi(\chi'\boxtimes\chi))$ identically
> componentwise, so the two pushed laws have identical comparison
> profiles against every aligned third complex and reader. Since the
> diagonal comparison separates any two complexes that are not
> congruent — by definition, incongruence means some comparison cell
> distinguishes them — equal profiles force congruence:
> $[\chi]\otimes[\chi']=[\chi']\otimes[\chi]$. ∎

## F-F2.2 (MODERATE) — §4.1's tag should record the empty-carrier corner

Defect. The classification tag
`P23AV2-ALGEBRA-COMMUTATIVE-UNITAL-GRADED-NONASSOCIATIVE-MAGMA` is
correct for the full family, but §4.1 does not note the one
associative substructure that does exist: the trivial submagma
$\{\mathbf 1\}$, and more generally the empty-carrier corner, where
Proposition H's counterexample cannot live. Recording this prevents
an overreading of "nonassociative" and is exactly the kind of scope
note the v1 rejection demanded.

Replacement sentence, verbatim:

> The only associative submagmas are trivial: any submagma in which
> associativity can fail must contain two nonempty-carrier classes,
> and bracketing then separates by Proposition H; the empty-carrier
> corner $\{\mathbf 1\}$ is trivially associative, and no nontrivial
> associative quotient or substructure exists on the certified
> fixtures.

## F-F2.3 (MINOR) — §4.2's closure coordinate should name its negation

Defect. `P23AV2-FP-BOOTSTRAP-ROUTE-CLOSED-FOR-PRESENT-GAMMA` is
earned; the pin also pre-registered `-OPEN`. One sentence should
state explicitly that `-OPEN` is not earned and why, for the record's
completeness.

Replacement sentence, verbatim:

> The coordinate `P23AV2-FP-BOOTSTRAP-ROUTE-OPEN` is not earned: no
> associative class product exists on the certified fixtures, so
> there is no ring for a character to live on, and no accepted or
> proposed object before this unit supplies one.

## Mandatory regressions

- Control 19 (rescue quotient): no coarser quotient anywhere;
  bracketing classes stay distinct even at the cost of
  associativity. PASS.
- Control 20: Prop H is the refutation; nothing promotes
  target-level equality. PASS.
- Control 21 (commutativity unproved): Prop G proves it — after the
  F-F2.1 repair, fully. CONDITIONAL-PASS.
- Control 22 (FP closure overstatement): §4.2's scope engraving is
  exact; the salvage paragraph names what a future law could change.
  PASS.
- Controls 15, 16, 17: no semiring asserted (refuted first); no
  character equation exists; no dimensions claimed. PASS.
- Controls 3, 14: out of mandate; tables cross-checked anyway, all
  values reproduce. PASS.

## Independent verification performed

Rebuilt the class product on the honest family and checked each
clause: well-definedness via Theorem A composition; carrier
additivity (sizes 0–4, symbolic); finite escape (unbounded); the
bracketing counterexample of Proposition H against the frontier
lists (({1},{2}),({1,2},{3}) vs ({2},{3}),({1},{2,3})); the unit
clause against §10.2's empty-family semantics; the no-duals argument
from carrier additivity; the FP closure's logical dependence on
Proposition H (verified: every character-equation route requires
associativity). Confirmed the eight earned outcome names match the
pin's pre-registered list verbatim and the five not-earned names are
correctly recorded. All arithmetic exact rationals.

## Verdict

ACCEPT-WITH-FIXES: apply F-F2.1, F-F2.2, F-F2.3 verbatim. The
classification then stands: commutative unital carrier-graded
nonassociative magma; FP bootstrap route closed for the present
$\Gamma_D$ fixtures. No outcome name is touched by the repairs.
