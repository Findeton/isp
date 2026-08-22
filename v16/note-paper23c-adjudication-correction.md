# Paper 23c adjudication correction — quotient-valued target, no-go re-derived

Date: 2026-08-22

Disposition: **FORWARD-ONLY ADJUDICATION CORRECTION TO #328/#329 —
PROPOSITION A VOID AS PROVED; PROPOSITION F'S WITNESS PAIR
QUOTIENT-EQUIVALENT; NO-GO RE-DERIVED ON THE CORRECT QUOTIENT WITH
NARROWED COORDINATES**

User-ordered read-only semantic correction. It edits no frozen bytes:
the candidate remains at `9f106e4526065593b3ab7cdd1b0202bee9bef2428b4bd0646abd428dc70fa3ca`;
this note and the ledger carry the corrected state, forward-only in the
house sense.

## 1. Bound corpus

| object | ordinary SHA-256 |
|---|---|
| Paper 13D | `3b91766fe269e8145766f4622f99e9009c3270530670119735e6045a473de5c9` |
| P23c pin (#324) | `d50dc41c7a7cf4f42b5caf3489b790990f9d899c113020a495844fbcac5dfcd2` |
| P23c candidate pre-repair (#326) | `7e90aba64c4abf5585d409f8d9696c76e0308007da3f81607e8e187cf709f126` |
| P23c candidate post-repair (#329, unchanged here) | `9f106e4526065593b3ab7cdd1b0202bee9bef2428b4bd0646abd428dc70fa3ca` |
| Seats (#327) | `e945a8ae…`, `bf676fb2…`, `c546f849…` |
| Adjudication (#328) | `48e0d881eb373b376d826138bbbc59fa90d9d05a22b3fb390d3ee94b91a5a149` |

## 2. The error, confirmed

The target of Definition 2.3 is an **exchangeable class**: an ordered
pair $(L_1,L_2)$ taken modulo simultaneous presentation transport *and*
the rank swap $(L_1,L_2)\sim(L_2,L_1)$ (Paper 15's contract; pin §2).
Proposition A as printed tests fixed points of **ordered pairs**, not of
their swap classes, and Proposition F uses the rank swap as a *second,
distinct* assignment — but rank-swapped pairs are the same target value.

**Counterexample (user-supplied), $n=2$.** Let $L_1\colon 1<2$ and
$L_2\colon 2<1$, and let $\tau=(1\,2)$ be the carrier transposition.
Transport exchanges the two orders: $\tau L_1=L_2$, $\tau L_2=L_1$. The
exchangeable class $\{L_1,L_2\}$ is therefore **fixed by $\tau$**.
More generally, a transport-orbit-saturated swap class is automatically
closed under every further transport, so *every* exchangeable class is a
fixed point of the full stabilizer action: **class-valued equivariant
outputs are trivially stabilizer-fixed at every size.**

Consequences for the frozen candidate:

- **Proposition A (line 67) is void as proved.** Its fixed-point
  obstruction applies to ordered-pair-valued outputs only. Since the
  declared target is quotient-valued, it excludes nothing. Verified by
  exhaustive recomputation: all five exchangeable classes at $n=3$
  (seventeen at $n=4$) are stabilizer-fixed as values.
- **Proposition F (line 162) loses its witness pair.** "An assignment
  and its rank swap" do not differ as values of Definition 2.3; that
  pair cannot evidence nonuniqueness.
- Consequently the printed derivation of
  `P23C-ORIENTED-PAIR-NOT-DERIVABLE` does not establish its claim by
  the route printed, and the coordinate set of #329 is over-awarded as
  it stands.

The three blind seats and the #328 adjudicator all missed this: each
checked the arguments against the ordered-pair reading. The defect is
attributable to the construction author (this programme), not to review
independence.

## 3. What the corrected analysis actually shows

Re-derived on the correct quotient (all checks exact, scaffolding under
`$TMPDIR/p23c/`, not part of any constructed object):

**(C1) Existence is NOT excluded on symmetric experiments.** Class-valued
assignments can be equivariant: e.g. at $n=2$ the antiparallel class
$\{(L,\mathrm{rev}\,L)\}$ is stabilizer-fixed and satisfies the
intersection condition for an antichain dependency. Any corrected no-go
must run through determination or uniqueness, not existence.

**(C2) Determination failure stands (Lemma C + Prop D, repaired form).**
The two exchangeable classes $[\,(L,\mathrm{rev}\,L)\,]$ (antiparallel)
and $[\,(L,L)\,]$ (parallel) are **distinct target values** (verified not
related by transport+swap for $n=2,3,4$), yet Lemma C's relabeling
invariance gives them one identical complete $\Gamma_D$ law, while their
oriented increasing–increasing pattern densities differ ($0$ vs
$\frac16$). Hence **no admissible observable valued in exchangeable
classes is determined by $\Gamma_D$: the law does not select which realizer
class, if any, to supply.**

**(C3) Uniqueness failure stands with a repaired witness.** On rigid
experiments both an antiparallel-class assignment and a parallel-class
assignment are admissible, and they are **genuinely non-equivalent**
(C2); $\Gamma_D$ provides no datum between them (#237 wall).

**(C4) Prop B survives untouched** — no covariant *single* total order
exists on free carriers; the swap quotient is irrelevant to it. But by
itself it blocks only order-valued (not class-valued) constructions.

## 4. Corrected coordinates

Withdrawn (over-awarded at #329):

```text
P23C-EQUIVARIANT-FIXED-POINT-OBSTRUCTION   (void: false for quotient-valued targets)
P23C-RIGID-EXPERIMENT-UNIQUENESS-FAILURE   (re-earned below under C3 with corrected witness)
```

Retained / re-earned, forward-only:

```text
P23C-ORIENTED-PAIR-NOT-DETERMINED-BY-GAMMA   (primary; from C2+C3)
P23C-NO-COVARIANT-SINGLE-ORDER               (C4, unchanged)
P23C-LAW-RANK-INVARIANCE                     (Lemma C + Prop D, unchanged)
P23C-REALIZER-CLASS-UNIQUENESS-FAILURE       (C3, repaired witness)
P23C-UNORIENTED-BOND-STRUCTURE-DERIVED       (§5 residual, unchanged)
```

Primary disposition renamed: what is proved is that $\Gamma_D$ does not
**determine** the exchangeable oriented null-realizer pair (no admissible
assignment is law-selected, and none is unique where symmetry lapses).
Whether some weaker non-law-selected covariant decoration could be
*declared* is not excluded by these results and was never the gate's
question; the rigidity-theorem input requires a law-derived pair, so the
gate outcome for Paper 15 is unchanged: **CONDITIONAL, bridge missing for
the present law.** Dimension firewall intact; ensemble gate closed.

## 5. Scope of this correction

No new construction; no v2; no automatic successor; Unit D stays
closed until the user opens it. One-strike rule not triggered (this is
a user-ordered chronology correction). The scoped synthesis about
present-$\Gamma_D$ — distinguishing symmetry breaking **in the law**
from symmetry breaking **in a root state, boundary condition, or
declared $\Pi_{\rm phys}$** — is separately authorized preparation and
is not part of this correction.
