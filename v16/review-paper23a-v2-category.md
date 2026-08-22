# Paper 23a v2 blind review — Seat C (category)

Date: 2026-08-22

Reviewer seat: category/sector structure. Repo read-only; produced
solely from the frozen v2 pin (#315, SHA-256
`26587fb58f4f30eb52f9daff725d547ba1d7547ead6f1255ce2ae2a83d0b5dd7`),
the candidate (#316, SHA-256
`c4503bd309bcc54f0c20de2d8f1a28b4b4742c02c5f9eb7d7b2918deb5889209`,
387 LF), the construction note
(`26d2134a839f79905a0374690df6592412fc1c30352a7cac81bd3103c3ce2085`),
terminal Paper 13D (`3b91766f…`), and the #314 adjudication whose
replacement sentences this seat checks verbatim. No other v2 seat's
report seen.

Verdict: **ACCEPT-WITH-FIXES**

The trace-sensitive rebuild is sound in structure. Three repairs,
none structural.

## F-C2.1 (MAJOR) — Proposition I's proof overstates "pointwise equality"

Defect. Proposition I (unit) claims the fused-with-empty history
"equals the original history pointwise." Strictly, the fused target
boundary object differs in type annotation: it carries the union
carrier presentation and an empty second component slot in the
generator's indexing family. The histories are equal in every
physical field but are presented as values of different (canonically
identified) boundary types. The diagonal comparison cannot distinguish
them — which is all the proposition needs — but "pointwise equal"
should not be claimed of objects with distinct type annotations.

Replacement sentences for Proposition I's proof, verbatim:

> **Proof.** The fusion kernel over an empty second component draws
> zero seeds and acts as the identity on every physical field; the
> resulting history agrees with the original in all carried fields
> under the canonical identification of Paper 13D Section 10.2's
> target with its unfused carrier, so no stabilizer translate or
> comparison cell separates them; hence the classes coincide. ∎

## F-C2.2 (MODERATE) — Theorem A(2)'s fusion clause should state its sort hypothesis

Defect. Clause (2) quantifies over "finite same-sort families" only
implicitly via the generator's typing. Make it explicit so the clause
cannot be read over mismatched sorts.

Replacement sentence, verbatim:

> 2. *(simultaneous fusion)* if $\chi_\alpha\sim\chi'_\alpha$ for a
>    finite family all of whose members share one atomic boundary
>    sort $s$ admitting $\Phi_s$, then
>    $\Phi_s(\boxtimes_\alpha\chi_\alpha)\sim
>    \Phi_s(\boxtimes_\alpha\chi'_\alpha)$;

## F-C2.3 (MINOR) — §2.2 composite-class display should name its closure rule

Defect. The displayed composite classes ($[\mathrm T_2(n)]$,
$[\Phi_2(n)]$, "$[\Phi(\mathrm T)](n)$ etc.") end with an open-ended
"etc." that leaves the fixture inventory vague at exactly the point
the v1 rejection punished.

Replacement sentence, verbatim:

> plus the closure of these five families under tensor, single
> simultaneous fusion, and staged words thereof, each such well-typed
> composite counted as one certified fixture class;

## Mandatory regressions

- Control 19 (rescue quotient): checked every definition — no
  quotient coarser than $\sim$ appears; Props C/H keep bracketing
  classes distinct. PASS.
- Control 20 (target-level associativity): Prop H proves
  nonassociativity; no promotion anywhere. PASS.
- Controls 3, 14: Def 3.1 full-orbit sums; tables verified. PASS.
- Controls 15, 16, 17: no semiring claimed before refutation; no
  character equation; FP route closed with scope. PASS.
- Controls 21, 22: commutativity proved at class level (Prop G); FP
  closure scope engraved. PASS.

## Independent verification performed

Rebuilt Definition 2.1's diagonal comparison from Paper 13D §15 and
checked Lemma 2.2's functoriality claim against it; verified
Proposition B's disjoint-orbit argument by explicit transport on the
$n=1$ fixtures; recomputed the frontier-support lists for left/right
bracketing (({1},{2}),({1,2},{3}) vs ({2},{3}),({1},{2,3}) —
non-isomorphic); re-derived primitive-vs-fusion separation; reproduced
all stage-2 mass tables elementwise; checked the six #314 replacement
sentences appear verbatim where required (F-C3 form in Def 2.1 ✓;
deletion clause in Thm A(4) ✓; chain proof in §3 ✓;
$16\times4\times2=128$ census sentence ✓; endpoint hypotheses ✓;
alignment-independence clause ✓). All arithmetic exact rationals.

## Verdict

ACCEPT-WITH-FIXES: apply F-C2.1, F-C2.2, F-C2.3 verbatim. Stages 1–2
and the stage-3 categorical clauses then stand as printed. No scope
wall moves; no outcome name is touched by the repairs.
