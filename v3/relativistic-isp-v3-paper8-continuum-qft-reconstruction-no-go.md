# Relativistic ISP V3 Paper 8: Continuum QFT Reconstruction And No-Go Theorems

Preprint, not peer reviewed, version 2026-05-28.

Author: Felix Robles Elvira

Status: theorem-level draft. This paper is the QFT reconstruction gate after
V3 Papers 1-7. It proves a positive restricted reconstruction/matching theorem
for enriched ISP finite batteries and a sharp negative theorem for Gamma-only
claims.

The result is intentionally mixed:

```text
enriched ISP + instruments + CAR/local-net/covariance data
-> restricted finite-battery QFT local-net reconstruction/matching;

bare Gamma alone
-> not full relativistic QFT reconstruction.
```

This is not a retreat. It is the Barandes-aligned way to say exactly what the
stochastic process determines, what the declared instruments determine, and
what remains representation enrichment.

Boundary warning: the positive local-net result in this paper is a finite
operational reconstruction/matching theorem on declared test batteries. It is
not a Haag-Kastler AQFT construction, not a proof of the time-slice axiom,
not a spectrum-condition theorem, and not a type-III local-algebra theorem.
Likewise, every covariance statement in the positive branch is a sampled
finite-battery matching statement or a declared continuum-representation
enrichment. It is not an exact nontrivial Lorentz action on one fixed finite
configuration set.

## 1. Main Question

Are projective ISP kernels, instruments, and minimal enrichment sufficient to
reconstruct known local QFT structures?

The answer of this paper is:

1. **Positive.** A restricted enriched ISP package reconstructs a finite-battery
   operational local net and matches the Wilson single-species Dirac/CAR QFT
   benchmark on the declared test class.
2. **Branch-complete.** The no-Wilson branch reconstructs a multi-taste local
   net, a selected-taste Wilson reduction, or a retained-record channel, but not
   hidden single-species QFT.
3. **Negative.** Bare Gamma does not reconstruct full QFT. In particular, it
   does not determine CAR/local-net data, polarization/vacuum data, signed
   metric/Clifford orientation, or the operational instrument layer.

## 2. Barandes-Aligned Reconstruction Rule

The primitive ISP datum is a whole-process stochastic endpoint structure with
declared records. A QFT reconstruction theorem may use Hilbert, CAR, local-net,
or covariance data only if those data are typed as enrichment or reconstructed
from declared operational data.

Thus the rule is:

```text
Do not claim that a representation layer has been reconstructed unless the
theorem derives it from the declared ISP data.
```

In this paper the Wilson and no-Wilson QFT structures are not Gamma-only
outputs. They are reconstructed/matched from the enriched datum declared by V3
Paper 1 and controlled by V3 Papers 3-7.

### Definition 2.1: Layer-Typed Reconstruction

A reconstruction claim is **Gamma-only** if its input is only the projective
stochastic endpoint datum `{\mathfrak D}^{\Gamma}` and the output is required to
be invariant under all Gamma-equivalences.

A reconstruction claim is **operational** if its input also includes declared
record-labelled instruments, effects, and source protocols. Its output may be
an effect system, a finite operational local net, or finite-battery statistics,
but not an undeclared Hilbert/CAR representation.

A reconstruction claim is **enriched QFT matching** if its input includes
declared representation data such as CAR fields, smearing maps, polarization,
vacuum/state data, Clifford/principal-symbol data, or covariance
representations. Its output may match a QFT local net on a finite test class,
but the imported representation data must be listed as imports rather than
quietly counted as Gamma-level consequences.

A reconstruction claim is **Haag-Kastler/AQFT-level** only if it additionally
constructs a quasilocal `C^*`-algebra or local von Neumann net with isotony,
additivity or an explicitly declared substitute, spacelike commutativity,
time-slice behavior where claimed, a spectrum/positive-energy condition, and
the relevant continuum completion. No theorem in this paper is AQFT-level
unless these extra clauses are explicitly listed.

### Lemma 2.2: Layer Ledger Criterion

Every theorem in this paper has a unique layer type in Definition 2.1.
Consequently a theorem proved at the enriched QFT matching layer cannot be
quoted later as a Gamma-only reconstruction theorem.

### Proof

The input list of a theorem determines its layer. Gamma-only theorems are
constant on Gamma-equivalence classes; operational theorems may depend on
declared instruments and effects; enriched QFT matching theorems may depend on
declared representation data. These inputs are nested but not equivalent.
Forgetting the layer would enlarge the theorem's input silently, which changes
the theorem. Therefore layer type is part of the theorem statement. `square`

### Lemma 2.3: Finite Stochastic Isomorphisms Are Permutations

Let `K:X\to X` be a stochastic map on a finite set, represented by a
row-stochastic matrix. If `K` has an inverse `L` that is also stochastic, then
`K` is a permutation matrix.

### Proof

Write `KL=I`. For `x\ne z`,

```math
0=(KL)_{xz}=\sum_y K_{xy}L_{yz}.
```

Every summand is nonnegative. Hence, whenever `K_{xy}>0`, one must have
`L_{yz}=0` for all `z\ne x`. Since row `y` of `L` sums to one, this forces
`L_{yx}=1`. Now if a row of `K` had two positive entries `K_{xy_1}` and
`K_{xy_2}`, then rows `y_1` and `y_2` of `L` would both be the point mass at
`x`, making `L` non-invertible. Thus every row of `K` has exactly one positive
entry, and that entry is one. Invertibility then forces distinct rows to hit
distinct columns, so `K` is a permutation. `square`

### Corollary 2.4: No Nontrivial Finite Lorentz Action By Stochastic Isomorphisms

An exact covariance action by invertible stochastic maps on a fixed finite
configuration set can only act by permutations. Therefore a nontrivial Lorentz
boost cannot be represented in this paper as an exact stochastic automorphism
of one fixed finite regulator state space.

The only admissible finite covariance statements in this paper are:

1. equality or convergence of declared finite-battery statistics for sampled
   Lorentz-related tests;
2. projective compatibility of different finite batteries approximating
   Lorentz-related continuum tests;
3. an imported continuum covariance representation listed as enrichment.

None of these is a finite-regulator proof of full Lorentz covariance. `square`

### Definition 2.5: Continuum Reconstruction Audit

A finite-battery theorem in this paper may be quoted as a continuum
reconstruction theorem only after the following additional clauses have been
proved or explicitly imported:

1. a directed projective family of finite test batteries whose union is
   cofinal in the target continuum test class;
2. tightness or another compactness criterion for the associated states or
   correlation functionals;
3. uniqueness or selection of the projective limit, not merely existence of
   subsequential limits;
4. continuum isotony and additivity, or named substitutes with their exact
   scope;
5. spacelike commutativity in the continuum completion;
6. a time-slice axiom if time-slice behavior is claimed;
7. a spectrum or positive-energy condition if relativistic QFT structure is
   claimed;
8. a quasilocal `C^*`-algebra or von Neumann local-net completion if AQFT-level
   language is used;
9. a continuum covariance representation acting on the limit object, not an
   exact nontrivial stochastic automorphism of a fixed finite set.

If these clauses are absent, the theorem remains a finite-battery
reconstruction/matching theorem even when its tests are labelled by continuum
regions.

## 3. Import Contract

### Gamma-level imports

From V3 Papers 2-4:

1. finite/projective endpoint kernels `\Gamma_a[O]`;
2. projective maps `P_{ab}`;
3. comparison maps `J_R=\Gamma_R\Gamma_0^{-1}`;
4. exchange defects `E_{R,S}`;
5. branchwise interacting curvature coefficients on the tested classes.

### Operational imports

From V3 Papers 5-7:

1. Wilson-compatible instruments and effect batteries;
2. no-Wilson taste instruments and pointer records;
3. finite-battery foliation independence for exchange-summable path classes;
4. recorded reject/no-click/selected-taste outcomes.

### Representation-enriched imports

From V3 Papers 1, 3, 5, and 6:

1. Hilbert/Fock/CAR representation data where used;
2. smearing maps `I_a`;
3. polarization/vacuum or state data;
4. local-net assignment data;
5. Clifford/principal-symbol data if metric orientation is claimed;
6. asymptotic covariance data for sampled Lorentz-related batteries.

### Forbidden imports

This paper does not import:

```text
Gamma-only CAR reconstruction;
Gamma-only local-net reconstruction;
exact finite-lattice Lorentz covariance;
nonperturbative interacting QFT;
non-Abelian gauge continuum theory.
```

Those are either no-go targets here or later-paper targets.

## 4. Reconstruction Data

Let `{\mathfrak D}^{\rm enr}` be an enriched ISP datum in the sense of V3 Paper
1:

```math
{\mathfrak D}^{\rm enr}
=
({\mathfrak D}^{\Gamma},\mathsf W,\mathsf I,\mathsf E,\mathsf H,
\mathsf F,\mathsf N,\mathsf S,\mathsf C,\mathcal A_{\rm adm}).
```

For a region `O` and regulator `a`, let:

```math
{\mathcal B}_a(O)
```

be the finite battery generated by declared sources, effects, detector records,
comparison-map weak probes, and local CAR polynomials whose supports lie in the
regulated approximation of `O`.

Let

```math
{\mathfrak A}_a^{\rm ISP}(O)
```

denote the operational algebra generated by these declared effects and
record-labelled instruments. If a CAR representation is imported, let

```math
{\mathfrak A}_a^{\rm CAR}(O)
```

be the local CAR algebra generated by the smeared finite fields supported in
`O`.

### Definition 4.1: Reconstructible Finite-Battery Local Net

An enriched ISP datum reconstructs a finite-battery local net on a continuum
region family `{\mathcal O}` if, for each `O\in{\mathcal O}`, there are finite
local algebras/effect systems `{\mathfrak A}_a(O)` and states `\omega_a` such
that:

1. **Isotony.** If `O_1\subset O_2`, then
   ```math
   {\mathfrak A}_a(O_1)\subset{\mathfrak A}_a(O_2)+o_a(1)
   ```
   on the finite battery.
2. **Locality.** If `O_1` and `O_2` are spacelike separated, then
   ```math
   [A_a,B_a]\to0
   ```
   in all tested matrix elements for `A_a\in{\mathfrak A}_a(O_1)` and
   `B_a\in{\mathfrak A}_a(O_2)`.
3. **Projective stability.**
   ```math
   P_{ab}{\mathcal B}_b(O)-{\mathcal B}_a(O)P_{ab}\to0
   ```
   in the declared finite-battery topology.
4. **Foliation independence.** The finite probabilities are independent of
   exchange-summable hypersurface paths in the sense of V3 Paper 7.
5. **Continuum matching.** There is a target continuum local net
   `O\mapsto{\mathfrak A}(O)` and state `\omega` such that every finite
   declared local test converges:
   ```math
   \omega_a(A_a(I_a f_1,\ldots,I_a f_n))
   \to
   \omega(A(f_1,\ldots,f_n)).
   ```

This definition is finite-battery reconstruction, not universal constructive
QFT. Clause 5 is a matching clause to a declared or independently constructed
continuum target. It is not, by itself, a construction of the target continuum
net or of its covariance, spectrum, or algebraic completion.

## 5. Operational Local-Net Reconstruction

### Theorem 5.1: Enriched Finite Operational Net Reconstruction

Assume an enriched ISP datum with:

1. a declared region family `{\mathcal O}`;
2. record-labelled local instruments `\mathsf I`;
3. separating effect systems `\mathsf E`;
4. projectively controlled endpoint kernels and comparison maps;
5. exchange-summable foliation control from V3 Paper 7;
6. finite residual bounds for restriction, inclusion, and locality maps.

Then the datum reconstructs a finite-battery operational local net

```math
O\mapsto{\mathfrak A}_{\rm op}^{\rm ISP}(O)
```

up to the declared residuals. In particular, isotony, operational locality,
projective stability, and foliation-independent probabilities hold on the
finite battery.

### Proof

The separating effect systems identify operational equivalence classes of local
events. Region inclusion gives the restriction/inclusion maps, whose residuals
are assumed controlled. Projective stability follows from the projective
control of kernels and instruments. For spacelike separated regions, local
detector/instrument commutation gives exact locality for detector effects, and
V3 Paper 7 controls any remaining dynamical ordering dependence by summable
exchange defects. Therefore the local operational algebras/effect systems form
a finite-battery net up to the stated residuals. `square`

### Interpretation

This is a genuine ISP reconstruction theorem, but only at the operational
finite-battery level. It reconstructs the local operational net carried by the
declared instruments. It does not by itself reconstruct a CAR field algebra,
vacuum, Hilbert space, or stress-energy tensor.

## 6. Wilson Positive QFT Benchmark

### Theorem 6.1: Wilson Single-Species Local-Net Matching

Consider the Wilson branch with:

1. the Wilson smearing maps, polarization, and propagator convergence of V3
   Paper 3;
2. Wilson-admissible interactions and curvature channels of V3 Paper 4;
3. Wilson-compatible instruments and finite benchmark equivalence of V3 Paper 5;
4. foliation independence from V3 Paper 7;
5. fixed finite particle number, finite energy window, and compact finite test
   family.

Then the enriched Wilson ISP datum reconstructs/matches the single-species
Dirac/CAR local-net benchmark on the finite test class:

```math
\omega_{a,W}^{\rm ISP}(A_a(I_a^W f_1,\ldots,I_a^W f_n))
\to
\omega_D(A(f_1,\ldots,f_n)).
```

The reconstructed/matched net satisfies, on the finite test class:

1. isotony;
2. CAR locality/microcausality;
3. sampled Lorentz-related finite-battery covariance matching;
4. Wilson-compatible interaction curvature probes;
5. foliation-independent endpoint statistics.

### Proof

The local CAR polynomial convergence and Wilson finite-battery equivalence are
V3 Paper 5, using the concrete smearing, polarization, propagator, and
Wilson-admissible interaction package from V3 Paper 3. Locality follows from
the continuum Dirac/CAR anti-commutator limit on spacelike-separated test
functions. Foliation independence and sampled Lorentz-related equality are V3
Paper 7. Isotony is inherited from the declared local smearing support and local
CAR net. The interacting curvature probes are precisely the declared
Wilson-compatible weak probes of V3 Papers 4-5. `square`

The phrase "sampled Lorentz-related equality" means equality or convergence of
the declared finite statistics for the selected Lorentz-related tests. By
Corollary 2.4, it does not mean that the fixed finite regulator carries an
exact nontrivial Lorentz group action by stochastic isomorphisms.

### What Is Reconstructed And What Is Imported

The Wilson theorem reconstructs/matches finite local statistics and the tested
local-net behavior from the declared enriched ISP package. It imports:

```text
CAR representation,
smearing maps,
polarization/vacuum data,
Wilson regulator choice,
finite-energy test sector,
instrument/effect system,
sampled covariance representation.
```

Therefore the theorem is an enriched reconstruction/matching theorem, not a
Gamma-only theorem.

## 7. No-Wilson Alternative

### Theorem 7.1: No-Wilson Local-Net Classification

Consider the no-Wilson detail-preserving branch of V3 Paper 6 with foliation
control from V3 Paper 7. Then the reconstructed/matched local-net target is
exactly one of:

1. a taste-blind operational quotient equivalent to the Wilson finite battery;
2. an ordinary multi-taste Dirac/CAR local net;
3. a selected-taste Wilson reduction with recorded reject outcomes;
4. an ISP-retained-record local net with taste-channel statistics absent from
   the single-species Wilson benchmark.

It is not an undeclared hidden single-species QFT.

### Proof

V3 Paper 6 gives the four-way taste-sector classification. Foliation
independence from V3 Paper 7 preserves branch distinctions under spacelike path
changes. Therefore the local-net target is determined by the declared
instrument algebra: taste-blind quotient, multi-taste CAR algebra, recorded
selected-taste quotient, or retained-record taste algebra. A hidden
single-species target would require silently erasing or importing the taste
sector, which violates the Paper-6 classification and the Paper-1 admissibility
criterion. `square`

## 8. Gamma-Only No-Go

### Theorem 8.1: No Gamma-Only Reconstruction Of Full Relativistic QFT

No reconstruction rule whose input is only the bare projective stochastic datum

```math
{\mathfrak D}^{\Gamma}
```

can reconstruct, on the V2/V3 tested classes, full relativistic QFT structure
including all of:

1. local CAR/field algebra;
2. vacuum/polarization or positive-energy state;
3. local operational effect system;
4. sampled Lorentz/covariance representation;
5. signed Clifford/principal-symbol metric orientation;
6. branch distinction between Wilson single-species and no-Wilson taste sectors.

### Proof

V3 Paper 1 proves that Gamma-only rules are constant on Gamma-equivalence
classes and gives independent obstruction witnesses: phase-sensitive coherent
composition, CAR/local-net data, and signed metric orientation. V3 Papers 5 and
6 add a branch witness: the same broad stochastic architecture supports Wilson
single-species and no-Wilson taste targets only after declared representation,
instrument, and regulator data. Bare Gamma alone does not specify which
instrument algebra, CAR algebra, polarization, Wilson term, taste readout, or
covariance representation is intended. Therefore a Gamma-only rule cannot
return the full QFT structure uniquely and correctly on all tested classes.
`square`

### Corollary 8.2: Representation Existence Is Not Reconstruction

If a Hilbert/CAR/local-net representation can be placed above a bare stochastic
kernel but is not uniquely determined by the declared ISP data, then its
existence is a representation theorem, not an ISP reconstruction theorem.

### Proof

Reconstruction requires a specified map from declared data to the target
structure. Mere existence supplies no such map and is compatible with multiple
inequivalent enrichments over the same Gamma-equivalence class. `square`

## 9. Reconstruction Status Theorem

### Theorem 9.1: Exact V3 QFT Status

After V3 Papers 1-8, the QFT status of relativistic ISP is:

```text
Bare Gamma:
  no full QFT reconstruction.

Operational enriched ISP:
  finite operational local-net reconstruction on declared batteries.

Wilson enriched ISP:
  finite-battery single-species Dirac/CAR local-net benchmark matching.

No-Wilson enriched ISP:
  multi-taste, selected-taste, taste-blind, or retained-record local-net branch.

Full interacting continuum QFT:
  not yet proved.
```

### Proof

The first line is Theorem 8.1. The second is Theorem 5.1. The Wilson line is
Theorem 6.1. The no-Wilson line is Theorem 7.1. The final line follows because
the present positive theorems are finite-battery, tested-sector, and
enriched-representation theorems; they do not establish nonperturbative
interacting vacuum/local-net convergence for arbitrary continuum QFT.
`square`

## 10. Relation To Standard QFT

This paper does not claim to replace standard QFT. It identifies a controlled
interface.

For the Wilson branch:

```text
ISP gives a finite/projective stochastic and operational representation whose
declared enrichment matches the tested single-species QFT local-net data.
```

For the no-Wilson branch:

```text
ISP keeps detail records and therefore naturally targets multi-taste or
retained-record local nets unless a recorded projection or taste-blind quotient
is declared.
```

For Gamma-only reconstruction:

```text
No.
```

The clean ontology is:

```text
Gamma is the stochastic endpoint layer.
Instruments are the operational layer.
CAR/local nets are enriched representation layers unless reconstructed from
operational data.
```

## 11. Export To Non-Abelian Papers

Paper 9 may now start finite non-Abelian gauge ISP. It may import:

1. enriched reconstruction discipline from Paper 1;
2. projective comparison-map control from Paper 3;
3. interacting curvature bookkeeping from Paper 4;
4. Wilson/no-Wilson branch distinction from Papers 5-6;
5. foliation independence for controlled finite batteries from Paper 7;
6. finite operational local-net reconstruction from this paper;
7. the finite covariance no-go of Corollary 2.4;
8. the continuum reconstruction audit of Definition 2.5.

Paper 9 may not claim:

```text
continuum Yang-Mills,
full non-Abelian QFT reconstruction,
Gamma-only gauge-field reconstruction,
or exact finite-regulator Lorentz covariance.
```

Its correct target is finite gauge-sector ISP with Gauss constraints, boundary
centers, local instruments, and first non-Abelian exchange coefficients.

## 12. What This Paper Proves

This paper proves:

1. a definition of enriched finite-battery local-net reconstruction;
2. a positive finite operational local-net reconstruction theorem;
3. a Wilson single-species Dirac/CAR local-net matching theorem on finite test
   classes;
4. a no-Wilson local-net classification theorem;
5. a Gamma-only no-go theorem for full relativistic QFT reconstruction;
6. a corollary separating representation existence from reconstruction;
7. a final V3 QFT status theorem;
8. an export contract for finite non-Abelian gauge ISP;
9. a finite-to-continuum audit separating finite-battery matching from
   continuum AQFT or Wightman-level reconstruction.

## 13. Finite-To-Continuum Audit Verdict

### Theorem 13.1: Paper 8 Exports Finite-Battery Reconstruction, Not Continuum QFT

Every positive theorem in this paper is one of the following:

```text
finite operational reconstruction on declared batteries;
enriched finite-battery QFT benchmark matching;
branch classification for declared Wilson/no-Wilson records.
```

No positive theorem in this paper proves any of the following without the
extra clauses of Definition 2.5:

```text
Haag-Kastler AQFT construction;
Wightman reconstruction;
continuum Lorentz covariance;
time-slice axiom;
spectrum condition;
quasilocal C^* or type-III local structure;
nonperturbative interacting continuum QFT;
continuum Yang-Mills existence or confinement.
```

Moreover, by Lemma 2.3 and Corollary 2.4, exact nontrivial Lorentz covariance
cannot be implemented as an invertible stochastic automorphism of one fixed
finite configuration set. Later papers may only cite Paper 8 covariance as
sampled finite-battery covariance matching, projective compatibility between
Lorentz-related batteries, or an explicitly imported continuum representation.

### Proof

Theorem 5.1 is operational and finite-battery by its hypotheses and conclusion.
Theorem 6.1 is enriched benchmark matching: it imports CAR, smearing,
polarization/vacuum, Wilson regulator, finite-energy sector, instruments, and
sampled covariance representation data. Theorem 7.1 is a branch
classification theorem over declared finite records. Theorem 8.1 is a
Gamma-only no-go theorem. None of these constructs the continuum completion
clauses listed in Definition 2.5. The covariance limitation is exactly
Corollary 2.4. Therefore every later use of Paper 8 must preserve this layer
typing. `square`

### Corollary 13.2: Consequence For The Non-Abelian Chain

Papers 9-20 may use Paper 8 to justify finite operational gauge-sector
records, declared instrument/effect nets, and projective matching discipline.
They may not use Paper 8 as a source for a continuum `4D SU(N)` Yang-Mills
measure, Lorentz-covariant AQFT, Wilson-loop area law, mass gap, or
confinement. Those must be proved or explicitly carried as later-paper source
gates.

## 14. Remaining Work After Paper 8

1. Build finite non-Abelian gauge-sector ISP in Paper 9.
2. Prove representation-cutoff/projective non-Abelian continuum control in
   Paper 10.
3. Strengthen finite-battery reconstruction to larger continuum domains.
4. Prove nonperturbative interacting vacuum and local-net convergence if the
   program aims beyond benchmark matching.
5. Decide whether ISP is ultimately a full QFT reconstruction program or a
   precise stochastic-operational representation layer beneath QFT.
6. Prove the Definition 2.5 continuum reconstruction audit clauses whenever a
   later theorem wants AQFT, Wightman, or full Lorentz-covariant continuum
   language.

## 15. Status

The honest conclusion is:

```text
Relativistic ISP has a controlled enriched interface to restricted QFT
finite-battery local-net data.
```

The honest non-conclusion is:

```text
Relativistic ISP has not reconstructed full interacting continuum QFT from
bare Gamma.
```

The next paper should be:

```text
V3 Paper 9: finite non-Abelian gauge ISP benchmark.
```
