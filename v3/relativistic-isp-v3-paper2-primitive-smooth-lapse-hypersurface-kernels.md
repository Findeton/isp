# Primitive Smooth-Lapse Hypersurface Kernels In Relativistic ISP

Preprint, not peer reviewed, version 2026-05-28.

Author: Felix Robles Elvira

V3 Paper 2 investigation draft

Date: 2026-05-17

Status: Positive-cone-to-signed-algebra pass. This paper tests whether the V2
log-smeared smooth-lapse comparison maps can be replaced by primitive finite
stochastic kernels. The current verdict is mixed but useful: a positive-cone
primitive kernel exists by a declared whole-process convex-mixture protocol and
has the correct leading stochastic-curvature limit under the V2 thin-slab
scaling; the resulting positive-cone curvature determines a unique signed
bilinear hypersurface-deformation algebra by cone completion; while naive
weighted-Hamiltonian Born-squared smoothing is not a clean real-lapse theorem
because its leading coefficient is nonlinear/signless in the lapse amplitude.

## 1. Purpose

V2 Paper 1 proved the free `1+1D` stochastic-curvature theorem in two stages.

1. At coefficient level,
   ```math
   \mathfrak C_a[N,M]=[\mathcal K_a[N],\mathcal K_a[M]],
   \qquad
   \mathcal K_a[N]=a\sum_nN(an)A_n^{(1)}
   ```
   converges on sampled smooth spinors to
   ```math
   K_\parallel[N\partial_xM-M\partial_xN].
   ```
2. At finite-slab level, V2 used the log-smeared algebraic comparison map
   ```math
   \mathbb J_{a,\Delta}[N]
   =
   \exp\left(a\sum_nN(an)\log J_n(a,\Delta)\right).
   ```

The log-smeared construction is controlled and Barandes-compatible as an
algebraic comparison-map construction, but it is not itself a primitive
positive stochastic kernel for a smooth lapse. V3 Paper 2 asks:

> Can smooth-lapse deformations be represented by primitive finite stochastic
> endpoint kernels, rather than by exponentials of comparison-map logarithms?

The target is not to replace V2 Paper 1. The target is to identify exactly
which part of smooth-lapse hypersurface deformation is primitive stochastic,
which part is algebraic comparison geometry, and which part would require
enriched representation data.

## 2. V3 Paper 1 Import Contract

This paper uses the V3 Paper 1 import contract.

```text
Gamma-level imports:
- finite configuration spaces X_a;
- projective maps P_ab when refinement is discussed;
- whole-process endpoint stochastic kernels Gamma_a[O];
- comparison maps J=Gamma[O] Gamma[O_0]^{-1};
- exchange defects E=J_N J_M J_N^{-1} J_M^{-1}.

Operational imports:
- only when a random clock/mixture protocol is interpreted as a declared
  randomized operation or record family.

Representation-enriched imports:
- none in the baseline positive-cone theorem.
- weighted-Hamiltonian Born-squared candidates may use a Hilbert lift as a
  diagnostic, but then the result is explicitly enriched, not Gamma-level.

Forbidden:
- composing unrecorded component kernels as if the process were Markov
  divisible;
- treating algebraic comparison maps as primitive stochastic kernels;
- using a Hilbert Hamiltonian principal symbol while advertising a Gamma-level
  theorem.
```

Thus the baseline construction must be a declared whole-process stochastic
operation at finite `a,\Delta`, not a hidden Markov chain through unrecorded
local subprocesses.

## 3. Data Imported From V2 Paper 1

Work in the free one-particle `1+1D` lattice Dirac benchmark. The reference
slab is

```math
\Gamma_0(\Delta)=\Gamma(e^{-i\Delta H_D}).
```

For a singleton collar deformation,

```math
J_n(a,\Delta)
=
\Gamma_n(a,\Delta)\Gamma_0(\Delta)^{-1},
```

and V2 Paper 1 supplies

```math
J_n(a,\Delta)=I+\Delta^2A_n^{(1)}+O(\Delta^4),
```

with one-step support and zero column sums. It also supplies the coefficient
theorem

```math
[\mathcal K_a[N],\mathcal K_a[M]]\iota_a\phi
\longrightarrow
\iota_aK_\parallel[N\partial_xM-M\partial_xN]\phi,
```

where

```math
\mathcal K_a[N]=a\sum_nN(an)A_n^{(1)}.
```

The finite-slab log-smeared theorem used the very-thin-slab condition

```math
\Delta(a)/a^2\to0.
```

V3 Paper 2 may improve this scaling only if it proves sharper uniform
remainders. The first pass keeps the V2 scaling as the safe baseline.

## 4. Candidate Primitive Smooth-Lapse Kernels

There are three natural candidates.

### Candidate A: weighted-Hamiltonian Born-squared slab

Choose a local deformation amplitude function `\theta(N_n)` and define a
whole-slab Hilbert operator

```math
U_\theta[N;\Delta]
=
\exp\left(-i\Delta\left(H_D-\sum_n\theta(N_n)C_n\right)\right),
```

then set

```math
\Gamma_\theta[N;\Delta]_{xy}
=
|U_\theta[N;\Delta]_{xy}|^2.
```

This is primitive and column-stochastic because it is Born-squared from a
unitary. But it is not automatically a Gamma-level construction: the Hilbert
Hamiltonian and the chosen local amplitude function are representation data
unless supplied as part of the finite operation definition.

The deeper problem is coefficient linearity. V2 Paper 1 proved the exact
singleton scaling

```math
A_{n,\lambda}^{(1)}
=
c_\lambda A_n^{(1)},
\qquad
c_\lambda=\lambda(2-\lambda).
```

Thus a naive local amplitude `\theta=N` gives the leading response

```math
c_N=N(2-N),
```

not `N`. The exchange bracket would then see

```math
c_N\partial_xc_M-c_M\partial_xc_N,
```

not

```math
N\partial_xM-M\partial_xN.
```

One can formally correct this on `0\le N\le1` by choosing

```math
\theta(N)=1-\sqrt{1-N},
\qquad
\theta(N)(2-\theta(N))=N.
```

But this is a positive-bounded lapse construction. It does not give arbitrary
signed real lapse profiles as primitive positive kernels.

### Candidate B: declared convex-mixture whole-process kernel

Let `N\ge0` be a smooth compactly supported lapse profile. For a fixed bounded
positive-lapse class, choose `\eta>0` so that

```math
\eta a\sum_nN(an)\le1
```

for all sufficiently small `a`. Define the primitive endpoint kernel

```math
\Gamma_a^{\rm mix}[N;\Delta]
:=
\left(1-\eta a\sum_nN_n\right)\Gamma_0(\Delta)
+\eta a\sum_nN_n\Gamma_n(\Delta),
```

where `N_n=N(an)`.

This is an exact column-stochastic kernel, because it is a convex combination
of exact endpoint kernels. Its comparison map is

```math
J_a^{\rm mix}[N;\Delta]
=
\Gamma_a^{\rm mix}[N;\Delta]\Gamma_0(\Delta)^{-1}
=
I+\eta a\sum_nN_n\bigl(J_n(a,\Delta)-I\bigr).
```

This construction is primitive stochastic for `N\ge0`; it is also
Barandes-compatible if interpreted as one declared randomized whole-process
operation. If the random choice is recorded, it belongs to the instrument
layer. If the record is ignored, the displayed convex mixture is the endpoint
kernel of the declared randomized operation.

### Candidate C: Trotterized local stochastic operation family

One may try to define

```math
\Gamma^{\rm trot}[N;\Delta]
=
\prod_n \Gamma_n(\epsilon_n\Delta)
```

or a randomized local-order variant. This is column-stochastic as a product of
column-stochastic matrices, but it is not automatically a primitive
indivisible process. It represents declared division events or a classical
protocol through recorded/unrecorded intermediate operations.

If the theorem wants a genuinely indivisible smooth-lapse kernel, Candidate C
is not the right primitive. If the theorem declares the division events, it may
be an operational protocol, but then it must obey the V3 Paper 1 admissibility
criterion.

## 5. Positivity And Column-Stochasticity Audit

### Proposition 5.1: convex-mixture primitive positivity

For `N\ge0` and `\eta a\sum_nN_n\le1`,

```math
\Gamma_a^{\rm mix}[N;\Delta]
```

is a column-stochastic finite endpoint kernel.

Proof. Each `\Gamma_0` and `\Gamma_n` is column-stochastic. The coefficients

```math
1-\eta a\sum_nN_n,
\qquad
\eta aN_n
```

are nonnegative and sum to one. A convex combination of column-stochastic
matrices is column-stochastic. `square`

### Proposition 5.2: signed lapse obstruction for primitive positivity

The convex-mixture construction cannot represent an arbitrary signed lapse
profile as a single primitive positive kernel while preserving linearity in
`N`.

Proof. If `N_n<0`, the coefficient `\eta aN_n` in the convex combination is
negative. Replacing it by `|N_n|` destroys the sign and changes the target
bracket. Splitting `N=N_+-N_-` gives two positive kernels, but their difference
is an algebraic comparison object, not a single primitive stochastic endpoint
kernel. `square`

Thus primitive smooth-lapse kernels are naturally positive-cone objects.
Signed real-lapse algebra belongs either to comparison-map linearization or to
an explicitly enriched representation.

## 6. Leading Curvature Of The Convex-Mixture Kernel

Define

```math
J_N:=J_a^{\rm mix}[N;\Delta],
\qquad
J_M:=J_a^{\rm mix}[M;\Delta],
```

and

```math
E_a^{\rm mix}[N,M;\Delta]
:=
J_NJ_MJ_N^{-1}J_M^{-1}.
```

Using the singleton expansion,

```math
J_N
=
I+\eta a\sum_nN_n(\Delta^2A_n^{(1)}+O(\Delta^4)).
```

Therefore

```math
J_N
=
I+\eta\Delta^2\mathcal K_a[N]
+B_a^{\rm mix}[N;\Delta],
```

with the same leading `\mathcal K_a[N]` as V2 Paper 1.

### Theorem 6.1: positive-cone primitive smooth-lapse curvature

Assume `N,M\ge0` are smooth compactly supported lapse profiles in a bounded
positive-lapse class, choose `\eta` so the convex-mixture kernels are defined,
and take the V2 thin-slab scaling

```math
\Delta(a)/a^2\to0.
```

Assume the singleton remainders are uniformly bounded in the V2 Paper 1
finite-slab topology. Then

```math
{1\over \eta^2\Delta(a)^4}
\left(E_a^{\rm mix}[N,M;\Delta(a)]-I\right)\iota_a\phi
\longrightarrow
\iota_aK_\parallel[N\partial_xM-M\partial_xN]\phi.
```

Proof. The comparison maps have the form

```math
J_N=I+\eta\Delta^2\mathcal K_a[N]+B_N,
\qquad
J_M=I+\eta\Delta^2\mathcal K_a[M]+B_M,
```

where the V2 thin-slab scaling makes the remainders negligible after division
by `\eta^2\Delta^4` on sampled smooth profiles. The Banach-algebra
group-commutator expansion gives

```math
J_NJ_MJ_N^{-1}J_M^{-1}
=
I+\eta^2\Delta^4[\mathcal K_a[N],\mathcal K_a[M]]
+o(\eta^2\Delta^4)
```

on the tested domain. Dividing by `\eta^2\Delta^4` and applying the V2
coefficient-level theorem gives the result. `square`

This is the first positive primitive smooth-lapse theorem. It is positive-cone,
declared-protocol, and leading-curvature level. It is not yet a theorem for all
signed lapses or all regulator families.

## 7. Positive-Cone-To-Signed-Algebra Theorem

The primitive stochastic construction above is naturally defined only on the
positive lapse cone. Relativistic hypersurface-deformation algebra, however, is
written for real signed lapse functions. The bridge is not a negative
probability operation. It is the bilinear tangent algebra generated by the
positive cone.

Let

```math
V=C_c^\infty(\mathbb R,\mathbb R),
\qquad
V_+=\{N\in V:N(x)\ge0\ \forall x\}.
```

### 7.1 Cone and topology conventions

The theorem is a continuum coefficient theorem on the sampled test domain
`\mathcal D=C_c^\infty(\mathbb R,\mathbb C^2)`, with convergence in the strong
sampled sense:

```math
T_a\Rightarrow T
\quad\hbox{means}\quad
\|T_a\iota_a\phi-\iota_aT\phi\|_{\ell^2}\to0
\quad
\hbox{for every }\phi\in\mathcal D.
```

The auxiliary intensity `\eta` in the convex-mixture kernel is not physical
metric data. For any finite list of nonnegative lapse profiles
`N_1,\ldots,N_k`, choose a common `\eta>0` such that

```math
\eta a\sum_nN_j(an)\le1
```

for all `j` and all sufficiently small `a`. After normalizing by `\eta^2`,
the continuum curvature response in Theorem 6.1 is independent of this common
choice of `\eta`.

The cone `V_+` generates `V`: every `N\in V` can be written as

```math
N=N_+-N_-,
\qquad
N_\pm\in V_+.
```

Indeed, choose a compactly supported smooth bump `B_N\ge |N|` on a compact set
containing `\operatorname{supp}N`; then

```math
N_+={1\over2}(B_N+N),
\qquad
N_-={1\over2}(B_N-N).
```

### Lemma 7.1: positive-cone values determine a bilinear extension

Let `W` be a real vector space and let

```math
b^+:V_+\times V_+\to W
```

be the restriction to `V_+` of some bilinear map `b:V\times V\to W`. Then `b`
is uniquely determined by `b^+`.

Equivalently, if `N=N_+-N_-` and `M=M_+-M_-` with all four pieces in `V_+`,
then every bilinear extension must satisfy

```math
b(N,M)
=
b^+(N_+,M_+)-b^+(N_+,M_-)
-b^+(N_-,M_+)+b^+(N_-,M_-).
```

If the right-hand side is independent of decomposition, it defines the unique
bilinear extension.

Proof. Since `V_+` generates `V`, every vector is a difference of positive
vectors. Bilinearity forces the displayed formula. Thus two bilinear maps that
agree on `V_+\times V_+` agree on all of `V\times V`. If the formula is
decomposition-independent, it is well defined and bilinear. `square`

### Theorem 7.2: positive primitive lapses determine the signed bracket

Assume Theorem 6.1 holds for all bounded nonnegative compactly supported smooth
lapses in the tested class, with a common auxiliary intensity `\eta` chosen for
each finite set of profiles being compared. Define the positive-cone curvature
response

```math
\mathcal B^+(N,M)
:=
\lim_{a\to0}
{1\over \eta^2\Delta(a)^4}
\left(E_a^{\rm mix}[N,M;\Delta(a)]-I\right)
```

on sampled smooth profiles, for `N,M\in V_+`. Then

```math
\mathcal B^+(N,M)
=
K_\parallel[N\partial_xM-M\partial_xN].
```

There is a unique alternating bilinear map

```math
\mathcal B:V\times V\to{\rm End}(\mathcal D)
```

extending `\mathcal B^+`, given by

```math
\mathcal B(N,M)
=
\mathcal B^+(N_+,M_+)
-\mathcal B^+(N_+,M_-)
-\mathcal B^+(N_-,M_+)
+\mathcal B^+(N_-,M_-),
```

for any decompositions

```math
N=N_+-N_-,
\qquad
M=M_+-M_-,
\qquad
N_\pm,M_\pm\in V_+.
```

The result is independent of the chosen positive decompositions and equals

```math
\mathcal B(N,M)
=
K_\parallel[N\partial_xM-M\partial_xN].
```

Thus primitive positive-lapse stochastic kernels determine the full signed
smooth-lapse hypersurface-deformation bracket at the algebraic comparison/tangent
level.

### Proof

Existence of positive decompositions follows from the bump construction in
Section 7.1. For a fixed pair of decompositions, choose one common `\eta` small
enough for the four positive pairs appearing in the formula. The normalized
limits are independent of this auxiliary choice by Theorem 6.1.

For `N_\pm,M_\pm\in V_+`, Theorem 6.1 gives

```math
\mathcal B^+(N_\sigma,M_\tau)
=
K_\parallel[N_\sigma\partial_xM_\tau-M_\tau\partial_xN_\sigma],
```

where `\sigma,\tau\in\{+,-\}`. Substitute this into the defining expression for
`\mathcal B(N,M)`. By linearity of `K_\parallel` in its vector-field argument
and bilinearity of

```math
(N,M)\mapsto N\partial_xM-M\partial_xN,
```

the four terms combine to

```math
K_\parallel[
(N_+-N_-)\partial_x(M_+-M_-)
-(M_+-M_-)\partial_x(N_+-N_-)
],
```

which is

```math
K_\parallel[N\partial_xM-M\partial_xN].
```

This expression depends only on `N` and `M`, not on the chosen positive
decompositions. Therefore the extension is well defined. It is alternating and
bilinear because the displayed formula is alternating and bilinear.

Uniqueness follows from Lemma 7.1. `square`

### Corollary 7.3: polarization from positive tests

The signed bracket can be recovered using only primitive positive-lapse tests.
For arbitrary `N,M\in V`, choose positive decompositions and evaluate the four
positive primitive curvature responses

```math
\mathcal B^+(N_+,M_+),\quad
\mathcal B^+(N_+,M_-),\quad
\mathcal B^+(N_-,M_+),\quad
\mathcal B^+(N_-,M_-).
```

Their alternating polarization is the signed bracket `\mathcal B(N,M)`.

This is the precise mathematical content of the slogan:

```text
positive stochastic deformations generate the signed infinitesimal algebra.
```

### What this theorem does not say

Theorem 7.2 does not construct a finite-regulator stochastic kernel for a
signed lapse. It constructs the unique signed continuum bilinear response
determined by positive primitive tests. A finite-regulator signed
comparison-map calculus would require an additional residual theorem:

```math
\mathcal B_a(N,M)
=
\mathcal B_a^+(N_+,M_+)-\mathcal B_a^+(N_+,M_-)
-\mathcal B_a^+(N_-,M_+)+\mathcal B_a^+(N_-,M_-)
```

with estimates uniform enough to pass to the continuum. That is a next proof
burden, not silently included here.

### Local jet version

The same conclusion is local. At a point `x`, positive lapse jets can realize
arbitrary signed bracket covectors. Given any covector value `\omega`, choose
`c>0` large enough and a compactly supported smooth bump realizing local
positive jets

```math
N(x)=1,\qquad dN_x=0,\qquad M(x)=c>0,\qquad dM_x=\omega.
```

Then

```math
N(x)dM_x-M(x)dN_x=\omega.
```

Thus the positive-cone primitive tests already probe the signed tangent
directions appearing in the hypersurface-deformation bracket. The signed
structure is not a negative stochastic process; it is the linearized
comparison algebra generated by positive stochastic processes.

### Ontological interpretation

This theorem is the clean Barandes-compatible bridge:

```text
primitive ontology: positive whole-process stochastic kernels
algebraic geometry: signed bilinear tangent/comparison bracket
```

Negative lapse functions are not primitive negative-probability operations.
They are coordinates in the real vector space obtained by group-completing the
positive cone of admissible future-directed deformations.

## 8. Comparison With Log-Smearing

The V2 log-smeared comparison map is

```math
\mathbb J_a^{\log}[N]
=
\exp\left(a\sum_nN_n\log J_n\right).
```

The primitive convex-mixture comparison map is

```math
J_a^{\rm mix}[N]
=
I+\eta a\sum_nN_n(J_n-I).
```

Both have the same leading coefficient:

```math
\mathbb J_a^{\log}[N]
=
I+\Delta^2\mathcal K_a[N]+O(\Delta^4),
```

```math
J_a^{\rm mix}[N]
=
I+\eta\Delta^2\mathcal K_a[N]+O(\Delta^4).
```

After the normalization by `\eta^2` in the exchange defect, both recover the
same leading stochastic curvature under the V2 thin-slab scaling.

The difference is ontological and technical.

| Construction | Primitive stochastic? | Signed lapses? | Main cost |
| --- | --- | --- | --- |
| Log-smearing | No, algebraic comparison map | Yes, algebraically | Uses logs/exponentials of `J`, not endpoint stochastic kernels. |
| Convex mixture | Yes for `N\ge0` | No, not as one positive kernel | Requires declared randomized whole-process protocol and positive lapse cone. |
| Weighted Hamiltonian | Yes if Hilbert lift supplied | Only with extra choices | Leading coefficient is nonlinear/signless unless carefully calibrated. |
| Trotterized stochastic protocol | Yes as declared protocol | Positive weights only | Introduces division/record structure; not indivisible by default. |

Thus primitive smooth-lapse and log-smearing are asymptotically equivalent at
the leading positive-cone curvature level, but not as full algebraic objects.

## 9. Pass/Fail Verdict

The investigation has a clean first-pass verdict.

### What passes

1. A primitive finite stochastic smooth-lapse kernel exists for bounded
   nonnegative lapse profiles by convex mixture of exact whole-process kernels.
2. The resulting comparison map has the correct leading `\mathcal K_a[N]`
   coefficient.
3. The normalized exchange defect recovers the V2 free stochastic-curvature
   limit under the same safe thin-slab scaling.
4. Positive-cone primitive curvature determines a unique signed bilinear
   hypersurface-deformation algebra by cone completion.
5. The construction is Barandes-compatible when the randomization is declared
   as the whole operation, with optional record/instrument refinement.

### What fails or remains outside scope

1. Arbitrary signed real lapse profiles are not primitive positive kernels in
   this construction; they are algebraic tangent/comparison data obtained from
   the positive cone.
2. Naive weighted-Hamiltonian Born-squared smoothing does not give a linear
   lapse coefficient; it sees `c_\theta=\theta(2-\theta)`.
3. Trotterized stochastic products require declared division events and are not
   indivisible smooth-lapse kernels by default.
4. The theorem still uses the V2 thin-slab scaling and imported singleton
   remainder bounds.
5. Interacting, Fock, gauge, and higher-dimensional versions are deferred.

The strongest honest conclusion is:

```text
Primitive smooth-lapse kernels work at the positive-cone leading-curvature
level by a declared whole-process convex-mixture protocol. The full signed
smooth-lapse bracket is then recovered rigorously as the unique bilinear
algebraic extension of the positive-cone curvature, not as a primitive
negative-probability operation.
```

## 10. Next Proof Burdens

1. Prove the singleton remainder estimate for the convex-mixture construction
   directly, rather than importing the V2 log-smearing topology.
2. Determine whether the slab scaling can be weakened from
   `\Delta(a)/a^2\to0`.
3. Lift the positive-cone-to-signed-algebra theorem from the continuum
   coefficient limit to a finite-regulator signed comparison-map calculus with
   explicit residuals.
4. Test the calibrated weighted-Hamiltonian amplitude
   `\theta(N)=1-\sqrt{1-N}` on `0\le N\le1` and quantify overlap corrections.
5. Decide whether the randomized convex mixture should be treated as Gamma-level
   operation data or as an operational instrument with an ignored clock record.
6. Extend the positive-cone primitive construction to larger support regions
   and to the V3 interacting inverse-control paper.

## 11. Current Verdict

V3 Paper 2 has a viable primitive smooth-lapse substitute for log-smearing, but
only if we keep the ontology clean. It gives a real primitive stochastic kernel
for nonnegative smooth lapses and recovers the free curvature theorem at leading
order. The signed smooth-lapse bracket is then recovered by the unique bilinear
extension of the positive-cone response, not by a primitive signed stochastic
kernel.

That is still progress. It means the V2 log-smearing construction was not pure
formal artifice: at least its leading positive-cone curvature content can be
realized by exact finite stochastic endpoint kernels. The remaining question is
whether the interacting and continuum-local parts of relativistic hypersurface
deformation can be obtained from similarly primitive positive operations whose
signed algebras arise by controlled tangent/cone completion.
