# v13 RQ0 — physical overlap of quantum regional instruments

**Status:** TERMINAL, STRICT, 2026-07-30 — delivered v13 #17
(`8d071641ecc3d028c4ee3355e4faacb368840e95`), hostile round frozen v13 #19
(`c17a6349a465248f735650d98e8f9e2627e9161d`), bounded repair v13 #21
(`6c3ef116cbc1102d74d4f15266f4a9a5c497e7c9`), terminal adjudication v13 #22.

**Repair pin:** `v13/note-rq0-physical-overlap-repair-pin.md`, commit
`b05ab95d6721d104a561875bc39aa6daa03f875e`.

**Antecedent verdict:** hostile review frozen at v13 #14 and accepted at
v13 #15.  Commits `307c36f` and `1537b14` remain immutable.

**Repair hostile round:** `ACCEPT-WITH-FIXES`, frozen at v13 #19,
adjudicated at v13 #20, repaired at v13 #21, and conferred terminal after the
post-commit rerun at v13 #22.  This file incorporates all six bounded fixes.

**Executable and receipts:** `v13/code/rq0_physical_overlap_exact.py`,
`v13/code/rq0_physical_overlap_output.txt`, and
`v13/code/rq0_physical_overlap_receipt.json`.

**Highest restored rung:** **`RQ0-FACT-DESCENT`.**

> Three equal-dimensional finite quantum regional instruments, non-padding
> under the exhaustive common-configuration-relabelling $4\times2$ test,
> occur as typed subinstruments of one fixed, canonically authenticated finite
> master instrument.
> Their common W3-stable record is the actual pullback of a shared overlap
> record through exact amplitude-instrument morphisms, not a consequence of
> matching laws.  `Reg`, `FactIface`, and `Rec` are distinct and the physical
> triple descends.  No causal, spacetime, field, or gravity claim is made.

This note repairs the two load-bearing defects in the earlier factual-base
delivery: regional diversity no longer comes from spectator padding, and the
common record is now connected to each region by process morphisms.  The
earlier one-region write/preserve/erase result survives; the old value-level
coupling and Born-shadow refinement survive only as controls.

---

## 1. Claim boundary

At this rung, a “region” is an operationally closed finite amplitude-
instrument family.  It is not yet a spacetime region.  The construction has
no global event set, hidden directed graph, coordinate, metric, causal cone,
field propagator, stress object, or gravitational dynamics.

The result is exact at one finite scope:

- every boundary space has dimension eight;
- amplitudes lie in $\mathbb Q(\sqrt2)$, including its rational subfield;
- the regional gauge is common configuration relabelling and exact real
  boundary signs;
- admissible subinstrument identifications use signed-permutation boundary
  maps;
- the anti-padding search exhausts all $8!=40{,}320$ common carrier
  relabellings for the declared $4\times2$ split;
- this finite test makes no arbitrary-unitary tensor-irreducibility claim;
- no numerical tolerance, random seed, fitted geometry, or field data occur.

The full complex $U(1)$ boundary gauge is not implemented.  All basis
preparations and the full configuration probe are explicit operational-access
postulates, not derived measurement instruments.

---

## 2. The equal-dimensional quantum regions

### 2.1 Primitive type

The primitive object remains

$$
D=
\bigl[
X_D,\mathrm{Prep}_D,\mathrm{Amp}_D,
U_D^{\mathrm{write}},\mathrm{Pres}_D,
\mathrm{Erase}_D,\mathrm{Ctrl}_D,\mathrm{Obs}_D
\bigr]/G_D^{\mathbb R}.
$$

$\mathcal R(D)$ is not primitive.  It is derived only after the instrument
and the accessible record candidate have been frozen.  Here

$$
G_D^{\mathbb R}
=\text{common configuration relabellings}
\times\{\pm1\}\text{ boundary rephasings}.
$$

An arrow carries a family label, source boundary, target boundary, and exact
amplitude matrix.  A morphism is more restrictive than matrix-size
agreement: it has typed boundary maps, an injective arrow-label map, exact
intertwiners, preparation compatibility, and readout-projector pullbacks.

### 2.2 Amplitude family

Write the three carrier bits as branch $b$, memory $r$, and auxiliary $a$.
The common write is

$$
U^{\mathrm{write}}
=\operatorname{CNOT}_{r\to a}
 \operatorname{CNOT}_{b\to r}H_b.
$$

It couples branch to record and record to auxiliary.  The common preserving
continuation is

$$
V^{\mathrm{core}}=\operatorname{CNOT}_{a\to b},
$$

which leaves $r$ unchanged.  The three regional preserving continuations are

$$
P_1=\operatorname{CNOT}_{b\to a},
$$

$$
P_2=\operatorname{CNOT}_{b\to a}H_b,
$$

$$
P_3=\operatorname{CNOT}_{b\to a}H_aH_b.
$$

Each acts on the auxiliary and leaves the memory bit fixed.  Each region also
contains a coherent eraser: it first uncopies $a$ from $r$ and $r$ from $b$,
then applies a region-specific coherent post-processing arrow.  The no-write
control is $H_b$.

Thus each region has the same eight-dimensional carrier and five substantive
arrows:

| arrow | family | role |
|---|---|---|
| `write` | write | common W3 record writer |
| `core-preserve` | preserve | common overlap continuation |
| `regional-preserve` | preserve | region-specific accessible dynamics |
| `erase` | erase | region-specific coherent erasure |
| `no-write` | control | failed-record anchor |

By construction, the displayed arrows directly couple branch to record,
record to auxiliary, and branch to auxiliary.  This is a transparent
constructor annotation, not an independently counted receipt gate and not a
causal graph.  The load-bearing anti-spectator result is instead the exact
family-level factorization search below.

### 2.3 Derived quantum seam

The frozen record candidate is the diagonal readout

$$
r(x)=x_r\in\{0,1\}.
$$

For all three regions, exact computation gives:

- $H_{\mathrm{corr}}$ true for the write on all eight admitted basis
  preparations;
- $H_{\mathrm{corr}}$ false for the no-write control;
- $H_{\mathrm{avail}}$ true for both preserving continuations;
- zero preserving cross-sector and within-sector cut coherence;
- zero preserving configuration defect $\Delta^B$;
- a defined, zero record-level residual for both preserves;
- $H_{\mathrm{avail}}$ false for the eraser;
- an undefined record quotient under erasure, together with restored
  cross-sector coherence and nonzero $\Delta^B$.

The eraser measurements are:

| region | nonzero cross-sector coherence pairs | nonzero $\Delta^B$ entries |
|---|---:|---:|
| $D_1$ | 16 | 16 |
| $D_2$ | 32 | 32 |
| $D_3$ | 32 | 32 |

Occurrence and continuation-relative availability therefore come from the
same regional amplitudes.  No independent memory witness is attached after
the fact.

---

## 3. Why the three regions are genuinely different

### 3.1 Same dimension, accessible invariant

Carrier dimension cannot distinguish the regions: all are eight.  Instead,
take the multiset of nonzero support counts over the complete accessible
preserve family.  Signed row/column permutations and arrow-label permutation
cannot change this multiset.  The exact values are

$$
D_1:\{8,8\},\qquad
D_2:\{8,16\},\qquad
D_3:\{8,32\}.
$$

The full signatures also include preserve-write composite support, eraser
support, defect support, and sorted Born-composite invariants.  All three are
distinct.  Regional diversity is therefore carried by accessible amplitude
dynamics rather than filenames, dimension, or dormant matrix entries.

### 3.2 Exhaustive anti-padding test

For each common relabelling $\pi\in S_8$, every substantive regional arrow is
conjugated by the corresponding permutation matrix.  For the declared
$4\times2$ split, an $8\times8$ matrix factors as $A_4\otimes B_2$ only if its
exact rearrangement has rank one.  The executable chooses an exact nonzero
pivot and tests the complete pivot-cross rank-one identities, then asks
whether **all five arrows** factor under one and the same relabelling.

The result is:

| family | relabellings tested | common product witness |
|---|---:|---|
| old q=3 padded control | 1 before witness | identity relabelling |
| $D_1$ | 40,320 | none |
| $D_2$ | 40,320 | none |
| $D_3$ | 40,320 | none |

The old control is the exact q=3 member of the earlier family: the two-qubit
write is tensored with an independent identity, while preserve/erase are
tensored with an independent Hadamard.  Its immediate detection shows that
the anti-padding instrument can return the opposite answer.

The result is scoped to common carrier relabellings and the nontrivial
$4\times2$ split.  Since swapping the two tensor factors is itself among the
carrier relabellings, this also covers the corresponding $2\times4$
presentation.  It is not a theorem about arbitrary dimensions.
Nor does it exclude product structure exposed only by an arbitrary unitary
change of tensor factorization.  “Non-padding” below always means the
exhaustive common-relabelling $4\times2$ result at the declared real
signed-permutation gauge scope.

---

## 4. The finite master and typed regional morphisms

### 4.1 Master instrument

The master $\mathsf E$ is a finite local operational witness with the same
three eight-dimensional boundaries.  Its accessible arrow family is the
union of:

- the shared write, shared preserve, and no-write arrows;
- the three regional preserves;
- the three regional erasers.

It is not a global universe, an ambient event set, or a global state of the
theory.  Its only role is to witness one finite compatible family of local
amplitude instruments.

The no-argument constructor, all readouts, the admissible morphism class, the
three regional embeddings, and the three overlap embeddings have the
same-file canonical specification digest

```text
132116e2a5b5880443eb609ce52fa940d71211746ba5d7b728984d08c9dbd7d9
```

The constructor, typed law controls, canonicalizer, and structural bridge
validators have the separate same-file canonical source digest

```text
e5661e6566279997e3ebd7bbd6a18e99cc635e2d7cd6f6e0e16c1b1030f5bcc3
```

These digests authenticate the delivered representation and evaluation
surface.  They do **not** retroactively prove that the exact construction was
historically preregistered independently of its author.  Immutable Git
provenance instead fixes the repair pin, original delivery, hostile report,
and adjudication as distinct events.  On every execution the family is built
and canonically authenticated before the equal-law controls are evaluated;
structural validation is a separate digest-free function.  A source audit
confirms that the constructor consumes no target law, marginal law, requested
fact map, coordinate, metric, or field object.

### 4.2 Instrument morphisms

For this exact fixed-carrier cover category, an admissible morphism $f:D\to E$
contains:

1. signed-permutation boundary maps $f_j:V_j^D\to V_j^E$;
2. a total injective map of accessible arrow labels preserving family and
   source/target type;
3. the exact intertwiner for every mapped arrow,
   $$
   f_tU_D=U_Ef_s;
   $$
4. compatibility of every admitted basis preparation and the actual
   preparation;
5. exact projector pullback for every accessible readout value.

The positive embeddings use identity boundary maps but remain explicit typed
objects:

$$
j_a:D_a\hookrightarrow\mathsf E,
\qquad a=1,2,3.
$$

Their arrow maps send the three common arrows to the master core and the two
regional arrows to the matching regional master arrows.  All boundary,
arrow, preparation, and readout diagrams pass.  Replacing one mapped
regional-preserve arrow by the common preserve makes every $j_a$ fail.  A
unitary Hadamard boundary map also fails because it lies outside the declared
signed-permutation morphism scope.  Composition-compatible sign gauges on
both source and target preserve the morphism equations.

---

## 5. Physical overlap and the regional cover category

### 5.1 Common amplitude subinstrument

Define $O$ as the amplitude subinstrument containing:

- the common write;
- the common preserving continuation;
- the no-write control;
- the common preparation scope;
- the frozen memory and configuration readouts.

There are explicit embeddings

$$
i_a:O\hookrightarrow D_a.
$$

For every pair of regional images inside $\mathsf E$, exact intersection of
the mapped accessible arrow families is

$$
\{\texttt{core.write},\texttt{core.preserve},
\texttt{core.no-write}\}.
$$

The triple intersection is the same nonvacuous core.  Within the declared
finite subinstrument category, the executable also verifies the pairwise
pullback universal property: every declared object mapping into both members
of a pair maps into $O$.

### 5.2 `Reg`

The positive finite category is

$$
\mathbf{Reg}=\{O,D_1,D_2,D_3,\mathsf E\},
$$

with five identities, the three $i_a$, the three $j_a$, and the common
composite $O\to\mathsf E$: twelve morphisms in total.  All 22 composable
morphism pairs equal their declared composites.  The three composites

$$
O\xrightarrow{i_a}D_a\xrightarrow{j_a}\mathsf E
$$

are exactly equal as typed morphisms.  Identities, composition, all
intertwiners, and the finite pullback tests pass.  The three regional images
cover the master because their accessible arrow-family union is exactly the
master family.

This earns the pin's internal rung `RQ0-REGIONAL-SITE` at the declared finite
operational-family scope.  In standard terminology the constructed object is
a finite amplitude-subinstrument cover category or atlas: no Grothendieck
topology is declared.  It is not a causal or spacetime site.

### 5.3 Refinement

$j_1:D_1\hookrightarrow\mathsf E$ is a positive fixed-carrier
intervention-family refinement: it adds accessible continuation choices and
satisfies the same amplitude-level morphism equations.  It is not a
spacetime-resolution limit.

The earlier $D_1\to D_2\to D_3$ marginalization squares amplitudes before
discarding a product ancilla.  It is therefore retained under the corrected
name **Born-shadow product coarse-graining** and fails the present
instrument-refinement type gate.

---

## 6. The common record is an actual restriction

For a memory value $v\in\{0,1\}$, let $P_v^D$ be the diagonal record
projector at the write boundary of instrument $D$.  Every $i_a$ and $j_a$
satisfies

$$
P_v^{\mathrm{source}}
=f_1^{\mathsf T}P_v^{\mathrm{target}}f_1
$$

exactly.  Thus the regional memory proposition is literally the pullback of
the master/core proposition.  It is not a new binary variable selected
because its probability happens to match.

After the amplitude cover category and morphisms pass, define the persistent
record algebra by the W3 predicates:

$$
\operatorname{Rec}(D)
=\operatorname{Bool}\{r:
H_{\mathrm{corr}}(U_D^{\mathrm{write}},r)=1,
\ H_{\mathrm{avail}}(V,r)=1
\text{ for every declared preserve }V\}.
$$

All five objects $O,D_1,D_2,D_3,\mathsf E$ derive the two-atom Boolean
algebra generated by memory.  No record algebra is present in the primitive
region tuple.

Now distinguish the types:

- `Reg` has amplitude instruments as objects and instrument morphisms as
  arrows;
- `FactIface` has derived stable-record algebras as objects and value/algebra
  restrictions as arrows;
- $\operatorname{Rec}:\mathbf{Reg}^{\mathrm{op}}\to\mathsf{FactIface}$ maps
  each validated regional morphism to its induced projector pullback.

`Rec` contains no call to the marginal-law or GHZ-control routines.  A static
source audit verifies that it uses only H-corr, H-avail, and induced projector
pullback.  The five identity laws and every declared contravariant
composition law pass.  In particular, all three paths

$$
\operatorname{Rec}(\mathsf E)
\longrightarrow\operatorname{Rec}(D_a)
\longrightarrow\operatorname{Rec}(O)
$$

equal the direct restriction $\operatorname{Rec}(\mathsf E)\to
\operatorname{Rec}(O)$.  The three core restrictions are the same identity
map on $\{0,1\}$.  This is the physical triple-descent result.

The old nine-arrow binary-value object is retained as a type control.  It is
`FactIface`-shaped and obeys its value-level groupoid laws, but it contains no
instrument morphisms and therefore fails the `Reg` schema.

---

## 7. Why matching laws still do not certify a fact

### 7.1 Diagonal versus anti-diagonal control

Two exact four-bit amplitude instruments have the same three fair binary
marginals.  Their joint record supports are respectively

$$
\{(0,0,0),(1,1,1)\}
$$

and

$$
\{(0,1,0),(1,0,1)\}.
$$

Each control is a typed 16-dimensional amplitude `Instrument`; both writes
and preserves are unitary, both joint readouts pass the scoped H-corr and
H-avail tests, and a deliberately inadequate law-only predicate accepts both.
But their forced pair maps differ:

| pair | diagonal control | anti-diagonal control |
|---|---|---|
| $1\to2$ | identity | complement |
| $2\to3$ | identity | complement |
| $1\to3$ | identity | identity |

For each control the executable constructs an explicit candidate
`InstrumentMorphism` into the fixed eight-dimensional master.  Both candidates
fail at the first structural gate: their three boundary pairs have dimensions
$16\to8$, so no signed-permutation boundary identification exists.  The
reported reason is `boundary_dimension_mismatch`; this is no longer rejection
by a positive-family digest or untyped dictionary schema.  The positive fact
certificate instead comes from the fixed, canonically authenticated
$O\to D_a\to\mathsf E$ morphisms.

### 7.2 Equal law, no bridge

A separate eight-dimensional rogue instrument $N$ has the same write and
the same stable fair memory law as the positive regions.  Its regional
preserve uses the exact rational rotation

$$
\begin{pmatrix}
3/5&4/5\\
4/5&-3/5
\end{pmatrix}
$$

on the branch before an auxiliary coupling.  It passes H-corr and H-avail.
Nevertheless, its preserve Born-entry multiset differs from each of the four
preserve-family arrows in the fixed master.  That multiset is invariant
under every signed row/column relabelling, so no admissible arrow image—and
hence no full regional embedding—exists in the declared finite morphism
scope.

The result is therefore

$$
\boxed{\texttt{SAME-LAW-NOT-SAME-FACT}.}
$$

Marginal equality is printed only after the structural certificate as a
consequence.  Phase is never used as a fact-identity criterion.

---

## 8. Four-gate accounting

| object | referent | necessity | no-smuggling | discriminator |
|---|---|---|---|---|
| master $\mathsf E$ | finite accessible amplitude family | the earlier free coupling did not connect regions | constructor consumes no law, fact map, geometry, or field | post-selected diagonal/anti-diagonal controls fail its schema |
| instrument morphism | signed-permutation boundary maps plus arrow/readout diagrams | value projections did not connect full processes | fact identity is not an input | mapped-arrow mutant and rogue region fail |
| overlap $O$ | common amplitude subinstrument inside $\mathsf E$ | a value groupoid is not a physical overlap | computed from mapped arrow families | positive pair/triple pullbacks pass; value-only object fails `Reg` |
| `Reg` | amplitude instruments and typed morphisms | prevents region/fact-map type compression | no record law enters its arrows | unitary nonmonomial map and old value groupoid fail |
| `FactIface` | derived Boolean record algebras and restrictions | records are not primitive region components | constructed only after W3 and `Reg` pass | erasure removes availability; no-write removes occurrence |
| `Rec` | contravariant record assignment induced by projectors | expresses descent without token identification | statically barred from law-only routines | three physical paths agree; law-only controls remain ambiguous |

The classifications are:

- **definitions:** the finite instrument, signed-permutation morphism,
  subinstrument cover category, `FactIface`, and `Rec` types;
- **postulates:** operational nomological individuation, basis-preparation
  access, complete configuration-probe access, the fixed admissible-extension
  class, and the exact real gauge scope;
- **inherited theorems:** Paper 1's W3 seam/composition result and Paper 2's
  distinction between shared law, shared fact, and shared token;
- **constructed objects:** $D_1,D_2,D_3,O,\mathsf E$, all $i_a,j_a$, `Reg`,
  `FactIface`, `Rec`, and the negative controls;
- **exact measurements:** W3 status, coherence/defect/residual counts,
  dynamic invariants, exhaustive anti-padding search, morphism diagrams,
  pullbacks, category laws, and triple descent;
- **conjectures/open objects:** localized quantum subinstrument, operational
  influence, causal order, volume, conformal geometry, fields, and gravity.

---

## 9. Receipt and outcome

The executable reports **69/69 passing exact checks**.  Those checks are
classified mechanically as 4 anchors, 2 canonical-authentication checks,
3 static audits, 7 type checks, 3 schema checks, 45 measurements, 5 controls,
and 0 semantic declarations.  Outcome labels and prose nonclaims are not
counted as checks.  Every rung is derived from a named prerequisite mapping.

Deliberately corrupting the **observed** active-pin hash in memory exits with
status 1 at **68/69**, closes every positive rung, prints `highest restored
rung: NONE`, and labels the receipt invalid.  It does not alter an expected
constant.  Two complete text runs and two complete JSON runs must be
byte-identical and exactly regenerate the stored receipts.  No legacy code is
imported; the old padded family and old shadow refinement are reconstructed
only as negative/type controls.

The earned ladder is:

| rung | result |
|---|---|
| `RQ0-REGIONS-CONSTRUCTED` | earned |
| `RQ0-REGIONAL-SITE` | earned at the finite amplitude-subinstrument scope |
| `RQ0-FACT-DESCENT` | earned through physical projector pullback |
| causal or geometric arena | not attempted |

The first unresolved obstruction is a typed, gauge-invariant localized
quantum subinstrument.  It is only a successor referent; no influence
relation is defined here.  A separately pinned unit would have to construct
that object before asking whether operational influence can yield causal
order.

$$
\boxed{
\texttt{RQ0-FACT-DESCENT, TERMINAL AT DECLARED FINITE SCOPE; HALT BEFORE RQ0-C1.}
}
$$
