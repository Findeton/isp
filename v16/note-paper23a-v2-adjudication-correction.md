# Paper 23a v2 adjudication correction — unital withdrawn

Date: 2026-08-22

Disposition: **FORWARD-ONLY CHRONOLOGY CORRECTION TO LEDGER ENTRY
#321 — UNITAL WITHDRAWN; ALL OTHER COORDINATES RETAINED**

This note is a correction to the #321 terminal conferral, ordered by
the user after a read-only semantic recheck. It edits no frozen bytes.
The candidate `v16/paper-23a-v2-trace-sensitive-sector-algebra.md`
remains byte-identical at its frozen hash; the correction lives here
and in the ledger, forward-only in the house sense (new state = new
artifact + LOG entry with hashes).

## 1. Bound corpus

| object | ordinary SHA-256 |
|---|---|
| Paper 13D (sole scientific source) | `3b91766fe269e8145766f4622f99e9009c3270530670119735e6045a473de5c9` |
| P23a v2 pin (#315) | `26587fb58f4f30eb52f9daff725d547ba1d7547ead6f1255ce2ae2a83d0b5dd7` |
| v2 construction note (#316) | `26d2134a839f79905a0374690df6592412fc1c30352a7cac81bd3103c3ce2085` |
| v2 candidate post-repair (#321) | `eca8e1670ecf0c02739c6f94c81e9eefe84b1809240efd8ea9bba94bb886820f` |
| Seat C (#317) | `9dbad9be6e1174d25ddff4ee6de84116148b23e1126e3c33529c1529ae417184` |
| Seat P (#318) | `d569bb3b3cc6ec3ea05f52bc1e4120c7eb3491552a6110136140c930a73d8b79` |
| Seat F (#319) | `c9e69c23c7773668638320d1e0919f848ce668bb1ef4ec555d2bc3bdaf236af3` |
| Adjudication (#320) | `87d6c290724c6f0e0273bce173a0d1e6941344c448f5a0e9f35a96cfee161828` |

## 2. The counterexample, confirmed

The recheck compared Proposition I of the frozen candidate against
Paper 13D §§5.2, 7.1 and 10.2 verbatim.

**Claim under correction (Prop I).** $\mathbf 1=[U_\varnothing(
\emptyset)]$ satisfies $[\chi]\otimes\mathbf 1=[\chi]$, on the
stated ground that the fused history "agrees with the original in
all carried fields" and the added vertex "carries no address, no
seed, and no bond".

**Why this fails.** The class product was defined in stage 3 as
$[\chi]\otimes[\chi']= [\Phi_s(\chi\boxtimes\chi')]$: taking the
product **is** traversing a fusion generator. Fusing with an empty
component therefore produces a *fusion history* — a typed string
diagram containing one additional fusion-generator vertex over the
unfused complex. By the candidate's own Definition 2.3, trace shape
is the isomorphism type of that diagram, "the ordered list of
generator vertices", retained in every complete history; by
Proposition B, complexes with non-isomorphic trace shapes are
incongruent. The unfused complex has no fusion vertex; the fused one
has one. Their trace shapes differ, so

$$[\Phi_s(\chi\boxtimes U_\varnothing)]\ \neq\ [\chi],$$

which is precisely the negation of Prop I's displayed equation.
Prop I's own text concedes the extra vertex ("gains only a degenerate
fusion vertex") and then identifies the classes anyway — contradicting
Def 2.3/Prop B on the candidate's own terms.

**Paper 13D testimony.**

- §5.2: Exec_D is "quotiented only by the symmetric-monoidal axioms,
  the finite-set covariance equations, and the explicitly stated n-ary
  permutation invariance of a single fusion generator." There is **no
  fusion-unit equation**; nothing legitimizes identifying a fusion
  history with an unfused complex even at an empty component.
- §7.1: "a fusion history retains its tensor source value and fused
  target value. The trace records the boundary sorts actually
  traversed…" — generator source/target boundaries survive in
  complete histories; the empty-corner fusion does not erase them.
- §10.2: staged sequences are "a different execution trace … not
  silently identified"; the same trace-sensitivity forbids silently
  deleting a degenerate fusion vertex.

Paper 13D §3.4 makes $U_\varnothing(\emptyset)$ the unit only of the
*formal boundary* $\boxtimes$ (empty tensor family) — a typing-level
fact about sources of fusion generators, not an identification law on
executed histories or classes. Prop I conflated the two.

**Verdict: CONFIRMED. Proposition I is false as proved; unital fails
in $\mathsf{Sect}^{ts}_{13D}$.**

Note also: $\mathbf 1\otimes\mathbf 1=[\Phi_s(U_\varnothing
\boxtimes U_\varnothing)]\neq\mathbf 1$, so $\{\mathbf 1\}$ is not
even closed under $\otimes$, and §4.1's sentence calling the
empty-carrier corner "trivially associative" falls with it.

## 3. Withdrawals

Withdrawn from the #321 coordinate set and from every derived claim:

1. **Proposition I (unit)** in its entirety, including both its
   statement and proof.
2. The **UNITAL** component of the algebra tag.
   Corrected tag:
   **`P23AV2-ALGEBRA-COMMUTATIVE-GRADED-NONASSOCIATIVE-MAGMA`
   WITHOUT UNIT**.
3. **§4.3 table row 3e**: unit EXISTS → corrected to **unit ABSENT**
   (by the counterexample above).
4. **§4.1**'s empty-corner sentence ("the empty-carrier corner
   $\{\mathbf 1\}$ is trivially associative") — withdrawn; see §2.
5. Every phrase in §§4.1/§6 asserting "unit" among constructed clauses
   ("well-definedness, commutativity, unit, nonassociativity…").
6. The symbol $\mathbf 1$ carries no class meaning going forward; it
   denotes only the formal boundary unit of Paper 13D §3.4.

No seat finding is reopened: the seats accepted Prop I on the same
misreading, which is exactly why the defect reached terminal. This
correction supersedes the affected coordinates of #321; it reopens no
review seat and orders no repair to frozen bytes.

## 4. Retentions

Each retained item is supported independently of any unit claim:

- **Trace-sensitive congruence** (Def 2.1, Thm A, Props B–C):
  untouched; indeed the very instrument that exposes the defect.
- **Repaired multiplicity descent** (stage 2): untouched.
- **Well-definedness** (Prop D): alignment composition through tensor
  and fusion kernel; no unit input.
- **Carrier monotonicity / finite-closure failure** (Lemma E, Thm F,
  outcome `P23AV2-FINITE-CLOSURE-FAILS-BY-CARRIER-MONOTONICITY`):
  strengthened, not weakened — since even products with the
  empty-carrier class strictly increase carrier size, no nontrivial
  subfamily closes, full stop.
- **Commutativity** (Prop G): family-indexed generator + braiding
  transport + equal comparison profiles + separation; no unit input.
- **Nonassociativity** (Prop H via Prop C/B): bracketing frontiers;
  no unit input.
- **Duals absent** (Prop J): carrier-additivity argument survives
  a fortiori without a unit class.
- **FP-route closure**, scope unchanged
  (`P23AV2-FP-BOOTSTRAP-ROUTE-CLOSED-FOR-PRESENT-GAMMA`, present-$
  \Gamma_D$ certified fixtures only, parent control 40): depends only
  on associativity failure (no ring for a character), which stands.
- All scope walls, the Paper 17 gate CLOSED status, control matrix
  rows 1–22 (row dispositions unaffected), and the non-earned outcome
  list are unchanged.

## 5. Corrected coordinate set for #321

```text
P23AV2-SECTOR-CONGRUENCE-TRACE-SENSITIVE-CONSTRUCTED
P23AV2-MULTIPLICITY-DESCENT-REPAIRED-CONSTRUCTED
P23AV2-FINITE-CLOSURE-FAILS-BY-CARRIER-MONOTONICITY
P23AV2-CLASS-PRODUCT-NONASSOCIATIVE
P23AV2-CLASS-PRODUCT-COMMUTATIVE
P23AV2-DUALS-ABSENT
P23AV2-ALGEBRA-COMMUTATIVE-GRADED-NONASSOCIATIVE-MAGMA-WITHOUT-UNIT
P23AV2-FP-BOOTSTRAP-ROUTE-CLOSED-FOR-PRESENT-GAMMA
```

Terminal status remains ACCEPT-WITH-SCOPE under this corrected set;
the negative result is, if anything, sharper — the sector family is a
commutative graded nonassociative magma without unit whose finite
closure fails outright.

One-strike rule: not triggered; this is a user-ordered chronology
correction of a terminal artifact, not a candidate rejection.

No automatic successor exists. Any further stage requires explicit
authorization and a fresh freeze. No v3 is authorized by this note.
