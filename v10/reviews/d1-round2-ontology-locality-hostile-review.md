# D1 hostile review, round 2: ontology, locality, and typed restriction

**Referee:** independent hostile ontology/locality audit  
**Date:** 2026-07-11  
**Artifacts reviewed:**

- `v10/note-d1-no-silent-support-birth.md`
- `v10/relativistic-isp-v10-paper2-no-silent-centers-do-not-select-support-birth.md`
- `v10/code/d1_no_silent_center_exact.py`
- `v10/code/d1b_marked_support_restriction_exact.py`

**Frozen D1B hash reviewed:**
`a36a51d1951dd881f827ddba1fa5a7ba2407910dce18e171f445bcb0683b9bb3`

## Verdict

**MAJOR REVISION**

The round-1 repairs are substantial and intellectually honest. The partition
receipt reproduces at **45/45** and the marked receipt at **20/20**. The robust
strictly positive nonuniqueness witness is sound. Ports, parents, field
carriers, existing supports, the joint law, and restriction maps now enter the
executable object rather than appearing only in prose. Target marginalization,
screen change, and typed record restriction are correctly separated. The
cutwise result is now stated at its actual strength, and projectivity is
explicitly scoped to the executed common-root family.

Two untested counterexamples nevertheless strike the central marked filter and
its locality interpretation. A third ambiguity can silently erase physically
distinct marked fields. These must be repaired before the marked receipt can be
treated as a clean ontology result.

## Major findings

### M1 — A complete screen can be declared an eligible support

`support_is_eligible` asks only whether every cut has exactly one nonlookup
entry returned by `cut_center_status`. `admissible_centers` includes the empty
set of added center fields. If the visible screen is already complete, that
screen partition is therefore returned with field-name tuple `()`. When the
boundary has more than one occupied nuisance atom, the screen is also
nonlookup. The code then calls the support eligible even though the no-silent
residual is exactly zero and no center was added.

An exact counterexample against the frozen receipt is:

- lineages `A,B` with a common recorded parent and output ports, so `AB` is a
  supplied candidate;
- no screen or center fields, hence the visible screen is constant;
- two occupied duplicate boundary nuisance atoms;
- counts `1` for every `(A,B,b)` atom, so `A` and `B` are exactly independent.

The current functions return:

```text
candidate_supports = ({A,B},)
cut_center_status  = ((constant partition, ()),)
eligible_supports  = ({A,B},)
```

This contradicts the stated discipline that factorized and complete-screen
controls add no redundant center. D1A refuses promotion correctly, but D1B's
marked support predicate does not implement that refusal.

**Required opening:** add a connected, factorized, multi-boundary-atom marked
control. Eligibility must require an incomplete visible screen on every
required cut and a genuine added center beyond the screen. Equivalently,
separate statuses such as `SCREEN_COMPLETE`, `CENTER_IDENTIFIED`, `LOOKUP`,
`AMBIGUOUS`, and `NO_CLOSURE`; do not infer eligibility from the cardinality of
one mixed status tuple.

### M2 — The supplied seam rule is component-global, not local

`candidate_supports` takes every subset of size at least two from each
connected component. Connectivity is transitive. Hence an `A-B-C` chain with
existing supports `AB` and `BC`, but no `AC` support, common parent, or joint
field, generates all of

```text
AB, AC, BC, ABC.
```

The `AC` candidate is licensed merely because a path through `B` exists. On a
large connected record web, the rule proposes arbitrary subsets of the whole
component and therefore requires component-wide knowledge. It blocks joins
between components, but it does not establish microscopic locality or bounded
ancestry locality.

This matters directly to the program's motivating problem: if the universe is
one connected component, the present axiom again allows effectively global
candidate generation.

**Required opening:** either rename the result
`connected-component-confined seam axiom` and remove claims of an explicitly
local candidate family, or define a genuinely local license using a direct
shared parent, an existing support containing the entire candidate, a joint
field carrying the entire candidate, or a bounded marked neighborhood. Add the
`AB-BC` chain adversary and state explicitly whether `AC` and `ABC` should be
licensed.

### M3 — Distinct marked fields with one partition are silently collapsed

`admissible_centers` stores results in a dictionary keyed only by the induced
boundary partition. If two boundary fields have the same values but different
names or stable provenance, the code retains the shorter/lexicographically
earlier name tuple. For example, adding a second ancestor field `H2` with the
same partition as `H` but provenance `root:H2` still returns only `("H",)`.

That is harmless only if equality of induced finite algebras is already proved
to make field identity and provenance gauge. The marked ontology currently
says provenance is stable and includes it in canonical histories, so such a
quotient has not been licensed. The implementation can therefore manufacture a
"unique marked center" by erasing distinct marked realizations.

**Required opening:** define the physical identity of a center. If a center is
only an induced boundary algebra, say explicitly that field name and provenance
are gauge for center selection and prove compatibility with restriction. If
provenance is physical, retain all marked realizations over the same partition
and test duplicate-field ambiguity rather than choosing lexicographically.

## Minor findings

### m1 — The typed projectivity result is valid but exceptionally narrow

The new exhaustive gates correctly check support-family projection on every
nonempty subset of `ABC` and path independence on every nested nonempty subset
path. This supports Proposition 9.1 exactly as scoped.

The category keeps the boundary-atom alphabet and field values fixed; only
record lineages, outcomes, carriers, supports, and marks are projected. It does
not test boundary coarse-graining, deletion of a center field, merging of
boundary atoms, loss of an external parent record, or competing-center
restriction. The paper now calls universal projectivity open, which is
correct. The phrase "projective under the executed restrictions of the finite
common-root family" is the claim ceiling.

### m2 — Some projection claims should be asserted component by component

R1's label says it checks lineages, ports, law, and field carriers, while its
condition directly inspects only lineages and the first field's carrier and
`projected` flag. Later canonical/path tests indirectly exercise ports and the
law, but explicit assertions for parent entries, ports, law marginals, field
provenance, and existing supports would make the typing guarantee auditable.

### m3 — “Nonlookup” remains only an elementary finite screen

The paper now discloses this, but it should consistently use “finite
nonlookup” rather than allowing “nonreconstructive” to carry a stronger
information-theoretic meaning. Fewer partition cells than boundary atoms does
not ensure that the center forgets substantial record information or scales
subraw.

### m4 — The seam axiom is a refusal mechanism, not a birth mechanism

The revised paper is mostly precise here. The disconnected control proves that
a supplied structural rule can veto a statistically dependent cross-component
candidate. It does not explain how a new seam or component bridge arises. It
also does not establish that the field/parent/support marks correspond to
sealed-holonomy observables rather than supplied classical metadata. These are
correctly listed as next-stage questions and must remain nonclaims.

## Findings that now pass

The following round-1 openings are satisfactorily repaired:

1. **Robust center nonuniqueness:** the new strictly positive equal-mass,
   rank-one-atomic witness has two incomparable minimal centers tied in cell
   count and cell-mass entropy. The negative theorem no longer relies on the
   earlier refinement-sensitive construction.
2. **Cutwise wording:** all three pair cuts and all three bipartitions of the
   triple are tested from one joint law. The paper no longer claims equivalent
   pair-edge and hyperedge generative histories.
3. **Operation typing:** target marginalization and screen change are no
   longer presented as record restriction.
4. **Finite projectivity:** the common-root family passes exact support-family
   projection and direct/successive history restriction throughout its
   nonempty subset lattice.
5. **Port intervention:** removing `C`'s output port removes every `C`-bearing
   candidate, so ports now affect candidate generation.
6. **Numerical and covariance discipline:** D1A separately tests X/Z relabeling,
   validates occupied boundary cells, checks every reported minimal center at
   120 digits, and scopes exhaustive versus representative atom permutations.

## Precise claim ceiling after round 2

Even before M1-M3 are repaired, the following mathematical statement survives:

> For supplied finite rational target/boundary laws, exact conditional-
> independence completion may identify a unique nonlookup boundary partition,
> may yield several incomparable minimal partitions even under strict
> positivity and tied elementary complexity, may require atomic lookup, or may
> fail to exist. In one supplied marked common-root model, every pair support
> and the triple support passes the same cutwise center test. A specified
> restriction operation is projective on that model's nonempty lineage-subset
> lattice.

After M1 is fixed, it will also be defensible to call the marked operation a
candidate **filter**. After M2, a locality claim will depend on the exact seam
license adopted. After M3, “unique marked center” will have an unambiguous
ontology.

It is not yet defensible to claim:

- a local record-support proposal law;
- a birth law;
- a law for joining previously disconnected components;
- universal projectivity;
- a field-identity quotient theorem;
- or a derivation from sealed holonomy rather than supplied marked data.

The paper's main negative conclusion remains correct: **no-silent closure is
not the interacting record-birth law.** The next stage should not weight these
candidates until the complete-screen bug and the meaning of “local candidate”
are resolved.
