# Relativistic ISP v10 Paper 2: No-Silent Centers Do Not Select Record Support Birth

## Exact center census, marked-history locality, and the projectivity boundary

**Author:** Felix Robles Elvira (ORCID: 0009-0009-2017-4394; independent researcher)

**Status:** revised after independent hostile review, 2026-07-11. This paper
does not derive the final interacting record click law. It establishes what the
first v10 candidate principle can and cannot do. The final receipts require
only Python's standard library and reside entirely under `v10/`.

**Receipts:**

- `v10/code/d1_no_silent_center_exact.py` — 45/45 exact/high-precision checks;
- `v10/code/d1b_marked_support_restriction_exact.py` — 28/28 exact checks.

## Abstract

V10 Paper 1 identified the no-silent seam as the strongest unused candidate
for record support birth. If record targets `X` and `Z` meet through a visible
boundary screen `Y`, a positive conditional dependence

$$
I(X;Z\mid Y)>0
$$

proves that `Y` is not a complete separator. A finite boundary `B` may contain
a center `C=c(B)` for which

$$
X\perp Z\mid C.
$$

The opening conjecture was that the unique minimal such center could determine
the birth of a joint record support. We test the conjecture with two receipts.
The first exhausts every partition of small rational boundary laws. The second
rebuilds the experiment with named record lineages and ports, parent maps,
boundary fields with carriers, support connectivity, candidate seams, one
joint three-record law, and a typed history restriction.

The positive result is real but narrow. Exact no-silent residue can expose an
incomplete screen and, in explicit cells, identify a unique minimal nonlookup
center. Factorized and complete-screen controls add no redundant center.
Lookup-only and no-boundary-closure cases are refused. An explicitly supplied
ancestry-local seam rule blocks joins between structurally disconnected direct
carriers, refuses already-complete screens, and does not transitively turn an
`AB-BC` chain into `AC` or `ABC`. Marked history data restrict
path-independently in both tested families.

The negative result is decisive for the proposed birth law. A strictly
positive integer witness has two incomparable, equally coarse, equal-mass
minimal centers. In a marked common-root law, every pair support and the triple
support passes the same unique-center filter. Thus the filter does not select
one support from the supplied candidate family. Moreover, the structural seam
license, the common-root field, and the candidate family are additional record
data; conditional independence does not generate them. A pairwise-independent
but jointly dependent parity history then gives a genuine typed counterexample
to eligibility-family projectivity under the implemented intersection support
projection: the full triple is eligible, every pair restriction is not, and
projection disagrees with recomputation.

The exact verdict is

$$
\boxed{
\text{no-silent closure is a boundary-accounting and candidate-filtering law,}
\quad
\text{not a record-support birth law.}
}
$$

The next investigation must derive the local seam license and irreducible
support proposal from record/diamond structure before asking for a positive
firing weight.

## 1. The question decomposed

The desired implication was

$$
I(X;Z\mid Y)>0
\Longrightarrow
\text{birth of a uniquely determined joint record support}.
$$

That arrow hides distinct claims:

1. the visible screen is incomplete;
2. the missing separator is boundary-definable;
3. a complete center exists;
4. a minimal center is unique;
5. the center is not full boundary lookup;
6. the records allowed to join are locally determined;
7. one support is selected rather than several pair and hyperedge candidates;
8. the construction is compatible with restriction of record histories;
9. an eligible event receives a positive rate and an outcome law.

Conditional mutual information directly decides only item 1. D1 tests items
2–8 in exact finite models. Item 9 is outside D1.

The paper makes no continuum or profinite claim. It introduces no emergent
distance, global commit order, fitted future result, or free interaction
coefficient.

## 2. Exact finite center census

### 2.1 Boundary law and screen

A census cell is a nonzero integer table

$$
n(x,z,b)\ge0,
$$

which normalizes to a rational probability law. The finite boundary alphabet
is `B`; the visible screen is a deterministic partition `Y=y(B)`.

A candidate center in the first receipt is a partition `C=c(B)` refining `Y`.
Only the partition matters. Center labels are gauge.

### 2.2 Exact completeness

For a center cell `c`, define

$$
n_c(x,z)=\sum_{b:c(b)=c}n(x,z,b).
$$

The center is complete exactly when every matrix `n_c` has rank at most one.
The receipt checks every `2x2` minor with integer cross-products. Floating
point never decides equality.

Conditional mutual information is only a report:

$$
I(X;Z\mid C)=
\sum_{x,z,c}p(x,z,c)
\log\frac{p(x,z,c)p(c)}{p(x,c)p(z,c)}.
$$

It is evaluated with standard-library `Decimal` at precision 120. Every
reported minimal center is also checked for agreement between exact rank and
high-precision CMI.

### 2.3 Minimality and nonlookup

Complete centers are ordered by partition refinement. A center is minimal when
no strictly coarser complete refinement of `Y` exists. The code enumerates the
full finite partition lattice and retains the whole minimal antichain; it never
chooses the first element.

A center is lookup when every occupied boundary atom is isolated. The finite
positive class requires fewer center cells than occupied boundary atoms. This
is a finite nonreconstruction screen, not an asymptotic compression theorem.

## 3. Controls and scoped positive cells

The registered suite establishes four useful facts.

First, in a factorized control the constant screen is already complete. No
center beyond the screen is identified.

Second, a mixture of product laws may be dependent unconditionally while a
visible two-cell screen is complete. The filter does not invent a redundant
finer center.

Third, a boundary of the form `B=(Y,H,N)` can have a unique minimal center
`(Y,H)` that forgets nuisance `N`. In the exact S2 cell,

$$
I(X;Z\mid Y)=
0.0527386866614484582603934795395073514425327\ldots,
$$

and the unique center has four cells over eight boundary atoms.

Fourth, explicit common-root models have a unique marked ancestor center. For
the two-record S3 cell,

$$
I(A;B)=
0.0457005415253128512036488425382057908953023\ldots.
$$

These are existence results for finite center identification. They do not show
that the center was created by the filter, nor that it selects a support birth.

## 4. Strictly positive center nonuniqueness

Hostile reconstruction replaced the original refinement-sensitive example by
a stronger witness. Its four boundary atoms carry

$$
M_0=\begin{pmatrix}16&4\\4&1\end{pmatrix},\qquad
M_1=\begin{pmatrix}3&2\\12&8\end{pmatrix},
$$

$$
M_2=\begin{pmatrix}1&4\\4&16\end{pmatrix},\qquad
M_3=\begin{pmatrix}2&8\\3&12\end{pmatrix}.
$$

Every entry is positive. Every atomic matrix has determinant zero and mass
25. The constant-screen aggregate is

$$
T=\sum_iM_i=
\begin{pmatrix}22&18\\23&37\end{pmatrix},
\qquad
\det T=400,
$$

so the visible screen is exactly incomplete. Its reported residual is

$$
I(X;Z)=
0.0134798482369601455707275987778085856454737\ldots.
$$

Exhaustive enumeration finds exactly three complete partitions: atomic lookup
and two minimal partitions

$$
C_R=\{\{0\},\{1,2\},\{3\}\},
\qquad
C_C=\{\{0\},\{1\},\{2,3\}\}.
$$

For `C_R`, the nontrivial aggregate is

$$
M_1+M_2=\begin{pmatrix}4&6\\16&24\end{pmatrix};
$$

for `C_C`, it is

$$
M_2+M_3=\begin{pmatrix}3&12\\7&28\end{pmatrix}.
$$

Both have determinant zero. Each center has three cells with masses
`25,50,25`; they therefore tie in cell count and cell-mass entropy. Neither
refines the other.

**Theorem 4.1 (positive finite center nonselection).** Strict positivity,
exact conditional independence, minimality, nonlookup, equal cell count, and
equal cell-mass entropy do not imply a unique boundary center.

The marked-history receipt repeats the result without allowing arbitrary
partitions: two actual boundary fields `R=(0,1,1,2)` and `C=(0,1,2,2)` generate
exactly the two incomparable minimal centers. Their ontology is therefore
load-bearing rather than a comment attached to a partition.

## 5. Marked record histories

The first receipt is a probability theorem, not yet a record theorem. A
hostile ontology audit correctly observed that names such as “support” and
“parent” did no mathematical work. The second receipt therefore defines a
finite marked history containing:

- named record lineages and ports;
- a parent map;
- marked boundary fields with carrier, kind, and stable provenance;
- existing support marks;
- one joint rational law;
- a structural connectivity graph;
- a candidate-support generator;
- a typed record restriction map.

Candidate centers are generated only by marked fields whose carrier contains
the candidate support. Arbitrary partitions of atom indices are excluded.
Candidate support also requires an exposed output port; removing `C`'s port
removes every `C`-bearing candidate in an exact intervention test.

D1B freezes the typed pair `(field name, stable provenance)` as center identity.
If two marked fields induce the same atom partition but carry different typed
pairs, the receipt preserves two center algebras and refuses uniqueness. The
delimiter-adversarial pairs `("A@B","C")` and `("A","B@C")` remain distinct.
Collapsing display aliases or provenance classes would require a separately
stated record-gauge quotient.

This repair changes the interpretation. A unique center means “one marked
field algebra closes this already supplied cut.” It does not mean “the
probability law created a new record object.”

Eligibility also requires the visible screen itself to be exactly incomplete
and the unique completion to use at least one non-screen marked field. Round-2
controls verify that a connected but factorized candidate and a candidate with
a visible complete `H` screen are both refused.

## 6. Locality and the seam license

Statistical factorization is not the definition of causal or record
disconnection. Conversely, a dependent table does not by itself authorize a
nonlocal join.

D1B supplies an explicit ancestry-local seam axiom. Its primitive carriers are
direct structural hyperedges: a sibling group with one recorded parent, an
existing support, or a marked joint boundary field. Candidate supports are
subsets of one primitive carrier, not arbitrary subsets of the transitive
connected component. Overlapping `AB` and `BC` supports make one graph
component but license only `AB` and `BC`; they do not silently license `AC` or
`ABC`.

A hostile locality cell gives two lineages a statistically dependent joint
table but distinct parents, no existing support, and no joint field. The
generator returns no candidate seam and hence no eligible support. This proves
that the marked construction can block unsupported cross-component joining.

It does **not** derive the seam axiom. Connectivity is extra record structure
supplied before the no-silent filter runs. The final interacting click law must
still explain when a locally admissible seam exists and how a genuinely new
connection can arise without presupposing it.

## 7. Candidate support over-eligibility

Use one strictly positive joint law for three records `A,B,C`. Given a marked
root field `H`, the records are conditionally product, with weight vectors

$$
A:(3,1)/(1,3),\quad
B:(4,1)/(1,4),\quad
C:(5,1)/(1,5),
$$

and a duplicated nuisance boundary bit. Common ancestry supplies one direct
three-lineage carrier, so the seam axiom generates
`AB`, `AC`, `BC`, and `ABC` as candidates.

Every pair cut and every bipartition of the triple has the unique marked
nonlookup center `H`:

| cut | visible residual |
|---|---:|
| `A|B` | `0.0457005415253128512036488425382057908953023...` |
| `A|C` | `0.0566330122651324909668082988411019088116763...` |
| `B|C` | `0.0822828785050518463915611582607958826146051...` |
| `AB|C` | `0.111340744596369033106478300440815784872281...` |
| `AC|B` | `0.100408273856549393343318844137919666955907...` |
| `BC|A` | `0.0747584076166300379185659847182256931529778...` |

**Theorem 7.1 (cutwise support nonselection).** Inside the supplied candidate
family, unique no-silent closure of every cut does not select one support:
all three pair supports and the triple support remain eligible.

This theorem is deliberately weaker than claiming equivalence between a
three-pair generative history and one hyperedge history. D1 constructs one
marked common-root law and a family of cuts; it does not construct two
observationally and dynamically equivalent birth kernels.

## 8. Lookup and boundary refusals

Two exact failure modes must remain distinct.

In S6, the only complete boundary partition is atomic lookup. The dependence
is boundary-resolvable but fails the finite nonreconstruction gate.

In S7, even each atomic boundary cell retains a rank-two target matrix. No
partition `c(B)` closes the seam. The current boundary is insufficient; it must
expand, the target must change, or a new physical sector must be supplied.

Therefore positive residue alone never implies birth.

## 9. Marginalization, screen change, and record restriction

The hostile audit found that the first draft had conflated three operations.

### 9.1 Target marginalization

Removing a target variable while leaving the boundary fixed may retain a
center or make it unnecessary. Both occur exactly in D1A. This is a statement
about the chosen prediction target, not a failure of record-history
projectivity.

### 9.2 Screen or grain change

Declaring a boundary field visible can make the screen complete; hiding the
same field can make a center eligible. This changes the experimental
sigma-algebra. It is not a restriction map.

### 9.3 Typed record restriction

D1B projects lineages, ports, parent entries, support marks, boundary-field
carriers, field provenance, and the joint law together. In the common-root
family:

1. restricting `ABC` to `AB` projects `H` to carrier `AB`;
2. the restricted law recomputes `AB` as its sole candidate support;
3. `H` remains the unique nonlookup center;
4. projected eligible supports equal recomputed eligible supports on every
   nonempty subset of `ABC`;
5. direct and successive restrictions agree on the full nonempty subset
   lattice;
6. no support survives on one lineage.

This is a positive control, but hostile round 2 found an exact typed adversary.
For restriction to retained lineages `K`, the implemented support projection is

$$
r_*\mathcal S
=
\{S\cap K:S\in\mathcal S,\ |S\cap K|\ge2\}.
$$

Let a common-root history have records `A,R,Z` and a four-state ancestor field

$$
H=(u,v),\qquad u,v\in\{0,1\},
$$

with every `H` state duplicated by nuisance `N`. Conditional on `H`, let

$$
A\text{ depend on }u,\qquad
Z\text{ depend on }v,\qquad
R\text{ depend on }u\oplus v,
$$

using the strictly positive weight vectors `(3,1)/(1,3)`,
`(5,1)/(1,5)`, and `(4,1)/(1,4)`, respectively. Exact integer aggregation
shows that every pair is independent at the constant screen, while every
bipartition of `ARZ` is dependent there and becomes independent at the unique
four-cell nonlookup field `H`.

Therefore

$$
\operatorname{Eligible}(ARZ)=\{ARZ\},
$$

but after genuine marked restriction to `AZ`,

$$
\operatorname{Eligible}(AZ)=\varnothing,
$$

while projection of the full eligible family gives `{AZ}`.

**Theorem 9.1 (typed eligibility-naturality refusal).** Marked history
restriction itself is path-independent in the executed common-root and parity
families, but under the implemented intersection support projection the
minimal no-silent eligible-support family is not a natural transformation.

The distinction is essential: the implemented marked-data restriction is
path-independent on the executed subset lattices; the nonlinear eligibility
operation is not natural. This is a genuine record-history restriction, not
target marginalization or screen deletion.

## 10. Covariance scope

The partition receipt checks all boundary permutations for cells with at most
four atoms and representative reversal/cycle generators for the eight-atom
cell. It separately relabels `X` and `Z` outcomes. The result is transported
back and compared as a set of partitions.

The algorithm is label-covariant because enumeration, refinement, exact rank,
and minimality depend only on the transported incidence structure. The
executable tests guard the implementation. This finite isomorphism covariance
does not establish physical covariance of a continuum or profinite law.

## 11. What D1 establishes

The surviving principle is:

> A visible record boundary may not silently discard dependence relevant to a
> supplied candidate cut. The dependence must wash out, be represented by a
> licensed boundary-definable center, close only by lookup, or be recorded as
> a boundary failure.

It supplies:

1. an exact incomplete-screen diagnostic;
2. a census of finite boundary completions;
3. unique center identification in some marked cells;
4. factorized, lookup, and no-closure refusals;
5. a test that can operate inside an explicitly local candidate family.

It does not supply:

1. the structural seam license;
2. a unique center in general;
3. one support from the candidate family;
4. equivalence or choice among generative decompositions;
5. a projective eligible-support family;
6. a firing rate, transfer coefficient, or outcome kernel;
7. root creation or genuinely new component joining.

No-silent closure therefore belongs after candidate generation and before
event weighting:

$$
\text{marked history}
\longrightarrow
\text{local candidate supports}
\longrightarrow
\text{no-silent center/refusal family}
\longrightarrow
\text{still-missing selector and rate}.
$$

## 12. Next investigation

D1 moves the foundational problem upstream. Investigation 2 should ask:

> What record-intrinsic diamond operation proposes a new local support without
> presupposing a global construction order or an already shared ancestor?

The strongest route is a marked-diamond amalgamation study:

1. define input and output ports of a sealed diamond from existing record
   ancestry, not from emergent distance;
2. define when two or more diamond boundaries admit a local pushout/amalgam;
3. distinguish an inherited common-root restriction from genuinely new joint
   support;
4. require construction-order gauge invariance for spacelike-independent
   amalgams;
5. pass each proposed support through D1's no-silent and grain-refusal gates;
6. only after support uniqueness, derive or refuse a positive click weight.

Connected-information or Möbius residuals should be tested as diagnostics for
irreducible arity, but not assumed to be probabilities: they can be signed and
can confuse cancellation with absence. Sealed boundary work remains a possible
selector, but D1 shows that it must help propose or distinguish support, not
merely weight a support chosen elsewhere.

## 13. Reproducibility

Run from the repository root:

```bash
python3 v10/code/d1_no_silent_center_exact.py
python3 v10/code/d1b_marked_support_restriction_exact.py
```

The first receipt prints 45/45 checks and uses standard-library `Decimal` at
precision 120 only for CMI reports. The second prints 28/28 checks and uses
integer arithmetic throughout. Neither requires a virtual environment.

The production scenarios are:

- S0 factorized control;
- S1 complete screen;
- S2 unique nonlookup center;
- S3 common-root center;
- S4 three-variable common-root cut;
- S5 robust strictly positive competing centers;
- S6 lookup-only closure;
- S7 no boundary-definable closure;
- S8 target-marginalization and screen-change classification;
- O1 all pair cuts and all triple bipartitions;
- O3 marked locality, support generation, and typed restriction;
- O4 complete-screen refusal, provenance preservation, direct-carrier
  locality, and the parity/synergy projectivity adversary.

## 14. Claims and nonclaims

### Claims

1. Exact finite no-silent residue can identify a unique marked nonlookup center
   inside some supplied candidate cuts.
2. Strict positivity and tied elementary complexity do not guarantee center
   uniqueness.
3. Cutwise unique centers do not select one support from a supplied pair/triple
   family.
4. A supplied ancestry-local seam axiom blocks structurally unlicensed joins,
   even when a statistical table is dependent.
5. Marked history data restrict path-independently in both executed families.
6. Under intersection support projection, the eligible-support family fails
   typed projectivity on an exact parity/synergy history.
7. Target marginalization and screen change are not record restriction.

### Nonclaims

This paper does not claim:

- a final interacting record click law;
- that conditional independence creates a seam, ancestor, or record;
- equivalence between pair-event and hyperedge generative histories;
- a repair of the proved eligibility-projectivity failure;
- a positive event rate, shared-evidence allocation, or transfer coefficient;
- quantum entanglement or transport dynamics;
- a marked profinite extension theorem;
- new geometry, cone, dimension, or scale results.

## 15. Conclusion

The no-silent seam survives, but not as the final dynamic law.

It is correct to say:

> once a local candidate cut has been supplied, its visible boundary may not
> silently erase target-relevant dependence.

It is not correct to conclude:

> that dependence uniquely tells the universe which records must join next.

The exact center census blocks universal uniqueness. The marked common-root
law blocks support selection. The locality repair reveals that the candidate
seam already requires extra record structure. Marked histories restrict
cleanly, but the parity/synergy adversary proves that the eligible-support
family itself is not projective.

Investigation 1 therefore ends with a sharper target for the program: derive a
local, construction-order-gauge diamond amalgamation law that proposes support;
then use no-silent closure as one exact admissibility test on that proposal.
