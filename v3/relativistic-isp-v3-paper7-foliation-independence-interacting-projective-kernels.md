# Relativistic ISP V3 Paper 7: Foliation Independence For Interacting Projective Kernels

Author: Felix Robles Elvira

Status: theorem-level draft. This paper follows V3 Papers 3-6 and proves the
restricted foliation-independence theorem that those papers need. It is aligned
with the Barandes discipline: whole-process endpoint kernels and declared
comparison maps are primary; no proof below composes undeclared microscopic
subprocesses as if the process were Markov divisible.

The guiding question is Einsteinian in the strict operational sense:

```text
If two descriptions differ only by the order in which spacelike collars are
crossed, do they give the same finite endpoint statistics?
```

The answer proved here is conditional but positive:

```text
adjacent spacelike swap control
+ summable exchange-collar defects
-> foliation-independent finite-battery continuum statistics.
```

The theorem is not exact finite-lattice Lorentz invariance. It is asymptotic
finite-battery covariance for declared interacting projective ISP data.

## 1. Main Question

Can the interacting projective kernels of V3 Papers 3-6 satisfy a genuine
hypersurface-path equivalence theorem?

The target statement is:

```math
\lim_{a\to0}P_{a,\pi}(B)
=
\lim_{a\to0}P_{a,\pi'}(B)
```

for every finite recorded event `B`, whenever `\pi` and `\pi'` are two
regulated hypersurface paths with the same continuum endpoints and related by
spacelike collar swaps.

This paper proves that target under an explicit exchange-collar summability
hypothesis and proves that hypothesis in the controlled branches already
available from V3 Papers 3-6.

## 2. Barandes-Aligned Discipline

The paper obeys four rules.

1. A finite path protocol is a declared endpoint comparison protocol, not an
   unrecorded Markov time slicing.
2. Local collars are operationally declared deformation regions, detector
   regions, or source regions.
3. Raw comparison maps and exchange defects are algebraic relative-dynamics
   maps. They become measured probabilities only after a declared finite
   battery of effects is supplied.
4. Spacelike order independence is proved by adjacent swaps and exchange
   defects, not assumed from continuum QFT intuition.

Thus the basic object is not a hidden chain

```text
state at time 1 -> state at time 2 -> state at time 3.
```

The basic object is a whole-process endpoint kernel with a declared family of
relative deformations:

```math
J_C^a=\Gamma_C^a(\Gamma_0^a)^{-1}.
```

Here `C` is a spacetime collar, not an unobserved time step.

## 3. Imports

From V3 Paper 1 this paper imports the enrichment discipline:

```text
Gamma-level kernels, operational instruments, and Hilbert/CAR representation
data are distinct layers.
```

From V3 Paper 2 it imports the positive-cone/signed-algebra lesson: finite
positive kernels can generate signed algebraic comparison brackets, but signed
real-lapse comparison geometry is not itself a primitive negative-probability
operation.

From V3 Paper 3 it imports:

1. local comparison maps `J_C`;
2. inverses `J_C^{-1}` under LC-log/inverse-control hypotheses;
3. exchange defects for collar pairs;
4. anchored/corridor norms and cross-regulator transfer estimates;
5. the Wilson and detail-preserving staggered branches.

From V3 Paper 4 it imports interacting curvature coefficients and the
branchwise distinction between Wilson single-species and no-Wilson multi-taste
targets.

From V3 Paper 5 it imports Wilson-compatible instruments and tested
single-species QFT benchmark data.

From V3 Paper 6 it imports taste detectors, taste no-signaling, and Hypothesis
EC as the finite-battery statement to be proved here.

## 4. Regulated Hypersurface Protocols

Fix a regulator `a`. A finite hypersurface protocol is a tuple

```math
\pi_a=(C_1,\ldots,C_N;{\mathcal T}_a),
```

where:

1. each `C_i` is a declared compact collar in the regulated spacetime cell
   complex;
2. each collar carries either a local deformation, a source insertion, a
   detector insertion, or an identity operation;
3. `{\mathcal T}_a` is a finite operational battery of effects and recorded
   events.

The algebraic endpoint comparison map for a deformation-only protocol is

```math
J_{\pi_a}
=
J_{C_N}^a\cdots J_{C_1}^a.
```

If detector/source instruments are present, their Kraus or effect maps are
inserted as declared operational maps in the same finite product. This product
is an algebraic endpoint comparison protocol. It is not a claim that the system
physically passed through unrecorded intermediate states.

For a recorded event `B`, write its finite probability as

```math
P_{a,\pi}(B)
=
\ell_{a,B}(J_{\pi_a}\rho_a),
```

where `\rho_a` is the declared initial endpoint state and `\ell_{a,B}` is the
declared effect functional for event `B`. More generally, with instruments, the
same notation absorbs the finite Kraus/effect composition into `J_{\pi_a}` and
`\ell_{a,B}`.

### Definition 4.1: Finite Battery Norm

A finite battery `{\mathcal T}` is **uniformly bounded** if there is a constant
`M_{\mathcal T}` such that, for all small `a`,

```math
\|\rho_a\|\le M_{\mathcal T},
\qquad
\|\ell_{a,B}\|\le M_{\mathcal T},
```

and every declared source, detector, and comparison factor in the battery has
operator norm at most `M_{\mathcal T}` in the relevant anchored/corridor module
norm.

All Paper-5 Wilson batteries and Paper-6 taste batteries are finite batteries
in this sense after their declared cutoffs and energy/particle windows are
fixed.

## 5. Spacelike Collar Swaps

Two collars `C,D` are **spacelike separated at regulator `a` with continuum
margin `\ell>0`** if their continuum supports have spacelike separation at
least `\ell` and the regulated collars lie inside fixed compact thickenings of
those supports.

Two paths are related by one adjacent spacelike swap if

```math
\pi_a=A_a\,C\,D\,B_a,
\qquad
\pi'_a=A_a\,D\,C\,B_a,
```

where `A_a` and `B_a` denote the unchanged parts of the finite protocol and
`C,D` are spacelike separated collars.

The exchange defect convention used in this paper is

```math
E_{C,D}^a
:=
(J_D^a)^{-1}(J_C^a)^{-1}J_D^aJ_C^a.
```

Some earlier notes use the inverse commutator convention. Nothing depends on
that choice: replacing `E_{C,D}` by its inverse only changes constants in the
small-defect norm when the unitized inverse bounds hold.

With this convention,

```math
J_D^aJ_C^a=J_C^aJ_D^aE_{C,D}^a.
```

Thus `E_{C,D}^a-I` is exactly the algebraic obstruction to exchanging the
spacelike collar order.

### Lemma 5.1: Causal Linear-Extension Lemma

Fix a finite set of collar supports inside a compact continuum window. Define a
partial order by

```math
C\prec D
```

when every point of `C` lies in the causal past of every point of `D`, after the
declared regulator thickening. A regulated hypersurface protocol compatible
with the causal order is a linear extension of this finite partial order.

If two protocols have the same collars and both respect the causal order, then
one can transform one ordering into the other by a finite sequence of adjacent
swaps of incomparable collar pairs. In the continuum interpretation, these
incomparable pairs are spacelike or regulator-spacelike.

### Proof

This is the standard linear-extension theorem for finite posets. If two linear
extensions differ, find the first position where they differ. Move the element
that should appear there leftward through adjacent elements. Every element it
passes is incomparable with it; otherwise moving it would violate one of the
two linear extensions. Repeating this process transforms one extension into the
other by adjacent swaps of incomparable elements. `square`

## 6. Adjacent-Swap Theorem

### Theorem 6.1: Adjacent Spacelike Swap Bound

Let `\pi_a=A_a C D B_a` and `\pi'_a=A_a D C B_a` differ by one adjacent
spacelike swap. Assume:

1. the finite battery is uniformly bounded;
2. `J_C^a,J_D^a` are invertible in the declared anchored/corridor algebra;
3. `E_{C,D}^a-I` is controlled in the same corridor norm.

Then, for every recorded event `B`,

```math
|P_{a,\pi}(B)-P_{a,\pi'}(B)|
\le
K_{\mathcal T}
\|E_{C,D}^a-I\|_{C:D},
```

where `K_{\mathcal T}` depends on the finite battery bounds and collar
scaffolds, but not on total volume.

### Proof

Using the exchange-defect identity,

```math
J_D^aJ_C^a-J_C^aJ_D^a
=
J_C^aJ_D^a(E_{C,D}^a-I).
```

Therefore

```math
J_{A}^aJ_D^aJ_C^aJ_B^a
-
J_A^aJ_C^aJ_D^aJ_B^a
=
J_A^aJ_C^aJ_D^a(E_{C,D}^a-I)J_B^a.
```

Apply the effect functional `\ell_{a,B}` to this difference acting on
`\rho_a`. The module inequalities and finite-battery bounds give

```math
|P_{a,\pi}(B)-P_{a,\pi'}(B)|
\le
\|\ell_{a,B}\|
\|J_A^a\|
\|J_C^a\|
\|J_D^a\|
\|E_{C,D}^a-I\|_{C:D}
\|J_B^a\rho_a\|.
```

Absorb all bounded factors into `K_{\mathcal T}`. `square`

### Corollary 6.2: Detector Adjacent Swaps

If `C` and `D` are detector collars whose Kraus/effect operators are even local
functions of disjoint block fields, then

```math
E_{C,D}^a=I
```

for the detector part. Any nonzero adjacent-swap error must therefore come from
the intervening dynamical comparison maps, not from the detector readout itself.

### Proof

Even local detector operators on spacelike/disjoint block supports commute, as
proved for taste instruments in Paper 6 and for Wilson-compatible local
instruments in Paper 5. The exchange product is therefore exactly the identity
on the detector algebra. `square`

## 7. Path-Summability Theorem

### Definition 7.1: Exchange-Summable Path Pair

Two regulated protocols `\pi_a,\pi'_a` with the same endpoint supports are
**exchange-summable** if, for all sufficiently small `a`, one can transform
`\pi_a` into `\pi'_a` by a finite sequence of adjacent spacelike swaps

```math
(C_1,D_1),\ldots,(C_{N_a},D_{N_a})
```

such that

```math
\Sigma_a(\pi,\pi')
:=
\sum_{k=1}^{N_a}\|E_{C_k,D_k}^a-I\|_{C_k:D_k}
\to0.
```

This is Paper 6's Hypothesis EC in path language.

### Theorem 7.2: Foliation Independence From Exchange Summability

If `\pi_a,\pi'_a` are exchange-summable and the finite battery is uniformly
bounded, then for every recorded event `B`,

```math
|P_{a,\pi}(B)-P_{a,\pi'}(B)|
\le
K_{\mathcal T}\Sigma_a(\pi,\pi')+o_a(1).
```

Consequently,

```math
\lim_{a\to0}P_{a,\pi}(B)
=
\lim_{a\to0}P_{a,\pi'}(B)
```

whenever either limit exists.

### Proof

Let

```math
\pi_a=\pi_a^{(0)},\pi_a^{(1)},\ldots,\pi_a^{(N_a)}=\pi'_a
```

be the adjacent-swap chain. By Theorem 6.1,

```math
|P_{a,\pi^{(k)}}(B)-P_{a,\pi^{(k+1)}}(B)|
\le
K_{\mathcal T}\|E_{C_k,D_k}^a-I\|_{C_k:D_k}
+o_{a,k}(1).
```

The battery is fixed and finite, and the path deformation is controlled inside
a fixed compact continuum window, so the accumulated remainder is `o_a(1)` by
the same uniformity assumptions that define exchange summability. Summing the
telescoping inequalities gives the result. `square`

## 8. Proving Exchange Summability In Controlled Branches

The abstract theorem is useful only if `\Sigma_a\to0` can be proved in actual
branches. The following results are the paper's positive content.

### Hypothesis CEC: Controlled Exchange-Collar Data

A branch satisfies **CEC** on a finite path class if:

1. the collars are smooth or otherwise admitted by the Paper-3 inverse-control
   topology;
2. for each spacelike pair `C,D`,
   ```math
   \|E_{C,D}^a-I\|_{C:D}
   \le
   A_a(C,D)e^{-\nu d_a(C,D)}+r_a(C,D);
   ```
3. `d_a(C,D)` is the graph/collar distance between spacelike supports;
4. for every allowed finite path deformation,
   ```math
   \sum_k A_a(C_k,D_k)e^{-\nu d_a(C_k,D_k)}
   +
   \sum_k r_a(C_k,D_k)
   \to0.
   ```

### Theorem 8.1: CEC Implies Hypothesis EC

Every branch satisfying CEC is exchange-summable. Therefore all finite
batteries in that branch have foliation-independent continuum statistics.

### Proof

The CEC bound is exactly a summable majorant for the terms defining
`\Sigma_a(\pi,\pi')`. Theorem 7.2 applies. `square`

### Theorem 8.2: Smooth-Collar Low-Sector Branch Satisfies CEC

Consider the fixed-ratio low-momentum accepted branch of V3 Paper 3 with smooth
collars, accepted low-sector readout, and error scale

```math
\zeta_{\rm low}^{ab}(\lambda)
=
a^2\Lambda(a)^3+\tau_N(a)+a|g_a|+|\Delta(a)/a-\lambda|.
```

Assume:

```math
\zeta_{\rm low}^{ab}(\lambda)\to0,
```

and the LC-log corridor constants are uniform on the finite path class. Then
CEC holds for every finite smooth-collar path deformation with a positive
continuum spacelike margin.

### Proof

V3 Paper 3 gives projective transfer for `E_{C,D}` in the smooth accepted
low-sector topology and an outside-window/corridor tail with constants
independent of total volume. For a fixed finite path class, spacelike-separated
continuum supports with positive margin have graph distance

```math
d_a(C,D)\ge c/a
```

for some `c>0`. Hence the exponential corridor tails are summable and vanish.
The accepted-branch refinement errors are bounded by
`\zeta_{\rm low}^{ab}(\lambda)`, so the finite sum of residual terms also
vanishes. Thus CEC holds. `square`

### Theorem 8.3: Wilson Finite-Energy Branch Satisfies CEC

Consider the Wilson single-species finite-energy branch of V3 Papers 3 and 5,
with:

1. Wilson smearing, polarization, and propagator convergence;
2. Wilson-admissible interactions satisfying the tested Feshbach bound;
3. finite particle number and finite energy windows;
4. smooth compact collar profiles;
5. uniformly bounded Wilson-compatible instruments.

Then CEC holds on every fixed finite path class with positive spacelike collar
margin.

### Proof

The Wilson branch has two possible sources of path-order error: physical-sector
exchange and detail-sector leakage. Physical-sector exchange is controlled by
the Paper-3 corridor estimate for smooth collars, hence has exponentially small
spacelike tail plus the branch's refinement residual. Detail-sector leakage is
controlled by the Wilson gap/Feshbach estimate imported in Paper 5: on fixed
finite-energy tests, detail excitations leave the tested sector and
physical/detail mixing is `O(a\|V_a\|_{\rm tested})`, which vanishes under the
Wilson-admissibility condition. A finite path class turns these pairwise bounds
into a summable CEC bound. `square`

### Theorem 8.4: No-Wilson Taste Branch Satisfies CEC Under The Same Dynamical Bound

Consider the no-Wilson detail-preserving/taste branch of V3 Paper 6. Suppose
the dynamical collar deformations satisfy the same smooth-collar exchange bound
as in CEC, and the taste detector/source instruments are the block-local
finite-battery instruments of Paper 6. Then CEC holds for every fixed finite
taste battery with positive spacelike collar margin.

### Proof

The taste detector/source part contributes no spacelike ordering error by Paper
6's detector no-signaling theorem. The remaining ordering error is dynamical and
is exactly the exchange-collar defect for the relevant local deformations. By
assumption that defect satisfies CEC. Therefore Theorem 8.1 applies. `square`

## 9. Restricted Interacting Foliation-Independence Theorem

### Theorem 9.1: Restricted Interacting Foliation Independence

Let `{\mathcal B}` be one of the following declared branches:

1. smooth-collar low-sector accepted branch;
2. Wilson finite-energy single-species branch;
3. no-Wilson taste branch with CEC dynamical collars;
4. bounded finite-range/common-collar Benchmark A from V3 Paper 3.

For every fixed finite continuum test window, every uniformly bounded finite
instrument battery, and every pair of regulated hypersurface protocols
`\pi_a,\pi'_a` with the same endpoints and connected by exchange-summable
spacelike swaps, the endpoint statistics satisfy

```math
\lim_{a\to0}P_{a,\pi}^{\mathcal B}(B)
=
\lim_{a\to0}P_{a,\pi'}^{\mathcal B}(B)
```

for every recorded event `B`.

### Proof

The smooth low-sector branch satisfies exchange summability by Theorem 8.2. The
Wilson finite-energy branch satisfies it by Theorem 8.3. The no-Wilson taste
branch satisfies it under the stated dynamical CEC hypothesis by Theorem 8.4.
Benchmark A has exact projective compatibility and uniform finite-range
common-collar LC-log control from V3 Paper 3, so the same adjacent-swap theorem
applies with zero or uniformly summable residuals. The path theorem, Theorem
7.2, then gives equality of continuum endpoint probabilities. `square`

### Interpretation

This is the first genuine interacting foliation theorem in the V3 sequence. It
is not full constructive interacting QFT. It says:

```text
within the declared controlled branches,
finite endpoint statistics are independent of arbitrary spacelike collar order.
```

That is the minimum relativistic content needed before Paper 8 can discuss QFT
reconstruction rather than fixed-foliation dynamics.

## 10. Relation To Lorentz Covariance

Foliation independence is not identical to Lorentz covariance, but it is the
operational core required here. Lorentz transformations change:

1. the sampled hypersurface family;
2. the ordering of spacelike-separated collars;
3. the smearing functions and detector supports;
4. the representation frame for spin/taste/gauge data.

The finite lattice does not have exact continuous Lorentz symmetry. The only
honest theorem is an asymptotic finite-battery theorem.

### Definition 10.1: Sampled Lorentz-Related Batteries

Two battery families `{\mathcal T}_a` and `{\mathcal T}'_a` are sampled
Lorentz-related if:

1. their continuum source, detector, and deformation supports are related by a
   fixed proper orthochronous Lorentz transformation `\Lambda`;
2. their smearing functions are transformed by the appropriate scalar,
   spinor, taste, or gauge representation data declared in V3 Paper 1;
3. their regulated paths approximate the two continuum descriptions with mesh
   error tending to zero;
4. their spacelike-order differences are exchange-summable.

### Theorem 10.2: Asymptotic Finite-Battery Lorentz Covariance

Assume a branch satisfying Theorem 9.1 and assume the branch's declared free or
interacting representation data transform the target continuum battery
covariantly on the finite test class. Then sampled Lorentz-related batteries
have equal continuum probabilities:

```math
\lim_{a\to0}P_{a,{\mathcal T}}(B)
=
\lim_{a\to0}P_{a,{\mathcal T}'}(\Lambda B).
```

### Proof

Split the comparison into two steps. First, use Theorem 9.1 to change the
regulated path order from one sampled foliation to the other; this changes no
continuum endpoint probability. Second, use the declared continuum
representation covariance on the finite test battery to identify the transformed
source/effect data. The result follows. `square`

### Exact Finite-Regulator Boundary

This theorem does not assert

```text
exact Poincare covariance at finite lattice spacing.
```

It asserts

```text
equal continuum finite-battery probabilities for sampled Lorentz-related
protocols after regulator refinement.
```

This distinction is essential. Claiming exact finite-lattice Lorentz symmetry
would be false for the Wilson and staggered regulators used here.

## 11. Wilson Versus No-Wilson Under Foliation

The foliation theorem does not collapse the Wilson and no-Wilson branches into
one ontology.

### Wilson Branch

The Wilson branch has:

```text
detail sector gapped
+ finite-energy tests
+ Wilson-compatible instruments
-> single-species finite-battery QFT statistics.
```

Foliation independence says those finite-battery statistics are independent of
spacelike collar order in the continuum limit.

### No-Wilson Branch

The no-Wilson branch has:

```text
detail sector retained
+ taste instruments if declared
-> multi-taste or retained-record finite-battery statistics.
```

Foliation independence says taste detector order does not cause superluminal
influence and the remaining dynamical order dependence is controlled by CEC.
It does not erase the taste sector. A taste-channel discriminator remains a
taste-channel discriminator after changing foliations.

### Theorem 11.1: Branch Distinction Is Foliation-Stable

If a Wilson battery and a no-Wilson taste battery differ by a nonzero
taste-channel statistic in the sense of V3 Paper 6, then applying a
foliation-equivalent path deformation to both batteries does not remove that
difference in the continuum limit.

### Proof

By Theorem 9.1, each branch's endpoint probabilities are unchanged under
exchange-summable path deformation. Therefore the difference between their
continuum probabilities is unchanged. `square`

## 12. Einstein Principle In ISP Form

Einstein's lesson is not that formulas should look Lorentzian at every cutoff.
It is that the arbitrary human slicing used to describe a process should not
change the empirical content.

In ISP language:

```text
Only the endpoint process, recorded instruments, and causal support relations
are physical. A spacelike foliation order is descriptive scaffolding.
```

The mathematical content is the adjacent-swap theorem. If two collars are
spacelike, then changing their order can affect the endpoint statistics only by
the exchange defect. If those defects vanish or are summable in the continuum
limit, the foliation was not physical.

This is the correct first-principles route. It does not start by assuming a
continuum stress-energy tensor or a preexisting quantum field net. It starts
from finite endpoint kernels and asks what must be true for arbitrary
hypersurface bookkeeping to wash out of finite recorded probabilities.

## 13. Obstruction Theorem

The positive theorem has a sharp converse.

### Theorem 13.1: Non-Summable Exchange Defects Obstruct Foliation Independence

Suppose there exists a finite battery event `B` and a sequence of path pairs
`\pi_a,\pi'_a` with the same continuum endpoints such that:

1. the paths differ by spacelike collar swaps;
2. for some swap subsequence, the exchange-defect contribution has a nonzero
   continuum effect under the battery functional;
3. the total contribution does not vanish:
   ```math
   \limsup_{a\to0}
   |P_{a,\pi}(B)-P_{a,\pi'}(B)|>0.
   ```

Then the branch does not define foliation-independent relativistic ISP on that
test class.

### Proof

Foliation independence is exactly equality of the continuum endpoint
probabilities for path-equivalent protocols. A nonzero limiting difference is
the negation of that equality. By the adjacent-swap identity, such a difference
can only come from exchange defects or from noncommuting declared instruments.
The latter is excluded for the Wilson and taste instruments by their local
commutation theorems, so the obstruction is dynamical exchange-collar
non-summability. `square`

### Consequence

If this obstruction appears in a future interacting branch, the branch may
still be a valid fixed-foliation finite stochastic theory, but it is not yet a
relativistic QFT reconstruction.

## 14. What This Paper Proves

This paper proves:

1. a formal regulated hypersurface protocol framework for endpoint ISP kernels;
2. a finite causal linear-extension lemma reducing foliation changes to
   adjacent spacelike swaps;
3. an adjacent spacelike swap theorem controlled by the exchange defect;
4. detector adjacent swaps are exact when detector supports are spacelike and
   locally commuting;
5. exchange summability implies finite-battery foliation independence;
6. the smooth-collar low-sector branch satisfies exchange summability;
7. the Wilson finite-energy branch satisfies exchange summability under its
   Wilson-admissible interaction conditions;
8. the no-Wilson taste branch satisfies exchange summability whenever its
   dynamical collars satisfy the same CEC bound, and its detector part is
   already causal;
9. sampled Lorentz-related finite batteries have equal continuum probabilities
   when the branch's declared representation data transform covariantly;
10. Wilson/no-Wilson branch distinctions are stable under foliation changes;
11. non-summable exchange defects are a precise obstruction to relativistic ISP.

## 15. Remaining Work After Paper 7

Paper 7 completes the first foliation-independence gate, but it does not finish
the QFT program.

Remaining tasks:

1. Paper 8 must decide whether the enriched ISP package reconstructs a
   continuum local QFT class or only represents it.
2. Papers 9-10 must build finite and projective non-Abelian gauge benchmarks.
3. A stronger interacting theorem must eventually remove some finite-battery,
   smooth-collar, and finite-energy restrictions.
4. Nonperturbative interacting vacuum/local-net convergence remains beyond this
   paper.
5. Exact finite-regulator Lorentz symmetry is not claimed and should not be
   claimed for the lattice branches used here.

## 16. Status

The Paper-7 pass condition is met in the restricted but meaningful sense:

```text
declared endpoint comparison protocols
+ adjacent spacelike swap theorem
+ exchange-collar summability
-> foliation-independent finite-battery continuum statistics.
```

The strongest honest conclusion is:

> Controlled interacting branches of relativistic ISP have foliation-independent
> finite-battery endpoint statistics whenever their spacelike exchange-collar
> defects are summable. This includes the smooth-collar low-sector branch, the
> Wilson finite-energy branch under Wilson-admissible conditions, and the
> no-Wilson taste branch once its dynamical collars satisfy the same bound.

The strongest honest non-conclusion is:

> This is not yet full interacting continuum QFT. It is the foliation gate that
> a QFT reconstruction paper may now import.

The export to Paper 8 is:

```text
finite-battery predictions no longer depend on arbitrary spacelike foliation
order in the controlled branches.
```
