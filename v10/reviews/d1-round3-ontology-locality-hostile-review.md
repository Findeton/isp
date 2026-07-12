# D1 hostile review, round 3: ontology, locality, and restriction

**Referee:** independent hostile ontology/locality audit  
**Date:** 2026-07-11  
**Verdict:** **PASS WITH MINOR CORRECTIONS at the stated finite scope**

## Frozen artifacts reviewed

- `v10/note-d1-no-silent-support-birth.md`
- `v10/relativistic-isp-v10-paper2-no-silent-centers-do-not-select-support-birth.md`
- `v10/code/d1_no_silent_center_exact.py`
- `v10/code/d1b_marked_support_restriction_exact.py`

Hashes executed in this review:

```text
1b6e4ef3339d65941445f1277dd0d0afe59f3ea29763854c078a1d33f79f078d  d1_no_silent_center_exact.py
b5a107382fbef24d7a2c20a45a2382dd64788b897b7dfc83efa7b27fca43011f  d1b_marked_support_restriction_exact.py
```

D1A reproduced **45/45** exact/high-precision checks. D1B reproduced **28/28**
exact checks. No numerical or executable discrepancy was found.

## Executive assessment

All three round-2 major findings are repaired in the executable semantics, not
only in prose:

1. complete screens are refused before center cardinality is interpreted;
2. candidate supports arise from direct structural carriers rather than the
   transitive connected component;
3. provenance-distinct marked fields remain distinct center realizations even
   when they induce the same boundary partition.

The new parity/synergy cell also resolves an important conceptual ambiguity.
The marked-history restriction data are path-independent in the executed
families, while the derived eligible-support family is not natural under the
same typed restriction. The paper now states that distinction correctly.

No support-birth law, generative-decomposition equivalence, universal
projectivity, continuum covariance, or profinite theorem is claimed. The main
negative conclusion is supported.

## Round-2 major findings: disposition

### M1 — Complete-screen false eligibility: CLOSED

`support_is_eligible` now performs three separate checks on every cut:

1. the visible screen must be exactly incomplete;
2. the unique completion must differ from the screen;
3. it must use at least one non-screen marked field.

M6 supplies a structurally connected but exactly factorized candidate and
refuses it. M7 turns `H` into a visible complete screen and refuses every
otherwise structural candidate. This closes the exact counterexample from
round 2.

### M2 — Transitive component-global locality: CLOSED at direct-carrier scope

`candidate_supports` no longer enumerates subsets of connected components. It
first constructs primitive carriers from:

- a sibling group sharing one recorded parent;
- an existing support hyperedge;
- an ancestor or joint-boundary field carrier.

It then enumerates output-port-bearing subsets only inside each direct
carrier. L4 verifies that overlapping `AB` and `BC` carriers do not license
`AC` or `ABC`, even though all three lineages lie in one transitive component.

This is a valid finite **direct-carrier-local** rule. It is still supplied as
an axiom and is not derived from diamonds; the paper says so.

### M3 — Provenance collapse: CLOSED

Center generator identity now includes stable `name@provenance`. Minimality is
first computed on induced partitions, after which every irredundant marked
generator realization of a minimal partition is retained. M8 duplicates `H`
with different provenance, obtains two center realizations over one partition,
and refuses uniqueness. No lexicographic physical selector remains.

## Load-bearing ontology audit

The marked fields now do actual work:

- **ports** constrain the candidate family; M2b removes all `C`-bearing
  candidates when `C` loses its output port;
- **parents** generate direct sibling carriers;
- **existing supports** generate direct carriers and the `AB-BC` adversary;
- **field carriers and kinds** determine both candidate seams and admissible
  center algebras;
- **field values** generate the tested boundary partitions;
- **provenance** distinguishes center realizations;
- **the joint law** supplies every exact cut table;
- **restriction** projects lineages, ports, parents, support marks, field
  carriers, provenance, and the joint law.

The objects are therefore no longer decorative metadata. They remain a frozen
finite ontology, not a derivation from sealed holonomy.

## Restriction and projectivity audit

The common-root positive family passes:

- eligible-support projection versus recomputation on every nonempty lineage
  subset;
- direct versus successive marked-history restriction on every nested
  nonempty subset path;
- loss of all multi-record supports on a one-lineage restriction.

The parity/synergy family then supplies a genuine typed adversary:

```text
Eligible(ARZ) = {ARZ}
project to AZ = {AZ}
Eligible(restrict to AZ) = empty
```

Every pair restriction is exactly complete at the visible constant screen,
while all full triple cuts require `H`. Meanwhile direct and successive
restriction of the marked history itself remain identical. Thus the receipt
supports precisely this statement:

> the executed marked-history restriction is functorial/path-independent, but
> the derived minimal eligible-support family is not a natural transformation.

It does not support the stronger statement that every possible record-history
restriction category has been classified. The paper explicitly refuses that
stronger claim.

## Remaining minor findings

### m1 — “Local” must remain qualified as direct-carrier-local

A primitive carrier may have arbitrarily large arity. A common parent or one
joint field carrying many lineages licenses every subset of that carrier. D1B
eliminates transitive graph nonlocality, but it does not establish bounded
range, bounded arity, finite propagation speed, relativistic locality, or a
local algorithm for discovering the primitive carrier.

The paper is defensible when it says “supplied ancestry-local” or
“direct-carrier-local.” Phrases such as “an explicitly local candidate family”
should be read with that qualification and preferably written that way.

### m2 — Eligibility non-naturality is relative to a supplied support functor

`project_support_family` maps a support to its intersection with retained
lineages when at least two survive. Another ontology could declare a joint
event destroyed when any participant is removed rather than project it to a
lower-arity support. The parity theorem is exact for the implemented
intersection functor, but it is not a no-go for every conceivable support
restriction semantics.

The paper should retain the phrase “under the executed typed restriction” or
equivalent whenever summarizing Theorem 9.1.

### m3 — Well-formedness is constructed rather than validated generically

The frozen histories have matching lineage lists, outcome dimensions, field
value lengths, carriers, nonnegative counts, and unique intended provenance.
There is no general validator enforcing those invariants for arbitrary
`MarkedHistory` inputs. This does not damage the exhibited theorems, but a
reusable birth-law implementation will need an explicit validity predicate.

### m4 — One legacy receipt label remains ontologically too strong

D1A still describes S4 in executable output/comments as a “genuine
three-record crossing.” The note and paper correctly downgrade it to a
three-variable common-root law that does not prove an irreducible three-record
event. The receipt label should eventually match that scoped interpretation.

## Claim-leak audit

No material claim leak remains in Paper 2.

- **Birth:** the paper repeatedly says candidate seams and centers are supplied
  or identified, not created by conditional independence.
- **Generative equivalence:** Theorem 7.1 is explicitly cutwise; the paper says
  it does not construct equivalent three-pair and hyperedge histories.
- **Projectivity:** history-data path independence is separated from the proved
  failure of eligible-family naturality.
- **Locality:** the seam axiom is admitted as extra record structure, and new
  component joining remains open.
- **Profinite/continuum:** both are explicit nonclaims.
- **Dynamics:** no click rate, transfer law, outcome kernel, root law, or final
  interacting law is inferred.

The title phrase “support birth” therefore names the conjecture being refused,
not a result being claimed.

## Surviving claim ceiling

The strongest defensible result is:

> In supplied finite rational marked histories, a direct-carrier candidate
> rule can feed an exact no-silent filter. The filter refuses complete screens,
> lookup-only closures, absent boundary closures, unlicensed cross-carrier
> joins, and marked-center ambiguity. It can identify a unique finite nonlookup
> marked center in some supplied cuts. Strict positivity and tied elementary
> complexity do not ensure center uniqueness. Cutwise unique closure does not
> select one support from a supplied pair/triple family. Under the implemented
> intersection restriction, marked histories are path-independent in the two
> executed families, but eligible-support formation is not natural.

It is not defensible to promote this to:

- a record-support proposal or birth law;
- a rule for creating primitive carriers or joining disconnected components;
- a unique support/arity selector;
- an equivalence theorem for alternative generative histories;
- universal projectivity;
- relativistic locality;
- a continuum or marked-profinite theorem;
- or a dynamic interacting click law.

## Remaining opening and final recommendation

No additional D1 computation is required for the paper's current finite claim.
The only wording corrections recommended before freezing Paper 2 are:

1. qualify “local” as “supplied direct-carrier-local”;
2. qualify eligibility non-naturality by the implemented intersection support
   functor;
3. rename D1A's S4 legacy “genuine crossing” label.

The substantive opening is correctly moved to Investigation 2:

> derive, or prove underdetermined, the diamond operation that creates the
> primitive direct carrier itself.

Until that operation exists, D1 is an exact accounting/filter theorem over
supplied marked candidates. At that scope, it passes hostile ontology review.

## Final verification addendum

**Independent recheck:** 2026-07-11  
**Final verdict:** **PASS at the finite scoped result; no open D1 blocker**

The post-review corrections were inspected and both receipts were rerun.
D1A remains **45/45** and D1B remains **28/28**. The reviewed final hashes are:

```text
51b3a6460ccf3ddcac7efc0448c770cfa76187a7560ce7bcbb63adf3fb735947  d1_no_silent_center_exact.py
d0944fbf99ac0b9e7f5d94c90feb1d8ae88be21a47bd52bb9461edee4dd978eb  d1b_marked_support_restriction_exact.py
f0dad6ce77932cd1bf60980009e999dc455153c84733876a716f7aebecd6fa61  note-d1-no-silent-support-birth.md
67619bb7fe3d49b07260cf887f483ab5a1244963b9acb31e68846b274b0851cb  relativistic-isp-v10-paper2-no-silent-centers-do-not-select-support-birth.md
```

The three requested corrections are verified:

1. Locality is explicitly supplied and defined by direct parent, support, or
   joint-field carriers; the text and receipt deny transitive completion.
   “Ancestry-local” is therefore used in its stated direct-carrier sense, not
   as a derived relativistic-locality claim.
2. The note defines `r_*S=S∩K`, discarding supports of retained arity below
   two, and Theorem 9.1 now attributes non-naturality specifically to this
   implemented intersection support projection.
3. D1A's S4 is renamed `S4-common-root-three-variable`; its comment and output
   now say that a supplied common-root field closes the cut and does not prove
   an irreducible three-record event.

The additional identity repair also passes. Center generators are represented
by typed `(name, provenance)` pairs rather than concatenated strings. M8 uses
the delimiter-adversarial pairs `("A@B","C")` and `("A","B@C")`, which
would collide under naive `name@provenance` concatenation, and preserves them
as two center algebras over the same partition. The support is consequently
refused as ambiguous.

No birth, generative-equivalence, universal-projectivity, relativistic-
locality, continuum, or profinite claim leaks remain. The next opening is not
a repair to D1: it is the derivation of primitive direct carriers from sealed
diamond structure.
