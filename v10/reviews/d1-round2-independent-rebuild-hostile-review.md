# D1 hostile review, round 2: independent reconstruction and adversary search

**Referee:** hostile independent rebuild

**Date:** 2026-07-11

**Verdict:** **MAJOR REVISION**

The repaired partition theorem is correct and independently reproducible. The
stronger S5 witness survives exact enumeration, refinement stability,
strict positivity, equal atom mass, equal center cardinality, and equal
cell-mass entropy. The six cut claims are also reproduced from one joint law.

The marked receipt, however, contains a complete-screen false positive. Once
that false positive is corrected, an exact parity/common-cause history gives a
genuine counterexample to eligibility-family projectivity. The history object
itself remains functorial; the derived eligible-support family does not. A
second structural opening is that the advertised ancestry-local seam generator
is only connected-component-confined and becomes global on a connected web.

These findings do not damage the principal negative result that no-silent
closure is not a record-birth law. They sharpen it. They do block the present
marked-filter and projectivity wording until the new adversaries are included.

## 1. Frozen artifacts reviewed

The following hashes identify the live round-2 snapshot reviewed:

```text
3f56214ff6700842fc6eeb32ffba18dc5d1acaa8ee26aaec2723a13755f70f75  v10/note-d1-no-silent-support-birth.md
10e7b17eb0fd46d21eaee5d8060c3826355db5dc3bb2d594a511c3880b5b6370  v10/relativistic-isp-v10-paper2-no-silent-centers-do-not-select-support-birth.md
1b6e4ef3339d65941445f1277dd0d0afe59f3ea29763854c078a1d33f79f078d  v10/code/d1_no_silent_center_exact.py
a36a51d1951dd881f827ddba1fa5a7ba2407910dce18e171f445bcb0683b9bb3  v10/code/d1b_marked_support_restriction_exact.py
```

The production commands were:

```bash
PYTHONDONTWRITEBYTECODE=1 \
  /opt/miniconda3/envs/tbp.monty/bin/python \
  v10/code/d1_no_silent_center_exact.py

PYTHONDONTWRITEBYTECODE=1 \
  python3 v10/code/d1b_marked_support_restriction_exact.py
```

Both were run twice. Each run exited zero. The byte-identical output hashes
were:

```text
a265b73f93e2fe23d77aebc2763152cc398240dcc98599442af68899d43d78ea  D1A output, both runs
7fd754dbc69a9883fa1a904b3c6e4efda9d73b4c687dbaa38f126500bc7abdcc  D1B output, both runs
```

D1A printed **45/45** and D1B printed **20/20**.

## 2. Independent rebuild

I wrote a fresh Ruby implementation which imported no production helper. It
independently:

1. generated restricted-growth set partitions;
2. tested conditional independence by exact integer minors;
3. selected coarsest complete partitions under refinement;
4. constructed the single three-variable common-root law;
5. marginalized that law into all three pair cuts and all three triple cuts;
6. compared direct and successive law restriction;
7. reconstructed the output-port support intervention; and
8. rebuilt the stronger S5 census.

The scratch implementation had SHA-256
`87b4b094c91ba9b81f0b3b5d8443b7d5e8df94ac8a0b65c052af99b983031de1`
during review. Its exact independent output was:

```text
CUT A|B   constant=false H=true complete=4 minima={{0,1},{2,3}}
CUT A|C   constant=false H=true complete=4 minima={{0,1},{2,3}}
CUT B|C   constant=false H=true complete=4 minima={{0,1},{2,3}}
CUT AB|C  constant=false H=true complete=4 minima={{0,1},{2,3}}
CUT AC|B  constant=false H=true complete=4 minima={{0,1},{2,3}}
CUT BC|A  constant=false H=true complete=4 minima={{0,1},{2,3}}
direct restriction equals successive restriction: true
full output-port support family: AB, AC, BC, ABC
after removing C output port: AB
```

Thus the one-joint-law/all-cuts result is genuine. The cut tables are not six
unrelated fitted laws.

## 3. Stronger S5 verification — pass

The reviewed S5 matrices are

$$
M_0=\begin{pmatrix}16&4\\4&1\end{pmatrix},\quad
M_1=\begin{pmatrix}3&2\\12&8\end{pmatrix},
$$

$$
M_2=\begin{pmatrix}1&4\\4&16\end{pmatrix},\quad
M_3=\begin{pmatrix}2&8\\3&12\end{pmatrix}.
$$

Independent exact results:

- every entry is positive;
- every atomic matrix has determinant zero;
- every atomic matrix has mass 25;
- the aggregate is
  $\begin{pmatrix}22&18\\23&37\end{pmatrix}$ with determinant 400;
- all 15 boundary partitions were enumerated;
- exactly three are complete;
- they are
  $\{\{0\},\{1,2\},\{3\}\}$,
  $\{\{0\},\{1\},\{2,3\}\}$, and atomic lookup;
- the first two are exactly the two incomparable minima;
- every refinement of either minimum is complete;
- both minima have cell-mass multiset $(25,25,50)$.

This is stronger than the first-round witness. The result does not rely on a
Simpson-effect failure at the atomic boundary. Neither block count nor center
entropy selects one minimum.

## 4. Major finding 1 — complete screens are falsely called eligible

`support_is_eligible` currently asks whether each cut has exactly one item in
`cut_center_status`. But `admissible_centers` includes the empty selection of
added center fields. If the visible screen is already complete, that screen is
returned with field-name tuple `()`. A multi-atom complete screen is not atomic
lookup, so `cut_center_status` retains it. The support is then called eligible
although its residual is exactly zero and no center was added.

An exact production-level adversary is:

- lineages `A,B` with the same recorded parent;
- output ports on both lineages;
- an ancestor field `H=(0,0,1,1)`;
- four positive boundary atoms;
- every `(A,B,b)` count equal to one.

The frozen functions return:

```text
candidates = (AB,)
status     = ((constant screen, no added field),)
eligible   = (AB,)
```

This contradicts the campaign's own rule that an already-complete screen does
not license a new center-supported event.

**Required repair:** use a typed cut classification rather than the length of
one mixed tuple. At minimum, eligibility must require:

1. the visible screen is exactly incomplete;
2. exactly one strictly finer marked center closes it;
3. that center is finite nonlookup; and
4. the closing field set is nonempty.

Add the connected-factorized adversary as a mandatory refusal gate.

## 5. Major finding 2 — corrected eligibility is not projective

Once complete screens are correctly refused, a genuine typed projectivity
counterexample appears.

Take lineages `A,R,Z`, all with output ports and one common recorded root. Let
the boundary center be

$$
H=(u,v),\qquad u,v\in\{0,1\},
$$

with every `H` state duplicated by a nuisance bit, giving eight boundary
atoms. Conditional on `H`, let the three records be independent with:

$$
A\text{ depends on }u:(3,1)/(1,3),
$$

$$
Z\text{ depends on }v:(5,1)/(1,5),
$$

$$
R\text{ depends on }u\oplus v:(4,1)/(1,4).
$$

Mark `H=(0,0,1,1,2,2,3,3)` as an ancestor field carried by `ARZ`.

All counts are positive integers. Exact reconstruction gives:

- `A,R`, `A,Z`, and `R,Z` are each independent at the constant screen;
- therefore all three pair supports must be refused after Major finding 1 is
  repaired;
- every bipartition of `ARZ` has positive residual;
- the marked `H` field is the unique nonlookup closing center for every
  triple cut;
- hence the corrected full eligible family is `{ARZ}`.

Now restrict the history to `AZ`:

$$
\operatorname{project}_{AZ}\{ARZ\}=\{AZ\},
$$

but exact recomputation gives

$$
\operatorname{Eligible}(H|_{AZ})=\varnothing.
$$

Therefore

$$
\operatorname{project}_{AZ}\operatorname{Eligible}(H)
\ne
\operatorname{Eligible}(H|_{AZ}).
$$

This is the standard pairwise-independent but jointly dependent parity
adversary expressed inside the paper's marked ontology. The history restriction
operation itself remains path-independent. The failure is in the derived
eligible-support family.

The paper already scopes its positive test to one common-root family, but it
also says D1 has no genuine typed counterexample. That sentence must be
withdrawn. Investigation 1 can now decide universal support-family naturality
negatively while retaining the positive functoriality result for the history
object and the original product-mixture family.

## 6. Major finding 3 — the seam generator is component-global

`candidate_supports` enumerates every subset of size at least two in each
transitive connected component. This blocks cross-component proposals, but it
does not define microscopic locality.

For example, a marked chain containing existing supports `AB` and `BC`, with
no direct `AC` support, no common parent of all three, and no `ABC` field,
nevertheless produces:

```text
AB, AC, BC, ABC
```

because all three lineages lie in one connected component. In a connected
universe the generator proposes arbitrary finite subsets of the whole web and
requires component-wide knowledge.

**Required repair:** either call this a
`connected-component-confined candidate axiom`, or replace it with a direct
license such as a shared parent, an existing support containing the entire
candidate, a joint field carried by the entire candidate, or a bounded marked
neighborhood. Add the `AB-BC` chain as an explicit classification gate.

## 7. Major finding 4 — marked provenance is silently quotiented

`admissible_centers` keys its result dictionary only by induced partition. Two
fields with identical values but different names, kind, or stable provenance
are collapsed, and the shorter/lexicographically earlier name tuple is kept.

This can turn two marked realizations into one “unique marked center.” It is
valid only if equality of induced finite algebras has already been declared a
gauge equivalence. But D1B stores provenance in the history and calls it stable
under restriction.

**Required repair:** choose and state one ontology:

- if only the induced algebra is physical, declare field identity/provenance
  gauge for center selection and prove the quotient commutes with restriction;
- if provenance is physical, retain every marked realization and report the
  ambiguity instead of selecting lexicographically.

The two-partition S5 theorem survives either choice because `R` and `C` induce
different partitions.

## 8. Minor findings

1. `candidate_supports` uses output ports, but `support_is_eligible` can still
   be called directly on a support with no exposed port. This is harmless when
   only `eligible_supports` is public, but the API invariant should be stated or
   enforced.
2. D1B's static joint laws are positive and normalized up to a common count,
   but it has no explicit positivity/occupied-atom gate comparable to D1A.
3. The typed history restriction tests keep the boundary-atom alphabet fixed.
   They do not cover boundary coarsening, loss of a parent record, or deletion
   of a center field. The paper mostly discloses this.
4. The finite `|C|<|B|` gate remains only finite nonlookup, not an asymptotic
   nonreconstruction theorem.

## 9. Results that survive hostile reconstruction

The following findings pass independently:

1. finite exact no-silent completion can have zero, one, or several minimal
   centers;
2. the stronger S5 proves robust positive center nonuniqueness;
3. S6 is lookup-only and S7 has no boundary-definable closing center;
4. one strictly positive common-root joint law produces unique `H` centers on
   all three pair cuts and all three triple bipartitions;
5. the cutwise filter does not select one support from the supplied candidate
   family;
6. removing an output port changes the candidate-support family;
7. the marked history restriction object is path-independent on the tested
   nonempty subset lattice;
8. no-silent closure remains downstream of a still-undetermined seam proposal
   law.

## 10. Required round-2 disposition

Before a passing review:

1. repair complete-screen eligibility and add the connected-factorized
   refusal;
2. execute the parity/synergy projectivity adversary and separate history
   functoriality from eligibility-family naturality;
3. classify component-global versus genuinely local candidate generation;
4. decide whether same-partition marked provenance is gauge or physical;
5. update the paper, note, receipt counts, hashes, claims, and next-step plan.

After those repairs, the expected final verdict is not a recovered birth law.
It is the sharper and well-supported boundary:

$$
\boxed{
\text{No-silent completion is an exact finite cut diagnostic, but it neither
generates local supports nor defines a universally projective support family.}
}
$$

