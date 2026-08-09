# The split in distribution

**v14 CR-B — stochastic refinement.**  Paper 06.  Pin:
`v14/note-cr-batch-pins.md`, CR-B section (v14 ledger #30, `1cfee4fc0891`).
Instrument: `v14/code/crb_stochastic_exact.py`; receipt
`v14/code/crb_stochastic_receipt.json`; output
`v14/code/crb_stochastic_output.txt`.  Every number below is rendered from the
receipt object.

---

## 1. The question, and why it is not R6a's

R6a asked whether the pinned record grammar forces a *value* for the split —
which pair $(n_1, n_2)$ a coarse interval's $n$ division events divide into when
the dyadic move subdivides it.  It answered `R6A-NO-MOTIVATED-SPLIT`: the split
is a class-(iii) freedom, a fiber of between 19683 and 1257565061957837936381
choices, and nothing in the pinned layer picks one of them.

That answer leaves a door open.  A refinement that cannot name a split might
still *know how splits are distributed*.  Physics is full of such situations:
the microstate is not determined but its law is, and the law is what the theory
predicts with.  So this unit asks the weaker, and strictly more generous,
question.  Not *which split*, but: **is there a conditional law over the split
fiber that the pinned structure forces?**

The criterion is the standard one and the pin names it: for a group acting on a
finite fiber the invariant probability measures form a simplex whose vertices
are the orbit-uniform measures, so a unique invariant law exists exactly when
the action is transitive.  Where it is not, the number that matters is the
dimension of what is left over — the orbit-simplex dimension, one less than the
orbit count.  This unit measures that dimension everywhere, and it does not take
the criterion on trust: at every cell small enough to carry the linear system,
the dimension of the affine space of invariant probability measures is computed
by exact Gaussian elimination over the rationals and compared against orbits
minus one.

**The answer is negative, and the negative is sharper than R6a's.**  Symmetry
leaves a simplex of astronomical dimension at every cell of the census; no other
pinned object narrows it; and the object that would be needed is identifiable
and absent.  The verdict head is `CRB-BLOCKED-AT-NO-PINNED-STOCHASTIC-LAW`.

---

## 2. The arena, declared

Sites $X = (\mathbb{Z}_3)^2$; the declared links $e_1$, $e_2$, $e_1+e_2$; the
geometry record $n_\ell(x) \in \mathbb{Z}_{>0}$ counting division events in the
record interval from $x$ to $x+\ell$; the readout
$q_{ij}e_\ell^i e_\ell^j = n_\ell(x)$ at density weight $w=0$, with a record
admissible iff $q$ is positive definite at every site.  Twenty-seven coarse
intervals.

The dyadic move sends $L \to 2L$, carries the coarse site $x$ to $2x$, and
subdivides the coarse interval $(x,\ell)$ at $2x+\ell$.  Count additivity is
forced by the counting semantics.  **The split** is the choice, at each of the
27 intervals, of the first half $a$ in the range 1 to $n-1$.

Two fibers are in play and the difference matters later.  The RAW fiber imposes
only positivity of both halves.  The ADMISSIBLE fiber additionally requires the
refined readout to be positive definite at the nine coarse image sites — the
only sites at which all three refined counts are determined by the split alone.

**Declared-arena rows** (RUNBOOK §15): boundary = the 27 intervals and the fiber
over them; family = I7's nine admissible records plus the declared count box;
law = the dyadic move; state = the split; arena = the symmetry inventory of §4;
provenance = R6a's receipt at DELIVERED-UNDER-PANEL status, read by hash
`022c3f488a93`, with every fiber count rebuilt here and anchored against it.

---

## 3. The fiber rebuild

Nothing is imported.  The record constructors, the readout, the admissibility
predicate and the fibers are rebuilt from the pinned declarations, then checked
cell by cell against the predecessor:

> the split fibers are rebuilt here from the pinned declarations alone and agree with the R6a receipt at 27 of 27 cells, spanning 19683 to 1257565061957837936381 over the 6 records that admit the move

Three of the nine admissible records — `G-ANISO`, `G-CURVED`, `G-FLAT` — carry a
count-1 interval and admit no subdivision at all.  Count 1 is a floor: the
flattest arena is the one that cannot be refined.  That is R6a's finding, and it
is reproduced here as a precondition, not assumed.

The predecessor's other tables are reproduced too, each by a route of this
unit's own: the stabiliser orders and their full orbit profiles on the 27
intervals; the chart-equivariant fibers, re-derived as the number of chart-group
FIXED POINTS of the raw fiber by a signed union-find; the declared count box;
and R6a's entire iteration table, reproduced with the balanced split
$a=\lfloor n/2\rfloor$ before that split is used for anything.

---

## 4. The symmetry inventory, as data

The pin asks for *every* pinned symmetry acting on a fiber.  The inventory is
built rather than assumed, and each row carries its provenance class.

| group | order | provenance |
|---|---|---|
| TRANS | 9 | PINNED — the chart translations |
| SIGMA | 2 | PINNED — the $d!$ direction relabellings |
| CHART | 18 | PINNED — the declared chart group |
| EXT | 108 | DECLARED-EXTENSION — translations times the $A_2$ point group |
| LOCALFLIP | $2^{27}$ | DECLARED-EXTENSION — the per-interval reversal group |

The extension is not an invention: the declared links together with their
negatives *are* the $A_2$ root system, and its automorphism group — the maximal
subgroup of $GL(2,\mathbb{Z})$ carrying the declared link set into itself up to
sign — is dihedral of order 12, built here by enumeration and verified closed.
It realises all six permutations of the three link directions, extending the
pinned $\Sigma = S_2$ to $S_3$, and it contains the point reflection, which acts
on a split by REVERSING it, $a \mapsto n-a$.  It is not pinned, and is entered
as arena data, never as a conclusion.

**A measured theorem falls out, and it is the structural finding of the unit:**

> the pinned chart group has order 18; the largest group the declared link set admits has order 108; and exactly 18 of those 108 elements preserve the block structure the admissible fiber is built on

Every element outside the pinned chart group reverses at least one interval, and
a reversal exchanges the two halves of a split.  The admissibility constraint
that makes a refined record a record is a constraint on FIRST halves — the
coarse image sites are the only sites where all three refined links are
determined — so it is intrinsically reversal-asymmetric.  The pinned chart group
is therefore not an arbitrary choice: **it is exactly the part of the largest
available lattice group that acts on the admissible fiber at all.**  Whether a
particular reversal nevertheless preserves a particular record's fiber is
measured per record, not assumed; it does for `G-DIAG2`, whose admissible set is
symmetric about $n/2$, and fails for `G-OFFDIAG`, where the direct orbit walk
records 39364 escapes — configurations the reversal throws out of the fiber.

---

## 5. The orbit decomposition, and three routes to it

> the orbit decomposition is computed at 24 (record, group) cells, cross-checked by direct enumeration at 4 of them and by a closed form at 5

Route one is Cauchy–Frobenius over the cycle structure of each group element,
with a signed cycle rule: around a cycle of intervals the split is transported,
and an odd number of reversals forces $a = n-a$, which has one solution at even
$n$ and none at odd $n$.  Route two is a direct orbit walk applying GENERATORS
only, run wherever the fiber falls under the declared cap of 20000 — a different
computation, not the same sum rearranged, and gated to have actually enumerated.
Route three is a closed form written from the group's structure rather than from
this file's cycle machinery: the translations' orbit count on functions from the
site set into the admissible set is $(k^9 + 8k^3)/9$.  All three agree at every
cell.

The two ends of the census:

> G-DIAG2's fiber of 19683 splits falls into 1230 orbits under the pinned chart group, with orbit sizes 3 x 1, 14 x 3, 9 x 6, 232 x 9, 972 x 18

> G-ANISO2's admissible fiber holds 1257565061957837936381 splits and 139729451328658254141 orbits, an invariant simplex of dimension 139729451328658254140

---

## 6. The invariant-measure census

> no cell of the census is transitive: 0 of 24, and the orbit-simplex dimension runs from 637 to 1257565061957837936380

Nowhere is the action transitive.  The criterion is not cited but measured — at
24 cells the linear system's solution space is computed exactly and equals
orbits minus one every time — so "unique invariant law iff transitive" is a
measurement in this unit, not an appeal.

**Why it fails is visible at the level of a single interval, where enumeration
is exact:**

> a single interval carrying n events has n - 1 splits: under the pinned group the simplex has dimension n - 2 and is a point only at n = 2, and under the declared reversal extension it is a point only at n = 2 and n = 3

The pinned group contains no element that reverses an interval, so its
stabiliser acts *trivially* on that interval's own fiber: the orbits are the
points, and the simplex has dimension $n-2$.  It collapses to a point only at
$n=2$, where the fiber is already a single split and there was nothing to
choose.  The declared reversal extension halves the dimension and buys exactly
one more count value, $n=3$.  That is the whole reach of symmetry over a split.

Over the declared count box the same statement is exact:

> of the 361 admissible count vectors in the declared box, 261 are splittable, exactly 1 has a fiber the pinned symmetry acts transitively on, and under the declared reversal extension 4 do -- 0 of them inside the declared record family

The one pinned-transitive vector is $(2,2,2)$ — R6a's unique-admissible-split
vector, whose fiber is a single point.  **Uniqueness by triviality, not by
selection.**  The four reversal-transitive vectors all lie outside the declared
record family.

---

## 7. Selection candidates beyond symmetry

Symmetry is not the only thing that could force a law, so seven further
candidates were registered and tested.

> 7 selection candidates beyond symmetry are tested and 0 are forced

**The record's own counts as weights.**  Five weight functionals are expressible
from the pinned data alone — uniform, binomial, linear, product, min-half — and
at every count value in the family they are pairwise distinct.  The counts admit
a family of laws; they do not select one.

**Maximum entropy under pinned constraints.**  This is the candidate that must
be audited rather than applied, because maximum entropy is motivated only if a
pinned declaration forces the constraint set.  The audit reads every declaration
the pinned receipt carries and classifies it:

> the pinned layer carries 0 distribution-level declarations out of 27, so maximum entropy has no constraint set of its own to act on

With no moment constraint anywhere, maximum entropy degenerates to the uniform
law on whatever support is declared — and the two supports the pinned grammar
makes available, the raw fiber and the admissible-at-images fiber, give
measurably different laws at five of the six records that admit the move.  A
principle whose answer is a function of an undeclared choice is not a forcing.
The one ratio-valued declaration in the pinned layer, the test-class norm, is
read as a bit by its own source ("boolean in disguise on this carrier"), which
is anchored verbatim.

**The uniform law on the admissible fiber.**  Invariant, but neither canonical
nor even well-posed interval by interval:

> the uniform law on the admissible fiber fails to factorise at 4 of the 6 records that admit the move

The admissibility constraint couples the three splits at a site, so under this
law "the law of a split" does not factorise into per-interval laws at all.

**The barycentre of the invariant simplex.**  The orbit sizes are unequal —
`G-DIAG2`'s 1230 orbits come in sizes 1, 3, 6, 9 and 18 — so the simplex's own
centre and the uniform law on the fiber are two *different* invariant laws.  Two
canonical-looking constructions disagree, measured.  On a chart-fixed split the
uniform law puts mass $1/19683$ and the barycentre $1/1230$.

**The front.**  The only functional the pinned data offers is the
front-proportional one, $a = n_\ell(x)\,N(x)/(N(x)+N(x+\ell))$, censused over
the declared profile family:

> the front-proportional split returns an admissible integer at 165 of 1944 cells, is non-integral at 141, out of range at 468 and undefined at 1170

And a value rule, even where defined, is not a law: it names a point, and a
point mass is invariant only if that point is fixed.

**The drag field.**  The index-set question is prior to the stochasticity
question and settles it: the drag carries two tangent indices or three link
indices; the split fiber at an interval carrying $n$ events has $n-1$ points;
the number of declared maps from one onto the other is counted, and it is zero.

**The equivariant (deterministic) laws.**  R6a's chart-equivariant splits are
exactly the invariant point masses — the vertices of the simplex that happen to
be deterministic.  There is never exactly one of them (the smallest is 3), so
demanding determinism does not select either.  This is R6a's value-level finding
recovered, unchanged, one level up.

---

## 8. Why no pinned object could have done it

The candidates fail one at a time; the census says why they must.  Every
declaration in the pinned layer is a statement about a record, a number or a map
— a VALUE-level statement.  None is a statement about a probability law.  And
the dynamics cannot supply what the declarations lack:

> the pinned dynamics is a bijection at 3168 of 3168 sampled cells with 0 collisions, so its pushforward carries point masses to point masses

$H_a[N]$ is a bijection with a closed-form inverse exhibited in the pinned
source (anchored verbatim), so no iterate of it turns a determinate split into a
distribution over splits.  The count of stochastic objects in the pinned layer
is zero.

**The missing object, named.**  What a motivated split distribution would
require is a joint law for WHERE inside a record interval its $n_\ell(x)$
division events fall — equivalently, the transition kernel between the
interval's endpoints whose renewal count is $n_\ell(x)$.  That is a
transition-matrix-layer object.  R0's inheritance carries the record layer (I7:
counts, front, $H_a[N]$, record-IS-metric) and no transition layer at all.  This
is the exact distribution-level counterpart of R6a's gated mechanism — that the
datum a split needs is the datum the record does not carry — and it identifies
what a successor would have to import: not a better symmetry argument, but the
renewal grammar itself.

---

## 9. Iteration in distribution

Under repeated refinement the simplex does not settle.

> at the one record that reaches a second level the fiber grows from 1257565061957837936381 to 8384268790037013033304454089952502124028416 under the first declared completion while the acting group stays at 9, so the simplex dimension grows from 139729451328658254140 to 931585421115223670367161565730857830751295; under the second completion the group doubles to 18 and the fiber, at 11709683552580630561569484011873192401249489, still outruns it

The fiber outruns the symmetry at every cell where a second level exists.  Two
honest qualifications ride with that number.  First, the level-1 reading is
COMPLETION-RELATIVE: the 54 refined links that lie on no coarse interval are
free, and the two declared completions of the diagonal give different level-1
fibers and different acting groups (9 versus 18).  The conclusion survives both,
because the fiber multiplies by more than $10^{21}$ either way while the group
at most doubles.  Second, everywhere else the fiber collapses to empty at the
first step, because a descendant interval reaches count 1 and count 1 admits no
split.  Growth or collapse; never stabilisation.

---

## 10. Controls

> the 2 positive controls each return a unique invariant measure and the 2 negative controls each return a positive-dimensional simplex

The positive controls are fibers a group acts transitively on — a count-3
interval under the reversal, and a cyclic group of order 5 on five points.  On
each, the unique invariant measure is FOUND, by the linear system coming out
zero-dimensional, not by citing the orbit theorem.  The negative controls are
asymmetric fibers, on which the instrument returns a positive-dimensional
simplex.  The instrument can say UNIQUE, and does, when uniqueness is there.

---

## 11. The verdict, as emitted

```
CRB-BLOCKED-AT-NO-PINNED-STOCHASTIC-LAW<FIBERS=REBUILT-27-OF-27-CELLS-0|SPAN-19683..1257565061957837936381|MOVE-ADMITTED-BY-6-OF-11|SYMMETRY=PINNED-CHART-18|SIGMA-2|EXTENSION-108|BLOCK-PRESERVING-18-OF-108|ORBITS=CELLS-24|ROUTES-4|CLOSED-FORM-5|MIN-638-MAX-1257565061957837936381|TRANSITIVE=UNIQUE-0-OF-24|SIMPLEX-DIM-637..1257565061957837936380|PER-INTERVAL=PINNED-DIM-N-MINUS-2|FLIP-DIM-CEIL-N-MINUS-1-OVER-2-MINUS-1|TRANSITIVE-AT-N-2-3|LATTICE=SPLITTABLE-261-OF-361|PINNED-TRANSITIVE-1|FLIP-TRANSITIVE-4|IN-THE-DECLARED-FAMILY-0|SELECTION=CANDIDATES-7|FORCED-0|REFUTED-7|MAXENT=PINNED-DISTRIBUTION-LEVEL-DECLARATIONS-0-OF-27|SUPPORT-RELATIVE-RECORDS-5|NON-FACTORISING-4|DETERMINISM=STOCHASTIC-PINNED-OBJECTS-0|H-BIJECTION-3168-OF-3168|COLLISIONS-0|ITERATION=CEILING-2|GROWS-2|COLLAPSES-6|SINGLE-LEVEL-4|FIBER-OUTRUNS-GROUP-True|COMPLETION-RELATIVE-True|CONTROLS=POSITIVE-2-UNIQUE-2|NEGATIVE-2-SIMPLEX-DIM-3-2|MISSING=THE-INTERVAL-POSITIONAL-LAW-=-THE-TRANSITION-KERNEL-BETWEEN-AN-INTERVALS-ENDPOINTS-WHOSE-RENEWAL-COUNT-IS-N|R0-CARRIES-THE-RECORD-LAYER-I7-AND-NO-TRANSITION-LAYER>
```

Read plainly: **there is no motivated split distribution at the pinned scope,
and the obstruction is not a missing symmetry but a missing layer.**  Symmetry
was given every chance — the pinned group, its maximal lattice extension, and
the count-preserving ceiling — and left a simplex of dimension up to
1257565061957837936380.  Seven further candidates were tested and none is
forced.  The object that would decide the question is named: the
interval-positional law, the transition kernel R0's inheritance does not carry.

R6a showed the continuum question is unposable from inside the pinned grammar at
the level of values.  This unit closes the obvious escape: it is unposable in
distribution too, and for a reason one level deeper — the pinned layer contains
no probabilistic object of any kind.

---

## 12. Scope and honesty

This unit takes no scaling limit, measures no invariant trajectories, and claims
nothing about records outside I7's declared family and the declared count box.
The extension groups are DECLARED, labelled as such, and reported beside the
pinned results rather than in place of them.  The level-1 iteration reading is
completion-relative and says so.  The predecessor is cited throughout at
DELIVERED-UNDER-PANEL status: if the R6a panel moves any of the anchored
numbers, the anchor gate here fails loudly rather than silently inheriting them.

Instrument: 97 gates, all passed; 52 anchors; 42 mutants, no survivors.  Two plain runs byte-identical.  Arithmetic is
exact throughout — `int` and `Fraction` only, enforced by an AST scan of the
source.

---

*Sources, hash-verified at run time:* `v14/note-cr-batch-pins.md`
(`1cfee4fc0891`), `v14/note-r0-founding-pin.md` (`e9d2bedff244`),
`v14/code/r6a_refinement_receipt.json` (`022c3f488a93`, DELIVERED-UNDER-PANEL),
`v13/code/ha_successor_receipt.json` (`542b8735daf0`),
`v13/paper-ha-successor.md` (`f286ba10d2d9`),
`v13/code/ha_successor_exact.py` (`d44cb72f8ee9`).
