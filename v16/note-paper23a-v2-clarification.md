# Paper 23a v2 clarification to the #322 correction

Date: 2026-08-22

Disposition: **FORWARD-ONLY ADJUDICATION CLARIFICATION TO #322 —
FINITE-CLOSURE MECHANISM RE-SPLIT; DUALS COORDINATE REPLACED**

This note clarifies the #322 correction. It constructs nothing, reopens
nothing, orders no repair, and authorizes no v3. Frozen candidate bytes
remain untouched at
`eca8e1670ecf0c02739c6f94c81e9eefe84b1809240efd8ea9bba94bb886820f`.

## 1. Finite-closure failure: scope restriction and second mechanism

Theorem F's printed proof handles only subfamilies containing a
positive-carrier class, and its closing remark that empty-carrier
subfamilies "close trivially" is wrong after the #322 unital withdrawal
($\mathbf 1\otimes\mathbf 1\neq\mathbf 1$). Corrected statement:

**(F′) Carrier-monotonic failure (restricted).** *No finite subfamily of
$\mathsf{Sect}^{ts}_{13D}$ containing a positive-carrier class is closed
under $\otimes$.* Proof unchanged: Lemma E forces unbounded carrier growth.

**(F″) Empty-carrier escape (new, separate).** For the remaining case —
a nonempty finite subfamily all of whose classes have empty carrier —
escape is proved by **trace-vertex grading**. Let $v(\chi)$ be the number
of fusion-generator vertices in $\chi$'s trace shape (Def 2.3). Every
class product traverses exactly one simultaneous fusion generator, so

$$v([\chi]\otimes[\chi']) = v(\chi)+v(\chi')+1,$$

an affine strictly increasing law. Two complexes with different fusion-
vertex counts have non-isomorphic trace shapes, so Proposition B
separates them: no product ever returns to a bounded-vertex class.
Repeated products leave any finite such subfamily after finitely many
steps.

**Global verdict unchanged:** no finite nontrivial subfamily of
$\mathsf{Sect}^{ts}_{13D}$ is closed under $\otimes$ — including
singletons and the empty-carrier corner. The earned coordinate
`P23AV2-FINITE-CLOSURE-FAILS-BY-CARRIER-MONOTONICITY` is hereby read as
**finite-closure failure by carrier-or-trace monotonicity**: carrier
monotonicity on positive-carrier content, trace-vertex monotonicity on
the empty corner. The mechanism attribution is narrowed accordingly;
the negative result itself is unaffected and now fully covered.

## 2. Duals coordinate replaced

Proposition J quantifies over "$y$ with $\mathbf 1$ inside $x\otimes y$".
After #322 withdrew the unit, **no duality predicate is defined** on the
class family: based-ring duality is relative to a unit, and none exists
here. Consequently neither `DUALS-ABSENT` nor `DUALS-PRESENT` is
assertable — absence of duals was a statement inside a predicate that
does not exist.

Corrected coordinate, replacing `P23AV2-DUALS-ABSENT` everywhere:

```text
P23AV2-DUAL-STRUCTURE-INAPPLICABLE  (dual structure UNCONSTRUCTED)
```

meaning: no duality predicate is presently defined on
$\mathsf{Sect}^{ts}_{13D}$; dual structure is neither constructed nor
ruled out, and cannot be discussed until some future accepted object
supplies a unit or an equivalent anchor.

## 3. Retained without change

- Commutativity (`P23AV2-CLASS-PRODUCT-COMMUTATIVE`, Prop G).
- Nonassociativity (`P23AV2-CLASS-PRODUCT-NONASSOCIATIVE`, Prop H).
- Fixture-scoped FP-route closure
  (`P23AV2-FP-BOOTSTRAP-ROUTE-CLOSED-FOR-PRESENT-GAMMA`): depends only
  on associativity failure, which stands.
- Trace-sensitive congruence, repaired descent, Prop D well-definedness,
  corrected algebra tag
  `P23AV2-ALGEBRA-COMMUTATIVE-GRADED-NONASSOCIATIVE-MAGMA-WITHOUT-UNIT`,
  all scope walls, Paper 17 gate CLOSED, control matrix rows 1–22.

Terminal status remains ACCEPT-WITH-SCOPE under #322's coordinate set
with the two substitutions recorded here. One-strike not triggered. No
automatic successor; no v3; no candidate reconstruction. Unit C may open
only through its own fresh freeze.
