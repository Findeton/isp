# Paper 23a v2 adjudication

Date: 2026-08-22

Disposition: **ACCEPT-WITH-FIXES — BOUNDED PROSE REPAIR ORDERED;
TERMINAL PENDING REPAIR VERIFICATION**

This is the joint adjudication of the three frozen v2 seats. It
confirms each finding, orders the bounded repair (nine replacement
sentences across nine findings, all prose), and states what terminal
status will mean. It constructs nothing.

## 1. Bound corpus

| object | ordinary SHA-256 |
|---|---|
| P23a v2 pin (#315) | `26587fb58f4f30eb52f9daff725d547ba1d7547ead6f1255ce2ae2a83d0b5dd7` |
| P23a v2 candidate (#316) | `c4503bd309bcc54f0c20de2d8f1a28b4b4742c02c5f9eb7d7b2918deb5889209` |
| v2 construction note | `26d2134a839f79905a0374690df6592412fc1c30352a7cac81bd3103c3ce2085` |
| Seat C (#317) | `9dbad9be6e1174d25ddff4ee6de84116148b23e1126e3c33529c1529ae417184` |
| Seat P (#318) | `d569bb3b3cc6ec3ea05f52bc1e4120c7eb3491552a6110136140c930a73d8b79` |
| Seat F (#319) | `c9e69c23c7773668638320d1e0919f848ce668bb1ef4ec555d2bc3bdaf236af3` |

## 2. Finding dispositions

All three seats returned ACCEPT-WITH-FIXES. Every finding is
confirmed by the adjudicator's own rebuild:

| finding | seat | severity | disposition |
|---|---|---|---|
| Prop I "pointwise equality" overstates across canonically identified type annotations | C F-C2.1 | MAJOR | CONFIRMED; replacement adopted verbatim |
| Thm A(2) sort hypothesis implicit | C F-C2.2 | MODERATE | CONFIRMED; replacement adopted verbatim |
| §2.2 fixture inventory open-ended "etc." | C F-C2.3 | MINOR | CONFIRMED; replacement adopted verbatim |
| Composite-class mass sentence kernel-level instead of orbit-sum | P F-P2.1 | MAJOR | CONFIRMED; replacement adopted verbatim |
| Chain-collapse remark ambiguous | P F-P2.2 | MINOR | CONFIRMED; replacement adopted verbatim |
| Prop G commutativity proof circular last step | F F-F2.1 | MAJOR | CONFIRMED — the printed argument does assume its conclusion; the supplied equal-profiles + separation lemma form is correct and adopted verbatim |
| Associative-substructure scope note missing | F F-F2.2 | MODERATE | CONFIRMED; replacement adopted verbatim |
| `-OPEN` coordinate negation unstated | F F-F2.3 | MINOR | CONFIRMED; replacement adopted verbatim |

No seat found any structural defect: the trace-sensitive class family,
the nonassociativity counterexample, carrier monotonicity, and the
FP-route closure survived independent rebuilding by all three seats.
The mandatory regressions passed at every seat (control 21
conditional on F-F2.1's repair, which this adjudication orders).

## 3. Ordered repair

Exactly the eight findings' replacement sentences, applied to
candidate §§2–4 as located by the seats. No number, definition,
outcome name, control disposition, or scope wall may move. The repair
is bounded prose substitution in the v3-repair sense of #306/#307:
the pre-repair bytes remain recoverable at hash `c4503bd3…`.

## 4. Terminal meaning after verified repair

On verification that the diff contains exactly the eight ordered
replacements and nothing else, this unit closes **TERMINAL —
ACCEPT-WITH-SCOPE** with these coordinates:

```text
P23AV2-SECTOR-CONGRUENCE-TRACE-SENSITIVE-CONSTRUCTED
P23AV2-MULTIPLICITY-DESCENT-REPAIRED-CONSTRUCTED
P23AV2-FINITE-CLOSURE-FAILS-BY-CARRIER-MONOTONICITY
P23AV2-CLASS-PRODUCT-NONASSOCIATIVE
P23AV2-CLASS-PRODUCT-COMMUTATIVE
P23AV2-DUALS-ABSENT
P23AV2-ALGEBRA-COMMUTATIVE-UNITAL-GRADED-NONASSOCIATIVE-MAGMA
P23AV2-FP-BOOTSTRAP-ROUTE-CLOSED-FOR-PRESENT-GAMMA
```

at certified-fixture scope of terminal Paper 13D under the
trace-sensitive congruence. Scope walls unchanged: no channel odds,
opportunity/activity/root law, `Pi_phys`, `Gamma_struct`, chronology,
dimension, metric, gravity, actuality. Paper 17 gate CLOSED. The FP
closure is fixture-scoped, not a global no-go (parent control 40).
Paper 22 v3 remains TERMINAL at #307, untouched, consumed nowhere.

One-strike rule: not applicable to this line (v1's rejection was a
candidate-level refusal; the user authorized this v2 explicitly; no
rule terminates investigability here).

No automatic successor exists. Any later stage (physical channel odds,
opportunity/activity/root, `Pi_phys` via the corrected joint-law
typing) requires explicit authorization and a fresh freeze.

## 5. Next event

Execute the ordered repair; verify byte-exactness; freeze the
post-repair hash forward-only; append the closing ledger entry. Then
update live-state registers.
