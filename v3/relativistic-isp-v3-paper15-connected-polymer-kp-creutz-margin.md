# Relativistic ISP V3 Paper 15: Connected-Polymer KP, Surface Subcriticality, And Creutz Margins

Preprint, not peer reviewed, version 2026-05-28.

Author: Felix Robles Elvira

## Abstract

Paper 14 reduced finite-block entry for actual continuum `SU(N)` Yang-Mills
to an explicit operational certificate. It exports a unique finite-block law,
a leading central character window, a forced-tower control ledger, and a
whole-process transport budget. This paper attacks the remaining Paper-13
actual-entry gates:

```text
RPF(s_0,L), KP_dec(s_0,rho,L), SUB(s_0,rho,L).
```

The central theorem is a reduction:

```text
Paper-14 FBE export
+ numerical Paper-15 certificate nCPSC
=> RCE + RKP + KP_dec + SUB + positive Creutz reserve
=> RPF + KP_dec + SUB
=> ACSB
=> RSB and the block-scale Creutz anchor.
```

The paper remains operational and Barandes-aligned. Residual polymers are not
virtual particles, hidden fields, or Markovian subprocesses. They are a
norm-controlled expansion of connected correlations in one exact
whole-process pushed-forward block record law.

### Post-Paper-20 Source Boundary

Paper 15 may export connected-polymer KP, decoration, subcriticality, and
Creutz-margin reductions. It does not export the later Paper-20 `SEL2`
tree-rate source. In particular, positive `nCPSC` or `X_15` data do not by
themselves prove

```text
q_rho gamma_rho > Theta_esc^tree,
T_-^{SEL2} > Theta_T^tree(rho).
```

Those remain active same-record coefficient/source inequalities for Paper 20
or a later source paper.

## 0. Compact Theorem Summary

The finished Paper-15 theorem is:

```text
Paper-14 FBE(s_0,rho,L)
+ positive nCPSC(s_0,rho,L)
=> X_15(s_0,L,rho).
```

Equivalently:

```text
Paper-14 FBE
+ AFRCE(A_AF,mu_AF,r_*)
+ eta_res^{bd}<1
+ eta_dec^{bd}<1
+ M_SUB^{bd}>0
+ M_15^{bd}>0
=> BC + CE + WP + RPF + KP_dec + SUB
=> ACSB(s_0,rho,L)
=> Paper-13 RSB_route(s_0,rho,L).
```

The final formal statement is Theorem 12.6. The export package is
`X_15(s_0,L,rho)` from Definition 12.5.

## 0A. Constants Ledger

| Constant | Source | Meaning | Positive/Small Condition |
| --- | --- | --- | --- |
| `mu_RG` | Paper 11, Theorem AF.14 | local-RG residual decay rate | enters `mu_base` |
| `S_RG` | Paper 11, Theorem AF.14 | summable local-RG residual tail | finite |
| `K_12^*` | Paper 12, Theorem 3.7 | finite renormalized connected-cumulant bound | finite |
| `mu_12` | Paper 12 connected-polymer localization | block-hull decay of renormalized loop cumulants | enters `mu_base` |
| `A_0,mu_0` | product reference `nu_0` | product-reference cumulant locality | finite, `mu_0>0` |
| `B_15,L_blk,c_blk` | Paper-14/Paper-15 block projection | coefficient and collar losses | finite |
| `lambda_gen` | Paper-15 generator ledger | generator refinement exponent | preferably `0` in generator-normalized branch |
| `lambda_tree` | Paper-15 tree ledger | local connected-tree exponent | must be beaten |
| `mu_base` | Definition 6B.1 | `min(mu_RG/c_blk,mu_0,mu_12)` | `>lambda_gen+lambda_tree` |
| `mu_AF` | Definition 6B.1 | exported residual decay rate | positive |
| `A_AF` | Definition 6B.1 | exported residual amplitude | finite |
| `h_an` | Definition 6B.1 | block lattice-animal entropy | must be beaten by KP decay |
| `eta_res^{bd}` | Theorem 7.2A | explicit residual KP bound | `<1` |
| `eta_ch^{bd}` | Definition 8A.1 | character-tail KP bound | finite |
| `eta_dec^{bd}` | Definition 8A.1 | combined residual plus character bound | `<1` |
| `D_*` | Definition 9A.1 | worst surface decoration growth | finite |
| `Delta_dec^{bd}` | Definition 9A.1 | worst Creutz decoration loss | finite |
| `M_SUB^{bd}` | Definition 10A.1 | surface-subcriticality reserve | `>0` |
| `T_loss^{bd}` | Definition 11A.1 | transport-loss bound | finite |
| `M_15^{bd}` | Definition 11A.2 | Creutz-margin reserve | `>0` |

The numerical certificate `nCPSC` is exactly the assertion that these
constants are computed for the same pushed-forward record law and satisfy
the displayed positivity/smallness conditions.

## 0B. Cross-Paper Reference Ledger

The cross-paper references used in Paper 15 have been checked against the
local V3 drafts:

| Paper | Local theorem/definition used | Role in Paper 15 |
| --- | --- | --- |
| Paper 11 | Theorem AF.14 | supplies `mu_RG` and summable local-RG tail `S_RG` |
| Paper 12 | Theorem 3.6C | supplies the AF local connected-polymer criterion |
| Paper 12 | Theorem 3.7 | supplies finite cumulant envelope and product-boundedness |
| Paper 13 | Definition 7.30Y | defines the six gates `BC, CE, RPF, KP_dec, SUB, WP` |
| Paper 13 | Theorem 7.30Z | proves the six gates imply `ACSB` |
| Paper 13 | Section 7.30 implication chain | records `ACSB -> SB -> surface-polymer entry -> exact RG entry -> RSB` |
| Paper 14 | Theorem 4.2 | proves `FBE => BC + CE + WP` |
| Paper 14 | Theorem 32.1 | final Paper-14 closure theorem exporting `FBE` and `X_14` |

This ledger is part of the proof hygiene: Paper 15 imports named record-law
estimates, not informal continuum-field assumptions.

## 0C. What Paper 15 Does Not Prove

Paper 15 does not prove:

1. positive `nCPSC` for actual four-dimensional continuum `SU(N)`
   Yang-Mills;
2. unconditional `AFRCE(A_AF,mu_AF,r_*)` on the full nonperturbative
   continuum trajectory;
3. mass gap, confinement, or Hilbert-space reconstruction;
4. that residual polymers are physical particles or virtual particles;
5. a Markovian decomposition of unrecorded microscopic subprocesses.

It proves the conditional bridge:

```text
if Paper-14 FBE holds and positive nCPSC holds,
then Paper 13's ACSB/RSB route is open on the declared finite battery.
```

## 1. Ontological Discipline

The objects of this paper are:

1. finite block record laws exported by Paper 14;
2. central character records and scalar Wilson-loop records;
3. connected cumulants of declared block records;
4. polymer activities derived from those cumulants;
5. finite surface and Creutz batteries.

The forbidden moves are:

1. treating residual polymers as microscopic particles;
2. composing partial kernels that were never declared as recorded
   subprocesses;
3. using a gauge-fixed field as ontology rather than as a certificate
   coordinate;
4. importing a mass gap, confinement, or a Hilbert-space spectrum before the
   representation layer has been reconstructed.

## 2. Imports From Paper 14

Paper 14 exports the finite tuple

```text
X_14(s_0,L,rho)
  = (
      nu_{s_0,L},
      u_-,
      u_+,
      M_cRGCE,
      Tail_CE,
      C_geom,
      m_F,
      g_c,
      FTS_margin,
      q_k,
      r_k,
      E_14^*,
      Lambda_*,
      D_*,
      L_tr
    ).
```

The entries mean:

1. `nu_{s_0,L}`: the unique finite-block continuum law;
2. `u_- <= u_rho <= u_+`: the leading character coefficient window;
3. `M_cRGCE`: the positive coefficient reserve;
4. `Tail_CE`: the non-leading character tail;
5. `C_geom,m_F,g_c,FTS_margin`: forced-tower control data;
6. `q_k,r_k`: shell-invertibility data;
7. `E_14^*`: remaining whole-process transport budget;
8. `Lambda_*`, `D_*`, `L_tr`: representation, degree, and Lipschitz data.

Paper 15 may use these only as operational record-law data.

## 3. Imports From Paper 13

Paper 13 split actual-continuum strong-block entry into six gates:

```text
BC, CE, RPF, KP_dec, SUB, WP.
```

Paper 14 proves the first, second, and sixth gates conditionally:

```text
FBE => BC + CE + WP.
```

This paper is responsible for the remaining three:

1. `RPF(s_0,L)`: local residual factorization of the exact block law relative
   to the extracted central character product.
2. `KP_dec(s_0,rho,L)`: one compatible decoration gas controls both residual
   polymers and non-leading character insertions.
3. `SUB(s_0,rho,L)`: surface entropy and decoration growth are beaten by the
   leading character coefficient.

## 4. Block Graph And Local Record Supports

Fix the finite block graph `G_blk` supporting the Creutz battery at physical
scale `s_0`. Its vertices are block cells and its plaquettes are block
plaquettes used in the finite battery.

For any finite connected set `X subset G_blk`, let `A_X` be the finite
algebra generated by declared scalar records supported in `X`.

A polymer is a finite connected set

```text
Gamma subset G_blk.
```

Two polymers are compatible if their graph distance is at least one block
cell, or more generally at least the declared interaction collar required by
the finite block record algebra.

## 5. Leading Product Reference And Residual Functional

### Definition 5.1: Product Character Reference

Using the Paper-14 coefficient window, define the central one-plaquette
reference factor

```text
K_p(U_p)
  = 1 + u_rho chi_rho(U_p) + R_p(U_p),
```

where `u_rho in [u_-,u_+]` and the non-leading character tail satisfies

```text
||R_p||_ch <= Tail_CE.
```

Let `nu_0` be the finite product reference law obtained from the product of
the `K_p` factors on the declared plaquette battery, normalized on the finite
record space.

### Definition 5.2: Residual Functional

The residual functional is the multilinear functional

```text
Res(F_1,...,F_n)
  = kappa_{nu_{s_0,L}}(F_1,...,F_n)
    - kappa_{nu_0}(F_1,...,F_n),
```

for local centered records `F_i in A_{X_i}`.

This definition avoids assuming a pointwise density ratio when a finite
record law is singular with respect to the product reference. If a
Radon-Nikodym density exists, this cumulant residual agrees with the usual
connected expansion of that density.

### Proposition 5.3: Density Branch Implies Cumulant Branch

If the exact finite-block law has a density

```text
d nu_{s_0,L}
  = Z^{-1} (prod_p K_p(U_p)) R(U) dU
```

with respect to the product reference, then the connected cumulants of
`log R` generate the residual functional of Definition 5.2.

Proof.

The logarithm of the moment generating functional of `nu_{s_0,L}` differs
from that of `nu_0` by the connected cumulant expansion of `R`. Differentiating
with respect to local sources gives exactly the residual cumulants. `square`

## 6. Residual Cumulant Envelope

### Definition 6.1: Residual Cumulant Envelope `RCE(A,mu,r_*)`

The finite-block law satisfies `RCE(A,mu,r_*)` if, for all declared normalized
atomic records or coefficient-normalized local record monomials
`F_i in A_{X_i}` with `||F_i||_{15} <= 1`, all `1<=n<=r_*`, and
`X=Hull(X_1 union ... union X_n)` connected,

```text
|Res(F_1,...,F_n)|
  <= A exp(-mu |X|) exp(-mu diam(X)).
```

Here `||.||_{15}` is the finite-battery coefficient norm induced by the
declared Paper-14 block generators: scalar central characters, scalar
Wilson-loop records, and the finite block-collar products admitted by the
Creutz battery. The constants `A` and `mu` are operational constants for the
pushed-forward record law. They are not particle masses unless a later
representation theorem identifies them as such.

The coefficient norm clause is essential. Exponential decay in `|X|` for
every bounded function on a large support is not the right cluster-expansion
input and is not expected in ordinary local field theory. The KP proof uses
decay of generated connected residual activities, not arbitrary macroscopic
decision functions on a large region.

### Proposition 6.2: Naive Sup-Norm `RCE` Is Too Strong

The following stronger statement is not used:

```text
for every bounded centered F_i with ||F_i||_infty <= 1,
|Res(F_1,...,F_n)| <= A exp(-mu |X|) exp(-mu diam(X)).
```

It is generally false for local continuum limits.

Proof.

Even in a classical high-temperature lattice model with a small nearest-block
interaction, take two adjacent slabs `S` and `T` with `|S|=|T|=N`, and set

```text
F_S = N^{-1} sum_{x in S} f_x,
G_T = N^{-1} sum_{y in T} g_y,
```

with local centered `|f_x|,|g_y|<=1`. Then `||F_S||_infty,||G_T||_infty<=1`.
The connected covariance receives contributions from bonds crossing the
interface and is typically of order `|partial S|/N^2`, or another polynomial
surface/volume scale, not `exp(-cN)`. Subtracting a product reference removes
independent one-site cumulants but not the connected boundary contribution
created by the local interaction. Thus volume-exponential decay for arbitrary
bounded macroscopic functions would rule out ordinary local interacting
record laws. The correct statement is the coefficient-normalized generator
or local-potential envelope above. `square`

### Definition 6.3: Residual Polymer Activity

For each connected polymer `Gamma`, define the residual activity
`phi_res(Gamma)` by the standard cumulant-to-polymer transform applied to
the residual cumulants supported in `Gamma`.

The activity norm is

```text
||phi_res(Gamma)||_op
  = sup |phi_res(Gamma;F_1,...,F_n)|,
```

where the supremum is over the finite local records admitted by the battery.

### Lemma 6.4: Cumulant Envelope Bounds Activities

If `RCE(A,mu,r_*)` holds, then there is a finite combinatorial constant
`C_cum(d,r_*)` such that

```text
||phi_res(Gamma)||_op
  <= C_cum A exp(-mu |Gamma|) exp(-mu diam(Gamma)).
```

Proof.

The cumulant-to-polymer transform expresses each connected activity as a
finite sum over connected partitions and finite source derivatives supported
in `Gamma`. The number of such terms is bounded by `C_cum(d,r_*)` at fixed
dimension and finite cumulant order. Applying the residual cumulant envelope
to each connected term gives the displayed bound. `square`

## 6A. Reduction Of `RCE` From The Actual Continuum Trajectory

This section is the hard boundary of Paper 15. It proves that the Paper-15
`RCE` certificate follows from the actual continuum trajectory only after
one imports the precise Paper-11/Paper-12 local-RG and renormalized-loop
ledgers. Nothing here treats an intermediate gauge field as ontology; gauge
charts and RG polymers are certificate coordinates for one exact
whole-process pushed-forward record law.

### Definition 6A.1: Block Generator Battery

For the fixed physical block scale `s_0`, let

```text
G_{15}(s_0,L)
```

be the finite block generator battery consisting of:

1. the scalar central character generators used in Paper 14;
2. the scalar Wilson-loop and Creutz-loop records used in Papers 12--14;
3. their finite block-collar products of degree at most `r_*`;
4. the finite centering constants determined by `nu_{s_0,L}` and `nu_0`.

The norm `||.||_{15}` is the projective coefficient norm in this generator
battery. For a local generator expression

```text
F = sum_b c_b G_b,
```

we set

```text
||F||_{15} = inf sum_b |c_b|,
```

where the infimum is over all declared expansions in the finite battery.
Let `B_15` be the finite comparison constant satisfying

```text
||F||_infty <= B_15 ||F||_{15}
```

on the declared battery. No inverse comparison from `||.||_infty` to
`||.||_{15}` is used; that inverse would grow with support and would destroy
the volume-decay margin.

### Definition 6A.2: AF Residual-Cumulant Certificate `AFRCE`

The actual continuum trajectory satisfies `AFRCE(A_AF,mu_AF,r_*)` on the
Paper-15 battery if the following constants are finite and declared:

1. **Paper-11 local-RG tail.** Along the ledger-compatible AF trajectory,
   Theorem AF.14 supplies constants `alpha`, `mu_RG`, `G_r`, `Q_r^*`,
   and `R_r` such that

   ```text
   eta_r <= 2 exp(alpha) G_r Q_r^* exp(-mu_RG R_r),
   S_RG := sum_{r>=r_0} eta_r < infinity.
   ```

2. **Paper-12 renormalized connected-polymer envelope.** For every admissible
   scalar Wilson-loop tuple in the finite battery, Paper 12 supplies not only
   the finite cumulant bound of Theorem 3.7 but also a connected-polymer
   localization rate `mu_12>0` on the block-collar graph:

   ```text
   |kappa_a(X_1,...,X_n)| <= K_12(alpha_tuple)
   ```

   after perimeter/cusp calibration, and the localized refinement

   ```text
   |kappa_a^{conn}(X_1,...,X_n; X)|
   <= K_12^* exp(-mu_12 |X|) exp(-mu_12 diam(X))
   ```

   for the connected block hull `X`. The local connected-polymer
   decomposition is supplied either directly or by Paper 12 Theorem 3.6C,
   while the positive rate `mu_12` is an explicit part of this Paper-15
   reduction certificate.

3. **Block projection Lipschitz control.** The Paper-14 finite-block
   pushforward from the continuum loop battery to `G_{15}` has coefficient
   Lipschitz constant `L_blk` and collar enlargement constant `c_blk`.

4. **Product-reference locality.** The leading product reference `nu_0`
   has cumulants supported inside one declared product collar and satisfies

   ```text
   |kappa_{nu_0}(F_1,...,F_n)|
   <= A_0 exp(-mu_0 |X|) exp(-mu_0 diam(X))
   ```

   for coefficient-normalized generators, with the convention that the
   cumulant is zero when the supports lie in distinct independent collars.

5. **Raw margin.** After the finite generator, collar, and tree-graph losses
   are charged, there is a positive number

   ```text
   mu_raw
   :=
   min(mu_RG/c_blk, mu_0, mu_12)
   - lambda_gen
   - lambda_tree
   >0.
   ```

Here `lambda_gen` is the coefficient-growth loss of the finite block
generator battery and `lambda_tree` is the connected-tree counting loss in
the cumulant-to-polymer transform. Define the preliminary amplitude

```text
A_pre :=
2 B_15^{r_*} L_blk^{r_*}
(
  A_0
  + K_12^*
  + S_RG
),
```

where `K_12^*` is the maximum Paper-12 connected cumulant constant over the
finite tuples in `G_{15}` of degree at most `r_*`. The certificate exports
`mu_AF=mu_raw/2` and any finite `A_AF` dominating `A_pre` after the
finite small-hull correction made explicit in Definition 6B.1.

### Lemma 6A.3: Whole-Process Local-RG Tail Gives Connected Decay

Assume the Paper-11 local-RG tail in `AFRCE`. Let `F_1,...,F_n` be
coefficient-normalized block records, and let
`X=Hull(X_1 union ... union X_n)`. Choose the local ansatz radius for this
tuple so that

```text
R(X) >= c_blk ( |X| + diam(X) ).
```

Then the contribution of all omitted local-RG polymers to the residual
cumulant obeys

```text
|Res_tail(F_1,...,F_n)|
<=
B_15^n L_blk^n S_RG
exp(-mu_RG c_blk^{-1}|X|)
exp(-mu_RG c_blk^{-1}diam(X)).
```

Proof.

Paper 11 Theorem AF.14 bounds the one-block local-RG residual by a summable
ledger entry `eta_r`. The local-radius choice assigns every omitted polymer
that can connect the tuple to a collar at least of size
`c_blk^{-1}(|X|+diam(X))` in block units. Multiplying the Paper-11 residual
bound by the finite coefficient and projection Lipschitz constants gives the
displayed estimate. This is a bound on the exact pushed-forward record law;
it does not compose hidden partial kernels. `square`

### Lemma 6A.4: Paper-12 Renormalized Loop Control Bounds The Local Part

Assume the Paper-12 cumulant envelope in `AFRCE`. The local connected part of
the exact continuum trajectory, after the perimeter/cusp counterterm ledger
and Paper-14 block projection are applied, satisfies

```text
|Res_loc(F_1,...,F_n)|
<=
B_15^n L_blk^n K_12^*
exp(-mu_12 |X|)
exp(-mu_12 diam(X))
```

for coefficient-normalized block records in the Paper-15 battery.

Proof.

Paper 12 Theorem 3.7 gives finite cumulant control for the renormalized
unsmeared Wilson-loop records in every finite admissible tuple. Paper 12
Lemmas 3.6A--3.6C identify the only local UV singularities on the clean class
as perimeter and cusp terms and prove that the remaining connected polymer
tails are summable on the AF trajectory. The extra Paper-15 requirement in
`AFRCE` is that this summability is quantified by the block-hull decay rate
`mu_12`. Paper 14's block projection is a finite coefficient-Lipschitz map
from those loop and character records to the Paper-15 generators. The
connected-tree distance can only shrink by the finite collar factor already
charged in `mu_12`; applying the Lipschitz and coefficient constants gives
the displayed bound. `square`

### Lemma 6A.5: Product Reference Subtraction Is Local

Assume product-reference locality in `AFRCE`. Then subtracting
`kappa_{nu_0}` changes the connected decay constants by at most the finite
term `A_0` already included in `A_AF`.

Proof.

The reference `nu_0` is a product of declared one-plaquette character
factors. Its mixed cumulants vanish between independent collars. Inside one
collar there are only finitely many coefficient-normalized generator tuples,
so their cumulants are bounded by `A_0` with the displayed finite-range
envelope. Subtracting this local term preserves the same exponential
envelope after taking the minimum decay rate. `square`

### Theorem 6A.6: `AFRCE` Proves Paper-15 `RCE`

If the actual continuum trajectory satisfies `AFRCE(A_AF,mu_AF,r_*)`, then
the finite-block law `nu_{s_0,L}` satisfies

```text
RCE(A_AF,mu_AF,r_*).
```

Proof.

For coefficient-normalized local records, decompose the residual cumulant as

```text
Res = Res_loc + Res_tail - kappa_{nu_0}^{loc}.
```

Lemma 6A.3 bounds `Res_tail`. Lemma 6A.4 bounds `Res_loc`. Lemma 6A.5 bounds
the product-reference subtraction. The raw margin hypothesis says the
smallest decay rate remaining after generator and tree-counting losses is
positive. Halving that positive rate absorbs all finite collar and
small-support exceptions into the constant `A_AF`. Hence the residual
cumulant obeys

```text
|Res(F_1,...,F_n)|
<=
A_AF exp(-mu_AF |X|) exp(-mu_AF diam(X)).
```

This is Definition 6.1. `square`

### Corollary 6A.7: `AFRCE + RKP` Gives The First Paper-15 Gate

If `AFRCE(A_AF,mu_AF,r_*)` holds and

```text
C_cum A_AF C_KP(mu_AF,m)<1,
```

then `RPF(s_0,L)` holds.

Proof.

Theorem 6A.6 gives `RCE(A_AF,mu_AF,r_*)`. The displayed inequality is exactly
`RKP(A_AF,mu_AF,m)`. Theorem 7.3 then proves `RPF`. `square`

### Honest Boundary Of The `RCE` Reduction

The result above is the sharp reduction currently available:

```text
Paper-11 AF multiscale local-RG summability
+ Paper-12 finite-battery renormalized connected cumulants
+ Paper-14 finite-block projection and product reference locality
+ positive raw decay margin after generator/tree losses
=> Paper-15 RCE.
```

What is not yet proved unconditionally is that actual four-dimensional
continuum `SU(N)` Yang-Mills satisfies all clauses of `AFRCE` beyond the
controlled finite-battery AF trajectory. In particular, the remaining hard
inputs are:

1. uniform or slowly degrading covariance/local-polymer constants on the
   actual nonperturbative trajectory;
2. Paper-12 local connected-polymer decomposition beyond the clean finite
   admissible loop class;
3. a positive raw margin `mu_raw>0` after generator growth and tree entropy;
4. compatibility of the finite-block projection with regulator and gauge
   chart changes.

Thus Paper 15 now proves `RCE` from named constructive ledgers. It does not
pretend that the full Clay-level continuum Yang-Mills construction has been
completed.

## 6B. Explicit Constants, Raw Margin, And The First KP Test

This section turns `AFRCE` into a computable finite-battery certificate. The
constants are still operational constants of the pushed-forward record law;
they are not hidden field-theoretic objects.

### Definition 6B.1: Numerical `AFRCE` Ledger

Fix the Paper-15 finite block graph and generator battery. Define:

```text
Delta_blk  = maximum degree of the block adjacency graph,
a_blk      = e(Delta_blk-1),
h_an       = log a_blk,
```

so that the number `N_n(x)` of connected block polymers of size `n`
containing a fixed block `x` obeys the standard lattice-animal bound

```text
N_n(x) <= a_blk^n.
```

Let:

```text
C_gen      = maximal number of declared generator refinements per block,
lambda_gen = log C_gen,
C_tree     = local connected-tree refinement base,
lambda_tree = log C_tree,
mu_base    = min(mu_RG/c_blk, mu_0, mu_12).
```

The constants `lambda_gen` and `lambda_tree` are pre-KP losses. They count
only generator refinements and local tree refinements inside a fixed block
hull. They do not count the number of possible external polymers; that
external entropy is `h_an` and enters the KP test below.

The amplitude ledger is:

```text
A_pre
  =
  2 B_15^{r_*} L_blk^{r_*}
  (
    A_0
    + K_12^*
    + S_RG
  ).
```

The numerical `AFRCE` ledger is positive if:

```text
mu_raw := mu_base - lambda_gen - lambda_tree > 0.
```

It then exports:

```text
mu_AF = mu_raw/2,
A_AF  = A_pre C_small(mu_raw,G_blk,r_*),
```

where `C_small` is the finite correction for hulls whose size is below the
asymptotic collar radius used in Lemmas 6A.3--6A.4. Explicitly, one may take

```text
C_small
 =
 max(
   1,
   max_{1<=|X|<=X_0}
   exp(mu_raw |X|/2) exp(mu_raw diam(X)/2)
 )
```

with `X_0` the largest small hull not covered by the asymptotic collar
estimate. Since the battery is finite, `C_small<infinity`.

### Proposition 6B.2: Generator-Normalized Branch Removes `lambda_gen`

If every admitted finite block-collar monomial in `G_{15}` is treated as a
declared generator with projective coefficient norm, then one may take

```text
C_gen=1,
lambda_gen=0.
```

Proof.

The coefficient norm charges the whole declared monomial as one operational
record rather than expanding it into all microscopic words. Therefore the
number of generator refinements does not grow exponentially with the hull
size. Any finite comparison between this declared generator and an underlying
Wilson-loop or character expression is absorbed into `B_15` and `L_blk`,
which affect amplitude but not the decay exponent. `square`

This is the Barandes-aligned branch: records are declared operational
readouts, not hidden microscopic decompositions.

### Theorem 6B.3: Raw-Margin Certificate

Assume the numerical `AFRCE` ledger of Definition 6B.1. If

```text
mu_base > lambda_gen + lambda_tree,
```

then Theorem 6A.6 applies with

```text
mu_AF = (mu_base - lambda_gen - lambda_tree)/2
```

and finite amplitude `A_AF`.

In the generator-normalized branch of Proposition 6B.2, this reduces to

```text
mu_base > lambda_tree.
```

Proof.

The inequality is precisely `mu_raw>0`. Lemmas 6A.3--6A.5 give decay at rate
`mu_base` before pre-KP generator and local-tree losses. Subtracting those
losses leaves `mu_raw`. Halving the positive remainder absorbs finite
small-hull exceptions into `C_small`, so Theorem 6A.6 gives
`RCE(A_AF,mu_AF,r_*)`. In the generator-normalized branch
`lambda_gen=0` by Proposition 6B.2. `square`

### Definition 6B.4: First-Gate Numerical Output

The first-gate numerical output of Paper 15 is the tuple

```text
Y_15^{(1)}
 =
 (
   A_AF,
   mu_AF,
   h_an,
   C_cum(d,r_*),
   C_KP(mu_AF,m),
   eta_res
 ).
```

It is computable from:

1. Paper-11 constants `alpha,mu_RG,G_r,Q_r^*,R_r`;
2. Paper-12 constants `K_12^*,mu_12`;
3. Paper-14 constants `B_15,L_blk,c_blk,A_0,mu_0`;
4. finite block graph constants `Delta_blk,a_blk,h_an`;
5. pre-KP losses `lambda_gen,lambda_tree`.

This tuple is what Paper 16 should import if Paper 15 is used as a positive
entry gate.

## 7. Connected-Polymer KP Criterion

### Definition 7.1: KP Geometry Constant

For `m>0` define

```text
C_KP(mu,m)
  =
  sup_x
  sum_{Gamma connected, Gamma contains x}
  exp(-(mu-m)|Gamma|) exp(-mu diam(Gamma)).
```

On a finite-dimensional bounded-degree block graph, `C_KP(mu,m)` is finite
whenever `0<m<mu` and `mu-m` is larger than the lattice animal entropy.

### Lemma 7.1A: Explicit Lattice-Animal Bound

With `h_an` from Definition 6B.1, if

```text
delta_KP := mu-m-h_an > 0,
```

then

```text
C_KP(mu,m)
<=
exp(-delta_KP)/(1-exp(-delta_KP)).
```

Proof.

Ignoring the extra factor `exp(-mu diam(Gamma))<=1` only increases the sum.
Using `N_n(x)<=exp(h_an n)` gives

```text
C_KP(mu,m)
<=
sum_{n>=1} exp(h_an n) exp(-(mu-m)n)
=
sum_{n>=1} exp(-delta_KP n)
=
exp(-delta_KP)/(1-exp(-delta_KP)).
```

`square`

### Definition 7.2: Residual KP Certificate `RKP(A,mu,m)`

The residual KP certificate holds if

```text
eta_res
  :=
  C_cum A C_KP(mu,m)
  < 1.
```

### Theorem 7.2A: Explicit First KP Smallness Test

Assume the numerical `AFRCE` ledger is positive, so Theorem 6B.3 exports
`A_AF` and `mu_AF`. Choose `m` with

```text
0<m<mu_AF-h_an.
```

Define

```text
delta_KP = mu_AF-m-h_an,
eta_res^{bd}
 =
 C_cum(d,r_*) A_AF
 exp(-delta_KP)/(1-exp(-delta_KP)).
```

If

```text
eta_res^{bd}<1,
```

then `RKP(A_AF,mu_AF,m)` holds, and consequently `RPF(s_0,L)` holds.

Proof.

Lemma 7.1A gives

```text
C_KP(mu_AF,m)
<= exp(-delta_KP)/(1-exp(-delta_KP)).
```

Thus

```text
eta_res
= C_cum A_AF C_KP(mu_AF,m)
<= eta_res^{bd}<1.
```

This is `RKP(A_AF,mu_AF,m)`. Corollary 6A.7 then gives `RPF`. `square`

### Corollary 7.2B: Canonical Half-Margin Choice

If

```text
mu_AF > h_an
```

and one chooses

```text
m_0 = (mu_AF-h_an)/2,
delta_0 = (mu_AF-h_an)/2,
```

then the sufficient first-gate test is

```text
C_cum(d,r_*) A_AF
exp(-delta_0)/(1-exp(-delta_0))
< 1.
```

This choice is not optimal, but it is explicit and leaves a positive KP
weight `m_0`.

### Theorem 7.3: `RKP` Proves Residual Factorization

If `RCE(A,mu,r_*)` and `RKP(A,mu,m)` hold, then `RPF(s_0,L)` holds.

Proof.

Lemma 6.4 bounds the residual activities. The definition of `C_KP` gives

```text
sup_x
sum_{Gamma contains x}
||phi_res(Gamma)||_op e^{m|Gamma|}
<= eta_res < 1.
```

Thus the residual cumulant expansion is an absolutely convergent compatible
polymer gas on the finite block graph. This is the local residual
factorization required by `RPF`. `square`

## 8. Combining Residual Polymers With Character Decorations

### Definition 8.1: Character Decoration Activity

The non-leading character remainder `R_p` from Paper 14 is represented as a
single-plaquette decoration activity with norm bounded by

```text
eta_ch := C_ch Tail_CE,
```

where `C_ch` is the finite character-to-record norm constant on the declared
representation battery.

### Definition 8.2: Combined Decoration KP Constant

Define

```text
eta_dec := eta_res + eta_ch.
```

The combined decoration KP certificate holds if

```text
eta_dec < 1.
```

### Theorem 8.3: Combined KP Proves `KP_dec`

If `RKP(A,mu,m)` holds and `eta_dec<1`, then
`KP_dec(s_0,rho,L)` holds.

Proof.

The residual polymers and non-leading character insertions form one
compatible decoration gas. The residual part contributes `eta_res` to the KP
sum, and the single-plaquette character decorations contribute `eta_ch`.
Their sum is `eta_dec<1`, so the combined decoration gas satisfies the
Kotecky-Preiss smallness condition required by `KP_dec`. `square`

## 8A. Numerical Decoration Smallness

The first KP gate controls residual polymers. The next gate asks whether the
non-leading character decorations exported by Paper 14 fit inside the same
KP margin.

### Definition 8A.1: Character-Tail Ledger

Let `C_ch` be the finite character-to-record norm constant on the declared
representation battery. Paper 14 exports `Tail_CE`. Define:

```text
eta_ch^{bd} := C_ch Tail_CE,
eta_dec^{bd} := eta_res^{bd} + eta_ch^{bd},
M_dec := 1 - eta_dec^{bd}.
```

Here `eta_res^{bd}` is the explicit residual bound from Theorem 7.2A. The
decoration ledger is positive if

```text
M_dec > 0.
```

### Theorem 8A.2: Explicit Decoration Smallness Proves `KP_dec`

Assume Theorem 7.2A gives `eta_res<=eta_res^{bd}` and Paper 14 gives
`eta_ch<=eta_ch^{bd}`. If

```text
eta_dec^{bd}<1,
```

then the combined decoration KP certificate holds and
`KP_dec(s_0,rho,L)` follows.

Proof.

By the two displayed bounds,

```text
eta_dec = eta_res + eta_ch
<= eta_res^{bd} + eta_ch^{bd}
= eta_dec^{bd}<1.
```

Theorem 8.3 then proves `KP_dec`. `square`

### Corollary 8A.3: Character-Tail Budget

If the residual KP bound has already consumed `eta_res^{bd}<1`, then the
allowed Paper-14 character tail is:

```text
Tail_CE < (1-eta_res^{bd})/C_ch.
```

This is the finite-character tail budget that Paper 14 must export for the
Paper-15 route to remain open.

## 9. Decoration Constants For Surfaces

### Definition 9.1: Surface Decoration Constants

For each Creutz loop `C`, define:

```text
D_C(eta_dec)
  = exp( c_surf eta_dec / (1-eta_dec) ),
xi_C(eta_dec)
  = c_C eta_dec / (1-eta_dec),
xi'_C(eta_dec)
  = c'_C eta_dec / (1-eta_dec).
```

The constants `c_surf,c_C,c'_C` depend only on the finite block graph, the
surface collar convention, and the finite Creutz battery.

### Proposition 9.2: KP Gives Surface Decoration Bounds

If `eta_dec<1`, then the decoration partition functions attached to the
minimal and nonminimal surfaces of the four Creutz loops obey the Paper-13
surface bounds with constants `D_C,xi_C,xi'_C` from Definition 9.1.

Proof.

The KP expansion gives absolute convergence of the logarithm of each finite
decoration partition function. A surface of excess area `q` has at most
`c_surf q + O(1)` additional collar sites. Summing the KP bound over the
collar gives a logarithmic correction bounded by
`c_surf eta_dec q/(1-eta_dec)` plus a finite minimal-collar constant. This
exponentiates to the displayed `D_C,xi_C,xi'_C` bounds. `square`

## 9A. Explicit Surface And Creutz Decoration Losses

### Definition 9A.1: Uniform Decoration-Loss Constants

For the finite Creutz battery define:

```text
c_surf^* = max_C c_surf(C),
c_xi^*   = max_C c_C,
c_xip^*  = max_C c'_C,
c_Delta^* = c_xi^* + c_xip^*.
```

Using the numerical decoration bound `eta_dec^{bd}<1`, set:

```text
D_* =
exp( c_surf^* eta_dec^{bd} / (1-eta_dec^{bd}) ),

xi_* =
c_xi^* eta_dec^{bd} / (1-eta_dec^{bd}),

xi'_* =
c_xip^* eta_dec^{bd} / (1-eta_dec^{bd}),

Delta_dec^{bd}
=
exp( c_Delta^* eta_dec^{bd} / (1-eta_dec^{bd}) ) - 1.
```

These are finite once `eta_dec^{bd}<1`.

### Theorem 9A.2: Explicit KP Loss Bounds

If `eta_dec<=eta_dec^{bd}<1`, then for every Creutz loop `C` in the finite
battery:

```text
D_C(eta_dec) <= D_*,
xi_C(eta_dec) <= xi_*,
xi'_C(eta_dec) <= xi'_*,
Delta_dec(eta_dec) <= Delta_dec^{bd}.
```

Proof.

The functions `x -> x/(1-x)` and `x -> exp(c x/(1-x))` are increasing on
`0<=x<1`. Substitute `eta_dec<=eta_dec^{bd}` and take the finite maxima of
the surface constants. `square`

## 10. Surface Subcriticality

### Definition 10.1: SUB Reserve

Let `E_C^surf` be the finite surface entropy constant from Paper 13. Define

```text
u_*^{15}
  =
  min_C (E_C^surf D_C(eta_dec))^{-1}.
```

The Paper-15 surface-subcriticality reserve is

```text
M_SUB
  = u_*^{15} - u_+.
```

### Theorem 10.2: Positive SUB Reserve Proves `SUB`

If

```text
M_SUB > 0,
```

then `SUB(s_0,rho,L)` holds.

Proof.

`M_SUB>0` means `u_+ < (E_C^surf D_C)^{-1}` for every Creutz loop `C`.
Since `u_rho <= u_+`, it follows that

```text
E_C^surf D_C u_rho < 1
```

for every loop. This is exactly the surface subcriticality gate. `square`

## 10A. Numerical Surface Subcriticality Test

### Definition 10A.1: Explicit `SUB` Reserve

Let

```text
E_surf^* = max_C E_C^surf.
```

Using `D_*` from Definition 9A.1, define:

```text
u_*^{bd} = (E_surf^* D_*)^{-1},
M_SUB^{bd} = u_*^{bd} - u_+.
```

The numerical surface-subcriticality ledger is positive if

```text
M_SUB^{bd}>0.
```

### Theorem 10A.2: Explicit `SUB` Reserve Proves `SUB`

If `M_SUB^{bd}>0`, then `M_SUB>0` and hence
`SUB(s_0,rho,L)` holds.

Proof.

For every Creutz loop `C`, `E_C^surf<=E_surf^*` and
`D_C(eta_dec)<=D_*` by Theorem 9A.2. Therefore

```text
(E_C^surf D_C(eta_dec))^{-1}
>=
(E_surf^* D_*)^{-1}
=
u_*^{bd}.
```

Thus

```text
M_SUB
= min_C (E_C^surf D_C)^{-1} - u_+
>= u_*^{bd} - u_+
= M_SUB^{bd}>0.
```

Theorem 10.2 proves `SUB`. `square`

## 11. Creutz Margin Reserve

### Definition 11.1: Paper-15 Creutz Margin

Let `N_0` and `Q_sigma` be the Paper-13 minimal-sheet and first-excess
surface constants. Let `T_loss` be the total transport loss inherited from
Paper 11, Paper 12, Paper 13, and the Paper-14 `WP` budget. Define

```text
M_15
  =
  u_-^{N_0}
  (1-u_+^{Q_sigma})
  - Delta_dec(eta_dec)
  - T_loss,
```

where

```text
Delta_dec(eta_dec)
  =
  exp(xi_C(eta_dec)+xi'_C(eta_dec))
  - 1
```

is the finite decoration loss, maximized over the four Creutz loops.

### Theorem 11.2: Positive Creutz Margin Survives Decorations

If

```text
M_15 > 0,
```

then the block-scale Creutz anchor survives the residual decoration gas and
the declared transport losses with positive reserve.

Proof.

The leading minimal sheet contributes at least `u_-^{N_0}`. The first
nonminimal sheet suppression is bounded by `1-u_+^{Q_sigma}`. Decoration
partition functions change this by at most `Delta_dec(eta_dec)`, and all
finite-volume, loop-approximation, chart, counterterm, and prior transport
losses are bounded by `T_loss`. The displayed positivity says the lower
bound remains strictly positive. `square`

## 11A. Numerical Creutz Margin Test

### Definition 11A.1: Transport-Loss Ledger

Decompose the finite transport loss as:

```text
T_loss
 =
 T_11 + T_12 + T_13 + T_14,
```

where:

1. `T_11` is the Paper-11 local-RG, reflection-positivity,
   Euclidean-covariance, and gauge-reconstruction ledger loss;
2. `T_12` is the Paper-12 perimeter/cusp, smearing-removal, and
   loop-approximation ledger loss;
3. `T_13` is the Paper-13 surface-polymer and exact-entry transport loss;
4. `T_14` is the Paper-14 whole-process finite-block projection loss,
   bounded by the exported `E_14^*`.

Let `T_loss^{bd}` be any declared finite upper bound for this sum.

### Definition 11A.2: Explicit Creutz Reserve

Using the decoration loss `Delta_dec^{bd}` from Definition 9A.1, define:

```text
M_15^{bd}
 =
 u_-^{N_0}
 (1-u_+^{Q_sigma})
 - Delta_dec^{bd}
 - T_loss^{bd}.
```

The numerical Creutz ledger is positive if

```text
M_15^{bd}>0.
```

### Theorem 11A.3: Explicit Creutz Reserve Proves Positive Margin

If `M_15^{bd}>0`, then `M_15>0`, so the block-scale Creutz anchor survives
decorations and transport losses.

Proof.

Theorem 9A.2 gives `Delta_dec(eta_dec)<=Delta_dec^{bd}`. The transport
ledger gives `T_loss<=T_loss^{bd}`. Therefore

```text
M_15
>=
u_-^{N_0}(1-u_+^{Q_sigma})
- Delta_dec^{bd}
- T_loss^{bd}
=
M_15^{bd}>0.
```

Theorem 11.2 applies. `square`

## 12. Paper-15 Closure Certificate

### Definition 12.1: Connected-Polymer Surface Certificate `CPSC`

The Paper-15 connected-polymer surface certificate consists of:

1. Paper-14 `FBE` and export package `X_14`;
2. `RCE(A,mu,r_*)`, either assumed directly or proved from `AFRCE` by
   Theorem 6A.6;
3. `RKP(A,mu,m)`;
4. combined decoration smallness `eta_dec<1`;
5. positive surface reserve `M_SUB>0`;
6. positive Creutz margin `M_15>0`;
7. whole-process compatibility: all constants are stable under the Paper-14
   `WP` ledger and are computed for the exact pushed-forward block record
   law.

### Definition 12.1A: Numerical Connected-Polymer Surface Certificate `nCPSC`

The numerical Paper-15 certificate `nCPSC` is the finite tuple:

```text
nCPSC
 =
 (
   X_14,
   A_AF,
   mu_AF,
   h_an,
   C_cum,
   eta_res^{bd},
   C_ch,
   Tail_CE,
   eta_ch^{bd},
   eta_dec^{bd},
   D_*,
   Delta_dec^{bd},
   E_surf^*,
   M_SUB^{bd},
   N_0,
   Q_sigma,
   T_loss^{bd},
   M_15^{bd}
 ).
```

It is positive if:

```text
AFRCE(A_AF,mu_AF,r_*) holds,
eta_res^{bd}<1,
eta_dec^{bd}<1,
M_SUB^{bd}>0,
M_15^{bd}>0,
```

and all constants are computed for the same exact pushed-forward block record
law and the same Paper-14/Paper-15 finite battery.

### Theorem 12.1B: `nCPSC` Proves `CPSC`

If `nCPSC` is positive, then `CPSC` holds.

Proof.

`AFRCE` and Theorem 6A.6 give `RCE(A_AF,mu_AF,r_*)`. The inequality
`eta_res^{bd}<1` and Theorem 7.2A give `RKP` and `RPF`. The inequality
`eta_dec^{bd}<1` and Theorem 8A.2 give `KP_dec`. The positive
`M_SUB^{bd}` gives `SUB` by Theorem 10A.2. The positive `M_15^{bd}` gives
the Creutz margin by Theorem 11A.3. The whole-process compatibility clause
is part of the certificate definition. These are exactly the entries of
`CPSC`. `square`

### Theorem 12.2: `CPSC` Proves The Remaining Paper-13 Gates

If `CPSC` holds, then

```text
RPF(s_0,L), KP_dec(s_0,rho,L), SUB(s_0,rho,L)
```

hold, and the block-scale Creutz anchor has positive reserve.

Proof.

`RCE` plus `RKP` proves `RPF` by Theorem 7.3. Combined decoration smallness
proves `KP_dec` by Theorem 8.3. Positive surface reserve proves `SUB` by
Theorem 10.2. Positive `M_15` proves the transported Creutz anchor survives
by Theorem 11.2. `square`

### Corollary 12.2A: Numerical Paper-15 Closure

If `nCPSC` is positive, then

```text
RPF(s_0,L), KP_dec(s_0,rho,L), SUB(s_0,rho,L)
```

hold, and the Creutz anchor has positive reserve.

Proof.

Theorem 12.1B gives `CPSC`; Theorem 12.2 gives the three gates and the
positive Creutz reserve. `square`

### Corollary 12.3: Paper 14 Plus Paper 15 Prove `ACSB`

Assume Paper 14 proves `FBE`, and Paper 15 proves `CPSC`. Then all six
Paper-13 gates hold:

```text
BC + CE + WP + RPF + KP_dec + SUB.
```

Consequently `ACSB(s_0,rho,L)` holds.

Proof.

Paper 14 gives `BC`, `CE`, and `WP`. Theorem 12.2 gives `RPF`, `KP_dec`, and
`SUB`. Paper 13's six-gate theorem gives `ACSB`. `square`

### Corollary 12.4: Export To Paper 16

Under the hypotheses of Corollary 12.3, Paper 16 may use:

1. `ACSB(s_0,rho,L)`;
2. the exact Paper-13 implication chain

   ```text
   ACSB -> SB -> surface-polymer entry -> exact RG entry -> RSB;
   ```

3. the positive Creutz margin reserve `M_15`;
4. the full list of imported constructive estimates.

Paper 16 may not assume a mass gap, confinement, or a Hilbert-space spectrum.

### Definition 12.5: Paper-15 Export Package `X_15`

When `nCPSC` is positive, Paper 15 exports:

```text
X_15(s_0,L,rho)
 =
 (
   X_14,
   nCPSC,
   RCE(A_AF,mu_AF,r_*),
   RKP(A_AF,mu_AF,m),
   eta_dec^{bd},
   D_*,
   M_SUB^{bd},
   M_15^{bd},
   ACSB(s_0,rho,L),
   RSB_route(s_0,rho,L)
 ).
```

Here `RSB_route` denotes the declared Paper-13 implication chain

```text
ACSB -> SB -> surface-polymer entry -> exact RG entry -> RSB.
```

This is an export package of record-law estimates. It is not a Hilbert-space
spectrum, a mass gap, or a confinement theorem.

### Theorem 12.6: Final Paper-15 Numerical Closure Theorem

Assume Paper 14 proves `FBE` for `X_14`, and assume the Paper-15 numerical
certificate `nCPSC` is positive. Then:

```text
BC + CE + WP + RPF + KP_dec + SUB
```

hold on the declared finite block battery. Consequently `ACSB(s_0,rho,L)`
holds, the Paper-13 route to `RSB(s_0,rho,L)` is open, and the export package
`X_15(s_0,L,rho)` is well defined.

Proof.

Paper 14's `FBE` gives `BC`, `CE`, and `WP`. Positive `nCPSC` gives
`CPSC` by Theorem 12.1B. Theorem 12.2 gives `RPF`, `KP_dec`, `SUB`, and the
positive Creutz reserve. Paper 13's six-gate theorem gives `ACSB`; Paper 13's
declared implication chain gives the `RSB_route`. Definition 12.5 collects
the resulting constants and gates into `X_15`. `square`

## 12A. Proof Dependency Map

The finished proof has the following dependency chain:

```text
Paper 11 AF ledger
  -> local-RG summability S_RG and mu_RG

Paper 12 loop ledger
  -> K_12^*, mu_12, perimeter/cusp-renormalized connected localization

Paper 14 finite-block entry
  -> X_14, u_-, u_+, Tail_CE, E_14^*, BC, CE, WP

Paper 15 Sections 6--7
  -> AFRCE -> RCE -> RKP -> RPF

Paper 15 Sections 8--9
  -> eta_dec^{bd}<1 -> KP_dec and explicit decoration losses

Paper 15 Sections 10--11
  -> M_SUB^{bd}>0 and M_15^{bd}>0

Paper 15 Section 12
  -> nCPSC -> CPSC -> ACSB -> RSB_route.
```

Every arrow is an implication between declared record laws or declared
finite-battery constants. No arrow composes an undeclared partial kernel.

## 12B. Barandes-Alignment Audit

Paper 15 obeys the following operational rules:

1. The primitive object is the whole-process pushed-forward block record law
   `nu_{s_0,L}`.
2. Polymer activities are expansions of connected record cumulants, not
   additional ontology.
3. Gauge-fixed variables enter only through Paper-11/Paper-12 certificates,
   never as hidden beables.
4. The product reference `nu_0` is a comparison record law, not an
   independent microscopic dynamics.
5. The KP expansion is a Banach-norm estimate for finite record algebras.
6. The Creutz anchor is an operational Wilson-loop/character record margin,
   not yet a representation-theoretic confinement statement.
7. Mass gap, confinement, and Hilbert-space reconstruction remain downstream
   representation-level problems.

## 13. Failure Ledger

Paper 15 can fail in the following precise ways:

1. **Raw-margin failure:** `mu_base<=lambda_gen+lambda_tree`, so `AFRCE`
   does not imply a positive residual decay exponent.
2. **Generator-choice failure:** the declared record basis is too microscopic,
   producing a positive `lambda_gen`; the Barandes-aligned repair is to
   declare the actual operational block monomials as generators when this is
   physically justified.
3. **KP-entropy failure:** `mu_AF<=h_an` or
   `eta_res^{bd}>=1`, so residual decay exists but is too weak to beat
   polymer entropy.
4. **Character-tail failure:** `eta_ch^{bd}` consumes the remaining KP
   margin, so `eta_dec^{bd}>=1`.
5. **Surface-entropy failure:** `M_SUB^{bd}<=0`, meaning the leading
   coefficient window is too large relative to surface entropy and
   decoration growth.
6. **Creutz-margin failure:** `M_15^{bd}<=0`, meaning the block-scale Creutz
   margin is consumed by decorations or transport losses.
7. **Wrong-norm failure:** the argument accidentally demands naive sup-norm
   volume decay for arbitrary macroscopic observables instead of the
   coefficient-normalized generator/activity envelope.
8. **Whole-process compatibility failure:** constants depend on a regulator,
   chart, or undeclared subprocess factorization.

These failures are record-law failures. None of them is repaired by
reinterpreting residuals as virtual particles or by composing unrecorded
microscopic kernels.

## 14. Honest Status

Paper 15 is now a rigorous reduction paper. It proves:

```text
Paper-14 FBE
+ AFRCE, hence coefficient-normalized residual connected-cumulant KP
+ character decoration smallness
+ surface subcriticality reserve
+ Creutz margin reserve
=> RPF + KP_dec + SUB
=> ACSB
=> Paper-13 RSB route.
```

The main advance over the first draft is that `RCE` has been repaired and
reduced. The paper no longer asks for impossible volume-exponential decay of
all bounded macroscopic observables. It asks for coefficient-normalized
generator decay, which is the input actually needed by the polymer KP
argument. Theorem 6A.6 proves this `RCE` from the named `AFRCE` certificate:
Paper-11 AF local-RG summability, Paper-12 renormalized connected-polymer
localization, Paper-14 block projection, product-reference locality, and a
positive raw margin after generator/tree losses.

The first numerical layer is also explicit now. Definition 6B.1 lists the
constants entering `A_AF` and `mu_AF`; Theorem 6B.3 proves the raw-margin
criterion; Lemma 7.1A and Theorem 7.2A reduce the first KP gate to the
single inequality

```text
C_cum(d,r_*) A_AF
exp(-delta_KP)/(1-exp(-delta_KP))
< 1.
```

The full numerical closure layer is now explicit as well. Theorem 8A.2 turns
character-tail control into `KP_dec`; Theorem 10A.2 turns the explicit
surface constant `D_*` into `SUB`; Theorem 11A.3 turns the explicit
decoration and transport losses into a positive Creutz reserve; and Theorem
12.1B packages all of this into the numerical certificate `nCPSC`. The final
output is Theorem 12.6: Paper-14 `FBE` plus positive `nCPSC` gives all six
Paper-13 `ACSB` gates, opens the declared route to `RSB`, and exports the
finite record-law package `X_15`.

It does not prove actual four-dimensional continuum `SU(N)` Yang-Mills
satisfies `AFRCE`, KP smallness, surface subcriticality, or positive Creutz
reserve. Those remain constructive Yang-Mills inputs or later paper targets.

Thus Paper 15 is finished as a conditional finite-battery bridge theorem. The
next paper should assemble `X_15` into the nonperturbative continuum
Yang-Mills closure theorem, keeping all remaining imported inputs explicit.
Mass gap and confinement remain later representation-level or large-loop
consequences, not assumptions of this paper.
