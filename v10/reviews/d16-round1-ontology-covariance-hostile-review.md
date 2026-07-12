# D16 hostile ontology/covariance review — round 1

**Date:** 2026-07-11  
**Review verdict:** **MAJOR REVISION — `INCOMPLETE-INVESTIGATION`**  
**Narrow exact result:** **FINITE RELABELING-INVARIANT INTERVAL-COEFFICIENT NONSELECTION SUPPORTED**

## Executive finding

D16 proves a clean finite combinatorial result and gives it a physically
overloaded name.

For five frozen strict partial orders, the interval counts `N_k` and every
action in the binary coefficient census are invariant under all vertex
permutations.  Sixteen coefficient packets produce eight distinct phase
signatures.  In particular, `N_0` and `N_2` assign opposite phases to the
four-element diamond and are not related by one common additive phase on the
frozen class.  Therefore **poset relabeling invariance plus interval-count
dependence does not select coefficients**.  That theorem is exact,
reproducible and worth keeping.

It is not yet a theorem of physical general covariance.

The executable has no typed boundary collars or ownership despite their being
part of the frozen source class.  “Boundary ownership” currently means only
that integer indices are in range, nonduplicated and form an antichain.  The
code cannot reject a boundary type/owner violation or test that relabeling
transports those fields.

The regional gluing cell has the same limitation.  It identifies “the last”
left element with “the first” right element positionally, without declared
boundary types, owners, automorphism quotient or action/measure ownership.
It correctly demonstrates that transitive closure creates a cross interval;
it does not define the promised causal-region sewing law.

Likewise, equal phase under all linear extensions removes a birth-order label
from one completed-poset **phase**.  It does not define a measure on
linear-extension fibers, generate the order locally, or eliminate a physical
global scheduler.  The receipt's linear-extension check repeats the same
whole-order phase for every extension; no sequential transition law is
constructed.

The draft is commendably honest about the major missing physics.  It has no
published BDG coefficient packet, normalized quantum measure, D14 records,
pointer environment, commit, collar, join entitlement, matter, stable `3+1`
phase, influence cone, proper units or `G`.  It opens no V9 holdout.  These
absences must remain part of the formal verdict.

The proper round-1 result is therefore:

```text
FINITE POSET-ISOMORPHISM INVARIANCE                  PROVED
BINARY INTERVAL-COEFFICIENT SELECTION                REFUTED
PHYSICAL GENERAL COVARIANCE                          NOT PROVED
TYPED/OWNED REGIONAL SEWING                          NOT IMPLEMENTED
QUANTUM MEASURE + RECORD/BIRTH LAW                   NOT IMPLEMENTED
DIMENSION/CONE/UNITS/G                               NOT DERIVED
FORMAL D16 VERDICT                                   INCOMPLETE-INVESTIGATION
```

## Exact reproduction

The standard-library source was copied to an isolated temporary tree.  Normal
and optimized Python produced byte-identical stdout and byte-identical packets.
The regenerated packet matches the primary artifact.

```text
checks                         = 20/20
normal stdout SHA-256          = 212df3c028e0fa7387170ba14dce541e868983e75c6a09c8bf6cb735635424ef
-O stdout SHA-256              = 212df3c028e0fa7387170ba14dce541e868983e75c6a09c8bf6cb735635424ef
generated JSON SHA-256         = d6b6efa782750bfcd59b79e8ebc849b2c82ae7daeb64027bef186fbf10a70ec0
primary JSON SHA-256           = d6b6efa782750bfcd59b79e8ebc849b2c82ae7daeb64027bef186fbf10a70ec0
semantic SHA-256               = 107bedcdc071c0be21edc12aa928dc57fd45416206d4049ad643aa67712dd04f
source SHA-256                 = 989f996af855daceffa8bff68d687ada60ab4f35a1736b76e6c0508156f7e386
normal/-O stdout               = byte-identical
generated/primary JSON         = byte-identical
```

One cell advertised as exact uses Python binary floats:

```text
1 / |Aut(C)|,
normalized Born weights 0.5.
```

The current tiny denominators make the comparisons reproducible, but a source
calling itself exact should use `fractions.Fraction` for these measure cells.
This is a hardening request rather than the central ontology blocker.

## Opening ledger

| ID | Severity | Opening | Required repair |
|---|---:|---|---|
| O1 | **MAJOR** | Poset relabeling invariance is called exact general covariance. | Rename the executable theorem `finite order-isomorphism covariance/nonselection`; reserve physical general covariance for the full state/measure/boundary/observable law. |
| O2 | **MAJOR** | Frozen typed boundaries and ownership are absent from `CausalOrder`. | Add typed collar objects, owner identities and transport under permutation; execute type/owner violation controls. |
| O3 | **MAJOR** | Gluing is positional and supplies no boundary quotient, automorphism measure or action ownership. | Glue matching declared collars, quotient the shared interface once, and print cross/boundary terms plus the chosen measure convention. |
| O4 | **MAJOR** | Linear-extension phase equality is promoted toward “no global clock.” | Distinguish whole-poset phase invariance from presentation-fiber measure and from a local sequential growth law.  Execute a pushforward or retain C8 open. |
| O5 | **MODERATE** | “Interval locality” can sound nearest-neighbor/local-causal although `N_k` scans all comparable pairs. | Use `order-intrinsic interval dependence` or `causal-set quasilocal/nonlocal`; quantify the support/nonlocality scale for BDG packets. |
| O6 | **MODERATE** | `1/|Aut|` is displayed as the unlabeled orbit measure although it is one supplied groupoid convention. | Separate unit weight per isomorphism class, labeled sums, `1/n!` quotient and groupoid `1/|Aut|`; derive none from covariance alone. |
| O7 | **MODERATE** | Opposite single-history phases are called inequivalent predictions without a state/measure/interference observable. | Keep algebraic action non-equivalence; add a common-boundary sum/decoherence functional before claiming different probabilities. |
| O8 | **PASS/OPEN** | Dimension tags are explicitly inputs and no BDG coefficients are claimed. | Add real BDG provenance before any dimension claim; retain calibration/emergence distinction. |
| O9 | **PASS/OPEN** | Quantum measure, D14 records, commit, collar, join and matter are absent and acknowledged. | Do not promote the interval action until an explicit packet supplies them. |
| O10 | **PASS** | `3+1`, cones, proper units and `G` are not claimed; V9 remains closed. | Preserve this refusal. |
| O11 | **FORMAL BLOCKER** | C0/C2/C5–C11 are not closed. | Formal verdict remains `INCOMPLETE-INVESTIGATION`; freeze only the narrowed coefficient nonselection theorem after repair. |

## O1 — label gauge is not full general covariance

The exact theorem proved by `permute()` is:

```text
If two finite relation matrices differ only by a vertex bijection, their
interval-count vector and interval-action value agree.
```

This is isomorphism invariance of a scalar poset functional.  It is necessary
for a label-free causal-set law.  It is not sufficient for physical general
covariance, which would also require the transformation/invariance of:

```text
typed boundaries and ownership;
state/boundary amplitudes;
history/orbit measure;
matter and record fields;
observables;
sewing/quotient data;
regulator and continuum limit.
```

The source check label

```text
exactly generally covariant under relabeling
```

conflates the necessary discrete label gauge with the completed physical
claim.  The theorem draft repeats “exact finite general covariance plus
interval locality.”

Use one of:

```text
finite relabeling covariance;
order-isomorphism invariance;
discrete label gauge on the frozen scalar functional.
```

Then state that whether a complete causal-set quantum law realizes physical
general covariance remains C5/C6 work.

## O2 — boundary type and ownership are not implemented

The frozen source class requires typed boundary antichains/collars and says a
physical relabeling must preserve relation, boundary types and ownership.

The executable stores only:

```text
past_boundary: tuple[int,...]
future_boundary: tuple[int,...].
```

`__post_init__` checks:

- indices are unique and in range; and
- elements in each boundary tuple are incomparable.

It has no boundary type, owner, collar identity or direction-specific
payload.  The exception message `invalid boundary ownership` therefore
mislabels index validation as ownership validation.

`permute()` maps the integer set and sorts it.  There is no type/owner record
to transport, so C1 cannot test the frozen equivalence relation.

### Required exact repair

Introduce, for example:

```text
BoundaryPort(element, kind, owner, collar_id, orientation).
```

Make permutation transport the entire port record.  Reject:

```text
wrong boundary kind/orientation;
owner reassignment;
duplicate collar identity;
gluing unequal types/owners;
non-antichain boundary support.
```

Only then can the executable claim the typed C0/C1 class.

## O3 — the gluing cell proves an obstruction, not a sewing law

The finite obstruction is correct.  Identifying the middle point of two
two-element chains and taking transitive closure produces a three-element
chain with one `N_1` interval.  Therefore naive addition misses a cross-region
term.

But `glue_at_last_first()` does not inspect the `past_boundary` or
`future_boundary` fields.  It always identifies the last numeric element of
the left order with numeric element zero of the right order.  Neither input
chain even declares a boundary in the test.

No choice is made for:

```text
matching type/owner;
shared boundary state;
automorphism quotient;
measure on internal labels/orders;
ownership of |C| on the identified point;
ownership of cross intervals;
boundary/corner action;
sum over alternative fillings.
```

Thus C5 is not passed.  The code supplies the mandatory **failed-naive-
additivity countercontrol**, which is useful evidence that a future sewing law
needs more data.

Repair by implementing typed collar gluing and comparing an explicitly
defined composite action/amplitude with the regional pieces plus printed
boundary/cross terms.

## O4 — linear extensions do not supply a local growth law

For each frozen order, the code enumerates every linear extension.  It then
checks

```python
len({action_a.phase(order) for _ in order.linear_extensions()}) == 1
```

The expression does not construct an extension-dependent history.  It repeats
the same completed-order phase once per extension.  Its truth follows directly
from the fact that `phase()` receives only `order`.

This proves absence of a birth-order label from the scalar action.  It does
not prove:

- that a sum over labeled growth histories will not multiply the order by its
  number of linear extensions;
- that all paths to one unlabeled order have the same transition-product
  probability;
- that a quotient/pushforward measure is normalized;
- that enabled births can be computed from local collar data; or
- that no global mechanism is needed to choose the next order.

The theorem draft substantially acknowledges this, but the sentence “removes
a label/global-birth-order presentation from the whole-history weight” is too
broad because only the phase, not the whole weight, exists.

Use:

```text
The scalar phase factors through the completed unlabeled order.  D16 has not
defined the measure on presentation fibers or a sequential growth law.
```

Rideout–Sorkin-type discrete general covariance is a constraint on a complete
growth measure/path product, not obtained from phase invariance alone.

## O5 — interval dependence is quasilocal/nonlocal

`N_k` loops over every comparable pair `(x,y)` and counts the entire open
interval between them.  Even `N_0` is link-local only in the order-theoretic
sense; higher `N_k` couple pairs beyond immediate links, and a BDG-style
nonlocal operator uses a dimension/scale-dependent layer combination.

Therefore “intrinsic interval locality” must not be read as nearest-neighbor
locality, continuum microcausality or a finite propagation theorem.  The
protocol says this, but the theorem draft does not include a dedicated scope
sentence.

Rename the property `order-intrinsic interval dependence` and state whether a
future coefficient packet is local, quasilocal or nonlocal at its declared
discreteness/nonlocality scale.

## O6 — automorphism counting does not select a measure

The automorphism counts are correct on the frozen objects:

```text
antichain4 24
chain4      1
V3          2
Lambda3     2
diamond4    2.
```

The following weight

```text
1 / |Aut(C)|
```

is natural for a groupoid cardinality or for a labeled sum divided by `n!`.
It is not forced by relabeling invariance.  A sum over isomorphism classes can
assign unit or other intrinsic weights; a labeled presentation sum has
`n!/|Aut(C)|` representatives; gauge fixing may introduce its own factors.

The correct conclusion is the one the prose mostly gives: an orbit convention
must be supplied.  The executable label should not call `1/|Aut|` **the**
unlabeled orbit measure.

Add exact `Fraction` arithmetic and show the alternative conventions before
declaring the measure/gauge-volume field open.

## O7 — action inequivalence versus physical prediction

The coefficient nonselection theorem is algebraically valid.  `S_A=N_0` and
`S_B=N_2` are different invariant functions and do not differ by one constant
on the frozen class.

The opposite phase of one isolated complete diamond is not by itself a
different probability: both have unit modulus, and a common phase of a single
closed alternative is unobservable.  Relative phase becomes physical only in
a supplied sum over alternatives with common boundary data and a state/effect
or decoherence functional.

The receipt correctly shows that raw pure phases do not normalize.  It should
therefore call check 13 a different **action amplitude assignment**, not yet a
different observed prediction.  To close the empirical version, give chain
and diamond a common typed boundary/measure, sum them coherently, and compare
a normalized boundary observable under the two packets.

## Quantum measure and records

**Open and honestly stated.**

The `raw_born_mass=2` control successfully refutes the idea that `exp(iS)`
alone is a normalized history law.  Dividing two unit masses by their sum is
only an illustrative classical normalization after the alternative set has
been supplied.  It is not a quantum measure, decoherence functional or a
derivation of the alternative domain.

D16 supplies none of:

```text
boundary/cosmological state;
complex measure and gauge volume;
convergence/regulator;
record environment and pointer basis;
explicit commit/protected future/live collar;
component ownership or join entitlement;
matter interaction.
```

Accordingly it does not reach the D14 interface.  The theorem draft and packet
ceiling say so.  `CAUSAL-ACTION-TO-RECORD-BRIDGE-CONDITIONAL` is not yet an
executed result; it is the appropriate future grade after these fields are
supplied.

## BDG and dimension provenance

**Open and honestly scoped.**

The two `dimension_tag` objects use arbitrary illustrative beta vectors.  The
check proves only that a programmer can attach dimension metadata and choose
different coefficients.  It is not a derivation or audit of published BDG
coefficients.

The draft explicitly denies implementing them.  This is important because
Benincasa–Dowker operators/actions are matched to continuum behavior in a
declared dimension and depend on a discreteness/nonlocality scale; later BDG
continuum work also studies dimension-specific bulk and joint terms
([Machet–Wang](https://arxiv.org/abs/2007.13192)).  Recovering the dimension
used to choose the packet is calibration, not emergence.

C4 requires a future provenance table containing at least:

```text
source/equation and convention;
continuum dimension/signature;
sprinkling/manifoldlike assumptions;
discreteness density and nonlocality scale;
layer cutoff/smearing;
bulk versus boundary/joint terms;
normalization and finite-size regime.
```

No `3+1` selection claim is currently made, so there is no present overclaim.

## Geometry, scales and V9

**PASS by refusal.**

D16 has no selected quantum measure or complete causal action packet.  It has
not derived:

```text
a stable manifoldlike phase;
dimension estimator target/correction;
matter influence/dispersion;
cone anisotropy versus scale;
proper units;
G;
a fixed uncertainty band;
two complete candidates with differing predictions.
```

Therefore C9/C10 do not fire and V9 remains sealed.  A four-dimensional
sprinkling or four-dimensional BDG coefficients would input the target
dimension/cone context and could support calibration only.  Preserve this
strict boundary.

## Gate adjudication

| Gate | Round-1 result |
|---|---|
| C0 exact partial orders | **PARTIAL.** Strict relation validation passes; typed boundary collars and ownership absent. |
| C1 label gauge | **PASS for untyped poset relabeling only; physical/general covariance open.** |
| C2 locality meaning | **PARTIAL.** Protocol is honest; theorem/code labels need quasilocal/nonlocal wording. |
| C3 coefficient nonselection | **PASS for the frozen scalar phase family, independent of missing physical measure.** |
| C4 dimension provenance | **OPEN.** Tags are illustrative; no BDG packet/provenance implemented. |
| C5 regional gluing | **FAIL/PARTIAL.** Cross-interval obstruction passes; typed sewing/measure/ownership absent. |
| C6 quantum measure | **OPEN.** Missing-data obstruction shown correctly. |
| C7 records and birth | **OPEN.** No D14 interface or matter/environment/commit packet. |
| C8 no global clock | **OPEN.** Completed-order phase ignores labels; presentation measure/local growth absent. |
| C9 geometry predictions | **OPEN.** No dimension/cone/unit/`G` predictions. |
| C10 empirical discriminator | **OPEN; V9 correctly refused.** |
| C11 hostile closure | **OPEN.  This review finds major repairs.** |

## Required repair order

1. Downgrade every “general covariance” theorem label to finite
   order-isomorphism/relabeling covariance.
2. Add typed/owned boundary collars and transport them under relabeling.
3. Replace positional gluing with matching typed collar gluing and explicit
   shared-boundary/cross-interval/action ownership.
4. Separate linear-extension phase invariance from presentation-fiber measure
   and local sequential growth.
5. Print alternative orbit-measure conventions using exact rational
   arithmetic.
6. Call interval counts quasilocal/nonlocal and attach scale provenance to any
   real BDG packet.
7. Keep action-function nonselection separate from observable probability
   differences until a quantum measure/state is supplied.
8. Retain all record, geometry, scale and V9 gates open.

## Verdict

**MAJOR REVISION — `INCOMPLETE-INVESTIGATION`.**  The exact 20-check receipt
supports one important negative theorem:

```text
ON THE FROZEN FIVE UNLABELLED POSET SHAPES,
RELABELING INVARIANCE + INTERVAL-COUNT DEPENDENCE
DO NOT SELECT THE BINARY COEFFICIENT PACKET.
```

It does not yet support the stronger phrase “exact finite general covariance
plus interval locality,” because typed/owned boundaries, regional measure,
sewing and physical observables are absent.  Nor does it remove a global clock
from a generative law; it only removes linear-extension labels from a supplied
completed-order phase.

The missing quantum measure, D14 record packet, join law, BDG provenance,
stable `3+1` phase, cone, units and `G` are correctly acknowledged.  No V9
holdout should open.
